"""Batch 9: moving company marketing in Houston (local and intrastate movers, some interstate), and property
management company marketing in Houston (winning owner clients and doors under management, not tenants).

Research, movers: 43 Tex. Admin. Code 218.52 (Cornell LII) on household goods advertising (TxDMV No. format, website
home-page items, 2-inch truck lettering); TxDMV's TxDMV number requirements page (HHG carriers register regardless of
vehicle weight; $100 application, $10 per vehicle, $100 insurance filings; $300,000 liability under 26,000 lb; $5,000 /
$10,000 cargo); TxDMV "Don't Make a Move" consumer page (helpline (888) 368-4689, binding or not-to-exceed proposals,
Rights and Responsibilities brochure); 49 CFR 375.207 (U.S. DOT No. in interstate ads); Google Ads local services
policy (advanced verification required only for locksmith and garage door in the U.S.); Google LSA category list
("Moving services", "Storage"); Google LSA screening page; Search Engine Journal on LSA moving into Google Ads (July
2026); BBB "Know Your Mover" study; FMCSA Operation Protect Your Move 2024 report; KPRC Click2Houston on BBB's May 2026
moving-scam warning; ABC13 on Chevron's HQ move; Greater Houston Partnership on Expand Energy and Devon HQ moves;
ABC13 on Census estimates (126,720 added, July 2024 to July 2025).
Research, property management: TREC FAQ on property manager licensing (TRELA 1101.002(1)(A)(x), Rule 535.4(h),
on-site apartment manager exemption); TREC "Social Media and Advertising" (Rule 535.155 name size, Rules 531.18 and
531.20 links); TREC IABS form page (label wording, 10-point font); Google's housing/employment/credit personalized ads
FAQ (property management services on the not-restricted list); Jon Loomer on Meta's Housing special ad category;
Google Maps prohibited content policy (conflict of interest, incentives, selective solicitation); Houston Agent
Magazine on HAR rental reports (Dec/full-year 2025 and July 2026); Community Impact on Houston single-family rental
demand (May 2026); KPRC on SB 38 (effective Jan 1, 2026).
Left out (couldn't verify from a primary page in this session): typical Houston management fee percentages,
Consumer Review Fairness Act specifics, Texas deposit-refund deadlines, any mover cost-per-lead benchmarks.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # movers
    "tac": A("https://www.law.cornell.edu/regulations/texas/43-Tex-Admin-Code-SS-218-52", "43 Texas Administrative Code §218.52"),
    "txnum": A("https://www.txdmv.gov/motor-carriers/txdmv-number?tab=requirements", "TxDMV’s registration requirements page"),
    "txmove": A("https://www.txdmv.gov/motorists/consumer-protection/dont-make-a-move", "TxDMV’s consumer page for people hiring movers"),
    "cfr375": A("https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-375/subpart-B/section-375.207", "49 CFR 375.207"),
    "gpolicy": A("https://support.google.com/adspolicy/answer/13527633?hl=en", "Google’s local services ad policy"),
    "lsacat": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "lsascreen": A("https://support.google.com/localservices/answer/6226575", "Google’s LSA screening page"),
    "sej": A("https://www.searchenginejournal.com/google-is-bringing-local-services-ads-into-google-ads/582816/", "Search Engine Journal"),
    "bbb": A("https://bbb.org/MoverScams", "the BBB’s “Know Your Mover” study"),
    "opym": A("https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-07/OPYM_report_2024.pdf", "FMCSA’s 2024 Operation Protect Your Move report"),
    "kprc": A("https://www.click2houston.com/news/local/2026/05/27/houston-area-families-warned-about-moving-scams-as-peak-moving-season-begins/", "KPRC reported in May 2026"),
    "chevron": A("https://abc13.com/post/chevron-move-texas-oil-gas-giant-lay-off-600-workers-california-relocates-corporate-operations-houston/16144517/", "ABC13"),
    "ghp": A("https://houston.org/news/houston-attracts-major-energy-investment-with-hq-moves-and-expansions", "the Greater Houston Partnership"),
    "census": A("https://abc13.com/post/houston-area-tops-latest-us-census-growth-estimates-despite-slowing-population-data-shows/18791745/", "Census estimates reported by ABC13"),
    # property management
    "trecpm": A("https://www.trec.texas.gov/q-does-property-manager-have-be-licensed?", "TREC’s licensing FAQ"),
    "trecsm": A("https://www.trec.texas.gov/sites/default/files/pdf-forms/Social%20Media%20and%20Advertising.pdf", "TREC’s social media and advertising guide"),
    "treciabs": A("https://www.trec.texas.gov/forms/consumer-protection-notice", "TREC’s forms page"),
    "gfaq": A("https://support.google.com/adspolicy/answer/9997418?hl=en", "Google’s housing ads policy FAQ"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    "ppcl": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
    "hardec": A("https://houstonagentmagazine.com/2026/01/26/har-rental-report-dec-full-year-2025/", "HAR’s full-year 2025 rental report"),
    "harjul": A("https://houstonagentmagazine.com/2026/08/24/har-rental-report-aug-2026/", "HAR’s July 2026 numbers"),
    "cisfr": A("https://communityimpact.com/houston/heights-river-oaks-montrose/real-estate/2026/05/12/home-edition-demand-for-single-family-rental-homes-climb-as-homeownership-slows/", "Community Impact"),
    "sb38": A("https://www.click2houston.com/news/local/2026/01/01/new-texas-law-targets-squatters-but-also-reshapes-evictions-for-renters/", "Senate Bill 38"),
}

MOVERS = "/blog/moving-company-marketing-houston/"
PM = "/blog/property-management-company-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: moving companies
    {
        "slug": "moving-company-marketing-houston",
        "title": "Moving Company Marketing in Houston: How to Book More Moves Without Buying Junk Leads",
        "seo_title": "Moving Company Marketing in Houston: Book More Moves",
        "desc": "Moving company marketing for Houston movers: TxDMV and USDOT ad rules, Google Ads and LSA, lead sites, reviews, quote speed, seasonality and cost per move.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b6",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for moving company marketing in Houston, The Woodlands, Katy and Sugar Land",
        "related": ["local-services-ads-vs-google-ads-home-services", "speed-to-lead-response-time-follow-up-crm", "angi-vs-thumbtack-leads-worth-it-contractors"],
        "sections": [
            (None, f"""<p>The 30th of the month, a Saturday, 7:10 a.m. Three crews are already out: a two-bedroom leaving an apartment in Katy, a four-bedroom in Kingwood, and a downsizing couple in The Woodlands headed to a patio home in Conroe. Your dispatcher is juggling a truck with a sticky liftgate. The office line rings and it’s a woman in Spring whose “movers” never showed up after she paid a $400 deposit to a website. She wants to know if you can do it today.</p>
<p>Meanwhile, a lead site has sold the same quote request to you and five competitors overnight. By the time anyone in your office looks at it, two of them have already called.</p>
<p>That morning has most of moving company marketing in it. Demand piles up on the same weekends. Trust is low because of the scammers. And the company that answers first with a believable price wins the job.</p>
<p>To get more moving customers in Houston, put your TxDMV number (and your USDOT number if you go interstate) everywhere a customer looks, win the Google Maps results for your part of town, run tight search ads and Local Services Ads, and answer quote requests in minutes, not hours. Then build the partnerships with apartments, agents and relocation managers that fill your calendar without bidding wars. Judge every bit of it on cost per booked move, never cost per lead.</p>"""),

            ("Start with the license, because Texas makes it part of your advertising", f"""<p>Most marketing advice for movers skips this, and it’s the cheapest trust signal you have.</p>
<p>In Texas, anyone who transports household goods for compensation has to register with TxDMV, regardless of vehicle weight, per {SRC['txnum']}. Carriers under 26,000 pounds need at least $300,000 in liability coverage, plus cargo coverage of $5,000 per vehicle and $10,000 aggregate. The fees are small: a $100 application, $10 per vehicle per year and $100 for each insurance filing.</p>
<p>The advertising rule is what matters for marketing. Under {SRC['tac']}, a household goods carrier can’t run false or misleading ads, and its print ads aimed at a local Texas market must show the business name as it appears on the certificate, a Texas street address and the registration number in the form “TxDMV No. ______.” Any website operated by or for the carrier has to show the name, TxDMV’s toll-free consumer help line and that “TxDMV No.” on its home page. Trucks need the name and number on both sides in letters at least two inches high.</p>
<p>If you do interstate moves, federal rules add one more line. {SRC['cfr375']} requires every ad for interstate household goods service to include your name as it appears on your USDOT registration and your number in the form “U.S. DOT No. ______.”</p>
<!--fig:license-->
<p>We’d go further than the minimum. Put both numbers in the header of the site, on every quote page, in the Google Business Profile description, on the crew shirts and in the email signature. Link the TxDMV number to the state’s lookup tool. A nervous customer who checks your number and finds “Active” is halfway to booking. One who can’t find it moves on, and honestly, they should.</p>"""),

            ("The trust gap: selling against moving scams", f"""<p>Movers start every conversation in a hole they didn’t dig. {SRC['bbb']} found the bureau receives an average of about 13,000 complaints and negative reviews about movers each year. In 2019, FMCSA logged 4,780 complaints, and 57% involved overcharging. The same study describes the pattern: a low quote by phone, a deposit, a job passed to an unlicensed crew, and a higher price once the goods are on the truck. It also notes some scammers work with online sites that “find movers” and post phony reviews.</p>
<p>The federal crackdown is real and Texas is in the middle of it. {SRC['opym']} lists 128 hostage-goods complaints addressed in that operation, and Texas had 11 investigations, the third-highest of any state. In Houston, {SRC['kprc']} that the BBB was warning families about scams as peak season started, telling them to check registration, avoid large deposits and be wary of phone-only estimates.</p>
<p>So your marketing has to answer the scam questions before the customer asks them. Here’s what that looks like on a page and on the phone:</p>
<!--fig:trust-->
<p>Texas already requires much of this. Per {SRC['txmove']}, a licensed mover has to give a written proposal before loading that’s either binding or not-to-exceed, and hand over the “Your Rights and Responsibilities When You Move in Texas” brochure. Say so on your site in plain words: “You’ll get a written not-to-exceed price before we load a single box.” Scammers can’t copy that line without lying, and most of them won’t bother with a real address and real truck photos either.</p>
<p>Use photos of your actual lettered trucks and uniformed crews. Customers have learned that stock photos of smiling couples with boxes are what fly-by-night sites use.</p>"""),

            ("Google Business Profile and reviews for movers", f"""<p>Most local moves start with a search like “movers near me” or “moving company Sugar Land,” and the map pack takes up a big piece of that screen. Choose <b>Moving company</b> or <b>Mover</b> as your primary category (match what your top-ranking local competitors use), and add <b>Moving and storage service</b> or <b>Storage facility</b> only if you actually run storage. If you have a yard or warehouse customers can visit, show the address. If you don’t, set it up as a service-area business with the towns you really serve.</p>
<p>Fill the Services list with what people search for: apartment moves, packing, piano moves, senior moves, office moves, labor-only loading, long-distance to Dallas, Austin and San Antonio. Put the TxDMV number in the description. Post photos every week from real jobs, with the customer’s permission and without house numbers in the shot.</p>
<p>Reviews do double duty for a mover. They feed the map ranking and they’re the main way a scared customer decides you’re real. The rules from {SRC['gpol']} are short: no incentives, no discouraging negative reviews and no selectively asking only happy customers. In April 2026, Google also added language against telling staff to collect a set number of reviews or reviews with specific content, per {SRC['ppcl']}, so skip the crew contests.</p>
<p>The ask that works: a text from the office the evening of the move, after the last box is in, with the same link for everyone.</p>
<p><i>“Hi Dana, it’s Marcus from [Company]. Thanks for trusting us with today’s move to Conroe. If you have a minute, a Google review helps other families find a licensed mover: [link]. And if anything arrived damaged, reply here and we’ll start a claim tomorrow.”</i></p>
<p>That last sentence matters. It sends unhappy customers to you first, and you still sent the same link to everyone. Reply to every review, and to the bad ones with specifics and a phone number. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("Local Services Ads and Google Ads for movers", f"""<p>Google’s {SRC['lsacat']} includes “Moving services” and “Storage.” LSAs are the pay-per-lead boxes at the top of the results. You pay for a call or message instead of a click. Screening varies by category and location, and per {SRC['lsascreen']} it can include license checks, a certificate of insurance and background checks for owners and the people who do the work. Have your TxDMV certificate, insurance certificate and crew list ready before you start.</p>
<p>Two other policy points. Google currently requires advanced verification for locksmith and garage door ads in the U.S. but doesn’t list movers there, per {SRC['gpolicy']}, so a mover’s regular search ads go through the standard advertiser verification every account eventually faces. And LSA itself is moving into Google Ads. {SRC['sej']} reported that starting in August 2026, a first group of U.S. advertisers sees LSA run as pay-per-lead Performance Max campaigns inside Google Ads, with daily budgets and a single target CPA, and the separate LSA dashboard going away after migration. If your LSA account flips over, check the budget settings the same week.</p>
<p>Regular search ads still matter, because LSA gives you almost no control over which jobs you get. How we’d set up a local mover:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Local movers by town</td><td>movers The Woodlands, moving company Katy, local movers Pearland</td><td>Town page with local price ranges and reviews from that area</td></tr>
<tr><td>Apartment moves</td><td>apartment movers Houston, 1 bedroom movers near me</td><td>Apartment page: flat rates by unit size, elevator and stairs notes</td></tr>
<tr><td>Long distance in Texas</td><td>movers Houston to Austin, Houston to Dallas moving company</td><td>Intrastate page with the TxDMV number and a binding-price explanation</td></tr>
<tr><td>Specialty</td><td>piano movers Houston, gun safe movers, senior moving services</td><td>One page per specialty, with real photos</td></tr>
<tr><td>Commercial</td><td>office movers Houston, commercial moving company Energy Corridor</td><td>Commercial page with weekend and after-hours scheduling</td></tr>
</tbody></table></div>
<p>Negatives on day one: truck rental, u-haul, uhaul, penske, budget truck, box truck, pods (unless you sell portable storage), boxes, moving supplies, jobs, hiring, driver, salary, “how to,” checklist, scam, complaints, free, and the names of national van lines you don’t represent.</p>
<p>Sample ad copy that answers the trust question in the ad itself:</p>
<ul>
<li>Headline: “Licensed Houston Movers, TxDMV No. [number]”</li>
<li>Headline: “Written Not-To-Exceed Price”</li>
<li>Headline: “Quote by Video in 15 Minutes”</li>
<li>Description: “Local crews, our own trucks, no large deposit. Apartments, homes and offices across Katy, Cypress and The Woodlands.”</li>
</ul>
<p>Set location targeting to people in or regularly in your area. Then add a separate campaign targeting people in other states searching “movers Houston,” since out-of-state transferees often book the destination crew before they fly in. Track calls as conversions. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads comparison')} goes deeper on splitting budget between the two, and our {L('/services/search-marketing/', 'search marketing team')} runs both.</p>"""),

            ("Lead aggregator sites: why they feel cheap and end up expensive", f"""<p>Moving lead sites are the first thing most new movers buy, and the first thing most established movers complain about. The model is simple: a customer fills out one form, and the site sells that lead to several movers. What follows is a race to call, a race to the bottom on price, and a customer who now has five companies texting them.</p>
<p>In accounts we’ve looked at, the problems repeat:</p>
<ul>
<li><b>Shared leads.</b> You’re paying for the same person four or five competitors are paying for. Your close rate is capped before you dial.</li>
<li><b>Stale or fake contacts.</b> Wrong numbers, people who already booked, people who were just curious about a price in March for a move in August.</li>
<li><b>Price anchoring.</b> When five movers quote, the customer remembers the lowest number, and the lowest number is often the one that turns into a hostage situation later. The BBB study mentions scammers working with “find a mover” sites.</li>
<li><b>No asset.</b> When you stop paying, the leads stop. Nothing you built carries over.</li>
</ul>
<p>We wouldn’t tell every mover to quit them. A young company with no reviews may need them for a season. But treat them like any other channel: track booked moves per 100 leads and revenue per lead, call within five minutes, use the dispute process for bad contacts, and cap the spend. The money usually does more on your own Google Business Profile, search ads and partnerships, where the customer only talked to you. Our {L('/blog/angi-vs-thumbtack-leads-worth-it-contractors/', 'post on Angi and Thumbtack leads')} covers the same math for contractors.</p>"""),

            ("Quote speed decides a lot of moves", f"""<p>A customer asking for a moving quote usually asks two or three companies at once. The first credible, specific price tends to set the bar for everyone after it. Customers say they choose on price. A lot of the time they actually choose the first mover that felt organized.</p>
<!--fig:speed-->
<p>A few things that make the speed possible:</p>
<ul>
<li><b>A real quote form.</b> Ask for move date, origin and destination ZIPs, home size, stairs or elevator, and big items (piano, safe, treadmill). Skip “tell us about your move” free-text boxes.</li>
<li><b>Video surveys.</b> A five-minute FaceTime or video walkthrough beats a phone guess and is faster than an in-home visit. It also answers the BBB’s warning about phone-only estimates.</li>
<li><b>Text-back for missed calls.</b> On a Saturday when the office is half-staffed, an automatic “Sorry we missed you, here’s a link to get a quote” keeps the lead warm.</li>
<li><b>Evening coverage.</b> Many quote requests come in after work. Someone should answer until 8 p.m. in peak season, even if it’s an answering service that books a callback.</li>
</ul>
<p>Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up side.</p>"""),

            ("Seasonality: summer, month-end and Houston weather", f"""<p>Moving demand isn’t smooth, and your ad budget shouldn’t be either. Summer is the peak (KPRC’s May 2026 report treated May as the start of the busy season), driven by school calendars and lease cycles. Inside every month there’s a second peak: the last few days and the first of the month, when apartment leases turn over. Weekends book first.</p>
<!--fig:season-->
<p>What we’d do with that pattern:</p>
<ul>
<li>Raise search budgets from April through August, and shift spend toward the second half of each month, when month-end movers are booking.</li>
<li>Sell the off-peak on purpose. A midweek, mid-month discount in January or February fills trucks that would otherwise sit. Put it in the ads and on the quote page.</li>
<li>Stop paying for clicks you can’t serve. When the last weekend of June is full, pause the campaigns that target that weekend’s searches or switch the message to “booking July now.”</li>
<li>Plan for the weather. Houston crews in August need earlier start times, and customers like hearing that you plan around the heat. Hurricane season runs June 1 to November 30; have a storm-related page ready for packing out flood-damaged homes and moving contents to storage, if you do that work.</li>
</ul>
<p>Our {L('/blog/seasonal-marketing-greater-houston/', 'Houston seasonal marketing calendar')} has the broader picture for local service businesses.</p>"""),

            ("Apartments, agents and corporate relocation: the partnerships that fill trucks", f"""<p>The best moving leads are the ones nobody else got. Those mostly come from people who see moves before they happen.</p>
<ul>
<li><b>Apartment leasing offices.</b> Communities in Katy, Cypress, Spring and The Woodlands turn over units every month. Leasing staff get asked “do you know a good mover?” constantly. A one-page flyer, a tenant discount (paid to the tenant, never a kickback to staff, which can create its own problems), and showing up reliably for their residents is the whole program.</li>
<li><b>Real estate agents.</b> Agents want their clients’ closing week to go smoothly. Give them a referral card, a priority slot for closings and a quick text update when their client’s move is done.</li>
<li><b>Senior living and downsizing.</b> Retirement communities and senior move managers send steady work that’s often midweek, exactly when you have capacity.</li>
<li><b>HR and relocation managers.</b> Corporate moves are bigger and pay on time.</li>
</ul>
<p>That last group deserves attention right now. Chevron is moving its headquarters and all corporate functions from California to Houston over five years, per {SRC['chevron']}. {SRC['ghp']} reported in February 2026 that Expand Energy planned to move its headquarters to Houston later in 2026 and that the combined Devon and Coterra would be headquartered here. And the Houston metro added 126,720 people between July 2024 and July 2025, the largest gain of any U.S. metro, according to {SRC['census']}.</p>
<p>Not every transferee gets a full relocation package, and plenty get a lump sum and pick their own movers. Build a “Relocating to Houston” page that explains neighborhoods and commutes in a paragraph each, offers destination-side services (unloading a container, unpacking, storage), and lets someone in California book a video survey. Then run search ads to people outside Texas searching for Houston movers.</p>"""),

            ("Cost per booked move: the only number worth arguing about", f"""<p>Cost per lead is easy to measure and easy to fool yourself with. A $15 shared lead that books 1 time in 20 costs $300 per move. A $90 search lead that books 1 time in 3 costs $270. The cheap lead lost.</p>
<!--fig:cpbm-->
<p>To get the real number, you need four things wired together:</p>
<ol>
<li>A tracked phone number per channel (Google Ads, LSA, Business Profile, lead sites, partners) with calls recorded. See {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'how to track calls and forms in GA4 and Google Ads')}.</li>
<li>A CRM or moving software where every lead keeps its original source.</li>
<li>A “booked” status that means a deposit or signed proposal, not “sounded interested.”</li>
<li>Revenue per move attached to each booking, so a $600 apartment move and a $6,000 corporate relocation don’t count the same.</li>
</ol>
<p>Here’s an illustrative month for a local mover with four trucks. These aren’t benchmarks; they show what to count.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Spend</th><th>Leads</th><th>Booked moves</th><th>Cost per booked move</th></tr></thead>
<tbody>
<tr><td>Google search ads</td><td>$3,000</td><td>45</td><td>14</td><td>$214</td></tr>
<tr><td>Local Services Ads</td><td>$1,500</td><td>40</td><td>11</td><td>$136</td></tr>
<tr><td>Lead aggregator</td><td>$1,800</td><td>120</td><td>7</td><td>$257</td></tr>
<tr><td>Partners and referrals</td><td>$400</td><td>18</td><td>10</td><td>$40</td></tr>
</tbody></table></div>
<p>Once a table like this is real for a full season, budget decisions mostly make themselves. Feed booked moves back into Google Ads as offline conversions so the bidding learns which searches turn into jobs.</p>
<p>If you’d like a senior strategist to look at your numbers and build a plan around your trucks, crews and season, <a href="/contact/">get in touch</a>. If you also manage rentals, our {L(PM, 'property management marketing guide')} covers the owner side.</p>"""),
        ],
        "faq": [
            ("How do moving companies get more customers?",
             "Most local movers grow through Google: a complete Business Profile with real photos and steady reviews, search ads on town and move-type keywords, and Local Services Ads in the Moving services category. Partnerships with apartment leasing offices, real estate agents, senior communities and relocation managers add jobs that nobody else is bidding on. Answering quote requests within minutes often matters as much as any ad."),
            ("Do Texas movers have to show their TxDMV number in ads?",
             "Yes. Texas rules require household goods carriers to show the registration number in the form TxDMV No. followed by the number in print ads aimed at a local Texas market, along with the business name and a Texas street address. Websites must show the name, TxDMV’s consumer help line and the number on the home page. Interstate movers also need U.S. DOT No. in their ads."),
            ("Are moving lead sites worth it?",
             "Sometimes, for a new company that needs volume quickly. The catch is that many lead sites sell the same request to several movers, so you compete on speed and price for every job, and contacts are often stale. Track booked moves and revenue per lead, call within five minutes, dispute bad leads, and compare the cost per booked move with your own search ads and referrals."),
            ("Can moving companies use Google Local Services Ads?",
             "Yes. Google’s Local Services Ads list includes Moving services and Storage. You pay per lead rather than per click, and screening can include license checks, insurance certificates and background checks depending on category and location. Google began moving LSA into Google Ads as pay-per-lead Performance Max campaigns in August 2026, so check budget settings if your account migrates."),
            ("When is peak moving season in Houston?",
             "Summer is the busiest stretch, with May usually treated as the start, because school calendars and lease renewals line up. Within each month, the last few days and the first are busiest because apartment leases turn over then, and weekends book first. Movers can fill slow periods by promoting midweek and mid-month pricing in winter and raising ad budgets from April through August."),
        ],
        "figures": {
            "license": {
                "type": "checklist",
                "title": "What a Texas mover’s ads and site must show",
                "sub": "Plus the extras we’d add",
                "items": ["Business name as on the TxDMV certificate", "“TxDMV No.” and number on the home page", "TxDMV consumer help line on the home page", "Texas street address in local print ads", "“U.S. DOT No.” in ads for interstate moves", "Name and number on both sides of every truck", "Numbers on quote pages and Business Profile", "Link to the state’s carrier lookup"],
                "alt": "Checklist of TxDMV and USDOT advertising requirements for moving company marketing in Houston and The Woodlands",
                "caption": f"Requirements from {SRC['tac']} and {SRC['cfr375']}. The last two items are our suggestions.",
            },
            "trust": {
                "type": "compare",
                "title": "Scam signals vs. signals that book moves",
                "left": {"title": "What scared customers watch for", "items": ["Phone-only estimate", "Large deposit up front", "No address, cell number only", "Unmarked or rental truck", "Price climbs after loading"]},
                "right": {"title": "What your marketing should show", "items": ["Video or in-home survey", "Small or no deposit, stated plainly", "Real address and office line", "Photos of your lettered trucks", "Written binding or not-to-exceed price"]},
                "alt": "Comparison of moving scam warning signs and trust signals for moving company marketing in Houston",
                "caption": f"Warning signs drawn from {SRC['txmove']} and the BBB study.",
            },
            "speed": {
                "type": "steps",
                "title": "From quote request to booked move",
                "sub": "A fast-response setup for a local mover",
                "steps": [["Instant text", "Auto-reply within a minute with the coordinator’s name."], ["Call in 5 minutes", "During business hours, a person calls right away."], ["Video survey", "Five-minute walkthrough instead of a phone guess."], ["Written price", "Binding or not-to-exceed proposal the same day."], ["Follow-up", "Text at 24 hours and 3 days if they haven’t booked."]],
                "alt": "Steps for fast quote response that helps moving companies in Houston and The Woodlands book more moves",
                "caption": "The first credible written price usually sets the bar for everyone after it.",
            },
            "season": {
                "type": "columns",
                "title": "How a mover’s demand might move through the year",
                "sub": "Relative booking volume, busiest month = 100",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [45, 48, 60, 70, 85, 100, 98, 92, 70, 62, 52, 50],
                "highlight": [5, 6, 7],
                "y_label": "Relative volume",
                "note": "Illustrative example. Use your own booking history.",
                "alt": "Illustrative chart of seasonal moving demand for Houston moving companies, peaking in summer",
                "caption": "Pace ad spend to your own curve, and push off-peak pricing in the low months.",
            },
            "cpbm": {
                "type": "funnel",
                "title": "Counting to cost per booked move",
                "stages": [["Ad spend", "$3,000"], ["Leads", "45"], ["Surveys done", "26"], ["Booked moves", "14"], ["Cost per booked move", "$214"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how a Houston moving company calculates cost per booked move from ad spend and leads",
                "caption": "Track every stage by source, or the cheapest-looking lead source will fool you.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: property management
    {
        "slug": "property-management-company-marketing-houston",
        "title": "Property Management Company Marketing in Houston: How to Win More Doors",
        "seo_title": "Property Management Marketing in Houston: Win More Doors",
        "desc": "Property management marketing for Houston: winning owner clients with TREC-compliant sites, suburb SEO, Google Ads, reviews, referrals and cost per new door.",
        "category": "Strategy",
        "icons": ["Google", "Google Ads", "Google Business Profile"],
        "art": "b4",
        "hero": "key",
        "hero_alt": "Illustration of a house key for property management company marketing in Houston, Katy, Cypress and The Woodlands",
        "related": ["real-estate-agent-marketing-the-woodlands-houston", "complete-guide-google-reviews", "seo-cost-houston-the-woodlands"],
        "sections": [
            (None, f"""<p>Tuesday afternoon. An owner calls from Denver. Her company moved her there last spring, she couldn’t get her price for the house in Cypress, so she rented it out herself. Now the tenant has left, the house has sat empty for three weeks, the AC quit in the heat, and she’s Googling “property management Cypress TX” from her desk.</p>
<p>She finds three companies. The first has a 3.4-star rating, mostly from tenants angry about deposits. The second has no prices anywhere on the site. The third shows its fees, has a page about Cypress rents and HOA leasing rules, and a 4.7 rating with reviews from owners. She calls the third one.</p>
<p>That’s property management marketing in one search. Tenants are not your customer here. Owners are, and every new owner adds doors under management that pay you every month for years.</p>
<p>To win more property management clients in Houston, build a site and Google profile that speak to owners (with TREC’s required links and broker name), rank for “property management [suburb]” with real local pages, run search ads on owner-intent keywords only, manage the tenant-review problem honestly, and grow referral partners who meet owners before you do. Measure all of it in cost per new door.</p>"""),

            ("Who your owners are, and what they’re searching", f"""<p>Houston keeps producing landlords. HAR counted 47,292 leases in 2025, up 6.2% from 2024, per {SRC['hardec']}. {SRC['cisfr']} reported the average number of single-family homes leased per month rose from 3,592 in 2023 to 3,945 in 2025, while average rent went from $2,236 to $2,319. In July 2026, single-family leases were up 12.1% from a year earlier at 5,185, with 9,832 rentals available and a typical 37 days on market, per {SRC['harjul']}.</p>
<p>More inventory and longer days on market are good news for your marketing. Owners who are getting nervous about a vacant house start looking for help.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Owner type</th><th>What they search</th><th>What they worry about</th><th>What wins them</th></tr></thead>
<tbody>
<tr><td>Accidental landlord (relocated, couldn’t sell, inherited)</td><td>“rent my house Houston,” “should I rent or sell my house,” “property management near me”</td><td>Being called at 2 a.m., bad tenants, eviction</td><td>Plain explanation of what you do, fees up front, a rent estimate</td></tr>
<tr><td>Small local investor (2 to 15 doors)</td><td>“property management company Katy,” “property manager fees Texas”</td><td>Maintenance markups, slow leasing, owner statements</td><td>Fee table, sample owner statement, days-to-lease stats</td></tr>
<tr><td>Out-of-state investor</td><td>“Houston property management for investors,” “turnkey rental Houston”</td><td>Can’t see the property, trust</td><td>Video inspections, online portal, references</td></tr>
<tr><td>Build-to-rent or small portfolio</td><td>Usually referral or LinkedIn, not search</td><td>Scale, reporting</td><td>Case-style capabilities page, direct outreach</td></tr>
</tbody></table></div>
<p>Most of the small companies we see in Houston make the same mistake: the homepage is written for tenants (“Find your next home!”) because that’s where the listings feed lives. Put the listings on their own tab. Make the homepage about owners.</p>"""),

            ("TREC rules come first: licensing and what your marketing must show", f"""<p>In Texas, most residential property management is a licensed activity. {SRC['trecpm']} says a license is required if the manager’s duties include showing or leasing the property for pay, and also for anyone who controls the acceptance or deposit of rent from a resident of a single-family home. The on-site manager exemption covers apartment complexes only; condos and townhomes don’t qualify. In practice, a property management company that leases houses runs under a broker license, and that broker’s name has to appear in its advertising.</p>
<p>The advertising rules then shape your website and social accounts. Per {SRC['trecsm']}, Rule 535.155 requires the broker’s name on ads, at least half the size of the largest contact information. Rules 531.18 and 531.20 require links to the Consumer Protection Notice and the Information About Brokerage Services (IABS) form, which on social media can live on the profile or one direct click away. {SRC['treciabs']} adds that the IABS link must be in a readily noticeable place on the homepage, labeled “Texas Real Estate Commission Information About Brokerage Services” in at least 10-point font.</p>
<!--fig:trec-->
<p>The rules don’t make a site any less effective. A licensed broker name and the TREC links are trust signals for an owner who’s about to hand you a house worth $350,000. Put your license number on the About page and link it to TREC’s license lookup. Many of the cheap “we’ll manage your rental” operations on Facebook can’t do that.</p>"""),

            ("SEO for “property management [suburb]” searches", f"""<p>Owners search with a place name. “Property management Katy.” “Property management company Sugar Land.” “Rental management The Woodlands.” “Property manager Pearland.” Each of those deserves a real page, and “real” is the whole trick.</p>
<p>A thin page that swaps the town name into the same 300 words won’t rank and won’t convince anyone. A strong suburb page includes:</p>
<ul>
<li>How many doors you manage in that area, and which neighborhoods (Cinco Ranch, Bridgeland, Towne Lake, Shadow Creek Ranch, Sienna, Kingwood, Creekside Park).</li>
<li>Typical rent ranges for three- and four-bedroom homes there, from your own leases, with the date.</li>
<li>Local wrinkles: HOA leasing restrictions and registration rules, MUD and tax notes for owners, school district pull, distance to the Energy Corridor, the Medical Center or The Woodlands business district.</li>
<li>Your typical days to lease in that suburb last quarter.</li>
<li>Reviews from owners in that area, and a photo of a home you manage there (with the owner’s okay).</li>
</ul>
<!--fig:areas-->
<p>Then build the owner-question pages that pull in early-stage searches: “how much do property managers charge in Texas,” “rent or sell my house in Houston,” “what does a property manager do,” “how to evict a tenant in Texas.” That last one got more timely when {SRC['sb38']} took effect January 1, 2026, changing eviction procedures and adding a faster route against squatters. An owner-facing explainer (with your attorney’s review) is exactly the content accidental landlords look for.</p>
<p>On Google Business Profile, choose <b>Property management company</b> as the primary category and add <b>Real estate agency</b> only if you also list homes for sale. List services in owner language: tenant placement, full-service management, leasing only, maintenance coordination, HOA compliance. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} shows how to structure suburb pages, and {L('/blog/seo-cost-houston-the-woodlands/', 'our SEO pricing post')} explains what this work typically costs.</p>"""),

            ("Content that attracts owners: rent estimates, fee tables and real numbers", f"""<p>The single best lead magnet in property management is a rent estimate. An owner who types in an address and asks “what would this rent for?” is telling you they’re thinking about it.</p>
<p>Done well, it’s a short form (address, beds, baths, square footage, condition) and a human-reviewed estimate within one business day, sent with three comparable leases and a note on how long similar homes took to lease. Done badly, it’s an instant automated number that’s $300 too high, which sets up a vacancy and an unhappy owner. We’d skip the instant number. The one-day turnaround is a reason to talk.</p>
<p>Other content that earns its keep:</p>
<ul>
<li><b>A fee table.</b> Monthly management percentage, leasing fee, renewal fee, any markup on maintenance, what happens when a house sits vacant. Owners compare companies on this. Hiding it sends them to the competitor who doesn’t.</li>
<li><b>A sample owner statement and a sample inspection report</b>, with personal details removed.</li>
<li><b>A quarterly Houston rent report</b> built from your own leases plus HAR’s public numbers. HAR put the average single-family rent at $2,245 in December 2025 and $2,419 in July 2026. Local agents and reporters link to this kind of page.</li>
<li><b>A rent-or-sell calculator</b> for accidental landlords, with honest assumptions about vacancy, repairs, management fees and taxes.</li>
<li><b>Storm and freeze pages.</b> What you do for owners before and after a hurricane or a hard freeze. In Houston, owners remember who called them after the last storm.</li>
</ul>"""),

            ("Google Ads for owner leads, not tenant clicks", f"""<p>The biggest waste we see in property management Google Ads is paying for tenants. Searches like “houses for rent Katy” have huge volume and cheap-looking clicks, and every one of them is a person looking for a home, not an owner looking for a manager.</p>
<!--fig:keywords-->
<p>Keep the account to owner intent:</p>
<ul>
<li>Suburb campaigns: “property management [town],” “property management company [town],” “rental property manager [town].”</li>
<li>Service campaigns: “tenant placement service Houston,” “leasing only property management,” “single family property management Houston.”</li>
<li>Situation campaigns: “rent my house,” “I need someone to manage my rental,” “property management for out of state owners.”</li>
<li>Brand, so a review site or competitor can’t sit on your name.</li>
</ul>
<p>Negatives on day one: for rent, rentals near me, apartments, houses for rent, rent to own, section 8 housing (unless you’re targeting owners who accept vouchers, with separate copy), low income, jobs, careers, salary, certification, course, license class, software, app, Buildium, AppFolio, HOA management (unless you offer it), commercial (unless you offer it), and “near me” tenant phrases like “cheap houses.”</p>
<p>On policy: Google’s housing rules restrict targeting by age, gender, parental status, marital status and ZIP code for housing ads, but {SRC['gfaq']} lists property management services among ads that may not have targeting restricted. Single-home listings and real estate brokers are on the restricted list. So an owner-acquisition campaign for your management services generally isn’t limited, while an ad for a vacant rental is. Keep them in separate campaigns.</p>
<p>Sample ad copy:</p>
<ul>
<li>Headline: “Katy Property Management”</li>
<li>Headline: “Leased in 30 Days or Less, Avg.” (only if your data proves it)</li>
<li>Headline: “See Our Fees, No Surprises”</li>
<li>Description: “Licensed Texas broker managing [number] homes in Katy and Fulshear. Free rent estimate in one business day.”</li>
</ul>
<p>Owner-intent clicks cost more than tenant clicks, and there are fewer of them. That’s fine. One owner can be worth years of fees. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a sense of click costs, and our {L('/services/search-marketing/', 'search team')} builds these accounts.</p>"""),

            ("Facebook and Instagram: housing rules apply to your listings, not your owner ads", f"""<p>Meta’s Housing special ad category covers ads that promote a housing opportunity, including listings for the sale or rental of a home or apartment, per {SRC['loomer']}. When you advertise a vacant rental, the category is required, and it brings the restrictions: age locked to 18 to 65+, all genders, at least a 15-mile radius, no ZIP code targeting, no lookalikes and limited detailed targeting.</p>
<p>Ads aimed at owners (“Own a rental in Cypress? See what we’d charge to manage it”) don’t promote a housing opportunity to the viewer, so they generally sit outside the category. Meta’s list isn’t exhaustive, though, and reviewers sometimes flag anything with a house photo. If an owner ad gets rejected, run it under Housing rather than fighting it. Owners are spread across every age and gender anyway, so you lose little.</p>
<p>What tends to work on Meta for owner acquisition:</p>
<ul>
<li>Retargeting people who visited your fee page or rent estimate page.</li>
<li>Short videos of a real make-ready or inspection with the manager talking to camera.</li>
<li>Lead forms with qualifying questions: how many properties, where, currently rented or vacant, currently managed or self-managed.</li>
</ul>
<p>Those questions cut volume and raise quality. Our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'guide to fixing bad Facebook leads')} explains why. Whatever you run for tenants, keep Fair Housing in the copy: describe the home, never the kind of renter you want.</p>"""),

            ("Reviews: when tenants drag your rating down", f"""<p>Here’s the uncomfortable math of property management reviews. You have two customer groups. Owners pay you and rarely review. Tenants don’t pay you, interact with you mostly when something’s broken or a deposit is withheld, and review often. A company doing its job well (enforcing leases, charging for real damage) can still end up at 3.5 stars.</p>
<p>What you can’t do, per {SRC['gpol']}: offer incentives for reviews, discourage negative reviews, selectively ask only happy people, or post reviews from staff, family or anyone with a conflict of interest. Google also tightened its language in April 2026 against review quotas and asking for specific content, per {SRC['ppcl']}. And you can’t get a review removed just because it’s from a tenant. Tenants are legitimate reviewers. Only policy violations, like harassment or off-topic content, are removable.</p>
<p>What you can do:</p>
<!--fig:reviews-->
<p>On replies, two Houston-specific cautions. Never disclose a tenant’s balance, eviction status or personal details in a public reply. And keep replies free of anything that could read as a judgment about a protected class. A good reply sounds like: <i>“We’re sorry the move-out felt unfair. Deposit deductions are itemized with photos, and we’re glad to walk through them. Please call our office at [number].”</i></p>
<p>Owners reading your profile know tenants complain. What they’re watching is how you respond and whether owner reviews say you protect their asset. Our {L('/blog/complete-guide-google-reviews/', 'guide to Google reviews')} has request templates.</p>"""),

            ("Referral partners who meet owners before you do", f"""<p>Many of the best owner leads never search at all. Someone they trust hands them your name.</p>
<ul>
<li><b>Real estate agents.</b> Agents meet accidental landlords constantly: sellers who can’t get their price, buyers keeping their old house. Many agents don’t want to manage rentals. Offer to send the owner back to them when it’s time to sell, and keep that promise. Our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how local agents market themselves')} shows their side.</li>
<li><b>Relocation and HR contacts.</b> Transferees leaving Houston often keep the house. Corporate relocation teams appreciate a manager they can name.</li>
<li><b>Estate and probate attorneys, CPAs and financial planners.</b> Inherited houses and tax questions both lead to rental decisions.</li>
<li><b>Investor groups and lenders</b> who finance rental purchases.</li>
<li><b>Contractors and make-ready vendors</b> who hear owners complain about their current manager.</li>
</ul>
<p>Check with your broker of record before paying anyone for a referral; TREC rules on compensation apply. A thank-you lunch and sending business back usually work better than a check anyway.</p>"""),

            ("Measuring cost per new door", f"""<p>A door is worth far more than a lead. Say a home rents for $2,300 and your management fee is 8% (illustrative; use your own fee). That’s about $184 a month, roughly $2,200 a year before leasing and renewal fees, and an owner who stays five years is worth well over $10,000 in revenue. Spending $800 or $1,000 to win that door can be a great deal. Most companies never calculate it, so they cut the channels that work because the cost per lead looks high.</p>
<!--fig:doors-->
<p>To measure it:</p>
<ol>
<li>Track owner leads separately from tenant inquiries, with tracked numbers per channel and forms tagged by source. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'call and form tracking guide')} covers setup.</li>
<li>Count signed management agreements, and the number of doors each brings (an investor with four houses is four doors).</li>
<li>Divide spend by new doors, per channel, by quarter.</li>
<li>Track door churn. If you win 30 doors a quarter and lose 20, the problem isn’t marketing.</li>
</ol>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Quarter spend</th><th>Owner leads</th><th>Agreements</th><th>New doors</th><th>Cost per door</th></tr></thead>
<tbody>
<tr><td>Google Ads (owner keywords)</td><td>$6,000</td><td>40</td><td>8</td><td>10</td><td>$600</td></tr>
<tr><td>SEO and suburb pages</td><td>$4,500</td><td>30</td><td>7</td><td>9</td><td>$500</td></tr>
<tr><td>Meta retargeting</td><td>$1,500</td><td>20</td><td>2</td><td>2</td><td>$750</td></tr>
<tr><td>Agent and partner referrals</td><td>$600</td><td>12</td><td>6</td><td>8</td><td>$75</td></tr>
</tbody></table></div>
<p>The numbers above are illustrative. Your own will be messier, and they’re still the only ones worth arguing about. A {L('/blog/understanding-cost-per-lead/', 'cost per lead')} that looks bad can be a cost per door that looks great.</p>
<p>If you want a senior strategist to build an owner-acquisition plan around your suburbs and fee structure, <a href="/contact/">get in touch</a>. And if your vendors include movers, our {L(MOVERS, 'moving company marketing guide')} is worth passing along.</p>"""),
        ],
        "faq": [
            ("How do property management companies get new clients?",
             "Most new owner clients come from Google searches for property management plus a suburb, referrals from real estate agents and other professionals, and the company’s reviews and website. The companies that grow fastest publish their fees, offer a human-reviewed rent estimate, build a real page for each suburb they serve, and run search ads only on owner-intent keywords instead of tenant searches."),
            ("Do you need a license to be a property manager in Texas?",
             "Usually. TREC says a license is required when a property manager shows or leases property for an owner for pay, and for anyone who controls the acceptance or deposit of rent from a resident of a single-family home. On-site managers of apartment complexes are exempt, but that exemption doesn’t cover condos or townhomes. Property management companies typically operate under a licensed broker."),
            ("Do Meta housing ad rules apply to property management ads?",
             "They apply to ads for rental listings, which must run in Meta’s Housing special ad category with age, gender, ZIP code and radius restrictions. Ads aimed at owners about your management services generally don’t promote a housing opportunity, though Meta reviewers sometimes flag them. On Google, property management services are on the list of ads that may not have targeting restricted, while single-home listings are."),
            ("How can a property management company deal with bad tenant reviews?",
             "You can’t remove reviews just because they’re from tenants, and you can’t offer incentives or ask only happy people. Instead, ask every owner for a review, ask tenants at good moments like move-in or a fast repair, reply professionally without disclosing private details, and fix the causes, such as unclear deposit deductions or slow maintenance. Report only reviews that actually break Google’s policies."),
            ("How much should a property management company spend to get a new door?",
             "It depends on your fees and how long owners stay. A single-family door renting near the Houston average can bring in a couple thousand dollars a year in management fees, so spending several hundred dollars to win it can pay back within months. Track spend, signed agreements and doors by channel each quarter, and watch churn, since losing doors erases acquisition gains."),
        ],
        "figures": {
            "trec": {
                "type": "checklist",
                "title": "TREC items on a property manager’s site",
                "sub": "What Texas rules require, plus what we’d add",
                "items": ["Broker name on ads, at least half the size of contact info", "IABS link on the homepage, labeled per TREC", "IABS label in at least 10-point font", "Consumer Protection Notice link", "Same links one click from social profiles", "License number on the About page (our add)", "Link to TREC’s license lookup (our add)"],
                "alt": "Checklist of TREC advertising requirements for property management company marketing in Houston and The Woodlands",
                "caption": f"From {SRC['trecsm']} and {SRC['treciabs']}. Confirm details with your broker of record.",
            },
            "areas": {
                "type": "map",
                "title": "Suburb pages worth building",
                "sub": "Where Houston owners search “property management [town]”",
                "highlight": ["Katy", "Cypress", "The Woodlands", "Spring", "Sugar Land", "Pearland", "Kingwood", "Tomball", "Conroe", "Fulshear"],
                "alt": "Map of Houston suburbs for property management company SEO pages, including Katy, Cypress, The Woodlands and Sugar Land",
                "caption": "Build pages only where you actually manage homes, with real local rent and HOA detail.",
            },
            "keywords": {
                "type": "compare",
                "title": "Tenant clicks vs. owner clicks",
                "left": {"title": "Tenant searches (exclude)", "items": ["houses for rent Katy", "apartments near me", "rent to own homes", "cheap houses for rent", "section 8 houses"]},
                "right": {"title": "Owner searches (bid)", "items": ["property management Katy", "rent my house Houston", "tenant placement service", "property manager fees Texas", "out of state owner management"]},
                "alt": "Comparison of tenant and owner keywords for property management Google Ads in Houston and The Woodlands",
                "caption": "Tenant clicks look cheap and never sign a management agreement.",
            },
            "reviews": {
                "type": "steps",
                "title": "Raising a property manager’s rating, legitimately",
                "sub": "What stays inside Google’s rules",
                "steps": [["Ask every owner", "Same link at onboarding and after a lease is signed."], ["Ask every tenant", "At move-in and after a repair is closed."], ["Reply to all", "Calm, specific, no private details."], ["Fix root causes", "Photo-backed deposit itemization, faster repairs."], ["Report violations only", "Harassment and off-topic reviews, nothing else."]],
                "alt": "Steps a Houston property management company can take to improve Google reviews within Google policy",
                "caption": "Ask everyone, the same way. Selective asking breaks the rules.",
            },
            "doors": {
                "type": "funnel",
                "title": "From owner lead to new doors",
                "stages": [["Owner leads", "40"], ["Rent estimates sent", "26"], ["Proposals", "14"], ["Signed agreements", "8"], ["New doors", "10"]],
                "note": "Illustrative example",
                "alt": "Funnel showing owner leads turning into new doors under management for a Houston property management company",
                "caption": "Count doors, not agreements. One investor can bring several.",
            },
        },
    },
]
