#!/usr/bin/env python3
"""Check a posts module before building:  python3 tools/validate_posts.py posts_b_a

Checks structure, lengths, figure references, related slugs, word counts, and flags
phrases that make writing read as machine-generated.
"""
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from blog_figures import render  # noqa: E402

BANNED = [
    "in today's", "in today’s", "digital landscape", "ever-evolving", "ever-changing", "delve", "navigate the",
    "navigating the", "game-changer", "game changer", "unlock", "elevate", "leverage", "harness", "tapestry",
    "it's important to note", "it’s important to note", "in conclusion", "furthermore", "moreover",
    "seamless", "robust", "cutting-edge", "look no further", "whether you're", "whether you’re", "when it comes to",
    "at the end of the day", "the world of", "realm", "embark", "supercharge", "skyrocket", "a testament",
    "let's dive", "let’s dive", "dive into", "dive in", "plays a crucial role", "crucial", "pivotal", "boasts",
    "not just about", "it's not just", "it’s not just", "in the realm", "bustling", "vibrant", "nestled",
    "treasure trove", "one-stop", "paramount", "myriad", "plethora", "empower", "foster", "holistic",
]
ICONS = {"Meta", "Instagram", "Facebook", "TikTok", "YouTube", "Google Ads", "Google", "Google Business Profile",
         "HubSpot", "Google Analytics", "Tag Manager", "Semrush", "Search Console", "Yelp", "Nextdoor", "LinkedIn",
         "Microsoft Ads"}
MOTIFS = {"hvac", "roof", "pool", "restaurant", "chiro", "fitness", "realestate", "medical", "wedding", "hotel"}


def text(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))


def main(modname):
    mod = importlib.import_module(modname)
    existing = set(os.listdir("site/blog"))
    errs, warns = [], []
    for p in mod.POSTS:
        sl = p.get("slug", "?")
        E = lambda m: errs.append(f"[{sl}] {m}")  # noqa: E731
        W = lambda m: warns.append(f"[{sl}] {m}")  # noqa: E731
        for k in ("slug", "title", "seo_title", "desc", "category", "icons", "art", "related", "sections", "faq", "hero", "figures"):
            if k not in p:
                E(f"missing key {k}")
        if errs:
            continue
        if not re.fullmatch(r"[a-z0-9-]+", sl):
            E("slug must be lowercase-hyphenated")
        if sl in existing:
            E("slug already exists on the blog")
        if len(p["seo_title"]) > 60:
            E(f"seo_title {len(p['seo_title'])} chars (max 60)")
        if not 120 <= len(p["desc"]) <= 158:
            E(f"desc {len(p['desc'])} chars (want 120-158)")
        if len(p["icons"]) != 3 or not set(p["icons"]) <= ICONS:
            E(f"icons must be 3 of {sorted(ICONS)}")
        if p["art"] not in {f"b{i}" for i in range(1, 7)}:
            E("art must be b1..b6")
        if p["hero"] not in MOTIFS:
            E(f"hero must be one of {sorted(MOTIFS)}")
        for r in p["related"]:
            if r not in existing:
                E(f"related slug not on blog: {r}")
        body = " ".join(h for _, h in p["sections"])
        refs = re.findall(r"<!--fig:([a-z0-9_-]+)-->", body)
        if set(refs) != set(p["figures"]):
            E(f"figure refs {refs} don't match figures {list(p['figures'])}")
        if len(p["figures"]) < 3:
            E("need at least 3 figures")
        for n, spec in p["figures"].items():
            try:
                render(spec)
            except Exception as ex:  # noqa: BLE001
                E(f"figure {n} fails to render: {ex!r}")
            if not spec.get("alt"):
                E(f"figure {n} needs alt text")
        all_txt = text(body) + " " + " ".join(q + " " + a for q, a in p["faq"])
        wc = len(all_txt.split())
        if wc < 1800:
            E(f"only {wc} words (want 1,800+)")
        low = all_txt.lower() + " " + p["title"].lower()
        hits = [b for b in BANNED if b in low]
        if hits:
            E(f"AI-tell phrases: {hits}")
        dashes = all_txt.count("—")
        if dashes > wc / 250:
            E(f"{dashes} em dashes; keep under {int(wc / 250)}")
        if len(p["faq"]) < 4:
            E("need 4+ FAQs")
        links = re.findall(r'href="(https?://[^"]+)"', body)
        if len(links) < 3:
            W(f"only {len(links)} outside sources linked")
        inner = re.findall(r'href="(/[^"#]*)"', body)
        for u in inner:
            path = "site" + u + ("index.html" if u.endswith("/") else "")
            if not os.path.exists(path):
                E(f"internal link to missing page {u}")
        if len(inner) < 3:
            W(f"only {len(inner)} internal links")
        print(f"{sl}: {wc} words, {len(p['figures'])} figures, {len(links)} sources, {len(inner)} internal links")
    for w in warns:
        print("WARN", w)
    for e in errs:
        print("ERROR", e)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main(sys.argv[1])
