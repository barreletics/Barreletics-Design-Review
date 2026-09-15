# Frozen Spec — Studio Program

---
status: FROZEN — partner surface UPDATED 2026-08-08 (D-048)
surface: Studio Partner intent → **dedicated `/pages/studio-program`** with its own intake form; `/pages/partners` is the routing hub
prior_surface: ~~Studio Partner intent → **Partners only** (D-042 / R-01 HOLD)~~ — RETIRED 2026-08-08
updated: 2026-08-08 (was 2026-07-20)
---

> **UPDATED 2026-08-08 — D-048 supersedes D-042.** Owner direction 2026-08-08 reversed the fold.
> Studio Program has a **dedicated page** again: `templates/page.studio-program.json` +
> `sections/page-studio-program.liquid`, built, type-corrected and mobile-QA'd
> (`planning/partner-programs.md` §5, `planning/partner-pages-qa/`).
> `/pages/partners` is retained as a **routing hub** — three program cards plus a general-inquiry fallback form.
> The `/pages/studio-program` → `/pages/partners` 301 is **retired** in `planning/m4a-redirect-map.md`; it would
> make the page unreachable. R-01/R-02 history below is preserved as history — **do not implement**.

## Applied decisions
| ID | Choice |
|----|--------|
| **D-048** | **CURRENT (2026-08-08).** Dedicated `/pages/studio-program` + own intake form (`BL-PARTNER-STUDIO`). `/pages/partners` = routing hub. Supersedes R-01 / R-02 below. |
| ~~R-01~~ | ~~Uphold D-042 — `/pages/partners#studio-partners`~~ — **SUPERSEDED 2026-08-08 by D-048.** History only. |
| ~~R-02~~ | ~~Deprecate orphan `page-studio-program`~~ — **SUPERSEDED 2026-08-08 by D-048.** The template is live and assigned. |
| R-10 | Never public partner pricing — **still in force** |

## Spec
- **Current (D-048):** `/pages/studio-program` is a dedicated public page with its own qualification form — locations, instructors on staff, primary discipline, weekly client visits, what they want to carry. Studios qualify on class volume and location.
- **Current (D-048):** `/pages/partners` routes to Wholesale / Studio / Ambassador and carries a general-inquiry fallback only.
- **Current (D-048):** no `/pages/studio-program` → `/pages/partners` 301. Retired in `planning/m4a-redirect-map.md`.
- R-10 unchanged: partner pricing never public.
- `Section-26-NotesFromStudio` is editorial/UGC for Home/PDP — **not** this program page. Unchanged.
- ~~Standalone Studio Program page **deprecated**. Canonical Partners `#studio-partners`.~~ — RETIRED 2026-08-08 (D-048)

## Critical includes
- Dedicated page + hub routing (D-048); no public partner pricing
