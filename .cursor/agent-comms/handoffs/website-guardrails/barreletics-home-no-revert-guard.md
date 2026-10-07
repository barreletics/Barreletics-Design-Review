---
name: Barreletics Home no-revert guard
description: >-
  use this before ANY Barreletics Home draft edit — no-revert locks for Grip/One
  Pair, reviews, Chat Interni, fullbleed image-only (no Commit overlay); one
  axis; no wholesale index.json; measure before done
---
# Barreletics Home no-revert guard

## When
Any Home / draft theme edit for Barreletics. Run before editing `index.json` or Home sections.

## Scope
Draft `187144929571` only. Never live. Never PDP.
Prefer preview: `https://barreletics.com/?preview_theme_id=187144929571`

## Locked (need exact section name + “go”)
- `fifty-fifty-grip` + `fifty-fifty-one-pair`: COVER, desk 860, mobile 520/520, pads 32/32, body 16, scale 100, centered
- Home reviews: 2 cards + See more only
- Interni art: Chat-supplied file only — do not remake/composite
- `fullbleed-statement`: **IMAGE-ONLY** — `show_text: false`, blank title/body/cta; NEVER put “You commit to the class” or Shop All/Now as overlay on that image (rejected 2026-09-15). Do not restore from old punch-list P0.

## Rules
1. One axis only — name the section id before editing
2. Never rewrite `index.json` wholesale (no full-template `json.dumps`)
3. After every push: pull-verify + measure the section you touched AND spot-check Grip/One Pair still 520
4. If a fix needs copy, ask — don’t restore from old commits
5. Say-done only with measured proof

## Compose with
Page layout OS · no-drift push gate · lock-scan
