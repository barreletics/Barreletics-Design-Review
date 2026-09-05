# Cloud handoff — Brand / About (ONE SUMMARY)

**Date:** 2026-08-13 · **Owner:** Andrew Nehra

---

## STEP 0 — Reply before you edit anything

**Can you see this repo and these files?** Reply yes or no with what you actually have:

```
ls docs/Barreletics\ Brand\ -\ Definitive-v*.html
ls planning/cloud-handoff-brand-about.md
```

**You must see v4–v14.** If you only see v1–v3, **STOP** — tell Andrew. Those files are not on GitHub yet (local only). He must commit + push `finish-home-collections` before you can work.

---

## Connect to the repo

| | |
|---|---|
| **GitHub** | https://github.com/barreletics/Barreletics-Design-Review |
| **Branch** | `finish-home-collections` |
| **Clone** | `git clone https://github.com/barreletics/Barreletics-Design-Review.git` |
| **Checkout** | `git checkout finish-home-collections && git pull` |
| **Andrew's local path** | `/Users/andrewnehra/Documents/GitHub/★ Barreletics-Design-Review` |
| **Work in** | `docs/` (HTML mocks) · read `planning/cloud-handoff-brand-about.md` |
| **Prior chat** | search transcript `8a732146-f103-4974-a93d-48ae5df35900` for "closest yet", "wrong direction" |

### What's on GitHub vs local-only (2026-08-13)

| On `origin/finish-home-collections` | Local only (unpushed) |
|---|---|
| v1, v2, v3 | **v4–v14**, modified `docs/index.html`, this handoff file |

**Andrew:** push before Cloud starts, or Cloud only has v1–v3 and will fail.

### Preview locally

```bash
cd docs && python3 -m http.server 8903
# http://localhost:8903/Barreletics%20Brand%20-%20Definitive-v14.html
```

Cloud: if you can't run localhost, use GitHub raw or htmlpreview on pushed files — **still confirm file list first**.

---

## The problem

We spent **more time on this page than the entire PDP**. Insane.

This is the **simplest page on the site** — founder story, photos we have, copy we have. FAQ / Contact / Returns were faster. **Do not explore layout directions. One small pass. Stop.**

**Scope:** HTML mock in `docs/` only. **No Shopify.** No `shopify-build/` edits. No theme push until Andrew says **`LOCK THIS`** + theme `187144929571`.

---

## Your job

Create **`docs/Barreletics Brand - Definitive-v15.html`** — small fix-forward from **v14**. Update `docs/index.html` hub card. One preview link. Wait for **`approved`**.

**Blend:** v10 structure + v3 type scale + v8 "closest yet" + v14 statement-on-hero. **Not v13. Not v7. Not v6.**

---

## Fixed page stack (do not add sections)

1. Jump hero (`barreletixxjumpingtogether.jpg` — cover OK)
2. Black statement **on hero unit** — *We didn't improve the grip sock. We made it obsolete.*
3. Intro — H1 Our story · lede · Stefanie Miller, Founder
4. **One split** — chair photo + founder copy (chair **contain, white, BIG**)
5. **One split** — prototype + product birth (cream OK on this row)
6. Joseph — museum pair on ink + essay below (v10) OR one white 50/50 (**NOT** v13 ink column)
7. Made in USA facts — cream, big type, 4-up grid
8. Letter close — standing founder + signoff
9. GEO accordion · dark close · light footer

**Max 2 splits.** No wow bands. No values grid. No Home modules. No Help-only shell.

---

## ALL 14 VERSIONS

**Files:** `docs/Barreletics Brand - Definitive-v[N].html`

| Ver | Status | What | Andrew said |
|-----|--------|------|-------------|
| **v14** | **START HERE** | v10 flow + statement on hero + bigger chair | Current base |
| v13 | **REJECTED** | Full-bleed · cream=text only · ink wow · Joseph ink 50/50 | **"NOOO wrong direction"** |
| v12 | **BROKEN** | Duplicate CSS · incomplete | Don't ship |
| v11 | Rejected | + cream inset product beat | Inset photos bad |
| v10 | **GOOD STRUCTURE** | 2 splits · museum+essay · letter close | Flow warmed to |
| v9 | Prior | Frameless · letter close | Better, not home run |
| v8 | **CLOSEST YET** | v3 scale · fixed narrative · museum · facts | **"Closest yet"** |
| v7 | Rejected | Help-page shell | Too plain |
| v6 | Rejected | Home ping-pong | Over-built |
| v5 | Rejected | Running pink photo | Wrong image |
| v4 | Rejected | Chapter eyebrows | Banned |
| v3 | **REFERENCE** | Cinematic scale · hang · museum · facts | Liked scale · **never overwrite** |
| v2 | Archive | Dual header + our-story | — |
| v1 | Archive | Lookbook · values | **never overwrite** |
| **v15** | **YOU CREATE** | Polish v14 only | — |

**Preview URLs** (after `python3 -m http.server 8903` in `docs/`):

```
v1  …/Barreletics%20Brand%20-%20Definitive-v1.html
v2  …/Barreletics%20Brand%20-%20Definitive-v2.html
v3  …/Barreletics%20Brand%20-%20Definitive-v3.html
v4  …/Barreletics%20Brand%20-%20Definitive-v4.html
v5  …/Barreletics%20Brand%20-%20Definitive-v5.html
v6  …/Barreletics%20Brand%20-%20Definitive-v6.html
v7  …/Barreletics%20Brand%20-%20Definitive-v7.html
v8  …/Barreletics%20Brand%20-%20Definitive-v8.html
v9  …/Barreletics%20Brand%20-%20Definitive-v9.html
v10 …/Barreletics%20Brand%20-%20Definitive-v10.html
v11 …/Barreletics%20Brand%20-%20Definitive-v11.html
v12 …/Barreletics%20Brand%20-%20Definitive-v12.html
v13 …/Barreletics%20Brand%20-%20Definitive-v13.html
v14 …/Barreletics%20Brand%20-%20Definitive-v14.html  ← START
```

---

## Approved images (CDN — do not swap)

| Use | Handle |
|-----|--------|
| Hero jump | `barreletixxjumpingtogether.jpg` |
| Founder chair | `43879272_2264664830242380_3230081226412916736_n.jpg` — contain |
| Letter close | `43677226_2264668403575356_8867191498509123584_n.jpg` |
| Prototype | `b.jpg` — contain |
| Joseph ×2 | `Screenshot_2026-06-06_at_6.59.10_PM.png` · `…9.58.53_PM.png` |

**Banned:** running pink · Square_Pink · crops that cut Stefanie off

---

## Copy law (instant fail)

**Never:** fully enclosed · enclosed heel · Open=barre / Closed=reformer · pool / poolside / aqua barre  
**Closed Sole:** "Heel and foot fully covered."  
**Both:** "Same grip, same stability. Choice is preference and feel only."  
**Source:** `docs/09-PRODUCT-KNOWLEDGE.md`

---

## Chrome

Nav #2 · 13px/500 Roboto · logo 42px · light footer Join the list · **NO 10%**

---

## v15 — allowed (pick 2–3 max)

1. Bigger chair (max-height / less padding)
2. Joseph — one white 50/50 if museum+essay too heavy (not v13)
3. Mobile spacing — image then copy in splits
4. Hero + statement reads as one unit

**Forbidden:** new sections · new layout · v13 · v7 · v6 · git restore · shopify-build · commit without Andrew

---

## Reply format

**First message:**
```
REPO CHECK: [yes/no]
FILES SEEN: v1–v3 only OR v1–v14
BRANCH: finish-home-collections
READY: [yes/no — if no, need Andrew to push v4–v14]
```

**When done:**
```
APPROVING: Brand About v15
LOOK FOR: v10 flow · v3 scale · no v13 · chair + mobile
LINK: [preview url]
Reply approved or what's wrong.
```

---

## Andrew note

Push `finish-home-collections` (v4–v14 + index + this file) before Cloud starts, or they can't see the work.
