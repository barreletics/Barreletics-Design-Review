# Frozen Spec — Homepage

---
status: LOCKED
surface: Homepage (`/`)
authority: Andrew 2026-09-09 — lock in the photo logic · lock in the home page
living_spine: `shopify-build/templates/index.json` on M4 `187144929571`
mock_lineage: `docs/Barreletics Home - Definitive-WORKING.html` — never overwrite that HTML
tokens: v49 (palette, type, spacing, components)
updated: 2026-09-09
---

## Photo law (HARD)

**The frame is locked. The photo fills the frame.** If the photo is wrong, move the photo. Do not rebuild the frame.

- Fill: `object-fit: cover` · `inset: 0` · 100% × 100%
- Crop: TE X/Y/Zoom at **1440** — never from Theme Editor sidebar
- Never: contain + cream/pink pad · 92vh ↔ photo-aspect ↔ 110% ↔ 400px

Skills: `barreletics-images` · `barreletics-home-split-hero`  
Rules: `.cursor/rules/barreletics-images.mdc` · `.cursor/rules/home-split-hero.mdc`

## Locked Home split-hero

| Piece | Locked |
|---|---|
| Split | **62/38** |
| Desktop frame | **92vh** |
| Trust | **Left** |
| Photo | Cover, fills the 92vh box |
| Crop | **50 / 22** desktop + phone · zoom **100** |

## Locked Coperni pair

Under the runway: **80%** · two **equal squares** · **cover** · **16px** gap · **no cream mats**.

## Locked spine (M4 `index.json` order)

1. Announcement + header (chrome)
2. **split-hero** — Stef pink run
3. **visual-mosaic**
4. **disciplines**
5. **variant-grid**
6. **fifty-fifty-grip** — Never loses shape (`#f5f2ec`)
7. **collab-hero** — Coperni runway + pair
8. **press-feature** — INTERNI
9. **statement-band** — Knock
10. **fullbleed-statement**
11. **reviews**
12. **proof-numbers**
13. **fifty-fifty-one-pair**
14. **problem-section** — Chair Pose
15. **home-juicer**
16. **guarantee-band**
17. Footer (sitewide)

Do not restack without a letter.

## Messaging (keep)

| Placement | Line |
|-----------|------|
| Hero trust | ★★★★★ Trusted by 1,000's of instructors & studios |
| Hero H1 | The Pilates Sock Era is Over |
| Hero CTA | Shop Now → `#variants` |
| Tag | #letusknockyoursocksoff → `#knock-socks` |
| Coperni | Barreletics × Coperni / Built for the body in motion |
| Guarantee | Zero risk. All grip. |
| UGC | @barreletics |

## RETIRED — July 17 stack (history only)

July 17 Home APPROVED + DP-01–DP-12 remains lineage. That stack (problem early, GEO accordion, page newsletter) is **not** the locked M4 spine. Do not restore it over this file.

## Critical includes

- Hero Concept A (Sock Era) · Coperni seasonal · Juicer · guarantee
- **Videos:** every `<video>` autoplay muted (`muted` + `autoplay` + `loop` + `playsinline`)
