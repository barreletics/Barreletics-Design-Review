Author: Grok Bot
Papa Grok can reach Grok Bot (agent id aa3b203e-439b-4c78-b271-222e1cbb46ba) directly for questions or handoffs on the eFulfillment go-live work.
# Grok Bot (front desk / director) handoff #2 — 2026-10-03 10:00 AM ET
Role: Andrew's front desk + director for Barreletics. Plan, delegate (cloud agents for repo work, executors for pushes), review. Short messages. Lives in sidebar section "Grok".
Standing rules: see shared user memory (push protocol to DRAFT 187144929571 only via Shopify CLI on Mac b9c0e142, temp dir, backup + base check + one file + --only --nodelete + pull-verify; never live 185687998755; never templates/*.json or config unless named; push without asking, tell after).
Done today on draft (verified): PR32 a066cdb, PR33 a4f05b0, PR34 0240403, PR35 b6a8138 then acd8a93 (hero live TE preview), PR36 108fff6 (problem-section live preview). Backups /workspace/backups/2026-10-03-pr32,-pr34,-pr35,-pr35b,-pr36. Andrew confirmed live preview works.
Lesson: TE only live-updates CSS in {% style %} that reads section.settings.* directly (not top-level assigns). Base for a file = last commit pushed to that file (PR34 touched many sections).
IN PROGRESS: cloud agent bc-93bd2b56 (watch it) — (a) bring remaining photo+text split sections to fifty-fifty controls, (b) remove never-read settings without changing look at saved values, (c) unify padding sliders in EVERY section (same ids/labels/order, defaults in label, live preview, no visual change). One commit per section, PR stacked on #36. When it reports: review, push each section file one at a time, tell Andrew.
Andrew delegated the removable-controls decisions to me ("you know what to do"); he's QCing in parallel.
Then: merge PRs 31–36+ when Andrew says, hand site work to Website bot (3f1bef3b).
Other cloud agents: bc-99f729ff (PR32), bc-1f053b9f (PR34), bc-50ac1bb3 (PR35) — idle.
Distribution bot 94d7b30c created (Ops); Andrew talks to it directly.
Routine to recreate: "Bot chat-size refresh and GitHub backup", cron 24 18 * * 1-5 ET — check bot chat sizes, refresh long bots per bot-refresh skill, back up handoffs to git, silent if nothing to do.

## 2026-10-13 call — Barreletics Shopify go-live with eFulfillment
Order routing: confirmed eFulfillment first, Barreletics second. Shopify can't disable routing once multiple locations take online orders.
Managed Markets (MM): works by country, not shipping profile. International pricing tests are only real with MM off.
Final test plan sent to Eric (madsen.e@efulfillmentservice.com) as a reply in Gmail thread "Re: Quick inventory question for go-live":
- Eric's fixes first: 30-min flow lacks weekend check; wholesale draft flow checks 0-Wholesale but real code is 0-HWholesale, and move step is on wrong branch; 12:30–1:00 paid orders go out immediately.
- April intermittent out-of-stock question; international connector question.
- Location cleanup: turn off old manual eFulfillment Center online orders after stock moves; remove Old Stock from shipping profiles; turn off both QC Hold locations.
- Test item published at $100, then unpublished. Draft orders before website checkouts.
- Layer 1 domestic rates/function. Layer 2 international function, MM on. Layer 3 international pricing, MM off then back on. Layer 4 profitability review with Andrew's 90–100 day invoice matrix. Layer 5 go-live: shut off old API, move products to new shipping profile, test every US and international region in first five minutes.
- Timing: tests 11–12, meet at 12 or after.
Invoice matrix ready for rate table comparison. No store settings changed.

## History from the old 3PL bot
- April go-live Apr 6 on eFS app; app disconnected Apr 17 (efs-golive-check/previous-connection-timeline.md).
- Intermittent out-of-stock: domestic "sold out" Apr 6–11 from wrong routing (eFS manual location, then eFS app, then Barreletics, then pickup, plus duplicate eFS location); fixed Apr 10–11. International "all sold out" Apr 6–12 because MM needed a non-3PL location; workaround was "sell when out of stock" at Barreletics, FedEx account removed from intl profile, 24-hour intl hold. Loss ~$15K that week, $20K+ by May 4 (fulfillment-handoffs/EFS-MASTER-KNOWLEDGE.md §6).
- MM vs connector: eFS (Nick Apr 14, Angela May 26, Steve Jun 23) attributed the intl blackout to MM with a 3PL; Eric later said the app has its own MM conflicts. No documented blackout happened with connector only (routing off, MM off) (previous-connection-timeline.md). Sep 15 decision to move off MM; MM still on as of Oct 12 (REVIEW-2026-10-13.md).
- Locations: old manual "eFulfillment Center" 111727542563 (created Apr 4, not a fulfillment-service location) holds real stock; new app location "Efulfillment Service - 2015" 114571313443 (installed Sep 28) is empty — turn off online orders at the old one after Eric moves stock (REVIEW-2026-10-13.md; previous-connection-timeline.md). Old Stock location 114832769315 sits in shipping profiles; Andrew wants it and both QC Hold locations removed, linking extra locations to the intermittent out-of-stock problem (REVIEW-2026-10-13.md).
- Prior notes: Oct 12 review said not safe to go live until Integration 5510 retired (double-injection risk), eFS stock consolidated into 114571313443, and customs data complete. eFS portal automatic fulfillment requests = No. Eric's Oct 12 hold flow: 30-min hold, immediate send 12:30–1:00, 2-hour weekend hold; store timezone must be Eastern (EFS-MASTER-KNOWLEDGE.md §6).

## Open items
- Waiting on Eric's reply and call time.
- EFS Go-Live bot (69cd9920-b751-4275-af4d-1634265851fc): open question for Papa Grok, as the new owner of this work, whether to hide or retire it. Andrew leaned toward hiding rather than deleting in case it's needed later. Not decided.
