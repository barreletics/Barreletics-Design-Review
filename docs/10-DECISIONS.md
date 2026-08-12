# Decision Log — Complete Reference

**Status:** PENDING REVIEW  
**Purpose:** Every decision, rationale, superseded decision, implementation rule, and architectural choice — sourced and cited  
**Method:** Lossless extraction from all repository sources  
**Sources:** Barreletics_Research_Bible.md, barreletics-decisions-2026-07-09.json, IMPLEMENTATION-ROADMAP-Jul2026.md, Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html, docs/02–09, manychat-kb/, WORKFLOW.md, docs/04-COMPONENT-LIBRARY.md, docs/05-PDP-ARCHITECTURE.md

---

## DESIGN DECISIONS

### D-001: Font — Roboto Only
```
Decision: "Font: Roboto only (300–700), no Josefin Sans"
Rationale: Single-family type system for consistency; Josefin Sans was previously used and explicitly removed.
Supersedes: Previous use of Josefin Sans
```
Source: Barreletics_Research_Bible.md (Section 7, line 288), docs/03-DESIGN-SYSTEM.md (Typography), docs/04-COMPONENT-LIBRARY.md (line 11)

### D-002: JetBrains Mono for Technical Eyebrows
```
Decision: JetBrains Mono reserved for technical eyebrows and grip-spec captions on the matured direction only.
Rationale: Differentiation between editorial copy and technical labels.
Supersedes: N/A (addition to the system)
```
Source: docs/03-DESIGN-SYSTEM.md (Typography section)

### D-003: Button Radius — 0px (Square)
```
Decision: "Buttons: Square (radius 0), black #050505" — No drop shadows, no gradients, no rounded corners.
Rationale: Matches Shopify "button_style":"square" setting; maintains clean, editorial look.
Supersedes: Live PDP mock uses 6px radius (CONFLICT — see CONFLICTS section)
```
Source: Barreletics_Research_Bible.md (Section 7, line 290), docs/03-DESIGN-SYSTEM.md (Buttons), docs/04-COMPONENT-LIBRARY.md (line 37)

### D-004: Coral Accent Restraint — Cart Badge ONLY
```
Decision: "--br-accent (#f97250) — cart badge ONLY. Do not paint CTAs, headings, or section backgrounds in --br-accent."
Rationale: "The coral exists for the cart badge and nothing else. This is the single biggest correction the matured direction makes to the live site."
Supersedes: Live site uses coral on CTAs, section backgrounds
```
Source: docs/03-DESIGN-SYSTEM.md (Color section — Accent discipline), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS :root comments)

### D-005: Coral Eyebrow Usage Exception
```
Decision: Eyebrows use coral (#f97250) ONLY on white/light backgrounds. On dark sections use WHITE rgba(255,255,255,0.7).
Rationale: Maintains visibility contrast while keeping coral controlled.
Supersedes: N/A
```
Source: Barreletics_Research_Bible.md (Section 7, line 289), docs/04-COMPONENT-LIBRARY.md (lines 13–14)

### D-006: 50/50 Split Sizing — CANONICAL, DO NOT CHANGE
```
Decision: Fixed height: 420px (not min-height), overflow: hidden, padding: 80px 72px on copy side, slogan: clamp(28px, 3.2vw, 42px) with min-height: 0. Mobile: height: auto.
Reference: v18 "Never slip in chair pose" section.
Rationale: Established through iteration — locked.
Supersedes: Earlier split sizing attempts
```
Source: Barreletics_Research_Bible.md (Section 7, lines 294–300), docs/04-COMPONENT-LIBRARY.md (line 143)

### D-007: Color Palette — Exact Values
```
Decision: bg=#fff, text=#050505, accent=#f97250, star=#fbc02d, alt-bg=#f9f9f9, text-soft=#4a4a4a, text-mute=#8a8a8a, line=#e6e6e6
Rationale: Calibrated to live site; cream/plum palette in Shopify settings_data.json is dead code.
Supersedes: Unused cream/plum palette in settings_data.json
```
Source: Barreletics_Research_Bible.md (Section 7, line 292), docs/03-DESIGN-SYSTEM.md (Color table), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS :root)

### D-008: Sale Price — Ink Bold, Not Red
```
Decision: "--br-sale: var(--br-text); sale price is just ink-bold, not red"
Rationale: Editorial restraint; keeps visual hierarchy clean.
Supersedes: Standard e-commerce red sale pricing
```
Source: docs/03-DESIGN-SYSTEM.md (Color section)

### D-009: Limited Edition Chip — Blue (#3a8de8)
```
Decision: "Limited Edition" chip uses --br-le (#3a8de8) text on --br-le-bg (#eaf3fc) background.
Rationale: Differentiation from accent coral; informational rather than action-oriented.
```
Source: docs/03-DESIGN-SYSTEM.md (Color section)

### D-010: Card Border Radius — None by Default
```
Decision: Cards have no radius by default. Where matured direction uses radius (rare), 2px or 4px — never 12–16px pill-card.
Rationale: Matured editorial aesthetic; rejected live site's rounded cards.
Supersedes: Live site pill-card style (12–16px radius)
```
Source: docs/03-DESIGN-SYSTEM.md (Hairlines & radii), docs/04-COMPONENT-LIBRARY.md (lines 31–33)

### D-011: No Black/Orange Color Scheme
```
Decision: "Critical: NO orange/black. Warm or neutral only."
Rationale: CEO directive across all sections in decision review.
Supersedes: Earlier design explorations using black/orange
```
Source: IMPLEMENTATION-ROADMAP-Jul2026.md (line 8), barreletics-decisions-2026-07-09.json (repeated across sections 10, 13, 19, 27, 28)

### D-012: Implementation Roadmap Colors
```
Decision: "Colors: Warm (#eae5da) or white. Accent: Terracotta (#c45c3f). NO black/orange."
Rationale: Warm, premium feel; terracotta is a softer accent.
Supersedes: CONFLICT with Design System tokens (see CONFLICTS section)
```
Source: IMPLEMENTATION-ROADMAP-Jul2026.md (line 40)

### D-013: Animation — Reduced Motion Gate
```
Decision: "All animations gate on @media (prefers-reduced-motion: no-preference). Final state must be visible without animation."
Rationale: Accessibility compliance.
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 977–978), docs/03-DESIGN-SYSTEM.md (Interactions table)

### D-014: Touch Targets — 44×44px Minimum
```
Decision: All interactive elements must have minimum 44×44px touch target.
Rationale: Accessibility and mobile usability standard.
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 1011–1012)

### D-015: Mobile Breakpoint — 768px
```
Decision: Mobile breakpoint: 768px and below. Desktop: 768px+.
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 1008–1009)

### D-016: Spacing Scale
```
Decision: 4/8/12/16/24/32/48/64/96/128px scale (--sp-1 through --sp-10).
```
Source: docs/03-DESIGN-SYSTEM.md (Spacing scale), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS :root)

### D-017: Typography Ramp
```
Decision: Eyebrow 12px → body-sm 14px → body 16px → h6/body-lg 18px → h5 22px → h4 28px → h3 36px → h2 44px → h1 56px → display 72px.
Rationale: Single cohesive ramp; mobile uses clamp() on hero/display only.
```
Source: docs/03-DESIGN-SYSTEM.md (Typography table)

### D-018: Eyebrow Styling — CONFLICT
```
Decision A: 12px / font-weight 700 / letter-spacing 0.14em / uppercase
Decision B: 12px / font-weight 600 / letter-spacing 0.08em / uppercase
CONFLICT: Sources disagree. See CONFLICTS section.
```
Source A: docs/04-COMPONENT-LIBRARY.md (line 12), Barreletics_Research_Bible.md (Section 7, line 289)
Source B: docs/03-DESIGN-SYSTEM.md (Typography table), docs/06-HOMEPAGE-ARCHITECTURE.md (CSS)

### D-019: Ticker — 3 Slides, 4s Interval
```
Decision: Announcement ticker: 3-slide auto-rotator, 4s interval, opacity crossfade 320ms ease. Pause on hover.
```
Source: docs/04-COMPONENT-LIBRARY.md (line 63), docs/03-DESIGN-SYSTEM.md (Interactions table)

### D-020: Hero Eyebrow Rotation — 3.5s Cycle
```
Decision: Rotating eyebrow with 3.5s cycle containing 5 messages:
1. "The Pilates sock era is over."
2. "A new kind of grip shoe."
3. "Trusted by 1,000's of instructors."
4. "Made in USA. Built for the carriage."
5. "Barre. Reformer. Megaformer. One shoe."
```
Source: Barreletics_Research_Bible.md (Section 4, lines 192–197), docs/04-COMPONENT-LIBRARY.md (lines 109–114), docs/02-BRAND-SYSTEM.md (Section 2)

### D-021: Product Card — No Swatches, Each Color = Own Card
```
Decision: "Each color = its own card with image, color name, price, Quick Add button. NEVER use swatches on one card."
Rationale: Direct add-to-cart from grid without PDP redirect.
Supersedes: Standard e-commerce single-card-with-swatches pattern
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 188–192)

### D-022: Reviews — Load More, Not Full Pagination
```
Decision: "Load more" appends next 6 reviews per click. No full pagination.
Rationale: Keep page lightweight while enabling browsing.
```
Source: docs/04-COMPONENT-LIBRARY.md (line 268), docs/03-DESIGN-SYSTEM.md (Interactions table)

### D-023: Collection Filter — Inline Chips, Not Sidebar
```
Decision: Filter row uses inline chips. Multi-select within a facet, exclusive between facets. URL-syncs via query params.
Rationale: Reduce friction; mobile-friendly.
Supersedes: Sidebar filter pattern
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 288–293), docs/03-DESIGN-SYSTEM.md (Interactions table)

### D-024: PDP Gallery — Sticky Buy Box
```
Decision: Sticky buy box on right (position: sticky; top: 64px). Image-stack left.
Rationale: Buy box always visible while browsing gallery.
```
Source: docs/05-PDP-ARCHITECTURE.md (line 35), docs/03-DESIGN-SYSTEM.md (PDP section order)

### D-025: PDP Accordion — One Open at a Time
```
Decision: One open at a time. 200ms height transition.
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 251–252), docs/03-DESIGN-SYSTEM.md (Interactions table)

### D-026: Sock ⇄ Skin Toggle
```
Decision: Cross-fade between two image states + swap two stat figures. 240ms ease-out. State persists via aria-pressed.
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 170–175), docs/03-DESIGN-SYSTEM.md (Interactions table)

### D-027: Header — Sticky with Hairline on Scroll
```
Decision: Sticky on scroll. Adds 1px bottom hairline (--br-line) on scroll > 8px. Cart badge dot (--br-accent) visible only when items > 0.
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 80–82), docs/03-DESIGN-SYSTEM.md (Interactions table)

### D-028: No State Library Required
```
Decision: "No app-level state library required." State handled by Shopify cart API, standard variant routing, URL query params, and local JS.
Rationale: Shopify handles all persistent state.
```
Source: docs/03-DESIGN-SYSTEM.md (State section)

### D-029: Matured Direction — Final Choice
```
Decision: "The team chose the matured editorial direction. Build that. The others are decision history."
Rationale: v2-v11 explored: cinematic, multi-tile, hybrid, Coperni-led, editorial, video hero. Matured editorial won.
Supersedes: All Home v2–v11 variants; all pre-matured exploration files
```
Source: docs/03-DESIGN-SYSTEM.md (Home page section)

### D-030: Section Count — Halved
```
Decision: Section count halved from original live site.
Rationale: Audit determined live site had too many sections ("slogan soup"). Cut for editorial restraint.
Supersedes: Original 20+ section live site homepage
```
Source: docs/03-DESIGN-SYSTEM.md (Audit reference)

### D-031: Numbered Sections — NOT for Production
```
Decision: "01-section.html through 29-section.html — Design study variations. Do NOT use for production builds; use named sections."
Rationale: Exploration files; named section files are canonical.
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 1086–1089)

### D-032: pg-tab-strip — Strip from Production
```
Decision: "Strip it from production output." Review-only navigation between mockups.
```
Source: docs/03-DESIGN-SYSTEM.md (lines 97–99)

### D-033: Tweaks Panel — Not for Production
```
Decision: "*-tweaks.jsx + tweaks-panel.jsx is a preview-time controls panel for design review. Not part of production site."
```
Source: docs/03-DESIGN-SYSTEM.md (lines 100–103)

### D-034: Design Files Are Prototypes
```
Decision: "They are prototypes showing intended look, copy, layout, density, and behavior — not production code to copy directly."
Rationale: Recreate in Shopify Liquid; do not lift HTML wholesale.
```
Source: docs/03-DESIGN-SYSTEM.md (About the Design Files)

### D-035: Implementation Order
```
Decision: 1. Tokens first → 2. Header + footer → 3. PDP → 4. Home → 5. Collection → 6. Articles + Blog → 7. Strip review chrome.
Rationale: PDP is highest-revenue page; tokens must be established first.
```
Source: docs/03-DESIGN-SYSTEM.md (Suggested implementation order)

### D-036: PDP Text Color — #1c1916
```
Decision: PDP uses text color #1c1916 (slightly warmer ink, not #050505).
Supersedes: Possible divergence from design system --br-text (#050505) — see CONFLICTS
```
Source: docs/05-PDP-ARCHITECTURE.md (CSS lines 24, 42–43)

### D-037: PDP CTA Button — Hover to Coral
```
Decision: PDP primary CTA hovers from ink (#1c1916) to coral (#c45c3f).
Supersedes: Possible conflict with coral restraint rule (D-004) — see CONFLICTS
```
Source: docs/05-PDP-ARCHITECTURE.md (line 47)

### D-038: PDP Review Card — 12px Border Radius
```
Decision: Review cards on PDP use border-radius: 12px.
Supersedes: Conflicts with D-010 (no radius by default, max 4px) — see CONFLICTS
```
Source: docs/05-PDP-ARCHITECTURE.md (line 67)

### D-039: PDP Gallery Hero — 8px Border Radius
```
Decision: PDP gallery hero image uses border-radius: 8px.
Supersedes: Conflicts with D-010 — see CONFLICTS
```
Source: docs/05-PDP-ARCHITECTURE.md (line 36)

### D-040: PDP Color Swatches — Used on PDP Only
```
Decision: PDP uses circular color swatches (23px diameter, 50% radius, 2px border, aria-selected state).
Rationale: PDP is the appropriate place for swatches (vs. never on product cards per D-021).
```
Source: docs/05-PDP-ARCHITECTURE.md (lines 48–51)

### D-041: Max Width Hierarchy
```
Decision: Multiple max-widths by context:
- Page container (matured): 1320px
- PDP sections: 1200px
- PDP hero: 1400px
- Implementation roadmap: 1200px
```
Source: docs/06-HOMEPAGE-ARCHITECTURE.md (au-doc: 1320px), docs/05-PDP-ARCHITECTURE.md (lines 53–54, 153), IMPLEMENTATION-ROADMAP-Jul2026.md

---

## BRAND DECISIONS

### B-001: "Performance Skin" — Not a Sock
```
Decision: "Product: $74 'performance skin' — NOT a sock. Never call it a sock."
Rationale: Category creation; differentiation from grip socks.
Supersedes: Any copy referring to product as a "sock"
```
Source: docs/02-BRAND-SYSTEM.md (Section 4), Barreletics_Research_Bible.md (Section 1, line 8)

### B-002: Voice Priority Order
```
Decision: "Voice priority: Safety + grip + 'replaces socks' BEFORE lifestyle."
Rationale: Safety and function-first before fashion.
```
Source: docs/02-BRAND-SYSTEM.md (Section 4)

### B-003: Brand Voice — Confident Instructor Tone
```
Decision: "Confident instructor who's seen it all. Direct, warm, a little dry. Never hype-y. Short sentences. Real benefits. Let reviews and the 30-day trial do the convincing."
```
Source: docs/02-BRAND-SYSTEM.md (Section 3), manychat-kb/12-brand-voice-and-taglines.md (lines 9–11)

### B-004: One Emoji Max
```
Decision: "Premium, calm, confident. One emoji max or none at all on serious messages."
```
Source: docs/02-BRAND-SYSTEM.md (Section 3), manychat-kb/12-brand-voice-and-taglines.md (line 11)

### B-005: Each Section Anchored by a Slogan
```
Decision: "Each section is anchored by a slogan. The rotating hero eyebrow slogans are the best lines in the brand — they should be the organizing principle."
Rationale: Slogans aren't decoration; they're section headlines.
Supersedes: Live site's "slogan soup" approach
```
Source: docs/02-BRAND-SYSTEM.md (Section 1)

### B-006: Benefits Distributed, Not Lumped
```
Decision: "No standalone 'benefit grid' section on the home page. Benefit grid lives on PDP and Collection pages."
Supersedes: Standalone benefit grid on homepage (live site)
```
Source: docs/02-BRAND-SYSTEM.md (Section 1)

### B-007: "Trusted by 1,000's" — Placement Rule
```
Decision: "Appears in the stars/trusted line of every 50/50 split hero, not as a section headline."
```
Source: docs/02-BRAND-SYSTEM.md (Section 1)

### B-008: Double Failure Concept — Use on PDP
```
Decision: "'Your foot moves in the sock. The sock moves on the floor. Now neither does.' — Use on PDP."
```
Source: docs/02-BRAND-SYSTEM.md (Section 4), Barreletics_Research_Bible.md (Section 1, line 10)

### B-009: Words to Avoid
```
Decision: Never use: "Cheap," "Just socks," generic hype ("amazing!!!"), medical promises, emoji spam.
```
Source: docs/02-BRAND-SYSTEM.md (Section 5), manychat-kb/12-brand-voice-and-taglines.md (line 58)

### B-010: Hashtag
```
Decision: Official hashtag: #letusknockyoursocksoff
```
Source: docs/02-BRAND-SYSTEM.md (Section 3), Barreletics_Research_Bible.md (Section 4, line 190)

### B-011: Hero Body Copy — Approved
```
Decision: "Not a sock. A performance skin. 360° grip through every pose, transition, class — on the mat or off it."
```
Source: Barreletics_Research_Bible.md (Section 6, line 269)

### B-012: Coperni Association — Restrained
```
Decision: "Light, restrained logo lockup with a single line of credibility copy. Do not scatter collab tiles like v1."
Supersedes: v1 scattered collab tiles approach
```
Source: docs/03-DESIGN-SYSTEM.md (Home section 7)

### B-013: Sock Math — Single Editorial Slogan
```
Decision: "Dark band, single editorial slogan with one rotating proof line. Not the stacked-claim soup of the live site."
Supersedes: Live site's stacked-claim sock math section
```
Source: docs/03-DESIGN-SYSTEM.md (Home section 8)

### B-014: Testimonial — One Proof, Not Tile Wall
```
Decision: "One editorial proof with citation and a supporting stat row. Not a dense tile wall."
Supersedes: Dense testimonial tile wall (live site)
```
Source: docs/03-DESIGN-SYSTEM.md (Home section 9)

### B-015: PDP Reviews — Resist Full Wall
```
Decision: "Reviews summary + 3 selected quotes + single 'read all reviews' link. Resist the temptation to ship a full reviews wall."
Supersedes: Full reviews wall on PDP
```
Source: docs/03-DESIGN-SYSTEM.md (PDP section 8)

### B-016: "Sock vs. Skin" — Editorial, Not Table
```
Decision: "Editorial 2-col, not a table of red Xs and green checks."
Supersedes: Standard comparison tables
```
Source: docs/03-DESIGN-SYSTEM.md (PDP section 6)

---

## NAMING DECISIONS

### N-001: "Blog" → "Journal"
```
Decision: "'Blog' → 'Journal' everywhere"
Rationale: Premium brand positioning.
Supersedes: "Blog" terminology
```
Source: Barreletics_Research_Bible.md (Section 7, line 291)

### N-002: Product Name — Design System vs Production
```
CURRENT PRODUCTION: "Best Grippy Shoes for Barre, Pilates & Yoga — [Sole Type]"
FUTURE DESIGN SYSTEM: "Studio Performance Skin — [Sole Type]"
Rationale: Production = SEO-optimized. Design System = brand-appropriate.
```
Source: docs/09-PRODUCT-KNOWLEDGE.md (Conflicts Register)
Cross-reference: docs/05-PDP-ARCHITECTURE.md, Shopify store

### N-003: Color Names — Design System vs Production
```
CURRENT PRODUCTION: Black, LightGrey, DarkGrey, Blue, Bright Yellow, Coral, etc.
FUTURE DESIGN SYSTEM: Onyx (→ Black), Stone (→ LightGrey), others TBD
```
Source: docs/09-PRODUCT-KNOWLEDGE.md (Conflicts Register), docs/05-PDP-ARCHITECTURE.md (lines 201, 205–207)

### N-004: Product Category Terms
```
Decision: "Grippy Footwear" (performance skin), "In-Studio Grip" (studio), "Outdoor" (water shoes), "Apparel", "Collaborations"
```
Source: docs/09-PRODUCT-KNOWLEDGE.md (product category fields)

### N-005: Navigation Labels
```
Decision: "Grippy Footwear, Apparel, Collaborations, Journal, About Us"
```
Source: docs/04-COMPONENT-LIBRARY.md (line 77)

### N-006: "Performance Skin" vs "Grip Shoe"
```
Decision: Body copy = "performance skin". SEO title = "Grippy Shoes".
Rationale: Brand differentiation in copy; search visibility in titles.
```
Source: Barreletics_Research_Bible.md (Section 1), docs/09-PRODUCT-KNOWLEDGE.md

---

## PRODUCT DECISIONS

### P-001: Pricing Structure
```
Standard Performance Skins: $74
Limited Edition Colors (Turquoise, Copper Swirl, Purple): $78
Coperni Collaboration: $115
One Off Colors (DRAFT): $82
Yoga Tight: $89 (sale) / $129 (compare-at)
V-Neck T-Shirt: $39
Tank Top: $34
```
Source: docs/09-PRODUCT-KNOWLEDGE.md, manychat-kb/04-pricing.md

### P-002: Sizing — M and L Only
```
Decision: Two sizes only: Medium (W 5.5–7.5) and Large (W 8–11 / M up to 10.5).
Rationale: "No small size — the material stretches and conforms to your foot."
```
Source: docs/09-PRODUCT-KNOWLEDGE.md, manychat-kb/03-sizing-chart.md

### P-003: Open vs Closed — Same Performance
```
Decision: "Both perform identically with the same grip and stability. The difference is feel and coverage."
```
Source: manychat-kb/02-open-vs-closed-sole.md

### P-004: First-Time Buyer → Open Sole — SUPERSEDED 2026-08-02
```
OLD (DO NOT USE): "Most first-time buyers start with Open Sole — the barefoot feel is where they shine."
SUPERSEDED: Do not recommend first-timers toward either sole. Choice = preference / feel only (P-003).
```
Source: Owner letter 2026-08-02; manychat-kb/02-open-vs-closed-sole.md (updated)

### P-005: No Machine Washing
```
Decision: "Warm soapy water, air dry. No machine washing."
```
Source: manychat-kb/06-care-and-cleaning.md

### P-006: Made in USA — Every Pair
```
Decision: All products made in USA.
```
Source: Barreletics_Research_Bible.md (Section 1), Shopify product descriptions

### P-007: No Direct Competitor
```
Decision: "No direct competitor in the 'performance skin' category. Barreletics created and owns this category."
```
Source: Barreletics_Research_Bible.md (Section 5, line 235)

### P-008: Grip Material — Not Silicone, Not Latex
```
Decision: "Proprietary grip material (not silicone, not latex)."
Rationale: Skin-safe; differentiator from grip socks.
```
Source: Barreletics_Research_Bible.md (Section 1, line 18)

### P-009: Injection-Molded Sole
```
Decision: Structured, injection-molded sole (not printed dots on fabric).
```
Source: docs/09-PRODUCT-KNOWLEDGE.md, Shopify product descriptions

### P-010: Kids Size — Partly resolved 2026-08-12
```
Decision: Water Shoes has 6 dedicated Kids variants in Shopify at 0 inventory. Not documented anywhere on live site or in any copy.
Status: Data quality flag — likely discontinued or placeholder.

UPDATED 2026-08-12 (owner): Distinct from the dedicated variants, Kids' US 2–5
fit MEDIUM, and that column has always been published on the live size chart.
It belongs on the size chart. See P-015 / D-053.
STILL OPEN: 09-PRODUCT-KNOWLEDGE.md line 84 says "Youth 4–6 wear Medium," which
does not match Kids' 2–5. Do not quote a youth number until Andrew resolves it.
```
Source: docs/09-PRODUCT-KNOWLEDGE.md (Data Quality Flags), owner letter 2026-08-12

### P-015: Canonical Answers Source — sizing, cleanliness, longevity (2026-08-12)
```
AUTHORITY: docs/11-CANONICAL-ANSWERS.md is the single source for customer-facing
answers. Pages, email, ManyChat, and ads copy from it verbatim. Change it there
first, then propagate. Full record: planning/10-decision-log.md → D-053.

SIZE CHART (publish all four columns):
  M = Women's 5.5–7.5 · Kids' 2–5
  L = Women's 7.5–11 · Men's up to 10.5
  Large starts at 7.5, NOT 8. 7.5 sits in both rows; width is the tiebreaker.

BETWEEN SIZES — width decides, never "size up":
  Wide foot at 7 or 7.5 → L
  Narrow foot at 7.5 or 8 → M
  8.5 and above → L always, regardless of width (length governs)

APPROVED: "patented" (accurate — do not purge) · non-porous / wipes clean ·
  skin-safe and non-toxic, no latex, no silicone · 195 countries via FedEx
  International Connect Plus (real) · longevity = expectation first, then
  1,000 classes and year four

RETIRED — never reintroduce:
  antimicrobial (any form) · any claim our material resists/repels/kills
  bacteria · "hygienic" · hypoallergenic (D-019) · "conforms over the first few
  wears" and all break-in variants · Foot Length column · M 5–8 / L 8.5–11 ·
  L 8–11 · M W 5–7.5 Men 6–8 / L W 8–10 Men 8.5–11 · blanket "size up" ·
  "Small is coming soon" · "18+ months" (internal floor only) ·
  "gentle environment" · antimicrobial fabric on the Apparel tee

SUPPORT-ONLY: the blow dryer heat-stretch tip is a HelpScout saved reply
  (template 2.7). Never on a page, never in ManyChat. Offer the exchange first.
```
Source: owner letters 2026-08-12 · docs/11-CANONICAL-ANSWERS.md · planning/10-decision-log.md D-053

### P-011: One-Off Colors — Surfaces + Lean PDP (updated 2026-08-10)
```
Decision: One-off colors are separate products (Closed + Open), not metafield-driven nav.

Gate: Theme settings → One-off colors → product picker.
  Set → header nav under Grippy + quiet PDP link under ATC + All Variants One-Offs tab.
  Empty → all hide. Theme setting wins over section product_oneoffs.
  Do not add One-off colors in Online Store → Navigation.

Products / Admin templates:
  one-off-colors-closed-sole → theme template one-off-closed
  one-off-colors-open-sole   → theme template one-off-open

Buy box (one-off PDPs): shoe-photo color pickers; hide sold-out options.
All Variants One-Offs tab: single grid — available first, then sold-out (no separate Earlier band).

PDP spine: Closed Sole quality twin (no sock-era / TRANSFORM / sock-math). See planning/one-off-surfaces.md.

Pricing remains $82.00 tier.
Featured-drop strategy → **P-014** / **D-052** (one picker at a time).
Cross-ref: D-051 · planning/one-off-surfaces.md · page-template-registry.md
```
Source: Owner direction 2026-08-10 (M4 QA); planning/one-off-surfaces.md

### P-014: One-Off Featured Drop — Single Theme Picker (2026-08-10)
```
Decision: Feature ONE one-off at a time via Theme settings → One-off colors → product picker.

RULES:
  - Featured = the single `one_off_product` picker (nav + quiet ATC link + core PDP One-Offs tab).
  - Both sole products may exist in Admin (Closed + Open one-off). Only the featured one appears in nav.
  - Flip the picker when the drop changes (Open OR Closed — not both in nav).
  - Do NOT mix Open + Closed variants into one Shopify product for now
    (inventory, template suffix, ATC, and sole badge all get messier).
  - Do NOT build a third-level nav (Grippy → One-off → Open/Closed) — messy on mobile.

FUTURE (not built — needs Andrew confirm before Liquid):
  If both drops must be live in the menu at once → two sibling links under Grippy
  ("One-off · Open" / "One-off · Closed"), each with its own picker. No third layer.
  Quiet link stays a single "this week’s" featured product.

Cross-ref: P-011 · D-051 · D-052 · planning/one-off-surfaces.md
```
Source: Owner direction 2026-08-10 (strategy lock after M4 one-off QA)

### P-012: Pool Positioning RETIRED — 2026-08-07
```
Decision: Remove all pool positioning from every surface.

BANNED: pool, poolside, pool deck, "around the pool", "in the pool",
        water park, tidal pool / tidepool, spa visits, aqua barre, water aerobics

USE INSTEAD: resortwear, paddleboarding, beach, outdoor yoga
             (plus boating, boat deck, hot sand, travel)

Do not invent scenery. No rocky coves, rocky coastline, rocky shorelines,
tidepools, shell-covered beaches, pebbly lake beds. Beach covers it.

Reason: customers bought for pool use and slipped on wet tile.
        Pool language attracts the wrong buyer and creates liability.

Scope: FAQ, GEO, product descriptions, SEO tags, collection copy,
       blog, email, ManyChat, ads, and all operating-system docs.
```
Source: Owner letter 2026-08-07; `.cursor/rules/no-pool-positioning.mdc`

### P-013: "Fully enclosed" RETIRED — 2026-08-08
```
Decision: Drop "Sleek, fully enclosed feel." from the P-003 Closed Sole answer.

BANNED: "fully enclosed", "fully-enclosed", "fully enclosed heel", "fully enclosed feel"

SURVIVING APPROVED LINE:
  Closed Sole: Heel and foot fully covered. Same grip, same stability.

Reason: Owner letter — "quit saying fully enclosed heel - dont make shit up".
        Supersedes the older approved P-003 wording. Historical record kept,
        marked RETIRED, in docs/09-PRODUCT-KNOWLEDGE.md and
        manychat-kb/02-open-vs-closed-sole.md — not reusable as source copy.

Scope: PDP + variant templates, collection copy, studio/wholesale/partner
       pages, FAQ, GEO, ManyChat KB, and all operating-system docs.
```
Source: Owner letter 2026-08-08; P-003 (`manychat-kb/02-open-vs-closed-sole.md`)

---

## BUSINESS DECISIONS

### BZ-001: 30-Day Return Policy
```
Decision: 30-day returns. Must be clean, like new, no outdoor wear. Return shipping: $7.95 deducted from refund.
```
Source: manychat-kb/07-returns-and-exchanges.md, docs/09-PRODUCT-KNOWLEDGE.md

### BZ-002: Free Exchanges
```
Decision: "Free exchanges — we ship at no cost once we receive and inspect your return."
```
Source: manychat-kb/07-returns-and-exchanges.md

### BZ-003: 90-Day Warranty
```
Decision: 90-day warranty against manufacturing defects. Return of defective item not required in most cases.
```
Source: manychat-kb/07-returns-and-exchanges.md

### BZ-004: Shipping — Free Over $150
```
Decision: Free shipping over $150. $9.95 flat rate under.
Rationale: Encourages multi-pair purchase (2 pairs = $148).
Supersedes: Previous $75 threshold
```
Source: manychat-kb/08-shipping.md, docs/09-PRODUCT-KNOWLEDGE.md

### BZ-005: Free Shipping Threshold — $75 → $150
```
Decision: Raised from $75 to $150.
Status: Change is now live (confirmed in docs/08-LIVE-SITE-COPY-AUDIT.md).
Supersedes: $75 free shipping threshold
```
Source: docs/03-DESIGN-SYSTEM.md (PDP key copy rules), docs/08-LIVE-SITE-COPY-AUDIT.md

### BZ-006: Buy 2+ Save 15% (Code: SAVE15)
```
Decision: Buy 2+ save 15%. Auto-applied at checkout.
Rationale: Instructor market buys 2–3 pairs.
```
Source: manychat-kb/04-pricing.md

### BZ-007: Newsletter 10% Off First Order — RETIRED
```
Original decision: 10% off via newsletter signup.
Superseded 2026-07-31 (Footer LOCK): newsletter offer is "Join the list" with benefit
checkmarks — NO 10%, NO discount promise. Do not reintroduce in any surface
(footer, page newsletter, email, ManyChat, ads).
Authority: specs/frozen/footer.md · planning/m4-section-freeze.md (Footer row)
```
Source: manychat-kb/04-pricing.md · retired per Footer LOCK 2026-07-31

### BZ-008: Shop Pay — 4 Installments
```
Decision: Shop Pay splits $74 into 4 interest-free payments of $18.50.
Rationale: Reduces price objection.
```
Source: manychat-kb/04-pricing.md

### BZ-009: No Medical Promises
```
Decision: "Cannot guarantee outcomes for specific medical conditions." Hand off sensitive medical questions to human team.
Rationale: Legal compliance; liability.
```
Source: manychat-kb/11-sensitive-and-medical.md, manychat-kb/14-escalation-and-handoff.md

### BZ-010: AI Escalation Rules
```
Decision: Hand off to human for: order status/tracking/refunds, wholesale/bulk/press, account access/payment data, complaints/disputes/legal, anything uncertain.
```
Source: manychat-kb/14-escalation-and-handoff.md

### BZ-011: No Personal Data in DM
```
Decision: "Never collect [personal data] in DM" — address, payment, account info requires handoff.
```
Source: manychat-kb/14-escalation-and-handoff.md

### BZ-012: Lost Package Policy
```
Decision: "Once tracking shows delivered, order considered fulfilled. Cannot issue refunds for packages shown as delivered."
```
Source: manychat-kb/08-shipping.md, docs/09-PRODUCT-KNOWLEDGE.md

### BZ-013: International — Customer Covers Duties → **SUPERSEDED by P-016**
```
RETIRED 2026-08-12. Was: "International customers responsible for duties, taxes, customs."
That is backwards — duties are prepaid.
```
Source: manychat-kb/08-shipping.md

### P-016: International duties are PREPAID *(Andrew 2026-08-12)*
```
Duties and taxes are prepaid. Orders clear customs with nothing further to pay.
Say it as an advantage — never as a warning.

Customer-paid exceptions (narrow, do not leak into outbound copy):
  · international RETURN shipping
  · international WARRANTY REPLACEMENT shipping
```
Andrew: the "customer responsible for duties" language was "probably for the warranty replacement." It had spread to eight surfaces, including a HelpScout reply telling buyers to "be prepared to pay them on delivery."
Supersedes: BZ-013 · Canonical: `docs/11-CANONICAL-ANSWERS.md` CA-18
⚠️ Open verification: confirm Shopify market/carrier collects duties at checkout (DDP) for all destinations — `planning/OWNER-MANUAL-TASKS.md`

---

## SECTION DECISIONS (CEO Review — 2026-07-09)

Raw CEO decisions from section-by-section review. Verbatim notes preserved.

Source: barreletics-decisions-2026-07-09.json, IMPLEMENTATION-ROADMAP-Jul2026.md

### Section 01 — Hero
```
Decision: Keep (custom blend)
Owner: Cowork
Notes: "Create th option to have the see in action button. Use the eye borw from current"
Version: custom
Build effort: Light
```

### Section 03 — 50/50 Progress
```
Decision: Keep (custom blend)
Owner: Cowork
Notes: "Keep the Trusted by rating from teh current."
Version: custom
Build effort: Light
```

### Section 04 — Coperni + FP
```
Decision: (undecided)
Notes: (none)
Version: (none)
```

### Section 06 — Credibility
```
Decision: Refactor
Owner: Cowork
Notes: "thishas to be updated in judgeme. We would also need to display images. Maybe we have more than one layout?"
Version: current
```

### Section 07 — Trust & Proof
```
Decision: Refactor
Notes: "we should probnably try a warm or white verion. I am not sure we want to introduce all the black or not"
Version: matured
```

### Section 08 — Disciplines
```
Decision: Refactor
Notes: "this is excellent - its the sie correct. Can we have settings to tweak or adjust it once the section is built"
Version: matured
```

### Section 09 — The Problem
```
Decision: Keep (matured)
Notes: "this section is good but there are others with the same messging that is also good we need to look at all of them. current mature 1 and mature 2 are all good"
Version: matured
Build effort: None
```

### Section 10 — Brand & Conv
```
Decision: Refactor
Notes: "v2 matured is the best. is this a pdp page or collection age or home page section?Its good but we cannot use black and orange, Too generic of a design that looks like claude, The warm background or neuatral mighr be cleaning but the actually content and messaing is great"
Version: matured
```

### Section 12 — Variants
```
Decision: Refactor
Notes: "V28, 14 th variant grid and 12 variants color + style sections are great . we need to design the best of but note this section is already custom buid with heavy coding. We would have to just modify the look and maybe a little functionality. small lift mostly aethtic"
Version: not sure
```

### Section 13 — Conversion
```
Decision: Refactor
Notes: "again not sure on the black and def not orange with black"
Version: matured
```

### Section 14 — Variant Grid v2
```
Decision: Refactor
Notes: "i made notes above use this version mixed with the other variant sections"
Version: not sure
```

### Section 15 — v28 Original
```
Decision: (undecided)
Notes: "yes keeo this section and merge with the other all variant sections"
Version: not sure
```

### Section 17 — Never Slip in Chair Pose
```
Decision: Keep (current)
Notes: "this is a modifaction of our current 50/50 section. We neeed to decide of this section will just have options in the shoify section to be able to tweak and modify. It will just require more or les a fe aesthtic updates and font chnages"
Version: current
Build effort: Medium
```

### Section 18 — Promo Tiles
```
Decision: Refactor
Notes: "this is really good. We need ot decide what we use it for but being versitle woluld be good"
Version: current
```

### Section 19 — Sock Math
```
Decision: Refactor
Notes: "this is excellent but a huge sectin and the black and orange sucks. We need it to be more mautrla with a punch kike nike. The design is very good but we need it to be more efficient"
Version: not sure
```

### Section 20 — Never Loses Grip
```
Decision: Refactor
Notes: "again is this a shared 50/50 section with fuctinality options in the section?"
Version: matured
```

### Section 21 — Push Harder
```
Decision: Refactor
Notes: "again another 50/50 section do we build one with section options?"
Version: matured
```

### Section 23 — Video & Content
```
Decision: Refactor
Notes: "this is. good but not sure if it nalils it. we may just use a 5050 with a video section. we also have to think about moble and I dont know if this is good for it"
Version: not sure
```

### Section 24 — Content 2
```
Decision: (undecided)
Notes: "this is good - as mentioned do we have more than one option and ability to add picture like the other section"
Version: not sure
```

### Section 25 — Coperni Collab
```
Decision: (undecided)
Notes: "this is not good enough. do we use our existing"
Version: custom
```

### Section 26 — Content 3
```
Decision: Refactor
Notes: "this is great for the blof. Does it need tweaks. orange?"
Version: current
```

### Section 27 — SEO Section
```
Decision: Refactor
Notes: "this iis excellent. I this for the pdp page at the bottom for seo and geo?no fucking orange. i think there is another version of this"
Version: current
```

### Section 28 — Conv Support
```
Decision: Refactor
Notes: "yes very good but black anf orange NO."
Version: current
```

### Section 29 — Final CTA
```
Decision: (undecided)
Notes: "we have our juicer feed. Could we mature the current site by going to an updated version> can we code juicer to make it look how we want?"
Version: not sure
```

---

## OPERATIONAL DECISIONS

### O-001: Document Status System
```
Decision: STUB → BUILDING → PENDING REVIEW → APPROVED → SUPERSEDED
Rule: "No document becomes APPROVED without explicit ChatGPT approval."
```
Source: WORKFLOW.md

### O-002: Role Definitions
```
CEO (Andrew): Assigns, approves, breaks ties.
Lead Architect (ChatGPT): Designs specs, reviews, approves.
Build Engineer (Cursor): Executes, commits, pushes.
```
Source: WORKFLOW.md

### O-003: One Commit Per Deliverable
```
Decision: "One commit per deliverable. The deliverable is the atomic unit, not the conversation."
```
Source: WORKFLOW.md

### O-004: No Invention Rule
```
Decision: "The Build Engineer builds from source material provided or independently verifiable. Never fabricate content."
```
Source: WORKFLOW.md (Rule 4)

### O-005: No Unsupported Metrics
```
Decision: "Never report counts, metrics, percentages, or statistics unless measured directly from repository or source material. No estimates. No inferred counts. No approximations."
```
Source: WORKFLOW.md (Rule 2)

### O-006: Correct, Don't Defend
```
Decision: "If the Build Engineer discovers during self-audit that an earlier report was incorrect, immediately correct it. Do not defend. Do not justify. Simply correct."
```
Source: WORKFLOW.md (Rule 3)

### O-007: Self-Audit Before Reporting
```
Decision: "Every deliverable is self-audited against its Acceptance Criteria before reporting done."
```
Source: WORKFLOW.md (Rule 5)

### O-008: Auto-Approve Categories
```
Decision: Auto-approve (no ChatGPT review): Status changes, structural edits, Shopify code, git operations, tooling, workflow docs.
```
Source: WORKFLOW.md (Approval Flow)

### O-009: Context Between Sessions
```
Decision: "Each session starts fresh from repository state. Git history, file contents, and this workflow persist. Prior conversation memory does not carry over unless transcripts are explicitly consulted."
```
Source: WORKFLOW.md (Context Between Sessions)

---

## IMPLEMENTATION DECISIONS

### I-001: Shopify Online Store 2.0 Assumed
```
Decision: "The designs assume [OS 2.0]. If not, templates need porting first."
```
Source: docs/03-DESIGN-SYSTEM.md (Questions for developer)

### I-002: Recreate in Liquid, Not Copy HTML
```
Decision: "Recreate inside existing Shopify theme using theme's established patterns. Do not lift HTML wholesale."
```
Source: docs/03-DESIGN-SYSTEM.md (About the Design Files)

### I-003: New Sections — Editor-Friendly Schema
```
Decision: "Add new Shopify section with editor-friendly schema (block types, settings) that mirrors variations."
```
Source: docs/03-DESIGN-SYSTEM.md (About the Design Files)

### I-004: Photography Is Placeholder
```
Decision: "All photography is placeholder. Brand team provides final art-directed photography before launch."
```
Source: docs/03-DESIGN-SYSTEM.md (Assets)

### I-005: Version Management — Increment, Don't Overwrite
```
Decision: "Increment version on every new file. Don't overwrite existing versions."
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 1060–1062)

### I-006: Structured Data / Schema.org
```
Decision: PDP includes Product structured data with AggregateRating, Offer (price $74, InStock), Brand.
```
Source: docs/05-PDP-ARCHITECTURE.md (lines 129–148, JSON-LD)

### I-007: PDP H1 = Shopify Product Title (SEO)
```
Decision: H1 = Shopify product title (18px/600). Marketing headline below (44px/700).
Rationale: SEO in H1; brand messaging in visual headline.
```
Source: docs/05-PDP-ARCHITECTURE.md (lines 181–188)

### I-008: PDP Hero Toggle — Closed/Open Sole
```
Decision: PDP has hero-toggle between Closed and Open Sole views (data-active switching).
Rationale: Single PDP serves both sole types.
```
Source: docs/05-PDP-ARCHITECTURE.md (lines 29–31)

### I-009: 50/50 Sections — Build One with Options
```
Decision: CEO asks "do we build one [50/50 section] with section options?" for Sections 17, 20, 21.
Rationale: Reusable section with Shopify settings vs. multiple unique sections.
Status: Needs clarification
```
Source: barreletics-decisions-2026-07-09.json (Sections 17, 20, 21)

### I-010: Variant Grid — Merge Multiple Versions
```
Decision: "V28, 14 the variant grid and 12 variants color + style sections are great. We need to design the best of."
Note: "This section is already custom build with heavy coding. Small lift mostly aesthetic."
```
Source: barreletics-decisions-2026-07-09.json (Sections 12, 14, 15)

### I-011: Juicer Feed — Mature Current
```
Decision: "we have our juicer feed. Could we mature the current site by going to an updated version? can we code juicer to make it look how we want?"
Status: Open question
```
Source: barreletics-decisions-2026-07-09.json (Section 29)

### I-012: JudgeMe Reviews — Display Images, Multiple Layouts
```
Decision: "this has to be updated in judgeme. We would also need to display images. Maybe we have more than one layout?"
Status: Open question
```
Source: barreletics-decisions-2026-07-09.json (Section 06)

---

## COMPONENT PLACEMENT RULES

```
ALWAYS:
- Ticker always top (above header)
- Hero directly below header
- Pillar strip after hero (all pages)
- Reviews near bottom (builds trust before checkout)
- Guarantee last before footer (reduces friction at decision point)

NEVER:
- Two different slogans in same section
- Multiple benefit grids on same page
- Sock Math + other comparison sections together
- Hamburger + horizontal nav simultaneously
```
Source: docs/04-COMPONENT-LIBRARY.md (lines 1034–1048)

---

## PAGE ARCHITECTURE DECISIONS

### Home Page — Matured Direction (13 Sections)
```
1. Announcement ticker
2. Header
3. Hero (media split)
4. Pillar strip
5. Why-it-works
6. Variant grid
7. Coperni + Free People association strip
8. Sock-math
9. Testimonial
10. Founder note
11. Disciplines index
12. Closing statement
13. Footer
```
Supersedes: Live site's 20+ section layout; v2–v11 alternatives
Source: docs/03-DESIGN-SYSTEM.md (Home section order)

### Home Page — Component Library Version (16 Sections)
```
Ticker → Header → Hero → Pillar strip → Split 1 → Product grid → Promo tiles → Sock Math → Split 2 → Disciplines → Split 3 → Reviews → Coperni → Journal → Guarantee → Newsletter/FAQ/Social/Footer
```
Note: May reflect pre-matured version. Differs from matured direction.
Source: docs/04-COMPONENT-LIBRARY.md (lines 931–947)

### PDP — Matured Direction (10 Sections)
```
1. Ticker + header
2. Gallery / buy box split (sticky)
3. Variant + size picker
4. Trust row
5. Pillar strip
6. "Sock vs. skin" comparison (editorial)
7. Spec / materials accordion
8. Reviews (3 quotes + "read all")
9. Cross-sell (3-up)
10. Footer
```
Source: docs/03-DESIGN-SYSTEM.md (PDP section order)

### Collection — Matured Direction (7 Sections)
```
1. Ticker + header
2. Collection hero
3. Sole-type chooser
4. Filter row (inline chips)
5. Product grid (editorial break every 9 cards)
6. Footer
```
Source: docs/03-DESIGN-SYSTEM.md (Collection section order)

### Articles — Shared Rules
```
720px content column, JetBrains Mono eyebrows, H2=36px, body=18px, 32–48px paragraph spacing, pull-quotes on hairlines (no quote-marks SVG).
```
Source: docs/03-DESIGN-SYSTEM.md (Articles section)

---

## IMPLEMENTATION ROADMAP SUMMARY

```
Date: July 9, 2026
Source: Section Decision Matrix (23 sections reviewed)

Keep: 4 sections (01, 03, 09, 17)
Refactor: 14 sections (06, 07, 08, 10, 12, 13, 14, 18, 19, 20, 21, 23, 26, 27, 28)
Undecided: 5 sections (04, 15, 24, 25, 29)

Timeline: 6-week sprint
- Week 1: Keep sections
- Week 2–3: High-priority refactors
- Week 4–6: Medium/light + clarifications
```
Source: IMPLEMENTATION-ROADMAP-Jul2026.md

---

## SOURCE CONFLICTS REGISTER

| ID | Conflict | Source A | Source B | Status |
|----|----------|----------|----------|--------|
| C-001 | Button radius: 0px vs 6px | Research Bible/Design System → 0px | PDP mock → 6px | Needs resolution |
| C-002 | Eyebrow letter-spacing: 0.14em vs 0.08em | Research Bible + Component Library → 0.14em/700 | Design System + Homepage CSS → 0.08em/600 | Needs resolution |
| C-003 | PDP review card radius: 0–4px vs 12px | Design System → 0–4px max | PDP mock → 12px | Needs resolution |
| C-004 | PDP text color: #050505 vs #1c1916 | Design System → #050505 | PDP mock → #1c1916 | Needs resolution |
| C-005 | PDP CTA coral hover vs restraint rule | D-004 → coral is cart-badge-only | PDP mock → CTA hovers to coral | Needs resolution |
| C-006 | Color naming: production vs design | Shopify → Black, LightGrey, etc. | Design system → Onyx, Stone | Timeline TBD |
| C-007 | Product title: SEO vs brand | Shopify → "Best Grippy Shoes..." | Design → "Studio Performance Skin..." | Timeline TBD |
| C-008 | Yoga Tight compare-at: missing in API | Shopify API → $89 only | Live site → $89 sale / $129 compare-at | Data quality issue |
| C-009 | Roadmap colors vs DS tokens | Roadmap → warm #eae5da, terracotta #c45c3f | DS → white #fff, coral #f97250 | Later/divergent decision? |
| C-010 | Free shipping: $75 vs $150 | Old docs reference $75 | Live site + KB → $150 | RESOLVED — $150 is current |

Cross-reference: docs/09-PRODUCT-KNOWLEDGE.md (Source Conflicts Register), docs/03-DESIGN-SYSTEM.md (Source Conflicts section)

---

---

## REPOSITORY RECONCILIATION

### R-001: PDP Design History Imported

**Date:** 2026-07-13  
**Decision:** Import PDP Complete v37–v49 from Claude Design into repository  
**Rationale:** Repository contained only v36; 13 versions of approved design evolution were missing. PDP Complete v49 is now the authoritative production design.  
**Location:** archive/pdp-history/ (v37–v49), docs/history/PDP-Revision-History.md  
**Impact:** docs/05-PDP-ARCHITECTURE.md source authority updated to reference v49  
**Supersedes:** Barreletics-PDP-v36-Jul2026.html is now SUPERSEDED (retained for historical reference)  
**Previous artifacts remain:** All earlier PDP versions (v1–v36) preserved at their existing locations  
**Source:** Claude Design export, July 13, 2026

---

**STATUS:** PENDING REVIEW  
**BUILD COMPLETE:** 2026-07-13
