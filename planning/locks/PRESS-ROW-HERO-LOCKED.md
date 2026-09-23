# LOCKED — Press row hero (Home mosaic)

**Date:** 2026-09-22  
**Draft theme:** `187144929571` only — never publish from this lock.  
**Section:** `press-row` (`sections/press-row.liquid`)  
**Home:** mosaic on; `press-home` (`press-cards`) **disabled** (keep for PDP/collection reuse).

## Do not thrash

1. **Shopify Files video wins.** Setting `video` = `shopify://files/videos/Coperni 3.mov`.
2. **`video_url` must stay blank.** A CDN URL in that field overrides / fights the picker and reintroduced the wrong encode + top letterbox.
3. **Cover crop:** hero `<video>` oversized past the cell (`top/left -12%`, `width/height 124%`) with `overflow: hidden` on `.press-row__hero` — do not revert to `height: auto` / letterbox-friendly global video CSS.
4. **Proven encode** (from Files sources, not the old URL field): CDN id `d7ca87eac5034642851089c63af6a2d8` (not `a91000…` URL override).
5. **Cards (Home mosaic):**
   - Runway → Coperni closed-sole PDP
   - Collaboration → `/pages/collaborations`
   - INTERNI → Interni blog post
   - ITSLIQUID · Venice → `/blogs/news` stub (no ITSLIQUID post yet)
6. **Size:** ~540px band — leave alone unless Andrew asks.
7. One axis → fix → draft-bar proof. No wholesale Home redesign via this section.

## Files

- `shopify-build/sections/press-row.liquid`
- `shopify-build/sections/press-cards.liquid` (3-card; off on Home)
- `shopify-build/templates/index.json` — `press-row` + disabled `press-home` only for this lock

## Undo

Only if Andrew names this lock and says to unlock.
