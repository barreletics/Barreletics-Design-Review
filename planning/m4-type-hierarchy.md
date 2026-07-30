# M4 Type Hierarchy — Simplified OS

**Date:** 2026-07-29  
**Status:** Caps experiment rejected · sentence-case OS in `shopify-build/`  
**Family:** Roboto only (unchanged)  
**Review surface:** `docs/Barreletics Home - Type OS Preview.html`

---

## Casing law (HARD)

| Role | Casing | Where |
|------|--------|-------|
| **Hero** | Sentence / brand line — not Title Case every word | `split-hero` only |
| **Section / statement** | **Sentence case** — one consistent H2 language | All section titles, bands, fifty-fifty |
| **Eyebrows / labels** | **Small uppercase only** (`.type-label` / `.eyebrow`) | Above titles; strip labels |
| **Body / lede** | Sentence case | Support copy |
| **CTAs / nav** | Quiet uppercase UI (unchanged) | Buttons, chrome |

**Banned:**
- `text-transform: uppercase` on H1 / H2 / campaign / statement headlines
- ALL CAPS display or “Hold Display” shout
- Title Case stacks on every heading
- Separate shouty “campaign caps” mode

---

## Simplified tiers

Hierarchy by **size + whitespace**, not CASE or wild style switches.

| Tier | Role | Desktop | Mobile | Weight / LH / Track | Casing |
|------|------|---------|--------|---------------------|--------|
| **Hero** | `--type-hero-*` | `clamp(48px, 6.8vw, 76px)` | `clamp(36px, 9vw, 48px)` | **500** / 1.02 / −0.032em | Sentence / brand |
| **Section** | `--type-section-*` | `clamp(26px, 3vw, 34px)` | `clamp(22px, 5.5vw, 28px)` | 400 / 1.2 / −0.015em | **Sentence** |
| **Statement** | `--type-statement-*` | `clamp(28px, 3.4vw, 38px)` | `clamp(24px, 6vw, 32px)` | same as section | **Sentence** — size bump only |
| **Body** | `--type-body-*`, lede, label | body 16 · lede 17 · label 11/500 | — | 400 body · labels quiet | Sentence · labels UPPER |

Utilities: `.type-hero`, `.type-section` (`.type-campaign` = alias), `.type-statement`, `.type-body`, `.type-lede`, `.type-label`.

**Statement-band:** slight size bump + a little more Y padding / measure — **not** a different casing or tracking language.

---

## Alignment roles

| Token / class | Intent | Use |
|---------------|--------|-----|
| `--align-hero` / `.align-hero` | Left (desk); hero CSS centers on mobile | `split-hero` |
| `--align-editorial` / `.align-editorial` | Left copy columns | `fifty-fifty` text |
| `--align-band` / `.align-band` | Center for band/moments only | `statement-band`, `guarantee-band`, commerce heads |

---

## Homepage mapping + casing examples

| Section | Tier | Casing example |
|---------|------|----------------|
| `split-hero` | Hero | *The Pilates Sock Era is Over* |
| `fifty-fifty` problem | Section | *Yoga socks are useless.* |
| `fifty-fifty` grip | Section | *Upgrade your grip. Upgrade your workout.* |
| `fifty-fifty` sock-math | Section | *One pair. Done.* |
| `statement-band` | Statement | *Studio workouts and footwear will never be the same.* |
| `guarantee-band` | Section | *Zero risk. All grip.* |
| `fifty-fifty` Coperni | Section | *Barreletics × Coperni* |
| `variant-grid` | Section | *Shop all styles & colors* |
| `social-proof` | Section | *Real people. Real results.* |
| `home-ugc` | Section | *@barreletics* |
| `newsletter` | Section | *10% off your first pair.* |
| `disciplines` / `value-strip` | Labels | Small uppercase via `.type-label` |
| `geo-section` | H3 | *Trusted across the country* |

Eyebrows (source sentence case → CSS uppercase): e.g. *Tired of slipping in your yoga socks?*

---

## Deliberate non-changes

- No new section layouts / major HTML restructures
- No text-over-image hero overlays
- Roboto retained; no second display face
- Theme Editor remains QA runtime; repo owns tokens
- Static review: `docs/Barreletics Home - Type OS Preview.html`

---

## Files

- `shopify-build/assets/design-tokens.css`
- `shopify-build/assets/barreletics-base.css`
- `shopify-build/assets/split-hero.css`
- Homepage sections + `templates/index.json`
- `docs/Barreletics Home - Type OS Preview.html`
