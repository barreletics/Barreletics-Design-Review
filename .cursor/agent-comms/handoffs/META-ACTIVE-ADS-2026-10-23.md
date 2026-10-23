# Meta ACTIVE / delivering ads — BPS (Blend alias bps-2c81)

- **Source:** Blend MCP (`user-blend-ai`), read-only `blendmcp_smart_query_meta` queries, account alias `bps-2c81` ("BPS"). Nothing was changed in Meta.
- **Pull time:** 2026-10-23 ~08:34 America/Detroit (EDT, UTC-4)
- **Spend windows (as shown by Blend, USD, account currency):** Oct 15–23 2026 (9 days, inclusive of today, partial day) and Sep 23–Oct 23 2026 (31 days). Last-7-day check used Oct 17–23.
- **"Active/delivering" definition:** ad `effective_status = ACTIVE` (so its ad set and campaign are also ACTIVE). Ads with status ACTIVE but effective_status CAMPAIGN_PAUSED / ADSET_PAUSED are NOT delivering and are excluded (many legacy ones; listed by count below).
- Budgets: Meta returns cents; shown here in dollars.

## Campaigns (ACTIVE)

| Campaign | ID | Status | Budget |
|---|---|---|---|
| BAR \| Creative Test \| Broad \| US | 120246830874010396 | ACTIVE | none at campaign level (ad set budget, ABO) |
| Barreletix \| Prospecting \| CBO \| US \| May | 120244835101840396 | ACTIVE | $150.00/day (campaign, CBO) |

## Ad sets (ACTIVE and delivering)

| Ad set | ID | Campaign | Status | Budget |
|---|---|---|---|---|
| Broad \| Men + Women 18-65+ \| US | 120246830874020396 | BAR \| Creative Test | ACTIVE | $90.00/day |
| Broad Women 35-65+ US | 120244835101830396 | Barreletix CBO | ACTIVE | none (uses campaign CBO $150/day) |

(Other ad sets in the Barreletix CBO campaign — SC - IC LLA 1% / SC - Purchase LLA 1% — are PAUSED.)

## Ads (ACTIVE / delivering)

| Ad | Ad ID | Ad set | Status | Spend Oct 15–23 | Spend Sep 23–Oct 23 | Flag |
|---|---|---|---|---|---|---|
| IG Reel \| Hear The Grip \| Prospecting \| Sep 2026 | 120251073140990396 | Broad Women 35-65+ US | ACTIVE | $760.97 | $1,914.92 | Expected |
| IG Reel \| Upgrade Your Grip \| Feb 2026 | 120251156105070396 | Broad \| Men + Women 18-65+ \| US | ACTIVE | $624.93 | $866.46 | Expected |
| IG Reel \| Upgrade Your Grip \| Prospecting \| Oct 2026 | 120251386386230396 | Broad Women 35-65+ US | ACTIVE | $137.19 | $137.19 | **FLAG – not on allow-list** |

## Flags: ads with spend in last 7 days (Oct 17–23) NOT on the allow-list
Allow-list: 120251073140990396 (Hear The Grip Prospecting Sep), 120251156105070396 (UYG Feb 2026).

| Ad | Ad ID | Current status | Last-7d spend (Oct 17–23) | Oct 15–23 | Sep 23–Oct 23 | Notes |
|---|---|---|---|---|---|---|
| IG Reel \| Upgrade Your Grip \| Prospecting \| Oct 2026 | 120251386386230396 | **ACTIVE (delivering)** | $137.19 | $137.19 | $137.19 | First spend Oct 22 ($120.44); $16.75 on Oct 23 so far |
| IG Reel \| Hear The Grip \| Yellow Footwear \| Oct 2026 | 120251325637030396 | PAUSED | $197.32 | $197.32 | $197.32 | Spent Oct 18–22; last spend Oct 22 ($1.02) |
| IG Reel \| Do Your Yoga Socks Sound This Grippy? \| Prospecting \| Oct 2026 | 120251330490580396 | PAUSED | $157.28 | $157.28 | $157.28 | Spent Oct 19–21; last spend Oct 21 |

All three sit in ad set "Broad Women 35-65+ US" (Barreletix CBO campaign). Only the first is currently active/delivering.

Daily spend for the two allow-listed ads, Oct 15→23: Hear The Grip 161.82, 153.04, 121.36, 143.88, 31.56, 33.22, 69.95, 41.30, 4.84; UYG Feb 43.72, 61.92, 63.04, 97.70, 77.26, 72.22, 95.73, 101.07, 12.27.

## Not delivering despite ad status = ACTIVE (excluded)
- Ad status ACTIVE but effective_status CAMPAIGN_PAUSED / ADSET_PAUSED: many legacy/other ads (e.g. the ads in BAR | International | Sales | Sep 2026 [campaign paused], Warm Stack / ATC LAL / Yellow Shoes / PV LAL ads, and the "Instagram post" legacy ads). Zero spend in Oct 15–23 for all of them (no rows in Blend insights).
- Note: BAR | International | Sales | Sep 2026 ads had Sep 23–Oct 23 spend (total ≈ $283.19) but none Oct 15–23; campaign is PAUSED.

## Other ads with Sep 23–Oct 23 spend but currently PAUSED (no Oct 15–23 spend)
Ad ID | Name | Sep 23–Oct 23 spend
- 120244905620190396 | Video # 01 – Corrected (Barreletix CBO / Broad Women) | $1,085.80
- 120250980208890396 | IG Reel | Hear The Grip | Sep 2026 (Creative Test) | $1,478.02
- 120250316994720396 | Pilates has evolved… Closed Sole (Creative Test) | $472.68
- 120250979484300396 | IG Reel | Sock Era Is Over | Sep 2026 (Creative Test) | $246.01
- 120251155780120396 | IG Reel | Grip Socks Weren't Built to Last | Oct 2026 (Creative Test) | $182.36
- 120251114414630396 | IG Reel | Sock Era Is Over | Sep 2026 (Barreletix CBO) | $158.25
- 120250947084390396 | Grip socks had their moment. (Creative Test) | $139.22
- 120251156273880396 | IG Reel | Do Your Yoga Socks Sound This Grippy | Oct 2026 (Creative Test) | $33.12
- International campaign ads (campaign paused): 120250693286880396 $85.71, 120250693286860396 $60.57, 120250991212980396 $46.56, 120251035715960396 $45.77, 120251035893220396 $17.42, 120251036108300396 $14.17, 120250693286890396 $7.82, 120250693286850396 $2.37, 120250693286900396 $2.00, 120250693286830396 $0.80

## Notes / caveats
- Oct 15–23 window is 9 days; the "last 7 days" flag check uses Oct 17–23 (and the daily Oct 15–23 breakdown confirms no other ads spent).
- Spend is account-level Blend/Meta insights (no attribution/conversion data pulled). No customer data, no secrets included.
- The allow-list names the two expected ads; both are ACTIVE and delivering. Ad IDs in the list matched exactly.
