---
name: add-section-background-control
description: >-
  Adds one Shopify color picker for a section or text-panel background after
  the user explicitly approves that section. Default equals the current rendered
  background. Zero intended visual change. Never auto-invoke for a site-wide
  pass. Use only when the user answers yes to “Add the standard background color
  control?” for the section being QCed.
---

# Add section background control

**Use only after** the user approves adding a background control on **this** section.  
If the user did not say yes for this section → stop.  
Companion: `.cursor/rules/qc-section-admin-preservation.mdc` · `te-user-state-sync.mdc`

Draft `187144929571` only. Never live `185687998755`.

## Do

- One normal Shopify `"type": "color"` picker on **this** section schema only
- Wire it only to the existing section or text-panel background
- `default` / Liquid fallback = the **exact hex that currently renders**
- Zero intended visual change when added
- Push liquid/CSS only (theme ID named in-message). Do not push template JSON to “save” the new color

## Do not

- Change typography, spacing, layout, CTA colors, stars, badges, images, media fills
- Alter existing color controls
- Convert pickers into dropdowns
- Edit template JSON merely to create a saved value (missing key → schema default)
- Add the control to other sections “while we’re here”
- Overwrite user-owned Theme Editor state

## Steps

1. Confirm the named section and the current rendered background (computed CSS / hardcoded hex / token).
2. Pull that page’s template from draft `187144929571` first if TE may have changed. Diff. Keep user-owned Theme Editor state.
3. Add the picker + wire it. Fallback = current hex.
4. Push **only** the section liquid (and CSS if required). One `--only` per file.
5. Verify on the draft:
   - looks identical before/after
   - picker changes only that background
   - previous TE choices intact
   - no unrelated JSON changed

If a pull/push would risk other settings → **STOP and tell the user**.
