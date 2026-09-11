# Earmark — Email me when back in stock (no dedicated BIS app if possible)

**Status:** TODO / decide stack (parked 2026-09-11). Andrew asked if we can build ourselves.

## Goal
On OOS variants (PDP buy box / size pills): **Notify me when in stock** — capture email, email when that variant restocks.

## What theme can do alone
- Show the form when variant is sold out
- Validate email + variant id
- Submit somewhere

Theme **cannot** by itself watch inventory and send email. Needs a backend.

## Preferred paths (lightest first)
1. **Klaviyo Back in Stock** (likely best if lifecycle email already on Klaviyo) — theme form → Klaviyo; they send on restock. Barreletics Email sibling owns lifecycle; coordinate there.
2. **Shopify Flow + customer / metaobject waitlist** — more DIY; workable on higher plans; more glue.
3. **Custom** webhook `inventory_levels/update` + store waitlist + send via ESP — heaviest; only if 1–2 fail.

## Do NOT (unless Andrew insists)
- Another single-purpose BIS app if Klaviyo already covers it
- Fake “we’ll email you” with no connected ESP

## PDP notes
- Buy box already has sold-out / Coming soon size states — BIS CTA plugs in there
- One-offs: do not hide sold-out sizes (existing lock)

## Related
- `planning/earmark-cart-drawer-upsell.md`
- Barreletics Email agent for ESP / Klaviyo wiring
