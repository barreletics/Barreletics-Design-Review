---
name: barreletics-product-on-foot
description: >-
  Composite the real Barreletics Performance Skin onto feet by copying website
  close-ups of the shoe already on a foot. Use when adding the shoe to a lifestyle
  shot, Sock Math photos, ChatGPT studio feet, or any product-on-foot generate.
  Never invent a shoe. Never use an empty packshot as the only ref.
---

# Barreletics product on a foot

Andrew 2026-08-15: *look at existing images on feet. there are plenty of close ups.*

**Read the close-ups in `refs/` before you generate. Those files are the product.**

## Fail closed

- Do **not** invent a shoe.
- Do **not** use `A14_TopBottom_*` / `Outside_Black` as the only shoe ref.
- Do **not** feed a previous generated attempt as a shoe ref (it drifts).
- If it does not match `refs/closeup-coral-putting-on.jpg` geometry → delete. One retry. Then stop.
- **Too many holes = fail.** The real shoe is simple: toe band + **three** top openings + heel wrap. A busy lattice / extra side windows is a miss.

## Mandatory close-ups (in this skill)

Look at these files. Do not skip.

| File | What it is |
|---|---|
| `refs/closeup-coral-putting-on.jpg` | Homepage. Both feet. Hands putting coral on. **Best geometry.** |
| `refs/closeup-coral-held.jpg` | P5A7000. Coral on a pointed foot, blue backdrop. |
| `refs/closeup-blue-held.jpg` | Yellow backdrop. Blue on a pointed foot. |
| `refs/closeup-rose-customer.jpg` | Judge.me. Dusty rose on dark skin, top view. |
| `refs/closeup-gray-customer.jpg` | Judge.me. Gray on both feet, yoga mat, top view. |

CDN if you need a fresh download:

- `https://cdn.shopify.com/s/files/1/0045/0612/4391/files/65797B34-D7D3-41DE-A279-F3779BBFB06C.jpg`
- `https://cdn.shopify.com/s/files/1/0045/0612/4391/files/P5A7000_blue_background_2.jpg`
- `https://barreletics.com/cdn/shop/products/Yellow_Image-Blue_Shoe_1200x1200_59ef7b79-1661-4c2f-a2da-c6b9211e2c42.jpg`
- `https://review-images.judgeme.com/barreletics/1778161226__9063__original.jpg`
- `https://review-images.judgeme.com/barreletics/1774226614__img_9682__original.jpeg`

## Exact geometry (copy, do not improve)

From `closeup-coral-putting-on.jpg` and the customer top-views:

1. **Toe band** — one horizontal band across the base of the toes. Toes stick out the front. Not a flip-flop thong. Not a closed sneaker toe.
2. **Top of foot** — **only three** openings: one center + one on each side. That is the whole pattern. No extra lattice. No extra side windows. No cage of many holes.
3. **Heel** — a wrap from the midfoot around the back of the heel. Small **white asterisk / dragonfly** on the outer heel.
4. **Material** — one-piece thin matte polymer. Flush on skin. Sharp edges. Not melted. Not a sock. Not a sneaker.
5. **Anatomy** — five toes. Normal ankle. No extra fingers.

Color = the close-up you picked (coral, blue, dusty rose, gray).

## Workflow

1. **Read** the matching close-up(s) in `refs/`.
2. Generate with refs in this order only:
   1. locked lifestyle / barefoot scene
   2. close-up #1 (same color)
   3. close-up #2 (same product family)
3. Prompt below. Do not add packshots. Do not add prior generates.
4. Compare output to the close-up. Kill if cutout count is wrong, thong appears, or edges melt.
5. Mock only. No Shopify push until Andrew names a theme ID.

## Prompt

```
Copy the Barreletics Performance Skin from the website close-ups (images 2 and 3). Do not redesign.

Image 1 is the locked scene. Do not change camera, crop, lighting, body, clothes, or studio. Replace only the bare feet.

Exact geometry from the close-ups:
- one band across the base of the toes; toes visible in front
- THREE openings on top of the foot: center triangle + one each side
- heel wrap from midfoot around the back of the heel
- small white asterisk logo on the outer heel
- thin matte polymer, flush on skin, sharp edges
- five toes
- NO flip-flop thong, NO extra lattice, NO sneaker, NO socks

Color: [coral | blue | dusty rose | gray] matching the close-ups.
```

## After a miss

Stop. Ask which close-up to match. Do not keep rolling dice.
