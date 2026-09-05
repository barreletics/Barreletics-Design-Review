# Copy audit — 2026-08-08

Pre-review sweep of every customer-facing copy surface against the 16 rules Andrew set today.
Words only — JSON validity, schema keys, images, links and mobile QA are a separate agent's lane.

**Scope swept:** `shopify-build/templates/**` · `shopify-build/sections/**` including `{% schema %}`
defaults · current mocks (Collection v19, SEO v37, FAQ v7, Journal v6, Help v4, Home WORKING,
PDP v19) · knowledge sources (`docs/09-PRODUCT-KNOWLEDGE.md`, `manychat-kb/**`,
`planning/m4b-tidio-knowledge-base.md`, `planning/07-product-knowledge-base.md`) ·
QA harnesses in `planning/pdp-variants-qa/`, `planning/partner-pages-qa/`, `planning/returns-pages-qa/`.

**Not touched (frozen):** `backups/**`, `archive/**`, `planning/archive/**`, prior mock versions,
and `docs/Barreletics PDP - Definitive-v19.html` (LOCKED — findings reported, file untouched).

No `git restore`. No `git checkout`. No commit. No Shopify command.

---

## 1. FIXED — 11 violations, 6 files

All fixes use only approved P-003 / brand-skill wording or are straight deletions. Nothing invented.

### 1.1 Discipline-to-sole assignment (rule 4) — the worst offender

**`shopify-build/templates/page.faq.json` → `sole-1`**

The most flagrant surviving violation in the repo. It assigned both soles to disciplines by name,
in bold, on the public FAQ page:

- Before: *"**Open Sole:** Heel grounded to the surface, barefoot connection, mid-foot ventilation.
  **Best for barre, yoga**, and practices where heel contact matters. **Closed Sole:** Full underfoot
  coverage, more protection, slightly warmer. **Best for reformer, Lagree**, and practices with footbar work."*
- After: the P-003 wording for each sole, then *"Both perform identically — same grip, same stability,
  same studio uses. Choice is preference and feel only."*

**`shopify-build/templates/page.faq.json` → `sole-2`** (question: "Which style is better for reformer?")

- Before: *"Most reformer practitioners prefer Closed Sole for the full underfoot coverage during
  footbar work. However, some prefer Open Sole for the barefoot connection."* — a sole recommendation,
  dead under P-004-superseded.
- After: *"Either. Both soles perform identically across barre, reformer Pilates, Lagree, and Megaformer
  — same grip, same stability, same studio uses. Choice is preference and feel only."*
  (Identical to the already-approved answer in `page.compare.json` → `geo-compare-2`.)

**`shopify-build/templates/collection.closed-sole.json` → `geo-reformer`, `geo-barre`, `geo-lagree`**

Three GEO blocks under the heading "Why studios choose Closed Sole" claimed reformer, barre and
Lagree for the Closed Sole with no parity statement anywhere on the page — exactly the
`❌ "Best for reformer footwork, barre, and Lagree" (as a Closed-Sole-only claim)` example in the rule.
The sibling `collection.open-sole.json` already carries parity lines; this file did not.

Appended to each: *"Both soles perform identically — same grip, same stability. Choice is preference
and feel only."* The SEO questions themselves are untouched.

### 1.2 "Enclosed" constructions (rule 3)

**`shopify-build/templates/collection.closed-sole.json`** — two live instances, both calling the
Closed Sole *enclosed*:

- `geo-barre`: "**Full enclosure** means nothing shifts during small isometric movements"
  → "**Heel and foot fully covered**, so nothing shifts during small isometric movements"
- `geo-sizing`: "Snug and secure — **the full enclosure** should hug your foot without bunching"
  → "Snug and secure — **heel and foot fully covered**, hugging your foot without bunching"
- `geo-reformer`: "Closed Sole **wraps heel to toe**" → "Closed Sole has the **heel and foot fully covered**"

These were the last two "enclosed" constructions in any live surface. Every other repo hit for
"fully enclosed" is a dated RETIRED banner or a frozen backup, which the rule permits.

### 1.3 Schema defaults re-seeding the drift (rule 3 / 4)

**`shopify-build/sections/page-compare.liquid`** — the `{% schema %}` defaults still shipped the
retired wording, so any newly added Compare section would regenerate it even though both compare
templates are clean:

- `product_a_desc`: "Heel grounded to the surface. Barefoot connection. Mid-foot ventilation."
  → "Heel exposed, mid-foot breathing hole. More grounded, barefoot feel. Natural toe splay."
- `product_b_desc`: "Full underfoot coverage. More protection. Slightly warmer."
  → "Heel and foot fully covered. Same grip, same stability."

No rendered output changes — `page.compare.json` and `page.compare-open-vs-closed.json` both set
these explicitly and were already correct. This closes the regeneration path.

### 1.4 Wet-surface grip promise (rule 12)

**`shopify-build/templates/collection.outdoor.json` → `geo-boat`**

- Before: *"**Wet fiberglass**, teak decking, inflatable SUP surfaces — injection-molded grip **holds
  where rubber soles hydroplane**."* — an explicit grip-when-wet promise, the exact liability the
  no-pool letter was written about.
- After: *"Boating and paddleboarding — grip where bare feet slip. Lightweight enough to forget you're
  wearing them. **Always check wet surfaces for slippage.**"*

The replacement is lifted verbatim from the already-approved sibling block in
`product.outdoor.json` → `geo-boat`, plus the sanctioned caution line.

### 1.5 Unsupported superlative (rule 6 / slogan-skill anti-pattern)

**`shopify-build/templates/page.faq.json` → `geo-faq-2`**

- Deleted: *"Barreletics are the **#1** grip sock alternative for barre."* — "#1 / best in the world"
  is a named anti-pattern in the slogan skill. Sentence deleted outright; the remaining sentence
  stands on its own.

### 1.6 Invented third-party association (rule 6)

**`shopify-build/templates/product.json` → `collection-faq` → `geo-nyc`**

- Deleted: *"from **SoulCycle-adjacent studios** to boutique Lagree rooms"* — an invented association
  with a third-party brand, traceable to nothing.
- Replaced with the phrasing already approved in the sibling `product.open-sole.json` → `geo-nyc`:
  "from boutique Lagree rooms to classical Pilates studios".

This is a clause-level copy fix inside the living v19 spine. No section order, no block order, no
other setting touched.

### 1.7 Knowledge source that re-infects everything (rule 3 / 4)

**`planning/07-product-knowledge-base.md` §2 "Open Sole vs Closed Sole"**

This doc's **Messaging guidance** actively instructed agents to write the retired wording
("Closed Sole: Use 'full coverage' and 'more protection'"). That is why the phrasing keeps coming
back in new sections. Rewritten to the four sanctioned P-003 lines plus an explicit
"never write fully enclosed / never assign a discipline to a sole" instruction, with a rule-file
cross-reference. The **Abbreviated Version** was carrying the same drift and was corrected to match.

A do-not-reuse banner was added above the Key Customer Quotes (see item 3.2 — the quote itself is
untouched and awaits your call).

`docs/09-PRODUCT-KNOWLEDGE.md` and `manychat-kb/**` were checked and are **clean** — both already
carry correct RETIRED banners and no reusable banned phrasing.

---

## 2. NEEDS YOUR DECISION

### 2.1 Fabricated and altered customer testimonials (rule 16) — biggest open issue

The review sets in `product.json`, `index.json`, `page.reviews.json` and
`page.judgeme_all_reviews.json` are the same nine reviews. Checked against the 297-review corpus
recorded in `docs/08-LIVE-SITE-COPY-AUDIT.md`:

**a) One real customer's words published under a different name.**
`product.json` → `fifty-fifty-lifestyle` runs Mia Evans's live testimonial
("My love-hate relationship with the sock has finally come to a ceremonial end") but attributes it to
**"Sarah M. · Barre Instructor · New York, NY"**. The same quote appears three sections later in
`social-proof` → `r1` correctly credited to **"Mia Evans"**. Same page, same words, two different people.

**b) The same quote is also altered.** The live review reads *"The **vast** improvement during the
first minute of barre class, **with my new barreletics performance skin shoes**, is beyond words."*
The repo version drops both, and adds a sentence that does not exist in the original:
*"I will never go back."*

**c) A spliced quote.** `r3` publishes, as Dvorah S.: *"**I refuse to wear anything else.** I am 70
years old and able to accomplish advanced moves on the Cadillac apparatus…"* — but
"I refuse to wear anything else" is **Kimberly's** line (it runs as `t1`, credited to Kimberly,
Knoxville). Dvorah's real review opens *"The best invention known to Pilates Devotee's."*
Two customers' words are welded into one testimonial. The same splice appears in
`product.open-sole.json` → `r5` and, in a variant form, `product.outdoor.json` → `r1`
("The security is unmatched" is also Kimberly's).

**d) Six reviews with no traceable source at all.** `r4` Lauren T. (Los Angeles), `r5` Hannah R.
(Austin), `r6` Priya K. (Chicago), `r7` Jordan P. (Miami), `r8` Elena V. (Toronto), `r9` Chris N.
(London). None appear in the live review corpus. Their cities map one-for-one onto the geo-target
list in the brand skill (New York, Los Angeles, London, Melbourne, Toronto, Chicago, Austin, Miami),
which is what you'd expect if they were written to fill an SEO map rather than quoted from customers.

**e) Three anonymous "Verified Buyer" quotes** on `page.grip-comparison.json` (`quote-1`, `quote-2`,
`quote-3`) — also untraceable. See 2.2 for a second problem with `quote-2`.

Not rewritten — restoring these to verbatim, or pulling them, is your call. Real verbatim source for
Mia Evans and Dvorah S. is in `docs/08-LIVE-SITE-COPY-AUDIT.md` lines 191–195 and 385–389.

**Known, per your instruction:** the two "Open Sole for mat, Closed for machines" quotes (Chris N.,
`r9`) are real customer words and are reported, not touched. They appear in `product.json`,
`index.json`, `page.reviews.json`, `page.judgeme_all_reviews.json`, plus the SEO v37 and
Home WORKING mocks.

### 2.2 Unapproved heat claim (rule 13) — two instances, not one

**Known:** `shopify-build/templates/product.json` → `collection-faq` → `geo-hot`:
*"The patented grip surface **performs better when warm**."* Reported, not fixed, per your instruction.

**Second instance you may not know about:** `shopify-build/templates/page.grip-comparison.json` →
`quote-2` launders the same banned claim through an anonymous testimonial:
*"The grip actually **gets better as you warm up**, not worse."* Same claim, harder to spot, and it
carries the added problem of being an untraceable quote. Left alone pending the same decision.

The claim is also live in the locked PDP v19 mock — see section 3.1.

### 2.3 Internal QA note rendering as customer copy

`shopify-build/templates/index.json` → `proof-numbers` → `n2` has `detail`:
**"Attribution TBD — verify named review before publishing claim"**

That string renders on the homepage under the "Classes" stat. `proof-numbers` is on the
radioactive list, so I have not touched it. It either needs a real detail line or the stat pulled.

### 2.4 Footer newsletter benefit check

`shopify-build/sections/footer.liquid` benefit checks include **"Studio partner discounts and events"**.
No "10% off" anywhere — that rule is clean sitewide. But this line does promise a discount in general
terms, and the footer is frozen. Flagging only; confirm it is one of the approved checks.

### 2.5 Headlines with no traceable source (rule 6)

None of the specifically-dead lines you named have reappeared — "Carry the pair that replaces eight",
"Covered heel to toe", "Nothing left to slip", "Hot sand. Wet deck. Same grip.", "Built for the ground
you actually stand on", "Grip that travels", "Barefoot, but covered", "Stop selling socks your clients
throw away" all return **zero hits** across the entire repo.

These headlines are live but trace to neither the approved inventory, the knowledge docs, nor live
Shopify copy. Deleting a page's own title is destructive, so they are listed rather than cut:

| File | Headline |
|---|---|
| `page.about.json` | **"The Grip Sock Era Is Over"** — a one-word swap on the locked H1 "The Pilates Sock Era is Over". The slogan skill says kill these on sight. |
| `page.about.json` | "Redefining Grip" · "Built by Someone Who Gets It" |
| `page.grip-comparison.json` | "The Category Is Over" |
| `collection.hot-kits.json` | "Kits For The Hot Room." · "One set. Nothing left to figure out." · "Be first to the kits." |
| `collection.gift-cards.json` | "Give the Gift of Grip" |
| `collection.limited-editions.json` | "Limited Runs. Unlimited Grip." · "Current Drops" |
| `collection.new-arrivals.json` | "Just Dropped" · "Latest Drops" |
| `collection.one-offs.json` | "One of a Kind" · "Unrepeated Designs" |
| `collection.sale.json` | "Performance on Sale" · "Marked Down" |
| `collection.outdoor.json` | "From Beach to Boat Deck" · "Built for Outside" |
| `collection.json` | "Grip That Holds Where It Matters Most" |
| `proof-numbers.liquid` (default) | "Built for the ones who show up." · "Proof in numbers" |
| `guarantee-band` (product templates) | "Built on guarantees, not guesses." |

### 2.6 Unsupported claims outside the partner pages

Rule 7 covers partner pages, and those are clean (see 4.2). These sit elsewhere:

- `page.grip-comparison.json` → `faq-4`: *"**Most studios accept** Barreletics"* — no source.
- `page.grip-comparison.json` → `geo-grip-3`: heading **"Barreletics vs ToeSox vs Tavi Noir"** names
  two competitors by brand and asserts their product lifespan. Legal exposure, and not approved copy.
- `page.about.json` → `geo-about-2`: *"Studios **nationwide are recommending** Barreletics to their
  clients."* The approved claim is "Trusted by 1,000's of instructors".
- `product.json` / `product.open-sole.json` → `geo-nyc`: *"is the **preferred** grip footwear at barre,
  Pilates, and reformer studios across Manhattan…"* — unsupported superlative. The SoulCycle clause
  was removed (1.6); this framing remains and needs your call.
- `collection.outdoor.json` → `variant-grid` body: *"Water-ready, heat-resistant, **grip-locked on
  every surface**."* Reads as an absolute grip promise including wet. Borderline against rule 12.

### 2.7 Casing (rule 14)

- **`product.json` → `fullbleed-statement`: "TRANSFORM YOUR PRACTICE"** — known named part of the
  locked v19 composition. Reported, not changed, as instructed.
- Beyond that there are no ALL CAPS statements in the templates. There is, separately, broad
  **Title Case** inconsistency in headings ("Shop All Styles & Colors", "Limited Runs. Unlimited Grip.",
  "Built by Someone Who Gets It") against sentence-case headings elsewhere ("Never loses shape.",
  "One pair. Done.", "Real people. Real results."). Not ALL CAPS, so not a rule-14 breach, but it is
  visibly two systems on one site. Worth one decision rather than 30.

### 2.8 FAQ provenance (rule 15)

`page.faq.json` carries 24 FAQ items. Most map cleanly to the live product FAQ and the ManyChat KB.
These assert specifics I could not trace to Help Scout replies, the ManyChat KB, or the approved
knowledge docs:

- `fit-2` / `tip-4` (size-guide): *"Dark Grey, Hot Coral, and Blue **run slightly snugger** than
  Light Grey."* Repeated on three surfaces as fact. Not in `docs/09-PRODUCT-KNOWLEDGE.md`.
- `returns-2`: *"We offer **free shipping on size exchanges** within 30 days."*
- `shipping-1` / `shipping-2`: *"**195 countries** via **FedEx International Connect Plus**."*
- `care-2` / `materials-1`: *"**antimicrobial**"* and *"they **never** develop odor"*.
- `warranty-2`: the international claims process ("customer pays replacement shipping").

If these are real policy, they need to land in the knowledge doc so they stop being unverifiable.
If they are not, they are invented FAQs.

---

## 3. LOCKED FILES — need your letter

Nothing in this section was edited.

### 3.1 `docs/Barreletics PDP - Definitive-v19.html` (LOCKED)

- **Line 1554** carries the banned heat claim verbatim: *"The patented grip surface performs better
  when warm — unlike silicone dots that degrade with heat and moisture. Hot yoga practitioners report
  improved traction during sweaty flows."*

  This is the same string as `product.json` → `geo-hot`. Whatever you decide on the heat claim has to
  be applied in two places, and the mock one needs a `LOCK THIS` letter or a new `Definitive-v20.html`.
- Otherwise clean: no pool language, no invented scenery, no "fully enclosed", no 10% off, no Small size.

### 3.2 `planning/07-product-knowledge-base.md` — customer quote

*"Closed sole for reformer, open sole for barre — I own both." — Frequent buyer*

A discipline split sitting in a source document agents copy from. Because it is presented as a
customer's words I did not rewrite it. I added a dated do-not-reuse banner above it so the next agent
cannot lift it as source copy. Your call whether it stays as a record or comes out.

### 3.3 Live Shopify Admin — still carries banned copy (not a repo fix)

Confirmed still outstanding, consistent with `.cursor/rules/no-pool-positioning.mdc` and
`planning/returns-pages-qa/README.md`:

- `/pages/returns` Admin body: "tidal pools", "poolside yoga", "Boating and poolside",
  "Rocky shorelines & shell-covered beaches", "Pebbly lake beds and shell-covered shorelines".
  Visible in `planning/returns-pages-qa/preview-returns.html`, which is an intentional snapshot of
  live copy, not repo copy.
- Closed Sole / Water Shoe product description: "poolside lounging".
- Product FAQ "Great for" list and caution line.
- Product tags including `grippy shoes for pools` on `aquatic-performance-skins`.
- Aqua-barre and water-aerobics blog posts — the strongest pool signal on the site.

---

## 4. VERIFIED CLEAN

### 4.1 Rules with zero live violations

| Rule | Result |
|---|---|
| 1 — pool language | **Zero** hits in `shopify-build/**` and in all current mocks. Remaining hits are rule files, decision records, the `docs/08` evidence snapshot, the `docs/pool-copy-review.html` before/after review page, and frozen backups — all permitted. |
| 2 — invented scenery | **Zero** in `shopify-build/**` and current mocks. Remaining hits are the live-copy snapshots described in 3.3. |
| 5 — "10% off" | **Zero** in `shopify-build/**` and in every current mock. Only prior versions, frozen backups and retirement notes. `newsletter.liquid` and `footer.liquid` both carry explicit "NO 10%" guards in their headers. |
| 8 — tax content on partner pages | **Zero.** All four partner sections carry an explicit "Barreletics has never collected a resale certificate or tax ID (owner, 2026-08-08)" note. No tax field or copy survives. |
| 9 — reassurance filler | **Zero.** "A person will read it" / "we read every application" / "not a ticket queue" appear only inside code comments recording that they were cut. Stated response times (2–3, 3–5, 5–7 business days) correctly remain. |
| 10 — ambassador figures | **Zero published.** 10% commission, 15% after $2,500, 30% instructor discount, 15% audience code and the $25 payout threshold appear only in a `page-ambassador.liquid` comment explaining they are unapproved, and in `docs/REVIEW-2026-08-08.html` as a decision you still owe. |
| 11 — Small / "coming soon" size | **Clean.** `show_soon_size` defaults to `false` in the `pdp-buy-box.liquid` schema and is explicitly `false` in all three product templates; `size_soon_note` is empty everywhere. Both settings carry "Retired 2026-08-08 — Small is not offered" info text. The `collection.hot-kits.json` "Coming soon" eyebrows refer to unreleased kits, not a size. |
| 6 — the eight dead slogans | **Zero hits repo-wide** for all eight named lines. |

### 4.2 Partner pages

`page.partners.json`, `page.wholesale.json`, `page.studio-program.json`, `page.ambassador.json` and
their four sections were read in full. No volume pricing, no tiers, no minimums, no margins, no
payment terms, no exclusivity, no territory, no guaranteed lead times, no co-op marketing, no
"named account contact", no "real person on the account", no tax content, no reassurance filler,
no unapproved figures. These read as clean.

### 4.3 Knowledge sources

- `docs/09-PRODUCT-KNOWLEDGE.md` — clean. Banned-copy banner at the top, RETIRED banner on the old
  P-003 sentence, correct "do not assign disciplines to either sole" instruction at line 255.
- `manychat-kb/**` — clean. `02-open-vs-closed-sole.md` carries the RETIRED banner and the correct
  parity line; `04-pricing.md` retires the 10% offer; `10-faq-general.md` carries the no-pool banner.
- `planning/m4b-tidio-knowledge-base.md` — clean on every banned term.
- `planning/07-product-knowledge-base.md` — **was** re-seeding drift; fixed forward (see 1.7).

### 4.4 Current mocks

Collection v19, SEO v37, FAQ v7, Journal v6, Help v4 and Home WORKING are clean on pool language,
invented scenery, "fully enclosed", 10% off, discipline splits and Small-size references. SEO v37
and Home WORKING carry the known "Open Sole for mat, Closed for machines" quote (2.1). One borderline
line: `Barreletics Journal - Definitive-v6.html` line 512 — *"smarter than grip socks that slide when
wet"* — implies wet grip by contrast. Judgement call, left alone.

---

## 5. Preview regeneration and proof

Only `planning/pdp-variants-qa/` had a source file change behind it (`product.json`). Rebuilt with
`build.py`; all three previews and all six screenshots regenerated.

Post-rebuild grep of the **generated HTML** (not the source):

```
planning/pdp-variants-qa/*.html   SoulCycle|full enclosure|fully enclos|hydroplane|#1 grip sock  → 0 hits
shopify-build/**                  SoulCycle|full enclosure|fully enclos|hydroplane|#1 grip sock
                                  |Best for barre, yoga|Most reformer practitioners
                                  |Full underfoot coverage, more protection
                                  |Heel grounded to the surface                                  → 0 hits
```

`preview-closed.html` confirmed to render the corrected NYC line
("from boutique Lagree rooms to classical Pilates studios").

`planning/partner-pages-qa/` and `planning/returns-pages-qa/` were **not** rebuilt — no source file
behind them changed, and their previews were already free of the fixed strings. The pool language
visible in `preview-returns.html` is a deliberate snapshot of the live Admin body (3.3), not repo copy.

All edited JSON re-parsed clean; the `page-compare.liquid` schema re-parsed clean.
