# Hero full-bleed module

Reusable edge-to-edge hero. Two alignments share the same class stack and tokens.

| Alignment | When | Authority |
|-----------|------|-----------|
| **Centered** (`data-align="center"`) | Help · Journal · content · SEO-style · campaign LPs | **BZ-025** · `docs/Barreletics Hero - Centered Fullbleed - Pattern-v1.html` |
| **Left / start** (default on SEO) | Commerce SEO landings (trust → H1 → shop) | SEO `Definitive-v34.html` |

**Snippet (centered):** `sections/hero-fullbleed-snippet.html`  
**Tokens:** BZ-020 (400 display · Home size 34–46 · 700 CTAs) · BZ-024 (Title Case hero H1)  
**Not this module:** Home WORKING split/left · Collection shop split hero (BZ-023)

## Settings

| Attr / control | Values | Notes |
|----------------|--------|--------|
| `data-media-type` | `image` \| `video` | On `<section class="hero-fullbleed">` |
| `data-align` | `center` \| omit/`start` | Centered = Pattern-v1; left = SEO v34 |
| Media | `<img>` or muted loop `<video>` + `poster` | Prefer **image** for LCP |
| Brand | `.hero-fullbleed__brand` | **Include** on content pages (hero-level brand signal). Optional when nav logo is enough. |
| Eyebrow / trust | Optional | Soft white/muted — **not** rust. Trust stars may use `#c45c3f`. |

## Overlay budget

Brand (recommended on content pages) · optional trust · optional eyebrow · **one H1** · short lede · CTA group.  
No cards, choosers, badges, or floating stickers on the media.

## Class list

```
.hero-fullbleed
.hero-fullbleed__media
.hero-fullbleed__overlay
.hero-fullbleed__brand          (recommended on centered content heroes)
.hero-fullbleed__trust          (optional)
.hero-fullbleed__stars
.hero-fullbleed__eyebrow        (optional)
.hero-fullbleed__title          (H1 — Title Case · 400 · clamp 34–46)
.hero-fullbleed__lede
.hero-fullbleed__cta-group
.hero-fullbleed__cta            (ALL CAPS · 700)
.hero-fullbleed__cta--ghost     (optional secondary)
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

## Usage notes

1. Copy CSS + markup from Pattern-v1 or `sections/hero-fullbleed-snippet.html`.
2. Keep ~100vh / min 90vh; full-bleed — no inset media cards.
3. Centered uses even vertical wash; left SEO uses left-weighted gradient.
4. Do **not** restore 64px / weight 500 unless explicitly asked.
5. Theme: map settings → media, align, brand, H1, lede, CTA label + URL.
