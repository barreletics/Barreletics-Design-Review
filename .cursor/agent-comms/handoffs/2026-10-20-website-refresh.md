# Website refresh, 2026-10-20 (replacing bot 25c9f763-68b9-4775-997c-f9c061016224)

Self-contained handoff. Repo barreletics/alternate-projects, main @ fc1d29a. Times ET.

## Read first (in order)
1. docs/bots/DECISIONS.md (main fc1d29a)
2. docs/bots/shopify-theme/WEBSITE-STATE-2026-10-20.md (fc1d29a): full state
3. docs/bots/shopify-theme/WEBSITE-DECISIONS-2026-10-20.md (fc1d29a; from PR #6 commit 35537b6)
4. docs/bots/shopify-theme/REVIEWS-JUDGEME.md (a5da293)
5. docs/bots/funnel/CALCURATES-2026-10-20.md (a736869): FINAL Calcurates email text
6. docs/bots/shopify-theme/routines.md (fc1d29a): exact routine prompts
7. Previous handoff: /workspace/handoffs/2026-10-19-website-refresh.md

## Lane scope
- Website bot `25c9f763-68b9-4775-997c-f9c061016224`, lane `shopify-theme` (Site Design). Replaced `b1d7deda` on 2026-10-19.
- Live theme `187144929571`. Draft for work `189135978787`. Any theme push needs Andrew's explicit go.
- Push procedure: Shopify CLI on Mac `b9c0e142`: fresh pull, backup, minimal diff, `theme push --only ... --nodelete`, then pull and md5 verify.
- Prefer Pages/admin edits over theme code. Never revert older than the post-launch baseline.
- Calcurates is the funnel lane (`docs/bots/funnel/`). EFS Set Up bot is retired.
- Doc pushes to GitHub don't need a separate go. Shopify, Judge.me, Help Scout or email changes do (guard check first, per 2026-10-19 HARD RULE).

## Anti-drift rules (Andrew / Papa Grok, 2026-10-20)
1. Ground every answer in GitHub before speaking: `docs/bots/DECISIONS.md` first, then the lane file.
2. Never drift from what was agreed on a call.
3. Log every decision the same day: a `DECISIONS.md` line plus the lane file.
4. When a plan changes several times, log the final version and mark earlier ones superseded.
5. Keep prepared emails in files and read them word for word. Never rebuild from memory.
6. After each call decision read back "Agreed: X. Replaces: Y.", get a yes, write it immediately.
7. If it isn't saved, say "I don't have that saved."

## Settled decisions
- **Calcurates FINAL (3:28 PM ET 10/20):** the reply only acknowledges their tagging system. No rates, no Ground Advantage, no box sizes. Never say wholesale loses free shipping. The 2:45 PM and 2:58 PM positions are superseded. Email NOT sent; needs Andrew's go. Text: `docs/bots/funnel/CALCURATES-2026-10-20.md` ("FINAL email to Calcurates").
- **Judge.me feed:** stay on the XML feed for now. Hidden reviews stay off Google; the API feed is irreversible and sends hidden reviews; XML ends Jan 15 2027; 108 of 358 imported reviews won't count. Andrew sent support questions 10/20, waiting on a human reply. Early December reminder routine was offered, NOT created. Detail: `REVIEWS-JUDGEME.md`.
- **Judge.me Flows:** "Returns: skip Judge.me review request" (trigger Return approved) plus "[Grok] Judge.me - DON'T TOUCH" (Refund created, Return requested). Returned orders never get review requests. nancyzachem@gmail.com is blocklisted.
- **Size guide live 10/19 7:47 PM ET:** page `113607835939`, title "Size Guide", Default page template. Backups: `/workspace/size-chart-fix/BACKUP-admin-*-2026-10-19-1845.*` (box). Say "4 kinds of size link repeated across 61 pages", never "61 links".
- **Sizing:** Medium fits women's US 5.5 to 7.5. The pilot smaller size has no stated range; never give customers one. Frame it confidently as testing with people in that range to decide listing and sales.
- **Customer email voice:** sign "Andrea, Barreletics". Short. No apologies, no "we'd love", no "stay in touch", no dashes, never "gotten".

## Open items
1. **Card testing / fraud check (read-only):** Shopify settings/checkout, online_store/preferences, settings/payments, settings/apps, settings/shipping. Blocked: browser had no screen. Report to Social Perf `f7a36d04` and Andrew. Change nothing without a go. Don't touch the pixel, the FB/IG app or tracking.
2. **Lynn #1024:** sample shipped via FedEx 878942451745. Confirm order #5999 is held in eFulfillment.
3. **Margon #1037** (Florida, EU 40.5): needs her address.
4. **Carmen #943:** packing-slip photo draft (Andrew pastes).
5. **#1049 Soi Books:** handed to One-off Emails.
6. **Reviewer drafts open:** #1033, #1034, #1043 (Raeven still has the "really long time" line), #1044, #1045, #1046.
7. **Help Scout wholesale saved replies** 7.4 (id 4167565) and 7.2a (id 4167936): one shipping line each; full text `/workspace/hs-saved-replies/wholesale-shipping-update-2026-10-20.md` (box). Andrew pastes by hand. Flags: 7.4 code `0-WHOLESALE-STUDIO` doesn't match `0-WHOLESALE-STANDARD-COLORS`; broken FAQ link; "we'd love" in 7.2a and 7.8. **UNSETTLED:** the Calcurates FINAL position takes no stance on wholesale free shipping, so whether to change these lines at all is open. Ask Andrew before pasting.
8. **Re-send routine confirmation** to old bot `b1d7deda` so it deletes its copies.
9. **PR #6** (`website/decisions-log-2026-10-20`, 35537b6): content folded into main as `WEBSITE-DECISIONS-2026-10-20.md`; PR left open. Ask Andrew to close it.
10. **Judge.me seen log mismatch:** `judgeme-watch-seen.md` marks Rebecca, Marlene K. and susan s. as spam; Judge.me now shows them ok. Check, don't change visibility.
11. **Refund Flow:** 1 error at 8:29 PM ET Oct 19, not investigated.
12. **Size guide leftovers:** empty "Kids' (US)" header in theme code (theme push needs a go); "Sizing for kids" fit tip on /pages/sizing.

## Pending sends (none sent; each needs Andrew's go)
- Calcurates FINAL reply (funnel file).
- Margon #1037 and Carmen #943 replies (Andrew pastes).
- Reviewer drafts listed above.
- Wholesale saved reply edits (unsettled, see item 7).

## Routines
Recreate each exactly from docs/bots/shopify-theme/routines.md (same as /workspace/website-backup-2026-10-20/ROUTINES.md):
1. Judge.me new review watch: daily 10:00 AM ET, enabled.
2. Water Shoes Google rethink reminder: once Oct 25 2026 10:00 AM ET, enabled.
3. Phase two reviewer drafts due: once Oct 23 2026 9:00 AM ET, enabled.
4. Reviewer outreach batch 2 send check: once Oct 21 2026 8:00 PM ET, PAUSED (keep paused).
5. Box connection watchdog: hourly, enabled.
Then confirm to 25c9f763 so it deletes its copies (and re-send the pending confirmation to b1d7deda).

## First message for new bot
Read /workspace/handoffs/2026-10-20-website-refresh.md and the GitHub files above. Do not rescan or re-audit. Wait for one task.
