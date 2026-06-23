"""Central configuration, loaded from environment (.env)."""
from __future__ import annotations

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    auth_mode: str = os.getenv("SF_AUTH_MODE", "cli")
    cli_alias: str = os.getenv("SF_CLI_ALIAS", "prod")
    login_url: str = os.getenv("SF_LOGIN_URL", "https://login.salesforce.com")
    client_id: str = os.getenv("SF_CLIENT_ID", "")
    username: str = os.getenv("SF_USERNAME", "")
    jwt_key_path: str = os.getenv("SF_JWT_KEY_PATH", "./secrets/server.key")
    api_version: str = os.getenv("SF_API_VERSION", "62.0")

    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    claude_model: str = os.getenv("CLAUDE_MODEL", "claude-opus-4-8")

    population_threshold: float = float(os.getenv("POPULATION_THRESHOLD", "0.02"))


settings = Settings()
