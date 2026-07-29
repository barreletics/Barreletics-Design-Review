# M4 Type Hierarchy — Four-Tier OS

**Date:** 2026-07-29  
**Status:** Implemented in `shopify-build/` · review via static Type OS Preview  
**Family:** Roboto only (unchanged)

---

## Casing law (HARD)

| Role | Casing | Where |
|------|--------|-------|
| **T1 Hero** | Brand line / sentence case — **not** bland Title Case every word | `split-hero` only |
| **T2 Campaign** | **ALL CAPS only** — major campaign statements | Hold Display moments |
| **T3 Section** | **Sentence case** — quieter editorial | Commerce, reviews, UGC, Coperni, newsletter |
| **Eyebrows / labels** | **Small uppercase only** (`.type-label` / `.eyebrow`) | Above titles; strip labels |
| **Body / lede** | Sentence case | Support copy |

**Anti-patterns (banned):**
- Title Case on every heading across the page
- ALL CAPS on section / editorial titles
- ALL CAPS on body copy
- Making every H2 look like another campaign moment

---

## Signature display — **Hold Display** (Tier 2)

Campaign treatment. Recognizable without a second font. **Always ALL CAPS.**

| Trait | Spec |
|-------|------|
| Scale | `clamp(32px, 4.2vw, 46px)` / mobile `clamp(26px, 6.5vw, 34px)` — large but **secondary to hero** |
| Weight | `400` |
| Leading | `1.08` |
| Tracking | `0.04em` (open — tuned for caps, not tight lowercase display) |
| Transform | `uppercase` (enforced on `.type-campaign`) |
| Measure | Optional narrow `14ch` / wide `28ch` |
| **Hold Mark** | Short rust rule under title: `2.75rem × 2px` |
| Utility | `.type-campaign` + `.type-campaign--mark` (+ `--narrow` / `--wide`) |
| Breath | `--section-padding-y-campaign` (112px) + `--stack-campaign-*` |

Not: purple-AI gradients, newspaper rules, Title Case stacks, or generic H2 scale.

---

## Four tiers (numeric contrast)

| Tier | Role | Desktop | Mobile | Weight / LH / Track | Casing |
|------|------|---------|--------|---------------------|--------|
| **1 Hero** | `--type-hero-*` | `clamp(48px, 6.8vw, 76px)` | `clamp(36px, 9vw, 48px)` | **500** / 1.02 / −0.032em | Brand / sentence |
| **2 Campaign** | `--type-campaign-*` + Hold Mark | `clamp(32px, 4.2vw, 46px)` | `clamp(26px, 6.5vw, 34px)` | 400 / 1.08 / **0.04em** | **ALL CAPS** |
| **3 Section** | `--type-section-*` | `clamp(22px, 2.4vw, 28px)` | `clamp(20px, 5vw, 24px)` | 400 / 1.28 / −0.01em | Sentence |
| **4 Body** | `--type-body-*`, lede, label | body 16 · lede 17 · label 11/500 | — | 400 body · labels quiet | Sentence · labels UPPER |

Utilities: `.type-hero`, `.type-campaign`, `.type-section`, `.type-body`, `.type-lede`, `.type-label`.

**Rhythm:** Campaign sections use larger Y padding (112 / 80 mobile) than quiet editorial (64 / 48). Stack gaps around campaign titles are looser than section titles.

---

## Alignment roles

| Token / class | Intent | Use |
|---------------|--------|-----|
| `--align-hero` / `.align-hero` | Left (desk); hero CSS centers on mobile | `split-hero` |
| `--align-campaign` / `.align-campaign` | Left editorial campaign | available |
| `--align-editorial` / `.align-editorial` | Left copy columns | `fifty-fifty` text |
| `--align-band` / `.align-band` | Center for band/moments only | `statement-band`, `guarantee-band`, commerce heads |

---

## Homepage mapping + casing examples

| Section | Tier | Casing example |
|---------|------|----------------|
| `split-hero` | 1 Hero | *The Pilates Sock Era is Over* |
| `fifty-fifty` problem | 2 Campaign | *YOGA SOCKS ARE USELESS.* |
| `fifty-fifty` grip | 2 Campaign | *UPGRADE YOUR GRIP. UPGRADE YOUR WORKOUT.* |
| `fifty-fifty` sock-math | 2 Campaign | *ONE PAIR. DONE.* |
| `statement-band` | 2 Campaign | *STUDIO WORKOUTS AND FOOTWEAR WILL NEVER BE THE SAME* |
| `guarantee-band` | 2 Campaign | *ZERO RISK. ALL GRIP.* |
| `fifty-fifty` Coperni | 3 Section | *Barreletics × Coperni* |
| `variant-grid` | 3 Section | *Shop all styles & colors* |
| `social-proof` | 3 Section | *Real people. Real results.* |
| `home-ugc` | 3 Section | *@barreletics* |
| `newsletter` | 3 Section | *10% off your first pair.* |
| `disciplines` / `value-strip` | 4 Labels | Small uppercase via `.type-label` |
| `geo-section` | 4 / H3 | *Trusted across the country* |

Eyebrows (source sentence case → CSS uppercase): e.g. *Tired of slipping in your yoga socks?*

Nav / CTAs: unchanged quiet UI (11/500 nav, 12/700 CTA) — must not compete with Tier 1–2.

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
