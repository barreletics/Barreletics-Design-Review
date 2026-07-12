# PDP Architecture

**Product Detail Page specification for Barreletics**

Last Updated: 2026-07-12  
Status: Matured specification (ready for theme development)

---

## Page Structure Overview

The PDP follows a **sticky header + single-column flow** with a two-column hero section at top.

```
┌─────────────────────────────┐
│  Rotating Ticker            │  (Announcement banner, auto-cycling)
├─────────────────────────────┤
│  Header (sticky)            │  (Navigation + branding, z-30)
├─────────────────────────────┤
│                             │
│  Hero Section (2-col)       │  (Gallery sticky left, buy box right)
│  • Gallery (sticky top)     │
│  • Buy Box (product controls)
│                             │
├─────────────────────────────┤
│  Variants Section           │  (Tabbed grid)
├─────────────────────────────┤
│  Reviews Section            │  (Customer testimonials grid)
├─────────────────────────────┤
│  [Additional sections]      │  (Benefits, videos, justifiers, FAQ, newsletter)
└─────────────────────────────┘
```

---

## 1. ROTATING TICKER

**Purpose:** Cycle through promotional/informational messages

**Markup:** `.pdp-ticker` (container), `.pdp-ticker__slide` (individual messages)

**Behavior:**
- Single strip at top, full width
- Messages cross-fade (0.55s transition)
- Auto-cycles between messages
- Height: 36px
- Uppercase, centered text, letter-spacing 0.12em

**Example messages:**
- "Buy 2 Save 15% · use code SAVE15"
- "🇺🇸 Made in USA · Free shipping over $150 · 30-day returns"
- "★ Trusted by 1000's of Instructors"

**Design tokens:**
- Background: var(--br-text) [#1c1916]
- Text color: #fff
- Font size: 12px (11px mobile)
- Font weight: 500
- Links: rgba(255,255,255,0.85), underline on hover

---

## 2. STICKY HEADER

**Purpose:** Persistent navigation and branding

**Markup:** `.pdp-header` (z-index: 30), `.pdp-header__inner` (grid container)

**Layout:** 3-column grid (nav | logo | util)

**Navigation:**
- Left: Primary nav (Grippy Footwear, Apparel, Collaborations, Journal, About Us)
- Center: Logo/branding
- Right: Account + Cart indicator

**Styling:**
- Background: #fff
- Border-bottom: 1px solid var(--br-line)
- Position: sticky, top: 0, z-index: 30
- Padding: 18px 32px
- Max-width: 1440px, centered

**Nav links:**
- Font size: 14px, weight: 500
- Color: var(--br-text)
- Hover: border-bottom appears
- Chevron icon for dropdowns

**Cart indicator:**
- Small dot visible when cart has items
- `.pdp-header__cart-dot` (pseudo-element or badge)

**Responsive:**
- Mobile: Hamburger menu (not specified in current spec, TBD)
- Tablet: Full nav preserved

---

## 3. HERO SECTION

**Purpose:** Primary product showcase + purchase controls

**Layout:** 2-column grid (gallery left, buy box right)

**Container specs:**
- `.pdp-hero` — display: grid, grid-template-columns: 1fr 1fr, gap: 64px
- Max-width: 1400px, centered
- Padding: 64px 40px
- Align-items: flex-start (gallery sticks, buy box scrolls past)

### 3.1 Gallery (Left Column)

**Markup:** `.pdp-gallery`, `.pdp-gallery__thumbs`, `.pdp-gallery__hero`

**Behavior:**
- Sticky positioning (top: 64px, below header)
- Flex column layout with 16px gap
- Primary image: 1:1 aspect ratio
- Thumbnails above or below (TBD based on mockup details)
- Zoom icon (⊕) on hover
- Image placeholder background: #f7f5f1 (off-white)

**Thumbnails:**
- Small preview squares
- Aria-selected attribute for active state
- Click to switch hero image
- Optional: Color-coded previews (e.g., `--blush`, `--dark`, `--video`)

**Responsive:**
- Desktop/tablet: Sticky positioning
- Mobile: Position: static (flows with page)

### 3.2 Buy Box (Right Column)

**Markup:** `.pdp-buy` (flex column, gap: 24px)

**Content structure:**

#### Trust Section
```
★★★★★ Trusted by 1000's of Instructors · read verified reviews
```
- Stars: 16px, color: var(--br-star) [#d4af37]
- Spacing: 2px letter-spacing
- Link to #reviews section

#### Headline Block
```
[Badge: "CLOSED SOLE"]
[Eyebrow: "Studio Performance Skin · Closed Sole"]
[SEO Label: "Best Grippy Shoes for Barre, Pilates & Yoga"]
[Main headline: "Secure in every hold. No sliding. No resets."]
[Description: "The premium grip system that replaced traditional grip socks — built for reformer, barre, and Megaformer."]
```

**Styling:**
- Badge: `.pdp-buy__badge` — 4px 10px padding, 10px font, uppercase, 0.08em letter-spacing, bg: var(--br-accent) [#c45c3f], white text
- Eyebrow: Accent color, smaller
- SEO label: Gray text, 13px
- Main headline (H1): 44px, weight 700, line-height 1.08, color: var(--br-text)
- Description: 16px, color: #4a4a4a, line-height: 1.6

#### Price Section
```
$74
or 4 payments of $18.50 · free shipping over $75
```

- Price now: `.pdp-buy__price-now` — 36px, weight 700, var(--br-text)
- Meta: `.pdp-buy__price-meta` — 13px, gray text, financing option + shipping note
- Optional sale pricing: strikethrough original, show sale price

#### Color Swatches
```
[Circular color buttons]
Compare all colors →
```

- `.pdp-buy__swatches` — flex, gap: 8px, flex-wrap, row-gap: 6px
- `.pdp-buy__swatch` — 23px diameter, border-radius 50%, border: 2px solid transparent, cursor pointer, 0.2s transition
- Hover: border-color: #9a9182
- Selected: aria-selected="true", border-color: var(--br-text)
- OnClick: Update hero image + name/description
- Link below swatches: "View all colors →"

#### Primary CTA
```
[Add to cart · $74]
```

- `.pdp-buy__cta` — full width, 18px padding, weight 600, bg: var(--br-text), white text
- Hover: bg: var(--br-accent)
- Size variants: compact / default / bold (configurable via tweaks)
- Include price in button text

#### Optional: Quick Links
- "Compare all colors"
- "Size guide"
- "Shipping details"

**Responsive:**
- Desktop: 2-column with sticky gallery
- Tablet (≤1024px): 2-column preserved, gallery slightly reflow
- Mobile (≤768px): 1-column stacked, gallery non-sticky, buy box full-width

---

## 4. VARIANTS SECTION

**Purpose:** Show related product variants (closed sole vs. open sole, color options, etc.)

**Markup:** `.pdp-variants__*` classes

**Layout:** Tabbed grid

### 4.1 Variants Header
```
[Label: "The Studio Collection"]
[Compare link: "Open vs closed → compare"]
```

### 4.2 Variant Tabs
```
[Closed sole] [Open sole]
```

- Role: tablist
- `.pdp-variant-tab` buttons
- aria-selected attribute for active
- Tab switching filters grid below

### 4.3 Variant Grid
- `.pdp-variants__grid` — 4-column grid, 20px gap
- Desktop: 4 columns
- Tablet (≤1024px): 2 columns
- Mobile (≤768px): 2 columns, 16px gap

### 4.4 Variant Card
```
[Image: 1:1, product photo]
[Name]
[Price]
[Add to cart / Quick add button]
```

- `.pdp-vcard__*` classes
- Image: aspect-ratio: 1, scale(1.05) on hover with 0.2s transition
- Name: 15px, weight 500
- Price: `.pdp-vcard__price` — 14px, bold
- Sale pricing: `.pdp-vcard__sale` — strikethrough original, show new price
- Quick Add: Visible on hover OR always visible (configurable via tweaks)
- Card styles: clean / bordered (configurable)

**Quick Add Behavior (configurable via data attributes):**
- `data-quick-add="off"` — Hidden, click card to product page
- `data-quick-add="hover"` — Appears on hover
- `data-quick-add="always"` — Always visible

**Responsive:**
- Images scale smoothly on zoom
- Card text remains readable at all breakpoints

---

## 5. REVIEWS SECTION

**Purpose:** Display customer testimonials and ratings

**Markup:** `.pdp-reviews__*` classes

### 5.1 Reviews Header
```
[Label: "Trusted by studios & instructors"]
[Title: "Real reviews from real customers"]
[Big stars: ★★★★★]
[Average rating text]
```

### 5.2 Review Grid
- `.pdp-reviews__grid` — 3-column grid, 32px gap
- Desktop: 3 columns
- Tablet (≤1024px): 2 columns
- Mobile: 1 column

### 5.3 Review Card
```
[Stars: ★★★★★]
[Verified badge]
[Title: "Game-changer for reformer"]
[Body: Long-form testimonial text]
[Attribution: "Jamie L. · Onyx · 2 weeks ago"]
```

- `.pdp-review` — article wrapper, white background, rounded, border: 1px solid #e6e6e6
- Stars: `.pdp-review__stars` — 14px, color: var(--br-star), 2px letter-spacing
- Verified badge: `.pdp-review__verified` — 11px, small gray label
- Title: `.pdp-review__title` — H3, 16px, weight 600, var(--br-text)
- Body: `.pdp-review__body` — 15px, #4a4a4a, line-height 1.7, italic
- Attribution: `.pdp-review__attr` — 13px, var(--br-text), includes buyer name, color worn, date

**Verified Buyer Badge:**
- Always shown by default
- Togglable via tweaks: `.pdp-buy__verified` show/hide
- Gray label, small text

**Reviews Footer:**
- Links: "Read all reviews →" + "Write a review"
- Both link to full reviews page or modal

---

## 6. ADDITIONAL SECTIONS

### 6.1 Benefits Section
```
[Section label: "Why these shoes"]
[Section title: "Built for every studio"]

[3-column grid of benefits]
[01] [Icon/number] [Title] [Description]
[02] [Icon/number] [Title] [Description]
[03] [Icon/number] [Title] [Description]
```

- `.pdp-section` — max-width: 100%, padding: 64px 40px
- `.pdp-section__inner` — max-width: 1200px, centered
- `.pdp-benefits` — 3-column grid, 40px gap
- Tablet (≤1024px): 2 columns
- Mobile: 1 column, 32px gap
- Number: `.pdp-benefit__num` — 11px, uppercase, var(--br-accent)
- Title: `.pdp-benefit__title` — 20px, weight 700, var(--br-text)
- Subtitle: `.pdp-benefit__sub` — 15px, #4a4a4a, line-height 1.6

### 6.2 Variants Showcase (Motion/Video)
```
[Section title: "See it in action"]

[3-column grid of videos/motion]
[Video 1: Video placeholder] [Caption]
[Video 2: Video placeholder] [Caption]
[Video 3: Video placeholder] [Caption]
```

- `.pdp-motion-grid` — 3-column, 32px gap
- Tablet: 2 columns
- Mobile: 1 column
- Video container: `.pdp-motion__video` — 1:1 aspect-ratio, bg: #f9f9f9, flex centered
- Caption: `.pdp-motion__cap` — 14px, #4a4a4a, 16px top margin

### 6.3 Justifier Section
```
[Section title: "Why instructors trust these"]

[2-column grid of testimonial blocks]
[Tag: "STUDIO OWNER"]
[Quote: Long testimonial]
[Author: Name]

[Tag: "REFORMER INSTRUCTOR"]
[Quote: Long testimonial]
[Author: Name]
```

- `.pdp-justifier` — 2-column grid, 40px gap
- Mobile: 1 column
- Cards: `.pdp-justifier__card` — 32px padding, bg: #fff, border-left: 5px solid var(--br-accent)
- Tag: `.pdp-justifier__tag` — 11px, weight 700, var(--br-accent), uppercase, 0.08em letter-spacing
- Quote: `.pdp-justifier__quote` — 16px, #4a4a4a, line-height 1.7
- Author: `.pdp-justifier__author` — 13px, weight 700, var(--br-text)

### 6.4 FAQ Section
```
[Section title: "Frequently asked"]
[Bg: #f5f2ec (light beige)]

[Accordion items]
[Question?] [▼]
  [Answer paragraph]

[Question?] [▼]
  [Answer paragraph]
```

- `.pdp-faq` — 80px padding (40px LR), bg: #f5f2ec
- `.pdp-faq__container` — max-width: 760px, centered
- `.pdp-faq__item` — border-top: 1px solid var(--br-line), 18px padding vertical
- Trigger (button): `.pdp-faq__trigger` — flex space-between, 16px, weight 500, full width, no button styling
- Body: `.pdp-faq__body` — 14px, #6b645a, line-height 1.6, display: none by default
- Active: `.pdp-faq__body[data-open="true"]` — display: block

**Interactivity:**
- Click trigger to toggle open state
- Set `data-open="true"` on body to show
- Optional: animated chevron/icon rotation

### 6.5 Newsletter Section
```
[Section title: "Get our latest releases"]
[Subtext: "Be the first to know when new colors drop"]

[Email input]
[Submit button]

[Fine print: "We'll only use this to notify you about launches"]
```

- `.pdp-newsletter` — 56px padding, bg: #fff, border-top: 1px solid var(--br-line)
- `.pdp-newsletter__container` — max-width: 600px, text-align: center
- Title: `.pdp-newsletter__title` — 36px, weight 500, var(--br-text)
- Description: `.pdp-newsletter__desc` — 15px, #6b645a, line-height 1.6, 24px bottom margin
- Form: `.pdp-newsletter__form` — flex, gap: 8px
- Input: `.pdp-newsletter__input` — flex: 1, 12px padding, border: 1px solid var(--br-line), 14px font
- Button: `.pdp-newsletter__button` — 12px padding LR 24px, bg: var(--br-text), white text, 14px weight 600, uppercase, 0.05em letter-spacing, cursor pointer
- Button hover: bg: var(--br-accent)
- Fine print: `.pdp-newsletter__fine` — 11px, #9a9182

---

## 7. RESPONSIVE BREAKPOINTS

**Desktop (>1024px):**
- Hero 2-column layout
- Gallery sticky top: 64px
- Benefits 3-column, 40px gap
- Motion grid 3-column
- Reviews 3-column
- Justifier 2-column

**Tablet (≤1024px):**
- Hero 2-column preserved
- Benefits 2-column, 40px gap
- Motion grid 2-column
- Reviews 2-column
- Justifier 1-column
- Variants 2-column

**Mobile (≤768px):**
- Hero 1-column stacked (gallery non-sticky)
- All sections: 1-column flow
- Padding reduced: 16px LR vs 40px
- Variants 2-column
- Section titles: 32px vs 42px
- Buy box name: 32px vs 44px

---

## 8. DESIGN TOKENS

**Colors:**
- Primary text: `var(--br-text)` #1c1916
- Accent: `var(--br-accent)` #c45c3f (coral)
- Stars: `var(--br-star)` #d4af37 (gold)
- Muted text: #8a8a8a, #6b645a, #4a4a4a
- Borders: `var(--br-line)` #d6cfc0 (warm beige)
- Backgrounds: #fff (primary), #f9f9f9 (alt), #f5f2ec (section)

**Typography:**
- Font family: 'Roboto', system sans
- Headings: weight 700
- Body: weight 400-500
- Letter-spacing: Varies by context (0.01em, 0.05em, 0.08em, 0.12em)

**Spacing:**
- Section padding: 64px (desktop), 48px (tablet), 32px (mobile)
- Internal gaps: 16px–40px depending on context
- Margin resets: All headings/paragraphs reset to 0

**Transitions:**
- Standard: 0.2s ease
- Ticker/fades: 0.55s ease

---

## 9. TWEAKABLE SETTINGS

**Via pdp-tweaks.jsx:**

1. **Quick Add Mode**
   - `off` — Hidden until click
   - `hover` — Visible on card hover
   - `always` — Always visible (sets `data-quick-add` on root)

2. **Card Style**
   - `clean` — Minimal borders
   - `bordered` — Full border treatment (sets `data-card-style` on root)

3. **Show Verified Badge**
   - Toggle review section verified badges on/off (sets `data-verified="on"|"off"`)

4. **CTA Size**
   - `compact` — Reduced padding
   - `default` — Standard
   - `bold` — Extra prominent (sets `data-cta-size` on root)

---

## 10. STICKY ADD TO CART BEHAVIOR

**Primary CTA:** Buy box "Add to cart · $74" button

**Sticky behavior (current design):**
- Not currently sticky; scrolls out of view with buy box
- **Potential future enhancement:** Add sticky "Add to cart" bar that persists at bottom or follows hero as user scrolls

**Variant:** Quick Add on variant cards
- Separate inline buttons on variant grid cards
- Configurable to appear on hover or always

---

## 11. INTERACTIONS & MICRO-BEHAVIORS

**Color Swatch Selection:**
- Click swatch to update hero image
- Update product description/pricing if variant-specific
- Animate image transition (fade or slide)
- Update active state: border-color and outline

**Variant Tab Switching:**
- Click tab to filter grid below
- Smooth transition (optional: fade/slide)
- Update aria-selected attribute
- Persist selection in URL hash (optional)

**FAQ Accordion:**
- Click question to toggle answer display
- Animate chevron rotation (optional)
- Smooth open/close with transition
- Only one item open at a time (optional)

**Newsletter Form:**
- Input validation (email format)
- Submit action (optional: show confirmation)
- Handle errors gracefully

---

## 12. ACCESSIBILITY

**ARIA attributes:**
- Gallery thumbnails: `aria-selected="true"|"false"`
- Color swatches: `aria-label="[Color name]"`, `aria-selected="true"`
- Variant tabs: `role="tablist"`, aria-selected on active
- FAQ items: Expandable/collapsible with aria-expanded
- Gallery: Zoom button or interaction hint
- Links: Standard semantics

**Semantic HTML:**
- Main hero: `<section>`
- Reviews: `<article>` wrapper per review
- FAQ: Structure for screen reader navigation
- Skip links: Optional (TBD)

**Color contrast:**
- All text meets WCAG AA minimum (4.5:1 for normal text, 3:1 for large text)
- Swatch selections: Clear visual feedback (border + color)

---

## 13. PERFORMANCE NOTES

**Image loading:**
- Hero image: Load eagerly (above fold)
- Thumbnails: Lazy load or load on demand
- Variant grid: Lazy load as user approaches section
- Consider WebP + fallback formats

**CSS:**
- All PDP styles in `pdp-styles.css`
- Inherits design tokens from `audit-styles.css`
- Class-based BEM naming: `.pdp-[component]__[element]`

**JavaScript:**
- Ticker auto-cycle: CSS animation or JS interval
- Gallery image switching: Vanilla JS or framework
- FAQ accordion: Optional CSS `details` element or custom JS
- Color swatch switching: Data attributes + DOM updates

---

## 14. FUTURE ENHANCEMENTS

**Considerations for future iterations:**

1. **Image gallery:**
   - Swipe/drag support on mobile
   - Full-screen zoom view
   - Video embed support (360° product spin, etc.)

2. **Sticky button:**
   - Sticky "Add to cart" bar following hero scrollout (monitor UX impact)

3. **Size guide modal:**
   - Link from buy box to size/fit guide
   - Optional integrated modal or external page

4. **Comparison tool:**
   - "Compare all colors" link expands side-by-side variant view
   - Filtering by size, sole type, etc.

5. **Personalization:**
   - Recently viewed products
   - AI-driven recommendations
   - Variant pre-selection based on previous purchase

6. **Social proof:**
   - Instagram feed integration
   - User-generated content (UGC) carousel
   - Live review count + timestamp

7. **Internationalization:**
   - Currency switcher
   - Multi-language support
   - Geo-specific messaging (shipping, duties, taxes)

---

## 15. EXPORTED FILES

**HTML prototypes:**
- `Barreletics PDP - Matured.html` — Finalized design markup + styles
- `Barreletics-PDP-v36-Jul2026.html` — Latest version/alternate

**Style files:**
- `pdp-styles.css` — Pixel-final PDP stylesheet
- `audit-styles.css` — Design tokens and color system
- `maturation-styles.css` — Style refinements
- `pages-extras.css` — Additional page-level styles

**JavaScript:**
- `pdp-tweaks.jsx` — Interactive configuration panel for design variants
- `ticker.js` — Rotating announcement banner logic (if separate)

---

## 16. DESIGN SPECIFICATIONS REFERENCE

**Key files from design system:**
- Color palette: Defined in audit-styles.css variables
- Typography scale: 11px, 12px, 13px, 14px, 15px, 16px, 20px, 36px, 42px, 44px
- Spacing scale: 4px, 6px, 8px, 12px, 16px, 18px, 20px, 24px, 28px, 32px, 40px, 48px, 56px, 64px, 80px

**Consistent with:**
- Barreletics Brand North Star (01-BRAND-NORTH-STAR.md)
- Brand System design (02-BRAND-SYSTEM.md)
- Component Library (04-COMPONENT-LIBRARY.md) — includes Sticky Add to Cart, Variant Grid, Reviews, etc.

---

## STATUS

✅ **Consolidated specification** — All PDP elements documented and ready for theme conversion  
✅ **Design review complete** — Matured HTML prototypes approved  
✅ **Responsive verified** — Breakpoints tested across desktop, tablet, mobile  
✅ **Accessibility checked** — ARIA labels and semantic HTML noted  

**Next steps:**
- Convert to Shopify Liquid theme (`.liquid` templates)
- Integrate with Shopify product data API
- Connect real images, pricing, variant inventory
- Test with actual product data

---

**End of PDP Architecture Specification**
