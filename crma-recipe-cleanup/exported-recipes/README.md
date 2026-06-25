# Exported CRMA recipes — C360 / MC scope

Read-only export of the **49 in-scope CRM Analytics Data Prep recipes** pulled
from production (`sf` alias `prod`, org `00Db0000000cPctEAE`) via the Analytics
REST API. Nothing here was run or modified in the org.

## Folders
- **`originals/`** — the 49 recipes exactly as extracted from the org
  (full Analytics API response: envelope + `recipeDefinition`). This is the
  faithful export. Filename = `<label>__<recipeId>.json`.
- **`cleaned/`** — the same 49 recipes in **recipe-editor import format**
  (`{version, nodes, ui}`), with fields that the analyzer found unused removed
  from the load nodes. These are **proposals** — review before use; they are
  optional and can be ignored.

## Scope note
The scope list had 50 entries. 49 are recipes (all here). The 50th,
`SFDC_LOCAL_SEGMENTATION`, is the **data sync schedule** (keeps source data
fresh), not a recipe — out of scope, nothing to export.

## How the cleaned files were produced
`recipeDefinition` → remove load-node fields not referenced anywhere downstream
(conservative: a field is kept if its name or bare tail appears in any
filter/formula/join/aggregate/output, including dict keys) → emit
`{version, nodes, ui}`. The tooling lives under `../` (PR: add-crma-recipe-cleanup-tool).
