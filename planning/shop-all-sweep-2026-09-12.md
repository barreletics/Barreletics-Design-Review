# Shop All formatting sweep — 2026-09-12

**Branch:** `finish-home-collections`  
**Scope:** Liquid/CSS only. No `templates/collection.json` push. Draft theme `187144929571` when Andrew pushes from Mac.

## Changed (this commit)

| Item | File(s) | Fix |
|------|---------|-----|
| Variant grid soft cream | `sections/variant-grid.liquid` | Packshot wells + M/L size chips: `#f5f2ec` / `--bg-alternate` → `var(--bg-alternate-soft, #faf8f6)` |
| Cream striping | `assets/barreletics-base.css` | Adjacent-sibling rule: `.sock-math` wrapper + next `.pdp-reviews` → reviews background white (overrides TE `#faf8f6` inline on Shop All) |
| Duplicate section id | `sections/collection-hero.liquid` | Removed inner `id="shopify-section-{{ section.id }}"` — Shopify theme wrapper already emits that id; duplicate broke DOM / anchors |

## Remaining — Andrew / TE (not in this commit)

| Surface | Issue | Contenders / action |
|---------|-------|---------------------|
| **Collection hero** | `Screenshot_2026-04-25_at_9.52.43_AM.png` — geometry/crop fail | TE pick one: `IMG_2917`, `barreletixxstefrunningpinkbackground`, `te-pick-ig-real-green-court`, `P5A4949*` |
| **fifty-fifty-grip** | Current `IMG_2704.jpg` — grip block media QC | Andrew to shortlist replacement; TE only (no JSON push from agent) |
| **Reviews bg** | TE still `#faf8f6` on `reviews` block | CSS striping handles sock-math → reviews; optional TE set Background → white for clarity |
| **Deploy** | Liquid not on M4 until push | `shopify theme push --theme 187144929571` — Mac/auth per prior sessions |

## Verify after push

- Shop All: `/collections/barre-pilates-yoga-shoe-sock-footwear?preview_theme_id=187144929571`
- Variant card wells + size chips = soft cream `#faf8f6`
- One pair. Done. → Real people = cream then **white** (no double-cream band)
- DOM: single `#shopify-section-*` per section (no duplicate on collection-hero)
