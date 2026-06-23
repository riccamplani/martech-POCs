"""Aggregate field usage across ALL in-scope recipes, per object.

For each object, a field is:
  - USED   if any recipe references it in its logic
  - UNUSED if it is loaded by some recipe(s) but referenced by none

This cross-recipe view is what decides safe cleanup: a field unused in one
recipe might be used in another, so we only flag fields unused EVERYWHERE.
"""
from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field as dc_field
from pathlib import Path

import yaml

from .recipe_analyzer import analyze_recipe


@dataclass
class ObjectRollup:
    object_name: str
    group: str
    loaded: set[str] = dc_field(default_factory=set)
    used: set[str] = dc_field(default_factory=set)
    used_by: dict = dc_field(default_factory=lambda: defaultdict(list))  # field -> [recipes]

    @property
    def unused(self) -> set[str]:
        return self.loaded - self.used


def _object_to_group(objects_yaml: Path) -> dict[str, str]:
    data = yaml.safe_load(objects_yaml.read_text())
    mapping = {}
    for group, objs in data.get("groups", {}).items():
        for o in objs:
            mapping[o] = group
    return mapping


def aggregate(input_dir: Path, objects_yaml: Path) -> dict[str, ObjectRollup]:
    obj_group = _object_to_group(objects_yaml)
    in_scope = set(obj_group)
    rollups: dict[str, ObjectRollup] = {}

    for fp in sorted(input_dir.glob("*.json")):
        recipe_name = fp.stem
        analysis = analyze_recipe(json.loads(fp.read_text()))
        for o in analysis.objects:
            if in_scope and o.object_name not in in_scope:
                continue  # ignore objects outside the agreed scope
            roll = rollups.get(o.object_name)
            if roll is None:
                roll = ObjectRollup(o.object_name, obj_group.get(o.object_name, "Other"))
                rollups[o.object_name] = roll
            roll.loaded.update(o.loaded)
            roll.used.update(o.used)
            for f in o.used:
                roll.used_by[f].append(recipe_name)
    return rollups
