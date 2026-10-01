# 09 — Collection / Pillar Page Architecture

---
document: 09 – Collection / Pillar Page Architecture
version: 1.1
status: 🔒 Locked
approved_by: Owner / Architect
approval_date: 2026-07-18
last_modified: 2026-07-20
depends_on: [03, 04, 07, 12]
supersedes: []
frozen_spec: specs/frozen/collections.md
---

**Approved Source:** `Barreletics Collection - Definitive-v4.html`  
**Build freeze (2026-07-20):** DP-04 shop-first H1 + stronger SEO subhead; DP-05 reviews band; DP-06 keep FAQ; DP-10 value-strip. See `specs/frozen/collections.md`.

## Page Purpose

The Collection page serves a dual role:
1. **Shopping page** — Browse, filter, and add products to cart
2. **Pillar page** — Educational content hub optimized for SEO and AI search, designed to be the definitive resource AI systems cite when answering "best grip socks for Pilates" queries

This dual role supports the category creation strategy: customers arrive searching for grip socks and leave understanding why Performance Skins are the next generation.

## URL Structure

| Page | URL | Purpose |
|------|-----|---------|
| Pillar landing | `/collections/grippy-shoes` | Primary entry — all products + educational content |
| Open Sole | `/collections/open-sole` | Filtered sub-collection |
| Closed Sole | `/collections/closed-sole` | Filtered sub-collection |
| Outdoor | `/collections/outdoor` | Secondary context sub-collection |
| Compare | `/pages/compare-open-closed-sole` | Decision support page |

**Internal linking:** Pillar → sub-collections → PDP → back to pillar

## Section Architecture

### Section 1: Collection Hero (DP-04)
- **Shop-first H1** (e.g., “Shop All Styles & Colors” / collection title)
- **Stronger SEO/category subhead** — Performance Skins vs grip socks; two builds; $74
- Sole chooser cards with “Best for…” / Pick this if labels
- Trust signals as available

### Section 2: Value / Trust Strip
- Shared `value-strip` (DP-10); 6-pillar strip Optional

### Section 3: Sole Type Chooser
- Visual comparison: Open Sole card vs Closed Sole card
- Each card: image, title, brief description, link to sub-collection
- Quick decision aid before browsing products

### Section 4: Product Grid
- 3–4 column desktop, 2 column mobile
- Filter row: inline horizontal chips (not sidebar)
- Facets: Sole Type, Color, Size
- Sort: Best selling, Price low-high, Price high-low, Newest
- Quick-add on product cards
- URL-syncs via query params for bookmarkable filtered views

### Section 5: Benefit Grid (abbreviated)
- 3 cards: Reformer-ready · Two builds (closed/open) · Rinse & reuse
- Scannable advantages below product grid

### Section 6: 50/50 Split — Category Creation
- "The Pilates sock era is over" framing
- Educational content about why Performance Skins replace grip socks

### Section 7: Reviews band (DP-05) — required
- 3–6 curated reviews / instructor quotes (`social-proof` section)
- Collection does **not** use Home IG widget (DP-09)

### Section 8: FAQ (abbreviated) — required (DP-06)
- 4–6 most common questions
- Accordion format, max-width 760px
- Content sourced from Master Knowledge Base (doc 07)
- FAQ schema markup for SEO

### Section 9: GEO Content (below FAQ)
- Positioned for crawlers, not shoppers
- City/state-specific content with discipline-specific moves
- Studio types, equipment, and specific exercises
- Internal links to relevant products
- See `12-seo-geo-standards.md` for full GEO strategy

### Section 9: Newsletter
- "Join the list" email signup + benefit checkmarks — **NO 10%** (offer retired; see `specs/frozen/footer.md`)

## Pillar Page Content Requirements (SEO)

The pillar page must include:
- Educational intro explaining the category (Performance Skins vs grip socks)
- Buying guidance (Open Sole vs Closed Sole decision framework)
- Category benefits (structured for featured snippets)
- Comparison content (vs grip socks) in structured format
- Product grid with all products
- FAQ with schema markup
- Discipline-specific content (with verified move names)
- Customer testimonials with name/city
- GEO sections for local SEO

## Structured Data

- `CollectionPage` schema
- `BreadcrumbList`: Home > Grippy Shoes (or Home > Grippy Shoes > Open Sole)
- `FAQPage` schema on FAQ section
- Product schema inherited from individual product cards

## Meta Tags

- `<title>`: `Grippy Shoes for Barre, Pilates & Reformer | Barreletics`
- `<meta description>`: Category-creation framing + key differentiators, 150–160 chars
- Canonical URL: `/collections/grippy-shoes`
- Sub-collections have their own canonical URLs

## Mobile Behavior

- Filter row: horizontal scroll, tap to toggle
- Product grid: 2-column
- All sections stack vertically
- Touch targets ≥ 44px

---

**Cross-references:**
- Design tokens → `03-design-system.md`
- Component specs → `04-component-library.md`
- Product content → `07-product-knowledge-base.md`
- Navigation → `11-navigation-architecture.md`
- SEO/GEO → `12-seo-geo-standards.md`
- Approved source → `Barreletics Collection - Definitive-v4.html`
