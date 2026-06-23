# Salesforce auth & permissions setup (fixes the blocker)

You hit auth/permission errors integrating an external tool with production
Salesforce. Here is the reliable setup. Do the **CLI path** first to unblock
today; move to **JWT** for automation.

---

## Path A — Salesforce CLI (unblock in 5 minutes, dev use)

```bash
# install the CLI (Homebrew on Mac)
brew install --cask sf-cli      # or: npm install -g @salesforce/cli

sf --version
sf org login web --alias prod   # opens browser, log in as a user with the perms below
sf org display --target-org prod   # confirm you get an access token + instance URL
```

Set `SF_AUTH_MODE=cli` and `SF_CLI_ALIAS=prod` in `.env`. The Python code reads
the CLI session, so **no credentials live in the repo**.

---

## Path B — JWT Bearer flow (headless / CI, no password)

### 1. Generate a key pair (kept OUT of git, see .gitignore)
```bash
mkdir -p secrets && cd secrets
openssl genrsa -out server.key 2048
openssl req -new -x509 -key server.key -out server.crt -days 365 \
  -subj "/CN=sfcleanup-integration"
cd ..
```

### 2. Create a Connected App (Setup -> App Manager -> New Connected App)
- Enable OAuth Settings.
- Callback URL: `http://localhost:1717/OauthRedirect` (unused by JWT but required).
- **Enable "Use digital signatures"** and upload `secrets/server.crt`.
- OAuth scopes: `api`, `refresh_token`, `offline_access`.
- Save. Copy the **Consumer Key** -> `SF_CLIENT_ID` in `.env`.

### 3. Pre-authorize the integration user
- Connected App -> Manage -> Edit Policies -> Permitted Users =
  "Admin approved users are pre-authorized".
- Assign the Connected App to the integration user's Permission Set or Profile.

### 4. Fill `.env`
```
SF_AUTH_MODE=jwt
SF_LOGIN_URL=https://login.salesforce.com   # https://test.salesforce.com for sandbox
SF_CLIENT_ID=<consumer key>
SF_USERNAME=integration.user@yourco.com
SF_JWT_KEY_PATH=./secrets/server.key
```

---

## Permission Set for the integration user (fixes most "permission" errors)

Create ONE permission set and assign it. Grant:

| Permission | Why it's needed |
|---|---|
| **API Enabled** | any REST/SOAP/Bulk call at all |
| **View Setup and Configuration** | read metadata via Tooling API (Describe enrichment, dependencies) |
| **Modify Metadata Through Metadata API Functions** | only if you will *apply* field changes later |
| **Read** on Account + **field-level security** on all 58 fields | `COUNT(field)` silently can't read fields hidden by FLS, skewing population % |
| **Use / Manage CRM Analytics** | to inventory CRMA Recipes for the migration |

Common error -> cause:
- `INVALID_SESSION_ID` -> wrong login URL (prod vs sandbox) or expired CLI session.
- `invalid_grant: user hasn't approved this consumer` -> step 3 not done.
- Field missing from Describe / count = 0 unexpectedly -> FLS not granted on that field.
- `INSUFFICIENT_ACCESS ... Metadata` -> add "View Setup and Configuration".
