#!/usr/bin/env python3
"""Parse and summarize Salesforce CRMA recipe JSON files."""

import json
import sys
from collections import Counter
from pathlib import Path


def load_recipe(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def build_edges(nodes: dict) -> list[tuple[str, str]]:
    """Build edge list from each node's 'sources' field."""
    edges = []
    for node_id, node in nodes.items():
        for src in node.get("sources", []):
            edges.append((src, node_id))
    return edges


def find_roots(nodes: dict, edges: list[tuple[str, str]]) -> list[str]:
    """Nodes with no incoming edges (load/source nodes)."""
    targets = {tgt for _, tgt in edges}
    return sorted(nid for nid in nodes if nid not in targets)


def find_terminals(nodes: dict, edges: list[tuple[str, str]]) -> list[str]:
    """Nodes with no outgoing edges (save/output nodes)."""
    sources = {src for src, _ in edges}
    return sorted(nid for nid in nodes if nid not in sources)


def summarize_data_sources(nodes: dict) -> None:
    """Print details about load nodes — what datasets feed the recipe."""
    load_nodes = {k: v for k, v in nodes.items() if v.get("action") == "load"}
    if not load_nodes:
        return
    print("\n  Data sources:")
    for node_id, node in sorted(load_nodes.items()):
        ds = node.get("parameters", {}).get("dataset", {})
        label = ds.get("label", ds.get("sourceObjectName", "?"))
        conn = ds.get("connectionName", "?")
        fields = node.get("parameters", {}).get("fields", [])
        print(f"    {node_id}: {label} ({conn}) — {len(fields)} fields")


def summarize_outputs(nodes: dict, terminals: list[str]) -> None:
    """Print details about save/output nodes."""
    print("\n  Outputs:")
    for node_id in terminals:
        node = nodes[node_id]
        action = node.get("action", "?")
        params = node.get("parameters", {})
        ds = params.get("dataset", {})
        label = ds.get("label", ds.get("name", node_id))
        print(f"    {node_id} ({action}): {label}")


def summarize_formulas(nodes: dict) -> None:
    """Print computed/formula columns."""
    formula_nodes = {k: v for k, v in nodes.items() if v.get("action") == "formula"}
    if not formula_nodes:
        return
    print(f"\n  Computed columns ({len(formula_nodes)} formula nodes):")
    for node_id, node in sorted(formula_nodes.items()):
        fields = node.get("parameters", {}).get("fields", [])
        for f in fields:
            name = f.get("name", "?")
            expr = f.get("formulaExpression", "")
            preview = expr.replace("\n", " ")[:80]
            print(f"    {node_id}.{name}: {preview}")


def summarize_recipe(recipe: dict, filename: str) -> None:
    print(f"\n{'='*60}")
    print(f"Recipe: {filename}")
    print(f"{'='*60}")

    version = recipe.get("version", "?")
    print(f"  Version: {version}")

    nodes = recipe.get("nodes", {})
    edges = build_edges(nodes)
    roots = find_roots(nodes, edges)
    terminals = find_terminals(nodes, edges)

    print(f"  Nodes: {len(nodes)}")
    print(f"  Edges: {len(edges)}")

    actions = Counter(n.get("action") for n in nodes.values())
    print("\n  Node types:")
    for action, count in actions.most_common():
        print(f"    {action}: {count}")

    summarize_data_sources(nodes)
    summarize_outputs(nodes, terminals)
    summarize_formulas(nodes)

    print(f"\n  Pipeline roots ({len(roots)}): {', '.join(roots)}")
    print(f"  Pipeline terminals ({len(terminals)}): {', '.join(terminals)}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_recipe.py <recipe.json | directory/>")
        sys.exit(1)

    target = Path(sys.argv[1])

    if target.is_dir():
        files = sorted(target.glob("*.json"))
        if not files:
            print(f"No JSON files found in {target}")
            sys.exit(1)
    else:
        files = [target]

    for filepath in files:
        recipe = load_recipe(filepath)
        summarize_recipe(recipe, filepath.name)


if __name__ == "__main__":
    main()
