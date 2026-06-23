"""Ask Claude to recommend KEEP / REVIEW / DEPRECATE for each field.

The model sees population rate, dependency count, type, and description, plus a
rules-based pre-classification, and returns structured JSON. This keeps a human
in the loop: nothing is deleted from the model's say-so alone.
"""
from __future__ import annotations

import json

from anthropic import Anthropic

from config.settings import settings
from .describe import FieldMeta

_SYSTEM = """You are a Salesforce data architect rationalizing an sObject's fields.
For each field decide one of: KEEP, REVIEW, DEPRECATE.
Rules of thumb:
- KEEP: standard identity/system fields (Id, Name, OwnerId, CreatedDate...),
  high population, or referenced by any downstream component.
- DEPRECATE: custom field, near-zero population, AND zero references.
- REVIEW: anything ambiguous, or population that could not be measured.
Never recommend DEPRECATE for a field with referenced_count > 0.
Return ONLY a JSON array, no prose, no markdown fences. Each item:
{"name": str, "recommendation": "KEEP|REVIEW|DEPRECATE", "reason": str}"""


def _rule_hint(f: FieldMeta) -> str:
    if f.referenced_count > 0:
        return "KEEP (has references)"
    if f.population_rate is None:
        return "REVIEW (uncountable type)"
    if f.custom and f.population_rate < settings.population_threshold:
        return "DEPRECATE candidate"
    return "KEEP candidate"


def classify_fields(fields: list[FieldMeta]) -> list[dict]:
    client = Anthropic(api_key=settings.anthropic_api_key)
    rows = [
        {
            "name": f.name,
            "type": f.type,
            "custom": f.custom,
            "population_rate": f.population_rate,
            "referenced_count": f.referenced_count,
            "description": f.description[:280],
            "rule_hint": _rule_hint(f),
        }
        for f in fields
    ]
    msg = client.messages.create(
        model=settings.claude_model,
        max_tokens=4000,
        system=_SYSTEM,
        messages=[{"role": "user", "content": json.dumps(rows, indent=2)}],
    )
    text = "".join(b.text for b in msg.content if b.type == "text").strip()
    text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(text)
