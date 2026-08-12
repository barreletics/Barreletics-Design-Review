# Barreletics Email Template Master
**Platform:** Help Scout
**Signature:** Lives in Help Scout (do not include in template body)
**Voice:** Premium, direct, warm — Nike / Free People retailer tone

---

## Help Scout naming convention

Each template title below uses the format **`Category — Subject`** (e.g. `Sizing — Size chart`). Paste the title exactly as shown into the **Name** field when creating the saved reply. The category prefix means typing the first few letters surfaces every related template in the picker.

Internal numbering (1.1, 1.2, etc.) is for this document only — don't include it in the Help Scout name.

## What to paste where

- **Name field** → the template title (e.g. `Sizing — Size chart`). Don't include the internal numbering.
- **Email Content** → the body text below each title. Select from the first line of the body through the end, copy, paste into Help Scout's rich text editor. Spacing is set up to paste cleanly.

## Tags

Tags are applied to conversations later in Help Scout (not at template creation). Suggested tags by category — apply after sending:

- **Sizing templates** → `size-issue`
- **Returns templates** → `returns`
- **Lost package** → `lost-package`
- **Wholesale / studio** → `wholesale-inquiry`, `wholesale-approved`
- **Instructor** → `instructor`
- **Creator / collab** → `creator-inquiry`
- **Press / editorial** → `press-inquiry`
- **Quality / defect** → `quality-issue`
- **Torn / first-use break (2.6)** → `quality-issue` (+ `size-issue` if fit also in play)
- **International** → `international`
- **Late return** → `late-return`

---

## Voice & Language Rules (apply to every reply)

- **Never call the product a "sock."** It is a Performance Skin, grip shoe, or second skin.
- **Never refer to grip socks as "ours."** Grip socks are the competitor category.
- **No medical claims.** No "supports arches," "prevents injury," etc.
- **No invented inventory, restock dates, or shipping promises.**
- **One emoji max** per reply. None on returns, defects, or lost-package replies.
- **Open with the customer's first name** when available. Skip greeting if not.
- **End on a clear next step**, not filler ("Let me know if you have questions").
- **"Outdoor"**, not "Aquatic" or "water shoe" (in our voice). Customers may call it a water shoe — that's fine, we answer their wording.
- **Refunds, wholesale approvals, and damage replacements** = human handoff, not canned.

---

## Variables

| Variable | Use |
|---|---|
| `{%customer.firstName%}` | Greeting line only |
| `{%conversation.number%}` | Optional — subject line / reference in footer |
| `{%customer.email%}` | Wholesale + Instructor templates only |

---

# 1. Greetings & Quick Replies

### 1.1  Greeting — Open inquiry
**Subject:** Re: Your question
Hi {%customer.firstName%},

Thanks for reaching out. What can we help with — sizing, an order, or something else?

---

### 1.2  Greeting — Holding reply
Hi {%customer.firstName%},

Thanks for the note. Let me look into this and get back to you shortly.

---

### 1.3  Greeting — Closing the loop
Anything else we can help with? We're here.

---

# 2. Sizing & Fit

### 2.1  Sizing — Size chart
Hi {%customer.firstName%},

Here's our fit guide: https://barreletics.com/pages/performance-skins-size-chart

Sizing runs M (women's 5.5–7.5) and L (women's 8–10.5 / men's up to 10.5). Tell us your usual shoe size if you'd like a recommendation.


---

### 2.2  Sizing — Between sizes
Hi {%customer.firstName,fallback=there%},

If you're between a 7.5 and an 8, foot width is the deciding factor:

- Wider foot → size up to the Large
- Narrower foot → size down to the Medium

Let us know which sounds like you and we'll help from there.


---

### 2.3  Sizing — No size small
Hi {%customer.firstName%},

Sizing starts at Medium (women's 5.5–7.5). We don't currently offer Small, but we're tracking the request as we plan future sizes.

If you're on the smaller end of M, a thin toeless sock helps fill the space while keeping grip and splay. Size chart: https://barreletics.com/pages/performance-skins-size-chart


---

### 2.4  Sizing — Save the return (narrow foot)
Hi {%customer.firstName%},

Before we process the return — some customers with narrower feet find a thin toeless sock creates a more secure fit without compromising grip. Worth a quick test in your next class.

If you'd still like to return or exchange, just say the word and we'll send instructions.


---

### 2.5  Sizing — Save the return (wrong size)
Hi {%customer.firstName,fallback=there%},

We'd love to get you into the right size before moving forward. Quick check:

- Tight or toe pressure → likely too small. Sizing up usually solves it.
- Loose or shifting mid-movement → likely too large. Sizing down usually solves it. Switching to a tighter-fitting color (Dark Gray, Blue, or Hot Coral) is another option.

Exchanges are free. Reply with your usual shoe size and we'll set one up for you — or start it yourself here: https://barreletics.com/pages/returns


---

### 2.6  Sizing — Save the return (torn on first use)
Hi {%customer.firstName,fallback= %},

I saw your return request come through and wanted to reach out personally before we process it.

Your outdoor Performance Skins absolutely should not have broken on the first use, and I’m very sorry that happened. It’s an unusual issue for us to see. Many of us on the team have pairs we’ve worn for years. Mine are three years in and still my go-to.

If you’re open to it, we’d love the opportunity to replace your pair rather than have you give up on them after this experience. There would, of course, be no charge for the replacement.

If it’s not too much trouble, could you send us a quick photo of where they broke? It would be very helpful for our quality control team. We’d also love to know your usual shoe size and whether you consider your foot narrow, average, or wide so we can make sure we send the best fit.

One quick tip that may be helpful with your replacement: when putting on your Performance Skins, pull from the top of the foot rather than pulling on the straps.

Of course, if you’d still prefer to proceed with the return, we’re happy to do that as well. We’d just really appreciate the chance to make this right for you.


---

### 2.7  Sizing — Save the return (tight toe box, the blow dryer trick)

**Support channel only.** Do not put this on the size guide, the FAQ, or any product page — see `docs/11-CANONICAL-ANSWERS.md` CA-08b. Before purchase it reads as a warning label. After purchase it reads as insider help.

**Send only when:** the customer already owns the pair, says it's tight in the **toe box specifically**, and the size is otherwise right. If the whole pair feels small, use **2.5** and exchange instead.

Hi {%customer.firstName,fallback=there%},

Since we manufacture these ourselves, we've picked up a trick for exactly this.

First things first though — if the whole pair feels small, let's just exchange it. That's free and it's the better fix, so reply with your usual shoe size and I'll set it up.

But if the size is right and it's only the toe box that's snug, try this: warm that spot with a blow dryer for about 30 seconds, keeping the dryer moving rather than holding it in one place. Once it's warm, gently stretch the material with your hand. Warm is all you need — not hot — and do it with them off your foot.

That usually opens up the spot that's bothering you. If it doesn't, the exchange offer stands.

---

# 3. Returns & Exchanges

### 3.1  Returns — Portal link
Hi {%customer.firstName%},

You can start a return or exchange here: https://barreletics.com/pages/returns

The portal walks you through it step by step. Reply here if you hit a snag.


---

### 3.2  Returns — Received, processing
Hi {%customer.firstName%},

Thanks for your patience. Returns are processed in the order they arrive, and current volume means it may take a few days from delivery to complete.

You'll get an email the moment it's processed. Reply if anything looks off.


---

### 3.3  Returns — Order already shipped
Hi {%customer.firstName%},

Your order is already with fulfillment, so we can't modify it. Once it arrives, we'll set up a free exchange or return — just reply here when it lands.


---

### 3.4  Returns — Outside 30-day window
Hi {%customer.firstName,fallback=there%},

Our standard return window is 30 days, but we'd still love to help where we can. Send us a quick note on what's going on — how long you've had them, the issue, and what you're hoping for — and we'll see what we can do.

We typically accommodate where it makes sense.


---

# 4. Product Info

### 4.1  Product — Open vs Closed vs Outdoor
Hi {%customer.firstName%},

All three are the same material — what changes is the sole.

- Open Sole — exposed midfoot for a barefoot, grounded feel. Front half still has grip and cushion.
- Closed Sole — full-bottom coverage. More protection, more versatility.
- Outdoor — closed sole built for sand, pool decks, boats, hot surfaces.

Open and Closed are largely interchangeable in studio — it's a feel preference.

Full comparison: https://barreletics.com/pages/compare-open-closed-sole

---

### 4.2  Product — Open sole outdoors
Hi {%customer.firstName%},

Yes — same material as Closed and Outdoor, so durability isn't a concern. Open Sole is great for the beach, pool deck, or a boat. For rough terrain or longer walks, Closed Sole gives more coverage.

Many of us wear Open Sole outdoors regularly.

---

### 4.3  Product — Beach and outdoor use
Hi {%customer.firstName,fallback=there%},

Yes — Performance Skins hold up well on sand, shells, and rougher beach terrain. The material is flexible but built to take that kind of use without tearing.

They've been a go-to for boats, pool decks, and beach days. Let us know if you have specific questions about the conditions you're using them in.

One note: some surfaces are slippery no matter what footwear you're wearing — wet tile, polished stone, or anything similar can be unpredictable. We don't recommend Performance Skins on those.


---

### 4.4  Product — Materials
Hi {%customer.firstName%},

Performance Skins are injection-molded from a proprietary soft synthetic rubber blend — one continuous material, not a fabric with grip added on top.

- Silicone-free
- Latex-free
- Skin-safe and hypoallergenic
- No hard plastics

---

### 4.5  Product — Lifespan
Hi {%customer.firstName,fallback=there%},

It depends on the person — how often you wear them, how you wear them, and how you care for them. Just like shoes, some people are harder on them than others.

That said, in a studio setting it's a gentle environment, and they hold up beautifully. One of our customers recently passed 1,000 classes on a single pair, and another is on year four of theirs.

Care is simple: warm soapy water, air dry, and pull from the top of the foot (not the straps) when putting them on.

---

### 4.6  Product — Care instructions
Hi {%customer.firstName,fallback=there%},

Easy care:
- Hand wash with warm, soapy water
- Air dry
- Pull from the top of the foot (not the straps) when putting them on

That's it. No special detergent, no machine needed.

---

### 4.7  Product — Wearing socks underneath
Hi {%customer.firstName,fallback=there%},

Totally up to you. Performance Skins are designed to be worn directly on the foot, but a thin sock works too — common reasons customers choose to:

- Toe coverage preference — a thin toeless or split-toe sock keeps toes free while covering the rest of the foot
- Tighter fit — a thin sock helps fill space for narrower feet
- Heavy sweat — a thin moisture-wicking sock absorbs more than skin contact alone

All of those work without affecting grip. It's a personal-preference call.

---

### 4.8  Product — Grip socks vs Performance Skins
Hi {%customer.firstName,fallback=there%},

Great question. The short version: grip socks are fabric with grip *added* on top. Performance Skins are one continuous piece of grippy material — there's nothing to compress, bunch, or peel off.

A few key differences:

- Grip: Performance Skins grip the floor directly. With grip socks, your foot moves inside the sock *and* the sock moves on the floor.
- Lifespan: Grip socks typically lose their grip after 6–8 washes. Performance Skins are built to last hundreds of classes — many customers are years into a single pair.
- Care: Hand wash with warm soapy water, air dry. No machine, no replacement cycle.

Same secure grip class one as class three hundred.

---

### 4.9  Product — Allergy and skin sensitivity
Hi {%customer.firstName,fallback=there%},

Performance Skins are made from a proprietary soft synthetic rubber blend — designed to be skin-safe and hypoallergenic:

- No silicone
- No latex
- No hard plastics

Most customers with sensitivities wear them without issue. If you have a known allergy to a specific material, we'd suggest doing a quick patch test (wear them briefly the first time) to see how your skin reacts.

---

# 5. Orders, Shipping & Tracking

### 5.1  Shipping — Lost package (marked delivered)
Hi {%customer.firstName%},

Tracking shows the carrier marked your package as delivered. A few places it usually turns up:

- Building leasing office or mailroom
- Parcel lockers or communal delivery area
- A neighbor who took it in

Carriers and buildings handle deliveries differently once they arrive, so checking locally is the fastest path. Keep us posted — if it doesn't surface in 48 hours, reply here and we'll go from there.


---

### 5.2  Shipping — Where is my order
Hi {%customer.firstName%},

Your order is on the way. Carrier delays happen — if tracking hasn't updated in 3+ business days, reply here and we'll look into it.

---

### 5.3  Shipping — International duties
Hi {%customer.firstName,fallback=there%},

Yes, we ship worldwide. Shipping time and cost depend on your country and are calculated at checkout.

A note on duties and taxes: depending on where you're located, these may be included at checkout — or they may be collected by your local carrier or customs office when the package arrives. If they're not included up front, be prepared to pay them on delivery.

Let us know if you have a specific country in mind and we can help confirm.


---

# 6. Discounts & Codes

### 6.1  Discount — SAVE15 not working
Hi {%customer.firstName%},

A few things to check:

- Code goes in the discount field at checkout
- Cart needs 2+ pairs
- Doesn't stack with other promos or sale items

If those all check out, send a screenshot of what you're seeing and we'll dig in.

---

### 6.2  Discount — Welcome code not received
Hi {%customer.firstName%},

The welcome code goes out via email after signup — sometimes it lands in promotions or spam. If you can't find it, reply and we'll send one over.

---

# 7. Wholesale & Instructor

### 7.1  Wholesale — Teacher/instructor inquiry (vetting)
Use when an individual teacher, instructor, or fitness professional asks about a personal discount. Vets credentials before approving.

Hi {%customer.firstName,fallback=there%},

Thanks for reaching out — we love working with teachers and instructors.

When you have a moment, send over:
- Where you teach (studio name + link)
- What you teach and how long you've been teaching
- Your social handles if you have them
- An email you'd like to use for your account (we'll set things up on that address)

Once we have that, we'll get you set up.


---

### 7.2  Wholesale — Studio inquiry (vetting)
Use when a studio or business wants to carry Barreletics for their clients. Vets the studio before sharing program details. Warm tone — these are relationship leads, not transactional inquiries.

Hi {%customer.firstName,fallback=there%},

Thank you for reaching out — we're glad you found us.

We're selective about the studios we partner with, and we look for spaces that share our approach to movement, design, and care for the community they're building. From what you've shared, it sounds like there could be real alignment.

To take the next step, send over a few things when you have a moment:
- A link to your studio (website + social)
- Where you're located
- The types of classes you offer and roughly how many clients you see weekly
- The email you'd like to use for ordering

Once we have that, we'll send program details and explore what makes sense from here.

Appreciate you thinking of us.


---

### 7.2a  Wholesale — Studio inquiry (high-context lead)
Use when a studio reaches out with detailed background already — studio name, location, type, vision, opening timeline, etc. They've done the work; don't ask them to repeat themselves. Acknowledge what they shared and ask only for the operational gaps.

Hi {%customer.firstName,fallback=there%},

Thank you for the thoughtful intro — it's clear you've put real care into what you're building, and we appreciate you thinking of us.

We're selective about the studios we partner with, and what you've described sounds genuinely aligned with where Barreletics fits. Our wholesale program starts at a 10-pair minimum, though many studios prefer to go deeper to give their clients more to choose from — orders fulfill quickly, so it's easy to adjust as you learn what they gravitate to.

A couple of quick things to get you set up:
- The best email to use for your wholesale account
- What you have in mind for your first order

Once we have those, we'll send program details and figure out next steps together.

Looking forward to it.


---

### 7.3  Wholesale — Distributor inquiry (vetting)
Use when someone asks about distributing, reselling, or representing Barreletics commercially (larger scale than a single studio). Different vetting bar — needs business verification.

Hi {%customer.firstName,fallback=there%},

Thanks for the interest in distributing Barreletics.

To explore a fit, please send over:
- Where you're located and the markets you'd cover
- How you plan to distribute (retail, online, both)
- A link to your website and any existing brands you carry
- Business verification — EIN or business license (US), or VAT / business registration number (international)
- Expected initial order volume

Once we have that, we'll review and follow up.


---

### 7.4  Wholesale — Studio onboarding
Hi {%customer.firstName%},

Welcome to the Barreletics studio program.

To place your first order:
1. Create an account at barreletics.com using {%customer.email%}
2. Log in with that same email
3. Add 10+ pairs to your cart
4. Enter code at checkout: 0-WHOLESALE-STANDARD-COLORS
5. Your 50% discount will apply automatically

⚠️ The code only works when logged in with {%customer.email%}.

What's included:
- Free shipping on your first order
- Demo pairs (M + L) for in-studio use

Care: Warm soapy water, or wear with a thin sock if preferred.

Questions: team@barreletics.com


---

### 7.5  Wholesale — Instructor discount code
Hi {%customer.firstName%},

Thanks for sharing your background — happy to support you.

Use code 0-Wholesale-Instructor at checkout with {%customer.email%}.

In exchange, we'd love a short video and a few photos of you using the Performance Skins. With your okay, we'd cross-promote you on our site and channels.


---

### 7.6  Wholesale — Creator/collab
Use when someone is asking for free product in exchange for content, promotion, or a review — creators and influencers. For editorial press requests (magazines, newspapers, stylists pulling for shoots), use 7.5.

Hi {%customer.firstName,fallback=there%},

Thanks for the interest — we'd love to hear more about what you have in mind.

When you have a moment, send over:
- Your social handles or platform
- Audience size and the kind of content you create
- What you're proposing (post, reel, review, etc.)

We're selective about who we send product to, and this helps us figure out if it's a good fit on both sides.


---

### 7.7  Wholesale — Press/editorial sample
Use when an editor, journalist, stylist, or PR rep requests samples for editorial coverage, a story, or a photo shoot. Different vetting from 7.5 (creators) — focus is on verifying the outlet and the feature.

Hi {%customer.firstName,fallback=there%},

Thanks for reaching out — we'd love to support the story.

When you have a moment, send over:
- The outlet and your role
- A brief on the feature (angle, timing, format)
- Sample needs (colors, sizes, quantity, and where to send)
- Your deadline

We'll get back to you quickly.


---

# 8. Quality & Defects

### 8.1  Quality — Defect initial response
Hi {%customer.firstName,fallback=there%},

Sorry to hear this — it's not something we see often. Most customers (and our own team) wear theirs for years without issues, so we want to get to the bottom of it.

When you have a moment, send:
- A photo of the issue
- Confirmation of whether "Barreletics" appears in raised lettering on the inside of the right shoe (helps us identify the batch)
- Your usual shoe size so we can get a replacement out to you

We'll get a new pair on the way as soon as we have those.


---

### 8.2  Quality — Replacement confirmed
Hi {%customer.firstName%},

Thanks for the photo — that helps us understand exactly what happened.

A quick tip going forward: pull from the top of the foot when putting them on, not the straps. Performance Skins are built to last, but that small change extends their life.

Your replacement ships tomorrow. You'll get tracking by email.


---

# 9. Subject Line Conventions (Help Scout)

For consistency, use these subject patterns:

| Type | Subject |
|---|---|
| First reply | `Re: Your Barreletics inquiry` |
| Sizing follow-up | `Sizing help — Barreletics` |
| Return/exchange | `Your return — Barreletics` |
| Wholesale | `Barreletics studio program` |
| Defect | `Your Performance Skins — let's fix this` |

---

# 10. Templates To Add Later (gaps to fill)

These don't exist yet — flag them when situations come up so we can build templates:

- **Pre-order / waitlist** (if a color goes OOS)
- **Gift order — receipt/packing slip request**
- **Pregnancy / postpartum sizing question** (no medical claims, just fit guidance)
- **Affiliate program** — once built, replace the triage default (7.1) with a dedicated reply for affiliate inquiries
