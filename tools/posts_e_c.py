"""Batch 5 lawn care / landscaping pair: "how to get more lawn care customers" (residential, The Woodlands) and
"how to get commercial landscaping contracts" (B2B pursuit plan, North Houston).

Research opened and read: Texas A&M AgriLife (Harris County St. Augustinegrass maintenance calendar HORT-PU-170,
AggieTurf St. Augustinegrass page, L-5519 Turfgrass Selection for Texas), TDA page on licensing to apply pesticides
to lawns for hire, TCEQ RG-470 landscape irrigator rules, KPRC and Space City Weather on Houston freeze dates,
Census QuickFacts for Montgomery County, Google's Local Services Ads category list, GreenPal Houston and LawnStarter
mowing prices, The Woodlands Township covenant FAQ and bid page, a Township streetscape RFB summary, SB 1173 (2025)
bill analysis, HB 3507 (2023) on MUD bid thresholds, Property Code 209.0052, 34 TAC 20.214 (ESBD), Conroe ISD
purchasing, City of Conroe 2026 mowing RFP listing, HOTCOG grounds RFP, Form 1295 guidance, a Harris County MUD
agenda record. Competitors read: Nextdoor business blog, Aspire.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "cal": A("https://harris.agrilife.org/files/2023/02/st-augustinegrass-home-lawn-maintenance-calendar.pdf", "AgriLife’s St. Augustinegrass maintenance calendar"),
    "aggie": A("https://aggieturf.tamu.edu/texas-turfgrasses/st-augustinegrass/", "AggieTurf"),
    "l5519": A("https://agrilifeextension.tamu.edu/wp-content/uploads/2025/06/Turfgrass-Selection-for-Texas.pdf", "Turfgrass Selection for Texas"),
    "tda": A("https://texasagriculture.gov/Regulatory-Programs/Pesticides/Agricultural-Applicators/Applying-Pesticides-to-Lawns-Trees-Ornamentals", "Texas Department of Agriculture"),
    "tceq": A("https://www.tceq.texas.gov/downloads/compliance/publications/rg/rg-470", "TCEQ’s landscape irrigation rules (RG-470)"),
    "kprc": A("https://www.click2houston.com/weather/2026/02/20/are-freezes-finished-in-houston/", "KPRC"),
    "scw": A("https://spacecityweather.com/winter-houston-probably-over/", "Space City Weather"),
    "census": A("https://www.census.gov/quickfacts/fact/table/montgomerycountytexas", "Census QuickFacts"),
    "lsa": A("https://support.google.com/localservices/answer/6224841?hl=en", "Google’s Local Services Ads category list"),
    "gp": A("https://www.yourgreenpal.com/blog/how-much-does-lawn-care-cost-in-houston-tx", "GreenPal’s 2026 Houston price guide"),
    "ls": A("https://lawnstarter.com/blog/cost/lawn-mowing-price", "LawnStarter"),
    "cov": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/FAQ", "Township’s covenant FAQ"),
    "bids": A("https://www.thewoodlandstownship-tx.gov/Departments/Finance/Purchasing-Procurement/Bids", "The Woodlands Township’s bid page"),
    "rfb": A("https://www.nationgraph.com/rfps/rfp-cb83d733-2027-2029-rfbstreetscapeand-town-cente", "a summary of the 2027-2029 streetscape RFB"),
    "sb": A("https://capitol.texas.gov/tlodocs/89R/analysis/pdf/SB01173F.pdf", "SB 1173"),
    "hb3507": A("https://capitol.texas.gov/tlodocs/88R/billtext/html/HB03507F.htm", "HB 3507"),
    "poa": A("https://texas.public.law/statutes/tex._prop._code_section_209.0052", "Texas Property Code section 209.0052"),
    "esbd": A("https://www.law.cornell.edu/regulations/texas/34-Tex-Admin-Code-SS-20-214", "state purchasing rules"),
    "cisd": A("https://www.conroeisd.net/page/purchasing/", "Conroe ISD’s purchasing page"),
    "conroe": A("https://samsearch.co/gov-explore/sled/annual-mowing-services/274173", "City of Conroe’s 2026 annual mowing RFP"),
    "hotcog": A("https://www.hotcogtx.gov/media/userfiles/subsite_185/files/groundsrfp2026.pdf", "a Heart of Texas Council of Governments grounds RFP"),
    "f1295": A("https://www.thecolonytx.gov/367/Certificate-of-Interested-Parties-Form-1", "Form 1295"),
    "mud": A("https://civiciq.com/public-contract/076c2d72-d98d-4315-97a7-9a5678047434", "one Harris County MUD’s June 2026 agenda"),
    "mudfaq": A("https://www.jbgoodwin.com/knowmud.htm", "a JBGoodwin explainer"),
}

SIB1 = "how-to-get-more-lawn-care-customers-the-woodlands"
SIB2 = "how-to-get-commercial-landscaping-contracts-houston"

POST1 = {
    "slug": SIB1,
    "title": "How to Get More Lawn Care Customers in The Woodlands and Houston",
    "seo_title": "How to Get More Lawn Care Customers in Houston",
    "desc": "How to get more lawn care customers in The Woodlands and Houston: tighter routes, Nextdoor, Google, reviews and licensed upsells that recur.",
    "category": "Local marketing",
    "icons": ["Google Business Profile", "Nextdoor", "Google Ads"],
    "art": "b3",
    "hero": "lawn",
    "hero_alt": "Illustration of a freshly striped lawn for a guide on how to get more lawn care customers in The Woodlands and Houston",
    "related": ["is-nextdoor-advertising-worth-it", "complete-guide-google-reviews", "local-services-ads-vs-google-ads-home-services"],
    "sections": [
        (None, f"""<p>The cheapest way to get more lawn care customers in The Woodlands and Houston is to sell the streets you already mow. Hang door hangers on the houses around every finished lawn, keep your Google Business Profile and Nextdoor page busy with real photos, and ask happy customers for reviews and neighbors. Once the route is full, add fertilization, weed control and irrigation work to the same addresses, which pays more per stop and keeps billing alive in January.</p>
<p>Say you run two crews out of Spring. Your problem probably isn’t finding lawns. It’s that the lawns you have are spread from Magnolia to Kingwood. So we start with the route, not the ads.</p>"""),

        ("How to get more lawn care customers on the streets you already mow", f"""<p>A lot of mowing companies take any lead inside 25 miles and then spend half the day on FM 1488 and the Grand Parkway.</p>
<p>Route density is the profit in mowing. If your crew finishes a lawn and the next one is three doors down, you’re mowing. If it’s 20 minutes away on the Grand Parkway, you’re paying two people to sit in a truck. So the best new customer is a neighbor of an existing one, and your marketing should be built around that.</p>
<!--fig:route-->
<p>Here’s rough math for one two-person crew. These are our planning numbers, not industry data:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Route type</th><th>Avg. drive between lawns</th><th>Lawns per 9-hour day</th><th>Revenue at $45 a lawn</th></tr></thead>
<tbody>
<tr><td>Scattered (whole metro)</td><td>18 minutes</td><td>11</td><td>$495</td></tr>
<tr><td>Clustered (a few ZIPs)</td><td>8 minutes</td><td>15</td><td>$675</td></tr>
<tr><td>Dense (same village or subdivision)</td><td>2 minutes</td><td>19</td><td>$855</td></tr>
</tbody></table></div>
<p>Same crew, same fuel, nearly 75% more revenue on the dense route. That’s why we tell lawn companies to pick five or six neighborhoods and own them before advertising anywhere else.</p>
<h3>The “neighbor of” playbook</h3>
<ol><li>Every time you start a new account, hang door hangers on the 10 nearest houses that day. Say “We mow for your neighbor on Timber Ridge” on the hanger (street name only, never the address).</li>
<li>Offer a neighbor rate: a small discount for any house on the same street, because it costs you less to serve.</li>
<li>Leave a yard sign for 48 hours after the first mow, if the customer agrees and the HOA allows it. Check the deed restrictions first.</li>
<li>Track which streets produce. If Alden Bridge converts and Cochran’s Crossing doesn’t, shift the hangers.</li></ol>"""),

        ("Lawn care advertising ideas that work in HOA neighborhoods", f"""<p>The Woodlands, Spring, Cypress and the master-planned communities along the Grand Parkway are built for lawn care marketing. Lots are similar sizes, so pricing is easy. Neighbors watch each other’s yards. And the rules push people toward hiring help.</p>
<p>The {SRC['cov']} says deed restrictions “require that properties be kept in good order and repair. That includes yard maintenance,” and violations lead to notices to the owner. A homeowner who just got a covenant letter about an overgrown yard is about as ready to buy as anyone you’ll ever meet. The same FAQ says The Woodlands encourages “natural yards” with less grass and more forest, which is a selling point for bed maintenance, mulch and pine straw, not only mowing.</p>
<!--fig:map-->
<p>Lawn care advertising ideas we’d try, roughly in order of cost:</p>
<ul><li><b>Nextdoor Business Page and posts.</b> Free, and neighbors ask “who mows for you?” constantly. Respond fast, with a photo. Our <a href="/blog/is-nextdoor-advertising-worth-it/">Nextdoor advertising breakdown</a> covers when paid ads and Opportunity Alerts are worth adding.</li>
<li><b>Door hangers around active jobs.</b> Cheap and pointed at the exact houses that help your route.</li>
<li><b>Yard signs.</b> Short-term, permission-based, and only where the deed restrictions allow them.</li>
<li><b>Truck and trailer wraps.</b> Your trucks are parked in these neighborhoods all week. Put the phone number big enough to read from a driveway.</li>
<li><b>Village association and HOA newsletter ads.</b> Many accept local business ads. Ask the management company.</li>
<li><b>Facebook and Instagram ads limited to your ZIP codes.</b> Before-and-after photos of a real lawn in the neighborhood beat any stock image.</li></ul>
<p>We’d skip mass mailers to the whole county. They spread you thin, which is the opposite of what your route needs.</p>"""),

        ("When Houston homeowners pick a lawn service", f"""<p>Up north, lawn care is a short-season business. Here the grass grows most of the year, which changes when your marketing has to run.</p>
<p>{SRC['cal']}, published through the Harris County Extension office, has weekly mowing starting in spring once St. Augustine is actively growing, fertilizer going down after the lawn has been mowed twice, and irrigation running until the turf stops growing in late fall. Even in December through February it says to mow “if necessary” to keep winter weeds from flowering. Houston’s average last freeze lands around February 15, according to {SRC['kprc']}, and {SRC['scw']} notes it runs later, into late February or early March, for areas north of the city like The Woodlands.</p>
<!--fig:season-->
<p>The grass matters too. {SRC['aggie']} calls St. Augustinegrass “one of the most widely planted turfgrass species in Texas,” and the AgriLife guide {SRC['l5519']} says it’s best adapted to Southeast Texas and is the most shade-tolerant warm-season grass. That shade tolerance matters under The Woodlands’ pine canopy. St. Augustine also comes with problems most homeowners can’t diagnose, like chinch bugs in summer, large patch in fall and take-all root rot, and each one is a reason to call a pro.</p>
<p>How that turns into a marketing calendar:</p>
<ul><li><b>February is your sign-up month.</b> Homeowners decide who’s mowing this year before the first spring cut. Push door hangers and ads in late January and February, not April.</li>
<li><b>Summer is retention season.</b> July heat browns lawns and frustrates people. A text that says “your lawn is heat stressed, here’s what we’re doing” keeps the account.</li>
<li><b>Fall is your upsell window.</b> AgriLife times the last nitrogen 4 to 6 weeks before the first frost and fall pre-emergent for winter weeds. That’s a natural pitch for a fertilization program.</li></ul>"""),

        ("How to get more lawn care leads from Google", f"""<p>Door hangers reach people who weren’t looking. Google reaches the ones who are looking today. Somebody in Creekside Park types “lawn service near me” and picks from the three businesses in the map pack, so you want to be one of them.</p>
<h3>Set up your Google Business Profile properly</h3>
<ul><li>Choose “Lawn care service” as your primary category. Add “Landscaper” or “Landscape designer” as secondary only if you really do that work.</li>
<li>If you don’t have a storefront, hide your address and set a service area by city or ZIP. List the places you want to win, not all of Harris County.</li>
<li>Upload photos every week from real jobs. Fresh photos tell customers you’re active.</li>
<li>Turn on messaging and answer within the hour during the season.</li></ul>
<p>We go deeper on rankings in our <a href="/blog/local-seo-contractors-houston/">local SEO guide for Houston contractors</a>.</p>
<h3>Consider Local Services Ads</h3>
<p>{SRC['lsa']} includes “Lawn care services” and “Landscaping services” in the U.S., so you can get the Google Screened badge and pay per lead instead of per click. LSA leads can cost less than search clicks that never call, but you need a background check, insurance and good reviews to get approved. Our <a href="/blog/local-services-ads-vs-google-ads-home-services/">LSA vs Google Ads comparison</a> walks through the tradeoffs.</p>
<h3>Search ads, carefully</h3>
<p>Regular Google Ads can work for higher-ticket jobs like landscape installs, sod and irrigation repair. For weekly mowing, the margins are thin and clicks aren’t cheap, so keep the budget small, target only your route ZIPs and track every call. If you already run ads, our <a href="/services/search-marketing/">search marketing team</a> can show you which keywords are paying off and which are just spending.</p>"""),

        ("Lawn care marketing ideas that cost almost nothing", f"""<p>Some of the best lawn care marketing ideas don’t need a budget at all. They need a habit.</p>
<ul><li><b>Ask for reviews in person, then text the link.</b> The moment a customer says “the yard looks great” is the moment to ask. Our <a href="/blog/complete-guide-google-reviews/">guide to Google reviews</a> has scripts that don’t feel pushy.</li>
<li><b>Mention specifics in your replies.</b> “Thanks, Linda, glad the St. Augustine bounced back after the chinch bug treatment” helps your profile more than “Thanks!”</li>
<li><b>Referral credit.</b> One free mow for each neighbor who signs up for a season. It costs you about $45 and buys a customer worth well over $1,000 a year.</li>
<li><b>Seasonal texts.</b> A February “we’re booking spring starts” text to last year’s customers and anybody who got a quote but didn’t buy.</li>
<li><b>Photos with every invoice.</b> A quick photo of the finished lawn makes the work visible to people who are at the office when you mow.</li>
<li><b>Partner with real estate agents.</b> Listings need curb appeal fast, and agents remember who saved a closing.</li></ul>
<p>Most competitors try these for a month and drop them by June. Keep doing them through August and you’ll stand out.</p>"""),

        ("Turn mowing into fertilization and weed control (license first)", f"""<p>Mowing gets you in the door. Fertilization and weed control is where the margin is, and it keeps billing in months when the mower barely runs.</p>
<p>Here’s the rule you can’t skip. According to the {SRC['tda']}, anyone who applies any pesticide to grass, trees, shrubs or other plants for hire must be licensed by TDA in the 3A category or by the Structural Pest Control Service, which is now part of TDA. Herbicides count as pesticides, so weed control and most weed-and-feed products fall under that rule. Applying fertilizer only does not need a license from either agency.</p>
<p>So a mowing company can sell a fertilizer-only program on day one. Weed control, fire ant treatment and chinch bug work need the license, or a licensed partner who does the application.</p>
<p>How we’d pitch the program:</p>
<ol><li>Start with a free lawn assessment for current mowing customers in late winter, before pre-emergent timing.</li>
<li>Show what’s wrong with photos: weeds, thin spots, signs of chinch bugs or large patch.</li>
<li>Offer a set program on the AgriLife calendar, billed monthly so it feels like the mowing bill.</li>
<li>Report after each visit with a photo and a note on what you applied.</li></ol>
<p>{SRC['gp']} puts Houston fertilization and weed control at $50 to $150 per application and $500 to $1,500 a year for a bundled program, with most programs running seven or eight applications.</p>"""),

        ("Irrigation checks: the upsell that needs a TCEQ license", f"""<p>Sprinklers are the other big add-on in Houston, especially after a summer like most of ours. They’re also where many lawn companies get sloppy.</p>
<p>Under {SRC['tceq']}, a person who “sells, designs, installs, maintains, alters, repairs, or services an irrigation system” needs a TCEQ irrigator license. Homeowners working on their own property are exempt; your crew is not. That covers more than new installs. Swapping a broken head or changing a controller program for a customer counts as servicing. Backflow assemblies also have to be tested by a licensed backflow tester after they’re installed or repaired.</p>
<p>If someone on your team holds the license, market it hard. A spring “sprinkler checkup” and a summer “water-saving audit” are easy sells in neighborhoods where people get covenant letters about brown lawns. If nobody does, refer the work to a licensed irrigator you trust and ask for referrals back.</p>"""),

        ("The pricing and upsell math", f"""<p>Here’s why the upsell matters more than the next mowing customer.</p>
<p>{SRC['gp']} puts a typical Houston mow, edge and blow at $35 to $55 per visit for a standard suburban lot. Nationally, {SRC['ls']} lists $44 to $71, averaging $57. Take $45 a visit and about 34 visits a year, weekly through the main season and every other week on the shoulders. That’s roughly $1,530 a year from one yard.</p>
<!--fig:upsell-->
<p>Add a $700 fertilization program and two $95 irrigation checks and the same address is worth about $2,420, with no extra drive time. Those are illustrative figures, and yours will vary with lot size, products and labor.</p>
<p>Quick pricing tips:</p>
<ul><li>Quote by lot size and obstacles, not a flat number for every house.</li>
<li>Offer annual agreements with monthly billing so revenue stays steady in January.</li>
<li>Raise prices at season start, with notice, instead of mid-year.</li>
<li>Don’t discount mowing to win an account. Discount the add-on instead.</li></ul>"""),

        ("How to get more customers for my lawn care business this month", f"""<p>For a plan you can start Monday, this is the order we’d go in:</p>
<ol><li><b>Pick your target neighborhoods.</b> Five or six villages or subdivisions where you already have accounts.</li>
<li><b>Fix your Google Business Profile.</b> Right category, a service area that matches your route, 20 recent photos.</li>
<li><b>Order door hangers and signs.</b> Hang 10 around every job for the next month.</li>
<li><b>Text every current customer</b> for a review and a referral, with the credit offer.</li>
<li><b>Post on Nextdoor</b> once a week with a real before-and-after.</li>
<li><b>Price your upsell program</b> and pitch it to existing customers first.</li>
<li><b>Track it.</b> Ask every new caller how they found you and write it down.</li></ol>
<p>Once your residential route is full, commercial work is the next step. Our guide on <a href="/blog/{SIB2}/">how to get commercial landscaping contracts</a> covers HOAs, MUDs and public bids. For how we work with home service companies in general, see our <a href="/industries/service/">home services page</a>.</p>
<p>If you’re paying for Google or Meta ads too, check where the clicks come from. A radius around your shop almost always reaches ZIP codes your crews never drive to. Our free <a href="/contact/">Ad Spend Leak Check</a> flags that kind of spend: we record a 10-minute video of your account, mapped against the route you actually run, and send it within 48 hours.</p>"""),
    ],
    "faq": [
        ("How do I get more lawn care customers fast?",
         "Market to the neighbors of customers you already have. Hang door hangers on the houses around each job, ask for a yard sign, and offer a neighbor rate. Then update your Google Business Profile, post before-and-after photos on Nextdoor, and text current customers for reviews and referrals. These steps cost little and fill your route faster than broad advertising."),
        ("What is the best advertising for a lawn care business?",
         "For most local lawn companies, the best return comes from a complete Google Business Profile, steady reviews, Nextdoor, and door hangers around active jobs. Google Local Services Ads include lawn care and landscaping categories and charge per lead. Paid search and social ads can work for bigger jobs like installs and irrigation repair, but keep them limited to your route ZIP codes."),
        ("Do I need a license to spray weeds in Texas?",
         "Yes, if you do it for hire. The Texas Department of Agriculture says anyone applying any pesticide to lawns, trees or shrubs for hire must be licensed through TDA's 3A category or the Structural Pest Control Service. Herbicides are pesticides. Applying fertilizer only does not require a license. Check TDA's current rules before you sell weed control."),
        ("How much should I charge to mow a lawn in Houston?",
         "GreenPal's 2026 Houston guide puts a standard suburban mow, edge and blow at about 35 to 55 dollars per visit, with larger lots costing more. LawnStarter's national range is 44 to 71 dollars. Price by lot size, obstacles and how close the yard is to your existing route, and set annual agreements with monthly billing."),
        ("How do lawn care companies get recurring customers?",
         "They sell season-long agreements instead of one-off mows, bill monthly, and add services that run year-round, like fertilization, weed control, bed maintenance and irrigation checks. In Houston, St. Augustine needs care from early spring into late fall, so a program built on the AgriLife maintenance calendar gives customers a reason to stay all year."),
    ],
    "figures": {
        "season": {
            "type": "columns",
            "title": "Lawn care workload by month, Houston area",
            "sub": "Relative demand for mowing plus treatments on St. Augustine",
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            "values": [12, 22, 55, 85, 100, 100, 95, 95, 90, 75, 45, 12],
            "highlight": [1, 2],
            "y_label": "Workload",
            "note": "Illustrative example based on the AgriLife maintenance calendar",
            "alt": "Column chart of lawn care workload by month in Houston and The Woodlands, peaking May through September",
            "caption": f"Sign-ups happen in February and March, before the work peaks ({SRC['cal']}).",
        },
        "route": {
            "type": "compare",
            "title": "Scattered route vs dense route",
            "left": {"title": "Any lead, anywhere", "items": ["18 minutes between lawns", "About 11 lawns a day", "Fuel and windshield time eat margin", "No neighborhood word of mouth"]},
            "right": {"title": "Own five neighborhoods", "items": ["2 to 8 minutes between lawns", "15 to 19 lawns a day", "Door hangers and signs reinforce each other", "Neighbor referrals keep the route full"]},
            "alt": "Comparison of scattered and dense mowing routes for lawn care customers in The Woodlands, Spring and Cypress",
            "caption": "Route density is the cheapest growth lever a mowing company has.",
        },
        "map": {
            "type": "map",
            "title": "HOA-heavy areas built for route density",
            "sub": "Where similar lots and deed restrictions make neighbor marketing pay",
            "highlight": ["The Woodlands", "Spring", "Cypress", "Tomball", "Magnolia", "Conroe"],
            "alt": "Map of North Houston towns where lawn care companies can get more customers through neighborhood marketing",
            "caption": "Pick five or six neighborhoods inside these areas and saturate them before expanding.",
        },
        "upsell": {
            "type": "bars",
            "title": "Annual revenue from one Houston yard",
            "sub": "Same address, same route, more services",
            "items": [
                ["Mowing only", 1530, "$1,530"],
                ["Mowing + fertilizer program", 2230, "$2,230"],
                ["+ two irrigation checks", 2420, "$2,420"],
            ],
            "highlight": [2],
            "note": "Illustrative example",
            "alt": "Bar chart showing how upsells raise annual revenue per lawn care customer in Houston from mowing only",
            "caption": f"Based on $45 visits, a $700 program and $95 checks; see {SRC['gp']} for local ranges.",
        },
    },
}

POST2 = {
    "slug": SIB2,
    "title": "How to Get Commercial Landscaping Contracts in North Houston",
    "seo_title": "How to Get Commercial Landscaping Contracts in Houston",
    "desc": "How to get commercial landscaping contracts in North Houston: HOAs, MUDs, Township and ISD bids, a bid calendar, insurance and an RFP checklist.",
    "category": "Strategy",
    "icons": ["LinkedIn", "Google", "Google Analytics"],
    "art": "b4",
    "hero": "growth",
    "hero_alt": "Illustration of a rising growth chart for a guide on how to get commercial landscaping contracts in North Houston",
    "related": ["local-seo-contractors-houston", "landing-pages-101", "questions-before-hiring-marketing-agency"],
    "sections": [
        (None, f"""<p>To get commercial landscaping contracts in North Houston, pick the buyers who fit your crew size, learn when each one bids, and be ready before the bid opens. That means insurance certificates, references, a capability page and a site walk-through habit. The buyers here are property management companies, HOAs, municipal utility districts, The Woodlands Township, cities and school districts. Each one has its own rules and calendar.</p>
<p>Most landscapers who move into commercial work can already price a job. Where they lose is earlier: they never get invited, or they hear about the bid after it closes. A Texas HOA generally has to take bids on service contracts over $50,000, and The Woodlands Township took bids in spring 2026 for streetscape work that starts in January 2027. Dates and rules like those decide who’s in the running, so that’s where this guide spends its time.</p>"""),

        ("How to get commercial landscaping contracts: know who signs the check", f"""<p>“Commercial” covers very different buyers. A retail center owner can sign a contract in a week. A school district might take four months and a board vote. Here’s how they compare:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Buyer</th><th>Who decides</th><th>How they buy</th><th>Rule to know</th></tr></thead>
<tbody>
<tr><td>Property management company</td><td>Portfolio or community manager, then owner or board</td><td>Invited proposals, often three bids</td><td>One manager may run many properties</td></tr>
<tr><td>HOA / property owners’ association</td><td>Board, usually advised by the manager</td><td>Bid process set by the association</td><td>Must solicit bids for services over $50,000</td></tr>
<tr><td>Municipal utility district (MUD)</td><td>Elected board, with operator and consultants</td><td>Proposals or formal bids at board meetings</td><td>Written bids from three bidders over $25,000</td></tr>
<tr><td>The Woodlands Township, cities</td><td>Purchasing staff, then elected board or council</td><td>Public RFB or RFP</td><td>Competitive procurement above $100,000</td></tr>
<tr><td>School districts (ISDs)</td><td>Purchasing department, then trustees</td><td>Public RFP through an eBid portal</td><td>Best-value process above $100,000 a year</td></tr>
<tr><td>Office parks, retail centers</td><td>Property or facilities manager</td><td>Relationship plus proposal</td><td>Contract terms set by the owner</td></tr>
</tbody></table></div>
<p>The HOA rule comes from {SRC['poa']}, which requires an association contracting for services over $50,000 to “solicit bids or proposals using a bid process established by the association” (developer-controlled associations are exempt). The $100,000 thresholds for cities, counties and school districts come from {SRC['sb']}, which raised them from $50,000 starting September 1, 2025. We’ll cover the MUD rule below.</p>
<p>A rule of thumb: start with the private buyers if you have one or two crews. Public bids reward companies that already have references, insurance and paperwork ready.</p>"""),

        ("HOAs and property management companies", f"""<p>For most landscapers, this is where commercial growth starts. Master-planned communities across Spring, Cypress, Tomball and Conroe have common areas, entry monuments, detention ponds and amenity centers that need weekly care.</p>
<p>The person to know is the community manager, not the board. Management companies in Houston often run dozens of associations, so one good relationship can lead to several bids. What a manager wants most is a contractor who shows up when promised and never makes them look bad in front of the board.</p>
<h3>How to get on the bid list</h3>
<ol><li>Make a list of the management companies that run communities inside your service area. HOA websites and resale certificates usually name them.</li>
<li>Ask for 15 minutes with the community manager. Bring a one-page capability statement and photos of comparable sites.</li>
<li>Offer a free site walk with a written observation report: dead plant material, irrigation leaks, drainage issues. That’s useful to them even if they don’t switch.</li>
<li>Show up where managers meet. Industry groups for community association managers and commercial property managers hold local events in Houston. Sponsoring a single chapter breakfast puts you in a room with more managers than a month of cold email will reach.</li>
<li>Follow up when the budget is being built. Many HOA boards approve next year’s budget in the fall, so contract changes often get discussed between August and November.</li></ol>"""),

        ("MUDs: the buyer most landscapers forget", f"""<p>If you’ve bought a house in North Houston, you’ve probably paid a MUD tax. A municipal utility district is a political subdivision of Texas, authorized by the TCEQ, that provides water, sewer and drainage to a development, as {SRC['mudfaq']} puts it. An elected board runs it, and many MUDs also maintain parks, trails, detention ponds and landscaped rights-of-way.</p>
<p>They hire landscapers. {SRC['mud']} shows the board discussing ongoing landscaping matters under an existing maintenance contract that expires October 31, 2026 and has a 30-day notice requirement for changes or termination. Contracts like that come up for review regularly, and a short notice period means a board that’s unhappy can switch quickly.</p>
<p>The bidding rules are set in the Water Code. After {SRC['hb3507']} took effect in 2023, district contracts covered by Section 49.273 need written competitive bids from at least three bidders when they’re over $25,000, and advertised bids above $150,000. Many landscape contracts fall in that middle band, so the district will be looking for three qualified bidders. Be one of them.</p>
<p>How to get in front of MUDs:</p>
<ul><li>Board meetings are public and agendas are posted. Read the agendas for districts in your area and look for landscape or maintenance items.</li>
<li>MUDs lean on their operators, engineers and attorneys. Those firms often recommend contractors. Get to know them.</li>
<li>Attend a meeting before you bid. Boards remember who showed up.</li></ul>"""),

        ("Public bids: The Woodlands Township, cities, ISDs and the ESBD", f"""<p>Public work takes more paperwork, but it’s the most open door in commercial landscaping. Anyone who qualifies can bid, and the rules are written down.</p>
<p><b>The Woodlands Township.</b> {SRC['bids']} lists its solicitations, with notices and documents as PDFs and a “Sign-Up for Updates” link for email alerts. In 2026 it bid Streetscape and Town Center Maintenance Services, covering village and neighborhood entries, right-of-way mowing, litter control and Town Center streetscape and waterway maintenance. According to {SRC['rfb']}, the contract runs 36 months, from January 1, 2027 through December 31, 2029. The bids were due in spring 2026, about eight months before the work starts. Miss that window and the next chance may be three years away.</p>
<!--fig:rules-->
<p><b>Cities.</b> {SRC['conroe']} is a useful example. It was posted June 25, held a pre-proposal meeting July 2 at the Public Works training room, and took proposals through OpenGov Procurement on July 16. Scoring was 60 points for cost, 25 for experience and qualifications, 10 for references and 5 for prior city experience. It also asked for a certificate of insurance and Form 1295, among other items.</p>
<p><b>School districts.</b> {SRC['cisd']} says vendors must register through its eBid system to respond to RFPs, registration is free, and registered vendors are notified automatically. It also notes that registering doesn’t make you an approved vendor; you still have to win a bid. Most Houston-area ISDs work the same way, so register with each district you want to serve.</p>
<p><b>State agencies.</b> Under {SRC['esbd']}, state agencies post solicitations estimated over $25,000 on the Electronic State Business Daily (ESBD). That matters if you want state facilities or universities. Cities, MUDs and ISDs usually post on their own portals, so you’ll need to watch both.</p>"""),

        ("Build a bid calendar", f"""<p>Most landscapers who lose public and HOA work don’t lose on price. They find out about the bid after it closes.</p>
<p>A bid calendar fixes that. It’s just a spreadsheet with every buyer you want, their contract end date, when they bid and where they post. Fill it in once, then check it every Monday.</p>
<!--fig:calendar-->
<p>Where to find the dates:</p>
<ul><li><b>Public entities.</b> Bid tabulations and award notices list the contract term. Count back six to nine months from the end date and that’s roughly when the next bid will post.</li>
<li><b>MUDs.</b> Board agendas and minutes mention contract renewals and expirations.</li>
<li><b>HOAs and property managers.</b> Ask directly: “When does your current landscape contract renew?” Most will tell you.</li>
<li><b>Office and retail.</b> Leases and management changes trigger new contracts. A center that just changed hands is worth a call.</li></ul>
<p>Sign up for email alerts on every portal, including the Township, each city’s OpenGov or bid page, each ISD eBid system and the ESBD. Then put a reminder on your calendar 30 days before each expected bid date to prep paperwork.</p>"""),

        ("How to get more commercial landscape accounts from office parks and retail", f"""<p>Private commercial work along I-45, the Grand Parkway and Research Forest Drive is relationship-driven. There’s rarely a public RFP. The facilities manager calls three companies they know.</p>
<p>So the job is getting known before they need you.</p>
<ul><li><b>Drive the corridor.</b> Make a list of office parks, medical buildings, retail centers and churches between the Hughes Landing area and the Grand Parkway. Note who looks under-maintained.</li>
<li><b>Find the manager on LinkedIn.</b> Search “property manager” or “facilities manager” plus The Woodlands, Spring or Conroe. Connect with a short note that names the property, not a pitch.</li>
<li><b>Lead with an observation.</b> “Noticed the irrigation at your east entrance has been running in the rain” is a better opener than a brochure.</li>
<li><b>Offer a walk-through.</b> A 20-minute site walk with the manager is where commercial contracts are won. Bring a tablet, take photos, and send a written summary the same day.</li>
<li><b>Post your commercial work.</b> Photos of a property you maintain, with permission, on LinkedIn and your Google Business Profile.</li></ul>
<p>For search, a separate page targeting commercial terms like “commercial landscaping The Woodlands” helps managers who search before they call. Our <a href="/blog/local-seo-contractors-houston/">local SEO guide for contractors</a> explains how to rank it.</p>"""),

        ("The capability statement page your prospects will check", f"""<p>Before a property manager invites you to bid, they’ll look you up. If your website is all residential mowing specials, you look small.</p>
<p>Build one page, at a URL like /commercial/, that works as your capability statement:</p>
<!--fig:capability-->
<ul><li>Types of properties you maintain, with photos of each</li>
<li>Crew count, equipment and service area map</li>
<li>Licenses: TDA pesticide license and TCEQ irrigator license holders on staff, if you have them</li>
<li>Insurance summary and a line saying COIs are available on request</li>
<li>Three references with names and roles (with their permission)</li>
<li>A downloadable one-page PDF version</li>
<li>A short form asking for property type, size and contract end date</li></ul>
<p>Our <a href="/blog/landing-pages-101/">landing page guide</a> covers layout. If you need the page built, our <a href="/services/web-design-seo-pr/">web design, SEO and PR team</a> does exactly this for service businesses.</p>"""),

        ("Insurance, licenses and references commercial buyers ask for", f"""<p>Commercial buyers will want proof before they sign. Expect requests like these:</p>
<ul><li><b>Insurance.</b> {SRC['hotcog']} in Waco required $2 million in general liability, $1 million in auto liability and workers’ compensation, plus proof of bonding and insurance for all employees. Local requirements vary, so read every RFP and talk to your agent before the bid is due.</li>
<li><b>Licenses.</b> Any herbicide or pesticide work for hire needs a license from the {SRC['tda']}. Irrigation repair or service needs a TCEQ license under {SRC['tceq']}.</li>
<li><b>References.</b> That same RFP asked for at least three references for similar services. Collect them now, from your best residential and small commercial clients.</li>
<li><b>Form 1295.</b> In Texas, {SRC['f1295']} applies to government contracts that need a governing body vote or are worth at least $1 million. You fill it out through the Texas Ethics Commission’s online filing system.</li>
<li><b>Scope detail.</b> That RFP spelled out at least 38 mowings a year, quarterly sprinkler testing and pre-emergent in February and September. Expect that level of detail and price every line.</li></ul>
<p>Scoring varies too. Conroe’s mowing RFP put 60 points on cost; the Waco-area RFP put only 40 on cost and 35 on demonstrated performance. Read the scoring and spend your effort where the points are.</p>"""),

        ("Commercial landscaping bids: an RFP response checklist", f"""<p>Use this before you submit anything:</p>
<!--fig:rfp-->
<ol><li>Read the whole package, including every addendum. Large public bids like the Township’s streetscape contract often issue more than one.</li>
<li>Attend the pre-bid meeting or site walk, even if it’s optional.</li>
<li>Submit questions before the deadline, in writing.</li>
<li>Match your pricing to the bid form exactly. Don’t add line items they didn’t ask for.</li>
<li>Include every required form: COI, Form 1295 if needed, signed addenda, references.</li>
<li>Write a short cover letter that restates the scope and names your account manager.</li>
<li>Submit a day early through the right portal. Late is disqualified.</li>
<li>After the award, request the bid tabulation and see where you landed.</li></ol>
<p>If you win, the first 90 days decide the renewal. Send a monthly report with photos, keep a single point of contact, and fix complaints within 48 hours.</p>
<p>Your first move doesn’t need a bid package. Open a spreadsheet tonight and add five buyers: two management companies, one MUD, the Township and the ISD closest to your yard. Next to each, write the contract end date if you can find it, or “ask” if you can’t. Then make the calls. Still building your residential base first? See <a href="/blog/{SIB1}/">how to get more lawn care customers</a> in The Woodlands, since good residential references help win the first commercial bids.</p>
<p>One paid-search warning. Ads on “commercial landscaping” terms can still pull homeowners who just want a big yard done. If your phone is full of those calls, our free <a href="/contact/">Ad Spend Leak Check</a> will show which searches are triggering the ads and what to block. It’s a 10-minute recorded review of your Google or Meta account, delivered within 48 hours.</p>"""),
    ],
    "faq": [
        ("How do I get commercial lawn care contracts?",
         "Start with property management companies and HOAs in your service area, since they buy often and decide faster than public agencies. Meet community managers, offer free site walks, and build a commercial page with insurance, licenses and references. Then register on city, ISD and Township bid portals and track contract end dates so you see bids before they close."),
        ("How do I get commercial contracts for landscaping with no experience?",
         "Begin with small commercial properties like churches, medical offices and small retail centers, where a manager can hire you without a formal RFP. Ask your best residential customers to be references. Do a few jobs well, photograph them, and use them to qualify for HOA and MUD work. Public bids usually come later, once you have references and insurance."),
        ("Does an HOA in Texas have to take bids for landscaping?",
         "Generally yes for larger contracts. Texas Property Code section 209.0052 says an association that proposes to contract for services costing more than 50,000 dollars must solicit bids or proposals using its own bid process. Associations still under developer control are exempt during the development period. Smaller contracts can be awarded at the board's discretion."),
        ("What insurance do I need for commercial landscaping bids?",
         "Expect general liability, auto liability and workers' compensation, plus a certificate of insurance naming the client. One Texas grounds RFP required 2 million dollars in general liability and 1 million in auto liability. Requirements vary by buyer, so check each RFP and confirm coverage with your agent before the bid is due."),
        ("Where can I find landscaping bids in Houston?",
         "Check The Woodlands Township bid page, each city's procurement portal such as Conroe's OpenGov page, and each school district's eBid system. State agencies post solicitations over 25,000 dollars on the Electronic State Business Daily. MUD board agendas and HOA managers are the best source for private and district work, which rarely appears on public portals."),
    ],
    "figures": {
        "rules": {
            "type": "stats",
            "title": "Texas bid rules landscapers should know",
            "stats": [
                ["$50K", "HOA service contracts that require bids"],
                ["$100K", "City, county and ISD competitive threshold"],
                ["36 mo", "Township streetscape contract, 2027-2029"],
                ["60%", "of Conroe’s 2026 mowing RFP score was cost"],
            ],
            "note": "Sources: Tex. Prop. Code 209.0052; SB 1173; Township RFB; City of Conroe RFP",
            "alt": "Stat tiles showing Texas bid thresholds for commercial landscaping contracts in Houston and The Woodlands",
            "caption": f"Thresholds from {SRC['poa']} and {SRC['sb']}.",
        },
        "calendar": {
            "type": "steps",
            "title": "How we’d build a landscaping bid calendar",
            "sub": "One spreadsheet, checked every Monday",
            "steps": [
                ["List target buyers", "HOAs, MUDs, Township, cities, ISDs and private properties in your area."],
                ["Find contract end dates", "Use bid tabs, award notices, board minutes or ask the manager."],
                ["Estimate bid dates", "Count back six to nine months from each end date."],
                ["Sign up for alerts", "Township updates, city portals, ISD eBid systems and the ESBD."],
                ["Prep 30 days out", "Pull COIs, references and forms before the bid posts."],
            ],
            "alt": "Five steps to build a bid calendar for commercial landscaping contracts in North Houston",
            "caption": "Most lost bids are bids nobody saw in time.",
        },
        "capability": {
            "type": "compare",
            "title": "What a property manager sees on your site",
            "left": {"title": "Residential-only site", "items": ["Mowing specials and coupons", "No proof of insurance", "Only home lawns pictured", "No references"]},
            "right": {"title": "Commercial capability page", "items": ["Property types and photos", "Licenses and insurance summary", "Named references", "One-page PDF to forward", "Form asking for contract end date"]},
            "alt": "Comparison of a residential site and a capability page for winning commercial landscaping contracts in Houston",
            "caption": "Managers forward your page to owners and boards, so make it easy to share.",
        },
        "rfp": {
            "type": "checklist",
            "title": "RFP response checklist for landscapers",
            "sub": "Run through it before every commercial bid",
            "items": [
                "Read every addendum",
                "Attend the pre-bid meeting or site walk",
                "Submit questions in writing before the deadline",
                "Price exactly to the bid form",
                "COI, Form 1295 if required, signed addenda",
                "Three references for similar sites",
                "Short cover letter naming your account manager",
                "Submit a day early through the right portal",
            ],
            "alt": "Checklist for responding to commercial landscaping bids and RFPs in The Woodlands and Houston",
            "caption": f"Items drawn from {SRC['conroe']} and similar Texas RFPs.",
        },
    },
}

POSTS = [POST1, POST2]
