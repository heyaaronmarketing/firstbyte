"""Batch 13 (module b): redesigning a website without losing Google rankings, and getting a website and domain
back from a web designer.

Research, redesign post: Google Search Central "Site move with URL changes" (permanent 301/308 redirects, no mass
redirects to the home page, keep redirects generally at least a year, change one thing at a time, few weeks or more
for medium sites, temporary ranking fluctuation, heavier crawling after the move); Google's redirects and Google
Search doc (302 not treated as canonical signal, instant vs delayed meta refresh, JavaScript redirects last resort);
Google's noindex doc (noindex must not be blocked by robots.txt); Search Console Change of Address help (domain and
subdomain moves only, not http to https or path changes, 180 days, keep redirects at least 180 days, keep old domain
a year); PPC Land on the June 17, 2026 site-move doc update covering www and non-www variants; Search Engine Journal
on John Mueller's one-year redirect advice (Dec 2021); Search Engine Roundtable on Gary Illyes at SMX Advanced 2017
(two weeks to about three months); Google's Core Web Vitals page (LCP 2.5 s, INP 200 ms, CLS 0.1); PPC Land on GA4
annotations (March 2025, Editor role, 1,000 per property).
Research, domain post: ICANN registrant transfer FAQ (auth code within five calendar days, may/must deny reasons,
60-day locks, transfer fee and expiry can't block, ICANN transfer complaint form); ICANN announcement on RDAP
replacing WHOIS for gTLDs on 28 January 2025 and the ICANN Lookup tool; ICANN Board resolution 2026.06.07.04 adopting
the Transfer Policy Review recommendations, implementation pending with no effective date; GNSO Council report to the
Board (720-hour locks, 336-hour TAC, 120 hours to issue TAC, dropping the 60-day change-of-registrant lock); U.S.
Copyright Office Circular 30 (work made for hire, nine categories) and 17 U.S.C. ch. 2 (201(a), 201(b), 204(a));
Google Business Profile request-ownership help (3 days to respond); Search Console owners and permissions help
(verified vs delegated owners, removing old tokens); GA4 move-a-property help (Administrator and Editor on both
accounts); Texas State Law Library small-claims FAQ ($20,000 justice court limit, Gov't Code 27.031).
Not fetched (permission prompts timed out): web.dev vitals article, ICANN Transfer Policy text page. Facts from those
were taken from Google's own Core Web Vitals page and ICANN's registrant FAQ instead.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # redesign post
    "gmove": A("https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes", "Google’s site move guide"),
    "gredir": A("https://developers.google.com/search/docs/crawling-indexing/301-redirects", "Google’s redirects documentation"),
    "gnoindex": A("https://developers.google.com/search/docs/crawling-indexing/block-indexing", "Google’s noindex documentation"),
    "gcoa": A("https://support.google.com/webmasters/answer/9370220", "Search Console’s Change of Address help page"),
    "ppccoa": A("https://ppc.land/googles-site-move-guide-now-covers-www-and-non-www-domain-variants/", "PPC Land"),
    "sej": A("https://www.searchenginejournal.com/google-keep-301-redirects-in-place-for-a-year/", "Search Engine Journal"),
    "ser": A("https://www.seroundtable.com/google-site-3-months-24019.html", "Search Engine Roundtable"),
    "gcwv": A("https://developers.google.com/search/docs/appearance/core-web-vitals", "Google’s Core Web Vitals page"),
    "ga4note": A("https://ppc.land/google-analytics-introduces-annotations-feature-to-enhance-data-context/", "PPC Land’s write-up of GA4 annotations"),
    # domain post
    "icfaq": A("https://www.icann.org/resources/pages/name-holder-faqs-2017-10-10-en", "ICANN’s registrant transfer FAQ"),
    "rdap": A("https://icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en", "ICANN’s RDAP announcement"),
    "lookup": A("https://lookup.icann.org/en", "ICANN Lookup"),
    "board": A("https://www.icann.org/en/board-activities-and-meetings/materials/approved-resolutions-regular-meeting-of-the-icann-board-07-06-2026-en", "the ICANN Board’s June 7, 2026 resolution"),
    "gnso": A("https://gnso.icann.org/sites/default/files/policy/2025/draft/gnso-council-recommendations-report-to-icann-board-tpr-wg-31mar25-en.pdf", "the GNSO Council’s report to the Board"),
    "complaint": A("https://forms.icann.org/en/resources/compliance/complaints/transfer/form", "ICANN’s transfer complaint form"),
    "circ30": A("https://www.copyright.gov/circs/circ30.pdf", "U.S. Copyright Office Circular 30"),
    "t17": A("https://copyright.gov/title17/92chap2.html", "Chapter 2 of the Copyright Act"),
    "gbp": A("https://support.google.com/business/answer/4566671?hl=en", "Google’s request-ownership help page"),
    "gsc": A("https://support.google.com/webmasters/answer/7687615?hl=en", "Search Console’s owners and permissions page"),
    "ga4move": A("https://support.google.com/analytics/answer/9305872?hl=en-GB", "Google’s move-a-property help page"),
    "sll": A("https://sll.texas.gov/faqs/small-claims-maximum", "the Texas State Law Library"),
}

REDESIGN = "/blog/website-redesign-without-losing-seo-rankings/"
DOMAIN = "/blog/get-website-domain-back-from-web-designer/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: redesign without losing rankings
    {
        "slug": "website-redesign-without-losing-seo-rankings",
        "title": "How to Redesign Your Website Without Losing Your Google Rankings",
        "seo_title": "Website Redesign Without Losing SEO Rankings",
        "desc": "How to redesign a website without losing Google rankings: crawl first, map every URL to a 301, keep what ranks, avoid staging noindex traps, watch 8 weeks.",
        "category": "SEO & AI search",
        "icons": ["Google", "Search Console", "Google Analytics"],
        "art": "b2",
        "hero": "browser",
        "hero_alt": "Illustration of a browser window for a website redesign that keeps Google rankings in Houston and The Woodlands",
        "related": ["signs-your-website-needs-a-redesign", "how-fast-should-your-website-load", "why-isnt-my-website-showing-up-on-google"],
        "sections": [
            (None, f"""<p>The new site went live on a Monday. It looked great. By Thursday the office manager at a Woodlands service company noticed the phone was quiet, and by the next Monday the owner was in Search Console staring at a line that had fallen off a cliff.</p>
<p>Nothing was “wrong” with the new site. It just had different addresses. The old /ac-repair-spring-tx/ page that had ranked for six years now returned a 404, and so did forty other pages. Google had been sending people to rooms that no longer existed.</p>
<p>To redesign a website without losing your Google rankings, you crawl and record every URL on the old site, map each one to its closest new page with a permanent 301 redirect, and keep the titles, copy and structured data that were earning traffic. Make sure the live site isn’t carrying the staging site’s noindex, keep your analytics and conversion tracking intact, and watch Search Console closely for about eight weeks after launch.</p>
<p>The rest of this post is the detail, in the order we do it.</p>"""),

            ("First, know which kind of change you’re making", f"""<p>“Redesign” covers a lot of ground. Google treats a new paint job very differently from a new domain, and the steps you need depend on which one you’re doing.</p>
<div class="bp-tbl"><table>
<thead><tr><th>What’s changing</th><th>Example</th><th>Redirects needed?</th><th>Change of Address tool?</th></tr></thead>
<tbody>
<tr><td>Design only, same URLs</td><td>New theme, same page addresses</td><td>No, but check nothing moved</td><td>No</td></tr>
<tr><td>Platform change</td><td>Wix to WordPress, Squarespace to Webflow</td><td>Almost always (URL patterns differ)</td><td>No</td></tr>
<tr><td>URL structure change</td><td>/services/ac-repair/ becomes /ac-repair/</td><td>Yes, every changed URL</td><td>No</td></tr>
<tr><td>HTTP to HTTPS</td><td>http:// to https://</td><td>Yes</td><td>No, Google detects it</td></tr>
<tr><td>New domain</td><td>oldname.com to newbrand.com</td><td>Yes, every URL</td><td>Yes, for every variant</td></tr>
</tbody></table></div>
<p>{SRC['gmove']} recommends changing only one thing at a time where you can. If you’re rebranding, moving domains and switching platforms in the same week, you lose the ability to tell which change caused a drop. We’d rather move the domain first and redesign a month later than do it all on one Saturday.</p>
<p>Google also suggests scheduling a move for a slower traffic period. For a Houston HVAC or roofing company, that means not launching in July or the week after a named storm. For a retailer, not in November.</p>
<p>If you’re still deciding whether you need a new site at all, our {L('/blog/signs-your-website-needs-a-redesign/', 'signs your website needs a redesign')} post is the place to start.</p>"""),

            ("Before anyone touches the design: crawl and inventory", f"""<p>Most ranking losses we get called in to fix trace back to one missing spreadsheet. Nobody wrote down what the old site had before it was replaced.</p>
<!--fig:inventory-->
<p>Here’s what goes into that spreadsheet:</p>
<ul>
<li><b>Every URL on the old site.</b> Run a crawler like Screaming Frog over the live site and export the list. Add URLs from the current XML sitemap too, since crawlers miss orphan pages.</li>
<li><b>Your top pages by search traffic.</b> In Search Console, go to Performance, set the date range to the last 12 or 16 months, open the Pages tab and export. These are the pages you protect at all costs.</li>
<li><b>Top landing pages and conversions from GA4.</b> Reports, then Engagement, then Landing page. A page that gets little traffic but produces half your form fills matters more than its traffic suggests.</li>
<li><b>Pages other sites link to.</b> Your SEO tool’s backlink report, or Search Console’s Links report. Each linked page needs a redirect or you lose that link’s value.</li>
<li><b>Titles, meta descriptions, H1s and structured data</b> for the top 50 pages. The crawler pulls these. Save them before the old site disappears.</li>
<li>PDFs, images that rank in image search, and any landing pages your ads point to.</li>
</ul>
<p>Keep a full copy of the old site, or at least the crawl export, after launch. When something drops in week three, you’ll want to compare the before and after.</p>"""),

            ("URL mapping and 301 redirects, done properly", f"""<p>Once you have the old URL list, every row gets a destination. Old URL in column A, new URL in column B, status in column C.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Old URL</th><th>New URL</th><th>Rule</th></tr></thead>
<tbody>
<tr><td>/services/ac-repair-spring-tx/</td><td>/ac-repair/spring-tx/</td><td>One-to-one, same topic</td></tr>
<tr><td>/blog/2019/05/hurricane-prep/</td><td>/blog/hurricane-prep-checklist/</td><td>Updated post on the same topic</td></tr>
<tr><td>/heating-repair-conroe.html</td><td>/heating-repair/conroe-tx/</td><td>Platform change, same page</td></tr>
<tr><td>/specials-summer-2021/</td><td>None (returns 410)</td><td>Expired offer, no equivalent</td></tr>
<tr><td>/about-us/team/ and /about-us/history/</td><td>/about/</td><td>Merged pages, closest match</td></tr>
</tbody></table></div>
<p>The rules from {SRC['gmove']}:</p>
<ul>
<li><b>Use permanent, server-side redirects</b> (301 or 308). Google says permanent redirects don’t cause a loss in PageRank.</li>
<li>Redirect straight to the final page. Avoid chains like old URL to interim URL to new URL. If a chain can’t be helped, keep it short.</li>
<li><b>Don’t send everything to the home page.</b> Google specifically warns against redirecting many old URLs to one irrelevant destination like the home page of the new site.</li>
<li>Let content you’ve truly dropped return a 404 or 410 rather than redirecting it somewhere unrelated.</li>
<li>Keep the redirects for as long as possible, generally at least a year.</li>
</ul>
<!--fig:redirects-->
<p>The redirect type matters. Per {SRC['gredir']}, Google follows a 302, but its indexing pipeline doesn’t treat a temporary redirect as a sign the new URL should be canonical, so the old URL can hang around in results. Instant meta refresh redirects are read as permanent, delayed ones as temporary, and JavaScript redirects are a last resort because rendering can fail.</p>
<p>Then test the map before launch. Load the old URL list into your crawler in list mode against the staging site (with redirects in place), and confirm every row returns a single 301 to a page that returns a 200.</p>"""),

            ("Keep what was ranking: titles, content and schema", f"""<p>Redirects pass the signals. They don’t protect you if the page on the other end is a different page.</p>
<p>The quiet killer in redesigns is the copy rewrite. A designer “cleans up” the AC repair page from 1,100 words to 140 words and three icons, removes the Spring and Klein references because they looked cluttered, and changes the title tag from “AC Repair in Spring, TX | Same-Day Service” to “Comfort Solutions.” The redirect works perfectly. The rankings still go.</p>
<p>For every page on your protect list:</p>
<ul>
<li>Keep the title tag and H1 close to what ranked, unless you have a reason backed by data to change them.</li>
<li>Carry the body copy over. You can tighten it and improve it. Don’t delete the sections that answered real questions.</li>
<li>Bring the structured data with you: LocalBusiness, Service, FAQ, Product, Review markup, whatever the old site had. Theme changes often drop it silently.</li>
<li><b>Keep image alt text and file names</b> on images that brought traffic.</li>
<li>Keep the page in the navigation if it was in the navigation. A top page buried three clicks deep loses internal link weight.</li>
</ul>
<p>Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} explains why those town-by-town pages carry so much of a Houston service company’s search traffic. They’re usually the first thing a redesign cuts and the last thing you want to lose.</p>"""),

            ("The staging site trap: noindex, robots.txt and passwords", f"""<p>Every new site gets built somewhere first. That staging site should be invisible to Google, and the live site shouldn’t be. Both halves of that sentence go wrong more often than you’d expect.</p>
<p>The two common versions of this mistake:</p>
<ol>
<li><b>The staging site gets indexed.</b> Someone forgets to hide it, Google finds it, and now you have a duplicate copy of your new site at staging.yourdomain.com or a developer’s preview URL. The best fix is a password on staging (HTTP authentication), which keeps everyone out, Google included.</li>
<li><b>The noindex follows the site to production.</b> WordPress has a “Discourage search engines from indexing this site” checkbox under Settings, then Reading. It gets ticked on staging and nobody unticks it at launch. Other platforms have their own version. The new site launches with a noindex tag on every page and starts falling out of Google within days.</li>
</ol>
<p>There’s a subtler trap too. Per {SRC['gnoindex']}, a noindex only works if Google can crawl the page and see it. If robots.txt blocks a page, Google never reads the noindex, and the URL can still show up in results when other pages link to it. So “block it in robots.txt” isn’t a reliable way to hide staging, and a leftover “Disallow: /” in the live robots.txt is a launch-day disaster of its own.</p>
<p>On launch day, view the source of the home page and three inner pages and search for “noindex.” Open yourdomain.com/robots.txt and read it. It takes two minutes and it’s the check we never skip.</p>"""),

            ("Change of Address in Search Console (domain moves only)", f"""<p>If you’re keeping your domain, skip this section. The Change of Address tool is only for moving from one domain or subdomain to another, per {SRC['gcoa']}. It isn’t for HTTP to HTTPS (Google works that out itself), for URL changes inside the same site, or for switching between www and non-www.</p>
<p>If you are moving domains, the steps:</p>
<ol>
<li>Verify both the old and new domains in Search Console with the same Google account. You must be an owner of both.</li>
<li>Have your 301 redirects live, at minimum from the old home page to the new one, and ideally for every page.</li>
<li>In the old property, open Settings, then Change of Address, pick the new property and submit.</li>
<li>Repeat for every subdomain variant of the old domain. Google updated its site move guide on June 17, 2026 to say this includes www and non-www, even if you weren’t using one of them, according to {SRC['ppccoa']}.</li>
</ol>
<p>Google says the tool forwards signals for 180 days, and asks you to keep redirects at least that long, longer if Google still sends traffic to the old URLs. It also recommends keeping the old domain registered for at least a year. We’d keep it forever. A lapsed old domain can get bought by someone who points your old links at whatever they like.</p>"""),

            ("Sitemaps and internal links", f"""<p>Submit a fresh XML sitemap of the new URLs in Search Console on launch day. Google’s guide notes that warnings about redirects on an old-URL sitemap are expected, so don’t panic if you keep the old sitemap around for a few weeks to help Google find the redirects.</p>
<p>Internal links are the part teams skip because “the redirects will handle it.” They will, but every internal link that hits a redirect is a wasted hop and a sign of a sloppy site. Update menus, footers, buttons and body links to point at the new URLs directly. Then crawl the new site and filter for internal links returning 3xx or 4xx codes.</p>
<p>Also update the links you control off the site: your Google Business Profile website and appointment links, Facebook and Instagram bio links, Yelp, Nextdoor, BBB and industry directories, email signatures, and the final URLs in every Google Ads and Meta ad. Ads pointed at a 404 keep spending.</p>"""),

            ("Core Web Vitals: don’t launch a slower site", f"""<p>New designs often arrive heavier than the old ones. Big hero videos, sliders, four web fonts, a chat widget and two tracking scripts that duplicate each other.</p>
<!--fig:cwv-->
<p>Per {SRC['gcwv']}, the targets for a good experience are a Largest Contentful Paint within 2.5 seconds, an Interaction to Next Paint under 200 milliseconds and a Cumulative Layout Shift below 0.1. Google says it highly recommends site owners achieve good Core Web Vitals for success in Search. Even apart from rankings, a slow site loses calls because people leave.</p>
<p>Test the staging site in PageSpeed Insights on the mobile tab before launch and compare it with the old site. If the new one is slower, fix it before launch rather than after. The usual culprits are an uncompressed hero image, lazy-loading the image at the top of the page, and third-party scripts loading before the content. Our {L('/blog/how-fast-should-your-website-load/', 'page speed guide')} goes deeper.</p>"""),

            ("Tracking and GA4 continuity", f"""<p>A redesign that keeps its rankings but breaks its tracking still costs you, because for the next two months nobody can tell whether the new site is working.</p>
<ul>
<li><b>Keep the same GA4 property and measurement ID.</b> Don’t create a new property for the new site. You lose the year-over-year comparison you’ll want in week four.</li>
<li>Rebuild every key event. If “generate_lead” fired on the old thank-you page and the new form shows an inline message instead, the event stops firing and your lead count drops to zero overnight.</li>
<li>Check Google Ads conversions separately. Many accounts import from GA4, some use the Google tag directly, and some use both. Submit a test lead and confirm it shows up in both places.</li>
<li><b>Carry over call tracking numbers.</b> Dynamic number insertion scripts often don’t make it into new templates.</li>
<li>Keep Search Console verified. If verification relied on an HTML file or meta tag on the old site, it can disappear with the old theme.</li>
</ul>
<p>Add a GA4 annotation on launch day so everyone reading reports later knows what happened. Annotations arrived in GA4 in March 2025: right-click a point on a line chart and choose Add annotation, which needs Editor access, per {SRC['ga4note']}.</p>
<p>Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'guide to tracking forms and calls in GA4 and Google Ads')} has the setup step by step.</p>"""),

            ("Launch-day checklist", f"""<p>Launch on a Tuesday or Wednesday morning, with the developer and whoever owns SEO both available for the rest of the week. Never on a Friday afternoon.</p>
<!--fig:launch-->
<p>Run the old URL list through the crawler against the live site within the first hour. Every row should be a single 301 to a 200 page. Anything else gets fixed that day. Google tends to crawl a moved site more heavily than usual right after the move, so the first few days are when broken redirects do the most damage. Google’s own guide says to make sure your server can handle the extra load.</p>
<p>Then use URL Inspection in Search Console on the home page and your five most important pages, and request indexing. It won’t make Google move faster across the whole site, but it confirms the live pages are crawlable and indexable.</p>"""),

            ("The 8 weeks after launch: what to watch", f"""<p>Launch is the middle of the project. The next eight weeks decide whether it worked.</p>
<!--fig:watch-->
<ul>
<li><b>Daily for the first week:</b> Search Console’s Pages report for new “Not found (404)” and “Excluded by noindex” entries, and GA4 for leads and calls compared with the same weekdays before launch.</li>
<li><b>Weekly through week four:</b> Search Console Performance, comparing clicks and impressions for your protect-list pages against the four weeks before launch. Check that the new URLs are appearing in results and the old ones are fading out.</li>
<li><b>Weeks four through eight:</b> rankings for your money keywords, Core Web Vitals field data as it builds up, and backlinks still pointing at old URLs.</li>
<li><b>Any week:</b> if a specific page drops hard while others hold, compare it with the saved copy of the old page. It’s almost always missing content, a changed title or a missing redirect.</li>
</ul>
"""),

            ("How big a dip to expect, and how long recovery takes", f"""<p>Some wobble is normal. Google’s site move guide says to expect temporary fluctuation in rankings during a move, and that a medium-sized site can take a few weeks or more for Google to start showing the new URLs instead of the old ones, with larger sites taking longer. Every URL on both the old and new site has to be crawled at least once for the move to finish.</p>
<p>Google people have given ranges over the years. Gary Illyes said at SMX Advanced in 2017 that a domain move can take two weeks for some sites and closer to three months for larger ones, as reported by {SRC['ser']}. John Mueller said in 2021 that Google recommends keeping redirects at least a year so it can be sure they’ve been seen a few times, per {SRC['sej']}.</p>
<!--fig:dip-->
<p>From the redesigns we’ve worked on and the broken ones we’ve been brought in to repair, our experience is this. A same-domain redesign with a complete redirect map and preserved content usually wobbles for a couple of weeks and settles. A redesign without a redirect map doesn’t recover on its own, because nothing is wrong from Google’s point of view; the old pages are simply gone. Fixing the redirects late helps, but you’re rebuilding from a lower starting point. We can’t promise a number for your site and nobody honest can.</p>
<p>If traffic is still down 20% or more on your protect-list pages at week six, stop waiting and go page by page. Our {L('/blog/why-isnt-my-website-showing-up-on-google/', 'troubleshooting guide for sites missing from Google')} covers the checks.</p>"""),

            ("Who should do this work", f"""<p>A good web designer can build a beautiful site and still have no idea any of this exists. Before you sign a redesign contract, ask who builds the redirect map, who carries over the content and schema, who checks tracking at launch and who watches Search Console for the eight weeks after. If the answer to all four is a shrug, budget for someone who does it.</p>
<p>Our team handles redesigns and migrations under {L('/services/web-design-seo-pr/', 'web design and SEO')}, with the SEO work built into the plan from the first meeting rather than bolted on at launch. If you’re weighing the cost, our {L('/blog/how-much-does-a-website-cost-the-woodlands/', 'website cost guide')} and {L('/blog/seo-cost-houston-the-woodlands/', 'SEO pricing guide')} lay out typical ranges. And if your designer is holding the old site hostage before you can even start, read our companion post on {L(DOMAIN, 'getting your website and domain back from a web designer')}.</p>
<p>If you’re planning a redesign and want it done without the Thursday-morning panic, <a href="/contact/">get in touch</a> and tell us what you’re changing.</p>"""),
        ],
        "faq": [
            ("Will redesigning my website hurt my SEO?",
             "It can, but it doesn’t have to. Rankings usually drop after a redesign because URLs changed without 301 redirects, ranking content was cut, title tags changed, or a staging noindex tag went live. If you map every old URL to its closest new page, keep the content and structured data that ranked, and check tracking and indexing at launch, most sites see only a short wobble before settling."),
            ("How long should I keep 301 redirects after a redesign?",
             "Google’s site move guide says to keep redirects as long as possible, generally at least one year. For a domain move, Search Console’s Change of Address help says to keep them at least 180 days and longer if Google still sends traffic to the old URLs. In practice we leave them in place indefinitely, since they cost almost nothing and old links keep working."),
            ("Do I need to use the Change of Address tool for a redesign?",
             "Only if you’re moving to a new domain or subdomain. Google says the Change of Address tool isn’t for HTTP to HTTPS moves, URL changes within the same site, or switching between www and non-www. If you’re moving domains, verify both properties, set up 301 redirects, and submit the change for every variant of the old domain, including www and non-www."),
            ("How long does it take to recover rankings after a website migration?",
             "Google says a medium-sized site can take a few weeks or more for the new URLs to replace the old ones, and larger sites take longer. A Google spokesperson once described the range as two weeks to about three months. A migration done with complete redirects usually settles within weeks. One done without redirects often doesn’t recover until the missing redirects and content are restored."),
            ("What is the most common mistake in a website redesign?",
             "In our experience it’s launching without a redirect map, so every old URL that ranked now returns a 404. A close second is the staging site’s noindex setting carried over to the live site, which tells Google to drop every page. Both are quick to check on launch day: crawl the old URL list against the new site, and search the page source for noindex."),
        ],
        "figures": {
            "inventory": {
                "type": "checklist",
                "title": "Save this before the old site goes",
                "sub": "The pre-redesign inventory",
                "items": ["Full crawl of every old URL", "URLs from the current XML sitemap", "Search Console top pages, 12 to 16 months", "GA4 landing pages with conversions", "Pages with backlinks from other sites", "Titles, H1s and meta descriptions", "Structured data on top pages", "Ad landing pages and PDFs"],
                "alt": "Checklist of what to inventory before a website redesign to protect Google rankings in Houston and The Woodlands",
                "caption": "One spreadsheet, filled in before design starts. It becomes your redirect map.",
            },
            "redirects": {
                "type": "compare",
                "title": "Redirects that lose rankings vs. keep them",
                "left": {"title": "Loses rankings", "items": ["Everything redirected to the home page", "302 temporary redirects", "Chains of three or four hops", "JavaScript redirects", "Removed in a few months"]},
                "right": {"title": "Keeps rankings", "items": ["Each old URL to its closest new page", "301 or 308 permanent redirects", "One hop straight to the final page", "Server-side redirects", "Kept at least a year"]},
                "alt": "Comparison of bad and good 301 redirect practices for a website redesign in Houston and The Woodlands",
                "caption": f"Based on {SRC['gmove']} and {SRC['gredir']}.",
            },
            "cwv": {
                "type": "stats",
                "title": "Core Web Vitals targets",
                "stats": [["2.5 s", "Largest Contentful Paint or faster"], ["200 ms", "Interaction to Next Paint or less"], ["0.1", "Cumulative Layout Shift or less"]],
                "note": "Source: Google Search Central",
                "alt": "Core Web Vitals targets to check before launching a redesigned website in Houston and The Woodlands",
                "caption": f"Thresholds from {SRC['gcwv']}. Test the mobile tab in PageSpeed Insights.",
            },
            "launch": {
                "type": "steps",
                "title": "Launch-day checklist",
                "sub": "In this order, before lunch",
                "steps": [["Check for noindex", "View source on key pages and read robots.txt."], ["Crawl the old URL list", "Every old URL: one 301 to a live 200 page."], ["Submit the new sitemap", "In Search Console, plus Change of Address if the domain moved."], ["Test tracking", "Submit a form, make a call, confirm GA4 and Google Ads record both."], ["Update outside links", "Business Profile, social bios, directories, ad final URLs."], ["Annotate GA4", "Mark the launch date so reports make sense later."]],
                "alt": "Six-step website launch day checklist for keeping SEO rankings after a redesign in Houston and The Woodlands",
                "caption": "The first two steps catch most of the disasters we see.",
            },
            "watch": {
                "type": "funnel",
                "title": "What to watch after launch",
                "stages": [["404s, noindex, leads and calls", "Daily, week 1"], ["Clicks on protect-list pages", "Weekly, weeks 1-4"], ["New URLs replacing old in results", "Weeks 2-6"], ["Keyword rankings and field speed data", "Weeks 4-8"]],
                "note": "Timing varies by site size",
                "alt": "Timeline of what to monitor in Search Console and GA4 for eight weeks after a website redesign in The Woodlands",
                "caption": "Most problems show up in the first two weeks, when they’re cheapest to fix.",
            },
            "dip": {
                "type": "columns",
                "title": "A clean redesign, week by week",
                "sub": "Weekly organic clicks as a share of pre-launch level",
                "labels": ["Pre", "Wk 1", "Wk 2", "Wk 3", "Wk 4", "Wk 6", "Wk 8"],
                "values": [100, 88, 92, 97, 99, 100, 100],
                "highlight": [6],
                "y_label": "% of pre-launch",
                "note": "Illustrative example of a redesign with a full redirect map. Without one, the line tends to fall and stay down.",
                "alt": "Illustrative chart of organic traffic after a website redesign with complete 301 redirects in Houston and The Woodlands",
                "caption": "Illustrative only. Your site’s curve depends on its size and how cleanly the move was done.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: get website and domain back
    {
        "slug": "get-website-domain-back-from-web-designer",
        "title": "How to Get Your Website and Domain Back From a Web Designer",
        "seo_title": "Get Your Website & Domain Back From a Web Designer",
        "desc": "How to get your website and domain back from a web designer: check who the registrant is, transfer the domain under ICANN rules, and recover your accounts.",
        "category": "Websites",
        "icons": ["Google Business Profile", "Search Console", "Google Analytics"],
        "art": "b1",
        "hero": "key",
        "hero_alt": "Illustration of a key for getting a website and domain back from a web designer in Houston and The Woodlands",
        "related": ["who-owns-google-ads-account-switch-agencies", "questions-before-hiring-marketing-agency", "how-much-does-a-website-cost-the-woodlands"],
        "sections": [
            (None, f"""<p>A plumbing company owner in Spring calls us on a Tuesday. His website has been down since Saturday. The designer who built it in 2017 stopped answering texts last year, and now there’s a “hosting account suspended” page where his homepage used to be. His email is down too, because it ran through the same domain.</p>
<p>He pays the invoices. He assumed he owned all of it. Then we looked up the domain and found it registered to the designer’s own business.</p>
<p>To get your website and domain back from a web designer, first look up who is listed as the domain’s registrant, because that person controls it, whoever paid. If it’s you, get into the registrar account (or have the registrar help you) and transfer the domain with its authorization code. If it’s the designer, ask in writing for a change of registrant or a transfer, and use the registrar and ICANN’s complaint process if they won’t cooperate. Then collect hosting, CMS and Google account access one at a time, and decide whether the site is worth recovering or rebuilding.</p>
<p>We’re marketers, not lawyers, and nothing here is legal advice. Where money or a contract dispute is involved, talk to a Texas business attorney.</p>"""),

            ("First, list what you need back", f"""<p>“My website” is usually five or six separate things, held in five or six separate accounts. Each one has a different owner, and you can win some back faster than others.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Asset</th><th>Where it lives</th><th>How to check who controls it</th><th>Urgency</th></tr></thead>
<tbody>
<tr><td>Domain name</td><td>A registrar (GoDaddy, Namecheap, Squarespace Domains, Cloudflare, etc.)</td><td>ICANN Lookup, then the registrar</td><td>Highest. Everything else depends on it.</td></tr>
<tr><td>DNS and email routing</td><td>Registrar, Cloudflare or the host</td><td>Nameservers in the lookup result</td><td>High. Your email depends on it.</td></tr>
<tr><td>Hosting</td><td>WP Engine, SiteGround, a reseller account, or the designer’s own server</td><td>Ask, or check the IP address owner</td><td>High if it’s lapsing</td></tr>
<tr><td>Site admin (CMS)</td><td>WordPress, Wix, Squarespace, Webflow</td><td>Whether you have an administrator login</td><td>Medium</td></tr>
<tr><td>Google Business Profile</td><td>business.google.com</td><td>Profile settings, People and access</td><td>High for local businesses</td></tr>
<tr><td>GA4 and Search Console</td><td>analytics.google.com, search.google.com/search-console</td><td>Admin, Access management; Settings, Users</td><td>Medium. History is the prize.</td></tr>
<tr><td>Design files, photos, logo</td><td>The designer’s computer or cloud drive</td><td>Your contract</td><td>Low, unless you plan to keep the design</td></tr>
</tbody></table></div>
<p>Work top to bottom. The domain matters most, because whoever controls it controls where your website and your email point.</p>"""),

            ("Registrant vs. account holder: who actually owns your domain", f"""<p>This is the distinction that catches most owners off guard. Two different people can be in charge of a domain.</p>
<ul>
<li><b>The registrant</b> (ICANN calls this the registered name holder) is the person or company listed in the domain’s registration record. The registrant has the rights in the domain, including the right to transfer it.</li>
<li><b>The account holder</b> is whoever logs in to the registrar account where the domain sits. That person can change settings and, in practice, can often change the registrant record too.</li>
</ul>
<p>In the best case, you’re both. In a common case, you’re the registrant but the domain sits in the designer’s registrar account alongside forty other client domains. In the worst case, the designer is listed as the registrant and holds the account. Paying the renewal invoices doesn’t change who’s listed.</p>
<p>ICANN’s guidance to domain holders is to keep registration contact details accurate and current, because those details are what protect you against unauthorized transfers. A record full of the designer’s email addresses works against you.</p>"""),

            ("Look up your domain with ICANN Lookup", f"""<p>The old WHOIS system was retired for generic top-level domains like .com, .net and .org. As of January 28, 2025, the Registration Data Access Protocol (RDAP) is the definitive source for that registration data, per {SRC['rdap']}. The easy way to use it is {SRC['lookup']}, ICANN’s own free lookup tool.</p>
<!--fig:lookup-->
<p>Type your domain in and read four things:</p>
<ol>
<li><b>Registrar.</b> The company the domain is registered through. This is who you’ll be dealing with.</li>
<li>Dates: creation, last update and expiration. If it expires next month, you have a deadline.</li>
<li><b>Status codes.</b> “clientTransferProhibited” means the registrar lock is on. That’s normal, and it’s turned off before a transfer. “redemptionPeriod” or “pendingDelete” means the domain has already expired and you need to act today.</li>
<li><b>Nameservers.</b> Where DNS is managed. If they point to the designer’s host, your website and email depend on that host.</li>
</ol>
<p>The registrant’s name will often be redacted for privacy. You may see only an organization name and state, or nothing. If it’s hidden, the registrar can confirm if you’re the registrant once you prove who you are, and your old renewal receipts or setup emails from the designer often show the account it was registered under.</p>
<p>Country-code domains like .us or .co.uk follow their own registry rules, so check that registry’s process if yours isn’t a .com, .net or similar.</p>"""),

            ("If you’re the registrant but don’t have the login", f"""<p>This is the easier situation. You have the rights. You just need the keys.</p>
<p>Try account recovery at the registrar first, using any email address you might have been set up with. If that fails, call the registrar’s support line, say you are the registrant and need access, and ask what identity verification they require. It usually means a government ID and something tying you to the business, like formation documents or a recent invoice under your company name. Some registrars will move the domain into a new account in your name once they verify you.</p>
<p>If the domain sits inside the designer’s account, you can also ask the designer to “push” it to an account you open at the same registrar. That keeps the domain at the same registrar and is usually instant. Under the current ICANN rules, a change to the registrant name, organization or email triggers a 60-day lock on transfers to another registrar, though some registrars let you opt out ahead of time, per {SRC['icfaq']}. Ask before the change is made.</p>"""),

            ("If the designer is listed as the registrant", f"""<p>Now you need their cooperation, or a dispute process. Start with the cooperative route, because it’s faster and cheaper than anything else on this page.</p>
<p>Ask in writing. Email is fine. Keep it short and factual, without threats:</p>
<blockquote><p>“Hi [name], we’re making some changes to how we manage our website and need to take over the domain [yourdomain.com]. Please either change the registrant to [your legal business name, your email], or remove the transfer lock and send the authorization code so we can transfer it to our own registrar account. We’d also like the hosting login and an administrator account on the site. Can you get this done by [date a week out]? Happy to pay any outstanding balance once we confirm the amount. Thanks.”</p></blockquote>
<p>Most designers do it. If they claim an unpaid balance, ask for an itemized invoice. If it’s legitimate, paying it is usually cheaper than fighting.</p>
<p>If they refuse or vanish, gather your evidence before going further: invoices you paid for the domain or the site, the contract or proposal, emails where they described the domain as yours, and your business formation documents. Contact the registrar’s support or legal team with that evidence and ask what their process is for a disputed registrant.</p>
<p>If the registrar won’t help and the designer won’t either, you’re in contract-dispute territory. That’s the point to call an attorney. Texas justice courts hear small claims up to $20,000, per {SRC['sll']}, which covers most web design disputes, though a court order about a domain is a different matter than a money judgment, and an attorney can tell you which you need.</p>"""),

            ("How a domain transfer works under ICANN’s current rules", f"""<p>Once you’re the registrant, moving the domain to a registrar account you control follows ICANN’s Transfer Policy. These are the rules in {SRC['icfaq']}:</p>
<!--fig:transfer-->
<ul>
<li><b>Your registrar must give you the authorization code</b> (also called an auth code, EPP code or transfer code) within five calendar days of your request.</li>
<li>A registrar may deny a transfer for evidence of fraud, a reasonable dispute over who authorized it, unpaid fees for a previous registration period, a written objection from the registrant, a lock you haven’t removed, or within 60 days of the initial registration or a previous transfer.</li>
<li>A registrar must deny a transfer during a UDRP, URS or transfer dispute proceeding, under a court order, or during a 60-day change-of-registrant lock.</li>
<li><b>A registrar can’t refuse because you haven’t paid its transfer fee</b>, and it can’t refuse because the domain expired or wasn’t renewed, unless a previous period is unpaid. A domain in its Redemption Grace Period has to be restored first, which can carry a redemption fee.</li>
</ul>
<p>In our experience, a transfer between two cooperative registrars wraps up in a few days to a week. Before you start, copy down every DNS record (especially MX records for email, and any TXT records used for verification) so you can recreate them if the DNS host changes. Losing email for three days because nobody saved the MX records is the most common self-inflicted wound we see in these moves.</p>
<!--fig:numbers-->"""),

            ("ICANN’s new transfer rules: adopted, not yet in effect", f"""<p>You’ll see blog posts saying the 60-day lock is gone. Not yet. In {SRC['board']}, ICANN’s Board adopted the Transfer Policy Review recommendations and directed ICANN staff to implement them, subject to prioritization, with an Implementation Review Team drafting the final policy language. The resolution gives no effective date, and as of this writing (November 2026) the current policy above still applies.</p>
<!--fig:policy-->
<p>The recommendations, per {SRC['gnso']}, would replace the 60-day locks after registration and after a transfer with 720-hour (30-day) locks, state the five days to issue an auth code as 120 hours, make an auth code valid for 336 hours (14 days) once set, and drop the 60-day transfer lock after a change of registrant. Check your registrar’s help pages for the date they adopt the new rules before you plan around them.</p>"""),

            ("Filing a complaint with ICANN", f"""<p>ICANN regulates registrars, not web designers. Its compliance team can act when a registrar breaks the Transfer Policy: refusing to give you an auth code within five days, denying a transfer for a reason the policy doesn’t allow, or ignoring your request entirely. For that, ICANN’s FAQ points you to {SRC['complaint']}.</p>
<p>Before you file, have the domain name, both registrars’ names, the dates you asked for the code and what the registrar told you, ideally in writing.</p>
<p>What ICANN won’t do is decide whether you or your designer should be the registrant. That’s a dispute between the two of you, governed by your agreement, and it goes to the registrar’s own process, negotiation or a court.</p>"""),

            ("Hosting, the CMS and the website files", f"""<p>Getting the domain back lets you point it anywhere. Getting the site itself back is a separate question.</p>
<ul>
<li><b>WordPress on hosting you don’t control.</b> Ask for an administrator account, then make a full backup with a plugin like UpdraftPlus or your new host’s migration tool before anything else changes. Ask for the hosting login or a copy of the files and database if the designer will provide one.</li>
<li><b>Wix, Squarespace or another hosted builder.</b> The site lives in someone’s account on that platform. Most let the account owner transfer a site to another account. Generally you can’t pick the design up and move it to a different platform, so “getting it back” means getting the account, or rebuilding.</li>
<li><b>Premium themes and plugins.</b> If the designer used their own agency licenses, those licenses may not transfer to you. Budget for your own.</li>
<li><b>Email.</b> If your email runs through the designer’s hosting or their Google Workspace or Microsoft 365 account, plan that move carefully. Export mailboxes before cutting anything off.</li>
</ul>
<p>If the hosting lapsed and the files are gone, the Wayback Machine may still have copies of your pages, which can at least save your copy and images for a rebuild.</p>"""),

            ("Who owns the design under copyright", f"""<p>Owners often assume that paying for a website means owning it. Copyright law doesn’t work that way by default.</p>
<p>Under {SRC['t17']}, copyright belongs at first to the author of the work. The exception is a “work made for hire.” Per {SRC['circ30']}, that covers work an employee creates within the scope of their job, or work that’s specially commissioned in one of nine listed categories (such as a contribution to a collective work, a compilation or part of an audiovisual work) when both sides sign a written agreement saying so. A freelance web designer isn’t your employee, and plenty of website contracts have no such clause.</p>
<p>Copyright can still be transferred, but section 204(a) of the Act says a transfer of ownership is valid only in writing, signed by the owner of the rights. So if your contract assigns the site, the code and the graphics to you, you’re in good shape. If you never signed anything, or the contract is silent, ownership of the design and code may be less clear than you assumed. Stock photos, fonts and themes carry their own license terms on top of that.</p>
<p>Two practical points. Your own content (your text, your photos, your logo if you made it or paid for it with an assignment) is a separate question from the designer’s code and layout. And for most small businesses, the domain, the content and the Google accounts are worth far more than a five-year-old theme. An attorney can read your contract and tell you where you stand.</p>"""),

            ("Google Business Profile, Analytics and Search Console", f"""<p>These are often the most valuable accounts to win back, and Google has a process for each.</p>
<!--fig:accounts-->
<p><b>Google Business Profile.</b> If someone else manages your profile, go to business.google.com/add, search for your business and choose Request Access when you see that someone else may manage it. Per {SRC['gbp']}, the current owner gets an email and has 3 days to respond. If they don’t, you may be able to claim the profile from the link in your confirmation email. If they deny it, you can appeal. Once you’re in, make yourself the primary owner and remove anyone who shouldn’t be there. If the profile has gone sideways along the way, our {L('/blog/google-business-profile-suspended-reinstatement/', 'suspension and reinstatement guide')} covers that.</p>
<p><b>Search Console.</b> You don’t need the designer’s permission. Verify ownership yourself, for example with a DNS record once you control the domain. Then, per {SRC['gsc']}, remove the old owner from Settings, then Users and permissions, and also delete their verification token (their HTML file, meta tag or DNS record). Removing the user alone leaves the token, and the token lets them verify again.</p>
<p><b>GA4.</b> Ask the designer to give you the Administrator role on the property under Admin, then Property access management. If the property sits inside the designer’s own Analytics account, it can be moved to an account you own; per {SRC['ga4move']}, whoever moves it needs the Administrator and Editor roles on both the source and destination accounts. If they won’t cooperate, you can create a new property, but the history stays behind.</p>
<p>Google Ads has its own rules about who owns the account and the billing. We cover those in {L('/blog/who-owns-google-ads-account-switch-agencies/', 'who owns your Google Ads account')}.</p>"""),

            ("What to put in writing next time", f"""<p>Every one of these fights is easier to prevent than to win. Whoever you hire next, including us, get these in the agreement:</p>
<!--fig:contract-->
<p>Make the agreement say plainly that the domain, the hosting account and every Google and Meta account are in your company’s name, and that the agency or designer gets user access, not ownership. Ask any agency the questions in {L('/blog/questions-before-hiring-marketing-agency/', 'our list of questions to ask before hiring a marketing agency')}, and read {L('/blog/marketing-agency-pricing-models-retainer-vs-percentage/', 'our breakdown of agency pricing models')} to see where ownership terms tend to hide in a retainer.</p>"""),

            ("When to rebuild instead of recovering", f"""<p>Sometimes the old site isn’t worth the fight. Our rule of thumb: always recover the domain, the Google Business Profile and your content. The design and code are negotiable.</p>
<ul>
<li><b>Recover</b> if the site still ranks well, converts well, runs on a mainstream platform and you can get an administrator login and a backup without a long dispute.</li>
<li><b>Rebuild</b> if the site is on a builder tied to the designer’s account, runs an outdated theme nobody can update, loads slowly on phones, or the designer wants more than a new site would cost to hand it over.</li>
</ul>
<p>If you rebuild, the ranking risk is real, because the new site will almost certainly have different URLs. Follow {L(REDESIGN, 'our guide to redesigning without losing your Google rankings')}: save the old URL list from Search Console before anything changes, and redirect every one of them. Our {L('/blog/signs-your-website-needs-a-redesign/', 'signs your website needs a redesign')} post and {L('/blog/how-much-does-a-website-cost-the-woodlands/', 'website cost guide')} can help you decide.</p>
<p>If you’re stuck halfway through one of these and want someone who’s untangled it before, <a href="/contact/">get in touch</a>. Tell us what you can and can’t access, and we’ll lay out the order to do it in.</p>"""),
        ],
        "faq": [
            ("Who owns my domain if my web designer registered it?",
             "Whoever is listed as the registrant in the domain’s registration record controls it, regardless of who paid. If your designer registered it under their own name or business, they hold the rights until they change the registrant or transfer it to you. Look the domain up at ICANN Lookup, then contact the registrar. If the designer won’t cooperate, gather your invoices and contract and talk to an attorney."),
            ("How do I get my domain transfer authorization code?",
             "Sign in to your registrar account and look for an option to remove the transfer lock and get the transfer or EPP code. If you can’t find one, contact the registrar. Under ICANN’s registrant FAQ, your registrar must provide the code within five calendar days of your request. If it refuses or ignores you without a valid reason, you can file a transfer complaint with ICANN Compliance."),
            ("Can I transfer my domain within 60 days?",
             "Under ICANN’s current Transfer Policy, a registrar may deny a transfer within 60 days of the initial registration or a previous transfer, and a change to the registrant’s name, organization or email triggers a 60-day transfer lock unless your registrar offered an opt-out. ICANN’s Board adopted changes in June 2026 that would shorten these locks, but they hadn’t taken effect as of November 2026."),
            ("Does my web designer own the copyright to my website?",
             "Possibly. Under U.S. copyright law, the creator owns the work by default unless it qualifies as a work made for hire or the rights were transferred in a signed writing. An independent designer’s work usually isn’t work for hire without a written agreement in a qualifying category. Your own text, photos and logo are separate questions. Have an attorney review your contract; this isn’t legal advice."),
            ("How do I get my Google Business Profile back from a former agency?",
             "Ask the agency to make you primary owner first. If they won’t, go to business.google.com/add, find your business and select Request Access. Google emails the current owner, who has 3 days to respond. If they don’t respond, you may be able to claim the profile from your confirmation email. If they deny the request, you can appeal through Google Business Profile support."),
        ],
        "figures": {
            "lookup": {
                "type": "steps",
                "title": "Find out who controls your domain",
                "sub": "Ten minutes with ICANN Lookup",
                "steps": [["Search lookup.icann.org", "Enter your domain. RDAP data replaced WHOIS for .com and similar in 2025."], ["Note the registrar", "That company holds the registration and handles transfers."], ["Check the dates", "An expiration date next month is your deadline."], ["Read the status codes", "Transfer lock is normal. Redemption or pending delete is an emergency."], ["Check the nameservers", "They show who controls DNS, and so your website and email."]],
                "alt": "Steps to look up who controls a business domain with ICANN Lookup before getting it back from a web designer in Houston",
                "caption": f"Use {SRC['lookup']}. Registrant names are often redacted, so the registrar may need to confirm it.",
            },
            "transfer": {
                "type": "steps",
                "title": "Moving the domain to your own registrar",
                "sub": "Once you are the listed registrant",
                "steps": [["Save your DNS records", "Screenshot or export every record, especially MX and TXT."], ["Remove the lock", "Turn off the transfer lock at the current registrar."], ["Get the auth code", "The registrar must provide it within five calendar days."], ["Start at the new registrar", "Enter the domain and code in an account in your company’s name."], ["Approve and confirm", "Approve the emails, then check the website and email still work."]],
                "alt": "Five steps to transfer a domain from a web designer’s registrar account to the business owner in Houston and The Woodlands",
                "caption": f"Rules from {SRC['icfaq']}. Expect a few days to a week in our experience.",
            },
            "numbers": {
                "type": "stats",
                "title": "Deadlines worth knowing",
                "stats": [["5 days", "for a registrar to provide your auth code"], ["60 days", "transfer lock after registration, transfer or registrant change"], ["3 days", "for a Business Profile owner to answer your request"], ["$20,000", "Texas justice court small claims limit"]],
                "note": "Sources: ICANN, Google Business Profile Help, Texas State Law Library",
                "alt": "Key deadlines for getting a domain and Google Business Profile back from a web designer in Houston and Texas",
                "caption": "The 60-day figure is the current ICANN policy. Adopted changes would shorten it once implemented.",
            },
            "policy": {
                "type": "compare",
                "title": "ICANN transfer rules: now vs. adopted",
                "left": {"title": "In effect now", "items": ["60-day lock after registration", "60-day lock after a transfer", "60-day lock after registrant change (opt-out at some registrars)", "Auth code within 5 calendar days"]},
                "right": {"title": "Adopted June 2026, pending", "items": ["720-hour (30-day) lock after registration", "720-hour lock after a transfer", "Change-of-registrant lock dropped", "Code within 120 hours, valid 336 hours"]},
                "alt": "Comparison of current and adopted ICANN domain transfer policy rules for business owners in Houston and The Woodlands",
                "caption": f"From {SRC['icfaq']} and {SRC['gnso']}. No effective date had been set as of November 2026.",
            },
            "accounts": {
                "type": "checklist",
                "title": "Accounts to take back",
                "sub": "In your company’s name, with your own login",
                "items": ["Domain registrar account", "DNS host (if separate)", "Website hosting", "CMS administrator login", "Email (Workspace or Microsoft 365)", "Google Business Profile, primary owner", "Search Console, verified owner", "GA4, Administrator role", "Google Ads and Meta Business Manager", "Call tracking and form tools"],
                "alt": "Checklist of website and Google accounts a Houston business should recover from a former web designer or agency",
                "caption": "Remove old users and old Search Console verification tokens once you’re in.",
            },
            "contract": {
                "type": "checklist",
                "title": "Put this in your next web contract",
                "sub": "Before the first invoice",
                "items": ["Domain registered with your company as registrant", "Hosting and registrar accounts in your name", "Copyright in the site assigned to you in writing", "Theme, plugin and font licenses listed", "Google and Meta accounts owned by you", "Agency gets user access, not ownership", "Handover of logins and files on exit", "A full backup delivered at launch"],
                "alt": "Checklist of ownership clauses for a website design contract for Houston and The Woodlands small businesses",
                "caption": "Not legal advice. Have your attorney turn these into contract language.",
            },
        },
    },
]
