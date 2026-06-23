"""Extract field metadata for an sObject.

Combines the standard Describe call (types, labels, custom flag) with the
Tooling API FieldDefinition (description, last-modified of the field definition,
business owner) so the AI classifier has rich context.
"""
from __future__ import annotations

from dataclasses import dataclass, field as dc_field

from .auth import SfSession, tooling_query


@dataclass
class FieldMeta:
    name: str
    label: str
    type: str
    custom: bool
    description: str = ""
    nillable: bool = True
    updateable: bool = True
    referenced_count: int = 0          # filled in by dependencies.py
    population_rate: float | None = None  # filled in by usage.py
    distinct_values: int | None = None
    extras: dict = dc_field(default_factory=dict)


def describe_fields(session: SfSession, sobject: str = "Account") -> list[FieldMeta]:
    desc = getattr(session.sf, sobject).describe()
    fields: list[FieldMeta] = []
    for f in desc["fields"]:
        fields.append(
            FieldMeta(
                name=f["name"],
                label=f["label"],
                type=f["type"],
                custom=f["custom"],
                nillable=f["nillable"],
                updateable=f["updateable"],
            )
        )
    _enrich_with_tooling(session, sobject, fields)
    return fields


def _enrich_with_tooling(session: SfSession, sobject: str, fields: list[FieldMeta]) -> None:
    """Pull human-authored descriptions from FieldDefinition (Tooling API)."""
    soql = (
        "SELECT QualifiedApiName, Description, BusinessOwner.Name "
        "FROM FieldDefinition "
        f"WHERE EntityDefinition.QualifiedApiName = '{sobject}'"
    )
    try:
        rows = tooling_query(session, soql).get("records", [])
    except Exception:
        return  # description is a nice-to-have; never block the run on it
    by_name = {r["QualifiedApiName"]: r for r in rows}
    for fm in fields:
        rec = by_name.get(fm.name)
        if rec:
            fm.description = rec.get("Description") or ""
            owner = (rec.get("BusinessOwner") or {})
            if owner:
                fm.extras["business_owner"] = owner.get("Name")
