"""Batch 14 (module a): pressure washing / soft washing business marketing in Houston and The Woodlands, and concrete
contractor marketing in Houston (driveways, patios, slabs, commercial flatwork).

Research, pressure washing post: Google's Local Services Ads category list (support.google.com/adwords/answer/6224841,
checked November 2026: no pressure washing, power washing or soft washing category; nearest are Window cleaning
services and House cleaning services); Sterling Sky's LSA category change tracker (updated November 3, 2026, no
pressure washing category added); ARMA on algae discoloration (Gloeocapsa magma, worst in the Gulf States, "DO NOT use
a power washer," 15 to 20 minute dwell); The Woodlands Township covenant FAQ ("kept in good order and repair," notices
sent once a violation is established) and its mildew and algae flyer; Harris County power washing best-practices
brochure hosted by the City of Hedwig Village (washwater must be collected; Texas Water Code 7.102 up to $25,000 a day,
Harris County regulations up to $1,000 a day); City of Sugar Land pressure washing page (discharge to storm drain
prohibited, capture and haul or sanitary sewer); TCEQ RG-434 Environmental Rules for Car Washes, revised June 2026
(get the wastewater utility's approval before discharging to sewer; other outdoor washing: contact TCEQ Small Business
and Local Government Assistance); Houston Permitting Center MS4 page (311 and the 713-640-4399 hotline for illicit
discharges); USPS Texas release on mailbox access (unstamped flyers in mailboxes are illegal).
Research, concrete post: Houston Permitting Center residential driveway/sidewalk/curb permit HPWOCE1011 (minimum $103,
two dimensioned site plans and a survey, inspections before and after placement, current bond, valid one year,
next-business-day inspections) and floodplain single-family driveway permit HPWFMO1006 ($33.56 admin fee, flatwork
vs. adjacent grade, mitigation plan); The Woodlands Township permitting process (prior written approval of the RDRC;
paving in some areas goes through Shenandoah); Houston Geological Society Bulletin, Oct 1995 (Beaumont Formation,
highly expansive soils, pavement damage); HUD Cityscape 2023 on expansive soils (one in four U.S. homes affected,
$15 billion a year); TCEQ construction stormwater general permit TXR150000 (1 to 5 acres small, 5+ large, SWP3, expires
March 5, 2028); NWS Houston/Hobby June normal of 6.09 inches (1991-2020); FAA Part 107 remote pilot requirements;
Autodesk BuildingConnected (network of over 1 million construction professionals); Google LSA list (Foundations
services and General contractor exist; no concrete category).
Not used (couldn't verify from a primary source): a Texas state license requirement for concrete or pressure washing
contractors, any average Houston price per square foot, specific HOAs' mildew notice policies, current Houston CPCs
for these trades.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # pressure washing post
    "lsa": A("https://support.google.com/adwords/answer/6224841", "Google’s Local Services Ads category list"),
    "ssky": A("https://www.sterlingsky.ca/google-local-services-ads-category-list-changes-lsa/", "Sterling Sky’s running tracker of LSA category changes"),
    "arma": A("https://www.asphaltroofing.org/algae-discoloration/", "the Asphalt Roofing Manufacturers Association"),
    "wtfaq": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/FAQ", "The Woodlands Township’s covenant FAQ"),
    "wtmildew": A("https://www.thewoodlandstownship-tx.gov/files/assets/main/v/2/covenant-administration/documents/mildew-algae20_1-converted.pdf", "flyer on algae and mildew"),
    "hcbmp": A("https://www.thecityofhedwigvillage.com/upload/common/Events/Storm Water Management PlanNewFolder/Power Washing brochure.pdf", "Harris County’s best-practices brochure for power washers"),
    "sugarland": A("https://sugarlandtx.gov/676/Pressure-Washing", "City of Sugar Land’s pressure washing page"),
    "rg434": A("https://www.tceq.texas.gov/downloads/assistance/publications/rg-434.pdf/@@download/file/rg-434.pdf", "TCEQ’s car wash guide (RG-434)"),
    "ms4": A("https://www.houstonpermittingcenter.org/municipal-separate-storm-sewer-system-ms4", "Houston’s storm sewer (MS4) page"),
    "usps": A("https://about.usps.com/news/state-releases/tx/2011/tx_2011_0429.htm", "the Postal Service"),
    # concrete post
    "cohdw": A("https://www.houstonpermittingcenter.org/hpwoce1011", "Houston Permitting Center’s residential driveway, sidewalk and curb permit page"),
    "cohfp": A("https://www.houstonpermittingcenter.org/hpwfmo1006", "a floodplain permit for single-family driveways"),
    "wtpermit": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/Permitting-Process", "The Woodlands Township’s permitting page"),
    "hgs": A("https://archives.datapages.com/data/HGS/vol38/no02/08.htm", "a Houston Geological Society Bulletin article"),
    "hud": A("https://www.huduser.gov/PORTAL/periodicals/cityscape/vol25num1/ch10.pdf", "a 2023 HUD Cityscape paper"),
    "cgp": A("https://www.tceq.texas.gov/permitting/stormwater/construction/index", "TCEQ’s construction stormwater general permit"),
    "nws": A("https://www.weather.gov/hgx/climate_hou_normals_jun", "the National Weather Service"),
    "faa": A("https://www.faa.gov/uas/commercial_operators/become_a_drone_pilot/", "the FAA"),
    "bc": A("https://construction.autodesk.com/products/buildingconnected/", "BuildingConnected"),
}

PW = "/blog/pressure-washing-marketing-houston-the-woodlands/"
CC = "/blog/concrete-contractor-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: pressure washing
    {
        "slug": "pressure-washing-marketing-houston-the-woodlands",
        "title": "Pressure Washing Marketing in Houston and The Woodlands: How to Book More Jobs",
        "seo_title": "Pressure Washing Marketing in Houston & The Woodlands",
        "desc": "Pressure washing marketing for Houston and The Woodlands: soft wash and roof jobs, HOA mildew notices, Google Ads keywords, Nextdoor and recurring contracts.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Nextdoor"],
        "art": "b1",
        "hero": "house",
        "hero_alt": "Illustration of a freshly washed house for pressure washing marketing in Houston and The Woodlands",
        "related": ["house-cleaning-business-marketing-houston", "is-nextdoor-advertising-worth-it", "commercial-cleaning-janitorial-marketing-houston"],
        "sections": [
            (None, f"""<p>Thursday afternoon, somewhere off Kuykendahl. You just finished a driveway, and the stripe between the cleaned half and the dirty half was so clean the homeowner took a picture of it before you did. Two neighbors walked over while you were rolling up the hose. One asked for a card. The other asked if you “do roofs too,” and you said yes, and then realized you’d left your cards in the other truck.</p>
<p>That’s the pressure washing business in a nutshell. The work sells itself to anyone standing on the sidewalk. Getting it in front of people who aren’t standing on the sidewalk is the marketing.</p>
<p>To get more pressure washing customers in Houston and The Woodlands, own the Google Maps results for the services you’re best at (house soft washing, driveways, roofs, commercial flatwork), run search ads on high-intent terms with a hard negative list, and turn every job into before-and-after content plus a door-hanger drop on that street. Then sell maintenance plans so the same customers book you every year. The humidity here does half the selling for you. Mildew comes back.</p>
<p>Below is the setup we’d run for an owner-operator or a small crew working Spring, Conroe, Cypress, Katy, Kingwood or anywhere inside the Beltway.</p>"""),

            ("Why Houston is a good market for washing (and a crowded one)", f"""<p>Houston grows things on houses. North-facing siding in The Woodlands goes green under the pines. Fences turn gray-black. Roofs get those dark streaks that every homeowner assumes are “dirt.”</p>
<p>Those streaks are usually algae. According to {SRC['arma']}, <i>Gloeocapsa magma</i> is the most common species behind roof discoloration, and it’s most widespread in the Gulf States, where it thrives in warm, humid conditions. That’s us. A roof that’s cleaned in March can look streaky again within a few years, and siding on the shady side of a house often needs attention every year.</p>
<p>The catch is that the barrier to entry is a trailer and a Facebook page. Every spring, new operators show up in local groups offering “$99 driveways.” You won’t beat that on price. You beat it by looking like the company that will still exist next year: a real website, a full Google profile, reviews with photos, proof of insurance.</p>
<!--fig:season-->
<p>Demand isn’t flat. In accounts we’ve worked for home service companies, calls for exterior cleaning climb from late February into May, sag in the worst of the summer heat, and pick back up in the fall before the holidays, when people want the house to look good for family. Hurricane season (June 1 to November 30) adds a wave of debris and storm cleanup calls after a big storm. Plan budget around that curve, and save some for the fall push most operators ignore.</p>"""),

            ("Split your services, because customers search for them separately", f"""<p>Nobody searches “exterior cleaning solutions.” They search the thing that’s bugging them, so organize your site, profile and ads the same way.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Service</th><th>What the customer types</th><th>What sells it</th></tr></thead>
<tbody>
<tr><td>House soft washing</td><td>house washing near me, soft wash house Spring TX, mildew on siding</td><td>Photos of the shady side before and after; a plain explanation of low pressure and plant protection</td></tr>
<tr><td>Driveway and sidewalk cleaning</td><td>driveway cleaning The Woodlands, pressure wash driveway near me</td><td>The stripe photo; a starting price; rust and oil stain options priced separately</td></tr>
<tr><td>Roof cleaning</td><td>roof cleaning Houston, black streaks on roof, roof soft wash</td><td>“No high pressure on shingles,” with a link to the manufacturer guidance; insurance proof</td></tr>
<tr><td>Fence and deck cleaning</td><td>fence cleaning near me, wood fence pressure washing Katy</td><td>Before-after of graying cedar; a staining upsell if you offer it</td></tr>
<tr><td>Commercial flatwork</td><td>commercial pressure washing Houston, dumpster pad cleaning, drive thru cleaning</td><td>Night or early-morning scheduling, wastewater recovery, certificate of insurance on request</td></tr>
<tr><td>Fleet washing</td><td>fleet washing Houston, truck washing service, mobile fleet wash</td><td>On-site service at the yard, recurring schedule, how you handle runoff</td></tr>
</tbody></table></div>
<p>Each row deserves its own page on your site with its own photos, and its own entry in the Services section of your Google Business Profile. A single “Services” page listing everything in bullets ranks for nothing.</p>
<p>For the profile itself, pick the primary category that matches the work you want most. Pressure washing service is the obvious choice for most operators. Add secondary categories only for work you really do. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest of the profile setup, and {L('/blog/power-of-local-landing-pages/', 'local landing pages')} explains how to build town pages (Spring, Tomball, Magnolia, Cypress) that don’t read like copy-paste.</p>"""),

            ("Roof cleaning: say how you do it, in writing", f"""<p>Roof jobs pay well and scare homeowners, who’ve heard pressure washing ruins shingles. They’re right.</p>
<p>The industry group for shingle makers is blunt. {SRC['arma']} says “DO NOT use a power washer or any type of brush or broom to clean algae from the roof surface,” recommends a cleaning solution per the shingle manufacturer’s directions, and says the solution should stay on the roof at least 15 minutes and no more than 20. That’s soft washing.</p>
<p>Put that on your roof cleaning page in plain words. Explain your mix in general terms, how you pre-wet and rinse plants, what happens to gutters and downspouts, and that you carry liability insurance. Link the ARMA page. A homeowner in Kingwood comparing three quotes will pick the one who explained the process over the one who said “we’ll make it look new.”</p>
<p>Also say what you won’t clean, or will only clean after a look. Tile, metal and very old roofs each have their own problems.</p>"""),

            ("HOA mildew letters and master-planned communities", f"""<p>This is a lead source almost nobody markets to on purpose. Large parts of Houston’s suburbs sit inside master-planned communities and HOAs with deed restrictions, and those restrictions usually require homes to be kept up.</p>
<p>The Woodlands is the obvious example. {SRC['wtfaq']} says the deed restrictions “require that properties be kept in good order and repair,” and that once a violation has been established, notices go to the owner. The Township even publishes a {SRC['wtmildew']} warning residents that painting over algae and mildew is a mistake, and that periodic cleaning with a power washer using water only may help prevent the problem.</p>
<p>When a homeowner gets a letter, they have a deadline and a problem, and they search right away. Build for that moment:</p>
<ul>
<li>A landing page titled something like “Got an HOA mildew notice? House washing in The Woodlands, Spring and Cypress.” Say how fast you can usually get out there, and offer to send a dated after photo they can forward to the HOA.</li>
<li>A search ad group for “HOA violation house washing,” “HOA letter mildew,” and “deed restriction violation pressure washing.” Low volume, very high intent.</li>
<li>Neighborhood pricing. When one house on a street gets a notice, its neighbors often got one too. Offer a few dollars off per house when three or more homes on the same street book together, and print it on your door hangers.</li>
</ul>
<p>Don’t pretend to speak for any HOA, and keep community logos out of your ads.</p>"""),

            ("Google Ads for pressure washing: keywords, negatives and settings", f"""<p>Search ads suit this trade. Someone typing “house washing Conroe” wants a house washed. Someone typing “pressure washer” wants to buy a machine, and that’s where most budgets leak.</p>
<p>Build one campaign with an ad group per service from the table above, each pointing to its own page. Use phrase and exact match for the core terms (“house washing,” “soft wash,” “roof cleaning,” “driveway cleaning,” “pressure washing service”) with town names and “near me.” Add the commercial terms in a separate campaign so the residential budget doesn’t get eaten by one restaurant chain manager searching at 2 a.m.</p>
<!--fig:negatives-->
<p>A few settings matter more than the rest:</p>
<ul>
<li><b>Location:</b> under Campaign settings, then Locations, then Location options, choose “Presence: people in or regularly in your included locations.” The default also shows ads to people merely interested in your area.</li>
<li><b>Radius:</b> draw it around where you actually want to drive a trailer. From The Woodlands, maybe Spring, Conroe and Tomball but not Pearland.</li>
<li><b>Call assets</b> scheduled for the hours someone answers, and calls counted as conversions. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} shows how.</li>
<li><b>Ad copy</b> that answers the obvious objections: “Soft wash for roofs and siding. Plants pre-wet and rinsed. Insured. Starting at [your price] for most driveways.”</li>
</ul>
<p>Click costs vary a lot by town and season. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a feel for home service ranges. For a solo operator, we’d start between $800 and $1,500 a month on search alone (illustrative, not a quote) and judge it on booked jobs after six weeks, not on clicks.</p>"""),

            ("Local Services Ads: what’s available for washing right now", f"""<p>Owners ask us about the “Google Guaranteed” ads at the top of the page all the time. For this trade the answer is mostly no, for now.</p>
<p>When we checked {SRC['lsa']} in November 2026, there was no pressure washing, power washing or soft washing category. The nearest categories are Window cleaning services and House cleaning services. {SRC['ssky']}, which logs every addition, showed no washing category added through its November 3, 2026 update.</p>
<p>If you really do run a window cleaning line, that category may be worth applying for, and you can check eligibility for your address in the sign-up. Don’t join a category to show up for work you don’t do; Google screens businesses, and you’ll waste money on leads you can’t serve. Watch the list, because Google has been adding categories steadily. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'comparison of Local Services Ads and Google Ads')} explains how the two work together once a category opens.</p>"""),

            ("Before-and-after content that actually gets used", f"""<p>Every operator has a phone full of before-and-after shots. Most never get posted, and the ones that do are shot from different spots in different light. Make the comparison easy to read.</p>
<!--fig:shots-->
<p>Where to put it:</p>
<ul>
<li><b>Google Business Profile.</b> Upload a few fresh photos every week, tagged by service in the caption, and note the town (“House soft wash, Alden Bridge”). Fresh, real photos are one of the easier ways to look active next to competitors.</li>
<li><b>Reels and TikTok.</b> The surface cleaner stripe is one of the most watchable things on the internet. Fifteen seconds, no music needed, the town in the caption.</li>
<li><b>Meta ads.</b> A before-after carousel aimed at homeowners in a tight radius, with a link to a quote form. Our {L('/services/paid-social-advertising/', 'paid social team')} runs these for service businesses, and the instant forms need qualifying questions or you’ll drown in tire-kickers (see {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'fixing bad Facebook leads')}).</li>
<li><b>Your quote follow-up.</b> Send three before-afters from the same neighborhood with every estimate.</li>
</ul>
<p>Ask before you post someone’s house. Blur the house number anyway.</p>"""),

            ("Nextdoor and door hangers: the street where you just worked", f"""<p>The best time to market to a street is the hour after you finish a job on it.</p>
<p><b>Door hangers.</b> Hit five houses on each side and the ten across the street before you leave. Print a photo of a local job, your Google rating, a starting price, a QR code to the quote form, and a “neighbor rate” that expires in 14 days. Hang them on doors, not mailboxes: per {SRC['usps']}, unstamped flyers placed in mailboxes are illegal under federal law, and only postage-paid mail delivered by authorized carriers belongs there. Also check HOA and city rules on solicitation; some neighborhoods restrict it.</p>
<p><b>Nextdoor.</b> Claim your free business page, ask happy customers to recommend you there, and answer “anyone know a good pressure washer?” threads as the business, not with a fake neighbor account. Paid Nextdoor ads can work for a hyperlocal service like this one. We weigh the pros and cons in {L('/blog/is-nextdoor-advertising-worth-it/', 'is Nextdoor advertising worth it')}.</p>
<p>Give door hangers their own QR code and promo code so you know whether they pay for the printing.</p>"""),

            ("Recurring contracts: the part that makes the business sellable", f"""<p>One-time driveway jobs pay the bills. Recurring work builds a company that’s worth something if you ever sell it, and it smooths out the slow summer.</p>
<!--fig:plan-->
<p><b>Residential plans.</b> Offer an annual house wash plus driveway at a set price, booked in the same month every year, with a small discount for signing up at the first job. Put a reminder in your CRM, and text the customer two weeks before. Get marketing-text consent separately from job updates (our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} covers why).</p>
<p><b>Commercial accounts.</b> Restaurants (dumpster pads, drive-thru lanes, patios), gas station canopies and aprons, apartment breezeways, retail center sidewalks, medical office entries along Research Forest and I-45. Property managers buy reliability: a set schedule, after-hours work, photos after every visit, one invoice a month, and a certificate of insurance ready the day they ask. Build a one-page commercial capability sheet and a commercial page on the site, then call 30 property managers within your radius. Our {L('/blog/commercial-cleaning-janitorial-marketing-houston/', 'commercial cleaning marketing post')} goes deeper on selling to facility managers.</p>
<p><b>Fleet washing.</b> HVAC and plumbing companies, landscapers, delivery operations and oilfield service yards along the Hardy Toll Road and FM 1960 all run fleets that look bad fast. Fleet managers care about scheduling around routes and about what happens to the water.</p>"""),

            ("Wastewater rules for commercial and fleet washing", f"""<p>That last point is a real selling point and a real liability. Commercial buyers increasingly ask how you handle runoff, and the answer “it goes in the drain” can lose you the account or worse.</p>
<p>The rules are mostly local, enforced under the state Water Code. {SRC['hcbmp']} (hosted by the City of Hedwig Village) says washwater must be completely collected and may not go to the storm drain, and lists penalties of up to $25,000 per day per violation under Texas Water Code Section 7.102 and up to $1,000 per day under Harris County’s storm water regulations. The {SRC['sugarland']} says discharge of pressure washing wastewater to the storm drain is prohibited and that it must be captured and hauled to a disposal facility or sent to the sanitary sewer. Inside Houston, {SRC['ms4']} says illicit discharges are handled by the Health Department with police and Public Works, and lists 311 and a hotline (713-640-4399) for reports.</p>
<p>At the state level, the closest TCEQ guidance is {SRC['rg434']}, revised June 2026. It says to get approval from your local wastewater treatment facility before discharging wash water to its sewer, and points other outdoor washing operations to TCEQ’s Small Business and Local Government Assistance section or local authorities. That’s the right call to make before you sign a fleet contract.</p>
<!--fig:rules-->
<p>How to turn it into marketing: describe your recovery setup (drain covers, berms, a vacuum recovery system, where the water goes) on your commercial page, and put a short “environmental practices” paragraph in every commercial proposal. Property managers forward that to their corporate office. We’re marketers, not environmental lawyers, so confirm the details for each city and county you work in.</p>"""),

            ("Pricing per square foot as a marketing tool", f"""<p>The most common call you get starts with “how much to wash a house?” Answering it online saves you hours of drive-by estimates and screens out the bargain hunters before they waste your Saturday.</p>
<p>You don’t have to publish a full price sheet. Publish enough to set expectations:</p>
<div class="bp-tbl"><table>
<thead><tr><th>What to publish</th><th>How to word it</th><th>Why it helps</th></tr></thead>
<tbody>
<tr><td>A starting price per service</td><td>“Most two-car driveways start at [your price]”</td><td>Answers the question in the ad and on the page</td></tr>
<tr><td>A per-square-foot range for flatwork</td><td>“Flatwork from [low] to [high] per sq ft depending on stains and access”</td><td>Lets commercial buyers budget before they call</td></tr>
<tr><td>House washing by size</td><td>“One-story homes under 2,500 sq ft from [your price]”</td><td>Homeowners know their square footage from HCAD or MCAD</td></tr>
<tr><td>A minimum job charge</td><td>“[your price] minimum per visit”</td><td>Kills the “just my front steps” calls</td></tr>
<tr><td>Add-ons</td><td>Rust removal, oil stains, gutter brightening, sealing</td><td>Raises the average ticket without a hard sell</td></tr>
</tbody></table></div>
<p>The square footage line is a nice local trick. Harris County and Montgomery County appraisal district records list a home’s living area, so a homeowner can look it up in a minute. An instant-quote form that asks for the address and square footage lets you price most houses without a visit, then confirm on arrival.</p>
<p>We aren’t publishing market rates here; there’s no reliable public source for Houston pricing, and it moves with chemical and fuel costs. If you price above the guys on Facebook, the page should say why.</p>"""),

            ("Reviews, follow-up and a first 90 days", f"""<p>Ask for the review the moment the customer sees the result. Text the link before you leave the driveway, with one line: “Thanks for having us out. If you’re happy with how it turned out, a quick Google review helps a small business a lot.” No discount for reviews, no only-asking-the-happy-ones. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has the rules and templates.</p>
<p>Then answer leads fast. A homeowner who fills out three quote forms on a Saturday morning books whoever calls back first, which is why we push owners to reply within minutes (more in {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')}).</p>
<!--fig:map-->
<p>A first 90 days for a small operator:</p>
<ul>
<li><b>Days 1 to 30.</b> Rebuild the Google profile (services, photos, hours, service area). Build service pages and one HOA-notice page. Set up call tracking and a quote form that asks for address and square footage. Start the review text on every job.</li>
<li><b>Days 31 to 60.</b> Launch search ads on house washing, driveway and roof cleaning with the full negative list. Start door hangers on every job street with a tracked QR code. Post before-afters weekly.</li>
<li><b>Days 61 to 90.</b> Launch the annual plan offer. Build the commercial page and capability sheet, and start calling property managers. Read the search terms report weekly and cut what isn’t booking.</li>
</ul>
<p>If you’d like a senior strategist to build that plan around your trucks, towns and goals, <a href="/contact/">get in touch</a>. And if you also pour or repair flatwork, our {L(CC, 'concrete contractor marketing post')} covers that side.</p>"""),
        ],
        "faq": [
            ("How do I get more pressure washing customers in Houston?",
             "Start with a complete Google Business Profile that lists each service separately, with fresh before-and-after photos and steady reviews. Build a page for each service and your main towns. Run search ads on terms like house washing, roof cleaning and driveway cleaning with negatives for equipment and DIY searches. Hang door hangers on every street you work, and sell annual plans so customers return each year."),
            ("Is there a Google Local Services Ads category for pressure washing?",
             "Not as of November 2026. Google’s Local Services Ads category list has no pressure washing, power washing or soft washing category. The closest categories are window cleaning services and house cleaning services. If window cleaning is a real part of your business, check eligibility for that category in the sign-up. Otherwise, rely on regular search ads and the map pack until Google adds a washing category."),
            ("What negative keywords should a pressure washing company use?",
             "Block equipment and DIY searches first: pressure washer for sale, rental, Home Depot, Harbor Freight, psi, parts, repair, surface cleaner, soap and how to. Add job seekers (jobs, hiring, salary) and car wash terms unless you do fleet work. Then read the search terms report weekly for the first month and keep adding anything that isn’t a customer looking to hire."),
            ("Can I drain pressure washing water into the storm drain in Harris County?",
             "No. Harris County’s best-practices guidance for power washers says washwater must be collected and may not go to the storm drain, and Sugar Land says the same. Wash water generally has to be captured and hauled for disposal or sent to the sanitary sewer with the utility’s approval. Penalties can be steep, so confirm the rules with each city and county you work in."),
            ("How do pressure washers get HOA and commercial contracts in The Woodlands?",
             "For HOA-driven work, build a page and ad group for homeowners who got a mildew or maintenance notice, and offer street pricing when several neighbors book together. For commercial work, create a commercial page and one-page capability sheet covering scheduling, insurance and wastewater recovery, then call property managers for restaurants, retail centers, offices and apartments near your base."),
        ],
        "figures": {
            "season": {
                "type": "columns",
                "title": "When Houston homeowners call for exterior cleaning",
                "sub": "Relative demand by month for a residential washing company",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [30, 48, 85, 100, 92, 66, 50, 46, 60, 78, 70, 38],
                "highlight": [2, 3, 4, 9],
                "y_label": "Relative demand",
                "note": "Illustrative example based on our experience with home service accounts; storms can spike any month",
                "alt": "Column chart of illustrative monthly pressure washing demand in Houston and The Woodlands, peaking in spring and fall",
                "caption": "Spring is the rush. The fall bump before the holidays is the one competitors forget to budget for.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for pressure washing ads",
                "sub": "Add these before the first dollar goes out",
                "items": ["Equipment: pressure washer, for sale, buy, best, review", "Stores: home depot, lowes, harbor freight, northern tool", "Specs and parts: psi, gpm, pump, nozzle, hose, parts, repair", "Rentals: rent, rental, rent a pressure washer", "DIY: how to, diy, yourself, youtube, soap, surface cleaner", "Jobs: jobs, hiring, salary, near me jobs", "Car wash: car wash, self serve (unless you sell fleet work)", "Brands: ryobi, karcher, simpson, generac"],
                "alt": "Checklist of negative keywords for pressure washing Google Ads in Houston and The Woodlands",
                "caption": "“Pressure washer” is a product. “Pressure washing” is your service. The ads need to know the difference.",
            },
            "shots": {
                "type": "steps",
                "title": "Shoot before-and-afters people believe",
                "sub": "A routine for every job in Houston or The Woodlands",
                "steps": [["Mark your spot", "Stand in the same place for both shots. A crack or sprinkler head works as a marker."], ["Same light", "Shoot before and after within the same hour, or both in shade."], ["Shoot the stripe", "Ten seconds of video mid-job, half clean and half dirty."], ["Add context", "Note service, surface and neighborhood for the caption."], ["Post and reuse", "Profile photos, a Reel, the quote follow-up and the door hanger."]],
                "alt": "Five steps for shooting pressure washing before and after photos for marketing in Houston and The Woodlands",
                "caption": "Consistency is what makes a before-after convincing. Fancy cameras don’t matter.",
            },
            "plan": {
                "type": "funnel",
                "title": "Turning one job into a recurring customer",
                "stages": [["First job (driveway or house)", "100 customers"], ["Asked about an annual plan at the job", "100"], ["Signed an annual plan", "25 to 35"], ["Renewed in year two", "20 to 30"], ["Referred a neighbor", "10 to 15"]],
                "note": "Illustrative example, not a benchmark",
                "alt": "Funnel showing how a Houston pressure washing company turns one-time jobs into annual plan customers",
                "caption": "Ask every customer. The plan only works if it’s offered on the driveway, while the result is fresh.",
            },
            "rules": {
                "type": "stats",
                "title": "Wash water and roof rules to know",
                "stats": [["$25,000", "per day, Texas Water Code penalty cited by Harris County"], ["$1,000", "per day, Harris County storm water regulations"], ["15-20", "minutes of dwell time ARMA gives for roof solution"], ["0", "LSA categories for pressure washing (Nov 2026)"]],
                "note": "Sources: Harris County power washing brochure, ARMA, Google Local Services Ads category list",
                "alt": "Key wastewater, roof cleaning and ad rules for pressure washing businesses in Houston and Harris County",
                "caption": f"From {SRC['hcbmp']}, {SRC['arma']} and {SRC['lsa']}.",
            },
            "map": {
                "type": "map",
                "title": "Where a north Houston washing route might run",
                "sub": "Pick a tight radius around your base; drive time eats margin",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Magnolia", "Kingwood", "Cypress"],
                "note": "Illustrative service area for a crew based in The Woodlands",
                "alt": "Map of an illustrative pressure washing service area around The Woodlands, Spring, Conroe and Cypress in Houston",
                "caption": "Ad radius, town pages and door-hanger routes should all match the area you actually want to work.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: concrete contractors
    {
        "slug": "concrete-contractor-marketing-houston",
        "title": "Concrete Contractor Marketing in Houston: Driveways, Patios and Flatwork Leads",
        "seo_title": "Concrete Contractor Marketing in Houston: Get More Bids",
        "desc": "Concrete contractor marketing for Houston: driveway and patio leads, Google Ads keywords and negatives, permits as proof, builder bids and estimate follow-up.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b6",
        "hero": "tools",
        "hero_alt": "Illustration of construction tools for concrete contractor marketing in Houston and The Woodlands",
        "related": ["foundation-repair-marketing-houston", "fence-company-marketing-houston", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>Monday, 5:15 p.m. You’re standing in a backyard in Cypress, measuring for a patio extension. Your phone has a pour scheduled for Wednesday in Spring that the forecast now says is a 70% chance of storms. The ready-mix order needs to move. Somewhere in your truck are four estimates from last week you haven’t followed up on, and one of them was a 1,400-square-foot driveway replacement.</p>
<p>The work isn’t the problem. Most concrete contractors we talk to in Houston are good at the work and don’t have time to sell it.</p>
<p>To get more concrete jobs in Houston, rank in Google Maps for the specific work you want (driveways, patios, slabs, commercial flatwork) in the towns you want it, run search ads on high-intent terms like “driveway replacement” with negatives that filter out DIY and bag-mix shoppers, and use permits, photos and drone shots as proof. Then follow up every estimate on a schedule, and build relationships with builders and GCs so your calendar isn’t all one-off homeowners.</p>
<p>This is the playbook we’d run for a residential and light commercial concrete company working Houston, The Woodlands, Katy, Sugar Land, Pearland and the rest of the metro.</p>"""),

            ("Three kinds of concrete customers, and what each one needs to see", f"""<p>A homeowner replacing a cracked driveway, a builder pouring 30 slabs a year, and a property manager fixing a trip hazard at a strip center all need concrete. They buy it in completely different ways.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Customer</th><th>How they find you</th><th>What wins the job</th><th>Sales cycle</th></tr></thead>
<tbody>
<tr><td>Homeowner (driveways, patios, walkways, extensions)</td><td>Google search and Maps, neighbors, Nextdoor, Facebook groups</td><td>Photos of similar jobs nearby, a clear written estimate, reviews, permit handled</td><td>Days to a few weeks</td></tr>
<tr><td>Builder or GC (slabs, foundations, flatwork packages)</td><td>Referrals, bid invites, bid platforms, supplier reps</td><td>Fast, complete bids, schedule reliability, insurance and paperwork on file</td><td>Months to start; years once you’re on the list</td></tr>
<tr><td>Commercial property (parking areas, sidewalks, dumpster pads, repairs)</td><td>Search, property manager referrals, facility vendor lists</td><td>Night or weekend scheduling, phasing to keep tenants open, COI and W-9 ready</td><td>Weeks, with recurring repair work after</td></tr>
</tbody></table></div>
<p>Most concrete websites try to talk to all three at once on one page and convince none of them. Give each its own page and its own ad campaign. The homeowner page leads with photos and the estimate process. The builder page leads with capacity, crews, pump access and how fast you return bids. The commercial page leads with scheduling and safety.</p>"""),

            ("Houston clay is your best sales argument", f"""<p>Every Houston homeowner has seen a cracked driveway. Most don’t know why it cracked, and the contractor who explains it gets trusted with the replacement.</p>
<p>The short version: much of Houston sits on the Beaumont Formation, and soils formed from it are highly expansive, according to {SRC['hgs']} by a University of Houston–Clear Lake geologist. The same article points to the local cost of pavement damage, from buckled streets to broken curbs. Nationally, {SRC['hud']} cites the American Society of Civil Engineers estimate that one in four homes in the continental U.S. has been affected by expansive soils, with yearly damage above $15 billion.</p>
<p>That’s the setup for your sales pitch. Clay swells when wet and shrinks when dry, so what goes under and inside the slab matters. Put your spec on the website and in every estimate:</p>
<ul>
<li>Base preparation and how deep you go.</li>
<li>Slab thickness for driveways versus patios and walks.</li>
<li>Reinforcement (rebar size and spacing, or wire, or fiber) and why you choose it.</li>
<li>Control joint spacing and expansion joints against the house and garage slab.</li>
<li>Drainage: slope away from the house, and what you do about downspouts.</li>
</ul>
<p>A homeowner comparing your $9,800 quote to someone’s $7,200 quote can’t see the difference in the dirt. They can see it on paper. The cheaper quote rarely lists rebar spacing.</p>
<p>One boundary: if a caller is describing a cracked slab under the house, doors sticking or interior cracks, that’s foundation repair territory, which is a different trade with engineers involved. We wrote a separate {L('/blog/foundation-repair-marketing-houston/', 'foundation repair marketing guide')} for those companies. If you do both, keep the pages and ad groups separate so the leads don’t mix.</p>"""),

            ("Permits as proof: City of Houston driveway and sidewalk rules", f"""<p>Pulling the permit is a cost to you and a trust signal to the customer. Market it.</p>
<p>Per {SRC['cohdw']}, a City of Houston permit is required for a new driveway or sidewalk and for removing and replacing an existing one, along with curb and gutter work and driveway extensions. The application needs a project number, two dimensioned site plans and a copy of the survey, plus the city’s sidewalk and driveway application form. The fee starts at a $103 minimum. Inspections are required before and after concrete placement, the culvert must be in and the forms set before you schedule, the bond must be current, inspections are scheduled for the next business day (no same-day), and the permit is valid for one year.</p>
<!--fig:permit-->
<p>If the property sits in a floodplain, there may be another layer. Houston also has {SRC['cohfp']}, which asks for the site plan to show all proposed flatwork and whether it matches adjacent grade, with a mitigation plan required for fill between natural grade and the 500-year flood elevation, plus pre-construction and final floodplain inspections. After Harvey, plenty of homeowners know their flood zone. Saying “we check floodplain requirements before we quote” on your driveway page is the kind of detail that wins a Meyerland or Kingwood job.</p>
<p>Outside the city, rules vary. In The Woodlands, {SRC['wtpermit']} says improvements need prior written approval from the Residential Design Review Committee, and that some paving goes through the City of Shenandoah depending on where the house is. Unincorporated Harris and Montgomery County, Sugar Land, Pearland and Katy all have their own processes.</p>
<p>How to use this in marketing:</p>
<ul>
<li>A line in every ad: “Permits and HOA approvals handled.”</li>
<li>A short FAQ on each town page about who issues permits there.</li>
<li>A photo of the posted permit and the inspection tag in your job gallery. It looks boring to you. To a homeowner who got burned by a cash-only crew, it looks like insurance.</li>
</ul>"""),

            ("A website and Google profile that sell flatwork", f"""<p>Concrete is visual and local. Your site should feel like a portfolio organized by job type and town, with an estimate form on every page.</p>
<p>Pages we’d build first: driveway replacement, new driveways and extensions, patios (broom, stamped and exposed aggregate, only the finishes you actually do), sidewalks and walkways, slabs for shops and garages, commercial flatwork, and town pages for the five or six places you most want to work. Each job page gets five to ten photos of real jobs, the spec you used, and roughly how long it took.</p>
<p><b>Drone proof.</b> An overhead shot of a finished circular driveway or a long commercial pour sells better than any copy. If you fly it yourself for business, {SRC['faa']} rules apply: you need a Remote Pilot Certificate under Part 107, which means passing the knowledge test at an approved center (age 16 or older) and completing online recurrent training every 24 calendar months. Or hire a licensed pilot for a few hours a month and batch your best jobs.</p>
<p><b>Google Business Profile.</b> Pick the primary category that matches your main work (concrete contractor for most), add real secondary categories, list each service separately, and set a service area that matches your trucks’ actual range. Post new job photos weekly with the town in the caption. Our {L('/blog/local-seo-contractors-houston/', 'local SEO guide for Houston contractors')} covers the full setup, and our {L('/services/web-design-seo-pr/', 'web design and SEO team')} builds these sites.</p>
<p><b>Local Services Ads.</b> When we checked {SRC['lsa']} in November 2026, there was no concrete contractor category. Foundations services and General contractor are listed. Foundations services fits foundation repair work, and General contractor fits companies that really manage whole projects, so most flatwork companies should rely on regular search ads and the map pack for now. Check eligibility for your address in the sign-up rather than guessing.</p>"""),

            ("Google Ads for concrete: high-intent keywords and the negatives that save you", f"""<p>Concrete searches split cleanly into people who want to hire a contractor and people who want to buy a bag of mix. The ads have to tell them apart, and that comes down to the keyword list.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page and notes</th></tr></thead>
<tbody>
<tr><td>Driveway replacement</td><td>driveway replacement Houston, concrete driveway contractor near me, replace cracked driveway</td><td>Driveway page with spec and permit note. Usually the best-converting group.</td></tr>
<tr><td>New driveways and extensions</td><td>driveway extension Katy, widen concrete driveway, circular driveway contractor</td><td>Extensions page; mention HOA approvals.</td></tr>
<tr><td>Patios</td><td>concrete patio contractor The Woodlands, stamped concrete patio Spring TX, patio extension</td><td>Patio page with finish photos; seasonal push in late winter and spring.</td></tr>
<tr><td>Slabs</td><td>concrete slab for shed, shop slab contractor Magnolia, garage slab pour</td><td>Slab page; more rural areas like Magnolia, Montgomery and Tomball.</td></tr>
<tr><td>Commercial flatwork</td><td>commercial concrete contractor Houston, parking lot concrete repair, dumpster pad replacement</td><td>Commercial page; calls matter more than forms.</td></tr>
</tbody></table></div>
<!--fig:negatives-->
<p>Notice what’s not on the negative list: “cement.” Homeowners say “cement driveway” all the time. Blocking it would cut real customers. Block the products and materials instead.</p>
<p>Settings: use “Presence” location targeting (Locations, then Location options in campaign settings), draw the radius around where your crews will drive for the job size, and set a minimum job size in the ad copy if you don’t do small work (“Driveways and patios, 300 sq ft and up”). Track calls and form fills as conversions and import closed jobs back when you can. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} explains the setup, and the {L('/services/search-marketing/', 'search marketing team')} runs these accounts.</p>
<p>A sample responsive search ad for the driveway group:</p>
<ul>
<li>Headlines: “Concrete Driveway Replacement” / “Permits and HOA Approvals Handled” / “Rebar and Real Base Prep” / “Free Written Estimates in Houston”</li>
<li>Description: “Old driveway out, new one poured to spec for Houston clay. Photos of jobs near you. Call or request an estimate today.”</li>
</ul>"""),

            ("Builders, GCs and bid platforms: the steady side of the business", f"""<p>Homeowner jobs have the best margins. Builder and GC work fills the calendar. You want both, and the marketing for builders looks nothing like the marketing for homeowners.</p>
<p>Start with the paperwork, because that’s what gets you on a bid list:</p>
<ul>
<li>A capabilities sheet: crew count, pump access, typical monthly volume, service area, the kind of work you want.</li>
<li>A certificate of insurance and W-9 ready to send the same day.</li>
<li>A safety program in writing, even a short one.</li>
<li>References from two or three builders or supers who’ll pick up the phone.</li>
</ul>
<p>Then get on the platforms GCs use to send invites. {SRC['bc']}, Autodesk’s bid platform, says its network includes over a million construction professionals, and GCs use it to send bid invites to subs. A complete profile with your trades, service area and past projects is what gets you invited. Then bid fast and bid complete: the subs who answer every invite, even with a “no bid this time,” are the ones who get asked next time.</p>
<p>On commercial sites, know the stormwater side. {SRC['cgp']} covers construction that disturbs one acre or more (one to five acres is a small site, five or more is large), and operators must have a stormwater pollution prevention plan before work starts. Your crews’ washout practices fall under the site’s plan, and a GC remembers which sub got them a stormwater complaint.</p>
<p>Relationships still close most builder work. Supplier reps at the ready-mix plants know which builders are growing. Builder association events and the occasional lunch with a superintendent matter. And a job page on your site for every notable project gives the super something to forward to the owner. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston')} has more on selling to companies rather than homeowners.</p>"""),

            ("Estimate follow-up: where most concrete jobs are lost", f"""<p>Back to those four estimates in the truck. Concrete buyers almost always get multiple quotes. The job often goes to whoever follows up, explains the difference, and makes it easy to say yes.</p>
<!--fig:followup-->
<p>What a good estimate looks like:</p>
<!--fig:quote-->
<p>Two rules we push hard. Answer new leads within minutes, because a homeowner who submits three forms usually meets the first contractor who calls back (see {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')}). And put every estimate in a CRM with a follow-up date, even a simple one. A spreadsheet beats your memory. Tracking close rate by lead source tells you which ads bring buyers and which bring price shoppers.</p>
<p>About lead sellers: platforms like Angi and Thumbtack can fill gaps, but the leads are shared and price-driven. Our {L('/blog/angi-vs-thumbtack-leads-worth-it-contractors/', 'Angi vs. Thumbtack breakdown')} covers when they pay off.</p>"""),

            ("Seasonality, rain delays and the Houston calendar", f"""<p>Houston pours most of the year, which is an advantage over northern markets. The tradeoff is rain. June alone averages 6.09 inches at Hobby, per {SRC['nws']} (1991 to 2020 normals), and a stalled tropical system can wipe out a week of pours.</p>
<p>Rain delays aren’t just a scheduling problem. They’re a review problem. A customer who was told “Wednesday” and didn’t hear from anyone until Friday leaves a two-star review that says nothing about the quality of the driveway. Build the communication in:</p>
<ul>
<li>Put your rain-delay policy in the estimate and the contract: how you decide, when you’ll notify them, and how rescheduling works.</li>
<li>Text the customer the day before every pour with a go or no-go, and again the morning of.</li>
<li>Send a photo when forms are set, when the pour is done, and when the job is cleaned up. It cuts the “is anyone coming?” calls and gives you before-after content.</li>
</ul>
<p>For marketing, run ads with the calendar. Patio searches climb in late winter and spring when people picture summer evenings outside. Driveway replacement runs steadier but slows over the holidays. After a hard freeze or a long drought, cracked-driveway searches tend to rise, so have your driveway ads ready to scale. When you’re booked out six weeks, lower bids rather than pausing, and say “now scheduling for [month]” in the ads so the leads you do get know what to expect.</p>
<!--fig:map-->
<p>Service area matters for profit. A driveway job in Pearland is a different day than one in Montgomery if your yard is in Tomball. Most of the companies we’ve seen do best picking a side of town, building pages and ads for it, and saying no to the rest.</p>"""),

            ("Reviews, budget and a first 90 days", f"""<p>Ask for the review when you do the final walkthrough, not when the invoice clears. Text the link with a photo of their finished job. Reply to every review with specifics (“the extension by the side gate”), which helps the next customer picture their own job. The {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has templates.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>Google Ads (search)</td><td>$1,500 to $4,000</td><td>Driveway, patio and slab ad groups in a defined radius</td></tr>
<tr><td>Local SEO and website content</td><td>$750 to $2,000</td><td>Service and town pages, job galleries, profile posts</td></tr>
<tr><td>Meta ads (retargeting and local video)</td><td>$300 to $1,000</td><td>Before-after video to people who visited your site</td></tr>
<tr><td>Drone and photo</td><td>$200 to $600</td><td>A few hours a month of shooting your best jobs</td></tr>
<tr><td>CRM and follow-up tools</td><td>$50 to $300</td><td>Estimate tracking, text follow-up, review requests</td></tr>
</tbody></table></div>
<!--fig:budget-->
<p>Treat those ranges as illustrative. They aren’t quotes. A company doing mostly builder work might spend far less on ads and more on relationships and bid platforms. Click costs for home services in Houston are covered in our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'CPC benchmarks post')}.</p>
<p>A first 90 days:</p>
<ul>
<li><b>Days 1 to 30.</b> Build the driveway, patio and commercial pages with real photos and your spec. Fix the Google profile. Set up call tracking and a CRM with follow-up dates. Write the rain-delay policy into your estimate template.</li>
<li><b>Days 31 to 60.</b> Launch search ads for driveways and patios with the full negative list. Start the review text on every finished job. Shoot drone footage of your three best recent pours.</li>
<li><b>Days 61 to 90.</b> Send your capabilities sheet to 20 builders and GCs. Complete your bid platform profiles. Review close rates by source, and move budget toward whatever is producing signed jobs.</li>
</ul>
<p>If you want a senior strategist to build that plan around your crews and the side of town you want to own, <a href="/contact/">get in touch</a>. If you also run a washing crew, our {L(PW, 'pressure washing marketing post')} covers that business.</p>"""),
        ],
        "faq": [
            ("How do concrete contractors get more customers in Houston?",
             "Rank in Google Maps for the specific work you want, such as driveway replacement and patios, in the towns you serve. Build a page for each service with real job photos and your spec for Houston clay. Run search ads on high-intent terms with negatives for DIY and bag-mix shoppers. Follow up every estimate on a schedule, and build relationships with builders and general contractors for steady work."),
            ("Do I need a permit to replace a driveway in Houston?",
             "Yes, inside the City of Houston. The Houston Permitting Center requires a residential driveway, sidewalk or curb and gutter permit for new driveways and for removing and replacing existing ones. The application needs two dimensioned site plans and a survey, fees start at a $103 minimum, and inspections are required before and after the pour. Properties in a floodplain may need a separate floodplain permit."),
            ("Is there a Google Local Services Ads category for concrete contractors?",
             "Not as of November 2026. Google’s Local Services Ads category list includes Foundations services and General contractor, but no concrete contractor category. Foundations services fits foundation repair companies, and General contractor fits firms that manage whole projects. Most flatwork companies should rely on regular Google search ads and the map pack, and check eligibility for their address in the sign-up."),
            ("What keywords should a concrete company use in Google Ads?",
             "Use service and town keywords such as driveway replacement Houston, concrete patio contractor The Woodlands, driveway extension Katy and commercial concrete contractor Houston. Add negatives for products and DIY searches, like Quikrete, bags, mix, calculator, Home Depot, how to and jobs. Avoid blocking the word cement, because many homeowners say cement driveway when they mean concrete."),
            ("How do concrete subcontractors get on builder and GC bid lists in Houston?",
             "Have a capabilities sheet, certificate of insurance, W-9, safety program and references ready to send the same day. Build complete profiles on the bid platforms general contractors use, such as BuildingConnected, and answer every invite quickly, even with a no-bid. Ready-mix supplier reps and builder association events are good ways to meet builders who are growing in Houston."),
        ],
        "figures": {
            "permit": {
                "type": "stats",
                "title": "City of Houston driveway permit, by the numbers",
                "stats": [["$103", "minimum permit fee"], ["2", "required inspections, before and after the pour"], ["1 day", "processing; inspections next business day"], ["1 year", "permit validity"]],
                "note": "Source: Houston Permitting Center, residential driveway, sidewalk or curb and gutter permit",
                "alt": "Key facts about the City of Houston residential driveway and sidewalk permit for concrete contractor marketing",
                "caption": f"From the {SRC['cohdw']}. Check for floodplain and HOA requirements too.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for concrete contractor ads",
                "sub": "Block shoppers and DIYers, keep the homeowners",
                "items": ["Products: quikrete, sakrete, bag, bags, mix, ready mix price", "Stores: home depot, lowes, menards", "Math: calculator, how many yards, cost per yard", "DIY: how to, diy, yourself, youtube, forms, tools", "Repair products: crack filler, sealer, resurfacer, patch", "Jobs: jobs, hiring, finisher jobs, salary, school", "Wrong work: asphalt, gravel, pavers (unless you do them)", "Keep: cement (homeowners say cement driveway)"],
                "alt": "Checklist of negative keywords for concrete contractor Google Ads in Houston and The Woodlands",
                "caption": "Read the search terms report weekly for the first month and keep adding.",
            },
            "followup": {
                "type": "steps",
                "title": "Estimate follow-up for concrete jobs",
                "sub": "A cadence that wins jobs without being pushy",
                "steps": [["Same day", "Send the written estimate with photos of a similar job nearby."], ["Day 2", "Text: any questions about the spec or schedule?"], ["Day 5", "Call. Offer to walk the site again or compare quotes line by line."], ["Day 10", "Share your next open pour dates and the estimate expiry."], ["Day 30", "Last check-in. Then add them to a seasonal email list."]],
                "alt": "Five-step estimate follow-up schedule for concrete contractors in Houston and The Woodlands",
                "caption": "Most competitors stop after the estimate. The second and third touch are where you win.",
            },
            "quote": {
                "type": "compare",
                "title": "Concrete estimates: vague vs. specific",
                "left": {"title": "The vague quote", "items": ["“Remove and replace driveway, $7,200”", "No mention of base or rebar", "Permit not mentioned", "No rain-delay policy", "Cash discount, no contract"]},
                "right": {"title": "The quote that wins", "items": ["Square footage, thickness and finish listed", "Base prep, rebar size and spacing, joints", "Permit and HOA approval included", "Rain-delay and rescheduling terms", "Photos of similar jobs nearby"]},
                "alt": "Comparison of vague and specific concrete driveway estimates for contractors in Houston",
                "caption": "A specific estimate lets the homeowner justify paying more. A vague one invites a price fight.",
            },
            "map": {
                "type": "map",
                "title": "Pick a side of town",
                "sub": "Drive time to the pour site eats into flatwork margins",
                "highlight": ["Tomball", "Cypress", "Spring", "The Woodlands", "Magnolia", "Katy"],
                "note": "Illustrative service area for a concrete company based in northwest Houston",
                "alt": "Map of an illustrative northwest Houston service area for a concrete contractor, including Tomball, Cypress and Katy",
                "caption": "Your ads, town pages and Google service area should all describe the same territory.",
            },
            "budget": {
                "type": "bars",
                "title": "Example monthly marketing mix",
                "sub": "Residential-heavy concrete company, midpoint of each range",
                "items": [["Google Ads", 2750, "$2,750"], ["Local SEO and content", 1375, "$1,375"], ["Meta ads", 650, "$650"], ["Drone and photo", 400, "$400"], ["CRM and follow-up", 175, "$175"]],
                "highlight": [0],
                "note": "Illustrative ranges, not quotes",
                "alt": "Bar chart of an illustrative monthly marketing budget for a Houston concrete contractor",
                "caption": "Midpoints of the table above. Shift budget toward whatever produces signed jobs.",
            },
        },
    },
]
