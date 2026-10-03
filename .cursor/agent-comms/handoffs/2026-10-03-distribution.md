# Handoff: Distribution bot (2026-10-03)

## Role
Barreletics international + domestic distribution: price ladder, deal and contract terms, partner selection.
This bot owns the **demand lane**. Supply/production belongs to the **Manufacturing Forecast bot (98680125)**; coordinate volumes with it.

## Where the work lives
Repo `barreletics/barreletics-ops`, **PR #8** (open, not merged), branch `distribution/framework-2026-10-03`.
https://github.com/barreletics/barreletics-ops/pull/8
- `distribution/FRAMEWORK.md`: Spain-first framework, BUSTO fit, Year 1 terms, source contradictions.
- `distribution/PLAYBOOK.md`: "how we work" for US/EU/GCC. Covers price ladders, channel margin, terms, intake checklist, duties table, freight, pricing policy and scenarios.
- `distribution/cogs.md`: per-pair COGS and landed cost (3PL excluded).
- `distribution/spain-distributor-shortlist.md`: ranked Spanish partners.
- `distribution/sources/`: Claude and ChatGPT summaries (2026-10-03).

## Key facts
- **Landed cost ~$9.30/pair** (base $8.83–9.86). **Worst case $12.46** until Brandon (PDS) confirms the TPE yield (1,200–1,400 pairs per 1,000 lb conflicts with the 0.444 lb/pair base).
- **Payment: 100% prepayment on all partner orders, no net terms** (decided). **Shipping: EXW/FCA** from the US 3PL; the partner is importer of record; no DDP by default.
- **Studio/retailer margin 50% is the BASE** (US studios get 50% off retail); 45% is the alternate.
- US: retail $74. Wholesale reference $36 (Free People INV-0075/0080/0081). Barreletics margin on landed: $29 = 67.9%, $25 = 62.8%, $22 = 57.7%.
- Positioning, use verbatim: "Patented Performance Skins for barre, Pilates, reformer, Megaformer, and studio fitness. Built because grip socks kept failing when grip mattered most." / "We didn't improve the grip sock. We made it obsolete."
- **Avoid distributors that carry grip socks.** Ingesba carries ToeSox/Tavi in Spain: excluded.
- **BUSTO** (Exclusivas Busto SA, San Sebastián, beauty/salon distribution; contact Patrizia): **regional / non-exclusive only**, performance-gated.
- Spain alternatives: Pilates Iberia, Aerobic & Fitness, Albion 1879, Comercial Udra (details in the shortlist).
- **Duties:**
  - Likely HS code 6402.99; get binding rulings (EU BTI and US CBP).
  - EU duty 0% if US origin and direct transport are proven under Reg. 2026/1455, otherwise 16.8%.
  - GCC 5%. UK 16%. Canada and Australia 0% if the product qualifies as US-made under their trade agreements.
- **Freight (ASSUMPTION), 500 pairs:** air $2.00–3.40/pair, sea LCL $0.80–1.60/pair.
- **Reverse pricing**, Spain shelf incl. 21% VAT, studio 50%, sea $1.20/pair, 0% duty → max distributor price:
  - €65: $18.50–20.00
  - €70: $20.20–21.80
  - €75: $21.80–23.50 (Barreletics margin 57–60%)
  - About $3.50 lower if duty is 16.8%.
- **DTC comparison:** $74 = €65.92 (ECB, 2 Oct). Plus VAT and duty that's **≈ €83.40 before shipping**. Sep median single-pair Global-e order: $119 ≈ €106 all-in.
- **Correction:** the EU €150 duty exemption ended 1 Jul 2026. A **€3/item flat duty** applies until 1 Jul 2028.
- DTC 3PL (eFulfillment), Jul–Aug: $8.36/order across all orders, ~$13.42 per 3PL-shipped order. The 3PL handled 62% of Sep orders.

## Open decisions (Andrew)
1. Distributor price per market: **$29 / $25 / $22**. Andrew leans toward a **€70–75 Spain shelf**, which implies about $20–23.50.
2. GCC shelf prices: about $89 UAE, $95 KSA at $29. Lower if the price drops.
3. US price list ($37 studios / $36 for 500+ retail) and whether to use sales reps (10–15%).
4. Exclusivity model: channel-limited, performance-gated, Year 1 minimum about 1,500 pairs.
5. **Intro emails to shortlist: not drafted, not approved; offer to draft when Andrew asks.**
6. **Origin letter from PDS** (for EU 0% duty): offered, no answer yet.
7. **Distribution/Ops sidebar section:** requested from Grok Bot, not confirmed.
8. Approve the $27/$25 volume-tier thresholds (2,500 / 7,500 pairs per year).

## Rules
- Never invent numbers; label ASSUMPTION.
- Push to the PR #8 branch; don't merge.
- No external sends without Andrew's explicit approval.
