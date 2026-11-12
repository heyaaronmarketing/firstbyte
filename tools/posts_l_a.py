"""Batch 12: water damage restoration company marketing in Houston.

Research: WordStream/LocaliQ 2026 Google Ads benchmarks (Home & Home Improvement median CPC $8.33, cost per lead
$90.92, conversion rate 8.05%); Google's Local Services Ads category list (includes "Water damage services", no
separate restoration or mold category); TDLR mold program at-a-glance sheet (license types, 25 contiguous sq ft
notification threshold, five-day notice, 10-day certificate, 5,646 licensees FY25, fees); TDLR mold FAQ (no
assessment and remediation on the same project; CMDR only from a licensed remediator); TDLR update on SB 1255
(effective Sept. 1, 2025, repealed the supervised-employee exemption); TDI on when water damage and mold are covered
(sudden and accidental, floods excluded, mold can grow within a day); TDI home damage FAQ (temporary repairs OK,
photos first); TDI "Roofing and insurance: know the law" (contractors can't act as or advertise as public adjusters
on jobs they work, can't waive or absorb deductibles); IICRC WRT page; Cleanfax on the IICRC Certified Firm program
(liability insurance, code of ethics, locator listing, logo use); ANSI listing for IICRC S500 fifth edition (2021);
ABC13 on the February 2021 freeze (one Houston plumbing company took about 20,000 calls in a day vs. 500-700
normally); Utility Dive on Hurricane Beryl (more than 2.26 million CenterPoint customers lost power); BrightLocal
2026 Local Consumer Review Survey; Google Maps prohibited content policy.
Competitor/PAA phrasing read for "water damage restoration marketing", "restoration company marketing", "water
damage leads", "restoration google ads", "how to get water damage jobs", "restoration SEO".
Left out (couldn't verify): a published CPC figure specific to water damage keywords, any TDLR rule requiring license
numbers in mold advertising, and specific Texas rules on referral fees to plumbers or adjusters.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "ws": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream/LocaliQ 2026 Google Ads benchmarks"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "tdlr": A("https://www.tdlr.texas.gov/media/pdf/mold-assessors-and-remediators-at-a-glance.pdf", "TDLR’s mold program summary"),
    "tdlrfaq": A("https://www.tdlr.texas.gov/mld/mldfaq.htm", "TDLR’s mold FAQ"),
    "sb1255": A("https://www.tdlr.texas.gov/news/2025/09/17/tdlr-mold-program-update", "TDLR’s note on SB 1255"),
    "tdicov": A("https://agate.tdi.texas.gov/tips/when-are-water-damage-and-mold-covered-by-insurance.html", "the Texas Department of Insurance"),
    "tdifaq": A("https://www.tdi.texas.gov/CONSUMER/storms/home-damaged-faq.html", "TDI’s home damage FAQ"),
    "tdilaw": A("https://www.tdi.texas.gov/Consumer/storms/roofing-and-insurance-know-the-law.html", "TDI’s “know the law” page for contractors"),
    "wrt": A("https://iicrc.org/wrt/", "IICRC’s WRT page"),
    "cfirm": A("https://cleanfax.com/beyond-the-badge-what-the-iicrc-certified-firm-program-delivers-to-you/", "Cleanfax’s interview on the Certified Firm program"),
    "s500": A("https://webstore.ansi.org/Standards/IICRC/ANSIIICRCS5002021", "ANSI/IICRC S500"),
    "abc13": A("https://abc13.com/plumbing-company-gets-20000-calls-for-service-in-single-day/10362334/", "told ABC13"),
    "beryl": A("https://www.utilitydive.com/news/texas-restoration-efforts-underway-beryl-almost-3-million-without-power/720816/", "Utility Dive"),
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
}

L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    {
        "slug": "water-damage-restoration-marketing-houston",
        "title": "Water Damage Restoration Marketing in Houston: SEO, Google Ads & Local Services Ads for Restoration Companies",
        "seo_title": "Water Damage Restoration Marketing in Houston: SEO & LSAs",
        "desc": "How Houston water damage restoration companies get more jobs: Local Services Ads, emergency Google Ads, insurance claims, TDLR mold rules and 24/7 calls.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google Business Profile", "Google"],
        "art": "b4",
        "hero": "plumbing",
        "hero_alt": "Illustration of a burst pipe for water damage restoration marketing in Houston, The Woodlands and Katy",
        "related": ["local-services-ads-vs-google-ads-home-services", "roofing-marketing-houston-storm-season", "how-to-get-more-plumbing-service-calls-houston"],
        "sections": [
            (None, f"""<p>It’s 2:10 a.m. on the second night of a hard freeze. A homeowner in Kingwood is standing in an inch of water in the hallway because a pipe in the attic split when it thawed. She types “water damage restoration near me” with one hand and calls the first company that looks real. If that phone goes to voicemail, she calls the second one. You never find out she existed.</p>
<p>Restoration is an emergency business with home-improvement click prices. The closest category in the {SRC['ws']}, Home &amp; Home Improvement, has a median cost per click of <b>$8.33</b> and a median cost per lead of <b>$90.92</b>, and emergency water terms usually sit above that median. Houston makes it harder, because demand arrives in spikes. During the February 2021 freeze, one Houston-area plumbing company {SRC['abc13']} it took about 20,000 service calls in a single day against a normal 500 to 700. When Hurricane Beryl came ashore in July 2024, more than 2.26 million CenterPoint customers lost power, per {SRC['beryl']}, and the roof leaks and soaked drywall followed.</p>
<p>The companies that win those weeks set things up months earlier. Here’s the setup we’d build for a restoration company covering Houston, The Woodlands, Spring, Katy, Cypress, Sugar Land, Pearland and Conroe.</p>
<!--fig:houston-->"""),

            ("Rank for water damage searches", f"""<p>To rank for water damage searches in Houston, you need a Google Business Profile with the right category and a real local address, plus one page per emergency type and one page per area you actually serve.</p>
<ul>
<li><b>Primary category:</b> set it to “Water damage restoration service.” Add secondary categories only for work you do in-house, such as fire damage or mold remediation if you hold the TDLR license (more on that below).</li>
<li><b>One page per emergency:</b> burst pipe cleanup, ceiling leak, flooded carpet, water heater leak, sewage backup cleanup, storm and roof leak water damage, commercial water damage. A homeowner with sewage in the tub isn’t searching the same words as one with a dripping light fixture.</li>
<li><b>Area pages with proof:</b> a Katy page needs Katy job photos and Katy reviews. One that swaps “Katy” for “Pearland” and changes nothing else ranks in neither. See our {L('/blog/power-of-local-landing-pages/', 'guide to local landing pages')}.</li>
<li><b>Answer the 2 a.m. questions:</b> will insurance cover this, how long does drying take, is the drywall ruined. Short, honest answers are what Google’s AI Overviews and ChatGPT pull from.</li>
<li><b>Hours:</b> only mark the profile open 24 hours if a person answers 24 hours.</li>
</ul>
<p>The map pack does most of the work in this category. Our {L('/blog/rank-in-google-map-pack-houston/', 'Houston map pack guide')} covers the ranking side in full.</p>"""),

            ("Use Local Services Ads for water damage", f"""<p>Yes, Google offers Local Services Ads for this work: “Water damage services” is on {SRC['lsa']}, and it’s usually the first paid channel we’d test for a restoration company with good reviews.</p>
<ul>
<li><b>You pay per lead, not per click.</b> A lead is a call or message from the ad. Leads that weren’t real customers (wrong service, spam, out of area) can be disputed for credit.</li>
<li><b>Only one category.</b> The list has no separate restoration, flood or mold category, so mold-only and fire-only work won’t get its own LSA. Build those pages for organic search and regular Google Ads instead.</li>
<li><b>Screening takes time.</b> Expect license, insurance and background checks before ads run, so start well before storm season. Our post on {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified')} explains the badge change.</li>
<li><b>Responsiveness affects ranking.</b> Missed LSA calls cost you twice: the lost job, and fewer impressions afterward.</li>
</ul>
<p>We compare the two ad types in detail in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}. For restoration, the short answer is to run both and compare cost per booked job.</p>"""),

            ("Run Google Ads with tight controls", f"""<p>Emergency water damage ads work when they’re built around phone calls, limited to the hours someone answers, and filtered hard with negative keywords.</p>
<ul>
<li><b>Keywords by emergency:</b> “water damage restoration Spring TX,” “burst pipe water cleanup,” “emergency water extraction,” “sewage backup cleanup Houston.” Group them so each ad matches its landing page.</li>
<li><b>Location settings:</b> in Campaign settings, under Locations, choose “Presence: People in or regularly in your included locations.” The default also reaches people merely interested in Houston.</li>
<li><b>Call assets and ad schedule:</b> add a call asset with call reporting on, and run ads only in hours a person answers. Nights that go to voicemail get paused.</li>
<li><b>Count calls over 60 seconds as conversions,</b> then import booked jobs from your CRM so bidding learns which calls turned into work. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers the setup.</li>
<li><b>A surge plan:</b> keep burst-pipe and storm ad groups written, approved and paused, and raise budgets the day the weather turns.</li>
</ul>
<p>Sample ad copy we’d start from (edit to what’s true for you):</p>
<div class="tbl"><table>
<thead><tr><th>Headline</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Burst Pipe? Crew Out in 60 Min</td><td>Water extraction and drying across north Houston. IICRC-certified techs. We document everything for your insurance claim.</td></tr>
<tr><td>Water Damage Help, 24/7</td><td>A real person answers, day or night. Moisture mapping, drying equipment and photo reports. Spring, The Woodlands, Conroe.</td></tr>
</tbody></table></div>
<p>Only promise a response time you hit nine times out of ten. Negatives are where most restoration accounts leak.</p>
<!--fig:negatives-->
<p>Our {L('/services/search-marketing/', 'search marketing team')} builds and runs these accounts, and our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} will help you set an opening budget.</p>"""),

            ("Work the insurance claim, inside Texas rules", f"""<p>Most of your customers are paying through homeowners insurance, so your marketing should explain the claim process without crossing the lines Texas draws for contractors.</p>
<p>Start with what’s covered. Per {SRC['tdicov']}, most homeowner and renter policies cover sudden and accidental water damage, usually not gradual leaks, and home policies don’t cover floods, which take a separate policy. TDI also tells homeowners that mold can start growing within a day after a leak. That one line is the most honest urgency message you have, and it belongs on your burst-pipe page.</p>
<p>A burst pipe in Sugar Land is usually a claim. Street flooding in Meyerland usually isn’t, unless the owner has flood coverage, so ask early whether the water came from inside or outside.</p>
<ul>
<li><b>Document like the adjuster is watching.</b> {SRC['tdifaq']} tells homeowners it’s generally OK to make temporary repairs, to take pictures before any work, and not to make permanent repairs until they’ve talked to their insurer. Your photo logs and moisture readings fit that advice exactly.</li>
<li><b>Don’t offer to handle the claim.</b> Per {SRC['tdilaw']}, Texas doesn’t allow a contractor to act as a public adjuster on claims for work they’re doing, or to advertise that they would.</li>
<li><b>Don’t waive the deductible.</b> The same page says it’s illegal for a contractor to offer to waive, rebate or absorb a policyholder’s deductible, and contracts of $1,000 or more involving an insurance settlement need a notice that the policyholder must pay it. “We’ll cover your deductible” in an ad is a liability.</li>
</ul>
<p>This isn’t legal advice. Have your attorney read your claim-related ad copy and contract language before you launch.</p>"""),

            ("Follow TDLR mold licensing rules", f"""<p>Mold assessment and mold remediation in Texas are licensed by the Texas Department of Licensing and Regulation (TDLR), and a water restoration company that advertises mold work needs the right license behind the ad.</p>
<ul>
<li><b>Separate licenses.</b> TDLR issues mold assessment technician, consultant and company licenses, and mold remediation contractor and company licenses, plus worker registrations, per {SRC['tdlr']}. The program had 5,646 licensees in fiscal 2025.</li>
<li><b>Thresholds and notice.</b> Projects under 25 contiguous square feet don’t require notice to TDLR. Above that, the license holder must notify TDLR at least five days before work begins, and a certificate of mold remediation is due within 10 days after completion.</li>
<li><b>No assessing and remediating the same job.</b> {SRC['tdlrfaq']} says a company may hold both licenses but can’t conduct both assessment and remediation on the same project. So “free mold testing and removal” from one company is a red flag, both to TDLR and to the customer who knows the rule.</li>
<li><b>Recent change.</b> SB 1255 took effect September 1, 2025 and repealed the provision that let license holders’ employees do mold work under supervision without their own credential, per {SRC['sb1255']}. Check with TDLR how that affects your crew.</li>
</ul>
<p>In practice, show your TDLR license numbers on mold pages and keep mold ad groups separate from water ones.</p>"""),

            ("Show IICRC certification where it matters", f"""<p>IICRC certification is the trust signal adjusters, property managers and informed homeowners look for, so it should appear in your ads, on your trucks and next to the call button.</p>
<p>The Water Damage Restoration Technician (WRT) course covers drying structures, water losses, sewer backflows and contamination such as mold, per {SRC['wrt']}, and the industry’s working standard for the job is {SRC['s500']} (fifth edition, 2021). A Certified Firm has to carry liability insurance and agree to the IICRC Code of Ethics, and in return can use the IICRC logo on websites, cards and vehicles and gets a listing in the IICRC locator, per {SRC['cfirm']}.</p>
<p>Make it specific. “Every lead tech holds WRT, and we dry to the S500 standard” beats a logo in the footer.</p>"""),

            ("Build referral partners: plumbers, agents and adjusters", f"""<p>Ads catch the homeowner who searches. Partners catch the one who calls someone else first, which in a burst-pipe emergency is usually a plumber.</p>
<ul>
<li><b>Plumbers.</b> The plumber stops the leak and then walks into a wet room. Give nearby plumbing companies a direct dispatch line and send plumbing problems you find their way. Our post on {L('/blog/how-to-get-more-plumbing-service-calls-houston/', 'plumbing service calls')} shows what plumbers are chasing.</li>
<li><b>Insurance agents.</b> Independent agents in The Woodlands, Cypress and Sugar Land get the panicked first call. Leave them a “first hour” card.</li>
<li><b>Adjusters.</b> They care about documentation and dry times. Send clean photo reports and moisture logs on every job.</li>
<li><b>Property managers.</b> A priority-response agreement turns one apartment manager into dozens of jobs a year.</li>
</ul>
<p>Keep any referral arrangement in writing, and ask your attorney before paying anyone for leads tied to insurance claims.</p>"""),

            ("Build reviews the right way", f"""<p>Reviews decide which restoration company a stressed homeowner calls, and they need to be recent. Per {SRC['bl']}, 68% of consumers will only use a business rated four stars or higher, 31% want 4.5 or higher, and 74% only care about reviews from the last three months.</p>
<ul>
<li><b>Ask when the drying equipment leaves.</b> That’s when relief peaks. The rebuild can take weeks, so don’t wait for it.</li>
<li><b>Same link, every customer.</b> {SRC['gpol']} bans incentives for reviews and bans selectively asking only happy customers.</li>
</ul>
<p>A simple text that works: “Hi [name], this is [tech] from [company]. Your home is dry and the equipment is out. If we did right by you, would you leave a short review? [link]. Thanks for trusting us with your house.” More templates are in our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')}.</p>"""),

            ("Answer every call, 24 hours a day", f"""<p>In restoration, the company that answers first and gives an arrival time usually gets the job, so 24/7 live answering matters more than any ad setting.</p>
<ul>
<li><b>Live answering overnight,</b> by your own on-call rotation or a service trained to book jobs.</li>
<li><b>A two-minute intake script:</b> where the water came from, how long it’s been, how many rooms, whether power is on, whether they’ve called insurance, and the address. Then give a window.</li>
<li><b>Forms and LSA messages answered in five minutes.</b> Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up system.</li>
</ul>
<p>Listen to ten recorded calls a week. You’ll find more lost revenue there than in the ad account.</p>"""),

            ("What a Houston restoration company should spend", f"""<p>There’s no honest single number. For a one-location residential restoration company, this is an illustrative starting point. Treat the ranges as examples; they aren’t quotes or benchmarks.</p>
<div class="tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Google Ads (search, call-focused)</td><td>$3,000 to $8,000</td><td>More during freezes and storms; set a surge cap in advance</td></tr>
<tr><td>Local Services Ads</td><td>$1,500 to $4,000</td><td>Pay per lead; dispute bad leads weekly</td></tr>
<tr><td>Local SEO and website</td><td>$1,000 to $2,500</td><td>Emergency pages, area pages, Business Profile</td></tr>
<tr><td>24/7 answering</td><td>$300 to $1,500</td><td>Depends on call volume and whether it books jobs</td></tr>
<tr><td>Referral partner outreach</td><td>$200 to $800</td><td>Leave-behinds, lunches, a dispatch line</td></tr>
</tbody></table></div>
<!--fig:budget-->
<p>Fix answering and reviews first. Paying $90 or more for a lead that hits voicemail is the most expensive mistake in this business.</p>"""),

            ("Your first 90 days", f"""<p>A realistic order of work if you’re starting with a basic site and a thin Business Profile. By day 90 you should see cost per booked job by channel before the next freeze.</p>
<!--fig:plan-->"""),

            ("Mistakes we see", f"""<ul>
<li><b>Buying shared leads during a storm</b> and racing four other companies to the same homeowner. Own your demand where you can.</li>
<li><b>One “services” page</b> for water, fire, mold and rebuild. It ranks for none of them.</li>
<li><b>Running ads overnight to voicemail.</b> You pay for the click and the competitor gets the job.</li>
<li><b>Mold claims you can’t back up,</b> or an ad that offers testing and removal from the same company.</li>
<li><b>Insurance promises.</b> “We work with all insurance” is fine. “We’ll handle your claim” or “no deductible” isn’t.</li>
<li><b>Judging campaigns by calls.</b> Plenty of calls are shoppers or jobs too small for a truck. Track booked jobs.</li>
</ul>"""),

            ("Measure what matters", f"""<p>Track a short list every month: answered call rate (overnight separately), cost per booked job by channel, average job value for mitigation and rebuild, review count and rating over the last 90 days, and share of revenue from referral partners. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} walks through the setup, and our {L('/services/web-design-seo-pr/', 'web design and SEO team')} builds the emergency pages.</p>
<p>If you want a plan built around your service area, crews and the storms you can’t predict, <a href="/contact/">get in touch</a> and a senior strategist will put one together.</p>"""),
        ],
        "faq": [
            ("How much should a water damage restoration company spend on Google Ads in Houston?",
             "Plan on at least $3,000 a month in search spend to get useful data, with room to double it during freezes and hurricanes. The closest benchmark category, Home and Home Improvement, has a median cost per lead around $91, and emergency water terms often run higher. Judge spend by cost per booked job, not cost per call."),
            ("Are Local Services Ads worth it for water damage restoration?",
             "Usually, yes. Google lists Water damage services as a Local Services Ads category, you pay per lead instead of per click, and you can dispute invalid leads. They work best for companies with strong recent reviews and live 24/7 answering, because missed calls hurt how often the ads show. There’s no separate category for mold or fire work."),
            ("Do I need a license to do mold remediation in Texas?",
             "Yes. The Texas Department of Licensing and Regulation licenses mold assessors and remediators, and projects of 25 contiguous square feet or more require notice to TDLR at least five days before work starts. One company can’t perform both the assessment and the remediation on the same project, so don’t advertise testing and removal as one package."),
            ("Can a restoration company help with the insurance claim in Texas?",
             "You can document the loss, share moisture readings and photos, and explain the process. Texas doesn’t allow a contractor to act as a public adjuster on a job they’re working, or to advertise that service, and it’s illegal to offer to waive or absorb the policyholder’s deductible. Have an attorney review claim-related ads and contracts."),
            ("How do restoration companies get more water damage jobs?",
             "Answer every call around the clock, rank in Google Maps with a Water damage restoration service profile and recent reviews, and run Local Services Ads and call-focused Google Ads with strict negatives. Build referral relationships with plumbers, insurance agents and property managers, and have storm and freeze campaigns ready to switch on the day the weather turns."),
        ],
        "figures": {
            "houston": {
                "type": "stats",
                "title": "Why Houston restoration demand spikes",
                "stats": [["20,000", "calls in one day at one plumber, Feb. 2021 freeze"], ["2.26M+", "CenterPoint customers out after Beryl"], ["$8.33", "median CPC, home improvement ads"], ["$90.92", "median cost per lead, same category"]],
                "note": "Sources: ABC13, Utility Dive, WordStream/LocaliQ 2026",
                "alt": "Stats on freeze and hurricane demand and Google Ads costs for water damage restoration marketing in Houston",
                "caption": f"From {SRC['abc13'].replace('told ABC13', 'ABC13')}, {SRC['beryl']} and the {SRC['ws']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for restoration ads",
                "sub": "Add these before launch, then check search terms weekly",
                "items": ["DIY: how to, diy, yourself, youtube", "Rentals: rent, rental, dehumidifier rental", "Products: shop vac, wet vac, fan, home depot", "Jobs: jobs, hiring, salary, course, certification", "Insurance only: claim denied, lawyer, attorney", "Out of scope: car, boat, phone water damage", "Wrong service: plumber only if you don’t plumb", "Free: free, cheap, cost estimator"],
                "alt": "Checklist of negative keywords for water damage restoration Google Ads in Houston and The Woodlands",
                "caption": "“Certification” can be a good term for a training school and a bad one for you. Know which you are.",
            },
            "budget": {
                "type": "bars",
                "title": "Example monthly marketing mix",
                "sub": "Single-location residential restoration company, midpoint of each range",
                "items": [["Google Ads", 5500, "$5,500"], ["Local Services Ads", 2750, "$2,750"], ["Local SEO and website", 1750, "$1,750"], ["24/7 answering", 900, "$900"], ["Referral outreach", 500, "$500"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of an example monthly marketing budget for a water damage restoration company in Houston",
                "caption": "Midpoints of the illustrative ranges above. Storm months will look very different.",
            },
            "plan": {
                "type": "steps",
                "title": "First 90 days for a restoration company",
                "sub": "In this order, before the next freeze or storm",
                "steps": [["Days 1-15", "Live 24/7 answering, call tracking, intake script."], ["Days 16-30", "Business Profile category, photos, review texts."], ["Days 31-45", "Emergency and area pages, Local Services Ads."], ["Days 46-60", "Call-focused search campaigns, negatives, surge ad groups."], ["Days 61-90", "Plumber and agent outreach, booked-job imports."]],
                "note": "Illustrative example",
                "alt": "Five-step first 90 days marketing plan for a water damage restoration company in Houston and The Woodlands",
                "caption": "Phone first, then visibility, then paid traffic. Reversing the order wastes the ad budget.",
            },
        },
    },
]
