# No-drift process LOCKED — 2026-09-12

Andrew’s time is finite. Never claim a visual match without proof. Never invent when a ruler exists.

## Autopsy — how we drifted (pad / Best Grippy Socks, 2026-09-12)

| # | Failure | What happened | Hard gate now |
|---|---------|---------------|---------------|
| 1 | Skipped scan | Moved hero, pushed, did not run lock-scan first | No push / no “done” without lock-scan |
| 2 | Trusted TE checkbox | `page_open_pad` pushed true, Shopify stripped it on pull | Tokens + Liquid gates only (`section.index` / suffix / `!important`). TE checkbox is optional mirror, never sole gate |
| 3 | Claimed fixed without proof | Said matched before remote verify + measure | Forbidden words (“fixed”, “matched”, “done”) until measure vs ruler |
| 4 | Wrong surface | Public `preview_theme_id` without preview cookie served **old** theme; early reads lied | Prefer Theme Editor link Andrew uses; if storefront preview, confirm redesign chrome (draft bar / “Shop all colors”) before measuring |
| 5 | Invented vs copied | Special-cased SEO instead of copying Shop All ruler | Name ruler first; copy numbers from lock/tokens; no new pad values |
| 6 | Wrong link / wrong noun | Bad page handle; called PDPs “collections” | Correct `previewPath` for the page changed; speak Andrew’s vocab (Open/Closed = PDPs) |
| 7 | Widget thrash | Asked menus after he already answered | Act on clear copy (“full underfoot grip”); one clarifying ask only if still blocked |
| 8 | Multiple false dones | Several “pushed / locked” messages while still 32px | One axis → one proof → one done. Pull-verify after every JSON push |

## Before ANY draft push
1. Name the **ruler** (Shop All or a LOCKED OS / `planning/locks/*.lock.json`).
2. Run `python3 scripts/lock-scan.py` (scoped to the template).
3. Fix every FAIL. Never weaken a lock to pass.
4. Prefer **code locks** (CSS tokens + Liquid) over TE settings for anything visual that must match sitewide.
5. **Pull-verify** after push: `shopify theme pull --only <file>` — confirm the setting/code actually landed.
6. **Measure** vs ruler (computed CSS + screenshot). Same number. If you didn’t measure, you don’t say matched.
7. Push **only** named files to draft `187144929571`. Never live. Never template JSON unless named.
8. Send the **correct** Theme Editor link for the page you changed.

## Say-done checklist (all required)
- [ ] Ruler named
- [ ] lock-scan clean for that template
- [ ] Pull-verify shows code/settings on draft
- [ ] Measured vs ruler (number + screenshot)
- [ ] Correct editor `previewPath`

## Rulers (copy, don’t invent)
| Topic | Ruler |
|-------|--------|
| Grid opens page — under nav | Shop All → `--pad-grid-page-open` 72 / mobile 56 |
| 50/50 mobile pads | PDP lock 96/96 · footprint 560/550 |
| Cream | `#faf8f6` |
| Type | `planning/type-os-LOCKED.md` |
| Shop All spine | `planning/locks/shop-all.lock.json` |
| Hero → cream strip → cream 50/50 | `planning/earmark-hero-value-strip-5050-flow.md` (earmark; apply when Andrew says go) |

## Skills / rules
- [Barreletics no-drift push gate](sand-workflow:barreletics-no-drift-push-gate)
- [Barreletics lock scan](sand-workflow:barreletics-lock-scan)
- `.cursor/rules/no-drift-push-gate.mdc` (alwaysApply)
- `.cursor/rules/grid-page-open-LOCKED.mdc` (alwaysApply)
- `.cursor/rules/barreletics-lock-scan.mdc`
