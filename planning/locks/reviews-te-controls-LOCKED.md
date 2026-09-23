# Reviews TE Controls — LOCKED 2026-09-20

**Do not change without Andrew's explicit approval.**

## Global (Theme Settings → Colors)
- Star color: sitewide picker (bright yellow, muted gold, terracotta, black)
- Star size: sitewide slider (12–22px, default 14)
- Aggregate score: ★★★★★ 4.9 out of 5 (no review count)

## Section controls per preset

### Home (`band_context: home`)
- Headline + subhead
- Text cards: 3 visible desktop, 2 visible phone + "See more reviews ↓"
- "Read reviews →" link
- No photos, no Judge.me
- Score line centered on mobile

### Reviews page (`band_context: reviews_page`)
- Headline + subhead
- 4 photo cards (desk 4-up, phone 1 or 2 cols)
- Judge.me full list below
- No text cards, no CTA link

### PDP (`band_context: pdp`)
- Headline + subhead
- Photo cards + text cards
- Judge.me optional (compact)
- "More reviews →" auto on product pages

### Collection (`band_context: collection`)
- Headline + subhead
- Text cards
- "Read reviews →" link
- Judge.me optional (compact)

## Locked CSS behavior (no knob — automatic)
- Tablet: 2-up photos, 2-col text grid
- Phone: 1 col stacked, center-aligned
- PDP phone: text cards capped at 4
- Score line centered on mobile

## Files
- `sections/pdp-reviews.liquid`
- `layout/theme.liquid` (global star override)
- `config/settings_schema.json` (star color + size)
- All 13 template JSONs with `band_context` + `show_aggregate: true`

## Legacy removed
`scope`, `live_mode`, `pictures_first` — gone from schema and all JSON.
