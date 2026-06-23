---
description: Analyze extracted recipes and build the per-object field-usage workbook
allowed-tools: Bash(python:*), Bash(ls:*), Bash(cat:*)
---
Analyze the recipes already in recipes/input/. This does NOT touch the org.

1. Run `python -m sfcleanup.crma_cli analyze` (per-recipe cleaned JSON + diffs).
2. Run `python -m sfcleanup.crma_cli aggregate --objects config/objects.yaml`
   (cross-recipe rollup -> output/field_usage_by_object.xlsx).
3. Report a concise summary table: for each of the 7 groups and 16 objects, how
   many fields are loaded / used / UNUSED-everywhere.
4. Call out the objects with the most UNUSED fields, and explicitly flag any
   legacy-warehouse (CCDW) or RecordTypeId-type fields that show as UNUSED.
5. Remind the user that nothing is changed in Salesforce: the cleaned JSON in
   recipes/output/ is a PROPOSAL to review, then apply in the recipe editor and
   verify with the before/after equivalence check.
