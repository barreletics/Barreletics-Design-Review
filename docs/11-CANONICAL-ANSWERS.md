# 11 · Canonical Answers — the one global source

**Created 2026-08-12 (Andrew letter: "make one global everything you need to know section rather than manage individually").**

This file is the **single source for customer-facing answers**. FAQ, PDP, collection copy, Help pages, email, ManyChat, HelpScout, and ads all copy from here **verbatim**. Do not rewrite an answer on a page. Change it here, then propagate.

**Upstream sources this consolidates:** `manychat-kb/02`–`16` · `helpscout-kb/Barreletics_Email_Template_Master.md` · `docs/09-PRODUCT-KNOWLEDGE.md` · `docs/10-DECISIONS.md` · `planning/10-decision-log.md`.

**When the KB and this file disagree, this file wins** — it carries Andrew's later corrections. Where a KB guide still holds retired wording, it is noted below.

---

## Rule 0 — Banned language (never ship these)

| Banned | Why | Say instead |
|---|---|---|
| **antimicrobial** (any form) | Andrew 2026-08-12 | See CA-01 / CA-02 |
| **bacteria claims** — "doesn't trap bacteria", "doesn't hold bacteria", "hygienic" | Andrew 2026-08-12: we can't claim they don't have bacteria | CA-02 (describe the surface, not biology) |
| **hypoallergenic**, "no allergic reaction risk" | **D-019** retired the allergy claim | CA-01 |
| **"conforms over the first few wears"**, "breaks in", "settles to your foot over time" | Andrew 2026-08-12: they do not change after wearing | CA-03 |
| **"fully enclosed"** / "fully enclosed heel" | **P-013** | CA-10 |
| **pool** · poolside · pool deck · water park · tidal pool · aqua barre · water aerobics | **P-012** — slip risk on wet tile, wrong buyer | CA-14 |
| **sole ↔ discipline split** ("Open = barre, Closed = reformer") | **P-003** | CA-10 |
| **"10% off your first order"** | Retired offer | "Join the list" — no discount promise |
| blanket **"size up"** for between sizes | Wrong rule — it's width | CA-05 |
| **"195 countries"**, "FedEx International Connect Plus" | Not in any KB — unsourced specificity | CA-17 "worldwide" |

⚠️ `manychat-kb/05-why-better-than-socks.md` still lists "Antimicrobial & sweat-resistant — doesn't trap bacteria." **That line is retired.** Use CA-01/CA-02.

---

## Material & surface

**CA-01 · What they're made of**
> A proprietary grip material — **skin-safe and non-toxic, with no latex and no silicone.** Made in the USA.

Short strip form (PDP): `Skin-safe — no latex · no silicone`
Basis: **D-019** ("skin-safe, non-toxic material") + **P-008** ("proprietary grip material, not silicone, not latex").

**CA-02 · Why it stays fresh** *(no biology claims)*
> The surface is non-porous, so sweat sits on it rather than soaking in the way it does with fabric.

**CA-03 · Fit over time — no break-in**
> The material stretches and conforms to your foot. There is no break-in period — how they feel on day one is how they feel.

**CA-04 · Shape and grip over time**
> Never loses shape. Never loses grip. The same performance on class 1 as on class 1,000.

---

## Sizing — canonical

**CA-05 · Size chart** *(source: `manychat-kb/03-sizing-chart.md`)*

| Size | Women's (US) | Men's (US) |
|---|---|---|
| **M** | 5.5–7.5 | — |
| **L** | 8–11 | up to 10.5 |

No small size. M and L only — **never** write "S coming soon."

⚠️ **Retired 2026-08-12:** the size-chart pages previously published **M = 5–8, L = 8.5–11**, and `product.json` published **M = W 5–7.5 / Men 6–8, L = W 8–10 / Men 8.5–11**. Both are wrong. The table above is the only correct chart. Unverified: the foot-length column (8.5"–9.5" / 9.5"–10.5") appears in no KB source — confirm or drop it.

**CA-06 · Between sizes** — the rule is **width, not "size up"** *(Andrew letter 2026-08-12)*
> Width decides — don't just round up.
> **Wide foot at 7 or 7.5** → size up to Large.
> **Narrow 8** → size down to Medium.
> **8.5 and above** → stay in Large, regardless of width. You need the length.

Below 7, take Medium. Never write a blanket "between sizes? size up."

**CA-07 · Colors and fit**
> Dark Grey, Hot Coral, and Blue run slightly snugger. Black and Light Grey are the most forgiving, especially for wider feet.

**CA-08 · Too tight / too loose**
> Too tight or toe pressure → the size is likely too small; move up one size.
> Too loose or shifting → likely too large; move down one size. Already in M? A thin sock underneath gives a snugger fit without affecting grip.

**CA-08b · One tight spot — the blow dryer trick · SUPPORT CHANNEL ONLY** *(Andrew letter 2026-08-12)*

🚫 **One home only: `helpscout-kb/Barreletics_Email_Template_Master.md` §2.7, a HelpScout saved reply a human chooses to send.**

**Not on** the size guide, the FAQ, a product page, or any pre-purchase surface. To a shopper who hasn't bought yet, "you may need a hairdryer" is a warning label sitting next to the claim that the fit works for nearly everyone. To someone who already owns the pair and writes in about a tight toe box, the identical sentence is insider help from the manufacturer and it saves the return. Same words, opposite effect — timing is the whole thing.

**Not in ManyChat either** (owner letter 2026-08-12). Automation can't judge whether the size is right or whether the person has even bought yet, so a bot would eventually hand a hairdryer to a browser. ManyChat's answer to a tight fit stays the free size exchange, full stop. A human decides when this one is appropriate.

**Send only when** the customer already owns the pair, the size is otherwise right, and it's the **toe box specifically**. Whole pair small → exchange, not heat.

Order of operations matters. **Always offer the free exchange first.** The heat trick is for a single stubborn spot on a pair that is otherwise the right size — never a workaround for the wrong size.

> We manufacture these ourselves, and the fit works for nearly everyone — but feet vary, and occasionally a pair just isn't right.
> If the size is right and it's only the toe box running tight: warm that spot with a blow dryer for about 30 seconds, keeping the dryer moving rather than holding it in one place, then gently stretch the material with your hand. Warm, not hot.

Guardrails, always attached:
- **Exchange first.** Whole pair feels small → free size exchange, not heat.
- **Keep the dryer moving.** Never park it on one spot.
- **Warm, not hot**, and off the foot — stretch by hand, not while wearing.

**Does not contradict CA-03 or CA-04.** They don't change from wearing or washing; this is a deliberate one-time adjustment at a temperature you never reach in a class. Do not "reconcile" these by deleting either one.

⚠️ **"Fits 98% of feet" is not approved for publication** pending Andrew's call — a hard percentage invites "based on what?" and this repo has already been through one fabricated-stat sweep. Approved framing is the qualitative version above.

**CA-09 · Placement**
> The ball of your foot sits where your foot meets your toes. Gently tug the top edge at the ankle.

---

## Soles

**CA-10 · Open vs Closed**
> **Open Sole:** Heel exposed, mid-foot breathing hole. More grounded, barefoot feel. Natural toe splay.
> **Closed Sole:** Heel and foot fully covered.
> Both perform identically — same grip, same stability, same studio uses. Choice is preference and feel only. Both $74.

Never assign a discipline to a sole. Never steer first-timers to either sole (**P-004** superseded).

---

## Grip & durability

**CA-11 · The grip**
> 360° all-over grip — not dots, not patches. It covers the entire sole, heel, and edges. Locked in through holds, transitions, and balance work.

**CA-12 · Why it can't wear off**
> The grip is injection-molded into the sole itself, so there is nothing to peel, flake, or separate.

**CA-13 · How long they last**
> Many customers use the same pair for years — some wear them 6+ days a week for over three years with zero issues. Built in the USA.
> That's the difference from a grip sock: silicone dots are printed onto fabric and wear off after six to eight washes.

**Cost math** (objection handling): grip socks $18–28/pair, 8–12 pairs/year = **$144–$336/year**. Barreletics **$74 once**.

---

## Use cases

**CA-14 · Where they work**
> Built for studio training: barre, Pilates, Lagree, reformer, Megaformer, and yoga.
> Also great for weight lifting, outdoor volleyball, martial arts, barefoot running, boating, paddleboarding, outdoor yoga, beach, and resortwear — anywhere you'd go barefoot.

**Never** pool/poolside/water park/aqua barre. Don't invent scenery (rocky coves, tidepools, shell beaches) — beach covers it.

**CA-15 · Wet-surface caution** — name the surface, never the venue
> Certain wet tile and stone areas are inherently slippery for any footwear.

**CA-16 · Heat and sweat**
> The open-toe design and lightweight material let air circulate, so they stay cooler than grip socks that wrap the whole foot. For hot yoga, a thin full sock works like a towel — it absorbs extra sweat without affecting grip.

**CA-16b · Socks**
> Either way works. Many prefer the barefoot feel; others like a thin toeless or individual-toe sock for warmth or moisture. Skip thick or full-toe socks — they reduce the natural toe splay that makes them work.

---

## Shipping, returns, warranty

**CA-17 · Shipping**
> Free shipping on Continental US orders over $150. $9.95 flat rate under $150. Expedited and overnight at checkout. We ship worldwide.
> Orders process within 24–48 hours and typically ship the next business day. Expedited orders placed before 12 PM Eastern ship the same business day. No shipping on weekends or holidays.

**CA-18 · International**
> We ship worldwide. Customers are responsible for duties, taxes, and customs fees — these vary by country and are outside our control.

**CA-19 · Returns — 30 days**
> Try them indoors for 30 days. If they don't perform, return for a full refund. Items must be clean and like new — no outdoor wear, no sole damage.
> US return shipping is $7.95 flat, deducted from the refund. Refunds process within 72 hours of inspection.

This is a fit trial, **not** a studio trial — do not write "try them in class for 30 days."

**CA-20 · Exchanges**
> Not the right size? Exchange for a different size free. We ship your exchange at no cost once we receive and inspect the return — often faster than a refund.

**CA-21 · Warranty — 90 days**
> Every purchase is covered against manufacturing defects for 90 days. Return of the defective item usually isn't required.
> International: send a photo of the defect. If approved, the customer pays replacement shipping — no need to ship the original pair back.

**CA-22 · Delivered but missing**
> Once tracking shows delivered to your address, the order is considered fulfilled. In an apartment or multi-unit building, check with building staff or the shared mail area first.

---

## Care

**CA-23 · Cleaning**
> Warm soapy water, rinse, air dry. That's it — no machine washing.
> When you wipe down your equipment, a pass with the same cloth works too.

**CA-24 · Dishwasher** *(acknowledge, don't recommend)*
> Some customers run theirs through the dishwasher. You don't need to — a rinse by hand does the same job with less wear.

**CA-25 · Putting them on**
> Pull from the top of the foot, not the straps. Pulling the straps puts stress on the attachment points.

---

## Price

**CA-26**
> $74 per pair. Buy 2 or more and save 15%, applied automatically at checkout. Shop Pay splits it into 4 interest-free payments of $18.50.

---

## Sensitive & medical (no emojis, no guarantees)

**CA-27**
> We can't guarantee outcomes for specific conditions. Many customers come to us for stability and confidence, and they can be worn with orthotics for extra support. There's always the 30-day return window so you can test them yourself.

Do not lead with condition-specific promises. Anecdotes belong in support conversations, not page copy.

---

## Propagation — where these answers live

Change here first, then update every surface below and note it in `planning/m4-section-freeze.md`.

| Answer | Surfaces to keep in sync |
|---|---|
| CA-01, CA-02 | `page.faq.json` · `page.technology.json` · `page.grip-comparison.json` · `product*.json` · `value-strip.liquid` · PDP strip |
| CA-03, CA-04 | `page.faq.json` · size-chart templates (all three aliases) · `product*.json` |
| CA-05–CA-09 | size-chart templates (`page.size-chart.json` + aliases) · `page.faq.json` · PDP size chart link |
| CA-10 | `page.faq.json` · `page.compare.json` · `product.json` · `product.open-sole.json` · collection copy |
| CA-11–CA-13 | `page.faq.json` · `page.technology.json` · `page.grip-comparison.json` · PDP features |
| CA-14, CA-15 | `page.faq.json` · `collection.outdoor.json` · `collection-faq` / `geo-section` blocks |
| CA-17–CA-22 | `page.shipping-retruns.json` (live) + `page.returns.json` alias · `page.faq.json` · `page.start-a-retrun.json` |
| CA-23–CA-25 | `page.faq.json` · care-instructions page · `page.technology.json` |
| CA-26 | PDP · collection · kit pages |

**Reminder:** three Help pages render a template whose name doesn't match the handle — see the verified suffix table in `planning/page-template-registry.md`. Push every alias in a pair.
