#!/usr/bin/env python3
"""Render each post's share image (1200x630 PNG) to site/assets/firstbyte/blog/<slug>/og.png.

Usage (repo root):  python3 tools/render_og.py posts_oct_2026_b
Needs Node + Playwright (Chromium). Uses tools/blog_figures.hero(..., title=...).
"""
import importlib
import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(__file__))
from blog_figures import hero  # noqa: E402

posts = importlib.import_module(sys.argv[1]).POSTS
tmp = tempfile.mkdtemp()
jobs = []
for p in posts:
    if not p.get("hero"):
        continue
    page = os.path.join(tmp, p["slug"] + ".html")
    open(page, "w", encoding="utf-8").write(
        '<html><body style="margin:0">' + hero(p["hero"], w=1200, h=630, title=p["title"]) + "</body></html>")
    out = os.path.abspath(f"site/assets/firstbyte/blog/{p['slug']}/og.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    jobs.append([page, out])
js = os.path.join(tmp, "og.js")
open(js, "w").write("""const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
for (const [src, out] of %s) { await pg.goto('file://' + src); await pg.screenshot({ path: out }); }
await b.close(); })();""" % json.dumps(jobs))
npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
subprocess.run(["node", js], check=True, env={**os.environ, "NODE_PATH": npm_root})
print(f"rendered {len(jobs)} share images")
