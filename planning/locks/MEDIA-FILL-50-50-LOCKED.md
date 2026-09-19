# MEDIA FILL · 50/50 LAW — LOCKED 2026-09-18

**Why this exists:** Never slip Chair Pose burned ~2h on a one-minute Cover/fill fix because we re-diagnosed the same class of bugs (padding inset, fixed clip height, `align-items: start`, CLI auth thrash) instead of opening a known card.

**Ruler:** Home `fifty-fifty` (One Pair / Grip) — COVER · desk **860** · phone **520** · media column full-bleed · stretch to row.

**Applies to:** Any Home/marketing split media+text that should match 50/50 fill (`fifty-fifty`, `problem-section` / Never slip with media, press enlargements that adopt the marketing split frame).

---

## Symptom → check → fix

| You see | Check | Fix (liquid only) |
|---|---|---|
| Cream/white **around** media (inset) | Section `padding` on the with-media state | `padding: 0` when `--with-media`; put pad on the **text** column only |
| White **above/below** media (letterbox) | `object-fit` / `--media-contain` / TE Media fit | COVER: `object-fit: cover` + absolute `inset: 0` on `video,img`; kill theme `video{height:auto}` with `height:100% !important` |
| Media shorter than text (white under media) | Clip `height`/`max-height` fixed; `align-items: start` | Grid `align-items: stretch`; `.media { height:100%; align-self:stretch }`; `.clip { position:absolute; inset:0 }` — **no fixed max-height on desk** |
| Left gutter / not edge-to-edge | Shell `max-width: 1100` wrapping media | With-media: shell full width; layout `width:100%`; media `left:0` |
| TE looks wrong, storefront OK | Theme Editor canvas lag / different asset | Measure **storefront preview**; TE media SoT is picker — never push `index.json` to “fix” fill |
| Push blocked / device codes | Box Shopify CLI session | Push from **Mac** CLI (`machineId`); don’t burn the axis on auth |

---

## Do / Don’t

**Do**
1. Name the family first (`fifty-fifty` vs problem-list).
2. Copy the 50/50 media law — don’t invent a third height/fill system.
3. One axis: fill only. Prove with measure (media rect = column rect, `object-fit: cover`, bottoms match text column).
4. Liquid-only; TE media SoT; no `templates/index.json` on control fixes.

**Don’t**
- `align-items: start` on a with-media split
- Fixed `max-height` on the desk media clip when text can grow
- Section padding around a full-bleed media column
- Re-open Cover vs Fit mid-axis without Andrew naming Fit
- Parallel agents on the same draft Home liquid

---

## Done gate (say-done)

- [ ] Media column left edge ≈ 0 (full-bleed)
- [ ] Media `getBoundingClientRect` matches column (≤2px)
- [ ] `object-fit: cover` (unless Andrew asked Fit/Contain)
- [ ] Media bottom matches text column bottom (row stretch)
- [ ] Desk min height ruler **860** unless Andrew set otherwise in TE
- [ ] No `index.json` push

**Commit baseline Never slip fill:** `bb1be68` + follow-up stretch/full-bleed 2026-09-18.
