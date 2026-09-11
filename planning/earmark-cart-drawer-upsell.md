# Earmark — Cart drawer upsell + free-shipping meter (no apps)

**Status:** Prefer **before go-live** for meter/app cleanup; upsell can be before or soft-launch after. Parked 2026-09-11.

## Timing (Andrew + recommendation)
| Item | When | Why |
| --- | --- | --- |
| Remove free-shipping **meter app** | **Before live** | Conflicts with our side cart; launch on one meter only |
| QC theme shipping meter (`cart.total_price` post-discount / SAVE2) | **Before live** | Launch blocker if wrong |
| Drawer upsell UI + Shopify automatic discount | **Before live if easy**, else right after | Conversion win; safer to ship on draft before Brian promotes |
| Fancy upsell rules / A-B | After live | Not needed for launch |

## Goal
Native upsells in **our** side cart + theme free-shipping meter. No upsell app, no meter app.

## Build split
1. Theme UI in `cart-drawer` + `cart.js`
2. Shopify automatic discount for any “10% off add-on”
3. QC with SAVE2 + shipping threshold

## Related
- BIS / Zapier: `planning/earmark-back-in-stock-notify.md` (after live)
