# fifty-fifty (50/50 Split): control standardization spec

**Status:** spec only, approved for writing by Andrew 2026-10-02. **No theme file, template, setting or PR has been changed.** Draft `187144929571` and live `185687998755` are untouched, and PR #31 stays a draft.
**Data source:** instance values come from **git `c0c0564`** (`shopify-build/templates/*.json`, 2026-10-02 16:53 ET). The draft theme couldn't be read: the CLI on the box isn't logged in, and the Admin API app lacks `read_themes`. **Before implementing, pull the 15 templates from the draft (pull only) and re-check every value below.**
**Code:** `sections/fifty-fifty.liquid` from `grok/fifty-fifty-live-preview` (`dc96103`, PR #31). **42 placed instances** in 14 templates. One is disabled: `collection : fifty-fifty-disciplines`.

**Ground rules for the implementing PR**
1. **Zero visual change** on all 42 instances. Every stored non-default value is preserved (see the list at the end). Wherever a default changes, the old effective value is **written explicitly** into each instance that relied on it, *before* the schema default changes.
2. Every kept control's default = the **most-used effective value** across the 42 instances. Its label ends in "(default: X)" or its `info` says "(default)".
3. Live preview: every range/colour/select value is dual-written in the `{% style %}` block, reading `section.settings.ID` directly (the PR #31 pattern). Class-toggle controls (reverse, stack order, fit) may stay Save-only.
4. Removals are limited to controls that are **dead** (no code reads them) or **never changed** in any instance. Media-source removals are **pending Andrew's approval**.

## Missing controls (asked for, not in 50/50 today)
| # | Wanted | Today | Proposal |
|---|---|---|---|
| 1 | **Phone focal point** | **None.** Phone *cover* uses the desktop `focal_x/focal_y`. Phone *fit* uses the desktop focal, or `center top` when focal is 50/50 / center. A separate phone image (`image_mobile`, 8 instances) also gets the desktop focal | Add `focal_mobile_custom` (checkbox, default **off** = same as desktop, today's behaviour) + `focal_x_mobile` / `focal_y_mobile` (range 0–100/1 %, default 50). Off on every instance → zero change |
| 2 | **Desktop top and bottom text padding, separately** | One `vertical_padding` slider applied to both top and bottom (32–120/4, default 88) | Split into `text_pad_top` + `text_pad_bottom` (32–120/4 px, default **80**, the most used). Migration: write both = the instance's current `vertical_padding` (3 instances rely on implicit 88, so write 88) |
| 3 | **Phone text side padding** | None. Fixed `var(--section-padding-x-mobile)` = **20px** (design-tokens.css) | Add `text_pad_x_mobile` (range 12–48/4 px, default **20**). Matches today exactly |
| 4 | **Phone media width** | None. Phone media is always full width | Optional: `mobile_media_width` (range 70–100/5 %, default **100**). Only add if Andrew wants inset phone images |
| 5 | Desktop cover/fit **and** phone cover/fit | ✅ exist (`media_fit`, `image_fit_mobile`) | Keep. Trim unused options (see table) |
| 6 | Reverse (desktop) / image top or bottom (phone) | ✅ exist (`reverse`, `mobile_stack_order`) | Keep |
| 7 | Phone height, phone top/bottom text pads | ✅ exist (`mobile_media_height`, `text_pad_top_mobile`, `text_pad_bottom_mobile`) | Keep. **`text_pad_bottom_mobile` stays separate (not merged)** per Andrew |

## Defaults that would change (each needs explicit write-back first)
| Control | Current default | Proposed default (most used) | Instances relying on the old default → write explicit value |
|---|---|---|---|
| Background (`bg_color` → `bg_style`) | `#ffffff` | **Cream `#faf8f6`** (29 of 42 vs white 13) | `product : fifty-fifty-sock-era` (key absent) → write `white`. The other 12 white instances already store `#ffffff`, so map them to `white` |
| Desktop text pad (`vertical_padding` → `text_pad_top`/`text_pad_bottom`) | 88 | **80** (28 vs 14) | `collection.apparel` : `fifty-fifty-tees`, `-think-outside`, `-leggings` (key absent, implicit 88) → write 88/88. 11 others store 88 explicitly, so copy it |
| `cta_link_target` | `custom` | **`#variants`** (14; #buy 12, custom 10) | All 42 store it explicitly, so no change. ⚠ New instances on collection/pages would default to `#variants`, an anchor that only exists on PDPs. Andrew may prefer to keep `custom` |
| `cta_text` (content) | "Shop Now" | **"Shop now"** (20 vs 7) | All 42 explicit, so no change |
| `image_position` | `center` | **removed** (folded into focal) | See risk R1 |
| Everything else kept | | already equals the most-used value | — |

## Background: fixed select instead of a colour picker
Proposed `bg_style` (select): **White `#ffffff`** · **Cream `#faf8f6` (default)** · **Darker cream `#efe9dd`** (optional).
- Darker cream: **`#efe9dd`** is proposed because it is already in the theme, used as the outdoor letterbox colour (4 instances). ⚠ **Do not use `#f5f2ec`.** `design-tokens.css` marks it "darker #f5f2ec retired forever".
- `bg_preset` (white/cream/custom, never changed, all 42 = custom) is removed and replaced by `bg_style`.

| Current panel `bg_color` | Instances | Maps to | Exact? |
|---|---|---|---|
| `#faf8f6` | 29 | Cream | ✅ exact |
| `#ffffff` (explicit) | 12 | White | ✅ exact |
| `#ffffff` (implicit default) | 1 (`product : fifty-fifty-sock-era`) | White (write explicitly) | ✅ exact |
| any other | 0 | — | — |

**Result: all 42 panel backgrounds map exactly. No flags.**

**Letterbox colour (`media_bg`) is a different control.** It only shows when media is in *fit* mode (or behind a still-loading or transparent image). Its values do **not** fit a 3-option select: `#ffffff`×21, `#faf8f6`×6, `#f9f9f9`×5, `#efe9dd`×4, `#3a7eb8`×2, `#1565c0`×2, `#f0a12a`×2.
- ⚠ `#f9f9f9` is **visible** on `page.best-grippy-socks : outgrew` (desktop fit) and isn't an option.
- The blue and orange values sit behind cover media on in-studio / open-sole PDPs. They show only while the media loads.
- **Recommendation:** keep `media_bg` as a colour picker, relabel it "Letterbox colour (fit only)", and remove only `media_bg_preset` (never changed). Converting it to a select would need Andrew to accept `#f9f9f9 → #ffffff` on outgrew (a barely visible change), so it is not proposed.

## Media source fields ("backup / fallback URLs")
Render priority in code: **Shopify `video`** → **`video_url`** → **`image`** (picker) → **`image_asset`** → **`image_url`** → placeholder. Poster for `video_url` = `image` if set, else `poster_url`. `image_mobile` swaps the still on phones (≤768px), and **only when there is no video**.

| Field | What it does | Wins (renders) in | Set but shadowed | Rec |
|---|---|---|---|---|
| `video` (Shopify video) | Native Shopify video; Shopify supplies its own preview frame | 1 (the **disabled** collection/disciplines) | — | **keep** (preferred native source) |
| `video_url` (mp4) | External/CDN mp4, autoplay muted loop | 13 | — | **keep** (main video source) |
| `poster_url` | **Still shown before the video loads** (the press-page behaviour Andrew wants). Only used when `image` is empty | 7 posters (index/grip, coperni/sock-era, product/sock-era, product/numbers, one-off-closed/numbers, one-off-open/numbers, apparel/think-outside) | 1: `collection : fifty-fifty-grip` (no video, so ignored) | **keep** (wanted) |
| `image` (picker) | Shopify-hosted still. Also used as the video poster if set | 7 | 1: collection/disciplines (video wins; becomes poster only for `video_url`, not native video) | **keep** |
| `image_url` | Still from a URL. The workhorse | 18 | **15** (behind video or picker; harmless backup) | **keep** |
| `image_asset` | Theme-asset filename (`asset_url`) | 3 (product.outdoor commit/numbers/barefoot) | — | **remove: pending approval.** Duplicates `image_url`. Migration: put each file's `asset_url` CDN URL into `image_url`; the same file means no visual change |
| `image_mobile` (picker) | Phone-only still (crop/orientation) | 8 (all non-video, so all effective) | — | **keep** |
| `image_alt` | Alt text for whichever still renders | 31 | — | **keep** (a11y) |

**Observations**
- **6 `video_url` instances have no poster:** coperni/commit, product/commit, one-off-closed/commit, one-off-open/commit, in-studio/tired-socks, open-sole/tired-socks. In 4 of them (the `commit` ones) `image_url` is set but unused.
- Option, **pending approval**: when `poster_url` and `image` are empty, fall back to `image_url` as the poster. That gives those 4 a pre-load still (only the loading moment changes, never the played video).
- Where `poster_url` and `image_url` are both set, they are identical in all 5 cases. So `poster_url` *could* later merge into `image_url` ("still image = poster"). **Not proposed now**, because Andrew wants the explicit poster field.

## Risky instances (need Andrew's decision; zero-change option given)
- **R1. Saved focal values that currently do nothing.** These 4 instances store a focal point, but `image_position` = `center`, so the focal is ignored today:
  - `product.coperni : fifty-fifty-commit` (focal_y 40; position implicit center)
  - `product.in-studio-template : fifty-fifty-lifestyle` (focal_y 72, position center)
  - `product.open-sole : fifty-fifty-lifestyle` (focal_y 72, position center)
  - `index : fifty-fifty-one-pair` (focal_x 100, position center)

  Folding `image_position` into focal (always active) would **move these images**. Zero-change migration: write focal 50/50 on these 4. **Ask Andrew** whether 72/40/100 were intended. If yes, that's a deliberate visual change he approves per instance.
- **R2. Phone fit focal quirk.** With phone *fit*, focal 50/50 renders `center top`, not `center center`. This affects `product.coperni : fifty-fifty-lifestyle` (custom 50/50, phone fit). Keep this rule exactly, both in the new phone-focal logic and when `focal_mobile_custom` is off.
- **R3. Desktop fit letterbox.** `page.best-grippy-socks : outgrew` (desktop fit, letterbox `#f9f9f9`). Keep `media_bg` as a picker, or it changes.
- **R4. Product-template overrides.** On product templates, code forces `section_gap_mobile` = 0 and `mobile_text_height` = 0. The new controls must keep those overrides. None of the 4 instances with `section_gap_mobile` = 24 are on product templates.
- **R5. Phone pad conflict.** The `text_pad_top_mobile` info text says "LOCKED global PDP standard: 96", but 8 PDP instances use 32 (with bottom at default 96). Keep the values and fix the info text only.

## Control table (proposed final set)
D = desktop, P = phone. Live: ✅ live via `{% style %}` today · 🆕 make live in the PR · 💾 Save-only (class toggle, acceptable). Usage = effective values across 42 instances.

### Media
| id | Label (proposed) | Type | Range / options | Default proposed (current) | D/P | Live | Usage | Migration | Rec |
|---|---|---|---|---|---|---|---|---|---|
| `video` | Shopify video | video | — | — | D+P | content | 1 (disabled instance) | none | keep |
| `video_url` | Video URL (mp4) | text | — | — | D+P | content | 13 | none | keep |
| `poster_url` | Video poster: still shown before video loads | text | — | — | D+P | content | 7 effective | none | keep |
| `image` | Image (Shopify), also the video poster | image_picker | — | — | D+P | content | 7 win | none | keep |
| `image_url` | Image URL | text | — | — | D+P | content | 18 win, 15 backup | none | keep |
| `image_asset` | Theme asset filename | text | — | — | D+P | content | 3 | asset → `image_url` CDN URL | **remove (pending approval)** |
| `image_mobile` | Phone image (optional) | image_picker | — | — | P | content | 8 | none | keep |
| `image_alt` | Image alt text | text | — | — | D+P | content | 31 | none | keep |
| `media_fit` | Media fit: desktop | select | **cover (default)**, fit | cover | D | 💾 | cover 41, fit 1 (outgrew) | drop unused `cover_inset`, `contain` (0 uses) | keep |
| `image_fit_mobile` | Media fit: phone | select | **cover (default)**, fit | cover | P | 💾 | cover 41, fit 1 (coperni/lifestyle) | drop unused `contain` | keep |
| `image_position` | Image focal point (presets) | select | 10 presets | center | D+P | ✅ | center 31, custom 11 | fold into focal: custom keeps x/y; center → 50/50 (**R1**) | **remove (merge into focal)** |
| `focal_x` | Focal point: horizontal (default 50) | range | 0–100 / 1 % | 50 | D (+P when no phone focal) | ✅ | 50×40, 100 (index/one-pair, *inert: position center*), 38 (outdoor/commit) | see R1. ⚠ index/one-pair x=100 is also inert (position center) → write 50 | keep |
| `focal_y` | Focal point: vertical (default 50) | range | 0–100 / 1 % | 50 | D (+P) | ✅ | 50×32, 85×5, 72×2 (*inert*), 40×2 (1 inert), 78×1 | see R1 | keep |
| `focal_mobile_custom` 🆕 | Separate phone focal point (default off) | checkbox | — | off | P | 🆕 | — | off everywhere = today | **add** |
| `focal_x_mobile` / `focal_y_mobile` 🆕 | Phone focal point | range | 0–100 / 1 % | 50 | P | 🆕 | — | none | **add** |
| `image_scale` | Image scale | range | 100–150 / 5 | 100 | D+P | ✅ | 100×42 | never changed | remove |
| `contain_width` | Contain media width | range | 40–100 / 2 | 72 | D+P | ✅ | 72×42 (contain unused) | never changed | remove |
| `media_bg_preset` | Letterbox preset | select | white/cream/custom | custom | D+P | ✅ | custom×42 | never changed | remove |
| `media_bg` | Letterbox colour (fit only) (default white) | color | — | #ffffff | D+P | ✅ | #ffffff 21, #faf8f6 6, #f9f9f9 5, #efe9dd 4, #3a7eb8 2, #1565c0 2, #f0a12a 2 | none (stays picker; R3) | keep |
| `media_aspect` | Frame shape: desktop | select | **stretch (default)**, square | stretch | D | 💾 | square 1 (index/grip) | none | keep |
| `media_aspect_mobile` | Frame shape: phone | select | stretch, square | stretch | P | 💾 | stretch×42 | never changed | remove |

### Layout and size
| id | Label | Type | Range / options | Default proposed (current) | D/P | Live | Usage | Migration | Rec |
|---|---|---|---|---|---|---|---|---|---|
| `reverse` | Image on right, desktop (default off) | checkbox | — | off | D | 💾 | on 15 | none | keep |
| `mobile_stack_order` | Phone: image on top / bottom (default top) | select | **media_first (default)**, copy_first | media_first | P | 💾 | copy_first 7 | none | keep |
| `media_column_pct` | Image width, desktop (default 50%) | range | 35–72 / 1 % | 50 | D | ✅ | 54 (index/one-pair) | none | keep |
| `min_height` | Height, desktop (default 560) | range | 400–1200 / 20 px | 560 | D | ✅ | 620×2 (index), 640×2 (best-grippy) | none | keep |
| `mobile_media_height` | Image height, phone (default 0 = theme 500px) | range | 0–700 / 10 px | 0 | P | ✅ | 400 (coperni/lifestyle), 360×2 (in-studio, open-sole lifestyle) | none | keep |
| `mobile_media_width` 🆕 | Image width, phone (default 100%) | range | 70–100 / 5 % | 100 | P | 🆕 | — | 100 = today | **add (optional)** |
| `mobile_text_height` | Text min-height, phone | range | 0–700 / 10 | 0 | P | ✅ | 0×42 (forced 0 on PDPs) | never changed | remove |
| `column_gap` | Gap between image and text, desktop (default 0) | range | 0–64 / 4 px | 0 | D | ✅ | 64, 56 (coperni) | none | keep |
| `media_radius` | Corner radius | range | 0–24 / 2 | 0 | D+P | ✅ | 0×42 | never changed | remove |

### Text padding (top and bottom kept separate on both desktop and phone)
| id | Label | Type | Range / options | Default proposed (current) | D/P | Live | Usage | Migration | Rec |
|---|---|---|---|---|---|---|---|---|---|
| `vertical_padding` | Text pad, desktop (top = bottom) | range | 32–120 / 4 | (88) | D | ✅ | 80×28, 88×14 (3 implicit) | → split into the two below | **replace** |
| `text_pad_top` 🆕 | Text pad top, desktop (default 80) | range | 32–120 / 4 px | **80** | D | 🆕 | — | = old vertical_padding per instance (write 88 on the 3 implicit apparel) | **add** |
| `text_pad_bottom` 🆕 | Text pad bottom, desktop (default 80) | range | 32–120 / 4 px | **80** | D | 🆕 | — | same | **add** |
| `side_padding` | Text pad left and right, desktop (default 64) | range | 16–96 / 4 px | 64 | D | ✅ | 64×42 | none (kept as the desktop side pad in the full set; was "never changed") | keep |
| `text_pad_top_mobile` | Text pad top, phone (default 96) | range | 16–120 / 4 px | 96 | P | ✅ | 32×10 | none; fix "LOCKED 96" info (R5) | keep |
| `text_pad_bottom_mobile` | Text pad bottom, phone (default 96) | range | 16–120 / 4 px | 96 | P | ✅ | 32×2 (index grip, one-pair) | **not merged** (Andrew) | keep |
| `text_pad_x_mobile` 🆕 | Text pad left and right, phone (default 20) | range | 12–48 / 4 px | 20 | P | 🆕 | — | 20 = today's token | **add** |

### Spacing and visibility
| id | Label | Type | Range / options | Default proposed (current) | D/P | Live | Usage | Migration | Rec |
|---|---|---|---|---|---|---|---|---|---|
| `section_gap` | Space above and below, desktop (default 32) | range | 0–96 / 4 px | 32 | D | ✅ | 0×3 (coperni) | none. Optional: split into top/bottom like text pads (write both = current) | keep |
| `section_gap_mobile` | Space after section, phone (default 0) | range | 0–96 / 4 px | 0 | P | ✅ | 24×4 (collection ×2, best-grippy ×2) | none (forced 0 on PDP, R4) | keep |
| `hide_on_mobile` / `hide_on_desktop` | Hide on phone / desktop | checkbox | — | off | P / D | 💾 | 0 | none | keep (cheap switch) |

### Background
| id | Label | Type | Range / options | Default proposed (current) | D/P | Live | Usage | Migration | Rec |
|---|---|---|---|---|---|---|---|---|---|
| `bg_style` 🆕 | Text panel background | select | White #ffffff · **Cream #faf8f6 (default)** · Darker cream #efe9dd | cream | D+P | 🆕 | — | from bg_color: #faf8f6 → cream (29), #ffffff → white (13, incl. 1 implicit). **All exact** | **add** |
| `bg_color` | Custom text panel colour | color | — | (#ffffff) | D+P | ✅ | #faf8f6 29, #ffffff 13 | → bg_style | **replace** |
| `bg_preset` | Text panel background preset | select | white/cream/custom | custom | D+P | ✅ | custom×42 | never changed | remove |

### Content, heading and CTA
| id | Label | Type | Range / options | Default proposed (current) | D/P | Live | Usage | Migration | Rec |
|---|---|---|---|---|---|---|---|---|---|
| `content_style` | Content style | select | **standard (default)**, quote (drop `statement`: no-op; drop `stats`: 0 uses) | standard | D+P | 💾 | quote 2 (product, outdoor lifestyle) | none | keep (trim options) |
| `eyebrow`, `title`, `body` | Eyebrow / Heading / Body | text / textarea | — | — | D+P | content | 13 / 41 / 41 | none | keep |
| `heading_level` | Heading level (default h2) | select | h1–h6 | h2 | — | 💾 | h2×42 | none | keep (SEO) |
| `heading_register` | Heading register | select | display/supporting/standard | display | — | ✖ dead | — | dead since 2026-09-27 heading lock | remove |
| `heading_size_override` | Heading size override | number | — | blank | D | 💾 | 0 | never set; global heading lock | remove |
| `title_size` | Title size (now quote text only) | select | default…56 | default | D+P | 💾 | default×42 | never set | remove |
| `title_weight` | Title weight | select | default/400–700 | 400 | D+P | 💾 | 400×40, "default"×2 (index grip/one-pair, renders = 400) | none (both render 400) | remove |
| `body_size` | Body size | select | default…56 | default | — | ✖ dead | 17×40, 16×2 (index) **stored but no effect** | none (body locked 17px) | remove |
| `body_weight` | Body weight | select | default/400–700 | default | D+P | 💾 | default×42 | never set | remove |
| `cta_text` | CTA label (default "Shop now") | text | — | **Shop now** (Shop Now) | D+P | content | 35 custom | all explicit | keep |
| `cta_link_target` | CTA link (default #variants) | select | custom, #buy, #variants, #knock-socks, #reviews, #guarantee, #never-loses-grip, #one-pair, #coperni, #problem, (#shop is stored ×2 but not in options, so verify) | **#variants** (custom) | D+P | 💾 | #variants 14, #buy 12, custom 10, #reviews 4, #shop 2 | all explicit; see the defaults note | keep |
| `cta_url` | Custom CTA URL | text | — | — | D+P | content | 10 | none | keep |
| `cta_size`, `cta_style` | CTA size / style | select | — | default / solid | D+P | 💾 | never set | none | remove |
| `cta_bg_color`, `cta_border_color`, `cta_text_color` | CTA colours | color | — | brand rust / white | D+P | ✅ | never set | hardcode | remove |
| `show_trust_strip`, `trust_text` | Stars + trust line | checkbox / text | — | off | D+P | 💾 / content | 10 / 9 | none | keep |
| `show_quote_stars` | Quote stars (default on) | checkbox | — | on | D+P | 💾 | on 30, off 12 (off values sit on non-quote instances, so no effect) | none | keep |
| `quote_author`, `quote_meta` | Quote author / description | text | — | — | D+P | content | 2 / 2 | none | keep |
| `quote_italic`, `quote_author_case` | Quote italic / author style | checkbox / select | — | on / uppercase | D+P | ✅ / 💾 | never changed | none | remove |
| `stat_1…3_value/label`, `stat_3_emphasis`, `stat_bar_color`, block `stat` | Stats mode | — | — | — | D+P | — | stats used by 0 instances (`stat_3_emphasis=false` ×3 has no effect) | none | remove |
| `anchor_id`, `aria_label` | Anchor ID / accessibility name | text | — | — | — | content | 7 / 5 | none | keep |

**Count after the PR:** 76 current controls → about 40 kept, 7 added (`text_pad_top`, `text_pad_bottom`, `text_pad_x_mobile`, `bg_style`, `focal_mobile_custom`, `focal_x_mobile`, `focal_y_mobile`, plus optional `mobile_media_width`), the rest removed. Every removal is dead or never changed, except `image_asset` (pending approval) and the merged `image_position` / `vertical_padding` / `bg_color` (values migrated).

## Implementation checklist (for the later, separately approved PR)
1. Pull the 15 templates from draft `187144929571` (pull only). Diff them against `c0c0564` and re-run this spec's numbers.
2. Template JSON migration first: write explicit values (bg white on product/sock-era, 88/88 pads on 3 apparel, focal 50/50 on R1 instances unless Andrew says otherwise, new `bg_style` / `text_pad_top` / `text_pad_bottom` from old keys).
3. Schema and Liquid changes. Dual-write the new range/select values in `{% style %}`. Keep the PDP overrides (R4) and the phone-fit `center top` rule (R2).
4. Pull-verify plus before/after screenshots of all 42 instances at desktop and 390px; pixel diff must be zero.
5. One section per PR. No other sections touched.

## Instances with non-default values to preserve (all 42)
Values Andrew set by hand (focal, heights, pads, backgrounds, order, fit). Every value below must render the same after migration. *Inert* focal values are flagged in R1.

| Instance (template : section key) | Non-default layout/visual values to preserve (git c0c0564) |
|---|---|
| `collection.apparel` : `fifty-fifty-tees` | reverse=True, mobile_stack_order=copy_first, bg_color=#faf8f6, vertical_padding=(implicit 88) |
| `collection.apparel` : `fifty-fifty-think-outside` | media_bg=#faf8f6, mobile_stack_order=copy_first, bg_color=#faf8f6, vertical_padding=(implicit 88) |
| `collection.apparel` : `fifty-fifty-leggings` | media_bg=#faf8f6, mobile_stack_order=copy_first, bg_color=#faf8f6, vertical_padding=(implicit 88) |
| `collection.hot-kits` : `fifty-fifty-kit-idea` | — |
| `collection` : `fifty-fifty-disciplines` (disabled) | media_bg=#faf8f6, bg_color=#faf8f6, section_gap_mobile=24 |
| `collection` : `fifty-fifty-grip` | media_bg=#f9f9f9, section_gap_mobile=24 |
| `index` : `fifty-fifty-grip` | media_bg=#f9f9f9, min_height=620, text_pad_top_mobile=32, text_pad_bottom_mobile=32, media_aspect=square, reverse=True, bg_color=#faf8f6 |
| `index` : `fifty-fifty-one-pair` | focal_x=100, media_bg=#f9f9f9, min_height=620, media_column_pct=54, text_pad_top_mobile=32, text_pad_bottom_mobile=32 |
| `page.best-grippy-socks` : `outgrew` | media_fit=fit, media_bg=#f9f9f9, min_height=640, bg_color=#faf8f6, section_gap_mobile=24 |
| `page.best-grippy-socks` : `upgrade` | media_bg=#f9f9f9, min_height=640, reverse=True, bg_color=#faf8f6, section_gap_mobile=24 |
| `product.coperni` : `fifty-fifty-sock-era` | column_gap=64, vertical_padding=80, bg_color=#faf8f6, section_gap=0 |
| `product.coperni` : `fifty-fifty-lifestyle` | image_fit_mobile=fit, image_position=custom, mobile_media_height=400, column_gap=56, vertical_padding=80, section_gap=0 |
| `product.coperni` : `fifty-fifty-commit` | focal_y=40, reverse=True, vertical_padding=80, bg_color=#faf8f6, section_gap=0 |
| `product.in-studio-template` : `fifty-fifty-sock-era` | media_bg=#3a7eb8, text_pad_top_mobile=32, show_trust_strip=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.in-studio-template` : `fifty-fifty-lifestyle` | focal_y=72, mobile_media_height=360, show_trust_strip=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.in-studio-template` : `fifty-fifty-commit` | media_bg=#1565c0, text_pad_top_mobile=32, show_trust_strip=True, reverse=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.in-studio-template` : `fifty-fifty-numbers` | media_bg=#f0a12a, text_pad_top_mobile=32, show_trust_strip=True, vertical_padding=80 |
| `product.in-studio-template` : `fifty-fifty-tired-socks` | text_pad_top_mobile=32, show_trust_strip=True, reverse=True, vertical_padding=80 |
| `product` : `fifty-fifty-sock-era` | vertical_padding=80, bg_color=(implicit #ffffff) |
| `product` : `fifty-fifty-lifestyle` | image_position=custom, focal_y=85, content_style=quote, vertical_padding=80, bg_color=#faf8f6 |
| `product` : `fifty-fifty-commit` | reverse=True, vertical_padding=80, bg_color=#faf8f6 |
| `product` : `fifty-fifty-numbers` | vertical_padding=80 |
| `product.one-off-closed` : `fifty-fifty-lifestyle` | image_position=custom, focal_y=85, vertical_padding=80, bg_color=#faf8f6 |
| `product.one-off-closed` : `fifty-fifty-commit` | reverse=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.one-off-closed` : `fifty-fifty-numbers` | image_position=custom, focal_y=85, vertical_padding=80, bg_color=#faf8f6 |
| `product.one-off-open` : `fifty-fifty-lifestyle` | image_position=custom, focal_y=85, vertical_padding=80, bg_color=#faf8f6 |
| `product.one-off-open` : `fifty-fifty-commit` | reverse=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.one-off-open` : `fifty-fifty-numbers` | image_position=custom, focal_y=85, vertical_padding=80, bg_color=#faf8f6 |
| `product.open-sole` : `fifty-fifty-sock-era` | media_bg=#3a7eb8, text_pad_top_mobile=32, show_trust_strip=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.open-sole` : `fifty-fifty-lifestyle` | focal_y=72, mobile_media_height=360, show_trust_strip=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.open-sole` : `fifty-fifty-commit` | media_bg=#1565c0, text_pad_top_mobile=32, show_trust_strip=True, reverse=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.open-sole` : `fifty-fifty-numbers` | media_bg=#f0a12a, text_pad_top_mobile=32, show_trust_strip=True, vertical_padding=80 |
| `product.open-sole` : `fifty-fifty-tired-socks` | text_pad_top_mobile=32, show_trust_strip=True, reverse=True, vertical_padding=80 |
| `product.outdoor` : `fifty-fifty-lifestyle` | image_position=custom, media_bg=#efe9dd, content_style=quote, vertical_padding=80, bg_color=#faf8f6 |
| `product.outdoor` : `fifty-fifty-commit` | image_position=custom, focal_x=38, media_bg=#efe9dd, reverse=True, vertical_padding=80, bg_color=#faf8f6 |
| `product.outdoor` : `fifty-fifty-numbers` | image_position=custom, focal_y=78, media_bg=#faf8f6, vertical_padding=80 |
| `product.outdoor` : `fifty-fifty-barefoot` | image_position=custom, focal_y=40, media_bg=#efe9dd, vertical_padding=80 |
| `product.outdoor` : `fifty-fifty-outdoor-works` | image_position=custom, media_bg=#efe9dd, reverse=True, vertical_padding=80 |
| `product.v-neck-tops` : `fifty-fifty-tees` | reverse=True, mobile_stack_order=copy_first, bg_color=#faf8f6 |
| `product.v-neck-tops` : `fifty-fifty-leggings` | media_bg=#faf8f6, mobile_stack_order=copy_first, bg_color=#faf8f6 |
| `product.yoga-pants` : `fifty-fifty-leggings` | media_bg=#faf8f6, mobile_stack_order=copy_first, bg_color=#faf8f6 |
| `product.yoga-pants` : `fifty-fifty-tees` | reverse=True, mobile_stack_order=copy_first, bg_color=#faf8f6 |
