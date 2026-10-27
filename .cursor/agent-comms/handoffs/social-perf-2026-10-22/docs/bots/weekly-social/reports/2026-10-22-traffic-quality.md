# Barreletics traffic-quality diagnosis — Thu Oct 22 2026 (pulled ~5:40–6:00 PM ET, read-only)
Same-hours window = 00:00–16:59 ET. Prior = Oct 15–21 daily average. Test orders #6018–#6025 (5:24–5:36 PM ET) are excluded. They fall after the same-hours window. Full-day session figures after 5 PM ET may include test sessions.

## Ranked likely causes
1. **The extra sessions are mostly low-intent organic Instagram and foreign/bot traffic, not buyers.** Same hours: 382 sessions vs 251.6 (+130). Where the extra sessions came from:
   - **IGShopping / Social (organic IG product tags): 75 vs 21.3 (+54), with 0 ATC.** Full day: 82 sessions, 87% bounce, 18 s average. 24 of them are Spain → `/es/` PDP with 96% bounce and 0.1 s.
   - **ig / social (organic IG): 33 vs 10.7 (+22).** 3 ATC, 0 checkouts.
   - **Direct/no-UTM: 110 vs 81 (+29).** 59 land on `/` with 83% bounce.
   - **ig / paid_social: 56 vs 31.6 (+24).** Produced the only order (#6017).
   - Non-US countries: +70 (Spain +18, Italy +11, Argentina +8, Mexico +7, India +5…). Combined, they gave 1 reached-checkout and 0 orders.
   - Paid Google and FB fell: pmax 26 vs 32.7, fb/paid_social 48 vs 51.4.
   - **Result:** add-to-cart sessions were flat at 16 vs 14.9. The extra ~130 sessions added almost no shopping intent.
2. **Meta buying intent dropped after ad edits on Oct 21–22. This is the most actionable change.** Meta pixel purchases by day: Oct 15–20 = 6, 7, 5, 8, 5, 4. **Oct 21 = 1, Oct 22 = 0**, on normal spend ($212 and $182 so far) and normal link clicks (133, 104). What changed:
   - Oct 21, 12:56 AM ET: paused "Do Your Yoga Socks Sound This Grippy?" in the CBO.
   - Oct 21, 1:07 AM ET: Creative Test ad set updated. Daily budget is now $90.
   - Oct 22, 12:28 AM ET: paused "Hear The Grip | Yellow Footwear".
   - **Oct 22, 12:38 AM ET: created new ad "IG Reel | Upgrade Your Grip | Prospecting | Oct 2026" in CBO ad set "Broad Women 35-65+ US".** This was a significant edit at 12:39 AM. **That ad set is now in LEARNING (0 conversions).**
   - Today the new ad took $86.54 of the CBO's $116.53, with 0 purchases. The proven "Hear The Grip | Sep 2026" ad dropped to $28.97.
   - **Upgrade Your Grip did NOT spend $0 on Oct 21–22.** The original "IG Reel | Upgrade Your Grip | Feb 2026" (Creative Test) spent $95.73 on Oct 21 and $65.79 today. Both days had 0 purchases, vs 2–6/day before.
3. **Some of the traffic is bot or junk.**
   - Spain/`/es/` PDP: 26 sessions vs 7.6, about 0.1 s, 96–100% bounce, all from instagram/IGShopping.
   - China fell to 2. Pinterest PaidSocial: 16 sessions vs 7.3, about 1 s, 94% bounce. That fits Pinterest's usual pattern.
   - The 10–11 AM ET hour had 31 sessions with 90% bounce and 4.9 s average.
   - Roughly 40–60 sessions today are junk. This inflates sessions but doesn't explain the lost orders.
4. **Checkout abandonment is small, and it's not from Meta.** 5 abandoned checkouts today. The 3 US ones are 1 Delaware shopper twice (Google pmax/Shopping) plus 1 NY shopper landing on `/` with no referrer. None came from paid social. (The earlier report counted 6/4 US. One of those no longer shows as abandoned, likely the #6017 buyer.)
5. Google PMax is light today: $39.87 and 24 clicks so far vs $66–187/day, with 0 conversions so far (Google reports with a lag). Pinterest is normal.

**Bottom line:** Traffic is up, but almost all of the gain is low-intent organic IG, IG Shopping, foreign and bot sessions. Real buying intent from Meta paid fell to about zero after the Oct 21–22 ad swaps. The swaps put the main CBO ad set back into learning and moved spend to the new, unproven Upgrade Your Grip Oct ad. Expect variance while learning. If it continues, consider restoring spend weight to "Hear The Grip | Sep 2026". This is the owner's decision; nothing was changed.

## Tables
### Funnel, same hours (00:00–16:59 ET): today vs prior avg [sessions / ATC / reached checkout / completed]
| Source/medium | Today | Prior avg |
|---|---|---|
| TOTAL | 382/16/11/1 | 251.6/14.9/9.1/5.0 |
| IGShopping/Social | 75/0/0/0 | 21.3/0.9/0.6/0 |
| (none)/direct | 110/5/5/0 | 81.0/4.7/3.9/2.0 |
| ig/paid_social | 56/2/1/1 | 31.6/1.3/1.0/0.6 |
| fb/paid_social | 48/1/0/0 | 51.4/2.9/1.0/0.7 |
| ig/social | 33/3/0/0 | 10.7/0.7/0.3/0.1 |
| google/pmax | 26/4/4/0 | 32.7/3.4/1.7/1.4 |
| Pinterest/PaidSocial | 16/0/0/0 | 7.3/0.1/0/0 (+5.3 pinterest/paid_social) |

| Referrer | Today | Prior avg |
|---|---|---|
| instagram | 151/5/1/1 | 59.7/2.3/1.4/0.7 |
| direct | 120/5/5/0 | 72.3/3.7/3.9/2.0 |
| facebook | 61/1/0/0 | 60.3/3.4/1.3/0.7 |
| google | 30/5/5/0 | 41.9/4.4/2.1/1.4 |

| Device | Today | Prior avg |
|---|---|---|
| mobile | 304/13/8/1 | 194/12/6.6/3.6 |
| desktop | 65/3/3/0 | 47/2.6/2.3/1.1 |
| tablet | 13/0/0/0 | 7.7/0.3/0.3/0.3 |

| Landing page | Today | Prior avg |
|---|---|---|
| /products/best-reformer… (Open Sole PDP) | 194/7/5/1 | 141.7/9.0/4.6/2.6 |
| / | 105/4/1/0 | 49.9/2.9/1.6/0.9 |
| /es/products/best-reformer… | 24/0/0/0 | 5.1/0/0/0 |
| /products/studio-performance-skin-footwear | 17/1/1/0 | 15.4/0.9/0.9/0.6 |

| Country | Today | Prior avg |
|---|---|---|
| United States | 249/9/7/1 | 196.4/12.0/7.3/5.0 |
| Spain | 26/0/0/0 | 7.6 |
| Italy | 13/1/0/0 | 2.4 |
| Argentina | 9/1/0/0 | 0.7 |
| Mexico | 9/2/1/0 | 2.0 |
| India | 7/0/0/0 | 1.7 |
| France | 6/1/1/0 | 1.7 |
| Canada | 7/1/1/0 | 3.7 |

UTM campaign, full day today vs prior daily avg: Prospecting CBO 80 vs 104; Creative Test 34 vs 39; pmax 30 vs 54; Pinterest 626760082398 18 vs 13.

### Engagement (full day), bot signals
| Segment | Sessions | Bounce | Avg s | Pages/sess |
|---|---|---|---|---|
| social | 251 | 80% | 26 | 1.42 |
| direct | 129 | 74% | 81 | 2.81 |
| search | 35 | 57% | 171 | 3.17 |
| IGShopping/Social | 82 | 87% | 19 | 1.24 |
| Spain | 32 | 97% | 0.1 | 1.03 |
| /es/ PDP | 28 | 96% | 0.1 | 1.04 |
| Pinterest PaidSocial | 18 | 94% | 0.9 | 1.06 |

### Abandoned checkouts today (ET)
| Time ET | Total | Country | Landing / referrer / UTM | Paid social? |
|---|---|---|---|---|
| 12:55 AM | $112.14 (REST $157.40) | CA-AB | /es/ PDP?utm_source=chatgpt.com, no referrer | No (ChatGPT) |
| 9:53 AM | $128.29 (REST $114.50) | FR | /fr?srsltid=… from google.com (organic Shopping) | No |
| 1:45 PM | $161.95 | US-DE | PDP, utm google/pmax barreletics_pmax (+ product_sync sag_organic), ref google.com | No (Google) |
| 1:50 PM | $83.95 | US-DE | same shopper/journey as above | No (Google) |
| 3:14 PM | $83.95 | US-NY | / , no referrer/UTM (direct) | No |
Order #6017 (3:54 PM ET, $83.95) came from ig / paid_social, campaign "Barreletix | Prospecting | CBO | US | May", landing on the Open Sole PDP, 1 visit.

### Meta daily (pixel purchases; link clicks)
| Date | CBO spend | CBO link clk | CBO purch | CT spend | CT link clk | CT purch | Freq CBO/CT |
|---|---|---|---|---|---|---|---|
| 10/15 | 161.82 | 99 | 4 | 43.72 | 15 | 2 | 1.32/1.24 |
| 10/16 | 153.04 | 129 | 1 | 61.92 | 28 | 6 | 1.33/1.16 |
| 10/17 | 121.36 | 92 | 2 | 63.04 | 23 | 3 | 1.17/1.25 |
| 10/18 | 201.23 | 179 | 4 | 97.70 | 54 | 4 | 1.34/1.22 |
| 10/19 | 178.38 | 78 | 3 | 77.26 | 45 | 2 | 1.56/1.19 |
| 10/20 | 135.55 | 70 | 0 | 72.22 | 38 | 4 | 1.51/1.16 |
| 10/21 | 117.02 | 94 | 1 | 95.73 | 39 | 0 | 1.35/1.19 |
| 10/22* | 116.53 | 71 | 0 | 65.79 | 33 | 0 | 1.30/1.21 |
*Partial day. Link CTR 1.3–2.6% all week; CPC $1.12–2.91. IC today: CBO 6, CT 0.

Ad level on 10/22: Upgrade Your Grip Oct 2026 (NEW, CBO) $86.54 / 51 link clicks / 0 purchases; Hear The Grip Sep $28.97 / 20 / 0; Upgrade Your Grip Feb (CT) $65.79 / 33 / 0; Yellow Footwear $1.02 (paused 12:28 AM).
Placement: Audience Network $0.08–1.83/day (<1% of spend) every day, unchanged. Instagram's share is 30–37% all week (today 35%). No shift. No traffic-objective campaign is active. Only the 2 OUTCOME_SALES campaigns are ACTIVE, and the old LINK_CLICKS campaigns are all paused.

### Google PMax 23842882230 and Pinterest 549756523361
| Date | PMax $ | Clicks | Conv | Pin $ | Pin impr | Outbound clicks |
|---|---|---|---|---|---|---|
| 10/15 | 46.34 | 41 | 0 | 20.63 | 743 | 18 |
| 10/16 | 62.73 | 43 | 1.0 | 19.05 | 622 | 15 |
| 10/17 | 92.48 | 70 | 2.8 | 20.16 | 885 | 27 |
| 10/18 | 187.43 | 66 | 3.2 | 23.86 | 1007 | 18 |
| 10/19 | 90.60 | 57 | 1.0 | 25.95 | 953 | 23 |
| 10/20 | 100.60 | 47 | 4.0 | 24.68 | 1138 | 19 |
| 10/21 | 77.55 | 47 | 2.7 | 23.63 | 1170 | 13 |
| 10/22* | 39.87 | 24 | 0 | 23.40 | 1041 | 17 |
