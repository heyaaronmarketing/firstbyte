"""Batch 8 (agency intent): WordPress vs Wix vs Squarespace vs Webflow (and Shopify) for a small business site, and
SMS / text message marketing for Texas small businesses (rules, setup, what to send).

Research, website post: PetaPixel on Squarespace's July 2026 price increase and Style Factory's Sept 2026 Squarespace
pricing/fees table; Style Factory (Aug 2026) and UsagePricing (retracted Aug 2026 Wix change) for Wix US plan prices;
BRIX Templates on Webflow's May 2026 site plan overhaul (Basic/Premium) and Memberstack on workspace plans; Website
Builder Expert (May 2026) on Shopify plans; eSEOspace on WordPress.com plans (plugins on all paid plans since April
2026); Wix Help Center (site can't be hosted elsewhere; URL prefixes in SEO Settings); Webflow Help Center (code export
on Workspace plans, CMS/forms/ecommerce excluded); WPBeginner on what Squarespace's export includes; Shopify staff
answers on fixed /pages/ /products/ /collections/ URL segments; Search Engine Journal on HTTP Archive Core Web Vitals
pass rates by CMS (July 2025 data); W3Techs CMS usage (Oct 31, 2026); Patchstack State of WordPress Security in 2026.

Research, SMS post: govregs.com text of 47 CFR 64.1200 (8 a.m. to 9 p.m. rule, prior express written consent);
Holland & Knight on Bradford v. Sovereign Pest Control of TX (5th Cir., Feb 25, 2026); Faegre Drinker on the 11th
Circuit's Insurance Marketing Coalition v. FCC and the FCC's July 2025 order; Kelley Drye on the revocation rules in
effect April 11, 2025; Burr & Forman on the revoke-all delay to Jan 31, 2027; Texas Secretary of State telephone
solicitation FAQ ($200 fee, $10,000 security, consent-based texting not required to register); K&L Gates one year
after SB 140 (Sept 2026); National Law Review on SB 140 after the November 2025 settlement (302.058 exemption, Texas
No-Call list, Chapter 301 hours); Twilio A2P 10DLC fee schedule and toll-free verification article; Prompt.io on the
Feb 1, 2025 10DLC blocking date; Postscript pricing page; Firstpier on Klaviyo SMS credits; TextBolt on SimpleTexting
plans (Jan 2026); Capterra on Podium's quote-based pricing.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # website post
    "sqs_up": A("https://petapixel.com/2026/07/17/squarespace-is-increasing-prices-by-up-to-26/", "PetaPixel"),
    "sqs_fees": A("https://www.stylefactoryproductions.com/squarespace-pricing", "Style Factory’s Squarespace fee breakdown"),
    "wix": A("https://www.stylefactoryproductions.com/blog/wix-pricing", "Style Factory’s Wix pricing guide"),
    "webflow": A("https://brixtemplates.com/blog/webflow-may-2026-pricing-changes-explained", "BRIX Templates’ breakdown of the May 2026 change"),
    "wfws": A("https://www.memberstack.com/blog/new-webflow-pricing-in-2026-what-every-plan-costs-and-how-to-choose", "Memberstack"),
    "shopify": A("https://www.websitebuilderexpert.com/ecommerce-website-builders/shopify-pricing/", "Website Builder Expert"),
    "wpcom": A("https://eseospace.com/blog/wordpress-com-plans/", "eSEOspace’s plan rundown"),
    "wixexport": A("https://support.wix.com/en/article/exporting-your-wix-site-elsewhere", "Wix’s own help center"),
    "wixurl": A("https://support.wix.com/en/article/customizing-your-pages-url-structure-in-seo-settings", "Wix’s SEO Settings"),
    "wfexport": A("https://help.webflow.com/hc/en-us/articles/33961386739347", "Webflow’s code export documentation"),
    "sqsexport": A("https://www.wpbeginner.com/wp-tutorials/how-to-properly-move-from-squarespace-to-wordpress/", "WPBeginner’s migration guide"),
    "shopurl": A("https://community.shopify.com/t/how-can-i-remove-pages-from-my-stores-url/1578", "Shopify’s own staff"),
    "cwv": A("https://www.searchenginejournal.com/wordpress-versus-everyone-the-top-cms-for-core-web-vitals/555746/", "Search Engine Journal’s look at HTTP Archive data"),
    "w3": A("https://w3techs.com/technologies/overview/content_management", "W3Techs"),
    "patch": A("https://www.patchstack.com/whitepaper/state-of-wordpress-security-in-2026/", "Patchstack’s 2026 security report"),
    # sms post
    "cfr": A("https://www.govregs.com/regulations/47/64.1200", "47 CFR 64.1200"),
    "bradford": A("https://www.hklaw.com/en/insights/publications/2026/03/tcpa-reset-fifth-circuit-rejects-prior-express-written-consent-rule", "Holland &amp; Knight’s summary"),
    "imc": A("https://www.faegredrinker.com/zh/insights/publications/2025/7/fcc-ends-quest-to-amend-its-definition-of-prior-consent-in-the-wake-of-eleventh-circuit-ruling", "Faegre Drinker"),
    "revoke": A("https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/fcc-issues-one-year-limited-waiver-of-new-tcpa-consent-revocation-rule", "Kelley Drye’s write-up"),
    "revokeall": A("https://www.burr.com/telephone-consumer-protection-act/the-fcc-delays-effective-date-of-tcpa-revoke-all-rule-until-january-31-2027", "pushed to January 31, 2027"),
    "sos": A("https://www.sos.texas.gov/statdoc/faqs3400.shtml", "Texas Secretary of State’s FAQ"),
    "klg": A("https://www.klgates.com/thought-leadership/Litigation-Minute-Text-Message-Marketing-in-Texas-One-Year-After-SB-140-9-14-2026", "K&amp;L Gates"),
    "nlr": A("https://natlawreview.com/article/texas-sb-140-after-november-settlement-consent-cold-texting-out", "National Law Review"),
    "tw10": A("https://support.twilio.com/hc/en-us/articles/1260803965530", "Twilio’s fee schedule"),
    "twtf": A("https://support.twilio.com/hc/en-us/articles/5377174717595", "Twilio"),
    "block": A("https://prompt.io/blog/2025-10dlc", "since February 1, 2025"),
    "postscript": A("https://postscript.io/pricing", "Postscript’s pricing page"),
    "klaviyo": A("https://www.firstpier.com/resources/klaviyo-text-messaging", "Firstpier’s Klaviyo breakdown"),
    "simple": A("https://textbolt.com/blog/simpletexting-pricing/", "TextBolt’s January 2026 rundown"),
    "podium": A("https://www.capterra.com/p/164285/Podium/pricing/", "Capterra"),
}

SMS = "/blog/sms-marketing-small-business-texas-rules/"
WEB = "/blog/wordpress-vs-wix-vs-squarespace-vs-webflow-small-business/"

POSTS = [
    # ------------------------------------------------------------------ post 1: website platforms
    {
        "slug": "wordpress-vs-wix-vs-squarespace-vs-webflow-small-business",
        "title": "WordPress vs Wix vs Squarespace vs Webflow: Which Fits a Small Business?",
        "seo_title": "WordPress vs Wix vs Squarespace vs Webflow (2026)",
        "desc": "WordPress vs Wix vs Squarespace vs Webflow for a small business site: real 2026 pricing, SEO limits, lock-in, upkeep, plus a pick-by-business-type table.",
        "category": "Websites",
        "icons": ["Google", "Search Console", "Google Analytics"],
        "art": "b3",
        "hero": "layout",
        "hero_alt": "Illustration of website layout blocks comparing WordPress, Wix, Squarespace and Webflow for a small business in The Woodlands",
        "related": ["how-much-does-a-website-cost-the-woodlands", "how-fast-should-your-website-load", "signs-your-website-needs-a-redesign"],
        "sections": [
            (None, f"""<p>Three tabs open on the laptop. Wix, Squarespace, and a WordPress tutorial that mentioned “child themes” in the second paragraph and lost you there. Your nephew swears by Webflow. Your accountant’s site is on GoDaddy and looks fine.</p>
<p>So which one? For most small service businesses around Houston, Squarespace or Wix gets you a good-looking site you can edit yourself for roughly $30 to $40 a month. WordPress is the better call when SEO content, integrations and full ownership matter more than convenience, and someone is on the hook for updates. Webflow suits design-led brands with a designer on call. Shopify wins when selling products online is the business.</p>
<p>There’s no single winner, and anyone who says otherwise probably sells one. We build and fix sites on several of these for businesses in The Woodlands, Spring and Conroe, and each has a spot where it’s right and a spot where it quietly costs you money.</p>
<p>Below: 2026 prices, SEO limits, who really owns the site, upkeep, and a pick-by-business-type table.</p>"""),

            ("What each platform actually is, in plain English", f"""<p>The big split is between <b>hosted builders</b> and <b>self-hosted software</b>.</p>
<p>Wix, Squarespace, Webflow and Shopify are hosted builders. You pay a monthly or yearly fee, and the company handles servers, security patches, backups and the SSL certificate. You rent the house, furnished, and the landlord fixes the plumbing. You also live by the landlord’s rules.</p>
<p>WordPress comes in two flavors, which confuses everyone. WordPress.org is free, open-source software you install on hosting you pay for separately. That’s what people usually mean by “a WordPress site.” WordPress.com is a hosted service run by Automattic that behaves more like the builders. Per {SRC['wpcom']}, since April 2026 every paid WordPress.com plan, starting with the $4-a-month Personal plan, can install plugins, which narrows the old gap between the two.</p>
<p>Scale-wise, {SRC['w3']} counted WordPress on 39.5% of all websites as of October 31, 2026, followed by Shopify at 5.3%, Wix at 4.2%, Squarespace at 2.4% and Webflow at 0.8%. Popularity means more developers and plugins, and more people trying to hack WordPress sites.</p>
<p>One more option worth naming: if your marketing company built your site on its own proprietary platform, you’re in a fifth category with the most lock-in of all. Ask before you sign.</p>"""),

            ("WordPress vs Wix vs Squarespace pricing: what you’ll actually pay", f"""<p>Sticker prices first. These are list prices for US plans billed annually, as published in fall 2026. Squarespace raised most plans in July 2026 (Core went from $23 to $29 a month on annual billing, per {SRC['sqs_up']}), and Webflow replaced its CMS and Business plans with a single Premium plan in May 2026, per {SRC['webflow']}.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform</th><th>Plan a typical service business needs</th><th>Price (annual billing)</th><th>Watch out for</th></tr></thead>
<tbody>
<tr><td>Squarespace</td><td>Core</td><td>$29/mo ($39 billed monthly)</td><td>Basic charges a 2% fee on product sales; scheduling is a paid add-on</td></tr>
<tr><td>Wix</td><td>Core or Business</td><td>$29 or $39/mo</td><td>Light ($17) has only 2GB storage; paid apps add up</td></tr>
<tr><td>Webflow</td><td>Premium site plan (Basic if no blog)</td><td>$25/mo ($39 monthly); Basic $15</td><td>Bandwidth caps; a Workspace plan for the designer is separate</td></tr>
<tr><td>Shopify</td><td>Basic</td><td>$29/mo ($39 monthly)</td><td>2% fee if you use an outside payment processor; app subscriptions</td></tr>
<tr><td>WordPress (self-hosted)</td><td>Software is free; hosting is not</td><td>Hosting often $10 to $50/mo</td><td>Premium plugins, theme licenses and someone to run updates</td></tr>
</tbody></table></div>
<p>Sources: {SRC['sqs_fees']}, {SRC['wix']}, BRIX for Webflow, {SRC['shopify']} for Shopify. Hosting ranges for WordPress are our typical observation, not a published price.</p>
<p>Now the part that matters: total cost of ownership. The plan fee is rarely the biggest line. A Wix site with four paid apps can quietly double its bill. A WordPress site on $12 hosting looks cheap until a plugin conflict takes the contact form down for a week in July, right when every AC in Spring is dying.</p>
<!--fig:tco-->
<p>That chart assumes a 10-page service site with a blog. Look at the last bar. A WordPress care plan (updates, backups, uptime monitoring, small fixes) is where the money goes, and we think it’s money well spent if WordPress is the right fit. If you don’t want to pay for it or do it yourself, that alone is a strong vote for a hosted builder.</p>
<p>The design and build is a separate, one-time cost, and it swamps all of this. Our <a href="/blog/how-much-does-a-website-cost-the-woodlands/">breakdown of what a website costs in The Woodlands</a> covers those ranges.</p>"""),

            ("Wix vs WordPress for SEO (and where Squarespace, Webflow and Shopify land)", f"""<p>Here’s an unpopular opinion from people who do SEO for a living: the platform is almost never the reason a local business doesn’t rank. Thin service pages, no reviews, a weak Google Business Profile and zero local links lose far more rankings than any builder does.</p>
<h3>URL control</h3>
<p>WordPress and Webflow let you set almost any URL structure you want, including clean service-area pages like /ac-repair-spring-tx/. Wix used to force prefixes like /post/ on blog articles; it now lets you change those prefixes in {SRC['wixurl']}, though the structure must keep at least one variable. Squarespace gives you control of page slugs, with collection items (blog posts, products) living under their collection’s URL.</p>
<p>Shopify is the strict one. Pages live under /pages/, products under /products/, collections under /collections/, and {SRC['shopurl']} have confirmed for years that those segments can’t be removed. For a store, that’s fine. For a plumber who wants a clean page per suburb, it’s an irritation.</p>
<h3>Redirects</h3>
<p>All five can do 301 redirects, which you need the moment you rename a page or move platforms. WordPress needs a plugin (or server rules). Wix has a URL Redirect Manager. Squarespace uses a URL Mappings panel where you type rules by hand. Webflow and Shopify have redirect screens in settings.</p>
<h3>Schema and technical extras</h3>
<p>WordPress with an SEO plugin like Yoast or Rank Math gives you the most control over structured data (LocalBusiness, FAQ, Service). Webflow lets you add custom code per page and wire CMS fields into JSON-LD, which is powerful but needs someone who knows what they’re doing. Wix adds some markup automatically and lets you paste custom structured data per page. Squarespace generates basic markup and accepts code injection on higher plans, but it’s the least flexible of the group.</p>
<p>Our honest ranking for local SEO flexibility: WordPress, then Webflow, then Wix, then Squarespace, with Shopify strong for products and awkward for service pages. The gap between first and fourth is smaller than forums make it sound. A well-written Squarespace site beats a neglected WordPress site every time.</p>"""),

            ("Which website builder is fastest?", f"""<p>Speed is one place where the hosted builders have a real edge, and the reason surprises people.</p>
<!--fig:cwv-->
<p>Those numbers come from HTTP Archive’s Core Web Vitals technology report, via {SRC['cwv']}, using July 2025 data. Read them carefully. WordPress isn’t slow software. WordPress sites are slow because so many sit on bargain shared hosting with a heavy page builder, eight sliders and 40 plugins. A well-built WordPress site on decent hosting passes Core Web Vitals without drama. The builders simply stop you from making the worst choices.</p>
<p>Shopify and Webflow weren’t in that breakdown; in our experience both are quick out of the box until apps and scripts pile up.</p>
<p>What to do with this: if you go WordPress, budget for real hosting and a lean theme. If you go Wix or Squarespace, stop fighting the platform with giant uncompressed hero videos. Either way, check your own site on PageSpeed Insights. Our guide on <a href="/blog/how-fast-should-your-website-load/">how fast your website should load</a> explains which numbers to watch.</p>"""),

            ("Who owns your website if you leave?", f"""<p>This is the question most owners never ask until they’re angry at a vendor.</p>
<p>With Wix, you own your content and your domain, but the site itself can’t leave. {SRC['wixexport']} says a Wix site has to be hosted and operated on Wix’s servers. Moving off Wix means rebuilding the site somewhere else and copying content over.</p>
<p>Squarespace has an export, and it’s partial. According to {SRC['sqsexport']}, basic pages, one blog and its posts, galleries, and text, image and embed blocks come across to WordPress. Product pages, events, audio and video blocks, styles and custom CSS don’t, and images have to be pulled over separately.</p>
<p>Webflow lets you export HTML, CSS and JavaScript, but only on a paid Workspace plan, and {SRC['wfexport']} spells out what’s left behind: CMS content, ecommerce, forms, site search and password protection. A blog-heavy Webflow site exports as a pretty shell. (CMS content can be exported separately as CSV.)</p>
<p>Shopify exports products, customers and orders as CSV files, which is what a store really needs. The theme stays.</p>
<p>Self-hosted WordPress is the only option where you can pack up the whole thing (files and database) and move it to any host. That portability is the single biggest argument for WordPress, and it’s why we lean that way for businesses that plan to be around in ten years and expect to switch vendors at least once.</p>
<!--fig:own-->
<p>Whatever you choose, the domain matters more than the platform. If your web person registered the domain in their own account, you don’t fully own your web presence on any platform. Our post on <a href="/blog/who-owns-google-ads-account-switch-agencies/">who owns your marketing accounts when you switch agencies</a> walks through getting the domain, analytics and ad accounts into your name.</p>"""),

            ("Editing, security and the maintenance nobody budgets for", f"""<p>Think about who edits the site after launch. Usually the owner on a Sunday night, or an office manager with 11 other jobs.</p>
<p>Squarespace is the easiest for that person. The layouts are tidy and it’s hard to break. Wix is more flexible, which cuts both ways: you can drag anything anywhere, and staff sometimes do, which is how mobile layouts end up with overlapping text. Webflow’s visual designer is built for designers; its content editing mode is simple for staff updating text and blog posts, but layout changes belong to whoever built it. WordPress depends entirely on how it was built. A clean block-editor site is pleasant. A site built in a page builder by someone who left in 2021 can be a minefield.</p>
<p>Security is where the trade-off gets real. On the hosted builders, patching is the company’s problem. On WordPress, it’s yours. {SRC['patch']} counted 11,334 new vulnerabilities in the WordPress ecosystem in 2025, 91% of them in plugins and only 6 in WordPress core. Worse, 46% didn’t have a fix from the developer by the time they were made public.</p>
<p>That’s not a reason to avoid WordPress. Millions of sites run it safely. It’s a reason to keep plugins few and reputable, run updates at least weekly, keep off-site backups, and use a host that offers a firewall. If nobody is doing those things today, you have a risk, and you won’t find out about it until the site starts redirecting visitors to a pharmacy in another country.</p>
<p>(We’ve cleaned up that exact mess. It’s never cheaper than the care plan.)</p>"""),

            ("Booking, forms, CRM and the tools you already use", f"""<p>For a lot of Houston-area businesses, the website is really a front door to some other system: ServiceTitan or Housecall Pro for home services, Toast or ChowNow for restaurant ordering, Mindbody or Vagaro for studios and salons, an EHR intake form for a medical practice.</p>
<p>Most of those tools give you an embed code or a booking link, and every platform here can take an embed. The differences show up at the edges:</p>
<ul>
<li><b>Booking built in:</b> Wix has its own bookings tools, and Squarespace sells scheduling as an add-on. Good enough for a solo lash artist or massage therapist. A multi-tech HVAC company will outgrow both and should book through its field-service software.</li>
<li><b>Forms and CRM:</b> WordPress has form plugins that connect to nearly any CRM. Wix and Squarespace forms work, but sending leads into a CRM often means Zapier or a native integration that may only exist for the big CRMs. Webflow forms are solid; remember they don’t survive a code export.</li>
<li><b>Tracking:</b> All five let you add Google Analytics 4 and Google Tag Manager. Call tracking scripts and conversion tracking are easiest on WordPress and Webflow, where you control the code. Wix and Squarespace have specific places to paste code, and a few tracking setups fight with them.</li>
<li><b>Medical and legal intake:</b> don’t assume any builder’s default contact form is right for sensitive information. Use your practice software’s intake tool and embed or link it.</li>
</ul>
<p>Before you pick a platform, list the three systems your site must talk to and check each one’s integration page. Ten minutes of checking beats a rebuild later.</p>"""),

            ("Webflow vs WordPress: when the designer’s favorite makes sense", f"""<p>Webflow comes up a lot because designers love it, and for good reason. It produces clean code, includes fast hosting, has no plugins to update, and gives a skilled designer pixel-level control without a developer. For a brand-conscious business with a designer on retainer (a boutique hotel, a med spa, a real estate team selling the Hughes Landing lifestyle), it can be the best of both worlds.</p>
<p>The catches are practical. Pricing now includes a site plan plus, for whoever builds and maintains the site, a Workspace plan; per {SRC['wfws']}, Workspace Core is $19 a month on yearly billing and is also where code export lives. The Premium site plan includes 50GB of bandwidth, with add-ons after that. The integration library is smaller than WordPress’s. And if your designer moves on, the pool of local Webflow pros is smaller than the pool of WordPress people.</p>
<p>WordPress wins when you need lots of pages and integrations, a big local content plan (service pages for Spring, Tomball, Magnolia, Cypress and Katy, for example), and the freedom to hire anyone. Webflow wins when design quality and low maintenance matter more than plugin variety.</p>
<p>We’d steer a DIY owner away from building in Webflow alone.</p>"""),

            ("Best website builder for small business: pick by business type", f"""<p>Here’s the decision tool. Find the row closest to you, then sanity-check it with the steps below.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Your business</th><th>Our usual pick</th><th>Why</th><th>Strong runner-up</th></tr></thead>
<tbody>
<tr><td>Solo pro: lash, massage, therapist, photographer</td><td>Squarespace</td><td>Easiest to keep looking good; booking add-on works for one calendar</td><td>Wix</td></tr>
<tr><td>Restaurant or café</td><td>Squarespace or Wix</td><td>Menus and hours change weekly; staff need easy edits; ordering lives in Toast or similar</td><td>WordPress</td></tr>
<tr><td>Home services with a service area (HVAC, plumbing, roofing, pest)</td><td>WordPress</td><td>Many location and service pages, schema, CRM forms, call tracking</td><td>Webflow</td></tr>
<tr><td>Design-led brand with a designer on retainer</td><td>Webflow</td><td>Visual control, fast hosting, little upkeep</td><td>WordPress</td></tr>
<tr><td>Selling more than a handful of products online</td><td>Shopify</td><td>Checkout, inventory, shipping and apps built for stores</td><td>WordPress with WooCommerce</td></tr>
<tr><td>Multi-location, franchise or content-heavy B2B</td><td>WordPress</td><td>Portability, permissions, unlimited structure, any developer can pick it up</td><td>Webflow</td></tr>
<tr><td>Starting out, under $1,000 total budget</td><td>Wix or Squarespace</td><td>Template plus a weekend; upgrade later</td><td>WordPress.com</td></tr>
</tbody></table></div>
<!--fig:pick-->
<p>The right answer depends on who will maintain it and how many pages your marketing needs, far more than on features.</p>"""),

            ("When to DIY and when to pay someone", f"""<p>DIY makes sense if you’re early, your budget is tight, you pick Squarespace or Wix, and you’re willing to spend a couple of weekends writing real copy. Use a template close to what you want and change as little of the design as possible. Spend your energy on the words, the photos of your actual team and trucks, and a clear call button.</p>
<p>Paying someone makes sense when the site has to carry real lead flow, when you’re running Google Ads to it, when you need a dozen service-area pages, or when you’re migrating an older site that already ranks. Migrations are where we see the most damage: URLs change, nobody sets up redirects, and six months of rankings disappear. If you’re seeing those symptoms now, our list of <a href="/blog/signs-your-website-needs-a-redesign/">signs your website needs a redesign</a> will help you decide whether to rebuild or repair.</p>
<p>If you want help, our <a href="/services/web-design-seo-pr/">web design and SEO team</a> builds on WordPress, Webflow and Shopify, and fixes sites on Wix and Squarespace. We’ll tell you plainly if your current platform is fine and the problem is elsewhere.</p>
<p>And if the site is fine but the ads sending traffic to it aren’t, start with a free <a href="/contact/">Ad Spend Leak Check</a>: a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours.</p>"""),
        ],
        "faq": [
            ("Is Wix or WordPress better for SEO?",
             "WordPress gives you more control over URLs, structured data, redirects and site speed tuning, so it has a higher ceiling. Wix has closed much of the gap and now lets you change blog and product URL prefixes. For a typical local business, content quality, reviews and your Google Business Profile matter far more than the platform. A well-written Wix site will outrank a neglected WordPress one."),
            ("Is Squarespace good for a small business website?",
             "Yes, for many small businesses. It is the easiest platform to keep looking polished, hosting and security are handled for you, and the Core plan costs $29 a month on annual billing after the July 2026 increase. It is less flexible for SEO and integrations, and its export to other platforms is partial, so it fits best when the site is simple and staff will do the edits."),
            ("Is Webflow worth it for a small business?",
             "Webflow is worth it when you have a designer who knows it and design quality matters to your brand. It is fast, needs no plugin updates, and its Premium site plan costs $25 a month billed yearly. It is a poor fit for owners building alone, because the learning curve is steep, and its code export leaves out CMS content, forms and ecommerce."),
            ("Can I move my Wix site to WordPress later?",
             "You can move your content and domain, but not the site itself. Wix says sites must be hosted on its servers, so moving means rebuilding the design on WordPress, copying pages and posts, and setting up 301 redirects from every old URL to its new address. Plan the redirects before launch, or you risk losing rankings you built on Wix."),
            ("What is the cheapest way to build a small business website?",
             "The cheapest workable route is a Squarespace or Wix template you set up yourself, at roughly $17 to $39 a month plus a domain. WordPress software is free, but hosting, premium plugins and maintenance usually cost more over a few years unless you handle updates yourself. Cheap is fine to start, as long as you own the domain and the content."),
        ],
        "figures": {
            "tco": {
                "type": "bars",
                "title": "Yearly cost to run a 10-page site",
                "sub": "Plan or hosting, add-ons and domain; design not included",
                "items": [["Webflow Premium", 320, "~$320"], ["Squarespace Core", 370, "~$370"], ["Wix Core", 370, "~$370"], ["WordPress, you run updates", 520, "~$520"], ["Shopify Basic + 2 apps", 610, "~$610"], ["WordPress + $100/mo care plan", 1720, "~$1,720"]],
                "highlight": [5],
                "note": "Illustrative example",
                "alt": "Bar chart comparing yearly running costs of WordPress, Wix, Squarespace, Webflow and Shopify for a small business website in The Woodlands",
                "caption": "Plan prices are 2026 annual-billing list prices; add-ons, hosting and care plan are typical examples.",
            },
            "cwv": {
                "type": "stats",
                "title": "Sites passing Core Web Vitals, July 2025",
                "stats": [["85%", "Duda sites with a good Core Web Vitals score"], ["73%", "Wix sites"], ["69%", "Squarespace sites"], ["44%", "WordPress sites"]],
                "note": "Source: HTTP Archive via Search Engine Journal",
                "alt": "Stat tiles showing Core Web Vitals pass rates for Wix, Squarespace and WordPress small business websites",
                "caption": f"Data from HTTP Archive’s technology report, reported by {SRC['cwv']}. Hosting and build quality drive most of the WordPress gap.",
            },
            "own": {
                "type": "checklist",
                "title": "Ownership check before you pick a platform",
                "sub": "Ask these before you sign anything",
                "items": ["Domain registered in your name, your login", "You are the account owner on the platform", "You know what the export includes and leaves out", "Google Analytics and Search Console in your account", "Form leads also go to an inbox you control", "Copy and photos stored somewhere you own", "Written list of paid apps and plugins and their logins", "Redirect plan exists before any migration"],
                "alt": "Checklist of website ownership questions for small businesses in Houston choosing between WordPress, Wix and Squarespace",
                "caption": "If you can tick every box, switching platforms later is a project, not a crisis.",
            },
            "pick": {
                "type": "steps",
                "title": "Choose your platform in five questions",
                "sub": "Answer in order; stop at the first clear yes",
                "steps": [
                    ["Selling products online is the core?", "Choose Shopify, or WooCommerce if you already run WordPress."],
                    ["Need 20+ service or location pages?", "Lean WordPress, or Webflow if you have a designer on call."],
                    ["Will staff edit it with no web person?", "Lean Squarespace for polish or Wix for flexibility."],
                    ["Design is your brand and you have a designer?", "Webflow is worth a serious look."],
                    ["Plan to switch vendors someday?", "Self-hosted WordPress is the most portable option."],
                ],
                "alt": "Five-question decision steps for choosing WordPress, Wix, Squarespace, Webflow or Shopify for a small business in The Woodlands",
                "caption": "A quick filter. The business-type table above covers the common edge cases.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: SMS marketing in Texas
    {
        "slug": "sms-marketing-small-business-texas-rules",
        "title": "SMS Marketing for Small Businesses in Texas: Rules, Setup and What to Send",
        "seo_title": "SMS Marketing for Texas Small Businesses: Rules & Setup",
        "desc": "SMS marketing for small businesses in Texas: TCPA consent, SB 140, quiet hours, A2P 10DLC registration, platforms and what to text. Checklist included.",
        "category": "Strategy",
        "icons": ["HubSpot", "Google Business Profile", "Google Analytics"],
        "art": "b5",
        "hero": "sms",
        "hero_alt": "Illustration of a phone with text message bubbles for SMS marketing by small businesses in Texas and The Woodlands",
        "related": ["email-marketing-basics", "how-to-sell-more-event-tickets-houston", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>A boutique owner in Magnolia exports 2,300 phone numbers from her point-of-sale system, signs up for a texting app, and drafts “20% off this weekend only!” Her thumb is over the send button.</p>
<p>Please don’t press it.</p>
<p>SMS marketing for a small business in Texas works well and is perfectly legal when four things are true: every person on the list agreed to get marketing texts from you, your number is registered with the carriers (A2P 10DLC or toll-free verification), you honor STOP immediately, and you send during reasonable hours. A phone number collected at checkout is not consent to marketing texts. Texas’s SB 140 also brought texts under the state’s telemarketing law in September 2025, though the state has since said businesses texting with prior consent don’t need to register.</p>
<p>This guide covers the federal and Texas rules as they stand in November 2026, carrier registration, opt-in and opt-out language, platform options, and what to actually send. There’s a compliance checklist near the end.</p>
<blockquote><b>Not legal advice.</b> We’re marketers who set up and run text programs, not lawyers. The rules below changed several times in 2025 and 2026 and are still being litigated. Use this to get organized, then have a Texas attorney who handles TCPA work review your opt-in language and program before you launch.</blockquote>"""),

            ("Is SMS marketing worth it for a small business?", f"""<p>Often, yes. Texts get seen quickly, they work on every phone, and a short list of people who asked to hear from you can outsell a much bigger email list.</p>
<p>You’ll see “98% open rate” quoted everywhere. We’ve never found a current primary source for it, so we don’t use it. Texts do get read, which is exactly why a bad one annoys people more than a bad email.</p>
<p>SMS earns its keep for businesses with a reason to reach people <i>this week</i>:</p>
<ul>
<li>Restaurants filling a slow Tuesday or announcing a crawfish weekend.</li>
<li>Salons, lash studios and med spas filling same-day cancellations.</li>
<li>Venues and promoters with presales and “two days left” pushes (our <a href="/blog/how-to-sell-more-event-tickets-houston/">event ticket playbook</a> covers the timing).</li>
<li>Home services sending maintenance reminders before the July heat or after a hail storm.</li>
</ul>
<p>It’s a weaker fit for long, considered purchases like a $60,000 pool. And it should sit beside email, never replace it; if your email program is thin, start with our <a href="/blog/email-marketing-basics/">email marketing basics</a>.</p>"""),

            ("Text message marketing rules: the federal layer", f"""<p>The federal law is the Telephone Consumer Protection Act (TCPA), enforced by the FCC and, more painfully, by private lawsuits. Statutory damages run $500 per violating message, up to $1,500 if willful. A 2,000-person blast without consent is a math problem nobody wants.</p>
<!--fig:law-->
<h3>Consent for marketing texts</h3>
<p>FCC rules require “prior express written consent” for telemarketing calls and texts sent with autodialers. Under {SRC['cfr']}, that means a written agreement with the person’s signature (an electronic signature counts) that clearly authorizes you to send marketing messages, and that tells them they don’t have to agree as a condition of buying anything.</p>
<p>There’s a Texas-specific wrinkle. In <i>Bradford v. Sovereign Pest Control of TX</i>, decided February 25, 2026, the Fifth Circuit (which covers Texas) held that the TCPA itself doesn’t require <i>written</i> consent for telemarketing calls; clear oral consent can count, per {SRC['bradford']}. Don’t build your text program on that. The case was about calls, other circuits still follow the written-consent framework, and carriers require documented opt-in regardless. Get it in writing.</p>
<h3>Rules that changed (or didn’t) in 2025 and 2026</h3>
<ul>
<li><b>One-to-one consent: gone.</b> The FCC’s rule requiring consent to name a single seller was vacated by the Eleventh Circuit in <i>Insurance Marketing Coalition v. FCC</i> in January 2025, and the FCC formally dropped its attempt to amend the definition in a July 2025 order, per {SRC['imc']}.</li>
<li><b>Revocation of consent: in effect since April 11, 2025.</b> People can opt out by any reasonable means. Replies like stop, quit, end, revoke, opt out, cancel and unsubscribe count automatically, and you have no more than 10 business days to honor a request. You can’t force one exclusive way to opt out. See {SRC['revoke']}.</li>
<li><b>“Revoke all”: delayed.</b> The part that would make one opt-out apply to all your unrelated messages (say, appointment reminders too) has been {SRC['revokeall']}. Many platforms already behave this way.</li>
</ul>
<h3>Quiet hours and Do Not Call</h3>
<p>Federal rules bar telephone solicitations before 8 a.m. or after 9 p.m. in the recipient’s local time (same {SRC['cfr']} section). The FCC has also made clear that National Do Not Call protections cover marketing texts, which is one more reason your consent records need to be tidy.</p>"""),

            ("Texas SMS marketing law: what SB 140 changed", f"""<p>Texas Senate Bill 140 took effect September 1, 2025. It amended the state’s telephone solicitation law (Business and Commerce Code Chapter 302) so that text and image messages count as telephone solicitations, not just voice calls. On its own, that pulled thousands of small businesses into a registration scheme built for call centers.</p>
<p>Registration, if you need it, is not trivial. The {SRC['sos']} lists a $200 filing fee and a $10,000 security deposit, with registration good for one year and renewable.</p>
<p>Then came the relief. In <i>Ecommerce Marketers Alliance v. State of Texas</i>, the parties agreed to dismiss the case, and the court’s November 17, 2025 order recited that consent-based text marketing isn’t subject to Chapter 302’s registration and disclosure requirements. The Secretary of State’s FAQ now says a business texting with prior consent “is not required to complete the Telephone Solicitation Registration Statement.”</p>
<p>Two cautions. {SRC['klg']} notes the order isn’t binding precedent and no contested decision has ruled on consent-based texts under the amended law. And {SRC['nlr']} lists what’s still on the hook: cold texting, purchased lists and anything sent without prior consent. It also flags a separate exemption (Section 302.058) for sellers texting only current or former customers under the same name for at least two years, and notes the Texas No-Call list and Deceptive Trade Practices Act remedies still apply.</p>
<p>On hours, Texas Chapter 301 limits telephone solicitation calls to 9 a.m. to 9 p.m. Monday through Saturday and noon to 9 p.m. on Sunday. The National Law Review piece describes those hours as a call rule but recommends applying them to texts as a conservative step. We agree, and we go further: we schedule marketing texts between 10 a.m. and 8 p.m., and not before noon on Sunday.</p>
<p>The practical reading for a Woodlands or Houston small business: if every number on your list opted in to your marketing texts, you’re very likely outside the registration requirement. Document that consent like you’ll need to prove it.</p>"""),

            ("A2P 10DLC registration, toll-free verification and short codes", f"""<p>Separate from the law, the carriers run their own gatekeeping. Business texting from a regular 10-digit number is called A2P 10DLC (application-to-person, 10-digit long code), and carriers have blocked unregistered 10DLC traffic {SRC['block']}. If your texts “send” but nobody receives them, registration is the first thing to check.</p>
<p>Registration has two parts. The <b>brand</b> is your business: legal name, EIN, address, website. The <b>campaign</b> is what you’ll send and how people opt in, with sample messages. Your texting platform files both with The Campaign Registry on your behalf. Per {SRC['tw10']}, Twilio charges $46 one time for a standard brand (including secondary vetting) or $4.50 for a low-volume standard brand, a $15 campaign vetting fee, and monthly campaign fees such as $10 for standard campaigns, $1.50 for low-volume mixed and $2 for sole proprietors. Other platforms bundle or mark up these fees, so ask.</p>
<!--fig:register-->
<p>Common rejection reasons: a privacy policy that doesn’t mention texting, an opt-in description that doesn’t match the real form, sample messages missing the business name or STOP language, and an EIN that doesn’t match the legal name. Fix the website first, then submit.</p>
<p><b>Toll-free numbers</b> (888, 877 and so on) skip 10DLC but need toll-free verification instead. {SRC['twtf']} says unverified toll-free numbers have been blocked from texting US and Canadian phones since January 31, 2024, and verification takes about 3 to 5 business days. Toll-free is a good option if you don’t want a local-looking number or you’re texting mostly transactional updates.</p>
<p><b>Short codes</b> (five- or six-digit numbers) cost far more and suit high-volume senders. Most small businesses don’t need one.</p>"""),

            ("How to build an opt-in list the right way", f"""<p>The list is the whole program. Here’s where we see small businesses go wrong, and what to do instead.</p>
<!--fig:optin-->
<p>Good sign-up points for local businesses:</p>
<ul>
<li><b>Keyword to number.</b> A sign at the register or on the table tent: “Text PATIO to (936) 555-0142 for weeknight specials.” The reply confirms the program and frequency.</li>
<li><b>Website form or pop-up</b> with a separate, unchecked SMS checkbox and the full disclosure next to it.</li>
<li><b>Booking and checkout flows</b>, again with a separate checkbox. Appointment confirmations are transactional; marketing needs its own yes.</li>
<li><b>QR code</b> at events (a vendor booth at a Market Street event, a race expo) that opens a pre-filled text.</li>
</ul>
<p>Sample disclosure to put next to a form checkbox (have your attorney adapt it):</p>
<blockquote>By checking this box, I agree to receive recurring automated marketing text messages from [Business Name] at the number provided. Consent is not a condition of purchase. Up to 4 msgs/month. Msg &amp; data rates may apply. Reply HELP for help, STOP to cancel. See our Terms and Privacy Policy.</blockquote>
<p><b>Double opt-in</b> (“Reply Y to confirm” before the first marketing message) isn’t legally required in most setups. We recommend it for web forms anyway: it filters typos and pranks, leaves a clean timestamped record, and carriers like it. You’ll lose a few sign-ups who never reply. They weren’t going to buy.</p>
<p>And the POS list from the opening scene? Don’t text it. Invite those customers to join by email or a keyword on receipts.</p>"""),

            ("Opt-out language: STOP, HELP and what each message must include", f"""<p>Carrier guidelines and the FCC rules land on the same practical standard. Every marketing program needs:</p>
<ul>
<li><b>A confirmation text right after opt-in</b> with your business name, what they signed up for, how often you’ll text, “Msg &amp; data rates may apply,” and HELP and STOP instructions.</li>
<li><b>Your business name on every message</b>, ideally first. People don’t save your number.</li>
<li><b>Opt-out instructions</b> (“Reply STOP to opt out”) at least in the first message and periodically after. Many programs put it on every promotional text, which we prefer.</li>
<li><b>Automatic handling</b> of STOP, QUIT, END, REVOKE, OPT OUT, CANCEL and UNSUBSCRIBE, plus a human check of replies like “please stop texting me,” which also count as reasonable revocation.</li>
<li><b>A single opt-out confirmation</b>, then silence.</li>
</ul>
<p>Example confirmation: “[Restaurant]: You’re in! Expect up to 4 texts a month with specials and events. Msg &amp; data rates may apply. Reply HELP for help, STOP to cancel.”</p>
<p>Keep messages to one segment when you can. A standard SMS segment holds 160 plain characters; one emoji or curly quote can switch the message to a format that holds only 70 per segment, and you pay per segment. Some platforms bill MMS at several times the SMS rate, so save images for messages where they earn it.</p>"""),

            ("SMS marketing platforms for small businesses: honest fit notes", f"""<p>Pick by what the rest of your business runs on, not the slickest demo. Confirm prices before you sign.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform</th><th>Best fit</th><th>Pricing model</th><th>Our take</th></tr></thead>
<tbody>
<tr><td>Klaviyo</td><td>Shopify and online stores already using Klaviyo email</td><td>SMS credits on top of email; free plan includes 150 mobile credits a month</td><td>Great when email and SMS should share segments and flows. Overkill for a local service business.</td></tr>
<tr><td>Postscript</td><td>Shopify brands focused on SMS revenue</td><td>Starter $0/mo with $49 monthly minimum; Growth $100/mo; per-message fees plus carrier fees</td><td>Strong ecommerce tooling. Not built for a plumber or a salon.</td></tr>
<tr><td>Attentive</td><td>Larger ecommerce brands</td><td>Custom quote, contract</td><td>Powerful, but sized for bigger senders. Most small businesses should start elsewhere.</td></tr>
<tr><td>SimpleTexting</td><td>Local businesses that want campaigns plus two-way texting</td><td>From about $39/mo for 500 credits; $89 for 2,000</td><td>Easy to learn, keyword sign-ups built in. A sensible default for restaurants, gyms, retail.</td></tr>
<tr><td>Podium</td><td>Service businesses wanting texting, reviews and webchat in one inbox</td><td>Custom quote</td><td>Better for conversations and review requests than for blasts. Get the contract terms in writing.</td></tr>
<tr><td>Your existing CRM or field-service software</td><td>Shops already on HubSpot, ServiceTitan, Jobber, Housecall Pro and similar</td><td>Varies</td><td>Check first. You may already pay for texting, and the data stays in one place. Registration still applies.</td></tr>
</tbody></table></div>
<p>Sources: {SRC['klaviyo']}, {SRC['postscript']}, {SRC['simple']} (a competitor’s summary, so double-check), and {SRC['podium']} for Podium’s quote-based plan.</p>
<p>One thing we’d avoid: marketing texts from a personal cell or an unregistered business-line app. It feels personal and cheap, and it’s how messages vanish into carrier filters and consent records go missing.</p>"""),

            ("What to send (and how often) by type of business", f"""<p>Most small programs should send 2 to 4 marketing texts a month and say so at sign-up. Transactional texts (confirmations, reminders, “your tech is 20 minutes away”) are a different category and don’t count against that number, but keep them free of promotions or they start looking like marketing.</p>
<p>Some patterns that fit the Houston calendar:</p>
<ul>
<li><b>Restaurants:</b> one weekly special, one event (watch parties, crawfish season, a patio night when the humidity breaks in October). Send around 2 to 3 p.m. for same-day dinner.</li>
<li><b>Salons, lash and med spas:</b> same-day openings to a small “last-minute” list, plus a monthly offer. Never text treatment details or anything health-related that someone else reading the lock screen shouldn’t see.</li>
<li><b>HVAC and home services:</b> maintenance reminders in March and September, a pre-summer tune-up push before the July heat, and storm messaging after hail. Our <a href="/industries/service/">home services marketing</a> page has more on the seasonal rhythm.</li>
<li><b>Hurricane season (June 1 to November 30):</b> closures and reopenings are welcome texts. Pure promos during an active storm aren’t, and people remember.</li>
</ul>
<p>Write like a person. “[Restaurant]: 4 patio tables left for tonight’s live music, 7 p.m. Reply YES and we’ll hold one. STOP to opt out” beats “HUGE DEALS INSIDE” every time. Track redemptions with a code or unique link.</p>
<p>Review requests by text work well; send them to every customer, not a hand-picked few (our <a href="/blog/complete-guide-google-reviews/">Google reviews guide</a> explains why).</p>"""),

            ("SMS compliance checklist for Texas businesses", f"""<p>Print this, or paste it into whatever you use to run the business. Then have your attorney mark it up.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Item</th><th>What it means in practice</th><th>Where it comes from</th><th>Status, Nov 2026</th></tr></thead>
<tbody>
<tr><td>Written opt-in for marketing</td><td>Separate, unchecked checkbox or keyword; disclosure says automated marketing, not a condition of purchase</td><td>FCC rule 64.1200(f)(9); carrier requirements</td><td>In effect (Fifth Circuit ruling on calls doesn’t change carrier rules)</td></tr>
<tr><td>Consent records</td><td>Timestamp, source, exact language shown, phone number; keep for years</td><td>Best practice; your defense in any claim</td><td>Do it</td></tr>
<tr><td>Honor opt-outs fast</td><td>Keywords automatic; other clear requests handled within 10 business days at most (aim for minutes)</td><td>FCC revocation rules</td><td>In effect since Apr 11, 2025</td></tr>
<tr><td>One opt-out stops everything</td><td>“Revoke all” across unrelated messages</td><td>FCC rule</td><td>Delayed to Jan 31, 2027</td></tr>
<tr><td>Quiet hours</td><td>Federal 8 a.m. to 9 p.m.; Texas call hours 9 a.m. to 9 p.m. Mon to Sat, noon to 9 p.m. Sun</td><td>64.1200(c)(1); Tex. Bus. &amp; Com. Code Ch. 301</td><td>Apply the stricter Texas window</td></tr>
<tr><td>Texas registration</td><td>$200 fee and $10,000 security deposit if required</td><td>SB 140, Ch. 302</td><td>Consent-based texting not required to register, per SOS FAQ</td></tr>
<tr><td>Carrier registration</td><td>A2P 10DLC brand and campaign, or toll-free verification</td><td>Carriers and The Campaign Registry</td><td>Unregistered traffic blocked</td></tr>
<tr><td>Message content</td><td>Business name, STOP language, no misleading claims, no restricted content</td><td>Carrier guidelines; Texas DTPA</td><td>In effect</td></tr>
</tbody></table></div>
<!--fig:presend-->"""),

            ("Your next step", f"""<p>Starting from zero? Update your privacy policy to mention texting, pick a platform, register, set up one sign-up point (a keyword at the counter is easiest), and send your first campaign to a few dozen real opt-ins. Already texting? Pull your consent records this week, and pause any numbers you can’t trace to an opt-in.</p>
<p>Texting works best when ads and your website are filling the list in the first place. If you’re running Google or Meta ads and want to know whether that money is pulling its weight, ask for a free <a href="/contact/">Ad Spend Leak Check</a>: a 10-minute video showing where your budget is leaking, in your inbox within 48 hours. And if your site needs a rebuild before you add a texting sign-up, our comparison of <a href="{WEB}">WordPress, Wix, Squarespace and Webflow</a> is a good place to start.</p>"""),
        ],
        "faq": [
            ("Is it legal to send marketing text messages in Texas?",
             "Yes, if each recipient agreed to receive marketing texts from your business, you honor opt-outs promptly, you send during allowed hours, and your number is registered with carriers. Texas SB 140 brought texts under the state telemarketing law in September 2025, but the Secretary of State says businesses texting with prior consent do not need to register. This is not legal advice; confirm your program with a Texas attorney."),
            ("Do I need to register with the Texas Secretary of State to send SMS marketing?",
             "Usually not if your texts go only to people who gave prior consent. The Secretary of State FAQ says consent-based texters are not required to file the telephone solicitation registration, which otherwise carries a $200 fee and a $10,000 security deposit. Cold texting or texting purchased lists is a different story. The court order behind this position is not binding precedent, so document consent carefully."),
            ("What is A2P 10DLC registration and do small businesses need it?",
             "A2P 10DLC is the carrier system for business texting from regular 10-digit phone numbers. If you send marketing or customer texts through software from a local number, you need a registered brand and campaign, and unregistered traffic has been blocked since February 2025. Your texting platform submits it for you. Twilio, for example, charges a $15 campaign vetting fee plus monthly campaign fees."),
            ("What hours can you send marketing texts in Texas?",
             "Federal rules bar telephone solicitations before 8 a.m. or after 9 p.m. in the recipient's time zone. Texas law limits solicitation calls to 9 a.m. to 9 p.m. Monday through Saturday and noon to 9 p.m. on Sunday, and attorneys recommend applying those hours to texts. We schedule marketing texts between 10 a.m. and 8 p.m. and after noon on Sundays."),
            ("How often should a small business send marketing texts?",
             "For most local businesses, two to four marketing texts a month is plenty, and you should state the expected frequency when people sign up. Restaurants and salons with same-day openings can sometimes go higher for a small opted-in list. Watch your opt-out rate after each send; a jump means you are texting too often or sending offers people do not care about."),
        ],
        "figures": {
            "law": {
                "type": "stats",
                "title": "The numbers behind text marketing rules",
                "stats": [["$500", "TCPA damages per unlawful text, up to $1,500 if willful"], ["10", "Business days, at most, to honor an opt-out request"], ["$10k", "Texas security deposit if telephone solicitation registration applies"]],
                "note": "Source: TCPA, FCC rules, Texas Secretary of State",
                "alt": "Stat tiles with TCPA damages, FCC opt-out deadline and Texas registration deposit for SMS marketing by small businesses in Texas",
                "caption": f"Opt-out timing from the FCC rules described by {SRC['revoke']}; deposit from the {SRC['sos']}.",
            },
            "register": {
                "type": "steps",
                "title": "Getting a texting number approved",
                "sub": "A2P 10DLC path for a local 10-digit number",
                "steps": [
                    ["Fix your website", "Privacy policy and terms that mention texting; visible opt-in form."],
                    ["Register the brand", "Legal name, EIN and address exactly as the IRS has them."],
                    ["Register the campaign", "Use case, opt-in description and sample texts with STOP language."],
                    ["Wait for approval", "Often days; rejections usually point to a website or opt-in mismatch."],
                    ["Test, then launch", "Send to staff phones on different carriers before the first real send."],
                ],
                "alt": "Five steps for A2P 10DLC SMS registration for a small business in Texas, from website fixes to first send",
                "caption": "Your texting platform files the paperwork; you supply accurate business details and a compliant website.",
            },
            "optin": {
                "type": "compare",
                "title": "Building a text list",
                "left": {"title": "How lists get built wrong", "items": ["Exporting phone numbers from the POS", "Pre-checked SMS box hidden in checkout", "Buying or renting a list", "Texting business cards from an expo", "Consent buried in the terms page"]},
                "right": {"title": "A list you can actually text", "items": ["Keyword sign-up at the counter or table", "Separate, unchecked SMS checkbox", "Clear disclosure next to the box", "Double opt-in reply for web forms", "Timestamped record of every opt-in"]},
                "alt": "Comparison of risky and compliant ways to build an SMS marketing list for small businesses in The Woodlands and Houston",
                "caption": "The right-hand column grows slower and stays safe to use.",
            },
            "presend": {
                "type": "checklist",
                "title": "Before every marketing text",
                "sub": "A 60-second check for whoever hits send",
                "items": ["Only opted-in contacts in the audience", "Business name at the start", "STOP language included", "Inside 10 a.m. to 8 p.m. Central (noon on Sunday)", "One segment if possible; no surprise emoji", "Link or code to track results", "Nothing sensitive on the lock screen", "Not during an active storm unless it helps"],
                "alt": "Pre-send checklist for SMS marketing messages from small businesses in Texas, covering consent, timing and opt-out language",
                "caption": "Stricter than the law requires, on purpose. It keeps opt-outs and complaints low.",
            },
        },
    },
]
