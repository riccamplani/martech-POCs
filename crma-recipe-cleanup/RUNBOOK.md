# RUNBOOK — CRMA recipe field cleanup, step by step

Scope from `CRMA_Recipes.xlsx`: **50 recipes**, **16 objects**, **7 analysis groups**.
This runbook takes you from an empty Mac to a reviewed cleanup proposal, in order.
Each step says what to run and what "done" looks like.

---

## Phase 0 — Prerequisites (once)

**Step 0.1 — Install tooling.**
```bash
brew install --cask sf-cli          # Salesforce CLI
brew install git node               # git + node (node only if you use npm path)
curl -fsSL https://claude.ai/install.sh | bash   # Claude Code (native installer)
python3 --version                   # need 3.11+
```
Done when `sf --version`, `git --version`, and `claude --version` all print.

**Step 0.2 — Resolve the access blocker FIRST.** You authenticate via SSO, so the
username/password flow is a dead end. **Verified blocker:** API access is already
fine — the gap is **CRM Analytics**. You need BOTH, assigned to your user:
1. a **CRM Analytics Plus license** (PSL), and
2. the **CRM Analytics Plus Admin** permission set (`EinsteinAnalyticsPlusAdmin`)
   — the license alone returns `FUNCTIONALITY_NOT_ENABLED`; the permission set is
   what turns the feature on.

Send `scripts/ADMIN_REQUEST.md` to Martin or Per (no full admin needed). Done when
`smoke_test` (see Quick reference) prints **✓ CRM Analytics reachable**.

---

## Phase 1 — Project setup

**Step 1.1 — Get the repo and environment.**
```bash
unzip salesforce-account-cleanup.zip && cd salesforce-account-cleanup
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

**Step 1.2 — Connect to the existing GitHub repo** (the "recipe" repo you already
created and added Carlos to as collaborator):
```bash
git init
git add .
git commit -m "CRMA recipe cleanup tooling + scope from CRMA_Recipes.xlsx"
git remote add origin <your-existing-repo-url>
git branch -M main
git push -u origin main
```
Open it in VS Code (`code .`) and start Claude Code in the integrated terminal
(`claude`). It reads `CLAUDE.md` and learns the two tracks + safety rules.

**Step 1.3 — Load the scope from the Excel.** The Excel is already in `data/`.
```bash
python -m sfcleanup.scope_loader --xlsx data/CRMA_Recipes.xlsx
```
Done when it prints `recipes: 50  objects: 16  groups: 7` and writes
`recipes/scope.txt` and `config/objects.yaml`. Commit both.

---

## Phase 2 — Authenticate (SSO, no password)

**Step 2.1 — Log in through the browser/SSO.**
```bash
sf org login web --alias prod
sf org display --target-org prod      # confirm an access token + instance URL
```
In `.env` keep `SF_AUTH_MODE=cli` and `SF_CLI_ALIAS=prod`.
Done when `sf org display` shows `Connected Status: Connected`.

> If `extract` fails with `FUNCTIONALITY_NOT_ENABLED` or "No valid licenses found",
> Phase 0.2 isn't complete — the CRM Analytics license and/or the
> `EinsteinAnalyticsPlusAdmin` permission set isn't assigned yet. Confirm with
> `smoke_test` before proceeding.
>
> Note: recent `sf` CLI masks the access token in `sf org display`, so the tool
> routes REST calls through `sf api request rest` under the hood (see `auth.py`).
> `sf org display` showing `Connected` is enough; you don't need a visible token.

---

## Phase 3 — Extract (the priority: "the export first")

**Step 3.1 — Download the 50 in-scope recipes to `recipes/input/`.**
```bash
python -m sfcleanup.crma_cli extract --scope recipes/scope.txt
```
Each line prints `✓ <recipe> -> recipes/input/<label>__<id>.json`. Failures print
`✗` with the reason and the run continues, so you can see which recipes need
attention (e.g. a name in the Excel that doesn't match the org label exactly).
Done when most/all 50 land as JSON files.

**Step 3.2 — Sanity-check one file.** Open one recipe JSON in VS Code and confirm
it has a `nodes` structure with `load` nodes and `fields` arrays. If the shape
differs from `tests/fixtures/sample_recipe.json`, tell Claude Code to adjust the
node parser in `src/sfcleanup/crma/recipe_analyzer.py` (the `_find_nodes` /
`_LOAD_ACTIONS` constants) — recipe JSON varies slightly by org/version.

---

## Phase 4 — Analyze and propose cleanup

**Step 4.1 — Per-recipe analysis + cleaned proposals.**
```bash
python -m sfcleanup.crma_cli analyze
```
Writes, for each recipe, `recipes/output/<recipe>.cleaned.json` (unused fields
removed from load nodes) and `<recipe>.diff.md` (what would be removed and why).

**Step 4.2 — Cross-recipe rollup by object (the master view).**
```bash
python -m sfcleanup.crma_cli aggregate --objects config/objects.yaml
```
Writes `output/field_usage_by_object.xlsx` — one sheet per analysis group
(Account, Account_Structure_Summary, Subscription, Subscription_Item,
Agreement_&Item, AccLoc_BSS_Con_PO, PS_User_TS_S_EU), each listing every field as
USED or UNUSED with how many recipes use it, plus a Summary sheet of counts.
A field is UNUSED only if **no** recipe references it — safe-to-clean evidence.

---

## Phase 5 — Human review (the gate)

**Step 5.1 — Review the workbook with Carlos/Martin.** Walk the UNUSED rows per
object. These are removal candidates. Pay attention to fields populated from the
old warehouse (the "CCDW" / RecordTypeId class of fields called out in the
kickoff) — they should surface as UNUSED.

**Step 5.2 — Approve per recipe.** For each recipe you'll clean, confirm its
`.diff.md` removals are acceptable.

> The tool does not write changes back to the org. Modifying recipe file content
> via API is not officially supported, so applying the cleaned definition is done
> in the recipe editor (or a supported update), deliberately, by a human.

---

## Phase 6 — Apply and verify (the proven loop)

The gate: a cleaned recipe must produce the **same output row counts** as the
original, per output dataset. The `verify` command automates that check
(SAQL count of every dataset the recipe writes), so it's a PASS/FAIL, not a
manual eyeball.

For each approved recipe:

**Step 6.1 — Baseline the live outputs BEFORE changing anything.**
```bash
python -m sfcleanup.crma_cli verify snapshot \
  --recipe recipes/input/<recipe>__<id>.json --label before
```
Writes `recipes/verify/<recipe>__before.json` with the current row count of every
output dataset. (These snapshots hold production audience sizes and are gitignored.)

**Step 6.2 — Apply the removals to a Save-As COPY, not the live recipe.** In CRM
Analytics Studio → Data Manager → Recipes, open the recipe, **Save As** a copy
(e.g. `<recipe> CLEANTEST`). In each Input node, untick exactly the fields listed
in `recipes/output/<recipe>.diff.md`. Save and run the copy.

**Step 6.3 — Snapshot the cleaned copy's outputs.** If the copy writes to renamed
datasets, pass the suffix you used so `verify` reads the copy's outputs:
```bash
python -m sfcleanup.crma_cli verify snapshot \
  --recipe recipes/input/<recipe>__<id>.json --label after --suffix _CLEANTEST
```

**Step 6.4 — Compare.**
```bash
python -m sfcleanup.crma_cli verify compare \
  --before recipes/verify/<recipe>__before.json \
  --after  recipes/verify/<recipe>__after.json
```
Done when it prints **✓ EQUIVALENT** (every output dataset PASS). Any `FAIL`
(row counts differ) or `MISSING` (dataset not found) means do NOT promote — a
removed field was actually used downstream; revert that field and re-check.

**Step 6.5 — Promote and record.** Once the copy is EQUIVALENT, apply the same
field removals to the real recipe. Commit the `recipes/input/` (original) and
`recipes/output/` (cleaned) pair for provenance. (`recipes/verify/` stays local.)

---

## Phase 7 — Object-level cleanup (later track)

Once a field is referenced by **no** recipe (UNUSED across the workbook) and no
other Salesforce dependency, it can be retired from the object itself:
```bash
python -m sfcleanup.cli analyze --object Account
```
This adds population %, dependency, and a Claude KEEP/REVIEW/DEPRECATE
recommendation, and emits a dbt staging model from the survivors — the bridge to
Phase 8.

---

## Phase 8 — CRMA → BigQuery + dbt (the destination)

For each in-scope recipe, reimplement its logic as a dbt model lineage
(staging → intermediate → marts) on BigQuery, using the cleaned field set as the
column contract. Validate each dbt model's output against the CRMA dataset before
switching consumers over. When all recipes are reproduced and verified, retire
CRMA. This is the foundation for the next-best-action engine.

---

## Quick command reference
```bash
python -m sfcleanup.scope_loader --xlsx data/CRMA_Recipes.xlsx   # scope -> files
sf org login web --alias prod                                    # SSO auth
python -m sfcleanup.crma_cli extract --scope recipes/scope.txt   # download recipes
python -m sfcleanup.crma_cli analyze                             # per-recipe cleanup
python -m sfcleanup.crma_cli aggregate                           # object rollup xlsx
python -m sfcleanup.crma_cli verify snapshot --recipe <f> --label before   # baseline outputs
python -m sfcleanup.crma_cli verify snapshot --recipe <f> --label after --suffix _CLEANTEST
python -m sfcleanup.crma_cli verify compare --before <b.json> --after <a.json>  # PASS/FAIL gate
python -m sfcleanup.cli analyze --object Account                 # object-level (later)
```

Quick connectivity check (auth + whether CRM Analytics is reachable):
```bash
python -c "from src.sfcleanup.auth import get_session, smoke_test; print(smoke_test(get_session()))"
```
