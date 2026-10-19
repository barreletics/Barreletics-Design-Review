# Frozen Spec — Cart

---
status: FROZEN
surface: Cart drawer + `/cart` full page
authority: D-024 + `docs/14-cart-flow.md` + R-06 (PR #18)
updated: 2026-07-20
---

## Applied decisions
| ID | Choice |
|----|--------|
| R-06 | Drawer = primary; implement `main-cart`; fix SSR ↔ `cart.js` selectors |

## Approved behavior
- **Drawer primary** on ATC; shipping progress ($150); line items; qty ±; remove; subtotal; View Full Cart; Checkout
- **Full page** `main-cart` parity with drawer fields + recommendations section
- SSR markup must use `data-line-key` + `data-qty-change` (match `cart.js`)
- Empty state → Shop Grippy Shoes

## Critical includes
- `sections/main-cart.liquid`; SSR/JS contract fix; drawer primary

## Deferred Optionals
- Upsell / SAVE15 near checkout; drawer upsell band
