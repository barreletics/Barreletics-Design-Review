# Earmark — Shopify legal Refund / Shipping policies (LIVE Admin)

**Status:** TODO — do when Andrew is at desktop (parked 2026-09-11).  
**Risk:** These are **live store policies** (cart / checkout / footer), not draft theme. Backup before any write.

## Do NOT
- Dump the full Help or FAQ page into legal policies
- Touch Terms / Privacy unless Andrew names them
- Touch live theme `185687998755` or draft theme as part of this task

## DO
1. Backup current Refund + Shipping bodies (Admin → Settings → Policies, or GraphQL `shop.shopPolicies`) into `planning/backups/` with a timestamp
2. Update **Refund policy** = full returns & exchanges + 90-day warranty (locked rules)
3. Update **Shipping policy** = full shipping + short returns pointer to Refund / Help
4. Verify `/policies/refund-policy` and `/policies/shipping-policy` on the live site
5. Prefer Andrew paste in Admin if API auth is flaky; otherwise API only after explicit “push it”

## Locked rules (must match Help / PDP accordion)
- 30-day returns & exchanges; indoor try-on for fit
- Workout / class / outdoors = not eligible; clean / like new
- US return shipping $7.95 (deducted); prepaid label after approval
- 90-day manufacturing-defect warranty only
- Not covered: normal wear, accidents, improper care, grip-surface wear from use
- Free shipping over $150 Continental US; $9.95 under

## Draft copy ready
- `draft-shopify-refund-policy.html`
- `draft-shopify-shipping-policy.html`

## Where in Admin
Settings → Policies → Refund policy / Shipping policy  
(or paste from the draft HTML files above)

## Related
- Help page (draft): `/pages/help` — already aligned
- Help Scout one-liner already given for returns workflow
- ManyChat / Tidio / guarantee-band still separate TODOs
