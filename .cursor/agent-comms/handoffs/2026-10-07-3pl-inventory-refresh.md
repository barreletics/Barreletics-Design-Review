# 3PL & Inventory refresh handoff (2026-10-07, from 3c578a23)
1. Role (Ops): owns the eFS connector go-live, shipping rates and markups, fulfillment Flows, all Shopify inventory writes (incl. PDS receiving at Barreletics, eFS ship-ups, corrections) and the eFS fee-agreement record. Skills: efs-ship-up, pds-receiving.
2. Rules: don't ping Andrew unless he messaged first or it's a true blocker. Low token. Draft-first, never send email as Andrew. Never say "gotten"; say "FedEx Connect". Never trash files without asking. Order routing stays OFF, no Shopify B2B. Inventory changes are add-only deltas. Read-only unless approved. Heavy analysis goes to Cursor agent bc-87c40cd0.
3. Test checkouts: use checkout-test-N@example.com (never Andrew or Stefanie emails) and close Shop Pay prompts. Test orders get tagged TEST ORDER, cancelled, refunded to gift card and restocked; never delete.
4. API helper /workspace/discount_switch/shop.py. Missing scopes: write_products, write_orders, write_gift_cards, read_markets, read_shipping, write_locations. The box browser is signed in to Shopify admin (since 10-07).
5. eFS app "eFulfillment Service 3PL" (reinstalled Sep 28) is STILL INSTALLED. Andrew said "wait" mid-uninstall; don't uninstall unless he re-approves.
6. Verdict (Cursor + my checks, ~95%): the app isn't causing the sales drop. Softness started Sep 24-25, Meta orders fell 52% on 19% less spend, US checkout completion held at 61-63%, and the app location 114571313443 has no stock, profile, market or orders, with auto fulfillment requests off. One caveat: if inventory sync ever marks sellable variants out of stock in feeds, disable the sync or uninstall then. Write-up: Barreletics-Design-Review branch grok/handoff-grok-director, .cursor/agent-comms/2026-10-07-efs-app-sales-investigation.md.
7. Gift-card test orders: all 4 (#5867 US, #5868-#5870 CA/DE/AE) are already cancelled, refunded to gift cards, restocked and tagged TEST ORDER. Nothing left for Andrew to cancel. The Canada order went through on gift card 2 after card 1 ran short by CAD 2.49.
8. Open: Coperni can't check out internationally. It's in "New Test Profile" (24 products, ships from Barreletics only), whose International zone has no rates. The fix is to add intl rates or move Coperni to General, but that needs Andrew's OK and he said to deal with it later. One Off products are Draft (done).
9. Open: 13 Global-e regions have no rates (Aruba, Bahamas, etc.). Andrew says it's been like this for months, so leave it.
10. Open (old handoff): PO-2001 ship-up and receipt, and eFS go-live waiting on Eric.
11. Logs: /workspace/checkout-tests/log.csv (T1-T19), /workspace/efs-golive-check/app-impact.md.
12. Andrew told to cancel Blend AI (Zaki doesn't use it).
13. Routines: none.
