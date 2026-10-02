# Automation inventory (all Barreletics bots), 2026-10-02

Compiled by Grok Bot, read-only. No bot was messaged or changed.
**Sources:** box snapshot `/home/box/agent-data/agents/*/automations/*.json`, plus `automation-changed` events in each bot's local transcript. That snapshot ends Sep 15–20 (synced to the box Oct 1 10:41 PM ET). The rest comes from the Invoice → Xero group posts, the Site Redesign memory export and refresh handoff (Oct 2), `ANDREW-TOKEN-GUIDE.md`, and the GitHub API.
**Caveat:** the ReadTranscript tool was not available to this subagent. Routines created on the server after about Sep 20 can't be seen from the box. "Confirmed" means a definition or recent first-hand evidence exists. "Last known" means it is inferred or older than Sep 20.

## Grok routines

| Bot | Routine | Schedule (ET) | What it does | Writes / sends? | Status |
|---|---|---|---|---|---|
| Grok Bot | Bot chat-size refresh and GitHub backup | Weekdays 6:24 PM | Checks bot chat sizes against the 400-entry refresh threshold and backs up to GitHub | Writes git commits/pushes; messages Andrew | Confirmed (given by Andrew) |
| Finance · Xero (22cfe83c) | Daily invoice → Xero Files | Weekdays 8:00 AM (`0 8 * * 1-5`) | Scans Gmail for vendor invoices and receipts, gets the PDF or a screenshot into Xero Accounting → Documents, matches only on a 100% fit, quiet if nothing new | **Yes**: forwards to the xerofiles inbox, uploads to Xero, may match bills; messages Andrew | Last known: enabled (created 9/16, updated twice 9/16, ran OK 9/16, ran 9/17 per group chat) |
| Gmail Inbox / "Daily Gmail" (bad05d1f) | Morning Gmail triage | About 8:00 AM **daily, including Sat/Sun** | Triages the inbox, drafts replies, and posts invoice candidates to the Invoice → Xero group | Writes Gmail drafts; posts to the group, which wakes Xero | Last known (no definition on the box; seen 9/17–9/20 in group posts) |
| Site Redesign · Director (f98d3d1b) | Barreletics commit reminder | Weekdays 5:00 PM (`0 17 * * 1-5`) | Checks the Mac Design Review repo for uncommitted approved work and reminds once; quiet if clean | Chat message only | Last known: enabled (4 OK runs 9/10–9/15) |
| Site Redesign (0b84b5bd) | Weekday design repo commit check | Weekdays 5:15 PM (`CRON_TZ=America/Detroit 15 17 * * 1-5`) | Same job as the Director's commit reminder | Chat message only | Last known, **conflicting**: listed in the bot's own memory export (10/2); the refresh handoff says "Routines: none" |
| Help Scout (e925d39b) | Scheduled Help Scout draft runs ("3× Help Scout") | About 3× per day (exact times unknown) | Pulls active and pending tickets and writes draft replies (latest batches 9/29 and 10/2 in `/workspace/hs-drafts`) | Writes drafts or screenshots; nothing sent | Last known (`ANDREW-TOKEN-GUIDE.md` mentions it; no definition seen) |
| Stalk Bot (446f8426) | Competitor "pulses" | Unknown | Its role says "each pulse reports" | Reports to chat | Unknown (no definition seen) |
| Site Redesign · Director | Shopify legal policies desktop reminder | n/a | One-off reminder | n/a | **Deleted** 9/11 (created 8:59, deleted 9:09) |

No routines were found (box or docs) for: One-off Emails, Finance · Forecast, Front Desk, Website, Admin workflows, Manufacturing Docs, Manufacturing Forecast, Blog, Email Templates, Venice Biennale Postcard, Partner codes, 3PL & Inventory, Image Editor, Go-live, Go-live 2, QC, or Evolving Grok. Bots created after about 9/20 can't be checked from the box.

## Non-Grok automations

| Where | Automation | Trigger | What it does | Writes? | Status |
|---|---|---|---|---|---|
| GitHub `barreletics/Barreletics-Design-Review` | `.github/workflows/` on `cursor/apparel-pdps-c982` | n/a | **No workflows folder on this branch or on main** (API returns 404) | n/a | Confirmed none |
| GitHub Actions registry | `ai-review-pr.yml` | PR (historical) | AI PR review. Still registered as "active", but the file no longer exists on main or this branch, so it can't fire | n/a | Confirmed dormant |
| GitHub Pages | pages-build-deployment | Push to `finish-home-collections` | Builds the Pages site (524 runs total; latest 9/30 ~9:56 PM ET) | Deploys Pages | Confirmed active |
| Cursor | Cursor automations / cloud agents | n/a | None found in the repo (`.cursor/hooks.json` only has local git anti-revert hooks) | n/a | Confirmed none in repo |
| Shopify Messaging | Welcome series (draft), SAVE10, abandoned cart, winback | Shopify | Customer emails (not a bot routine; noted for overlap) | Sends customer email | Last known (welcome is a draft and not turned on) |

## Overlaps to fix
1. **Commit reminder runs twice:** Director at 5:00 PM and Site Redesign at 5:15 PM do the same check. Keep one (or neither, since Grok Bot's 6:24 PM backup covers git).
2. **Invoice intake runs twice:** Daily Gmail's triage and Xero's 8 AM routine both scan Gmail for invoices, and the group post wakes both bots. Pick one owner.
3. **Daily Gmail runs on weekends** with mostly noise (9/19, 9/20). Make it weekdays only.
