"""CRM Analytics (CRMA / "wave") REST client for Data Prep recipes.

Verified endpoints (Analytics REST API, v62.0):
  GET /services/data/vXX.0/wave/recipes                 -> list recipes
  GET /services/data/vXX.0/wave/recipes/{id}?format=R3  -> a single recipe (metadata + nodes)

Note (important & honest): creating/modifying recipes via POST is NOT supported by
this API — recipes are authored in the recipe editor UI. So this client is built for
EXTRACTION + ANALYSIS (fully supported). The "clean" step produces a proposed JSON +
diff for review; re-applying field removals should go through the recipe editor or a
supported PUT with the correct R3 input, then be verified by running both versions
(exactly the before/after check Carlos already does).
"""
from __future__ import annotations

import json
from pathlib import Path

import requests

from ..auth import SfSession

INPUT_DIR = Path("recipes/input")


def _headers(session: SfSession) -> dict:
    return {"Authorization": f"Bearer {session.access_token}",
            "Content-Type": "application/json"}


def _base(session: SfSession) -> str:
    return f"{session.instance_url}/services/data/v{session.api_version}/wave"


def list_recipes(session: SfSession, name_filter: str | None = None) -> list[dict]:
    """Return [{id, name, label}] for all recipes, optionally filtered by name."""
    url = f"{_base(session)}/recipes"
    params = {"q": name_filter} if name_filter else {}
    out: list[dict] = []
    while url:
        resp = requests.get(url, headers=_headers(session), params=params, timeout=60)
        resp.raise_for_status()
        body = resp.json()
        for r in body.get("recipes", body.get("items", [])):
            out.append({"id": r.get("id"),
                        "name": r.get("name"),
                        "label": r.get("label") or r.get("name")})
        # follow pagination if present
        nxt = body.get("nextPageUrl")
        url = f"{session.instance_url}{nxt}" if nxt else None
        params = {}
    return out


def get_recipe(session: SfSession, recipe_id: str, fmt: str = "R3") -> dict:
    """Fetch one recipe's full definition (nodes live under the returned JSON)."""
    url = f"{_base(session)}/recipes/{recipe_id}"
    resp = requests.get(url, headers=_headers(session), params={"format": fmt}, timeout=120)
    resp.raise_for_status()
    return resp.json()


def save_recipe_json(recipe: dict, recipe_meta: dict) -> Path:
    """Persist a recipe to recipes/input/<label>__<id>.json."""
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in (recipe_meta.get("label") or "recipe"))
    path = INPUT_DIR / f"{safe}__{recipe_meta.get('id')}.json"
    path.write_text(json.dumps(recipe, indent=2))
    return path
