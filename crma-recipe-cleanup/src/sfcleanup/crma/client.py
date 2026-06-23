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

from ..auth import SfSession, rest_get

INPUT_DIR = Path("recipes/input")


def _base_path(session: SfSession) -> str:
    return f"/services/data/v{session.api_version}/wave"


def list_recipes(session: SfSession, name_filter: str | None = None) -> list[dict]:
    """Return [{id, name, label}] for all recipes, optionally filtered by name.

    Uses the shared `rest_get` transport, so it works under both CLI auth
    (routed through `sf api request rest`) and JWT auth (direct bearer token).
    """
    path = f"{_base_path(session)}/recipes"
    params = {"q": name_filter} if name_filter else None
    out: list[dict] = []
    while path:
        body = rest_get(session, path, params=params)
        for r in body.get("recipes", body.get("items", [])):
            out.append({"id": r.get("id"),
                        "name": r.get("name"),
                        "label": r.get("label") or r.get("name")})
        # follow pagination if present (nextPageUrl is an absolute API path)
        path = body.get("nextPageUrl")
        params = None
    return out


def get_recipe(session: SfSession, recipe_id: str, fmt: str = "R3") -> dict:
    """Fetch one recipe's full definition (nodes live under the returned JSON)."""
    path = f"{_base_path(session)}/recipes/{recipe_id}"
    return rest_get(session, path, params={"format": fmt})


def save_recipe_json(recipe: dict, recipe_meta: dict) -> Path:
    """Persist a recipe to recipes/input/<label>__<id>.json."""
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in (recipe_meta.get("label") or "recipe"))
    path = INPUT_DIR / f"{safe}__{recipe_meta.get('id')}.json"
    path.write_text(json.dumps(recipe, indent=2))
    return path
