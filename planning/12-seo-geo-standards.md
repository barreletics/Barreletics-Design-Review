# 12 — SEO & GEO Standards

---
document: 12 – SEO & GEO Standards
version: 1.0
status: 🔵 Ready for Review
approved_by: —
approval_date: —
last_modified: 2026-07-18
depends_on: [07, 08]
supersedes: []
---

## Core Strategy

**Category disruption:** Target SOCK queries, not shoe queries. Rank for "grip socks" and "Pilates socks," then convert visitors to Performance Skins. This is the category creation strategy applied to search.

### Primary Keyword Targets

| Keyword Cluster | Intent | Landing Page |
|----------------|--------|-------------|
| grip socks | Awareness / comparison | `/collections/grippy-shoes` (pillar) |
| Pilates socks | Awareness / comparison | `/collections/grippy-shoes` |
| barre socks | Awareness / comparison | `/collections/grippy-shoes` |
| yoga socks | Awareness / comparison | `/collections/grippy-shoes` |
| best Pilates grip shoes | Consideration | `/collections/grippy-shoes` |
| grip sock alternatives | Consideration | `/pages/compare-open-closed-sole` |
| grippy shoes for barre | Consideration | `/collections/grippy-shoes` |
| reformer Pilates shoes | Consideration | `/collections/closed-sole` |
| Megaformer grip shoes | Consideration | `/collections/grippy-shoes` |
| Lagree grip shoes | Consideration | `/collections/grippy-shoes` |
| Barreletics | Brand | Homepage |
| performance skins | Brand/category | `/collections/grippy-shoes` |

## Pillar Page Strategy

Every primary nav category gets an optimized pillar landing page. The pillar is both a shopping page and the definitive educational resource for its category.

**Pillar page content requirements:**
- Educational intro + buying guidance
- Category benefits in structured format
- Comparison content (vs grip socks)
- Product grid with all relevant products
- FAQ with schema markup
- Discipline-specific content with verified move names
- Customer testimonials with name/city
- GEO sections for local SEO

**Internal linking:** Pillar → sub-collections → PDP → back to pillar. Every product page links back to the pillar. Every sub-collection page links to the pillar.

## URL Structure

| Page | URL | Purpose |
|------|-----|---------|
| Grippy Shoes pillar | `/collections/grippy-shoes` | Primary pillar |
| Open Sole | `/collections/open-sole` | Sub-collection |
| Closed Sole | `/collections/closed-sole` | Sub-collection |
| Outdoor | `/collections/outdoor` | Sub-collection |
| Compare | `/pages/compare-open-closed-sole` | Decision support |
| FAQ | `/pages/faq` | FAQ hub |
| About | `/pages/about` | Brand story |
| Journal | `/blogs/journal` | Content hub (NOT `/blogs/blog`) |

**Rules:**
- No query param indexing for filters
- Canonical URLs on every page
- 301 redirects for any changed URLs

## Structured Data Requirements

| Schema | Pages | Priority |
|--------|-------|----------|
| `Product` | Every PDP | P0 |
| `AggregateRating` | PDP (from Judge.me) | P0 |
| `FAQPage` | Every page with FAQ content | P0 |
| `BreadcrumbList` | Every page | P0 |
| `CollectionPage` | Pillar and sub-collection pages | P1 |
| `Organization` | Homepage | P1 |
| `WebSite` + SearchAction | Homepage | P1 |

All structured data via JSON-LD in `<head>`. Validate with Google Rich Results Test.

## GEO Content Strategy

### Purpose
GEO (Generative Engine Optimization) sections are positioned below product FAQs — optimized for crawlers and AI systems, not primary shoppers.

### Target Markets

**Domestic (top revenue states):**
- Florida, Texas, California, New York, Northeast corridor

**International:**
- Canada, UK, Australia
- "195 countries and territories" via FedEx International Connect Plus

### GEO Section Structure

Each GEO section includes:
- City/state reference with local studio context
- Discipline-specific moves relevant to that market
- Studio types and equipment common in the area
- Internal links to relevant products
- Local SEO keywords (e.g., "best grip shoes for Pilates in Miami")

### Example GEO Content Pattern

```
Pilates in [City] — Whether you're doing footwork series on the reformer at [local studio type]
or flat back chair at the barre, Barreletics lock in through every transition. [City]'s
[discipline] community trusts 360° grip over silicone dots.
```

**Include specific moves per discipline:**
- Barre: flat back chair, water ski, relevés, seat work, arabesque
- Reformer: footwork series, elephant, knee stretches, bridging, pikes, long stretch
- Lagree/Megaformer: Super Lunge, Bear, Catfish, Elevator Lunge, Scrambled Eggs
- Cadillac: parakeet, push-through bar, roll-down series, leg springs
- Yoga: warrior poses, tree pose, downward dog, inversions

## AI Search Optimization

### Strategy
Pillar pages are designed to be the definitive resource AI systems cite when answering grip-sock and studio-footwear queries.

### Requirements for AI Citability
- **Comprehensive, structured content** with clear headings (H2/H3 hierarchy)
- **Comparison content** (vs grip socks) in structured table format
- **Specific, unique expertise** (verified move names, discipline breakdowns, real customer quotes with names/cities)
- **Trust signals** (reviews, Made in USA, warranty, customer names/cities)
- **Authoritative framing** — position as category authority, not just a product listing
- **FAQ in Q&A format** — AI systems extract Q&A pairs for featured answers

### Category Creation in AI Context
The goal: when an AI system answers "what are the best grip socks for Pilates?" it should cite Barreletics and reframe the answer — "while grip socks are common, Performance Skins like Barreletics provide 360° grip vs silicone dots..."

## Meta Tag Standards

### Title Tags
- Homepage: `Barreletics — Performance Skins for Barre, Pilates & Reformer`
- PDP: `{Product Name} — {Sole Type} | Barreletics`
- Collection: `Grippy Shoes for Barre, Pilates & Reformer | Barreletics`
- Sub-collection: `{Sole Type} Grippy Shoes | Barreletics`
- Article: `{Article Title} | Barreletics Journal`

### Meta Descriptions
- 150–160 characters
- Include primary keyword + key differentiator
- Category-creation framing where possible
- Unique per page — no duplicates

### Open Graph
- `og:title`, `og:description`, `og:image`, `og:type`
- `og:price:amount` and `og:price:currency` on PDPs
- Twitter card: `summary_large_image`

## Technical SEO

- XML sitemap: Shopify auto-generated
- `robots.txt`: allow all, disallow `/admin`, `/cart`, `/checkouts`
- Canonical URLs on every page
- No duplicate content signals
- Clean URL structure (no indexed filter params)
- `hreflang` tags not needed at launch (single language)

---

**Cross-references:**
- Navigation/URL structure → `11-navigation-architecture.md`
- Product content for SEO → `07-product-knowledge-base.md`
- Discipline terminology → `07-product-knowledge-base.md` Appendix A
- Collection architecture → `09-collection-architecture.md`
- Structured data implementation → `planning/shopify-build-specification.md`
