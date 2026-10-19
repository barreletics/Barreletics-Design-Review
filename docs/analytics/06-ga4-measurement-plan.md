# 06 — Google Analytics 4 Measurement Plan

**Purpose:** What Barreletics measures in GA4, how, and what “good” looks like.  
**Property ID:** `300437005`  
**Site:** barreletics.com  
**Related:** `docs/15-analytics-architecture.md`, [04](./04-marketing-attribution-framework.md), [16](./16-conversion-funnel-dashboard.md).

---

## Role of GA4

GA4 answers: **Who came, from where, what did they do, where did they drop?**  
GA4 does **not** replace Shopify for revenue truth.

| Use GA4 for | Do not use GA4 alone for |
|-------------|--------------------------|
| Sessions, users, geo, device | Final revenue / P&L |
| Channel quality (rev/session) | Paid scale decisions |
| Funnel event rates | Inventory |
| Landing page diagnosis | Wholesale pipeline |

---

## Implementation preference

Shopify native Google & YouTube channel preferred; theme snippets are fallback only. Never dual-fire ([`docs/15-analytics-architecture.md`](../15-analytics-architecture.md)).

---

## Standard report recipes

### Traffic by channel

| Field | Value |
|-------|-------|
| **Definition** | Volume and monetization by default channel group |
| **Formula** | Metrics: `sessions`, `activeUsers`, `totalRevenue` by dimension `sessionDefaultChannelGroup` |
| **Data source** | GA4 `ga_run_report` |
| **Owner** | Marketing |
| **Reporting cadence** | Daily (spot) / Weekly (full) |
| **Target** | Rev/session: Organic Search ~$2.21 · Email ~$2.25 · Paid Social ~$0.74 |

### Traffic by country

| Field | Value |
|-------|-------|
| **Definition** | Geo demand and revenue concentration |
| **Formula** | Same metrics by dimension `country` |
| **Data source** | GA4 |
| **Owner** | Marketing / Founder |
| **Reporting cadence** | Weekly / Monthly |
| **Target** | Inform GEO page qualification (Growth Engine / SEO — by name); no vanity international pages |

### Traffic by date

| Field | Value |
|-------|-------|
| **Definition** | Trend detection |
| **Formula** | Metrics by dimension `date` |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Daily |
| **Target** | N/A |

### Pages

| Field | Value |
|-------|-------|
| **Definition** | Page engagement and associated revenue |
| **Formula** | `screenPageViews`, `totalRevenue` by `pagePath` |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline; PDP and key collection paths prioritized |

---

## Event inventory (business view)

Align with theme/Shopify events:

| Event | Business meaning | Owner check |
|-------|------------------|-------------|
| `page_view` / session | Arrival | Marketing |
| `view_item` | PDP view | Marketing |
| `view_item_list` | Collection browse | Marketing |
| `add_to_cart` | Mid-funnel intent | Marketing |
| `begin_checkout` | Checkout start | Marketing |
| `purchase` | Transaction (Shopify/Custom Pixel — not theme) | Marketing + verify vs Shopify |

Custom: `size_selector_click`, `sticky_atc_click`, `cart_drawer_open` — CRO diagnostics.

### KPI: Funnel step conversion

| Field | Value |
|-------|-------|
| **Definition** | Progression rates between key events |
| **Formula** | See [16](./16-conversion-funnel-dashboard.md) |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

---

## Channel quality scorecard

| Channel | Benchmark rev/session | Interpretation |
|---------|----------------------|----------------|
| Organic Search | ~$2.21 | High value — protect SEO / brand search |
| Email | ~$2.25 | High value — protect list hygiene & flows |
| Paid Social | ~$0.74 | Lower — watch Shopify ROAS carefully |
| Referral | High $/session, low volume | Investigate sources (studios, PR, affiliates) |

### KPI: Revenue per session (by channel)

| Field | Value |
|-------|-------|
| **Definition** | Monetization density of a traffic source |
| **Formula** | `totalRevenue` ÷ `sessions` for channel |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | Hold near benchmarks; investigate material deviations |

---

## Device / browser splits (when diagnosing)

For Meta mid-funnel issues, break ATC and checkout by:

- Device category (mobile/desktop)  
- Browser (Safari vs Chrome)  
- Landing page (`/` vs PDP/collection)

Document findings in weekly pack; do not invent device targets without baseline.

---

## GA4 vs Shopify reconciliation

| Check | Method | Cadence |
|-------|--------|---------|
| Purchase count | GA4 purchases vs Shopify orders | Weekly |
| Revenue | GA4 totalRevenue vs Shopify net sales | Weekly |
| Channel | GA4 Paid Social revenue vs Shopify Meta UTMs | Weekly |

Expect differences (attribution windows, tax, consent, bots). Large unexplained gaps → audit before trusting GA4 for decisions.

---

## Privacy & quality

- Respect consent mode / region requirements as configured in Shopify/GA  
- Filter internal traffic where practical  
- Do not use GA4 debug traffic in executive packs  

---

## Cross-links

- Funnel dashboard → [16](./16-conversion-funnel-dashboard.md)  
- Attribution → [04](./04-marketing-attribution-framework.md)  
- Tech architecture → [`docs/15-analytics-architecture.md`](../15-analytics-architecture.md)  
- SEO Platform (by name) for Search Console / content KPIs
