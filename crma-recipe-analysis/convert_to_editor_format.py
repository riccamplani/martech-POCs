#!/usr/bin/env python3
"""Convert raw CRMA recipe extracts (Analytics API response) into the
recipe-editor import format `{version, nodes, ui}`.

The Analytics REST API returns each recipe wrapped in an envelope
(`recipeDefinition` + metadata + `runMode`). The recipe editor imports/exports
only the bare definition. This strips the envelope — no field trimming, the
faithful original — so the files re-import cleanly.

Usage:
    python convert_to_editor_format.py <src_dir> <dst_dir>

Stdlib only; no dependencies.
"""
import glob
import json
import os
import sys


def to_editor(recipe: dict) -> dict:
    defn = recipe.get("recipeDefinition", recipe)
    return {
        "version": defn.get("version"),
        "nodes": defn.get("nodes", {}),
        "ui": defn.get("ui", {}),
    }


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: python convert_to_editor_format.py <src_dir> <dst_dir>")
    src, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    n = 0
    for path in sorted(glob.glob(os.path.join(src, "*.json"))):
        recipe = json.load(open(path))
        editor = to_editor(recipe)
        out = os.path.join(dst, os.path.basename(path))
        json.dump(editor, open(out, "w"), indent=2, ensure_ascii=False)
        n += 1
    print(f"converted {n} recipe(s) -> {dst}")


if __name__ == "__main__":
    main()
