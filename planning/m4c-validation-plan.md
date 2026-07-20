# M4C — Validation Gate Plan

**Milestone:** 4C — Validation  
**Created:** 2026-07-19  
**Status:** In Progress  
**Entry Criterion:** M4B Integrations locked (D-046)

---

## Validation Structure

Every item uses:

| Field | Description |
|-------|-------------|
| **Validation ID** | e.g., NAV-001 |
| **Requirement** | What must be true |
| **Validation Method** | How to verify (code review, browser test, tool output) |
| **Expected Result** | The specific expected outcome |
| **Evidence Required** | What proves it (screenshot, console output, code reference, network request, schema test result, Lighthouse score) |
| **Status** | □ PASS / □ FAIL / □ N/A |
| **Notes** | Findings, fix commit if remediated, or blocker reason |

---

## 1. Navigation (NAV-001 – NAV-010)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| NAV-001 | Main navigation renders all primary items per Doc 11 (Grippy Shoes, Apparel, Collaborations, Journal) | Code review of `snippets/header-nav.liquid` | All 4 primary nav items present in markup | Code reference showing nav item text/handles | □ | |
| NAV-002 | Grippy Shoes dropdown contains correct sub-items (Shop All, Open Sole, Closed Sole, Outdoor, Compare Styles) | Code review of `snippets/header-nav.liquid` | All 5 sub-items present under Grippy Shoes dropdown | Code reference showing sub-item markup | □ | |
| NAV-003 | Apparel dropdown contains correct sub-items | Code review of `snippets/header-nav.liquid` | Apparel sub-items present | Code reference | □ | |
| NAV-004 | Help utility menu contains correct items (About Us, FAQ, Contact Us, Returns & Exchanges) | Code review of `snippets/header-nav.liquid` | All 4 utility items present | Code reference | □ | |
| NAV-005 | Mobile hamburger menu opens/closes correctly | Code review for toggle mechanism + browser test | Hamburger button toggles mobile menu visibility | Toggle JS/class mechanism in code; screenshot for M4D | □ | |
| NAV-006 | Mobile sub-items expand as accordion | Code review for accordion markup/JS | Sub-items have expand/collapse behavior | aria-expanded attributes + toggle logic | □ | |
| NAV-007 | All navigation links resolve to valid pages | Cross-reference hrefs against templates/ | Every nav href maps to an existing template | Template inventory vs. nav hrefs | □ | |
| NAV-008 | Cart icon opens cart drawer | Code review for cart trigger mechanism | Cart icon click dispatches cart drawer open | Event listener or class toggle reference | □ | |
| NAV-009 | Cart badge updates on add-to-cart | Code review of cart.js badge update | Badge count DOM element updated after cart mutation | Code reference in cart.js | □ | |
| NAV-010 | Announcement strip displays and rotates messages | Code review of `snippets/announcement-strip.liquid` | Rotation mechanism present (interval/CSS animation) | Code reference showing rotation logic | □ | |

---

## 2. Homepage (HOME-001 – HOME-010)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| HOME-001 | Hero section renders with correct copy | Code review of `sections/hero.liquid` + `templates/index.json` | Hero section included in homepage template with schema settings | Section file + template reference | □ | |
| HOME-002 | Hero alternative concept (hero-alt) renders correctly | Code review of `sections/hero-alt.liquid` | Hero-alt section exists and is structurally valid | File existence + valid schema | □ | |
| HOME-003 | Value strip displays all metrics | Code review of `sections/value-strip.liquid` | Value strip has metric blocks with settings | Code reference | □ | |
| HOME-004 | Variant grid renders with all tabs functional | Code review of `sections/variant-grid.liquid` | Tab markup + JS toggle logic present | Code reference for tab buttons + panels | □ | |
| HOME-005 | Disciplines section renders with correct line-divider style | Code review of `sections/disciplines.liquid` | Line-divider class/element present per design system | Code reference | □ | |
| HOME-006 | 50/50 sections render correctly | Code review of `sections/fifty-fifty.liquid` | Two-column layout with image + text | Code reference | □ | |
| HOME-007 | Social proof / reviews section renders | Code review of `sections/social-proof.liquid` | Review cards or testimonial content rendered | Code reference | □ | |
| HOME-008 | Newsletter signup section renders with form | Code review of `sections/newsletter.liquid` | Form element with email input + submit button | Code reference | □ | |
| HOME-009 | GEO section renders (if included in homepage template) | Code review of `templates/index.json` | GEO section referenced or excluded by design | Template reference | □ | |
| HOME-010 | All sections use design tokens (no hardcoded colors/spacing) | Grep all homepage section files for hardcoded hex values | Zero hardcoded hex colors in section Liquid files | Grep results | □ | |

---

## 3. Collection Pages (COL-001 – COL-010)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| COL-001 | Collection hero renders with "Two Versions. One Performance." eyebrow | Code review of `sections/collection-hero.liquid` | Eyebrow text present in default or schema | Code reference | □ | |
| COL-002 | Collection intro copy matches approved version ("naturally grounded" language) | Code review of collection-hero defaults | Approved copy present | Code reference | □ | |
| COL-003 | Variant grid shows correct products per tab | Code review of `sections/variant-grid.liquid` | Tab-product mapping logic present | Code reference | □ | |
| COL-004 | Tab switching works (All/Closed/Open/One-Offs/Outdoor) | Code review for tab JS logic | Tab buttons toggle panel visibility | Code reference for JS toggle | □ | |
| COL-005 | Product cards render with correct styling (border, Quick Add, price, installment) | Code review of `snippets/product-card.liquid` | All elements present: border, Quick Add, price, installment text | Code reference | □ | |
| COL-006 | Compare link present in variant grid utilities | Code review of `sections/variant-grid.liquid` | Compare link in utility area | Code reference | □ | |
| COL-007 | Disciplines section renders in collection template | Code review of `templates/collection.json` | Disciplines section referenced | Template JSON reference | □ | |
| COL-008 | FAQ section renders with accordion in collection | Code review of `templates/collection.json` | FAQ section referenced | Template JSON reference | □ | |
| COL-009 | GEO section renders in collection | Code review of `templates/collection.json` | GEO section referenced | Template JSON reference | □ | |
| COL-010 | Sub-collection templates exist (Open Sole, Closed Sole, Outdoor, etc.) | File existence check | All sub-collection .json files present | File list | □ | |

---

## 4. PDP (PDP-001 – PDP-015)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| PDP-001 | Buy box renders with product images, title, price | Code review of `sections/pdp-buy-box.liquid` | Image gallery, product.title, product.price rendered | Code reference | □ | |
| PDP-002 | Color swatches render and are clickable | Code review of pdp-buy-box.liquid | Color option rendered as clickable elements | Code reference | □ | |
| PDP-003 | Size buttons render and are clickable | Code review of pdp-buy-box.liquid | Size option rendered as buttons | Code reference | □ | |
| PDP-004 | Variant selection updates hidden input, price, availability, image, URL | Code review of `assets/variant-selector.js` | JS updates: form input value, price text, sold-out state, image src, URL | Code reference for each update | □ | |
| PDP-005 | Add to Cart button submits via AJAX | Code review of `assets/cart.js` | fetch() or XMLHttpRequest to /cart/add.js | Code reference | □ | |
| PDP-006 | Add to Cart opens cart drawer with correct item | Code review of cart.js | After successful add, cart drawer open triggered | Code reference for drawer trigger | □ | |
| PDP-007 | Sold out variants show disabled state | Code review of variant-selector.js | Unavailable variant → button disabled + visual state | Code reference | □ | |
| PDP-008 | Features section renders | Code review of `sections/pdp-features.liquid` | Feature blocks with icons/text present | Code reference | □ | |
| PDP-009 | Sock Math section renders | Code review of `sections/pdp-sock-math.liquid` | Sock math comparison content present | Code reference | □ | |
| PDP-010 | Reviews section renders (Judge.me integration) | Code review of `sections/pdp-reviews.liquid` | Metafield reads + review card rendering | Code reference | □ | |
| PDP-011 | FAQ section renders with accordion | Code review of `templates/product.json` | FAQ section included in product template | Template JSON reference | □ | |
| PDP-012 | GEO section renders | Code review of `templates/product.json` | GEO section included in product template | Template JSON reference | □ | |
| PDP-013 | Trust row includes "Made in USA" | Code review of `snippets/trust-strip.liquid` | "Made in USA" text present | Code reference | □ | |
| PDP-014 | Sticky ATC appears when buy box scrolls out of view | Code review of `snippets/sticky-atc.liquid` | IntersectionObserver or scroll event monitoring buy box | Code reference | □ | |
| PDP-015 | Sticky ATC syncs with variant selection | Code review of sticky-atc.liquid + variant-selector.js | Variant change event updates sticky ATC display | Code reference | □ | |

---

## 5. Cart (CART-001 – CART-010)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| CART-001 | Cart drawer opens on Add to Cart | Code review of `assets/cart.js` | After /cart/add.js success, drawer class/attribute toggled | Code reference | □ | |
| CART-002 | Cart drawer displays line items correctly | Code review of `snippets/cart-drawer.liquid` | Line item loop rendering image, title, variant, price, qty | Code reference | □ | |
| CART-003 | Quantity +/- updates quantity via AJAX | Code review of `assets/cart.js` | fetch to /cart/change.js or /cart/update.js on qty button | Code reference | □ | |
| CART-004 | Remove button removes item | Code review of cart.js | Remove sets quantity to 0 or calls remove endpoint | Code reference | □ | |
| CART-005 | Subtotal updates after every cart mutation | Code review of cart.js | DOM subtotal element updated in response callback | Code reference | □ | |
| CART-006 | Free shipping progress bar works ($150 threshold) | Code review of `snippets/cart-drawer.liquid` | Threshold = 15000 (cents) or $150, progress calculation present | Code reference | □ | |
| CART-007 | Empty cart state displays correctly | Code review of cart-drawer.liquid | Empty state conditional with messaging | Code reference | □ | |
| CART-008 | Checkout button links to Shopify checkout | Code review of cart-drawer.liquid | href="/checkout" on checkout button | Code reference | □ | |
| CART-009 | Cart drawer closes on X, overlay click, Escape key | Code review of cart-drawer.liquid + cart.js | Three close mechanisms present | Code reference for each | □ | |
| CART-010 | Focus trap active when drawer is open | Code review of cart-drawer.liquid or cart.js | Focus trap logic (tabindex management or focus cycling) | Code reference | □ | |

---

## 6. Checkout Handoff (CHK-001 – CHK-003)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| CHK-001 | Checkout button navigates to Shopify checkout | Code review of cart-drawer.liquid | `href="/checkout"` or form action to checkout | Code reference | □ | |
| CHK-002 | Cart contents pass correctly to checkout | Structural review | Shopify native cart → checkout flow (no custom cart API) | Architecture confirmation | □ | |
| CHK-003 | Discount codes applicable at checkout | Shopify native | N/A — discount codes handled by Shopify checkout | N/A | □ | |

---

## 7. Analytics (ANA-001 – ANA-009)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| ANA-001 | GA4 snippet conditionally loads (blank = no output) | Code review of `snippets/analytics-head.liquid` | `{% if settings.ga4_id != blank %}` guard | Code reference | □ | |
| ANA-002 | Meta Pixel snippet conditionally loads | Code review of `snippets/meta-pixel.liquid` | `{% if settings.meta_pixel_id != blank %}` guard | Code reference | □ | |
| ANA-003 | Pinterest Tag conditionally loads | Code review of `snippets/pinterest-tag.liquid` | `{% if settings.pinterest_tag_id != blank %}` guard | Code reference | □ | |
| ANA-004 | Clarity conditionally loads | Code review of `snippets/clarity.liquid` | `{% if settings.clarity_id != blank %}` guard | Code reference | □ | |
| ANA-005 | No JavaScript errors when all IDs blank | Code review | All JS wrapped in conditionals; no bare references to undefined tracking objects | Code review confirmation | □ | |
| ANA-006 | D-045 compliance — warning in settings about native vs theme tracking | Code review of `config/settings_schema.json` | Info/warning text about Shopify native tracking vs theme tracking | Code reference | □ | |
| ANA-007 | Enhanced ecommerce data layer populated on PDP | Code review of `snippets/analytics-events.liquid` | Product data pushed to dataLayer or sent via gtag | Code reference | □ | |
| ANA-008 | Add-to-cart event fires with correct data structure | Code review of `snippets/analytics-events.liquid` | add_to_cart event with items array (id, name, price, quantity) | Code reference | □ | |
| ANA-009 | No duplicate event listeners | Code review of analytics-events.liquid | Event listener attached once (not in loop or repeated include) | Code reference | □ | |

---

## 8. SEO (SEO-001 – SEO-014)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| SEO-001 | Product JSON-LD schema present on PDP | Code review of `sections/pdp-buy-box.liquid` | `<script type="application/ld+json">` with Product schema | Code reference | □ | |
| SEO-002 | Product schema has dynamic aggregateRating | Code review of JSON-LD in pdp-buy-box | Rating values from metafields, not hardcoded numbers | Code reference | □ | |
| SEO-003 | FAQPage schema present on FAQ page | Code review of `sections/page-faq.liquid` | FAQPage JSON-LD block | Code reference | □ | |
| SEO-004 | FAQPage schema present on PDP FAQ section | Code review of product template FAQ section | FAQPage schema generated from PDP FAQ items | Code reference | □ | |
| SEO-005 | BreadcrumbList schema on all pages except homepage | Code review of `snippets/breadcrumb.liquid` | Homepage exclusion conditional | Code reference | □ | |
| SEO-006 | No duplicate BreadcrumbList schemas | Code review of theme.liquid + breadcrumb.liquid | Single inclusion point, no double rendering | Architecture review | □ | |
| SEO-007 | Organization schema on About page | Code review of `snippets/organization-schema.liquid` + theme.liquid | Conditional render on about page or global with proper scope | Code reference | □ | |
| SEO-008 | All JSON-LD is valid JSON | Parse all JSON-LD blocks in Liquid (accounting for Liquid variables) | No syntax errors in static portions | Validation results | □ | |
| SEO-009 | Meta titles follow conventions | Code review of `layout/theme.liquid` | Title tag uses `{{ page_title }}` with site name | Code reference | □ | |
| SEO-010 | Meta descriptions present | Code review of theme.liquid | `<meta name="description">` with `{{ page_description }}` | Code reference | □ | |
| SEO-011 | Canonical URLs set correctly | Code review of theme.liquid | `<link rel="canonical" href="{{ canonical_url }}">` | Code reference | □ | |
| SEO-012 | Open Graph tags present | Code review of theme.liquid | og:title, og:description, og:image, og:url meta tags | Code reference | □ | |
| SEO-013 | Sitemap accessible at /sitemap.xml | Shopify native | N/A — Shopify auto-generates sitemap | N/A | □ | |
| SEO-014 | robots.txt correctly configured | Shopify native | N/A — Shopify manages robots.txt | N/A | □ | |

---

## 9. Accessibility (A11Y-001 – A11Y-013)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| A11Y-001 | Skip navigation link present and functional | Code review of theme.liquid or header-nav.liquid | `<a href="#main-content" class="skip-link">` or equivalent | Code reference | □ | |
| A11Y-002 | All headings in logical order (no skipped levels) | Code review of all page sections | h1 → h2 → h3 hierarchy maintained | Heading audit results | □ | |
| A11Y-003 | All images have alt text or aria-hidden | Code review of img tags across files | Every `<img>` has `alt` attribute or `aria-hidden="true"` | Code reference | □ | |
| A11Y-004 | All form inputs have associated labels | Code review of newsletter, contact, pdp-buy-box | Every input has matching `<label for="">` or aria-label | Code reference | □ | |
| A11Y-005 | Focus-visible indicators on all interactive elements | Code review of `assets/barreletics-base.css` | `:focus-visible` rule present for buttons, links, inputs | Code reference | □ | |
| A11Y-006 | Keyboard navigation works end-to-end | Browser test | N/A — requires deployed preview | N/A | □ | |
| A11Y-007 | Cart drawer has focus trap | Code review of cart-drawer.liquid / cart.js | Focus cycling logic when drawer is open | Code reference | □ | |
| A11Y-008 | Mobile menu has focus trap | Code review of header-nav.liquid | Focus trap when mobile menu is open | Code reference | □ | |
| A11Y-009 | Accordion announces open/close state | Code review of `snippets/faq-accordion.liquid` | `aria-expanded` attribute toggled on trigger | Code reference | □ | |
| A11Y-010 | Dynamic content updates announced | Code review for aria-live regions | `aria-live="polite"` on cart totals, variant price changes | Code reference | □ | |
| A11Y-011 | Color contrast meets WCAG AA (4.5:1 normal, 3:1 large) | Design token analysis | Primary text on backgrounds meet 4.5:1 ratio | Token color pair analysis | □ | |
| A11Y-012 | Touch targets ≥ 44x44px on mobile | Code review of base CSS | min-height/min-width: 44px on buttons and interactive elements | Code reference | □ | |
| A11Y-013 | Reduced motion respected | Code review of base CSS | `@media (prefers-reduced-motion: reduce)` present | Code reference | □ | |

---

## 10. Performance (PERF-001 – PERF-007)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| PERF-001 | No render-blocking resources in critical path | Code review of theme.liquid | All scripts have `defer` or are at end of body; CSS loaded efficiently | Code reference | □ | |
| PERF-002 | Images lazy-loaded below fold | Code review of section files | `loading="lazy"` on images outside hero | Code reference | □ | |
| PERF-003 | JavaScript deferred | Code review of theme.liquid | `<script defer>` on all JS assets | Code reference | □ | |
| PERF-004 | No inline styles that should be in token system | Grep for `style=` with color/spacing values | Zero inline color/spacing styles in Liquid files | Grep results | □ | |
| PERF-005 | CSS has no unnecessary duplication | Code review of barreletics-base.css | No repeated rule blocks | Code review | □ | |
| PERF-006 | Font loading strategy (preload or font-display: swap) | Code review of theme.liquid + CSS | Font preload link or font-display: swap in @font-face | Code reference | □ | |
| PERF-007 | No N+1 Liquid query patterns | Code review of section files | No nested forloops querying Shopify objects | Code review | □ | |

---

## 11. Mobile (MOB-001 – MOB-009)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| MOB-001 | No horizontal overflow at 375px | Code review + browser test | CSS prevents overflow (max-width, overflow-x patterns) | Code reference; screenshot for M4D | □ | |
| MOB-002 | Typography readable without zooming | Code review of design-tokens.css | Body font-size ≥ 16px | Code reference | □ | |
| MOB-003 | Navigation works correctly (hamburger + accordion) | Cross-ref NAV-005, NAV-006 | Mobile nav mechanism present | Cross-reference | □ | |
| MOB-004 | Product cards stack correctly | Code review of product-card + variant-grid CSS | Mobile grid (1-col or 2-col) defined | Code reference | □ | |
| MOB-005 | PDP buy box stacks correctly | Code review of pdp-buy-box responsive rules | Single-column layout on mobile breakpoint | Code reference | □ | |
| MOB-006 | Sticky ATC shows selected size on mobile | Code review of sticky-atc.liquid | Size displayed in sticky bar | Code reference | □ | |
| MOB-007 | Cart drawer usable on mobile | Code review of cart-drawer.liquid | Full-width or near-full-width on mobile | Code reference | □ | |
| MOB-008 | Forms usable on mobile | Code review of base CSS | Input font-size ≥ 16px (prevents iOS zoom) | Code reference | □ | |
| MOB-009 | Footer stacks correctly | Code review of footer.liquid | Mobile-responsive column layout | Code reference | □ | |

---

## 12. Desktop (DSK-001 – DSK-006)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| DSK-001 | Layout correct at 1280px | Code review of base CSS | Container max-width or responsive grid at 1280px | Code reference | □ | |
| DSK-002 | Layout correct at 1440px+ | Code review of base CSS | Container constrains content at large widths | Code reference | □ | |
| DSK-003 | Navigation dropdown alignment correct | Code review of header-nav CSS | Dropdown positioned relative to parent | Code reference | □ | |
| DSK-004 | Variant grid displays correct column count | Code review of variant-grid CSS | Desktop grid-template-columns (3-4 columns) | Code reference | □ | |
| DSK-005 | 50/50 sections display side-by-side | Code review of fifty-fifty CSS | Flex or grid with two equal columns at desktop | Code reference | □ | |
| DSK-006 | Footer displays in correct column layout | Code review of footer CSS | Multi-column grid/flex at desktop | Code reference | □ | |

---

## 13. Integrations (INT-001 – INT-007)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| INT-001 | Judge.me metafield references correct (namespace.key) | Code review of `sections/pdp-reviews.liquid` | Metafield accessed as `product.metafields.judgeme.*` or `reviews.*` | Code reference | □ | |
| INT-002 | Judge.me widget hooks present in DOM | Code review of pdp-reviews.liquid | Container div with ID/class for Judge.me API binding | Code reference | □ | |
| INT-003 | Judge.me default CSS NOT loaded | Code review of theme.liquid + pdp-reviews | No `<link>` to judgeme CSS CDN | Absence confirmation | □ | |
| INT-004 | Help Scout Beacon conditionally loads | Code review of `snippets/helpscout-beacon.liquid` | `{% if settings.helpscout_beacon_id != blank %}` guard | Code reference | □ | |
| INT-005 | Tidio widget conditionally loads | Code review of `snippets/tidio-widget.liquid` | `{% if settings.tidio_key != blank %}` guard | Code reference | □ | |
| INT-006 | Search Console verification meta tag conditionally renders | Code review of theme.liquid | `{% if settings.google_verification != blank %}` guard | Code reference | □ | |
| INT-007 | Settings schema has all integration fields | Code review of `config/settings_schema.json` | Fields for: GA4, Meta Pixel, Pinterest, Clarity, Help Scout, Tidio, Search Console | Code reference | □ | |

---

## 14. Customer Support (SUP-001 – SUP-007)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| SUP-001 | Contact form renders and has required fields | Code review of `sections/page-contact.liquid` | Form with name, email, message fields | Code reference | □ | |
| SUP-002 | Partner inquiry form renders with program dropdown | Code review of `sections/page-partners.liquid` | Form with program select/dropdown | Code reference | □ | |
| SUP-003 | FAQ content matches Doc 07 Knowledge Base | Code review of `sections/page-faq.liquid` | FAQ items present and aligned with product knowledge base | Content comparison | □ | |
| SUP-004 | Size Guide content matches Doc 07 | Code review of `sections/page-size-guide.liquid` | Size chart/guide content present | Code reference | □ | |
| SUP-005 | Shipping page content matches Doc 07 | Code review of `sections/page-shipping.liquid` | Shipping information present | Code reference | □ | |
| SUP-006 | Returns page content matches Doc 07 | Code review of `sections/page-returns.liquid` | Return policy content present with "30-day, new sellable condition" | Code reference | □ | |
| SUP-007 | Warranty page content matches Doc 07 | Code review of `sections/page-warranty.liquid` | Warranty content with "90-day manufacturing defects" | Code reference | □ | |

---

## 15. Business Rules (BIZ-001 – BIZ-010)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| BIZ-001 | Free shipping threshold = $150 | Code review of `snippets/cart-drawer.liquid` | Threshold value = 15000 (cents) or 150 (dollars) | Code reference | □ | |
| BIZ-002 | Announcement strip includes "Code SAVE15" | Code review of `snippets/announcement-strip.liquid` | "SAVE15" text in announcement content | Code reference | □ | |
| BIZ-003 | 30-day return policy stated correctly (new, sellable condition) | Code review of page-returns.liquid | "30" + "new, sellable condition" language | Code reference | □ | |
| BIZ-004 | 90-day warranty stated correctly (manufacturing defects only) | Code review of page-warranty.liquid | "90" + "manufacturing defects" language | Code reference | □ | |
| BIZ-005 | No internal wholesale pricing exposed publicly | Code review of page-wholesale.liquid | No actual dollar amounts for wholesale pricing | Code reference | □ | |
| BIZ-006 | No retired claims present | Grep all .liquid files for retired claims per RETIRED_CLAIMS.md | Zero matches for retired claim strings | Grep results | □ | |
| BIZ-007 | "Never Loses Grip" present (approved claim) | Grep .liquid files for "Never Loses Grip" | At least one match | Grep results | □ | |
| BIZ-008 | "Never degrades" NOT present (retired per D-018) | Grep all .liquid files for "Never degrades" | Zero matches | Grep results | □ | |
| BIZ-009 | "No allergic reaction risk" NOT present | Grep all .liquid files | Zero matches | Grep results | □ | |
| BIZ-010 | Product pricing consistent ($74 where stated) | Code review of pdp-buy-box.liquid | Dynamic pricing from `product.price` (not hardcoded) | Code reference | □ | |

---

## 16. Launch Readiness (LR-001 – LR-010)

| ID | Requirement | Validation Method | Expected Result | Evidence Required | Status | Notes |
|----|-------------|-------------------|-----------------|-------------------|--------|-------|
| LR-001 | All page templates exist and are valid JSON | JSON parse of all templates/*.json | Zero parse errors | Validation tool output | □ | |
| LR-002 | Settings schema is valid JSON | JSON parse of `config/settings_schema.json` | Zero parse errors | Validation output | □ | |
| LR-003 | Settings data is valid JSON | JSON parse of `config/settings_data.json` | Zero parse errors | Validation output | □ | |
| LR-004 | Locales file exists and is valid JSON | JSON parse of `locales/en.default.json` | Zero parse errors | Validation output | □ | |
| LR-005 | No temporary/versioned files in production | File inventory check | No v2, m3 suffixes in canonical paths (hero-alt exempt per D-041) | File list review | □ | |
| LR-006 | Redirect map complete | Review of `planning/m4a-redirect-map.md` | Document exists with redirect entries | File existence + content review | □ | |
| LR-007 | Asset inventory documented (pending items flagged) | Review of `planning/m4a-asset-inventory.md` | Pending items identified | Content review | □ | |
| LR-008 | Content inventory reviewed (pending items flagged) | Review of `planning/m4a-content-inventory.md` | Pending items identified | Content review | □ | |
| LR-009 | Decision Log up to date | Review of `planning/10-decision-log.md` | Latest decision = D-046 | Code reference | □ | |
| LR-010 | All Foundation compliance items verified | File existence check for docs 01-13 | All 13 foundation docs present in planning/ | File list | □ | |

---

## Exit Criteria

M4C passes when:
1. All PASS + N/A items account for 100% of validations (zero unresolved FAILs)
2. Any remaining FAILs have documented Owner actions or are deferred to M4D with rationale
3. QA Report (`planning/m4c-qa-report.md`) is complete
4. All fixes committed with validation ID references
