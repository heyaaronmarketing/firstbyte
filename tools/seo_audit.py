#!/usr/bin/env python3
"""Read-only SEO audit of every HTML page in site/.

Reports, per page type: title length/duplicates/local terms, meta description
length/duplicates, H1 count, canonical, robots, image alt problems, and which
schema.org types are present. Writes a CSV for detail and prints a summary.

Run from the repo root:  python3 tools/seo_audit.py [out.csv]
"""
import collections
import csv
import html
import json
import os
import re
import sys

ROOT = "site"
LOCAL = re.compile(r"woodlands|houston|spring|conroe|katy|cypress|tomball|magnolia|humble|kingwood|atascocita|montgomery|shenandoah|oak ridge|pearland|sugar land|huntsville|new caney|pinehurst|porter|willis|texas|\btx\b", re.I)


def page_type(url, s):
    if url == "/":
        return "home"
    if url.startswith("/blog/page/") or url == "/blog/":
        return "blog-index"
    if url.startswith("/blog/"):
        return "blog-post"
    if url.startswith("/case-studies/"):
        return "case-study"
    if url.startswith("/industries/"):
        return "industry"
    if url.startswith("/services/"):
        return "service"
    if url.startswith("/digital-marketing-agency-"):
        return "geo-agency"
    if re.match(r"^/(seo|paid-advertising|web-design|brand-development|influencer-marketing|performance-marketing|public-relations)-[a-z-]+-tx/$", url):
        return "geo-service"
    if url.startswith("/work_tax/") or url.startswith("/work/"):
        return "legacy-work"
    return "page"


def text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def schema_types(s):
    types = []
    for block in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', s, re.S):
        try:
            data = json.loads(block)
        except Exception:
            types.append("INVALID_JSON")
            continue
        stack = [data]
        while stack:
            x = stack.pop()
            if isinstance(x, dict):
                t = x.get("@type")
                if isinstance(t, str):
                    types.append(t)
                elif isinstance(t, list):
                    types += t
                stack += list(x.values())
            elif isinstance(x, list):
                stack += x
    return types


rows = []
for r, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".html"):
            continue
        p = os.path.join(r, f)
        rel = "/" + os.path.relpath(p, ROOT).replace(os.sep, "/")
        url = rel[:-10] if rel.endswith("/index.html") else rel
        s = open(p, encoding="utf-8", errors="replace").read()
        title = text((re.search(r"<title>(.*?)</title>", s, re.S) or [None, ""])[1])
        desc_m = re.search(r'<meta name="description" content="([^"]*)"', s)
        desc = html.unescape(desc_m.group(1)) if desc_m else ""
        robots = (re.search(r'<meta name="robots" content="([^"]*)"', s) or [None, ""])[1]
        canon = (re.search(r'<link rel="canonical" href="([^"]*)"', s) or [None, ""])[1]
        h1s = re.findall(r"<h1\b[^>]*>(.*?)</h1>", s, re.S)
        imgs = re.findall(r"<img\b[^>]*>", s)
        no_alt = [i for i in imgs if not re.search(r'\salt="', i)]
        empty_alt = [i for i in imgs if re.search(r'\salt=""', i)]
        bad_alt = [i for i in imgs if re.search(r'\salt="([^"]*\.(jpe?g|png|webp|gif)|img[-_ ]?\d*|image|photo|untitled|\d+[_-]\d+[^"]*)"', i, re.I)]
        types = schema_types(s)
        new_design = "/assets/firstbyte/" in s
        rows.append(dict(
            url=url, type=page_type(url, s), new_design=new_design,
            noindex="noindex" in robots.lower(), title=title, title_len=len(title),
            title_local=bool(LOCAL.search(title)), desc=desc, desc_len=len(desc),
            h1=len(h1s), h1_text=text(h1s[0]) if h1s else "", canonical=canon,
            imgs=len(imgs), no_alt=len(no_alt), empty_alt=len(empty_alt), bad_alt=len(bad_alt),
            schema=";".join(sorted(set(types))),
            has_faq_markup=bool(re.search(r'<details class="qa"', s)),
        ))

rows.sort(key=lambda x: x["url"])
idx = [r for r in rows if not r["noindex"]]
tdup = collections.Counter(r["title"] for r in idx)
ddup = collections.Counter(r["desc"] for r in idx if r["desc"])

if len(sys.argv) > 1:
    with open(sys.argv[1], "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def pct(n, d):
    return f"{n}/{d}"


print(f"{len(rows)} pages, {len(idx)} indexable\n")
by = collections.defaultdict(list)
for r in idx:
    by[r["type"]].append(r)
hdr = f"{'type':<13}{'n':>4} {'title>60':>9} {'title<30':>9} {'no-local':>9} {'dupTitle':>9} {'desc?':>6} {'desc>160':>9} {'desc<70':>8} {'dupDesc':>8} {'h1!=1':>6} {'noAlt':>6} {'badAlt':>7}"
print(hdr)
for t, rs in sorted(by.items()):
    print(f"{t:<13}{len(rs):>4} "
          f"{sum(r['title_len'] > 60 for r in rs):>9} {sum(r['title_len'] < 30 for r in rs):>9} "
          f"{sum(not r['title_local'] for r in rs):>9} {sum(tdup[r['title']] > 1 for r in rs):>9} "
          f"{sum(not r['desc'] for r in rs):>6} {sum(r['desc_len'] > 160 for r in rs):>9} "
          f"{sum(0 < r['desc_len'] < 70 for r in rs):>8} {sum(bool(r['desc']) and ddup[r['desc']] > 1 for r in rs):>8} "
          f"{sum(r['h1'] != 1 for r in rs):>6} {sum(r['no_alt'] for r in rs):>6} {sum(r['bad_alt'] for r in rs):>7}")
print("\nschema types by page type:")
for t, rs in sorted(by.items()):
    c = collections.Counter()
    for r in rs:
        c.update(set(r["schema"].split(";")) - {""})
    print(f"  {t:<13} " + ", ".join(f"{k}:{v}" for k, v in c.most_common()))
print("\nnoindex pages:", [r["url"] for r in rows if r["noindex"]][:20])
