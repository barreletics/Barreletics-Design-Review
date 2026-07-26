# M4 Production Build — Progress

**Delivery:** GitHub / `shopify-build/` = Design System **master**; Shopify = disposable QA runtime only  
**Handoff:** approved repo → Brian → production  
**Shopify push:** disposable draft QA **only** when Andrew names a theme ID in-message; never invent; never live  
**Retired draft ID:** `187143618851` (dead — do not use)  
**2a:** Pre-approved per handoff KEEP/DROP  
**Tracker updated:** 2026-07-26 (`split-hero` built — **in review, not frozen**)

## ARCHITECTURE APPROVED

**Contract:** `planning/m4-section-library-CONTRACT.md` (frozen 2026-07-26)

| Gate | Status |
|------|--------|
| Architecture decisions (H1–X3) | **APPROVED** |
| Final inventory CONTRACT | **written** — acknowledged |
| Next production work | **`split-hero` IN REVIEW** — not frozen; no other sections |
| Shopify | **none** |

- Deliverable = **section library in repo**, not homepage assembly on Shopify  
- Proposal doc superseded: `planning/m4-section-library-architecture.md`  
- **`split-hero`** replaces `home-split-hero` — **in review, not frozen**  
- Blocked until `split-hero` frozen: every other new/rebuild marketing section  
- No parallel builds; one section at a time

| ID | Item | Status |
|----|------|--------|
| 0 | Draft ID + hard rule (user + project) | **superseded** — draft abandoned; repo-only rules updated |
| 0b | Repo backup `backups/m4-pre-phase1-2026-07-26/` + git commit | **done** |
| 0c | Pull draft theme into backup before first push | **done** → `backups/.../draft-theme-pull/` (historical) |
| 1 | Shell: tokens, layout, header/footer in `shopify-build/` | **done** (live untouched; draft path abandoned) |
| ARCH | Section library architecture | **APPROVED** → CONTRACT |
| CONTRACT | Final section inventory contract | **done** → `planning/m4-section-library-CONTRACT.md` |
| 1b | Heroes / section library | **`split-hero` IN REVIEW** (not frozen); next section **blocked** |
| AUDIT | Shell audit report | **done** → `planning/m4-shell-audit-report.md` |
| 2.0 | Post–layout-swap functional QA | **PASS** → `planning/m4-phase-2.0-qa-report.md` (historical draft QA) |
| 2a | KEEP/DROP (handoff) | **done** (pre-approved) |
| 2b | fifty-fifty → visual-mosaic → variant-grid | **blocked** until `split-hero` frozen |
| 2c | Wire Home → Collection → SEO → PDP | **blocked**; assembly = Brian after repo freeze |
| 3 | Help / FAQ / Journal + thin pages | **blocked** |
| 4 | Lighthouse / a11y / metafields | pending |
| HANDOFF | Repo → Brian via GitHub | **operating model** |
| PUBLISH | Owner only | **blocked** |

## Section freeze queue

| Section | Status | Notes |
|---------|--------|-------|
| `split-hero` | **IN REVIEW** | Built in repo; DS gaps from audit addressed; awaiting Andrew approve → freeze. Docs: `planning/sections/split-hero.md` |
| `hero-fullbleed` | **blocked** | Do not start until `split-hero` frozen |
| All other library sections | **blocked** | One at a time after freeze |

## Phase 1 local deliverables
- BZ-020 tokens in `design-tokens.css` + base type utilities
- `sections/announcement-strip.liquid`, `header.liquid`, `footer.liquid`
- `header-group.json` / `footer-group.json` wired in `layout/theme.liquid`
- Menus via Theme Editor link lists (not hardcoded)
- CSS/JS extracted to `assets/chrome.css` + `assets/chrome.js`

## Theme IDs (historical / forbidden)

- **LIVE (never touch):** `185687998755` — Live Barreletics - Brian Go Live
- **RETIRED DRAFT (do not use):** `187143618851` — deleted / abandoned
- Other library copies: **forbidden** unless Andrew names a new ID in-message
