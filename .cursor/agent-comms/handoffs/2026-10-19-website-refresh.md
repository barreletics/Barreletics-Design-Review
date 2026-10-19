# Website refresh — 2026-10-19 evening (old bot b1d7deda-373f-4f8b-9986-b349720604c8, ~1,570 msgs)

## Role
Barreletics Website (Site Design). Live theme 187144929571 (live since 10/8); any theme push needs Andrew's explicit go. Theme, PDP, Home, collections, content pages, day-to-day storefront. Also currently owns reviewer outreach (Judge.me low-star win-back in Help Scout) per docs/bots/communications/REVIEW-OUTREACH-SYSTEM.md in barreletics/alternate-projects. Prior handoff: /workspace/handoffs/2026-10-15-website-refresh.md.

## Standing rules
- HARD RULE (10/19): nothing sent, scheduled, pushed or executed without a side-by-side guard check of the full content shown to Andrew first, then his go.
- Theme pushes: Shopify CLI on Mac b9c0e142 (fresh pull, backup, minimal diff, push --only --nodelete, md5 pull-verify) or the box theme key with backup + pull-verify. Prefer Pages/admin edits that don't touch theme code. Never revert older than the post-launch baseline.
- Outreach emails: no dashes, never "gotten", signed "Andrea, Barreletics", sent as Closed. Internal notes go on each conversation right after its email sends.
- Short replies. Draft-first for anything outbound.

## Open items
1. Size guide: rebuilt as plain page content (no kids column, same wording, fit tips, Shop Now, help links). Preview shown 10/19 5:12 PM; NOT live. Waiting on Andrew's go to paste into the "Shoe Size Chart" page in Pages (no theme code). Done today: kids column removed from /pages/sizing; Medium kids value cleared on the theme size guide setting (backup saved); /pages/sizing table replaced with links to the size guide; all 61 live pages checked, every shoe size link goes to /pages/performance-skins-size-chart. Leftovers: empty "Kids' (US)" header (theme code) and "Sizing for kids" fit tip on /pages/sizing. Youth/kids sizes stay off the site until the youth line launches. FAQs never list sizes; they point to the size chart.
2. Reviewer outreach drafts in Help Scout: group one #1033 to #1038 plus #1041 updated with the new 3-paragraph opening (pilot invite as a question, complimentary pair). All Closed, nothing scheduled; Stefanie to read them; Andrew said group them afterwards and give a send time. Lynn #1024 went out (sent by the team). Angela #1033 has no "send" tag yet (size undecided). Raeven #1043 still says "We know it's been a really long time". Only Lynn's internal note is posted. Files: /workspace/reviews-google/recovery/ (tag-plan, outreach-tracker, hs-internal-notes-FINAL 2026-10-19). Archive: alternate-projects PR #4 (branch outreach-archive-2026-10-18), open, not merged.
3. Help Scout tag names (renamed 10/19): win back, judge me, send small proto, send soft medium, soft ask size, ask size, send new medium, send medium, check in only; problem tags slipping, tore, too big, too tight, hard put on, bunions, between sizes; we missed; grok draft. Help Scout bot 53e39134 has a hard hold on #1024 and #1033 to #1046.

## Routines
The old bot will send its exact routine list (it runs the daily 10 AM ET Judge.me sweep per the outreach doc). Recreate each one exactly, then confirm back to the old bot so it deletes its copies.

## First message for new bot
Read your handoff at /workspace/handoffs/2026-10-19-website-refresh.md and shared user memory. Do not rescan or re-audit. Don't message Andrew to say you're set up; wait for one task.
