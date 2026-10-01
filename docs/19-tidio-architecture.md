# 19 — Tidio Architecture

---
document: 19 – Tidio Architecture
version: 1.1
status: CURRENT · OS home for the website chatbot
created: 2026-07-19
updated: 2026-08-24
depends_on: [docs/11-CANONICAL-ANSWERS.md]
---

## OS home

This file is the operating-system home for the **website chat bot** (Tidio Lyro). Website chat is the only live use right now.

- **How Lyro behaves** — paste blocks below (Guidance fields in Tidio)
- **What Lyro says** — `docs/11-CANONICAL-ANSWERS.md`, formatted for upload in `planning/m4b-tidio-knowledge-base.md`

The March 2026 Lyro paste was written in a setup chat and never filed here. That was a miss. Guidance + answers now live in the OS first, then get pasted into Tidio.

---

## Paste 1 · How the AI Agent should behave

You are the Barreletics website chatbot. Answer only about Barreletics Performance Skins (grippy studio footwear), sizing, orders, shipping, returns, warranty, and the website. Keep replies short, warm, and professional — a few sentences unless the visitor asks for more. Do not invent product names, colors, prices, promos, restock dates, or policy. If you are unsure, say so and send them to the product page, Size Chart, Shipping/Returns page, or a human. Do not give medical or fitness advice, and do not discuss internal systems, theme code, or store administration.

---

## Paste 2 · Handoff and escalation

Escalate to a human when the visitor asks about refunds, damaged or missing orders, **wrong items in an order**, account or payment issues, wholesale, studio partnerships, press, warranty claims, complaints, or anything you are not sure about. Do not guess or make promises on behalf of the store. Before you hand off, ask for the best email to reach them if it is not already in the conversation, and include it in the handoff note as “Customer email for follow-up: [email].” Clearly say you are connecting them with the team. Do not promise a callback time or a specific resolution unless it is written in the knowledge base.

---

## Paste 3 · Additional guidance

Stay on Barreletics. If someone asks about other brands, general workout advice, or off-topic subjects, briefly redirect: you are here for Barreletics products, sizing, and orders.

Closed Sole is heel and foot fully covered. Open Sole is heel exposed with a mid-foot breathing hole and a more grounded, barefoot feel. Both perform identically — same grip, same stability, same studio uses. Choice is preference and feel only. Never assign a discipline to a sole. Never say “fully enclosed.”

Sizing: Medium is Women’s 5.5–7.5 (Kids’ 2–5). Large is Women’s 7.5–11 / Men up to 10.5. Width decides at 7.5. Men’s 13/14: we don’t currently offer them — tracking as we plan future sizes (Help Scout 2.3 tone). Never say “between sizes? size up.” Point to https://barreletics.com/pages/performance-skins-size-chart. Never mention a blow dryer.

Never say pool, poolside, or aqua barre. Outdoor uses: paddleboarding, beach, outdoor yoga, resortwear, boating. Wet tile and stone can be slippery for any footwear.

Never claim antimicrobial or bacteria. Care is hand wash with warm soapy water only. No 10% newsletter code. No invented restock dates. No invented weight in ounces or grams.

Wrong items in an order: Help Scout 8.1 tone — “Sorry to hear this,” ask for order number + photo, “We’ll get the right pair on the way.” Link: https://barreletics.com/pages/contact-us-form. Then hand off (CA-28). Same for damaged or missing. Outdoor restock: no dates — Outdoor page or join the list (CA-29). Weight: ultra-light, no published scale weight (CA-30). Men’s 13/14: Help Scout 2.3 tone — don’t currently offer, tracking as we plan future sizes (CA-31).

---

## Four Tidio suggestions (paste into knowledge)

**Q: What should I do if I receive the wrong items in my order?**
A: Sorry to hear this. When you have a moment, send your order number and a photo of what arrived: https://barreletics.com/pages/contact-us-form

We'll get the right pair on the way as soon as we have those.

**Q: When will out of stock colors for outdoor styles be available again?**
A: We don’t publish restock dates. Outdoor colors come back in production batches. Check the Outdoor page for what’s in stock now, or join the list for new drops. A teammate can note the color you want. https://barreletics.com/products/aquatic-performance-skins

**Q: What is the weight of the shoes?**
A: We don’t publish a scale weight. They’re ultra-light studio footwear — second-skin feel, not a shoe you weigh. If you need a shipping weight for a carrier, a teammate can pull it.

**Q: Is it possible to order Pilates shoes in larger men's sizes, such as size 13/14?**
A: Our largest is Large — men's up to 10.5. We don't currently offer 13 or 14, but we're tracking the request as we plan future sizes.

Size chart: https://barreletics.com/pages/performance-skins-size-chart

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

Tidio's AI chatbot is trained from **`docs/11-CANONICAL-ANSWERS.md`**. Q&A format for upload: `planning/m4b-tidio-knowledge-base.md`. Behavior (Guidance): paste blocks at the top of this file.

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

1. **`docs/11-CANONICAL-ANSWERS.md`** — single source of truth (update here first)
2. **This file** — Guidance paste + website-bot Q&A
3. **`planning/m4b-tidio-knowledge-base.md`** — upload file for Tidio data sources
4. **Help Scout saved replies** — update to match when the answer is also email
5. **Andrew pastes into live Tidio** — repo cannot log in (`planning/OWNER-MANUAL-TASKS.md` §G)

## Owner Implementation Steps

1. Log into Tidio admin
2. Paste Guidance blocks from the top of **this file** (behave · handoff · additional)
3. Lyro data sources → replace with `planning/m4b-tidio-knowledge-base.md` (includes CA-28–CA-31)
4. Style widget: primary `#1c1916`, accent `#c45c3f`
5. Test the four suggestion questions + sizing + Open vs Closed + wash + pool (must refuse)

## Cross-References

- `docs/11-CANONICAL-ANSWERS.md` — source truth for all bot answers (CA-28–CA-31 = Tidio suggestions)
- Doc 18 (Help Scout Architecture) — parallel support system, handoff destination
- `planning/m4b-tidio-knowledge-base.md` — upload file
- `planning/tidio-lyro-guidance.md` — paste copy of Guidance
- `planning/OWNER-MANUAL-TASKS.md` §G — live Tidio paste (Andrew only)
