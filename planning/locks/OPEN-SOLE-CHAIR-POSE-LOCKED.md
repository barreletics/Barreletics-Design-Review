# Open Sole — Chair Pose yellow LOCKED

**Confirmed:** 2026-09-10 · re-confirmed 2026-09-14 (Andrew)  
**Branch tip at lock:** `e071777` on `finish-home-collections`  
**Draft theme only:** `187144929571`  
**Product:** `/products/studio-performance-skin-footwear`  
**Editor:** `/admin/themes/187144929571/editor?previewPath=%2Fproducts%2Fstudio-performance-skin-footwear`

## What is locked

Section: `fifty-fifty-lifestyle`  
Heading: **Never slip in chair pose**  
Templates: `shopify-build/templates/product.open-sole.json` · `product.in-studio-template.json`

| Control | Value |
| --- | --- |
| `image` | `shopify://shop_images/P5A4949.jpg` |
| CDN | `https://cdn.shopify.com/s/files/1/0045/0612/4391/files/P5A4949.jpg` (2100×1400 landscape) |
| `media_fit` | **cover** |
| `image_fit_mobile` | **cover** |
| `image_scale` | **100** |
| `min_height` | **560** |
| `mobile_media_height` | **360** (landscape exception — not 550) |
| `text_pad_top_mobile` | **96** |
| `text_pad_bottom_mobile` | **96** |

## Forbidden (the thrash loop)

- `fit` / `contain` on this heading
- `P5A4943` or yellow-pad experiment assets
- `image_scale` &gt; 100
- Collapsing desktop `min_height` 560
- Changing *other* Open Sole 50/50s to “match” Chair Pose

```
❌ P5A4943 + FIT → “fix” → cover thrash
✅ P5A4949 · COVER · 100 · mmh 360 · leave it
```

## Guardrails in this repo (always refer here)

| Layer | Path |
| --- | --- |
| Letter (this file) | `planning/locks/OPEN-SOLE-CHAIR-POSE-LOCKED.md` |
| Machine lock | `planning/locks/sitewide.lock.json` → `chair_pose_open` |
| Scanner | `scripts/lock-scan.py` (fails if image/fit/mmh/pads drift) |
| Cursor rule (alwaysApply) | `.cursor/rules/chair-pose-yellow-fit.mdc` |
| Cursor rule (must-read) | `.cursor/rules/use-chair-pose-yellow-lock.mdc` |
| Cursor skills | `.cursor/skills/barreletics-chair-pose-yellow-fit/` · `barreletics-use-chair-pose-yellow-lock/` |
| Related | `.cursor/rules/image-in-the-frame.mdc` · `barreletics-images.mdc` · `heading-is-the-target.mdc` |

## Before any Open Sole / yellow / cover / fit change

1. Read this letter + `chair-pose-yellow-fit.mdc`
2. `python3 scripts/lock-scan.py . templates/product.open-sole.json`
3. Pull-verify draft TE after push — picker image must stay `P5A4949`
4. Fix-forward only — do not full-restore older Open Sole JSON to “fix” this block

## Restore recipe (surgical)

Set only `fifty-fifty-lifestyle` settings to the table above on both Open templates. Push those JSON files to draft `187144929571`. Do not touch live theme.
