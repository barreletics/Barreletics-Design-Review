# eFulfillment (eFS) knowledge record — 2026-10-13 (written ~4:00 PM ET)
Read-only compile. Nothing was sent or changed.

**Source limits:** the cursor ReadTranscript tool was NOT available to this agent, so the bot transcripts for 69cd9920, 31ff3976, 3c578a23 and e2c461a2 were not read directly. This record is built from the derived box files those bots wrote:
- /workspace/fulfillment-handoffs/EFS-MASTER-KNOWLEDGE.md (MK), built Oct 12 from the raw ee353fac transcript plus the 3c578a23 and e2c461a2 extracts
- /workspace/efs-golive-check/previous-connection-timeline.md (TL, Oct 7) and REVIEW-2026-10-13.md (RV; cites Eric's Oct 12 meeting transcript, Drive doc 12hk-LkVTolgfLR0zuafizlQBYy1ePHRukYI_ffjAZk4)
- /workspace/handoffs/2026-10-07-3pl-inventory-refresh.md, 2026-10-12-3pl-inventory-refresh.md, 2026-10-13-efs-testing-handoff.md, 2026-10-13-efs-golive-bot-retire.md
- Gmail thread 1a1354c38479a59a, all 7 messages (Oct 13, 8:45 AM to 2:42 PM ET)

Anything marked [UNCERTAIN] could not be confirmed from these sources.

## 1. April 2026 out-of-stock errors: cause and resolution (ANSWERED, from the April record)
- Apr 6: the eFS app went live, and sales dropped right away (Andrew, May 26 email) (TL).
- **B1, domestic, Apr 6 to Apr 10/11:** items showed "sold out" or dropped out of the cart. **Cause: order routing / location priority was misconfigured.** It checked the eFS manual location first, then the eFS app, then Barreletics, then pickup, and products also had a duplicate manual eFS location. Andrew diagnosed and fixed it Apr 10–11 (Apr 11 9:36 AM email). On May 29, Andrew wrote that Shopify verified the routing was wrong (TL).
- **B2, international, Apr 6 to Apr 12:** every product showed "SOLD OUT." **Cause: Shopify Managed Markets (Global-e) with a 3PL-only setup.** MM needs a location that isn't tied to a 3PL. eFS agreed: Nick (Apr 14), Angela (May 26) and Steve (Jun 23). Workaround on Apr 11–12: "sell when out of stock" at Barreletics. On Apr 14, eFS removed the FedEx account from the international profile and put a 24-hour hold on the international method (TL).
- Apr 14–17 ("B3"): irregular sales. No clear cause; MM was still on. The app was disconnected on Apr 17. Losses were about $15K that week and $20K+ by May 4. Orders went through an API (Brian) from May 15–18, and the move back to the app was agreed on Jul 7 (TL).
- **What's different now (Oct 4 and Oct 12 decisions):** order routing stays OFF, MM goes off before the new rates go live (never both at once), every location has a rate for every zone, and extra locations get removed (MK §6; RV). On Oct 12, Andrew also tied the extra locations to the intermittent OOS (RV [00:14:10]).
- **Status of the question to Eric:** Andrew asked again on Oct 13 at 9:26 AM ("What caused them, and what's different now?"). **Eric's 2:42 PM reply did not address it.** The answer is already on record from April, so it doesn't need to be re-asked unless Andrew wants Eric's own statement.

## 2. Connector, app and flows
- New "eFulfillment Service 3PL" app installed Sep 28; its location is "Efulfillment Service - 2015" 114571313443 (TL, Oct 7 handoff). Andrew said "wait" mid-uninstall; don't uninstall without his re-approval (Oct 7).
- Old Integration 5510 / API still sends orders to eFS. It must be retired before go-live because of the double-injection risk (Oct 12 handoff). Andrew's Oct 13 plan, Layer 5: "Shut off the old API connection." Eric said on Oct 12 that the old location would be left in place but kept off the profile (RV). [UNCERTAIN] Who actually shuts off 5510, and when.
- eFS portal: automatic fulfillment requests = No (MK).
- Grow plan plus Barreletics' own FedEx account: done; Eric has the account (Oct 4, MK). It's used only for 2Day, Overnight and FedEx Connect (Oct 12 meeting, RV).
- Profile switch: products move from General into New Test Profile. There's no on/off switch (Oct 12, RV).
- **Flows (Eric's build, Oct 12):** 30-minute hold with an immediate send 12:30–1:00 (eFS cutoff is 1 PM), a 2-hour weekend hold, and a wholesale move flow on the code `0-HWholesale`. All three are OFF until cutover (Oct 12, RV; Oct 13 handoff).
- Flow defects found Oct 13 (from Andrew's screenshots) and sent to Eric at 9:26 AM:
  - the 30-minute flow has no weekend check, so the weekend hold doesn't work and may send a duplicate request
  - the wholesale flow is still Draft, matches "0-Wholesale" instead of "0-HWholesale", and its move step looks wired to the False branch
  - a race in the 12:30–1:00 window
- **Eric's reply (Oct 13, 2:42 PM):** he suspected the interaction too and planned to see it in testing. If Grok is concerned, he can "bulletproof those flows" and maybe merge them into "one mega flow." → Andrew still needs to say yes or no.
- Wholesale code case sensitivity is unclear (Oct 12, RV). Saturday: Andrew believes eFS doesn't ship Saturdays; don't ask (Oct 4).

## 3. SKU mapping and the test item
- At cutover, eFS turns on the app SKU mapping (outdoor → Closed Sole). Until then, test orders request fulfillment but won't reach eFS (Eric, Oct 12, RV). If mapping goes on earlier, test orders WILL reach eFS.
- **Test item SKUs (SETTLED Oct 13, 8:50 AM):** Eric confirmed he put "TEST" in front of the test item's SKUs, so they don't duplicate live SKUs. The Oct 13 scan saw TEST CS- SKUs. The item is DRAFT, 1 lb, HS 640299, all Closed Sole variants.
- Test plan (Andrew, Oct 13 email): publish the test item at $100 for testing, then unpublish it.
- Eric says MM applies at the product level, and the draft test item is ineligible, so MM shouldn't affect it. Layer 2 should confirm (Eric, Oct 13 2:42 PM). This contradicts Grok's "MM works by country" line in Andrew's email. **[UNCERTAIN] not verified.** The token lacks read_markets.

## 4. Locations and inventory
- Barreletics 31315624039; eFulfillment Center 111727542563 (manual location created Apr 4, holds the real eFS stock); app location 114571313443 (empty); Barreletics Old Stock 114832769315 (online orders ON, in General + New Test profiles); 2 QC Hold locations (Oct 12 handoff, Oct 13 email). Oct 13 scan: all 4 main locations are active and fulfill online orders.
- **Stock transfer (SETTLED Oct 13, 8:47 AM):** Eric: "we'll transfer the stock into the app's location on go-live day."
- Andrew's cleanup plan (Oct 13 email): after the transfer, turn off online orders at the eFulfillment Center location; take Old Stock out of the profiles and turn off its online orders; turn off online orders at both QC Holds; routing order is eFS first, Barreletics second. Eric raised no objection (his 2:42 PM reply didn't comment on it).
- Oct 12 count applied to Barreletics (31 SKUs); old stock moved to Old Stock (OS-LG Blue 114, Black 110, DGY 46, Yellow 74). Gaps between the eFulfillment Center location and eFS's own count: LG-Yellow 5 short, LG-DR 1 short (fix offered, not applied). The Sep 28 ~120-pair ship-up is superseded by the count (Oct 12 handoff).
- An unsent draft card to Eric about old stock being separate is Andrew's call (Oct 12). The EFS Go-Live bot's older draft cards are obsolete (Oct 13).

## 5. Shipping method mapping and rates (SETTLED)
- Standard USPS GA $9.95; free at $150+; USPS Priority $18.95; FedEx Ground Economy $17.95; FedEx 2Day = quote +120%; Standard Overnight = quote +120% (Andrew corrected this Oct 12 from the Sep 17 lock of 100%; matches Eric's build); AK/HI/PR $18.95; international FedEx Connect only, +50%; no UPS or DHL; 1 lb per pair (Sep 17 lock, Oct 12–13 confirmations; Eric confirmed the built rates in the Oct 12 meeting).
- "%" means extra on top of the FedEx account quote (Oct 4 / Oct 12).
- Weights: live shoes go from 2 lb to 1 lb on go-live day. Clothing weights and the empty-box weight are still unconfirmed (Oct 12).
- Reopened Oct 12: AK/HI might get a calculated USPS option alongside the flat rate (a 10-pair order at flat). Eric suggested it; not decided (RV).
- Andrew is worried about Overnight; it rests on a single eFS invoice (Oct 12, RV). Whether to keep Ground Economy was never formally closed (MK).
- Draft orders may not show calculated FedEx rates. Eric has Drafts permission and was going to check (Oct 12).

## 6. International, DDP, Managed Markets
- **Connector (SETTLED Oct 13, 2:42 PM):** Eric said nothing in the connector blocks or limits international.
- International ships from eFS on FedEx Connect (Oct 12 meeting: "have you guys ship it").
- DDP: Andrew, Oct 4: "EFS does ship DDP. We already know that." Don't re-ask whether eFS ships DDP. For self-shipped international, use the free FedEx Ship Manager pull app, not the $99 Duty & Tax app (Oct 4–5). Finance rule: don't recommend MM or the $99 app (Oct 5).
- **Still open:** how eFS bills duties (to Barreletics' FedEx account as shipper or third party?) and the per-order fee. The eFS FAQ lists $10/order for shipping on a seller's own account. Raised Oct 4 and in the Oct 12 meeting; never answered (MK §9 #1; RV).
- MM was still ON as of Oct 12. The plan is to turn it off with Shopify's off button before go-live. Andrew's Layer 3 turns MM off briefly to test international pricing; Eric's product-level comment may change whether that's needed.
- 13 Global-e regions have no rates; leave them (Andrew, Oct 7). Coperni international is fixed (Oct 12).
- HS codes set Oct 12: kids Outdoor 640299, Fabric 610990, Studio Sample 640299, Knee tights 610463. SAMPLE ITEMS untouched.

## 7. Billing and fees
- Agreement (Steve, accepted Jul 7, effective Jul 13): no base or storage fees Jul 13 2026–Jul 12 2027, then 50% Jul 13 2027–Jul 12 2028. Oct 5 review: $0 base and $0 storage on all 10 invoices since Jul 13.
- Oct 6: Andrew asked Steve about the second-year 50% rate (Gmail inbox handoff). [UNCERTAIN] Reply status unknown.
- Air billing: eFS bills ~$34–35 for 2Day (card + residential + fuel). Eric said the card is correct (Sep 16–17). Labor: $1.25/order + $0.35/item.
- eFS invoice 584171 is link-only; don't chase the portal (Oct 9).

## 8. Questions to Eric that are SETTLED (do not ask again)
Rates and the markup meaning; FedEx account connection; test item build and TEST SKUs (Oct 13); stock transfer into the app location on go-live day (Oct 13); connector doesn't block international (Oct 13); the existence and logic of the flows; the wholesale code prefix; test method (draft orders, then a $100 storefront window); Drafts permission; order routing OFF; profile switch method; eFS ships DDP; Saturday shipping (Andrew said don't ask); the April cause (on record from April).

## 9. Genuinely open (as of Oct 13, ~4 PM ET)
To TELL Eric / decide:
1. Yes or no on his offer to bulletproof or merge the flows (recommended given the confirmed defects). Wholesale code case sensitivity can be folded into that fix.
2. Andrew's response to Eric's MM product-level point: test it in Layer 2, and decide whether Layer 3 (MM off) is still needed.
3. Confirm the timing for today's or the next call. Andrew proposed 12 PM or later on Oct 13; Eric replied at 2:42 PM without naming a time. Also ask for a phone window right after go-live (asked, not answered).
4. Confirm the location cleanup plan and that the eFS → Barreletics routing order is fine (sent, no comment from Eric).

To ASK Eric (never answered):
5. Who retires Integration 5510 / the old API at cutover, and when.
6. Does the app push tracking back to Shopify? (trackingSupport=false; not discussed)
7. Does the app need Shopify order routing on? (asked Oct 12, unanswered)
8. International duties: billed to Barreletics' FedEx account? Any per-order fee?
9. Empty-box weight. AK/HI calculated USPS option (Eric proposed it; Andrew needs to decide).

Internal, not for Eric: Overnight markup validation against billing history; the LG-Yellow/LG-DR count gaps; the old-stock selling decision; the eFS international invoice to validate the +50%.


## CORRECTION (Andrew, 2026-10-13 4:01 PM ET)
The April 2026 out-of-stock errors, US and international, came from Managed Markets. Settled. Do not ask Eric about April.
