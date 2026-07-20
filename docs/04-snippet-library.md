# 04 — Snippet Library

Every snippet lives in `shopify-build/snippets/` and is included via `{% render 'snippet-name' %}`.

---

## Layout

### `header-nav.liquid`

Fixed site header with logo, desktop dropdown navigation, utility actions (Help, Account, Cart), and mobile slide-in drawer.

**Included in:** `layout/theme.liquid` (global)

**Structure:**
- Desktop: logo center-left, nav links (Grippy Shoes, Apparel, Collaborations, Journal), actions right
- Grippy Shoes subnav: Shop All, Open Sole, Closed Sole, Outdoor, Compare Styles
- Apparel subnav: Shop All Apparel, Tops, Bottoms
- Mobile: hamburger → left-sliding drawer with accordion sub-menus + utility links (About, FAQ, Contact, Returns)
- Cart icon shows coral badge with `data-cart-count` for AJAX updates
- Scroll behavior: transparent initially, adds `.is-scrolled` (white bg + warm border) after 8px scroll

**Parameters:** None  
**Dependencies:** `design-tokens.css` (z-index, colors), `cart.js` (`window.BarreleticsCart.open()`)  
**JS:** Inline — scroll detection, mobile menu open/close, accordion toggle, Escape key handling.

### `footer.liquid`

4-column grid footer on charcoal background: Shop, Support, Company, Newsletter.

**Included in:** `layout/theme.liquid` (global)

**Structure:**
- Column 1 (Shop): All Grippy Shoes, Open Sole, Closed Sole, Outdoor, Apparel
- Column 2 (Support): FAQ, Shipping, Returns, Warranty, Contact Us
- Column 3 (Company): About Us, Journal, Collaborations, Compare Styles
- Column 4 (Newsletter): email signup form, "No spam. Unsubscribe anytime."
- Bottom bar: social icons (Instagram, TikTok, Facebook) + copyright

**Parameters:** None  
**Dependencies:** `design-tokens.css`, theme settings for social URLs

### `announcement-strip.liquid`

Rotating promotional message bar at page top. Charcoal background, white text, 320ms opacity crossfade, 4-second rotation interval. Pauses on hover. Respects `prefers-reduced-motion`.

**Included in:** `layout/theme.liquid` (global — rendered as a section with blocks)

**Settings/Blocks:** Configured via section blocks in theme customizer — each block has `text` (text) and `link_url` (url).  
**Parameters:** None  
**JS:** Inline — `setInterval` rotation, mouseenter/mouseleave pause.

### `section-wrapper.liquid`

Documentation-only snippet. Does not render any HTML.

Documents the standard section wrapper CSS pattern used across all sections:

| CSS Class | Effect |
|---|---|
| `.section` | Default padding (64px / 40px → 48px / 16px mobile) |
| `.section--narrow` | Reduced vertical padding (48px) |
| `.section--flush` | No padding |
| `.section--cream` | `--bg-alternate` background (#f5f2ec) |
| `.section--dark` | `--bg-dark` background, white text |
| `.section__inner` | Max-width 1200px, centered |
| `.section__inner--wide` | Max-width 1400px |
| `.section__inner--narrow` | Max-width 760px |

**Included in:** Referenced by `hero.liquid` and `hero-alt.liquid` (via `{% render %}` calls, though the snippet itself is empty). Sections use the CSS classes directly.

### `breadcrumb.liquid`

Template-aware breadcrumb trail with `BreadcrumbList` JSON-LD. Hidden on homepage. Handles sub-collection nesting (Open Sole, Closed Sole, Outdoor nest under "Grippy Shoes").

**Included in:** Not currently rendered in `theme.liquid` — available for use in templates.

**Supports:** collection, product, article, blog, page, search, cart templates.  
**Parameters:** None  
**Dependencies:** `design-tokens.css`

---

## Product

### `product-card.liquid`

Product card used in grids: image with hover scale (1.02×, 320ms), name, optional subtitle (metafield), price, installment text, optional quick-add form, optional badge (metafield or "Sold Out").

**Included in:** `variant-grid.liquid`, `search-results.liquid`

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `product` | Shopify product | (required) | Product object |
| `show_quick_add` | boolean | true | Show add-to-cart button |
| `show_badge` | boolean | true | Show custom badge or sold-out indicator |
| `show_installments` | boolean | true | Show "4 × $X with Shop Pay" |
| `card_style` | string | "default" | "default" or "minimal" (no border/shadow) |

**Dependencies:** `design-tokens.css`, `barreletics-base.css`

### `review-card.liquid`

Individual review card: star rating, optional title, body, optional photo, author, location, date. Uses Schema.org `Review` microdata.

**Included in:** `social-proof.liquid` (homepage reviews)

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `review` | object | Must have: `rating`, `body`, `author`. Optional: `title`, `location`, `date`, `photo` |

**Dependencies:** `design-tokens.css`

### `sticky-atc.liquid`

Sticky add-to-cart bar fixed to bottom of viewport. Hidden when buy box is in view (via `IntersectionObserver`). Shows product thumbnail, title, price, selected size, and "Add to Cart" button.

**Included in:** `pdp-sticky-atc.liquid` section

**Parameters:** None (reads from `product` Liquid object)  
**Dependencies:** `cart.js` (`window.BarreleticsCart.add()`), listens to `variant:changed` custom event  
**JS:** Inline — IntersectionObserver on `[data-buy-box]`, variant change listener, add-to-cart handler.

---

## UI Components

### `button.liquid`

Renders a styled `<a>` or `<button>` element. No CSS — relies on `.btn` classes from `barreletics-base.css`.

**Included in:** `page-contact.liquid`, `page-size-guide.liquid`, `page-compare.liquid`, `page-technology.liquid`, `page-ambassador.liquid`, `page-wholesale.liquid`, `page-studio-program.liquid`, `page-partners.liquid`, `page-grip-comparison.liquid`

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `label` | string | (required) | Button text |
| `url` | string | — | If set, renders `<a>` instead of `<button>` |
| `style` | string | "primary" | "primary" / "secondary" / "inverted" |
| `size` | string | "md" | "sm" / "md" / "lg" |
| `full` | boolean | false | Full-width button |
| `type` | string | "button" | "button" / "submit" |
| `disabled` | boolean | false | Disabled state |
| `aria_label` | string | — | Accessible label override |
| `class` | string | — | Additional CSS class |

### `faq-accordion.liquid`

Collapsible Q&A pairs with one-at-a-time behavior. Outputs FAQPage JSON-LD by default.

**Included in:** Not directly rendered by sections (sections inline their own accordion patterns). Available as a reusable component.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `items` | array | (required) | Blocks with `.settings.question` and `.settings.answer` |
| `heading` | string | — | Optional section heading |
| `bg_class` | string | "cream" | "cream" or "white" |
| `include_schema` | boolean | true | Output FAQPage JSON-LD |

**CSS:** Inline. Max-width `--max-width-narrow` (760px).  
**JS:** Inline — `toggle` event listener for one-at-a-time behavior + `aria-expanded`.

### `trust-strip.liquid`

Horizontal strip of trust signals: "★★★★★ 1,000+ Reviews · Free Shipping Over $150 · 30-Day Returns · Made in USA". Two variants: default (warm cream bg) and `value` (transparent bg, flex layout).

**Included in:** Available for any section.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `items` | array | — | Custom items (defaults to standard trust signals) |
| `style` | string | "default" | "default" or "value" |

### `related-links.liquid`

Centered row of contextual navigation links with arrow icons.

**Included in:** Available for any section.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `heading` | string | — | Optional heading |
| `links` | array | — | Blocks with `.settings.link_title` and `.settings.link_url` |

---

## Tracking

### `analytics-head.liquid`

GA4 gtag.js loader. Conditional on `settings.ga4_measurement_id`.

**Included in:** `layout/theme.liquid` `<head>`  
**Parameters:** None  
**Configured via:** Theme Settings → Tracking & Integrations → GA4 Measurement ID

### `analytics-events.liquid`

GA4 enhanced ecommerce events. Fires `view_item` (PDP), `view_item_list` (collection), `add_to_cart` (via `cart:item-added` event), `begin_checkout` (checkout button click). Custom events: `size_selector_click`, `sticky_atc_click`, `cart_drawer_open`.

**Included in:** `layout/theme.liquid` (before `</body>`)  
**Parameters:** None  
**Dependencies:** `analytics-head.liquid` (requires `gtag` to be defined)

### `meta-pixel.liquid`

Meta/Facebook Pixel base code + standard events: `PageView` (all pages), `ViewContent` (PDP), `AddToCart` (via `cart:item-added`), `InitiateCheckout` (checkout button). Event deduplication via `eventID` parameter for CAPI compatibility.

**Included in:** `layout/theme.liquid` `<head>`  
**Parameters:** None  
**Configured via:** Theme Settings → Meta Pixel ID

### `pinterest-tag.liquid`

Pinterest Tag base code + events: `pagevisit` (PDP), `viewcategory` (collection), `addtocart`, `checkout`. Enhanced match passes customer email when logged in.

**Included in:** `layout/theme.liquid` `<head>`  
**Parameters:** None  
**Configured via:** Theme Settings → Pinterest Tag ID

### `clarity.liquid`

Microsoft Clarity session recording. Single script tag, no page-specific events.

**Included in:** `layout/theme.liquid` `<head>`  
**Parameters:** None  
**Configured via:** Theme Settings → Clarity Project ID

---

## Support Widgets

### `helpscout-beacon.liquid`

Help Scout Beacon support widget. Auto-identifies logged-in customers (name + email).

**Included in:** `layout/theme.liquid` (before `</body>`)  
**Parameters:** None  
**Configured via:** Theme Settings → Help Scout Beacon ID

### `tidio-widget.liquid`

Tidio AI chat widget. Sets contact properties (ID, email, name) for logged-in customers via `tidioChat-ready` event.

**Included in:** `layout/theme.liquid` (before `</body>`)  
**Parameters:** None  
**Configured via:** Theme Settings → Tidio Widget Key

---

## SEO / Structured Data

### `organization-schema.liquid`

Extended Organization JSON-LD: name, URL, logo (`logo.png` asset), description, `foundingCountry: US`, `sameAs` (Instagram, TikTok, Facebook).

**Included in:** Available for about page (also rendered inline by `theme.liquid` in a simpler form).

### `collection-schema.liquid`

`CollectionPage` JSON-LD: name, description, URL, numberOfItems.

**Included in:** `layout/theme.liquid` (conditional — collection pages only)

### `article-schema.liquid`

`BlogPosting` JSON-LD: headline, dates, author, publisher (Barreletics), description, image, mainEntityOfPage.

**Included in:** `layout/theme.liquid` (conditional — article pages only)

### `geo-section.liquid` (snippet)

Snippet version of the geo-section — accordion content with FAQPage JSON-LD. Same visual and structural pattern as the `geo-section.liquid` section, but accepts `items` and `heading` parameters for programmatic use.

**Included in:** Available for render by any section.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `items` | array | — | Objects with `.question` and `.answer` |
| `heading` | string | "Trusted in studios everywhere" | Section eyebrow |

---

## Cart

### `cart-drawer.liquid`

Slide-in AJAX cart drawer (D-024). Right-aligned panel with overlay, line items, quantity controls, remove buttons, free shipping progress bar, subtotal, View Full Cart link, Checkout CTA.

**Included in:** `layout/theme.liquid` (global)

**Structure:**
- Overlay click → close
- Shipping bar: progress fill based on `FREE_SHIPPING_THRESHOLD` ($150)
- Empty state: "Your cart is empty" + Shop CTA
- Footer: subtotal, view cart link, checkout button
- Focus trap and keyboard handling (Escape, Tab) in `cart.js`

**Parameters:** None  
**Dependencies:** `cart.js` (`window.BarreleticsCart.open()` / `.close()`)  
**JS:** Inline — binds `[data-cart-trigger]` elements to `BarreleticsCart.open()`.
