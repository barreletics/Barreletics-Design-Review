# 17 — Judge.me Architecture

---
document: 17 – Judge.me Architecture
version: 1.0
status: Draft
created: 2026-07-19
depends_on: [06-design-tokens]
decision_refs: [D-025, D-006]
---

## Overview

Judge.me is used as a **data source only** (D-025). All review rendering uses Barreletics design tokens and custom Liquid templates. Judge.me's default app blocks and widgets are disabled — the theme handles all display.

## Data Flow

Judge.me syncs review data to Shopify metafields:

| Metafield | Namespace | Key | Type | Liquid Access |
|---|---|---|---|---|
| Average Rating | `judgeme` | `average_rating` | float | `product.metafields.judgeme.average_rating` |
| Review Count | `judgeme` | `review_count` | integer | `product.metafields.judgeme.review_count` |

These metafields are read by:
- `sections/pdp-reviews.liquid` — aggregate stats display
- `sections/pdp-buy-box.liquid` — Product JSON-LD `aggregateRating`

Individual reviews are fetched client-side via the Judge.me public API:
```
https://judge.me/api/v1/reviews?shop_domain={{ shop.permanent_domain }}&product_handle={handle}&per_page=6
```

## Review Card Component

**File:** `snippets/review-card.liquid`
**Usage:** `{% render 'review-card', review: review_object %}`

### Expected `review` object properties

| Property | Type | Required |
|---|---|---|
| `rating` | integer (1–5) | Yes |
| `title` | string | No |
| `body` | string | Yes |
| `author` | string | Yes |
| `location` | string | No |
| `date` | date | No |
| `photo` | image URL | No |

### Rendering

- **Stars:** Filled `★` / empty `☆` using `--accent-stars` (gold, `#d4af37`). 14px font-size, 0.12em letter-spacing. Empty stars at `opacity: 0.3`.
- **Title:** `.review-card__title` — `var(--text-lg)`, `var(--weight-bold)`, `var(--text-primary)` color.
- **Body:** `.review-card__body` — `var(--text-base)`, `font-style: italic`, `var(--text-body)` color, `var(--leading-relaxed)` line-height.
- **Photo:** Optional. 200×200 max, `object-fit: cover`, `var(--radius-gallery)` border-radius, lazy loaded.
- **Footer:** `.review-card__footer` — flex row with author (13px bold), location (12px muted), date (12px muted).

### Card styling

- Border: `1px solid #e6e6e6`
- Border-radius: `var(--radius-card)` (12px per D-006)
- Padding: `var(--space-7)` (desktop), `var(--space-5)` (mobile ≤768px)
- Background: `var(--bg-primary)`
- Layout: flex column with `var(--space-3)` gap

### Schema.org markup

Each card outputs `itemscope itemtype="https://schema.org/Review"` with `itemprop` attributes: `reviewRating`, `name`, `reviewBody`, `author`, `datePublished`.

## PDP Reviews Section

**File:** `sections/pdp-reviews.liquid`

### Aggregate stats

Reads `product.metafields.judgeme.average_rating` and `product.metafields.judgeme.review_count`. Assigns:
```liquid
{% assign jm_rating = product.metafields.judgeme.average_rating | default: nil %}
{% assign jm_count  = product.metafields.judgeme.review_count | default: 0 %}
{% assign has_reviews = false %}
{% if jm_count > 0 and jm_rating %}
  {% assign has_reviews = true %}
{% endif %}
```

Displays: `"{rating} out of 5 · {count} reviews"` or `"No reviews yet — be the first!"` fallback.

### Featured reviews

Merchant-curated via section blocks (`type: 'featured_review'`). Each block has settings: `title`, `body`, `author`, `verified` (checkbox), `bg_gradient`. Rendered in a 2-column grid card with alternating media/content order on even items.

### Community reviews

Client-side JS fetches from Judge.me API, renders cards using the same `.review-card` class structure as the Liquid snippet. States:
- **Loading:** "Loading reviews…" placeholder (centered, spans grid)
- **Empty:** "No community reviews yet. Be the first to share your experience!"
- **Error:** "Reviews are temporarily unavailable. Please check back soon."
- **Success:** 3-column grid (2-col on tablet, 1-col on mobile)

### "Write a Review" link

Links to `https://judge.me/reviews/{product.handle}/new` (opens new tab with `rel="noopener"`).

## Structured Data (Product JSON-LD)

**File:** `sections/pdp-buy-box.liquid` (bottom of file)

```liquid
{% assign jm_rating_schema = product.metafields.judgeme.average_rating %}
{% assign jm_count_schema  = product.metafields.judgeme.review_count | plus: 0 %}
```

The Product JSON-LD conditionally includes `aggregateRating`:

```json
{% if jm_rating_schema and jm_count_schema > 0 %}
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": {{ jm_rating_schema }},
  "reviewCount": {{ jm_count_schema }}
}
{% endif %}
```

**Fallback:** When `jm_count_schema == 0` or `jm_rating_schema` is nil, the `aggregateRating` block is omitted entirely from the JSON-LD. No empty/zero ratings are output.

## Disabled Judge.me Defaults

All Judge.me default rendering is disabled:
- Judge.me app blocks: not added to any template JSON
- Judge.me widget JS/CSS: not loaded by theme
- Judge.me badge/star widgets: replaced by custom `.pdp-buy__stars` in buy box
- Judge.me review form: external link to `judge.me/reviews/{handle}/new`

The theme loads zero Judge.me frontend assets. Only the metafield sync and public API are used.

## Cross-References

- Doc 06 (Design Tokens) — `--accent-stars`, `--radius-card`, `--space-7` definitions
- Doc 20 (SEO Architecture) — Product structured data with `aggregateRating`
- D-025 — Decision: Judge.me as data source only, custom rendering
- D-006 — Decision: 12px border-radius on cards
