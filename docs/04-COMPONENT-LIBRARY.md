# Component Library

**Status:** Authoritative  
**Purpose:** Single source of truth for all reusable components, page sections, and layout patterns

---

## Core Design System

### Typography
- **Font:** Roboto only (300–700). No other font families.
- **Eyebrows (labels):** 12px / font-weight 700 / letter-spacing 0.14em / uppercase
  - On dark sections: WHITE rgba(255,255,255,0.7)
  - On light/white bg: Coral #f97250 (var(--br-accent)) only
- **Buttons:** Font weight 600 / letter-spacing 0.06em / 14px size
- **Headings:** Use semantic tags (h1, h2, h3) with appropriate hierarchy

### Color Palette
- **Background:** #ffffff
- **Text (primary):** #050505
- **Accent (coral):** #f97250 (var(--br-accent))
- **Star (rating):** #fbc02d
- **Alt background:** #f9f7f2
- **Text (soft):** #6a6a6a
- **Text (muted):** #999999
- **Line (border):** #e5e2db

### Spacing & Borders
- **Borders:** 1px solid var(--br-line) (#e5e2db)
- **Border radius:** No radius by default
  - Cards: 0px (square)
  - Where matured direction uses radius: 2px or 4px only
  - Never use pill-card style (12–16px radius)

### Button System

**Three variants, all square (border-radius: 0px, no drop shadows, no gradients):**

1. **Primary** — Black background (#050505) with white text
   - 14px text size / 600 weight / 0.06em letter-spacing
   - Padding: 14px y / 28px x
   - Used for: Primary CTAs like "Shop Collection", "Add to Cart"

2. **Secondary** — Ink outline border with ink text on transparent background
   - Same sizing as primary
   - Border: 1px solid text color
   - Used for: Alternative actions, secondary CTAs

3. **Tertiary** — Text + arrow, no border
   - Text only, right arrow suffix (→)
   - Same sizing
   - Used for: Links, learn more, pagination

---

## Interactive Components

### Ticker Bar
**Purpose:** Highlight promotional messages and shipping info  
**Business Goal:** Increase conversion by highlighting SAVE15 code, made in USA, and social proof  
**User Goal:** Quick access to key benefits and promotions  
**Behavior:** 3-slide auto-rotator, 4s interval, opacity crossfade 320ms ease  
**Interaction:** Pause on hover  
**Implementation:** ticker.js  
**Slides (home):** SAVE15 · Made in USA · 1,000+ instructors  
**Mobile:** Full width, same behavior  
**Desktop:** Full width, same behavior  
**Placement Rules:** Always top of page, above header  
**Animation:** Respect `@media (prefers-reduced-motion: no-preference)` — final state visible without animation

### Header / Navigation
**Purpose:** Main navigation and shopping cart  
**Business Goal:** Drive product discovery and checkout  
**User Goal:** Browse categories, access account, view cart  
**Layout:**
- Centered logo
- Left side: Category links (Grippy Footwear, Apparel, Collaborations, Journal, About Us)
- Right side: Account, Cart
**Behavior:** 
- Sticky on scroll
- Adds 1px bottom hairline (var(--br-line)) on scroll > 8px
- Cart badge dot (var(--br-accent)) visible only when items > 0
**Mobile Requirement:** Hamburger menu (currently hidden — needs implementation)  
**Desktop:** Full horizontal nav  
**Mobile:** Hamburger menu for categories, persistent cart icon  
**Design Rules:** 
- Use Roboto 600 weight for nav text
- No background until scroll > 8px
- Hairline adds smoothly on scroll

### Hero (Main Hero Section)
**Purpose:** Communicate core brand promise with rotating messaging  
**Business Goal:** Set brand tone and communicate key differentiator  
**User Goal:** Understand what Barreletics is  
**Slogan Anchor:** "Secure in every hold. No sliding. No resets."  
**Content:**
- Rotating eyebrow (3.5s cycle, 5 messages)
- H1 headline
- Full-bleed background image
- Primary + Secondary CTAs
**Primary CTA:** "Shop performance skins" → Collection  
**Secondary CTA:** "See how it grips" → in-page anchor #why-it-works  
**Design Rules:**
- Full viewport width and height
- Centered text overlay
- Hero image: barreletics.com/cdn/shop/files/IMG_2917.jpg
**Mobile:** Stack vertically, reduce image height, maintain full bleed width  
**Desktop:** Full bleed, centered layout  
**Eyebrow Rotation (Home):**
1. "The Pilates sock era is over."
2. "A new kind of grip shoe."
3. "Trusted by 1,000's of instructors."
4. "Made in USA. Built for the carriage."
5. "Barre. Reformer. Megaformer. One shoe."

### Pillar Strip
**Purpose:** Highlight product attributes and key features  
**Business Goal:** Reinforce product benefits at a glance  
**User Goal:** Understand core product attributes  
**Slogan Anchor:** #letusknockyoursocksoff  
**Content:** 6 pillars (attributes):
1. 360° Grip
2. Two Surfaces
3. No Adjustments
4. Rinse & Reuse
5. No Latex
6. Barefoot  
**Design Rules:**
- Horizontal card layout
- Light background (var(--alt-bg), #f9f7f2)
- Each pillar: icon + label + short description
- Equal column widths
**Mobile:** Stack vertically or 2-column grid  
**Desktop:** 6-column grid, full width  
**Placement Rules:** Appears early on all pages after main hero

### 50/50 Split Section
**Purpose:** Establish credibility with proof + messaging  
**Business Goal:** Drive conversion through visual proof and testimonial  
**User Goal:** See product in action and hear from users  
**Layout:** Image (left) + copy/messaging (right), or reversed  
**Trusted Line (All Splits):** Stars (★★★★★) + "Trusted by 1,000's of instructors & studios"  
**Sizing:** Fixed through iteration — DO NOT change split CSS proportions  
**Three Versions on Home:**  
1. **Split 1 — "Never slip in chair pose."** (Grip Proof)
   - Image: Multi_Image.jpg (barreletics.com/cdn/shop/files/Multi_Image.jpg)
   - Copy: "Or side plank. Or reformer bridges…"
   - Includes: Trusted line + stars

2. **Split 2 — "Progress, built from the ground up."** (Journey/Transformation)
   - Copy left, image right (reversed layout)
   - Transformation messaging

3. **Split 3 — "Never loses grip."** (Durability Proof)
   - Video (pink foot video): cdn.shopify.com/videos/c/o/v/d11716a75dc64da7ba1a5521e39d942b.mov
   - Includes: Trusted line + stars

**Design Rules:**
- Dark text on light bg (or light text on dark bg)
- Ample whitespace
- High-quality imagery or video
- Video plays on hover/interaction
**Mobile:** Stack vertically, image top or bottom  
**Desktop:** Side-by-side 50/50 split

### Sock ⇄ Skin Toggle
**Purpose:** Show product in two different states  
**Business Goal:** Communicate product versatility  
**User Goal:** See both product variations  
**Behavior:** 
- Cross-fade between two image states (240ms ease-out)
- Swap two stat figures on toggle
- State persists via aria-pressed
**Mobile:** Full width toggle, large touch target  
**Desktop:** Centered, appropriate sizing  
**Interaction:** Click to toggle, visual feedback on active state

### Product Card (Variant Card)
**Purpose:** Display individual product variations  
**Business Goal:** Drive product discovery and add-to-cart  
**User Goal:** Browse and purchase specific variants  
**Content:**
- Product image
- Color name
- Price
- Quick Add button (primary button style)
- Hover state: underline draws into caption
**Product Grid Rule:** Each color = its own card with image, color name, price, Quick Add button  
- Tabs: Closed Sole / Open Sole (at grid level)
- Size (M/L): At grid level, not per-card
- NEVER use swatches on one card
- Add to cart from home page (no PDP redirect required)
**Hover Behavior:**
- Image scales 1.02x over 320ms ease-out
- Caption underline draws in
- Primary button becomes interactive
**Mobile:** Stack vertically, full width cards  
**Desktop:** 4-column grid (or configured per page)

### PDP Main Section
**Purpose:** Enable product purchase and detail exploration  
**Business Goal:** Maximize conversion and reduce friction  
**User Goal:** See product details, select size/options, add to cart  
**Slogan Anchor:** "Your body moves. Your grip doesn't."  
**Layout:**
- Left: PDP gallery (see below)
- Right: Buy box
  - Product title
  - Price
  - Size selector (Size & Fit tab)
  - Add to Cart button (primary)
  - Quick specs
- Tabs below (or expandable sections):
  - Description
  - Size & Fit
  - Care
  - Returns
**Design Rules:** Maintain conversion flow, minimal friction  
**Mobile:** Gallery top, buy box below, sticky Add to Cart button  
**Desktop:** 2-column layout, buy box sticky on scroll

### PDP Gallery
**Purpose:** Allow detailed product inspection  
**Business Goal:** Increase conversion through visual confidence  
**User Goal:** See product from multiple angles  
**Behavior:**
- Click thumbnail → swap main image
- Pinch/double-tap → zoom on touch
- Keyboard ←/→ → advance between images
**Thumbnails:** Vertical strip below main image  
**Zoom:** Modal or lightbox expansion  
**Mobile:** Full width, responsive thumbnail sizing  
**Desktop:** Standard 2-column layout

### PDP Size Picker
**Purpose:** Facilitate size selection  
**Business Goal:** Reduce returns from incorrect sizing  
**User Goal:** Confidently select the right size  
**Behavior:**
- Size pills toggle aria-pressed state
- Out-of-stock pills: strikethrough + cursor not-allowed
- Selected state: highlighted background
**Design Rules:** Clear visual hierarchy, accessibility compliance  
**Label:** "Size Guide" link above/below

### Accordion (PDP Specs/FAQ)
**Purpose:** Organize detailed information compactly  
**Business Goal:** Provide info without overwhelming page  
**User Goal:** Find specific details quickly  
**Behavior:**
- One section open at a time
- 200ms height transition
- Smooth expand/collapse
**Design Rules:** Clear labels, good spacing  
**Icon:** Chevron/arrow indicates state  
**Mobile:** Full width, touch-friendly headers

### Reviews Component
**Purpose:** Display customer testimonials and ratings  
**Business Goal:** Build trust through social proof  
**User Goal:** Hear from other customers  
**Content:**
- Star rating (5 stars)
- Customer name
- Review text
- "Verified purchase" badge (if available)
- Load More button (pagination)
**Behavior:** "Load more" appends next 6 reviews; no full pagination  
**Design Rules:**
- Clean card layout
- Consistent spacing
- High contrast for readability
**Mobile:** Single column, full width cards  
**Desktop:** 2-3 column grid (or card list)

### Reviews Load More Button
**Purpose:** Lazy-load additional reviews  
**Business Goal:** Keep page lightweight, encourage browsing  
**User Goal:** Browse more reviews without page reload  
**Behavior:** Append next 6 reviews per click  
**Styling:** Secondary button style  
**Placement:** Below review cards

### Collection Filter Row
**Purpose:** Allow browsing by product attributes  
**Business Goal:** Reduce friction in product discovery  
**User Goal:** Find products matching preferences  
**Filter Types:** Inline chips (not sidebar)  
**Behavior:**
- Multi-select within a facet (e.g., size)
- Exclusive between facets (e.g., only one sole type)
- URL-syncs via query params
- Visual feedback for active filters
**Design Rules:**
- Horizontal chip layout
- Clear labels
- Secondary button styling
**Mobile:** Horizontal scroll or wrapping  
**Desktop:** Full width, wrapping

### Article / Blog Card
**Purpose:** Promote journal/content  
**Business Goal:** Drive traffic to long-form content  
**User Goal:** Discover brand stories and tips  
**Content:**
- Featured image
- Category label
- Headline
- Excerpt (2-3 lines)
- "Read more" link or CTA
**Design Rules:** Consistent card styling  
**Mobile:** Full width stack  
**Desktop:** 3-column grid (on home)

### Article Pull-Quote
**Purpose:** Highlight key insights from long-form content  
**Business Goal:** Drive readership with compelling excerpts  
**User Goal:** See key takeaways  
**Content:** Quote text (no animation)  
**Design Rules:**
- Larger typography (18px+)
- Distinct background or border
- Left or center alignment
**Styling:** Italic or distinct font style

### CTA Blocks
**Purpose:** Guide user actions  
**Business Goal:** Drive conversions (shop, sign up, learn more)  
**User Goal:** Know what action to take  
**Button Types:** Primary (conversion), Secondary (explore), Tertiary (learn more)  
**Copy Patterns:**
- "Shop the Collection" → Collection page
- "Shop Now" → PDP
- "Learn More" → #anchor or article
- "See How It Works" → video or section
- "Sign Up for Updates" → newsletter
**Design Rules:** Clear, action-oriented copy

### Guarantee Section
**Purpose:** Reduce purchase hesitation  
**Business Goal:** Increase conversion by removing risk  
**User Goal:** Feel safe buying  
**Slogan Anchor:** "Zero risk. All grip."  
**Content:**
- 30-day trial guarantee
- 90-day warranty
- Easy return instructions
- Badge/seal imagery
**Design Rules:** Trust-building visual hierarchy  
**Mobile:** Stack information vertically  
**Desktop:** 2-column or side-by-side layout

### Newsletter Signup
**Purpose:** Build email list  
**Business Goal:** Enable direct customer communication  
**User Goal:** Opt in to updates (benefits-driven)  
**Content:**
- Headline ("Get updates on new releases…")
- Email input
- Subscribe button (primary)
- Privacy notice
**Design Rules:** Minimal, low-friction form  
**Mobile:** Full width input  
**Desktop:** Inline or stacked

### Social Proof / Trust Badges
**Purpose:** Build credibility  
**Business Goal:** Increase conversion through trust signals  
**User Goal:** Feel confident in purchase  
**Elements:**
- Star rating (5★)
- Number of reviews ("1,000+ reviews")
- "Trusted by 1,000's of instructors & studios"
- Made in USA badge
- Security/return badges
**Placement:** Hero, product cards, checkout-related sections

### Footer
**Purpose:** Secondary navigation and legal  
**Business Goal:** SEO, navigation, legal compliance  
**User Goal:** Find links, contact info, policies  
**Content:**
- Footer navigation (columns)
- Contact info
- Social links
- Copyright
- Privacy/Terms links
- Newsletter signup (sometimes)
**Design Rules:** Dark background typically, light text  
**Mobile:** Stack vertically  
**Desktop:** Multi-column layout

### Benefit Grid
**Purpose:** List product advantages in scannable format  
**Business Goal:** Communicate key differentiators  
**User Goal:** Quickly understand why product is better  
**Content:** 3-6 benefit cards, each with:
- Icon (optional)
- Benefit title
- Brief description (1-2 lines)
**Variants:**
- **Home Sock Math** (6 cells below comparison): 360° traction, Second-skin fit, Reformer-ready, Rinse & reuse, No latex/silicone, Barefoot-inspired
- **PDP Benefit Grid** (6 cards): Reformer-ready, No twist, Sweat-ready, Rinse & reuse, Skin-safe, Barefoot feel
- **Collection Benefit Grid** (3 cards): Reformer-ready, Two builds (closed/open), Rinse & reuse
**Design Rules:**
- Even spacing and sizing
- High contrast text
- Icon consistency
**Mobile:** Stack or 2-column  
**Desktop:** Multi-column grid

### Sock Math Section (Comparison Component)
**Purpose:** Show value vs. grip socks  
**Business Goal:** Drive purchase decision through comparison  
**User Goal:** Understand the cost of ownership and value proposition  
**Slogan Anchor (Home):** "Stop replacing. Start performing."  
**Slogan Anchor (PDP):** "One pair. Done."  
**Layout:**
- Eyebrow: "The Sock Math" (white on dark bg, #1a1a1a)
- Headline: "Stop replacing. Start performing." (full-bold second half)
- Subtext: "Grip socks have two failure points — your foot moves in the sock, and the sock moves on the floor. Barreletics eliminates both."
- Two cards side-by-side (dark bg #1a1a1a)

**Card 1 — Grip Socks:**
- Label: GRIP SOCKS
- Price: $336 (struck-through, light gray text)
- Subtitle: "per year · 8–12 pairs at $18–28 each"
- Rows:
  - Grip lifespan → 6–8 washes
  - Pairs per year → 8–12
  - Foot slips inside? → Yes
  - Grip after 6 months → Gone

**Card 2 — Barreletics:**
- Label: BARRELETICS (coral accent)
- Price: $74 (bold, prominent)
- Subtitle: "once · same grip class 1 to class 260"
- Rows (all bold/highlight):
  - Grip lifespan → 4+ years proven
  - Pairs needed → 1
  - Foot slips inside? → Impossible
  - Grip after 6 months → Identical to day 1

**Below Cards:** 6-cell benefit grid (dark bg, white text):
01 · 360° traction — Full-contact grip across entire underfoot — not patches of silicone dots that wash off.
02 · Second-skin fit — Your foot can't move inside it. That's the point. No twist, no bunch, no reset.
03 · Reformer-ready — Tested on Megaformer & reformer carriages, hardwood barre studios, and yoga mats.
04 · Rinse & reuse — Warm soapy water, air dry. No machine washing. No grip degradation.
05 · No latex · no silicone — Skin-safe proprietary grip material. Made in USA.
06 · Barefoot-inspired — Natural toe articulation. Move freely — without the slip.

**CTA:** SHOP THE COLLECTION → (primary button, centered below)

**PDP Version (Condensed):**
- Same layout, reduced height
- Same pricing and comparison
- Highlights: "Double failure" concept
- Quote: "Your foot moves in the sock. The sock moves on the floor. Now neither does."

**Design Rules:**
- Dark background maintains contrast
- Card styling: light borders only
- Typography hierarchy: label → price → rows
- 16px rows, 14px subtitle
**Mobile:** Stack cards vertically  
**Desktop:** 2-column side-by-side

### Disciplines Section
**Purpose:** Show product versatility across workout types  
**Business Goal:** Appeal to multiple customer segments  
**User Goal:** See that product works for their workout  
**Slogan Anchor:** "Barre. Reformer. Megaformer. One shoe."  
**Content:** 3 cards:
- **Barre** card
- **Reformer** card
- **Megaformer** card  
Each with: Icon/image + discipline name + 2-3 benefit lines specific to that discipline  
**Design Rules:** Consistent card styling, discipline-specific copy  
**Mobile:** Stack vertically  
**Desktop:** 3-column grid

### Coperni Collaboration Section
**Purpose:** Highlight brand partnership and heritage  
**Business Goal:** Drive traffic via brand association  
**User Goal:** Learn about exclusive collaboration  
**Slogan Anchor:** "The Pilates sock era is over."  
**Content:**
- Runway video (cdn.shopify.com/videos/c/o/v/d7ca87eac5034642851089c63af6a2d8.mov)
- OR still image (barreletics.com/cdn/shop/files/Screenshot_2026-03-20_at_6.53.30_PM.png)
- LE (Limited Edition) badge
- Copy about collaboration
- "Shop Now" CTA
**Design Rules:** Premium positioning, high-impact imagery  
**Mobile:** Full width video/image  
**Desktop:** Full-bleed section

### Testimonial / Review Quote
**Purpose:** Feature single standout customer review  
**Business Goal:** Social proof, conversion impact  
**User Goal:** Hear one compelling customer story  
**Content:**
- Quote text (larger font, 20px+)
- Customer name
- "Verified purchase" badge
- Star rating
- Optional: customer photo
**Design Rules:** Large, prominent typography; center alignment; high contrast  
**Mobile:** Center-aligned, full-width text  
**Desktop:** Center or left-aligned

### Founder Letter
**Purpose:** Personal founder communication to build trust and brand intimacy  
**Business Goal:** Humanize brand and build emotional connection  
**User Goal:** Understand founder's vision and commitment  
**Slogan Anchor:** Custom per founder message  
**Layout:**
- Dark background (var(--m-dark))
- Left: Founder image (proportional media)
- Right: Quote + body copy + signature
**Content:**
- Eyebrow label (optional)
- Opening quote (26–40px, 300 weight)
- Body text (15px, 1.65 line-height)
- Signature with title/role
- Optional: supporting details list
**Design Rules:**
- Premium dark positioning (builds prestige)
- High contrast white text on dark
- Max-width 48ch on copy
- Generous padding (76px vertical)
**Mobile:** Stack image top, copy below; single column  
**Desktop:** 2-column layout (0.85fr image : 1fr copy)
**Typography:** Roboto 300/600 weight, warm dark background  
**Spacing:** 76px vertical padding desktop, 48px mobile
**Interaction:** Static, no animation  
**HTML Source:** `/sections/founder-letter.html`

### Founder Story
**Purpose:** Narrative background on founder/brand origin  
**Business Goal:** Build credibility and brand authority  
**User Goal:** Understand the story and passion behind the product  
**Content:**
- Founder image
- First-person narrative or bio
- Key milestones or turning points
- Connection to product mission
**Design Rules:** Similar to Founder Letter; warm, premium treatment  
**Mobile:** Stack vertically  
**Desktop:** 2-column split  
**HTML Source:** `/sections/founder2.html`

### Manifesto
**Purpose:** Declare brand beliefs and core values  
**Business Goal:** Establish brand positioning and loyalty  
**User Goal:** Know what Barreletics stands for  
**Slogan Anchor:** Rotating manifesto statements  
**Layout:**
- Dark background (var(--m-dark))
- Centered text-only section
- Rotating headline (changes every 0.7s)
- Supporting subtitle
- Voice/tone tags below
**Content:**
- Eyebrow ("MANIFESTO" or custom)
- Rotating headline carousel (multiple claims)
- Optional: subtitle/body text (16px, soft white)
- Voice tags (e.g., "Rigorous," "Warm," "Precise")
**Design Rules:**
- Dark prestige positioning
- Large headline (38–92px clamp)
- Opacity transitions (0.7s ease)
- Centered alignment
- Generous vertical padding (96px)
**Mobile:** Reduced padding (60px), single column  
**Desktop:** Full-width center-aligned, 96px padding  
**Typography:** Roboto 300/600, all-caps eyebrow (11px, 0.18em letter-spacing)  
**Animation:** Rotate between manifesto statements, fade in/out (prefers-reduced-motion respected)  
**HTML Source:** `/sections/manifesto.html`, `/sections/manifesto2.html`

### Problem / Pain Point
**Purpose:** Agitate pain point and establish need for solution  
**Business Goal:** Drive desire for product by highlighting existing frustration  
**User Goal:** Recognize their struggle in a relatable way  
**Layout:**
- Light/white background
- Left column: Problem statement + old solution list
- Right column: Supporting details or image
**Content:**
- Eyebrow ("THE PROBLEM" or custom)
- Display headline (30–50px)
- Body description (15px, soft text)
- List of old/failed solutions with strikethrough
- Optional: supporting visual or stat
**Design Rules:**
- Left-aligned copy (1.15fr column)
- Right sidebar for visual context (0.85fr)
- Strikethrough on old solutions (var(--m-accent) color)
- Border dividers between list items
**Mobile:** Stack single column  
**Desktop:** 2-column grid (1.15fr : 0.85fr)
**Typography:** Roboto, body 15px, list items 15px with strikethrough  
**Spacing:** 64px padding, 14px gap between list items  
**Design Variations:** problem.html and problem2.html (different messaging)  
**HTML Source:** `/sections/problem.html`, `/sections/problem2.html`

### Closing Statement (Call to Final Action)
**Purpose:** Bold final message before footer, reinforce primary CTA  
**Business Goal:** Drive final conversion decision  
**User Goal:** Know the last step to take  
**Layout:**
- Dark background (var(--m-dark))
- Centered text + CTA button
- Restrained, high-impact copy
**Content:**
- Eyebrow (optional)
- Headline (34–60px, 300 weight)
- Subtitle/body (16px, soft white)
- Primary button (white bg, dark text)
- Optional: fine print or offer details
**Design Rules:**
- Dark prestige positioning
- Center-aligned text
- Ample vertical padding (88px)
- Button contrast: white on dark
**Mobile:** Reduced padding (48px), single column  
**Desktop:** Center-aligned, 88px padding  
**Typography:** Roboto 300/600, headline bold second half optional  
**Button:** Primary style, white background, dark text  
**HTML Source:** `/sections/closing-statement.html`

### Credibility / Social Proof Band
**Purpose:** Establish trust through brand partnerships and logos  
**Business Goal:** Build legitimacy through association  
**User Goal:** See trusted brands using Barreletics  
**Slogan Anchor:** "Trusted by..." messaging  
**Layout:**
- Dark prestige background
- Grid of 2–4 logo/partner cells with image support
- Logo bar below (partner counts/titles)
**Content:**
- Eyebrow
- Headline (30–52px)
- Subtext (16px, soft white)
- Grid cells: each has image + caption (studio name + "classes")
- Logo bar with brand names
**Design Rules:**
- Dark prestige (var(--m-dark))
- Consistent cell sizing (5:4 aspect ratio)
- Logo bar with centered text (26px font weight 400)
- Small caps on counts (10px, uppercase)
**Mobile:** 1-column grid, logo bar stacks vertically  
**Desktop:** 2-column grid (gap 2px), logo bar horizontal  
**Typography:** Roboto, eyebrow 11px technical, logo 18–26px clamp  
**Spacing:** 56px padding top/bottom, 2px cell gaps  
**Design Variations:** Multiple client logos and counts  
**HTML Source:** `/sections/credibility.html`

### Closing CTAs & Button Groups
**Purpose:** Action-oriented button clusters throughout page  
**Business Goal:** Maximize conversion funnel entry points  
**User Goal:** Know what to do next  
**Button Variants:**
- Primary (black bg, white text): "Shop Collection", "Add to Cart", "Buy Now"
- Secondary (outline): "Learn More", "See Details"
- Tertiary (text + arrow): "Read full story →", "Shop now →"
**Design Rules:** No shadows, gradients, or rounded corners  
**Spacing:** 28px horizontal padding, 14px vertical  
**Typography:** 12px, 600 weight, 0.06em letter-spacing, uppercase  
**Mobile:** Full-width or stacked on small screens  
**Desktop:** Inline, flex-wrapped  
**Interaction:** Slight opacity shift on hover (0.9)  
**HTML Source:** Integrated in all section components

### Variants Grid (Product Selector)
**Purpose:** Allow users to select shoe build (Closed Sole / Open Sole) and color  
**Business Goal:** Enable informed purchase decisions  
**User Goal:** Find and customize preferred option  
**Layout:**
- Left: Style selector tabs + color swatches
- Right: Product image preview
**Content:**
- Label row (Build selection): "Closed Sole" | "Open Sole"
- Color picker: Click to select from available colors
- Color name label below swatches
- Summary: "You chose: [Color] [Build]" + price
- Primary button: "Add to Cart"
**Behavior:**
- Tabs: Mutually exclusive (only one build active at a time)
- Color picker: Multi-select within build, visual feedback (outline on active)
- Image updates as selections change
**Design Rules:**
- Left-column form (1fr), right-column image (1.1fr)
- 56px gap between
- Font size: Color name 13px; "Chosen" summary 14px
- Price: 24px clamp, 300 weight
- Button: 11.5px uppercase, full-width
**Mobile:** Stack form top, image bottom; single column  
**Desktop:** 2-column side-by-side  
**Typography:** Roboto, monospace labels (11px), standard body (13–14px)  
**Spacing:** 64px padding section, 28px gap between form rows, 22px button margin-top  
**Source:** `/sections/variants.html`

### Product Grid (Range/Collection Display)
**Purpose:** Showcase all available products in a collection  
**Business Goal:** Drive product discovery and quick add-to-cart  
**User Goal:** Browse and purchase products without PDP redirect  
**Layout:**
- Grid of product cards (3–4 columns depending on page context)
- Each card: image + color name + price + "Quick Add" CTA
**Card Content:**
- Product image (aspect ratio 4:3 or 3:4)
- Product name (21px, 400 weight, dark text)
- Optional: Product number/index (11px monospace, accent color)
- Description line (14px, soft text, max 26ch)
- Price row: $XX + "Shop" link (12px, accent, no underline)
**Behavior:**
- Hover: Image opacity or scale (1.02x), caption underline
- No swatches on card (swatches belong in detailed modal/PDP only)
- Quick Add: Adds to cart directly from grid
**Design Rules:**
- 28px gap between cards
- Light background (var(--m-bg))
- High contrast product names
- Price: 14px dark weight 500
**Mobile:** 1–2 column stack  
**Desktop:** 3-column grid at 64px padding  
**Typography:** Roboto 400/500/600, number (11px monospace), name (21px), desc (14px)  
**Spacing:** 64px padding, 28px card gap, 20px bottom padding in card  
**Variants:** Home product grid, collection variants grid, "Pairs with your kit" rail  
**Source:** `/sections/range.html`

### Sticky Add to Cart Button
**Purpose:** Enable convenient checkout on mobile/desktop while browsing PDP content  
**Business Goal:** Reduce friction in purchase flow  
**User Goal:** Add to cart from any scroll position  
**Layout:**
- Fixed position (bottom on mobile, floating on desktop)
- Single primary button spanning available width
- Label: "Add to Cart" or "Choose Size & Add"
**Behavior:**
- Appears after hero/main PDP section
- Disappears on footer overlap (intelligent positioning)
- Text updates based on current selection state
- Clicking opens cart summary or proceeds to checkout
**Design Rules:**
- Primary button styling (black bg, white text)
- Full available width (mobile), reduced width (desktop)
- Safe area padding on mobile
- Shadow on desktop (subtle elevation)
**Mobile:** Fixed bottom, 100% width of viewport - safe padding  
**Desktop:** Floating above footer, max-width 480px, centered  
**Typography:** Button 12px, 600 weight, uppercase  
**Z-Index:** High (above other content but below modals)  
**Source:** Integrated in PDP sections

### Promo Tiles & Range Showcase
**Purpose:** Highlight featured products or promotions  
**Business Goal:** Cross-sell, highlight new releases, drive impulse buys  
**User Goal:** Discover new or promoted options  
**Layout:**
- 2-column grid of tiles (or 1-column on mobile)
- Each tile: image + small label (LE, "New", etc.) + brief copy
**Content:**
- Tile image (4:3 aspect ratio or custom)
- Label: "LE" (Limited Edition), "New Release", "Bestseller"
- Copy (optional): Short description or brand message
- CTA: "Explore" or "Learn More" (tertiary style)
**Design Rules:**
- Light background tile  
- Positioned text overlay (bottom-left)
- Slight border or shadow for definition
- Gap: 28px between tiles
**Mobile:** 1-column full-width  
**Desktop:** 2-column (1fr 1fr) gap 28px  
**Typography:** Label 11px uppercase; copy 13–14px  
**Interaction:** Hover slight scale or opacity on image  
**Source:** `/sections/range.html` (promo variations)

### Associative Trust / Logo Strip
**Purpose:** Reinforce legitimacy through brand partners (Coperni, Free People, etc.)  
**Business Goal:** Social proof and credibility  
**User Goal:** See known brands endorsing the product  
**Layout:**
- Light background section
- Centered title line
- Row of partner logos with dividers
- Optional: supporting text below
**Content:**
- Eyebrow (optional, "Loved by" or "Trusted by")
- Statement: "Free People favorite. Coperni chosen." (editable copy)
- Logo bar: 3–4 partner marks, centered, with | dividers
- Fine print (optional): "Sold at...", "Featured in..." (12.5px, muted)
**Design Rules:**
- Text-centered layout
- Logos: 18–24px clamp, 400 weight
- Borders on row (1px solid line, light)
- Even spacing (20px padding left/right per mark)
**Mobile:** Single column, logo names stack or wrap  
**Desktop:** Horizontal row, logos centered, max-width 720px centered  
**Typography:** Roboto 300/400, statement 20–30px, logo 18–24px  
**Spacing:** 56px padding section, 22px between mark and border  
**Design Variations:** Two versions depending on partner count  
**Source:** `/sections/assoc.html`

### Featured Article / Journal Section
**Purpose:** Drive traffic to content via featured article card  
**Business Goal:** Build audience, increase time-on-site  
**User Goal:** Discover brand stories and tips  
**Layout:**
- Article grid (usually 3 cards per row)
- Each card: image + category label + headline + excerpt + read more link
**Card Content:**
- Featured image (aspect ratio 4:3 or 3:4)
- Category label (11px monospace, uppercase, accent color)
- Headline (21px, 400 weight, dark)
- Excerpt (13–14px, soft, max 26ch, 2–3 lines)
- "Read More →" link (12px, accent color, tertiary style)
**Design Rules:**
- 28px gap between cards
- Light border or shadow on card
- High contrast headline
- Italic or soft styling on excerpt
**Mobile:** 1-column full-width stack  
**Desktop:** 3-column grid (64px padding)  
**Typography:** Roboto, category (11px monospace), headline (21px), excerpt (14px)  
**Spacing:** 64px padding, 28px card gap, 20px internal card padding  
**Hover:** Image brightness or scale, headline underline  
**Source:** Integrated in home page sections

### Trust Badges & Guarantees Strip
**Purpose:** Reduce purchase anxiety with guarantees and trust signals  
**Business Goal:** Overcome objections, increase conversion  
**User Goal:** Feel confident in purchase decision  
**Content:**
- Multiple benefit/guarantee rows
- Icons (checkmark, shield, etc., optional)
- Short headline + description per item
- Possible: "30-Day Trial", "90-Day Warranty", "Easy Returns"
**Design Rules:**
- 2–3 columns depending on number of guarantees
- Centered alignment
- Icons left-aligned or top, text right-aligned
- Light dividers between items
**Mobile:** Stack single column  
**Desktop:** 2–3 column grid  
**Typography:** Headline 14–15px bold, description 13px soft  
**Spacing:** 56px padding, 20px gap between items  
**Design Variations:** Can appear as cards with bg, or text-only rows  
**Placement:** Typically just before/after checkout CTA or guarantee section

### Navigation / Sticky Header
**Purpose:** Main navigation and shopping cart access  
**Business Goal:** Enable product discovery and checkout  
**User Goal:** Browse categories and access cart  
**Desktop Layout:**
- Left: Logo (centered in mobile/tablet)
- Center: Category links (Grippy Footwear, Apparel, Collaborations, Journal, About Us)
- Right: Account, Cart
**Mobile Layout:**
- Left: Hamburger menu (categories)
- Center: Logo
- Right: Cart icon
**Behavior:**
- Sticky on scroll (stays at top)
- Hairline appears on scroll > 8px (1px solid var(--br-line))
- Cart badge: Dot (var(--br-accent)) visible only when items > 0
- Hamburger: Opens drawer/modal, closes on selection
**Design Rules:**
- No background until scroll (transparent)
- Roboto 600 weight for nav text
- Links: 13–14px
- Badge dot: 8px radius, positioned top-right on cart icon
**Mobile:** Full-width, hamburger priority  
**Desktop:** Full horizontal nav, centered logo  
**Typography:** Roboto 600, 13–14px nav text  
**Spacing:** Default 16px internal padding, 8px gap between nav items  
**Sticky Behavior:** position: fixed; top: 0; z-index: 40 (below modals, above content)  
**Source:** `/sections/hero.html` (header integrated)

### Footer
**Purpose:** Secondary navigation, legal, and sitewide links  
**Business Goal:** SEO, navigation completeness, legal compliance  
**User Goal:** Find links, policies, contact info  
**Content:**
- Multiple link columns (3–4)
  - Customer Service (Returns, Sizing, FAQ)
  - About (Brand story, Careers, Press)
  - Legal (Privacy, Terms, Accessibility)
  - Social (Instagram, TikTok, etc.)
- Newsletter signup (optional)
- Copyright notice + year
- Social icons (hover states)
**Design Rules:**
- Dark background (typically var(--m-dark))
- Light text (white, muted white for secondary)
- Column links: 13px, soft light
- Section headers: 14px bold
- Copyright: 11px, muted
**Mobile:** Single column stack, full width  
**Desktop:** 4-column grid (1fr 1fr 1fr 1fr), 56px padding  
**Typography:** Roboto, links 13px, headers 14px 600, copyright 11px  
**Spacing:** 56px padding, 28px gap between columns, 20px gap within column  
**Link Styling:** Text color only, underline on hover, accent on active  
**Newsletter Integration:** Horizontal form, full width, 40px height input + button  
**Source:** Common across all pages, not a dedicated section file

### Responsive Behavior Summary

**Mobile (< 768px):**
- Single-column layout for all sections
- Full-width images and cards
- Hamburger navigation replaces horizontal nav
- Sticky Add to Cart: fixed bottom
- Font sizes reduce via `clamp()` function
- Padding: 24px sides instead of 56px+
- Tap targets: 44×44px minimum

**Desktop (≥ 768px):**
- Multi-column grids (2–4 columns per section)
- Side-by-side splits and layouts
- Horizontal navigation bar
- Hover states active (1.02x scale, underlines, opacity)
- Font sizes at full clamp() max
- Padding: 56–96px depending on section
- Proper text width (max-widths on long-form content)

---

## Page Section Architecture

### Home Page (16 Sections)
1. Ticker
2. Header
3. Hero
4. Pillar strip
5. Split 1 ("Never slip in chair pose")
6. Product grid (4 cards)
7. Promo tiles (2 side-by-side)
8. **Sock Math** section
9. Split 2 ("Progress, built from the ground up")
10. Disciplines (3 cards)
11. Split 3 ("Never loses grip")
12. Reviews (6 curated)
13. Coperni collab
14. Journal/Articles (3)
15. Guarantee
16. Newsletter → FAQ → Social → Footer

### PDP (Product Detail Page, 10 Sections)
1. Ticker
2. Header
3. PDP main (gallery + buy box + tabs)
4. Pillar strip
5. Benefit grid (6 cards, product-specific)
6. Split — fabric/construction ("Safely push harder…")
7. Sock Math condensed ("One pair. Done")
8. Reviews (Judge.me grid)
9. Guarantee
10. Product rail ("Pairs with your kit") → Footer

### Collection Page (9 Sections)
1. Ticker
2. Header
3. Collection hero ("Your body moves…")
4. Variant grid (all products, filter tabs)
5. Pillar strip
6. Benefit grid (3 cards, category-specific)
7. Disciplines (same 3 cards)
8. Split — category story ("The Pilates sock era…")
9. Testimonial (best review for this collection) → Footer

---

## Interaction & Animation Rules

### Animation Principles
- All animations gate on `@media (prefers-reduced-motion: no-preference)`
- Final state must be visible without animation
- Prefer opacity crossfades over complex transforms
- Smooth ease-out timing (240ms–320ms)

### Common Timings
- Opacity crossfade: 320ms ease
- Image scale hover: 320ms ease-out
- Transition height (accordions): 200ms
- Toggle cross-fade: 240ms ease-out
- Hero eyebrow rotation: 3.5s cycle
- Ticker slide: 4s interval

### Keyboard & Touch
- Tab navigation: all interactive elements must be keyboard-accessible
- Touch targets: minimum 44×44px
- Pinch/zoom: supported on PDP gallery
- Keyboard arrows: ←/→ for image galleries
- Mobile hamburger: menu on click, closes on selection or escape

### Hover States
- Links: text-decoration underline or color shift
- Buttons: slight background or opacity shift
- Product cards: image scale 1.02x + caption underline draw
- Variant cards: all hover effects as listed

---

## Accessibility & Mobile

### Responsive Behavior
- **Mobile breakpoint:** 768px and below
- **Desktop:** 768px+
- Stacking: Single column on mobile unless specified
- Touch targets: 44×44px minimum
- Font sizes: Readable at 375px viewport width

### Mobile-Specific Components
- Hamburger navigation (replaces horizontal nav)
- Sticky Add to Cart button on PDP
- Full-width product cards
- Vertical stacking of all 2-column sections
- Simplified filter interface (drawer or modal)

### Accessibility Requirements
- All interactive elements: keyboard-navigable
- All images: descriptive alt text
- Color not sole information carrier (star ratings, badges)
- Focus indicators: visible (outline or highlight)
- ARIA attributes where needed (aria-pressed, aria-expanded)
- Form labels: associated with inputs

---

## Component Placement Rules

### What Goes Next to What
- **Ticker** → Always header-top
- **Hero** → Directly below header
- **Pillar strip** → After hero (all pages)
- **Split 1** → After pillar strip (home only)
- **Product grid** → After splits or pillars
- **Sock Math** → After product grid (home) or early on PDP
- **Reviews** → Near bottom (builds trust before checkout)
- **Guarantee** → Last content section before footer (reduces friction at decision point)

### What Should Never Appear Together
- Two different slogans in same section (one anchor per section)
- Multiple benefit grids on same page (consolidate into one per section)
- Sock Math + other comparison sections (Math is the only comparison)
- Hamburger + horizontal nav (choose one per viewport)

---

## Design System Constraints

### Fixed & Immutable
- **50/50 split CSS:** Do NOT modify sizing proportions
- **Button styling:** No drop shadows, gradients, or rounded corners
- **Color palette:** Exact HEX values as specified above
- **Typography hierarchy:** Roboto 300–700 weight range only

### Version Management
- Increment version on every new file (v1, v2, v3)
- Don't overwrite existing versions
- Keep multiple versions if design variations exist

---

## HTML Component Locations

All reusable components have source HTML in the `/sections/` directory. Reference below:

**Named Section Files (Use These):**
- `hero.html` — Main hero section with eyebrow rotator
- `manifesto.html`, `manifesto2.html` — Brand manifesto with rotating statements
- `problem.html`, `problem2.html` — Problem statement / pain point agitation
- `founder-letter.html` — Founder communication section
- `founder2.html` — Founder story variant
- `sock-math.html` — Sock Math comparison section
- `split-section.html`, `split-section2.html`, `split-section3.html` — 50/50 editorial splits
- `disciplines.html` — Discipline/workout type selector (Barre, Reformer, Megaformer)
- `variants.html` — Product variant selector (Closed/Open Sole + color picker)
- `range.html` — Product grid / range display
- `testimonial.html` — Single customer testimonial with proof
- `credibility.html` — Partner logos and brand associations
- `closing-statement.html` — Final CTA section before footer
- `assoc.html` — Trust badges and associated brands strip

**Numbered Section Files (Study Reference, Not for Production):**
- `01-section.html` through `29-section.html` — Design study variations and component tests
- These are design exploration files showing current vs. matured treatments
- Do NOT use these for production builds; use named sections above

**Legacy/Reference Files:**
- `/barreletics-design-review/Barreletics_Handoff.md` — Last known handoff notes
- `Barreletics_v28_1_BASE.html` — Approved home page reference build
- `/files/` directory — v24 and prior versions (legacy, reference only)

**How to Use This Index:**
1. For building a new section, open the corresponding `.html` file in `/sections/`
2. Copy the relevant component HTML and CSS
3. Adapt content/copy while preserving all class names and design structure
4. Refer to this document for specifications and constraints
5. Test on mobile (< 768px) and desktop (≥ 768px) before deployment

---

## Version & Change Log

**Latest Version:** Component Library documented July 2026  
**Source:** Migration from in-repository HTML studies and design specs  
**Status:** Authoritative single source of truth  
**Last Updated:** 2026-07-12

**What Changed in This Version:**
- Added comprehensive documentation for all named section components
- Documented founder, problem, manifesto, and closing statement sections
- Added detailed mobile/desktop behavioral specs
- Included all typography, spacing, and design rules extracted from HTML sources
- Added section placement rules and component interdependencies
- Created authoritative HTML source index

---

**This document is the authoritative source for all component specifications, page layouts, design rules, and interactions. Use this and the referenced HTML files when building any new pages or sections to ensure consistency across Barreletics.**
