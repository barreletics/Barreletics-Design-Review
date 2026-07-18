# 11 — Navigation Architecture

---
document: 11 – Navigation Architecture
version: 1.0
status: 🔒 Locked
approved_by: Owner / Architect
approval_date: 2026-07-18
last_modified: 2026-07-18
depends_on: [02, 09]
supersedes: []
---

## Primary Navigation (flat, no mega-menu)

```
Grippy Shoes | Apparel | Collaborations | Journal     [Help] [Account] [Cart]
```

### Why "Grippy Shoes" Not "Performance Skins"

- **Mobile conversion:** Instantly understood, zero cognitive load
- **SEO:** Targets real search queries ("grip shoes for Pilates")
- **Brand building:** "Performance Skins" lives in page content, H1s, product descriptions — not wayfinding
- **Category name evolves** when brand is established and multiple product lines exist

### Grippy Shoes Sub-Navigation

- Shop All Grippy Shoes → `/collections/grippy-shoes` (pillar landing page)
- Open Sole → `/collections/open-sole`
- Closed Sole → `/collections/closed-sole`
- Outdoor → `/collections/outdoor`
- Compare Styles → `/pages/compare-open-closed-sole`

### Apparel Sub-Navigation

- Shop All Apparel → `/collections/apparel`
- Tops → `/collections/tops`
- Bottoms → `/collections/bottoms`
- Accessories → `/collections/accessories` (future)

### Help (Utility Nav)

- About Us → `/pages/about`
- FAQ → `/pages/faq`
- Contact Us → `/pages/contact`
- Returns & Exchanges → `/pages/returns-exchanges`

## Category Creation in Navigation

The nav uses "Grippy Shoes" because that's what customers search for today. But every page they land on educates them that these aren't shoes — they're Performance Skins. The nav meets customers where they are; the content moves them forward.

This is the category creation strategy applied to information architecture: familiar nav labels → educational page content → new category understanding.

## Mobile Behavior

- **Hamburger menu** with flat list (left side, opens slide-out drawer)
- Each category tap reveals sub-items inline (accordion, not new page)
- Help in utility position (bottom of mobile menu or separate icon)
- Cart icon always visible (right side)
- Close on selection, tap outside, or Escape key
- Touch targets ≥ 44px

## Header Behavior

| State | Behavior |
|-------|----------|
| Top of page | Transparent background, no bottom border |
| Scrolled (>8px) | White background, 1px hairline bottom (`#d6cfc0`), 200ms fade-in |
| Cart empty | No badge on cart icon |
| Cart has items | Coral dot badge (`#e8927c`) |
| Sticky | `position: fixed; top: 0; z-index: 40` |

## Footer Structure

| Column | Links |
|--------|-------|
| Shop | All Grippy Shoes · Open Sole · Closed Sole · Outdoor · Apparel |
| Support | FAQ · Shipping & Returns · Warranty · Contact Us |
| Company | About Us · Journal · Collaborations · Compare Styles |
| Newsletter | Email signup with 10% off |

**Footer style:** Dark background (`#1c1916`), white text, 4-column desktop → single-column mobile. Social icons: Instagram, TikTok, Facebook. Copyright: `© {year} Barreletics. All rights reserved.`

## Announcement Strip

Single strip rotating 3 messages:
1. `Buy 2, Save 15% — Code SAVE15`
2. `Free Shipping Over $150`
3. `30-Day Returns · Made in USA`

**Behavior:** 4s interval, 320ms opacity crossfade, pauses on hover, reduced motion → static (first slide).

## Future Scaling (3–5 Years)

```
Grippy Shoes | Socks | Apparel | Collaborations | Journal     [Help] [Account] [Cart]
```

- Socks get own top-level nav item (complement to Performance Skins, not a sub-product)
- Flat nav maintained — no "Shop" mega-menu unless 8+ categories
- 6 items within optimal 5–7 range
- "Performance Skins" may replace "Grippy Shoes" once brand recognition is sufficient

## Breadcrumbs

| Page Type | Breadcrumb |
|-----------|------------|
| Home | (none) |
| Collection | Home > Grippy Shoes |
| Sub-collection | Home > Grippy Shoes > Open Sole |
| PDP | Home > Grippy Shoes > [Product Name] |
| Article | Home > Journal > [Article Title] |
| Static page | Home > [Page Title] |

All breadcrumbs include `BreadcrumbList` schema markup.

---

**Cross-references:**
- SEO URL structure → `12-seo-geo-standards.md`
- Collection page → `09-collection-architecture.md`
- Header component → `04-component-library.md`
- Shopify implementation → `planning/shopify-build-specification.md`
