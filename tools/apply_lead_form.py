"""Rebuild every lead form on the site into ONE standard form.

Fields: Name, Email (any email), Phone, Website, Industry, Monthly ad spend.
Keeps each form's own wrapper (classes, id, header line, hours note) so it still fits
its page's layout; replaces only the fields and the submit button.

Industry pages pre-select their industry. Anything else can pre-select one with
?industry=<slug> in the URL or a link carrying data-industry="<slug>" (see site.js).

Idempotent. Run from the repo root:  python3 tools/apply_lead_form.py
"""
import glob
import re

INDUSTRIES = [
    ("home-services", "Home services (HVAC, plumbing, electrical, roofing)"),
    ("med-spa", "Med spa & wellness"),
    ("dental-medical", "Dental & medical practice"),
    ("chiropractic", "Chiropractic & physical therapy"),
    ("professional-services", "Law, accounting & professional services"),
    ("restaurants", "Restaurants & food"),
    ("fitness", "Fitness, gyms & sports"),
    ("hospitality", "Hotels, resorts & travel"),
    ("live-events", "Live events & entertainment"),
    ("ecommerce", "eCommerce & consumer brands"),
    ("beverage", "Beverage & spirits"),
    ("technology", "Technology & B2B services"),
    ("other", "Other"),
]

AD_SPEND = [
    "Not running ads yet",
    "Under $2k / month",
    "$2k – $5k / month",
    "$5k – $10k / month",
    "$10k+ / month",
]

# /industries/<page>/ -> industry slug to pre-select
INDUSTRY_PAGES = {
    "service": "home-services",
    "restaurants": "restaurants",
    "sports-fitness": "fitness",
    "hospitality": "hospitality",
    "live-entertainment": "live-events",
    "ecommerce": "ecommerce",
    "beverage-spirits": "beverage",
    "technology": "technology",
}

BUTTON = ('<div class="full"><button class="btn btn-p" type="submit" style="border: 0; cursor: pointer; font: inherit; '
          'font-weight: 600; font-size: 17px; width: 100%; min-height: 60px">Get my free Ad Spend Leak Check '
          '<span class="arr">→</span></button></div>')


def fields(prefix, industry=None):
    ind_opts = ['<option value="" disabled selected>Choose one</option>' if not industry else
                '<option value="" disabled>Choose one</option>']
    for slug, label in INDUSTRIES:
        sel = " selected" if slug == industry else ""
        ind_opts.append(f'<option value="{label.replace("&", "&amp;")}" data-slug="{slug}"{sel}>{label.replace("&", "&amp;")}</option>')
    spend_opts = ['<option value="" disabled selected>Choose one</option>'] + [
        f'<option>{s}</option>' for s in AD_SPEND]
    p = prefix
    return "\n".join([
        '<input type="hidden" name="offer" value="Ad Spend Leak Check">',
        f'<div class="fld"><label for="{p}-name">Name</label><input id="{p}-name" name="name" required type="text" placeholder="Jane Smith" autocomplete="name"></div>',
        f'<div class="fld"><label for="{p}-email">Email</label><input id="{p}-email" name="email" required type="email" placeholder="you@business.com" autocomplete="email"></div>',
        f'<div class="fld"><label for="{p}-phone">Phone</label><input id="{p}-phone" name="phone" type="tel" placeholder="(713) 555-0123" autocomplete="tel"></div>',
        f'<div class="fld"><label for="{p}-web">Website</label><input id="{p}-web" name="website" type="text" inputmode="url" placeholder="yourbusiness.com" autocomplete="url"></div>',
        f'<div class="fld"><label for="{p}-ind">Industry</label><select id="{p}-ind" name="industry" required>{"".join(ind_opts)}</select></div>',
        f'<div class="fld"><label for="{p}-spend">Monthly ad spend</label><select id="{p}-spend" name="ad_spend" required>{"".join(spend_opts)}</select></div>',
        BUTTON,
    ])


FORM_RE = re.compile(r'(<form\b[^>]*action="/api/contact"[^>]*>)(.*?)(</form>)', re.S)
HIDDEN_RE = re.compile(r'<input type="hidden" name="_v"[^>]*>.*?name="_honey"[^>]*>', re.S)
HEADER_RE = re.compile(r'<div class="full ca-fh">.*?</div>', re.S)
HOURS_RE = re.compile(r'<div class="full"><div class="hours">.*?</div></div>', re.S)
PREFIX_RE = re.compile(r'id="([a-z]+)-name"')


def rebuild(match, path):
    open_tag, body, close = match.groups()
    if 'data-ajax="news"' in open_tag or 'lp-form' in open_tag:
        return match.group(0)
    hidden = HIDDEN_RE.search(body)
    header = HEADER_RE.search(body)
    hours = HOURS_RE.search(body)
    pm = PREFIX_RE.search(body)
    prefix = pm.group(1) if pm else "lf"
    m = re.search(r"site/industries/([^/]+)/index\.html$", path)
    industry = INDUSTRY_PAGES.get(m.group(1)) if m else None
    if "data-lead" not in open_tag:
        open_tag = open_tag[:-1] + " data-lead>"
    parts = [open_tag]
    parts.append(hidden.group(0) if hidden else
                 '<input type="hidden" name="_v" value="2"><input type="hidden" name="_subject" value="New website lead — First Byte">'
                 '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true" '
                 'style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">')
    if header:
        parts.append(header.group(0))
    parts.append(fields(prefix, industry))
    if hours:
        parts.append(hours.group(0))
    parts.append(close)
    return "\n".join(parts)


def main():
    changed = 0
    for path in glob.glob("site/**/*.html", recursive=True):
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        out = FORM_RE.sub(lambda m: rebuild(m, path), src)
        if out != src:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(out)
            changed += 1
    print(f"updated {changed} files")


if __name__ == "__main__":
    main()
