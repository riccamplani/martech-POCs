---
description: Check or establish Salesforce auth for this project (SSO/CLI), read-only
argument-hint: [org-alias, default "prod"]
allowed-tools: Bash(sf:*)
---
You are verifying Salesforce connectivity for this project. Do NOT modify anything.

1. Set ALIAS to `$ARGUMENTS` if non-empty, otherwise `prod`.
2. Run `sf org display --target-org ALIAS --json` and report Connected Status,
   username, instance URL, and API version.
3. If it fails:
   - If the error mentions API being disabled or insufficient access, explain that
     the user's Salesforce user is missing the **API Enabled** permission and point
     them to scripts/ADMIN_REQUEST.md — do not attempt workarounds.
   - If there is simply no session, instruct them to run
     `sf org login web --alias ALIAS` (this uses their SSO; no password needed).
4. Never print or store the access token in any file.
