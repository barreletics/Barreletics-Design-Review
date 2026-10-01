# Ambassador program — research + recommendation (Track E0)

**Status:** AWAITING ANDREW · 2026-08-12  
**Owner:** cloud (Track E0)  
**Scope:** research + recommendation only  
**Hard stops:** no Shopify app install · no theme Liquid/template edits · no nav/footer implementation until Andrew approves this plan  

**Prior deep dive (still authoritative for numbers/tooling detail):** `planning/partner-programs.md` (§0 deferral · §2A terms proposal · §7 UpPromote proposal). This doc is the **decision brief** for E0 — not a rewrite of that file.

---

## 1. What already exists

### 1.1 Repo surfaces (built)

| Surface | Path | Role today |
|---|---|---|
| Ambassador page | `templates/page.ambassador.json` + `sections/page-ambassador.liquid` | Plain H1 + who-it’s-for + native contact form (`BL-PARTNER-AMBASSADOR`). **No commission / discount figures on the page.** |
| Partners hub | `templates/page.partners.json` + `sections/page-partners.liquid` | Three cards → Wholesale / Studio / Ambassador + general inquiry (`BL-PARTNER-GENERAL`) |
| Studio program | `templates/page.studio-program.json` + `sections/page-studio-program.liquid` | Separate B2B studio intake |
| Wholesale | `templates/page.wholesale.json` + `sections/page-wholesale.liquid` | Separate wholesale intake |
| Specs | `specs/frozen/ambassador.md` · `specs/implementation-maps/ambassador.md` | **D-048 current** — dedicated `/pages/ambassador`; hub at `/pages/partners` |
| Decision log | `planning/10-decision-log.md` → **D-048** (supersedes D-042 fold) | Three program pages + hub |
| Research / terms / tooling | `planning/partner-programs.md` | Full comps, §2A proposed terms (**NOT APPROVED**), §7 UpPromote proposal (**NOT APPROVED**) |
| Local QA | `planning/partner-pages-qa/` | Mobile/desktop harness from 2026-08-08 |
| Help Scout copy | `helpscout-kb/Barreletics_Email_Template_Master.md` §7 | Wholesale / studio / instructor **manual codes** already in ops language (`0-WHOLESALE-*`, `0-Wholesale-Instructor`). Note: *“Affiliate program — once built…”* still a placeholder. |

**Page shape (owner direction 2026-08-08, still in Liquid comments):** heading + one paragraph + form. No benefits grid, FAQ, or public rates. R-10 (never publish commission rates) and R-11 (affiliate embed deferred) remain in force in the frozen spec.

### 1.2 Nav / footer / redirects (as coded or planned)

| Location | Current state |
|---|---|
| **Footer (repo)** | `snippets/footer.liquid` Company column → **Partner Programs** → `/pages/partners` |
| **Primary / Help nav** | No ambassador or partners link in header Liquid. Help pick list (`planning/help-pages-variation-index.md`) explicitly parks Ambassador under Track E. |
| **Legacy mocks** | Many `files/Barreletics_Home_v*.html` footers still show “Become an affiliate” placeholders — not live theme authority. |
| **Redirects that should stay** | `/pages/become-an-affiliate` → `/pages/partners` · `/pages/wholesale-calculator` → `/pages/partners` |
| **Redirects that must NOT exist (D-048)** | `/pages/ambassador`, `/pages/studio-program`, `/pages/wholesale` must **not** 301 to partners (would make dedicated pages unreachable) |

**Doc drift to be aware of (not fixed in this track):** `planning/m4a-redirect-map.md` CSV and `planning/m4a-navigation-config.md` Admin note 6 still describe the old D-042 fold. Frozen specs + `partner-programs.md` + decision log carry **D-048** as current. Owner/Brian should confirm Shopify Admin URL Redirects match D-048 before launch.

### 1.3 Shopify Admin clues (inferred — no Admin access this run)

From Help Scout templates + partner-programs owner checklist:

1. **Manual instructor/wholesale discount codes already exist in ops copy** — the brand already runs code-based partner economics without an affiliate app.
2. **Four Admin pages may still need creating / template assignment** (`ambassador`, `studio-program`, `wholesale`, `partners`) — listed as owner/Brian tasks in `partner-programs.md` §4.5; not verified live.
3. **No evidence an affiliate app is installed** (Collabs / UpPromote / ReferralCandy / GoAffPro) in repo or KB.
4. **Contact forms** post to the store Sender email via native `{% form 'contact' %}` — routing depends on mail filters + Help Scout (proposed Partners inbox; not confirmed live).
5. **Ambassador program economics are deliberately blank** — owner (2026-08-08): *“earmark that for the second phase.”* Page approved in shape; program not designed.

---

## 2. Options comparison

| Option | What you get | Fit for Barreletics instructors | Cost (public list, 2026-08) | Verdict |
|---|---|---|---|---|
| **A. Shopify Collabs** | First-party apply → codes/links → attribution → payouts on Shopify bill (~2.9% of commission paid) | **Weak.** Creators need Collabs accounts; Discover is US/UK/CA; secondary sources report ~1k follower floors and paused new creator signups. Instructor-first roster (class influence, often &lt;1k followers) is the wrong product shape. | $0 app + fee on commissions | **Do not use for v1.** Reconsider only if a named instructor can create/join Collabs in a five-minute test. |
| **B. UpPromote (Free)** | Unique code + link, commission ledger, registration form, fraud basics; **manual payouts** on Free | **Strong.** No follower gate. Works for invite-only instructors. Matches prior owner ask (“Find an app please”) in `partner-programs.md` §7. | **$0/mo**, no revenue share on Free · ceiling ~$3k reviewed referral sales/mo · Growth $29.99 + **2%** | **Best app if Andrew wants an app.** |
| **C. ReferralCandy** | Refer-a-friend + affiliate positioning | Misaligned primary use case (customer referral loops). Expensive vs instructor affiliate need. | From **$39/mo + 10.5%** success fee (lower % at higher tiers) | **Skip.** Wrong tool / wrong cost curve. |
| **D. GoAffPro / Refersion / Social Snowball** | Full affiliate stacks | GoAffPro = solid #2 (free tier, Premium flat $49). Refersion from $39+3%. Snowball from $249+3%. | Paid or revenue-share heavy | Hold as later alternatives; not v1. |
| **E. Manual landing + Shopify discount codes** | `/pages/ambassador` form + one code per person + monthly Shopify discount report + PayPal/Venmo | **Strong for first ~10–15.** Already how wholesale/instructor codes work in Help Scout. Breaks around 25–30 people. | $0 software | **Simplest possible ops.** |
| **F. Native Shopify pages only (no tracking program)** | Pitch + application form; reply with terms privately; no attribution/commission automation | Fine for **intake only** while terms are undecided — **current page state**. Does not run a paid ambassador program. | $0 | **Correct until terms + tooling approved.** |

---

## 3. Recommended approach (simplest that fits)

**Ship the pages as an application funnel; run v1 as invite-only instructors; track with unique Shopify codes; add UpPromote Free only when Andrew wants a ledger / self-serve apply.**

Concrete sequence:

1. **Keep public page blank of rates** (already true). Who it’s for + response time + form only.  
2. **Approve economics offline** (see §5) before any Theme Editor numbers or app config. Proposed starting point from prior research (`partner-programs.md` §2A — still NOT APPROVED): **10% commission · 25% personal (non-shareable) · 15% audience code · one gifted pair on acceptance · invite-only 10–15.**  
3. **v1 ops = Option E** unless Andrew explicitly chooses an app: create one discount code per accepted instructor; pay monthly from code reports; gift via single-use 100% code or $0 draft order.  
4. **If Andrew wants an app now → Option B (UpPromote Free)** — not Collabs, not ReferralCandy. Point Apply at UpPromote registration **or** keep native form and re-key approved people (2 minutes each).  
5. **Do not install anything until Andrew answers §5.**

Why this beats Collabs / paid referral apps: Barreletics ambassadors are **teachers with in-room influence**, not Collabs-network creators; the brand already issues partner codes by hand; Free UpPromote only earns its keep once the spreadsheet hurts.

---

## 4. Where links should live

| Placement | Recommendation |
|---|---|
| **Footer → Company** | Keep **Partner Programs** → `/pages/partners` (already in `snippets/footer.liquid`). Hub card → `/pages/ambassador`. |
| **Primary nav** | **No.** Partners is not a shop path; header stays product-led. |
| **Help / Support menu** | **Optional secondary** — “Partner programs” or “Teach with us” only if Help pick session wants it. Not required for v1; Track A already excludes Ambassador from Help picks. |
| **Dedicated page** | `/pages/ambassador` is the canonical apply URL (D-048). |
| **Legacy URLs** | Keep `/pages/become-an-affiliate` → `/pages/partners`. Do **not** deep-link old affiliate URL past the hub until brand copy settles on “Ambassador” vs “Affiliate.” |
| **Contact form topic** | Wholesale Inquiry already exists on contact; leave ambassador traffic on the dedicated form (cleaner routing via `BL-PARTNER-AMBASSADOR`). |

**No nav/footer changes in this track** — placement above is the plan to implement only after Andrew approves.

---

## 5. Decisions Andrew must make

| # | Decision | Why it blocks |
|---|---|---|
| **1. App Y/N** | **None for now** · **UpPromote Free** · or test Collabs with one instructor | Determines Apply button target and whether Help Scout stays the intake |
| **2. Commission** | Approve or rewrite §2A: cash % on post-discount subtotal | Cannot populate TE settings or app program without this |
| **3. Audience code depth** | 15% vs 10% (COGS-dependent) | Stacks with commission on the same order |
| **4. Personal discount** | 25% (proposed) vs other | Must stay below studio/wholesale trade pricing |
| **5. Gifted pair Y/N** | One pair on acceptance for invite-only cohort? | Inventory / COGS budget |
| **6. Roster model** | Invite-only 10–15 vs open public apply | Controls free-product abuse and ops load |
| **7. Legal / tax** | Written terms + W-9 / 1099 path for cash commissions; FTC disclosure expectation for ambassadors | Required before first payout; counsel or existing template |
| **8. Admin plumbing** | Create four pages + confirm D-048 redirects (no fold of ambassador→partners) + Partners Help Scout inbox? | Pages unreachable / mail chaos without this |
| **9. Landed COGS** | Rough COGS/pair (freight + duty) | Confirms whether 15% audience code is safe |

**Nothing below goes on the public page without a separate written approve of published figures.** R-10 stays default: rates confirmed in writing on acceptance.

---

## 6. Draft URL structure (no implementation)

```
/pages/partners                 ← hub (Wholesale · Studio · Ambassador cards)
/pages/ambassador               ← canonical apply + pitch (blank rates)
/pages/studio-program           ← separate program (out of E0 scope to build)
/pages/wholesale                ← separate program (out of E0 scope to build)

# Legacy (keep 301 → hub)
/pages/become-an-affiliate  →  /pages/partners
/pages/wholesale-calculator →  /pages/partners

# Do NOT 301 (D-048)
/pages/ambassador        ✗→ /pages/partners
/pages/studio-program    ✗→ /pages/partners
/pages/wholesale         ✗→ /pages/partners
```

**Optional later (only if app approved):**  
`/pages/ambassador` Apply CTA → UpPromote hosted registration URL (external), while the Shopify page remains the brand pitch.

**Preview (after Admin pages exist + M4 has templates):**  
`https://barreletics.myshopify.com/pages/ambassador?preview_theme_id=187144929571`  
`https://barreletics.myshopify.com/pages/partners?preview_theme_id=187144929571`

---

## 7. Stop state

- Artifact: this file  
- Queue: Track **E0** → **AWAITING ANDREW**  
- **No theme changes made** · **no app installed** · **no nav/footer edits**  
- Next only after Andrew replies on §5 (especially App Y/N + commission + legal)
