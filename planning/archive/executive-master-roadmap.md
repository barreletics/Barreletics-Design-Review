# Executive Master Roadmap — Sprints 07–56

**Date:** 2026-07-13  
**Status:** PLANNING  
**Context:** Sprints 01–06 complete (knowledge base built, planning done). Ready for decisions + implementation.  
**Timeline:** 6 weeks per IMPLEMENTATION-ROADMAP-Jul2026.md  
**Implementation Order:** Tokens → Header → PDP → Home → Collection → Articles

---

## PHASE A: ADR RESOLUTION + DOCUMENT APPROVAL (Sprints 07–10)

---

### Sprint 07: ADR-01 Color Palette Resolution
**Goal:** Resolve the canonical color palette conflict between docs/04 and docs/06.
**Deliverables:**
- ADR-01-color-palette-values.md updated with DECIDED status
- docs/04-COMPONENT-LIBRARY.md lines 23–26 updated to match canonical values
- docs/06-HOMEPAGE-ARCHITECTURE.md confirmed as source of truth for :root tokens
**Dependencies:** Architect decision (ChatGPT)
**Acceptance Criteria:**
- ADR-01 status = DECIDED with rationale
- Zero color conflicts between docs/04 and docs/06
- docs/10-DECISIONS.md D-007 resolved
**Complexity:** S
**Expected Outcome:** Single canonical color palette; no ambiguity for Shopify token file
**Critical Path:** Yes — blocks all token implementation

---

### Sprint 08: ADR-02 + ADR-03 Batch Resolution
**Goal:** Resolve shipping threshold (ADR-02) and button border-radius (ADR-03) conflicts.
**Deliverables:**
- ADR-02-free-shipping-threshold.md → DECIDED
- ADR-03-button-border-radius.md → DECIDED
- docs/05-PDP-ARCHITECTURE.md: 4 instances of "$75" → "$150"
- docs/04 + docs/05 radius conflict resolved
**Dependencies:** Architect decision (ChatGPT)
**Acceptance Criteria:**
- Zero "$75" instances in docs/05
- docs/10 CONFLICT-001 resolved
- PDP CTA radius rule documented (exception or system change)
**Complexity:** S
**Expected Outcome:** PDP implementation unblocked for buttons and shipping banner
**Critical Path:** Yes — blocks PDP build

---

### Sprint 09: ADR-04 + ADR-05 + ADR-06 + ADR-07 Batch Resolution
**Goal:** Resolve eyebrow letter-spacing, PDP text color, review card radius, and star rating color.
**Deliverables:**
- ADR-04 through ADR-07 → DECIDED
- docs/04 canonical eyebrow spec updated to single value
- docs/04 system token `--br-text` resolved (#1c1916 vs #050505)
- Review card and star rating values locked
**Dependencies:** Architect decision (ChatGPT); ADR-01 must be resolved first
**Acceptance Criteria:**
- All 7 ADRs in DECIDED state
- docs/10 conflicts C-002, C-004 resolved
- Complete token inventory with zero ambiguities
**Complexity:** M
**Expected Outcome:** Design system fully resolved; all tokens locked for implementation
**Critical Path:** Yes — blocks token implementation

---

### Sprint 10: Document Review Batch (6 PENDING REVIEW docs)
**Goal:** Get all 6 PENDING REVIEW documents to APPROVED status.
**Deliverables:**
- docs/01-BRAND-NORTH-STAR.md → APPROVED
- docs/02-BRAND-SYSTEM.md → APPROVED
- docs/03-DESIGN-SYSTEM.md → APPROVED
- docs/07-COPY-GUIDE.md → APPROVED
- docs/09-PRODUCT-KNOWLEDGE.md → APPROVED
- docs/10-DECISIONS.md → APPROVED
**Dependencies:** ADR-01 through ADR-07 resolved (Sprint 09 complete)
**Acceptance Criteria:**
- ChatGPT grants APPROVED status to all 6
- Review packets (planning/review-01 through review-10) archived
- docs/INDEX.md updated to reflect all APPROVED
**Complexity:** M
**Expected Outcome:** Entire knowledge base is APPROVED — implementation can proceed with full authority
**Critical Path:** Yes — blocks implementation phase

---

## PHASE B: REMEDIATION BATCHES (Sprints 11–15)

---

### Sprint 11: Critical Remediation (CRIT-001 through CRIT-003)
**Goal:** Fix the 3 critical consistency findings blocking implementation.
**Deliverables:**
- CRIT-001: Color palette disagreement resolved in docs/04
- CRIT-002: All $75 → $150 in docs/05 (4 instances)
- CRIT-003: Button radius contradiction resolved
**Dependencies:** Sprint 09 (ADR decisions locked)
**Acceptance Criteria:**
- consistency-remediation-plan.md tickets CRIT-001–003 marked DONE
- grep for "$75" in docs/05 returns 0 results
- docs/04 and docs/05 agree on button radius value
**Complexity:** S
**Expected Outcome:** Zero critical conflicts in knowledge base
**Critical Path:** Yes — blocking

---

### Sprint 12: High Priority Remediation Batch 1 (HIGH-001 through HIGH-004)
**Goal:** Resolve eyebrow letter-spacing, PDP text color, copy cross-references, and product variant naming.
**Deliverables:**
- HIGH-001: Canonical eyebrow spec applied to docs/04
- HIGH-002: --br-text token updated system-wide
- HIGH-003: Cross-references added to docs/01, 02, 09, 10 pointing to docs/07
- HIGH-004: Variant naming in docs/09 aligned with docs/05
**Dependencies:** Sprint 11 (critical remediation done)
**Acceptance Criteria:**
- Tickets HIGH-001–004 marked DONE
- Single source of truth for eyebrow styling
- All docs reference the copy guide
**Complexity:** M
**Expected Outcome:** Token system complete and internally consistent
**Critical Path:** Yes — tokens feed into Shopify implementation

---

### Sprint 13: High Priority Remediation Batch 2 (HIGH-005 through HIGH-008)
**Goal:** Resolve remaining high-priority design token and structure conflicts.
**Deliverables:**
- HIGH-005: docs/04 vs docs/05 radius reconciliation complete
- HIGH-006: Matured homepage token inheritance documented
- HIGH-007: Section-level status indicators added to docs/06
- HIGH-008: docs/03 design principles aligned with docs/04 implementation
**Dependencies:** Sprint 12
**Acceptance Criteria:**
- Tickets HIGH-005–008 marked DONE
- docs/03 and docs/04 use identical token names and values
**Complexity:** M
**Expected Outcome:** No design token ambiguity remains between any docs/ files
**Critical Path:** No — parallel with Sprint 14 possible

---

### Sprint 14: Medium Priority Remediation (MED-001 through MED-008)
**Goal:** Resolve all 8 medium-priority findings (structural gaps, missing references, documentation holes).
**Deliverables:**
- MED-001 through MED-008 resolved
- Cross-reference links verified
- Dead references removed
**Dependencies:** Sprint 12 (HIGH batch 1 done for structural references)
**Acceptance Criteria:**
- All MED tickets marked DONE
- No broken internal references in docs/
**Complexity:** M
**Expected Outcome:** Documentation is clean and internally consistent
**Critical Path:** No

---

### Sprint 15: Low Priority Remediation + Audit Close-Out
**Goal:** Resolve all LOW findings and close the consistency audit.
**Deliverables:**
- LOW-001 through remaining LOW tickets resolved
- planning/knowledge-base-consistency-audit.md marked CLOSED
- Final audit re-run confirms 0 open findings
**Dependencies:** Sprint 14
**Acceptance Criteria:**
- All 30 findings from consistency audit resolved
- Clean audit report
- consistency-remediation-plan.md all tickets = DONE
**Complexity:** S
**Expected Outcome:** Knowledge base is production-ready reference material
**Critical Path:** No

---

## PHASE C: SHOPIFY FOUNDATION — TOKENS + GLOBAL COMPONENTS (Sprints 16–20)

---

### Sprint 16: Shopify Token File — CSS Custom Properties
**Goal:** Create the canonical Shopify token file from resolved docs/03 + docs/04 values.
**Deliverables:**
- `assets/barreletics-tokens.css` — all design tokens as CSS custom properties
- Color palette, typography scale, spacing scale, border-radius, shadows
- Token naming convention documented
**Dependencies:** Sprint 12 (all token conflicts resolved)
**Acceptance Criteria:**
- Every token in docs/03 has a corresponding CSS custom property
- File validates with no syntax errors
- Token file referenced by theme.liquid
**Complexity:** M
**Expected Outcome:** Single source of truth for all Shopify CSS values
**Critical Path:** Yes — all components consume tokens

---

### Sprint 17: Global Header Component (Liquid)
**Goal:** Build the Shopify Liquid header section matching docs/04 + live site.
**Deliverables:**
- `sections/header.liquid` — announcement bar + nav + logo + cart
- Free shipping threshold bar ($150) with dynamic messaging
- Mobile hamburger menu
- Schema settings for merchant customization
**Dependencies:** Sprint 16 (token file)
**Acceptance Criteria:**
- Header renders correctly at all breakpoints (320px–1440px)
- Free shipping bar uses $150 threshold
- Logo links to homepage
- Navigation matches live site structure
**Complexity:** L
**Expected Outcome:** Global header ready; all pages can reference it
**Critical Path:** Yes — every page uses header

---

### Sprint 18: Global Footer Component (Liquid)
**Goal:** Build the Shopify Liquid footer section.
**Deliverables:**
- `sections/footer.liquid` — links, newsletter signup, social, copyright
- Schema settings for editable content
- Mobile-responsive layout
**Dependencies:** Sprint 16 (token file)
**Acceptance Criteria:**
- Footer renders correctly at all breakpoints
- Newsletter form functional
- All links resolve
**Complexity:** M
**Expected Outcome:** Global footer ready; all pages can reference it
**Critical Path:** Yes — every page uses footer

---

### Sprint 19: Typography + Base Styles
**Goal:** Implement global typography and base element styles.
**Deliverables:**
- `assets/barreletics-base.css` — reset, typography, spacing utilities
- Roboto 400–700 loaded (or system font fallback)
- Heading scale, body copy, eyebrow component styles
- Utility classes for common patterns
**Dependencies:** Sprint 16 (token file for values)
**Acceptance Criteria:**
- Typography matches docs/03 spec at all breakpoints
- Eyebrow letter-spacing uses resolved canonical value
- No !important overrides
**Complexity:** M
**Expected Outcome:** All text rendering matches design system
**Critical Path:** Yes — feeds all component styling

---

### Sprint 20: Button + Form Component Library
**Goal:** Build reusable button and form input components per docs/04 specs.
**Deliverables:**
- `snippets/button.liquid` — primary, secondary, ghost variants
- `snippets/input.liquid` — text, email, number inputs
- `snippets/select.liquid` — size picker / dropdown
- `assets/barreletics-components.css` — component styles
**Dependencies:** Sprint 16, Sprint 19
**Acceptance Criteria:**
- Buttons use resolved border-radius value (per ADR-03)
- All states: default, hover, active, disabled, loading
- Components accept Liquid parameters for customization
**Complexity:** M
**Expected Outcome:** Reusable component library ready for PDP + Homepage
**Critical Path:** Yes — PDP uses buttons and inputs

---

## PHASE D: PDP IMPLEMENTATION (Sprints 21–30)

---

### Sprint 21: PDP Template Shell + Layout Grid
**Goal:** Create the PDP page template with responsive grid layout.
**Deliverables:**
- `templates/product.liquid` (or product.json + sections)
- Two-column layout: media gallery left, product info right
- 1200px max-width container with 32px gutters (16px mobile)
**Dependencies:** Sprint 17, Sprint 18, Sprint 19
**Acceptance Criteria:**
- Grid matches docs/05 layout spec
- Responsive breakpoints: mobile, tablet, desktop
- Header + footer render correctly on PDP
**Complexity:** M
**Expected Outcome:** PDP skeleton ready for components
**Critical Path:** Yes — all PDP components attach to this

---

### Sprint 22: PDP Media Gallery
**Goal:** Implement product image gallery with thumbnails and zoom.
**Deliverables:**
- `sections/product-media.liquid` — main image + thumbnail strip
- Swipe support on mobile
- Lazy loading for performance
**Dependencies:** Sprint 21
**Acceptance Criteria:**
- Gallery displays all product images from Shopify
- Thumbnail click swaps main image
- Images are responsive (srcset)
- Matches docs/05 media gallery spec
**Complexity:** L
**Expected Outcome:** Product images display correctly
**Critical Path:** Yes — visual-first PDP

---

### Sprint 23: PDP Product Info — Title, Price, Badges
**Goal:** Implement the product title block, pricing, and trust badges.
**Deliverables:**
- Product title with correct typography (warm ink #1c1916)
- Price display with compare-at-price logic
- Star rating display (using resolved ADR-07 color)
- Trust badges row
**Dependencies:** Sprint 21, Sprint 16 (token colors)
**Acceptance Criteria:**
- Title uses resolved --br-text color
- Star rating uses resolved ADR-07 value
- Price formatting matches Shopify money format
- Badges from docs/05 spec
**Complexity:** M
**Expected Outcome:** Product identity section complete
**Critical Path:** Yes

---

### Sprint 24: PDP Variant Selector
**Goal:** Build size/color variant picker with inventory-aware UI.
**Deliverables:**
- Size pill grid (per docs/05 variant UI spec)
- Color swatch row
- Sold-out state styling
- Variant selection updates price and availability
**Dependencies:** Sprint 20 (button/form components), Sprint 21
**Acceptance Criteria:**
- All variants from Shopify product render
- Selecting variant updates URL, price, and image
- Sold-out variants disabled with visual indicator
- Border-radius per ADR-03 resolution
**Complexity:** L
**Expected Outcome:** Customers can select variants correctly
**Critical Path:** Yes — required for add-to-cart

---

### Sprint 25: PDP Add to Cart + Shipping Bar
**Goal:** Implement add-to-cart button and free shipping progress bar.
**Deliverables:**
- Add to cart button with loading state
- Quantity selector
- Free shipping progress bar ($150 threshold per ADR-02)
- Cart drawer or redirect behavior
**Dependencies:** Sprint 24 (variant must be selected), Sprint 20
**Acceptance Criteria:**
- Add to cart sends correct variant ID to Shopify
- Shipping bar shows progress toward $150
- Button uses resolved border-radius
- Loading state prevents double-submit
**Complexity:** L
**Expected Outcome:** Core purchase flow functional
**Critical Path:** Yes — revenue-blocking

---

### Sprint 26: PDP Accordion Sections
**Goal:** Build expandable accordion for product details, materials, shipping info.
**Deliverables:**
- `snippets/accordion.liquid` — reusable component
- PDP sections: Description, Materials, Shipping & Returns, Size Guide
- Accessible: aria-expanded, keyboard nav
**Dependencies:** Sprint 21
**Acceptance Criteria:**
- Matches docs/05 accordion spec
- Content from metafields or section settings
- Only one panel open at a time (or configurable)
- Smooth open/close animation
**Complexity:** M
**Expected Outcome:** Product details accessible without page scroll
**Critical Path:** No — enhances but doesn't block purchase

---

### Sprint 27: PDP Review Section
**Goal:** Implement customer review display section.
**Deliverables:**
- Review cards with star rating, author, date, body
- Review card border-radius per ADR-06
- Star color per ADR-07
- Pagination or "load more"
**Dependencies:** Sprint 21, Sprint 16
**Acceptance Criteria:**
- Reviews render from Shopify metafields or app integration
- Card radius matches ADR-06 decision
- Star color matches ADR-07 decision
- Empty state when no reviews
**Complexity:** M
**Expected Outcome:** Social proof visible on PDP
**Critical Path:** No

---

### Sprint 28: PDP Cross-Sell / You May Also Like
**Goal:** Implement related products section below PDP.
**Deliverables:**
- Related products grid (4 items desktop, 2 mobile)
- Product card component with image, title, price
- Logic: same collection or manual recommendation
**Dependencies:** Sprint 21
**Acceptance Criteria:**
- Shows relevant products (not current product)
- Product cards link to correct PDP
- Responsive grid layout
**Complexity:** M
**Expected Outcome:** Increases AOV and browse depth
**Critical Path:** No

---

### Sprint 29: PDP Mobile Optimization
**Goal:** Ensure PDP is fully optimized for mobile experience.
**Deliverables:**
- Sticky add-to-cart bar on mobile scroll
- Touch-friendly variant selectors (44px minimum)
- Image gallery swipe behavior
- Accordion touch targets
**Dependencies:** Sprints 22–28 (all PDP components built)
**Acceptance Criteria:**
- All interactive elements ≥44px touch target
- Sticky CTA appears after scrolling past main button
- No horizontal overflow at 320px
- PageSpeed mobile score ≥ 70
**Complexity:** M
**Expected Outcome:** Mobile conversion-ready PDP
**Critical Path:** No — but high revenue impact

---

### Sprint 30: PDP Integration Testing + Bug Fixes
**Goal:** End-to-end testing of complete PDP and fix all issues.
**Deliverables:**
- Full PDP test pass on desktop + mobile
- Bug fix commits for any visual/functional issues
- Cross-browser check (Chrome, Safari, Firefox)
- Lighthouse audit and performance fixes
**Dependencies:** Sprints 21–29 all complete
**Acceptance Criteria:**
- PDP matches docs/05 at pixel level (±2px tolerance)
- Add-to-cart flow works end-to-end
- No console errors
- Lighthouse performance ≥ 70, accessibility ≥ 90
**Complexity:** M
**Expected Outcome:** PDP is production-ready
**Critical Path:** Yes — PDP must be complete before homepage launch

---

## PHASE E: HOMEPAGE IMPLEMENTATION (Sprints 31–40)

---

### Sprint 31: Homepage Template + Section Order
**Goal:** Create homepage template with correct section ordering per docs/06.
**Deliverables:**
- `templates/index.json` with section order
- Section slots matching IMPLEMENTATION-ROADMAP phase decisions
- Keep sections: Hero (01), 50/50 Progress (03), The Problem (09), Chair Pose (17)
**Dependencies:** Sprint 17, Sprint 18 (header/footer)
**Acceptance Criteria:**
- Homepage loads with correct section order
- All "Keep" sections positioned correctly
- Sections render as empty placeholders until built
**Complexity:** S
**Expected Outcome:** Homepage skeleton ready for section development
**Critical Path:** Yes — all homepage sections attach here

---

### Sprint 32: Hero Section (Section 01 — Keep)
**Goal:** Implement Hero section per docs/04 + docs/06 spec.
**Deliverables:**
- `sections/hero.liquid` — full-width hero with video/image background
- Eyebrow text, headline, subhead, CTA button
- "See in action" button (per IMPLEMENTATION-ROADMAP notes)
- Mobile-responsive with text overlay
**Dependencies:** Sprint 16, Sprint 19, Sprint 20
**Acceptance Criteria:**
- Hero matches docs/06 HTML/CSS spec
- Eyebrow uses canonical letter-spacing
- CTA button uses resolved radius
- Video loads or falls back to image
**Complexity:** L
**Expected Outcome:** Above-the-fold homepage experience complete
**Critical Path:** Yes — first thing visitors see

---

### Sprint 33: 50/50 Progress Section (Section 03 — Keep)
**Goal:** Implement 50/50 split section with "Trusted by" rating.
**Deliverables:**
- `sections/progress-split.liquid`
- Image/text split layout
- Star rating + "Trusted by" social proof element
- Schema for editable copy
**Dependencies:** Sprint 16, Sprint 19
**Acceptance Criteria:**
- Layout matches docs/06 Section 03 spec
- "Trusted by" rating from current site preserved
- Responsive: stacks vertically on mobile
**Complexity:** M
**Expected Outcome:** Social proof + visual storytelling section live
**Critical Path:** No

---

### Sprint 34: Problem Section (Section 09 — Keep/Matured)
**Goal:** Implement The Problem section.
**Deliverables:**
- `sections/the-problem.liquid`
- Full-width statement with supporting imagery
- Typography per docs/04 manifesto component
**Dependencies:** Sprint 16, Sprint 19
**Acceptance Criteria:**
- Matches matured design from docs/06
- Copy from docs/07 (Section 09 content)
- Correct background color (warm #eae5da or white per ADR-01)
**Complexity:** S
**Expected Outcome:** Emotional hook section live
**Critical Path:** No

---

### Sprint 35: Chair Pose Section (Section 17 — Keep)
**Goal:** Implement "Never Slip in Chair Pose" section.
**Deliverables:**
- `sections/chair-pose.liquid`
- Lifestyle imagery with text overlay
- Shopify settings for image/copy customization
**Dependencies:** Sprint 16, Sprint 19
**Acceptance Criteria:**
- Layout matches current live site (Keep decision)
- Image quality ≥ 1200px wide source
- Mobile responsive
**Complexity:** M
**Expected Outcome:** Use-case demonstration section live
**Critical Path:** No

---

### Sprint 36: Refactor Sections Batch 1 (06, 07, 08)
**Goal:** Build high-priority refactor sections with color compliance.
**Deliverables:**
- Section 06: `sections/refactor-06.liquid`
- Section 07: `sections/refactor-07.liquid`
- Section 08: `sections/refactor-08.liquid`
- All using warm/neutral palette (NO black/orange)
**Dependencies:** Sprint 16, Sprint 19, Sprint 20
**Acceptance Criteria:**
- Zero instances of #000000 or orange (#ff6600 variants)
- Colors from resolved token palette only
- Shopify settings schemas for merchant editing
**Complexity:** L
**Expected Outcome:** First refactor batch deployed
**Critical Path:** No

---

### Sprint 37: Refactor Sections Batch 2 (10, 12, 13, 14)
**Goal:** Build second batch of refactored homepage sections.
**Deliverables:**
- Sections 10, 12, 13, 14 as Liquid sections
- Consistent component usage (buttons, typography, spacing)
- Color-compliant implementation
**Dependencies:** Sprint 36 (patterns established)
**Acceptance Criteria:**
- Sections render correctly at all breakpoints
- Token file values used exclusively (no hardcoded colors)
- Pass visual QA against docs/06 spec
**Complexity:** L
**Expected Outcome:** Second refactor batch deployed
**Critical Path:** No

---

### Sprint 38: Refactor Sections Batch 3 (18, 19, 20, 21)
**Goal:** Build third batch of refactored homepage sections.
**Deliverables:**
- Sections 18, 19, 20, 21 as Liquid sections
- Shopify settings for sections requiring merchant config (18, 20, 21)
**Dependencies:** Sprint 37
**Acceptance Criteria:**
- Shopify settings functional and correctly mapped
- Sections render in theme editor preview
- Color compliance verified
**Complexity:** L
**Expected Outcome:** Third refactor batch deployed
**Critical Path:** No

---

### Sprint 39: Refactor Sections Batch 4 (23, 26, 27, 28)
**Goal:** Build final refactor batch including FAQ and Newsletter.
**Deliverables:**
- Section 23: `sections/refactor-23.liquid`
- Section 26 (Notes from Studio): `sections/notes-studio.liquid`
- Section 27 (FAQ): `sections/faq.liquid` — accordion-based
- Section 28 (Newsletter): `sections/newsletter.liquid`
**Dependencies:** Sprint 26 (accordion component from PDP)
**Acceptance Criteria:**
- FAQ uses accordion component from Sprint 26
- Newsletter form submits to Shopify email
- All sections color-compliant
**Complexity:** L
**Expected Outcome:** All refactor sections deployed
**Critical Path:** No

---

### Sprint 40: Homepage Integration Testing + Undecided Sections
**Goal:** Test full homepage flow and resolve remaining undecided sections (04, 15, 24, 25, 29).
**Deliverables:**
- Full homepage visual QA pass
- Decision on 5 undecided sections (build or cut)
- Bug fix commits
- Section order finalized in templates/index.json
**Dependencies:** Sprints 31–39 complete
**Acceptance Criteria:**
- Homepage matches docs/06 architecture at full fidelity
- All section transitions smooth
- No layout shifts (CLS < 0.1)
- All undecided sections have KEEP/CUT decision
**Complexity:** M
**Expected Outcome:** Homepage production-ready
**Critical Path:** Yes — homepage must be complete for launch

---

## PHASE F: COLLECTION + CONTENT PAGES (Sprints 41–45)

---

### Sprint 41: Collection Page Template
**Goal:** Build product collection grid page.
**Deliverables:**
- `templates/collection.liquid` (or collection.json)
- Product card grid (responsive: 4-col desktop, 2-col mobile)
- Filtering + sorting UI
- Collection hero banner
**Dependencies:** Sprint 16, Sprint 19, Sprint 20
**Acceptance Criteria:**
- Products display with image, title, price, quick-add
- Grid matches Barreletics Collection design (from design review)
- Pagination or infinite scroll
- SEO: proper heading hierarchy
**Complexity:** L
**Expected Outcome:** Customers can browse product collections
**Critical Path:** Yes — primary shopping path

---

### Sprint 42: Blog/Article Template
**Goal:** Build article page template for Barreletics content (6 article designs exist).
**Deliverables:**
- `templates/article.liquid`
- Article layout: hero image, title, body, author, date
- Related articles component
- Social sharing
**Dependencies:** Sprint 16, Sprint 19
**Acceptance Criteria:**
- Article renders rich HTML content correctly
- Typography matches docs/03 spec
- Mobile-readable (max 680px content width)
- Matches article designs from design review
**Complexity:** M
**Expected Outcome:** Blog/content marketing pages functional
**Critical Path:** No

---

### Sprint 43: Blog Index Page
**Goal:** Build blog listing page with article cards.
**Deliverables:**
- `templates/blog.liquid`
- Article card grid with featured image, title, excerpt
- Tag filtering
- Pagination
**Dependencies:** Sprint 42
**Acceptance Criteria:**
- Blog cards link to correct articles
- Responsive grid layout
- Matches Blog design from design review
**Complexity:** S
**Expected Outcome:** Blog browsing experience complete
**Critical Path:** No

---

### Sprint 44: Static Pages (About, Contact, Shipping Policy)
**Goal:** Build standard static page templates.
**Deliverables:**
- `templates/page.liquid` — default rich text page
- About page with founder letter content
- Contact page with form
- Shipping/Returns policy page
**Dependencies:** Sprint 16, Sprint 19
**Acceptance Criteria:**
- Pages render rich content from Shopify page editor
- Contact form submits correctly
- Policy content matches docs/09 product knowledge
**Complexity:** M
**Expected Outcome:** All standard store pages functional
**Critical Path:** No — but needed for launch

---

### Sprint 45: 404 Page + Cart Page
**Goal:** Build 404 error page and standalone cart page.
**Deliverables:**
- `templates/404.liquid` — branded error page with search + popular products
- `templates/cart.liquid` — full cart with quantity edit, remove, proceed to checkout
- Free shipping progress bar on cart ($150 threshold)
**Dependencies:** Sprint 16, Sprint 20
**Acceptance Criteria:**
- 404 includes search functionality
- Cart updates quantities via AJAX
- Shipping bar matches PDP implementation
- Checkout button prominent
**Complexity:** M
**Expected Outcome:** Error and cart experiences complete
**Critical Path:** Yes — cart is purchase-critical

---

## PHASE G: INTEGRATION, QA, MIGRATION (Sprints 46–50)

---

### Sprint 46: Full Theme Integration Test
**Goal:** Verify all pages work together as a complete theme.
**Deliverables:**
- End-to-end user flow testing: Home → Collection → PDP → Cart → Checkout
- Cross-page navigation verification
- Header/footer consistency check
- Session/cart persistence validation
**Dependencies:** Sprints 30, 40, 41, 45 (all page types built)
**Acceptance Criteria:**
- Complete purchase flow works without errors
- Navigation between all page types functional
- Cart persists across page navigation
- No 404s on internal links
**Complexity:** M
**Expected Outcome:** Theme functions as cohesive unit
**Critical Path:** Yes — must pass before migration

---

### Sprint 47: Performance Optimization
**Goal:** Optimize theme for Core Web Vitals and Shopify speed score.
**Deliverables:**
- Image optimization (WebP, srcset, lazy loading)
- CSS/JS minification and critical path extraction
- Font loading strategy (preload, display: swap)
- Lighthouse audit report with all scores ≥ 70
**Dependencies:** Sprint 46 (all pages functional first)
**Acceptance Criteria:**
- LCP < 2.5s on mobile (3G simulation)
- CLS < 0.1
- FID/INP < 200ms
- Shopify speed score ≥ 60
**Complexity:** M
**Expected Outcome:** Fast-loading store, good SEO signals
**Critical Path:** No — but impacts ranking and conversion

---

### Sprint 48: Accessibility Audit + Fixes
**Goal:** Ensure WCAG 2.1 AA compliance across all page types.
**Deliverables:**
- Full accessibility audit (axe-core + manual testing)
- Fix all critical and serious accessibility violations
- Keyboard navigation verified on all interactive elements
- Screen reader testing on key flows
**Dependencies:** Sprint 46
**Acceptance Criteria:**
- Zero critical axe-core violations
- All interactive elements keyboard-accessible
- Color contrast ratios ≥ 4.5:1 (text) and 3:1 (large text)
- ARIA labels on all icon buttons
**Complexity:** M
**Expected Outcome:** Store accessible to all users
**Critical Path:** No — but legal and ethical requirement

---

### Sprint 49: SEO + Structured Data
**Goal:** Implement SEO fundamentals and structured data markup.
**Deliverables:**
- JSON-LD Product schema on PDP
- JSON-LD Organization schema sitewide
- JSON-LD BreadcrumbList on all pages
- Meta titles/descriptions from Shopify fields
- Canonical URLs, Open Graph, Twitter Cards
**Dependencies:** Sprint 46
**Acceptance Criteria:**
- Google Rich Results Test passes for Product pages
- No duplicate content signals
- Sitemap.xml includes all active pages
- Robots.txt correctly configured
**Complexity:** M
**Expected Outcome:** Search engine visibility optimized
**Critical Path:** No — but critical for organic traffic

---

### Sprint 50: Data Migration Plan + Content Population
**Goal:** Plan migration from current live theme and populate all content.
**Deliverables:**
- Migration checklist: current theme → new theme
- All section content populated from docs/07 copy
- Product metafields configured for PDP content
- Image assets uploaded to Shopify CDN
- Redirect map for any URL changes
**Dependencies:** Sprints 46–49 (theme complete and QA'd)
**Acceptance Criteria:**
- Every section has real content (no lorem ipsum)
- All product images uploaded at correct dimensions
- Redirect map covers all legacy URLs
- Rollback plan documented
**Complexity:** L
**Expected Outcome:** Theme ready for staging deployment
**Critical Path:** Yes — must be complete before launch prep

---

## PHASE H: LAUNCH PREPARATION (Sprints 51–56)

---

### Sprint 51: Staging Deployment
**Goal:** Deploy complete theme to Shopify staging/unpublished theme.
**Deliverables:**
- Theme uploaded as unpublished theme in Shopify admin
- All section settings configured
- Test orders placed successfully
- Payment gateway tested (test mode)
**Dependencies:** Sprint 50
**Acceptance Criteria:**
- Theme accessible via preview link
- All pages render correctly in Shopify preview
- Test checkout completes end-to-end
- Email notifications trigger correctly
**Complexity:** M
**Expected Outcome:** Stakeholder review possible on staging
**Critical Path:** Yes

---

### Sprint 52: Stakeholder Review + Feedback Round
**Goal:** Collect and address CEO feedback on staging theme.
**Deliverables:**
- Review session with CEO
- Feedback documented in planning/
- Priority fixes identified and categorized
- Approved/change-requested per section
**Dependencies:** Sprint 51
**Acceptance Criteria:**
- CEO has reviewed all pages on staging
- Feedback categorized: must-fix, nice-to-have, future
- Must-fix items ≤ 10 for launch
**Complexity:** S
**Expected Outcome:** Clear list of final changes before launch
**Critical Path:** Yes — CEO approval required

---

### Sprint 53: Feedback Implementation
**Goal:** Implement all must-fix items from stakeholder review.
**Deliverables:**
- All must-fix issues resolved
- Updated staging theme
- Visual diff of before/after for major changes
**Dependencies:** Sprint 52
**Acceptance Criteria:**
- All must-fix items resolved and verified
- No new bugs introduced
- CEO sign-off on fixes
**Complexity:** M (variable based on feedback)
**Expected Outcome:** Theme ready for final QA
**Critical Path:** Yes

---

### Sprint 54: Final QA Pass
**Goal:** Complete final quality assurance before go-live.
**Deliverables:**
- Full regression test (all pages, all breakpoints)
- Cross-browser final check (Chrome, Safari, Firefox, Edge)
- Real device testing (iPhone, Android)
- Analytics/tracking verification (GA4, Meta pixel)
**Dependencies:** Sprint 53
**Acceptance Criteria:**
- Zero P1 bugs
- All tracking fires correctly
- Performance scores maintained (≥ 70 Lighthouse)
- No visual regressions from feedback fixes
**Complexity:** M
**Expected Outcome:** Go/no-go decision ready
**Critical Path:** Yes

---

### Sprint 55: Launch Day — Theme Publish
**Goal:** Publish new theme as live store theme.
**Deliverables:**
- Theme published via Shopify admin
- DNS/redirects verified
- Real-time monitoring for first 4 hours
- Hotfix branch ready if critical issue found
**Dependencies:** Sprint 54 + CEO go decision
**Acceptance Criteria:**
- Theme is live at barreletics.com
- All pages loading correctly
- No 500 errors in Shopify logs
- Checkout functional with real payment
- Analytics receiving data
**Complexity:** S
**Expected Outcome:** New design live for customers
**Critical Path:** Yes — this is the goal

---

### Sprint 56: Post-Launch Monitoring + Documentation
**Goal:** Monitor launch metrics and close out project documentation.
**Deliverables:**
- 48-hour performance report (orders, conversion, speed)
- Any hotfixes applied
- Project retrospective documented
- Repository marked as PRODUCTION COMPLETE
- Handoff documentation for ongoing maintenance
**Dependencies:** Sprint 55
**Acceptance Criteria:**
- Conversion rate stable or improved vs pre-launch
- No critical bugs reported by customers
- All monitoring tools active (GA4, Shopify analytics)
- Repository README updated with final project status
**Complexity:** S
**Expected Outcome:** Project complete, store operating on new design
**Critical Path:** No — maintenance mode begins

---

## SUMMARY

| Phase | Sprints | Focus | Duration |
|-------|---------|-------|----------|
| A — ADR + Approval | 07–10 | Resolve conflicts, approve docs | Week 1 |
| B — Remediation | 11–15 | Fix 30 consistency findings | Week 1–2 |
| C — Shopify Foundation | 16–20 | Tokens, header, footer, base styles | Week 2 |
| D — PDP | 21–30 | Complete product page | Week 2–4 |
| E — Homepage | 31–40 | All homepage sections | Week 3–5 |
| F — Collection + Content | 41–45 | Collection, blog, static pages | Week 4–5 |
| G — Integration + QA | 46–50 | Testing, performance, migration | Week 5–6 |
| H — Launch | 51–56 | Deploy, review, go-live | Week 6 |

**Total Sprints:** 50 (Sprint 07–56)  
**Critical Path:** A → B(11–12) → C(16–20) → D(21–30) → E(31,40) → G(46,50) → H(51–55)
