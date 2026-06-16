# CRMA Recipe Analysis

Parsing and analysis tooling for Salesforce CRM Analytics (CRMA) recipe JSON files.

CRMA recipes define data transformation pipelines — joins, filters, aggregations, computed columns, etc. — used by Telenor's marketing team. This POC provides utilities to load, inspect, and document those pipelines.

## Structure

```
crma-recipe-analysis/
├── data/                  # Place exported recipe JSON files here
├── analyze_recipe.py      # CLI script to parse and summarize recipes
└── README.md
```

## Usage

```bash
# Analyze a single recipe
python analyze_recipe.py data/my_recipe.json

# Analyze all recipes in the data folder
python analyze_recipe.py data/
```

## Recipe JSON format

Each recipe JSON contains:
- **nodes** — the transformation steps (source, join, filter, aggregate, computeExpression, etc.)
- **connectors** — edges linking nodes into a DAG
- **metadata** — recipe name, version, dataset references
