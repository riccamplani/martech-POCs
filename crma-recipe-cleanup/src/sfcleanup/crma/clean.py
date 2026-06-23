"""Produce a cleaned recipe JSON by removing unused fields from load nodes.

Output is a PROPOSAL: the cleaned JSON plus a diff written to recipes/output/.
We do NOT auto-PUT back to the org, because modifying recipe file content via API
is not officially supported and could break a production recipe. The supported,
verified-safe loop is: apply the proposed removals in the recipe editor (or a
supported update), then run both old/new versions and confirm identical output.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from .recipe_analyzer import RecipeAnalysis, _find_nodes

OUTPUT_DIR = Path("recipes/output")


def build_clean_recipe(recipe: dict, analysis: RecipeAnalysis) -> dict:
    cleaned = copy.deepcopy(recipe)
    nodes = _find_nodes(cleaned)
    unused_by_node = {o.node_id: set(o.unused) for o in analysis.objects}
    for nid, drop in unused_by_node.items():
        if not drop:
            continue
        params = nodes[nid].get("parameters", {}) or {}
        raw = params.get("fields", [])
        params["fields"] = [
            f for f in raw
            if (f if isinstance(f, str) else f.get("name")) not in drop
        ]
    return cleaned


def write_cleaned(recipe_label: str, recipe: dict, analysis: RecipeAnalysis) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cleaned = build_clean_recipe(recipe, analysis)
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in recipe_label)

    (OUTPUT_DIR / f"{safe}.cleaned.json").write_text(json.dumps(cleaned, indent=2))

    diff_lines = [f"# Cleanup proposal: {recipe_label}", ""]
    for o in analysis.objects:
        diff_lines.append(f"## {o.object_name}  (node {o.node_id})")
        diff_lines.append(f"- loaded: {len(o.loaded)}  used: {len(o.used)}  remove: {len(o.unused)}")
        for f in o.unused:
            diff_lines.append(f"  - REMOVE  {f}")
        diff_lines.append("")
    (OUTPUT_DIR / f"{safe}.diff.md").write_text("\n".join(diff_lines))

    return {"cleaned_path": str(OUTPUT_DIR / f"{safe}.cleaned.json"),
            "diff_path": str(OUTPUT_DIR / f"{safe}.diff.md"),
            "removed": analysis.total_unused, "loaded": analysis.total_loaded}
