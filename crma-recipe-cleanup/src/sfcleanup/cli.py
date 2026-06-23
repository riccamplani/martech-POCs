"""Entry point: python -m sfcleanup.cli analyze --object Account

Read-only by default. Produces output/<object>_cleanup_plan.{csv,md} and a
starter dbt staging model. Applying changes to the org is intentionally a
separate, gated step (not enabled here) so a human approves the plan first.
"""
from __future__ import annotations

import argparse

from rich.console import Console
from rich.table import Table

from .auth import get_session
from .describe import describe_fields
from .usage import measure_usage
from .dependencies import map_dependencies
from .classify import classify_fields
from .report import write_plan

console = Console()


def analyze(sobject: str) -> None:
    console.print(f"[bold]Authenticating…[/bold]")
    session = get_session()

    console.print(f"[bold]Describing {sobject}…[/bold]")
    fields = describe_fields(session, sobject)
    console.print(f"  {len(fields)} fields found")

    console.print("[bold]Measuring field usage…[/bold]")
    measure_usage(session, sobject, fields)

    console.print("[bold]Mapping dependencies…[/bold]")
    refs = map_dependencies(session, sobject, fields)

    console.print("[bold]Classifying with Claude…[/bold]")
    recs = classify_fields(fields)

    console.print("[bold]Writing plan…[/bold]")
    write_plan(sobject, fields, recs, refs)

    _print_summary(fields, recs)
    console.print(f"\n[green]Done.[/green] See output/{sobject.lower()}_cleanup_plan.md")


def _print_summary(fields, recs) -> None:
    by_name = {r["name"]: r for r in recs}
    t = Table(title="Field analysis")
    for c in ("Field", "Type", "Pop%", "Refs", "Rec"):
        t.add_column(c)
    for f in sorted(fields, key=lambda x: (x.population_rate or 0)):
        rec = by_name.get(f.name, {}).get("recommendation", "REVIEW")
        pop = "n/a" if f.population_rate is None else f"{f.population_rate*100:.1f}"
        color = {"KEEP": "green", "DEPRECATE": "red", "REVIEW": "yellow"}.get(rec, "white")
        t.add_row(f.name, f.type, pop, str(f.referenced_count), f"[{color}]{rec}[/{color}]")
    console.print(t)


def main() -> None:
    p = argparse.ArgumentParser(prog="sfcleanup")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("analyze", help="read-only field analysis + plan")
    a.add_argument("--object", default="Account")
    args = p.parse_args()
    if args.cmd == "analyze":
        analyze(args.object)


if __name__ == "__main__":
    main()
