# Draft code-applied test — parent dependencies (not resolved by theme)

## What the theme does **not** do
- Does not create, enable, or auto-apply Shopify discount codes
- Does not change native checkout flow or cart subtotal without customer using checkout or an explicit `/discount/{code}` link
- Does not assert that 2FOR15, SAVE2, SAVE15, or a 35% pants code exist or combine

## Required before “true” code-applied draft QA
1. **Admin verification** (parent / sanctioned API): footwear multi-pair code id, status, eligibility (Closed Sole), stackability
2. **Pants 35% code**: confirm exists or create on draft policy only — **unknown in repo**
3. **Theme settings** (after verification only): set `cart_bundle_footwear_discount_code` and/or `cart_bundle_pants_discount_code` in draft theme customizer — **leave blank until verified**
4. **Combinability test**: parent confirms whether footwear + pants codes can apply in one checkout (theme does not imply yes)

## Supported storefront mechanism (when codes configured)
- Optional link: `/discount/{code}?redirect=/cart` — standard Shopify discount URL; customer click only; no JS interception

## Until codes are set
- `qualification_test` mode shows qualifying copy and estimated savings math with honest draft notice
- `simulation` mode adds explicit “Simulation” labels on savings/pants prices
