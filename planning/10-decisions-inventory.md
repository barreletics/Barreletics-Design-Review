# Decisions Inventory — Source Extraction

**Purpose:** Raw inventory of every decision, rationale, superseded decision, implementation decision, naming decision, and business rule found across the repository.  
**Status:** PLANNING ONLY — source material for docs/10-DECISIONS.md  
**Extracted:** 2026-07-13

---

## DESIGN DECISIONS

### D-001: Font — Roboto Only
- **Decision:** "Font: Roboto only (300–700), no Josefin Sans"
- **Rationale:** Single-family type system for consistency; Josefin Sans was previously used and explicitly removed.
- **Supersedes:** Previous use of Josefin Sans
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7), docs/03-DESIGN-SYSTEM.md (Typography section), docs/04-COMPONENT-LIBRARY.md (line 11)
- **Category:** DESIGN

### D-002: JetBrains Mono for Technical Eyebrows (Matured Direction Only)
- **Decision:** JetBrains Mono reserved for technical eyebrows and grip-spec captions on the matured direction only.
- **Rationale:** Differentiation between editorial copy and technical labels.
- **Supersedes:** N/A (addition to the system)
- **Source:** docs/03-DESIGN-SYSTEM.md (Typography section)
- **Category:** DESIGN

### D-003: Button Radius — 0px (Square)
- **Decision:** "Buttons: Square (radius 0), black #050505" — No drop shadows, no gradients, no rounded corners.
- **Rationale:** Matches Shopify "button_style":"square" setting; maintains clean, editorial look.
- **Supersedes:** Live PDP mock uses 6px radius (CONFLICT: docs/05-PDP-ARCHITECTURE.md line 46 uses border-radius: 6px)
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7), docs/03-DESIGN-SYSTEM.md (Buttons), docs/04-COMPONENT-LIBRARY.md (line 37)
- **Category:** DESIGN

### D-004: Coral Accent Restraint — Cart Badge ONLY
- **Decision:** "--br-accent (#f97250) — cart badge ONLY. Do not paint CTAs, headings, or section backgrounds in --br-accent."
- **Rationale:** "The coral exists for the cart badge and nothing else. This is the single biggest correction the matured direction makes to the live site."
- **Supersedes:** Live site uses coral more liberally (on CTAs, section backgrounds)
- **Source:** docs/03-DESIGN-SYSTEM.md (Color section), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS :root comments)
- **Category:** DESIGN

### D-005: Coral Eyebrow Usage Exception
- **Decision:** Eyebrows use coral (#f97250) ONLY on white/light backgrounds. On dark sections use WHITE rgba(255,255,255,0.7).
- **Rationale:** Maintains visibility contrast while keeping coral controlled.
- **Supersedes:** N/A
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7), docs/04-COMPONENT-LIBRARY.md (lines 13-14)
- **Category:** DESIGN

### D-006: 50/50 Split Sizing — CANONICAL, DO NOT CHANGE
- **Decision:** Fixed height: 420px (not min-height), overflow: hidden, padding: 80px 72px on copy side, slogan: clamp(28px, 3.2vw, 42px) with min-height: 0. Mobile: height: auto.
- **Rationale:** Reference: v18 "Never slip in chair pose" section. Established through iteration.
- **Supersedes:** Earlier split sizing attempts
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7), docs/04-COMPONENT-LIBRARY.md (line 143: "Fixed through iteration — DO NOT change split CSS proportions")
- **Category:** DESIGN

### D-007: Color Palette — Exact Values
- **Decision:** bg=#fff, text=#050505, accent=#f97250, star=#fbc02d, alt-bg=#f9f9f9, text-soft=#4a4a4a, text-mute=#8a8a8a, line=#e6e6e6
- **Rationale:** Calibrated to live site; cream/plum palette in Shopify settings_data.json is dead code.
- **Supersedes:** Unused cream/plum palette in settings_data.json
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7), docs/03-DESIGN-SYSTEM.md (Color table), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS :root)
- **Category:** DESIGN

### D-008: Sale Price — Ink Bold, Not Red
- **Decision:** "--br-sale: var(--br-text); sale price is just ink-bold, not red"
- **Rationale:** Editorial restraint; keeps visual hierarchy clean.
- **Supersedes:** Standard e-commerce red sale pricing
- **Source:** docs/03-DESIGN-SYSTEM.md (Color section)
- **Category:** DESIGN

### D-009: Limited Edition Chip — Blue (#3a8de8)
- **Decision:** "Limited Edition" chip uses --br-le (#3a8de8) text on --br-le-bg (#eaf3fc) background.
- **Rationale:** Differentiation from accent coral; informational rather than action-oriented.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (Color section)
- **Category:** DESIGN

### D-010: Card Border Radius — None by Default
- **Decision:** Cards have no radius by default. Where matured direction uses radius (rare), it is 2px or 4px — never 12–16px pill-card look.
- **Rationale:** Matured editorial aesthetic; rejected live site's rounded cards.
- **Supersedes:** Live site pill-card style (12-16px radius)
- **Source:** docs/03-DESIGN-SYSTEM.md (Hairlines & radii), docs/04-COMPONENT-LIBRARY.md (lines 31-33)
- **Category:** DESIGN

### D-011: No Black/Orange Color Scheme
- **Decision:** "Critical: NO orange/black. Warm or neutral only."
- **Rationale:** Color compliance direction from implementation matrix.
- **Supersedes:** Earlier design explorations using black/orange
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md
- **Category:** DESIGN

### D-012: Implementation Roadmap Colors
- **Decision:** "Colors: Warm (#eae5da) or white. Accent: Terracotta (#c45c3f). NO black/orange."
- **Rationale:** Warm, premium feel; terracotta is a softer accent vs orange.
- **Supersedes:** N/A (implementation direction)
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md (Design System section)
- **Category:** DESIGN

### D-013: Animation — Reduced Motion Gate
- **Decision:** "All animations gate on @media (prefers-reduced-motion: no-preference). Final state must be visible without animation."
- **Rationale:** Accessibility compliance.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 977-978), docs/03-DESIGN-SYSTEM.md (Interactions table)
- **Category:** DESIGN

### D-014: Touch Targets — 44×44px Minimum
- **Decision:** All interactive elements must have a minimum 44×44px touch target.
- **Rationale:** Accessibility and mobile usability standard.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 1011-1012)
- **Category:** DESIGN

### D-015: Mobile Breakpoint — 768px
- **Decision:** Mobile breakpoint: 768px and below. Desktop: 768px+.
- **Rationale:** Standard responsive breakpoint.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1008-1009)
- **Category:** DESIGN

### D-016: Spacing Scale
- **Decision:** 4/8/12/16/24/32/48/64/96/128px scale (--sp-1 through --sp-10).
- **Rationale:** Consistent spacing system.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (Spacing scale), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS :root)
- **Category:** DESIGN

### D-017: Typography Ramp
- **Decision:** Eyebrow 12px → body-sm 14px → body 16px → h6/body-lg 18px → h5 22px → h4 28px → h3 36px → h2 44px → h1 56px → display 72px.
- **Rationale:** Single cohesive ramp; mobile uses clamp() on hero/display only.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (Typography table)
- **Category:** DESIGN

### D-018: Eyebrow Styling — Consistent Spec
- **Decision:** 12px / font-weight 700 / letter-spacing 0.14em / uppercase (per Component Library). OR: 12px / 600 / 0.08em / uppercase (per Design System).
- **Rationale:** N/A
- **Supersedes:** CONFLICT between sources — Component Library says 0.14em/700, Design System says 0.08em/600. Needs resolution.
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 12) vs docs/03-DESIGN-SYSTEM.md (Typography table) vs barreletics-design-review/Barreletics_Research_Bible.md (0.14em/700)
- **Category:** DESIGN

### D-019: Ticker — 3 Slides, 4s Interval
- **Decision:** Announcement ticker is a 3-slide auto-rotator, 4s interval, opacity crossfade 320ms ease. Pause on hover.
- **Rationale:** N/A (established behavior)
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 63), docs/03-DESIGN-SYSTEM.md (Interactions table)
- **Category:** DESIGN

### D-020: Hero Eyebrow Rotation — 3.5s Cycle, 5 Messages
- **Decision:** Rotating eyebrow with 3.5s cycle containing 5 messages.
- **Rationale:** Brand messaging rotation for hero visibility.
- **Supersedes:** N/A
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 4), docs/04-COMPONENT-LIBRARY.md (lines 109-114), docs/02-BRAND-SYSTEM.md (Section 2)
- **Category:** DESIGN

### D-021: Product Card — No Swatches, Each Color = Own Card
- **Decision:** "Each color = its own card with image, color name, price, Quick Add button. NEVER use swatches on one card."
- **Rationale:** Direct add-to-cart from grid without PDP redirect.
- **Supersedes:** Standard e-commerce single-card-with-swatches pattern
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 188-192)
- **Category:** DESIGN

### D-022: Reviews — Load More (Not Full Pagination)
- **Decision:** "Load more" appends next 6 reviews per click. No full pagination.
- **Rationale:** Keep page lightweight while enabling browsing.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 268), docs/03-DESIGN-SYSTEM.md (Interactions table)
- **Category:** DESIGN

### D-023: Collection Filter — Inline Chips, Not Sidebar
- **Decision:** Filter row uses inline chips, not sidebar. Multi-select within a facet, exclusive between facets. URL-syncs via query params.
- **Rationale:** Reduce friction in product discovery; mobile-friendly.
- **Supersedes:** Sidebar filter pattern
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 288-293), docs/03-DESIGN-SYSTEM.md (Interactions table)
- **Category:** DESIGN

### D-024: PDP Gallery — Sticky Buy Box
- **Decision:** Sticky buy box on right. Image-stack left. Gallery is sticky (position: sticky; top: 64px).
- **Rationale:** Maintain conversion flow, reduce friction; buy box always visible while browsing gallery.
- **Supersedes:** N/A
- **Source:** docs/05-PDP-ARCHITECTURE.md (line 35: "position: sticky; top: 64px"), docs/03-DESIGN-SYSTEM.md (PDP section order)
- **Category:** DESIGN

### D-025: PDP Accordion — One Open at a Time
- **Decision:** Accordion sections: one open at a time, 200ms height transition.
- **Rationale:** Organize information compactly without overwhelming.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 251-252), docs/03-DESIGN-SYSTEM.md (Interactions table)
- **Category:** DESIGN

### D-026: Sock ⇄ Skin Toggle Timing
- **Decision:** Cross-fade between two image states + swap two stat figures. 240ms ease-out. State persists via aria-pressed.
- **Rationale:** Smooth, accessible interaction.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 170-175), docs/03-DESIGN-SYSTEM.md (Interactions table)
- **Category:** DESIGN

### D-027: Header — Sticky with Hairline on Scroll
- **Decision:** Header sticky on scroll. Adds 1px bottom hairline (--br-line) on scroll > 8px. No background until scroll. Cart badge dot (--br-accent) visible only when items > 0.
- **Rationale:** Clean header that gains definition on scroll; minimal cart indicator.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 80-82), docs/03-DESIGN-SYSTEM.md (Interactions table)
- **Category:** DESIGN

### D-028: No State Library Required
- **Decision:** "No app-level state library required." State handled by Shopify cart API, standard variant routing, URL query params, and local JS.
- **Rationale:** Shopify handles all persistent state; no need for React/Redux.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (State section)
- **Category:** IMPLEMENTATION

### D-029: Matured Direction — Final Choice
- **Decision:** "The team chose the matured editorial direction. Build that. The others are decision history."
- **Rationale:** v2-v11 explored cinematic, multi-tile, hybrid, Coperni-led, editorial, video hero variants. Matured editorial direction won.
- **Supersedes:** All Home v2-v11 variants; all pre-matured exploration files
- **Source:** docs/03-DESIGN-SYSTEM.md (Home page section)
- **Category:** DESIGN

### D-030: Section Count — Halved
- **Decision:** Section count was halved from original live site.
- **Rationale:** Audit determined live site had too many sections ("slogan soup"). Cut for editorial restraint.
- **Supersedes:** Original 20+ section live site homepage
- **Source:** docs/03-DESIGN-SYSTEM.md (Audit reference)
- **Category:** DESIGN

### D-031: Numbered Section Files — NOT for Production
- **Decision:** "01-section.html through 29-section.html — Design study variations and component tests. Do NOT use these for production builds; use named sections above."
- **Rationale:** Exploration files showing current vs. matured treatments; named section files are canonical.
- **Supersedes:** N/A (clarification)
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 1086-1089)
- **Category:** IMPLEMENTATION

### D-032: pg-tab-strip — Strip from Production
- **Decision:** "The pg-tab-strip at the top of most pages is a review aid. Strip it from production output."
- **Rationale:** Review-only navigation between mockups; not part of production site.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (line 97-99)
- **Category:** IMPLEMENTATION

### D-033: Tweaks Panel — Not for Production
- **Decision:** "The Tweaks panel (*-tweaks.jsx + tweaks-panel.jsx) is a preview-time controls panel for design review. It is not part of the production site."
- **Rationale:** Review tool only.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (lines 100-103)
- **Category:** IMPLEMENTATION

### D-034: Design Files Are Prototypes, Not Production Code
- **Decision:** "They are prototypes showing intended look, copy, layout, density, and behavior — not production code to copy directly."
- **Rationale:** Task is to recreate in Shopify Liquid using theme's established patterns; do not lift HTML wholesale.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (About the Design Files section)
- **Category:** IMPLEMENTATION

### D-035: Implementation Order
- **Decision:** 1. Tokens first → 2. Header + footer → 3. PDP → 4. Home → 5. Collection → 6. Articles + Blog → 7. Strip review chrome.
- **Rationale:** PDP is highest-revenue page; tokens must be established first for consistency.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (Suggested implementation order)
- **Category:** IMPLEMENTATION

### D-036: PDP Text Color — #1c1916 (Not #050505)
- **Decision:** PDP uses text color #1c1916 throughout (body, headings, buy box).
- **Rationale:** Slightly warmer ink tone for PDP specifically.
- **Supersedes:** Potential conflict with design system --br-text (#050505)
- **Source:** docs/05-PDP-ARCHITECTURE.md (CSS lines 24, 42-43)
- **Category:** DESIGN

### D-037: PDP CTA Button — Hover to Coral
- **Decision:** PDP primary CTA hovers from ink (#1c1916) to coral (#c45c3f).
- **Rationale:** N/A (established in PDP mock)
- **Supersedes:** Possible conflict with coral restraint rule (D-004)
- **Source:** docs/05-PDP-ARCHITECTURE.md (line 47)
- **Category:** DESIGN

### D-038: PDP Review Card — 12px Border Radius
- **Decision:** Review cards on PDP use border-radius: 12px.
- **Rationale:** N/A (established in PDP mock)
- **Supersedes:** Conflicts with D-010 (no radius by default, max 4px)
- **Source:** docs/05-PDP-ARCHITECTURE.md (line 67)
- **Category:** DESIGN

### D-039: PDP Gallery Hero — 8px Border Radius
- **Decision:** PDP gallery hero image uses border-radius: 8px.
- **Rationale:** N/A
- **Supersedes:** Conflicts with D-010 (no radius by default)
- **Source:** docs/05-PDP-ARCHITECTURE.md (line 36)
- **Category:** DESIGN

### D-040: PDP Color Swatches — Used on PDP
- **Decision:** PDP uses circular color swatches (23px diameter, 50% radius, 2px border, aria-selected state).
- **Rationale:** PDP is the appropriate place for swatches (vs. never on product cards).
- **Supersedes:** N/A (coexists with D-021 which bans swatches on CARDS only)
- **Source:** docs/05-PDP-ARCHITECTURE.md (lines 48-51)
- **Category:** DESIGN

### D-041: Max Width — 1320px (Matured) vs 1200px (PDP) vs 1400px (PDP Hero)
- **Decision:** Multiple max-widths: page container 1320px (matured CSS), PDP sections 1200px, PDP hero 1400px.
- **Rationale:** PDP hero needs more breathing room; inner sections are tighter.
- **Supersedes:** N/A (different contexts)
- **Source:** docs/06-HOMEPAGE-ARCHITECTURE.md (au-doc: 1320px), docs/05-PDP-ARCHITECTURE.md (lines 53-54: 1200px, line 153: 1400px)
- **Category:** DESIGN

---

## BRAND DECISIONS

### B-001: "Performance Skin" — Not a Sock
- **Decision:** "Product: $74 'performance skin' — NOT a sock. Never call it a sock."
- **Rationale:** Category creation; differentiation from grip socks.
- **Supersedes:** Any copy referring to product as a "sock"
- **Source:** docs/02-BRAND-SYSTEM.md (Section 4), barreletics-design-review/Barreletics_Research_Bible.md (Section 1)
- **Category:** BRAND

### B-002: Voice Priority Order
- **Decision:** "Voice priority: Safety + grip + 'replaces socks' BEFORE lifestyle."
- **Rationale:** Safety and function-first messaging before lifestyle/fashion positioning.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 4)
- **Category:** BRAND

### B-003: Brand Voice — Confident Instructor Tone
- **Decision:** "Confident instructor who's seen it all. Direct, warm, a little dry. Never hype-y. Short sentences. Real benefits. Let reviews and the 30-day trial do the convincing."
- **Rationale:** Premium, calm, confident positioning.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 3), manychat-kb/12-brand-voice-and-taglines.md
- **Category:** BRAND

### B-004: One Emoji Max — None on Serious Messages
- **Decision:** "Premium, calm, confident. One emoji max or none at all on serious messages."
- **Rationale:** Premium brand positioning; avoids cheapening communication.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 3), manychat-kb/12-brand-voice-and-taglines.md
- **Category:** BRAND

### B-005: Each Section Anchored by a Slogan
- **Decision:** "Each section is anchored by a slogan. The rotating hero eyebrow slogans are the best lines in the brand — they should be the organizing principle for every section on every page."
- **Rationale:** Slogans aren't decoration; they're section headlines. Structural organizing principle.
- **Supersedes:** Live site's "slogan soup" approach
- **Source:** docs/02-BRAND-SYSTEM.md (Section 1)
- **Category:** BRAND

### B-006: Benefits Distributed, Not Lumped
- **Decision:** "No standalone 'benefit grid' section on the home page. Instead, each section carries its own relevant benefit messaging. The benefit grid lives on PDP and Collection pages with context-specific copy."
- **Rationale:** Avoids repetitive benefit walls; contextualizes benefits within storytelling.
- **Supersedes:** Standalone benefit grid on homepage (live site pattern)
- **Source:** docs/02-BRAND-SYSTEM.md (Section 1)
- **Category:** BRAND

### B-007: "Trusted by 1,000's" — Placement Rule
- **Decision:** "'Trusted by 1,000's of instructors' appears in the stars/trusted line of every 50/50 split hero, not as a section headline."
- **Rationale:** Supporting credibility line, not a primary headline.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 1)
- **Category:** BRAND

### B-008: Double Failure Concept — Use on PDP
- **Decision:** "'Your foot moves in the sock. The sock moves on the floor. Now neither does.' — Use on PDP."
- **Rationale:** Core differentiator concept; placed on highest-conversion page.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 4), barreletics-design-review/Barreletics_Research_Bible.md (Section 1)
- **Category:** BRAND

### B-009: Words to Avoid
- **Decision:** Never use: "Cheap," "Just socks," generic hype ("amazing!!!"), medical promises, emoji spam.
- **Rationale:** Brand protection; premium positioning.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 5), manychat-kb/12-brand-voice-and-taglines.md
- **Category:** BRAND

### B-010: Hashtag
- **Decision:** Official hashtag: #letusknockyoursocksoff
- **Rationale:** Brand memorability; playful-but-premium tone.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 3), barreletics-design-review/Barreletics_Research_Bible.md (Section 4)
- **Category:** BRAND

### B-011: Hero Body Copy — Approved
- **Decision:** "Not a sock. A performance skin. 360° grip through every pose, transition, class — on the mat or off it."
- **Rationale:** Core positioning statement.
- **Supersedes:** N/A
- **Source:** docs/02-BRAND-SYSTEM.md (Section 4), barreletics-design-review/Barreletics_Research_Bible.md (Section 6)
- **Category:** BRAND

### B-012: Coperni Association — Restrained, Not Scattered
- **Decision:** "Coperni + Free People association strip — Light, restrained logo lockup with a single line of credibility copy. Do not scatter collab tiles like v1."
- **Rationale:** Editorial restraint; premium association without visual noise.
- **Supersedes:** v1 scattered collab tiles approach
- **Source:** docs/03-DESIGN-SYSTEM.md (Home section order, item 7)
- **Category:** BRAND

### B-013: Sock Math — Single Editorial Slogan (Not Stacked Claims)
- **Decision:** "Sock-math — Dark band, single editorial slogan with one rotating proof line. Not the stacked-claim soup of the live site."
- **Rationale:** Editorial clarity; live site's stacked claims diluted impact.
- **Supersedes:** Live site's stacked-claim sock math section
- **Source:** docs/03-DESIGN-SYSTEM.md (Home section order, item 8)
- **Category:** BRAND

### B-014: Testimonial — One Editorial Proof (Not Dense Tile Wall)
- **Decision:** "Testimonial — One editorial proof with citation and a supporting stat row. Not a dense tile wall."
- **Rationale:** Focus attention on one compelling story.
- **Supersedes:** Dense testimonial tile wall (live site)
- **Source:** docs/03-DESIGN-SYSTEM.md (Home section order, item 9)
- **Category:** BRAND

### B-015: PDP Reviews — Resist Full Wall
- **Decision:** "Reviews summary + 3 selected quotes — Plus a single 'read all reviews' link. Resist the temptation to ship a full reviews wall on the PDP."
- **Rationale:** Curated social proof is more persuasive than a wall of reviews.
- **Supersedes:** Full reviews wall on PDP
- **Source:** docs/03-DESIGN-SYSTEM.md (PDP section order, item 8)
- **Category:** BRAND

### B-016: "Sock vs. Skin" — Editorial, Not Table
- **Decision:** "'Sock vs. skin' comparison — Editorial 2-col, not a table of red Xs and green checks."
- **Rationale:** Premium editorial treatment vs. generic comparison table.
- **Supersedes:** Standard red-X/green-check comparison tables
- **Source:** docs/03-DESIGN-SYSTEM.md (PDP section order, item 6)
- **Category:** BRAND

---

## NAMING DECISIONS

### N-001: "Blog" → "Journal"
- **Decision:** "'Blog' → 'Journal' everywhere"
- **Rationale:** Premium brand positioning; "Journal" feels more elevated.
- **Supersedes:** "Blog" terminology
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7)
- **Category:** NAMING

### N-002: Product Name — Design System vs Production
- **Decision:** Design system uses "Studio Performance Skin — [Sole Type]". Production uses "Best Grippy Shoes for Barre, Pilates & Yoga — [Sole Type]".
- **Rationale:** Design system is FUTURE state (brand-appropriate); production is CURRENT (SEO-optimized).
- **Supersedes:** Production name is current; design system name is future direction.
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Product 1 header, Conflicts Register)
- **Category:** NAMING

### N-003: Color Names — Design System vs Production
- **Decision:** Design system: "Onyx" (maps to Black), "Stone" (maps to LightGrey). Others TBD. Production: Black, LightGrey, DarkGrey, Blue, etc.
- **Rationale:** Design system uses elevated naming; production uses literal color names.
- **Supersedes:** Design system is FUTURE; production is CURRENT.
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Conflicts Register), docs/05-PDP-ARCHITECTURE.md (lines 201, 205-207)
- **Category:** NAMING

### N-004: Product Category Terms
- **Decision:** Categories: "Grippy Footwear" (performance skin), "In-Studio Grip" (studio use), "Outdoor" (water shoes), "Apparel", "Collaborations".
- **Rationale:** Shopify collection/navigation structure.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (product category fields)
- **Category:** NAMING

### N-005: Navigation Labels
- **Decision:** Nav links: "Grippy Footwear, Apparel, Collaborations, Journal, About Us"
- **Rationale:** Clear categorization with "Journal" (not "Blog").
- **Supersedes:** Any nav using "Blog"
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 77)
- **Category:** NAMING

### N-006: "Performance Skin" (Not "Grip Shoe")
- **Decision:** Primary product descriptor is "performance skin" — though SEO title uses "Grippy Shoes."
- **Rationale:** Brand differentiation in body copy while maintaining SEO in titles.
- **Supersedes:** N/A (dual usage: SEO vs brand)
- **Source:** barreletics-design-review/Barreletics_Research_Bible.md (Section 1), docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** NAMING

---

## PRODUCT DECISIONS

### P-001: Price — $74 Standard, $78 LE Colors, $115 Coperni
- **Decision:** Standard: $74. Limited Edition colors (Turquoise, Copper Swirl, Purple): $78. Coperni: $115. Yoga Tight: $89 (sale) / $129 (compare-at).
- **Rationale:** Premium pricing justified by longevity vs. grip sock replacement cost.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md, manychat-kb/04-pricing.md
- **Category:** PRODUCT

### P-002: Sizing — M and L Only
- **Decision:** Two sizes only: Medium (W 5.5–7.5) and Large (W 8–11 / M up to 10.5). No small size.
- **Rationale:** "No small size — the material stretches and conforms to your foot."
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md, manychat-kb/03-sizing-chart.md
- **Category:** PRODUCT

### P-003: Open Sole vs Closed Sole — Same Performance
- **Decision:** "Both perform identically with the same grip and stability. The difference is feel and coverage."
- **Rationale:** Eliminates customer confusion about performance differences.
- **Supersedes:** N/A
- **Source:** manychat-kb/02-open-vs-closed-sole.md, docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** PRODUCT

### P-004: First-Time Buyer Recommendation
- **Decision:** "Most first-time buyers start with Open Sole — the barefoot feel is where they shine."
- **Rationale:** Open Sole showcases the product's signature barefoot feel.
- **Supersedes:** N/A
- **Source:** manychat-kb/02-open-vs-closed-sole.md
- **Category:** PRODUCT

### P-005: No Machine Washing
- **Decision:** Care: "Warm soapy water, air dry. No machine washing. No grip degradation."
- **Rationale:** Protects product longevity.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md, manychat-kb/06-care-and-cleaning.md
- **Category:** PRODUCT

### P-006: Made in USA — Every Pair
- **Decision:** All products made in USA.
- **Rationale:** Quality assurance, brand credibility signal.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md, barreletics-design-review/Barreletics_Research_Bible.md
- **Category:** PRODUCT

### P-007: No Direct Competitor
- **Decision:** "No direct competitor in the 'performance skin' category. Barreletics created and owns this category."
- **Rationale:** Category creation narrative; grip socks are indirect competitors only.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md, barreletics-design-review/Barreletics_Research_Bible.md (Section 5)
- **Category:** PRODUCT

### P-008: Grip Material — Not Silicone, Not Latex
- **Decision:** "Proprietary grip material (not silicone, not latex)."
- **Rationale:** Skin-safe, differentiator from grip socks which use silicone/latex.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md, barreletics-design-review/Barreletics_Research_Bible.md (Section 1)
- **Category:** PRODUCT

### P-009: Injection-Molded Sole
- **Decision:** Sole is injection-molded / structured (not printed dots on fabric).
- **Rationale:** Structural durability vs. grip socks' printed dots that wash off.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** PRODUCT

### P-010: Kids Size — Undocumented, Zero Inventory
- **Decision:** Water Shoes has Kids variants (6 SKUs) in Shopify at 0 inventory. Not mentioned in any site copy or size chart.
- **Rationale:** Likely discontinued or placeholder. Data quality flag.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Data Quality Flags)
- **Category:** PRODUCT

### P-011: "One Off Colors" — Draft Products at $82
- **Decision:** Two DRAFT products ("One Off Colors" Open/Closed) at $82.00 with unique colorways. Not visible.
- **Rationale:** Likely future special-release pricing tier.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Products Not on Live Storefront)
- **Category:** PRODUCT

---

## BUSINESS DECISIONS

### BZ-001: 30-Day Return Policy
- **Decision:** 30-day returns. Must be clean, like new, no outdoor wear, no sole damage. Return shipping: $7.95 deducted from refund.
- **Rationale:** Risk-free trial drives conversion; conditions prevent abuse.
- **Supersedes:** N/A
- **Source:** manychat-kb/07-returns-and-exchanges.md, docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** BUSINESS

### BZ-002: Free Exchanges
- **Decision:** "Free exchanges — we ship at no cost once we receive and inspect your return."
- **Rationale:** Reduces friction for size uncertainty; preferred over refunds.
- **Supersedes:** N/A
- **Source:** manychat-kb/07-returns-and-exchanges.md, docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** BUSINESS

### BZ-003: 90-Day Warranty
- **Decision:** 90-day warranty against manufacturing defects. Return of defective item not required in most cases.
- **Rationale:** Trust building; covers quality concerns.
- **Supersedes:** N/A
- **Source:** manychat-kb/07-returns-and-exchanges.md, docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** BUSINESS

### BZ-004: Shipping — Free Over $150
- **Decision:** Free shipping on orders over $150. $9.95 flat rate under $150.
- **Rationale:** Encourages multi-pair purchase (2 pairs = $148, nearly hits threshold).
- **Supersedes:** Previous $75 free-shipping threshold (being raised per docs/03-DESIGN-SYSTEM.md)
- **Source:** manychat-kb/04-pricing.md, docs/09-PRODUCT-KNOWLEDGE.md, manychat-kb/08-shipping.md
- **Category:** BUSINESS

### BZ-005: Free Shipping Threshold Change — $75 → $150
- **Decision:** "Free-shipping threshold is $150 site-wide (the live $75 is being raised)."
- **Rationale:** Business margin consideration; raised from $75.
- **Supersedes:** $75 free shipping threshold
- **Source:** docs/03-DESIGN-SYSTEM.md (PDP key copy rules)
- **Category:** BUSINESS

### BZ-006: Buy 2+ Save 15% (Code: SAVE15)
- **Decision:** Discount: Buy 2+ save 15%. Automatically applied at checkout.
- **Rationale:** Encourages multi-pair purchase; instructor market buys 2-3 pairs.
- **Supersedes:** N/A
- **Source:** manychat-kb/04-pricing.md, docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** BUSINESS

### BZ-007: Newsletter 10% Off First Order
- **Decision:** New customers get 10% off via newsletter signup.
- **Rationale:** List building + first-purchase incentive.
- **Supersedes:** N/A
- **Source:** manychat-kb/04-pricing.md
- **Category:** BUSINESS

### BZ-008: Shop Pay — 4 Installments of $18.50
- **Decision:** Shop Pay splits $74 into 4 interest-free payments.
- **Rationale:** Reduces price objection for $74 single purchase.
- **Supersedes:** N/A
- **Source:** manychat-kb/04-pricing.md, docs/09-PRODUCT-KNOWLEDGE.md
- **Category:** BUSINESS

### BZ-009: No Medical Promises
- **Decision:** "Cannot guarantee outcomes for specific medical conditions." No medical claims. Hand off sensitive medical questions to human team.
- **Rationale:** Legal compliance; liability avoidance.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md, manychat-kb/11-sensitive-and-medical.md, manychat-kb/14-escalation-and-handoff.md
- **Category:** BUSINESS

### BZ-010: AI Escalation Rules
- **Decision:** Hand off to human for: order status/tracking/refunds, wholesale/bulk/press, account access/payment data, complaints/disputes/legal, anything uncertain.
- **Rationale:** AI should not handle sensitive operations or unknowns.
- **Supersedes:** N/A
- **Source:** manychat-kb/14-escalation-and-handoff.md
- **Category:** BUSINESS

### BZ-011: No Personal Data Collection in DM
- **Decision:** "Never collect [personal data] in DM" — address, payment, account info requires handoff.
- **Rationale:** Security and compliance.
- **Supersedes:** N/A
- **Source:** manychat-kb/14-escalation-and-handoff.md
- **Category:** BUSINESS

### BZ-012: Lost Package Policy
- **Decision:** "Once tracking shows delivered, order considered fulfilled. Cannot issue refunds for packages shown as delivered."
- **Rationale:** Prevents delivery dispute abuse.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Shipping section)
- **Category:** BUSINESS

### BZ-013: International — Customer Covers Duties/Returns
- **Decision:** International customers responsible for duties, taxes, customs fees. Return/exchange shipping costs are customer's responsibility.
- **Rationale:** Standard international shipping policy.
- **Supersedes:** N/A
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Shipping section), manychat-kb/08-shipping.md
- **Category:** BUSINESS

### BZ-014: We Outgrew Grip Socks — Category Slogan (Not Primary H1)
- **Decision:** Add *We Outgrew Grip Socks.* as approved category-creation slogan. Primary hero H1 stays *The Pilates Sock Era Is Over*. *Studio Workouts and Footwear Will Never Be the Same* demoted to legacy/meta only.
- **Rationale:** Strongest north-star line for category break; "We" acceptable as evolution statement in mid-page band, not hero. Pilates Sock Era retains SEO + discipline specificity.
- **Supersedes:** N/A
- **Source:** planning/02-brand-system.md, Definitive-v16 Home mockup
- **Category:** BRAND

### BZ-015: Home Typography — Hybrid (Alo UI + Nike Display)
- **Decision:** Lock Hybrid type: **Manrope** for UI/body (Alo ≈ Avenir); **Barlow Condensed** weight 600, sentence case, for hero H1 and section statements (Nike Futura-condensed energy without ALL CAPS). Coperni keeps Syne + Cormorant. Do not use Roboto as primary Home face; no Fraunces/italic display serifs on Home.
- **Rationale:** Matches real Alo/Nike patterns; AI serif stacks felt generic.
- **Supersedes:** v49 Roboto-only default for Home marketing surfaces
- **Status:** SUPERSEDED by BZ-016 (kept as experiment — Definitive-v20.html retained)
- **Source:** Definitive-v20, barreletics-design-system skill
- **Category:** BRAND

### BZ-016: Home Typography — Jost + Helvetica Neue (Home Run)
- **Decision:** Lock Home type: **Helvetica Neue** for UI/body/nav; **Jost** weight 500–600, sentence case, tight line-height (~1.0–1.05) for hero H1 and major display statements (Knock Socks, Commit full-bleed, We Outgrew, section H2s). Slightly larger hero/statement scale. Coperni keeps Syne + Cormorant. No ALL CAPS display shout; no Fraunces/Cormorant on Home marketing.
- **Rationale:** Hybrid (Manrope + Barlow Condensed) was neat but not a home run — Barlow reads gym-flyer condensed; Jost carries Futura geometric DNA with studio-premium calm. Helvetica Neue is the real Nike/Alo web UI face.
- **Supersedes:** BZ-015 Hybrid for Home marketing surfaces. Keep all prior mocks (v16–v20, v19 type-lab) — do not delete.
- **Status:** SUPERSEDED by BZ-017 (kept as experiment — Definitive-v21.html retained)
- **Source:** Definitive-v21, barreletics-design-system skill
- **Category:** BRAND

### BZ-017: Home Typography — Roboto Craft (Lulu / On Precision)
- **Decision:** Lock Home type to **Roboto only** (weights 400 / 500 / 700). Elevate via tracking, hierarchy, and moderate scale — Lululemon / On-level precision, not bigger-for-bigger. Shop/UI quiet; Barreletics heat in slogans, rust, imagery, and a few stronger statement lines (700). Coperni keeps Syne + Cormorant. Keep warm neutrals + category punch (do not become Lulu).
- **Rationale:** Font-hopping (Fraunces/Syne/Cormorant Home, Barlow gym, Hybrid, Jost) was not a home run. Single-family craft matches premium athletic ecom (Lulu/On) while keeping Barreletics voice.
- **Supersedes:** BZ-016 for Home marketing surfaces. Keep all prior mocks (v16–v21, v19 type-lab) — do not delete.
- **Source:** Definitive-v22, barreletics-design-system skill
- **Category:** BRAND

### BZ-018: Home Copy OS — Master Slogan Inventory
- **Decision:** `planning/HOME-WORKING-ENTRY.md` is the Home start entry (sections build/refine/change + instructions). `planning/home-copy-v24.md` holds the deep slogan/copy inventory. Brand-copy + slogan-engine skills must point here. Agents must not require the owner to re-paste the inventory.
- **Rationale:** Owner repeatedly resurfaces the full live/approved slogan set; it belongs in repo OS, not chat.
- **Source:** Owner paste 2026-07-23 + live barreletics.com Home + WORKING v29
- **Category:** BRAND / OPERATIONAL

### BZ-019: Home Working Authority — Definitive-v28 → v29
- **Decision:** Working Home mock = `Barreletics Home - Definitive-WORKING.html` (**v29**). Same as v28 difference spine + optional quiet Knock Socks sub: *Safely push harder in every studio move.* v28 kept without sub for A/B. Next edits = **v30+**.
- **Rationale:** Owner: “20000% better” on v28; then asked for Knock Socks secondary (keep-or-drop).
- **Source:** Definitive-v28/v29, Compare-v24-v28, planning/home-copy-v24.md
- **Category:** BRAND

### BZ-020: Type Weight Roles (Roboto 400 / 500 / 700)
- **Decision:** Keep the **dual weight system** — do not make every H2 700.
  - **400** body / handles / quiet UI
  - **500** section & display titles (Shop, Reviews, FAQ, IG “Studio workouts…”, hero H1)
  - **700** statement heat only (We Outgrew, Never Loses, Knock Socks, Commit, Sock Math title) + CTAs / badges
- **Rationale:** Owner liked the lighter IG line vs heavier statement bands — that contrast is intentional. IG at 400 was leftover under-spec; lock IG at **500** (section), not 700.
- **Source:** barreletics-design-system skill · SEO v29 · Home WORKING craft
- **Category:** BRAND

### BZ-021: SEO Never Loses — Full-Bleed Barre Short Video
- **Decision:** SEO mid-page Never Loses uses **Barre Short Video** (`Barre_Short_Video_-nosound.mp4`) full-bleed ~**90vh** (`.lifestyle-break`), not the first-viewport hero. Hero stays still `IMG_2917`. Same clip as Home Never Loses proof.
- **Rationale:** Still hero = message/LCP; full-bleed video mid-page = grip proof without diluting Sock Era CTA.
- **Source:** SEO Definitive-v29 · owner 2026-07-24
- **Category:** BRAND

### BZ-022: Collection — No Closed/Open Sole Sections (tabs + FAQ only)
- **Decision:** Collection authority = `Definitive-v16`. Spine: **hero → value strip → variants**. Remove early `#explain` sole cards **and** late “Closed Sole or Open Sole” 50/50. Closed/Open via **grid tabs + FAQ** only. Hero may still name the choice.
- **Rationale:** Shop-first convert (matches SEO); sole explainer bands delayed/duplicated the grid without adding interaction.
- **Source:** Owner 2026-07-24 · Collection v16
- **Category:** BRAND

### BZ-023: Collection Hero — Media Fill Control (theme)
- **Decision:** Theme schema for Collection split hero must include **`media_fill`**: `inset` (default — matches mock) \| `column` (fills entire right 50%). Also `media_type` image\|video. Mock stays inset; merchant/Brian can switch to full-column fill without code change.
- **Rationale:** Owner wants full-half fill available at build time without changing the locked mock look now.
- **Source:** Owner 2026-07-24 · planning/COLLECTION-WORKING-ENTRY.md
- **Category:** BRAND / OPERATIONAL

---

## OPERATIONAL DECISIONS

### O-001: Document Status System
- **Decision:** Five statuses: STUB → BUILDING → PENDING REVIEW → APPROVED → SUPERSEDED. "No document becomes APPROVED without explicit ChatGPT approval."
- **Rationale:** Quality control; prevents premature "done" declaration.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md
- **Category:** OPERATIONAL

### O-002: Role Definitions
- **Decision:** CEO (Andrew): Assigns/approves/breaks ties. Lead Architect (ChatGPT): Designs specs/reviews/approves. Build Engineer (Cursor): Executes/commits/pushes.
- **Rationale:** Clear responsibility separation.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md
- **Category:** OPERATIONAL

### O-003: One Commit Per Deliverable
- **Decision:** "One commit per deliverable. The deliverable is the atomic unit, not the conversation."
- **Rationale:** Clean git history; traceability.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md
- **Category:** OPERATIONAL

### O-004: No Invention Rule
- **Decision:** "The Build Engineer builds from source material provided or independently verifiable. Never fabricate content."
- **Rationale:** Accuracy; prevents AI hallucination in brand content.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md (Rule 4)
- **Category:** OPERATIONAL

### O-005: No Unsupported Metrics
- **Decision:** "Never report counts, metrics, percentages, or statistics unless they are measured directly from the repository or source material. No estimates. No inferred counts. No approximations."
- **Rationale:** Accuracy enforcement.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md (Rule 2)
- **Category:** OPERATIONAL

### O-006: Correct, Don't Defend
- **Decision:** "If the Build Engineer discovers during self-audit that an earlier report was incorrect, immediately correct it before reporting completion. Do not defend. Do not justify. Simply correct."
- **Rationale:** Quality culture; no ego in corrections.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md (Rule 3)
- **Category:** OPERATIONAL

### O-007: Self-Audit Before Reporting
- **Decision:** "Every deliverable is self-audited against its Acceptance Criteria before reporting done."
- **Rationale:** Quality gate before review.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md (Rule 5)
- **Category:** OPERATIONAL

### O-008: Auto-Approve Categories
- **Decision:** "Auto-approve (no ChatGPT review): Status changes, structural edits, Shopify code, git operations, tooling, workflow docs."
- **Rationale:** Reduces bottleneck on non-creative work.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md (Approval Flow)
- **Category:** OPERATIONAL

### O-009: Context Between Sessions
- **Decision:** "Each session starts fresh from repository state. Git history, file contents, and this workflow persist. Prior conversation memory does not carry over unless transcripts are explicitly consulted."
- **Rationale:** Ensures consistency; no accumulated drift.
- **Supersedes:** N/A
- **Source:** WORKFLOW.md (Context Between Sessions)
- **Category:** OPERATIONAL

### O-010: Implementation Roadmap — Phase Structure
- **Decision:** KEEP 4 sections, REFACTOR 14 sections, CLARIFY 5 sections. 6-week sprint timeline.
- **Rationale:** Prioritized by effort level and decision readiness.
- **Supersedes:** N/A
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md
- **Category:** OPERATIONAL

### O-011: Section 01 Hero — Keep (Custom Blend)
- **Decision:** Keep Hero section with custom blend: add "See in action" button, use eyebrow from current. Build effort: Light.
- **Rationale:** Working well; minor enhancements only.
- **Supersedes:** N/A
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md (Phase 1)
- **Category:** OPERATIONAL

### O-012: Section 03 — Keep (Custom Blend, Retain Trusted Rating)
- **Decision:** Keep 50/50 Progress section with "Trusted by" rating from current.
- **Rationale:** Effective section; retain social proof element.
- **Supersedes:** N/A
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md (Phase 1)
- **Category:** OPERATIONAL

### O-013: Section 09 — Keep (Matured, No Changes)
- **Decision:** Keep "The Problem" section from matured direction. Build effort: None.
- **Rationale:** Already in final state.
- **Supersedes:** N/A
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md (Phase 1)
- **Category:** OPERATIONAL

### O-014: Section 17 — Keep (Current)
- **Decision:** Keep "Never Slip in Chair Pose" section from current. Build effort: Medium.
- **Rationale:** Strong performing section.
- **Supersedes:** N/A
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md (Phase 1)
- **Category:** OPERATIONAL

---

## IMPLEMENTATION DECISIONS

### I-001: Shopify Online Store 2.0 Assumed
- **Decision:** "The designs assume [Online Store 2.0]. If not, Home and Collection page templates need to be ported to OS 2.0 sections first."
- **Rationale:** Sections everywhere architecture required for the section-based design.
- **Supersedes:** N/A (pre-condition)
- **Source:** docs/03-DESIGN-SYSTEM.md (Questions for developer)
- **Category:** IMPLEMENTATION

### I-002: Recreate in Liquid, Not Copy HTML
- **Decision:** "Recreate these designs inside the existing Barreletics Shopify theme (Liquid sections, snippets, existing settings_data.json schema, current section-rendering API) using theme's established patterns. Do not lift the HTML wholesale."
- **Rationale:** Maintain theme architecture; design files are prototypes only.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (About the Design Files)
- **Category:** IMPLEMENTATION

### I-003: New Sections Need Editor-Friendly Schema
- **Decision:** "If a section in the design has no equivalent today, add a new Shopify section with editor-friendly schema (block types, settings) that mirrors the variations shown."
- **Rationale:** Maintains Shopify theme editor usability.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (About the Design Files)
- **Category:** IMPLEMENTATION

### I-004: Photography Is Placeholder
- **Decision:** "All photography is placeholder — pulled from barreletics.com/cdn/... or stand-in CDNs. The brand team will provide final art-directed photography per page before launch."
- **Rationale:** Design-first; photography is secondary to structure.
- **Supersedes:** N/A
- **Source:** docs/03-DESIGN-SYSTEM.md (Assets section)
- **Category:** IMPLEMENTATION

### I-005: Version Management — Increment, Don't Overwrite
- **Decision:** "Increment version on every new file (v1, v2, v3). Don't overwrite existing versions. Keep multiple versions if design variations exist."
- **Rationale:** Preserve design history and decision trail.
- **Supersedes:** N/A
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 1060-1062)
- **Category:** IMPLEMENTATION

### I-006: Structured Data / Schema.org
- **Decision:** PDP includes Product structured data with AggregateRating, Offer (price $74, InStock), Brand.
- **Rationale:** SEO/rich results.
- **Supersedes:** N/A
- **Source:** docs/05-PDP-ARCHITECTURE.md (lines 129-148, JSON-LD)
- **Category:** IMPLEMENTATION

### I-007: PDP H1 = Shopify Product Title (SEO)
- **Decision:** H1 on PDP is the Shopify product title ("Best Grippy Shoes for Barre, Pilates & Yoga") at 18px/600. Marketing headline below at 44px/700.
- **Rationale:** SEO in H1; brand messaging in visual headline.
- **Supersedes:** N/A
- **Source:** docs/05-PDP-ARCHITECTURE.md (lines 181-188)
- **Category:** IMPLEMENTATION

### I-008: PDP Hero Toggle — Closed/Open Sole
- **Decision:** PDP has a hero-toggle between Closed Sole and Open Sole views (data-active switching).
- **Rationale:** Single PDP serves both sole types.
- **Supersedes:** N/A
- **Source:** docs/05-PDP-ARCHITECTURE.md (lines 29-31)
- **Category:** IMPLEMENTATION

### I-009: Layout Max — 1200px Main Content
- **Decision:** Site layout: 1200px max, 32px gutters (desktop), 16px (mobile).
- **Rationale:** Standard content width for readability.
- **Supersedes:** N/A
- **Source:** IMPLEMENTATION-ROADMAP-Jul2026.md (Design System)
- **Category:** IMPLEMENTATION

---

## COMPONENT PLACEMENT RULES (Structural Decisions)

### CP-001: Ticker Always Top
- **Decision:** Ticker always appears at top of page, above header.
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 1034-1035)
- **Category:** DESIGN

### CP-002: Hero Directly Below Header
- **Decision:** Hero section directly below header on all pages.
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1036)
- **Category:** DESIGN

### CP-003: Pillar Strip After Hero (All Pages)
- **Decision:** Pillar strip appears after hero on all pages.
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1037)
- **Category:** DESIGN

### CP-004: Reviews Near Bottom
- **Decision:** Reviews section near bottom of page (builds trust before checkout).
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1041)
- **Category:** DESIGN

### CP-005: Guarantee — Last Before Footer
- **Decision:** Guarantee section is last content section before footer (reduces friction at decision point).
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1042)
- **Category:** DESIGN

### CP-006: Never — Two Slogans in Same Section
- **Decision:** "Two different slogans in same section" — never allowed. One anchor per section.
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1045)
- **Category:** DESIGN

### CP-007: Never — Multiple Benefit Grids on Same Page
- **Decision:** Never have multiple benefit grids on same page (consolidate into one per section).
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1046)
- **Category:** DESIGN

### CP-008: Never — Sock Math + Other Comparisons
- **Decision:** "Sock Math + other comparison sections" — never together. Math is the only comparison.
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1047)
- **Category:** DESIGN

### CP-009: Never — Hamburger + Horizontal Nav
- **Decision:** Never show hamburger and horizontal nav simultaneously. Choose one per viewport.
- **Source:** docs/04-COMPONENT-LIBRARY.md (line 1048)
- **Category:** DESIGN

---

## SOURCE CONFLICTS (Decisions Needing Resolution)

### CONFLICT-001: Button Radius — 0px vs 6px
- **Rule:** Design System says 0px (square). PDP mock uses 6px (border-radius: 6px on CTA).
- **Source A:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7) — 0px
- **Source B:** docs/05-PDP-ARCHITECTURE.md (line 46) — 6px
- **Resolution needed:** Which is canonical for PDP?

### CONFLICT-002: Eyebrow Letter-Spacing — 0.14em vs 0.08em
- **Rule A:** 0.14em / 700 weight (Research Bible + Component Library)
- **Rule B:** 0.08em / 600 weight (Design System + Homepage CSS)
- **Source A:** barreletics-design-review/Barreletics_Research_Bible.md (Section 7), docs/04-COMPONENT-LIBRARY.md (line 12)
- **Source B:** docs/03-DESIGN-SYSTEM.md (Typography table), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS)
- **Resolution needed:** Which spec is authoritative?

### CONFLICT-003: PDP Review Card Radius — 12px vs 0-4px Max
- **Rule A:** Design System says no radius by default; max 2-4px where matured direction uses it.
- **Rule B:** PDP mock uses 12px on review cards.
- **Source A:** docs/03-DESIGN-SYSTEM.md (Hairlines & radii)
- **Source B:** docs/05-PDP-ARCHITECTURE.md (line 67)
- **Resolution needed:** PDP exception or design system violation?

### CONFLICT-004: PDP Text Color — #1c1916 vs #050505
- **Rule A:** Design System --br-text = #050505
- **Rule B:** PDP uses #1c1916 (slightly warmer)
- **Source A:** docs/03-DESIGN-SYSTEM.md, docs/06-HOMEPAGE-ARCHITECTURE.md
- **Source B:** docs/05-PDP-ARCHITECTURE.md (CSS)
- **Resolution needed:** Is PDP intentionally divergent?

### CONFLICT-005: PDP CTA Hover — Coral vs Restraint Rule
- **Rule A:** Coral is cart-badge-only (D-004)
- **Rule B:** PDP CTA hovers to coral (#c45c3f)
- **Source A:** docs/03-DESIGN-SYSTEM.md (Color — accent discipline)
- **Source B:** docs/05-PDP-ARCHITECTURE.md (line 47)
- **Resolution needed:** Is PDP CTA an exception to coral restraint?

### CONFLICT-006: Color Naming — Current vs Future
- **Current Production:** Black, LightGrey, DarkGrey, Blue, etc.
- **Future Design System:** Onyx, Stone, (others TBD)
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Conflicts Register)
- **Resolution needed:** Timeline for migration

### CONFLICT-007: Product Title — SEO vs Brand
- **Current Production:** "Best Grippy Shoes for Barre, Pilates & Yoga — Closed Sole"
- **Future Design System:** "Studio Performance Skin — Closed Sole"
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Conflicts Register)
- **Resolution needed:** When does the switch happen?

### CONFLICT-008: Yoga Tight Price — $89 Only vs $89/$129
- **Shopify API:** Returns only $89
- **Live site display:** Shows $129 strikethrough with $89 sale price
- **Source:** docs/09-PRODUCT-KNOWLEDGE.md (Data Quality Flags)
- **Resolution needed:** Is compare-at price configured correctly in Shopify?

### CONFLICT-009: Implementation Roadmap vs Design System Colors
- **Roadmap:** "Warm (#eae5da) or white. Accent: Terracotta (#c45c3f). NO black/orange."
- **Design System:** bg=#ffffff, accent=#f97250 (coral, not terracotta), text=#050505 (nearly black)
- **Source A:** IMPLEMENTATION-ROADMAP-Jul2026.md
- **Source B:** docs/03-DESIGN-SYSTEM.md, docs/06-HOMEPAGE-ARCHITECTURE.md
- **Resolution needed:** Roadmap appears to be a later/divergent decision from the design system tokens.

### CONFLICT-010: Free Shipping Threshold — $75 vs $150
- **Current live site:** $75 (per docs/03-DESIGN-SYSTEM.md)
- **Design direction & KB:** $150
- **Source A:** docs/03-DESIGN-SYSTEM.md ("the live $75 is being raised")
- **Source B:** manychat-kb/04-pricing.md, docs/09-PRODUCT-KNOWLEDGE.md ($150)
- **Resolution needed:** Has the change been implemented?

---

## PAGE ARCHITECTURE DECISIONS (Structural)

### PA-001: Home Page — 13 Sections (Matured)
- **Decision:** Final home page has 13 sections: Ticker → Header → Hero (media split) → Pillar strip → Why-it-works → Variant grid → Coperni/FP association → Sock-math → Testimonial → Founder note → Disciplines index → Closing statement → Footer.
- **Supersedes:** Live site's 20+ section layout; v2-v11 alternatives
- **Source:** docs/03-DESIGN-SYSTEM.md (Home section order)
- **Category:** DESIGN

### PA-002: Home Page — 16 Sections (Component Library Version)
- **Decision:** Component Library documents 16 sections: Ticker → Header → Hero → Pillar strip → Split 1 → Product grid → Promo tiles → Sock Math → Split 2 → Disciplines → Split 3 → Reviews → Coperni → Journal → Guarantee → Newsletter/FAQ/Social/Footer.
- **Note:** This differs from the matured direction (PA-001). The Component Library may reflect a pre-matured version.
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 931-947)
- **Category:** DESIGN

### PA-003: PDP — 10 Sections (Component Library)
- **Decision:** PDP architecture: Ticker → Header → PDP main → Pillar strip → Benefit grid → Split (fabric/construction) → Sock Math condensed → Reviews → Guarantee → Product rail → Footer.
- **Source:** docs/04-COMPONENT-LIBRARY.md (lines 949-959)
- **Category:** DESIGN

### PA-004: PDP — 10 Sections (Matured)
- **Decision:** PDP from matured direction: Ticker/header → Gallery/buy box split → Variant/size picker → Trust row → Pillar strip → Sock vs. skin comparison → Spec/materials accordion → Reviews (3 quotes) → Cross-sell → Footer.
- **Source:** docs/03-DESIGN-SYSTEM.md (PDP section order)
- **Category:** DESIGN

### PA-005: Collection — 7 Sections (Matured)
- **Decision:** Collection page: Ticker/header → Collection hero → Sole-type chooser → Filter row → Product grid → Editorial break (every 9 cards) → Footer.
- **Source:** docs/03-DESIGN-SYSTEM.md (Collection section order)
- **Category:** DESIGN

### PA-006: Articles — 720px Content Column
- **Decision:** All article templates share 720px content column, JetBrains Mono eyebrows, H2=36px, body=18px, 32-48px paragraph spacing, pull-quotes on hairlines (no quote-marks SVG).
- **Source:** docs/03-DESIGN-SYSTEM.md (Articles section)
- **Category:** DESIGN

---

## SUMMARY STATISTICS

| Category | Count |
|----------|-------|
| DESIGN | 41+ |
| BRAND | 16 |
| NAMING | 6 |
| PRODUCT | 11 |
| BUSINESS | 13 |
| OPERATIONAL | 14 |
| IMPLEMENTATION | 9 |
| CONFLICTS | 10 |
| **TOTAL** | **120+** |

---

**END OF INVENTORY**
