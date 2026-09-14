#!/usr/bin/env python3
"""Scan Shopify templates against sitewide + page locks. Exit 1 if mismatches."""
from __future__ import annotations

import fnmatch
import json
import re
import sys
from pathlib import Path


def load_json(path: Path):
  t = path.read_text()
  if t.lstrip().startswith("/*"):
    t = re.sub(r"^/\*.*?\*/\s*", "", t, count=1, flags=re.S)
  return json.loads(t)


def title_of(sec):
  st = sec.get("settings") or {}
  return st.get("title") or st.get("headline") or st.get("heading") or ""


def feature_titles(sec):
  blocks = sec.get("blocks") or {}
  order = sec.get("block_order") or list(blocks.keys())
  out = []
  for bid in order:
    b = blocks.get(bid) or {}
    t = (b.get("settings") or {}).get("title")
    if t:
      out.append(t)
  return out


def scan_page_lock(lock: dict, build: Path):
  issues = []
  tmpl = build / lock["template"]
  if not tmpl.exists():
    return [f'MISSING template {lock["template"]}'], []
  data = load_json(tmpl)
  sections = data.get("sections") or {}
  order = data.get("order") or []
  visible = [k for k in order if not sections.get(k, {}).get("disabled")]

  for i, key in enumerate(lock.get("visible_spine") or []):
    if i >= len(visible) or visible[i] != key:
      got = visible[i] if i < len(visible) else "MISSING"
      issues.append(f"SPINE: expected #{i+1}={key}, got {got}")

  for key in lock.get("disabled_must") or []:
    if key in sections and not sections[key].get("disabled"):
      issues.append(f"DISABLED: {key} should be disabled")

  for key, expect in (lock.get("section_titles") or {}).items():
    sec = sections.get(key)
    if not sec or sec.get("disabled"):
      issues.append(f"TITLE: {key} missing/disabled")
      continue
    got = title_of(sec)
    if expect not in got and got not in expect:
      issues.append(f"TITLE: {key} expected contains {expect!r}, got {got!r}")

  feat_key = lock.get("features_section") or "no-socks-features"
  if lock.get("features_required") and feat_key in sections:
    got = feature_titles(sections[feat_key])
    for req in lock["features_required"]:
      if req not in got:
        issues.append(f"FEATURE missing: {req}")

  for path, expect in (lock.get("required_settings") or {}).items():
    sec_id, field = path.split(".", 1)
    sec = sections.get(sec_id) or {}
    got = (sec.get("settings") or {}).get(field)
    if got != expect:
      issues.append(f"SETTING: {path} expected {expect!r} (Shop All ruler), got {got!r}")

  for path, expect in (lock.get("pads") or {}).items():
    sec_id, field = path.split(".", 1)
    sec = sections.get(sec_id) or {}
    got = (sec.get("settings") or {}).get(field)
    if got != expect:
      issues.append(f"PAD: {path} expected {expect}, got {got}")

  for sec_id, expect in (lock.get("cream_bg") or {}).items():
    sec = sections.get(sec_id) or {}
    got = (sec.get("settings") or {}).get("bg_color") or (sec.get("settings") or {}).get("bg_class")
    if not got:
      continue
    if expect == "#faf8f6" and str(got) in ("cream", "#faf8f6", "#FAF8F6"):
      continue
    if str(got).lower() != str(expect).lower() and expect not in str(got):
      issues.append(f"BG: {sec_id} expected {expect}, got {got}")

  return issues, visible


def scan_sitewide(site: dict, build: Path, only: Path | None):
  issues = []
  cream = (site.get("tokens") or {}).get("cream", "#faf8f6")
  lifestyle = site.get("fifty_fifty_lifestyle") or {}
  forbid = set(site.get("forbidden_pad_values") or [])
  gb = site.get("guarantee_band") or {}
  apply_ff = lifestyle.get("applies_to_templates") or ["product*.json"]

  templates = sorted((build / "templates").glob("*.json"))
  if only:
    templates = [only] if only.exists() else []

  pad_keys = (
    "section_gap",
    "section_gap_mobile",
    "pad_top",
    "pad_bottom",
    "pad_top_mobile",
    "pad_bottom_mobile",
    "pad_y",
    "vertical_padding",
    "text_pad_top_mobile",
    "text_pad_bottom_mobile",
  )

  for tmpl in templates:
    try:
      data = load_json(tmpl)
    except Exception as e:
      issues.append(f"{tmpl.name}: JSON parse {e}")
      continue
    rel = f"templates/{tmpl.name}"
    ff_applies = any(fnmatch.fnmatch(tmpl.name, pat) for pat in apply_ff)

    for key, sec in (data.get("sections") or {}).items():
      if sec.get("disabled"):
        continue
      st = sec.get("settings") or {}
      stype = sec.get("type") or ""

      for pk in pad_keys:
        if pk in st and st[pk] in forbid:
          issues.append(f"{rel} {key}: forbidden pad {pk}={st[pk]}")

      if stype == "fifty-fifty" and ff_applies:
        fit = (st.get("image_fit_mobile") or st.get("image_fit") or "").lower()
        if "text_pad_top_mobile" in st and st["text_pad_top_mobile"] not in (None, ""):
          if st.get("text_pad_top_mobile") != lifestyle.get("text_pad_top_mobile"):
            issues.append(
              f"{rel} {key}: text_pad_top_mobile expected {lifestyle.get('text_pad_top_mobile')}, got {st.get('text_pad_top_mobile')}"
            )
        if "text_pad_bottom_mobile" in st and st["text_pad_bottom_mobile"] not in (None, ""):
          if st.get("text_pad_bottom_mobile") != lifestyle.get("text_pad_bottom_mobile"):
            issues.append(
              f"{rel} {key}: text_pad_bottom_mobile expected {lifestyle.get('text_pad_bottom_mobile')}, got {st.get('text_pad_bottom_mobile')}"
            )
        if "min_height" in st and st["min_height"] not in (None, "") and st.get("min_height") != 560:
          issues.append(f"{rel} {key}: min_height expected 560, got {st.get('min_height')}")
        if fit in ("cover", "") and "mobile_media_height" in st and st["mobile_media_height"] not in (None, ""):
          mmh = st["mobile_media_height"]
          # 550 lifestyle lock; 360 = known Chair Pose landscape exception; ~400 = packshot FIT frame
          if fit == "cover" and mmh not in (550, 360) and mmh != 550:
            issues.append(
              f"{rel} {key}: COVER mobile_media_height expected 550 (or locked exception), got {mmh}"
            )

      bg = st.get("bg_color")
      if isinstance(bg, str) and bg.lower() in ("#fafafa", "#f8f6f4", "#f7f5f2", "#fff8f0"):
        issues.append(f"{rel} {key}: cream should be {cream}, got {bg}")


      # Grid opens page on page.* templates → need page_open_pad
      if stype == "variant-grid" and fnmatch.fnmatch(tmpl.name, "page*.json"):
        order = data.get("order") or []
        visible = [k for k in order if not (data.get("sections") or {}).get(k, {}).get("disabled")]
        if visible and visible[0] == key and not st.get("page_open_pad"):
          issues.append(
            f"{rel} {key}: page-open under nav — set page_open_pad true (72 desk / 56 phone)"
          )

      if stype == "guarantee-band":
        blob = (json.dumps(st) + json.dumps(sec.get("blocks") or {})).lower()
        for phrase in gb.get("forbidden_phrases") or []:
          if phrase.lower() in blob:
            issues.append(f"{rel} {key}: forbidden guarantee phrase {phrase!r}")
        # PDP Display head
        if fnmatch.fnmatch(tmpl.name, "product*.json"):
          role = (st.get("title_role") or "").strip()
          expect_role = gb.get("title_role_pdp") or "display"
          if role and role != expect_role:
            issues.append(f"{rel} {key}: title_role expected {expect_role!r}, got {role!r}")
          elif not role:
            issues.append(f"{rel} {key}: title_role missing (expected {expect_role!r})")
        # Outline CTA must not be white-on-white
        if (st.get("cta_style") or "").lower() == "outline" and (st.get("cta_text") or "").strip():
          tc = (st.get("cta_text_color") or "").lower()
          expect_tc = (gb.get("cta_outline_text_color") or "#1c1916").lower()
          if tc in ("", "#ffffff", "#fff", "white") or (tc and tc != expect_tc):
            issues.append(
              f"{rel} {key}: outline CTA text color expected {expect_tc}, got {st.get('cta_text_color')!r}"
            )

  # Liquid CSS must keep locked column token + outline CTA default
  gu_liq = build / "sections" / "guarantee-band.liquid"
  if gu_liq.exists() and not only:
    liq_txt = gu_liq.read_text()
    for must in gb.get("liquid_must_contain") or []:
      if must not in liq_txt:
        issues.append(f"sections/guarantee-band.liquid: missing locked pattern {must!r}")
    # Forbid loud/tiny hardcodes if present without token
    if "guarantee-item h4" in liq_txt:
      if "clamp(20px, 2.2vw, 26px)" in liq_txt:
        issues.append("sections/guarantee-band.liquid: forbidden loud column size clamp(20px, 2.2vw, 26px)")
      if re.search(r"\.guarantee-item h4\s*\{[^}]*font-size:\s*1[45]px", liq_txt):
        issues.append("sections/guarantee-band.liquid: forbidden tiny 14–15px column titles")

  # Open Sole Chair Pose yellow — COVER / P5A4949 / mmh 360
  chair = site.get("chair_pose_open") or {}
  if chair:
    for tmpl_name in chair.get("templates") or []:
      tmpl = build / "templates" / tmpl_name
      if only and tmpl.resolve() != only.resolve():
        continue
      if not tmpl.exists():
        issues.append(f"MISSING {tmpl_name} for chair_pose_open lock")
        continue
      try:
        data = load_json(tmpl)
      except Exception as e:
        issues.append(f"{tmpl_name}: JSON parse {e}")
        continue
      sid = chair.get("section") or "fifty-fifty-lifestyle"
      sec = (data.get("sections") or {}).get(sid) or {}
      if sec.get("disabled"):
        issues.append(f"templates/{tmpl_name} {sid}: Chair Pose section disabled")
        continue
      st = sec.get("settings") or {}
      title = st.get("title") or ""
      if chair.get("title_contains") and chair["title_contains"] not in title:
        issues.append(f"templates/{tmpl_name} {sid}: title expected contains {chair['title_contains']!r}, got {title!r}")
      img = str(st.get("image") or "") + str(st.get("image_url") or "")
      if chair.get("image_contains") and chair["image_contains"] not in img:
        issues.append(f"templates/{tmpl_name} {sid}: image expected {chair['image_contains']}, got {img!r}")
      for bad in chair.get("forbidden_images") or []:
        if bad in img:
          issues.append(f"templates/{tmpl_name} {sid}: forbidden image {bad}")
      for field, expect in [
        ("media_fit", chair.get("media_fit")),
        ("image_fit_mobile", chair.get("image_fit_mobile")),
        ("image_scale", chair.get("image_scale")),
        ("min_height", chair.get("min_height")),
        ("mobile_media_height", chair.get("mobile_media_height")),
        ("text_pad_top_mobile", chair.get("text_pad_top_mobile")),
        ("text_pad_bottom_mobile", chair.get("text_pad_bottom_mobile")),
      ]:
        if expect is None:
          continue
        got = st.get(field)
        if got != expect:
          issues.append(f"templates/{tmpl_name} {sid}: {field} expected {expect!r}, got {got!r}")

  return issues


def scan_forbidden_cream(site: dict, build: Path):
  """Fail if retired darker cream hexes are used as real color values."""
  issues = []
  forbid = [h.lower() for h in (site.get("forbidden_cream_hex") or ["#f5f2ec"])]
  soft = ((site.get("tokens") or {}).get("cream") or "#faf8f6").lower()
  allow_words = ("never", "retired", "forbidden", "darker", "ban", "do not", "don't")
  exts = {".liquid", ".css", ".json"}
  for path in build.rglob("*"):
    if path.suffix.lower() not in exts:
      continue
    if any(x in path.parts for x in ("node_modules", ".tmp")):
      continue
    try:
      lines = path.read_text().splitlines()
    except Exception:
      continue
    for i, line in enumerate(lines, 1):
      low = line.lower()
      for h in forbid:
        if h not in low:
          continue
        # allow documentation that bans the hex
        if any(w in low for w in allow_words):
          continue
        # allow JSON lock-style string lists only if key suggests forbid — rare in build
        rel = path.relative_to(build.parent) if build.name == "shopify-build" else path
        issues.append(f"{rel}:{i}: forbidden cream {h} as value (use {soft})")
  return issues



def scan_trusted_by_footer(site: dict, build: Path):
  """Footer Trusted by must stay dark sitewide."""
  issues = []
  lock = site.get("trusted_by_footer") or {}
  if not lock:
    return issues
  path = build / "sections" / "footer-group.json"
  if not path.exists():
    issues.append("MISSING sections/footer-group.json for trusted_by_footer lock")
    return issues
  try:
    data = load_json(path)
  except Exception as e:
    issues.append(f"footer-group.json: JSON parse {e}")
    return issues
  sid = lock.get("section") or "footer"
  sec = (data.get("sections") or {}).get(sid) or {}
  st = sec.get("settings") or {}
  if lock.get("show_studio_trust") is True and not st.get("show_studio_trust", True):
    issues.append("footer-group footer: show_studio_trust expected true")
  expect = lock.get("trust_theme") or "dark"
  got = st.get("trust_theme") or "light"
  if got != expect:
    issues.append(f"footer-group footer: trust_theme expected {expect!r}, got {got!r}")
  return issues


def main():
  root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".").resolve()
  only_rel = sys.argv[2] if len(sys.argv) > 2 else None

  if (root / "shopify-build").is_dir():
    build = root / "shopify-build"
  elif root.name == "shopify-build":
    build = root
    root = root.parent
  else:
    build = root

  locks_dir = root / "planning" / "locks"
  site_path = locks_dir / "sitewide.lock.json"
  any_fail = False
  only = (build / only_rel) if only_rel else None

  if site_path.exists():
    site = json.loads(site_path.read_text())
    print("## sitewide.lock.json")
    sw = scan_sitewide(site, build, only)
    if not sw:
      print("OK — no sitewide mismatches in scanned templates")
    else:
      any_fail = True
      for i in sw[:80]:
        print("FAIL:", i)
      if len(sw) > 80:
        print(f"… +{len(sw) - 80} more")

  for lock_path in sorted(locks_dir.glob("*.lock.json")):
    if lock_path.name == "sitewide.lock.json":
      continue
    lock = json.loads(lock_path.read_text())
    if lock.get("skip_page_scan") or not lock.get("template"):
      continue
    if only_rel and lock.get("template") and only_rel not in lock["template"]:
      continue
    print(f"## {lock_path.name}")
    issues, visible = scan_page_lock(lock, build)
    print("visible:", " → ".join(visible[:14]), ("…" if len(visible) > 14 else ""))
    if not issues:
      print("OK — matches lock")
    else:
      any_fail = True
      for i in issues:
        print("FAIL:", i)

  return 1 if any_fail else 0


if __name__ == "__main__":
  sys.exit(main())
