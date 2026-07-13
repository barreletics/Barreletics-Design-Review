# PDP Architecture — Lossless Complete Specification

**CRITICAL:** This document is a lossless migration of EVERY specification, measurement, code, class name, color value, font size, and decision from the approved Barreletics PDP design system. NO SUMMARIZATION. NO SIMPLIFICATION. ALL DECISIONS PRESERVED EXACTLY.

Last Updated: 2026-07-12  
Source Authority: Barreletics-PDP-v36-Jul2026.html, Barreletics PDP - Matured.html, pdp-styles.css, pdp-tweaks.jsx  
Status: APPROVED

---

## EXTRACTED SOURCE CODE AND SPECIFICATIONS

### HTML Structure (from Barreletics-PDP-v36-Jul2026.html)

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Best Grippy Shoes for Barre, Pilates & Yoga — Barreletics</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body { font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif; color: #1c1916; background: #fff; line-height: 1.5; }
    a { color: #1c1916; text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* HERO TOGGLE */
    .hero-toggle { display: flex; gap: 8px; margin-bottom: 24px; }
    .hero-toggle__btn { padding: 8px 16px; border: 1px solid #d6cfc0; background: #fff; cursor: pointer; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; transition: all 0.2s; }
    .hero-toggle__btn[data-active="true"] { background: #1c1916; color: #fff; border-color: #1c1916; }

    .pdp-hero { display: none; grid-template-columns: 1fr 1fr; gap: 64px; max-width: 1400px; margin: 0 auto; padding: 64px 40px; align-items: flex-start; }
    .pdp-hero[data-active="true"] { display: grid; }
    .pdp-gallery { display: flex; flex-direction: column; gap: 16px; position: sticky; top: 64px; }
    .pdp-gallery__hero { aspect-ratio: 1; background: #f9f9f9; overflow: hidden; border-radius: 8px; }
    .pdp-gallery__hero img { width: 100%; height: 100%; object-fit: cover; display: block; }

    .pdp-buy { display: flex; flex-direction: column; gap: 24px; }
    .pdp-buy__badge { display: inline-block; background: #c45c3f; color: #fff; padding: 4px 10px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; border-radius: 3px; }
    .pdp-buy__stars { font-size: 16px; color: #d4af37; letter-spacing: 2px; }
    .pdp-buy__name { font-size: 44px; font-weight: 700; line-height: 1.08; margin: 0; color: #1c1916; }
    .pdp-buy__desc { font-size: 16px; color: #4a4a4a; margin: 0; line-height: 1.6; }
    .pdp-buy__price-now { font-size: 36px; font-weight: 700; color: #1c1916; }
    .pdp-buy__price-meta { font-size: 13px; color: #8a8a8a; }
    .pdp-buy__cta { width: 100%; padding: 18px; background: #1c1916; color: #fff; font-size: 16px; font-weight: 600; border: none; cursor: pointer; border-radius: 6px; }
    .pdp-buy__cta:hover { background: #c45c3f; }
    .pdp-buy__swatches { display: flex; gap: 8px; flex-wrap: wrap; }
    .pdp-buy__swatch { width: 23px; height: 23px; border-radius: 50%; border: 2px solid transparent; cursor: pointer; transition: all 0.2s; padding: 9px; box-sizing: content-box; background-clip: content-box; }
    .pdp-buy__swatch:hover { border-color: #9a9182; }
    .pdp-buy__swatch[aria-selected="true"] { border-color: #1c1916; outline: none; }

    .pdp-section { max-width: 100%; padding: 64px 40px; }
    .pdp-section__inner { max-width: 1200px; margin: 0 auto; }
    .pdp-section__label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #8a8a8a; font-weight: 700; margin-bottom: 16px; }
    .pdp-section__title { font-size: 42px; font-weight: 700; line-height: 1.2; color: #1c1916; margin: 0 0 32px 0; }

    .pdp-benefits { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 48px; }
    .pdp-benefit__num { font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #c45c3f; font-weight: 700; }
    .pdp-benefit__title { font-size: 20px; font-weight: 700; color: #1c1916; margin: 12px 0 0; }
    .pdp-benefit__sub { font-size: 15px; color: #4a4a4a; line-height: 1.6; margin: 0; }

    .pdp-variants__grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
    .pdp-variants__grid img { transform: scale(1.05); transform-origin: center; }

    .review-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-top: 48px; }
    .review-card { background: #fff; border-radius: 12px; overflow: hidden; border: 1px solid #e6e6e6; }
    .review-image { aspect-ratio: 1; background: #e0e0e0; overflow: hidden; }
    .review-image img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .review-content { padding: 28px; }
    .review-stars { font-size: 14px; color: #d4af37; margin-bottom: 12px; letter-spacing: 2px; }
    .review-text { font-size: 15px; color: #4a4a4a; line-height: 1.7; margin: 0 0 16px 0; font-style: italic; }
    .review-author { font-size: 13px; font-weight: 700; color: #1c1916; margin: 0; }

    .pdp-motion-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-top: 48px; }
    .pdp-motion__video { width: 100%; aspect-ratio: 1; background: #f9f9f9; display: flex; align-items: center; justify-content: center; color: #8a8a8a; font-size: 14px; border-radius: 8px; }
    .pdp-motion__cap { font-size: 14px; color: #4a4a4a; line-height: 1.6; margin: 16px 0 0 0; font-weight: 500; }

    .pdp-justifier { display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; margin-top: 48px; }
    .pdp-justifier__card { padding: 32px; background: #fff; border-radius: 12px; border-left: 5px solid #c45c3f; }
    .pdp-justifier__tag { font-size: 11px; font-weight: 700; color: #c45c3f; text-transform: uppercase; letter-spacing: 0.08em; margin: 0 0 12px 0; }
    .pdp-justifier__quote { font-size: 16px; line-height: 1.7; color: #4a4a4a; margin: 0 0 16px 0; }
    .pdp-justifier__author { font-size: 13px; font-weight: 700; color: #1c1916; margin: 0; }

    .pdp-faq { padding: 80px 40px; background: #f5f2ec; }
    .pdp-faq__container { max-width: 760px; margin: 0 auto; }
    .pdp-faq__item { border-top: 1px solid #d6cfc0; padding: 18px 0; }
    .pdp-faq__trigger { cursor: pointer; font-size: 16px; font-weight: 500; color: #1c1916; display: flex; justify-content: space-between; align-items: center; width: 100%; background: none; border: none; padding: 0; }
    .pdp-faq__body { margin-top: 12px; font-size: 14px; color: #6b645a; line-height: 1.6; display: none; }
    .pdp-faq__body[data-open="true"] { display: block; }

    .pdp-newsletter { padding: 56px 40px; background: #fff; border-top: 1px solid #e6e6e6; }
    .pdp-newsletter__container { max-width: 600px; margin: 0 auto; text-align: center; }
    .pdp-newsletter__title { font-size: 36px; font-weight: 500; margin: 0 0 12px; color: #1c1916; }
    .pdp-newsletter__desc { font-size: 15px; color: #6b645a; margin: 0 0 24px; line-height: 1.6; }
    .pdp-newsletter__form { display: flex; gap: 8px; margin-bottom: 12px; }
    .pdp-newsletter__input { flex: 1; padding: 12px 16px; border: 1px solid #d6cfc0; background: #fff; font-size: 14px; color: #1c1916; border-radius: 4px; }
    .pdp-newsletter__input::placeholder { color: #9a9182; }
    .pdp-newsletter__button { padding: 12px 24px; background: #1c1916; color: #fff; border: none; font-size: 14px; font-weight: 600; cursor: pointer; letter-spacing: 0.05em; text-transform: uppercase; border-radius: 4px; }
    .pdp-newsletter__button:hover { background: #c45c3f; }
    .pdp-newsletter__fine { font-size: 11px; color: #9a9182; margin: 0; }

    @media (max-width: 1024px) {
      .pdp-benefits { grid-template-columns: repeat(2, 1fr); }
      .pdp-motion-grid { grid-template-columns: repeat(2, 1fr); }
      .pdp-variants__grid { grid-template-columns: repeat(2, 1fr); }
      .review-grid { grid-template-columns: repeat(2, 1fr); }
      .pdp-justifier { grid-template-columns: 1fr; }
    }

    @media (max-width: 768px) {
      .pdp-hero { grid-template-columns: 1fr; gap: 32px; padding: 32px 16px; }
      .pdp-gallery { position: static; }
      .pdp-buy__name { font-size: 32px; }
      .pdp-variants__grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }
      .pdp-benefits { grid-template-columns: 1fr; gap: 32px; }
      .pdp-motion-grid { grid-template-columns: 1fr; }
      .review-grid { grid-template-columns: 1fr; }
      .pdp-section { padding: 48px 16px; }
      .pdp-section__title { font-size: 32px; }
    }
  
    .pdp-variants__card { transition: none; }
    .pdp-variants__card:hover .card-img { transform: scale(1.03); }
    .card-img { transition: transform 0.4s ease; }
    .pdp-variants__card:hover .card-cta { letter-spacing: 0.06em; }

  </style>
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Best Grippy Shoes for Barre, Pilates & Yoga",
  "description": "The premium grip system that replaces traditional grip socks—built for reformer, barre, Pilates and Megaformer.",
  "brand": { "@type": "Brand", "name": "Barreletics" },
  "offers": {
    "@type": "Offer",
    "price": "74.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5",
    "reviewCount": "1000"
  }
}
</script>
</head>
<body>

<!-- HERO -->
<section class="pdp-hero" style="display:grid;grid-template-columns:1fr 1fr;gap:64px;max-width:1400px;margin:0 auto;padding:64px 40px;align-items:flex-start;">

  <!-- GALLERY -->
  <div class="pdp-gallery">
    <div class="pdp-gallery__hero">
      <img id="v10-main-img" src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800" alt="Studio Performance Skin — Onyx" />
    </div>
    <div style="display:flex;gap:6px;margin-top:8px;">
      <button onclick="v10Thumb(this,'https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=400')" style="width:72px;height:72px;border:2px solid #1c1916;background:#f9f9f9;padding:0;cursor:pointer;overflow:hidden;flex-shrink:0;"><img class="card-img-el" src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=400" style="width:100%;height:100%;object-fit:cover;display:block;" alt="View 1" /></button>
      <button onclick="v10Thumb(this,'https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=400')" style="width:72px;height:72px;border:1px solid #e6e6e6;background:#f9f9f9;padding:0;cursor:pointer;overflow:hidden;flex-shrink:0;"><img class="card-img-el" src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=400" style="width:100%;height:100%;object-fit:cover;display:block;" alt="View 2" /></button>
      <button onclick="v10Thumb(this,'https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg?v=1773920300&width=400')" style="width:72px;height:72px;border:1px solid #e6e6e6;background:#f9f9f9;padding:0;cursor:pointer;overflow:hidden;flex-shrink:0;"><img class="card-img-el" src="https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg?v=1773920300&width=400" style="width:100%;height:100%;object-fit:cover;display:block;" alt="View 3" /></button>
      <button onclick="v10Thumb(this,'https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png?v=1774119812&width=400')" style="width:72px;height:72px;border:1px solid #e6e6e6;background:#f9f9f9;padding:0;cursor:pointer;overflow:hidden;flex-shrink:0;"><img class="card-img-el" src="https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png?v=1774119812&width=400" style="width:100%;height:100%;object-fit:cover;display:block;" alt="View 4" /></button>
    </div>
  </div>

  <!-- BUY PANEL -->
  <div class="pdp-buy" style="gap:20px;">

    <!-- Reviews -->
    <div style="display:flex;align-items:center;gap:10px;">
      <span class="pdp-buy__stars" style="font-size:14px;letter-spacing:1px;">★★★★★</span>
      <span style="font-size:13px;font-weight:400;color:#4a4a4a;">Trusted by 1000's of Instructors</span>
      <span style="color:#d6cfc0;">·</span>
      <a href="#reviews" style="font-size:12px;color:#8a8a8a;font-weight:400;">Reviews →</a>
    </div>

    <!-- Title block -->
    <div>
      <!-- H1 = Shopify product title + badge inline -->
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;">
        <h1 style="font-size:18px;letter-spacing:0;color:#2d2926;font-weight:600;margin:0;">Best Grippy Shoes for Barre, Pilates &amp; Yoga</h1>
        <span class="pdp-buy__badge">Closed Sole</span>
      </div>
      <!-- Marketing headline -->
      <p class="pdp-buy__name" style="margin:0;"><span style="font-weight:300;">Secure in every hold.</span><br/><span style="font-weight:700;">No sliding. No resets.</span></p>
      <!-- Desc -->
      <p class="pdp-buy__desc" style="margin-top:16px;max-width:40ch;line-height:1.65;font-weight:400;color:#5a5248;">The premium grip system that replaces traditional grip socks—built for reformer, barre, Pilates and Megaformer.</p>
    </div>

    <!-- Price -->
    <div style="padding:16px 0;border-top:1px solid #e6e6e6;border-bottom:1px solid #e6e6e6;">
      <span class="pdp-buy__price-now">$74</span>
      <span style="font-size:13px;color:#8a8a8a;margin-left:8px;">or 4 payments · free shipping over $150</span>
    </div>

    <!-- Color -->
    <div style="padding:16px 0;border-bottom:1px solid #e6e6e6;">
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px;">
        <span style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;">Color · <span id="v10-color-name">Onyx</span></span>
        <a href="#variants" style="font-size:12px;text-decoration:none;color:#8a8a8a;font-weight:400;">View all colors →</a>
      </div>
      <div class="pdp-buy__swatches" style="gap:6px;flex-wrap:wrap;row-gap:6px;">
        <button class="pdp-buy__swatch" style="background:#050505;" aria-selected="true" aria-label="Onyx" onclick="v10Color(this,'Onyx','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#e9d3cb;" aria-label="Dusty Rose" onclick="v10Color(this,'Dusty Rose','https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#c9c5b8;" aria-label="Stone" onclick="v10Color(this,'Stone','https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg?v=1773920300&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#7b8c84;" aria-label="Sage" onclick="v10Color(this,'Sage','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#fff;border-color:#ccc;" aria-label="White" onclick="v10Color(this,'White','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#d4a78a;" aria-label="Terracotta" onclick="v10Color(this,'Terracotta','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#3d3530;" aria-label="Espresso" onclick="v10Color(this,'Espresso','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#b8c4c0;" aria-label="Mist" onclick="v10Color(this,'Mist','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#e8e0d0;" aria-label="Cream" onclick="v10Color(this,'Cream','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#8b7355;" aria-label="Mocha" onclick="v10Color(this,'Mocha','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <button class="pdp-buy__swatch" style="background:#5c6b5e;" aria-label="Forest" onclick="v10Color(this,'Forest','https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800')"></button>
        <div style="position:relative;display:inline-flex;">
          <button class="pdp-buy__swatch" style="background:#c8b99a;" aria-label="Coperni" onclick="v10Color(this,'Coperni','https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png?v=1774119812&width=800')"></button>
          <span style="position:absolute;top:-2px;right:-2px;background:#2563eb;color:#fff;font-size:8px;font-weight:700;padding:1px 4px;border-radius:2px;line-height:1.4;pointer-events:none;">LE</span>
        </div>
      </div>
    </div>

    <!-- Size -->
    <div style="padding:16px 0;border-bottom:1px solid #e6e6e6;">
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px;">
        <span style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;">Size · <span id="v10-size-name">L</span></span>
        <a href="#" style="font-size:12px;text-decoration:underline;color:#1c1916;">Size chart</a>
      </div>
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;">
        <button style="padding:14px;border:1px solid #e6e6e6;background:#fff;text-align:center;cursor:pointer;font-size:14px;font-weight:600;border-radius:6px;font-family:inherit;" onclick="v10Size(this,'M')">M<span style="display:block;font-size:11px;color:#8a8a8a;font-weight:400;margin-top:4px;">Women 5–7.5 · Men 6–8</span></button>
        <button style="padding:14px;border:2px solid #1c1916;background:#f9f9f9;text-align:center;cursor:pointer;font-size:14px;font-weight:600;border-radius:6px;font-family:inherit;" onclick="v10Size(this,'L')">L<span style="display:block;font-size:11px;color:#8a8a8a;font-weight:400;margin-top:4px;">Women 8–10 · Men 8.5–11</span></button>
      </div>
    </div>

    <!-- CTA -->
    <button class="pdp-buy__cta">Add to cart · $74</button>

    <!-- Trust -->
    <div style="display:flex;gap:20px;flex-wrap:wrap;font-size:12px;color:#8a8a8a;padding:12px 0;border-top:1px solid #e6e6e6;">
      <span><b style="color:#1c1916;">✓</b> Ships 1–2 days</span>
      <span><b style="color:#1c1916;">✓</b> 30-day returns</span>
      <span><b style="color:#1c1916;">✓</b> 90-day warranty</span>
      <span><b style="color:#1c1916;">✓</b> Latex- &amp; silicone-free</span>
    </div>

    <!-- Accordion -->
    <div style="border-top:1px solid #e6e6e6;">
      <details style="border-bottom:1px solid #e6e6e6;">
        <summary style="padding:14px 0;font-size:14px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;">Description <span>+</span></summary>
        <div style="padding:0 0 16px;font-size:14px;color:#4a4a4a;line-height:1.7;">
          <p style="margin:0 0 10px;">The Studio Performance Skin Closed Sole is the premium grip system that replaced traditional studio socks for thousands of reformer, barre, Megaformer, and Pilates practitioners. Full-contact 360° grip across the entire underfoot — not patches, not gels — for consistent traction every transition, every class.</p>
          <p style="margin:0;">Built from non-toxic, skin-safe materials with no latex and no silicone. Rinses clean in warm soapy water and air-dries in under an hour.</p>
        </div>
      </details>
      <details style="border-bottom:1px solid #e6e6e6;">
        <summary style="padding:14px 0;font-size:14px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;">Care &amp; how to wear <span>+</span></summary>
        <div style="padding:0 0 16px;font-size:14px;color:#4a4a4a;line-height:1.7;">
          <p style="margin:0 0 10px;"><b>How to put on:</b> pull from the top of the foot — not the straps — to help extend their lifespan.</p>
          <p style="margin:0;"><b>Cleaning:</b> warm soapy water, rinse well, air dry. No machine washing.</p>
        </div>
      </details>
      <details style="border-bottom:1px solid #e6e6e6;">
        <summary style="padding:14px 0;font-size:14px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;">Shipping <span>+</span></summary>
        <div style="padding:0 0 16px;font-size:14px;color:#4a4a4a;line-height:1.7;">Free shipping on orders over $75. Standard 3–5 days. Express 1–2 days at checkout.</div>
      </details>
      <details style="border-bottom:1px solid #e6e6e6;">
        <summary style="padding:14px 0;font-size:14px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;">30-day returns + 90-day warranty <span>+</span></summary>
        <div style="padding:0 0 16px;font-size:14px;color:#4a4a4a;line-height:1.7;">30-day returns on items returned in new, unused condition. 90-day warranty covers grip-surface wear under normal use.</div>
      </details>
    </div>
  </div>
</section>

<script>
function v10Thumb(btn, src) {
  document.querySelectorAll('.pdp-hero button[onclick^="v10Thumb"]').forEach(b => b.style.border = '1px solid #e6e6e6');
  btn.style.border = '2px solid #1c1916';
  document.getElementById('v10-main-img').src = src;
}
function v10Color(btn, name, src) {
  document.querySelectorAll('.pdp-buy__swatch').forEach(s => s.removeAttribute('aria-selected'));
  btn.setAttribute('aria-selected','true');
  document.getElementById('v10-color-name').textContent = name;
  document.getElementById('v10-main-img').src = src;
}
function v10Size(btn, name) {
  document.querySelectorAll('[onclick^="v10Size"]').forEach(s => { s.style.border='1px solid #e6e6e6'; s.style.background='#fff'; });
  btn.style.border = '2px solid #1c1916';
  btn.style.background = '#f9f9f9';
  document.getElementById('v10-size-name').textContent = name;
}
</script>

<!-- BRAND SECTION -->
<section style="padding:40px 40px 36px;background:#f5f2ec;">
  <div style="max-width:1240px;margin:0 auto;">

    <div style="margin-bottom:72px;">
      <p style="font-size:11px;text-transform:uppercase;letter-spacing:0.1em;color:#9a9182;font-weight:600;margin:0 0 16px;">Why Barreletics</p>
      <h2 style="font-size:40px;line-height:1.1;color:#1c1916;margin:0;max-width:18ch;"><span style="font-weight:300;">Confidence, from the</span><br/><span style="font-weight:700;">ground up.</span></h2>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:64px 80px;">

      <div style="border-top:1px solid #d6cfc0;padding-top:32px;">
        <p style="font-size:18px;font-weight:700;color:#1c1916;margin:0 0 10px;line-height:1.2;">360° grip — not patches.</p>
        <p style="font-size:15px;color:#4a4a4a;line-height:1.65;margin:0;">Full-contact underfoot grip across every surface. Not patches, not gels — consistent traction every transition, every class.</p>
      </div>

      <div style="border-top:1px solid #d6cfc0;padding-top:32px;">
        <p style="font-size:18px;font-weight:700;color:#1c1916;margin:0 0 10px;line-height:1.2;">One pair. 1,000+ classes.</p>
        <p style="font-size:15px;color:#4a4a4a;line-height:1.65;margin:0;">Grip socks wear out in 4–8 weeks. Barreletics are engineered to hold their grip through a year of regular studio use — without degrading.</p>
      </div>

      <div style="border-top:1px solid #d6cfc0;padding-top:32px;">
        <p style="font-size:18px;font-weight:700;color:#1c1916;margin:0 0 10px;line-height:1.2;">Replaces eight pairs.</p>
        <p style="font-size:15px;color:#4a4a4a;line-height:1.65;margin:0;">Eight grip sock replacements per year at $9 each = $72. One pair of Barreletics = $74. Same investment — no more sock runs.</p>
      </div>

      <div style="border-top:1px solid #d6cfc0;padding-top:32px;">
        <p style="font-size:18px;font-weight:700;color:#1c1916;margin:0 0 10px;line-height:1.2;">No latex. No silicone. No compromise.</p>
        <p style="font-size:15px;color:#4a4a4a;line-height:1.65;margin:0;">Non-toxic, skin-safe construction with no irritants. Rinse with warm water. Air dry. Back in class in under an hour.</p>
      </div>

    </div>
  </div>
</section>

<!-- VARIANTS -->
<section class="pdp-section" id="variants" style="padding-top:96px;padding-bottom:96px;">
  <div class="pdp-section__inner">

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:flex-end;margin-bottom:56px;">
      <div>
        <p class="pdp-section__label" style="margin-bottom:14px;">The Studio Collection</p>
        <h2 style="font-size:38px;line-height:1.08;color:#1c1916;margin:0;"><span style="font-weight:300;">One Performance.</span><br/><span style="font-weight:700;">Every Style.</span></h2>
      </div>
      <p style="font-size:15px;color:#6b6459;line-height:1.7;margin:0;max-width:36ch;">Same patented 360° grip. Choose the build that fits your practice.</p>
    </div>

    <div style="border-top:1px solid #e6e6e6;padding:13px 0;margin-bottom:52px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;border-bottom:1px solid #e6e6e6;">
      <div style="display:flex;align-items:center;gap:24px;">
        <button id="tab-closed" onclick="switchTab('closed')" style="font-size:12px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#1c1916;background:none;border:none;cursor:pointer;padding:0 0 2px;border-bottom:2px solid #1c1916;">Closed Sole</button>
        <button id="tab-open" onclick="switchTab('open')" style="font-size:12px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;color:#7a7268;background:none;border:none;cursor:pointer;padding:0 0 2px;border-bottom:2px solid transparent;">Open Sole</button>
        <span style="font-size:12px;font-weight:400;letter-spacing:0.06em;text-transform:uppercase;color:#b0a898;">Outdoor</span>
        <span style="font-size:12px;font-weight:400;letter-spacing:0.06em;text-transform:uppercase;color:#b0a898;">One-Off</span>
      </div>
      <div style="display:flex;align-items:center;gap:16px;">
        <div style="display:flex;align-items:center;gap:8px;">
          <span style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;color:#4a4a4a;">Size</span>
          <button id="size-m" onclick="switchSize('m')" style="font-size:11px;font-weight:700;color:#fff;background:#1c1916;padding:4px 10px;border:none;cursor:pointer;font-family:inherit;">M</button>
          <button id="size-l" onclick="switchSize('l')" style="font-size:11px;font-weight:700;color:#8a8a8a;background:#f0efec;padding:4px 10px;border:none;cursor:pointer;font-family:inherit;">L</button>
        </div>
        <a href="#" style="font-size:11px;color:#8a8a8a;text-decoration:none;border-bottom:1px solid #d0c8be;padding-bottom:1px;">Size Chart →</a>
        <a href="#" style="font-size:11px;color:#1c1916;font-weight:500;text-decoration:none;border-bottom:1px solid #1c1916;padding-bottom:1px;">Compare Open vs Closed →</a>
      </div>
    </div>

    <div id="grid-closed" style="display:grid;grid-template-columns:repeat(4,1fr);column-gap:28px;row-gap:60px;">
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=600" alt="Black" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Black</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size M (W 5.5–7.5)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=600" alt="Dusty Rose" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Dusty Rose</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size L (W 8–10)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
      <div style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg?v=1773920300&width=600" alt="Stone" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Stone</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size L (W 8–10)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:13px;font-weight:500;color:#9a9182;cursor:pointer;border-bottom:1px solid #d0c8be;padding-bottom:2px;">Notify Me →</span>
      </div>
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png?v=1774119812&width=600" alt="Coperni" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          <span style="position:absolute;top:10px;left:10px;font-size:8px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;background:#c45c3f;color:#fff;padding:2px 9px;border-radius:1px;line-height:1.3;">Limited Edition</span>
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Coperni</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole · Limited Edition</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size M (W 5.5–7.5)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$115</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=600" alt="Ebony" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Ebony</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size M (W 5.5–7.5)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=600" alt="Rust" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Rust</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size L (W 8–10)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
      <div style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg?v=1773920300&width=600" alt="Clay" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Clay</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size M (W 5.5–7.5)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:13px;font-weight:500;color:#9a9182;cursor:pointer;border-bottom:1px solid #d0c8be;padding-bottom:2px;">Notify Me →</span>
      </div>
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=600" alt="Sand" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Sand</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Closed Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size L (W 8–10)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
    </div>
    <div id="grid-open" style="display:none;grid-template-columns:repeat(4,1fr);column-gap:28px;row-gap:60px;">
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=600" alt="Black" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Black</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Open Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size M (W 5.5–7.5)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
      <div onmouseenter="this.querySelector('img').style.transform='scale(1.04)'" onmouseleave="this.querySelector('img').style.transform='scale(1)'" style="display:flex;flex-direction:column;">
        <div style="aspect-ratio:1;overflow:hidden;background:#f5f2ec;margin-bottom:26px;position:relative;">
          <img src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=600" alt="Dusty Rose" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.45s ease;">
          
        </div>
        <p style="font-size:24px;font-weight:700;color:#1c1916;margin:0 0 3px;line-height:1.1;">Dusty Rose</p>
        <p style="font-size:11px;color:#9a9182;margin:0 0 8px;font-weight:300;letter-spacing:0.01em;">Open Sole</p>
        <span style="display:inline-block;font-size:10px;font-weight:600;color:#6b6459;background:#ece9e3;padding:3px 8px;border-radius:20px;letter-spacing:0.04em;margin-bottom:10px;width:fit-content;">Size L (W 8–10)</span>
        <p style="font-size:13px;font-weight:700;color:#1c1916;margin:0 0 12px;">$74</p>
        <span style="font-size:15px;font-weight:600;color:#1c1916;cursor:pointer;border-bottom:1.5px solid #9a9182;padding-bottom:2px;letter-spacing:0.01em;">Add to Cart →</span>
      </div>
    </div>

  </div>
</section>
<script>
function switchTab(tab) {
  var closed = document.getElementById('grid-closed');
  var open = document.getElementById('grid-open');
  var tc = document.getElementById('tab-closed');
  var to = document.getElementById('tab-open');
  closed.style.display = tab === 'closed' ? 'grid' : 'none';
  open.style.display = tab === 'open' ? 'grid' : 'none';
  tc.style.color = tab === 'closed' ? '#1c1916' : '#7a7268';
  tc.style.fontWeight = tab === 'closed' ? '700' : '500';
  tc.style.borderBottom = tab === 'closed' ? '2px solid #1c1916' : '2px solid transparent';
  to.style.color = tab === 'open' ? '#1c1916' : '#7a7268';
  to.style.fontWeight = tab === 'open' ? '700' : '500';
  to.style.borderBottom = tab === 'open' ? '2px solid #1c1916' : '2px solid transparent';
}
function switchSize(size) {
  document.getElementById('size-m').style.background = size === 'm' ? '#1c1916' : '#f0efec';
  document.getElementById('size-m').style.color = size === 'm' ? '#fff' : '#8a8a8a';
  document.getElementById('size-l').style.background = size === 'l' ? '#1c1916' : '#f0efec';
  document.getElementById('size-l').style.color = size === 'l' ? '#fff' : '#8a8a8a';
}
</script>



<!-- REVIEWS WITH IMAGES -->
<section class="pdp-section" style="background:#f9f9f9;" id="reviews">
  <div class="pdp-section__inner">
    <p class="pdp-section__label">Trusted by studios & instructors</p>
    <h2 class="pdp-section__title">Real people. Real results.</h2>
    <div class="review-grid">
      <div class="review-card">
        <div class="review-image" style="background:linear-gradient(135deg, #c45c3f 0%, #e9a89f 100%);"></div>
        <div class="review-content">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"I've tried everything. This is the only grip system that lasts through my entire class."</p>
          <p class="review-author">Sarah M. · Barre Instructor, NYC</p>
        </div>
      </div>
      <div class="review-card">
        <div class="review-image" style="background:linear-gradient(135deg, #7b8c84 0%, #b8c9bf 100%);"></div>
        <div class="review-content">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"No slipping in chair pose. No adjusting mid-class. This is what I've been waiting for."</p>
          <p class="review-author">Jessica R. · Studio Owner, LA</p>
        </div>
      </div>
      <div class="review-card">
        <div class="review-image" style="background:linear-gradient(135deg, #e9d3cb 0%, #f5e9e0 100%);"></div>
        <div class="review-content">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"Invested a year ago. Still gripping the same. This is the upgrade I didn't know I needed."</p>
          <p class="review-author">Maya K. · Megaformer Lover, Chicago</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- VALUE COMPARISON -->
<section class="pdp-section" style="background:#f9f9f9;">
  <div class="pdp-section__inner">
    <h2 class="pdp-section__title">One pair replaces eight.</h2>
    <p style="font-size:16px;color:#4a4a4a;margin:0 0 48px 0;line-height:1.6;max-width:60ch;">Grip socks wear out. Barreletics don't. Compare the value over a year in the studio.</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px;">
      <div style="padding:32px;background:#fff;border-radius:12px;border:1px solid #e6e6e6;">
        <p style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#8a8a8a;font-weight:700;margin:0 0 12px 0;">Grip Socks</p>
        <p style="font-size:32px;font-weight:700;margin:0 0 20px 0;">$240/yr</p>
        <ul style="list-style:none;padding:0;margin:0;font-size:14px;color:#666;line-height:1.8;">
          <li>✗ Replace every 8–12 weeks</li>
          <li>✗ Inconsistent grip quality</li>
          <li>✗ Landfill waste</li>
          <li>✗ Comfort varies</li>
        </ul>
      </div>
      <div style="padding:32px;background:#1c1916;border-radius:12px;color:#fff;">
        <p style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#d4af37;font-weight:700;margin:0 0 12px 0;">Barreletics</p>
        <p style="font-size:32px;font-weight:700;margin:0 0 20px 0;color:#fff;">$74</p>
        <ul style="list-style:none;padding:0;margin:0;font-size:14px;color:#e6e6e6;line-height:1.8;">
          <li>✓ One pair, 1–4+ years</li>
          <li>✓ Grip never degrades</li>
          <li>✓ Zero waste</li>
          <li>✓ Same feel, always</li>
        </ul>
      </div>
      <div style="padding:32px;background:#fff;border-radius:12px;border:1px solid #e6e6e6;">
        <p style="font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#8a8a8a;font-weight:700;margin:0 0 12px 0;">Other Brands</p>
        <p style="font-size:32px;font-weight:700;margin:0 0 20px 0;">$180+/yr</p>
        <ul style="list-style:none;padding:0;margin:0;font-size:14px;color:#666;line-height:1.8;">
          <li>✗ Frequent replacements</li>
          <li>✗ Premium pricing</li>
          <li>✗ Limited sizes</li>
          <li>✗ Unproven durability</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- MOTION -->
<section class="pdp-section">
  <div class="pdp-section__inner">
    <p class="pdp-section__label">The shoe in motion</p>
    <h2 class="pdp-section__title">See how it works.</h2>
    <div class="pdp-motion-grid">
      <figure>
        <div class="pdp-motion__video">Play video</div>
        <figcaption class="pdp-motion__cap"><b>Slip it on</b> Just like a second skin.</figcaption>
      </figure>
      <figure>
        <div class="pdp-motion__video">Play video</div>
        <figcaption class="pdp-motion__cap"><b>Grip in motion</b> Through every transition.</figcaption>
      </figure>
      <figure>
        <div class="pdp-motion__video">Play video</div>
        <figcaption class="pdp-motion__cap"><b>Rinse & go</b> Warm soapy water · ready for next class.</figcaption>
      </figure>
    </div>
  </div>
</section>

<!-- JUSTIFIER FEED -->
<section class="pdp-section" style="background:#f5f2ec;">
  <div class="pdp-section__inner">
    <p class="pdp-section__label">Why studios choose us</p>
    <h2 class="pdp-section__title">Real feedback from the floor.</h2>
    <div class="pdp-justifier">
      <div class="pdp-justifier__card">
        <p class="pdp-justifier__tag">Instructor Trust</p>
        <p class="pdp-justifier__quote">"After 8 years of barre teaching, I've never seen my students slip in these. The consistency is insane."</p>
        <p class="pdp-justifier__author">Jennifer T. — Master Instructor</p>
      </div>
      <div class="pdp-justifier__card">
        <p class="pdp-justifier__tag">Studio Adoption</p>
        <p class="pdp-justifier__quote">"We recommend Barreletics to all new members now. It cuts our slip-related safety concerns to zero."</p>
        <p class="pdp-justifier__author">Brooklyn Barre Studio</p>
      </div>
      <div class="pdp-justifier__card">
        <p class="pdp-justifier__tag">Durability</p>
        <p class="pdp-justifier__quote">"After a year of daily use, zero degradation. This is a genuine upgrade from disposable socks."</p>
        <p class="pdp-justifier__author">Marcus L. — Pilates Professional</p>
      </div>
      <div class="pdp-justifier__card">
        <p class="pdp-justifier__tag">Customer Loyalty</p>
        <p class="pdp-justifier__quote">"I've bought 3 pairs for different studios. It's the only grip product I'll recommend to friends."</p>
        <p class="pdp-justifier__author">Amanda K. — Studio Hopper</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="pdp-faq">
  <div class="pdp-section__inner" style="max-width:760px;">
    <p class="pdp-section__label">Common questions</p>
    <h2 class="pdp-section__title">Everything you need to know.</h2>
    <div class="pdp-faq__container">
      <div class="pdp-faq__item">
        <button class="pdp-faq__trigger">What makes Barreletics different from grip socks? <span>▼</span></button>
        <div class="pdp-faq__body">Grip socks have two failure points: the toe box and the heel. Barreletics wraps your foot like a second skin with 360° grip from heel to toe. No slipping, no adjusting.</div>
      </div>
      <div class="pdp-faq__item">
        <button class="pdp-faq__trigger">Are Barreletics good for reformer Pilates? <span>▼</span></button>
        <div class="pdp-faq__body">Yes — engineered specifically for reformer Pilates, barre, Lagree and Megaformer. 294 verified reviews from studio instructors.</div>
      </div>
      <div class="pdp-faq__item">
        <button class="pdp-faq__trigger">How long do Barreletics last? <span>▼</span></button>
        <div class="pdp-faq__body">Customers report 1–4+ years with no grip degradation, even with daily studio use. One pair replaces 8–12 pairs of grip socks.</div>
      </div>
      <div class="pdp-faq__item">
        <button class="pdp-faq__trigger">How do you clean them? <span>▼</span></button>
        <div class="pdp-faq__body">Warm soapy water, air dry. Never machine wash or bleach. Grip lasts indefinitely with proper care.</div>
      </div>
      <div class="pdp-faq__item">
        <button class="pdp-faq__trigger">What size should I order? <span>▼</span></button>
        <div class="pdp-faq__body">M (W 5.5–7.5) and L (W 8–11). For men up to 10.5, choose Large.</div>
      </div>
    </div>
  </div>
</section>

<!-- NEWSLETTER -->
<section class="pdp-newsletter">
  <div class="pdp-newsletter__container">
    <p class="pdp-section__label">Join the list</p>
    <h2 class="pdp-newsletter__title">10% off your first pair.</h2>
    <p class="pdp-newsletter__desc">New drops, studio stories, care tips. Once or twice a quarter.</p>
    <form class="pdp-newsletter__form" onsubmit="event.preventDefault();">
      <input class="pdp-newsletter__input" type="email" placeholder="Email address" required />
      <button class="pdp-newsletter__button" type="submit">Get 10% off</button>
    </form>
    <p class="pdp-newsletter__fine">By subscribing you agree to receive marketing emails. Unsubscribe anytime.</p>
  </div>
</section>

<script>
  // Hero toggle
  document.querySelectorAll('.hero-toggle__btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const version = this.dataset.version;
      document.querySelectorAll('.pdp-hero').forEach(hero => hero.removeAttribute('data-active'));
      document.querySelector(`[data-version="${version}"]`).setAttribute('data-active', 'true');
      document.querySelectorAll('.hero-toggle__btn').forEach(b => b.removeAttribute('data-active'));
      this.setAttribute('data-active', 'true');
    });
  });

  // FAQ toggle
  document.querySelectorAll('.pdp-faq__trigger').forEach(trigger => {
    trigger.addEventListener('click', function() {
      const body = this.nextElementSibling;
      const isOpen = body.getAttribute('data-open') === 'true';
      body.setAttribute('data-open', !isOpen);
      this.textContent = this.textContent.replace(isOpen ? '▼' : '▲', isOpen ? '▲' : '▼');
    });
  });
</script>

</body>
</html>
---

### CSS Specifications (from pdp-styles.css)

/* ============================================================
   PDP pixel-final stylesheet
   Inherits all tokens from audit-styles.css
   ============================================================ */

html, body { background: #ffffff; }

/* ---------- Announcement + header ---------- */

/* ============================================================
   ROTATING TICKER — single strip, messages cross-fade
   ============================================================ */
.pdp-ticker {
  background: var(--br-text);
  color: #fff;
  height: 36px;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.pdp-ticker__slide {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0 16px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.55s ease, transform 0.55s ease;
  white-space: nowrap;
}
.pdp-ticker__slide.is-active {
  opacity: 1;
  transform: translateY(0);
}
.pdp-ticker__slide b { font-weight: 700; }
.pdp-ticker__slide a {
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,0.6);
  padding-bottom: 1px;
  margin-left: 6px;
}
.pdp-ticker__slide a:hover { color: #fff; border-color: #fff; }

@media (max-width: 600px) {
  .pdp-ticker__slide { font-size: 11px; letter-spacing: 0.08em; }
}

.pdp-announce {
  background: var(--br-text);
  color: #fff;
  text-align: center;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  padding: 11px 16px;
}

.pdp-announce--sale {
  background: var(--br-info);
  color: #fff;
  letter-spacing: 0.12em;
  font-weight: 600;
}
.pdp-announce--sale b { font-weight: 700; }

.pdp-announce--info {
  background: #fafafa;
  color: var(--br-text);
  font-weight: 500;
  font-size: 11.5px;
  border-bottom: 1px solid var(--br-line);
}
.pdp-announce--info a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  margin-left: 6px;
  font-weight: 500;
}
.pdp-announce--info a:hover { opacity: 0.7; }

.pdp-header {
  position: sticky;
  top: 0;
  z-index: 30;
  background: #ffffff;
  border-bottom: 1px solid var(--br-line);
}

.pdp-header__inner {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 18px 32px;
  gap: 24px;
}

.pdp-header__nav {
  display: flex;
  gap: 30px;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.01em;
}
.pdp-header__nav a {
  color: var(--br-text);
  text-decoration: none;
  padding: 4px 0;
  border-bottom: 1px solid transparent;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.pdp-header__nav a:hover { border-color: var(--br-text); }
.pdp-header__chev {
  font-size: 12px;
  line-height: 1;
  display: inline-block;
  margin-top: -1px;
  opacity: 0.7;
}

.pdp-header__logo {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 200px;
  height: 38px;
  padding: 0 8px;
  text-decoration: none;
}
.pdp-header__logo img {
  display: block;
  height: 100%;
  width: auto;
}
.pdp-header__logo--placeholder {
  border: 1px dashed var(--br-line);
  background: rgba(0,0,0,0.015);
  padding: 0 16px;
}
.pdp-header__logo span {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 10.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-mute);
  text-transform: lowercase;
}

.pdp-header__util {
  display: flex;
  gap: 24px;
  justify-content: flex-end;
  align-items: center;
  font-size: 13px;
  font-weight: 500;
}
.pdp-header__util a {
  color: var(--br-text);
  text-decoration: none;
  position: relative;
}
.pdp-header__cart {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.pdp-header__cart-dot {
  width: 24px; height: 24px;
  background: var(--br-accent);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0;
}
.pdp-header__cart-dot::before {
  content: "0";
}

/* ---------- Crumb ---------- */
.pdp-crumb {
  max-width: 1440px;
  margin: 0 auto;
  padding: 18px 32px 0;
  font-size: 11.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text-mute);
}
.pdp-crumb a { color: inherit; text-decoration: none; }
.pdp-crumb a:hover { color: var(--br-text); }

/* ============================================================
   PDP MAIN — gallery + buy box
   ============================================================ */

.pdp-main {
  max-width: 1440px;
  margin: 0 auto;
  padding: 32px 32px 80px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: flex-start;
}

@media (max-width: 1000px) {
  .pdp-main { grid-template-columns: 1fr; gap: 32px; }
}

/* Gallery */
.pdp-gallery {
  display: grid;
  grid-template-columns: 88px 1fr;
  gap: 12px;
  position: sticky;
  top: 88px;
}
@media (max-width: 700px) {
  .pdp-gallery { grid-template-columns: 1fr; position: static; }
  .pdp-gallery__thumbs { display: flex; flex-direction: row; }
}

.pdp-gallery__thumbs {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.pdp-gallery__thumb {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 10px, #e8e4d6 10px 20px);
  border: 1px solid transparent;
  cursor: pointer;
  position: relative;
}
.pdp-gallery__thumb[aria-selected="true"] { border-color: var(--br-text); }
.pdp-gallery__thumb--blush {
  background:
    repeating-linear-gradient(135deg, #f3e3dc 0 10px, #efdcd2 10px 20px);
}
.pdp-gallery__thumb--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 10px, #232323 10px 20px);
}
.pdp-gallery__thumb--video::after {
  content: "▶";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 16px;
  color: rgba(255,255,255,0.8);
}

.pdp-gallery__hero {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 12px;
  color: #8a7e63;
  position: relative;
}
.pdp-gallery__zoom {
  position: absolute;
  bottom: 12px;
  right: 12px;
  width: 36px;
  height: 36px;
  background: rgba(255,255,255,0.9);
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 16px;
  color: var(--br-text);
}

/* Buy box */
.pdp-buy {
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding-top: 6px;
}

.pdp-buy__judge {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--br-text-soft);
}
.pdp-buy__stars {
  color: var(--br-accent);
  letter-spacing: 0.16em;
}
.pdp-buy__judge a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  font-weight: 500;
}

.pdp-buy__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  margin: 0;
}

.pdp-buy__name {
  font-size: clamp(28px, 3vw, 40px);
  font-weight: 400;
  margin: 0;
  letter-spacing: -0.015em;
  line-height: 1.1;
}

/* v2 — Brand-line dominant hierarchy */
.pdp-buy__seo-label {
  font-size: 16px;
  font-weight: 500;
  letter-spacing: -0.005em;
  color: var(--br-text);
  margin: 6px 0 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--br-line);
  line-height: 1.3;
}

.pdp-buy__name--brand {
  font-size: clamp(34px, 3.8vw, 52px);
  font-weight: 400;
  line-height: 1;
  letter-spacing: -0.02em;
}
.pdp-buy__seo {
  font-size: 15px;
  line-height: 1.4;
  color: var(--br-text-soft);
  margin: 14px 0 0;
  max-width: 50ch;
  font-weight: 400;
}

.pdp-buy__tagline {
  font-size: clamp(17px, 1.6vw, 20px);
  font-weight: 500;
  color: var(--br-text);
  margin: 10px 0 0;
  letter-spacing: -0.005em;
  line-height: 1.3;
}

.pdp-buy__sub {
  font-size: 15px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
  max-width: 50ch;
}

.pdp-buy__price {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-top: 4px;
}
.pdp-buy__price-now {
  font-size: 22px;
  font-weight: 500;
}
.pdp-buy__price-meta {
  font-size: 12.5px;
  color: var(--br-text-soft);
  letter-spacing: 0.04em;
}

.pdp-buy__row { display: flex; flex-direction: column; gap: 10px; }
.pdp-buy__row-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--br-text);
}
.pdp-buy__row-head a {
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  font-weight: 500;
}

.pdp-buy__swatches {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.pdp-buy__swatch {
  width: 36px;
  height: 36px;
  border: 1px solid var(--br-line);
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  transition: border-color 0.12s, transform 0.12s;
}
.pdp-buy__swatch:hover { transform: scale(1.06); }
.pdp-buy__swatch[aria-selected="true"] {
  border-color: var(--br-text);
  box-shadow: inset 0 0 0 2px #fff;
}
.pdp-buy__swatch[data-le]::after {
  content: "LE";
  position: absolute;
  top: -8px; right: -8px;
  background: var(--br-le);
  color: #fff;
  font-size: 8.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 2px 5px 1px;
  border-radius: 2px;
}

.pdp-buy__sizes {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 6px;
}
.pdp-buy__sizes--two {
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.pdp-buy__size {
  border: 1px solid var(--br-text);
  background: #fff;
  padding: 12px 4px;
  text-align: center;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.12s, color 0.12s;
}
.pdp-buy__size--wide {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 16px 12px;
}
.pdp-buy__size-letter {
  font-size: 22px;
  font-weight: 500;
  letter-spacing: 0.04em;
  line-height: 1;
}
.pdp-buy__size-meta {
  font-size: 11px;
  letter-spacing: 0.04em;
  color: var(--br-text-soft);
  text-transform: none;
}
.pdp-buy__size--wide[aria-selected="true"] .pdp-buy__size-meta {
  color: rgba(255,255,255,0.78);
}
.pdp-buy__size:hover { background: var(--br-text); color: #fff; }
.pdp-buy__size[aria-selected="true"] { background: var(--br-text); color: #fff; }
.pdp-buy__size[disabled] {
  opacity: 0.34;
  color: var(--br-text-mute);
  border-color: var(--br-line);
  text-decoration: line-through;
  cursor: not-allowed;
}
.pdp-buy__size[disabled]:hover { background: transparent; color: var(--br-text-mute); }

.pdp-buy__cta-row {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-buy__cta {
  background: var(--br-text);
  color: #fff;
  border: 0;
  padding: 18px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: opacity 0.15s;
  text-align: center;
}
.pdp-buy__cta:hover { opacity: 0.88; }

.pdp-buy__shipnote {
  display: flex;
  gap: 16px;
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  flex-wrap: wrap;
}
.pdp-buy__shipnote span::before {
  content: "✓ ";
  color: var(--br-accent);
  margin-right: 2px;
  font-weight: 700;
}

.pdp-buy__tabs {
  border-top: 1px solid var(--br-line);
  margin-top: 4px;
}
.pdp-buy__tab {
  border-bottom: 1px solid var(--br-line);
}
.pdp-buy__tab summary {
  list-style: none;
  cursor: pointer;
  padding: 16px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.06em;
}
.pdp-buy__tab summary::-webkit-details-marker { display: none; }
.pdp-buy__tab summary::after {
  content: "+";
  font-weight: 300;
  font-size: 22px;
  color: var(--br-text-mute);
  transition: transform 0.15s;
}
.pdp-buy__tab[open] summary::after {
  content: "−";
}
.pdp-buy__tab-body {
  padding: 0 0 18px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--br-text-soft);
}
.pdp-buy__tab-body p { margin: 0 0 10px; }
.pdp-buy__tab-body p:last-child { margin-bottom: 0; }

/* ============================================================
   PILLAR STRIP
   ============================================================ */

.pdp-pillars {
  background: var(--br-alt-bg);
  border-top: 1px solid var(--br-line);
  border-bottom: 1px solid var(--br-line);
}
.pdp-pillars__inner {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  align-items: stretch;
}
.pdp-pillars__label {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--br-text);
  white-space: nowrap;
  padding: 18px 28px;
  background: #fff;
  border-right: 1px solid var(--br-line);
  display: flex;
  align-items: center;
}
.pdp-pillars__pts {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 32px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  gap: 20px;
}
.pdp-pillars__div {
  width: 1px;
  height: 14px;
  background: var(--br-line);
}

@media (max-width: 800px) {
  .pdp-pillars__label { display: none; }
  .pdp-pillars__pts {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    font-size: 10.5px;
    text-align: center;
  }
  .pdp-pillars__div { display: none; }
}

/* ============================================================
   SECTION HELPERS
   ============================================================ */

.pdp-section {
  max-width: 1440px;
  margin: 0 auto;
  padding: 96px 32px;
}
.pdp-section--tight { padding: 64px 32px; }
.pdp-section--alt { background: var(--br-alt-bg); max-width: none; }
.pdp-section--alt > * {
  max-width: 1440px;
  margin-left: auto;
  margin-right: auto;
}

.pdp-eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text);
  margin: 0 0 14px;
}

.pdp-h2 {
  font-size: clamp(28px, 3.2vw, 44px);
  font-weight: 500;
  letter-spacing: -0.01em;
  line-height: 1.1;
  margin: 0;
  text-wrap: balance;
}

.pdp-h3 {
  font-size: clamp(20px, 1.6vw, 24px);
  font-weight: 500;
  letter-spacing: -0.005em;
  line-height: 1.2;
  margin: 0;
}

.pdp-lede {
  font-size: 18px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 16px 0 0;
  max-width: 60ch;
}

/* ============================================================
   PREMIUM / VALUE BLOCK — addresses the "expensive" objection
   ============================================================ */

.pdp-value {
  background: var(--br-text);
  color: #fff;
}
.pdp-value__inner {
  max-width: 1440px;
  margin: 0 auto;
  padding: 96px 32px;
  display: grid;
  grid-template-columns: 1fr 1.1fr;
  gap: 64px;
  align-items: center;
}
@media (max-width: 900px) {
  .pdp-value__inner { grid-template-columns: 1fr; padding: 64px 24px; gap: 32px; }
}

.pdp-value__copy .pdp-eyebrow { color: rgba(255,255,255,0.7); }
.pdp-value__copy .pdp-h2 { color: #fff; }
.pdp-value__copy .pdp-lede { color: rgba(255,255,255,0.78); }

.pdp-value__compare {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.12);
}
.pdp-value__col {
  padding: 26px 24px;
  background: var(--br-text);
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-value__col--ours { background: #1a1a1a; }
.pdp-value__tag {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.6);
}
.pdp-value__col--ours .pdp-value__tag { color: var(--br-accent); }
.pdp-value__amount {
  font-size: clamp(28px, 3vw, 38px);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1;
  color: #fff;
  margin: 4px 0 12px;
}
.pdp-value__amount-unit {
  font-size: 13px;
  font-weight: 400;
  color: rgba(255,255,255,0.55);
  letter-spacing: 0;
  margin-left: 4px;
}
.pdp-value__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 13.5px;
  color: rgba(255,255,255,0.78);
}
.pdp-value__list li {
  position: relative;
  padding-left: 16px;
}
.pdp-value__list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 1px;
  background: rgba(255,255,255,0.4);
}
.pdp-value__col--ours .pdp-value__list li::before {
  background: var(--br-accent);
}

/* ============================================================
   BENEFIT GRID — PDP variant
   ============================================================ */

.pdp-benefits {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 48px;
}
@media (max-width: 800px) {
  .pdp-benefits { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 520px) {
  .pdp-benefits { grid-template-columns: 1fr; }
}

.pdp-benefit {
  background: #fff;
  border-top: 2px solid var(--br-text);
  padding: 22px 22px 26px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.pdp-benefit__num {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  letter-spacing: 0.12em;
  color: var(--br-text-mute);
  margin-bottom: 8px;
}
.pdp-benefit__title {
  font-size: 17px;
  font-weight: 600;
  margin: 0;
  letter-spacing: -0.005em;
}
.pdp-benefit__sub {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  margin: 0;
}

/* ============================================================
   MEDIA SPLIT (story block)
   ============================================================ */

.pdp-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  min-height: 580px;
}
@media (max-width: 900px) {
  .pdp-split { grid-template-columns: 1fr; min-height: 0; }
}

.pdp-split__media {
  background:
    repeating-linear-gradient(135deg, #efece2 0 18px, #e8e4d6 18px 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7a6f5b;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  min-height: 100%;
  position: relative;
}
.pdp-split__media--dark {
  background:
    repeating-linear-gradient(135deg, #2c2c2c 0 18px, #232323 18px 36px);
  color: #a39a83;
}
.pdp-split__media-tag {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: rgba(0,0,0,0.5);
  color: #fff;
  padding: 5px 9px;
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: 0;
}

.pdp-split__copy {
  padding: 80px 64px;
  background: var(--br-alt-bg);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
@media (max-width: 900px) {
  .pdp-split__copy { padding: 48px 24px; }
  .pdp-split__media { aspect-ratio: 4/5; }
}
.pdp-split__copy .pdp-h2 { margin-bottom: 16px; }

.pdp-split__list {
  list-style: none;
  margin: 28px 0 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 15px;
}
.pdp-split__list li {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.pdp-split__list li::before {
  content: "→";
  color: var(--br-accent);
  font-weight: 700;
  flex-shrink: 0;
}

/* ============================================================
   TESTIMONIAL
   ============================================================ */

.pdp-quote {
  text-align: center;
  max-width: 760px;
  margin: 0 auto;
}
.pdp-quote__stars {
  color: var(--br-accent);
  letter-spacing: 0.2em;
  font-size: 18px;
  margin-bottom: 22px;
}
.pdp-quote__body {
  font-size: clamp(22px, 2.4vw, 32px);
  font-weight: 400;
  line-height: 1.35;
  margin: 0 0 24px;
  text-wrap: balance;
  letter-spacing: -0.005em;
  color: var(--br-text);
}
.pdp-quote__attr {
  font-size: 11.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pdp-quote__attr b {
  color: var(--br-text);
  font-weight: 700;
  margin-right: 8px;
}

/* ============================================================
   VARIANT GRID — "Shop all colors & sizes"
   ============================================================ */

.pdp-variants__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}
.pdp-variants__head-meta { display: flex; flex-direction: column; gap: 4px; }
.pdp-variants__head-link {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
}

.pdp-variants__tabs {
  display: flex;
  gap: 0;
  margin-bottom: 28px;
}
.pdp-variant-tab {
  font-family: inherit;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.04em;
  padding: 12px 22px;
  border: 1px solid var(--br-text);
  background: #fff;
  color: var(--br-text);
  cursor: pointer;
  margin: 0 -1px 0 0;
  position: relative;
  transition: background 0.12s, color 0.12s;
}
.pdp-variant-tab[aria-selected="true"] {
  background: var(--br-text);
  color: #fff;
  z-index: 2;
}
.pdp-variant-tab:hover:not([aria-selected="true"]) {
  background: var(--br-alt-bg);
}

.pdp-variants__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 1000px) { .pdp-variants__grid { grid-template-columns: repeat(2, 1fr); } }

.pdp-vcard {
  background: #fff;
  display: flex;
  flex-direction: column;
  position: relative;
  cursor: pointer;
}
.pdp-vcard__media {
  aspect-ratio: 1/1;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  margin-bottom: 14px;
  position: relative;
  overflow: hidden;
}
.pdp-vcard__media--blush {
  background: repeating-linear-gradient(135deg, #f3e3dc 0 14px, #efdcd2 14px 28px);
}
.pdp-vcard__media--stone {
  background: repeating-linear-gradient(135deg, #d4d0c4 0 14px, #c9c5b8 14px 28px);
}
.pdp-vcard__media--dark {
  background: repeating-linear-gradient(135deg, #2c2c2c 0 14px, #232323 14px 28px);
}
.pdp-vcard__le {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--br-le);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 4px 8px 3px;
}
.pdp-vcard__quick {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  background: rgba(255,255,255,0.96);
  color: var(--br-text);
  padding: 10px;
  text-align: center;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  opacity: 0;
  transition: opacity 0.15s;
}
.pdp-vcard:hover .pdp-vcard__quick { opacity: 1; }

.pdp-vcard__title {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 2px;
  line-height: 1.35;
}
.pdp-vcard__meta {
  font-size: 12px;
  color: var(--br-text-soft);
  letter-spacing: 0.02em;
}
.pdp-vcard__price {
  font-size: 13px;
  font-weight: 500;
  margin-top: 2px;
}
.pdp-vcard__sale {
  color: var(--br-accent);
  font-weight: 500;
}
.pdp-vcard__sale s {
  color: var(--br-text-mute);
  text-decoration: line-through;
  font-weight: 400;
  margin-right: 4px;
}

/* ============================================================
   REVIEWS (Judge.me restyled)
   ============================================================ */

.pdp-reviews__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  margin-bottom: 32px;
  gap: 24px;
  flex-wrap: wrap;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--br-line);
}
.pdp-reviews__head-bigstars {
  font-size: 32px;
  color: var(--br-accent);
  letter-spacing: 0.18em;
  line-height: 1;
}
.pdp-reviews__head-summary {
  font-size: 14px;
  color: var(--br-text-soft);
  margin-top: 4px;
}
.pdp-reviews__head-summary b { color: var(--br-text); font-weight: 600; }

.pdp-reviews__grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0;
  border-top: 1px solid var(--br-line);
}
.pdp-review {
  padding: 24px 32px;
  border-bottom: 1px solid var(--br-line);
  border-right: 1px solid var(--br-line);
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.pdp-review:nth-child(2n) { border-right: 0; }
.pdp-review__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--br-text-soft);
}
.pdp-review__stars { color: var(--br-accent); letter-spacing: 0.16em; font-size: 13px; }
.pdp-review__verified {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.pdp-review__verified::before {
  content: "✓";
  color: var(--br-accent);
  font-weight: 700;
}
.pdp-review__title {
  font-size: 15px;
  font-weight: 600;
  margin: 0;
  letter-spacing: -0.005em;
}
.pdp-review__body {
  font-size: 14px;
  line-height: 1.6;
  color: var(--br-text);
  margin: 0;
}
.pdp-review__attr {
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--br-text-soft);
  margin: 0;
}
.pdp-review__attr b { color: var(--br-text); font-weight: 600; }

@media (max-width: 720px) {
  .pdp-reviews__grid { grid-template-columns: 1fr; }
  .pdp-review { border-right: 0; }
}

.pdp-reviews__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  margin-top: 32px;
  flex-wrap: wrap;
}
.pdp-reviews__more {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 2px;
  font-weight: 500;
}
.pdp-reviews__write {
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--br-text);
  text-decoration: none;
  background: var(--br-text);
  color: #fff;
  padding: 12px 20px;
  font-weight: 700;
}
.pdp-reviews__write:hover { opacity: 0.88; }

/* ============================================================
   FAQ
   ============================================================ */

.pdp-faq {
  max-width: 880px;
  margin: 0 auto;
}
.pdp-faq__list {
  margin-top: 32px;
  border-top: 1px solid var(--br-line);
}
.pdp-faq__item {
  border-bottom: 1px solid var(--br-line);
}
.pdp-faq__item summary {
  list-style: none;
  cursor: pointer;
  padding: 22px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  font-size: 17px;
  font-weight: 500;
  letter-spacing: -0.005em;
}
.pdp-faq__item summary::-webkit-details-marker { display: none; }
.pdp-faq__item summary::after {
  content: "+";
  font-size: 24px;
  font-weight: 300;
  color: var(--br-text-mute);
  flex-shrink: 0;
}
.pdp-faq__item[open] summary::after { content: "−"; }
.pdp-faq__body {
  padding: 0 0 22px;
  font-size: 15px;
  line-height: 1.65;
  color: var(--br-text-soft);
  max-width: 64ch;
}
.pdp-faq__body p { margin: 0 0 12px; }
.pdp-faq__body p:last-child { margin-bottom: 0; }
.pdp-faq__body a {
  color: var(--br-text);
  border-bottom: 1px solid var(--br-text);
  padding-bottom: 1px;
  text-decoration: none;
}

/* ============================================================
   PRODUCT RAIL — pairs with your kit
   ============================================================ */

.pdp-rail__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  margin-bottom: 32px;
  gap: 24px;
}
.pdp-rail__list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}
@media (max-width: 900px) { .pdp-rail__list { grid-template-columns: 1fr 1fr; } }

.pdp-rail-card {
  background: #fff;
  display: flex;
  flex-direction: column;
}
.pdp-rail-card__media {
  aspect-ratio: 4/5;
  background:
    repeating-linear-gradient(135deg, #efece2 0 14px, #e8e4d6 14px 28px);
  margin-bottom: 14px;
}
.pdp-rail-card__media--blush { background: repeating-linear-gradient(135deg, #f3e3dc 0 14px, #efdcd2 14px 28px); }
.pdp-rail-card__media--stone { background: repeating-linear-gradient(135deg, #d4d0c4 0 14px, #c9c5b8 14px 28px); }
.pdp-rail-card__media--dark  { background: repeating-linear-gradient(135deg, #2c2c2c 0 14px, #232323 14px 28px); }
.pdp-rail-card__title {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 2px;
}
.pdp-rail-card__price {
  font-size: 13px;
  color: var(--br-text-soft);
  margin: 0;
}

/* ============================================================
   Tweaks-controlled variants
   ============================================================ */

/* Quick Add legacy hover button kept for tweaks-panel testing only;
   the production default is the text-link .pdp-vcard__addlink */
.pdp-vcard__add {
  display: none !important;
}

/* Card style — bordered variant */
[data-card-style="bordered"] .pdp-vcard {
  border: 1px solid var(--br-line);
  padding: 12px;
  background: #fff;
  transition: border-color 0.15s;
}
[data-card-style="bordered"] .pdp-vcard:hover { border-color: var(--br-text); }
[data-card-style="bordered"] .pdp-vcard__media { margin-bottom: 12px; }

/* Verified badge toggle */
[data-verified="off"] .pdp-review__verified { display: none; }

/* CTA size variants */
[data-cta-size="compact"] .pdp-buy__cta { padding: 14px; font-size: 13px; }
[data-cta-size="bold"]    .pdp-buy__cta { padding: 22px; font-size: 15px; letter-spacing: 0.14em; }

/* ============================================================ */

.pdp-footer {
  background: #fff;
  border-top: 1px solid var(--br-line);
  padding: 80px 32px 32px;
}
.pdp-footer__grid {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.4fr repeat(4, 1fr);
  gap: 48px;
  padding-bottom: 56px;
  border-bottom: 1px solid var(--br-line);
}
@media (max-width: 900px) {
  .pdp-footer__grid { grid-template-columns: 1fr 1fr; gap: 32px; }
}
.pdp-footer__brand .pdp-header__logo {
  margin-bottom: 16px;
}
.pdp-footer__brand p {
  font-size: 14px;
  line-height: 1.55;
  color: var(--br-text-soft);
  max-width: 32ch;
  margin: 0 0 20px;
}
.pdp-footer__newsletter {
  display: flex;
  gap: 0;
  border: 1px solid var(--br-text);
}
.pdp-footer__newsletter input {
  flex: 1;
  padding: 12px 14px;
  font-family: inherit;
  font-size: 13px;
  border: 0;
  background: transparent;
  color: var(--br-text);
}
.pdp-footer__newsletter input::placeholder { color: var(--br-text-mute); }
.pdp-footer__newsletter button {
  background: var(--br-text);
  color: #fff;
  border: 0;
  padding: 12px 16px;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
}

.pdp-footer__col h6 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin: 0 0 18px;
  color: var(--br-text);
}
.pdp-footer__col ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pdp-footer__col a {
  color: var(--br-text-soft);
  text-decoration: none;
  font-size: 14px;
}
.pdp-footer__col a:hover { color: var(--br-text); }

.pdp-footer__bottom {
  max-width: 1440px;
  margin: 0 auto;
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 12px;
  color: var(--br-text-mute);
  letter-spacing: 0.02em;
}

---

### JavaScript Configuration (from pdp-tweaks.jsx)

/* global React, ReactDOM */
const { useEffect } = React;

const PDP_TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "quickAddMode": "hover",
  "showVerifiedBadge": true,
  "cardStyle": "clean",
  "ctaSize": "default"
}/*EDITMODE-END*/;

function PdpTweaks() {
  const [t, setTweak] = useTweaks(PDP_TWEAK_DEFAULTS);

  useEffect(() => {
    const root = document.documentElement;
    root.dataset.quickAdd = t.quickAddMode;
    root.dataset.verified = t.showVerifiedBadge ? 'on' : 'off';
    root.dataset.cardStyle = t.cardStyle;
    root.dataset.ctaSize = t.ctaSize;
  }, [t]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Variant grid · Quick Add">
        <TweakRadio
          label="Quick Add behavior"
          value={t.quickAddMode}
          onChange={v => setTweak('quickAddMode', v)}
          options={[
            { value: 'off',    label: 'Off' },
            { value: 'hover',  label: 'On hover' },
            { value: 'always', label: 'Always' },
          ]}
        />
        <TweakRadio
          label="Card style"
          value={t.cardStyle}
          onChange={v => setTweak('cardStyle', v)}
          options={[
            { value: 'clean',  label: 'Clean' },
            { value: 'bordered',label: 'Bordered' },
          ]}
        />
      </TweakSection>

      <TweakSection label="Reviews">
        <TweakToggle
          label="Show 'Verified buyer' badge"
          value={t.showVerifiedBadge}
          onChange={v => setTweak('showVerifiedBadge', v)}
        />
      </TweakSection>

      <TweakSection label="Primary CTA">
        <TweakRadio
          label="Button size"
          value={t.ctaSize}
          onChange={v => setTweak('ctaSize', v)}
          options={[
            { value: 'compact', label: 'Compact' },
            { value: 'default', label: 'Default' },
            { value: 'bold',    label: 'Bold' },
          ]}
        />
      </TweakSection>
    </TweaksPanel>
  );
}

ReactDOM.createRoot(document.getElementById('pdp-tweaks-root')).render(<PdpTweaks />);

---

## MATURED DESIGN SPECIFICATION (from Barreletics PDP - Matured.html)

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="icon" type="image/png" href="barreletics-mark.png" />
<title>Best Grippy Shoes for Barre, Pilates &amp; Yoga — Closed Sole | Barreletics — Matured</title>
<link href="maturation-styles.css" rel="stylesheet">
<meta name="description" content="Secure in every hold. The premium performance grip system built to replace traditional grip socks. Free shipping over $75 · 30-day returns · 90-day warranty." />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />

<link rel="stylesheet" href="audit-styles.css" />
<link rel="stylesheet" href="pdp-styles.css" />
</head>

<body data-screen-label="PDP · Studio Performance Skin Closed Sole" data-matured="on" data-ground="warm">

<!-- ============================== ANNOUNCEMENT + HEADER ============================== -->
<div class="pdp-ticker" aria-live="polite">
  <span class="pdp-ticker__slide is-active">Buy 2 Save 15% · use code <b>SAVE15</b></span>
  <span class="pdp-ticker__slide">🇺🇸 Made in USA · Free shipping over $150 · 30-day returns &nbsp;<a href="#">details →</a></span>
  <span class="pdp-ticker__slide">★ Trusted by 1000's of Instructors</span>
</div>

<header class="pdp-header">
  <div class="pdp-header__inner">
            <nav class="pdp-header__nav">
      <a href="Barreletics Collection.html">Grippy Footwear <span class="pdp-header__chev">⌄</span></a>
      <a href="#">Apparel <span class="pdp-header__chev">⌄</span></a>
      <a href="#">Collaborations <span class="pdp-header__chev">⌄</span></a>
      <a href="Barreletics Blog.html">Journal</a>
      <a href="#">About Us <span class="pdp-header__chev">⌄</span></a>
    </nav>
    <a href="Barreletics Home.html" class="pdp-header__logo" aria-label="Barreletics — home"><img src="barreletics-logo.png" alt="Barreletics" /></a>
    <div class="pdp-header__util">
      <a href="#">Account</a>
      <a href="#" class="pdp-header__cart">Cart <span class="pdp-header__cart-dot"></span></a>
    </div>
  </div>
</header>

<!-- Cross-tab nav between mockups (review aid — strip out before launch) -->
<div class="pg-tab-strip">
  <div class="pg-tab-strip__inner">
    <span class="pg-tab-strip__label">Mock pages</span>
    <a href="Barreletics Home.html" >v1</a>
    <a href="Barreletics Home v2.html" >v2 · cinematic</a>
    <a href="Barreletics Home v3.html" >v3 · multi-tile</a>
    <a href="Barreletics Home v4.html" >v4 · hybrid</a>
    <a href="Barreletics Home v5a.html" >v5a · Coperni</a>
    <a href="Barreletics Home v5b.html" >v5b · no-collab</a>
    <a href="Barreletics Home v6.html" >v6 · editorial</a>
    <a href="Barreletics Home v7.html" >v7 · video hero</a>
    <a href="Barreletics Home v8.html" >v8 · ed+video</a>
    <a href="Barreletics Home v9.html" >v9 · image-led</a>
    <a href="Barreletics PDP.html" >PDP v1</a>
    <a href="Barreletics PDP v2.html" aria-current="page">PDP v2</a>
    <a href="Barreletics Collection.html" >Coll</a>
    <a href="Barreletics Article.html" >Article</a>
    <a href="Barreletics Blog.html" >Blog</a>
    <span style="margin-left: auto; font-size: 11px; color: var(--br-text-mute); letter-spacing: 0.08em; text-transform: uppercase;">v2 mocks</span>
  </div>
</div>

<!-- crumb -->
<nav class="pdp-crumb">
  <a href="#">Shop</a> &nbsp;/&nbsp; <a href="#">Studio</a> &nbsp;/&nbsp; <a href="#">Closed sole</a> &nbsp;/&nbsp; Studio Performance Skin
</nav>


<!-- ============================== PDP MAIN ============================== -->
<section class="pdp-main">

  <!-- Gallery -->
  <div class="pdp-gallery">
    <div class="pdp-gallery__thumbs">
      <div class="pdp-gallery__thumb" aria-selected="true">[1]</div>
      <div class="pdp-gallery__thumb pdp-gallery__thumb--blush">[2]</div>
      <div class="pdp-gallery__thumb">[3]</div>
      <div class="pdp-gallery__thumb pdp-gallery__thumb--dark pdp-gallery__thumb--video"></div>
      <div class="pdp-gallery__thumb">[5]</div>
    </div>
    <div class="pdp-gallery__hero" style="background: #f7f5f1;"><img src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800" alt="Closed Sole Black" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-gallery__zoom">⊕</div></div>
  </div>

  <!-- Buy box -->
  <div class="pdp-buy">
    <div class="pdp-buy__judge">
      <span class="pdp-buy__stars" style="color: var(--br-star);">★★★★★</span>
      <span><b>Trusted by 1000's of Instructors</b> · <a href="#reviews">read verified reviews</a></span>
    </div>

    <div class="pdp-buy__title-block">
      <p class="pdp-buy__eyebrow" style="color: var(--br-accent);">Studio Performance Skin · Closed Sole</p>
      <p class="pdp-buy__seo-label">Best Grippy Shoes for Barre, Pilates &amp; Yoga</p>
      <h1 class="pdp-buy__name pdp-buy__name--brand">Secure in every hold.<br/>No sliding. No resets.</h1>
      <p class="pdp-buy__seo">The premium grip system that replaced traditional studio socks — built for reformer, barre, and Megaformer.</p>
    </div>

    <p class="pdp-buy__sub"><b>Smarter Than Grip Socks.</b> A premium performance grip system for barre, reformer, Pilates, and Megaformer. Rinse, dry, reuse.</p>

    <div class="pdp-buy__price">
      <span class="pdp-buy__price-now">$74</span>
      <span class="pdp-buy__price-meta">or 4 payments of $18.50 · free shipping over $75</span>
    </div>

    <!-- color -->
    <div class="pdp-buy__row">
      <div class="pdp-buy__row-head">
        <span>Color · <b style="font-weight: 500;">Onyx</b></span>
        <a href="#variants">Compare all colors</a>
      </div>
      <div class="pdp-buy__swatches">
        <button class="pdp-buy__swatch" style="background:#050505;" aria-selected="true" aria-label="Onyx"></button>
        <button class="pdp-buy__swatch" style="background:#e9d3cb;" aria-label="Blush"></button>
        <button class="pdp-buy__swatch" style="background:#c9c5b8;" aria-label="Stone"></button>
        <button class="pdp-buy__swatch" style="background:#7b8c84;" aria-label="Sage"></button>
        <button class="pdp-buy__swatch" style="background:#ffffff; border-color:#bbb;" aria-label="Ivory"></button>
        <button class="pdp-buy__swatch" style="background:#3a3a3a;" data-le aria-label="Coperni × Closed (LE)"></button>
      </div>
    </div>

    <!-- size -->
    <div class="pdp-buy__row">
      <div class="pdp-buy__row-head">
        <span>Size · <b style="font-weight: 500;">L</b></span>
        <a href="#" aria-label="Open size guide">Size chart</a>
      </div>
      <div class="pdp-buy__sizes pdp-buy__sizes--two">
        <button class="pdp-buy__size pdp-buy__size--wide">
          <span class="pdp-buy__size-letter">M</span>
          <span class="pdp-buy__size-meta">Women&rsquo;s 5–7.5 · Men&rsquo;s 6–8</span>
        </button>
        <button class="pdp-buy__size pdp-buy__size--wide" aria-selected="true">
          <span class="pdp-buy__size-letter">L</span>
          <span class="pdp-buy__size-meta">Women&rsquo;s 8–10 · Men&rsquo;s 8.5–11</span>
        </button>
      </div>
    </div>

    <div class="pdp-buy__cta-row">
      <button class="pdp-buy__cta">Add to cart · $74</button>
      <div class="pdp-buy__shipnote">
        <span>Ships in 1–2 days</span>
        <span>30-day returns</span>
        <span>90-day warranty</span>
        <span>Latex- &amp; silicone-free</span>
      </div>
    </div>

    <div class="pdp-buy__tabs">
      <details class="pdp-buy__tab" open>
        <summary>Description</summary>
        <div class="pdp-buy__tab-body">
          <p>The Studio Performance Skin Closed Sole is the premium grip system that replaced traditional studio socks for thousands of reformer, barre, Megaformer, and Pilates practitioners. Full-contact 360° grip across the entire underfoot — not patches, not gels — for consistent traction every transition, every class, every sweat.</p>
          <p>Built from non-toxic, skin-safe materials with no latex and no silicone. Rinses clean in warm soapy water and air-dries in under an hour. The first grip footwear you wash instead of throwing away.</p>
        </div>
      </details>
      <details class="pdp-buy__tab">
        <summary>Care &amp; how to wear</summary>
        <div class="pdp-buy__tab-body">
          <p><b>How to put on:</b> pull from the top of the foot — not the straps — to help extend their lifespan.</p>
          <p><b>Cleaning:</b> warm soapy water, rinse well, air dry. No machine washing. Avoid direct sunlight for more than an hour.</p>
        </div>
      </details>
      <details class="pdp-buy__tab">
        <summary>Shipping</summary>
        <div class="pdp-buy__tab-body">
          <p>Free shipping on orders over $75. Standard delivery 3–5 business days. Express delivery 1–2 business days at checkout.</p>
        </div>
      </details>
      <details class="pdp-buy__tab">
        <summary>30-day returns + 90-day warranty</summary>
        <div class="pdp-buy__tab-body">
          <p>Try them in studio for 30 days. If they don't perform, return for a full refund. 90-day warranty covers grip-surface wear under normal use.</p>
        </div>
      </details>
    </div>
  </div>
</section>


<!-- ============================== PILLAR STRIP ============================== -->
<section class="pdp-pillars" aria-label="Why it works">
  <div class="pdp-pillars__inner">
    <span class="pdp-pillars__label">Why it works</span>
    <div class="pdp-pillars__pts">
      <span>360° Grip</span><span class="pdp-pillars__div"></span>
      <span>Stay Secure</span><span class="pdp-pillars__div"></span>
      <span>No Sock Fuss</span><span class="pdp-pillars__div"></span>
      <span>Rinse &amp; Reuse</span><span class="pdp-pillars__div"></span>
      <span>No Latex / No Silicone</span>
    </div>
  </div>
</section>


<!-- ============================== VALUE / PREMIUM ============================== -->
<section class="pdp-value">
  <div class="pdp-value__inner">
    <div class="pdp-value__copy">
      <p class="pdp-eyebrow">The premium math</p>
      <h2 class="pdp-h2">Cheaper than the socks you keep replacing.</h2>
      <p class="pdp-lede">Grip socks don’t enhance your workout — they just exist. They slip, slide, and demand mid-class adjustments. The silicone dots wear off in weeks, the fabric absorbs sweat and bacteria, and you replace them six to eight times a year. Barreletics is the pair you buy once — secure, safe, and built for actual movement.</p>
      <p style="font-size: 11px; letter-spacing: 0.06em; color: rgba(255,255,255,0.45); margin-top: 18px;">Sock-cost figures are illustrative based on common DTC grip-sock pricing &amp; lifespan ranges — verify against your own brand research before publishing.</p>
    </div>
    <div class="pdp-value__compare">
      <div class="pdp-value__col">
        <span class="pdp-value__tag">Traditional grip socks</span>
        <p class="pdp-value__amount">$112 <span class="pdp-value__amount-unit">/ year</span></p>
        <ul class="pdp-value__list">
          <li>8 pairs at ~$14 each</li>
          <li>Silicone dots wear off in 6–8 weeks</li>
          <li>Sweat-absorbing fabric, bacterial buildup</li>
          <li>Inconsistent grip when wet</li>
          <li>Replaced every 6–8 weeks on average</li>
        </ul>
      </div>
      <div class="pdp-value__col pdp-value__col--ours">
        <span class="pdp-value__tag">Barreletics performance skin</span>
        <p class="pdp-value__amount">$74 <span class="pdp-value__amount-unit">/ 18+ months</span></p>
        <ul class="pdp-value__list">
          <li>One pair · rinse and reuse</li>
          <li>Full-contact 360° grip surface</li>
          <li>Skin-safe materials · no latex · no silicone</li>
          <li>Consistent grip in sweat-on conditions</li>
          <li>Built to outlast the socks five times over</li>
        </ul>
      </div>
    </div>
  </div>
</section>


<!-- ============================== BENEFIT GRID ============================== -->
<section class="pdp-section">
  <p class="pdp-eyebrow">Built for the studio floor</p>
  <h2 class="pdp-h2">Why this is the upgrade.</h2>
  <p class="pdp-lede">Designed around the customer value stack: <b>safety</b> first, then <b>grip</b>, then everything that makes day-after-day ownership easier.</p>

  <div class="pdp-benefits">
    <article class="pdp-benefit">
      <span class="pdp-benefit__num">01 · Safety</span>
      <h3 class="pdp-benefit__title">Reduced slip risk on reformer + Megaformer</h3>
      <p class="pdp-benefit__sub">Confidence through transitions, holds, and full-contact movement. The biggest conversion driver — your feet stay where you put them.</p>
    </article>
    <article class="pdp-benefit">
      <span class="pdp-benefit__num">02 · Grip</span>
      <h3 class="pdp-benefit__title">360° full-contact traction</h3>
      <p class="pdp-benefit__sub">Not patches, not gel dots. The entire underfoot grips, every direction, every class.</p>
    </article>
    <article class="pdp-benefit">
      <span class="pdp-benefit__num">03 · Upgrade</span>
      <h3 class="pdp-benefit__title">Replaces grip socks for good</h3>
      <p class="pdp-benefit__sub">A premium alternative — built to outperform the disposables you keep buying.</p>
    </article>
    <article class="pdp-benefit">
      <span class="pdp-benefit__num">04 · Clean</span>
      <h3 class="pdp-benefit__title">Rinse, dry, reuse</h3>
      <p class="pdp-benefit__sub">Warm soapy water resets them between classes. Cleaner than a sock that lives in your bag.</p>
    </article>
    <article class="pdp-benefit">
      <span class="pdp-benefit__num">05 · Barefoot</span>
      <h3 class="pdp-benefit__title">Barefoot-inspired feel</h3>
      <p class="pdp-benefit__sub">Engineered for natural toe articulation. Freedom to move — without the slip.</p>
    </article>
    <article class="pdp-benefit">
      <span class="pdp-benefit__num">06 · Safe</span>
      <h3 class="pdp-benefit__title">No latex · No silicone · Non-toxic</h3>
      <p class="pdp-benefit__sub">Skin-safe materials for sensitive skin and wellness-aware practice.</p>
    </article>
  </div>
</section>


<!-- ============================== MEDIA SPLIT — STORY ============================== -->
<section class="pdp-split">
  <div class="pdp-split__media" style="background: none;"><img src="https://barreletics.com/cdn/shop/files/IMG_2704.jpg?v=1710103438&width=1600" alt="Performance Skin technology" style="width: 100%; height: 100%; object-fit: cover; display: block;" /></div>
  <div class="pdp-split__copy">
    <p class="pdp-eyebrow">Engineered, not accidental</p>
    <h2 class="pdp-h2">Grip that performs when you heat up.</h2>
    <p class="pdp-lede">The performance skin holds its grip in the conditions that break ordinary studio socks — sweat, transitions, full-contact holds. Built from a proprietary skin-safe compound with no latex and no silicone.</p>
    <ul class="pdp-split__list">
      <li>Tested on Megaformer + reformer carriages — same grip wet or dry</li>
      <li>Anti-microbial surface · no sweat-absorbing fabric to harbor bacteria</li>
      <li>Engineered to keep its texture for 18+ months of regular use</li>
    </ul>
  </div>
</section>


<!-- ============================== TESTIMONIAL ============================== -->
<section class="pdp-section pdp-section--alt pdp-section--tight">
  <div class="pdp-quote">
    <div class="pdp-quote__stars">★★★★★</div>
    <p class="pdp-quote__body">&ldquo;My love-hate relationship with the sock has finally come to a ceremonial end. The vast improvement during the first minute of barre class is beyond words.&rdquo;</p>
    <p class="pdp-quote__attr"><b>Mia Evans</b> Verified buyer · Studio Performance Skin · 2 weeks ago</p>
  </div>
</section>




<!-- ============================== LIFESTYLE MEDIA SPLIT ============================== -->
<section class="pg-hero-split" style="border-top: 1px solid var(--br-line); border-bottom: 1px solid var(--br-line);">
  <div class="pg-hero-split__media" style="background: none; padding: 0;"><img src="https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg?v=1710549452&width=1600" alt="In the studio" style="width: 100%; height: 100%; object-fit: cover; display: block;" /></div>
  <div class="pg-hero-split__copy">
    <p class="pg-hero-split__eyebrow">Built for movement</p>
    <h2 class="pg-hero-split__title" style="font-size: clamp(30px, 3.6vw, 48px);">Worn through every transition.</h2>
    <p class="pg-hero-split__body">Studio Performance Skins move how you move — barre holds, reformer transitions, full-contact Pilates moments. The first studio shoe practitioners want to wear all class.</p>
    <p style="font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--br-accent); font-weight: 700; margin: 20px 0 0;">Trusted by 1000's of Instructors</p>
  </div>
</section>

<!-- ============================== VARIANT GRID — SHOP ALL COLORS & SIZES ============================== -->
<section class="pdp-section" id="variants">
  <header class="pdp-variants__head">
    <div class="pdp-variants__head-meta">
      <p class="pdp-eyebrow" style="margin: 0;">Same grip · two builds · all colors</p>
      <h2 class="pdp-h2">Shop all colors &amp; sizes.</h2>
    </div>
    <a href="#" class="pdp-variants__head-link">Open vs closed → compare</a>
  </header>

  <div class="pdp-variants__tabs" role="tablist">
    <button class="pdp-variant-tab" aria-selected="true">Closed sole</button>
    <button class="pdp-variant-tab">Open sole</button>
  </div>

  <div class="pdp-variants__grid">
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/products/Outside_Black-600x600_f1b31d95-ec45-4761-801c-9885e9572232.jpg?v=1776454640&width=800" alt="Closed Sole Onyx" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Closed Sole · Onyx</h3>
      <span class="pdp-vcard__meta">Verified buyer · M / L</span>
      <span class="pdp-vcard__price">$74</span>
      <a href="#" class="pdp-vcard__addlink">Add to cart →</a>
    </article>
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/files/Dusty_Rose_5e602111-f285-4b53-98b2-b3cdc3ff25a2.png?v=1773521063&width=800" alt="Closed Sole Blush" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Closed Sole · Blush</h3>
      <span class="pdp-vcard__meta">Verified buyer · M / L</span>
      <span class="pdp-vcard__price">$74</span>
      <a href="#" class="pdp-vcard__addlink">Add to cart →</a>
    </article>
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/files/A14_TopBottom_LightGrey-1000x1000_d30b6fcb-229e-4af9-8062-e1c4901df31e.jpg?v=1773920303&width=800" alt="Closed Sole Stone" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Closed Sole · Stone</h3>
      <span class="pdp-vcard__meta">Verified buyer · M / L</span>
      <span class="pdp-vcard__price">$74</span>
      <a href="#" class="pdp-vcard__addlink">Add to cart →</a>
    </article>
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/files/Copreni_Final_More_grey.png?v=1774119812&width=1600" alt="Coperni" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><span class="pdp-vcard__le">Limited Edition</span><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Coperni × Closed</h3>
      <span class="pdp-vcard__meta">Limited drop · 1 run</span>
      <span class="pdp-vcard__price">$115</span>
      <a href="#" class="pdp-vcard__addlink">Add to cart →</a>
    </article>
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/files/Deep_Teal.png?v=1773521063&width=800" alt="Closed Sole Sage" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Closed Sole · Sage</h3>
      <span class="pdp-vcard__meta">Verified buyer · M / L</span>
      <span class="pdp-vcard__price">$74</span>
      <a href="#" class="pdp-vcard__addlink">Add to cart →</a>
    </article>
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/products/Performance-Skin-Footwear-White_a7103efd-c227-477c-84f8-41352ac1053e.jpg?v=1776396965&width=800" alt="Closed Sole Ivory" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Closed Sole · Ivory</h3>
      <span class="pdp-vcard__meta">M only</span>
      <span class="pdp-vcard__price"><span class="pdp-vcard__sale"><s>$74</s> $48</span></span>
    </article>
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/files/A14_TopBottom_Yellow-600x600.jpg?v=1776454640&width=800" alt="Closed Sole Sand" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Closed Sole · Sand</h3>
      <span class="pdp-vcard__meta">Verified buyer · M / L</span>
      <span class="pdp-vcard__price">$74</span>
      <a href="#" class="pdp-vcard__addlink">Add to cart →</a>
    </article>
    <article class="pdp-vcard">
      <div class="pdp-vcard__media" style="background: #f5f5f5;"><img src="https://barreletics.com/cdn/shop/files/Purple_45b2348c-f5a1-45a8-a704-88f8afd10414.jpg?v=1776454640&width=800" alt="Closed Sole Plum" style="width: 100%; height: 100%; object-fit: cover; display: block;" /><div class="pdp-vcard__quick">Quick view</div></div><h3 class="pdp-vcard__title">Closed Sole · Plum</h3>
      <span class="pdp-vcard__meta">Verified buyer · M / L</span>
      <span class="pdp-vcard__price">$74</span>
      <a href="#" class="pdp-vcard__addlink">Add to cart →</a>
    </article>
  </div>

  <div style="text-align: center; margin-top: 48px; padding-top: 32px; border-top: 1px solid var(--br-line);">
    <a href="Barreletics Collection.html" class="pdp-variants__head-link" style="font-size: 14px; border-bottom-width: 2px; padding-bottom: 4px;">See all 12 colors &amp; styles  →</a>
    <p style="font-size: 12px; color: var(--br-text-mute); letter-spacing: 0.06em; margin: 14px 0 0;">Closed Sole · Open Sole · M / L sizing</p>
  </div>
</section>


<!-- ============================== JUDGE.ME REVIEWS ============================== -->
<section class="pdp-section pdp-section--alt" id="reviews">
  <header class="pdp-reviews__head">
    <div>
      <p class="pdp-eyebrow">Reviews · this product</p>
      <h2 class="pdp-h2" style="font-size: clamp(24px, 2.4vw, 32px); margin-top: 8px;">Reviews</h2>
      <p class="pdp-reviews__head-summary">Real reviews from real customers</p>
    </div>
    <div class="pdp-reviews__head-bigstars">★★★★★</div>
  </header>

  <div class="pdp-reviews__grid">
    <article class="pdp-review">
      <div class="pdp-review__head">
        <span class="pdp-review__stars">★★★★★</span>
        <span class="pdp-review__verified">Verified buyer</span>
      </div>
      <h3 class="pdp-review__title">Game-changer for reformer</h3>
      <p class="pdp-review__body">I used to slide on every transition. With these I just don't. Two months in, grip is still exactly the same as day one. Tried the rinse and they're spotless.</p>
      <p class="pdp-review__attr"><b>Jamie L.</b> · Onyx · 2 weeks ago</p>
    </article>

    <article class="pdp-review">
      <div class="pdp-review__head">
        <span class="pdp-review__stars">★★★★★</span>
        <span class="pdp-review__verified">Verified buyer</span>
      </div>
      <h3 class="pdp-review__title">Tried 3 grip sock brands first</h3>
      <p class="pdp-review__body">Don't bother with anything else. The math alone makes the price obvious — I went through a sock pair every 6 weeks. These are the same on day 120.</p>
      <p class="pdp-review__attr"><b>Casey M.</b> · Stone · 1 month ago</p>
    </article>

    <article class="pdp-review">
      <div class="pdp-review__head">
        <span class="pdp-review__stars">★★★★★</span>
        <span class="pdp-review__verified">Verified buyer</span>
      </div>
      <h3 class="pdp-review__title">Studio recommends them</h3>
      <p class="pdp-review__body">I run a barre studio and we now stock them for new students. They actually grip the carriage instead of sliding. Worth every penny.</p>
      <p class="pdp-review__attr"><b>Priya R.</b> · Onyx · 3 weeks ago</p>
    </article>

    <article class="pdp-review">
      <div class="pdp-review__head">
        <span class="pdp-review__stars">★★★★☆</span>
        <span class="pdp-review__verified">Verified buyer</span>
      </div>
      <h3 class="pdp-review__title">Took 2 classes to break in</h3>
      <p class="pdp-review__body">First class I wasn't sure. By class 3, perfect — fit my foot better than a sock and the grip on Megaformer is legitimate. Just be patient.</p>
      <p class="pdp-review__attr"><b>Diane K.</b> · Blush · 6 weeks ago</p>
    </article>

    <article class="pdp-review">
      <div class="pdp-review__head">
        <span class="pdp-review__stars">★★★★★</span>
        <span class="pdp-review__verified">Verified buyer</span>
      </div>
      <h3 class="pdp-review__title">My do-everything studio shoe</h3>
      <p class="pdp-review__body">Barre, Pilates, reformer, even a hot yoga class once. Same grip across all of them. Rinses clean in two minutes.</p>
      <p class="pdp-review__attr"><b>Dana W.</b> · Sage · 2 months ago</p>
    </article>

    <article class="pdp-review">
      <div class="pdp-review__head">
        <span class="pdp-review__stars">★★★★★</span>
        <span class="pdp-review__verified">Verified buyer</span>
      </div>
      <h3 class="pdp-review__title">Skin-safe for once</h3>
      <p class="pdp-review__body">I'm sensitive to silicone-dot socks — got rashes for a year before switching. These don't cause any reaction. Finally found my pair.</p>
      <p class="pdp-review__attr"><b>Helen T.</b> · Ivory · 4 months ago</p>
    </article>
  </div>

  <div class="pdp-reviews__foot">
    <a href="#" class="pdp-reviews__more">Read all reviews →</a>
    <a href="#" class="pdp-reviews__write">Write a review</a>
  </div>
</section>


<!-- ============================== FAQ ============================== -->
<section class="pdp-section pdp-faq" id="faq">
  <p class="pdp-eyebrow">Frequently asked</p>
  <h2 class="pdp-h2">Before you order.</h2>
  <p class="pdp-lede">Most of the questions we get from first-time buyers. If yours isn&rsquo;t here, <a href="#" style="border-bottom: 1px solid currentColor; color: var(--br-text); text-decoration: none;">read all FAQs</a> or message us — we reply within a few hours.</p>

  <div class="pdp-faq__list">
    <details class="pdp-faq__item" open>
      <summary>My studio doesn&rsquo;t allow exposed toes — can I still wear these?</summary>
      <div class="pdp-faq__body">
        <p>Yes. The Closed Sole option covers the toes completely and works in any studio that requires covered feet. If you specifically need the Open Sole feel but your studio prefers fabric coverage, slip a thin grip sock <em>under</em> the open-sole skin — you get the barefoot-inspired articulation of Barreletics plus the coverage your studio asks for.</p>
        <p>Worth noting: Joseph Pilates designed the practice to be done barefoot, and yoga has always been a barefoot tradition. The "covered toes" rule is a studio convention, not a movement requirement. The Closed Sole is built to honor both — barefoot-like grip and full coverage.</p>
      </div>
    </details>

    <details class="pdp-faq__item">
      <summary>Are these really cheaper than grip socks long-term?</summary>
      <div class="pdp-faq__body">
        <p>Yes, and by a wide margin. The average reformer/barre practitioner replaces grip socks every 6–8 weeks — silicone dots wear off, fabric thins out, and the sweat-absorbed bacteria make most pairs unwearable in under three months. At $14–$18 a pair, that&rsquo;s $112–$144 a year, minimum.</p>
        <p>A pair of Barreletics performance skins runs $74–$74 and is built to outlast 8 sock replacements. Rinse them between classes, air-dry, and they stay grippy. See the comparison above for the full math.</p>
      </div>
    </details>

    <details class="pdp-faq__item">
      <summary>What about bacteria — aren&rsquo;t open-sole shoes less hygienic?</summary>
      <div class="pdp-faq__body">
        <p>Actually, the reverse. Grip socks absorb sweat into the fabric, sit in your studio bag damp, and harbor bacteria for the weeks you keep wearing them. Performance skins are a single-material surface — sweat runs off, and a 60-second rinse with warm soapy water resets them between classes.</p>
        <p>The materials are skin-safe and non-toxic — no latex, no silicone. They&rsquo;re also more hygienic than going actually barefoot on shared studio equipment.</p>
      </div>
    </details>

    <details class="pdp-faq__item">
      <summary>How do I know my size?</summary>
      <div class="pdp-faq__body">
        <p>Performance skins fit very close to your true street-shoe size. If you&rsquo;re between sizes, go down — the material has slight stretch in the toe box. Our <a href="#">size chart</a> lists measured length, width, and the corresponding street-shoe size.</p>
      </div>
    </details>

    <details class="pdp-faq__item">
      <summary>How long do they last?</summary>
      <div class="pdp-faq__body">
        <p>Built to last hundreds of classes — actual lifespan varies by use, care, and frequency. The 90-day warranty covers premature grip-surface wear; the 30-day return covers fit and feel.</p>
      </div>
    </details>

    <details class="pdp-faq__item">
      <summary>What&rsquo;s the difference between Closed Sole and Open Sole?</summary>
      <div class="pdp-faq__body">
        <p><b>Closed Sole:</b> the upper covers your whole foot. Best for barre, reformer, and Megaformer — and required by some studios.</p>
        <p><b>Open Sole:</b> the upper leaves the toes exposed for maximum barefoot feel. Best for yoga, mat Pilates, and floor work where toe articulation matters.</p>
        <p>Same grip system on the underside. <a href="#">See the side-by-side comparison →</a></p>
      </div>
    </details>
  </div>
</section>


<!-- ============================== PRODUCT RAIL ============================== -->
<section class="pdp-section">
  <header class="pdp-rail__head">
    <div>
      <p class="pdp-eyebrow">Build the kit</p>
      <h2 class="pdp-h2">Pairs with your studio kit.</h2>
    </div>
    <a href="#" class="pdp-variants__head-link">Shop the kit →</a>
  </header>

  <div class="pdp-rail__list">
    <article class="pdp-rail-card">
      <div class="pdp-rail-card__media" style="background: none;"><img src="https://barreletics.com/cdn/shop/products/Performance-Skin-Footwear-White_a7103efd-c227-477c-84f8-41352ac1053e.jpg?v=1776396965&width=800" alt="Open Sole" style="width: 100%; height: 100%; object-fit: cover; display: block;" /></div>
      <h3 class="pdp-rail-card__title">Open Sole · Stone</h3>
      <p class="pdp-rail-card__price">$74</p>
    </article>
    <article class="pdp-rail-card">
      <div class="pdp-rail-card__media" style="background: none;"><img src="https://barreletics.com/cdn/shop/products/Studio_TopBottom_Pink-1000x1000.jpg?v=1776396965&width=800" alt="Open Sole Coral" style="width: 100%; height: 100%; object-fit: cover; display: block;" /></div>
      <h3 class="pdp-rail-card__title">Open Sole · Blush</h3>
      <p class="pdp-rail-card__price">$74</p>
    </article>
    <article class="pdp-rail-card">
      <div class="pdp-rail-card__media" style="background: none;"><img src="https://barreletics.com/cdn/shop/files/Screenshot_2026-05-23_at_12.15.49_PM.png?v=1779553195&width=1200" alt="Apparel" style="width: 100%; height: 100%; object-fit: cover; display: block;" /></div>
      <h3 class="pdp-rail-card__title">High-Rise Yoga Pant</h3>
      <p class="pdp-rail-card__price">$98</p>
    </article>
    <article class="pdp-rail-card">
      <div class="pdp-rail-card__media pdp-rail-card__media--dark"></div>
      <h3 class="pdp-rail-card__title">Studio Bundle · save 15%</h3>
      <p class="pdp-rail-card__price">$116</p>
    </article>
  </div>
</section>


<!-- ============================== FOOTER ============================== -->
<footer class="pdp-footer">
  <div class="pdp-footer__grid">
    <div class="pdp-footer__col pdp-footer__brand">
      <a href="Barreletics Home.html" class="pdp-header__logo" aria-label="Barreletics — home"><img src="barreletics-logo.png" alt="Barreletics" /></a>
      <p>The premium performance alternative to traditional grip socks. Superior grip, greater stability, safer movement.</p>
      <form class="pdp-footer__newsletter" aria-label="Newsletter signup">
        <input type="email" placeholder="Email · 10% off · quarterly drops only" aria-label="Email address" />
        <button type="submit">Get 10% off</button>
      </form>
    </div>
    <div class="pdp-footer__col">
      <h6>Shop</h6>
      <ul>
        <li><a href="#">Studio collection</a></li>
        <li><a href="#">Outdoor</a></li>
        <li><a href="#">Bundles</a></li>
        <li><a href="#">One-of-a-kind</a></li>
        <li><a href="#">Gift cards</a></li>
      </ul>
    </div>
    <div class="pdp-footer__col">
      <h6>Support</h6>
      <ul>
        <li><a href="#">Size chart</a></li>
        <li><a href="#">Care guide</a></li>
        <li><a href="#">Shipping &amp; returns</a></li>
        <li><a href="#">FAQ</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </div>
    <div class="pdp-footer__col">
      <h6>Stories</h6>
      <ul>
        <li><a href="#">Journal</a></li>
        <li><a href="#">Coperni × Barreletics</a></li>
        <li><a href="#">Brand story</a></li>
        <li><a href="#">Affiliates</a></li>
      </ul>
    </div>
    <div class="pdp-footer__col">
      <h6>Follow</h6>
      <ul>
        <li><a href="#">Instagram</a></li>
        <li><a href="#">TikTok</a></li>
        <li><a href="#">YouTube</a></li>
        <li><a href="#">Pinterest</a></li>
      </ul>
    </div>
  </div>
  <div class="pdp-footer__bottom">
    <span>© 2026 Barreletics. All rights reserved.</span>
    <span><a href="#" style="color: inherit; text-decoration: none;">Privacy</a> · <a href="#" style="color: inherit; text-decoration: none;">Terms</a> · <a href="#" style="color: inherit; text-decoration: none;">Accessibility</a></span>
  </div>
</footer>

<div id="pdp-tweaks-root"></div>
<script src="https://unpkg.com/react@18.3.1/umd/react.development.js" integrity="sha384-hD6/rw4ppMLGNu3tX5cjIb+uRZ7UkRJ6BPkLpg4hAu/6onKUg4lLsHAs9EBPT82L" crossorigin="anonymous"></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js" integrity="sha384-u6aeetuaXnQ38mYT8rp6sbXaQe3NL9t+IBXmnYxwkUI2Hw4bsp2Wvmx4yRQF1uAm" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" integrity="sha384-m08KidiNqLdpJqLq95G/LEi8Qvjl/xUYll3QILypMoQ65QorJ9Lvtp2RXYGBFj1y" crossorigin="anonymous"></script>
<script type="text/babel" src="tweaks-panel.jsx"></script>
<script type="text/babel" src="pdp-tweaks.jsx"></script>
<script src="ticker.js" defer></script>
</body>
</html>
