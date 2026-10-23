# Why Barreletics sales are slow: read-only diagnosis (Fri Oct 23, 2026)

**READ-ONLY. Nothing changed, nothing sent, no secrets printed or saved. Aggregates and order numbers only, no customer details.** Prepared for Andrew John.

## Sources and pull times (all times America/Detroit, ET)
| Tag | Source | Window (ET) | Pulled (ET) |
|---|---|---|---|
| [ORD] | Shopify Admin GraphQL 2025-10 `orders`, **unfiltered**, newest first back to Jul 11 (1,050 orders, newest #6028 created Oct 22 9:57 PM ET). Sanitized copy: `/workspace/diag-sales-slow/orders_sanitized.json` | Sep 1 to Oct 22 (Oct 23 so far has 0 orders of any kind) | Oct 23 8:32 AM |
| [SQL] | ShopifyQL `FROM sessions` (day, referrer_source, device) via Admin API | Sep 1 to Oct 22 | Oct 23 8:33 AM |
| [BLEND] | Blend MCP, account `bps-2c81` (the Barreletics account per earlier notes). Meta account insights daily; Google Ads daily by campaign (only PMax "Barreletics, PMax, US, Test" spent); Pinterest ad account 549756523361 daily. All are **platform-claimed** numbers | Sep 1 to Oct 22 (52 rows each, complete) | Oct 23 ~8:34 AM |
| [ADM] | Shopify Admin API: discount codes, markets, delivery profiles, abandoned checkouts, order risk | as stated | Oct 23 8:35-8:37 AM |
| [PRIOR] | `/workspace/handoffs/CLEAN-BEFORE-AFTER-2026-10-22.md`, `/workspace/no-sales-scan/zaki-diagnosis.md` (Oct 15 ads diagnosis), `/workspace/paid-dashboard-check/NOTES.md` | as stated there | earlier |

**REAL order** = card-paid, not cancelled, no test tag, no gift-card gateway, not ReturnZap/exchange, total above $0 (same rule as the Oct 22 report). **Net sales** = line-item gross minus order discounts (excludes shipping/tax), by order created date (ET). Tests are 1 to 9 orders on only 9 of the 52 days. Per Andrew's update, test windows each lasted about 10 minutes and are treated as a minor cause. Windows used: **"Sep" = Sep 1-24** (before the slowdown began), **"Pre" = Sep 25-Oct 8**, **"Post" = Oct 9-22** (14 full days after launch day). Oct 8 is the launch day (about 1:02 PM ET), kept in Pre so Post is a clean 14 days.

---

## Bottom line (read this first)
1. **The slowdown is real, about 20-25%, and it started BEFORE the Oct 8 relaunch.** Real orders per day: **8.96 (Sep 1-24) to 6.36 (Sep 25-Oct 8) to 7.00 (Oct 9-22)**. Net sales per day: **$861 to $592 to $615**. [ORD, Oct 23 8:32 AM] The 7-day average fell from about 10-11 orders/day (Sep 20-22) to 7 by Sep 27, i.e. 11 days before launch. Since the relaunch it has been flat, drifting back up (Oct 16-22: 7.7/day, $657/day).
2. **Last 14 days vs prior 14 is noise (+10%); last 14 vs September is a real decline (-22% orders, -29% net sales).** About 98 real orders were seen against about 125 expected at the September rate (Poisson z about -2.4).
3. **No evidence the relaunch broke checkout.** Session-to-purchase conversion (ShopifyQL, unverified) is 1.64% in Sep, 1.40% Pre, **1.83% Post**. Checkout reach is about 3.7-3.8% of sessions in both Sep and Post. Card payments clear (all real orders paid through Shopify Payments, none held, none flagged). Traffic fell (sessions about -22%), the ratio did not.
4. **The most likely drivers are upstream of checkout: less paid Meta traffic (and international Meta test ended), and the loss of code-driven orders.** Details below. These are correlations; none is proven causal.

---

## 1. Daily real orders and sales, Sep 1 to Oct 22 (with 7-day moving average)
[ORD Oct 23 8:32 AM; sessions [SQL] 8:33 AM; spend [BLEND] ~8:34 AM; abandoned [ADM] 8:36 AM] CSV copy: `/workspace/diag-sales-slow/daily_real_orders_sessions_spend.csv`

| Date (ET) | Day | Real orders | Real net $ | 7d avg orders | 7d avg $ | Test orders | Sessions | Meta $ | Google $ | Pinterest $ | Abandoned chk (n/$) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 09-01 | Tue | 5 | 363 | - | - | 0 | 601 | 205 | 78 | 35 | 1/143 |
| 09-02 | Wed | 9 | 846 | - | - | 0 | 510 | 325 | 47 | 36 | 2/164 |
| 09-03 | Thu | 10 | 1037 | - | - | 0 | 442 | 260 | 75 | 33 | 0/0 |
| 09-04 | Fri | 8 | 640 | - | - | 0 | 452 | 238 | 103 | 18 | 1/74 |
| 09-05 | Sat | 11 | 947 | - | - | 0 | 428 | 208 | 83 | 10 | 1/132 |
| 09-06 | Sun | 10 | 925 | - | - | 0 | 421 | 316 | 100 | 10 | 3/346 |
| 09-07 | Mon | 9 | 872 | 8.86 | 804 | 0 | 526 | 302 | 85 | 10 | 3/340 |
| 09-08 | Tue | 9 | 799 | 9.43 | 867 | 0 | 563 | 347 | 64 | 10 | 2/173 |
| 09-09 | Wed | 4 | 636 | 8.71 | 837 | 0 | 511 | 331 | 42 | 10 | 2/436 |
| 09-10 | Thu | 9 | 863 | 8.57 | 812 | 0 | 597 | 292 | 60 | 9 | 7/724 |
| 09-11 | Fri | 6 | 602 | 8.29 | 806 | 0 | 426 | 267 | 44 | 11 | 4/559 |
| 09-12 | Sat | 10 | 818 | 8.14 | 788 | 0 | 414 | 238 | 70 | 10 | 4/131 |
| 09-13 | Sun | 5 | 431 | 7.43 | 717 | 0 | 651 | 402 | 93 | 10 | 4/431 |
| 09-14 | Mon | 17 | 1530 | 8.57 | 811 | 0 | 559 | 312 | 88 | 10 | 2/197 |
| 09-15 | Tue | 12 | 953 | 9.0 | 833 | 0 | 562 | 328 | 68 | 10 | 0/0 |
| 09-16 | Wed | 8 | 900 | 9.57 | 871 | 0 | 493 | 278 | 67 | 9 | 2/247 |
| 09-17 | Thu | 15 | 1489 | 10.43 | 960 | 0 | 556 | 297 | 79 | 10 | 4/168 |
| 09-18 | Fri | 6 | 438 | 10.43 | 937 | 0 | 544 | 282 | 66 | 10 | 0/0 |
| 09-19 | Sat | 9 | 820 | 10.29 | 937 | 0 | 449 | 233 | 63 | 10 | 2/353 |
| 09-20 | Sun | 14 | 1355 | 11.57 | 1069 | 0 | 645 | 392 | 84 | 10 | 4/741 |
| 09-21 | Mon | 7 | 956 | 10.14 | 987 | 0 | 587 | 286 | 86 | 10 | 2/290 |
| 09-22 | Tue | 10 | 1323 | 9.86 | 1040 | 0 | 546 | 263 | 113 | 10 | 2/196 |
| 09-23 | Wed | 8 | 733 | 9.86 | 1016 | 0 | 577 | 287 | 130 | 10 | 1/532 |
| 09-24 | Thu | 4 | 389 | 8.29 | 859 | 0 | 462 | 299 | 89 | 10 | 0/0 |
| 09-25 | Fri | 4 | 296 | 8.0 | 839 | 0 | 450 | 281 | 81 | 10 | 2/160 |
| 09-26 | Sat | 8 | 708 | 7.86 | 823 | 0 | 396 | 219 | 76 | 9 | 1/88 |
| 09-27 | Sun | 9 | 718 | 7.14 | 732 | 0 | 873 | 373 | 106 | 10 | 3/368 |
| 09-28 | Mon | 7 | 718 | 7.14 | 698 | 0 | 770 | 191 | 92 | 10 | 8/476 |
| 09-29 | Tue | 10 | 858 | 7.14 | 631 | 0 | 671 | 302 | 45 | 10 | 7/767 |
| 09-30 | Wed | 8 | 659 | 7.14 | 621 | 0 | 678 | 280 | 102 | 9 | 1/0 |
| 10-01 | Thu | 7 | 517 | 7.57 | 639 | 0 | 389 | 265 | 63 | 10 | 12/1192 |
| 10-02 | Fri | 9 | 1059 | 8.29 | 748 | 0 | 330 | 256 | 57 | 5 | 1/77 |
| 10-03 | Sat | 3 | 285 | 7.57 | 688 | 0 | 321 | 199 | 59 | 12 | 1/0 |
| 10-04 | Sun | 5 | 431 | 7.0 | 647 | 8 | 510 | 299 | 31 | 10 | 4/154 |
| 10-05 | Mon | 7 | 870 | 7.0 | 668 | 1 | 460 | 277 | 65 | 10 | 1/84 |
| 10-06 | Tue | 1 | 74 | 5.71 | 556 | 0 | 660 | 233 | 80 | 22 | 0/0 |
| 10-07 | Wed | 7 | 659 | 5.57 | 556 | 4 | 427 | 225 | 93 | 22 | 1/184 |
| 10-08 | Thu | 4 | 441 | 5.14 | 545 | 12 | 752 | 271 | 95 | 20 | 4/880 |
| 10-09 | Fri | 4 | 433 | 4.43 | 456 | 1 | 290 | 212 | 70 | 36 | 0/0 |
| 10-10 | Sat | 7 | 655 | 5.0 | 509 | 0 | 345 | 184 | 78 | 33 | 0/0 |
| 10-11 | Sun | 9 | 798 | 5.57 | 561 | 0 | 585 | 262 | 80 | 31 | 8/1229 |
| 10-12 | Mon | 6 | 600 | 5.43 | 523 | 0 | 363 | 186 | 60 | 30 | 0/0 |
| 10-13 | Tue | 8 | 670 | 6.43 | 608 | 5 | 344 | 188 | 71 | 22 | 1/84 |
| 10-14 | Wed | 2 | 152 | 5.71 | 535 | 7 | 346 | 187 | 42 | 19 | 5/491 |
| 10-15 | Thu | 8 | 705 | 6.29 | 573 | 8 | 362 | 206 | 46 | 21 | 2/324 |
| 10-16 | Fri | 8 | 592 | 6.86 | 596 | 0 | 427 | 215 | 63 | 19 | 1/143 |
| 10-17 | Sat | 6 | 503 | 6.71 | 574 | 0 | 326 | 184 | 92 | 20 | 5/470 |
| 10-18 | Sun | 11 | 818 | 7.0 | 577 | 0 | 415 | 299 | 187 | 24 | 2/214 |
| 10-19 | Mon | 9 | 881 | 7.43 | 617 | 1 | 405 | 256 | 91 | 26 | 0/0 |
| 10-20 | Tue | 8 | 659 | 7.43 | 616 | 0 | 435 | 208 | 101 | 25 | 3/227 |
| 10-21 | Wed | 8 | 851 | 8.29 | 716 | 0 | 455 | 213 | 78 | 24 | 3/686 |
| 10-22 | Thu | 4 | 296 | 7.71 | 657 | 9 | 585 | 264 | 87 | 26 | 5/570 |
### Window comparison [ORD]
| Window (ET) | Days | Real orders | Orders/day | Net $ | Net $/day | AOV (net/order) | Orders with a code |
|---|---|---|---|---|---|---|---|
| Sep 1-14 | 14 | 122 | 8.71 | 11,310 | 808 | 92.70 | 22 |
| Sep 11-24 | 14 | 131 | 9.36 | 12,737 | 910 | 97.23 | 22 |
| Sep 1-24 | 24 | 215 | 8.96 | 20,665 | 861 | 96.12 | 38 |
| Sep 25-Oct 8 (prior 14) | 14 | 89 | 6.36 | 8,293 | 592 | 93.18 | 26 |
| **Oct 9-22 (last 14)** | 14 | **98** | **7.00** | 8,614 | **615** | 87.89 | 10 |
| Oct 16-22 (last 7) | 7 | 54 | 7.71 | 4,600 | 657 | n/a | 4 |
| Aug 1-31 (context) | 31 | 288 | 9.29 | 31,800 approx | 1,026 | n/a | n/a |

Weekly real orders (Mon-Sun, ET) [ORD]: Jul 13: 73, Jul 20: 58, Jul 27: 68, Aug 3: 67, Aug 10: 69, Aug 17: 65, Aug 24: 53, Aug 31: 64, Sep 7: 52, **Sep 14: 81**, Sep 21: 50, Sep 28: 49, Oct 5: 39, Oct 12: 49, Oct 19 (Mon-Thu only): 29. Mid-September (week of Sep 14) was an unusually strong week and flatters the September baseline. A fairer baseline is the Jul-Aug norm of about 65/week (9.3/day). **Caution:** the weeks of Sep 7 (52) and Sep 21 (50) were already as low as the recent weeks, so the erosion started around early September (3 of the 11 weeks from Jul 13 to Sep 21 were below 55: 53, 52, 50), with the Sep 14 week as the outlier. Since Sep 21 every full week is 50 or less (50, 49, 39, 49), about 25% under the Jul-Aug norm. Against the Jul-Aug rate the last 14 days expected about 130 orders and saw 98.

**Real decline vs noise.**
- **Noise:** last 14 vs prior 14 (+10%, 98 vs 89; a count of about 90 swings by about +/-10 by chance alone). Day-to-day swings (1 to 17 orders/day; Sep daily sd about 3.2).
- **Real:** the step down from the Sep 11-24 level (131 orders per 14 days) to the Sep 25-Oct 8 level (89), -32%, and it has not come back (98). Part of that step is the unusually strong Sep 14 week unwinding. Also real: net sales/day -29% vs Sep 1-24 (orders -22%, plus AOV -9%: $96.12 to $87.89; units per order 1.34 to 1.19; orders at or under $75 net were 63% of orders in Sep 1-24 and 66% in Oct 9-22, so smaller baskets and fewer large coded orders).
- **Odd days:** Oct 6 had 1 real order ($74); Oct 3 had 3; Oct 14 had 2; Sep 24 and 25 had 4 each. None has a documented cause. Oct 6 and Oct 3 are pre-launch and untested days, so low days occur without any test or launch.

### Weekday pattern [ORD, real orders per day, average]
| Window | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Sep 1-24 | 11.0 | 9.0 | 7.2 | 9.5 | 6.7 | 10.0 | 9.7 |
| Sep 25-Oct 8 | 7.0 | 5.5 | 7.5 | 5.5 | 6.5 | 5.5 | 7.0 |
| Oct 9-22 | 7.5 | 8.0 | 5.0 | 6.0 | 6.0 | 6.5 | 10.0 |
| All Sep 1-Oct 22 | 8.9 | 7.9 | 6.8 | 7.6 | 6.4 | 7.7 | 9.0 |
Mon and Sun are the best days and Wed/Fri the weakest overall, but with 2 to 4 samples per cell the post-launch weekday pattern is mostly noise. The one consistent signal is that nearly every weekday sits lower than in Sep 1-24.

---

## 2. Order gaps and order-type mix
### Gaps [ORD, real orders only, "awake gap" = elapsed time counted only 8 AM-10 PM ET]
| Window | Median awake gap | 90th percentile | Longest |
|---|---|---|---|
| Sep 1-24 | 1.14 h | 3.4 h | 10.3 h |
| Sep 25-Oct 7 | 1.46 h | 4.2 h | 12.4 h |
| Oct 8-22 | 1.66 h | 5.5 h | 8.4 h |
Orders simply became less frequent; there is no new long blackout. The longest awake-hour gaps overall: Oct 6 9:34 AM to Oct 7 6:10 AM (12.4 h, no test), Oct 2 3:54 PM to Oct 3 1:09 PM (11.3 h), Sep 27 8:17 PM to Sep 28 4:47 PM (10.5 h), Sep 12 5:20 PM to Sep 13 1:39 PM (10.3 h), Sep 11 9:08 AM to 6:26 PM (9.3 h). Four of the top five happened before Oct 8 and none overlaps a test.

**Around each test window (real-order gap that contains the window):**
| Window | Last real before | Next real after | Gap | Awake hours |
|---|---|---|---|---|
| Oct 8 tests 1:05-1:47 PM (launch 1:02 PM) | #5879 12:23 PM | #5892 3:29 PM | 3.1 h | 3.1 (about the 90th-percentile gap in September; not unusual) |
| Oct 13 eFS tests 9:06-9:15 PM | #5929 7:41 PM | #5934 9:24 PM | 1.7 h | 1.7 (normal) |
| Oct 14 tests 1:17-1:20 PM | #5935 Oct 13 9:31 PM | #5939 Oct 14 3:52 PM | 18.4 h | 8.4 (long: 4th-longest of the stretch, but the real-order silence started 15 h before the test and the 1:17 PM test was a small piece of it) |
| Oct 14 tests 8:54-9:06 PM | #5940 6:37 PM | #5945 Oct 15 8:54 AM | 14.3 h | 4.3 (normal overnight) |
| Oct 15 Managed-Markets-OFF tests 12:53-1:00 PM | #5946 9:21 AM | #5956 3:23 PM | 6.0 h | 6.0 (above the 90th percentile; plausible partial effect, or noise) |
Also seen: another test burst **Oct 22 5:24-5:36 PM** (9 cancelled gift-card orders tagged "Grok test", #6018-#6025, plus #6015 "TEST shipping failure" at 11:21 AM). Real orders that day: 4. Test windows may have cost a few orders each; they cannot explain a multi-week, 22% level shift because the slowdown predates them (pre-launch tests ran Oct 4-7, and the 7-day average was already 7/day on Sep 27).

### Domestic vs international [ORD, real orders, ship-to country]
| Window | US orders (per day) | Intl orders (per day) | Intl share | Intl countries |
|---|---|---|---|---|
| Sep 1-24 | 193 (8.04) | 22 (0.92) | 10% | AU 7, CA 6, AE 3, ES 2, FR/KR/NO/CZ 1 each |
| Sep 25-Oct 8 | 85 (6.07) | 4 (0.29) | 4% | ES 2, CA 1, AE 1 |
| Oct 9-22 | 95 (6.79) | 3 (0.21) | 3% | CA 2, IL 1 |
| Oct 13-15 only | 17 | 1 (CA #5957, Oct 15) | 6% | |
| Oct 16-22 | 54 (7.71) | 0 | 0% | |
- **International orders fell about 77% (0.92 to 0.21/day) and the fall began in late September, not at Managed Markets off (Oct 15).** AU orders stop after Sep 19, and from Sep 23 international orders thin to about one every 3-4 days (Sep 26 AE, Oct 1 ES x2, Oct 4 CA, then after launch Oct 10 CA, Oct 11 IL, Oct 15 CA #5957). Only 3 intl real orders exist after Oct 8, so the Oct 15 Managed Markets change cannot be separated from the pre-existing decline.
- Likely explanation (hypothesis, consistent with `/workspace/paid-dashboard-check/NOTES.md`): a Meta international test campaign "BAR | International | Sales | Sep 2026" ran from Sep 4 at about $44/day (AU, CA, AE, IT) with a rule to pause at day 14. 12 of the 22 September intl orders were paid-Meta last-touch. Its current status was not re-checked today.
- **US domestic orders also fell: 8.04 to 6.79/day (-16%)**, so international alone explains about 0.7 of the 1.96 orders/day lost; the rest is domestic.
- Andrew's rule (Managed Markets off blacked out international and some domestic orders): no sign of a domestic blackout in the data around Oct 15. US orders Oct 13-15 were 17 in 3 days (5.7/day), Oct 16-22 rose to 7.7/day. Oct 15's own gap of 6.0 h is the only candidate, and it contains the tests. This does not prove MM-off is harmless; the sample is small.
- Time-of-day: orders between midnight and 7 AM ET (mostly overseas buyers) were 0.83/day in Sep 1-24 and 0.29/day in Oct 9-22 [ORD], consistent with the international drop.

---

## 3. Traffic, ad spend and channel
### Sessions [SQL, pulled Oct 23 8:33 AM ET] (**unverified**: the earlier discrepancy stands, and this series has obvious anomalies: Sep 27-30 sessions of 873/770/671/678 with ordinary order counts, Oct 8 add-to-cart sessions 87 and Oct 11 add-to-cart sessions 119 against a normal 15-35. Treat trends as indicative only.)
| Window | Sessions/day | Cart-add sessions / sessions | Reached checkout / sessions | Completed checkout / sessions |
|---|---|---|---|---|
| Sep 1-24 | 522 | 5.5% | 3.8% | 1.64% |
| Sep 25-Oct 7 | 533 | 4.2% | 3.2% | 1.40% |
| Oct 9-22 | 406 | 7.1% (inflated by the Oct 11 anomaly; 5.7% for Oct 16-22) | 3.8% | 1.83% |
- Sessions/day fell 22% Sep to Post. By referrer [SQL] per day, Sep 1-24 to Oct 9-22: social 263 to 206 (-22%), direct 159 to 125 (-21%), search 96 to 72 (-25%), email 0.5 to 0.1. Everything fell together. Pre window: direct 267/day (inflated; likely bots/untracked since orders did not follow).
- Device conversion (SQL): mobile 1.63% (Sep) to 1.77% (Post), desktop 1.45% to 1.89%. No device-specific break.

### Ad spend by day [BLEND, platform-claimed, pulled ~8:34 AM ET] and real orders by channel [ORD Shopify last-click UTM; "direct/unknown" includes untagged]
| Window | Meta $/day | Google $/day | Pinterest $/day | Total paid $/day |
|---|---|---|---|---|
| Sep 1-24 | 291 | 78 | 13 | 383 |
| Sep 25-Oct 8 | 262 | 75 | 12 | 349 |
| Oct 9-22 | **219** | 82 | 25 | 326 |
Total paid spend per day is -15% (Meta -25%, Google +5%, Pinterest about +90% from a very low base).

Meta platform detail [BLEND]: clicks/day **385 to 276 to 201 (-48%)**, impressions/day 8,825 to 7,184 to 6,736, CPC $0.76 to $0.95 to $1.09 (+43%), CPM $33.0 to $36.5 to $32.5 (flat). Spend fell 25% but clicks fell 48%: **click-through rate fell**, which fits the creative decay documented Oct 15 (below), not a pricing change.

| Channel (last-click UTM, real orders) | Sep 1-24 orders/day | Sep 25-Oct 8 | Oct 9-22 | Shopify net ROAS Sep / Pre / Post |
|---|---|---|---|---|
| Paid Meta (paid_social) | 3.54 | 2.14 | 2.43 | 1.07x / 0.75x / 0.96x |
| Google PMax (pmax) | 1.75 | 1.93 | 1.64 | 2.24x / 2.27x / 1.71x |
| Pinterest | 0.04 | 0.07 | 0.14 | 0.23x / 0.43x / 0.42x |
| All other (direct, organic search, email, referrals, untagged) | 3.62 | 2.21 | 2.79 | n/a |
Paid-attributed orders: 5.33 to 4.14 to 4.21/day. Blended (all real net / all paid spend): 2.25x to 1.70x to 1.89x. ROAS here is net sales (after discounts, excl. shipping/tax) over platform spend, last-click; Meta's own claimed ROAS is 1.78x / 1.44x / 1.80x (purchase value / spend).

**Where the 1.96 orders/day went (Sep 1-24 vs Oct 9-22, approximate, last-click):** international -0.71 (about half of that Meta-attributed), paid Meta in the US -0.61, non-paid US (direct, organic, email, untagged) -0.64, Google -0.11, Pinterest +0.10. [ORD]

Earlier ads diagnosis [PRIOR, `/workspace/no-sales-scan/zaki-diagnosis.md`, Oct 15; not re-verified today]: Meta change log showed the Broad ad set budget lowered $150 to $100 (Oct 9), to $50 (Oct 11) and to $40 (Oct 14), three creatives paused, "Hear The Grip" ad decayed (0 purchases Oct 6-12), Prospecting running on one ad; Google PMax limited by target ROAS 300% (impression share under 10-19%); Pinterest catalog campaigns paused Oct 13-14 (zero checkouts). I did not re-pull Meta's change history today.

---

## 4. Discount codes and email/DM flows
### Orders with vs without a code [ORD]
| Window | Orders with code | Share | Code orders/day | No-code orders/day | AOV code / no-code (net) |
|---|---|---|---|---|---|
| Sep 1-24 | 38 | 18% | 1.58 | 7.38 | $137.39 / $87.25 |
| Sep 25-Oct 7 | 25 | 29% | 1.92 | 4.62 | $109.44 / $85.27 |
| Oct 9-22 | 10 | 10% | 0.71 | 6.29 | $144.66 / $81.44 |
- Codes in Post: only SAVE2 (9 orders) and one wholesale-instructor code. Gone since Oct 8: FB-EMAIL-xxxx and IG-EMAIL-xxxx (per-person codes; 11 redeemed Sep 26-Oct 4, 0 after), SAVE10 (51 uses all-time, **last used Sep 28**, one SAVE10-xxxx variant Oct 5), 0-20OFF (Oct 5), THANKYOU codes (last Sep 21).
- Code orders per day fell 0.87 (1.58 to 0.71) but **no-code orders also fell 1.09/day (7.38 to 6.29)**, so codes explain at most 45% of the lost orders and some coded buyers might have bought anyway. Pre-launch no-code orders were weak too (4.62/day).
- **Email/DM code generation (Shopify discount codes created, [ADM] Oct 23 8:35 AM):** FB-EMAIL/IG-EMAIL per-person codes created: **Sep 1-24: 20 (0.8/day, 0 redeemed); Sep 25-Oct 7: 69 (5.3/day, 11 redeemed); Oct 8-22: 13 (0.9/day, 0 redeemed)**. So a code-issuing flow ran hot for 13 days just before launch (an apparent promotion push, source unverified, possibly the ManyChat/DM lead-capture, which would fit the FB/IG naming) and then nearly stopped at the launch. It is still alive at a trickle (codes created Oct 9, 10, 11, 17, 20, 22, 23).
- "Abandoned Cart Unique 10%" codes are still created every day (20 in Sep 25-Oct 7; 26 in Oct 8-22, so the abandoned-cart email flow is running). Redemptions: 1 before launch, 0 after. Judge.me THANKYOU codes still created (6 in Oct 8-22, 0 redeemed).
- **Cannot see:** Shopify Flow, Shopify Email/Messaging campaigns, Klaviyo or ManyChat scheduling and send history (no scope/tool here). I cannot say whether a campaign or flow was turned off; only that code creation and code redemption dropped at launch.
- Email-channel sessions are negligible in both periods (13, 4, 2 sessions), so email was never a traffic driver; the code orders came from paid social visitors who got a code via DM/popup.
- AOV: net AOV fell $96.12 to $87.89. The code orders skew larger ($137-145), so losing them lowers volume more than AOV.

---

## 5. Checkout, payments, markets, theme [ADM unless noted, Oct 23 8:35-8:37 AM ET]
- **Theme publish / app changes: cannot see.** The app token has no `read_themes` scope (Admin API returned ACCESS_DENIED). Relaunch time (about 1:02 PM ET Oct 8) is taken from Andrew/earlier notes, not from the API. No webhooks subscribed (empty list). No scope changes are visible.
- **Markets:** "United States" (primary) ACTIVE and "International" (59 countries incl. AU, CA, GB, AE, DE, FR, IT, ES, BR) ACTIVE. Shop ships to 60 countries. Managed Markets/Global-e on-off state is not exposed to this API; the setting change on Oct 15 is documented in `/workspace/efs-receipts/mm-off-test-orders-2026-10-15.md` only. 29 real orders since Sep 1 carry the `globale` tag, exactly the 29 ship-abroad orders (CA 9, AU 7, ES 4, AE 4, 5 others); the last is #5957 on Oct 15.
- **Shipping:** General profile has 11 active rates. US zone: Standard $9.95, Free Shipping (cart total threshold, 3-9 day estimate), USPS Priority $16.95, FedEx Ground Economy $14.95, plus carrier-calculated FedEx; AK/HI/PR $16.95; International zone uses carrier-calculated FedEx/UPS/DHL Express; Mexico DHL eCommerce. A second profile named "New Test Profile" (US Standard $9.95, free over a threshold, USPS Priority $19.95, International FedEx) also has active rates. No rate-change history is available through the API. **Share of real orders paying zero shipping: 6% (Sep) to 3% (Post); shipping revenue per order $12.95 to $10.18, units per order 1.34 to 1.19.** (The free-shipping threshold is not shown here; earlier work is in `/workspace/freeshipping-check` and `/workspace/golive-*`.)
- **Payment gateways:** every real order in all three windows was paid by `shopify_payments` (215, 85, 102). No order in Jul 11-Oct 23 used PayPal (gateways seen across 1,050 orders: shopify_payments 915, gift_card 58, shop_cash 2, manual 1). So the open "PayPal off" task has no visible effect on past sales, and I cannot tell whether a PayPal button was ever shown (not evidenced as a lost-sales cause, but not ruled out either, because it could not capture orders if absent).
- **Fraud/risk holds:** 0 orders held or cancelled for risk. All 267 orders (tests included) from Sep 25 to Oct 23 have Shopify risk recommendation ACCEPT (192) or NONE (75); 0 CANCEL/INVESTIGATE. Fulfillment ON_HOLD: 2 orders Sep 25-Oct 7 and 3 orders Oct 8-22 (all in the ReturnZap/partially-paid exchange class, not new sales). No real order is unpaid or authorized-only (all PAID). Cancelled card-paid orders: none (all 46 cancelled in the Oct 22 report were gift-card tests).
- **Order numbering:** 7 order numbers are missing between #5520 and #6028 (#5557, #5609, #5612, #5736, #5793, #5856, #5893). Likely deleted tests or drafts; #5893 sits inside Oct 8 launch-day. Unverified, low weight.
- **Abandoned checkouts** (Shopify's list only includes checkouts with a captured email) [ADM Oct 23 8:36 AM]:
| Window | Count (per day) | Value (per day) | Recovered (completed) |
|---|---|---|---|
| Sep 1-24 | 53 (2.2) | $6,379 ($266) | 3 (5.7%) |
| Sep 25-Oct 7 | 42 (3.2) | $3,549 ($273) | 0 |
| Oct 9-22 | 35 (2.5) | $4,439 ($317) | 0 |
  Abandonment did not spike after the relaunch (2.5/day vs 2.2 in Sep). Recovery shows 0 since Sep 25; counts are small and the "recovered" field is not a reliable attribution. ShopifyQL checkout-reach is about 3.7-3.8% of sessions in both Sep and Post, and checkout-completion 43% (Sep), 44% (Pre), 48% (Post): the checkout step itself is not leaking more after launch.

---

## 6. Conclusion
### The 3 most likely causes, ranked (all correlation, not proven causation)
1. **Less paid Meta traffic: budgets cut, the winning creative decayed, and the international Meta test wound down.** Evidence strength: **moderate to strong (platform data + order attribution + earlier change log)**. Meta spend -25%, clicks -48%, CPC +43%; Meta-attributed real orders 3.54 to 2.43/day (about 1.1/day lost incl. intl). Meta last-click orders fell from 3.5 to 2.1/day in Sep 25-Oct 8 while spend was still $262/day (Shopify ROAS 0.75x); in Oct 9-22 spend fell to $219/day and ROAS recovered to 0.96x. Timing predates the relaunch.
   - Hypothesis part: that the budget cuts of Oct 9-14 and the creative pause (Oct 13) are the direct cause; I did not re-pull Meta's change log today. The Oct 15 diagnosis lists them.
2. **Loss of code-driven orders (FB-EMAIL/IG-EMAIL/SAVE10/abandoned-cart style discounts).** Evidence strength: **moderate that the orders disappeared, weak on why**. Code orders 1.58 to 0.71/day, per-person code issuing 5.3/day to 0.9/day exactly at launch. Whether the issuing flow broke on the new theme or was simply stopped is unknown. SAVE10 stopped Sep 28, before launch. No-code orders also fell, so this is at most about half of the loss.
3. **General traffic/top-of-funnel softness not tied to the relaunch (direct, organic search, untagged); includes international demand loss.** Evidence strength: **weak to moderate**. Sessions -22% across all referrers, non-paid US orders -0.64/day, intl orders -0.71/day. Session data is unverified. Could be seasonality, the end of mid-September promo effect (week of Sep 14 was a spike), or SEO/ranking changes; none checked.
- **Not supported by the data (ranked low):** relaunch/theme checkout break (conversion and checkout completion did not fall), payment failures, fraud holds, Managed Markets off causing a domestic blackout, test activity (minor, as Andrew said; it can explain at most small short gaps like Oct 15's 6 h).

### Evidence missing
- Theme publish/app history (no `read_themes`) and Shopify Flow/Messaging/Klaviyo/ManyChat send logs and schedules.
- Who/what issues the FB-EMAIL/IG-EMAIL codes and whether it was changed Oct 8.
- Meta change log and ad-set-level data for Sep 20-Oct 8 (I relied on the Oct 15 report); whether the international Meta campaign is still on.
- Verified sessions (GA4 `300437005`; Shopify sessions have bot-like spikes), plus GA4/Shopify landing-page and device funnel by day.
- Google Search Console (organic), Merchant Center disapprovals trend (Oct 15 note: about 947 of 1,748 rows not eligible).
- Whether the "free shipping" threshold, shipping rates or prices changed in late September.
- Why Pre-window conversion was lower (1.40%) before launch.

### Exact next checks
1. Meta (Blend `bps-2c81`): pull the activity/change history Sep 18-Oct 8 and ad-set daily spend/CTR by ad; confirm when the "Hear The Grip" creative fatigued and whether "BAR | International | Sales | Sep 2026" is paused. Compare click-through and CPC per ad before restoring budget.
2. Find the FB-EMAIL/IG-EMAIL code issuer (ManyChat DM flow or Shopify Forms/popup): check whether the flow/popup/script exists on the new theme and when it last fired; open the 13 post-launch codes' creation timestamps.
3. Confirm SAVE10's and similar codes: still published or removed from the site/popup/footer? A code removal, not demand, may explain SAVE10 stopping Sep 28.
4. Add `read_themes` scope (or have Andrew check Online Store > Themes > history) to confirm the theme publish time and any later edits; check Shopify Admin Settings > Notifications/Flow for turned-off automations.
5. Re-run this report after Oct 26-28 (7-day average is climbing: 6.3 on Oct 15 to 8.3 on Oct 21) to see whether the decline is already reversing; Oct 18-21 look like the first non-declining days.
6. Check organic: Google Search Console impressions/clicks Sep 1-Oct 22 and GA4 sessions by default channel group.
7. Keep the tests off real hours: schedule future gift-card tests in off-peak hours (overnight) and tag everything "TEST ORDER" so they remain separable.

### Data caveats
- REAL gross uses raw line-item sums; the Oct 22 report found a $32-74 gap versus ShopifyQL's gross in a 12-day window. Not material.
- Channel attribution is Shopify last-click UTM; "direct/unknown" is large.
- Ad numbers are platform-claimed.
- Order classification: cancelled/gift-card/test-tag = TEST (Andrew's rule), consistent with the Oct 22 report. Oct 22 test orders (#6015, #6018-#6025) are classified TEST.
- All "ET" times: box clock America/Detroit.
