# M4 Type Hierarchy — Type OS (weight ladder)

**Date:** 2026-07-29  
**Status:** Andrew Type OS fix brief — law  
**Family:** Roboto only (unchanged)  
**Review surface:** `docs/Barreletics Home - Type OS Preview.html`

---

## Weight ladder (HARD — highest priority)

| Role | Weight | Size | Tracking / LH |
|------|--------|------|---------------|
| **Hero H1** | **800** | `clamp(48px, 6vw, 76px)` | −0.02em / 1.02 |
| **Section H2** | **700** | `clamp(32px, 3.4vw, 40px)` | −0.01em / 1.2 |
| **Statement** | **600** | `clamp(26px, 2.8vw, 32px)` | −0.01em / 1.2 |
| **Lede / body** | **400** | lede 17px · body 16px | lh 1.55 / 1.65 |

Ladder: **800 → 700 → 600 → 400**.  
Section H2 always outranks statement (size + weight). No heading below an H2 may render heavier than that H2.

---

## Casing law (HARD)

| Role | Casing | Where |
|------|--------|-------|
| **Hero** | Sentence / brand line — not Title Case every word | `split-hero` only |
| **Section / statement** | **Sentence case** | All section titles, bands, fifty-fifty |
| **Eyebrows / labels** | **Small uppercase only** (`.type-label` / `.eyebrow`) | Above titles; strip labels |
| **Body / lede** | Sentence case | Support copy |
| **CTAs / nav** | Quiet uppercase UI (unchanged) | Buttons, chrome |

**Banned:**
- `text-transform: uppercase` on H1 / H2 / campaign / statement headlines
- ALL CAPS display
- Title Case stacks on every heading
- Eyebrow that restates the H2 (e.g. “Real results” above “Real people. Real results.”)

---

## Eyebrows

```css
font-size: 11px;
font-weight: 600;
letter-spacing: 0.08em;
text-transform: uppercase;
color: #6b645a;
```

No text under 11px.

---

## Dark bands — max two tiers

| Tier | Role | Spec |
|------|------|------|
| **1** | Statement | `clamp(26px, 2.8vw, 32px)` / **600** / `#ffffff` |
| **2** | Support | **16px** / **400** / `#d6d2cb` (≥4.5:1 on charcoal) |

Delete tier 3; merge into tier 2 if needed. CTAs are UI, not a text tier.

---

## Alignment (no exceptions)

| Surface | Align |
|---------|-------|
| Section headers (eyebrow + H2 + lede) | **Left** |
| Full-bleed statement / dark bands | **Centered** |

---

## Token map

```css
--fw-hero: 800;
--fw-h2: 700;
--fw-statement: 600;
--fw-body: 400;
--fs-hero: clamp(48px, 6vw, 76px);
--fs-h2: clamp(32px, 3.4vw, 40px);
--fs-statement: clamp(26px, 2.8vw, 32px);
--fs-lede: 17px;
--fs-body: 16px;
--fs-label: 11px;
--ls-hero: -0.02em;
--ls-h2: -0.01em;
--ls-label: 0.08em;
--lh-hero: 1.02;
--lh-h2: 1.2;
--lh-lede: 1.55;
--lh-body: 1.65;
```

Mapped to `--type-hero-*`, `--type-section-*`, `--type-statement-*`, `--type-lede-*`, `--type-body-*`, `--type-label-*` in `design-tokens.css`.

Utilities: `.type-hero`, `.type-section` (`.type-campaign` = alias), `.type-statement`, `.type-body`, `.type-lede`, `.type-label`.

---

## Homepage mapping + casing examples

| Section | Tier | Casing example |
|---------|------|----------------|
| `split-hero` | Hero | *The Pilates Sock Era is Over* |
| `fifty-fifty` problem | Section | *Yoga socks are useless.* |
| `fifty-fifty` grip | Section | *Upgrade your grip. Upgrade your workout.* |
| `fifty-fifty` sock-math | Section | *One pair. Done.* |
| `statement-band` | Statement (dark) | *Studio workouts and footwear will never be the same.* |
| `guarantee-band` | Statement (dark) | *Zero risk. All grip.* |
| `fifty-fifty` Coperni | Section | *Barreletics × Coperni* |
| `variant-grid` | Section (left) | *Shop all styles & colors* |
| `social-proof` | Section (left) — no redundant eyebrow | *Real people. Real results.* |
| `home-ugc` | Section (left) | *@barreletics* |
| `newsletter` | Section (left) | *10% off your first pair.* |
| `disciplines` / `value-strip` | Labels | Small uppercase via `.type-label` |
| `geo-section` | H3 | *Trusted across the country* |

---

## Deliberate non-changes

- No new section layouts / major HTML restructures
- No color system overhaul beyond eyebrow + dark-band support colors
- Sentence case headings; hero tracking −0.02em; body 16/1.65; lede 17/1.55
- Roboto retained; Theme Editor remains QA runtime; repo owns tokens
- Static review: `docs/Barreletics Home - Type OS Preview.html`

---

## Files

- `shopify-build/assets/design-tokens.css`
- `shopify-build/assets/barreletics-base.css`
- Homepage sections + `templates/index.json`
- `docs/Barreletics Home - Type OS Preview.html`
