# Implementation Map — Cart

## Reuse
| File | Role |
|------|------|
| `snippets/cart-drawer.liquid` | Primary UX |
| `assets/cart.js` | AJAX contract |
| `templates/cart.json` | Full page template |
| `sections/recommendations.liquid` | Below cart |

## Modify
| File | Change |
|------|--------|
| `snippets/cart-drawer.liquid` | SSR: `data-line-key` + `data-qty-change` |

## New
| File | Role |
|------|------|
| `sections/main-cart.liquid` | Full-page cart parity |

## Dependencies
- Free shipping threshold setting ($150)
- Cart AJAX `/cart/change.js`

## Technical risks
- First-paint qty broken until SSR fix; main-cart missing 404s `/cart`

## Recommended order
1. Fix drawer SSR attributes
2. Build main-cart
3. Bind same cart.js patterns on full page if needed
