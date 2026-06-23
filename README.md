# MARTEC / CRMA Recipe Cleanup → BigQuery + dbt

Automates the workflow validated in the project kickoff: extract CRM Analytics
(CRMA) **Data Prep recipes**, find which fields from each input object are
actually used in the recipe logic, propose a cleaned recipe (unused fields
removed), and prepare the eventual migration of recipe logic to **BigQuery + dbt**.

It replaces the manual loop (export JSON → paste into VS Code → ask Claude which
fields are used → remove them → re-import) with repeatable, reviewable commands.

## Two tracks

**Track A — CRMA recipe cleanup (the current priority: "the export first").**
Scope = all in-scope recipes and **all their input objects (standard + custom)**,
not just Account.
- `crma_cli.py extract` — download recipes to `recipes/input/`
- `crma_cli.py analyze` — per recipe, per object: loaded vs used vs removable;
  writes a cleaned JSON + diff to `recipes/output/`

**Track B — Salesforce object cleanup (later phase).**
Once recipes no longer reference a field, the field can be retired from the
object itself. `cli.py analyze` measures population %, dependencies, and a Claude
recommendation per field, and emits a dbt staging model from the survivors.

## Quickstart (Mac)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# AUTH — works with SSO, no password (see scripts/ADMIN_REQUEST.md first)
brew install --cask sf-cli
sf org login web --alias prod

# TRACK A: extract the in-scope recipes, then analyze
python -m sfcleanup.crma_cli extract --scope recipes/scope.txt
python -m sfcleanup.crma_cli analyze
open recipes/output/   # review each *.diff.md before changing anything

# TRACK B (later): object-level field analysis
python -m sfcleanup.cli analyze --object Account
```

## Blocked on auth? Read this first
`scripts/ADMIN_REQUEST.md` — you log in via SSO so there's no password; the only
missing piece is the **API Enabled** permission. That file is a copy-paste ask
for the admin (no full admin rights needed). `scripts/setup_connected_app.md`
covers the headless/CI (JWT) path.

## Safety
- Read-only by default. Extraction and analysis never change the org.
- Recipe re-import is intentionally NOT automated: modifying recipe file content
  via API isn't officially supported and could break a production recipe. Apply
  the proposed removals in the recipe editor, then run both versions and confirm
  identical output (the before/after check already proven to work).

## Repo layout
```
src/sfcleanup/
  auth.py              # SSO/CLI session or JWT bearer
  crma/client.py       # CRMA REST: list + fetch recipes
  crma/recipe_analyzer.py  # loaded vs referenced fields per object
  crma/clean.py        # proposed cleaned recipe + diff
  crma_cli.py          # extract / analyze (Track A)
  describe.py usage.py dependencies.py classify.py report.py cli.py  # Track B
recipes/input/   recipes/output/   recipes/scope.txt
dbt/models/staging/  scripts/  tests/
```
See `CLAUDE.md` for how to drive this with Claude Code.
