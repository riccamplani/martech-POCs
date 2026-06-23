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


def main() -> None:
    p = argparse.ArgumentParser(prog="sfcleanup.crma")
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract", help="download recipes to recipes/input/")
    e.add_argument("--scope", help="file with in-scope recipe names/ids (one per line)")
    e.add_argument("--all", action="store_true", help="extract every recipe")
    sub.add_parser("analyze", help="analyze + propose cleanup for recipes/input/")
    a = sub.add_parser("aggregate", help="cross-recipe field usage -> Excel workbook")
    a.add_argument("--objects", default="config/objects.yaml")
    args = p.parse_args()
    if args.cmd == "extract":
        extract(args.scope, args.all)
    elif args.cmd == "analyze":
        analyze()
    elif args.cmd == "aggregate":
        aggregate_report(args.objects)


if __name__ == "__main__":
    main()
