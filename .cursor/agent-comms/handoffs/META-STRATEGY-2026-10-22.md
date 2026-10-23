# Barreletics Paid Meta Strategy (Social Perf bot, for Andrew John)

- **Status:** PROPOSAL, pending Andrew's approval and Zaki's input. Nothing here is live, scheduled, or approved.
- **Andrew's Oct 21 position:** "no strategy until data is verified." This document is a draft to react to. It does not override that position.
- **Data pulled:** Oct 22, ~8:15 PM ET (Shopify pull 8:00 PM ET; excludes cancelled, test and $0 orders; Oct 22 is partial).
- **Windows:** A = Oct 15-22. B = Sep 23-Oct 22.
- **Ground rules:**
  - Meta is **LOOK-ONLY**. Every action below is a **recommendation** that Andrew must approve. Nothing is automatic.
  - Judge everything on **Shopify last-touch**. Platform (Meta/Pinterest) numbers are claims.
- **Account baseline (Blend `bps-2c81`, Shopify last-touch):**

| Window | Spend | Orders | Revenue | Shopify ROAS | Meta claims |
|---|---|---|---|---|---|
| A (Oct 15-22) | $1,788 | 21 | $1,968 | 1.10x | 1.94x |
| B (Sep 23-Oct 22) | $7,262 | 65 | $6,476 | 0.89x | 1.50x |

"Return" below means Shopify last-touch ROAS (revenue / spend).

---

## 1. Performance thresholds: scale-up and pause triggers

**Andrew's proposed rule (as given):**
- **Scale-up trigger:** any Meta ad set above **1.5x** return over **5 days**.
- **Pause trigger:** anything under **0.8x** for **3 straight days**.
- Between 0.8x and 1.5x is the hold zone.

**Applied to real numbers.** The data pulled so far is window totals (8 and 30 days), not 5-day or daily series. So each line below is a read against the rule, not a trigger. A true 5-day and 3-straight-day check needs the daily Shopify last-touch split, which is the Oct 23 recheck.

| Item | Spend / window | Shopify return | Read against rule |
|---|---|---|---|
| **UYG Feb 2026** (ad in Creative Test) | $588 (A); $830 (B) | 1.81x (A); 1.49x (B) | Clears 1.5x on window A, so it is a scale candidate. B is 1.49x, just under 1.5x. **0 orders Oct 21-22** is 2 days, so the 3-day pause trigger is not hit, but day 3 (Oct 23) matters. Current state says "don't touch UYG." Recommendation only. |
| **Prospecting CBO** ($150/day) | $1,200 (A); $3,598 (B) | 0.75x (A); 0.81x (B) | A is under 0.8x. B is just above. If daily data shows 3 straight days under 0.8x, this would hit the pause trigger. Current state says Hold. Flag for Andrew (see Open questions). |
| **Hear The Grip Prospecting Sep** (CBO) | $748 (A); $1,902 (B) | 0.90x (A); 1.07x (B) | Hold zone (0.8x-1.5x). No trigger. |
| **UYG Prospecting Oct 2026** (new, created Oct 22 12:38 AM) | $97 | 0 orders | Too early. It is on day 1 and is covered by the new-ad-set rule in section 2. Recheck Oct 23. |
| **Paused: Hear The Grip Sep (Creative Test)** | $1,478 (B) | 0.87x | Hold zone on the rule, not under 0.8x. Pausing was a judgment call. Do not assume shifting back to it is right. Andrew decides. |
| **Paused: Video #01 Corrected** | $1,086 (B) | 0.59x | Well under 0.8x. Consistent with a pause. |
| **Paused: Closed Sole** | $473 (B) | 0.71x | Under 0.8x. Consistent with a pause. |

**Proposed clarifications to the rule (for Andrew to confirm):**
- The rule is written for ad sets. Several of the data points above are ads inside an ad set (e.g. UYG Feb 2026 sits inside the Creative Test ad set, which is $588 / 1.81x in A and $3,381 / 0.98x in B). Confirm whether the rule applies at ad set level, ad level, or both.
- Small ad-level order counts (1-14) mean a threshold hit is directional. Consider a minimum-orders or minimum-spend guard before any action.

---

## 2. Budget actions: what happens at each threshold

**Recommendation ladder (all need Andrew's approval):**

| Situation | Proposed action | Dollar example |
|---|---|---|
| Above 1.5x over 5 days | **Bump** | Existing scale rule: +20% every 3-4 days while 7-day Shopify ROAS >= 1.5. On the Creative Test ad set ($90/day), +20% is $108/day. On Prospecting CBO ($150/day), +20% is $180/day. These are illustrations, not proposals to act. |
| 0.8x-1.5x | **Hold** | Leave the budget as is. Example: HTG Prospecting Sep stays as is (0.90x A / 1.07x B). |
| Under 0.8x for 3 straight days | **Cut or pause** | Example (if daily data confirms): Prospecting CBO at $150/day would be a pause or cut candidate (0.75x on $1,200 in A). Freed budget moves to what's working, not to a paused ad. |

**Brand-new ad set launch rule (Andrew's example, stated as written):**
- A brand-new ad set launches at **$25-30/day**, not $15. $15 is too small a sample for Meta's auction at Barreletics price points.
- It runs a **5-day window**.
- Clearing 1:1 by day 5 "steps it to $25." Still under 1:1 kills it, and the budget moves to what's working.
- **Ambiguity, flagged for Andrew to clarify, not silently fixed:** "steps it to $25" conflicts with launching at $25-30. If it launches at $25-30, "stepping to $25" could be flat or a decrease. Possible intent: step up to $25 from a lower launch figure, step up to $35 or more, or "$25" is a typo. Needs Andrew's answer before this rule is used.

**Example: UYG Prospecting Oct 2026** (new, created Oct 22 12:38 AM). So far $97 spend and 0 orders, on day 1. Under this rule its 5-day window would end around Oct 27. Day-5 call: if at 1:1 or better on Shopify last-touch, apply the step rule. Otherwise kill it and move the budget to what's working. No action before then. The Oct 23 recheck is look-only.

**Existing Pinterest campaign mapped into this framework (NOT Meta):**
- **"Grok Restore Winner"** is a **Pinterest** campaign (`626760082398`), $25/day, ACTIVE. It is not part of Meta, and this plan does not change it. Its existing routine stays as is.
- **Existing rule:**
  - **Oct 24:** report only.
  - **Oct 31:** raise to **$31** only if both weekly windows are ~2.0x or better and the campaign is still $25/ACTIVE.
- **Current numbers:**
  - Pinterest-claimed Oct 17-22 (Oct 22 partial): spend $126.88, 2 checkouts, $148 (claims, ~1.17x).
  - Shopify last-touch Oct 17-21: spend $100.37, 1 order, $83.95 = **0.84x**.
- **Mapped read:** 0.84x on Shopify sits in the hold zone, just above the 0.8x pause line and nowhere near the 1.5x scale-up trigger. Under the existing rule the Oct 31 raise would not fire on these numbers. Order counts are tiny (1 order), so this is directional only.

---

## 3. Testing rules

**Proposed rule (Andrew's direction):** a new creative or audience starts at **$20/day** and earns scale only after hitting the threshold (Section 1, over 1.5x).

**Overlap with Section 2 and proposed reconciliation (for Andrew to confirm):**
- Section 2: a brand-new ad set launches at $25-30/day.
- Section 3: a new creative or audience starts at $20/day.
- **Proposed reconciliation:**
  - **$20/day** for a new creative or audience inside an **existing** campaign or ad set.
  - **$25-30/day** for a **brand-new ad set**.
  - Same pass test either way: Shopify last-touch at or above 1:1 by day 5 keeps it. At or above 1.5x earns a bump.
- **Example:** Andrew's own new creative (pending) would go in as a $20/day test inside an existing campaign. A new ad set built around it would start at $25-30/day.

**Strategy direction under discussion with Zaki (exploring, not decided):**
- Take viral creatives into **template families** (same hook and format, new angles).
- Use winners as the **creative spine of every campaign**.
- Run a rapid loop of **five variants a week**.
- **Kill losers in 48 hours.**
- **Scale what clears the threshold.**
- Note: a 48-hour kill conflicts with the 5-day window in Section 2 and the 3-straight-day pause in Section 1. Reconcile only if Andrew and Zaki adopt this.

**Phase 1 retargeting test (from the Oct 19 plan):** $30/day for 14 days, pass at 2.0x. It is **not launched** and still **pending Andrew's approval** (the Retargeting US July campaign is paused). The Oct 19 plan's other phases are also awaiting Andrew's yes, and its status conflicts with the Oct 21 position. The Oct 21 position is current.

**Also pending with Zaki:** the proposal to pause 3 lagging ads and scale UYG ~20% (~$50/day mirror test).

---

## 4. Review cadence

- **Oct 24 and Oct 31:** Meta review check-ins, per Andrew. He says they are already on the calendar.
  - The only saved routines on those dates are the **Pinterest** "Grok Restore Winner" budget reviews at 9 AM ET (routine B). There is **no verified Meta-specific routine**.
  - Suggestion: confirm whether a Meta routine should be added for Oct 24 and Oct 31. If so, it would be look-only, report-only.
- **Oct 23:** recheck of Meta purchases by ad and ad set (including UYG Prospecting Oct 2026, UYG Feb 2026 for day 3 after the 0-order days Oct 21-22, and the daily split for Prospecting CBO).
- **Daily:** look-only checks of Shopify last-touch by ad and ad set. They report only and take no action.
- **Other existing routines (not Meta):** Daily Pinterest spend from Blend (6:17 AM ET). Oct 30 budget check-in email (draft card only, never sent). PMax is on hold, reviewed ~Oct 26.

---

## Open questions for Andrew

1. **"Steps it to $25" vs launching at $25-30:** what is the intended post-day-5 budget for a new ad set that clears 1:1?
2. **Rule scope:** do the thresholds apply at ad set level, ad level, or both? Should there be a minimum spend or minimum orders before a trigger counts?
3. **Prospecting CBO** ($150/day, 0.75x A / 0.81x B): current state is Hold. Under the proposed pause rule it may qualify for a pause or cut if daily data shows 3 straight days under 0.8x. Hold, or apply the rule?
4. **UYG Feb 2026** (1.81x A, 1.49x B, 0 orders Oct 21-22): current instruction is "don't touch." Does the proposed 1.5x scale rule override that?
5. **Test budget reconciliation:** confirm $20/day (new creative or audience in an existing campaign) vs $25-30/day (new ad set).
6. **Overnight Oct 21-22 edits:** the editor and the changes are unknown. Social Perf did not make them, and the API only shows `updated_time`. Also unexplained: the Oct 11 CBO edit and the Oct 21 Creative Test ad set edit. Andrew was going to ask Zaki.
7. **65 vs 62 orders gap:** window B shows 65 orders / $6,476 / 0.89x in the Shopify last-touch pull, but the dashboard says 62 / $6,264 / 0.86x. The gap is unexplained.
8. **Meta routine:** should a Meta-specific routine be added for Oct 24 and Oct 31?
9. **Phase 1 retargeting test** ($30/day, 14 days, 2.0x): approve, defer, or drop.

## Sources and caveats

- Source: `/workspace/handoffs/2026-10-22-social-perf-state.md` (Blend `bps-2c81`, Shopify last-touch, pulled Oct 22 ~8:15 PM ET). No numbers here were added beyond that file and the figures Andrew provided. Dollar amounts for bumps (+20%) are simple arithmetic on stated budgets.
- Ad-level order counts are small (1-14), so treat them as directional only. Pinterest's Shopify read is a single order.
- Last-touch UTM undercounts: only 65 of ~175 paid orders carry Meta UTMs.
- Dashboard `campaign_status`, `agency_activity`, `challenges` and `actions` blocks are stale (August). The "$100/day cap" is wrong: the real CBO budget is $150/day.
- Oct 22 is a partial day. The handoff's "0 purchases Oct 22" is outdated (order #6017, ig paid_social, 3:54 PM ET).
- Nothing was pushed, changed live, or sent. Meta stays look-only.
