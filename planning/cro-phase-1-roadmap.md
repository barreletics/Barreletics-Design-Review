# CRO Phase 1 — Conversion Rate Optimization Roadmap

---
document: CRO Phase 1 Roadmap
version: 1.0
status: ⚪ Planning
created: 2026-07-19
depends_on: [02, 07, 11, 12, MILESTONES-4-5-6-ROADMAP]
---

## Overview

This document defines the complete CRO strategy for Barreletics post-launch. It covers friction identification, testing priorities, and a 50+ experiment roadmap — all within brand guardrails (no fake urgency, no shaming, educate/elevate/simplify).

**Primary goal:** Increase revenue per session across all traffic sources.
**Measurement anchor:** Shopify orders as ground truth, GA4 as behavioral signal.

---

## 1. Complete Friction Audit

### Discovery → Homepage

| Friction Point | Severity | Detail |
|---|---|---|
| 5-second comprehension | High | First-time visitors see "The Pilates Sock Era Is Over" — assumes they know what grip socks are and why that matters. Zero context for non-sock-buyers. |
| Category confusion | Medium | "Performance Skins" vs "Grippy Shoes" — nav says one thing, hero says another. New visitors may not connect these as the same product. |
| Hero CTA is generic | Medium | "Shop Now" doesn't communicate value. No specificity about what they're shopping for or why. |
| Mobile hero image below fold | High | On mobile (grid stacks), the product image is below the first screen. Visitors see only text + a generic CTA before scrolling. |
| Value strip visibility | Low | Value propositions (360° grip, Ships 1–2 days, Made in USA) sit below the hero — requires scroll to reach on all devices. |
| No video on first visit | Medium | Complex new product category without a demonstration video above the fold. Users don't see the product in action. |

### Collection Page

| Friction Point | Severity | Detail |
|---|---|---|
| Open vs Closed decision paralysis | High | Two sole types at same price — sole cards show images + short text but no clear "pick this if…" decision framework. Users who don't understand the difference may bounce. |
| No filtering by discipline | Medium | Nav offers Open/Closed/Outdoor but not by use case (Barre, Reformer, Lagree). Users self-identify by discipline, not sole architecture. |
| Quick Add bypasses variant selection | Medium | Product card "Add to Cart" adds default variant — user may not realize they haven't selected their size or color. |
| Price visible before value | Medium | $74 appears on product cards before the user understands why this costs 5× a grip sock. No context for the number. |
| Compare Styles link placement | Low | "Compare Styles" lives in the sub-nav but not prominently on the collection page itself where the decision is happening. |

### PDP (Product Detail Page)

| Friction Point | Severity | Detail |
|---|---|---|
| Price shock without anchoring | High | $74 price block appears before any cost-per-class or sock-replacement math. First-time visitors see the number without context. |
| Only 2 sizes (M and L) | High | Limited sizing with no upfront reassurance. Users with small or wide feet may assume product won't fit and leave. Size ranges are in small text inside buttons — easy to miss on mobile. |
| Reviews below fold | Medium | Star rating row says "Trusted by 1,000+ Instructors" with a "Reviews →" link, but actual review content is far down-page. Social proof isn't reinforcing at the point of purchase decision. |
| Color swatch size on mobile | Medium | Swatches are 23×23px (content-box) + 9px padding = ~41px. Borderline for touch targets. Close spacing (6px gap) increases mis-tap risk. |
| Accordion content hidden by default | Medium | Description, Care, Shipping, Returns all collapsed. Key decision information requires interaction to reveal. |
| No video in gallery | Medium | Only static images in gallery. No movement, no "in-action" footage at the product level. |
| Installments messaging is subtle | Low | "or 4 payments · free shipping over $150" is small text below the price — Shop Pay/Afterpay not explicitly named. |
| Size guide opens new page | Low | "Size Chart →" navigates away from PDP. Any navigation away from the buy decision creates cart abandonment risk. |

### Variant Selection

| Friction Point | Severity | Detail |
|---|---|---|
| Color + Size as sequential choices | Medium | User must make two decisions (color then size). If either feels uncertain, it blocks the ATC. |
| No "help me choose" pathway | Medium | No quiz, no guided selection for users unsure between Open/Closed sole types. |
| Size button states for unavailable | Low | Unavailable sizes get `opacity: 0.35` + strikethrough but no "notify me" option. Dead ends create frustration. |
| No fit guarantee messaging at selection | Medium | 30-day returns and free size exchanges aren't surfaced at the moment of size anxiety. They're hidden in an accordion below. |

### Add to Cart → Cart Drawer

| Friction Point | Severity | Detail |
|---|---|---|
| Cart drawer lacks product image context | Low | Images are small (80×80). On mobile, hard to verify you added the right color/size. |
| $150 free shipping threshold | High | Average order is $74 (single pair). Free shipping requires 2+ pairs. Progress bar starts at 0% — shows $76 remaining, which feels like a barrier rather than motivation. |
| No cross-sell at cart level | Medium | Cart drawer shows items + checkout. No "Complete your collection" or "Studio + Outdoor pairing" suggestions. |
| Discount code not visible | Medium | SAVE15 (Buy 2 Save 15%) isn't mentioned in cart. Users who don't know about it miss the incentive to add a second pair. |
| Two-step checkout (View Full Cart + Checkout) | Low | Cart drawer has both "View Full Cart" and "Checkout" links. Which should they click? |

### Cart → Checkout (Shopify)

| Friction Point | Severity | Detail |
|---|---|---|
| Transition to Shopify checkout | Medium | Visual brand continuity breaks at checkout. Different fonts, colors, spacing. |
| Express checkout options visibility | Medium | Apple Pay / Google Pay / Shop Pay positioning — if not prominently placed, mobile users add friction by entering card details. |
| Guest checkout friction | Low | Shopify's "create account" prompts can interrupt purchase flow for first-time buyers. |
| Shipping estimate surprise | Medium | If user is under $150, seeing a shipping cost at checkout they didn't expect creates abandonment. |

---

## 2. CTA Audit

### Homepage CTAs

| CTA | Current Text | Placement | Issues | Recommendation |
|-----|---|---|---|---|
| Hero Primary | "Shop Now" | Hero copy section, above fold on desktop | Generic. Doesn't tell user what they're shopping for or create urgency through value. | Test: "Shop Grippy Shoes — $74" / "Replace Your Grip Socks" / "See the Difference" |
| Hero Secondary | "See Why →" | Below primary CTA | Vague. No indication of what they'll see. | Test: "Watch 30 Seconds" / "How It Works" / "Compare to Grip Socks" |
| Value Strip | None (informational) | Below hero | Missed opportunity — value props without action | Consider adding micro-CTAs or making strip clickable |
| Social Proof | "Read all reviews →" | Reviews section header | Good placement, small font (12px). Easy to miss. | Increase prominence, test "294 Reviews →" |
| Newsletter | "Get 10% off" | End of page | Good specificity. But page-bottom placement means low visibility unless user scrolls fully. | Test popup timing, test sticky footer bar |
| Sock Math CTA | "Shop Barreletics →" | End of Sock Math section | After compelling comparison content — good context. | Test "Get Yours — $74" / "One Pair. Done. →" |

### PDP CTAs

| CTA | Current Text | Placement | Issues | Recommendation |
|-----|---|---|---|---|
| Primary ATC | "Add to Cart — $74" | Buy box, below size selection | Strong — includes price, action-oriented. Good. | Test "Add to Bag" / "Get Yours — $74" / "Add to Cart" (no price) |
| Sticky ATC | "Add to Cart — $74" | Fixed bottom bar when buy box scrolls out | Effective pattern. Mobile: product info hidden, only size + button visible. | Test adding color swatch preview to sticky |
| Size Chart | "Size Chart →" | Inline with size selector | Text link, small. Not styled as button. | Test modal instead of page navigation |
| Reviews Link | "Reviews →" | Rating row in buy box | Small link (12px). Under-emphasized. | Test "294 Reviews" with star icons as clickable |

### Collection CTAs

| CTA | Current Text | Placement | Issues | Recommendation |
|-----|---|---|---|---|
| Quick Add | "Add to Cart" | Below product card content | Outlined button, good size. But adds default variant without selection. | Test "Quick Add — $74" / "Choose Options" for multi-variant products |
| Compare Link | Sub-navigation only | Top of page in nav | Not visible when browsing product grid | Test inline "Compare Open vs Closed" card within grid |

### Cart CTAs

| CTA | Current Text | Placement | Issues | Recommendation |
|-----|---|---|---|---|
| Checkout | "Checkout" | Cart drawer footer | Primary button style. Good. | Test "Secure Checkout" / "Checkout — $74" (with total) |
| View Full Cart | "View Full Cart" | Above checkout button | Creates decision paralysis — two paths to same goal | Test removing or de-emphasizing |
| Empty Cart | "Shop Grippy Shoes" | Empty cart state | Good — directs to collection | Fine as-is |

### Mobile CTA Sizing Audit

| CTA | Tap Target | Thumb Zone | Pass? |
|-----|---|---|---|
| Hero Primary | Full btn (18px padding) | Upper-middle | ✓ |
| ATC (PDP) | Full width, 18px padding | Lower section | ✓ |
| Sticky ATC | flex: 1 on mobile | Bottom fixed (ideal thumb zone) | ✓ |
| Checkout (Cart) | Full width, 16px padding | Bottom of drawer | ✓ |
| Color Swatches | ~41px diameter | Mid-page | ⚠️ Borderline |
| Size Buttons | 14px padding, grid layout | Mid-page | ✓ |

---

## 3. Mobile Conversion Audit

### First Screen Impression (375px–428px)

**What users see without scrolling:**
- Announcement strip (rotating: SAVE15, Free Shipping, Returns/USA)
- Header (Logo, hamburger, cart icon)
- Hero copy: eyebrow, headline, body, CTAs
- Partial hero image (if any — depends on copy length)

**What's missing from first screen:**
- Product imagery (stacks below on mobile)
- Price context
- Social proof
- Any product demonstration

**Recommendation:** Test mobile-first hero with image-first layout or overlay text on image.

### Thumb-Zone Analysis

| Element | Position | Thumb-Friendly? | Notes |
|---|---|---|---|
| Hamburger menu | Top-left | ❌ Requires stretch | Standard pattern but not ideal for one-handed use |
| Cart icon | Top-right | ❌ Requires stretch | Same — standard but not optimal |
| Hero CTA | Upper-middle area | ⚠️ Depends on copy length | May require scroll to reach |
| Sticky ATC | Bottom-fixed | ✅ Ideal | Perfect thumb zone |
| Color swatches (PDP) | Mid-page | ✅ Natural resting zone | Good — but tight spacing |
| Size buttons (PDP) | Mid-page | ✅ Natural resting zone | Good — adequate padding |
| Cart drawer Checkout | Bottom of drawer | ✅ Good | Natural thumb position |

### Scroll Depth to CTA

| Page | First CTA | Scroll Required (Mobile) |
|---|---|---|
| Homepage | Hero "Shop Now" | ~200px (minor scroll if headline is long) |
| Collection | Product card Quick Add | ~500px (below hero + sole cards) |
| PDP | ATC button | ~800–1000px (below gallery, rating, title, price, variants) |
| PDP (Sticky) | Sticky ATC | 0px once triggered (appears when buy box exits viewport) |

### Mobile-Specific Issues

1. **Gallery on PDP:** Single image with thumbs below. No swipe gesture for mobile gallery — users must tap thumbnails. Swipe is the expected mobile pattern.
2. **Cart drawer width:** `max-width: 90vw` — good. But `420px` fixed width means content is comfortable.
3. **Accordion tap targets:** `<summary>` elements have 14px vertical padding. Combined with text, total height ~48px. Acceptable.
4. **Newsletter form:** Stacks vertically on mobile (good). Email input + button are separate — OK.
5. **Font sizes on mobile:** Hero title drops to 34px, PDP name to `--text-3xl`. Readable.
6. **Page weight concern:** Multiple full-res images (product gallery up to 800w), Sock Math section graphics, social proof section. Cumulative mobile load time needs monitoring.

### Back Button Behavior

- Cart drawer: Close on overlay tap or × button. Back button may navigate away from page entirely (browser default). No explicit back-button trap for drawer.
- PDP → Collection: Standard browser back. No SPA interference.
- Checkout: Shopify manages. External to theme control.

---

## 4. Heatmap Strategy (Microsoft Clarity)

### Configuration Requirements

Clarity is integrated (`snippets/clarity.liquid`). Define smart events and tag pages for segmented analysis.

### Homepage Heatmaps

| Metric | Expected Behavior | Problem Indicator | Action |
|---|---|---|---|
| Click map | Clicks on hero CTA, product cards, nav items | Clicks on non-interactive elements (hero image, value strip text) | Make clicked elements interactive or add CTAs |
| Scroll depth | 60-70% reach Sock Math, 40% reach reviews | <30% reach Sock Math | Move value content higher, shorten hero |
| Rage clicks | None expected | Rage clicks on value strip items or hero image | Add links/CTAs to those elements |
| Dead clicks | None expected | Clicks on review stars (non-linked), discipline icons | Link those elements to relevant pages |

### Collection Page Heatmaps

| Metric | Expected Behavior | Problem Indicator | Action |
|---|---|---|---|
| Click map | Clicks on product cards, sole comparison cards, Quick Add | High clicks on sole card images (not linked) | Make sole cards clickable to sub-collections |
| Scroll depth | 80%+ reach first product row | <50% scroll past hero section | Shorten hero, move products higher |
| Attention | Concentration on product images and prices | Attention on sole comparison without clicking either | Decision paralysis — add "Help me choose" |
| Rage clicks | None | Rage clicks on product images or sole cards | Ensure all expected links work |

### PDP Heatmaps

| Metric | Expected Behavior | Problem Indicator | Action |
|---|---|---|---|
| Click map | Color swatches, size buttons, ATC, accordions | High clicks on price area, gallery images (non-interactive) | Add lightbox to gallery, consider anchoring near price |
| Scroll depth | 90%+ reach ATC button | <70% reach ATC | Content above ATC is too long — condense |
| Rage clicks | None | Rage on size buttons (OOS), swatches, gallery | Improve OOS messaging, fix swatch states |
| Dead clicks | None | Clicks on trust row items (not linked) | Consider linking trust items to policy pages |
| Accordion engagement | 20-30% open at least one | <10% engagement | Consider making Description open by default |

### Cart Drawer Heatmaps

| Metric | Expected Behavior | Problem Indicator | Action |
|---|---|---|---|
| Click map | Checkout button, quantity controls, close | High clicks on "View Full Cart" vs Checkout | Remove/de-emphasize View Full Cart |
| Scroll depth | N/A (drawer is short) | Users scroll within item list | Consider cart summary at top |
| Exit pattern | Overlay click to close, then continue shopping | Close button clicks + no return | Cart anxiety — add trust messaging |

---

## 5. Scroll Depth Analysis Plan

### Homepage

| Section | Approx. Position | Priority Content? | Conversion Impact |
|---|---|---|---|
| Hero (headline + CTAs) | 0–75vh | ✅ Critical | High — first impression, primary CTA |
| Value Strip | 75–85vh | ✅ High | Medium — trust signals |
| Disciplines Section | 85–150vh | Medium | Medium — use-case education |
| Fifty-Fifty (educational) | 150–220vh | Medium | Low-Medium — builds understanding |
| Sock Math | 220–320vh | ✅ Critical | High — price justification + comparison |
| Social Proof / Reviews | 320–400vh | ✅ High | High — social validation |
| Newsletter | 400–450vh | Low | Medium — list building |

**Key Insight:** Sock Math (the primary price-justification content) sits at ~3× viewport height. Converting visitors who need price justification must scroll 3 full screens. This is too far.

**Recommendation:**
- Move Sock Math section above Social Proof (or inline a micro-version into the hero/value-strip area)
- Test condensed "one pair replaces $144/year in socks" messaging above the fold
- Consider removing or shortening Disciplines section on homepage if scroll depth shows low engagement

### Collection Page

| Section | Approx. Position | Priority Content? | Conversion Impact |
|---|---|---|---|
| Collection Hero + Sole Cards | 0–60vh | ✅ Critical | High — orientation + decision support |
| Product Grid (first row) | 60–120vh | ✅ Critical | High — products visible |
| Product Grid (remaining) | 120–250vh | Medium | Medium — browsing continues |
| Related content / trust | 250vh+ | Low | Low |

**Recommendation:** First product should be visible without scrolling on both mobile and desktop.

### PDP

| Section | Approx. Position (Mobile) | Priority Content? | Conversion Impact |
|---|---|---|---|
| Gallery | 0–100vh | ✅ Critical | High — product visualization |
| Rating + Title + Price | 100–130vh | ✅ Critical | High — establishes context |
| Variant Selection | 130–180vh | ✅ Critical | High — required for purchase |
| ATC Button | 180–200vh | ✅ Critical | High — the conversion action |
| Trust Row | 200–210vh | High | Medium — risk reduction |
| Accordions | 210–280vh | Medium | Low-Medium |
| Sock Math | 280–380vh | High | Medium — reinforces value |
| Reviews | 380–480vh | High | Medium — social proof |
| Recommendations | 480vh+ | Low | Low — cross-sell |

**Key Insight:** On mobile, ATC is approximately 2 full screens down. The sticky ATC compensates, but users who haven't scrolled to ATC yet haven't completed variant selection. Sticky ATC uses the pre-selected variant — potential wrong-size-adds.

---

## 6. Exit Intent Strategy

### Brand Guardrails (Non-Negotiable)

Per Doc 02:
- ❌ No countdown timers
- ❌ No "Only X left in stock" (unless real-time, truthful inventory)
- ❌ No pressure tactics or manipulative language
- ❌ No first-visit discount popups (devalues brand at $74 price point)
- ❌ No competitor shaming
- ✅ Educate, elevate, simplify

### Desktop Exit Intent (Mouse Toward Chrome)

| Visitor Segment | Trigger | Content | Goal |
|---|---|---|---|
| First-time, homepage | Mouse to browser chrome, >30s on page | "Curious how one pair replaces your grip socks?" + educational content link | Move to consideration (Collection or Compare page) |
| First-time, PDP viewed | Mouse to chrome, viewed PDP but no ATC | "Questions about sizing? We're here to help." + size guide link + live chat | Remove sizing uncertainty |
| Cart abandoner | Mouse to chrome, items in cart | "Your cart is saved." + free shipping reminder if close to $150 | Reduce urgency to decide now, enable return |
| Returning visitor, no purchase | Mouse to chrome, 2+ sessions | "Still researching? See what 294 reviewers say." + reviews link | Social proof push |

### Mobile Exit Intent (Back Button / Tab Switch)

Mobile exit intent is less reliable. Recommended approach:

| Trigger | Content | Implementation |
|---|---|---|
| Back button on PDP | None — respect the navigation | Don't trap. Let them go. |
| Tab switch (visibility change API) | None on first occurrence | Track for analytics, don't interrupt |
| Cart page inactivity (>60s) | Subtle: "Need help? Chat with us." (Tidio trigger) | Non-intrusive, support-oriented |

### What NOT to Build

| Tactic | Why Not |
|---|---|
| Spin-to-win discount wheels | Devalues $74 premium positioning |
| "Wait! Don't go!" overlays | Aggressive. Violates brand tone. |
| Countdown timers on offers | Fake urgency. Brand guardrail violation. |
| "X people viewing this" notifications | Manipulation. Not authentic to Barreletics. |
| Email-gate before any content | Barrier creates friction, not trust |

---

## 7. Trust Optimization Opportunities

### Current Trust Signals Inventory

| Signal | Current Placement | Visibility | Effectiveness |
|---|---|---|---|
| Made in USA | Trust row (PDP), Value strip (Home), Announcement strip | Medium — requires scroll on PDP | High — differentiator for $74 price |
| 30-day returns | Trust row (PDP), Accordion (PDP), Announcement strip | Low — hidden in accordion detail | High — risk reducer |
| 90-day warranty | Trust row (PDP), Accordion (PDP) | Low | Medium |
| 360° grip claim | Value strip, Sock Math, Hero body | Medium | High — core differentiator |
| Ships 1–2 days | Trust row (PDP), Value strip | Medium | Medium |
| 4.9★ / 294 reviews | Social proof section, PDP rating row | Medium | High — but actual reviews are far down-page |
| "Trusted by 1,000+ Instructors" | PDP rating row | Low (small text) | High — authority signal |
| Latex & silicone free | Trust row (PDP) | Low | Medium — safety for sensitive users |
| $74 replaces $144/yr | Sock Math section | Low (far down page) | High — value justification |
| Free shipping over $150 | Announcement strip, Price meta, Cart drawer | Medium | Mixed — also creates friction |

### Trust Gaps (What's Missing)

| Missing Signal | Expected Impact | Recommended Placement |
|---|---|---|
| Review snippets near ATC | High | 2-3 short quotes in buy box area, before ATC |
| Instructor/studio endorsement badges | High | PDP + Collection — "Used in 500+ studios" |
| Patent mention | Medium | PDP trust row — "Patented grip technology" |
| Real customer photo gallery (UGC) | High | PDP below gallery, Collection page |
| "As seen in" press logos | Medium | Homepage below hero, About page |
| Money-back guarantee framing | High | Near ATC — "Love it or return within 30 days" |
| Secure checkout badges | Low | Cart footer, pre-checkout |
| Payment method icons | Low | Cart footer |
| Verified buyer badges on reviews | Medium | Review cards |
| "Free size exchanges" prominently | High | Size selector area — reduces size anxiety |

### Recommended Priority Improvements

1. **Add review micro-quotes to PDP buy box** (above ATC) — highest expected impact
2. **Surface "Free size exchanges" at the size selector** — directly addresses top anxiety
3. **Add "Patented 360° grip" to trust row** — engineering credibility
4. **Move "Trusted by 1,000+ Instructors" to a more prominent visual treatment** — currently undersized text
5. **Add UGC carousel or Instagram feed to PDP** — visual social proof

---

## 8. Cart Abandonment Improvements

### Cart Drawer Analysis

**Current state:** Clean, functional drawer with item list, shipping progress bar, subtotal, and checkout CTA. Missing several conversion-positive elements.

| Gap | Impact | Recommendation |
|---|---|---|
| No cross-sell | Medium | Show "Complete Your Collection" — if Open Sole in cart, suggest Closed Sole (and vice versa) |
| SAVE15 not surfaced | High | If cart has 1 pair: show "Add a second pair — save 15% with code SAVE15" |
| Free shipping bar feels punitive | Medium | At $74 (one pair): bar shows ~49% progress. Feels far from goal. Reframe: "Add one more pair for free shipping + 15% off" |
| No trust messaging in cart | Low | Add micro-trust line: "30-day returns · Free exchanges · Made in USA" |
| No estimated delivery | Medium | Show "Estimated delivery: [date]" based on shipping speed |
| No urgency (authentic) | Low | If inventory is genuinely low on selected variant, show "Only X left in [Color/Size]" |

### Free Shipping Threshold Strategy ($150)

**The problem:** AOV for a single pair is $74. Free shipping at $150 requires exactly 2 pairs ($148 doesn't qualify) or a pair + apparel.

**Options:**

| Strategy | Pros | Cons | Recommendation |
|---|---|---|---|
| Lower threshold to $100 | Achievable with 1 pair + accessory | Reduces shipping revenue | ❌ Not recommended without margin analysis |
| Keep $150, better framing | No revenue impact | Still 2-pair minimum | ✅ Frame as "Free shipping when you buy 2" |
| Show savings stacked | Motivating | Complexity | ✅ "Buy 2: Save 15% ($22.20) + Free Shipping ($X)" |
| Remove threshold | Simplest experience | Margin impact | ❌ Not recommended without data |

**Recommended approach:** Keep $150 threshold but reframe messaging. Instead of "You're $76 away from free shipping" → "Add a second pair: save 15% + free shipping."

### Abandoned Cart Recovery

| Channel | Strategy | Timing | Content |
|---|---|---|---|
| Email #1 | Cart reminder | 1 hour | "Your [Color] [Style] is saved. Still deciding? Here's what 294 customers say." + review snippet |
| Email #2 | Value reinforcement | 24 hours | "One pair replaces $144/year in grip socks." + Sock Math visual |
| Email #3 | Support offer | 72 hours | "Questions about sizing or fit? Reply to this email — we'll help." |
| Retargeting (Meta) | Dynamic product ad | 1–7 days | Product image + review quote + "Still gripping after 1,000+ classes" |
| Retargeting (Pinterest) | Lifestyle pin | 3–14 days | Studio action shot + "The grip sock replacement" |

### Cart Persistence

- Shopify native: Cart persists via cookie for 14 days (logged out) or indefinitely (logged in)
- Cross-device: Requires account. Consider "Email my cart" feature for non-account users.
- Session restore: Ensure cart drawer shows correct state on return visit.

---

## 9. Bundle Strategy

### Bundle 1: Studio Duo (Open Sole + Closed Sole)

| Aspect | Detail |
|---|---|
| Value proposition | "One for barefoot feel. One for full coverage. Your complete studio kit." |
| Pricing | $148 → $125.80 (15% off with SAVE15) + free shipping (hits $150 with original price logic) |
| Implementation | Shopify automatic discount (buy 2 any Grippy Shoes = 15% off). Already exists via SAVE15. |
| AOV impact | +100% (doubles order from $74 to $148) |
| Messaging | "Most customers own both — Closed for reformer days, Open for barre." |

### Bundle 2: Multi-Pair Same Style (2+ of same)

| Aspect | Detail |
|---|---|
| Value proposition | "One for the studio bag. One for home practice." |
| Pricing | Same 15% off (SAVE15) |
| Implementation | Already supported |
| AOV impact | +100% |
| Messaging | "A second pair means one is always ready." |

### Bundle 3: Gift Bundle

| Aspect | Detail |
|---|---|
| Value proposition | "The gift every studio-goer actually wants." |
| Pricing | Performance Skin + digital gift card ($25) = custom bundle price TBD |
| Implementation | Shopify native product bundle or manual bundling via cart script |
| AOV impact | +30-50% |
| Messaging | Seasonal — holiday, Mother's Day, instructor appreciation |

### Bundle 4: Grippy Shoes + Apparel

| Aspect | Detail |
|---|---|
| Value proposition | "Head-to-toe studio performance." |
| Pricing | Grippy Shoes + Yoga Tights (or similar) — bundle discount TBD |
| Implementation | Cross-category automatic discount or manual code |
| AOV impact | +40-80% depending on apparel price |
| Messaging | "Complete the look" — shown at cart level as cross-sell |

### Bundle 5: Studio Starter (Future — Post Sock Launch)

| Aspect | Detail |
|---|---|
| Value proposition | "Performance Skin + Barreletics Socks — the complete system." |
| Pricing | TBD pending sock pricing |
| Implementation | Product bundle when socks launch |
| AOV impact | TBD |
| Messaging | "Designed to work together." |

**Note:** Bundle 5 references an Upcoming product (Barreletics Socks). Do not implement or reference publicly until owner authorizes.

---

## 10. A/B Testing Roadmap

### Scoring System

Priority Score = (Revenue Impact × 3) + (Confidence × 2) − (Dev Effort × 1)

| Rating | Value |
|---|---|
| High (H) | 3 |
| Medium (M) | 2 |
| Low (L) | 1 |

**Maximum score:** (3×3) + (3×2) − (1×1) = 14
**Minimum score:** (1×3) + (1×2) − (3×1) = 2

---

### Homepage Experiments (12)

| # | Experiment | Page | Hypothesis | Primary Metric | Revenue Impact | Dev Effort | Confidence | Priority Score |
|---|---|---|---|---|---|---|---|---|
| H-01 | Hero headline: "The Pilates Sock Era Is Over" vs "One Pair Replaces All Your Grip Socks" vs "360° Grip. $74. Done." | Homepage | More specific, benefit-driven headlines will increase click-through to collection | Collection page entries from hero CTA | H | L | H | 14 |
| H-02 | Hero CTA: "Shop Now" vs "Shop Grippy Shoes — $74" vs "See the Difference" | Homepage | Specific CTAs with price or benefit will outperform generic "Shop Now" | Hero CTA CTR | H | L | H | 14 |
| H-03 | Add video to hero (product demo or studio footage) replacing static image | Homepage | Video demonstration will increase engagement and scroll depth for new visitors | Bounce rate, scroll depth, collection entry rate | H | M | M | 11 |
| H-04 | Move Sock Math section from position 4 to position 2 (directly after hero) | Homepage | Earlier price justification will reduce bounce rate for price-sensitive visitors | Bounce rate, session duration | H | L | M | 12 |
| H-05 | Value strip content order: lead with "One pair replaces $144/yr in socks" instead of "360° locked grip" | Homepage | Cost savings message has higher urgency than technical feature | Scroll depth past value strip | M | L | M | 9 |
| H-06 | Social proof section: move from bottom to position 3 (after hero + value strip) | Homepage | Earlier social proof will validate the category-creation message and reduce skepticism | Scroll depth, PDP entry rate | M | L | H | 11 |
| H-07 | Add "As Seen In" press logo bar below hero | Homepage | Third-party credibility signals will increase trust and reduce bounce | Bounce rate | M | M | L | 5 |
| H-08 | Newsletter popup at 60s vs 30s vs scroll-triggered (50% depth) | Homepage | Later/scroll-triggered popup will have higher conversion rate due to engagement context | Email signup rate | L | L | H | 8 |
| H-09 | First-screen optimization: product image above copy on mobile | Homepage | Showing the product immediately on mobile will reduce bounce | Mobile bounce rate | H | M | H | 13 |
| H-10 | Category navigation prominence: add "Open Sole vs Closed Sole" visual cards in hero area | Homepage | Clearer path to decision will increase collection entries | Collection page entries | M | M | M | 7 |
| H-11 | "Why not socks" messaging: comparison list above fold vs below | Homepage | Visible category-disruption messaging will increase engagement for grip-sock searchers | Session depth, PDP entries for organic search traffic | H | L | M | 12 |
| H-12 | Announcement strip: static vs rotating, content order testing | Homepage | Static "Buy 2 Save 15%" may outperform rotation (message visibility) | Multi-pair purchase rate | M | L | M | 9 |

### Collection Experiments (11)

| # | Experiment | Page | Hypothesis | Primary Metric | Revenue Impact | Dev Effort | Confidence | Priority Score |
|---|---|---|---|---|---|---|---|---|
| C-01 | Grid layout: 2 columns vs 3 columns on desktop | Collection | 2-column shows larger images — better for a visual product with few SKUs | Add to cart rate from collection | M | L | M | 9 |
| C-02 | Product card: show "One pair replaces 6–8 grip socks" vs current subtitle | Collection | Value framing on card will outperform generic subtitle | Quick Add CTR | H | L | H | 14 |
| C-03 | Quick Add button text: "Add to Cart" vs "Quick Add — $74" vs "Choose Size" | Collection | "Choose Size" will reduce wrong-variant adds and increase PDP visits (higher intent) | Correct-variant ATC rate | M | L | H | 11 |
| C-04 | Sole comparison cards: add "Best for Reformer/Pilates" vs "Best for Barre/Yoga" discipline labels | Collection | Discipline-specific guidance reduces decision paralysis | Time to first product click | H | L | H | 14 |
| C-05 | Add inline "Compare" card in product grid (visual comparison between Open/Closed) | Collection | In-context comparison will reduce bounce from undecided visitors | PDP view rate, bounce rate | M | M | M | 7 |
| C-06 | Collection hero length: current (hero + sole cards) vs condensed (hero only, cards moved to sidebar) | Collection | Showing products faster increases engagement | First product card CTR | M | L | M | 9 |
| C-07 | Trust badges on collection page (below grid): "Made in USA · 30-Day Returns · Free Shipping on 2+" | Collection | Trust signals reinforce purchase confidence before PDP entry | PDP entry rate | M | L | H | 11 |
| C-08 | Sort default: "Best Selling" vs "Newest" vs "Featured" | Collection | Best Selling leverages social proof in product ordering | Conversion rate | L | L | M | 6 |
| C-09 | Add lifestyle images between product cards (every 4th position) | Collection | Lifestyle context increases emotional engagement | Scroll depth, session duration | L | M | L | 2 |
| C-10 | Discipline-specific entry points: "Shop for Barre" / "Shop for Reformer" tabs | Collection | Users self-identify by discipline — matching reduces cognitive load | ATC rate from collection | H | M | M | 11 |
| C-11 | Price visibility: show price on hover only vs always visible | Collection | Always-visible price sets expectation early and reduces PDP price shock | PDP bounce rate | M | L | M | 9 |

### PDP Experiments (16)

| # | Experiment | Page | Hypothesis | Primary Metric | Revenue Impact | Dev Effort | Confidence | Priority Score |
|---|---|---|---|---|---|---|---|---|
| P-01 | Price anchoring: add "Replaces $144/yr in grip socks" next to $74 price | PDP | Visible cost comparison at the price block will reduce price-shock abandonment | ATC rate | H | L | H | 14 |
| P-02 | Review quotes in buy box: add 2-3 micro-testimonials between trust row and ATC | PDP | Proximal social proof increases conversion confidence at decision point | ATC rate | H | L | H | 14 |
| P-03 | Sock Math section: above reviews vs below reviews vs inline (condensed in buy box) | PDP | Closer proximity to purchase decision increases effectiveness of price justification | ATC rate, revenue per session | H | L | M | 12 |
| P-04 | CTA text: "Add to Cart — $74" vs "Add to Bag — $74" vs "Get Yours — $74" vs "Add to Cart" (no price) | PDP | Action-specific language with price confirmation reduces post-click anxiety | ATC rate | M | L | H | 11 |
| P-05 | Size guide: modal overlay vs current page navigation | PDP | Modal keeps user on PDP — avoids navigation-away abandonment | ATC rate for users who click size guide | H | M | H | 13 |
| P-06 | "Free size exchanges" messaging at size selector | PDP | Explicitly stating "wrong size? exchange free" at the anxiety point reduces size-selection abandonment | ATC rate, return rate | H | L | H | 14 |
| P-07 | Image gallery: add swipe gesture on mobile (carousel) vs current thumb-tap | PDP | Swipe matches mobile user expectation — increases image engagement | Image interaction rate, time on PDP | M | M | H | 9 |
| P-08 | Video in gallery: add 15–30s product demo as first or second gallery item | PDP | Video demonstration increases product understanding and confidence | ATC rate, time on PDP | H | M | M | 11 |
| P-09 | Description accordion: open by default vs collapsed (current) | PDP | Key product information visible without interaction increases informed purchases | ATC rate | M | L | M | 9 |
| P-10 | Trust row: current inline text vs icon-based visual treatment (checkmark icons) | PDP | Visual trust signals are more scannable than text-only | ATC rate | L | L | M | 6 |
| P-11 | Sticky ATC: add color swatch indicator + size on mobile (currently hidden) | PDP | Confirming variant in sticky bar reduces wrong-variant purchases and returns | Return rate, correct-variant ATC | M | M | M | 7 |
| P-12 | "Compare styles" link: add to PDP buy box area (between price and variants) | PDP | Users unsure between Open/Closed get easy path to decision content without leaving PDP | Compare page views, reduce PDP bounce for undecided | M | L | M | 9 |
| P-13 | FAQ section: open first question by default, keep rest collapsed | PDP | Most common question gets answered without click — reduces support contacts | Support ticket volume, ATC rate | L | L | H | 8 |
| P-14 | Cross-sell recommendations: "Customers also bought" with Open ↔ Closed pairing | PDP | Product recommendations increase multi-pair purchases | Multi-pair order rate, AOV | H | M | M | 11 |
| P-15 | Urgency via authentic stock: show "[Color] [Size] — Limited stock" when inventory < 5 | PDP | Real inventory scarcity (not fabricated) creates authentic motivation | ATC rate for low-stock variants | M | M | M | 7 |
| P-16 | Installment messaging: "or 4 × $18.50 with Shop Pay" more prominently styled | PDP | Explicit installment breakdown reduces price barrier perception | ATC rate for first-time visitors | M | L | H | 11 |

### Cart Experiments (11)

| # | Experiment | Page | Hypothesis | Primary Metric | Revenue Impact | Dev Effort | Confidence | Priority Score |
|---|---|---|---|---|---|---|---|---|
| K-01 | Free shipping progress bar: reframe "Add a second pair for free shipping + 15% off" | Cart | Positive framing (gain) outperforms negative framing (you're $76 short) | Multi-pair add rate from cart | H | L | H | 14 |
| K-02 | Cross-sell in cart drawer: suggest opposite sole type | Cart | Relevant product suggestion at cart increases AOV | AOV, multi-pair rate | H | M | H | 13 |
| K-03 | Auto-apply SAVE15 on 2+ items vs require manual code entry | Cart | Removing friction of code entry increases multi-pair conversion | Multi-pair checkout rate | H | M | H | 13 |
| K-04 | Remove "View Full Cart" link — single path to checkout | Cart | Eliminating choice reduces decision paralysis | Checkout initiation rate | M | L | H | 11 |
| K-05 | Add trust line in cart footer: "30-day returns · Free exchanges · Secure checkout" | Cart | Trust signals at pre-checkout reduce anxiety-driven abandonment | Checkout completion rate | M | L | H | 11 |
| K-06 | Estimated delivery date in cart: "Arrives by [date]" | Cart | Concrete delivery expectation reduces uncertainty | Checkout initiation rate | M | M | M | 7 |
| K-07 | Upsell message: "Buy 2, save 15%" when cart has 1 item | Cart | Explicit savings opportunity motivates second-pair add | Multi-pair rate | H | L | H | 14 |
| K-08 | Cart drawer vs full cart page as default on mobile | Cart | Drawer keeps user in shopping context — less likely to feel "committed" | Continue shopping rate, checkout rate | M | M | L | 4 |
| K-09 | Express checkout (Apple Pay / Shop Pay) prominence in cart drawer | Cart | Reducing checkout steps for mobile users increases completion | Mobile checkout completion rate | H | M | H | 13 |
| K-10 | "Save for later" functionality in cart | Cart | Users who aren't ready to buy but don't want to lose their selection return at higher rates | Return visit purchase rate | L | H | L | 2 |
| K-11 | Cart drawer: show product image larger (120px vs 80px) | Cart | Better visual confirmation reduces "did I pick the right one?" anxiety | Cart-to-checkout rate | L | L | M | 6 |

### Sitewide Experiments (6)

| # | Experiment | Page | Hypothesis | Primary Metric | Revenue Impact | Dev Effort | Confidence | Priority Score |
|---|---|---|---|---|---|---|---|---|
| S-01 | Announcement strip: static "Buy 2, Save 15%" vs current 3-message rotation | Sitewide | Static high-value message has higher comprehension than rotating content | Multi-pair order rate | M | L | H | 11 |
| S-02 | Navigation label: "Grippy Shoes" vs "Performance Skins" vs "Shop" | Sitewide | Nav label impacts category comprehension and click-through | Nav CTR to collection | M | L | M | 9 |
| S-03 | Footer newsletter: "10% off" vs "Join 5,000+ studio athletes" (social proof framing) | Sitewide | Social proof incentive may outperform discount for premium brand | Email signup rate | L | L | M | 6 |
| S-04 | Exit intent: educational content vs support offer vs no exit intent | Sitewide | Educational exit intent will capture more first-time visitors than support offer | Email capture rate, return visit rate | M | M | M | 7 |
| S-05 | Return visitor personalization: "Welcome back" + recently viewed | Sitewide | Personalized experience increases return-visit conversion | Return visitor conversion rate | M | H | M | 5 |
| S-06 | Tidio chat widget: proactive "Need sizing help?" on PDP after 30s vs passive icon only | Sitewide | Proactive support at anxiety moment increases conversion for uncertain visitors | Chat engagement rate, ATC rate for chat users | M | L | M | 9 |

---

### Total Experiments: 56

---

## Prioritization Matrix

### Tier 1 — Quick Wins (Score 12–14)

Do first. High revenue, low effort, high confidence.

| # | Experiment | Score | Expected Impact |
|---|---|---|---|
| H-01 | Hero headline variants | 14 | Improved first-impression click-through |
| H-02 | Hero CTA specificity | 14 | Higher hero engagement rate |
| C-02 | Product card value framing | 14 | Card-level conversion increase |
| C-04 | Discipline labels on sole cards | 14 | Reduced decision paralysis |
| P-01 | Price anchoring on PDP | 14 | Reduced price-shock abandonment |
| P-02 | Review quotes in buy box | 14 | Higher ATC from social proof proximity |
| P-06 | "Free size exchanges" at selector | 14 | Reduced size-anxiety abandonment |
| K-01 | Reframe shipping bar messaging | 14 | Higher multi-pair add rate |
| K-07 | "Buy 2, save 15%" in cart | 14 | Increased multi-pair conversion |
| H-09 | Mobile: product image first | 13 | Reduced mobile bounce |
| P-05 | Size guide modal (not new page) | 13 | Reduced PDP abandonment |
| K-02 | Cross-sell opposite sole type in cart | 13 | AOV increase |
| K-03 | Auto-apply SAVE15 on 2+ items | 13 | Multi-pair checkout increase |
| K-09 | Express checkout prominence | 13 | Mobile completion rate |

### Tier 2 — Strategic Bets (Score 10–12)

Plan carefully. High revenue but need more development or data.

| # | Experiment | Score |
|---|---|---|
| H-04 | Move Sock Math higher on homepage | 12 |
| H-11 | "Why not socks" above fold | 12 |
| P-03 | Sock Math positioning on PDP | 12 |
| H-06 | Social proof section earlier | 11 |
| C-03 | Quick Add button text change | 11 |
| C-07 | Trust badges on collection | 11 |
| C-10 | Discipline-specific tabs | 11 |
| P-04 | CTA text variants | 11 |
| P-08 | Video in PDP gallery | 11 |
| P-14 | Cross-sell recommendations (PDP) | 11 |
| P-16 | Installment messaging prominence | 11 |
| K-04 | Remove "View Full Cart" | 11 |
| K-05 | Trust line in cart | 11 |
| S-01 | Static announcement strip | 11 |
| H-03 | Hero video | 11 |

### Tier 3 — Incremental Gains (Score 6–9)

Fill testing calendar between strategic tests.

| # | Experiment | Score |
|---|---|---|
| H-05 | Value strip content order | 9 |
| H-12 | Announcement strip testing | 9 |
| C-01 | Grid columns | 9 |
| C-06 | Collection hero condensed | 9 |
| C-11 | Price visibility testing | 9 |
| P-07 | Mobile swipe gallery | 9 |
| P-09 | Description open by default | 9 |
| P-12 | Compare link in buy box | 9 |
| S-02 | Nav label testing | 9 |
| S-06 | Proactive chat trigger | 9 |
| H-08 | Newsletter popup timing | 8 |
| P-13 | FAQ first question open | 8 |
| C-05 | Inline compare card | 7 |
| C-10 | Discipline tabs | 7 |
| K-06 | Estimated delivery in cart | 7 |
| P-11 | Sticky ATC variant info | 7 |
| P-15 | Authentic stock levels | 7 |
| S-04 | Exit intent testing | 7 |

### Tier 4 — Long-Term / Backlog (Score ≤5)

Requires significant effort or low confidence. Defer.

| # | Experiment | Score | Reason |
|---|---|---|---|
| H-07 | "As seen in" press logos | 5 | Requires press coverage assets |
| S-05 | Return visitor personalization | 5 | High dev effort, needs data infrastructure |
| C-08 | Sort default testing | 6 | Low revenue impact |
| C-09 | Lifestyle images in grid | 2 | Low confidence, medium effort |
| K-08 | Drawer vs full page default | 4 | Low confidence |
| K-10 | "Save for later" | 2 | High effort, unproven for this category |
| K-11 | Larger cart images | 6 | Marginal impact |
| P-10 | Trust row icon treatment | 6 | Low revenue impact |
| S-03 | Footer newsletter framing | 6 | Low revenue impact |

---

## Implementation Requirements

### Recommended Testing Tool

| Tool | Pros | Cons | Recommendation |
|---|---|---|---|
| **Shopify Split Testing (native)** | No additional cost, theme-level control | Limited to full-theme A/B only (not section-level) | ❌ Too coarse for section tests |
| **Google Optimize (sunset)** | Free | Discontinued 2023 | ❌ Not available |
| **Convert.com** | Shopify integration, visual editor, strong stats | $$$, adds page weight | ⚠️ Consider for Tier 1/2 |
| **ABConvert (Shopify app)** | Native Shopify app, built for Shopify themes | Limited to specific test types | ⚠️ Budget option |
| **VWO** | Full-featured, good statistical engine | $$$, adds weight | ⚠️ Enterprise option |
| **Custom (Liquid + Shopify Sections)** | Zero additional cost, zero page weight, full control | Requires dev work per test, manual statistics | ✅ Recommended for Tier 1 quick wins |

**Recommended approach:**
1. **Tier 1 Quick Wins:** Custom Liquid implementation (section-level content swapping via theme settings or metafields + GA4 custom events for measurement)
2. **Tier 2 Strategic Bets:** Evaluate Convert.com or VWO for complex multi-page tests requiring statistical rigor
3. **All tiers:** GA4 as measurement backbone (custom dimensions for test variants)

### Statistical Significance Requirements

| Traffic Level | Min Sample per Variant | Test Duration (est.) | Notes |
|---|---|---|---|
| Homepage (~500 sessions/day) | 1,000 per variant | 4–5 days minimum | Must run full week to capture day-of-week effects |
| Collection (~200 sessions/day) | 1,000 per variant | 10–14 days | Run 2 full weeks |
| PDP (~150 sessions/day) | 1,000 per variant | 14–21 days | Most tests will need 2-3 weeks |
| Cart (~50 entries/day) | 500 per variant minimum | 20–30 days | Consider running during promo periods for higher volume |

**Statistical requirements:**
- Confidence level: 95% (p < 0.05)
- Minimum detectable effect: 20% relative lift (given traffic constraints)
- Power: 80%
- Test type: Two-tailed (we don't assume direction of effect)
- Correction: Bonferroni correction for tests with 3+ variants

### Test Duration Rules

1. **Minimum:** 7 days (capture full week of traffic patterns)
2. **Maximum:** 45 days (avoid seasonal drift invalidating results)
3. **Stop rules:** Never stop a test early because one variant "looks good." Commit to minimum sample size.
4. **External factors:** Pause tests during major promotions, site outages, or Meta campaign spikes that skew traffic quality.

### Architecture Compatibility

Tests must not violate the locked architecture (Milestones 1-3). Implementation constraints:

| Allowed | Not Allowed |
|---|---|
| Theme settings content changes (section settings, metafields) | New section files that duplicate existing architecture |
| CSS class additions for variant styling | Modification of design tokens or component structure |
| JavaScript event listeners for tracking | Changes to core JS architecture (variant-selector.js, cart.js) |
| Liquid conditionals for variant rendering | New layout files or template restructuring |
| GA4 custom events and dimensions | Third-party scripts that block rendering |

**How to implement section-level A/B tests without breaking architecture:**
1. Add a `test_variant` setting to the section schema (hidden from theme editor)
2. Use Liquid conditional to render variant A or B content
3. Fire GA4 custom event with variant assignment
4. Measure conversion downstream
5. After winner declared, remove losing variant and test setting

### Measurement Framework

| Metric Type | Metrics | Purpose |
|---|---|---|
| **Primary** | ATC rate, Checkout initiation rate, Purchase rate, Revenue per session | Direct conversion measurement |
| **Secondary** | Bounce rate, Scroll depth, Time on page, Pages per session | Engagement signals |
| **Guardrail** | Return rate, Support tickets, Page load time, Accessibility score | Ensure tests don't degrade experience |
| **Segmentation** | Device (mobile/desktop), Traffic source, New vs returning, Entry page | Identify differential effects |

**GA4 Custom Events for CRO:**
- `cro_variant_assigned` (experiment_id, variant_id)
- `cro_section_viewed` (section_name, scroll_depth)
- `cro_cta_clicked` (cta_id, location, variant)
- `cro_exit_intent_shown` (page_type, visitor_segment)
- `cro_cross_sell_shown` (product_from, product_suggested)
- `cro_cross_sell_added` (product_from, product_added)

---

## Appendix: Testing Calendar (First 90 Days)

### Weeks 1–2: Foundation
- Implement Clarity smart events for baseline heatmaps
- Record 2 full weeks of baseline data (no changes)
- Establish conversion funnel baseline in GA4
- Set up CRO custom events infrastructure

### Weeks 3–4: First Tests (Tier 1 Quick Wins)
- **Test 1:** P-01 + P-02 (price anchoring + review quotes in buy box) — combined since both affect same area
- **Test 2:** K-01 + K-07 (shipping bar reframe + "Buy 2 save 15%" message)

### Weeks 5–6: Continue Quick Wins
- **Test 3:** H-01 + H-02 (hero headline + CTA together)
- **Test 4:** P-06 (free size exchanges at selector)

### Weeks 7–8: Quick Wins + Strategic Start
- **Test 5:** C-02 + C-04 (card value framing + discipline labels)
- **Test 6:** K-03 (auto-apply SAVE15)

### Weeks 9–10: Strategic Bets Begin
- **Test 7:** H-09 (mobile image-first hero)
- **Test 8:** P-05 (size guide modal)

### Weeks 11–12: Strategic Bets + Analysis
- **Test 9:** K-02 + K-09 (cross-sell + express checkout)
- Analyze first 90 days of data
- Re-prioritize based on results
- Document learnings

---

## Document Status

This is a **planning document only** — no code, no implementation. Tests require M4D launch completion and baseline data collection before execution begins.

**Cross-references:**
- Brand guardrails → Doc 02 (Brand System)
- Product knowledge → `planning/07-product-knowledge-base.md`
- Site architecture → `shopify-build/` (sections, snippets, templates)
- Growth platform context → `planning/MILESTONES-4-5-6-ROADMAP.md` §5.9
- Analytics architecture → `docs/15-analytics-architecture.md`
- Variant selection flow → `docs/13-variant-selection-flow.md`
- Cart flow → `docs/14-cart-flow.md`
