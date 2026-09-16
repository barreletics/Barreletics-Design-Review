# Page Layout OS — LOCKED 2026-09-15

**Andrew GO.** Coffee-blurt. No marketplace apps.  
**Source measure:** `planning/home-5050-enlarge-diag-2026-09-15/measure.json` (draft `187144929571`)  
**Machine lock:** `sitewide.lock.json` → `page_layout_os`  
**Family:** **Home / marketing page layout** — separate from PDP `fifty_fifty_lifestyle` **560 / 550**. Do not unify.

## Law (one line)

**Name the section family first.** Then apply that family’s ruler. Marketing **split media+text** visual frame = **COVER · desk 860 · phone 520/520 · center · pads 32/32 · body 16 · scale 100**. Desk **860 / 88 / 88 / 64** stays frozen on mobile passes. **FIT forbidden** on Home fifty-fifty. **Asymmetric 32/96 rejected.**

## Step 0 — Name the family (mandatory)

Before any pad / height / fit edit:

1. Name the **page** (Home, Collection, PDP, …).
2. Name the **section family** from the table below — not a neighbor, not “that tall block.”
3. Apply **only** that family’s ruler. Never borrow FF numbers onto collab / fullbleed / statement / reviews / problem unless the letter says so.

## Families (Home / marketing spine)

| Family | Section type(s) | Layout role | Visual frame / guidance |
| --- | --- | --- | --- |
| **fifty-fifty** | `fifty-fifty` | Split media+text story | **Marketing split frame** (below) — REQUIRED |
| **press-feature** | `press-feature` | Press / editorial stack (media→copy) | Own type. When Andrew enlarges to match marketing split look, adopt the **same mobile visual frame** as FF (520/520 · center · 32/32 · COVER · scale 100 · body 16) — **stay `press-feature` type** (do not convert to `fifty-fifty`). Interni is the Home instance. |
| **collab-hero** | `collab-hero` | Campaign stage | Stage ~**105vh** desk guidance · own lane — not a 50/50 |
| **fullbleed** | `fullbleed-statement` | **Image-only** beat (Commit overlay **LOCKED OFF**) | COVER · vh/pct (~900 desk / ~439 phone @52) — **no title/CTA on image** — not 50/50 mmh |
| **statement** | `statement-band` | Text band (Knock socks) | Text height only · Type Statement role |
| **reviews** | `pdp-reviews` | Quote-led | Home **desk: all 6** curated text cards; Home **phone: 2 + See more** (mobile-only hide). No aggregate on Home. |
| **problem-section** | `problem-section` | Problem / × list band | Text-list family · not FF |

Also on Home (not in the split-frame set): `split-hero` (62/38 · **92vh** desk), `disciplines` + `variant-grid`, `home-juicer`, `guarantee-band`.

Other marketing pages: map each block into one of these families. Same numbers. **Do not invent a FIT Home 50/50 family.**

## Marketing split media+text visual frame (locked)

Applies to every Home/marketing **`fifty-fifty`**. Also the target frame when Andrew enlarges a **`press-feature`** (Interni) to match — type stays press-feature.

Viewport rulers: **desktop 1280×900** · **mobile 390×844**.

| Axis | Desktop | Mobile |
| --- | --- | --- |
| Media height | **860** | **520** |
| Text column min-height | desk stretch | **520** (`mobile_text_height` — image≈text) |
| Justify / alignment | — | **center** (offset 0) |
| Text pad T / B | **88 / 88** | **32 / 32** (symmetric) |
| Side pad | **64 / 64** | **20 / 20** (measured) |
| Body | **16** | **16** |
| Image fit | **COVER** | **COVER** |
| Image scale | **100** | **100** |

**Frozen on mobile passes:** desk **860 / vertical 88 / 88 / side 64** — do not reopen desk numbers while tuning phone.

JSON keys: `media_fit: cover`, `image_fit_mobile: cover`, `min_height: 860`, `mobile_media_height: 520`, `mobile_text_height: 520`, `image_scale: 100`, `vertical_padding: 88`, `side_padding: 64`, `text_pad_top_mobile: 32`, `text_pad_bottom_mobile: 32`, `body_size: "16"`.

### Rejected / forbidden

| Rule | Status |
| --- | --- |
| Asymmetric phone text pads **32 / 96** | **REJECTED** — use **32 / 32** center |
| **FIT** on Home `fifty-fifty` | **FORBIDDEN** — FIT makes height a no-op (One Pair was FIT; converted) |
| Inventing a third Home 50/50 height family | Forbidden |
| Copying PDP **560 / 550** / **96 / 96** onto Home | Forbidden |

### PDP contrast (do not touch)

| Family | Desk min | Phone COVER mmh | Phone text pad |
| --- | --- | --- | --- |
| **PDP** `fifty_fifty_lifestyle` | **560** | **550** | **96 / 96** |
| **Home / marketing** `page_layout_os` split frame | **860** | **520** | **32 / 32** |

Never “fix Home by copying PDP” or the reverse.

## Other media heights (non-split families)

| Block | Mode | Desktop | Mobile | Notes |
| --- | --- | --- | --- | --- |
| Hero (`split-hero`) | COVER frame | **92vh** | media content stack | Do **not** swap to photo-aspect / 110 / invent px |
| Collab | stage | **105vh** guidance | own lane | Not a 50/50 |
| Fullbleed | COVER · **image-only** | ~900 (=100vh @900) | ~439 (~52) | Overlay `show_text` **false** — Commit+Shop CTA on image **REJECTED 2026-09-15** |
| Statement / problem / reviews | text / cards | own | own | No FF media-height claim |

## COVER vs FIT

| | COVER | FIT |
| --- | --- | --- |
| Frame | Height **is** the lock (860/520 Home) | Height **is not** a lock — media sizes to asset |
| Image | Fills box · may crop | Whole asset visible · may letterbox |
| **Home 50/50** | **REQUIRED** | **FORBIDDEN** |
| PDP | Lifestyle 560/550 | Packshot exception — separate letter |

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

Full Type OS: `planning/type-os-LOCKED.md`. Layout OS pins **body 16** on split-frame text.

## 30-second apply checklist (ANY marketing page)

```
PAGE LAYOUT OS GATE
- [ ] Named the page + section FAMILY first (fifty-fifty / press-feature / collab-hero / fullbleed / statement / reviews / problem-section)
- [ ] Family: Home/marketing OR PDP — never mix 860/520 with 560/550
- [ ] Marketing split (fifty-fifty)? → COVER 860/520 · center · pads 32/32 · scale 100 · body 16 · FIT forbidden
- [ ] Desk 860/88/88/64 frozen when this is a mobile-only pass
- [ ] Asymmetric 32/96 rejected
- [ ] press-feature (Interni): stay press-feature type; frame 640/640 · 32/32 center; clamp overflow; FIT/contain only via Andrew media QC option C (not Home fifty-fifty)
- [ ] Home reviews: desk all 6; phone 2 + See more (mobile-only `[hidden]`; desk never truncated)
- [ ] Phone text min-height mobile_text_height 520 (image≈text) on ALL Home fifty-fifty
- [ ] Hero stays 92vh / 62/38 if touching Home hero
- [ ] fullbleed-statement: show_text **false** + blank title/body/cta (Commit overlay LOCKED OFF — Andrew 2026-09-15)
- [ ] Never restore overlay copy without **explicit Andrew go**
- [ ] Never thrash unrelated sections when editing Interni (and vice versa)
- [ ] Draft theme only 187144929571 — never live
- [ ] Prove gate below before "done" — MANDATORY
```

## Prove gate (MANDATORY)

No “done” without all of:

1. **Pull-verify** — after any JSON/Liquid push: pull the named file(s) back; confirm keys match this letter.  
2. **Measure draft preview** — run `planning/home-5050-enlarge-diag-2026-09-15/measure-home-5050.mjs` against `?preview_theme_id=187144929571`.  
3. Pass only if:
   - **Every** Home fifty-fifty COVER mediaH ≈ **860** desk / **520** phone (±2px)
   - Pads match ruler (desk **88/88 · 64**; phone **32/32** center — not 32/96)
   - Body font-size **16px** on 50/50 text
   - Phone text boxes equal via `mobile_text_height` **520** (±2px; image≈text; centered)
   - No Home fifty-fifty still on FIT
4. **Visual prove** non-FF families touched (press / collab / fullbleed / statement / reviews / problem) — do not stop at FF measure-JSON alone.  
5. lock-scan: `python3 scripts/lock-scan.py .` — Home keys under scan key `page_layout_os` must OK; PDP 560/550 still OK.

## Scan key

`sitewide.lock.json` → **`page_layout_os`**  
Scanner: `scripts/lock-scan.py` → `scan_page_layout_os` (Home `index.json` only).  
Humans/agents: every Home `fifty-fifty` must be COVER + 860/520 + **32/32** center pads + body 16.

## Interni note

`press-feature-interni` stays **`press-feature`**. Mobile visual frame: **490 / 490 · center · 32/32 · body 16 · COVER** (aspect-matched Chat editorial; prior 640 FIT exception superseded) via section settings (`mobile_media_height` / `mobile_text_height` / equal text pads) — type remains `press-feature` (do **not** convert to `fifty-fifty`). TE can retune the knobs; Home Interni JSON locks the OS defaults.

**No overflow / no blow-up:** media + img must stay **inside** the 640 frame — `overflow: hidden`, `width/height/max-width/max-height: 100%`, `transform: none` (no scale>100). Do **not** enlarge frame further to “fix” a zoomed crop.

### Andrew-approved FIT exception (media QC option C) — 2026-09-15

Root cause: COVER + tall **640** frame on a **wide/square flat-lay** side-cropped INTERNI/ZINE masthead.

| Axis | Value |
| --- | --- |
| `image_fit_mobile` (desk uses same setting on this section) | **`contain`** (FIT / letterbox) |
| Media / text height | **490 / 490** (aspect match; 640 FIT exception superseded) |
| Pads / justify | **32 / 32 · center** kept |
| `media_bg_color` | **`#F4EEE5`** cream — letterbox matches section |
| Scope | **Interni `press-feature` only** — Grip / One Pair stay **COVER** |
| Home `fifty-fifty` FIT | Still **FORBIDDEN** |

**Media QC gate options** when COVER crops the required subject: (A) swap asset · (B) reframe/crop asset · **(C) Andrew-approved FIT/contain exception** (this letter). Never invent FIT as default on Home fifty-fifty.

## Home reviews ruler

Home `reviews` (`pdp-reviews` on `index.json`): **desk `text_cards_initial: 0` (all 6)**; **phone `text_cards_initial_mobile: 2`** + **`text_cards_expand: true`**. Mobile extras use `hidden` + `display:none !important` ≤768 only; desk always shows all cards. Measure phone: 2 + See more; desk: 6 visible, no See more.


## Fullbleed Commit overlay — LOCKED OFF (2026-09-15)

**Andrew rejection:** “You commit to the class” + Shop CTA **on the image** must stop. Do not revert to overlay.

| Axis | Value |
| --- | --- |
| Section | `fullbleed-statement` |
| Mode | **Image-only** |
| `show_text` | **`false`** |
| `show_overlay` | **`false`** |
| `mobile_full_bleed` | **`true`** (keeps ~52vh; without it phone-photo collapses H→0) |
| `title` / `body` / `cta_text` | **blank** |
| Media | Keep coral shoe `IMG_2917` (or current approved asset) — no burned-in Commit copy |
| Re-enable overlay? | **Only with explicit Andrew go** — never from punch-list P0 nostalgia (`71200de` wrongly restored) |

**History:** Punch-list P0 (empty overlay → “restore Commit”) conflicted with Andrew’s image-only intent. `71200de` restored title+Shop Now. **2026-09-15 Andrew angry: remove from image.** Lock holds image-only.

Scan: `fullbleed_guidance.mode = image_only` in `sitewide.lock.json`; `lock-scan` asserts blank overlay fields.

## Interni edit hygiene

- Chat Interni editorial art only (`barreletics-interni-chatgpt-editorial-clean`).
- **No Commit strings** in Interni settings or PNG.
- When editing Interni: **do not** touch fullbleed / Grip / One Pair.
- When editing fullbleed: **do not** touch Interni / Grip / One Pair.

## Do not

- Use FIT on any Home fifty-fifty (height becomes a no-op)
- Reintroduce asymmetric phone pads **32/96** on marketing split frame
- Touch PDP `product*.json` / `fifty_fifty_lifestyle` 560/550
- Push live theme
- Invent a third Home 50/50 height family
- Convert Interni to `fifty-fifty` just to share the visual frame
- Restore Commit / Shop CTA overlay on `fullbleed-statement` without explicit Andrew go
- Put Commit strings on Interni settings or bake them into Interni PNG
- Thrash Grip / One Pair / Interni when the ticket is fullbleed (or the reverse)
