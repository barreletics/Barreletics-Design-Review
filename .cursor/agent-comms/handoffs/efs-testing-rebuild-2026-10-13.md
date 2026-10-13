# eFS go-live testing: rebuilt state, 2026-10-13 (written ~6:30 PM ET, read-only)
Nothing was sent, changed or messaged while building this. All times are ET.

## Sources and gaps (read this first)
- **The ReadTranscript tool was NOT available to this agent.** I didn't call it on 31ff3976, 3c578a23, e2c461a2 or 69cd9920.
- Instead I used raw transcript pages that other agents saved earlier to /workspace/agent-tools/. All of them come from the current 3PL & Inventory conversation on Oct 13:
  - [T1] 95d23bea…txt: positions 329–383, 12:53–1:40 PM
  - [T2] dc232b80…txt: positions 442–518, 1:57–2:28 PM
  - [T3] 3b995cd1…txt: positions 519–583, 2:29–2:40 PM
  - [T4] 1ed4adcc…txt: positions 584–650, 3:56–4:08 PM
  - [T5] 1ab6df72…txt: positions 749–788, 4:20–4:31 PM
  - [T6] e70e53b8…txt: positions 789–858, 4:32–4:39 PM
- **Transcript pages I did not have:** positions 0–328 (before 12:53 PM), 384–441 (~1:40–1:57 PM, which includes the 65% decision and the Austin/Atlanta re-reads), and 651–748 (~4:08–4:20 PM). For the earlier history I relied on the box files.
- Earlier files used: [K] handoffs/efs-knowledge-2026-10-13.md; [H1] handoffs/2026-10-13-efs-testing-handoff.md; [H2] 2026-10-13-efs-golive-bot-retire.md; [H3] 2026-10-12-3pl-inventory-refresh.md; [TP] efs-golive-check/TEST-PLAN.md and TEST-PLAN-v2.md.
- Proof screenshots: [P] efs-receipts/proof/*.png. Gmail thread 1a1354c38479a59a: [G1] Andrew 9:26 AM, [G2] Eric 2:42 PM, [G3] Andrew **6:07 PM (sent)**.
- /workspace/efs-receipts holds inventory receipts, a landed-cost file and the proof screenshots. /workspace/efs-rate-cards holds the eFS 2026 rate-card xlsx files.

## 1. Settled decisions (newest wins)
| Item | Decision | Date | Source |
|---|---|---|---|
| Standard | $9.95, free at $150+ (USPS Ground Advantage) | Sep 17 lock; reconfirmed Oct 13 | K §5; G3 |
| USPS Priority | $18.95 → **$19.95** ("ok bumbp it to 19.95") | Oct 13 2:00 PM | T2 |
| AK/HI/PR | $18.95 → $22.95 (2:00 PM) → **$19.95** ("maybe we should put it at 1995") | Oct 13 4:36 PM | T2, T6 |
| Puerto Rico | Stays in the AK/HI/PR group. A separate PR rate was discussed but not done | Oct 13 2:02 PM | T2 |
| Ground service | Standard, free shipping and AK/HI/PR ship USPS Ground Advantage only. Priority, 2Day and Overnight ship only when the customer picks them ("we only ship ground advantage") | Oct 13 2:40 PM | T3, G3 |
| FedEx Ground Economy $17.95 | Andrew doesn't want it, and G3 tells Eric it's "removed from checkout." **It is still in the profile.** The bot said it wouldn't remove it until Andrew said to | Oct 13 4:34–4:35 PM | T6, G3 |
| FedEx Home Delivery | Not wanted (unreliable). Not offered at checkout | Oct 13 ~4:05 PM, 4:38 PM | T4, T6 |
| FedEx 2Day markup | 100% → 120% (Oct 12) → 75% (approved ~1:57 PM) → bot proposed 65% (2:11 PM) → G3 tells Eric **75%** | Oct 13 | K, T2, G3 |
| FedEx Overnight markup | 120% (Oct 12) → 60% approved → G3 tells Eric **60%** | Oct 13 | T2, T5, G3 |
| International | FedEx International Connect Plus only, +50%. No UPS or DHL | Sep 17; Oct 12 | K §5; P fedex-markup-65 |
| Weight | 1 lb per pair. Live shoes drop from 2 lb to 1 lb on go-live day | Sep 17 / Oct 12 | K §5 |
| Managed Markets (MM) | April out-of-stock errors (US and international) came from MM. Settled; don't ask Eric | Oct 13 4:01 PM | K correction, T4 |
| MM for testing | International has to be tested with MM OFF. It's a store-wide switch, so the test runs while the site is live, in a short window with Eric on the phone; MM goes back on afterward (Andrew's logic, sent to Eric as a question). Eric's 2:42 PM view: MM is product-level and the draft test item is ineligible. Not verified | Oct 13 4:30 PM; G3 6:07 PM | T5, G2, G3 |
| Connector & international | Nothing in the connector blocks international (Eric). Andrew told Eric to ignore that question | Oct 13 2:42 PM / 6:07 PM | G2, G3 |
| Flows | Yes to Eric bulletproofing or merging them into "one mega flow." All flows stay OFF until cutover | Oct 13 (G3); Oct 12 | G3, K §2 |
| Stock transfer | Eric moves the stock into the app location 114571313443 on go-live day | Oct 13 8:47 AM | K §4 |
| Location cleanup | After the transfer: eFulfillment Center 111727542563 online orders OFF; Old Stock 114832769315 out of the profiles with online orders OFF; both QC Holds OFF | Oct 13 9:26 AM (G1) | G1 |
| Routing | eFS first, Barreletics second; no other locations | Oct 13 9:26 AM (G1) | G1 |
| Test item | Closed Sole Test Item: TEST CS- SKUs (Eric), 1 lb, HS 640299. Plan: $100 storefront window, then unpublish | Oct 13 8:50 AM; G1 | K §3 |
| SKU mapping | eFS turns on the app SKU mapping at cutover. Until then, test orders don't reach eFS | Oct 12 | K §3 |
| Old API | Integration 5510 must be shut off at go-live (Layer 5). Who does it is unresolved | Oct 12–13 | H3, G1 |

## 2. Test plan as built, and what's done
**Plan sent to Eric on Oct 13 at 9:26 AM [G1]:**
1. Flow fixes
2. Location cleanup
3. $100 test item
4. Step 1: draft orders
5. Layer 1: domestic (routing, rates, transfer, fulfilment, tracking)
6. Layer 2: international function with MM on
7. Layer 3: international pricing with MM off, then back on
8. Layer 4: profitability vs. the 90–100 day invoice matrix
9. Layer 5: go live (old API off, products moved to the new profile, test every region in the first 5 minutes, phone window)

**G3 at 6:07 PM revised this to:**
- domestic draft orders (done)
- then domestic website checkouts to confirm the rates
- then Phase two, international: MM off in a short live window with Eric, test item visible, one order per region, then hide the item and turn MM back on

The bot's own TEST-PLAN-v2 (9:15 AM) has more detail: expected rates per state, international expectations ×1.5, and flow timing tests. [TP]

**Done (draft orders only; nothing paid, invoiced or completed; no checkouts, so no order numbers exist):**
- **Draft #D655** (https://admin.shopify.com/store/barreletics/draft_orders/1350627000611). Test item M (W 5.5-7.5)/Dusty Rose at $74, customer "eFS Test" (no email), MI tax $4.44. [T1, 12:53 PM]
- **Detroit 48226 at 120%:** Standard $9.95, Ground Economy $17.95, Priority $18.95, 2Day $59.53, Overnight $81.14. Proof: phase1-rates.png [T1]
- **Markup read (1:02 PM):** domestic "FedEx (own account)" had 2Day and Standard Overnight, 120% + $0. International FICP is 50%. AK/HI/PR had only Standard $18.95. Proof: fedex-markup.png [T1]
- **Five states at 120% (1:40 PM)** [T1; proof zones.png]:

| Location | 2Day | Overnight |
|---|---|---|
| Miami FL | $66.75 | $94.62 |
| LA CA | $59.53 | $99.13 |
| NY | $66.75 | $88.35 |
| Austin TX | $59.53 | $87.41 |
| Atlanta GA | $59.53 | $81.14 |

  The flat rates were exact in every state.
- **Profile change at ~2:04 PM** [T2; proof fedex-markup-new.png]:
  - Shopify would not allow a second FedEx (own account) option in the zone, so the bot fell back to one option: 2Day only at 75%, with Overnight removed.
  - Priority set to $19.95; AK/HI/PR set to $22.95.
  - Partial re-read at 75%: Detroit 2Day $47.36, NY 2Day $53.10, no Overnight offered.
  - The tab crashed. **D655 was left saved with the 100 Broadway, New York, NY 10005 address and no shipping line.** No later reset back to Detroit is recorded.
- **Analyses (read-only)** [T1–T3]:
  - eFS invoiced 2Day at $34.04–35.40 and Overnight at $40.20 (one data point).
  - PR via Priority was billed $17.66–18.26. Before eFS, PR Ground Advantage labels were $6.95.
  - Free shipping Apr 1–Oct 7: 73 orders. 35 two-pair orders were pushed under $150 by discounts.
  - Overnight orders: only #5743 ($104.14).
  - USPS Priority Mail Express is only a viable backup near Michigan.
  - eFS's Express rate card is wrong (it duplicates the Priority card).
- **Not run yet:**
  - the $149/$151 free-shipping draft
  - the multi-pair draft
  - AK/HI/PR drafts
  - Miami, Austin, LA and Seattle at the new markup
  - routing check
  - all storefront checkouts and international tests
  - flow tests [T2 2:12 PM list; TP]

## 3. New Test Profile 133926158627: last verified state
Latest proof screenshots: fedex-markup-65.png (4:13 PM) and akhipr-1995.png (4:38 PM). [P]
- **Profile:** "New Test Profile", 24 products. Fulfillment locations: Barreletics (Bloomfield Hills) and Efulfillment Service - 2015 (App). "Not fulfilling from": eFulfillment Center. **Old Stock does not appear** (contrast with the Oct 12 handoff, which had it in the profile).
- **AL, HI, and Protectorates (10 states):** Standard **$19.95** (verified 4:38 PM).
- **Domestic 48 + Armed Forces (52):**
  - FedEx Ground Economy $17.95 (still present)
  - Standard $9.95, free at $150+
  - USPS Priority $19.95
  - FedEx (own account): 2 services, 2Day + Standard Overnight, **handling fee 65%**, calculated
- **International (UAE, Argentina, Austria + 56 more):** FedEx (own account), FICP only, 50%.
- **⚠ Conflict:** G3 (sent 6:07 PM) tells Eric 2Day is +75% and Overnight +60%, and that Ground Economy was removed. The profile shows **65% for both**, with Ground Economy still present.
  - The bot told Andrew at 4:26 PM that only one FedEx markup per zone is possible, and offered either a flat Overnight rate or keeping 65%. No answer is recorded. [T5]
  - When Overnight was put back at 65% falls in transcript gap 651–748 (or 384–441). Only the 4:13 PM screenshot proves it.

## 4. What's left to test, in order (from G3 + T2 2:12 PM list + TP), with blockers
0. **Fix the profile to match what Eric was told** (Andrew's go is needed for each change):
   - resolve the markup (75/60 vs. the real 65/65)
   - remove FedEx Ground Economy
1. Finish the domestic drafts on D655 (reset the address first; it's on NY):
   - Miami, Austin, LA, Seattle at the current markup
   - $149 vs. $151 free-shipping check
   - multi-pair (2/3/6/10 pairs)
   - AK, HI and PR at $19.95
   - wholesale code 0-HWholesale
2. Routing check: the test order lands at the eFS app location first and Barreletics second. Shopify only shows routing on a placed order. [T1]
3. Domestic website checkouts (Layer 1 on the storefront): publish the test item at $100, place the orders, then unpublish. Test orders get tagged TEST ORDER, then cancelled, refunded and restocked. [G1, H3, TP]
4. Phase two, international: MM off in a live window with Eric, one order per region, FICP ×1.5 check, MM back on. Coordination is waiting on Eric's reply to G3.
5. Flow tests after Eric's rework (with Eric on the call; mapping off).
6. Profitability review against invoices (Layer 4); validate Overnight against the first real invoices.
7. Go-live (Layer 5):
   - stock transfer
   - location cleanup
   - weights to 1 lb
   - SKU mapping on
   - products moved to the profile
   - flows on
   - old API 5510 off
   - all-region tests
   - 48 h monitoring

**Blockers and answers to the specific questions:**
- **Test gift card:** the plan says pay by gift card [TP, H3], but **no specific test gift card is identified in any source I could read.** Unresolved.
- **Item visibility:** the test item is Active with all sales channels off, so it's not on the website (Andrew, Oct 13, G3/T4). Earlier scans saw it as DRAFT [H2]. Memory: "may be active but must not be shown on the storefront." It has to be made visible for steps 3–4.
- **Separate FedEx markups for 2Day and Overnight:** the bots found this is **not possible** as a second carrier option.
  - At 2:04 PM, Shopify disabled "FedEx (own account)" in the carrier dropdown when the bot tried to add a second option to the same zone.
  - Result: one handling fee per carrier option per zone. [T2]
  - Options the bot offered: a flat Overnight rate (e.g. $59.95) or one shared markup. No decision is recorded. [T2, T5]
- **Other open items (raise with Eric only if Andrew wants):**
  - who shuts off 5510
  - tracking push-back (trackingSupport=false)
  - whether the app needs routing
  - how international duties are billed and any per-order fee
  - empty-box weight
  - AK/HI calculated USPS option
  - API token lacks read_shipping/read_markets [K §9, H2]
- Eric hasn't replied to G3 yet (as of 6:07 PM sent).

## 5. What Andrew said NOT to do
- Don't ask Eric about the April out-of-stock errors. It was MM; settled (Oct 13 3:58/4:01 PM). [T4]
- Don't re-ask settled points. Check the Oct 12 meeting transcript first. Andrew doesn't want settled items re-asked. [H2, K §8]
- Don't ask whether eFS ships DDP; don't ask about Saturday shipping (Oct 4). [K]
- Don't recommend Managed Markets or the $99 Duty & Tax app (Oct 5). [K]
- Don't take Overnight off. "I never told you to take fucking overnight off" (Oct 13 4:08 PM). [T4]
- Don't put Ground Economy in the Ground Advantage shipping-method line (4:31 PM). No FedEx Ground Economy/SmartPost, no FedEx Home. [T5, T6]
- Don't change store settings without approval. A 4:36 PM voice note said the AK/HI/PR change wasn't approved, but Andrew's chat at 4:36 PM said "put it at 1995" and it was applied. [T6]
- Don't show the test item on the storefront outside a test window. [memory/T6]
- Don't uninstall the eFS app without re-approval (Oct 7). [K]
- Draft-first: never send email as Andrew. Order routing stays OFF/default with no custom rule. Ask before moving any order to eFS. Leave OD-* SKUs alone. [H3]
- Don't touch the 13 Global-e regions that have no rates (Oct 7). [K]
- Discard the old EFS Go-Live bot draft cards. [H2]
