# 05 — PDP Architecture

---
document: 05 – PDP Architecture
version: 1.0
status: 🔵 Ready for Review
approved_by: —
approval_date: —
last_modified: 2026-07-18
depends_on: [03, 04, 07, 08]
supersedes: []
---

**Approved Source:** `Barreletics PDP - APPROVED July 17.html`

## Page Purpose

Convert a browsing visitor into a buyer by providing complete product information, social proof, and frictionless purchase flow — while reinforcing the category creation message (Performance Skins replace grip socks).

## Layout

Two-column desktop, single-column mobile. Max content width: 1200px. Gutters: 32px desktop, 16px mobile.

**Desktop:** Media gallery (left, ~55%) + Buy box (right, ~45%)
**Mobile:** Gallery → Buy box → Content sections (vertical stack)

## Section Architecture

### Section 1: Hero (Gallery + Buy Box)

**Gallery (left column):**
- Hero image with 8px border-radius
- Thumbnail strip below (horizontal scroll mobile)
- Click thumbnail → swap hero
- Pinch-to-zoom on mobile
- Keyboard ←/→ navigation
- Lazy-loaded via Shopify `image_url` filters
- Hero image: `loading="eager"`, `fetchpriority="high"`

**Buy Box (right column):**
- Rust badge: category label (10px / 700 / uppercase / 0.08em / `#c45c3f` bg / 3px radius)
- Product title: 44px / 700 / `#1c1916` / 1.08 line-height → 32px mobile
- Star rating: `#d4af37` gold, linked to review count
- Price: $74 (compare-at with strikethrough when applicable)
- Installments: "4 interest-free payments of $18.50"
- Size selector: pill buttons (S/M/L), 6px radius, `aria-pressed`, strikethrough for OOS
- Color swatches: 23px circles, 2px border, `border-color: #1c1916` when selected
- Add to Cart button: full width, 18px padding, `#1c1916` bg, 6px radius, hover → `#c45c3f`
- Trust row below ATC: Ships 1–2 days · 30-day returns · 90-day warranty · Latex- & silicone-free · Made in USA

### Section 2: Brand Pillars Strip
- Warm cream background (`#f5f2ec`)
- 6 pillar items with icons
- Same component as homepage pillar strip

### Section 3: Variant Grid — "The Studio Collection"
- Tab filtering: Closed Sole / Open Sole
- Size selector: M / L
- 4-column → 2-column at 1024px
- Product cards with quick-add (no swatches on cards)
- Gap: 20px → 16px mobile

### Section 4: Reviews — "Real people. Real results."
- Judge.me integration
- 3-column grid with images
- Review cards: 12px radius, 1px `#e6e6e6` border, 28px padding
- Stars: 14px `#d4af37`
- Load More pagination (6 per page)
- Aggregate rating + review count display

### Section 5: Sock Math — "One pair replaces eight."
- Condensed PDP variant
- Dark background section
- Two comparison cards: Traditional Socks ($336/year) vs Barreletics ($74)
- 6 benefit cells
- "Double failure" concept embedded
- CTA: "One Pair. Done."

### Section 6: Motion — "See how it works."
- Video container with 8px border-radius
- Autoplay on hover/interaction (not on load)
- Mobile: tap to play

### Section 7: Justifier Testimonials — "Real feedback from the floor."
- Justifier cards: 12px radius, left border 5px solid `#c45c3f`
- Tag: 11px `#c45c3f` uppercase
- Customer quotes with name and city

### Section 8: FAQ — "Everything you need to know."
- Accordion component, max-width 760px, centered
- Warm cream background (`#f5f2ec`)
- Padding: 80px 40px
- One item open at a time
- Content sourced from Master Knowledge Base (doc 07)
- FAQ schema markup for SEO

### Section 9: Newsletter — "Join the list"
- Email input + subscribe button
- Border-top: 1px solid `#e6e6e6`
- Klaviyo integration
- Privacy notice

### Sticky Add to Cart
- Appears after scrolling past main ATC button
- Mobile: fixed bottom, 100% width, safe-area padding
- Desktop: floating, max-width 480px, centered, subtle shadow
- Dynamic text: "Add to Cart" or "Choose Size & Add"

## PDP Accordion Content (Specs)

| Panel | Content Source |
|-------|---------------|
| Description | Product description from Knowledge Base |
| Size & Fit | Sizing guidance from Knowledge Base (doc 07) |
| Care | Cleaning & care from Knowledge Base |
| Returns & Exchanges | Policy from Knowledge Base |

## Structured Data

- `Product` JSON-LD: name, description, image, sku, brand, offers (price, availability, url)
- `AggregateRating`: ratingValue, reviewCount (from Judge.me)
- `BreadcrumbList`: Home > Grippy Shoes > [Product Name]
- `FAQPage`: All FAQ accordion items

## Meta Tags

- `<title>`: `{Product Name} — {Sole Type} | Barreletics`
- `<meta description>`: 150–160 chars, includes primary keyword + key benefit
- OG tags: title, description, product image, price
- Canonical URL: `/products/{handle}`

## Content Strategy

The PDP reinforces category creation at three touch points:
1. **Badge + title framing** — "Studio Performance Skin" not "grip shoe"
2. **Sock Math section** — quantifies why grip socks are the wrong choice
3. **FAQ** — answers reframe from "is this better than socks?" to "this replaces socks entirely"

---

**Cross-references:**
- Design tokens → `03-design-system.md`
- Component specs → `04-component-library.md`
- Product content → `07-product-knowledge-base.md`
- SEO requirements → `12-seo-geo-standards.md`
- Approved source → `Barreletics PDP - APPROVED July 17.html`
