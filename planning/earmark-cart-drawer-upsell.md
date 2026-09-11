# Earmark — Cart drawer upsell (no app)

**Status:** TODO after QC (parked 2026-09-11). Andrew approved direction.

## Goal
Native upsells inside **our** side cart (`snippets/cart-drawer.liquid` + `assets/cart.js`) — not Shopify’s default drawer, not an upsell app.

## Product idea
When cart is open, offer add-on items (tee, yoga pants, another pair). Optional: **10% off the added item** via a real Shopify automatic discount (theme cannot invent checkout prices).

## Build split
1. **Theme UI** — drawer strip: image, title, price, one-tap Add; refresh drawer + shipping meter after add.
2. **Shopify Discounts (Admin)** — automatic rule for the offer (e.g. 10% off apparel when Skins in cart, or specific product IDs). Must coexist with SAVE2.
3. **QC** — post-discount free-shipping meter still correct; no double-app meters.

## Do NOT
- Install an upsell / cart-drawer app for this
- Depend on the free-shipping meter app (removing after QC; use theme meter)

## Related
- Theme meter already uses `cart.total_price` (after discounts)
- Full `/cart` has generic recommendations section — drawer upsell is separate, curated
