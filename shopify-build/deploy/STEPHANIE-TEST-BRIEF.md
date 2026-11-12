# Draft QA brief (Stephanie / Papa) — cart bundle preview only

**Scope:** Unpublished draft with `cart_bundle_promo_enabled` on. Stop **before** checkout; orders remain paused.

## Setup
1. Add **one** Closed Sole Performance Skin to cart; open cart drawer.
2. Confirm **native** drawer footer still shows live Shopify subtotal + Checkout link unchanged.

## 1 Closed Sole pair
- Banner: **Preview only—offers aren't applied at checkout.**
- Footwear line: **Buy 2+ Closed Sole pairs. Save 15%.**
- Pants line: **Save 35% on one pair of yoga pants with 2+ Closed Sole pairs.**
- Helper: **Add 1 more Closed Sole pair for the 35% yoga-pants offer.**
- **Yoga pants photo visible**; **no** size picker / **no** add button (cannot bypass 2-pair rule).
- No word **unlock** / **unlocked** anywhere in panel.

## 2+ Closed Sole pairs (no pants yet)
- Same preview + footwear + pants copy.
- Pants **thumbnail + preview prices**; size picker + **Add yoga pants** enabled only after variant selected.
- Subtotal in footer still **live cart total** (not replaced by preview math).

## Full cart page
- Same preview block between line items and summary; summary/checkout block unchanged.

## Must NOT happen
- Discount auto-applied, code field filled, checkout intercepted, shipping bar copy replaced by preview shipping promises.

## Mobile
- Repeat 1-pair and 2-pair checks in drawer.
