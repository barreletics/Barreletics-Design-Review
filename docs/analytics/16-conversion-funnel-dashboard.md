# 16 — Conversion Funnel Dashboard

**Purpose:** Diagnose session → purchase drop-offs, especially Paid Social mid-funnel.  
**Audience:** Marketing, Founder.  
**Related:** [06](./06-ga4-measurement-plan.md), [05](./05-meta-ads-reporting-framework.md), `docs/15-analytics-architecture.md`.

---

## Canonical funnel stages

```
Sessions → PDP view (view_item) → Add to cart → Begin checkout → Purchase (Shopify)
```

Homepage landings may skip PDP; always segment by **landing page type**.

---

## KPI set

### Session → ATC rate

| Field | Value |
|-------|-------|
| **Definition** | Mid-funnel engagement |
| **Formula** | Sessions with `add_to_cart` ÷ Sessions |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Daily (when diagnosing) / Weekly |
| **Target** | TBD — set from 90-day baseline |

### ATC → Checkout rate

| Field | Value |
|-------|-------|
| **Definition** | Cart intent to checkout |
| **Formula** | `begin_checkout` ÷ `add_to_cart` (users or events — label) |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Checkout → Purchase rate

| Field | Value |
|-------|-------|
| **Definition** | Checkout completion |
| **Formula** | Purchases ÷ `begin_checkout`  
*Reconcile purchases to Shopify order count* |
| **Data source** | GA4 + Shopify |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Overall CVR

| Field | Value |
|-------|-------|
| **Definition** | End-to-end conversion |
| **Formula** | Shopify Orders ÷ Sessions (state session source) |
| **Data source** | Shopify + GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

### Abandoned checkout rate

| Field | Value |
|-------|-------|
| **Definition** | Checkouts not completed |
| **Formula** | Abandoned checkouts ÷ (Abandoned + Completed) or Shopify abandon report |
| **Data source** | Shopify |
| **Owner** | Marketing / CS |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline |

---

## Diagnostic segments (required when Paid Social weak)

| Segment | Why |
|---------|-----|
| Channel = Paid Social | Primary paid path |
| Landing = `/` vs PDP/collection | Homepage ATC death pattern |
| Mobile Safari / in-app browser | Webview checkout risk |
| Device = mobile | Majority Meta traffic |

### KPI: Paid Social ATC rate vs sitewide

| Field | Value |
|-------|-------|
| **Definition** | Relative mid-funnel health of paid traffic |
| **Formula** | Paid Social ATC rate ÷ Sitewide ATC rate |
| **Data source** | GA4 |
| **Owner** | Marketing |
| **Reporting cadence** | Weekly |
| **Target** | TBD — set from 90-day baseline; investigate if Paid Social ATC collapses |

---

## Red-flag playbook

| Symptom | Likely area | Next doc / action |
|---------|-------------|-------------------|
| Sessions OK, ATC dies | PDP, size, price, webview | Creative/LP match; webview skill |
| ATC OK, checkout dies | Cart friction, shipping threshold ($150) | Cart UX / threshold messaging |
| Checkout OK, purchase dies | Payment, Shop Pay, trust | Shopify abandons; gateway null check |
| Meta IC ≫ Purchase | Pixel/CAPI | Attribution ([04](./04-marketing-attribution-framework.md)) |

---

## Cross-links

- GA4 → [06](./06-ga4-measurement-plan.md)  
- Meta → [05](./05-meta-ads-reporting-framework.md)  
- Ecommerce defs → [03](./03-ecommerce-kpi-definitions.md)  
- Executive → [01](./01-executive-kpi-dashboard.md)
