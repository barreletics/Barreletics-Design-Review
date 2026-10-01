# Implementation Map — Ambassador (dedicated page — UPDATED 2026-08-08, D-048)

> **UPDATED 2026-08-08 — D-048 supersedes D-042.** This map previously read
> "**Ambassador (deprecated standalone)**" and told the reader to fold Ambassador into
> `/pages/partners#ambassadors`. Owner direction 2026-08-08 reversed that: `/pages/ambassador` is a
> **dedicated page with its own intake form**, and `/pages/partners` is a **routing hub**.
> The prior fold instructions are struck below as history — **do not implement**.
> Current state: built, type-corrected and mobile-QA'd. See `planning/partner-programs.md` §5
> and `planning/partner-pages-qa/`.

## Reuse
- `snippets/button`; `geo-section`; `contact-cta`
- ~~Partners `#ambassadors`~~ — RETIRED 2026-08-08 (D-048). `page-partners.liquid` is now the hub that links **out** to `/pages/ambassador`.

## Modify
- `sections/page-ambassador.liquid` — **live section**, full schema, presets, Theme-Editor-editable terms (commission %, discounts, thresholds are settings, not hardcoded)
- `templates/page.ambassador.json` — **live template**: `page-ambassador` → `geo-section` → `contact-cta`
- ~~Deprecate `page-ambassador.liquid` / `page.ambassador.json`~~ — RETIRED 2026-08-08 (D-048)

## New
- None built here (affiliate embed still deferred, R-11). Remaining work is Shopify Admin page creation + form routing.

## Dependencies
- Shopify Admin page with handle `ambassador`, template assigned
- Form intake token `BL-PARTNER-AMBASSADOR` routed to the Partners inbox (`planning/partner-programs.md` §4)
- Hub CTA on `page-partners.liquid` pointing at `/pages/ambassador`
- The `/pages/ambassador` → `/pages/partners` 301 is **retired** (`planning/m4a-redirect-map.md`); `/pages/become-an-affiliate` → `/pages/partners` **remains correct**
- ~~Partners form Program Interest = Ambassador~~ — RETIRED 2026-08-08 (D-048). Ambassadors now fill the dedicated form; the hub's fallback form is for people who don't know which program fits.
- R-10 still in force: never public commission rates

## Technical risks
- If the retired 301 was already imported into Shopify Admin from an earlier CSV, `/pages/ambassador` is unreachable — delete it in Online Store → Navigation → URL Redirects before launch
- Ambassador terms in the schema are a **proposal, not approved** (`planning/partner-programs.md` §risks)
- ~~Same as wholesale orphans~~ — RETIRED 2026-08-08 (D-048)

## Recommended order
1. Create `/pages/ambassador` in Admin, assign `page.ambassador.json`
2. Confirm the retired folding 301 is absent from URL Redirects
3. Verify hub card on `/pages/partners` routes here
4. Submit a test application; confirm `BL-PARTNER-AMBASSADOR` tagging
