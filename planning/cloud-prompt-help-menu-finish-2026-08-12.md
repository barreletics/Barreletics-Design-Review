# Cloud / new agent — Finish Help menu (2026-08-12)

**Paste this whole letter.** Desktop agent stood down after Andrew’s visual pass.

**Repo:** Barreletics-Design-Review · branch `finish-home-collections`  
**Theme:** M4 `187144929571` only — unpublished. Never publish. Never other theme IDs.  
**CLI:** Desktop already authenticated pages + theme push. Re-auth if needed; do not invent tokens.  
**Laws (FAIL CLOSED):** `.cursor/rules/anti-revert-fail-closed.mdc` · `barreletics-anti-revert` skill · Finish→Approve→Lock→Next · sole copy · no pool · **CURRENT MESSAGE WINS**  
**Type law:** `planning/help-family-type-law.md` — Page H1 = Help v8 scale · Section H2 = h2-standard · **no type-hero**

## HARD — anti-revert

You keep “fixing” by rolling back. **FORBIDDEN** without Andrew saying **`restore X`** in the CURRENT message:

- `git restore` / `git checkout` / `git show … >` on `shopify-build/sections/**` or `templates/**`
- Matching older FAQ / Size chart / live Impulse because “it looked wrong”
- Overwriting Locked mocks in place (Help v3 · FAQ v4 · PDP v16/v19)
- Touching footer · `pdp-buy-box` · `product*.json` · `value-strip` · juicer · `proof-numbers` · `index.json` · header nav #2

**Fix forward only.** If unsure what “used to look good” means → **ASK** with a preview link. Do not restore.

## Andrew visual pass (CURRENT — authority)

| Surface | Handle / URL | Verdict | Job |
|---|---|---|---|
| **Help hub** | `/pages/help` · template `help` | Built (Admin page exists) | Keep Help **v8** tiles. No Track Order. Hub → real M4 destinations. |
| **FAQ** | `/pages/faq` | **REVERTED / BAD** | Rebuild to **FAQ Definitive-v7** quiet (`docs/Barreletics FAQ - Definitive-v7.html`). Slight topic-anchor standout OK. Never overwrite Locked FAQ v4 HTML in place. Fix forward in `page.faq` / FAQ section Liquid. |
| **Shipping & returns** | `/pages/returns` | **Looks good — needs work** | Polish only. **Kill internal lede** if present (see below). Customer voice only. |
| **Start a return** | `/pages/returns-portal` | **Pretty good** | Light polish only (title = support H1). ReturnZap body stays. No Track tab. No Portal Definitive-v1 mock. |
| **Size chart** | `/pages/performance-skins-size-chart` | **FUCKED — used to look good** | Fix forward to restore good Size chart look. Do **not** `git restore`. Compare M4 vs prior good composition; ask Andrew if unclear. Chart must show M/L. No “S coming soon.” |
| **Contact** | `/pages/contact-us-form` | **GOOD — intact** | **Do not thrash.** Type-law H1 only if still wrong. Never Contact Definitive-v1. |

## Lede question (answered)

> “Clear policy language — returns, warranty, shipping, and exchanges. Product and grip questions live on FAQ.”

**NOT for customers.** That is internal/agent draft. If it appears on storefront → remove. Customer lede only (plain, helpful). Also purge from `page.shipping-retruns.json` / any returns template still carrying it. Source of truth for policy page = `/pages/returns` + `page.returns.json`.

## Workflow

1. One surface at a time.  
2. Fix in repo → push **only** to `187144929571` when needed for that surface.  
3. Send M4 preview + Theme Editor URL.  
4. Stop **AWAITING ANDREW**. Wait for `approved` / `looks good` before next surface.  
5. Never self-approve. Never lock without letter.

## Order

1. **FAQ** (highest anger — reverted)  
2. **Size chart** (broken vs prior good)  
3. **Shipping & returns** polish (customer lede; no internal note)  
4. **Start a return** light polish only  
5. Contact = leave alone unless type bug  
6. Help hub = only if tile links / chrome wrong

## Preview URLs (M4)

- Help: `https://barreletics.com/pages/help?preview_theme_id=187144929571`  
- FAQ: `https://barreletics.com/pages/faq?preview_theme_id=187144929571`  
- Returns: `https://barreletics.com/pages/returns?preview_theme_id=187144929571`  
- Portal: `https://barreletics.com/pages/returns-portal?preview_theme_id=187144929571`  
- Size: `https://barreletics.com/pages/performance-skins-size-chart?preview_theme_id=187144929571`  
- Contact: `https://barreletics.com/pages/contact-us-form?preview_theme_id=187144929571`  
- Editor pattern: `https://admin.shopify.com/store/barreletics/themes/187144929571/editor?previewPath=%2Fpages%2F{handle}`

If storefront drops preview and shows live Impulse: use Theme Editor link.

## Done when

Each claimed surface is **AWAITING ANDREW** with working M4 URL. Desktop stands down on Help family unless Andrew writes in this Mac chat.
