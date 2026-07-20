# Growth Engine — Customer Lifecycle Architecture

---
document: Growth Engine
version: 1.0
status: 🔵 Ready for Review
last_modified: 2026-07-19
depends_on: [02-brand-system, 07-product-knowledge-base, 08-copy-guide, 13-knowledge-architecture]
related: [m4b-helpscout-alignment, m4b-tidio-knowledge-base, MILESTONES-4-5-6-ROADMAP]
email_platform: Klaviyo (preferred; confirm activation) / Shopify Email fallback
---

## Purpose

Map every customer touchpoint from first awareness through advocacy so lifecycle marketing is intentional, on-brand, and fact-consistent with Doc 07.

**Brand guardrails (hard):**
- Never fake urgency  
- Never shame grip sock users  
- Never attack competitors by name  
- Always educate, elevate, simplify  
- AI may draft wording; **facts only from Knowledge Base**  

---

## 1. Customer Journey Map

```
AWARENESS → CONSIDERATION → PURCHASE → ONBOARDING → RETENTION → ADVOCACY
```

| Stage | Mindset | Primary touchpoints | Key messages | Conversion goal | Metrics |
|-------|---------|---------------------|--------------|-----------------|---------|
| Awareness | “My socks slip / smell / die” | IG/Pinterest/TikTok, Meta/Google/Pinterest ads, SEO, studio WOM, influencers, PR | Category creation: why grip socks fail; Performance Skins exist | Site visit / engaged view | New users, CPMs, branded search |
| Consideration | “Is this better than socks?” | Homepage → Collection → PDP, browse emails, retargeting, Compare, FAQ, Tidio | Open vs Closed, Sock Math, $74, Made in USA, reviews | ATC / email capture | ATC rate, email capture %, PDP CVR |
| Purchase | “I’ll try a pair” | Cart, checkout, Shop Pay, trust strip | Free ship $150+, 30-day returns (sellable), 90-day defect warranty | Paid order | CVR, AOV, checkout completion |
| Onboarding | “How do I wear these?” | Transactional email, care/size content, Help Scout | Fit, barefoot intent, first-class tips, rinse/reuse | Successful first class + no return | Ticket rate, exchange rate |
| Retention | “I want another / apparel” | Review ask, cross-sell, VIP, studio ask | Second style, care, community | Repeat purchase | Repeat rate, LTV |
| Advocacy | “Everyone in my studio needs these” | UGC ask, referral, ambassador, reviews | Share proof; instructor trust | Review / referral / UGC | Review rate, referral rate |

### Touchpoint timeline

```
Day -∞ → 0: Awareness
├── Social (IG primary, Pinterest, TikTok if active)
├── Paid (Meta primary; Google; Pinterest)
├── Organic search (sock + shoe queries → pillar)
├── Studio / instructor recommendation
├── Influencer / ambassador
└── PR / press

Day 0: First visit
├── Home → Collection → PDP
├── Newsletter capture (after engagement threshold)
├── Browse abandonment eligible (if subscribed)
└── Retargeting pixels fire

Day 0–7: Consideration
├── Browse abandonment email
├── Retargeting ads
├── Return visits / cart create
└── Cart abandonment sequence

Day X: Purchase
├── Order confirmation
├── Shipping + delivery notifications
└── Post-purchase sequence starts

Day X+1 → X+7: Onboarding
├── Getting started / how to wear
├── Care instructions
├── First-class tips
└── Support invitation (Help Scout / Tidio)

Day X+14 → X+90: Retention
├── Review request (Judge.me)
├── UGC request
├── Cross-sell Open ↔ Closed / apparel
├── Referral intro
└── Studio recommendation prompt

Day X+90+: Advocacy
├── VIP recognition
├── Ambassador invite (qualified)
├── Repeat / new color nudges
├── Seasonal campaigns
└── Win-back if lapsed
```

---

## 2. Email Flows

Platform: **Klaviyo** when active; otherwise Shopify Email with same architecture.

### Flow 1: Welcome Series (newsletter)

| | |
|--|--|
| **Trigger** | Email captured (popup/footer) |
| **Emails** | 5 |
| **Exit** | Purchase → post-purchase |

| # | Timing | Subject direction | Content | CTA |
|---|--------|-------------------|---------|-----|
| 1 | Immediate | Welcome + brand | Story + Performance Skins intro + welcome offer (if approved) | Shop grippy shoes |
| 2 | Day 2 | Why grip socks fail | Double Failure education (no shaming) | See the difference |
| 3 | Day 4 | Open vs Closed | Decision support | Compare styles |
| 4 | Day 7 | Social proof | Instructor/customer quotes (Doc 07) | Read reviews / shop |
| 5 | Day 10 | Reminder | Offer reminder + free shipping **$150** | Complete your pair |

**KPIs:** signup→purchase rate, email revenue/session (~$2.25 benchmark), unsub rate.

### Flow 2: Browse abandonment

| | |
|--|--|
| **Trigger** | Viewed PDP, no ATC (subscribed only) |
| **Emails** | 3 |
| **Exit** | ATC or purchase |

1. **1h** — Still considering [product]? Value props  
2. **24h** — vs grip socks + reviews  
3. **72h** — Sizing confidence + FAQ  

### Flow 3: Cart abandonment

| | |
|--|--|
| **Trigger** | ATC, no checkout |
| **Emails** | 3 |
| **Exit** | Purchase |

1. **1h** — Cart reminder + image + CTA  
2. **24h** — Sock Math + reviews  
3. **72h** — Sizing help + returns framing (sellable condition, not “trial”)  

**No fake countdown inventory.**

### Flow 4: Post-purchase — first-time buyer

| # | Timing | Content | CTA |
|---|--------|---------|-----|
| 1 | Immediate | Order confirmation (Shopify) | View order |
| 2 | Day 1 | What to expect / ship window | Track (when available) |
| 3 | Shipped | Tracking | Track package |
| 4 | Delivery +1d | How to wear + first class | Size guide if needed |
| 5 | Delivery +7d | Care + check-in | Care tips / support |
| 6 | Delivery +14d | Review request | Judge.me |
| 7 | Delivery +21d | Cross-sell opposite sole / apparel | Shop |
| 8 | Delivery +30d | UGC ask | Share #BarreleticsMovement |

### Flow 5: Post-purchase — repeat buyer

Abbreviated onboarding. Emphasize VIP recognition, referral, ambassador path, apparel cross-sell.

### Flow 6: Review request

- **Trigger:** Delivery +14d (align with Flow 4 #6)  
- **+7d follow-up** if no review: photo-friendly ask  
- **Exit:** Review submitted  

### Flow 7: Win-back

| Timing | Content |
|--------|---------|
| Day 180 no purchase | Miss you + what’s new (no fake scarcity) |
| Day 195 | New colors / community |
| Day 210 | Final value reminder + testimonials |
| Exit | Purchase or suppress after sequence |

### Flow 8: VIP / loyalty (email phase)

**Qualify:** 3+ orders OR ≥$200 LTV (tune with data).  
Recognition email + early access to colors + quarterly VIP note + ambassador invite when fit.

### Flow 9: Sunset / re-permission

- No engagement 90 days → re-opt-in  
- +14 days → final notice → suppress  
Protects deliverability.

**Campaign emails:** 1–2 thoughtful sends/week max once list is warm; always Category Creation–aligned; approve offers with Owner if discounting.

---

## 3. SMS Flows (conditional)

Adopt only with compliant opt-in platform (often Klaviyo SMS).

| Flow | Trigger | Notes |
|------|---------|-------|
| Welcome | SMS opt-in | Offer link + opt-out |
| Cart abandon | Cart abandon (SMS subs) | ~2h; one reminder preferred |
| Shipping | Shipped/delivered | Transactional |
| Back in stock | Restock of viewed SKU | |
| Launch | Manual | VIP early → general |

**Guardrails:** ≤4 promo SMS/month; always opt-out; transactional > promo; no pressure tactics.

---

## 4. Post-Purchase Journey

```
PURCHASE
├── Order confirmation (immediate)
├── Shipping confirmation
├── Delivery confirmation
├── Day 1: Getting started
├── Day 7: Care + first-class check-in
├── Day 14: Review request
├── Day 21: Cross-sell
├── Day 30: UGC request
├── Day 60: Referral intro
├── Day 90: “90 days of grip” milestone
├── Day 180: Win-back if no repurchase
└── Day 365: Anniversary
```

| Touchpoint | Channel | Metric |
|------------|---------|--------|
| Confirmations | Email/SMS | Delivery rate |
| Getting started | Email | Support deflection |
| Review | Email → Judge.me | Review rate 10–15% target |
| Cross-sell | Email | Attach rate |
| UGC | Email/Social | Rights-cleared assets |
| Referral | Email | Referral rate |
| Win-back | Email + retargeting | Reactivation rate |

---

## 5. Win-Back Strategy

| Segment | Approach |
|---------|----------|
| 90-day lapse | Soft content + new colors (no heavy discount first) |
| 180-day | Modest incentive if needed (Owner-approved) |
| 365-day | Final brand reminder → suppress if no engagement |

**Channel order:** Email → Meta/Pinterest retargeting → stop.  
**Suppress:** Complaints, hard bounces, sunset non-responders.

---

## 6. VIP Program

| Item | v1 definition |
|------|----------------|
| Qualification | 3+ purchases OR ≥$200 LTV |
| Benefits | Early access, VIP email, thank-you recognition, ambassador consideration |
| Cadence | Quarterly VIP + launch early-access |
| Not yet | Points currency (see Loyalty Roadmap Phase 2+) |

---

## 7. Ambassador Program Architecture

**Status:** Architecture only (page exists: Ambassador). No full affiliate stack required for v1.

| Stage | Actions |
|-------|---------|
| Apply | Form on `/pages/ambassador` |
| Select | Studio instructor / aligned audience / brand fit / content quality |
| Onboard | Guardrails + Doc 07 facts + asset kit + hashtag `#BarreleticsMovement` |
| Activate | Content guidelines; gifting and/or future commission |
| Track | Manual UTM links until platform chosen |
| Grow | Featured instructor → brand partner path |

**Never** invent claims in ambassador briefs.

---

## 8. Wholesale Program Architecture

**Process today:** Manual via Help Scout / wholesale page.

```
Inquiry → Qualification → Terms → First order → Reorder → Growth
```

| Stage | Ops notes |
|-------|-----------|
| Inquiry | Saved reply; collect business type + location |
| Qualify | Legitimate retail/studio; not consumer gaming wholesale |
| Terms | INTERNAL pricing (e.g. trade discount off MSRP) — **never publish net wholesale prices on storefront** |
| Opening order | 10 pairs minimum (ops standard — confirm with Owner) |
| Reorder | Check-in cadence; display support materials |
| Growth | Volume tiers / display programs when ready |

Help Scout: use wholesale-specific replies; escalate pricing exceptions to Founder.

---

## 9. Studio Onboarding

```
Discovery → Application → Qualification → Onboarding → Activation → Retention
```

| Asset | Purpose |
|-------|---------|
| Digital welcome kit | Brand story, Open vs Closed, sock math, care |
| Instructor training | Fit, disciplines, returns framing |
| Marketing kit | Images, approved claims, hashtag |
| Spotlight program | Content trade for partners |
| Reorder path | Simple email/Help Scout reorder |

**Value prop:** Instructors get reliable grip gear students ask about; studios retail a durable SKU aligned with premium practice.

Track: partner list, reorder rate, spotlight pipeline.

---

## 10. UGC Collection Engine

| Source | Timing / method |
|--------|-----------------|
| Post-purchase email | Day 30 |
| Judge.me photo reviews | Review flow |
| Instagram | `#BarreleticsMovement` + manual rights ask |
| Ambassadors | Briefed shoots |

**Pipeline:** Collect → rights confirm → curate → place (PDP, social proof, email, ads).  
**Legal:** Written permission for ads; store release records.

---

## 11. Referral Engine

| Element | v1 architecture |
|---------|-----------------|
| Mechanism | Unique code or link (Shopify / referral app TBD) |
| Incentive example | Give $10 / Get $10 (Owner sets final) |
| Flow | Share → click → purchase → reward |
| Intro timing | Day 60 post-purchase + VIP |
| Fraud | Block self-referral; monitor code abuse |

Measure: referral rate, referred CVR, CAC impact vs paid social (~$0.74 rev/session watchout).

---

## 12. Review Engine

| Element | Spec |
|---------|------|
| Platform | Judge.me |
| Ask timing | Delivery +14d; follow-up +7d |
| Photo push | Encourage studio/context photos |
| Response | Help Scout owner or designee within 48h business |
| Negative | Empathy → policy-accurate resolution → escalate defects/warranty |
| Display | Custom theme modules (D-025); never hardcode stars |
| Mining | Pull quotes into Doc 07 / ads only if approved |

---

## 13. Loyalty Roadmap

| Phase | Timing | Scope |
|-------|--------|-------|
| 1 | Launch | Email VIP recognition + early access (no points) |
| 2 | ~6 months | Evaluate rewards app; launch referral; formalize ambassadors |
| 3 | ~12 months | Full loyalty only if LTV/repeat data justifies; future socks/apparel integration |

---

## Lifecycle Metrics Dashboard

| Stage | Metric | Target | Source |
|-------|--------|--------|--------|
| Awareness | New visitors | Baseline + growth | GA4 |
| Consideration | Email capture rate | 3–5% | Shopify/Klaviyo |
| Purchase | Conversion rate | Baseline + lift | Shopify |
| Onboarding | First review rate | 10–15% | Judge.me |
| Retention | Repeat purchase (12 mo) | 15–25% | Shopify |
| Advocacy | Referral rate | 5–10% of customers | Referral tool |
| Lifetime | LTV:CAC | >3:1 | Shopify + ads |

**Channel revenue benchmarks (sessions):** Organic ~$2.21 · Email ~$2.25 · Paid Social ~$0.74 (watch ROAS).  
**Revenue truth:** Shopify orders. Treat Meta/GA4 claims with overclaim awareness.

---

## Channel Priority Matrix

| Touchpoint | Email | SMS | Site | Ads | Social | Support |
|------------|-------|-----|------|-----|--------|---------|
| Welcome | Primary | If opted in | Popup | Retarget | — | — |
| Cart abandon | Primary | Secondary | Drawer | Retarget | — | — |
| Post-purchase | Primary | Transactional | — | — | UGC later | — |
| Review request | Primary | — | — | — | — | — |
| Win-back | Primary | — | — | Retarget | — | — |
| Support | — | — | Tidio | — | — | Help Scout |
| VIP | Primary | Exclusive OK | — | — | — | — |

---

## Support Integration

- **Tidio:** First-touch Q&A from Doc 07 (`m4b-tidio-knowledge-base.md`); hand off orders/refunds/wholesale/legal.  
- **Help Scout:** Saved replies (`m4b-helpscout-alignment.md`); <4h business / <24h weekend target.  
- Lifecycle emails must not contradict support macros (returns, warranty, shipping).

---

## Cross-References

- Brand / guardrails → `planning/02-brand-system.md`  
- Facts → `planning/07-product-knowledge-base.md`  
- Copy → `planning/08-copy-guide.md`  
- Knowledge cascade → `planning/13-knowledge-architecture.md`  
- M5 Growth scope → `planning/MILESTONES-4-5-6-ROADMAP.md`  
- Operating System (ops detail) → `docs/operating-system.md` (when merged)  
