# BOOT: run this at the start of EVERY task (Papa Grok, every director, every lane bot)

> STEP 0 (2026-11-04, before anything else): Read Ground Zero. Repos are private, so the URL needs GitHub login; bots without login read it with the GitHub connector: get_file_contents owner=barreletics repo=barreletics-ops path=BR-Social-Hub/GROUND-ZERO-ALL-BOTS.md ref=main. URL (logged-in only): https://raw.githubusercontent.com/barreletics/barreletics-ops/main/BR-Social-Hub/GROUND-ZERO-ALL-BOTS.md

> STEP 0b: Before giving Andrew any step-by-step instructions, read the instructions-for-andrew skill (connector path owner=barreletics repo=barreletics-ops path=.cursor/skills/barreletics-instructions-for-andrew/SKILL.md ref=main) and follow it: numbered steps, direct links.

> FIRST: links in [LINKS.md](LINKS.md).

This is the ONLY load order. INDEX.md and OPERATING-STANDARD.md point here. Who owns what: ROSTER.md. Theme IDs: THEMES.md. Live status board (built / open / owner): STATUS.md, read right after THEMES.md.

0. RULE ZERO (save as you go): every durable decision, sent email, changed fact, new rule or open item gets a dated line in your lane `DECISIONS.md` AND the shared `docs/bots/DECISIONS.md`, pushed to main and read back from main in the same session, never batched. Before any chat refresh, retirement or end of a long task, run the save and report the commit SHA. When Andrew says "save all" (or "Papa Grok: save all"), every bot runs `docs/bots/SAVE-ALL.md`.
1. Read `docs/bots/THEMES.md` for the current DRAFT before any store or theme talk. If THEMES.md lists DRAFT as "none", no push. Only Website changes themes, and only on the DRAFT named in THEMES.md. Never publish without Andrew's go naming the theme ID.
   STANDING RULE (Andrew, 2026-10-26 5:26 PM ET, on a call, no exceptions): the Website bot (Website · Ecom) ALWAYS asks Andrew directly for any theme approval or go-live decision, and nothing goes live unless Website asked him directly and he said go (naming the theme ID per THEMES.md). Papa Grok and every other bot never relay or request theme approvals; Papa Grok relays everything else. Agreed: Website asks directly. Replaces: any earlier approach where theme approvals could be relayed through Papa Grok or Email Templates.
   If a lane HOME declares a SAFETY HOLD, no theme push until Andrew's go naming a theme ID; otherwise theme work is Website bot only, only on the DRAFT in THEMES.md.
2. Read `RULES.md`, then your lane `HOME.md` and `DECISIONS.md` (newest dated line wins; the "Read map by bot" table in `LANE-MAP.md` names your exact folders; there is no docs/bots/ops/ folder). If the task touches ads, social, the paid dashboard or bc- agents, also read `docs/bots/SOCIAL-PAID-ARCHITECTURE-POINTER.md`. HISTORY.md only for "when/why"; transcripts only for provenance, never at startup. Unsure of your lane or owner: `ROSTER.md`.
3. Cite one line from those files, THEMES.md, or a testing doc. If you can't, say `missing` and stop.
   **THEMES.md citations use Role rows only** (`LIVE row`, `DRAFT row`, `Rollback row`, etc.) — never copy a numeric theme ID into chat, TOOL-LOG, DECISIONS, handoffs, or any file except THEMES.md itself. Andrew's go at publish still names the ID from THEMES.md; bots do not duplicate the number elsewhere.
   Read receipt (2026-10-31): log one line in [TOOL-LOG.md](TOOL-LOG.md): `YYYY-MM-DD HH:MM ET | bot | BOOT read | file:line or THEMES.md:<Role> row | main commit` (no numeric theme IDs in this field).
4. One task this turn. No "while I'm here."
5. Two failures on the same step: write a one-sentence blocker and stop (Papa: route or escalate; director: don't re-plan).
   A 'blocked' report must name the exact missing permission or tool and the fastest manual path, sent to the owner at once. The box desktop is one shared screen: if a browser job fails once with 'window not ready' or 'all screens in use', stop retrying, report immediately, and ask the lane owner (LANE-MAP.md) or Papa Grok to do it; do not wait on a stalled desktop job. (This desktop case is the one exception to waiting for two failures.)

Directors: specialists execute; directors relay briefs and verify, and never re-plan.

## Director to specialist brief (template)
**Task:** [one sentence]. **Done when:** [observable result]. **Sources:** read [lane HOME/DECISIONS and/or THEMES.md]; do not use chat memory for theme IDs. **Constraints:** draft-only / no store changes / theme work only by Website, only on the DRAFT in THEMES.md, publish only with Andrew's go naming the ID. **Return:** outcome plus one cited line or "missing". No new plan, no re-draft unless asked.

## Standing rules
- Voice: Dir · Finance uses the 'Regal' voice on calls with Andrew; never 'Leora' (2026-10-29).
- Customer copy (support voice, lifespan, warranty, lost package): read `docs/bots/communications/SUPPORT-VOICE-LIFESPAN-WARRANTY.md` before drafting (2026-10-29).
- Cross-lane citations (2026-10-30): any SendToAgent that asks another bot to act on a cross-lane decision must cite the DECISIONS.md line/commit (or say "committed this session"); a bot that gets one without it asks for the citation before acting. Bot ids come only from `docs/bots/ROSTER.md`.

## Core files (links)
[THEMES.md](THEMES.md) · [STATUS.md](STATUS.md) · [RULES.md](RULES.md) · [ROSTER.md](ROSTER.md) · [LANE-MAP.md](LANE-MAP.md) · [DECISIONS.md](DECISIONS.md) · [SAVE-ALL.md](SAVE-ALL.md) · [REFRESH-RULE.md](REFRESH-RULE.md) · [DRIFT-CHECK.md](DRIFT-CHECK.md) · [ARCHITECTURE.md](ARCHITECTURE.md) · [PORTABLE-ARCHITECTURE.md](PORTABLE-ARCHITECTURE.md) · [SOCIAL-PAID-ARCHITECTURE-POINTER.md](SOCIAL-PAID-ARCHITECTURE-POINTER.md) · [Support voice](communications/SUPPORT-VOICE-LIFESPAN-WARRANTY.md) · [Papa Grok handoff](director/handoffs/PAPA-GROK-HANDOFF-2026-10-30.md) · [Starter kit](../kit/README.md)
