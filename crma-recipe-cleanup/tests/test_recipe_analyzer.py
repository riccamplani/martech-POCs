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


def test_qualified_field_names_not_false_removed():
    """Regression: append/staged recipes load fields qualified with a dot
    (e.g. 'TRANSFORM1.Kurt_Id'). They must count as used when referenced
    downstream by their full name OR their bare tail — never false-removed."""
    recipe = {
        "nodes": {
            "LOAD0": {"action": "load", "parameters": {
                "dataset": {"label": "Staged"},
                "fields": [
                    "TRANSFORM1.Kurt_Id",        # referenced downstream by full name
                    "AlleMails.Email",            # referenced downstream by bare tail
                    "TRANSFORM1.Truly_Unused__c",  # referenced nowhere -> removable
                ],
            }},
            "APPEND0": {"action": "appendV2", "parameters": {
                "sources": ["TRANSFORM1.Kurt_Id"],
            }},
            "FORMULA0": {"action": "formula", "parameters": {
                # bare tail reference (downstream re-qualified / renamed source)
                "expression": "trim(Email)",
            }},
        }
    }
    a = analyze_recipe(recipe)
    staged = a.objects[0]
    assert staged.unused == ["TRANSFORM1.Truly_Unused__c"]
    assert "TRANSFORM1.Kurt_Id" in staged.used
    assert "AlleMails.Email" in staged.used
