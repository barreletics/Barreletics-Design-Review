# Barreletics Meta history, verified (Sep 2023 to Oct 21 2026)
Generated Oct 21 2026, 10:15 PM EDT. Read-only: nothing changed in Meta, Shopify or GitHub. This report contains data only, with no recommendations.

## Sources
- **Meta**: pulled fresh from Blend MCP, account bps-2c81, using `omni_purchase` and default attribution. Monthly account insights cover 2023-09-01 to 2026-10-21. Ad-level lifetime insights returned 124 ads. Creatives returned 130 ads.
  - Account spend for the period is **$61,522.11**. The 124 ad-level rows add up to exactly the same amount, so every dollar of spend is assigned to an ad.
  - Meta reports no spend before Nov 2023. Its claimed purchases are 0 until Oct 2025.
- **Shopify**: Admin GraphQL `orders`, created 2023-09-01 to 2026-10-21. The pull returned 3,861 orders (raw: /workspace/mh/orders.json).
  - Excluded: 126 cancelled orders (including 46 in Oct 2026: Oct 4: 8, Oct 7: 4, Oct 8: 12, Oct 14: 7, Oct 15: 12, plus 1 each on Oct 5, 9 and 13), 192 orders totalling $0, and 1 test order. That leaves **3,542 valid orders**.
  - Revenue is `currentTotalPriceSet`, which is net of edits and refunds and includes tax and shipping.
  - "Card testing" was screened only by these rules: cancelled, $0 or test. No other heuristic was applied.
- **Google Ads**: Blend, `cost_micros` ÷ 1e6.
- **Pinterest**: not available. The query failed on the first try (limited to 186 days per range) and the split retry was interrupted. **MER below therefore covers Meta + Google only.**
- **ShopifyQL cross-check**: `FROM sales … GROUP BY month, referring_channel`. ShopifyQL exposes no UTM column: `utm_source` and `last_visit_utm_source` both returned "Column Not Found".

## Attribution method (corrected)
- **Meta, paid last touch**: the last visit in `customerJourneySummary` meets one of these conditions:
  - the landing URL contains `fbclid=`;
  - `utm_source` contains fb, facebook, ig, instagram or meta (not link_in_bio);
  - the referrer host is facebook.com, l./m./lm.facebook.com, instagram.com or l.instagram.com, the landing page has no UTMs, and the referrer is not organic Instagram.
- **Any touch**: the paid-Meta rule above matches the first visit or the last visit.
- **Instagram organic / link_in_bio**: counted separately and excluded from Meta paid. This bucket is any utm containing link_in_bio, or an instagram.com referrer with no UTMs.
- **Coverage**: the share of orders that have any journey data.

## Monthly table
| Month | Meta spend | Meta purch | Meta value | Meta ROAS | Shop LT ord | Shop LT rev | Shop LT ROAS | Any-touch ord | Any-touch rev | IG organic/bio ord / rev | Store ord | Store rev | Google spend | MER (Meta+Google) | Journey cov | No-journey ord |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2023-09 | 0.00 | 0 | 0 | – | 0 | 0 | – | 0 | 0 | 0 / 0 | 19 | 2,782 | 0 | n/a (<$50 spend) | 100% | 0 |
| 2023-10 | 0.00 | 0 | 0 | – | 1 | 86 | – | 1 | 86 | 0 / 0 | 15 | 1,662 | 0 | n/a (<$50 spend) | 100% | 0 |
| 2023-11 | 173.13 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 0 / 0 | 22 | 2,282 | 103 | 8.28x | 95% | 1 |
| 2023-12 | 30.00 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 0 / 0 | 30 | 3,049 | 100 | 23.42x | 100% | 0 |
| 2024-01 | 0.00 | 0 | 0 | – | 0 | 0 | – | 0 | 0 | 0 / 0 | 34 | 3,099 | 23 | n/a (<$50 spend) | 100% | 0 |
| 2024-02 | 0.00 | 0 | 0 | – | 0 | 0 | – | 0 | 0 | 0 / 0 | 35 | 3,896 | 0 | n/a (<$50 spend) | 86% | 5 |
| 2024-03 | 13.13 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 1 / 136 | 30 | 2,962 | 0 | n/a (<$50 spend) | 97% | 1 |
| 2024-04 | 106.87 | 0 | 0 | 0.00x | 3 | 355 | 3.33x | 4 | 432 | 1 / 136 | 43 | 4,545 | 0 | 42.46x | 95% | 2 |
| 2024-05 | 55.00 | 0 | 0 | 0.00x | 5 | 269 | 4.89x | 5 | 269 | 3 / 279 | 46 | 4,536 | 0 | 82.05x | 96% | 2 |
| 2024-06 | 0.00 | 0 | 0 | – | 0 | 0 | – | 0 | 0 | 0 / 0 | 42 | 3,686 | 0 | n/a (<$50 spend) | 95% | 2 |
| 2024-07 | 26.76 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 1 / 137 | 41 | 4,188 | 0 | n/a (<$50 spend) | 98% | 1 |
| 2024-08 | 92.35 | 0 | 0 | 0.00x | 1 | 77 | 0.83x | 1 | 77 | 1 / 117 | 76 | 7,840 | 0 | 84.65x | 97% | 2 |
| 2024-09 | 247.39 | 0 | 0 | 0.00x | 1 | 77 | 0.31x | 1 | 77 | 0 / 0 | 48 | 4,666 | 0 | 18.85x | 98% | 1 |
| 2024-10 | 74.70 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 1 / 136 | 43 | 4,864 | 0 | 64.86x | 100% | 0 |
| 2024-11 | 155.92 | 0 | 0 | 0.00x | 1 | 84 | 0.54x | 1 | 84 | 0 / 0 | 32 | 3,242 | 5 | 20.10x | 97% | 1 |
| 2024-12 | 9.06 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 1 / 84 | 54 | 5,332 | 100 | 48.75x | 98% | 1 |
| 2025-01 | 69.93 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 1 / 77 | 41 | 3,737 | 100 | 21.96x | 100% | 0 |
| 2025-02 | 0.00 | 0 | 0 | – | 1 | 136 | – | 1 | 136 | 0 / 0 | 54 | 4,338 | 101 | 43.11x | 94% | 3 |
| 2025-03 | 85.01 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 0 / 0 | 67 | 6,197 | 100 | 33.49x | 93% | 5 |
| 2025-04 | 40.87 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 0 / 0 | 66 | 6,656 | 8 | n/a (<$50 spend) | 98% | 1 |
| 2025-05 | 60.00 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 0 / 0 | 62 | 5,238 | 11 | 73.66x | 98% | 1 |
| 2025-06 | 300.45 | 0 | 0 | 0.00x | 1 | 10 | 0.03x | 1 | 10 | 0 / 0 | 60 | 5,311 | 14 | 16.91x | 100% | 0 |
| 2025-07 | 163.24 | 0 | 0 | 0.00x | 2 | 160 | 0.98x | 2 | 160 | 0 / 0 | 67 | 6,245 | 17 | 34.60x | 99% | 1 |
| 2025-08 | 161.35 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 1 / 69 | 52 | 4,806 | 16 | 27.13x | 92% | 4 |
| 2025-09 | 24.67 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 0 / 0 | 49 | 4,475 | 11 | n/a (<$50 spend) | 94% | 3 |
| 2025-10 | 25.18 | 5 | 457 | 18.14x | 3 | 244 | 9.71x | 3 | 244 | 1 / 136 | 55 | 5,309 | 10 | n/a (<$50 spend) | 98% | 1 |
| 2025-11 | 93.51 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 1 / 148 | 64 | 6,076 | 17 | 55.02x | 89% | 7 |
| 2025-12 | 2.48 | 0 | 0 | 0.00x | 0 | 0 | 0.00x | 0 | 0 | 0 / 0 | 82 | 7,203 | 23 | n/a (<$50 spend) | 89% | 9 |
| 2026-01 | 1,146.47 | 44 | 4,905 | 4.28x | 29 | 2,630 | 2.29x | 33 | 2,944 | 2 / 158 | 108 | 10,445 | 27 | 8.90x | 97% | 3 |
| 2026-02 | 3,896.64 | 108 | 9,779 | 2.51x | 65 | 5,948 | 1.53x | 74 | 6,988 | 17 / 2,058 | 184 | 18,549 | 27 | 4.73x | 97% | 6 |
| 2026-03 | 7,038.93 | 142 | 13,120 | 1.86x | 96 | 9,586 | 1.36x | 111 | 11,273 | 32 / 3,736 | 247 | 25,191 | 30 | 3.56x | 94% | 14 |
| 2026-04 | 7,662.78 | 112 | 10,663 | 1.39x | 79 | 7,554 | 0.99x | 88 | 8,488 | 24 / 2,910 | 223 | 23,523 | 24 | 3.06x | 93% | 15 |
| 2026-05 | 4,002.21 | 100 | 12,897 | 3.22x | 34 | 3,550 | 0.89x | 43 | 4,462 | 24 / 2,997 | 221 | 23,716 | 1,270 | 4.50x | 90% | 22 |
| 2026-06 | 5,258.73 | 115 | 11,450 | 2.18x | 62 | 6,567 | 1.25x | 68 | 7,154 | 29 / 3,137 | 262 | 28,799 | 3,372 | 3.34x | 92% | 21 |
| 2026-07 | 8,782.97 | 195 | 19,268 | 2.19x | 117 | 11,297 | 1.29x | 131 | 13,075 | 17 / 2,543 | 304 | 36,128 | 3,032 | 3.06x | 97% | 8 |
| 2026-08 | 8,300.63 | 165 | 16,370 | 1.97x | 100 | 9,266 | 1.12x | 113 | 10,753 | 11 / 3,109 | 272 | 33,254 | 1,702 | 3.32x | 95% | 14 |
| 2026-09 | 8,631.00 | 161 | 15,156 | 1.76x | 105 | 10,544 | 1.22x | 117 | 11,805 | 3 / 390 | 250 | 26,207 | 2,379 | 2.38x | 96% | 9 |
| 2026-10 | 4,790.75 | 75 | 7,684 | 1.60x | 48 | 4,981 | 1.04x | 55 | 5,847 | 4 / 484 | 142 | 14,872 | 1,600 | 2.33x | 96% | 6 |
| **2026 YTD** | 59,511.11 | 1217 | 121,292 | 2.04x | 735 | 71,924 | 1.21x | 833 | 82,788 | | 2213 | 240,684 | 13,462 | 3.30x | 95% | 118 |
| **Lifetime Sep-2023→** | 61,522.11 | 1222 | 121,749 | 1.98x | 754 | 73,422 | 1.19x | 853 | 84,362 | | 3542 | 368,907 | 14,223 | 4.87x | 95% | 172 |

(Months with no Meta spend before Jan 2026 are shown for completeness. Lifetime Meta spend is $61,522.11. The YTD row is Jan to Oct 21 2026.)

## ShopifyQL native cross-check (Jan to Oct 2026)
ShopifyQL's facebook + instagram referring channel includes organic traffic, so it is compared with our paid last touch plus Instagram organic.

| Month | ShopifyQL facebook+instagram referring_channel ord / sales | Ours: paid LT + IG-organic ord / rev | Ours paid-Meta last-touch ord | Agreement |
|---|---|---|---|---|
| 2026-01 | 33 / 2,944 | 31 / 2,788 | 29 | agree (±10%) (-2 ord) |
| 2026-02 | 87 / 8,549 | 82 / 8,006 | 65 | agree (±10%) (-5 ord) |
| 2026-03 | 135 / 13,876 | 128 / 13,322 | 96 | agree (±10%) (-7 ord) |
| 2026-04 | 107 / 10,255 | 103 / 10,465 | 79 | agree (±10%) (-4 ord) |
| 2026-05 | 56 / 6,064 | 58 / 6,547 | 34 | agree (±10%) (+2 ord) |
| 2026-06 | 90 / 9,334 | 91 / 9,704 | 62 | agree (±10%) (+1 ord) |
| 2026-07 | 139 / 14,042 | 134 / 13,840 | 117 | agree (±10%) (-5 ord) |
| 2026-08 | 118 / 12,692 | 111 / 12,375 | 100 | agree (±10%) (-7 ord) |
| 2026-09 | 112 / 10,674 | 108 / 10,934 | 105 | agree (±10%) (-4 ord) |
| 2026-10 | 52 / 5,114 | 52 / 5,465 | 48 | agree (±10%) (+0 ord) |

Result: all 10 months agree within ±10% on order count (difference of -7 to +2 orders). ShopifyQL's `total_sales` is a different revenue measure from our order totals, so small revenue gaps are expected.

## Per ad: top 15 by lifetime spend
| # | Ad ID | Ad name | Ad set | Spend | Meta purch | Meta value | Meta ROAS | Shopify LT ord / rev (ad-id match) | Shopify LT ROAS | Match basis |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 120240962879380396 | Yellow Shoes - January 4 2026 | Yellow performance skins BROAD TEST 2/10 | 12,217.55 | 221 | 21,345.24 | 1.75x | 138 / 13,284 | 1.09x | utm_content = ad ID |
| 2 | 120244905620190396 | Video # 01 – Corrected | Broad Women 35-65+ US | 9,990.68 | 249 | 23,003.95 | 2.30x | 1 / 84 | 0.01x | utm_content = ad ID |
| 3 | 120247424832360396 | Video / No Socks Just Grip / Lifestyle / Tag Friend | Broad / Men + Women 18-65+ / US | 8,019.88 | 195 | 20,090.96 | 2.51x |  |  | NOT MATCHABLE to this ad: name used by 2 ads; name-level total 116 ord / $11,409 |
| 4 | 120250316994720396 | Pilates has evolved. Why hasn’t your footwear? Closed Sole | Broad / Men + Women 18-65+ / US | 3,870.34 | 65 | 6,094.35 | 1.57x | 47 / 4,190 | 1.08x | utm_content = ad name (name unique) |
| 5 | 120239540476510396 | Yellow Shoes - January 4 2026 | Yellow performance skins (barre-Pilates-yoga) targeting | 3,361.90 | 105 | 10,848.99 | 3.23x | 67 / 6,359 | 1.89x | utm_content = ad ID |
| 6 | 120241196854640396 | Yellow Shoes - January 4 2026 - Copy | Yellow performance skins BROAD TEST 2/10 | 3,339.46 | 68 | 5,373.50 | 1.61x | 39 / 3,599 | 1.08x | utm_content = ad ID |
| 7 | 120249603535410396 | Video / No Socks Just Grip / Lifestyle / Tag Friend / Collection page | Broad / Men + Women 18-65+ / US | 2,687.04 | 48 | 4,833.04 | 1.80x | 30 / 2,940 | 1.09x | utm_content = ad name (name unique) |
| 8 | 120249399076230396 | Pilates athletes deserve athletic footwear. | Broad / Men + Women 18-65+ / US | 2,091.82 | 43 | 3,954.55 | 1.89x | 26 / 2,466 | 1.18x | utm_content = ad name (name unique) |
| 9 | 120251073140990396 | IG Reel / Hear The Grip / Prospecting / Sep 2026 | Broad Women 35-65+ US | 1,853.73 | 35 | 3,642.05 | 1.96x | 20 / 1,955 | 1.05x | utm_content = ad name (name unique) |
| 10 | 120245410378760396 | Video # 01 – New Ad Copy | Broad Women 35-65+ US | 1,743.99 | 36 | 7,566.93 | 4.34x |  |  | NOT MATCHABLE to this ad: name used by 3 ads; name-level total 13 ord / $1,369 |
| 11 | 120250980208890396 | IG Reel / Hear The Grip / Sep 2026 | Broad / Men + Women 18-65+ / US | 1,478.02 | 21 | 1,991.25 | 1.35x |  |  | NOT MATCHABLE to this ad: name used by 3 ads; name-level total 15 ord / $1,578 |
| 12 | 120249603687150396 | Pilates athletes deserve athletic footwear. – Collection page | Broad / Men + Women 18-65+ / US | 1,033.19 | 23 | 1,916.45 | 1.85x | 11 / 1,105 | 1.07x | utm_content = ad name (name unique) |
| 13 | 120251156105070396 | IG Reel / Upgrade Your Grip / Feb 2026 | Broad / Men + Women 18-65+ / US | 742.11 | 25 | 2,319.00 | 3.12x | 15 / 1,396 | 1.88x | utm_content = ad name (name unique) |
| 14 | 120247725404300396 | Video / No Socks Just Grip / Lifestyle / Tag Friend | Broad Women 35-65+ US | 448.59 | 2 | 425.20 | 0.95x |  |  | NOT MATCHABLE to this ad: name used by 2 ads; name-level total 116 ord / $11,409 |
| 15 | 120245006792760396 | Image # 02 | Broad Women 35-65+ US | 359.10 | 8 | 752.70 | 2.10x | 3 / 244 | 0.68x | utm_content = ad ID |

Matching notes:
- From about Feb to May 2026, Shopify's last-visit `utm_content` is the numeric ad ID, with `utm_source=facebook&utm_medium=paid` (this looks like Meta's own auto-tagging). After that, `utm_content` is the ad name from the `{{ad.name}}` url_tags. So:
  - Ad-ID matches are exact.
  - Name matches are exact only when no other ad uses the same name.
  - Reused names (#3, #10, #11, #14) cannot be split across their ads.
- #2 "Video # 01 – Corrected": only 1 order ($84) carries its ad ID. The name "Video # 01 – Corrected" is shared by 6 ads and carries **103 orders / $10,160**. This ad has 99.7% of the spend among those six ads, so most of that revenue very likely belongs to it, but this is **not provable at ad level**.

## Specific checks
| Check | Claimed | Fresh Meta | Status |
|---|---|---|---|
| Yellow Shoes - January 4 2026, ad set "BROAD TEST 2/10" (ad 120240962879380396) | $12,217.55 / $21,345 | $12,217.55 spend, 221 purchases, $21,345.24 | ✅ exact |
| GRIP YOU CAN HEAR ad 120239540476510396 (named "Yellow Shoes - January 4 2026", ad set "…targeting") | $3,361.90 / $10,849 | $3,361.90, 105 purchases, $10,848.99 | ✅ exact |
| Video # 01 – Corrected (ad 120244905620190396, ad set "Broad Women 35-65+ US") | $9,990.68 / $23,004 | $9,990.68, 249 purchases, $23,003.95 | ✅ exact |
| Do all "Yellow Shoes" ads use the GRIP YOU CAN HEAR creative? | assumed yes | **No** | ❌ see below |

Yellow Shoes creatives (Meta creative data):
- **The $12,217.55 ad (120240962879380396) is not the GRIP video.** It is a dynamic or asset-feed creative with **one image** (hash 7e3e9c04…), link http://Barreletics.com/, and no body text or video.
- The GRIP YOU CAN HEAR ad (120239540476510396) is a video (video_id 935136142651962), titled "GRIP YOU CAN HEAR", body "That sound = grip…".
- These Yellow Shoes ads use the same "That sound = grip" copy but **different video IDs**: 120241196854640396, 120240510240090396, 120240073446140396, 120244816543690396, 120244269240190396 and 120244477234770396. Whether they are re-uploads of the same video cannot be confirmed from the IDs.
- "Yellow Shoes - Carousel Problem Solution TEST" (120244040677890396) is a different, carousel creative.
- "Yellow Shoes | Hero Video | Interest Rebuild V1" (120246049301690396) is another video, 1018793967344820.
- None of the old Yellow Shoes creatives have url_tags. Even so, Shopify did record `utm_source=facebook`, `utm_medium=paid` and ID-valued campaign, term and content for their orders (67 orders for the GRIP ad, 138 for the $12k ad), apparently from Meta's own auto-applied parameters. **The premise that these ads arrived untagged is not borne out by the Shopify data.**

## Reconciliation with previous "Shopify-verified" figures
| Month | Previous | New Shopify Meta last touch (corrected) | Difference | Why |
|---|---|---|---|---|
| Jan | 2.23x | 2.29x ($2,630 / $1,146.47) | +0.06 | 1 referrer-only order added; ig link_in_bio separated out |
| Feb | 1.49x | 1.53x ($5,948 / $3,896.64) | +0.04 | 5 referrer-only orders added |
| Mar | 1.30x | 1.36x ($9,586 / $7,038.93) | +0.06 | 5 referrer-only orders added |
| Apr | 0.97x | 0.99x ($7,554 / $7,662.78) | +0.02 | 4 referrer-only orders added |
| May | 0.84x | 0.89x ($3,550 / $4,002.21) | +0.05 | 1 referrer-only order added, plus revenue and refund timing |

- Under the corrected method, the previous figures move only slightly, by 0.02x to 0.06x. The reason is that the fbclid-only bucket is **0 orders in every month**, and referrer-only Meta adds just 0 to 6 orders a month. UTMs were present on the large majority of Meta orders.
- Even with first-touch Meta included (any touch), Jan to May 2026 is only 2.57x, 1.79x, 1.60x, 1.11x and 1.11x.
- Exact matching to the previous numerators was not possible because the prior spend and revenue bases were not available here. The differences above are inferred from method changes.
- Separately, Instagram organic / link_in_bio is $158 to $3,736 a month and is **not** counted as Meta paid.

## Confidence
- Meta spend, purchases and value (monthly and per ad): **high**. Pulled fresh, and the ad-level total equals the account total to the cent.
- Shopify store orders and revenue: **high**.
- Shopify Meta last touch, monthly: **high for Jan to Oct 2026**. It agrees with ShopifyQL within ±10% every month. Journey coverage is 90 to 97%, and 118 orders in 2026 have no journey data. Those are unattributed and could include Meta, so Shopify Meta figures are a **lower bound**.
- Any-touch figures: **medium**. Shopify keeps only the first and last visit, so middle touches are invisible.
- Per ad: **high** where matched by ID or by a unique name. **Not matchable** for ads with reused names (#3, #10, #11, #14), and partial for #2.
- MER: **medium**. Pinterest spend is missing, and Google spend is from Blend.
- Pre-2026: Meta spend is high confidence but tiny. Shopify Meta orders in that period are only a handful.

## Assumptions and data gaps
- Months are grouped by order createdAt in shop and box time (EDT), while Meta months follow the ad account's time zone.
- Revenue is current total including tax and shipping. Meta "value" is pixel purchase value.
- No Pinterest spend is included.
- ShopifyQL has no UTM dimension, so the cross-check is by referring channel only.
- No card-testing heuristic was used beyond cancelled, $0 or test.
