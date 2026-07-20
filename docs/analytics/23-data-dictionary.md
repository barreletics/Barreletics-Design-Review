# 23 — Data Dictionary

**Purpose:** Canonical names, systems, and filters for Barreletics analytics.  
**Audience:** Anyone pulling or reporting numbers.  
**Related:** [24](./24-metric-governance.md), [04](./04-marketing-attribution-framework.md).

---

## Systems

| System | ID / note | Role |
|--------|-----------|------|
| Shopify Admin | barreletics.com store | Revenue / orders / inventory / customers truth |
| GA4 | Property `300437005` | Sessions, events, directional revenue |
| Blend | Connected ad accounts | Spend & platform metrics (Meta, Google, Pinterest, etc.) |
| Meta Ads / Events Manager | Business Manager | Auction + claimed conversions |
| Google Search Console | Domain property | Brand / SEO demand |
| Help Scout | Support | CS / wholesale inquiry tags |
| Email ESP | As configured | Email sends / attributed sales (reconcile to Shopify) |

---

## Core commerce fields

| Term | Definition | Formula / mapping | Source | Owner | Cadence | Target |
|------|------------|-------------------|--------|-------|---------|--------|
| `net_sales` | Shopify Net sales | Per Shopify Analytics | Shopify | Founder | Daily | See [03](./03-ecommerce-kpi-definitions.md) |
| `orders_paid` | Paid order count | Count paid orders | Shopify | Founder | Daily | TBD — set from 90-day baseline |
| `aov` | Average order value | `net_sales` ÷ `orders_paid` | Shopify | Marketing | Daily | TBD — set from 90-day baseline |
| `units_sold` | Units | Sum line quantities | Shopify | Ops | Weekly | TBD — set from 90-day baseline |
| `new_customer` | First-time buyer | First paid order in period | Shopify | Marketing | Weekly | TBD — set from 90-day baseline |
| `refund_rate` | Refund pressure | Refund $ ÷ `net_sales` | Shopify | CS | Weekly | TBD — set from 90-day baseline |

---

## Traffic & GA4 fields

| Term | Definition | GA4 API mapping | Source | Owner | Cadence | Target |
|------|------------|-----------------|--------|-------|---------|--------|
| `sessions` | Sessions | metric `sessions` | GA4 | Marketing | Daily | TBD — set from 90-day baseline |
| `active_users` | Users | metric `activeUsers` | GA4 | Marketing | Weekly | TBD — set from 90-day baseline |
| `ga4_total_revenue` | GA4 revenue | metric `totalRevenue` | GA4 | Marketing | Weekly | Directional only |
| `channel_group` | Default channel | dim `sessionDefaultChannelGroup` | GA4 | Marketing | Weekly | Benchmarks below |
| `rev_per_session` | Monetization density | `ga4_total_revenue` ÷ `sessions` | GA4 | Marketing | Weekly | Organic ~$2.21; Email ~$2.25; Paid Social ~$0.74 |
| `page_path` | URL path | dim `pagePath` | GA4 | Marketing | Weekly | — |
| `country` | Geo | dim `country` | GA4 | Marketing | Monthly | GEO input |

---

## Paid media fields

| Term | Definition | Formula / mapping | Source | Owner | Cadence | Target |
|------|------------|-------------------|--------|-------|---------|--------|
| `spend` | Media cost | Sum spend | Blend | Marketing | Daily | Budget |
| `impressions` | Impressions | Sum | Blend | Marketing | Daily | — |
| `link_clicks` | Clicks (consistent def) | Sum link clicks | Blend | Marketing | Daily | — |
| `cpm` | Cost per mille | (spend ÷ impressions) × 1000 | Blend | Marketing | Daily | TBD — set from 90-day baseline |
| `cpc` | Cost per click | spend ÷ link_clicks | Blend | Marketing | Daily | TBD — set from 90-day baseline |
| `roas_platform` | Platform ROAS | Platform purchase value ÷ spend | Blend/Meta | Marketing | Daily | Diagnostic |
| `roas_shopify_meta` | Decision ROAS | Shopify Meta-UTM net sales ÷ Meta spend | Shopify + Blend | Marketing | Daily | TBD — set from 90-day baseline |
| `cac_blended` | Blended CAC | Paid spend ÷ new customers | Blend + Shopify | Marketing | Weekly | TBD — set from 90-day baseline |

---

## Meta UTM filter aliases (maintain)

Treat as Meta-paid when **medium** indicates paid AND **source** matches (case-insensitive):

| utm_source examples | utm_medium examples |
|--------------------|---------------------|
| `facebook`, `instagram`, `fb`, `ig`, `meta` | `paid_social`, `paid`, `cpc`, `paidsocial` |

Exact production filter list should be versioned here when locked after 90-day audit.

---

## Funnel events

| Term | Definition | Mapping | Source | Owner | Cadence | Target |
|------|------------|---------|--------|-------|---------|--------|
| `view_item` | PDP view | GA4 / theme | GA4 | Marketing | Weekly | TBD — set from 90-day baseline |
| `add_to_cart` | ATC | GA4 event | GA4 | Marketing | Weekly | TBD — set from 90-day baseline |
| `begin_checkout` | Checkout start | GA4 event | GA4 | Marketing | Weekly | TBD — set from 90-day baseline |
| `purchase` | Purchase event | Shopify/Custom Pixel | GA4 + Shopify | Marketing | Weekly | Reconcile to `orders_paid` |

---

## Partnership fields

| Term | Definition | Source | Owner |
|------|------------|--------|-------|
| `wholesale_order` | Order tagged wholesale | Shopify tags | Wholesale |
| `active_studio_partner` | T180 active studio | Tracker | Partnerships |
| `ambassador_code` | Unique discount/UTM | Shopify | Marketing |

---

## Time & currency

| Rule | Value |
|------|-------|
| Timezone | Shopify store timezone |
| Currency | USD |
| Week start | Monday (unless Shopify report forces Sunday — label if so) |

---

## Naming conventions

- Prefer snake_case IDs in docs: `roas_shopify_meta`  
- Always suffix LTV windows: `ltv_180d`  
- Always label revenue source on ROAS/CAC  

Changes → [24](./24-metric-governance.md).
