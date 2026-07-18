# 04 — Component Library

---
document: 04 – Component Library
version: 1.0
status: 🔵 Ready for Review
approved_by: —
approval_date: —
last_modified: 2026-07-18
depends_on: [03]
supersedes: [component-inventory.md]
---

**Source:** Promoted from `component-inventory.md` (archived)

## Component Index

| # | Component | Pages Used | Reusable |
|---|-----------|-----------|----------|
| 1 | Announcement Ticker | All | Yes |
| 2 | Header / Navigation | All | Yes |
| 3 | Hero Section | Home, Collection | Yes |
| 4 | Pillar Strip | Home, PDP, Collection | Yes |
| 5 | 50/50 Split | Home (×3), PDP, Collection | Yes |
| 6 | Product Card | Home, Collection, PDP cross-sell | Yes |
| 7 | Product Grid | Home, Collection, PDP | Yes |
| 8 | Sock Math | Home, PDP | Yes (2 variants) |
| 9 | Benefit Grid | Home, PDP, Collection | Yes |
| 10 | Accordion (FAQ/Specs) | PDP, FAQ page | Yes |
| 11 | Reviews Section | Home, PDP | Yes (2 variants) |
| 12 | Guarantee Section | Home, PDP | Yes |
| 13 | Newsletter Section | Home, PDP | Yes |
| 14 | Footer | All | Yes |
| 15 | Founder Letter | Home, About | Yes |
| 16 | Manifesto | Home, About | Yes |
| 17 | Problem Section | Home, PDP, Landing | Yes |
| 18 | Closing Statement | Home, About | Yes |
| 19 | Credibility / Social Proof | Home | Yes |
| 20 | Trust Badges | Hero, PDP buy box, Cart | Snippet |
| 21 | Variant Grid (Selector) | Collection | Page-specific |
| 22 | Range Section | Home, Collection | Yes |
| 23 | Sticky Add to Cart | PDP | Page-specific |
| 24 | Promo Tiles | Home | Yes |
| 25 | Association Strip | Home | Yes |
| 26 | FAQ Section | PDP, Home, FAQ page | Yes |

## Component Specifications

### 1. Announcement Ticker

**Purpose:** Rotate promotional messages at page top.

**Inputs:** Array of slide messages (max 5), rotation interval (4000ms), transition (320ms opacity crossfade)

**States:** Default (auto-rotating) · Hover (paused) · Reduced motion (static, last slide)

**Responsive:** Full width, same behavior all breakpoints.

**Accessibility:** `prefers-reduced-motion` respected. Content readable without JS (fallback to first slide).

**Shopify:** Section with slide blocks. Content editable via theme customizer.

---

### 2. Header / Navigation

**Purpose:** Primary site navigation, logo, cart access.

**States:** Default (transparent bg, no border) · Scrolled (white bg, 1px hairline bottom) · Cart empty (no badge) · Cart has items (coral dot badge) · Mobile menu open/closed

**Responsive:** Desktop: horizontal nav + centered logo. Mobile (<768px): hamburger left, logo center, cart right.

**Accessibility:** Keyboard navigable. `aria-expanded` on hamburger. Focus trap in mobile drawer. Skip-to-content as first focusable element.

**Shopify:** `sections/header.liquid`. Sticky: `position: fixed; top: 0; z-index: 40`. Nav from `linklists`.

---

### 3. Hero Section

**Purpose:** Full-viewport brand statement with rotating eyebrow.

**Inputs:** Background image, H1 headline, eyebrow rotation (5 messages, 3.5s), primary CTA, secondary CTA.

**Variants:** Home hero (full eyebrow rotation, 2 CTAs) · Collection hero (different copy, same layout)

**Responsive:** Mobile: stack vertically, reduce image height. Desktop: full viewport, centered.

**Accessibility:** Background image needs `alt` or `aria-label`. CTAs keyboard-focusable. Eyebrow rotation respects reduced motion.

---

### 4. Pillar Strip

**Purpose:** Horizontal display of 6 product attributes.

**Inputs:** 6 pillar items (icon + label + description). Background: `#f9f7f2`.

**Responsive:** Mobile: 2-column or vertical stack. Desktop: 6-column grid.

---

### 5. 50/50 Split

**Purpose:** Side-by-side image + copy editorial section.

**Inputs:** Image/video, eyebrow, headline, body, trusted line + stars (optional), layout direction (image-left or image-right).

**Canonical sizing:** `height: 420px` fixed, `overflow: hidden`, `padding: 80px 72px` copy side. Mobile: `height: auto`.

**Variants:** Split 1 "Never slip in chair pose" · Split 2 "Progress, built from the ground up" · Split 3 "Never loses grip" (video) · PDP Split · Collection Split

**Responsive:** Mobile: stack vertically, image top/bottom.

---

### 6. Product Card

**Purpose:** Display single product variant with image, name, price, quick-add.

**States:** Default · Hover (image 1.02× scale, 320ms, caption underline draws in) · Loading (spinner during cart add)

**Rule:** NEVER use swatches on individual cards — one color per card. No sold-out state defined yet (needs design).

**Responsive:** Mobile: full-width. Desktop: sized by parent grid.

---

### 7. Product Grid

**Purpose:** Collection of product cards in responsive grid.

**Inputs:** Product array, column count (3–4), filter tabs (Closed Sole / Open Sole), size selector (M/L), gap (28px).

**Accessibility:** Tabs: `role="tablist"`, `role="tab"`, `aria-selected`. Announce filter changes to screen readers.

---

### 8. Sock Math

**Purpose:** Cost-of-ownership comparison — grip socks vs Barreletics.

**Inputs:** Sock data ($336/year), Barreletics data ($74), 6 benefit grid cells, CTA.

**Variants:** Home (full, 6 benefit cells, "Stop replacing. Start performing.") · PDP (condensed, "One pair. Done.", includes double failure concept)

**Accessibility:** Dark bg requires high contrast. Comparison data in structured table. Strikethrough price needs `aria-label` or `<del>`.

---

### 9. Benefit Grid

**Purpose:** Scannable grid of product advantages.

**Variants:** Home/Sock Math (6 cells, dark bg): 360° traction, Second-skin fit, Reformer-ready, Rinse & reuse, No latex/silicone, Barefoot-inspired · PDP (6 cards): Reformer-ready, No twist, Sweat-ready, Rinse & reuse, Skin-safe, Barefoot feel · Collection (3 cards)

**Rule:** Only one benefit grid per page section.

---

### 10. Accordion (FAQ/Specs)

**Purpose:** Collapsible sections for product details or FAQ.

**Behavior:** Only one section open at a time. 200ms height animation. Chevron rotation indicator.

**Accessibility:** `aria-expanded`, `aria-controls`, `<button>` triggers. Enter/Space to toggle. 44px min tap target.

**Shopify:** PDP variant: Description, Size & Fit, Care, Returns. FAQ variant: Q&A pairs, max-width 760px.

---

### 11. Reviews Section

**Inputs:** Review array (stars, name, text, verified badge, optional image). 6 reviews per page, load more.

**Variants:** Home (6 curated, 2–3 col grid) · PDP (Judge.me integration, 3-col with images)

**Styling:** 12px border-radius, 1px solid `#e6e6e6`, 28px padding. Stars: 14px `#d4af37`.

---

### 12. Guarantee Section

**Purpose:** Reduce purchase hesitation by highlighting return/warranty policies.

**Inputs:** Guarantee items: 30-day returns, 90-day warranty, easy returns. Badge/seal imagery (optional).

**States:** Default (static display). No interactive states.

**Variants:** None — same content on Home and PDP.

**Responsive:** Mobile: stack vertically. Desktop: 2-column or side-by-side layout.

**Accessibility:** Badge images need `alt` text describing the guarantee. Text must be high contrast.

**Shopify:** Section with editable guarantee item blocks (icon, headline, description). Placement: last content section before footer (per placement rules).

---

### 13. Newsletter Section

**Purpose:** Email list signup form.

**Inputs:** Headline text, description, privacy notice, form action URL (Shopify or Klaviyo endpoint).

**States:** Default (empty input) · Focus (input border highlight) · Submitting (button disabled/loading) · Success (confirmation message) · Error (validation message).

**Variants:** Standalone section (footer area) · Inline in footer · PDP newsletter (separate styling with `border-top: 1px solid #e6e6e6`).

**Responsive:** Mobile: full-width input, stacked or inline. Desktop: inline or stacked, max-width `600px` centered.

**Accessibility:** `<label>` associated with email `<input>` (visible or `aria-label`). Error messages linked via `aria-describedby`. Success/error announcements via `aria-live`.

**Shopify:** Section with headline, description, privacy text, success message settings. Form: Shopify customer form or Klaviyo embed. PDP CSS: `.pdp-newsletter__form`, input padding `12px 16px`, button `12px 24px`.

---

### 14. Footer

**Purpose:** Secondary navigation, legal compliance, social links.

**Inputs:** Navigation link columns (Customer Service, About, Legal, Social), social media URLs, copyright text + year, optional newsletter form.

**States:** Default (static) · Link hover (underline appears) · Link active (accent color) · Social icon hover (opacity or color shift).

**Variants:** None — consistent across all pages.

**Responsive:** Mobile: single-column stack, full width. Desktop: 4-column grid (`1fr 1fr 1fr 1fr`), `56px` padding.

**Accessibility:** `<nav>` landmark with `aria-label="Footer"`. Links: descriptive text (no "click here"). Social icons: `aria-label` on each. Sufficient contrast (light text on dark bg).

**Shopify:** Section in `layout/theme.liquid`. Settings: link lists per column, social URLs, copyright text. Common across all pages.

---

### 15. Founder Letter

**Purpose:** Personal founder communication to humanize the brand.

**Inputs:** Founder image URL, eyebrow label (optional), opening quote (26–40px, 300 weight), body text (15px, 1.65 line-height), signature with title/role, optional supporting details list.

**States:** Default (static display). No interactive states.

**Variants:** Founder Letter (`/sections/founder-letter.html`) — quote + body + signature. Founder Story (`/sections/founder2.html`) — narrative background/bio variant.

**Responsive:** Mobile: stack image top, copy below; single column; padding `48px`. Desktop: 2-column (`0.85fr` image : `1fr` copy); padding `76px`.

**Accessibility:** Founder image: descriptive `alt` text. High contrast white text on dark bg. Quote: use `<blockquote>` element. Max-width `48ch` on copy for readability.

**Shopify:** Section with image picker, quote text, body text, signature, title settings.

---

### 16. Manifesto

**Purpose:** Declare brand beliefs and core values with impact typography.

**Inputs:** Eyebrow text ("MANIFESTO" or custom), array of rotating headline statements, optional subtitle/body text (16px, soft white), voice/tone tags.

**States:** Default (headline rotating, 0.7s ease transitions) · Reduced motion (static headline).

**Variants:** manifesto.html — primary version. manifesto2.html — alternate messaging.

**Responsive:** Mobile: reduced padding (`60px`), single column. Desktop: full-width center-aligned, `96px` padding.

**Accessibility:** Rotation must respect `prefers-reduced-motion`. High contrast white text on dark bg. Headline size via `clamp(38px, ..., 92px)`.

**Shopify:** Section with eyebrow, headline messages (repeater blocks), subtitle, voice tags. Typography: Roboto 300/600, all-caps eyebrow (`11px`, `0.18em` letter-spacing).

---

### 17. Problem Section

**Purpose:** Agitate customer pain point to establish need for the product.

**Inputs:** Eyebrow text ("THE PROBLEM" or custom), display headline (30–50px), body description (15px), list of old/failed solutions (with strikethrough styling), optional supporting visual.

**States:** Default (static display). No interactive states.

**Variants:** problem.html — primary messaging. problem2.html — alternate framing.

**Responsive:** Mobile: single column stack. Desktop: 2-column grid (`1.15fr` : `0.85fr`).

**Accessibility:** Strikethrough items: use `<del>` or `<s>` with `aria-label` to convey meaning. Text contrast on light bg must meet WCAG AA.

**Shopify:** Section with eyebrow, headline, body, old-solutions list (repeater blocks), image picker. Strikethrough uses `var(--m-accent)` color. Spacing: `64px` padding, `14px` gap.

---

### 18. Closing Statement

**Purpose:** Bold final CTA section before the footer.

**Inputs:** Eyebrow text (optional), headline (34–60px, 300 weight), subtitle/body (16px, soft white), primary CTA button (white bg, dark text — inverted), optional fine print.

**States:** Default (static display) · Button hover (slight opacity or background shift).

**Variants:** None — single version.

**Responsive:** Mobile: reduced padding (`48px`), single column. Desktop: center-aligned, `88px` padding.

**Accessibility:** CTA must be keyboard-focusable with visible focus indicator. Sufficient contrast (white button on dark bg). Headline readable at min `clamp()` value.

**Shopify:** Section with eyebrow, headline, subtitle, CTA text/URL, fine print settings.

---

### 19. Credibility Section (Social Proof Band)

**Purpose:** Establish trust through brand partnerships and studio logos.

**Inputs:** Eyebrow text, headline (30–52px), subtext (16px, soft white), grid cells: 2–4 partner images with captions (studio name + "classes"), logo bar: brand names with dividers.

**States:** Default (static display). No interactive states.

**Variants:** Multiple depending on partner count and imagery.

**Responsive:** Mobile: 1-column grid, logo bar stacks vertically. Desktop: 2-column grid (`2px` cell gaps), horizontal logo bar.

**Accessibility:** Partner images: descriptive `alt` text. Logo text: readable at minimum `clamp()` size. High contrast white text on dark bg.

**Shopify:** Section with eyebrow, headline, subtext, partner blocks (image + name + count). Cell aspect ratio: `5:4`. Logo bar: centered text (`26px` weight `400`), small caps counts (`10px`).

---

### 20. Trust Badges

**Purpose:** Build credibility through trust signals placed contextually.

**Inputs:** Star rating (5★), review count ("1,000+ reviews"), trust statement, Made in USA badge, security/return badges.

**States:** Default (static display). No interactive states.

**Variants:** Hero placement (inline with copy) · Product card placement (below price) · Checkout-area placement (near CTA).

**Responsive:** Scales with parent container. Text wraps on mobile.

**Accessibility:** Stars: `aria-label="5 out of 5 stars"` (not color-only). Badges: `alt` text on images. Text must be readable.

**Shopify:** Reusable trust-badge snippet. Data: hardcoded or from metafields (review count from Judge.me). Placement rules: Hero, product cards, checkout sections.

---

### 21. Variant Grid (Product Selector)

**Purpose:** Select shoe build (Closed/Open Sole) and color with live preview.

**Inputs:** Build options (Closed Sole / Open Sole) tabs, color options per build (swatches), product images per combination, prices per variant.

**States:** Default (first build and color selected) · Tab active (one build selected) · Color active (selected color has outline border) · Image updating (swaps on selection change) · Add to Cart (standard button states).

**Variants:** None — single implementation for Collection page.

**Responsive:** Mobile: stack form top, image bottom; single column. Desktop: 2-column side-by-side (`1fr` : `1.1fr`), `56px` gap.

**Accessibility:** Tabs: `role="tablist"`, `role="tab"`, `aria-selected`. Color picker: `aria-label` per swatch with color name. Selection summary: live region announcing current choice.

**Shopify:** Section with collection reference, build labels. Dynamic product variants from Shopify product API.

---

### 22. Range Section (Product Showcase Grid)

**Purpose:** Showcase all available products in a collection with quick-add.

**Inputs:** Array of products (image, name, optional number/index, description, price, shop link), column count (3), section padding (`64px`), card gap (`28px`).

**States:** Default (static grid) · Card hover (image 1.02× scale, caption underline) · Quick Add (adds to cart directly). No swatches on cards.

**Variants:** Home product grid · Collection variants grid · "Pairs with your kit" rail (PDP).

**Responsive:** Mobile: 1–2 column stack. Desktop: 3-column grid at `64px` padding.

**Accessibility:** Card images: `alt` text. Quick Add: keyboard-accessible. Price: not color-dependent.

**Shopify:** Section with collection reference. Settings: collection picker, columns, show-description toggle. Typography: number `11px` monospace accent, name `21px` 400, description `14px` soft, price `14px` dark 500.

---

### 23. Sticky Add to Cart

**Purpose:** Persistent add-to-cart button visible while scrolling PDP content.

**Inputs:** Current product selection state (size, variant), button text (dynamic: "Add to Cart" or "Choose Size & Add"), visibility trigger (appears after hero/main PDP section).

**States:** Hidden (above hero section or at footer overlap) · Visible (fixed bottom mobile or floating desktop) · Needs size ("Choose Size & Add") · Ready ("Add to Cart") · Loading (spinner during cart operation).

**Variants:** Mobile: fixed bottom, 100% width (minus safe-area padding). Desktop: floating above footer, max-width `480px`, centered, subtle shadow.

**Responsive:** Mobile: `position: fixed; bottom: 0;` 100% viewport width with safe-area padding. Desktop: floating, `max-width: 480px`, centered.

**Accessibility:** Must not trap keyboard focus. Button must be keyboard-accessible. Text updates announced via `aria-live` or meaningful label. Z-index high but below modals.

**Shopify:** Integrated into PDP sections (not standalone). Requires JS: scroll observer for show/hide, cart state for label. Button: `12px`, `600` weight, uppercase.

---

### 24. Promo Tiles

**Purpose:** Highlight featured products, new releases, or promotions.

**Inputs:** 2 tile items, each with: image (4:3 or custom), label (LE/New/Bestseller), optional copy, CTA. Grid gap (`28px`).

**States:** Default (static display) · Hover (slight scale or opacity on image).

**Variants:** None — 2-tile layout only.

**Responsive:** Mobile: 1-column full-width. Desktop: 2-column (`1fr 1fr`), `28px` gap.

**Accessibility:** Image alt text required. Label badges: not color-only (text included). CTA must be keyboard-accessible.

**Shopify:** Section (or variation within range section). Blocks: 2 tile blocks with image picker, label, copy, CTA URL.

---

### 25. Association Strip

**Purpose:** Reinforce legitimacy through partner brand names (Coperni, Free People, etc.).

**Inputs:** Eyebrow text (optional: "Loved by" or "Trusted by"), statement text ("Free People favorite. Coperni chosen."), logo/partner names array (3–4), fine print (optional).

**States:** Default (static display). No interactive states.

**Variants:** Two versions depending on partner count.

**Responsive:** Mobile: single column, logo names stack or wrap. Desktop: horizontal row, logos centered, max-width `720px` centered.

**Accessibility:** Text-based logos ensure screen reader compatibility. Dividers: decorative (`aria-hidden`). Statement text: readable contrast.

**Shopify:** Section with eyebrow, statement, partner names (repeater blocks), fine print settings. Typography: statement `20–30px`, logo names `18–24px` clamp, fine print `12.5px` muted.

---

### 26. FAQ Section

**Purpose:** Answer common questions in collapsible format.

**Inputs:** Array of FAQ items (question + answer pairs), section background (`#f5f2ec`), max-width (`760px`).

**States:** Same as Accordion (Component 10). Items: closed (default), open (one at a time). Transition: 200ms height.

**Variants:** PDP FAQ (product-specific questions) · General FAQ (site-wide questions). Shares accordion component implementation.

**Responsive:** Mobile: full width, touch-friendly (44px tap targets). Desktop: centered, max-width `760px`.

**Accessibility:** Same as Accordion: `aria-expanded`, `aria-controls`, keyboard navigation. `<button>` triggers, focusable content.

**Shopify:** Section with repeater blocks (question/answer). Settings: section title, FAQ item blocks. PDP CSS: `.pdp-faq` with `80px 40px` padding, `#f5f2ec` background.

---

### Additional Components

#### Sock ⇄ Skin Toggle
Cross-fade toggle between two product image states (240ms ease-out). Swaps stat figures, persists via `aria-pressed`. Home page component.

#### PDP Main Section (Gallery + Buy Box)
Left: gallery with thumbnail strip. Right: buy box (title, price, size, ATC). PDP-specific, 2-column layout.

#### PDP Gallery
Click thumbnail → swap main, pinch/zoom on touch, keyboard ←/→. Vertical thumbnail strip below main image.

#### PDP Size Picker
Size pills with `aria-pressed`, strikethrough + `cursor: not-allowed` for OOS. "Size Guide" link.

#### Collection Filter Row
Inline chips (not sidebar), multi-select within facet, URL-syncs via query params.

#### Article / Blog Card
Image + category label + headline + excerpt + "Read More" link. 3-column grid on home.

#### Article Pull-Quote
Larger typography (18px+), distinct background or border.

#### Disciplines Section
3 cards: Barre, Reformer, Megaformer. Each: icon/image + discipline name + 2–3 benefit lines.

#### Coperni Collaboration Section
Runway video or still image, LE badge, CTA. Premium positioning, full-bleed.

#### Testimonial / Review Quote
Single standout review, large typography (20px+), center-aligned.

#### Trust Badges & Guarantees Strip
Multiple guarantee rows with icons, 2–3 column grid.

#### Closing CTAs & Button Groups
Action-oriented button clusters, Primary/Secondary/Tertiary. Integrated in all sections.

#### Featured Article / Journal Section
Article grid (3 cards per row), category + headline + excerpt + read more.

## Component Placement Rules

### Required Ordering
1. Ticker → top of page, above header
2. Header → below ticker
3. Hero → directly below header
4. Pillar Strip → after hero (all pages)
5. Content sections → per page architecture
6. Guarantee → last content section before footer
7. Footer → bottom

### Mutual Exclusions
- Two slogans in same section → not allowed
- Multiple benefit grids on same page → consolidate
- Sock Math + other comparison sections → Sock Math is the only comparison
- Hamburger + horizontal nav → one per viewport

## Token Dependencies

All components reference CSS custom properties from the design system (`03-design-system.md`). No hardcoded hex values in component CSS.

---

**Cross-references:**
- Design tokens → `03-design-system.md`
- PDP component usage → `05-pdp-architecture.md`
- Homepage component usage → `06-homepage-architecture.md`
- Collection component usage → `09-collection-architecture.md`
