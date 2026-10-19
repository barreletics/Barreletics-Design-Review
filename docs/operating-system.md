# Barreletics Operating System

**Status:** Living operations manual  
**Audience:** Any competent executive stepping in without prior Barreletics knowledge  
**Scope:** Run the business for 30 days without founders  
**Type:** Documentation only — no implementation  
**Last updated:** 2026-08-11  
**Canonical facts:** Always defer to `planning/07-product-knowledge-base.md` for product/policy truth

---

## How to Use This Manual

1. Read the **Executive Summary** once.
2. Use the department sections as runbooks.
3. When facts conflict across channels, **Doc 07 wins** — update Doc 07 first, then cascade (`planning/13-knowledge-architecture.md`).
4. Never republish claims listed in `planning/RETIRED_CLAIMS.md`.
5. Escalate per Section 21 / `planning/DECISION_FRAMEWORK.md`.

---

## EXECUTIVE SUMMARY

### What Barreletics Is

Barreletics makes **Studio Performance Skins** — injection-molded, 360° grip performance footwear that replaces disposable grip socks for barre, Reformer Pilates, Lagree/Megaformer, Cadillac, and yoga. Positioning: big like Nike, refined like Alo, smart like Tesla. Made in USA. DTC primary; wholesale and studio partnerships secondary.

### Category Creation Strategy

We do not compete inside the grip sock category. We make grip socks irrelevant. Every asset should move customers from “Which grip sock should I buy?” to “Why am I still wearing grip socks?” This governs website, ads, email, support, wholesale, SEO, and AI systems (`planning/01-brand-north-star.md`, `planning/02-brand-system.md`).

### Current Product Line

| Product | Status | Price |
|---------|--------|-------|
| Open Sole Grippy Shoes | Active | $74 |
| Closed Sole Grippy Shoes | Active | $74 |
| Outdoor (Closed Sole variant context) | Active | $74 |
| Apparel (Yoga Tights, etc.) | Active | Per Shopify |
| Barreletics Socks | Upcoming — **not public** | — |

Sizes: **M and L** only. Fit note: Dark Grey, Hot Coral, and Blue run snugger than Light Grey. Promo: Buy 2, Save 15% (`SAVE15`); newsletter 10% off first order; free shipping over **$150**.

### Current Channels

- **DTC:** Shopify at barreletics.com (custom theme in this repo)
- **Wholesale:** Manual via Help Scout / partner forms (not self-serve)
- **Studio / Ambassador:** Inquiry → qualification → onboarding
- **Paid media:** Meta (primary), Google Ads, Pinterest, Microsoft (as active)
- **Owned:** Email, Instagram (primary social), Journal/SEO content

### Team Structure (Founder-Led)

| Role | Focus |
|------|--------|
| Founder / Owner / Architect | Brand, product, pricing, partnerships, financials, final approval |
| Builder / Operator (when engaged) | Theme, content within Foundation, integrations, analytics ops |
| Customer Support (Help Scout) | First-line CS; escalate out-of-policy to founder |
| Tidio AI | First-touch chat; handoff to Help Scout per rules |

Assume lean coverage: one person may wear multiple hats. Founder approval required for product, pricing, partnerships, and financial decisions.

### Revenue Model

1. **DTC product sales** ($74/pair + apparel) — primary  
2. **Wholesale** — 50% off MSRP (**INTERNAL — never publish publicly**), 10-pair opening minimum  
3. **Future:** ambassador/commission (framework in Milestone 5; confirm before promising)

Installments: 4 × $18.50 where enabled.

### Key Metrics to Watch

| Cadence | Watch |
|---------|--------|
| **Daily** | Shopify revenue, orders, conversion; GA4 sessions; ad spend + ROAS (Blend/Meta) |
| **Weekly** | Channel revenue/session vs benchmarks; email revenue; cart abandonment; Meta claimed vs Shopify Meta-UTM |
| **Monthly** | Full funnel, SEO/Search Console, LTV trends, Help Scout resolution time, inventory health, wholesale/studio pipeline |

**Channel revenue/session benchmarks (GA4):** Organic Search ~$2.21 · Email ~$2.25 · Paid Social ~$0.74 · Referral high $/session, low volume.

**Truth rule:** Shopify dollars are ground truth for revenue. Meta/GA4 can overclaim — investigate cliffs with sales-drop diagnostic skills before trusting ad dashboards alone.

---

## 1. BRAND

### Brand North Star (Doc 01)

- **Vision:** Redefining how people grip; replacing grip socks with Performance Skins.
- **Mission:** One piece of gear that ends the compromise between grip, durability, hygiene, and cost.
- **Values:** Performance over promise; category creation over competition; commitment match; durability as design; studio-first always.
- **North Star metric:** Market talk shifts from “best grip socks” → “grip sock alternatives” → “performance skins” / brand search.

### Category Creation Strategy

**Barreletics is replacing the grip sock category.** Grip socks = first generation; Performance Skins = next. Compete on the category question, not brand-vs-brand sock wars.

### Brand Voice

Premium, educational, confident — never arrogant, hype-bro, or shaming. Data-backed, direct, studio-aware.

### Brand Guardrails (Always / Never — Doc 02)

**Always:** Educate · Elevate · Simplify · Demonstrate · Support claims with Knowledge Base evidence.

**Never:** Shame grip sock users · Attack competitors by name · Overpromise durability · Fake urgency · Unsupported performance claims · Health/medical claims.

### Visual Identity

Canonical design system: `planning/03-design-system.md` + design system skill (v49).

| Token | Hex |
|-------|-----|
| Charcoal | `#1c1916` |
| Rust accent | `#c45c3f` |
| Warm cream bg | `#f5f2ec` |
| Warm border | `#d6cfc0` |
| Coral (cart badge only) | `#e8927c` |

Typography: Roboto stack per Doc 03. **No black-and-orange palette** (retired).

### Competitive Positioning

Position **vs grip socks** (Double Failure + Sock Math), not vs other athletic shoes. Outdoor/water is secondary — never lead hero messaging.

### Brand Assets

- Theme assets / logos: Shopify theme + owner-held brand files  
- Design tokens & components: Doc 03, Doc 04, `shopify-build/`  
- Copy inventory: Doc 02 slogans + Doc 08  
- Usage: warm neutrals + rust; Category Creation framing; no retired claims

### Messaging Hierarchy

**Primary (hero-level):** The Pilates Sock Era is Over · Let Us Knock Your Socks Off · Think Outside the Sock · One Pair Replaces Eight · You Commit to the Class. Commit to the Gear.

**Secondary:** Upgrade Your Grip. Upgrade Your Workout. · Never Loses Grip · Socks fail. This doesn't. · Performance Skins, not grip socks.

**Hashtag:** `#BarreleticsMovement`

Full inventory: `planning/02-brand-system.md`.

### Retired Claims

**Hard block.** See `planning/RETIRED_CLAIMS.md`. Includes (non-exhaustive): Free shipping over $75 · 30-day studio trial · Heat-activated grip · Warranty covers grip wear · Black/orange palette · Absolute “never degrades” / allergy absolutes.

---

## 2. MARKETING

### Strategy Overview

Drive Category Creation across every touchpoint: paid social for volume awareness, organic + SEO to intercept sock queries, email for high revenue/session, studios/wholesale for authority and reorder, influencers for proof.

### Channel Mix

| Channel | Role |
|---------|------|
| Paid social (Meta primary) | Prospecting + retargeting; watch ROAS |
| Organic social (IG primary) | Education, studio life, UGC |
| Email | Highest owned revenue/session after organic |
| SEO / Journal | Sock-query interception → Performance Skins |
| Influencer / Ambassador | Trust + UGC rights |
| Studio outreach | Instructor adoption + retail |
| Wholesale | B2B revenue (manual) |

### Budget Allocation Framework (Template)

Until founder sets fixed % splits, use:

| Bucket | Suggested share of media | Notes |
|--------|--------------------------|-------|
| Meta prospecting | 50–70% | Primary acquisition |
| Meta retargeting | 15–25% | Cart/view/ATC pools |
| Google / Pinterest / other | 10–25% | Scale only if ROAS clears target |
| Testing / creative | 5–10% | Always-on creative tests |

Email and organic are mostly production cost, not media.

### Campaign Planning Process

1. Objective (purchase / list / launch)  
2. Audience + offer (must match Doc 07 — no fake scarcity)  
3. Message (Category Creation; one slogan per creative)  
4. Landing page match (ad promise = page)  
5. UTM package (see UTM guide)  
6. Creative + copy approval  
7. Launch → daily spend/ROAS check → weekly learnings  

### Creative Production Process

Brief → brand-aligned assets (studio-first imagery) → copy from Docs 02/07/08 → founder review if new claims → export sizes → upload → naming convention → launch.

### UTM Tracking Standards

Follow: `/Users/andrewnehra/Documents/Claude/Projects/Barreletics social/utm-tracking/UTM-GUIDE.md`  
Also referenced in Milestone 5 campaign architecture. Every paid/email/influencer link gets UTMs. Shopify UTM attribution is the commercial truth check.

### Marketing Calendar Framework

Plan around: back-to-studio seasons, new color launches, limited editions, holiday gifting (premium tone — not discount frenzy), studio partnership moments, Journal education drops.

### Approval Workflow

| Asset | Approver |
|-------|----------|
| Within approved budget + approved claims | Marketing operator executes |
| New claims / slogans / policies | Founder |
| Over-budget spend | Founder |
| Partnerships / collabs | Founder |

### Performance Benchmarks

| Channel | Revenue / session (approx.) | Action |
|---------|----------------------------|--------|
| Organic Search | ~$2.21 | Protect & grow |
| Email | ~$2.25 | Protect & grow |
| Paid Social | ~$0.74 | Watch ROAS carefully |
| Referral | High $/session, low volume | Investigate sources |

---

## 3. ADVERTISING (PAID MEDIA)

### Platform Overview

| Platform | Role |
|----------|------|
| **Meta** | Primary paid engine |
| **Google Ads** | Search/intent when active |
| **Pinterest** | Discovery / visual |
| **Microsoft** | Secondary search if active |

Analytics via **Blend MCP** (`user-blend`) + Meta Marketing API when needed. GA4 Property **300437005**.

### Account Structure & Naming (Recommended Convention)

`[Platform]_[Objective]_[Audience]_[OfferOrProduct]_[YYYYMM]`  
Examples: `META_PROS_LAL_PURCH_OpenSole_202607`, `META_RET_ATC_SAVE15_202607`.

Keep one naming system; do not rename mid-flight without logging.

### Campaign Types

1. **Prospecting** — lookalikes, interests (studio/Pilates/barre), broad tests  
2. **Retargeting** — site visitors, ATC, checkout abandoners  
3. **Loyalty / purchasers** — new color, multi-pair, apparel (careful frequency)

### Creative Guidelines

Category Creation messaging; studio footage; grip surface visible; customer quotes OK; **never** shame sock users or name competitors; **never** “studio trial” / heat-grip / fake urgency.

### Audience Strategy

Custom (purchasers, ATC, viewers) → Lookalikes → Interest/behavior tests. Exclude recent purchasers from prospecting where appropriate.

### Budget Management Cadence

| Cadence | Action |
|---------|--------|
| Daily | Spend vs plan, ROAS flags, broken creatives |
| Weekly | Scale winners, pause losers, creative fatigue check |
| Monthly | Channel mix vs revenue/session benchmarks |

### ROAS Targets & Scale/Pause Rules (Operating Defaults)

| Signal | Action |
|--------|--------|
| Blended ROAS sustainably **> ~2.0x** (confirm with Shopify) | Scale carefully (+10–20%) |
| ROAS collapsing while Meta “purchases” look fine | **Shopify Meta-UTM check** — possible pixel/CAPI overclaim |
| Creative fatigue / rising CPM + flat conversions | Rotate creative |
| Learning limited / spend concentration | Audit auction health |

Exact numeric targets are founder-set; use 2.0x as a **watchline**, not dogma.

### Creative Rotation

Aim for fresh primary creative every **2–4 weeks** on heavy spend ads, sooner if frequency spikes or CTR/ROAS decays. Keep proven winners as controls.

### Reporting Cadence

- Daily: spend, purchases (Shopify), ROAS flags  
- Weekly: platform vs Shopify attribution  
- Tools: Blend smart_query (Meta/Google/Pinterest), GA4 channel report  

### Ad Copy Rules

Lead with sock failure → Performance Skin solution; Sock Math where space; no competitor naming; no retired claims.

### Landing Page Strategy

| Ad theme | Preferred land |
|----------|----------------|
| Category / vs socks | `/collections/grippy-shoes` (pillar) |
| Open vs Closed | `/pages/compare-open-closed-sole` or style collection |
| Specific style | Matching collection or PDP |
| Campaign offer | Dedicated LP when available (M5 framework) |

Match message → page. Avoid sending purchase-intent ads to generic About.

### Pixel / CAPI

Meta Pixel + Conversions API required (Purchase, ATC, InitiateCheckout, ViewContent); browser + CAPI deduplication. Roadmap reference: M4B integrations / Decision Log (D-045 family as maintained in `planning/10-decision-log.md`). Validate events in Meta Events Manager + Shopify orders.

### Blend MCP Access

Server: `user-blend`. Provide business context (Barreletics, fitness gear, goal = purchases/ROAS) before querying. Use for spend, ROAS, campaign health — not as sole revenue truth.

---

## 4. EMAIL

### Platform

**Klaviyo** is planned in M4B but marked **unconfirmed** until owner credentials are verified. Until confirmed, operate via **Shopify Email / Shopify customer notifications** and do not promise Klaviyo-only features.

If Klaviyo is confirmed mid-coverage period: welcome, browse/cart abandon, post-purchase, review, win-back, VIP, sunset become the Growth Engine stack (M5).

### List Management

- Segments: purchasers, non-purchasers, engaged, VIP (repeat), discipline tags if available  
- Suppression: unsubscribes, bounces, complainers, recent purchasers for acquisition blasts as appropriate  
- Hygiene: sunset inactive; never buy shady lists  

### Automated Flows (Target Architecture)

| Flow | Purpose |
|------|---------|
| Welcome | Brand + Category Creation + 10% signup offer if active |
| Browse abandonment | Education, not panic discounts |
| Cart abandonment | Reminder + size confidence + policy clarity |
| Post-purchase | Care, sizing help, review ask path |
| Review request | Judge.me |
| Win-back | Lapsed purchasers |
| VIP | Early access to colors / limited editions |
| Sunset | Re-permission or suppress |

### Campaign Emails

Cadence: quality over volume (e.g., 1–2 thoughtful campaigns/week when list is warm). Content: education, launches, studio stories — premium tone. Approval: new claims → founder; routine within Doc 07 → operator.

### Template Standards

Align with design system (charcoal, cream, rust accents sparingly). Mobile-first. Clear single CTA. No fake urgency.

### Deliverability

Ensure SPF, DKIM, DMARC on sending domain. Warm new domains/IPs gradually. Monitor bounce/complaint rates.

### Email KPIs

Open rate, click rate, revenue per email / revenue per recipient, list growth, unsubscribe rate. Benchmark channel: ~$2.25 revenue/session for Email in GA4.

---

## 5. SOCIAL MEDIA

### Platforms

| Platform | Priority |
|----------|----------|
| Instagram | Primary |
| Facebook | Support / ads |
| Pinterest | Discovery |
| TikTok | If account active — studio/demo short form |

### Content Pillars

1. Product education (grip, care, Open vs Closed)  
2. Studio life (real class contexts)  
3. Community / UGC / instructor voice  
4. Behind-the-scenes / Made in USA / brand craft  

### Posting Cadence (Operating Defaults)

| Platform | Cadence |
|----------|---------|
| Instagram | 4–7 feed/Reels touches per week + Stories as available |
| Pinterest | Steady pins of product + educational graphics |
| TikTok | 2–4/week if active |
| Facebook | Mirror key IG + community replies |

### Content Creation Process

Brief → shoot/edit or UGC pull → Doc 07 fact check → brand guardrails → schedule → engage.

### UGC Rights

Never reuse customer/influencer content without documented permission. Prefer written grant covering paid + organic + ads. Track source, date, scope.

### Hashtag Strategy

Primary brand: `#BarreleticsMovement`. Discipline tags sparingly; avoid spammy tag blocks.

### Community Management

| Item | Standard |
|------|----------|
| Response time | Same as CS intent: aim business-hours same day |
| Tone | Helpful, confident, never defensive |
| Escalation | Warranty, refund disputes, PR risk → Help Scout / founder |

### Influencer Repurposing

Only with rights; credit creators; adapt to brand templates without distorting claims.

### Social Analytics

Engagement rate, reach, follower growth, clicks to site (UTM), assisted conversions in GA4. Brand guardrails apply to **all** social content.

---

## 6. CUSTOMER SERVICE

### Platform

**Help Scout** — saved replies master: `helpscout-kb/Barreletics_Email_Template_Master.md` (stub: `planning/m4b-helpscout-alignment.md`).  
**Tidio AI** — first-touch from `planning/m4b-tidio-knowledge-base.md`; escalate per handoff rules.

### Response Time Targets

- **Business hours:** < 4 hours  
- **Weekends:** < 24 hours  
- Monthly KPI: Help Scout resolution time < 4 hours (business)

### Saved Replies

Use approved macros from `helpscout-kb/Barreletics_Email_Template_Master.md` for sizing (incl. **2.4–2.6** save-the-return), shipping, returns, warranty, care, Open vs Closed, wholesale/partner, order status, discounts, vs grip socks. Do not freestyle policy language.

**2.6 Sizing — Save the return (torn on first use)** (added 2026-08-11): outdoor/first-use tear — offer free replacement before processing return; request break photo + usual shoe size + narrow/average/wide; put-on tip (pull from top of foot, not straps). Tag `quality-issue`.

### Common Scenarios

| Scenario | Resolution |
|----------|------------|
| Sizing issues | Educate (snug fit; color snug notes); **exchange** — free exchange shipping per Doc 07; Help Scout may recommend return + reorder for stock certainty |
| Return requests | **30-day**, new/sellable condition; original mesh bag + tag; **not** a “studio trial” |
| Warranty | **90-day manufacturing defects only**; photos required (esp. international); customer pays intl replacement shipping |
| Torn / broke on first use | **2.6** — offer free replacement (no charge); request photo + size + foot width; put-on tip; process return if they decline |
| Product questions | Answer from Doc 07 / saved replies |
| Wholesale | Qualify → partner form → founder path |
| Studio | Studio program / partners process |

### Escalation Matrix → Founder

Escalate: out-of-policy refunds, legal threats, PR/social crises, wholesale terms negotiation, product defects at scale, payment disputes needing write-offs, anything not in Knowledge Base.

### Tidio AI

Trained from Doc 07 topics. Handles first-touch; escalates warranty, anger, Shopify admin needs, wholesale, unknown facts, explicit human requests, billing, customs issues.

### Tone

Helpful, confident, never defensive, always solution-oriented. Embed Category Creation naturally (“Performance Skins are designed to…”).

### Refund / Exchange Authority

| Level | Authority |
|-------|-----------|
| Agent | Within published 30-day / 90-day policies |
| Founder | Exceptions, goodwill beyond policy, wholesale credits |

### Difficult Customer Playbook

1. Acknowledge + restate issue  
2. State policy clearly (Doc 07 language)  
3. Offer in-policy solution first  
4. If stuck or abusive: escalate; document in Help Scout  
5. Never argue Category Creation mid-conflict — resolve the order first  

---

## 7. WHOLESALE

### Current Process

**Manual** via Help Scout + partner inquiry form (`/pages/partners` or wholesale page). Not self-serve checkout at scale.

### Commercial Terms (INTERNAL)

| Term | Value |
|------|-------|
| Opening order | **10 pairs minimum** |
| Pricing | **50% off MSRP** — **INTERNAL ONLY; never publish on site or social** |
| Reorder minimum | **10 pairs** (operating assumption — confirm with founder if disputed) |
| Payment | Prefer **prepaid** for new accounts; **Net 30** only for trusted/approved accounts (founder approval) |

### Qualification Criteria

Legitimate retail or studio location; able to represent brand (display + messaging); aligned with Category Creation (not positioning as “just another grip sock”).

### Onboarding Process

1. Inquiry received  
2. Qualification (location, channel, volume)  
3. Terms shared privately  
4. First order (MOQ)  
5. Education pack (product facts from Doc 07 — no retired claims)  
6. Reorder cadence check-ins  

### Account Management

Periodic reorder check-ins; display/support assets; correct messaging if partner drifts into sock-comparison warfare or retired claims.

### Marketing Materials for Partners

Product specs, Sock Math (illustrative), Open vs Closed, care, studio discipline language, digital imagery. Update quarterly or on launch.

### Wholesale Returns / Exchanges

Founder-defined; default tighter than DTC. Do not invent terms — escalate.

### Growth Path

Volume tiers, display programs, studio education sessions — expand only with founder approval (M5 wholesale resource library).

---

## 8. MANUFACTURING

### Product Truths

- **Made in USA**  
- **Patented / proprietary grip technology** — injection-molded 360° grip compound  
- Latex-free, silicone-free, antimicrobial, non-porous, sweat-resistant  

### Current SKUs

Open Sole (multi-color), Closed Sole (multi-color), Outdoor context as Closed Sole variant use-case. Sizes **M / L**. Color fit: Dark Grey, Hot Coral, Blue snugger than Light Grey.

### Lead Times

**Placeholder — confirm with manufacturing partner.** Until documented in Doc 07 Manufacturing domain, do not promise dates to customers or wholesale beyond “ships 1–2 business days” for in-stock DTC.

### Quality Control

Incoming QC against manufacturing specs; customer warranty photos feed defect patterns back to founder + partner. Doc 07 Manufacturing domain is still a placeholder — log new facts into Doc 07 when verified.

### Inventory Management

Shopify inventory as operational source. Watch sell-through by style/size/color. Use manufacturing forecast skill / planner when planning production buys.

### Reorder Triggers (Operating Defaults)

Trigger reorder discussion when velocity would stock-out before lead time + buffer; prioritize core colors/sizes. Founder approves POs.

### Supplier Relationships

Treat manufacturing partner as confidential. No public disclosure of costs, MOQs with factory, or formulas.

### Defect Handling

90-day manufacturing defect warranty; replace/refund per founder guidance; international photo + shipping rules per Doc 07.

### New Color / Product Development

Founder-approved concept → sampling → QC → photography → Shopify + Doc 07 update → launch playbook (Section 12). Never announce Upcoming products publicly without authorization.

---

## 9. WEBSITE

### Platform & Theme

**Shopify** + custom Barreletics theme in this repository (`shopify-build/`). Live: barreletics.com.

### Key Pages

Homepage · Collection pillar `/collections/grippy-shoes` · Open/Closed/Outdoor collections · PDP · FAQ · About · Contact · Compare · Partners · Size Guide · Warranty · Shipping · Returns · Technology · Grip Comparison · Journal · Studio/Ambassador pages as published.

Nav architecture: `planning/11-navigation-architecture.md` — flat nav: Grippy Shoes | Apparel | Collaborations | Journal.

### Content Update Process

1. Confirm fact in Doc 07 (or update Doc 07 first)  
2. Edit theme/page/section copy  
3. Check retired claims  
4. PR → review → deploy  

### Product / Collection Management

Shopify Admin for products, variants, inventory, collections. Create collections only when architecture + SEO justify (see Doc 09/12). Avoid thin SEO collections.

### Navigation Updates

Shopify Navigation menus must match Doc 11. Structural nav changes escalate (Decision Framework).

### Content Governance

Customer-facing product/policy copy originates from Doc 07. AI may reword; AI may never invent facts (`planning/13-knowledge-architecture.md`).

### Theme Update Process

`branch → PR → review → merge → Shopify theme push/preview → owner approve publish → monitor`

### Emergency Procedures

See Appendix C and `planning/m4d-rollback-procedure.md`. Keep prior theme as instant rollback.

---

## 10. SEO

### Strategy

**Target sock queries to disrupt the category** — rank for grip/Pilates/barre/yoga socks language, convert to Performance Skins (`planning/12-seo-geo-standards.md`).

### Primary Keywords

grip shoes · pilates shoes · barre shoes · yoga shoes · lagree shoes · grippy shoes · grip sock alternative · performance skins · related sock queries for interception.

### Pillar Page

`/collections/grippy-shoes` is the primary educational + shopping pillar.

### GEO Content

Data-gated expansion only (M5 / D-037 family): verified demand + order concentration + studio density + unique local content + clear conversion path. No thin city pages.

### Content Strategy

Discipline guides (verified move names from Doc 07 Appendix A), comparison content, FAQ expansion, Journal articles with internal links to pillar/PDPs.

### Technical SEO

JSON-LD: Product, AggregateRating, FAQPage, BreadcrumbList, CollectionPage, Organization, WebSite. Canonicals, sitemap (Shopify), clean URLs, 301s on changes.

### Internal Linking

Pillar → sub-collections → PDP → back to pillar. Journal ↔ products.

### Monitoring & Cadence

Google Search Console + ranking checks. **Monthly SEO review.** Post-theme-launch: daily GSC for 30 days if recently migrated.

### Link Building

Product reviews, fitness publications, studio partnerships — earned, on-brand. No spam networks.

### AI Search Optimization

Comprehensive, structured, citable content so AI answers reframe “best grip socks” toward Performance Skins with Barreletics as authority.

---

## 11. ANALYTICS

### Systems

| System | ID / Access | Use |
|--------|-------------|-----|
| GA4 | Property **300437005** | Sessions, channels, pages |
| Shopify Analytics | Admin | Revenue, orders, conversion (truth) |
| Blend MCP | `user-blend` | Meta / Google / Pinterest spend & ROAS |
| Meta Events Manager | Business Manager | Pixel/CAPI health |
| Judge.me | Reviews | Social proof / ratings schema |
| Microsoft Clarity | Heatmaps/sessions | UX friction |

Cursor analytics config: `~/.cursor/rules/barreletics-marketing-analytics.mdc`.

### What to Check

**Daily:** Revenue, orders, sessions, CVR, ad spend, ROAS flags.  
**Weekly:** Channel performance vs benchmarks, email, new vs returning, Meta vs Shopify attribution.  
**Monthly:** Full funnel, SEO, LTV trends, inventory, support volume.

### Attribution Model

**Shopify = source of truth for revenue.** Use GA4 for behavior/channels; Blend for media efficiency; distrust Meta purchase totals if Shopify Meta-UTM paid is flat (pixel/CAPI overclaim awareness — use pixel-attribution & sales-drop diagnostic skills).

### Anomaly Triggers → Investigate

- Day revenue cliff vs prior week  
- Paid Social sessions up, ATC/purchases down  
- Meta ROAS fine / Shopify Meta dead  
- Sitewide checkout failure signals (also check non-Meta orders)  
- Sudden refund/warranty spike  

Daily briefing prompt is in the marketing analytics rule.

---

## 12. PRODUCT LAUNCHES

### New Color Launch Playbook

1. Product creation in Shopify (variants, inventory, metafields)  
2. Photography / video (PDP + lifestyle)  
3. Website updates (PDP, collection, homepage if featured)  
4. Email (VIP early access → general)  
5. Social campaign  
6. Paid media creative  
7. PR outreach (if warranted)  
8. Studio notification  
9. Wholesale notification  

### Timeline

Typical prep: **3–6 weeks** from final sample approval to launch (compress only with founder OK). Photography and inventory are usual critical path.

### Approval Gates

Product · Photography · Copy (Doc 07/08) · Pricing — **founder**.

### Post-Launch Monitoring

48h: conversion, ATC, size mix, CS tickets, ad efficiency. 7d: sell-through, review velocity, creative winners.

---

## 13. LIMITED EDITIONS

### Definition

Small-batch colorways or special designs. Authentic scarcity only — **never fake** “Only 3 left!” on evergreen stock.

### Drop Workflow

1. Product development  
2. Limited inventory allocation  
3. Assign to Limited Edition collection  
4. Teaser (social + email)  
5. Drop date announcement  
6. Launch (email + social + site simultaneous)  
7. Sold-out handling (waitlist only if operationally real)

### Pricing

Default **same MSRP ($74)** unless founder sets premium for collab/limited.

### Communication

Honest inventory language. Brand guardrails forbid fake urgency.

---

## 14. COLLABORATIONS

### Current Reference

**Caperni** (and any live Collaborations nav items on barreletics.com) — treat live site as current catalog of public collabs.

### Evaluation Criteria

Brand alignment · Audience overlap · Quality standards · Amplifies Category Creation (not sock commodity vibes).

### Process

Outreach → alignment → product development → co-branded creative → launch (same gates as Section 12) → post-mortem.

### Co-Branding Guidelines

Barreletics visual system + partner marks per written agreement. No partner claims that violate Doc 07 / retired claims.

### Revenue / Cost Sharing

Founder-negotiated. Document in writing before production.

### Marketing Responsibilities

Define owner of email, paid, social, PR, wholesale notify in the collab brief.

---

## 15. PHOTOGRAPHY & VIDEO

### Product Photography Standards

- White/neutral for PDP primary  
- Lifestyle/studio for marketing  
- On-foot shots showing **grip surface**  
- Color-accurate (esp. snug-fit colors for trust)  

### Video Types

Grip demo · Real studio class · Testimonials · How-to (on/off, care, sizing).

### Asset Management

Store in owner-designated brand drive; name `YYYYMM_type_style_color_version`. Theme-ready exports in Shopify Files / theme assets.

### Usage Rights

Track licenses for stock, photographers, UGC, influencers. Ads require commercial rights.

---

## 16. STUDIO OUTREACH

### Goal

Instructor adoption + studio retail/recommendation of Barreletics.

### Process

Identify → contact → demo → trial (business terms, not “studio trial” consumer language) → partnership → reorder.

### Studio Types

Barre · Pilates/Reformer · Lagree · Megaformer · Yoga (studio-first).

### Value Proposition

Students stop replacing failed grip socks; instructors get reliable grip through holds/transitions; Sock Math + Made in USA + Category Creation education.

### Partnership Tiers

Use site Studio Program / Partners pages as public face; custom tiers founder-approved.

### Marketing Support

Assets, spotlight opportunities (Journal/social), accurate sizing guidance for front desk.

### Studio Spotlight Program

Feature partner studios with real practice context — educational, not pay-to-play spam.

### Tracking

CRM or simple sheet: studio name, contact, status, pairs ordered, reorder dates, notes.

---

## 17. INFLUENCER & AMBASSADOR OUTREACH

### Identification Criteria

Fitness/wellness · studio instructors · audience alignment · authentic practice · brand-safe history.

### Process

Identify → vet → contact → negotiate → brief (Docs 02/07/08) → activate → rights signed → measure.

### Compensation Models

Product gifting (default) · Flat fee · Commission/affiliate (**future — confirm before promising**).

### Content Requirements

Category Creation OK; no retired claims; disclose per FTC; show grip/studio use when possible.

### Performance Tracking

Reach, engagement, referral traffic (UTM), conversions (Shopify), content reuse rights obtained.

### Relationship Cadence

Thank + feedback after deliverables; re-engage on launches; retire misaligned partners.

### Ambassador vs Influencer

| | Influencer | Ambassador |
|--|------------|------------|
| Nature | Campaign / episodic | Ongoing brand representation |
| Access | Briefed creatives | Deeper education + possible codes |
| Bar | Higher continuous alignment |

### UGC Rights

Written grant before ads reuse.

---

## 18. TRADE SHOWS & EVENTS

### Relevant Events

Boutique fitness conferences, Pilates/barre expos, wellness retail shows — prioritize audience fit over vanity size.

### Evaluation Criteria

Audience alignment · Total cost (booth, travel, samples, labor) · Expected leads/orders · Brand presentation quality.

### Booth / Display Standards

Premium, calm, studio-credible; Performance Skins story; grip visible; no black/orange; no sock-shaming copy.

### Materials

Product samples · Displays · One-pagers from Doc 07 facts · Wholesale leave-behinds (pricing **not** on public flyers) · Lead capture (tablet/form).

### Lead Capture & Follow-Up

Capture name, studio/role, email, interest (retail vs personal). Follow up within **3 business days** via Help Scout/email sequences.

### Budget Framework

Founder approves per event. Track cost per qualified lead and wholesale open rate post-show.

---

## 19. KPIs & METRICS

Baselines marked `[baseline]` / `[target]` / `[budget]` must be filled from current Shopify/GA4/Blend before the coverage period; update monthly.

### Daily KPIs

| Metric | Source | Target |
|--------|--------|--------|
| Revenue | Shopify | [baseline] |
| Orders | Shopify | [baseline] |
| Sessions | GA4 | [baseline] |
| Conversion Rate | Shopify | [baseline] |
| Ad Spend | Blend/Meta | [budget] |
| ROAS | Blend (validate vs Shopify) | >2.0x watchline |

### Weekly KPIs

| Metric | Source | Target |
|--------|--------|--------|
| Revenue by Channel | GA4 | Organic/Email high $/sess; Paid Social watched |
| Email Revenue | Email platform | [target] |
| New vs Returning | GA4 | [ratio] |
| Cart Abandonment Rate | Shopify | <70% |
| Customer Acquisition Cost | Calculated | [target] |
| Average Order Value | Shopify | [target] |

### Monthly KPIs

| Metric | Source | Target |
|--------|--------|--------|
| Total Revenue | Shopify | [target] |
| Gross Margin | Accounting | [target] |
| LTV:CAC | Calculated | >3:1 |
| Repeat Purchase Rate | Shopify | 15–25% |
| Email List Growth | Email platform | [target] |
| SEO Rankings | Search Console | Progress to Top 3 primary terms |
| Review Count | Judge.me | [growth target] |
| Help Scout Resolution Time | Help Scout | <4 hours |

### Quarterly KPIs

Revenue growth · Acquisition trends · Channel efficiency · Inventory health · Wholesale growth · Studio partner count · Content published · SEO authority growth.

---

## 20. QUARTERLY PLANNING

### Process

1. Review previous quarter KPIs  
2. What worked / what didn’t  
3. Set revenue and growth targets  
4. Plan product launches / limited editions  
5. Plan campaigns and promotions  
6. Allocate marketing budget  
7. Set content calendar  
8. Plan studio/wholesale outreach  
9. Technology/website improvements (within Foundation — no silent architecture rewrites)  
10. Team capacity planning  

### Timeline

Start planning **30 days before** quarter begins. Monthly check-ins; mid-quarter adjustment. **Annual planning in Q4** for the following year.

---

## 21. DECISION FRAMEWORK

Canonical: `planning/DECISION_FRAMEWORK.md`.

| Decision type | Rule |
|---------------|------|
| Builder vs Owner | Builder executes within Docs 01–13; escalate strategy/policy/architecture |
| Brand | Always Doc 02 |
| Product / Pricing / Partnerships / Financials | **Founder approval** |
| Marketing spend | Within approved budget → execute; over → escalate |
| Customer service | Within policy → resolve; outside → escalate |
| Website | Within Foundation → execute; architectural change → Decision Log |
| Content | Within Knowledge Base → execute; new claims → founder |
| Conflicts | Doc 07 wins for facts; later Decision Log wins for strategy conflicts; log in `planning/10-decision-log.md` |

---

## APPENDICES

### A. Key Contacts & Accounts

*(Credentials live in founder password manager — not in this repo.)*

| System | Purpose |
|--------|---------|
| Shopify Admin | Store, orders, theme, products |
| Domain registrar / DNS | barreletics.com |
| GA4 (300437005) | Web analytics |
| Meta Business Manager + Pixel/CAPI | Ads + events |
| Google Ads | Search/intent (if active) |
| Pinterest Business + Tag | Ads + tracking |
| Microsoft Advertising | Secondary paid (if active) |
| Blend | Cross-channel ad analytics (MCP) |
| Help Scout | Customer email/support |
| Tidio | Chat / AI first-touch |
| Judge.me | Reviews |
| Klaviyo | Email (confirm if active) |
| Shopify Email | Fallback email |
| Microsoft Clarity | Session/heatmaps |
| Manufacturing partner | Production (confidential) |
| Accounting / payments | Finance, tax, payouts |
| Cloud / Cursor MCP config | `~/.cursor/mcp.json` for operator tooling |

### B. Glossary

| Term | Meaning |
|------|---------|
| Performance Skins | Barreletics category name |
| Grippy Shoes | Customer-facing / nav product name |
| Open Sole | Heel-open variant — more naturally grounded feel |
| Closed Sole | Full-coverage variant |
| Category Creation | Strategic philosophy: replace grip socks as a category |
| Knowledge Base | Doc 07 — single source of truth |
| Foundation | Docs 01–13 — locked architecture |
| GEO | Geographic / generative-engine-oriented local content (data-gated) |
| Sock Math | Illustrative cost comparison vs buying 6–8 grip sock pairs/year |
| Double Failure | Grip dots fail + fabric absorbs sweat/bacteria |
| Builder | Executor within approved docs |
| Owner / Architect / Founder | Strategic approver |

### C. Emergency Procedures

| Crisis | First moves |
|--------|-------------|
| **Site down / broken checkout** | Unpublish broken theme → roll back per `planning/m4d-rollback-procedure.md` → verify purchase path → communicate if prolonged |
| **Revenue crash** | Shopify ground truth → non-Meta orders (sitewide vs Meta-only) → GA4 funnel → Blend spend → use sales-drop-diagnostic skill checklist |
| **Customer crisis** | Help Scout ownership → founder escalate → do not argue publicly |
| **Social media crisis** | Pause amplification → factual correction if needed → founder approval before statements → no ratio battles |
| **Data breach** | Isolate access → notify founder immediately → legal/counsel path; preserve logs; do not speculate publicly |
| **Supplier disruption** | Contact manufacturing partner → inventory triage → delay launches → honest site inventory messaging |

### D. Document Map

| Area | Location |
|------|----------|
| **This Operating System** | `docs/operating-system.md` |
| Foundation Docs 01–13 | `planning/01-*.md` … `planning/13-*.md` |
| Decision Log | `planning/10-decision-log.md` |
| Decision Framework | `planning/DECISION_FRAMEWORK.md` |
| Retired Claims | `planning/RETIRED_CLAIMS.md` |
| Roadmap M4–M6 | `planning/MILESTONES-4-5-6-ROADMAP.md` |
| Help Scout saved replies (master) | `helpscout-kb/Barreletics_Email_Template_Master.md` |
| Help Scout alignment (stub) | `planning/m4b-helpscout-alignment.md` |
| Tidio KB | `planning/m4b-tidio-knowledge-base.md` |
| Launch / rollback (M4D) | `planning/m4d-*.md` |
| Technical developer docs | `docs/00-README.md` … `docs/25-*.md`, `docs/INDEX.md` |
| Theme code | `shopify-build/` |
| Design system skill | `~/.cursor/skills/barreletics-design-system/SKILL.md` |
| Brand copy skill | `~/.cursor/skills/barreletics-brand-copy/SKILL.md` |
| Marketing analytics rule | `~/.cursor/rules/barreletics-marketing-analytics.mdc` |
| UTM guide | `/Users/andrewnehra/Documents/Claude/Projects/Barreletics social/utm-tracking/UTM-GUIDE.md` |

---

## 30-Day Coverage Checklist (Quick Start)

**Day 1:** Access Shopify, Help Scout, Meta, GA4, Blend, email platform; read Docs 01, 02, 07, RETIRED_CLAIMS; verify site purchase path.  
**Daily:** Shopify revenue/orders · GA4 sessions · ad spend/ROAS · CS SLA.  
**Weekly:** Channel benchmarks · creative health · inventory · wholesale/studio pipeline.  
**Never:** Invent claims · publish wholesale % · promise Upcoming products · skip Doc 07 on policy answers.

---

*End of Barreletics Operating System manual.*
