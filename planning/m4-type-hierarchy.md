# M4 Type Hierarchy — Type OS v2

**Date:** 2026-07-29  
**Status:** TYPE-OS-v2 law (supersedes v1 weight ladder)  
**Family:** Roboto only (unchanged)  
**Review surface:** `docs/Barreletics Home - Type OS Preview.html`

---

## Governing rule (HARD)

**Weight falls as size rises.**  
The biggest type on the page must not be the heaviest. Weight densifies *small* type; large type already has presence from scale.

---

## Roles

| Role | Weight | Size | Tracking / LH |
|------|--------|------|---------------|
| **Hero H1** | **700** | `clamp(50px, 6.4vw, 82px)` | −0.028em / 1.06 |
| **H2 Display** (brand) | **500** | `clamp(38px, 4.6vw, 52px)` | −0.028em / 1.10 · measure 15ch |
| **H2 Standard** (wayfinding) | **600** | `clamp(26px, 2.9vw, 32px)` | −0.012em / 1.22 |
| **Statement** | **500** | `clamp(28px, 3vw, 36px)` | −0.022em |
| **Lede / body** | **400** | lede 17px · body 16px | lh 1.60 / 1.72 |
| **Label** | **600** | 11px | 0.08em |

Classes: `.type-hero` · `.h2-display` · `.h2-standard` · `.type-statement` · `.type-body` / `.type-lede` · `.type-label`  
`.em` = `font-weight: 700` — one word per signature headline only (hero, H2 Display, statement). Never on H2 Standard.

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

## Homepage register map

| Section | Register | Example |
|---------|----------|---------|
| `split-hero` | Hero | *The Pilates Sock Era is Over* |
| `fifty-fifty` problem / grip / sock-math | **H2 Display** | *Yoga socks are useless.* |
| `fifty-fifty` Coperni | **H2 Standard** | *Barreletics × Coperni* |
| `variant-grid` | **H2 Standard** | *Shop all styles & colors* |
| `social-proof` | **H2 Standard** | *Real people. Real results.* |
| `statement-band` / `guarantee-band` | Statement | dark-band tier 1 |
| `home-ugc` / `newsletter` | **H2 Standard** | *@barreletics* · *10% off…* |

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

--fs-hero:        clamp(50px, 6.4vw, 82px);
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

## Files

- `shopify-build/assets/design-tokens.css`
- `shopify-build/assets/barreletics-base.css`
- Homepage sections + `templates/index.json`
- `docs/Barreletics Home - Type OS Preview.html`
