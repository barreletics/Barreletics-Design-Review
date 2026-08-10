# 08 — Theme Settings Reference

Settings are defined in `config/settings_schema.json` and current values stored in `config/settings_data.json`.

---

## Colors

| Setting ID | Type | Label | Default | Consumed By |
|------------|------|-------|---------|-------------|
| `color_charcoal` | `color` | Charcoal (primary text) | `#1c1916` | `assets/design-tokens.css` (maps to `--color-charcoal`) |
| `color_body_text` | `color` | Body text | `#4a4a4a` | `assets/design-tokens.css` (`--color-body`) |
| `color_muted` | `color` | Muted text | `#8a8a8a` | `assets/design-tokens.css` (`--color-muted`) |
| `color_white` | `color` | White | `#ffffff` | `assets/design-tokens.css` (`--color-white`) |
| `color_warm_cream` | `color` | Warm cream (alternate bg) | `#f5f2ec` | `assets/design-tokens.css` (`--color-warm-cream`) |
| `color_coral` | `color` | Coral (accent) | `#e8927c` | `assets/design-tokens.css` (`--color-coral`), cart badge |
| `color_rust` | `color` | Rust (CTA/accent) | `#c45c3f` | `assets/design-tokens.css` (`--color-rust`) |
| `color_gold` | `color` | Gold (star ratings) | `#d4af37` | `assets/design-tokens.css` (`--color-gold`) |
| `color_border` | `color` | Default border | `#e5e0d8` | `assets/design-tokens.css` |
| `color_warm_border` | `color` | Warm border (header scroll) | `#d6cfc0` | `assets/design-tokens.css` (`--color-warm-border`) |

---

## Typography

| Setting ID | Type | Label | Default | Range | Consumed By |
|------------|------|-------|---------|-------|-------------|
| `type_font_family` | `font_picker` | Primary font | `roboto_n4` | — | `layout/theme.liquid` (font loading), `assets/design-tokens.css` |
| `type_base_size` | `range` | Base font size | 16 | 14–20 px, step 1 | `assets/design-tokens.css` (`--text-base`) |
| `type_heading_scale` | `range` | Heading scale factor | 100 | 100–150 %, step 5 | `assets/design-tokens.css` (heading sizes) |

---

## Layout

| Setting ID | Type | Label | Default | Range | Consumed By |
|------------|------|-------|---------|-------|-------------|
| `max_width` | `range` | Max content width | 1200 | 1000–1600 px, step 40 | `assets/design-tokens.css` (`--max-width`) |
| `section_padding_x` | `range` | Section horizontal padding | 24 | 16–64 px, step 4 | `assets/design-tokens.css` (`--section-padding-x`) |

---

## Announcement Bar

| Setting ID | Type | Label | Default | Range | Consumed By |
|------------|------|-------|---------|-------|-------------|
| `announcement_enabled` | `checkbox` | Show announcement bar | `true` | — | `snippets/announcement-strip.liquid` |
| `announcement_message_1` | `text` | Message 1 | "Buy 2, Save 15% — Code SAVE15" | — | `snippets/announcement-strip.liquid` |
| `announcement_message_2` | `text` | Message 2 | "Free Shipping Over $150" | — | `snippets/announcement-strip.liquid` |
| `announcement_message_3` | `text` | Message 3 | "30-Day Returns · Made in USA" | — | `snippets/announcement-strip.liquid` |
| `announcement_rotation_speed` | `range` | Rotation speed | 4 | 2–8 s, step 1 | `snippets/announcement-strip.liquid` |

> **Note:** The announcement strip in this codebase uses section blocks (not these settings) for its slides. These settings exist in the schema for potential future use or a simpler non-block-based configuration.

---

## Cart

| Setting ID | Type | Label | Default | Options | Consumed By |
|------------|------|-------|---------|---------|-------------|
| `cart_type` | `select` | Cart type | `"drawer"` | `drawer` (Drawer — recommended), `page` (Full page) | `snippets/cart-drawer.liquid`, `assets/cart.js` |
| `cart_show_free_shipping_bar` | `checkbox` | Show free shipping progress bar | `true` | — | `snippets/cart-drawer.liquid` |
| `cart_free_shipping_threshold` | `text` | Free shipping threshold | `"150"` | — | `snippets/cart-drawer.liquid` (display text) |

> **Note:** `cart.js` hardcodes `FREE_SHIPPING_THRESHOLD = 15000` (cents). The `cart_free_shipping_threshold` setting controls the display text in the drawer's shipping bar (`${{ settings.free_shipping_threshold | default: 150 }}`). Keep these values synchronized.

---

## Social Media

| Setting ID | Type | Label | Default | Consumed By |
|------------|------|-------|---------|-------------|
| `social_instagram` | `text` | Instagram URL | `https://instagram.com/barreletics` | `snippets/footer.liquid` |
| `social_tiktok` | `text` | TikTok URL | `https://tiktok.com/@barreletics` | `snippets/footer.liquid` |
| `social_facebook` | `text` | Facebook URL | `https://facebook.com/barreletics` | `snippets/footer.liquid` |
| `social_pinterest` | `text` | Pinterest URL | `https://pinterest.com/Barreletics` | `snippets/footer.liquid` |
| `social_youtube` | `text` | YouTube URL | `""` (empty) | `snippets/footer.liquid` |

> **Note:** The footer currently hardcodes its social links rather than reading these settings. These settings are defined in the schema for future dynamic rendering.

---

## Favicon & Branding

| Setting ID | Type | Label | Default | Info | Consumed By |
|------------|------|-------|---------|------|-------------|
| `favicon` | `image_picker` | Favicon | — | — | `layout/theme.liquid` (`{{ content_for_header }}` auto-injects) |
| `og_default_image` | `image_picker` | Default Open Graph image | — | Recommended 1200×630px | `layout/theme.liquid` (fallback OG image) |

---

## Tracking & Integrations

All tracking settings follow **D-045**: Shopify native channel integrations preferred; theme-level tracking is a fallback. Each setting's `info` text warns against using both simultaneously.

### Analytics

| Setting ID | Type | Label | Default | Consumed By |
|------------|------|-------|---------|-------------|
| `ga4_measurement_id` | `text` | GA4 Measurement ID | `""` | `snippets/analytics-head.liquid` (gtag.js config), `snippets/analytics-events.liquid` (ecommerce events) |
| `meta_pixel_id` | `text` | Meta Pixel ID | `""` | `snippets/meta-pixel.liquid` (fbevents.js init, PageView, ViewContent, AddToCart, InitiateCheckout) |
| `pinterest_tag_id` | `text` | Pinterest Tag ID | `""` | `snippets/pinterest-tag.liquid` (pintrk init, pagevisit, viewcategory, addtocart, checkout) |
| `clarity_project_id` | `text` | Microsoft Clarity Project ID | `""` | `snippets/clarity.liquid` (session recording tag) |

### Customer Support

| Setting ID | Type | Label | Default | Consumed By |
|------------|------|-------|---------|-------------|
| `helpscout_beacon_id` | `text` | Help Scout Beacon ID | `""` | `snippets/helpscout-beacon.liquid` (Beacon widget init + customer identify) |
| `tidio_widget_key` | `text` | Tidio Widget Key | `""` | `snippets/tidio-widget.liquid` (chat widget script + customer properties) |

### Search & Verification

| Setting ID | Type | Label | Default | Consumed By |
|------------|------|-------|---------|-------------|
| `search_console_verification` | `text` | Google Search Console Verification | `""` | `layout/theme.liquid` (`<meta name="google-site-verification">`) |

---

## Free Shipping

| Setting ID | Type | Label | Default | Range | Consumed By |
|------------|------|-------|---------|-------|-------------|
| `free_shipping_threshold` | `range` | Free shipping threshold ($) | 150 | $50–$300, step $10 | `snippets/cart-drawer.liquid` (shipping bar display text) |
| `free_shipping_message` | `text` | Free shipping message | "Free shipping on orders over $150" | — | `snippets/cart-drawer.liquid` |

> **Note:** There are two threshold settings: `cart_free_shipping_threshold` (text, in Cart group) and `free_shipping_threshold` (range, in Free shipping group). The cart drawer references `settings.free_shipping_threshold` for its display. `cart.js` hardcodes `15000` cents. Ensure all three values agree when changing the threshold.

---

## Settings Loading in `layout/theme.liquid`

```
<head>
  └─ settings.search_console_verification  → <meta> tag
  └─ analytics-head.liquid                 → settings.ga4_measurement_id
  └─ meta-pixel.liquid                     → settings.meta_pixel_id
  └─ pinterest-tag.liquid                  → settings.pinterest_tag_id
  └─ clarity.liquid                        → settings.clarity_project_id
</head>
<body>
  └─ announcement-strip.liquid             → section block settings (messages)
  └─ cart-drawer.liquid                     → settings.free_shipping_threshold
  └─ analytics-events.liquid               → settings.ga4_measurement_id
  └─ helpscout-beacon.liquid               → settings.helpscout_beacon_id
  └─ tidio-widget.liquid                   → settings.tidio_widget_key
</body>
```

---

## One-off colors (2026-08-10)

| Setting ID | Type | Label | Default | Consumed By |
|------------|------|-------|---------|-------------|
| `one_off_product` | `product` | One-off product | — | `snippets/one-off-nav-item.liquid`, `snippets/one-off-quiet-link.liquid`, `sections/variant-grid.liquid` (wins over section picker) |
| `one_off_nav_label` | `text` | Nav label | `One-off colors` | Header inject under parent match |
| `one_off_parent_match` | `text` | Parent menu match | `grippy` | Header subnav parent title contains |
| `one_off_link_label` | `text` | PDP quiet link | `This week’s one-off color →` | Under ATC on Closed/Open/Outdoor; hidden on one-off PDP |

**Behavior:** Product set → show nav + quiet link + One-Offs tab. Picker empty → hide all. Do not also add this link in Online Store → Navigation. OS: **P-011** / **D-051** · `planning/one-off-surfaces.md`.

---

## Cross-References

- Design token CSS custom properties sourced from these settings → [07-css-architecture.md](07-css-architecture.md)
- Analytics event implementation details → [06-javascript-architecture.md](06-javascript-architecture.md)
- D-045 tracking strategy (Shopify native preferred) → decision log
- One-off gate → P-011 / D-051
