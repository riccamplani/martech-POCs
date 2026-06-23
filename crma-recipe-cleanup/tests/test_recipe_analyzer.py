"""Recipe analyzer tests — run without a live org."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sfcleanup.crma.recipe_analyzer import analyze_recipe

FIXTURE = Path(__file__).parent / "fixtures" / "sample_recipe.json"


def _by_obj(analysis, name):
    return next(o for o in analysis.objects if o.object_name == name)


def test_account_unused_fields_detected():
    recipe = json.loads(FIXTURE.read_text())
    a = analyze_recipe(recipe)
    acct = _by_obj(a, "Account")
    # CCDW/legacy/recordtype fields are loaded but never referenced downstream
    # (matches the transcript: RecordTypeId + CCDW fields are the ones to drop)
    assert set(acct.unused) == {
        "RecordTypeId", "Legacy_CCDW_Code__c",
        "Old_Warehouse_Segment__c", "Unused_Flag__c",
    }
    # fields used in filter/join/formula/output are kept
    for keep in ("Id", "Name", "Type", "AnnualRevenue", "Industry", "BillingCountry"):
        assert keep in acct.used


def test_opportunity_unused_field_detected():
    recipe = json.loads(FIXTURE.read_text())
    a = analyze_recipe(recipe)
    opp = _by_obj(a, "Opportunity")
    assert "Deprecated_Field__c" in opp.unused
    assert "AccountId" in opp.used   # used as a join key


def test_totals():
    recipe = json.loads(FIXTURE.read_text())
    a = analyze_recipe(recipe)
    assert a.total_loaded == 15      # 10 Account + 5 Opportunity
    assert a.total_unused == 5        # 4 Account + 1 Opportunity
