"""Remove Margaritaville, the Cynthia Woods Mitchell Pavilion and Landshark Lager from the whole site (Nov 2026).

Logos are swapped for other brands already shown on the site so every strip and row keeps its count:
  Landshark Lager  -> Celsius (client logo strips), Budweiser (beverage rows)
  Margaritaville   -> Wyndham Hotels & Resorts
  Pavilion         -> NASCAR (live events rows)
Blog copy that named the Pavilion is reworded to stay accurate without it.
Idempotent; safe to re-run after any rebuild. Run: python3 tools/remove_brands_nov_2026.py [--check]
"""
import os, re, sys, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITE = os.path.join(ROOT, "site")
A = "/assets/firstbyte/"

def img_sub(s, old_file, new_file, new_alt, height_map=None):
    """Replace <img> tags pointing at old_file; keep loading/decoding attrs, drop stale width/height."""
    def rep(m):
        tag = m.group(0)
        h = int(re.search(r'height: (\d+)px', tag).group(1))
        if height_map:
            h = height_map(h)
        lazy = ' loading="lazy"' if 'loading="lazy"' in tag else ''
        return f'<img src="{A}{new_file}" alt="{new_alt}" style="height: {h}px"{lazy} decoding="async">'
    return re.sub(r'<img src="%s%s"[^>]*>' % (re.escape(A), re.escape(old_file)), rep, s)

# Strips whose other logos are all clients' wordmarks: Celsius replaces Landshark.
# Rows grouped by industry (homepage industry list, industry pages): Budweiser keeps it a beverage row.
def fix_logos(s, path):
    beverage_row = 'class="ind-logos"' in s or "/industries/" in path
    if beverage_row:
        # industry rows: only touch imgs inside ind-logos / ix-logos spans/divs
        def row(m):
            r = m.group(0)
            r = img_sub(r, "land-shark-logo.png", "budweiser.png", "Budweiser (Anheuser-Busch) logo", lambda h: h + 6)
            r = img_sub(r, "margaritaville.png", "wyndham.png", "Wyndham Hotels & Resorts logo", lambda h: h)
            r = img_sub(r, "pavilion.png", "nascar.png", "NASCAR logo", lambda h: max(16, h - 12))
            return r
        s = re.sub(r'<(span|div) class="(?:ind|ix)-logos">.*?</\1>', row, s, flags=re.S)
    # logo marquees / client strips
    s = img_sub(s, "land-shark-logo.png", "celsius.png", "Celsius logo", lambda h: h - 2)
    s = img_sub(s, "margaritaville.png", "wyndham.png", "Wyndham Hotels & Resorts logo", lambda h: h + 4)
    s = img_sub(s, "pavilion.png", "nascar.png", "NASCAR logo", lambda h: max(16, h - 8))
    return s

TEXT = [
    ("Pre-show dinner before a concert at the Cynthia Woods Mitchell Pavilion.",
     "Pre-show dinner before a big concert in The Woodlands."),
    ("<b>Ride the local calendar:</b> Pavilion concert nights,", "<b>Ride the local calendar:</b> concert nights in The Woodlands,"),
    ("distance to the Pavilion, to the nearest hospital, to the marina.",
     "distance to Market Street, to the nearest hospital, to the marina."),
    ("event organizers who book the Pavilion or conference space.", "event organizers who book venues or conference space."),
    ("The Woodlands sees spikes around Pavilion concerts and IRONMAN Texas", "The Woodlands sees spikes around big concert weekends and IRONMAN Texas"),
    ("A Saturday matinee at the Cynthia Woods Mitchell Pavilion pulls easily from", "A Saturday matinee in The Woodlands pulls easily from"),
    ("Ticketmaster (Pavilion capacity), ", ""),
    ('    "pavilion": L("https://origin-blog.ticketmaster.com/venue-faq-cynthia-woods-mitchell-pavilion-woodlands-tx", "16,500 people"),\n', ""),
]
CONCERTS_SRC = "The Cynthia Woods Mitchell Pavilion holds {SRC['pavilion']}, and fans who"
CONCERTS_HTML = re.compile(r'The Cynthia Woods Mitchell Pavilion holds <a href="https://origin-blog\.ticketmaster\.com/[^"]*"[^>]*>16,500 people</a>, and fans who')
CONCERTS_NEW = "Big summer shows draw crowds in the thousands, and fans who"

def fix_text(s):
    for old, new in TEXT:
        s = s.replace(old, new)
    s = s.replace(CONCERTS_SRC, CONCERTS_NEW)
    s = CONCERTS_HTML.sub(CONCERTS_NEW, s)
    return s

def files():
    for p in glob.glob(os.path.join(SITE, "**", "*"), recursive=True):
        if p.endswith((".html", ".xml", ".txt", ".json")) and os.path.isfile(p):
            yield p
    for p in glob.glob(os.path.join(ROOT, "tools", "posts_*.py")):
        yield p

BAD = re.compile(r"margaritaville|cynthia woods|landshark|land-shark|land shark|\bpavilion\b", re.I)

def run(check=False):
    changed, left = 0, []
    for p in files():
        s = open(p, encoding="utf-8").read()
        n = fix_text(fix_logos(s, p)) if p.endswith(".html") else fix_text(s)
        if n != s:
            changed += 1
            if not check:
                open(p, "w", encoding="utf-8").write(n)
        if BAD.search(n):
            left.append(os.path.relpath(p, ROOT))
    print(f"brand removal: {'would change' if check else 'changed'} {changed} files; remaining mentions: {left or 'none'}")
    return left

if __name__ == "__main__":
    sys.exit(1 if run("--check" in sys.argv) else 0)
