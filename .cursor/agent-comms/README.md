# Agent comms (Barreletics)

**Purpose:** Bots talk via git files, not pasted megachats. Institutional knowledge lives in rules/skills/code — not in Grok/Cursor thread history.

## When Grok is back online

Andrew (or Grok’s first turn): **Read `GROK-START-HERE.md` in this folder, then `STRATEGY.md`.** Reply only in `grok-to-cursor.md` unless the task is code in Grok’s lane.

## Files

| File | Who writes | Who reads |
|------|------------|-----------|
| `GROK-START-HERE.md` | Cursor (updated on handoff) | Grok — every **new** Grok session |
| `STRATEGY.md` | Cursor + Andrew | All agents — architecture + token rules |
| `cursor-to-grok.md` | Cursor | Grok |
| `grok-to-cursor.md` | Grok | Cursor |
| `log/YYYY-MM-DD.md` | Any agent | Next session — 5-bullet closeout only |

## Message format (append-only)

```markdown
## YYYY-MM-DD HH:MM — From {Cursor|Grok} — {topic one line}

- Decision / ask:
- Files touched (if any):
- Commit (if any):
- Next owner:
```

No full reports. Link paths; paste ≤10 lines unless Andrew says “full detail.”

## Lanes (do not overlap)

| Lane | Owner | Examples |
|------|--------|----------|
| Site Redesign / Type OS / TE JSON | **Grok** | `templates/*.json`, press-row, Type OS headings, `lock-scan.py` |
| Image foundation / PDP gates / media-img | **Cursor** | P6–P8, snippets, section liquid (except Grok-held) |
| Live publish | **Andrew only** | Explicit “push live” in current message |

Draft theme only unless Andrew approves live in that message: **187144929571** (M4 QA) for pushes from this repo unless Andrew names another approved draft.

## Andrew workflow (minimal tokens)

1. Tell one bot one job.
2. That bot updates `log/` + their `*-to-*.md` file and pushes (or asks Cursor to push).
3. Tell the other bot: “Read `.cursor/agent-comms/cursor-to-grok.md`” (or grok-to-cursor).
4. **New chat** per task on Grok when the thread is long — memory is in repo, not transcript.
