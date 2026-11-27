"""Refresh batch (module s_d): three existing thin posts rewritten in place, same slugs.
1. power-of-local-landing-pages: step-by-step build guide for city/service-area pages (Houston, The Woodlands).
2. google-business-profile-number-one-asset: field-by-field Google Business Profile guide with 2024-2026 changes.
3. digital-marketing-cost-the-woodlands-houston: cost guide with a channel price sheet and three sample budgets.

Research, landing pages: Google Search spam policies (doorway abuse definition and examples; scaled content abuse);
Google's March 5, 2024 Search blog post (scaled content policy, 40% expected and 45% final reduction in low-quality,
unoriginal content); Google Business Profile service area help (up to 20 areas, no radius, about 2 hours' drive);
Guidelines for representing your business (virtual offices ineligible, coworking signage, hide address for SABs,
"IS a" categories); Google Ads Quality Score help (expected CTR, ad relevance, landing page experience); Google Search
Central LocalBusiness structured data docs; Census Bureau Vintage 2025 city estimates (Fulshear +21.0% to 64,630;
Houston 2,397,315); The Woodlands Township village association page (eight villages incl. Creekside Park).
GBP: Google's local ranking help (relevance, distance, prominence; no way to pay for better ranking); Edit your
Business Profile help (750-character description, 1 primary + up to 9 additional categories, 1 + 2 phone numbers,
re-verification after address or name changes); GBP performance help (calls = taps on call button, directions,
website clicks, searches, views counted once per person per day); Google's chat and call history notice (ended July
31, 2024); Search Engine Land on Business Profile websites redirecting to Maps (March 2024); Search Engine
Roundtable on Q&A being replaced by the AI "Ask" feature in Maps (Dec 2025); PPC Land on the April 2026 review
staff-quota rule; Google Maps prohibited content policy; BrightLocal Local Consumer Review Survey 2026 (Feb 11, 2026;
1,002 US adults; 97% read reviews, Google 71%, AI tools 45%, 31% need 4.5+, 47% won't use under 20 reviews, 74%
last three months, 89% expect replies); Texas Tribune on 2.26 million Beryl outages; Google special hours help.
Cost: LocaliQ 2026 search advertising benchmarks (CPC $5.42, CPL $66.69, CTR 6.64%; per-industry CPC/CPL); WordStream
2026 Facebook ads benchmarks via PPC Land (Sept 14, 2026; median CPL $27.39, traffic CPC $0.60); Backlinko SEO pricing
survey (300+ pros, updated Dec 29, 2025; $1,001-$2,500 most common retainer; projects mostly $1,000-$5,000; $50-$100
typical hourly); SE Ranking 2023 agency pricing survey (US/Canada median retainer $1,863, project $3,625, hourly
$112); Gartner 2026 CMO Spend Survey (7.8% of revenue, 401 leaders); AdQuick Houston billboard ranges; AdWave 2026 CTV
CPM (~$26); MailPro July 2026 EDDM rate ($0.260). Figures reused from our own earlier posts where they were sourced.
Left out because we couldn't verify: an SBA "7-8% of revenue" rule (only found on archived or third-party pages);
any official Google statement on minimum word counts for city pages; exact date Q&A disappeared in the US.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

SRC = {
    # landing pages
    "spam": A("https://developers.google.com/search/docs/essentials/spam-policies", "Google’s spam policies"),
    "spam2": A("https://developers.google.com/search/docs/essentials/spam-policies", "the same spam policy page"),
    "mar24": A("https://blog.google/products/search/google-search-update-march-2024/", "Google’s March 2024 announcement"),
    "sa": A("https://support.google.com/business/answer/9157481?hl=en", "Google’s service area help page"),
    "guide": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s guidelines for representing your business"),
    "qs": A("https://support.google.com/google-ads/answer/6167118?hl=en", "Google’s Quality Score help page"),
    "lb": A("https://developers.google.com/search/docs/appearance/structured-data/local-business", "Google’s LocalBusiness structured data docs"),
    "census_city": A("https://www.census.gov/newsroom/press-releases/2026/vintage-2025-city-town-pop-estimates.html", "Census Bureau’s Vintage 2025 city estimates"),
    "twp": A("https://www.thewoodlandstownship-tx.gov/villageassociations", "The Woodlands Township’s village list"),
    # GBP
    "rank": A("https://support.google.com/business/answer/7091?hl=en", "Google’s own explanation of local ranking"),
    "edit": A("https://support.google.com/business/answer/14368911?hl=en", "Google’s Edit your Business Profile page"),
    "perf": A("https://support.google.com/business/answer/9918094?hl=en", "Google’s performance help page"),
    "chat": A("https://support.google.com/business/answer/14919056?hl=en", "Google’s notice on chat and call history"),
    "sites": A("https://searchengineland.com/google-business-profile-websites-are-now-redirected-to-google-maps-438154", "Search Engine Land"),
    "qa": A("https://www.seroundtable.com/google-maps-qa-feature-ask-40594.html", "Search Engine Roundtable"),
    "ppcl": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "bl2": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 survey"),
    "beryl": A("https://texastribune.org/2024/07/11/centerpoint-power-restore-texas-houston-when-why-timeline", "the Texas Tribune"),
    "special": A("https://support.google.com/business/answer/6303076?hl=en", "Google’s special hours help page"),
    # cost
    "liq": A("https://localiq.com/blog/search-advertising-benchmarks/", "LocaliQ’s 2026 search advertising benchmarks"),
    "liq2": A("https://localiq.com/blog/search-advertising-benchmarks/", "LocaliQ"),
    "fb": A("https://ppc.land/facebook-lead-costs-hold-at-27-39-as-traffic-clicks-drop-to-0-60/", "WordStream’s 2026 Facebook ads benchmarks, as summarized by PPC Land"),
    "blko": A("https://backlinko.com/seo-pricing", "Backlinko’s survey of more than 300 SEO professionals"),
    "ser": A("https://knowledge.seranking.com/hubfs/Survey/2023-Marketing-and-SEO-Agency-Pricing-Models-Survey_c.pdf", "SE Ranking’s agency pricing survey"),
    "gartner": A("https://gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities", "Gartner’s 2026 CMO Spend Survey"),
    "aq": A("https://adquick.com/billboard-locations/texas/houston", "AdQuick’s Houston rate ranges"),
    "ctv": A("https://adwave.com/resources/average-ctv-cpm-q2-2026", "AdWave’s 2026 CTV benchmark"),
    "mp": A("https://www.mailpro.org/post/usps-rate-changes-july-2026/", "MailPro’s July 2026 rate table"),
}

LP = "/blog/power-of-local-landing-pages/"
GBP = "/blog/google-business-profile-number-one-asset/"
COST = "/blog/digital-marketing-cost-the-woodlands-houston/"

POSTS = [
    # ------------------------------------------------------------------ post 1: local landing pages
    {
        "slug": "power-of-local-landing-pages",
        "date": "2025-12-18",
        "modified": "2026-11-27",
        "title": "The Power of Local Landing Pages: How to Build Service-Area Pages That Rank in Houston and The Woodlands",
        "seo_title": "Local Landing Pages for Every Service Area (Houston)",
        "desc": "How to build local landing pages for every Houston and The Woodlands service area: which cities to pick, what each page needs, and how to avoid doorway pages.",
        "category": "SEO & AI search",
        "icons": ["Google", "Google Business Profile", "Search Console"],
        "art": "b2",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for local landing pages covering Houston, The Woodlands, Katy and Conroe service areas",
        "related": ["the-woodlands-spring-conroe-address-local-seo", "multi-location-local-seo-houston-franchises", "landing-pages-101"],
        "sections": [
            (None, f"""<p>One page can’t rank in Katy, Conroe and Pearland at the same time. Those towns are 60 miles apart, and Google treats “water heater repair Katy” and “water heater repair Conroe” as two different questions from two different people.</p>
<p>Most service businesses in Greater Houston still try anyway. The homepage says “proudly serving Houston and surrounding areas,” the footer lists 30 towns in gray 11-point type, and the business wonders why it only shows up near its own shop.</p>
<p><b>Short answer:</b> a local landing page is a page built for one service area, with proof you actually work there: jobs, reviews, photos, prices and local details. Build them only for towns you serve and want more of, make each one useful on its own, and link them from a service-area hub. Thin copies with the city name swapped are what Google calls doorway pages.</p>
<p>This guide walks through it in order: whether city pages still work, how to pick the towns, what goes on each page, how they connect to your Google Business Profile and your ads, and a 90-day rollout.</p>"""),

            ("Do local landing pages still work in 2026?", f"""<p>Yes, when they’re good. Google never banned location pages. It bans a specific bad version of them.</p>
<p>{SRC['spam']} define doorway abuse as sites or pages “created to rank for specific, similar search queries” that lead users to intermediate pages “that aren’t as useful as the final destination.” One of the listed examples is having “multiple domain names or pages targeted at specific regions or cities that funnel users to one page.” Another is “creating substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy.”</p>
<p>Read that twice and you have the whole rulebook. A Katy page that’s the Cypress page with “Katy” pasted in, and that exists only to push people to a contact form, fits the definition. A Katy page that shows six jobs you did in Cinco Ranch and Elyson, explains how permits work out there and quotes a Katy customer does not.</p>
<p>The penalty risk got sharper in 2024. In {SRC['mar24']} on March 5, 2024, Google said its update and the expanded scaled content abuse policy would cut low-quality, unoriginal content in results by 40%; by April 26 it said the rollout had delivered a 45% reduction. The policy covers content produced at scale to manipulate rankings “whether automation, humans or a combination are involved.” Generating 80 city pages with an AI tool in an afternoon is the textbook case.</p>
<!--fig:doorway-->
<p>So the question isn’t really “do city pages work.” It’s whether you have enough real material for each town to justify a page. For most Houston service businesses that’s somewhere between three and fifteen towns, never 80.</p>"""),

            ("Which Houston-area cities deserve their own page?", f"""<p>Start from where the money is, then check Google agrees there’s demand. We score candidate towns on five things before we write a word.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Question</th><th>Why it matters</th><th>Where to check</th></tr></thead>
<tbody>
<tr><td>Have you done paid jobs there in the last year?</td><td>No jobs means no photos, reviews or specifics, which means a thin page</td><td>Your CRM or invoicing, sorted by ZIP</td></tr>
<tr><td>Do people search “[service] [town]”?</td><td>Some towns are searched by name, some aren’t (more on that below)</td><td>Google Ads Keyword Planner, Search Console queries</td></tr>
<tr><td>Can you get there profitably?</td><td>A $150 service call in Fulshear from a Conroe shop loses money in drive time</td><td>Your dispatch history and average ticket</td></tr>
<tr><td>Is it already inside your map pack reach?</td><td>If you rank in the map pack there, the page adds less than in towns where you don’t</td><td>A grid rank tracker or a few manual searches from that area</td></tr>
<tr><td>Is it growing?</td><td>New subdivisions mean new homeowners with no loyalty yet</td><td>Census estimates, county permit data</td></tr>
</tbody></table></div>
<p>Growth is uneven around Houston, and it shows up in the data. The {SRC['census_city']} put Fulshear at 64,630 people in 2025, up 21.0% in a single year, while the City of Houston added 11,515 to reach 2,397,315. A 21% town on the west side and a mature inner-loop neighborhood are different bets.</p>
<!--fig:map-->
<p>Houston geography has a few quirks that change which page names make sense.</p>
<ul>
<li><b>The Woodlands isn’t a city.</b> It’s a township with eight villages per {SRC['twp']}, and Creekside Park sits across Spring Creek in Harris County. People search “The Woodlands” far more than “Alden Bridge,” so one strong Woodlands page usually beats eight village pages.</li>
<li><b>“Spring” and “Cypress” are mostly mailing addresses.</b> Huge unincorporated areas with no city hall. People search them by name constantly, so they deserve pages even though there’s no municipal anything to write about.</li>
<li><b>Some places are searched as neighborhoods.</b> “Kingwood” gets searched more than “Humble” for a lot of home services, and “The Heights” or “Memorial” behave like towns inside Houston. Check before you assume.</li>
<li><b>Permits split along city lines.</b> A fence or patio job inside the City of Houston goes through the city’s permitting center, unincorporated Harris County through the county engineer, and Conroe or Montgomery through their own offices. That’s real, page-worthy local detail for contractors.</li>
</ul>
<p>If you’re in The Woodlands or Spring, our {L('/blog/the-woodlands-spring-conroe-address-local-seo/', 'post on Woodlands, Spring and Conroe addresses')} covers how the address on your profile affects all of this.</p>"""),

            ("What goes on a local landing page that actually ranks", f"""<p>Here’s the anatomy we build to. Not every page needs every block, but a page with fewer than half of them usually isn’t ready.</p>
<!--fig:anatomy-->
<p>A few of these deserve more explanation, because they’re where most city pages fall flat.</p>
<p><b>Local jobs with photos.</b> “Recent work in Katy” with three to six projects, each with a neighborhood or cross street, what the problem was, and a real photo. Not stock, and not the same three photos on every page. This is the single block that makes a page impossible to copy.</p>
<p><b>Reviews from that town.</b> If your review platform lets you filter by location, pull two or three from customers there. A Pearland homeowner trusts a Pearland review more than one from Tomball.</p>
<p><b>Local conditions.</b> This is where you show you’ve been there. Expansive clay soil and foundation movement in parts of Katy and Cypress. Pine pollen and tree canopy in The Woodlands. Older cast-iron plumbing in pre-1980 homes in Spring Branch. Flood-prone streets near Cypress Creek. HOA approval for exterior work in master-planned communities like Bridgeland or Woodforest. Only write what’s true for your trade.</p>
<p><b>Drive time and scheduling.</b> “We’re based off Research Forest, so we’re usually 20 to 30 minutes from Magnolia. Same-day slots open most weekdays.” Customers want this, and it’s a detail nobody fakes well.</p>
<p><b>Pricing context.</b> If trip charges or prices differ by area, say so. If they don’t, say that too. A page that answers the price question gets more calls, as we argue in {L('/blog/website-copy-that-sells/', 'website copy that sells')}.</p>"""),

            ("How long should a city page be, and how different does it need to be?", f"""<p>Google publishes no word count, and we’d ignore anyone who quotes you one. A tight 500-word page with eight real job photos beats a 1,500-word page of filler about Katy’s history.</p>
<p>The better test is uniqueness. Before a page goes live, we run it through five checks:</p>
<!--fig:unique-->
<p>If the page fails the first or second check, don’t publish it yet. Put the town on your service-area hub page as a line item and come back once you have jobs there. That’s honest, it’s useful to the visitor, and it keeps you clear of the “substantially similar pages” language in {SRC['spam2']}.</p>
<p>Reusing some text is fine. Your warranty terms, your licensing, your process: those can be the same everywhere, and rewriting them five ways to look unique is silly. The test is whether the parts that should differ actually do.</p>"""),

            ("How city pages work with your Google Business Profile", f"""<p>Your website’s city pages and your Google Business Profile do different jobs. The profile decides whether you appear in the map pack. The pages help you rank in the regular results below it, give the map-pack click somewhere better than the homepage to land, and back up the profile’s claim that you serve those towns.</p>
<p>Three rules from Google that trip up Houston businesses:</p>
<ul>
<li><b>Service areas.</b> You can list up to 20 on your profile, there’s no radius option, and the area “shouldn’t be more than about 2 hours of driving time” from your base, per {SRC['sa']}. Match your city pages to those areas.</li>
<li><b>No fake offices.</b> Per {SRC['guide']}, a rented address you don’t operate from isn’t eligible, and a coworking office needs clear signage and staff during business hours. A virtual office in Sugar Land does not get you a Sugar Land map listing. It gets you suspended.</li>
<li><b>Hide the address if customers don’t come to you.</b> Service-area businesses should hide it. Hybrid businesses with a staffed storefront can show it and set service areas too.</li>
</ul>
<p>If you do have real staffed locations, each one gets its own profile, and each profile’s website link should go to that location’s page, not the homepage. Our {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO guide')} covers that setup, and the {L(GBP, 'Google Business Profile guide')} covers the profile itself.</p>"""),

            ("Using local landing pages for Google Ads", f"""<p>City pages pay for themselves twice if you run search ads. Google’s Quality Score has three components, per {SRC['qs']}: expected clickthrough rate, ad relevance and landing page experience, described as “how relevant and useful your landing page is to people who click your ad.”</p>
<p>So an ad group for “plumber Katy” and “Katy plumbing repair” should land on the Katy page, with an ad headline that says Katy. A headline promising “Katy plumbers” that lands on a homepage talking about The Woodlands is a small trust break, and those add up in conversion rate.</p>
<!--fig:adsmatch-->
<p>Two cautions. Don’t build city pages only for ads and block them from search with noindex unless they’re truly duplicates; a good page should do both jobs. And watch your location settings: “Presence: people in or regularly in your included locations” keeps a Katy campaign from paying for clicks from people in Ohio researching a move. Our {L('/services/search-marketing/', 'search marketing team')} builds these campaigns, and our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} help with the budget side.</p>"""),

            ("URLs, internal links and schema for service-area pages", f"""<p>The structure matters more than people expect, because it’s how Google tells a browseable hierarchy from a pile of doorways.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Element</th><th>What we do</th><th>What we avoid</th></tr></thead>
<tbody>
<tr><td>URL</td><td><code>/service-areas/katy-tx/</code> or <code>/drain-cleaning/katy-tx/</code> for service-plus-city pages</td><td><code>/best-cheap-plumber-katy-tx-77494/</code></td></tr>
<tr><td>Hub page</td><td>One “Areas we serve” page linking to every city page, with a sentence or two on each town</td><td>City links only in a stuffed footer</td></tr>
<tr><td>Internal links</td><td>Service pages link to the city pages where that service is common; city pages link back to service pages</td><td>Every city page linking to every other city page</td></tr>
<tr><td>Title tag</td><td>“Drain Cleaning in Katy, TX | Company Name”</td><td>Five town names crammed into one title</td></tr>
<tr><td>Schema</td><td>LocalBusiness markup on real locations; areaServed listing the towns you cover</td><td>A fake street address for each city in the markup</td></tr>
</tbody></table></div>
<p>{SRC['lb']} cover the LocalBusiness properties Google reads. Markup should describe what’s true. If there’s no office in Pearland, the Pearland page shouldn’t carry markup that implies one.</p>
<p>On service-plus-city combinations (drain cleaning Katy, water heaters Katy, slab leaks Katy), start with one city page per town. Add combination pages only where a service is big enough in that town to have its own jobs and reviews. Otherwise you multiply thin pages, which is how a 12-page site becomes a 300-page site Google doesn’t trust.</p>
<p>We use this structure on our own site, with pages for {L('/digital-marketing-agency-katy-tx/', 'Katy')}, Conroe, Spring and other towns we work in.</p>"""),

            ("How long until a new city page ranks?", f"""<p>In the sites we’ve worked on, a new city page usually shows up in Search Console impressions within a few weeks and takes three to six months to settle into steady rankings. Towns where you already have reviews, jobs and some brand searches move faster. Towns where you’re a stranger take longer, and some never crack page one against companies based there.</p>
<!--fig:ramp-->
<p>Treat that curve as illustrative. What we’d actually watch in Search Console, per page: impressions for queries containing the town name, average position for your top two service terms plus the town, and clicks. Then in your call tracking or CRM, leads with that town’s ZIPs. A page with rising impressions and no leads has a conversion problem, not an SEO problem. Our {L('/blog/how-long-does-seo-take-houston-the-woodlands/', 'post on how long SEO takes')} goes deeper on timelines.</p>"""),

            ("Mistakes we see on Houston service-area sites", f"""<p>Most of these come from a template someone bought, or from an SEO package that charged per page.</p>
<ul>
<li>Forty city pages and two of them have ever produced a call.</li>
<li>Pages for towns the business won’t actually drive to. A customer in League City books, the tech declines the job, and now you have a one-star review from League City.</li>
<li>Stock photos of the Houston skyline on the Magnolia page.</li>
<li>Copy that mentions the town name 14 times and says nothing about the town.</li>
<li>No way to reach the pages except the sitemap. If your own site doesn’t link to a page, don’t expect Google to care about it.</li>
<li>City pages built once in 2021 and never touched. Add new jobs and reviews every quarter.</li>
</ul>
<p>The fix for almost all of them is fewer pages, each one better, linked from a real hub.</p>"""),

            ("A 90-day rollout plan for local landing pages", f"""<p>If you’re starting from a homepage and a services page, this is the order we’d go in.</p>
<!--fig:rollout-->
<p>After day 90, add one or two towns a quarter, and only once you have the jobs and photos to fill them. Pages like these are part of how we build sites under {L('/services/web-design-seo-pr/', 'web design and SEO')}. If you’d like a senior strategist to look at which towns are worth a page for your business and build a plan around it, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How many local landing pages should a Houston service business have?",
             "Only as many as you can fill with real local material. For most single-location service businesses around Houston and The Woodlands that means three to fifteen towns where you’ve done paid jobs, see search demand and can drive profitably. Start with your best three to five, add one or two a quarter, and list the rest on an areas-we-serve hub page instead of giving each a thin page."),
            ("Are city pages considered doorway pages by Google?",
             "Not automatically. Google’s spam policy targets pages created to rank for similar queries that funnel visitors elsewhere, including substantially similar pages aimed at different cities. A city page with local jobs, photos, reviews, drive times and conditions specific to that town is a useful page. A copy of another city page with the name swapped is the kind Google describes as doorway abuse."),
            ("Can I get a Google Business Profile in every city I serve?",
             "No. A Business Profile needs a real location where you operate, and Google says virtual offices are not eligible. Coworking spaces only qualify with clear signage and staff during business hours. Service-area businesses should list one profile, hide the address if customers don’t visit, and add up to 20 service areas. City landing pages on your website support those areas."),
            ("Should I use AI to write local landing pages?",
             "AI can help with outlines and editing, but it can’t supply the parts that make a city page rank: your jobs, photos, reviews and local knowledge. Google’s scaled content abuse policy applies whether content is made by automation, people or both, and it targets mass-produced pages with little value. Use your own job records as the raw material and keep each page specific."),
            ("Do local landing pages help with Google Ads in Houston?",
             "Yes. Landing page experience is one of the three parts of Google Ads Quality Score, so sending a Katy ad group to a page about Katy usually beats sending it to your homepage. The page should repeat the town and service from the ad, show local proof, and make calling easy. Use presence-based location targeting so you only pay for people actually in that area."),
        ],
        "figures": {
            "doorway": {
                "type": "compare",
                "title": "Doorway page vs. real local landing page",
                "left": {"title": "Doorway (risky)", "items": ["Same copy on every city page, name swapped", "Stock skyline photo", "No jobs, reviews or details from that town", "Exists only to push visitors to a form", "Reachable only through the sitemap"]},
                "right": {"title": "Local landing page (useful)", "items": ["Copy written from real jobs in that town", "Photos from projects nearby", "Reviews from local customers", "Drive times, permits, local conditions", "Linked from an areas-we-serve hub"]},
                "alt": "Comparison of doorway pages and useful local landing pages for service-area businesses in Houston and The Woodlands",
                "caption": f"Based on the doorway abuse definition in {SRC['spam']}.",
            },
            "map": {
                "type": "map",
                "title": "One shop, many searches",
                "sub": "Towns a Woodlands-based service business might build pages for, if it has jobs there",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Magnolia", "Tomball", "Kingwood", "Cypress", "Montgomery"],
                "note": "Illustrative example",
                "alt": "Map of possible local landing page towns around The Woodlands and north Houston, including Spring, Conroe, Magnolia and Kingwood",
                "caption": "Each highlighted town is a separate search. Pick by jobs and profit, not by how many dots fit on the map.",
            },
            "anatomy": {
                "type": "checklist",
                "title": "Anatomy of a city page that ranks",
                "sub": "Aim for at least half of these before publishing",
                "items": ["Town and service in the H1 and title", "Three to six recent local jobs with photos", "Two or three reviews from customers in that town", "Local conditions that affect the work", "Drive time and scheduling from your base", "Pricing or trip-charge notes for that area", "Permits, HOAs or rules specific to the town", "FAQs people there actually ask", "Click-to-call and a short form above the fold", "Links to related service pages and the hub"],
                "alt": "Checklist of what a local landing page needs to rank for Houston and The Woodlands service area searches",
                "caption": "The jobs, photos and reviews blocks do most of the work. They’re also the hardest to fake.",
            },
            "unique": {
                "type": "steps",
                "title": "The five-check uniqueness test",
                "sub": "Run every city page through this before it goes live",
                "steps": [["Real jobs", "Can you name at least three paid jobs in this town from the last year?"], ["Own photos", "Are the photos from this town and on no other city page?"], ["Swap test", "Replace the town name with another. Does the page still read as true? If yes, rewrite it."], ["Local fact", "Does it say something about the town a local would nod at?"], ["Next step", "Can a visitor call, book or get a price without leaving the page?"]],
                "alt": "Five steps to test whether a local landing page is unique enough for Houston and The Woodlands service areas",
                "caption": "The swap test catches most template pages in about ten seconds.",
            },
            "adsmatch": {
                "type": "funnel",
                "title": "Message match from search to call",
                "stages": [["Search: “drain cleaning Katy”", "Intent"], ["Ad headline names Katy and the service", "Relevance"], ["Lands on the Katy page, not the homepage", "Experience"], ["Local proof: jobs, reviews, drive time", "Trust"], ["Taps to call", "Lead"]],
                "alt": "Funnel showing how a Google search for a Katy service flows to a local landing page and a phone call in Houston",
                "caption": f"Landing page experience is one of three Quality Score components, per {SRC['qs']}.",
            },
            "ramp": {
                "type": "columns",
                "title": "How a new city page tends to ramp",
                "sub": "Share of eventual monthly impressions, by month after launch",
                "labels": ["Mo 1", "Mo 2", "Mo 3", "Mo 4", "Mo 5", "Mo 6"],
                "values": [10, 25, 45, 65, 80, 95],
                "highlight": [3, 4, 5],
                "y_label": "% of eventual impressions",
                "note": "Illustrative example based on our experience, not a benchmark",
                "alt": "Column chart of how a new local landing page ramps in impressions over six months for a Houston service business",
                "caption": "Towns where you already have reviews and jobs usually move faster than this.",
            },
            "rollout": {
                "type": "steps",
                "title": "A 90-day local page rollout",
                "steps": [["Days 1-10", "Pull a year of jobs by ZIP. Score towns on jobs, demand, profit and growth."], ["Days 11-20", "Build the areas-we-serve hub and fix the URL structure."], ["Days 21-45", "Write and photograph the top three town pages. Run the uniqueness test."], ["Days 46-60", "Point matching Google Ads ad groups at the new pages."], ["Days 61-90", "Add two more towns. Check Search Console and call data per page."]],
                "alt": "Steps in a 90-day plan to launch local landing pages for a business in Houston and The Woodlands",
                "caption": "Five excellent pages by day 90 beat thirty thin ones on day one.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: Google Business Profile
    {
        "slug": "google-business-profile-number-one-asset",
        "date": "2025-06-12",
        "modified": "2026-11-27",
        "title": "Why Your Google Business Profile Is Your #1 Local Marketing Asset in Houston and The Woodlands",
        "seo_title": "Google Business Profile: Your #1 Local Marketing Asset",
        "desc": "A field-by-field Google Business Profile guide for Houston and The Woodlands businesses: categories, reviews, photos, 2024-2026 changes and what to track.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google", "Google Analytics"],
        "art": "b4",
        "hero": "stars",
        "hero_alt": "Illustration of review stars for a Google Business Profile guide for Houston and The Woodlands businesses",
        "related": ["rank-in-google-map-pack-houston", "complete-guide-google-reviews", "google-business-profile-suspended-reinstatement"],
        "sections": [
            (None, f"""<p>A dentist in Spring asked us last year whether she still needed a website, since “everybody calls from the Google thing anyway.” Fair question. Her profile was producing more calls than her site. She still needed the website (we’ll get to why), but she was right about which one people saw first.</p>
<p><b>Short answer:</b> for a local business in Houston or The Woodlands, the Google Business Profile is usually the most valuable marketing asset you own because it’s where people compare you, read reviews, call and get directions, often without visiting your site. It’s free. Most profiles are half finished, which is your opening.</p>
<p>This is the field-by-field version: what Google says decides rankings, the settings most Houston profiles get wrong, what changed between 2024 and 2026, and how to tell whether the profile is working.</p>"""),

            ("Is a Google Business Profile more important than a website?", f"""<p>For the first impression, usually yes. For closing the sale, they work as a pair.</p>
<p>The profile is where comparison happens now. In {SRC['bl']}, published in February 2026 from a panel of 1,002 U.S. adults, 97% of consumers said they read reviews for local businesses and Google was still the top review source at 71%, down from 83% a year earlier. Generative AI tools jumped to 45% as a source for local recommendations. Those AI answers lean heavily on the same reviews and profile data, so a weak profile costs you in two places.</p>
<!--fig:bl-->
<p>The website still matters because the profile can’t hold everything. Pricing detail, your full service list, financing, before-and-after galleries, the reason to pick you over the four other dentists in the map pack. The profile earns the click or call; the site handles the customer who wants more proof first. If you’ve been relying on a free Google-built site, note that Google shut those down in March 2024 and started redirecting them to profiles, per {SRC['sites']}.</p>"""),

            ("What Google says decides local rankings", f"""<p>Google is unusually direct about this. In {SRC['rank']}, local results are based on three things:</p>
<ul>
<li><b>Relevance:</b> “how well a Business Profile matches what someone is searching for.”</li>
<li><b>Distance:</b> how far the business is from the searcher, or from the location in the search.</li>
<li><b>Prominence:</b> “how well-known a business is,” including links, articles and review count and rating.</li>
</ul>
<p>The same page says “There’s no way to request or pay for a better local ranking on Google.” Ads can appear above the map pack, but they don’t move your organic map position. Anyone selling you guaranteed map rankings is selling something Google says doesn’t exist.</p>
<p>Distance is the one you can’t change, and it explains most of the frustration we hear. A plumber off Woodlands Parkway will usually rank well in Shenandoah and Oak Ridge North and badly in Katy, no matter how good the profile is.</p>
<!--fig:distance-->
<p>That’s why the profile and the {L(LP, 'local landing pages on your website')} work together. The profile wins near your address. The pages, reviews from farther-out customers, and ads cover the towns where distance works against you. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} goes further on prominence.</p>"""),

            ("The field-by-field setup most Houston profiles get wrong", f"""<p>Open your profile from Google Search (search your business name while signed in) or the Maps app, and go through this table. The limits come from {SRC['edit']} and {SRC['guide']}.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Field</th><th>Google’s rule or limit</th><th>What we do</th></tr></thead>
<tbody>
<tr><td>Business name</td><td>Must match your real-world name; no taglines, locations or extra keywords (Google’s example: “Midas” is fine, “Midas Auto Service Experts” isn’t)</td><td>Use the name on your sign. Keyword-stuffed names invite edits and suspensions.</td></tr>
<tr><td>Primary category</td><td>One; choose the most specific that completes “this business IS a”</td><td>Pick the category for the work you most want. “Emergency veterinarian” and “Veterinarian” aren’t interchangeable.</td></tr>
<tr><td>Additional categories</td><td>Up to nine; use as few as possible</td><td>Add only real lines of business, never “has a” amenities</td></tr>
<tr><td>Description</td><td>750 characters; no URLs, HTML, prices or promos</td><td>Who you serve, what you do, where, and what makes you different, in plain language</td></tr>
<tr><td>Address and service area</td><td>Service-area businesses hide the address; up to 20 areas; about 2 hours’ drive max</td><td>List the towns you actually want work in, matching your website pages</td></tr>
<tr><td>Phone</td><td>One primary plus up to two more; must be under your direct control</td><td>A number that’s answered during listed hours, every time</td></tr>
<tr><td>Website</td><td>No redirects to other businesses’ pages</td><td>Link the location’s own page, tagged with UTM parameters so GA4 can separate profile visits</td></tr>
<tr><td>Hours</td><td>Keep current, including special hours</td><td>Update holiday and storm hours before the day, not after</td></tr>
<tr><td>Services and products</td><td>Plain descriptions of what you sell</td><td>Every real service, each with a one- or two-sentence description</td></tr>
<tr><td>Photos</td><td>Must represent the business</td><td>Exterior from the street, interior, team, real work. Monthly additions.</td></tr>
</tbody></table></div>
<p>One judgment call: call tracking. Google’s guidelines don’t address it directly. Our practice is to put a tracking number as primary and the main business line as an additional number so the listing stays consistent with the rest of the web. Do it once and leave it; swapping primary numbers every few months is asking for trouble.</p>
<p>The name field is where we see Houston businesses take the most risk. “Best Roofing Company Houston TX Roof Repair” might rank for a while. Then a competitor suggests an edit, or Google catches it, and the profile gets suspended right before storm season. Read our {L('/blog/google-business-profile-suspended-reinstatement/', 'reinstatement guide')} if that’s already happened.</p>
<p>Two fields get skipped that shouldn’t. Attributes (wheelchair-accessible entrance, free parking, women-owned or veteran-owned where they apply, online appointments) are small, but they’re exactly what an AI answer pulls when someone asks Maps for “a pediatric dentist in Cypress with Saturday hours.” And the appointment or booking link should go to a page where someone can actually book, not your homepage. If you use a scheduler, link straight to it.</p>"""),

            ("What changed on Google Business Profiles from 2024 to 2026", f"""<p>A lot of advice online is stale. Here’s what’s gone and what’s new.</p>
<!--fig:changes-->
<ul>
<li><b>Free Business Profile websites</b> were shut down in March 2024 and redirected to the profile, per {SRC['sites']}.</li>
<li><b>Chat and call history</b> ended on July 31, 2024, per {SRC['chat']}. If a vendor’s report still shows “chats,” ask where they come from.</li>
<li><b>Public Q&amp;A</b> was pulled back through 2025 and replaced by an AI “Ask” feature in Maps that answers from your own information and reviews, as {SRC['qa']} reported in December 2025. Answers you’d previously posted may still inform Google, but seeding your own Q&amp;A, once standard advice, isn’t the lever it was. Your description, services and reviews do that work now.</li>
<li><b>Review requests got stricter.</b> Google’s {SRC['gpol']} already banned incentives, review gating and discouraging negative reviews. In April 2026 it added language against making staff collect a set number of reviews or reviews with specific content, per {SRC['ppcl']}. Stop the “get 10 reviews that mention your name” contests.</li>
</ul>"""),

            ("Reviews: the part of the profile people read first", f"""<p>Most of what makes a profile convert is the review section. The 2026 numbers from {SRC['bl2']} are harder on businesses than they used to be.</p>
<!--fig:thresholds-->
<p>Thirty-one percent of consumers will only use a business rated 4.5 stars or higher, up from 17% the year before. Forty-seven percent won’t use a business with fewer than 20 reviews. Seventy-four percent only care about reviews from the last three months, which means a profile with 300 reviews and none since spring looks closed. And 89% expect owners to respond, with 81% expecting a reply within a week.</p>
<p>A review ask that works and stays inside Google’s rules:</p>
<ol>
<li>Send the same request to every customer, by text, within a few hours of the job or visit.</li>
<li>Keep it short: “Thanks for choosing us today. If you have a minute, a Google review helps other families in Spring find us: [link]. Either way, we appreciate you.”</li>
<li>Mention it once in person at checkout. No discount, no pressure, no “only if it’s five stars.”</li>
<li>Reply to every review within a week. For bad ones, acknowledge the specific problem, skip the defensiveness and give a name and number to call.</li>
</ol>
<p>One Houston-specific habit worth copying: answer a review in the language it was written in. A Spanish or Vietnamese review in Bellaire or Alief that gets a reply in English only reads as a form letter. If nobody on staff writes that language well, keep the reply short and have someone fluent check it.</p>
<p>Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates, and {L('/blog/fake-reviews-rule-local-businesses/', 'the post on the FTC fake reviews rule')} covers what not to do.</p>"""),

            ("Photos, posts and storm hours: keeping a Houston profile alive", f"""<p>Customers notice dead profiles. The newest photo is from 2022, the last update was a Fourth of July post, and the hours say open on a day the office was flooded.</p>
<!--fig:pair-->
<p>A realistic cadence for a small team:</p>
<ul>
<li><b>Photos:</b> four to ten new ones a month. Real jobs, real staff, the storefront from the street so first-timers can find the turn off FM 1488 or Kuykendahl.</li>
<li><b>Updates (posts):</b> one or two a month. A seasonal offer, a new service, a recent project. Short, with a photo and a button.</li>
<li><b>Services:</b> review each quarter. Add what you started offering, remove what you stopped.</li>
</ul>
<p>Houston adds one job most of the country doesn’t have: weather hours. When Hurricane Beryl came through in July 2024, {SRC['beryl']} counted 2.26 million power outages across the region, and plenty of businesses that were closed for days still showed “Open” on Google. Every customer who drove over and found a dark building had a bad experience you couldn’t see. Set special hours from your phone the moment you know, using {SRC['special']}, and mark “temporarily closed” if you need to. Freeze days in January get the same treatment. Our {L('/blog/hurricane-season-marketing-playbook-houston-the-woodlands/', 'hurricane season playbook')} has the rest.</p>"""),

            ("How do I know if my Google Business Profile is working?", f"""<p>Open the Performance tab. Per {SRC['perf']}, you’ll see views (unique people, counted at most once per person per day), the search terms that surfaced you, calls (taps on the call button), direction requests, website clicks, and bookings or messages where they apply.</p>
<p>Those are interactions, not customers. To connect them to revenue:</p>
<!--fig:funnel-->
<ul>
<li><b>Calls:</b> a tap isn’t a conversation. Call tracking on the profile’s number tells you how many connected, how long they lasted and which became appointments.</li>
<li><b>Website clicks:</b> tag the profile’s link with UTM parameters (for example utm_source=google, utm_medium=organic, utm_campaign=gbp) so GA4 reports profile traffic separately. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 tracking guide')} walks through setup.</li>
<li><b>Search terms:</b> check monthly. If “emergency plumber” never appears but “plumbing supply” does, your categories or services need work.</li>
<li><b>Direction requests:</b> for storefronts, compare to walk-ins. A spike in requests with flat walk-ins can mean a bad pin location.</li>
</ul>
<p>Look at trends over three months, not week to week. Weather, holidays and school calendars move Houston local search more than most owners expect.</p>"""),

            ("Suspensions, scam calls and the address question", f"""<p>Three problems eat more GBP time than everything else combined, at least in the accounts we see.</p>
<p><b>Suspensions.</b> The usual triggers are a keyword-stuffed name, a virtual office or coworking address without signage, and repeated edits to the address or name. Google says changing your address or name after verification may mean verifying again. If you’re moving, read {L('/blog/change-business-address-google-without-suspension/', 'how to change your address without a suspension')} first, and see {L('/blog/google-business-profile-video-verification/', 'video verification')} for what Google asks you to film.</p>
<p><b>Scam calls.</b> “This is Google, your listing will be deleted.” It isn’t Google. The profile is free, and Google doesn’t cold-call threatening to remove it. Our {L('/blog/google-business-listing-scam-calls/', 'scam calls post')} has the script for hanging up.</p>
<p><b>The address question.</b> A Spring mailing address inside The Woodlands, or a Conroe address on the Woodlands side of the county line, changes which searches you show for. Use the address that’s actually on your building, keep it identical everywhere online, and let landing pages handle the towns you serve but aren’t located in.</p>"""),

            ("A 20-minute weekly Google Business Profile routine", f"""<p>Nobody needs to live in the dashboard. Twenty minutes on Monday morning covers it.</p>
<!--fig:weekly-->
<p>Once a quarter, add a longer pass: recheck categories against your top competitors in the map pack, update services, refresh the description, and compare three months of calls and direction requests with the same period last year.</p>
<p>If you’d rather have someone handle the profile alongside your website and ads, that’s part of our {L('/services/web-design-seo-pr/', 'SEO and local search work')}. Tell us about your business and what you want more of, and a senior strategist will build a plan around it. <a href="/contact/">Get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I rank higher on Google Maps in The Woodlands or Houston?",
             "Google ranks local results on relevance, distance and prominence, and says you can’t pay for better placement. Choose the most specific primary category, fill in services and the description, keep hours accurate, and earn a steady stream of recent reviews you reply to. Distance from the searcher is fixed, so use local landing pages and ads for towns farther from your address."),
            ("How many Google reviews does a local business need?",
             "There’s no official number, but BrightLocal’s 2026 survey found 47% of consumers won’t use a business with fewer than 20 reviews and 74% only care about reviews from the last three months. Aim for at least 20 to start, then a steady flow every month. Recent reviews matter more than a large old total, and replies to them matter too."),
            ("Can I use a tracking number on my Google Business Profile?",
             "Google’s guidelines don’t address call tracking directly. They require numbers under your direct control and allow one primary plus up to two additional numbers. A common approach is a local tracking number as primary with your main line as an additional number, so the listing still matches your number elsewhere online. Set it once and avoid frequent changes."),
            ("What happened to Q&A on Google Business Profiles?",
             "Google pulled back public questions and answers on Business Profiles during 2025 and replaced them with an AI Ask feature in Google Maps that answers from a business’s own information and reviews. Previously published answers may still inform Google. In practice, a complete description, detailed services, accurate attributes and recent reviews now do the job seeded Q&A used to do."),
            ("How often should I post on my Google Business Profile?",
             "One or two updates a month is enough for most small businesses, plus four to ten new photos. Posts keep the profile looking active and give customers current offers or news, but they matter less for ranking than categories, reviews and distance. Spend the extra time replying to reviews and updating special hours around holidays and Houston storms."),
        ],
        "figures": {
            "bl": {
                "type": "stats",
                "title": "How local customers decide in 2026",
                "stats": [["97%", "read reviews for local businesses"], ["71%", "use Google for reviews, the top source"], ["45%", "use AI tools for local picks"], ["89%", "expect owners to reply to reviews"]],
                "note": "Source: BrightLocal Local Consumer Review Survey 2026",
                "alt": "Stats from BrightLocal 2026 on how consumers use Google reviews, relevant to Google Business Profiles in Houston and The Woodlands",
                "caption": f"From {SRC['bl']}.",
            },
            "distance": {
                "type": "map",
                "title": "Distance: the ranking factor you can’t edit",
                "sub": "A business near The Woodlands usually ranks best close to home",
                "highlight": ["The Woodlands", "Shenandoah", "Spring", "Conroe"],
                "note": "Illustrative example",
                "alt": "Map showing how Google Business Profile map rankings fade with distance from The Woodlands toward Katy and Pearland",
                "caption": "The rings mark about 10, 20 and 30 miles. Outer towns need landing pages, reviews from there and often ads.",
            },
            "changes": {
                "type": "steps",
                "title": "Google Business Profile changes, 2024-2026",
                "steps": [["March 2024", "Free Business Profile websites shut down and redirect to the profile."], ["July 31, 2024", "Chat and call history removed from profiles."], ["2025", "Public Q&A pulled back; an AI Ask feature in Maps answers questions instead."], ["April 2026", "Review policy adds limits on staff review quotas and scripted content."]],
                "alt": "Timeline of Google Business Profile changes from 2024 to 2026 that affect Houston and The Woodlands businesses",
                "caption": "If your GBP advice predates this list, check it against the current rules.",
            },
            "thresholds": {
                "type": "bars",
                "title": "What customers require before choosing you",
                "sub": "Share of consumers, 2026",
                "items": [["Only care about reviews from the last 3 months", 74, "74%"], ["Won’t use a business with under 20 reviews", 47, "47%"], ["Only use businesses rated 4.5 stars or higher", 31, "31%"], ["Expect a reply the same day", 19, "19%"]],
                "highlight": [0],
                "note": "Source: BrightLocal Local Consumer Review Survey 2026",
                "alt": "Bar chart of consumer review thresholds from BrightLocal 2026 for Google Business Profiles in Houston and The Woodlands",
                "caption": "Recency beats volume. A steady monthly flow does more than a burst every January.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From profile view to customer",
                "stages": [["Profile views", "2,400"], ["Interactions (calls, directions, site)", "190"], ["Connected calls and visits", "95"], ["Booked appointments", "38"], ["Paying customers", "30"]],
                "note": "Illustrative example",
                "alt": "Funnel from Google Business Profile views to paying customers for a local business in Houston or The Woodlands",
                "caption": "Google reports the top two rows. Call tracking and your CRM fill in the rest.",
            },
            "weekly": {
                "type": "checklist",
                "title": "The Monday 20-minute GBP routine",
                "items": ["Reply to every new review", "Check for suggested edits to your name, hours or category", "Add two or three new photos from last week’s work", "Set special hours for upcoming holidays or weather", "Glance at calls and direction requests vs. last week", "Post an update every other week", "Confirm the website link and UTM still work"],
                "alt": "Checklist for a weekly Google Business Profile routine for businesses in Houston and The Woodlands",
                "caption": "Suggested edits are the sneaky one. Anyone can propose a change to your profile.",
            },
            "pair": {
                "type": "compare",
                "title": "Set-and-forget vs. a working profile",
                "left": {"title": "Set and forget", "items": ["Claimed in 2021, never touched", "Name stuffed with keywords", "Last review reply a year ago", "Holiday and storm hours never set", "Website link goes to the homepage"]},
                "right": {"title": "Working profile", "items": ["Categories checked every quarter", "Name matches the sign", "Every review answered within a week", "Special hours set before the day", "Link goes to the right page, UTM-tagged"]},
                "alt": "Comparison of a neglected and an active Google Business Profile for local businesses in Houston and The Woodlands",
                "caption": "Most of the right column takes minutes, not money.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: digital marketing cost
    {
        "slug": "digital-marketing-cost-the-woodlands-houston",
        "date": "2026-10-03",
        "modified": "2026-11-27",
        "title": "How Much Does Digital Marketing Cost in The Woodlands & Houston? (2026 Pricing Guide)",
        "seo_title": "Digital Marketing Cost in Houston & The Woodlands (2026)",
        "desc": "What digital marketing costs in The Woodlands and Houston in 2026: SEO, Google Ads, social, websites, CTV and agency fees, plus three sample monthly budgets.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Analytics"],
        "art": "b6",
        "hero": "receipt",
        "hero_alt": "Illustration of a receipt for a digital marketing cost guide for The Woodlands and Houston businesses",
        "related": ["seo-cost-houston-the-woodlands", "google-ads-management-houston-cost", "marketing-agency-pricing-models-retainer-vs-percentage"],
        "sections": [
            (None, f"""<p>$66.69. That’s the 2026 national median cost of a lead from Google search ads across all industries, per {SRC['liq']}. Attorneys pay about twice that. Restaurants pay less than half.</p>
<p>That spread is why “how much does digital marketing cost?” gets such useless answers. It’s also the question we hear most from owners in The Woodlands, Spring, Conroe and across Greater Houston, so here are real numbers.</p>
<p><b>Short answer:</b> most single-location businesses around Houston spend roughly $2,500 to $12,000 a month on digital marketing, all in. That covers ad spend plus management, usually $1,500 to $5,000 a month for SEO or ads management, with a website of $3,000 to $15,000 up front. Competitive categories like law, HVAC and med spas spend more.</p>
<p>That range comes from our own proposals and the benchmarks below, and we’ll show the math, by channel, then three sample budgets.</p>"""),

            ("The four costs inside every marketing budget", f"""<p>Every quote you get mixes these together. Pull them apart before you compare two proposals.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Cost</th><th>What it is</th><th>Who gets the money</th><th>Typical share of a small budget</th></tr></thead>
<tbody>
<tr><td>Media</td><td>Clicks, impressions, leads, postage</td><td>Google, Meta, streaming networks, billboard owners, USPS</td><td>40% to 70%</td></tr>
<tr><td>Management</td><td>Strategy, setup, optimization, reporting</td><td>Your agency, freelancer or employee</td><td>20% to 40%</td></tr>
<tr><td>Creative</td><td>Ad copy, photos, video, landing pages, design</td><td>Agency, photographer, video crew</td><td>10% to 25%</td></tr>
<tr><td>Tools</td><td>Call tracking, CRM, review software, scheduling</td><td>Software vendors</td><td>2% to 10%</td></tr>
</tbody></table></div>
<p>The shares are from proposals we’ve built and seen, not a survey. Treat them as a sanity check. A plan that’s 90% management and 10% media can’t reach anyone. A plan that’s 95% media and nobody is reading the search terms report usually wastes a third of it.</p>"""),

            ("How much does digital marketing cost in Houston, by channel?", f"""<p>Here’s the price sheet. Media figures are national or Houston benchmarks from the sources linked; management ranges come from the surveys cited and our own Houston-area experience.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Media cost benchmarks</th><th>Typical management or project cost</th></tr></thead>
<tbody>
<tr><td>Google search ads</td><td>Avg. CPC $5.42, avg. cost per lead $66.69 (2026)</td><td>10% to 20% of spend, or $1,000 to $2,500/mo flat for accounts up to about $10,000</td></tr>
<tr><td>Facebook and Instagram ads</td><td>Median lead cost $27.39; median traffic CPC $0.60 (2026)</td><td>$750 to $3,000/mo, plus fresh creative every few weeks</td></tr>
<tr><td>SEO and local SEO</td><td>No media cost</td><td>Most common retainer $1,001 to $2,500/mo; projects mostly $1,000 to $5,000</td></tr>
<tr><td>Website</td><td>Hosting and domain, modest</td><td>$3,000 to $15,000 for most small-business sites; more for custom or e-commerce</td></tr>
<tr><td>Streaming TV (CTV)</td><td>CPM around $26 (2026)</td><td>Campaigns commonly start around $3,000 to $10,000/mo including production</td></tr>
<tr><td>Billboards</td><td>Freeway bulletin about $4,000 to $14,000 per 4 weeks; digital slots about $1,800 to $18,000</td><td>Design plus print and install for static faces</td></tr>
<tr><td>EDDM postcards</td><td>$0.260 postage per piece (since July 12, 2026)</td><td>About $2,000 to $3,000 all in for 5,000 homes</td></tr>
</tbody></table></div>
<p>Sources: {SRC['liq2']}, {SRC['fb']}, {SRC['blko']}, {SRC['ctv']}, {SRC['aq']} and {SRC['mp']}. Website ranges are from our {L('/blog/how-much-does-a-website-cost-the-woodlands/', 'website cost guide')}.</p>
<!--fig:headline-->"""),

            ("Google Ads costs in Houston: what drives the bill", f"""<p>Search ads are the closest thing to buying customers by the pound. You pay when someone who typed your service clicks. The price depends on your industry, more than anything you do.</p>
<!--fig:cpl-->
<p>Houston tends to run above those national medians in the categories where everyone fights: personal injury, roofing, emergency HVAC and plumbing, foundation repair. A homeowner in Kingwood with no AC in August is worth a lot to a lot of companies, and the auction knows it.</p>
<p>Budget guidance we give most local businesses: $1,500 to $3,000 a month in media is enough to learn what works in a tight service area. Competitive categories in Houston usually need $5,000 or more to stay visible all day. Management on top, typically 10% to 20% of spend or a flat fee, plus a one-time setup of around $1,000 to $2,000 for tracking and structure. Our {L('/blog/google-ads-management-houston-cost/', 'Google Ads management cost guide')} and {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} go deeper. If your category qualifies, Local Services Ads charge per lead instead of per click, which we compare in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads')}.</p>"""),

            ("SEO costs: monthly retainers and one-time projects", f"""<p>SEO has no media bill. You’re paying for people’s time: technical fixes, service and city pages, Google Business Profile work, reviews, links and reporting.</p>
<p>{SRC['blko']}, last updated in December 2025, found $1,001 to $2,500 a month is the most common retainer range, with $501 to $1,000 typical for small businesses with simple sites and $2,501 to $5,000 the premium tier. Most one-off projects (audits, content packages, migrations) landed between $1,000 and $5,000, and typical hourly rates ran $50 to $100, with senior specialists in the U.S. higher.</p>
<p>In Houston, a single-location business in a normal category usually lands between $800 and $2,000 a month. Law, dental, HVAC and roofing usually need $2,000 to $5,000 because the competition publishes more and earns more links. SEO is the slowest channel to pay back, often three to six months before meaningful movement, and the cheapest per lead once it works. Full breakdown in {L('/blog/seo-cost-houston-the-woodlands/', 'what SEO costs in Houston and The Woodlands')}.</p>"""),

            ("Paid social, websites, streaming TV and mail", f"""<p><b>Facebook and Instagram.</b> Cheaper per lead than search on paper. WordStream’s 2026 benchmarks put the median lead cost at $27.39 and traffic clicks at $0.60, per {SRC['fb']}. The catch is intent: you’re interrupting people, so lead quality varies a lot and creative wears out. Most local businesses start at $1,000 to $5,000 a month in media. Our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'post on fixing bad Facebook leads')} explains why the cheap lead isn’t always the cheap customer.</p>
<p><b>Websites.</b> Most professional small-business sites in The Woodlands land between $3,000 and $15,000. A site with service-area pages, booking and integrations runs higher. Budget domain and hosting yearly, plus some support time.</p>
<p><b>Streaming TV and audio.</b> CTV CPMs average around $26 per {SRC['ctv']}, and you can target by ZIP code, which made “TV” realistic for local brands. Production is the other line item. Our {L('/blog/radio-tv-advertising-cost-houston/', 'Houston radio and TV cost guide')} has station-level detail.</p>
<p><b>Billboards.</b> {SRC['aq']} put a static freeway bulletin on I-45, I-10 or the 610 Loop at about $4,000 to $14,000 per four weeks. Full detail in our {L('/blog/billboard-advertising-cost-houston/', 'billboard cost guide')}.</p>
<p><b>Direct mail.</b> EDDM postage is $0.260 a piece since July 12, 2026, per {SRC['mp']}, so 5,000 homes in Sterling Ridge or Alden Bridge costs $1,300 in postage before printing. See {L('/blog/eddm-direct-mail-cost-the-woodlands-houston/', 'EDDM costs in The Woodlands')}.</p>"""),

            ("What do marketing agencies in Houston charge?", f"""<p>Four pricing models, often mixed:</p>
<ul>
<li><b>Monthly retainer.</b> The most common for ongoing work. Small-business retainers in Houston commonly run $1,500 to $5,000 a month; multi-channel programs for growing brands $5,000 to $20,000 and up.</li>
<li><b>Percentage of ad spend.</b> Usually 10% to 20% of media, almost always with a monthly minimum.</li>
<li><b>Project fees.</b> Websites, rebrands, launches, audits.</li>
<li><b>Hourly.</b> Mostly freelancers and consultants.</li>
</ul>
<p>For a national reference point, {SRC['ser']} found U.S. and Canadian agencies reported a median retainer of $1,863 a month, a median project of $3,625 and a median hourly rate of $112. Small sample (135 agencies), but it lines up with what we see locally.</p>
<!--fig:quote-->
<p>Be wary of very low monthly prices. A $299 SEO package almost always means automated reports and little real work. Equally, be wary of long lock-in contracts and any setup where the agency owns your Google Ads account. Our posts on {L('/blog/marketing-agency-pricing-models-retainer-vs-percentage/', 'agency pricing models')} and {L('/blog/who-owns-google-ads-account-switch-agencies/', 'who owns your ad account')} cover both.</p>"""),

            ("How much should a small business spend on marketing?", f"""<p>The figure everyone quotes comes from big companies. {SRC['gartner']} found marketing budgets averaged 7.8% of company revenue, from a survey of 401 marketing leaders at large organizations. Useful context, not a rule for a three-truck plumbing company in Tomball.</p>
<p>A better method is to work backwards from what a customer is worth:</p>
<!--fig:backwards-->
<p>Run it with real numbers. Say a new HVAC maintenance customer is worth $1,200 in gross profit over two years and you’ll pay up to $300 to win one. Ten new customers a month means a $3,000 acquisition budget. If search leads cost around $90 and one in three becomes a customer, each customer costs about $270, so search fits. If your close rate is one in six, it doesn’t, and the fix is your follow-up, not the budget. Our {L('/blog/set-a-marketing-budget-small-business/', 'budget guide')} and {L('/blog/understanding-cost-per-lead/', 'cost per lead explainer')} go step by step.</p>"""),

            ("Three sample monthly budgets for Houston-area businesses", f"""<p>These are illustrative, built from the benchmarks above and the kinds of plans we put together. They aren’t quotes, and your mix should follow your tracked results.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Starter: groomer in Spring</th><th>Growth: HVAC in Conroe</th><th>Multi-channel: two-location med spa</th></tr></thead>
<tbody>
<tr><td>Google Ads media</td><td>$1,200</td><td>$4,500</td><td>$6,000</td></tr>
<tr><td>Meta and Instagram media</td><td>$500</td><td>$1,000</td><td>$4,000</td></tr>
<tr><td>Ads management</td><td>$750</td><td>$1,500</td><td>$2,500</td></tr>
<tr><td>SEO and Business Profile</td><td>$600</td><td>$1,500</td><td>$2,500</td></tr>
<tr><td>Creative (photo, video, design)</td><td>$200</td><td>$500</td><td>$2,000</td></tr>
<tr><td>Streaming TV or mail</td><td>$0</td><td>$1,300 (one EDDM drop)</td><td>$3,000 (CTV)</td></tr>
<tr><td>Tools (call tracking, reviews, CRM)</td><td>$100</td><td>$300</td><td>$500</td></tr>
<tr><td><b>Monthly total</b></td><td><b>$3,350</b></td><td><b>$10,600</b></td><td><b>$20,500</b></td></tr>
</tbody></table></div>
<!--fig:samples-->
<p>Notice what changes as budgets grow. Media rises fastest. Management rises slower. Creative jumps once you’re on Meta and CTV, because those channels need fresh video. The starter plan skips TV and mail entirely, which is right: spread $3,000 across seven channels and none of them gets enough to work.</p>
<p>Geography changes the math too. Targeting 10 miles around The Woodlands is a very different budget from covering the whole metro out to Pearland and Fulshear.</p>
<!--fig:radius-->"""),

            ("Hidden costs nobody puts on the first quote", f"""<p>These show up in month two if nobody mentioned them in month one.</p>
<!--fig:hidden-->
<p>None of these are scams. They’re just real. Ask for an all-in monthly number with media, management, creative and tools on separate lines, and ask what happens to your accounts, pages and data if you leave.</p>
<p>If you want to know what a sensible plan would cost for your business, tell us what you sell, where your customers are and what you’re spending today, and a senior strategist will put real numbers on it. <a href="/contact/">Get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much does digital marketing cost per month for a small business in Houston?",
             "Most single-location small businesses in the Houston area spend roughly $2,500 to $12,000 a month all in, including ad spend, management, creative and tools. Lean starter plans can run near $3,000, while competitive categories like law, HVAC or med spas often spend $10,000 to $20,000 or more. A website is usually a separate one-time cost of $3,000 to $15,000."),
            ("What is a good monthly budget for Google Ads in The Woodlands?",
             "Most local businesses in The Woodlands and north Houston can learn what works with $1,500 to $3,000 a month in ad spend in a tight service area, plus management. Competitive categories such as personal injury law, roofing and emergency HVAC usually need $5,000 or more to stay visible. The 2026 national average cost per lead from search ads was $66.69, with wide swings by industry."),
            ("How much do marketing agencies charge in Houston?",
             "Houston agencies usually charge a monthly retainer, a percentage of ad spend, project fees, or a mix. Small-business retainers commonly run $1,500 to $5,000 a month, percentage pricing is typically 10% to 20% of ad spend with a minimum, and websites are quoted as projects. An SE Ranking survey put the U.S. and Canada median retainer at $1,863 a month."),
            ("Is it cheaper to hire a marketing person or an agency?",
             "For most small businesses an agency costs less than a full-time hire once you add salary, benefits, tools and the range of skills needed: ads, SEO, design and analytics rarely sit in one person. A full-time marketer makes more sense once you have enough steady work to fill their week, and many companies pair one in-house coordinator with an agency for specialist work."),
            ("What percentage of revenue should a small business spend on marketing?",
             "Gartner’s 2026 survey of large companies found marketing budgets averaged 7.8% of revenue, which many people quote as a guide. For a small business, a better method is to start with what a new customer is worth, decide what you can afford to pay to win one, and multiply by how many customers you need each month. Growing businesses usually spend a larger share."),
        ],
        "figures": {
            "headline": {
                "type": "stats",
                "title": "Four numbers to anchor a 2026 budget",
                "stats": [["$5.42", "avg. Google search ad click"], ["$66.69", "avg. Google search ad lead"], ["$27.39", "median Facebook lead"], ["$1,863", "median agency retainer, U.S./Canada"]],
                "note": "Sources: LocaliQ 2026, WordStream 2026, SE Ranking",
                "alt": "Key digital marketing cost benchmarks for Houston and The Woodlands businesses: Google Ads CPC and CPL, Facebook CPL, agency retainer",
                "caption": "National benchmarks. Competitive Houston categories run higher.",
            },
            "cpl": {
                "type": "bars",
                "title": "Google search ad cost per lead by industry",
                "sub": "2026 national medians",
                "items": [["Attorneys and legal", 131.63, "$131.63"], ["Real estate", 102.51, "$102.51"], ["Home and home improvement", 90.92, "$90.92"], ["Dentists and dental", 72.97, "$72.97"], ["All industries", 66.69, "$66.69"], ["Beauty and personal care", 39.25, "$39.25"], ["Restaurants and food", 30.57, "$30.57"]],
                "highlight": [4],
                "note": "Source: LocaliQ 2026 search advertising benchmarks",
                "alt": "Bar chart of Google Ads cost per lead by industry for budgeting digital marketing in Houston and The Woodlands",
                "caption": f"From {SRC['liq']}.",
            },
            "quote": {
                "type": "compare",
                "title": "A cheap quote vs. a real one",
                "left": {"title": "The $299 package", "items": ["One price, nothing itemized", "Automated monthly report", "No call or form tracking", "Agency owns the ad account", "12-month lock-in"]},
                "right": {"title": "A quote worth comparing", "items": ["Media, management, creative and tools on separate lines", "Named person doing the work", "Tracking set up before spend starts", "You own every account and page", "30 to 90 days’ notice to leave"]},
                "alt": "Comparison of a cheap marketing quote and a transparent agency proposal for businesses in Houston and The Woodlands",
                "caption": "Ask every agency for the right-hand column. Good ones won’t mind.",
            },
            "backwards": {
                "type": "steps",
                "title": "Build the budget backwards",
                "steps": [["Customer value", "Gross profit from an average new customer over a year or two."], ["Affordable cost", "What you’ll pay to win one, often 15% to 30% of that value."], ["Monthly goal", "How many new customers you need each month."], ["Acquisition budget", "Affordable cost times customers needed."], ["Channel check", "Compare to real cost per lead and your close rate for each channel."]],
                "alt": "Steps to build a small business marketing budget backwards from customer value for Houston and The Woodlands",
                "caption": "Close rate is the number most owners don’t know. Find it before you raise the budget.",
            },
            "samples": {
                "type": "bars",
                "title": "Three sample monthly budgets",
                "sub": "All-in totals from the table above",
                "items": [["Starter: groomer in Spring", 3350, "$3,350"], ["Growth: HVAC in Conroe", 10600, "$10,600"], ["Multi-channel: two-location med spa", 20500, "$20,500"]],
                "highlight": [1],
                "note": "Illustrative example",
                "alt": "Bar chart of three illustrative monthly digital marketing budgets for businesses in Spring, Conroe and Houston",
                "caption": "Illustrative only. Real plans follow tracked cost per customer.",
            },
            "radius": {
                "type": "map",
                "title": "Service area drives the budget",
                "sub": "Covering 10 miles around The Woodlands vs. the whole metro",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Shenandoah", "Tomball"],
                "note": "Illustrative example",
                "alt": "Map comparing a 10-mile and a metro-wide service area for digital marketing budgets in The Woodlands and Houston",
                "caption": "Each ring adds more searches and more competitors. Start tight, then widen where results justify it.",
            },
            "hidden": {
                "type": "checklist",
                "title": "Costs to ask about before you sign",
                "items": ["Setup fees for tracking and account structure", "Call tracking and CRM subscriptions", "New ad creative every few weeks", "Photography or video shoots", "Landing pages built for ads", "Minimum monthly fees on percentage pricing", "Contract length and exit terms", "Who owns the ad accounts, site and data"],
                "alt": "Checklist of hidden digital marketing costs for small businesses in Houston and The Woodlands to ask about",
                "caption": "The last two items cost the most when nobody asked.",
            },
        },
    },
]
