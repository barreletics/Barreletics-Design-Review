# Product Data Model — Shopify Implementation

**Date:** 2026-07-13  
**Status:** PLANNING  
**Purpose:** Complete product information architecture for Shopify implementation  
**Sources:** docs/09-PRODUCT-KNOWLEDGE.md, docs/08-LIVE-SITE-COPY-AUDIT.md, Shopify catalog (live)

---

## DATA MODEL DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SHOPIFY DATA MODEL                                 │
│                                                                             │
│  ┌─────────────┐         ┌──────────────┐         ┌──────────────┐        │
│  │  PRODUCTS   │────────►│   VARIANTS   │────────►│    MEDIA      │        │
│  │             │         │ (Size×Color) │         │ (per variant) │        │
│  └──────┬──────┘         └──────────────┘         └──────────────┘        │
│         │                                                                   │
│         │ belongs_to                                                        │
│         ▼                                                                   │
│  ┌─────────────┐         ┌──────────────┐         ┌──────────────┐        │
│  │ COLLECTIONS │◄────────│  COLLECTION  │         │    TAGS       │        │
│  │             │         │    RULES     │         │ (filtering)   │        │
│  └─────────────┘         └──────────────┘         └──────────────┘        │
│         │                                                                   │
│         │                 ┌──────────────┐         ┌──────────────┐        │
│         └────────────────►│  METAFIELDS  │         │  CROSS-SELLS │        │
│                           │ (product,    │         │ (product →   │        │
│                           │  variant,    │         │   product)   │        │
│                           │  collection) │         └──────────────┘        │
│                           └──────────────┘                                  │
│                                                                             │
│  ┌─────────────┐         ┌──────────────┐         ┌──────────────┐        │
│  │  JUDGE.ME   │         │     FAQ      │         │   PAGES      │        │
│  │  REVIEWS    │────────►│  (metaobj)   │         │ (collab,     │        │
│  │             │         │              │         │  returns)    │        │
│  └─────────────┘         └──────────────┘         └──────────────┘        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## PRODUCTS

| # | Product Name (Design System) | Shopify Handle | Type | Vendor | Status |
|---|------------------------------|----------------|------|--------|--------|
| 1 | Studio Performance Skin — Closed Sole | `best-reformer-pilates-legree-workout-shoes` | Grippy Footwear | Barreletics | Active |
| 2 | Studio Performance Skin — Open Sole | `studio-performance-skin-footwear` | Grippy Footwear | Barreletics | Active |
| 3 | Aquatic Performance Skins | `aquatic-performance-skins` | Grippy Footwear | Barreletics | Active |
| 4 | Barreletics × Coperni — Closed Sole | `barreletics-x-coperni-closed-sole` | Grippy Footwear | Barreletics | Active (Limited) |
| 5 | Super-High Rise Reinforced Knee Yoga Tight | `lightly-padded-knee-yoga-pant-black` | Apparel | Barreletics | Active |
| 6 | Barreletics Performance Fabric T-Shirt/Tank | `barreletics-performance-fabric-yoga-t-shirts` | Apparel | Barreletics | Active |

### Live Production Names (SEO-optimized, current Shopify titles)

| Handle | Live Title |
|--------|-----------|
| `best-reformer-pilates-legree-workout-shoes` | Best Grippy Shoes for Barre, Pilates & Yoga — Closed Sole |
| `studio-performance-skin-footwear` | Best Grippy Shoes for Barre, Pilates & Yoga — Open Sole |
| `aquatic-performance-skins` | Aquatic Performance Skins |
| `barreletics-x-coperni-closed-sole` | Barreletics × Coperni — Closed Sole |
| `lightly-padded-knee-yoga-pant-black` | Lightly Padded Knee Yoga Pant — Black |
| `barreletics-performance-fabric-yoga-t-shirts` | Barreletics Performance Fabric Yoga T-Shirts |

---

## VARIANTS

### Footwear Size Matrix

| Size Label | Women's (US) | Men's (US) | Kids' (US) |
|-----------|-------------|-----------|-----------|
| Medium (M) | 5.5–7.5 | — | 2–5 |
| Large (L) | 7.5–11 | Up to 10.5 | — |

### Product 1: Closed Sole — Color × Size

| Color | Standard/LE | Price | M | L |
|-------|------------|-------|---|---|
| Black | Standard | $74 | ✓ | ✓ |
| LightGrey | Standard | $74 | ✓ | ✓ |
| DarkGrey | Standard | $74 | ✓ | ✓ |
| Blue | Standard | $74 | ✗ | ✗ |
| Bright Yellow | Standard | $74 | ✓ | ✓ |
| Dusty Rose | LE | $74 | ✓ | ✓ |
| Turquoise | LE | $78 | ✓ | ✓ |
| Copper Swirl | LE | $78 | ✗ | ✓ |
| Deep Teal | LE | $74 | ✓ | ✓ |
| Purple | LE | $78 | ✓ | ✓ |

**Future Design System Color Names:**  
Onyx → Black, Stone → LightGrey (others not yet mapped)

### Product 2: Open Sole — Color × Size

| Color | Standard/LE | Price | M | L |
|-------|------------|-------|---|---|
| Rivian Green | LE | $74 | ✓ | ✓ |
| Bright Yellow | Standard | $74 | ✓ | ✓ |
| White | Standard | $74 | ✓ | ✓ |
| Coral | Standard | $74 | ✓ | ✗ |
| Black | Standard | $74 | ✓ | ✓ |
| Blue | Standard | $74 | ✓ | ✓ |
| LightGrey | Standard | $74 | ✓ | ✓ |
| DarkGrey | Standard | $74 | ✓ | ✓ |
| Blue Heaven | LE | — | ✗ | ✗ |

### Product 3: Aquatic — Color × Size

| Color | Price | M | L | Kids |
|-------|-------|---|---|------|
| DarkGrey | $74 | ✓ | ✓ | 0 inv |
| Black | $74 | ✓ | ✓ | 0 inv |
| Blue | $74 | ✓ | ✓ | 0 inv |
| Bright Yellow | $74 | ✓ | ✓ | 0 inv |
| White | $74 | ✓ | ✓ | 0 inv |
| LightGrey | $74 | ✓ | ✓ | 0 inv |
| Coral | $74 | ✓ | ✓ | — |

### Product 4: Coperni — Size Only

| Size | Price | Status |
|------|-------|--------|
| M | $115 | Sold Out |
| L | $115 | In Stock |

### Product 5: Yoga Tight — Size × Color

| Size | US Size | Colors: Black, Black & White |
|------|---------|------------------------------|
| S | 2–4 | ✓ |
| M | 6–8 | ✓ |
| L | 10–12 | ✓ |
| XL | 12–14 | ✓ |

Price: $89 (sale) / $129 (compare-at)

### Product 6: T-Shirt/Tank — Size × Style

| Size | V-Neck ($39) | Tank Top ($34) |
|------|-------------|---------------|
| S | ✓ | ✓ |
| M | ✓ | ✓ |
| L | ✓ | ✓ |
| XL | ✓ | ✓ |

---

## COLLECTIONS

| Collection | Type | Rule | Products |
|-----------|------|------|----------|
| **All Products** | Automated | All active products | All |
| **In-Studio Grip** | Automated | tag = `in-studio-grip` | Closed Sole, Open Sole, Coperni |
| **Outdoor** | Manual | — | Aquatic Performance Skins |
| **Apparel** | Automated | product_type = `Apparel` | Yoga Tight, T-Shirt/Tank |
| **Limited Edition** | Automated | tag = `limited-edition` | Coperni, LE colorways |
| **Collaborations** | Manual | — | Coperni, Free People |
| **Best Sellers** | Manual | curated | Closed Sole, Open Sole |
| **New Arrivals** | Automated | created_at < 60 days | Dynamic |
| **Closed Sole** | Automated | tag = `closed-sole` | Closed Sole, Coperni |
| **Open Sole** | Automated | tag = `open-sole` | Open Sole |
| **Sale** | Automated | compare_at_price > price | Yoga Tight |

### Homepage Collection Display

Per docs/06 and the matured design, homepage shows a "Shop the Range" section with a product grid pulling from the primary footwear collection (In-Studio Grip).

---

## TAGS

### Product-Level Tags

| Tag | Purpose | Applied To |
|-----|---------|-----------|
| `in-studio-grip` | Collection membership | Closed, Open, Coperni |
| `outdoor` | Collection membership | Aquatic |
| `closed-sole` | Sole type filter | Closed Sole, Coperni, Aquatic |
| `open-sole` | Sole type filter | Open Sole |
| `limited-edition` | LE badge + collection | Coperni + LE colorways |
| `collaboration` | Collaboration collection | Coperni |
| `apparel` | Type filter | Yoga Tight, T-Shirt |
| `made-in-usa` | Trust/filter | All products |
| `barre` | Discipline filter | All footwear |
| `pilates` | Discipline filter | All footwear |
| `reformer` | Discipline filter | All footwear |
| `yoga` | Discipline filter | All footwear |
| `lagree` | Discipline filter | All footwear |
| `new-arrival` | Badge display | Dynamic |
| `best-seller` | Badge display | Curated |

### Variant-Level Discrimination (via option values, not tags)

Colors flagged as Limited Edition: Dusty Rose, Turquoise, Copper Swirl, Deep Teal, Purple, Rivian Green, Blue Heaven

---

## METAFIELDS

### Product-Level Metafields

| Namespace | Key | Type | Products | Example Value |
|-----------|-----|------|----------|---------------|
| `custom` | `sole_type` | single_line_text | All footwear | `closed` / `open` |
| `custom` | `grip_technology` | single_line_text | All footwear | `360° full-contact grip` |
| `custom` | `material_composition` | multi_line_text | All | `Proprietary grip material, antimicrobial, sweat-resistant` |
| `custom` | `care_instructions` | multi_line_text | All | (see docs/09 care section) |
| `custom` | `made_in` | single_line_text | All | `USA` |
| `custom` | `disciplines` | list.single_line_text | All footwear | `["Barre","Pilates","Reformer","Lagree","Yoga"]` |
| `custom` | `size_chart_type` | single_line_text | All | `footwear` / `apparel-pants` / `apparel-tops` |
| `custom` | `benefit_grid` | json | Footwear | 6-cell benefit array (from docs/04 line 403) |
| `custom` | `sock_math_data` | json | Closed/Open Sole | Comparison table data |
| `custom` | `collaboration_name` | single_line_text | Coperni | `Coperni Spring–Summer 2026` |
| `custom` | `collaboration_story` | multi_line_text | Coperni | Runway story copy |
| `custom` | `warranty_days` | number_integer | All | `90` |
| `custom` | `return_days` | number_integer | All | `30` |
| `custom` | `installment_count` | number_integer | All | `4` |
| `custom` | `discount_code` | single_line_text | Standard products | `save15` |
| `custom` | `discount_threshold` | number_integer | Standard products | `2` (buy 2+ to qualify) |
| `custom` | `hero_video_url` | url | Footwear | Motion grid video URL |
| `custom` | `faq_entries` | json | All | Array of {question, answer} objects |
| `custom` | `cross_sell_handles` | list.single_line_text | All | Related product handles |

### Variant-Level Metafields

| Namespace | Key | Type | Purpose | Example |
|-----------|-----|------|---------|---------|
| `custom` | `color_family` | single_line_text | Swatch grouping | `neutral` / `bright` / `limited` |
| `custom` | `limited_edition` | boolean | LE badge + pricing | `true` |
| `custom` | `design_system_name` | single_line_text | Future naming | `Onyx` / `Stone` |
| `custom` | `swatch_hex` | single_line_text | Color swatch rendering | `#000000` |
| `custom` | `fit_notes` | single_line_text | Per-color fit guidance | `Runs most forgiving for wider feet` |

### Collection-Level Metafields

| Namespace | Key | Type | Purpose |
|-----------|-----|------|---------|
| `custom` | `collection_headline` | single_line_text | Section title override |
| `custom` | `collection_subhead` | multi_line_text | Marketing description |
| `custom` | `hero_image` | file_reference | Collection hero image |
| `custom` | `collection_badge` | single_line_text | Badge text (e.g., "Limited") |
| `custom` | `sort_priority` | number_integer | Manual sort weight |

---

## MEDIA

### Required Images Per Product (Footwear)

| Slot | Purpose | Specs | Source |
|------|---------|-------|--------|
| Hero (per color) | Primary product shot | 1:1 aspect, white/neutral bg, 2000×2000px | Shopify CDN |
| Gallery 2–4 | Alternate angles | 1:1, same treatment | Shopify CDN |
| Lifestyle | In-use/studio shot | 4:3 or 1:1, real environment | Photo library |
| On-foot detail | Close-up grip/fit | 1:1, macro detail | Photo library |
| Size chart | Size reference graphic | Static image | Generated asset |
| Swatch | Color circle for PDP | 46×46px circle, content-box | CSS background-color (no image needed) |

### Required Images Per Product (Apparel)

| Slot | Purpose | Specs |
|------|---------|-------|
| Hero (per color) | Flat lay or model | 1:1, 2000×2000px |
| Gallery 2–3 | Detail/back/side | 1:1 |
| Size chart | Measurement graphic | Static image |

### PDP Section Media

| Section | Media Type | Count |
|---------|-----------|-------|
| Gallery | Product images | 4–6 per color |
| Variant Grid | Product thumbnails | 1 per colorway |
| Motion Grid | Video placeholders (3) | 1:1 aspect |
| Reviews | Customer photos | 1 per review card |
| Coperni section | Runway + product | 2 images |

---

## REVIEWS (JudgeMe)

### Integration Requirements

| Requirement | Detail |
|-------------|--------|
| **Platform** | JudgeMe (installed) |
| **Display: PDP** | Review section with photo grid (3-column, cards with border-radius: 12px) |
| **Display: Homepage** | "Confidence, from the ground up" section — 3 featured reviews |
| **Star Color** | `#d4af37` (gold) per design system decision D-041 |
| **Review Count** | Badge showing total (297+ as of Jul 2026) |
| **Photo Reviews** | Prioritize reviews with customer images |
| **Widget Location** | Below variant grid, above FAQ on PDP |
| **Aggregate Rating** | Product structured data (JSON-LD) |
| **Collection Page** | Star rating + count on product cards |

### Approved Hero Reviews (for static display)

Source: docs/09-PRODUCT-KNOWLEDGE.md — 12+ curated reviews with full attribution, covering: price objection crushers, safety stories, instructor testimonials, durability proof.

---

## FAQ

### Data Location

| Source | Content | Format |
|--------|---------|--------|
| `manychat-kb/10-faq-general.md` | General FAQ (disciplines, surfaces, wearing with socks) | Markdown |
| `manychat-kb/09-faq-fit-sizing.md` | Fit & sizing FAQ | Markdown |
| `docs/08-LIVE-SITE-COPY-AUDIT.md` (URL 30) | Live site FAQ accordion | HTML |
| `docs/09-PRODUCT-KNOWLEDGE.md` | Consolidated FAQ entries | Structured |
| Product metafield `faq_entries` | Per-product FAQ | JSON array |

### PDP FAQ Section (Accordion)

From docs/05 and Section-27-FAQ.html:
- What surfaces do they work on?
- How do I know my size?
- Open Sole vs Closed Sole?
- How do I care for them?
- What's the return policy?
- Can I wear them with socks?
- Are they latex-free / silicone-free?

### FAQ → Product Connection

```
Product (metafield: faq_entries) ──► PDP FAQ accordion section
                                      │
manychat-kb/10-faq-general.md ────────┤ (source of truth)
manychat-kb/09-faq-fit-sizing.md ─────┘
                                      │
                                      ▼
                              ManyChat automation responses
```

---

## CROSS-SELLS

### Rules

| Product | Cross-Sell Logic | Recommended Products |
|---------|-----------------|---------------------|
| Closed Sole | Complement (different sole) + Apparel | Open Sole, Yoga Tight |
| Open Sole | Complement (different sole) + Apparel | Closed Sole, Yoga Tight |
| Aquatic | Complement (studio option) | Closed Sole, Open Sole |
| Coperni | Complement (everyday option) | Closed Sole (standard), Open Sole |
| Yoga Tight | Complement (footwear) | Closed Sole, Open Sole |
| T-Shirt/Tank | Complement (footwear + bottoms) | Closed Sole, Yoga Tight |

### Implementation

- Metafield `cross_sell_handles` on each product: list of product handles
- Theme renders "You May Also Like" section below reviews
- Fallback: automated by collection membership if metafield empty

---

## RELATIONSHIPS

```
PRODUCT → COLLECTION (many-to-many via tags/rules)
  ├── Closed Sole → [In-Studio Grip, All, Best Sellers, Closed Sole]
  ├── Open Sole → [In-Studio Grip, All, Best Sellers, Open Sole]
  ├── Aquatic → [Outdoor, All]
  ├── Coperni → [In-Studio Grip, Limited Edition, Collaborations, Closed Sole]
  ├── Yoga Tight → [Apparel, All, Sale]
  └── T-Shirt → [Apparel, All]

PRODUCT → PRODUCT (cross-sell, stored in metafield)
  ├── Closed Sole ↔ Open Sole (bidirectional complement)
  ├── Footwear → Apparel (upsell)
  └── Coperni → Standard (everyday alternative)

VARIANT → COLOR FAMILY (metafield grouping)
  ├── Neutral: Black, LightGrey, DarkGrey, White
  ├── Bright: Blue, Bright Yellow, Coral, Rivian Green
  └── Limited: Dusty Rose, Turquoise, Copper Swirl, Deep Teal, Purple, Blue Heaven

PRODUCT → FAQ (metafield → accordion)
  └── All footwear share base FAQ set; Coperni adds collaboration Q&A

PRODUCT → REVIEWS (JudgeMe product_id linkage)
  └── Each product has own review set; homepage pulls curated subset
```

---

## FUTURE EXPANSION

### Gift Cards

| Field | Plan |
|-------|------|
| Product type | `gift_card` (Shopify native) |
| Denominations | $50, $74, $100, $150 |
| Why $74 | Matches single-pair price — "Gift a pair" positioning |
| Collection | Standalone (not in footwear/apparel collections) |
| Metafields | None required (native Shopify handling) |

### Bundles

| Bundle Concept | Products | Discount | Implementation |
|---------------|----------|----------|----------------|
| Studio Set | Closed Sole + Open Sole | 15% (existing code: save15) | Discount function or bundle app |
| Complete Kit | Any 2 footwear + Yoga Tight | 20% | Bundle app |
| His & Hers | 2× any footwear | 15% | Existing discount code |

Notes: Current `save15` code for 2+ already covers basic bundling. Future bundles may need Shopify Functions for automatic application.

### Subscriptions

| Concept | Logic | Timeline |
|---------|-------|----------|
| Not applicable for footwear | Product lasts 4+ years — no consumable cycle | Not planned |
| Potential for apparel | Quarterly new colorway drops | Future exploration |

### One-Off Colors / Limited Drops

| Field | Plan |
|-------|------|
| Implementation | New variant added to existing product |
| Pricing | $78 (LE premium) per existing pattern |
| Metafield | `limited_edition: true` on variant |
| Badge | "Limited Edition" chip — `#3a8de8` on `#eaf3fc` (Decision D-009) |
| Inventory | Finite — no restock |
| Collection | Auto-added to "Limited Edition" via tag |

### New Colorways (Permanent)

| Field | Plan |
|-------|------|
| Implementation | New variant at standard $74 |
| Metafield | `limited_edition: false`, new `swatch_hex` |
| Color family | Assign to neutral/bright grouping |
| Design system name | Map to future naming (e.g., Onyx, Stone pattern) |
| Required assets | Hero + 3 gallery per size, swatch color value |

### Additional Product Lines (Speculative)

| Concept | Type | Dependencies |
|---------|------|-------------|
| Kids-specific SKU | Footwear | Separate product (not just variant size) with kid-specific copy |
| Men's-specific SKU | Footwear | Sizing note update; possibly separate product for SEO |
| Grip-specific accessories | Accessories | New product type, new collection |
| Studio bag / carry case | Accessories | New product type |

---

## SHOPIFY SCHEMA SUMMARY

```
Product
├── title (SEO-optimized live name)
├── handle (URL slug)
├── product_type: "Grippy Footwear" | "Apparel"
├── vendor: "Barreletics"
├── tags: [collection tags, discipline tags, badge tags]
├── metafields.custom.*: (see Metafields table above)
├── variants[]
│   ├── option1: Size (M / L / S / XL)
│   ├── option2: Color (Black / LightGrey / etc.)
│   ├── price
│   ├── compare_at_price (if on sale)
│   ├── inventory_quantity
│   ├── metafields.custom.*: (color_family, limited_edition, swatch_hex, etc.)
│   └── images[] (color-specific hero + gallery)
├── images[] (all product images)
└── body_html (product description — rendered on PDP)

Collection
├── title
├── handle
├── rules[] (automated) OR products[] (manual)
├── metafields.custom.*: (headline, hero_image, badge)
└── sort_order

Page (non-product)
├── /pages/returns-portal
├── /pages/free-people
├── /pages/size-guide
└── /pages/about (founder story)
```
