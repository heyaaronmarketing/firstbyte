"""Build a standalone page for every homepage case study, plus a /case-studies/ index.

Source of truth for each story is its <article id="stage-..."> on the homepage
(site/index.html). Edit the story there, then re-run this script so the standalone
page matches. The page shell (head, nav, form section, footer) comes from
site/industries/service/index.html.

Run from the repo root:  python3 tools/build_case_studies.py
"""
import html
import json
import os
import re

SITE = "site"
BASE = "https://firstbyte.agency"

# homepage stage id -> (url slug, display name, industry slug for the form, label)
CASES = {
    "eqx": ("equinox", "Equinox", "fitness", "Fitness"),
    "ty": ("the-toasted-yolk-cafe", "The Toasted Yolk Cafe", "restaurants", "Restaurants"),
    "ion": ("ionstream", "ionstream", "technology", "Technology"),
    "vic": ("viceroy-los-cabos", "Viceroy Los Cabos", "hospitality", "Hospitality"),
    "vp": ("vital-proteins", "Vital Proteins", "ecommerce", "Consumer brands"),
    "kr": ("kroger", "Kroger", "ecommerce", "Grocery retail"),
    "cel": ("celsius", "Celsius", "beverage", "Beverage"),
    "sl": ("skinlab-by-dr-roth", "SkinLab by Dr. Roth", "med-spa", "Med spa"),
}


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def esc(s):
    return html.escape(s, quote=True)


home = read(f"{SITE}/index.html")
tpl = read(f"{SITE}/industries/service/index.html")

# ---- pieces of the shell ----------------------------------------------------
head_m = re.search(r"<head>(.*?)</head>", tpl, re.S)
head_tail = re.search(r'<link rel="preconnect".*', head_m.group(1), re.S).group(0)  # fonts, css, js
icons = "\n".join(re.findall(r'<link rel="(?:icon|apple-touch-icon|manifest)"[^>]*>', head_m.group(1)))
body_open = re.search(r"<body.*?</header>", tpl, re.S).group(0)
form_section = re.findall(r'<section class="sec sv-sec"[^>]*>(?:(?!<section).)*?<form.*?</section>', tpl, re.S)[-1]
footer = re.search(r'<footer class="foot".*</html>', tpl, re.S).group(0)
form_m = re.search(r"<form\b.*?</form>", form_section, re.S)
form_html = form_m.group(0)
awards = re.search(r'<div class="awards rv">.*?</ul></div>', tpl, re.S).group(0)


def form_for(industry, name):
    f = re.sub(r'<div class="full ca-fh">.*?</div>',
               f'<div class="full ca-fh"><b>Want results like {esc(name)}?</b>'
               '<small>Free Ad Spend Leak Check · We reply within 1 hour, Mon–Fri</small></div>', form_html, flags=re.S)
    # pre-select this case's industry
    f = re.sub(r'(<select id="[a-z]+-ind" name="industry" required>)(.*?)(</select>)',
               lambda m: m.group(1) + re.sub(r' selected', '', m.group(2))
               .replace('<option value="" disabled>', '<option value="" disabled>' if industry else '<option value="" disabled selected>')
               .replace(f'data-slug="{industry}"', f'data-slug="{industry}" selected') + m.group(3),
               f, flags=re.S)
    return f.replace('id="ix-', 'id="cs-').replace('for="ix-', 'for="cs-')


def contact_block(industry, name):
    return f'''<section class="sec sv-sec" style="border-top: 1px solid var(--line)" id="get-started">
<div class="wrap ix-two">
<div><span class="lbl"><span class="tri"></span>Your turn</span><h2 class="h2" style="font-size: clamp(36px,4.4vw,64px); margin-bottom: 20px">Find out where your budget <span class="cy">is leaking.</span></h2>
<p class="sub" style="max-width: 520px">Get a free Ad Spend Leak Check: a 10-minute video showing where your Google or Meta budget is leaking. In your inbox within 48 hours.</p>
<div style="margin-top: 40px">{awards}</div></div>
{form_for(industry, name)}
</div>
</section>'''


def page(title, desc, canonical, body, schema):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<link rel="canonical" href="{canonical}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0a090b">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="First Byte - Digital Marketing &amp; Advertising Agency">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{BASE}/og-image.png">
{icons}
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
{head_tail}
</head>
{body}
{footer}'''


def breadcrumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


cards = []
arts = {m.group(1): m.group(0) for m in re.finditer(r'<article id="stage-([a-z]+)".*?</article>', home, re.S)}
assert set(arts) == set(CASES), sorted(arts)

for key, (slug, name, industry, label) in CASES.items():
    art = arts[key]
    headline = strip_tags(re.search(r"<h3>(.*?)</h3>", art, re.S).group(1))
    chal = strip_tags(re.search(r'<p class="cs-chal">(.*?)</p>', art, re.S).group(1))
    ind_line = strip_tags(re.search(r'<span class="cs-ind">(.*?)</span>', art, re.S).group(1))
    mets = re.findall(r'<div class="met"><b[^>]*>(.*?)</b><span>(.*?)</span></div>', art)
    logo = re.search(r'<div class="cs-brand">(.*?)<span class="cs-ind">', art, re.S).group(1)  # <img> or inline <svg>
    # standalone article: no tab semantics, always visible, CTA without "full case study" link
    a = re.sub(r'<article id="stage-[a-z]+"[^>]*class="([^"]*)">',
               rf'<article id="story" class="\1" data-id="{key}">', art)
    a = re.sub(r'<a class="cs-more"[^>]*>.*?</a>', "", a)
    top = mets[0] if mets else ("", "")
    url = f"{BASE}/case-studies/{slug}/"
    title = f"{name} Case Study: {headline} | First Byte"
    desc = f"{chal} How First Byte did it" + (f": {strip_tags(top[0])} {strip_tags(top[1]).lower()}." if top[0] else ".")
    body = f'''{body_open}

<section class="sv-hero ix-hero" style="padding-bottom: 40px">
<div class="glow" style="width: 640px; height: 640px; left: -240px; top: -140px; background: #be00bb; opacity: .2"></div>
<div class="glow" style="width: 520px; height: 520px; right: -160px; top: 120px; background: #0054ff; opacity: .2"></div>
<div class="wrap">
<div class="sv-copy" style="max-width: 900px">
<p class="seo-h1" style="margin-bottom: 22px"><span class="tri"></span><a href="/case-studies/" style="color: inherit; text-decoration: none">Case studies</a> · {esc(ind_line)}</p>
<h1 class="sv-disp" style="font-size: clamp(44px,6vw,92px)">{esc(name)}: <span class="cy">{esc(headline)}</span></h1>
<p class="sub">{esc(chal)}</p>
<div class="cta-row"><a class="btn btn-p" href="#contact" data-industry="{industry}">Run a business like {esc(name)}? Get your Leak Check <span class="arr">→</span></a><a class="btn btn-g" href="/case-studies/">All case studies</a></div>
</div>
</div>
</section>

<section class="sec cases" style="padding-top: 20px">
<div class="wrap">
<div class="cs cs-solo">
{a}
</div>
</div>
</section>

{contact_block(industry, name)}
'''
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": f"{name}: {headline}", "description": desc, "url": url,
         "author": {"@type": "Organization", "name": "First Byte", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "First Byte", "url": BASE + "/"}},
        breadcrumbs([("Home", BASE + "/"), ("Case studies", BASE + "/case-studies/"), (name, url)])]}
    write(f"{SITE}/case-studies/{slug}/index.html", page(title, desc, url, body, schema))
    stat = f'<b class="csl-stat">{top[0]}</b><span class="csl-sl">{top[1]}</span>' if top[0] else ""
    cards.append(f'<a class="csl-card" href="/case-studies/{slug}/">{logo}<span class="csl-ind">{esc(ind_line)}</span>'
                 f'<h2>{esc(headline)}</h2>{stat}<span class="csl-go">Read the case study →</span></a>')

# ---- index page ----------------------------------------------------------------
idx_url = f"{BASE}/case-studies/"
idx_body = f'''{body_open}

<section class="sv-hero ix-hero" style="padding-bottom: 40px">
<div class="glow" style="width: 640px; height: 640px; left: -240px; top: -140px; background: #be00bb; opacity: .2"></div>
<div class="wrap">
<div class="sv-copy" style="max-width: 900px">
<h1 class="seo-h1"><span class="tri"></span>Case studies · First Byte</h1>
<p class="sv-disp">Demand we’ve <span class="cy">driven.</span></p>
<p class="sub">Eight brands, eight very different problems. Here’s what we did and what it produced.</p>
<div class="cta-row"><a class="btn btn-p" href="#contact">Get my free Ad Spend Leak Check <span class="arr">→</span></a></div>
</div>
</div>
</section>

<section class="sec" style="padding-top: 20px">
<div class="wrap">
<div class="csl-grid">
{"".join(cards)}
</div>
</div>
</section>

{contact_block("", "these brands")}
'''
idx_schema = {"@context": "https://schema.org", "@graph": [
    {"@type": "CollectionPage", "name": "First Byte case studies", "url": idx_url},
    breadcrumbs([("Home", BASE + "/"), ("Case studies", idx_url)])]}
write(f"{SITE}/case-studies/index.html",
      page("Case Studies | First Byte Digital Marketing Agency",
           "Results First Byte has driven for Equinox, Kroger, Celsius, Viceroy and more: the problem, what we did, and the numbers.",
           idx_url, idx_body, idx_schema))

# ---- point existing "featured case study" links at the new pages ---------------
SLUG = {k: v[0] for k, v in CASES.items()}
n = 0
for root, _, files in os.walk(SITE):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        p = os.path.join(root, fn)
        s = read(p)
        o = re.sub(r'href="/#work-([a-z]+)"', lambda m: f'href="/case-studies/{SLUG[m.group(1)]}/"' if m.group(1) in SLUG else m.group(0), s)
        if o != s:
            write(p, o)
            n += 1

# ---- sitemap ---------------------------------------------------------------------
sm_path = f"{SITE}/sitemap.xml"
sm = read(sm_path)
urls = [idx_url] + [f"{BASE}/case-studies/{v[0]}/" for v in CASES.values()]
missing = [u for u in urls if f"<loc>{u}</loc>" not in sm]
if missing:
    add = "".join(f"<url><loc>{u}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n" for u in missing)
    sm = sm.replace("</urlset>", add + "</urlset>")
    write(sm_path, sm)

print(f"built {len(CASES)} case study pages + index; relinked {n} pages; added {len(missing)} sitemap urls")
