#!/usr/bin/env python3
"""Install Google Analytics 4 and the First Byte event tracking on every page.

Adds to each page's <head>:
  1. the GA4 gtag.js snippet for MEASUREMENT_ID (skipped while it is empty), and
  2. /assets/firstbyte/analytics.js, which sends the lead, call, CTA, case study and
     scroll events described at the top of that file.

Set MEASUREMENT_ID below (GA4 → Admin → Data streams → firstbyte.agency → Measurement ID),
then run from the repo root:  python3 tools/apply_analytics.py
Idempotent: re-running replaces the block, so changing the ID is one edit + one run.
(enhance.py's own GA4_ID stays empty so the tag is never installed twice.)
"""
import glob
import re
import sys

MEASUREMENT_ID = ""  # e.g. "G-ABC123XYZ9"

START, END = "<!-- fb-analytics:start -->", "<!-- fb-analytics:end -->"


def block(mid):
    parts = [START]
    if mid:
        parts.append(f'<script async src="https://www.googletagmanager.com/gtag/js?id={mid}"></script>')
        parts.append("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
                     f"gtag('js',new Date());gtag('config','{mid}');</script>")
    parts.append('<script src="/assets/firstbyte/analytics.js?v=1" defer></script>')
    parts.append(END)
    return "\n".join(parts)


def main():
    mid = (sys.argv[1] if len(sys.argv) > 1 else MEASUREMENT_ID).strip()
    if mid and not re.fullmatch(r"G-[A-Z0-9]{6,12}", mid):
        sys.exit(f"'{mid}' doesn't look like a GA4 measurement ID (G-XXXXXXXXXX)")
    b = block(mid)
    changed = 0
    for path in glob.glob("site/**/*.html", recursive=True):
        s = open(path, encoding="utf-8").read()
        if "</head>" not in s:
            continue
        out = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
        # put it early in <head> so the tag loads first
        m = re.search(r'<meta name="viewport"[^>]*>\n?', out) or re.search(r"<meta charset[^>]*>\n?", out)
        at = m.end() if m else out.index("</head>")
        out = out[:at] + b + "\n" + out[at:]
        if out != s:
            open(path, "w", encoding="utf-8").write(out)
            changed += 1
    print(f"analytics: {'GA4 ' + mid if mid else 'no measurement ID yet (event script only)'}; updated {changed} pages")


if __name__ == "__main__":
    main()
