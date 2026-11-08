
# Shopify theme

> Big picture: [docs/bots/LANES.md](../LANES.md)

- **Operating standard (2026-10-16):** [OPERATING-STANDARD.md](../OPERATING-STANDARD.md)

## HARD RULE (Andrew, 2026-10-16)

**Never touch, edit, or change the LIVE theme without Andrew's explicit go-ahead first.** Test every update on the **draft** theme before anything is released to live.

- **Theme IDs, roles and the current draft live ONLY in [`docs/bots/THEMES.md`](../THEMES.md).** Read it before any theme work; it wins over anything here. For the current LIVE, DRAFT and rollback, read THEMES.md; do not restate them here.

Authoritative lines: [DECISIONS.md](DECISIONS.md).

Barreletics storefront theme only. Workspace is the Design Review theme repo, not this repo and not `~/barreletics-ops`.

## Owner

- Site Redesign · Director `f98d3d1b` retired 2026-10-23 (last message 2026-09-15).
- Current (live) bot: **Website `247649ea-81e5-4d92-a90c-eeb6f8b13e73`** (per `docs/bots/ROSTER.md`; replaced `6247c85a`, retired, which replaced `f1b1afce` and `25c9f763`) (handoff [`handoffs/2026-10-23-website-refresh.md`](handoffs/2026-10-23-website-refresh.md)). Retired: `b1d7deda` ([audit](RETIREMENT-AUDIT-b1d7deda-2026-10-20.md)) and older Website / Site Redesign bots; see HISTORY.md and `transcripts/`.
- Routines with full prompts: [handoffs/2026-10-23-website-refresh.md](handoffs/2026-10-23-website-refresh.md) (current; [routines.md](routines.md) is the stale Oct 20 copy).

## Current truth

- Store: `barreletics`.
- **Theme state:** read [`docs/bots/THEMES.md`](../THEMES.md). SAFETY HOLD (2026-10-25 11:58 PM ET, reaffirmed 2026-10-26) **scoped 2026-11-08:** Andrew named **DRAFT row** (Nov 08 · Cart + bundles) for cart/bundle rotation work — **that row only**; **no LIVE row** edits, **no publish**, **no test orders**, **no** store-wide discount/price changes without separate goes. Former **DRAFT row** (Oct 26 · Work here) is not the work target.
- Store was at 18 themes after Andrew's cleanup (count may have changed; check Admin).
- Local `shopify-build/` and Design Review repo: draft work only. Live theme on disk is reference only.
- Push via Mac b9c0e142 Shopify CLI: fresh pull, backup, minimal diff, `push --only --nodelete`, md5 verify, **draft only** unless Andrew approves live.
- Retail free shipping at $150+; shipping $9.95 otherwise.

## Open items (updated 2026-10-24)

- **Updated 2026-10-28:** Tidio app embed ON on live and draft; it is per theme, re-enable after any publish of a different theme (settings_data.json pushes can wipe it). Judge.me reviews tab OFF on live; draft tab broken pending Andrew's direct go on a CSS workaround (DECISIONS.md 2026-10-27). Mobile has no Judge.me tab by Judge.me design (<768px).
- **Updated 2026-10-30:** PDP color-sync fix ready locally, awaiting Andrew's own go for a draft push; 8 uncertain test gift cards awaiting Andrew's call; Judge.me draft tab fix awaiting go.

- **Go-live — awaiting Andrew:** SEO admin-field fixes; Change B visual OK; third-party script trim (**Clarity** stays); White metafield clear + Deep Teal L QC Hold; Shop Pay/Apple Pay tests then gift card [card redacted] cleanup. DECISIONS rollup line.
- **Pueblo / #D663:** no Shopify B2B; Papa Grok rebuilding Kristyn's order — do not touch company, customer, or #D663. Guard [`b2b-guard.py`](b2b-guard.py) alert-only.
- **Rules (2026-10-23):** same-session GitHub commits; Papa Grok on cross-lane; no customer sends unapproved; Help Scout bot `e6809db5` for email drafts.
- Optional: deactivate test gift cards ending [card redacted] / [card redacted] (permanent); gift card [card redacted] active until Andrew finishes wallet tests.
- Size guide **LIVE** (Oct 19, page `113607835939`). Leftovers: hardcoded "Kids' (US)" header, Fit tips listing sizes. [README](size-guide-2026-10-19/README.md).
- Reviewer outreach: 7 sent Oct 19. Unsent drafts: #1033 Angela (no send tag, size undecided), #1034, #1043 (still says "really long time"), #1044, #1045, #1046. Lynn #1024 wants a gift card plus link (Canada). Phase two (10 reviewers) due Oct 23. [Details](../communications/review-outreach/review-save-2026-10/).
- Rebecca (Bex Burton) reply draft waiting on Andrew; Judge.me #5832 / refund Flow unchecked; test order **#5995** unfulfilled (Andrew only). [review-save-2026-10](../communications/review-outreach/review-save-2026-10/).
- Water Shoes off Google & YouTube since Oct 16. Rethink reminder Oct 25.
- Unclear: internal note to Andrew & Stefanie scheduled Oct 22; outreach schedules stopped Oct 19. Confirm with Andrew.

- Calcurates draft reply to Nik Pasholok — funnel lane owns Calcurates.
- From 10-09: Coperni rating; gift-card test orders; continue-selling variants. Large size range undecided.
- Mac branch `cursor/apparel-pdps-c982` uncommitted.

## Do not

- Edit the live theme without Andrew's explicit go-ahead.
- Use or reference any theme not listed in THEMES.md.
- Do theme work inside Alternate-projects or barreletics-ops.
- Push from Design-Review `main` (behind draft) or whole `templates/index.json`.
- Regress past baseline `2026-10-08-1445-BASELINE-post-launch`.

## Publish record (2026-10-25 10:59 PM ET)

- The Website bot published the theme listed as LIVE in THEMES.md at Andrew's explicit go; the previous live theme (rollback in THEMES.md) was left untouched. IDs: read THEMES.md.
- Cookie banner EU-only admin setting NOT applied (skipped unless Andrew asks). Sticky bar settled.
- Test gift card [card redacted] stays active until Andrew says tests are finished; code is never shared (not in chat, email or GitHub).

## Current truth update (2026-10-30 audit of Website · Ecom 247649ea)
- Oct 27 11:29 AM ET: toggles, cart sentence and FAQ shipping line are LIVE (Andrew's direct go).
- Oct 28 9:13 PM ET (Andrew): no test orders of any kind; live tap-tests stop before checkout; fix on the draft only.
- Open: Closed Sole thumbnail/label fix awaiting Andrew's go to the draft; Tidio key mismatch; Tidio Pro ends Nov 2; real-phone/Instagram test; cart sentence "always show" request.
- Current bot handoff source: handoffs/2026-10-25-website-refresh-2.md (the Owner/Routines pointers above to 2026-10-23 are stale).
- Detail: WEBSITE-ECOM-247649ea-FULL-AUDIT-2026-10-30.md
