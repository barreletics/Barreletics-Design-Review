# Shopify Build — Deployment Checklist

## Title Tag Configuration (M-05, M-09)

### Required Metafields

Before deployment, ensure the following metafields are created in Shopify Admin:

| Namespace | Key | Type | Used On | Purpose |
|-----------|-----|------|---------|---------|
| `custom` | `sole_type` | Single-line text | Products | "Open Sole" or "Closed Sole" — used in PDP badge and title tag |

### Title Tag Logic

Update `shopify-build/layout/theme.liquid` title tag at deployment to:

```liquid
{%- case template.name -%}
  {%- when 'index' -%}
    Barreletics — Performance Skins for Barre, Pilates & Reformer
  {%- when 'product' -%}
    {{ product.title }} — {{ product.metafields.custom.sole_type | default: 'Performance Skin' }} | Barreletics
  {%- when 'collection' -%}
    Grippy Shoes for {{ collection.title }} | Barreletics
  {%- when 'article' -%}
    {{ article.title }} | Barreletics Journal
  {%- else -%}
    {{ page_title }} | Barreletics
{%- endcase -%}
```

**Why deferred:** The `sole_type` metafield must exist on all products before the PDP title tag format can be deployed. Deploying the dynamic format without the metafield would produce "Performance Skin" as a default for all products, which is acceptable as a fallback but not ideal.

**M-05:** PDP title tag format — requires `custom.sole_type` metafield on each product.
**M-09:** Collection title tag format — Doc 12 specifies `Grippy Shoes for [Discipline] | Barreletics`. Requires collection titles to follow the naming convention or a dedicated metafield.

### Pre-Deployment Steps

1. Create `custom.sole_type` metafield definition in Shopify Admin → Settings → Custom data → Products
2. Populate `sole_type` for all products ("Open Sole" or "Closed Sole")
3. Verify collection titles follow discipline naming (`Barre`, `Pilates & Reformer`, etc.)
4. Update theme.liquid title tag with the format above
5. Test title tags render correctly across all page types
6. Verify Google Search Console picks up new title formats

### Judge.me Metafields

| Namespace | Key | Type | Used On | Purpose |
|-----------|-----|------|---------|---------|
| `judgeme` | `average_rating` | Decimal | Products | Aggregate star rating (e.g., 4.9) |
| `judgeme` | `review_count` | Integer | Products | Total review count |

These are typically auto-populated by the Judge.me app once installed and configured.
