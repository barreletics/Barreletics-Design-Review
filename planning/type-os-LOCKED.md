# Type OS — owner + agent guide

**Status:** SETTLED — Closed phone QC LOCKED 2026-09-08 did **not** change Type OS  
**Code source:** `shopify-build/assets/design-tokens.css`  
**Deep spec:** `planning/m4-type-hierarchy.md`  
**Visual mock:** `docs/type-os-specimen.html`

**Layout vs type (2026-09-08):** Closed 50/50 phone pad **104/104** is section pad, not a type size and not `--gap-a/b/c`. Roles stay Display on 50/50 · Supporting on features · buy lede 34–44 / 400.

---

## One rule

**Weight falls as size rises.** Big type = lighter weight. Small type = can be bolder.

---

## Locked roles (Roboto unless noted)

| Role | Weight | Size | Where |
|------|--------|------|--------|
| **Hero** | 700 | 50–72px | Home hero only |
| **Big 50/50 title** | **400** | **38–52px** | All `fifty-fifty` with `heading_register: display` (locked 2026-09-10; CSS fallback 400) |
| **Section title** | 600 | 26–32px | Variant grid, wayfinding headings |
| **Statement band** | 500 | 28–36px | TRANSFORM / `fullbleed-statement` |
| **Features block title** | 400 | 28–40px | `pdp-features` main title |
| **Feature row name** | 700 | 26px | Each grip feature label |
| **Body** | 400 | 16px | 50/50 body, FAQ answers, most blurbs |
| **Lede** | 400 | 17px | Reviews header, some intros |
| **Label / eyebrow** | 600 | 11px caps | Eyebrows, small UI labels |
| **Trust strip** | 500 | 12px | Value strip under ATC |

---

## Section → type map (PDP body)

| Section | Title type | Body type |
|---------|------------|-----------|
| `fifty-fifty` (display) | Big 50/50 · 500 · 38–52px | Body · 400 · 16px |
| `fifty-fifty` **quote** | **Pending** — now Cormorant 400 italic 28px | See specimen A vs B |
| `pdp-features` | Features title · 400 · 28–40px | Body · 400 · 16px |
| `disciplines` | Label · 500 · 12–14px | — |
| `variant-grid` | Section · 600 · 26–32px | Body · 400 · 16px |
| `fullbleed-statement` | Statement · 500 · 28–36px | Body · 400 · 16px (if any) |
| `pdp-sock-math` | **LOCKED 56 / 400** (editorial One pair. Done.) | Body · 14–16px |
| `guarantee-band` | Point · 700 · 14px | Body · 400 · 16px |
| `social-proof` / reviews | Lede · 400 · 17px | Quote · 400 · 14–20px |
| `collection-faq` | Question · 600 · 16px | Answer · 400 · 16px |
| `coperni-crosslink` | **See Coperni row below** | Georgia italic subhead |
| `coperni-pdp-story` | Big 50/50 elsewhere | Body 400 · quote Georgia italic |

---

## Do not unify

| Surface | Type | Why |
|---------|------|-----|
| **Buy-box lede** | Roboto 400 · 30–40px | Product column — own lane |
| **Buy-box desc** | Roboto 400 · 14px | Short, under price |
| **Nav / footer / CTA** | Separate UI tokens | Not page body story type |

---

## Coperni (pending lock)

| Line | Current | Target |
|------|---------|--------|
| Banner title | Roboto 500 · 38–52px (matches 50/50) | **Approve 500** or **switch to 400** |
| Banner subhead | Georgia 400 italic · 14–19px | Keep italic or match body? |
| Story quote | Georgia 400 italic · 22–30px | Keep or Roboto? |
| Runway note | Georgia 400 italic · 19px | Keep or Roboto? |
| 50/50 blocks on Coperni PDP | Same as Closed | **Locked — no change** |

---

## Quote 50/50 (pending lock)

Closed PDP Kimberly block (`content_style: quote`).

| Option | Type | Feel |
|--------|------|------|
| **A — now** | Cormorant Garamond · 400 · italic · 28px | Fashion quote — different from other 50/50s |
| **B — match** | Roboto · 500 · straight · 38–52px | Same as “Never loses shape.” |

**Do not change Liquid until Andrew says `keep A` or `switch to B`.**

---

## Agent rules

1. **Never** change buy-box lede to match 50/50 titles.
2. **Never** use Georgia / italic on new pages unless Coperni-style exception is approved.
3. **Never** use weight 700 on big display titles (hero excepted).
4. New 50/50 sections: `heading_register: display` · body one short line · no repeat phrases on same page.
5. Copy changes only in JSON TE — type changes in `design-tokens.css` + section CSS with owner letter.

---

## Sign-off checklist

- [ ] Andrew reviewed `docs/type-os-specimen.html`
- [ ] Coperni banner weight picked (500 vs 400)
- [ ] Coperni Georgia italics — keep or kill
- [ ] Quote 50/50 — keep A (Cormorant italic) or switch to B (Roboto)
- [ ] Update this file status to **LOCKED** + date
- [ ] Add row to `planning/m4-section-freeze.md` if needed

## Locked — Sock Math / One pair. Done. (2026-09-10)

**Status:** LOCKED on draft QA `187144929571` · Design System default for `pdp-sock-math` editorial

| Token | Value | Notes |
|-------|--------|--------|
| Title size | **56px** | Statement section — unique beat, louder via size |
| Title weight | **400** | Big type stays light (Type OS) |
| Role | Display statement | Not the same as Features / Obsession |

### Do not

- Match **Obsession / `pdp-features`** to 56 — Features stays Supporting (~40 / 400)
- Bump weight to 500–700 when sizing up
- Jump to home-hero 64–72 on PDP

### Code

- Schema defaults: `sections/pdp-sock-math.liquid` → `title_size` 56, `title_weight` 400
- CSS: editorial headline uses `--sm-title-size` / `--sm-title-weight` (desk + phone)

### Features / Obsession (unchanged)

| Token | Value |
|-------|--------|
| Eyebrow | Why Barreletics |
| Title | Built around one obsession: **Grip.** |
| Title type | Supporting · **400** · ~28–40px |

## Locked — PDP Features / Obsession title (2026-09-10)

**Status:** LOCKED with sock-math at same scale for studio PDPs (draft QA)

| Token | Value | Notes |
|-------|--------|--------|
| Title size | **56px** | Matches One pair. Done. statement scale |
| Title weight | **400** | Big type stays light |
| Eyebrow (studio) | Why Barreletics | Not “Welcome to a new category” on this block |
| Punch `Grip.` | roman, inherit size/ink | No italic / no grey |
| One-offs | Keep “Same grip system…” copy; type 56/400 | |
| Outdoor | Own copy + own reviews | Do not paste studio featured quote |

Schema defaults: `sections/pdp-features.liquid` → title_size 56, title_weight 400.

## Locked — Fifty-fifty display weight (2026-09-10)

PDP `fifty-fifty` display titles = **weight 400** (not 500). Schema/CSS default 400. Footprint **560 / 550**, scale **100**, COVER preferred.

Quote-only 50/50s on Coperni/one-offs converted to slogan lead (**Grip isn’t optional.**) + quote in body — do not ship orphan quote-as-title blocks.
