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

Doc 07 (Product Knowledge Base) is the single source of truth for product **facts**. Help Scout **saved-reply wording** lives in:

**`helpscout-kb/Barreletics_Email_Template_Master.md`** (numbered library: 1.x greetings, 2.x sizing, 3.x returns, …)

`planning/m4b-helpscout-alignment.md` is a short M4B stub — **not** the master.

### Sizing — Save-the-return series (2.x)

| # | Help Scout name | Trigger |
|---|---|---|
| 2.4 | Sizing — Save the return (narrow foot) | Narrow-foot fit before return |
| 2.5 | Sizing — Save the return (wrong size) | Too small / too large before return |
| 2.6 | Sizing — Save the return (torn on first use) | Outdoor (or any) pair tore/broke on first use — offer free replacement + photo + size/width; put-on tip |

**2.6 added 2026-08-11.** Tag: `quality-issue`.

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
2. Manage → Saved Replies → create/update each reply from `helpscout-kb/Barreletics_Email_Template_Master.md` (Name = title after the number)
3. Set up email forwarding: Shopify admin → Settings → Notifications → Customer email → Help Scout inbox
4. Configure Beacon appearance in Help Scout admin (colors, position, greeting)
5. Enter Beacon ID in Theme Customizer → Tracking & Integrations → Help Scout Beacon ID
6. Test: submit contact form → verify arrives in Help Scout → verify saved reply formatting

## Cross-References

- Doc 07 (Product Knowledge Base) — source truth for all support content
- Doc 13 (Knowledge Architecture) — update cascade process
- Doc 16 (Integration Architecture) — snippet placement and guard pattern
- Doc 19 (Tidio Architecture) — parallel chat integration, same knowledge source
- `helpscout-kb/Barreletics_Email_Template_Master.md` — full saved reply content (master)
- `planning/m4b-helpscout-alignment.md` — short M4B stub (not master)
