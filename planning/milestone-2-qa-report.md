# Milestone 2 — QA Report

**Date:** 2026-07-18
**Branch:** `milestone-2-core-experience`
**PR:** #2 against `main`
**Auditor:** QA Lead (Phase 3)

---

## Summary

| Category | Result | Critical | Minor | Observations |
|----------|--------|----------|-------|--------------|
| Foundation Compliance | ❌ Fail | 7 | 3 | 1 |
| Prototype Fidelity | ⚠️ Partial | 0 | 2 | 2 |
| Accessibility (WCAG 2.1 AA) | ❌ Fail | 4 | 4 | 0 |
| Responsive Validation | ✅ Pass | 0 | 0 | 1 |
| Performance Review | ✅ Pass | 0 | 0 | 2 |
| Component Consistency | ❌ Fail | 2 | 0 | 1 |
| Cross-Browser | ✅ Pass | 0 | 1 | 0 |
| **Totals** | | **13** | **10** | **7** |

**Overall Quality Score:** 73/100 — Solid foundation with critical token/markup issues that must be fixed before merge.

---

## Critical Issues

### C-01: Button border-radius token is 4px, should be 6px
- **File:** `shopify-build/assets/design-tokens.css` line 114
- **What's wrong:** `--radius-button: 4px`
- **Should be:** `--radius-button: 6px` — per D-003 ("CTA buttons use 6px border-radius") and Doc 03 border radius table
- **Impact:** All buttons across the entire theme render with wrong radius
- **Severity:** Critical

### C-02: Eyebrow letter-spacing token is 0.1em, should be 0.08em
- **File:** `shopify-build/assets/design-tokens.css` line 75
- **What's wrong:** `--tracking-eyebrow: 0.1em`
- **Should be:** `--tracking-eyebrow: 0.08em` — per D-004 ("System default is 0.08em") and Doc 03
- **Impact:** All sections using `var(--tracking-eyebrow)` render with incorrect spacing (fifty-fifty, variant-grid, collection-hero, pdp-features)
- **Severity:** Critical

### C-03: Hero eyebrow uses hardcoded 0.12em letter-spacing
- **File:** `shopify-build/sections/hero.liquid` line 75
- **What's wrong:** `.hero__eyebrow { letter-spacing: 0.12em; }` — hardcoded value, not using token
- **Should be:** `letter-spacing: var(--tracking-widest);` (0.08em) per D-004
- **Severity:** Critical

### C-04: Disciplines headline uses hardcoded 0.12em letter-spacing
- **File:** `shopify-build/sections/disciplines.liquid` line 37
- **What's wrong:** `.disciplines-proof__headline { letter-spacing: 0.12em; }` — hardcoded
- **Should be:** `letter-spacing: var(--tracking-widest);` (0.08em) per D-004
- **Severity:** Critical

### C-05: PDP trust row missing "Made in USA"
- **File:** `shopify-build/sections/pdp-buy-box.liquid` lines 116–120
- **What's wrong:** Trust row has 4 items: Ships 1–2 days, 30-day returns, 90-day warranty, Latex- & silicone-free
- **Should be:** 5 items including "Made in USA" — per Doc 05 Section 1 trust row spec
- **Severity:** Critical

### C-06: Sock Math uses retired claim "grip never degrades"
- **File:** `shopify-build/sections/pdp-sock-math.liquid` line 40
- **What's wrong:** Text reads "18+ month lifespan, grip never degrades"
- **Should be:** "Injection-molded grip won't peel or flake like silicone dots" — per D-018 (claim retired)
- **Severity:** Critical

### C-07: Collection 50/50 uses retired "never degrades" claim
- **File:** `shopify-build/templates/collection.json` line 37 (fifty-fifty-grip body)
- **What's wrong:** "The patented grip surface never degrades"
- **Should be:** "The patented grip surface won't peel or flake — not after 100 classes, not after 1,000" — per D-018
- **Severity:** Critical

### C-08: No focus-visible indicators in base CSS
- **File:** `shopify-build/assets/barreletics-base.css`
- **What's wrong:** No `:focus-visible` styles defined. Interactive elements (buttons, links, inputs) have no visible focus ring.
- **Should be:** Global `:focus-visible` rule providing visible outline per WCAG 2.1 AA 2.4.7. Build spec Section 10 requires "Visible `:focus-visible` ring on all interactive elements."
- **Severity:** Critical (Accessibility)

### C-09: PDP accordion open/close icon CSS broken
- **File:** `shopify-build/sections/pdp-buy-box.liquid` line 443
- **What's wrong:** `.pdp-accordion[open] .pdp-accordion__trigger span { content: "−"; }` — the `content` property only works on `::before`/`::after` pseudo-elements, not on regular `<span>` elements. The `+` icon never changes to `−` when open.
- **Should be:** Use the same pattern as faq-accordion.liquid: `::after` pseudo-element with content swap
- **Severity:** Critical (Broken UI)

### C-10: Nested `<header>` elements — duplicate landmark
- **File:** `shopify-build/layout/theme.liquid` line 100 + `shopify-build/snippets/header-nav.liquid` line 17
- **What's wrong:** theme.liquid wraps `{% render 'header-nav' %}` inside `<header class="site-header" role="banner">`. header-nav.liquid itself also contains `<header class="site-header" data-site-header role="banner">`. Result: nested `<header>` elements with duplicate `role="banner"`.
- **Should be:** Single `<header>` element. Remove the outer wrapper from theme.liquid.
- **Severity:** Critical (Invalid HTML, accessibility landmark confusion)

### C-11: Nested `<footer>` elements — duplicate landmark
- **File:** `shopify-build/layout/theme.liquid` line 110 + `shopify-build/snippets/footer.liquid` line 12
- **What's wrong:** Same pattern as C-10. theme.liquid wraps footer snippet in `<footer class="site-footer" role="contentinfo">`, and footer.liquid also has `<footer class="site-footer" ... role="contentinfo">`.
- **Should be:** Single `<footer>` element. Remove the outer wrapper from theme.liquid.
- **Severity:** Critical (Invalid HTML, accessibility landmark confusion)

### C-12: Duplicate skip-to-content links
- **File:** `shopify-build/layout/theme.liquid` line 93 + `shopify-build/snippets/header-nav.liquid` line 12
- **What's wrong:** Two `<a href="#main-content" class="skip-link">Skip to content</a>` elements. One in theme.liquid (before announcement strip) and one inside header-nav.liquid (inside the nested header).
- **Should be:** Single skip link, first focusable element in DOM (the one in theme.liquid). Remove the duplicate from header-nav.liquid.
- **Severity:** Critical (Accessibility — confusing for keyboard/screen reader users)

### C-13: Cart trigger not wired to drawer
- **File:** `shopify-build/snippets/header-nav.liquid` line 82 + `shopify-build/snippets/cart-drawer.liquid`
- **What's wrong:** The cart icon link has `data-cart-trigger` attribute but no click handler connects it to `CartDrawer.open()`. Clicking the cart icon navigates to `/cart` page instead of opening the drawer (D-024 specifies drawer as primary).
- **Should be:** JavaScript event listener on `[data-cart-trigger]` that calls `e.preventDefault()` and `CartDrawer.open()`
- **Severity:** Critical (Core UX — D-024)

---

## Minor Issues

### M-01: Product card hover scale 1.04, should be 1.02
- **File:** `shopify-build/snippets/product-card.liquid` line 101
- **What's wrong:** `.product-card:hover .product-card__img { transform: scale(1.04); }`
- **Should be:** `scale(1.02)` per Doc 04 Component 6 ("image 1.02× scale, 320ms")
- **Severity:** Minor

### M-02: Product card hover transition 0.4s, should be 320ms
- **File:** `shopify-build/snippets/product-card.liquid` line 100
- **What's wrong:** `transition: transform 0.4s ease;`
- **Should be:** `transition: transform 320ms ease;` or `transition: transform var(--transition-ticker);` per Doc 04
- **Severity:** Minor

### M-03: Announcement strip link hover uses coral
- **File:** `shopify-build/snippets/announcement-strip.liquid` line 79
- **What's wrong:** `.announcement-strip__link:hover { color: var(--color-coral); }` — coral (#e8927c) is restricted to cart badge only per Doc 03 rule 5
- **Should be:** `color: rgba(255, 255, 255, 0.7);` or similar light hover state
- **Severity:** Minor

### M-04: Variant grid inactive tabs missing aria-selected
- **File:** `shopify-build/sections/variant-grid.liquid` lines 23–27
- **What's wrong:** Non-active tab buttons have `role="tab"` but no `aria-selected="false"`
- **Should be:** All `role="tab"` buttons must have `aria-selected="true"` or `aria-selected="false"` per WAI-ARIA
- **Severity:** Minor (Accessibility)

### M-05: PDP title tag missing sole type
- **File:** `shopify-build/layout/theme.liquid` line 12
- **What's wrong:** `{{ product.title }} | Barreletics`
- **Should be:** `{{ product.title }} — {{ product.metafields.custom.sole_type | default: 'Performance Skin' }} | Barreletics` per Doc 12
- **Severity:** Minor (SEO)

### M-06: Trust strip stars lack accessible label
- **File:** `shopify-build/snippets/trust-strip.liquid` line 28
- **What's wrong:** `★★★★★ 1,000+ Reviews` — screen readers read each star as "black star" character
- **Should be:** Wrap stars in `<span aria-hidden="true">★★★★★</span>` and add `<span class="visually-hidden">5 out of 5 stars,</span>` per Doc 04 Component 20
- **Severity:** Minor (Accessibility)

### M-07: PDP accordion missing aria-expanded updates
- **File:** `shopify-build/sections/pdp-buy-box.liquid` lines 123–142
- **What's wrong:** PDP accordion `<summary>` elements don't have or manage `aria-expanded`. FAQ accordion manages this correctly via JS.
- **Should be:** Add `aria-expanded="false"` to summaries and JS toggle on open/close, matching faq-accordion.liquid pattern
- **Severity:** Minor (Accessibility)

### M-08: 50/50 split dimensions differ from Doc 04
- **File:** `shopify-build/sections/fifty-fifty.liquid` lines 51, 130
- **What's wrong:** `min-height: 580px`, copy padding `80px 64px`
- **Should be:** `height: 420px` fixed with `overflow: hidden`, copy padding `80px 72px` per Doc 04 Component 5
- **Severity:** Minor (Design deviation — may be intentional for Liquid flexibility)

### M-09: Collection title tag format differs from Doc 12
- **File:** `shopify-build/layout/theme.liquid` line 15
- **What's wrong:** `{{ collection.title }} | Barreletics Grippy Shoes`
- **Should be:** `Grippy Shoes for Barre, Pilates & Reformer | Barreletics` per Doc 12 (or dynamic equivalent)
- **Severity:** Minor (SEO)

### M-10: Social proof section hardcodes review card styles
- **File:** `shopify-build/sections/social-proof.liquid` lines 98–132
- **What's wrong:** Review card styles are redefined inline in social-proof.liquid instead of reusing the review-card.liquid snippet (D-025)
- **Should be:** Use `{% render 'review-card' %}` for consistency per D-025 decision
- **Severity:** Minor (Component consistency)

---

## Observations

### O-01: PDP buy box uses inline font-weight styles
- **File:** `shopify-build/sections/pdp-buy-box.liquid` lines 54–55
- **Note:** `.pdp-buy__name` children use `style="font-weight: 300"` and `style="font-weight: 700"` instead of design token weight variables. Functional but inconsistent with token-first approach.

### O-02: Variant grid tabs have no JavaScript wiring
- **File:** `shopify-build/sections/variant-grid.liquid`
- **Note:** Tab buttons and size buttons have correct ARIA markup but no JS event handling. This is likely intentional — filtering will be backed by Shopify collection API at deployment. Not a bug, but requires JS implementation before go-live.

### O-03: No CSS custom property fallbacks for critical values
- **File:** `shopify-build/assets/barreletics-base.css`, all sections
- **Note:** CSS custom properties are used without fallback values (e.g., `color: var(--text-primary)` not `color: var(--text-primary, #1c1916)`). Browsers that support CSS custom properties handle this fine, but fallbacks provide defense-in-depth.

### O-04: Duplicate skip link styling
- **File:** `shopify-build/assets/barreletics-base.css` lines 123–137 + `shopify-build/layout/theme.liquid` lines 119–136
- **Note:** Skip link styles are defined both in base CSS and inline in theme.liquid. After fixing C-12 (removing duplicate skip link from header-nav), consolidate styling to base CSS only.

### O-05: theme.liquid has duplicate prefers-reduced-motion rule
- **File:** `shopify-build/layout/theme.liquid` lines 140–149 + `shopify-build/assets/barreletics-base.css` lines 173–180
- **Note:** The `prefers-reduced-motion` media query is defined in both files. The base CSS version is sufficient; the inline version in theme.liquid is redundant.

### O-06: Build spec v2 border-radius table has stale value
- **File:** `planning/shopify-build-spec-v2.md` line 129
- **Note:** Build spec lists "Button / CTA | 4px" which contradicts D-003 (6px). The build spec should be updated but is not a Foundation document, so not blocking. Noting for awareness.

### O-07: Product card badge styling differs from Design System spec
- **File:** `shopify-build/snippets/product-card.liquid` lines 116–126
- **Note:** Product card badge uses `font-size: 9px`, `background: rgba(28, 25, 22, 0.7)`, `border-radius: 2px`. Design System badge spec is `10px / #c45c3f bg / 3px radius`. This may be intentional for product-card-specific badge styling vs the category badge in PDP.

---

## QA Checklist Results

### 1. Foundation Compliance — ❌ FAIL
- Color values: ✅ All hex values match Doc 03
- Typography: ❌ Eyebrow letter-spacing token wrong (C-02, C-03, C-04)
- Spacing: ✅ Section padding, max-width correct
- Border radius: ❌ Button radius wrong (C-01)
- Star color: ✅ `#d4af37` correct per D-007
- Navigation: ✅ Matches Doc 11 exactly
- SEO: ⚠️ Structured data present, title tag format deviates slightly (M-05, M-09)
- Copy: ❌ Retired claims used (C-06, C-07)

### 2. Prototype Fidelity — ⚠️ PARTIAL
- All three page types (Home, PDP, Collection) are implemented
- Section order matches approved prototypes
- 50/50 split dimensions deviate (M-08)
- Social proof section doesn't reuse review-card snippet (M-10)
- All sections from prototypes are accounted for
- No unauthorized sections added

### 3. Accessibility — ❌ FAIL
- Skip link: ❌ Duplicate (C-12)
- Focus indicators: ❌ Missing (C-08)
- ARIA: ❌ Nested landmarks (C-10, C-11), missing aria-selected (M-04), missing aria-expanded on PDP accordion (M-07)
- Labels: ✅ Form inputs have labels, cart drawer has aria-labels
- Reduced motion: ✅ Properly handled
- Keyboard: ⚠️ Cart drawer has focus trap ✓, mobile menu has Escape handler ✓, but cart trigger broken (C-13)
- Heading order: ✅ Logical hierarchy maintained
- Touch targets: ✅ All interactive elements ≥ 44px

### 4. Responsive — ✅ PASS
- All breakpoints (1024px, 768px) properly defined
- Mobile-first approach in base CSS
- Touch targets meet 44px minimum
- Grids collapse correctly (4→2→1 col)
- Typography scales (H1 44→32px)
- No horizontal overflow patterns detected

### 5. Performance — ✅ PASS
- Hero image: `loading="eager"`, `fetchpriority="high"` ✓
- Below-fold images: `loading="lazy"` ✓
- Font preconnects in `<head>` ✓
- CSS organized efficiently, uses tokens
- JS is minimal, inline per-component
- `srcset` and `sizes` on responsive images ✓

### 6. Component Consistency — ❌ FAIL
- Review card snippet exists but social-proof section duplicates styles (M-10)
- Nested landmark elements break component encapsulation (C-10, C-11)
- Template JSON files reference correct sections ✓
- All three templates (index, product, collection) properly assembled ✓

### 7. Cross-Browser — ✅ PASS
- CSS custom properties used consistently (IE11 not a target)
- Flexbox/Grid usage is compatible with modern browsers
- No bleeding-edge CSS without broader support
- `IntersectionObserver` used for sticky ATC (supported in all modern browsers)
- Minor: No CSS fallbacks (O-03 — not blocking)

---

## Fix Plan

### Phase 1: Critical fixes (must fix before merge)
1. Fix `--radius-button` token → 6px (C-01)
2. Fix `--tracking-eyebrow` token → 0.08em (C-02)
3. Fix hero eyebrow hardcoded letter-spacing (C-03)
4. Fix disciplines headline hardcoded letter-spacing (C-04)
5. Add "Made in USA" to PDP trust row (C-05)
6. Replace retired "never degrades" claims (C-06, C-07)
7. Add `:focus-visible` styles to base CSS (C-08)
8. Fix PDP accordion icon CSS (C-09)
9. Fix nested `<header>` and `<footer>` elements (C-10, C-11)
10. Remove duplicate skip link (C-12)
11. Wire cart trigger to CartDrawer.open() (C-13)

### Phase 2: Minor fixes (straightforward, fix now)
1. Product card hover scale/timing (M-01, M-02)
2. Announcement strip hover color (M-03)
3. Variant grid aria-selected (M-04)
4. Trust strip star accessibility (M-06)
5. PDP accordion aria-expanded (M-07)

### Deferred
- M-05, M-09: Title tag formats (requires metafield/dynamic content — fix during deployment)
- M-08: 50/50 split dimensions (may be intentional deviation for Liquid flexibility)
- M-10: Social proof refactor to use review-card snippet (non-trivial, defer to Milestone 3)
