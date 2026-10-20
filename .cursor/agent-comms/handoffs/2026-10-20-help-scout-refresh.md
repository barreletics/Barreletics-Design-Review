# Help Scout bot refresh — 2026-10-20 (from 53e39134), for the replacement bot

GitHub barreletics/alternate-projects main commits: e8cbb0837ffec6078504204bab140736883dccab ("Help Scout bot state backup (2026-10-20)"); e05f6838b1c041c4dc3d7fb3816e00352912b6eb ("Help Scout state: add routine saved prompt verbatim (2026-10-20)"); 7874d979543f0c3ddb56535ed2264b950634891b ("Help Scout lane: 10/20 decisions, supersede old sign-off/tag/openers, today's open items, #1030 decline example"); d6bc560da68e579e3f116179f47fd9aece89d687 ("Help Scout state: lessons from 2026-10-20; keep #842 in HOME open items"); 150e0f64a0c1fd0c57504600509b16fc66ef085e ("Help Scout: Margon address off GitHub, closed tickets, vendor skips, lesson decisions (2026-10-20)", current main).
Files: docs/bots/communications/HELP-SCOUT-STATE-2026-10-20.md (full state, same as below); docs/bots/DECISIONS.md (5 dated lines added). Tone source: docs/bots/communications/TONE-EXAMPLES.md (dff4735, 1142aa1).
Load at startup: docs/bots/communications/HOME.md, DECISIONS.md, HELP-SCOUT-STATE-2026-10-20.md, TONE-EXAMPLES.md, REVIEW-OUTREACH-SYSTEM.md.


Bot: Help Scout agent `53e39134`, Barreletics Help Scout mailbox 369185. Backup ahead of a bot refresh. Nothing was sent to customers and Help Scout was not touched during this backup.
Prior handoffs: `/workspace/handoffs/2026-10-15-help-scout-refresh.md`, `2026-10-12-help-scout-refresh.md`, `2026-10-06-help-scout-refresh.md`.

## Role and hard rules
- Draft first, never sends. Andrew approves.
- **HARD RULE (2026-10-19):** nothing is sent, scheduled, finalized or executed without a full-content guard check shown to Andrew. See [`../OPERATING-STANDARD.md`](../OPERATING-STANDARD.md).
- **REVIEWER OUTREACH HOLD:** never touch #1024 or #1033 to #1046. Website owns them and Andrew gives the go. See [`REVIEW-OUTREACH-SYSTEM.md`](REVIEW-OUTREACH-SYSTEM.md).

## Tone
- Warm, short, plain, professional but human.
- No dashes. No "we'd love". No "stay in touch". Never "gotten". No apologies or pandering.
- Sign off: "Warmly," then "Andrea".
- Gold standard (Andrew, 2026-10-20; already in [`TONE-EXAMPLES.md`](TONE-EXAMPLES.md), commits dff4735 and 1142aa1):

```
Hi Lynn no problem.

Happy to hear in class no less!

Just a quick update: your pair is set to ship tomorrow. We've chosen one that should feel a little snugger. My only question is whether the length will be a noticeable improvement, but I'm hopeful it'll be a better fit overall. Fingers crossed!

Thanks again for your patience and for giving us a chance to try this.

Warmly,
Andrea
```

- Influencer decline: Andrew's #1030 wording (2026-10-18), file `/workspace/hs-saved-replies/influencer-decline-andrew-2026-10-18.txt` (signed "Barreletics Team"):

```
Hi Erica,

Thank you so much for reaching out and for your interest in Barreletics!

We appreciate your enthusiasm for our Performance Skins and your creative ideas. While we don't currently have a formal influencer or creator collaboration program in place, it's something we may explore in the future.

Thanks again for thinking of us, and we wish you continued success!

Best,
Barreletics Team
```

## Sizing and policy rules
- Size 8.5 normally stays Large. Don't suggest sizing down.
- Medium only in stretchier options (Dusty Rose, or Open Sole Rivian Green), framed as usually successful, not guaranteed.
- Dusty Rose is softer and stretchier.
- Narrow feet: suggest a thin sock.
- A return that is really an exchange: ask the customer to resubmit as an exchange; we reject the return to free it.
- Free replacement or giveaway pairs: Shopify draft order with 100% discount, tagged giveaway / unhappy customer.
- Canada: no free shipping. Free samples to Canada go FedEx with a full customs form.
- Studio wholesale: 50% off, 10 pair minimum.

## Customer fact (never mix)
- **Lynn Chua**, Aurora ON, orders #3490 and #5999, uses only `lmoulds422@gmail.com`.
- `michelle.mjbr@gmail.com` is a different customer: **Michelle Berger**, Jacksonville FL (#5842, #5983).

## FedEx: Lynn sample (DONE, finalized by Andrew 2026-10-20)
- Shipment `01a15a1d-3a71-7b6a-959d-453393adf917`, tracking 8789 4245 1745.
- Service: International Connect Plus $21.00 (chosen over Ground $48.03, Economy $44.46, Priority $52.14). Est. delivery Thu 10/22.
- Box 1 lb, 12x9x2. Item 0.64 lb, $10 Sample, HS 640299. CUSMA statement. DDP; duties and transport billed to Andrew. Notifications to lmoulds422.
- Label shows NSR ETD RES, so no paper invoice needed (EWO would need a paper pouch).
- Label and invoice PDFs: `/workspace/hs-drafts/2026-10-20/Lynn_Chua_label_878942451745.pdf`, `Lynn_Chua_commercial_invoice_878942451745.pdf`.
- **Flag for Andrew:** sender prints 42999 Woodward Ave, Bloomfield Hills 48304, possibly a typo for 42939.
- In FedEx Ship Manager never click CANCEL or EDIT.

## Open items
- Confirm order #5999 is held or removed from eFulfillment so it isn't double shipped.
- #5999 note says 10.2 lb; should be 10.2 oz.
- Andrew decides on keeping PluginHive before any charge.
- #1037 Margon (hold range): address 20321 W Country Club Dr, Coronado 1, Townhouse 6, Aventura FL 33180, size 40.5, sent 12:50 PM ET 10/20 after Andrew's softer-pair reply. Andrew/Website act.
- #1047 Return Zap #5842, reason Other, no note: waiting on Andrew.
- #1049 (ticket closed by staff): my two old drafts: delete or keep.
- Violet #1006 reship and Nancy #5832 replacement: pending Andrew.
- #842 Susan: on hold with Distribution.
- #716 has a grok draft.


## Closed by staff 10/20 afternoon
#943, #1049/#1050, #1051, #1024, #590, #1058, #1059, #1060.

## Vendor tickets the routine skips
#1011 (Judge.me), #913 (theme vendor), #588 and #207 (sock vendors).

## Pending sends
- None.
- `/workspace/hs-drafts/2026-10-20/lynn-sample-heads-up.txt` was never sent and is superseded by Andrew's own email.

## Lessons from 2026-10-20
- **Never claim Andrew confirmed something he didn't.** The bot wrongly said Andrew confirmed michelle.mjbr@gmail.com was Lynn's email. It then fixed its memory, the draft and the FedEx recipient (Lynn uses only lmoulds422@gmail.com).
- **Say a pair "ships tomorrow" until it actually ships.** Don't say "on the way, arriving Thursday" before it ships.
- **FedEx Ship Manager: always verify the sender address and the drop-off location.** Andrew's screen once showed 1450 Clarendon as the sender, and a Telegraph Rd drop box as the drop-off. The drop-off doesn't stay set after a reload until "Nearest" is clicked.

## Routine
- Name: "Help Scout inbox check + drafts" (folder help-scout-inbox-check-drafts).
- Schedule: `CRON_TZ=America/Detroit 40 8,14 * * 1-5`, flexible 15 min early or late.
- Saved prompt (verbatim from `/workspace/handoffs/help-scout-routine-prompt-2026-10-20.txt`):

````
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
````
