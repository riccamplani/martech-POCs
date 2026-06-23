---
description: Adapt the recipe parser to a real exported recipe JSON and prove it with a test
argument-hint: <path to a real recipe json in recipes/input/>
allowed-tools: Bash(python:*), Edit, Bash(cat:*)
---
A real recipe JSON may differ slightly from the sample fixture. Make the analyzer
match the org's actual format WITHOUT weakening the safety logic.

1. Read the file at `$ARGUMENTS`. Identify where nodes live, what the load/source
   node action is called, where the loaded `fields` list sits, and how downstream
   references (filters, joins, formulas, output) are expressed.
2. Compare against src/sfcleanup/crma/recipe_analyzer.py (_find_nodes,
   _LOAD_ACTIONS, _loaded_fields, _collect_referenced_tokens). Propose minimal
   edits so loaded-vs-referenced detection is correct for this format.
3. Add a small fixture under tests/fixtures/ derived (and anonymized) from this
   recipe, plus a test asserting the known used/unused split. Run `pytest -q`.
4. Keep the rule conservative: a loaded field is "used" if referenced anywhere
   downstream; never mark a referenced field as unused. Show me the diff before
   finalizing — do not commit.
