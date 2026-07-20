# M4D — Deferred Validations from M4C

**Source:** M4C QA Report (`m4c-qa-report.md`)  
**Rule:** Every item below MUST be validated on the deployed Shopify preview with actual evidence before theme publish is authorized.

---

## Deferred Validation Items

| # | ID | Requirement | Evidence Method | Status |
|---|-----|-------------|-----------------|--------|
| 1 | PDP-014 | Sticky ATC IntersectionObserver fires correctly — hidden when buy box visible, appears when scrolled past | Browser DevTools → Elements → observe `.sticky-atc` class toggle while scrolling PDP. Screenshot of both states. | ⬜ Pending |
| 2 | CHK-003 | Discount codes apply correctly at checkout | Apply test discount code in live checkout → screenshot of line item discount applied → verify total recalculates | ⬜ Pending |
| 3 | A11Y-006 | Full keyboard navigation works across all pages | Manual Tab-through: homepage → nav → PDP → cart drawer → checkout. Screen recording of complete flow. Document any focus traps or unreachable elements. | ⬜ Pending |
| 4 | A11Y-011 | WCAG AA contrast ratios pass | Lighthouse accessibility audit → screenshot of results. Run on homepage, PDP, and collection page. All scores ≥90. | ⬜ Pending |
| 5 | A11Y-012 | Touch targets meet 44px minimum on mobile | Chrome DevTools → Device Mode (iPhone SE) → inspect button/link dimensions. Screenshot of DevTools showing computed sizes on PDP buy box buttons and nav links. | ⬜ Pending |
| 6 | MOB-001 | No horizontal overflow at 375px viewport | Chrome DevTools → Responsive → 375px width → scroll horizontally on homepage, collection, PDP. Screenshot showing no horizontal scrollbar. | ⬜ Pending |
| 7 | MOB-004 | Product cards stack correctly on mobile | Chrome DevTools → 375px → collection page showing 2-column grid. Screenshot of card layout. | ⬜ Pending |
| 8 | MOB-005 | PDP buy box stacks correctly on mobile | Chrome DevTools → 375px → PDP page. Screenshot showing gallery stacked above buy box, size selector visible, Add to Cart full-width. | ⬜ Pending |
| 9 | MOB-007 | Cart drawer functions on mobile | Open cart drawer on mobile viewport (375px). Screenshot showing drawer overlay, line items, checkout button. Test close via X and overlay tap. | ⬜ Pending |
| 10 | DSK-001 | Layout correct at 1280px | Browser window at 1280px → homepage, collection, PDP. Screenshot showing max-width container centered, no overflow. | ⬜ Pending |
| 11 | DSK-002 | Layout correct at 1440px+ | Browser window at 1440px → same pages. Screenshot showing content constrained within max-width, no stretching. | ⬜ Pending |
| 12 | PERF-001 | No render-blocking resources | Lighthouse Performance audit → screenshot of "Eliminate render-blocking resources" section. Document any flagged resources and remediation plan. | ⬜ Pending |
| 13 | PERF-005 | No significant CSS duplication | Chrome DevTools → Coverage tab → load homepage → screenshot showing CSS coverage percentage. Flag any files with >50% unused CSS. | ⬜ Pending |
| 14 | SEO-013 | Sitemap accessible at /sitemap.xml | Navigate to `barreletics.com/sitemap.xml` → screenshot showing valid XML sitemap. Verify product, collection, and page URLs present. | ⬜ Pending |
| 15 | SEO-014 | robots.txt accessible and correct | Navigate to `barreletics.com/robots.txt` → screenshot showing valid robots.txt. Verify sitemap reference and no unintended Disallow rules. | ⬜ Pending |

---

## Validation Protocol

1. **Environment:** Shopify preview theme (unpublished) or production after publish
2. **Evidence format:** Screenshots saved to a shared folder or pasted into the PR/issue thread
3. **Pass criteria:** Each item gets a screenshot or recording demonstrating the expected behavior
4. **Fail handling:** Any failure becomes a P1 or P2 issue (per `m4d-severity-matrix.md`) and must be fixed before publish (if on preview) or immediately after (if discovered post-publish)
5. **Sign-off:** Both Owner and Builder confirm all 15 items pass before publish authorization

---

## Responsibility

| Items | Owner |
|-------|-------|
| PDP-014, A11Y-006, A11Y-011, A11Y-012, MOB-001, MOB-004, MOB-005, MOB-007, DSK-001, DSK-002, PERF-001, PERF-005 | Builder executes, Owner reviews evidence |
| CHK-003 | Joint — Owner provides discount code, Builder tests |
| SEO-013, SEO-014 | Builder verifies on deployed store |
