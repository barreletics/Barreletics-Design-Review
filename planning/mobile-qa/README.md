# Mobile QA harness

Systematic mobile testing for the `docs/` mocks. Every section gets checked at a real
phone viewport before it is called done.

## Run it

```bash
python3 planning/mobile-qa/mqa.py                 # default page set at 390px + screenshots
python3 planning/mobile-qa/mqa.py --width 360     # small-Android spot check
python3 planning/mobile-qa/mqa.py --no-shots      # audit only, ~2x faster
python3 planning/mobile-qa/mqa.py --pages "Barreletics PDP - Definitive-v19.html"
```

Outputs land in `planning/mobile-qa/`:

- `findings-<width>px.json` — full machine-readable results
- `<page-slug>-<width>px.png` — full-page screenshot at a true phone width

The console line per page is the summary:

```
Barreletics PDP - Definitive-v19.html   vw=390 overflow=1(roots 1) tap<44=53 text<12=30 sticky=0 h=33287
```

**Always confirm `vw=` equals the width you asked for.** If it says 500, the harness is
broken and the results are meaningless.

## Why an iframe instead of `--window-size=390,900`

Headless Chrome on macOS clamps its window to a **500px minimum**. Asking for a 390px
window silently renders at 500px and merely crops the screenshot, which shows up as
phantom overflow on elements that are actually fine.

So the harness renders the target inside an `<iframe width="390">` in a 500px window.
The iframe gets a genuine 390px viewport. `--allow-file-access-from-files` (required)
lets the parent reach `iframe.contentDocument` and measure it, which means **target
pages are never modified** — important, since most of them are locked mocks.

Two passes run per page:

1. a 24000px-tall iframe so the whole page lays out and lazy media loads (overflow,
   tap targets, font sizes). Page height is read off the body box, since
   `documentElement.scrollHeight` just reports the tall iframe.
2. an 844px-tall iframe so sticky/fixed stacking is measured against a real phone.

## What it checks

| Check | Rule |
|---|---|
| Horizontal overflow | `getBoundingClientRect().right > clientWidth + 1` |
| Tap targets | `a`, `button`, `summary`, `input`, `select`, `[role=button]` under 44px tall |
| Small text | elements with their own text node rendering below 12px |
| Sticky stacking | every `position: sticky/fixed` box with its top/bottom/z-index/height |

Overflow is split into two buckets. Anything sitting inside an ancestor with
`overflow-x: auto/scroll/hidden/clip` is **contained** and reported separately, because
it cannot make the page scroll sideways. The walk deliberately stops before `<body>`:
`body { overflow-x: hidden }` is a page-wide band-aid that hides the scrollbar while
leaving content clipped, so those offenders still get reported as real.

`rootCause: true` marks an offender whose parent is not also overflowing — start there.
Also check `bodyOverflowX` and `scrollWidth`: `scrollWidth > vw` means the page really
does scroll sideways.

## Reading the results

11px text is the Type OS label scale (uppercase eyebrows) and is expected. Type OS is
SETTLED — do not "fix" it here. Genuine legibility problems show up at 8–9px.

Tap-target counts run high on every page because inline footer and nav text links are
short by design. Filter to `button` / `summary` / `input` for the actionable list.

Reports live alongside as `REPORT-<date>.md`.
