# home-split-hero — Design System audit

**Date:** 2026-07-26  
**Scope:** `shopify-build/sections/home-split-hero.liquid`, `shopify-build/assets/heroes.css`, `layout/theme.liquid` heroes.css load  
**Authority intent:** `docs/Barreletics Home - Definitive-WORKING.html`  
**Status:** **NOT FROZEN** — awaiting Andrew architecture + code approval  
**Block:** No next section (`hero-fullbleed`, `collection-split-hero`, or others) until freeze

---

## Verdict

Solid first pass as a Theme Editor section: schema + preset, BEM CSS, LCP image attrs, no JS, no sibling-section deps. Gaps below keep it from “library frozen” quality.

---

## Checklist

| Standard | Result | Notes |
|----------|--------|-------|
| Own `sections/*.liquid` | **PASS** | `home-split-hero.liquid` |
| Complete schema + presets (addable) | **PASS** | Preset `"Home split hero"`; settings cover copy + media + aria |
| Independently draggable / removable | **PASS** | Standard section; no group lock |
| No dependency on other sections | **PASS** | Self-contained Liquid |
| Shared code only in snippets/assets | **PASS** | Styles in `heroes.css`; no cross-section Liquid |
| CSS scoped (BEM / section classes) | **PASS** | `.home-split-hero__*` only; file notes home-split-only for now |
| LCP / performance | **PASS** | `loading: eager`, `fetchpriority: high`, `widths`/`sizes`, `decoding: async`; no JS |
| Responsive behavior | **PASS** | 768 stack + center; 480 full-width CTA; matches WORKING |
| `section.shopify_attributes` | **PASS** | On root element |
| Placeholder when image blank | **PASS** | Merchant-friendly |
| No homepage-only coupling | **GAP** | Name/defaults lean Home; Liquid hardcodes `#knock-socks` |
| No page-specific architecture | **GAP** | Always renders `<h1>` (bad if reused off-home or twice) |
| CSS load strategy | **GAP** | `heroes.css` global in `theme.liquid` (all templates) |
| Markup semantics | **GAP** | Schema `"tag": "section"` + inner `<section>` → nested `<section>` |
| Merchant reuse controls | **GAP** | Missing reverse, heading level, spacing/color knobs (see below) |

---

## Gaps & refinement recommendations (do not implement until Andrew directs)

### P0 — architecture / library correctness

1. **Nested `<section>`** — Prefer schema wrapper only (`tag: section`) and use a `<div class="home-split-hero">` inside, or drop `"tag": "section"` and keep the explicit `<section>`. One landmark wrapper.
2. **Heading level setting** — `select` for `h1`–`h3` (default `h1`). Library sections must not force H1 on every placement.
3. **Remove hardcoded `#knock-socks` fallback** — If `tag_url` blank, omit `href` behavior or render as non-link / `#` only via setting. Anchors as *schema defaults/info* are OK; Liquid hardcoding page structure is not.
4. **CSS load** — Long-term: section `{% stylesheet %}` or load `heroes.css` only when section present. Global load is fine short-term but document as tech debt before freeze.

### P1 — reusable library controls (merchant)

5. **Media/copy reverse** — Checkbox or select (`image_left` / `image_right`) for Collection/SEO reuse without a second section.
6. **Naming for Theme Editor** — Consider display name `Split hero` (filename may stay `home-split-hero` until freeze rename). “Home …” implies homepage-only.
7. **Optional visibility toggles** — Explicit show/hide for tag link (trust already has toggles); optional min-height / section padding if mock allows without bloat.
8. **Color / surface** — Optional background setting (or rely on tokens only) so section isn’t locked to white/cream hardcodes beyond token fallbacks.

### P2 — polish / docs

9. **`enabled_on`** — Optional; leaving unrestricted is better for a library (current = OK).
10. **Font stacks in `heroes.css`** — Prefer token/CSS variables already on `:root` over repeating `'Roboto', …` if chrome/tokens own type.
11. **Preset completeness** — Current preset is enough; avoid bloating with homepage-specific preset JSON that assumes other sections exist.

---

## What is already aligned with WORKING

- 50/50 grid → mobile image-first / copy-centered  
- Trust + stars + H1 clamp / body / single rust CTA / tag link  
- One primary CTA (outline retired per mock)  
- BZ-020 title sizing

---

## Explicit freeze gate

- [ ] Andrew approves architecture (section boundaries, CSS strategy, naming)  
- [ ] Andrew approves code after P0 (and agreed P1) refinements  
- [ ] Mark frozen in `planning/m4-build-progress.md`  
- [ ] Only then unlock next section

**Until then: NOT FROZEN. Next sections blocked.**
