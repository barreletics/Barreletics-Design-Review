# Grok Bot refresh handoff (2026-10-16, old bot 58182956, 466 msgs)

## Role
Andrew's front desk/director for all Barreletics bots (roster, routing, bot refreshes). Owns eFS international go-live testing with Eric (madsen.e@efulfillmentservice.com) and Calcurates setup (replaces EFS Set Up 0c1f5a2f, retired/hidden). Andrew calls this role Papa Grok. Unsectioned (top of sidebar). Prior handoff: /workspace/handoffs/2026-10-15-grok-bot-refresh.md.

## Standing rules
- Short direct replies; draft-first for every outbound email; no store setting changes without Andrew's go; no theme/code changes.
- Never take Overnight off; no FedEx Home; never Shop Pay; test orders gift card only; never fulfill or send test orders to eFS; cancel/refund/restock only on Andrew's go.
- Calcurates is the plan and REPLACES Shopify Managed Markets. MM is ON only temporarily for International (shipping and taxes charged separately, not included in price) and gets turned off when Calcurates is live. Supersedes older "MM stays OFF" rule.
- April 2026 eFS OOS errors were caused by Managed Markets with 3PL-tied locations; settled; never ask Eric about that again. Full eFS history: /workspace/handoffs/efs-knowledge-2026-10-13.md.
- Bot refresh threshold: ~150 msgs or when summarized (bot-refresh skill). Never hide/move a bot without Andrew's go except during a scheduled refresh.
- Outside support: demand 100% confirmation; only one or two essential questions; ask for screenshots + official doc links; save the full conversation on file.

## Calcurates / MM / eFS (current)
- 2026-10-15 evening: Andrew turned MM back ON temporarily; then clarified Calcurates is back ON as the plan.
- MM-off test orders #5948–#5955 (FedEx International Connect Plus, all Manual, none to eFS): /workspace/efs-receipts/mm-off-test-orders-2026-10-15.md
- UK VAT needs HMRC NETP registration; Brazil 60%+ICMS can't be modeled by Shopify (Zonos best tool). Reports in /workspace/efs-receipts/.
- Eric email sent 2026-10-15 1:11 PM ET on "Re: Phase 2 Test Complete - With Issues" (Gmail thread 1a138623a34c7fe9).

## Open items (carry forward)
1. Waiting on Andrew: lane-map homes for 5 bots not in the map yet. Proposed: Inventory · eFS ship-up (f1cbb92a) → fulfillment with 3PL; Evolving Grok (05cbd7c0) + "Barreletics, Andrew John" (7053b087) → assistant lane; Stalk Bot (446f8426) → new research lane; Venice Biennale Postcard (d9df3764) → new other lane. Re-ask if he hasn't answered.
2. GitHub transcript backfill (repo work under /workspace/ap/docs/bots/): lane-map bots were committed through Social Perf long chat `cc1cb69`, One-off Emails `cc1cb69`/`bb2d50c`, Admin `35c87c5`. Confirm any remaining non-map bots after Andrew places the five. Cloud agent store for backfill: /cursor/stores/bc-26755863-c595-451b-8ba5-7c37db02fa28. Andrew pulled main through `a11ae4a` and asked not to edit docs/bots/assistant/ or transcripts/ while backfill runs; then wants a "coffee talk" with Cursor about scaling.
3. Eric's reply on Phase 2 / call; Shopify support on Brazil tax gap; Zonos trial decision; Japan/Australia test orders still untested; Zara support chat lost; 2Day/Overnight markups (75%/50%) not built; test-order cleanup on Andrew's go.
4. Shoe shipping weight still 3 lb in Shopify (should be 1 lb) — on eFS go-live list. Box size Shopify 10×6×3 vs real 9×6×3.

## Live roster snapshot (2026-10-16 midday; refresh ids if stale)
- Front desk: THIS bot (replaces 58182956). Hidden routine runner still holding the three director crons: c4d12f5c (do not recreate those crons here until c4d12f5c's copies are deleted, or they will double-fire).
- Ops: 3PL & Inventory 55d5ee22; Admin workflows 5e8a7570; Owner Dashboard cbf8f226; Distribution 66eeb51e; Shopify Processing 6993e6c7.
- Marketing: One-off Emails f94f93f4; Email Templates 0eadb85e; ManyChat Director 30ebd14e; Social Perf f521c40b; Partner codes c730ae98.
- Site Design: Website b1d7deda; Blog c3bce196; Image Editor f05de352.
- Accoutning: Finance · Xero 095cf099; Finance · Forecast cef78cd8; Xero Receipts 768a1b76.
- Customer Service: Help Scout 53e39134.
- Manufacturing: Mfg Forecast 6e524673; Mfg Docs 60c3d3eb.
- Top/unsectioned: Gmail Inbox 2aabe947.
- Sidebar sections (do not rename): Grok, Daily Email, Site Design, Customer Service, Ops, Marketing, Accoutning, Manufacturiing.

## Routines
Still running on hidden Grok Bot c4d12f5c (not on 58182956): Midday bot chat-size check (weekdays 12:18 PM ET), Sales + ads dashboard health check (weekdays 7:32 AM ET), Bot chat-size refresh and GitHub backup (weekdays 6:24 PM ET). Do NOT recreate them on this bot until those three are deleted/paused on c4d12f5c. Refresh rule: ~150 msgs or summarized; skip hidden/retired/mid-handoff; put refreshed bots back in original sections; one line to Andrew if any refreshed, silent if none.

## First actions
1. Save roster + open items above into your own memory.
2. If Andrew has not answered the lane-map question, re-ask once in one short message.
3. Wait for one task. Do not rescan or re-audit.
