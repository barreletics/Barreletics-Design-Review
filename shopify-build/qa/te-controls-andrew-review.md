# Theme Editor controls — Andrew review (do not remove)

Plain-English list of controls you probably rarely need. **Usage** = instances in git `templates/*.json` where the value differs from schema default (or key missing when default matters).

## problem-section — 50/50 parity (stacked PR on #32)

- **Photo / video**: Same priority as fifty-fifty (Shopify video → Video URL → Shopify image → Image URL); legacy `video_asset` / `image_asset` hidden but still render when higher sources empty.
- **Focus + height**: Focal desktop/phone, `min_height` (default **860**), `media_column_pct` (legacy `desktop_split` maps when unset), phone height/width, frame shape desktop+phone, fit cover/fit (+ legacy cover_inset/contain from JSON).
- **Heading / body / CTA**: Global heading lock + **Button** (`cta_style`: Rust / Black / Rust outline / Black outline → `.btn--*`); pain points stay **Pain point** blocks; **Space above bullet list** (`copy_stack_gap`).
- **Trust strip**: Optional `show_trust_strip` + `trust_text` (stars above copy).
- **Layout**: Reverse, phone stack, unified **Text pad top & bottom** (`text_pad_y` **96** / `text_pad_y_mobile` **80**); side pads default **40** / **16** (not 50/50’s 64/20); `bg_style` + legacy `bg_preset`/`bg_color`.
- **Section gap**: `section_gap` default **0** (cover-flush Home band); `section_gap_mobile`, hide on phone/desktop.
- **Legacy hidden**: Old CTA colour pickers, separate text pad keys, `heading_size_override` — preserved on save, not used for output (except legacy bg paths).

## fifty-fifty — Andrew TE fixes (2026-10-03, PR #32 branch)

- **Button style** (`cta_style`): schema select — rust solid (default), rust outline, black solid, black outline; uses global `.btn--*` classes (+ new `.btn--brand-outline` in `barreletics-base.css`). Removed dead per-section CTA colour overrides.
- **Text pad (unified)** (`text_pad_y` desktop default **96**, `text_pad_y_mobile` phone default **80**): only these drive top/bottom padding. Legacy ids `text_pad_top`, `text_pad_bottom`, `text_pad_top_mobile`, `text_pad_bottom_mobile`, `vertical_padding` stay hidden in schema (JSON values preserved on save) but are **ignored for rendering** — unset unified pad uses schema default.
- **Phone pad balance fix**: `.split-text` no longer `justify-content: center` on the raw children (biased ~48px extra air above copy on phone). Copy lives in `.split-text__stack` with first/last margins zero; desktop centers the stack with `margin-block: auto` inside the stretched column.
- **Gap between image & text** (`column_gap`): control removed; grid gap is always **0**.
- **Eyebrow / quote heading**: label + info for Quote style; quote-mode eyebrow respects **Heading level** (not hardcoded H2).

## collection-hero — 50/50 parity (stacked PR on #36)

- **Photo / video**: Same priority as fifty-fifty; collection-specific **Photo size** (`media_fill`: inset / column / bleed) and phone frame (`aspect_ratio_mobile`, fit selects, `text_height_mobile`).
- **Focus + height**: `image_zoom`, `min_height` (legacy `media_height` when unset — e.g. **660** on main collection JSON), `media_column_pct`.
- **Heading / body / CTA**: H1 locked; **Button** (`cta_style` → `.btn--*`); secondary text link unchanged.
- **Trust strip**: `show_trust_strip` (fallback legacy `show_trust`) + `trust_text`; eyebrow when trust off.
- **Layout**: Reverse, phone stack, **Text pad top & bottom** (`text_pad_y` optional — unset keeps legacy **56px** split padding; `text_pad_y_mobile` unset uses legacy **`text_spacing_mobile`** e.g. **36**).
- **Section gap**: `section_gap` / `section_gap_mobile` default **0** (bleed hero keeps separate 32px token before grid).
- **Legacy hidden**: `media_type`, `media_height`, `show_trust`, `text_spacing_mobile`.

## page-about-split — 50/50 parity (stacked PR on #36)

- Same header order 1–6 as fifty-fifty; About-specific height sliders + legacy clamp pads when unified pads unset in JSON.

## page-about-joseph — 50/50 parity (stacked PR on #36)

- Dual gallery images under section 1; no height sliders (natural aspect); layout + legacy type keys hidden.

## split-hero — 50/50 parity (stacked PR on #34)

- **Photo / video**: Same priority as fifty-fifty (Shopify video → Video URL → Shopify image → Image URL); optional phone still via `<picture>`; `poster_url` for external mp4; legacy `media_type` hidden.
- **Focus + height**: Focal desktop/phone + `image_scale` (legacy `image_pos_*` / `image_zoom*` map when focal unset); **Section height** `media_height` (% of 92vh, default **100**); `media_column_pct` (default **50** in schema, renders saved JSON); fit cover/fit, frame shape, phone height/width, `media_bg` letterbox.
- **Heading / body / CTA**: `type-hero` title + nbsp last-two-words; **Button** (`cta_style` → `.btn--*`); typography overrides (`title_size`, weights, `cta_size`); hashtag line under CTA.
- **Trust strip**: `show_trust_strip` (fallback legacy `show_trust`) + stars, colours, gaps, trust link, `trust_text_size`.
- **Layout**: Reverse (`reverse` / legacy `reverse_layout`), phone stack, text pads **72** / **56** / **52** / **24**, `bg_style` + legacy `bg_color`, corner radius on media + copy.
- **Section gap**: `section_gap` default **0** (flush hero); `section_gap_mobile`, hide on phone/desktop; frame **inset_*** in section 6 via `section-inset-vars`.
- **Legacy hidden**: `image_pos_*`, `image_zoom*`, CTA colour pickers, `video_controls`, old content/media layout headers — preserved on save, not shown in TE.

## fifty-fifty (41 placed instances)

- **Custom CTA URL when link target is Custom** (`cta_url`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Custom desktop focal horizontal %** (`focal_x`) — changed from default on **2/41** instances; key absent **11/41**; schema default: `50`.
- **Custom desktop focal vertical %** (`focal_y`) — changed from default on **10/41** instances; key absent **11/41**; schema default: `50`.
- **Custom phone focal horizontal %** (`focal_x_mobile`) — changed from default on **0/41** instances; key absent **41/41**; schema default: `50`.
- **Custom phone focal vertical %** (`focal_y_mobile`) — changed from default on **0/41** instances; key absent **41/41**; schema default: `50`.
- **Custom trust link URL** (`trust_url`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **External mp4 URL (vs Shopify video picker)** (`video_url`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **External still image URL** (`image_url`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Extra CSS class on heading** (`heading_class`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Extra space after section on phone** (`section_gap_mobile`) — changed from default on **3/41** instances; key absent **15/41**; schema default: `0`.
- **Heading tag level** (`heading_level`) — changed from default on **0/41** instances; key absent **23/41**; schema default: `'h2'`.
- **Hide on desktop** (`hide_on_desktop`) — changed from default on **0/41** instances; key absent **24/41**; schema default: `False`.
- **Hide this 50/50 block on phone** (`hide_on_mobile`) — changed from default on **0/41** instances; key absent **24/41**; schema default: `False`.
- **Jump-link ID for in-page anchors** (`anchor_id`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy body size (locked; no visual effect)** (`body_size`) — changed from default on **41/41** instances; key absent **0/41**; schema default: `'default'`.
- **Legacy custom panel colour picker** (`bg_color`) — changed from default on **28/41** instances; key absent **1/41**; schema default: `'#ffffff'`.
- **Legacy min text column height on phone** (`mobile_text_height`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy single desktop pad slider** (`vertical_padding`) — changed from default on **28/41** instances; key absent **3/41**; schema default: `88`.
- **Legacy stat emphasis** (`stat_3_emphasis`) — changed from default on **3/41** instances; key absent **21/41**; schema default: `True`.
- **Legacy stat row** (`stat_2_label`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy stat row** (`stat_2_value`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy stat row** (`stat_3_label`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy stat row** (`stat_3_value`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy stat row labels** (`stat_1_label`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy stat values** (`stat_1_value`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy theme asset filename for image** (`image_asset`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Legacy title weight** (`title_weight`) — changed from default on **2/41** instances; key absent **0/41**; schema default: `'400'`.
- **Override screen-reader name** (`aria_label`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Phone image width below 100%** (`mobile_media_width`) — changed from default on **0/41** instances; key absent **41/41**; schema default: `100`.
- **Phone square frame (legacy hidden)** (`media_aspect_mobile`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Poster URL when using mp4 URL** (`poster_url`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Quote author uppercase styling (legacy)** (`quote_author_case`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Quote italic (legacy)** (`quote_italic`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Small line above heading (most pages use heading only)** (`eyebrow`) — changed from default on **0/41** instances; key absent **0/41**; schema default: `'—'`.
- **Square frame shape vs fill height** (`media_aspect`) — changed from default on **1/41** instances; key absent **24/41**; schema default: `'stretch'`.

