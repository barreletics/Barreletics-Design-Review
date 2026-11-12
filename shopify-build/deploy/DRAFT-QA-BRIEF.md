# Draft QA brief (parent / device) — qualification test mode

**No orders.** Confirm on unpublished draft with `cart_bundle_promo_enabled` on. Codes in theme settings remain **blank** until Admin verification (see `MISSING-CODES-DEPENDENCIES.md`).

## 1 Closed Sole pair
- Notice: draft test / not auto-applied
- **Buy 2+ Closed Sole pairs. Save 15%.**
- **Add 1 more Closed Sole pair for 35% off yoga pants**
- Pants **photo** visible; **no** size picker / add
- Native drawer **Subtotal + Checkout** unchanged

## 2+ Closed Sole (no pants)
- **Save 35% on one pair of yoga pants with 2+ Closed Sole pairs**
- Picker + add after variant select
- Savings line when 2+ pairs (no “Simulation” tag in qualification_test mode)
- **No** `/discount/` links until parent enters verified codes in theme settings

## After codes configured (parent only)
- Optional footwear link appears at 2+ pairs; pants link at 2+ with pants offer — customer must **click** link
- Confirm discount in cart/checkout manually; stop before placing order

**Not in scope:** cloud box draft URL, email handoffs — source + manifest only.
