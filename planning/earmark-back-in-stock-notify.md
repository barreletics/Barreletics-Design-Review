# Earmark — Email me when back in stock (Shopify Flow only)

**Status:** Post-live project (updated 2026-09-11). After full QC and site live.  
**Andrew:** No Klaviyo. **No Zapier.** Use **Shopify Flow + Shopify Email** exactly.

## Timing
**After** page QC + go-live. Not a launch blocker.

## Goal
OOS variant on PDP → Notify me when in stock → email when that variant restocks.

## Planned workflow (Shopify-native)
1. **Theme (us):** sold-out → form (email + `variant_id` + product URL).
2. **On submit:** create/find Customer by email; store waitlist entry in Shopify:
   - Preferred: metaobject / customer metafield list (`email`, `variant_id`, `product_url`, `created_at`)
   - Simpler: customer tag `bis:<variant_id>` (OK early; messier at scale)
3. **Shopify Flow:** trigger when inventory for a variant goes from 0 → available.
4. **Flow action:** find waitlist rows/tags for that `variant_id` → send **Shopify Email** with deep link to PDP/variant.
5. **Cleanup:** remove waitlist entry / tag after send.

## Theme vs backend
| Layer | Owner |
| --- | --- |
| Form UI | Theme |
| Waitlist store | Shopify (customer metafield / metaobject / tags) |
| Restock detect + send | Shopify Flow + Shopify Email |

## Do NOT
- Klaviyo
- Zapier / Make
- Dedicated BIS app (unless Flow/Email blocked on plan)
- Fake notify CTA with no Flow wiring

## Prerequisite before build
Confirm plan has **Flow** + **Shopify Email** (or another Flow-send channel Andrew approves).

## Related
- Sequence: `planning/earmark-post-qc-cart-bis-sequence.md`
- Cart upsell: `planning/earmark-cart-drawer-upsell.md`
