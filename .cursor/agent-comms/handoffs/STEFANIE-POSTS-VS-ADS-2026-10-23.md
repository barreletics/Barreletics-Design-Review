# Stefanie's organic posts vs Meta ads vs Shopify orders — Sep 23 to Oct 23 2026

**READ-ONLY analysis. Nothing sent, changed or posted. Prepared for Andrew John. No customer details, no secrets.**
All dates/times America/Detroit (ET, UTC-4). Window = order/spend date **Sep 23 to Oct 23 2026** (31 days). **Oct 23 is a partial day** (pulls ~8:36 AM ET) and is excluded from all correlation stats (30 full days, Sep 23 to Oct 22).

## Bottom line
1. **I could NOT get post dates or views for Stefanie's organic posts.** Only one post link exists in the files (Instagram Venice post). Its date is only *derived* (about **Oct 18 2026, ~7:00 AM ET**), not read from Instagram. There are no views/reach/likes for any post, and no TikTok post list. So a real "posts vs orders" test **cannot be done yet**.
2. **Organic social drove very little last-touch revenue in this window:** Instagram organic 5 real orders ($518), TikTok 0, out of 199 real orders ($18,028). Meta ads were 66 orders ($5,833).
3. Ad spend and Meta-attributed orders only weakly line up day to day (r about 0.3 on 30 days; not reliable).
4. Oct 18 (the derived Venice post day) had the highest order count of the month (11 vs a 6.5 average), but it was also a Sunday and a high-spend day, and only 1 of the 11 was Instagram-organic. **One day, hypothesis only.**

## Sources and pull times
| Data | Source | Window | Pull time (ET) |
|---|---|---|---|
| Orders | Shopify Admin GraphQL 2025-10, `orders` connection, **no date filter** (sorted newest first, paged back to Sep 20), client_credentials app (SHOPIFY_GROK_ADMIN_*). 350 orders pulled, 279 created in window. Fields: createdAt, tags, cancelledAt, gateway, totals, `customerJourneySummary` lastVisit/firstVisit, landingPageUrl, referrerUrl. Script: `/workspace/scratch-posts/pull.py` | Sep 23 to Oct 23 (order created date, ET) | **2026-10-23 08:35:51** |
| Daily Meta spend per ad | Blend MCP `blendmcp_smart_query_meta`, account alias **bps-2c81**, level=ad, daily, 167 rows (2 pages, complete) | Sep 23 to Oct 23 | **~2026-10-23 08:36-08:38** (box clock 08:36:19 at the start) |
| Active-ad context | `/workspace/handoffs/META-ACTIVE-ADS-2026-10-23.md` | Sep 23 to Oct 23 | 2026-10-23 ~08:34 (as stated in that file) |
| Instagram post link | `/workspace/handoffs/2026-10-19-social-perf-refresh.md` line 20 (only post link found anywhere in handoffs) | n/a | file as of Oct 19 |
| Post date derivation | Instagram shortcode `DeohlT4CBvL` decoded locally (see section 3) + WebFetch of the post URL returning "5 days ago" | n/a | 2026-10-23 ~08:37 |
| TikTok profile | public page `tiktok.com/@barreletics` via curl | n/a | 2026-10-23 08:37 |

Cross-checks: per-ad Sep 23 to Oct 23 spend matches META-ACTIVE-ADS file (Hear The Grip Prospecting $1,915.00 now vs $1,914.92 earlier; UYG Feb $866.73 vs $866.46; new UYG Oct $137.42 vs $137.19; differences are Oct 23 spend still accruing). Total spend **$7,352.40** over the window (including $34.44 partial Oct 23). Order check: #5877 (ReturnZap) is present in the unfiltered pull and is excluded as an exchange.

## 1. Orders (Shopify)
**Exclusions applied (first match wins), 279 orders created in window:** TEST ORDER tag 47; cancelled (not already tagged) 9; $0 total 19; ReturnZap / Exchange Shipment 5. Extra safety rules (any other tag containing "test", gift_card gateway) removed 0 additional. **Real orders: 199.** (#5995 carries TEST ORDER so is excluded.)

**Sales** = order subtotal after discounts, excluding shipping/tax ($18,028.14; $20,253.14 total price including shipping/tax).

**Last-touch classification** (Shopify `customerJourneySummary.lastVisit`; falls back to "Direct / no journey data" when Shopify has no visit record):
- Meta ads = UTM source fb/ig/facebook/instagram with medium containing "paid" (paid_social).
- Pinterest = any Pinterest source/referrer/UTM (includes 1 Pinterest paid UTM and 3 organic/referrer).
- Instagram organic = Instagram/l.instagram referrer or ig/social, IGShopping, link_in_bio UTMs, with no paid UTM.
- TikTok organic = any tiktok source/referrer (0 found).
- Google/search = google pmax/product_sync UTM (55, which is Google PAID) plus organic search (13: Google SEO, Bing, DuckDuckGo).
- Email = shopify_email/newsletter. Direct = Shopify "direct" source (including self-referrals from barreletics.com) plus 7 orders with no journey record.
- "Other: Facebook no ad UTM" = Facebook referrer with no UTM (could be organic or untagged ads; not counted as Meta ads). Other = shop.com, ChatGPT, YouTube-type referrers.

| Class (Sep 23 to Oct 23) | Real orders | Sales |
|---|---|---|
| Meta ads (UTM) | 66 | $5,833.30 |
| Google / search (55 paid pmax, 13 organic) | 68 | $5,976.89 |
| Direct / no journey data (39 direct + 7 no record) | 46 | $4,608.15 |
| Instagram organic | 5 | $518.00 |
| Pinterest | 4 | $296.00 |
| Facebook referrer, no ad UTM | 4 | $359.20 |
| Email | 3 | $214.60 |
| Other | 3 | $222.00 |
| TikTok organic | 0 | $0.00 |
| **Total** | **199** | **$18,028.14** |

Instagram organic orders: #5866 (Oct 7), #5878 (Oct 8), #5926 (Oct 13), #5981 (Oct 18), #5989 (Oct 19). Last-touch only: organic posts can also seed orders that Shopify credits to direct/Google/Meta, so these are floor numbers.

Caveat: Meta itself reports **119 purchases** in the window vs Shopify last-touch Meta **66** (Meta counts view-through and 7-day click credit; Shopify counts last click). Not reconciled here.

### Daily orders by class, spend and sales (Sep 23 to Oct 23; Oct 23 partial)
| Date | Day | Spend | Real orders | Sales (after disc., excl ship/tax) | Meta ads | Pinterest | IG organic | TikTok | Google/search | Email | Direct/none | FB no-UTM | Other | Meta-ads $ | IG-organic $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-23 | Wed | $286.53 | 8 | $732.80 | 2 | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 0 | $148.00 | $0.00 |
| 2026-09-24 | Thu | $298.81 | 4 | $389.00 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | $0.00 | $0.00 |
| 2026-09-25 | Fri | $280.92 | 4 | $296.00 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | $148.00 | $0.00 |
| 2026-09-26 | Sat | $218.58 | 8 | $708.24 | 3 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | $336.60 | $0.00 |
| 2026-09-27 | Sun | $372.55 | 9 | $717.80 | 4 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | $351.60 | $0.00 |
| 2026-09-28 | Mon | $191.15 | 7 | $717.80 | 0 | 0 | 0 | 0 | 5 | 1 | 0 | 1 | 0 | $0.00 | $0.00 |
| 2026-09-29 | Tue | $301.62 | 10 | $858.00 | 7 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | $569.60 | $0.00 |
| 2026-09-30 | Wed | $279.83 | 8 | $659.20 | 3 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | $230.00 | $0.00 |
| 2026-10-01 | Thu | $264.67 | 7 | $517.30 | 3 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | $221.30 | $0.00 |
| 2026-10-02 | Fri | $256.17 | 9 | $1,059.00 | 4 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | $396.20 | $0.00 |
| 2026-10-03 | Sat | $199.24 | 3 | $285.20 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | $133.20 | $0.00 |
| 2026-10-04 | Sun | $298.61 | 5 | $430.74 | 1 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | $133.20 | $0.00 |
| 2026-10-05 | Mon | $277.14 | 7 | $870.00 | 0 | 0 | 0 | 0 | 3 | 0 | 4 | 0 | 0 | $0.00 | $0.00 |
| 2026-10-06 | Tue | $233.45 | 1 | $74.00 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | $0.00 | $0.00 |
| 2026-10-07 | Wed | $224.88 | 7 | $658.60 | 1 | 0 | 1 | 0 | 2 | 0 | 3 | 0 | 0 | $74.00 | $148.00 |
| 2026-10-08 | Thu | $271.16 | 4 | $440.80 | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | $152.00 | $74.00 |
| 2026-10-09 | Fri | $212.33 | 4 | $433.20 | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | $148.00 | $0.00 |
| 2026-10-10 | Sat | $184.20 | 7 | $654.62 | 2 | 0 | 0 | 0 | 3 | 1 | 1 | 0 | 0 | $148.00 | $0.00 |
| 2026-10-11 | Sun | $261.63 | 9 | $797.77 | 6 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | $570.40 | $0.00 |
| 2026-10-12 | Mon | $185.65 | 6 | $600.00 | 1 | 0 | 0 | 0 | 4 | 0 | 1 | 0 | 0 | $78.00 | $0.00 |
| 2026-10-13 | Tue | $188.08 | 8 | $670.00 | 1 | 1 | 1 | 0 | 3 | 0 | 2 | 0 | 0 | $74.00 | $148.00 |
| 2026-10-14 | Wed | $186.93 | 2 | $152.00 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | $78.00 | $0.00 |
| 2026-10-15 | Thu | $205.54 | 8 | $705.27 | 3 | 0 | 0 | 0 | 1 | 0 | 3 | 1 | 0 | $226.00 | $0.00 |
| 2026-10-16 | Fri | $214.96 | 8 | $592.00 | 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 2 | $148.00 | $0.00 |
| 2026-10-17 | Sat | $184.40 | 6 | $503.20 | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | $355.20 | $0.00 |
| 2026-10-18 | Sun | $298.93 | 11 | $818.00 | 3 | 1 | 1 | 0 | 4 | 1 | 1 | 0 | 0 | $222.00 | $74.00 |
| 2026-10-19 | Mon | $255.64 | 9 | $881.20 | 4 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 1 | $448.00 | $74.00 |
| 2026-10-20 | Tue | $207.77 | 8 | $659.20 | 3 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | $222.00 | $0.00 |
| 2026-10-21 | Wed | $212.76 | 8 | $851.20 | 1 | 0 | 0 | 0 | 4 | 0 | 3 | 0 | 0 | $74.00 | $0.00 |
| 2026-10-22 | Thu | $263.83 | 4 | $296.00 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | $148.00 | $0.00 |
| 2026-10-23 | Fri | $34.44 | 0 | $0.00 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | $0.00 | $0.00 |

Full CSV: `/workspace/handoffs/STEFANIE-POSTS-VS-ADS-2026-10-23-daily-orders.csv` (also includes per-class sales).

## 2. Daily Meta spend per ad (Blend, bps-2c81, USD)
Top five ads by window spend shown; every ad (23 ads with spend) is in `/workspace/handoffs/STEFANIE-POSTS-VS-ADS-2026-10-23-ad-spend-daily.csv`. Spend only (no conversion data used for attribution).

| Ad ID | Ad | Spend Sep 23 to Oct 23 |
|---|---|---|
| 120251073140990396 | IG Reel | Hear The Grip | Prospecting | Sep 2026 | $1,915.00 |
| 120250980208890396 | IG Reel | Hear The Grip | Sep 2026 | $1,478.02 |
| 120244905620190396 | Video # 01 – Corrected | $1,085.80 |
| 120251156105070396 | IG Reel | Upgrade Your Grip | Feb 2026 | $866.73 |
| 120250316994720396 | Pilates has evolved. Why hasn’t your footwear? Closed Sole | $472.68 |
| 120250979484300396 | IG Reel | Sock Era Is Over | Sep 2026 | $246.01 |
| 120251325637030396 | IG Reel | Hear The Grip | Yellow Footwear | Oct 2026 | $197.32 |
| 120251155780120396 | IG Reel | Grip Socks Weren't Built to Last | Oct 2026 | $182.36 |
| 120251114414630396 | IG Reel | Sock Era Is Over | Sep 2026 | $158.25 |
| 120251330490580396 | IG Reel | Do Your Yoga Socks Sound This Grippy? | Prospecting | Oct 2026 | $157.28 |
| 120250947084390396 | Grip socks had their moment. | $139.22 |
| 120251386386230396 | IG Reel | Upgrade Your Grip | Prospecting | Oct 2026 | $137.42 |
| 120250693286880396 | Pilates athletes deserve athletic footwear. – Copy | $85.71 |
| 120250693286860396 | Pilates athletes deserve athletic footwear. – Copy | $60.57 |
| 120250991212980396 | IG Reel | Hear The Grip | Sep 2026 | $46.56 |
| 120251035715960396 | IG Reel | Hear The Grip | Sep 2026 | $45.77 |
| 120251156273880396 | IG Reel | Do Your Yoga Socks Sound This Grippy | Oct 2026 | $33.12 |
| 120251035893220396 | IG Reel | Pilates Socks Era is over | Sep 2026 | $17.42 |
| 120251036108300396 | IG Reel | 100% Grip | Sep 2026 | $14.17 |
| 120250693286890396 | Video # 01 – New Ad Copy – Copy | $7.82 |
| 120250693286850396 | Pilates has evolved. Why hasn’t your footwear? Closed Sole – Copy | $2.37 |
| 120250693286900396 | Video # 01 – New Ad Copy – Copy | $2.00 |
| 120250693286830396 | Pilates has evolved. Why hasn’t your footwear? Closed Sole – Copy | $0.80 |

| Date | Day | Total spend | HTG Prosp Sep | HTG Sep (Creative Test) | Video #01 Corrected | UYG Feb 2026 | Closed Sole | All other ads |
|---|---|---|---|---|---|---|---|---|
| 2026-09-23 | Wed | $286.53 | $0.00 | $0.00 | $107.49 | $0.00 | $145.81 | $33.23 |
| 2026-09-24 | Thu | $298.81 | $0.00 | $0.00 | $93.09 | $0.00 | $30.91 | $174.81 |
| 2026-09-25 | Fri | $280.92 | $0.00 | $0.00 | $106.05 | $0.00 | $141.93 | $32.94 |
| 2026-09-26 | Sat | $218.58 | $0.00 | $59.77 | $83.75 | $0.00 | $18.89 | $56.17 |
| 2026-09-27 | Sun | $372.55 | $0.00 | $167.98 | $121.16 | $0.00 | $8.36 | $75.05 |
| 2026-09-28 | Mon | $191.15 | $0.00 | $83.54 | $81.56 | $0.00 | $6.78 | $19.27 |
| 2026-09-29 | Tue | $301.62 | $0.00 | $162.43 | $107.89 | $0.00 | $7.70 | $23.60 |
| 2026-09-30 | Wed | $279.83 | $0.00 | $145.42 | $101.55 | $0.00 | $11.73 | $21.13 |
| 2026-10-01 | Thu | $264.67 | $0.00 | $133.48 | $105.08 | $0.00 | $10.21 | $15.90 |
| 2026-10-02 | Fri | $256.17 | $37.85 | $110.74 | $67.99 | $0.00 | $17.29 | $22.30 |
| 2026-10-03 | Sat | $199.24 | $32.73 | $62.15 | $42.27 | $0.00 | $26.13 | $35.96 |
| 2026-10-04 | Sun | $298.61 | $46.05 | $68.65 | $67.68 | $0.00 | $46.33 | $69.90 |
| 2026-10-05 | Mon | $277.14 | $42.05 | $90.19 | $0.24 | $0.00 | $0.61 | $144.05 |
| 2026-10-06 | Tue | $233.45 | $14.29 | $123.90 | $0.00 | $0.00 | $0.00 | $95.26 |
| 2026-10-07 | Wed | $224.88 | $55.18 | $54.73 | $0.00 | $11.10 | $0.00 | $103.87 |
| 2026-10-08 | Thu | $271.16 | $118.13 | $14.59 | $0.00 | $21.45 | $0.00 | $116.99 |
| 2026-10-09 | Fri | $212.33 | $105.45 | $83.77 | $0.00 | $21.39 | $0.00 | $1.72 |
| 2026-10-10 | Sat | $184.20 | $91.14 | $57.07 | $0.00 | $35.99 | $0.00 | $0.00 |
| 2026-10-11 | Sun | $261.63 | $187.50 | $42.31 | $0.00 | $31.82 | $0.00 | $0.00 |
| 2026-10-12 | Mon | $185.65 | $137.01 | $17.26 | $0.00 | $31.38 | $0.00 | $0.00 |
| 2026-10-13 | Tue | $188.08 | $144.37 | $0.04 | $0.00 | $43.67 | $0.00 | $0.00 |
| 2026-10-14 | Wed | $186.93 | $142.20 | $0.00 | $0.00 | $44.73 | $0.00 | $0.00 |
| 2026-10-15 | Thu | $205.54 | $161.82 | $0.00 | $0.00 | $43.72 | $0.00 | $0.00 |
| 2026-10-16 | Fri | $214.96 | $153.04 | $0.00 | $0.00 | $61.92 | $0.00 | $0.00 |
| 2026-10-17 | Sat | $184.40 | $121.36 | $0.00 | $0.00 | $63.04 | $0.00 | $0.00 |
| 2026-10-18 | Sun | $298.93 | $143.88 | $0.00 | $0.00 | $97.70 | $0.00 | $57.35 |
| 2026-10-19 | Mon | $255.64 | $31.56 | $0.00 | $0.00 | $77.26 | $0.00 | $146.82 |
| 2026-10-20 | Tue | $207.77 | $33.22 | $0.00 | $0.00 | $72.22 | $0.00 | $102.33 |
| 2026-10-21 | Wed | $212.76 | $69.95 | $0.00 | $0.00 | $95.73 | $0.00 | $47.08 |
| 2026-10-22 | Thu | $263.83 | $41.30 | $0.00 | $0.00 | $101.07 | $0.00 | $121.46 |
| 2026-10-23 | Fri | $34.44 | $4.92 | $0.00 | $0.00 | $12.54 | $0.00 | $16.98 |

Spend pattern: roughly $190 to $300 a day all window (30-day mean $243.93/day). Mid-window, spend shifted from Video #01 / Closed Sole / Creative Test ads to Hear The Grip and UYG ads. Delivering ads now are only the 3 in META-ACTIVE-ADS-2026-10-23.md.

## 3. Stefanie's organic posts: what exists and what does not
**Verified (what I could actually obtain):**
- One post link in all handoffs: Instagram `instagram.com/barreletics/p/DeohlT4CBvL` ("Stefanie's Venice post"; only mentioned in a Oct 19 handoff about an unresolved IG product-tag problem). No post links, dates or views appear anywhere in `/workspace/handoffs` or `/workspace/handoffs/social-perf-2026-10-22` (they cover paid social; organic IG appears only as session/order buckets).
- WebFetch of that URL returned only "Instagram, 5 days ago" at ~8:37 AM Oct 23, with no views or likes.
- `curl` of the same URL and of the Instagram profile returned Instagram's logged-out error page (no post data). I did not try to log in or bypass anything.
- TikTok public profile `@barreletics` (curl, 8:37 AM Oct 23): **137 followers, 61 videos, 1,937 total likes**, bio "Barreletics. The grip shoe for Pilates & Barre. No socks. Just grip." The video list was empty to a logged-out fetch, so **no TikTok post dates or views**. I cannot confirm this is Stefanie's own account vs the brand account.
- Connectors checked: Blend (paid ad data only, no organic insights), Gmail (only TikTok Shop promo emails and an Oct 18 Meta invite, no post data), X (not relevant). No Instagram Insights or TikTok analytics connector is available to me.

**Derived, not verified:** Instagram shortcodes encode the media ID, which embeds a timestamp. Decoding `DeohlT4CBvL` gives **2026-10-18 about 06:59 AM ET**, consistent with the "5 days ago" label. Treat Oct 18 (Sunday) as the probable post date of the Venice post, pending Stefanie confirming. (A web-search summary also mentioned a "MEET STEPHANIE" reel dated Sep 23; the link it cited decodes to January 2024, so I discarded that claim.)

**Not obtainable:** dates, views, reach, saves, link clicks for any other post; any TikTok post; Stefanie's posting cadence; story posts.

## 4. Correlation: what the numbers do and do not say
Based on 30 full days (Sep 23 to Oct 22). Daily real orders: mean 6.63, std dev about 2.4 (range 1 to 11), so day-to-day swings of +/-2 orders are normal noise.

**A. Organic posts vs orders — cannot test.** Only one candidate post day (Oct 18, derived).
- Oct 18: 11 real orders, $818 sales, highest daily orders of the month (others in the top group: Sep 29 = 10; four days at 9). Rest-of-window average 6.48, std dev 2.3, so Oct 18 is about 2 std dev above typical. Oct 19 was 9 and Oct 17 was 6 (a three-day run of 6, 11, 9).
- Composition on Oct 18: Meta ads 3, Instagram organic 1, Pinterest 1, Email 1, Google 4, Direct 1. The **extra orders were not obviously Instagram organic**; the one organic IG order is a count of 1.
- Confounders on Oct 18: it was a Sunday (Sundays averaged 8.5 orders vs 6.6 other days, n=4 Sundays: 9, 5, 9, 11); it was also the highest-spend day of October ($298.93); relaunch and discount changes happened Oct 8.
- Instagram organic orders happened on Oct 7, 8, 13, 18, 19 (1 each). Can't tell which of those dates had a post. TikTok organic orders: 0 on every day.
- **Verdict:** one data point, **hypothesis only** ("Oct 18 may have been helped by the Venice post"); it is equally consistent with Sunday plus ad spend plus random variation.

**B. Meta ad spend vs orders (verified numbers, weak signal).**
- Daily spend vs Meta-attributed orders: Pearson r = 0.30 (Spearman 0.21). Spend vs total real orders: r = 0.24 (Spearman 0.28). Spend vs non-Meta orders: r = 0.03. Spend vs daily sales: r = 0.16. With n = 30, |r| below roughly 0.36 is not statistically distinguishable from zero.
- Previous-day spend vs next-day Meta orders: r = -0.33 (no lag effect; negative and not significant).
- Higher-than-median spend days (> $244.55) averaged 2.8 Meta-attributed orders vs 1.6 on lower-spend days; total orders 7.2 vs 6.1. Directionally consistent but small samples (15 vs 15 days).
- First half (Sep 23 to Oct 7): $3,984.15 spend, 31 Meta-attributed orders, 97 total real orders. Second half (Oct 8 to Oct 22): $3,333.81 spend (down 16%), 35 Meta-attributed orders, 102 total. Spend fell while Meta-attributed and total orders held, but the relaunch (Oct 8), discount-code removal and creative swaps all changed at once.
- Rough cost per Shopify last-touch Meta order: $7,352 / 66 = about $111 on window spend (Meta's own 119 purchases implies about $62). Show this as a range, not a verified CAC.

**C. Any overlap between organic posts and ads?** Not testable. The same Instagram reels are also run as ads ("IG Reel | Hear The Grip", "Upgrade Your Grip") and Meta ad traffic often arrives with `ig` UTMs, so organic and paid on Instagram share an audience and cannot be separated without post dates and Meta/IG insights. Also Meta orders by day don't jump on Oct 18 (3 vs a 2.2 average).

## 5. Verified vs hypothesis
| Statement | Status |
|---|---|
| 199 real orders / $18,028.14 in the window, classified as in the table | Verified from Shopify (last-touch UTM/referrer; classification rules are mine and stated above) |
| Spend $7,352.40 total, daily per ad | Verified from Blend/Meta |
| Instagram organic last-touch = 5 orders, TikTok = 0 | Verified (last-touch only) |
| Venice post was on ~Oct 18 | Derived from shortcode, probable, **unconfirmed** |
| Oct 18 was the best order day | Verified; **cause unknown** |
| Posts lift orders | **Hypothesis, untested** |
| Spend and Meta orders correlate weakly | Verified calculation; **not statistically reliable (n=30, r~0.3)** |
| Organic posts lift ad-attributed orders | **Hypothesis, untested** |

## 6. What Andrew/Stefanie need to provide
1. **List of posts** for Sep 23 to Oct 23: platform, link, posting date and time (ET), format (reel, carousel, story, TikTok), product featured, and whether a link-in-bio/IG product tag/UTM link was used. (Stefanie's Venice post date to confirm: Oct 18?)
2. **Instagram Insights export** (Meta Business Suite > Insights > Content > Export, daily, Sep 23 to Oct 23): views, reach, saves, shares, profile visits, **link/website taps**, follows, per post and per day.
3. **TikTok Analytics export** (TikTok Studio > Analytics > Content/Overview, CSV, same dates): video views, profile views, link clicks, per video with post time.
4. Which account is TikTok @barreletics (Stefanie's or brand), and whether the IG bio link uses a UTM (e.g. `utm_source=ig&utm_medium=social`/link_in_bio) so organic clicks are separable from paid.
5. Access: Andrew accepting the Oct 18 invitation to the "Barreletixx" business portfolio (email from Facebook, Stefanie Miller-Kwiatkowski) would let Blend/Meta read organic page/IG insights. His Facebook login is currently blocked by Meta "Verify account" per the Oct 19 handoff. I did not act on that invitation.
6. Optional: Shopify sessions by `ig/social` and `IGShopping` source by day (earlier work found session data unreliable, so unverified here). With ~10 to 15 dated posts, a simple post-day vs non-post-day comparison with a 0 to 2 day lag would be meaningful; with one post it is not.

## Files
- This report: `/workspace/handoffs/STEFANIE-POSTS-VS-ADS-2026-10-23.md`
- `/workspace/handoffs/STEFANIE-POSTS-VS-ADS-2026-10-23-daily-orders.csv`, `/workspace/handoffs/STEFANIE-POSTS-VS-ADS-2026-10-23-ad-spend-daily.csv`
- Scratch scripts and sanitized order-level classification (order number, date, class, amounts only): `/workspace/scratch-posts/`
