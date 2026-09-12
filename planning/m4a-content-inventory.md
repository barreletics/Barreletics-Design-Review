# M4A Content Inventory

---
document: M4A Content Inventory
status: 🔵 Ready for Review
created: 2026-07-18
depends_on: [07-product-knowledge-base, 08-copy-guide, 11-navigation-architecture]
---

## Purpose

Inventory of all production content required for launch. Each item is cross-referenced against Doc 07 (Knowledge Base) and Doc 08 (Copy Guide) where applicable. Items requiring Owner approval are flagged.

---

## Homepage Sections

| Section | Content Needed | Source | Status |
|---------|---------------|--------|--------|
| Announcement strip — Message 1 | "Buy 2, Save 15% — Code SAVE15" | Doc 07 §16, Doc 08 | ✅ Ready |
| Announcement strip — Message 2 | "Free Shipping Over $150" | Doc 07 §15 (D-002) | ✅ Ready |
| Announcement strip — Message 3 | "30-Day Returns · Made in USA" | Doc 07 §13, §12 | ✅ Ready |
| Hero headline | **TWO concepts pending Owner comparison — do not lock.** Concept A: "The Pilates Sock Era Is Over" / Concept B: "Think Outside the Sock." | Doc 08 brand voice | ⚠️ Owner Comparison Pending (D-041) |
| Hero subheadline | Concept A: "Studio Workouts & Footwear Will Never Be The Same" / Concept B: "No Socks. Just Grip." | Doc 08 | ⚠️ Owner Comparison Pending (D-041) |
| Hero CTA | "Shop Performance Skins" or similar | Doc 08 | ✅ Ready |
| Value strip — 6 pillars | 360° Grip · Antimicrobial · Barefoot Control · Studio-Tested · Made in USA · Replaces Socks | Doc 07 §1, §12, §11 | ✅ Ready |
| 50/50 split — Category creation | "The grip sock era is over" framing | Doc 07 §11, Doc 08 | ✅ Ready |
| Social proof — Reviews | Customer testimonials with name/city | Doc 07 (quotes throughout) | ✅ Ready |
| Sock Math section | Cost comparison data ($74 vs $112-144/yr) | Doc 07 §11 | ✅ Ready |
| Disciplines section | Barre, Pilates, Lagree, Reformer, Yoga | Doc 07 §7 | ✅ Ready |
| Newsletter section | "Join the list" + benefit checkmarks (NO 10%) | `specs/frozen/footer.md` | ✅ Ready |
| GEO section | City/state-specific editorial content | Doc 12 | ⚠️ Needs Review |

## Collection Pages

| Page | Content Needed | Source | Status |
|------|---------------|--------|--------|
| `/collections/grippy-shoes` — Hero headline | Category-creation pillar headline | Doc 09, Doc 08 | ⚠️ Needs Review |
| `/collections/grippy-shoes` — Description | Educational intro (Performance Skins vs grip socks) | Doc 07 §11, Doc 09 | ✅ Ready |
| `/collections/grippy-shoes` — FAQ (4-6 items) | Top questions from Doc 07 | Doc 07 §1-§12 | ✅ Ready |
| `/collections/open-sole` — Hero headline | "Open Sole" positioning | Doc 07 §2 | ✅ Ready |
| `/collections/open-sole` — Description | Open Sole specifics | Doc 07 §2 | ✅ Ready |
| `/collections/closed-sole` — Hero headline | "Closed Sole" positioning | Doc 07 §2 | ✅ Ready |
| `/collections/closed-sole` — Description | Closed Sole specifics | Doc 07 §2 | ✅ Ready |
| `/collections/outdoor` — Hero headline | Outdoor/water use | Doc 07 §10 | ✅ Ready |
| `/collections/outdoor` — Description | Secondary use positioning | Doc 07 §10 | ✅ Ready |
| `/collections/new-arrivals` — Description | New arrivals intro | Doc 08 | ⚠️ Needs Review |
| `/collections/limited-editions` — Description | Limited edition framing | Doc 08 | ⚠️ Needs Review |
| `/collections/one-offs` — Description | One-of-a-kind framing | Doc 08 | ⚠️ Needs Review |
| `/collections/apparel` — Hero headline | Apparel collection intro | — | ⚠️ Needs Review |
| `/collections/apparel` — Description | Apparel positioning | — | ⚠️ Needs Review |
| `/collections/sale` — Description | Sale messaging | Doc 08 | ⚠️ Needs Review |

## Supporting Pages

| Page | Content Needed | Source | Status |
|------|---------------|--------|--------|
| `/pages/faq` | Full FAQ content (all sections from Doc 07) | Doc 07 §1-§16 | ✅ Ready |
| `/pages/about` | Brand story, mission, founder | Doc 02, Doc 01 | ⚠️ Needs Review |
| `/pages/contact` | Contact form, business hours, email | — | ⚠️ Needs Review |
| `/pages/shipping` | Shipping policy (1-2 days, $150 threshold, international) | Doc 07 §15 | ✅ Ready |
| `/pages/returns` | Return policy (30-day, sellable condition) | Doc 07 §13 | ✅ Ready |
| `/pages/warranty` | 90-day warranty details | Doc 07 §14 | ✅ Ready |
| `/pages/size-guide` | Size chart, fit guidance | Doc 07 §3 | ✅ Ready |
| `/pages/compare-open-closed-sole` | Open vs Closed Sole comparison | Doc 07 §2 | ✅ Ready |
| `/pages/grip-comparison` | Barreletics vs Grip Socks | Doc 07 §11 | ✅ Ready |
| `/pages/technology` | Materials, manufacturing, performance | Doc 07 §12 | ✅ Ready |
| `/pages/partners` | Partner Programs **routing hub** — three cards + general-inquiry fallback form | **D-048** | ✅ Built |
| `/pages/wholesale` | Wholesale inquiry — dedicated page + own qualification form (`BL-PARTNER-WHOLESALE`) | **D-048** | ✅ Built |
| `/pages/ambassador` | Ambassador program — dedicated page + own qualification form (`BL-PARTNER-AMBASSADOR`) | **D-048** | ✅ Built |
| `/pages/studio-program` | Studio partnership — dedicated page + own qualification form (`BL-PARTNER-STUDIO`) | **D-048** | ✅ Built |

> **UPDATED 2026-08-08 — the four partner rows above.** They previously read:
> `/pages/partners` = "Consolidated Partner Programs (Wholesale + Studio + Ambassador)" (D-042), with
> ~~`/pages/wholesale`~~, ~~`/pages/ambassador`~~ and ~~`/pages/studio-program`~~ struck as
> "🔄 Redirected — superseded by `/pages/partners`". Owner direction 2026-08-08 reversed the fold:
> **three dedicated program pages plus `/pages/partners` as a routing hub**. Recorded as **D-048** in
> `planning/10-decision-log.md`, superseding D-042. All four templates are built, type-corrected and
> mobile-QA'd (`planning/partner-programs.md` §5, `planning/partner-pages-qa/`). The three folding
> 301s are **retired** in `planning/m4a-redirect-map.md` — they would make the new pages unreachable.
> `/pages/become-an-affiliate` and `/pages/wholesale-calculator` still point at the hub and are unaffected.

## Navigation

| Element | Content | Source | Status |
|---------|---------|--------|--------|
| Primary nav items | Grippy Shoes, Apparel, Collaborations, Journal | Doc 11 | ✅ Ready |
| Grippy Shoes sub-items | Shop All, Open Sole, Closed Sole, Outdoor, Compare Styles | Doc 11 | ✅ Ready |
| Apparel sub-items | Shop All Apparel, Tops, Bottoms | Doc 11 | ✅ Ready |
| Utility nav | Help, Account, Cart | Doc 11 | ✅ Ready |
| Mobile utility | Help & FAQ, Account, Returns & Exchanges, Contact Us | Doc 11 | ✅ Ready |
| Footer — Shop column | All Grippy Shoes, Open Sole, Closed Sole, Outdoor, Apparel | Doc 11 | ✅ Ready |
| Footer — Support column | FAQ, Shipping, Returns, Warranty, Contact Us | Doc 11 | ✅ Ready |
| Footer — Company column | About Us, Journal, Collaborations, Compare Styles | Doc 11 | ✅ Ready |
| Footer — Newsletter | "Join the list" + benefit checkmarks (NO 10%) | `specs/frozen/footer.md` | ✅ Ready |

## Content Requiring Owner Approval

| Item | Reason | Priority |
|------|--------|----------|
| Homepage hero headline/subheadline | D-041: TWO concepts built for side-by-side comparison — Owner must choose before lock | Critical |
| About page — founder story & mission | Personal/brand narrative | High |
| Contact page — business hours & email | Operational detail | Medium |
| Partner program terms — wholesale / studio / ambassador | **D-048** (2026-08-08, supersedes D-042 "consolidated page built"): three dedicated pages + `/pages/partners` hub, all built. Terms are Theme Editor settings. Internal pricing never public. Ambassador 10/15/30/15 numbers are a proposal, not approved. | Medium |
| New Arrivals/Limited Editions/One-Offs descriptions | Merchandising tone | Low |
| GEO content blocks | Location-specific claims | Low |
| Collection hero headlines (pillar pages) | Editorial voice approval | Medium |
| Apparel collection description | New category positioning | Medium |

---

## Summary

- **Total content pieces:** ~65
- **Ready (sourced from Knowledge Base/Copy Guide):** ~38 (58%)
- **Needs Review (requires Owner approval or editorial decisions):** ~27 (42%)
- **Placeholder (no source exists yet):** 0

All "Ready" content is directly sourceable from locked Foundation documents. "Needs Review" items have a clear source but require editorial approval or contain business decisions only the Owner can make.

---

## Forms Inventory

| Form | Location | Action URL | Required Fields | Backend |
|------|----------|-----------|----------------|---------|
| Newsletter signup | Footer, Newsletter section | Shopify customer create | Email | Shopify (tag: "newsletter") |
| Contact form | `/pages/contact` | Shopify form endpoint | Name, Email, Subject, Message | Help Scout forwarding |
| Wholesale application | `/pages/wholesale` | Shopify form endpoint (`BL-PARTNER-WHOLESALE`) | Business name, business type, website, resale cert, first order size, contact name, email, ship-to, about, consent | Help Scout — Partners inbox |
| Studio Program application | `/pages/studio-program` | Shopify form endpoint (`BL-PARTNER-STUDIO`) | Studio name, website, city/state, locations, primary discipline, contact name, role, email, background | Help Scout — Partners inbox |
| Ambassador application | `/pages/ambassador` | Shopify form endpoint (`BL-PARTNER-AMBASSADOR`) | First/last name, email, city/state, discipline, stocking question, about, consent | Help Scout — Partners inbox |
| Partner general inquiry (hub fallback) | `/pages/partners` | Shopify form endpoint | Name, Email, Program interest, Message | Help Scout — Partners inbox |
| Review submission | PDP (via Judge.me) | Judge.me API | Rating, Title, Body, Name, Email | Judge.me |

> **UPDATED 2026-08-08 (D-048 supersedes D-042).** The four partner rows above replace a single
> *"Partner inquiry (unified) — `/pages/partners`"* row. There is no unified partner form: each program
> has its own qualification form on its own page, and the hub form is the fallback for people who don't
> know which program fits. Field lists and Help Scout routing: `planning/partner-programs.md` §3–§4.

### Form Configuration Notes

- All Shopify forms use `{% form 'contact' %}` or `{% form 'customer' %}` Liquid tags
- Help Scout forwarding requires email routing configuration in Shopify admin (Settings > Notifications)
- Judge.me review form is managed by the Judge.me app — no custom form needed
- Newsletter form tags contacts with "newsletter" for segmentation
- Success/error states styled per brand palette (D-033: no Material Design green/red)
- All forms meet WCAG 2.1 AA: visible labels, error messages, focus management
