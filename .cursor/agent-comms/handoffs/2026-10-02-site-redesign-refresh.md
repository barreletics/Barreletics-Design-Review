# Site Redesign bot refresh: handoff (2026-10-02)

Old bot: "Site Redesign" (agent `0b84b5bd-8846-478f-bca4-9faedc5de6a7`). The new bot starts from git. Read this file first, then `GROK-START-HERE.md`, `GROK-TOKEN-RULES.md`, `STATUS.md`, `cursor-to-grok.md`.
Sources: the old bot's box profile, its voice-call notes and its report attachments, plus agent-comms on this branch. Its chat transcript was not readable here. The box held no memory file and no transcript copy, so anything only in that chat is missing.

## Role and lane
- Profile: "Barreletics site redesign: theme, PDP, Home, and day-to-day storefront layout work. Sibling to Site Redesign · QC (draft QC) and Image Editor (asset reframes). Draft theme work and production publishes as Andrew directs. Never confuse this bot's name with the production theme." No title set.
- Owns (when assigned): `templates/*.json` (coordinate before any push), Type OS / headings / hide utilities, `sections/press-row.liquid`, `sections/page-about-facts.liquid`, Admin blog content, `scripts/lock-scan.py`. Fifty-fifty split height is shared work: use `split_media_height_mobile` / `--split-media-h-mobile`, with no hardcoded phone heights.
- Never touches: PDP gates P6–P8 (`pdp-reviews`, `pdp-buy-box`, `media-img`), the buy-box gallery (Cursor, `b0d93c5`), or the exceptions in `barreletics-media.mdc`.

## Repo, branch, theme
- Repo `barreletics/Barreletics-Design-Review`, branch `finish-home-collections` (not Barreletics Ops, not a May 22 repo). `shopify-build/` is the source of truth. Shopify is only for visual QA.
- Draft theme `187144929571` ("Redesign — Latest (M4 QA)", role unpublished) on `barreletics.myshopify.com`. `187143618851` is retired. Live is `185687998755` (Streamline). Never touch live.
- Run no `shopify theme` command unless Andrew names the theme ID in that same message. Never push `templates/*.json` or `settings_data.json` over his Theme Editor edits.

## Standing rules, guardrails, locked decisions
- Before handing Andrew a link, verify the real URL at 390 and 1440. Use `https://barreletics.com/...?preview_theme_id=187144929571`, never myshopify (it drops the preview). Curl for 200 first, and read push output in full.
- Scan each change against the whole page first. If you don't recommend it, say so up front and let him decide (Andrew, 2026-09-28: "I'm weeks behind in launching").
- Banner headings match the 50/50 heading size. One shared heading class on the draft is the global default, and a section can override it (Andrew, 2026-09-28).
- Copy: "Hold every pose." for the shoe pages. The beach banner line stays "Shapa" for now (2026-09-28).
- Copy law: no pool positioning (say resortwear / paddleboarding / beach), and never mention a dishwasher or washing machine. Care wording is "Hand wash with warm soapy water. That's it." Returns copy drops bacteria/antimicrobial/hygiene claims.
- One concern per commit, and one change per Andrew message (page, change, theme ID). Reply only in `grok-to-cursor.md` (short, newest on top). End each session with 5 bullets in `.cursor/agent-comms/log/YYYY-MM-DD.md`.
- Don't re-scan the theme or re-audit P1–P8 / `b0d93c5`. Don't ask Andrew to paste Cursor reports. Start a new chat when a thread gets long.

## Skills (barreletics-* on the box)
These are the site skills on the box. The transcript wasn't readable, so it isn't confirmed which ones this bot used:
home-no-revert-guard, home-qc-self-prompt, no-drift-push-gate, lock-scan, page-layout-os (and -2), 50-50-mobile-ruler, media-fill-50-50, content-page-type, cream-band, guarantee-band, chair-pose-yellow.

## Open items / waiting on Andrew
- Andrew still has to hard-refresh the draft PDP thumbs and swatches after `b0d93c5` and sign off. Then the publish decision is his alone.
- Leave the buy-box gallery alone unless Andrew assigns it.
- Full-bleed heading pass across every banner was parked on 2026-09-28. Andrew reviews it in page context before committing.
- Live Admin edits handed to Andrew: Returns claims guide (2026-09-29, draft already done) and 8 URL-redirect fixes. Not confirmed whether he applied them.
- Draft link audit, 2026-09-30 (62 URLs, 2 broken):
  - `studio-sample-medium-no-charge`: `Liquid error: invalid url input` in the JSON-LD `"image"` field at `pdp-buy-box.liquid` line 590. This is in Cursor's file.
  - No themed 404 on the draft. This branch now has `templates/404.liquid`, but whether the draft has it was not checked.

## Last commits
- Grok `e20e1d0`, 2026-09-30 5:17 PM ET: Shop Pay installments line follows the selected variant (`variant-selector.js`). Pushed to draft only. Before it: `241a2d0` (no sole badge on apparel; Style as buttons) and `cbd1494` (apparel size values).
- Cursor `b0d93c5`, 2026-09-30 8:38 PM ET: PDP gallery thumb clicks plus a sized variant hero swap.

## Routines
None found. The box has no automations for this agent.

## Verification questions (for the new bot)
1. Q: On 2026-09-28, which line did Andrew pick for the shoe pages, and what happened to the beach banner line? A: "Hold every pose." The beach line stays "Shapa" for now.
2. Q: How should banner heading sizes work on the draft? A: Match the 50/50 size through one shared heading class as the global default, which a section can override.
3. Q: In the 2026-09-30 draft link audit, how many URLs were checked and which 2 failed? A: 62. `studio-sample-medium-no-charge` failed with a JSON-LD Liquid error at `pdp-buy-box.liquid` line 590, and there was no themed 404 template.
