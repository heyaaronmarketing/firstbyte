"""Blog SEO pass (Nov 27, 2026 audit). Idempotent; runs at the end of seo_fixes_oct_2026.py.

1. Topic hubs: /topics/<slug>/ pages that group every post into one of 12 clusters (industries + channels),
   each with an intro, links to the matching service/industry pages, and CollectionPage + ItemList +
   BreadcrumbList schema. The blog index chips link to them.
2. One consistent category per post: card labels, the post's category pill (now a link to its hub) and the
   BlogPosting articleSection all use the hub name. BreadcrumbList becomes Home > Blog > Topic > Post.
   (Fixes the old "SEO & AI search" / "SEO &amp; AI search" split and the Websites / Web design split.)
3. Blog index: Blog schema with the 20 newest posts.
4. BlogPosting.wordCount filled in from the article text where missing.
5. Meta descriptions rewritten for older pages that were under ~110 characters.
6. Sitemap lastmod uses real dates (post dateModified, newest post per hub, git history for other pages)
   instead of stamping every URL with today's date; topic hubs are added to the sitemap and llms.txt.
Run: python3 tools/seo_topics_nov_2026.py
"""
import glob
import html
import json
import os
import re
import subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITE = os.path.join(ROOT, "site")
BASE = "https://firstbyte.agency"
ORG = BASE + "/#organization"

# (slug, short label, page title (<=60 incl. brand), H1, meta description, intro, [(href, text)], slug regex)
HUBS = [
    ("houston-local-guides", "Houston local guides", "Houston & The Woodlands Marketing Guides | First Byte",
     "Local marketing guides for Houston and The Woodlands",
     "Local marketing guides for Houston and The Woodlands businesses: sign rules, growth areas, seasonal calendars, local PR, chambers and community marketing.",
     "Guides that only make sense here. Township sign rules, which Houston suburbs are adding customers fastest, how rodeo season and hurricane season change what you should run, and how to get local press, chambers and sponsorships working for you. If your customers live between Conroe and Sugar Land, start with these.",
     [("/service-areas/", "Areas we serve"), ("/digital-marketing-agency-houston-tx/", "Houston digital marketing")],
     r"growth-corridors|marketing-your-business-(spring|katy)|reaching-customers-conroe|rodeo|hurricane|asian-american|hispanic|sign-rules|chambers|press-coverage|sponsorships|address-local-seo|questions-answered|standing-out-houston|woodlands-businesses-win|local-marketing-game-plan|seasonal-marketing-greater|back-to-school|new-mover|eddm|marketing-calendar|trade-show|small-business-marketing-ideas-the-woodlands|grand-opening|holiday-marketing"),
    ("healthcare-marketing", "Healthcare", "Healthcare & Medical Practice Marketing Guides | First Byte",
     "Healthcare and medical practice marketing in Houston",
     "Marketing guides for Houston and The Woodlands healthcare practices: dental, med spa, therapy, PT, dermatology, senior care and HIPAA-safe tracking.",
     "Patients pick a provider the way they pick anything else now: a search, a map, a few reviews and a website that answers their question. These guides cover what works for dental, medical, med spa, therapy, physical therapy, senior care and veterinary practices across Houston and The Woodlands, including the privacy rules that change how you can track and advertise.",
     [("/services/search-marketing/", "Search marketing"), ("/services/web-design-seo-pr/", "Websites & SEO")],
     r"dental|medical|chiropract|med-spa|therap|dermatolog|plastic-surgeon|optometr|orthodont|urgent-care|hearing|hospice|home-care|senior-living|weight-loss|iv-therapy|acupuncture|veterinar|hipaa|clinic"),
    ("fitness-beauty-studios", "Fitness & beauty", "Gym, Salon & Studio Marketing Guides | First Byte",
     "Gym, fitness, beauty and studio marketing in Houston",
     "Marketing guides for gyms, fitness studios, salons, spas and lesson studios in Houston and The Woodlands: presales, memberships, bookings and reviews.",
     "Memberships, class packs and recurring bookings live or die on local search and social. These guides cover presale launches, founding-member offers, booking flows, reviews and paid social for gyms, Pilates and yoga studios, martial arts and dance, salons, lash and massage businesses around Houston and The Woodlands.",
     [("/industries/sports-fitness/", "Sports & fitness marketing"), ("/services/paid-social-advertising/", "Paid social")],
     r"salon|lash|massage|esthetician|gym|fitness|pilates|yoga|martial-arts|dance-studio|cryotherapy|music-lessons"),
    ("restaurants-hospitality-events", "Restaurants & events", "Restaurant, Hotel & Event Marketing Guides | First Byte",
     "Restaurant, hospitality and event marketing in Houston",
     "Marketing guides for Houston and The Woodlands restaurants, hotels, venues, caterers and event promoters: direct orders, bookings and ticket sales.",
     "Covers, room nights and tickets all depend on being found at the moment someone decides. These guides cover direct online ordering, Google Maps, creators and paid social for restaurants and cafes, direct bookings for hotels and rentals, and ticket sales for shows, festivals and venues around Houston.",
     [("/industries/restaurants/", "Restaurant marketing"), ("/industries/hospitality/", "Hospitality marketing"), ("/industries/live-entertainment/", "Live events marketing")],
     r"restaurant|bakery|catering|food-truck|brewery|hotel|wedding|event|ticket|party|short-term-rental"),
    ("retail-ecommerce-auto", "Retail & eCommerce", "Retail, eCommerce & Auto Marketing Guides | First Byte",
     "Retail, eCommerce, CPG and auto marketing",
     "Marketing guides for eCommerce brands, CPG and retail stores, and auto businesses in Houston: Shopping ads, Meta creative, email flows and store traffic.",
     "Selling a product, online or off a shelf, is a different game from booking a service call. These guides cover Shopping ads, Meta creative testing, Klaviyo flows, retail sell-through at Kroger and H-E-B, and local marketing for boutiques, dealerships, car washes, storage and auto shops.",
     [("/industries/ecommerce/", "eCommerce & CPG marketing"), ("/industries/beverage-spirits/", "Beverage marketing")],
     r"ecommerce|shopify|cpg|boutique|beverage|car-dealership|boat-dealer|car-wash|klaviyo|self-storage|auto-detailing|collision|auto-repair"),
    ("professional-services-b2b", "Professional services", "Professional Services & B2B Marketing Guides | First Byte",
     "Professional services and B2B marketing in Houston",
     "Marketing guides for Houston law firms, CPAs, advisors, agents, schools, nonprofits and B2B companies: SEO, Google Ads, LinkedIn and referrals.",
     "When one client is worth thousands, the marketing has to earn trust before it earns a call. These guides cover law firms, accounting and financial firms, insurance and mortgage, real estate and property management, schools and childcare, nonprofits, and B2B companies selling into Houston's energy and industrial base.",
     [("/industries/technology/", "B2B & technology marketing"), ("/services/search-marketing/", "Search marketing")],
     r"law-firm|cpa|financial-advisor|insurance|mortgage|real-estate|property-management|staffing|b2b|linkedin|interior-designer|photographer|funeral|daycare|private-school|tutoring|nonprofit|ad-grants"),
    ("home-services-marketing", "Home services", "Home Service Marketing Guides for Houston | First Byte",
     "Home service marketing in Houston and The Woodlands",
     "Marketing guides for Houston and The Woodlands home service companies: HVAC, plumbing, roofing, remodeling, pools, landscaping, cleaning and more.",
     "Booked jobs come from three places: the map pack, Local Services Ads and a website that turns a visit into a call. These guides break that down trade by trade for HVAC, plumbing, roofing, electrical, remodeling, pools, landscaping, cleaning, pest control and the rest of Houston's home service businesses.",
     [("/industries/service/", "Home service marketing"), ("/services/search-marketing/", "Google Ads & LSA management")],
     r"hvac|plumb|roofing|electrician|pest|lawn|landscap|pool|fence|garage-door|foundation|remodel|kitchen-bath|painting|concrete|tree-service|junk|moving|cleaning-business|commercial-cleaning|pressure-washing|irrigation|appliance|flooring|countertop|solar|water-damage|locksmith|home-builder|home-inspector|outdoor-living|angi|contractor|dog-|window-door"),
    ("google-ads", "Google Ads", "Google Ads Guides for Houston Businesses | First Byte",
     "Google Ads guides for Houston businesses",
     "Google Ads guides for Houston and The Woodlands businesses: costs and CPC benchmarks, Local Services Ads, Performance Max, tracking and fixing campaigns.",
     "What Google Ads costs in Houston, how to set it up so the phone rings, and how to fix it when it doesn't. Covers search campaigns, Local Services Ads, Performance Max, YouTube, call and form tracking, click fraud and account suspensions.",
     [("/services/search-marketing/", "Google Ads management")],
     r"google-ads|performance-max|local-services-ads|microsoft-ads|google-shopping|youtube|geo-fencing|google-guaranteed|call-tracking|cost-per-click|cost-per-lead"),
    ("seo-local-search", "SEO & local search", "SEO & Local Search Guides for Houston | First Byte",
     "SEO and local search guides for Houston businesses",
     "SEO guides for Houston and The Woodlands businesses: Google Business Profile, map pack rankings, reviews, local landing pages and AI search.",
     "How to show up when someone nearby searches for what you sell: Google Business Profile, the map pack, reviews, local landing pages, SEO costs and timelines, and the newer question of getting recommended by AI Overviews and ChatGPT.",
     [("/services/web-design-seo-pr/", "SEO services")],
     r"seo|google-business|map-pack|near-me|reviews|ai-overviews|chatgpt|blogging|local-search|outrank|landing-pages|fake-reviews|showing-up-on-google|change-business-address"),
    ("social-media-influencer", "Social & influencer", "Social Media & Influencer Marketing Guides | First Byte",
     "Social media, influencer and email marketing guides",
     "Paid social, influencer, email and SMS guides for Houston and The Woodlands businesses: Meta and TikTok ads, lead quality, creators and the rules.",
     "Facebook, Instagram and TikTok ads, creators and influencers, retargeting, email and text marketing, plus the rules that keep you out of trouble (FTC disclosures, Texas SMS law) and what to do when an ad account gets restricted.",
     [("/services/paid-social-advertising/", "Paid social advertising")],
     r"facebook|instagram|tiktok|influencer|ugc|nextdoor|meta-|retargeting|social-media|yelp|sms|email"),
    ("websites-branding", "Websites & branding", "Website & Branding Guides for Houston | First Byte",
     "Website and branding guides for Houston businesses",
     "Website and branding guides for Houston and The Woodlands businesses: website costs, redesigns, speed, copy, platforms, logos and brand identity.",
     "What a website should cost, when it needs a redesign, how fast it has to load, what to write on it, and who should own the domain. Plus branding: logos, colors, voice, video and rebrands that don't confuse the customers you already have.",
     [("/services/web-design-seo-pr/", "Web design"), ("/services/creative-branding/", "Creative & branding")],
     r"website|homepage|brand|logo|domain|wordpress|copy|mobile-first|rebrand|video-production|conversion-funnel|load"),
    ("marketing-strategy-budgets", "Strategy & budgets", "Marketing Strategy, Budget & Agency Guides | First Byte",
     "Marketing strategy, budgets and hiring an agency",
     "Marketing strategy guides for Houston and The Woodlands owners: budgets, costs, measuring ROI, billboards and TV, and how to hire or fire an agency.",
     "The decisions above the channel: how much to spend, what marketing should cost in Houston, which numbers to watch, when traditional media like billboards, radio and streaming TV make sense, and how to choose, contract with or leave a marketing agency.",
     [("/contact/", "Talk to a strategist"), ("/services/ctv-ooh-streaming-radio/", "Streaming TV, radio & billboards")],
     r".*"),
]
HUB_BY_SLUG = {h[0]: h for h in HUBS}


def hub_for(slug):
    for h in HUBS:
        if re.search(h[7], slug):
            return h
    return HUBS[-1]


DESCS = {
    "/blog/ai-and-your-business-2026/": "What AI changes for Houston small businesses in 2026: AI search and Overviews, AI ad tools, content and where human judgment still beats automation.",
    "/blog/signs-your-website-needs-a-redesign/": "Seven signs your business website needs a redesign, from slow mobile load times to dead forms, and how Houston businesses can fix them without losing rankings.",
    "/blog/how-to-rebrand-without-losing-customers/": "How to rebrand a local business without confusing loyal customers or losing Google rankings: planning, rollout order, redirects and announcing the change.",
    "/case-studies/ionstream/": "ionstream case study: how First Byte built $38M in qualified B2B pipeline with positioning, a new website and paid search and LinkedIn programs.",
    "/case-studies/celsius/": "Celsius case study: how First Byte drove a 41% lift in sell-through in target regions with creators, retail activation and geo-targeted ads.",
    "/case-studies/the-toasted-yolk-cafe/": "Toasted Yolk Cafe case study: how First Byte helped launch seven new locations with grand-opening campaigns, local SEO and paid social.",
    "/blog/google-business-profile-number-one-asset/": "Why your Google Business Profile is your most valuable local marketing asset, and the settings, photos, posts and reviews that make it bring in calls.",
    "/blog/set-a-marketing-budget-small-business/": "How to set a small business marketing budget: percent-of-revenue benchmarks, working back from cost per lead, and splitting spend across channels.",
    "/blog/what-makes-a-homepage-convert/": "What makes a small business homepage convert visitors into leads: the headline, proof, calls to action and page speed that matter most on mobile.",
    "/blog/local-seo-checklist-the-woodlands/": "A practical local SEO checklist for businesses in The Woodlands: Google Business Profile, citations, reviews, local pages and tracking, step by step.",
    "/blog/mobile-first-design-houston-service-businesses/": "Mobile-first web design for Houston service businesses: tap-to-call, fast load times, short forms and layouts built for customers searching on a phone.",
    "/blog/marketing-your-business-spring-tx/": "How to market a business in Spring, TX: local SEO for Spring and Klein ZIP codes, Google Ads targeting, community events and growth along the Grand Parkway.",
    "/blog/psychology-of-logos/": "The psychology of logos: how shape, color and type shape first impressions, and what makes a small business logo memorable, trusted and easy to use.",
    "/blog/clicks-to-customers-conversion-funnel/": "How to turn website clicks into customers: find where your conversion funnel leaks, fix landing pages and forms, and follow up on leads faster.",
    "/blog/get-found-near-me-google/": "How to show up in \"near me\" searches on Google: Google Business Profile categories, proximity, reviews and local pages that put you in the results.",
    "/blog/marketing-that-pays-for-itself/": "How First Byte plans marketing that pays for itself: start from customer value and cost per lead, track every call and form, and cut what doesn't return.",
    "/blog/spring-cleaning-your-digital-marketing/": "A yearly digital marketing cleanup for small businesses: Google Business Profile, website, tracking, ad accounts, logins and listings to review.",
    "/blog/show-up-in-chatgpt-ai-search-aeo/": "How to show up in ChatGPT, Google AI Overviews and other AI search: answer engine optimization (AEO) steps for Houston and The Woodlands businesses.",
    "/blog/10-website-mistakes-costing-customers/": "Ten common small business website mistakes that send customers to competitors, from slow pages and hidden phone numbers to weak calls to action.",
    "/blog/questions-before-hiring-marketing-agency/": "The questions to ask before hiring a Houston marketing agency: who does the work, who owns the accounts, how results are reported and what it costs.",
    "/blog/standing-out-houston-competitive-market/": "How small businesses stand out in Houston's crowded market: pick a niche, own your neighborhoods in local search, and give people a reason to choose you.",
    "/blog/2026-local-marketing-game-plan-woodlands/": "A prioritized 2026 local marketing plan for businesses in The Woodlands: what to fix first, which channels to fund and how to track it month by month.",
    "/blog/complete-guide-google-reviews/": "How to get more Google reviews the right way: when and how to ask, review request scripts, responding to negative reviews and what Google prohibits.",
    "/blog/the-woodlands-businesses-win-local-search/": "How businesses in The Woodlands win local search: map pack rankings by village, reviews, local pages and content that competitors in Spring and Conroe skip.",
    "/blog/turn-your-website-into-a-lead-machine/": "How to turn a small business website into a lead machine: clear offers, calls to action on every page, fast forms, tracking and quick follow-up.",
    "/blog/back-to-school-marketing-woodlands/": "Back-to-school marketing for businesses in The Woodlands and Conroe ISD: timing, offers and ads that catch parents as routines and budgets reset.",
    "/blog/blogging-for-local-seo/": "Does blogging still help local SEO in 2026? What to write, how often, and how Houston service businesses turn blog posts into rankings and leads.",
    "/blog/email-marketing-basics/": "Email marketing basics for small businesses: building a list, welcome and follow-up emails, what to send, how often, and the numbers to track.",
    "/blog/facebook-instagram-ads-local-businesses/": "Do Facebook and Instagram ads work for local businesses? When they do, which campaign types to use, and how Houston businesses target nearby customers.",
    "/blog/power-of-local-landing-pages/": "Why service-area businesses need local landing pages, how to write city pages that rank without being duplicates, and how many to build.",
    "/blog/measure-marketing-success-metrics/": "The marketing metrics that tell you if it's working: cost per lead, cost per customer, close rate and return on ad spend, and how to track them.",
    "/blog/micro-influencers-vs-big-names/": "Micro-influencers vs. big-name creators for local brands: reach, cost, trust and results, and how Houston businesses choose the right size partner.",
    "/blog/rank-in-google-map-pack-houston/": "How to rank in the Google map pack in Houston: relevance, distance and prominence, Google Business Profile settings, reviews and local links that help.",
    "/blog/retargeting-explained/": "Retargeting explained: how ads follow website visitors on Google, Facebook and Instagram, what it costs, and how local businesses use it to win back leads.",
    "/blog/what-is-a-brand-really/": "What a brand really is, beyond the logo: the promise, voice, visuals and customer experience that make a local business recognizable and trusted.",
    "/blog/why-local-businesses-outrank-national-brands/": "Why local businesses can outrank national brands in local search: proximity, reviews, local content and Google Business Profile signals you control.",
    "/blog/holiday-marketing-checklist/": "A holiday marketing checklist for Houston businesses: when to start, offers, Google Business Profile hours, ads, email and gift card promotions.",
    "/blog/how-fast-should-your-website-load/": "How fast should a business website load? Core Web Vitals targets (LCP, INP, CLS), how to test your site, and fixes that speed up slow pages.",
    "/blog/brand-voice-sound-like-you/": "How to define a brand voice and keep it consistent across your website, ads, social and emails, with examples and a simple voice guide template.",
    "/blog/diy-vs-hiring-an-agency/": "DIY marketing vs. hiring an agency in Houston: what you can do yourself, signs you've outgrown it, and the true cost of each option.",
    "/blog/measuring-influencer-marketing-roi/": "How to measure influencer marketing ROI: tracking links, discount codes, lift in branded search and sales, and what a good return looks like.",
    "/blog/website-copy-that-sells/": "How to write website copy that sells: headlines, service pages, proof and calls to action that turn visitors into calls for local businesses.",
    "/blog/content-marketing-service-businesses/": "Content marketing for service businesses: what to publish, how to turn customer questions into posts and videos, and how it brings in leads.",
    "/blog/ftc-rules-influencer-partnerships/": "FTC influencer rules for businesses: disclosure requirements, #ad and paid partnership labels, contracts and how to keep creator campaigns compliant.",
    "/blog/seasonal-marketing-greater-houston/": "A seasonal marketing calendar for Greater Houston businesses: heat, hurricanes, rodeo, holidays and school calendars, and what to run when.",
    "/blog/website-accessibility-matters/": "Why website accessibility matters for small businesses: ADA risk, SEO benefits, WCAG basics and quick fixes for contrast, alt text, forms and menus.",
    "/blog/reaching-customers-conroe-montgomery/": "How to market a business in Conroe and Montgomery County, TX: local SEO, Lake Conroe seasonality, targeting growing ZIP codes and community events.",
    "/blog/social-proof-reviews-testimonials/": "How to use reviews and testimonials on your website: where to place them, getting permission, video testimonials and review schema basics.",
    "/blog/brand-colors-that-build-trust/": "How to choose brand colors that build trust: color psychology, contrast and accessibility, and building a palette that works on signs, web and ads.",
    "/blog/find-the-right-influencers/": "How to find the right Houston influencers for your business: where to search, vetting audience and engagement, outreach and what to pay.",
    "/blog/small-business-guide-google-ads-2026/": "A no-nonsense 2026 Google Ads guide for small businesses: campaign setup, keywords and negatives, budgets, conversion tracking and common mistakes.",
}


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def esc(s):
    return html.escape(s, quote=True)


def ld_blocks(s):
    return list(re.finditer(r'(<script type="application/ld\+json">)(.*?)(</script>)', s, re.S))


def git_date(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        return out if out and not dirty else None
    except OSError:
        return None


def article_words(s):
    m = re.search(r"<article\b.*?</article>", s, re.S)
    if not m:
        return 0
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style|svg)\b.*?</\1>", " ", m.group(0), flags=re.S))
    return len(html.unescape(t).split())


TOPIC_CSS = ('<style id="fb-topics">.hub-cats a{font-size:13px;font-weight:600;padding:8px 14px;border-radius:999px;'
             'border:1px solid var(--line2);color:var(--soft);text-decoration:none;transition:border-color .2s,color .2s}'
             '.hub-cats a b{color:var(--cyan);margin-left:6px}.hub-cats a:hover,.hub-cats a:focus-visible{border-color:var(--cyan);color:#fff}'
             '.hub-cats a.on{background:var(--cyan);border-color:var(--cyan);color:#021615}.hub-cats a.on b{color:#021615}'
             '.topic-links{margin-top:18px;font-size:14px;color:var(--soft)}.topic-links a{color:var(--cyan);margin-right:14px}'
             'a.pill-cat{text-decoration:none}</style>')


def main():
    idx_path = f"{SITE}/blog/index.html"
    idx = read(idx_path)
    card_re = re.compile(r'<a class="post rv[^"]*" href="/blog/([^"/]+)/">.*?</a>', re.S)

    # ---- posts: data, category pill, articleSection, breadcrumb, wordCount, descriptions --------
    posts = {}
    for p in sorted(glob.glob(f"{SITE}/blog/*/index.html")):
        slug = p.split("/")[-2]
        s = read(p)
        if 'http-equiv="refresh"' in s:
            continue
        h = hub_for(slug)
        url = f"{BASE}/blog/{slug}/"
        orig = s
        s = re.sub(r'<(span|a) class="pill-cat"[^>]*>.*?</\1>',
                   f'<a class="pill-cat" href="/topics/{h[0]}/">{esc(h[1])}</a>', s, count=1, flags=re.S)
        if 'id="fb-topics"' not in s:
            s = s.replace("</head>", TOPIC_CSS + "\n</head>", 1)
        d = DESCS.get(f"/blog/{slug}/")
        if d:
            for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
                s = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc(d) + m.group(2), s)
        wc = article_words(s)
        info = {"slug": slug, "url": url, "hub": h[0]}
        for m in ld_blocks(s):
            try:
                data = json.loads(m.group(2))
            except ValueError:
                continue
            nodes = data.get("@graph", [data])
            changed = False
            for n in nodes:
                t = n.get("@type")
                if t == "BlogPosting":
                    if n.get("articleSection") != h[1]:
                        n["articleSection"] = h[1]; changed = True
                    if not n.get("wordCount") or abs(n["wordCount"] - wc) / max(wc, 1) > 0.3:
                        n["wordCount"] = wc; changed = True
                    if d and n.get("description") != d:
                        n["description"] = d; changed = True
                    if not n.get("isPartOf"):
                        n["isPartOf"] = {"@id": BASE + "/blog/#blog"}; changed = True
                    info.update(headline=n.get("headline"), datePublished=n.get("datePublished"),
                                dateModified=n.get("dateModified") or n.get("datePublished"),
                                image=n.get("image"), node_id=n.get("@id", url + "#article"))
                if t == "BreadcrumbList":
                    items = n.get("itemListElement", [])
                    if items and items[-1].get("item") == url:
                        last = items[-1]
                        want = [
                            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                            {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "/blog/"},
                            {"@type": "ListItem", "position": 3, "name": h[1], "item": f"{BASE}/topics/{h[0]}/"},
                            {"@type": "ListItem", "position": 4, "name": last.get("name"), "item": url},
                        ]
                        if items != want:
                            n["itemListElement"] = want; changed = True
            if changed:
                new = json.dumps(data, ensure_ascii=False, indent=1)
                s = s.replace(m.group(0), m.group(1) + "\n" + new + "\n" + m.group(3), 1)
        if s != orig:
            write(p, s)
        posts[slug] = info

    # ---- blog index: card labels, chips, Blog schema -------------------------------------------
    def relabel(m):
        slug = m.group(1)
        h = hub_for(slug)
        return re.sub(r'<span class="post-cat">.*?</span>', f'<span class="post-cat">{esc(h[1])}</span>', m.group(0), count=1)
    idx = card_re.sub(relabel, idx)
    order = [m.group(1) for m in card_re.finditer(idx)]
    counts = {}
    for sl in order:
        counts[hub_for(sl)[0]] = counts.get(hub_for(sl)[0], 0) + 1

    def chips(active=None):
        return '<div class="hub-cats">' + "".join(
            f'<a href="/topics/{h[0]}/"{" class=\"on\" aria-current=\"page\"" if h[0] == active else ""}>{esc(h[1])}<b>{counts.get(h[0], 0)}</b></a>'
            for h in sorted(HUBS, key=lambda h: -counts.get(h[0], 0)) if counts.get(h[0])) + "</div>"
    idx = re.sub(r'<div class="hub-cats">.*?</div>', lambda _: chips(), idx, count=1, flags=re.S)
    if 'id="fb-topics"' not in idx:
        idx = idx.replace("</head>", TOPIC_CSS + "\n</head>", 1)

    def post_ref(sl):
        i = posts.get(sl, {})
        r = {"@type": "BlogPosting", "@id": i.get("node_id", f"{BASE}/blog/{sl}/#article"), "headline": i.get("headline"),
             "url": f"{BASE}/blog/{sl}/", "datePublished": i.get("datePublished"), "dateModified": i.get("dateModified"),
             "author": {"@id": BASE + "/#sean-melton", "name": "Sean Melton"}}
        if i.get("image"):
            r["image"] = i["image"]
        return {k: v for k, v in r.items() if v}

    blog_node = {"@type": "Blog", "@id": BASE + "/blog/#blog", "name": "First Byte Marketing Blog",
                 "url": BASE + "/blog/", "inLanguage": "en-US",
                 "description": "Marketing playbooks for Houston and The Woodlands businesses.",
                 "publisher": {"@id": ORG}, "blogPost": [post_ref(sl) for sl in order[:20]]}
    m = ld_blocks(idx)[0]
    data = json.loads(m.group(2))
    graph = [n for n in data.get("@graph", [data]) if n.get("@type") != "Blog"]
    graph.insert(0, blog_node)
    new = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    idx = idx.replace(m.group(0), m.group(1) + "\n" + new + "\n" + m.group(3), 1)
    write(idx_path, idx)

    # ---- topic hub pages --------------------------------------------------------------------------
    cards = {m.group(1): m.group(0) for m in card_re.finditer(idx)}
    feat_start = idx.find('<div class="head rv"><div><span class="lbl"><span class="tri"></span>Latest')
    grid_start = idx.find('<div class="posts">')
    all_cards = list(card_re.finditer(idx, grid_start))
    grid_end = all_cards[-1].end() + len("</div>")
    for h in HUBS:
        slug, label, title, h1, desc, intro, links, _ = h
        url = f"{BASE}/topics/{slug}/"
        members = [sl for sl in order if hub_for(sl)[0] == slug]
        s = idx
        s = s[:feat_start] + (
            f'<div class="head rv"><div><span class="lbl"><span class="tri"></span>{esc(label)}</span>'
            f'<h2 class="h2">{len(members)} guides, <span class="cy">newest first.</span></h2></div></div>\n'
            f'<div class="posts">' + "".join(cards[sl] for sl in members) + "</div>") + s[grid_end:]
        s = re.sub(r"<!-- ===== SEO head: .*? ===== -->", f"<!-- ===== SEO head: {url} ===== -->", s)
        s = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title, quote=False)}</title>", s, flags=re.S)
        for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
            s = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc(desc) + m.group(2), s)
        for prop in ('property="og:title"', 'name="twitter:title"'):
            s = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc(title) + m.group(2), s)
        s = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), s)
        s = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), s)
        s = re.sub(r'(<meta property="og:type" content=")[^"]*(")', lambda m: m.group(1) + "website" + m.group(2), s)
        s = re.sub(r'<h1 class="seo-h1">.*?</h1>', lambda _: f'<h1 class="seo-h1"><span class="tri"></span>{esc(h1)}</h1>', s, count=1, flags=re.S)
        s = re.sub(r'<p class="sv-disp">.*?</p>', lambda _: f'<p class="sv-disp">{esc(label)}.<br><span class="cy">Every guide in one place.</span></p>', s, count=1, flags=re.S)
        link_html = "".join(f'<a href="{href}">{esc(t)} →</a>' for href, t in links)
        s = re.sub(r'<p class="sub">.*?</p>', lambda _: f'<p class="sub">{esc(intro)}</p><p class="topic-links">Related: {link_html}<a href="/blog/">All {len(order)} articles →</a></p>', s, count=1, flags=re.S)
        s = re.sub(r'<div class="hub-cats">.*?</div>', lambda _: chips(slug), s, count=1, flags=re.S)
        graph = [
            {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": title.replace(" | First Byte", ""),
             "description": desc, "inLanguage": "en-US", "isPartOf": {"@id": BASE + "/#website"},
             "about": label, "publisher": {"@id": ORG},
             "breadcrumb": {"@id": url + "#breadcrumb"}, "mainEntity": {"@id": url + "#list"}},
            {"@type": "ItemList", "@id": url + "#list", "name": h1, "numberOfItems": len(members),
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/blog/{sl}/",
                                  "name": posts.get(sl, {}).get("headline", sl)} for i, sl in enumerate(members)]},
            {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "/blog/"},
                {"@type": "ListItem", "position": 3, "name": label, "item": url}]},
        ]
        blocks = ld_blocks(s)
        new = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
        s = s.replace(blocks[0].group(0), blocks[0].group(1) + "\n" + new + "\n" + blocks[0].group(3), 1)
        for b in blocks[1:]:
            s = s.replace(b.group(0), "", 1)
        write(f"{SITE}/topics/{slug}/index.html", s)

    # ---- other pages with short descriptions (case studies) ---------------------------------------
    for u, d in DESCS.items():
        if u.startswith("/blog/"):
            continue
        p = f"{SITE}{u}index.html"
        if os.path.exists(p):
            s = read(p)
            n = s
            for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
                n = re.sub(rf'(<meta {prop} content=")[^"]*(")', lambda m: m.group(1) + esc(d) + m.group(2), n)
            if n != s:
                write(p, n)

    # ---- sitemap: real lastmod dates + topic hubs --------------------------------------------------
    sp = f"{SITE}/sitemap.xml"
    sm = read(sp)
    newest = {}
    for sl in order:
        hb = hub_for(sl)[0]
        dm = (posts.get(sl, {}).get("dateModified") or "")[:10]
        if dm and dm > newest.get(hb, ""):
            newest[hb] = dm
    blog_newest = max(newest.values())
    for h in HUBS:
        loc = f"{BASE}/topics/{h[0]}/"
        if f"<loc>{loc}</loc>" not in sm:
            sm = sm.replace("</urlset>", f"<url><loc>{loc}</loc><lastmod>{newest.get(h[0], blog_newest)}</lastmod>"
                                         f"<changefreq>weekly</changefreq><priority>0.7</priority></url>\n</urlset>")

    def fix(m):
        block = m.group(0)
        loc = re.search(r"<loc>([^<]*)</loc>", block).group(1)
        path = loc[len(BASE):]
        date = None
        if path.startswith("/topics/"):
            date = newest.get(path.split("/")[2], blog_newest)
        elif path == "/blog/":
            date = blog_newest
        elif path.startswith("/blog/") and path.strip("/").count("/") == 1:
            date = (posts.get(path.split("/")[2], {}).get("dateModified") or "")[:10] or None
        else:
            f = f"site{path}index.html"
            date = git_date(f)
        if date:
            block = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{date}</lastmod>", block)
        return block
    sm = re.sub(r"<url>.*?</url>", fix, sm, flags=re.S)
    write(sp, sm)

    # ---- llms.txt: topic hubs ------------------------------------------------------------------------
    lp = f"{SITE}/llms.txt"
    if os.path.exists(lp):
        ll = read(lp)
        ll = re.sub(r"\n## Blog topics\n.*?(?=\n## |\Z)", "", ll, flags=re.S).rstrip("\n")
        ll += "\n\n## Blog topics\n" + "".join(f"- [{h[3]}]({BASE}/topics/{h[0]}/): {h[4]}\n" for h in HUBS)
        write(lp, ll)
    print(f"topics: {len(HUBS)} hubs, {len(order)} posts; " + ", ".join(f"{h[0]}={counts.get(h[0], 0)}" for h in HUBS))


if __name__ == "__main__":
    main()
