# Partner Programs — Ambassador · Studio · Wholesale

**Status:** v1 proposal · 2026-08-08
**Scope:** public pages, application intake, email routing
**Repo surfaces:** `shopify-build/sections/page-{ambassador,studio-program,wholesale,partners}.liquid` · `shopify-build/templates/page.{ambassador,studio-program,wholesale,partners}.json`
**Not done here (owner/Brian tasks):** creating the four pages in Shopify Admin, nav links, redirect map update, Help Scout inbox creation, mail rules.

---

## 0. AMBASSADOR PROGRAM — DEFERRED TO PHASE TWO (owner, 2026-08-08)

> "I like the ambassador, but we still yet have to work out the program — earmark that for the second phase."

**The page is approved in shape. The program is not designed.** Those are two different things and must not be conflated.

**Every commission figure was deliberately blanked** from `templates/page.ambassador.json` and from the `sections/page-ambassador.liquid` schema defaults on 2026-08-08:

| Blanked figure | Where it used to appear |
|---|---|
| 10% commission on net sales | benefit block |
| 15% after $2,500 in a rolling 12 months | benefit block |
| 30% off personal orders | benefit block |
| 15% audience code | benefit block |
| $25 payout threshold | terms note + FAQ |

These were benchmarked against comparable instructor programs in §1 below. **They were never signed off.** On a plain page they read as a public offer.

**No figure returns to the page without Andrew's written approval.** Everything in §1–§2 of this document is research, not policy. Do not treat a number in this file as a source for page copy.

**What the page says now:** who it is for, and the response time. Nothing about compensation.

**Phase two, in order:**

1. Decide the compensation model — commission rate, any tier, personal discount, audience code, gifted product, payout threshold, attribution window, term.
2. Get it in writing from Andrew.
3. Populate the Theme Editor settings on the ambassador section. The page structure does not need to change to carry them.

**Step 1 is now drafted — see §2A (PROPOSED 2026-08-08, NOT APPROVED).** §2A supersedes §2 forward. Step 2 has not happened, so step 3 is still blocked and the page is still blank.

---

## 1. Research — how brands actually run ambassador programs

### 1.1 The five comp models in use

| Model | How it works | Where it fits |
|---|---|---|
| **Affiliate commission on code/link** | Ambassador gets a unique code + link, earns a % of tracked sales, paid monthly | The default for instructor programs. Zero fixed cost. |
| **Product only (gifting)** | Free or discounted product, no cash | Micro-audiences, seeding, first-touch relationships |
| **Tiered commission** | Base rate, steps up after a sales threshold | Rewards proven performers without overpaying every signup |
| **Gifting + affiliate hybrid** | Welcome product *and* a commission code | Most common in fitness/activewear — the product is the demo tool |
| **Paid flat fee for content** | Per-deliverable payment, usage rights | Campaign work, not an ongoing ambassador program |

### 1.2 Real numbers

**Commission rates, apparel/footwear (2026):**
- 8–15% is the standard planning band for apparel affiliate programs; below 10% struggles to attract creators who have alternatives. ([Override](https://overrideaff.com/blog/affiliate-commission-rates-by-industry), [Override apparel guide](https://overrideaff.com/blog/affiliate-program-for-fashion-brands))
- Mature fashion/beauty DTC programs run 8–15% mass / 5–10% luxury on first order, and affiliate ends up 18–30% of online revenue when the program is mature. ([Eightx, 2026](https://eightx.co/blog/average-ecommerce-affiliate-revenue-share-by-vertical-2026))
- Creator-commerce operators put apparel and footwear at 10–18% working range, 8–12% when AOV is high. Average creator rate across fashion brands on LTK sits 15–18%. ([Landing Partners](https://www.landing.partners/blog/creator-commerce-fashion-brand-affiliate-program))
- Tiering convention: base rate plus a **2–5 point** step for top performers, rather than starting at the ceiling. ([Override](https://overrideaff.com/blog/affiliate-commission-rates-by-industry))
- Cookie/attribution windows: 7–14 days for new programs, 21–30 days at the generous end. ([Landing Partners](https://www.landing.partners/blog/creator-commerce-fashion-brand-affiliate-program), [Kove T&Cs — 21 days](https://kovethebrand.com/pages/kove-instructor-ambassador-programme-terms-and-conditions))

**What instructor-specific programs actually publish:**

| Brand | Ambassador's own discount | Audience code | Commission | Notes |
|---|---|---|---|---|
| [MATE the Label](https://matethelabel.com/pages/ambassador) | 20%, capped at 20 uses / 6 months | same 20% code, shareable | 10% | Must be actively teaching; reapply every 6 months; product provided for hosted classes |
| [Kove](https://kovethebrand.com/pages/kove-instructor-ambassador-programme-terms-and-conditions) | 20% (non-shareable) | personal code + link | 10% on referrals, ex-VAT/shipping/discounts, paid monthly | Qualified Pilates/movement instructors only; 21-day cookie; last-click wins |
| [Lete Active](https://www.leteactive.com/pages/ambassador-program) | store discount or gifting | 25% | 10%, monthly payouts | Select creators up to $400 in product or paid campaigns; runs on Shopify Collabs |
| [Revel Athletic](https://www.revelathletic.com/pages/ambassador-program) | instructor discount (30% instructor pricing site-wide) | yes | yes | Runs on a third-party ambassador app |

The pattern is consistent and tight: **10% commission · ~20% personal instructor discount · 20–25% audience code · monthly payouts · no follower minimum, but a real teaching requirement.**

**Thresholds:** instructor-led programs gate on *teaching*, not followers — actively teaching in a studio setting with an engaged class (MATE requires active teaching and re-application every 6 months; Kove requires a recognized Pilates/movement qualification). Generic influencer programs are the ones that use follower floors (commonly 1k–10k). For Barreletics, class attendance is the better qualifier than follower count: an instructor with 400 followers who teaches 12 classes a week touches more feet than a 20k-follower lifestyle account.

### 1.3 Platforms and rough cost (build vs buy)

| Option | Cost | Read |
|---|---|---|
| **Shopify Collabs** | Free / built into Shopify (commission paid out through Shopify Billing) | What Lete Active uses. Cheapest real start. Creator-application flow included. |
| **UpPromote** | Free up to $3,000 reviewed referral sales/mo; Growth $29.99/mo + 2% of referral sales; Professional $89.99/mo + 1.5% | [Pricing](https://uppromote.com/pricing/) · [App listing](https://apps.shopify.com/affliate-by-secomapp). Best value at low volume; auto-tier commission is on the $89.99 plan. |
| **Refersion** | Launch $39/mo (+3%); Growth $199/mo (+2%) | Deeper reporting, no useful free tier. Overkill for v1. |
| **Social Snowball** | From $249/mo + 3% | Not justifiable at v1 volume. |
| **Manual (discount codes + a spreadsheet)** | $0 | Viable for the first ~20 ambassadors: one Shopify discount code per person, pull code usage from Shopify reports monthly, pay by PayPal/store credit. Breaks around 25–30 people. |

Cost comparisons cross-checked against [UpPromote vs Snowball vs Refersion, 2026](https://ecomaidaily.com/blog/uppromote-vs-social-snowball-vs-refersion-small-shopify-stores-2026/).

**Recommendation:** start manual or on Shopify Collabs. Move to UpPromote when you pass roughly 20 active ambassadors or $2–3k/mo of referral revenue — at that point the $29.99 + 2% tier is cheaper than the admin time.

> **SUPERSEDED FORWARD 2026-08-08 — see §7.** Owner asked for an app ("Find an app please"), so the manual start is off the table, and Shopify Collabs was pressure-tested and fails on creator eligibility for instructor-ambassadors. Current tooling proposal is **UpPromote Free ($0/mo, no revenue share)**. The cost table above is kept as history; §7 carries prices re-verified on 2026-08-08.

### 1.4 What wholesale / stockist applications ask for

Field lists pulled from real application pages and B2B templates ([Formbot template](https://tryformbot.com/templates/wholesale-application-form), [SoCal Blanks](https://scbwholesaleform.vercel.app/), [BrightLines](https://brightlinespaper.com/wholesale), [wholesale application template PDF](https://mcsprogram.org/default.aspx/u1272D/242165/Wholesale%20Application%20Template.pdf)):

Legal business name · DBA · entity type (LLC / corp / sole prop / partnership) · years in business · Federal EIN · state sales-tax / resale permit number · resale certificate upload · website · social handles · business type (retail store / studio / clinic / online / distributor) · number of locations · billing address · ship-to address · primary contact name, title, email, phone · secondary contact · sales channels (brick-and-mortar / e-comm / marketplaces / internal use) · product categories of interest · estimated opening order · estimated monthly or annual volume · preferred payment terms · trade references · how they heard about you · terms acknowledgement + signature.

Common gates seen on live pages: valid resale certificate, EIN or state business ID, and a **minimum opening order** (typically $250–$2,000; $500–$2,000 is the range vendors are told to set).

---

## 2. Recommended v1 ambassador program (opinionated)

> **SUPERSEDED FORWARD 2026-08-08 — see §2A.** Andrew responded to this draft and moved three of the numbers. §2A is the current proposal. This section is kept as the first-pass benchmark reasoning, not as the recommendation. Neither section is approved.

Deliberately boring, matched to what the category already pays, and runnable with no app.

**Name:** The Barreletics Collective

**Who qualifies:** actively teaching barre, Pilates, reformer, yoga, or sculpt. No follower minimum. Teaching evidence (studio link or schedule) required.

**Terms:**

| Lever | v1 | Why |
|---|---|---|
| Commission | **10%** of product subtotal on tracked orders | Category standard (MATE, Kove, Lete all at 10%) |
| Performance tier | **15%** after $2,500 in tracked sales in a rolling 12 months | Uses the 2–5 point step convention; nothing paid out until proven |
| Ambassador's own discount | **30% off personal orders**, not shareable | Matches instructor pricing already seen in the space; they must own the product to teach in it |
| Audience code | **15% off** for their clients | Deep enough to convert on a $72 item without training the market to wait for a sale |
| Attribution | 14-day cookie, last click / last code wins | Middle of the 7–30 day band |
| Payout | Monthly, on completed orders only, net of returns and refunds | Standard, and the only version that survives a returns-heavy category |
| Welcome product | One free pair for ambassadors teaching **8+ classes/week** | Gifting where it demonstrably gets on feet; not a blanket cost |
| Content ask | 1 post or reel per month, plus one story when a new colorway drops. Usage rights granted. | Low enough that instructors actually comply |
| Term | 6 months, renewable on re-application | MATE's re-application cadence keeps the roster live |
| Kill switch | Codes on marketplaces/coupon sites, or misrepresenting the product, ends the agreement | Coupon leak is the main failure mode of a public code |

**Cost check at $72:** a 15% audience code puts the order at $61.20; 10% commission is ~$6.12. Blended give-away is roughly 25% of gross on referred orders — inside the 8–15% commission plus promo band the category runs, and only paid on incremental sales.

**Launch sequence:** publish the page → invite 10–15 instructors you already know by name → issue one Shopify discount code per person → pay monthly from Shopify's discount-code report → move to UpPromote when the spreadsheet hurts.

**Copy rules observed:** the retired newsletter discount is not reintroduced anywhere, banned venue language stays out per `.cursor/rules/no-pool-positioning.mdc`, and the product is "Performance Skins" — not socks, not shoes.

---

## 2A. PROPOSED v1 — 2026-08-08 · NOT APPROVED

> **STATUS: PROPOSED / NOT APPROVED.** This is a recommendation written in response to Andrew's 2026-08-08 questions. **No figure below may be entered into `templates/page.ambassador.json`, the `page-ambassador.liquid` schema defaults, or any Theme Editor setting until Andrew approves in writing.** §0 still governs: the page stays blank. Supersedes §2 forward.

### 2A.1 The four levers are four different things

Andrew's question — *"are you saying their clients get 15% off and then the instructors that they sell to get 30% off?"* — reads the 30% and the 15% as two tiers of customer discount. They are not. They are separate levers paid **to and by different people**, and they can be set independently:

| # | Lever | Who gets it | What it is |
|---|---|---|---|
| 1 | **Commission** | Ambassador, in cash | What she **earns** on sales other people make through her code or link. Money out of the brand, into her bank account. |
| 2 | **Her own discount** | Ambassador, as a buyer | What **she personally pays** when she buys product for herself. Never shareable, never commissionable. |
| 3 | **Audience code** | Her students | What **her followers/students get off** when they use her code. A price reduction on their order, not a payment to her. |
| 4 | **Gifted pair** | Ambassador, once | A **free pair on acceptance** so she has the product on her feet in class. Costs COGS, not retail. |

Lever 1 is her income. Lever 2 is her price. Lever 3 is her students' price. Lever 4 is her sample. Levers 1 and 3 both come out of the same referred order — that is the stacking risk, handled in §2A.6.

### 2A.2 Recommended v1 — the whole program

| Lever | v1 number | Basis |
|---|---|---|
| **1 · Commission** | **10%** of the post-discount product subtotal, excluding shipping and tax, reversed on returns | Every direct instructor-program comparable pays 10% (MATE, Kove, Lete, Vital Apparel). Shopify's own Collabs guidance says merchant programs "usually are set at around 10% on average." |
| **2 · Her own discount** | **25%** off her personal orders. Not shareable. No commission earned on her own orders. | Andrew's number, and it lands mid-market between the 20% floor (MATE, Kove) and the 30–40% top (Climate, Revel, Vital tier 2, Warrior Addict). See §2A.5 — the gifted pair makes this the least consequential of the four. |
| **3 · Audience code** | **15%** off for her students | Sits at the top of the published 10–15% customer-discount band for fashion/apparel and matches the depth of the buy-2 offer already running, so it introduces no new price point. **This is the one number that moves if COGS is high — see §2A.7.** |
| **4 · Gifted pair** | **One free pair on acceptance**, her choice of sole and colorway. One pair, once — not a recurring stipend. | Standard in instructor programs, and the cheapest lever he has. See §2A.4. |
| Platform | **Shopify Collabs.** Free to install; 2.9% processing fee on commission actually paid. Application flow, code/link generation, tracking, and payouts are built in. | Already identified as the tool. No app subscription in v1. |
| Attribution | **Leave Collabs at its 30-day default.** Do not tune it. | 30 days is the Collabs baseline and the fashion/apparel standard. |
| Payout | Collabs' default holding period (30 days) and $25 minimum, billed through the Shopify bill | Holding period auto-reverses commission on returns inside the window. Nothing to administer. |
| Who qualifies | Actively teaching. Evidence = a studio schedule link or class listing with her name on it. **No follower minimum.** | Instructor programs gate on teaching; follower floors are a general-influencer mechanic. An instructor with 400 followers teaching 12 classes a week touches more feet than a 20k lifestyle account. |
| Roster size | **Invite-only for v1 — roughly 10–15 instructors Andrew already knows by name.** The public application page can collect applications; v1 acceptances come off the invite list. | This is what makes lever 4 safe. See §2A.4. |
| Term | 6 months, renewable | MATE re-applies every 6 months; keeps the roster live without a cancellation conversation. |

### 2A.3 Is 10–15% commission what other brands do?

Yes — 10–15% is squarely the market, and **10% is specifically the instructor-program number.**

- **The broad band:** apparel and fashion affiliate programs run **8–15%** on first order ([Eightx 2026](https://eightx.co/blog/average-ecommerce-affiliate-revenue-share-by-vertical-2026), [track360 2026](https://track360.io/blog/ecommerce-affiliate-commission-rates-structures-2026)). UpPromote's 2026 industry table puts Fashion & Apparel at **8–15%, median 12%**, and Fitness & Sports at **8–12%, median 10%** ([UpPromote](https://uppromote.com/blog/shopify-affiliate-commission-rates/)). Shopify's own guide puts physical goods at 5–15%, with 10–15% for well-known publishers ([Shopify](https://www.shopify.com/uk/blog/affiliate-commission)).
- **What instructor programs actually publish:** MATE the Label 10%, Kove 10%, Lete Active 10%, Vital Apparel 10%. The 15% payers — [Warrior Addict](https://warrioraddict.com/pages/terms-conditions-brand-ambassadors), [CLIMATE](https://www.climateclothing.co.uk/ambassador-termsandconditions) — both pair 15% commission with a **10%** audience code, i.e. they buy the higher headline rate by giving the customer less.
- **So 15% is not wrong, it's a trade.** Nobody in this set gives 15% commission *and* a 15% audience code. Andrew can have the higher commission or the deeper customer discount, not both, unless he wants ~28% of gross going out the door on every referred order.

**Recommendation: 10%.** These are instructors, not content creators. A creator with an LTK account is comparing your rate against every other brand's rate and will route her post to whoever pays most — rate is the whole negotiation. An instructor selling from the front of a room is not rate-shopping; she recommends what she actually wears and what stops her students sliding. Paying 15% buys no additional loyalty from that person, and it costs 50% more per order. Hold the extra 5 points in reserve as the thing to offer the two or three who turn out to be real producers.

### 2A.4 The gifted pair — Andrew is right, and it's probably his best-value lever

**Is it standard?** Yes, in this category specifically. MATE provides product for hosted classes. Lete Active gifts up to $400 in product. Warrior Addict lists gifting as a program pillar. Gymshark's entire creator pipeline starts with seeding — free product, no obligation, used as an audition ([ContentGrip](https://www.contentgrip.com/gymshark-creator-partnership-program/), [AmbassadorFlow seeding guide](https://ambassadorflow.com/influencer-seeding)).

**On acceptance, or after a threshold?** The published counter-argument is real: some DTC playbooks hold free product until the ambassador drives her first referral, precisely because a public application form attracts people chasing free stuff — Gymshark cites this as its reason for not running a public form at all ([D2C Times](https://d2c-times.com/how-to-build-a-profitable-ambassador-program-that-scales-to-10m/)).

**Recommend gifting on acceptance anyway**, for two reasons:

1. **The product is the sales tool, not content fodder.** An instructor cannot recommend the grip she hasn't stood on. Withholding the pair until she's sold one is backwards — it asks her to sell a product she doesn't own, to a room that can see her feet. This is the structural difference between an instructor program and a general creator program, and it's why the threshold convention doesn't transfer.
2. **The free-product risk is solved by the roster, not by a threshold.** Making v1 **invite-only** — Andrew hand-picking 10–15 instructors he already knows — removes the applicant-chasing-free-stuff problem entirely, without building any tracking. A threshold would reintroduce exactly the per-person counting he has said he doesn't want.

So: **one pair, on acceptance, invite-only cohort.** If the public form later becomes the intake route, that's the moment to add a gate — not now.

**Cost:** a gifted pair costs **landed COGS plus shipping**, not $74 of revenue. Nothing is foregone unless that instructor would have bought a pair at full price, which — for someone being recruited to represent the brand — she mostly wasn't going to. Commission and the audience code are **recurring** costs that fire on every referred order forever; the gifted pair is a **one-time** cost that fires once per ambassador. On a 15-person cohort it is 15 × COGS, full stop. **The benchmarks support calling this the cheapest and highest-goodwill lever of the four — but the actual number depends on Andrew's landed cost, which is not in the repo.** See §2A.7.

### 2A.5 How the gifted pair changes lever 2 — 25% vs 30% gets smaller

It changes it in Andrew's favour, and the answer is: **hold at 25%.**

Once she has a free pair, her personal discount is no longer how she gets the product — it's how she buys her **second** pair: the other sole, a new colorway, a replacement. That's an occasional purchase, not her entry point. The gap between 25% and 30% on $74 is **$3.70 a pair**, on a purchase she makes maybe two or three times a year. It is a rounding error in her mind and in the P&L, which is exactly why it isn't worth spending the margin on.

Two further reasons to stop at 25%:

- **It protects the studio and wholesale programs.** 25% off $74 is **$55.50**. Any plausible wholesale or studio price sits well below that, so an instructor buying at ambassador pricing never undercuts a studio buying at trade pricing. Push the personal discount toward 40% and that gap starts closing, and studios discover their instructors can buy cheaper than the shop can. This is a structural reason, not a taste one.
- **25% is genuinely mid-market**, not stingy: MATE 20%, Kove 20%, CLIMATE 30%, Revel 30%, Vital tier 2 30%, Warrior Addict 40%. Paired with a free pair on day one, a 25% standing discount is a better total package than MATE's or Kove's.

### 2A.6 Stacking — the thing to get right on day one

Levers 1 and 3 both come out of the **same order**. On a $74 pair:

| | |
|---|---|
| Student pays, with the 15% code | **$62.90** |
| Discount given up | $11.10 |
| Commission at 10% of the **$62.90 net** | $6.29 |
| Collabs 2.9% processing on that commission | $0.18 |
| **Total out the door on a referred order** | **$17.57 — about 23.7% of gross** |

That is inside the range the category runs, but it is only defensible because it's paid **on incremental sales that mostly wouldn't have happened**. Three rules keep it there:

1. **Commission is calculated on the post-discount subtotal**, excluding shipping and tax. Kove and CLIMATE both spell this out. Paying 10% on gross instead adds $1.11 per order for nothing.
2. **The ambassador code must not combine with the existing buy-2-save-15% offer.** In Shopify, code and automatic discounts do not combine unless combinations are explicitly enabled — leave them off. If they stack, a student gets roughly 28% off and the order goes underwater.
3. **No commission on her own orders.** Universal in the comparables (Vital and Warrior Addict both state it; Warrior Addict voids the sale outright). Prevents the personal code and the affiliate link being used together to buy at 25% off *and* earn 10% back.

### 2A.7 The one number needed from Andrew

**Landed cost per pair — COGS including freight and duty.** That single figure sets or confirms all four levers, and it is not in the repo. Retail is **$74** standard / **$78** limited-edition (`docs/09-PRODUCT-KNOWLEDGE.md`). *Note: §2's cost check above used $72 — that was wrong; the correct anchor is $74.*

Conditional answer, so he can approve without waiting:

- **If landed cost is under ~$30/pair:** the recommendation above stands as written. A referred order nets about $56.51 before shipping and payment fees, which clears comfortably, and a gifted pair costs less than half of one referred order's revenue.
- **If landed cost is ~$30–$37/pair:** still workable, but the gifted pair should be treated as a real budget line — 15 pairs is $450–$555 of inventory at cost — and reviewed at 6 months rather than renewed automatically.
- **If landed cost is above ~$40/pair:** **drop the audience code from 15% to 10%** first. That recovers $3.70 per order and puts the program at 15%+10% — CLIMATE's and Warrior Addict's exact structure. Cut the audience code before cutting commission or the gifted pair, because the audience code is the lever her students notice least and the other two are what actually motivate her.

The general rule the sources agree on: **maximum sustainable commission is roughly 30–50% of net margin**, and rates should be set from contribution margin after returns, not from category averages ([UpPromote](https://uppromote.com/blog/shopify-affiliate-commission-rates/), [track360](https://track360.io/blog/ecommerce-affiliate-commission-rates-structures-2026)).

### 2A.8 Deliberately NOT in v1

| Not doing | Why |
|---|---|
| **The 15%-after-$2,500 performance tier** (from §2) | It requires tracking a rolling 12-month sales total per person and telling someone they've been demoted. That's the complexity Andrew has rejected all day. Nobody earns it in year one anyway. Add it the month someone actually gets close — and it becomes a nice phone call instead of a policy. |
| **Recurring product stipends / seasonal ambassador boxes** | One free pair, once. Monthly shipments are an inventory and fulfilment job with no attribution attached. |
| **A follower minimum** | Wrong filter for this population, and it screens out the best candidates. Teaching evidence instead. |
| **An enforced content quota** | Ask for a post when she gets the pair and a mention when a colorway drops. Do not police it in v1 — policing a quota across 15 people costs more than the posts are worth. |
| **A paid affiliate app** (UpPromote, Refersion, Social Snowball) | Collabs is free and does everything v1 needs. Revisit at roughly 20+ active ambassadors or $2–3k/mo referral revenue. |
| **Tuning the attribution window** | Collabs' 30-day default is also the category standard. Changing it is a decision with no upside at this size. |
| **Publishing any of this on the page** | §0 stands. The page stays blank until written approval. |

### 2A.9 Launch sequence if approved

1. Andrew confirms landed cost and approves the four numbers in writing.
2. Install Shopify Collabs; create one program with 10% commission and a 15% audience code; leave holding period and attribution at defaults.
3. Turn off discount combinations so the ambassador code can't stack with buy-2-save-15%.
4. Invite 10–15 named instructors. Ship one pair each on acceptance.
5. Populate the ambassador page settings — **only then**, and only with the approved figures.
6. Review at 90 days: who sold anything, who posted, who went quiet. That review is what tells you whether a 15% tier is worth building.

**Copy law observed in this section:** no "fully enclosed" phrasing, no discipline assigned to a sole, no banned venue language (`.cursor/rules/sole-description-language.mdc`, `.cursor/rules/no-pool-positioning.mdc`). None of these figures were written to any template, schema default, or Theme Editor setting.

---

## 3. Form field lists (as built)

Every form posts through Shopify's native `{% form 'contact' %}` — the same mechanism `page-contact.liquid` already uses. Every form carries a hidden `contact[form_id]` routing token and a hidden `contact[subject]`.

### 3.1 Ambassador — `BL-PARTNER-AMBASSADOR`
First name* · last name* · email* · city/state* · discipline* · certification · years teaching · studio name (or independent) · studio URL · classes per week · clients per week · Instagram · TikTok · audience size · other links · does your studio already stock Barreletics* · do you already own a pair · about you + how you'd talk about the grip* (`contact[body]`) · how you heard about us · terms consent*

### 3.2 Studio Program — `BL-PARTNER-STUDIO`
Studio name* · **studio website URL*** · studio Instagram · city/state* · number of locations* · instructors on staff · primary discipline* · weekly client visits · contact name* · role* · email* · phone · **background on the studio and on you*** (`contact[body]`) · **what they want to carry** (open sole / closed sole / instructor-only / retail shelf / new-member gifting) · intended opening quantity · brands currently stocked · resale/tax ID · how they heard about us

The three items the owner asked for verbatim — studio link, background, what they want to carry — are all required or prominent.

### 3.3 Wholesale — `BL-PARTNER-WHOLESALE`
Legal business name* · DBA · business type* · entity type · years in business · number of locations · website* · Instagram · EIN · state sales-tax / resale permit number · resale certificate on file* · sales channels (storefront / studio desk / own website / marketplace / internal use) · product interest (open sole / closed sole / undecided) · first order size* · expected annual volume · brands currently carried · contact name* · role · email* · phone · AP/billing email · ship-to city/state* · about the business* (`contact[body]`) · how they heard about us · terms consent*

Deliberately **not** on the public page: per-pair wholesale pricing, margin, MOQ dollar figures, payment terms. Those go in the reply, not on the page. Resale certificate is asked as a yes/no plus permit number — Shopify's native contact form cannot take a file upload, so the PDF gets requested in the reply.

### 3.4 Partners hub — `BL-PARTNER-GENERAL`
Name* · email* · which program* · message. This is a fallback for people who land on the hub and don't self-select.

---

## 4. Routing / intake workflow

### 4.1 How the Shopify form actually behaves (verified 2026)

- `{% form 'contact' %}` delivers **every** submission to the store's **Sender email** (Settings → Notifications). There is no per-form recipient. ([Shopify Help Center](https://help.shopify.com/en/manual/online-store/themes/customizing-themes/add-contact-page))
- The recipient cannot be overridden in theme code. Shopify's own documented workaround is a third-party form app or embedded form service.
- `contact[body]` is run through Shopify's spam filter; flagged mail arrives with a `[SPAM]` subject prefix. Don't let a spam-prefixed application silently bypass the rule — match on the body token, which survives the prefix.
- So: **routing has to happen after delivery**, on the mail side. That is what the hidden `contact[form_id]` token is for. It appears in the email body of every application as a stable, unique string.

### 4.2 The recommendation

**One dedicated Help Scout inbox for applications, fed by a mail-server rule. No Google Group.**

1. Create a second Help Scout inbox — call it **Partners** — with its own address, e.g. `partners@barreletics.com`. Help Scout Standard includes 2 inboxes, Plus includes 5; extra inboxes are **$10/mo annual ($12 monthly)**. ([Help Scout pricing](https://www.helpscout.com/pricing/), [billing guide](https://docs.helpscout.com/article/596-price-and-plans-guide))
2. In that inbox, **Manage → Inbox → Partners → Auto Reply → toggle off → Save**. Auto Reply is a per-inbox setting, so the support inbox keeps its auto-reply and the Partners inbox sends nothing automatically. ([confirmed current](https://www.guideflow.com/tutorial/how-to-disable-auto-reply-in-helpscout))
3. In Google Workspace (or whatever hosts the Sender email), add a filter on the support mailbox: *body contains `BL-PARTNER-`* → forward to the Partners inbox address, skip the inbox, apply label `Partners`. One rule covers all four forms; add per-token rules only if you want separate tagging.
4. In Help Scout Partners, add three **automatic workflows** keyed on body text — `BL-PARTNER-AMBASSADOR`, `BL-PARTNER-STUDIO`, `BL-PARTNER-WHOLESALE` — each doing: add tag, assign to owner. Optionally add *Reply to the Customer* on the wholesale/studio workflows only, if a "we got it, here's what happens next" note is wanted. Workflows fire once per conversation, so no loops. ([conditions/actions](https://docs.helpscout.com/article/502-workflow-condition-action), [automatic workflows](https://docs.helpscout.com/article/1399-automatic-workflows))

**The auto-reply answer, plainly:** yes — a dedicated inbox with Auto Reply switched off is the clean way, because auto-reply is per-inbox. If he'd rather keep everything in one inbox, the alternative is to leave the inbox-level auto-reply off entirely and re-create it as a workflow that *excludes* conversations whose body contains `BL-PARTNER-`. That works, but it makes the general support auto-reply depend on a condition that will silently break the day someone changes a token. The dedicated inbox is worth the $10/mo.

### 4.3 Google Group — skip it

A Group is an extra hop that actively degrades the data:

- When mail arrives from a domain with a strict DMARC policy, Google Groups **rewrites the `From:` header to the group address** and moves the original sender to `Reply-To`. Downstream systems then see the group as the sender. ([DMARCTrust](https://www.dmarctrust.com/troubleshooting/forwarding-and-arc), [Google forum](https://discuss.google.dev/t/google-group-shows-sender-as-group-address/338650))
- Help desks hit exactly this: tickets get created with the group address as the requester instead of the real person. Atlassian's documented fix for the identical setup is "use a direct mailbox, not a group." ([Atlassian](https://support.atlassian.com/jira/kb/reporter-shows-helpdesk-email-in-jsm-cloud-requests/))
- Group footers and subject prefixes also break DKIM body hashes on the way through.

A Group is the right tool for *notifying several humans*. It is the wrong tool for *feeding a ticketing system*. If he wants Brian or a VA to see applications, add them as Help Scout users — not as Group members.

### 4.4 Teams — leave it out

Teams isn't an intake channel and shouldn't hold application state; the reply has to come from the brand address and the thread has to live where the history is. The legitimate use is a **notification**: Help Scout can post to Slack natively, and to Teams via Zapier/Make, so a new-application ping lands in a channel while the conversation stays in Help Scout. Nice-to-have, not part of v1.

### 4.5 Owner checklist

1. Create the four pages in Shopify Admin with handles `ambassador`, `studio-program`, `wholesale`, `partners`, and assign the matching templates.
2. Confirm the Sender email in Settings → Notifications is a mailbox you can write filter rules on.
3. Create the Help Scout **Partners** inbox; turn its Auto Reply off.
4. Add the `BL-PARTNER-` forwarding rule on the Sender mailbox.
5. Add the three tagging workflows in the Partners inbox.
6. Submit one test application per form and confirm: arrives in Partners, tagged correctly, **no auto-reply sent**, and the support inbox auto-reply still works for normal mail.
7. Nav + redirects — **UPDATED 2026-08-08 (D-048).** The three folding 301s (`/pages/ambassador`, `/pages/wholesale`, `/pages/studio-program` → `/pages/partners`) are now **retired in `planning/m4a-redirect-map.md`** and removed from its bulk-import CSV. *This item previously read that the redirect map "currently sends" those three to the hub and that they must be removed — that is no longer true of the repo.* Remaining owner task: confirm those three redirects are **absent from Shopify Admin** (Online Store → Navigation → URL Redirects); if an earlier CSV was already imported, delete them or the new pages are unreachable. `/pages/become-an-affiliate` and `/pages/wholesale-calculator` → `/pages/partners` are **correct** and stay.

---

## 5. What was built in the repo

Templates were already present and composing existing sections; content and forms were written into them.

| Page | Template | Sections |
|---|---|---|
| `/pages/ambassador` | `templates/page.ambassador.json` | `page-ambassador` → `geo-section` → `contact-cta` |
| `/pages/studio-program` | `templates/page.studio-program.json` | `page-studio-program` → `geo-section` → `contact-cta` |
| `/pages/wholesale` | `templates/page.wholesale.json` | `page-wholesale` → `geo-section` → `contact-cta` |
| `/pages/partners` | `templates/page.partners.json` | `page-partners` (hub) → `contact-cta` |

- All four section files rewritten with real content, full schemas, presets, and Theme-Editor-editable copy. Program terms (commission %, discounts, thresholds) are **settings**, not hardcoded, so terms can change without a code edit.
- `page-partners.liquid` repurposed as a router: three cards linking to the dedicated program pages, plus a general-inquiry fallback form.
- Every form carries `contact[form_id]` with a `BL-PARTNER-*` token.
- All eight files pass Shopify Theme Check.
- No new sections invented; no `chrome.css`, header, footer, design-tokens, nav-spec, or `docs/*.html` files touched. Nothing committed.

### Visual QA pass — 2026-08-08

Rendered and audited at 1440px and 390px: `planning/partner-pages-qa/` (harness, screenshots, per-page audit JSON, README). All four pages come out clean — no horizontal overflow, no tap target under 44px, no sticky-header collision, no sentence-case copy below 13px. Four fixes went in during the pass:

1. `page-partners.liquid` moved onto the Type OS classes (`.type-hero` / `.h2-standard` / `.type-lede` / `.type-body`). It was still carrying 32px/700 and 28px/700 headings and a mobile hero override that fought `--type-hero-size-mobile`. Its schema defaults were also stale Title Case ("Get in Touch", "Represent the Next Generation of Grip") and now match the approved template copy in sentence case.
2. Checkbox rows on the wholesale and studio forms measured 21–41.6px tall. `.page-*__check` / `.page-*__consent` now carry a 44px minimum with the whole label as the hit area.
3. The hero CTAs jump to `#*-apply`, which landed the form heading behind the 57px sticky header on mobile. Each anchored section now sets `scroll-margin-top: 96px` in its own `<style>`.
4. Terms notes, hints, pricing notes, and consent text were using `--text-sm`, which resolves to the 11px *label* token. Moved to `--type-trust-size` (13px). Uppercase micro-labels stay at 11px, matching `page-contact.liquid` and the rest of the theme.

Flagged, not changed: `contact-cta.liquid` — reused by all three program pages and the FAQ — hardcodes `32px/700`, `15px`, and `11px/700` instead of Type OS tokens. Fixing it is a sitewide type change and belongs to that section's owner.

### Architecture note — flagged, not resolved

`planning/m4-section-library-CONTRACT.md` and decision **D-042** consolidated all three programs onto `/pages/partners` and marked these `page-*` monoliths for deletion after decomposition. Owner direction on 2026-08-08 asks for three dedicated pages with their own intake forms, so the current message wins and the existing files were extended forward rather than reverted or deleted. Two follow-ups for whoever owns the contract:

1. ~~D-042 should be superseded forward in `docs/10-DECISIONS.md` to record three program pages + a hub.~~ — **DONE 2026-08-08.** Recorded as **D-048** in `planning/10-decision-log.md` (the live decision log; D-042 was never in `docs/10-DECISIONS.md`). D-042's original text is preserved there as history under a SUPERSEDED banner. The downstream doc sweep is also done — see the D-048 cross-references in `planning/m4a-redirect-map.md`, `planning/page-inventory-decisions.md`, `planning/m4a-content-inventory.md`, `planning/m4a-navigation-config.md`, `planning/m4-section-library-CONTRACT.md`, `docs/03-section-library.md`, `PROJECT_DASHBOARD.md`, `specs/frozen/{wholesale,ambassador,studio,navigation}.md`, and `specs/implementation-maps/{wholesale,ambassador,studio}.md`.
2. If the long-term goal is still no `page-*` monoliths, the right decomposition is a shared `partner-application` section with a program-type setting, plus reuse of `fifty-fifty` / `value-strip` / `collection-faq` for the editorial parts. That's a refactor, not a v1 blocker. Noted forward in the CONTRACT so its **DELETE after decompose** rows are not misread as deprecation.

---

## 6. Inferences — what I could not verify

**No Help Scout access.** No connector, no API, no saved replies. Everything about the current setup below is inferred:

1. **Current intake questions are unknown.** All three field lists were built from external brand application pages and B2B templates, plus the owner's stated asks — not from their saved replies. Fields may duplicate or contradict what support already asks.
2. **Plan tier unknown**, so the inbox headroom is unknown. If they're on Standard, the second inbox may already be used; the Partners inbox could be the $10/mo add-on. If they're on Plus, it's free.
3. **Existing auto-reply text and trigger unknown.** I'm assuming a standard inbox-level auto-reply on the support inbox. If it's already implemented as a workflow, step 2 of the routing plan changes to editing that workflow's conditions instead.
4. **Sender email identity unknown.** The plan assumes the Shopify Sender email is a real Google Workspace mailbox where filters can be written. If it's a Shopify-managed forwarding address, the filter has to live on the destination mailbox instead.
5. **Existing partner-inquiry volume unknown**, so the tagging scheme is a guess at useful granularity.
6. **`planning/m4b-helpscout-alignment.md` §7 already drafts a wholesale/partner saved reply** pointing at `/pages/partners`. That doc is a repo *proposal*, not a mirror of live Help Scout, so I did not treat it as evidence of current behavior. If it was implemented as written, its link needs updating to the new hub cards.
7. **Wholesale economics unknown.** No wholesale price, MOQ, margin, or payment terms exist in the repo, so the page asks about volume without publishing terms, and the form deliberately omits payment-terms selection. Owner to supply before the first reply template.
8. **Ambassador terms are a proposal, not approval.** §2's 10/15/30/15 numbers and §2A's 10/25/15/free-pair recommendation are both benchmarked to the category. Neither is signed off.
9. **Landed cost per pair is unknown.** No COGS, freight, or duty figure exists anywhere in the repo, so every margin statement in §2A is conditional. Retail ($74 / $78 LE) is the only verified price input.

### What would tighten this — asks for the owner

- The Help Scout saved replies for wholesale, studio, and ambassador inquiries, verbatim.
- Which Help Scout plan, and how many inboxes are already in use.
- Whether the support auto-reply is an inbox Auto Reply or a workflow, and its current text.
- The exact Sender email address and where it actually lands.
- Wholesale price list, MOQ, and payment terms — internal, for the reply not the page.
- Any commitments already made to existing studio partners or instructors, so v1 terms don't undercut them.
- **Landed cost per pair (COGS incl. freight and duty).** The single number that confirms or moves all four ambassador levers in §2A. Everything there is conditional without it.

---

## 7. Tooling — what actually runs the program · PROPOSED / NOT APPROVED · 2026-08-08

> **PROPOSED — NOT APPROVED.** Nothing in this section is installed, purchased, or configured. No app was installed, no store setting was changed, no theme command was run. Every price below was checked on **2026-08-08** against the vendor's own pricing page or Shopify's own documentation; app pricing moves, so re-check before paying.
>
> **Supersedes forward** the one-line platform advice in §1.3 ("start manual or on Shopify Collabs"). §1.3's cost table is still broadly accurate and is kept as history. This section is the current tooling proposal.
>
> Scope note: this section covers **software only**. Commission rate, personal discount, audience code, and gifted pair are §2A's job — see there, not here.

### 7.0 The decision, in one line

**Install UpPromote: Affiliate Marketing, stay on the Free plan — $0/month, no revenue share.** It is the only option checked that gives every ambassador a unique code, self-serve applications, and a running ledger of commission owed, without gating on the ambassador's follower count and without a percentage cut of sales.

Owner direction on 2026-08-08, in order, was: *"Do we need an app? Find one that works well, is simple and affordable."* → *"Unless you can build something out, or we use a Shopify Flow."* → **"Find an app please."** The manual and custom-build paths are therefore **not recommended**, and are retained below in §7.4 and §7.5 as record only.

---

### 7.1 The recommendation — UpPromote, Free plan

**App:** UpPromote: Affiliate Marketing (developer: Secomapp) — [App Store listing](https://apps.shopify.com/affliate-by-secomapp) · [pricing page](https://uppromote.com/pricing/) · [docs](https://docs.uppromote.com/)

**Cost at his scale: $0/month.** Free plan, permanent, not a trial.

| | Free (recommended) | Growth (only if he outgrows Free) |
|---|---|---|
| Monthly | **$0** | $29.99/mo ($24.99 billed yearly) |
| **Performance fee / revenue share** | **None** | **2% of approved referral sales** |
| Affiliates | Unlimited | Unlimited |
| Programs | 1 | Unlimited |
| Referral sales reviewed per month | **$3,000** | 300 referral orders |
| Coupons per affiliate | 1 | 1 |

*Verified from [uppromote.com/pricing](https://uppromote.com/pricing/), fetched 2026-08-08. Tier list cross-checked against [docs.uppromote.com](https://docs.uppromote.com/).*

**Per-order fee or revenue share — asked explicitly, answered explicitly: NO, not on Free.** The Free plan's performance fee is listed as *None*. The revenue share starts only if he upgrades: **2%** on Growth, 1.5% on Professional, 1% on Enterprise, each charged monthly on approved referral sales *on top of* the subscription. He is cost-sensitive, so this is the number to watch — see the graduation trigger in §7.3. There is no per-order flat fee on any tier.

**What it does that he asked for:**

| His requirement | UpPromote Free |
|---|---|
| Unique discount code per ambassador | Yes — 1 coupon per affiliate, assigned to them and tracked |
| Unique referral link | Yes — link tracking included on Free |
| Attribute orders to a person over time | Yes — link *and* coupon attribution, with a configurable delay before orders auto-approve so returns fall out first |
| Calculate commission owed | Yes — per-affiliate ledger, fraud detection included on Free |
| **Pay the ambassadors** | **Partly — see §7.2. This is the catch.** |
| Ingest applications from the page we built | Yes — see §7.1.1 |
| Gift product without a mess | Not on Free — see §7.2 |

#### 7.1.1 It connects to the ambassador page — no re-keying

UpPromote hosts a **branded affiliate registration form** per program. Applicants fill it in, land in the Affiliates tab, and he approves or declines. On the **Free** plan he can add custom fields — short answer, long answer, checkbox, dropdown, and multiple checkboxes — so discipline, studio name, studio URL, classes per week, and Instagram handle all fit. **File upload is Growth-only**, which does not matter here since the ambassador form asks for no documents. ([add/edit form fields](https://docs.uppromote.com/management/affiliate-registration-form/add-more-fields))

So the `/pages/ambassador` page we built becomes the **pitch**, and its Apply button points at the UpPromote registration link. Nobody gets re-keyed by hand.

One consequence to accept knowingly: the actual form then lives on UpPromote's hosted page, not in our Liquid. The `BL-PARTNER-AMBASSADOR` native form in §3.1 and its Help Scout routing in §4 would become **redundant for ambassadors** — studio and wholesale keep theirs. Alternative, if he wants applications to keep arriving as email in Help Scout: leave the native form in place and re-key the approved ones into UpPromote. That is 2 minutes per approved ambassador and preserves the intake he already has. **Either is defensible; the registration-link route is the one that matches "simple."**

---

### 7.2 What it will NOT do — read this before installing

**1. On Free, it does not send the money. This is the one real limitation.** UpPromote collects each ambassador's payment details, calculates exactly what each is owed, and records payment — but on Free he pays them **outside the app** (PayPal, Venmo, bank transfer, whatever) and then clicks **Mark as paid**. UpPromote's own docs are blunt about it: *"the system will not pay your affiliate or connect to any of your payment methods."* ([manual payouts](https://docs.uppromote.com/management/payments/manual-payouts))

For 10–15 ambassadors that is one sitting a month: open Payments → Manual, see the list, send the payments, tick them off. It is bookkeeping, not spreadsheet-building — the amounts are already computed. But he should not install expecting one-click payouts.

> **Vendor doc inconsistency, flagged:** UpPromote's pricing page lists *Auto-pay with PayPal* as a **Professional** ($89.99) feature, and its docs contradict themselves — [one page](https://docs.uppromote.com/management/payments) says PayPal auto-payout is "Growth plan and above," [another](https://docs.uppromote.com/management/payments/in-app-payments) says "Professional plan and above." Confirm in-app before upgrading for that reason alone. Do not budget for automated payouts on the strength of this doc.

**2. No tiered commission on Free or Growth.** *Auto tier commission* — the mechanism that would step an ambassador from a base rate to a higher rate after they cross a sales threshold — is **Professional ($89.99/mo) and up**. Free supports 2 commission levels by order value, which is a different thing. **If §2A's approved terms include a performance tier, it has to be administered by hand at v1** (move the ambassador into a higher-rate program manually), or the tier waits.

**3. Codes are not auto-generated on Free.** *Auto-generate coupon on signup* is Professional-and-up. On Free he creates each ambassador's discount code in Shopify and assigns it in UpPromote — one manual step per approved ambassador. Fine at 10–15 people.

**4. Gifting a pair is not an app feature on Free.** *Gifts for affiliates* is a paid tier. But this barely matters: the clean way to gift a pair on any plan, with or without an app, is a **single-use 100%-off discount code scoped to the one product**, or a **$0 draft order** he fulfils normally. Both keep the gift inside Shopify's order records where returns and inventory already work. That answers "gift product without it being a mess" independently of the tooling choice.

**5. Second dashboard.** UpPromote is not native to the Shopify admin the way Collabs is. It is one more login and one more place to look.

**6. Tax and record-keeping is still his.** UpPromote's docs show W-9 collection and 1099-NEC forms across all plans including Free — **verify this in-app rather than trusting the doc table**, because it is the kind of row vendors move. Regardless of the app, paying individuals over $600 in a calendar year is a real 1099 obligation and the app only helps with the paperwork; it does not assume the obligation.

---

### 7.3 Why UpPromote beats Shopify Collabs — the requirement Collabs fails

Shopify Collabs was §1.3's pick and it *should* have won: it is first-party, free to install, available on **all Shopify plans except Starter and Retail** ([Shopify Help Center](https://help.shopify.com/en/manual/promoting-marketing/collabs/merchants)), it has an application page, unique codes *and* links, native attribution, gifting, and automatic payouts on the Shopify bill with only a **2.9% fee on the commission paid** — not on order revenue. On a $74 order at 10% commission that fee is about **21 cents**. That is the best cost model of anything reviewed.

**It fails on who the ambassadors are.**

Collabs is a *creator* network, and the ambassador cannot simply be handed a code — they must become a **Shopify Collabs creator** with a completed profile and a **connected, verified social account**. The creator side is restricted to the **United States, United Kingdom, and Canada** ([Shopify Help Center](https://help.shopify.com/en/manual/promoting-marketing/collabs/creators/discover)), and multiple current secondary sources report a **follower minimum of roughly 1,000 on a single platform** — forum-sourced and not in Shopify's own documentation, so treat the exact number as unconfirmed, but the direction is not in doubt.

Andrew's ambassadors are barre, Pilates, reformer, Lagree, Megaformer, and yoga **instructors** — described in the brief as *"people with in-person influence over a class, not large-audience social influencers."* An instructor with 400 followers who teaches 12 classes a week is precisely the profile a follower gate excludes. Requirement one is *"give each ambassador a unique discount code."* If a chunk of his roster cannot get an account, the tool fails requirement one.

Two further risks stack on top:

1. **New creator signups appear to be paused.** Several current sources state Shopify is not accepting new creator registrations, with merchants still able to send direct invites and receive applications from creators who *already* hold accounts. ([Omnisend, 2026](https://www.omnisend.com/blog/shopify-collabs/) · [Mastroke, 2026](https://blog.mastroke.com/social-media-marketing/how-shopify-collabs-works-a-guide-to-influencer-marketing-without-the-chaos/) · [Gaurav Tiwari](https://gauravtiwari.org/shopify-affiliate-programs-bloggers/)) I could not confirm this from a first-party Shopify page — **treat it as unverified but credible.** If true, direct invites do not rescue it, because the invited instructor still has to create an account to accept.
2. **A documented, unresolved submission bug.** A merchant review on the Collabs listing reports applicants connecting a social account and still being blocked with *"a social account must be connected,"* unfixed for over a month. ([review](https://taranker.com/shopify-collabs-app-customer-reviews?filter-by=2))
3. Collabs also has **no tiered commission**, a **$25 minimum before a creator is paid**, and requires the creator to switch on auto-payouts or the commission sits in limbo.
4. Its application page is **Collabs' own page**, so the instructor-specific fields on `/pages/ambassador` do not feed it.

**Documentation conflict worth knowing:** Shopify's own marketing page footnote says Collabs is free *"for any Shopify merchant on the Shopify, Advanced, or Shopify Plus plans"* ([shopify.com/collabs](https://www.shopify.com/collabs/find-influencers)) — which would exclude Basic — while the Help Center says **all plans except Starter and Retail**. The Help Center is the better source, but if Barreletics is on Basic, verify before relying on Collabs at all.

**What he gives up by not using Collabs:** everything in one admin with no second login, payouts that ride on the Shopify bill so he never touches PayPal, attribution he never has to trust a third party for, and a cost model of pennies per order instead of a plan ceiling. Those are real. They are simply worth less than a program every ambassador can actually join.

**Why not the others:** all three of the main paid alternatives charge a **revenue share**, which is exactly the structure to avoid on a small program — and none is cheaper than $0.

- **Refersion** — Launch **$39/mo + 3% of affiliate-driven sales**; Growth $199/mo + 2%. No useful free tier. ([refersion.com/pricing](https://www.refersion.com/pricing/), checked 2026-08-08)
- **Social Snowball** — Snow Day from **$249/mo + 3% of affiliate revenue**; Blizzard from $899/mo. No free plan, no free trial. ([socialsnowball.io/pricing](https://www.socialsnowball.io/pricing), checked 2026-08-08) Not remotely justifiable at v1 volume.
- **GoAffPro** — genuinely competitive and the designated second choice; see §7.6.

#### Graduation trigger — when to stop being on Free

**Upgrade when referred sales pass roughly $3,000 in a month.** That is the Free plan's review ceiling — at a ~$74 order that is about **40 referred orders per month**. Below it, Free costs nothing and does everything except send money.

At that point Growth is **$29.99/mo + 2% of referral sales**. Do the arithmetic before clicking: at $3,000/mo of referred sales the 2% is $60, so the real cost is about **$90/mo, not $30**. At $10,000/mo it is $230/mo. That 2% is the thing that scales badly, and it is the moment to compare **GoAffPro Premium at $49/mo flat with no revenue share** (§7.6) rather than climbing UpPromote's ladder by reflex.

Secondary triggers, either of which justifies upgrading earlier: he wants **automated payouts** because marking payments by hand has become the chore, or §2A's **performance tier** is approved and he is tired of moving people between programs manually.

---

### 7.4 Shopify Flow — kept for the record · NOT the recommendation

Flow is **free on all paid Shopify plans** — Basic, Grow, Advanced, Plus — and needs only the free Flow app installed. It was Plus-only until July 2023. ([shopify.com/flow](https://www.shopify.com/flow) · [changelog](https://changelog.shopify.com/posts/shopify-flow-now-available-to-basic-plan) · [Help Center](https://help.shopify.com/en/manual/shopify-flow)) There are no task or execution caps.

The brief's expectation was that Flow is good at discrete actions and bad at the parts that make an affiliate program work. **Verified — that is correct, and the boundary is sharper than expected.**

**What Flow CAN do here:**

- **Create a discount code.** Not a first-class Flow action — done through the *Send Admin API request* action calling the `discountCodeBasicCreate` mutation. It works; Flow now runs on Admin API version 2025-10. ([mutation docs](https://shopify.dev/docs/api/admin-graphql/2025-07/mutations/discountCodeBasicCreate) · [community thread](https://community.shopify.com/t/how-to-create-discount-codes-via-shopify-flow-using-discountcodebasiccreate-mutation/577239/3))
- **Tag a customer or an order**, add order notes, update fulfilment instructions.
- **Notify** — Slack ping, or a project-management tool, when something happens.
- **Automate Collabs itself**, if Collabs were the choice: Shopify ships ready-made Flow templates to auto-approve applicants, sync approved applicants to Klaviyo, tag every Collabs-attributed order, and ping the team on a new application or first sale, using Collabs-specific triggers like *application received* and *gift claimed*. ([Using Flow with Shopify Collabs](https://help.shopify.com/en/manual/promoting-marketing/collabs/merchants/flow))

**What Flow CANNOT do here:**

- **No attribution.** Flow has no concept of an affiliate. It cannot tie an order to a person via a referral link, and there is no cookie or click tracking anywhere in Flow. Code-based attribution would have to be reconstructed by hand from Shopify's discount reports.
- **No commission ledger.** Flow fires on an event and forgets. It holds no running balance of what an ambassador has earned or been paid. Storing it in metafields means hand-building an accounting system out of automation steps.
- **No payouts.** Flow moves no money, ever.
- **No affiliate portal.** Ambassadors get no login and cannot see their own performance.
- **It cannot even see who a code belongs to.** The *Discount code created* trigger does not expose the associated customer — no email, no name, no ID — so linking a generated code back to a person requires a follow-up GraphQL query inside the workflow. ([Shopify dev forum](https://community.shopify.dev/t/need-help-retrieving-customer-data-when-a-discount-code-is-created-shopify-flow-limitation/25622))
- Flow is also **English-only**.

**Honest verdict, exactly as the boundary falls:** Flow covers the **onboarding half** — issue the code, tag the person, notify support, route the application — and leaves the **tracking-and-payout half completely unsolved.** Flow plus a spreadsheet would genuinely have been enough at v1 volume. **Andrew rejected that route on 2026-08-08 ("Find an app please"), so it is not the recommendation.** Flow remains useful *alongside* UpPromote for notifications and order tagging, and needs no decision now.

---

### 7.5 Building it ourselves — kept for the record · NOT the recommendation

**One plain sentence: building this would be the wrong call, and it is not close.**

Issuing codes and tagging customers is the easy, visible 10% — a day's work against the Admin API. The other 90% is permanent, invisible, and unglamorous:

- **Attribution** — click tracking, cookie windows, last-click resolution, code-versus-link precedence, and correctly reversing commission when an order is refunded or partially returned. In a returns-heavy category this is where a home-built system quietly produces wrong numbers.
- **A commission ledger** that survives edge cases: partial refunds, exchanges, discount stacking, cancelled orders, an ambassador leaving mid-period.
- **Payouts** — either integrating a payments API or building the same manual process UpPromote already gives away for free.
- **Tax and record-keeping for paying individuals** — W-9 collection, 1099-NEC thresholds, retention. This is a compliance surface, not a feature.
- **An ambassador-facing portal**, plus the support load of instructors asking why their number looks wrong.
- **Ongoing maintenance forever** — Admin API version deprecations arrive on Shopify's schedule, not ours, and this code would sit directly in the path of getting people paid correctly.

Against **$0/month** for a tool that already does all of it, with fraud detection and tax forms included, there is no version of this trade that favours building. It also fails the standing brief: Andrew has rejected complexity repeatedly today, and a custom payout system is the single most complex thing in this document.

---

### 7.6 Second choice — one line

**GoAffPro** — free tier with **no monthly order or revenue cap**, and Premium at **$49/mo flat with zero revenue share** ([App Store](https://apps.shopify.com/goaffpro) · [docs](https://docs.goaffpro.com/frequently-asked-questions), checked 2026-08-08); rougher and less polished than UpPromote, but the better arithmetic the moment the program gets big enough that UpPromote's 2% starts to bite.

---

### 7.7 Setup — four steps, in order

Nothing below has been done. All four are owner actions.

1. **Install UpPromote from the Shopify App Store and stay on the Free plan.** Do not start the 14-day paid trial — Free is permanent and sufficient. Skip anything the onboarding pushes that costs money.
2. **Create one program** with the commission rate from §2A once approved, and set *Delay time to approve orders* to match the returns window so refunded orders never accrue commission. Add the payment methods he will actually use (PayPal, Venmo) so ambassadors can enter their details.
3. **Customise the registration form** — add discipline, studio name, studio URL, classes per week, Instagram — then point the Apply button on `/pages/ambassador` at that registration link. (Repo change, Theme Editor setting on `page-ambassador`; not done, awaiting approval of this section.)
4. **Per approved ambassador:** create their discount code in Shopify, assign it to them in UpPromote, and send the welcome note. **Once a month:** Payments → Manual, pay each person by PayPal or Venmo, click *Mark as paid.*

### 7.8 What I could not verify

1. **Barreletics' Shopify plan is unconfirmed.** It determines nothing for UpPromote, but it decides whether Collabs is even available under the stricter of the two conflicting Shopify sources.
2. **Whether Shopify Collabs creator signups are actually paused.** Reported consistently by current secondary sources; I found no first-party Shopify confirmation. If Andrew wants Collabs reconsidered, the five-minute test is to have one instructor try to create a Collabs account.
3. **The Collabs follower minimum (~1,000)** is forum-sourced, not in Shopify's documentation. The US/UK/Canada creator restriction *is* documented.
4. **Which UpPromote tier unlocks in-app PayPal payouts** — the vendor's own pages disagree (Growth vs Professional). Irrelevant on Free, material if he upgrades for that reason.
5. **Whether 1099-NEC support is genuinely on the Free tier.** UpPromote's docs table says yes across all plans; the pricing-page matrix does not make the tier legible. Verify in-app.
6. **No app was installed and no pricing was seen inside the admin**, so every figure is the vendor's public list price as of 2026-08-08, not a confirmed charge on this store.
