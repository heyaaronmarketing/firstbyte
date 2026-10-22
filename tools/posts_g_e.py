"""Batch 7 (agency intent): multi-location local SEO for franchises and chains, and YouTube ads for local businesses.

Research: Google Business Profile help on bulk verification (#4490296), business groups (#6085326), store codes (#4542487),
guidelines for representing your business (#3038177), local ranking (#7091) and review replies (#3474050); Google Maps
user-contributed content policy on fake engagement (#7400114); Google Search spam policies (doorway abuse); Google Search
Central LocalBusiness structured data docs; schema.org parentOrganization (supersedes branchOf); GA4 UTM help (#10917952);
Google Ads location assets (#2404182) and location targeting (#1722043). YouTube: Google Ads video ad formats (#2375464),
Video views campaigns (#13982458), Video Action -> Demand Gen upgrade (#15110871), Discovery -> Demand Gen (#13859703),
Demand Gen low-budget guidance (#14718973), Shorts ads guide (#16041697), engaged-view conversions (#10048752),
view-through conversions (#6270625), Brand Lift (#9049825), YouTube data segments (#2545661), Customer Match policy
(#6299717), Google's ABCD reference guide, Nielsen Media Distributor Gauge (April 2025) and Advanced Television on the
May 2026 Gauge, WebFX survey on YouTube cost per view.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "bulk": A("https://support.google.com/business/answer/4490296?hl=en", "bulk verification rules"),
    "groups": A("https://support.google.com/business/answer/6085326?hl=en", "business groups"),
    "codes": A("https://support.google.com/business/answer/4542487?hl=en", "store code help page"),
    "guide": A("https://support.google.com/business/answer/3038177?hl=en", "guidelines for representing your business"),
    "rank": A("https://support.google.com/business/answer/7091?hl=en", "explanation of local ranking"),
    "reply": A("https://support.google.com/business/answer/3474050?hl=en", "review reply help page"),
    "fake": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "fake engagement policy"),
    "doorway": A("https://developers.google.com/search/docs/essentials/spam-policies", "spam policies"),
    "lb": A("https://developers.google.com/search/docs/appearance/structured-data/local-business", "LocalBusiness structured data documentation"),
    "parent": A("https://schema.org/parentOrganization", "schema.org"),
    "utm": A("https://support.google.com/analytics/answer/10917952?hl=en", "Google Analytics UTM help"),
    "locassets": A("https://support.google.com/google-ads/answer/2404182?hl=en", "location assets"),
    # YouTube
    "formats": A("https://support.google.com/google-ads/answer/2375464?hl=en", "video ad formats page"),
    "views": A("https://support.google.com/google-ads/answer/13982458?hl=en", "Video views campaigns"),
    "vac": A("https://support.google.com/google-ads/answer/15110871?hl=en", "upgrade notice"),
    "disc": A("https://support.google.com/google-ads/answer/13859703", "Discovery upgrade page"),
    "dgbudget": A("https://support.google.com/google-ads/answer/14718973", "Demand Gen budget guidance"),
    "shorts": A("https://support.google.com/google-ads/answer/16041697?hl=en", "Shorts ads guide"),
    "evc": A("https://support.google.com/google-ads/answer/10048752?hl=en", "engaged-view conversions"),
    "vtc": A("https://support.google.com/google-ads/answer/6270625?hl=en", "view-through conversions"),
    "lift": A("https://support.google.com/google-ads/answer/9049825", "Brand Lift"),
    "segments": A("https://support.google.com/google-ads/answer/2545661?hl=en", "YouTube data segments"),
    "cm": A("https://support.google.com/adspolicy/answer/6299717?hl=en", "Customer Match policy"),
    "geo": A("https://support.google.com/google-ads/answer/1722043", "location targeting help"),
    "abcd": A("https://services.google.com/fh/files/misc/youtube_google_abcd_reference_guide_en.pdf", "ABCD reference guide"),
    "nielsen": A("https://www.nielsen.com/news-center/2025/youtube-maintains-largest-share-of-tv-viewing-among-media-companies-for-third-consecutive-month/", "Nielsen"),
    "advtv": A("https://www.advanced-television.com/2026/07/29/nielsen-youtube-takes-13-8-of-us-tv-watch-time-in-may/", "Advanced Television’s report on Nielsen’s May 2026 Gauge"),
    "webfx": A("https://www.webfx.com/internet-marketing/how-much-does-youtube-advertising-cost.html", "WebFX’s survey of 270 marketers"),
}

ML = "/blog/multi-location-local-seo-houston-franchises/"
YT = "/blog/youtube-ads-cost-local-business-houston/"

POSTS = [
    # ------------------------------------------------------------------ post 1: multi-location local SEO
    {
        "slug": "multi-location-local-seo-houston-franchises",
        "title": "Multi-Location Local SEO for Houston Franchises and Chains",
        "seo_title": "Multi-Location Local SEO for Houston Franchises",
        "desc": "Multi-location local SEO for Houston franchises and chains with 2-50 locations: Business Profile setup, location pages, schema, reviews and tracking.",
        "category": "SEO & AI search",
        "icons": ["Google Business Profile", "Google", "Google Ads"],
        "art": "b2",
        "hero": "pins",
        "hero_alt": "Illustration of several map pins on a grid for a guide to multi-location local SEO in Houston",
        "related": ["power-of-local-landing-pages", "rank-in-google-map-pack-houston", "google-business-profile-number-one-asset"],
        "sections": [
            (None, f"""<p>You have six locations, Kingwood to Katy. You search your own brand from the parking lot of the Cypress store and Google shows you the Tomball one. One profile still lists a suite you moved out of two years ago. Another sends calls to a corporate line that rings out after 5 p.m.</p>
<p>Most multi-location local SEO work starts with a mess like that. Every real location needs its own verified Google Business Profile and its own page on your site. Name, address and phone should match everywhere. Add schema per page, handle reviews store by store, and track which location the calls came from.</p>
<p>Google ranks each location on its own. A strong brand doesn’t carry a neglected listing.</p>
<p>This is for owners running 2 to 50 locations around Greater Houston: franchisees, regional chains, multi-office practices, home service companies with shops in Conroe and Pearland. It’s the order we work in, and you can do most of it without us.</p>"""),
            ("How does local SEO work when you have multiple locations?", f"""<p>Google’s own {SRC['rank']} names three factors: relevance, distance and prominence. The second one is the reason a chain can’t treat local SEO as a brand-level project. Distance is measured from the person searching to each individual location. Your Katy store has no chance in a Kingwood search, and it shouldn’t.</p>
<p>What you actually have is six (or twenty) small local SEO programs sharing a brand and a website. The Sugar Land store might face two national chains; the Magnolia store might face one guy with 400 reviews who has owned that market since 2009.</p>
<!--fig:footprint-->
<p>It’s also why chains often lose to single-location shops. The independent in Spring has one owner answering every review; the chain has a profile nobody at corporate looks at. Prominence is earned per location, and only real, staffed locations qualify for a profile at all. For how a single profile climbs, see <a href="/blog/rank-in-google-map-pack-houston/">how to rank in the Google map pack in Houston</a>.</p>"""),
            ("Google Business Profile for multiple locations: groups, bulk verification and store codes", f"""<h3>Business groups</h3>
<p>Google’s {SRC['groups']} let you add owners or managers to a whole set of profiles at once (the option appears at two or more). Anyone added gets every current and future profile in the group, which is convenient until your Katy manager can edit the Pearland hours. We split groups by region or franchisee, and since each group needs its own bulk spreadsheet, plan that split before uploading anything.</p>
<h3>Bulk verification (10 or more locations)</h3>
<p>Under Google’s {SRC['bulk']}, you can request chain verification once your account holds 10 or more eligible profiles for the same business. Duplicates and suspended profiles don’t count toward the 10. You do it in Business Profile Manager on a computer: <b>Verifications</b>, then <b>Chain</b>, then <b>Start</b>, and fill in the form. A few details catch people:</p>
<ul><li>Service-area businesses aren’t eligible.</li>
<li>Agencies holding several different businesses in one account can’t bulk verify; the brand does it from its own account.</li>
<li>Google may still ask for video verification at a location.</li>
<li>No timeline is given. Don’t schedule a grand opening around it.</li></ul>
<p>Under 10 locations, you verify one at a time. It’s tedious work, though none of it is hard. Our <a href="/blog/google-business-profile-video-verification/">video verification walkthrough</a> covers the tricky part.</p>
<h3>Store codes</h3>
<p>Every location in a bulk spreadsheet needs a unique store code. Google’s {SRC['codes']} says any identifier works as long as it never changes for that location: “HOU-KATY-01” or just “114”. The warning on that page is worth reading twice. If you add or change a store code on an existing location through a spreadsheet upload, Google creates a duplicate location. Change codes in Business Profile Manager under Advanced settings, and use spreadsheets only for new locations.</p>
<h3>Names and categories</h3>
<p>Google’s {SRC['guide']} require all locations in the same country to use the same name, unless a location consistently uses a different name on its signage and website. Store codes and city names don’t belong in the business name; Google’s own example says “The UPS Store - 2872” is not acceptable. Adding “Katy” to the name because it might help rankings is a common route to a suspension. All locations should also share the one primary category that best fits the business.</p>
<h3>Practitioners, departments and shared addresses</h3>
<p>Practitioners (doctors, dentists, lawyers, agents) can have their own profiles if they’re public-facing and reachable at the location. Support staff can’t, and one practitioner shouldn’t have a profile per specialty. Departments that operate as distinct public entities, like a dealership’s service center, can get their own profile and hours; a counter inside a bigger store doesn’t qualify.</p>
<p>Otherwise it’s one profile per location. Two brands under one roof get separate profiles only if they operate independently.</p>
<!--fig:setup-->"""),
            ("Keeping NAP consistent across every location", f"""<p>NAP is name, address, phone. With 15 locations, the problems are rarely in Google. They live in the Yelp listing a former manager claimed, or the Apple Maps pin still sitting on the old strip center on FM 1960.</p>
<p>Build one master location record and update everything from it. Never the other way around.</p>
<div class="bp-tbl"><table><thead><tr><th>Field</th><th>Example</th><th>Rule we follow</th></tr></thead><tbody>
<tr><td>Store code</td><td>HOU-SPR-03</td><td>Never changes, even if the store moves down the street</td></tr>
<tr><td>Business name</td><td>Brand name only</td><td>Identical at every location, no city or keywords added</td></tr>
<tr><td>Address</td><td>Street, suite, city, ZIP</td><td>Written the same way everywhere (pick “Suite” or “Ste” once)</td></tr>
<tr><td>Primary phone</td><td>Local number for that store</td><td>Rings at that location, not a central line, during business hours</td></tr>
<tr><td>Website URL</td><td>/locations/spring/</td><td>That location’s page, never the homepage</td></tr>
<tr><td>Hours and holiday hours</td><td>Mon to Sat 8 to 6</td><td>Updated before every holiday and every hurricane closure</td></tr>
<tr><td>Primary category</td><td>Same for all</td><td>Matches the brand; secondary categories can vary by what the store offers</td></tr>
</tbody></table></div>
<p>Check, roughly in order: Business Profile, your location pages, Apple Business Connect, Bing Places, Facebook, Yelp, and your industry’s big directory (Healthgrades, Avvo, Houzz). We skip 80-directory syndication packages for most clients. The first eight or ten listings do nearly all the work; the rest mostly generate invoices.</p>
<p>On call tracking, the usual practice is a tracking number per store as the profile’s primary phone, with the real local number kept as an additional phone. Never a different tracking number on every directory; that’s 40 numbers for one store and a confused Google.</p>
<p>When a store closes, mark it permanently closed instead of deleting it. When one moves, read <a href="/blog/change-business-address-google-without-suspension/">changing a business address without a suspension</a> first. Moves are the most common way we see chain profiles get flagged.</p>"""),
            ("Location pages SEO: one page per profile, without building doorway pages", f"""<p>Every Business Profile should link to its own page on your site, not the homepage or a bare store locator.</p>
<p>The risk is the shortcut. Google’s {SRC['doorway']} list “having multiple domain names or pages targeted at specific regions or cities that funnel users to one page” and “creating substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy” as doorway abuse. Twelve location pages where only the city name changes is that, more or less word for word.</p>
<!--fig:pages-->
<p>A location page earns its keep with boring, specific details that only someone who works there would know.</p>
<ul><li>The manager and staff, with real photos and a sentence each.</li>
<li>Directions that help: which side of the road, where to park, “the turn-in off Kuykendahl comes up fast if you’re heading north.”</li>
<li>Which services this store does and doesn’t offer. Chains almost always have some variation, and hiding it costs you angry reviews.</li>
<li>Holiday hours, and what happens during a hurricane or freeze closure.</li>
<li>Reviews and a few photos from this location, not a brand-wide carousel.</li>
<li>A few FAQs this store actually gets (parking at Market Street on a Saturday is its own question).</li></ul>
<p>Write them one at a time, with 20 minutes of input from each store manager. Slow going, and most competitors skip it.</p>
<p>City pages where you have no store are a separate question. A page or two for areas your Spring store genuinely serves can be legitimate. Forty pages for every suburb within 60 miles is a doorway problem waiting for a core update. More in <a href="/blog/power-of-local-landing-pages/">the power of local landing pages</a>.</p>"""),
            ("LocalBusiness schema for each location (and where department and branchOf fit)", f"""<p>Schema won’t rank a weak location, but it removes ambiguity about which store is which. Google’s {SRC['lb']} says to define each location as its own LocalBusiness (<b>name</b> and <b>address</b> required). Put each block on that location’s page, not 15 blocks on the homepage, and include <b>geo</b> and opening hours.</p>
<div class="bp-tbl"><table><thead><tr><th>Property</th><th>What to put there</th><th>Multi-location note</th></tr></thead><tbody>
<tr><td>@type</td><td>The most specific type that fits (Dentist, Plumber, Restaurant, AutoRepair)</td><td>Same type across locations unless a store is genuinely different</td></tr>
<tr><td>name, address, telephone</td><td>Exactly what’s in the master record</td><td>Must match the Business Profile character for character</td></tr>
<tr><td>url</td><td>The location page</td><td>The same URL the profile’s website link uses (minus UTM tags)</td></tr>
<tr><td>parentOrganization</td><td>Reference to the brand’s Organization @id</td><td>Ties every store to one brand entity</td></tr>
<tr><td>department</td><td>Nested LocalBusiness for distinct departments</td><td>Only for real departments, like a pharmacy or service center</td></tr>
</tbody></table></div>
<p>Older tutorials still use <b>branchOf</b>. According to {SRC['parent']}, <b>parentOrganization</b> supersedes it. For departments, Google’s example pairs the store name with the department (“gMart” and “gMart Pharmacy”) unless the department has its own brand.</p>
<p>One expectation to reset: Google recommends <b>aggregateRating</b> only for sites that collect reviews about other businesses, so marking up your own testimonials won’t earn stars. Spot-check a few pages in the Rich Results Test after any template change, which is when markup quietly breaks.</p>"""),
            ("Franchise local SEO: who should own the Google Business Profile?", f"""<p>This one causes real fights, usually when a franchisee sells and nobody can say who owns the profile with 600 reviews.</p>
<p>Your franchise agreement may already decide it, so read its marketing and digital assets sections first. The common models:</p>
<div class="bp-tbl"><table><thead><tr><th>Model</th><th>Who owns the profile</th><th>Works well when</th><th>Where it breaks</th></tr></thead><tbody>
<tr><td>Brand controlled</td><td>Franchisor, franchisee has no access</td><td>Large systems with a central marketing team</td><td>Reviews go unanswered, photos are stock, local hours drift</td></tr>
<tr><td>Franchisee controlled</td><td>Each franchisee, brand has no access</td><td>Very small systems or loose licensing deals</td><td>Inconsistent names and categories, profiles lost when owners exit</td></tr>
<tr><td>Hybrid (our usual pick)</td><td>Brand is owner; franchisee is manager</td><td>Most 2 to 50 location systems</td><td>Needs a written rule on who edits what</td></tr>
</tbody></table></div>
<p>In the hybrid model the brand controls what should be identical (name, primary category, website URL) and the franchisee handles what only they do well: review replies, real photos, hours. One wrinkle catches people. When a business group bulk verifies through its main owner, Google says no one else can own those profiles, so if the brand bulk verifies, franchisees become managers by design. Decide that on purpose.</p>
<p>Then there’s the franchisee who builds a separate territory website (sometimes with a nephew’s help) that competes with the brand’s location page. Let franchisees add local content to their page on the main site and most will happily drop it.</p>"""),
            ("Review management at scale: asking and replying per location", f"""<p>One store has 900 reviews and a manager who replies to every one. The store 20 minutes away has 41, and the last reply is from 2022. Customers notice, and so does the map pack.</p>
<p>Start with what you can’t do. Google’s {SRC['fake']} bans discouraging negative reviews, selectively asking only happy customers, incentives, and pressuring people while they’re still on the premises. A “rate us 1 to 5, and fives go to Google” flow is selective solicitation, and we see it in franchise review software all the time. (The FTC has rules too; see <a href="/blog/fake-reviews-rule-local-businesses/">the fake reviews rule</a>.)</p>
<p>At scale, this is the routine we set up:</p>
<ol><li>Give every location its own review link and QR code from its own profile. Brand-wide links that land on the wrong store are common.</li>
<li>Ask every customer the same way, at the same moment. A text after the job beats a card at the counter.</li>
<li>Local managers reply within two business days. Corporate takes legal threats, injuries and press.</li>
<li>Mention something real from the review. Thirty stores posting “Thanks for your feedback!” reads as nobody listening.</li>
<li>Track monthly per store: new reviews, rating, reply rate, oldest unanswered review.</li></ol>
<p>Per Google’s {SRC['reply']}, replies are checked before they appear (usually within 10 minutes, sometimes up to 30 days) and show as the business, not the person. Basics on getting reviews are in our <a href="/blog/complete-guide-google-reviews/">complete guide to Google reviews</a>.</p>"""),
            ("Tracking each location: UTM tags, calls and Business Profile performance", f"""<p>Most chains we audit know total leads and nothing about which store produced them.</p>
<p>Start with UTM tags on every profile’s website link. Without them, profile clicks blend into organic search in Google Analytics. Tag each profile’s link with something like <i>?utm_source=google&amp;utm_medium=organic&amp;utm_campaign=gbp&amp;utm_content=spring</i>. Google’s {SRC['utm']} recommends always including source, medium and campaign, and warns that values are case-sensitive: “Spring” and “spring” become two rows in your report. Pick lowercase and stick to it. In GA4, the Traffic acquisition report then splits profile traffic by store.</p>
<p>Calls come next. For most local businesses the call is the conversion that matters, and a tracking number per store shows which location’s calls are growing.</p>
<p>Each profile also reports its own calls, direction requests and clicks. Pair that with a grid rank tracker, because rankings around Hughes Landing can look nothing like rankings near Waterway Square.</p>
<!--fig:monthly-->
<p>Keep one sheet, a row per location, refreshed monthly. Within a quarter the weak stores stand out, usually for a fixable reason like a missing location page or a manager who never asks for reviews.</p>"""),
            ("Google Ads location assets for multi-location businesses", f"""<p>Link your Business Profiles to Google Ads and you get {SRC['locassets']}: the nearest store’s address, distance and call button alongside your ads. The data comes from Business Profile and Maps, so a wrong profile address becomes a wrong ad address.</p>
<p>Set it up in <b>Tools</b>, <b>Shared library</b>, <b>Location manager</b>. For chains:</p>
<ul><li>Location groups let each campaign use only the stores it’s about.</li>
<li>Campaign-level settings override account-level ones, so remove the broad account-level asset if you manage locations per campaign.</li>
<li>Video ads show locations by default unless you opt out.</li>
<li>Removing all locations also removes location-based targeting, bidding and store visit tracking. Don’t switch it off to tidy up.</li></ul>
<p>Match targeting to each store’s real trade area. A Conroe campaign that also targets The Woodlands competes with your own Woodlands store. We set a radius per store and add negative locations where stores sit close together; our <a href="/services/search-marketing/">Google Ads management</a> for chains usually starts with that cleanup.</p>"""),
            ("A multi-location local SEO audit you can run this week", f"""<p>Score each location 0 to 2 per line, one column per store. Anything under 11 out of 18 gets your time first.</p>
<div class="bp-tbl"><table><thead><tr><th>Check</th><th>0 points</th><th>2 points</th></tr></thead><tbody>
<tr><td>Profile verified and owned by the brand account</td><td>Unverified or owned by an ex-employee</td><td>Verified, in the right business group</td></tr>
<tr><td>Name and primary category</td><td>Keywords or city added, category differs</td><td>Brand name only, shared primary category</td></tr>
<tr><td>Website link</td><td>Points to homepage</td><td>Points to a tagged location page</td></tr>
<tr><td>Location page</td><td>City-swap template</td><td>Staff, directions, services, local FAQs</td></tr>
<tr><td>Schema on location page</td><td>None, or homepage only</td><td>LocalBusiness with parentOrganization</td></tr>
<tr><td>NAP on top directories</td><td>Two or more mismatches</td><td>All match the master record</td></tr>
<tr><td>Reviews in last 90 days</td><td>Fewer than 5</td><td>Steady, at least weekly</td></tr>
<tr><td>Review replies</td><td>Unanswered reviews older than a month</td><td>Replies within a few days, specific</td></tr>
<tr><td>Tracking</td><td>No UTM, no call tracking</td><td>Both, reported monthly</td></tr>
</tbody></table></div>
<p>Can you do this in-house? Under five locations, with someone who has four hours a week, yes. Past ten, or once franchisees are involved, the job turns into governance (who owns what, who updates hours during a storm), and outside help tends to pay off there. It’s part of our <a href="/services/web-design-seo-pr/">SEO and web work</a>, and we’ll say so if a store manager with a checklist would do the job.</p>
<p>If you also run Google or Meta ads across those stores, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where that budget leaks, overlapping store radiuses included, in your inbox within 48 hours. For the profile side, start with <a href="/blog/google-business-profile-number-one-asset/">why your Business Profile is your number one asset</a>, then score your weakest store.</p>"""),
        ],
        "faq": [
            ("How do I manage Google Business Profiles for multiple locations?",
             "Put every location in one Business Profile account, organized into business groups by brand or region, with a unique store code for each location. Keep the brand as owner and add local managers only to their own stores. Use a master spreadsheet for name, address, phone, hours and website link, and update profiles from it so details stay identical everywhere."),
            ("How many locations do you need for Google bulk verification?",
             "Google's bulk verification requires 10 or more eligible profiles for the same business in one account. Duplicates, suspended and disabled profiles don't count. Service-area businesses aren't eligible, and agencies holding several different businesses in one account can't use it. With fewer than 10 locations, each profile is verified individually, sometimes by video."),
            ("Do I need a separate page on my website for each location?",
             "Yes. Each Business Profile should link to its own location page, not the homepage. The page needs content specific to that store, such as staff, directions, parking, services offered, hours and local reviews. Pages that only swap the city name can look like doorway pages under Google's spam policies, so write each one individually."),
            ("Should a franchisee or the franchisor own the Google Business Profile?",
             "Check your franchise agreement first. In most systems of 2 to 50 locations we prefer the brand as owner and the franchisee as manager. The brand protects the name, category and website link, while the franchisee replies to reviews, adds photos and keeps hours current. It also keeps the profile and its reviews with the location if a franchisee exits."),
            ("Can I add the city name to my business name on Google for each location?",
             "Usually not. Google's guidelines require all locations in the same country to share one name, unless a store consistently uses a different name on its signage and website. Adding a city, store number or keywords to the name is not allowed and can lead to suspension. Put the city in your location page and categories instead."),
        ],
        "figures": {
            "footprint": {
                "type": "map",
                "title": "Each store competes in its own map pack",
                "sub": "A hypothetical seven-location Houston-area brand",
                "highlight": ["Katy", "Cypress", "Tomball", "The Woodlands", "Kingwood", "Sugar Land", "Pearland"],
                "alt": "Map of a hypothetical seven-location brand around Houston, showing multi-location local SEO competition by area",
                "caption": f"Distance is one of Google’s three local ranking factors, per its {A('https://support.google.com/business/answer/7091?hl=en', 'local ranking explainer')}.",
            },
            "setup": {
                "type": "steps",
                "title": "Setting up profiles for a multi-location brand",
                "sub": "The order we use for 2 to 50 locations",
                "steps": [
                    ["Build the master record", "One row per real location with store code, NAP, hours, URL and manager."],
                    ["Create business groups", "Split by brand, region or franchisee so managers only see their stores."],
                    ["Verify every location", "Bulk verification at 10+ eligible profiles; otherwise one at a time."],
                    ["Fix names and categories", "Brand name only, one shared primary category, no city or store numbers."],
                    ["Link location pages", "Each profile’s website link goes to its own tagged location page."],
                    ["Assign review owners", "Each store manager replies within two business days; corporate handles escalations."],
                ],
                "alt": "Six steps for setting up Google Business Profiles in a multi-location local SEO program for Houston brands",
                "caption": f"Bulk verification rules from Google’s {A('https://support.google.com/business/answer/4490296?hl=en', 'Business Profile help')}.",
            },
            "pages": {
                "type": "compare",
                "title": "Location pages: doorway vs. useful",
                "left": {"title": "City-swap template", "items": ["Same copy, new city name", "Stock photos on every page", "No staff, no directions", "Brand-wide reviews carousel", "Links to a generic contact form"]},
                "right": {"title": "A real location page", "items": ["Manager and team with photos", "Parking and turn-in directions", "Services this store offers", "Reviews from this location", "Local phone and hours"]},
                "alt": "Comparison of a templated doorway page and a useful location page for multi-location local SEO in Houston",
                "caption": f"Google lists near-identical city pages as doorway abuse in its {A('https://developers.google.com/search/docs/essentials/spam-policies', 'spam policies')}.",
            },
            "monthly": {
                "type": "checklist",
                "title": "Monthly per-location check",
                "sub": "One row per store, same checks every month",
                "items": [
                    "Hours and holiday hours correct",
                    "New reviews this month, and all replied to",
                    "Calls from the profile vs. last month",
                    "Website clicks by UTM content (store)",
                    "Map rank grid around the store",
                    "New photos added by the store team",
                    "No unexpected edits or duplicate listings",
                    "Location page still live with correct NAP",
                ],
                "alt": "Checklist of monthly checks for each store in a multi-location local SEO program around Houston and The Woodlands",
                "caption": "Ten minutes per location per month catches most problems before they cost rankings.",
            },
        },
    },
    # ------------------------------------------------------------------ post 2: YouTube ads
    {
        "slug": "youtube-ads-cost-local-business-houston",
        "title": "YouTube Ads Cost for Local Businesses in Houston: Formats That Work",
        "seo_title": "YouTube Ads Cost for Local Businesses in Houston",
        "desc": "What YouTube ads cost a local business in Houston and The Woodlands, which formats work, how to target by ZIP code, and how to tell if they’re working.",
        "category": "Paid ads",
        "icons": ["YouTube", "Google Ads", "Google Analytics"],
        "art": "b5",
        "hero": "play",
        "hero_alt": "Illustration of a video player with a play button for a guide to YouTube ads cost for local businesses in Houston",
        "related": ["streaming-tv-ads-worth-it-small-business", "retargeting-explained", "radio-tv-advertising-cost-houston"],
        "sections": [
            (None, f"""<p>A roofer in The Woodlands spends $1,500 on a YouTube ad, gets 31,000 views and doesn’t get a single call he can trace to it. He decides YouTube doesn’t work. Maybe it doesn’t, for him. More often the ad ran across half of Texas with the logo showing up at second 27, and nobody measured anything past views.</p>
<p>On YouTube ads cost for a local business, the short version is that you pay per view or per thousand impressions, and format and targeting move the price a lot. In {SRC['webfx']}, the most common answer (43% of respondents) was $0.11 to $0.40 per view. A useful local test runs about $1,000 to $1,500 a month for two or three months. Less than that and you mostly learn what a small sample looks like.</p>
<p>The rest of this covers format pricing, keeping ads inside your service area, the opening seconds of the ad, and measuring results without kidding yourself.</p>"""),
            ("How much do YouTube ads cost?", f"""<p>There’s no price list. YouTube is an auction, and what you pay depends on how you buy. Google’s {SRC['formats']} spells out the billing for each format.</p>
<p>Skippable in-stream ads on cost-per-view bidding charge you when someone watches 30 seconds (or the whole ad if it’s shorter) or interacts with it, whichever comes first. Skip at second 6 and you pay nothing. Switch the same ad to Target CPM or conversion bidding and you pay per impression, skipped or not.</p>
<ul><li>Bumpers and non-skippable ads are always per impression (CPM).</li>
<li>In-feed video charges when someone clicks to watch.</li>
<li>Shorts ads on CPV count a view at 10 seconds, at the end of the ad, or on a click, like, comment or share.</li></ul>
<p>In our experience, tightly targeted local campaigns cost more per view than national ones, because you’re competing with every advertiser who wants Montgomery County homeowners. Fine. A $0.25 view in Spring beats a $0.04 view in Lubbock.</p>
<p>Illustrative monthly ranges for planning (not sourced benchmarks):</p>
<div class="bp-tbl"><table><thead><tr><th>Goal</th><th>Typical setup</th><th>Illustrative monthly budget</th><th>What you’d judge it on</th></tr></thead><tbody>
<tr><td>Remarketing only</td><td>Show video to past site visitors and channel viewers</td><td>$300 to $800</td><td>Return visits, calls, form fills</td></tr>
<tr><td>Local test</td><td>Video views campaign, one ZIP cluster, two ads</td><td>$1,000 to $1,500 for 60 to 90 days</td><td>View rate, branded search lift, calls</td></tr>
<tr><td>Steady local awareness</td><td>Views plus bumpers, 10 to 15 mile radius</td><td>$1,500 to $4,000</td><td>Reach, frequency, branded search, lead volume</td></tr>
<tr><td>Lead generation (Demand Gen)</td><td>Conversion bidding with good tracking</td><td>$3,000+ (see Google’s guidance below)</td><td>Cost per lead and lead quality</td></tr>
<tr><td>Multi-location or seasonal push</td><td>Several markets, CTV included</td><td>$5,000+</td><td>Store-level leads and reach on TV screens</td></tr>
</tbody></table></div>
<!--fig:budget-->
<p>People forget about creative. A phone-shot 30-second ad can cost you an afternoon, while a produced spot with a crew and a script usually starts in the low thousands, depending on the shop.</p>"""),
            ("YouTube ad formats in 2026, and which ones local businesses should use", f"""<p>Discovery campaigns are gone. Google’s {SRC['disc']} says remaining Discovery campaigns were automatically upgraded to Demand Gen between January and March 2024. Video action campaigns followed: per Google’s {SRC['vac']}, new ones couldn’t be created after April 2025, existing ones were auto-upgraded in batches in September 2025, and the last stragglers were scheduled for April 2026. If an agency pitches you a “Video action campaign” today, ask what they mean.</p>
<div class="bp-tbl"><table><thead><tr><th>Format</th><th>Length and skip</th><th>How you pay</th><th>Local use we like</th></tr></thead><tbody>
<tr><td>Skippable in-stream</td><td>Skip after 5 seconds; under 3 minutes recommended</td><td>CPV, CPM or per impression on conversion bidding</td><td>The workhorse: a 15 to 45 second ad with a clear offer</td></tr>
<tr><td>In-feed</td><td>Thumbnail in search and Home feed</td><td>Per click to watch</td><td>How-to and explainer videos people choose to watch</td></tr>
<tr><td>Shorts</td><td>Swipe away anytime; under 60 seconds</td><td>CPV or CPM</td><td>Vertical, casual, owner or tech talking to camera</td></tr>
<tr><td>Bumper</td><td>6 seconds, can’t skip</td><td>CPM</td><td>Reminders to people who already saw a longer ad</td></tr>
<tr><td>Non-skippable in-stream</td><td>Up to 60 seconds depending on subtype</td><td>CPM</td><td>Rarely worth it for small budgets</td></tr>
</tbody></table></div>
<p>For most Houston service businesses, skippable in-stream and Shorts carry the load, with bumpers as a cheap reminder layer. In-feed is underrated for businesses that already have useful videos (a pool builder explaining permits, a dentist walking through an implant consult) because the viewer chose to click.</p>"""),
            ("Video views, Video reach or Demand Gen: which campaign type?", f"""<p>Inside Google Ads, the format choice mostly comes through the campaign type and its bidding.</p>
<p><b>Video views</b> uses Target CPV. Google’s page on {SRC['views']} describes it as getting more views at a lower cost, spread across in-stream, in-feed and Shorts. You set an average amount you’re willing to pay per view and some views cost more or less. For a local business testing YouTube, we usually start here, mostly because you only pay for people who actually watched.</p>
<p>Video reach uses Target CPM and aims for unique people at a set frequency. Good for bumpers and for covering an area before a busy season, like HVAC before the first 95-degree week.</p>
<p><b>Demand Gen</b> runs video and images across YouTube, Discover and Gmail with conversion bidding: Target CPA, Maximize conversions and their value-based versions. On paper it’s the lead-generation option. In practice, read Google’s {SRC['dgbudget']} before you commit. It recommends a budget of at least 20 times your target CPA for conversion bidding, at least $100 a day per ad group to avoid a cold start, and $500 a day per ad group for “effective and efficient performance.”</p>
<p>Run that for a business with a $100 target cost per lead and you get a $2,000 budget recommendation per campaign before Google’s algorithm is even comfortable. Plenty of local businesses can’t feed Demand Gen enough conversions to learn, and a starved Demand Gen campaign tends to wander. We’d rather see a $1,200 Video views test plus solid remarketing than a $1,200 Demand Gen campaign that never exits learning.</p>
<p>Later, with dependable conversion tracking (qualified calls, booked appointments, CRM imports) and money to spare, it’s worth a look.</p>"""),
            ("YouTube ads for local business: targeting by radius and ZIP code", f"""<p>Local YouTube campaigns flop on geography more than anything else. Google’s {SRC['geo']} gives you the tools, but the defaults weren’t built for a plumber in Tomball.</p>
<p>On every local video campaign we set these:</p>
<ol><li><b>ZIP codes or a radius instead of “Houston.”</b> Radius targeting needs at least 1 km. ZIP codes work in the US, and bulk entry wants the state included (“77381, Texas”). For a Woodlands business we’ll often use 77380, 77381, 77382, 77384, 77385 and 77389 plus Spring and Conroe ZIPs, rather than a circle that drags in half of north Houston.</li>
<li><b>Location options set to Presence.</b> “Presence or interest” includes people who are merely interested in your area. Google’s help page suggests Presence when you only want people physically in your locations, which describes almost every service business.</li>
<li>A radius that matches how far you’ll actually drive. If your techs won’t go south of Beltway 8, don’t pay for views there, and add negative locations for anywhere you can’t serve. Cheap insurance.</li>
<li>A look at the Locations report after week one, filtered by matched location. Surprises show up fast.</li></ol>
<!--fig:area-->
<p>Houston’s sprawl matters here. Someone living in Kingwood who commutes down 59 to Greenway Plaza watches YouTube at home in the evening. For most home and personal services, target where people live. For lunch spots near the Energy Corridor or Hughes Landing, it’s the reverse.</p>"""),
            ("YouTube remarketing and Customer Match", f"""<p>The cheapest, most reliable YouTube spend for a local business is usually remarketing: showing video to people who already visited your site or watched your channel. They already know your name, so a 20-second clip with a couple of reviews and an offer doesn’t have to do much.</p>
<p>Link your YouTube channel to Google Ads, and you can build {SRC['segments']} for people who watched any video on your channel, watched specific videos, subscribed, visited the channel page, liked a video or saved one to a playlist. Combine those with website visitors from your Google tag, and you have a warm audience that grows every time someone finds you.</p>
<p>Customer Match (uploading your customer emails or phone numbers) is more restricted than people assume. Google’s {SRC['cm']} requires a good history of policy compliance and payment. It also still lists 90 days of account history and more than $50,000 in lifetime spend for using lists in the “Targeting” setting, while every compliant account can use them for Observation and Exclusions. Check what your own account allows before planning around it. Excluding current customers from a new-customer offer is useful even if you can’t target them.</p>
<p>Cap frequency (a few impressions per person per week is plenty) and rotate creative every six to eight weeks. Our <a href="/blog/retargeting-explained/">retargeting explainer</a> covers the setup across Google and Meta.</p>"""),
            ("What makes a YouTube ad work: the first five seconds and the rest", f"""<p>Every skippable ad is a five-second pitch for the right to keep talking. Google’s {SRC['abcd']} distills its YouTube ad research into specific advice:</p>
<ul><li>Introduce your brand or product in the first five seconds, with visuals or audio.</li>
<li>Use more than two shots in the first five seconds. A static opening frame loses people.</li>
<li>Brand mentions land better when spoken by someone on screen than by a voiceover.</li>
<li>Make the call to action both audible and visible.</li></ul>
<p>The same guide cites Nielsen Catalina Solutions research, across nearly 500 campaigns, attributing 49% of sales contribution to creative versus 36% to media. Google notes the findings are correlational. Still, it matches what we see: we’ve never watched a targeting tweak rescue a weak ad.</p>
<!--fig:creative-->
<p>For Shorts, Google’s {SRC['shorts']} is clear: vertical 9:16 video is best, horizontal video shows with blurred bars, under 60 seconds is recommended, and for action-focused ads 10 to 30 seconds works best. It also says ads with sound (music, voiceover or both) have “been shown to increase conversions by over 20%” and recommends ads that blend in with organic Shorts. Google’s guidance doesn’t say much about captions, but we burn them in on every ad anyway. Plenty of people watch on a phone with the sound off in a waiting room or at the kids’ practice.</p>
<p>A decent local 30-second ad, roughly:</p>
<ol><li><b>Seconds 0 to 5:</b> the problem in the customer’s words, the owner or tech on camera, logo and name visible. “If your AC is blowing warm air in Spring this week, this is for you.”</li>
<li><b>Seconds 5 to 20:</b> one reason to choose you. A real job, a real review, a guarantee. Not a list of eight services.</li>
<li><b>Seconds 20 to 30:</b> what to do next, said out loud and on screen. “Call or book online, same-day in The Woodlands and Spring.”</li></ol>"""),
            ("Shooting on a phone or hiring a production company?", f"""<p>It comes up in almost every first meeting. Start with a phone, and pay for production later where it earns its keep.</p>
<p>A modern phone, a $30 clip-on mic, daylight and a steady hand produce video that fits Shorts and in-stream perfectly well. People on YouTube are used to creators shooting on phones. An owner talking straight to the camera in the shop or in front of a finished job often outperforms a glossy spot, because it looks like the content around it. Shoot five or six versions of the opening line in one session and test two of them.</p>
<p>Production is worth paying for when the ad will run on TV screens (shaky phone footage looks worse at 65 inches) or when your brand sells on polish, like luxury remodels, med spas and custom homes. It also makes sense if you’ll run one spot for a year across YouTube, CTV and maybe broadcast, or if phone tests already found a message that works and you want a better version of it.</p>
<p>We’d skip the $10,000 brand film before you know which message makes people call. Spend the first few hundred dollars learning, then spend on production. (Our <a href="/services/creative-branding/">creative team</a> does both, and we’ll still tell you to start with the phone.)</p>"""),
            ("YouTube on the TV screen (CTV)", f"""<p>YouTube isn’t only phones. According to {SRC['nielsen']}, YouTube accounted for 12.4% of all TV viewing time in the US in April 2025, the largest share of any media company that month. {SRC['advtv']} puts it at a platform-best 13.8% in May 2026.</p>
<!--fig:tv-->
<p>On a TV, nobody clicks. The ad is closer to a TV commercial that you can target by ZIP code, which is genuinely new for a business that could never afford Houston broadcast. You can segment by device in Google Ads and check how much of your spend lands on TV screens versus phones.</p>
<p>TV views look great on reports and are hard to tie to leads, so we judge them on branded search, direct traffic and calls from the targeted ZIPs. Keep the phone number and a short URL on screen long enough to read from a couch. Longer than feels necessary.</p>
<p>If TV screens are the main reason you’re interested, compare YouTube with other streaming buys. Our post on <a href="/blog/streaming-tv-ads-worth-it-small-business/">whether streaming TV ads are worth it for small businesses</a> walks through that, and our <a href="/services/ctv-ooh-streaming-radio/">CTV and streaming service</a> covers buying across Hulu, Roku and the rest.</p>"""),
            ("How to measure YouTube ads without fooling yourself", f"""<p>YouTube reporting is generous with credit, so know which column you’re reading.</p>
<p><b>Engaged-view conversions</b> count when someone watches a meaningful chunk of your ad and converts later without clicking. Per Google’s page on {SRC['evc']}, that’s 10 seconds for skippable in-stream (or the full ad if shorter), 5 seconds for in-feed, and 5 seconds or a click for Shorts. The default window for website conversions is 3 days.</p>
<p><b>View-through conversions</b> are looser: someone saw the ad, didn’t interact, and converted later. Google’s page on {SRC['vtc']} notes they’re not included in the main Conversions column. They show in their own column and in All conversions. Report them separately or you’ll double count what Search already gets credit for.</p>
<p>Brand Lift studies survey people who saw your ad against people who didn’t. Google’s {SRC['lift']} page calls it free, but it has a spend requirement, runs over about 10 days, and isn’t available to every account; you need to go through a Google rep. We rarely see a local budget that qualifies.</p>
<p>For local businesses we lean on cruder tools:</p>
<ol><li>Track calls and forms properly first. If your Google Ads conversions aren’t clean, YouTube numbers are meaningless.</li>
<li>Watch branded search volume and Business Profile calls in the targeted ZIPs before and during the campaign.</li>
<li>Run a simple geo split: advertise in one set of ZIPs (say Spring and Klein) and hold back a similar set (say Humble and Atascocita) for six to eight weeks, then compare leads per household. It’s rough, but it’s honest.</li>
<li>Ask new customers how they heard about you, and log it.</li></ol>"""),
            ("Are YouTube ads worth it for a small business?", f"""<p>Sometimes. We lean yes when most of these hold:</p>
<ul><li>Your Google Search and Business Profile are already working, and you want more people searching your name.</li>
<li>Your average job or customer value is high enough that a few extra customers a month pays for $1,000 or more in media.</li>
<li>You can show what you do on camera: a finished pool, a before-and-after, a tech explaining a repair.</li>
<li>You serve a defined area you can target by ZIP code.</li>
<li>You’ll give it at least two to three months and measure it with something beyond views.</li></ul>
<p>We’d hold off if your search campaigns are still leaking money, your website doesn’t convert on mobile, or you need leads next week. YouTube builds demand that Search then captures, and if the capture side is broken, YouTube just makes the leak bigger. So we usually look at <a href="/services/search-marketing/">search</a> first.</p>
<p>If you want an outside look before spending on video, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your current Google or Meta budget is leaking, in your inbox within 48 hours. Fix those leaks, then give YouTube a real test with a phone-shot ad and a tight ZIP list. For context on what TV and radio cost by comparison, see <a href="/blog/radio-tv-advertising-cost-houston/">radio and TV advertising costs in Houston</a>.</p>"""),
        ],
        "faq": [
            ("How much do YouTube ads cost per view?",
             "There's no fixed price because YouTube runs an auction. In a WebFX survey of 270 marketers, the most common answer was $0.11 to $0.40 per view. With cost-per-view bidding on skippable ads you pay only when someone watches 30 seconds, the whole ad if shorter, or interacts. Tightly targeted local campaigns often pay more per view than broad national ones."),
            ("Are YouTube ads worth it for a small business?",
             "They can be when your search marketing already works, your customer value is high, and you serve an area you can target by ZIP code. They are a weak fit if you need leads this week or your website and search campaigns are leaking money. Plan on two to three months of testing and measure branded searches, calls and leads, not views."),
            ("What is the minimum budget for YouTube ads?",
             "Google Ads lets you start with a small daily budget, but a useful local test usually needs around $1,000 to $1,500 a month for two to three months. Demand Gen campaigns need more: Google recommends at least 20 times your target cost per acquisition and at least $100 a day per ad group to avoid a slow start."),
            ("Can I target YouTube ads to specific ZIP codes in Houston?",
             "Yes. Google Ads supports US ZIP code targeting and radius targeting with a minimum radius of 1 kilometer. For local businesses, set the location option to Presence so ads reach people physically in the area rather than anyone interested in Houston, and check the locations report after the first week to confirm where the ads actually ran."),
            ("Do YouTube ads show on TV?",
             "Yes. YouTube ads run on connected TVs as well as phones and computers, and YouTube is now the largest single source of TV viewing time in the US according to Nielsen. On a TV nobody clicks, so use a produced horizontal ad with your phone number on screen and judge results by branded searches and calls from the targeted ZIP codes."),
        ],
        "figures": {
            "budget": {
                "type": "bars",
                "title": "Illustrative monthly YouTube budgets",
                "sub": "Midpoints of the planning ranges in the table above",
                "items": [["Remarketing only", 550, "$550"], ["Local test", 1250, "$1,250"], ["Steady awareness", 2750, "$2,750"], ["Demand Gen leads", 3500, "$3,500+"], ["Multi-location push", 6000, "$5,000+"]],
                "highlight": [1],
                "note": "Illustrative ranges",
                "alt": "Bar chart of illustrative monthly YouTube ads cost for a local business in Houston by campaign goal",
                "caption": "Planning numbers, not benchmarks; your auction prices depend on targeting, season and creative.",
            },
            "area": {
                "type": "map",
                "title": "Target where customers live",
                "sub": "A sample ZIP cluster for a Woodlands-based service business",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Shenandoah", "Magnolia", "Tomball"],
                "alt": "Map of a sample YouTube ads targeting area for a local business in The Woodlands, Spring and Conroe",
                "caption": f"Radius targeting starts at 1 km, and ZIP codes are supported in the US, per Google’s {A('https://support.google.com/google-ads/answer/1722043', 'location targeting help')}.",
            },
            "creative": {
                "type": "checklist",
                "title": "Local YouTube ad checklist",
                "sub": "What we check before an ad goes live",
                "items": [
                    "Brand name and logo inside the first 5 seconds",
                    "More than two shots in the first 5 seconds",
                    "Owner or tech says the brand name on camera",
                    "One offer or reason to choose you, not eight",
                    "Call to action spoken and shown on screen",
                    "Captions burned in for sound-off viewing",
                    "Vertical 9:16 version for Shorts",
                    "Service area named (The Woodlands, Spring...)",
                ],
                "alt": "Checklist for YouTube ad creative for a local business in Houston and The Woodlands before launch",
                "caption": f"Based on Google’s {A('https://services.google.com/fh/files/misc/youtube_google_abcd_reference_guide_en.pdf', 'ABCD guide')} and its Shorts ads guidance.",
            },
            "tv": {
                "type": "stats",
                "title": "YouTube’s share of US TV viewing",
                "stats": [["12.4%", "April 2025, largest of any media company"], ["13.8%", "May 2026, a platform best"]],
                "note": "Source: Nielsen Media Distributor Gauge",
                "alt": "Stat tiles showing YouTube's share of US TV viewing, relevant to YouTube ads for local businesses in Houston",
                "caption": f"From {A('https://www.nielsen.com/news-center/2025/youtube-maintains-largest-share-of-tv-viewing-among-media-companies-for-third-consecutive-month/', 'Nielsen')} and {A('https://www.advanced-television.com/2026/07/29/nielsen-youtube-takes-13-8-of-us-tv-watch-time-in-may/', 'Advanced Television')}.",
            },
        },
    },
]
