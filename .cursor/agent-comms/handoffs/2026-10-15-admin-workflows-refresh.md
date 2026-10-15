# Admin workflows refresh — 2026-10-15 (old bot 5ca5d970-8f7e-4c25-abda-cadbdef432b0, 267 msgs, idle since 9/30)

## Role
Barreletics Admin workflows (Ops section): ops blockers, not theme QC or influencer codes. Owns box Shopify Admin/API/CLI auth and scopes, Cloudflare/Turnstile blockers, and other admin/session/ops workflows Andrew parks here. Front-door routing is NOT this bot's job (that's Grok Bot c4d12f5c). Full rules are in your profile description.

## Settled
- Shopify Admin's Cloudflare is Shopify's own; no allowlist exists for the box's datacenter IP. Don't try to get around it.
- API path works from the box with the client-credentials grant (24-hour token). As of 10-15 the app "Grok Bot Admin" is installed (env SHOPIFY_GROK_ADMIN_CLIENT_ID / _SECRET; scopes write_markets, write_shipping, write_orders, write_products, write_inventory, write_publications, read_locations). The older "Grok Inventory" app is read-only. Still need Andrew's Chrome: Shopify Email campaigns, app installs/billing, staff, payments, domains, most store settings.
- Live theme backup: old live theme 185687998755 ("Live Barreletics - Brian Go Live", 406 files) is in repo barreletics/Barreletics-Design-Review, branch finish-home-collections, folder backups/live-theme-185687998755-2026-09-29; Andrew also duplicated it in Shopify. OK to uninstall Theme Updater & Backup app. Keep Sitemap NoIndex Pro ($3.49/mo) for now.

## Open (waiting on Andrew's go)
1. Go-live backup setup was promised "when draft theme 187144929571 goes live". It went LIVE on 10/8 and nobody kicked this off. Plan: weekly dated snapshot of the live theme to GitHub; Shopify duplicate before big changes (keep 2-3, 20-theme cap); monthly content export (products, pages, blogs, nav); monthly theme release-notes check; cancel Theme Updater & Backup app. Needs Andrew's OK before building any routine. Any push to theme 187144929571 needs Andrew's explicit go (it's live).

## Routines
None known on the old bot.
