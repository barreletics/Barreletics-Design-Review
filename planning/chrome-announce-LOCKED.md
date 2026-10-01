# LOCKED — Desktop chrome / announcement (2026-09-12)

**Status:** LOCKED · draft QA `187144929571` · Andrew: "done lock it in"  
**Mobile:** two-bar unchanged (sale + trust; logo_height_mobile **39**)  
**Do not thrash.** One-axis TE only if Andrew asks.

## Desktop layout
- **One cream announcement line** (SAVE2 + trust). Sale banner **hidden on desktop** via `chrome.css` (`.sale-banner-section` `display:none` ≥901px).
- Cream bg on announce only (`bg_color` cream). No border under announce; no border under cream sale (sale hidden desktop anyway).
- **🇺🇸 Made in USA** in trust messages.
- Nav: **centered** even group (`nav_distribute: center`) — not right-aligned, not edge-spread.

## Locked TE values (pulled from draft)
### Sale banner (mobile-visible; desktop CSS-hidden)
```json
{
  "enabled": true,
  "show_on_desktop": true,
  "show_on_mobile": true,
  "text": "Buy 2 save 10% | Use SAVE2",
  "link_url": "",
  "bg_color": "#faf8f6",
  "text_color": "#1c1916",
  "font_weight": "400",
  "font_size": 15,
  "pad_y": 10
}
```

### Announcement strip
```json
{
  "enabled": true,
  "font_size": 13,
  "pad_y": 9,
  "pad_x": 48,
  "item_gap": 12,
  "announce_distribute": "center",
  "letter_spacing": 3,
  "promo_weight": "700",
  "max_width": 1320,
  "bg_color": "#faf8f6",
  "text_color": "#5a544c",
  "promo_color": "#2e2a26",
  "rotation_speed": 4
}
```

### Header
```json
{
  "menu": "m4-menu",
  "help_menu": "help-menu",
  "show_help": true,
  "show_account": true,
  "show_cart": true,
  "show_action_labels": true,
  "logo_height": 56,
  "logo_height_mobile": 39,
  "sticky_header": true,
  "nav_link_size": "16",
  "nav_gap": 50,
  "nav_weight": "400",
  "action_link_size": "14",
  "action_gap": 16,
  "nav_distribute": "center",
  "header_max_width": 1320,
  "header_pad_y": 12,
  "header_pad_x": 48,
  "header_bg": "#ffffff",
  "header_text": "#4a4a4a"
}
```

### Announce messages
- Buy 2 save 10% · Use SAVE2
- 🇺🇸 Made in USA
- Free Shipping Over $150
- 30 Day Returns

## Files
- `assets/chrome.css` — desktop one-line / mobile two-bar rules
- `sections/header-group.json` — TE source of truth after pull
- `sections/header.liquid` · `announcement-strip.liquid` · `sale-banner.liquid` — TE knobs

## TE knobs (keep; don't remove)
Header: Nav layout · gap · size · weight · logo · pads · rail  
Sale: show desktop/mobile · size · weight · pad · colors  
Announcement: desktop + mobile size/pad/bg · message layout · item gap · promo weight

## Forbidden without Andrew yes
- Reintroduce desktop two-bar or blue SAVE2 bar
- Right-align / live-pack nav
- Edge-spread canyon nav
- Bold SAVE2/nav as default
- Overwrite TE via blind header-group push without pull-first
