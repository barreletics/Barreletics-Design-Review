# Theme Editor controls — Andrew review (do not remove)

Plain-English list of controls you probably rarely need. **Usage** = instances in git `templates/*.json` where the value differs from schema default (or key missing when default matters).

## fifty-fifty — Andrew TE fixes (2026-10-03, PR #32 branch)

- **Button style** (`cta_style`): schema select — rust solid (default), rust outline, black solid, black outline; uses global `.btn--*` classes (+ new `.btn--brand-outline` in `barreletics-base.css`). Removed dead per-section CTA colour overrides.
- **Text pad (unified)** (`text_pad_y` desktop default **96**, `text_pad_y_mobile` phone default **80**): only these drive top/bottom padding. Legacy ids `text_pad_top`, `text_pad_bottom`, `text_pad_top_mobile`, `text_pad_bottom_mobile`, `vertical_padding` stay hidden in schema (JSON values preserved on save) but are **ignored for rendering** — unset unified pad uses schema default.
- **Phone pad balance fix**: `.split-text` no longer `justify-content: center` on the raw children (biased ~48px extra air above copy on phone). Copy lives in `.split-text__stack` with first/last margins zero; desktop centers the stack with `margin-block: auto` inside the stretched column.
- **Gap between image & text** (`column_gap`): control removed; grid gap is always **0**.
- **Eyebrow / quote heading**: label + info for Quote style; quote-mode eyebrow respects **Heading level** (not hardcoded H2).

## split-hero (1 placed instances)

- **Custom desktop focal — horizontal % (only if focal = Custom)** (`image_pos_x`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `50`.
- **Custom desktop focal — vertical %** (`image_pos_y`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `50`.
- **Custom phone focal — horizontal %** (`image_pos_x_mobile`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `50`.
- **Custom phone focal — vertical %** (`image_pos_y_mobile`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `50`.
- **Custom trust strip link URL** (`trust_url`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'—'`.
- **Desktop zoom % (fine-tune crop)** (`image_zoom`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `100`.
- **Fallback hero image URL when Shopify picker is empty** (`image_url`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg?v=1710549452&width=2400'`.
- **Heading tag level (H1 vs H2) — SEO tweak** (`heading_level`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'h1'`.
- **Hide the whole hero on desktop** (`hide_on_desktop`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `False`.
- **Hide the whole hero on phone** (`hide_on_mobile`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `False`.
- **Legacy: show video controls (hidden; was never on in git)** (`video_controls`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `False`.
- **Override body font size** (`body_size`) — changed from default on **1/1** instances; key absent **0/1**; schema default: `'default'`.
- **Override body weight** (`body_weight`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'default'`.
- **Override CTA button size** (`cta_size`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'default'`.
- **Override hero title font size** (`title_size`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'default'`.
- **Override hero title weight** (`title_weight`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'default'`.
- **Override screen-reader name (heading is usually enough)** (`aria_label`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `'—'`.
- **Phone frame margin bottom** (`inset_bottom_mobile`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `0`.
- **Phone frame margin left/right** (`inset_x_mobile`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `0`.
- **Phone frame margin top (only when separate phone margins on)** (`inset_top_mobile`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `0`.
- **Phone zoom %** (`image_zoom_mobile`) — changed from default on **0/1** instances; key absent **0/1**; schema default: `100`.

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

