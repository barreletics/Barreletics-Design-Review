# M4 Type Hierarchy — Type OS SETTLED

**Date:** 2026-07-29  
**Status:** **SETTLED** (TYPE-OS-v2 + Display/Standard audit + hero max **72**)  
**Family:** Roboto only (unchanged)  
**Review surface:** `docs/Barreletics Home - Type OS Preview.html` (primary — not Shopify)  
**Authority:** `shopify-build/assets/design-tokens.css`

---

## Governing rule (HARD)

**Weight falls as size rises.**  
The biggest type on the page must not be the heaviest. Weight densifies *small* type; large type already has presence from scale.

---

## Roles

| Role | Weight | Size | Tracking / LH |
|------|--------|------|---------------|
| **Hero H1** | **700** | `clamp(50px, 6.4vw, 72px)` | −0.028em / 1.06 |
| **H2 Display** (brand) | **500** | `clamp(38px, 4.6vw, 52px)` | −0.028em / 1.10 · measure 15ch |
| **H2 Supporting** (compact editorial) | **400** | **40px** (mobile `clamp(28px, 3.5vw, 40px)`) | −0.02em / 1.10 |
| **H2 Standard / Section** (wayfinding) | **600** | `clamp(26px, 2.9vw, 32px)` | −0.012em / 1.22 |
| **Value strip** | **500** | **12px** | 0.08em / uppercase |
| **Statement** | **500** | `clamp(28px, 3vw, 36px)` | −0.022em |
| **Lede / body** | **400** | lede 17px · body 16px | lh 1.60 / 1.72 |
| **Label** | **600** | 11px | 0.08em |

Classes: `.type-hero` · `.h2-display` · `.h2-standard` · `.type-statement` · `.type-body` / `.type-lede` · `.type-label`  
`.em` = `font-weight: 700` — one word per signature headline only (hero, H2 Display, statement). Never on H2 Standard.

---

## QC assignment (LOCKED 2026-09-02 — Collection approved)

**Use this when QCing a page.** Tokens stay in `design-tokens.css`. Do not invent sizes.

| On the page | Type OS role |
|---|---|
| Page-opening H1 | **Hero** (72 / 700) |
| 50/50 / image-led editorial · Home Upgrade | **H2 Display** (52 / 500 / 1.1) |
| Compact editorial (PDP “Built around one obsession: Grip.”) | **H2 Supporting** (40 / 400 / 1.1) |
| Text-only brand statement | **Statement** |
| Functional / wayfinding heading | **H2 Section** (32 / 600 / 1.22) |
| Scan labels | **Value strip** (12 / 500 / uppercase) |
| Body / lede | **Body** |
| Buttons | **Global CTA Type OS** (`--type-cta-*`) |

No arbitrary one-off font sizes or weights. Editorial copy stays sentence case unless there is a deliberate brand reason otherwise.

**Rollout is page-by-page. Do not retrofit the site.**

- **Home is frozen.** Do not touch Home. It is the reference page.
- **PDP:** do not change until we QC that page. Fix only mismatches then.
- **Collection (Shop All):** approved 2026-09-02 on M4 `187144929571`. Keep current Collection type + Hero Shop Now CTA. Knock band `#faf8f6`. 3-row All Variants.

---

## Cadence (HARD)

Only three gaps between eyebrow → headline → body → CTA:

```css
--gap-a: 16px;   /* eyebrow  → headline */
--gap-b: 20px;   /* headline → body/lede */
--gap-c: 32px;   /* body     → CTA */
```

No per-section stack overrides.

---

## Casing law (HARD)

| Role | Casing |
|------|--------|
| **Hero / H2 / statement** | Sentence / brand line |
| **Eyebrows / labels** | Small uppercase only |
| **CTAs / nav** | Quiet uppercase UI |

**Banned:** uppercase on H1/H2/statement · ALL CAPS display · Title Case stacks

---

## Dark bands — max two tiers

| Tier | Role | Spec |
|------|------|------|
| **1** | Statement | statement tokens / `#ffffff` |
| **2** | Support | **16px** / **400** / `#d6d2cb` |

No third text tier (merge points into paragraph or drop one).

---

## Homepage H2 Display vs Standard audit (2026-07-29)

**Rule:** Display = brand/emotion/moment · Standard = shop/navigate/utility. Ambiguous → Standard for shop/utility, Display for brand emotion.

| Section | Title | Register | Why |
|---------|-------|----------|-----|
| `split-hero` | The Pilates Sock Era is Over | **Hero** | Page-opening H1 only |
| `fifty-fifty` problem | Yoga socks are useless. | **Display** | Problem / brand punch |
| `disciplines` | Upgrade your grip. Upgrade your workout. | **Display** | Brand grip slogan on cream band (`.h2-display`; not label/hero) |
| `value-strip` | — | — | No section title |
| `variant-grid` | Shop all styles & colors | **Standard** | Shop wayfinding |
| `fifty-fifty` grip | Never loses shape. Never loses grip. | **Display** | Brand grip moment |
| `fifty-fifty` Coperni | Barreletics × Coperni | **Standard** | Named campaign module / navigate |
| `statement-band` | Let us knock your socks off | **Display** | Home brand slogan. TE `title_role: display`. Not Hero. Other pages stay Statement unless lettered. |
| `social-proof` | Real people. Real results. | **Standard** | Reviews framing / wayfinding |
| `fifty-fifty` sock-math | One pair. Done. | **Display** | Obsession / brand close |
| `home-ugc` | @barreletics | **Standard** | Functional UGC section label |
| `guarantee-band` | Zero risk. All grip. | **Display** (Home only) | Matches knock-socks. PDPs stay Statement (*Built on guarantees…*). TE `title_role`. |
| `geo-section` | Trusted across the country | **Supporting** | Accordion label (eyebrow/H3, not H2) |
| `newsletter` | Join the list | **Standard** | Utility signup framing |

Wiring: `fifty-fifty` uses TE `heading_register` (`display` \| `standard`) → `.h2-display` / `.h2-standard`. `statement-band` + `guarantee-band` use TE `title_role` (`statement` \| `display`). `.em` only on hero / Display / statement — never Standard.

**Forward 2026-08-30 (Andrew: knock-socks + Zero risk felt right at Display):** Type OS **tokens did not change.** Home brand slogans use the existing H2 Display role. Do **not** restyle the site or bump clamps. Hero stays page-opening only.

---

## Final token set

```css
--fw-hero:        700;
--fw-h2-display:  500;
--fw-h2-standard: 600;
--fw-statement:   500;
--fw-body:        400;
--fw-label:       600;
--fw-emphasis:    700;

--fs-hero:        clamp(50px, 6.4vw, 72px);
--fs-h2-display:  clamp(38px, 4.6vw, 52px);
--fs-h2-standard: clamp(26px, 2.9vw, 32px);
--fs-statement:   clamp(28px, 3vw, 36px);
--fs-lede:        17px;
--fs-body:        16px;
--fs-label:       11px;

--ls-hero:        -0.028em;
--ls-h2-display:  -0.028em;
--ls-h2-standard: -0.012em;
--ls-statement:   -0.022em;
--ls-label:        0.08em;

--lh-hero:        1.06;
--lh-h2-display:  1.10;
--lh-h2-standard: 1.22;
--lh-lede:        1.60;
--lh-body:        1.72;

--gap-a: 16px;
--gap-b: 20px;
--gap-c: 32px;
```

Mapped in `shopify-build/assets/design-tokens.css`. Utilities in `barreletics-base.css`.

---

## Scope (sitewide)

Applied to **all** Shopify templates/sections (index, collection, product, page, cart, blog, search, etc.) and **authority** HTML mocks in `docs/`. Historical Definitives (SEO v11–v35, Collection ≤v17, etc.) remain priors — do not treat as type authority.

## Theme Editor (HARD)

Type OS owns family, size, weight, tracking. Sections must **not** add `font_picker` or per-section type sprawl. TE may expose heading *register* (display vs standard) where useful — not font families. Control tiers / schema headers: `planning/m4-te-controls.md`.

## Files

- `shopify-build/assets/design-tokens.css` — tokens (master)
- `shopify-build/assets/barreletics-base.css` — utilities
- All `shopify-build/sections/*.liquid` + `templates/*.json` (class/CSS wiring)
- `docs/Barreletics Home - Type OS Preview.html` — review surface
- Authority mocks: Home WORKING · Collection v18 · SEO v36 · PDP v16 · Journal v5 · Help v3 · Pattern-v2 · FAQ/Contact/Returns/Size/Track
- `planning/m4-te-controls.md` — TE tiers (A/B/C) + Shared/Section schema order
