# M4A Metafield Specification

---
document: M4A Metafield Specification
status: 🔵 Ready for Review
created: 2026-07-18
depends_on: [05-pdp-architecture, 07-product-knowledge-base, 12-seo-geo-standards]
---

## Purpose

Complete metafield specification for Shopify admin configuration. Defines namespace, key, type, and usage for all metafields required by the Barreletics theme.

---

## Product Metafields

### Judge.me Review Data (D-025)

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| `judgeme` | `average_rating` | `number_decimal` | Average star rating (0.0–5.0) |
| `judgeme` | `review_count` | `number_integer` | Total number of approved reviews |

**Notes:** These are automatically synced by the Judge.me app. Used in `snippets/review-card.liquid`, `sections/pdp-reviews.liquid`, and `snippets/product-card.liquid` for star display.

### Product Specifications

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| `product` | `sole_type` | `single_line_text_field` | "open" or "closed" — used for filtering |
| `product` | `disciplines` | `list.single_line_text_field` | Applicable disciplines (barre, pilates, reformer, lagree, yoga, outdoor) |
| `product` | `materials` | `multi_line_text_field` | Material composition description |
| `product` | `weight` | `weight` | Product weight for shipping |
| `product` | `country_of_origin` | `single_line_text_field` | Manufacturing country ("USA") |

### Product Marketing

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| `marketing` | `short_description` | `single_line_text_field` | One-line product summary for cards/meta |
| `marketing` | `key_benefit_1` | `single_line_text_field` | Primary benefit statement |
| `marketing` | `key_benefit_2` | `single_line_text_field` | Secondary benefit statement |
| `marketing` | `key_benefit_3` | `single_line_text_field` | Tertiary benefit statement |

---

## Collection Metafields

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| `collection` | `hero_headline` | `single_line_text_field` | Collection hero section headline |
| `collection` | `hero_subheadline` | `single_line_text_field` | Collection hero subheadline |
| `collection` | `pillar_content` | `multi_line_text_field` | SEO pillar content (educational) |
| `collection` | `faq_items` | `json` | FAQ accordion items `[{q, a}]` |

---

## Page Metafields

### GEO Content (D-022)

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| `geo` | `city` | `single_line_text_field` | Target city name |
| `geo` | `state` | `single_line_text_field` | Target state/region |
| `geo` | `content` | `multi_line_text_field` | City-specific editorial content |
| `geo` | `studios` | `list.single_line_text_field` | Notable studios in the area |
| `geo` | `disciplines` | `list.single_line_text_field` | Popular disciplines in the area |

### Page SEO

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| `seo` | `schema_type` | `single_line_text_field` | JSON-LD schema type override |
| `seo` | `canonical_override` | `url` | Override canonical URL if needed |

---

## Shop Metafields (Global)

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| `brand` | `free_shipping_threshold` | `number_integer` | Free shipping threshold in cents (15000 = $150) |
| `brand` | `promo_code` | `single_line_text_field` | Active promo code ("SAVE15") |
| `brand` | `promo_description` | `single_line_text_field` | Promo description ("Buy 2, Save 15%") |

---

## Metafield Definitions (Shopify Admin Setup)

All metafields should be created as **definitions** in Shopify Admin > Settings > Custom data to enable:
- Type validation
- Theme editor visibility
- Bulk import/export
- API access

### Priority Order for Setup

1. **Judge.me metafields** — Required for review display (auto-created by Judge.me app installation)
2. **Product sole_type** — Required for collection filtering
3. **Product disciplines** — Required for discipline-based recommendations
4. **Collection hero fields** — Required for collection page rendering
5. **GEO content fields** — Required for GEO sections
6. **Marketing fields** — Enhancement, can launch without

---

## Implementation Notes

- Judge.me metafields are managed by the Judge.me app — do not manually create or modify
- All `list.*` types support multiple values (comma-separated in admin)
- JSON metafields must validate against expected schema before use in Liquid
- GEO metafields are optional per page — sections gracefully hide when empty
- Product `sole_type` metafield drives the variant-grid filter behavior
