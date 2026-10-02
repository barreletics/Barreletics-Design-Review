# Bot efficiency review: Email Templates, Help Scout, Finance · Xero (2026-10-02)

Read-only review by Grok Bot. Refresh threshold: **400 entries**.
**Method and caveat:** ReadTranscript was not available. I sampled each bot's local transcript (`store.db` plus its jsonl) and its routine files. The local copy is a frozen snapshot that ends **Sep 16**, so entry counts are floors (the real numbers are now higher). For "last ~2 weeks", I relied on artifacts on the box (`/workspace/hs-drafts`, receipts, the Invoice → Xero group).

## 1. Email Templates / "Email Campaign" (c5982362): **needs refresh + fixes**
- **Entries:** 550 at snapshot (136 Andrew msgs, 259 bot msgs, 140 model turns, 11 subagents). That is over the 400 threshold.
- **Routines:** none.
- **Waste:**
  - **Screenshot ping-pong.** 65 bot messages ask Andrew for a screenshot or paste, or give "next click only" steps. Because Cloudflare blocks Shopify Admin, each Admin step costs a full-context turn.
  - **Long messages.** 17 messages run over 3,000 characters, and 28 file attachments were re-sent.
  - **Stalled.** The last message (9/16) is "still waiting on your screenshot", a re-ask.
- **Delivered:** Welcome series v1–v3 HTML plus a Sidekick handoff pack (welcome stays draft, not on); email-flow audit previews; 60-day recent-buyer exclude decided. Nothing visible from 9/18 to 10/2.
- **Top fixes:**
  1. Refresh the chat now (write a handoff, start a new bot).
  2. Batch Admin steps: one message with the full click list and one screenshot back, not click-by-click.
  3. Park the bot until Andrew sends the Automations screenshot. No re-asks.

## 2. Help Scout (e925d39b): **efficient**
- **Entries:** 38 at snapshot (7 turns). The chat is small.
- **Routines:** "3× Help Scout" scheduled draft runs (last known, per the token guide; times not visible).
- **Waste:**
  - **Browser drafting.** Drafts are captured as browser screenshots (`draft-*.png`, about 140 KB each) on top of the text drafts.
  - **Possible empty runs.** With 3 runs a day, some likely fire with nothing new (the 9/29 batch had 12 of 16 conversations skipped).
- **Delivered:** Ops spine (FLOW, TICKET-TYPE-MAP, AUTO-DRAFT-RULES), a 38-saved-reply inventory, a closed-ticket playbook, and draft batches on 9/29 (16 conversations, 4 drafts) and 10/2 (#907, #918). Nothing was sent.
- **Top fixes:**
  1. Quiet-when-nothing rule: no message if there are no new or changed tickets since the last run.
  2. Cut to 2 runs a day (morning and late afternoon) on a cheaper model with a fixed short prompt.
  3. Use the Help Scout MCP (read) plus text drafts. Drop the browser screenshots unless Andrew asks for them.

## 3. Finance · Xero (22cfe83c): **needs refresh + fixes**
- **Entries:** 396 at the 9/16 snapshot, and almost certainly **over 400 now**. It went from 0 to 396 in 2 days (90 turns, 22 subagents), and its daily routine runs inside this same chat.
- **Routines:** Daily invoice → Xero Files, weekdays 8:00 AM, with a long (~1.7 KB) multi-step prompt.
- **Waste:**
  - **Every update sent twice.** A voice-style spoken version plus a text version (for example "Costco warehouse one ten oh six" followed by "Costco WHSE $110.06").
  - **Filler status pings.** 131 progress updates, such as "Still working" and "sweep is running".
  - **Duplicate invoice intake.** Daily Gmail posts candidates in the group, Xero re-confirms them, and the two bots trade acknowledgements ("Sounds good", "Got it").
  - **Weekend posts.** Daily Gmail posts on weekends too, which wake Xero.
  - **Browser screenshots.** HTML-only receipts are captured with browser screenshots.
- **Delivered:** Bank-feed Find & Match on ···4473 and ···5003, intake of the Help Scout $60, PDS $1,039, and Color Master $1,966.35 receipts into Documents, and later receipt captures (DHL, Alibaba/PayPal, 9/23–9/24 meals) seen on the box. The Xero connection broke on 9/18 (`invalid_client`).
- **Top fixes:**
  1. Refresh the chat, and recreate the 8 AM routine on the new bot so the routine doesn't resend a 400+ entry context every morning.
  2. One owner for Gmail-to-Xero intake (keep Xero's routine, drop Daily Gmail's invoice posts, or the reverse). Make the routine quiet-when-nothing and run it on a cheaper model.
  3. Send one message per update, with no spoken-plus-text duplicates and no "still working" pings.
