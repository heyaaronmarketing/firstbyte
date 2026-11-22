"""Batch 14: how to choose a digital marketing agency in The Woodlands and Houston, and marketing a business in
Katy and Cypress, TX.

Research (agency post): Clutch's 2026 digital marketing pricing guide (US agencies typically $100-$149/hour, typical
reviewed project $10,000-$49,999); Google Ads help on Google Partner requirements (70% optimization score, $10,000 spend
across managed accounts in 90 days, 50% of strategists certified; Premier = top 3% per country); Google Partners
directory; Clutch help center on review verification ("Not Verified" label); Morgan Lewis summary of the FTC consumer
reviews and testimonials rule (effective Oct. 21, 2024, up to $51,744 per violation); Texas Comptroller franchise tax
account status search; Google Ads help on account access levels (Admin manages users); Google Business Profile help on
owners and managers (managers can't add/remove users; 7-day wait for new owners). Pricing ranges kept consistent with
our existing cost posts and labeled as our experience.
Research (Katy/Cypress post): InnovationMap on Census Vintage 2025 county estimates (Harris +48,695 past 5 million,
No. 1 numeric gain; Fort Bend +24,163 to 975,191, No. 8; Waller +5.69% to 69,858, No. 2 percentage; Montgomery
781,194); Census QuickFacts for Fort Bend (18.3% growth since April 2020, 23.9% Asian, 25.4% Hispanic, 41.3% speak a
language other than English at home); Community Impact on TEA enrollment 2021-26 (Katy ISD +6,927); Texas Tribune
Schools Explorer (Cy-Fair ISD 114,697 students, 3rd largest of 1,202, 45.7% Hispanic); Community Impact on CFISD's
PASA study (91% built out, growth west near the Grand Parkway) and Katy ISD's Nov. 2025 demographic study (northwest
quadrant fastest); Katy ISD 2026-27 calendar via My Neighborhood News and CFISD 2026-27 calendar via Community Impact;
Houston Agent Magazine on RCLCO's 2025 top-selling MPCs (Sunterra No. 5, 1,024; Tamarron, Anniston, Elyson; Bridgeland
812); Community Impact on Bridgeland (11,500 acres, ~22,000 residents, 70,000 at build-out, Grand Parkway Segment E),
Towne Lake (300-acre lake, 14 miles of shoreline, ~3,000 homes, Caldwell), Cane Island (1,100 acres, city's first MPC);
Construction Dive on Elyson (3,600 acres, 6,200 homes, Newland); Community Impact on 2020 Census Asian population in
the Katy area; Asian Chamber of Commerce on KAT LunarFest at Katy Asian Town (22541 Grand Circle Blvd); Katy Rice
Harvest Festival (Rotary Club of Katy, Oct. 10-11, 2026); Light the Towne at The Boardwalk at Towne Lake; Lone Star
College Cy-Fest; Google Business Profile help on service areas (up to 20, about 2 hours' drive, no radius).
Competitor/PAA phrasing read for "how to choose a digital marketing agency", "marketing agency houston", "the woodlands
marketing agency", "katy marketing", "cypress tx marketing", "local seo katy tx", "advertising in cypress tx".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # agency post
    "clutch_price": A("https://www.clutch.co/agencies/digital-marketing/pricing", "Clutch’s 2026 digital marketing pricing guide"),
    "gpartner": A("https://support.google.com/google-ads/answer/9702452?hl=en", "Google’s Partner requirements"),
    "gdir": A("https://partnersdirectory.withgoogle.com", "Google Partners directory"),
    "clutch_verify": A("https://help.clutch.co/en/knowledge/how-clutch-verifies-reviews", "Clutch’s help center"),
    "ftc": A("https://www.morganlewis.com/pubs/2024/08/ftc-issues-final-rule-on-consumer-reviews-and-testimonials", "Morgan Lewis’s summary of the FTC rule"),
    "comptroller": A("https://comptroller.texas.gov/taxes/franchise/account-status/search", "Texas Comptroller’s franchise tax account status search"),
    "gads_access": A("https://support.google.com/google-ads/answer/9978556?hl=en-GB", "Google’s access level guide"),
    "gbp_roles": A("https://support.google.com/business/answer/3403100?hl=en-GB", "Google’s owners and managers page"),
    # katy / cypress post
    "im": A("https://houston.innovationmap.com/houston-metro-population-growth-2025-2676677221.html", "InnovationMap’s write-up of the Census estimates"),
    "qf": A("https://www.census.gov/quickfacts/fortbendcountytexas", "Census QuickFacts for Fort Bend County"),
    "ci_tea": A("https://communityimpact.com/new-caney-porter/education/data-most-greater-houston-area-school-districts-saw-enrollment-losses-from-2021-26/", "Community Impact’s look at TEA enrollment data"),
    "tt": A("https://schools.texastribune.org/districts/cypress-fairbanks-isd", "Texas Tribune’s Schools Explorer"),
    "ci_cfisd": A("https://communityimpact.com/cy-fair/education/demographic-shifts-expected-to-drive-cy-fair-isd-enrollment-down-by-2034/", "Community Impact"),
    "ci_kisd": A("https://communityimpact.com/houston/katy-fulshear/nonprofit/2025/11/26/katy-isd-demographic-study-shows-rezoning-may-be-needed-in-next-decade", "Katy ISD’s November 2025 demographic study"),
    "kcal": A("https://myneighborhoodnews.com/katy-isd-approves-october-fall-breaks-for-202627-and-202728-school-years-following-community-feedback", "Katy ISD’s approved 2026-27 calendar"),
    "cfcal": A("https://communityimpact.com/cypress/education/cy-fair-isd-students-staff-to-get-fall-break-in-2026/", "CFISD’s 2026-27 calendar"),
    "rclco": A("https://houstonagentmagazine.com/2026/01/08/sunterra-houstons-top-selling-mpc/", "Houston Agent Magazine’s summary of RCLCO’s 2025 rankings"),
    "bridgeland": A("https://communityimpact.com/cy-fair/development/residential-commercial-development-picks-up-in-bridgeland/", "Community Impact"),
    "townelake": A("https://communityimpact.com/cy-fair/photos-caldwell-companies-celebrates-the-completion-of-300-acre-lake-at-towne-lake/", "Community Impact"),
    "cane": A("https://communityimpact.com/katy-fulshear/news/cane-island-to-be-citys-first-master-planned-community/", "the city’s first master-planned community"),
    "elyson": A("https://www.constructiondive.com/news/newland-communities-3600-acre-elyson-development-set-to-open-near-houston/428102/", "Construction Dive"),
    "asian": A("https://communityimpact.com/katy/data-reference/katy-area-fort-bend-county-see-notable-increase-in-asian-population-data-shows/", "Community Impact’s read of the 2020 Census"),
    "lunar": A("https://asianchamber-hou.org/2026/01/28/kat-lunarfest-2026/", "KAT LunarFest"),
    "rice": A("https://myneighborhoodnews.com/lonestar-headlining-2026-katy-rice-harvest-festival-signals-major-year-for-community-tradition-in-historic-downtown-katy", "the Rotary Club of Katy"),
    "light": A("https://myneighborhoodnews.com/towne-lakes-10th-annual-light-the-towne-returns-november-19-with-santa-live-reindeer-and-40-foot-christmas-tree-lighting", "Light the Towne"),
    "cyfest": A("https://www.lonestar.edu/cy-fest", "Cy-Fest"),
    "gbp_sa": A("https://support.google.com/business/answer/9157481?hl=en", "Google’s service area rules"),
    "cfchamber": A("https://www.katyedc.org/about/economic-development-partners/p/item/22360/cyfair-houston-chamber-of-commerce", "Cy-Fair Houston Chamber of Commerce"),
}

AGENCY = "/blog/choose-digital-marketing-agency-the-woodlands-houston/"
KATY = "/blog/marketing-your-business-katy-cypress-tx/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: choosing an agency
    {
        "slug": "choose-digital-marketing-agency-the-woodlands-houston",
        "title": "How to Choose a Digital Marketing Agency in The Woodlands and Houston",
        "seo_title": "How to Choose a Marketing Agency in The Woodlands & Houston",
        "desc": "How to choose a digital marketing agency in The Woodlands or Houston: local vs. national, real pricing, proposals, proof you can verify and a scoring matrix.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Analytics"],
        "art": "b5",
        "hero": "scale",
        "hero_alt": "Illustration of a balance scale for choosing a digital marketing agency in The Woodlands and Houston",
        "related": ["questions-before-hiring-marketing-agency", "marketing-agency-contract-red-flags", "fractional-cmo-vs-agency-vs-in-house-houston"],
        "sections": [
            (None, f"""<p>Thursday afternoon, a conference room off Research Forest. Three proposals on the table. One from a downtown Houston agency with a beautiful deck and a $7,500 monthly retainer. One from a national firm whose rep flew in from somewhere colder, at $3,900 a month plus 15% of ad spend. One from a two-person shop in Spring for $1,800, sent as a Google Doc.</p>
<p>All three say “data-driven.” All three promise “transparent reporting.” None of them answers the owner’s real question, which is which one will still be worth paying in month nine.</p>
<p>This is how we’d choose a digital marketing agency in The Woodlands or anywhere in Greater Houston if we were sitting on your side of that table. We’re an agency in The Woodlands ourselves, so read it with that in mind. We’ve tried to write the version we’d hand a friend, including the parts where the honest answer is someone else.</p>"""),

            ("Before you call anyone, write a one-page brief", f"""<p>Most agency searches go wrong before the first call. The owner hasn’t decided what the agency is for, so every pitch gets judged on charm.</p>
<p>Write one page. It should say:</p>
<ul>
<li><b>The outcome you’re buying.</b> Booked jobs, consults, online orders, tickets. Pick the one number that pays your bills, and say what it is today if you know.</li>
<li><b>Budget, split in two.</b> What you can pay an agency each month, and what you can put into media (ad spend) on top. Owners who give one lump number get proposals that can’t be compared.</li>
<li><b>What’s running now</b>, and who holds the logins for the website, Google Ads, Google Business Profile, Meta and analytics.</li>
<li><b>Your capacity.</b> If 30 more calls a week would swamp your front desk in Kingwood, say so. An agency that hears that and plans around it is worth more than one that doesn’t ask.</li>
<li><b>Your calendar.</b> Hurricane season for a restoration company, August for a tutoring center, the rodeo weeks for a restaurant near NRG.</li>
</ul>
<p>Send the same brief to every agency. You’ll learn a lot from who reads it. If you’re still deciding whether an agency is even the right model, compared with a hire or a fractional CMO, our {L('/blog/fractional-cmo-vs-agency-vs-in-house-houston/', 'fractional CMO vs. agency vs. in-house breakdown')} covers that decision first.</p>"""),

            ("Local vs. national agencies: what proximity buys you in Houston", f"""<p>“Local” isn’t a virtue on its own. A Houston agency that runs your Google Ads from a template is no better than a template from Ohio. But proximity does buy some specific things, and it’s worth knowing which ones matter for your business.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Factor</th><th>Houston or The Woodlands agency</th><th>National agency</th></tr></thead>
<tbody>
<tr><td>Market knowledge</td><td>Knows Katy and Kingwood are about 50 miles apart and shop differently, and that a June storm changes everything for a week</td><td>Learns your market from your data and from you</td></tr>
<tr><td>Meetings</td><td>In person at your office, clinic or job site when it matters</td><td>Video calls, maybe a yearly visit</td></tr>
<tr><td>Field work</td><td>Photo and video shoots at your location without travel costs</td><td>Usually stock, user-generated content or a flown-in crew</td></tr>
<tr><td>Process</td><td>Ranges from excellent to “whatever the founder remembers”</td><td>Usually documented, with more specialists on staff</td></tr>
<tr><td>Minimums</td><td>Often lower retainers and spend minimums</td><td>Often higher, since their sales costs are higher</td></tr>
<tr><td>Who runs your account</td><td>At small shops, often a senior person or the founder</td><td>Often a coordinator, and turnover can be high</td></tr>
<tr><td>Best fit</td><td>Local service businesses, clinics, restaurants, multi-location brands within Houston, events</td><td>Ecommerce, national brands, one channel at large scale</td></tr>
</tbody></table></div>
<p>Where local pays off: local SEO and Google Business Profile work, where knowing that a Conroe plumber shouldn’t be bidding in Pearland saves real money. Shoot days. Billboards on I-45 and Houston radio, where relationships with local sellers help. Events. Anything that needs someone to drive over on a Tuesday.</p>
<p>Where it barely matters: an online store shipping to all 50 states, or a software company selling to buyers who’ve never been to Texas. For those, pick the best team for the channel and stop worrying about the ZIP code.</p>
<p>For what it’s worth, we run national brands from an office in The Woodlands. Geography alone doesn’t decide much. The people on your account decide nearly everything.</p>"""),

            ("Specialist or full-service?", f"""<p>A specialist does one channel deeply: Google Ads only, SEO only, paid social only. A full-service agency handles strategy across channels, plus creative and often the website.</p>
<!--fig:specialist-->
<p>Go specialist when one channel produces most of your revenue and someone on your team can coordinate the rest. A personal injury firm living on Google Ads, or a Shopify brand living on Meta, often does better with a team that does nothing else.</p>
<p>Go full-service when you have no marketing person and the channels depend on each other. Ads need landing pages. Landing pages need copy and photos. Somebody has to decide that the spring promotion runs on Instagram and in search at the same time with the same offer. Three specialists who never talk to each other will each blame the other two.</p>
<p>Two things to ask either kind. First, who does each piece of the work, and is any of it subcontracted? White-labeled SEO and offshore ad management are common, and they aren’t automatically bad, but you should know. Second, what will they tell you to stop doing? A specialist who says your SEO is the problem when your website is the problem isn’t helping.</p>"""),

            ("What agencies in Houston and The Woodlands typically charge", f"""<p>Pricing is where proposals are hardest to compare, so separate the pieces.</p>
<p>Nationally, {SRC['clutch_price']} puts typical U.S. agency rates at $100 to $149 an hour for services like PPC, SEO and social, with most reviewed projects falling between $10,000 and $49,999. That’s across the whole country, but Houston-area hourly rates we see sit in the same neighborhood.</p>
<!--fig:pricing-->
<p>The ranges below come from our experience: our own pricing, plus competing proposals that prospects in The Woodlands, Spring, Katy and inside the Loop have shown us. They aren’t a survey, and you’ll find quotes outside them in both directions.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Service</th><th>Monthly fee we commonly see</th><th>What pushes it up</th></tr></thead>
<tbody>
<tr><td>Google Ads management</td><td>$1,000 to $2,500 flat, or 10% to 20% of ad spend with a minimum</td><td>Number of campaigns and locations, landing pages included, call tracking</td></tr>
<tr><td>Local SEO, one location</td><td>$800 to $2,000</td><td>Competitive categories (law, HVAC, dental), content volume, multiple service areas</td></tr>
<tr><td>Paid social management</td><td>$1,000 to $3,000, plus creative</td><td>Video production, number of platforms, how often creative is refreshed</td></tr>
<tr><td>Multi-channel retainer, small business</td><td>$1,500 to $5,000</td><td>Channels covered, creative, meetings and reporting depth</td></tr>
<tr><td>Multi-channel program, growing brand</td><td>$5,000 to $20,000+</td><td>More channels, more markets, CTV and radio, larger creative needs</td></tr>
<tr><td>Website build (one-time)</td><td>$3,000 to $15,000, more for custom or ecommerce</td><td>Page count, service-area pages, bookings, payments</td></tr>
</tbody></table></div>
<p>Ask every agency to fill in the same four lines: management fee, recommended media, software or tool costs, and one-time setup. Then you’re comparing like with like. The $1,800 quote in the opening scene may become $3,100 once you add the call tracking and reporting software it quietly assumed you’d buy.</p>
<p>Very low prices deserve suspicion. A $299 SEO package is usually automated reports and little else. For the full cost picture, see our {L('/blog/digital-marketing-cost-the-woodlands-houston/', 'digital marketing cost guide for The Woodlands and Houston')}, and for how retainers, percentage-of-spend and pay-per-lead models compare, {L('/blog/marketing-agency-pricing-models-retainer-vs-percentage/', 'our pricing models post')} runs the math.</p>"""),

            ("How to read a proposal (and spot the copy-paste ones)", f"""<p>Read page one first. It should be about you. If the proposal could go to a dentist in Sugar Land and a roofer in Tomball with only the logo swapped, it probably did.</p>
<!--fig:proposal-->
<p>A good proposal usually comes after the agency asked for read-only access to your accounts. It tells you something about your own business you didn’t know: that 40% of your Google Ads budget goes to searches for jobs at your company, say, or that your Business Profile lists the wrong primary category. That one finding is worth more than ten pages of capabilities.</p>
<p>Look for a first 90 days written in weeks, not adjectives. “Weeks 1 and 2: rebuild conversion tracking for calls and forms. Weeks 3 to 6: restructure search campaigns by service line.” If the plan is “optimize, refine, scale,” you’ve learned nothing.</p>
<p>Check that the KPIs match your brief. You asked for booked jobs. If the proposal promises impressions, reach and “engagement,” it’s measuring the agency’s activity instead of your result. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'guide to tracking calls and form fills')} shows what real conversion tracking includes, so you can tell whether a proposal plans for it.</p>
<p>For the questions to ask in the meeting itself, our {L('/blog/questions-before-hiring-marketing-agency/', 'questions to ask before hiring an agency')} list is short and worth printing.</p>"""),

            ("Case studies you can actually verify", f"""<p>“Client in home services: +312% leads.” Every agency has slides like that. Most can’t be checked, and the ones that can’t be checked are the ones to discount.</p>
<p>When you see a result, ask four things. Whose account was it? What was the period? What was the baseline? And what else changed at the same time, such as a new location, a price cut, or a storm that sent every restoration company’s calls through the roof for a month?</p>
<!--fig:verify-->
<p>Some notes on each step.</p>
<p><b>Partner badges</b> tell you less than they look like they do. Under {SRC['gpartner']}, a Google Partner needs a 70% optimization score, $10,000 in ad spend across managed accounts over 90 days, and at least half its account strategists certified. Premier Partners are roughly the top 3% of partners in their country. You can confirm a badge in the {SRC['gdir']}. The badge proves a minimum level of activity and housekeeping. It doesn’t prove anyone made a client money.</p>
<p><b>Third-party reviews</b> help if you know how they’re checked. Per {SRC['clutch_verify']}, Clutch confirms each reviewer’s identity and work history, and publishes reviews it can’t confirm with a “Not Verified” label. Read those labels.</p>
<p><b>Testimonials</b> now carry legal weight. The FTC’s rule on consumer reviews and testimonials, effective October 21, 2024, bans fake testimonials and undisclosed insider reviews, with civil penalties up to $51,744 per violation, per {SRC['ftc']}. That doesn’t make every testimonial true. It does mean an agency that won’t put a name on its praise is telling you something.</p>
<p><b>The company itself.</b> For a Texas agency, the {SRC['comptroller']} lets you look up the business by name or Secretary of State file number. Takes two minutes. You’d be surprised how often the “agency” is a sole proprietor with a nice website, which is fine if they’re upfront about it.</p>
<p>The best proof is a live account. Ask the agency to screen-share a current client’s Google Ads or Meta account, with that client’s permission, and walk you through the last 90 days. Good agencies have a client or two happy to allow it. Our own {L('/case-studies/', 'case studies')} name the clients, and you should hold us to the same standard you hold anyone else.</p>"""),

            ("Is meeting in person worth the drive?", f"""<p>In Houston, “local” can mean 45 minutes on I-45 at 5 p.m. So the point of a local agency isn’t a weekly coffee. It’s being able to meet when it matters: kickoff, the quarterly review, a shoot day at your location, the week something breaks.</p>
<p>If you do meet, use the time well.</p>
<ul>
<li>Insist that the person who will run your account day to day is in the room. Not only the founder, and not only the salesperson.</li>
<li>Give them read-only access beforehand and ask them to open your Google Ads or Meta account on the screen and talk through what they see. Ten minutes of that beats an hour of slides.</li>
<li>Ask what they’d stop doing in week one. Strong practitioners always have an answer.</li>
<li>Watch who answers the technical questions. If the salesperson fields every one, you’ve met the pitch. You haven’t met the work.</li>
</ul>
<p>National agencies can pass the same test over video. The format matters less than whether the doer shows up.</p>"""),

            ("Contracts and account ownership: settle three things before you sign", f"""<p>We’ve written a whole post on {L('/blog/marketing-agency-contract-red-flags/', 'marketing agency contract red flags')}, so here are only the three that decide whether you can leave cleanly.</p>
<ol>
<li><b>Term and exit.</b> Know the minimum term, the notice period and whether it auto-renews. A short initial term followed by month-to-month with 30 days’ notice is common and fair for ongoing management.</li>
<li><b>Who owns the accounts.</b> Your Google Ads account should be in your name with you as an Admin; per {SRC['gads_access']}, Admin is the level that can add and remove users, while Standard can edit campaigns but can’t manage access. On your Google Business Profile, you should be the primary owner and the agency a manager. {SRC['gbp_roles']} says managers can’t add or remove users or delete the profile, and that new owners must wait seven days before removing other owners. Same idea for your Meta business portfolio, your domain registrant and your analytics.</li>
<li><b>What leaves with you.</b> Creative, landing pages, keyword research, call recordings and reporting data. Get it in writing.</li>
</ol>
<p>If you already have an agency and aren’t sure who owns what, our {L('/blog/who-owns-google-ads-account-switch-agencies/', 'guide to account ownership and switching agencies')} goes asset by asset.</p>"""),

            ("A scoring matrix for comparing agencies", f"""<p>Gut feel picks the best presenter. A matrix makes you write down why. Score each agency 1 to 5 on each line, multiply by the weight, and add it up. Have one colleague score separately, then compare notes before you talk numbers.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Criterion</th><th>Weight</th><th>What a 5 looks like</th><th>What a 1 looks like</th></tr></thead>
<tbody>
<tr><td>Understood our business</td><td>20%</td><td>Restated our brief accurately and found something in our accounts we didn’t know</td><td>Generic capabilities deck</td></tr>
<tr><td>The people doing the work</td><td>20%</td><td>We met the account lead, know their experience and how many accounts they carry</td><td>“A dedicated team” with no names</td></tr>
<tr><td>Proof we could verify</td><td>15%</td><td>Named references we called and a live account walkthrough</td><td>Unnamed percentages only</td></tr>
<tr><td>Channel fit</td><td>15%</td><td>Specialist or full-service matches our brief, no hidden subcontracting</td><td>Pitched services we didn’t ask for and can’t use</td></tr>
<tr><td>Measurement plan</td><td>15%</td><td>KPIs tied to our revenue number, tracking setup in the first month</td><td>Impressions, reach and “engagement”</td></tr>
<tr><td>Terms and ownership</td><td>10%</td><td>We own every account, fair notice period, assets transfer on exit</td><td>Agency-owned accounts, long lock-in</td></tr>
<tr><td>Price clarity</td><td>5%</td><td>Fee, media, tools and setup on separate lines</td><td>One bundled number</td></tr>
</tbody></table></div>
<p>Price gets only 5% on purpose. Your budget already filtered out the agencies you can’t afford. Among the ones you can, clarity matters more than a few hundred dollars a month. A cheap agency that wastes $2,000 of ad spend is the expensive one.</p>
<!--fig:scores-->
<p>Most searches look something like the funnel below. Four to six weeks is normal. Longer usually means nobody owns the decision.</p>
<!--fig:process-->"""),

            ("Making the call", f"""<p>Before you sign, call two references, and ask them three things. What went wrong, and how did the agency handle it? Who actually works on your account now, and is it the same person as at the start? Would you hire them again at the same price?</p>
<p>Then put a 90-day review on the calendar the day you sign. Pull out the one-page brief and the proposal, and check one against the other: did the tracking get fixed, did the plan happen, and is the number you care about moving? If not, our list of {L('/blog/signs-your-marketing-agency-isnt-working/', 'signs your marketing agency isn’t working')} will help you have that conversation.</p>
<p>If you’d like First Byte to be one of the proposals on your table, tell us about your business and goals and a senior strategist will build a custom plan around them. You can <a href="/contact/">get in touch</a> here.</p>"""),
        ],
        "faq": [
            ("How do I choose a digital marketing agency in The Woodlands or Houston?",
             "Start with a one-page brief: the outcome you want, your fee and ad budgets, what’s running now and who holds the logins. Send it to three or four agencies. Compare proposals on whether they understood your business, who will do the work, proof you can verify, the measurement plan and contract terms. Meet the person who will run your account, and call two references before signing."),
            ("How much does a marketing agency cost in Houston?",
             "In our experience, Google Ads management runs about $1,000 to $2,500 a month or 10% to 20% of ad spend, local SEO for one location about $800 to $2,000 a month, and small-business multi-channel retainers about $1,500 to $5,000 a month. Ad spend is extra. Clutch’s 2026 guide puts typical U.S. agency rates at $100 to $149 an hour. Ask every agency to separate fees, media, tools and setup."),
            ("Is it better to hire a local marketing agency or a national one?",
             "It depends on the work. A Houston or The Woodlands agency helps most for local SEO, Google Business Profile, shoots at your location, billboards, radio and events, and it usually has lower minimums. National agencies often have deeper benches and documented processes, which suits ecommerce and national brands. In both cases, the people running your account matter far more than where the office is."),
            ("How can I verify a marketing agency’s case studies?",
             "Ask whose account it was, the period, the baseline and what else changed. Request a named reference and a screen-share of a live client account with that client’s permission. Confirm Google Partner status in Google’s Partners directory, read third-party reviews and check their verification labels, and look up a Texas agency in the Comptroller’s franchise tax account status search."),
            ("Who should own my Google Ads and Google Business Profile accounts?",
             "You should. Your Google Ads account should be in your business’s name with you as an Admin, since Admin is the access level that can add and remove users. On Google Business Profile, you should be the primary owner and the agency a manager, which lets them work on the profile without adding or removing users or deleting it. Apply the same rule to Meta, analytics and your domain."),
        ],
        "figures": {
            "specialist": {
                "type": "compare",
                "title": "Specialist or full-service agency?",
                "left": {"title": "Specialist fits when", "items": ["One channel drives most revenue", "You have someone to coordinate", "The channel is complex (PPC, Amazon)", "You want depth over breadth", "Your website and brand are already solid"]},
                "right": {"title": "Full-service fits when", "items": ["No one in-house owns marketing", "Ads depend on new pages and creative", "Offers must line up across channels", "You want one set of numbers", "Brand, site and ads all need work"]},
                "alt": "Comparison of when to choose a specialist or full-service digital marketing agency in The Woodlands and Houston",
                "caption": "Either way, ask who does each piece and whether any of it is subcontracted.",
            },
            "pricing": {
                "type": "stats",
                "title": "Agency pricing, in four numbers",
                "stats": [["$100-149", "typical U.S. agency hourly rate"], ["$10K-50K", "typical reviewed project size"], ["10-20%", "common percentage-of-spend fee"], ["4 lines", "fee, media, tools, setup"]],
                "note": "Source: Clutch 2026 pricing guide (first two); our experience (last two)",
                "alt": "Stats on digital marketing agency pricing for businesses in Houston and The Woodlands, including hourly rates",
                "caption": f"Hourly and project figures from {SRC['clutch_price']}. Ask every agency to price the same four lines.",
            },
            "proposal": {
                "type": "checklist",
                "title": "What a good agency proposal includes",
                "sub": "Check each one before you compare prices",
                "items": ["Your brief restated in their words", "Findings from your actual accounts", "First 90 days, week by week", "Named people and their roles", "KPIs tied to your revenue number", "Tracking setup in month one", "What they need from you", "What’s excluded, in writing"],
                "alt": "Checklist of what a good digital marketing agency proposal should include for a Houston or The Woodlands business",
                "caption": "If page one isn’t about your business, the rest probably isn’t either.",
            },
            "verify": {
                "type": "steps",
                "title": "Five ways to verify an agency’s results",
                "sub": "Before you trust the case study slide",
                "steps": [["Named reference", "A client you can call, not a quote on a slide."], ["Live account", "Screen-share of a real account, last 90 days."], ["Partner directory", "Confirm Google Partner status yourself."], ["Verified reviews", "Read third-party reviews and their labels."], ["Entity lookup", "Check the company in the Texas Comptroller search."]],
                "alt": "Five steps to verify a digital marketing agency's case studies and claims in Houston and The Woodlands",
                "caption": "A good agency will be glad you asked. A defensive one has told you what you need to know.",
            },
            "scores": {
                "type": "columns",
                "title": "Weighted scores for three agencies",
                "sub": "Total score as a percent of the maximum, using the matrix above",
                "labels": ["Agency A", "Agency B", "Agency C"],
                "values": [58, 82, 71],
                "highlight": [1],
                "y_label": "Score",
                "note": "Illustrative example",
                "alt": "Illustrative column chart of weighted scores comparing three digital marketing agencies for a business in The Woodlands",
                "caption": "Agency B won on people and proof, not price. That’s usually how it goes.",
            },
            "process": {
                "type": "funnel",
                "title": "A typical agency search",
                "stages": [["Long list from referrals and search", "8 names"], ["Discovery calls with the brief", "4 calls"], ["Written proposals", "3 proposals"], ["Working sessions with account leads", "2 meetings"], ["Signed agreement", "1 agency"]],
                "note": "Illustrative example, four to six weeks",
                "alt": "Funnel of a typical process for choosing a digital marketing agency in Houston and The Woodlands, from long list to signing",
                "caption": "Fewer than three proposals and you can’t compare. More than four and you stop reading them closely.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: Katy and Cypress
    {
        "slug": "marketing-your-business-katy-cypress-tx",
        "title": "Marketing Your Business in Katy and Cypress, TX: A Local Playbook",
        "seo_title": "Marketing Your Business in Katy & Cypress, TX",
        "desc": "Marketing a business in Katy and Cypress, TX: growth data, master-planned communities, commutes, school calendars, local SEO, Facebook groups and events.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Facebook", "Google"],
        "art": "b4",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for marketing a business in Katy and Cypress, TX, west of Houston",
        "related": ["marketing-your-business-spring-tx", "reaching-customers-conroe-montgomery", "multi-location-local-seo-houston-franchises"],
        "sections": [
            (None, f"""<p>Saturday, 7:52 a.m. Someone in a Bridgeland neighborhood Facebook group posts: “Our AC died overnight. Who do you all use? Need someone today.” By 8:30 there are 41 comments. Two companies get named over and over. One of them answers the post itself, with a first name and a phone number. That one gets the job.</p>
<p>Marketing a business in Katy and Cypress works a lot like that thread. The area is huge and still growing, but people buy inside small circles: their master-planned community, their school zone, their side of the Grand Parkway, the groups and events they already belong to.</p>
<p>We work out of The Woodlands, on the other side of the Grand Parkway, and the pattern is the same up here, but the details aren’t. This playbook covers what’s specific to Katy and Cypress, west and northwest of Houston: the growth numbers, the communities, the commutes, the school calendars, local SEO across multiple service areas, community groups, language, events and chambers. If you also serve the north side, we’ve written separate notes on {L('/blog/marketing-your-business-spring-tx/', 'marketing in Spring')} and {L('/blog/reaching-customers-conroe-montgomery/', 'reaching customers in Conroe and Montgomery County')}, so we won’t repeat them here.</p>"""),

            ("How fast Katy and Cypress are growing", f"""<p>Katy sits across three counties: Harris, Fort Bend and Waller. Cypress and the wider Cy-Fair area are unincorporated Harris County. All three counties are growing quickly.</p>
<!--fig:growth-->
<p>Census Bureau estimates for July 2024 to July 2025, as reported in {SRC['im']}: Harris County added 48,695 residents and passed 5 million, the largest numeric gain of any U.S. county. Fort Bend added 24,163 to reach 975,191, eighth in the nation by numeric growth. Waller County grew 5.69% to 69,858, second among U.S. counties by percentage. {SRC['qf']} puts Fort Bend’s growth since April 2020 at 18.3%.</p>
<p>The schools tell the same story. Katy ISD gained 6,927 students from 2021 to 2026, third in the Houston area for total gains, per {SRC['ci_tea']}. Cy-Fair ISD is the third-largest district in Texas with 114,697 students, according to {SRC['tt']}.</p>
<p>The growth isn’t even, though. Cy-Fair ISD was about 91% built out as of 2025, with most remaining growth on the western edge near the Grand Parkway, per {SRC['ci_cfisd']}. In Katy ISD, {SRC['ci_kisd']} found the northwest quadrant growing fastest, around Elyson, Anniston, Bridgeland and Sunterra. Older parts of both districts are flat or shrinking.</p>
<p>For marketing, that means two different jobs. In the newer areas, households are choosing a dentist, a pediatrician, a lawn service and a favorite Tex-Mex place for the first time, and the first business they find often keeps them for years. In the established areas around Cinco Ranch, Copperfield or Jersey Village, you’re mostly persuading people to switch, which takes reviews and a reason.</p>"""),

            ("Master-planned communities are their own markets", f"""<p>A family in Elyson doesn’t say they live in Katy. They say they live in Elyson. That identity shapes where they look for recommendations, which events they go to and what they type into Google.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Community</th><th>What we could verify</th><th>Marketing angle</th></tr></thead>
<tbody>
<tr><td>Cinco Ranch (Katy)</td><td>Long-established community south of I-10, home to LaCenterra</td><td>Mature households; switching offers, reviews from neighbors</td></tr>
<tr><td>Cane Island (Katy)</td><td>About 1,100 acres; {SRC['cane']} inside the city of Katy</td><td>Close to downtown Katy; tie in Rice Harvest Festival timing</td></tr>
<tr><td>Elyson (Katy)</td><td>3,600 acres and about 6,200 homes planned by Newland, per {SRC['elyson']}; No. 41 nationally in 2025 with 413 sales</td><td>Steady stream of first-year homeowners</td></tr>
<tr><td>Sunterra (Katy)</td><td>No. 5 nationally in 2025 with 1,024 sales, per RCLCO</td><td>Newest buyers in the area; move-in services, first appointments</td></tr>
<tr><td>Bridgeland (Cypress)</td><td>11,500 acres, about 22,000 residents in 2024 and 70,000 expected at build-out; Grand Parkway Segment E runs through it, per {SRC['bridgeland']}</td><td>Large, still filling in; community group activity is high</td></tr>
<tr><td>Towne Lake (Cypress)</td><td>A roughly 300-acre lake with 14 miles of shoreline and about 3,000 homes planned, by Caldwell Companies, per {SRC['townelake']}</td><td>The Boardwalk is a natural venue for events and sponsorships</td></tr>
</tbody></table></div>
<p>RCLCO’s 2025 list of the nation’s top-selling master-planned communities, per {SRC['rclco']}, also included Tamarron (No. 9) and Anniston (No. 12) in Katy, plus Bridgeland at 812 sales. The west side is selling homes at a pace few markets in the country match.</p>
<p>What to do with that:</p>
<ul>
<li>Use community names in your copy and on your service pages where you genuinely serve them. “Lawn care in Elyson and Cane Island” matches how people search and how they talk.</li>
<li>Bid on community names plus your service in Google Ads (“Bridgeland dentist,” “Towne Lake pool service”). Volumes are small and the intent is strong.</li>
<li>Ask about advertising in community newsletters, magazines and event sponsorships through the developer or HOA. Rules vary a lot by community, so ask before you print anything.</li>
<li>Time new-homeowner offers to the building pace. A neighborhood that closed 80 homes last quarter needs blinds, fences, pest control and a dentist this quarter.</li>
</ul>"""),

            ("Commuters: I-10, US-290 and the Grand Parkway", f"""<p>A lot of Katy and Cypress works somewhere else. Katy households commute east on I-10 toward the Energy Corridor, the Galleria and downtown. Cypress households take US-290 into the city or the Grand Parkway north and south between the two. The Grand Parkway (SH 99) connects them directly, and it’s why a Katy business can now realistically pull customers from Bridgeland.</p>
<!--fig:map-->
<p>What commute patterns change in your marketing:</p>
<ul>
<li><b>Target where people live.</b> In Google Ads, use “Presence: people in or regularly in your locations” and draw locations around homes. Weekday daytime traffic to your site might be people at their desks in the Energy Corridor, but they’ll buy near home.</li>
<li><b>Schedule around the drive.</b> In accounts we’ve run, calls to service businesses here cluster early in the morning and after people get home. Make sure someone answers then. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} explains why the first callback wins.</li>
<li><b>Use the drive.</b> Streaming audio and radio reach commuters on 290 and I-10 in the car, and billboards along the Grand Parkway reach the same people every day. Both work better as reminders than as the whole plan.</li>
<li><b>Say which side you serve.</b> “Same-day service north of I-10” or “Cypress side of the Grand Parkway” removes doubt. Nobody in Fulshear wants to wait on a tech coming from Jersey Village at rush hour.</li>
</ul>"""),

            ("Katy ISD and Cy-Fair ISD calendars run your season", f"""<p>Family-heavy suburbs plan their lives around the school calendar. Restaurants, tutors, camps, orthodontists, pediatric dentists, gyms and home services all see the effects. And Katy ISD and Cy-Fair ISD don’t share the same breaks.</p>
<div class="bp-tbl"><table>
<thead><tr><th>2026-27 date</th><th>Katy ISD</th><th>Cy-Fair ISD</th></tr></thead>
<tbody>
<tr><td>First day of school</td><td>Aug. 12, 2026</td><td>Aug. 12, 2026</td></tr>
<tr><td>Fall break</td><td>Oct. 9-13, 2026</td><td>Oct. 12-16, 2026</td></tr>
<tr><td>Spring break</td><td>March 8-12, 2027</td><td>March 15-19, 2027</td></tr>
<tr><td>Last day of school</td><td>May 26, 2027</td><td>May 27, 2027</td></tr>
</tbody></table></div>
<p>Dates from {SRC['kcal']} and {SRC['cfcal']}. CFISD also has Thanksgiving week off (Nov. 23-27) and winter break from Dec. 21 to Jan. 1.</p>
<p>Notice that spring breaks are a week apart. A camp, family entertainment center or kids’ dentist serving both districts gets two spring breaks, so run two campaigns with two date ranges and two audiences. The same applies to fall break, which is new for CFISD this year.</p>
<p>A rough calendar we’d use:</p>
<ul>
<li>Three to four weeks before a break: promote camps, family dining deals, appointment openings for kids out of school.</li>
<li>During a break: daytime ad scheduling shifts, since parents are home and searching midday.</li>
<li>Late July: back-to-school (physicals, haircuts, tutoring, uniforms, carpool-friendly hours). Our {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing post')} has more.</li>
<li>Late April into May: graduation, summer camps, pool openings and summer HVAC.</li>
</ul>
<p>Check each district’s official calendar before you lock in ads, since bad weather days can shift dates. Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing calendar')} covers the rest of the year.</p>"""),

            ("Local SEO when you serve Katy, Cypress and everything between", f"""<p>Most businesses here serve more than one town. A plumber in Cypress takes calls from Tomball, Jersey Village and Bridgeland. A Katy med spa draws from Fulshear and Brookshire. Google needs to understand all of that.</p>
<p>Start with your Business Profile. Under {SRC['gbp_sa']}, you can list up to 20 service areas, by city or ZIP code, and the whole area shouldn’t extend beyond about two hours’ drive from your base. A radius isn’t allowed. If customers don’t visit you, hide your address. Pick the areas you really serve. Listing all 20 doesn’t make you rank in all 20; the map pack still leans heavily on how close you are to the searcher.</p>
<p>Then build one real page for each main area on your site. A Katy page should mention Katy things: the ZIPs you cover (77449, 77450, 77493, 77494), the communities, how fast you get there, photos of jobs done there, and reviews from customers there. A Cypress page covers 77429 and 77433, Bridgeland, Towne Lake, Fairfield. If your Katy and Cypress pages are the same text with the town name swapped, Google will treat them as thin, and so will customers.</p>
<!--fig:pages-->
<p>Ask for reviews that mention where you worked. Don’t script them, and don’t offer anything in exchange, but customers often add their neighborhood on their own if you ask them to describe the job. For a deeper treatment, see our {L('/blog/rank-in-google-map-pack-houston/', 'Houston map pack guide')}, {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} and, if you have more than one office, {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO')}.</p>"""),

            ("Facebook community groups: how to show up without getting kicked out", f"""<p>Neighborhood Facebook groups in Katy and Cypress can be the busiest recommendation engines in the area. Every master-planned community has a few, plus groups for moms, newcomers, school zones and buy-sell-trade. They’re also run by volunteer admins who ban businesses for posting ads.</p>
<!--fig:groups-->
<p>The pattern that works: the owner, or one senior person, joins with a personal profile, follows the rules, and answers questions helpfully even when there’s no sale in it. When a “who do you use?” thread comes up, you respond once, with your name and how to reach you. You don’t copy-paste a flyer. Happy customers tagging you does more than anything you post yourself.</p>
<p>Many groups allow business posts on one day a week, or sell sponsorships. Ask the admin. A few hundred dollars to sponsor a community group for a quarter can beat the same amount on ads, because the audience is exactly your neighborhood. Nextdoor works similarly in some neighborhoods; our {L('/blog/is-nextdoor-advertising-worth-it/', 'Nextdoor advertising review')} covers whether the paid side pays off.</p>
<p>Paid Facebook and Instagram ads still matter. Target by city or a radius around your service area, use real photos from local jobs, and name the community in the copy. “We just finished three backyards in Towne Lake this month” stops a scroll. Our {L('/services/paid-social-advertising/', 'paid social team')} runs this kind of campaign.</p>"""),

            ("Asian and Hispanic communities, and the language question", f"""<p>Katy and Cypress are among the most diverse suburbs in Texas. In Fort Bend County, 23.9% of residents are Asian and 25.4% are Hispanic, and 41.3% of people over age five speak a language other than English at home, per {SRC['qf']}. Cy-Fair ISD’s students are 45.7% Hispanic, per {SRC['tt']}. In the 2020 Census, Asian residents made up more than 20% of some parts of the Katy area south of the Katy Freeway and west of the Grand Parkway, per {SRC['asian']}.</p>
<p>Katy Asian Town, on Grand Circle Boulevard in the 77449 ZIP, anchors much of that community’s shopping and dining, and hosts events such as {SRC['lunar']}, which ran Feb. 14-15, 2026.</p>
<p>Practical advice, without stereotypes:</p>
<ul>
<li><b>Ask your customers.</b> Your intake form or point-of-sale can ask what language a customer prefers. That beats guessing from a ZIP code, and it tells you whether Spanish, Mandarin, Vietnamese, Hindi, Korean or something else is worth the investment for you.</li>
<li><b>Only advertise in a language you can answer the phone in.</b> A Spanish ad that reaches an English-only voicemail is worse than no ad.</li>
<li><b>Write it, don’t translate it.</b> Native speakers should write ad copy and landing pages. Literal translations read as foreign, and people notice.</li>
<li><b>Show up where the community already gathers.</b> Lunar New Year and Diwali events, cultural associations, community centers, language-specific social media groups and local publications.</li>
</ul>
<p>For Spanish-language search and social campaigns specifically, our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing in Houston guide')} goes through bilingual SEO, Google Ads language settings and Spanish radio.</p>"""),

            ("Local events and chambers in Katy and Cypress", f"""<p>Events here are big, family-focused and mostly free to attend, which makes them good for awareness and terrible for direct response unless you plan the follow-up.</p>
<ul>
<li><b>Katy Rice Harvest Festival.</b> Run by {SRC['rice']} in Historic Downtown Katy every October, with proceeds going to scholarships and community grants. This year’s festival ran Oct. 10-11, 2026.</li>
<li><b>Light the Towne.</b> The Boardwalk at Towne Lake held its 10th annual free holiday tree lighting, {SRC['light']}, on Nov. 19, 2026, with booths from local businesses along Candy Cane Lane.</li>
<li><b>Cy-Fest.</b> A free fall festival at Lone Star College-CyFair. {SRC['cyfest']} lists the next one for Saturday, Oct. 2, 2027.</li>
<li><b>KAT LunarFest</b> at Katy Asian Town around Lunar New Year.</li>
</ul>
<!--fig:events-->
<p>For a booth or sponsorship to pay off, bring a way to capture names (a drawing, a QR code to a booking page), staff it with people who can answer real questions, and follow up within a week while the event is fresh. Track it with a dedicated URL or offer code so you know what it produced.</p>
<p>Chambers are worth a look too, mostly for referrals and B2B work. The Katy Area Chamber of Commerce and the {SRC['cfchamber']} both run networking events, ribbon cuttings and member directories, and the Katy Area Economic Development Council works with larger employers. Go to three events before judging. The value is in the regulars, and you meet them on visit three, not visit one.</p>"""),

            ("Your first 90 days marketing in Katy and Cypress", f"""<p>If you’re starting from scratch, or starting over, here’s the order we’d go in.</p>
<!--fig:plan-->
<p>On budget: a single-location service business in Katy or Cypress can do the first 90 days of this for a few thousand dollars, plus ad spend. That’s our experience, not a quote. Click costs here are similar to the rest of Houston; our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} give you a feel for your category.</p>
<p>And if you’d like a team that knows the difference between Cinco Ranch and Cypress Creek Lakes to run it, we have local pages for {L('/digital-marketing-agency-katy-tx/', 'Katy')} and {L('/digital-marketing-agency-cypress-tx/', 'Cypress')}. Tell us about your business and goals and a senior strategist will build a custom plan. <a href="/contact/">Get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I market a small business in Katy, TX?",
             "Start with a complete Google Business Profile listing the Katy-area cities or ZIPs you serve, plus one real page on your site for Katy with local photos and reviews. Use master-planned community names where you serve them, take part in neighborhood Facebook groups as a person rather than an ad, and time promotions to the Katy ISD calendar. Add Google Ads on service plus community keywords once tracking works."),
            ("What is the best way to advertise in Cypress, TX?",
             "For most local businesses, Google search and the map pack come first, since people search when they need something. Then add Facebook and Instagram ads targeted around your service area with real local photos, community group participation in places like Bridgeland and Towne Lake, and event sponsorships such as those at The Boardwalk at Towne Lake. Track every channel so you can cut what doesn't produce customers."),
            ("Is Katy, TX still growing?",
             "Yes. Census estimates for July 2024 to July 2025 show Fort Bend County adding 24,163 residents to reach 975,191, Waller County growing 5.69%, second among U.S. counties by percentage, and Harris County adding the most people of any county in the country. Katy ISD gained 6,927 students from 2021 to 2026. Growth is concentrated in northwest Katy communities like Elyson and Sunterra."),
            ("How many service areas can I add to Google Business Profile in Katy and Cypress?",
             "Google lets you list up to 20 service areas by city or ZIP code, and the whole area should stay within about two hours of driving from your base. You can’t use a radius. Listing more areas doesn’t guarantee rankings in each, because proximity still matters a lot in the map pack, so pair your profile with a genuinely local page for each main area like Katy and Cypress."),
            ("When are Katy ISD and Cy-Fair ISD spring breaks in 2027?",
             "Katy ISD’s spring break is March 8-12, 2027, and Cy-Fair ISD’s is March 15-19, 2027, a week apart. Both districts started the 2026-27 year on Aug. 12, 2026. Businesses that serve families in both districts, like camps, kids’ dentists and family entertainment, should plan separate promotions for each break and check the official calendars for any weather-related changes."),
        ],
        "figures": {
            "growth": {
                "type": "stats",
                "title": "West Houston growth, by the numbers",
                "stats": [["+48,695", "Harris County residents, 2024-25 (No. 1 in U.S.)"], ["975,191", "Fort Bend County population, 2025"], ["5.69%", "Waller County growth, No. 2 in U.S."], ["114,697", "Cy-Fair ISD students, 3rd in Texas"]],
                "note": "Sources: U.S. Census Bureau via InnovationMap; Texas Tribune",
                "alt": "Stats on population growth in Katy and Cypress, TX, across Harris, Fort Bend and Waller counties west of Houston",
                "caption": f"From {SRC['im']} and {SRC['tt']}.",
            },
            "map": {
                "type": "map",
                "title": "Katy, Cypress and the roads that connect them",
                "sub": "I-10, US-290 and the Grand Parkway shape who can reach you",
                "highlight": ["Katy", "Cypress", "Fulshear", "Tomball", "Memorial"],
                "alt": "Map of Katy, Cypress, Fulshear and Tomball with I-10, US-290 and the Grand Parkway for local marketing west of Houston",
                "caption": "Target where customers live, and say plainly which side of the Grand Parkway you serve.",
            },
            "pages": {
                "type": "compare",
                "title": "Service-area pages: thin vs. local",
                "left": {"title": "Thin (city name swapped)", "items": ["Same text on Katy and Cypress pages", "Stock photos", "No ZIPs or communities named", "Reviews from anywhere", "No drive time or coverage detail"]},
                "right": {"title": "Local (worth ranking)", "items": ["Copy written for that area", "Photos from real jobs there", "ZIPs and communities you serve", "Reviews from customers there", "Arrival times and coverage map"]},
                "alt": "Comparison of thin and local service-area pages for local SEO in Katy and Cypress, TX",
                "caption": "One genuinely local page per main area beats twenty copies.",
            },
            "groups": {
                "type": "checklist",
                "title": "Facebook group rules for local businesses",
                "sub": "How to be recommended instead of removed",
                "items": ["Join as a person, with your real name", "Read the group rules before posting", "Answer questions even with no sale in it", "Reply to “who do you use?” once, briefly", "Never paste a flyer into a thread", "Ask the admin about business days or sponsorship", "Thank customers who tag you", "Take complaints to a private message fast"],
                "alt": "Checklist for local businesses using neighborhood Facebook groups in Katy, Cypress, Bridgeland and Towne Lake",
                "caption": "Admins remember who helps and who spams.",
            },
            "events": {
                "type": "steps",
                "title": "Make a local event booth pay off",
                "sub": "Katy Rice Harvest Festival, Light the Towne, Cy-Fest and the rest",
                "steps": [["Pick the right event", "Match the crowd to your customer, not the size."], ["Capture names", "A drawing or QR code to a booking page."], ["Staff it well", "People who can answer real questions."], ["Follow up in a week", "Email or text while the event is fresh."], ["Track it", "A dedicated URL or offer code per event."]],
                "alt": "Five steps to get customers from local event sponsorships in Katy and Cypress, TX",
                "caption": "Awareness is nice. A list of names you can follow up with is better.",
            },
            "plan": {
                "type": "steps",
                "title": "First 90 days in Katy and Cypress",
                "sub": "The order we’d do it in",
                "steps": [["Days 1-14", "Fix Business Profile, service areas, call and form tracking."], ["Days 15-30", "Build Katy and Cypress pages with local photos and reviews."], ["Days 31-45", "Launch search ads on service and community keywords."], ["Days 46-60", "Join community groups; start a steady review routine."], ["Days 61-90", "Add Meta ads and one event, timed to the school calendar."]],
                "alt": "A 90-day plan for marketing a local business in Katy and Cypress, TX, west of Houston",
                "caption": "Tracking comes first so every later step can be judged on results.",
            },
        },
    },
]
