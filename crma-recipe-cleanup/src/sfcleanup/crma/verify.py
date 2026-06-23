"""Before/after equivalence check for a cleaned recipe.

The rule Carlos set: after removing unused input fields, the recipe must still
produce the SAME output — same number of rows per output dataset (and ideally
the same column values). This module captures a row-count *snapshot* of every
dataset a recipe writes, so you can compare a baseline (before cleanup) against
the cleaned run (after) and get a per-dataset PASS/FAIL.

Typical flow:
  1) BEFORE touching anything, snapshot the live outputs:
       crma_cli verify snapshot --recipe recipes/input/<recipe>.json --label before
  2) Apply the field removals to a Save-As copy of the recipe and run it. If the
     copy writes to renamed datasets, pass --suffix (e.g. _CLEANTEST) so the
     snapshot reads the copy's outputs.
       crma_cli verify snapshot --recipe recipes/input/<recipe>.json \
                --suffix _CLEANTEST --label after
  3) Compare the two snapshots:
       crma_cli verify compare --before <before.json> --after <after.json>

Row counts are queried with SAQL via the CRM Analytics query API; works under
both CLI and JWT auth through the shared transport in auth.py.
"""
from __future__ import annotations

import json
from pathlib import Path

from ..auth import SfSession, rest_get, rest_post

VERIFY_DIR = Path("recipes/verify")


def recipe_output_datasets(recipe: dict) -> list[str]:
    """Return the dataset names a recipe writes (its `save` node targets)."""
    defn = recipe.get("recipeDefinition", recipe)
    nodes = defn.get("nodes", {})
    out: list[str] = []
    for node in nodes.values():
        if node.get("action") != "save":
            continue
        params = node.get("parameters", {})
        dataset = params.get("dataset")
        name = dataset.get("name") if isinstance(dataset, dict) else params.get("name")
        if name:
            out.append(name)
    # stable, de-duplicated
    return sorted(dict.fromkeys(out))


def resolve_dataset(session: SfSession, name: str, api_version: str) -> dict | None:
    """Find a dataset by exact name; return {id, version, name} or None."""
    body = rest_get(session, f"/services/data/v{api_version}/wave/datasets",
                    params={"q": name})
    datasets = body.get("datasets", body.get("items", [])) if isinstance(body, dict) else []
    exact = [d for d in datasets if d.get("name") == name]
    cand = exact[0] if exact else (datasets[0] if datasets else None)
    if not cand:
        return None
    return {"id": cand.get("id"), "version": cand.get("currentVersionId"),
            "name": cand.get("name")}


def row_count(session: SfSession, dataset: dict, api_version: str) -> int:
    """Total row count of a dataset via a SAQL count-all query."""
    saql = (f'q = load "{dataset["id"]}/{dataset["version"]}";'
            ' q = group q by all;'
            " q = foreach q generate count() as 'c';")
    res = rest_post(session, f"/services/data/v{api_version}/wave/query",
                    {"query": saql})
    records = res["results"]["records"] if isinstance(res, dict) else []
    return int(records[0]["c"]) if records else 0


def snapshot(session: SfSession, recipe_path: Path, label: str,
             suffix: str = "", api_version: str = "62.0") -> dict:
    """Capture row counts for every output dataset of `recipe_path`.

    `suffix` is appended to each target name (use it when the cleaned copy writes
    to renamed datasets, e.g. `Fiberleads_CLEANTEST`).
    """
    recipe = json.loads(recipe_path.read_text())
    targets = recipe_output_datasets(recipe)
    results: dict[str, dict] = {}
    for target in targets:
        looked_up = f"{target}{suffix}"
        ds = resolve_dataset(session, looked_up, api_version)
        if not ds:
            results[target] = {"looked_up": looked_up, "found": False, "rows": None}
            continue
        results[target] = {"looked_up": looked_up, "found": True,
                            "rows": row_count(session, ds, api_version),
                            "dataset_id": ds["id"]}
    snap = {"recipe": recipe_path.stem, "label": label, "suffix": suffix,
            "outputs": results}
    VERIFY_DIR.mkdir(parents=True, exist_ok=True)
    out_path = VERIFY_DIR / f"{recipe_path.stem}__{label}.json"
    out_path.write_text(json.dumps(snap, indent=2))
    snap["_path"] = str(out_path)
    return snap


def compare(before: dict, after: dict) -> dict:
    """Diff two snapshots by logical target name. Returns per-dataset verdicts."""
    rows = []
    targets = sorted(set(before["outputs"]) | set(after["outputs"]))
    n_pass = n_fail = 0
    for t in targets:
        b = before["outputs"].get(t, {})
        a = after["outputs"].get(t, {})
        br, ar = b.get("rows"), a.get("rows")
        if not b.get("found") or not a.get("found"):
            verdict = "MISSING"
        elif br == ar:
            verdict = "PASS"
        else:
            verdict = "FAIL"
        n_pass += verdict == "PASS"
        n_fail += verdict in ("FAIL", "MISSING")
        rows.append({"dataset": t, "before": br, "after": ar, "verdict": verdict})
    return {"rows": rows, "pass": n_pass, "fail": n_fail,
            "ok": n_fail == 0 and n_pass > 0}
