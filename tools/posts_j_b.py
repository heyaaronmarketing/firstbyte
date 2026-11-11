"""Batch 10 (module b): tree service marketing in Houston and The Woodlands, junk removal marketing in Houston, and
independent P&C insurance agency marketing in Houston.

Research, tree post: FOX Weather on the May 16, 2024 derecho (NWS survey of 100 mph winds downtown, at least seven
deaths, 800,000+ Houston-metro outages); T&D World on CenterPoint's 2.26 million Beryl outages and severe tree damage;
Community Impact on Beryl in The Woodlands (35 trees on homes on July 8, a resident's uprooted pine) and on the
township's extra $2 million and Montgomery County's ~1 million cubic yards of debris; Houston Landing on post-Beryl
contractor scams (don't pay upfront, don't sign over insurance checks); Texas AG on the three-day cancellation right for
door-to-door contracts; Texas A&M Forest Service on oak wilt (no pruning February-June, paint wounds year-round, 76
counties, Central and West Texas); ISA credential page, Jobber's summary of eligibility and CEUs, ISA's arborist
verification tool; Texas Trees Foundation on asking for liability and workers' comp proof; Google's LSA category list
(Tree services; Junk removal services; Insurance agency limited to California and Florida); City of Houston Solid
Waste November 2, 2026 release (heavy trash including tree waste collected in even-numbered months).
Junk post: Google Business Profile help on service-area businesses (hide address, up to 20 service areas, about two
hours' drive); ABC13 Feb 2026 on One Clean Houston funding running out (8,200+ dumping calls in 12 months, 120 cameras);
Axios Houston on Harris County dumping prosecutions (46 charges in 2025, 150-200 mobile cameras); Texas Health &
Safety Code 365.012 penalty tiers via Texas Public Law.
Insurance post: TDI homeowners market overview (average premium $3,489 in 2025 vs $1,791 in 2016; 21.1%, 18.7%, 4.3%
average rate changes 2023-2025; State Farm, Allstate, USAA shares; 90-day filed average -4.0%); Carrier Management Oct
2026 on rate decreases; Community Impact on Cy-Fair premiums, nonrenewals and Kinder Institute flood exposure; TWIA
overview (14 counties plus parts of Harris County east of SH 146, insurer of last resort, WPI-8); FloodSmart agent
resource on the 30-day waiting period; IIAT summaries of 28 TAC Chapter 21 advertising rules and rebating/referral fee
rules; WordStream 2025 Google Ads benchmarks (Finance & Insurance); Jon Loomer on Meta's Financial Products and
Services category including insurance; Google's housing/employment/credit policy FAQ (no insurance); Morrison Foerster
and Goodwin on the Eleventh Circuit vacating and the FCC removing the one-to-one consent rule; Morgan Lewis and Mondaq on
Texas SB 140 and its exemptions.
Competitor/PAA phrasing read for "tree service marketing", "how to get more tree service customers", "tree service
google ads", "junk removal marketing", "how to get more junk removal jobs", "insurance agency marketing", "how to get
more home insurance clients", "insurance agent facebook ads".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # tree post
    "fox_derecho": A("https://www.foxweather.com/weather-news/thunderstorm-damage-houston-texas.amp", "FOX Weather’s report on the derecho"),
    "tdw_beryl": A("https://tdworld.com/disaster-response/news/55125353/centerpoint-energy-restores-power-to-more-than-1-million-customers-following-hurricane-beryl", "T&amp;D World"),
    "ci_beryl_tw": A("https://communityimpact.com/the-woodlands/weather/beryls-effects-in-the-woodlands-include-35-downed-trees-on-homes-7-rescues/", "Community Impact"),
    "ci_debris": A("https://communityimpact.com/the-woodlands/government/the-woodlands-township-approves-2m-for-debris-removal-after-beryl/", "Community Impact reported"),
    "hl_scams": A("https://houstonlanding.org/scammers-are-likely-lurking-in-the-aftermath-of-hurricane-beryl-heres-what-to-look-out-for", "Houston Landing’s post-Beryl scam guide"),
    "oag_door": A("https://oag.state.tx.us/news/releases/paxton-issues-consumer-alert-warning-texans-scammers-aftermath-houston-storms", "the Texas Attorney General’s office"),
    "tfs_ow": A("https://tfsweb.tamu.edu/oak-wilt-disease-threatens-texas-oaks-in-spring", "Texas A&amp;M Forest Service"),
    "tfs_faq": A("https://tfsweb.tamu.edu/oakwiltfaqs", "the Forest Service’s oak wilt FAQ"),
    "isa": A("https://www.isa-arbor.com/Credentials/Types-of-Credentials/ISA-Certified-Arborist", "ISA Certified Arborist credential"),
    "jobber_isa": A("https://www.getjobber.com/academy/tree-service-arborist/how-to-become-an-arborist/", "Jobber’s summary of the requirements"),
    "isa_find": A("https://www.treesaregood.org/findanarborist/arboristsearch", "ISA’s public lookup tool"),
    "ttf": A("https://texastrees.org/how-to-hire-an-arborist/", "Texas Trees Foundation"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "hou_heavy": A("https://houstontx.gov/solidwaste/press-11022026.html", "the city’s Solid Waste Management Division"),
    # junk post
    "gbp_sab": A("https://support.google.com/business/answer/2853879?hl=en", "Google’s help page on hiding your address"),
    "gbp_areas": A("https://support.google.com/business/answer/9157481", "Google’s service-area guidance"),
    "abc_dump": A("https://abc13.com/post/houston-program-aimed-cracking-down-illegal-dumping-runs-money/18645759/", "ABC13 reported in February 2026"),
    "axios_dump": A("https://www.axios.com/local/houston/2026/06/04/houston-illegal-dumping-harris-county-district-attorney", "Axios Houston"),
    "hsc365": A("https://texas.public.law/statutes/tex._health_&amp;_safety_code_section_365.012", "Texas Health and Safety Code Section 365.012"),
    # insurance post
    "tdi_mkt": A("https://www.tdi.texas.gov/general/texas-homeowners-insurance-market-overview.html", "TDI’s homeowners market overview"),
    "cm_rates": A("https://www.carriermanagement.com/news/2026/10/08/292585.htm", "Carrier Management"),
    "ci_cyfair": A("https://communityimpact.com/houston/cy-fair-jersey-village/real-estate/2025/07/10/home-insurance-rates-on-the-rise-in-cy-fair", "Community Impact’s Cy-Fair report"),
    "twia": A("https://www.twia.org/about-us/overview", "TWIA’s own overview"),
    "nfip": A("https://agents.floodsmart.gov/resource-library/en/2024-flooding-disaster-response-social-graphic-30-day-coverage-gap", "FloodSmart’s agent resources"),
    "iiat_ads": A("https://www.iiat.org/agency-operations/insurance-laws-regulations/insurance-laws-regulations-sales-marketing/advertising", "IIAT’s summary of the Texas advertising rules"),
    "iiat_reb": A("https://www.iiat.org/agency-operations/insurance-laws-regulations/insurance-laws-regulations-sales-marketing/rebating-and-referral-fees", "IIAT’s summary of rebating and referral rules"),
    "ws": A("https://wordstream.com/blog/2025-google-ads-benchmarks", "WordStream’s 2025 benchmarks"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "gfaq": A("https://support.google.com/adspolicy/answer/9997418?hl=en", "Google’s personalized ads policy FAQ"),
    "mofo": A("https://www.mofo.com/resources/insights/250130-eleventh-circuit-vacates-fcc-s-tcpa-one-to-one-consent-rule", "Morrison Foerster"),
    "goodwin": A("https://www.goodwinlaw.com/en/insights/blogs/2025/09/the-fcc-issues-final-rule-formally-eliminating-the-one-to-one-consent-requirement", "Goodwin"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    "mondaq_tx": A("https://www.mondaq.com/unitedstates/privacy-protection/1676466/new-amendments-to-texas-telemarketing-law-have-gone-into-effectsellers-should-carefully-consider-the-exemptions", "a Mondaq review of the exemptions"),
}

TREE = "/blog/tree-service-marketing-houston-the-woodlands/"
JUNK = "/blog/junk-removal-marketing-houston/"
INS = "/blog/insurance-agency-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: tree service
    {
        "slug": "tree-service-marketing-houston-the-woodlands",
        "title": "Tree Service Marketing in Houston and The Woodlands: Storm Calls, Trimming Work and Trust",
        "seo_title": "Tree Service Marketing in Houston & The Woodlands",
        "desc": "Tree service marketing for Houston and The Woodlands: storm-ready Google Ads, LSA, ISA and insurance proof, oak wilt timing and a year-round plan.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Nextdoor"],
        "art": "b2",
        "hero": "lawn",
        "hero_alt": "Illustration of trees and a yard for tree service marketing in Houston, The Woodlands and Spring",
        "related": ["roofing-marketing-houston-storm-season", "how-to-get-more-lawn-care-customers-the-woodlands", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>The morning after a bad storm line, a two-crew tree company in Spring has 60 voicemails before 7 a.m. A pine is lying across a roof in Panther Creek. A water oak has a driveway in Kingwood blocked. Somebody in Cypress wants a price on “the big limb hanging over the kids’ room,” and three people just want to know if you’re real.</p>
<p>Six weeks later the same owner is staring at an empty October calendar, wondering where everyone went.</p>
<p>Tree service marketing in Houston has two jobs that pull in opposite directions. When a storm hits, you need to be findable, answer fast and look trustworthy to people who are scared and being door-knocked by trucks with out-of-state plates. The rest of the year, you need a steady pipeline of trimming, removals and stump grinding that keeps crews busy without a hurricane doing your sales for you.</p>
<p>This post covers both: the Google setup, the ad campaigns we’d split, the proof that wins the call, and a seasonal calendar built around Houston weather and the oak pruning rules.</p>"""),

            ("Two businesses in one truck", f"""<p>Most tree companies market themselves as one thing. They’re really two.</p>
<p><b>Emergency work</b> is a tree on a house, a car, a fence or a power drop. The customer wants someone today, will pay a premium, and decides in minutes based on who answers and who looks legitimate. Price shopping is light. Trust is everything.</p>
<p><b>Planned work</b> is trimming, crown cleaning, deadwood removal, clearance over the roof, removals of dying trees, stump grinding, lot clearing and plant health care. These customers get two or three bids, read reviews, look at your photos and take a week or a month to decide.</p>
<p>The two need different keywords, different landing pages, different ad schedules and different budgets. When they share one campaign and one “Tree Services” page, the emergency budget gets spent on someone price-checking crape myrtle trimming in March, and the storm calls hit a page that doesn’t mention emergencies at all.</p>
<p>Keep that split in mind. It shows up in every section below.</p>"""),

            ("What Houston storms do to tree demand", f"""<p>Houston gets tree emergencies from more than hurricanes. The May 16, 2024 derecho is the clearest recent example. A National Weather Service survey found straight-line winds peaking around 100 mph in downtown Houston, at least seven people died, and more than 800,000 Houston-metro customers lost power, per {SRC['fox_derecho']}. Falling trees were among the causes of death named by city officials.</p>
<p>Seven weeks later, Hurricane Beryl knocked out power to 2.26 million CenterPoint customers, and the utility reported severe tree damage across its system, according to {SRC['tdw_beryl']}. In The Woodlands alone, the fire department logged 35 trees on homes and 32 trees blocking roads on July 8, per {SRC['ci_beryl_tw']}, which quoted a Panther Creek resident saying he’d never seen a pine uprooted like the one that hit his house. Afterward, {SRC['ci_debris']} that the township approved an additional $2 million for debris removal while the county worked to move around 1 million cubic yards of storm debris.</p>
<!--fig:storms-->
<p>North Houston’s tall pines are a big part of why. Loblollies over a roofline are the call nobody wants to make and everybody makes eventually. That’s also your planned-work pitch: a lot of storm damage is preventable with clearance pruning and removals of trees that were already leaning or declining.</p>
<p>Hurricane season runs June 1 to November 30. Spring brings its own squall lines, and winter freezes snap limbs too. So “storm season” in tree marketing covers most of the year, and your setup needs a switch you can flip in an afternoon.</p>"""),

            ("The storm-chaser trust gap", f"""<p>After every big Houston storm, trucks show up from other states with chainsaws, a magnetic sign and a phone number. Some do honest work. Some take a deposit and disappear. Homeowners know this now, and it changes how they pick a tree company.</p>
<p>The post-Beryl advice from {SRC['hl_scams']} was blunt: make sure the contractor is licensed and insured, get several quotes, don’t pay upfront, be wary of pressure to sign quickly, and don’t sign over insurance checks to start repairs. And {SRC['oag_door']} has reminded Texans that state law lets them cancel a contract with a door-to-door seller within three days of signing.</p>
<p>Your marketing should answer the questions a nervous homeowner is already asking. Homeowners can’t look up a tree crew on TDLR the way they can an electrician, so the proof has to come from you.</p>
<!--fig:trust-->
<p>Put these on your website, your Google Business Profile and your estimates:</p>
<ul>
<li>A local street address or at least a clear home base (“based in Spring since 2011, serving north Harris and south Montgomery County”).</li>
<li>Your certificate of insurance, available on request the same day, with general liability and workers’ comp named. Say so on the emergency page in plain words.</li>
<li>Photos of your actual trucks, crane or grapple saw, and crew in branded shirts. Stock photos of a man in a harness read as fake.</li>
<li>A payment policy that says no full payment before the work is done, and that you’ll provide photos and an itemized invoice for the insurance claim.</li>
<li>Reviews that mention storms by name. “Came out the day after Beryl and got the pine off our roof” is worth more than ten “great job” reviews.</li>
</ul>
<p>You’re selling the opposite of a storm chaser. Make that obvious without ever naming or mocking anyone.</p>"""),

            ("ISA certification and insurance: the credentials that sell", f"""<p>The {SRC['isa']} is the closest thing tree care has to a license homeowners recognize. Candidates generally need three years of full-time tree care experience (a related degree can substitute for some of it), must pass the exam, and recertify every three years with 30 continuing education units, per {SRC['jobber_isa']}. Customers can confirm a certification with {SRC['isa_find']}.</p>
<p>The {SRC['ttf']} tells homeowners to look for ISA certification and to ask for proof of liability and workers’ compensation insurance, with the insurer’s phone number if they want to check. So the people researching you are being coached to ask. Answer before they do.</p>
<ul>
<li>Name your certified arborists on the site with their certification numbers and a photo. If the owner is certified, say it in the first screen of the homepage.</li>
<li>Put “ISA Certified Arborist on staff” in your Google Business Profile description and in ad copy, but only if it’s true today. Expired certifications are easy to check.</li>
<li>Offer a written assessment for removals of large or high-value trees. Homeowners in The Woodlands, Memorial or the Heights often want a second opinion before cutting down a 60-year-old oak.</li>
<li>Show the equipment that limits risk to their property: crane work, rigging, ground protection mats.</li>
</ul>
<p>Certification and insurance won’t fill your calendar by themselves. They decide who wins the call once three companies show up in the same search.</p>"""),

            ("Oak wilt and the February-through-June rule", f"""<p>{SRC['tfs_ow']} advises that oaks shouldn’t be pruned or wounded from February through June, when the beetles that spread oak wilt are most active, and that wounds on oaks should be painted at any time of year. Oak wilt has been confirmed in 76 Texas counties and is hitting Central and West Texas hardest, per {SRC['tfs_faq']}.</p>
<p>The Houston area isn’t the epicenter, and we wouldn’t scare anyone into thinking it is. But the pruning guidance is a real scheduling fact, and your customers read the same headlines. A homeowner in Montgomery or Magnolia with live oaks they love wants a crew that knows the rule and explains it.</p>
<p>Marketing uses for it:</p>
<ul>
<li>A page titled something like “When to trim oak trees in Houston and Montgomery County” that explains the guidance, your wound-painting practice and how you schedule around it.</li>
<li>An email and social push in late fall and January to book oak work before February. That fills what is often a slower stretch.</li>
<li>Training whoever answers the phone to say “we’ll schedule your oak for July” instead of quietly doing it in April.</li>
</ul>
<p>It shows expertise in a way a homeowner can verify, which is the whole point.</p>"""),

            ("Google Business Profile and Local Services Ads", f"""<p>The map pack is where “tree removal near me” gets decided. Set the profile up for both of your businesses.</p>
<ul>
<li>Primary category: <b>Tree service</b>. Add secondary categories only for real services from Google’s list, such as an arborist or stump-related category if it fits.</li>
<li>Services: list emergency tree removal, storm cleanup, tree trimming, tree removal, stump grinding, lot clearing and plant health care as separate entries with one-line descriptions.</li>
<li>Hours: if you really answer at 2 a.m. after a storm, say 24 hours. If you don’t, don’t. Angry callers who reach voicemail leave reviews.</li>
<li>Photos: before-and-after shots by neighborhood, crane jobs, crews in gear. Add a batch after every storm week.</li>
</ul>
<p>Our {L('/blog/rank-in-google-map-pack-houston/', 'Houston map pack guide')} covers the ranking factors in detail.</p>
<p>Local Services Ads are worth a test. “Tree services” is on {SRC['lsa']}, so tree companies can run the pay-per-lead ads that sit above regular search results, usually with the Google Verified badge after background and insurance checks. You pay per lead, can dispute junk leads, and your rank leans heavily on reviews and how fast you respond.</p>
<p>Two cautions from storm weeks. Set a weekly budget you can actually service, because LSA can hand you 40 leads a day after a hurricane and every unanswered one hurts your ranking. And pause the moment you’re booked out for two weeks. We compare LSA and regular search ads in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}, and the badge question in {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified')}.</p>"""),

            ("Google Ads: an emergency campaign and a trimming campaign", f"""<p>This is where the two-businesses idea pays off. Build two campaigns with separate budgets.</p>
<p><b>Emergency campaign.</b> Keywords like “emergency tree removal,” “tree fell on house,” “tree on roof,” “fallen tree removal near me,” “storm tree removal Houston,” “24 hour tree service.” Call-focused ads, call assets on, and a landing page that loads fast on a phone with a giant tap-to-call button, your insurance line and photos of crane jobs. Keep it running year-round at a low budget so it has history, then raise the budget the day a storm is forecast, before landfall. Bids spike after a storm when every company in Texas turns on ads.</p>
<p>Sample ad:</p>
<p><i>Tree on Your Roof? Local Crew Today | ISA Certified, Fully Insured | Crane and Grapple Saw Removal. Spring-Based Since 2011. Photos and Itemized Invoice for Your Claim. No Payment Before Work.</i></p>
<p><b>Planned-work campaign.</b> Keywords by service and town: “tree trimming The Woodlands,” “tree removal Spring TX,” “stump grinding Cypress,” “pine tree removal Conroe,” “oak tree trimming Kingwood,” “tree removal cost.” Send each ad group to the matching service page, which should show starting prices or typical ranges and a “send us photos for a quote” form. Schedule it for business hours.</p>
<p>Negatives keep both campaigns clean:</p>
<!--fig:negatives-->
<p>A few settings matter more than people think. Use “Presence: people in or regularly in your included locations.” Draw the radius around where you’ll actually drive a crane. Track calls over 60 seconds as conversions, plus form submissions, using our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')}. Our {L('/services/search-marketing/', 'search marketing team')} builds this structure for home service companies, and the {L('/blog/roofing-marketing-houston-storm-season/', 'roofing storm-season post')} covers the same switch-on logic from a roofer’s side.</p>"""),

            ("Job-site marketing, Nextdoor and reviews", f"""<p>A crane in a cul-de-sac is the best ad you’ll ever buy. Every neighbor watches. Most of them have a tree they’ve been worrying about.</p>
<ul>
<li>Yard sign at every job, with permission, for the day and a few days after.</li>
<li>Door hangers on the five houses each side: “We’re working at 14 Elm today. If you’ve got a limb over your roof, we can look while we’re here.”</li>
<li>A neighborhood-specific post on your Business Profile and Nextdoor page with before-and-after photos (no house numbers).</li>
</ul>
<p>Nextdoor fits tree work better than most categories because neighbors ask “who did your trees?” constantly. Our {L('/blog/is-nextdoor-advertising-worth-it/', 'Nextdoor advertising review')} covers when paid placements make sense.</p>
<p>Reviews are the other half. Text the review link the evening the job finishes, when the yard is clean and the customer is relieved. A simple script for the crew lead: “If we did right by you today, a Google review helps a small local company a lot. I’ll text you the link.” Don’t offer discounts for reviews and don’t send the link only to happy customers; both break Google’s rules. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("A seasonal plan built around Houston weather", f"""<p>Tree demand in Houston follows weather, the oak pruning window and the city’s heavy trash schedule. Inside the City of Houston, heavy trash, including bulk and tree waste, is now collected every other month in even-numbered months, per {SRC['hou_heavy']}. A homeowner who saws up a limb in July waits until August for pickup. “We haul everything away the same day” is a real selling point for planned work.</p>
<!--fig:seasons-->
<ul>
<li><b>November to January:</b> book oak pruning before February, removals of dead trees from the past summer, holiday-season “clean up before guests” offers. Email past customers.</li>
<li><b>February to April:</b> pine and non-oak pruning, spring storm readiness, stump grinding. Raise the planned-work budget.</li>
<li><b>May:</b> pre-hurricane-season clearance pruning over roofs and power drops. This is the month to market prevention hardest.</li>
<li><b>June to November:</b> emergency campaign on standby with a storm budget ready, oak work resumes in July, steady trimming in between.</li>
</ul>
<p>Most companies only market in the busy weeks. The ones that grow keep a baseline running all year and use storms as surges, not as the plan.</p>"""),

            ("What to track and what to spend in the first 90 days", f"""<p>Track three numbers by campaign: booked estimates, sold jobs and revenue. Lead counts alone will lie to you after a storm, when everything looks like it’s working.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Planned-work Google Ads</td><td>$1,500 to $3,000</td><td>Service and town ad groups, business hours</td></tr>
<tr><td>Emergency Google Ads (baseline)</td><td>$300 to $800</td><td>Raised sharply in storm weeks</td></tr>
<tr><td>Local Services Ads</td><td>$500 to $1,500</td><td>Weekly cap you can actually answer</td></tr>
<tr><td>Local SEO and profile work</td><td>$500 to $1,500</td><td>Service pages, photos, review replies</td></tr>
<tr><td>Job-site signs and door hangers</td><td>$100 to $300</td><td>Usually the cheapest jobs you’ll book</td></tr>
</tbody></table></div>
<p>Those ranges are examples for a two-to-four-crew company, not quotes or benchmarks. A first 90 days that works:</p>
<ol>
<li><b>Days 1 to 30:</b> fix the Business Profile, build separate emergency and service pages, put insurance and ISA proof on both, start review texts.</li>
<li><b>Days 31 to 60:</b> launch the planned-work campaign, set up the emergency campaign at a low baseline, wire up call tracking.</li>
<li><b>Days 61 to 90:</b> test LSA, cut keywords that produce calls but no estimates, write the storm-week playbook (who answers phones, budget levels, when to pause).</li>
</ol>
<p>If you want a plan built for your crews and service area, <a href="/contact/">get in touch</a> and tell us how many trucks you run and where you want more work.</p>"""),
        ],
        "faq": [
            ("How do I get more customers for my tree service?",
             "Split your marketing into emergency and planned work. Set up your Google Business Profile with the Tree service category, real photos and storm-specific reviews, then run separate Google Ads campaigns for emergency removal and for trimming, removal and stump grinding by town. Show your ISA certification and insurance everywhere, use yard signs and door hangers at every job, and keep a baseline running all year instead of only after storms."),
            ("Are Local Services Ads available for tree services?",
             "Yes. Tree services is one of the categories on Google’s Local Services Ads list, so tree companies can run pay-per-lead ads above regular search results after passing Google’s screening. Availability can vary by area, so start the sign-up with your address to check. Set a weekly budget you can actually answer, because storm weeks can flood you with leads, and slow responses hurt your ranking."),
            ("When should you not trim oak trees in Texas?",
             "Texas A&M Forest Service advises against pruning or wounding oaks from February through June, when the beetles that spread oak wilt are most active, and recommends painting oak wounds at any time of year. Oak wilt is most severe in Central and West Texas, but the guidance is a good practice for oaks anywhere. Tree companies can use it to book oak work in winter and summer."),
            ("How can homeowners tell a real tree company from a storm chaser?",
             "Look for a local address and history, proof of liability and workers’ compensation insurance, an ISA Certified Arborist you can verify with ISA’s lookup tool, and reviews that mention past local storms. Avoid anyone who wants full payment upfront or asks you to sign over an insurance check. Texas law also lets you cancel a door-to-door contract within three days of signing."),
            ("Should a tree service run Google Ads all year?",
             "Yes, at least at a baseline. A year-round planned-work campaign keeps crews busy with trimming, removals and stump grinding between storms, and a small always-on emergency campaign builds history so it performs when you raise the budget before a storm. Companies that only advertise after storms pay the highest click prices and compete with every out-of-town crew at once."),
        ],
        "figures": {
            "storms": {
                "type": "stats",
                "title": "Two 2024 storms and Houston’s trees",
                "stats": [["100 mph", "peak derecho winds downtown, May 2024"], ["2.26M", "CenterPoint customers out after Beryl"], ["35", "trees on homes in The Woodlands, July 8"], ["~1M", "cubic yards of Beryl debris in the county"]],
                "note": "Sources: NWS via FOX Weather, T&D World, Community Impact",
                "alt": "Stats on the 2024 derecho and Hurricane Beryl tree damage in Houston and The Woodlands for tree service marketing",
                "caption": f"From {SRC['fox_derecho']}, {SRC['tdw_beryl']} and {SRC['ci_beryl_tw']}.",
            },
            "trust": {
                "type": "compare",
                "title": "What a nervous homeowner checks",
                "left": {"title": "Storm-chaser signals", "items": ["Out-of-area plates, no address", "Wants payment upfront", "Asks you to sign over the insurance check", "Pressure to sign today", "No insurance certificate"]},
                "right": {"title": "Signals that win the call", "items": ["Local home base and years in business", "No full payment before the work", "Photos and itemized invoice for the claim", "Written estimate, time to decide", "Insurance and ISA proof on request"]},
                "alt": "Comparison of storm chaser warning signs and trust signals for tree service companies in Houston and The Woodlands",
                "caption": "Answer these on your site and estimates before the customer has to ask.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for tree service ads",
                "sub": "Start with these, then read search terms weekly",
                "items": ["Jobs: jobs, hiring, salary, climber, groundsman", "DIY: how to, diy, chainsaw, pole saw, rental", "Free stuff: free wood chips, free mulch, firewood", "Nursery: tree nursery, plant a tree, buy trees", "Off-topic: family tree, tree house, christmas tree", "City programs: city tree permit, 311 (unless you do permits)", "Legal: tree fell on neighbor lawyer, who is responsible", "Courses: arborist course, certification exam"],
                "alt": "Checklist of negative keywords for tree service Google Ads in Houston and The Woodlands",
                "caption": "Keep emergency and planned-work campaigns on the same negative list.",
            },
            "seasons": {
                "type": "columns",
                "title": "Tree service demand by month",
                "sub": "Planned work, before any storm surge",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [55, 60, 75, 80, 90, 70, 75, 65, 60, 50, 55, 45],
                "highlight": [4],
                "y_label": "Relative demand",
                "note": "Illustrative example",
                "alt": "Column chart of illustrative monthly tree service demand in Houston and The Woodlands with a May peak before hurricane season",
                "caption": "Storms add surges on top of this. Market prevention hardest in May.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: junk removal
    {
        "slug": "junk-removal-marketing-houston",
        "title": "Junk Removal Marketing in Houston: How Independents Book More Jobs",
        "seo_title": "Junk Removal Marketing in Houston: Book More Jobs",
        "desc": "Junk removal marketing for Houston independents: Google Ads keywords, service-area Business Profile, LSA, realtor and property manager partners, pricing.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Facebook"],
        "art": "b4",
        "hero": "tools",
        "hero_alt": "Illustration of tools for junk removal business marketing in Houston, Katy, Spring and Cypress",
        "related": ["moving-company-marketing-houston", "property-management-company-marketing-houston", "house-cleaning-business-marketing-houston"],
        "sections": [
            (None, f"""<p>Thursday, 9:15 a.m. A two-truck junk removal company in Spring just had its 10 o’clock cancel. Across the Grand Parkway, a franchise truck with a famous logo is backed up to an apartment complex in Cypress. The owner’s phone buzzes: a realtor needs a garage emptied in Katy before Saturday’s listing photos, and asks if he can text a price off three photos.</p>
<p>He can. That text is the business.</p>
<p>Junk removal marketing in Houston comes down to being the first company that shows up on Google with clear prices, then making booking feel as easy as ordering a pizza. After that, you build a few referral relationships that send you the same kind of job every month. Independents can beat franchises on most of that. The franchises win when independents act like a phone number on a truck.</p>
<p>Below is how we’d set up an independent in Houston, Katy, Spring, Cypress, Pearland or The Woodlands.</p>"""),

            ("Independents vs. franchises: where each one wins", f"""<p>Houston has every national junk brand plus hundreds of one- and two-truck operators. The franchises bring a known name, call centers that answer every time, online booking, uniforms and a lot of reviews. Their weakness is the same thing that makes them consistent. A lot of the experience is scripted, pricing is standardized, and the person who answers often isn’t in Houston.</p>
<!--fig:indie-->
<p>An independent wins with speed and flexibility, and with a real person who answers. Same-day pickup when the franchise is booked until Tuesday. A price off photos in ten minutes. The owner on the job. A crew that speaks Spanish in neighborhoods where that matters (our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing guide')} covers Spanish ads and pages). The willingness to take the weird stuff: a hot tub in Kingwood, a backyard shed in Pearland, a piano up a staircase.</p>
<p>The trap is pricing yourself as the cheap option. You’ll never out-cheap a guy with a trailer on Facebook Marketplace, and the customers who pick on price alone are the ones who argue about the bill. Compete on speed, clarity and trust, and price like a real business.</p>"""),

            ("Know which jobs you want, then market to them", f"""<p>“Junk removal” covers very different jobs with different customers, margins and channels. Pick your favorites and build pages and campaigns for each.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Job type</th><th>Who calls</th><th>Example searches</th><th>Best channel</th></tr></thead>
<tbody>
<tr><td>Single items</td><td>Homeowners, renters</td><td>couch removal, mattress disposal, appliance removal near me</td><td>Google Ads, LSA, Business Profile</td></tr>
<tr><td>Move-outs</td><td>Renters, sellers, landlords</td><td>move out junk removal, apartment cleanout Houston</td><td>Movers and property manager referrals, Google Ads</td></tr>
<tr><td>Estate cleanouts</td><td>Adult children, executors</td><td>estate cleanout Houston, house cleanout after death</td><td>Estate sale companies, attorneys, senior move managers</td></tr>
<tr><td>Garage and attic cleanouts</td><td>Homeowners, sellers</td><td>garage cleanout The Woodlands, attic junk removal</td><td>Google Ads, realtors, Nextdoor</td></tr>
<tr><td>Rental turnovers</td><td>Property managers, landlords</td><td>tenant trash out service, eviction cleanout</td><td>Direct outreach, repeat accounts</td></tr>
<tr><td>Light demo and yard debris</td><td>Homeowners after storms or projects</td><td>shed removal, hot tub removal, storm debris removal</td><td>Google Ads, Business Profile</td></tr>
</tbody></table></div>
<p>Estate cleanouts and rental turnovers are the jobs most independents undersell. They’re bigger tickets, they come through referral partners rather than ads, and the customer cares more about care and speed than price. More on partners below.</p>"""),

            ("Pricing, photos and online booking", f"""<p>Every junk removal customer asks the same thing: how much? “Depends on how much stuff” is true and useless.</p>
<ul>
<li><b>Publish your volume pricing.</b> Most companies price by how much of the truck the load fills. Show starting prices for a single item, a quarter load, half and full, plus surcharges for mattresses, tires or heavy materials. A range beats nothing.</li>
<li><b>Quote by photo.</b> Put “Text us photos for a price” at the top of every page with a real number that reaches someone who answers. This is the single best conversion tool we see in this category.</li>
<li><b>Offer online booking</b> with arrival windows. Plenty of customers, especially move-outs, decide at 10 p.m. and won’t call. Use whatever your field software supports, and make sure a booking triggers a text confirmation.</li>
<li><b>Confirm the final price on site</b> before loading, in writing. Surprise totals are where one-star reviews come from.</li>
</ul>
<!--fig:booking-->
<p>Speed matters as much as price. A customer who texts three companies usually books the first one that answers with a number. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up setup.</p>"""),

            ("Google Business Profile for a service-area business", f"""<p>Most junk removal companies run from a yard or a home, so they’re service-area businesses in Google’s terms. Google lets you hide your address and list a service area instead if you don’t serve customers at your location, per {SRC['gbp_sab']}. You can list up to 20 service areas, and Google’s tip is to keep the whole area within about two hours’ drive of your base, per {SRC['gbp_areas']}.</p>
<p>For a Spring-based company, that might mean Spring, The Woodlands, Tomball, Cypress, Humble, Kingwood, Conroe and a handful of north Houston ZIP codes. Be realistic. Listing all of Greater Houston won’t make you rank in Sugar Land, where you aren’t based.</p>
<ul>
<li>Pick the junk removal category that best matches your main work as primary, and add secondary categories only for services you really do (demolition or a dumpster category, for example, if you actually offer them).</li>
<li>Add each job type from the table above as a service with a short description and a starting price.</li>
<li>Upload real photos every week: loaded trucks, empty garages, crews in shirts. Before-and-after pairs work best.</li>
<li>Keep hours accurate, including Saturdays, which matter for move-outs.</li>
</ul>
<p>Proximity still matters, so a hidden-address business tends to rank best near its verified base. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} explains how to widen that circle with reviews, service pages and links.</p>"""),

            ("Local Services Ads and Google Ads keywords", f"""<p>“Junk removal services” is on {SRC['lsa']}, so you can run pay-per-lead Local Services Ads above the regular results after Google’s screening. As with any LSA category, availability can vary by area, so start the sign-up with your address and see what comes back. Reviews and response time drive your LSA rank, so a company with 200 reviews and fast replies will usually beat a newer one regardless of budget.</p>
<p>Regular search ads let you control which jobs you pay for. Build ad groups by job type:</p>
<ul>
<li>Single items: “couch removal Houston,” “mattress disposal near me,” “refrigerator removal,” “hot tub removal Katy.”</li>
<li>Cleanouts: “garage cleanout The Woodlands,” “estate cleanout Houston,” “house cleanout service,” “hoarder cleanout” (only if you do it well and discreetly).</li>
<li>Move-outs and turnovers: “move out junk removal,” “apartment cleanout,” “tenant trash out.”</li>
<li>General: “junk removal near me,” “junk hauling Spring TX,” “same day junk removal.”</li>
</ul>
<p>Negatives matter a lot here, because “junk” attracts car buyers, scrap hunters and people looking for city pickup:</p>
<!--fig:negatives-->
<p>Sample ad: <i>Same-Day Junk Removal in Spring | Text Photos for a Price in 10 Min | Upfront Volume Pricing. Local, Insured Crew. We Donate and Recycle What We Can.</i> Track texts, calls and bookings as conversions, set by our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')}.</p>"""),

            ("Illegal dumping is your trust story", f"""<p>Houston has a real illegal dumping problem, and your customers know it. The city logged more than 8,200 illegal dumping service calls over 12 months, and the One Clean Houston program that paid for six inspectors and 120 cameras ran out of federal money, as {SRC['abc_dump']}. Harris County prosecutors filed 46 illegal dumping charges in 2025, and the city and county rely mostly on 150 to 200 mobile cameras to catch dumpers, per {SRC['axios_dump']}.</p>
<!--fig:dumping-->
<p>State law treats commercial dumping harshly. Under {SRC['hsc365']}, dumping for a commercial purpose becomes a Class A misdemeanor at more than five pounds and a state jail felony at 200 pounds or 200 cubic feet, lower thresholds than for an individual.</p>
<p>Nobody wants their mother’s old recliner to end up in a ditch in Acres Homes with their name on a piece of mail stuck in the cushion. So tell customers exactly where their stuff goes:</p>
<ul>
<li>A “Where your junk goes” page naming the types of facilities you use (landfill, transfer station, metal recycler, donation partners) and what share you typically divert, if you track it.</li>
<li>Disposal receipts available on request for larger jobs, especially for property managers and estate executors who need records.</li>
<li>Donation receipts passed along to the customer when items go to a charity.</li>
<li>Branded trucks and uniforms. An unmarked trailer is exactly what a nervous customer fears.</li>
</ul>
<p>Don’t accuse anyone. Just be the company that can prove where every load went.</p>
<p>And there’s a timing angle. Inside city limits, heavy trash is collected in even-numbered months, per {SRC['hou_heavy']}, and residents look up their week with the city’s HTX Collects tool. Someone moving out on the 3rd of an odd month isn’t waiting. “Can’t wait for heavy trash day?” is honest, local ad copy.</p>"""),

            ("Realtors, property managers and other referral partners", f"""<p>Ads find you one-off jobs. Partners send you the same kind of job every month, and these are the ones worth building:</p>
<ul>
<li><b>Listing agents.</b> Sellers have garages and attics full of stuff, and agents need it gone before photos. Offer a 48-hour listing-prep promise and invoice the seller or the agent directly. HAR’s agent community in your area is small enough to know by name. Our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how local agents market themselves')} shows their world.</li>
<li><b>Property managers and landlords.</b> Tenant move-outs and evictions leave furniture and trash that has to be gone before the make-ready crew arrives. Offer photo documentation before and after, net-30 invoicing and a priority slot. See our {L('/blog/property-management-company-marketing-houston/', 'property management marketing post')} for how those companies think.</li>
<li><b>Estate sale companies, probate attorneys and senior move managers.</b> They handle the hardest cleanouts and want a crew that’s respectful, careful with family items and fast. One good relationship can mean a job every few weeks.</li>
<li><b>Movers and house cleaners.</b> Movers get asked “can you take this to the dump?” on every job, and move-out cleaners can’t clean around a pile of junk. Cross-referrals work both ways. Our {L('/blog/moving-company-marketing-houston/', 'moving company post')} covers the movers’ side.</li>
</ul>
<p>Give every partner a one-page sheet with your pricing, how to book, and a direct text line. Then call them after the first job to ask how it went. Most independents never do that second call.</p>"""),

            ("Reviews that sell the next job", f"""<p>Junk removal reviews are unusually persuasive when they’re specific. “They took a sleeper sofa down three flights in 20 minutes” tells the next customer more than any ad.</p>
<p>Text the review link as the truck pulls away, with a before-and-after photo attached. A crew-lead script that works: “Thanks for having us. If we did a good job, a quick Google review really helps us. I just texted you the link.” Same link to every customer, no discounts in exchange, and a reply to every review. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>
<p>Estate cleanout customers deserve a softer ask, a few days later, by the person who ran the job. They’ve had a hard week.</p>"""),

            ("Cost per booked job: the only number that matters", f"""<p>Cost per lead flatters everything. Track cost per booked job by channel, and average ticket by channel, because a property manager referral and a single-mattress pickup aren’t the same customer.</p>
<!--fig:funnel-->
<p>Here’s how we’d phase the first 90 days for a one- to three-truck company. The spend ranges are illustrative examples, not quotes.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Phase</th><th>Work</th><th>Illustrative monthly spend</th></tr></thead>
<tbody>
<tr><td>Days 1 to 30</td><td>Business Profile cleanup, pricing page, text-a-photo quotes, online booking, review texts</td><td>$300 to $800 (setup and software)</td></tr>
<tr><td>Days 31 to 60</td><td>Google Ads by job type with full negatives, call and text tracking, LSA sign-up</td><td>$1,000 to $2,500 in ads</td></tr>
<tr><td>Days 61 to 90</td><td>Partner outreach to 20 agents, 10 property managers, 5 estate sale firms; cut ad groups with no bookings</td><td>Mostly time, plus printed partner sheets</td></tr>
</tbody></table></div>
<p>If your cost per booked job on ads is creeping past what a half-load earns you, the fix is usually the landing page, the response time or the negatives, not more budget. If you’d like a senior strategist to build that plan around your trucks and your area, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I get more junk removal jobs?",
             "Publish clear volume pricing and let customers text photos for a quote, then answer fast, because the first company to reply with a number usually wins. Set up your Google Business Profile as a service-area business with real photos and job-type services, run Google Ads by job type with strong negatives, and build referral relationships with realtors, property managers, estate sale companies and movers."),
            ("Are Google Local Services Ads available for junk removal?",
             "Yes. Junk removal services is one of the categories on Google’s Local Services Ads list, so junk removal companies can run pay-per-lead ads above the regular search results after Google’s screening. Availability can vary by location, so start the sign-up with your business address to check. Ranking leans heavily on reviews and how quickly you respond to leads."),
            ("Should a junk removal company show its address on Google?",
             "Only if customers come to that location. Google allows service-area businesses to hide their address and list up to 20 service areas instead, and suggests keeping the area within about two hours of driving from your base. Most junk removal companies run from a yard or home, so hiding the address and listing realistic nearby cities is the right setup."),
            ("What keywords should junk removal companies avoid in Google Ads?",
             "Add negatives for junk car searches (junk cars, cash for cars, junkyard), scrap metal prices, city heavy trash pickup and landfill hours, free donation pickup, dumpster rental if you don’t offer it, and job searches like hiring or salary. Then review the search terms report weekly for the first month. These searches can eat a large share of a small budget."),
            ("How can junk removal companies build trust with customers?",
             "Show customers where their items go. A page explaining your landfill, recycling and donation partners, disposal receipts for larger jobs, branded trucks and uniforms, and written price confirmation before loading all help. Houston has an ongoing illegal dumping problem, and commercial dumping carries heavier penalties under Texas law, so proving responsible disposal is a real advantage."),
        ],
        "figures": {
            "indie": {
                "type": "compare",
                "title": "Franchise strengths vs. independent edge",
                "left": {"title": "What franchises bring", "items": ["National name and big review counts", "Call center answers every time", "Online booking and set pricing", "Uniforms and branded trucks", "Scripted, consistent process"]},
                "right": {"title": "Where independents win", "items": ["Same-day slots when others are booked", "Price off photos in minutes", "Owner on the job", "Spanish-speaking crews where it matters", "Takes the odd jobs: hot tubs, sheds, pianos"]},
                "alt": "Comparison of junk removal franchise strengths and independent company advantages in Houston",
                "caption": "Match the franchises on booking and branding, then win on speed and flexibility.",
            },
            "booking": {
                "type": "steps",
                "title": "From photo to booked truck",
                "sub": "A booking flow that beats a callback",
                "steps": [["Text photos", "Customer texts photos from any page or ad."], ["Price range", "Reply with a volume-based range within minutes."], ["Book a window", "Online booking link with two-hour arrival windows."], ["Confirm on site", "Final price confirmed in writing before loading."], ["Review ask", "Before-and-after photo and review link by text."]],
                "alt": "Five-step junk removal booking flow for Houston customers from photo quote to booked job and review",
                "caption": "Every step is a text. That’s on purpose.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for junk removal ads",
                "sub": "Searches that look like customers and aren’t",
                "items": ["Cars: junk cars, cash for cars, junkyard, salvage yard", "Scrap: scrap metal prices, copper prices", "City service: heavy trash, bulk pickup schedule, landfill hours", "Donations: free furniture pickup, Salvation Army, Goodwill", "Dumpsters: dumpster rental, roll off (unless you offer it)", "Jobs: hiring, jobs, salary, driver", "DIY: how to dispose, trailer rental, dump near me", "Buying: used furniture for sale, free stuff"],
                "alt": "Checklist of negative keywords for junk removal Google Ads campaigns in Houston",
                "caption": "Then check search terms weekly for the first month.",
            },
            "dumping": {
                "type": "stats",
                "title": "Illegal dumping in Houston",
                "stats": [["8,200+", "dumping calls to the city in 12 months"], ["120", "city cameras bought by One Clean Houston"], ["46", "Harris County dumping charges in 2025"], ["200 lb", "commercial dumping becomes a state jail felony"]],
                "note": "Sources: ABC13, Axios Houston, Tex. Health & Safety Code 365.012",
                "alt": "Stats on illegal dumping enforcement in Houston and Harris County relevant to junk removal marketing",
                "caption": f"From {SRC['abc_dump']}, {SRC['axios_dump']} and {SRC['hsc365']}.",
            },
            "funnel": {
                "type": "funnel",
                "title": "One month of junk removal ads",
                "stages": [["Clicks", "600"], ["Calls, texts and forms", "75"], ["Quotes given", "60"], ["Booked jobs", "30"], ["Completed, paid jobs", "27"]],
                "note": "Illustrative example",
                "alt": "Funnel showing an illustrative month of junk removal Google Ads in Houston from clicks to paid jobs",
                "caption": "Divide ad spend by booked jobs, not leads. At $1,800 in spend, this month is $60 per booked job.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: insurance agency
    {
        "slug": "insurance-agency-marketing-houston",
        "title": "Insurance Agency Marketing in Houston: Growing an Independent P&C Book in a Hard Texas Market",
        "seo_title": "Insurance Agency Marketing in Houston for P&C Agents",
        "desc": "Insurance agency marketing for Houston independent P&C agents: TDI ad rules, Google Ads, Meta’s insurance ad limits, TCPA and lead buying, referral partners.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b6",
        "hero": "shield",
        "hero_alt": "Illustration of a shield for insurance agency marketing in Houston, The Woodlands, Katy and Kingwood",
        "related": ["real-estate-agent-marketing-the-woodlands-houston", "sms-marketing-small-business-texas-rules", "facebook-lead-ads-bad-leads-fix-quality"],
        "sections": [
            (None, f"""<p>Tuesday at an independent agency in Kingwood. One client forwards a renewal with a number she doesn’t believe. Another has a nonrenewal letter from a carrier that’s pulling back in Texas. A lender in Cypress needs a binder by Thursday for a Friday closing, and a lead vendor is calling about “exclusive home insurance leads” at a price that sounds too good.</p>
<p>That’s the week. Marketing has to work inside all of it.</p>
<p>Insurance agency marketing in Houston works when it puts you in front of homeowners at the exact moments they shop: a renewal shock, a nonrenewal, a home purchase, a flood scare. It has to stay inside Texas Department of Insurance advertising rules and federal telemarketing law, and it builds referral pipelines with the realtors and lenders who control the timing. Then you round out every account so one carrier’s rate filing doesn’t take your book with it.</p>
<p>This is written for independent property and casualty agencies with one to a few offices across Greater Houston.</p>"""),

            ("The Texas home insurance market you’re selling into", f"""<p>The last few years made home insurance a kitchen-table topic in Houston. The average Texas homeowners premium was $3,489 in 2025, up from $1,791 in 2016, and average rate changes ran 21.1% in 2023 and 18.7% in 2024 before slowing to 4.3% in 2025, according to {SRC['tdi_mkt']}. The three biggest groups, State Farm, Allstate and USAA, wrote about 47% of the market between them in 2024.</p>
<p>Carriers pulled back too. {SRC['ci_cyfair']} described Hippo nonrenewing a Cypress-area homebuilder’s policy despite no claims, noted USAA’s first loss in its 102-year history in 2022, and cited a Kinder Institute finding that more than 20% of Harris County housing units sit in major flood areas.</p>
<!--fig:market-->
<p>Now the market is shifting. Over the 90 days through October 2026, filed homeowners rate changes averaged a 4.0% decrease, per the same TDI page, and {SRC['cm_rates']} reported that filings since July 1, 2026 would cut rates for about 700,000 Texas homeowners policyholders.</p>
<p>For an independent agency, both halves of that story are marketing. Homeowners who got hit with two years of increases are still angry and still shopping. Homeowners whose captive carrier is now cutting rates may not hear about better options unless someone tells them. Your pitch, “we shop multiple carriers every renewal so you don’t have to,” has rarely been easier to explain.</p>"""),

            ("TWIA, flood and the coastal side of Houston", f"""<p>If you write in Clear Lake, League City, Seabrook, La Porte, Galveston or Brazoria County, windstorm coverage is part of nearly every conversation. The Texas Windstorm Insurance Association covers the 14 first-tier coastal counties, including Galveston, Brazoria and Chambers, plus parts of Harris County east of Highway 146 such as La Porte, Morgan’s Point, Pasadena, Seabrook and Shore Acres, per {SRC['twia']}. TWIA calls itself a residual insurer of last resort, applications go through a TDI-licensed agent, and applicable structures need a WPI-8 certificate of compliance.</p>
<p>That’s a content opportunity most agencies ignore. Pages like “TWIA windstorm insurance in League City: what you need” and “Do I need a WPI-8 to sell my house in Seabrook?” answer questions homeowners and realtors type into Google.</p>
<p>Flood is the cross-sell almost every Houston household needs and many don’t have. It typically takes 30 days for a new flood policy to go into effect, per {SRC['nfip']}, so the marketing window is before a storm is in the forecast. Send flood reminders in April and May, and again when the season’s first storm forms in the Gulf. “Your homeowners policy doesn’t cover flooding, and a new flood policy usually takes 30 days” is a message that works, as long as it’s accurate for each client.</p>"""),

            ("Texas Department of Insurance advertising rules, in plain terms", f"""<p>Insurance ads in Texas fall under 28 TAC Chapter 21, Subchapter B. Read the rule itself or ask your carriers’ compliance teams before anything goes live, but the main points, as summarized by {SRC['iiat_ads']}, are these:</p>
<ul>
<li>Every ad must identify who’s responsible for it, through the full licensed name, a registered assumed name or the agent’s Texas license number.</li>
<li>Ads must be truthful and not misleading in fact or implication, can’t make unfair or incomplete comparisons of policies or rates, and can’t disparage competitors.</li>
<li>An ad about a specific policy must state the insurer’s full licensed name, and an agent must file an ad that mentions an insurer or its policy with that insurer for approval before using it.</li>
<li>Testimonials must be genuine, reflect the author’s current opinion and apply to the advertised policy.</li>
<li>Online, required disclosures can sit behind a conspicuous, clearly labeled link next to the relevant information.</li>
</ul>
<p>Gifts and incentives are tightly limited. Promotional or educational items of $25 or less are allowed, per {SRC['iiat_reb']}, and anything bigger tied to buying insurance can become an illegal rebate.</p>
<!--fig:copy-->
<p>The practical takeaway: write about your service and process, which you control, rather than about price promises you can’t keep for every household.</p>"""),

            ("Google Ads for “home insurance quote” searches", f"""<p>Search is where shopping intent lives, and it isn’t cheap. WordStream’s 2025 benchmarks put the median Finance &amp; Insurance cost per click at $3.46 and cost per lead at $83.93, per {SRC['ws']}. That category blends banks, lenders and every kind of insurance, and in accounts we’ve run, home insurance quote terms in Houston often cost well above that blended figure. Expect to pay more for the click and to win on conversion rate.</p>
<p>Structure we’d use:</p>
<ul>
<li><b>Home by town:</b> “home insurance quote Katy,” “homeowners insurance The Woodlands,” “home insurance Pearland,” landing on a town page that mentions local issues (flood zones, MUD-heavy new construction, hail in Cypress).</li>
<li><b>Moment-of-need:</b> “home insurance non renewal Texas,” “dropped by home insurance,” “home insurance went up,” “new home insurance before closing.” These are often the best-converting ad groups.</li>
<li><b>Coastal and flood:</b> “TWIA agent League City,” “windstorm insurance Galveston,” “flood insurance quote Houston.”</li>
<li><b>Independent agent:</b> “independent insurance agent near me,” “insurance agency Spring TX,” “compare home insurance quotes.”</li>
<li><b>Bundles and specialty:</b> “home and auto insurance quote,” “landlord insurance Houston,” “umbrella insurance.”</li>
</ul>
<!--fig:negatives-->
<p>Two policy notes. Google’s personalized ad restrictions cover housing, employment and credit, and insurance isn’t on that list, per {SRC['gfaq']}, so you keep normal targeting. Carrier names are trademarks; bidding on them is a gray area and using them in ad text usually needs permission, which your appointment may or may not give. Ask the carrier.</p>
<p>Send calls to a licensed person during business hours and use a short quote form with a callback promise after hours. Our {L('/services/search-marketing/', 'search marketing team')} runs this setup, and our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give more local context.</p>"""),

            ("Meta ads: insurance is a special ad category now", f"""<p>A lot of agents still think the special ad category rules on Facebook and Instagram are only about credit. They aren’t. Meta’s Financial Products and Services category replaced the old Credit category and covers banking, investment and insurance ads as well as loans, according to {SRC['loomer']}. In the U.S., that means age locked to 18 to 65+, all genders, no ZIP code targeting, a minimum 15-mile radius around any location, limited detailed targeting with no exclusions, and no lookalike audiences.</p>
<p>So on Meta, the creative has to do the targeting. A stock photo of a smiling family and “Save on insurance!” reaches everyone and converts no one. What works better:</p>
<ul>
<li>A 30-second phone video of the agent saying “If your home insurance renewal jumped this year, bring it to us. We’ll shop it with several carriers and tell you honestly if you’re already in a good spot.”</li>
<li>Nonrenewal and new-homeowner messages, which self-select the right people.</li>
<li>Lead forms with a qualifying question or two (renewal date, ZIP, whether they own or rent) and a higher-intent setting. Fewer leads, better ones. Our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'guide to fixing bad Facebook leads')} goes into detail.</li>
<li>Retargeting website visitors and video viewers, which still works inside the category.</li>
</ul>
<p>Meta is a good place to build familiarity before renewal season. Search does the closing. If you’d rather hand this off, see our {L('/services/paid-social-advertising/', 'paid social service')}.</p>"""),

            ("Buying leads: TCPA consent and Texas telemarketing rules", f"""<p>Shared and “exclusive” internet leads are a big part of how many agencies grow, and the compliance ground moved recently.</p>
<p>The FCC’s one-to-one consent rule, which would have required a consumer’s consent to name a single seller, was vacated by the Eleventh Circuit in <i>Insurance Marketing Coalition v. FCC</i> just days before its January 27, 2025 effective date, along with the requirement that calls be “logically and topically” related to the original interaction, per {SRC['mofo']}. The FCC then formally removed the rule in 2025, per {SRC['goodwin']}. Prior express written consent is still required for autodialed or prerecorded marketing calls and texts, and the consent still has to clearly tell the consumer they may hear from the sellers in question.</p>
<p>Texas added its own layer. SB 140, effective September 1, 2025, brought marketing texts under the state’s telephone solicitation law, with a registration requirement and a private right of action, per {SRC['sb140']}. Persons licensed under the Texas Insurance Code are exempt from that registration, per {SRC['mondaq_tx']}, but the lead vendors and call centers working for you may not be. And the federal rules still apply to you either way.</p>
<!--fig:vendor-->
<p>Our view: the cheapest lead is usually the most expensive one once you count the agent time spent chasing people who don’t remember filling out a form. Lawsuits cost more than that. Ask your attorney before you buy, and read our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} before you text anyone.</p>"""),

            ("Realtors, mortgage lenders and builders: the referral engine", f"""<p>Every home purchase in Houston needs a policy before closing, which makes realtors, loan officers and title companies the best referral sources an agency has. They don’t care about your logo. They care whether you’ll get a binder to the lender on time and keep their closing from slipping.</p>
<ul>
<li><b>Make a closing promise.</b> “Quote within one business day, binder to the lender within 24 hours of approval.” Then keep it, every time.</li>
<li><b>Give them a dedicated line</b> that reaches a licensed person, plus a simple intake form they can send buyers.</li>
<li><b>Educate, don’t pitch.</b> A one-page “Insurance questions to ask before you buy in Houston” covering flood zones, roof age, WPI-8 on the coast and TWIA is something agents happily hand to clients. Keep it inside the advertising rules above.</li>
<li><b>Show up where they are.</b> HAR events, lender lunch-and-learns, builder sales offices in Bridgeland, Sienna or The Woodlands Hills.</li>
</ul>
<p>On paying for referrals, Texas generally allows a licensed agent to pay an unlicensed person a referral fee as long as the fee isn’t based on whether the customer buys insurance and the referrer doesn’t discuss specific policy terms, per {SRC['iiat_reb']}. Lenders and realtors have their own rules about what they can accept, so many agencies stick to reciprocal referrals and great service. Our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how local agents market themselves')} shows what they’re juggling.</p>"""),

            ("Google Business Profile, reviews and why LSA isn’t an option here", f"""<p>Local Services Ads might seem like an obvious fit, but Google lists the Insurance agency category as available in California and Florida only, per {SRC['lsa']}. Houston agencies have to win with the Business Profile, organic search and regular ads.</p>
<ul>
<li>Primary category <b>Insurance agency</b>, with secondary categories only for real specialties.</li>
<li>One profile per physical office with staff during posted hours. Don’t create profiles for home addresses or virtual offices.</li>
<li>Photos of the actual office and team. Insurance is a trust purchase, and faces help.</li>
<li>Services listed by line: home, auto, flood, windstorm, landlord, umbrella, commercial.</li>
</ul>
<p>Ask for reviews at two moments: right after a client binds a policy that saves them money or solves a nonrenewal, and after a claim goes well. Same link to everyone, no gift cards (that runs into both Google’s rules and Texas rebating limits), and reply to every review without discussing policy or claim details in public. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has request templates.</p>"""),

            ("Retention and cross-sell: rounding out the account", f"""<p>In a market where a carrier’s rate filing can move your whole book, the agencies that grow are the ones whose clients hold several policies with them. A household with home, auto, umbrella and flood is far harder to poach than a single auto policy.</p>
<!--fig:renewal-->
<ul>
<li>Track policies per household as a headline number, and set a target for it.</li>
<li>Run a renewal review 45 to 60 days before every home renewal, before the client gets the notice and starts shopping without you.</li>
<li>Run flood and umbrella campaigns to your own book. Your best prospects are already clients.</li>
<li>Send a short monthly email: storm prep, what changed in Texas rates, a claim story with names removed. Our {L('/blog/email-marketing-basics/', 'email marketing basics')} post covers getting started.</li>
</ul>
<p>Track new households, policies per household, retention rate and cost per bound policy by source. Lead counts are the least useful number you’ll see.</p>"""),

            ("A first 90 days for a Houston agency", f"""<p>Here’s a plan we’d use for a one-to-three-office independent agency. Spend ranges are illustrative.</p>
<ol>
<li><b>Days 1 to 30:</b> tighten the Business Profile, build town pages and moment-of-need pages (nonrenewal, new purchase, flood, TWIA), run the ad copy past your carriers, set up call tracking and a CRM source field.</li>
<li><b>Days 31 to 60:</b> launch Google Ads at roughly $2,000 to $5,000 a month across home-by-town and moment-of-need ad groups, start renewal reviews and flood campaigns to the existing book.</li>
<li><b>Days 61 to 90:</b> build a referral list of 25 realtors and 10 loan officers you’ll actually call on, test Meta video under the Financial Products and Services category, and decide on lead vendors only after checking their consent records.</li>
</ol>
<p>If you want a senior strategist to build that plan around your carriers, territory and staffing, <a href="/contact/">get in touch</a> and tell us what your book looks like today.</p>"""),
        ],
        "faq": [
            ("How do I get more home insurance clients in Houston?",
             "Show up where homeowners shop: Google searches for home insurance quotes by town, nonrenewal and new-purchase searches, and referrals from realtors and mortgage lenders who need binders before closing. Build pages for each of those moments, keep a strong Google Business Profile with steady reviews, and run renewal reviews for your own book. Rounding out accounts with flood, auto and umbrella keeps clients longer."),
            ("Are insurance ads a special ad category on Facebook?",
             "Yes. Meta’s Financial Products and Services special ad category replaced the old Credit category and includes insurance ads. In the U.S., age is locked to 18 to 65+, all genders are included, ZIP code targeting is unavailable, locations need at least a 15-mile radius, detailed targeting is limited and lookalike audiences are off. Specific creative and retargeting work best under these limits."),
            ("Can Houston insurance agencies use Google Local Services Ads?",
             "Not currently. Google lists the Insurance agency category for Local Services Ads as available in California and Florida only, so Texas agencies can’t run them. Houston agencies should focus on their Google Business Profile, reviews, local landing pages and regular Google search ads targeting home insurance quote and nonrenewal searches."),
            ("Is the FCC one-to-one consent rule in effect for insurance leads?",
             "No. The Eleventh Circuit vacated the FCC’s one-to-one consent rule in Insurance Marketing Coalition v. FCC in January 2025, days before it was set to take effect, and the FCC formally removed it later in 2025. Prior express written consent is still required for autodialed or prerecorded marketing calls and texts, and Texas SB 140 now covers marketing texts. Check with an attorney before buying leads."),
            ("What are the Texas insurance advertising rules for agents?",
             "Under 28 TAC Chapter 21, an ad must identify the responsible agent or agency by licensed name, registered assumed name or license number, be truthful and not misleading, avoid unfair comparisons and disparaging competitors, and name the insurer when promoting a specific policy. Agents must get insurer approval for ads that mention the insurer. Promotional gifts are limited to $25 or less."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "Texas home insurance, by the numbers",
                "stats": [["$3,489", "average Texas homeowners premium, 2025"], ["$1,791", "average premium in 2016"], ["18.7%", "average rate change in 2024"], ["-4.0%", "average filed change, Aug to Oct 2026"]],
                "note": "Source: Texas Department of Insurance",
                "alt": "Stats on Texas homeowners insurance premiums and rate changes for insurance agency marketing in Houston",
                "caption": f"From {SRC['tdi_mkt']}. Two years of big increases, now filings trending down.",
            },
            "copy": {
                "type": "compare",
                "title": "Insurance ad copy: risky vs. safer",
                "left": {"title": "Risky in Texas", "items": ["“Cheapest home insurance in Houston”", "“Save 40% guaranteed”", "“Better than State Farm”", "$100 gift card for a quote", "Ad naming a carrier, not approved"]},
                "right": {"title": "Safer and still persuasive", "items": ["“We shop several carriers every renewal”", "“See if you can save, no obligation”", "“Independent, so we work for you”", "Item worth $25 or less, or nothing", "Carrier-approved ad with full insurer name"]},
                "alt": "Comparison of risky and safer insurance ad copy under Texas advertising rules for Houston insurance agencies",
                "caption": "Sell your process, which you control. Run carrier-specific ads past the carrier first.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for P&C agency ads",
                "sub": "Searches that burn insurance budgets",
                "items": ["Existing customers: login, pay bill, claims number, customer service", "Careers: jobs, hiring, become an agent, licensing class", "Lines you don’t write: health, Medicare, life, dental", "Government: FEMA, disaster assistance, TDI complaint", "Free: free insurance, no money down", "Research: definition, what is, statistics", "Carrier brands you aren’t appointed with", "Car-only bargain hunters: $20 car insurance, no license"],
                "alt": "Checklist of negative keywords for independent insurance agency Google Ads campaigns in Houston",
                "caption": "Adjust the lines-you-don’t-write group to match your appointments.",
            },
            "vendor": {
                "type": "checklist",
                "title": "Ask every lead vendor before you buy",
                "sub": "Get answers in writing",
                "items": ["Can you show the exact consent language and page?", "Is each consent record stored with a timestamp and certificate?", "How many buyers receive the same lead?", "Do you or your call centers text or call for us?", "Are you registered in Texas if you text or call?", "What’s your return policy for bad or duplicate leads?", "Who handles do-not-call and opt-out requests?"],
                "alt": "Checklist of TCPA and Texas compliance questions for insurance agencies buying leads in Houston",
                "caption": "Not legal advice. Review vendor contracts with your attorney.",
            },
            "renewal": {
                "type": "steps",
                "title": "A renewal review that keeps the account",
                "sub": "Start before the client sees the notice",
                "steps": [["60 days out", "Pull the renewal and remarket if the change is large."], ["45 days out", "Call or email with options and a plain explanation."], ["Coverage check", "Roof age, flood, umbrella and auto gaps."], ["Decide together", "Stay, switch carriers or adjust deductibles."], ["Follow up", "Confirm in writing, then ask for a review."]],
                "alt": "Five-step insurance renewal review process for Houston independent agencies to retain and cross-sell clients",
                "caption": "The agency that calls first usually keeps the client.",
            },
        },
    },
]
