# PDP 50/50 mobile — LOCKED 2026-09-10

**Source:** Coperni Closed Sole QA (draft `187144929571`) → sitewide PDP standard.  
**Surfaces:** all `product*.json` fifty-fifty sections + `sections/fifty-fifty.liquid` defaults.

## Text (every 50/50 — identical)

| Control | Value |
|---|---|
| `text_pad_top_mobile` | **96** |
| `text_pad_bottom_mobile` | **96** |
| `vertical_padding` (desktop) | **80** |
| `side_padding` | **64** |
| `bg_color` | **`#faf8f6`** |

Do **not** special-case one block’s text pads (that caused Grip drift).

## Media footprint

| Control | Value |
|---|---|
| `min_height` (desktop) | **560** |
| `mobile_media_height` (lifestyle COVER) | **550** |

## Packshot / FIT exception (media only)

When the photo is a **product packshot** (e.g. Coperni purple shoe on Grip isn’t optional):

- `image_fit_mobile`: **fit** (whole shoe visible)
- `media_bg`: same as section bg (`#faf8f6`)
- `mobile_media_height`: **~400** for ~square packshots — so FIT does **not** leave a tall cream letterbox that *looks like* broken text pad
- Top-anchor FIT in Liquid (no cream band above the shoe)
- Do **not** “fix” packshot letterbox by changing text pads
- Trust strip optional — if on, it shifts title vs siblings; prefer off unless Andrew asks

Lifestyle photos stay **COVER** + 550.

## Agent / Cursor rules

- `.cursor/rules/pdp-fifty-fifty-te-controls.mdc` — phone text pad **96/96** (was 104)
- Skill: Barreletics 50/50 mobile ruler
- Liquid defaults in `shopify-build/sections/fifty-fifty.liquid`

## Forbidden

- Hardcoding product text pad to 104
- Thrashing Grip pads while Sock era / Commit stay fixed
- Using COVER on a packshot to “match footprint” when FIT + ~400 frame is the lock
