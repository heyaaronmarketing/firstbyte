"""Partner badges in the awards bar.

Every awards bar (<ul class="awl">) lists the six partner programs. Each shows as a
text tile until its official badge file exists in site/assets/firstbyte/partners/:

    google-partner.svg   meta-partner.svg     tiktok-partner.svg
    semrush-partner.svg  hubspot-partner.svg  klaviyo-partner.svg

(.png or .webp work too.) Download each badge from that program's partner portal,
drop it in that folder with the name above, then run this script: it swaps the text
tile for the badge image on every page. Use only badges for programs you are
currently enrolled in.

Idempotent. Run from the repo root:  python3 tools/apply_partner_badges.py
"""
import glob
import os
import re

PARTNERS = [
    ("google", "Google", "Partner"),
    ("meta", "Meta", "Business Partner"),
    ("tiktok", "TikTok", "Marketing Partner"),
    ("semrush", "Semrush", "Agency Partner"),
    ("hubspot", "HubSpot", "Solutions Partner"),
    ("klaviyo", "Klaviyo", "Partner"),
]
DIR = "site/assets/firstbyte/partners"


def badge_file(key):
    for ext in ("svg", "webp", "png"):
        if os.path.isfile(f"{DIR}/{key}-partner.{ext}"):
            return f"/assets/firstbyte/partners/{key}-partner.{ext}"
    return None


def tile(key, name, tier):
    src = badge_file(key)
    img = (f'<img src="{src}" alt="{name} {tier} badge" style="height: 56px" loading="lazy" decoding="async">'
           if src else "")
    return (f'<li class="awc pbadge" data-partner="{key}">{img}'
            f'<span class="pb-txt"><b>{name}</b><small>{tier}</small></span></li>')


TILES = "".join(tile(*p) for p in PARTNERS)
LI_RE = re.compile(r'<li class="awc pbadge" data-partner="[a-z]+">.*?</li>', re.S)


def main():
    changed = 0
    for path in glob.glob("site/**/*.html", recursive=True):
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        if 'class="awl"' not in src:
            continue
        out = LI_RE.sub("", src)
        out = re.sub(r'(<ul class="awl"[^>]*>.*?)(</ul>)', lambda m: m.group(1) + TILES + m.group(2), out, flags=re.S)
        if out != src:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(out)
            changed += 1
    have = [k for k, *_ in PARTNERS if badge_file(k)]
    print(f"updated {changed} files; badge images found for: {', '.join(have) or 'none yet'}")


if __name__ == "__main__":
    main()
