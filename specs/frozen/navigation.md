# Frozen Spec — Navigation

---
status: FROZEN
surface: Header (`snippets/header-nav.liquid` + announcement)
authority: Doc 11 + R-03, R-04, R-12 (PR #18); D-048 Partner programs not in primary
updated: 2026-08-08 (was 2026-07-20 — partner row only)
---

> **UPDATED 2026-08-08 — D-048 supersedes D-042.** The "keep Partners out of primary nav" call is
> unchanged, but its authority moved. There are now **three dedicated program pages**
> (`/pages/wholesale`, `/pages/studio-program`, `/pages/ambassador`) plus `/pages/partners` as a
> **routing hub** — not one consolidated page. None of the four belong in primary nav; footer / Contact
> quick links remain the entry point (`specs/implementation-maps/footer.md`). The three folding 301s
> are retired in `planning/m4a-redirect-map.md`. Nothing else in this spec changes.

## Applied decisions
| ID | Choice |
|----|--------|
| R-03 | Desktop Help **dropdown**: About, FAQ, Contact, Returns & Exchanges |
| R-04 | Coral cart badge **with count** (not pure dot) |
| R-01/**D-048** | Partner programs **not** in primary nav — applies to all four surfaces (hub + three dedicated pages). *Was cited as R-01/D-042; D-042 superseded 2026-08-08, the nav call itself is unchanged.* |
| R-12 | Chrome ships with/after core three |

## Approved structure
- Primary: Grippy Shoes | Apparel | Collaborations | Journal
- Subnav: Grippy (Shop All, Open, Closed, Outdoor, Compare); Apparel (All, Tops, Bottoms) — only live when collections exist
- Utility: Help (dropdown) · Account · Cart (coral badge + count)
- Mobile: hamburger + accordion; utility list already includes Help links
- Sticky: transparent → white + hairline

## Critical includes
- Help dropdown (desktop); coral count badge; flat primary IA

## Deferred Optionals
- Wordmark SVG; pure-dot badge variant
