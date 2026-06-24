"""Produce a cleaned recipe in the recipe-editor IMPORT format.

The CRMA extract is the full API response (envelope + metadata) whose
``recipeDefinition`` holds the actual recipe graph. The recipe editor, however,
imports/exports only the bare definition object ``{version, nodes, ui}`` (no
``runMode``, no API envelope). So we emit that: the definition with the unused
fields trimmed from its load nodes, and the ``ui`` block kept consistent (no
hiddenColumns references to removed columns).

Output is a PROPOSAL written to recipes/output/ (``<recipe>.editor.json`` +
``<recipe>.diff.md``). We do NOT auto-PUT back to the org; the editor.json is
imported by a human in the recipe editor, then both versions are run and
compared for identical output.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from .recipe_analyzer import RecipeAnalysis

OUTPUT_DIR = Path("recipes/output")
# keys of the editor import/export format, in order
_EDITOR_KEYS = ("version", "nodes", "ui")


def _field_name(f) -> str:
    return f if isinstance(f, str) else (f.get("name", "") if isinstance(f, dict) else "")


def _hidden_col_removed(entry, removed: set[str]) -> bool:
    """True if a ui.hiddenColumns entry references a removed column.

    hiddenColumns entries may be bare strings or dicts keyed by name/column/
    field; we match against the removed field names and their bare tails."""
    if isinstance(entry, str):
        return entry in removed
    if isinstance(entry, dict):
        for k in ("name", "column", "field", "columnName", "fieldName"):
            v = entry.get(k)
            if isinstance(v, str) and v in removed:
                return True
    return False


def build_editor_recipe(recipe: dict, analysis: RecipeAnalysis) -> dict:
    """Return the editor-import definition ``{version, nodes, ui}`` with unused
    load-node fields removed and ui.hiddenColumns kept consistent."""
    defn = recipe.get("recipeDefinition", recipe)
    defn = copy.deepcopy(defn)
    nodes = defn.get("nodes", {}) or {}

    removed: set[str] = set()
    for o in analysis.objects:
        drop = set(o.unused)
        if not drop or o.node_id not in nodes:
            continue
        params = nodes[o.node_id].get("parameters", {}) or {}
        params["fields"] = [f for f in params.get("fields", [])
                            if _field_name(f) not in drop]
        removed |= drop
    # also match ui references that use the bare tail of a qualified field
    removed_cols = removed | {r.rsplit(".", 1)[-1] for r in removed}

    ui = defn.get("ui", {}) or {}
    hidden = ui.get("hiddenColumns")
    if isinstance(hidden, list) and hidden:
        ui["hiddenColumns"] = [h for h in hidden
                               if not _hidden_col_removed(h, removed_cols)]

    return {"version": defn.get("version"), "nodes": nodes, "ui": ui}


def write_cleaned(recipe_label: str, recipe: dict, analysis: RecipeAnalysis) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    editor = build_editor_recipe(recipe, analysis)
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in recipe_label)

    (OUTPUT_DIR / f"{safe}.editor.json").write_text(json.dumps(editor, indent=2))

    diff_lines = [f"# Cleanup proposal: {recipe_label}", ""]
    for o in analysis.objects:
        diff_lines.append(f"## {o.object_name}  (node {o.node_id})")
        diff_lines.append(f"- loaded: {len(o.loaded)}  used: {len(o.used)}  remove: {len(o.unused)}")
        for f in o.unused:
            diff_lines.append(f"  - REMOVE  {f}")
        diff_lines.append("")
    (OUTPUT_DIR / f"{safe}.diff.md").write_text("\n".join(diff_lines))

    return {"editor_path": str(OUTPUT_DIR / f"{safe}.editor.json"),
            "diff_path": str(OUTPUT_DIR / f"{safe}.diff.md"),
            "removed": analysis.total_unused, "loaded": analysis.total_loaded}
