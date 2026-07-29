# M4 Type Hierarchy — Four-Tier OS

**Date:** 2026-07-29  
**Status:** Implemented in `shopify-build/` · QA on theme `187144929571`  
**Family:** Roboto only (unchanged)

---

## Signature display — **Hold Display**

Tier 2 campaign treatment. Recognizable without a second font.

| Trait | Spec |
|-------|------|
| Scale | Near-hero: `clamp(40px, 5.2vw, 56px)` / mobile `clamp(32px, 7.5vw, 40px)` |
| Weight | `400` (calm brand; presence from size + tracking, not bold) |
| Leading | `1.04` |
| Tracking | `-0.042em` (tighter than section) |
| Measure | Optional narrow `16ch` / wide `22ch` |
| **Hold Mark** | Short rust rule under title: `2.75rem × 2px` (`--type-campaign-rule-*`). On dark bands → light rule. |
| Utility | `.type-campaign` + `.type-campaign--mark` (+ `--narrow` / `--wide`) |
| Breath | Campaign sections use `--section-padding-y-campaign` (96px) and `--stack-campaign-*` |

Not: purple-AI gradients, newspaper rules, title-case stacks, or generic H2 scale.

---

## Four tiers

| Tier | Role tokens | Desktop | Mobile | Weight / LH / Track |
|------|-------------|---------|--------|---------------------|
| **1 Hero** | `--type-hero-*` (alias `--type-opening-*`) | `clamp(44px, 6vw, 68px)` | `clamp(34px, 8.5vw, 44px)` | 400 / 1.05 / −0.035em |
| **2 Campaign** | `--type-campaign-*` + Hold Mark | `clamp(40px, 5.2vw, 56px)` | `clamp(32px, 7.5vw, 40px)` | 400 / 1.04 / −0.042em |
| **3 Section** | `--type-section-*` | `clamp(24px, 2.6vw, 32px)` | `clamp(22px, 5.5vw, 28px)` | 400 / 1.18 / −0.02em |
| **4 Body** | `--type-body-*`, `--type-lede-*`, `--type-label-*` | body 16px · lede 17px · label 11px/500 | lede 16px | 400 body · labels quiet |

Utilities: `.type-hero`, `.type-campaign`, `.type-section`, `.type-body`, `.type-lede`, `.type-label`.

---

## Alignment roles

| Token / class | Intent | Use |
|---------------|--------|-----|
| `--align-hero` / `.align-hero` | Left (desk); hero CSS centers on mobile | `split-hero` |
| `--align-campaign` / `.align-campaign` | Left editorial campaign | available |
| `--align-editorial` / `.align-editorial` | Left copy columns | `fifty-fifty` text |
| `--align-band` / `.align-band` | Center for band/moments only | `statement-band`, `guarantee-band`, commerce heads |

---

## Homepage mapping

| Section | Tier | Align | Notes |
|---------|------|-------|-------|
| `split-hero` | 1 Hero | hero (L → C mobile) | Opening only |
| `fifty-fifty` problem | 2 Campaign + Hold Mark | editorial L | |
| `fifty-fifty` grip | 2 Campaign + Hold Mark | editorial L | |
| `fifty-fifty` sock-math | 2 Campaign + Hold Mark | editorial L | |
| `statement-band` | 2 Campaign + Hold Mark | band C | Extra Y padding |
| `guarantee-band` | 2 Campaign + Hold Mark | band C | Dark; light Hold Mark |
| `fifty-fifty` Coperni | 3 Section | editorial L | Supporting, not a moment |
| `variant-grid` | 3 Section | band C | Commerce head stays centered |
| `social-proof` | 3 Section | left header | Title: “Real people. Real results.” |
| `home-ugc` | 3 Section | band C | |
| `newsletter` | 3 Section | band C | |
| `disciplines` / `value-strip` | 4 Labels | band | Strip UI, not headings |
| `geo-section` | 4 / H3 | — | Accordion supporting |

Nav / CTAs: unchanged quiet UI (11/500 nav, 12/700 CTA) — must not compete with Tier 1–2.

---

## Deliberate non-changes

- No new section layouts / major HTML restructures
- No text-over-image hero overlays (not structurally present without redesign)
- Roboto retained; no second display face
- Theme Editor remains QA runtime; repo owns tokens

---

## Files

- `shopify-build/assets/design-tokens.css`
- `shopify-build/assets/barreletics-base.css`
- `shopify-build/assets/split-hero.css`
- Homepage sections listed above + `templates/index.json` (`heading_tier` on fifty-fifty)
