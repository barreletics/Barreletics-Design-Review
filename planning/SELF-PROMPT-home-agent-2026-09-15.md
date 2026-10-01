# SELF-PROMPT — Home / draft agent turns (Andrew reusable)

**Paste at the top of every Home / layout / Interni / fullbleed turn.**  
Draft only: `187144929571`. Never live. Never publish.

## One-pass rules

1. **Name the section family first** (fifty-fifty / press-feature / collab / fullbleed / statement / reviews / problem). Apply **only** that family’s ruler.
2. **One ticket = one family.** Do not “while you’re there” edit neighbors.
3. **Never thrash unrelated sections.** Editing Interni ≠ touch fullbleed / Grip / One Pair. Editing fullbleed ≠ touch Interni / Grip / One Pair.
4. **Never revert FF locks.** Grip + One Pair stay COVER · desk **860** · phone **520/520** · pads **32/32** center · body **16** · scale **100**. FIT forbidden on Home fifty-fifty.
5. **Never invent overlay copy.** If the image is meant to stand alone, leave it alone.
6. **Never restore overlay / copy / settings from an old punch-list or commit** without **explicit Andrew go** in *this* message.
7. **Pull-verify after push.** Then visual prove the family you touched — not just FF measure JSON.

## Locked surfaces (do not “fix” casually)

| Surface | Lock |
| --- | --- |
| `fifty-fifty-grip` / `fifty-fifty-one-pair` | COVER 860/520 · 32/32 · body 16 — **hands off** unless Andrew names them |
| `fullbleed-statement` | **IMAGE-ONLY** · `show_text: false` · blank title/body/cta · `mobile_full_bleed: true` (~52vh) · Commit+Shop CTA **on the image REJECTED 2026-09-15** |
| `press-feature-interni` | Chat editorial only · no Commit strings · leave Chat PNG alone unless Commit is baked in |
| PDP `fifty_fifty_lifestyle` | 560/550 — separate family — do not unify with Home |

## Forbidden moves

- Re-adding “You commit to the class…” / Shop Now / Shop All onto the fullbleed image
- Baking Commit copy into Interni (or any) PNG
- Converting Interni ↔ fifty-fifty types just to share a frame
- Whole-theme push / live theme / publish
- Using myshopify preview URLs (301 drops cookie) — use `https://barreletics.com/…?preview_theme_id=187144929571`

## Prove list (no “done” without)

- [ ] Named family + only that family’s files changed (diff proof)
- [ ] Grip / One Pair hashes or measure unchanged if not in ticket
- [ ] If fullbleed touched: `show_text === false` and title/cta blank in pulled `index.json`
- [ ] If Interni touched: no Commit phrases; Chat editorial asset kept unless Andrew swaps
- [ ] `shopify theme push --theme 187144929571 --only <files>` then `theme pull --only` match
- [ ] Screenshot / measure @390 (and desk if layout) of **touched** section
- [ ] `python3 scripts/lock-scan.py .` → `page_layout_os` OK
- [ ] Commit message states root cause + what was *not* touched

## Root-cause memory (2026-09-15)

Punch-list P0 said “restore Commit overlay” because title/cta were blank while `show_text` was true. That restore (`71200de`) put **Commit + Shop Now on the coral fullbleed image**. Andrew rejected it: text must **not** sit on that image. Correct state = **image-only** (`show_text false`, blank copy). Do not thrash Interni or FF when fixing fullbleed.

## Preview

Home draft: https://barreletics.com/?preview_theme_id=187144929571  
Letter: `planning/locks/PAGE-LAYOUT-OS-LOCKED.md`  
Scan: `planning/locks/sitewide.lock.json` → `page_layout_os.fullbleed_guidance`
