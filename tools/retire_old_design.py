#!/usr/bin/env python3
"""Retire every page still on the old (leadmode.css) design.

For each old-design page this:
  1. 301-redirects it (in site/_redirects) to the most relevant new-design page,
  2. deletes the old HTML file so the old design can never be served or indexed,
  3. rewrites any internal link to it on remaining pages to point straight at the target,
  4. drops it from sitemap.xml.

Idempotent. Run it LAST, after any generator (geo_pages.py, industries.py, service_pages.py,
blog.py, seo_pass.py ...), because those older generators can recreate the retired pages.
Usage (repo root):  python3 tools/retire_old_design.py
"""
import glob
import os
import re

SITE = "site"
NEW_MARK = "/assets/firstbyte/firstbyte"   # stylesheet path only the new design uses

CITIES = ["atascocita", "conroe", "cypress", "houston", "humble", "huntsville", "katy", "kingwood",
          "magnolia", "montgomery", "new-caney", "oak-ridge-north", "pearland", "pinehurst", "porter",
          "shenandoah", "spring", "sugar-land", "tomball", "willis"]
CITY_SERVICES = ["seo", "paid-advertising", "web-design", "brand-development", "influencer-marketing",
                 "performance-marketing", "public-relations"]

# old URL -> new-design URL (most relevant match)
MAP = {
    "/services/": "/#services",
    "/services/seo/": "/services/search-marketing/",
    "/services/paid-advertising/": "/services/search-marketing/",
    "/services/public-relations/": "/services/web-design-seo-pr/",
    "/industries/": "/#industries",
    "/industries/retail/": "/industries/ecommerce/",
    "/industries/banking/": "/industries/service/",
    "/launch/": "/services/web-design-seo-pr/",
    "/work/viceroy-cabo/": "/case-studies/viceroy-los-cabos/",
    "/work/": "/case-studies/",
    "/work_tax/brand-development/": "/services/creative-branding/",
    "/work_tax/influencer-marketing/": "/services/paid-social-advertising/",
    "/work_tax/web-design-development/": "/services/web-design-seo-pr/",
    "/work_tax/performance-marketing/": "/services/search-marketing/",
}
for svc in CITY_SERVICES:
    for c in CITIES:
        MAP[f"/{svc}-{c}-tx/"] = f"/digital-marketing-agency-{c}-tx/"
# catch-alls (any other legacy portfolio URL), written after the specific rules
SPLATS = [
    ("/work/*", "/case-studies/"),
    ("/work_tax/performance-marketing/page/*", "/services/search-marketing/"),
    ("/work_tax/*", "/case-studies/"),
]

R_START, R_END = "# retire-old-design:start", "# retire-old-design:end"


def url_of(path):
    u = "/" + os.path.relpath(path, SITE).replace(os.sep, "/")
    return u[: -len("index.html")] if u.endswith("index.html") else u


def target_for(u):
    if u in MAP:
        return MAP[u]
    if u.startswith("/work/"):
        return "/case-studies/"
    if u.startswith("/work_tax/performance-marketing/"):
        return "/services/search-marketing/"
    if u.startswith("/work_tax/"):
        return "/case-studies/"
    return None


def main():
    old = []
    for p in glob.glob(f"{SITE}/**/*.html", recursive=True):
        s = open(p, encoding="utf-8").read()
        if NEW_MARK not in s and "</head>" in s:
            old.append(p)
    unmapped = [url_of(p) for p in old if not target_for(url_of(p))]
    if unmapped:
        raise SystemExit("No redirect target for: " + ", ".join(unmapped) + " (add them to MAP)")

    # 1. redirects (exact rules, with and without trailing slash, then splats)
    lines = [R_START]
    for src, dst in MAP.items():
        lines.append(f"{src} {dst} 301")
        if src != "/" and src.endswith("/"):
            lines.append(f"{src[:-1]} {dst} 301")
    for src, dst in SPLATS:
        lines.append(f"{src} {dst} 301")
    lines.append(R_END)
    rp = f"{SITE}/_redirects"
    cur = open(rp, encoding="utf-8").read() if os.path.exists(rp) else ""
    cur = re.sub(re.escape(R_START) + r".*?" + re.escape(R_END) + r"\n?", "", cur, flags=re.S).rstrip("\n")
    open(rp, "w", encoding="utf-8").write("\n".join(lines) + "\n" + (cur + "\n" if cur else ""))

    # 2. delete old files (and now-empty dirs)
    for p in old:
        os.remove(p)
        d = os.path.dirname(p)
        while d != SITE and os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)
            d = os.path.dirname(d)

    # 3. internal links on remaining pages
    pat = re.compile(r'href="(?:https://firstbyte\.agency)?(/[^"#?]*)"')
    fixed = 0
    for p in glob.glob(f"{SITE}/**/*.html", recursive=True):
        s = open(p, encoding="utf-8").read()

        def sub(m):
            u = m.group(1)
            key = u if u.endswith("/") else u + "/"
            t = target_for(key) if (key in MAP or key.startswith(("/work/", "/work_tax/"))) else None
            return f'href="{t}"' if t else m.group(0)

        out = pat.sub(sub, s)
        if out != s:
            open(p, "w", encoding="utf-8").write(out)
            fixed += 1

    # 4. sitemap
    sp = f"{SITE}/sitemap.xml"
    sm = open(sp, encoding="utf-8").read()

    def keep(m):
        loc = re.search(r"<loc>https://firstbyte\.agency(/[^<]*)</loc>", m.group(0))
        u = loc.group(1) if loc else ""
        return "" if target_for(u if u.endswith("/") else u + "/") else m.group(0)

    sm2 = re.sub(r"\s*<url>.*?</url>", keep, sm, flags=re.S)
    open(sp, "w", encoding="utf-8").write(sm2)
    print(f"retired {len(old)} old-design pages; {len(MAP) + len(SPLATS)} redirect rules; "
          f"links fixed on {fixed} pages; sitemap {sm.count('<loc>')} -> {sm2.count('<loc>')} URLs")


if __name__ == "__main__":
    main()
