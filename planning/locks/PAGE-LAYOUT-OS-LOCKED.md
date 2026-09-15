# Page Layout OS — LOCKED 2026-09-15

**Andrew GO.** Coffee-blurt. No marketplace apps.  
**Source measure:** `planning/home-5050-enlarge-diag-2026-09-15/measure.json` (draft `187144929571`)  
**Machine lock:** `sitewide.lock.json` → `page_layout_os`  
**Family:** **Home / marketing page layout** — separate from PDP `fifty_fifty_lifestyle` **560 / 550**. Do not unify.

## Law (one line)

Home fifty-fifty = **always COVER 860 desk / 520 phone**. FIT is **forbidden** on Home 50/50 (FIT makes height a no-op — that caused inconsistency). Pads = **One Pair ruler**. Body **16**. Image scale **100**. Phone text min-height **`mobile_text_height` 520** (image≈text).

## Section architecture (Home spine — apply-same language to any page)

| Beat | Section type | Layout role |
| --- | --- | --- |
| Hero | `split-hero` | 62/38 · desktop frame **92vh** · COVER photo fills frame · trust left |
| Shop open | `disciplines` + `variant-grid` | Wayfinding + shop |
| Story 50/50 COVER | `fifty-fifty` (Grip / Never loses) | Fixed footprint **860 / 520** · COVER · body 16 |
| Campaign | `collab-hero` | Stage ~**105vh** desk guidance · own lane |
| Statement | `statement-band` | Text band (Knock socks) — type Statement role |
| Fullbleed | `fullbleed-statement` | Commit beat · COVER · vh/pct height (not 50/50 mmh) |
| Reviews | `pdp-reviews` | Quote-led · no aggregate count on Home |
| Story 50/50 COVER | `fifty-fifty` (One Pair) | **COVER** (was FIT — converted) · **860 / 520** · pads = ruler · body 16 |
| UGC | `home-juicer` | From the studio |
| Close | `guarantee-band` | Sitewide guarantee lock (Display + H3 columns) |

Other pages: map each block into hero / 50/50 COVER / fullbleed / statement / reviews / juicer / guarantee. Same numbers. **Do not invent a FIT Home 50/50 family.**

## Size table (locked)

Viewport rulers: **desktop 1280×900** · **mobile 390×844**.

### Media heights

| Block | Mode | Desktop | Mobile | Notes |
| --- | --- | --- | --- | --- |
| Hero (`split-hero`) | COVER frame | **92vh** | media content stack | Do **not** swap to photo-aspect / 110 / invent px |
| **Every Home `fifty-fifty`** | **COVER** | **860** | **520** | `--ff-min-height` / `--ff-mobile-media-height` · Grip + One Pair + any future Home 50/50 |
| Collab | stage | **105vh** guidance | own lane | Not a 50/50 |
| Fullbleed | COVER | ~900 (=100vh @900) | ~439 (~52) | Not a 50/50 |
| Statement band | text | text height | text height | No media height claim |

### Pads + type (50/50 text — One Pair ruler)

| Axis | Desktop | Mobile |
| --- | --- | --- |
| Text pad T / B | **88 / 88** | **32 / 96** |
| Side pad | **64 / 64** | **20 / 20** (measured) |
| Body | **16** | **16** |
| Image scale | **100** | **100** |
| Text column min-height | desk stretch | **`mobile_text_height` 520** (image≈text) |
| Display title | Type OS Big 50/50 (38–52 / 400) | same ladder |

JSON keys: `media_fit: cover`, `image_fit_mobile: cover`, `min_height: 860`, `mobile_media_height: 520`, `mobile_text_height: 520`, `image_scale: 100`, `vertical_padding: 88`, `side_padding: 64`, `text_pad_top_mobile: 32`, `text_pad_bottom_mobile: 96`, `body_size: "16"`.

### PDP contrast (do not touch)

| Family | Desk min | Phone COVER mmh | Phone text pad |
| --- | --- | --- | --- |
| **PDP** `fifty_fifty_lifestyle` | **560** | **550** | **96 / 96** |
| **Home** `page_layout_os` | **860** | **520** | **32 / 96** |

Never “fix Home by copying PDP” or the reverse.

## COVER vs FIT

| | COVER | FIT |
| --- | --- | --- |
| Frame | Height **is** the lock (860/520 Home) | Height **is not** a lock — media sizes to asset |
| Image | Fills box · may crop | Whole asset visible · may letterbox |
| **Home 50/50** | **REQUIRED** | **FORBIDDEN** — convert any FIT (One Pair was FIT) |
| PDP | Lifestyle 560/550 | Packshot exception — separate letter |
| Agent sin | Claiming FIT “should be 640 tall” because JSON says so | Leaving FIT on Home 50/50 |

**Rule:** Home `type=fifty-fifty` → always COVER + 860/520. If you see `media_fit: fit` on Home, convert it.

## Text type ladder (page body)

| Role | Size | Where |
| --- | --- | --- |
| Hero | 50–72 / 700 | Home hero only |
| Big 50/50 | 38–52 / 400 | `heading_register: display` |
| Statement | 28–36 / 500 | statement / fullbleed heads |
| Body | **16 / 400** | **All 50/50 body copy** |
| Lede | 17 / 400 | Reviews intros |
| Eyebrow | 11 / 600 | Labels |

Full Type OS: `planning/type-os-LOCKED.md`. Layout OS pins **body 16** on 50/50 text.

## 30-second apply checklist (ANY page including Home)

```
PAGE LAYOUT OS GATE
- [ ] Named the page + section (not a neighbor)
- [ ] Family: Home/marketing OR PDP — never mix 860/520 with 560/550
- [ ] Home fifty-fifty? → COVER 860/520 · scale 100 · FIT forbidden
- [ ] Pads = One Pair ruler (88/88 · 64 · phone 32/96 · side ~20)
- [ ] Phone text min-height `mobile_text_height` **520** (image≈text) on ALL Home 50/50
- [ ] Body 16 on 50/50 text
- [ ] Hero stays 92vh / 62/38 if touching Home hero
- [ ] Draft theme only 187144929571 — never live
- [ ] Prove gate below before "done"
```

## Prove gate (required)

1. **Pull-verify** — after any JSON/Liquid push: pull the named file(s) back; confirm keys match this letter.  
2. **Measure draft preview** — run `planning/home-5050-enlarge-diag-2026-09-15/measure-home-5050.mjs` against `?preview_theme_id=187144929571`.  
3. Pass only if:
   - **Every** Home fifty-fifty COVER mediaH ≈ **860** desk / **520** phone (±2px)
   - Pads match ruler (desk 88/88 · 64; phone 32/96)
   - Body font-size **16px** on 50/50 text
   - Phone text boxes equal via `mobile_text_height` **520** (±2px; image≈text)
   - No Home fifty-fifty still on FIT
4. lock-scan: `python3 scripts/lock-scan.py .` — Home keys under scan key `page_layout_os` must OK; PDP 560/550 still OK.

## Scan key

`sitewide.lock.json` → **`page_layout_os`**  
Scanner: `scripts/lock-scan.py` → `scan_page_layout_os` (Home `index.json` only).  
Humans/agents: every Home `fifty-fifty` must be COVER + 860/520 + One Pair pads + body 16.

## Do not

- Use FIT on any Home fifty-fifty (height becomes a no-op)
- Touch PDP `product*.json` / `fifty_fifty_lifestyle` 560/550
- Push live theme
- Invent a third Home 50/50 height family
