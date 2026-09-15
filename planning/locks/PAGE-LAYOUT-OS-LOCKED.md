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
| **fullbleed** | `fullbleed-statement` | Commit / image beat | COVER · vh/pct height (~900 desk / ~439 phone @52) — not 50/50 mmh |
| **statement** | `statement-band` | Text band (Knock socks) | Text height only · Type Statement role |
| **reviews** | `pdp-reviews` | Quote-led | Own card stack · no aggregate count on Home |
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
| Fullbleed | COVER | ~900 (=100vh @900) | ~439 (~52) | Not a 50/50 |
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
- [ ] press-feature (Interni): stay press-feature type; when enlarging, adopt FF mobile visual frame
- [ ] Phone text min-height mobile_text_height 520 (image≈text) on ALL Home fifty-fifty
- [ ] Hero stays 92vh / 62/38 if touching Home hero
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

`press-feature-interni` stays **`press-feature`**. When Andrew asks to enlarge Interni to the marketing split look, adopt the **same mobile visual frame** as fifty-fifty (520/520 · center · 32/32 · COVER · scale 100 · body 16). Do **not** retarget the section type to `fifty-fifty`.

## Do not

- Use FIT on any Home fifty-fifty (height becomes a no-op)
- Reintroduce asymmetric phone pads **32/96** on marketing split frame
- Touch PDP `product*.json` / `fifty_fifty_lifestyle` 560/550
- Push live theme
- Invent a third Home 50/50 height family
- Convert Interni to `fifty-fifty` just to share the visual frame
