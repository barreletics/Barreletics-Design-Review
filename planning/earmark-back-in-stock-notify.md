# Earmark — Email me when back in stock (Flow + Zapier, no Klaviyo)

**Status:** Post-live project (parked 2026-09-11). After full QC and site live.  
**Andrew:** No Klaviyo. Include **Zapier** in the workflow. Prefer no dedicated BIS app.

## Timing
**After** page QC + go-live. Not a launch blocker.

## Goal
OOS variant on PDP → Notify me when in stock → email when that variant restocks.

## Planned workflow
1. **Theme (us):** sold-out → form (email + variant_id + product URL).
2. **Zapier:** form webhook → store waitlist (Sheet/Zapier Tables) keyed by variant_id.
3. **Restock signal:** Shopify inventory webhook / Flow → Zapier when variant goes 0 → available.
4. **Zapier:** match waitlist rows for that variant → send email (Gmail/Shopify Email/transactional) with PDP link → mark notified / remove row.

Shopify Flow can still help as the inventory trigger if useful; **Zapier owns waitlist + send** so we’re not tied to Klaviyo.

## Theme vs backend
| Layer | Owner |
| --- | --- |
| Form UI | Theme |
| Waitlist + email send | Zapier |
| Inventory trigger | Shopify → Zapier (Flow optional) |

## Do NOT
- Assume Klaviyo
- Ship a fake notify CTA with no Zapier/Flow wiring
- Block go-live on this

## Related
- `planning/earmark-cart-drawer-upsell.md` (cart sequencing separate)
