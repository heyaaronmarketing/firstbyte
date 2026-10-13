"""Batch 5, plumbing: "how to get more plumbing service calls" (Houston playbook) + "plumbing seo keywords" (Houston keyword map).

Research: NWS Houston/Galveston Feb 2021 and annual 2021 climate summaries (IAH 13F on Feb 16, tying 1895; Hobby 15F;
"broken pipes"; likely costliest Texas weather disaster), USDA NRCS official series description for Lake Charles clay
(cracks 1-2 in. wide, open 60-90 days most years, SE Texas between the Colorado and Trinity rivers), Google Business
Profile help on service areas (20 max, about 2 hours' drive) and business-name rules, Google's local ranking help page
(relevance, distance, prominence; reviews), Local Services Ads billing and ranking help pages, Twilio's Sept 2023 A2P
10DLC blocking notice, DOE Energy Saver on water heater lifespans, Fixr's Jan 2026 water heater install cost guide,
22 TAC 367.10 (RMP license number on vehicles, ads, invoices) and 367.9, TSBPE site (still the licensing agency, Oct 2026)
and the 2018 Sunset staff recommendation to move plumbing to TDLR, Census QuickFacts (Harris and Montgomery counties,
V2025), Google spam policies (doorway abuse), Google multilingual-site guidance, Search Console performance report help,
Search Engine Land quoting Google on regex filters. Competitors read: Simpro, Clicksgeek, Hearth, Loopex Digital.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "nwsfeb": A("https://www.weather.gov/media/hgx/climate/summary/Feb_2021_Regional_Climate_Summary.pdf", "National Weather Service’s February 2021 climate summary"),
    "nwsyr": A("https://www.weather.gov/media/hgx/climate/summary/Annual_2021_Regional_Climate_Summary.pdf", "NWS Houston/Galveston’s 2021 annual summary"),
    "clay": A("https://soilseries.sc.egov.usda.gov/OSD_Docs/L/LAKE_CHARLES.html", "USDA’s official description of Lake Charles clay"),
    "sab": A("https://support.google.com/business/answer/9157481?hl=en", "Google’s service area help page"),
    "gbpg": A("https://support.google.com/business/answer/3038177?hl=en", "Business Profile guidelines"),
    "rank": A("https://support.google.com/business/answer/7091?hl=en", "Google’s own local ranking page"),
    "lsabill": A("https://support.google.com/adwords/answer/7195435", "Local Services Ads billing page"),
    "lsarank": A("https://support.google.com/localservices/answer/7527305?hl=en", "LSA ranking page"),
    "twilio": A("https://www.twilio.com/en-us/changelog/-u-s--a2p-10dlc--full-blocking-of-traffic-sent-from-unregistered", "Twilio’s carrier notice"),
    "doe": A("https://www.energy.gov/energysaver/articles/which-water-heater-right-you", "Department of Energy"),
    "fixr": A("https://www.fixr.com/costs/install-water-heater", "Fixr’s January 2026 cost guide"),
    "rule10": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-367-10", "22 TAC §367.10"),
    "tsbpe": A("https://tsbpe.texas.gov/", "Texas State Board of Plumbing Examiners"),
    "sunset": A("https://www.sunset.texas.gov/public/uploads/files/reports/Texas%20State%20Board%20of%20Plumbing%20Examiners%20Executive%20Summary_11-9-18.pdf", "2018 Sunset staff report"),
    "qfh": A("https://www.census.gov/quickfacts/fact/table/harriscountytexas,montgomerycountytexas/PST045224", "Census QuickFacts"),
    "qfm": A("https://www.census.gov/quickfacts/fact/table/montgomerycountytexas/PST045225", "Census QuickFacts for Montgomery County"),
    "doorway": A("https://developers.google.com/search/docs/essentials/spam-policies", "spam policies"),
    "intl": A("https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites", "guidance on multilingual sites"),
    "gsc": A("https://support.google.com/webmasters/answer/7576553?hl=en", "Search Console’s performance report"),
    "regex": A("https://searchengineland.com/regular-expression-filter-support-coming-to-google-search-console-performance-reports-337224", "Search Engine Land"),
}

SIB1 = "/blog/how-to-get-more-plumbing-service-calls-houston/"
SIB2 = "/blog/plumbing-seo-keywords-houston/"

POSTS = [
    # ------------------------------------------------------------------ post 1
    {
        "slug": "how-to-get-more-plumbing-service-calls-houston",
        "title": "How to Get More Plumbing Service Calls in Houston: A 2026 Playbook",
        "seo_title": "How to Get More Plumbing Service Calls in Houston",
        "desc": "How to get more plumbing service calls in Houston and The Woodlands: freeze-week prep, Business Profile areas, LSA, missed-call text-back and memberships.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google"],
        "art": "b2",
        "hero": "plumbing",
        "hero_alt": "Illustration of pipes and a wrench for a guide on how to get more plumbing service calls in Houston",
        "related": ["local-services-ads-vs-google-ads-home-services", "call-tracking-which-ads-make-phone-ring", "angi-vs-thumbtack-leads-worth-it-contractors"],
        "sections": [
            (None, f"""<p>To get more plumbing service calls in Houston, answer more of the calls you already get, then make sure Google shows you first when the next one happens. That means a text back within a minute on every missed call, a Business Profile with honest service areas, Local Services Ads raised before the weather turns, and new reviews every week. After that, build offers around the work this region sends you on a schedule: burst pipes in a hard freeze, slab leaks in clay that shrinks and swells, and water heaters at the end of their life.</p>
<p>We’d hand this to a two- or three-truck shop in The Woodlands in exactly this order. The first fix costs almost nothing, and it isn’t really marketing.</p>"""),

            ("Fix the phone before you buy more calls", f"""<p>Here’s the part most shops get wrong. They spend real money to make the phone ring, then let a big share of those calls hit voicemail while the owner is under a sink in Oak Ridge North. A homeowner with water on the floor won’t leave a message. They call the next plumber on the list.</p>
<p>Missed-call text-back fixes most of that for very little money. When a call goes unanswered, your phone system sends a text within seconds: “Sorry we missed you, this is Smith Plumbing. Is this an active leak? Reply with your address and we’ll call you right back.” A lot of people reply, and every reply is a lead you already paid for.</p>
<!--fig:textback-->
<p>Before you switch it on, ask your phone or CRM vendor to confirm your number is registered for A2P 10DLC, the carrier system for business texting from 10-digit numbers. Per {SRC['twilio']}, unregistered traffic to US numbers has been blocked since September 1, 2023. And give each marketing channel its own tracking number so you can see which one drove the call; our guide to <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking</a> walks through the setup.</p>"""),

            ("How to get more plumbing service calls: sort them by trigger", f"""<p>With the phone covered, sort your work by what makes people call. Each trigger has its own timing and its own best channel, yet most shops advertise all of it the same way all year.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Job type</th><th>What triggers the call</th><th>Timing in Greater Houston</th><th>Channel that catches it</th></tr></thead>
<tbody>
<tr><td>Burst and frozen pipes</td><td>Hard freeze, often with power loss</td><td>A few days a year, enormous spikes</td><td>LSA, Business Profile, a phone someone answers</td></tr>
<tr><td>Slab leaks, high water bills</td><td>Soil movement under slab homes, a shocking utility bill</td><td>Builds through long dry spells; check your own job history</td><td>Search (organic and paid), a leak detection page</td></tr>
<tr><td>Drains and sewer lines</td><td>Roots, grease, aging cast iron, houseguests</td><td>Year-round</td><td>LSA, map pack, repeat customers</td></tr>
<tr><td>Water heaters</td><td>Tank age, a leak in the garage, no hot water</td><td>Year-round, with more failures once cold fronts arrive in many shops</td><td>Search, past-customer lists, memberships</td></tr>
<tr><td>Repipes, gas lines, remodels</td><td>Planned projects, home sales, insurance claims</td><td>Steady, with planning in spring and fall</td><td>Google Ads search, website, reviews, referrals</td></tr>
</tbody></table></div>
<p>Ad budget should follow the emergency rows. Follow-up systems (reminders, memberships, quotes that get a second text) should follow the planned ones.</p>
<!--fig:calendar-->
<p>Pull two years of jobs by month and ZIP code from ServiceTitan, Housecall Pro or Jobber. Your own peaks beat any national chart, ours included, and they tell you when to raise budgets before the phones light up instead of after.</p>"""),

            ("Plan for the freeze before the forecast", f"""<p>Winter Storm Uri is the reference point for every plumber here. According to the {SRC['nwsfeb']}, Bush Intercontinental hit 13°F on February 16, 2021, tying a record from 1895, and Hobby dropped to 15°F. The {SRC['nwsyr']} lists “broken pipes” among the impacts and says the event may have been the costliest weather disaster in Texas history, ahead of Harvey.</p>
<!--fig:uri-->
<p>The shops that did well that week were already visible, already answering and honest about wait times. Freezes that size are rare, but shorter hard freezes come often enough that prep pays. Our November checklist:</p>
<ul><li><b>Build a freeze page now.</b> Burst pipe repair, frozen pipes, how to find the main shutoff, what to do while you wait. Homeowners search for help before they search for a plumber.</li>
<li><b>Write a paused “freeze” campaign in Google Ads.</b> Terms like burst pipe repair, frozen pipe repair and emergency plumber plus your towns, with ads that state real wait times. Turn it on when the NWS issues a hard freeze watch.</li>
<li><b>Raise your LSA budget a few days ahead,</b> then cap it at what your trucks can actually run. Calls you can’t serve still cost money and reviews.</li>
<li><b>Line up overflow answering</b> and a triage script: active leak first, no water second, everything else on a callback list by text.</li>
<li><b>Plan the follow-up.</b> Two weeks after a freeze, the calls change to pipe insulation, rerouting exposed lines and repipes after damage.</li></ul>"""),

            ("Slab leaks, clay soil and the calls nobody plans for", f"""<p>Most Houston-area homes sit on concrete slabs, and much of the metro sits on clay that moves. The {SRC['clay']}, a soil mapped across Southeast Texas between the Colorado and Trinity rivers, says it cracks 1 to 2 inches wide at the surface when dry, and the cracks stay open 60 to 90 days most years. Soil that opens and closes like that puts stress on everything buried in it, including supply lines under the slab.</p>
<p>Homeowners rarely search “slab leak” first. They search the symptom: a water bill that doubled, a warm spot on the tile, water running with every tap off.</p>
<ul><li>Build one page for slab leak detection and one for slab leak repair, with your options explained plainly (spot repair, reroute, repipe).</li>
<li>Write a short guide on reading your water meter to check for a leak. It earns links and calls from people who aren’t sure yet.</li>
<li>Offer leak detection as a flat-fee entry job. It’s a smaller ticket that opens the door to a reroute or a repipe.</li>
<li>Trade referrals with a foundation repair company. Their inspectors find plumbing problems and your techs find cracks.</li></ul>
<p>Soil varies across the metro, so check where your slab jobs actually cluster by ZIP before you target a town. We cover which slab, repipe and leak phrases deserve their own page in our <a href="{SIB2}">plumbing SEO keyword map for Houston</a>.</p>"""),

            ("How to get more plumbing leads from your Google Business Profile", f"""<p>Your Business Profile is the free version of the ad, and for emergency work it often beats the paid one. The settings that matter most:</p>
<ul><li><b>Service areas.</b> {SRC['sab']} allows up to 20, defined by city or ZIP code, and says your overall area shouldn’t run more than about 2 hours of driving from your base. For a shop based off Research Forest Drive, that might be The Woodlands, Spring, Conroe, Shenandoah, Oak Ridge North, Tomball and Magnolia, plus ZIP codes like 77380, 77381, 77382, 77373 and 77379 where you want the work.</li>
<li><b>Address.</b> If customers don’t come to you, remove the address and run as a service-area business. Most plumbers working from a house or a yard fall in this group.</li>
<li><b>Name.</b> The {SRC['gbpg']} prohibit adding service or location words to your name. “Smith Plumbing” is fine; “Smith Plumbing Emergency Plumber The Woodlands” is a suspension waiting to happen.</li>
<li><b>Category and services.</b> Choose Plumber as the primary category and add each service you actually sell with a short description: water heater replacement, slab leak detection, hydro jetting, gas line repair.</li>
<li><b>Photos and posts.</b> Real trucks and real jobs. Set special hours and post shutoff tips before a freeze.</li></ul>
<p>One honest limit: service areas tell Google where you work, but your distance from the searcher still counts. A shop in Conroe won’t own Katy by listing it. For the full ranking picture, see our guide to <a href="/blog/local-seo-contractors-houston/">local SEO for Houston contractors</a>.</p>"""),

            ("How to get more plumbing customers with Local Services Ads", f"""<p>Local Services Ads sit above everything else on the page and charge per lead instead of per click. For an emergency trade that’s usually the first paid channel we’d turn on. If you’re weighing it against regular search ads, our breakdown of <a href="/blog/local-services-ads-vs-google-ads-home-services/">LSA vs Google Ads for home services</a> covers the trade-offs, and <a href="/blog/google-guaranteed-vs-google-verified/">Google Guaranteed vs Google Verified</a> explains the badge.</p>
<p>Know what you’re paying for. Google’s {SRC['lsabill']} counts answered calls, texts, voicemails, booking requests and even some missed calls as charged leads. Follow-ups from the same customer within 15 days aren’t charged again, and unanswered calls are only charged during your ad schedule and business hours. Google keeps checking lead quality for 30 days and can credit bad ones automatically.</p>
<p>The {SRC['lsarank']} lists your bid, how likely your ad is to produce a lead, and your profile quality as the placement factors, with responsiveness to customer inquiries counted under the second one. So a shop that lets calls ring out ranks lower and still pays for some of the missed calls. That’s one more reason the phone section came first.</p>
<p>How we run LSA for plumbers:</p>
<ul><li>Turn off job types you don’t want, so a drain-only crew doesn’t pay for water softener shoppers.</li>
<li>Set your schedule to the hours someone really answers.</li>
<li>Dispute junk leads every week; don’t wait for the automatic review.</li>
<li>Run regular search ads alongside LSA for high-ticket work like repipes and tankless installs, where a landing page sells better than a phone call. That’s the work our <a href="/services/search-marketing/">search marketing team</a> does every day.</li></ul>
<p>Buying from Angi or Thumbtack too? Here’s <a href="/blog/angi-vs-thumbtack-leads-worth-it-contractors/">whether those leads are worth it</a>.</p>"""),

            ("How to get more plumbing jobs from the reviews you already earn", f"""<p>{SRC['rank']} says review count and rating feed into how prominent Google considers a business. It doesn’t talk about recency, but we keep seeing it in map pack audits: a shop with 400 reviews and nothing new since spring tends to slip behind a shop with 120 and a few fresh ones every week.</p>
<p>So make the review request part of closing the ticket:</p>
<ol><li>The tech finishes, walks the customer through the work and asks in person.</li>
<li>Your system sends a text with the direct review link within the hour, while the customer still has hot water and good feelings.</li>
<li>One reminder two days later. No more.</li>
<li>The office replies to every review within a few days, naming the service (“glad the new water heater is working”) without sharing private details.</li></ol>
<p>Ask every customer, not only the happy ones, and never offer anything for a review. The FTC rule on fake and incentivized reviews applies to small shops too; our explainer on the <a href="/blog/fake-reviews-rule-local-businesses/">fake reviews rule</a> covers the lines. Techs named in reviews should hear about it at the Monday meeting.</p>"""),

            ("Water heater replacement offers that don’t race to the bottom", f"""<p>Water heaters are the most predictable revenue in residential plumbing. The {SRC['doe']} says conventional storage tanks last about 10 to 15 years and tankless units about 20. Run that against your own map. A Spring or Conroe subdivision that went up in 2012 is full of original tanks that are now 14 years old, and the builder probably installed the same model in every garage on the street.</p>
<p>For pricing, {SRC['fixr']} puts a typical national install at about $1,400, within a $900 to $3,000 range, and tankless at roughly $1,000 to $4,000. Houston prices vary with permits, venting and attic installs, so treat those as a sanity check.</p>
<!--fig:offers-->
<p>Offers that work without wrecking your margin:</p>
<ul><li><b>Free age check on every service call.</b> Techs read the serial number, note the year and tell the homeowner where the tank stands. It’s honest and it fills next year’s pipeline.</li>
<li><b>“Replace before it floods the garage.”</b> Upfront, all-in price including haul-away, permit and expansion tank if needed.</li>
<li><b>Financing shown on the page,</b> since a $2,500 surprise is easier as a monthly number.</li>
<li><b>A tankless consult</b> for homeowners who are planning, not panicking. Different page, different ad, different conversation.</li></ul>"""),

            ("How to grow a plumbing business with memberships", f"""<p>Emergency calls are lumpy. A membership program smooths them out and builds a list of homeowners who already trust you.</p>
<p>A plumbing membership in Houston can be simple: an annual water heater flush and inspection, a whole-house plumbing check, no trip fee, a small repair discount and priority scheduling. Priority is the part people here actually buy. In a freeze, members go to the front of the line, and you can say so plainly when you sell the plan.</p>
<p>A hypothetical: a three-truck shop in Spring signs 250 members at $15 a month. That’s $45,000 a year before a single repair, plus 250 scheduled visits where techs spot aging tanks, corroded shutoffs and slow drains. Nobody charged you a lead fee for those jobs. Your numbers will differ, but the visit is the marketing.</p>
<p>Don’t promise priority you can’t deliver in a freeze week. And text members in November with shutoff and insulation tips so they remember why they pay. More on how this fits the rest of the funnel is on our <a href="/industries/service/">home services marketing</a> page.</p>"""),

            ("Put your license number on everything", f"""<p>Texas makes license display a rule, and it doubles as a trust signal. Under {SRC['rule10']}, the responsible master plumber’s license number and the company name have to appear on both sides of every service vehicle, in contrasting letters at least two inches tall, preceded by “M,” “MPL” or “RMP.” Advertising that solicits plumbing work has to show the license number too, and the first page of every proposal, invoice and contract has to say the company is “regulated by the Texas State Board of Plumbing Examiners.”</p>
<p>Licensing is handled by the {SRC['tsbpe']}, which was still the agency in charge when we checked in October 2026. The board’s future has been debated before (a {SRC['sunset']} recommended moving plumbing into TDLR), so confirm the current rules on the state’s site before you print new wraps.</p>
<p>From a marketing view, put the license number in your site footer, on every landing page, in your Business Profile description and on the truck. Homeowners who have been burned by an unlicensed handyman look for it.</p>
<p>Your homework this week takes ten minutes. Call your own business line from a cell phone at 12:30 on a weekday and again at 7 p.m., and note what happens. If either call ends in voicemail with no text back, fix that before you add a dollar of ad budget. And if you’re running Local Services Ads and search ads at the same time, our free <a href="/contact/">Ad Spend Leak Check</a> will show whether the search campaign is paying for emergency calls LSA already brings in. You get a 10-minute recorded walkthrough of the account within 48 hours.</p>"""),
        ],
        "faq": [
            ("How do I get more plumbing calls?", "Start with the basics that decide who Google shows and who gets hired: a complete Business Profile with real service areas, Local Services Ads, fast answers on every call, and a text back on every missed one. Then add steady review requests and offers built around predictable work like water heater replacement. Most shops gain more from answering faster than from spending more."),
            ("How do I get more plumbing leads without paying for them?", "Your Business Profile, reviews, past customers and memberships are the free channels. Keep the profile complete, post before freezes, ask every customer for a review by text, and contact past customers when their water heater reaches 10 years. A short guide on checking your water meter for leaks can also earn search traffic and calls over time."),
            ("What are good plumbing marketing ideas for a small shop?", "Pick ideas tied to local demand: a freeze-prep page and paused freeze ad campaign, a slab leak detection page, free water heater age checks on every call, a simple membership with priority scheduling, referral swaps with foundation repair companies, and missed-call text-back. Each one is cheap to set up and easy to measure with call tracking."),
            ("Are Local Services Ads worth it for plumbers in Houston?", "For most residential plumbers, yes, as long as someone answers the phone. You pay per lead rather than per click, and LSA appears above regular ads. Google charges for answered calls, texts and some missed calls, so a shop that lets calls ring out pays for leads it never books. Dispute junk leads weekly and turn off job types you don't want."),
            ("How long does it take to see more plumbing service calls?", "Paid channels like Local Services Ads and search ads can add calls within days of launch. Missed-call text-back helps the first week. Business Profile improvements, reviews and SEO pages usually take a few months to show up in rankings, and memberships build over a year. Track calls by source from day one so you can see which change actually worked."),
        ],
        "figures": {
            "calendar": {
                "type": "columns",
                "title": "A hypothetical Spring shop’s calls by month",
                "sub": "Freeze months spike; summer slab and water heater work keeps the floor up",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [88, 100, 58, 52, 55, 60, 68, 72, 64, 56, 60, 78],
                "highlight": [0, 1],
                "y_label": "Relative call volume",
                "note": "Illustrative example",
                "alt": "Illustrative column chart of monthly plumbing service calls for a Spring, Houston area shop, peaking in winter",
                "caption": "Your own two-year job history by month and ZIP code is the version of this chart that matters.",
            },
            "uri": {
                "type": "stats",
                "title": "What Winter Storm Uri did to Houston",
                "stats": [["13°F", "Low at Bush Intercontinental, Feb 16, 2021"], ["15°F", "Low at Hobby the same morning"], ["1895", "The year of the record IAH tied"]],
                "note": "Source: NWS Houston/Galveston, February 2021 climate summary",
                "alt": "Stat tiles showing Houston record lows during Winter Storm Uri, a key driver of plumbing service calls",
                "caption": f"Figures from the {A('https://www.weather.gov/media/hgx/climate/summary/Feb_2021_Regional_Climate_Summary.pdf', 'NWS February 2021 summary')}, which lists broken pipes among the storm’s impacts.",
            },
            "textback": {
                "type": "steps",
                "title": "How missed-call text-back saves a lead",
                "sub": "The sequence we set up for plumbing shops",
                "steps": [
                    ["Call goes unanswered", "The tech is under a house or the office line is busy."],
                    ["Text fires in seconds", "A short message asks if it’s an active leak and for the address."],
                    ["Customer replies", "The reply lands in a shared inbox or CRM, tagged with the call source."],
                    ["Callback inside 5 minutes", "Whoever is free calls back and books, or triages to the next slot."],
                    ["Log the outcome", "Booked, lost or spam, so you can see what missed calls cost you."],
                ],
                "alt": "Five steps of a missed-call text-back system that helps Houston plumbers get more plumbing service calls",
                "caption": "Register your number for A2P 10DLC first, or carriers will block the texts.",
            },
            "offers": {
                "type": "compare",
                "title": "Water heater offers: discount vs value",
                "left": {"title": "Race to the bottom", "items": ["“$200 off any water heater”", "Price hidden until the visit", "Same ad for panic and planning", "No follow-up after the quote"]},
                "right": {"title": "What books more jobs", "items": ["Free age check on every call", "All-in price with haul-away", "Financing shown up front", "Separate tankless consult page", "Text follow-up two days later"]},
                "alt": "Comparison of discount water heater offers versus value offers that win more plumbing jobs in Houston",
                "caption": f"The {A('https://www.energy.gov/energysaver/articles/which-water-heater-right-you', 'DOE')} puts storage tank life at 10 to 15 years, which makes replacements predictable.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2
    {
        "slug": "plumbing-seo-keywords-houston",
        "title": "Plumbing SEO Keywords for Houston: A Keyword Map That Books Jobs",
        "seo_title": "Plumbing SEO Keywords for Houston: A Keyword Map",
        "desc": "Plumbing SEO keywords for Houston plumbers: emergency vs. high-ticket terms, suburb and Spanish keywords, where each goes, and how to track them.",
        "category": "SEO & AI search",
        "icons": ["Search Console", "Google Business Profile", "Google"],
        "art": "b4",
        "hero": "search",
        "hero_alt": "Search bar illustration for a Houston guide to plumbing SEO keywords and local plumber SEO",
        "related": ["local-seo-contractors-houston", "power-of-local-landing-pages", "get-found-near-me-google"],
        "sections": [
            (None, f"""<p>The plumbing SEO keywords that book jobs in Houston fall into a handful of groups: emergency terms (“emergency plumber Spring TX,” “burst pipe repair”), high-ticket services (water heater replacement, slab leak repair, whole-house repipe, sewer line replacement, hydro jetting), suburb modifiers like The Woodlands, Tomball, Kingwood and Conroe, Spanish-language searches, and the questions homeowners ask before they call. Each group belongs on a different kind of page, and that mapping matters more than the list.</p>
<p>A list of 100 phrases is easy to find. Deciding which phrase gets its own page, which one belongs in the Business Profile and which one isn’t worth chasing is the actual work. Below is the map we’d build for a residential plumber north of Houston, with a way to check in Search Console whether each piece is paying off.</p>"""),

            ("Why a Houston plumber’s keyword list looks different", f"""<p>A downloaded list treats “plumber” as one market. Google doesn’t. Its {A('https://support.google.com/business/answer/7091?hl=en', 'local ranking help page')} says results depend on relevance, distance and prominence, so a search for “water heater repair” in Spring and the same search in Katy are two different contests with different winners.</p>
<p>National lists also come with monthly volumes that look precise and mean little at the suburb level. “Plumber Tomball” will never show a big number in a keyword tool, yet one booked repipe from it can pay for a year of content. We’d rank keywords by job value and intent first and by volume a distant third.</p>
<p>And no national list knows what this region produces: hard freezes, slab homes on moving clay, subdivisions full of tanks the same age, and a large Spanish-speaking population. The map below is built around those. If you want the call-volume side of the plan, our companion piece on <a href="{SIB1}">how to get more plumbing service calls in Houston</a> covers ads, phones and memberships.</p>"""),

            ("Plumbing SEO keyword clusters, by intent", f"""<p>Here’s the map. Volumes are left out on purpose; check your own in Google Ads Keyword Planner or Search Console. “Relative value” is our rough view of what a booked job from that cluster is worth to a typical residential shop.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Cluster</th><th>Example keywords</th><th>Intent</th><th>Relative value</th><th>Best home</th></tr></thead>
<tbody>
<tr><td>Emergency</td><td>emergency plumber the woodlands, 24 hour plumber spring tx, burst pipe repair, water leak in ceiling</td><td>Call now</td><td>Medium, high volume</td><td>Business Profile, LSA, emergency page</td></tr>
<tr><td>Water heaters</td><td>water heater replacement, water heater repair conroe, tankless water heater installation, no hot water</td><td>Hire this week</td><td>High</td><td>Service pages</td></tr>
<tr><td>Slab and leaks</td><td>slab leak detection, slab leak repair, high water bill leak, leak detection kingwood</td><td>Diagnose, then hire</td><td>High</td><td>Service pages, guide</td></tr>
<tr><td>Repipe</td><td>whole house repipe, repipe cost, pex repipe, repiping company houston</td><td>Research, compare</td><td>Very high</td><td>Service page, cost page</td></tr>
<tr><td>Sewer and drains</td><td>sewer line replacement, sewer camera inspection, hydro jetting, drain cleaning tomball</td><td>Hire, sometimes urgent</td><td>Medium to very high</td><td>Service pages</td></tr>
<tr><td>Gas and fixtures</td><td>gas line repair, gas leak plumber, toilet installation, garbage disposal replacement</td><td>Hire</td><td>Low to high</td><td>Service pages</td></tr>
<tr><td>Questions</td><td>why is my water bill so high, how long do water heaters last, how to shut off water to house</td><td>Learn</td><td>Low now, builds trust</td><td>Blog, guides</td></tr>
<tr><td>Spanish</td><td>plomero cerca de mí, plomero en houston, fuga de agua, calentador de agua</td><td>Call or hire</td><td>Medium to high</td><td>Spanish pages</td></tr>
</tbody></table></div>
<!--fig:value-->
<p>Notice how few clusters belong on the blog. Most plumbing intent is commercial, so most of your keyword work goes into service pages and the Business Profile.</p>"""),

            ("Emergency plumbing keywords belong in the map pack, not the blog", f"""<p>Someone searching “burst pipe” at 2 a.m. in a February freeze doesn’t read articles. They tap the first phone number they trust. That means emergency keywords are won mostly in the map pack and Local Services Ads, with a single strong emergency page on your site to back them up.</p>
<p>What that emergency page needs:</p>
<ul><li>A click-to-call button and your real hours above the fold. Only say 24/7 if a human answers at 2 a.m.</li>
<li>The emergencies you handle, in the words people use: burst pipe, water leak in ceiling, toilet overflowing, sewage backing up, no water, gas smell.</li>
<li>What to do while you wait, starting with how to shut off the main.</li>
<li>Your towns, with honest response times, and your license number.</li></ul>
<p>In the Business Profile, emergency relevance comes from your primary category (Plumber), your listed services and your hours. Reviews that mention “came out at night during the freeze” help too, but you can’t script them. Build and publish the emergency page in the fall. A page needs weeks to get indexed and settle, and nobody writes one while the phones are ringing in a hard freeze. Our <a href="{SIB1}">plumbing service calls playbook</a> has the rest of the freeze prep.</p>"""),

            ("High-ticket plumbing keywords that deserve their own page", f"""<p>This is where plumbing SEO earns its keep. Each of these jobs is worth a dedicated page with real depth, not a paragraph on a “services” page.</p>
<h3>Water heater replacement and installation</h3>
<p>Cover tank vs tankless, gas vs electric, attic vs garage installs, and how long each lasts (the {SRC['doe']} has lifespan figures you can cite). Searchers also type “water heater replacement cost,” so give your own installed range and what pushes a job to the top of it: attic access, venting, a pan and drain line, permits. National cost guides are a sanity check, not your price.</p>
<h3>Slab leak detection and repair</h3>
<p>Write for the symptoms (high water bill, warm floor, running water sound) and explain spot repair vs reroute vs repipe. Homeowners also want to know why it happened. A short paragraph on expansive clay soil, linked to the {SRC['clay']}, answers that without sounding like a sales pitch.</p>
<h3>Whole-house repipe</h3>
<p>The longest research cycle and the biggest ticket. Searchers want material options (PEX vs copper), time in the house, drywall repair and cost. A separate cost page often ranks for “repipe cost” queries the main page can’t.</p>
<h3>Sewer line replacement, camera inspection and hydro jetting</h3>
<p>Explain the camera inspection first, since it usually leads to the bigger job. Hydro jetting gets its own page because people search it by name.</p>"""),

            ("Local plumber SEO: suburb modifiers and location pages", f"""<p>City and town names are the most useful modifiers in local plumber SEO. People type “plumber in the woodlands” or “water heater repair spring tx” even when Google already knows where they are, and those phrases signal a buyer.</p>
<!--fig:towns-->
<p>The trap is building twenty identical town pages. Google’s {SRC['doorway']} list “multiple domain names or pages targeted at specific regions or cities that funnel users to one page” as doorway abuse. A location page has to earn its place with things only that town has:</p>
<ul><li><b>The Woodlands:</b> village names like Alden Bridge, Sterling Ridge, Cochran’s Crossing and Creekside Park, and the jobs you’ve done in each.</li>
<li><b>Spring:</b> the specific neighborhoods and ZIP codes you serve (77373 and 77379, for example), and drive times off I-45 and the Grand Parkway.</li>
<li><b>Tomball and Magnolia:</b> older homes in town alongside new subdivisions, and well or septic work if you do it.</li>
<li><b>Kingwood:</b> its own villages, its mature trees and the root intrusion into sewer lines that comes with them, if that matches your job history.</li>
<li><b>Conroe:</b> Lake Conroe properties and fast-growing subdivisions on the west and south sides.</li></ul>
<p>Add photos from real jobs in that town, a review from a customer there and an honest response time. If you can’t fill a page with that, skip the page and list the town on your service-area page instead. Our guide to <a href="/blog/power-of-local-landing-pages/">local landing pages</a> goes deeper.</p>"""),

            ("Spanish-language plumbing keywords", f"""<p>This is the cluster almost every keyword list skips. According to {SRC['qfh']}, 45.0% of Harris County residents age 5 and up speak a language other than English at home, and 46.1% of the county is Hispanic or Latino. In Montgomery County the figures are 25.3% and 30.2%. Not every one of those households searches in Spanish, but plenty do, and in the accounts we see, few plumbers have built real Spanish pages to catch them.</p>
<p>Useful terms to start from: plomero, plomero cerca de mí, plomero en Houston, plomería, fuga de agua, fuga debajo de la casa, calentador de agua, destapar drenaje, reparación de tubería. Have a native speaker who knows the trade review them, since regional wording varies.</p>
<p>Get the setup right. Google’s {SRC['intl']} recommends separate URLs for each language version and warns against automatically redirecting visitors by language, so build real /es/ pages instead of a translate widget. And only do it if someone answers the phone in Spanish. A Spanish page that leads to an English-only voicemail wastes the click.</p>"""),

            ("How to handle “near me” plumbing searches", f"""<p>“Plumber near me” and “emergency plumber near me” are probably the most common plumbing searches there are, and they are almost entirely a map pack game. Google reads “near me” as a request to use the searcher’s location, so distance and your Business Profile do most of the work.</p>
<p>What not to do: stuff “near me” into headings, alt text and footers. It reads badly and does little. And don’t add keywords to your business name; Google’s {SRC['gbpg']} forbid service or location terms in the name and can suspend profiles that do it.</p>
<p>What does help:</p>
<ul><li>Accurate service areas (up to 20 cities or ZIP codes) and a verified profile.</li>
<li>Services listed in the profile with plain descriptions.</li>
<li>A steady flow of reviews, which Google says feed prominence.</li>
<li>Town names used naturally on service pages, so Google sees that your water heater page is about water heaters in Spring and The Woodlands.</li></ul>
<p>Our post on <a href="/blog/get-found-near-me-google/">getting found for “near me” searches</a> covers the profile side in more detail.</p>"""),

            ("Which keywords go on service pages, location pages and the blog", f"""<p>Here’s the page structure we’d build for a residential plumber covering The Woodlands, Spring, Conroe, Tomball and Kingwood. One primary keyword per page; close variants live on the same page instead of getting their own.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Page type</th><th>Example URL</th><th>Target keywords</th><th>Must include</th></tr></thead>
<tbody>
<tr><td>Home</td><td>/</td><td>plumber the woodlands, plumbing company + main towns</td><td>Phone, license number, top services, reviews</td></tr>
<tr><td>Emergency</td><td>/emergency-plumber/</td><td>emergency plumber, 24 hour plumber, burst pipe repair</td><td>Real hours, shutoff steps, response times</td></tr>
<tr><td>Service</td><td>/water-heater-replacement/</td><td>water heater replacement, installation, no hot water</td><td>Options, price range, financing, FAQs</td></tr>
<tr><td>Service</td><td>/slab-leak-repair/</td><td>slab leak detection, slab leak repair</td><td>Symptoms, repair options, process photos</td></tr>
<tr><td>Cost page</td><td>/repipe-cost/</td><td>repipe cost, how much to repipe a house</td><td>Ranges, what changes price, timeline</td></tr>
<tr><td>Location</td><td>/plumber-spring-tx/</td><td>plumber spring tx, plumbing spring tx</td><td>Local jobs, neighborhoods, a local review</td></tr>
<tr><td>Spanish</td><td>/es/plomero/</td><td>plomero, fuga de agua, calentador de agua</td><td>Spanish phone line, same depth as English</td></tr>
<tr><td>Blog</td><td>/blog/check-for-water-leak/</td><td>how to check for a water leak, why is my water bill high</td><td>Steps, photos, link to the service page</td></tr>
</tbody></table></div>
<!--fig:servicepage-->
<p>Every blog post should link to the service page it supports, and every service page should link to the location pages that mention it. Building that structure is most of what our <a href="/services/web-design-seo-pr/">web design and SEO team</a> does for contractors.</p>"""),

            ("Plumbing SEO tips for measuring keywords in Search Console", f"""<p>Rankings screenshots don’t pay bills. Search Console shows which searches put you in front of people and which pages they clicked, for free. The {SRC['gsc']} reports clicks, impressions, CTR and average position, which Google defines as the position of the topmost result from your site.</p>
<!--fig:gsc-->
<p>Search Console supports regex filters on queries and pages; per {SRC['regex']}, Google uses RE2 syntax and matching is case-sensitive unless you start with (?i). A filter like (?i)woodlands|spring|conroe|tomball|kingwood shows every town-modified search in one view. Run a second one for (?i)slab|repipe|water heater|sewer to see whether your high-ticket pages are gaining impressions.</p>
<p>Search Console stops at the click, so pair it with call tracking on the site. Our guide to <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking</a> covers that, and our <a href="/blog/local-seo-contractors-houston/">local SEO guide for Houston contractors</a> covers the Business Profile side. Give new pages three to six months before you judge them.</p>
<p>Before you close this tab, save those two regex filters in Search Console and write down the impressions for your water heater, slab leak, repipe and sewer pages. Check the same four numbers in 90 days. If you also run Google Ads, the search terms report there is keyword research you’ve already paid for, since it lists the exact phrases people typed before they clicked. Our free <a href="/contact/">Ad Spend Leak Check</a> starts with that report. We record a 10-minute video, sent within 48 hours, flagging the terms that spent money without producing a call, which are often the same phrases that deserve an organic page instead.</p>"""),
        ],
        "faq": [
            ("What are the best keywords for plumbers?", "The best keywords combine a service with a place: water heater replacement Spring TX, slab leak repair The Woodlands, emergency plumber Conroe. High-ticket services like repipes, slab leaks, sewer lines and water heaters usually earn the most per booked job. Emergency keywords bring volume but are mostly won in the map pack and Local Services Ads rather than with blog content."),
            ("How do plumbers do local SEO?", "Local SEO for plumbers starts with a complete Google Business Profile: the Plumber category, accurate service areas, listed services, photos and a steady flow of reviews. On the website, build one strong page per major service, a few location pages with genuinely local content, and helpful guides that link to those service pages. Track progress in Search Console and with call tracking."),
            ("Should I put 'near me' on my plumbing website?", "Mostly no. Google reads near me as a request to use the searcher's location, so distance and your Business Profile do the work. Repeating near me in headings or footers reads badly and adds little. Use town names naturally on service pages, keep service areas accurate and keep reviews coming. Never add near me or a city name to your business name."),
            ("Do I need a separate page for every city I serve?", "Only for towns where you can write something specific: jobs you've done there, neighborhoods, response times, local photos and a local review. Google's spam policies treat near-identical city pages that funnel visitors to one page as doorway abuse. For a shop north of Houston, five or six strong location pages usually beat twenty thin ones."),
            ("How long does plumbing SEO take to work?", "New service pages usually take three to six months to settle in rankings, longer in competitive areas like central Houston. Business Profile changes and new reviews can move map pack results sooner. Watch impressions in Search Console first, since they rise before clicks and calls. If impressions stay flat after six months, the page or the keyword choice needs work."),
            ("What plumbing keywords should I use in Spanish?", "Start with plomero, plomero cerca de mí, plomero en Houston, plomería, fuga de agua, calentador de agua and destapar drenaje, and have a native speaker in the trade review the wording. Put them on dedicated Spanish pages with their own URLs instead of a translate widget, and only promote those pages if someone answers the phone in Spanish."),
        ],
        "figures": {
            "value": {
                "type": "bars",
                "title": "Relative job value by keyword cluster",
                "sub": "Our rough view for a residential shop, not search volume",
                "items": [
                    ["Repipe", 100, "Very high"],
                    ["Sewer line", 85, "High"],
                    ["Slab leak", 70, "High"],
                    ["Water heater", 60, "High"],
                    ["Emergency repair", 35, "Medium"],
                    ["Drain cleaning", 20, "Lower"],
                ],
                "highlight": [0, 2],
                "note": "Illustrative ranges",
                "alt": "Bar chart of relative job value for plumbing SEO keywords in Houston, from repipe to drain cleaning",
                "caption": "Rank keywords by what a booked job is worth to you, then check volumes in your own tools.",
            },
            "towns": {
                "type": "map",
                "title": "Suburb modifiers worth a location page",
                "sub": "Towns north of Houston where local plumber searches add a place name",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Kingwood", "Magnolia"],
                "alt": "Map of The Woodlands, Spring, Conroe, Tomball, Kingwood and Magnolia for local plumber SEO keywords",
                "caption": "Build a page only for towns where you can show real local jobs and response times.",
            },
            "servicepage": {
                "type": "checklist",
                "title": "What a plumbing service page needs",
                "sub": "Use this for water heater, slab leak, repipe and sewer pages",
                "items": [
                    "One primary keyword in the title and H1",
                    "Click-to-call button above the fold",
                    "Options explained in plain words",
                    "Honest price range and what changes it",
                    "Photos from real local jobs",
                    "Towns served, named naturally",
                    "Texas license number visible",
                    "FAQs written from real customer calls",
                    "Links to related guides and location pages",
                ],
                "alt": "Checklist for a plumbing service page built around plumbing SEO keywords for Houston homeowners",
                "caption": "A thin paragraph on a services page won’t rank for a high-ticket term; a full page can.",
            },
            "gsc": {
                "type": "steps",
                "title": "Tracking plumbing keywords in Search Console",
                "sub": "A monthly 20-minute routine",
                "steps": [
                    ["Open Performance", "Search results report, last 3 months, compared to the previous period."],
                    ["Filter town queries", "Custom regex on queries for your towns, case-insensitive."],
                    ["Filter service queries", "A second regex for slab, repipe, water heater and sewer."],
                    ["Check pages", "Click each service page to see which searches it shows for."],
                    ["Match to calls", "Line up rising pages with call tracking data before adding content."],
                ],
                "alt": "Five steps to measure plumbing SEO keywords for Houston towns in Google Search Console",
                "caption": f"Based on {A('https://support.google.com/webmasters/answer/7576553?hl=en', 'Google’s performance report help')}; impressions usually rise before clicks do.",
            },
        },
    },
]
