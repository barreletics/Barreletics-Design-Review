# Page Layout OS — LOCKED 2026-09-15

**Andrew GO.** Coffee-blurt. No marketplace apps.  
**Source measure:** `planning/home-5050-enlarge-diag-2026-09-15/measure.json` (draft `187144929571`, measured 2026-09-15)  
**Machine lock:** `sitewide.lock.json` → `page_layout_os`  
**Family:** **Home / marketing page layout** — separate from PDP `fifty_fifty_lifestyle` **560 / 550**. Do not unify.

## Law (one line)

Home COVER 50/50 = **Grip 860 desk / 520 phone**. Pads follow **One Pair ruler**. Body **16**. FIT **ignores height** — never claim a media height on FIT.

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
| Math / FIT 50/50 | `fifty-fifty` (One Pair) | **FIT** · pads = ruler · **height not locked** |
| UGC | `home-juicer` | From the studio |
| Close | `guarantee-band` | Sitewide guarantee lock (Display + H3 columns) |

Other pages: map each block into hero / 50/50 COVER / 50/50 FIT / fullbleed / statement / reviews / juicer / guarantee. Same numbers. Do not invent a third 50/50 family.

## Size table (locked from measure)

Viewport rulers: **desktop 1280×900** · **mobile 390×844**.

### Media heights

| Block | Mode | Desktop | Mobile | Notes |
| --- | --- | --- | --- | --- |
| Hero (`split-hero`) | COVER frame | **92vh** (measured ~972 @ scale 1.08) | media ~658 (content stack) | Do **not** swap to photo-aspect / 110 / invent px |
| Grip 50/50 | **COVER** | **860** | **520** | `--ff-min-height` / `--ff-mobile-media-height` |
| One Pair 50/50 | **FIT** | *(ignore)* measured ~853 | *(ignore)* measured ~520 | Settings may show 720/640 — **FIT collapses**; do not QC to those px |
| Collab | stage | **105vh** guidance | ~78 setting / measured media ~658 | Own lane |
| Fullbleed | COVER | ~900 (=100vh @900) | ~439 (~52) | Not a 50/50 |
| Statement band | text | ~371 | ~317 | No media height claim |

### Pads + type (50/50 text — One Pair ruler)

| Axis | Desktop | Mobile |
| --- | --- | --- |
| Text pad T / B | **88 / 88** | **32 / 96** |
| Side pad | **64 / 64** | **20 / 20** (measured) |
| Body | **16** | **16** |
| Display title | Type OS Big 50/50 (38–52 / 400) | same ladder |

JSON keys (Home COVER Grip today): `vertical_padding: 88`, `side_padding: 64`, `text_pad_top_mobile: 32`, set `text_pad_bottom_mobile: 96` when bottom must not mirror top. `body_size` → **16** (or `default` only if Liquid resolves to 16px — prove in measure).

### PDP contrast (do not touch)

| Family | Desk min | Phone COVER mmh | Phone text pad |
| --- | --- | --- | --- |
| **PDP** `fifty_fifty_lifestyle` | **560** | **550** | **96 / 96** |
| **Home** `page_layout_os` | **860** (COVER Grip) | **520** | **32 / 96** |

Never “fix Home by copying PDP” or the reverse.

## COVER vs FIT

| | COVER | FIT |
| --- | --- | --- |
| Frame | Height **is** the lock (860/520 Home Grip) | Height **is not** a lock — media sizes to asset |
| Image | Fills box · may crop | Whole asset visible · may letterbox |
| Home | Grip / lifestyle story | One Pair pack / product-in-frame |
| PDP | Lifestyle 560/550 | Packshot exception ~400 phone — separate letter |
| Agent sin | Claiming FIT “should be 640 tall” because JSON says so | Flipping COVER→FIT to dodge crop without letter |

**Rule:** If `media_fit` / `image_fit(_mobile)` is **fit** → do not assert `min_height` or `mobile_media_height` in QA copy. Measure asset height; pads still apply.

## Text type ladder (page body)

| Role | Size | Where |
| --- | --- | --- |
| Hero | 50–72 / 700 | Home hero only |
| Big 50/50 | 38–52 / 400 | `heading_register: display` |
| Statement | 28–36 / 500 | statement / fullbleed heads |
| Body | **16 / 400** | **All 50/50 body copy** |
| Lede | 17 / 400 | Reviews intros |
| Eyebrow | 11 / 600 | Labels |

Full Type OS: `planning/type-os-LOCKED.md`. Layout OS does not rewrite type — it only pins **body 16** on 50/50 text.

## 30-second apply checklist (ANY page including Home)

```
PAGE LAYOUT OS GATE
- [ ] Named the page + section (not a neighbor)
- [ ] Family: Home/marketing OR PDP — never mix 860/520 with 560/550
- [ ] COVER? → set desk/phone media heights from this letter
- [ ] FIT? → pads only; I will NOT claim media height
- [ ] Pads = One Pair ruler (88/88 · 64 · phone 32/96 · side ~20)
- [ ] Body 16 on 50/50 text
- [ ] Hero stays 92vh / 62/38 if touching Home hero
- [ ] Draft theme only 187144929571 — never live
- [ ] Prove gate below before "done"
```

## Prove gate (required)

1. **Pull-verify** — after any JSON/Liquid push: pull the named file(s) back; confirm keys match this letter.  
2. **Measure draft preview** — run / reuse `planning/home-5050-enlarge-diag-2026-09-15/measure-home-5050.mjs` (or equivalent) against `?preview_theme_id=187144929571`.  
3. Pass only if:
   - Grip COVER mediaH ≈ **860** desk / **520** phone (±2px)
   - One Pair pads match ruler; FIT mediaH may differ — OK
   - Body font-size **16px** on 50/50 text
4. lock-scan: `python3 scripts/lock-scan.py .` — Home keys under scan key `page_layout_os` must OK; PDP 560/550 still OK.

## Scan key

`sitewide.lock.json` → **`page_layout_os`**  
Scanner: `scripts/lock-scan.py` → `scan_page_layout_os` (Home `index.json` only).  
Humans/agents: if scanner skipped, manually check Grip `min_height`/`mobile_media_height`/`media_fit` + One Pair `media_fit: fit` + pads.

## Do not

- Push live theme `185687998755`
- Change `product*.json` to Home 860/520
- Regress PDP 560/550 / phone text 96/96
- Claim height on FIT One Pair
- Re-open Closed/Open/Outdoor/Coperni PDP letters

## Evidence

- Measure JSON: `planning/home-5050-enlarge-diag-2026-09-15/measure.json`
- Home JSON (at lock time): Grip COVER 860/520 · One Pair FIT · vertical 88 · side 64 · text_pad_top_mobile 32
