# TEST ORDER tagging, 2026-10-23

Method: Admin API 2025-10 (client_credentials), only the additive `tagsAdd` mutation. No other order changes, no tags removed.
Each order was re-pulled by name/id before writing and checked: gateway is gift_card only, and cancelled (or #5995 non-cancelled gift card).

## Result
- Orders in scope: 47 (46 cancelled + #5995)
- **Tagged "TEST ORDER": 21** (0 mutation failures)
- Skipped, already had exact tag "TEST ORDER": 26
- Skipped because not paid by gift card: 0 (nothing for Andrew to review)

## Tagged (21)
Cancelled, BEFORE window (7): #5845, #5846, #5847, #5848, #5849, #5850, #5851
Cancelled, AFTER window (13): #5924, #5941, #5942, #5943, #5944, #5948, #5949, #5950, #5951, #5952, #5953, #5954, #5955
Non-cancelled gift card test (1): #5995 (previously had tag "TEST" only; that tag kept)

## Skipped, already tagged (26)
#5844, #5855, #5867, #5868, #5869, #5870, #5880-#5891 (12), #5895, #5930, #5931, #5932, #5933, #5936, #5937, #5938

## Verification
Re-pulled all 21 touched orders after writing: "TEST ORDER" present on all 21; tags equal previous tags plus "TEST ORDER" (nothing removed); cancelledAt, cancel reason, financial status, fulfillment status, gateways, totals, refunded amount, line item quantities, fulfillments, and hashes of note/contact/address/customer all unchanged. The 26 skipped orders were also re-checked: tags unchanged. Result: PASS, 0 discrepancies.

Notes: A first run's built-in verification step crashed on a bug in my script (after all 21 mutations had succeeded); I then ran verification separately against the pre-write snapshot, which is the result above. Cancelled orders outside the two windows (e.g. #6015-#6025 Oct 22 "Grok test", #5491, #4770, #4671) were not touched.
