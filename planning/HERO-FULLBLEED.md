# Hero full-bleed module (Brian)

Reusable edge-to-edge hero for **any page**: Home (optional), Collection, SEO, campaign LPs.

**Authority mock:** SEO `Definitive-v28.html` (still + trust → H1; eyebrow optional)  
**Snippet:** `sections/hero-fullbleed-snippet.html`

## Settings

| Attr / control | Values | Notes |
|----------------|--------|--------|
| `data-media-type` | `image` \| `video` | Put on `<section class="hero-fullbleed">` |
| Media | `<img>` or muted loop `<video>` + `poster` | Inside `.hero-fullbleed__media` · prefer **image** for LCP on SEO |
| Eyebrow | Soft white/muted on dark · **optional** | `rgba(255,255,255,0.72)` — **not** rust · SEO v28 omits |

## Overlay budget

Optional **`.hero-fullbleed__trust`** as **first line** of the overlay stack · optional eyebrow · **one H1** · short lede · CTA group.  
Brand (`.hero-fullbleed__brand`) is optional — omit when nav already has the logo.  
No cards, choosers, badges, or floating stickers on the media (trust belongs in the copy stack, not absolute-positioned on the media).

## Class list

```
.hero-fullbleed
.hero-fullbleed__media
.hero-fullbleed__overlay
.hero-fullbleed__trust          (optional — first overlay line; Home rhythm)
.hero-fullbleed__stars          (inside trust; rust #c45c3f)
.hero-fullbleed__brand          (optional — skip if nav has logo)
.hero-fullbleed__eyebrow
.hero-fullbleed__title          (H1)
.hero-fullbleed__lede
.hero-fullbleed__cta-group
.hero-fullbleed__cta
.hero-fullbleed__cta--ghost     (optional secondary)
```

## Copy-paste HTML skeleton

```html
<!-- REUSABLE — hero-fullbleed. data-media-type: image|video -->
<section class="hero-fullbleed" aria-label="Page hero" data-media-type="video">
  <div class="hero-fullbleed__media">
    <!-- image: <img src="…" alt=""> -->
    <video autoplay muted loop playsinline webkit-playsinline preload="metadata" poster="POSTER_URL" aria-hidden="true">
      <source src="VIDEO_URL" type="video/mp4">
    </video>
  </div>
  <div class="hero-fullbleed__overlay">
    <!-- optional first line — not a floating sticker -->
    <p class="hero-fullbleed__trust">
      <span class="hero-fullbleed__stars" aria-hidden="true">★★★★★</span>
      <a href="#reviews">Trusted by 1,000&#39;s of instructors &amp; studios</a>
    </p>
    <!-- optional: <p class="hero-fullbleed__brand">Barreletics</p> -->
    <p class="hero-fullbleed__eyebrow">Eyebrow line</p>
    <h1 class="hero-fullbleed__title">Headline</h1>
    <p class="hero-fullbleed__lede">One short supporting sentence.</p>
    <div class="hero-fullbleed__cta-group">
      <a href="#shop" class="hero-fullbleed__cta">Shop Now</a>
      <!-- optional: <a href="…" class="hero-fullbleed__cta hero-fullbleed__cta--ghost">Secondary</a> -->
    </div>
  </div>
</section>
```

## Usage notes

1. Copy the CSS block commented **REUSABLE — copy this section + CSS to any page** from SEO v27 (or the snippet file).
2. Set `data-media-type` to match the child (`img` vs `video`).
3. Keep ~100vh / min 90vh; full-bleed edge-to-edge — no inset media cards.
4. Left-weighted overlay is fine for trust-first stacks; soften left gradient for readability.
5. Theme: map settings → media source, eyebrow, H1, lede, CTA label + URL.

First shipped: Best Grippy Socks SEO v6 · refined as reusable module in **v8** · trust-in-stack + no brand in **v27** · still hero + no eyebrow in **v28**.
