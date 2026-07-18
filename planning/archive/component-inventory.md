# Component Inventory

**Status:** INVENTORY  
**Source:** `docs/04-COMPONENT-LIBRARY.md` (authoritative), supplemented by `docs/05-PDP-ARCHITECTURE.md` and `docs/06-HOMEPAGE-ARCHITECTURE.md`  
**Last Updated:** 2026-07-13

---

## 1. Ticker Bar

**Purpose:** Highlight promotional messages, shipping info, and social proof at the top of every page.

**Inputs:**
- Array of slide messages (currently 3: SAVE15 code, Made in USA, 1,000+ instructors)
- Rotation interval (4s)
- Transition duration (320ms)

**Outputs:**
- Full-width bar with auto-rotating text slides
- Opacity crossfade between slides

**States:**
- Default: auto-rotating
- Hover: paused (rotation freezes)
- Reduced motion: final slide visible, no animation

**Variants:** None documented. Same behavior across all pages.

**Dependencies:** None. Standalone component.

**Responsive Behavior:**
- Mobile: full width, same behavior
- Desktop: full width, same behavior

**Accessibility:**
- Must respect `@media (prefers-reduced-motion: no-preference)` — final state visible without animation
- Content must be readable without JavaScript (fallback to first slide)

**Shopify Implementation Notes:**
- Section: dedicated ticker section, always first in page template
- Implementation file: `ticker.js`
- Content should be editable via section settings (slide text, promo code, interval)

**Reuse Opportunities:**
- Used on every page (Home, PDP, Collection, Article)
- Could be extended for sale/event-specific messaging via metafields

---

## 2. Header / Navigation

**Purpose:** Primary site navigation, logo display, and cart access.

**Inputs:**
- Logo image/text
- Navigation links array (Grippy Footwear, Apparel, Collaborations, Journal, About Us)
- Cart item count (integer)
- Scroll position (for sticky behavior)

**Outputs:**
- Desktop: horizontal nav bar with centered logo, category links left, account/cart right
- Mobile: hamburger menu left, centered logo, cart icon right
- Sticky header with hairline on scroll

**States:**
- Default (top of page): transparent background, no bottom border
- Scrolled (> 8px): white background, 1px bottom hairline (`var(--br-line)`)
- Cart empty: no badge
- Cart has items: coral dot badge (`var(--br-accent)`) on cart icon
- Mobile menu open: drawer/modal visible
- Mobile menu closed: hamburger icon visible

**Variants:**
- Desktop layout (horizontal nav)
- Mobile layout (hamburger + drawer)

**Dependencies:**
- Cart state (Shopify cart API or JS cart object)

**Responsive Behavior:**
- Mobile (< 768px): hamburger replaces horizontal nav, logo centered
- Desktop (≥ 768px): full horizontal navigation

**Accessibility:**
- Keyboard navigable (Tab through links)
- Hamburger menu: opens on click, closes on selection or Escape
- Cart badge: not color-only (count or aria-label needed)
- `aria-expanded` on hamburger toggle
- Focus trap inside mobile menu when open

**Shopify Implementation Notes:**
- Section: `header` section (typically in `layout/theme.liquid`)
- Nav links from `linklists` or section settings
- Cart count from `cart.item_count`
- Sticky behavior: `position: fixed; top: 0; z-index: 40`
- Source: integrated in `/sections/hero.html`

**Reuse Opportunities:**
- Global — appears on every page
- Mobile hamburger currently hidden — needs implementation

---

## 3. Hero Section

**Purpose:** Full-viewport brand statement with rotating eyebrow messaging.

**Inputs:**
- Background image URL (e.g., `barreletics.com/cdn/shop/files/IMG_2917.jpg`)
- H1 headline text
- Eyebrow rotation messages (5 messages, 3.5s cycle)
- Primary CTA (text + URL)
- Secondary CTA (text + anchor or URL)

**Outputs:**
- Full-bleed background image
- Centered text overlay: rotating eyebrow → headline → CTA buttons
- Opacity crossfade between eyebrow messages

**States:**
- Default: eyebrow rotating, hero image visible
- Reduced motion: static eyebrow (first or last message)
- Loading: image placeholder until loaded

**Variants:**
- Home hero (5-message eyebrow rotation, 2 CTAs)
- Collection hero ("Your body moves…" — different copy, same layout)
- PDP hero is a different component (gallery + buy box)

**Dependencies:**
- Button component (Primary + Secondary)

**Responsive Behavior:**
- Mobile: stack vertically, reduce image height, maintain full-bleed width, font sizes via `clamp()`
- Desktop: full viewport width and height, centered layout

**Accessibility:**
- Background image needs meaningful `alt` on `<img>` or `role="img"` + `aria-label` on container
- CTAs must be keyboard-focusable
- Eyebrow rotation must not auto-play if reduced motion preferred
- Sufficient color contrast on text overlay

**Shopify Implementation Notes:**
- Section: dedicated hero section
- Settings: image picker, headline text, eyebrow messages (textarea or repeater blocks), CTA text/URL pairs
- Source: `/sections/hero.html`

**Reuse Opportunities:**
- Home page, Collection page (with different content)
- Could be adapted for landing pages or campaign pages

---

## 4. Pillar Strip

**Purpose:** Horizontal display of 6 product attributes/benefits.

**Inputs:**
- 6 pillar items, each with: icon, label, short description
- Background color (`var(--alt-bg)`, `#f9f7f2`)

**Outputs:**
- Horizontal card row with icon + label + description per pillar
- Equal-width columns

**States:**
- Default: static display
- No interactive states documented

**Variants:** None — same 6 pillars on all pages.

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: stack vertically or 2-column grid
- Desktop: 6-column grid, full width

**Accessibility:**
- Icons need `aria-hidden="true"` if decorative, or `alt` text if informative
- Text must be readable at mobile sizes

**Shopify Implementation Notes:**
- Section: dedicated pillar-strip section
- Blocks: 6 pillar blocks, each with icon, label, description settings
- Placement: after hero on all pages (Home, PDP, Collection)

**Reuse Opportunities:**
- Home (after hero), PDP (after gallery), Collection (after hero)
- Content is the same across all pages currently — could be customized per collection via metafields

---

## 5. 50/50 Split

**Purpose:** Side-by-side image + copy editorial section for credibility and proof.

**Inputs:**
- Image or video URL
- Eyebrow text (optional)
- Headline text
- Body copy
- Trusted line + star rating (optional)
- Layout direction (image-left/copy-right or reversed)

**Outputs:**
- Two equal-width columns: one media, one copy
- Optional star rating and trusted line

**States:**
- Default: static layout
- Video variant: video plays on hover/interaction
- No hover states on the section itself

**Variants:**
- Split 1 — "Never slip in chair pose" (image left, copy right, with trusted line)
- Split 2 — "Progress, built from the ground up" (copy left, image right — reversed)
- Split 3 — "Never loses grip" (video, with trusted line)
- PDP Split — "Safely push harder…" (fabric/construction)
- Collection Split — "The Pilates sock era…"

**Dependencies:**
- Star rating sub-component
- Trusted line sub-component ("Trusted by 1,000's of instructors & studios")

**Responsive Behavior:**
- Mobile: stack vertically, image top or bottom, `height: auto`
- Desktop: side-by-side 50/50, fixed `height: 420px`, `overflow: hidden`

**Accessibility:**
- Images need descriptive `alt` text
- Video needs captions or transcript
- Sufficient contrast on text overlay areas

**Shopify Implementation Notes:**
- Section: split-section with direction setting (normal/reversed)
- Settings: image/video picker, headline, body, show-trusted-line toggle
- **CRITICAL:** 50/50 split CSS proportions are CANONICAL — do NOT change sizing (per Research Bible and Component Library)
- Source: `/sections/split-section.html`, `split-section2.html`, `split-section3.html`

**Reuse Opportunities:**
- Home (3 instances), PDP (1), Collection (1)
- Flexible enough for any image + copy pairing (about page, landing pages)

---

## 6. Product Card (Variant Card)

**Purpose:** Display a single product variant with image, name, price, and quick-add.

**Inputs:**
- Product image URL
- Color/variant name
- Price (formatted)
- Product variant ID (for add-to-cart)

**Outputs:**
- Card with image, color name, price, Quick Add button

**States:**
- Default: static card
- Hover: image scales 1.02x (320ms ease-out), caption underline draws in, button becomes interactive
- Active/click: add-to-cart action
- Loading: spinner or disabled state during cart add
- Sold out: not explicitly documented — needs definition

**Variants:** None — each color is its own card (no swatches on card).

**Dependencies:**
- Button component (Primary — Quick Add)
- Cart API (for add-to-cart)
- Product Grid parent (provides tab context: Closed Sole / Open Sole, Size M/L)

**Responsive Behavior:**
- Mobile: full-width cards, single column
- Desktop: 4-column grid (or configured per page)

**Accessibility:**
- Image alt text required
- Quick Add button must be keyboard-focusable
- Price must not rely on color alone to indicate sale
- Focus indicator on hover/focus

**Shopify Implementation Notes:**
- Snippet: reusable product-card snippet
- Data: product variant object (title, price, featured_image, variant_id)
- Tab filtering (Closed/Open Sole) at grid level, not per-card
- Size selection at grid level
- **Rule:** NEVER use swatches on individual card — one color per card
- Add to cart from homepage (no PDP redirect required)

**Reuse Opportunities:**
- Home product grid, Collection page, "Pairs with your kit" PDP rail
- Any cross-sell or upsell context

---

## 7. Product Grid

**Purpose:** Display a collection of product cards in a responsive grid.

**Inputs:**
- Array of product objects
- Column count (3–4)
- Filter tabs (Closed Sole / Open Sole — at grid level)
- Size selector (M/L — at grid level)
- Grid gap (`28px`)

**Outputs:**
- Multi-column grid of Product Cards
- Tab bar for sole-type filtering
- Size selector

**States:**
- Default: all products shown (or filtered by active tab)
- Tab active: one sole type selected
- Size selected: M or L active
- Empty: no products match filter (needs empty state design)

**Variants:**
- Home product grid (4 cards)
- Collection variants grid (all products, filter tabs)
- "Pairs with your kit" rail (PDP, subset)
- Range display (3-column at 64px padding)

**Dependencies:**
- Product Card component
- Button component (tab styling)

**Responsive Behavior:**
- Mobile: 1–2 column stack
- Desktop: 3–4 column grid, 28px gap

**Accessibility:**
- Tab controls: `role="tablist"`, `role="tab"`, `aria-selected`
- Grid: semantic list or grid role
- Announce filter changes to screen readers

**Shopify Implementation Notes:**
- Section: product-grid section with collection reference
- Blocks: product cards rendered from collection products
- Settings: columns count, show tabs toggle, collection picker
- Source: `/sections/range.html`

**Reuse Opportunities:**
- Home, Collection, PDP (product rail), search results
- Any page needing product display

---

## 8. Sock Math (Comparison Component)

**Purpose:** Cost-of-ownership comparison between grip socks and Barreletics.

**Inputs:**
- Sock data (price $336/year, stats for grip lifespan, pairs, slippage, grip longevity)
- Barreletics data (price $74, stats)
- Benefit grid items (6 cells)
- CTA button

**Outputs:**
- Dark section with eyebrow + headline
- Two comparison cards side-by-side
- 6-cell benefit grid below
- Centered CTA button

**States:**
- Default: static display
- No interactive states documented

**Variants:**
- Home version (full, 6 benefit cells, "Stop replacing. Start performing.")
- PDP version (condensed, reduced height, "One pair. Done.", includes "double failure" concept)

**Dependencies:**
- Button component (Primary CTA)
- Benefit Grid (6 cells below cards, reused concept)

**Responsive Behavior:**
- Mobile: stack cards vertically, benefit grid to 1–2 columns
- Desktop: 2-column side-by-side cards, multi-column benefit grid

**Accessibility:**
- Dark bg requires high contrast white text (check WCAG)
- Comparison data should be in a structured table or definition list for screen readers
- Strikethrough price needs `aria-label` ("was $336") or `<del>` element

**Shopify Implementation Notes:**
- Section: sock-math section with editable prices, stats, benefit items
- Blocks: comparison card blocks (sock vs Barreletics), benefit blocks
- Content heavily text-based — all should be editable in theme customizer
- Source: `/sections/sock-math.html`

**Reuse Opportunities:**
- Home page and PDP
- Could be adapted for other comparison contexts (e.g., vs. barefoot, vs. competitor shoes)

---

## 9. Benefit Grid

**Purpose:** Scannable grid of product advantages with optional icons.

**Inputs:**
- 3–6 benefit items, each with: optional icon, title, description (1–2 lines)

**Outputs:**
- Multi-column grid of benefit cards

**States:**
- Default: static display
- No interactive states documented

**Variants:**
- Home Sock Math variant (6 cells, dark bg, white text): 360° traction, Second-skin fit, Reformer-ready, Rinse & reuse, No latex/silicone, Barefoot-inspired
- PDP variant (6 cards): Reformer-ready, No twist, Sweat-ready, Rinse & reuse, Skin-safe, Barefoot feel
- Collection variant (3 cards): Reformer-ready, Two builds (closed/open), Rinse & reuse

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: stack or 2-column
- Desktop: multi-column grid (3 or 6 depending on variant)

**Accessibility:**
- Icons: `aria-hidden="true"` if decorative
- Text must maintain readable contrast
- Grid items should use semantic list markup

**Shopify Implementation Notes:**
- Section: benefit-grid section with block repeater
- Blocks: benefit items (icon picker, title, description)
- Settings: columns, background color, text color
- PDP benefits grid: `repeat(3, 1fr)` with `40px` gap

**Reuse Opportunities:**
- Home (within Sock Math), PDP (standalone section), Collection (standalone)
- Any feature-highlight context
- **Rule:** only one benefit grid per page section

---

## 10. PDP Accordion (Specs/FAQ)

**Purpose:** Collapsible sections for product details (Description, Size & Fit, Care, Returns).

**Inputs:**
- Array of accordion items, each with: trigger label, body content (HTML)

**Outputs:**
- Vertically stacked expandable sections
- Chevron/arrow indicator per item

**States:**
- Closed (default for all except optionally the first)
- Open: content visible, chevron rotated
- Transition: 200ms height animation
- **Rule:** only one section open at a time (accordion behavior, not independent toggles)

**Variants:**
- PDP specs accordion (Description, Size & Fit, Care, Returns)
- FAQ accordion (general Q&A items) — same component, different content

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: full width, touch-friendly headers (44px min tap target)
- Desktop: constrained width (max-width `760px` for FAQ variant)

**Accessibility:**
- `aria-expanded` on trigger buttons
- `aria-controls` linking trigger to panel
- `role="button"` on triggers (or use `<button>`)
- Keyboard: Enter/Space to toggle, focus visible
- Content inside panel must be focusable when expanded

**Shopify Implementation Notes:**
- Snippet: reusable accordion snippet
- PDP: rendered as product tabs/collapsible metafields
- FAQ: section with block repeater (question/answer pairs)
- PDP CSS: `.pdp-faq__trigger` / `.pdp-faq__body[data-open="true"]`

**Reuse Opportunities:**
- PDP (product details), FAQ section on any page
- About page, policy pages, any expandable content

---

## 11. Reviews Section

**Purpose:** Display customer testimonials and star ratings.

**Inputs:**
- Array of review objects (star rating, customer name, review text, verified badge, optional image)
- Reviews per page (6)
- Total review count

**Outputs:**
- Grid of review cards
- Load More button (pagination)

**States:**
- Default: 6 reviews visible
- Load More clicked: next 6 appended
- All loaded: Load More button hidden
- Loading: spinner during fetch
- Empty: no reviews (needs design — not documented)

**Variants:**
- Home reviews (6 curated, 2–3 column grid)
- PDP reviews (Judge.me integration, 3-column grid with images)

**Dependencies:**
- Star rating sub-component
- Load More button (Secondary button style)
- Review Card (image + content + stars + author)

**Responsive Behavior:**
- Mobile: single column, full-width cards
- Desktop: 2–3 column grid

**Accessibility:**
- Star rating: not color-only (numeric `aria-label` like "5 out of 5 stars")
- Review text: readable contrast
- Load More: announce new content to screen readers (`aria-live` region)

**Shopify Implementation Notes:**
- Section: reviews section, likely integrating Judge.me app
- Home: curated reviews via metafields or hardcoded
- PDP: dynamic from Judge.me API
- Load More: JS-driven append, no full page reload

**Reuse Opportunities:**
- Home, PDP, Collection (best review per collection)
- Testimonial pages, landing pages

---

## 12. Guarantee Section

**Purpose:** Reduce purchase hesitation by highlighting return/warranty policies.

**Inputs:**
- Guarantee items: 30-day trial, 90-day warranty, easy returns
- Badge/seal imagery (optional)

**Outputs:**
- Trust-building layout with guarantee details and badges

**States:**
- Default: static display
- No interactive states

**Variants:** None documented — same content on Home and PDP.

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: stack vertically
- Desktop: 2-column or side-by-side layout

**Accessibility:**
- Badge images: `alt` text describing the guarantee
- Text must be high contrast

**Shopify Implementation Notes:**
- Section: guarantee section with editable guarantee items
- Blocks: guarantee item blocks (icon, headline, description)
- Placement: last content section before footer (per placement rules)

**Reuse Opportunities:**
- Home (section 15), PDP (section 9)
- Checkout page (trust signals), cart drawer
- Any conversion-focused page

---

## 13. Newsletter Section

**Purpose:** Email list signup form.

**Inputs:**
- Headline text ("Get updates on new releases…")
- Description text
- Privacy notice text
- Form action URL (Shopify or Klaviyo endpoint)

**Outputs:**
- Centered form with headline, email input, subscribe button, privacy notice

**States:**
- Default: empty input
- Focus: input border highlight
- Submitting: button disabled/loading
- Success: confirmation message
- Error: validation message (invalid email)

**Variants:**
- Standalone section (footer area)
- Inline in footer (sometimes)
- PDP newsletter: separate styling with `border-top: 1px solid #e6e6e6`

**Dependencies:**
- Button component (Primary — Subscribe)
- Form validation

**Responsive Behavior:**
- Mobile: full-width input, stacked or inline
- Desktop: inline or stacked, max-width `600px` centered

**Accessibility:**
- `<label>` associated with email `<input>` (visible or `aria-label`)
- Error messages linked via `aria-describedby`
- Submit button must be keyboard-accessible
- Success/error announcements via `aria-live`

**Shopify Implementation Notes:**
- Section: newsletter section
- Form: Shopify customer form or Klaviyo embed
- Settings: headline, description, privacy text, success message
- PDP CSS: `.pdp-newsletter__form`, input padding `12px 16px`, button `12px 24px`

**Reuse Opportunities:**
- Home (near footer), PDP, potentially all pages
- Pop-up/modal version (not currently documented)

---

## 14. Footer

**Purpose:** Secondary navigation, legal compliance, social links.

**Inputs:**
- Navigation link columns (Customer Service, About, Legal, Social)
- Social media URLs
- Copyright text + year
- Optional newsletter form

**Outputs:**
- Dark background section with multi-column links, social icons, copyright

**States:**
- Default: static display
- Link hover: underline appears
- Link active: accent color
- Social icon hover: opacity or color shift

**Variants:** None — consistent across all pages.

**Dependencies:**
- Newsletter Section (optional embed)
- Social icon components

**Responsive Behavior:**
- Mobile: single-column stack, full width
- Desktop: 4-column grid (`1fr 1fr 1fr 1fr`), `56px` padding

**Accessibility:**
- Navigation: `<nav>` landmark with `aria-label="Footer"`
- Links: descriptive text (no "click here")
- Social icons: `aria-label` on each (e.g., "Instagram")
- Sufficient contrast (light text on dark bg)

**Shopify Implementation Notes:**
- Section: footer section in `layout/theme.liquid`
- Settings: link lists per column, social URLs, copyright text
- Common across all pages — not a dedicated section file

**Reuse Opportunities:**
- Global — every page
- Column structure could be reused for other multi-column text layouts

---

## 15. Founder Letter

**Purpose:** Personal founder communication to humanize the brand.

**Inputs:**
- Founder image URL
- Eyebrow label (optional)
- Opening quote (26–40px, 300 weight)
- Body text (15px, 1.65 line-height)
- Signature with title/role
- Optional supporting details list

**Outputs:**
- Dark background 2-column layout: image (left) + quote/body/signature (right)

**States:**
- Default: static display
- No interactive states (no animation)

**Variants:**
- Founder Letter (`/sections/founder-letter.html`) — quote + body + signature
- Founder Story (`/sections/founder2.html`) — narrative background/bio variant

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: stack image top, copy below; single column; padding `48px`
- Desktop: 2-column (`0.85fr` image : `1fr` copy); padding `76px`

**Accessibility:**
- Founder image: descriptive `alt` text
- High contrast white text on dark bg
- Quote: use `<blockquote>` element
- Max-width `48ch` on copy for readability

**Shopify Implementation Notes:**
- Section: founder-letter section
- Settings: image picker, quote text, body text, signature, title
- Source: `/sections/founder-letter.html`, `/sections/founder2.html`

**Reuse Opportunities:**
- Home page, About page
- Any page needing personal brand communication

---

## 16. Manifesto

**Purpose:** Declare brand beliefs and core values with impact typography.

**Inputs:**
- Eyebrow text ("MANIFESTO" or custom)
- Array of rotating headline statements
- Optional subtitle/body text (16px, soft white)
- Voice/tone tags (e.g., "Rigorous," "Warm," "Precise")

**Outputs:**
- Dark background centered section
- Rotating headline with opacity transitions
- Supporting text and voice tags

**States:**
- Default: headline rotating (0.7s ease transitions)
- Reduced motion: static headline (first or last)
- No interactive states

**Variants:**
- manifesto.html — primary version
- manifesto2.html — alternate messaging

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: reduced padding (`60px`), single column
- Desktop: full-width center-aligned, `96px` padding

**Accessibility:**
- Rotation must respect `prefers-reduced-motion`
- High contrast white text on dark bg
- Headline size via `clamp(38px, ..., 92px)` — ensure readability at minimum

**Shopify Implementation Notes:**
- Section: manifesto section
- Settings: eyebrow, headline messages (repeater blocks), subtitle, voice tags
- Typography: Roboto 300/600, all-caps eyebrow (`11px`, `0.18em` letter-spacing)
- Source: `/sections/manifesto.html`, `/sections/manifesto2.html`

**Reuse Opportunities:**
- Home page, About page
- Campaign landing pages
- Any brand-positioning context

---

## 17. Problem Section (Pain Point)

**Purpose:** Agitate customer pain point to establish need for the product.

**Inputs:**
- Eyebrow text ("THE PROBLEM" or custom)
- Display headline (30–50px)
- Body description (15px, soft text)
- List of old/failed solutions (with strikethrough styling)
- Optional supporting visual or stat

**Outputs:**
- Light/white background 2-column layout
- Left: problem statement + strikethrough list
- Right: supporting visual

**States:**
- Default: static display
- No interactive states

**Variants:**
- problem.html — primary messaging
- problem2.html — alternate messaging/framing

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: single column stack
- Desktop: 2-column grid (`1.15fr` : `0.85fr`)

**Accessibility:**
- Strikethrough items: use `<del>` or `<s>` with `aria-label` to convey meaning
- Text contrast on light bg must meet WCAG AA

**Shopify Implementation Notes:**
- Section: problem section
- Settings: eyebrow, headline, body, old-solutions list (repeater blocks), image picker
- Strikethrough uses `var(--m-accent)` color
- Spacing: `64px` padding, `14px` gap between list items
- Source: `/sections/problem.html`, `/sections/problem2.html`

**Reuse Opportunities:**
- Home page (not currently in Home section list — could be added)
- PDP, Collection, Landing pages
- Any comparison/agitation context

---

## 18. Closing Statement

**Purpose:** Bold final CTA section before the footer.

**Inputs:**
- Eyebrow text (optional)
- Headline (34–60px, 300 weight)
- Subtitle/body (16px, soft white)
- Primary CTA button (white bg, dark text — inverted from normal)
- Optional fine print

**Outputs:**
- Dark background centered section with headline + CTA

**States:**
- Default: static display
- Button hover: slight opacity or background shift
- No other interactive states

**Variants:** None documented — single version.

**Dependencies:**
- Button component (Primary — inverted: white bg, dark text)

**Responsive Behavior:**
- Mobile: reduced padding (`48px`), single column
- Desktop: center-aligned, `88px` padding

**Accessibility:**
- CTA must be keyboard-focusable and have visible focus indicator
- Sufficient contrast (white button on dark bg)
- Headline readable at min `clamp()` value

**Shopify Implementation Notes:**
- Section: closing-statement section
- Settings: eyebrow, headline, subtitle, CTA text/URL, fine print
- Source: `/sections/closing-statement.html`

**Reuse Opportunities:**
- Home page, About page, any page needing final conversion push
- Campaign pages

---

## 19. Credibility Section (Social Proof Band)

**Purpose:** Establish trust through brand partnerships and studio logos.

**Inputs:**
- Eyebrow text
- Headline (30–52px)
- Subtext (16px, soft white)
- Grid cells: 2–4 partner images with captions (studio name + "classes")
- Logo bar: brand names with dividers

**Outputs:**
- Dark background section with partner image grid + logo bar

**States:**
- Default: static display
- No interactive states

**Variants:** Multiple depending on partner count and imagery.

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: 1-column grid, logo bar stacks vertically
- Desktop: 2-column grid (`2px` cell gaps), horizontal logo bar

**Accessibility:**
- Partner images: descriptive `alt` text
- Logo text: readable at minimum `clamp()` size
- High contrast white text on dark bg

**Shopify Implementation Notes:**
- Section: credibility section with image/caption blocks
- Settings: eyebrow, headline, subtext, partner blocks (image + name + count)
- Cell aspect ratio: `5:4`
- Logo bar: centered text (`26px` weight `400`), small caps counts (`10px`)
- Source: `/sections/credibility.html`

**Reuse Opportunities:**
- Home page
- About page, press page
- Any trust-building context

---

## 20. Social Proof / Trust Badges

**Purpose:** Build credibility through trust signals placed contextually.

**Inputs:**
- Star rating (5★)
- Review count ("1,000+ reviews")
- Trust statement ("Trusted by 1,000's of instructors & studios")
- Made in USA badge
- Security/return badges

**Outputs:**
- Inline or stacked trust elements (stars, text, badges)

**States:**
- Default: static display
- No interactive states

**Variants:**
- Hero placement (inline with copy)
- Product card placement (below price)
- Checkout-area placement (near CTA)

**Dependencies:** None — atomic elements.

**Responsive Behavior:**
- Scales with parent container
- Text wraps on mobile

**Accessibility:**
- Stars: `aria-label="5 out of 5 stars"` (not color-only)
- Badges: `alt` text on images
- Text must be readable

**Shopify Implementation Notes:**
- Snippet: reusable trust-badge snippet
- Data: hardcoded or from metafields (review count from Judge.me)
- Placement rules: Hero, product cards, checkout sections

**Reuse Opportunities:**
- Hero, product cards, PDP buy box, cart drawer, checkout
- Email templates

---

## 21. Variant Grid (Product Selector)

**Purpose:** Select shoe build (Closed/Open Sole) and color with live preview.

**Inputs:**
- Build options (Closed Sole / Open Sole) — tabs
- Color options per build (swatches)
- Product images per combination
- Prices per variant

**Outputs:**
- Left: build tabs + color picker + selection summary + Add to Cart button
- Right: product image preview (updates on selection change)

**States:**
- Default: first build and color selected
- Tab active: one build selected (mutually exclusive)
- Color active: selected color has outline border
- Image updating: swaps on selection change
- Add to Cart: standard button states (default, hover, loading, disabled)

**Variants:** None — single implementation for Collection page.

**Dependencies:**
- Button component (Primary — Add to Cart, `11.5px` uppercase, full-width)
- Tab component (build selector)
- Product image display

**Responsive Behavior:**
- Mobile: stack form top, image bottom; single column
- Desktop: 2-column side-by-side (`1fr` : `1.1fr`), `56px` gap

**Accessibility:**
- Tabs: `role="tablist"`, `role="tab"`, `aria-selected`
- Color picker: `aria-label` per swatch with color name
- Selection summary: live region announcing current choice
- Form controls keyboard-navigable

**Shopify Implementation Notes:**
- Section: variants section
- Settings: collection reference, build labels
- Dynamic: product variants from Shopify product API
- Source: `/sections/variants.html`

**Reuse Opportunities:**
- Collection page (primary use)
- Could be adapted for gift sets or bundle builders

---

## 22. Range Section (Product Showcase Grid)

**Purpose:** Showcase all available products in a collection with quick-add.

**Inputs:**
- Array of products: image, name, optional number/index, description, price, shop link
- Column count (3)
- Section padding (`64px`)
- Card gap (`28px`)

**Outputs:**
- Grid of product cards with image + name + description + price + shop link

**States:**
- Default: static grid
- Card hover: image opacity or scale (1.02x), caption underline
- Quick Add: adds to cart directly from grid
- No swatches on cards

**Variants:**
- Home product grid
- Collection variants grid
- "Pairs with your kit" rail (PDP)

**Dependencies:**
- Product Card component (or simplified card)
- Cart API

**Responsive Behavior:**
- Mobile: 1–2 column stack
- Desktop: 3-column grid at `64px` padding

**Accessibility:**
- Card images: `alt` text
- Quick Add: keyboard-accessible
- Price: not color-dependent

**Shopify Implementation Notes:**
- Section: range section with collection reference
- Settings: collection picker, columns, show-description toggle
- Typography: number `11px` monospace accent, name `21px` 400, description `14px` soft, price `14px` dark 500
- Source: `/sections/range.html`

**Reuse Opportunities:**
- Home, Collection, PDP (product rail), search results
- Upsell/cross-sell anywhere

---

## 23. Sticky Add to Cart

**Purpose:** Persistent add-to-cart button visible while scrolling PDP content.

**Inputs:**
- Current product selection state (size, variant)
- Button text (dynamic: "Add to Cart" or "Choose Size & Add")
- Visibility trigger (appears after hero/main PDP section)

**Outputs:**
- Fixed-position primary button

**States:**
- Hidden: above hero section or at footer overlap
- Visible: fixed bottom (mobile) or floating (desktop)
- Default: shows current CTA text
- Needs size: "Choose Size & Add"
- Ready: "Add to Cart"
- Loading: spinner during cart operation

**Variants:**
- Mobile: fixed bottom, 100% width (minus safe-area padding)
- Desktop: floating above footer, max-width `480px`, centered, subtle shadow

**Dependencies:**
- Button component (Primary)
- PDP state (selected variant, size)
- Cart API
- Scroll position observer (visibility logic)

**Responsive Behavior:**
- Mobile: `position: fixed; bottom: 0;` 100% viewport width with safe-area padding
- Desktop: floating, `max-width: 480px`, centered

**Accessibility:**
- Must not trap keyboard focus
- Button must be keyboard-accessible
- Text updates announced via `aria-live` or meaningful label
- Z-index high but below modals

**Shopify Implementation Notes:**
- Integrated into PDP sections (not a standalone section)
- Requires JS: scroll observer for show/hide, cart state for label
- Button: `12px`, `600` weight, uppercase

**Reuse Opportunities:**
- PDP only (primary use)
- Could be adapted for collection quick-add or bundle pages

---

## 24. Promo Tiles

**Purpose:** Highlight featured products, new releases, or promotions.

**Inputs:**
- 2 tile items, each with: image (4:3 or custom), label (LE/New/Bestseller), optional copy, CTA
- Grid gap (`28px`)

**Outputs:**
- 2-column grid of promotional tiles with image + overlay label + copy + CTA

**States:**
- Default: static display
- Hover: slight scale or opacity on image
- No other interactive states

**Variants:** None documented — 2-tile layout only.

**Dependencies:**
- Button component (Tertiary — "Explore" or "Learn More")

**Responsive Behavior:**
- Mobile: 1-column full-width
- Desktop: 2-column (`1fr 1fr`), `28px` gap

**Accessibility:**
- Image alt text required
- Label badges: not color-only (text included)
- CTA must be keyboard-accessible

**Shopify Implementation Notes:**
- Section: promo-tiles section (or variation within range section)
- Blocks: 2 tile blocks with image picker, label, copy, CTA URL
- Source: `/sections/range.html` (promo variations)

**Reuse Opportunities:**
- Home page (section 7)
- Collection page, campaign pages
- Could expand to 3+ tiles for seasonal promotions

---

## 25. Association Strip (Associative Trust / Logo Strip)

**Purpose:** Reinforce legitimacy through partner brand names (Coperni, Free People, etc.).

**Inputs:**
- Eyebrow text (optional: "Loved by" or "Trusted by")
- Statement text ("Free People favorite. Coperni chosen.")
- Logo/partner names array (3–4)
- Fine print (optional: "Sold at…", "Featured in…")

**Outputs:**
- Light background centered section with statement + horizontal logo row with dividers

**States:**
- Default: static display
- No interactive states

**Variants:** Two versions depending on partner count.

**Dependencies:** None. Self-contained.

**Responsive Behavior:**
- Mobile: single column, logo names stack or wrap
- Desktop: horizontal row, logos centered, max-width `720px` centered

**Accessibility:**
- Text-based logos ensure screen reader compatibility
- Dividers: decorative (`aria-hidden`)
- Statement text: readable contrast

**Shopify Implementation Notes:**
- Section: association-strip section
- Settings: eyebrow, statement, partner names (repeater blocks), fine print
- Typography: statement `20–30px`, logo names `18–24px` clamp, fine print `12.5px` muted
- Source: `/sections/assoc.html`

**Reuse Opportunities:**
- Home page
- About page, press page
- Any trust/partnership display

---

## 26. FAQ Section

**Purpose:** Answer common questions in collapsible format.

**Inputs:**
- Array of FAQ items (question + answer pairs)
- Section background (`#f5f2ec` per PDP CSS)
- Max-width (`760px`)

**Outputs:**
- Vertically stacked accordion with FAQ items

**States:**
- Same as PDP Accordion (Component 10)
- Items: closed (default), open (one at a time)
- Transition: 200ms height

**Variants:**
- PDP FAQ (product-specific questions)
- General FAQ (site-wide questions)
- Shares accordion component implementation

**Dependencies:**
- Accordion component (Component 10)

**Responsive Behavior:**
- Mobile: full width, touch-friendly (44px tap targets)
- Desktop: centered, max-width `760px`

**Accessibility:**
- Same as PDP Accordion: `aria-expanded`, `aria-controls`, keyboard navigation
- `<button>` triggers, focusable content

**Shopify Implementation Notes:**
- Section: FAQ section with repeater blocks (question/answer)
- Settings: section title, FAQ item blocks
- PDP CSS: `.pdp-faq` with `80px 40px` padding, `#f5f2ec` background

**Reuse Opportunities:**
- PDP, Home (section 16), About page, policy pages
- Customer service page

---

## Additional Components (documented in 04 but not in user's list)

### Sock ⇄ Skin Toggle
- Cross-fade toggle between two product image states (240ms ease-out)
- Swaps stat figures, persists via `aria-pressed`
- Home page component

### PDP Main Section (Gallery + Buy Box)
- Left: gallery with thumbnail strip; Right: buy box (title, price, size, ATC)
- PDP-specific, 2-column layout

### PDP Gallery
- Click thumbnail → swap main, pinch/zoom on touch, keyboard ←/→
- Vertical thumbnail strip below main image

### PDP Size Picker
- Size pills with `aria-pressed`, strikethrough + `cursor: not-allowed` for OOS
- "Size Guide" link

### Collection Filter Row
- Inline chips (not sidebar), multi-select within facet, URL-syncs via query params

### Article / Blog Card
- Image + category label + headline + excerpt + "Read More" link
- 3-column grid on home

### Article Pull-Quote
- Larger typography (18px+), distinct background or border

### Disciplines Section
- 3 cards: Barre, Reformer, Megaformer
- Each: icon/image + discipline name + 2–3 benefit lines

### Coperni Collaboration Section
- Runway video or still image, LE badge, CTA
- Premium positioning, full-bleed

### Testimonial / Review Quote
- Single standout review, large typography (20px+), center-aligned

### Trust Badges & Guarantees Strip
- Multiple guarantee rows with icons, 2–3 column grid

### Closing CTAs & Button Groups
- Action-oriented button clusters, Primary/Secondary/Tertiary
- Integrated in all sections

### Featured Article / Journal Section
- Article grid (3 cards per row), category + headline + excerpt + read more
- Source: integrated in home page sections

---

## Component Placement Rules (from docs/04)

### Required Ordering
1. **Ticker** → always top of page, above header
2. **Header** → below ticker
3. **Hero** → directly below header
4. **Pillar Strip** → after hero (all pages)
5. **Splits** → after pillar strip (home)
6. **Product Grid** → after splits or pillars
7. **Sock Math** → after product grid (home) or early on PDP
8. **Reviews** → near bottom (trust before checkout)
9. **Guarantee** → last content section before footer

### Mutual Exclusions
- Two different slogans in same section → not allowed
- Multiple benefit grids on same page → consolidate
- Sock Math + other comparison sections → Math is the only comparison
- Hamburger + horizontal nav → choose one per viewport

---

## Cross-Component Token Dependencies

Many components reference CSS variables that have conflicting values across source documents. See `planning/design-token-audit.md` for the full conflict inventory. Key impacts:

- **All dark sections** (Manifesto, Founder Letter, Closing Statement, Credibility, Sock Math) reference `var(--m-dark)` — not defined in `:root`
- **Eyebrow styling** used in 10+ components has 3 conflicting letter-spacing specs
- **Border/line color** used in Header, Splits, Cards, Accordion differs across 3 sources
- **Button radius** is `0px` in system but `6px` in PDP CTA

---

**Last Updated:** 2026-07-13  
**Next Step:** Architect reviews token conflicts in `design-token-audit.md`, then this inventory gets updated with resolved token references.
