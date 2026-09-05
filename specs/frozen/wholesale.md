# Frozen Spec — Wholesale

---
status: FROZEN — partner surface UPDATED 2026-08-08 (D-048)
surface: Wholesale intent → **dedicated `/pages/wholesale`** with its own intake form; `/pages/partners` is the routing hub
prior_surface: ~~Wholesale intent → **Partners only** (D-042 / R-01 HOLD)~~ — RETIRED 2026-08-08
updated: 2026-08-08 (was 2026-07-20)
---

> **UPDATED 2026-08-08 — D-048 supersedes D-042.** Owner direction 2026-08-08 reversed the fold.
> Wholesale has a **dedicated page** again: `templates/page.wholesale.json` + `sections/page-wholesale.liquid`,
> built, type-corrected and mobile-QA'd (`planning/partner-programs.md` §5, `planning/partner-pages-qa/`).
> `/pages/partners` is retained as a **routing hub** — three program cards plus a general-inquiry fallback form.
> The `/pages/wholesale` → `/pages/partners` 301 is **retired** in `planning/m4a-redirect-map.md`; it would make
> the page unreachable. R-01/R-02 history below is preserved as history — **do not implement**.

## Applied decisions
| ID | Choice |
|----|--------|
| **D-048** | **CURRENT (2026-08-08).** Dedicated `/pages/wholesale` + own intake form (`BL-PARTNER-WHOLESALE`). `/pages/partners` = routing hub. Supersedes R-01 / R-02 below. |
| ~~R-01~~ | ~~**HOLD / Uphold D-042.** Canonical = `/pages/partners#wholesale`~~ — **SUPERSEDED 2026-08-08 by D-048.** History only. |
| ~~R-02~~ | ~~Deprecate orphan `page-wholesale` template — do not ship standalone~~ — **SUPERSEDED 2026-08-08 by D-048.** The template is live and assigned. |
| R-10 | Never public wholesale pricing/minimums — **still in force** |

## Spec
- **Current (D-048):** `/pages/wholesale` is a dedicated public page with its own qualification form — business/entity details, resale certificate, sales channels, first order size, expected annual volume. B2B buyers qualify on questions no shared form can carry.
- **Current (D-048):** `/pages/partners` routes to Wholesale / Studio / Ambassador and carries a general-inquiry fallback only.
- **Current (D-048):** no `/pages/wholesale` → `/pages/partners` 301. Retired in `planning/m4a-redirect-map.md`.
- R-10 unchanged: per-pair pricing, margin, MOQ dollar figures and payment terms are **internal** — reply-only, never on the page.
- ~~Standalone Wholesale page is **deprecated**. All public Wholesale UX routes through Partners.~~ — RETIRED 2026-08-08 (D-048)
- ~~Orphan Liquid/templates remain only as deprecated stubs (not assigned in live Shopify).~~ — RETIRED 2026-08-08 (D-048)
- ~~301s: legacy wholesale URLs → `/pages/partners` (or `#wholesale`).~~ — RETIRED 2026-08-08 (D-048). Note `/pages/wholesale-calculator` → `/pages/partners` **remains correct** and is unaffected.

## Critical includes
- Dedicated page + hub routing (D-048); no public pricing (R-10)

## Deferred Optionals
- Affiliate unrelated; studio testimonials live on `/pages/studio-program`
