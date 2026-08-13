# Owner manual tasks — do these at the END of the redesign

**Purpose:** things only Andrew can do, in systems outside this repo — HelpScout, ManyChat, Shopify Admin, the live theme. Agents **append** here instead of interrupting with "you need to go change X." One focused sitting at the end.

**Rule for agents:** if a fix lives outside `shopify-build/` and the repo docs, it goes here. Never ask Andrew to stop and do a manual task mid-build unless it blocks the build. Add the date and the reason.

**Status key:** `[ ]` to do · `[x]` done · `[?]` needs an Andrew decision before anyone can act

---

## A · Questions only you can answer

These block work. Everything else in this file is mechanical.

- [?] **Kids sizing conflict.** Every chart including the live site says Kids' US **2–5** wear Medium. But `docs/09-PRODUCT-KNOWLEDGE.md` line 84 says **Youth 4–6**. Which is right? Until you say, nobody quotes a youth number.
- [?] **Dead Kids variants.** Shopify carries 6 dedicated Kids variants on Water Shoes (DarkGrey, Black, Blue, Bright Yellow, White, LightGrey), all at 0 inventory, documented nowhere. Discontinued, or should they come back? Separate question from "kids 2–5 fit Medium."
- [?] **Foot length inches.** Removed from the size chart because they matched no source. If you ever want a measurement column, someone has to measure a real pair.
- [x] **Duties at checkout — confirmed DDP.** Andrew 2026-08-12: *"we are collecting DDP."* Nothing to do; the checkout setting backs the copy. Closed. *(If markets or the carrier ever change, this claim is on the FAQ, the Returns page, and the collection FAQ — CA-18.)*

---

## B · HelpScout saved replies

Six edits. The corrected text already lives in `helpscout-kb/Barreletics_Email_Template_Master.md`, so you can copy from that file in the editor rather than retyping. Exact replacement text is in section F below.

Do the two sizing ones first if you only have time for two — wrong sizing costs returns; the rest is wording.

- [ ] **2.1 Sizing — Size chart.** Wrong Large range. Says women's 8–10.5; should be 7.5–11, and add kids' 2–5 to Medium.
- [ ] **2.2 Sizing — Between sizes.** Missing the 8.5-and-above rule, and the width rule needs to cover 7.5 as well as 8.
- [ ] **2.7 Sizing — Tight toe box (blow dryer).** BRAND NEW saved reply. Doesn't exist yet.
- [ ] **4.4 Product — Materials.** Says "hypoallergenic." Retired by D-019.
- [ ] **4.5 Product — Lifespan.** Says "gentle environment," which reads like we're calling studio work easy.
- [ ] **4.9 Product — Allergy and skin sensitivity.** Says "hypoallergenic." Same retirement.
- [ ] **5.3 Shipping — International duties.** Led with "be prepared to pay them on delivery." Duties are charged at checkout, so that framing talked people out of international orders. Reordered so the fact leads — **your hedge about customs varying by country is kept**, just moved after it.

---

## C · ManyChat

- [?] **First, tell us how ManyChat gets its answers.** The `manychat-kb/*.md` files are written as AI knowledge base articles. If your setup **ingests them as uploaded documents**, this whole section is "re-upload five files" and takes two minutes. If the answers are **typed into individual flow blocks**, it's laborious and you should only bother with the sizing ones.
- [ ] Update from these five corrected files: `03-sizing-chart.md` (Large 7.5, kids column, width rule) · `05-why-better-than-socks.md` (antimicrobial line) · `06-care-and-cleaning.md` (antimicrobial + longevity) · `09-faq-fit-sizing.md` (retired the half-size advice) · `10-faq-general.md` (longevity).
- [ ] **Do NOT add the blow dryer trick to ManyChat.** Deliberate — automation can't tell whether someone has bought yet or whether the size is right, so a bot would eventually hand a hairdryer to a browser. HelpScout only, sent by a human.

---

## D · Shopify Admin — live theme and product data

The repo fixes the M4 build. These live in Admin and survive any theme push.

- [ ] **Water Shoes product description — one field, twelve pages.** Verified live 2026-08-12. The description on `/products/aquatic-performance-skins` reads: "Perfect for outdoor adventures, the closed sole provides grip, stability, and protection from hot sand. **Ideal for paddle-boarding, boating and poolside activities.** Always check wet surfaces for slippage." Shopify echoes it into JSON-LD structured data on **every page of the site**, which is why "poolside" appears sitewide. Fixing this one field clears all of it. Suggested: "Perfect for outdoor adventures — grip, stability, and protection from hot sand. Ideal for paddle-boarding, boating, beach, and resortwear. Certain wet tile and stone areas are inherently slippery for any footwear."

- [ ] **`/blogs/news/barre-anywhere` — the real problem.** Verified live 2026-08-12. This is an **aqua barre article**: how to convert a land barre class into an aqua barre class in the shallow end with a pool noodle, and it pitches Performance Skins for "working out in the pool doing water aerobics, aqua barre or any other pool or beach activity." It actively recommends the product for pool use, which is exactly the slip liability P-012 exists to prevent. Unpublish or rewrite — don't just trim the word "pool."

- [ ] **`/blogs/news/eating-healthy-is-important-to-maximize-your-performance-in-the-water` — lower risk.** A nutrition article for aquatic athletes and swimmers. Off-brand and it draws aquatic-fitness traffic, but it never recommends the shoes for wet surfaces. Your call whether it's worth the SEO of an existing indexed post.

- [ ] **No other pool language in the blog.** All 14 live articles were scanned 2026-08-12. There is no post titled "aqua barre" or "water aerobics" — the earlier rule named them imprecisely. Everything else was the JSON-LD echo above.

- [ ] **Antimicrobial in live product descriptions.** Admin copy, not repo copy. Replace with: non-porous, wipes clean, nothing soaks in the way it does in fabric.
- [ ] **Product FAQ "Great for" list and the FAQ caution line** (per P-012). Not yet re-verified against the live site — check whether these still carry pool wording before spending time on them.
- [ ] **Coperni variant titles.** Shopify variant names appear to read `L (W 8-11)`. If the size range is baked into the variant title, that's an Admin rename — the repo can't fix it.
- [ ] **Live size chart renders its table twice.** Identical both times. Live-theme bug, unrelated to the M4 build.

---

## E · Optional cleanup — Admin template suffixes

Not urgent, but it's a permanent trip hazard. Three Admin pages point at a template whose filename doesn't match the handle, two of them with typos baked in:

| Page | Handle | Renders this template |
|---|---|---|
| Shipping & returns | `/pages/returns` | `page.shipping-retruns.json` (typo) |
| Start a return | `/pages/returns-portal` | `page.start-a-retrun.json` (typo) |
| Size chart | `/pages/performance-skins-size-chart` | `page.size-chart.json` |

- [ ] Repoint each page's template in Admin to the canonical name, then the duplicate alias files can be deleted from the repo. Until then **every agent must push both files in each pair** or the change appears not to work. This has already burned one session.

---

## F · Exact replacement text for HelpScout

Plain text, no formatting — select and copy straight into HelpScout.

### 2.1 Sizing — Size chart

Replace the sizing line with:

Sizing runs M (women's 5.5–7.5, kids' 2–5) and L (women's 7.5–11, men's up to 10.5). Tell us your usual shoe size if you'd like a recommendation.

### 2.2 Sizing — Between sizes

Replace the bullet list with:

Foot width is the deciding factor, not rounding up:

- Wide foot at 7 or 7.5 → size up to the Large
- Narrow foot at 7.5 or 8 → size down to the Medium
- 8.5 or above → stay in the Large regardless of width; you need the length

Let us know which sounds like you and we'll help from there.

### 2.7 Sizing — Save the return (tight toe box) — NEW

Send only when the customer already owns the pair, says it's tight in the toe box specifically, and the size is otherwise right. If the whole pair feels small, use 2.5 and exchange instead.

Hi [first name],

Since we manufacture these ourselves, we've picked up a trick for exactly this.

First things first though — if the whole pair feels small, let's just exchange it. That's free and it's the better fix, so reply with your usual shoe size and I'll set it up.

But if the size is right and it's only the toe box that's snug, try this: warm that spot with a blow dryer for about 30 seconds, keeping the dryer moving rather than holding it in one place. Once it's warm, gently stretch the material with your hand. Warm is all you need — not hot — and do it with them off your foot.

That usually opens up the spot that's bothering you. If it doesn't, the exchange offer stands.

### 4.4 Product — Materials

Replace the bullet list with:

- Silicone-free
- Latex-free
- Skin-safe and non-toxic
- No hard plastics
- Non-porous, so it wipes clean — nothing soaks in the way it does in fabric

### 4.5 Product — Lifespan

Replace the second paragraph with:

That said, used for what they're designed for — Pilates, barre, reformer, Lagree, yoga — they hold up beautifully. One of our customers recently passed 1,000 classes on a single pair, and another is on year four of theirs.

### 4.9 Product — Allergy and skin sensitivity

Change the opening line to end with "skin-safe and non-toxic" instead of "skin-safe and hypoallergenic." Leave the patch-test advice exactly as it is — it's good.

### 5.3 Shipping — International duties

Replace the whole body with:

Yes, we ship worldwide — 195 countries via FedEx International Connect Plus. Shipping time and cost depend on your country and are calculated at checkout, and orders typically arrive within 7–14 business days.

A note on duties and taxes: these are charged at checkout, so in most cases there's nothing further to pay when your order arrives. Customs handling does vary by country, though — if they weren't collected up front, your local carrier or customs office may ask for them on delivery.

Let us know if you have a specific country in mind and we can help confirm.

---

## Log

**2026-08-12 (later)** — Duties correction. Andrew: duties are **prepaid**; the "customer responsible for duties" line was probably about warranty replacements. Corrected on nine live surfaces plus six source docs. Added HelpScout 5.3 to sections B and F. Authority: CA-18 · P-016 · D-054.

**2026-08-12 (later still)** — DDP confirmed by Andrew, so the section A verification question is closed the same day it was raised. Section A is down to the three sizing/variant questions.

**2026-08-12** — Created. Sections A through F from the canonical-answers pass: sizing corrected to L 7.5–11 with kids' 2–5, antimicrobial and bacteria claims retired in favor of the wipe-clean framing, longevity rewritten, "patented" confirmed accurate, 195 countries confirmed real, blow dryer tip routed to HelpScout only. Authority: `docs/11-CANONICAL-ANSWERS.md` · `planning/10-decision-log.md` D-053 · `docs/10-DECISIONS.md` P-015.
