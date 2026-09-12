# Hero full-bleed module

Reusable edge-to-edge hero. Two alignments share the same class stack and **BZ-020 FINAL BALANCE** tokens.

| Alignment | When | Authority |
|-----------|------|-----------|
| **Centered** (`data-align="center"`) | Help · Journal · content · SEO-style · campaign LPs | **BZ-025** · `docs/Barreletics Hero - Centered Fullbleed - Pattern-v2.html` |
| **Left / start** | Commerce SEO landings (trust → H1 → shop) | SEO `Definitive-v36.html` |

**Snippet (centered):** `sections/hero-fullbleed-snippet.html`  
**Tokens:** Opening H1 `clamp(40–64)` / **400** / lh 1.08 / Title Case · sections sentence case 400 · CTAs **700** ALL CAPS  
**Not this module:** Home WORKING split · Collection shop split (BZ-023) — same opening H1 tokens, different layout

## Settings

| Attr / control | Values | Notes |
|----------------|--------|--------|
| `data-media-type` | `image` \| `video` | On `<section class="hero-fullbleed">` |
| `data-align` | `center` \| omit/`start` | Centered = Pattern-v2; left = SEO v36 |
| Media | `<img>` or muted loop `<video>` + `poster` | Prefer **image** for LCP |
| Brand | `.hero-fullbleed__brand` | **Include** on content pages |
| Eyebrow / trust | Optional | Soft white/muted — **not** rust |

## Overlay budget

Brand · optional trust/eyebrow · **one H1** · short lede · CTA group.  
No cards, choosers, badges, or floating stickers on the media.

## Class list

```
.hero-fullbleed
.hero-fullbleed__media
.hero-fullbleed__overlay
.hero-fullbleed__brand
.hero-fullbleed__trust
.hero-fullbleed__stars
.hero-fullbleed__eyebrow
.hero-fullbleed__title          (H1 — Title Case · 400 · clamp 40–64)
.hero-fullbleed__lede
.hero-fullbleed__cta-group
.hero-fullbleed__cta            (ALL CAPS · 700)
.hero-fullbleed__cta--ghost
```

## Centered skeleton

```html
<section class="hero-fullbleed" aria-label="Page hero" data-media-type="image" data-align="center">
  <div class="hero-fullbleed__media">
    <img src="…" alt="" width="2000" height="1333" fetchpriority="high" decoding="async">
  </div>
  <div class="hero-fullbleed__overlay">
    <p class="hero-fullbleed__brand">Barreletics</p>
    <h1 class="hero-fullbleed__title">Headline In Title Case</h1>
    <p class="hero-fullbleed__lede">One short supporting sentence.</p>
    <div class="hero-fullbleed__cta-group">
      <a href="#main" class="hero-fullbleed__cta">Primary Cta</a>
    </div>
  </div>
</section>
```
