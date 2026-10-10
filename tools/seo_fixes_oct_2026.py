#!/usr/bin/env python3
"""Site-wide SEO + schema fixes from the October 2026 audit. Idempotent; run from the repo root
AFTER every generator (build_new_posts.py, seo_pass.py ...) and BEFORE apply_analytics.py /
retire_old_design.py:

    python3 tools/seo_fixes_oct_2026.py

What it does
  schema   - fixes the Organization/LocalBusiness logo + image (they pointed at a deleted WordPress file)
           - drops breadcrumb steps that point at redirected URLs (/services/, /industries/)
           - case studies: full Article markup (@id, mainEntityOfPage, image, dates, author/publisher refs)
           - blog posts: page-specific image, author/publisher linked to the #organization entity
  social   - a page-specific 1200x630 share image (og:image / twitter:image) for every blog post,
             case study, service, industry and city page that was using the generic site image
  links    - "From the blog" section with 3 relevant guides on every industry, service and city page
  content  - case-study pages: first content heading h3 -> h2 (no skipped heading level)
           - Terms page title lengthened
  files    - /blog/feed.xml (RSS) + <link rel="alternate"> on every page, /site.webmanifest + <link rel="manifest">,
             llms.txt key pages / guides / case studies refreshed, sitemap lastmod filled in,
             _headers gains HSTS + Permissions-Policy, two oversized hero photos recompressed
"""
import datetime
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from blog_figures import hero  # noqa: E402

SITE = "site"
BASE = "https://firstbyte.agency"
TODAY = datetime.date.today().isoformat()
WP_IMG = "https://firstbyte.agency/wp-content/uploads/2025/02/474564578_122209849448190241_1671659700825052575_n.jpg"
LOGO = {"@type": "ImageObject", "url": BASE + "/icon-512.png", "width": 512, "height": 512}
ORG_REF = {"@type": "Organization", "@id": BASE + "/#organization", "name": "First Byte", "url": BASE + "/"}
PUBLISHER = {"@type": "Organization", "@id": BASE + "/#organization", "name": "First Byte", "logo": LOGO}
GENERIC_OG = BASE + "/og-image.png"


def read(p):
    return open(p, encoding="utf-8").read()


def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)


def url_of(p):
    u = "/" + os.path.relpath(p, SITE).replace(os.sep, "/")
    return u[:-10] if u.endswith("index.html") else u


def esc(s):
    return html.escape(s, quote=True)


def redirect_sources():
    out = set()
    for line in read(f"{SITE}/_redirects").splitlines():
        parts = line.split()
        if len(parts) >= 2 and not line.startswith("#") and "*" not in parts[0]:
            out.add(parts[0])
    return out


REDIRECTS = redirect_sources()


def page_kind(u):
    if u.startswith("/blog/") and u != "/blog/":
        return "post"
    if u.startswith("/case-studies/") and u != "/case-studies/":
        return "case"
    if u.startswith("/services/"):
        return "service"
    if u.startswith("/industries/"):
        return "industry"
    if u.startswith("/digital-marketing-agency-"):
        return "city"
    return "other"


MOTIFS = [("hvac", "hvac"), ("roof", "roof"), ("pool", "pool"), ("restaurant", "restaurant"), ("toasted-yolk", "restaurant"),
          ("chiro", "chiro"), ("gym", "fitness"), ("fitness", "fitness"), ("equinox", "fitness"), ("real-estate", "realestate"),
          ("medical", "medical"), ("dental", "medical"), ("med-spa", "medical"), ("skinlab", "medical"), ("wedding", "wedding"),
          ("live-entertainment", "wedding"), ("hotel", "hotel"), ("hospitality", "hotel"), ("viceroy", "hotel"),
          ("billboard", "billboard"), ("streaming", "billboard"), ("ctv", "billboard"), ("kroger", "billboard"),
          ("call", "phone"), ("scam", "phone"), ("review", "stars"), ("social-proof", "stars"), ("fake-reviews", "stars"),
          ("contractor", "tools"), ("industries/service", "tools"), ("home-services", "tools"), ("angi", "tools"),
          ("website", "browser"), ("web-design", "browser"), ("homepage", "browser"), ("landing", "browser"),
          ("mobile", "browser"), ("accessibility", "browser"), ("load", "browser"), ("ecommerce", "browser"),
          ("brand", "browser"), ("logo", "browser"), ("copy", "browser"), ("seo", "search"), ("google", "search"),
          ("search", "search"), ("near-me", "search"), ("map-pack", "search"), ("chatgpt", "search"), ("ai-", "search"),
          ("digital-marketing-agency-", "search"), ("service-areas", "search"), ("local", "search"), ("case-studies/", "growth"), ("/blog/", "search"), ("contact", "phone")]


def motif_for(u):
    for k, m in MOTIFS:
        if k in u:
            return m
    return "growth"


def og_title(s):
    t = re.search(r'<meta property="og:title" content="([^"]*)"', s)
    t = html.unescape(t.group(1)) if t else html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1))
    t = re.split(r"\s+\|\s+", t)[0].strip()
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    h1 = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h1.group(1)))).strip() if h1 else ""
    # prefer the H1 when it is a readable length (titles are shortened for Google)
    return h1 if 20 <= len(h1) <= 90 else t


# ------------------------------------------------------------------ JSON-LD rewriting
def fix_jsonld(u, s, og_url):
    def fix_block(m):
        raw = m.group(1)
        try:
            data = json.loads(raw)
        except Exception:
            return m.group(0)
        nodes = data.get("@graph") if isinstance(data, dict) and "@graph" in data else [data]

        def walk(o, parent_key=None):
            if isinstance(o, dict):
                for k, v in list(o.items()):
                    if v == WP_IMG:
                        o[k] = LOGO if k == "logo" else GENERIC_OG
                    elif isinstance(v, dict) and v.get("url") == WP_IMG:
                        o[k] = LOGO if k == "logo" else GENERIC_OG
                    else:
                        walk(v, k)
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    if v == WP_IMG:
                        o[i] = GENERIC_OG
                    else:
                        walk(v, parent_key)

        walk(data)

        def crumbs(o):  # every BreadcrumbList, top-level or nested (e.g. WebPage.breadcrumb)
            if isinstance(o, dict):
                if o.get("@type") == "BreadcrumbList":
                    items = [i for i in o.get("itemListElement", [])
                             if not (isinstance(i.get("item"), str) and i["item"].replace(BASE, "") in REDIRECTS)]
                    for k, i in enumerate(items, 1):
                        i["position"] = k
                    o["itemListElement"] = items
                for v in o.values():
                    crumbs(v)
            elif isinstance(o, list):
                for v in o:
                    crumbs(v)

        crumbs(data)
        for n in nodes:
            t = n.get("@type")
            if t == "BlogPosting":
                n["author"] = dict(ORG_REF)
                n["publisher"] = dict(PUBLISHER)
                if og_url:
                    n["image"] = {"@type": "ImageObject", "url": og_url, "width": 1200, "height": 630}
            if t == "Article" and page_kind(u) == "case":
                url = BASE + u
                n["@id"] = url + "#article"
                n["url"] = url
                n["mainEntityOfPage"] = url
                n["author"] = dict(ORG_REF)
                n["publisher"] = dict(PUBLISHER)
                n.setdefault("datePublished", "2026-10-03")
                n["dateModified"] = n.get("dateModified") or TODAY
                if og_url:
                    n["image"] = {"@type": "ImageObject", "url": og_url, "width": 1200, "height": 630}
                n.setdefault("inLanguage", "en-US")
        out = json.dumps(data, ensure_ascii=False, indent=1)
        return '<script type="application/ld+json">\n' + out + "\n</script>"

    return re.sub(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', fix_block, s, flags=re.S)


# ------------------------------------------------------------------ related guides
RELATED = {
    "/industries/service/": ["hvac-marketing-houston-the-woodlands", "roofing-marketing-houston-storm-season", "angi-vs-thumbtack-leads-worth-it-contractors"],
    "/industries/restaurants/": ["restaurant-marketing-the-woodlands-houston", "is-yelp-advertising-worth-it-small-business", "grand-opening-marketing-plan-30-days"],
    "/industries/hospitality/": ["hotel-marketing-houston-direct-bookings", "wedding-venue-marketing-houston-montgomery-county", "restaurant-marketing-the-woodlands-houston"],
    "/industries/sports-fitness/": ["gym-fitness-studio-marketing-the-woodlands-houston", "ugc-vs-influencers-creator-content", "facebook-instagram-ads-local-businesses"],
    "/industries/live-entertainment/": ["wedding-venue-marketing-houston-montgomery-county", "billboard-advertising-cost-houston", "streaming-tv-ads-worth-it-small-business"],
    "/industries/ecommerce/": ["performance-max-vs-search-campaigns-local", "retargeting-explained", "email-marketing-basics"],
    "/industries/beverage-spirits/": ["micro-influencers-vs-big-names", "ftc-rules-influencer-partnerships", "billboard-advertising-cost-houston"],
    "/industries/technology/": ["show-up-in-chatgpt-ai-search-aeo", "ai-overviews-local-search-houston", "landing-pages-101"],
    "/services/search-marketing/": ["google-ads-management-houston-cost", "google-ads-cost-per-click-houston-benchmarks", "is-yelp-advertising-worth-it-small-business"],
    "/services/paid-social-advertising/": ["facebook-instagram-ads-local-businesses", "geo-fencing-ads-target-customers-nearby", "retargeting-explained"],
    "/services/web-design-seo-pr/": ["seo-cost-houston-the-woodlands", "how-much-does-a-website-cost-the-woodlands", "why-are-my-google-reviews-disappearing"],
    "/services/creative-branding/": ["how-to-rebrand-without-losing-customers", "psychology-of-logos", "brand-colors-that-build-trust"],
    "/services/ctv-ooh-streaming-radio/": ["billboard-advertising-cost-houston", "streaming-tv-ads-worth-it-small-business", "geo-fencing-ads-target-customers-nearby"],
}
CITY_LOCAL = {"spring": "marketing-your-business-spring-tx", "conroe": "reaching-customers-conroe-montgomery",
              "montgomery": "reaching-customers-conroe-montgomery", "willis": "reaching-customers-conroe-montgomery"}
CITY_POOL = ["hvac-marketing-houston-the-woodlands", "restaurant-marketing-the-woodlands-houston", "chiropractor-marketing-the-woodlands-houston",
             "roofing-marketing-houston-storm-season", "medical-practice-marketing-houston", "pool-builder-marketing-houston-the-woodlands",
             "real-estate-agent-marketing-the-woodlands-houston", "gym-fitness-studio-marketing-the-woodlands-houston",
             "wedding-venue-marketing-houston-montgomery-county", "hotel-marketing-houston-direct-bookings",
             "billboard-advertising-cost-houston", "google-business-listing-scam-calls", "angi-vs-thumbtack-leads-worth-it-contractors",
             "is-yelp-advertising-worth-it-small-business", "why-are-my-google-reviews-disappearing"]
HUBS = {"/blog/", "/case-studies/", "/service-areas/", "/about/", "/contact/"}
R_START, R_END = "<!-- fb-related:start -->", "<!-- fb-related:end -->"


def related_for(u, i_city):
    if u in RELATED:
        return RELATED[u], None
    m = re.match(r"^/digital-marketing-agency-([a-z-]+)-tx/$", u)
    if m:
        city = m.group(1)
        first = CITY_LOCAL.get(city, "rank-in-google-map-pack-houston")
        a, b = CITY_POOL[(2 * i_city) % len(CITY_POOL)], CITY_POOL[(2 * i_city + 1) % len(CITY_POOL)]
        name = city.replace("-", " ").title()
        return [first, a, b], name
    return None, None


def blog_cards(idx_html):
    cards = {}
    for m in re.finditer(r'<a class="post rv[^"]*" href="/blog/([^"/]+)/">.*?</a>', idx_html, re.S):
        cards[m.group(1)] = m.group(0)
    return cards


def related_section(slugs, cards, city):
    heading = f'Guides for <span class="cy">{esc(city)} businesses.</span>' if city else 'Guides that <span class="cy">go deeper.</span>'
    body = "".join(cards[s].replace('class="post rv', 'class="post rv') for s in slugs if s in cards)
    return (f'{R_START}\n<section class="sec sv-sec fb-related">\n<div class="wrap">\n<div class="head rv"><div><span class="lbl"><span class="tri"></span>From the blog</span>'
            f'<h2 class="h2">{heading}</h2></div><a class="btn btn-g" href="/blog/">All guides <span class="arr">→</span></a></div>\n'
            f'<div class="posts">{body}</div>\n</div>\n</section>\n{R_END}\n')


def insert_related(s, block):
    s = re.sub(re.escape(R_START) + r".*?" + re.escape(R_END) + r"\n?", "", s, flags=re.S)
    i = s.find('class="faq-list"')
    at = s.rfind("<section", 0, i) if i != -1 else -1
    if at == -1:
        at = s.find("<footer")
    return s[:at] + block + s[at:] if at != -1 else s


# ------------------------------------------------------------------ main
def main():
    pages = {}
    for root, _, files in os.walk(SITE):
        for f in files:
            if f.endswith(".html"):
                p = os.path.join(root, f)
                pages[p] = read(p)
    cards = blog_cards(pages[f"{SITE}/blog/index.html"])
    changed = set()

    # ---- share images
    og_jobs = []
    og_for = {}
    for p, s in pages.items():
        u = url_of(p)
        if 'content="noindex' in s or (page_kind(u) == "other" and u not in HUBS):
            continue
        cur = re.search(r'<meta property="og:image" content="([^"]*)"', s)
        cur = cur.group(1) if cur else ""
        if cur and cur != GENERIC_OG and "/assets/firstbyte/og/" not in cur:
            og_for[p] = cur
            continue
        key = u.strip("/").replace("/", "-")
        rel = f"/assets/firstbyte/og/{key}.png"
        og_for[p] = BASE + rel
        if not os.path.exists(SITE + rel):
            og_jobs.append((SITE + rel, motif_for(u), og_title(s)))
    if og_jobs:
        import tempfile
        tmp = tempfile.mkdtemp()
        jobs = []
        for i, (out, motif, title) in enumerate(og_jobs):
            page = os.path.join(tmp, f"{i}.html")
            write(page, '<html><body style="margin:0">' + hero(motif, w=1200, h=630, title=title) + "</body></html>")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            jobs.append([page, os.path.abspath(out)])
        js = os.path.join(tmp, "og.js")
        write(js, "const { chromium } = require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1200,height:630}});"
                  "for(const [s,o] of %s){await pg.goto('file://'+s);await pg.screenshot({path:o});}await b.close();})();" % json.dumps(jobs))
        npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        subprocess.run(["node", js], check=True, env={**os.environ, "NODE_PATH": npm_root})
        from PIL import Image
        for out, _, _ in og_jobs:
            Image.open(out).convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT).save(out, optimize=True)

    city_i = 0
    for p in sorted(pages):
        s = pages[p]
        u = url_of(p)
        orig = s
        og_url = og_for.get(p)
        # og / twitter image
        if og_url and og_url != GENERIC_OG:
            s = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*(")', lambda m: m.group(1) + og_url + m.group(2), s)
            alt = esc(og_title(s))
            s = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(")', lambda m: m.group(1) + alt + m.group(2), s)
        s = fix_jsonld(u, s, og_url if og_url and og_url != GENERIC_OG else None)
        # related guides
        slugs, city = related_for(u, city_i)
        if slugs:
            if city:
                city_i += 1
            s = insert_related(s, related_section(slugs, cards, city))
        # case-study heading level
        if page_kind(u) == "case":
            s = s.replace('<h2 class=\\"cs-h\\">', '<h2 class="cs-h">')
            s = re.sub(r'(<div class="cs-copy">.*?)<h3>(.*?)</h3>', lambda m: m.group(1) + '<h2 class="cs-h">' + m.group(2) + "</h2>", s, count=1, flags=re.S)
        # terms title
        if u == "/terms-of-service/":
            s = s.replace("<title>Terms of Service | First Byte</title>", "<title>Terms of Service | First Byte Digital Marketing</title>")
        # feed + manifest links
        if 'type="application/rss+xml"' not in s:
            s = s.replace("</head>", '<link rel="alternate" type="application/rss+xml" title="First Byte blog" href="https://firstbyte.agency/blog/feed.xml">\n</head>', 1)
        if 'rel="manifest"' not in s:
            s = s.replace("</head>", '<link rel="manifest" href="/site.webmanifest">\n</head>', 1)
        if s != orig:
            write(p, s)
            changed.add(u)
            pages[p] = s

    # ---- case-study heading style
    css_p = f"{SITE}/assets/firstbyte/lead.css"
    css = read(css_p)
    rule = '.cs-copy h2.cs-h{font-family:"Funnel Display",sans-serif;font-size:clamp(28px,2.6vw,40px);font-weight:600;letter-spacing:-.035em;line-height:1.02;margin:6px 0 0}'
    if rule not in css:
        write(css_p, css + "\n/* case-study pages: first heading is an h2 (was h3) */\n" + rule + "\n")

    # ---- RSS feed
    posts = []
    for p, s in pages.items():
        u = url_of(p)
        if page_kind(u) != "post":
            continue
        t = og_title(s)
        d = re.search(r'<meta name="description" content="([^"]*)"', s)
        dt = re.search(r'"datePublished": "([0-9-]+)"', s)
        cat = re.search(r'"articleSection": "([^"]+)"', s)
        posts.append((dt.group(1) if dt else "2026-01-01", u, t, html.unescape(d.group(1)) if d else "", cat.group(1) if cat else ""))
    posts.sort(reverse=True)

    def rfc(d):
        return datetime.datetime.strptime(d, "%Y-%m-%d").strftime("%a, %d %b %Y 12:00:00 -0500")
    items = "".join(
        f"<item><title>{esc(t)}</title><link>{BASE}{u}</link><guid isPermaLink=\"true\">{BASE}{u}</guid>"
        f"<pubDate>{rfc(d)}</pubDate>{f'<category>{esc(c)}</category>' if c else ''}<description>{esc(desc)}</description></item>\n"
        for d, u, t, desc, c in posts)
    write(f"{SITE}/blog/feed.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>\n'
          f'<title>First Byte blog</title><link>{BASE}/blog/</link><description>Marketing guides for businesses in The Woodlands and Greater Houston.</description>'
          f'<language>en-us</language><atom:link href="{BASE}/blog/feed.xml" rel="self" type="application/rss+xml"/>'
          f"<lastBuildDate>{rfc(posts[0][0])}</lastBuildDate>\n{items}</channel></rss>\n")

    # ---- web manifest
    write(f"{SITE}/site.webmanifest", json.dumps({
        "name": "First Byte", "short_name": "First Byte", "start_url": "/", "display": "browser",
        "background_color": "#0e0c0f", "theme_color": "#0e0c0f",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1) + "\n")

    # ---- llms.txt
    lp = f"{SITE}/llms.txt"
    llms = read(lp)
    def section(title, lines):
        return f"## {title}\n" + "\n".join(lines) + "\n"
    key = section("Key pages", [
        f"- [Home]({BASE}/): Overview of First Byte's digital marketing services.",
        f"- [Free Ad Spend Leak Check]({BASE}/contact/): A free 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours.",
        f"- [Google Ads / search marketing]({BASE}/services/search-marketing/)",
        f"- [Paid social advertising]({BASE}/services/paid-social-advertising/)",
        f"- [Web design, SEO & PR]({BASE}/services/web-design-seo-pr/)",
        f"- [Creative & branding]({BASE}/services/creative-branding/)",
        f"- [CTV, billboards & streaming radio]({BASE}/services/ctv-ooh-streaming-radio/)",
        f"- [Case studies]({BASE}/case-studies/): Results for Equinox, Kroger, Celsius, Vital Proteins, Viceroy Los Cabos and more.",
        f"- [Service areas]({BASE}/service-areas/): The 20 Greater Houston cities we serve.",
        f"- [About]({BASE}/about/): Founder Sean Melton's story and how First Byte works.",
        f"- [Blog]({BASE}/blog/): {len(posts)} guides on local SEO, Google Ads, social ads and industry marketing. RSS: {BASE}/blog/feed.xml",
        f"- [Contact]({BASE}/contact/): (713) 578-0634, contact@firstbyte.agency."])
    cases = []
    for p, s in sorted(pages.items()):
        u = url_of(p)
        if page_kind(u) == "case":
            cases.append(f"- [{og_title(s)}]({BASE}{u})")
    guides = [f"- [{t}]({BASE}{u})" for d, u, t, desc, c in posts]
    llms = re.sub(r"## Key pages\n.*?(?=\n## )", lambda _: key.rstrip("\n"), llms, flags=re.S)
    llms = re.sub(r"\n## (Case studies|Guides|Latest articles)\n.*\Z", "", llms, flags=re.S)
    llms = llms.rstrip("\n") + "\n\n" + section("Case studies", cases) + "\n" + section("Guides", guides)
    llms = llms.replace("https://firstbyte.agency/launch/", "https://firstbyte.agency/contact/")  # /launch/ was retired
    write(lp, llms)

    # ---- sitemap lastmod
    sp = f"{SITE}/sitemap.xml"
    sm = read(sp)

    def fix_url(m):
        block = m.group(0)
        loc = re.search(r"<loc>https://firstbyte\.agency([^<]*)</loc>", block).group(1)
        if "<lastmod>" not in block:
            block = block.replace("</loc>", f"</loc><lastmod>{TODAY}</lastmod>")
        elif loc in changed:
            block = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{TODAY}</lastmod>", block)
        return block
    write(sp, re.sub(r"<url>.*?</url>", fix_url, sm, flags=re.S))

    # ---- headers
    hp = f"{SITE}/_headers"
    hd = read(hp)
    if "Strict-Transport-Security" not in hd:
        hd = hd.replace("  Referrer-Policy: strict-origin-when-cross-origin",
                        "  Referrer-Policy: strict-origin-when-cross-origin\n  Strict-Transport-Security: max-age=31536000\n"
                        "  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()", 1)
        write(hp, hd)

    # ---- oversized photos
    from PIL import Image
    for f in ("office.webp", "vic.webp"):
        fp = f"{SITE}/assets/firstbyte/{f}"
        if os.path.exists(fp) and os.path.getsize(fp) > 200_000:
            im = Image.open(fp)
            im.save(fp, "WEBP", quality=72, method=6)

    print(f"share images rendered: {len(og_jobs)}; pages changed: {len(changed)}; feed items: {len(posts)}")


if __name__ == "__main__":
    main()
