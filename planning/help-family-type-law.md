# Help-family type law (HARD)

**Date:** 2026-08-12 · Andrew letter  
**Surfaces:** Help hub · FAQ · Shipping & returns (policy) · Returns portal · Size chart · Contact  
**Decide board:** `docs/HELP-OPEN-ME.html` · Cloud: `planning/cloud-prompt-help-family-2026-08-12.md`

## Roles

| Role | Spec | Use |
|---|---|---|
| **Page H1** | `clamp(32px, 4vw, 44px)` / **400** / lh 1.15 / ls −0.028em | Same as Help v8 “How Can We Help?” |
| **Section H2** | Type OS **h2-standard** (`clamp(26–32)` / **600**) | How to start a return · Need a hand? · Size Chart · Fit Tips |
| **Body / lede** | Type OS body / lede | Customer voice only — no internal notes |
| **Labels / eyebrows** | 11 / 600 / uppercase / rust | Marketing OK · **not** Help hub card taxonomy |

## Forbidden

- `type-hero` / homepage hero **72 / 700** on Help-family **page titles**
- Track Order on Help hub or returns portal
- Fake Returns Portal mock as live destination
- Contact → Contact Definitive-v1 (use M4 `/pages/contact-us-form`)
- “S coming soon” on Help size card
- Pool / “fully enclosed”

## Destinations (Help hub)

| Tile | Target |
|---|---|
| FAQ | FAQ Definitive-v7 (until M4 FAQ rebuilt) |
| Shipping & returns | M4 `/pages/returns` |
| Start a return | M4 ReturnZap `/pages/returns-portal` |
| Size chart | M4 size chart handle |
| Contact | M4 `/pages/contact-us-form` |

## Liquid touchpoints

- `sections/page-faq.liquid` · `templates/page.faq.json` — FAQ Definitive-v7 quiet (support H1 · underline search · hairline topics · rule rows)
- `sections/page-returns.liquid` · `sections/page-contact.liquid` · `sections/page-size-guide.liquid` · `sections/main-page.liquid` (portal)
- Templates: `page.returns.json` lede · `page.performance-skins-size-chart.json` / `page.size-chart.json`
