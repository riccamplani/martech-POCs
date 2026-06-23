"""Turn the project's CRMA_Recipes.xlsx into machine-readable scope files.

Reads:
  - sheet "Recipes": the in-scope recipe names
  - sheet "Objects": Salesforce object -> analysis-group ("Sheet") mapping

Writes:
  - recipes/scope.txt     (one recipe name per line; consumed by crma_cli extract)
  - config/objects.yaml   (in-scope objects + the 7 analysis groups)

Run:  python -m sfcleanup.scope_loader --xlsx data/CRMA_Recipes.xlsx
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import yaml


def _find_column_values(df: pd.DataFrame, header: str) -> list[str]:
    """Find the cell equal to `header` and return non-null values below it."""
    for col in df.columns:
        series = df[col].astype("string")
        match = series[series.str.strip() == header]
        if not match.empty:
            start = match.index[0]
            vals = df[col].iloc[start + 1 :].dropna().astype(str).str.strip()
            return [v for v in vals if v]
    return []


def load_recipes(xlsx: Path) -> list[str]:
    df = pd.read_excel(xlsx, sheet_name="Recipes", header=None)
    return _find_column_values(df, "Recipe")


def load_objects(xlsx: Path) -> dict[str, list[str]]:
    """Return {analysis_group: [object_api_names]} preserving file order."""
    df = pd.read_excel(xlsx, sheet_name="Objects", header=None)
    # locate the header row containing "Salesforce object" and "Sheet"
    obj_col = sheet_col = header_row = None
    for r in range(len(df)):
        row = df.iloc[r].astype("string").str.strip()
        if (row == "Salesforce object").any() and (row == "Sheet").any():
            header_row = r
            obj_col = row[row == "Salesforce object"].index[0]
            sheet_col = row[row == "Sheet"].index[0]
            break
    if header_row is None:
        raise ValueError("Could not locate 'Salesforce object'/'Sheet' header in Objects sheet")

    groups: dict[str, list[str]] = {}
    for r in range(header_row + 1, len(df)):
        obj = df.iat[r, obj_col]
        grp = df.iat[r, sheet_col]
        if pd.isna(obj) or pd.isna(grp):
            continue
        groups.setdefault(str(grp).strip(), []).append(str(obj).strip())
    return groups


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--xlsx", default="data/CRMA_Recipes.xlsx")
    args = ap.parse_args()
    xlsx = Path(args.xlsx)

    recipes = load_recipes(xlsx)
    groups = load_objects(xlsx)
    flat = [o for objs in groups.values() for o in objs]

    Path("recipes").mkdir(exist_ok=True)
    Path("recipes/scope.txt").write_text(
        "# Auto-generated from " + xlsx.name + " — in-scope recipes\n"
        + "\n".join(recipes) + "\n"
    )
    Path("config").mkdir(exist_ok=True)
    Path("config/objects.yaml").write_text(
        yaml.safe_dump({"groups": groups, "objects": flat}, sort_keys=False, allow_unicode=True)
    )
    print(f"recipes: {len(recipes)}  objects: {len(flat)}  groups: {len(groups)}")
    print("wrote recipes/scope.txt and config/objects.yaml")


if __name__ == "__main__":
    main()
