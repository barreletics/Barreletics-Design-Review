# Design System Audit & Homepage Alignment

**Date:** 2026-07-29  
**QA theme:** `187144929571` (M4 Visual QA) — unpublished  
**Authority:** Home WORKING · BZ-020 · Collection v18 / SEO v36 type OS  

---

## Files changed

| File | Change |
|------|--------|
| `shopify-build/assets/design-tokens.css` | Full type-role + stack + hero measure tokens |
| `shopify-build/assets/barreletics-base.css` | Role utilities; CTA brand button; quieter type |
| `shopify-build/assets/chrome.css` | Nav/announce match WORKING (11/500, brand 14/700) |
| `shopify-build/assets/split-hero.css` | Token-only; no local type scale / font overrides |
| `shopify-build/sections/split-hero.liquid` | Removed font_picker/size/color TE overrides |

---

## Sections / pages affected

- **Global:** every template via tokens + base + chrome  
- **Homepage:** `split-hero` (wired on `index.json`)  
- **Collection / PDP:** inherit new tokens/base (not yet section-by-section mock pass)

---

## Visual mismatches corrected

| Issue | Before | After (WORKING) |
|-------|--------|-----------------|
| Nav weight | 12px / 600 | 11px / 500 / 0.12em |
| Brand mark | 15px | 14px / 700 / 0.16em |
| Hero body (“secondary”) | TE font_picker → often heavier | Forced **400** / 17px lede token |
| Hero title | Local clamps + picker | `--type-opening-*` only |
| Marketing stars | Gold / TE color | `--accent-stars-marketing` rust |
| CTA type | Mixed 13px | 12px / 700 / 0.1em |
| Button radius | 6px | 4px (WORKING) |
| Stack rhythm | Arbitrary | `--stack-*` tokens |
| TE type knobs | Fought the mock | Removed — system owns type |

---

## QA links

- **Desktop / mobile preview:** https://barreletics.myshopify.com?preview_theme_id=187144929571  
- **Theme Editor:** https://admin.shopify.com/store/barreletics/themes/187144929571/editor  

Hard-refresh. Check hero headline + lede weight, nav quietness, CTA.

---

## Decisions needing approval

1. **Marketing stars = rust** (`--accent-stars-marketing`); review widgets stay **gold** (`--accent-stars`). OK?  
2. **No per-section font/size TE controls** on split-hero — type is global only. OK?  
3. **Collection / PDP deep mock alignment** — next after you sign off homepage type, or wait?

---

## Not done yet (per order)

- Full Collection v18 / PDP v16 section-by-section alignment  
- Screenshot comparison pack  
- Freeze split-hero (await visual OK)
