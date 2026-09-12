# Frozen Spec — About / Our Story

---
status: FROZEN
surface: `/pages/our-story` · template `page.our-story.json`
mock: `docs/Barreletics Brand - Definitive-v25.html` · **LOCKED 2026-08-13**
updated: 2026-08-13
---

## Applied decisions

| Item | Choice |
|------|--------|
| Mock authority | **v25** — cream Joseph mat gallery · 2-col values · larger founder shots · white pull quote |
| Prior mock | v24 (black museum) · v26 white Joseph (not picked) |
| Mobile stack | **TE `mobile_stack_order`** on every `page-about-split` + `page-about-joseph` (+ sitewide `fifty-fifty` / heroes) |

## Approved section stack (Theme Editor order)

1. `page-about-hero` — cover jump photo
2. `page-about-intro` — Our story · lede · byline · pull quote (white)
3. `page-about-split` — founder (chair)
4. `page-about-split` — prototype (cream · reverse desktop)
5. `page-about-values` — What we stand for · 2×2 + 1 grid
6. `page-about-joseph` — cream mat gallery + essay
7. `page-about-facts` — Made in USA · 4-up
8. `page-about-split` — letter close (standing founder)
9. `geo-section` — Barreletics, in brief
10. `page-about-close` — dark shop CTA

Footer: sitewide `footer-group` (not in page template).

## TE controls per split section

- **Reverse layout** — desktop left/right only
- **Mobile stack order** — Image above copy \| Copy above image (768px and below)
- **Media column width** — desktop %
- **Media size caps** — desktop + mobile vh/px
- **Cream background** — toggle on splits

## Do not

- Revert to monolithic `page-about` text-only stack without Andrew letter
- Black `#111` Joseph museum band (v24 prior)
- Admin `product.description` on About (N/A here)
- Pool / fully enclosed / discipline sole split copy

## QA

- Draft theme **`187144929571`** — visual approve before production
- Repo = master · Shopify = QA runtime only
