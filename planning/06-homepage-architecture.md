# 06 — Homepage Architecture

---
document: 06 – Homepage Architecture
version: 1.1
status: 🔒 Locked
approved_by: Owner / Architect
approval_date: 2026-07-18
last_modified: 2026-07-20
depends_on: [02, 03, 04, 07, 08]
supersedes: []
frozen_spec: specs/frozen/homepage.md
---

**Approved Source:** `Barreletics Home - APPROVED July 17.html`  
**Build freeze (2026-07-20):** DP-01–DP-12 defaults applied — Hero A (Sock Era); keep GEO; Coperni seasonal; Home IG/UGC; value-strip (not 6-pillars); defer Founder/Manifesto/full Sock Math to About / Optional. Canonical frozen stack: `specs/frozen/homepage.md`.

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

### Section 2: Value / Trust Strip (launch)
- Shared `value-strip` component (DP-10) — **not** a forced 6-pillar strip at launch
- Optional later: dedicated 6-pillar strip if needed

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

### Section 5: Sock Math lite — "One Pair. Done." (launch)
- Condensed fifty-fifty / lite module (DP-11) — full dark 6-cell Sock Math is Optional / PDP-primary
- CTA to collection or shop

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

### Section 9–11: Founder / Manifesto / Closing — DEFERRED (DP-11)
- Ship on **About** first; do not block Home conversion spine
- Optional on Home after launch if length budget allows

### Section 9b (launch): GEO accordion (DP-03 / D-022)
- Required on Home for SEO/AI retrieval

### Section 9c (launch): Instagram / UGC band (DP-09)
- Home IG pattern; Collection uses reviews band instead

### Section 9d (launch): Coperni collab — seasonal (DP-08)
- Removable when campaign ends

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
