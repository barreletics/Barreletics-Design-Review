# PDP section QA checklist — contamination-safe (2026-08-11)

**SIGNED LOCKED — do not open unless letter:** header nav #2 · Closed/Open/Outdoor rust badges · buy-box fold/ATC · v20d chrome · one-off buy-box layout.

**Rule:** JSON fix = only the template that owns the bug. Shared Liquid = only with proven bug + re-QA all five PDPs. Never rebuild one-off buy-box from `product.json`.

## Order of walk

1. Closed `product.json`  
2. Open `product.open-sole.json`  
3. Outdoor `product.outdoor.json`  
4. One-off Closed `product.one-off-closed.json`  
5. One-off Open `product.one-off-open.json`

---

## Core Closed / Open / Outdoor (full spine)

| # | Section | Check | If wrong |
|---|---|---|---|
| 1 | **pdp-buy-box** | SIGNED — ATC fold · chart-only Size · rust badge · 7 thumbs · empty under ATC | ASK — radioactive |
| 2 | **value-strip** | 4-up: Made in USA · Free shipping over $150 · 30-day returns · 90-day warranty | `value-strip` settings in that JSON only |
| 3 | **pdp-features** | Eyebrow/title/cards match sole; no pool; no “fully enclosed” | JSON only |
| 4 | **disciplines** | Cards/copy for that product family | JSON only |
| 5 | **fifty-fifty-sock-era** / water-shoes (Outdoor) | Media + copy; Open love-hate where intended | JSON only |
| 6 | **variant-grid** | Tabs · LE/Sold Out · quiet 4× · One-Offs tab rules | Shared Liquid only if all tabs broken |
| 7 | **fifty-fifty-lifestyle** | Quote/meta/CTA | JSON only |
| 8 | **fullbleed-statement (TRANSFORM)** | Title readable above scrim · CTA works | Shared Liquid stacking (done 2026-08-11) + per-JSON `overlay_opacity` |
| 9 | **pdp-sock-math** | Closed/Open only — compact; no review quote | JSON only |
| 10 | **fullbleed-lifestyle** | Media-only wow | JSON media URLs |
| 11 | **fifty-fifty-commit** | Title/body/CTA/media | JSON only |
| 12 | **reviews** (`pdp-reviews`) | Hybrid photo+text; not invented ratings | JSON blocks; Liquid only if TE broken |
| 13 | **fifty-fifty-numbers** | Think outside the sock / Outdoor equivalent | JSON only |
| 14 | **guarantee-band** | 3-up promise | JSON only |
| 15 | **home-juicer** | SIGNED pattern — after guarantee | Radioactive — ASK |
| 16 | **collection-faq** | FAQ+GEO; city last; no pool | JSON blocks |
| 17 | **pdp-sticky-atc** | Sticky works with fold | Shared only if broken everywhere |

---

## One-off Closed / Open (lean spine)

| # | Section | Check | If wrong |
|---|---|---|---|
| 1 | **pdp-buy-box** | SIGNED fold · One-Off badge (Closed black / Open rust) · kits off · chart-only | ASK — radioactive |
| 2 | **value-strip** | Same 4-up trust | JSON |
| 3 | **pdp-features** | “Same grip system. Limited color.” | JSON |
| 4 | **fifty-fifty-lifestyle** | Limited-color quote (Prompt 3) | JSON |
| 5 | **fullbleed-lifestyle** | Open one-off only (studio media) if present | JSON |
| 6 | **variant-grid** | Default One-Offs · available then sold-out · no Earlier band | Shared only if grid logic |
| 7 | **fifty-fifty-commit** | Limited color. Unlimited grip. | JSON |
| 8 | **reviews** | Prompt 4 set ≠ core Kimberly set; Open hybrid JM text | JSON |
| 9 | **fifty-fifty-numbers** | One-Off colors eyebrow | JSON |
| 10 | **guarantee-band** | 3-up | JSON |
| 11 | **home-juicer** | Match Closed juicer settings | Radioactive — ASK |
| 12 | **collection-faq** | Closed stack + 3 one-off Qs | JSON |
| 13 | **pdp-sticky-atc** | Works | Shared only if global |

---

## Pass / fail notes (fill during QA)

| Template | Pass | Issues |
|---|---|---|
| Closed | | |
| Open | | |
| Outdoor | | |
| One-off Closed | | |
| One-off Open | | |
