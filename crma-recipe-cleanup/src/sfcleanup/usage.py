"""Measure how much each field is actually used.

population_rate = COUNT(field) / COUNT(Id)   (SOQL COUNT(field) skips NULLs)

We batch many COUNT() expressions into as few SOQL calls as possible to stay
under the SELECT-clause limit, and skip field types SOQL can't aggregate
(textarea/long text, base64, address/location compounds, encrypted).
"""
from __future__ import annotations

from .auth import SfSession
from .describe import FieldMeta

# Types you cannot COUNT() directly in SOQL.
_UNCOUNTABLE = {"textarea", "base64", "address", "location", "encryptedstring"}
_MAX_AGGS_PER_QUERY = 40  # keep well under the SELECT-clause limit


def measure_usage(session: SfSession, sobject: str, fields: list[FieldMeta]) -> None:
    total = _total_rows(session, sobject)
    if total == 0:
        for fm in fields:
            fm.population_rate = 0.0
        return

    countable = [f for f in fields if f.type not in _UNCOUNTABLE and f.name != "Id"]
    for chunk in _chunks(countable, _MAX_AGGS_PER_QUERY):
        exprs = ", ".join(f"COUNT({f.name}) {f.name}" for f in chunk)
        soql = f"SELECT {exprs} FROM {sobject}"
        row = session.sf.query(soql)["records"][0]
        for f in chunk:
            non_null = row.get(f.name) or 0
            f.population_rate = round(non_null / total, 4)

    # Fields we couldn't count get None -> surfaced as "REVIEW" downstream.
    for f in fields:
        if f.type in _UNCOUNTABLE:
            f.population_rate = None


def _total_rows(session: SfSession, sobject: str) -> int:
    res = session.sf.query(f"SELECT COUNT(Id) total FROM {sobject}")
    return res["records"][0]["total"] if res["records"] else 0


def _chunks(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i : i + size]
