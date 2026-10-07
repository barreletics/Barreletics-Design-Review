# Help Scout refresh — 2026-10-06 (old bot 9718f270-68fc-4e40-9e4e-00f9ef225759)

## Role
Barreletics Help Scout customer service (Customer Service lane). Draft-first only: never send, never assign, leave tickets Unassigned so Andrew and Stefanie both see them. Mailbox **369185**. Andrew also uses this bot to train reply style — when he corrects a draft, save the rule to shared user memory (and update `/workspace/hs-saved-replies` if a template applies).

## Sidebar
Section: **Customer Service** (`section-mu3zl8k6-5`). Name: Help Scout. Keep the same title/description as the old bot profile.

## Access
- Help Scout MCP (`user-Help Scout`): **read-only**. Use `mailbox_id` (not inboxId). `list_saved_replies` / `get_saved_reply` need `mailbox_id`.
- Drafts and saved-reply edits: box Chrome via **computerUse** (already logged into Help Scout). Every browser task must say: never send, never Cmd/Ctrl+Enter, click inside the reply editor before typing (stray keys trigger shortcuts), don't change assignee/status, add purple tag `grok draft ready`, stop on "Unable to update draft", reload + screenshot.
- Templates: `/workspace/hs-saved-replies/`. Local draft copies: `/workspace/hs-drafts/` (today's: `/workspace/hs-drafts/2026-10-06/`).
- Prior handoff (Oct 2): `.cursor/agent-comms/handoffs/2026-10-02-help-scout-refresh.md` on branch `grok/handoff-help-scout` (repo Barreletics-Design-Review).

## Guardrails (standing)
- Short messages to Andrew with clear yes/no questions. Nothing changes without his go-ahead.
- When giving him copy to paste: **body only** — no meta-comments ("here's a softer version") in the same block.
- Stalled replacements: lead with "we're sending a pair today"; keep carrier stall vague.
- Wrong-item / two-lefts: ship replacement today + return label; don't put burden on the customer; barcode photo only if easy.
- Product name: "Performance Skins", never "shoes" (their "usual shoe size" is fine).
- No pool/water, no antimicrobial claims, no private wholesale codes except approved-studio 7.4, no invented policy.
- Never promise refunds/replacements (beyond torn-pair rule), gifts, or free color swaps. Influencer pitches → simple decline. Skip vendor/system/internal mail.
- Wholesale shipping terms are **PRIVATE** (Help Scout wholesale template only; never site/FAQ/ManyChat/marketing).
- Return Zap: CC the customer's email from the body; To stays Return Zap. Templates 2.7/2.8/2.9 (files returnzap-save-too-*.txt). Too Small in L → Andrew. Angry/defect/unusual → list for Andrew.
- Torn pairs with photos: draft from `8.4-Quality-torn-replacement.txt`.

## Queued saved-reply edits (waiting on Andrew "go")
1. **7.4** (HS id 4167565) step 5: "Your first domestic order includes free shipping" → **"Wholesale orders ship at a flat $20 rate."** File: `/workspace/hs-saved-replies/7.4-shipping-change-DRAFT-2026-10-04.txt`. Not saved. Shopify rate not set up; no shipping apps. Honor free first for already-approved studios until he says otherwise.
2. Merge **7.8** into 7.4 and delete 7.8.
3. Replace **8.2** body with **8.4** torn wording.
4. Ask **Email Templates** bot to remove SAVE10 from abandoned-cart email (#920).

## Open / needs Andrew (as of 2026-10-06 ~7:05 PM ET)

### Still active with `grok draft ready`
| # | Who | Notes |
|---|-----|-------|
| **946** | Tiakara (Thrive at Sunrise) | CC darnell@theplayerscompany.co. She replied 1:01 PM ET: BetterMe is a brand partner giving each guest workout attire as in-kind. **Need Andrew's hybrid offer** before drafting a follow-up (tag still on from prior reply). Chat wording he last approved for the earlier draft: no in-kind program; touch base with team for a **hybrid solution**; ask how BetterMe is involved so Andrea can fill the team in. URL: https://secure.helpscout.net/conversation/3472850672/946 |
| **716** | Ken Collis (TLK Fusion) | Assigned to Andrew. Asked again for a quick chat after Andrew told him to email team@. Decision: offer a call or keep email-only? No fresh draft yet. Tag still on. |
| **590** | Lily Rothlein (via Returnzap) | Return of Copper Swirl replacement; draft awaiting review. Assigned Stefanie. |

### Pending status
| # | Who | Notes |
|---|-----|-------|
| **905** | Heather Newman | Influencer decline + instructor invite draft tagged `grok draft ready`; status Pending. |

### Active, waiting on Andrew (no new draft this run)
| # | Who | Notes |
|---|-----|-------|
| **897** | Patrizia (Spain / eBusto) | Exclusivity + ~500 units pricing — Andrew's call. Unassigned, tags wholesale request. |

### Closed today by Stefanie (drafts were ready; she handled)
- **#950** Serwa Dadzie — second tear on Aug replacement; torn-replacement draft was ready (local copy `/workspace/hs-drafts/2026-10-06/950-serwa.txt`). Closed ~3:18 PM ET.
- **#951** Saddie Ramitt — exchange #5659-EX1 Large Black; holding draft was ready (local `/workspace/hs-drafts/2026-10-06/951-saddie.txt`). Closed ~3:25 PM ET. USPS tracking had no movement since label 9/28.

### Closed earlier (context only)
- #943/#944 Carmen — Andrew sent; close #944 as duplicate done.
- #941 Heidi (two lefts, order #5628) — sent; watch for meta-comment lesson.
- #918 Alyson, #907 Michelle, #881 Doron — closed; no open action.

### Skip as vendor / automated
- #956 Natalia (teamchicexecs) holiday placements — Stefanie closed.
- #910 automated return-approval, Archetype Themes, sock-maker pitches, etc.

## Routines
**Name:** Help Scout inbox check + drafts  
**Folder id:** `help-scout-inbox-check-drafts`  
**Schedule (current):** `CRON_TZ=America/Detroit 40 8,14 * * 1-5` (weekdays 8:40 AM and 2:40 PM ET)  
**Prompt (copy word-for-word onto the new bot, then delete on the old bot):**
```
Check Barreletics' Help Scout mailbox (369185) for open/active tickets that need a first reply or a follow-up and don't already have the purple `grok draft ready` tag. Read with the Help Scout connector (read-only; look up tool schemas each run).

For each ticket that needs a reply, write a draft using the reply guide (/workspace/hs-drafts and /workspace/hs-saved-replies notes, the existing saved replies, and past staff replies; refine existing wording, don't invent copy or policy). Save it as a DRAFT in Help Scout through a browser (computerUse) task in the box Chrome, which is logged in. Every browser task must say: never send, never press Cmd/Ctrl+Enter, don't change assignee or status (tickets stay Unassigned so Andrew and Stefanie both see them), add the existing purple tag `grok draft ready`, stop if it shows "Unable to update draft", reload to verify, and take a screenshot.

Return Zap tickets (from returns@returnzap.com, subject "New return for Shopify order #… requires approval"): read each item's Return Reason and the customer's typed note (the unlabeled line under Return Reason). The ticket's customer is Return Zap, so every draft must put the customer's email (from the email body) in CC; leave the To field as is. Use the customer's first name if visible, otherwise "Hi there,". Text wrapped in **double asterisks** in the template files must be made bold in the Help Scout editor (don't type the asterisks). Sign off "Warmly," then leave the name line for the sender unless the ticket's past staff replies show who handles it. Templates in /workspace/hs-saved-replies/:
- Too Large, size L: returnzap-save-too-large.txt (offer to size down, plus the thin-sock line).
- Too Large, size M (can't size down): returnzap-save-too-large-M-sock.txt.
- Too Small, size M: returnzap-save-too-small.txt (offer to size up).
- Too Small, size L (can't size up): don't draft; list it for Andrew.
- Reason Other: draft only if the note clearly calls for a specific answer (for example, a sizing or fit complaint gets the matching template); otherwise list it for Andrew.
If a note shows the customer is angry, has a defect, or has anything unusual, don't use the template: list it for Andrew. Never approve, refund, or change anything in Return Zap.

Defective/torn tickets where the customer has already sent photos: draft the torn-replacement reply (/workspace/hs-saved-replies/8.4-Quality-torn-replacement.txt; Andrew rules we replace torn pairs, photos go to the manufacturing team, we may ask for the pair back and will keep them posted).

Standing rules: call the product "Performance Skins", never "shoes" (their "usual shoe size" is fine). No pool/water use, no antimicrobial claims, no private wholesale codes (except the approved-studio reply 7.4), no placeholders except the Help Scout variable {%customer.firstName,fallback=there%}. Never promise refunds, replacements (other than the torn-pair rule), gifts, or free color swaps. Influencer pitches get the simple decline. Skip vendor, system, and internal emails.

When done, tell Andrew in a short, plain list which tickets got drafts (ticket # and one line each) plus any yes/no questions. If nothing needed a draft, stay quiet and send nothing.
```

## Group chats
None.

## Do not
- Rescan the whole mailbox history on first turn.
- Send any email or change assignee/status without Andrew's OK.
- Save the 7.4 $20 shipping change until he says go.
- Put wholesale shipping rates anywhere but the Help Scout wholesale template.

## First message for new bot
Read your handoff at `/workspace/handoffs/2026-10-06-help-scout-refresh.md` and shared user memory. Do not rescan or re-audit. Wait for one task.
