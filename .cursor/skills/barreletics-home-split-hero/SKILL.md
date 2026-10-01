---
name: barreletics-home-split-hero
description: >-
  HARD lock for Barreletics Home split-hero (Stef pink run). LOCKED 2026-09-09.
  Auto-invoke BEFORE any edit to split-hero.liquid, split-hero.css, or
  index.json split_hero. ALSO when Andrew says the hero is too big, photo
  doesn’t fit, trust is centered, nooooo, restore the hero, or the agent wants
  to set 92vh / contain / photo-aspect / 110%. One pass. Never a 10-try loop.
---

# Home split-hero — LOCKED 2026-09-09

Andrew 2026-09-09: *we are not doing one task that takes ten attempts.*  
Andrew 2026-09-09: *lock in the photo logic* · *lock in the home page.*

If you are about to “try another geometry,” **STOP. Read this. Do the recipe once. Then ask.**

**Parent image law:** `barreletics-images` (always-on). This skill is the Home hero row of that law.  
Companion: `barreletics-te-vs-fullwidth-crop` · `barreletics-anti-revert`  
Rule: `.cursor/rules/home-split-hero.mdc` · `.cursor/rules/barreletics-images.mdc`

**This section only.** Not Coperni. Not INTERNI. Not Collection hero. Not mosaic.

## What is LOCKED (do not re-litigate)

| Piece | Locked | Do not |
|---|---|---|
| Split | **62/38** | 59/41 |
| Section size | **92vh** desktop frame | Photo-aspect ~1022px / Section height 110 |
| Trust | **Left** with the H1 | `justify-content: center` + `width: 100%` |
| Photo | **Fills the 92vh frame.** `cover` · `inset: 0` · 100%×100% | Change the **box** to “fix” the crop |
| Crop | **50 / 22** desktop + phone · zoom **100** | 0/59 · contain + pink pad |
| Copy | Left · white column | Center desktop copy |

**If the photo doesn’t fit the frame:** move **X/Y/Zoom only**.  
**Never** grow/shrink the frame (no photo-aspect undo, no 110, no new vh).

## The 10-try graveyard (do not repeat)

1. Push Home JSON → drifted split to **59**
2. Center desktop **trust**
3. Section height **110** / photo-aspect box → hero **too large**
4. Force **92vh** then he said size/trust good, **photo not**
5. Agent “fixed” photo by **removing 92vh** and going back to photo-aspect → **nooooo**
6. contain + studio/pink fill (2026-08-31, rejected)
7. Judging crop from **TE sidebar** (narrow ≠ 1440)

## Recipe (one pass)

```
HOME SPLIT-HERO GATE
- [ ] Home split-hero ONLY
- [ ] Keep 62/38
- [ ] Keep desktop frame 92vh (do not delete it)
- [ ] Keep trust left
- [ ] Photo = cover, fills the 92vh box
- [ ] Crop stays 50 / 22 unless Andrew names a new pixel
- [ ] I will NOT set contain, pink pad, or photo-aspect height
- [ ] Screenshot 1440 + 390. One link. Then STOP.
```

CSS shape:

```
.split-hero { min-height: 92vh; }
.split-hero__media {
  height: 92vh;
  min-height: 92vh;
  max-height: 92vh;
  aspect-ratio: auto;
}
.split-hero__media img { object-fit: cover; inset: 0; width: 100%; height: 100%; }
.split-hero__trust { justify-content: flex-start; width: auto; text-align: left; }
```

Locked crop: **center / 22%** (`image_pos_x: 50`, `image_pos_y: 22`) desktop + mobile. Verify at 1440 before linking.

## Files you may touch

- `shopify-build/assets/split-hero.css`
- `shopify-build/sections/split-hero.liquid` (only if a CSS var is required)
- `templates/index.json` → **`split_hero` keys only** after a pull. Never Coperni / INTERNI in the same push.

## Files you must not touch

`collab-hero` · Coperni tiles · `press-feature` · mosaic · buy-box · juicer

## After one pass

Link. Ask **approved** or what’s wrong.  
If he says no: **ASK what pixel is wrong.** Do not invent a fourth geometry.
