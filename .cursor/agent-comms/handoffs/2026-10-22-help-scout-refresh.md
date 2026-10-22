# Help Scout bot refresh — 2026-10-22
- Current bot: 53107b2d-43b1-4480-9365-19364cabd835 (Barreletics Help Scout, mailbox 369185). Draft only, never send.
- Full state: docs/bots/communications/HELP-SCOUT-STATE-2026-10-22.md (extends HELP-SCOUT-STATE-2026-10-20.md).
- Load: communications/HOME.md, both DECISIONS.md files, both state files, TONE-EXAMPLES.md, REVIEW-OUTREACH-SYSTEM.md, ADVANCE-REPLACEMENT-WORKFLOW.md.
- Top open items:
  1. #5026 Violet: replacements CS-LG-TQ + CS-MED-DR unfulfilled; label first, fulfill when Andrew says go. Don't restock originals until they arrive.
  2. Re-check 1 extra committed unit each on CS-LG-TQ / CS-MED-DR (stale test edit).
  3. Andrew's OK pending: Shopify Processing (6993e6c7) owns advance-replacement tracker; 3PL & Inventory restocks.
  4. Margon #1037 ACTIVE, waiting on us (flagged to Andrew).
  5. Kristyn #969: finish wholesale setup, write playbooks/WHOLESALE-ACCOUNT-SETUP.md, draft reply from saved reply 7.4.
  6. Email card to stefanie@ + andrew@ awaiting Andrew's Send; old team@ card to be discarded. Internal notices never to team@.
  7. Nov 5: Lynn #1024 + Margon #1037 follow-up drafts sent by Andrew/Stefanie (routine 2 reminds).
- Shopify token: /workspace/shop_token.py (app grok-bot-admin-3).

## Appendix: routine prompts (verbatim)

ROUTINE 1: "Help Scout inbox check + drafts"
Schedule: CRON_TZ=America/Detroit 40 8,14 * * 1-5 (flexible, ±15 min)
Prompt (verbatim):

Check Barreletics' Help Scout mailbox (369185) for open/active tickets that need a first reply or a follow-up and don't already have the purple `grok draft` tag (formerly `grok draft ready`, renamed 2026-10-18). Read with the Help Scout connector (read-only; look up tool schemas each run).

For each ticket that needs a reply, write a draft using the reply guide (/workspace/hs-drafts and /workspace/hs-saved-replies notes, the existing saved replies, and past staff replies; refine existing wording, don't invent copy or policy). Save it as a DRAFT in Help Scout through a browser (computerUse) task in the box Chrome, which is logged in. Every browser task must say: never send, never schedule, never press Cmd/Ctrl+Enter, don't change assignee or status (tickets stay Unassigned so Andrew and Stefanie both see them; the composer status dropdown defaults to Closed, so leave the ticket's status as is), add the existing purple tag `grok draft`, stop if it shows "Unable to update draft", reload to verify, and take a screenshot saved under /workspace/hs-drafts/<date>/. Hard rule (Andrew, 2026-10-19): nothing is ever sent, scheduled or executed without a full-content guard check shown to Andrew first; this routine only drafts.

Help Scout tags (renamed 2026-10-19, see /workspace/docs/bots/communications/REVIEW-OUTREACH-SYSTEM.md):
- `grok draft` on every bot-prepared draft.
- Review-recovery outreach: `judge me` (formerly save judge me), plus `win back` (formerly free pair win back) when a free pair is offered.
- Outreach sending tags: `send small proto`, `send soft medium`, `soft ask size`, `ask size`, `send new medium`, `send medium`, `check in only`.
- Problem tags: `slipping`, `tore`, `too big`, `too tight`, `hard put on`, `bunions`, `between sizes`.
- Other: `we never replied` (customer contacted us and never got a reply).
Use these exact names on new drafts where they apply. Never remove or change tags on existing conversations.

REVIEWER OUTREACH HOLD (2026-10-19): do not touch, edit, retag, draft on, schedule or send anything in #1024 or #1033 through #1046. Website owns them and Andrew will give a go himself.

Tone: warm, plain, short, matter-of-fact; no hype, no dashes, never the word "gotten". Every customer reply ends with the sign-off "Warmly," on one line and "Andrea" on the next. No internal notes in customer email.

Customers who are between sizes: add them (name, email, ticket #, sizes, date) to /workspace/hs-saved-replies/softer-material-waitlist.csv when drafting their reply.

Return Zap tickets (from returns@returnzap.com, subject "New return for Shopify order #… requires approval"): read each item's Return Reason and the customer's typed note (the unlabeled line under Return Reason). The ticket's customer is Return Zap, so every draft must put the customer's email (from the email body) in CC; leave the To field as is (expect a bounce from Return Zap). Use the customer's first name if visible, otherwise "Hi there,". Text wrapped in **double asterisks** in the template files must be made bold in the Help Scout editor (don't type the asterisks). Templates in /workspace/hs-saved-replies/:
- Too Large, size L: returnzap-save-too-large.txt (offer to size down, plus the thin-sock line).
- Too Large, size M (can't size down): returnzap-save-too-large-M-sock.txt.
- Too Small, size M: returnzap-save-too-small.txt (offer to size up).
- Too Small, size L (can't size up): don't draft; list it for Andrew.
- Reason Other: draft only if the note clearly calls for a specific answer (for example, a sizing or fit complaint gets the matching template); otherwise list it for Andrew.
If a note shows the customer is angry, has a defect, or has anything unusual, don't use the template: list it for Andrew. Never approve, refund, or change anything in Return Zap.

Defective/torn tickets where the customer has already sent photos: draft the torn-replacement reply (/workspace/hs-saved-replies/8.4-Quality-torn-replacement.txt; Andrew rules we replace torn pairs, photos go to the manufacturing team, we may ask for the pair back and will keep them posted).

Trial wholesale/instructor requests: follow skill wholesale-trial-instructor-code (0-WHOLESALE-INSTRUCTOR 25%, add their email to the Shopify code in the same pass). Studio terms are 50% off with a 10-pair minimum. Wholesale shipping rates only in the Help Scout wholesale template.

Standing rules: call the product "Performance Skins", never "shoes" (their "usual shoe size" is fine). No pool/water use, no antimicrobial claims, no private wholesale codes (except the approved-studio reply 7.4), no placeholders except the Help Scout variable {%customer.firstName,fallback=there%}. Never name the tools or vendors we use in customer replies. Never promise refunds, replacements (other than the torn-pair rule), gifts, or free color swaps. Influencer pitches get the simple decline. Skip vendor, system, and internal emails. Leave alone unless Andrew wrote first: #842 Susan (teacher code, with Distribution), #1013 Natalia, #1006 Violet reship, Nancy #5832 replacement (pending Andrew).

Never send anything. When done, tell Andrew in a short, plain list which tickets got drafts (ticket # and one line each) plus any yes/no questions. If nothing needed a draft, stay quiet and send nothing.

ROUTINE 2: "Judge.me saves follow-up (Lynn + Margon)"
Schedule: one-off, CRON_TZ=America/Detroit 0 9 5 11 * (exact)
Prompt (verbatim):

It's the two-week follow-up for the Judge.me saves (Andrew's 2026-10-22 decision): Lynn (Help Scout #1024, conversation 3485659751, order #5999) and Margon Wynn (Help Scout #1037, conversation 3486873761, order #6016). Unsent follow-up drafts were saved in both conversations on 10/22 ("Just following up to see how the ... pair is working out ... Fingers crossed! Warmly, Andrea"). Check (read-only via the Help Scout connector, or the box browser) that both drafts are still there. If one is missing, recreate it in the box browser with the same wording. Never send the customer emails. Then do two things: (1) tell Andrew in chat that both drafts are ready to send today, with links. (2) Remind Stefanie: draft an email card (DraftExternalMessage, from Andrew's Gmail) to stefanie@barreletics.com saying the Judge.me win-back follow-up drafts for Lynn #1024 (order 5999) and Margon #1037 (order 6016) are ready to send in Help Scout today. They're short check-ins to see if anything improved. Andrew presses Send. This is a one-off: pause or delete this routine after it runs.
