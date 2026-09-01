---
name: barreletics-te-vs-fullwidth-crop
description: >-
  HARD gate for Barreletics hero/media crop. Theme Editor sidebar preview is
  narrower than full desktop — object-fit cover in a width-fluid column shows
  full figure in TE and legs-only or cut feet at full width. Auto-invoke BEFORE
  any split-hero / hero crop / object-fit / object-position / media-frame change,
  and BEFORE claiming a hero photo “fits” or sending a preview link for crop QA.
---

# TE vs full-width crop — FAIL CLOSED

Companion rule: `.cursor/rules/te-sidebar-crop-lies.mdc`

## Sense it — STOP

You are about to fail if you:

- Judge hero crop from Theme Editor with the left settings sidebar open
- “Fix” by only nudging `object-position` / focal while media still `cover`s a **full-width fluid** column
- Tell Andrew it’s fixed after one TE glance
- Re-enter the contain ↔ cover ↔ pad ↔ cream-gap loop without dual-width proof

## Root cause (memorize)

Portrait photo + `object-fit: cover` + media box whose **width changes with viewport** =

- **Narrow (TE sidebar)** → box closer to portrait → more of figure visible
- **Wide (full desktop)** → box more landscape → cover crops harder → head gone / wrong feet

That is why Andrew’s screenshots disagree. Not a Shopify bug. Not “needs one more focal tweak.”

## Mandatory gate (copy into turn before hero crop work)

```
TE↔FULLWIDTH CROP GATE
- [ ] I will NOT approve crop from TE-sidebar-narrow alone
- [ ] Fix uses portrait-locked inner frame (or equivalent stable aspect) — not fluid full-column cover
- [ ] Studio fill color matches photo bg (no cream/white gap)
- [ ] I verified BOTH ≥1280–1440 full width AND ~900 narrow — same figure (head + feet)
- [ ] Only then send preview link
```

## Correct Home split-hero pattern

Files: `shopify-build/assets/split-hero.css` · `shopify-build/sections/split-hero.liquid`

1. Grid column stays e.g. **62/38** (layout)
2. Media column `background` = **studio fill** matching photo (`media_fill_color`)
3. Image **`object-fit: contain`** + `object-position: center` so head + feet stay visible at every width
4. Side fill = photo pink continuing — not cream/white. If strips show, fill color is wrong — sample photo corners
5. Dual-width verify (≥1440 and ~900) before link — same full figure both

**Forbidden “fix”:** width-fluid `object-fit: cover` on this portrait hero (TE will lie again).

## Forbidden thrash list

- contain + pink pad as the only “fix” without explaining TE lie (already burned Andrew)
- cream gap from portrait frame inside column without fill color
- left-shifted grid that breaks mosaic alignment (unless Andrew asks)
- `git restore` of hero to “old version that was right” without restore letter — anti-revert still wins

## Verify commands (before link)

Storefront preview cookie jar → open home → CDP or screenshot at **1440** and **900** width. Same crop. Then link.
