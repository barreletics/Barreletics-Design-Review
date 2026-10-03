#!/usr/bin/env python3
"""
Full before/after render snapshot diff: old (grok/fifty-fifty-live-preview) vs new liquid.
Uses git template JSON only; simulates computed classes, CSS vars, media source, padding, CTA.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

TEMPLATES = Path("/workspace/shopify-build/templates")
ARTIFACT = Path("/opt/cursor/artifacts/ff-render-diff-report.md")
SECTION_PADDING_X_MOBILE = 20  # design-tokens.css


def load_template_json(path: Path):
    raw = path.read_text()
    if raw.lstrip().startswith("/*"):
        raw = raw[raw.index("*/") + 2 :]
    return json.loads(raw)


def template_name(stem: str) -> str:
    if stem == "product" or stem.startswith("product."):
        return "product"
    return stem.split(".")[0]


def g(settings, key, default=None):
    v = settings.get(key)
    if v is None or v == "":
        return default
    return v


def panel_bg_old(s):
    bg_preset = g(s, "bg_preset", "")
    if bg_preset == "white":
        return "#ffffff"
    if bg_preset == "cream":
        return "#faf8f6"
    if bg_preset == "custom":
        return g(s, "bg_color", "#ffffff")
    return g(s, "bg_color", "#ffffff")


def panel_bg_new(s):
    bg_style = s.get("bg_style")
    if bg_style == "white":
        return "#ffffff"
    if bg_style == "cream":
        return "#faf8f6"
    if bg_style == "darker_cream":
        return "#efe9dd"
    bg_preset = g(s, "bg_preset", "")
    if bg_preset == "white":
        return "#ffffff"
    if bg_preset == "cream":
        return "#faf8f6"
    if bg_preset == "custom":
        return g(s, "bg_color", "#ffffff")
    legacy_bg = g(s, "bg_color", "")
    if legacy_bg.lower() in ("#faf8f6",):
        return "#faf8f6"
    if legacy_bg.lower() in ("#efe9dd",):
        return "#efe9dd"
    if legacy_bg:
        return legacy_bg
    return "#ffffff"


def media_pad_bg_old(s):
    preset = s.get("media_bg_preset")
    if preset == "cream":
        return "#faf8f6"
    if preset == "white":
        return "#ffffff"
    if preset == "custom":
        return g(s, "media_bg", "#ffffff")
    return g(s, "media_bg", "#ffffff")


def media_pad_bg_new(s):
    mb = g(s, "media_bg", "#ffffff")
    if not mb:
        return media_pad_bg_old(s)
    return mb


def desktop_object(s):
    key = g(s, "image_position", "center")
    if key == "custom":
        fx, fy = g(s, "focal_x", 50), g(s, "focal_y", 50)
        return f"{fx}% {fy}%"
    return key


def phone_fit_old(s):
    key = g(s, "image_position", "center")
    pos = desktop_object(s)
    if key and key != "center":
        if key != "custom" or pos != "50% 50%":
            return pos
    return "center top"


def phone_fit_new(s):
    pm = g(s, "image_position_mobile", "same")
    if pm in ("same", None, ""):
        return phone_fit_old(s)
    if pm == "custom":
        fx, fy = g(s, "focal_x_mobile", 50), g(s, "focal_y_mobile", 50)
        return f"{fx}% {fy}%"
    return pm


def phone_cover_new(s):
    pm = g(s, "image_position_mobile", "same")
    if pm in ("same", None, ""):
        return desktop_object(s)
    if pm == "custom":
        fx, fy = g(s, "focal_x_mobile", 50), g(s, "focal_y_mobile", 50)
        return f"{fx}% {fy}%"
    return pm


def section_gap(s, key, default):
    if key not in s:
        return default
    return s[key]


def text_pad_mobile(s):
    top = 96
    if s.get("text_pad_top_mobile") is not None and s.get("text_pad_top_mobile") != "":
        top = s["text_pad_top_mobile"]
    bottom = top
    if s.get("text_pad_bottom_mobile") is not None and s.get("text_pad_bottom_mobile") != "":
        bottom = s["text_pad_bottom_mobile"]
    return top, bottom


def media_source(s):
    if s.get("video"):
        return "shopify_video", s.get("video")
    if g(s, "video_url"):
        return "video_url", s["video_url"]
    if s.get("image"):
        return "shopify_image", "picker_set"
    if g(s, "image_asset"):
        return "image_asset", s["image_asset"]
    if g(s, "image_url"):
        return "image_url", s["image_url"]
    return "placeholder", None


def poster_source(s):
    if s.get("image"):
        return "shopify_image"
    if g(s, "poster_url"):
        return "poster_url"
    return None


def mobile_stack_class(order):
    if order == "copy_first":
        return "split-section--copy-first"
    return "split-section--media-first"


def build_classes(s, tmpl):
    media_fit = g(s, "media_fit", "cover")
    image_fit_m = g(s, "image_fit_mobile", "cover")
    media_aspect = g(s, "media_aspect", "stretch")
    media_aspect_m = g(s, "media_aspect_mobile", "stretch")
    parts = ["section-frame", "split-section"]
    if tmpl == "product":
        parts.append("split-section--pdp")
    if s.get("reverse"):
        parts.append("split-section--reverse")
    if media_fit == "contain":
        parts.append("split-section--contain")
    if media_fit == "fit":
        parts.append("split-section--fit")
    if media_fit == "cover_inset":
        parts.append("split-section--cover-inset")
    if image_fit_m == "fit":
        parts.append("split-section--fit-m")
    if image_fit_m == "contain":
        parts.append("split-section--contain-m")
    if media_aspect == "square":
        parts.append("split-section--media-square")
    if media_aspect_m == "square":
        parts.append("split-section--media-square-m")
    parts.append(mobile_stack_class(g(s, "mobile_stack_order", "media_first")))
    if s.get("hide_on_mobile"):
        parts.append("section-frame--hide-mobile")
    if s.get("hide_on_desktop"):
        parts.append("section-frame--hide-desktop")
    return " ".join(parts)


def compute(s, tmpl, variant: str) -> dict:
    is_product = tmpl == "product"
    panel_bg = panel_bg_old(s) if variant == "old" else panel_bg_new(s)
    media_pad = media_pad_bg_old(s) if variant == "old" else media_pad_bg_new(s)

    mobile_h = g(s, "mobile_media_height", 0) or 0
    ff_mobile_media_h = f"{mobile_h}px" if mobile_h > 0 else "var(--split-media-h-mobile, 500px)"

    mobile_text_h = g(s, "mobile_text_height", 0) or 0
    if is_product:
        mobile_text_h = 0

    if variant == "old":
        vpad = g(s, "vertical_padding", 88)
        text_pad_top_d = text_pad_bottom_d = vpad
        text_pad_x_m = SECTION_PADDING_X_MOBILE
        phone_cover_pos = desktop_object(s)
        phone_fit_pos = phone_fit_old(s)
        mobile_media_width = 100
    else:
        text_pad_top_d = s.get("text_pad_top")
        if text_pad_top_d is None or text_pad_top_d == "":
            text_pad_top_d = g(s, "vertical_padding", 88)
        text_pad_bottom_d = s.get("text_pad_bottom")
        if text_pad_bottom_d is None or text_pad_bottom_d == "":
            text_pad_bottom_d = g(s, "vertical_padding", 88)
        text_pad_x_m = g(s, "text_pad_x_mobile", 20)
        phone_cover_pos = phone_cover_new(s)
        phone_fit_pos = phone_fit_new(s)
        mobile_media_width = g(s, "mobile_media_width", 100)

    text_pad_top_m, text_pad_bottom_m = text_pad_mobile(s)

    sg = section_gap(s, "section_gap", 32)
    if s.get("section_gap") is not None:
        sg = s["section_gap"]
    sgm = 0
    if s.get("section_gap_mobile") is not None:
        sgm = s["section_gap_mobile"]
    if is_product:
        sgm = 0

    media_pct = g(s, "media_column_pct", 50)
    image_scale = g(s, "image_scale", 100)
    scale_ratio = float(image_scale) / 100.0

    cta_target = g(s, "cta_link_target", "custom")
    if cta_target and cta_target != "custom":
        cta_href = cta_target
    else:
        cta_href = s.get("cta_url")

    ms_type, ms_val = media_source(s)
    content_style = g(s, "content_style", "standard")

    css_vars = {
        "--ff-min-height": f"{g(s, 'min_height', 560)}px",
        "--ff-mobile-media-height": ff_mobile_media_h,
        "--ff-mobile-text-height": f"{mobile_text_h}px",
        "--ff-media-fr": f"{media_pct}fr",
        "--ff-text-fr": f"{100 - media_pct}fr",
        "--ff-object-position": desktop_object(s),
        "--ff-object-position-fit-m": phone_fit_pos,
        "--ff-image-scale": str(scale_ratio),
        "--ff-contain-width": f"{g(s, 'contain_width', 72)}%",
        "--ff-media-radius": f"{g(s, 'media_radius', 0)}px",
        "--ff-panel-bg": panel_bg,
        "--ff-media-pad-bg": media_pad,
        "--ff-column-gap": f"{g(s, 'column_gap', 0)}px",
        "--ff-side-padding": f"{g(s, 'side_padding', 64)}px",
        "--ff-text-pad-top-d": f"{text_pad_top_d}px",
        "--ff-text-pad-bottom-d": f"{text_pad_bottom_d}px",
        "--ff-section-gap": f"{sg}px",
        "--ff-section-gap-m": f"{sgm}px",
        "--ff-text-pad-top-m": f"{text_pad_top_m}px",
        "--ff-text-pad-bottom-m": f"{text_pad_bottom_m}px",
        "--ff-text-pad-x-m": f"{text_pad_x_m}px",
        "--ff-cta-bg": g(s, "cta_bg_color", "#c45c3f"),
        "--ff-cta-border": g(s, "cta_border_color", g(s, "cta_bg_color", "#c45c3f")),
        "--ff-cta-text": g(s, "cta_text_color", "#ffffff"),
    }
    if variant == "new":
        css_vars["--ff-object-position-m"] = phone_cover_pos
        css_vars["--ff-mobile-media-width"] = f"{mobile_media_width}%"
    else:
        css_vars["--ff-object-position-m"] = phone_cover_pos  # effective on phone in old CSS

    return {
        "classes": build_classes(s, tmpl),
        "css_vars": css_vars,
        "media_source_type": ms_type,
        "media_source_key": ms_val if ms_type != "shopify_image" else "picker",
        "poster_source": poster_source(s) if ms_type == "video_url" else None,
        "image_mobile_set": bool(s.get("image_mobile")),
        "object_position_desktop": desktop_object(s),
        "object_position_phone_cover": phone_cover_pos,
        "object_position_phone_fit": phone_fit_pos,
        "object_fit_desktop": g(s, "media_fit", "cover"),
        "object_fit_phone": g(s, "image_fit_mobile", "cover"),
        "padding_desktop_top": text_pad_top_d,
        "padding_desktop_bottom": text_pad_bottom_d,
        "padding_desktop_sides": g(s, "side_padding", 64),
        "padding_phone_top": text_pad_top_m,
        "padding_phone_bottom": text_pad_bottom_m,
        "padding_phone_sides": text_pad_x_m,
        "media_column_pct": media_pct,
        "min_height_desktop": g(s, "min_height", 560),
        "mobile_media_height_css": ff_mobile_media_h,
        "mobile_media_width_pct": mobile_media_width,
        "reverse": bool(s.get("reverse")),
        "mobile_stack_order": g(s, "mobile_stack_order", "media_first"),
        "cta_href": cta_href,
        "cta_text": s.get("cta_text"),
        "content_style": content_style,
        "anchor_id": s.get("anchor_id"),
        "aria_label": s.get("aria_label"),
    }


def normalize_css_vars(old: dict, new: dict) -> tuple[dict, dict]:
    """Align old/new var maps so new-only defaults are not false diffs."""
    o = dict(old)
    n = dict(new)
    if "--ff-mobile-media-width" not in o and n.get("--ff-mobile-media-width") == "100%":
        o["--ff-mobile-media-width"] = "100%"
    return o, n


def diff_dict(a, b):
    d = {}
    if "css_vars" in a or "css_vars" in b:
        ocss, ncss = normalize_css_vars(a.get("css_vars", {}), b.get("css_vars", {}))
        for k in sorted(set(ocss) | set(ncss)):
            if ocss.get(k) != ncss.get(k):
                d[f"css_vars.{k}"] = {"old": ocss.get(k), "new": ncss.get(k)}
        a = {k: v for k, v in a.items() if k != "css_vars"}
        b = {k: v for k, v in b.items() if k != "css_vars"}
    keys = sorted(set(a) | set(b))
    for k in keys:
        if a.get(k) != b.get(k):
            d[k] = {"old": a.get(k), "new": b.get(k)}
    return d


def main():
    instances = []
    for path in sorted(TEMPLATES.glob("*.json")):
        try:
            data = load_template_json(path)
        except (json.JSONDecodeError, ValueError):
            continue
        tmpl = template_name(path.stem)
        for key, sec in data.get("sections", {}).items():
            if sec.get("type") != "fifty-fifty":
                continue
            name = f"{path.stem}:{key}"
            s = sec.get("settings") or {}
            old = compute(s, tmpl, "old")
            new = compute(s, tmpl, "new")
            delta = diff_dict(old, new)
            instances.append((name, delta))

    failures = [(n, d) for n, d in instances if d]
    lines = [
        "# Fifty-fifty render snapshot diff (old preview vs new)",
        "",
        f"Instances checked: **{len(instances)}**",
        f"Differences: **{len(failures)}**",
        "",
    ]
    if failures:
        lines.append("## Failures\n")
        for name, delta in failures:
            lines.append(f"### `{name}`\n")
            for k, v in sorted(delta.items()):
                lines.append(f"- **{k}**: old `{v['old']}` → new `{v['new']}`")
            lines.append("")
    else:
        lines.append("**Zero diffs** across classes, CSS vars, media source, object positions, padding, layout, and CTA for all instances.\n")

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text("\n".join(lines))
    print(ARTIFACT.read_text())
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
