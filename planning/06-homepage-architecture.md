# 06 — Homepage Architecture

---
document: 06 – Homepage Architecture
version: 1.0
status: 🔒 Locked
approved_by: Owner / Architect
approval_date: 2026-07-18
last_modified: 2026-07-18
depends_on: [02, 03, 04, 07, 08]
supersedes: []
---

**Approved Source:** `Barreletics Home - APPROVED July 17.html`

## Page Purpose

Establish Barreletics as a category-creating brand — not just a product. The homepage moves visitors from "I need grip socks" to "grip socks are obsolete" to "show me Performance Skins." Primary conversion path: hero → product grid → PDP or direct add-to-cart.

## Section Architecture

### Section 1: Hero
- Full-viewport brand statement
- Background: lifestyle/studio image (1920×1080 desktop, 750×900 mobile)
- Rotating eyebrow (5 messages, 3.5s cycle):
  1. Barre. Reformer. Megaformer. One shoe.
  2. Trusted by 1,000's of instructors
  3. 360° grip. No latex, no silicone.
  4. Made in USA
  5. One Pair. No More Socks.
- H1 headline (category-creation statement)
- Primary CTA: Shop now → `/collections/grippy-shoes`
- Secondary CTA: See in action → scrolls to motion/video section
- Trust line: star rating + "Trusted by 1,000's of instructors & studios"

### Section 2: Pillar Strip
- Warm cream background (`#f5f2ec`)
- 6 pillars: 360° Grip · Second-Skin Fit · Reformer-Ready · Rinse & Reuse · No Latex/Silicone · Barefoot-Inspired
- Same component used on PDP and Collection

### Section 3: 50/50 Split — "Progress, built from the ground up"
- Image left, copy right
- Trusted line with star rating
- Category-creation messaging: studio performance, not sock replacement

### Section 4: Product Grid — "The Studio Collection"
- 4-column desktop, 2-column mobile
- Tab filtering: Closed Sole / Open Sole
- Size selector: M / L
- Product cards with quick-add (add to cart from homepage, no PDP redirect required)
- Gap: 28px

### Section 5: Sock Math — "Stop replacing. Start performing."
- Full variant (not condensed PDP version)
- Dark background
- Comparison: Traditional Socks ($336/year) vs Barreletics ($74)
- 6 benefit grid cells
- CTA to collection or PDP

### Section 6: 50/50 Split — "The Problem"
- Copy left, image right (reversed layout)
- Strikethrough list of old/failed solutions
- "The Double Failure" concept

### Section 7: 50/50 Split — "Never loses grip"
- Video variant with trusted line
- Image right, copy left (or configurable)

### Section 8: Reviews — "Real people. Real results."
- 6 curated reviews, 2–3 column grid
- Star ratings in `#d4af37`
- Load More button

### Section 9: Founder Letter
- Dark background, 2-column: portrait left, quote + body + signature right
- Personal brand communication
- Mobile: stack image top, copy below

### Section 10: Manifesto
- Dark background, centered
- Rotating headline statements (0.7s transitions)
- Voice/tone tags
- `prefers-reduced-motion` → static

### Section 11: Closing Statement
- Dark background, centered
- Bold headline + subtitle
- Inverted CTA (white bg, dark text)
- Final conversion push before footer

### Section 12: Newsletter — "Join the list"
- Email input + subscribe
- Klaviyo integration
- 10% off / SAVE15 code mention

### Global: Announcement Ticker (top of page)
- Single strip: `Buy 2, Save 15% — Code SAVE15 · Free Shipping Over $150 · 30-Day Returns · Made in USA`
- 3 slides, 4s interval, 320ms crossfade
- Pauses on hover

## Mobile Behavior

All sections stack vertically. Key adaptations:
- Hero: reduced height, text overlay maintained
- Product grid: 2-column
- 50/50 splits: image top, copy below, `height: auto`
- Sock Math: cards stack vertically
- Manifesto: reduced padding (60px)
- All touch targets ≥ 44px

## Content Strategy

The homepage follows a deliberate narrative arc:
1. **Declare** (Hero) — Bold category statement
2. **Prove** (Pillars, Splits) — Product attributes and social proof
3. **Compare** (Sock Math) — Quantify the category shift
4. **Convert** (Product Grid) — Shop directly
5. **Validate** (Reviews, Founder) — Trust and authenticity
6. **Close** (CTA, Newsletter) — Final conversion + retention

## Structured Data

- `Organization` JSON-LD: name, logo, url, sameAs (social links)
- `WebSite` JSON-LD: SearchAction for sitelinks searchbox
- `BreadcrumbList`: Home (single item)
- `FAQPage`: if FAQ section appears on homepage

## Meta Tags

- `<title>`: `Barreletics — Performance Skins for Barre, Pilates & Reformer`
- `<meta description>`: Category-creation framing, 150–160 chars
- OG tags with hero image

---

**Cross-references:**
- Design tokens → `03-design-system.md`
- Component specs → `04-component-library.md`
- Product content → `07-product-knowledge-base.md`
- Navigation → `11-navigation-architecture.md`
- SEO → `12-seo-geo-standards.md`
- Approved source → `Barreletics Home - APPROVED July 17.html`
