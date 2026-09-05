# Implementation Map — Studio Program (dedicated page — UPDATED 2026-08-08, D-048)

> **UPDATED 2026-08-08 — D-048 supersedes D-042.** This map previously read
> "**Studio Program (deprecated standalone)**" and told the reader to fold Studio into
> `/pages/partners#studio-partners`. Owner direction 2026-08-08 reversed that: `/pages/studio-program`
> is a **dedicated page with its own intake form**, and `/pages/partners` is a **routing hub**.
> The prior fold instructions are struck below as history — **do not implement**.
> Current state: built, type-corrected and mobile-QA'd. See `planning/partner-programs.md` §5
> and `planning/partner-pages-qa/`.

## Reuse
- `snippets/button`; `geo-section`; `contact-cta`
- ~~Partners `#studio-partners`~~ — RETIRED 2026-08-08 (D-048). `page-partners.liquid` is now the hub that links **out** to `/pages/studio-program`.

## Modify
- `sections/page-studio-program.liquid` — **live section**, full schema, presets, Theme-Editor-editable copy
- `templates/page.studio-program.json` — **live template**: `page-studio-program` → `geo-section` → `contact-cta`
- ~~Deprecate `page-studio-program.liquid` / `page.studio-program.json`~~ — RETIRED 2026-08-08 (D-048)

## New
- None — the page is built. Remaining work is Shopify Admin page creation + form routing.

## Dependencies
- Shopify Admin page with handle `studio-program`, template assigned
- Form intake token `BL-PARTNER-STUDIO` routed to the Partners inbox (`planning/partner-programs.md` §4)
- Hub CTA on `page-partners.liquid` pointing at `/pages/studio-program`
- The `/pages/studio-program` → `/pages/partners` 301 is **retired** (`planning/m4a-redirect-map.md`)
- Do not confuse with `Section-26-NotesFromStudio` UGC — that is Home/PDP editorial, not this page
- R-10 still in force: never public partner pricing

## Technical risks
- If the retired 301 was already imported into Shopify Admin from an earlier CSV, `/pages/studio-program` is unreachable — delete it in Online Store → Navigation → URL Redirects before launch
- ~~Orphan template assignment~~ — RETIRED 2026-08-08 (D-048). The template is not an orphan.

## Recommended order
1. Create `/pages/studio-program` in Admin, assign `page.studio-program.json`
2. Confirm the retired folding 301 is absent from URL Redirects
3. Verify hub card on `/pages/partners` routes here
4. Submit a test application; confirm `BL-PARTNER-STUDIO` tagging
