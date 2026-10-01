# Token guide (plain English) — Andrew

You are **not** doing it wrong by having many bots. Each bot = one coworker. **Keep all of them.**

## What ate $25 in 15 minutes

Grok (and similar) charges like this: **every message sends the whole conversation so far back to the model.**

- Short thread = cheap message.
- Long thread = every message is expensive.
- Pasting a huge Cursor report into Grok = one giant expensive message.
- One bot doing Site Design **and** re-explaining architecture **and** re-scanning the repo every turn = burn.

**This is not “too many bots.” It is “one conversation got huge” or “too much pasted in one go.”**

## Do I hide all the current bots?

**No.**

| Action | What it does | Saves tokens? |
|--------|----------------|---------------|
| **Hide from sidebar** | Tidies the list. Chat still exists. | **No** — only if you **stop messaging that old chat** |
| **Delete chat** | Gone. | **No** for future — only removes clutter |
| **New chat in the SAME bot** | Fresh thread. Same bot, same rules/skills. | **Yes** — this is the main fix |
| **New bot for everything** | Wrong. You’d lose specialty prompts. | **No** |

You do **not** replace 15 bots with 1 bot per day that “knows everything.”

## Where “everything” actually lives

| Memory | Where |
|--------|--------|
| Architecture, theme rules, handoffs | **GitHub** (this repo, `.cursor/rules/`, `.cursor/skills/`, `.cursor/agent-comms/`) |
| Help Scout drafts, Xero, email | **Those products + that bot’s scheduled runs** |
| Today’s task | **The current chat** (throwaway when it gets long) |

**Specialty bots read GitHub when they need context** — they don’t need your month-long chat history.

## Simple rules (do this)

1. **Keep every specialty bot** (Help Scout, Xero, blog, 3PL, Site Redesign, Admin, etc.).
2. **When a chat feels long or slow or pricey → New chat in that same bot.**  
   First message: *“Read `AGENTS.md` and `.cursor/agent-comms/STATUS.md` (and my handoff file if any). Today’s job: …”*
3. **Bots don’t read each other’s chats.** They read **handoff files** in `.cursor/agent-comms/` (5–15 lines).
4. **Scheduled runs** (3× Help Scout, etc.): use a **fixed short prompt** every time — “process since last run, write log, don’t recap old chats.”
5. **Site work while go-live:** **Cursor** finishes theme gates on draft; **Site Redesign Grok** only when TE/templates need him. Ops bots ignore the theme unless `@site-design` in a handoff.

## Cursor vs Grok automation

- **Grok bots:** great for scheduled Gmail, Help Scout drafts, Xero, campaigns (already connected).
- **Cursor:** theme code, Shopify draft push, PDP image gates, verify storefront — updates `cursor-to-grok.md` so Grok doesn’t re-audit.

You don’t need one tool to do both.

## When Grok comes back online

Paste **only** the block in `GROK-START-HERE.md`.  
Grok reads `cursor-to-grok.md` + `GROK-TOKEN-RULES.md` — **no full-repo rescan**, no asking Andrew to paste Cursor essays.

## Admin bot (optional habit)

Once a day or when something big lands: update `STATUS.md` (10 lines max). Every bot can start from that.
