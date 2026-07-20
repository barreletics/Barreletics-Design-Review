# Frozen Spec — Wholesale

---
status: FROZEN
surface: Wholesale intent → **Partners only** (D-042 / R-01 HOLD)
updated: 2026-07-20
---

## Applied decisions
| ID | Choice |
|----|--------|
| R-01 | **HOLD / Uphold D-042.** Canonical = `/pages/partners#wholesale` |
| R-02 | Deprecate orphan `page-wholesale` template — do not ship standalone |
| R-10 | Never public wholesale pricing/minimums |

## Spec
- Standalone Wholesale page is **deprecated**. All public Wholesale UX routes through Partners.
- Orphan Liquid/templates remain only as deprecated stubs (not assigned in live Shopify).
- 301s: legacy wholesale URLs → `/pages/partners` (or `#wholesale`).

## Critical includes
- Partners-only architecture; no public pricing

## Deferred Optionals
- Affiliate unrelated; studio testimonials on Partners
