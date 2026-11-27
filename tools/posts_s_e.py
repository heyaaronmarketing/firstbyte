"""Refresh batch (module s_e): three existing thin posts rewritten in place, same slugs.

1. how-much-does-a-website-cost-the-woodlands (cost guide)
   Research: Squarespace published pricing (Basic $25/$19, Core $39/$29, Plus $65/$49, Advanced $139/$99);
   Shopify pricing (Basic $39 monthly / $29 yearly, Grow, Advanced; 2.9% + 30c online card rate); webhosting.today on
   Verisign's .com wholesale increase from $10.26 to $10.97 effective November 1, 2026; Texas Comptroller Publication
   96-259 (01/2026) on taxable data processing services (web hosting, web site creation and maintenance; 20% exempt);
   Grant Thornton on the amended Rule 3.330 (effective April 2, 2025; design-only blueprints not taxable); Texas
   Comptroller sales tax page (6.25% state, up to 2% local, 8.25% max); ADA.gov web accessibility guidance (Title III,
   WCAG referenced); web.dev Core Web Vitals thresholds (LCP 2.5 s, INP 200 ms, CLS 0.1 at the 75th percentile); Texas
   Tribune on Hurricane Beryl (about 2.26 million CenterPoint outages).
2. show-up-in-chatgpt-ai-search-aeo (step-by-step playbook)
   Research: BrightLocal Local Consumer Review Survey 2026 (45% use ChatGPT/AI for local recommendations, up from 6%;
   82% read AI review summaries; 47% won't use a business with fewer than 20 reviews); TechCrunch on ChatGPT's 900M
   weekly users (Feb 27, 2026); Alphabet Q2 2026 CEO remarks (AI Mode over 1 billion monthly users); Pew Research July
   2025 (8% vs 15% click rate with/without AI summary, 1% click a cited link); Google Search Central "AI features and
   your website" (no special optimization, query fan-out, no special schema); Google's "Optimizing your website for
   generative AI features" guide (updated July 2026: no llms.txt or AI text files needed, no chunking, non-commodity
   content, Business Profile feeds AI responses, scaled content abuse warning); OpenAI crawler docs (OAI-SearchBot vs
   GPTBot vs ChatGPT-User); Bing Webmaster Tools AI Performance public preview (Feb 10, 2026).
3. small-business-guide-google-ads-2026 (setup guide)
   Research: WordStream/LocaliQ 2026 Google Ads benchmarks (Apr 2025-Mar 2026, 13,474 campaigns; median CPC $5.42,
   CVR 8.18%, CPL $66.69; Home & Home Improvement $8.33/$90.92; Attorneys $9.87/$131.63; Dentists $8.00/$72.97);
   Google Ads help on daily budget overdelivery (2x a day, 30.4x a month) and the June 1, 2026 pacing change for
   day-of-week schedules; Search Engine Roundtable on the September 1, 2026 auto-upgrade of ACA and campaign-level
   broad match campaigns to AI Max; Google's AI Max help page; Google's call ads transition (creation removed Feb 2026,
   serving ends Feb 2027); PPC Land on the 10,000 PMax negative keyword limit (March 2025); Google's advanced location
   options ("Presence or interest" is the default).
Competitor/PAA phrasing read for "how much does a website cost", "website cost small business", "how to show up in
ChatGPT", "AEO for local business", "Google Ads for small business", "how much should I spend on Google Ads".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # website cost post
    "sq": A("https://squarespace.com/assets/pricing.txt", "Squarespace’s published pricing"),
    "shop": A("https://www.shopify.com/pricing", "Shopify’s pricing page"),
    "com": A("https://webhosting.today/2026/05/21/verisign-starts-a-four-year-com-price-cycle-the-first-7-hits-in-november/", "Verisign’s November 2026 increase"),
    "tx96": A("https://comptroller.texas.gov/taxes/publications/96-259.php", "Texas Comptroller Publication 96-259"),
    "gt": A("https://www.grantthornton.com/insights/alerts/tax/2025/salt/p-t/tx-updates-data-processing-services-tax-rule-04-11", "Grant Thornton’s summary of the amended rule"),
    "txrate": A("https://comptroller.texas.gov/taxes/sales/", "the Comptroller’s sales tax page"),
    "ada": A("https://www.ada.gov/resources/web-guidance", "the Justice Department’s web accessibility guidance"),
    "cwv": A("https://web.dev/articles/vitals", "Google’s Core Web Vitals thresholds"),
    "beryl": A("https://www.texastribune.org/2024/07/08/hurricane-beryl-texas-damage-updates-rain/", "the Texas Tribune"),
    # AEO post
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "tc": A("https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users", "TechCrunch"),
    "alpha": A("https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/", "Alphabet’s Q2 2026 earnings remarks"),
    "pew": A("https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/", "Pew Research Center"),
    "gai": A("https://developers.google.com/search/docs/appearance/ai-features", "Google’s “AI features and your website” page"),
    "gguide": A("https://developers.google.com/search/docs/fundamentals/ai-optimization-guide", "Google’s guide to optimizing for generative AI features"),
    "oai": A("https://developers.openai.com/api/docs/bots", "OpenAI’s crawler documentation"),
    "bing": A("https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview", "AI Performance report in Bing Webmaster Tools"),
    # Google Ads post
    "ws": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream’s 2026 Google Ads benchmarks"),
    "budget": A("https://support.google.com/google-ads/answer/2375423?hl=en", "Google’s budget help page"),
    "pacing": A("https://support.google.com/google-ads/answer/16913225", "a pacing change Google made on June 1, 2026"),
    "aimax": A("https://seroundtable.com/google-ads-migrate-ai-max-sep1-41829.html", "Search Engine Roundtable"),
    "aimaxhelp": A("https://support.google.com/google-ads/answer/15910366", "Google’s AI Max help page"),
    "callads": A("https://support.google.com/google-ads/answer/16598240?hl=en", "Google’s call ads transition notice"),
    "pmaxneg": A("https://ppc.land/google-raises-negative-keywords-limit-to-10-000-for-performance-max-campaigns/", "10,000 negative keywords"),
    "loc": A("https://support.google.com/google-ads/answer/1722038?hl=en", "Google’s advanced location options page"),
}

L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: website cost
    {
        "slug": "how-much-does-a-website-cost-the-woodlands",
        "date": "2026-05-07",
        "modified": "2026-11-27",
        "title": "How Much Does a Website Cost in The Woodlands and Houston? (2026 Price Guide)",
        "seo_title": "How Much Does a Website Cost in The Woodlands? (2026)",
        "desc": "What a small business website costs in The Woodlands and Houston in 2026: price tiers, line items, platform fees, Texas sales tax and yearly upkeep.",
        "category": "Web design",
        "icons": ["Google", "Google Analytics", "Search Console"],
        "art": "b2",
        "hero": "browser",
        "hero_alt": "Illustration of a browser window for a guide to website cost in The Woodlands and Houston",
        "related": ["wordpress-vs-wix-vs-squarespace-vs-webflow-small-business", "signs-your-website-needs-a-redesign", "website-redesign-without-losing-seo-rankings"],
        "sections": [
            (None, f"""<p>Three website quotes on one desk in a Research Forest office park: $1,400, $8,800 and $31,000. Same business, same request, same “we just need a new site.” The owner’s first instinct is that somebody is crazy. Usually nobody is. The three quotes describe three different products that happen to share a name.</p>
<p><b>Short answer:</b> most small business websites in The Woodlands and Houston cost between $3,000 and $15,000 to build in 2026, plus roughly $300 to $2,500 a year to keep online and current. A five-page template site sits at the bottom. A custom service business site with location pages, booking and real SEO work lands in the middle. Ecommerce and custom features push past $20,000.</p>
<p>The rest of this guide is the detail behind that number: what each price tier actually buys, the line items hiding inside a quote, the yearly bills nobody mentions, Texas sales tax (yes, it applies), and how to tell a fair quote from a padded one.</p>"""),

            ("How much does a small business website cost in The Woodlands?", f"""<p>These are the tiers we see in proposals across Greater Houston, including the ones owners bring to us for a second opinion. They come from our experience and aren’t survey data, but they match what most local shops charge.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Tier</th><th>Typical build cost</th><th>What you get</th><th>Who it fits</th></tr></thead>
<tbody>
<tr><td>DIY builder</td><td>$0 up front, $200 to $1,200 a year</td><td>A Squarespace, Wix or Shopify template you set up yourself</td><td>Brand-new businesses testing an idea, side businesses</td></tr>
<tr><td>Freelancer template</td><td>$1,500 to $4,000</td><td>5 to 8 pages on a theme, your copy and photos, basic contact form</td><td>Solo operators who need something credible fast</td></tr>
<tr><td>Small agency starter</td><td>$4,000 to $8,000</td><td>Custom-styled design, 8 to 15 pages, written copy, on-page SEO, tracking set up</td><td>Established local businesses with one location</td></tr>
<tr><td>Service business build</td><td>$8,000 to $18,000</td><td>Service pages, area pages for Spring, Conroe, Tomball and so on, booking or quote flow, CRM hookup</td><td>Contractors, clinics, firms that win on search</td></tr>
<tr><td>Ecommerce or custom</td><td>$15,000 to $50,000+</td><td>Product catalog, payments, integrations, member areas, custom tools</td><td>Retail, product brands, multi-location groups</td></tr>
</tbody></table></div>
<!--fig:tiers-->
<p>Those ranges are wide on purpose. A 12-page site for a law firm in Hughes Landing and a 12-page site for a landscaper in Magnolia can cost the same or differ by half, depending on how much writing, photography and strategy each needs.</p>
<p>Anything advertised at a few hundred dollars for a “complete website” is usually a template with your logo dropped in, hosted on the seller’s account. It may be fine for a month. Read the ownership terms before you pay for it, because those are the sites owners most often struggle to move later (we wrote a whole post on {L('/blog/get-website-domain-back-from-web-designer/', 'getting your domain back from a web designer')}).</p>"""),

            ("What’s inside a website quote: the line items", f"""<p>A good quote breaks the work into parts. If yours is one number with “website design” next to it, ask for the breakdown. Here’s roughly how the hours split on a mid-tier service business site in our experience.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Share of a mid-tier budget</th><th>What it covers</th><th>Can you skip it?</th></tr></thead>
<tbody>
<tr><td>Discovery and sitemap</td><td>5% to 10%</td><td>Goals, competitors, page list, which searches to target</td><td>No. Skipping it is how sites end up pretty and useless.</td></tr>
<tr><td>Design</td><td>20% to 30%</td><td>Layouts for home, service, area and contact pages, mobile versions</td><td>Partly, with a good template</td></tr>
<tr><td>Copywriting</td><td>15% to 25%</td><td>Every word on every page, written to rank and to sell</td><td>Only if you can really write</td></tr>
<tr><td>Development</td><td>20% to 30%</td><td>Building the pages, forms, booking, speed work, CMS setup</td><td>No</td></tr>
<tr><td>Photos and video</td><td>0% to 15%</td><td>A half-day shoot at your shop, team, trucks, work in progress</td><td>Yes, but stock photos cost you trust</td></tr>
<tr><td>SEO setup</td><td>5% to 10%</td><td>Titles, schema, redirects from the old site, Search Console, sitemaps</td><td>No, especially on a redesign</td></tr>
<tr><td>Tracking and launch</td><td>5%</td><td>GA4, call and form tracking, testing on real phones</td><td>No</td></tr>
</tbody></table></div>
<p>Copywriting is the line owners cut first and regret most. Most owners can explain their business beautifully out loud. Very few can turn that into a page that answers “AC repair Spring TX” better than the nine other companies on page one. If you’re writing it yourself, our {L('/blog/website-copy-that-sells/', 'guide to website copy that sells')} will save you a few drafts.</p>
<p>Redirects deserve their own sentence. If you’re replacing an older site that ranks, every old URL needs to point to its new equivalent. Skip that and you can lose years of search traffic in a week. The {L('/blog/website-redesign-without-losing-seo-rankings/', 'redesign without losing rankings')} post walks through it.</p>"""),

            ("Why do two Houston web designers quote $2,000 and $20,000 for the same site?", f"""<p>Because they aren’t quoting the same site. When we lay two quotes side by side for an owner, the gap almost always comes from four things: who writes the words, whether anyone researched what customers search for, how many pages target specific services and towns, and what happens after launch.</p>
<!--fig:quotes-->
<p>Neither quote is automatically wrong. A $2,000 site is a reasonable purchase for a new business that gets its customers from referrals and just needs to look real when someone checks. It’s the wrong purchase for a plumbing company that needs Google to send 40 calls a month.</p>
<p>The question to ask each bidder is simple: “What will this site do for my business in a year that the cheaper one won’t?” A good designer has a specific answer. A weak one talks about colors.</p>"""),

            ("The yearly bill after launch", f"""<p>The build is one check. The site also has running costs, and they’re where surprise invoices come from.</p>
<p><b>Platform or hosting.</b> {SRC['sq']} lists Basic at $25 a month billed monthly ($19 a month on an annual plan), Core at $39 ($29 annually), Plus at $65 ($49) and Advanced at $139 ($99). {SRC['shop']} lists Basic at $39 a month or $29 billed yearly, plus card fees starting at 2.9% + 30¢ online. A WordPress site on decent managed hosting usually runs $25 to $60 a month in our experience, more for busy stores. Static sites like ours can cost almost nothing to host.</p>
<p><b>Domain.</b> A .com still costs most businesses somewhere around $15 to $25 a year at retail. The wholesale price went up again with {SRC['com']}, from $10.26 to $10.97, so expect registrars to nudge renewals. Put the domain in your own name and on your own card.</p>
<p><b>Email.</b> Google Workspace or Microsoft 365, per user per month. Not part of the website, but often bundled into a designer’s invoice so you lose track of it.</p>
<p><b>Plugins, apps and licenses.</b> Booking tools, form builders, review widgets, premium themes. Each is $5 to $50 a month and they add up quietly.</p>
<p><b>Maintenance and updates.</b> $50 to $500 a month depending on what’s included. For WordPress this means updates and security patches. On any platform it should include small text and photo changes, so your hours and prices don’t sit wrong for six months.</p>
<!--fig:running-->
<p>Be wary of any agency whose mandatory monthly plan is the only way your site stays online, especially if the site lives on their account. Paying for ongoing help is fine. Being unable to leave is not.</p>"""),

            ("Does Texas charge sales tax on website design?", f"""<p>Often, yes, and plenty of owners find out from their accountant after the fact. {SRC['tx96']} lists “web hosting, web site creation and maintenance” as examples of data processing, a taxable service in Texas, and says 20 percent of the charge for data processing is exempt.</p>
<p>The rule was amended in 2025. Per {SRC['gt']}, design that only produces a blueprint or plan for a website isn’t taxable, while creation, repair and maintenance are taxable when they involve storing, manipulating, compiling or entering data. In practice, most website builds land on the taxable side.</p>
<p>Rates: the state rate is 6.25 percent, and cities, counties and special districts can add up to 2 percent, for a combined maximum of 8.25 percent, per {SRC['txrate']}. Much of the Houston area, including The Woodlands, sits at that 8.25 percent cap, but check the exact rate for your address.</p>
<p>An illustrative example: on a $10,000 build that’s fully taxable as data processing, 20 percent is exempt, so tax applies to $8,000. At 8.25 percent, that’s $660. Ask your bidders whether their quote includes tax, and ask your CPA how your specific contract should be treated. We’re marketers; this paragraph is a heads-up, not tax advice.</p>"""),

            ("The costs owners forget: photos, speed and accessibility", f"""<p>Three things rarely show up in the first quote and almost always come up later.</p>
<p><b>Real photos.</b> A half-day shoot of your team, trucks, office or work in progress usually runs $500 to $2,000 around Houston. It’s the cheapest trust you can buy. Customers in Kingwood can spot the same smiling stock-photo technician that’s on a competitor’s site in Katy.</p>
<p><b>Speed.</b> Google measures real visitors’ experience with Core Web Vitals. {SRC['cwv']} call a page good when its largest content loads within 2.5 seconds, it responds to taps within 200 milliseconds and the layout barely shifts (a CLS of 0.1 or less), measured at the 75th percentile of visits on mobile and desktop. Heavy page builders, autoplay video and a dozen tracking scripts are how sites miss those numbers. Ask bidders what scores their recent sites get on a phone, not a laptop.</p>
<p><b>Accessibility.</b> {SRC['ada']} says Title III of the ADA covers businesses open to the public and points to WCAG as a helpful technical standard for websites. Building to WCAG from the start costs a little more. Retrofitting after a demand letter costs a lot more. Our {L('/blog/website-accessibility-matters/', 'website accessibility post')} covers the basics.</p>
<!--fig:forgotten-->"""),

            ("How many pages does a Houston service business need?", f"""<p>Page count drives price more than anything else, so it’s worth getting right. For a service business, a page earns its keep if it answers a search someone actually types.</p>
<ul>
<li>Home, about, contact. Everyone needs these.</li>
<li>One page per main service. “Water heater replacement” and “slab leak repair” are different searches with different buyers. Lumping them on one “Services” page throws away rankings.</li>
<li>One page per town you really serve, with real local detail: which neighborhoods, how fast you get there, local jobs you’ve done, local reviews. The Woodlands, Spring, Conroe, Tomball, Magnolia and Kingwood are the usual set for a company based off I-45 or the Grand Parkway.</li>
<li>Reviews or project gallery, financing if you offer it, and an FAQ.</li>
</ul>
<!--fig:areas-->
<p>A typical home service build ends up at 15 to 30 pages. That sounds like a lot until you see the analytics a year later and notice the Conroe page brings in more calls than the homepage. Area pages only work if they’re genuinely different from each other, though. Swapping the town name into the same paragraph 12 times is a known pattern, and Google treats it that way. See {L('/blog/power-of-local-landing-pages/', 'our local landing pages guide')} for what a good one looks like.</p>"""),

            ("Hosting and hurricane season", f"""<p>A Houston-specific cost question: where does your site live when the power goes out? After Hurricane Beryl in July 2024, CenterPoint’s outage count started at about 2.26 million customers, per {SRC['beryl']}. A site hosted on a server in your office closet went down with the building. A site on a reputable cloud host or CDN stayed up, which mattered for every business that needed to post “we’re open on generator power” or “closed until Thursday.”</p>
<p>Two cheap habits help. Make sure someone outside your office can edit the site (a phone login is fine). And keep a ready-made alert banner you can switch on in two minutes. Our {L('/blog/hurricane-season-marketing-playbook-houston-the-woodlands/', 'hurricane season marketing playbook')} has the rest of the storm checklist.</p>"""),

            ("How to read a website quote before you sign", f"""<p>Most bad website experiences we hear about weren’t caused by bad design. They came from a vague contract. Before you sign, walk through these.</p>
<!--fig:quotecheck-->
<p>Three red flags we see in Houston quotes over and over: the designer registers the domain in their own name, the price includes “SEO” with no description of what that means, and there’s no line about what happens to the site if you stop paying the monthly plan. Our {L('/blog/marketing-agency-contract-red-flags/', 'agency contract red flags')} post covers more of them.</p>
<p>Timelines matter too. A template site can launch in two to four weeks. A custom service business site usually takes eight to twelve weeks, and the delay is almost always content: photos not shot, copy not approved, an old site login nobody can find.</p>"""),

            ("Is a $10,000 website worth it? Run the math on your own numbers", f"""<p>The useful way to judge a website price is by what it returns, which means doing a little arithmetic with your own numbers. Here’s an illustrative example for a home service company in Spring.</p>
<!--fig:payback-->
<p>The old site converts 2% of visitors into calls and forms. The new one, with clear service pages, prices, reviews and a click-to-call button, converts 4%. On 1,200 visits a month, that’s 24 extra leads. If 40% book and the average job is $650, the difference is roughly 10 jobs and $6,000 a month. A $10,000 site pays back in under two months on those assumptions.</p>
<p>Change the assumptions to your own. If your business lives on referrals and the site gets 150 visits a month, the math says buy the cheaper site and spend the difference elsewhere. If you run Google Ads, the math gets more lopsided, because every click you pay for lands on the site. Doubling the conversion rate halves your cost per lead without changing the ad budget. We cover that link in {L('/blog/turn-your-website-into-a-lead-machine/', 'turning your website into a lead machine')}.</p>
<p>Our {L('/services/web-design-seo-pr/', 'web design team')} builds custom, fast, mobile-first sites with local SEO and tracking included, and we put the price in writing before we start. If you’d like a real number for your project, <a href="/contact/">get in touch</a> and tell us what the site needs to do.</p>"""),
        ],
        "faq": [
            ("How much should a website cost for a plumber or contractor in The Woodlands?",
             "Most contractors in The Woodlands and Houston spend $6,000 to $18,000 on a site that actually generates calls. That budget covers a page for each main service, pages for the towns you serve such as Spring, Conroe and Tomball, written copy, real photos, click-to-call, quote forms and call tracking. A cheaper template can work for a new company that runs on referrals, but it rarely ranks."),
            ("How much does it cost to maintain a website per month?",
             "Plan on roughly $25 to $150 a month for hosting or a platform plan, about $15 to $25 a year for a .com domain, and $50 to $500 a month if you pay someone for updates, security and small edits. WordPress sites need more upkeep than hosted builders like Squarespace or Shopify. Add any paid plugins or apps, which often run $5 to $50 each per month."),
            ("Is it cheaper to build a website on Wix or hire a web designer in Houston?",
             "Building it yourself on Wix, Squarespace or Shopify is cheaper in cash, usually a few hundred dollars a year. It costs time, and most DIY sites underperform on copy, speed and local SEO. Hiring a Houston designer costs more up front but should come with written copy, service and area pages and tracking. If your customers find you through Google, the paid site usually earns back the difference."),
            ("Do I have to pay sales tax on a website in Texas?",
             "Usually. The Texas Comptroller treats web hosting and website creation and maintenance as data processing, a taxable service, with 20 percent of the charge exempt. Design that only produces a plan or blueprint is not taxable under the 2025 rule. With the 8.25 percent combined rate common around Houston, tax on a $10,000 build can be about $660. Confirm treatment of your contract with a CPA."),
            ("Who should own my domain and website when I hire a designer?",
             "You should. Register the domain in your name with your own email and card, and make sure the contract says you own the finished site, content and photos, with logins handed over at launch. If the site runs on the designer's hosting account, ask how you would move it if you leave. Ownership problems are the most common reason Houston owners end up paying for a site twice."),
        ],
        "figures": {
            "tiers": {
                "type": "bars",
                "title": "Website build cost by tier",
                "sub": "Midpoint of typical quotes we see in Houston and The Woodlands",
                "items": [["DIY builder (first year)", 700, "$700"], ["Freelancer template", 2750, "$2,750"], ["Small agency starter", 6000, "$6,000"], ["Service business build", 13000, "$13,000"], ["Ecommerce or custom", 32500, "$32,500"]],
                "highlight": [3],
                "note": "Illustrative example based on our experience, not a survey",
                "alt": "Bar chart of website cost tiers for small businesses in The Woodlands and Houston, from DIY builders to ecommerce",
                "caption": "The service business tier is where most local companies that rely on Google land.",
            },
            "quotes": {
                "type": "compare",
                "title": "A $2,000 quote vs. a $12,000 quote",
                "left": {"title": "Typical $2,000 quote", "items": ["Theme with your logo and colors", "You write and supply all copy", "One “Services” page for everything", "No keyword or competitor research", "Hosted on the designer’s account", "Help after launch billed hourly"]},
                "right": {"title": "Typical $12,000 quote", "items": ["Design built around your sales process", "Copy written to rank and convert", "A page per service and per town", "Research on what Houston customers search", "Domain and site in your name", "Tracking for calls and forms from day one"]},
                "alt": "Comparison of a cheap and a mid-range website quote for a small business in The Woodlands and Houston",
                "caption": "The price gap is mostly words, research and pages, not design polish.",
            },
            "running": {
                "type": "stats",
                "title": "The yearly bill after launch",
                "stats": [["$10.97", ".com wholesale price per year from Nov 1, 2026"], ["$348", "a year for Squarespace Core billed annually"], ["$29/mo", "Shopify Basic billed yearly, plus card fees"], ["8.25%", "top combined Texas sales tax rate"]],
                "note": "Sources: Verisign via webhosting.today, Squarespace, Shopify, Texas Comptroller",
                "alt": "Stats on yearly website running costs for Houston and The Woodlands businesses, including domain, platform and Texas sales tax",
                "caption": f"Prices from {SRC['sq']}, {SRC['shop']} and {SRC['txrate']}.",
            },
            "forgotten": {
                "type": "checklist",
                "title": "Costs that rarely make the first quote",
                "sub": "Ask about each one before you sign",
                "items": ["Professional photos of your team and work", "Copywriting for every page", "Redirects from your old site’s URLs", "Accessibility to WCAG guidelines", "Speed testing on real phones", "Call and form tracking set up", "Texas sales tax on the build", "Paid plugins, apps and licenses"],
                "alt": "Checklist of hidden website costs for small businesses in Houston and The Woodlands",
                "caption": "Each of these is cheaper to plan for than to add after launch.",
            },
            "areas": {
                "type": "map",
                "title": "Area pages for a business based in The Woodlands",
                "sub": "Towns that often deserve their own page, if you truly serve them",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Magnolia", "Kingwood", "Shenandoah"],
                "alt": "Map of Greater Houston towns that a The Woodlands business website might target with area pages",
                "caption": "Each area page should carry local detail, not the same paragraph with a new town name.",
            },
            "quotecheck": {
                "type": "steps",
                "title": "Read a website quote in five checks",
                "sub": "Do these before you sign anything",
                "steps": [["Scope", "Page list, number of revisions and who writes the copy, in writing."], ["Ownership", "Domain, site files, photos and logins belong to you."], ["SEO detail", "What “SEO included” means: research, titles, redirects, schema."], ["Running costs", "Hosting, plugins, maintenance and what happens if you cancel."], ["Tax and timeline", "Whether sales tax is included and a realistic launch date."]],
                "alt": "Five steps to review a website design quote for a business in The Woodlands or Houston",
                "caption": "A good designer will be glad you asked. A vague answer to step two is a reason to walk away.",
            },
            "payback": {
                "type": "funnel",
                "title": "How a better site pays for itself",
                "stages": [["1,200 monthly visits", "same traffic"], ["Conversion rises 2% to 4%", "+24 leads"], ["40% of new leads book", "+10 jobs"], ["Average job $650", "+$6,500"], ["$10,000 build cost", "~2 months"]],
                "note": "Illustrative example. Use your own traffic, close rate and job value.",
                "alt": "Funnel showing how a new website can pay back its cost for a home service business in Spring and The Woodlands",
                "caption": "If your site gets little traffic, the same math may favor a cheaper build.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: AEO
    {
        "slug": "show-up-in-chatgpt-ai-search-aeo",
        "date": "2026-04-02",
        "modified": "2026-11-27",
        "title": "How to Show Up in ChatGPT and AI Search (AEO): A Playbook for Houston and The Woodlands Businesses",
        "seo_title": "How to Show Up in ChatGPT and AI Search (AEO) in Houston",
        "desc": "How Houston and The Woodlands businesses get named in ChatGPT, Google AI Mode and Copilot answers: crawler settings, Business Profile, mentions, tracking.",
        "category": "SEO",
        "icons": ["Google", "Google Business Profile", "Search Console"],
        "art": "b4",
        "hero": "speech",
        "hero_alt": "Illustration of a chat bubble for showing up in ChatGPT and AI search for Houston and The Woodlands businesses",
        "related": ["ai-overviews-local-search-houston", "rank-in-google-map-pack-houston", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>“Why does ChatGPT recommend my competitor?” We hear some version of that from Houston owners most weeks now. Usually they typed something like “best roofer in The Woodlands” into ChatGPT, got three names, and theirs wasn’t one of them.</p>
<p><b>Short answer:</b> to show up in ChatGPT and AI search, make your website readable by AI crawlers, state plainly what you do and where, keep your Google Business Profile complete with a steady flow of reviews, and get mentioned on local sites that AI tools already trust. AEO (answer engine optimization) is good local SEO with a few extra settings. There’s no secret file.</p>
<p>This is the step-by-step version, with the settings to check, the copy to change, the things to skip, and a simple way to measure whether any of it is working.</p>"""),

            ("How many Houston customers actually ask AI for recommendations?", f"""<p>Enough that ignoring it is no longer the safe choice. In {SRC['bl']}, 45% of U.S. consumers said they’d used ChatGPT or another AI tool to find local business recommendations, up from 6% the year before. That made AI the third most popular source in the survey.</p>
<p>The audience is huge on both sides. ChatGPT passed 900 million weekly users in February 2026, per {SRC['tc']}, and Google says AI Mode has passed 1 billion monthly users since its global expansion, per {SRC['alpha']}.</p>
<p>The catch is clicks. A {SRC['pew']} study found Google users clicked a regular result on 8% of visits when an AI summary appeared, against 15% when one didn’t, and clicked a link inside the summary itself on just 1% of visits. The answer box is increasingly the whole experience. If you aren’t named in it, a lot of people never see your listing at all.</p>
<!--fig:stats-->"""),

            ("Where ChatGPT, Google AI Mode, Gemini and Copilot get their answers", f"""<p>Each tool assembles answers differently, and that tells you where to work. Google says its AI Overviews and AI Mode may use “query fan-out,” issuing several related searches across subtopics and data sources to build one response, per {SRC['gai']}. The others work along similar lines: search, pick sources, write.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Tool</th><th>Where answers come from</th><th>What you can check or control</th></tr></thead>
<tbody>
<tr><td>ChatGPT (with search)</td><td>Pages found by OpenAI’s OAI-SearchBot crawler and search partners, plus map-style business listings for local questions</td><td>Allow OAI-SearchBot in robots.txt; watch chatgpt.com referrals in GA4</td></tr>
<tr><td>Google AI Overviews and AI Mode</td><td>Google’s own index and Business Profile data</td><td>Indexing in Search Console; a complete Business Profile</td></tr>
<tr><td>Gemini</td><td>Google Search and Google Maps data</td><td>Same as above</td></tr>
<tr><td>Microsoft Copilot</td><td>Bing’s index</td><td>Bing Webmaster Tools, including its AI citation report</td></tr>
<tr><td>Perplexity</td><td>Its own crawler (PerplexityBot) plus live web search</td><td>Allow PerplexityBot; watch perplexity.ai referrals</td></tr>
</tbody></table></div>
<!--fig:fanout-->
<p>The practical takeaway for a Houston business: you’re not optimizing for one robot. You’re making sure your facts are readable and consistent in the five or six places all of them read from, which is your site, your Google profile, Bing, review sites and local press.</p>"""),

            ("Step 1: Make sure AI crawlers can read your site", f"""<p>This is the step nobody checks, and it takes ten minutes. Some sites block AI crawlers without the owner knowing, through a security plugin, a hosting setting or a robots.txt file someone copied from a blog post in 2023.</p>
<p>OpenAI runs separate crawlers for separate jobs, per {SRC['oai']}. <b>OAI-SearchBot</b> surfaces websites in ChatGPT’s search features; block it and your pages won’t appear in ChatGPT search answers. <b>GPTBot</b> crawls content that may be used to train OpenAI’s models; blocking it opts you out of training without affecting search. <b>ChatGPT-User</b> fetches a page when a person asks ChatGPT to look at it.</p>
<p>So a business can reasonably block training and still allow search. Most local service businesses we work with allow both, since there’s little to protect on a page about water heater installation in Tomball, but it’s your call.</p>
<!--fig:bots-->
<p>Then check the basics that matter for every engine. Pages need to be indexed and eligible to show a snippet in Google to appear in AI features, according to {SRC['gai']}, which also says there are no additional technical requirements. Use the URL Inspection tool in Search Console on your key service pages. And verify your site in Bing Webmaster Tools, since Copilot leans on Bing’s index and most small businesses have never logged in there.</p>"""),

            ("Step 2: Say plainly who you are, where and for whom", f"""<p>AI tools quote specifics. Vague copy gives them nothing to quote. When an answer says “X Plumbing is a family-owned company in Spring that handles slab leaks and repiping across north Harris County,” it pulled that sentence, or something close, from a page that said it clearly.</p>
<!--fig:copy-->
<p>Go page by page and make sure these facts are stated in plain sentences, not buried in images or sliders: your business name exactly as it appears on Google, what you do (each main service named), where (towns and neighborhoods you actually serve, like Shenandoah, Oak Ridge North or Atascocita), who you serve, hours, licenses and how long you’ve been doing it.</p>
<p>Then add what only you can say. Google’s generative AI guide calls this non-commodity content, meaning “unique expert or experienced takes that go beyond common knowledge and the ordinary,” and describes it as a major factor in long-term visibility, per {SRC['gguide']}. For a Houston business, that’s things like why clay soil in Katy cracks slabs differently than sandy soil in Magnolia, what you actually charge for a diagnostic, or how you handle insurance after a hail storm. A generic “10 tips for a healthy lawn” page is commodity content. AI can write that itself and doesn’t need to cite you.</p>
<p>Keep schema markup accurate (LocalBusiness, services, FAQ where it fits) but don’t expect it to work miracles. Google says there’s no special structured data you need to add for AI features, and that markup should match the visible text on the page, per {SRC['gai']}.</p>"""),

            ("Step 3: Treat your Google Business Profile as an AI source", f"""<p>For local questions, the Business Profile may matter more than the website. Google’s guide says AI responses can include local business information, and that Business Profiles can help your products and services show up in AI responses as well as regular search results, per {SRC['gguide']}.</p>
<p>What to check, in Business Profile manager:</p>
<ul>
<li><b>Primary category</b> matches your main money service. Secondary categories cover the rest of what you really do.</li>
<li><b>Services</b> are listed one by one, with short descriptions written like you’d explain them on the phone.</li>
<li>Hours, holiday hours and the service area are accurate. AI answers repeat wrong hours with total confidence.</li>
<li>Attributes (women-owned, veteran-owned, wheelchair accessible, Spanish spoken, online estimates) are filled in where true. They match the qualifiers people add to AI prompts.</li>
<li>Photos are recent and real.</li>
</ul>
<p>Reviews feed AI answers directly. BrightLocal found 82% of consumers read AI-generated review summaries, 47% won’t use a business with fewer than 20 reviews, and 74% only care about reviews from the last three months, per {SRC['bl']}. A profile with 300 reviews from 2021 and nothing since reads stale to people and to software. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has request scripts, and {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Houston map pack')} covers the rest of the profile work.</p>"""),

            ("Step 4: Get mentioned where AI tools already look", f"""<p>When an AI answer recommends three businesses, it’s often echoing a “best of” list, a news story, a Reddit thread or a review site. Your own site saying you’re great counts for little. Other credible sites saying it counts for a lot.</p>
<p>Local places that tend to get cited for Houston-area questions include Community Impact, the Houston Chronicle and local TV station sites, chamber of commerce directories (The Woodlands Area Chamber, the Greater Houston Partnership, Conroe and Tomball chambers), industry association member directories, Yelp, Nextdoor, BBB, and subreddits like r/houston and r/TheWoodlands.</p>
<p>How to earn the mentions without faking them:</p>
<ol>
<li>Pitch a useful local story to Community Impact or a TV station: a storm-prep tip, a data point from your own jobs, a new location. Our {L('/blog/get-press-coverage-houston-the-woodlands/', 'press coverage guide')} has the pitch format.</li>
<li>Join the chambers and associations you’d join anyway, and fill out the directory profile completely. {L('/blog/chambers-networking-groups-the-woodlands-houston/', 'Our chamber guide')} compares the local ones.</li>
<li>Sponsor something real (a youth league, a school fundraiser) that produces a link and a local mention.</li>
<li>Answer questions honestly in community forums when you can help, under your real name, without spamming links.</li>
</ol>
<p>Don’t buy mentions or plant fake ones. Google’s guide specifically lists inauthentic brand mentions among the tactics site owners can skip, per {SRC['gguide']}. Fake Reddit praise also tends to get spotted and screenshotted, which is the opposite of what you wanted.</p>"""),

            ("Step 5: Answer the questions people actually type into ChatGPT", f"""<p>People talk to AI tools in full sentences with conditions attached. They don’t type “plumber Spring TX.” They type “who can fix a slab leak in Spring this week and do they work with insurance?”</p>
<p>Collect those questions from your own phone calls and emails for two weeks. Typical Houston examples we see:</p>
<ul>
<li>“Which AC companies in The Woodlands are open on Sunday in August?”</li>
<li>“Best pediatric dentist near Kingwood that takes Medicaid”</li>
<li>“How much does foundation repair cost in Katy, and how long does it take?”</li>
<li>“Family law attorney in Conroe who offers payment plans”</li>
</ul>
<p>Then make sure your site answers them in plain language: on the relevant service page, in an FAQ section, or in a blog post if the question needs room. Put the direct answer in the first sentence or two, then the detail. That format works for featured snippets and AI answers alike.</p>
<p>Don’t go the other way and spin up a page for every possible variation. Google’s guide warns that creating pages for every possible AI sub-query, mainly to manipulate rankings or AI responses, can violate its scaled content abuse policy, per {SRC['gguide']}. Thirty genuinely useful answers beat 300 near-duplicates.</p>"""),

            ("What doesn’t help: llms.txt, AI rewrites and schema overload", f"""<p>Plenty of AEO advice online is selling something. Per {SRC['gguide']}, Google Search ignores AI text files, special markup and Markdown versions of pages, so creating them won’t help or hurt your visibility in Google. The same guide says you don’t need to chop content into tiny pieces for AI and that page length should suit your audience.</p>
<p>A word on llms.txt, since owners ask about it constantly. It’s a proposed file that lists your key pages for AI tools. We publish one ourselves because it takes five minutes and costs nothing, and some non-Google tools may read it. We’d never pay anyone to “optimize” one, and we wouldn’t expect it to change a single Google answer.</p>
<p>Also skip: rewriting your whole site in a robotic Q&amp;A style, stuffing every schema type you can find onto every page, and tools that promise to “submit” your business to ChatGPT. There’s no submission form.</p>"""),

            ("How do you track whether ChatGPT is recommending you?", f"""<p>Imperfectly, but better than a year ago. Three sources, from most to least reliable:</p>
<p><b>GA4 referrals.</b> In GA4, go to Reports, then Acquisition, then Traffic acquisition, and look at session source for chatgpt.com, perplexity.ai, copilot.microsoft.com and gemini.google.com. ChatGPT also adds a utm_source=chatgpt.com tag to many links it shows. Counts are small for most local businesses, and people who read your name in an answer often call or search your name instead of clicking, so treat this as a floor.</p>
<p><b>Bing’s citation data.</b> The {SRC['bing']}, launched in public preview in February 2026, shows how often your pages are cited in Copilot and Bing’s AI summaries, which pages get cited, and a sample of the queries the AI used to find them. It’s one of the first citation reports to come straight from a major engine. Google’s Search Console doesn’t break AI Mode out the same way.</p>
<p><b>A monthly prompt audit.</b> Write 15 to 20 prompts your customers would use, run them in ChatGPT, Google AI Mode, Gemini and Copilot on the same day each month, and log the results in a sheet like this one.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Prompt</th><th>Tool</th><th>Were we named?</th><th>Who was named</th><th>Sources it cited</th></tr></thead>
<tbody>
<tr><td>best HVAC company in The Woodlands</td><td>ChatGPT</td><td>No</td><td>Three competitors</td><td>Yelp list, a Community Impact story</td></tr>
<tr><td>AC repair Spring TX open Sunday</td><td>Google AI Mode</td><td>Yes, second</td><td>Us plus two others</td><td>Business Profiles</td></tr>
<tr><td>who does ductless mini splits near Conroe</td><td>Gemini</td><td>No</td><td>One competitor</td><td>Competitor’s service page</td></tr>
</tbody></table></div>
<p>The example rows are illustrative. The “sources it cited” column is the useful one, because it tells you exactly which site to get onto next. Results also vary by run and by who’s asking, so look for trends over three months rather than reacting to one answer.</p>
<!--fig:audit-->"""),

            ("Does AEO work differently for The Woodlands than for Houston proper?", f"""<p>A little. AI tools interpret “near” loosely. Ask for “the best electrician near The Woodlands” and you may get businesses in Spring, Conroe and Tomball, because the tool is matching on the region, the reviews and the pages that mention the area. A business in Shenandoah with a page about The Woodlands and reviews mentioning Creekside Park can beat a closer company whose site never names a neighborhood.</p>
<!--fig:near-->
<p>Inside the Loop it’s the reverse: lots of competitors in a small area, so the qualifiers in the prompt (open late, Spanish-speaking, takes insurance, free estimates) do more of the sorting. That’s an argument for filling in every Business Profile attribute that’s true and writing those details on your pages in plain words. If you serve both, our {L('/blog/the-woodlands-spring-conroe-address-local-seo/', 'post on The Woodlands, Spring and Conroe addresses')} explains how Google treats the area’s overlapping place names.</p>"""),

            ("A 90-day AEO plan for a Houston small business", f"""<p>None of this needs a new budget line. Most of it is cleanup and consistency that also helps your regular Google rankings, which is why we fold it into {L('/services/search-marketing/', 'search marketing')} work rather than selling it separately.</p>
<!--fig:plan-->
<p>Expect results to trail the work. AI answers are built from what’s indexed and written about you, and new reviews, mentions and pages take weeks to months to get crawled and reflected. Google itself says changes to its controls can take several days to several months to show up, per {SRC['gai']}. Run the prompt audit monthly and give it a full quarter before judging.</p>
<p>If you’d like a senior strategist to run the prompt audit for your business and build a plan from what it finds, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I get my business recommended by ChatGPT in Houston?",
             "Allow OpenAI's OAI-SearchBot crawler in your robots.txt, state your services and the Houston-area towns you serve in plain sentences on your site, and keep your Google Business Profile complete with recent reviews. Then earn mentions on local sites ChatGPT tends to cite, such as Community Impact, chamber directories, Yelp and industry lists. There is no form to submit your business to ChatGPT."),
            ("Does schema markup help with Google AI Overviews?",
             "Accurate schema helps Google understand your business, but Google says there is no special structured data required to appear in AI Overviews or AI Mode, and markup should match the visible text on the page. Use LocalBusiness and relevant service or FAQ markup where it fits. Clear page content, indexing and a strong Business Profile matter more than adding every schema type."),
            ("Should I block GPTBot on my website?",
             "It depends on whether you mind your content being used to train OpenAI's models. Blocking GPTBot opts you out of training but does not remove you from ChatGPT search, which uses a separate crawler called OAI-SearchBot. Most local service businesses allow both. If you block anything, make sure OAI-SearchBot, Googlebot, Bingbot and PerplexityBot can still crawl your service pages."),
            ("How can I see if ChatGPT sends traffic to my website?",
             "In GA4, open Reports, then Acquisition, then Traffic acquisition, and look for chatgpt.com, perplexity.ai, copilot.microsoft.com and gemini.google.com as sources. ChatGPT also tags many links with utm_source=chatgpt.com. Numbers are usually small because people often call or search your name after reading an answer, so pair GA4 with a monthly prompt audit and Bing Webmaster Tools citation data."),
            ("Is AEO different from SEO for a local business in The Woodlands?",
             "Mostly no. Google says its AI features run on its core ranking systems and need no special optimization, so the foundation is the same local SEO: indexed pages, clear service and area content, a complete Business Profile and reviews. AEO adds a few checks, such as AI crawler access, Bing Webmaster Tools, more question-and-answer content and earning mentions on sites AI tools cite."),
        ],
        "figures": {
            "stats": {
                "type": "stats",
                "title": "AI search, by the numbers",
                "stats": [["45%", "of consumers used AI tools for local recommendations in 2026"], ["900M", "ChatGPT weekly users, February 2026"], ["1B+", "monthly users of Google AI Mode"], ["1%", "of visits with an AI summary clicked a link inside it"]],
                "note": "Sources: BrightLocal, TechCrunch, Alphabet, Pew Research Center",
                "alt": "Stats on AI search use for local business recommendations relevant to Houston and The Woodlands businesses",
                "caption": f"From {SRC['bl']}, {SRC['tc']}, {SRC['alpha']} and {SRC['pew']}.",
            },
            "fanout": {
                "type": "steps",
                "title": "How an AI answer gets built",
                "sub": "Simplified, based on Google’s description of query fan-out",
                "steps": [["The prompt", "“Best roofer in The Woodlands who works with insurance.”"], ["Fan-out searches", "The tool runs several related searches: roofers, reviews, insurance, the area."], ["Retrieval", "It pulls pages, Business Profiles, review sites and news it can read."], ["Selection", "It keeps sources that state facts clearly and agree with each other."], ["The answer", "Two or three names, often with the sources linked underneath."]],
                "alt": "Five steps showing how ChatGPT and Google AI Mode build answers about Houston and The Woodlands businesses",
                "caption": "You can influence steps three and four. That’s where AEO work goes.",
            },
            "bots": {
                "type": "checklist",
                "title": "Crawler access check for AI search",
                "sub": "Open yoursite.com/robots.txt and your security plugin settings",
                "items": ["OAI-SearchBot allowed (ChatGPT search)", "GPTBot: your choice (model training only)", "Googlebot allowed on all service pages", "Bingbot allowed (feeds Copilot)", "PerplexityBot allowed", "No firewall rule blocking AI user agents", "Key pages indexed in Search Console", "Site verified in Bing Webmaster Tools"],
                "alt": "Checklist of AI crawler settings for a Houston or The Woodlands business website to appear in ChatGPT and AI search",
                "caption": f"Crawler roles from {SRC['oai']}.",
            },
            "copy": {
                "type": "compare",
                "title": "Copy AI can’t use vs. copy it can quote",
                "left": {"title": "Vague", "items": ["“Your trusted local experts”", "“Serving the Greater Houston area”", "“Quality service at fair prices”", "Services listed only in an image", "Hours only on the contact page footer"]},
                "right": {"title": "Quotable", "items": ["“Licensed electricians, in Spring since 2009”", "“Serving The Woodlands, Spring, Conroe and Tomball”", "“Service calls from $89, credited to the repair”", "Each service named in text with its own page", "Hours, including weekends, stated in plain words"]},
                "alt": "Comparison of vague and specific website copy for AI search visibility for businesses in Houston and The Woodlands",
                "caption": "If a stranger couldn’t repeat it accurately after one read, an AI tool can’t either.",
            },
            "audit": {
                "type": "columns",
                "title": "Example prompt audit: share of prompts naming you",
                "sub": "20 customer-style prompts run monthly in each tool",
                "labels": ["ChatGPT", "AI Mode", "Gemini", "Copilot", "Perplexity"],
                "values": [15, 35, 30, 10, 20],
                "highlight": [1],
                "y_label": "% of prompts",
                "note": "Illustrative example",
                "alt": "Column chart of an example AI prompt audit for a business in The Woodlands and Houston across ChatGPT, Google AI Mode, Gemini, Copilot and Perplexity",
                "caption": "A pattern like this one, strong on Google tools and weak on Copilot, usually points to Bing indexing and missing mentions.",
            },
            "near": {
                "type": "map",
                "title": "How AI tools read “near The Woodlands”",
                "sub": "Answers often pull businesses from across the north Houston region",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Shenandoah", "Magnolia"],
                "alt": "Map of towns AI search tools may include when answering near The Woodlands questions in Greater Houston",
                "caption": "Name the towns and neighborhoods you serve on your pages so the tool can match you to them.",
            },
            "plan": {
                "type": "steps",
                "title": "A 90-day AEO plan",
                "sub": "For a single-location Houston-area business",
                "steps": [["Days 1-10", "Crawler check, Search Console and Bing Webmaster Tools, first prompt audit."], ["Days 10-30", "Rewrite homepage, service and area pages with plain facts and real detail."], ["Days 30-45", "Complete every Business Profile field; start a steady review request routine."], ["Days 45-75", "Add answers to 15 to 30 real customer questions; pitch one local story."], ["Days 75-90", "Join or update chamber and association listings; rerun the prompt audit."]],
                "alt": "Five-step 90-day plan for AEO and AI search visibility for a business in Houston or The Woodlands",
                "caption": "Most of this also lifts your regular Google rankings, so nothing is wasted if AI tools change.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: Google Ads guide
    {
        "slug": "small-business-guide-google-ads-2026",
        "date": "2025-07-31",
        "modified": "2026-11-27",
        "title": "Google Ads for Small Businesses in Houston and The Woodlands: The 2026 Guide",
        "seo_title": "Google Ads for Small Businesses: 2026 Houston Guide",
        "desc": "A step-by-step 2026 Google Ads guide for Houston and The Woodlands small businesses: budgets, tracking, campaign types, keywords, negatives and targeting.",
        "category": "Paid search",
        "icons": ["Google Ads", "Google Analytics", "Tag Manager"],
        "art": "b6",
        "hero": "growth",
        "hero_alt": "Illustration of a growth chart for a Google Ads guide for small businesses in Houston and The Woodlands",
        "related": ["google-ads-cost-per-click-houston-benchmarks", "google-ads-not-converting-clicks-no-calls", "performance-max-vs-search-campaigns-local"],
        "sections": [
            (None, f"""<p>When we open a small business Google Ads account for the first time, the money is usually leaking in the same four places: no conversion tracking, ads showing to people outside the service area, broad keywords with no negatives, and every click landing on the homepage. Fix those four and most accounts improve before anyone touches the ad copy.</p>
<p><b>Short answer:</b> Google Ads is worth it for most Houston small businesses that sell a service people search for. Start with a Search campaign on high-intent keywords, track calls and forms before spending, target only the area you serve, add negative keywords on day one, and plan on at least $1,500 to $3,000 a month for a fair test.</p>
<p>This guide walks through the setup in order, with the actual settings, updated for what changed in 2026: AI Max, the end of call-only ads and a quiet budget pacing change.</p>"""),

            ("How much should a small business spend on Google Ads in Houston?", f"""<p>Start from leads, not from a round number. The median cost per lead across U.S. search campaigns was $66.69 in {SRC['ws']}, which covered 13,474 campaigns from April 2025 to March 2026, with a median cost per click of $5.42 and a conversion rate of 8.18%. Service categories run higher: Home and Home Improvement at $8.33 a click and $90.92 a lead, Dentists at $8.00 and $72.97, and Attorneys at $9.87 and $131.63.</p>
<!--fig:cpl-->
<p>Simple math: if you want 25 leads a month and your category costs about $90 a lead, budget roughly $2,250 a month. Houston is a big, competitive market, so we wouldn’t assume you’ll beat the national median in month one. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} go category by category.</p>
<p>Two budget mechanics trip up new advertisers. Google can spend up to twice your average daily budget on a busy day, but over a month it won’t spend more than 30.4 times the daily budget, per {SRC['budget']}. And after {SRC['pacing']}, campaigns that switch off whole days of the week now pace toward that full 30.4x monthly figure, even on the days they run. If you only advertise weekdays and set $100 a day, expect to spend around $3,040 a month, not $2,200. Lower the daily number to match the monthly total you want.</p>
<!--fig:budget-->
<p>A budget that’s too small is its own problem. At $10 a day in a $9-a-click category, you get one click a day and learn nothing for months. Narrow the keywords and the area until the budget buys at least 10 to 15 clicks a day.</p>"""),

            ("Step 1: Set up the account so you own it", f"""<p>New Google Ads accounts are steered toward a simplified “Smart campaign” setup. It’s easy and it gives you very little control over where your money goes. When Google offers to create a campaign during sign-up, look for the option to switch to Expert mode, and use it.</p>
<p>Make sure the account is under your business’s Google login, with your card on file, and add any agency or freelancer as a user. Never let someone else create the account for you on their login. We wrote a whole post on {L('/blog/who-owns-google-ads-account-switch-agencies/', 'who owns your Google Ads account')} because untangling this later is miserable.</p>
<p>Complete advertiser verification when Google asks for it. Link Google Analytics 4 and your Google Business Profile under Tools, then Data manager. The Business Profile link is what lets location assets show your address and reviews in ads.</p>"""),

            ("Step 2: Track calls and forms before you spend a dollar", f"""<p>Without tracking, Google’s bidding has no idea which clicks became customers, and neither do you. Set these up before launch:</p>
<ul>
<li><b>Form submissions</b> counted on the thank-you page or a confirmed form event, not on button clicks.</li>
<li>Calls from ads, using Google’s call assets with a minimum call length (we usually use 60 seconds for service businesses).</li>
<li>Calls from the website, via a call tracking number that swaps in for ad visitors.</li>
<li>Enhanced conversions for leads, which matches hashed form data back to the click and fills gaps from cookie loss.</li>
</ul>
<p>Mark only real leads as primary conversions. Page views and “clicked directions” as primary goals teach the system to chase cheap, useless actions. The {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} has the click-by-click setup, and {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking')} explains numbers.</p>"""),

            ("Step 3: Which campaign type should a small business use?", f"""<p>For most local service businesses, start with Search. It shows text ads to people typing what you sell, and you can see and control the searches. Performance Max spreads one budget across Search, Maps, YouTube, Display and Gmail, and it works best for businesses with plenty of conversion data or a product feed.</p>
<!--fig:types-->
<p>Three 2026 changes to know:</p>
<p><b>AI Max for Search.</b> Starting September 1, 2026, Google began auto-upgrading Search campaigns that used automatically created assets or the campaign-level broad match setting into AI Max, with search term matching (and for ACA campaigns, text customization) on by default, per {SRC['aimax']}. AI Max can also change which landing page a click goes to through final URL expansion, per {SRC['aimaxhelp']}. On a small account, check whether yours was upgraded, review the search terms it adds weekly, and set URL exclusions for pages you never want ads sending people to, such as careers or blog posts.</p>
<p>Call-only ads are going away. Google removed the option to create new call-only ads in February 2026, and existing ones stop serving in February 2027, per {SRC['callads']}. Move to responsive search ads with call assets now, on your own timeline.</p>
<p><b>Performance Max got more controllable.</b> It now accepts up to {SRC['pmaxneg']} per campaign. If you run PMax, add your negative list and brand exclusions on day one. Our {L('/blog/performance-max-vs-search-campaigns-local/', 'Performance Max vs. Search comparison')} goes deeper.</p>
<p>And if you’re a home service business, look at Local Services Ads alongside Search. They’re pay-per-lead and sit above regular ads on many searches; see {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</p>"""),

            ("Step 4: Keywords, match types and the negatives that save your budget", f"""<p>Group keywords by the service and the page they belong to. One ad group per service keeps ads and landing pages matched. Here’s an illustrative structure for a plumbing company based in The Woodlands.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Match type</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Emergency plumbing</td><td>emergency plumber near me, 24 hour plumber The Woodlands</td><td>Phrase and exact</td><td>Emergency service page with click-to-call</td></tr>
<tr><td>Water heaters</td><td>water heater replacement Spring TX, tankless water heater install</td><td>Phrase and exact</td><td>Water heater page with price ranges</td></tr>
<tr><td>Slab leaks</td><td>slab leak repair, slab leak detection Conroe</td><td>Phrase and exact</td><td>Slab leak page explaining the process</td></tr>
<tr><td>Brand</td><td>[your business name], [your name] plumbing reviews</td><td>Exact</td><td>Homepage</td></tr>
</tbody></table></div>
<p>We start most small accounts on phrase and exact match. Broad match can work with smart bidding and a lot of conversion data, but on a $2,000-a-month account it tends to wander into searches you never meant to buy. Once tracking is solid and you’ve got a month or two of data, testing broad in one ad group is reasonable.</p>
<p>Negative keywords are where small budgets get saved. Load a starter list before launch, then read the search terms report (Insights and reports, then Search terms) every week for the first two months and keep adding.</p>
<!--fig:negatives-->"""),

            ("Step 5: Location targeting for Houston and The Woodlands", f"""<p>Houston is huge and the traffic is real. Few customers in Kingwood will hire a company that’s an hour away in Sugar Land when there are 30 closer options. Target where you actually work, and draw it tighter than you think.</p>
<p>The setting that matters most is hidden under Locations, then Location options. Google’s default is “Presence or interest,” which includes people who’ve merely shown interest in your area, per {SRC['loc']}. Switch it to <b>Presence: people in or regularly in your included locations</b>. Otherwise someone in Ohio researching a move to The Woodlands can trigger your “emergency plumber” ad.</p>
<!--fig:area-->
<p>Use ZIP codes or towns rather than one big radius when your area has edges. A radius around Market Street reaches into neighborhoods across Lake Woodlands you might not serve. If you’re in Cypress, think about whether you really work east of I-45. And exclude areas you won’t drive to, even if they’re inside the radius. You can add location bid adjustments later once you see which towns produce jobs.</p>"""),

            ("Step 6: Write ads and landing pages that match the search", f"""<p>Responsive search ads take up to 15 headlines and 4 descriptions, and Google mixes them. Write headlines that each stand on their own. An illustrative set for the water heater ad group:</p>
<ul>
<li>Water Heater Replacement Spring</li>
<li>Same-Day Installs, Most Models</li>
<li>Upfront Prices Before We Start</li>
<li>Licensed Texas Master Plumber</li>
<li>4.9 Stars From 600+ Neighbors (only if true)</li>
<li>Tankless and Tank Water Heaters</li>
</ul>
<p>Add sitelinks, callouts and a call asset scheduled for hours when someone answers. Pin only if you have a legal or brand reason to.</p>
<p>Then send the click to the matching page. Someone who searched “slab leak repair Conroe” should land on a page about slab leaks that mentions Conroe, shows a phone number at the top and explains what happens next. The homepage is almost never the right answer. {L('/blog/landing-pages-101/', 'Landing pages 101')} covers the layout, and if clicks come in but calls don’t, the {L('/blog/google-ads-not-converting-clicks-no-calls/', 'not-converting checklist')} is the place to start.</p>"""),

            ("Step 7: Bidding, and when to let Google’s automation drive", f"""<p>Automated bidding is only as smart as the conversions you feed it. Our rule of thumb for small accounts:</p>
<ol>
<li><b>Weeks 1 to 4:</b> Maximize conversions if tracking is solid from day one. If it isn’t, Maximize clicks with a maximum CPC cap so a few expensive clicks don’t eat the budget.</li>
<li><b>After about 30 conversions in 30 days:</b> test a target CPA set near your actual cost per lead. Setting it far lower than reality just throttles volume.</li>
<li><b>Ongoing:</b> change bid targets by 10% to 20% at a time and wait a week or two between changes. The system needs time to recalibrate.</li>
</ol>
<p>Those thresholds are our experience, not a Google rule. Two settings to check under the campaign’s Networks: uncheck Display Network on Search campaigns (it’s a different product with different intent), and watch Search partners in the segment report before deciding to keep it.</p>"""),

            ("How long does it take for Google Ads to work?", f"""<p>Calls can start the first week. Knowing whether the account is profitable takes longer: two to three months for most small businesses, because you need enough leads to judge quality, and enough closed jobs to know what a lead is worth.</p>
<!--fig:funnel-->
<p>Judge the account on cost per customer, not cost per click. A $12 click that books a $4,000 repair beats a $3 click that never calls. That means someone has to tell the ad account, or at least a spreadsheet, which leads turned into jobs. Our post on {L('/blog/understanding-cost-per-lead/', 'understanding cost per lead')} shows the math.</p>
<p>A weekly 30-minute routine covers most of what a small account needs. Read the search terms from the last seven days and add negatives. Listen to two or three recorded calls from ads, because the recordings tell you more about lead quality than any dashboard. Check that spend is pacing where you expect for the month. Look at which ad groups produced leads and which only produced clicks. Then leave everything else alone. Ignore impression share swings and the auto-generated recommendations tab for now; accepting every recommendation is a reliable way to raise spend without raising leads.</p>"""),

            ("Your first 90 days, and the mistakes we see most", f"""<p>Here’s the order we’d run a new small business account in.</p>
<!--fig:plan-->
<p>The mistakes we see most in Houston small business accounts, roughly in order of how much money they waste:</p>
<ul>
<li>Location set to “Presence or interest,” so a share of clicks come from outside the service area.</li>
<li>Primary conversions that aren’t leads, such as page views or direction clicks.</li>
<li>No negatives, so the budget pays for job seekers, DIYers and people looking for free stuff.</li>
<li>Ads running 24/7 with a call asset, when nobody answers after 6 p.m.</li>
<li>Seasonal blindness. AC and plumbing demand jumps with the first heat wave and the first hard freeze; roofers see spikes after hail. Raise budgets before the rush. Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing guide')} has the calendar.</li>
<li>Changing everything at once every week, so nothing ever has time to learn.</li>
</ul>
<p>Running Google Ads yourself is completely doable if you’ll spend a couple of hours a week in the account. If you’d rather hand it off, our {L('/services/search-marketing/', 'search marketing team')} runs accounts like these every day, and {L('/blog/google-ads-management-houston-cost/', 'our management cost guide')} explains what agencies charge. Either way, <a href="/contact/">get in touch</a> and tell us about your business and goals; a senior strategist will put together a plan for you.</p>"""),
        ],
        "faq": [
            ("What is the minimum budget for Google Ads for a small business?",
             "Google has no minimum spend, but a useful test usually needs enough budget for 10 to 15 clicks a day. With service-category clicks often costing $5 to $10, that means roughly $1,500 to $3,000 a month for most Houston service businesses. If that's too much, narrow the keywords and the service area rather than spreading a small budget thin across everything."),
            ("Is Google Ads worth it for a small local business in The Woodlands?",
             "Usually yes for businesses that sell something people actively search for, like home services, legal, medical, auto repair or local retail. It works when calls and forms are tracked, ads target only the area you serve, negatives block junk searches and clicks land on matching pages. It is a harder fit for businesses customers rarely search for, where social ads or referrals tend to work better."),
            ("Should I use Performance Max or Search campaigns for a service business?",
             "Start with Search for most service businesses, because you can see and control which searches trigger your ads. Performance Max spreads budget across Search, Maps, YouTube, Display and Gmail and tends to perform better with lots of conversion data. If you test it, add negative keywords and brand exclusions, use real lead conversions only, and compare its cost per customer against Search."),
            ("Why am I getting Google Ads clicks from outside Houston?",
             "Most often because the location option is set to Presence or interest, the default, which includes people who have only shown interest in your area. Change it to Presence, meaning people in or regularly in your locations, under Locations and Location options in campaign settings. Also check that your radius or ZIP list doesn't reach areas you don't serve, and review the location report monthly."),
            ("Can I run Google Ads myself or should I hire someone in Houston?",
             "You can run it yourself if you'll learn the settings and spend a couple of hours a week reading search terms, adjusting negatives and checking lead quality. Hire help when the budget is large enough that wasted spend costs more than management, when you can't keep up with weekly reviews, or when results have stalled. Either way, keep the account under your own login."),
        ],
        "figures": {
            "cpl": {
                "type": "bars",
                "title": "Median cost per lead from Google search ads",
                "sub": "U.S. campaigns, April 2025 to March 2026",
                "items": [["All industries", 66.69, "$66.69"], ["Dentists and dental services", 72.97, "$72.97"], ["Home and home improvement", 90.92, "$90.92"], ["Attorneys and legal services", 131.63, "$131.63"]],
                "highlight": [2],
                "note": "Source: WordStream 2026 Google Ads benchmarks (medians)",
                "alt": "Bar chart of Google Ads cost per lead by industry for planning a small business budget in Houston and The Woodlands",
                "caption": f"From {SRC['ws']}. Houston costs can run higher in crowded categories.",
            },
            "budget": {
                "type": "stats",
                "title": "Google Ads budget rules worth knowing",
                "stats": [["2x", "a campaign can spend up to twice its daily budget on one day"], ["30.4x", "the daily budget is the monthly spending cap"], ["$5.42", "median cost per click, U.S. search ads"], ["8.18%", "median click-to-lead conversion rate"]],
                "note": "Sources: Google Ads Help, WordStream",
                "alt": "Stats on Google Ads budget pacing and benchmarks for small businesses in Houston and The Woodlands",
                "caption": f"Budget rules from {SRC['budget']}; benchmarks from {SRC['ws']}.",
            },
            "types": {
                "type": "compare",
                "title": "Performance Max vs. Search for a local service business",
                "left": {"title": "Performance Max first", "items": ["Budget split across six channels", "Less visibility into exact searches", "Needs lots of conversion data", "Can chase cheap form fills and spam", "Best with a product feed or many leads"]},
                "right": {"title": "Search first (our default)", "items": ["Ads only on searches you choose", "Full search terms report and negatives", "Works on a $1,500-a-month budget", "Ad and landing page matched per service", "Add PMax later as a measured test"]},
                "alt": "Comparison of Performance Max and Search campaigns for small service businesses in Houston and The Woodlands",
                "caption": "PMax isn’t bad. It’s just a poor first campaign for most small local accounts.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Starter negative keywords for local services",
                "sub": "Add before launch, then grow from the search terms report",
                "items": ["Jobs: jobs, hiring, salary, careers, apprentice", "DIY: how to, diy, yourself, youtube, video", "Free: free, cheap only if you don’t sell on price", "Education: course, school, training, certification", "Parts and supplies: parts, home depot, lowes", "Research: what is, definition, meaning, reddit", "Wrong area: towns you won’t drive to", "Wrong service: work you don’t offer"],
                "alt": "Checklist of starter negative keywords for Google Ads for small service businesses in Houston and The Woodlands",
                "caption": "Then read search terms weekly for the first two months. Every account has its own surprises.",
            },
            "area": {
                "type": "map",
                "title": "A realistic ad area for a business in The Woodlands",
                "sub": "Target where you actually take jobs, then expand on data",
                "highlight": ["The Woodlands", "Spring", "Shenandoah", "Conroe", "Tomball", "Magnolia"],
                "alt": "Map of a Google Ads location targeting area for a small business in The Woodlands and north Houston",
                "caption": "Targeting all of Houston from The Woodlands usually buys clicks from people who would never hire you.",
            },
            "funnel": {
                "type": "funnel",
                "title": "What $2,000 a month can look like",
                "stages": [["$2,000 budget", "month"], ["Clicks at ~$8", "250"], ["Leads at 8% conversion", "20"], ["Booked appointments", "10"], ["Paying customers", "6"]],
                "note": "Illustrative example. Your click cost, conversion rate and close rate will differ.",
                "alt": "Funnel of an example Google Ads budget turning into leads and customers for a small business in Houston",
                "caption": "Divide the budget by paying customers. If that number beats your profit per job, scale it.",
            },
            "plan": {
                "type": "steps",
                "title": "Your first 90 days on Google Ads",
                "sub": "For a single-location Houston small business",
                "steps": [["Before launch", "Own the account, set up call and form tracking, write negatives."], ["Weeks 1-2", "Search campaign, phrase and exact match, Presence targeting, matching pages."], ["Weeks 3-6", "Read search terms weekly, add negatives, pause keywords with no leads."], ["Weeks 7-10", "Shift budget to winning ad groups; test new headlines and a landing page change."], ["Weeks 11-13", "Compare cost per customer to job value; decide to scale, fix or stop."]],
                "alt": "Five-step 90-day Google Ads plan for small businesses in Houston and The Woodlands",
                "caption": "Resist rebuilding the account in week three. Most of the gains come from steady weekly pruning.",
            },
        },
    },
]
