# Barreletics storefront relaunch: clean before/after (cancelled and test orders excluded)

**READ-ONLY analysis. Nothing changed, nothing sent. Aggregates and order numbers only; no customer details. Prepared for Andrew John.**

## Sources and pull times (all times America/Detroit, ET)
- **Raw orders (all statuses):** Shopify Admin GraphQL 2025-10, `orders` connection with no date filter, newest first back to Jun 1 2026 (1450 orders), pulled **10:50:41 PM ET, Oct 22 2026**. Scratch copy sanitized in `/workspace/scratch-verify/clean/orders_clean_v2.json` (customer email reduced to a yes/no @barreletics.com flag; notes reduced to yes/no flags).
- **ShopifyQL (`FROM sales`)**: same API, pulled **10:47:00 PM ET, Oct 22 2026**. Used only to reconcile all-order totals.
- **Windows (order created date, ET):** BEFORE = Sep 26 to Oct 7 2026 (12 days). AFTER = Oct 8 to Oct 19 2026 (12 days). Relaunch live about 1:02 PM ET Oct 8, so Oct 8 is a half-and-half day.
- **Pitfall found:** a date-filtered orders search (`created_at:>=...`) silently omitted order #5877 (a ReturnZap exchange, Oct 8). Earlier scratch pulls that used it showed 120 AFTER orders instead of 121. This report uses the unfiltered pull, which matches ShopifyQL exactly (106 and 121 orders).

## Definitions (applied in this order; first match wins)
1. **TEST** = any of: payment gateway `gift_card`; any tag containing "test" (`TEST ORDER`, `TEST`); or the order is **cancelled** (Andrew's rule: only Barreletics cancels orders, so cancelled = test). Cancelled alone is treated as a test marker per Andrew's latest instruction, but each cancelled order's gateway and tags are listed so he can confirm. Any cancelled order paid by credit card is flagged separately ("real cancellations").
2. **RETURNZAP / exchange** = tag contains `ReturnZap` (customer's exchange order, partly paid) or `Exchange Shipment Order` ($0 replacement shipment). Own line, not in REAL.
3. **$0 / fully discounted** = order total price is $0 and not test or exchange. All are Shopify draft orders (comps, replacements, studio-owner giveaways).
4. **REAL** = everything else: card-paid (shopify_payments), not cancelled, no test tag, total above $0.
- Secondary test signals checked: customer email at @barreletics.com (3 orders in AFTER, all already gift-card cancelled tests), a note mentioning test (5 orders in AFTER, all already gift-card tests), an order attribute `test` (4 orders, same). No non-test-classified order carried any of these. No order has the Shopify `test` flag set (0).
- **Metrics:** Gross sales = sum of line-item prices before discounts (excl. shipping/tax). Discounts = order discounts. Net sales = gross minus discounts minus returned item value. Refunds shown two ways: item value (what Shopify calls returns) and cash (includes shipping/tax refunded). AOV = (gross minus discounts) divided by orders; AOV incl. ship/tax shown too. Revenue per day uses gross minus discounts by order date.
- **Paid Meta** = last-visit UTM source in {fb, ig, facebook, instagram} and UTM medium containing "paid" (almost all are `paid_social`). Sensitivity: first-visit OR last-visit paid Meta. `ig / social` (not paid) counts as other.

## 1. Order classes (created date in window, all statuses)
| Class | BEFORE Sep 26-Oct 7 | AFTER Oct 8-Oct 19 |
|---|---|---|
| All orders (matches ShopifyQL 106 / 121) | 106 | 121 |
| TEST (gift card / test tag / cancelled) | 13 | 34 |
| ReturnZap / exchange | 3 | 4 |
| $0 / fully discounted (drafts) | 9 | 1 |
| **REAL** | 81 | 82 |
| ...of TEST: cancelled | 13 | 33 |
| ...of TEST: gift_card gateway | 13 | 34 |
| ...of TEST: carrying a test tag | 6 | 21 |
| ...of TEST: NOT cancelled (gift card + test tag) | none | #5995 |
| **Cancelled orders paid by credit card ("real cancellations")** | NONE | NONE |

Every cancelled order in both windows (46) was paid with the `gift_card` gateway. None was paid by credit card, so nothing needs a separate "real cancellation" call. Counts reconcile to the earlier check: cancelled 13 BEFORE, 33 AFTER (12 on Oct 8, 1 on Oct 9, 20 on Oct 13-15).

### 1a. Every cancelled (test) order: gateway, tags, total
Cancel reason in Shopify: `CUSTOMER` or `OTHER` (the field is a dropdown, not evidence of who cancelled). Times are ET order-created time.

| Order | Created (ET) | Gateway | Tags (excl. eFulfillment) | Order total | Refunded cash | Cluster |
|---|---|---|---|---|---|---|
| #5844 | Oct 04 13:38 (before) | gift_card | TEST ORDER | $88.39 | $88.39 | Pre-launch tests Oct 4-5 |
| #5845 | Oct 04 13:44 (before) | gift_card | (none) | $88.39 | $88.39 | Pre-launch tests Oct 4-5 |
| #5846 | Oct 04 13:46 (before) | gift_card | (none) | $166.83 | $166.83 | Pre-launch tests Oct 4-5 |
| #5847 | Oct 04 13:47 (before) | gift_card | (none) | $51.29 | $51.29 | Pre-launch tests Oct 4-5 |
| #5848 | Oct 04 13:49 (before) | gift_card | (none) | $158.68 | $158.68 | Pre-launch tests Oct 4-5 |
| #5849 | Oct 04 13:50 (before) | gift_card | (none) | $122.95 | $122.95 | Pre-launch tests Oct 4-5 |
| #5850 | Oct 04 13:52 (before) | gift_card | (none) | $166.83 | $166.83 | Pre-launch tests Oct 4-5 |
| #5851 | Oct 04 13:53 (before) | gift_card | (none) | $88.39 | $88.39 | Pre-launch tests Oct 4-5 |
| #5855 | Oct 05 08:17 (before) | gift_card | TEST ORDER | $88.39 | $88.39 | Pre-launch tests Oct 4-5 |
| #5867 | Oct 07 11:13 (before) | gift_card | TEST ORDER | $88.39 | $88.39 | Pre-launch tests Oct 7 (Global-e) |
| #5868 | Oct 07 11:25 (before) | gift_card | globale, TEST ORDER | $113.33 | $113.34 | Pre-launch tests Oct 7 (Global-e) |
| #5869 | Oct 07 11:26 (before) | gift_card | globale, TEST ORDER | $132.48 | $132.47 | Pre-launch tests Oct 7 (Global-e) |
| #5870 | Oct 07 11:27 (before) | gift_card | globale, TEST ORDER | $116.08 | $116.07 | Pre-launch tests Oct 7 (Global-e) |
| #5880 | Oct 08 13:05 (after) | gift_card | TEST ORDER | $151.15 | $151.15 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5881 | Oct 08 13:06 (after) | gift_card | TEST ORDER | $83.95 | $83.95 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5882 | Oct 08 13:08 (after) | gift_card | TEST ORDER | $48.95 | $48.95 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5883 | Oct 08 13:09 (after) | gift_card | globale, TEST ORDER | $129.23 | $129.23 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5884 | Oct 08 13:11 (after) | gift_card | globale, TEST ORDER | $160.43 | $160.43 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5885 | Oct 08 13:15 (after) | gift_card | globale, TEST ORDER | $116.08 | $116.07 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5886 | Oct 08 13:19 (after) | gift_card | TEST ORDER | $48.95 | $48.95 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5887 | Oct 08 13:20 (after) | gift_card | globale, TEST ORDER | $113.33 | $113.34 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5888 | Oct 08 13:21 (after) | gift_card | TEST ORDER | $94.95 | $94.95 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5889 | Oct 08 13:30 (after) | gift_card | globale, TEST ORDER | $129.01 | $129.01 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5890 | Oct 08 13:33 (after) | gift_card | globale, TEST ORDER | $232.54 | $232.54 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5891 | Oct 08 13:47 (after) | gift_card | globale, TEST ORDER | $80.76 | $80.75 | Oct 8 post-launch gift-card tests (13:05-13:47) |
| #5895 | Oct 09 02:30 (after) | gift_card | globale, TEST ORDER | $124.18 | $124.18 | Oct 9 overnight, globale, TEST ORDER-tagged |
| #5924 | Oct 13 02:39 (after) | gift_card | globale | $123.99 | $124.00 | Oct 13 overnight, globale, gift card, no test tag |
| #5930 | Oct 13 21:06 (after) | gift_card | TEST ORDER | $88.39 | $88.39 | Oct 13 eFS tests |
| #5931 | Oct 13 21:12 (after) | gift_card | TEST ORDER | $93.95 | $93.95 | Oct 13 eFS tests |
| #5932 | Oct 13 21:14 (after) | gift_card | TEST ORDER | $121.36 | $121.36 | Oct 13 eFS tests |
| #5933 | Oct 13 21:15 (after) | gift_card | TEST ORDER | $152.86 | $152.86 | Oct 13 eFS tests |
| #5936 | Oct 14 13:17 (after) | gift_card | TEST ORDER | $88.39 | $88.39 | Oct 14 TEST ORDER-tagged |
| #5937 | Oct 14 13:19 (after) | gift_card | TEST ORDER | $88.39 | $88.39 | Oct 14 TEST ORDER-tagged |
| #5938 | Oct 14 13:20 (after) | gift_card | TEST ORDER | $88.39 | $88.39 | Oct 14 TEST ORDER-tagged |
| #5941 | Oct 14 20:54 (after) | gift_card | (none) | $107.63 | $106.03 | Oct 14 evening, note says test (no test tag) |
| #5942 | Oct 14 21:01 (after) | gift_card | (none) | $111.13 | $109.49 | Oct 14 evening, note says test (no test tag) |
| #5943 | Oct 14 21:03 (after) | gift_card | (none) | $118.62 | $116.87 | Oct 14 evening, note says test (no test tag) |
| #5944 | Oct 14 21:06 (after) | gift_card | (none) | $112.97 | $111.28 | Oct 14 evening, note says test (no test tag) |
| #5948 | Oct 15 12:53 (after) | gift_card | (none) | $121.77 | $119.96 | Oct 15 Managed-Markets-off tests |
| #5949 | Oct 15 12:54 (after) | gift_card | (none) | $164.78 | $164.78 | Oct 15 Managed-Markets-off tests |
| #5950 | Oct 15 12:54 (after) | gift_card | (none) | $111.34 | $109.70 | Oct 15 Managed-Markets-off tests |
| #5951 | Oct 15 12:56 (after) | gift_card | (none) | $130.09 | $128.16 | Oct 15 Managed-Markets-off tests |
| #5952 | Oct 15 12:56 (after) | gift_card | (none) | $142.46 | $140.36 | Oct 15 Managed-Markets-off tests |
| #5953 | Oct 15 12:57 (after) | gift_card | (none) | $145.13 | $142.98 | Oct 15 Managed-Markets-off tests |
| #5954 | Oct 15 12:58 (after) | gift_card | (none) | $132.84 | $130.87 | Oct 15 Managed-Markets-off tests |
| #5955 | Oct 15 13:00 (after) | gift_card | (none) | $178.17 | $178.17 | Oct 15 Managed-Markets-off tests |

Cluster match: Oct 8 = #5880-#5891 (12, first at 13:05, three minutes after launch) plus #5895 at 02:30 on Oct 9; Oct 13 eFS tests #5930-#5933 confirmed; Oct 15 #5948-#5955 (8) confirmed against `mm-off-test-orders-2026-10-15.md`. The other 8 cancelled in Oct 13-15 (#5924, #5936-#5938, #5941-#5944) were checked by gateway: all gift card, so they fit the rule, but #5924 (Oct 13 02:39) and #5941-#5944 carry no test tag, so Andrew should confirm those 5. BEFORE window also had 13 cancelled gift-card tests (Oct 4-7), i.e. testing happened before launch too.

### 1b. Order numbers behind the other classes
**BEFORE**
- Non-cancelled test: none
- ReturnZap / exchange: #5112-EX1 ($0.00, paid, Exchange Shipment Order); #5842 ($157.95, partially_paid, ReturnZap Exchanged); #5659-EX1 ($0.00, paid, Exchange Shipment Order)
- $0 / fully discounted (draft orders): #5857 (discount $78.00); #5834 (discount $74.00); #5816 (discount $74.00); #5815 (discount $74.00); #5792 (discount $148.00); #5789 (discount $148.00); #5787 (discount $74.00); #5780 (discount $74.00); #5779 (discount $89.00)
- REAL (81): #5771, #5772, #5773, #5774, #5775, #5776, #5777, #5778, #5781, #5782, #5783, #5784, #5785, #5786, #5788, #5790, #5791, #5794, #5795, #5796, #5797, #5798, #5799, #5800, #5801, #5802, #5803, #5804, #5805, #5806, #5807, #5808, #5809, #5810, #5811, #5812, #5813, #5814, #5817, #5818, #5819, #5820, #5821, #5822, #5823, #5824, #5825, #5826, #5827, #5828, #5829, #5830, #5831, #5832, #5833, #5835, #5836, #5837, #5838, #5839, #5840, #5841, #5843, #5852, #5853, #5854, #5858, #5859, #5860, #5861, #5862, #5863, #5864, #5865, #5866, #5871, #5872, #5873, #5874, #5875, #5876
**AFTER**
- Non-cancelled test: #5995
- ReturnZap / exchange: #5965 ($231.95, partially_paid, ReturnZap Exchanged); #5897 ($157.95, partially_paid, ReturnZap Exchanged); #5589-EX1 ($0.00, paid, Exchange Shipment Order); #5877 ($276.35, partially_paid, ReturnZap Exchanged)
- $0 / fully discounted (draft orders): #5947 (discount $74.00)
- REAL (82): #5878, #5879, #5892, #5894, #5896, #5898, #5899, #5900, #5901, #5902, #5903, #5904, #5905, #5906, #5907, #5908, #5909, #5910, #5911, #5912, #5913, #5914, #5915, #5916, #5917, #5918, #5919, #5920, #5921, #5922, #5923, #5925, #5926, #5927, #5928, #5929, #5934, #5935, #5939, #5940, #5945, #5946, #5956, #5957, #5958, #5959, #5960, #5961, #5962, #5963, #5964, #5966, #5967, #5968, #5969, #5970, #5971, #5972, #5973, #5974, #5975, #5976, #5977, #5978, #5979, #5980, #5981, #5982, #5983, #5984, #5985, #5986, #5987, #5988, #5989, #5990, #5991, #5992, #5993, #5994, #5996, #5997

## 2. REAL orders: before vs after
| Metric (REAL only) | BEFORE Sep 26-Oct 7 | AFTER Oct 8-Oct 19 | Change |
|---|---|---|---|
| Orders | 81 | 82 | +1.2% |
| Gross sales | $8,200.53 | $7,389.06 | -9.9% |
| Discounts | $644.65 | $141.00 | -78.1% |
| Gross minus discounts | $7,555.88 | $7,248.06 | -4.1% |
| Returns on these orders (refund on an order created in the same window), item value | $0.00 | $0.00 | n/a |
| Net sales by order date (= gross minus discounts minus returns on these orders) | $7,555.88 | $7,248.06 | -4.1% |
| Real returns by REFUND date (any order, refunded in window), item value | $882.15 | $819.55 | -7.1% |
| ...same, cash refunded to card/no-cash | $844.40 | $685.90 | -18.8% |
| Net sales, Shopify-style (gross minus discounts minus real returns by refund date) | $6,673.73 | $6,428.51 | -3.7% |
| Shipping charged | $865.33 | $838.72 | -3.1% |
| Taxes | $64.63 | $70.83 | +9.6% |
| Order total price (incl. ship/tax/duties, before refunds) | $8,494.02 | $8,164.08 | -3.9% |
| AOV (gross minus discounts) per order | $93.28 | $88.39 | -5.2% |
| AOV incl. ship/tax per order | $104.86 | $99.56 | -5.1% |

Source: raw orders pulled 10:50 PM ET Oct 22 2026. Real refunds by order date are $0 in both windows (no REAL order created in either window has a refund yet), so "refunds by order date" for REAL is $0.00 vs $0.00. The real returns by refund date come from older orders (created before Sep 26 or in the other window's gaps): BEFORE 10 refunds, AFTER 11 refunds (AFTER includes one $78.00 refund with no cash transaction, i.e. store credit or exchange).

**Sensitivity: #5862 (Oct 5, discount code `0-WHOLESALE-STUDIO`, gross $748.00, discount $374.00) is a wholesale-style order inside REAL BEFORE.** Without it BEFORE is 80 orders, gross $7,452.53, discounts $270.65, gross minus discounts $7,181.88, AOV $89.77. AFTER has one comparable order (`0-WHOLESALE-INSTRUCTOR`, $37.00 discount).

### 2a. Reversals (refunds): test vs real, both windows
| Basis | Bucket | BEFORE item value | BEFORE cash | AFTER item value | AFTER cash |
|---|---|---|---|---|---|
| By ORDER date (orders created in window) | Test/cancelled, refunded to gift card | $1,159.58 | $1,470.41 | $2,558.80 | $3,917.88 |
| By ORDER date (orders created in window) | REAL (card) | $0.00 | $0.00 | $0.00 | $0.00 |
| By ORDER date (orders created in window) | ReturnZap/exchange | $0.00 | $0.00 | $0.00 | $0.00 |
| By ORDER date (orders created in window) | $0 drafts | $0.00 | $0.00 | $0.00 | $0.00 |
| By REFUND date (refund created in window, any order) | Test, refunded to gift card | $1,159.58 | $1,470.41 | $2,558.80 | $3,917.88 |
| By REFUND date (refund created in window, any order) | REAL orders (card refunds + no-cash) | $882.15 | $844.40 | $819.55 | $685.90 |
| By REFUND date (refund created in window, any order) | ReturnZap/exchange and $0 orders | $288.60 | $66.05 | $74.00 | $0.00 |
| Total by refund date (my pull) | all | $2,330.33 | | $3,452.35 | |
| ShopifyQL `returns` (all orders, by refund date) | all | $2,330.33 | | $3,341.86 | |

What this shows: the ShopifyQL returns jump ($2,330.33 to $3,341.86) is driven by test refunds, which rose from $1,159.58 to $2,558.80 item value ($1,470.41 to $3,917.88 cash including shipping and tax). Real returns went the other way: $882.15 to $819.55. Test orders also inflate gross sales ($1,159.58 BEFORE, $2,662.40 AFTER) because the sale is booked and then refunded to the gift card. Reconciliation: my by-refund-date item totals match ShopifyQL exactly BEFORE ($2,330.33 vs $2,330.33); AFTER mine is $3,452.35 vs ShopifyQL $3,341.86, a $110.49 gap that I could not fully explain (it equals the $78.00 no-cash refund plus $32.49, which is the same size as the AFTER gross gap below).

### 2b. Reconciliation of all orders to ShopifyQL (same windows)
| Measure (all orders incl. test) | BEFORE mine | BEFORE ShopifyQL | AFTER mine | AFTER ShopifyQL |
|---|---|---|---|---|
| Orders | 106 | 106 | 121 | 121 |
| Gross sales | $10,341.11 | $10,267.11 | $10,791.46 | $10,758.97 |
| Discounts | $1,477.65 | $1,477.65 | $274.20 | $274.20 |
| Total sales (ShopifyQL, net of returns) | n/a | $7,452.92 | n/a | $8,154.38 |

Order counts and discounts match exactly. Gross sales differ by $74.00 BEFORE and $32.49 AFTER (raw line-item prices vs ShopifyQL's gross; cause unverified, probably currency rounding/exchange line handling). These gaps are under 1% and do not change any conclusion, but REAL gross is my raw line-item sum, not Shopify's own figure.

### 2c. Test and other classes (for scale)
| Class | BEFORE orders | BEFORE gross | AFTER orders | AFTER gross |
|---|---|---|---|---|
| Test/cancelled | 13 | $1,159.58 | 34 | $2,662.40 |
| ReturnZap/exchange | 3 | $148.00 | 4 | $666.00 |
| $0 drafts | 9 | $833.00 | 1 | $74.00 |

## 3. REAL revenue per day (gross minus discounts, by order created date, ET)
| Date | Day | BEFORE orders | BEFORE $ | | Date | Day | AFTER orders | AFTER $ |
|---|---|---|---|---|---|---|---|---|
| Sep 26 | Sat | 8 | $708.24 | | Oct 08 | Thu | 4 | $440.80 |
| Sep 27 | Sun | 9 | $717.80 | | Oct 09 | Fri | 4 | $433.20 |
| Sep 28 | Mon | 7 | $717.80 | | Oct 10 | Sat | 7 | $654.62 |
| Sep 29 | Tue | 10 | $858.00 | | Oct 11 | Sun | 9 | $797.77 |
| Sep 30 | Wed | 8 | $659.20 | | Oct 12 | Mon | 6 | $600.00 |
| Oct 01 | Thu | 7 | $517.30 | | Oct 13 | Tue | 8 | $670.00 |
| Oct 02 | Fri | 9 | $1,059.00 | | Oct 14 | Wed | 2 | $152.00 |
| Oct 03 | Sat | 3 | $285.20 | | Oct 15 | Thu | 8 | $705.27 |
| Oct 04 | Sun | 5 | $430.74 | | Oct 16 | Fri | 8 | $592.00 |
| Oct 05 | Mon | 7 | $870.00 | | Oct 17 | Sat | 6 | $503.20 |
| Oct 06 | Tue | 1 | $74.00 | | Oct 18 | Sun | 11 | $818.00 |
| Oct 07 | Wed | 7 | $658.60 | | Oct 19 | Mon | 9 | $881.20 |
- BEFORE: total $7,555.88, mean $629.66/day, median $683.72/day, range $74.00 to $1,059.00; orders/day median 7.0, range 1 to 10.
- AFTER: total $7,248.06, mean $604.00/day, median $627.31/day, range $152.00 to $881.20; orders/day median 7.5, range 2 to 11.

**Odd days:**
- **Oct 6 (BEFORE): 1 real order, $74.00**, versus a typical 7-9. Lowest day in either window; cause unverified (no Meta-paid orders that day).
- **Oct 3 (BEFORE, Sat): 3 orders, $285.20**; Saturdays are weak in general (Oct 17 Sat AFTER: 6, $503.20).
- **Oct 5 (BEFORE): gross $1,274 but discounts $404**, driven by wholesale order #5862 ($374 discount). Highest gross minus discounts before is Oct 2 ($1,059.00).
- **Oct 8 (AFTER, launch day): 4 real orders, $440.80.** Only 2 real orders before 1:02 PM ET (#5878 11:19, #5879 12:23) and 2 after (#5892 15:29, #5894 21:25). The 12 gift-card tests between 13:05 and 13:47 are excluded; all-order count that day was 18 (ShopifyQL 18), which is what made launch day look busy.
- **Oct 9 (AFTER): 4 orders, $433.20**, a soft day right after launch.
- **Oct 14 (AFTER, Wed): only 2 real orders, $152.00**, with 7 test orders that day (#5936-#5938, #5941-#5944); the dip coincides with eFS/Managed Markets testing but the cause is unverified.
- **Oct 18-19 (AFTER): 11 and 9 orders, $818.00 and $881.20**, the two strongest AFTER days, the latest data in the window.
- All-order counts per day are inflated by tests on Oct 4, 8, 13, 14, 15 (see table column in the data file); do not read them as demand.

## 4. Paid Meta vs other channel (REAL orders)
| Window | Channel | Orders | Gross minus discounts | Share of orders | Share of $ |
|---|---|---|---|---|---|
| BEFORE | Paid Meta (last-touch) | 27 | $2,445.70 | 33% | 32% |
| BEFORE | Other channels | 54 | $5,110.18 | 67% | 68% |
| AFTER | Paid Meta (last-touch) | 29 | $2,647.60 | 35% | 37% |
| AFTER | Other channels | 53 | $4,600.46 | 65% | 63% |

Sensitivity (paid Meta if EITHER first or last visit was paid Meta): BEFORE 31 of 81 orders, $2,791.14; AFTER 37 of 82 orders, $3,488.02.

Other-channel split (last-touch, REAL orders): 
- BEFORE: Paid Meta 27, Google 26, Direct/organic/untagged 25, Meta organic/other 1, Pinterest 1, Email 1
- AFTER: Paid Meta 29, Direct/organic/untagged 26, Google 19, Meta organic/other 3, Pinterest 2, Email 2, Other 1

Source: Shopify `customerJourneySummary` on the raw orders pulled 10:50 PM ET Oct 22 2026 (attribution is Shopify's last-click UTM; Meta's own numbers were not re-pulled here).

## 5. Takeaways (each with window, source, pull time)
Raw-order figures: BEFORE Sep 26-Oct 7 vs AFTER Oct 8-Oct 19 ET, Shopify Admin API, pulled 10:48-10:50 PM ET Oct 22 2026; ShopifyQL pulled 10:47 PM ET Oct 22 2026.

1. **The headline lift is mostly test noise.** ShopifyQL showed total sales $7,452.92 to $8,154.38 (+9.4%) and orders 106 to 121, but those include 13 and 34 test orders and 9 and 1 $0 drafts. REAL orders: 81 to 82 (+1). REAL gross minus discounts: $7,555.88 to $7,248.06 (-4.1%). Per day: $629.66 to $604.00 (-4.1%).
2. **Real order volume was flat; order value dipped.** AOV (gross minus discounts) $93.28 to $88.39 (-5.2%). Excluding the wholesale order #5862 BEFORE, AOV was $89.77, so the AOV drop is mostly that one order and small either way.
3. **Discounts fell from $644.65 to $141.00, mainly because specific codes stopped being used.** BEFORE had 15 REAL orders on FB-EMAIL, IG-EMAIL or Save10-type codes plus a $374 wholesale discount (#5862); AFTER has none of those (only SAVE2 and one wholesale-instructor code). Treat it as a discount-code change, not a demand signal: it raises revenue per order after discounts without showing up as more orders.
4. **Reversals are not a real-returns problem.** ShopifyQL returns rose $2,330.33 to $3,341.86, but test refunds to gift cards account for $1,159.58 and $2,558.80. Real returns by refund date: $882.15 to $819.55, no REAL order created in either window has been refunded yet.
5. **Paid Meta carried about a third of real orders in both windows.** Paid Meta 27 to 29 orders ($2,445.70 to $2,647.60); other channels 54 to 53 orders ($5,110.18 to $4,600.46, -10.0%, partly the wholesale order). The mix did not visibly shift toward Meta.

## 6. What can and cannot be concluded
**Can conclude:** (a) the clean number of real orders did not move materially (81 to 82); (b) test and cancelled orders, all gift-card, explain essentially all of the jump in ShopifyQL returns and a large part of gross; (c) real card refunds were not higher after launch; (d) the discount drop is due to specific codes disappearing, not a demand signal; (e) every cancelled order was a gift-card order, none paid by card.
**Cannot conclude:** (a) that the relaunch raised or lowered conversion or sales: 12-day windows, 81-82 orders each, daily revenue standard deviation about $190-260, so a 4% difference is well inside noise; (b) anything about causation: the Meta paid push and the relaunch changed at the same time (paid Meta share was already about a third BEFORE) and email-signup codes were removed at the same time, all confounded; (c) sessions and conversion rate: the earlier check found the sessions data unreliable, so **sessions and conversion figures stay unverified** and none are used here; (d) attribution beyond Shopify last-click UTM (many real orders are direct/untagged, see the channel split above); (e) the cause of the odd days (Oct 6, Oct 14) or of the small gross gap to ShopifyQL.
**Unverified or assumed:** cancelled = test is Andrew's rule, not a Shopify field (cancel reason is only CUSTOMER or OTHER); #5924 and #5941-#5944 are gift-card cancelled orders without test tags and should be confirmed; the 3 orders with a @barreletics.com email were identified by a yes/no flag only; the $78 no-cash refund on a REAL-class order is unexplained; orders from Jun 1 to Sep 25 were pulled only to date refunds, and refunds on orders older than Jun 1 are not visible.
