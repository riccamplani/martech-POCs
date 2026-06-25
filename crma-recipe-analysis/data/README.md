# C360 / MC recipe export — `data/`

The **49 in-scope CRM Analytics Data Prep recipes** (the C360 / MC set), exported
read-only from production (`sf` alias `prod`, org `00Db0000000cPctEAE`). Last
refreshed **2026-06-25**. Nothing here was run or modified in the org.

## Format
Each file is the recipe in **recipe-editor import format** — exactly:
```json
{ "version": ..., "nodes": { ... }, "ui": { ... } }
```
i.e. the bare recipe definition with the Analytics API envelope and `runMode`
stripped, so it **imports directly into the recipe editor** (Data Manager →
Recipes → Import). These are the **faithful originals** — no fields removed.

## Naming
```
<recipe label>__<recipeId>.json
```
e.g. `C360_210_-_Logic_Calculated_Items__05v7Q000000srmnQAA.json`. The
`__<recipeId>` suffix guarantees uniqueness (some labels differ only by spacing).

> `C360 210 - Logic Calculated Items.json` (no id suffix) is the earlier manual
> export and is left untouched alongside the set.

## Scope
50 scope entries → **49 recipes** (all here). The 50th,
`SFDC_LOCAL_SEGMENTATION`, is the **data sync schedule** (keeps source data
fresh), not a recipe — out of scope.

## Refreshing this export
Re-pull from prod and re-convert (read-only):
```bash
# 1) pull the in-scope recipes (raw API JSON) — tooling in ../../crma-recipe-cleanup/
python -m sfcleanup.crma_cli extract --scope recipes/scope.txt

# 2) strip the API envelope -> editor format into this folder
python ../convert_to_editor_format.py recipes/input crma-recipe-analysis/data
```
`convert_to_editor_format.py` (one folder up) is stdlib-only — no dependencies.
