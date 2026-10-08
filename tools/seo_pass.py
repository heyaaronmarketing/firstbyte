#!/usr/bin/env python3
"""SEO pass: title tags, meta descriptions, social tags, canonicals, robots and schema.

Targets local search in The Woodlands and Greater Houston. Idempotent: re-running it
changes nothing once applied, and it is safe to run after any page rebuild.

What it does
  * Sets <title>, meta description, og:/twitter: title + description, and the schema
    WebPage name/description from the TITLES / DESCS maps and the templates below.
    Titles stay at or under 60 characters; descriptions at or under 158.
  * Makes every canonical absolute; noindexes paginated legacy archives.
  * Widens the LocalBusiness areaServed with the two counties and Greater Houston.

Run from the repo root:  python3 tools/seo_pass.py
Then:                     python3 tools/seo_audit.py   (read-only report)
"""
import html
import json
import os
import re

ROOT = "site"
BASE = "https://firstbyte.agency"
BRAND = " | First Byte"

# ---------------------------------------------------------------------------------
# Page-specific titles (without the brand suffix; it is added when it fits in 60).
# ---------------------------------------------------------------------------------
TITLES = {
    "/": "The Woodlands & Houston Digital Marketing Agency | First Byte",  # brand kept on the homepage
    "/about/": "About First Byte | Marketing Agency in The Woodlands, TX",
    "/contact/": "Contact First Byte | Marketing Agency in The Woodlands",
    "/blog/": "Houston Marketing Blog: SEO, Ads & Local Growth",
    "/case-studies/": "Digital Marketing Case Studies & Results",
    "/services/": "Marketing Services in The Woodlands & Houston",
    "/services/search-marketing/": "Google Ads Agency in The Woodlands & Houston",
    "/services/paid-social-advertising/": "Paid Social Agency in The Woodlands & Houston",
    "/services/ctv-ooh-streaming-radio/": "CTV, Radio & Billboard Ads in Houston",
    "/services/creative-branding/": "Branding Agency in The Woodlands & Houston",
    "/services/web-design-seo-pr/": "Web Design Agency in The Woodlands & Houston",
    "/services/seo/": "SEO Company in The Woodlands & Houston",
    "/services/paid-advertising/": "PPC Agency in The Woodlands & Houston",
    "/services/public-relations/": "PR Agency in The Woodlands & Houston",
    "/service-areas/": "Service Areas: The Woodlands & Greater Houston",
    "/industries/": "Industries We Serve in The Woodlands & Houston",
    "/industries/service/": "Home Services Marketing in The Woodlands & Houston",
    "/industries/restaurants/": "Restaurant Marketing in The Woodlands & Houston",
    "/industries/sports-fitness/": "Gym & Fitness Marketing in Houston & The Woodlands",
    "/industries/hospitality/": "Hotel & Hospitality Marketing in Houston",
    "/industries/live-entertainment/": "Event & Ticket Sales Marketing in Houston",
    "/industries/ecommerce/": "eCommerce Marketing Agency in Houston",
    "/industries/beverage-spirits/": "Beverage & Spirits Marketing Agency in Houston",
    "/industries/technology/": "B2B & Tech Marketing Agency in Houston",
    "/industries/banking/": "Bank & Credit Union Marketing in Houston",
    "/industries/retail/": "Retail Marketing in The Woodlands & Houston",
    "/launch/": "Launch a Custom Website for $0 Down, $250/mo",
    "/terms-of-service/": "Terms of Service",
    "/work_tax/brand-development/": "Brand Development in The Woodlands & Houston",
    "/work_tax/influencer-marketing/": "Influencer Marketing Agency in Houston",
    "/work_tax/performance-marketing/": "Performance Marketing in The Woodlands & Houston",
    "/work_tax/web-design-development/": "Web Design & Development in The Woodlands",
    # ---- blog posts: shorter, local where it reads naturally -------------------
    "/blog/10-website-mistakes-costing-customers/": "10 Website Mistakes That Cost Small Businesses Customers",
    "/blog/2026-local-marketing-game-plan-woodlands/": "2026 Local Marketing Plan for The Woodlands Businesses",
    "/blog/ai-and-your-business-2026/": "AI for Small Businesses in 2026: What to Know",
    "/blog/ai-overviews-local-search-houston/": "AI Overviews & Local Search for Houston Businesses",
    "/blog/back-to-school-marketing-woodlands/": "Back-to-School Marketing for The Woodlands Businesses",
    "/blog/blogging-for-local-seo/": "Blogging for Local SEO: Does It Still Work in 2026?",
    "/blog/call-tracking-which-ads-make-phone-ring/": "Call Tracking: Know Which Ads Make the Phone Ring",
    "/blog/clicks-to-customers-conversion-funnel/": "From Clicks to Customers: Fix Your Conversion Funnel",
    "/blog/complete-guide-google-reviews/": "How to Get More Google Reviews: The Complete Guide",
    "/blog/content-marketing-service-businesses/": "Content Marketing for Service Businesses",
    "/blog/digital-marketing-cost-the-woodlands-houston/": "Digital Marketing Cost in Houston (2026 Guide)",
    "/blog/diy-vs-hiring-an-agency/": "DIY Marketing vs. Hiring an Agency in Houston",
    "/blog/facebook-instagram-ads-local-businesses/": "Do Facebook & Instagram Ads Work for Local Businesses?",
    "/blog/facebook-vs-instagram-vs-tiktok-local-business/": "Facebook vs. Instagram vs. TikTok for Local Businesses",
    "/blog/find-the-right-influencers/": "How to Find Houston Influencers for Your Business",
    "/blog/ftc-rules-influencer-partnerships/": "FTC Influencer Rules: What Businesses Must Know",
    "/blog/geo-fencing-ads-target-customers-nearby/": "Geo-Fencing Ads: Reach Customers Near Your Store",
    "/blog/get-found-near-me-google/": "How to Show Up in \"Near Me\" Searches on Google",
    "/blog/google-ads-cost-per-click-houston-benchmarks/": "Google Ads Cost in Houston: CPC by Industry",
    "/blog/google-business-profile-number-one-asset/": "Google Business Profile: Your #1 Local Marketing Asset",
    "/blog/google-business-profile-suspended-reinstatement/": "Google Business Profile Suspended? How to Fix It",
    "/blog/holiday-marketing-checklist/": "Holiday Marketing Checklist for Houston Businesses",
    "/blog/how-fast-should-your-website-load/": "How Fast Should Your Website Load? Core Web Vitals",
    "/blog/how-much-does-a-website-cost-the-woodlands/": "How Much Does a Website Cost in The Woodlands? (2026)",
    "/blog/local-seo-checklist-the-woodlands/": "Local SEO Checklist for The Woodlands Businesses",
    "/blog/local-services-ads-vs-google-ads-home-services/": "Local Services Ads vs. Google Ads for Home Services",
    "/blog/marketing-that-pays-for-itself/": "Marketing That Pays for Itself: The First Byte Approach",
    "/blog/marketing-your-business-spring-tx/": "Marketing Your Business in Spring, TX",
    "/blog/measure-marketing-success-metrics/": "How to Measure Marketing Success: Metrics That Matter",
    "/blog/measuring-influencer-marketing-roi/": "How to Measure Influencer Marketing ROI",
    "/blog/micro-influencers-vs-big-names/": "Micro-Influencers vs. Big Names for Local Brands",
    "/blog/mobile-first-design-houston-service-businesses/": "Mobile-First Web Design for Houston Service Businesses",
    "/blog/power-of-local-landing-pages/": "Local Landing Pages for Every Service Area",
    "/blog/psychology-of-logos/": "The Psychology of Logos: What Yours Says About You",
    "/blog/questions-before-hiring-marketing-agency/": "Questions to Ask Before Hiring a Houston Marketing Agency",
    "/blog/rank-in-google-map-pack-houston/": "How to Rank in the Google Map Pack in Houston",
    "/blog/reaching-customers-conroe-montgomery/": "Marketing in Conroe & Montgomery County, TX",
    "/blog/retargeting-explained/": "Retargeting Explained: Turn Visitors Into Customers",
    "/blog/seasonal-marketing-greater-houston/": "Seasonal Marketing Calendar for Greater Houston",
    "/blog/seo-vs-paid-ads-woodlands-business/": "SEO vs. Paid Ads for The Woodlands Businesses",
    "/blog/set-a-marketing-budget-small-business/": "How to Set a Small Business Marketing Budget",
    "/blog/signs-your-website-needs-a-redesign/": "7 Signs Your Business Website Needs a Redesign",
    "/blog/small-business-guide-google-ads-2026/": "Google Ads for Small Businesses: 2026 Guide",
    "/blog/small-business-marketing-ideas-the-woodlands/": "25 Small Business Marketing Ideas for The Woodlands",
    "/blog/social-proof-reviews-testimonials/": "Using Reviews & Testimonials on Your Website",
    "/blog/standing-out-houston-competitive-market/": "How to Stand Out in Houston's Competitive Market",
    "/blog/streaming-tv-ads-worth-it-small-business/": "Are Streaming TV (CTV) Ads Worth It in Houston?",
    "/blog/the-woodlands-businesses-win-local-search/": "How The Woodlands Businesses Win Local Search",
    "/blog/turn-your-website-into-a-lead-machine/": "How to Turn Your Website Into a Lead Machine",
    "/blog/ugc-vs-influencers-creator-content/": "UGC vs. Influencers: Which Creator Content Sells?",
    "/blog/understanding-cost-per-lead/": "Cost Per Lead: What's Good and How to Lower It",
    "/blog/website-accessibility-matters/": "Website Accessibility: Why It Matters for SEO",
    "/blog/website-copy-that-sells/": "How to Write Website Copy That Sells",
    "/blog/what-is-a-brand-really/": "What Is a Brand, Really? (It's More Than a Logo)",
    "/blog/what-makes-a-homepage-convert/": "What Makes a Homepage Convert?",
    "/blog/why-local-businesses-outrank-national-brands/": "Why Local Businesses Outrank National Brands",
}

DESCS = {
    "/": "First Byte is a digital marketing agency in The Woodlands serving Houston: Google Ads, paid social, SEO and web design that drive leads. Free Leak Check.",
    "/contact/": "Contact First Byte, a digital marketing agency in The Woodlands, TX. Call (713) 578-0634 or get a free Ad Spend Leak Check. We reply within 1 hour.",
    "/blog/": "Marketing playbooks for Houston and The Woodlands businesses: Google Ads costs, local SEO, Google Business Profile, paid social and AI search.",
    "/case-studies/": "Results First Byte drove for Equinox, Kroger, Celsius, Viceroy and Houston-area brands: the problem, what we did, and the numbers.",
    "/services/": "Google Ads, paid social, SEO, web design, branding and CTV for businesses in The Woodlands and Greater Houston, from one senior team.",
    "/services/search-marketing/": "Google Ads, Local Services Ads and Shopping managed by a senior team in The Woodlands. More calls and sales across Houston. Free Leak Check.",
    "/services/paid-social-advertising/": "Facebook, Instagram and TikTok ads that sell, from a senior team in The Woodlands serving Houston. Creative, targeting and tracking included.",
    "/services/ctv-ooh-streaming-radio/": "Streaming TV, streaming audio and digital billboard campaigns targeted by ZIP code across Houston and The Woodlands, measured to sales.",
    "/services/creative-branding/": "Brand identity, ad creative and video from a branding agency in The Woodlands. Built to stand out in Houston and convert on every channel.",
    "/services/web-design-seo-pr/": "Fast, conversion-focused websites, local SEO and PR for businesses in The Woodlands and Houston. Built to rank and turn visitors into leads.",
    "/services/seo/": "Local SEO and Google Business Profile optimization for businesses in The Woodlands and Houston. Rank in the map pack and get more calls.",
    "/services/paid-advertising/": "PPC and paid advertising on Google, Meta, TikTok and more for businesses in The Woodlands and Houston. Managed to cost per lead, not clicks.",
    "/services/public-relations/": "Public relations and media outreach for brands in The Woodlands and Houston: press coverage, launches and reputation that support search.",
    "/industries/": "Marketing for home services, healthcare, restaurants, fitness, hospitality, events, eCommerce and tech brands across The Woodlands and Houston.",
    "/industries/service/": "Local Services Ads, Google Ads and map-pack SEO for HVAC, plumbing, dental, med spa and law firms in The Woodlands and Houston. More booked jobs.",
    "/industries/restaurants/": "Restaurant marketing in The Woodlands and Houston: grand openings, Google Maps rankings, creators and paid social that fill tables.",
    "/industries/sports-fitness/": "Gym and fitness marketing for Houston and The Woodlands: presale campaigns, founding-member offers and paid social that sell memberships.",
    "/industries/hospitality/": "Hotel and resort marketing from Houston: paid search, social, CTV and OOH campaigns that grow direct bookings and cut OTA fees.",
    "/industries/live-entertainment/": "Ticket sales marketing for touring shows, festivals and venues from our Houston-area team. Paid social, search and creators that sell out dates.",
    "/industries/ecommerce/": "eCommerce and CPG marketing from Houston: paid social, Shopping ads, creators and retail activation that grow DTC and in-store sales.",
    "/industries/beverage-spirits/": "Beverage and spirits marketing from Houston: creators, retail activation and geo-targeted ads that drive velocity at the shelf.",
    "/industries/technology/": "B2B and technology marketing from Houston: positioning, websites and paid search and LinkedIn programs that build qualified pipeline.",
    "/industries/banking/": "Marketing for banks and credit unions in Houston and The Woodlands: compliant paid search, social and local SEO that open new accounts.",
    "/industries/retail/": "Retail marketing in The Woodlands and Houston: local inventory ads, Google Maps, paid social and creators that drive store visits.",
    "/launch/": "Get a custom, conversion-ready website for $0 down and $250 a month, all-in. Built by First Byte in The Woodlands, TX in days, not months.",
    "/work_tax/brand-development/": "Brand development work by First Byte in The Woodlands: identities, packaging and launch creative for brands across Houston and beyond.",
    "/work_tax/influencer-marketing/": "Influencer marketing campaigns by First Byte: Houston creators and national talent that drive sales, not just likes.",
    "/work_tax/performance-marketing/": "Performance marketing work by First Byte in The Woodlands: paid search and social campaigns measured to revenue for Houston brands.",
    "/work_tax/web-design-development/": "Web design and development work by First Byte in The Woodlands: fast, conversion-focused sites for Houston-area businesses.",
}

GEO_SERVICES = {  # url prefix -> (display name, phrase used mid-sentence, title noun)
    "seo": ("SEO", "local SEO", "SEO Company"),
    "paid-advertising": ("Paid Advertising", "Google and social ads", "PPC & Paid Ads"),
    "web-design": ("Web Design", "web design", "Web Design"),
    "brand-development": ("Brand Development", "branding", "Branding Agency"),
    "influencer-marketing": ("Influencer Marketing", "influencer marketing", "Influencer Marketing"),
    "performance-marketing": ("Performance Marketing", "performance marketing", "Performance Marketing"),
    "public-relations": ("Public Relations", "PR", "PR Agency"),
}
CITY_FIX = {"Oak Ridge North": "Oak Ridge North", "Sugar Land": "Sugar Land", "New Caney": "New Caney"}

EXTRA_AREAS = [
    {"@type": "AdministrativeArea", "name": "Montgomery County, TX"},
    {"@type": "AdministrativeArea", "name": "Harris County, TX"},
    {"@type": "AdministrativeArea", "name": "Greater Houston"},
]


def city_from_slug(slug):
    return " ".join(w.capitalize() for w in slug.split("-"))


def with_brand(t):
    if t.endswith(BRAND):
        return t
    return t + BRAND if len(t + BRAND) <= 60 else t


def clip(s, n=158):
    if len(s) <= n:
        return s
    cut = s[: n - 1].rsplit(" ", 1)[0].rstrip(",;:—-")
    return cut + "…"


def esc_attr(s):
    return html.escape(s, quote=True)


def geo_title_desc(url):
    m = re.match(r"^/digital-marketing-agency-([a-z-]+)-tx/$", url)
    if m:
        city = city_from_slug(m.group(1))
        d = (f"Digital marketing agency serving {city}, TX: Google Ads, paid social, local SEO and web design "
             f"from a senior team in The Woodlands. Free Leak Check.")
        return None, d
    for key, (name, phrase, noun) in GEO_SERVICES.items():
        m = re.match(rf"^/{key}-([a-z-]+)-tx/$", url)
        if m:
            city = city_from_slug(m.group(1))
            t = f"{noun} in {city}, TX"
            d = (f"{name} for {city}, TX businesses from First Byte, a senior marketing team based in "
                 f"The Woodlands. More calls and customers. Free Ad Spend Leak Check.")
            if len(d) > 158:
                d = f"{name} for {city}, TX businesses from First Byte in The Woodlands. More calls and customers. Free Ad Spend Leak Check."
            return t, d
    return None, None


def set_meta(s, title, desc):
    if title:
        s = re.sub(r"<title>.*?</title>", lambda _: f"<title>{html.escape(title, quote=False)}</title>", s, count=1, flags=re.S)
        for prop in ('property="og:title"', 'name="twitter:title"'):
            s = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc_attr(title) + m.group(2), s)
    if desc:
        for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
            s = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc_attr(desc) + m.group(2), s)
    return s


def fix_schema(s, url, title, desc):
    def edit(m):
        raw = m.group(2)
        try:
            data = json.loads(raw)
        except Exception:
            return m.group(0)
        changed = False
        nodes = data.get("@graph", [data]) if isinstance(data, dict) else []
        for n in nodes:
            if not isinstance(n, dict):
                continue
            t = n.get("@type")
            if t in ("WebPage", "AboutPage", "ContactPage", "CollectionPage"):
                if title and n.get("name") != title:
                    n["name"] = title; changed = True
                if desc and "description" in n and n["description"] != desc:
                    n["description"] = desc; changed = True
            if t == "ProfessionalService" and isinstance(n.get("areaServed"), list):
                names = {a.get("name") for a in n["areaServed"] if isinstance(a, dict)}
                for a in EXTRA_AREAS:
                    if a["name"] not in names:
                        n["areaServed"].append(a); changed = True
        if not changed:
            return m.group(0)
        return m.group(1) + "\n" + json.dumps(data, ensure_ascii=False, indent=1) + "\n" + m.group(3)
    return re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', edit, s, flags=re.S)


# Eyebrow-style H1s (class="seo-h1") that should name the service and the market.
H1S = {
    "/services/creative-branding/": "Creative &amp; Branding Agency · The Woodlands &amp; Houston",
    "/services/search-marketing/": "Google Ads &amp; Search Marketing Agency · The Woodlands &amp; Houston",
    "/services/paid-social-advertising/": "Paid Social Advertising Agency · The Woodlands &amp; Houston",
    "/services/ctv-ooh-streaming-radio/": "CTV, Streaming Radio &amp; Digital Billboard Ads · Houston",
    "/services/web-design-seo-pr/": "Web Design, SEO &amp; PR Agency · The Woodlands &amp; Houston",
    "/blog/": "Marketing Blog for Houston &amp; The Woodlands Businesses",
    "/case-studies/": "Digital Marketing Case Studies · First Byte, The Woodlands TX",
    "/contact/": "Contact First Byte · Digital Marketing Agency in The Woodlands, TX",
}


def set_h1(s, url):
    new = H1S.get(url)
    if not new:
        return s
    return re.sub(r'(<h1 class="seo-h1"><span class="tri"></span>)(.*?)(</h1>)', lambda m: m.group(1) + new + m.group(3), s, count=1, flags=re.S)


CRUMB_NAMES = {
    "/contact/": "Contact", "/industries/": "Industries", "/services/": "Services",
    "/terms-of-service/": "Terms of Service",
    "/work_tax/brand-development/": "Brand Development", "/work_tax/influencer-marketing/": "Influencer Marketing",
    "/work_tax/performance-marketing/": "Performance Marketing", "/work_tax/web-design-development/": "Web Design & Development",
}


def add_breadcrumbs(s, url):
    """Indexable pages without a BreadcrumbList get Home > Page."""
    if url == "/" or "BreadcrumbList" in s or 'content="noindex' in s or url not in CRUMB_NAMES:
        return s
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": CRUMB_NAMES[url], "item": BASE + url}]}
    block = '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1) + "\n</script>\n"
    return s.replace("</head>", block + "</head>", 1)


def main():
    changed = 0
    for r, _, fs in os.walk(ROOT):
        for f in fs:
            if not f.endswith(".html"):
                continue
            p = os.path.join(r, f)
            rel = "/" + os.path.relpath(p, ROOT).replace(os.sep, "/")
            url = rel[:-10] if rel.endswith("/index.html") else rel
            src = open(p, encoding="utf-8").read()
            s = src

            title = TITLES.get(url)
            desc = DESCS.get(url)
            gt, gd = geo_title_desc(url)
            title = title or gt
            desc = desc or gd
            if title:
                title = with_brand(title)
            if desc:
                desc = clip(desc)
            s = set_meta(s, title, desc)

            # any remaining description over 158 characters gets trimmed at a word boundary
            def trim(m):
                v = html.unescape(m.group(2))
                return m.group(1) + esc_attr(clip(v)) + m.group(3) if len(v) > 158 else m.group(0)
            s = re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")([^"]*)(")', trim, s)

            # absolute canonicals
            s = re.sub(r'(<link rel="canonical" href=")(/[^"]*)(")', lambda m: m.group(1) + BASE + m.group(2) + m.group(3), s)
            # paginated legacy archives: keep out of the index
            if re.match(r"^/work_tax/[^/]+/page/\d+/$", url) and 'content="noindex' not in s:
                if '<meta name="robots"' in s:
                    s = re.sub(r'<meta name="robots" content="[^"]*"\s*/?>', '<meta name="robots" content="noindex, follow">', s)
                else:
                    s = s.replace("</head>", '<meta name="robots" content="noindex, follow">\n</head>', 1)

            s = fix_schema(s, url, title, desc)
            s = add_breadcrumbs(s, url)
            s = set_h1(s, url)

            if s != src:
                open(p, "w", encoding="utf-8").write(s)
                changed += 1
    print(f"seo pass: updated {changed} files")


if __name__ == "__main__":
    main()
