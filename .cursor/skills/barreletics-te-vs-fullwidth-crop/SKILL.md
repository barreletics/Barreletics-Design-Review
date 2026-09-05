---
name: barreletics-te-vs-fullwidth-crop
description: >-
  HARD gate for Barreletics Home split-hero crop. Theme Editor sidebar preview
  is narrower than full desktop — object-fit cover crops differently. Auto-invoke
  BEFORE any split-hero / hero crop / object-fit / object-position / zoom change,
  and BEFORE claiming a hero photo “fits” or sending a preview link for crop QA.
  Current approved hero is cover + scale zoom — NEVER contain + studio fill.
---

# TE vs full-width crop — FAIL CLOSED

Companion rule: `.cursor/rules/te-sidebar-crop-lies.mdc`

## Sense it — STOP

You are about to fail if you:

- Judge hero crop from Theme Editor with the left settings sidebar open
- Reintroduce **`object-fit: contain`** + studio fill / pink pad (rejected)
- Tell Andrew it’s fixed after one TE glance
- Re-enter the contain ↔ cover ↔ pad ↔ cream-gap loop

## Root cause (memorize)

Portrait photo + `object-fit: cover` + media box whose **width changes with viewport** =

- **Narrow (TE sidebar)** → box closer to portrait → more of figure visible
- **Wide (full desktop)** → box more landscape → cover crops harder

That is why Andrew’s screenshots disagree. Not a Shopify bug. Not “needs contain + pink fill.”

**Approved response:** keep cover. Compose with X/Y/Zoom at **full desktop**. Do not pad the photo.

## Mandatory gate (copy into turn before hero crop work)

```
TE↔FULLWIDTH CROP GATE
- [ ] I will NOT approve crop from TE-sidebar-narrow alone
- [ ] I will NOT reintroduce object-fit: contain, studio fill, or pink/cream pad bands
- [ ] Current hero = cover + object-position X/Y + scale() zoom min 1
- [ ] I verified BOTH ≥1280–1440 full width AND ~900 narrow
- [ ] Only then send preview link
```

## Current approved Home split-hero (2026-09-01)

Files: `shopify-build/assets/split-hero.css` · `shopify-build/sections/split-hero.liquid`

1. Grid column stays layout % (e.g. **62/38**). Height = photo aspect × Section height slider.
2. Image **`object-fit: cover`**, `inset: 0`, 100% × 100%. **No contain. No fill bands.**
3. X/Y = `object-position` + `transform-origin` (TE Image Position X / Y).
4. Zoom = `scale(max(1, zoom))`. Liquid `at_least: 100` — TE below 100 stays fill (no gaps).
5. One Corner radius clips photo + text. Text panel background shades the **copy column only**.
6. Media `background: transparent`. Do not add `media_fill_color` / studio fill.
7. Dual-width verify before link. Crops will differ; compose at 1440, don’t “fix” with contain.

**Forbidden “fix”:** `object-fit: contain` + column/studio fill matching the photo pink. Rejected. Do not restore it from older freeze rows.

## Forbidden thrash list

- contain + pink pad (already burned Andrew; rejected 2026-08-31)
- cream/white gaps from shrinking the img box or zoom &lt; 1
- left-shifted grid that breaks mosaic alignment (unless Andrew asks)
- merging `split-hero` into `fifty-fifty`
- `git restore` of hero without restore letter — anti-revert still wins

## Verify commands (before link)

Storefront preview cookie jar → open home → CDP or screenshot at **1440** and **900** width. Then link.
