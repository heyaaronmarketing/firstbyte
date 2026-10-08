"""Partner logos in the awards bar.

Every awards bar (<ul class="awl">) lists the six partner programs as the company's
logo (shown in white to match the client logo wall) with the program tier under it.
Logos live in site/assets/firstbyte/partners/<key>.svg.

To use a program's official partner BADGE instead of the plain logo (Google and Meta in
particular ask partners to use their badge), download it from that program's partner
portal and save it as site/assets/firstbyte/partners/<key>-badge.svg (or .png/.webp),
then re-run this script: the badge replaces the logo + label for that program.

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
        if os.path.isfile(f"{DIR}/{key}-badge.{ext}"):
            return f"/assets/firstbyte/partners/{key}-badge.{ext}"
    return None


def tile(key, name, tier):
    badge = badge_file(key)
    if badge:
        return (f'<li class="awc pbadge pb-official" data-partner="{key}"><img src="{badge}" '
                f'alt="First Byte is a {name} {tier}" loading="lazy" decoding="async"></li>')
    return (f'<li class="awc pbadge" data-partner="{key}"><img class="pb-logo" src="/assets/firstbyte/partners/{key}.svg" '
            f'alt="{name} {tier}" loading="lazy" decoding="async"><small aria-hidden="true">{tier}</small></li>')


TILES = "".join(tile(*p) for p in PARTNERS)
LI_RE = re.compile(r'<li class="awc pbadge[^"]*" data-partner="[a-z]+">.*?</li>', re.S)


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
    print(f"updated {changed} files; official badges used for: {', '.join(have) or 'none (logos shown)'}")


if __name__ == "__main__":
    main()
