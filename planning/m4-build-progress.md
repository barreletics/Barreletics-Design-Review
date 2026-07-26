# M4 Production Build — Progress

**Draft theme only:** `187143618851` (never live, never other backups)  
**Editor:** https://admin.shopify.com/store/barreletics/themes/187143618851/editor  
**2a:** Pre-approved per handoff KEEP/DROP  
**Tracker updated:** 2026-07-26

| ID | Item | Status |
|----|------|--------|
| 0 | Draft ID + hard rule (user + project) | **done** |
| 0b | Repo backup `backups/m4-pre-phase1-2026-07-26/` + git commit | **done** |
| 0c | Pull draft theme into backup before first push | **blocked** — needs Shopify CLI login |
| 1 | Shell: tokens, layout, header/footer sections + chrome.css/js | **done locally** — push pending auth |
| 1b | Heroes (fullbleed / home-split / collection-split) | pending |
| 2a | KEEP/DROP (handoff) | **done** (pre-approved) |
| 2b | fifty-fifty → visual-mosaic → variant-grid | pending |
| 2c | Wire Home → Collection → SEO → PDP | pending |
| 3 | Help / FAQ / Journal + thin pages | pending |
| 4 | Lighthouse / a11y / metafields | pending |
| PUBLISH | Owner only | **blocked** |

## Phase 1 local deliverables
- BZ-020 tokens in `design-tokens.css` + base type utilities
- `sections/announcement-strip.liquid`, `header.liquid`, `footer.liquid`
- `header-group.json` / `footer-group.json` wired in `layout/theme.liquid`
- Menus via Theme Editor link lists (not hardcoded)
- CSS/JS extracted to `assets/chrome.css` + `assets/chrome.js`

## Blocker
Shopify CLI auth required before pull/push to `187143618851`.
