# Barreletics eFS go-live: MASTER source of truth (2026-10-13, ~6:50 PM ET)
Read-only consolidation. Nothing was sent, changed, or messaged. Andrew's binding decisions (Oct 13) override every older file.
Sources: [MK] fulfillment-handoffs/EFS-MASTER-KNOWLEDGE.md; [KX3c]/[KXe2] KNOWLEDGE-EXTRACT-3c578a23/e2c461a2; [RM] EFS-FULL-RATE-MATRIX.md; [RB] READINESS-BRIEF; [WS] WEIGHT-SWEET-SPOT-MODEL; [DDP] DDP-LABEL-RESEARCH; [K] handoffs/efs-knowledge-2026-10-13; [TR] efs-testing-rebuild-2026-10-13 (its cited transcript pages T1–T6 and proof PNGs); [EX] eric-efs-extraction-2026-10-13; [H1] 2026-10-13-efs-testing-handoff; [D3c] agent-tools/018f408e… (3c578a23, pos 426–472, Oct 7 era); [D31] agent-tools/e1a24a10… (31ff3976, pos 266–347, Oct 12–13 inventory); [G3] Andrew → Eric email, 6:07 PM ET Oct 13 (sent).
Superseded wholesale: [H1] and [RM]/[K]/[EX] "Phase 1" rate lines (120%/120%, Priority $18.95, GE $17.95, AK/HI/PR $18.95).

## 1. Settled decisions  (🔒 = never re-ask)
| # | Decision | Date | Source |
|---|---|---|---|
| 1 | 🔒 FedEx 2Day = FedEx own-account quote **+75%** (approved ~1:57 PM). The 65% in the profile was a bot workaround, NOT Andrew's decision | Oct 13 | Andrew; TR(T2); G3 |
| 2 | 🔒 FedEx Standard Overnight = quote **+50%** (changed from 60%, Andrew ~6:55 PM Oct 13; Eric was told 60% at 6:07 PM) | Oct 13 | Andrew voice call |
| 3 | 🔒 Overnight stays offered. "I never told you to take … overnight off" (4:08 PM) | Oct 13 | TR(T4) |
| 4 | 🔒 Standard $9.95, free at $150+, ships USPS Ground Advantage | Sep 17; Oct 13 | MK; G3 |
| 5 | 🔒 USPS Priority **$19.95** ("bump it to 19.95", ~2:00 PM) | Oct 13 | TR(T2); G3 |
| 6 | 🔒 AK/HI/PR **$19.95** via USPS Ground Advantage (4:36 PM; $22.95 at 2:00 PM superseded). PR stays in the AK/HI/PR group | Oct 13 | TR(T2,T6); G3 |
| 7 | 🔒 Only Ground Advantage for Standard/free/AK-HI-PR; Priority/2Day/Overnight only when the customer picks them | Oct 13 2:40 PM | TR(T3); G3 |
| 8 | 🔒 FedEx Ground Economy **removed** (closes MK §9 "keep or drop"). No FedEx Home Delivery, no SmartPost | Oct 13 | TR(T4–T6); G3 |
| 9 | 🔒 International = FedEx International Connect Plus (FICP) only, **+50%**; no UPS/DHL | Sep 17; Oct 12–13 | MK; G3 |
| 10 | 🔒 International tested live with **Managed Markets OFF**, one order per region, short window, Eric on the phone; MM back on after | Oct 13 | TR(T5); G3 |
| 11 | 🔒 April 2026 out-of-stock errors (US and intl) were caused by Managed Markets. Do not ask Eric | Oct 13 4:01 PM | K correction; TR(T4) |
| 12 | 🔒 1 lb per pair; live shoes 3 lb (Andrew 10/14 correction) → 1 lb on go-live day | Sep 17; Oct 12 | K §5 |
| 13 | 🔒 "%" = extra on top of the FedEx account quote | Oct 4/12 | K §5 |
| 14 | 🔒 eFS ships DDP; don't ask. Don't ask about Saturday shipping | Oct 4 | K §6, §2 |
| 15 | 🔒 Don't recommend MM or the $99 Duty & Tax app | Oct 5 | K §6 |
| 16 | Flows: yes to Eric bulletproofing/merging them ("one mega flow"); all flows OFF until cutover | Oct 13 (G3); Oct 12 | G3; K §2 |
| 17 | 🔒 Stock transfer into app location 114571313443 by eFS on go-live day | Oct 13 8:47 AM | K §4 |
| 18 | Location cleanup after transfer: eFS Center 111727542563 online orders OFF; Old Stock 114832769315 out of profiles + online OFF; both QC Holds OFF | Oct 13 9:26 AM | K §4 (G1) |
| 19 | Fulfilment priority: eFS app location first, Barreletics only fallback; Old Stock/QC never for online | Oct 13 | G1; D31 memory |
| 20 | 🔒 Test item: TEST CS- SKUs, 1 lb, HS 640299; $100 storefront window then hide | Oct 13 8:50 AM | K §3 |
| 21 | 🔒 SKU mapping turned on by eFS at cutover; until then test orders don't reach eFS | Oct 12 | K §3 |
| 22 | 🔒 Connector doesn't block international (Eric); Andrew told Eric to ignore that question | Oct 13 | K §6; G3 |
| 23 | Old API / Integration 5510 must be off at go-live (who does it: OPEN) | Oct 12–13 | K §2 |
| 24 | 13 Global-e regions without rates: leave them | Oct 7 | K §6 |

**Conflicts flagged**
- C1 Markup: Eric told 75/60 (G3); profile shows **65%/65%** (TR §3, proof fedex-markup-65.png 4:13 PM). Andrew's 75/60 wins; profile is wrong.
- C2 Ground Economy: G3 says "removed from checkout"; profile still has it at $17.95 (TR §3). Profile is wrong.
- C3 Order routing: K/MK say "order routing stays OFF / default"; D31 memory (Oct 13) records live routing rules (MM supported-locations constraint → Minimize split → Ranked locations). Need one verified read before go-live.
- C4 MM scope: Eric (2:42 PM) says MM is product-level and the draft test item is ineligible; Andrew's plan treats MM as store-wide. Unverified (token lacks read_markets). Andrew's decision #10 governs the test regardless.
- C5 Old Stock in profile: Oct 12 handoff had it in General + New Test; TR's last read (4:13 PM) doesn't show it in New Test Profile.
- C6 Test item status: earlier scans DRAFT; Andrew Oct 13 says Active with all channels off.
- C7 3c578a23's earlier live set (Oct 7: Priority $16.95, GE $14.95, 90% handling, AK/HI $16.95) is history only.

## 2. Rate matrix (from 3c578a23's EFS-FULL-RATE-MATRIX, recomputed)
Inputs from [RM]: origin Traverse City 49686; pick/pack $1.60 (1 pair) / $1.95 (2 pairs). "Barre card" = Barreletics FedEx own-account list card; "eFS card" = eFS card rate. Margin = price − eFS cost − pick/pack.
**Caveat:** the card figures exclude residential/fuel surcharges. The live Shopify quotes are far higher than the card (Detroit 2Day live base $27.06 vs card $19.01), and eFS actually invoices 2Day $34.04–35.40 (card + residential + fuel). Treat card-based margins as optimistic; the live-quote rows are the realistic ones.

### 2a. Flat methods (price vs eFS invoiced average, by zone)
| Method | Price | 1 pair cost → margin | 2 pairs cost → margin |
|---|---|---|---|
| Standard GA (paid) | $9.95 | Z2 7.17 → +1.18; Z5 7.92 → +0.43; Z7 8.29 → +0.06 | Z3 8.01 → −0.01; Z4 8.87 → −0.87; Z5 9.45 → **−1.45**; Z6 10.81 → **−2.81**; Z7 11.59 → **−3.59** |
| Standard free ($150+) | $0 | loses ≈ $8.8–9.9 per order | loses ≈ $9.5–13.5 per order (35 discounted 2-pair orders fell under $150 Apr–Oct) |
| USPS Priority | **$19.95** (matrix used 18.95; +$1 added here) | Z5 13.85 → +4.50; Z6 14.34 → +4.01; Z7 16.10 → +2.25; Z8 18.26 → +0.09 | Z5 14.06 → +3.94; Z8 16.73 → +1.27 |
| AK/HI/PR GA | **$19.95** | AK Z8 GA 8.58 → +9.77 (n=101 is the Z8 GA pool, not AK-only). PR via Priority was billed $17.66–18.26 → ≈ +0.1–0.7 | Z8 GA 12.85 → +5.15 |
| FedEx Ground Economy | REMOVED | (was $17.95; margins $3.63–9.19) | — |

### 2b. FedEx 2Day at +75% (was ×2.2)
| Basis | Base | Price ×1.75 | Margin |
|---|---|---|---|
| Barre card, all zones | 19.01 | 33.27 | vs eFS card 23.19: +8.48 (1p) / +8.13 (2p). vs eFS invoices: Z8 1p 34.04 → **−2.37**; Z5 2p 35.40 → **−4.08** |
| Live quote Detroit / LA / Austin / Atlanta (from 120% reads ÷2.2) | 27.06 | 47.35 (observed $47.36 at 75%) | vs invoice ~34–35.40 + pick/pack: ≈ +10.0 to +11.7 |
| Live quote Miami / NY | 30.34 | 53.10 (observed NY $53.10) | ≈ +15.7 to +17.5 |

### 2c. FedEx Standard Overnight at +60% (was ×2.2)
| Basis | Base | Price ×1.6 | Margin |
|---|---|---|---|
| Barre card Z2–5 | 26.92 | 43.07 | vs eFS card 32.16: +9.31 (1p) / +8.96 (2p). vs the single eFS invoice $40.20 (Z2 2p): **+0.92** |
| Barre card Z7 / Z8 | 27.67 / 28.90 (1p); 31.69 / 33.50 (2p) | 44.27 / 46.24; 50.70 / 53.60 | vs eFS card: +10.51 / +12.48; +16.59 / +19.49 |
| Live Detroit / Atlanta | 36.88 | 59.01 | vs $40.20 invoice: ≈ +17.2 |
| Live NY / Austin / Miami / LA | 40.16 / 39.73 / 43.01 / 45.06 | 64.25 / 63.57 / 68.81 / 72.09 | ≈ +22 to +30 (only one Overnight invoice exists; Andrew flagged it as thin) |
At 65% (current profile) the Overnight prices would be $60.85 Detroit … $74.35 LA (≈ +3% over 60%); 2Day would be $44.65 / $50.06 (under the 75% decision).

### 2d. International FICP +50% (card ×1.5, margin vs eFS card, [RM] §3)
Canada A 1p 20.27 → +3.00 / 2p 20.29 → +2.65; UK/DE/FR 1p 22.70 → +3.55 / 2p 22.52 → +3.16; Australia 1p 26.66 → +4.45 / 2p 27.77 → +4.35; Japan 1p 22.47 → +3.49; UAE 1p 24.72 → +4.00; Mexico 1p 18.55 → +2.60. No pick/pack subtracted in [RM]'s intl margin; subtracting $1.60–1.95 leaves ≈ +0.7 to +2.9. Duties billing/per-order fee (eFS FAQ: $10/order on seller account) unanswered, so it could erase this.

## 3. Profile state: New Test Profile 133926158627
| Item | Last verified (proof PNGs 4:13 PM fedex-markup-65, 4:38 PM akhipr-1995) | Should be |
|---|---|---|
| Products | 24 products; locations Barreletics + "Efulfillment Service - 2015" (app); not fulfilling from eFS Center; Old Stock not shown | Same; Old Stock out and online OFF after transfer |
| Domestic 48 + Armed Forces: Standard | $9.95, free at $150+ | Same ✔ |
| USPS Priority | $19.95 | $19.95 ✔ |
| FedEx Ground Economy | **$17.95 still present** | **Removed** ✘ |
| FedEx (own account) | 2Day + Standard Overnight, **65%** handling, one option | **2Day +75%, Overnight +60%** ✘ (see §4) |
| FedEx Home | not offered | not offered ✔ |
| AK/HI/PR (10 states) | Standard $19.95 | $19.95 ✔ |
| International (59 countries) | FedEx own account, FICP only, 50% | Same ✔ |
| Draft D655 | left on 100 Broadway, New York 10005, no shipping line | reset before more drafts |
Not verified since: anything after 4:38 PM. Eric has not acknowledged the Oct 13 rate changes (EX).

## 4. Known Shopify constraint: two FedEx own-account markups in one zone
**Evidence:** at ~2:04 PM the bot tried to add a second "FedEx (own account)" calculated option to the domestic zone; Shopify disabled FedEx (own account) in the carrier dropdown. Conclusion recorded: one handling fee per carrier option per zone (TR(T2); proof fedex-markup-new.png). The bot repeated this to Andrew at 4:26 PM (T5). This is one observed UI behaviour; no Shopify doc or support confirmation is in the files.
**Options in the evidence** (bot-offered; no decision by Andrew recorded):
- A. Flat Overnight rate (bot example $59.95) + FedEx own-account 2Day at 75%. Note: a flat rate is not a FedEx quote; at 60% live Overnight ranges $59.01 (Detroit) to $72.09 (LA), so $59.95 would under-charge far zones vs the 60% rule.
- B. One shared markup (the 65% that's live now). Contradicts Andrew's 75/60, so not acceptable as-is.
**Not in evidence / untested:**
- A second zone with the same states: never tried. Shopify generally lets a country/state sit in only one zone per profile, so this probably won't work. Verify before relying on it.
- Splitting zones by states (e.g. two zones each carrying a different FedEx markup) wouldn't give both services to the same customer.
- A third-party rate app or a separate carrier calculation path: not researched in any file.
**Gap:** the transcript pages ~1:40–1:57 PM and 4:08–4:20 PM were never read, so when Overnight went back at 65% isn't documented.

## 5. Test plan (in order)
**Done (drafts only; nothing paid or placed):** D655 test item M/Dusty Rose. Detroit at 120% (Standard 9.95, GE 17.95, Priority 18.95, 2Day 59.53, ON 81.14); five states at 120% (Miami 66.75/94.62, LA 59.53/99.13, NY 66.75/88.35, Austin 59.53/87.41, Atlanta 59.53/81.14); flats exact. Partial reads at 75%: Detroit 2Day 47.36, NY 53.10. Overnight wasn't offered at that moment. Analyses: invoices, free-shipping, PR.
**Next:**
0. Andrew decides how to get 75/60 (§4), then the profile is fixed (Overnight markup, GE removed). Each change needs Andrew's go.
1. Reset D655 address; re-run domestic drafts at the final settings: Detroit, Miami, Austin, LA, Seattle, NY; $149 vs $151 free-ship; multi-pair 2/3/6/10; AK, HI, PR at $19.95; wholesale code 0-HWholesale. Draft orders may not show calculated FedEx rates (Eric checking).
2. Domestic website checkouts: show test item at $100, place orders (tag TEST ORDER; cancel/refund/restock), check fulfilment routing (app location first, Barreletics second), then hide. Payment method (gift card) not identified: OPEN.
3. Phase two international: MM off in a short live window with Eric on the phone, test item visible, one order per region, check FICP ×1.5, hide the item, MM back on. Waiting on Eric's reply to G3.
4. Flow tests after Eric's rework (Eric on call, mapping off).
5. Profitability review vs invoices (Layer 4); validate Overnight and +50% intl on first real invoices.
6. Go-live (Layer 5): stock transfer → location cleanup → weights 1 lb → SKU mapping on → products to profile → flows on → 5510 off → all-region tests → 48 h monitoring.
**Open for Eric (only if Andrew wants):** who shuts off 5510; tracking push-back (trackingSupport=false); whether the app needs routing; intl duty billing + per-order fee; empty-box weight; AK/HI calculated USPS option; phone window right after go-live.

## 6. Do-not-do
- Don't ask Eric about April OOS (MM; settled), DDP, Saturday shipping, or anything in §1 🔒.
- Don't use 65%, 120%, $18.95, $22.95, or GE $17.95 anywhere as current.
- Don't take Overnight off. No Ground Economy, SmartPost, or FedEx Home; don't put GE in the Ground Advantage line.
- Don't change store/profile settings, publish the test item, or toggle MM without Andrew's go; never show the test item outside a test window.
- Don't recommend MM or the $99 Duty & Tax app.
- Don't send email as Andrew (draft-first); don't message bots from this task.
- Don't add custom order-routing rules; ask before moving any order to eFS.
- Don't uninstall the eFS app without re-approval. Leave OD-* SKUs and the 13 Global-e no-rate regions alone.
- Don't turn on flows or SKU mapping before cutover. Discard the old EFS Go-Live bot draft cards.


## UPDATE 2026-10-13 ~6:55 PM ET: Overnight locked at 50% (replaces 60%)
- 2Day stays at **+75%**. Overnight is now **+50%** on the live FedEx quote. Documentation only: the store is unchanged (still 65% on both) until Andrew gives the go.
- **Reasoning (Andrew):** at 50%, profit is at least about $13 per order on live calculator quotes, measured against eFS cost (the $40.20 invoice + $1.95 pick/pack, about $42.15 near and an estimated $44.50 far):
  - Detroit/Atlanta: quote $36.88, price $55.32, about +$13.17
  - New York: quote $40.16, price $60.24, about +$15.74
  - Austin: quote $39.73, price $59.59, about +$15.09
  - Miami: quote $43.01, price $64.52, about +$20.02
  - LA: quote $45.06, price $67.59, about +$23.09
- That's at or above the top of typical 3PL carrier markups (5–30%: Speed Commerce, Simple Distribution, GoBolt). The real margin over eFS cost is about 30–50%, because Shopify marks up the discounted FedEx quote.
- **Benchmark gap:** the 90-day sample (Jun 16–Sep 16, 704 shipments) has one Overnight order, #5239 (16 pairs, $105.96, later refunded). #5743 ($104.14) hasn't been verified. 50% is a judgment call based on the draft math, not on observed customer prices.
- **Flag:** far-zone eFS costs are estimates from one invoice. Check them against the first real Overnight bills.
- **Follow-up:** Eric's email says Overnight +60%, so tell him it's now 50% when the profile is changed.
