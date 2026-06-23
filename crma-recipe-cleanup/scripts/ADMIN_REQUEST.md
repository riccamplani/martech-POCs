# Access request to send the Salesforce admin (Martin / Per)

**Diagnosis (verified 2026-06-23 against production):** SSO login works
(`sf org login web`), and **API access is already granted** — a SOQL query and
authenticated REST calls succeed. The blocker is specifically **CRM Analytics**:
the Analytics REST API returns `FUNCTIONALITY_NOT_ENABLED` on `/wave/recipes`
and `"No valid licenses found for the user."` on `/wave/datasets`. So the user
has **no CRM Analytics license / "Use CRM Analytics" permission**.

You do **not** need full admin — just a CRMA license and permission set assigned
to your user. Paste the block below to the admin.

---

**Subject: CRM Analytics access for the recipe-cleanup automation (read-only to start)**

Hi — for the CRMA recipe field-cleanup project I authenticate from the Salesforce
CLI / Claude Code to production. Basic API access already works; the only thing
blocking me is CRM Analytics. Could you grant my user the following (no full
admin needed)?

1. **A CRM Analytics license** assigned to my user (e.g. *CRM Analytics Plus*),
   then the matching **permission set** (*CRM Analytics Plus Admin* or *User*).
   This is the missing piece — without a license the Analytics REST API returns
   "No valid licenses found for the user."
2. **Use CRM Analytics** (and **Manage CRM Analytics** if I'll later update
   recipes) — to list and read Data Prep recipes via the Analytics REST API.
3. Access to the specific CRMA app/recipes in scope (the C360 / MC Data Prep
   recipes), so they're visible to my user.
4. **View Setup and Configuration** + read access (incl. field-level security)
   on the input objects used by the in-scope recipes — so field-usage counts
   aren't skewed by hidden fields.

> Note: **API Enabled is already in place** — no need to grant it again.

For login: SSO is fine — `sf org login web` opens the browser and authenticates
through our identity provider, so no password is needed. If you'd rather set up
headless/CI access later, a **Connected App** with a digital certificate (JWT
bearer flow) avoids passwords entirely; I can send the certificate.

Everything starts **read-only** (extract + analyze). No recipe is modified in
production without review and the before/after equivalence check.

---

## Why SSO changes the auth choice
- Username/password flow: not usable (no password under SSO). Skip it.
- `sf org login web`: **works with SSO** out of the box — use this for dev.
- JWT bearer (Connected App + cert): best for automation/CI; needs the admin to
  create the Connected App once and pre-authorize your user.
