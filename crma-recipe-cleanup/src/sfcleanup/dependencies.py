"""Find where each field is referenced.

Uses the Tooling API MetadataComponentDependency, which captures references from
flows, Apex, validation rules, layouts, reports, email templates, and — important
for this project — CRM Analytics datasets/recipes that source from the field.

A field with population_rate ~0 but referenced_count > 0 must NOT be auto-deleted:
something downstream (often a CRMA Recipe) still points at it.
"""
from __future__ import annotations

from collections import Counter

from .auth import SfSession, tooling_query
from .describe import FieldMeta


def map_dependencies(session: SfSession, sobject: str, fields: list[FieldMeta]) -> dict[str, list[str]]:
    """Return {field_name: [referencing component names]} and set referenced_count."""
    soql = (
        "SELECT RefMetadataComponentName, RefMetadataComponentType, "
        "MetadataComponentName, MetadataComponentType "
        "FROM MetadataComponentDependency "
        f"WHERE RefMetadataComponentType = 'CustomField' "
        f"AND RefMetadataComponentName LIKE '{sobject}.%'"
    )
    try:
        rows = tooling_query(session, soql).get("records", [])
    except Exception:
        # Dependency API needs the right perms; degrade gracefully but flag it.
        for fm in fields:
            fm.extras["dependency_scan"] = "unavailable"
        return {}

    refs: dict[str, list[str]] = {}
    for r in rows:
        # RefMetadataComponentName comes back like "Account.My_Field__c"
        field_api = r["RefMetadataComponentName"].split(".", 1)[-1]
        consumer = f'{r["MetadataComponentType"]}:{r["MetadataComponentName"]}'
        refs.setdefault(field_api, []).append(consumer)

    counts = Counter({k: len(v) for k, v in refs.items()})
    for fm in fields:
        fm.referenced_count = counts.get(fm.name, 0)
    return refs
