"""Batch 9: electrician marketing for residential and light commercial electrical contractors in Houston and The
Woodlands, and house cleaning / maid service marketing in Houston.

Research: TDLR electrician compliance guide (TECL on both sides of vehicles, 2-inch lettering, license number on
proposals, invoices and contracts); 16 TAC 73.51 via Justia (name and license number on advertising and business cards,
exemptions for national TV and phone solicitation); City of Houston generator permit page (permits issued only to
registered master electricians, plan review and inspection required); Utility Dive on Hurricane Beryl (2.26 million
CenterPoint customers out at peak, about 80% of its customers); Texas Tribune on Winter Storm Uri (Feb. 15-18, 2021,
largest controlled blackout in U.S. history per federal regulators); FOX 26 Houston, May 2021 (generator demand after the
freeze, about six months order-to-install, standby units from around $10,000); ABC13, Sept. 2024 (CenterPoint automatic
transfer switch approval backlog, up to a month per CenterPoint, documents showing waits near eight weeks); IRS page on
the 30C refueling property credit (30% up to $1,000 per port, eligible tracts, property placed in service through June
30, 2026); Google Local Services Ads category list (Electricians; House cleaning services); Google Business Profile
service-area rules (remove address, up to 20 areas, no radius, about 2 hours' drive).
Cleaning post: Texas Comptroller publication 94-111 (maid services collect sales tax, including on cleaning a home);
BLS OEWS May 2023 for maids and housekeeping cleaners (Houston metro 15,270 jobs, $14.49 mean hourly); Census QuickFacts
for Houston city (42.0% owner-occupied, 47.2% speak a language other than English at home, 44.1% Hispanic or Latino);
Texas State Law Library on security deposit refunds (30 days, no deductions for normal wear and tear); Nextdoor's guide
to recommendations (free business page, Faves, Nextdoor's own survey stats); Jon Loomer on Meta special ad categories
(Employment restrictions); Google Maps prohibited content policy on reviews.
Competitor/PAA phrasing read for "electrician marketing", "how to get more electrical leads", "electrician google ads",
"generator installer marketing", "house cleaning business marketing", "how to get more cleaning clients",
"maid service marketing ideas", "cleaning business google ads".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # electrician post
    "tdlr": A("https://www.tdlr.texas.gov/electricians/compliance-guide.htm", "TDLR’s electrician compliance guide"),
    "tac": A("https://regulations.justia.com/states/texas/title-16/part-4/chapter-73/section-73-51", "16 TAC §73.51"),
    "cohgen": A("https://www.houstonpermittingcenter.org/hpwcode1118", "City of Houston’s generator permit page"),
    "cohev": A("https://www.houstonpermittingcenter.org/hpwcode1056", "its own permit type for EV charging outlets"),
    "beryl": A("https://www.utilitydive.com/news/texas-restoration-efforts-underway-beryl-almost-3-million-without-power/720816/", "Utility Dive"),
    "uri": A("https://www.texastribune.org/2026/01/29/texas-winter-storm-uri-anniversary-power-grid-ercot/", "the Texas Tribune"),
    "fox26": A("https://www.fox26houston.com/news/texans-rush-to-get-back-up-generators-installed-at-homes", "FOX 26 Houston"),
    "ats": A("https://abc13.com/post/centerpoint-blamed-after-several-houstonian-households-have-generator-install-delays-ahead-francine/15283375/", "ABC13 reported"),
    "irs30c": A("https://irs.gov/zh-hant/credits-deductions/alternative-fuel-vehicle-refueling-property-credit-for-individuals", "the IRS page on the credit"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "sab": A("https://support.google.com/business/answer/9157481", "Google’s service-area rules"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    # cleaning post
    "comp": A("https://comptroller.texas.gov/taxes/publications/94-111.php", "Texas Comptroller’s cleaning and janitorial services publication"),
    "bls": A("https://www.bls.gov/oes/2023/May/oes372012.htm", "BLS occupational data for May 2023"),
    "census": A("https://census.gov/quickfacts/fact/table/houstoncitytexas,US/RHI225220", "Census QuickFacts"),
    "deposit": A("https://guides.sll.texas.gov/landlord-tenant-law/security-deposit-refunds", "Texas State Law Library’s guide to deposit refunds"),
    "nd": A("https://business.nextdoor.com/en-us/blog/small-business-guide-to-getting-nextdoor-recommendations", "Nextdoor’s own guide to recommendations"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
}

ELEC = "/blog/electrician-marketing-houston-the-woodlands/"
CLEAN = "/blog/house-cleaning-business-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: electricians
    {
        "slug": "electrician-marketing-houston-the-woodlands",
        "title": "Electrician Marketing in Houston and The Woodlands: Getting the Calls Worth Taking",
        "seo_title": "Electrician Marketing in Houston & The Woodlands",
        "desc": "Electrician marketing for Houston and The Woodlands: Local Services Ads, Google Ads for panels, generators and EV chargers, TDLR license rules, GBP, reviews.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Google"],
        "art": "b2",
        "hero": "bolt",
        "hero_alt": "Illustration of a lightning bolt for electrician marketing in Houston, The Woodlands, Spring and Conroe",
        "related": ["hvac-marketing-houston-the-woodlands", "how-to-get-more-plumbing-service-calls-houston", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>First week of June. The forecast shows something spinning in the Gulf, and by Wednesday afternoon your office has taken nine calls. Six want a standby generator quote “before it gets here.” One is a breaker that keeps tripping in a 1980s house in Kingwood. One is a property manager with a dead parking lot light in Spring. The last one asks whether you install Tesla chargers, and nobody is sure what to tell him about the tax credit.</p>
<p>Three weeks later the storm misses, the generator callers go quiet, and you’re back to waiting on the phone.</p>
<p>Electrician marketing in Houston and The Woodlands comes down to two jobs. The first is owning the everyday service searches (“electrician near me,” “breaker keeps tripping”) through Google Maps, Local Services Ads and reviews, so the phone rings in every season. The second is building demand for the high-ticket project work, mainly panel upgrades, generators, EV chargers and rewiring, before customers are panicking, and showing up first when they are.</p>
<p>This is how we’d set it up for a residential or light commercial shop with two to fifteen trucks, with the actual settings and the Texas rules that apply.</p>"""),

            ("Know which electrical jobs you’re actually marketing", f"""<p>Most electrical contractor websites list 30 services in a grid and treat them all the same. Your margins don’t. Before you spend a dollar, sort your work into buckets, because each one gets found differently.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Job type</th><th>How the customer searches</th><th>What wins it</th></tr></thead>
<tbody>
<tr><td>Service and repair calls</td><td>“electrician near me,” “outlet not working,” “breaker keeps tripping,” often on a phone, often today</td><td>Map pack position, reviews, answering the phone, LSA</td></tr>
<tr><td>Panel upgrades and replacements</td><td>“panel upgrade cost,” “200 amp service upgrade,” “replace electrical panel Spring TX”</td><td>A page with honest price ranges, photos of your panel work, financing</td></tr>
<tr><td>Standby generators</td><td>“whole home generator installer,” “Generac dealer near me,” spikes after outages</td><td>Being visible before hurricane season, a clear timeline, dealer credentials</td></tr>
<tr><td>EV chargers</td><td>“level 2 charger installation,” “Tesla wall connector install”</td><td>A dedicated page, fast quotes by photo, current incentive info</td></tr>
<tr><td>Rewiring and older homes</td><td>“rewire house cost,” “aluminum wiring,” “old house electrical inspection”</td><td>Trust content, inspection offers, realtor relationships</td></tr>
<tr><td>Light commercial</td><td>“commercial electrician Houston,” “parking lot lighting repair”</td><td>Outreach to property managers, a commercial page, response time</td></tr>
</tbody></table></div>
<p>Service calls keep trucks moving. Project work pays for the trucks. A marketing plan that only chases one of them gets lumpy fast, and in Houston the lumps come from the weather.</p>"""),

            ("Your TDLR license number is a marketing asset (and a legal requirement)", f"""<p>Start with the rule most shops half-follow. In Texas, the license isn’t just something you hang on the office wall.</p>
<p>Per {SRC['tdlr']}, a licensed electrical contractor has to put its name and license number on both sides of every business vehicle, in contrasting lettering at least two inches tall, with the number shown as “TECL” plus the number. Proposals, invoices and written contracts need your name, address, phone number and license number, and invoices and contracts also carry TDLR’s regulatory statement. Advertising is covered too. Under {SRC['tac']}, solicitation ads and business cards must include your name and license number, with narrow exceptions such as phone solicitations, where you have to give the number on request.</p>
<p>So put it everywhere a customer looks, on purpose:</p>
<ul>
<li>The site header or footer on every page, in text, not buried in an image.</li>
<li>Your Google Business Profile description (“Licensed Texas electrical contractor, TECL 12345”).</li>
<li>Your landing pages for Google Ads, next to the phone number.</li>
<li>Yard signs, door hangers, truck wraps and the quote PDF.</li>
</ul>
<p>Homeowners in The Woodlands and Sugar Land have all heard a story about a handyman doing electrical work. A visible TECL number, plus a line like “we pull the permit,” answers that worry before they voice it. It also matters in the City of Houston, where the {SRC['cohgen']} says electrical permits are only issued to registered master electricians, with plan review and an inspection required. Most unlicensed competitors can’t say “permitted and inspected.” You can.</p>"""),

            ("Google Business Profile for electricians: categories, service areas, photos", f"""<p>For most electrical shops, Google Maps is the biggest free source of service calls. Get the settings right first.</p>
<ul>
<li><b>Primary category:</b> Electrician. Then add secondary categories that match real work you want more of. Search the category list in your profile editor for the installation and repair options and pick only what you do.</li>
<li><b>Service area:</b> most electricians don’t have customers visit the shop, so per {SRC['sab']} you remove the address and list service areas instead. You get up to 20, defined by city or ZIP code, never a radius, and Google says the whole area shouldn’t stretch past about two hours of driving from your base. For a shop in Conroe, that might be The Woodlands, Spring, Montgomery, Magnolia, Willis, Tomball and the ZIP codes in between.</li>
<li><b>Services:</b> fill in the services list with plain descriptions. “Panel replacement and 200-amp service upgrades, permit and inspection included.”</li>
<li><b>Photos:</b> real panels you’ve replaced (the before shot of a scorched bus bar does more selling than any stock image), generator pads, your trucks with the TECL lettering showing, and your techs in uniform.</li>
<li><b>Hours:</b> if you offer emergency service, say so and mean it. If a 10 p.m. call goes to voicemail, don’t list 24 hours.</li>
</ul>
<p>Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest, including why proximity to the searcher limits how far a single profile can reach.</p>
<h3>Reviews that mention the job</h3>
<p>Reviews are the tiebreaker in the map pack and on LSA. The policy is simple. Per {SRC['gpol']}, you can’t pay or discount for reviews, can’t ask only the happy customers, and can’t discourage negative ones. Send every customer the same link.</p>
<p>The timing and wording are where shops differ. Send the request by text the same day the job closes, from the tech’s name if your software allows it:</p>
<p><i>“Hi Dana, this is Marcus from [Company]. Thanks for having us out to replace the panel today. If you have a minute, a Google review helps other folks in Spring find a licensed electrician: [link]. Any problems at all, call me directly at [number].”</i></p>
<p>Customers who describe the job (“replaced our Federal Pacific panel,” “installed a 22kW generator”) give future customers exactly what they’re scanning for. You can’t script what they say, but naming the job in your request makes it more likely. The {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("Local Services Ads for electricians", f"""<p>Electricians is one of the categories on {SRC['lsa']}, so you can run the pay-per-lead ads that sit above the regular search ads, with the Google Verified badge once you clear Google’s screening. You pay for a call or message rather than a click, and you can dispute leads that weren’t real customers, such as job seekers or wrong numbers.</p>
<p>LSA tends to be strongest for service calls, the “electrician near me” kind of search. It’s weaker for planned projects like generators, because you can’t write ad copy or send people to a generator landing page; the ad is basically your name, rating and phone number.</p>
<p>A few things make LSA work for electrical shops:</p>
<ol>
<li>Turn on only the job types you want. If you don’t do ceiling fan installs at a profit, switch them off.</li>
<li>Set ad scheduling to hours someone answers. LSA ranking leans on responsiveness, and missed calls cost you twice.</li>
<li>Mark every lead as booked or not in the app. It trains your own reporting, and it keeps you honest about what each lead is worth.</li>
<li>Get reviews coming in steadily. A shop with 200 reviews and a 4.8 will usually outrank one with 25 reviews on the same street.</li>
</ol>
<p>We compare the two ad types in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}, and the badge question in {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified')}.</p>"""),

            ("Google Ads for electricians: keywords, negatives and sample ads", f"""<p>Regular search ads are where you market the project work, because you control the keyword, the ad text and the page the click lands on. Split campaigns by job type so each gets its own budget:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Emergency and repair</td><td>electrician near me, emergency electrician, breaker keeps tripping, outlet sparking, power out in half my house</td><td>Service page with a call button at the top</td></tr>
<tr><td>Panels</td><td>electrical panel upgrade, 200 amp panel upgrade, replace breaker box, panel upgrade cost</td><td>Panel page with price ranges and permit info</td></tr>
<tr><td>Generators</td><td>whole house generator installation, standby generator installer, Generac installer The Woodlands</td><td>Generator page with timeline and financing</td></tr>
<tr><td>EV chargers</td><td>EV charger installation, level 2 charger install, Tesla wall connector installer</td><td>EV page with a photo-quote form</td></tr>
<tr><td>Rewiring</td><td>rewire house, aluminum wiring replacement, old house electrical upgrade</td><td>Rewiring page with an inspection offer</td></tr>
</tbody></table></div>
<p>Two settings matter more than most owners realize. Set location targeting to “Presence: People in or regularly in your included locations,” so you’re not paying for someone in Ohio researching panel brands. And track calls from ads as conversions, because most electrical customers call. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'guide to tracking calls and forms')} walks through it.</p>
<p>Then the negatives, which is where electrical accounts leak the most money:</p>
<!--fig:negatives-->
<p>Sample ad for the panel campaign, written to fit the character limits:</p>
<ul>
<li>Headline 1: Panel Upgrades in The Woodlands</li>
<li>Headline 2: Licensed TECL Contractor</li>
<li>Headline 3: Permit and Inspection Included</li>
<li>Description: Upfront pricing on 200-amp upgrades and panel replacements. Financing available. Same-week estimates in Spring, Conroe and Magnolia.</li>
</ul>
<p>Read the search terms report every week for the first month and add negatives as you go. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a sense of click costs before you set budgets, and {L('/services/search-marketing/', 'our search marketing team')} runs this for shops that would rather be on a job site.</p>"""),

            ("Generators and hurricane season: market before the storm", f"""<p>No product in Houston electrical work swings harder with the news than standby generators, and the swings have names.</p>
<!--fig:storms-->
<p>Winter Storm Uri hit Feb. 15 to 18, 2021, in what federal regulators called the largest controlled blackout in U.S. history, per {SRC['uri']}. That May, {SRC['fox26']} reported one Houston generator company had fielded about 10,000 inquiries since February, with roughly six months from order to install and whole-home units starting around $10,000. Then Hurricane Beryl came ashore on July 8, 2024, and at the peak more than 2.26 million CenterPoint customers lost power, about 80% of its customers, according to {SRC['beryl']}.</p>
<p>After Beryl, the bottleneck moved. In September 2024, {SRC['ats']} that CenterPoint, which reviews and approves automatic transfer switches before a generator can be connected, had a backlog of applications. CenterPoint told customers to allow up to a month, and documents the station reviewed showed average waits near eight weeks. One family in the story had a generator sitting installed and unusable.</p>
<p>What that means for your marketing:</p>
<ul>
<li><b>Sell generators in the off-season.</b> Run your strongest generator campaigns from January through May, with messages like “Get installed before June 1.” Atlantic hurricane season runs June 1 to November 30, and the people who wait for a named storm are the ones who end up on a waitlist.</li>
<li><b>Show the real timeline.</b> Put the steps on your generator page, including utility approval and the city permit. Customers who know it takes weeks are calmer, and calmer customers leave better reviews.</li>
<li><b>Have a storm mode ready.</b> Build an ad group and landing page now that says you’re taking generator consultations and gives the current lead time. Switch it on the afternoon a storm is named. Turn it off when the inquiries stop converting.</li>
<li><b>Market maintenance.</b> Every generator you install is a yearly service visit, and the spring “test it before the season” reminder is one of the easiest emails you’ll send.</li>
</ul>
<!--fig:generator-->
<p>Freezes count too. A February cold snap pulls the same searches as a hurricane, smaller and shorter, so keep the generator campaign live with a modest budget all year rather than off entirely.</p>"""),

            ("EV chargers: update your pages for the end of the federal credit", f"""<p>Plenty of electrician websites still say “get 30% back with the federal tax credit” on their EV charger page. Check yours.</p>
<p>The federal 30C credit covered 30% of the cost of a home charger, up to $1,000 per charging port, and only in eligible low-income or non-urban census tracts. Per {SRC['irs30c']}, it applies to property placed in service through June 30, 2026. A charger installed today doesn’t qualify, and a page that implies otherwise is the kind of thing that turns into a bad review.</p>
<p>The demand doesn’t depend on the credit, though. People who buy an EV in Katy or Cypress still need a 240-volt circuit in the garage, and many need a panel upgrade to support it. That combined job is what we’d market:</p>
<ul>
<li>A dedicated EV page per charger type you install, with a “text us photos of your panel and garage” quote option. Photo quotes cut a site visit out of a small job.</li>
<li>Keyword targeting on charger brand plus “install” or “installer.”</li>
<li>A clear note when a panel upgrade may be needed, so the bigger quote doesn’t feel like an upsell.</li>
<li>Permit language. The City of Houston has {SRC['cohev']}, and saying you handle it beats leaving the customer to wonder.</li>
</ul>
<p>New-construction builders in Bridgeland and Sienna are worth a referral conversation too. Their buyers ask who to call.</p>"""),

            ("Service-area pages that rank in Spring, Katy and Sugar Land", f"""<p>One profile won’t rank everywhere you drive. Location pages on your website help fill the gaps, as long as each one is actually about that place.</p>
<!--fig:map-->
<p>A thin page that swaps the city name into the same 300 words doesn’t help anyone. A useful one includes:</p>
<ul>
<li>The neighborhoods you work in (Grogan’s Mill and Panther Creek in The Woodlands, Cinco Ranch in Katy, First Colony in Sugar Land) and the kind of housing stock there.</li>
<li>Photos and short write-ups of recent jobs in that area, with the customer’s permission.</li>
<li>Reviews from customers in that city.</li>
<li>Permit notes. The City of Houston, unincorporated Harris and Montgomery County, and suburban cities each handle electrical permits their own way, and naming the right office shows you’ve worked there.</li>
<li>Your typical arrival window from your shop.</li>
</ul>
<p>Older homes inside the Loop and in established suburbs like Kingwood and Clear Lake bring rewiring, panel replacement and insurance-driven inspection work. Newer master-planned communities bring EV chargers, generator pads and ceiling fan and lighting jobs in homes where the builder ran minimum circuits. Write each page for what you actually do there. The {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} goes deeper.</p>"""),

            ("Financing and membership plans close the big tickets", f"""<p>A $1,200 repair is a decision. A $14,000 generator or a $3,500 panel upgrade is a household budget conversation, and the shop that offers monthly payments often wins it even at a higher price.</p>
<p>On financing, our advice is mostly about presentation:</p>
<ul>
<li>Show a “from $X per month” figure on the generator and panel pages, from whatever lender you use, with the lender’s required disclosures.</li>
<li>Have techs mention financing at the estimate, not after the customer flinches.</li>
<li>Put the pre-qualification link in the follow-up text that goes out with the quote.</li>
</ul>
<p>Membership plans are the other underused tool. HVAC and plumbing companies have run them for years (it’s a model we’ve seen up close working with Weiss Air Conditioning &amp; Plumbing). For an electrician, a plan might bundle a yearly safety inspection, generator maintenance, priority scheduling and a discount on repairs. The marketing value isn’t the fee. It’s that members call you first for the next job instead of searching, and every inspection visit creates a list of future work.</p>
<p>If you already do HVAC or plumbing alongside electrical, our {L('/blog/hvac-marketing-houston-the-woodlands/', 'HVAC marketing playbook')} covers the plan structure in more detail.</p>"""),

            ("What to spend and what to track", f"""<p>Here’s an illustrative monthly starting point for a shop with four to eight trucks in north Houston. These ranges are examples from how we’d build a plan, not quotes or benchmarks.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Local Services Ads</td><td>$1,000 to $3,000</td><td>Service calls; scale with booked jobs</td></tr>
<tr><td>Google Ads search</td><td>$1,500 to $4,000</td><td>Panels, generators, EV; more generator budget January to May</td></tr>
<tr><td>Local SEO and service-area pages</td><td>$750 to $2,000</td><td>Pages, profile work, photos, review replies</td></tr>
<tr><td>Call tracking and review software</td><td>$100 to $400</td><td>Needed to judge everything above</td></tr>
</tbody></table></div>
<p>None of it works if calls go to voicemail. Route ad and LSA calls to a person, answer forms within five minutes, and listen to ten recorded calls a month; our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the follow-up sequence. Then track cost per booked job by campaign, not cost per lead. A generator lead that costs $150 and turns into a $14,000 install is cheap. A $40 lead for a single outlet swap that eats a two-hour drive from Conroe to Pearland isn’t. Set your goals by job type once you have three months of real data.</p>
<p>A first 90 days, roughly:</p>
<ol>
<li><b>Month one:</b> fix the profile, add TECL everywhere, build the panel, generator and EV pages, set up call tracking, start review requests.</li>
<li><b>Month two:</b> launch LSA for service calls and search campaigns for panels and generators, with the negative list from above.</li>
<li><b>Month three:</b> cut what isn’t booking, add two or three service-area pages, and set up the storm-mode campaign so it’s ready to switch on.</li>
</ol>
<p>If you’d like a senior strategist to build that plan around your trucks and your service area, <a href="/contact/">get in touch</a> and tell us what work you want more of.</p>"""),
        ],
        "faq": [
            ("How do electricians get more customers?",
             "Start with a complete Google Business Profile using Electrician as the primary category, accurate service areas and real job photos, then ask every customer for a review by text the same day. Add Local Services Ads for service calls and Google search ads for panel upgrades, generators and EV chargers, each sending traffic to its own page. Answer calls fast, because the first shop to pick up usually gets the job."),
            ("Do Texas electricians have to show their license number in ads?",
             "Yes. TDLR rules require electrical contractors to include their name and license number on advertising and business cards, with limited exceptions such as phone solicitations, where the number must be provided on request. Vehicles need the name and TECL number on both sides in letters at least two inches tall, and proposals, invoices and contracts must show the license number. Displaying it prominently also builds trust."),
            ("Are Local Services Ads worth it for electricians?",
             "Often, for service and repair calls. Electricians is a listed Local Services Ads category, you pay per lead instead of per click, and you can dispute leads that aren't real customers. LSA is less useful for planned projects like generators because you can't write custom ads or choose a landing page. Many shops run LSA for service calls and regular Google Ads for project work."),
            ("When should I advertise standby generator installation in Houston?",
             "Run your strongest generator campaigns from January through May, before hurricane season starts June 1. After big outages like Uri and Beryl, demand spiked and installs backed up for weeks or months, including utility transfer switch approvals. Keep a smaller campaign running year-round, have a storm-mode ad group ready to switch on when a storm is named, and show customers the real installation timeline."),
            ("Can I still advertise the federal tax credit for EV charger installation?",
             "Not for new installs. The federal 30C credit covered 30% of the cost up to $1,000 per charging port in eligible census tracts, but it applies only to property placed in service through June 30, 2026. Remove or update any website copy or ads that promise the credit. EV owners still need 240-volt circuits and sometimes panel upgrades, so the service is still worth marketing."),
        ],
        "figures": {
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for electrician Google Ads",
                "sub": "Add these before launch, then keep adding",
                "items": ["Jobs: jobs, hiring, apprentice, salary, union", "Training: school, course, exam, license test, CE hours", "DIY: how to, diy, wiring diagram, youtube", "Retail: home depot, lowes, amazon, for sale", "Parts: breaker part number, wire gauge chart", "Utility: CenterPoint outage map, report outage", "Portable: portable generator, rent generator", "Wrong trade: electrician tape, auto electrician"],
                "alt": "Checklist of negative keywords for electrician Google Ads in Houston and The Woodlands",
                "caption": "Outage and portable-generator searches spike after every storm and almost never book an install.",
            },
            "storms": {
                "type": "stats",
                "title": "Houston’s power outage history, in numbers",
                "stats": [["2.26M", "CenterPoint customers out at Beryl’s peak"], ["~80%", "of CenterPoint’s customers"], ["4 days", "Uri blackouts, Feb. 15 to 18, 2021"], ["~6 mo.", "generator order-to-install wait, spring 2021"]],
                "note": "Sources: Utility Dive, Texas Tribune, FOX 26 Houston",
                "alt": "Stats on Hurricane Beryl and Winter Storm Uri outages that drive generator demand for Houston electricians",
                "caption": f"From {SRC['beryl']}, {SRC['uri']} and {SRC['fox26']}.",
            },
            "generator": {
                "type": "steps",
                "title": "The standby generator timeline to show customers",
                "sub": "Put these steps on your generator page",
                "steps": [["Site visit and sizing", "Load calculation, location, gas supply check."], ["Quote and financing", "Written proposal with your license number."], ["Permit", "Pulled by the master electrician, plan review where required."], ["Utility approval", "Transfer switch review by the utility, which can take weeks."], ["Install and inspection", "Pad, gas, transfer switch, then inspection."], ["Startup and maintenance", "Walkthrough and a yearly service reminder."]],
                "alt": "Six-step standby generator installation timeline for Houston and The Woodlands electricians to share with customers",
                "caption": "Customers who see the steps up front are calmer when the utility approval takes a while.",
            },
            "map": {
                "type": "map",
                "title": "Where to build service-area pages",
                "sub": "Example for a shop based between The Woodlands and Spring",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Magnolia", "Tomball", "Montgomery", "Kingwood", "Cypress"],
                "note": "Illustrative example",
                "alt": "Map of Houston-area service-area pages for an electrician based in The Woodlands, including Spring, Conroe and Kingwood",
                "caption": "Build pages where you’ve done real jobs and can arrive on time.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: house cleaning
    {
        "slug": "house-cleaning-business-marketing-houston",
        "title": "House Cleaning Business Marketing in Houston: How to Get More Recurring Clients",
        "seo_title": "House Cleaning Business Marketing in Houston",
        "desc": "How Houston house cleaning and maid services get more recurring clients: Google Business Profile, Nextdoor, instant quotes, reviews, move-outs, retention.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Nextdoor", "Facebook"],
        "art": "b4",
        "hero": "house",
        "hero_alt": "Illustration of a clean home for house cleaning business marketing in Houston, The Woodlands and Katy",
        "related": ["is-nextdoor-advertising-worth-it", "complete-guide-google-reviews", "hispanic-marketing-houston-spanish-ads-seo"],
        "sections": [
            (None, f"""<p>Sunday night, 9:15. You’re looking at the booking inbox. Two people want a price on a one-time deep clean and haven’t answered your reply from Friday. A tenant in Midtown needs a move-out clean by Thursday so she gets her deposit back. A Facebook message says “how much for a 3 bed 2 bath?” and nothing else. And your best biweekly client in Cypress texted that they’re “going to pause for a while.”</p>
<p>That inbox is the whole business. One-time jobs fill the calendar this week, and recurring clients pay the bills all year.</p>
<p>To get more cleaning clients in Houston, make it easy to get a price and book online, show up in Google Maps for the neighborhoods you serve, collect reviews from every recurring client, and work Nextdoor and local Facebook groups where neighbors ask for referrals. Then measure the number that matters: what it costs you to land one client who books recurring service and stays.</p>
<p>This guide is for owner-operated maid services and small cleaning companies with one to ten crews, from Kingwood to Sugar Land.</p>"""),

            ("Why recurring clients are the whole game", f"""<p>Most cleaning owners know recurring work is better. Fewer have put numbers on how much better, and that changes what you can afford to spend to get a client.</p>
<p>Take an illustrative biweekly client paying $160 a visit. If they stay a year, that’s 26 visits and $4,160 in revenue. A one-time deep clean at $320 is a good day, and then it’s over. Even if half your recurring clients leave in the first six months, the average recurring client is worth several times a one-time job.</p>
<!--fig:value-->
<p>That math gives you a ceiling on acquisition cost. If a recurring client is worth $4,000 a year in revenue and your margin after labor and supplies is 25% to 35%, spending $150 to $250 to land one is reasonable. Spending $150 to land a one-time clean that never comes back usually isn’t.</p>
<p>So treat one-time and move-out cleans as a way in. Price them to make money on their own, then offer every one-time customer a recurring rate before the crew leaves. “Your first recurring clean is at our regular biweekly price instead of the deep-clean rate” is a natural pitch, because the house is already in good shape.</p>"""),

            ("Let people get a price and book without a phone call", f"""<p>“How much for a 3 bed 2 bath?” is the most common message a cleaning company gets, and most owners answer it slowly or vaguely. The companies growing fastest in Houston answer it instantly, on the website.</p>
<p>What a booking page needs:</p>
<ul>
<li>Price by bedrooms, bathrooms and approximate square footage, with clear add-ons (inside oven, inside fridge, interior windows, laundry, pet hair).</li>
<li>Separate prices for standard, deep and move-in/move-out cleans, and the recurring discount shown next to each.</li>
<li>Available dates you can actually fill, with crew capacity behind them.</li>
<li>A card on file at booking, with your cancellation policy in plain words.</li>
<li>Your service area by ZIP code, so someone in Pearland doesn’t book when you only serve The Woodlands.</li>
</ul>
<p>One Texas detail to get right on that page: sales tax. Per the {SRC['comp']}, maid, janitorial and custodial services should collect state and local sales tax, and tax is due on the charge to clean “a home, office, warehouse, garage, restaurant, or any other building.” The exception is a self-employed person working directly as an employee of the household, not a subcontractor for a maid service. If you run a company with crews, show prices “plus tax” or build it in, and say which. Surprise tax on the first invoice is a common reason a new client doesn’t rebook.</p>
<!--fig:quote-->
<p>If you keep a phone-quote option, answer within five minutes during business hours. A homeowner messaging three cleaning companies books with whoever replies first with a real number. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up texts. And if your site wasn’t built for booking, our {L('/services/web-design-seo-pr/', 'web design team')} builds these.</p>"""),

            ("Google Business Profile for a cleaning company that doesn’t have a storefront", f"""<p>Most cleaning companies run from a home office or a small warehouse that customers never visit. Google calls that a service-area business, and the rules are specific.</p>
<p>Per {SRC['sab']}, if customers don’t come to your address, remove it from the profile and list service areas instead. You can list up to 20 cities or ZIP codes, you can’t use a radius, and the whole area shouldn’t go past about two hours of driving. For a cleaning crew that’s irrelevant, because nobody drives two hours to clean a house. List the areas you actually serve and keep the list tight enough that your crews aren’t spending half the day on the Grand Parkway.</p>
<p>The rest of the setup:</p>
<ul>
<li><b>Category:</b> pick the house cleaning category as primary if residential is your main work. Add a commercial cleaning category only if you really take office contracts.</li>
<li><b>Services:</b> list standard cleaning, deep cleaning, move-in/move-out, post-construction and recurring service, each with a short description and a starting price.</li>
<li><b>Photos:</b> before and after shots of kitchens and bathrooms (with client permission and no personal items showing), your team in uniform, your branded car.</li>
<li><b>Booking link:</b> point the appointment link straight to your online booking page.</li>
<li><b>Posts:</b> monthly offers, holiday booking reminders, open recurring slots in a given area.</li>
</ul>
<p>Rankings in Maps lean heavily on how close the searcher is to your business location, which a service-area business still has behind the scenes. That’s why a company based in Spring usually shows up more easily in Spring than in Sugar Land. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} explains what you can and can’t influence.</p>"""),

            ("Reviews: ask after the second clean, not the first", f"""<p>Reviews are the main thing a stranger uses to decide whether to let your crew into their home. Trust is the product.</p>
<p>The rules from {SRC['gpol']} apply: no discounts or free add-ons for reviews, no asking only the clients you know are happy, and no discouraging negative reviews. Ask everyone.</p>
<p>The timing trick that works for recurring services: ask after the second or third visit, once the client has seen consistency. A first clean can be great and still leave the client unsure whether you’ll show up on time next time. By the third clean, they know.</p>
<p>A text that tends to work:</p>
<p><i>“Hi Priya, it’s Ana from [Company]. Hope the house felt good after today’s clean. Would you mind leaving us a quick Google review? Mentioning that you’re a biweekly client in Katy really helps other families find us: [link]. And if anything was missed, reply here and we’ll come back.”</i></p>
<p>Reply to every review within a couple of days. On a bad one, skip the defense, name the fix, and offer a re-clean. People shopping for a cleaner read the replies to see how you treat problems. The {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more scripts.</p>"""),

            ("Move-out cleans: apartments, property managers and realtors", f"""<p>Houston is a renter’s city. In {SRC['census']} for 2019 to 2023, only 42.0% of occupied homes in the City of Houston were owner-occupied, so most are rented. Every lease that ends is a possible move-out clean.</p>
<!--fig:houston-->
<p>The tenant’s motivation is the deposit. Under the Texas Property Code, as summarized in the {SRC['deposit']}, a landlord has to refund the deposit within 30 days after the tenant surrenders the premises (once the tenant gives a written forwarding address), can’t keep any of it for normal wear and tear, and generally has to itemize deductions. Tenants who know a dirty oven or a grimy shower can come out of their deposit will pay for a professional move-out clean.</p>
<p>How to get that work:</p>
<ul>
<li><b>A move-out page and ad group.</b> Keywords like “move out cleaning Houston,” “apartment move out cleaning,” “end of lease cleaning” and “move in cleaning,” with a checklist of what you clean (inside appliances, cabinets, baseboards, blinds).</li>
<li><b>Apartment locators and leasing offices.</b> Houston has a big apartment locator industry. Locators and leasing agents get asked “do you know a cleaner?” constantly. A one-page flyer and a reliable 48-hour turnaround earns referrals.</li>
<li><b>Property managers.</b> Single-family rental managers in Katy, Cypress and Humble need turnover cleans between tenants. That’s steady B2B work with invoicing instead of card-on-file.</li>
<li><b>Realtors.</b> Listing agents want a pre-listing deep clean before photos, and buyer’s agents get asked about move-in cleans. Our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how local agents market themselves')} shows what they care about.</li>
</ul>
<p>Move-out customers are, by definition, leaving. Some are moving across town, though. Ask for the new address and offer a move-in clean or a recurring rate at the new place.</p>"""),

            ("Nextdoor and Facebook: where neighbors ask for a cleaner", f"""<p>Search Facebook groups for The Woodlands, Kingwood or Pearland and you’ll find a post asking for a house cleaner recommendation almost every week. Same on Nextdoor. For a cleaning company, these referral threads are one of the cheapest sources of recurring clients there is.</p>
<h3>Nextdoor</h3>
<p>Claiming a Nextdoor business page is free, and verified neighbors can recommend you and “Fave” you. Per {SRC['nd']}, your Fave count helps you rank higher in Nextdoor search. The same guide cites Nextdoor’s own survey numbers: 78% of neighbors say they’re more likely to trust a small business a neighbor recommended, and businesses with even one recommendation get three times as many page views. Treat those as Nextdoor’s figures, but the direction matches what we see.</p>
<p>What to do: claim the page, ask your recurring clients who use Nextdoor to recommend you (the same ask as a Google review, sent to the ones you know are on the app, without any reward), and post when you have openings in a specific neighborhood. Whether paid Nextdoor ads are worth it is a separate question we answered in {L('/blog/is-nextdoor-advertising-worth-it/', 'is Nextdoor advertising worth it')}.</p>
<h3>Facebook groups and Facebook ads</h3>
<p>In groups, don’t spam the wall with ads. Most neighborhood groups ban it, and admins remember. The better play is to get your clients to tag you when someone asks for a recommendation. A reply from a real neighbor saying “Ana’s crew has cleaned our house every other Friday for two years” beats any ad.</p>
<p>Facebook and Instagram ads can work for a cleaning company with an offer and a tight area. What we’d test:</p>
<ul>
<li>A short video of a crew finishing a kitchen, shot on a phone, with the price for a standard clean on screen.</li>
<li>An offer aimed at recurring service, like a discount on the first clean when you book biweekly.</li>
<li>Targeting a few ZIP codes where you already have clients, so new bookings fit your routes.</li>
<li>Sending clicks to your booking page. If you use instant forms, ask for home size and preferred frequency so you’re not chasing price shoppers. Our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'guide to fixing bad Facebook leads')} has the form settings.</li>
</ul>"""),

            ("Google Ads and Local Services Ads for cleaning companies", f"""<p>House cleaning services is a Local Services Ads category on {SRC['lsa']}, so you can run pay-per-lead ads at the top of searches like “house cleaning near me” and “maid service Houston.” For a cleaning company, LSA is usually worth a test once you have 30 or more Google reviews. Without reviews, you’ll pay for leads that pick the competitor with 300.</p>
<p>Regular search ads let you target the specific cleans you want. A starter keyword set:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th></tr></thead>
<tbody>
<tr><td>Recurring</td><td>house cleaning service, maid service near me, weekly house cleaning, biweekly cleaning service</td></tr>
<tr><td>Deep clean</td><td>deep cleaning service, deep house cleaning Katy, one time deep clean</td></tr>
<tr><td>Move-out</td><td>move out cleaning, apartment move out cleaning Houston, move in cleaning</td></tr>
<tr><td>Local</td><td>house cleaners The Woodlands, maid service Sugar Land, cleaning service Pearland</td></tr>
</tbody></table></div>
<p>And the negatives, which matter even more here because “cleaning” attracts job seekers and DIY searches in huge numbers:</p>
<!--fig:negatives-->
<p>Budget-wise, a small company can start search ads around $1,000 to $2,000 a month in a tight area (an illustrative range, not a benchmark). Track bookings, not clicks. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads comparison')} covers how to split the budget, and {L('/services/search-marketing/', 'our search team')} can run it for you.</p>"""),

            ("Spanish-language marketing: for customers and for crews", f"""<p>In the City of Houston, 47.2% of residents age 5 and up speak a language other than English at home, and 44.1% are Hispanic or Latino, per {SRC['census']}. For a cleaning company, that matters on both sides of the business.</p>
<p><b>Customers.</b> Many Houston families would rather book in Spanish. A Spanish version of your booking page, a bilingual phone line and a few Spanish-language reviews open up a part of the market that a lot of English-only competitors ignore. Our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing guide')} covers Spanish ads and SEO in detail. Translate the pages properly, with a fluent speaker, rather than running them through a tool and hoping.</p>
<p><b>Crews.</b> Hiring is the real growth limit for most cleaning companies, and recruiting is a marketing job. The {SRC['bls']} counted 15,270 maids and housekeeping cleaners in the Houston metro, with a mean wage of $14.49 an hour. You’re competing with hotels, hospitals and every other cleaning company for those people. A careers page in English and Spanish, with pay, schedule and how tips work, does better than a vague “we’re hiring” post.</p>
<p>If you advertise jobs on Facebook or Instagram, the ads must run under Meta’s Employment special ad category. Per {SRC['loomer']}, that locks age to 18 to 65+ and all genders, requires at least a 15-mile radius with no ZIP code targeting, removes lookalike audiences, and keeps instant forms from asking about age, gender or relationship status. Write the ad so the right applicants recognize themselves: pay range, days, area, “no nights or weekends.”</p>"""),

            ("Retention: the first three cleans decide it", f"""<p>Marketing gets clients in. Retention decides whether the marketing was worth it. In accounts we’ve looked at across home services, a client who makes it past the first few visits tends to stay much longer, so the first month deserves extra care.</p>
<ul>
<li><b>Same crew, same day.</b> Clients hire a company and stay for the people. Keep the crew consistent and tell the client when it changes.</li>
<li><b>Notes on every home.</b> Where the dog stays, which bathroom gets the special cleaner, “don’t move the papers on the desk.” Put it in your software so a substitute crew knows.</li>
<li><b>A check-in after the first and third clean.</b> One text: “Anything we should do differently next time?” Fix it, then thank them.</li>
<li><b>A real pause option.</b> Summer travel and holidays cause cancellations. Offer a pause with a return date instead of a cancel, and send a reminder the week before.</li>
<li><b>Holiday and season pushes.</b> Thanksgiving and Christmas deep cleans, spring cleaning, back-to-school. Offer existing clients first pick of the slots.</li>
</ul>
<p>Track monthly churn: recurring clients lost divided by recurring clients at the start of the month. If it’s high, fix service before you spend more on ads. Pouring new clients into a leaky schedule just raises your cost per retained client.</p>"""),

            ("What to track: cost per booked recurring client", f"""<p>Most cleaning owners track leads, or worse, likes. The number that tells you whether a channel works is cost per booked recurring client, measured for each source.</p>
<!--fig:funnel-->
<p>To get it, tag every booking with its source (Google Maps, LSA, search ads, Nextdoor, Facebook, referral, apartment locator). Your booking software or a simple “How did you hear about us?” field can do it, and call tracking numbers handle phone bookings. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} walks through the setup. Then once a month, divide what you spent on each source by the recurring clients it produced who are still active after 60 days.</p>
<p>A first 90 days for a small company:</p>
<ol>
<li><b>Month one:</b> online pricing and booking, Google Business Profile cleanup, Nextdoor page claimed, review texts going to every recurring client after their second clean.</li>
<li><b>Month two:</b> move-out page and outreach to five apartment locators or property managers, plus one Facebook ad test in your best ZIP codes.</li>
<li><b>Month three:</b> Local Services Ads or search ads once reviews are in place, Spanish booking page if your market calls for it, and the first look at cost per recurring client by source.</li>
</ol>
<p>Tell us about your crews, your area and how many recurring clients you want to add, and a senior strategist will put together a plan that fits. <a href="/contact/">Get in touch</a> whenever you’re ready.</p>"""),
        ],
        "faq": [
            ("How do I get more clients for my house cleaning business?",
             "Make it easy to get a price and book online, set up a Google Business Profile as a service-area business, and ask every recurring client for a Google review after their second or third clean. Claim your free Nextdoor page and have clients recommend you there and in local Facebook groups. Then add Local Services Ads or search ads once you have enough reviews to compete."),
            ("How much should a cleaning company pay to get a new client?",
             "It depends on whether the client recurs. A biweekly client who stays a year can bring in around $4,000 in revenue at typical Houston pricing, so spending $150 to $250 to land one is often reasonable. Spending that on a one-time clean usually isn't. Track cost per booked recurring client by source, counting only clients still active after 60 days."),
            ("Do cleaning services charge sales tax in Texas?",
             "Generally yes. The Texas Comptroller says maid, janitorial and custodial services should collect state and local sales tax, and tax is due on cleaning a home, office or other building. The exception is a self-employed person working directly as a household employee rather than for a maid service. Show prices plus tax or with tax included, and confirm details with the Comptroller or your accountant."),
            ("Is Nextdoor good for marketing a cleaning business?",
             "Often, yes. Neighbors regularly ask Nextdoor for cleaner recommendations, and a business page is free to claim. Verified neighbors can recommend you and Fave you, and Nextdoor says your Fave count helps you rank higher in its search. Ask existing clients who use Nextdoor to recommend you, post when you have openings in a neighborhood, and test paid ads separately."),
            ("How do I get move-out cleaning jobs in Houston?",
             "Build a move-out cleaning page with a clear checklist and price, then run search ads on phrases like apartment move out cleaning Houston. Introduce yourself to apartment locators, leasing offices, single-family rental property managers and realtors, since they're asked for cleaner referrals constantly. Fast turnaround matters because Texas landlords must refund deposits within 30 days of move-out, and tenants want a clean unit before inspection."),
        ],
        "figures": {
            "value": {
                "type": "bars",
                "title": "One-year revenue per client by service type",
                "sub": "Illustrative Houston pricing, one client, first 12 months",
                "items": [["Weekly at $140", 7280, "$7,280"], ["Biweekly at $160", 4160, "$4,160"], ["Monthly at $190", 2280, "$2,280"], ["Move-out clean", 380, "$380"], ["One-time deep clean", 320, "$320"]],
                "highlight": [1],
                "note": "Illustrative example. Assumes the client stays all year; real retention is lower.",
                "alt": "Bar chart comparing one-year revenue from recurring and one-time house cleaning clients in Houston",
                "caption": "Even with churn, recurring clients are worth several one-time jobs. Price acquisition accordingly.",
            },
            "quote": {
                "type": "compare",
                "title": "Answering “how much for a 3 bed 2 bath?”",
                "left": {"title": "What loses the booking", "items": ["“Depends, can we schedule a walkthrough?”", "Reply the next morning", "No prices anywhere online", "Sales tax appears on the first invoice", "No mention of a recurring rate"]},
                "right": {"title": "What books the client", "items": ["Instant price by beds, baths and size", "Online booking with real open dates", "Add-ons priced and listed", "Tax shown up front", "Recurring discount next to every price"]},
                "alt": "Comparison of how Houston house cleaning companies answer price questions, from vague replies to instant online quotes",
                "caption": "The fastest clear price usually wins the booking.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for cleaning company ads",
                "sub": "Start with these and review search terms weekly",
                "items": ["Jobs: jobs, hiring, near me hiring, part time, salary", "Supplies: products, supplies, vacuum, mop, spray", "DIY: how to, tips, checklist printable, hacks", "Wrong service: carpet, pressure washing, window, pool", "Commercial: janitorial, office, if you only do homes", "Free: free, volunteer", "Hotel: housekeeping jobs, hotel housekeeping", "Franchise: franchise, start a cleaning business"],
                "alt": "Checklist of negative keywords for house cleaning business Google Ads in Houston",
                "caption": "Cleaning keywords pull a lot of job seekers. Block them on day one.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From click to retained recurring client",
                "stages": [["Quote requests", "120"], ["Booked first clean", "40"], ["Chose recurring", "18"], ["Still active at 60 days", "13"]],
                "note": "Illustrative example. $2,000 spent / 13 retained = about $154 per recurring client.",
                "alt": "Funnel showing cost per booked recurring client for a Houston house cleaning business, from quote to 60-day retention",
                "caption": "Judge every channel on the bottom number, not the top.",
            },
            "houston": {
                "type": "stats",
                "title": "Houston numbers a cleaning company should know",
                "stats": [["42.0%", "of Houston homes owner-occupied (most are rented)"], ["47.2%", "speak a language other than English at home"], ["15,270", "maids and housekeeping cleaners in the metro"], ["30 days", "Texas deadline to refund a deposit"]],
                "note": "Sources: Census QuickFacts 2019-2023, BLS May 2023, Texas Property Code",
                "alt": "Stats on Houston renters, Spanish speakers and cleaning workers relevant to house cleaning business marketing",
                "caption": f"From {SRC['census']}, {SRC['bls']} and the {SRC['deposit']}.",
            },
        },
    },
]
