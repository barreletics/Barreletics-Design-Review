# Help Scout bot refresh (2026-10-12, from 62711973)
Read first: /workspace/handoffs/2026-10-06-help-scout-refresh.md (role, full guardrails, routine prompt).
1. Role: Barreletics Help Scout, mailbox 369185. The MCP is read-only, so drafts are made through box Chrome computerUse: tag "grok draft ready", leave assignee and status alone, reload to verify, save a screenshot under /workspace/hs-drafts/<date>/. The composer status dropdown defaults to Closed.
2. Sending: only when Andrew explicitly says send in chat (he did for #990 and #982 today). Otherwise draft only.
3. Tone: warm openers ("We'd love for you to..."), never "Great news". End at "Warmly," with no name unless asked. No internal notes in customer email. Say Performance Skins, never shoes.
4. Return Zap tickets: CC the customer email from the message body. A bounce flag is expected (no-reply To address). Close the ticket and wait; a customer reply reopens it.
5. Trial wholesale: clear studio or instructor wants to try pairs = draft the reply with 0-WHOLESALE-INSTRUCTOR (25%) AND add their email to that Shopify code in the same pass. Report every add. Iffy cases go to Andrew. Skill: wholesale-trial-instructor-code. Studio terms: 50% off, 10-pair minimum, most studios order 20 to 40.
6. Done today: #985 Maureen v5 draft saved (full content, she's on the code, 8 customers; Andrew sends). #990 Corrin sent 3:27 PM and closed. #982 Miriam sent 3:39 PM and closed.
7. Open, waiting on Andrew: #842 Susan (Royal Oak Pilates) 10%/10% teacher code is ON HOLD. Strategy handed to Distribution bot 94d7b30c, which will report back what to offer, then rewrite her draft. #989 Return Zap #5853 (acrobatbra@yahoo.com): draft a save-the-return check-in or just approve? #897 Patrizia terms, #716 Ken, #970 check-in are still unanswered.
8. Idea parked: Andrew is musing about replacing Help Scout with a shared Gmail inbox (support@ is a Google Group; Return Zap mails support@). Maybe later. Help Scout Docs or Beacon are worth trying if kept.
9. Routine: "Help Scout inbox check + drafts", folder help-scout-inbox-check-drafts, CRON_TZ=America/Detroit 40 8,14 * * 1-5. Recreate it from the 10-06 handoff prompt plus rules 3 to 5 above.
10. Standing order: message Andrew only when he wrote first or for a true blocker. Quiet runs send nothing.
