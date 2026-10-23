# Meta ROAS on one basis, Fri Oct 23, 2026

**READ-ONLY. Nothing changed or sent. No customer data, no secrets (aggregates and order counts only).**
Pulled: Shopify Admin GraphQL 2025-10 `orders`, **unfiltered**, newest first back to Sep 19 (320 orders, newest #6028), **Oct 23 8:55 AM ET**; filtered locally. Meta spend: Blend MCP account `bps-2c81` (Meta ad-level and account-level insights, spend in USD), **Oct 23 ~8:56 AM ET**, windows complete through Oct 22 (final day data).

## Answer: which basis gave $6,486.11?
**Basis A, order total including shipping and tax** (Shopify `currentTotalPriceSet`, i.e. after refunds/edits). The 66 Meta paid orders (Sep 23-Oct 22) sum to **$6,486.11** on A. (Original `totalPriceSet`, before refunds, is $6,560.11; the $74 gap is one refund.) The same 66 orders on **Basis B (line-item gross minus order discounts, excl shipping and tax) = $5,833.30**, which is the $5,833 in the Oct 23 report. So the two figures are the same 66 orders on two bases. The $652.81 gap is shipping $668.98 plus tax $49.65 minus the $74.00 refund (net $644.63), leaving an $8.18 residual I did not trace (likely shipping-discount/rounding handling in Shopify's discount total). The Oct 22 late addendum figures ($675.60, $2,039.40, $1,150.55, $1,322.45, $6,486.11) all match basis A exactly. **Every sales figure and ROAS in the addendum was on basis A (overstated vs net sales).** Meta-reported value ($10,907 then; $11,075 now) is a different thing again.

## Rules used (same as the Oct 22 pull)
- Order date in ET. Valid = not cancelled, `test` flag false, no tag containing "test" (TEST ORDER, Grok test, etc.), current total above $0, not a gift-card gateway, **not tagged ReturnZap Exchanged** (this removes #5877 and also #5965, #5842, #5770, which are Meta-UTM orders in the windows; #5877 itself is Oct 8 so outside both windows). Doing this gives exactly 66 orders; leaving the ReturnZap tags in gives 69 and $7,033.96 on A.
- Paid Meta = last-visit UTM source matches fb/facebook/ig/instagram/meta, or last-visit landing page has fbclid; excludes link_in_bio / igshopping (identical to `meta_paid` in /workspace/scratch-verify/an.py).
- Per-ad attribution: last-visit `utm_content` equals the ad name (exact): "IG Reel | Hear The Grip | Prospecting | Sep 2026" for (a) and "IG Reel | Upgrade Your Grip | Feb 2026" for (b). Other Hear The Grip variants ("| Sep 2026", "| Yellow Footwear") are NOT counted in (a). Order counts match the addendum (8/21 and 13/15).
- Bases: **A** = order total incl shipping and tax (current). **B** = sum(quantity x original unit price) minus order-level discounts, excl shipping and tax (the Oct 23 report's "net sales"). **C** = B minus refunded line-item subtotals (only 1 refunded order among the Meta orders, $74.00 in the 30-day all-Meta set; none in the 2 ads). **ROAS is on B** (column "ROAS on B"), A shown for reference.
- Spend = Blend Meta insights for the same dates (ET account day), whole-window totals.

## Results

### Oct 15-22 ET (8 days)

| Segment | Spend | Orders | Sales A: order total incl ship/tax | Sales B: after discounts, excl ship/tax | Sales C: B minus returns | ROAS on B | (ROAS on A, for reference) |
|---|---|---|---|---|---|---|---|
| (a) Hear The Grip Prospecting (Sep) 120251073140990396 | $756.13 | 8 | $675.60 | $596.00 | $596.00 | **0.79x** | 0.89x |
| (b) Upgrade Your Grip Feb 2026 120251156105070396 | $612.66 | 13 | $1,150.55 | $1,021.20 | $1,021.20 | **1.67x** | 1.88x |
| (c) All paid Meta (account bps-2c81 spend; UTM last-touch orders) | $1,843.83 | 22 | $2,052.15 | $1,843.20 | $1,843.20 | **1.00x** | 1.11x |

### Sep 23-Oct 22 ET (30 days)

| Segment | Spend | Orders | Sales A: order total incl ship/tax | Sales B: after discounts, excl ship/tax | Sales C: B minus returns | ROAS on B | (ROAS on A, for reference) |
|---|---|---|---|---|---|---|---|
| (a) Hear The Grip Prospecting (Sep) 120251073140990396 | $1,910.08 | 21 | $2,039.40 | $1,840.40 | $1,840.40 | **0.96x** | 1.07x |
| (b) Upgrade Your Grip Feb 2026 120251156105070396 | $854.19 | 15 | $1,322.45 | $1,173.20 | $1,173.20 | **1.37x** | 1.55x |
| (c) All paid Meta (account bps-2c81 spend; UTM last-touch orders) | $7,317.96 | 66 | $6,486.11 | $5,833.30 | $5,759.30 | **0.80x** | 0.89x |

## Changes vs the Oct 22 addendum
| Segment / window | Addendum (Oct 22 ~10:35 PM) | Now, same basis A | Now, basis B (use this) |
|---|---|---|---|
| (a) HTG Oct 15-22 | $753.31 / $675.60 / 0.90x | $756.13 / $675.60 / 0.89x | $756.13 / $596.00 / **0.79x** |
| (a) HTG 30d | $1,907.26 / $2,039.40 / 1.07x | $1,910.08 / $2,039.40 / 1.07x | $1,910.08 / $1,840.40 / **0.96x** |
| (b) UYG Oct 15-22 | $602.76 / $1,150.55 / 1.91x | $612.66 / $1,150.55 / 1.88x | $612.66 / $1,021.20 / **1.67x** |
| (b) UYG 30d | $844.29 / $1,322.45 / 1.57x | $854.19 / $1,322.45 / 1.55x | $854.19 / $1,173.20 / **1.37x** |
| (c) All Meta 30d | $7,295.69 / $6,486.11 / 0.889x | $7,317.96 / $6,486.11 / 0.89x | $7,317.96 / $5,833.30 / **0.80x** (0.79x after returns) |

Orders are unchanged. Spend moved up slightly (+$2.82, +$9.90, +$22.27) because the addendum was pulled at 10:35 PM ET before Oct 22 spend and late attribution finished; the figures here are the later, fuller Blend values (not re-verified against the Meta UI). Net sales per order is about 10% lower than order total (shipping is about $10 on a typical order; tax is small, $49.65 across 66 orders).

## Caveats
- Last-touch UTM undercounts Meta influence (view-through, untagged FB/IG referrals ~5 orders, about $483 earlier) and credits only the final paid touch; platform claims differ (Oct 15-22: HTG 15 purchases / $1,183.30, UYG 23 / $2,147.10; 30d: HTG 37 / $3,809.95, UYG 27 / $2,486.90, account 120 / $11,075.10).
- Account-level Oct 15-22 spend ($1,843.83) matches the Meta daily sum in WHY-SALES-SLOW (about $1,845).
- Returns basis C: refund line-item subtotals only (shipping/tax refunds excluded). Orders refunded later will change C.
- Raw files with order data stay in `/workspace/meta-roas-basis/` (orders_raw.json contains customer-linked order data, do not share). Scripts: pull.py, an.py, calc.py; results.json.
