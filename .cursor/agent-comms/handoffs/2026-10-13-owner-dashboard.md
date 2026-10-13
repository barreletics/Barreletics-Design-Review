# Owner dashboard: handoff (2026-10-13)

**Live URL:** https://barreletics.github.io/private-wow-snapshot/ (staticrypt password gate, home-screen installable)
**Password:** /workspace/owner-dashboard-preview/PASSWORD.txt (chmod 600). Also stored as the repo secret OWNER_PAGE_STATICRYPT_PASSWORD.

## Repos
- `barreletics/owner-dashboard` (PRIVATE): code, workflow `.github/workflows/publish.yml`, all secrets. Local clone: /workspace/owner-dashboard-repo
- `barreletics/private-wow-snapshot` (PUBLIC, Pages from main /): only the encrypted `index.html`, manifest, icons and `.nojekyll`. Never commit plaintext here.
- The old branch `cursor/owner-dashboard-v1-6beb` / PR #16 in barreletics-ops is superseded and was not touched.

## Schedule
publish.yml runs at 11:00 and 23:00 UTC (7 AM / 7 PM ET) and on manual dispatch. Steps: pull the br-paid-dashboard latest.json (token), refresh_owner.py, build_static.py, inject PWA tags, staticrypt 3.5.4 (remember up to 30 days), scripts/check_leaks.py, push to the public repo.

## Secrets (owner-dashboard; values never in git)
OWNER_PAGE_STATICRYPT_PASSWORD, SNAPSHOT_DEPLOY_TOKEN (Andrew's fine-grained PAT, also GITHUB_DASHBOARD_TOKEN on the box), SHOPIFY_CLIENT_ID, SHOPIFY_CLIENT_SECRET, XERO_CLIENT_ID, XERO_CLIENT_SECRET (the working "_NEW" value), META_ACCESS_TOKEN, GA_SERVICE_ACCOUNT_JSON (normalized JSON for dashboard-reader@valiant-bonbon-489502-g4), HELPSCOUT_APP_ID, HELPSCOUT_APP_SECRET.

## Sources (all 8 live as of 12:43 PM ET)
Shopify, Xero (Checking 5003, card 4473, bills via the granted scopes and the balance-sheet report), Meta, GA4 (paid/organic/overall split), Help Scout (mailbox 369185; return zaps identified by tag `returnzap`, sender returns@returnzap.com, or "New return for Shopify order #N requires approval"; drafts by tag `grok draft ready`), Google/Pinterest (via the br-paid-dashboard cache).

## Open items
- The cash tile uses "Barreletics Checking 5003 (new)"; Xero has no Chase bank account. Confirm with Andrew (config `xero_chase_account_name_contains`).
- Check the safe-payout formula with Andrew (checking - $15k reserve - bills due in 30d).
- Low stock lists 12 dead, out-of-stock SKUs (no sales in 28d). Consider hiding discontinued colors.
- Ad spend comes from the paid-dash 7d cache. Meta's live spend is used only when it's higher.
- The box env GA_SERVICE_ACCOUNT_JSON is in a flattened format. The code tolerates it, but re-save it as real JSON if possible.
- The URL contains the org slug. Add a custom domain if needed.
- Actions Node 20 deprecation warning (harmless for now; bump the action versions later).
