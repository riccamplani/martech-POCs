---
name: clean-recipes
description: Clean CRMA recipe JSONs by removing unused fields from load (source) nodes. Produces cleaned recipe files and per-recipe field usage reports.
---

# CRMA Recipe Field Cleanup

This skill analyzes CRMA recipe JSON files, traces field usage through the DAG, and removes fields from load nodes that are never referenced downstream. The logic has been validated in production (identical output row counts, faster execution).

## How to run

Run the analysis script from the `crma-recipe-analysis/` directory:

```bash
cd crma-recipe-analysis && python3 analyze_field_usage.py
```

This will:
1. Clean old output files from previous runs
2. Scan all `.json` files in `crma-recipe-analysis/data/`
3. For ALL valid recipes: decode HTML entities and output a cleaned recipe as `clean_<original_filename>.json` in `crma-recipe-analysis/output/json/`
4. For recipes with target SF objects: also trim unused fields from load nodes, clean DROP schemas, generate a markdown report in `crma-recipe-analysis/output/reports/`, and add to dashboard data
5. Output `dashboard_data.json` in `crma-recipe-analysis/output/json/` (consumed by the dashboard)

## What the script does (DO NOT change this logic)

- **Only analyzes load nodes for the 16 target SF objects**: Account, Account_Structure__c, Account_Summary__c, Subscription, Subscription_Item, Agreement__c, Agreement_Item__c, Account_Location__c, BSS_Event__c, Contact, Shortcut_to_Product_Offer_ID__c, Payment_Status__c, User, Terminated_Subscription__c, Suspect__c, External_User__c
- **Modifies load node `fields` arrays AND downstream DROP schema nodes** — when a field is removed from a load node, it is also removed from DROP schema nodes **downstream of that specific load node** (CRMA validates that DROP fields exist in the data flow). The cleanup is scoped per-load-node to avoid removing common field names (Name, CreatedDate, etc.) from unrelated branches.
- **Load nodes for non-target objects are left untouched** — datasets, Case, Opportunity, etc. are not cleaned
- **Output format matches input format** — if the input is `{nodes, ui, version}`, the output is too. If the input is an API export with `recipeDefinition`, the output extracts just the `recipeDefinition` content (what CRMA expects for import)
- **Schema DROP mode**: fields listed in DROP mode schemas are being discarded — they do NOT count as used
- **Schema SELECT mode**: fields listed in SELECT mode schemas ARE actively used
- **Formula/computeRelative SQL expressions**: field references are extracted by tokenizing the SQL expression and filtering out SQL keywords
- **Dot-qualified field names**: after joins, fields get prefixed with join alias paths (e.g., `CangetFib1.HavenotIA.SEogAgrol.DPSS_Portfolio__c`). The tracer matches the last segment (base field name) back to load node fields. DROP schema cleanup also handles dot-qualified names.
- **All node types are covered**: filter, formula, computeRelative, join, aggregate, extractGrains, schema, appendV2, typeCast, save

## Folder structure

```
crma-recipe-analysis/
  data/                  # Input: raw recipe JSONs
  output/
    json/                # Cleaned recipe JSONs + dashboard_data.json
    reports/             # Markdown field usage reports
  dashboard.html         # Interactive HTML dashboard (open in browser)
  analyze_field_usage.py # Analysis script
```

## After running

Report the summary output to the user. The cleaned recipe files can be imported directly into CRMA. The user should validate by running both original and cleaned recipes and comparing output dataset row counts. Open `crma-recipe-analysis/dashboard.html` in a browser to explore results interactively.

## Important

- Do NOT modify the `analyze_field_usage.py` script logic. It has been validated in production.
- Do NOT add or remove nodes — only field arrays in load nodes and field lists in DROP schema nodes are trimmed. All other nodes are unchanged (except HTML entity decoding).
- API export format HTML-encodes strings throughout the recipe (`&#39;` for `'`, `&lt;` for `<`, `&quot;` for `"`). The script automatically decodes ALL HTML entities in ALL nodes back to plain characters, which is what CRMA import expects.
- If the user reports a failure after import, check the field usage report to see which fields were kept vs removed, and investigate whether a field reference was missed by the SQL parser or dot-qualified name matching.
