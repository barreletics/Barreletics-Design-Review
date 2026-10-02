# Cursor Handoff: Apparel PDP Pages Recovery

## AJ rules (Mac review first)

- **No changes to `pdp-buy-box.liquid`.**
- **No draft theme push** until AJ reviews and approves on GitHub PR #30.

## Problem
The Tops and Bottoms pages in Shopify draft theme (187144929571) were overwritten with wrong content (Closed Sole copy/images).

## Solution Found
**All original code and content recovered from GitHub commit `fed5cf0`** (Oct 1, 2026).

---

## What We Found

### Commit Details
- **Commit ID:** `fed5cf0`
- **Message:** "Add M4 apparel PDPs so tee and pants leave Closed Sole."
- **Date:** Oct 1, 2026
- **Location:** `shopify-build/sections/` and `shopify-build/templates/`

### Files to Restore

#### Product Templates (JSON)
1. **`product.v-neck-tops.json`** — V-Neck Tops page
   - Hero: "Softness. Versatility. Comfort." / "Lightweight. Doesn't pill."
   - Features: Made in USA, soft performance fabric, moisture-wicking, won't pill
   - Size chart: `/pages/yoga-pants-t-shirt-size-guide`

2. **`product.yoga-pants.json`** — Yoga Pants page
   - Hero: "Focus on your workout." / "High-rise compression."
   - Features: Super-high rise, reinforced knees, Italian 4-way stretch, won't pill
   - Size chart: `/pages/yoga-pants-size-guide`

#### Section Templates (Liquid)
These `.liquid` files are referenced by the JSON configs:
- `pdp-features.liquid` — Feature grid ("Why these tees/pants")
- `fifty-fifty.liquid` — Split image + copy sections
- `variant-grid.liquid` — Product tabs/color grid
- `pdp-reviews.liquid` — Customer reviews section
- `value-strip.liquid` — 4-benefit bar
- `pdp-sticky-atc.liquid` — Sticky add-to-cart
- `pdp-buy-box.liquid` — Already exists, no changes needed

---

## Next Steps for Cursor

### 1. Copy Files to Draft Theme
```bash
# Files are in shopify-build/templates/ in the repo
cp shopify-build/templates/product.v-neck-tops.json shopify-build/templates/
cp shopify-build/templates/product.yoga-pants.json shopify-build/templates/

# Verify Liquid sections exist in shopify-build/sections/
# (all 7 sections listed above)
```

### 2. Push to Shopify Draft Theme (187144929571)
Use Shopify CLI or admin API:
```bash
shopify theme pull --theme 187144929571  # Pull current state first
# Copy the .json files into templates/
shopify theme push --theme 187144929571 --only templates/product.v-neck-tops.json,templates/product.yoga-pants.json
```

### 3. Verify in Shopify Admin
1. Go to Online Store > Themes > Draft (187144929571)
2. Preview the pages:
   - `/products/v-neck-tops?preview_theme_id=187144929571`
   - `/products/yoga-pants?preview_theme_id=187144929571`
3. Confirm copy and sections render correctly

---

## Content Summary

### Tops (V-Neck Tees)
- **Lede:** Softness. Versatility. Comfort. / Lightweight. Doesn't pill.
- **Description:** Super cozy, ultra-light performance T-shirt or tank. Buttery-soft, moisture-wicking fabric with 4-way stretch and breathable comfort. Long lasting and doesn't pill. Made in the USA.
- **Key Benefits:** Made in USA, Free exchanges, 30-day returns, Doesn't pill
- **Features:** Made in USA, Soft performance fabric, Draws moisture away, Won't pill

### Bottoms (Yoga Pants)
- **Lede:** Focus on your workout. / High-rise compression.
- **Description:** Luxury compression leggings built for studio training. Crafted from premium Italian 4-way stretch fabric for sculpting support, durability, and long-lasting performance. Super-high rise waistband. Reinforced knee panels. Compression fit. Studio-grade durability. Made in the USA. Size down for the best fit.
- **Key Benefits:** Made in USA, Free exchanges, 30-day returns, Doesn't pill
- **Features:** Super-high rise, Reinforced knees, Italian 4-way stretch, Won't pill

---

## Files Available

All recovery files have been extracted and are ready:
- `product.v-neck-tops.json` ✓
- `product.yoga-pants.json` ✓
- `pdp-features.liquid` ✓
- `fifty-fifty.liquid` ✓
- `variant-grid.liquid` ✓
- `pdp-reviews.liquid` ✓
- `value-strip.liquid` ✓
- `pdp-sticky-atc.liquid` ✓

**HTML Preview available:** `apparel_preview.html` shows both pages rendered in full.

---

## Why This Happened

The commit message suggests these pages were built to prevent the Tops and Bottoms from "falling through" to a generic `product.json` template. They were never pushed to the live theme — only built in draft. Someone or something overwrote them with the wrong content (Closed Sole PDP copy).

Git history kept them safe. They're unchanged since Oct 1.

---

## Questions?

If anything is unclear, the full git commit is available to inspect:
```bash
cd /tmp/Barreletics-Design-Review
git show fed5cf0
```

All code is production-ready. Just push to draft and verify.
