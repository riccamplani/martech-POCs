"""Tests that run without a live Salesforce org."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sfcleanup.describe import FieldMeta
from sfcleanup.classify import _rule_hint


def test_referenced_field_is_kept():
    f = FieldMeta(name="X__c", label="X", type="text", custom=True,
                  population_rate=0.0, referenced_count=3)
    assert "KEEP" in _rule_hint(f)


def test_unused_custom_field_is_deprecate_candidate():
    f = FieldMeta(name="Old__c", label="Old", type="text", custom=True,
                  population_rate=0.0, referenced_count=0)
    assert "DEPRECATE" in _rule_hint(f)


def test_uncountable_field_goes_to_review():
    f = FieldMeta(name="Notes__c", label="Notes", type="textarea", custom=True,
                  population_rate=None, referenced_count=0)
    assert "REVIEW" in _rule_hint(f)
