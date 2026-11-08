# Handoff to Grok — 2026-10-02

From the Cloud Agent setup chat. Read this once. Do not ask Andrew to paste the setup thread.

## How tokens actually get spent

Every Grok message resends the whole conversation. A long Site Redesign thread, or a pasted Cursor report, is the burn. Hiding a chat does not save money. A new chat in the same bot does.

Memory is in git, not in the chat:

- `AGENTS.md`
- `.cursor/agent-comms/STATUS.md`
- `.cursor/agent-comms/GROK-START-HERE.md`
- `.cursor/agent-comms/GROK-TOKEN-RULES.md`
- `.cursor/agent-comms/cursor-to-grok.md`
- this file

## What to do each session

1. Checkout `finish-home-collections` in `barreletics/Barreletics-Design-Review`. That is the site redesign. It is not Barreletics Ops and not a May 22 repo.
2. Read the files above. Do not rescan the theme. Do not re-audit image gates P1–P8.
3. Reply in `grok-to-cursor.md` (short, newest block on top). End with 5 bullets in `log/YYYY-MM-DD.md`.
4. One concern per commit. One change per Andrew message: page, what changes, theme ID.
5. No `shopify theme` command unless Andrew names the theme ID in that same message. Never the live theme.

## Theme

Repo rule `.cursor/rules/shopify-draft-theme-only.mdc` on this branch:

- Draft for visual QA: `187144929571` (M4 Visual QA), store `barreletics.myshopify.com`.
- `187143618851` is marked retired in that rule. Do not use it.
- Do not push `templates/*.json` or `settings_data.json` over Andrew’s Theme Editor edits.

## Where the work stopped

Last Grok theme commit: `e20e1d0` on 2026-09-30 at 5:17 PM ET. Shop Pay installments on the PDP follow the selected variant (`shopify-build/assets/variant-selector.js`). Pushed to draft `187144929571` only.

After that, Cursor (not Grok) did image gates P4–P8 and gallery hotfix `b0d93c5`. Leave the buy-box gallery alone unless Andrew assigns it.

Andrew still has not signed off a hard-refresh of draft PDP thumbs and swatches, and has not made a publish decision.

## Who does what

- Cursor Desktop: Andrew looks at the store and approves one visual change.
- Grok: a named change, written to git, one commit. Do not replay Cursor’s report.
- This setup chat: environment only. It does not continue the redesign. A new Cloud Agent gets Shopify CLI 4.8.3 and the design preview. It does not get the setup transcript, and it opens `main` until you checkout `finish-home-collections`.

## Shopify secret

The setup session could not see a Shopify secret and had no CLI store session. The shop name in the repo is `barreletics.myshopify.com`. In a new agent, confirm the secret’s shop name. Do not print the token.
