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
username/password flow is a dead end and the Connected App attempt was declined
because your user lacks **API Enabled**. Send `scripts/ADMIN_REQUEST.md` to Martin
or Per. You need a Permission Set granting: API Enabled, Use CRM Analytics, View
Setup and Configuration, and read/FLS on the 16 in-scope objects. No full admin.
Done when the admin confirms the permission set is assigned to your user.

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

> If this still fails with `API_DISABLED_FOR_ORG` or a permission error, Phase 0.2
> isn't complete — the API Enabled grant is missing. Don't proceed until it works.

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

For each approved recipe:
1. Apply the field removals from `<recipe>.cleaned.json` in the CRMA recipe editor.
2. Run BOTH the original and cleaned recipe.
3. Compare outputs — they must be **identical** (this is the equivalence check
   already validated manually). If identical, keep the cleaned version.
4. Commit the `recipes/input/` (original) and `recipes/output/` (cleaned) pair for
   provenance.

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
python -m sfcleanup.cli analyze --object Account                 # object-level (later)
```
