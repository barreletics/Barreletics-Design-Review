---
name: barreletics-images
description: >-
  HARD Barreletics image law. LOCKED 2026-09-09. Auto-invoke BEFORE any
  object-fit, object-position, cover, contain, crop, zoom, 92vh, photo-aspect,
  tile_fit, cream pad, or “photo doesn’t fit” work on split-hero, collab-hero,
  fifty-fifty, mosaic, fullbleed, collection-hero, or press-feature. ALSO when
  Andrew says nooooo, too large, padding around the image, or the agent is
  about to change the frame to fix the photo. One pass. Hours-long image
  loops are forbidden.
---

# Barreletics images — LOCKED 2026-09-09

Andrew 2026-09-09: *we have spent hours in this loop. Make a skill so this never happens again.*  
Andrew 2026-09-09: *lock in the photo logic.*

**Law:** The **frame is locked. The photo fills the frame.**  
If the photo looks wrong, move the photo. **Do not rebuild the frame.**

**Open Never slip in chair pose (HARD):** `fit` · scale **100**. Whole photo in the frame. **Never cover.** Open mobile 50/50s match that size (`image_fit_mobile: fit`). `.cursor/rules/chair-pose-yellow-fit.mdc`.

Read this before you write CSS. One pass. Then stop and ask.

Companions: `barreletics-image-in-the-frame` · `barreletics-use-image-in-the-frame-lock` · `barreletics-home-split-hero`  
Rules: `image-in-the-frame.mdc` · `use-image-in-the-frame-lock.mdc` · `barreletics-images.mdc`

## Sense it — STOP

You are in the loop if you think any of these:

- “I’ll change the box so the photo fits”
- “Contain + pad will show the whole image”
- “92vh made it crop, so go back to photo aspect”
- “Photo aspect made it huge, so cap at 400px / 80% / a new vh”
- “TE looks fine so we’re done”
- “While I’m here, also tweak Coperni / INTERNI / mosaic”

**STOP. Ask which pixel is wrong.** Do not invent geometry #4.

## The only recipe

1. **Keep the signed frame** (width % · height · gap). Do not invent a new one.
2. **Fill it:** `object-fit: cover` · `inset: 0` · `width/height: 100%`.
3. **Compose inside it:** TE X/Y/Zoom (or `object-position`) at **1440 full width**.
4. Screenshot **1440** and **390**. One link. Stop.

```
IMAGE GATE
- [ ] Named the section + the frame (selector + current width/height)
- [ ] I will NOT change that frame
- [ ] Photo = cover, fills the frame
- [ ] Crop = X/Y/Zoom only, verified at 1440 (not TE sidebar)
- [ ] No contain, no cream/pink pad, no 400px cap, no new vh
- [ ] One surface. Then STOP.
```

## Frame vs photo (memorize)

| If you see | You do | You do not |
|---|---|---|
| Photo chopped | X/Y/Zoom inside the **same** box | New height, new aspect, contain |
| Photo too big (section too tall) | Andrew already locked height — restore **that** height | Guess 110% / photo-aspect / 400px |
| Cream/white mats around a tile | Cover the **existing** tile | `contain` in a square (that IS the mat) |
| “Doesn’t fit the frame” | Fill the frame with cover + crop | Resize the frame to the photo |
| TE looks good, storefront doesn’t | Compose at **1440** | contain + studio fill |

**TE sidebar is a lie.** Narrow pane ≠ full desktop under `cover`. Never approve from TE.

## Home hero (Stef) — LOCKED 2026-09-09

- Split **62/38**
- Desktop frame **92vh**
- Trust **left**
- Photo **fills the 92vh frame** (`cover` · `inset: 0`)
- Crop **50 / 22** desktop + phone (`image_pos_x: 50`, `image_pos_y: 22`, zoom **100**)
- **Forbidden:** delete 92vh to “fit” Stef · Section height 110 · photo-aspect ~1022px · crop 0/59

## Coperni pair — LOCKED 2026-09-09

- Under the runway. **80%** · two **equal squares** · **cover** · **16px** gap
- **No cream mats**
- **Forbidden:** contain (cream boxes) · natural-height blow-up · 400px cap

## Forbidden (sitewide)

- `object-fit: contain` + pink/cream/studio fill (rejected 2026-08-31)
- Changing frame to fix crop (92vh ↔ photo-aspect ↔ 110% ↔ 400px)
- `git restore` of image CSS without **restore X**
- Pushing `index.json` to change a photo when CSS/X/Y would do
- Two image surfaces in one turn

## After one pass

Preview link. **Approved** or what pixel is wrong.  
No fourth geometry without a new letter.
