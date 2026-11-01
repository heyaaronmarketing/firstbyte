"""Batch 8 (agency intent): a step-by-step diagnostic for a website that isn't showing up on Google, and a setup guide
for tracking form submissions and phone calls in GA4 and Google Ads on a lead-gen site.

Research: Google Search Central on the site: operator, the SEO starter guide (timing, discovery), noindex and robots.txt;
Search Console help on URL Inspection (verdict names, request indexing, daily limits), the single-page troubleshooting
flow, the Page indexing report (reason names, "don't expect every URL", validation up to about two weeks) and the Manual
actions report; Wix, Squarespace and WordPress visibility settings; Google Business Profile local ranking factors.
GA4 post: Search Engine Roundtable on the March 2024 conversions-to-key-events rename, GA4 help on marking key events
(30 per standard property), enhanced measurement form events, recommended lead events, DebugView; GTM form submission
trigger settings; Google Ads phone call conversion types and GA4 import differences; Google consent mode overview;
Texas Attorney General on the TDPSA. Competitors read: WebFX on why sites don't show up; Measureschool and Fishtank on
GA4 form tracking.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "site": A("https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site", "Google’s own documentation on the site: operator"),
    "starter": A("https://developers.google.com/search/docs/fundamentals/seo-starter-guide", "SEO starter guide"),
    "inspect": A("https://support.google.com/webmasters/answer/9012289?hl=en", "URL Inspection tool"),
    "single": A("https://support.google.com/webmasters/answer/12482179", "troubleshooting checklist for a single page"),
    "pir": A("https://support.google.com/webmasters/answer/7440203", "Page indexing report"),
    "noindex": A("https://developers.google.com/search/docs/crawling-indexing/block-indexing", "Google’s noindex documentation"),
    "manual": A("https://support.google.com/webmasters/answer/9044175?hl=en", "Manual actions report"),
    "wix": A("https://support.wix.com/en/article/enabling-search-engines-like-google-to-index-your-site", "Wix’s help page"),
    "sqsp": A("https://www.collaborada.com/blog/hiding-content", "this Squarespace walkthrough from Collaborada"),
    "wp": A("https://kinsta.com/blog/discourage-search-engines-from-indexing-this-site/", "Kinsta’s explainer"),
    "local": A("https://support.google.com/business/answer/7091?hl=en", "Google’s local ranking help page"),
    # GA4 post
    "rename": A("https://www.seroundtable.com/google-analytics-ads-conversion-metrics-37096.html", "Search Engine Roundtable"),
    "keyev": A("https://support.google.com/analytics/answer/13128484", "Google’s key events help page"),
    "em": A("https://support.google.com/analytics/answer/9216061?hl=en", "enhanced measurement documentation"),
    "rec": A("https://support.google.com/analytics/answer/9267735", "recommended events list"),
    "gtmform": A("https://support.google.com/tagmanager/answer/7679217?hl=en", "Tag Manager’s trigger documentation"),
    "calls": A("https://support.google.com/google-ads/answer/6100664", "Google Ads’ phone call conversion page"),
    "import": A("https://support.google.com/google-ads/answer/2375435?hl=en", "Google’s import documentation"),
    "consent": A("https://developers.google.com/tag-platform/security/concepts/consent-mode", "consent mode overview"),
    "debug": A("https://support.google.com/analytics/answer/7201382?hl=en", "DebugView help page"),
    "tdpsa": A("https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/enforcing-privacy-and-data-security-laws-protect-texans/texas-data-privacy-and-security-act", "Texas Attorney General"),
}

L = lambda path, name: f'<a href="{path}">{name}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: not showing up on Google
    {
        "slug": "why-isnt-my-website-showing-up-on-google",
        "title": "Why Isn’t My Website Showing Up on Google? A Troubleshooting Guide",
        "seo_title": "Why Isn’t My Website Showing Up on Google?",
        "desc": "Why isn’t your website showing up on Google? Run our step-by-step diagnostic, with real Search Console statuses and fixes for Houston-area businesses.",
        "category": "SEO & AI search",
        "icons": ["Google", "Search Console", "Google Business Profile"],
        "art": "b3",
        "hero": "search",
        "hero_alt": "Illustration of a magnifying glass and map pin for a guide to why your website isn’t showing up on Google in Houston",
        "related": ["how-long-does-seo-take-houston-the-woodlands", "signs-your-website-needs-a-redesign", "local-seo-checklist-the-woodlands"],
        "sections": [
            (None, f"""<p>You’re sitting in the truck outside a job in Spring, you type your company name into Google, and you scroll. Yelp is there. Your Facebook page is there. Some directory you’ve never heard of is there. Your new website, the one you paid for in August, is nowhere.</p>
<p>It’s almost always one of two problems. Either Google hasn’t indexed the site at all (it’s new, or something is telling Google to stay out), or it’s indexed but doesn’t rank for the searches you tried. Occasionally there’s a sneakier third case, where you’re looking at the map results, which run on your Google Business Profile, and blaming the website for them. Each has a different fix. Diagnose first, then touch settings.</p>
<p>What follows is the order we check things in when an owner in The Woodlands or anywhere around Houston sends us that exact panicked text. Most of it takes an hour and costs nothing.</p>
<!--fig:order-->"""),

            ("Is my website indexed? Start with a site: search", f"""<p>Open Google (on google.com itself, not by typing into your browser’s address bar) and search <b>site:yourdomain.com</b> with no space after the colon. Then try a single important page with the full address, like <b>site:yourdomain.com/ac-repair</b>.</p>
<p>Per the {SRC['starter']}, if results point to your site, you’re in the index. That one search splits the problem in half.</p>
<p>Zero results means Google has nothing. That’s an indexing problem, and it usually has a mechanical cause you’ll find in the next two sections. If some pages come up but not the ones that matter, you’re partially indexed, so look at which are missing and why (duplicates, thin pages, a broken canonical).</p>
<p>And if dozens of pages come up but you still can’t find yourself for “plumber Conroe”? You’re indexed. That’s a ranking problem, it’s slower, and no checkbox will fix it.</p>
<p>Don’t treat the count as gospel. {SRC['site']} says the list is “not always exhaustive” and that the results beyond the first one are “relatively random.” Use it as a smoke test, then confirm in Search Console.</p>"""),

            ("Website not indexed? What Google Search Console will tell you", f"""<p>If you don’t have Search Console set up, do that first. It’s free, and it’s the only place Google tells you directly why a page isn’t in the index. Verify a <b>Domain property</b> through a DNS record at your registrar (GoDaddy, Squarespace Domains, Cloudflare) so it covers every version of your address.</p>
<h3>URL Inspection: one page at a time</h3>
<p>Paste your homepage URL into the bar at the top. The {SRC['inspect']} gives one of four verdicts: <b>URL is on Google</b>, <b>URL is on Google, but has issues</b>, <b>URL is not on Google</b>, or <b>URL is an alternate version</b>. If it’s not on Google, expand the indexing section and read four lines, the same ones Google’s {SRC['single']} walks through:</p>
<ol><li><b>Crawl allowed?</b> Anything but “Yes” means robots.txt is blocking Google.</li>
<li>Page fetch should say “Successful.” If it doesn’t, Google hit an error: a 404, a server error, a login wall.</li>
<li>A “No” under <b>Indexing allowed?</b> means there’s a noindex directive on the page.</li>
<li>Then the Google-selected canonical. If Google picked a different URL as the main version, this page is being treated as a duplicate.</li></ol>
<p>If <b>Last crawl</b> is blank, Google simply hasn’t found the page yet. Click <b>Test live URL</b>, then <b>Request indexing</b>. Google says there’s a daily limit on those requests and that a request doesn’t guarantee anything, so spend them on your handful of money pages and let the sitemap handle the rest. (Clicking it again every morning doesn’t speed anything up. People try.)</p>
<h3>Page indexing report: the whole site</h3>
<p>Under <b>Indexing → Pages</b>, the {SRC['pir']} lists every reason pages weren’t indexed. The names you’ll see most on small business sites are <b>Excluded by ‘noindex’ tag</b>, <b>Blocked by robots.txt</b>, <b>Crawled - currently not indexed</b>, <b>Discovered - currently not indexed</b>, <b>Duplicate without user-selected canonical</b>, <b>Alternate page with proper canonical tag</b>, <b>Page with redirect</b>, <b>Not found (404)</b> and <b>Soft 404</b>.</p>
<p>Some of those are fine. “Page with redirect” on your old URLs after a redesign is exactly what should happen. Google’s own line is that you “should not expect all URLs on your site to be indexed.” Save the worrying for pages that are supposed to make the phone ring.</p>"""),

            ("Did a redesign or a website builder hide your site from Google?", f"""<p>We find this one more than anything else, and it’s almost always innocent. Designers build new sites on a staging copy and tell Google to stay away while it’s unfinished. Then launch day comes, everybody is busy testing the contact form, and nobody flips the switch back.</p>
<p>On WordPress the switch is under Settings → Reading → <b>Search engine visibility</b>. If “Discourage search engines from indexing this site” is ticked, uncheck it. Per {SRC['wp']}, the box works by adding a robots meta tag that tells search engines not to index the site.</p>
<p>Other platforms hide it in different places:</p>
<ul><li>Wix has a <b>Let search engines index your site</b> toggle in SEO Settings. {SRC['wix']} has the current menu path, which Wix has moved around more than once.</li>
<li>On Squarespace, a site-wide password or Site Availability set to Private keeps Google out. So does the per-page <b>Hide Page from Search Results</b> toggle under the page’s SEO settings, as {SRC['sqsp']} explains. Owners turn that on for a draft services page and forget it.</li>
<li>Custom or developer-built sites: look for a robots.txt with <b>Disallow: /</b> left over from staging, and an HTTP header called X-Robots-Tag set to noindex.</li></ul>
<p>The quick check on any platform: open your homepage, right-click, choose View Page Source, and search the page for “noindex.” If you find it in a robots meta tag on a page you want found, that’s your answer.</p>
<p>One trap worth knowing. Blocking a page in robots.txt doesn’t remove it from Google, and it can actually stop a noindex from working. {SRC['noindex']} says plainly that the page “must not be blocked by a robots.txt file” or Google never sees the noindex. For pages you want hidden, use noindex and leave robots.txt alone.</p>
<!--fig:launch-->
<p>If your redesign launched months ago and traffic never came back, our post on {L('/blog/signs-your-website-needs-a-redesign/', 'signs your website needs a redesign')} covers the other side of it: when the new site itself is the problem.</p>"""),

            ("Canonical tags, duplicate pages and thin content", f"""<p>A canonical tag tells Google which version of a page is the real one. When it’s right, nobody notices it. When it’s wrong, it quietly hands your rankings to another URL.</p>
<p>After a launch, the usual culprit is a canonical on every page pointing at the staging domain, or at the homepage. Google reads that as “this page is a copy of that one” and indexes the other address. URL Inspection shows it as a mismatch between the user-declared canonical and the Google-selected one. Fixing it is a one-line change in your SEO plugin or theme, then Request indexing on the main pages.</p>
<p>Sites also duplicate themselves. Service-area pages are the repeat offender: twenty near-identical pages reading “Best AC repair in Tomball,” “Best AC repair in Magnolia” and so on down the list, with only the town name swapped. Google often indexes one or two and drops the rest into <b>Duplicate without user-selected canonical</b> or <b>Crawled - currently not indexed</b>. We’d write five real pages before twenty clones. A Magnolia page that mentions the actual neighborhoods you serve, the jobs you’ve done off FM 1488, and your real response time out there is worth more than ten clones.</p>
<p>Thin pages get the same treatment. A “Services” page with a list of six bullet points and nothing else gives Google little reason to index it, and honestly, it gives a customer little reason to call.</p>"""),

            ("Why does my business show up when I search the name but not for my services?", f"""<p>Because indexing and ranking are different things. If <b>site:</b> finds you and a search for your business name brings you up first, Google has your site and trusts it’s yours. That part works.</p>
<p>Searching “ac repair the woodlands” is a different contest. You’re now competing with every HVAC company that serves 77380 and 77382, plus directories, plus companies that have been publishing pages and collecting links and reviews for ten years. A two-month-old site will lose that race for a while, even with everything set up perfectly.</p>
<!--fig:rank-->
<p>Open Search Console’s <b>Performance</b> report first. It shows the queries you already get impressions for, and if service searches appear at an average position of 30 or 40, you’re in the game, just far back.</p>
<p>Then put your service page next to the three that rank above you and count the words, photos and reviews, plus how many real specifics each one gives. Whatever they have that you don’t goes on the to-do list.</p>
<p>How long it takes to close that gap is its own question, and we answer it honestly in {L('/blog/how-long-does-seo-take-houston-the-woodlands/', 'how long SEO takes in Houston and The Woodlands')}. Short version: it’s measured in months, and longer in crowded trades like roofing.</p>"""),

            ("My business is not showing on Google Maps. Is that the website’s fault?", f"""<p>Usually not. The map results (the “local pack” with three businesses and a map) come mostly from your <b>Google Business Profile</b>, which is a separate thing from your website. A business can have a beautiful, fully indexed site and still be missing from the map, or rank in the map with no website at all.</p>
<p>Google names three factors in {SRC['local']}: relevance (how well the profile matches the search), distance (how far the business is from the searcher), and prominence (how well-known it is, including links and reviews). It also says a verified profile is “more likely to show up in search results.” Start with the boring checks:</p>
<ul><li>Is the profile verified, and not suspended? Sign in at business.google.com and look.</li>
<li>Is your primary category the thing people search? “Air conditioning contractor” and “HVAC contractor” behave differently.</li>
<li>Are you searching from where your customers are? A shop in Conroe won’t appear for someone in Sugar Land searching “plumber near me,” and that’s distance working as designed.</li>
<li>Does the profile link to the matching page on your website, with the same name, address and phone?</li></ul>
<p>Our {L('/blog/local-seo-checklist-the-woodlands/', 'local SEO checklist for The Woodlands')} covers the profile side in depth. Fix it alongside the website, because for most service searches around here, the map shows up above the regular results.</p>"""),

            ("Manual actions, hacked sites and the rarer causes", f"""<p>Rare for a local business, but check, because it takes thirty seconds. In Search Console, open <b>Security &amp; Manual Actions</b>.</p>
<p>The {SRC['manual']} shows whether a human reviewer at Google has penalized the site. The types include “Thin content with little or no added value,” “Unnatural links to your site,” “Hidden text and/or keyword stuffing,” “User-generated spam” and “Site abused with third-party spam.” Google says most actions lower rankings or remove pages, and that it notifies you in the report and in the Search Console message center.</p>
<p>If you see one, fix every listed problem on every affected page (Google says partial fixes don’t restore anything), then click <b>Request Review</b> with a plain explanation of what you changed. Reviews can take days or weeks.</p>
<p>On the small business sites we audit, we see hacks far more often than penalties. Old WordPress plugins are the usual way in. Search <b>site:yourdomain.com</b> plus words like “casino” or “pills,” and if spam pages show up, you’ve been hacked.</p>
<p>A flaky host shows up as <b>Server error (5xx)</b> in the Page indexing report; pages usually come back once the site is stable. And if you bought an expired domain, look it up on the Wayback Machine. A previous owner’s spam can follow it.</p>"""),

            ("Symptom, cause and fix: the cheat sheet", f"""<p>Find the row that matches what you’re seeing. Start at the top; the cheapest fixes are first.</p>
<div class="bp-tbl"><table>
<thead><tr><th>What you see</th><th>Likely cause</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>site: search returns nothing</td><td>New domain not discovered yet, or the whole site is noindexed or password-protected</td><td>Check builder visibility settings, remove noindex, submit a sitemap, request indexing on the homepage</td></tr>
<tr><td>Fell out of Google right after a redesign</td><td>Staging noindex or robots.txt carried to the live site; old URLs not redirected</td><td>Remove the block; 301-redirect every old URL to its new match</td></tr>
<tr><td>“Excluded by ‘noindex’ tag” on pages that matter</td><td>Builder toggle, SEO plugin setting, or a hidden-page option</td><td>Turn the setting off, then Validate Fix in the report</td></tr>
<tr><td>“Blocked by robots.txt”</td><td>A Disallow rule covering pages you want found</td><td>Edit robots.txt; test the URL live</td></tr>
<tr><td>“Duplicate, Google chose different canonical than user”</td><td>Near-identical pages, or a canonical tag pointing to the wrong address</td><td>Fix canonicals; merge or rewrite clone pages</td></tr>
<tr><td>“Crawled - currently not indexed”</td><td>Google saw the page and didn’t think it was worth keeping</td><td>Make the page more useful and specific; link to it from your main pages</td></tr>
<tr><td>“Discovered - currently not indexed”</td><td>Google knows the URL but hasn’t crawled it yet</td><td>Add internal links and a sitemap; give it time</td></tr>
<tr><td>Shows for your name, not for services</td><td>Indexed but not competitive yet</td><td>Better service pages, reviews, local links; patience</td></tr>
<tr><td>Missing from the map</td><td>Business Profile unverified, wrong category, or distance</td><td>Verify, fix the category, link the profile to the right page</td></tr>
<tr><td>Sudden drop across the whole site</td><td>Manual action, hack, or server errors</td><td>Check Security &amp; Manual Actions and the 5xx count</td></tr>
</tbody></table></div>
<p>After you fix something in the Page indexing report, click <b>Validate Fix</b>. Google says validation “typically takes up to about two weeks,” sometimes longer, so don’t panic if the count doesn’t move on day three.</p>"""),

            ("How long should you wait before you worry?", f"""<p>For a brand-new domain, a week or two of nothing is normal. Google’s URL Inspection documentation says indexing “typically takes only a day or so, but can take much longer in some cases,” and elsewhere that it “can take up to a week or two.” The {SRC['starter']} is blunter about results: “Some changes might take effect in a few hours, others could take several months.”</p>
<p>For the first 14 days on a new site, set up Search Console, submit the sitemap, request indexing on the homepage and top service pages, and then leave it alone. Really. Stop checking.</p>
<p>Two to four weeks with zero pages indexed means something is blocking Google, so go back through the redesign section. If you’re indexed but have no service rankings after three to six months, you’re past the technical stuff and into content and authority.</p>
<!--fig:pipeline-->
<p>Meanwhile, the phone still needs to ring. If you just launched and the busy season is now (for a lot of Houston trades that means the first 95-degree week in May), a small Google Ads campaign and a well-built Business Profile can cover the months while organic catches up. We’d rather you spend a few hundred dollars a month on tightly targeted ads during that stretch than pay someone to “submit your site to 500 search engines.” Google finds sites through links and sitemaps; nobody needs to submit you anywhere.</p>"""),

            ("Fix it yourself or call someone?", f"""<p>Most of this is DIY. An owner can run the site: search, check the builder toggles, look over the Business Profile and open the Manual actions report in one afternoon.</p>
<p>Pay for help if a migration went badly and you’ve got hundreds of old URLs with no redirect map, or if Search Console shows canonical and duplicate problems across most of the site. Same if you’re indexed and just not competitive. That one is real SEO work, and our {L('/services/web-design-seo-pr/', 'web design and SEO team')} does it for businesses across Montgomery and Harris County.</p>
<p>Your next step today: run <b>site:yourdomain.com</b>, then inspect your homepage in Search Console. Those two checks tell you which half of this guide you need. And if you’re running Google Ads or Meta ads to cover the gap, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where that budget is leaking, in your inbox within 48 hours.</p>"""),
        ],
        "faq": [
            ("Why is my website not showing up on Google?", "Usually because Google hasn't indexed it or because it's indexed but doesn't rank for the searches you tried. Run a site:yourdomain.com search on google.com. No results points to an indexing block such as a noindex tag, a password, or a robots.txt rule. Results without rankings for your services is a competition problem. Search Console's URL Inspection tool tells you which one you have."),
            ("How do I get Google to index my website?", "Verify the site in Google Search Console, submit an XML sitemap, and use URL Inspection on your homepage and main service pages, then click Request indexing. Make sure nothing blocks Google: no noindex tag, no site password, no robots.txt disallow rule. Link your important pages from the homepage. Google says indexing often takes a day or so but can take a week or two."),
            ("Why does my business show up on Google Maps but not my website?", "The map results come mainly from your Google Business Profile, which is separate from your website. A verified profile with the right category can appear in the map pack even if the site isn't indexed or doesn't rank. Check the site with a site: search and Search Console, and make sure the profile links to the matching page on your website."),
            ("How long does it take for a new website to show up on Google?", "A new site often appears for its own name within days to a couple of weeks once Search Console and a sitemap are set up. Ranking for competitive service searches like plumber or roofer in Houston takes much longer, usually months. Google itself says some changes take effect in hours and others take several months, so judge progress over weeks rather than days."),
            ("Can a website redesign make you disappear from Google?", "Yes, and it's one of the most common causes we see. The new site may launch with a staging noindex tag, a robots.txt block, a password page, or canonical tags pointing at the wrong address. Old URLs that aren't redirected also lose their rankings. Check visibility settings, view the page source for noindex, and set up 301 redirects from every old URL."),
        ],
        "figures": {
            "order": {
                "type": "steps",
                "title": "The order we troubleshoot a missing site",
                "sub": "Cheapest, most common causes first",
                "steps": [
                    ["site: search", "Zero results, some pages, or indexed but not ranking."],
                    ["URL Inspection", "Read crawl allowed, page fetch, indexing allowed, canonical."],
                    ["Builder and redesign settings", "Noindex, passwords, robots.txt left from staging."],
                    ["Duplicates and thin pages", "Canonical mistakes and cloned city pages."],
                    ["Business Profile", "Map results run on a separate system."],
                    ["Manual actions and hacks", "Rare, but a thirty-second check."],
                ],
                "alt": "Six-step order for diagnosing why a website is not showing up on Google for Houston and The Woodlands businesses",
                "caption": "Work top to bottom. Most sites are fixed in the first three steps.",
            },
            "launch": {
                "type": "checklist",
                "title": "Launch-day checks after a redesign",
                "sub": "Do these before you celebrate",
                "items": [
                    "WordPress search engine visibility box unchecked",
                    "Wix or Squarespace indexing on, no site password",
                    "No noindex in the homepage source code",
                    "robots.txt has no Disallow: / line",
                    "Canonical tags point to the live domain",
                    "Every old URL 301-redirects to its new match",
                    "New sitemap submitted in Search Console",
                    "Homepage inspected and indexing requested",
                ],
                "alt": "Checklist for keeping a redesigned website showing up on Google after launch for a Spring, TX business",
                "caption": "The most common reason a new site vanishes is a staging setting nobody turned off.",
            },
            "rank": {
                "type": "compare",
                "title": "Not indexed vs indexed but not ranking",
                "left": {"title": "Not indexed", "items": ["site: search shows nothing", "URL Inspection: URL is not on Google", "Usually a setting or error", "Fixed in days once found"]},
                "right": {"title": "Indexed, not ranking", "items": ["Shows up for your business name", "Missing for service searches", "Content, reviews and links problem", "Fixed over months, not days"]},
                "alt": "Comparison of a website not indexed versus indexed but not ranking on Google for a Houston service business",
                "caption": "Figure out which column you’re in before spending a dollar on fixes.",
            },
            "pipeline": {
                "type": "funnel",
                "title": "From published page to ranking page",
                "stages": [["Pages on the site", "40"], ["Discovered by Google", "36"], ["Crawled", "30"], ["Indexed", "22"], ["Ranking on page one for a service", "4"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how website pages move from discovered to indexed to ranking on Google for a Woodlands business",
                "caption": "Every stage loses pages. The Page indexing report shows where yours drop out.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: GA4 form and call tracking
    {
        "slug": "track-form-submissions-phone-calls-ga4-google-ads",
        "title": "How to Track Form Submissions and Phone Calls in GA4 and Google Ads",
        "seo_title": "Track Form Submissions and Phone Calls in GA4",
        "desc": "How to track form submissions and phone calls in GA4 and Google Ads: key events, generate_lead, GTM triggers, call tracking and testing for lead-gen sites.",
        "category": "Paid ads",
        "icons": ["Google Analytics", "Tag Manager", "Google Ads"],
        "art": "b4",
        "hero": "browser",
        "hero_alt": "Illustration of a browser window with a lead form for a guide to tracking form submissions and phone calls in GA4",
        "related": ["call-tracking-which-ads-make-phone-ring", "measure-marketing-success-metrics", "google-ads-not-converting-clicks-no-calls"],
        "sections": [
            (None, f"""<p>GA4 says your site produced two leads last month. Your office manager says the phone rang 70 times and the inbox has 18 form emails. One of those numbers is lying, and it isn’t the office manager.</p>
<p>To track form submissions and phone calls in GA4 reliably, fire one event, <b>generate_lead</b>, only when a form actually succeeds (on a thank-you page or a confirmed success message), mark it as a key event, and count calls using actual call data, since a tap on your phone number proves very little. Then send those same actions to Google Ads so it bids on leads rather than clicks.</p>
<p>That’s the whole idea.</p>
<p>The rest is the plumbing: how to do it on a normal small business site, what breaks, and how to test it without guessing. We set this up for service businesses around The Woodlands and Houston every month, and the same five or six problems show up so reliably we could almost bet on the order.</p>"""),

            ("Conversions are now “key events” in GA4. What changed?", f"""<p>In March 2024 Google renamed GA4’s conversions to <b>key events</b>. As Google’s Ads Liaison put it in {SRC['rename']}, “In GA4, legacy conversions will be renamed to key events.” The word “conversion” now belongs to Google Ads: a key event only becomes a conversion when you share it with an Ads account.</p>
<p>In GA4 you now mark an event as important under <b>Admin → Data display → Events</b> by clicking the star next to it. {SRC['keyev']} says standard properties can have up to 30 key events, which is far more than a lead-gen site needs. We’d keep it to three or four. Old tutorials that tell you to “toggle Mark as conversion” are describing the same switch under its old name, so don’t let them confuse you.</p>
<p>The test for what earns a star is simple. Would you pay for this action? A submitted quote form, sure. A real phone call, absolutely. Someone scrolling 90% of your About page is just someone reading your About page.</p>"""),

            ("Can GA4 track form submissions automatically?", f"""<p>Sort of. GA4’s enhanced measurement has a <b>Form interactions</b> option that sends two events. Per Google’s {SRC['em']}, <b>form_start</b> fires “the first time a user interacts with a form in a session” and <b>form_submit</b> fires “when the user submits a form.” It costs nothing to switch on, and the parameters (form_id, form_name, form_destination, form_submit_text) only show in reports after you register them as custom dimensions.</p>
<p>We don’t use it as a lead count.</p>
<p>Depending on how the form is built, form_submit may fire when someone clicks Submit even if the form then fails validation because the phone number was missing a digit. So it can count attempts. It also misses plenty of real forms: ones that send without a standard browser submit (common with WordPress plugins and page builders) and embedded forms living inside an iframe from another service often don’t register at all. And it happily counts the wrong forms, because your newsletter box and the search bar in your header are forms too.</p>
<p>Leave it on if you like seeing form starts versus finishes. Just don’t mark form_submit as a key event and send it to Google Ads. You’d be training the bidding on noise.</p>"""),

            ("Thank-you page vs event-based form tracking", f"""<p>To know a form actually went through, you need a signal that only appears on success. The table puts the dependable options next to the automatic one above.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Method</th><th>How it works</th><th>Reliability</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Enhanced measurement form_submit</td><td>GA4 guesses from browser form events</td><td>Low; counts attempts, misses many forms</td><td>Rough engagement data only</td></tr>
<tr><td>Thank-you page</td><td>Form redirects to /thank-you/; you track that page view</td><td>High, if nobody can reach the page any other way</td><td>Simple sites; any form plugin that can redirect</td></tr>
<tr><td>Success event (GTM)</td><td>Tag fires on the plugin’s success signal or confirmation message</td><td>High, once tested</td><td>Forms that show an inline “Thanks!” message</td></tr>
<tr><td>Developer dataLayer push</td><td>Site code sends generate_lead after the server accepts the form</td><td>Highest</td><td>Custom sites, booking tools, multi-step quotes</td></tr>
</tbody></table></div>
<p>Thank-you pages are underrated. They’re easy to test and they work with almost every builder. They also give you somewhere to set expectations (“We’ll call within an hour during business hours”), which cuts down on the person who submits the form and then calls twice. Noindex the page so nobody lands on it from Google, and keep it out of your menu, or every curious visitor becomes a “lead.”</p>
<!--fig:methods-->"""),

            ("How to track form submissions in GA4 with Google Tag Manager", f"""<p>If your form shows an inline success message instead of redirecting, Google Tag Manager is the usual tool. The flow for a typical WordPress or Webflow lead form:</p>
<ol><li><b>Find the success signal.</b> Submit a test form and watch what changes. It might be a redirect, a “Thanks, we got it” message appearing, or an event your form plugin pushes to the dataLayer (Gravity Forms, WPForms and Contact Form 7 all have one, sometimes with a helper plugin).</li>
<li>Build the trigger. For a standard HTML form, the <b>Form Submission</b> trigger works. Tick <b>Check Validation</b> so it only fires when the form is “successfully sent,” in the words of {SRC['gtmform']}, and <b>Wait for Tags</b> so the tag fires before the page moves on. For inline messages, an <b>Element Visibility</b> trigger on the confirmation text is often more dependable.</li>
<li>Create a GA4 event tag named <b>generate_lead</b>. Add a parameter like form_name = “quote_request” so you can tell the quote form from the careers form. (Yes, people apply for jobs through the quote form. Constantly.)</li>
<li>Fill out the form in Tag Manager’s Preview mode and confirm the tag fires once, after success. A failed submit should fire nothing.</li>
<li>Publish, then mark the event as a key event in GA4 once it has come through.</li></ol>
<p>Whatever else you rush, submit the form with a mistake on purpose. A tag that fires on the failed attempt will count garbage forever.</p>
<p>For more on what to do with the leads once you count them, our guide to {L('/blog/measure-marketing-success-metrics/', 'measuring marketing success')} covers cost per lead and the numbers worth watching weekly.</p>"""),

            ("Tracking phone calls: a tel: click isn’t a phone call", f"""<p>For a lot of Houston service businesses (plumbers, roofers, HVAC, med spas), calls outnumber forms by a wide margin. They’re also the leads most sites track worst.</p>
<p>The easy version is a Tag Manager <b>Click - Just Links</b> trigger where Click URL starts with <b>tel:</b>, sending a GA4 event like phone_click. That tells you someone tapped the number. Whether they actually called, stayed on the line, or turned out to be your supplier asking about an invoice, it can’t say. Desktop visitors who read the number and dial it from a desk phone never show up at all.</p>
<p>Google Ads is upfront about this. Its {SRC['calls']} lists five ways to count calls: calls from ads (call assets and call-only ads), calls to a Google forwarding number shown on your website, clicks on a number on your mobile website, clicks on call ads and assets, and imported call conversions. On the mobile clicks option, Google’s own words are “we can only track these clicks, not the phone calls themselves.”</p>
<!--fig:calls-->
<p>Start with the cheap part. For calls straight from your ads, set up a call conversion for call assets with a minimum call length; we usually start at 60 seconds, which filters out most wrong numbers and hang-ups. Google’s website call conversion handles the next layer by swapping in a forwarding number for ad visitors, though it only covers Google Ads traffic.</p>
<p>For everything else you need a call tracking service. CallRail, CallTrackingMetrics and WhatConverts are the common ones. With dynamic number insertion, organic, Business Profile, Meta and ad callers each get credited to the right source, and most of these tools can send qualified calls to GA4 and Google Ads. It’s a monthly bill, but for a shop where the phone is the business, we think it pays for itself fast.</p>
<p>Our post on {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking for local businesses')} covers how dynamic numbers work and how to keep them from scrambling your Business Profile’s phone number.</p>"""),

            ("Use the generate_lead event (and the lead events after it)", f"""<p>GA4 has a {SRC['rec']} that includes a set built for lead generation. <b>generate_lead</b> is the one you’ll use first; Google describes it as when a user “submits a form online or submits information offline.” The rest of the set covers what happens after:</p>
<ul><li><b>qualify_lead</b> and <b>disqualify_lead</b>, for when someone on your team decides a lead is real or junk</li>
<li><b>working_lead</b>, when a rep makes contact</li>
<li><b>close_convert_lead</b> and <b>close_unconvert_lead</b>, for won and lost</li></ul>
<p>Use Google’s names even if “quote_form_success_v2” feels more descriptive. Recommended events slot into GA4’s reports and future features without extra setup, and whoever inherits your account later will know what they mean without calling you.</p>
<p>The later events matter more than most owners realize. A roofing company in Kingwood might get 40 form fills in a hail month, and half are price shoppers from outside the service area. If your CRM can send qualify_lead or close_convert_lead back (most can, through an integration or a CSV upload), Google Ads can learn which clicks became roofs. That’s also what enhanced conversions for leads is for on the Ads side.</p>
<p>Add a value to generate_lead if you can, even a rough one. A $90 drain cleaning lead and a $12,000 repipe lead shouldn’t look identical.</p>"""),

            ("Import GA4 key events into Google Ads, or use Google Ads conversions?", f"""<p>You can do either, and plenty of accounts do both. {SRC['import']} lists the differences that matter:</p>
<ul><li>GA4 can credit any channel. Google Ads conversion tracking only measures Google Ads.</li>
<li>Google Ads records the conversion on the click date, while GA4 records it on the day it happened. That alone explains a lot of “why don’t these numbers match” emails.</li>
<li>Imported conversions can take up to 24 hours to show in Google Ads.</li>
<li>Conversions created from GA4 come in as <b>Secondary</b>, so they won’t steer bidding until you change that.</li></ul>
<p>Our default for a local lead-gen account: native Google Ads conversion tracking (through the Google tag or Tag Manager) for forms, Google’s call conversions for calls, both set as <b>Primary</b>. GA4 key events stay in GA4 for cross-channel reporting and get imported as Secondary, if at all.</p>
<!--fig:source-->
<p>What you don’t want is two Primary actions for the same lead, say a Google Ads form tag and an imported GA4 generate_lead. Every quote request counts twice. Your cost per lead looks like half of what it really is, and smart bidding happily overpays for the next one. If your Google Ads results look too good to be true, check this before you celebrate, and see our {L('/blog/google-ads-not-converting-clicks-no-calls/', 'Google Ads not converting audit')} for the other tracking failures.</p>
<p>Either way, auto-tagging has to be on, and nothing on your site can strip the gclid off the URL.</p>
<p>Redirect plugins and some booking tools do exactly that, silently, and you won’t find out until someone asks why Ads shows zero conversions for a month the phones were busy.</p>"""),

            ("Consent mode basics for a Texas business", f"""<p>Consent mode lets your Google tags adjust to what a visitor agreed to. The {SRC['consent']} lists four signals: <b>ad_storage</b>, <b>analytics_storage</b>, <b>ad_user_data</b> and <b>ad_personalization</b>.</p>
<p>It comes in two flavors. <b>Basic</b> blocks Google tags entirely until someone answers a cookie banner, and if they decline, nothing is sent. <b>Advanced</b> loads tags with consent denied by default and sends cookieless pings, which Google uses to model conversions it can’t observe.</p>
<p>For most Houston-area businesses selling to Texans, consent mode is a lower priority than getting the events right. Google’s strictest consent requirements are aimed at visitors in Europe. Texas has its own law, the Texas Data Privacy and Security Act, in effect since July 1, 2024, but according to the {SRC['tdpsa']}, small businesses as defined by the SBA are “generally exempt,” apart from a consent rule for selling sensitive data. If you already run a cookie banner (many WordPress themes add one), make sure it’s wired to consent mode rather than silently blocking every tag. We’ve seen banners that zeroed out a client’s conversions for months.</p>
<p>We’re not lawyers. If you handle health information (a clinic or med spa), talk to one before putting any tracking on booking or intake pages.</p>"""),

            ("Test it with DebugView and Tag Assistant", f"""<p>Never trust a tracking setup you haven’t broken on purpose. We run the same routine on every account we touch, and it’s quicker than it looks.</p>
<ol><li>Open <b>tagassistant.google.com</b>, enter your site, and connect. Per Google’s {SRC['debug']}, Tag Assistant adds a parameter that turns on debug mode for your device only.</li>
<li>In GA4, go to <b>Admin → Data display → DebugView</b>. Your device appears and events stream in as they happen.</li>
<li>Submit the form with an error. Nothing should fire.</li>
<li>Submit it properly. Exactly one generate_lead should appear, with your form_name parameter.</li>
<li>Tap the phone number on your phone. Your click event should appear.</li>
<li>Back in Google Ads, check <b>Goals → Summary</b> and confirm each Primary action shows as active after a day or so.</li>
<li>Call your own call asset from a mobile phone and stay on longer than your minimum call length.</li></ol>
<!--fig:test-->
<p>After that, once a month, compare GA4’s generate_lead count with the form emails in your inbox, and your call conversions with your call log. Within 10 to 15% is healthy. Off by half means something broke, usually after a plugin update or a site edit.</p>"""),

            ("When to do this yourself and when to hand it off", f"""<p>A single contact form with a thank-you page is a one-hour DIY job. Redirect, track the page, mark the key event, test. Call assets in Google Ads are about the same.</p>
<p>It gets messier fast once you add a second form, an embedded booking tool or another location. Cross-channel call tracking and CRM data flowing back into Google Ads are where most owners (reasonably) tap out. That’s the kind of setup our {L('/services/search-marketing/', 'Google Ads team')} builds and maintains for businesses from Katy to Conroe.</p>
<p>Your next step: submit your own contact form today and see if GA4 notices. If you’re running ads and aren’t sure the numbers in your account are real, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your Google or Meta budget is leaking, tracking included, in your inbox within 48 hours.</p>"""),
        ],
        "faq": [
            ("How do I track form submissions in GA4?", "The reliable way is to fire a generate_lead event only when the form succeeds, either by tracking a thank-you page view or by using Google Tag Manager to catch the form's success message or dataLayer event. Then mark generate_lead as a key event under Admin, Data display, Events. Avoid relying on enhanced measurement's form_submit, which can count failed attempts and miss embedded forms."),
            ("What is the difference between key events and conversions in GA4?", "In March 2024 Google renamed GA4 conversions to key events. A key event is an action you mark as important in Google Analytics. It becomes a conversion only when you share it with Google Ads, where it can be used for bidding and reporting. Standard GA4 properties allow up to 30 key events, though most lead-gen sites only need three or four."),
            ("Can GA4 track phone calls?", "GA4 can track clicks on a tel: link, usually with a Google Tag Manager click trigger, but a click is not a completed call. To count real calls, use Google Ads call conversions for call assets and website forwarding numbers, or a call tracking service with dynamic number insertion that sends qualified calls to GA4 and Google Ads, ideally with a minimum call length."),
            ("Should I import GA4 conversions into Google Ads?", "You can, but for local lead generation we usually make Google Ads' own form and call conversions the Primary actions and keep GA4 imports as Secondary. Native tracking credits the click date and only Google Ads clicks, while GA4 imports can take up to 24 hours. Never set two Primary actions for the same lead, or each lead is counted twice."),
            ("How do I test if my GA4 event is working?", "Connect your site in Google Tag Assistant, which turns on debug mode for your device, then open Admin, Data display, DebugView in GA4. Submit your form once with an error and once correctly. Only the successful submission should fire generate_lead. For Google Ads, check the conversion action status under Goals and Summary after about a day."),
        ],
        "figures": {
            "methods": {
                "type": "steps",
                "title": "Our form tracking setup order",
                "sub": "From a plain contact form to bid-ready leads",
                "steps": [
                    ["Find the success signal", "Redirect, confirmation message or plugin dataLayer event."],
                    ["Fire generate_lead", "Only on success, with a form_name parameter."],
                    ["Mark it as a key event", "Admin, Data display, Events, star it."],
                    ["Send it to Google Ads", "Native tag as Primary, or a GA4 import."],
                    ["Test, then audit monthly", "DebugView, Tag Assistant, inbox comparison."],
                ],
                "alt": "Five steps to track form submissions in GA4 and Google Ads for a Houston lead generation website",
                "caption": "Skipping the first step is why most GA4 lead counts are wrong.",
            },
            "calls": {
                "type": "bars",
                "title": "What “phone leads” can mean",
                "sub": "One month on a Houston service site",
                "items": [["Taps on the tel: link", 100, "100"], ["Calls that connected", 64, "64"], ["Calls over 60 seconds", 43, "43"], ["New customers booked", 19, "19"]],
                "highlight": [3],
                "note": "Illustrative example",
                "alt": "Bar chart comparing phone link taps with real calls and booked customers when tracking phone calls in GA4",
                "caption": "Tracking only the first bar overstates phone leads by a wide margin.",
            },
            "source": {
                "type": "compare",
                "title": "GA4 import vs native Google Ads tracking",
                "left": {"title": "Imported GA4 key event", "items": ["Credits the conversion date", "Can take up to 24 hours", "Arrives as Secondary", "Counts every channel in GA4"]},
                "right": {"title": "Google Ads conversion", "items": ["Credits the ad click date", "Built for bidding", "Works with call conversions", "Only measures Google Ads"]},
                "alt": "Comparison of importing GA4 key events versus native Google Ads conversion tracking for a Woodlands business",
                "caption": "Differences per Google’s import documentation. Pick one Primary source per lead.",
            },
            "test": {
                "type": "checklist",
                "title": "Lead tracking checklist",
                "sub": "Run it after every site update",
                "items": [
                    "Failed form submit fires nothing",
                    "Successful submit fires one generate_lead",
                    "Thank-you page is noindexed and not in the menu",
                    "tel: taps tracked as a separate event",
                    "Call assets counted with a minimum call length",
                    "Only one Primary action per lead type in Ads",
                    "Auto-tagging on and gclid survives redirects",
                    "GA4 leads within 15% of the inbox count",
                ],
                "alt": "Checklist for testing form and phone call tracking in GA4 and Google Ads for Houston service businesses",
                "caption": "Ten minutes a month keeps your lead numbers honest.",
            },
        },
    },
]
