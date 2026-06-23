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
from dataclasses import dataclass

import jwt
import requests
from simple_salesforce import Salesforce

from config.settings import settings


@dataclass
class SfSession:
    sf: Salesforce
    access_token: str
    instance_url: str
    api_version: str


def _from_cli(alias: str, api_version: str) -> SfSession:
    """Pull an existing CLI auth so we never store credentials in the repo."""
    out = subprocess.run(
        ["sf", "org", "display", "--target-org", alias, "--json"],
        capture_output=True, text=True, check=True,
    )
    info = json.loads(out.stdout)["result"]
    token = info["accessToken"]
    instance = info["instanceUrl"]
    sf = Salesforce(instance_url=instance, session_id=token, version=api_version)
    return SfSession(sf, token, instance, api_version)


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
    return SfSession(sf, token, instance, api_version)


def get_session() -> SfSession:
    if settings.auth_mode == "jwt":
        return _from_jwt(settings.api_version)
    return _from_cli(settings.cli_alias, settings.api_version)


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
