# Coperni PDP LOCKED — Andrew confirmed 2026-09-14

**Branch:** `finish-home-collections`  
**Draft theme:** `187144929571` only (never live `185687998755`)  
**Template:** `shopify-build/templates/product.coperni.json`  
**Editor:** `/admin/themes/187144929571/editor?previewPath=%2Fproducts%2Fbarreletics-x-coperni-closed-sole`

## Confirmed (do not thrash)

| Axis | Locked |
| --- | --- |
| Spine | buy-box → coperni-crosslink → coperni-pdp-story → features → … — **no value-strip** before yellow hero/video |
| Hero | Runway lady still; banner 1200 / shoe_y 100; shoe mat white |
| Mobile | Yellow ~58vh no split shoe; story video → lead → text → 2-up; no hero→video divider |
| Cream | Soft `#faf8f6` only (sock-era match). Rule: `cream-band-LOCKED.mdc` |
| Guarantee head | Display (`h2-display`) — “Built on guarantees, not guesses.” |
| Guarantee columns | Type H3 via `--type-guarantee-column-size` (18–22 / 500) |
| Guarantee CTA | Outline **See details →** → `/pages/help#returns`; text/border `#1c1916` (never white) |
| Video caption | **Coperni 2026 Paris Fashion Week** |
| Home collab pair | Lady/runway first, packshot second |

## Code pins (git)

- Guarantee type + CTA liquid defaults + lock-scan: `9969217` (+ `05a8e9e`, `f4c2ad6`)
- Cream soft lock: `50f40ca`
- Coperni spine/hero letter: `38631bc` / `461193e` (fix-forward only — do not `git restore` whole JSON to “fix” cream)

## Guardrails

- `python3 scripts/lock-scan.py .` before draft push
- Skills: `barreletics-guarantee-band`, `barreletics-cream-band`, `barreletics-no-drift-push-gate`
- Rules: `.cursor/rules/guarantee-band-LOCKED.mdc`, `cream-band-LOCKED.mdc`
- Sitewide: `planning/locks/sitewide.lock.json` → `guarantee_band` + `cream_bands`

## Restore policy

CURRENT MESSAGE wins. Prefer surgical fix-forward over full template checkout. Full restore of older Coperni JSON re-breaks outline CTA colors and can reintroduce value-strip / wrong cream.
