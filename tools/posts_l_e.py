"""Batch 12 (module e): commercial cleaning and janitorial company marketing in Houston.

Research: WordStream/LocaliQ 2026 Google Ads benchmarks (Business Services median CPC $5.87, CVR 4.85%, CPL $93.69;
Industrial & Commercial $5.87 CPC, $75.19 CPL; data April 1, 2025 to March 31, 2026); Google Local Services Ads
category list (no commercial cleaning or janitorial category; House cleaning services, Carpet cleaning services and
Window cleaning services are listed); Texas Comptroller publication 94-111 (janitorial and custodial services taxable,
including cleaning an office, warehouse, restaurant or any other building); Lee & Associates Q3 2026 Greater Houston
office report (237.9 million SF, 22.9% direct and 24.0% total vacancy, The Woodlands 9.1% direct vacancy, Class A
$36.47 vs Class B $23.32 asking rent); Lee & Associates Q3 2026 Houston industrial report (382.4 million SF, 5.2%
direct vacancy, about 5.9 million SF delivered in Q3, 21.4 million SF year to date); LinkedIn's budget best-practices
page ($10 minimum daily budget for any ad format); City of Houston Strategic Procurement supplier page (Beacon Bid
registration required to respond to solicitations); Texas Comptroller bid opportunities page (CMBL, $70 annual fee);
ISSA CIMS overview (certification for building service contractors, infection prevention criteria folded in from
GBAC STAR, Green Building variant aligned with LEED); SuretyBonds.com on janitorial service bonds (protects clients
from employee theft, from $125 a year for $10,000 for small companies); OSHA hospital housekeeping eTool on
bloodborne pathogens (exposure determination, written cleaning schedule); TDI employer FAQ (non-subscribers);
IFMA chapter map (Houston Chapter of IFMA). GBP category naming checked against GMB Everywhere's janitorial guide.
Competitor/PAA phrasing read for "commercial cleaning marketing", "how to get commercial cleaning contracts",
"janitorial marketing ideas", "commercial cleaning google ads", "how to get janitorial clients".
Left out: a Houston-specific CPC for "commercial cleaning services" (no public source; told readers to pull it from
Keyword Planner), BLS Houston metro janitor wage figures (couldn't load the metro table), any claim that Texas licenses
janitorial companies.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "wordstream": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream and LocaliQ’s 2026 Google Ads benchmarks"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "tax": A("https://comptroller.texas.gov/taxes/publications/94-111.php", "Texas Comptroller’s guide for cleaning and maintenance services"),
    "office": A("https://www.lee-associates.com/houston/2026/10/19/greater-houston-office-market-report-q3-2026/", "Lee & Associates’ Q3 2026 Houston office report"),
    "industrial": A("https://www.lee-associates.com/houston/?p=12567", "Lee & Associates’ Q3 2026 industrial report"),
    "linkedin": A("https://business.linkedin.com/advertise/ads/best-practices/maximize-your-budget", "LinkedIn’s own budget guide"),
    "coh": A("https://www.houstontx.gov/bizwithhou/SupplierPortal.html", "City of Houston’s supplier page"),
    "cmbl": A("https://comptroller.texas.gov/purchasing/vendor/bid-opportunities.php", "Texas Comptroller"),
    "cims": A("https://cims.issa.com/about-cims/", "ISSA’s CIMS certification"),
    "bond": A("https://www.suretybonds.com/commercial/janitorial-service-bonds", "SuretyBonds.com"),
    "osha": A("https://www.osha.gov/etools/hospitals/housekeeping/bloodborne-pathogens", "OSHA’s housekeeping guidance on bloodborne pathogens"),
    "tdi": A("https://agate.tdi.texas.gov/wc/employer/employerfaq.html", "Texas Department of Insurance"),
    "ifma": A("https://ifma.org/membership/networks/local-chapter-map/chapter-details/houston", "Houston Chapter of IFMA"),
}

L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    {
        "slug": "commercial-cleaning-janitorial-marketing-houston",
        "title": "Commercial Cleaning Marketing in Houston: SEO, Google Ads & LinkedIn for Janitorial Companies",
        "seo_title": "Commercial Cleaning Marketing Houston: SEO, Ads & LinkedIn",
        "desc": "How Houston janitorial companies win contracts: building-type SEO, Google Ads costs, LinkedIn, RFPs, bonding and insurance proof, and booked walkthroughs.",
        "category": "Search marketing",
        "icons": ["Google Ads", "LinkedIn", "Google Business Profile"],
        "art": "b4",
        "hero": "industry",
        "hero_alt": "Illustration of commercial buildings for commercial cleaning and janitorial company marketing in Houston and The Woodlands",
        "related": ["b2b-marketing-houston-energy-industrial", "property-management-company-marketing-houston", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>The closest category in {SRC['wordstream']} is Business Services, where search ads ran a median <b>$5.87 per click</b> and <b>$93.69 per lead</b>, and Houston makes that harder: a 237.9 million square foot office market with 24.0% total vacancy, per {SRC['office']}, means owners are watching operating costs, and janitorial is an easy contract to rebid.</p>
<p>Thursday, 4:50 p.m. A facility manager at a three-story medical office building in Sugar Land is staring at a photo a tenant sent her: an overflowing trash can in a suite that was supposedly cleaned last night. It’s the third complaint this month. She opens Google and types “commercial cleaning company Sugar Land,” then texts a property manager friend in Westchase asking who they use.</p>
<p>You want to be the answer to both. That means showing up when a frustrated buyer searches, proving you’re safe to hand a building key to, and turning interest into a booked walkthrough. This guide is for janitorial companies; residential maid services should read our {L('/blog/house-cleaning-business-marketing-houston/', 'house cleaning marketing guide')} instead.</p>"""),

            ("Know who actually signs the contract", """<p>Commercial cleaning is bought by someone whose job is keeping a building running, and they almost never search until the current vendor has failed them.</p>
<ul>
<li><b>Property managers</b> at multi-tenant office and retail buildings. They answer to an owner and often rebid every two or three years.</li>
<li><b>Facility managers</b> at corporate campuses, plants and energy company offices in the Energy Corridor and The Woodlands. They want documented scopes and safety records.</li>
<li><b>Practice administrators</b> at clinics and surgery centers. Infection control and HIPAA-aware crews matter more to them than price.</li>
<li><b>Office managers</b> at 5,000 to 20,000 square foot offices. Smaller contracts, faster decisions, usually found on Google.</li>
</ul>
<p>The trigger is usually a complaint, so your ads and pages should speak to the pain of a bad vendor (missed nights, turnover, no supervisor checking work) more than to “sparkling clean.”</p>"""),

            ("Rank for service and building-type searches", f"""<p>Build one page for each building type and each core service, because buyers search the type of building they manage, and a single “Services” page won’t rank for any of them.</p>
<ul>
<li><b>Building-type pages:</b> office cleaning, medical office cleaning, industrial and warehouse cleaning, church and school cleaning, retail and restaurant, property management. Each names the risks for that building, your crew training and a short case story.</li>
<li><b>Service pages:</b> nightly janitorial, day porter, floor stripping and waxing, carpet extraction, window cleaning, post-construction cleanup, disinfection.</li>
<li><b>Area pages that earn their place:</b> The Woodlands, Energy Corridor, Westchase, Greenway Plaza, Texas Medical Center area, Sugar Land, Katy, Pasadena and Baytown for industrial. Mention business parks you already service. A page that only swaps the city name won’t rank, as our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} explains.</li>
<li><b>Google Business Profile:</b> pick “Janitorial service” as the primary category (or the commercial cleaning option if it shows up for you), list each service, and set it up as a service-area business if clients never visit your office.</li>
<li><b>Proof on every page:</b> insurance, bonding, background checks and photos of real crews.</li>
</ul>
<p>The Woodlands deserves its own page. Its office submarket had just 9.1% direct vacancy in Q3 2026 against 22.9% citywide, per {SRC['office']}, so those buildings are full and funded. On the industrial side, Houston had 382.4 million square feet of distribution space with about 5.9 million delivered in Q3 alone, per {SRC['industrial']}. New warehouses along the Grand Parkway and near Port Houston all need a cleaning vendor. Our {L('/blog/seo-cost-houston-the-woodlands/', 'SEO pricing guide')} covers what a build-out like this costs.</p>"""),

            ("Skip Local Services Ads for commercial work", f"""<p>Google doesn’t offer a commercial cleaning or janitorial category in Local Services Ads, so that channel isn’t available for nightly office contracts.</p>
<p>{SRC['lsa']} includes House cleaning services, Carpet cleaning services and Window cleaning services, but nothing for janitorial or office cleaning. Signing up under house cleaning would put you in front of homeowners wanting a maid. A separate carpet or window division can test those categories; janitorial budget belongs in regular Google Ads. The trade-offs between the two ad types are in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</p>"""),

            ("Run Google Ads with tight controls", f"""<p>Google Ads works for commercial cleaning when you bid only on buyer phrases, block the job seekers, and send every click to a page that books a walkthrough.</p>
<ul>
<li><b>Keywords that signal a buyer:</b> “commercial cleaning services,” “janitorial services Houston,” “office cleaning company,” “medical office cleaning,” “warehouse cleaning services,” “day porter services,” “floor stripping and waxing.” Use phrase and exact match to start.</li>
<li><b>Negatives on day one:</b> jobs, hiring, careers, “cleaning jobs near me,” salary, “part time,” franchise, “how to start,” supplies, equipment, rental, residential, house, maid, “move out,” apartment, “carpet cleaner rental.” Janitorial searches pull a lot of job seekers.</li>
<li><b>Schedule and location:</b> run ads weekdays during business hours and only in areas your crews can staff.</li>
<li><b>One campaign per building type</b> so medical office searches land on the medical page, with ad copy that names the pain.</li>
<li><b>Know your real click cost:</b> Business Services medians are $5.87 per click and a 4.85% conversion rate in {SRC['wordstream']}. Big-metro clicks can price higher, so check Keyword Planner for your ZIP codes.</li>
</ul>
<p>Sample headline set: “Crews That Show Up Nightly” / “Bonded, Insured, Screened” / “Book a Walkthrough This Week.” Descriptions should name your inspection schedule and complaint response time. Our {L('/services/search-marketing/', 'search marketing team')} builds these accounts.</p>
<!--fig:benchmarks-->"""),

            ("Use LinkedIn to reach facility and property managers", f"""<p>LinkedIn is the one platform where you can target people by job title, so it’s the right place to stay in front of facility and property managers between bids.</p>
<ul>
<li><b>Budget floor:</b> the minimum daily budget is $10 for any ad format, per {SRC['linkedin']}. Clicks cost more than on Google, so use it for awareness and retargeting.</li>
<li><b>Targeting:</b> job titles like facilities manager, property manager, building engineer, practice administrator and office manager, in Houston-area locations.</li>
<li><b>Account lists:</b> upload a list of the management companies and building owners you want, and show ads only to people who work there.</li>
<li><b>The owner’s profile:</b> post once a week about real work. Buyers check the owner before the meeting.</li>
<li><b>Offline rooms:</b> the {SRC['ifma']} and BOMA Houston events put you in a room with exactly these buyers. Follow up on LinkedIn the same week.</li>
</ul>
<p>Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston energy and industrial companies')} covers LinkedIn targeting for plant and corporate buyers in more depth.</p>"""),

            ("Put trust signals where buyers check them", f"""<p>A commercial buyer is handing your crew the keys and alarm codes to their building, so bonding, insurance and background checks should be on your website before they ask.</p>
<ul>
<li><b>Janitorial bond:</b> it protects your clients, not you, if an employee steals. {SRC['bond']} lists coverage starting around $125 a year for $10,000 for companies with five or fewer employees, and calls it optional but often requested before a client signs.</li>
<li><b>Insurance:</b> general liability, plus a certificate naming the building owner and manager as additional insureds when the contract asks for it.</li>
<li><b>Workers’ comp:</b> Texas lets private employers opt out and become non-subscribers, per the {SRC['tdi']}. Some contracts require coverage anyway, so say whether you carry it.</li>
<li><b>Medical offices:</b> show crews are trained on bloodborne pathogen exposure and follow a written cleaning schedule, which {SRC['osha']} recommends for each area.</li>
<li><b>Certification:</b> {SRC['cims']} is built for building service contractors and now includes infection prevention criteria. Large buyers recognize it.</li>
</ul>
<!--fig:trust-->"""),

            ("Get on public bid lists and answer RFPs well", f"""<p>Public and institutional contracts only reach vendors who are registered, so sign up for the bid portals before you need them.</p>
<ul>
<li><b>City of Houston:</b> suppliers must register on the Beacon Bid portal to respond to City solicitations, per the {SRC['coh']}.</li>
<li><b>State of Texas:</b> the Centralized Master Bidders List is the database state agencies and public universities use to send bids, with a $70 annual registration fee, per the {SRC['cmbl']}.</li>
<li><b>Private RFPs:</b> keep a ready packet with your scope template, staffing plan, supervisor inspection checklist, insurance certificates, references from similar buildings and a transition plan for the first 30 days.</li>
</ul>
<p>Price bids with Texas sales tax in mind. The {SRC['tax']} says janitorial and custodial services are taxable, including cleaning “a home, office, warehouse, garage, restaurant, or any other building.” State whether your number includes tax. This isn’t legal or tax advice; confirm specifics with your CPA.</p>"""),

            ("Do the lifetime value math before you set a budget", """<p>A commercial cleaning contract is worth tens of thousands of dollars over its life, which is why paying a few hundred dollars for a qualified walkthrough is reasonable.</p>
<p>Take an illustrative 20,000 square foot office cleaned five nights a week at $3,500 a month. That’s $42,000 a year. If the client stays an average of three years, the contract brings in $126,000. At a 15% to 20% net margin after labor and supplies, that’s $18,900 to $25,200 in profit from one signature.</p>
<!--fig:ltv-->
<p>Now work backward. If one in four walkthroughs becomes a signed contract, and you’re willing to spend 10% of the contract’s three-year profit to win it, your ceiling is roughly $1,890 to $2,520 per contract, or about $470 to $630 per walkthrough. Plug in your own numbers. Retention changes the answer more than price, so supervisor inspections are a marketing expense too.</p>"""),

            ("Make the walkthrough the conversion", f"""<p>The goal of every ad, page and post is a booked site walkthrough, because nobody signs a janitorial contract from a web form.</p>
<ul>
<li><b>Book it online:</b> a short form (building type, square footage, nights per week) and a calendar.</li>
<li><b>Call back in five minutes:</b> a facility manager with a tenant complaint calls several companies, and the first to answer usually wins. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers follow-up.</li>
<li><b>Track it properly:</b> count calls, forms and booked walkthroughs as separate conversions, then import signed contracts back into Google Ads so bidding learns which clicks pay. The setup is in our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')}.</li>
<li><b>Send a proposal within 48 hours</b> of the walkthrough.</li>
</ul>
<!--fig:funnel-->"""),

            ("What to budget in Houston", """<p>Most small and mid-size janitorial companies in Houston should plan on roughly $3,000 to $9,000 a month across channels to see steady walkthroughs. These are planning ranges from our experience, not quotes.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Typical monthly range</th><th>What it’s for</th></tr></thead>
<tbody>
<tr><td>Google Ads (media)</td><td>$1,500-$5,000</td><td>Buyers searching right after a vendor failure</td></tr>
<tr><td>SEO and building-type pages</td><td>$1,000-$3,000</td><td>Lower-cost leads that compound over 6-12 months</td></tr>
<tr><td>LinkedIn ads</td><td>$300-$1,500</td><td>Staying known to facility and property managers</td></tr>
<tr><td>Networking (IFMA, BOMA)</td><td>Dues and event fees</td><td>Relationships that turn into invited bids</td></tr>
</tbody></table></div>
<p>Start with Google Ads and the core pages, then add LinkedIn.</p>"""),

            ("Your first 90 days", """<ul>
<li><b>Days 1-30:</b> build or rewrite pages for your top three building types, fix the Google Business Profile, set up call tracking and walkthrough booking, and register on Beacon Bid and the CMBL.</li>
<li><b>Days 31-60:</b> launch Google Ads on buyer keywords with the full negative list, add your COI, bond and certification details to every page, and ask every client for a Google review.</li>
<li><b>Days 61-90:</b> start a small LinkedIn campaign aimed at a target account list, publish two case stories, and review which keywords produced walkthroughs versus calls from job seekers.</li>
</ul>"""),

            ("Mistakes we see", """<ul>
<li><b>Paying for job seeker clicks.</b> Without negatives, “cleaning jobs” searches can eat a large part of your budget.</li>
<li><b>One page for everything.</b> A medical practice administrator wants to see medical office cleaning, not a list of every service you offer.</li>
<li><b>Hiding the trust details.</b> Bonding, insurance and background checks buried in a PDF nobody downloads.</li>
<li><b>Measuring leads instead of walkthroughs.</b> Form fills from people wanting house cleaning or a job look like leads in a report.</li>
</ul>"""),

            ("Measure what matters", """<p>Track four numbers each month: cost per booked walkthrough, walkthrough-to-proposal rate, proposal-to-signed rate, and average contract value by building type. Lots of walkthroughs and few signatures points to pricing or the proposal. If you’d like a senior strategist to build a plan around your crews, territory and target buildings, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much should a commercial cleaning company spend on Google Ads in Houston?",
             "Most small and mid-size janitorial companies in Houston start with $1,500 to $5,000 a month in Google Ads media. The closest benchmark category, Business Services, has a median click cost of $5.87 and a median cost per lead of $93.69, and Houston buyer terms can run higher. Judge spend by cost per booked walkthrough, not cost per click."),
            ("Are Local Services Ads available for commercial cleaning companies?",
             "No. Google’s Local Services Ads category list includes house cleaning, carpet cleaning and window cleaning services, but no commercial cleaning or janitorial category. Signing up as a house cleaner would bring residential leads. Commercial cleaning companies should put their paid search budget into regular Google Ads, and test LSAs only for a separate carpet or window cleaning division."),
            ("How do I get commercial cleaning contracts in Houston?",
             "Build pages for each building type you serve, run Google Ads on buyer keywords with strong negatives, and make a booked walkthrough the goal of every page. Register on the City of Houston’s Beacon Bid portal and the Texas CMBL for public bids. Attend IFMA and BOMA Houston events, and keep a ready RFP packet with insurance and references."),
            ("Do commercial cleaning companies in Texas need to be bonded and insured?",
             "Texas doesn’t require a janitorial bond by law, and private employers can opt out of workers’ compensation. Most commercial clients still ask for general liability insurance, a certificate naming them as additional insureds, and often a janitorial bond. Show all three on your website so buyers don’t have to ask. Confirm your contract requirements with your insurance agent."),
            ("Is LinkedIn advertising worth it for a janitorial company?",
             "It can be, as a supporting channel. LinkedIn lets you target facility managers, property managers and practice administrators by job title, with a $10 minimum daily budget. Clicks cost more than on Google, so use it to stay visible to target accounts between bids and pair it with networking. Google search should still produce most of your walkthroughs."),
        ],
        "figures": {
            "benchmarks": {
                "type": "stats",
                "title": "Google Ads benchmarks closest to commercial cleaning",
                "stats": [["$5.87", "Median CPC, Business Services"], ["$93.69", "Median cost per lead, Business Services"], ["4.85%", "Median conversion rate, Business Services"], ["$75.19", "Median cost per lead, Industrial & Commercial"]],
                "note": "WordStream/LocaliQ 2026 benchmarks, April 2025 to March 2026. No cleaning-specific category exists.",
                "alt": "Google Ads benchmark CPC and cost per lead for commercial cleaning and janitorial companies advertising in Houston",
                "caption": f"Source: {SRC['wordstream']}. Check Keyword Planner for your own Houston ZIP codes.",
            },
            "trust": {
                "type": "checklist",
                "title": "The trust packet commercial buyers expect",
                "sub": "Put these on your website and in every proposal",
                "items": ["General liability certificate, with additional insureds on request", "Janitorial bond covering employee theft", "Workers’ comp status stated plainly", "Background check policy for every crew member", "Supervisor inspection schedule and checklist", "Bloodborne pathogen training for medical sites", "ISSA CIMS or other certification, if held", "References from similar buildings"],
                "alt": "Checklist of trust signals for commercial cleaning companies bidding on Houston and The Woodlands contracts",
                "caption": "Buyers compare vendors on risk first. Make the comparison easy.",
            },
            "ltv": {
                "type": "bars",
                "title": "What one office contract is worth",
                "sub": "20,000 sq ft office, five nights a week, $3,500 a month",
                "items": [["Monthly invoice", 3500, "$3,500"], ["First-year revenue", 42000, "$42,000"], ["Three-year revenue", 126000, "$126,000"], ["Three-year profit at 15-20%", 25200, "$18.9K-$25.2K"]],
                "highlight": [2],
                "note": "Illustrative example",
                "alt": "Illustrative lifetime value of a commercial cleaning contract for a janitorial company in Houston",
                "caption": "Retention drives this math. A client who stays five years is worth far more than a slightly higher monthly rate.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From search to signed contract",
                "stages": [["Ad clicks and calls", "400"], ["Qualified inquiries", "24"], ["Booked walkthroughs", "12"], ["Proposals sent", "10"], ["Signed contracts", "3"]],
                "note": "Illustrative example",
                "alt": "Funnel showing commercial cleaning leads becoming walkthroughs and signed janitorial contracts in Houston",
                "caption": "Track every stage. The walkthrough is the number to optimize ads toward.",
            },
        },
    },
]
