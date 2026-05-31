# Barreletics Redesign — Handoff Document
## For the next chat session

---

## CRITICAL FIRST TASK

**The 50/50 split sections are the WRONG SIZE.** Three of the four splits ("Progress," "Never loses grip," "Safely push harder") do not match the first split ("Never slip in chair pose"). 

**Before doing anything else:**
1. Open v24 in browser (GitHub Pages or locally)
2. Screenshot all 4 splits side by side
3. Measure the rendered height of "Never slip in chair pose" — that is the CORRECT size
4. Make the other 3 splits match it exactly
5. Do NOT change CSS without visual confirmation

Current CSS (may still be wrong):
```css
.v11-split { height: 420px; overflow: hidden; }
.v11-split__copy { padding: 80px 72px; }
.v11-split__slogan { font-size: clamp(28px, 3.2vw, 42px); min-height: 0; }
```

---

## Current State

- **Latest file:** `Barreletics_Home_v24.html`
- **GitHub repo:** github.com/barreletics/Barreletics-Design-Review
- **GitHub Pages:** barreletics.github.io/Barreletics-Design-Review/
- **Shopify store:** barreletics.com (connected via MCP)
- **Research Bible:** `Barreletics_Research_Bible.md` (in project knowledge — search it)

---

## What's Done
- ✅ Home page v10–v24 (iterative builds)
- ✅ Full section structure (22 sections)
- ✅ All slogans approved and placed
- ✅ 30+ reviews curated and categorized
- ✅ Industry research (barre/reformer/Lagree terminology)
- ✅ Design system (Roboto, colors, buttons, eyebrow rules)
- ✅ Asset inventory (all videos + images cataloged)
- ✅ Coperni collab section
- ✅ Value/price comparison section
- ✅ Guarantee section (30-day / 90-day / 4-year)
- ✅ FAQ (6 questions, GEO-optimized)
- ✅ Instagram/Juicer feed placeholder

## What's NOT Done
- ❌ **50/50 split sizing** — still wrong, fix first
- ❌ **PDP v3** — needs cost comparison + guarantee badge + double failure copy
- ❌ **Collection v2** — needs hero + benefit section + discipline cards
- ❌ **Mobile hamburger menu** — nav hidden on mobile, no hamburger
- ❌ **Custom Juicer feed** — using default embed, custom API recommended
- ❌ **GitHub upload** — v11–v24 + Research Bible need uploading by user

---

## Home v24 Section Order
1. Ticker (3 slides: SAVE15 / Made in USA / 1,000+ instructors)
2. Header (Journal not Blog)
3. Hero — "Secure in every hold. No sliding. No resets." + rotating eyebrow
4. Pillar strip — 6 pillars
5. Split 1: "Never slip in chair pose." (DEAD STOP) — Multi_Image ← REFERENCE SIZE
6. Belief band — "Your body moves. Your grip doesn't."
7. Product grid — 4 products, tabs (closed/open sole)
8. Promo tiles — Limited edition color + Performance apparel
9. Value section (cream bg) — "One pair. Done." — 3-col price comparison
10. Split 2: "Progress, built from the ground up." — IMG_5051
11. 3 Disciplines — Barre / Reformer / Megaformer
12. Split 3: "Never loses grip." — pink foot video
13. Video section — 3-up (action + slip-on + rinse)
14. Reviews — 6 testimonials, "1,000+ five-star reviews"
15. Coperni collab — "The Pilates sock era is over." + runway
16. Journal preview — 3 articles
17. Split 4: "Safely push harder in every studio move." — blue bg
18. Guarantee — "Zero risk. All grip." — 3 panels
19. Newsletter — "10% off your first pair"
20. FAQ — 6 questions
21. Instagram feed — @barreletics + #letusknockyoursocksoff
22. Footer

---

## Design Rules (DO NOT BREAK)

- **Font:** Roboto only (300–700). No Josefin Sans.
- **Eyebrows:** 12px/700/0.14em/uppercase — WHITE `rgba(255,255,255,0.7)` on dark/image sections. Coral `var(--br-accent)` ONLY on white/light backgrounds.
- **Buttons:** Square (radius 0), black #050505.
- **"Blog" → "Journal"** everywhere.
- **Colors:** bg=#fff, text=#050505, accent=#f97250, star=#fbc02d
- **50/50 splits:** Reference = v18 "Never slip in chair pose." All splits must match.
- **Mobile breakpoint:** 768px. Splits stack, height: auto.

---

## Key Brand Copy

**Hero H1:** "Secure in every hold. No sliding. No resets."
**Hero body:** "Not a sock. A performance skin. 360° grip through every pose, transition, class — on the mat or off it."
**Double Failure:** "Your foot moves in the sock. The sock moves on the floor. Now neither does."
**Price Math:** Grip socks = $144–$336/yr. Barreletics = $74 once.

---

## Where to Find Everything

| What | Where |
|------|-------|
| All reviews + industry research | Search project knowledge: "Barreletics Research Bible" |
| Slogans | Memory entries #3 and #4 |
| Design rules | Memory entry #6 |
| Asset URLs | Memory entry #8 + Research Bible Section 8 |
| Section order | Memory entry #9 |
| 50/50 issue | Memory entry #10 |
| HTML files | GitHub repo or project files |

---

*Last updated: May 25, 2026*
