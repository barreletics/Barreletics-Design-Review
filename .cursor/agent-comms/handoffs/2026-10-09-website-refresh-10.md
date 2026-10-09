# Website bot handoff — refresh #10 (from 30d4abb2, 2026-10-09)
Role: Barreletics Website (Site Design). Short, plain, no-jargon replies to Andrew.
LIVE theme 187144929571 (site live since 2026-10-08 ~1:02 PM ET). Any push to it needs Andrew's explicit go. Never publish the working copy. Copy only the approved single file: --only <file> --nodelete --allow-live, back up first, md5 pull-verify. Shopify CLI runs on Mac b9c0e142.
Working copy (unpublished) 188900901155: all edits go here first.
Baseline: never restore anything older than Mac ~/grok-theme-backups/snapshots/2026-10-08-1445-BASELINE-post-launch (box /workspace/baselines/).
Last live pushes 2026-10-08: currency/free-ship fix at ~3:05 PM (cart.js 1e242a1d…, variant-selector.js 48b286b4…, sticky-atc.liquid 84e285c8…, main-cart.liquid 4a58ab25…); stars at ~7:24 PM (sections/pdp-buy-box.liquid c56d63c16ccc2f554e57d3a4639b0078, lines 920-921 read reviews.rating metafields; rollback ~/grok-theme-backups/2026-10-08/stars-live-pre/*.live-pre-stars-7035ea0d…).
Stars: hidden structured data only. Open Sole 4.97/152, Closed 4.99/93, Aquatic 4.98/59, Pants 4.9/10, Tee 5.0/1. Coperni has none (not fixed; offered). Never touch Judge.me, hidden reviews, widgets or app embeds. The number must never be shown on the page.
Blogs fixed 2026-10-08 (3 articles). Sheryl C. Coperni review photo 404 left alone (no go).
Open, waiting on Andrew: Coperni rating; 4 gift-card test orders (2 US, UK, CA; never started; refund to card, restock, tag TEST ORDER, no email); 8 continue-selling variants.
Orders: card/Shop Pay = real, gift card = test, Zaki = tester. Fulfillment is manual; don't flag eFS. Real sales after launch: #5892, #5894 (FB "Hear The Grip" reel). #5895 = Zaki test.
Ads/Merchant/GA4 belong to Social Perf 9692c727 (Meta via Cursor bc-3fa70894; no Google Ads/Merchant access). Andrew was upset it seemed unconnected, and his connection location is still unresolved there.
Routines: none (launch-day order watch deleted itself 2026-10-09). Admin API helper: /workspace/test-order-cancel-20261008/sh.py (/workspace/.shoptok expired; uses app creds).
