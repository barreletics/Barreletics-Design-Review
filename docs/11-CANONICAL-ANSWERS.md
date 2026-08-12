# 11 · Canonical Answers — the one global source

**Created 2026-08-12 (Andrew letter: "make one global everything you need to know section rather than manage individually").**

This file is the **single source for customer-facing answers**. FAQ, PDP, collection copy, Help pages, email, ManyChat, HelpScout, and ads all copy from here **verbatim**. Do not rewrite an answer on a page. Change it here, then propagate.

**Found something only Andrew can fix — in HelpScout, ManyChat, Shopify Admin, or the live theme?** Append it to `planning/OWNER-MANUAL-TASKS.md`. Do **not** interrupt a build to ask him to go change it by hand unless it blocks the build. He batches those in one sitting at the end.

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
| **"antimicrobial fabric"** on the Apparel tee | Andrew 2026-08-12: steer clear of the claim | describe softness, weight, and moisture movement instead |

⚠️ `manychat-kb/05-why-better-than-socks.md` still lists "Antimicrobial & sweat-resistant — doesn't trap bacteria." **That line is retired.** Use CA-01/CA-02.

---

## Material & surface

**CA-01 · What they're made of**
> A proprietary grip material — **skin-safe and non-toxic, with no latex and no silicone.** Made in the USA.

Short strip form (PDP): `Skin-safe — no latex · no silicone`
Basis: **D-019** ("skin-safe, non-toxic material") + **P-008** ("proprietary grip material, not silicone, not latex").

**CA-02 · Why it stays fresh** *(approved framing, Andrew 2026-08-12)*
> Non-porous, so it wipes clean. Nothing soaks in and lingers the way it does in fabric.

The claim is about the **surface being wipeable**, never about the material acting on bacteria. Contrasting with fabric does the persuading — a sock absorbs and holds moisture; this doesn't. Never write that it resists, repels, kills, or prevents bacterial growth.

**"Patented" is accurate and approved** *(Andrew 2026-08-12)*. Both "patented" and "proprietary" may be used for the grip and the material. Do not purge "patented" — an earlier reading of P-008 treated it as unsupported; it is not.

**CA-03 · Fit over time — no break-in**
> The material stretches and conforms to your foot. There is no break-in period — how they feel on day one is how they feel.

**CA-04 · Shape and grip over time**
> Never loses shape. Never loses grip. The same performance on class 1 as on class 1,000.

---

## Sizing — canonical

**CA-05 · Size chart** *(Andrew confirmed 2026-08-12 — matches the live site)*

| Size | Women's (US) | Men's (US) | Kids' (US) |
|---|---|---|---|
| **M** | 5.5–7.5 | — | 2–5 |
| **L** | 7.5–11 | up to 10.5 | — |

**Publish all four columns.** Kids' 2–5 in Medium is real and has always been on the live site; a build that drops it stops answering parents.

No small size. M and L only — **never** write "S coming soon."

⚠️ **Retired 2026-08-12 — never reintroduce:**
- **M 5–8 / L 8.5–11** (was on all three size-chart templates)
- **M W 5–7.5 · Men 6–8 / L W 8–10 · Men 8.5–11** (was in five product templates and hardcoded at `pdp-buy-box.liquid` line ~409)
- **L 8–11** — briefly shipped 2026-08-12 afternoon before Andrew confirmed 7.5. Large starts at **7.5**.
- The **Foot Length** column (8.5"–9.5" / 9.5"–10.5") — repo-only, never on the live site, traceable to no source. Removed. We publish shoe size only.

**CA-06 · The overlap at 7.5 — width decides** *(Andrew letter 2026-08-12)*

7.5 sits in both rows on purpose. Width is the tiebreaker, not rounding up.

> **Wide foot at 7 or 7.5** → Large.
> **Narrow foot at 7.5 or 8** → Medium.
> **8.5 and above** → Large, regardless of width. You need the length.

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

**CA-13 · How long they last** *(rewritten 2026-08-12 from `helpscout-kb` §4.5 — Andrew: this is the right framing)*
> It depends on how you wear them — how often, how hard you go, and how you care for them. Just like shoes, some people are harder on them than others.
> Used for what they're designed for — Pilates, barre, reformer, Lagree, yoga — they hold up beautifully. One customer recently passed 1,000 classes on a single pair. Another is on year four.
> The grip is molded into the sole, so there's nothing to peel or flake off.

Set the honest expectation **first**, then land the two proof points. That order is the whole trick: it reads as candor rather than a promise, and the anecdotes are more persuasive than any range.

🚫 **Do not publish "18+ months."** It was on six product templates, twice each. Andrew 2026-08-12: it's an internal floor, not a claim. Next to "1,000 classes" and "year four," a customer anchors on the smaller number and reads it as a ceiling. Keep it internal.

🚫 Don't say "gentle environment." Name what they're built for instead.

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

**CA-18 · International** *(Andrew confirmed 2026-08-12: the 195 figure is real)*
> We ship to 195 countries via FedEx International Connect Plus. International orders typically arrive within 7–14 business days.
> Customers are responsible for duties, taxes, and customs fees — these vary by country and are outside our control.

This is a real carrier arrangement, not marketing padding. It was briefly stripped from the FAQ on 2026-08-12 for being absent from the KB; that was wrong. Keep it on the Shipping page and the FAQ.

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
| CA-01, CA-02 | `page.technology.json` (**two** cards titled "Antimicrobial", ~L46 + ~L60) · `page.grip-comparison.json` (~L39, L40, L63) · `collection.apparel.json` (~L71 tee) · `page.faq.json` · `product*.json` · `value-strip.liquid` |
| CA-03, CA-04 | `page.faq.json` · size-chart templates (all three aliases) · `product*.json` |
| CA-05–CA-09 | size-chart templates (`page.size-chart.json` + both aliases) · `sections/page-size-guide.liquid` (fallback rows **and** schema defaults) · **`pdp-buy-box.liquid` ~L409 hardcoded `size_range`** · `page.faq.json` · six `product*.json` FAQ blocks · `collection.json` (~L296 "Small is coming soon" + size-up) · `collection.open-sole.json` (~L69 size-up) |
| CA-10 | `page.faq.json` · `page.compare.json` · `product.json` · `product.open-sole.json` · collection copy |
| CA-11–CA-13 | six `product*.json` (**"18+ months" twice each**) · `sections/collection-faq.liquid` · `sections/page-grip-comparison.liquid` · `page.grip-comparison.json` · `page.faq.json` · `page.technology.json` |
| CA-14, CA-15 | `page.faq.json` · `collection.outdoor.json` · `collection-faq` / `geo-section` blocks |
| CA-17–CA-22 | `page.shipping-retruns.json` (live) + `page.returns.json` alias · `page.shipping.json` + `sections/page-shipping.liquid` · `page.faq.json` · `page.start-a-retrun.json` |
| CA-23–CA-25 | `page.faq.json` · care-instructions page · `page.technology.json` |
| CA-26 | PDP · collection · kit pages |

**Reminder:** three Help pages render a template whose name doesn't match the handle — see the verified suffix table in `planning/page-template-registry.md`. Push every alias in a pair.

**Guarded surfaces in this list.** `pdp-buy-box.liquid` and `product*.json` are under the anti-revert and buy-box locks. Sizing corrections there are copy-only and need Andrew naming the file in his current message. Never bundle them with other work in the same turn.
