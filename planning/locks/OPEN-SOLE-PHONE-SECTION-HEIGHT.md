# Open Sole phone section height — Sock era is the ruler

**Andrew 2026-10-07:** He was never talking about font size. Phone **section height** on Open Sole. Reference = **The Pilates sock era is over.** (not Never loses, not One pair).

**Draft only:** `187144929571` · never live  
**Template:** `templates/product.in-studio-template.json`  
**Page:** `/products/studio-performance-skin-footwear?preview_theme_id=187144929571`

## Reference at 390 / DPR 3 (before this pass)

| | px |
|---|---|
| Section | **1013** |
| Media | **500** (`mobile_media_height` 0 = global) |
| Text | **513** |

## Match these four to Sock era

| Heading | Section | How |
|---|---|---|
| Barefoot feel. Zero slip. | `fifty-fifty-lifestyle` | `mobile_media_height` **550 → 0** (media 500). `mobile_text_height` **513**. Pads 96/96, P5A4949 cover, focal 50/72 stay. |
| Tired of slipping in your yoga socks? | `fifty-fifty-tired-socks` | media already 500. `mobile_text_height` **513**. |
| Redefine movement. | `fifty-fifty-numbers` | media already 500. `mobile_text_height` **513**. |
| Let us knock your socks off | `knock-socks` | no height setting — `statement-band` phone `min-height: 1013px` on Knock only (`open_knock_join`). Think outside the sock stays auto. |

`mobile_text_height` is honored on `in-studio-template` only (other product templates still zero it). Desktop unchanged. Typography / 96 pads / images stay.

Do **not** retarget Never loses or One pair.
