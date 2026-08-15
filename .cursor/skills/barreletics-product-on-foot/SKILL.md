---
name: barreletics-product-on-foot
description: >-
  Composite the real Barreletics Performance Skin onto feet by copying website
  on-foot photos only. Use when putting the shoe on a lifestyle shot, Sock Math
  photos, ChatGPT studio feet, “add the shoe,” Closed/Open on-foot, or any
  generated product-on-foot image. Never invent a new shoe from a packshot.
---

# Barreletics product on a foot

Andrew 2026-08-15: *look at pictures on the website with the shoe on a foot and just copy that.*

Empty packshots lie. Agents invent sneakers, extra straps, melted cages. **Worn site photos are the only shoe reference.**

## Fail closed

- Do **not** invent a shoe.
- Do **not** use `A14_TopBottom_*` / `Outside_Black` as the only shoe ref.
- Do **not** ship a composite Andrew would call “on drugs.”
- If the output does not match a worn site photo → delete it. Try once more. Then stop.

Copy law still applies in any caption: Closed Sole = *heel and foot fully covered.* Never “fully enclosed.”

## Worn refs (download these, then look)

| File | URL | Why |
|---|---|---|
| Yellow / blue on foot | `https://barreletics.com/cdn/shop/products/Yellow_Image-Blue_Shoe_1200x1200_59ef7b79-1661-4c2f-a2da-c6b9211e2c42.jpg` | Best 3/4. Blue skin on a real foot. |
| P5A7000 coral | `https://cdn.shopify.com/s/files/1/0045/0612/4391/files/P5A7000_blue_background_2.jpg` | Coral on a real foot. Blue backdrop. |
| IMG_2917 | `https://barreletics.com/cdn/shop/files/IMG_2917.jpg` | Coral on a real foot. Maroon backdrop. |
| Stef run | `https://barreletics.com/cdn/shop/products/barreletixxstefrunningpinkbackground.jpg` | Blue on foot, full body, stride. |
| Jumping | `https://barreletics.com/cdn/shop/products/barreletixxjumpingtogether.jpg` | Coral on two pairs of pointed feet. |
| Customer gray | `https://review-images.judgeme.com/barreletics/1774226614__img_9682__original.jpeg` | Gray on both feet, yoga mat, top view. |
| Customer rose | `https://review-images.judgeme.com/barreletics/1778161226__9063__original.jpg` | Dusty rose on dark skin, wood, top view. |

Local copies (if present): `docs/sock-math-photos/on-foot/`

**Do not use as on-foot truth:** `IMG_2704` (hands holding product), mesh-bag reviews, empty `Multi_Image` lineup, Open keep shots (`IMG_5051`, `IMG_3158`, `Square_Pink`) unless Andrew names Open.

## What the worn shoe actually looks like

Copy this geometry. Do not “improve” it.

- One-piece thin molded polymer. Second skin. Not a sneaker. Not a sock.
- Heel cup / heel wrap. Small **white asterisk / dragonfly** on the outer heel.
- Geometric cutouts on the instep (usually a center opening + side openings).
- Band across the ball of the foot. Toes often show at the front.
- Thin sole that follows the foot. Sits **flush** on skin — no floating straps, no melted edges.
- Five toes. Normal ankle. No extra limbs.

Color = the worn ref you picked (coral, blue, gray, dusty rose). Recolor only if Andrew names a color **and** you keep this geometry.

## Workflow

1. Download 2 worn refs in the color you will use. **Read them.**
2. Generate with references in this order:
   1. lifestyle / barefoot scene (locked)
   2. worn on-foot #1
   3. worn on-foot #2 (same product, same color if possible)
3. Use the prompt below. Do not add packshots unless a third ref is a **worn** 3/4.
4. Read the output. Compare to the worn refs.
5. Kill it if: extra toes, melted straps, sneaker tongue, random lattice, shoe growing out of skin, Open cage when the job is Closed and Andrew said copy site photos but the result is a new design.
6. Put survivors on the mock. Do not push Shopify until Andrew names a theme ID.

## Prompt (paste, then only swap color + scene notes)

```
Copy the Barreletics Performance Skin EXACTLY as it is worn in the website photos (images 2 and 3). Do not redesign.

Image 1 is the locked scene. Do not change camera, crop, lighting, body, clothes, or studio. Replace only the bare feet.

The shoe must match the worn photos:
- same thin molded polymer
- same heel wrap and small white asterisk logo on the outer heel
- same geometric cutouts, same count, same shapes
- same band across the ball of the foot
- same toe opening
- flush on the skin, not floating, not melted
- five toes, normal anatomy

Color: [coral | blue | gray | dusty rose] matching the worn photos.
No sneaker. No extra straps. No invented lattice. No socks.
```

## After a miss

Andrew already rejected two invented sets. Next miss → stop generating. Ask which worn site photo to copy more closely. Do not keep rolling dice.
