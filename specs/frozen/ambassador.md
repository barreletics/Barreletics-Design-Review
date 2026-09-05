# Frozen Spec — Ambassador

---
status: FROZEN — partner surface UPDATED 2026-08-08 (D-048)
surface: Ambassador intent → **dedicated `/pages/ambassador`** with its own intake form; `/pages/partners` is the routing hub
prior_surface: ~~Ambassador intent → **Partners only** (D-042 / R-01 HOLD)~~ — RETIRED 2026-08-08
updated: 2026-08-08 (was 2026-07-20)
---

> **UPDATED 2026-08-08 — D-048 supersedes D-042.** Owner direction 2026-08-08 reversed the fold.
> Ambassador has a **dedicated page** again: `templates/page.ambassador.json` + `sections/page-ambassador.liquid`,
> built, type-corrected and mobile-QA'd (`planning/partner-programs.md` §5, `planning/partner-pages-qa/`).
> `/pages/partners` is retained as a **routing hub** — three program cards plus a general-inquiry fallback form.
> The `/pages/ambassador` → `/pages/partners` 301 is **retired** in `planning/m4a-redirect-map.md`; it would make
> the page unreachable. R-01/R-02 history below is preserved as history — **do not implement**.

## Applied decisions
| ID | Choice |
|----|--------|
| **D-048** | **CURRENT (2026-08-08).** Dedicated `/pages/ambassador` + own intake form (`BL-PARTNER-AMBASSADOR`). `/pages/partners` = routing hub. Supersedes R-01 / R-02 below. |
| ~~R-01~~ | ~~Uphold D-042 — `/pages/partners#ambassadors`~~ — **SUPERSEDED 2026-08-08 by D-048.** History only. |
| ~~R-02~~ | ~~Deprecate orphan `page-ambassador`~~ — **SUPERSEDED 2026-08-08 by D-048.** The template is live and assigned. |
| R-10 | Never public commission rates — **still in force** |
| R-11 | Defer affiliate embed (placeholder OK) — **still in force** |

## Spec
- **Current (D-048):** `/pages/ambassador` is a dedicated public page with its own qualification form — discipline, certification, classes/clients per week, Instagram/TikTok, audience size. Creators qualify on audience and content channels.
- **Current (D-048):** `/pages/partners` routes to Wholesale / Studio / Ambassador and carries a general-inquiry fallback only.
- **Current (D-048):** no `/pages/ambassador` → `/pages/partners` 301. Retired in `planning/m4a-redirect-map.md`.
- R-10 / R-11 unchanged: commission rates stay off the public page (Theme Editor settings / internal), affiliate platform embed still deferred.
- ~~Standalone Ambassador page **deprecated**. Canonical Partners `#ambassadors` + inquiry form.~~ — RETIRED 2026-08-08 (D-048)
- ~~Do not ship orphan ambassador marketing template.~~ — RETIRED 2026-08-08 (D-048). Note `/pages/become-an-affiliate` → `/pages/partners` **remains correct** and is unaffected.

## Critical includes
- Dedicated page + hub routing (D-048); no public rates; affiliate deferred
