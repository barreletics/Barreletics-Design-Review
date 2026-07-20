# 24 — Known Technical Debt

---
document: 24 – Known Technical Debt
status: Reference
last_modified: 2026-07-19
depends_on: [10-DECISIONS, 02-theme-architecture]
sources: planning/10-decision-log.md, planning/m4c-qa-report.md, planning/m4d-deferred-validations.md
---

## Overview

This document catalogs every known limitation, shortcut, deferred improvement, and intentional deviation in the Barreletics Shopify theme. Items are sourced from the Decision Log, QA reports, and codebase analysis.

---

## Inventory

### TD-001: 50/50 Split Section Uses min-height Instead of Fixed Height

**Source:** D-026
**What:** `sections/fifty-fifty.liquid` uses `min-height: 580px` with token-based padding (`var(--space-14) var(--space-12)`) rather than the static prototype spec of `height: 420px` + `padding: 80px 72px`.
**Why:** The section is reused 6× across three page types with varying content lengths. A fixed height clips content on mobile and in longer-copy instances.
**Impact:** Low. Visual result is proportionally consistent at desktop widths; mobile responsiveness is improved.
**Resolution:** None needed — intentional deviation. Document in component library if prototype specs are ever referenced.
**Priority:** Low

---

### TD-002: V2 Pattern Creates Duplicate Files

**Source:** D-030
**What:** Navigation and footer updates created as v2 files (`header-nav-v2.liquid`, `footer-v2.liquid`) rather than modifying the locked M2 originals. The v2 files were later consolidated back into the canonical filenames.
**Why:** M2 components were locked (D-027). Creating v2 files allowed M3 additions without risking M2 regressions.
**Impact:** Low. The pattern itself is documented for future reference — if further non-breaking updates are needed, the v2 approach may recur.
**Resolution:** Already resolved for M3 (v2 consolidated into canonical files). Future navigation changes should modify the canonical snippets directly unless a lockdown gate is active.
**Priority:** Low

---

### TD-003: Homepage Hero Not Locked — Two Concepts Pending

**Source:** D-041
**What:** `sections/hero.liquid` and `sections/hero-alt.liquid` both exist. Neither is finalized. The homepage hero remains the only unlocked section in the theme.
**Why:** Owner requested two concepts ("The Pilates Sock Era Is Over" vs. "Think Outside the Sock.") for side-by-side comparison before committing.
**Impact:** Medium. Final hero selection blocks launch. Both sections are functionally complete and independently deployable.
**Resolution:** Owner reviews both in Theme Customizer, selects one. Losing variant is archived. Hero status changes to Locked.
**Priority:** High (blocks launch)

---

### TD-004: Collections Should Only Be Created When Products Require Them

**Source:** D-043
**What:** Collection templates exist (`collection.open-sole.json`, `collection.closed-sole.json`, `collection.outdoor.json`, `collection.one-offs.json`, etc.) but the corresponding Shopify admin collections should not be batch-created until products populate them.
**Why:** Empty collections degrade storefront UX and create false navigation expectations.
**Impact:** Medium. Templates are ready. Launch requires matching merchandising readiness with template availability.
**Resolution:** Create collections in Shopify Admin only as products are added. Track which templates have matching admin collections in a deployment checklist.
**Priority:** Medium

---

### TD-005: M4D Deferred Validations (15 Items)

**Source:** `planning/m4d-deferred-validations.md`
**What:** 15 validation items from M4C require a deployed Shopify preview or device testing. They cannot be verified at the code level.

| ID | Requirement |
|----|-------------|
| PDP-014 | Sticky ATC IntersectionObserver fires correctly |
| CHK-003 | Discount codes apply at checkout |
| A11Y-006 | Full keyboard navigation across all pages |
| A11Y-011 | WCAG AA contrast ratios (Lighthouse audit) |
| A11Y-012 | 44px touch targets on device |
| MOB-001 | No horizontal overflow at 375px |
| MOB-004 | Product cards stack correctly on mobile |
| MOB-005 | PDP buy box stacks on mobile |
| MOB-007 | Cart drawer on mobile |
| DSK-001 | Layout correct at 1280px |
| DSK-002 | Layout correct at 1440px+ |
| PERF-001 | No render-blocking resources (Lighthouse) |
| PERF-005 | No significant CSS duplication (Coverage tab) |
| SEO-013 | Sitemap accessible at /sitemap.xml |
| SEO-014 | robots.txt accessible and correct |

**Why:** These require runtime evidence — browser rendering, network requests, or live Shopify infrastructure.
**Impact:** High. All must pass before publish authorization.
**Resolution:** Execute on deployed preview theme per methods documented in `m4d-deferred-validations.md`. Screenshot evidence required for each.
**Priority:** Critical (launch gate)

---

### TD-006: M4C Advisory Findings (Non-Blocking)

**Source:** `planning/m4c-qa-report.md` (Advisory Findings section)

#### A. Organization Schema Potentially Orphan

**What:** `snippets/organization-schema.liquid` (enhanced version with `sameAs`, description) exists but is never rendered. Basic Organization schema is inline in `theme.liquid:113–121`.
**Impact:** Low. The inline schema works. The enhanced snippet could provide richer structured data (social links, description).
**Resolution:** Render enhanced snippet on About page via `{% render 'organization-schema' %}`. Remove inline duplicate from theme.liquid.
**Priority:** Low

#### B. Fifty-Fifty bg_color Setting

**What:** `index.json` and `collection.json` pass `bg_color: "#f5f2ec"` as a merchant-editable setting. This hex value works (settings values are not hardcoded CSS) but could use a predefined token dropdown.
**Impact:** Low. Functionally correct. Merchant could set a non-brand color.
**Resolution:** Replace `bg_color` text input with a select dropdown in `fifty-fifty.liquid` schema offering token-mapped options (white, cream, charcoal).
**Priority:** Low

#### C. Mobile Menu Focus Trap

**What:** Mobile menu locks scroll and has close mechanisms but does not implement Tab-cycling focus trap like the cart drawer.
**Impact:** Low. The menu is not `aria-modal="true"` so a focus trap is not strictly required by WCAG. Users can still close via Escape or overlay.
**Resolution:** Add Tab-cycling within `.mobile-menu__drawer` matching the cart drawer pattern in `cart.js`.
**Priority:** Medium

---

### TD-007: Navigation Hardcoded in Snippets

**What:** All navigation links in `snippets/header-nav.liquid` and `snippets/footer.liquid` are hardcoded HTML rather than pulling from Shopify navigation menus (`linklists`).
**Why:** Intentional architectural decision. Hardcoded nav ensures exact control over structure, ordering, and sub-navigation grouping without depending on merchant menu configuration.
**Impact:** Medium. Merchants cannot self-service navigation changes via Shopify Admin → Navigation. Any nav change requires a code deploy.
**Resolution:** For merchant self-service, convert to `{% for link in linklists['main-menu'].links %}` pattern. Requires restructuring the dropdown/subnav logic to work with Shopify's linklist nesting model.
**Priority:** Medium (acceptable for current single-merchant operation; becomes higher priority if theme is used by non-technical operators)

---

### TD-008: Cart Drawer Re-renders Full HTML

**What:** `cart.js:renderDrawer()` (lines 101–138) rebuilds the entire `#cart-drawer-items` innerHTML on every cart change (add, quantity change, remove).
**Why:** Simplicity. Full re-render avoids complex DOM diffing logic for a small DOM tree (max ~10 line items).
**Impact:** Low. Cart items are a small DOM subtree. No perceptible performance issue with typical cart sizes (1–5 items).
**Resolution:** If cart performance becomes an issue (large carts, slow devices), implement targeted DOM updates or a lightweight diffing approach.
**Priority:** Low

---

### TD-009: Product Card JS Must Match Snippet Classes (D-034)

**Source:** D-034
**What:** When rendering product cards client-side via JavaScript (recommendations, recently-viewed sections), CSS class names must exactly match those in `snippets/product-card.liquid`: `product-card__content` (not `__info`), `product-card__name` (not `__title`).
**Why:** JS-rendered cards must inherit the same `<style>` block defined in the product-card snippet. Class mismatch = broken styling.
**Impact:** High if violated. Cards render without styling.
**Resolution:** Any new section rendering product cards client-side must reference `product-card.liquid` class names exactly. Consider extracting a shared JS template constant.
**Priority:** Medium (documented; requires discipline on future card-rendering sections)

---

### TD-010: No Automated Testing

**What:** Zero unit tests, integration tests, or visual regression tests exist for the theme.
**Why:** Shopify Liquid themes have limited testing infrastructure. The theme was built with manual QA (M4C: 130 validations) and code review.
**Impact:** High for long-term maintenance. Regressions can only be caught by manual review or post-deploy monitoring.
**Resolution:** Options by priority:
1. Visual regression testing with Percy/Chromatic on preview theme URLs
2. Lighthouse CI for performance/accessibility regression
3. Custom test harness for JS modules (variant-selector.js, cart.js) using Jest with DOM mocking
4. Liquid linting via Theme Check (`shopify theme check`)
**Priority:** Medium (acceptable for v1 launch; becomes high as the theme grows)

---

### TD-011: Single Font With All 6 Weights

**What:** Google Fonts loads Roboto with weights 300, 400, 500, 600, 700, 800 in a single request:
```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```
**Why:** All weights are used across the design system (300=light hero text, 400=body, 500=subnav, 600=headings, 700=CTAs, 800=hero).
**Impact:** Low. Google Fonts serves variable font files where available, reducing the penalty. Total font payload is still reasonable.
**Resolution:** If performance budget tightens:
1. Audit actual weight usage — 800 may be droppable
2. Self-host subset of Roboto (Latin only) for fewer round-trips
3. Use `font-display: optional` for non-critical weights
**Priority:** Low

---

### TD-012: Announcement Strip Block Architecture

**What:** The announcement strip uses theme settings (`settings.announcement_message_1/2/3`) rather than section blocks. This limits extensibility and requires settings_schema changes for more messages.
**Why:** Simpler implementation for a fixed 3-message rotation.
**Impact:** Low. Current 3-message limit is sufficient. Adding a 4th message requires a schema change.
**Resolution:** Convert to a section with `blocks` of type `message` for unlimited messages via the Theme Customizer.
**Priority:** Low

---

### TD-013: No TODO/FIXME Comments in Codebase

A grep of all `.liquid`, `.js`, and `.css` files in `shopify-build/` for `TODO`, `FIXME`, `HACK`, `XXX`, and `WORKAROUND` returned zero results. All technical debt is tracked in planning documents rather than inline comments.

---

## Priority Summary

| Priority | Items |
|----------|-------|
| **Critical** | TD-005 (15 deferred validations — launch gate) |
| **High** | TD-003 (hero not locked), TD-010 (no automated testing) |
| **Medium** | TD-004 (collections), TD-006C (mobile focus trap), TD-007 (hardcoded nav), TD-009 (card class matching) |
| **Low** | TD-001 (50/50 height), TD-002 (v2 pattern), TD-006A (orphan schema), TD-006B (bg_color), TD-008 (cart re-render), TD-011 (font weights), TD-012 (announcement blocks) |

---

**Cross-references:**
- Decision Log → `planning/10-decision-log.md`
- QA Report → `planning/m4c-qa-report.md`
- Deferred Validations → `planning/m4d-deferred-validations.md`
- Theme architecture → `docs/02-theme-architecture.md`
