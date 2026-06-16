#!/usr/bin/env python3
"""Bulk-export selected CRM Analytics (CRMA) Data Prep recipe JSON definitions.

Authenticates to Salesforce via simple_salesforce, paginates through
GET /wave/recipes, filters to the target recipe list, fetches each
recipe's JSON definition via GET /wave/recipes/{id}/file, and saves
them to crma_recipes_export/.
"""

import json
import re
import sys
from pathlib import Path

from simple_salesforce import Salesforce

# ─────────────────────────────────────────────────────────────────────
# CONFIGURATION — update before running
# ─────────────────────────────────────────────────────────────────────

# Option 1: Username / Password / Security Token
SF_USERNAME = "YOUR_USERNAME"
SF_PASSWORD = "YOUR_PASSWORD"
SF_SECURITY_TOKEN = "YOUR_TOKEN"

# Option 2: Connected App (OAuth client_credentials or JWT)
# If using a Connected App, replace the Salesforce() call in
# authenticate() below with the appropriate flow. See:
# https://github.com/simple-salesforce/simple-salesforce#connected-app

SF_DOMAIN = "telenor"          # → telenor.my.salesforce.com
API_VERSION = "62.0"           # confirm with your Salesforce admin

OUTPUT_DIR = Path(__file__).parent / "crma_recipes_export"
PAGE_SIZE = 100

# ─────────────────────────────────────────────────────────────────────
# RECIPES TO EXPORT — matched against recipe label (case-insensitive)
# Set to None to export ALL recipes.
# ─────────────────────────────────────────────────────────────────────

TARGET_RECIPES = {
    "SFDC_LOCAL_SEGMENTATION",
    "C360 210 - Logic Calculated Items",
    "C360 220 - Logic Suppressions",
    "C360 310 - Logic Service Model SE",
    "C360 320 - Logic Deep Sale",
    "C360 330 -  Logic New Sales MV",
    "C360 340 - Logic Fiber Rebinding",
    "C360 350 - Logic Fiber and TBB Newsale",
    "C360 410 - Logic New Sales MV Campaign",
    "C360 420 - Logic Fiber Rebinding Campaign",
    "C360 421 - Logic Migrasjon TBB til Fiber Campaign",
    "C360 430 - Logic Fiber and TBB Newsale Campaign",
    "C360 431 - Logic Fiber Newsale Feil nummer Campaign",
    "C360 432 - Logic Oppfølging opportunities fra KS - Fiber og TBB Campaign",
    "C360 433 - Logic Fiber deepsale Medium Campaign",
    "C360 434 - Logic Fiber Newsale and deepsale Medium DMU Campaign",
    "C360 438 -  Logic Møtebooking DPSS Medium Campaign Loyalty",
    "C360 439 -  Logic Møtebooking-pilot Hunter M Campaign",
    "C360 440 -  Logic Mobile Voice Rebinding",
    "C360 450 - Logic New Sales MV Agrol",
    "C360 460 - Logic Vekst to Verdi Campaign",
    "C360 461 - Logic New Sales SafeZone Oppdatert",
    "C360 470 - Rebinding MT Red group Portugal Pilot",
    "C360 480 - Rebinding Forbund",
    "C360 490 - Logic Førstegangssamtale Small Campaign",
    "C360 491 - Mobile Voice Rebinding Agrol",
    "C360 492 - New Sales MV Daughter Outside Mother Agreement",
    "C360 493 - New Sales MV NHO Service og Handel",
    "C360 494 - New Sales MV Churn Customer last 12-30 months",
    "C360 495 - Holdback NHO Byggenæringen",
    "C360 496 - Pilot SafeZone og Oppdatert bundle",
    "C360 497 - New Sales MV Campaign - Medium",
    "C360 510 - Append Sales Tips - Account",
    "C360 520 - Append Sales Tips - Subscription",
    "C360 610 - Insert Sales Tips",
    "C360 620 - Update Sales Tips - Response Code",
    "C360 630 - Update Sales Tips - Personalization fields",
    "C360 635 - Update Sales Tips - Channel and Agency",
    "C360 640 - Update Subscriptions",
    "C360 - MC - Always On - Onboarding ny Mobil Tale kunde",
    "C360 - MC - Always On - Onboarding ny SafeZone Mobil kunde",
    "C360 - MC - Always On - Onboarding ny SafeZone Mobil kunde oppsalg oppdatert",
    "C360 - MC - Always On - Nysalg Fiber ved ikke svar",
    "C360 - MC - Always On - Fiber rebinding ved ikke svar",
    "C360 - MC - Always On - Fiber nysalg - Har fiber gjennom utleier_3.part",
    "C360 - MC - Always On - Velkomstprogram nye medlemmer Forbund",
    "C360 - MC - Always On - Append C360 eDM Master",
    "Backup_C360_eDM_master",
    "MC - Automatised Rebinding - Deep sales using SafeZone",
    "MC - Moonrise",
}


# ─────────────────────────────────────────────────────────────────────
# AUTHENTICATION
# ─────────────────────────────────────────────────────────────────────

def authenticate() -> Salesforce:
    """Return an authenticated Salesforce session."""
    sf = Salesforce(
        username=SF_USERNAME,
        password=SF_PASSWORD,
        security_token=SF_SECURITY_TOKEN,
        domain=SF_DOMAIN,
        version=API_VERSION,
    )
    print(f"Authenticated as {SF_USERNAME} on {SF_DOMAIN}.my.salesforce.com")
    return sf


# ─────────────────────────────────────────────────────────────────────
# RECIPE LISTING (with pagination)
# ─────────────────────────────────────────────────────────────────────

def list_all_recipes(sf: Salesforce) -> list[dict]:
    """Paginate through GET /wave/recipes and return all recipe metadata."""
    recipes = []
    url = f"/services/data/v{API_VERSION}/wave/recipes?pageSize={PAGE_SIZE}"

    while url:
        response = sf.restful(url, method="GET")
        batch = response.get("recipes", [])
        recipes.extend(batch)
        print(f"  Fetched {len(batch)} recipes (total so far: {len(recipes)})")
        url = response.get("nextPageUrl")

    return recipes


def filter_recipes(recipes: list[dict]) -> list[dict]:
    """Filter recipes to only those in TARGET_RECIPES. Match on label or name."""
    if TARGET_RECIPES is None:
        return recipes

    target_lower = {name.lower() for name in TARGET_RECIPES}

    matched = []
    for recipe in recipes:
        label = recipe.get("label", "").lower()
        name = recipe.get("name", "").lower()
        if label in target_lower or name in target_lower:
            matched.append(recipe)

    return matched


# ─────────────────────────────────────────────────────────────────────
# RECIPE DEFINITION DOWNLOAD
# ─────────────────────────────────────────────────────────────────────

def fetch_recipe_json(sf: Salesforce, recipe_id: str) -> dict:
    """Fetch the full JSON definition for a single recipe."""
    url = f"wave/recipes/{recipe_id}/file"
    return sf.restful(url, method="GET")


def sanitize_filename(name: str) -> str:
    """Replace filesystem-unsafe characters with underscores."""
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip(". ")


# ─────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sf = authenticate()

    print("\nListing all recipes...")
    all_recipes = list_all_recipes(sf)
    print(f"Found {len(all_recipes)} total recipes in org.")

    recipes = filter_recipes(all_recipes)
    total = len(recipes)

    if TARGET_RECIPES is not None:
        # Report which target recipes were NOT found
        matched_labels = {r.get("label", "").lower() for r in recipes}
        matched_names = {r.get("name", "").lower() for r in recipes}
        matched_all = matched_labels | matched_names
        not_found = [name for name in sorted(TARGET_RECIPES)
                     if name.lower() not in matched_all]
        print(f"Matched {total} of {len(TARGET_RECIPES)} target recipes.\n")
        if not_found:
            print(f"  WARNING — {len(not_found)} target recipes not found in org:")
            for name in not_found:
                print(f"    ? {name}")
            print()
    else:
        print(f"\nExporting all {total} recipes.\n")

    if total == 0:
        print("Nothing to export.")
        return

    succeeded = []
    failed = []

    for i, recipe in enumerate(recipes, 1):
        recipe_id = recipe["id"]
        recipe_name = recipe.get("name", recipe_id)
        label = recipe.get("label", recipe_name)

        print(f"[{i}/{total}] Exporting: {label} ({recipe_id})...", end=" ")

        try:
            definition = fetch_recipe_json(sf, recipe_id)
            filename = sanitize_filename(label) + ".json"
            out_path = OUTPUT_DIR / filename
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(definition, f, indent=4, ensure_ascii=False)
            print(f"OK → {filename}")
            succeeded.append(label)
        except Exception as e:
            print(f"FAILED — {e}")
            failed.append((label, str(e)))

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"Export complete.")
    print(f"  Target recipes:         {len(TARGET_RECIPES) if TARGET_RECIPES else 'ALL'}")
    print(f"  Matched in org:         {total}")
    print(f"  Exported successfully:  {len(succeeded)}")
    print(f"  Failed:                 {len(failed)}")

    if failed:
        print(f"\nFailed recipes:")
        for name, error in failed:
            print(f"  ✗ {name}: {error}")

    print(f"\nOutput directory: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
