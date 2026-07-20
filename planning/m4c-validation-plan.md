# M4C Validation Plan

---
document: M4C Validation Plan
status: ⚪ Planning
created: 2026-07-19
depends_on: [M4A locked, M4B locked, D-040 Policy Freeze Gate]
---

## Purpose

Complete execution checklist for M4C Validation gate. Defines every QA, accessibility, performance, and compliance check required before the theme can proceed to M4D Launch.

---

## Entry Criteria

All must be satisfied before M4C work begins:

- [x] M4A Production Assembly: 🔒 Locked
- [x] M4B Integrations: 🔒 Locked
- [ ] Theme uploadable to Shopify preview
- [ ] Content inventory reviewed (Owner approval on pending items)
- [ ] Policy Freeze Gate satisfied (D-040): Owner sign-off on shipping terms, return terms, warranty language, pricing, discounts/promo codes, free-shipping threshold ($150), size guidance, product claims, wholesale terms, Studio Program terms, Ambassador terms

---

## Scope

### 1. Functional QA

- [ ] Homepage loads correctly with all sections
- [ ] Collection pages load, filter, and sort correctly
- [ ] PDP loads with correct product data
- [ ] Variant selection works (color, size → correct variant ID, price, image, URL)
- [ ] Add to Cart → Cart Drawer → Checkout flow works end-to-end
- [ ] Sticky ATC appears/disappears correctly and adds correct variant
- [ ] Cart drawer: quantity +/-, remove, subtotal update, shipping bar
- [ ] All supporting pages load (FAQ, About, Contact, Compare, Partners, Size Guide, Warranty, Shipping, Returns, Technology, Grip Comparison)
- [ ] Search works
- [ ] Navigation (desktop + mobile) works with all dropdowns
- [ ] Footer links all resolve
- [ ] Newsletter signup works
- [ ] Contact form submits
- [ ] Partner inquiry form submits
- [ ] Breadcrumbs display correctly on all pages
- [ ] Announcement strip displays and rotates

### 2. Accessibility Audit (WCAG 2.1 AA)

- [ ] Keyboard navigation: all interactive elements reachable and operable
- [ ] Focus indicators visible on all interactive elements
- [ ] Screen reader: headings in logical order, no skipped levels
- [ ] Screen reader: all images have alt text or aria-hidden
- [ ] Screen reader: form inputs have labels
- [ ] Screen reader: dynamic content announced (cart updates, accordion, drawer)
- [ ] Color contrast: all text meets 4.5:1 (normal) / 3:1 (large)
- [ ] Touch targets: minimum 44x44px on mobile
- [ ] Skip navigation link works
- [ ] Focus trap on cart drawer and mobile menu
- [ ] Reduced motion: animations respect prefers-reduced-motion

### 3. Responsive / Device Testing

- [ ] Mobile portrait (375px)
- [ ] Mobile landscape (667px)
- [ ] Tablet portrait (768px)
- [ ] Tablet landscape (1024px)
- [ ] Desktop (1280px)
- [ ] Large desktop (1440px+)
- [ ] No horizontal overflow on any viewport
- [ ] Typography scales correctly
- [ ] Images responsive (no layout shifts)
- [ ] Navigation works on all viewports

### 4. Cross-Browser Testing

- [ ] Chrome (latest 2 versions)
- [ ] Safari (latest 2 versions)
- [ ] Firefox (latest 2 versions)
- [ ] Edge (latest 2 versions)
- [ ] iOS Safari
- [ ] Android Chrome

### 5. Structured Data Validation

- [ ] Product schema (PDP) — Google Rich Results Test
- [ ] FAQPage schema (FAQ page, PDP FAQ, Collection FAQ) — Google Rich Results Test
- [ ] BreadcrumbList schema (all pages except homepage)
- [ ] Organization schema (About page)
- [ ] BlogPosting schema (Journal articles)
- [ ] CollectionPage schema (collection pages)
- [ ] No hardcoded review data in schema
- [ ] All JSON-LD valid (no parsing errors)

### 6. Performance (Lab Testing)

- [ ] Lighthouse Performance ≥ 90
- [ ] Lighthouse Accessibility ≥ 95
- [ ] Lighthouse Best Practices ≥ 95
- [ ] Lighthouse SEO ≥ 95
- [ ] LCP ≤ 2.5s (lab)
- [ ] CLS ≤ 0.1 (lab)
- [ ] No render-blocking resources in critical path
- [ ] Images lazy-loaded below fold
- [ ] JavaScript deferred
- [ ] CSS optimized (no unnecessary duplication)
- [ ] Note: INP and field CWV data require real traffic post-launch

### 7. Analytics Event Validation

- [ ] Per D-045: verify only ONE tracking source active (native OR theme)
- [ ] page_view fires on every page
- [ ] view_item fires on PDP with correct product data
- [ ] view_item_list fires on collection with correct list data
- [ ] add_to_cart fires with correct variant data
- [ ] begin_checkout fires
- [ ] purchase fires (via Shopify checkout — document verification method)
- [ ] No duplicate events
- [ ] Meta Pixel events fire correctly (if theme-managed)
- [ ] Pinterest events fire correctly
- [ ] Clarity loads and records sessions

---

## Exit Criteria

All must be satisfied before M4C is locked:

- All functional QA items pass
- All critical accessibility items pass (no WCAG AA violations)
- All viewports render correctly
- All supported browsers work
- All structured data validates
- Lighthouse scores meet targets
- Analytics events verified (or documented as credential-dependent)
- QA report produced with pass/fail evidence
- Owner sign-off on any remaining content items

---

## Responsibility

| Domain | Responsible |
|--------|-------------|
| Functional QA | Builder |
| Accessibility audit | Builder |
| Device/browser testing | Builder (lab) + Owner (real devices) |
| Structured data | Builder |
| Performance | Builder |
| Analytics validation | Joint (Builder implements, Owner provides accounts) |
| Content approval | Owner |
| Policy freeze gate | Owner (must sign off on all business terms before M4C exit) |

---

## Deliverable

- `planning/m4c-qa-report.md` with pass/fail for every item
- Updated `PROJECT_DASHBOARD.md`
- PR with any fixes discovered during validation
