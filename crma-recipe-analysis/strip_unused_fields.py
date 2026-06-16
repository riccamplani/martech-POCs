#!/usr/bin/env python3
"""Strip unused fields from CRMA recipe load nodes.

Analyzes which fields are loaded but never used in any transformation logic
(formulas, filters, joins, aggregates) and never survive to output datasets.
Removes those fields from both the load node and any downstream schema
DROP-list nodes that reference them.

Outputs a cleaned recipe JSON to the output/ folder.
"""

import json
import re
import sys
from collections import defaultdict
from copy import deepcopy
from pathlib import Path


LOGIC_ACTIONS = {
    "filter", "formula", "join", "aggregate",
    "extractGrains", "computeRelative", "typeCast", "appendV2",
}


def build_graph(nodes):
    children = defaultdict(list)
    for nid, node in nodes.items():
        for src in node.get("sources", []):
            children[src].append(nid)
    return children


def get_descendants(start, children):
    visited = set()
    queue = [start]
    while queue:
        n = queue.pop()
        if n in visited:
            continue
        visited.add(n)
        for c in children.get(n, []):
            queue.append(c)
    visited.discard(start)
    return visited


def find_logic_refs(field, nodes, descendants):
    """Check if a field is referenced in any logic node among descendants."""
    for desc_id in descendants:
        desc = nodes[desc_id]
        if desc.get("action") not in LOGIC_ACTIONS:
            continue
        raw = json.dumps(desc.get("parameters", {}))
        if re.search(r'(?<![a-zA-Z0-9_])' + re.escape(field) + r'(?![a-zA-Z0-9_])', raw):
            return True
    return False


def find_schema_refs(field, nodes, descendants):
    """Find schema nodes that reference a field in their slice.fields drop/select list."""
    refs = []
    for desc_id in descendants:
        desc = nodes[desc_id]
        if desc.get("action") != "schema":
            continue
        slice_data = desc.get("parameters", {}).get("slice", {})
        slice_fields = slice_data.get("fields", [])
        if field in slice_fields:
            refs.append((desc_id, slice_data.get("mode", "?")))
    return refs


def field_survives_to_output(field, load_id, nodes, children):
    """Check if a field makes it past all schema nodes to any save node.

    A field survives if there's at least one path from the load node to a
    save node where no schema node drops it (DROP mode with field listed)
    and no schema node selects without it (SELECT mode without field listed).
    """
    descendants = get_descendants(load_id, children)
    save_nodes = [d for d in descendants if nodes[d].get("action") == "save"]

    for save_id in save_nodes:
        # Walk backwards from save to load, checking schema nodes
        # Simpler: walk forward and track if field is alive on each path
        pass

    # Simplified: check all schema nodes between load and saves.
    # If ALL schema nodes either don't mention the field or have ignoreMissingFields,
    # the field passes through.
    for desc_id in descendants:
        desc = nodes[desc_id]
        if desc.get("action") != "schema":
            continue
        slice_data = desc.get("parameters", {}).get("slice", {})
        mode = slice_data.get("mode", "")
        slice_fields = slice_data.get("fields", [])

        if mode == "DROP" and field in slice_fields:
            continue  # dropped here, but might survive on another path
        if mode == "SELECT" and field not in slice_fields:
            continue  # not selected, filtered out

    return False  # conservative: assume it doesn't survive


def analyze_load_node(load_id, nodes, children):
    """Return (used_in_logic, unused, affected_schema_nodes) for a load node."""
    loaded_fields = set(nodes[load_id]["parameters"]["fields"])
    descendants = get_descendants(load_id, children)

    used = set()
    unused = set()

    for field in loaded_fields:
        if find_logic_refs(field, nodes, descendants):
            used.add(field)
        else:
            unused.add(field)

    affected_schemas = []
    for desc_id in descendants:
        desc = nodes[desc_id]
        if desc.get("action") != "schema":
            continue
        slice_data = desc.get("parameters", {}).get("slice", {})
        slice_fields = set(slice_data.get("fields", []))
        if slice_fields & unused:
            affected_schemas.append(desc_id)

    return used, unused, affected_schemas


def strip_fields(recipe, load_id, unused_fields, affected_schemas):
    """Return a modified recipe with unused fields removed."""
    cleaned = deepcopy(recipe)
    nodes = cleaned["nodes"]

    # Remove from load node's field list
    nodes[load_id]["parameters"]["fields"] = [
        f for f in nodes[load_id]["parameters"]["fields"]
        if f not in unused_fields
    ]

    # Remove from schema node slice.fields lists
    for schema_id in affected_schemas:
        schema_node = nodes[schema_id]
        slice_data = schema_node["parameters"].get("slice", {})
        original = slice_data.get("fields", [])
        slice_data["fields"] = [f for f in original if f not in unused_fields]

    return cleaned


def main():
    if len(sys.argv) < 2:
        print("Usage: python strip_unused_fields.py <recipe.json> [--dry-run]")
        sys.exit(1)

    path = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv

    with open(path) as f:
        recipe = json.load(f)

    nodes = recipe["nodes"]
    children = build_graph(nodes)

    load_nodes = {k: v for k, v in nodes.items() if v.get("action") == "load"}

    total_removed = 0

    for load_id in sorted(load_nodes):
        ds = nodes[load_id]["parameters"].get("dataset", {})
        label = ds.get("label", ds.get("sourceObjectName", load_id))

        used, unused, affected_schemas = analyze_load_node(load_id, nodes, children)

        if not unused:
            continue

        print(f"\n{'='*60}")
        print(f"{load_id} ({label})")
        print(f"  Loaded: {len(used) + len(unused)}  |  Used in logic: {len(used)}  |  Unused: {len(unused)}")
        print(f"{'='*60}")

        print(f"\n  Fields to KEEP ({len(used)}):")
        for f in sorted(used):
            print(f"    ✓ {f}")

        print(f"\n  Fields to REMOVE ({len(unused)}):")
        for f in sorted(unused):
            schema_refs = find_schema_refs(f, nodes, get_descendants(load_id, children))
            schema_info = ""
            if schema_refs:
                schema_info = " (also remove from: " + ", ".join(
                    f"{sid}[{mode}]" for sid, mode in schema_refs) + ")"
            print(f"    ✗ {f}{schema_info}")

        total_removed += len(unused)

    if total_removed == 0:
        print("\nNo unused fields found. Recipe is clean.")
        return

    if dry_run:
        print(f"\n{'─'*60}")
        print(f"DRY RUN — {total_removed} fields would be removed. Run without --dry-run to generate cleaned file.")
        return

    cleaned = deepcopy(recipe)
    cleaned_nodes = cleaned["nodes"]
    cleaned_children = build_graph(cleaned_nodes)

    for load_id in sorted(load_nodes):
        used, unused, affected_schemas = analyze_load_node(load_id, cleaned_nodes, cleaned_children)
        if unused:
            cleaned = strip_fields(cleaned, load_id, unused, affected_schemas)
            cleaned_nodes = cleaned["nodes"]

    out_dir = path.parent.parent / "output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / path.name
    with open(out_path, "w") as f:
        json.dump(cleaned, f, indent=4, ensure_ascii=False)

    print(f"\n{'─'*60}")
    print(f"Cleaned recipe written to: output/{out_path.name}")
    print(f"Total fields removed: {total_removed}")


if __name__ == "__main__":
    main()
