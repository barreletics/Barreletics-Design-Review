# Barreletics conversion investigation: what's already been checked (as of 2026-10-24)

For the new site-audit bot. Everything below was read-only. No store settings were changed. All times are ET. V = verified (data or test). I = inferred. ? = unknown.

## Key metrics
- **ShopifyQL, 30 days to about Oct 23 (V):** US had 12,467 sessions, 707 with add-to-cart (5.7%), 429 that reached checkout and 215 completed, a **1.72% conversion rate**. Canada had 259 sessions, 21 carts, 16 checkouts reached and 4 completed (1.54%).
- **ShopifyQL by day, sessions / cart / checkout reached / completed (V; source: `/workspace/diag-1023-1635/sess_hour.txt`):** Oct 21: 455 / 31 / 20 / 7. Oct 22: 585 / 30 / 20 / 7. Oct 23 to about 4 PM: 331 / 22 / 9 / 2.
- **Real orders per day (V; `hourly.txt`):** 6 to 11 a day from Oct 10 to Oct 21, with one low day (Oct 14: 2). Then Oct 22: 4 and Oct 23: 1 (to 4 PM). Oct 20 4 PM to Oct 23 4 PM: 18 real orders, against a prior-7-day average of 24.1.
- **Traffic sources:**
  - On Oct 23 to 11:37 AM, sessions were 206: social 136, direct 42, search 26 (V).
  - Meta spend / link clicks / landing page views / purchases (Meta-reported, V): Oct 19 $256 / 123 / 116 / 5. Oct 20 $208 / 108 / 106 / 4. Oct 21 $213 / 133 / 126 / 1. Oct 22 $264 / 148 / 145 / 4.
  - Google PMax spend / clicks: Oct 19 to 22 between $78 and $101 a day and 47 to 57 clicks a day. Status is LIMITED, reason unknown.
  - Pinterest "Grok Restore Winner": about $25 a day, 12 to 23 clicks, 0 checkouts Oct 20 to 23.
- **Meta, Sep 23 to Oct 22 (V):** $7,318 spend, 66 orders, $5,833 sales, **0.80x ROAS**.
- **? Not checked:** 30-day conversion by source, mobile vs desktop, landing page, or new vs returning visitors.

## Tests and checks done
1. **Ad accounts.** Social Perf checked Meta, Pinterest and Google through Blend on Oct 23 at about 11:35 AM. All were delivering, with no disapprovals, billing blocks or spend limits (V).
   - Two Meta ads are paused, "Hear The Grip | Yellow Footwear" and "Yoga Socks Grippy". Who paused them is unknown.
   - The Meta pixel showed last fired Oct 22 at 7:58 PM. That is probably reporting lag (I), and it was not checked in Events Manager (?).
2. **Pre-cart visibility.** Website bot, Oct 23 at 11:38 AM.
   - Site, SSL, domain registration and Google search visibility are healthy (V).
   - ManyChat's API is live and the comment-to-DM flows exist (V).
   - Not seen: DNS records and Search Console.
3. **Payments and checkout, Admin API.** Oct 23 at 11:42 AM.
   - No failed, pending or authorized transactions since Oct 22. The only exception is #6015, a pending sale that was voided.
   - Risk was ACCEPT on #6026 to #6028.
   - Shop Pay, Apple Pay and Google Pay are listed as supported wallets.
   - Checkout loads with no captcha (V).
   - The status of the Shopify Payments account itself was not seen, because the token lacks `read_shopify_payments` (?).
   - Product edits around 10 PM on Oct 22 were only Judge.me widget refreshes. The 7:10 AM shop update showed no visible change. US shipping rates are intact (V).
4. **Real end-to-end test order #6029.** Oct 23, about midday.
   - Paid with a gift card using code 0-WHOLESALE-STUDIO: $740 became $370, total $392.20.
   - It created a real order. It was then cancelled, refunded and restocked (V). Checkout completes.
   - The $108 shown in the cart came from a test browser stuck in a Canada session (`/en-ca/`). The order itself recorded $74 USD (V).
5. **Clean-browser check (V).** A fresh visitor lands on barreletics.com with no redirect. Closed Sole shows $74 on the product page and in the cart, with no country popup.
6. **Canadian pricing / CAD.** Oct 23, using curl with fresh cookie jars and the Admin API (V). Details are in `findings/2026-10-23-canada-pricing/`.
   - A US IP gets `localization=US` and `cart_currency=USD` from the server.
   - Only `?country=CA` or `?currency=CAD` forces CAD. It persists for 1 year, and `?country=US` resets it.
   - The theme has no currency selector, no geolocation and no cookie writes.
   - 84 abandoned checkouts in 30 days: 26 internal tests and 58 real. Only 4 were in CAD, and 0 had a US shipping address with a non-USD currency.
   - All 253 US-ship orders were in USD.
   - Help Scout and Gmail had no complaints about currency.
   - Behavior for a Canadian IP was not tested (? box egress is US only).
7. **Help Scout scan (V).** About 200 conversations since Sep 25, all statuses. No customer reported a site, cart, checkout, payment, button or page-load problem. The only related items were 2 discount-code questions (SAVE10 had expired).
8. **Google Merchant Center** (browser; partial read, may have missed rows).
   - Approved products fell by 481 week over week, with a step drop around Oct 16 and 17 (V).
   - Issues: 133 products missing shipping info, mostly for Germany and the UK, 20 with an invalid price, 20 with a missing image, and 10 with an unavailable product page.
   - Open Sole and Water Shoes are not published to the Google channel. Closed Sole has no GTINs (V, Admin API).
   - Many sock variants are out of stock and ineligible.
9. **Wholesale draft #D663.** Not a retail blocker. A B2B company location had no address and one-time addresses were turned off, so the checkout became a draft (V). A guard routine now watches for this.
10. **Cart drawer "bounce" fix** went to the live theme Oct 22 at 5:10 PM (cart.js), and its smoke test passed (V). Its effect on conversion has not been measured (?).
11. **Earlier, Oct 4 to 7.** Go-live test checkouts passed (8 orders). A US test checkout worked on Oct 6 (V).

## Findings so far
- No technical blocker has been found in the ad accounts, domain, payments, checkout or currency (V, within the access limits noted above).
- Store-wide conversion is about 1.7% (V). About 6% of sessions add to cart and about 3.4% reach checkout (V). The biggest drop is before the cart.
- I think Oct 23's 5 checkouts with 0 orders by 11:40 AM is consistent with chance: about an 11% probability at the usual rate. Meta ROAS of 0.80x points to a traffic quality or offer problem, not a broken site (I).

## Open hypotheses (not ruled out)
- Paid social traffic is low intent, or the creative doesn't match the landing page (prospecting CBO and Creative Test). Conversion by source and by landing page has not been checked.
- Mobile product pages or the cart have UX friction: no session recordings or heatmaps are available, the theme liquid hasn't been read, and Lighthouse and page-speed audits have not been run.
- Shopify Payments account status: holds or verification problems (missing scope).
- The Meta pixel or CAPI is under-reporting, which would distort optimization. Not verified in Events Manager.
- Out-of-stock sock variants or sold-out variants on ad landing pages. Which variants the ads link to is unknown.
- Merchant Center approval drop around Oct 16 and 17, and missing GTINs, which limit PMax.
- Most checkout abandoners leave no email (429 checkout sessions vs about 38 real US abandoned checkouts with an email), so the step where they stop is unknown.
- How Canadian-IP visitors are treated, and whether any links in the wild carry `?country=CA`.

## Access gaps
`read_shopify_payments`, `read_themes`, `read_markets`, script tags and web pixels are blocked. There is no Search Console, TikTok or session-recording tool. The Papa Grok (58182956) transcript could not be read here, so this briefing relies on its saved files.

Sources: alternate-projects `docs/bots/funnel/` (findings, DECISIONS, HISTORY), `weekly-social/STATE-2026-10-23-midday.md`, the `shopify-theme/transcripts/f1b1afce…` Website transcript, `/workspace/diag-1023-1635/`.
