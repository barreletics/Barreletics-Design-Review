# Barreletics low-sales diagnosis — Thu Oct 22 2026 (pulled ~4:45–4:55 PM ET, read-only)
Window = 00:00–16:41 ET each day. "Web" = online-store orders, not cancelled.

## Most likely causes (ranked)
1. **Checkout completion collapse (not a traffic problem).** Same-hours funnel today vs prior 7-day avg (Oct 15–21):
   sessions **372 vs 249 (+50%)**, sessions w/ add-to-cart **16 vs 14.9**, reached checkout **10 vs 9.6**, **completed checkout 1 vs 5.0**.
   Checkout completion rate **10% vs ~52%** normal. Shoppers are reaching checkout at a normal rate and not finishing.
   Abandoned checkouts today: **6** (5 between 9:53 AM and 4:21 PM ET; 4 US with shipping address entered, $84–$162, mostly Closed Sole). Prior days: about 1–3/day.
   No Shopify incident (status page: "All Systems Operational", no unresolved incidents). `/checkout` returns 302 to the Shop Pay checkout. Payment step, shipping-rate step and error messages can't be seen read-only. **Next manual check:** open a real checkout to the shipping/payment step on mobile and desktop **without submitting**, and look at Shopify Payments/payout alerts in Admin.
2. **Small-number variance and a traffic-mix shift (secondary).** Web orders by 4:41 PM ET: today 1 vs prior-7 avg 4.3 and 28-day avg 3.9 (prior Thursdays 3, 3, 3, 4). If a day like that is normal, getting ≤1 order has about a 7% chance (Poisson). Extra sessions are from **social (219 so far, already a full-day level, 7-day avg ~219/day)** but social converted 1/219 to checkout. That could be low-intent or bot traffic. Search: 31 sessions (vs ~68/day). It does not explain normal checkout reach with near-zero completion.
3. **Ad delivery is not the cause.** Meta spend is $170 today so far (Prospecting CBO $109.68 / 109 clicks; Creative Test $60.80 / 46 clicks), with 4 pixel initiate-checkouts and 0 purchases. Google PMax 23842882230 is ENABLED/SERVING (primary_status LIMITED, same as all week): $39.87 / 24 clicks so far vs ~$80–100/day. Pinterest $23.01 / 15 clicks, normal.

## 50-point checklist
| # | Check | Status | Evidence |
|---|---|---|---|
|1|Orders today, all statuses|ISSUE|3 total: #6016 paid (app source 435840516097, no gateway), #6015 manual VOIDED and cancelled 11:23 AM, #6017 web paid via shopify_payments 3:54 PM. 0 drafts today. 6 abandoned checkouts|
|2|Orders by hour vs prior|ISSUE|Only web order at 15:xx. Prior 7 days had 3–5 by 16:41|
|3|Sessions by hour|OK|372 by 4:41 PM vs 249 avg (above normal)|
|4|Sessions by source|OK/WATCH|Today social 219, direct 120, search 31, email 0, unknown 2. Prior 7-day/day avg: social 219, direct 114, search 68|
|5|ATC rate|OK-low|16/372 = 4.3% (7-day same-hours 6.0%). Count is normal|
|6|Reached-checkout rate|OK|10 vs 9.6 avg|
|7|Checkout completion|**ISSUE**|1/10 = 10% vs ~52%|
|8|Abandoned checkouts|**ISSUE**|6 today (US×4, FR, CA). Reason not visible via API|
|9|Meta delivery|OK|$170 spent, 4,569 impressions, 155 clicks, both campaigns delivering. Statuses not pulled|
|10|Upgrade Your Grip|UNKNOWN|Not among spending campaigns yesterday or today (only Prospecting CBO + Creative Test)|
|11|Google PMax|OK|Serving, not on hold. $39.87/24 clicks so far. LIMITED all week|
|12|Pinterest|OK|$23.01, 916 impressions, 15 clicks (API account id 549756523361)|
|13|Homepage|OK (UNKNOWN load)|WebFetch renders fully. Box curl got 429 (bot rate-limit on box IP)|
|14|PDPs|UNKNOWN|429 from box. Products ACTIVE with online URLs|
|15|Cart page|UNKNOWN|429 from box|
|16|Checkout reachable|OK|/checkout 302 → shop.app Shop Pay checkout|
|17|Inventory top sellers|OK|Open Sole 750, Closed Sole 731 units. A few variants at 0 (e.g., Coperni M, Tight L, Water Shoes negative)|
|18|Published to Online Store|OK|Top products ACTIVE, published, onlineStoreUrl present|
|19|Prices/compare-at|WATCH|Top 5 products all edited today ~12:47 PM and ~3:54 PM ET. Prices $74/$78. Some Closed Sole variants have price 78 > compare-at 74 (odd but harmless)|
|20|Live theme id|UNKNOWN|App lacks read_themes|
|21|App installs/uninstalls|UNKNOWN|Not readable|
|22|Payment gateways|OK (partial)|Wallets: Shop Pay, Apple Pay, Google Pay. Today's web order used shopify_payments. PayPal not visible|
|23|Markets|OK|United States + International both enabled, USD|
|24|Shipping zones|OK|US: Standard $9.95, Free $0 (3–9 day), Priority $16.95, FedEx Economy $14.95, fedex carrier. AK/HI $16.95. The New Test Profile has an extra $0 "Standard"|
|25|Checkout settings|UNKNOWN|Not exposed; checkoutApiSupported=true|
|26|Discounts|OK|Active codes and automatic free shipping. Nothing expired today|
|27|Fraud/card testing|OK|1 voided manual order today. No cluster|
|28|Shopify status|OK|All Systems Operational|
|29|Meta/Google status|UNKNOWN|Not checked; ads delivering|
|30|Pixel firing|OK|Meta pixel ATC 1, IC 4, view content 93 today|
|31|Email sends|ISSUE?/UNKNOWN|0 email sessions today (7-day total: 1). Send logs not checked|
|32|Robots/password|UNKNOWN|429 from box|
|33|Storefront password|OK|Homepage renders publicly|
|34|SSL|OK|Cert valid until Dec 29 2026|
|35|Mobile render|UNKNOWN|429 from box|
|36|Cart JS errors|UNKNOWN|Not visible|
|37|Banner changes|UNKNOWN|No announcement seen in rendered homepage|
|38|Thursday seasonality|OK|Prior Thursdays by 4:41 PM: 3, 3, 3, 4 web orders|
|39|Refunds spike|OK|None today|
|40|Intl vs domestic|OK|All 3 orders US. Abandoned carts include FR and CA|
|41|Last order time|ISSUE|#6017 3:54 PM ET. Previous web order Oct 21 7:36 PM ET (gap ~20 hours)|
|42|Traffic but no orders?|**ISSUE**|Yes: traffic up, checkout reach normal, completions about 0|
|43|Wholesale/B2B tags|UNKNOWN|Wholesale codes active (pre-existing)|
|44|Calcurates|UNKNOWN|Carrier services (fedex/ups/dhl/usps) active. App effect not visible|
|45|Judge.me scripts|UNKNOWN|Judge.me coupon active. Script not checked|
|46|ChatGPT/organic|OK-low|Search 31 sessions so far|
|47|Product edits today|WATCH|Top products edited 12:47 PM and 3:54 PM ET today|
|48|Merchant feed|UNKNOWN|Not accessible|
|49|Inventory locations|OK|eFulfillment and Barreletics locations active and fulfilling. "Old Stock" location updated Oct 13|
|50|Other|NOTE|Orders from apps/drafts were cancelled in bulk on earlier days (Oct 4, 8, 13–15). Unrelated to today|
