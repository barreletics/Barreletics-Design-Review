# Home mobile simplify recommendations (read-only)
**Date:** 2026-09-15 ET · Draft `187144929571` · Viewport 390  
**Prove:** Commit overlay **OFF** on fullbleed (`show_text false`, blank title/cta, `mobile_full_bleed true`, H≈**439**, no Commit/Shop CTA in section text).  
**FF spot-check:** Grip + One Pair `--ff-mobile-media-height/text-height: 520px` (One Pair mediaH **520**). Untouched.  
**Source:** `home-mobile-scan-readonly-390.json` · pageH ≈ **14993** (!).

## (1) Commit-on-image — DONE
Root cause: `71200de` restored Commit title + Shop Now on `fullbleed-statement`. Andrew NO-REVERT: image-only. Fixed + locked.

## (2) Simplify suggestions — DO NOT implement without Andrew go

Page is ~**15k px** tall on phone. Biggest compress / clarity wins:

| Priority | Section | Measured H | Suggestion | Risk |
| --- | --- | --- | --- | --- |
| **P0** | `visual-mosaic` | **2198** | Tallest block. Cap mobile tile height / 2-col denser grid, or drop to 4 tiles max on phone. | Medium — marketing proof |
| **P0** | `home-juicer` | **1593** | Already “see more” — default to **2–3** tiles + expand; shorter Instagram CTA strip. | Low |
| **P1** | `split_hero` | **1089** | Media alone **658**. Soften mobile media vh or tighten trust+copy stack; keep 62/38 desk frozen. | Medium — hero law |
| **P1** | Double Shop CTA rhythm | Grip + statement + problem + mosaic all shout Shop Now | Keep **one** primary Shop in first screen (hero/variants); demote later CTAs to text links or fewer solids. | Copy/CTA OS |
| **P1** | `variant-grid` | **1190** | “Shop all colors” is correct aisle — OK tall; optional collapse Outdoor row or tighter cards. | Low |
| **P2** | `proof-numbers` + `reviews` | 715 + 680 | Both “social proof.” Consider merging lede or placing numbers as a thin strip under reviews. | Medium |
| **P2** | `statement-band` then `fullbleed` | 317 + 439 | Knock-socks band + coral image-only beat are adjacent. Keep both for now (Commit locked image-only); later optional: drop statement CTA (redundant). | Low |
| **P2** | `collab-hero` | **894** | Stage + grid heavy. Phone: shorter stage vh or single product card. | Campaign |
| **Leave** | Grip / One Pair | 1056 / 1040 · **520/520** | **LOCKED — do not “simplify” by shrinking.** | Forbidden |
| **Leave** | Interni Chat art | 980 · media **490** | Editorial only; no Commit. Don’t thrash. | Forbidden without go |
| **Leave** | fullbleed image-only | **439** | Overlay LOCKED off. Don’t restore Commit. | Forbidden |

### One-line simplify thesis
**Cut mosaic + juicer height first**, then **reduce repeated Shop Now solids** below the fold — without touching FF locks or reintroducing fullbleed overlay copy.

### Not recommended
- Restoring Commit/Shop on fullbleed image  
- Shrinking Grip/One Pair below 520  
- Wholesale index.json redesign  
- Merging Interni into fifty-fifty  

