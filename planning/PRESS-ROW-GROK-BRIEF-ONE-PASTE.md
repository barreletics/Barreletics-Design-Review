# Barreletics Home — Press row (one paste for Grok)

**Store:** barreletics · **Draft theme only:** `187144929571` (M4 QA) · **Do not push live.**

---

## What we want (approved direction)

**ONE section** on Home (above Juicer), not two stacked heroes.

**Desktop grid (single row, ~540px tall, max-width 1200px, bg `#faf8f6`):**

| Cell | Content |
|------|---------|
| Left column, spans 2 rows | Coperni runway **video** + overlay copy: label “Barreletics × Coperni”, line “Limited edition · Paris 2026” |
| Top-right | Runway still #1 → title “Runway”, caption “Paris Fashion Week” → link Coperni PDP |
| Top-right #2 | Runway still #2 → title “Collaboration”, caption “Spring–Summer 2026” → link Coperni PDP |
| Bottom-right | **INTERNI** magazine image (contain in cell, not heavy crop) → “Sano come un piede” → `/blogs/news/barreletics-in-interni` |
| Bottom-right #2 | **ITSLIQUID · Venice** (placeholder until art) → “Biennale arte 2026” → Journal |

**Card pattern:** white card, 1px border `#e8e4dc`, image area + footer with serif-style **title** (see fonts below) + muted caption + `→`.

**Mobile:** hero video full width, then 2×2 or stack of four cards.

**Visual reference (local mock, theme untouched):**  
`planning/PRESS-ROW-UNIFIED-MOCK-2026-09-22.html` — open via  
http://127.0.0.1:8847/PRESS-ROW-UNIFIED-MOCK-2026-09-22.html

---

## Typography (fix — current Grok build is wrong)

**Barreletics Type OS:** **`Roboto` only** for UI, labels, and headings (no Georgia on Home).

| Role | Font | Size / weight |
|------|------|----------------|
| Section title “Press” | Roboto | ~32px, weight **600** (h2-standard) |
| Card titles (INTERNI, Coperni, etc.) | Roboto | ~17–18px, weight **600** |
| Captions | Roboto | 12–13px, weight **400**, color `#6b645a` |
| Hero overlay label | Roboto | 11px, weight **600**, uppercase, letter-spacing 0.08em |
| Hero overlay line | Roboto | clamp ~24–34px, weight **500** (display), sentence case |

Do **not** use `font-family: Georgia, serif` (that’s in the current `recognition-split.liquid` and the old mock).

---

## What’s wrong today (Grok’s draft)

1. **Two sections on Home** — `recognition-before` + `recognition-after` in `templates/index.json` → double height, duplicate Coperni video + duplicate Interni story.
2. **Layout `coperni_rail`:** tiles still say “Limited edition” / product shots, not runway; rail has **two INTERNI** images, no Venice slot.
3. **Layout `interni_press`:** full Interni 50/50 **plus** 3 cards — repeats everything again.
4. **Fonts:** Georgia in section CSS — should be Roboto.

**Keep one section.** Drop the second from `order` or merge into one layout.

---

## Theme files (repo)

| File | Role |
|------|------|
| `shopify-build/sections/recognition-split.liquid` | Grok section: layouts `coperni_rail` \| `interni_press` |
| `shopify-build/templates/index.json` | Instances `recognition-before`, `recognition-after` |

**Assets already in JSON:**

- Video: `https://barreletics.com/cdn/shop/videos/c/vp/a91000a89fb04c70935becea5180b69e/a91000a89fb04c70935becea5180b69e.HD-1080p-7.2Mbps-43057645.mp4`
- Poster: `https://barreletics.com/cdn/shop/files/yellow_tone_mix.png?width=2000`
- Runway/product stills: `Screenshot_2026-03-20_at_6.53.30_PM.png`, `Copreni_Final_More_grey.png` (CDN under `/cdn/shop/files/…`)
- Interni: `Interni_Blog_Magazine_Page.png` on Shopify files CDN

---

## Target implementation (for Grok)

**Option A — extend `recognition-split.liquid`:** add layout `unified_press` (or rename) with grid:

```css
/* desktop */
.press-grid {
  display: grid;
  grid-template-columns: 1.08fr 0.46fr 0.46fr;
  grid-template-rows: 1fr 1fr;
  gap: 10px;
  height: clamp(440px, 52vw, 540px);
}
.hero { grid-row: 1 / 3; grid-column: 1; /* video cover */ }
/* four .press-card cells in remaining grid cells */
```

**Blocks in schema:** keep `tile` (×2 runway), `rail_image` or `card` (×2 press). Section settings: video, poster, stage eyebrow/title.

**Option B — new section `press-row.liquid`** matching mock HTML structure; one instance on Home.

**Home `order` (tail):** … `guarantee-band` → **`press-row`** (single) → `home-juicer`.

---

## Current Grok liquid (coperni_rail branch) — simplify toward one grid

```liquid
{% else %}
  <div class="recognition-split__stage">
    <div class="recognition-split__stage-video">…video…</div>
    <div class="recognition-split__tiles">{% for block type tile %}…{% endfor %}</div>
  </div>
  <div class="recognition-split__rail">{% for block type rail_image %}…{% endfor %}</div>
{% endif %}
```

**Replace** two-column “stage | rail” with **one CSS grid** (mock) so video spans left; four cards on right — not stage nested 1.4fr/0.7fr + separate rail column.

---

## Current index.json spine (wrong — two press sections)

```json
"order": [
  …,
  "guarantee-band",
  "recognition-before",
  "recognition-after",
  "home-juicer"
]
```

**Fix:** one id, e.g. `"press-home"`, type `recognition-split` with layout `unified_press` and blocks: 2× tile, 2× rail_image (Interni + Venice).

---

## Grok must not

- Push theme `185687998755` or live role
- Leave two recognition sections on Home
- Use Georgia for headings
- Duplicate Interni in two rail slots (use Interni + Venice)
- Re-add full-width collab hero + separate Interni carousel

---

## Done when

- [ ] One Press band on Home preview `187144929571`
- [ ] Roboto typography matches Type OS
- [ ] Video + 2 runway cards + Interni + Venice placeholder
- [ ] Mobile stack readable
- [ ] Juicer still last before footer

---

*End of brief — send this entire file to Grok.*
