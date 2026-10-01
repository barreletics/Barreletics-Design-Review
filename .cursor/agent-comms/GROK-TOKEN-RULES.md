# Grok — token rules (mandatory)

From Cursor + Andrew (2026-09-30). Goal: keep automation, stop burning credits on context resend.

## Do

1. **Start heavy sessions** by reading (in order, no repo-wide grep unless the task requires it):
   - `AGENTS.md`
   - `.cursor/agent-comms/STATUS.md`
   - `.cursor/agent-comms/cursor-to-grok.md` (if site/dev)
   - Your lane section in `BOT-ROSTER.md` if present
2. **Reply to Cursor** only in `grok-to-cursor.md` — short blocks, file paths, commit SHAs.
3. **Scheduled runs** (Help Scout, Gmail, Xero, etc.):
   - Scope: *this run only* (e.g. tickets since last run).
   - Output: drafts + **5 bullets** in `log/YYYY-MM-DD.md`.
   - Do **not** summarize prior chat transcripts in the scheduled prompt.
4. **Cheaper model** for: implement, push, format, repetitive sweeps.  
   **Stronger model** for: architecture, legal/sensitive copy, publish decisions.
5. **Cross-bot:** write `@site-design` / `@finance` handoffs in `agent-comms/handoffs/` — never ask Andrew to paste another bot’s full thread.

## Do not

1. Re-run full-theme or full-repo audits if Cursor already documented result in `cursor-to-grok.md`.
2. Ask Andrew to paste Cursor diagnostic tables — read git.
3. Grow one Site Redesign thread for weeks — tell Andrew: *“Start a new chat in this bot; I’ll read agent-comms.”*
4. Touch Shopify theme **live** or theme `185687998755`. Draft work: only IDs Andrew/Cursor rules allow (currently M4 QA **187144929571** unless Andrew says otherwise in **this** message).

## Site Redesign lane reminder

Templates JSON, Type OS, press-row, page-about-facts = Grok when assigned.  
PDP media-img gates P6–P8 = **Cursor** unless Andrew explicitly moves task.
