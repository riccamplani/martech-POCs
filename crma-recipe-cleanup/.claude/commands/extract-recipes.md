---
description: Load scope from the Excel and extract in-scope CRMA recipes (read-only)
allowed-tools: Bash(python:*), Bash(sf:*), Bash(ls:*), Bash(cat:*)
---
Extract the in-scope CRMA recipes. This is READ-ONLY against the org.

1. Confirm `recipes/scope.txt` and `config/objects.yaml` exist. If not, run
   `python -m sfcleanup.scope_loader --xlsx data/CRMA_Recipes.xlsx` and report the
   counts (expected: 50 recipes, 16 objects, 7 groups).
2. Verify auth with `sf org display --target-org prod --json` (Connected = ok).
3. Run `python -m sfcleanup.crma_cli extract --scope recipes/scope.txt`.
4. Summarize: how many recipes downloaded into recipes/input/, and list any that
   FAILED with the reason (usually a name in the Excel that doesn't exactly match
   the org's recipe label — note those so the user can switch them to recipe IDs).
Do not analyze or modify recipes in this command. Stop after the extraction summary.
