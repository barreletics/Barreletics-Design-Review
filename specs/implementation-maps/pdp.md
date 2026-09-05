# Implementation Map — PDP

## Reuse
| File | Role |
|------|------|
| `sections/pdp-buy-box.liquid` | Gallery + ATC |
| `sections/value-strip.liquid` | Trust |
| `sections/pdp-features.liquid` | Why |
| `sections/fifty-fifty.liquid` | Video motion + lifestyle |
| `sections/variant-grid.liquid` | Color/style shop |
| `sections/pdp-sock-math.liquid` | Full Sock Math |
| `sections/pdp-reviews.liquid` | Reviews/UGC |
| `sections/geo-section.liquid` | GEO |
| `sections/pdp-sticky-atc.liquid` | Sticky ATC |

## Modify
| File | Change |
|------|--------|
| `sections/pdp-buy-box.liquid` | Micro-quotes under trust row (DP-07) |
| `templates/product.json` | Confirm July 17 order; video fifty-fifty retained |

## New
| File | Role |
|------|------|
| (none required if micro-quotes in buy-box) | Justifier strip Optional later |

## Dependencies
- Product media + variants; Judge.me optional
- Size guide page
- `cart.js` for ATC drawer

## Technical risks
- Swatch hex mapping brittle; sticky ATC vs drawer z-index
- Announcement strip must remain in layout for P-C2

## Recommended order
1. Micro-quotes in buy-box
2. Confirm product.json order
3. Reviews/UGC wiring
4. Mobile gallery swipe polish
