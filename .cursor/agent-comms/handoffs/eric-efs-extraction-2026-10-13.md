# Eric Madsen / eFS: go-live extraction (built 2026-10-13, read-only)
Source: Gmail `user-Gmail` (andrew@barreletics.com). All times are America/Detroit (ET). Nothing was sent, drafted or modified.

## Coverage and gaps
- Searches run: `efulfillmentservice.com in:anywhere` (3 pages, about 201 threads); `from:/to:/cc:madsen.e@efulfillmentservice.com` (2 pages, 80 threads, includeTrash); `from:madsen.e… before:2026/09/10` (snippets).
- **About 120 of the eFS-domain threads came back "The caller does not have permission"** and could not be read. They include many from Sep 30 to Oct 13 (for example 1a135c9f66d1b9bf, 1a1358ea62a38e4a, 1a1356f8…, 1a1353c4ecfef4f0, 1a1348e305db426b, 1a13230a5712f68f, 1a131143302a3ed9, 1a130aecaf46250f, 1a13041f…, 1a12f4…, 1a11ff4c0213ce80, 1a11cd09f83e2b29, 1a11c557b505b30e). Senders and subjects are unknown. They may be other eFS staff, support tickets, or alerts. Two Eric threads were also blocked: 1a0d882a73bdcb00 (Sep 25, 3 messages) and 1a0a2af863800b00 (Sep 15, 3 messages). The second message in the forwarded-notes thread 1a131efd5e1dcd60 also did not return.
- Other eFS senders that were readable but contain only system mail: support@, do.not.reply@ (Oct 6, several), billing@alerts (Oct 6), mailgun@alerts (Oct 8). hughes.s@efulfillmentservice.com appears Apr 14–15 (not read in full).
- The third results page of the domain search hit a Gmail rate limit (HTTP 429) and was not retried.
- `user-Gmail--personal`: no eFS mail ("efulfillmentservice.com OR eFulfillment" returned 0).
- Apr–Aug threads: I read only the key ones (Managed Markets/routing in April, OD SKU/inventory sync in June, Calcurates/rate cards in June–July, FedEx rate card in Aug–Sep). The rest are covered by snippets only.

## 1. Chronology (go-live relevant)

### Background (Apr–Sep 10)
- **Apr 16–17**, thread 19d97d0787335093, "Troubleshooting for Order Routing/International Orders through Managed Markets." This was the first app attempt. Sales dropped, and Andrew had set "sell when out of stock" on items eFS didn't stock. Eric (Apr 17 9:07 AM) explained the least-impactful way to pause: "unstock all of your SKUs from the EFS location using the bulk editor… unstocking is an extra step in addition to removing inventory." He also said deleting the app means "all the setup will have to be repeated." At 9:30 AM: "our app does not install either script tags or checkout scripts." At 4:07 PM: "the orders will remain unfulfilled until you manually mark them as fulfilled."
- **Apr 27 11:36 AM**, Eric, same thread: he linked the open API docs (https://fcp-api-docs.efulfillmentservice.com/). eFS "currently lack[s] a solution for submitting labels through our system"; pre-printed labels go through support tickets with a fee and lose eFS discounted rates. He suggested Andrew keep shipping through eFS even without the app.
- **May**: Brian Bolli built the API path (the "old API" / Brian's script). May 18: Eric confirmed orders 4426/4428/4429/4432 came through. May 19: no orders are marked as requiring insurance. May 29 (snippet): "there unfortunately isn't any incoming mapping that can be performed when orders are sent through the API."
- **Jun 15**, thread 19ecb338769ac1a7. OD SKU workaround: add the OD SKU and transfer stock, edit the order to the non-OD SKU, or place it manually in the FCP. Inventory sync "will run at whatever cadence Brian sets it up to run at… only works one way, so whatever you do with your inventory in Shopify will not effect our system." He suggested a US-only shipping profile for SKUs that should not take international orders.
- **Jun 26 9:33 / 10:58 AM**, thread 19efa6052c450d76. Eric sent the full 2026 rate cards: FedEx Ground Economy, 2Day, **Home Delivery**, Ground, 3Day Express Saver, Intl Connect Plus, Standard Overnight, Intl Priority/Economy, USPS Priority, Priority Express, Priority Intl, **Ground Advantage**, First Class Intl. He also sent standard packaging costs. **Fees:** "your pick and pack fees are set at $0.35 per item, and $1.25 per order, not the $0.60 per item and $2.00 per order on the general services page." Per-order cost breakdowns are under the blue "i" button on invoices.
- **Jul 7 10:08 AM**: on occasional DDP, "basically the plan would probably be to use your account to order labels from Shopify; I believe that should work without any issue, but I will confirm."
- **Aug 10/12**: labeling fee is "$22.50 + $0.25 per label for each job."
- **Aug 28 11:21 AM**, thread 1a048e839d3290f4: "I know we don't get a discount on surcharges… they don't need to be factored into the analysis." This conflicts with his Sep 16 statement below. Eric's task list: compare rates; wholesale default box; update the Flow to remove boxes on wholesale codes; add wholesale codes to the Flow; verify label printing on negotiated accounts. Andrew's tasks: annual Grow plan, discount codes, DHL usage report.
- **Sep 2 11:37 AM**: "there should be no unexpected issues this time around, and will make sure to perform extra testing to confirm before we begin the crossover. I will also confirm for certain that you will still have a process for printing DDP labels on your end." At 11:56 AM, Receiving agreed to count by the supplier's carton labeling if the packing slip notes it.

### Sep 11 – Oct 13
- **Sep 11 3:59 PM**, Eric, "Re: Timeline for connector needed": he proposed reviewing the setup with Brian on Monday and said "I think we can still go live with the new setup next week."
- **Sep 14 10:19 AM**, Eric: 3:30 PM preview meeting (invite at 10:22 AM, with Brian).
- **Sep 14 4:41 PM**, Eric, "Action Items for Wednesday" (thread 1a0a1a70f0d9ea9f): Andrew to move to the annual Grow plan "for carrier rating access," provide discount codes, analyze DHL usage, and "figure out markup on weights."
- **Sep 15 4:26 PM**, Eric: attached "Barreletics 2026 Invoiced Shipments.xlsx" and "EFS X Barreletics FedEx Rate Comparison 2026.xlsx." He asked to push the meeting to Thursday.
- **Sep 16 9:45 AM**, Eric, "Invoice PDFs attached to email?": "Our current system does not produce pdfs at all for invoices, it only produces Excel spreadsheets." There is a code freeze on the current FCP. He will ask accounting about a QuickBooks PDF option. **No follow-up found.**
- **Sep 16 12:09/12:10 PM**, Eric: sent the "Final" versions with zip/zone added. On air rates: "I didn't think we were going to include those in the shipping profile for customers to select."
- **Sep 16 4:30 PM**, Eric, on 2Day: order #4116 (2 lb, Zone 5) was billed $35.40 = rate $23.19 + $4.04 residential + $8.17 fuel. Retail all-in would have been $59.79, and "we also get discounts on fuel as well," so eFS came in $24.39 under retail. Air gets a smaller discount "because in general we don't ship air frequently." If Andrew can get $19 all-in through Shopify, "ship it from your location, or even print the label and send it to us and pay the $10 TPB fee." Routing rare 2Day orders to Barreletics is "certainly something we'd be able to set up in the shipping profile."
- **Sep 17 8:39 AM**, Eric: asked whether "Ground Advantage" meant USPS or FedEx Ground Economy, noting "We can still add in USPS retail rates and mark those down to meet our commercial rates." He also said eFS always batches after the 1:00 deadline. **Andrew 10:55 AM: USPS Ground Advantage.**
- **Sep 17 11:02 AM**, Eric: "if we are putting an automatic 30 minute hold on all orders on the Shopify side… I can adjust with a flow such that the hold does not apply from 12:30-1. I'll have to do some testing."
- **Sep 17 3:17 PM**, Andrew, "Barreletics Phase 1 Action Items for connector" (thread 1a0b0a4025908014), Phase 1 table: Standard (USPS Ground Advantage) $9.95; free at $150+; USPS Priority $18.95; FedEx Ground Economy $17.95; 2Day 120%; Overnight 100%; AK/HI/PR $18.95 USPS; International FedEx Connect 50% only; UPS/DHL dropped; weights unchanged in Phase 1 (moving to about 1 lb is Phase 2 with Brian). He attached a Shopify shipment sample CSV.
- **Sep 21 8:41/8:44 AM**, Eric: contaminated CS-MED-Black was removed and backorders ship, leaving 3 units. At 9:03 AM: "We do have lot tracking and do follow FIFO when required… client facing lot visibility in the FCP rewrite."
- **Sep 21 10:35 AM**, Andrew's checklist: wholesale direction "zero-h wholesale → Barreletics"; flows (30-min hold, 12:30–1 immediate, weekend 2-hour hold); DDP; snapshot/rollback; test orders; "Managed Markets off only when we're happy."
- **Sep 21 2:02 PM**, Eric, OD-LG-Y → CS-LG-Yellow: he created the OD SKU and will edit the order. "I'm pretty sure that the way the tracking component of Brian's script works that this will not cause problems… If there are issues with the tracking, you will be able to manually add the tracking by finding it in the FCP." Brian (3:55 PM): the tracking trigger is "the line item fulfillment's location ID being eFulfillment."
- **Sep 23 8:30/9:00 AM**, Eric: SKU done. When Andrew couldn't change the location ("api is blocking it"), Eric said "the order did come through."
- **Sep 25**: Eric sent a "Connector Testing" invite for 3:30–4:30 PM and offered Monday availability. Thread 1a0d882a73bdcb00 is unreadable.
- **Sep 28 10:32 AM**, Eric: meeting moved to 3:30 PM ("Touch down" invite).
- **Sep 29 2:18 PM**, Andrew: "Shopify is on the annual plan now." **Sep 30 11:59 AM**: "Grow plan is live."
- **Oct 1 12:53 PM**, Eric: the shipment was received Sep 30. "I should have everything in place and ready for us to touch base tomorrow morning." Andrew followed up on Oct 2 (12:31 PM and 2:57 PM), Oct 4 and Oct 6. **I found no Eric reply until Oct 8.**
- **Oct 4 5:43 PM**, Andrew: rates locked; the model shows 2Day, Overnight, Ground Economy and international at 50% all make money, with thin spots in Priority to the far West and heavier Standard orders. "Order routing stays off. eFulfillment is the default location, and wholesale goes to Barreletics through the Flow." On DDP, he is testing the FedEx Ship Manager app, and DDP inside Shopify appears to require FedEx's $99/mo Duty & Tax app. He asked Eric to "let me know if you see the same on your side." **Unanswered.**
- **Oct 8 4:00 PM**, Eric, "Re: Updates" (thread 1a11c0099d534f57): he had been home sick. "Let's plan on meeting Monday… I will make sure everything is in place and ready to go, and I'll make sure we have forward momentum from that point until we've fully transitioned."
- **Oct 12 10:34 AM**, Eric: meeting set for 3 PM (invite 1a1313d5acf9d266). At 4:50 PM he had not received the transcript yet.
- **Oct 12 5:05 PM**, Eric, "Fwd: Notes: 'Updates' Oct 12, 2026" (Gemini, auto-generated, "may contain errors"; thread 1a131efd5e1dcd60):
  - Eric built the shipping profile with test products copied from existing variants at 1 lb.
  - AK/HI/protectorates $18.95. Domestic 48 + armed forces: FedEx Ground Economy $17.95 and Standard $9.95, free over $150. USPS Priority flat $18.95. FedEx 2Day and Standard Overnight at a "120% markup from wholesale." International: Intl Connect Plus at 50% markup.
  - "EFS workflows remain inactive to prevent affecting current live orders." Flow 1 is a 30-min hold except 12:30–1:00. Flow 2 is a 2-hour hold from Fri 1 PM to Mon 7 AM. Flow 3 routes wholesale discount-code orders to the Barreletics location.
  - "The Barletics [sic] location will serve as the primary active fulfillment center within the new shipping profile." (This is probably a transcription error. Every other source says eFS first.) "Manage markets settings must be disabled prior to the final cutover." "Outdoor item variants require mapping to close soul [closed sole] products within the EFS app before launch."
  - Next steps: Andrew grants Eric draft-order permission; feeds the transcript to Grok; the group tests rates via draft orders; disable Managed Markets before going live; Andrew removes the old stock locations; map outdoor variants; live tests "tomorrow afternoon"; Eric sends the recording and screenshots.
- **Oct 13 8:45 / 8:46 AM**, Andrew, "Quick inventory question for go-live" (thread 1a1354c38479a59a): he asked whether eFS transfers stock into the app's location on go-live day, and whether the test-item SKUs duplicate the live SKUs.
- **Oct 13 8:47 AM**, Eric: "That's correct, we'll transfer the stock into the app's location on go-live day."
- **Oct 13 8:49 / 8:50 AM**, Eric: "I did add TEST to the SKUs for the test item, so there is no duplication, as I wanted to be able to test the connection once the Shopify side was tested."
- **Oct 13 9:26 AM**, Andrew sent the full plan:
  - Fix the flows: no weekend check on the 30-min flow, so weekend orders get a double request; the wholesale flow is in Draft, looks for "0-Wholesale" when the code is "0-HWholesale", and its move step is on the False branch; orders paid 12:30–1 can reach eFS before a wholesale move.
  - Questions: what caused the April out-of-stock errors; whether the connector limits international.
  - Location cleanup: turn off the old manual eFulfillment Center location; remove Old Stock and turn it off; turn off both QC Holds; routing eFS first, Barreletics second.
  - Test item at $100. Draft orders first.
  - L1 domestic: Standard $9.95 (free $150+), Ground Economy $17.95, Priority $18.95, 2Day/Overnight FedEx +120%, AK/HI/PR $18.95, transfer, fulfillment and tracking.
  - L2: international function with Managed Markets on. L3: Managed Markets off, check FedEx Connect +50%. L4: profitability review against the 90–100-day matrix.
  - L5: shut off the old API, move products from the test profile into the new profile, test all regions within 5 minutes, and review by phone.
  - Timing: 11–12 tests, meet at 12 or later.
- **Oct 13 2:42 PM**, Eric (msg 1a13692c823c030d):
  - "Flows: I did think that there could be an issue with flow interaction in the way that Grok indicates, but was planning on seeing how it went in testing… I can in fact bulletproof those flows, and maybe just turn it into one mega flow, which might work better."
  - "International: Nothing with the connector blocks or limits international."
  - "Managed Markets: Grok is actually wrong about this, because Managed Markets applies at the product level. The product we are using is ineligible for Managed Markets (mainly because it's draft, I assume), so my understanding is that Managed Markets does not apply. Layer 2 testing should confirm this."
  - He did not address the April out-of-stock question, location cleanup, rates, the old API, tracking, the phone window or timing.
- **Oct 13 6:07 PM**, Andrew (msg 1a1374e8d668abf1): ignore the connector/international question; "please go ahead and bulletproof them. One mega flow is fine." He described testing so far and gave the new rates, the shipping-method request and the Managed Markets plan (detailed in section 3). **No reply from Eric yet.**

## 2. What Eric has stated or agreed
- **Rates and markups as configured.** These come from Eric's forwarded Gemini notes of Oct 12, not his own words: Standard $9.95 / free over $150; Ground Economy $17.95; Priority $18.95; AK/HI/PR $18.95; 2Day and Standard Overnight at 120%; Intl Connect Plus at 50%. Andrew's Phase 1 table said Overnight 100%. The notes say 120% for both.
- **Fees.** Pick/pack is $0.35/item + $1.25/order (Jun 26). Labeling is $22.50 + $0.25/label per job. Applying a pre-printed label (TPB) is $10. Air shipments get a smaller discount. On surcharges Eric has said both things: "we don't get a discount on surcharges" (Aug 28), then "we also get discounts on fuel" (Sep 16).
- **Carrier mapping.** Eric asked on Sep 17 whether Ground Advantage meant USPS or FedEx Ground Economy, and Andrew said USPS. Eric has **not yet acknowledged** the Oct 13 request to ship Standard, free and AK/HI/PR as Ground Advantage only. **Home Delivery** appears only as a rate card Eric sent on Jun 26. No statement from Eric on mapping to it.
- **Flows.** He agreed to the 12:30–1 exception (Sep 17). Per the notes, the flows are built but inactive. Oct 13: he will bulletproof them, possibly as one mega flow.
- **Managed Markets.** The notes say it must be disabled before final cutover. Eric's Oct 13 view: it "applies at the product level," the draft test item is ineligible, so it doesn't apply, and Layer 2 should confirm.
- **Locations and inventory.** eFS transfers stock into the app's location on go-live day. The notes say Andrew removes the obsolete stock locations. They also say "Barletics location… primary," which conflicts with eFS-first and needs confirming.
- **Test item.** SKUs are prefixed "TEST", so there is no duplication. It was built from copied variants at 1 lb. Eric calls it "draft"; Andrew says it is Active with all channels off.
- **Old API / tracking.** Brian's script pulls tracking when the line item's fulfillment location is eFS. Tracking can be added manually from the FCP if needed. Inventory sync is one-way at Brian's cadence. The FCP has no inbound SKU mapping via the API. Eric has said nothing about shutting off the old API at go-live.
- **Order routing.** Rare 2Day orders can be routed to Barreletics in the shipping profile. Wholesale codes go to Barreletics via the Flow. Outdoor (OD) variants need mapping to closed-sole (CS) in the eFS app before launch.
- **International / DDP.** The connector doesn't limit international. For DDP, his plan was probably to use Barreletics' own account to buy labels in Shopify, which he said he would confirm (Jul 7, Sep 2). Not confirmed.
- **Billing.** No PDF invoices, only Excel. He would check QuickBooks with accounting. Open.
- **Lots.** FIFO/lot tracking is internal only.

## 3. What Andrew has told Eric (latest, Oct 13 6:07 PM)
- Disregard the connector/international question. Go ahead and bulletproof the flows (one mega flow is OK).
- Test status: the test item is **Active with all sales channels off**, and only Shopify draft orders have been used. Andrew believes draft-order rates equal checkout rates because both pull from the same profile, and asked "Do you agree?"
- **Current rates:** Standard $9.95, free over $150; USPS Priority **$19.95**; AK/HI/PR **$19.95**; FedEx 2Day = FedEx rate **+75%**; FedEx Overnight = FedEx rate **+60%**; FedEx Ground Economy **removed** from checkout.
- Standard, free and AK/HI/PR should **ship USPS Ground Advantage only**, and he asked Eric to set that.
- Next: domestic website test orders to confirm they match the drafts.
- International: he is confirming that Managed Markets must be off store-wide to test the new profile while live. He proposes a short phone window: Managed Markets off, item visible, one order per region, then hide the item and turn Managed Markets back on. He asked "How would you want to coordinate that?"
- Earlier: Grow plan is live (Sep 29–30). Routing is off with eFS as the default (Oct 4). He is testing the FedEx Ship Manager app for DDP.

## 4. Open questions
Asked of Eric, no answer found:
1. Do draft-order rates equal checkout rates? (Oct 13, 6:07 PM)
2. Will Eric set Standard, free and AK/HI/PR to Ground Advantage only? (Oct 13)
3. How to coordinate the Managed Markets-off international test window. This also needs Eric's product-level Managed Markets view reconciled with Andrew's store-wide view. (Oct 13)
4. What caused the April out-of-stock errors at checkout, and what's different now? (Oct 13, 9:26 AM; skipped in Eric's reply)
5. Location cleanup and the eFS-first, Barreletics-second routing; a phone window after go-live; timing (11–12 / 12+). (Oct 13, 9:26 AM; not addressed)
6. Whether FedEx's $99/mo Duty & Tax app is the only way to do DDP inside Shopify. (Oct 4)
7. The weekend hold and a snapshot/rollback of live settings. (Sep 21 checklist; status unknown beyond the notes)

Eric's own outstanding commitments:
- Confirm that Andrew can still print DDP labels with his own account (Jul 7, Sep 2).
- Check with accounting about QuickBooks PDF invoices (Sep 16).
- Send the meeting recording and screenshots (Oct 12 notes). Only the Gemini notes arrived.
- Bulletproof or merge the flows (Oct 13).
- Map OD variants to CS (Oct 12 notes).
- Unresolved discrepancies: whether the notes' "Barreletics primary" is a transcription error; Overnight at 100% (Andrew's Phase 1) vs 120% (notes); fuel and surcharge discounts.

## 5. The store and setup as Eric understands it
- There is a new shipping profile containing a test product (TEST-prefixed SKUs, 1 lb, copied variants). Eric believes the product is "draft" and so ineligible for Managed Markets. Andrew says it is Active with channels off.
- As far as Eric last confirmed (Oct 12 notes), the profile has the **old** rates: $9.95 / $17.95 GE / $18.95 Priority / $18.95 AK-HI-PR / 120% air / 50% international. He has not acknowledged the Oct 13 changes ($19.95, +75%, +60%, Ground Economy removed).
- The eFS flows (30-min hold with the 12:30–1 exception, weekend 2-hour hold, wholesale → Barreletics) exist but are **inactive**. He now plans to harden or merge them.
- Live orders still go through the old API / Brian's script. Stock moves into the app location on go-live day. Managed Markets is on in the live store. He expects the Layer 2 tests to show that Managed Markets doesn't affect the test item. The connector has no international limits.
