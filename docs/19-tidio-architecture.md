# 19 — Tidio Architecture

---
document: 19 – Tidio Architecture
version: 1.0
status: Draft
created: 2026-07-19
depends_on: [07-product-knowledge-base, 08-copy-guide, 13-knowledge-architecture]
---

## Overview

Tidio provides AI-powered chat support. Integrated via `snippets/tidio-widget.liquid`, loaded before `</body>` in `layout/theme.liquid`. Controlled entirely by `settings.tidio_widget_key` — if blank, zero output (graceful degradation).

## Widget Integration

**File:** `snippets/tidio-widget.liquid`
**Setting:** `tidio_widget_key`
**Placement:** Before `</body>` via `{% render 'tidio-widget' %}` in `theme.liquid`

### Script Loading

Tidio chat JS loaded async from `//code.tidio.co/{{ settings.tidio_widget_key }}.js`. Single script tag — no initialization wrapper needed. Tidio handles widget rendering internally.

### Customer Identification

If a Shopify customer is logged in (`{% if customer %}`), the widget sets contact properties on the `tidioChat-ready` event:

```liquid
document.addEventListener('tidioChat-ready', function() {
  window.tidioChatApi.setContactProperties({
    distinct_id: {{ customer.id | json }},
    email: {{ customer.email | json }},
    name: {{ customer.name | json }}
  });
});
```

This passes `distinct_id`, `email`, and `name` so Tidio associates conversations with the Shopify customer record.

## Knowledge Base Training

Tidio's AI chatbot is trained from Doc 07 (Product Knowledge Base). Content is formatted as Q&A pairs for Tidio's knowledge base system. Full training data defined in `planning/m4b-tidio-knowledge-base.md`.

### Q&A Categories

| Category | Example Questions |
|---|---|
| Product Basics | "What are Performance Skins?", "Are they socks?" |
| Sizing & Fit | "What size should I order?", "Do they stretch?" |
| Product Styles | "Open Sole vs Closed Sole?", "Which style should I get?" |
| Grip & Performance | "How does the grip work?", "Will it wear off?" |
| Materials & Quality | "Where are they made?", "How long do they last?" |
| Care & Maintenance | "How do I wash them?", "Can I use the dryer?" |
| Shipping & Delivery | "How much is shipping?", "Do you ship internationally?" |
| Returns & Warranty | "What's your return policy?", "Do you have a warranty?" |
| Pricing & Promotions | "What's the price?", "Do you have discounts?" |
| Sock Math (Value Prop) | "Are they worth the price vs grip socks?" |

### Q&A Pair Format

Questions use natural customer language ("How do I clean them?"). Answers use the exact approved language from Doc 07, delivered in the brand voice defined in Doc 08 (Copy Guide).

## Conversation Flows

Defined in `planning/m4b-tidio-knowledge-base.md`:

1. **Sizing Help** — Trigger: mentions "size" or "fit" → ask shoe size → recommend → offer Size Guide link
2. **Style Recommendation** — Trigger: mentions "which style" → ask primary activity → recommend Open/Closed Sole
3. **Returns Process** — Trigger: mentions "return" → confirm order number → check eligibility → escalate to Help Scout

## Human Handoff Rules

Configured in Tidio admin. Escalate to Help Scout (human agent) when:

1. Warranty claim (requires photos/investigation)
2. Customer is upset or frustrated
3. Order issue requiring Shopify admin access (cancellation, modification)
4. Wholesale/partnership inquiry (business decision)
5. Question not in the Knowledge Base
6. Customer explicitly requests a person
7. Payment or billing dispute
8. International shipping customs/duties issue

## Conversation Flow Summary

```
Customer message
  → Tidio AI answers from knowledge base
    → If resolved: conversation ends
    → If unresolved or handoff triggered:
      → Route to human agent (Help Scout ticket creation)
```

## Widget Styling

Configured in **Tidio admin**, not in theme code:
- Primary color: `#1c1916` (brand charcoal)
- Accent: `#c45c3f` (brand rust)
- Enabled: all pages except checkout

## Knowledge Base Update Cascade

Same cascade as Doc 18 (Help Scout Architecture):

1. **Doc 07** — single source of truth (update here first)
2. **Website copy** — update affected pages/sections
3. **Help Scout saved replies** — update to match
4. **Tidio Q&A pairs** — update AI training data to match

## Owner Implementation Steps

1. Log into Tidio admin
2. AI Chatbot → Knowledge Base → import Q&A pairs from `planning/m4b-tidio-knowledge-base.md`
3. Configure conversation flows (sizing, style recommendation, returns)
4. Set handoff rules (Tidio → Help Scout)
5. Style widget: primary `#1c1916`, accent `#c45c3f`
6. Enter Widget Key in Theme Customizer → Tracking & Integrations → Tidio Widget Key
7. Test: ask each category of question → verify answer accuracy
8. Test: trigger handoff → verify Help Scout ticket creation

## Cross-References

- Doc 07 (Product Knowledge Base) — source truth for all AI training content
- Doc 08 (Copy Guide) — brand voice for answer formatting
- Doc 13 (Knowledge Architecture) — update cascade process
- Doc 16 (Integration Architecture) — snippet placement and guard pattern
- Doc 18 (Help Scout Architecture) — parallel support system, handoff destination
- `planning/m4b-tidio-knowledge-base.md` — full Q&A training data and flows
