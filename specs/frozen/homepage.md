# Frozen Spec — Homepage

---
status: FROZEN
surface: Homepage (`/`)
authority: July 17 Home APPROVED + Decision Packet DP-01–DP-12 (PR #17 defaults)
tokens: v49 (palette, type, spacing, components)
updated: 2026-07-20
---

## Applied decisions
| ID | Choice |
|----|--------|
| DP-01 | Hero A — “The Pilates Sock Era Is Over” (`hero.liquid`, not `hero-alt`) |
| DP-02 | July 17 composition authority; v49 = tokens/components only |
| DP-03 | Keep Home GEO accordion |
| DP-08 | Coperni = seasonal module (removable when campaign ends) |
| DP-09 | Home Instagram / UGC band |
| DP-10 | Shared `value-strip` (no forced 6-pillars) |
| DP-11 | Defer Founder Letter / Manifesto / full dark Sock Math (Sock Math lite OK) |
| DP-12 | `planning/06` patched to match this stack |

## Approved section list (conversion spine)
1. Announcement strip + header nav (chrome)
2. **Hero** — ★★★★★ trust top; Sock Era H1; rust + outline CTAs; live lifestyle image
3. **Problem** — H2 + Yoga Socks Are Useless. + body + list + Shop (no THE FIX / no extra closers)
4. Disciplines → **Variant grid** (no lineup placeholder) → Editorial → Grip video 50/50 → Coperni one 50/50 → Full-bleed one line → Reviews → Sock Math → IG (6) → Guarantee → GEO → Footer
4. **Disciplines** proof
5. **Value strip** (shared)
6. **Variant grid** (Closed/Open + quick-add)
7. **Fifty-fifty — grip** (“Upgrade Your Grip. Upgrade Your Workout.”)
8. **Coperni** seasonal fifty-fifty (toggle off when campaign ends)
9. **Statement band** — commit full-bleed (“You Commit to the Class…”)
10. **Social proof** reviews
11. **Sock Math lite** (“One Pair. Done.”)
12. **Instagram / UGC** band
13. **Guarantee** — “Zero risk. All grip.”
14. **GEO** accordion (D-022)
15. **Newsletter**

## Messaging (slogan decisions)
| Placement | Line | Decision |
|-----------|------|----------|
| Hero trust | ★★★★★ Trusted by 1,000's of athletes | **Ship** (top of hero copy, live-site pattern) |
| Hero H1 | The Pilates Sock Era Is Over | **Keep** |
| Hero CTAs | Rust Shop Now + outline See Why | **Ship** (both, live-site pattern) |
| Problem H2 | Tired of slipping in your yoga socks? | **Ship** (only slogan in section) |
| Problem close | Shop Now (rust) | **Ship** — “Yoga Socks Are Useless” / One Pair. Done. live elsewhere (PDP / Sock Math) |
| Grip 50/50 | Upgrade Your Grip. Upgrade Your Workout. | **Keep** |
| Coperni | Barreletics × Coperni / Built for the body in motion | **Keep** (seasonal) |
| Statement | You Commit to the Class. Commit to the Gear. | **Keep** |
| Sock Math | One Pair. Done. | **Keep** (lite) |
| Guarantee | Zero risk. All grip. | **Keep** (July 17) |
| UGC | @barreletics / Follow the Movement | **Keep** |

## Matrix audit (Section Decision Matrix Jul 2026)
| Matrix § | Include on Home | Skip + why |
|----------|-----------------|------------|
| 01 Hero | **Yes** — Hero A | — |
| 03 50/50 Progress | No | Absorbed into grip / statement; avoid duplicate editorial |
| 04 Coperni + FP | **Yes** — seasonal lite | Full FP partner sprawl held (D-042 partners page) |
| 06 Credibility | **Yes** — value-strip + guarantee | — |
| 07 Trust & proof | **Yes** — reviews | — |
| 08 Disciplines | **Yes** | — |
| 09 The problem | **Yes** — early after hero | — |
| 10 Brand & conversion | **Yes** — statement band | — |
| 12 / 14 Variants | **Yes** — one grid (12) | Skip 14 duplicate v2 |
| 13 Conversion | **Yes** — reviews + CTAs | — |
| 15 v28 original | No | Legacy |
| 17 Never slip in chair pose | No | Move names live in disciplines/GEO; no dedicated band |
| 18 Promo tiles | No | Seasonal handled by Coperni module |
| 19 Sock math | **Yes** — lite only | Full dark 6-cell → PDP (DP-11) |
| 20 Never loses grip | **Yes** — grip fifty-fifty | — |
| 21 Push harder | No | PDP/motion territory |
| 23–24 Video & content | No on Home as dedicated | Grip 50/50 carries video; avoid content sprawl |
| 25 Coperni collab (full) | No | Use seasonal lite (04), not full video split |
| 26 Content 3 / UGC | **Yes** — home-ugc | — |
| 27 SEO section | **Yes** — GEO | — |
| 28 Conv support | **Yes** — guarantee | — |
| 29 Final CTA | **Yes** — newsletter (+ guarantee CTA) | — |
| Footer variants | Theme footer (standard) | Dark/minimal not Home-specific |

## Critical includes
- Hero Concept A; problem early; GEO; value-strip; variant-grid; statement band; guarantee; announcement in theme layout
- **Videos:** every `<video>` must autoplay muted (`muted` + `autoplay` + `loop` + `playsinline`; harden via JS `muted`/`defaultMuted` for Firefox) — see July 17 Home mockup comment + mute script

## Deferred Optionals
- Rotating 5-message eyebrow; dedicated 6-pillar strip; full dark Sock Math; Founder/Manifesto/Closing (About); hero video above fold; promo tiles; full Coperni video split
