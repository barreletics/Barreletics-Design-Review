# 15 — Collection Performance Dashboard

**Purpose:** Measure merchandising health of Shopify collections and landing paths.  
**Audience:** Marketing, Founder.  
**Related:** Collection architecture (`planning/09-collection-architecture.md`), [14](./14-product-performance-dashboard.md), [16](./16-conversion-funnel-dashboard.md), Growth Engine (by name).

---

## Scope

Collections include core footwear groupings, seasonal, New Arrivals, campaign LPs that use collection templates, and discipline-oriented sets — per Doc 09 patterns when applicable.

---

## KPI set

### Collection sessions / views

| Field | Value |
|-------|-------|
| **Definition** | Traffic to collection paths |
| **Formula** | Sessions or `view_item_list` / page views by `pagePath` or collection handle |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Collection → PDP click rate

| Field | Value |
|-------|-------|
| **Definition** | Browse engagement |
| **Formula** | PDP views from collection ÷ Collection views *(approximate via pathing or events)* |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Collection conversion rate

| Field | Value |
|-------|-------|
| **Definition** | Purchases attributed to collection landing or view_item_list journey |
| **Formula** | Orders from sessions that viewed collection ÷ Collection sessions *(define attribution path clearly in report)* |
| **Data source** | GA4 (+ Shopify for order truth) |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Collection net sales

| Field | Value |
|-------|-------|
| **Definition** | Sales of products in collection *(not the same as landing attribution)* |
| **Formula** | Sum net sales of member products |
| **Data source** | Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Paid landing efficiency

| Field | Value |
|-------|-------|
| **Definition** | For UTM landings on a collection URL — Shopify revenue ÷ spend |
| **Formula** | Shopify net sales with landing/campaign UTM ÷ Spend |
| **Data source** | Shopify + Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly when campaigns active |
| **Target** | Per [11](./11-roas-measurement-framework.md) |

---

## Merchandising health checks

| Check | Bad signal | Action |
|-------|------------|--------|
| OOS in grid | Many sold-out tiles above fold | Reorder or hide |
| Weak PDP CTR | High views, low PDP | Imagery / sorting |
| High bounce paid LP | Sessions without ATC | Message match / webview |
| Cannibalizing collections | Overlapping SKUs confusing IA | Nav / Doc 09 cleanup |

---

## Category Creation

Collections should reinforce “why grip socks at all?” where copy allows — not generic sock grids. SEO Platform / Growth Engine own content; Analytics tracks outcomes.

---

## Cross-links

- Product → [14](./14-product-performance-dashboard.md)  
- Funnel → [16](./16-conversion-funnel-dashboard.md)  
- GA4 pages → [06](./06-ga4-measurement-plan.md)  
- Planning → `planning/09-collection-architecture.md`
