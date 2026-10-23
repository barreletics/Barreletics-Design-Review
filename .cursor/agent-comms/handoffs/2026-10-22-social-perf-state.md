# Social Perf current state, 2026-10-22 ~8:15 PM ET

Intended repo location (save later; not pushed): `barreletics/alternate-projects` → `docs/bots/weekly-social/STATE-2026-10-22.md`

## Ground rules

- **Meta is LOOK-ONLY** (Andrew, Oct 19; no-touch protocol Oct 20).
- Judge every ad on **Shopify last-touch**. Platform numbers are claims.
- Andrew, Oct 21: **"no strategy until data is verified."**

## Plan status

- **Oct 19 4-step plan** is still awaiting Andrew's yes. Its status conflicts with the Oct 21 position, and the **Oct 21 position is current**.
  - Phase 0: investigate purchase gap / scopes / UTMs.
  - Phase 1: retargeting test, $30/day for 14 days, pass at 2.0x.
  - Phase 2: relaunch Yellow Shoes + GRIP.
  - Phase 3: Advantage+ at $50/day for 14 days, pass at 1.5x.
  - Scale +20% every 3-4 days while 7-day Shopify ROAS >= 1.5.
- **Proposal pending Zaki:** pause 3 lagging ads and scale UYG ~20% (~$50/day mirror test).

## Routines

Recreated 2026-10-22 on bot `e20dc32e`, replacing `f7a36d04`.

| ID | Routine | Schedule |
|---|---|---|
| A | Daily Pinterest spend from Blend | 6:17 AM ET daily, flexible ±15 |
| B | Grok Restore Winner budget review | Exact Oct 24 and Oct 31, 9 AM ET |
| C | Oct 30 budget check-in email | Exact Oct 30, 9 AM ET; **draft card only** |

Note: the env var is `SHOPIFY_GROK_ADMIN_CLIENT_SECRET` (the routines say CLIENT_ID/SECRET).

## Sales

Shopify pull at 8:00 PM ET Oct 22; excludes cancelled, test and $0 orders.

- Oct 16-22: **54 orders, $5,294.30** vs Oct 9-15: 45 orders, $4,728.63 (**+12%**). Oct 22 is partial.
- Dashboard 30d (Sep 23-Oct 22): **175 orders, $17,877**, down 28% vs prior 30d (222 orders, $24,718).
- Last-touch, Oct 16-22:

| Channel | Orders | Revenue |
|---|---|---|
| Meta paid | 19 | $1,944.30 |
| PMax | 12 | $1,137.80 |
| Pinterest | 1 | $83.95 |

## Pinterest

- **Grok Restore Winner** (`626760082398`): ACTIVE, $25/day.
- Pinterest-claimed, Oct 17-22 (Oct 22 partial): spend $126.88, 98 clicks, 2 checkouts, $148 (claim, ~1.17x).
- Shopify, Oct 17-21: spend $100.37, 1 order, $83.95 (**0.84x**).
- Plan:
  - **Oct 24:** report only.
  - **Oct 30:** draft email, **never send**.
  - **Oct 31:** raise to $31 only if both weekly windows are ~2.0x or better.
- Other campaigns are paused, including "(KEEP OFF) Winners Oct 2026" (`626760011313`).
- PMax is on hold; review ~Oct 26.

## Meta

Blend account `bps-2c81`. Shopify last-touch. Window A = Oct 15-22; Window B = Sep 23-Oct 22.

### Totals

| Window | Spend | Orders | Revenue | Shopify ROAS | Meta claims |
|---|---|---|---|---|---|
| A | $1,788 | 21 | $1,968 | 1.10x | 1.94x |
| B | $7,262 | 65 | $6,476 | 0.89x | 1.50x |

The dashboard says 62 orders / $6,264 / 0.86x for B. The gap is unexplained.

### Campaigns

| Campaign | Status | A | B | Action |
|---|---|---|---|---|
| Prospecting CBO ($150/day) | Active | $1,200, 0.75x | $3,598, 0.81x | Hold |
| Creative Test (ad set Broad Men+Women 18-65+, $90/day, avg ~$73/day) | Active | $588, 1.81x | $3,381, 0.98x | Leave alone |
| International Sales Sep 2026 | Paused | n/a | $283, 0.95x | n/a |
| Retargeting US July | Paused | n/a | n/a | Phase 1 test not launched |

### Ads

| Ad | Status | Data | Note |
|---|---|---|---|
| HTG Prospecting Sep (CBO) | Active | A $748 0.90x; B $1,902 1.07x | Hold |
| UYG Prospecting Oct 2026 (new, created Oct 22 12:38 AM) | Active | $97 spend, 0 orders | Recheck Oct 23 |
| UYG Feb 2026 (Creative Test) | Active | A $588 1.81x; B $830 1.49x | Only ad above 1.5x. **Don't touch UYG.** Oct 21-22 had 0 orders. |
| HTG Yellow Footwear | Paused Oct 22 12:28 AM | $197, 1 order, $226 | n/a |
| DYYS Prospecting | Paused Oct 21 12:56 AM | $157, 0 orders | n/a |
| HTG Sep (Creative Test) | Paused | B $1,478, 0.87x | n/a |
| Video #01 Corrected | Paused | B $1,086, 0.59x | n/a |
| Closed Sole | Paused | B $473, 0.71x | n/a |
| Sock Era Is Over | Paused | B $246, 1.82x on 4 orders; CBO copy $158, 0 orders | n/a |

### Unexplained changes

- Overnight edits Oct 21-22 were **not made by Social Perf**. The editor and the changes are unknown (the API shows only `updated_time`).
- The Oct 11 CBO edit and the Oct 21 Creative Test ad set edit are unexplained.

## Open items

- **Oct 23:** recheck Meta purchases by ad / ad set.
- Do **NOT** assume shifting back to HTG Sep is right (0.87x on Shopify 30d). Andrew decides.
- Andrew asks Zaki about the overnight changes.
- Zaki WhatsApp reply pending (Andrew sends).
- Zaki email draft card `t29s1` still mentions Yellow Shoes. Update it to Andrew's own creative.
- Andrew's new creative is pending.
- PayPal is off (Website bot / Andrew).
- Fake-order protection task: unanswered whether to resend to Website bot `f1b1afce`.
- Managed Markets stays ON.

## Caveats

- Dashboard `campaign_status`, `agency_activity`, `challenges` and `actions` blocks are stale (August). The "$100/day cap" is wrong; the real CBO is $150.
- Last-touch UTM undercounts: only 65 of ~175 paid orders carry Meta UTMs.
- Ad-level order counts are small (1-14), so treat them as directional only.
- The handoff's "0 purchases Oct 22" is outdated (order #6017, ig paid_social, 3:54 PM ET).
