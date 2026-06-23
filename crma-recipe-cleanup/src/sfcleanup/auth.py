"""Authenticated Salesforce access.

Two modes:
  - "cli": reuse a Salesforce CLI session (`sf org login web --alias prod`).
           Zero secrets in the repo; best for local development.
  - "jwt": OAuth 2.0 JWT Bearer flow with a Connected App + certificate.
           No password, no interactive login; best for CI / headless automation.

Both return a `simple_salesforce.Salesforce` instance plus the raw access token
and instance URL (needed for direct Tooling API calls).
"""
from __future__ import annotations

import json
import subprocess
import time
import urllib.parse
from dataclasses import dataclass

import jwt
import requests
from simple_salesforce import Salesforce

from config.settings import settings


class SalesforceRestError(RuntimeError):
    """A Salesforce REST API error (carries the errorCode for callers to branch on)."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")


@dataclass
class SfSession:
    sf: Salesforce
    access_token: str
    instance_url: str
    api_version: str
    auth_mode: str = "cli"
    alias: str | None = None


def _from_cli(alias: str, api_version: str) -> SfSession:
    """Reuse an existing CLI auth so we never store credentials in the repo.

    NOTE: recent `sf` CLI *masks* the access token in `sf org display` output
    (and encrypts it at rest), so the returned token is NOT usable for direct
    REST/`simple_salesforce` calls. For cli auth we therefore route REST through
    the CLI itself (`rest_get` -> `sf api request rest`), which decrypts and
    authenticates internally. The masked token is kept only for reference.
    """
    out = subprocess.run(
        ["sf", "org", "display", "--target-org", alias, "--json"],
        capture_output=True, text=True, check=True,
    )
    info = json.loads(out.stdout)["result"]
    token = info.get("accessToken", "")
    instance = info["instanceUrl"]
    sf = Salesforce(instance_url=instance, session_id=token, version=api_version)
    return SfSession(sf, token, instance, api_version, auth_mode="cli", alias=alias)


def _from_jwt(api_version: str) -> SfSession:
    """Server-to-server auth. Sign a JWT with the private key and exchange it."""
    with open(settings.jwt_key_path, "rb") as fh:
        private_key = fh.read()

    now = int(time.time())
    claims = {
        "iss": settings.client_id,          # Connected App consumer key
        "sub": settings.username,            # integration user
        "aud": settings.login_url,           # login vs test
        "exp": now + 180,
    }
    assertion = jwt.encode(claims, private_key, algorithm="RS256")

    resp = requests.post(
        f"{settings.login_url}/services/oauth2/token",
        data={
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": assertion,
        },
        timeout=30,
    )
    resp.raise_for_status()
    payload = resp.json()
    token = payload["access_token"]
    instance = payload["instance_url"]
    sf = Salesforce(instance_url=instance, session_id=token, version=api_version)
    return SfSession(sf, token, instance, api_version, auth_mode="jwt")


def get_session() -> SfSession:
    if settings.auth_mode == "jwt":
        return _from_jwt(settings.api_version)
    return _from_cli(settings.cli_alias, settings.api_version)


# --------------------------------------------------------------------------- #
# REST transport (works for both auth modes) + connectivity smoke test
# --------------------------------------------------------------------------- #
def _cli_rest(alias: str, path: str) -> dict | list:
    """GET a REST resource via the CLI's own (decrypted) auth.

    `sf api request rest` writes the raw response body to stdout. Salesforce
    API errors come back as a list like [{"errorCode": ..., "message": ...}].
    """
    proc = subprocess.run(
        ["sf", "api", "request", "rest", path, "--target-org", alias],
        capture_output=True, text=True,
    )
    body = proc.stdout.strip()
    if not body:
        raise RuntimeError(f"sf api request returned no output: {proc.stderr.strip()}")
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        raise RuntimeError(f"unexpected response from sf api request: {body[:300]}")
    if isinstance(data, list) and data and isinstance(data[0], dict) and data[0].get("errorCode"):
        err = data[0]
        raise SalesforceRestError(err.get("errorCode", "ERROR"), err.get("message", ""))
    return data


def rest_get(session: SfSession, path: str, params: dict | None = None) -> dict | list:
    """GET a Salesforce REST resource, regardless of auth mode.

    `path` is the API path beginning with `/services/...`. For cli auth this
    goes through `sf api request rest` (the displayed token is masked); for jwt
    auth it uses the real bearer token directly.
    """
    if params:
        path = f"{path}?{urllib.parse.urlencode(params)}"
    if session.auth_mode == "cli" and session.alias:
        return _cli_rest(session.alias, path)
    resp = requests.get(
        f"{session.instance_url}{path}",
        headers={"Authorization": f"Bearer {session.access_token}"},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


def smoke_test(session: SfSession) -> str:
    """Verify the session can actually call Salesforce, and report whether the
    CRM Analytics API (the recipe-cleanup gate) is reachable. Returns a
    human-readable multi-line status string; never raises for the CRMA probe.
    """
    v = session.api_version
    lines = [f"auth_mode={session.auth_mode}  org={session.instance_url}  api=v{v}"]

    # 1) Basic auth + API reachability (no special license needed).
    try:
        limits = rest_get(session, f"/services/data/v{v}/limits")
        daily = limits.get("DailyApiRequests", {}) if isinstance(limits, dict) else {}
        used = daily.get("Max", 0) - daily.get("Remaining", 0) if daily else None
        lines.append("✓ Auth + API OK"
                     + (f"  (API calls today: {used}/{daily.get('Max')})" if daily else ""))
    except (SalesforceRestError, requests.HTTPError, RuntimeError) as e:
        return "\n".join(lines + [f"✗ Auth/API FAILED: {e}"])

    # 2) CRM Analytics probe — the actual blocker for `extract`.
    try:
        recipes = rest_get(session, f"/services/data/v{v}/wave/recipes")
        n = len(recipes.get("recipes", recipes.get("items", []))) if isinstance(recipes, dict) else 0
        lines.append(f"✓ CRM Analytics reachable — {n} recipe(s) visible; `extract` can run")
    except SalesforceRestError as e:
        lines.append(f"✗ CRM Analytics BLOCKED [{e.code}]: {e.message}")
        lines.append("  → assign a CRM Analytics license to this user "
                     "(see scripts/ADMIN_REQUEST.md)")
    except (requests.HTTPError, RuntimeError) as e:
        lines.append(f"✗ CRM Analytics probe error: {e}")

    return "\n".join(lines)


def tooling_query(session: SfSession, soql: str) -> dict:
    """Run a Tooling API query (used for FieldDefinition + dependency graph)."""
    url = f"{session.instance_url}/services/data/v{session.api_version}/tooling/query"
    resp = requests.get(
        url,
        headers={"Authorization": f"Bearer {session.access_token}"},
        params={"q": soql},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()
