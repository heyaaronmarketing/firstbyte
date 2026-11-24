"""Batch 15: outdoor living / patio cover company marketing in Houston and The Woodlands, and staffing agency
marketing in Houston.

Research (outdoor living): The Woodlands Township Covenant Administration permitting page (RDRC prior written approval,
site marking, Civic Access Portal, Grogan's Forest/Shenandoah exception); the Township's RDRC page (nine village RDRCs,
monthly meetings) and DSC page (only committee that grants variances, meets first and third Wednesdays); the recorded
2024 Residential Standards (sealed plans for 400 sq ft open-roof structures, third-party inspector over 200 sq ft roof,
screen colors, plate height); Houston Permitting Center residential addition permit page (site plan, windstorm/strapping
details, 10 business days, $33.56 admin fee) and floodplain outdoor improvement page (pergolas, porches, awnings);
Google's Local Services Ads category list (no patio/pergola category; General contractor, Carpenters, Landscaping);
CFPB Regulation Z 1026.24(d) triggering terms; Houston Public Media via KEDT on 145 days at 90F+ in 2025 (NWS); Axios
Houston on Harris County West Nile detections; Houzz 2026 outdoor trends study; Housecall Pro on Houzz profiles/Pro.
Research (staffing): Jon Loomer on Meta's Employment special ad category; Google's housing/employment/credit FAQ;
Google Search Central JobPosting docs; Indeed pricing page; HR Dive on Indeed's 2019 rule for recruitment-based accounts;
TWC UI coverage page (Labor Code 201.011 and 201.029); TDLR history (Personnel Employment Services abolished 2011,
Temporary Common Worker Employers deregulated 2017); American Staffing Association Q3 2025 survey; Greater Houston
Partnership 2026 jobs forecast; Glassdoor on review integrity; Search Engine Roundtable on Google's employee-review rule;
Morgan Lewis on Texas SB 140.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # outdoor living post
    "twp_permit": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/Permitting-Process", "The Woodlands Township’s permitting page"),
    "rdrc": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/RDRC", "the Township’s RDRC page"),
    "dsc": A("https://www.thewoodlandstownship-tx.gov/Government/Committees-Boards/Development-Standards-Committee", "Development Standards Committee"),
    "stds": A("https://www.thewoodlandstownship-tx.gov/files/sharedassets/main/v/2/covenant-administration/documents/2024-residential-standards-recorded-12-10-2024.pdf", "the Township’s 2024 Residential Standards"),
    "hpc_add": A("https://www.houstonpermittingcenter.org/hpwcode1134", "Houston Permitting Center’s residential addition permit page"),
    "hpc_flood": A("https://www.houstonpermittingcenter.org/hpwfmo1004", "a separate floodplain permit"),
    "lsa": A("https://support.google.com/localservices/answer/6224841?hl=en", "Google’s Local Services Ads category list"),
    "regz": A("https://www.consumerfinance.gov/rules-policy/regulations/1026/24/", "Regulation Z, section 1026.24"),
    "heat": A("https://www.kedt.org/texas-news/2026-01-05/houston-saw-more-90-plus-degree-days-in-2025-than-ever-before", "Houston Public Media"),
    "axios": A("https://www.axios.com/local/houston/2026/06/05/houston-harris-county-west-nile-mosquitoes", "Axios Houston"),
    "houzz": A("https://www.houzz.com/magazine/10-outdoor-remodeling-trends-to-know-for-2026-stsetivw-vs~185305660", "Houzz’s 2026 outdoor trends study"),
    "hcp": A("https://www.housecallpro.com/resources/what-is-houzz-how-does-it-work/", "Housecall Pro’s rundown of Houzz"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s review policy"),
    # staffing post
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "gfaq": A("https://support.google.com/adspolicy/answer/9997418?hl=en", "Google’s housing, employment and credit policy FAQ"),
    "jobschema": A("https://developers.google.com/search/docs/data-types/job-posting", "Google’s JobPosting documentation"),
    "indeed": A("https://www.indeed.com/hire/resources/howtohub/how-pricing-works-on-indeed", "Indeed’s pricing page"),
    "hrdive": A("https://www.hrdive.com/news/indeed-now-requires-recruiting-companies-to-pay-for-listings/545453", "HR Dive"),
    "twc": A("https://efte.twc.texas.gov/ui_law_coverage_issues.html", "TWC’s unemployment coverage guide"),
    "tdlr": A("https://www.tdlr.texas.gov/history.htm", "TDLR’s own history page"),
    "asa": A("https://americanstaffing.net/posts/2025/12/29/staffing-employment-ticks-up-in-third-quarter/", "the American Staffing Association"),
    "ghp": A("https://houston.org/news/job-growth-forecasted-for-houston-region-in-2026", "the Greater Houston Partnership’s 2026 forecast"),
    "glassdoor": A("https://api.glassdoor.com/about/trust/fighting-fake-reviews/", "Glassdoor’s review integrity rules"),
    "ser_emp": A("https://www.seroundtable.com/google-maps-negative-reviews-employees-24995.html", "Search Engine Roundtable"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
}

PATIO = "/blog/outdoor-living-patio-cover-marketing-houston-the-woodlands/"
STAFF = "/blog/staffing-agency-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: outdoor living / patio covers
    {
        "slug": "outdoor-living-patio-cover-marketing-houston-the-woodlands",
        "title": "Outdoor Living and Patio Cover Marketing in Houston and The Woodlands",
        "seo_title": "Patio Cover & Outdoor Living Marketing: Houston, Woodlands",
        "desc": "Marketing for Houston and The Woodlands patio cover, pergola and outdoor kitchen companies: RDRC approvals, renderings, Google Ads, Houzz, financing rules.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Instagram", "Google Business Profile"],
        "art": "b2",
        "hero": "house",
        "hero_alt": "Illustration of a home with a covered patio for outdoor living and patio cover marketing in Houston and The Woodlands",
        "related": ["pool-builder-marketing-houston-the-woodlands", "how-to-get-more-remodeling-leads-houston", "kitchen-bath-remodeling-marketing-the-woodlands"],
        "sections": [
            (None, f"""<p>Thursday, 6:15 p.m., a back patio in Alden Bridge. Your estimator has a tape measure out and the homeowners have a Pinterest board open on an iPad. The wife wants a cedar-stained pergola with a fan. The husband wants a solid roof “so we can actually sit out here in August.” Halfway through, she asks the question you hear every week: “Will the RDRC approve this?”</p>
<p>Then the real one. “The other two companies are sending us drawings. Do you do that?”</p>
<p>Patio cover marketing in Houston and The Woodlands comes down to three things. Get in front of homeowners while they’re fed up with the heat and the mosquitoes, show them the finished space before they sign, and take the approval and permit paperwork off their plate. The companies that win also follow up on a $35,000 estimate like it’s worth $35,000, which is rarer than you’d think.</p>
<p>This guide is for patio cover, pergola, outdoor kitchen and screened room companies working from Katy to Kingwood. If you also build pools, our {L('/blog/pool-builder-marketing-houston-the-woodlands/', 'pool builder marketing guide')} covers that side, and we won’t repeat it here.</p>"""),

            ("Why outdoor living leads in Houston behave the way they do", f"""<p>A patio cover is a strange purchase. It’s not urgent like a broken AC, it’s not as big as a pool, and almost nobody has bought one before. So the buyer does a lot of research, gets three bids, and talks it over at dinner for weeks.</p>
<p>In the accounts we’ve run for home improvement companies, a few patterns hold for this category:</p>
<ul>
<li>Both spouses (or every decision-maker) need to see the design. If one of them missed the consult, your rendering is doing the selling at the kitchen table without you.</li>
<li>Three bids is the norm. You’re rarely the only one in the backyard.</li>
<li>The first question is often about the HOA, and the second is about price per square foot.</li>
<li>Projects grow once the homeowner sees what’s possible. A pergola request becomes a cover with a kitchen.</li>
</ul>
<p>The demand is real. {SRC['houzz']}, a survey of 1,191 U.S. Houzz users fielded in spring 2026, found 71% of homeowners doing outdoor projects hired a pro, up from 65% in 2024. Shade structures were part of 35% of projects, up 15 points, and screened-in porches showed up in 14%. Among homeowners who added or upgraded an outdoor kitchen, 44% fully covered it. People want to be outside, under a roof.</p>"""),

            ("Selling shade and screens: Houston heat and mosquito season", f"""<p>Your best ad copy is the weather. Houston hit 90 degrees or higher on 145 days in 2025, breaking the old record of 142 set in 2011, according to {SRC['heat']} reporting on the National Weather Service’s annual review. A family in Cypress or Pearland doesn’t need to be told why shade matters. They need to be shown what the patio looks like at 4 p.m. in July with a solid roof, two fans and a misting line.</p>
<p>Mosquitoes are the other half of the pitch, and the reason screened rooms sell. Harris County’s mosquito control division says West Nile can be detected in mosquitoes from March through December, and in 2025 detections began in May and carried on through the year and into 2026, per {SRC['axios']}. Anyone who’s tried to grill near a drainage ditch in Spring in June already knows.</p>
<!--fig:climate-->
<p>What that means for your marketing:</p>
<ul>
<li>Lead with comfort facts in ads. “Solid roof, rated fans, 12 degrees cooler in the shade” works better than “Transform your backyard.” (If you quote a temperature drop, measure it on your own jobs first.)</li>
<li>Show real Houston conditions in photos and reels: a covered patio during a summer storm, a screened room at dusk with the lights on and no bugs.</li>
<li>Sell screens as an add-on at every consult between March and October.</li>
</ul>"""),

            ("When to spend: the outdoor living calendar in Greater Houston", f"""<p>Houston’s outdoor season is long, but buying intent isn’t flat. Homeowners start looking when the first hot weekend hits, and they want the project finished before the summer or before holiday hosting. Most companies we talk to also need to sell in fall to keep crews busy through winter.</p>
<!--fig:season-->
<p>A practical calendar:</p>
<ul>
<li><b>January to March:</b> heaviest search and consult volume for spring builds. Spend the most here. This is also when RDRC and permit lead times hurt, so push “approval handled” messaging.</li>
<li><b>April to June:</b> still strong, but your schedule fills. Sell the fall slot.</li>
<li><b>July to August:</b> the heat drives searches for covers and screens even while crews are slammed. Keep ads running, raise prices or extend lead times, and lean on financing messaging.</li>
<li><b>September to November:</b> holiday hosting angle (“outdoor kitchen ready for Thanksgiving”). Hurricane season runs through November 30, so be ready to talk about wind-rated framing and attachment details after any storm.</li>
<li><b>December:</b> slow for new leads, good for following up every open estimate from the year.</li>
</ul>
<p>Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing guide')} has the wider local calendar.</p>"""),

            ("HOA and deed restriction approvals: The Woodlands RDRC, the DSC and everyone else", f"""<p>In The Woodlands, the approval question isn’t a formality. Per {SRC['twp_permit']}, changes to a lot with an existing home, including patio covers, outdoor living areas, summer kitchens, gazebos and arbors, need prior written approval from the Residential Design Review Committee or its designated staff. Applications go through the Township’s Civic Access Portal. A contractor can submit for the owner, but the owner has to register an account first.</p>
<p>The details are where contractors win or lose time. Owners and contractors must mark the outline of the improvement on site, give distances to the property lines, mark overhangs over 12 inches, and flag any trees proposed for removal at the time of submission. There are nine village RDRCs, each meeting at least once a month, according to {SRC['rdrc']}. The {SRC['dsc']} is the body that grants variances, and it meets on the first and third Wednesdays of the month.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Rule in The Woodlands</th><th>What it means for your sale</th></tr></thead>
<tbody>
<tr><td>Prior written approval required for patio covers, outdoor living areas, summer kitchens and arbors</td><td>Build approval time into every quoted start date</td></tr>
<tr><td>Sealed plans for attached open-roof structures (pergolas, arbors) and detached roofed structures of 400 sq ft or more</td><td>Big projects need an engineer; price it in and say so up front</td></tr>
<tr><td>Third-party inspector for structures with more than 200 sq ft of roof</td><td>Another line on the schedule, and a credibility point if you handle it</td></tr>
<tr><td>Screens must be brown, black, bronze or charcoal gray</td><td>Show only approved screen colors in Woodlands renderings</td></tr>
<tr><td>Outdoor living roof plate height within 12 inches of the home’s first-floor plate</td><td>Design to it from the first sketch so the drawing you sell is the one that passes</td></tr>
<tr><td>Grogan’s Forest sections (Cantwell Forest, Avalon Oaks, Dulcimer Woods) go through the City of Shenandoah for patio covers and pergolas</td><td>Check the address before you promise a timeline</td></tr>
</tbody></table></div>
<p>Those rows come from {SRC['stds']} and the permitting page. They change, and neighborhood criteria can be stricter, so treat this as a starting checklist and confirm with Covenant Administration on each job.</p>
<p>Inside Houston city limits, you’re dealing with permits instead of (or on top of) deed restrictions. The {SRC['hpc_add']} covers residential accessory structures and additions, and asks for a Texas registered survey or site plan, framing and foundation plans, and details showing how windstorm or strapping compliance is achieved. It lists 10 business days for processing and a $33.56 admin fee on top of the fee schedule. Pergolas, porches and awnings on lots in mapped flood zones can also need {SRC['hpc_flood']}. Whether a given cover needs a full building permit depends on the scope, so confirm with the Permitting Center (832-394-9000) for each design type you sell, then write it down once.</p>
<p>Sugar Land, Pearland, Conroe, Tomball and the rest each run their own permitting, and many master-planned communities in Katy and Cypress have their own architectural review on top. This is all a marketing asset. A page called “Patio covers in The Woodlands: we handle the RDRC submittal” answers the exact question homeowners ask, and almost nobody in this trade has written it.</p>"""),

            ("3D renderings are your best sales tool", f"""<p>Back to the Thursday consult. The two companies sending drawings have an edge before anyone talks price. A homeowner can’t picture a 16-by-24 gable cover attached to their roofline. They can picture a rendering of their own house with it.</p>
<p>How we’d use renderings in the sales process:</p>
<ol>
<li>Photograph the back of the house and measure at the first visit, then send a rendering within 48 hours. Speed beats polish.</li>
<li>Show two options side by side, like a pergola with a polycarbonate top versus a solid roof tied into the existing roofline. Two choices close better than one.</li>
<li>Put the price on the same page as the picture. The rendering creates the want, and the number right next to it keeps the conversation honest.</li>
<li>Reuse the rendering for the RDRC or permit application so the homeowner sees one consistent design from sales to approval.</li>
<li>After the build, post the rendering next to the finished photo. Those before-and-after pairs are your best Instagram content and your best proof.</li>
</ol>
<p>Renderings also give your ads and landing pages a hook that isn’t “quality craftsmanship.” “See your patio before you sign” is a promise most competitors can’t make.</p>"""),

            ("Google Ads and Local Services Ads for patio cover companies", f"""<p>Search is where the high-intent buyer shows up. Build ad groups by product, each with its own landing page:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Patio covers</td><td>patio cover contractor Houston, covered patio builder The Woodlands, attached patio cover Katy</td><td>Patio covers page with prices “starting at” and roof options</td></tr>
<tr><td>Pergolas</td><td>pergola builder Houston, louvered pergola Cypress, cedar pergola installation</td><td>Pergola page with material comparison</td></tr>
<tr><td>Outdoor kitchens</td><td>outdoor kitchen builder Spring TX, outdoor kitchen contractor Sugar Land</td><td>Outdoor kitchen page with covered and uncovered examples</td></tr>
<tr><td>Screened rooms</td><td>screened porch builder Houston, patio enclosure Pearland, screen in patio</td><td>Screened rooms page with mosquito-season angle</td></tr>
<tr><td>HOA and approvals</td><td>patio cover HOA approval The Woodlands, patio cover permit Houston</td><td>Approvals page (the one nobody else has)</td></tr>
</tbody></table></div>
<p>Negatives matter as much as keywords. DIY and retail shoppers eat budgets in this category fast.</p>
<!--fig:negatives-->
<p>Settings we’d use: location targeting set to people in or regularly in your service area, a radius that matches how far your crews actually drive (the Grand Parkway is a long road), call assets scheduled for staffed hours, and conversions for calls, forms and booked consults. Our guide to {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking forms and calls')} walks through that setup, and the {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} will tell you what clicks roughly cost before you budget.</p>
<p>Local Services Ads are less straightforward here. {SRC['lsa']} has no patio, pergola, outdoor kitchen or screened room category. It does list General contractor, Carpenters and Landscaping services, and some outdoor living companies qualify under one of those. Whether yours does depends on how Google classifies your business and your area, so run the eligibility check and expect some leads for work you don’t do. We compare the two ad types in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</p>"""),

            ("Google Business Profile and reviews", f"""<p>Pick your primary category for the work you most want, then add secondary categories that are honestly yours. Fill the Services list with patio covers, pergolas, outdoor kitchens and screened rooms, each with a one-line description and a starting price where you’re comfortable sharing it.</p>
<p>Photos do the heavy lifting. Upload finished projects tagged by town (“Gable patio cover, Sterling Ridge”), short clips of the build, and your crew on site. A profile with 300 real project photos beats one with 12 stock images every time.</p>
<p>For reviews, send the link by text the week the project is finished, while the homeowner is still hosting people out there. Don’t offer anything for a review and don’t only ask the happy customers; both break {SRC['gpol']}. Ask homeowners to mention what was built and where, in their own words, if they’re comfortable. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has request templates.</p>"""),

            ("Houzz and Instagram reels", f"""<p><b>Houzz.</b> Homeowners planning outdoor projects browse it for ideas, and some use it to find pros. A basic professional profile is free, and Houzz Pro adds paid software and a separate advertising package, per {SRC['hcp']}. Pricing varies, so get a written quote and ask whether any lead volume is promised. We’d set up the free profile with your best 30 projects and real reviews before paying for anything, then judge any paid package on booked consults, not profile views.</p>
<p><b>Instagram reels.</b> Outdoor living is one of the few trades where the product is fun to watch. The reels that work for this category tend to be:</p>
<ul>
<li>Time-lapses of a cover going up in a day or two, ending on the finished space at golden hour.</li>
<li>Rendering-to-reality transitions (the rendering fades into the finished build).</li>
<li>A 20-second walk-through with the homeowner, if they’re willing.</li>
<li>Close-ups of details buyers ask about: the flashing where the cover ties into the roof, the fan box, the gutter.</li>
</ul>
<p>Shoot vertical, keep house numbers out of frame, and put the town in the caption. Boost the best ones to homeowners within your service radius. Our {L('/services/paid-social-advertising/', 'paid social team')} runs these campaigns if you’d rather not.</p>"""),

            ("Financing ads: the disclosure rules most contractors miss", f"""<p>Financing sells big outdoor projects. It also comes with federal advertising rules that apply to your ads, your website and your yard signs.</p>
<p>Under {SRC['regz']}, if a closed-end credit ad states certain “triggering terms” (the down payment amount or percentage, the number of payments or repayment period, the amount of any payment, or the amount of any finance charge), the ad must also state the down payment, the repayment terms and the annual percentage rate, using that term, along with whether the rate can increase. So “$299 a month for your new patio cover” on a Facebook ad, all by itself, is a problem.</p>
<!--fig:financing-->
<p>Practical rules we follow:</p>
<ul>
<li>General phrases like “financing available” or “ask about payment options” don’t trigger the extra disclosures.</li>
<li>If you want to show a monthly payment, get the full disclosure language from your lender and use it every time the payment appears.</li>
<li>“0% interest” and deferred-interest promos have their own pitfalls. Use the lender’s approved wording and keep a copy.</li>
<li>Keep financing claims off the ad if you can’t fit the disclosures, and put the details on the landing page instead (where the full terms appear next to the payment).</li>
</ul>
<p>We’re marketers, not lawyers. Have your lender or attorney review any ad that shows a payment amount.</p>"""),

            ("Following up on a $35,000 estimate", f"""<p>The estimate is where most outdoor living companies leak money. They do a good consult, send a nice PDF, and then wait. A week later the homeowner signs with whoever called back.</p>
<!--fig:followup-->
<p>A follow-up sequence that respects the size of the purchase:</p>
<ul>
<li><b>Day 0:</b> rendering and estimate sent, with a short personal note from the estimator.</li>
<li><b>Day 2:</b> a call, not a text, to walk through the drawing and answer questions. Ask what the other bids looked like.</li>
<li><b>Day 7:</b> send a project from the same neighborhood or HOA with photos (“Here’s one we built two streets over in Creekside Park, approved in one RDRC cycle”).</li>
<li><b>Day 14:</b> offer a revised option, maybe a smaller footprint or a phased approach (cover now, kitchen next spring).</li>
<li><b>Day 30 and 60:</b> a check-in with something useful, like the current approval timeline or a schedule opening.</li>
<li><b>Lost:</b> ask why, politely. The answer is your best marketing data.</li>
</ul>
<p>Put every estimate in a CRM with the lead source attached so you can see which channel produces signed contracts, not just leads. Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead and CRM follow-up')} covers the setup.</p>"""),

            ("What to budget and what to track in the first 90 days", f"""<p>For a single-crew to three-crew outdoor living company in the north Houston suburbs, this is an illustrative starting budget. It’s an example, not a benchmark or a quote.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Google Ads search</td><td>$2,000 to $5,000</td><td>Covers, pergolas, kitchens, screens; heavier January to June</td></tr>
<tr><td>Meta and Instagram</td><td>$750 to $2,000</td><td>Reels, retargeting, local homeowners</td></tr>
<tr><td>Local SEO and website</td><td>$750 to $2,000</td><td>Product pages, approvals page, project pages by town</td></tr>
<tr><td>Renderings</td><td>$100 to $500</td><td>Software or outsourced per project</td></tr>
<tr><td>Houzz (optional)</td><td>Varies</td><td>Free profile first, paid only after a quote</td></tr>
</tbody></table></div>
<p>The first 90 days, roughly:</p>
<ol>
<li><b>Month one:</b> fix the Google Business Profile, build product pages and the approvals page, set up call and form tracking, start search ads on your two most profitable products.</li>
<li><b>Month two:</b> add Instagram reels from current jobs, start retargeting, and put every estimate into a follow-up sequence.</li>
<li><b>Month three:</b> review cost per consult and cost per signed contract by channel. Cut what doesn’t produce contracts and move that money to what does.</li>
</ol>
<p>Track consults booked, renderings sent, estimates issued, close rate and average contract value. Lead counts will mislead you; a channel that sends half as many leads at twice the contract value is the better channel.</p>
<p>If you want a plan built around your crews, your service area and the projects you’d rather be building, <a href="/contact/">get in touch</a>. A senior strategist will put one together for you.</p>"""),
        ],
        "faq": [
            ("How do patio cover companies get more leads in Houston?",
             "Most leads come from Google searches for a product plus a town, like patio cover contractor Houston or pergola builder The Woodlands, along with Google Maps, referrals and Instagram. Build a page for each product, show real projects by neighborhood, request reviews after every job, and send a 3D rendering quickly after each consult. Follow up on every estimate for at least 60 days."),
            ("Do I need RDRC approval for a patio cover in The Woodlands?",
             "Yes. The Woodlands Township requires prior written approval from the Residential Design Review Committee or its staff for patio covers, outdoor living areas, summer kitchens and arbors on lots with an existing home. Applications go through the Township’s Civic Access Portal, the outline must be marked on site, and larger roofed structures need sealed plans. Some Grogan’s Forest sections go through the City of Shenandoah instead."),
            ("Does a patio cover need a permit in the City of Houston?",
             "Many do. The Houston Permitting Center’s residential addition permit covers accessory structures and additions and asks for a site plan, framing details and windstorm or strapping details, with about 10 business days of processing. Lots in mapped flood zones can need a separate floodplain permit for pergolas and porches. Confirm each design type with the Permitting Center before quoting a start date."),
            ("Can patio cover companies use Google Local Services Ads?",
             "Sometimes. Google’s Local Services Ads list has no patio cover, pergola or outdoor kitchen category, but it does include General contractor, Carpenters and Landscaping services, and some outdoor living companies qualify under one of those. Eligibility depends on your business type and service area, so run Google’s eligibility check. Regular search ads on product keywords remain the main paid channel for most companies."),
            ("Can I advertise monthly payments for a patio cover?",
             "Only with the right disclosures. Under federal Regulation Z, an ad that states a monthly payment, number of payments, down payment or finance charge must also state the down payment, repayment terms and APR. Phrases like financing available don’t trigger those rules. Get approved disclosure language from your lender and have your attorney or lender review ads that show payment amounts."),
        ],
        "figures": {
            "climate": {
                "type": "stats",
                "title": "Why Houston buys shade and screens",
                "stats": [["145", "days at 90°F or higher in 2025"], ["142", "the old record, set in 2011"], ["Mar-Dec", "when West Nile can show up in mosquitoes"], ["35%", "of outdoor projects add shade structures"]],
                "note": "Sources: NWS via Houston Public Media, Harris County via Axios, Houzz 2026",
                "alt": "Stats on Houston heat, mosquito season and shade demand for patio cover marketing in Houston and The Woodlands",
                "caption": f"From {SRC['heat']}, {SRC['axios']} and {SRC['houzz']}.",
            },
            "season": {
                "type": "columns",
                "title": "When outdoor living leads come in",
                "sub": "Relative consult requests by month for a north Houston patio cover company",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [70, 85, 100, 95, 85, 75, 70, 65, 60, 60, 45, 30],
                "highlight": [1, 2, 3],
                "y_label": "Relative volume",
                "note": "Illustrative example",
                "alt": "Column chart of illustrative monthly lead volume for outdoor living companies in Houston and The Woodlands",
                "caption": "Your own pattern will differ. Pull 24 months of leads from your CRM and chart them before you set budgets.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for patio cover ads",
                "sub": "Add these before launch, then read the search terms weekly",
                "items": ["DIY: diy, how to build, plans, kit, yourself", "Retail: home depot, lowes, costco, wayfair, amazon", "Cheap products: pop up, gazebo tent, canopy, umbrella", "Materials only: lumber, brackets, polycarbonate sheets", "Jobs: jobs, hiring, salary, carpenter apprentice", "Rentals: rent, rental, event canopy", "Ideas only: pinterest, ideas, pictures (test first)", "Out of area towns you don’t serve"],
                "alt": "Checklist of negative keywords for patio cover and pergola Google Ads in Houston and The Woodlands",
                "caption": "Test “ideas” searches carefully. Some convert for remarketing, most don’t convert at all.",
            },
            "financing": {
                "type": "compare",
                "title": "Financing ad copy: risky vs. safer",
                "left": {"title": "Triggers extra disclosures", "items": ["“$299 a month for your patio cover”", "“Only 10% down”", "“60 easy payments”", "“Just $1,200 in total interest”", "Payment shown with no APR"]},
                "right": {"title": "Safer without full terms", "items": ["“Financing available”", "“Ask about payment options”", "“Apply in minutes on our site”", "Full terms on the landing page", "Lender-approved wording, every time"]},
                "alt": "Comparison of financing ad wording for outdoor living and patio cover companies in Houston and The Woodlands",
                "caption": f"Based on the triggering terms in {SRC['regz']}. Have your lender review payment ads.",
            },
            "followup": {
                "type": "steps",
                "title": "Following up on a big outdoor estimate",
                "sub": "A 60-day sequence for patio cover and outdoor kitchen bids",
                "steps": [["Day 0", "Rendering and estimate with a personal note."], ["Day 2", "Phone call to walk through the drawing."], ["Day 7", "Nearby project in the same HOA, with photos."], ["Day 14", "A revised or phased option."], ["Day 30-60", "Useful check-ins, then ask why if lost."]],
                "alt": "Steps for following up on patio cover and outdoor kitchen estimates for companies in Houston and The Woodlands",
                "caption": "Most of the contracts lost in this trade are lost to silence, not price.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: staffing agencies
    {
        "slug": "staffing-agency-marketing-houston",
        "title": "Staffing Agency Marketing in Houston: Winning Clients and Candidates",
        "seo_title": "Staffing Agency Marketing in Houston: Clients & Candidates",
        "desc": "Staffing agency marketing in Houston: Meta job ad rules, Google Jobs schema, Indeed, LinkedIn, client SEO, reviews, speed to fill and cost per placement.",
        "category": "Strategy",
        "icons": ["Meta", "Google", "LinkedIn"],
        "art": "b4",
        "hero": "industry",
        "hero_alt": "Illustration of an industrial site for staffing agency marketing in Houston and The Woodlands",
        "related": ["b2b-marketing-houston-energy-industrial", "speed-to-lead-response-time-follow-up-crm", "commercial-cleaning-janitorial-marketing-houston"],
        "sections": [
            (None, f"""<p>Monday, 6:40 a.m. A plant manager off the Ship Channel calls your branch: he needs twelve forklift operators by Wednesday, second shift, and his regular agency just told him “maybe six.” Your recruiter pulls up the Indeed post from last week. Four applicants, two of them in Dallas.</p>
<p>Across town, your account manager is in the Energy Corridor pitching an AP clerk and a payroll specialist to a controller who has already talked to three other firms.</p>
<p>That’s staffing agency marketing in Houston. You’re running two businesses at once. One sells to employers who want people fast, and the other sells jobs to people who have plenty of other options. Most agencies market only one side well, usually by accident.</p>
<p>The agencies that grow here build a steady pipeline of qualified candidates through job ads and Google’s job listings, win clients with industry-specific pages and direct outreach, collect reviews from both sides, and measure everything against cost per placement. This guide covers both sides for light industrial, healthcare, administrative and professional search firms in Houston, The Woodlands and the suburbs around them.</p>"""),

            ("Two-sided marketing: clients and candidates need different funnels", f"""<p>Clients and candidates don’t search the same way, don’t respond to the same channels, and don’t care about the same things. Treating them as one audience is the most common mistake we see in staffing marketing.</p>
<!--fig:twosides-->
<p>Keep separate campaigns, separate landing pages, separate budgets and separate reporting. A dashboard that mixes “leads” from both sides is useless. Ten candidate applications and one client inquiry are not eleven leads.</p>
<p>The balance shifts with the market. When clients are hiring and candidates are scarce, put money into candidate acquisition. When orders slow down, shift toward client development. Your recruiters and account managers will tell you which side is starving if you ask them every week.</p>"""),

            ("What Houston employers are hiring for now", f"""<p>Your client marketing should follow the hiring. {SRC['ghp']} projects 30,900 new jobs in metro Houston for 2026, below the recent average of about 50,000 a year. Health care and social assistance are expected to drive nearly half of that growth, with 14,000 new positions. Construction, public education, government and professional services also add jobs. Upstream oil and gas, along with administrative support services, is expected to shrink as oil prices fall.</p>
<!--fig:market-->
<p>Nationally, staffing firms employed just under two million temporary and contract workers a week in the third quarter of 2025, down 7.5% from a year earlier, with sales of $28.1 billion, according to {SRC['asa']}. The ASA’s weekly index had turned positive year over year starting in September.</p>
<p>The takeaway for a Houston firm: if your client book is heavy on upstream energy and back-office admin, diversify your marketing toward healthcare, construction and petrochemical maintenance now, while you still have the margin to do it. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston energy and industrial companies')} covers selling into those buyers; this post focuses on what’s different about staffing.</p>"""),

            ("Candidate ads on Meta and Google: the employment rules", f"""<p>Facebook and Instagram are still the cheapest way to reach hourly workers in Pasadena, Baytown, Humble or Conroe. But job ads on Meta must run under the Employment special ad category, and that changes how you target.</p>
<p>Per {SRC['loomer']}, employment ads are locked to ages 18 to 65+, all genders, and a minimum 15-mile radius around any location you pick. ZIP code targeting is off, some detailed targeting disappears, you can’t exclude anything, and lookalike and saved audiences aren’t available. Google applies similar restrictions to employment ads: no targeting or excluding by age, gender, parental status or marital status, and no ZIP code targeting, per {SRC['gfaq']}.</p>
<p>So the ad itself does the targeting. Specific beats clever:</p>
<ul>
<li>“Forklift operators, 2nd shift, $19/hr, La Porte, start Wednesday” finds forklift operators. “Join our team!” finds nobody.</li>
<li>Put the pay, shift, location and start date in the first line and on the image.</li>
<li>Run separate ads in Spanish for roles where that’s your candidate pool. Our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Spanish-language marketing guide')} covers how to do it well.</li>
<li>Use Meta instant forms with two or three screening questions (certification, shift availability, transportation). Short forms bring volume; a question or two of friction brings people who show up.</li>
</ul>
<p>Client-facing ads (selling your services to employers) are a different campaign. In accounts we’ve run, we keep job-offer language out of them entirely so they’re not confused with employment ads. Our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'guide to fixing bad Facebook leads')} applies to candidate forms too.</p>"""),

            ("Google Jobs and JobPosting structured data", f"""<p>When someone searches “warehouse jobs Katy” or “medical assistant jobs The Woodlands,” Google often shows a job listings box above the regular results. Your own job pages can appear there, at no cost, if they carry JobPosting structured data that follows Google’s rules.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Property</th><th>Status</th><th>Staffing note</th></tr></thead>
<tbody>
<tr><td>title, description, datePosted, hiringOrganization, jobLocation</td><td>Required</td><td>Title should be the job, not “Hiring now!!”</td></tr>
<tr><td>baseSalary</td><td>Recommended</td><td>Pay is the first thing candidates look for; include it</td></tr>
<tr><td>employmentType</td><td>Recommended</td><td>Temporary, contractor, full time; be accurate</td></tr>
<tr><td>validThrough</td><td>Recommended</td><td>Set it, and expire filled jobs promptly</td></tr>
<tr><td>directApply</td><td>Recommended</td><td>Only true if applying is short and on your page</td></tr>
<tr><td>hiringOrganization “confidential”</td><td>Option</td><td>For roles where you can’t name the client</td></tr>
</tbody></table></div>
<p>A few points from {SRC['jobschema']} that trip up staffing firms. Google doesn’t allow expired job postings, so you need to set validThrough to a past date, return a 404 or 410, or remove the markup when a job fills. Google recommends its Indexing API over sitemaps for job pages, because it gets new and removed jobs crawled faster. And for a staffing agency hiring on behalf of a client it can’t name, Google says to use “confidential” as the hiring organization name.</p>
<!--fig:schema-->
<p>Most applicant tracking systems can output this markup. Check that yours does it correctly with Google’s Rich Results Test, because a lot of them get pay or location wrong.</p>"""),

            ("Indeed sponsorship and LinkedIn", f"""<p><b>Indeed.</b> Since January 2019, Indeed has required recruitment-based accounts in the U.S., including staffing agencies, to pay to post their listings, per {SRC['hrdive']}. Today, {SRC['indeed']} describes results-based pricing. Depending on your setup, you pay per click on the job or per started application, and Indeed suggests a budget based on the title, location and competition. The same page says jobs can require payment when you aggregate them from a feed or ATS while also posting directly, or when a confidential post doesn’t name your organization.</p>
<p>How we’d manage it:</p>
<ul>
<li>Sponsor the hard-to-fill and high-margin roles, not every req.</li>
<li>Rewrite titles to match what candidates search (“Forklift Operator,” not “Material Handler II – Client Site 4”).</li>
<li>Close or pause filled jobs the same day. Paying for applications to filled jobs is the easiest money to save.</li>
<li>Track cost per hire by job type, not cost per application. A $4 application that never shows up is expensive.</li>
</ul>
<p><b>LinkedIn.</b> For professional search (engineers, accountants, IT, project controls), LinkedIn is the main candidate channel, and recruiter seats usually beat ads for passive candidates. On the client side, LinkedIn is where you reach HR directors and plant managers with useful content, like a quarterly Houston pay rate report for the roles you fill. For light industrial, LinkedIn rarely earns its cost.</p>"""),

            ("SEO for “staffing agency [industry] Houston”", f"""<p>Clients search for staffing by specialty and place: “industrial staffing agency Houston,” “healthcare staffing Houston,” “administrative staffing The Woodlands,” “temp agency Pasadena TX.” A generic homepage won’t rank for any of them. A page built for each will.</p>
<p>What each industry page needs:</p>
<ul>
<li>The roles you fill, in the client’s words (millwrights, CNAs, AP clerks, process operators).</li>
<li>Typical time to fill, safety and screening process, and any industry requirements (TWIC cards, OSHA 10, background and drug screening).</li>
<li>Your service area by suburb and corridor: Ship Channel, Energy Corridor, Medical Center, I-45 north to Conroe.</li>
<li>A short case story with numbers you can actually back up.</li>
<li>A form for “request staff,” not “contact us.”</li>
</ul>
<p>Separate those client pages from candidate pages (“forklift jobs Houston,” “CNA jobs Spring TX”). Candidate traffic is easier to win and it can flood your analytics, so report on the two separately.</p>
<p>For Google Maps, each branch needs its own Business Profile with accurate hours and categories. Don’t expect help from Local Services Ads; {SRC['lsa']} has no staffing or employment category. Our posts on {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Houston map pack')} and {L('/blog/power-of-local-landing-pages/', 'local landing pages')} go deeper on both.</p>"""),

            ("Texas rules that touch staffing marketing", f"""<p>Texas doesn’t license general staffing agencies the way some states do. The state abolished its Personnel Employment Services program in 2011 (House Bill 3167) and deregulated Temporary Common Worker Employers in 2017 (Senate Bill 2065), according to {SRC['tdlr']}. Professional employer organizations are a separate category with their own rules, so check if you offer PEO services.</p>
<p>For unemployment tax, Texas law treats the staffing firm as the employer of its temporary employees. {SRC['twc']} quotes Labor Code 201.029, which says “a temporary help firm is the employer of an individual employed by the firm.” That matters for your marketing claims. You can honestly tell clients that you handle payroll, unemployment tax and claims for your temps, and that’s a real selling point for a small manufacturer in Tomball who doesn’t want the headache.</p>
<p>Texting candidates needs care too. Texas brought marketing texts under its telephone solicitation law through SB 140, effective September 1, 2025, with exemptions for some situations, per {SRC['sb140']}. Job alerts to candidates who opted in are different from promotional blasts, but get your attorney’s read on your setup. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS marketing rules post')} covers consent in more detail.</p>
<p>None of this is legal advice.</p>"""),

            ("Reviews on Google and Glassdoor", f"""<p>Both sides read reviews. Clients check Google before calling, and candidates check Google, Indeed and Glassdoor before applying.</p>
<p>Google is the tricky one for staffing. Google’s conflict-of-interest rules have covered reviews about a current or former employment experience since late 2017, per {SRC['ser_emp']}. Your placed temps are your employees, so their reviews of working for you sit in a gray area. We’d focus Google review requests on client hiring managers and on candidates as job seekers (how fast you responded, how the interview went), and steer feedback about the employment itself to Glassdoor and Indeed.</p>
<p>Glassdoor has its own rules. Per {SRC['glassdoor']}, employers can’t offer money, bonuses or prizes for reviews, can’t ask employees for proof they posted, and can’t require reviews written in the office or on company equipment. Glassdoor says reviews tied to incentives are removed.</p>
<p>What works on both platforms:</p>
<ul>
<li>Ask every client contact for a Google review after the first successful fill, by email with a direct link.</li>
<li>Ask candidates for feedback at the end of their first week, when you know how the placement is going.</li>
<li>Reply to every review, especially the angry ones from candidates who didn’t get a callback. That reply is for the next 100 candidates reading it.</li>
</ul>
<p>Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has request templates you can adapt.</p>"""),

            ("Speed to fill is a marketing metric", f"""<p>In staffing, the agency that fills first usually wins the order, and the agency that calls a candidate back first usually wins the candidate. Speed is a marketing problem as much as an operations one, because everything you spend on ads is wasted if nobody responds.</p>
<!--fig:speed-->
<p>What to set up:</p>
<ul>
<li>Text new applicants within five minutes with a link to schedule a screening call. Automate it.</li>
<li>Respond to client inquiries the same hour. Route them to the account manager’s phone, not a shared inbox.</li>
<li>Keep a “ready bench” of screened candidates for your most common roles, and market to fill it before orders arrive.</li>
<li>Track time from order to first submittal, and from first submittal to start. Those are the numbers clients care about and the ones you should advertise once they’re good.</li>
</ul>
<p>Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead and CRM follow-up')} explains the response-time setup in more depth.</p>"""),

            ("Light industrial vs. professional search: different marketing", f"""<p>Light industrial and professional search are different businesses that happen to share a word.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Light industrial and hourly</th><th>Professional and direct hire</th></tr></thead>
<tbody>
<tr><td>Candidate channels</td><td>Indeed, Facebook and Instagram, Google Jobs, referrals, walk-ins</td><td>LinkedIn, referrals, your database, niche job boards</td></tr>
<tr><td>Ad copy focus</td><td>Pay, shift, location, start date</td><td>Role, company type, growth, compensation range</td></tr>
<tr><td>Speed expectation</td><td>Hours to a few days</td><td>Weeks</td></tr>
<tr><td>Client buyer</td><td>Plant, warehouse or operations manager</td><td>HR director, hiring manager, CFO</td></tr>
<tr><td>Client channels</td><td>Direct outreach, Google search, local SEO</td><td>LinkedIn, referrals, content, events</td></tr>
<tr><td>Main metric</td><td>Fill rate, cost per start, show rate</td><td>Placements, fee per placement, time to fill</td></tr>
</tbody></table></div>
<p>If you do both, run them as separate brands or at least separate sections of your site and separate ad accounts. Light industrial candidates don’t care about your executive search page, and a CFO doesn’t want to land on a forklift job.</p>"""),

            ("Measuring cost per placement", f"""<p>Cost per lead and cost per application are the wrong numbers for staffing. Cost per placement (or cost per start for temp roles) is the one that matters, and you can calculate it by channel.</p>
<p>The formula is simple: total marketing spend on a channel divided by placements sourced from that channel. Getting the source right is the hard part. Every candidate needs a source field in your ATS, set automatically from the job board or ad, and every client needs a lead source in your CRM.</p>
<!--fig:funnel-->
<p>Once you have three months of clean data, compare channels by cost per start rather than cost per application. In accounts we’ve seen, the cheapest application source is rarely the cheapest placement source.</p>
<!--fig:cpp-->
<p>On the client side, measure cost per new account and the gross margin each account brings in its first year. A client that costs $3,000 to win and orders 40 temps is a much better deal than one that cost $500 and ordered two.</p>
<p>Check one more number monthly: the show rate for first-day starts. If candidates aren’t showing up, the problem may be your ad copy promising something the job doesn’t deliver.</p>"""),

            ("A first 90 days for a Houston staffing agency", f"""<p>A realistic starting plan:</p>
<ol>
<li><b>Month one:</b> split client and candidate tracking, set source fields in your ATS and CRM, fix your Google Business Profile for each branch, and check your job pages’ structured data.</li>
<li><b>Month two:</b> launch Meta candidate ads under the Employment category for your two highest-volume roles, sponsor hard-to-fill jobs on Indeed, and build two industry pages for clients.</li>
<li><b>Month three:</b> start client review requests, add automatic applicant texts, and review cost per placement by channel. Shift budget toward what produces starts, not applications.</li>
</ol>
<p>If you want help building that plan around your verticals and branches, <a href="/contact/">get in touch</a>. A senior strategist will put together a custom plan for your agency.</p>"""),
        ],
        "faq": [
            ("How do staffing agencies get more clients in Houston?",
             "Build a page for each industry and role you fill, like industrial staffing Houston or healthcare staffing The Woodlands, with time to fill, screening process and service area. Pair that with direct outreach to plant and HR managers, Google reviews from client hiring managers, and LinkedIn content for professional roles. Track cost per new account and first-year margin, not just inquiries."),
            ("Can staffing agencies target job ads by age or ZIP code on Facebook?",
             "No. Job ads on Meta must run under the Employment special ad category, which locks age to 18 to 65+, includes all genders, removes ZIP code targeting and requires at least a 15-mile radius. Lookalike and saved audiences aren’t available and you can’t exclude targeting. Google has similar rules for employment ads. Specific ad copy with pay, shift and location does the targeting instead."),
            ("How do I get my staffing agency’s jobs on Google Jobs?",
             "Add JobPosting structured data to each job page with the required properties: title, description, datePosted, hiringOrganization and jobLocation. Include pay, employment type and validThrough where possible. Google doesn’t allow expired postings, so remove or expire filled jobs promptly, and use the Indexing API for faster updates. For confidential clients, Google says to use confidential as the hiring organization name."),
            ("Do staffing agencies need a license in Texas?",
             "Texas doesn’t currently license general staffing agencies. The state abolished its Personnel Employment Services program in 2011 and deregulated Temporary Common Worker Employers in 2017, according to TDLR. For unemployment tax, Texas law treats the staffing firm as the employer of its temporary workers. Professional employer organizations have separate rules, so check with an attorney if you offer PEO services."),
            ("How should a staffing agency measure marketing ROI?",
             "Measure cost per placement, or cost per start for temp roles, by channel. Divide what you spent on each channel by the placements it produced, which requires a source field on every candidate in your ATS. On the client side, track cost per new account and first-year gross margin. Cost per application is misleading, because cheap applicants often don’t qualify or show up."),
        ],
        "figures": {
            "twosides": {
                "type": "compare",
                "title": "Two audiences, two funnels",
                "left": {"title": "Candidates", "items": ["Search jobs by role, pay and place", "Indeed, Meta, Google Jobs, referrals", "Want pay, shift, start date fast", "Judge you on callback speed", "Measured by cost per start"]},
                "right": {"title": "Clients", "items": ["Search staffing by industry and city", "Google, LinkedIn, outreach, referrals", "Want reliable people quickly", "Judge you on fill rate and quality", "Measured by cost per new account"]},
                "alt": "Comparison of candidate and client marketing funnels for staffing agency marketing in Houston and The Woodlands",
                "caption": "Separate campaigns, pages and reports for each side.",
            },
            "market": {
                "type": "stats",
                "title": "The staffing market Houston firms sell into",
                "stats": [["30,900", "metro Houston jobs forecast for 2026"], ["14,000", "of those in health care and social assistance"], ["~2M", "U.S. temp and contract workers a week, Q3 2025"], ["$28.1B", "U.S. staffing sales, Q3 2025"]],
                "note": "Sources: Greater Houston Partnership, American Staffing Association",
                "alt": "Stats on Houston job growth and U.S. staffing employment for staffing agency marketing in Houston",
                "caption": f"From {SRC['ghp']} and {SRC['asa']}.",
            },
            "schema": {
                "type": "checklist",
                "title": "Job page checklist for Google Jobs",
                "sub": "What each staffing job page needs",
                "items": ["Required: title, description, datePosted", "Required: hiringOrganization and jobLocation", "Pay in baseSalary, matching the page text", "Accurate employmentType (temporary, full time)", "validThrough set on every posting", "Filled jobs expired, 404 or markup removed", "“confidential” for unnamed clients", "Indexing API or fast sitemap updates"],
                "alt": "Checklist of JobPosting structured data requirements for staffing agency job pages in Houston",
                "caption": f"Based on {SRC['jobschema']}.",
            },
            "speed": {
                "type": "steps",
                "title": "Speed to fill, step by step",
                "sub": "Response times a Houston staffing branch can hold",
                "steps": [["Under 5 minutes", "Automatic text to new applicants with a booking link."], ["Same hour", "Client inquiries routed to the account manager."], ["Same day", "Screening call and submittal for urgent orders."], ["Ready bench", "Pre-screened candidates for your most common roles."], ["Weekly review", "Order-to-submittal and submittal-to-start times."]],
                "alt": "Steps for faster response and fill times in staffing agency marketing in Houston and The Woodlands",
                "caption": "The fastest agency usually wins the order and the candidate.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From applicant to placement",
                "stages": [["Applications", "400"], ["Screened and qualified", "120"], ["Submitted to clients", "60"], ["Offers or assignments", "30"], ["Started and stayed a week", "24"]],
                "note": "Illustrative example",
                "alt": "Funnel from applications to placements for a light industrial staffing agency in Houston",
                "caption": "Example numbers for one month in one branch. Your drop-offs show where to fix things.",
            },
            "cpp": {
                "type": "bars",
                "title": "Cost per start by channel",
                "sub": "One branch, one quarter, light industrial roles",
                "items": [["Referrals", 90, "$90"], ["Google Jobs (organic)", 110, "$110"], ["Meta employment ads", 240, "$240"], ["Indeed sponsored", 310, "$310"], ["Job fairs", 420, "$420"]],
                "highlight": [0, 1],
                "note": "Illustrative example",
                "alt": "Bar chart of illustrative cost per start by channel for a staffing agency in Houston",
                "caption": "Illustrative only. Build your own from ATS source data before moving budget.",
            },
        },
    },
]
