# Theme Editor fixes — split hero (Andrew QA 2026-10-03)

**Section Andrew was using:** Home **Split hero** (`sections/split-hero.liquid`, template `index.json` → `split_hero`). Always-visible X/Y + zoom sliders were here, not fifty-fifty (fifty-fifty already uses focal dropdowns from PR #32).

## Broken → fixed

| Issue | Cause | Fix |
|-------|--------|-----|
| **No live preview on sliders** (width, height, focal, pads, etc.) | PR #35 `{% style %}` used top-of-file Liquid assigns (`media_pct`, `img_x`, `text_pad_y_d`…). Theme Editor only hot-patches `{% style %}` output that ties to `section.settings.*` — assigns are frozen until Save. | Dual-write block reads `section.settings` directly (focal legacy resolved inside `{% style %}`), `!important` on `--sh-*` vars + copy padding/backgrounds — same pattern as `fifty-fifty.liquid`. |
| Mobile focal X/Y + zoom | Inline `style` on `#split-hero-*` beat TE live CSS updates; mobile vars never got `!important` dual-write | TE `{% style %}` block with `!important` on `--sh-img-x-m`, `--sh-img-y-m`, `--sh-img-zoom-m` (and desktop vars) |
| Star size | Liquid read `settings.star_size_global` instead of `section.settings.star_size` | Use section star size/color with theme global fallback |
| Show video controls | `controls` attribute not updated on live preview without full re-parse | `data-video-controls` + `shopify:section:load` / `select` script toggles `controls` on `<video>` |

## Focal pattern (matches fifty-fifty)

- Desktop: `image_position` preset dropdown + Custom → `image_pos_x` / `image_pos_y` / `image_zoom` via `visible_if`
- Phone: `image_position_mobile` (default **Same as desktop**) + Custom → phone sliders
- Legacy JSON without `image_position`: infer Center when 50/50, else Custom (index hero → Center, zero visual change)

## Insets

- `section-inset-vars.liquid`: when `inset_custom_mobile` is off, phone margins use **desktop** inset values (was always reading phone sliders).
- Schema: desktop vs phone labels; phone sliders only when “Separate phone inset” is on (`visible_if`).

## Accessibility

- Split hero: always outputs `aria-label` (heading text stripped, else “Split hero”).
- Fifty-fifty: always outputs `aria-label` (aria field → heading → “50/50 section”).
