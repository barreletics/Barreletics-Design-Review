# GRIP YOU CAN HEAR: full settings for an exact duplicate
Read-only. Pulled from Blend MCP (`blendmcp_smart_query_meta`, account bps-2c81) on 2026-10-21 at ~10 PM ET. Nothing was created, edited, paused or duplicated. No action tools were called.
Context: 2026-10-19-meta-history.json, 2026-10-20-meta-copy-vs-new.md.

## Identity
| Field | Value |
|---|---|
| Ad ID | 120239540476510396 |
| Ad name (Meta) | Yellow Shoes - January 4 2026 (several other ads share this name: 120240962879380396, 120240073446140396, plus "- Copy" variants. Use the ID.) |
| Ad status | ACTIVE (configured) / CAMPAIGN_PAUSED (effective) |
| Created | 2026-01-04 14:02 ET |

## Campaign
| Field | Value |
|---|---|
| Name / ID | "January 4 2025" (yes, 2025 in the name) / 120239540476330396 |
| Objective | OUTCOME_SALES |
| Buying type | AUCTION |
| Budget type | **CBO (Advantage campaign budget)**: daily_budget $152.00/day (15200 cents) at campaign level. Ad sets have no budget. |
| Bid strategy | LOWEST_COST_WITHOUT_CAP (Highest volume, no cap/bid) |
| Special ad categories | none |
| budget_rebalance_flag / adset budget sharing | false / false |
| Creation flow | smart_promotion_type GUIDED_CREATION (not Advantage+ Shopping) |
| Start / stop | 2026-01-04 14:02 ET / no stop time |
| Status | PAUSED (last updated 2026-05-13 13:14 ET) |
| Spend cap | none returned |

Note: $152/day is the **current** value. Blend has no change history, so it can't show what the budget was in Jan–Feb. Feb spend of about $2,197 over 28 days is about $78/day for this ad, but the CBO also funded other ad sets.

## Ad set
| Field | Value |
|---|---|
| Name / ID | "Yellow performance skins (barre-Pilates-yoga) targeting" / 120239540476340396 |
| Optimization goal | OFFSITE_CONVERSIONS (maximise number of conversions) |
| Conversion event | Pixel 628405251798480, PURCHASE (smart_pse_enabled false) |
| Attribution | 7-day click only (no view-through, no engaged-view) |
| Billing event | IMPRESSIONS |
| Budget / bid | None at ad set level (CBO). No bid amount. |
| Schedule | Start 2026-01-04 14:02 ET, no end, no dayparting returned |
| Destination type | UNDEFINED (website) |
| Dynamic creative | false |
| Status | ACTIVE / CAMPAIGN_PAUSED |

### Targeting (raw from API)
- **Advantage+ audience: ON** (`targeting_automation.advantage_audience = 1`). Everything below acts as a *suggestion*, not a hard limit.
- Age: age_min 18 / age_max 65 (hard controls); **suggested age_range 18–55**
- Gender: women only (`genders: [2]`)
- Geo: United States; location types home + recent (people living in or recently in)
- Interests, one OR group (flexible_spec): Studio Pilates 6002912233321, pure barre 6003115552014, Pilates 6003159020675, Yoga 6003306084421, Barre (ballet) 6003733940316, Pilates services 6901132242923; plus work position Pilates Instructor 786108144800685
- Custom audience included: **ATC 90** (120239957138170396). This is a website audience: pixel 628405251798480, AddToCart, 90-day retention (the rule is listed twice, which is harmless). Size is shown as 20 (a Meta lower bound/placeholder). Created 2026-01-15 ET, so **it was added about 11 days after launch**. The first ~11 days of January ran without it.
- Lookalikes: none
- Exclusions: **none** (no excluded custom audiences, so purchasers were not excluded)
- Placements: no publisher_platforms or positions in targeting, so **Advantage+ placements (automatic, all placements)**
- Languages, devices and OS: none set

Exact targeting JSON (drop nothing; for a write, remove `targeting_optimization` if it appears):
```json
{"age_max":65,"age_min":18,"age_range":[18,55],"custom_audiences":[{"id":"120239957138170396","name":"ATC 90"}],"flexible_spec":[{"interests":[{"id":"6002912233321","name":"Studio Pilates"},{"id":"6003115552014","name":"pure barre"},{"id":"6003159020675","name":"Pilates"},{"id":"6003306084421","name":"Yoga"},{"id":"6003733940316","name":"Barre (ballet)"},{"id":"6901132242923","name":"Pilates services"}],"work_positions":[{"id":"786108144800685","name":"Pilates Instructor"}]}],"genders":[2],"geo_locations":{"countries":["US"],"location_types":["home","recent"]},"targeting_automation":{"advantage_audience":1}}
```

## Ad creative (current)
| Field | Value |
|---|---|
| Creative ID | 986853500427976 (name "GRIP YOU CAN HEAR 2026-04-30-e56fd910…") |
| Format | Single video (object_type VIDEO, `video_data`, no asset_feed_spec) |
| Primary text | `That sound = grip.  Yoga socks can’t compete. This is next-level Barre & Pilates Grip.  👉 Feel the difference.` (double spaces are in the original) |
| Headline | GRIP YOU CAN HEAR |
| Description | none returned (no link_description) |
| CTA | SHOP_NOW |
| URL | http://Barreletics.com/ (http, capital B; link_format VIDEO_LPP) |
| URL params (url_tags) | **none** (history file also says has_utm_url_tags false) |
| Video ID | object_story_spec.video_id **683036644759796**; the creative's top-level video_id is **935136142651962** (they differ; see gaps) |
| Thumbnail | image_hash 7e3e9c045383838162ac0c3bbab7076d |
| Facebook Page | 1577670678941802 |
| Instagram account | instagram_user_id 17841406361484200 |

For an exact copy that keeps likes and comments, use the existing post (effective_object_story_id). **Blend didn't return that ID**, so get it from Ads Manager under Ad > Preview > "Facebook post with comments".

## Monthly performance (Meta-reported, 7d-click, pixel purchases)
| Month | Spend | Impr. | Reach | Freq. | CPM | CTR (all) | Clicks | Purchases | Value | Meta ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| Jan | $999.14 | 40,132 | 27,530 | 1.46 | $24.90 | 7.71% | 3,094 | 43 | $4,832.67 | 4.84x |
| Feb | $2,197.21 | 100,139 | 74,484 | 1.34 | $21.94 | 6.41% | 6,419 | 61 | $5,932.37 | 2.70x |
| Mar | $111.42 | 4,245 | 3,873 | 1.10 | $26.25 | 5.56% | 236 | 1 | $83.95 | 0.75x |
| Apr | $54.13 | 661 | 581 | 1.14 | $81.89 | 5.75% | 38 | 0 | $0 | – |
| May | $0 (no delivery) | – | – | – | – | – | – | – | – | – |

Jan–Feb total: $3,196.35 spend, 104 Meta purchases, $10,765 value, 3.37x Meta ROAS. Compare Shopify last-touch: 68 orders, ~$6,523, ~2.0x. Meta counts about 1.5x more. CTR is Meta's "CTR (all)".

## Gaps / what Blend can't return
1. **No change history.** We can't see the Jan–Feb CBO budget (only today's $152/day) or whether targeting and creative were edited after launch. Evidence that they were: ATC 90 was created Jan 15 (after launch), and the creative name is dated 2026-04-30. The Jan–Feb video, copy or URL may not be identical to what is shown now.
2. **Video ID mismatch** (935136142651962 vs 683036644759796). Check which video actually plays in Ads Manager preview before rebuilding.
3. **No post ID** (effective_object_story_id). It wasn't returned, so it's needed from Ads Manager to keep social proof.
4. **Advantage+ creative enhancements** (degrees_of_freedom_spec, music, etc.) were not returned. Check them in Ads Manager.
5. **Placements:** inferred as Advantage+ (automatic) because no placement fields were present. Not explicitly confirmed.
6. ATC 90's audience size shows only a lower bound of 20, so the real size is unknown.
7. In the CBO, the same campaign also funded ad sets 120240073446150396 (Broad Test Feb 1) and 120240962879370396 (copies). This ad's spend was Meta's allocation within the CBO, not a fixed budget.

## Duplication cautions (see 2026-10-20 memo)
An exact clone would include the ATC 90 warm pool and have no purchaser exclusion. That likely inflated the Jan–Feb ROAS. The 10-20 memo recommends an ABO test that excludes Purchase 180D, ATC 30D, IC 30D and visitors 30D, adds UTMs (`utm_campaign={{campaign.id}}&utm_content={{ad.id}}`), and runs at about $25/day.
