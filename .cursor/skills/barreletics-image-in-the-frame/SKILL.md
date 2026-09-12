---
name: barreletics-image-in-the-frame
description: >-
  HARD. ALL images. Auto-invoke BEFORE media_fit, image_scale, object-fit,
  cover, fit, contain, crop, zoom, 92vh, 50/50 photos, heroes, mosaic,
  fullbleed, or “photo doesn’t fit.” Locked frame. One recipe. Never flip
  cover/fit/zoom. Never rebuild the box. Never remap to a neighbor.
---

# Image in the frame — ALL images

Andrew 2026-09-09: *a rule for all images where this problem repeats* · *never again*.

## Sense it — STOP

You are in the loop if you:

- Switch cover ↔ fit ↔ zoom to “fix” it
- Change the box so the photo fits
- Pick a neighbor 50/50
- Skip opening `image-in-the-frame.mdc` this turn

## Recipe

Keep the locked frame.

- **Fit inside / don’t crop** → `fit` · **100**
- **Open Never slip in chair pose** → `fit` · **100**. NEVER cover.
- **Fill / image-led 50/50 / Stef / sock era desktop / Coperni** → `cover` · **100** · X/Y only

Do not flip Chair Pose to cover. Do not change other 50/50s to match Chair Pose.

One heading. One pass. Then stop.

## Gate

```
IMAGE-IN-FRAME GATE
- [ ] Opened image-in-the-frame.mdc this turn
- [ ] Exact heading named
- [ ] Frame unchanged
- [ ] One recipe — not a flip
```

Also run `barreletics-use-image-in-the-frame-lock`.
