# 20 — SEO Architecture

---
document: 20 – SEO Architecture
version: 1.0
status: Draft
created: 2026-07-19
depends_on: [12-seo-geo-standards]
decision_refs: [D-022]
---

## Overview

SEO implementation is split between `layout/theme.liquid` (meta tags, Organization/WebSite schemas), dedicated schema snippets (per-page structured data), and the GEO content section (AI discoverability). All structured data uses JSON-LD format in `<head>` or inline with the section that owns the data.

## Structured Data Inventory

| Schema Type | Location | Condition |
|---|---|---|
| Organization | `layout/theme.liquid` (inline) | All pages |
| WebSite + SearchAction | `layout/theme.liquid` (inline) | Homepage only (`template.name == 'index'`) |
| Product + aggregateRating | `sections/pdp-buy-box.liquid` | PDP only |
| BreadcrumbList | `snippets/breadcrumb.liquid` | All pages except homepage |
| CollectionPage | `snippets/collection-schema.liquid` | Collection pages (`template.name == 'collection'`) |
| BlogPosting | `snippets/article-schema.liquid` | Article pages (`template.name == 'article'`) |
| FAQPage | `sections/geo-section.liquid` | Any page with GEO blocks (conditional on `geo_blocks_count > 0`) |
| Organization (enhanced) | `snippets/organization-schema.liquid` | About page (manually rendered) |

## Schema Details

### Organization (`theme.liquid`)

Output on every page in `<head>`:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Barreletics",
  "url": "{{ shop.url }}",
  "logo": "{{ 'logo.png' | asset_url }}"
}
```

### WebSite + SearchAction (`theme.liquid`)

Output only on homepage (`template.name == 'index'`):
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Barreletics",
  "url": "{{ shop.url }}",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "{{ shop.url }}/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### Product (`sections/pdp-buy-box.liquid`)

Output at bottom of PDP buy box section. Includes:
- `@type: Product`
- `name`, `description` (truncated 200 chars), `brand` (Barreletics), `image`, `url`
- `sku` (if variant has one)
- `offers` with `price`, `priceCurrency` (USD), `availability` (InStock/OutOfStock), `seller`
- `aggregateRating` — conditional on `jm_count_schema > 0` (see Doc 17)

### BreadcrumbList (`snippets/breadcrumb.liquid`)

Output on all pages except homepage (`template != 'index'`). JSON-LD with `itemListElement` array. Position numbering starts at 1 (Home).

### CollectionPage (`snippets/collection-schema.liquid`)

Rendered by `theme.liquid` when `template.name == 'collection'`:
```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "{{ collection.title }}",
  "description": "{{ collection.description | strip_html | truncate: 160 }}",
  "url": "{{ shop.url }}{{ collection.url }}",
  "numberOfItems": {{ collection.products_count }}
}
```

### BlogPosting (`snippets/article-schema.liquid`)

Rendered by `theme.liquid` when `template.name == 'article'`:
- `headline`, `datePublished`, `dateModified`, `author` (Person), `publisher` (Organization with logo)
- `description` (excerpt, truncated 160 chars), `mainEntityOfPage`, `image` (conditional)

### FAQPage (`sections/geo-section.liquid`)

Output when section has `geo_item` blocks. Each block becomes a `Question` with `acceptedAnswer`. Used for GEO content — see GEO section below.

### Organization Enhanced (`snippets/organization-schema.liquid`)

Extended version for About page with `description`, `foundingCountry`, and `sameAs` array (Instagram, TikTok, Facebook URLs).

---

## Meta Tag Strategy

All meta tags managed in `layout/theme.liquid`.

### Title Tags

Case statement in `<title>` by `template.name`:

| Page Type | Format |
|---|---|
| Homepage (`index`) | `Barreletics — Performance Skins for Barre, Pilates & Reformer` |
| Product | `{{ product.title }} \| Barreletics` |
| Collection | `{{ collection.title }} \| Barreletics Grippy Shoes` |
| Article | `{{ article.title }} \| Barreletics Journal` |
| Blog | `{{ blog.title }} \| Barreletics Journal` |
| Page | `{{ page.title }} \| Barreletics` |
| Other | `{{ page_title }} \| Barreletics` |

### Meta Description

```liquid
{%- if page_description -%}
  <meta name="description" content="{{ page_description | escape }}">
{%- endif -%}
```

Only output when `page_description` is non-empty. Content comes from Shopify admin (product description, collection description, page SEO fields).

### Canonical URL

```liquid
<link rel="canonical" href="{{ canonical_url }}">
```

Shopify's `canonical_url` object handles deduplication (removes query params, pagination, etc.).

---

## Open Graph

All OG tags in `layout/theme.liquid`. Present on every page:
- `og:site_name` → "Barreletics"
- `og:url` → `{{ canonical_url }}`

Contextual by `template.name`:

| Page Type | og:type | og:title | og:description | og:image | Extras |
|---|---|---|---|---|---|
| Product | `product` | `product.title` | `product.description` (200 chars) | Product featured image (1200w) | `og:price:amount`, `og:price:currency` |
| Article | `article` | `article.title` | `article.excerpt_or_content` (200 chars) | Article image (1200w) | — |
| Collection | `website` | `collection.title` | `collection.description` (200 chars) | Collection image (1200w) | — |
| Blog | `blog` | `blog.title` | `page_description` | Fallback | — |
| Other | `website` | `page_title` | `page_description` (if exists) | Fallback | — |

**Fallback OG image:** `{{ 'og-default.jpg' | asset_url }}` — used on pages without a specific image (not product, article, or collection).

---

## Twitter Cards

```liquid
<meta name="twitter:card" content="summary_large_image">
```

Single tag, all pages. Inherits OG title/description/image for the card display.

---

## Breadcrumb Navigation

**File:** `snippets/breadcrumb.liquid`

Combines visual breadcrumb (`<nav>` with `<ol>`) and BreadcrumbList JSON-LD in a single snippet. Hidden on homepage (`template == 'index'`).

### Path structures

| Page Type | Breadcrumb Path |
|---|---|
| Collection (standard) | Home › {Collection Title} |
| Collection (sub: `open-sole`, `closed-sole`, `outdoor`) | Home › Grippy Shoes › {Collection Title} |
| Product (under sub-collection) | Home › Grippy Shoes › {Collection Title} › {Product Title} |
| Product (under standard collection) | Home › {Collection Title} › {Product Title} |
| Product (no collection) | Home › Grippy Shoes › {Product Title} |
| Article | Home › Journal › {Article Title} |
| Blog | Home › Journal |
| Page | Home › {Page Title} |
| Search | Home › Search |
| Cart | Home › Cart |

Sub-collections (`open-sole`, `closed-sole`, `outdoor`) receive an extra "Grippy Shoes" parent crumb linking to `/collections/grippy-shoes`. Product pages inherit the hierarchy from their primary collection (first in `product.collections`).

### Visual styling

- Font: `var(--text-sm)`, `var(--text-muted)` color
- Separator: `›` character with `var(--space-2)` margins
- Current item: `var(--color-charcoal)`, `font-weight: 500`
- Links: `min-height: 44px` (touch target), hover darkens to charcoal
- Accessible: `aria-label="Breadcrumb"`, `aria-current="page"` on current item

---

## GEO Content

**Files:** `sections/geo-section.liquid`, `snippets/geo-section.liquid`
**Decision:** D-022

### Purpose

GEO (Generative Engine Optimization) sections render accordion Q&A blocks optimized for AI crawlers and LLM retrieval. Positioned below primary content. Used on Homepage, Collection, and PDP templates.

### Implementation

Section version (`sections/geo-section.liquid`) uses Shopify section blocks (`type: 'geo_item'`) with `question` (text) and `answer` (richtext) settings. Snippet version (`snippets/geo-section.liquid`) accepts an `items` array parameter.

Both output:
1. Visual accordion (`.geo-section__item` as `<details>` elements)
2. `FAQPage` JSON-LD structured data (only when blocks/items exist)

### Content Requirements (from Doc 12)

- Premium editorial content — not keyword stuffing
- City/state references with local studio context
- Discipline-specific moves (verified terminology from Doc 07 Appendix A)
- Internal links to relevant products
- Local SEO keywords

### Styling

- Container: max-width 900px, centered
- Eyebrow heading: `var(--text-sm)`, uppercase, `var(--tracking-widest)`, muted
- Items: bordered top with `#eee8de`, 12px trigger font-size, muted color `#9a9182`
- Expand/collapse: `+` / `−` indicator via CSS `::after`

---

## Technical SEO

| Concern | Implementation |
|---|---|
| robots.txt | Shopify native (auto-generated) |
| Sitemap | Shopify native (`/sitemap.xml`) |
| Canonical URL | `<link rel="canonical" href="{{ canonical_url }}">` on every page |
| Preconnects | `fonts.googleapis.com`, `fonts.gstatic.com`, `cdn.shopify.com`, `googletagmanager.com`, `connect.facebook.net` |
| Search Console | Meta verification tag via `settings.search_console_verification` |
| hreflang | Not needed (single language at launch) |

---

## Cross-References

- Doc 12 (SEO & GEO Standards) — keyword targets, URL structure, content requirements
- Doc 17 (Judge.me Architecture) — `aggregateRating` in Product schema
- Doc 16 (Integration Architecture) — Search Console verification setting
- `planning/12-seo-geo-standards.md` — full SEO strategy and GEO content patterns
