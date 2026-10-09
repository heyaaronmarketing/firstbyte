#!/usr/bin/env python3
"""Render the posts in tools/posts_oct_2026.py into site/blog/<slug>/ using the current
blog design, then add them to the blog index, the homepage blog section and the sitemap.

The page shell (head, nav, sidebar offer, contact form, footer) is copied from an existing
post, so new posts always match the live design. Idempotent.

Run from the repo root:  python3 tools/build_new_posts.py [posts_module]
  (default module: posts_oct_2026; the October batch 2 posts are posts_oct_2026_b)
Posts may also carry:
  "hero":    a motif name from blog_figures._motif (hvac, roof, pool, ...) -> hero illustration
             at the top of the article plus /assets/firstbyte/blog/<slug>/og.png (made by
             tools/render_og.js) used as the share image and schema image.
  "figures": {name: spec}; put <!--fig:name--> in a section's HTML where the figure goes.
             Specs are documented in tools/blog_figures.py.
"""
import html
import json
import os
import re
import sys
from datetime import date

import importlib

sys.path.insert(0, os.path.dirname(__file__))
_mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else "posts_oct_2026")
POSTS, DATE = _mod.POSTS, _mod.DATE
from blog_figures import render as render_fig, hero as render_hero  # noqa: E402

SITE = "site"
BASE = "https://firstbyte.agency"
TEMPLATE = f"{SITE}/blog/digital-marketing-cost-the-woodlands-houston/index.html"
ICON = {  # sprite index (see the .ic sprite in /assets/firstbyte/icons2.png)
    "Meta": 0, "Instagram": 1, "Facebook": 2, "TikTok": 3, "YouTube": 6, "Google Ads": 9, "Google": 10,
    "Google Business Profile": 11, "HubSpot": 19, "Google Analytics": 22, "Tag Manager": 23,
    "Semrush": 28, "Search Console": 29, "Yelp": 30, "Nextdoor": 34, "LinkedIn": 38, "Microsoft Ads": 39,
}


def read(p):
    return open(p, encoding="utf-8").read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)


def esc(s):
    return html.escape(s, quote=True)


def slugify(t):
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def human_date(d):
    y, m, dd = map(int, d.split("-"))
    return date(y, m, dd).strftime("%B %-d, %Y")


def words(post):
    txt = " ".join(h for _, h in post["sections"]) + " ".join(q + a for q, a in post["faq"])
    return len(re.sub(r"<[^>]+>", " ", txt).split())


def icons(names, size):
    total = 46 * size
    return "".join(
        f'<span class="pa-ic pa{i}"><span class="ic" role="img" aria-label="{esc(n)}" style="width: {size}px; height: {size}px; '
        f'background-size: {total}px {size}px; background-position: -{ICON[n] * size}px 0"></span></span>'
        for i, n in enumerate(names))


def card(p, extra_cls=""):
    """Post card used on the blog index, homepage and 'Keep reading'."""
    mins = max(3, round(p["words"] / 230))
    return (f'<a class="post rv {extra_cls}" href="/blog/{p["slug"]}/"><div class="post-art {p["art"]}"><div class="pa-grid"></div>'
            f'{icons(p["icons"], 44)}<span class="post-cat">{esc(p["category"])}</span></div><div class="post-b">'
            f'<small style="color: var(--muted); font-size: 12px">{human_date(p["date"])} · {mins} min read</small>'
            f'<h3>{esc(p["title"])}</h3><p>{esc(p["desc"])}</p><span class="post-more">Read the post <i>→</i></span></div></a>')


def existing_card(slug):
    """Card for an existing post, taken from the blog index."""
    idx = read(f"{SITE}/blog/index.html")
    m = re.search(rf'<a class="post rv[^"]*" href="/blog/{re.escape(slug)}/">.*?</a>', idx, re.S)
    return m.group(0) if m else ""


tpl = read(TEMPLATE)
new_slugs = {p["slug"] for p in POSTS}
for p in POSTS:
    p["date"] = p.get("date", DATE)
    p["words"] = words(p)
    if not p["seo_title"].endswith(" | First Byte") and len(p["seo_title"] + " | First Byte") <= 60:
        p["seo_title"] += " | First Byte"

for p in POSTS:
    url = f"{BASE}/blog/{p['slug']}/"
    mins = max(3, round(p["words"] / 230))
    s = tpl
    # ---- head ---------------------------------------------------------------------
    s = re.sub(r"<!-- ===== SEO head: .*? ===== -->", f"<!-- ===== SEO head: {url} ===== -->", s)
    s = re.sub(r"<title>.*?</title>", f"<title>{html.escape(p['seo_title'], quote=False)}</title>", s, flags=re.S)
    for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc(p["desc"]) + m.group(2), s)
    for prop in ('property="og:title"', 'name="twitter:title"'):
        s = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc(p["seo_title"]) + m.group(2), s)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), s)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), s)
    s = re.sub(r'(<meta property="article:published_time" content=")[^"]*(")', lambda m: m.group(1) + p["date"] + m.group(2), s)
    graph = [
        {"@type": "BlogPosting", "@id": url + "#article", "headline": p["title"], "description": p["desc"],
         "datePublished": p["date"], "dateModified": p["date"],
         "author": {"@type": "Organization", "name": "First Byte", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "@id": BASE + "/#organization", "name": "First Byte",
                       "logo": {"@type": "ImageObject", "url": BASE + "/icon-512.png"}},
         "mainEntityOfPage": url, "image": BASE + "/og-image.png", "articleSection": p["category"],
         "wordCount": p["words"], "inLanguage": "en-US",
         "spatialCoverage": [{"@type": "Place", "name": "The Woodlands, TX"}, {"@type": "Place", "name": "Houston, TX"}]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    if p.get("hero"):
        og = f"{BASE}/assets/firstbyte/blog/{p['slug']}/og.png"
        graph[0]["image"] = og
        s = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*(")', lambda m: m.group(1) + og + m.group(2), s)
        s = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(")', lambda m: m.group(1) + esc(p["title"]) + m.group(2), s)
    schema = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    s = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _: f'<script type="application/ld+json">\n{schema}\n</script>', s, count=1, flags=re.S)
    # ---- hero ---------------------------------------------------------------------
    s = re.sub(r'<span class="pill-cat">.*?</span>', f'<span class="pill-cat">{esc(p["category"])}</span>', s, count=1)
    s = re.sub(r'<h1 class="bp-h1">.*?</h1>', lambda _: f'<h1 class="bp-h1">{esc(p["title"])}</h1>', s, count=1, flags=re.S)
    s = re.sub(r'<p class="bp-dek">.*?</p>', lambda _: f'<p class="bp-dek">{esc(p["desc"])}</p>', s, count=1, flags=re.S)
    s = re.sub(r'(<div class="bp-meta">.*?<small>).*?(</small>)', lambda m: m.group(1) + f"{human_date(p['date'])} · {mins} min read" + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r"https://firstbyte\.agency/blog/digital-marketing-cost-the-woodlands-houston/", url, s)
    s = re.sub(r'<div class="post-art b\d bp-art"><div class="pa-grid"></div>.*?</div></div>',
               lambda _: f'<div class="post-art {p["art"]} bp-art"><div class="pa-grid"></div>{icons(p["icons"], 64)}</div></div>', s, count=1, flags=re.S)
    # ---- table of contents + body -------------------------------------------------
    heads = [h for h, _ in p["sections"] if h] + ["Frequently asked questions"]
    toc = "".join(f'<a href="#{slugify(h)}">{esc(h)}</a>' for h in heads)
    s = re.sub(r'(<nav class="bp-toc" aria-label="In this article"><span class="lbl">In this article</span>).*?(</nav>)',
               lambda m: m.group(1) + toc + m.group(2), s, count=1, flags=re.S)
    inline = re.search(r'<aside class="bp-inline">.*?</aside>', tpl, re.S).group(0)
    author = re.search(r'<div class="bp-author">.*?</div></div>', tpl, re.S).group(0)
    body = []
    asset_dir = f"{SITE}/assets/firstbyte/blog/{p['slug']}"
    if p.get("hero"):
        write(f"{asset_dir}/hero.svg", render_hero(p["hero"]))
        body.append(f'<figure class="bp-fig bp-fig-hero"><img src="/assets/firstbyte/blog/{p["slug"]}/hero.svg" width="1200" height="600" '
                    f'alt="{esc(p.get("hero_alt", p["title"]))}" fetchpriority="high"></figure>')

    def fig(m):
        name = m.group(1)
        spec = p["figures"][name]
        svg = render_fig(spec)
        wh = re.search(r'width="(\d+)" height="(\d+)"', svg)
        write(f"{asset_dir}/{name}.svg", svg)
        svg_m = render_fig(spec, 440)  # narrow version for phones, so chart text stays readable
        whm = re.search(r'width="(\d+)" height="(\d+)"', svg_m)
        write(f"{asset_dir}/{name}-m.svg", svg_m)
        cap = f'<figcaption>{spec["caption"]}</figcaption>' if spec.get("caption") else ""
        src = f"/assets/firstbyte/blog/{p['slug']}/{name}"
        return (f'<figure class="bp-fig"><picture><source media="(max-width: 600px)" srcset="{src}-m.svg" width="{whm.group(1)}" height="{whm.group(2)}">'
                f'<img src="{src}.svg" width="{wh.group(1)}" height="{wh.group(2)}" '
                f'alt="{esc(spec.get("alt", spec["title"]))}" loading="lazy" decoding="async"></picture>{cap}</figure>')

    for i, (h, content) in enumerate(p["sections"]):
        if h:
            body.append(f'<h2 id="{slugify(h)}">{esc(h)}</h2>')
        body.append(re.sub(r"<!--fig:([a-z0-9_-]+)-->", fig, content.strip()))
        if i == 2:
            body.append(inline)
    body.append(f'<h2 id="{slugify("Frequently asked questions")}">Frequently asked questions</h2>')
    for q, a in p["faq"]:
        body.append(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>")
    body.append(author)
    s = re.sub(r'<article class="bp-body">.*?</article>', lambda _: '<article class="bp-body">' + "\n".join(body) + "\n</article>", s, count=1, flags=re.S)
    # ---- keep reading ---------------------------------------------------------------
    rel = []
    for r in p["related"]:
        if r in new_slugs:
            rel.append(card(next(x for x in POSTS if x["slug"] == r)))
        else:
            rel.append(existing_card(r))
    s = re.sub(r'(<div class="head rv"><div><span class="lbl"><span class="tri"></span>Keep reading</span>.*?<div class="posts">).*?(</div>\n</div>\n</section>)',
               lambda m: m.group(1) + "".join(rel) + m.group(2), s, count=1, flags=re.S)
    write(f"{SITE}/blog/{p['slug']}/index.html", s)

# ---- blog index: newest first ------------------------------------------------------------
newest = sorted(POSTS, key=lambda x: x["date"])  # oldest of the batch first
idx_path = f"{SITE}/blog/index.html"
idx = read(idx_path)
# drop any cards for these posts from a previous run
idx = re.sub(r'<a class="post rv[^"]*" href="/blog/(' + "|".join(map(re.escape, new_slugs)) + r')/">.*?</a>', "", idx, flags=re.S)
feat_m = re.search(r'(<div class="hub-feat">)((?:<a class="post.*?</a>)?)(</div>)', idx, re.S)
old_feat = feat_m.group(2)
lead = POSTS[0]
rest = [card(p) for p in POSTS[1:]]
idx = idx[:feat_m.start()] + feat_m.group(1) + card(lead) + feat_m.group(3) + idx[feat_m.end():]
grid = idx.index('<div class="posts">', feat_m.start()) + len('<div class="posts">')
idx = idx[:grid] + "".join(rest) + old_feat + idx[grid:]
total = len(re.findall(r'<a class="post rv[^"]*" href="/blog/[^"]+/">', idx))
idx = re.sub(r"\d+ articles and counting\.", f"{total} articles and counting.", idx)
cats = {}
for c in re.findall(r'<span class="post-cat">([^<]+)</span>', idx):
    cats[c] = cats.get(c, 0) + 1
idx = re.sub(r'<div class="hub-cats">.*?</div>', lambda _: '<div class="hub-cats">' + "".join(
    f"<span>{c}<b>{n}</b></span>" for c, n in sorted(cats.items(), key=lambda x: -x[1])) + "</div>", idx, count=1, flags=re.S)


def add_blogposts(m):
    data = json.loads(m.group(2))
    nodes = data.get("@graph", [data])
    for n in nodes:
        if n.get("@type") == "Blog":
            posts = [x for x in n.get("blogPost", []) if not any(x.get("url", "").endswith(f"/blog/{s}/") for s in new_slugs)]
            for p in reversed(POSTS):
                posts.insert(0, {"@type": "BlogPosting", "headline": p["title"], "url": f"{BASE}/blog/{p['slug']}/", "datePublished": p["date"]})
            n["blogPost"] = posts[:20]
    return m.group(1) + "\n" + json.dumps(data, ensure_ascii=False, indent=1) + "\n" + m.group(3)


idx = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', add_blogposts, idx, count=1, flags=re.S)
write(idx_path, idx)

# ---- homepage blog section: six newest -------------------------------------------------
home_path = f"{SITE}/index.html"
home = read(home_path)
hm = re.search(r'(<section class="sec blog" id="blog".*?<div class="posts">)(.*?)(</div>\n<div style="display: flex; justify-content: center)', home, re.S)
cards_now = re.findall(r'<a class="post rv[^"]*" href="/blog/[^"]+/">.*?</a>', hm.group(2), re.S)
cards_now = [c for c in cards_now if not any(f'/blog/{s}/"' in c for s in new_slugs)]
home_cards = [card(p) for p in POSTS] + cards_now
home = home[:hm.start()] + hm.group(1) + "".join(home_cards[:6]) + hm.group(3) + home[hm.end():]
write(home_path, home)

# ---- sitemap --------------------------------------------------------------------------
sm_path = f"{SITE}/sitemap.xml"
sm = read(sm_path)
add = "".join(f"<url><loc>{BASE}/blog/{p['slug']}/</loc><lastmod>{p['date']}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>\n"
              for p in POSTS if f"/blog/{p['slug']}/</loc>" not in sm)
if add:
    sm = sm.replace("</urlset>", add + "</urlset>")
    write(sm_path, sm)

print(f"built {len(POSTS)} posts; blog index now {total} posts; homepage shows {min(6, len(home_cards))} newest")
