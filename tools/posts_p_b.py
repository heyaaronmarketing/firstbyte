"""Batch 16 (module p_b): flooring company marketing in Houston and The Woodlands, countertop fabricator marketing in
Houston, and boat dealer and marina marketing on Lake Conroe.

Research, flooring post: Community Impact on the final HCFCD Harvey report (154,170 Harris County homes flooded, just
under half outside the 100- and 500-year floodplains, 36% insured for flood); Texas Tribune on Beryl (Cat 1 landfall
near Matagorda at about 4 a.m. July 8, 2024; 2.26 million CenterPoint outages); ABC13 on Houston Public Works leak
calls doubling in the July 2022 drought as soil shifted; TDI flood insurance page (homeowners policies exclude flood,
30-day wait, $250,000 building / $100,000 contents); TDI on contractors waiving deductibles (illegal); Google's
Local Services Ads category list (Flooring services, Countertop services); Google Business Profile guidelines on
hybrid and service-area businesses (about 2 hours of driving); CFPB Regulation Z 12 CFR 1026.24(d) triggering terms;
Jon Loomer on Meta's Financial Products and Services special ad category; Google Maps prohibited content policy.
Countertop post: 2025 U.S. Houzz Kitchen Trends Study (engineered quartz 39%, granite 19%, quartzite 11%); OSHA
general industry silica page (PEL 50 ug/m3, action level 25, exposure plan, medical exams every three years); OSHA
State Plans page (Texas is federal OSHA); AIHA on the March 2026 OSHA/NIOSH countertop hazard alert (granite up to
50% silica, engineered stone and quartzite among the highest, wet methods, low-silica products); CDC MMWR Nov. 2023
California silicosis surveillance (7 of 19 confirmed cases tied to engineered stone, median age 44); Public Health
Watch on the Aug. 2024 $52.4 million Los Angeles verdict; Safe Work Australia on the July 1, 2024 ban.
Boat post: TWDB Lake Conroe page (19,640 acres at conservation pool, 201 ft msl, completed Jan. 1973, Montgomery and
Walker counties); SJRA history page (about 150 miles of shoreline); SJRA flood mitigation FAQ (seasonal lowering to
200.5/200.0 ft through 2023); Houston Boat Shows and Houston Auto Show sites (combined AutoBoative show Jan. 27-31,
2027 at NRG Park); Google vehicle ads policies (boats excluded) and the May 2026 ATV/UTV/trailer expansion; Meta
Marketing API vehicles catalog reference (vehicle_type BOAT); CBT News on Meta removing business Page vehicle listings
from Marketplace (Jan. 2023); Boats Group about page (Boat Trader, boats.com, YachtWorld); TPWD dealer license
supplemental info (5 vessels/year, $500 two-year fee, license per location, displayed, Occupations Code 2352.0522
territory advertising rule); TPWD registration and titles FAQ (6.25% tax collected by TPWD, 45 working days, renew
90 days early); TPWD mandatory boater education (born on or after Sept. 1, 1993; over 15 hp); NMMA June 2026
powerboat report (156,754 new powerboats in 2025, pontoons 33.6%).
Not used (couldn't verify): 2027 Southwest International Boat Show dates; whether Meta's 2023 Marketplace change
covers boats specifically; Google Merchant Center unit pricing details for flooring.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # flooring post
    "harvey": A("https://communityimpact.com/news/2018/06/08/hurricane-harvey-damage-report-harris-county", "Community Impact’s summary of the Flood Control District’s final Harvey report"),
    "beryl": A("https://www.texastribune.org/2024/07/08/hurricane-beryl-texas-damage-updates-rain/", "The Texas Tribune"),
    "leaks": A("https://abc13.com/amp/post/houston-public-works-drought-2022-water-leak-pipe-burst/12044204/", "ABC13"),
    "tdi_flood": A("https://www.tdi.texas.gov/consumer/storms/flood-insurance.html", "the Texas Department of Insurance"),
    "tdi_ded": A("https://tdi.texas.gov/tips/can-a-contractor-waive-my-deductible.html", "TDI is blunt about it"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "gbp": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s Business Profile guidelines"),
    "regz": A("https://www.consumerfinance.gov/rules-policy/regulations/1026/24/", "Regulation Z, section 1026.24"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    # countertop post
    "houzz": A("https://www.houzz.com/magazine/see-the-top-trends-in-kitchen-cabinets-countertops-and-more-stsetivw-vs~179668579", "the 2025 U.S. Houzz Kitchen Trends Study"),
    "osha": A("https://www.osha.gov/silica-crystalline/general-industry-maritime", "OSHA’s general industry silica standard"),
    "osha_tx": A("https://www.osha.gov/stateplans", "OSHA’s State Plans page"),
    "aiha": A("https://www.aiha.org/news/260305-osha-niosh-urge-countertop-fabrication-shops-to-adopt-silica-controls", "AIHA’s summary of the 2026 OSHA/NIOSH hazard alert"),
    "mmwr": A("https://www.cdc.gov/mmwr/volumes/72/wr/mm7246a4.htm", "a November 2023 CDC report"),
    "verdict": A("https://publichealthwatch.org/2024/08/08/jury-awards-52-4m-in-case-against-artificial-stone-countertop-makers/", "Public Health Watch"),
    "aus": A("https://www.safeworkaustralia.gov.au/esban", "Safe Work Australia"),
    # boat post
    "twdb": A("https://www.twdb.texas.gov/surfacewater/rivers/reservoirs/conroe", "the Texas Water Development Board"),
    "sjra": A("https://www.sjra.net/about/history/", "the San Jacinto River Authority"),
    "lower": A("https://www.sjra.net/wp-content/uploads/2022/01/Flood-Mitigation-Strategy-FAQs_Compromise_2022.pdf", "SJRA’s flood mitigation FAQ"),
    "hbs": A("https://houstonboatshows.com/", "Houston Boat Shows"),
    "has": A("https://www.houstonautoshow.com/about-the-show/", "the Houston Auto Show"),
    "gva": A("https://support.google.com/merchants/answer/11544533?hl=en", "Google’s vehicle ads policies"),
    "gva26": A("https://support.google.com/merchants/answer/17091241", "a May 2026 expansion"),
    "metacat": A("https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/product-catalog/vehicles", "Meta’s vehicle catalog reference"),
    "mkt": A("https://www.cbtnews.com/new-facebook-marketplace-rule-restricts-business-pages-from-listing-cars/", "CBT News"),
    "bg": A("https://www.boatsgroup.com/?p=17", "Boats Group"),
    "tpwd_dealer": A("https://tpwd.texas.gov/publications/pwdforms/media/pwd_0310_a0900_supplemental_info.pdf", "TPWD’s dealer license packet"),
    "tpwd_title": A("https://tpwd.texas.gov/faq/fishboat/boat/registration_and_titles/", "TPWD’s registration and titling FAQ"),
    "tpwd_ed": A("https://tpwd.texas.gov/regulations/outdoor-annual/boating/mandatory-boater-education-requirements", "TPWD’s boater education rules"),
    "nmma": A("https://www.nmma.org/press/article/25543", "NMMA’s 2025 powerboat sales report"),
}

FLOOR = "/blog/flooring-company-marketing-houston-the-woodlands/"
COUNTER = "/blog/countertop-fabricator-marketing-houston/"
BOAT = "/blog/boat-dealer-marina-marketing-lake-conroe/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: flooring
    {
        "slug": "flooring-company-marketing-houston-the-woodlands",
        "title": "Flooring Company Marketing in Houston and The Woodlands: Showroom, Shop-at-Home and the Water-Damage Call",
        "seo_title": "Flooring Company Marketing in Houston & The Woodlands",
        "desc": "Flooring company marketing for Houston and The Woodlands: showroom vs. shop-at-home, water damage jobs, Google Ads, sample funnels and financing ad rules.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b2",
        "hero": "remodel",
        "hero_alt": "Illustration of a remodeled room for flooring company marketing in Houston and The Woodlands",
        "related": ["kitchen-bath-remodeling-marketing-the-woodlands", "water-damage-restoration-marketing-houston", "how-to-get-more-remodeling-leads-houston"],
        "sections": [
            (None, f"""<p>Thursday, 4:40 p.m., at a flooring showroom off FM 1960. A woman walks in holding a strip of swollen laminate in a grocery bag. A slab leak under her kitchen, the restoration crew pulled 900 square feet of flooring on Monday, the adjuster’s estimate is in her email, and her in-laws land at Bush Intercontinental in three weeks. She wants to know what’s in stock.</p>
<p>At the same moment your shop-at-home rep is in a living room in Cinco Ranch with a sample case, on an appointment that came from a Google ad. The homeowner is “just getting ideas.”</p>
<p>Both of those people count as one lead in your Google Ads account. They are not the same customer, and treating them the same is where most flooring company marketing goes sideways.</p>
<p>Flooring marketing that works in Houston and The Woodlands sorts customers by what triggered the purchase, then sends each one to the page, the offer and the salesperson that fits. Choice remodelers get inspiration, samples and patience. Water-damage replacements get speed and in-stock inventory. Builders and remodelers get pricing and a crew that shows up. And the whole thing gets judged on measured appointments that turned into signed jobs.</p>"""),

            ("Three flooring customers in Houston, and why they need different marketing", f"""<p>Almost every flooring dealer we talk to describes their customers the same way: homeowners. That’s true and not very useful. The trigger matters more than the demographic.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Customer</th><th>What set it off</th><th>Typical searches</th><th>What closes the job</th></tr></thead>
<tbody>
<tr><td>Choice remodeler</td><td>Tired of carpet, selling the house, a kitchen remodel next door</td><td>“lvp flooring near me,” “hardwood floors The Woodlands,” “tile showroom Katy”</td><td>Samples at home, a clear installed price, photos of finished local rooms</td></tr>
<tr><td>Water-damage replacement</td><td>Slab leak, burst supply line, storm water, a failed water heater</td><td>“flooring replacement after water damage,” “flooring in stock Houston,” “insurance flooring replacement”</td><td>Install date, in-stock material, comfort with adjuster estimates</td></tr>
<tr><td>Trade account</td><td>A builder, remodeler, property manager or investor with a schedule</td><td>Rarely searches; finds you through referrals and outreach</td><td>Price sheets, reliable crews, fast turns between tenants</td></tr>
</tbody></table></div>
<p>The choice remodeler might take two months and visit three showrooms. The water-damage customer often decides in two days, and the first company that answers with a real install date usually wins. The trade account doesn’t care about your Instagram at all.</p>
<p>One website and one campaign can’t talk to all three. You need separate landing pages and ad groups, and ideally separate phone numbers so you can see which trigger is paying the bills.</p>"""),

            ("Showroom, shop-at-home or both: set up Google Business Profile to match", f"""<p>The map pack drives a lot of flooring calls, and the setup depends on how you sell.</p>
<p>If you have a showroom that’s staffed during posted hours, show the address. If you also measure and sell in homes, you’re a hybrid, and {SRC['gbp']} allow you to show the storefront and add a service area. A shop-at-home operation without a staffed showroom should hide its address and list only a service area. Google says the service area shouldn’t extend much past about two hours of driving from your base, which covers the whole Houston metro from almost anywhere, so draw it honestly around where your crews actually go.</p>
<!--fig:showroom-->
<p>Pick the primary category that matches the money. A store that sells and installs might lead with a flooring store category and add flooring contractor, carpet store or tile store as secondary categories if they’re true. Search the category list in your profile and choose the closest match; Google adds and renames categories often enough that we don’t trust anyone’s old list, including our own.</p>
<p>Then do the boring parts well. Photos of the showroom from the parking lot, so people can find the door. A product section for LVP, tile, hardwood and carpet with “from” prices per square foot installed. An appointment link that books a measure or a showroom visit. Saturday hours that are real. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest.</p>
<p>Shop-at-home companies can win in the map pack without a storefront, but they lean harder on reviews and on the service pages of their website, because there’s no address near the searcher to help them.</p>"""),

            ("Water damage jobs: Harvey, Beryl, slab leaks and the replacement call", f"""<p>Houston generates water-damage flooring work every year, and some years it generates a flood of it.</p>
<p>Hurricane Harvey flooded 154,170 homes in Harris County, just under half of them outside the 100- and 500-year floodplains, and only 36% of those homes had flood insurance, according to {SRC['harvey']}. Hurricane Beryl made landfall near Matagorda as a Category 1 early on July 8, 2024, and CenterPoint faced 2.26 million outages, per {SRC['beryl']}. Beryl was more of a wind, roof-leak and fallen-tree storm than a flood, but roof leaks ruin floors too, weeks after the storm.</p>
<!--fig:water-->
<p>The steady work comes from leaks. Clay soil swells and shrinks, and pipes under slabs pay for it. During the dry summer of 2022, Houston Public Works said water leak calls had doubled in a week and blamed drought-shifted soil, as reported by {SRC['leaks']}. Those were city lines, but plumbers see the same pattern under houses, and the flooring calls follow the plumbing calls by a week or two.</p>
<p>What that means for your marketing:</p>
<ul>
<li>Build one water-damage replacement page. Say what you stock, how fast you can install, that you work from adjuster estimates, and that you check subfloor moisture before installing. Put the phone number at the top.</li>
<li>Run a small, always-on ad group for replacement searches, and have a bigger budget ready to switch on after a named storm or a hard freeze. Don’t wait until the day after to write the ads.</li>
<li>Partner with restoration companies and plumbers. They pull the wet floor and the homeowner asks them who should put it back. Our {L('/blog/water-damage-restoration-marketing-houston/', 'water damage restoration marketing post')} explains how those companies market, which tells you how to pitch them.</li>
<li>Keep a short “in stock, installs this week” list on the site and update it on Mondays.</li>
</ul>
<p>And know the coverage basics so your team doesn’t overpromise. A homeowners policy doesn’t cover flood, flood policies usually carry a 30-day waiting period, and NFIP building coverage tops out at $250,000, per {SRC['tdi_flood']}. Plumbing leaks are a different claim under the homeowners policy, with its own terms. Your salespeople shouldn’t interpret anyone’s policy. They should know enough to ask the right question.</p>"""),

            ("Insurance jobs without the headaches", f"""<p>Insurance work is good business for flooring companies that handle it cleanly and miserable for the ones that don’t.</p>
<p>The customer has an estimate with line items for removal, material and installation, usually priced per square foot. They want to know if you can do the job for that number, and if not, what the difference buys them. Train one person to read those estimates and answer in a day. That single skill wins more insurance work than any ad.</p>
<p>The legal line is simple. In Texas it’s illegal for a contractor to waive a homeowner’s deductible or offer rebates or credits that cover it, and {SRC['tdi_ded']}: offenders can be fined or jailed. So “we’ll cover your deductible” never goes in an ad, a script or a text. “We work directly from your adjuster’s estimate” is fine.</p>
<p>A few other things we’d put on the insurance page:</p>
<ul>
<li>How you handle supplements when the estimate misses something, like stairs or transitions.</li>
<li>Whether you’ll match flooring in adjoining rooms, and how you price it if the claim doesn’t cover it.</li>
<li>When payment is due and how you handle mortgage-company checks, which can take a while.</li>
</ul>
<p>Homeowners in this situation are stressed and already tired of phone calls. A page that answers those three things before they ask reads like competence.</p>"""),

            ("Builder, remodeler and property manager accounts", f"""<p>Trade accounts smooth out the months when retail traffic drops. North Houston has plenty of them: production and custom builders along I-45 and the Grand Parkway, kitchen and bath remodelers in The Woodlands and Kingwood, and property managers turning rentals in Spring and Conroe every week.</p>
<p>Ads don’t win these accounts. Outreach and reliability do.</p>
<ol>
<li>Build a trade page with what you install, crew capacity, typical lead time, how you quote, and a contact who answers.</li>
<li>Make a list of 30 local remodelers and property managers. The {L('/blog/kitchen-bath-remodeling-marketing-the-woodlands/', 'kitchen and bath remodelers')} who don’t install flooring themselves are the easiest yes.</li>
<li>Offer a price sheet for your core LVP and carpet lines, refreshed quarterly, so they can bid without calling you.</li>
<li>Promise a turnaround on rental turns and keep it. Property managers count vacant days.</li>
<li>Send a short monthly email with new lines, discontinued colors and lead times.</li>
</ol>
<p>Track jobs and revenue per account per month. Two good remodelers can be worth more than your entire Meta budget, and it helps to know which two.</p>"""),

            ("Google Ads for flooring in Houston: search, Shopping and Local Services Ads", f"""<p>Search is where flooring buyers tell you what they want. Split campaigns by material and by trigger, and send each to its own page.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>LVP / vinyl plank</td><td>lvp flooring installation, luxury vinyl plank near me, waterproof flooring Spring TX</td><td>LVP page with installed “from” price and sample request</td></tr>
<tr><td>Tile</td><td>tile installation The Woodlands, porcelain tile store near me, wood look tile</td><td>Tile page with showroom booking</td></tr>
<tr><td>Hardwood</td><td>hardwood flooring installers, engineered hardwood Kingwood, hardwood refinishing</td><td>Hardwood page with finished-room gallery</td></tr>
<tr><td>Carpet</td><td>carpet installation near me, carpet store Cypress, carpet replacement</td><td>Carpet page with whole-house pricing</td></tr>
<tr><td>Water damage replacement</td><td>flooring replacement water damage, flooring after slab leak, flooring in stock</td><td>Replacement page with phone at top</td></tr>
</tbody></table></div>
<p>Negatives matter more than usual, because flooring searches are full of DIY shoppers and job seekers.</p>
<!--fig:negatives-->
<p><b>Local Services Ads.</b> {SRC['lsa']} includes a Flooring services category, so test it. You pay per lead rather than per click, and you can dispute junk. It tends to suit installers with strong reviews more than showrooms selling material only.</p>
<p><b>Shopping-style ads.</b> If you sell material online or publish prices for in-stock lines, a Merchant Center feed lets those products appear in Shopping results. It works best for a dealer with real per-box or per-square-foot pricing and a pickup option. For install-only companies, Shopping is the wrong tool, and Performance Max without a feed tends to spend on broad, cheap placements before you’ve learned anything. We’d start with Search.</p>
<p>Settings worth checking: target “people in or regularly in” your locations rather than people interested in them, keep your radius to where crews actually go, and track calls and sample requests as conversions. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} will give you a sense of click costs, and our {L('/services/search-marketing/', 'search marketing team')} runs these accounts if you’d rather not.</p>"""),

            ("Sample request funnels that turn browsers into measure appointments", f"""<p>The choice remodeler isn’t ready to book a measure on the first visit. Ask them for one anyway and most will leave. Offer samples instead.</p>
<p>A sample request is a small yes. Five samples mailed or ready for pickup, in exchange for a name, phone, address and a rough project size. Then the follow-up does the selling:</p>
<ul>
<li>Text within an hour confirming the samples and asking which room they’re for.</li>
<li>A call when the samples arrive, offering a measure with a specific day.</li>
<li>An email a week later with installed photos of the same products in local homes.</li>
<li>A retargeting audience of sample requesters on Meta, showing finished rooms and reviews.</li>
</ul>
<!--fig:funnel-->
<p>Speed matters here more than in most trades. A sample request that sits until Monday competes with every big-box store that already texted them. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up setup.</p>
<p>On Meta, run sample offers with short videos: a plank click-locking into place, a before-and-after of a dated Kingwood living room, water poured on a waterproof LVP sample. Instant forms bring volume; a website form brings better leads. If the leads are junk, add a qualifying question about timeline. The fixes in {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'our post on bad Facebook leads')} apply directly.</p>"""),

            ("Financing ads: what you can say and what triggers disclosures", f"""<p>Financing sells flooring. A $9,000 whole-house LVP job is a different conversation at a monthly number. The ads are where companies get sloppy.</p>
<p>Under {SRC['regz']}, if a closed-end credit ad states certain terms (the down payment, the number of payments or repayment period, a payment amount, or a finance charge), it must also state the down payment, the repayment terms and the APR. So “$129 a month” on a Facebook ad without the rest is a problem. “Financing available” states none of those terms.</p>
<!--fig:financing-->
<p>Many flooring financing programs are store cards, which are open-end credit with their own advertising section in the same regulation. Your financing provider almost always has approved ad language. Use it word for word and keep a copy.</p>
<p>Meta adds its own layer. Ads promoting credit offers fall under the Financial Products and Services special ad category, which locks age and gender targeting, requires at least a 15-mile radius and removes lookalike audiences, according to {SRC['loomer']}. If financing is the headline, expect to run under it. If financing is a line in the copy of a flooring ad, keep it general. Our {L('/blog/kitchen-bath-remodeling-marketing-the-woodlands/', 'kitchen and bath remodeling post')} has more on financing messages for bigger projects.</p>"""),

            ("Reviews that mention the install, not just the sale", f"""<p>Most flooring companies ask for a review at the wrong moment, which is the sale. The customer hasn’t seen the floor yet.</p>
<p>Ask the day after installation, by text, with a direct link. The installer can mention it as they leave: “The office will text you a link. If we did right by you, a review helps us a lot.” That’s enough.</p>
<p>The rules, from {SRC['gpol']}: no discounts or gifts for reviews, no asking only the happy customers, and no discouraging negative reviews. Send every customer the same link.</p>
<p>Reply to reviews with specifics, mention the product and the area when the customer did (“Glad the oak-look LVP worked in the Sterling Ridge house”) and handle the bad ones calmly with an offer to come back out. Prospects read your replies to complaints more closely than the five-star reviews. The {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has templates.</p>"""),

            ("Measure appointment-to-sale, then spend", f"""<p>Lead counts lie in flooring. A shop-at-home company can buy 200 Meta leads a month and close nine. A showroom can get 40 search calls and close 15. The useful number is cost per signed job by source.</p>
<p>Here’s an illustrative month for a single-showroom dealer with a shop-at-home option. It isn’t a benchmark, just a picture of what to count.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Source</th><th>Leads</th><th>Measures set</th><th>Measures run</th><th>Sold</th></tr></thead>
<tbody>
<tr><td>Google Search</td><td>70</td><td>34</td><td>29</td><td>12</td></tr>
<tr><td>Local Services Ads</td><td>25</td><td>14</td><td>12</td><td>5</td></tr>
<tr><td>Meta sample offers</td><td>110</td><td>22</td><td>16</td><td>4</td></tr>
<tr><td>Restoration and plumber referrals</td><td>12</td><td>11</td><td>11</td><td>8</td></tr>
<tr><td>Trade accounts</td><td>n/a</td><td>n/a</td><td>n/a</td><td>9 jobs</td></tr>
</tbody></table></div>
<p>To build that table you need tracked numbers per channel, a CRM that holds the original source, and a measure appointment marked as set, run and sold. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'call and form tracking guide')} covers the plumbing. Once it’s real, send sold jobs back to Google Ads as offline conversions so the bidding learns from buyers, not browsers.</p>
<!--fig:plan-->
<p>Mistakes we see most: one landing page for everything, financing ads with a monthly payment and nothing else, sample requests followed up on Monday, review requests at the sale, and a Google Ads account still targeting “people interested in” Houston, which includes people in Ohio.</p>
<p>If you want a senior strategist to look at how you’re set up now and build a plan around your showroom, crews and trade accounts, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do flooring companies get more customers in Houston?",
             "Split your marketing by what triggered the purchase. Choice remodelers respond to samples, local project photos and clear installed prices. Water-damage customers need fast install dates and in-stock material, often found through Google and restoration company referrals. Builders, remodelers and property managers come from outreach and reliable crews. Track each source to measures run and jobs sold, and spend more where the cost per sold job is lowest."),
            ("Should a flooring company in The Woodlands show its address on Google?",
             "Show it if you have a showroom staffed during posted hours. If you also sell in homes, Google’s guidelines let you show the storefront and add a service area. A shop-at-home business without a staffed location should hide its address and list a service area, which Google says shouldn’t extend much beyond about two hours of driving from your base."),
            ("Are Google Local Services Ads available for flooring?",
             "Yes. Google’s Local Services Ads category list includes Flooring services. You pay per lead instead of per click and can dispute leads that weren’t real customers. LSA ranking leans on reviews and responsiveness, so installers with a strong Google rating tend to do best. Test it beside a regular search campaign and compare cost per sold job, not just cost per lead."),
            ("Can a flooring company advertise monthly payments?",
             "Yes, with the full disclosures. Under Regulation Z, an ad that states a payment amount, the number of payments, a down payment or a finance charge must also state the down payment, repayment terms and APR. General phrases like financing available don’t trigger that. On Meta, credit offers fall under the Financial Products and Services category, which limits targeting. Use your financing provider’s approved ad language."),
            ("Can a flooring contractor cover my insurance deductible in Texas?",
             "No. The Texas Department of Insurance says it is illegal for contractors to waive a homeowner’s deductible or offer rebates or credits that cover it, and violators can be fined or jailed. A flooring company can work directly from your adjuster’s estimate and explain what upgrades cost beyond the claim, but it can’t absorb the deductible or advertise that it will."),
        ],
        "figures": {
            "showroom": {
                "type": "compare",
                "title": "Showroom-first vs. shop-at-home marketing",
                "left": {"title": "Shop-at-home first", "items": ["Address hidden, service area only", "Ranks on reviews and service pages", "Sample case does the showing", "Meta lead forms drive volume", "Measure booked on the first call"]},
                "right": {"title": "Showroom plus in-home (hybrid)", "items": ["Storefront address and a service area", "Map pack near the showroom", "Showroom visits and in-home measures", "Search ads to material pages", "Book a visit or a measure, your choice"]},
                "alt": "Comparison of shop-at-home and showroom flooring company marketing in Houston and The Woodlands",
                "caption": "Most Houston dealers do best as hybrids, but only if the showroom is really staffed during posted hours.",
            },
            "water": {
                "type": "stats",
                "title": "Why Houston keeps replacing floors",
                "stats": [["154K", "Harris County homes flooded in Harvey"], ["36%", "of those homes had flood insurance"], ["2.26M", "CenterPoint outages after Beryl"], ["30 days", "typical flood policy waiting period"]],
                "note": "Sources: HCFCD via Community Impact, Texas Tribune, TDI",
                "alt": "Stats on Harvey flooding, Beryl outages and flood insurance that drive flooring replacement demand in Houston",
                "caption": f"From {SRC['harvey']}, {SRC['beryl']} and {SRC['tdi_flood']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for flooring ads",
                "sub": "Add these before launch, then read search terms weekly",
                "items": ["DIY: how to install, diy, yourself, youtube", "Tools: tile saw, flooring nailer, rental", "Jobs: installer jobs, hiring, salary, apprentice", "Big-box names if you don’t price-match", "Free and cheap, unless you sell on price", "Materials you don’t carry: epoxy, rubber, cork", "Commercial terms if you only do homes", "Cleaning: carpet cleaning, grout cleaning"],
                "alt": "Checklist of negative keywords for flooring company Google Ads in Houston and The Woodlands",
                "caption": "Flooring searches are heavy with DIY and job seekers. Cut them on day one.",
            },
            "funnel": {
                "type": "funnel",
                "title": "A sample request funnel",
                "stages": [["Sample requests", "100"], ["Reached within an hour", "80"], ["Measure booked", "35"], ["Measure run", "28"], ["Sold", "11"]],
                "note": "Illustrative example",
                "alt": "Funnel from sample request to sold flooring job for a showroom in Houston and The Woodlands",
                "caption": "The biggest drop is usually between request and first contact. That one’s fixable.",
            },
            "financing": {
                "type": "compare",
                "title": "Financing copy: what triggers full disclosures",
                "left": {"title": "Triggers APR and terms", "items": ["Only $129 a month", "48 easy payments", "Just 10% down", "Less than $300 in interest", "Pay it off in 3 years"]},
                "right": {"title": "General statements", "items": ["Financing available", "Ask about financing options", "Apply online in minutes", "Approved provider’s full disclosure", "Monthly options at the showroom"]},
                "alt": "Comparison of flooring financing ad wording under Regulation Z for Houston flooring companies",
                "caption": f"Based on the closed-end triggering terms in {SRC['regz']}. Store-card programs have their own rules; use the provider’s language.",
            },
            "plan": {
                "type": "steps",
                "title": "A first 90 days for a Houston flooring dealer",
                "steps": [["Days 1-15", "Fix the Business Profile, hours, categories and photos."], ["Days 15-30", "Build material, water-damage, insurance and trade pages."], ["Days 30-45", "Launch Search by material with negatives; tracked numbers."], ["Days 45-60", "Add sample requests, the one-hour text and Meta retargeting."], ["Days 60-90", "Test Local Services Ads; send sold jobs back as conversions."]],
                "alt": "Steps in a first 90 day marketing plan for a flooring company in Houston and The Woodlands",
                "caption": "Trade outreach runs alongside all of this. It costs time, not ad spend.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: countertops
    {
        "slug": "countertop-fabricator-marketing-houston",
        "title": "Countertop Fabricator Marketing in Houston: Trade Accounts, Homeowner Leads and the Slab Yard",
        "seo_title": "Countertop Fabricator Marketing in Houston",
        "desc": "Countertop fabricator marketing in Houston: trade accounts, homeowner Google Ads, Instagram install videos, slab yard visits, silica safety and reviews.",
        "category": "Local marketing",
        "icons": ["Instagram", "Google Ads", "Google Business Profile"],
        "art": "b4",
        "hero": "tools",
        "hero_alt": "Illustration of fabrication tools for countertop fabricator marketing in Houston and The Woodlands",
        "related": ["kitchen-bath-remodeling-marketing-the-woodlands", "interior-designer-marketing-the-woodlands-houston", "home-builder-marketing-houston-montgomery-county"],
        "sections": [
            (None, f"""<p>Tuesday, 9:15 a.m., at a fabrication shop off the Hardy Toll Road. The bridge saw is cutting a white quartz for a builder’s spec home in Conroe. Two installers are loading a granite vanity bound for Kingwood. Out in the slab yard, a homeowner from The Woodlands is holding her phone up next to a quartzite, comparing it to a photo she saved from Instagram. Her designer is on speakerphone.</p>
<p>Meanwhile the office phone rings with a remodeler asking if you can template Thursday instead of next week.</p>
<p>That’s a fabricator’s marketing problem in one morning. Most of your volume comes from trade accounts that never see an ad, but your best margins often come from homeowners who found you on Google or Instagram, and both groups judge you on the same thing: whether the template, fabrication and install dates you promised actually happen.</p>
<p>Countertop fabricator marketing in Houston works when you keep the builder, remodeler and designer pipeline full with outreach and reliability, and buy homeowner searches with ads that point to a bookable slab yard visit. Show the install on video and publish a timeline you keep. Be open about how you handle silica dust, because more people are asking.</p>"""),

            ("Two businesses under one roof: trade accounts and homeowners", f"""<p>A fabrication shop is really two businesses sharing a saw.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Customer</th><th>How they find you</th><th>What they care about</th><th>Marketing that works</th></tr></thead>
<tbody>
<tr><td>Production and custom builders</td><td>Bids, referrals, purchasing managers</td><td>Price per square foot, schedule, no callbacks</td><td>Outreach, price sheets, punctual crews</td></tr>
<tr><td>Remodelers and kitchen designers</td><td>Referrals, slab yard reputation, Instagram</td><td>Lead times, seam quality, how you treat their client</td><td>Trade program, visit-ready slab yard, tagged install videos</td></tr>
<tr><td>Interior designers</td><td>Instagram, word of mouth, showrooms</td><td>Material selection, bookmatching, a clean install</td><td>Portfolio, designer appointments, credit on social posts</td></tr>
<tr><td>Homeowners direct</td><td>Google search, Maps, Instagram, Nextdoor</td><td>Price, timeline, trust</td><td>Search ads, reviews, bookable visits, clear process page</td></tr>
</tbody></table></div>
<p>Trade work fills the schedule. Homeowner jobs usually carry better margins, because there’s no middleman markup and you sell edge profiles, backsplashes and sink upgrades directly. Most Houston shops we talk to want more homeowner work and are scared of the hassle. The hassle mostly comes from unclear expectations, which marketing can fix.</p>
<p>Keep the two separate in your tracking. A trade account is measured in jobs per month; a homeowner campaign in cost per signed job.</p>"""),

            ("What Houston homeowners are choosing: quartz, granite and quartzite", f"""<p>Engineered quartz is the default for most kitchens now. In {SRC['houzz']}, 39% of renovating homeowners chose engineered quartz countertops, against 19% for granite and 11% for quartzite.</p>
<!--fig:materials-->
<p>Your site should have a page for each material you fabricate, because homeowners search by material: “quartz countertops Katy,” “granite countertops near me,” “quartzite countertops Houston.” Each page should explain the material plainly, show finished local kitchens, and give a price range per square foot installed, even a wide one. If you aren’t comfortable publishing prices, at least publish your price levels (“Group A quartz from [your price] per square foot installed”).</p>
<p>The quartz-versus-quartzite confusion is your friend. Homeowners mix them up constantly, and a short, honest page explaining the difference (one engineered, one natural stone; different care, different price) ranks for a lot of searches and makes you look like the expert. Same for “is granite out of style,” which Houston homeowners ask every year, and which you can answer with photos of the granite kitchens you installed last month.</p>
<p>Remnants deserve their own page. Vanities, laundry rooms, outdoor kitchen tops and bar tops from remnant slabs bring in smaller homeowner jobs that often turn into a kitchen later.</p>"""),

            ("Template to install: sell the timeline in Houston", f"""<p>Ask homeowners what worries them about countertops and you’ll hear the same thing: how long the kitchen is torn up. Sell your timeline, then keep it.</p>
<!--fig:timeline-->
<p>A process page should walk through selection, deposit, template, layout approval, fabrication and install, with the typical days between each step and what the homeowner needs to do (cabinets level and secured, sink and faucet on site, old tops removed or not). Shops that send layout drawings or digital slab layouts for approval before cutting should say so loudly. It’s the single best answer to “will my seams look bad?”</p>
<p>Then use it in follow-up. A text the day before template, a photo of their slab on the saw, a heads-up the morning of install. These cost nothing and get mentioned in reviews more than anything else.</p>
<p>Your timeline is also your trade pitch. Builders along the Grand Parkway and remodelers in Cypress and Tomball will switch fabricators for a reliable template-to-install window. If you can hold one, put it in writing on your trade page.</p>"""),

            ("Silica safety is a marketing question now", f"""<p>Engineered stone has been in the news for years, and homeowners and designers increasingly ask fabricators about it. Have a clear answer.</p>
<p>The facts. Federal OSHA covers private employers in Texas, since Texas isn’t a State Plan state, per {SRC['osha_tx']}. Under {SRC['osha']}, the permissible exposure limit for respirable crystalline silica is 50 micrograms per cubic meter averaged over eight hours, the action level is 25, and employers need a written exposure control plan, exposure assessments, and medical exams every three years for workers exposed at or above the action level for 30 or more days a year.</p>
<p>In 2026, OSHA and NIOSH updated a hazard alert for countertop manufacturing, finishing and installation. Per {SRC['aiha']}, it names engineered stone and quartzite among the highest-silica materials, notes granite can be up to 50% silica, points to powered hand tools as the biggest exposure source, and recommends wet methods, local exhaust ventilation and doing as much work as possible in the shop.</p>
<!--fig:silica-->
<p>The news side: {SRC['mmwr']} found that at least 7 of 19 confirmed silicosis cases reported in California were tied to engineered stone countertop fabrication, with a median age of 44 for those workers. In August 2024 a Los Angeles County jury awarded $52.4 million to a 34-year-old fabrication worker with silicosis, according to {SRC['verdict']}. Australia banned engineered stone benchtops, panels and slabs from July 1, 2024, per {SRC['aus']}.</p>
<p>What to do with that in your marketing:</p>
<ul>
<li>Publish a short safety page about how your shop works: wet cutting, dust collection, in-shop fabrication, training. Only claim what you can back up with your written plan.</li>
<li>If you carry low-silica or alternative surfaces, give them their own page with accurate product claims from the manufacturer.</li>
<li>Don’t scare homeowners about the countertops already in their kitchens or take shots at competitors. The exposure issue is about cutting and grinding.</li>
<li>Give your sales team two calm sentences for when a designer asks.</li>
</ul>
<p>Shops that handle this openly look like professionals. Shops that dodge it look like they have something to hide.</p>"""),

            ("Trade accounts: winning builders, remodelers and designers", f"""<p>Trade business comes from relationships, and relationships come from showing up with something useful.</p>
<ol>
<li><b>A trade page and price sheet.</b> Material groups, edge profiles, cutout fees, typical lead times, and who to call. Refresh it quarterly.</li>
<li><b>Slab holds that work.</b> Designers and remodelers want to tag a slab for a client and know it’ll be there next week. Make holds easy and confirm them in writing.</li>
<li><b>A target list.</b> Remodelers in The Woodlands, Kingwood and Memorial, custom builders in Magnolia and Montgomery, kitchen designers in Houston showrooms. Twenty-five names, one visit or call each per month.</li>
<li><b>Credit on social.</b> Tag the designer and builder (with their permission) on every install post. That’s free marketing for them, which they notice.</li>
<li><b>Easy client handoff.</b> When a remodeler sends a homeowner to pick a slab, treat that homeowner like gold and report back to the remodeler.</li>
</ol>
<p>Our posts on {L('/blog/interior-designer-marketing-the-woodlands-houston/', 'how interior designers market themselves')} and {L('/blog/home-builder-marketing-houston-montgomery-county/', 'how builders market new homes')} show what those partners are dealing with. Pitch to their problems.</p>"""),

            ("Google Ads for countertop fabricators in Houston", f"""<p>Homeowner search volume is real, and the intent is strong. Someone typing “quartz countertops installed near me” has a kitchen in mind.</p>
<p>Structure we’d start with:</p>
<ul>
<li>One ad group per material (quartz, granite, quartzite, marble, solid surface if you do it), each to its material page.</li>
<li>A “countertop replacement” group for people keeping their cabinets, which is a big share of Houston kitchens built in the 1990s and 2000s.</li>
<li>A remnants and vanity group for smaller jobs.</li>
<li>A slab yard group: “granite slab yard Houston,” “quartz showroom near me.” These people want to visit, so the conversion is a booked visit.</li>
</ul>
<!--fig:negatives-->
<p>{SRC['lsa']} also includes a Countertop services category. Test it if you have strong reviews. Pay-per-lead pricing can suit fabricators, since one booked kitchen pays for a lot of leads.</p>
<p>Write ads that answer the timeline worry. “Template to install in [your days] days. Visit our slab yard in Houston, book a time online.” Add the starting price per square foot if you can. Price in the ad cuts clicks from people who were never going to buy, which saves money.</p>
<p>Budget honestly: a single-location fabricator testing homeowner search might start around $1,500 to $3,000 a month (an illustrative range, not a benchmark), then scale on cost per signed job. Our {L('/services/search-marketing/', 'Google Ads team')} sets these up, and the {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} help with expectations.</p>"""),

            ("Instagram install videos and the slab yard as content", f"""<p>Countertops are made for short video. A 20-ton slab moving on a forklift is more interesting than almost anything a dentist can post.</p>
<p>Content we’d film every week, on a phone:</p>
<ul>
<li>The slab reveal: a homeowner or designer seeing their slab for the first time.</li>
<li>The layout: seam placement and vein matching on a digital or taped layout.</li>
<li>Waterjet or saw cuts, sink cutouts and edge profiling (with your dust controls visible, which quietly answers the safety question).</li>
<li>The install: tops going in, the final wipe, the faucet hole drilled.</li>
<li>The finished kitchen with the neighborhood in the caption: “Calacatta-look quartz, Creekside Park.”</li>
</ul>
<!--fig:instagram-->
<p>Organic reach builds the trade audience. Paid reach gets homeowners. On Meta, run your best install videos to people within 20 to 30 miles who’ve shown home-improvement interest, then retarget video viewers and site visitors with a slab-yard visit offer. Our {L('/services/paid-social-advertising/', 'paid social team')} runs these if you’d rather not.</p>"""),

            ("Showroom and slab yard visits in The Woodlands and Houston", f"""<p>The slab yard visit is where homeowner jobs are won, so make it easy to book.</p>
<p>Put a booking link on every material page and in your Google Business Profile. Offer Saturday mornings, when couples can come together. Tell people what to bring: cabinet drawings, a photo of the kitchen, the cabinet color and floor sample. Send a confirmation text with a map pin, because many Houston slab yards sit in industrial parks with confusing entrances.</p>
<p>On the profile itself, upload photos of the yard, the showroom, and the entrance from the street. Answer the common questions in your own posts and website FAQ: do you sell to homeowners directly, do you have remnants, do you remove old tops, do you install backsplashes.</p>
<p>Count visits as a conversion and track which ads and pages produced them. A visit that turns into a signed kitchen is the number your budget should follow.</p>"""),

            ("Reviews from homeowners and trade partners", f"""<p>Ask homeowners the day after install, by text, with a direct link. The installer can mention it on the way out. Ask trade partners too, once a year, since a remodeler’s review carries weight with other remodelers.</p>
<p>The rules, from {SRC['gpol']}: no incentives, no asking only happy customers, no discouraging negative reviews. Same link to everyone.</p>
<p>Reply with specifics: the material, the edge, the neighborhood if the customer named it. When a review complains about a seam or a chip, answer calmly and offer a service visit. Read our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} for templates.</p>"""),

            ("What to track, and a first 90 days", f"""<p>Here’s an illustrative scorecard for a fabricator adding homeowner marketing to a trade-heavy business. The numbers are examples, not benchmarks.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Where it comes from</th><th>Example month</th></tr></thead>
<tbody>
<tr><td>Homeowner leads (calls, forms)</td><td>Call tracking, Google Ads, CRM</td><td>60</td></tr>
<tr><td>Slab yard visits booked</td><td>Scheduler</td><td>24</td></tr>
<tr><td>Visits that showed</td><td>Front desk log</td><td>19</td></tr>
<tr><td>Homeowner jobs signed</td><td>CRM</td><td>9</td></tr>
<tr><td>Active trade accounts</td><td>Job log</td><td>14</td></tr>
<tr><td>Trade jobs per account</td><td>Job log</td><td>3.1</td></tr>
</tbody></table></div>
<!--fig:budget-->
<p>A first 90 days: fix the Business Profile and build material, process and safety pages in month one. Launch search by material and start weekly Instagram install videos in month two. In month three, add Local Services Ads and Meta retargeting, and start the trade target list. Send signed jobs back to Google Ads so bidding learns from real buyers.</p>
<p>Mistakes we see: a homepage with a slab photo and no prices, process pages that skip the timeline, Instagram feeds with no locations or credits, and homeowner leads that wait two days for a callback because the office is busy with builders.</p>
<p>If you want a senior strategist to build a plan around your shop’s capacity and trade mix, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do countertop fabricators get more customers in Houston?",
             "Run two pipelines. For trade work, build a trade page and price sheet, make slab holds easy, keep a target list of remodelers, builders and designers, and keep your template-to-install promises. For homeowners, run Google search ads by material that lead to a bookable slab yard visit, post install videos on Instagram, and collect reviews after every install. Track trade jobs per account and homeowner cost per signed job."),
            ("What countertop material is most popular right now?",
             "Engineered quartz. In the 2025 U.S. Houzz Kitchen Trends Study, 39% of renovating homeowners chose engineered quartz, 19% chose granite and 11% chose quartzite. In Houston, granite still shows up in plenty of remodels and outdoor kitchens. A fabricator should have a separate web page for each material it cuts, with local photos and an installed price range."),
            ("What is the OSHA silica rule for countertop shops in Texas?",
             "Texas private employers fall under federal OSHA. The general industry silica standard sets a permissible exposure limit of 50 micrograms per cubic meter over eight hours and an action level of 25. It requires a written exposure control plan, exposure assessments, dust controls, training and medical exams for workers exposed at or above the action level for 30 or more days a year."),
            ("Should a fabricator mention silica safety in its marketing?",
             "Yes, calmly. Homeowners and designers increasingly ask about engineered stone after news coverage of silicosis among fabrication workers. A short page describing your wet cutting, dust collection and training, backed by your written plan, answers the question before it’s asked. Avoid scaring homeowners about installed countertops, avoid health claims you can’t support, and don’t attack competitors."),
            ("Are Google Local Services Ads available for countertop companies?",
             "Yes. Google’s Local Services Ads list includes a Countertop services category. You pay per lead rather than per click, and ranking leans on reviews and how quickly you respond. For a fabricator with a strong Google rating, it’s worth testing alongside a regular search campaign. Judge both by booked slab yard visits and signed jobs, not by raw lead counts."),
        ],
        "figures": {
            "materials": {
                "type": "columns",
                "title": "Countertop materials homeowners chose",
                "sub": "Share of renovating homeowners, 2025 U.S. Houzz Kitchen Trends Study",
                "labels": ["Engineered quartz", "Granite", "Quartzite"],
                "values": [39, 19, 11],
                "highlight": [0],
                "y_label": "Percent",
                "note": "Source: Houzz",
                "alt": "Column chart of quartz, granite and quartzite countertop choices for countertop fabricator marketing in Houston",
                "caption": f"From {SRC['houzz']}. Build a page for each material you cut.",
            },
            "timeline": {
                "type": "steps",
                "title": "Template to install, the way homeowners should see it",
                "sub": "Publish your real days between steps",
                "steps": [["Select and deposit", "Pick the slab at the yard; tag it with a hold."], ["Template", "Cabinets set and level, sink on site."], ["Layout approval", "Seams and veining approved before cutting."], ["Fabrication", "A photo of their slab on the saw."], ["Install", "Tops set, cutouts finished, final wipe."]],
                "alt": "Steps from slab selection to countertop installation for countertop fabricator marketing in Houston and The Woodlands",
                "caption": "A timeline you keep is your best homeowner ad and your best trade pitch.",
            },
            "silica": {
                "type": "stats",
                "title": "Silica numbers every fabricator should know",
                "stats": [["50 µg", "OSHA limit per cubic meter, 8-hour average"], ["25 µg", "action level that triggers assessments"], ["$52.4M", "2024 Los Angeles silicosis verdict"], ["2024", "Australia’s engineered stone ban took effect"]],
                "note": "Sources: OSHA, Public Health Watch, Safe Work Australia",
                "alt": "Stats on OSHA silica limits and engineered stone news relevant to countertop fabricators in Houston",
                "caption": f"From {SRC['osha']}, {SRC['verdict']} and {SRC['aus']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for countertop ads",
                "sub": "Start here and add from your search terms report",
                "items": ["DIY: diy, how to cut, epoxy countertop kit", "Paint and refinishing kits, unless you refinish", "Laminate, if you don’t sell it", "Jobs: fabricator jobs, installer hiring, salary", "Wholesale: slab wholesale, distributor", "Cleaning and sealing products", "Countertop decor and organizers", "Big-box store names"],
                "alt": "Checklist of negative keywords for countertop fabricator Google Ads in Houston",
                "caption": "Countertop searches mix buyers with DIY shoppers. Keep the budget on buyers.",
            },
            "instagram": {
                "type": "compare",
                "title": "Instagram posts that book slab yard visits",
                "left": {"title": "Gets scrolled past", "items": ["Stock slab photos", "No location in the caption", "No credit to designer or builder", "Finished kitchen only", "Posting when someone remembers"]},
                "right": {"title": "Gets saved and shared", "items": ["Phone video of a real install", "Neighborhood and material named", "Designer and builder tagged", "Reveal, layout, cut, install, finish", "One video a week, every week"]},
                "alt": "Comparison of Instagram content for countertop fabricator marketing in Houston and The Woodlands",
                "caption": "Show your dust controls in the cutting clips. It answers the safety question quietly.",
            },
            "budget": {
                "type": "bars",
                "title": "Example monthly homeowner marketing mix",
                "sub": "Single-location fabricator adding homeowner work",
                "items": [["Google Search", 2200, "$2,200"], ["Local Services Ads", 800, "$800"], ["Meta video and retargeting", 900, "$900"], ["Content and video time", 500, "$500"], ["Review and text software", 150, "$150"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of an example monthly marketing budget for a countertop fabricator in Houston",
                "caption": "Trade outreach isn’t on the chart because it costs time, not ad spend.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: boats and marinas
    {
        "slug": "boat-dealer-marina-marketing-lake-conroe",
        "title": "Boat Dealer and Marina Marketing on Lake Conroe: Inventory, Slips, Service and Show Season",
        "seo_title": "Boat Dealer & Marina Marketing on Lake Conroe",
        "desc": "Boat dealer and marina marketing on Lake Conroe: boat show season, inventory ads on Google and Meta, financing ad rules, slips, service and TPWD dealer rules.",
        "category": "Strategy",
        "icons": ["Facebook", "Google Ads", "Google Business Profile"],
        "art": "b6",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for boat dealer and marina marketing on Lake Conroe near The Woodlands and Conroe",
        "related": ["car-dealership-marketing-houston", "reaching-customers-conroe-montgomery", "seasonal-marketing-greater-houston"],
        "sections": [
            (None, f"""<p>The first warm Saturday in March at a marina on Lake Conroe. The fuel dock line is six boats deep. A family from Spring is at the sales desk asking about the pontoon they saw on Facebook, which sold two weeks ago. The service department has 40 boats that haven’t been run since October and every owner wants theirs by Memorial Day. And somebody’s on the phone asking if you have a covered slip.</p>
<p>That one Saturday holds the whole business: inventory, financing, service, slips, and a season that arrives all at once.</p>
<p>Boat dealer and marina marketing on Lake Conroe works when you build demand in January and February, around the Houston boat show, and keep inventory listings accurate on the channels that accept boats. Then the service department brings owners back every year. You also need to know the rules: Google won’t run boats in vehicle ads, Meta treats financing as a special category, and TPWD and Texas law limit how far a dealer can advertise a brand’s prices.</p>"""),

            ("Lake Conroe’s market: who’s buying and when", f"""<p>Lake Conroe covers about 19,640 acres at its conservation pool elevation of 201 feet, across Montgomery and Walker counties, and was completed in January 1973, per {SRC['twdb']}. {SRC['sjra']}, which operates the dam, puts the shoreline at about 150 miles. That’s a lot of lake homes, and a short drive from The Woodlands, Conroe, Montgomery and Willis.</p>
<p>Your buyers fall into a few groups. Lakefront owners in communities like Walden, April Sound and Bentwater. Weekenders driving up I-45 from Spring, Cypress and north Houston. Fishing buyers who also run the Gulf from Galveston. And first-time buyers who just moved to a Montgomery County master-planned community and noticed everyone has a boat.</p>
<p>Nationally, pontoons are the biggest segment. {SRC['nmma']} counted 156,754 new powerboats sold in 2025, with pontoons making up 33.6% of units. On a lake full of families and lake-house owners, that tracks with what you’d see from the 105 bridge on a summer Sunday.</p>
<!--fig:season-->
<p>Seasonality is extreme. Inquiries climb from January (show season) through May, peak in spring, hold through summer, then drop hard after Labor Day. Service runs on its own curve: spring prep, summer breakdowns, fall storage. Your budget should follow both curves rather than sitting flat at a monthly retainer.</p>"""),

            ("Boat show season: plan January through March backward", f"""<p>The Houston boat show is the start of the selling year. For 2027 it’s combined with the Houston Auto Show as the AutoBoative show, January 27 to 31 at NRG Park, with one ticket for both, per {SRC['hbs']} and {SRC['has']}.</p>
<p>Whether you exhibit or not, the show moves buyers. People walk the floor, look at 30 boats, and go home to search the brands they liked. If you’re the local dealer for those brands, January searches are yours to lose.</p>
<!--fig:show-->
<p>What we’d do:</p>
<ul>
<li><b>December:</b> build a show page with the models you’ll have, show-only offers with a real end date, and a form to book a time at the booth or a lake demo after.</li>
<li><b>Two weeks out:</b> email and text past customers and leads with the dates and what you’re bringing. Run Meta video of the show boats to people within driving distance of NRG Park and the lake.</li>
<li><b>Show week:</b> capture every booth conversation in the CRM the same day, with model interest and timeline. Paper forms in a box get entered in March, which is too late.</li>
<li><b>The two weeks after:</b> call every booth lead, book lake demos for the first nice weekend, and retarget show-page visitors.</li>
</ul>
<p>Our {L('/blog/seasonal-marketing-greater-houston/', 'seasonal marketing guide for Greater Houston')} has more on timing spend around local events.</p>"""),

            ("Inventory ads: what Google and Meta will and won’t take", f"""<p>Car dealers have it easy here. Boat dealers have to know which channels accept boat inventory.</p>
<p><b>Google vehicle ads don’t accept boats.</b> {SRC['gva']} allow passenger and non-commercial vehicles, including RVs, ATVs, UTVs, campers and non-motorized trailers, and list boats explicitly among the excluded types, with motorcycles and planes. {SRC['gva26']} added ATVs, UTVs and travel trailers in the U.S. Boats stayed out. If you also sell ATVs or UTVs, those can now go in a vehicle feed; boats go into Search campaigns instead.</p>
<p><b>Meta accepts boats in vehicle catalogs.</b> {SRC['metacat']} lists BOAT as a valid vehicle type. That means a catalog of your inventory can drive dynamic ads that show the exact boat a person looked at on your site. It’s the closest thing to a car dealer’s inventory ads, and it’s underused by boat dealers.</p>
<p><b>Facebook Marketplace changed.</b> In January 2023, Meta removed vehicle listings posted from business Pages on Marketplace, per {SRC['mkt']}. The coverage talked about vehicles and didn’t spell out boats, so test what your Page can post, and read Meta’s commerce policies before you ask salespeople to list dealer inventory on personal profiles.</p>
<p><b>The boat portals.</b> {SRC['bg']} owns Boat Trader, boats.com and YachtWorld. For used inventory especially, that’s where shoppers compare. Judge them on cost per sold boat, not leads.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Takes boat inventory?</th><th>Best use</th></tr></thead>
<tbody>
<tr><td>Google vehicle ads</td><td>No (boats excluded)</td><td>ATVs, UTVs, trailers if you sell them</td></tr>
<tr><td>Google Search</td><td>Yes, as text ads to model pages</td><td>Brand, model and “for sale near me” searches</td></tr>
<tr><td>Meta catalog ads</td><td>Yes (vehicle type BOAT)</td><td>Dynamic retargeting of boats people viewed</td></tr>
<tr><td>Facebook Marketplace</td><td>Business Page vehicle listings removed in 2023</td><td>Test carefully; follow commerce policies</td></tr>
<tr><td>Boat Trader, boats.com, YachtWorld</td><td>Yes</td><td>Used and brokerage inventory, comparison shoppers</td></tr>
</tbody></table></div>
<p>Whatever the channel, the website is the source of truth. Every boat gets its own page with price (or “call for price” if your agreement requires it), photos, engine hours for used units, and a “schedule a lake demo” button. Mark sold boats sold the same day. Nothing burns a buyer faster than driving up from Katy for a boat that’s gone.</p>"""),

            ("Google Search for boat dealers around Lake Conroe", f"""<p>Search is the closer. Buyers search brands and models after the show, after a test ride with a friend, or after a Saturday staring at other people’s boats.</p>
<p>Campaigns we’d build:</p>
<ul>
<li><b>Brand and model:</b> each brand you carry plus “for sale,” “dealer,” “price,” and the town names (Conroe, Montgomery, The Woodlands, Houston).</li>
<li><b>Category:</b> “pontoon boats for sale,” “wake boats Houston,” “bay boats for sale near me,” “used boats Conroe.”</li>
<li><b>Service:</b> “boat repair near me,” “outboard service Lake Conroe,” “boat mechanic Montgomery TX.” Service search is steady and cheap compared with sales.</li>
<li><b>Marina:</b> “boat slip rental Lake Conroe,” “dry stack storage Lake Conroe,” “boat storage Conroe TX.”</li>
</ul>
<!--fig:negatives-->
<p>Now the rule many dealers miss. Texas Occupations Code section 2352.0522, summarized in {SRC['tpwd_dealer']}, says a dealer may not advertise or promote a manufacturer’s boats outside its assigned territory, online included, unless the ad shows no price or shows only the manufacturer’s suggested retail price. A dealer can still sell to an out-of-territory buyer who comes in on their own. In practice, match the location targeting of any priced ad to your dealer agreement’s territory, and keep priced ads off broad national targeting. Ask your manufacturer rep what your territory actually is; we often find the dealer isn’t sure.</p>
<p>Our {L('/blog/car-dealership-marketing-houston/', 'car dealership marketing post')} covers inventory search structure in more depth, and the {L('/services/search-marketing/', 'search marketing team')} handles accounts like this.</p>"""),

            ("Financing ads under Meta’s Financial Products and Services category", f"""<p>Most boats are financed, so monthly payments sell. They also bring rules.</p>
<p>On Meta, ads promoting credit offers such as loans and long-term financing run under the Financial Products and Services special ad category. Age and gender targeting are locked, the location must include at least a 15-mile radius, ZIP targeting and lookalike audiences go away, and instant forms can’t ask for things like age or location, per {SRC['loomer']}. If the ad is about a payment, choose the category. Try to work around it and you risk rejected ads or an account restriction.</p>
<p>The copy has rules too. Under {SRC['regz']}, stating a payment amount, a number of payments or term, a down payment or a finance charge means you must also state the down payment, the repayment terms and the APR. “$389 a month” alone doesn’t pass. Your lender or manufacturer finance program usually supplies compliant language.</p>
<!--fig:financing-->
<p>The radius rule matters less on Lake Conroe than you’d think, since a 15-mile circle around the lake already covers The Woodlands, Conroe, Montgomery and Willis. The bigger loss is detailed targeting. So the creative has to find the buyer: a video of a specific tritoon pulling a tube past the 105 bridge, the payment with full disclosure on the landing page, and a “book a lake demo” button.</p>"""),

            ("Slip rentals and dry stack: marketing a Lake Conroe marina", f"""<p>Marinas sell space, and space runs out. The marketing job changes with occupancy.</p>
<p>When slips are full, run a waitlist page with slip sizes, covered or uncovered, power, and an honest estimate of the wait. When you have openings, publish them with “from” monthly rates, photos from the water and the parking lot, and what’s included (fuel dock, pump-out, ship store, security). People comparing marinas want the rate, the walk from parking to the slip, and how the place looks at 6 p.m. on a Saturday.</p>
<p>Your Google Business Profile matters a lot here. Pick the marina category as primary, add boat storage and boat repair if you do them, keep hours accurate by season, and post photos often. Many people search “marina near me” while they’re on the water.</p>
<p>Lake level is a content topic your tenants care about. {SRC['lower']} describes the seasonal lowering program that ran through at least 2023, with spring releases to 200.5 feet and fall releases down to 200.0 feet, a foot below normal pool, at the City of Houston’s request. Whatever the current plan, a short page or post explaining lake level and what it means for your docks answers a question your office gets every year.</p>
<p>And plan for storms. Hurricane season runs June through November. Have a storm-prep page and a text template ready for tenants before the first named storm.</p>"""),

            ("The service department is the retention engine", f"""<p>A dealer might sell a customer one boat every five or six years. The service department can see them twice a year. That’s where loyalty, trade-ins and referrals come from.</p>
<ul>
<li><b>Spring prep reminders</b> in January and February, before the rush. Book appointments early with a schedule you can keep.</li>
<li><b>Mid-summer check-ins</b> for impellers, batteries and anything the Houston heat is cooking.</li>
<li><b>Fall storage and service</b> offers in September.</li>
<li><b>Registration renewal reminders.</b> {SRC['tpwd_title']} says owners can renew up to 90 days before expiration. A reminder from you is good service and a reason to book a visit.</li>
<li><b>New-owner orientation.</b> Texas requires boater education for operators born on or after September 1, 1993, running a vessel with a motor over 15 horsepower, per {SRC['tpwd_ed']}. Add a line to every delivery checklist and a page about it on your site. Parents buying a boat for teenagers search for this.</li>
</ul>
<p>Use text for service updates and email for marketing, with separate consent for marketing texts. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'SMS marketing post')} covers the Texas rules.</p>"""),

            ("TPWD dealer rules that touch your marketing", f"""<p>A few Texas rules are worth knowing because they show up in ads and on websites.</p>
<p>Per {SRC['tpwd_dealer']}, a dealer is anyone who buys, sells, consigns, displays for sale or exchanges at least five vessels, motorboats or outboard motors in a calendar year. The license costs $500 for two years, each place of business needs its own license, and the license has to be displayed at that location. If you’re running ads for a second location or a seasonal lot, check that it’s licensed first.</p>
<!--fig:tpwd-->
<p>Sales tax is part of the buyer’s real cost. TPWD collects 6.25% tax on boats and outboard motors, due within 45 working days of the sale, per {SRC['tpwd_title']}. Out-the-door pricing that explains tax, title and registration on the website saves an awkward conversation at the desk, and buyers from out of state appreciate it.</p>
<p>None of this is legal advice. Your manufacturer agreements and your attorney get the last word, especially on territory.</p>"""),

            ("Reviews from buyers, slip tenants and service customers", f"""<p>Three kinds of customers, three moments to ask. Buyers the week after delivery, once they’ve had the boat on the water. Service customers the day after pickup. Slip tenants once a year, and after you fix something they asked about.</p>
<p>The rules, from {SRC['gpol']}: no incentives, no asking only happy customers, no discouraging negatives. Same link to everyone.</p>
<p>Service reviews will be your most numerous and your most critical. Reply to every one with specifics and a name to call. Buyers read service reviews before they buy, because they know they’ll be back. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has request templates.</p>"""),

            ("What to track, and a season plan", f"""<p>Measure each department on its own numbers. A rough version, with example figures that are illustrative only:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Department</th><th>Metric</th><th>Example March</th></tr></thead>
<tbody>
<tr><td>Sales</td><td>Leads, lake demos booked, boats sold by source</td><td>140 leads, 26 demos, 9 sold</td></tr>
<tr><td>Service</td><td>Appointments booked, ticket average, return rate</td><td>180 appointments</td></tr>
<tr><td>Marina</td><td>Slip occupancy, waitlist size, inquiries</td><td>94% occupied, 22 on waitlist</td></tr>
<tr><td>Show</td><td>Booth leads entered same day, demos booked within 2 weeks</td><td>85 leads, 19 demos</td></tr>
</tbody></table></div>
<p>A season plan in one breath: December builds the show page and list, January runs the show and follow-up, February and March push lake demos and spring service, April and May are peak sales spend, summer shifts toward service and used inventory, September runs storage and year-end offers, and October through November is for reviews, website fixes and planning. Spend rises and falls with that curve.</p>
<p>Mistakes we see: sold boats still listed, financing ads with a payment and no APR, priced ads running outside the dealer territory, and booth leads entered weeks after the show. Our {L('/blog/reaching-customers-conroe-montgomery/', 'guide to reaching customers in Conroe and Montgomery County')} has more on local channels north of The Woodlands.</p>
<p>If you want a senior strategist to build a plan around your brands, slips and service bays, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do boat dealers on Lake Conroe get more buyers?",
             "Start before the season. Build a show page and contact list in December, follow up every Houston boat show lead within two weeks, and book lake demos for the first warm weekends. Keep every boat on its own website page with accurate pricing, run Google Search on your brands and models, use Meta catalog ads to retarget boats people viewed, and keep service customers coming back."),
            ("Can boat dealers use Google vehicle ads?",
             "No. Google’s vehicle ads policies allow passenger and non-commercial vehicles, including RVs, campers, ATVs, UTVs and non-motorized trailers, but list boats among the excluded vehicle types. Boat dealers should use Google Search campaigns that send model and brand searches to individual inventory pages. If you also sell ATVs, UTVs or trailers, those can go in a vehicle ads feed in the U.S."),
            ("Do boat financing ads on Facebook need a special ad category?",
             "Generally yes. Meta’s Financial Products and Services category covers ads promoting credit offers such as loans and long-term financing. It locks age and gender targeting, requires at least a 15-mile radius, removes ZIP code and lookalike targeting, and limits instant form questions. The copy also has to follow Regulation Z: a stated monthly payment requires the down payment, repayment terms and APR."),
            ("Do you need a license to sell boats in Texas?",
             "Yes, in most cases. Texas Parks and Wildlife requires a dealer license for anyone who buys, sells, consigns, displays for sale or exchanges at least five vessels, motorboats or outboard motors in a calendar year. The license costs $500 for two years, each place of business needs its own, and it must be displayed at that location. Some very small boats and motors are exempt."),
            ("When is the 2027 Houston Boat Show?",
             "The 2027 Houston boat show runs January 27 to 31, 2027, at NRG Park, combined with the Houston Auto Show as the AutoBoative show with one ticket for both, according to the show organizers. Lake Conroe dealers should have show pages, offers and booth lead capture ready in December, then follow up with lake demos in February and March."),
        ],
        "figures": {
            "season": {
                "type": "columns",
                "title": "When Lake Conroe boat buyers shop",
                "sub": "Relative sales inquiries by month for a typical lake dealer",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [62, 70, 88, 100, 92, 74, 60, 48, 34, 26, 22, 28],
                "highlight": [2, 3, 4],
                "y_label": "Relative",
                "note": "Illustrative example",
                "alt": "Column chart of seasonal boat buyer inquiries for boat dealer marketing on Lake Conroe near The Woodlands",
                "caption": "Shape varies by dealer and brand. Build your own from last year’s CRM data.",
            },
            "show": {
                "type": "steps",
                "title": "Working the Houston boat show",
                "sub": "January 27-31, 2027, NRG Park",
                "steps": [["December", "Show page, show-only offers with end dates, booking form."], ["Two weeks out", "Email and text past customers; Meta video of show boats."], ["Show week", "Every booth lead in the CRM the same day."], ["Weeks 1-2 after", "Call every lead; book lake demos."], ["February-March", "Retarget show visitors; push spring service."]],
                "alt": "Steps for Lake Conroe boat dealers to market around the 2027 Houston boat show at NRG Park",
                "caption": f"Show dates from {SRC['hbs']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for boat dealer ads",
                "sub": "Adjust for what you actually sell and rent",
                "items": ["Rental: rent, rental, charter (unless you rent)", "Jobs: boat mechanic jobs, marina jobs, hiring", "DIY: how to, manual, wiring diagram", "Parts only: part number, propeller sizes", "Free: free boat, donate a boat", "Tickets: boat show tickets, discount code", "Lake info: lake level, fishing report, weather", "Toys: model boat, rc boat, kayak (unless sold)"],
                "alt": "Checklist of negative keywords for boat dealer and marina Google Ads on Lake Conroe",
                "caption": "Lake searches pull in a lot of fishing reports and lake-level checks. Filter them.",
            },
            "financing": {
                "type": "compare",
                "title": "Boat financing ads that pass",
                "left": {"title": "Gets you in trouble", "items": ["“$389 a month” with nothing else", "Payment ad outside the special category", "Age or ZIP targeting on a loan offer", "Instant form asking for age", "Priced ad outside your territory"]},
                "right": {"title": "Holds up", "items": ["Payment, down payment, term and APR together", "Financial Products and Services category", "15-mile-plus radius around the lake", "Creative that finds the buyer", "Territory-matched location targeting"]},
                "alt": "Comparison of boat financing ad practices for dealers on Lake Conroe under Meta and Regulation Z rules",
                "caption": f"Based on {SRC['loomer']}, {SRC['regz']} and {SRC['tpwd_dealer']}.",
            },
            "tpwd": {
                "type": "stats",
                "title": "Texas boat rules in four numbers",
                "stats": [["5", "boats a year makes you a dealer"], ["$500", "two-year TPWD dealer license"], ["6.25%", "boat and motor sales tax"], ["15 hp", "boater ed threshold, born 9/1/93 or later"]],
                "note": "Sources: TPWD",
                "alt": "Stats on Texas Parks and Wildlife boat dealer, tax and boater education rules for Lake Conroe dealers",
                "caption": f"From {SRC['tpwd_dealer']}, {SRC['tpwd_title']} and {SRC['tpwd_ed']}.",
            },
        },
    },
]
