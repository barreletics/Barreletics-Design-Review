# Engineering Backlog — Barreletics Shopify Implementation

**Date:** 2026-07-13  
**Status:** PLANNING — do not commit  
**Structure:** Epics → Features → Stories → Tasks  
**Total tasks:** 128

---

## EPIC 1: Design System Foundation

### Feature 1.1: Token Implementation

#### Story 1.1.1: Port CSS Variables to Shopify Theme

**TASK-001: Create settings_schema.json token definitions**
- Acceptance criteria:
  - All color tokens from docs/03 and docs/06 :root block are defined as Shopify theme settings
  - Token names match `--br-*` convention from design system
  - Default values match APPROVED docs (pending ADR-01 through ADR-07 resolution)
- Dependencies: ADR-01 resolved
- Priority: P0
- Complexity: M

**TASK-002: Create css-variables.liquid snippet**
- Acceptance criteria:
  - Outputs `:root {}` block with all design tokens mapped from theme settings
  - Included in theme.liquid `<head>`
  - Variables render correctly in browser dev tools
- Dependencies: TASK-001
- Priority: P0
- Complexity: S

**TASK-003: Create Tailwind/utility config (if used) or custom utility classes**
- Acceptance criteria:
  - Utility classes for spacing, color, and typography reference CSS variables
  - No hardcoded hex values in utility layer
- Dependencies: TASK-002
- Priority: P2
- Complexity: S

#### Story 1.1.2: Validate Token Consistency

**TASK-004: Audit all token values against docs/04 APPROVED spec**
- Acceptance criteria:
  - Every token in css-variables.liquid matches docs/04 + ADR resolutions
  - Zero hardcoded values that bypass the token system
  - Documented mapping table in code comments
- Dependencies: TASK-002, ADR-01 through ADR-07
- Priority: P0
- Complexity: S

### Feature 1.2: Typography System

#### Story 1.2.1: Configure Font Loading

**TASK-005: Set up Montserrat font loading via Shopify**
- Acceptance criteria:
  - Montserrat loaded via Google Fonts or self-hosted in assets/
  - Weights: 400, 500, 600, 700 loaded
  - `font-display: swap` set
- Dependencies: None
- Priority: P0
- Complexity: S

**TASK-006: Set up Oswald font loading**
- Acceptance criteria:
  - Oswald loaded for eyebrow/label use
  - Weights: 600, 700
  - `font-display: swap` set
- Dependencies: None
- Priority: P0
- Complexity: S

**TASK-007: Create typography token variables**
- Acceptance criteria:
  - `--t-heading`, `--t-body`, `--t-eyebrow`, `--t-label` defined per docs/03
  - Responsive type scale uses clamp() or media queries
  - Eyebrow letter-spacing matches ADR-04 decision
- Dependencies: TASK-002, ADR-04
- Priority: P0
- Complexity: M

#### Story 1.2.2: Set Up Responsive Breakpoints

**TASK-008: Define breakpoint system**
- Acceptance criteria:
  - Mobile: ≤767px, Tablet: 768–1023px, Desktop: ≥1024px
  - Breakpoints stored as CSS custom properties or SCSS variables
  - Documented in code header
- Dependencies: None
- Priority: P0
- Complexity: S

### Feature 1.3: Color System

#### Story 1.3.1: Implement Color Palette

**TASK-009: Define primary palette tokens**
- Acceptance criteria:
  - `--br-ink`, `--br-white`, `--br-bg`, `--br-alt-bg` match ADR-01 resolution
  - `--br-accent-coral`, `--br-accent-terracotta` defined
  - `--br-star-gold` matches ADR-07 resolution
- Dependencies: ADR-01, ADR-07
- Priority: P0
- Complexity: S

**TASK-010: Define semantic color tokens**
- Acceptance criteria:
  - `--br-text`, `--br-text-soft`, `--br-text-muted` match ADR-05 resolution
  - `--br-border`, `--br-surface` tokens defined
  - Semantic names map to palette primitives
- Dependencies: TASK-009, ADR-05
- Priority: P0
- Complexity: S

### Feature 1.4: Spacing System

**TASK-011: Define spacing scale**
- Acceptance criteria:
  - 4px base unit: 4, 8, 12, 16, 24, 32, 48, 64, 80, 120
  - CSS custom properties `--space-xs` through `--space-3xl`
  - Section padding follows docs/06 patterns (80px desktop, 48px mobile)
- Dependencies: TASK-002
- Priority: P1
- Complexity: S

### Feature 1.5: Animation System

**TASK-012: Define animation tokens**
- Acceptance criteria:
  - `--ease-default`, `--duration-fast`, `--duration-normal` defined
  - Hover transitions: 0.3s ease per docs/05 and docs/06
  - Scroll-triggered animations use Intersection Observer
- Dependencies: TASK-002
- Priority: P2
- Complexity: S

---

## EPIC 2: Global Components

### Feature 2.1: Header

**TASK-013: Build header section (sections/header.liquid)**
- Acceptance criteria:
  - Logo, nav links, cart icon, mobile hamburger present
  - Sticky behavior on scroll
  - HTML structure matches docs/04 header component
- Dependencies: TASK-002
- Priority: P0
- Complexity: M

**TASK-014: Create header settings schema**
- Acceptance criteria:
  - Logo image upload setting
  - Navigation menu picker
  - Announcement bar toggle + text
  - Background color / transparency options
- Dependencies: TASK-013
- Priority: P0
- Complexity: S

**TASK-015: Header mobile responsive**
- Acceptance criteria:
  - Hamburger menu triggers slide-out drawer at ≤767px
  - Touch-friendly tap targets (≥44px)
  - Nav links stack vertically in mobile drawer
- Dependencies: TASK-013
- Priority: P0
- Complexity: M

**TASK-016: Header accessibility**
- Acceptance criteria:
  - Skip-to-content link as first focusable element
  - `aria-expanded` on hamburger toggle
  - Keyboard navigation through all nav items
  - Focus trap in mobile drawer when open
- Dependencies: TASK-015
- Priority: P1
- Complexity: M

**TASK-017: Header QA**
- Acceptance criteria:
  - Renders correctly in Chrome, Safari, Firefox, Edge
  - Logo links to homepage
  - Cart icon shows badge count from cart.item_count
- Dependencies: TASK-013, TASK-015, TASK-016
- Priority: P1
- Complexity: S

### Feature 2.2: Footer

**TASK-018: Build footer section (sections/footer.liquid)**
- Acceptance criteria:
  - Newsletter signup form (Klaviyo integration point)
  - Navigation columns (Shop, About, Support)
  - Social links, copyright
  - HTML matches docs/04 footer component
- Dependencies: TASK-002
- Priority: P0
- Complexity: M

**TASK-019: Footer settings schema**
- Acceptance criteria:
  - Column headings and link lists configurable
  - Social media URL inputs
  - Newsletter heading/subtext editable
  - Copyright text editable
- Dependencies: TASK-018
- Priority: P0
- Complexity: S

**TASK-020: Footer mobile responsive**
- Acceptance criteria:
  - Columns stack on mobile
  - Accordion collapse for nav sections on small screens
  - Newsletter form full-width on mobile
- Dependencies: TASK-018
- Priority: P1
- Complexity: S

**TASK-021: Footer accessibility**
- Acceptance criteria:
  - All links have descriptive text (no "click here")
  - Social icons have `aria-label`
  - Newsletter form has proper label association
- Dependencies: TASK-018
- Priority: P1
- Complexity: S

### Feature 2.3: Announcement Ticker

**TASK-022: Build ticker section**
- Acceptance criteria:
  - Horizontal scrolling text with CSS animation
  - Configurable message (discount code, shipping threshold)
  - Dismissible with close button (session persistence)
- Dependencies: TASK-002
- Priority: P1
- Complexity: M

**TASK-023: Ticker settings schema**
- Acceptance criteria:
  - Message text, link URL, background color, text color configurable
  - Show/hide toggle
  - Animation speed control
- Dependencies: TASK-022
- Priority: P1
- Complexity: S

### Feature 2.4: Navigation

**TASK-024: Build mega-menu / dropdown navigation**
- Acceptance criteria:
  - Supports 2-level dropdown menus
  - Featured image slot for collection promos
  - Matches brand typography (Montserrat)
- Dependencies: TASK-013
- Priority: P1
- Complexity: L

**TASK-025: Navigation mobile drawer**
- Acceptance criteria:
  - Full-screen overlay on mobile
  - Accordion sub-menus
  - Close button + click-outside-to-close
  - Smooth enter/exit transitions
- Dependencies: TASK-024
- Priority: P1
- Complexity: M

### Feature 2.5: Cart Drawer

**TASK-026: Build cart drawer (Ajax cart)**
- Acceptance criteria:
  - Slide-out drawer from right side
  - Line items with image, title, variant, quantity, price
  - Quantity +/- controls with Ajax update
  - Free shipping progress bar ($150 threshold per ADR-02)
  - Checkout button
- Dependencies: TASK-002, ADR-02
- Priority: P0
- Complexity: L

**TASK-027: Cart drawer accessibility**
- Acceptance criteria:
  - Focus trap when open
  - `aria-live` region for quantity/total updates
  - ESC key closes drawer
  - Screen reader announces cart contents
- Dependencies: TASK-026
- Priority: P1
- Complexity: M

**TASK-028: Cart drawer mobile**
- Acceptance criteria:
  - Full-width on mobile
  - Scrollable line items
  - Fixed checkout button at bottom
  - Touch-friendly quantity controls
- Dependencies: TASK-026
- Priority: P0
- Complexity: S

---

## EPIC 3: Product Detail Page (PDP)

### Feature 3.1: Image Gallery

**TASK-029: Build PDP gallery section**
- Acceptance criteria:
  - Hero image with 8px border-radius (per docs/05)
  - Thumbnail strip below (horizontal scroll on mobile)
  - Click thumbnail to swap hero
  - Images lazy-loaded with Shopify image_url filters
- Dependencies: TASK-002
- Priority: P0
- Complexity: M

**TASK-030: Gallery mobile behavior**
- Acceptance criteria:
  - Horizontal swipe carousel on mobile
  - Dot indicators for current slide
  - Pinch-to-zoom on hero image
- Dependencies: TASK-029
- Priority: P0
- Complexity: M

**TASK-031: Gallery accessibility**
- Acceptance criteria:
  - Alt text from product.images[n].alt
  - Arrow key navigation between thumbnails
  - `aria-current` on active thumbnail
- Dependencies: TASK-029
- Priority: P1
- Complexity: S

### Feature 3.2: Buy Box

**TASK-032: Build buy box component**
- Acceptance criteria:
  - Product title, price (sale + compare-at), variant selector
  - Add-to-cart button (border-radius per ADR-03)
  - "Free shipping over $150" trust line
  - Matches docs/05 `.pdp-buy` structure
- Dependencies: TASK-002, ADR-02, ADR-03
- Priority: P0
- Complexity: L

**TASK-033: Buy box dynamic pricing**
- Acceptance criteria:
  - Price updates on variant change via JS
  - Compare-at price shows with strikethrough when present
  - "Save X%" badge when on sale
- Dependencies: TASK-032
- Priority: P0
- Complexity: M

**TASK-034: Buy box add-to-cart Ajax**
- Acceptance criteria:
  - Form submits via Fetch API (no page reload)
  - Cart drawer opens on successful add
  - Button shows loading state during request
  - Error state for out-of-stock / network error
- Dependencies: TASK-032, TASK-026
- Priority: P0
- Complexity: M

### Feature 3.3: Variant Picker

**TASK-035: Build size selector pills**
- Acceptance criteria:
  - Pill buttons for S/M/L (border-radius per ADR-03)
  - Active state with ink background
  - Disabled/sold-out state with strikethrough
  - Maps to Shopify variant options
- Dependencies: TASK-032, ADR-03
- Priority: P0
- Complexity: M

**TASK-036: Build color selector swatches**
- Acceptance criteria:
  - Circle swatches with actual color fill
  - Active state with border ring
  - Updates product image on color change
  - Variant availability recalculated on selection
- Dependencies: TASK-035
- Priority: P0
- Complexity: M

**TASK-037: Variant picker accessibility**
- Acceptance criteria:
  - Radio group semantics (`role="radiogroup"`)
  - `aria-checked` on selected variant
  - `aria-disabled` on sold-out variants
  - Keyboard arrow navigation between options
- Dependencies: TASK-035, TASK-036
- Priority: P1
- Complexity: S

### Feature 3.4: Reviews Section

**TASK-038: Integrate JudgeMe reviews widget**
- Acceptance criteria:
  - Star rating display using `--br-star-gold` (per ADR-07)
  - Review count shown
  - Review cards with configurable border-radius (per ADR-06)
  - Pagination or "load more"
- Dependencies: ADR-06, ADR-07
- Priority: P1
- Complexity: M

**TASK-039: JudgeMe review form**
- Acceptance criteria:
  - Star rating input
  - Text review + optional photo upload
  - Verification badge display
  - Form validates before submit
- Dependencies: TASK-038
- Priority: P1
- Complexity: M

**TASK-040: Reviews Schema.org markup**
- Acceptance criteria:
  - `AggregateRating` JSON-LD with ratingValue and reviewCount
  - Individual `Review` markup for visible reviews
  - Validates in Google Rich Results Test
- Dependencies: TASK-038
- Priority: P1
- Complexity: S

### Feature 3.5: Cross-Sell / You May Also Like

**TASK-041: Build cross-sell section**
- Acceptance criteria:
  - Horizontal product card row (3 desktop, 1.5 mobile with peek)
  - Uses Shopify product recommendations API
  - Product cards match docs/04 card component
- Dependencies: TASK-002
- Priority: P1
- Complexity: M

**TASK-042: Cross-sell mobile carousel**
- Acceptance criteria:
  - Swipeable on touch
  - Snap to card boundaries
  - Peek next card to indicate scrollability
- Dependencies: TASK-041
- Priority: P1
- Complexity: S

### Feature 3.6: FAQ Accordion

**TASK-043: Build FAQ accordion component**
- Acceptance criteria:
  - Expandable Q&A pairs with +/- toggle
  - Smooth height transition animation
  - Only one item open at a time (optional: configurable)
  - Content editable via section settings
- Dependencies: TASK-002
- Priority: P1
- Complexity: M

**TASK-044: FAQ Schema.org markup**
- Acceptance criteria:
  - `FAQPage` JSON-LD with all visible Q&A pairs
  - Validates in Google Rich Results Test
- Dependencies: TASK-043
- Priority: P1
- Complexity: S

**TASK-045: FAQ accessibility**
- Acceptance criteria:
  - `<details>/<summary>` or `aria-expanded` pattern
  - Enter/Space toggles open/close
  - Focus visible on active question
- Dependencies: TASK-043
- Priority: P1
- Complexity: S

### Feature 3.7: Trust Row

**TASK-046: Build trust badges row**
- Acceptance criteria:
  - Icons + text for: Free Shipping, Easy Returns, Secure Checkout
  - Horizontal layout (3-up on desktop, stack or scroll on mobile)
  - Icons from SVG sprite or inline SVG
- Dependencies: TASK-002
- Priority: P1
- Complexity: S

### Feature 3.8: Sock Math Section

**TASK-047: Build PDP sock math section**
- Acceptance criteria:
  - Annual cost comparison: Barreletics vs competitors
  - Animated counter or static comparison block
  - Copy from docs/09 pricing comparison data
  - Matches docs/05 sock math specification
- Dependencies: TASK-002
- Priority: P2
- Complexity: M

### Feature 3.9: PDP Schema.org / SEO

**TASK-048: Implement Product JSON-LD**
- Acceptance criteria:
  - `Product` schema with name, description, image, price, availability
  - `Offer` with priceCurrency USD
  - Includes `brand` and `sku`
  - Validates in Google Rich Results Test
- Dependencies: TASK-032
- Priority: P0
- Complexity: S

**TASK-049: PDP meta tags**
- Acceptance criteria:
  - `<title>`, `meta description`, `og:title`, `og:image`, `og:price:amount`
  - Canonical URL set
  - Proper `robots` tag
- Dependencies: None
- Priority: P0
- Complexity: S

### Feature 3.10: PDP Mobile Layout

**TASK-050: PDP mobile responsive layout**
- Acceptance criteria:
  - Gallery → Buy box → Reviews → Cross-sell → FAQ vertical stack
  - Sticky add-to-cart bar at bottom on mobile
  - All touch targets ≥44px
  - No horizontal scroll
- Dependencies: TASK-029 through TASK-049
- Priority: P0
- Complexity: M

---

## EPIC 4: Homepage

### Feature 4.1: Hero Section

**TASK-051: Build hero section**
- Acceptance criteria:
  - Full-width image/video background
  - Headline + subhead overlay
  - Primary CTA button
  - Matches docs/06 Section 01 specification
- Dependencies: TASK-002
- Priority: P0
- Complexity: M

**TASK-052: Hero settings schema**
- Acceptance criteria:
  - Image/video upload, headline, subtext, CTA text/link configurable
  - Desktop/mobile image variants
  - Text alignment and color options
- Dependencies: TASK-051
- Priority: P0
- Complexity: S

**TASK-053: Hero mobile**
- Acceptance criteria:
  - Image crops appropriately for portrait viewport
  - Text remains readable (proper contrast)
  - CTA is full-width on mobile
- Dependencies: TASK-051
- Priority: P0
- Complexity: S

### Feature 4.2: Pillar Strip

**TASK-054: Build pillar strip section**
- Acceptance criteria:
  - Horizontal row of 3–4 value props with icons
  - Matches docs/06 pillar strip specification
  - Auto-scroll ticker variant (optional)
- Dependencies: TASK-002
- Priority: P1
- Complexity: S

### Feature 4.3: 50/50 Splits (×3)

**TASK-055: Build 50/50 split section (reusable)**
- Acceptance criteria:
  - Image left/right + text content on opposite side
  - "Flip" setting to swap image/text sides
  - Eyebrow, heading, body, CTA fields
  - Matches docs/06 50/50 sections (Progress, Problems, Performance)
- Dependencies: TASK-002
- Priority: P0
- Complexity: M

**TASK-056: 50/50 split mobile**
- Acceptance criteria:
  - Stacks to image-on-top, text-below on mobile
  - Maintains readable text hierarchy
  - Image uses aspect-ratio container
- Dependencies: TASK-055
- Priority: P0
- Complexity: S

**TASK-057: 50/50 split settings schema**
- Acceptance criteria:
  - Image, eyebrow, heading, body, CTA (text + URL) configurable
  - Layout direction toggle (image left vs right)
  - Background color picker (white / alt-bg)
- Dependencies: TASK-055
- Priority: P0
- Complexity: S

### Feature 4.4: Product Grid

**TASK-058: Build product grid section**
- Acceptance criteria:
  - 2–4 column responsive grid of product cards
  - Product card: image, title, price, quick-add button
  - Collection picker in settings
  - Matches docs/04 product card component
- Dependencies: TASK-002
- Priority: P0
- Complexity: M

**TASK-059: Product card component**
- Acceptance criteria:
  - Hover state: image swap to secondary image
  - Sale badge when compare-at price exists
  - Quick-add triggers Ajax cart
  - Links to PDP
- Dependencies: TASK-058
- Priority: P0
- Complexity: M

**TASK-060: Product grid mobile**
- Acceptance criteria:
  - 2-column grid on mobile
  - Cards maintain aspect ratio
  - Touch-friendly quick-add
- Dependencies: TASK-058
- Priority: P0
- Complexity: S

### Feature 4.5: Sock Math (Homepage)

**TASK-061: Build homepage sock math section**
- Acceptance criteria:
  - Annual cost comparison visualization
  - Animated counters or bar chart
  - Copy sourced from docs/09
  - Matches docs/06 sock math section
- Dependencies: TASK-002
- Priority: P1
- Complexity: M

### Feature 4.6: Testimonial Section

**TASK-062: Build testimonial section**
- Acceptance criteria:
  - Customer quote with name, star rating
  - Carousel or grid of 3+ testimonials
  - Star color matches `--br-star-gold`
  - Configurable via settings blocks
- Dependencies: TASK-002, ADR-07
- Priority: P1
- Complexity: M

**TASK-063: Testimonial settings schema**
- Acceptance criteria:
  - Blocks for individual testimonials (quote, author, rating, image)
  - Section heading editable
  - Layout toggle (carousel vs grid)
- Dependencies: TASK-062
- Priority: P1
- Complexity: S

### Feature 4.7: Founder Section

**TASK-064: Build founder story section**
- Acceptance criteria:
  - Portrait image + founder bio text
  - Matches docs/06 founder section
  - Signature image optional
- Dependencies: TASK-002
- Priority: P1
- Complexity: S

### Feature 4.8: Disciplines Section

**TASK-065: Build disciplines section**
- Acceptance criteria:
  - Grid or carousel of discipline icons/images (CrossFit, Yoga, HIIT, etc.)
  - Each links to relevant collection or content
  - Matches docs/06 disciplines specification
- Dependencies: TASK-002
- Priority: P2
- Complexity: M

### Feature 4.9: Coperni Collaboration

**TASK-066: Build Coperni section**
- Acceptance criteria:
  - Split layout with collaboration imagery
  - CTA to Coperni product or collection
  - Conditional visibility (show/hide if product available)
- Dependencies: TASK-002
- Priority: P2
- Complexity: S

### Feature 4.10: Guarantee Section

**TASK-067: Build guarantee section**
- Acceptance criteria:
  - Bold guarantee statement (e.g., "100% Satisfaction")
  - Icon + supporting text
  - Matches docs/06 guarantee section
- Dependencies: TASK-002
- Priority: P1
- Complexity: S

### Feature 4.11: Newsletter Section

**TASK-068: Build newsletter signup section**
- Acceptance criteria:
  - Email input + submit button
  - Klaviyo form integration
  - Success/error state handling
  - SAVE15 discount code mention (per docs/09)
- Dependencies: TASK-002
- Priority: P1
- Complexity: M

**TASK-069: Newsletter accessibility**
- Acceptance criteria:
  - Label associated with input
  - Error messages announced to screen readers
  - Submit button has descriptive text
- Dependencies: TASK-068
- Priority: P1
- Complexity: S

### Feature 4.12: Homepage QA

**TASK-070: Homepage mobile responsive QA**
- Acceptance criteria:
  - All sections render correctly 320px–768px
  - No horizontal overflow
  - All images have appropriate aspect ratios
  - Text readable without zoom
- Dependencies: TASK-051 through TASK-069
- Priority: P0
- Complexity: M

**TASK-071: Homepage performance audit**
- Acceptance criteria:
  - LCP < 2.5s on mobile
  - CLS < 0.1
  - All images use responsive srcset
  - Lazy loading on below-fold sections
- Dependencies: TASK-070
- Priority: P1
- Complexity: M

---

## EPIC 5: Collection Page

### Feature 5.1: Collection Hero

**TASK-072: Build collection hero section**
- Acceptance criteria:
  - Collection title, description, optional banner image
  - Reads from collection.title, collection.description
  - Image fallback when no banner set
- Dependencies: TASK-002
- Priority: P0
- Complexity: S

### Feature 5.2: Sole-Type Chooser

**TASK-073: Build sole-type filter toggle**
- Acceptance criteria:
  - Toggle/pill buttons for sole type categories
  - Filters product grid without page reload (JS)
  - Uses Shopify tags or metafields for categorization
- Dependencies: TASK-002
- Priority: P1
- Complexity: M

### Feature 5.3: Filter Row

**TASK-074: Build filter/sort bar**
- Acceptance criteria:
  - Sort dropdown (Price low-high, high-low, Best selling, Newest)
  - Filter by: Size, Color, Price range
  - Uses Shopify Storefront Filtering API
  - Active filters shown as removable chips
- Dependencies: TASK-002
- Priority: P1
- Complexity: L

**TASK-075: Filter mobile drawer**
- Acceptance criteria:
  - Filters collapse into slide-up drawer on mobile
  - Apply/Clear buttons
  - Filter count badge on trigger button
- Dependencies: TASK-074
- Priority: P1
- Complexity: M

### Feature 5.4: Collection Product Grid

**TASK-076: Build collection product grid**
- Acceptance criteria:
  - 3-column desktop, 2-column mobile
  - Reuses product card component (TASK-059)
  - Pagination (infinite scroll or numbered pages)
  - Products per page configurable in settings
- Dependencies: TASK-059
- Priority: P0
- Complexity: M

**TASK-077: Collection grid empty state**
- Acceptance criteria:
  - Friendly message when filters return 0 results
  - "Clear filters" CTA
  - Suggestions for related collections
- Dependencies: TASK-076
- Priority: P2
- Complexity: S

### Feature 5.5: Editorial Breaks

**TASK-078: Build editorial break blocks**
- Acceptance criteria:
  - Full-width content blocks between product rows
  - Support image + text or video + text
  - Configurable position (after row N)
- Dependencies: TASK-076
- Priority: P2
- Complexity: M

---

## EPIC 6: Content Pages

### Feature 6.1: Article Template (6 Variants)

**TASK-079: Build base article template**
- Acceptance criteria:
  - Hero image, title, date, author
  - Rich text body with responsive images
  - Share buttons (social)
  - Related articles at bottom
- Dependencies: TASK-002
- Priority: P1
- Complexity: M

**TASK-080: Article template — FAQ variant**
- Acceptance criteria:
  - Inherits base article styles
  - FAQ accordion auto-rendered from FAQ content type
  - FAQPage Schema.org markup
- Dependencies: TASK-079, TASK-043
- Priority: P1
- Complexity: S

**TASK-081: Article template — Guide variant**
- Acceptance criteria:
  - Table of contents sidebar (sticky on desktop)
  - Section anchor links
  - "Time to read" estimate
- Dependencies: TASK-079
- Priority: P2
- Complexity: M

**TASK-082: Article template — Comparison variant**
- Acceptance criteria:
  - Side-by-side comparison table
  - Product card embeds
  - CTA to recommended product
- Dependencies: TASK-079
- Priority: P2
- Complexity: M

**TASK-083: Article template — Story variant**
- Acceptance criteria:
  - Full-bleed images between paragraphs
  - Pull quotes styled
  - No sidebar
- Dependencies: TASK-079
- Priority: P2
- Complexity: S

**TASK-084: Article template — Video variant**
- Acceptance criteria:
  - Embedded video hero (YouTube/Vimeo)
  - Transcript expandable below
  - Related videos section
- Dependencies: TASK-079
- Priority: P3
- Complexity: M

### Feature 6.2: Blog Index

**TASK-085: Build blog index template**
- Acceptance criteria:
  - Grid of article cards (image, title, excerpt, date)
  - Category filtering by blog tags
  - Pagination
  - Featured post pinned at top
- Dependencies: TASK-079
- Priority: P1
- Complexity: M

### Feature 6.3: FAQ Page

**TASK-086: Build standalone FAQ page**
- Acceptance criteria:
  - Category-grouped FAQ sections
  - Search/filter within FAQs
  - Reuses accordion component (TASK-043)
  - FAQPage Schema.org on full page
- Dependencies: TASK-043
- Priority: P1
- Complexity: M

### Feature 6.4: About Page

**TASK-087: Build About page template**
- Acceptance criteria:
  - Founder story section (reuses TASK-064 component)
  - Brand values section
  - Timeline or milestones
  - Team/founder photo
- Dependencies: TASK-002
- Priority: P2
- Complexity: M

---

## EPIC 7: Integration

### Feature 7.1: JudgeMe Reviews

**TASK-088: Install and configure JudgeMe app**
- Acceptance criteria:
  - App installed on dev store
  - Review widget renders on PDP
  - Star rating shows in collection product cards
  - Email review request flow configured
- Dependencies: TASK-038
- Priority: P0
- Complexity: M

**TASK-089: JudgeMe style overrides**
- Acceptance criteria:
  - Star color matches `--br-star-gold` token
  - Review card styling matches brand (radius per ADR-06)
  - Font family overridden to Montserrat
  - No JudgeMe branding visible
- Dependencies: TASK-088, ADR-06, ADR-07
- Priority: P1
- Complexity: S

### Feature 7.2: Juicer Social Feed

**TASK-090: Integrate Juicer social feed**
- Acceptance criteria:
  - Instagram feed grid renders on homepage or dedicated section
  - Responsive grid (4 desktop, 2 mobile)
  - Linked to brand Instagram account
  - Custom CSS to match brand design
- Dependencies: TASK-002
- Priority: P2
- Complexity: M

### Feature 7.3: Shop Pay

**TASK-091: Enable and configure Shop Pay**
- Acceptance criteria:
  - Shop Pay button appears on PDP and cart
  - Express checkout enabled
  - Shop Pay Installments configured (if eligible)
- Dependencies: TASK-032
- Priority: P0
- Complexity: S

### Feature 7.4: Klaviyo

**TASK-092: Install Klaviyo Shopify integration**
- Acceptance criteria:
  - Klaviyo app installed and connected
  - On-site tracking script in theme.liquid
  - Newsletter form posts to Klaviyo list
  - Welcome flow triggered on signup
- Dependencies: TASK-068
- Priority: P1
- Complexity: M

**TASK-093: Klaviyo event tracking**
- Acceptance criteria:
  - Viewed Product, Added to Cart, Started Checkout events fire
  - Events include product data (title, price, variant, image URL)
  - Events visible in Klaviyo activity log
- Dependencies: TASK-092
- Priority: P1
- Complexity: M

### Feature 7.5: GA4

**TASK-094: Implement GA4 via Google Tag Manager**
- Acceptance criteria:
  - GTM container snippet in theme.liquid
  - GA4 configuration tag with property 300437005
  - Enhanced ecommerce data layer events
- Dependencies: None
- Priority: P0
- Complexity: M

**TASK-095: GA4 ecommerce event data layer**
- Acceptance criteria:
  - `view_item` on PDP load
  - `add_to_cart` on add-to-cart
  - `view_item_list` on collection pages
  - `begin_checkout` on checkout start
  - `purchase` on order confirmation
  - All events include items array with id, name, price, quantity
- Dependencies: TASK-094
- Priority: P0
- Complexity: L

**TASK-096: GA4 event validation**
- Acceptance criteria:
  - All events visible in GA4 DebugView
  - No duplicate events
  - Revenue data matches Shopify orders
  - UTM parameters tracked correctly
- Dependencies: TASK-095
- Priority: P0
- Complexity: M

---

## EPIC 8: Quality & Launch

### Feature 8.1: Performance Optimization

**TASK-097: Image optimization audit**
- Acceptance criteria:
  - All images use Shopify CDN with responsive srcset
  - WebP format served where supported
  - No images > 200KB after optimization
  - Lazy loading on all below-fold images
- Dependencies: All section builds complete
- Priority: P0
- Complexity: M

**TASK-098: CSS optimization**
- Acceptance criteria:
  - Critical CSS inlined in `<head>`
  - No unused CSS > 10KB
  - CSS minified in production
  - No render-blocking stylesheets
- Dependencies: All section builds complete
- Priority: P1
- Complexity: M

**TASK-099: JavaScript optimization**
- Acceptance criteria:
  - JS deferred or async loaded
  - No blocking scripts in `<head>` (except critical)
  - Bundle size < 100KB (excluding third-party)
  - Third-party scripts loaded after first interaction
- Dependencies: All section builds complete
- Priority: P1
- Complexity: M

**TASK-100: Core Web Vitals audit**
- Acceptance criteria:
  - LCP < 2.5s on homepage and PDP (mobile 4G)
  - FID/INP < 200ms
  - CLS < 0.1
  - All pages pass PageSpeed Insights mobile "Good"
- Dependencies: TASK-097, TASK-098, TASK-099
- Priority: P0
- Complexity: L

### Feature 8.2: Accessibility Audit

**TASK-101: WCAG 2.1 AA automated audit**
- Acceptance criteria:
  - Run axe-core on all page templates
  - Zero critical/serious violations
  - All images have alt text
  - Color contrast meets 4.5:1 minimum
- Dependencies: All section builds complete
- Priority: P0
- Complexity: M

**TASK-102: Keyboard navigation audit**
- Acceptance criteria:
  - All interactive elements reachable via Tab
  - Focus indicators visible on all focusable elements
  - No keyboard traps (except intended modals with ESC escape)
  - Skip links functional
- Dependencies: TASK-101
- Priority: P0
- Complexity: M

**TASK-103: Screen reader testing**
- Acceptance criteria:
  - Tested with VoiceOver (macOS) or NVDA
  - Landmark regions defined (header, main, footer, nav)
  - Form inputs have associated labels
  - Dynamic content changes announced
- Dependencies: TASK-102
- Priority: P1
- Complexity: M

### Feature 8.3: SEO Implementation

**TASK-104: Technical SEO setup**
- Acceptance criteria:
  - XML sitemap generated (Shopify auto or custom)
  - robots.txt configured
  - Canonical URLs on all pages
  - Hreflang tags if multilingual (N/A for launch)
- Dependencies: None
- Priority: P0
- Complexity: S

**TASK-105: Structured data validation**
- Acceptance criteria:
  - Product, FAQPage, AggregateRating, BreadcrumbList schemas present
  - All pass Google Rich Results Test
  - No errors in Search Console
- Dependencies: TASK-048, TASK-044, TASK-040
- Priority: P0
- Complexity: S

**TASK-106: Meta tag audit**
- Acceptance criteria:
  - Every template has unique `<title>` and `<meta description>`
  - OG tags on all pages (title, description, image)
  - Twitter card tags on all pages
  - No duplicate meta tags
- Dependencies: All templates complete
- Priority: P0
- Complexity: S

**TASK-107: Internal linking structure**
- Acceptance criteria:
  - Breadcrumbs on PDP and collection pages
  - Related products link to PDPs
  - Blog articles link to products where relevant
  - Footer contains key page links
- Dependencies: All templates complete
- Priority: P1
- Complexity: S

### Feature 8.4: Migration

**TASK-108: Content migration from current theme**
- Acceptance criteria:
  - All products, collections, pages, blog posts preserved
  - No broken URLs (301 redirects for changed paths)
  - Customer accounts and order history unaffected
  - Navigation menus migrated
- Dependencies: All templates complete
- Priority: P0
- Complexity: L

**TASK-109: URL redirect mapping**
- Acceptance criteria:
  - Old URL → new URL mapping document created
  - 301 redirects implemented in Shopify for all changed paths
  - Verified: no 404s for previously indexed pages
- Dependencies: TASK-108
- Priority: P0
- Complexity: M

**TASK-110: Asset migration**
- Acceptance criteria:
  - All product images in Shopify CDN
  - Custom page images uploaded to Files
  - No broken image references
- Dependencies: TASK-108
- Priority: P0
- Complexity: M

### Feature 8.5: Launch

**TASK-111: Pre-launch checklist**
- Acceptance criteria:
  - All P0 tasks complete and verified
  - Payment gateway tested with test orders
  - Shipping rates configured and tested
  - Tax settings verified
  - Email notifications tested (order confirmation, shipping, etc.)
- Dependencies: All P0 tasks
- Priority: P0
- Complexity: M

**TASK-112: DNS and domain configuration**
- Acceptance criteria:
  - barreletics.com pointed to Shopify
  - SSL certificate active
  - www redirect configured
  - Email DNS records (MX, SPF, DKIM) preserved
- Dependencies: TASK-111
- Priority: P0
- Complexity: S

**TASK-113: Theme publish and verification**
- Acceptance criteria:
  - Development theme published as live
  - All pages load correctly on production domain
  - Google Search Console revalidated
  - GA4 receiving production data
- Dependencies: TASK-112
- Priority: P0
- Complexity: S

**TASK-114: Post-launch monitoring (24h)**
- Acceptance criteria:
  - GA4 real-time shows sessions
  - No 5xx errors in Shopify admin
  - Checkout flow tested on production
  - Core Web Vitals stable in field data
- Dependencies: TASK-113
- Priority: P0
- Complexity: S

---

## SUPPLEMENTARY TASKS

### Cross-Cutting Concerns

**TASK-115: Create Shopify theme directory structure**
- Acceptance criteria:
  - Standard Shopify 2.0 directory: layout/, templates/, sections/, snippets/, assets/, config/, locales/
  - theme.liquid with CSS variables snippet included
  - Blank templates for product, collection, page, blog, article, index
- Dependencies: None
- Priority: P0
- Complexity: S

**TASK-116: Configure theme settings_schema.json**
- Acceptance criteria:
  - Brand settings group (logo, colors, fonts)
  - Social media settings group
  - Cart settings group (free shipping threshold)
  - Footer settings group
- Dependencies: TASK-001
- Priority: P0
- Complexity: M

**TASK-117: Set up Shopify development store**
- Acceptance criteria:
  - Dev store created with product data from docs/09
  - Test products with all variants (S/M/L × colors)
  - Collections created (Grippy Shoes, Coperni, etc.)
  - Test customer accounts
- Dependencies: None
- Priority: P0
- Complexity: M

**TASK-118: Create reusable button snippet**
- Acceptance criteria:
  - `snippets/button.liquid` with primary, secondary, outline variants
  - Border-radius from design token (per ADR-03)
  - Hover state transitions per docs/05
  - Accepts: text, url, style, size parameters
- Dependencies: TASK-002, ADR-03
- Priority: P0
- Complexity: S

**TASK-119: Create reusable section-wrapper snippet**
- Acceptance criteria:
  - Consistent section padding (80px desktop, 48px mobile)
  - Background color option (white, alt-bg, ink)
  - Max-width container (1200px centered)
- Dependencies: TASK-002
- Priority: P0
- Complexity: S

**TASK-120: Create responsive image snippet**
- Acceptance criteria:
  - Uses Shopify `image_url` with width parameter
  - Generates srcset for 400, 600, 800, 1200, 1600px
  - Lazy loading by default (eager option for above-fold)
  - Proper width/height attributes for CLS prevention
- Dependencies: None
- Priority: P0
- Complexity: S

**TASK-121: 404 page template**
- Acceptance criteria:
  - On-brand 404 page with helpful navigation
  - Search bar
  - Links to popular collections
  - Matches brand typography and colors
- Dependencies: TASK-002
- Priority: P2
- Complexity: S

**TASK-122: Password page template**
- Acceptance criteria:
  - Branded password page for pre-launch
  - Email capture form (Klaviyo integration)
  - Brand messaging / teaser content
- Dependencies: TASK-002
- Priority: P2
- Complexity: S

**TASK-123: Cart page template (fallback)**
- Acceptance criteria:
  - Full cart page as fallback when JS disabled
  - Line items, quantity update, checkout button
  - Free shipping progress bar
  - Matches cart drawer styling
- Dependencies: TASK-026
- Priority: P1
- Complexity: M

**TASK-124: Search results page**
- Acceptance criteria:
  - Uses Shopify predictive search API
  - Product results in grid format (reuses product card)
  - Page/article results in list format
  - "No results" state with suggestions
- Dependencies: TASK-059
- Priority: P1
- Complexity: M

**TASK-125: Breadcrumb component**
- Acceptance criteria:
  - Home > Collection > Product trail
  - BreadcrumbList Schema.org markup
  - Styled with brand typography
  - Hidden on homepage
- Dependencies: TASK-002
- Priority: P1
- Complexity: S

**TASK-126: Social sharing component**
- Acceptance criteria:
  - Share buttons for Facebook, Twitter/X, Pinterest, Email
  - Uses native share API on mobile (with fallback)
  - No third-party tracking scripts
  - Copy-link option
- Dependencies: None
- Priority: P2
- Complexity: S

**TASK-127: Back-to-top button**
- Acceptance criteria:
  - Appears after scrolling 500px
  - Smooth scroll to top
  - Accessible (aria-label, keyboard activatable)
  - Styled to match brand
- Dependencies: TASK-002
- Priority: P3
- Complexity: S

**TASK-128: Cookie consent banner**
- Acceptance criteria:
  - GDPR/CCPA compliant banner
  - Blocks analytics scripts until consent
  - Remembers preference in localStorage
  - Matches brand styling
- Dependencies: TASK-094
- Priority: P1
- Complexity: M

---

## SUMMARY

| Epic | Tasks | P0 | P1 | P2 | P3 |
|------|-------|----|----|----|----|
| 1: Design System Foundation | 12 | 8 | 1 | 3 | 0 |
| 2: Global Components | 16 | 7 | 8 | 0 | 1 |
| 3: PDP | 22 | 10 | 10 | 1 | 1 |
| 4: Homepage | 21 | 9 | 9 | 2 | 1 |
| 5: Collection | 7 | 2 | 3 | 2 | 0 |
| 6: Content Pages | 9 | 0 | 4 | 4 | 1 |
| 7: Integration | 9 | 4 | 4 | 1 | 0 |
| 8: Quality & Launch | 18 | 13 | 4 | 0 | 1 |
| Supplementary | 14 | 6 | 4 | 3 | 1 |
| **TOTAL** | **128** | **59** | **47** | **16** | **6** |

### Blocked Tasks (require ADR decisions)
- TASK-001, TASK-004, TASK-009, TASK-010: ADR-01 (color palette)
- TASK-007: ADR-04 (eyebrow letter-spacing)
- TASK-010: ADR-05 (text color)
- TASK-032, TASK-035, TASK-118: ADR-03 (button border-radius)
- TASK-026: ADR-02 (free shipping threshold)
- TASK-038, TASK-089: ADR-06 (review card radius), ADR-07 (star color)

### Recommended Build Order
1. TASK-115 → TASK-117 (scaffolding + dev store)
2. TASK-001 → TASK-012 (design system tokens)
3. TASK-013 → TASK-028 (global components)
4. TASK-029 → TASK-050 (PDP)
5. TASK-051 → TASK-071 (Homepage)
6. TASK-072 → TASK-078 (Collection)
7. TASK-079 → TASK-087 (Content pages)
8. TASK-088 → TASK-096 (Integrations)
9. TASK-097 → TASK-114 (QA + Launch)

---

**END OF BACKLOG**
