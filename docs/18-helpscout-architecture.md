# 18 — Help Scout Architecture

---
document: 18 – Help Scout Architecture
version: 1.0
status: Draft
created: 2026-07-19
depends_on: [07-product-knowledge-base, 08-copy-guide, 13-knowledge-architecture]
---

## Overview

Help Scout Beacon provides the customer support widget. Integrated via `snippets/helpscout-beacon.liquid`, loaded before `</body>` in `layout/theme.liquid`. Controlled entirely by `settings.helpscout_beacon_id` — if blank, zero output (graceful degradation).

## Widget Integration

**File:** `snippets/helpscout-beacon.liquid`
**Setting:** `helpscout_beacon_id`
**Placement:** Before `</body>` via `{% render 'helpscout-beacon' %}` in `theme.liquid`

### Script Loading

Help Scout Beacon v2 SDK loaded async on window `load` event from `https://beacon-v2.helpscout.net`. SDK is loaded via an IIFE that creates the `Beacon` function immediately (for queuing commands) and defers actual script load until the page finishes loading.

### Initialization

```liquid
window.Beacon('init', {{ settings.helpscout_beacon_id | json }});
```

### Customer Identification

If a Shopify customer is logged in (`{% if customer %}`), the widget identifies them:

```liquid
window.Beacon('identify', {
  name: {{ customer.name | json }},
  email: {{ customer.email | json }}
});
```

This associates Help Scout conversations with the customer's identity — support agents see the customer name and email without asking.

## Beacon Styling

Widget appearance (position, color, icon, greeting) is configured in **Help Scout admin**, not in theme code. Per `planning/m4b-helpscout-alignment.md`:

| Setting | Value |
|---|---|
| Position | Bottom-right |
| Color | `#1c1916` (brand charcoal) |
| Icon | Chat bubble (default) |
| Greeting | "Need help finding your perfect fit?" |
| Pages shown | All pages |
| Pages hidden | Checkout (Shopify handles separately) |
| Contact form | Name, Email, Subject, Message |
| Knowledge Base link | `/pages/faq` |

## Saved Reply Alignment

Doc 07 (Product Knowledge Base) is the single source of truth for all product information. Help Scout saved replies contain the exact approved copy from Doc 07, formatted for customer support responses.

**Saved replies defined in `planning/m4b-helpscout-alignment.md`:**

| # | Topic | Trigger |
|---|---|---|
| 1 | Sizing & Fit | Customer asks about sizing |
| 2 | Shipping Information | Delivery times, costs, international |
| 3 | Returns & Exchanges | Return policy, exchange process |
| 4 | Warranty Claims | Manufacturing defect reports |
| 5 | Product Care | Cleaning, washing, maintenance |
| 6 | Open Sole vs Closed Sole | Style comparison |
| 7 | Wholesale/Partner Inquiry | Business partnerships |
| 8 | Order Status / Tracking | Where is my order |
| 9 | Discount Codes / Promotions | Deals, code issues |
| 10 | Performance Skins vs Grip Socks | Differentiation |

## Contact Form Routing

Managed entirely in Help Scout admin mailbox settings. Theme does not control form fields or routing rules. Email forwarding: Shopify admin → Settings → Notifications → Customer email → Help Scout inbox.

## Knowledge Base Update Cascade

When Doc 07 (Product Knowledge Base) is updated:

1. **Doc 07** — single source of truth (update here first)
2. **Website copy** — update any affected pages/sections
3. **Help Scout saved replies** — update replies to match new approved copy
4. **Tidio Q&A pairs** — update AI training data to match

See Doc 13 (Knowledge Architecture) for the full cascade process and responsibility matrix.

## Owner Implementation Steps

1. Log into Help Scout admin
2. Manage → Saved Replies → create each reply from `planning/m4b-helpscout-alignment.md`
3. Set up email forwarding: Shopify admin → Settings → Notifications → Customer email → Help Scout inbox
4. Configure Beacon appearance in Help Scout admin (colors, position, greeting)
5. Enter Beacon ID in Theme Customizer → Tracking & Integrations → Help Scout Beacon ID
6. Test: submit contact form → verify arrives in Help Scout → verify saved reply formatting

## Cross-References

- Doc 07 (Product Knowledge Base) — source truth for all support content
- Doc 13 (Knowledge Architecture) — update cascade process
- Doc 16 (Integration Architecture) — snippet placement and guard pattern
- Doc 19 (Tidio Architecture) — parallel chat integration, same knowledge source
- `planning/m4b-helpscout-alignment.md` — full saved reply content
