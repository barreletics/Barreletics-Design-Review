# 05 — Meta Ads Reporting Framework

**Purpose:** How Barreletics reports and governs Meta (Facebook/Instagram) performance.  
**Audience:** Marketing, Founder.  
**Business context:** Fitness / grip footwear DTC; goal = purchases; mid-price (~$74). Meta is typically primary paid channel.  
**Related:** [04](./04-marketing-attribution-framework.md), [11](./11-roas-measurement-framework.md).

---

## Reporting layers

| Layer | Question | Source |
|-------|----------|--------|
| Delivery | Are we buying attention efficiently? | Blend / Meta Ads Manager |
| Creative | Is the ad fatigued or concentrated? | Ad-level Blend / Meta |
| Funnel | Are clicks converting on-site? | GA4 + Shopify |
| Truth ROAS | Did Shopify get paid Meta orders? | Shopify Meta-UTM ÷ spend |
| Platform ROAS | What does Meta claim? | Meta / Blend (diagnostic only) |

---

## Delivery KPIs

### Ad spend (Meta)

| Field | Value |
|-------|-------|
| **Definition** | Meta media cost in period |
| **Formula** | Sum spend |
| **Data source** | Blend `smart_query_meta` / Ads Manager |
| **Owner** | Marketing |
| **Reporting cadence** | Daily |
| **Target** | Within Founder-set budget |

### CPM

| Field | Value |
|-------|-------|
| **Definition** | Cost per 1,000 impressions |
| **Formula** | (Spend ÷ Impressions) × 1000 |
| **Data source** | Blend / Meta |
| **Owner** | Marketing |
| **Reporting cadence** | Daily / Weekly |
| **Target** | TBD — set from 90-day baseline; spike → check auction + creative fatigue |

### CPC

| Field | Value |
|-------|-------|
| **Definition** | Cost per link click (use consistent click definition) |
| **Formula** | Spend ÷ Link clicks |
| **Data source** | Blend / Meta |
| **Owner** | Marketing |
| **Reporting cadence** | Daily |
| **Target** | TBD — set from 90-day baseline |

### CTR (link)

| Field | Value |
|-------|-------|
| **Definition** | Link clicks ÷ impressions |
| **Formula** | Link clicks ÷ Impressions |
| **Data source** | Blend / Meta |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Frequency

| Field | Value |
|-------|-------|
| **Definition** | Average times ads shown per person in audience |
| **Formula** | Impressions ÷ Reach |
| **Data source** | Meta |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline; rising frequency + falling CTR → creative refresh |

---

## Efficiency KPIs

### Meta platform ROAS (diagnostic)

| Field | Value |
|-------|-------|
| **Definition** | Meta-claimed purchase value ÷ spend |
| **Formula** | Meta purchase conversion value ÷ Spend |
| **Data source** | Meta / Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Daily |
| **Target** | Not a P&L target; compare only to Shopify Meta ROAS |

### Shopify Meta ROAS (decision)

| Field | Value |
|-------|-------|
| **Definition** | Shopify net sales with Meta UTMs ÷ Meta spend |
| **Formula** | Shopify Meta-UTM net sales ÷ Meta spend |
| **Data source** | Shopify + Blend |
| **Owner** | Marketing / Founder |
| **Reporting cadence** | Daily / Weekly |
| **Target** | TBD — set from 90-day baseline |

### CPA (Shopify new customers from Meta)

| Field | Value |
|-------|-------|
| **Definition** | Cost to acquire a new customer credited to Meta UTMs |
| **Formula** | Meta spend ÷ New customers with first order Meta-UTM |
| **Data source** | Shopify + Blend |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | See [10](./10-cac-measurement-framework.md) |

---

## Creative & structure KPIs

### Spend concentration

| Field | Value |
|-------|-------|
| **Definition** | Share of spend in top ads |
| **Formula** | Top 3 ads spend ÷ Total Meta spend |
| **Data source** | Blend / Meta |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline; extreme concentration = fatigue risk |

### Learning Limited share

| Field | Value |
|-------|-------|
| **Definition** | Ad sets stuck in Learning Limited |
| **Formula** | Spend in Learning Limited ÷ Total spend |
| **Data source** | Meta |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | Minimize; consolidate structure when chronic |

### Category-creation creative share

| Field | Value |
|-------|-------|
| **Definition** | Share of spend on ads that attack grip-sock category (not generic product-only) |
| **Formula** | Spend on category-creation message class ÷ Meta spend |
| **Data source** | Creative taxonomy sheet + Meta |
| **Owner** | Marketing / Founder |
| **Reporting cadence** | Monthly |
| **Target** | TBD — Founder sets strategic mix |

---

## Weekly Meta review agenda

1. Spend vs budget  
2. Shopify Meta ROAS vs Meta claimed ROAS (gap)  
3. CPM / frequency / CTR movement  
4. Top ads by spend and Shopify-attributed results  
5. Landing destination check (collection/PDP vs homepage traps)  
6. In-app browser / ATC notes if Paid Social mid-funnel weak ([16](./16-conversion-funnel-dashboard.md))  
7. Scale / hold / kill decisions — Founder approves budget changes

---

## Hard rules

1. **Do not** declare Meta “working” from Events Manager Purchase alone.  
2. **Do** reconcile InitiateCheckout vs Purchase anomalies before trusting CAPI.  
3. **Do not** duplicate Pixel + theme pixel ([`docs/15-analytics-architecture.md`](../15-analytics-architecture.md)).  
4. **Do** keep UTM discipline on every ad URL ([04](./04-marketing-attribution-framework.md)).

---

## Cross-links

- Attribution → [04](./04-marketing-attribution-framework.md)  
- ROAS → [11](./11-roas-measurement-framework.md)  
- Funnel → [16](./16-conversion-funnel-dashboard.md)  
- Executive board → [01](./01-executive-kpi-dashboard.md)
