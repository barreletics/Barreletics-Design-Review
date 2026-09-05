# Implementation Map — Wholesale (dedicated page — UPDATED 2026-08-08, D-048)

> **UPDATED 2026-08-08 — D-048 supersedes D-042.** This map previously read
> "**Wholesale (deprecated standalone)**" and told the reader to fold Wholesale into
> `/pages/partners#wholesale`. Owner direction 2026-08-08 reversed that: `/pages/wholesale` is a
> **dedicated page with its own intake form**, and `/pages/partners` is a **routing hub**.
> The prior fold instructions are struck below as history — **do not implement**.
> Current state: built, type-corrected and mobile-QA'd. See `planning/partner-programs.md` §5
> and `planning/partner-pages-qa/`.

## Reuse
- `snippets/button`; `geo-section`; `contact-cta` — the dedicated page composes with these
- ~~`sections/page-partners.liquid` `#wholesale` — **canonical**~~ — RETIRED 2026-08-08 (D-048). `page-partners.liquid` is now the hub that links **out** to `/pages/wholesale`.

## Modify
| File | Change |
|------|--------|
| `sections/page-wholesale.liquid` | **Live section** — full schema, presets, Theme-Editor-editable copy. Assign in Admin. |
| `templates/page.wholesale.json` | **Live template** — `page-wholesale` → `geo-section` → `contact-cta` |
| ~~`sections/page-wholesale.liquid`~~ | ~~Deprecation banner / comment; do not assign in Admin~~ — RETIRED 2026-08-08 (D-048) |
| ~~`templates/page.wholesale.json`~~ | ~~Mark deprecated in comment if possible~~ — RETIRED 2026-08-08 (D-048) |

## New
- None — the page is built. Remaining work is Shopify Admin page creation + form routing (owner/Brian).

## Dependencies
- Shopify Admin page with handle `wholesale`, template assigned
- Form intake token `BL-PARTNER-WHOLESALE` routed to the Partners inbox (`planning/partner-programs.md` §4)
- Hub CTA on `page-partners.liquid` pointing at `/pages/wholesale`
- ~~Redirects M4A → `/pages/partners`~~ — RETIRED 2026-08-08 (D-048). The `/pages/wholesale` → `/pages/partners` 301 is retired in `planning/m4a-redirect-map.md`; it would make this page unreachable. `/pages/wholesale-calculator` → `/pages/partners` **remains correct**.
- ~~R-01 HOLD~~ — SUPERSEDED 2026-08-08 by D-048 (`specs/frozen/wholesale.md`)
- R-10 still in force: never public wholesale pricing/minimums

## Technical risks
- If the retired 301 was already imported into Shopify Admin from an earlier CSV, `/pages/wholesale` is unreachable — delete it in Online Store → Navigation → URL Redirects before launch
- ~~Live page still assigned orphan template~~ — RETIRED 2026-08-08 (D-048). The template is not an orphan.

## Recommended order
1. Create `/pages/wholesale` in Admin, assign `page.wholesale.json`
2. Confirm the retired folding 301 is absent from URL Redirects
3. Verify hub card on `/pages/partners` routes here
4. Submit a test application; confirm `BL-PARTNER-WHOLESALE` tagging
