# 04 — Component Library

**Status:** 🔵 Ready for Review
**Last Updated:** 2026-07-18
**Source:** Promoted from `component-inventory.md` (archived)

---

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

### 12–26: Remaining Components

See the archived `component-inventory.md` for full specifications of: Guarantee, Newsletter, Footer, Founder Letter, Manifesto, Problem Section, Closing Statement, Credibility, Trust Badges, Variant Grid, Range Section, Sticky ATC, Promo Tiles, Association Strip, FAQ Section.

All follow the same specification pattern: Purpose, Inputs, States, Variants, Responsive, Accessibility, Shopify implementation notes.

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
- Full specs (archived) → `archive/component-inventory.md`
