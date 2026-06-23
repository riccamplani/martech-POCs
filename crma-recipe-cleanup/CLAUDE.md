# CLAUDE.md — Project context for Claude Code

## What this project does
Two tracks:
- **Track A (priority): CRMA Data Prep recipe cleanup.** Extract recipes, find
  which fields from each input object (standard AND custom — not just Account)
  are actually used in the recipe logic, and propose a cleaned recipe with unused
  fields removed. Automates the manual export->analyze->clean->reimport loop.
- **Track B (later): Salesforce object field cleanup**, then migration of recipe
  logic from CRMA to **BigQuery + dbt**.

Track A pipeline: `list recipes` -> `download JSON to recipes/input/` ->
`analyze loaded-vs-referenced fields per object` -> `write cleaned JSON + diff` ->
human review -> apply in recipe editor -> verify both versions identical.

Track B pipeline: `describe` -> `measure population` -> `map dependencies`
-> `Claude classifies KEEP/REVIEW/DEPRECATE` -> plan -> dbt staging model.

## Stack
- Python 3.11+, `simple-salesforce`, `requests`, `anthropic`, `pydantic`, `rich`
- Salesforce CLI (`sf`) for interactive auth; JWT Bearer flow for headless/CI
- dbt-bigquery for the migration target
- Git + GitHub for collaboration

## Repo layout
- `src/sfcleanup/auth.py` — get an authenticated Salesforce client (CLI or JWT)
- `src/sfcleanup/describe.py` — pull Account field metadata (Describe + Tooling API)
- `src/sfcleanup/usage.py` — population %, distinct counts per field (SOQL aggregates)
- `src/sfcleanup/dependencies.py` — MetadataComponentDependency reference graph
- `src/sfcleanup/classify.py` — Claude recommends KEEP/REVIEW/DEPRECATE per field
- `src/sfcleanup/report.py` — write CSV + Markdown cleanup plan to ./output
- `src/sfcleanup/cli.py` — orchestrates the run (`python -m sfcleanup.cli analyze`)
- `dbt/models/staging/stg_salesforce__accounts.sql` — generated from KEEP fields

## Conventions for Claude Code
- NEVER hardcode credentials. Everything comes from `.env` (see `.env.example`).
- NEVER call destructive Metadata API operations without an explicit `--apply` flag
  AND a human-approved plan file. Default runs are read-only.
- Treat the org as PRODUCTION. Read-only by default; deletes are deprecations
  (set field as not-required, remove from layouts) before any hard delete.
- Add new SOQL behind the `usage.py` helpers; keep API version in one constant.
- Write tests in `tests/` for any parsing/classification logic.

## How to run
1. `source .venv/bin/activate`
2. `sf org login web --alias prod`   (or configure JWT in .env)
3. `python -m sfcleanup.cli analyze --object Account`
4. Review `output/account_cleanup_plan.md`, then optionally `--apply`.
