# Multi-agent architecture (token-safe)

Locked for Barreletics go-live period. Andrew’s setup: many Grok bots (Site Design, Help Scout, Finance, etc.) that were meant to “talk to each other.”

## What went wrong

- **Long chat threads re-send the whole history every turn** → cost scales with thread length, not with “memory.”
- **Pasting Cursor diagnostics into Grok** duplicates work both agents already did.
- **No one said on day one:** chats are sessions; **git + rules are memory.**

## Correct model (three layers)

1. **Canon** — `.cursor/rules/`, `.cursor/skills/`, theme code, planning docs. Updated when decisions stick.
2. **Handoff** — `.cursor/agent-comms/*.md` short blocks. Bot-to-bot = read file, act, write file.
3. **Session** — one Grok/Cursor chat per task or day. End with 5 bullets in `log/`. Start fresh next time.

## Bot-to-bot (cheap)

- **Do not** chain full transcripts Design → Help Scout → Finance.
- **Do** write: `@finance` / `@help-scout` tags in handoff, file paths, commit SHAs, one ask.
- Optional later: separate inboxes per domain (`out/finance.md`, `out/site-design.md`).

## Grok token discipline

- **New chat** for new task when thread is huge (sidebar: hide old chat for UI; idle chats cost $0 until you message).
- **Cheaper model** for implement/push; stronger model for architecture/copy/safety.
- Grok **does not** re-run full-repo scans if Cursor already posted result in `cursor-to-grok.md` — verify only if touching those files.

## Go-live vs draft (Sep 2026)

- Storefront work lands on **draft M4 QA** first; live publish is Andrew’s explicit call.
- **Cursor can finish PDP image gates (P6–P8) without Grok online.** Grok lane not required for that path.
- When Grok returns: TE/template work only in his lane; read `cursor-to-grok.md` before editing.

## Signatures (paste format)

- From Cursor: `From Cursor (Claude):` …
- From Grok: `From Grok (Site Redesign):` …

Match the other agent’s convention when relaying to Andrew.
