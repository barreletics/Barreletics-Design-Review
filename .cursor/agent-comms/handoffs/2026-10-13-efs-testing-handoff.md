# eFS Testing Handoff (2026-10-13)
Sources: /workspace/fulfillment-handoffs/EFS-MASTER-KNOWLEDGE.md, EFS-FULL-RATE-MATRIX.xlsx/.md, /workspace/efs-golive-check/REVIEW-2026-10-13.md, ERIC-EMAIL-DRAFT.md, the Eric meeting doc 12hk-LkVTolgfLR0zuafizlQBYy1ePHRukYI_ffjAZk4, and the raw ee353fac transcript /workspace/ee353fac/ (positions 0-982). Gmail thread 1a1354c38479a59a.
Settled: Standard $9.95 (free at $150+), Priority $18.95, Ground Economy $17.95, 2Day +120%, Overnight +120%, AK/HI/PR $18.95, international Connect +50%, 1 lb per pair.
Test order: (1) full system test, (2) 10-12 draft orders, (3) Eric's test product live in the new profile, (4) compare with Shopify billing history. Nothing live and no email to Eric without Andrew's go.

## Flow screenshots (Andrew, 10/13 8:57 AM): /workspace/efs-golive-check/flow-screens/
- 30-min flow: no weekend check. If updated before the cutoff, wait 30 minutes and submit. Otherwise, if created between 12:30 and 1:00, submit immediately; else wait 30 minutes and submit. So weekend orders still go out at 30 minutes, and the 2-hour weekend flow only adds a second, later submit request. Risk: the weekend hold is ineffective, plus a possible duplicate request.
- Wholesale flow (still Draft): the condition is "starts with 0-Wholesale", but the code is 0-HWholesale, so there's no match. The move step looks wired to the False branch; unconfirmed.
- Race: orders paid 12:30–1:00 are submitted immediately, so a wholesale order could reach eFS before it gets moved.
All three flows are OFF.
