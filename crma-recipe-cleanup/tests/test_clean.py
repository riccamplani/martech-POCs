"""Tests for editor-import-format output (clean.build_editor_recipe)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sfcleanup.crma.recipe_analyzer import analyze_recipe
from sfcleanup.crma.clean import build_editor_recipe


def _recipe():
    """API-shaped extract: envelope + recipeDefinition with runMode and a
    ui.hiddenColumns entry that references a field we expect to be removed."""
    return {
        "id": "05vXXXXXXXXXXXXXXX",          # envelope keys that must NOT survive
        "label": "Test Recipe",
        "createdBy": {"name": "x"},
        "url": "/services/data/v62.0/wave/recipes/05v",
        "recipeDefinition": {
            "version": 62.0,
            "runMode": "full",               # must be dropped (not editor format)
            "nodes": {
                "LOAD0": {"action": "load", "parameters": {
                    "dataset": {"label": "Acct"},
                    "fields": ["KeepMe__c", "DropMe__c"],
                }},
                "FILTER0": {"action": "filter", "parameters": {
                    "filterExpressions": [{"field": "KeepMe__c", "operator": "=="}],
                }},
            },
            "ui": {
                "nodes": {"LOAD0": {"label": "Acct", "type": "LOAD_DATASET",
                                    "parameters": {"sampleSize": 10000}}},
                "connectors": [],
                "hiddenColumns": ["DropMe__c", {"name": "KeepMe__c"}],
            },
        },
    }


def test_editor_format_shape_and_trim():
    recipe = _recipe()
    analysis = analyze_recipe(recipe)
    editor = build_editor_recipe(recipe, analysis)

    # 1) exactly the editor keys, in order; no envelope/runMode leakage
    assert list(editor.keys()) == ["version", "nodes", "ui"]
    assert "runMode" not in editor and "recipeDefinition" not in editor
    assert "id" not in editor and "label" not in editor
    assert editor["version"] == 62.0

    # 2) load node trimmed to the used set
    fields = [f if isinstance(f, str) else f["name"]
              for f in editor["nodes"]["LOAD0"]["parameters"]["fields"]]
    assert fields == ["KeepMe__c"]

    # 3) ui kept consistent: hiddenColumns entry for the removed field is gone,
    #    the kept-field entry remains
    assert editor["ui"]["hiddenColumns"] == [{"name": "KeepMe__c"}]


def test_editor_does_not_mutate_source():
    recipe = _recipe()
    analysis = analyze_recipe(recipe)
    build_editor_recipe(recipe, analysis)
    # original definition untouched (deep-copied)
    src_fields = recipe["recipeDefinition"]["nodes"]["LOAD0"]["parameters"]["fields"]
    assert src_fields == ["KeepMe__c", "DropMe__c"]
