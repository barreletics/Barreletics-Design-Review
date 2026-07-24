# Home Working Entry — Barreletics

**Read this first** for Home build, refine, theme gut, and copy.  
**WORKING mock:** `barreletics-design-review/design_handoff_barreletics 2/pages/Barreletics Home - Definitive-WORKING.html` (= **v29**)  
**Also:** `Definitive-v28.html` (no Knock Socks sub) · `Definitive-v29.html` · Compare `Compare-v24-v28.html`  
**Copy/slogan deep inventory:** `planning/home-copy-v24.md`  
**Decisions:** BZ-017 (Roboto craft) · BZ-018 (copy OS) · BZ-019 (WORKING = v28→v29) · **BZ-020 type calm** (400 display · 700 CTAs)  
**Type:** WORKING updated in place to BZ-020 calm (aligned with SEO v30 / Collection v18).  
**Next mock pass:** layout/copy = new Definitive version — never overwrite WORKING/v28/v29 casually.  
**Updated:** 2026-07-24  

---

## Who does what

| Role | Owns |
|------|------|
| **Brian** | Architecture, Shopify allowlist, gut plan, section schema, QA |
| **Agent** | Code against WORKING + this entry only; no inventing extra sections |
| **Andrew** | Final keep/drop on optional lines (e.g. Knock Socks sub) |

**Theme rebuild:** allowlist only — do not port unused Dawn/stock sections.

---

## Hard rules (non-negotiable)

1. **One featured slogan per section** — never stack two Tier S headlines.
2. **Bodies must make a difference** — inventory differentiators only. Ban bland filler (molded/360/Made in USA/$74 stacks as the whole body).
3. **Pose slip → solution** — name real moves (chair pose, flat back chair, water ski, footwork, lunges).
4. **Reviews on Home** — quote-led; **no** aggregate score / review count.
5. **Product naming** — Performance Skin / grippy shoes — not sneakers.
6. **Every media section** — image **or** video capable (settings).
7. **Every section** — stars/trust line **on/off** (settings).
8. **Coperni / campaign** — reusable stage + side-by-side grid (not Coperni-only forever).
9. **Type** — Roboto craft (BZ-017); Coperni = Syne + Cormorant only.
10. **New versions only** — never overwrite WORKING or prior Definitives.

---

## WORKING sequence (v29) — current lock

| # | Section | Featured slogan | Difference body / notes | Status |
|---|---------|-----------------|-------------------------|--------|
| 0 | Trust strip + nav | — | Buy 2 / shipping / returns chrome | **Built → refine** (theme chrome) |
| 1 | Hero | The Pilates Sock Era Is Over | Most Grippy… Outperforming Barre/Pilates/Yoga Socks — Combined! · stars · Shop Now · #hashtag | **Built → update** (image\|video) |
| 2 | Visual mosaic (multi-square) | Secure in Every Hold | CTA Shop Now; small tiles Stability/Balance/Durability/Breathability | **Built → refine/simplify** |
| 3 | Disciplines | Upgrade your grip. Upgrade your workout. | Discipline list under | **Built → light refine** |
| 4 | Shop / variants | Shop all colors & styles | Grip shoes for Barre, Pilates, Yoga—Secure in Every Hold. No Slipping. No Resets. | **Built → update** (live stock/URLs) |
| 5 | Never Loses 50/50 | Never Loses Shape. Never Loses Grip. | Built to hold when it matters most—push deeper, stay longer, move with confidence. | **Built → update** (image\|video) |
| 6 | Campaign (Coperni) | Built for the body in motion. | Stage video + 2×2 grid · seasonal toggle | **Built → generalize** as campaign module |
| 7 | Knock Socks | Let Us Knock Your Socks Off | *Optional sub:* Safely push harder in every studio move. (v29 on; v28 off) | **Built** |
| 8 | Commit full-bleed | You Commit to the Class. Commit to the Gear. | Shop Now | **Built → update** (image\|video) |
| 9 | Reviews (Judge.me) | Real people. Real results. | See the difference. Feel the grip. · See all reviews → | **Built → wire Judge.me** |
| 10 | Hot Kits | Hot Pilates & Yoga Kits | Coming soon · **data-enabled=false** | **Built, off** |
| 11 | One Pair | One Pair. Done. | Smarter than grip socks. Lightweight, flexible, 100% traction… | **Built → refine** |
| 12 | Problem | Never Slip in Chair Pose | Never slip again in side plank or flat back chair… + pose list | **Built** |
| 13 | Instagram | From the studio | @barreletics · static grid or Juicer | **Built → refine** (Juicer optional) |
| 14 | Guarantee | Zero risk. All grip. | Shipping / 30-day / 90-day / Made in USA | **Built** |
| 15 | Studio trust | Trusted by 1,000's of instructors & studios. | Dig into deep lunges… | **Built** (GEO accordion retired unless Brian re-locks) |
| 16 | Footer + newsletter | 10% off your first pair | — | **Built → light update** |

---

## Build / refine / change matrix

### TO BUILD (capabilities — not new sequence slots)

| ID | What | Spec |
|----|------|------|
| `hero-media` | Hero media image \| video | Poster + muted loop; same copy stack |
| `hero-fullbleed` | Optional full-bleed hero | Off by default; available |
| `section-stars` | Stars/trust on/off every section | Setting per section |
| `section-media` | Image \| video on every media block | Never Loses, Commit, mosaic tiles, campaign |
| `campaign-stage` | Full-bleed runway video/image + overlay | Generalized from Coperni |
| `campaign-grid` | 2×2 side-by-side tiles | Reusable anytime |
| `campaign-bundle` | Stage + grid one section | Coperni = first instance |
| Judge.me Home | Quote carousel or featured + See all | No aggregate count on Home |
| Juicer optional | Grid or slider auto-rotate | Prefer refined static; slider if auto-change wanted |

### TO REFINE (already in WORKING)

| Section | Refine what |
|---------|-------------|
| Mosaic | Simplify overlays/type; fewer competing labels |
| Variants | Live products, badges, sold-out; keep shop Secure line |
| Reviews | Real Judge.me quotes; title stays Real people… |
| IG | Title From the studio; Juicer vs static decision |
| One Pair | Keep punch; sock-math accurate |
| Type/spacing | Roboto craft already; mosaic/shop polish |
| Knock Socks sub | Owner keep-or-drop (*Safely push harder…*) |

### TO CHANGE (vs live / old freeze)

| Change | From → To |
|--------|-----------|
| Hero H1 | Live “A new kind of grip sock” → **Sock Era** |
| Problem | Live scattered → **Never Slip in Chair Pose** late |
| Reviews title | Live “Let customers speak” → **Real people. Real results.** |
| IG title | Was Real people… → **From the studio** |
| Shop head | Lock **live Secure shop line** |
| GEO accordion | → Studio trust line (unless SEO requires accordion) |
| Value-strip checklist | Removed from Home spine |
| Mid-page repeat stars | Off (hero owns stars; section toggle available) |
| Frozen `specs/frozen/homepage.md` | Stale — update to match WORKING |

---

## Shopify / theme allowlist (Home)

**Ship:** announcement/trust · header · hero · mosaic · disciplines · variant-grid · fifty-fifty (Never Loses, One Pair) · campaign-collab · statement-band · fullbleed-commit · social-proof/reviews · ugc/ig · guarantee · studio-trust · footer/newsletter · hot-kits (off)

**Do not ship on Home:** Juicer infinite-by-default · GEO accordion (unless re-locked) · slogan-soup ALL CAPS stacks · aggregate review counts · unused Dawn sections

---

## WORKING copy map (exact)

| Section | Featured | Body / sub |
|---------|----------|------------|
| Hero | The Pilates Sock Era Is Over | The Most Grippy Shoes on the Planet—Outperforming Barre Socks, Pilates Socks, Yoga Socks —Combined! |
| Mosaic | Secure in Every Hold | — |
| Disciplines | Upgrade your grip. Upgrade your workout. | Barre · Reformer · Megaformer · Lagree · Pilates · Yoga |
| Shop | Shop all colors & styles | Grip shoes for Barre, Pilates, Yoga—Secure in Every Hold. No Slipping. No Resets. |
| Never Loses | Never Loses Shape. Never Loses Grip. | Built to hold when it matters most—so you can push deeper, stay longer, and move with confidence. |
| Knock Socks | Let Us Knock Your Socks Off | Safely push harder in every studio move. *(optional)* |
| Commit | You Commit to the Class. Commit to the Gear. | — |
| Reviews | Real people. Real results. | See the difference. Feel the grip. |
| One Pair | One Pair. Done. | Smarter than grip socks. Lightweight, flexible, 100% traction—no replacing every month. |
| Problem | Never Slip in Chair Pose | Never slip again in side plank or flat back chair. Try that in a barre grip sock. |
| IG | From the studio | @barreletics |
| Guarantee | Zero risk. All grip. | Returns, warranty, and shipping that match the gear. |

---

## BEST OF — strongest statements (use these)

### Tier S — Home spine

1. Secure in Every Hold. No Sliding. No Resets.  
2. Shop all colors & styles + Grip shoes for Barre, Pilates, Yoga—Secure in Every Hold…  
3. The Pilates Sock Era Is Over  
4. Never Slip in Chair Pose (+ flat back chair, water ski, footwork, lunges)  
5. Never Loses Shape. Never Loses Grip.  
6. Let Us Knock Your Socks Off · Safely push harder in every studio move. *(sub optional)*  
7. We Outgrew Grip Socks. *(alt surfaces; not current Problem H2)*  
8. One Pair. Done.  
9. You Commit to the Class. Commit to the Gear.  
10. The Most Grippy Shoes on the Planet—Outperforming Barre Socks, Pilates Socks, Yoga Socks —Combined! *(hero body)*  
11. Real people. Real results.  
12. Zero risk. All grip.  
13. Upgrade your grip. Upgrade your workout.  
14. Built to hold when it matters most—so you can push deeper, stay longer, and move with confidence.

### Tier A — accent / support (not second H2)

- Think Outside the Sock  
- Tired Of Slipping in Your Yoga Socks?  
- Smarter than grip socks.  
- See the difference. Feel the grip.  
- The open-toe design mimics barefoot freedom while ensuring total control—smarter than grip socks.  
- Lightweight and flexible, delivering 100% traction, balance & stability.  
- FOCUS ON YOUR PRACTICE / cool on your feet… dig into deep lunges…  
- Never slip again in side plank or flat back chair…  
- Trusted by 1,000's of instructors & studios  
- #letusknockyoursocksoff  

### Tier B — skip on Home

- A new kind of grip sock!  
- Precision, Performance, Perfection  
- Increase Strength / Focus On Your Workout *(apparel)*  
- Join the Movement / Unleash Your Best Workout *(soft vs Tier S)*  
- Experience Anti-Slip *(vague vs Secure / Chair Pose)*  
- Bland filler bodies (see hard rules)

### Full inventory + pose tables

See **`planning/home-copy-v24.md`** for the complete owner/live paste inventory, pose→slip→solution table, and caution (medical) lines.

---

## Module settings (every section)

| Setting | Values | Default |
|---------|--------|---------|
| `stars_enabled` | true / false | true on hero; false elsewhere unless set |
| `media_type` | image / video | image (hero, Never Loses, Commit, mosaic cells) |
| `media_image` | URL | — |
| `media_video` | URL | — |
| `media_poster` | URL | — |
| `enabled` | true / false | campaign/hot-kits use `data-enabled` |

---

## Agent instructions (checklist)

When working on Home:

1. Open **WORKING** mock + this entry.  
2. Read `home-copy-v24.md` before writing slogans.  
3. New visual pass → **v30+** file; update WORKING only when Andrew says “make this working.”  
4. One slogan per section; bodies from Tier S/A difference list.  
5. Do not reintroduce aggregate review counts or mid-page star spam.  
6. Do not ask Andrew to re-paste the slogan inventory.  
7. Theme work: allowlist only; Brian owns gut architecture.

---

## Preview URLs (local)

- WORKING: `http://127.0.0.1:8766/Barreletics%20Home%20-%20Definitive-WORKING.html`  
- v28 (no Knock sub): `…/Definitive-v28.html`  
- v29: `…/Definitive-v29.html`  
- Compare v24↔v28: `…/Compare-v24-v28.html`  

---

## Open decisions (Brian / Andrew)

- [ ] Knock Socks sub keep or drop  
- [ ] Juicer slider vs static IG grid  
- [ ] Judge.me carousel vs featured + See all  
- [ ] GEO accordion required for SEO?  
- [ ] Update `specs/frozen/homepage.md` to WORKING  
- [ ] Theme repo path + section file names finalize  
