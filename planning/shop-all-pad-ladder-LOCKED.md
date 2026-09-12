**SITEWIDE RULER (2026-09-12):** Shop All collection grid-open (72 desk / 56 phone) is the pad under nav for EVERY page that opens on `variant-grid`. Copy it — set `page_open_pad: true` on page templates. Do not invent.

# Shop All pad ladder LOCKED — 2026-09-12

**Token source:** `assets/design-tokens.css`

| Token | Desk | Phone |
|-------|------|-------|
| `--section-padding-y` | **32** | **24** |
| band = 2× token | **64** | **48** (features) / **64** (Upgrade) |
| `--section-padding-y-campaign` | **96** | **72** |
| mosaic tight (Home lock) | **16** | **16** |
| grid page-open top (no hero) | **72** | **56** |

## Section map
| Section | Vertical air | Notes |
|---------|----------------|-------|
| variant-grid | top 72/56, bottom token | liquid collection exception |
| upgrade-grip | pad_y **64/64** | cream |
| fifty-fifty-grip | section_gap **32/24** | white |
| fullbleed-commit | height 80vh | media breath |
| pdp-sock-math | pad **64/64** | cream editorial |
| fifty-fifty-disciplines | section_gap **32/24** | cream wrap after One pair |
| reviews | token | white |
| no-socks-features | **64/64** · mob **48/48** | white |
| in-use-mosaic | **16/16** | Home tile air |
| knock-socks | **96** (statement-band) | cream; no top border on collection |
| home-juicer | token | white |
| collection-faq | section default | cream |

Do not invent one-off gaps (no 40). Between 50/50s always 32/24.

## Fullbleed → One pair
After `fullbleed-commit`, sock-math `pad_top` = **32** (token between-section), not 64. Bottom stays 64.
