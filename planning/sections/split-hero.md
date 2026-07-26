# Split hero

**Status:** Awaits visual QA — **not frozen**  
**Blocker:** Need Andrew to paste a **new disposable draft theme ID** → deploy → return preview URL + Theme Editor URL  
**Note:** Implementation / GitHub code review alone is **insufficient**. Visual approval = Shopify preview (desktop + mobile, TE controls, schema, crop, performance).  
**Filename:** `shopify-build/sections/split-hero.liquid`  
**CSS:** `shopify-build/assets/split-hero.css` (loaded in the section)  
**Authority mock:** `docs/Barreletics Home - Definitive-WORKING.html` (hero ~812–825; CSS ~82–132; mobile ~646–654)  
**Contract:** `planning/m4-section-library-CONTRACT.md` (H1 rename from `home-split-hero`)

---

## Purpose

Reusable 50/50 first-viewport hero: media | copy on desktop; image first, centered copy on mobile. Library section for Home, Collection, Landing — not homepage-only.

---

## Theme Editor settings

| Setting | ID | Type | Default | Notes |
|---------|----|------|---------|-------|
| Hero image | `image` | image_picker | — | LCP: eager + fetchpriority high |
| Image alt text | `image_alt` | text | Performance Skins alt from mock | Falls back to image.alt / title |
| Reverse layout | `reverse_layout` | checkbox | false | Desktop copy left / image right; mobile stays image-first |
| Show trust line | `show_trust` | checkbox | true | |
| Show star rating | `show_stars` | checkbox | true | Decorative ★★★★★ (aria-hidden) |
| Trust line | `trust_text` | text | Trusted by 1,000's… | |
| Trust line link | `trust_url` | url | — | Optional; omit link if blank |
| Headline | `title` | text | The Pilates Sock Era is Over | BZ-020 title case |
| Heading level | `heading_level` | select h1\|h2\|h3 | h1 | One H1 per page when reused |
| Body | `body` | textarea | Outperforms barre socks… | |
| Primary CTA | `cta_text` | text | Shop Now | |
| Primary CTA link | `cta_url` | url | — | Falls back to all-products collection |
| Tag link text | `tag_text` | text | #letusknockyoursocksoff | |
| Tag link | `tag_url` | url | — | **No hardcoded URL**; if blank, text only (no `<a>`) |
| Section aria-label | `aria_label` | text | Hero | On region wrapper |

**Preset:** “Split hero”

---

## Architectural decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Filename / TE name | `split-hero` / **Split hero** | Contract H1; library-reusable, not “Home…” |
| Landmark | Schema `"tag": "section"` + inner `<div role="region">` | Avoids nested `<section>`; one Shopify section landmark + labeled region |
| CSS load | `{{ 'split-hero.css' \| asset_url \| stylesheet_tag }}` in section | OS 2.0 pattern; no global `heroes.css` in `theme.liquid` |
| `heroes.css` | Deleted | Obsolete after rename; only served split-hero styles |
| Heading level | Setting h1–h3 | Reuse off-home without forcing multiple H1s |
| Tag URL | No Liquid fallback to `#knock-socks` | Page anchors are merchant/TE concerns, not hardcoded structure |
| Reverse layout | Desktop-only modifier | Justified for Collection/SEO reuse; mobile keeps LCP image-first |
| Legacy `hero` / `hero-alt` | Kept for now | H3: delete only after freeze approved |
| Next sections | Blocked | Gate until Andrew freezes `split-hero` after visual QA on draft preview |
| Approval path | Shopify preview | Deploy disposable draft + preview URL; not approve from GitHub alone |

---

## How Brian uses it

1. Pull approved repo into the production theme (or disposable draft for QA when Andrew names an ID).
2. Theme Editor → **Add section** → **Split hero**.
3. Upload hero image; set alt; wire CTA / trust / tag URLs to real destinations (`#reviews`, collection, etc.).
4. Leave **Heading level = H1** on the primary page entry; switch to H2/H3 if another H1 already exists.
5. Optional **Reverse layout** when the composition needs copy-left on desktop.
6. Do not edit in Theme Editor as master — copy/settings changes that become permanent belong back in the repo defaults or page JSON in git.

---

## Visual / type (match mock)

- Desktop: image left / copy right; `min-height: 75vh`; copy padding 72×64; max-width 560px  
- Title: `clamp(40px, 6vw, 64px)` / 400 / −0.03em / lh 1.08 → mobile `clamp(34px, 9vw, 44px)`  
- CTA: 12px / 700 / uppercase / rust `#c45c3f` → hover charcoal `#1c1916`  
- Mobile ≤768: stack, image order 1, copy centered  
