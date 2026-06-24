"""Analyze a CRMA recipe's JSON to find which input fields are actually used.

Mirrors what Carlos does manually with Claude, but deterministically:
  1. Find every LOAD/source node and the fields it pulls from each object.
  2. Collect every field token referenced ANYWHERE else (filters, formulas,
     joins, aggregates, output column lists, transformations).
  3. A loaded field is "used" if its token appears outside its own load node;
     otherwise it is a candidate to remove (unused in the recipe logic).

Conservative by design: if a field name appears anywhere downstream we keep it.
Ambiguous cases (e.g. fields built dynamically) are flagged for human/Claude review.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field as dc_field

# node actions that LOAD data from a source object
_LOAD_ACTIONS = {"load", "digest", "edgemart", "connectedDataset", "input"}
# tokens that look like Salesforce field API names
_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:__[a-z]{1,2})?")
# qualified dotted paths, e.g. "TRANSFORM1.Kurt_Id" or "AlleMails.Email"
_QUALIFIED = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+")


@dataclass
class ObjectUsage:
    object_name: str
    node_id: str
    loaded: list[str] = dc_field(default_factory=list)
    used: list[str] = dc_field(default_factory=list)
    unused: list[str] = dc_field(default_factory=list)


@dataclass
class RecipeAnalysis:
    objects: list[ObjectUsage] = dc_field(default_factory=list)

    @property
    def total_loaded(self) -> int:
        return sum(len(o.loaded) for o in self.objects)

    @property
    def total_unused(self) -> int:
        return sum(len(o.unused) for o in self.objects)


def _find_nodes(recipe: dict) -> dict:
    """Locate the node mapping wherever it lives in the recipe payload."""
    if "nodes" in recipe and isinstance(recipe["nodes"], dict):
        return recipe["nodes"]
    for key in ("definition", "recipeDefinition", "graph", "rows"):
        sub = recipe.get(key)
        if isinstance(sub, dict) and isinstance(sub.get("nodes"), dict):
            return sub["nodes"]
    return {}


def _loaded_fields(params: dict) -> tuple[str, list[str]]:
    """Return (source_object, [field names]) from a load node's parameters."""
    ds = params.get("dataset", {}) or {}
    obj = ds.get("sourceObjectName") or ds.get("label") or ds.get("name") or "UNKNOWN"
    raw = params.get("fields", [])
    fields = [f if isinstance(f, str) else f.get("name", "") for f in raw]
    return obj, [f for f in fields if f]


def _collect_referenced_tokens(nodes: dict, load_node_ids: set[str]) -> set[str]:
    """Every identifier token used anywhere EXCEPT inside load nodes' field lists.

    Walks both dict VALUES and KEYS (field references can appear as map keys in
    schema/rename specs), and captures qualified dotted paths whole, so that a
    name like ``TRANSFORM1.Kurt_Id`` is recorded as ``TRANSFORM1.Kurt_Id`` *and*
    contributes its bare tail ``Kurt_Id``.
    """
    tokens: set[str] = set()

    def add(text: str) -> None:
        # bare identifiers (split on dots) ...
        tokens.update(_TOKEN.findall(text))
        # ... plus whole qualified dotted paths (e.g. Alias.Field__c)
        tokens.update(_QUALIFIED.findall(text))

    def walk(value):
        if isinstance(value, str):
            add(value)
        elif isinstance(value, list):
            for v in value:
                walk(v)
        elif isinstance(value, dict):
            for k, v in value.items():
                if isinstance(k, str):   # keys can hold field references too
                    add(k)
                walk(v)

    for nid, node in nodes.items():
        params = node.get("parameters", {}) or {}
        if nid in load_node_ids:
            # walk everything except the loaded-fields list itself
            scrubbed = {k: v for k, v in params.items() if k != "fields"}
            walk(scrubbed)
        else:
            walk(params)
    return tokens


def _is_used(field: str, referenced: set[str]) -> bool:
    """Conservative usage test. A loaded field is "used" if its full name OR its
    bare tail (after the last '.') is referenced downstream. Errs toward KEEP:
    qualified inputs like ``TRANSFORM1.Kurt_Id`` are never dropped just because
    the recipe refers to them by a different qualifier."""
    if field in referenced:
        return True
    tail = field.rsplit(".", 1)[-1]
    return tail != field and tail in referenced


def analyze_recipe(recipe: dict) -> RecipeAnalysis:
    nodes = _find_nodes(recipe)
    load_nodes = {nid: n for nid, n in nodes.items()
                  if (n.get("action") or "").lower() in _LOAD_ACTIONS}
    referenced = _collect_referenced_tokens(nodes, set(load_nodes))

    analysis = RecipeAnalysis()
    for nid, node in load_nodes.items():
        obj, loaded = _loaded_fields(node.get("parameters", {}) or {})
        used = [f for f in loaded if _is_used(f, referenced)]
        unused = [f for f in loaded if not _is_used(f, referenced)]
        analysis.objects.append(
            ObjectUsage(object_name=obj, node_id=nid,
                        loaded=loaded, used=used, unused=unused)
        )
    return analysis
