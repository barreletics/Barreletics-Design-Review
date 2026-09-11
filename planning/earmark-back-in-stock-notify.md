# Earmark — Email me when back in stock (no Klaviyo)

**Status:** TODO / decide stack (updated 2026-09-11).  
**Andrew:** We do **not** use Klaviyo (trial only; not part of the stack). Prefer building without a dedicated BIS app if possible.

## Goal
OOS variant on PDP → **Notify me when in stock** → capture email → email that person when *that* variant restocks.

## Theme vs backend
| Layer | Who | What |
| --- | --- | --- |
| UI | Theme (us) | Sold-out → form (email + variant id); success state |
| Store waitlist | Shopify | Where signups live (see workflow below) |
| Detect restock | Shopify Flow (or lightweight custom) | Inventory 0 → >0 for that variant |
| Send email | Shopify Email (or transactional ESP you already pay for) | “It’s back” + PDP link |

Theme alone cannot watch inventory or send mail.

## Recommended workflow (no Klaviyo, no BIS app)

### A — Preferred: Shopify-native waitlist
1. **PDP form** (buy box): email + `variant_id` (+ product handle).
2. **On submit:** create/find Customer by email; write waitlist entry, e.g.:
   - Customer metafield list / metaobject `bis_waitlist` rows (`email`, `variant_id`, `product_url`, `created_at`), **or**
   - Tag pattern `bis:<variant_id>` on the customer (simpler; messier at scale).
3. **Shopify Flow:** trigger when inventory for a variant goes from 0 to available.
4. **Flow action:** find waitlist rows/tags for that `variant_id` → send **Shopify Email** (or Admin notification → manual only as fallback) with deep link to the PDP/variant.
5. **Cleanup:** remove that waitlist entry / tag after send (or after N days).

Needs: Shopify Email (or another send channel Flow can use) + Flow. Confirm plan includes Flow + Shopify Email before building.

### B — Fallback if Flow/Email missing
- Form → webhook to a tiny automation (Make/Zapier) → Sheet + “send Gmail/transactional when inventory webhook fires.” More glue, still no Klaviyo/BIS app.
- Or one focused BIS app only if A/B are blocked — last resort.

### C — Not preferred
- ManyChat/Tidio as primary BIS (chat-first; weak for “email me when in stock”).
- Fake notify UI with no backend.

## PDP notes
- Plug into buy box sold-out / Coming soon states.
- One-offs: keep sold-out sizes visible (existing lock).

## Related
- `planning/earmark-cart-drawer-upsell.md`
- Do not assume Klaviyo in Email sibling work unless Andrew reinstate it
