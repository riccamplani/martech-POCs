"""CRMA recipe workflow CLI.

  # 1) EXTRACT (the priority): download in-scope recipes to recipes/input/
  python -m sfcleanup.crma_cli extract --scope recipes/scope.txt
  python -m sfcleanup.crma_cli extract --all

  # 2) ANALYZE + propose cleanup for everything in recipes/input/
  python -m sfcleanup.crma_cli analyze

`recipes/scope.txt` = one recipe name (or id) per line, taken from Carlos's
Excel list of in-scope recipes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

from pathlib import Path as _Path

from .auth import get_session, SalesforceRestError
from .crma.client import list_recipes, get_recipe, save_recipe_json, INPUT_DIR
from .crma.recipe_analyzer import analyze_recipe
from .crma.clean import write_cleaned
from .crma.aggregate import aggregate as _aggregate
from .crma.report_xlsx import write_workbook

console = Console()


def _load_scope(path: str | None) -> set[str] | None:
    if not path:
        return None
    lines = Path(path).read_text().splitlines()
    return {ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")}


def extract(scope_path: str | None, take_all: bool) -> None:
    session = get_session()
    scope = _load_scope(scope_path)
    console.print("[bold]Listing recipes…[/bold]")
    try:
        recipes = list_recipes(session)
    except SalesforceRestError as e:
        console.print(f"[red]✗ CRM Analytics not accessible[/red] [{e.code}]: {e.message}")
        if e.code in ("FUNCTIONALITY_NOT_ENABLED", "720"):
            console.print("  → this user needs a CRM Analytics license assigned. "
                          "See [bold]scripts/ADMIN_REQUEST.md[/bold].")
        return
    console.print(f"  {len(recipes)} recipes in org")

    selected = recipes if (take_all or not scope) else [
        r for r in recipes if r["name"] in scope or r["id"] in scope or r["label"] in scope
    ]
    console.print(f"[bold]Extracting {len(selected)} recipe(s)…[/bold]")
    for r in selected:
        try:
            definition = get_recipe(session, r["id"])
            path = save_recipe_json(definition, r)
            console.print(f"  [green]✓[/green] {r['label']} -> {path}")
        except Exception as e:  # keep going; report failures
            console.print(f"  [red]✗[/red] {r['label']} ({r['id']}): {e}")


def analyze() -> None:
    files = sorted(INPUT_DIR.glob("*.json"))
    if not files:
        console.print("[yellow]No recipes in recipes/input/. Run `extract` first.[/yellow]")
        return
    table = Table(title="Recipe field usage")
    for c in ("Recipe", "Object", "Loaded", "Used", "Remove"):
        table.add_column(c)
    grand_loaded = grand_remove = 0
    for fp in files:
        recipe = json.loads(fp.read_text())
        result = analyze_recipe(recipe)
        label = fp.stem
        for o in result.objects:
            table.add_row(label, o.object_name, str(len(o.loaded)),
                          str(len(o.used)), f"[red]{len(o.unused)}[/red]")
        summary = write_cleaned(label, recipe, result)
        grand_loaded += result.total_loaded
        grand_remove += result.total_unused
    console.print(table)
    console.print(f"\n[bold]Totals[/bold]: loaded={grand_loaded}  "
                  f"proposed-to-remove={grand_remove}")
    console.print("Proposals written to recipes/output/ (review the .diff.md files).")


def aggregate_report(objects_yaml: str) -> None:
    rollups = _aggregate(INPUT_DIR, _Path(objects_yaml))
    if not rollups:
        console.print("[yellow]No in-scope objects found in recipes/input/. "
                      "Run `extract` and check config/objects.yaml.[/yellow]")
        return
    table = Table(title="Field usage across all in-scope recipes")
    for c in ("Group", "Object", "Loaded", "Used", "Unused"):
        table.add_column(c)
    for roll in sorted(rollups.values(), key=lambda r: (r.group, r.object_name)):
        table.add_row(roll.group, roll.object_name, str(len(roll.loaded)),
                      str(len(roll.used)), f"[red]{len(roll.unused)}[/red]")
    console.print(table)
    out = write_workbook(rollups, _Path("output/field_usage_by_object.xlsx"))
    console.print(f"[green]Workbook:[/green] {out}")


def verify(action: str, recipe: str | None, label: str, suffix: str,
           before: str | None, after: str | None) -> None:
    from .crma import verify as V
    from .auth import get_session
    if action == "snapshot":
        session = get_session()
        rp = _Path(recipe)
        console.print(f"[bold]Snapshotting outputs of {rp.stem}"
                      f"{' (suffix '+suffix+')' if suffix else ''}…[/bold]")
        snap = V.snapshot(session, rp, label=label, suffix=suffix)
        found = sum(1 for o in snap["outputs"].values() if o["found"])
        total_rows = sum(o["rows"] or 0 for o in snap["outputs"].values() if o["found"])
        console.print(f"  {found}/{len(snap['outputs'])} output datasets found, "
                      f"{total_rows} rows total")
        console.print(f"[green]Snapshot:[/green] {snap['_path']}")
        return
    # compare
    b = json.loads(_Path(before).read_text())
    a = json.loads(_Path(after).read_text())
    report = V.compare(b, a)
    table = Table(title=f"Equivalence: {b['label']} vs {a['label']}")
    for c in ("Output dataset", "Before", "After", "Verdict"):
        table.add_column(c)
    colour = {"PASS": "green", "FAIL": "red", "MISSING": "yellow"}
    for r in report["rows"]:
        v = r["verdict"]
        table.add_row(r["dataset"], str(r["before"]), str(r["after"]),
                      f"[{colour[v]}]{v}[/{colour[v]}]")
    console.print(table)
    verdict = "[green]✓ EQUIVALENT[/green]" if report["ok"] else "[red]✗ DIFFERENCES FOUND[/red]"
    console.print(f"\n{verdict}  (pass={report['pass']}  fail/missing={report['fail']})")


def main() -> None:
    p = argparse.ArgumentParser(prog="sfcleanup.crma")
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract", help="download recipes to recipes/input/")
    e.add_argument("--scope", help="file with in-scope recipe names/ids (one per line)")
    e.add_argument("--all", action="store_true", help="extract every recipe")
    sub.add_parser("analyze", help="analyze + propose cleanup for recipes/input/")
    a = sub.add_parser("aggregate", help="cross-recipe field usage -> Excel workbook")
    a.add_argument("--objects", default="config/objects.yaml")
    v = sub.add_parser("verify", help="before/after row-count equivalence check")
    vsub = v.add_subparsers(dest="vcmd", required=True)
    vs = vsub.add_parser("snapshot", help="record output row counts for a recipe")
    vs.add_argument("--recipe", required=True, help="path to extracted recipe JSON")
    vs.add_argument("--label", default="before", help="snapshot label (e.g. before/after)")
    vs.add_argument("--suffix", default="", help="suffix on cleaned output dataset names")
    vc = vsub.add_parser("compare", help="diff two snapshots")
    vc.add_argument("--before", required=True)
    vc.add_argument("--after", required=True)
    args = p.parse_args()
    if args.cmd == "extract":
        extract(args.scope, args.all)
    elif args.cmd == "analyze":
        analyze()
    elif args.cmd == "aggregate":
        aggregate_report(args.objects)
    elif args.cmd == "verify":
        verify(args.vcmd, getattr(args, "recipe", None), getattr(args, "label", "before"),
               getattr(args, "suffix", ""), getattr(args, "before", None),
               getattr(args, "after", None))


if __name__ == "__main__":
    main()
