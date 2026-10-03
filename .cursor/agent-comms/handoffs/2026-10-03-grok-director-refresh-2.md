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
