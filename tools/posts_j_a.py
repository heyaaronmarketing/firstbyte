"""Batch 10 (module a): solar installer marketing in Houston, painting contractor marketing in Houston, and fence
company marketing in Houston.

Research, solar post: IRS FAQ on the One Big Beautiful Bill Act (Section 25D ends for expenditures made after Dec 31,
2025; installation completion rule); Solar Power World and EnergySage on Section 48E for leases and PPAs (begin
construction by July 4, 2026 or placed in service by Dec 31, 2027); ESS News on storage staying eligible under 48E and
FEOC limits; TDLR press release and "What's in Effect When" page on SB 1036 (Occupations Code ch. 1806, five-business-day
cancellation, registration from Sept 1, 2026, enforcement suspension of 16 TAC 71.41/71.43 until Nov 1, 2026); KPRC
Click2Houston on the law taking effect (deadline extended to Nov 1, 2026; $2,500 per violation, $10,000 for 65+);
CFPB Aug 2024 report on solar loan dealer fees; 12 CFR 1026.24(d) trigger terms; Canary Media on Beryl (2.26 million
CenterPoint customers out); SolarReviews on Texas buyback plans; Google LSA category list (Solar energy contractor,
Painter, Fencing services); Jon Loomer on Meta's Financial products and services category; Morrison Foerster on the
Eleventh Circuit vacating the FCC one-to-one consent rule; CAI summary of Tex. Prop. Code 202.010; Tax Code 11.27.
Painting post: EPA RRP contractors page (firms can't advertise covered work without firm certification; 6/20 sq ft
thresholds); Texas DSHS (EPA administers RRP in Texas); Sherwin-Williams exterior application FAQ (above-dew-point
for 48 hours, avoid direct summer sun, surfactant leaching); The Woodlands Township Residential Standards (house
repainting and color changes need approval; gloss prohibited) and permitting page; My Neighborhood News on Cinco Ranch
II (color changes need ACC approval, up to 30 business days, same-color repaint exempt).
Fence post: Houston Permitting Center (permit for fences over 8 ft or with masonry/concrete; $33.56 admin fee); The
Woodlands Residential Standards sec. 1.5 and 2.6 (more than 8 linear feet replaced needs approval; 7 ft 6 in solid
height; plastic prohibited; finished side out; stains); Texas811 FAQ (two business days, free); NAHB on 2025 lumber
duties (35% AD/CVD plus 10% Section 232); FOX 26 on post-Beryl fence backlogs (6-8 weeks, ~$33/ft); KPRC on who pays
for storm fence damage; Community Impact on post-Beryl permit fee waivers; Nextdoor Ads Manager page.
Competitor/PAA phrasing read for "solar marketing", "solar leads", "solar google ads", "painting contractor marketing",
"how to get more painting jobs", "painting company google ads", "fence company marketing", "how to get more fence
jobs", "fence contractor leads".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # solar post
    "irs": A("https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-act-obbb", "the IRS’s FAQ on the 2025 law"),
    "spw": A("https://www.solarpowerworldonline.com/2025/07/how-does-hr1-change-the-residential-solar-itc/", "Solar Power World"),
    "esage": A("https://www.energysage.com/news/trumps-tax-changes-impact-tpo-solar/", "EnergySage"),
    "essnews": A("https://www.ess-news.com/?p=6002", "ESS News"),
    "tdlr_pr": A("https://www.tdlr.texas.gov/media/pressrelease/2025-09-03-residential-solar-retail-sales-now-regulated-by-tdlr.pdf", "TDLR’s announcement"),
    "tdlr_eff": A("https://www.tdlr.texas.gov/residential-solar-retailers/effect.htm", "TDLR’s “What’s in Effect When” page"),
    "kprc_solar": A("https://www.click2houston.com/news/local/2026/09/02/new-texas-solar-protections-law-takes-effect/", "KPRC 2 reported"),
    "cfpb": A("https://www.consumerfinance.gov/about-us/newsroom/cfpb-report-finds-lenders-cramming-markup-fees-and-confusing-terms-into-solar-energy-loans", "a 2024 CFPB report"),
    "regz": A("https://www.consumerfinance.gov/rules-policy/regulations/1026/24/", "Regulation Z’s advertising rule"),
    "canary": A("https://canarymedia.com/articles/distributed-energy-resources/houstons-post-beryl-outages-highlight-benefits-of-distributed-energy", "Canary Media"),
    "srev": A("https://www.solarreviews.com/blog/texas-net-metering-complete-guide", "SolarReviews’ Texas buyback guide"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "loomer_fin": A("https://www.jonloomer.com/qvt/financial-products-and-services/", "Jon Loomer’s summary"),
    "mofo": A("https://www.mofo.com/resources/insights/250130-eleventh-circuit-vacates-fcc-s-tcpa-one-to-one-consent-rule", "vacated by the Eleventh Circuit in January 2025"),
    "cai": A("https://www.caionline.org/advocacy/advocacy-priorities-overview/solar-rights-and-easements/solar-restrictions-texas/", "Section 202.010 of the Texas Property Code"),
    "tax1127": A("https://texas.public.law/statutes/tex._tax_code_section_11.27", "Texas Tax Code Section 11.27"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary"),
    # painting post
    "epa_rrp": A("https://epa.gov/lead/renovation-repair-and-painting-program-contractors-0", "EPA’s RRP page for contractors"),
    "dshs": A("https://www.dshs.texas.gov/elp/EPA-rules-summary.aspx", "Texas DSHS"),
    "sw": A("https://www.sherwin-williams.com/painting-contractors/tape-masking/resources/faqs/exterior-product-application-faqs", "Sherwin-Williams’ exterior application FAQ"),
    "twp_std": A("https://www.thewoodlandstownship-tx.gov/files/sharedassets/main/v/2/covenant-administration/documents/2024-residential-standards-recorded-12-10-2024.pdf", "The Woodlands Residential Standards"),
    "twp_glance": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/Covenants-Standards/At-a-Glance", "the Township’s standards summary"),
    "twp_permit": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/Permitting-Process", "the Township’s permitting page"),
    "cinco": A("https://myneighborhoodnews.com/exterior-improvements-in-cinco-ranch-ii", "a Cinco Ranch II association notice"),
    # fence post
    "hpc": A("https://www.houstonpermittingcenter.org/hpwcode1145", "the Houston Permitting Center"),
    "tx811": A("https://www.texas811.org/faq", "Texas811"),
    "nahb": A("https://www.nahb.org/advocacy/top-priorities/building-materials-trade-policy/how-tariffs-impact-the-home-building-industry", "NAHB"),
    "fox26": A("https://www.fox26houston.com/news/rebuilding-after-beryl-homeowners-face-long-wait-fence-repairs", "told FOX 26"),
    "kprc_fence": A("https://www.click2houston.com/news/local/2024/07/22/was-your-fence-damaged-during-hurricane-beryl-if-so-whos-responsible-for-paying-for-it-heres-what-we-know", "KPRC 2’s explainer"),
    "ci_beryl": A("https://communityimpact.com/bay-area/real-estate/homeowners-assess-damages-cities-waive-permit-fees-following-hurricane-beryl/", "Community Impact"),
    "nextdoor": A("https://business.nextdoor.com/en-us/advertise-with-nam-2026", "Nextdoor’s Ads Manager page"),
}

SOLAR = "/blog/solar-company-marketing-houston/"
PAINT = "/blog/painting-contractor-marketing-houston/"
FENCE = "/blog/fence-company-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: solar
    {
        "slug": "solar-company-marketing-houston",
        "title": "Solar Company Marketing in Houston After the Tax Credit: A Practical Playbook",
        "seo_title": "Solar Company Marketing in Houston After the Tax Credit",
        "desc": "Solar marketing for Houston installers after 25D ended: battery backup demand, SB 1036 rules, Google Ads keywords, lead vendors, reviews and financing ads.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b1",
        "hero": "bolt",
        "hero_alt": "Illustration of a lightning bolt for solar company marketing in Houston, Cypress and The Woodlands",
        "related": ["roofing-marketing-houston-storm-season", "electrician-marketing-houston-the-woodlands", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>Thursday afternoon, a homeowner in Cypress calls your office. Before you can say hello, she asks if you’re “with the Texas solar program.” Two men knocked on her door last week, told her the state was paying for panels, and left a flyer with no company name on it. She found you on Google because she wanted a second opinion.</p>
<p>That call tells you most of what you need to know about selling solar in Houston right now. Buyers want backup power and lower bills. They also expect to be lied to.</p>
<p>Solar company marketing in Houston works when it sells what’s true in 2026: no homeowner tax credit, buyback rates set by retail electric providers rather than the state, and a battery that keeps the fridge cold when CenterPoint goes down. Paid search should catch people already shopping, reviews should do the convincing, and every claim in an ad should hold up in front of a skeptical spouse. The installers we see winning sound like the calm second opinion. They don’t sound like the guy at the door.</p>
<p>This playbook is for residential installers with one to a few crews in the Houston area, from Katy and Sugar Land up through Spring, The Woodlands and Conroe.</p>"""),

            ("What changed: the 30% homeowner credit is gone, leases and batteries are the new story", f"""<p>For years, the first line of every solar ad in America was “30% federal tax credit.” That line is dead for homeowner-owned systems.</p>
<p>The 2025 tax law ended the Section 25D residential clean energy credit for expenditures made after December 31, 2025, and an expenditure counts as made when installation is complete. A homeowner who paid in December but whose system was finished in January doesn’t get the credit, per {SRC['irs']}. Standalone home batteries bought by the homeowner lost the credit on the same date.</p>
<p>Third-party ownership is different. Leases and power purchase agreements run through Section 48E, the commercial credit, which the solar company claims. As {SRC['spw']} and {SRC['esage']} explain, those systems stay eligible if construction began by July 4, 2026 or the system is placed in service by December 31, 2027. Energy storage got a longer runway under 48E, with projects that begin construction before 2033 remaining eligible, subject to foreign-sourcing limits, according to {SRC['essnews']}.</p>
<p>What that means for your marketing, in plain terms:</p>
<ul>
<li>Pull every “30% tax credit” mention from your ads, landing pages, Google Business Profile posts and old blog posts. A stale credit claim on a page today is a misleading savings claim, and Texas now has a law about those.</li>
<li>If you offer leases or PPAs, you can talk about a lower price that reflects the company’s credit. Say it accurately: the company claims the credit, and the customer gets a lower lease or PPA price.</li>
<li>Talk about the end-of-2027 placed-in-service date only if your financing partner confirms it applies to their product, and tell your sales team the same thing.</li>
<li>Lead with the battery. In Houston, “keep the power on” is a stronger reason to buy than a tax form ever was.</li>
</ul>
<p>Two Texas rules are still worth putting on your site because they answer real objections. {SRC['tax1127']} exempts the added appraised value from a solar device used on site from property tax, and {SRC['cai']} keeps most HOAs from banning roof-mounted panels, with exceptions for things like placement, the developer period and devices installed without approval. In master-planned communities like Bridgeland or Towne Lake, that second one comes up on almost every sales call.</p>"""),

            ("Selling into Texas’s deregulated market: buyback plans and honest savings math", f"""<p>Most Houston homeowners don’t buy electricity from CenterPoint. CenterPoint owns the wires and the meter; the customer picks a retail electric provider. That split decides what a solar customer gets paid for the power they push back to the grid.</p>
<p>Texas has no statewide net metering rule, so buyback terms depend on the provider. {SRC['srev']} found only seven retail electric providers offering some form of solar buyback, out of more than 100 in the state, with plan types that range from credits at the full energy charge, to credits capped at the month’s usage, to real-time market rates that often sit around 3 cents per kWh. Those credits usually exclude delivery charges, which are a big part of a Houston bill.</p>
<p>This is why savings promises get installers in trouble here. A homeowner told “your bill goes to zero” who later sees delivery charges, a buyback cap or a provider changing terms will feel cheated even if the system works perfectly. A Houston-area homeowner {SRC['kprc_solar']} in September 2026 said she was paying $316 a month for panels plus about $150 for electricity, and that her provider cut her credits after the first year.</p>
<p>So the marketing needs a savings story you can defend:</p>
<ul>
<li>Show estimated production in kWh, then show savings as a range under named assumptions (current rate, buyback plan type, usage).</li>
<li>Explain buyback plans on a page of their own. Searches like “solar buyback plans Texas” are real, and a straight explainer earns trust and links.</li>
<li>Never claim a “zero bill.” Say what the system covers and what it doesn’t.</li>
<li>Put the battery’s job in hours, not feelings: which circuits it can carry, and for roughly how long, under a stated load.</li>
</ul>"""),

            ("Beryl and Uri changed the pitch: battery backup sells itself, if you’re specific", f"""<p>Houston has had two very public lessons in what a grid failure feels like. Winter Storm Uri left millions of Texans without power in February 2021. Then Hurricane Beryl knocked out power to about 2.26 million of CenterPoint’s nearly 3 million customers in July 2024, with roughly 130,000 still out more than a week later, per {SRC['canary']}. In the same story, a Houston family with rooftop solar and two batteries kept their food, lights and devices running.</p>
<!--fig:houston-->
<p>Every homeowner in Kingwood, Pearland or Tomball who sat in a hot house that week remembers it. The temptation is to lean on fear. We’d resist it; fear-based storm ads make you look like the door knocker.</p>
<p>What works better is specificity:</p>
<ul>
<li>A short video walking through a real install in Spring or Katy: panel, inverter, battery, the critical-loads panel, and the homeowner flipping the main breaker off while the fridge keeps running.</li>
<li>A “what will my battery run?” page with three example setups (fridge and lights; plus one AC zone; whole home) and honest runtime ranges.</li>
<li>A comparison with a standby generator. Some buyers should get a generator, and saying so earns trust.</li>
<li>Timing. Push battery campaigns in April and May, before hurricane season starts June 1, and again after a big outage when people are researching. Don’t run “Beryl is coming back” ads during an active storm. It reads as opportunism.</li>
</ul>"""),

            ("The trust problem, and how Texas SB 1036 gives honest installers a marketing edge", f"""<p>Residential solar has a reputation problem, and the industry earned it. High-pressure door-to-door sales, flyers implying a government program, savings promises that don’t survive the first summer bill, and financing nobody explained.</p>
<p>Texas responded with Senate Bill 1036, which put residential solar sales under the Texas Department of Licensing and Regulation. Per {SRC['tdlr_pr']} and {SRC['tdlr_eff']}, the contract and cancellation provisions took effect September 1, 2025:</p>
<ul>
<li>Buyers can cancel without penalty by written notice through the fifth business day after signing, and the contract must state the last calendar date to cancel and where to send notice.</li>
<li>Installation must be done by a licensed electrical contractor, named in the contract with a license number (or chosen from a listed set).</li>
<li>If a lender is affiliated with or referred by the retailer, the lender must cancel the loan when the sale is cancelled.</li>
<li>Retailers can’t state or imply they’re affiliated with a utility or government agency, can’t make misleading claims about performance or cost, and can’t solicit at a home with a “no soliciting” sign unless invited.</li>
</ul>
<p>Registration for retailers and salespeople became required on September 1, 2026, and {SRC['kprc_solar']} that the deadline was extended to November 1, 2026, with civil penalties of up to $2,500 per violation (up to $10,000 when a court finds a person over 65 was harmed). TDLR also suspended enforcement of its contract-disclosure and educational-materials rules until November 1, 2026, so those are live now too.</p>
<!--fig:pitch-->
<p>Most installers treat this as paperwork. We’d treat it as copy, because a buyer burned by a door knocker wants proof you’re different:</p>
<ul>
<li>Put your TDLR registration and your electrical contractor’s license number in the site footer, on the quote PDF and on your Google Business Profile description.</li>
<li>Write a “How our contract works” page that explains the five-day cancellation in plain English, with the exact wording you use.</li>
<li>Say “We don’t door-knock” if it’s true. In Houston neighborhoods that have been canvassed hard, it’s one of the strongest lines you can run.</li>
<li>Show the electrician. Name the licensed contractor and show their face on the installation page.</li>
</ul>
<p>We’re marketers, not your lawyer, so have counsel review your contract and scripts. Just don’t hide the compliance work in a drawer.</p>"""),

            ("Google Ads for solar installers: keywords, negatives and copy that survives scrutiny", f"""<p>Search is where the honest installer wins, because the searcher is already doing research. The keyword list should follow what people are actually trying to decide.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Installer near me</td><td>solar installers near me, solar company Houston, solar panel installation Katy</td><td>Service-area page with reviews, license numbers, real installs nearby</td></tr>
<tr><td>Battery backup</td><td>home battery backup Houston, solar battery installation, whole home battery</td><td>Battery page with runtime examples and generator comparison</td></tr>
<tr><td>Cost and savings</td><td>solar panel cost Houston, is solar worth it in Texas, solar buyback plans</td><td>Pricing ranges and buyback explainer</td></tr>
<tr><td>Lease / PPA</td><td>solar lease Texas, solar PPA Houston</td><td>Ownership options page, only if you sell them</td></tr>
<tr><td>Second opinion / repair</td><td>solar panel repair, solar inverter replacement, my solar company went out of business</td><td>Service page for orphaned systems</td></tr>
</tbody></table></div>
<p>That last row is underrated. Installers have gone under, leaving Houston homeowners with systems and no one to call, and that service work often turns into a battery add-on.</p>
<!--fig:negatives-->
<p>Sample responsive search ad lines that stay on the right side of SB 1036 and Google’s misrepresentation policy:</p>
<ul>
<li>“Licensed Houston Solar Installer” / “Battery Backup for Storm Season” / “Real Quotes, No Door-Knocking”</li>
<li>“See What a Battery Can Run” / “5-Day Cancellation in Every Contract” / “Licensed Electricians on Every Install”</li>
<li>Descriptions: “Local crew serving Spring, The Woodlands and Cypress. Written production estimate with your actual usage. No pressure, no surprise fees.”</li>
</ul>
<p>What to keep out: “Texas Solar Program,” “state-approved,” “free solar,” “eliminate your bill,” and any tax credit language for owned systems.</p>
<p>On cost, be ready for expensive clicks. Solar is one of the more competitive home-service categories, with national lead sellers bidding in every metro. We won’t quote a Houston solar CPC here because it moves with the season and the competition, but in accounts we’ve seen it sits well above HVAC and plumbing. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a feel for the local market. Settings that matter: target people “in or regularly in” your service area, not people “interested in” it, and track calls and booked consultations as conversions, not page views. Our {L('/services/search-marketing/', 'search marketing team')} runs this for installers who don’t want to babysit the search terms report.</p>"""),

            ("Local Services Ads and your Google Business Profile", f"""<p>{SRC['lsa']} includes a <b>Solar energy contractor</b> category. Local Services Ads charge per lead rather than per click and sit above the regular ads where available. Availability varies by area, so start the sign-up with your business address to see what you get.</p>
<p>LSA ranking leans on reviews, response rate and your business hours, so an installer with 18 reviews will struggle there. Fix the profile first: a primary category that matches your main work (Google has several solar categories, so pick the installation one if that’s your business), real photos of installs with addresses blurred, your service area drawn around where your crews actually go, and the TDLR registration in the description. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads comparison')} and {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} cover the rest.</p>"""),

            ("Lead vendors and shared leads: what to ask before you buy", f"""<p>Plenty of Houston installers buy leads. Some of those leads come from web forms that promise a “free solar quote” and sell the same person to four or five companies. That’s why the homeowner sounds annoyed when you call: you’re the fourth one that hour.</p>
<p>Before you sign with a vendor, ask:</p>
<ol>
<li>Is the lead exclusive or shared, and with how many buyers?</li>
<li>What did the consumer see when they opted in? Get a screenshot of the actual form and consent language.</li>
<li>What ads drove the form? If the ad said “Texas solar program” or “free panels,” you’re inheriting that misrepresentation.</li>
<li>Can you return bad leads (wrong number, renter, no roof, outside the area), and within how many days?</li>
</ol>
<p>Consent matters because you’ll call and text these people. The FCC’s “one-to-one” consent rule for lead generators was {SRC['mofo']} before it took effect, which means federal rules didn’t tighten the way the industry expected. Texas went its own way: SB 140 brought marketing texts under the state’s telephone solicitation law in September 2025, per {SRC['sb140']}. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'guide to Texas texting rules')} covers what that means; ask your attorney whether registration applies to you.</p>
<p>We’d judge every vendor on cost per signed contract after cancellations, not cost per lead. Five-day cancellations mean a sale isn’t a sale until day six. Our {L('/blog/angi-vs-thumbtack-leads-worth-it-contractors/', 'post on Angi and Thumbtack leads')} applies the same math to the big marketplaces.</p>"""),

            ("Facebook and Instagram: battery stories, not bill-zero promises", f"""<p>Meta reaches homeowners who aren’t searching yet. Put real installs in front of the neighborhoods you already work in, then retarget site visitors with the battery and pricing pages.</p>
<p>Creative that tends to work: a 30-second phone video on a roof in Magnolia, a customer showing the app during a summer afternoon, a crew lead explaining what a critical-loads panel is. Lead forms should ask two or three qualifying questions (own the home, roof age, average electric bill), which costs you volume and saves your closers a lot of wasted driving. Our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'guide to fixing bad Facebook leads')} goes deeper.</p>
<p>A policy note. If an ad leads with a loan (“$0 down, $129 a month”), Meta’s Financial products and services special ad category may apply, which removes age and gender targeting, ZIP code targeting and lookalike audiences, per {SRC['loomer_fin']}. Ads about the system, the battery or the installer usually don’t need it. That’s another reason to keep financing out of the headline.</p>"""),

            ("Financing disclosures: the line most solar ads get wrong", f"""<p>Financing is where solar marketing gets regulators’ attention. {SRC['cfpb']} found lenders adding hidden “dealer fees” that can raise the cost of a loan by 30% or more above the cash price, often left out of the stated APR, and loans structured around a tax credit the borrower might not qualify for. After 25D ended, any ad or proposal still assuming a credit-funded paydown is a problem.</p>
<p>Ad copy has its own rule. Under {SRC['regz']}, if an ad states the number of payments, the repayment period, a payment amount or a finance charge (or a down payment amount, where one is required), it must also disclose the down payment, the repayment terms and the annual percentage rate. “Only $129 a month” in a Facebook ad triggers that. Most installers don’t realize it.</p>
<p>Our advice:</p>
<ul>
<li>Advertise the system and the cash price range. Leave monthly payment numbers for the proposal, where the full disclosures can live.</li>
<li>Show the cash price next to the financed price on every proposal, so the dealer fee isn’t hidden.</li>
<li>Have your finance partner sign off on any ad that mentions a rate, term or payment.</li>
</ul>"""),

            ("Reviews and referrals: your cheapest leads", f"""<p>A solar sale takes trust, so reviews carry more weight here than in most trades. Ask twice: once after installation and once after the customer’s first full summer bill, when the savings are real. The second ask is the one that produces specific reviews (“our August bill was $61”), and those sell better than anything you’ll write.</p>
<p>Follow Google’s rules: same link to every customer, no incentives for reviews, no filtering for happy ones. A referral program is different and fine; you can pay for referred sales, just not for reviews. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has request scripts. A simple text after the first summer works:</p>
<p><i>“Hi Dana, it’s Marcus from [company]. Your system made it through its first Houston summer. If it’s been doing its job, a quick Google review helps neighbors find an installer they can trust: [link]. And if anything isn’t right, call me directly.”</i></p>"""),

            ("Tracking and your first 90 days", f"""<p>Solar has a long sales cycle and a five-day cancellation window, so measure further down the funnel than most trades do. At minimum: tracked call numbers by channel, form fills, booked consultations, proposals sent, signed contracts, contracts still standing after day six, and installs completed. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} covers setup, and the {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} explains why the first five minutes of a lead decide so much.</p>
<!--fig:plan-->
<p>Then judge each channel on cost per installed system. If you want a senior strategist to build a plan around your crews, territory and close rate, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Is the 30% solar tax credit still available in Texas?",
             "Not for homeowner-owned systems. The 2025 tax law ended the Section 25D residential credit for expenditures made after December 31, 2025, and an expenditure counts as made when installation is complete. Leases and power purchase agreements are different, because the solar company claims a commercial credit under Section 48E. Those systems qualify if construction began by July 4, 2026 or the system is placed in service by the end of 2027."),
            ("How do solar companies get leads in Houston?",
             "The main sources are Google search ads and Local Services Ads, the Google Business Profile, Facebook and Instagram ads, referral programs, purchased leads from vendors, and door-to-door canvassing. The highest-quality leads usually come from search and referrals, because those homeowners are already researching. Judge every source on cost per installed system after cancellations, not cost per lead, since shared vendor leads often look cheap and close poorly."),
            ("What does Texas SB 1036 require of solar companies?",
             "SB 1036 put residential solar sales under TDLR. Contracts must give buyers five business days to cancel without penalty and state the last day to cancel. A licensed electrical contractor must do the installation. Sellers can’t imply a utility or government affiliation, make misleading performance or cost claims, or solicit at homes with no-soliciting signs. Retailers and salespeople must register with TDLR, with the deadline extended to November 1, 2026."),
            ("Does Texas have net metering for solar?",
             "Texas has no statewide net metering rule. In deregulated areas like most of Houston, the retail electric provider you choose sets the buyback terms, and only a handful of providers offer solar buyback plans. Plans range from credits at the energy charge rate, to credits capped at monthly usage, to real-time wholesale rates. Credits usually don’t offset delivery charges, so savings estimates should state the plan type assumed."),
            ("Can I advertise a monthly payment in my solar ads?",
             "You can, but it triggers federal disclosure rules. Under Regulation Z, an ad that states a payment amount, the number of payments, the repayment period or a finance charge must also disclose the down payment, the repayment terms and the annual percentage rate. Many installers advertise the system and a cash price range instead, keep monthly payments for the proposal, and have their finance partner approve any ad that mentions rates or terms."),
        ],
        "figures": {
            "houston": {
                "type": "stats",
                "title": "Why Houston buyers want batteries and proof",
                "stats": [["2.26M", "CenterPoint customers lost power in Beryl"], ["12/31/25", "last day for the homeowner credit"], ["5", "business days to cancel under SB 1036"], ["$2,500", "max civil penalty per violation"]],
                "note": "Sources: Canary Media, IRS, TDLR, KPRC 2",
                "alt": "Stats on Hurricane Beryl outages, the end of the 25D credit and Texas SB 1036 for solar company marketing in Houston",
                "caption": f"From {SRC['canary']}, {SRC['irs']}, {SRC['tdlr_eff']} and KPRC 2.",
            },
            "pitch": {
                "type": "compare",
                "title": "The old solar pitch vs. what sells now",
                "left": {"title": "The pitch buyers distrust", "items": ["“Texas solar program” flyers", "30% tax credit on owned systems", "“Your bill goes to zero”", "Monthly payment as the headline", "Door-knocking a no-soliciting home"]},
                "right": {"title": "The pitch that earns calls", "items": ["Named, registered local installer", "Lease credit explained accurately", "Production estimate with assumptions", "Cash price range, full disclosures", "Battery runtime in real hours"]},
                "alt": "Comparison of outdated and trustworthy solar sales messaging for Houston and The Woodlands solar installers",
                "caption": "Most of the right column is just compliance with SB 1036, written as copy.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for solar search ads",
                "sub": "Start with these, then read search terms weekly",
                "items": ["Jobs: jobs, hiring, salary, sales rep, door to door jobs", "DIY: diy, kit, how to install, harbor freight", "Portable: portable, camping, rv, solar generator", "Small solar: solar lights, solar fan, solar charger", "Free: free solar, government program, grant", "Wrong scale: solar farm, land lease, community solar", "Stocks: stock, etf, invest, share price", "Brands you don’t sell or service"],
                "alt": "Checklist of negative keywords for solar installer Google Ads campaigns in Houston and The Woodlands",
                "caption": "“Free solar” searchers are often answering the same misleading ads SB 1036 targets.",
            },
            "plan": {
                "type": "steps",
                "title": "A solar installer’s first 90 days",
                "sub": "Order matters more than budget",
                "steps": [["Days 1-15", "Remove credit claims, add license and TDLR numbers, fix profile."], ["Days 15-30", "Build battery, pricing, buyback and contract pages."], ["Days 30-45", "Launch search ads on battery and near-me terms."], ["Days 45-60", "Start Meta install videos and site retargeting."], ["Days 60-90", "Judge sources on installs after cancellations."]],
                "alt": "Ninety-day marketing plan steps for a residential solar company in Houston and The Woodlands",
                "caption": "Illustrative example. Timing shifts if you’re heading into spring or storm season.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: painting
    {
        "slug": "painting-contractor-marketing-houston",
        "title": "Painting Contractor Marketing in Houston: How to Book More Interior, Exterior and Cabinet Jobs",
        "seo_title": "Painting Contractor Marketing in Houston: Book More Jobs",
        "desc": "Painting contractor marketing for Houston: LSA, Google Ads keywords and negatives, photo-led social, estimate follow-up, HOA color approval and EPA RRP.",
        "category": "Local marketing",
        "icons": ["Instagram", "Google Ads", "Google Business Profile"],
        "art": "b6",
        "hero": "remodel",
        "hero_alt": "Illustration of home improvement tools for painting contractor marketing in Houston, Katy and The Woodlands",
        "related": ["how-to-get-more-remodeling-leads-houston", "kitchen-bath-remodeling-marketing-the-woodlands", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Tuesday in late July. Your exterior crew in Kingwood started at 7 a.m. to beat the sun, quit the south wall at noon because the siding was too hot to touch, and lost the afternoon to a thunderstorm. Meanwhile you have nine estimates out from last week, and you haven’t heard back from seven of them.</p>
<p>Houston painting contractors don’t usually have a lead problem in spring. What they have is a scheduling problem in summer, a follow-up problem all year and a slow stretch in the winter holidays.</p>
<p>Painting contractor marketing in Houston that works does three things. It wins the Google Maps and Local Services Ads results for the work you want most. It shows real before-and-after photos everywhere a homeowner might look. And it follows up on every estimate until you get a yes or a clear no. Add the hooks this market hands you, like HOA color approvals in The Woodlands and Cinco Ranch and lead-safe certification for older homes inside the Loop, and you can fill the calendar in the months other painters go quiet.</p>
<p>This is written for residential painters doing interior, exterior and cabinet work across Greater Houston.</p>"""),

            ("What Houston’s heat and humidity mean for your marketing calendar", f"""<p>Weather sets the painting calendar here more than any ad budget. Paint makers say the same thing. {SRC['sw']} advises that the temperature should stay in the suggested range and above the dew point for at least 48 hours after application, to avoid painting in direct sunlight in hot summer months, and warns that moisture and cool temperatures can cause surfactant leaching, mildew and adhesion problems. It also suggests waiting at least a day after heavy rain.</p>
<p>Anyone who has painted on a humid Houston morning knows what that means in practice. Dew sits on the siding until mid-morning, the west wall is too hot by 2 p.m., and an afternoon storm can wash out a day’s work. Exterior capacity is limited from June through September, and hurricane season (June 1 to November 30) adds rain days and the occasional week when nobody’s thinking about paint.</p>
<!--fig:calendar-->
<p>So plan the marketing calendar around crew capacity, not the other way around:</p>
<ul>
<li><b>January to March:</b> Book exterior work for spring. Run exterior campaigns hard; homeowners decide early here, and spring is the best exterior weather Houston gets.</li>
<li><b>April to May:</b> Exterior demand peaks and HOA approvals stack up. Keep ads on, raise prices before you cut ad spend.</li>
<li><b>June to September:</b> Shift budget to interior and cabinets. Air-conditioned work keeps crews busy, and “interior painters near me” searches stay steady.</li>
<li><b>October to November:</b> Second exterior window. Promote “done before the holidays” interior work and fall exteriors.</li>
<li><b>December:</b> Cabinet refinishing and pre-listing work for spring sellers. Book January exteriors now.</li>
</ul>
<p>Put your weather policy on your website, too. A short page on “what happens if it rains” or “why we start the south side early” answers the question homeowners are too polite to ask and makes your crew look like professionals.</p>"""),

            ("Google Business Profile and Local Services Ads for painters", f"""<p>The map pack is the first fight. Primary category <b>Painter</b> for most residential shops, with secondary categories added only when they match work you actually do. Under Services, list each line separately: interior painting, exterior painting, cabinet painting, drywall repair, fence and deck staining, wallpaper removal. Each one is a search someone runs.</p>
<p>Photos matter more for painters than nearly any other trade. Upload finished jobs every week, with a mix of wide shots, details (cut lines, trim, cabinet doors) and before-and-afters taken from the same spot. Name the neighborhood in the caption: “Exterior repaint in Cinco Ranch, Sherwin-Williams Duration.” Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers the rest of the profile work.</p>
<p>Local Services Ads are worth a test. {SRC['lsa']} includes a <b>Painter</b> category, and you pay per lead instead of per click. Availability varies by area, so start the sign-up with your address. LSA rewards reviews and fast responses, so if you have 11 reviews, build those first. The {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified explainer')} covers the badge and screening process, and {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads')} explains how the two work together.</p>"""),

            ("Google Ads for painting companies: keywords and the negatives that save your budget", f"""<p>Painting searches split cleanly by job type, and each type should have its own ad group and landing page.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>What the landing page needs</th></tr></thead>
<tbody>
<tr><td>Exterior</td><td>exterior house painters Katy, exterior painting The Woodlands, house painters near me</td><td>Exterior gallery, prep process, HOA approval help, weather policy</td></tr>
<tr><td>Interior</td><td>interior painters near me, interior painting Sugar Land, painting contractors Houston</td><td>Interior gallery, how you protect floors and furniture, timeline per room</td></tr>
<tr><td>Cabinets</td><td>cabinet painting Houston, kitchen cabinet refinishing Spring TX, paint kitchen cabinets</td><td>Cabinet process (spray vs. brush), cure times, price range</td></tr>
<tr><td>Older homes</td><td>lead safe painting contractor, painting old house Heights</td><td>RRP certification, how you contain dust, firm certification number</td></tr>
<tr><td>Commercial (optional)</td><td>office painting Houston, commercial painters</td><td>Separate page; don’t mix with residential copy</td></tr>
</tbody></table></div>
<!--fig:negatives-->
<p>Settings worth checking: location targeting set to people “in or regularly in” your service area, ad schedule matched to when someone answers the phone, and call tracking on. A homeowner choosing a painter usually calls or fills a form, then waits to see who shows up first.</p>
<p>Sample ad text for an exterior campaign:</p>
<ul>
<li>Headlines: “Exterior Painters in The Woodlands” / “We Handle the HOA Paperwork” / “Written Estimate in 48 Hours”</li>
<li>Description: “Pressure wash, scrape, prime, two coats. Insured crews, written warranty, daily cleanup. See 200+ finished homes near you.”</li>
</ul>
<p>We won’t quote a Houston painting CPC here, since it shifts by month and neighborhood, but in accounts we’ve seen it’s well below solar or roofing and higher in spring than August. Check our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} for local context, and see our {L('/services/search-marketing/', 'search marketing service')} if you’d rather hand the account off.</p>"""),

            ("HOA color approval: the hook most painters ignore", f"""<p>In Houston’s master-planned communities, the homeowner can’t just pick a color and call you. They need approval, and most of them hate the process. That’s an opportunity.</p>
<p>In The Woodlands, {SRC['twp_std']} list “all roof replacement or house repainting” and exterior color changes among projects requiring prior approval, encourage muted earth tones and prohibit gloss paint; painting brick or masonry needs its own review, per {SRC['twp_glance']}. Applications run through the Township’s online portal, and per {SRC['twp_permit']}, contractors can apply once the owner has registered an account. In Cinco Ranch, {SRC['cinco']} says exterior paint changes need Architectural Control Committee approval before work starts, the committee can take up to 30 business days, and a same-color repaint doesn’t need an application. Bridgeland and other master-planned communities have their own guidelines, so check each association’s documents before promising anything.</p>
<!--fig:hoa-->
<p>Turn that into marketing:</p>
<ul>
<li>Build a page per big community (“Exterior painting in The Woodlands: HOA approval made simple”) explaining the process, the typical timeline, and what you handle.</li>
<li>Offer to prepare the application: color names and codes, a photo of the house, sample swatches, the product sheet. Many homeowners would pay for that alone.</li>
<li>Keep a running list of colors and combinations you’ve had approved in each village or section. That’s content nobody else in town has.</li>
<li>Time your ads to the review calendar. If approvals take weeks, homeowners need to start in February for April work, so your exterior campaigns should start in January.</li>
</ul>
<p>Don’t claim to guarantee approval, and don’t start work before the letter arrives. A crew painting without approval puts the homeowner in violation, and that story spreads fast on neighborhood Facebook groups.</p>"""),

            ("EPA lead-safe (RRP) certification for pre-1978 homes", f"""<p>Plenty of Houston housing predates 1978: much of the Heights, Montrose, Garden Oaks, Oak Forest, Meyerland and Bellaire, plus older parts of Pasadena and Baytown. Painting those homes falls under the EPA’s Renovation, Repair and Painting rule, which {SRC['dshs']} confirms EPA administers directly in Texas.</p>
<p>The rule applies to paid work that disturbs paint in pre-1978 housing and child-occupied facilities, unless the work disturbs 6 square feet or less per room inside or 20 square feet or less outside, or the paint has been tested and documented as lead-free, per {SRC['epa_rrp']}. Firms need EPA firm certification, workers need a certified renovator on the job, and homeowners must get the “Renovate Right” pamphlet before work begins. Window replacement is covered regardless of square footage.</p>
<p>The marketing part is in one sentence on EPA’s page: firms can’t advertise or perform covered renovation work without firm certification. If you aren’t certified, don’t run ads for “historic home painting” in the Heights. If you are, say so prominently:</p>
<ul>
<li>Put your EPA firm certification number on your site and older-home landing page.</li>
<li>Explain your containment in plain English, with photos of plastic sheeting, HEPA vacuums and cleanup verification.</li>
<li>Target pre-1978 neighborhoods with that page and copy. Parents of young children in older homes are specifically worried about lead dust, and most painters never mention it.</li>
</ul>"""),

            ("Photo-led social: Instagram, Facebook and Nextdoor", f"""<p>Painting is the most visual trade there is. Social media is your portfolio, and in our experience the before-and-after reel is the single best piece of content a painter can make.</p>
<p>What works on Instagram and Facebook:</p>
<ul>
<li>Before-and-after shots from the exact same angle. Tripod or a tape mark on the floor.</li>
<li>Short videos: a cabinet door being sprayed, a crisp cut line along a ceiling, a full exterior time-lapse in 20 seconds.</li>
<li>The crew lead explaining one thing: why you prime bare wood, why you caulk before the second coat, why you don’t paint siding at noon in July.</li>
<li>Color stories. “This Spring homeowner went from builder beige to a deep green” gets shared in neighborhood groups.</li>
</ul>
<p>For ads, run your best before-and-afters to homeowners within your service area and retarget website visitors with a gallery carousel. Our {L('/services/paid-social-advertising/', 'paid social team')} handles this, and our {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads guide')} covers the basics.</p>
<p>Nextdoor deserves a mention because neighbors ask for painter recommendations constantly. Claim your business page, ask happy customers to recommend you there, and post finished jobs by neighborhood. Our {L('/blog/is-nextdoor-advertising-worth-it/', 'Nextdoor advertising review')} covers whether paid ads there make sense.</p>"""),

            ("Estimates and follow-up: where painters lose the most money", f"""<p>Back to those seven quiet estimates. Most homeowners get two or three painting bids, and the one who follows up politely and clearly often wins even when they’re not the cheapest. Most painters send one estimate and wait.</p>
<!--fig:followup-->
<p>A simple sequence that we’ve seen work:</p>
<ol>
<li><b>Same day:</b> Send the written estimate by email and text, with photos of the areas you discussed and a link to three similar finished jobs.</li>
<li><b>Day 2:</b> A short text: “Any questions on the estimate? Happy to walk through color options.”</li>
<li><b>Day 5:</b> Something useful: HOA application help, a product comparison, your current start date.</li>
<li><b>Day 10:</b> A call from the estimator. Ask what’s holding them up.</li>
<li><b>Day 30:</b> A final check-in, then move them to a quarterly email list.</li>
</ol>
<p>Write estimates in a way that wins on comparison: itemize prep (pressure wash, scrape, caulk, prime), name the product and sheen, state the number of coats, and include the warranty. A one-line “Paint house exterior: $6,800” loses to a detailed bid at $7,400 more often than painters think.</p>
<p>Speed matters before the estimate too. A homeowner who fills out three forms books the first painter who calls back. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} shows the response times worth aiming for.</p>"""),

            ("Reviews, referrals and repeat work", f"""<p>Painting customers come back. A homeowner who had the exterior done in 2024 needs a kitchen in 2026 and an interior before they sell. Keep a list, and send a short note every six months with a recent project photo.</p>
<p>Ask for a review the day of the final walkthrough, while the house looks perfect. Same link to every customer, no discounts in exchange for reviews, and reply to every one. Reviews that mention the neighborhood, the type of work and the crew lead help most, and they come naturally if the request reminds people what you did. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has templates:</p>
<p><i>“Thanks again for letting us paint your home in Sienna. If you’re happy with how it turned out, a Google review helps other homeowners find us: [link]. If anything needs a touch-up, text me and we’ll be back this week.”</i></p>
<p>Real estate agents and property managers are worth cultivating for interior repaints before listing and between tenants. One agent in The Woodlands or Katy can send a dozen jobs a year.</p>"""),

            ("Budget, tracking and a first-month plan", f"""<p>For a residential painter with two or three crews, here’s an illustrative monthly starting point (these are examples, not quotes or benchmarks):</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Google Ads</td><td>$1,000 to $3,000</td><td>Higher January to May for exteriors</td></tr>
<tr><td>Local Services Ads</td><td>$500 to $1,500</td><td>Once reviews are solid</td></tr>
<tr><td>Meta ads</td><td>$500 to $1,500</td><td>Before-and-after creative and retargeting</td></tr>
<tr><td>Local SEO and profile work</td><td>$500 to $1,500</td><td>Community pages, photos, review replies</td></tr>
<tr><td>CRM and follow-up software</td><td>$50 to $300</td><td>Estimate follow-up automation</td></tr>
</tbody></table></div>
<p>Track calls and forms by source, estimates given, estimates won and revenue per job. Your close rate by source tells you more than cost per lead. If LSA leads close at 40% and Facebook at 15%, the cheaper lead may still be the expensive one. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} covers setup.</p>
<p>First month: fix the Google profile and photos, build the exterior, interior and cabinet pages, write the HOA page for your biggest community, set up the follow-up sequence, then turn on search ads. If you’d like a senior strategist to build that plan around your crews and service area, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do painting contractors get more customers?",
             "Start with a complete Google Business Profile in the Painter category, weekly photos of finished work and a steady flow of reviews. Add Google search ads split by exterior, interior and cabinet work, and test Local Services Ads once reviews are strong. Post before-and-after photos on Instagram, Facebook and Nextdoor. Then follow up on every estimate for at least ten days, since that is where most painters lose jobs."),
            ("What is the best time of year to market exterior painting in Houston?",
             "Start exterior campaigns in January and keep them running through May, because homeowners plan spring work early and HOA approvals can take weeks. Summer heat, humidity and afternoon storms limit exterior work, so shift budget toward interior and cabinet painting from June through September. October and November are a second exterior window, and December is a good time to book January jobs."),
            ("Do painters need EPA lead-safe certification in Texas?",
             "Yes, for most paid work that disturbs paint in homes or child-occupied facilities built before 1978. EPA administers the Renovation, Repair and Painting rule directly in Texas. Firms need EPA firm certification and a certified renovator on the job, unless the work is very small or the paint is documented as lead-free. EPA also says uncertified firms cannot advertise covered work, so certification affects your ads too."),
            ("Do I need HOA approval to paint my house in The Woodlands?",
             "Generally yes. The Woodlands Residential Standards list house repainting and exterior color changes among projects that need prior approval, encourage muted earth tones and prohibit gloss paint. Applications go through the Township’s online portal, and contractors can apply once the owner registers. Other communities differ; Cinco Ranch II, for example, requires approval for color changes but not a same-color repaint. Check your association’s rules first."),
            ("What negative keywords should a painting company use in Google Ads?",
             "Block job seekers (jobs, hiring, painter salary), DIY searches (how to, diy, tutorial, best paint for), retail and product searches (Home Depot, Lowe’s, paint store, paint sprayer), art and hobby terms (canvas, painting classes, portrait, paint and sip), and auto painting if you don’t do it. Then review the search terms report weekly for the first month and keep adding new negatives."),
        ],
        "figures": {
            "calendar": {
                "type": "columns",
                "title": "Where to put painting ad budget through the year",
                "sub": "Share of budget on exterior campaigns, by month",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [70, 80, 85, 80, 70, 35, 25, 25, 35, 65, 55, 30],
                "highlight": [1, 2, 3, 9],
                "y_label": "% exterior",
                "note": "Illustrative example",
                "alt": "Column chart of exterior painting ad budget share by month for a Houston and The Woodlands painting contractor",
                "caption": "Illustrative only. The rest of the budget goes to interior and cabinet campaigns.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for painting contractors",
                "sub": "Add before launch, then review weekly",
                "items": ["Jobs: jobs, hiring, painter salary, apprentice", "DIY: how to, diy, tutorial, youtube", "Products: best paint for, paint colors, sherwin williams store", "Retail: home depot, lowes, paint sprayer, rental", "Art: canvas, portrait, painting classes, paint and sip", "Auto: car painting, auto body, maaco", "Free or cheap only, if you don’t compete on price", "Commercial terms, if you’re residential only"],
                "alt": "Checklist of negative keywords for painting contractor Google Ads in Houston and The Woodlands",
                "caption": "The art and auto negatives catch more waste than most painters expect.",
            },
            "hoa": {
                "type": "steps",
                "title": "Making HOA color approval your sales hook",
                "sub": "What a painter can handle for the homeowner",
                "steps": [["Check the rules", "Pull the community’s standards and approved palettes."], ["Build the packet", "Color names and codes, swatches, product sheet, house photo."], ["Submit early", "Allow weeks; Cinco Ranch II can take 30 business days."], ["Schedule on approval", "No brush touches the house before the letter arrives."], ["Log what passed", "Track approved colors by village for future clients."]],
                "alt": "Steps for handling HOA exterior paint color approval in The Woodlands and Cinco Ranch for painting contractor marketing",
                "caption": "Homeowners hate this paperwork. Offering to handle it wins jobs.",
            },
            "followup": {
                "type": "funnel",
                "title": "Where painting estimates go quiet",
                "stages": [["Leads (calls and forms)", "100"], ["Estimates scheduled", "60"], ["Estimates delivered", "52"], ["Followed up 3+ times", "30"], ["Jobs won", "18"]],
                "note": "Illustrative example",
                "alt": "Funnel showing painting contractor leads to estimates to jobs won for a Houston painting company",
                "caption": "Illustrative numbers. The gap between estimates delivered and followed up is where most painters leak jobs.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: fences
    {
        "slug": "fence-company-marketing-houston",
        "title": "Fence Company Marketing in Houston: More Installs, Fewer Dead Estimates",
        "seo_title": "Fence Company Marketing in Houston: Get More Fence Jobs",
        "desc": "Fence company marketing for Houston: near-me searches, LSA, Google Ads keywords, Nextdoor, yard signs, HOA and permit rules, storm demand and lumber prices.",
        "category": "Local marketing",
        "icons": ["Nextdoor", "Google Ads", "Google Business Profile"],
        "art": "b5",
        "hero": "tools",
        "hero_alt": "Illustration of tools for fence company marketing in Houston, Katy, Spring and The Woodlands",
        "related": ["roofing-marketing-houston-storm-season", "is-nextdoor-advertising-worth-it", "rank-in-google-map-pack-houston"],
        "sections": [
            (None, f"""<p>Monday after a storm. Your phone has 41 missed calls, the voicemail box is full and three neighbors on the same street in Cypress want quotes for one shared fence line. Your estimator can see maybe eight homes a day. Two months later the phone is quiet, cedar pickets cost more than they did in spring, and you’re wondering where all those people went.</p>
<p>Fence companies in Houston live on that cycle. Storms create bursts of demand, the rest of the year is replacement work for fences that have simply rotted or leaned in the clay, and lumber prices move enough to wreck a quote that sits too long.</p>
<p>Fence company marketing in Houston that works keeps a steady flow of “fence installation near me” leads coming from Google Maps, Local Services Ads and search ads, then turns every finished job into the next one with yard signs, Nextdoor recommendations and neighbor offers. It also tracks every estimate to a signed contract, so you know which leads are worth chasing when the phone blows up after the next storm.</p>
<p>This guide is for residential fence contractors working wood, iron and vinyl jobs across Greater Houston.</p>"""),

            ("Why fence demand in Houston comes in waves", f"""<p>Two kinds of fence customers call you. The first has a fence that’s 12 to 15 years old, gray and leaning, and has been meaning to replace it. The second just watched it blow over.</p>
<p>Hurricane Beryl in July 2024 showed how big the second group gets. Sugar Land councilman and fence company owner William Ferguson {SRC['fox26']} his company fielded hundreds of calls in the week after the storm, that some customers would wait six to eight weeks, and that crews couldn’t always get lumber. He also put the average Houston fence at just over $33 a foot. {SRC['kprc_fence']} noted that most Texas policies cover fences as “other structures,” usually paid at actual cash value prorated for age, and that neighbors often split shared-fence costs 50/50 by custom.</p>
<p>Cities react too. After Beryl, League City waived permit fees for fences 8 feet and over, and Bellaire let fence replacement start without a permit, with a no-fee permit afterward, per {SRC['ci_beryl']}.</p>
<p>What that means for marketing:</p>
<ul>
<li>Have a storm page ready before hurricane season: how to document damage for insurance, how neighbor splits work, temporary fixes, your current wait time. Turn it on the day after a storm.</li>
<li>Have a call plan. A full voicemail box after a storm is lost revenue. Add an answering service or a short text auto-reply with a booking link.</li>
<li>Don’t price-gouge, and don’t sound like you are. The same KPRC story quoted a storm attorney warning about contractors charging far more than normal. Homeowners remember.</li>
<li>Build the off-season pipeline. The rotted-fence customer is the one who pays your bills in February. Your marketing should speak to them most of the year.</li>
</ul>"""),

            ("Permits and HOA rules: the Houston and Woodlands specifics", f"""<p>Fence rules in Greater Houston depend on where the house is, and getting them wrong costs you jobs and reviews. Knowing them cold is also great marketing material.</p>
<p><b>City of Houston.</b> Per {SRC['hpc']}, a residential fence permit is needed for fences more than 8 feet above grade, and for any fence made partly or wholly of masonry or concrete regardless of height. There’s a $33.56 admin fee plus base and plan review fees, Planning and Development review, inspections, and a typical processing time of about 10 days. Most standard 6-foot wood fences inside the city don’t need a city permit, but deed restrictions may still apply.</p>
<p><b>The Woodlands.</b> The covenant rules are stricter, and they’re specific. {SRC['twp_std']} require prior approval when more than eight linear feet of fence is replaced, redesigned, rebuilt or relocated. Solid fences top out at 7 feet 6 inches on most lots (8 feet 6 inches for solid wood along the side facing an arterial or major street), transparent fences at 6 feet 6 inches, and the finished side must face out. Acceptable materials are wood, metal, stone and masonry; plastic and fiberglass are on the prohibited list, along with chain link and wire unless screened inside a solid fence. Paint, solid stain or tinted sealant needs approval, while transparent and semi-transparent stains from the Township’s list are pre-approved.</p>
<!--fig:rules-->
<p>That plastic line matters if you sell vinyl. Check the specific village and lot before quoting vinyl anywhere in The Woodlands. Other master-planned communities around Katy, Cypress and Conroe have their own architectural review, and some sit inside small cities (Bellaire, the Memorial villages, Shenandoah) with their own permit rules.</p>
<p>And everywhere: call before you dig. {SRC['tx811']} asks for at least two business days’ notice before digging, the service is free, and they say to contact them no matter how small or shallow the project. Put “we call 811 on every job” on your process page. It sounds obvious, and homeowners still notice.</p>
<p>How to use all this in marketing: build one page per major area (“Fence installation in The Woodlands: what the covenants allow”), and offer to handle the HOA application for the customer. A fence company that knows the 7-foot-6 rule without looking it up wins the estimate.</p>"""),

            ("Winning “fence installation near me” in Google Maps", f"""<p>Most fence searches are local and urgent-ish: “fence company near me,” “fence installation near me,” “fence repair Katy,” “iron fence Pearland.” The map pack takes most of those clicks.</p>
<ul>
<li><b>Primary category:</b> “Fence contractor.” Add secondary categories only for work you really do, such as gates or decks, when Google offers a matching one.</li>
<li><b>Services:</b> List each one separately with a sentence of detail. Cedar privacy fence, pine fence, board-on-board, wrought iron, ornamental aluminum, vinyl, automatic gates, fence repair, fence staining.</li>
<li><b>Photos:</b> Every finished job, ideally with a before shot. Close-ups of post caps, rot boards and gate hardware help homeowners compare quality.</li>
<li><b>Service area:</b> Where your crews actually go. A Tomball shop claiming Pearland and League City confuses Google and customers.</li>
<li><b>Reviews:</b> Ask on the day the gate latches for the first time. More on this below.</li>
</ul>
<p>Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the full process.</p>"""),

            ("Local Services Ads and Google Ads for fence companies", f"""<p>{SRC['lsa']} includes <b>Fencing services</b>, so many Houston fence companies can run pay-per-lead ads above the regular results. Availability varies by area; start the sign-up with your address. As with every LSA category, reviews and response time drive ranking. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads comparison')} explains how to run both.</p>
<p>For regular search ads, split campaigns by material and job type:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Wood privacy</td><td>wood fence installation near me, cedar fence Cypress, privacy fence Spring TX</td><td>Highest volume. Show a price-per-foot range.</td></tr>
<tr><td>Iron and ornamental</td><td>wrought iron fence Sugar Land, aluminum fence installation, iron fence near me</td><td>Higher ticket. Pool-code fences are a niche worth naming.</td></tr>
<tr><td>Vinyl</td><td>vinyl fence installation Houston, vinyl privacy fence</td><td>Exclude areas where HOAs prohibit plastic.</td></tr>
<tr><td>Gates</td><td>automatic gate installation, driveway gate Magnolia</td><td>Bigger rural lots in Magnolia, Montgomery and Waller.</td></tr>
<tr><td>Repair and storm</td><td>fence repair near me, fence blown down, storm fence repair</td><td>Pause or cap when you’re booked out.</td></tr>
</tbody></table></div>
<!--fig:negatives-->
<p>Sample headlines: “Cedar Fences Built in The Woodlands” / “HOA Paperwork Handled for You” / “Written Quote in 48 Hours.” Description: “Board-on-board cedar, steel posts, finished side out. Local crews, 811 called on every job, warranty in writing.”</p>
<p>Settings: target people in or regularly in your service area, schedule ads for hours you answer, and track calls as conversions. When you’re booked six weeks out after a storm, lower budgets or switch ads to “now booking for [month]” rather than paying for calls you can’t serve. Our {L('/services/search-marketing/', 'search marketing team')} sets these accounts up for contractors.</p>"""),

            ("Nextdoor and yard signs: the neighbor effect", f"""<p>Fences are public. Every job you finish is visible from the street and from the neighbor’s yard, and a shared fence line means at least one neighbor is already involved. No other trade gets that much free exposure.</p>
<p><b>Yard signs.</b> Ask permission to leave a sign for two weeks after the install. Use a big phone number, a short URL and one line (“New cedar fence by [company]”). Make sure the HOA allows it. Track signs with their own phone number so you know they work.</p>
<p><b>Neighbor offers.</b> When you finish a fence, knock on (or mail) the five or six houses that can see it, with a photo of the job and an offer on the shared line. Many fences in a subdivision are the same age and fail together.</p>
<p><b>Nextdoor.</b> Homeowners ask Nextdoor for fence recommendations all the time. Claim your business page, ask happy customers to recommend you there, and reply when someone tags you. {SRC['nextdoor']} offers image, video, carousel and lead gen ads with homeownership audiences and customer-list lookalikes. In our experience, paid Nextdoor works best for fence companies when it supports organic recommendations in neighborhoods where you already have finished jobs. Our {L('/blog/is-nextdoor-advertising-worth-it/', 'Nextdoor advertising review')} covers when it’s worth paying for.</p>
<!--fig:neighbor-->"""),

            ("Lumber prices and quotes that don’t lose you money", f"""<p>Wood fences run on lumber, and lumber prices move. Supply matters more than most homeowners realize: per {SRC['nahb']}, Canada supplies roughly 85% of U.S. softwood lumber imports, and in 2025 antidumping and countervailing duties on Canadian lumber rose from 14.5% to 35%, with an additional 10% Section 232 tariff on top.</p>
<p>That’s a pricing problem and a marketing problem. A quote sent in March and signed in June can lose money if picket and post prices moved in between. What we see fence companies do well:</p>
<ul>
<li>Put an expiration date on every quote, typically 15 to 30 days, and say why in plain language.</li>
<li>Show price-per-foot ranges on your website by material, with a “last updated” date, rather than one number you’ll have to defend for a year.</li>
<li>Use rising prices as an honest follow-up reason: “Your quote holds through the 30th; after that we’ll re-price based on current lumber.” That’s real urgency, not a fake sale.</li>
<li>When lumber gets expensive, push materials with steadier pricing (iron, aluminum, steel-post wood hybrids) in your ads and social.</li>
</ul>"""),

            ("Estimate-to-close tracking", f"""<p>Fence companies often measure leads and revenue and nothing in between. The middle is where the money is. Track every lead through these stages: lead (call, form or LSA message), estimate scheduled, estimate delivered, signed contract, deposit paid, installed.</p>
<!--fig:funnel-->
<p>Then look at the numbers by source. In accounts we’ve seen, Nextdoor and referral leads often close at higher rates than search leads, and storm leads close fast but cancel more when wait times stretch. You only learn your own version of that by tracking it. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and call tracking guide')} covers the setup, and {L('/blog/understanding-cost-per-lead/', 'understanding cost per lead')} explains why cost per signed job is the number to manage.</p>
<p>Follow up on every open estimate: a text the next day, a call at day four, and an email when the quote is about to expire. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the timing that tends to work.</p>"""),

            ("Reviews and a first-month plan", f"""<p>Ask for a review when the job is done and the customer has walked the line. Same link to everyone, no discounts for reviews, and reply to every one. A review that says “they handled the HOA application in The Woodlands and finished in two days” is worth more than anything you write. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has scripts. A text that works:</p>
<p><i>“Thanks for choosing us for your new fence. If you’re happy with it, a quick Google review helps your neighbors find us: [link]. And if the gate ever sticks, text me.”</i></p>
<p>A first-month plan for a fence company that wants steadier work:</p>
<ol>
<li>Week 1: Fix the Google Business Profile, add services and photos, set up call tracking.</li>
<li>Week 2: Build material pages and area pages for your top three markets, including HOA and permit details.</li>
<li>Week 3: Launch search ads on wood and iron keywords with the negatives above; start the LSA sign-up.</li>
<li>Week 4: Order yard signs, set up the review text and the estimate follow-up sequence, and write the storm page so it’s ready.</li>
</ol>
<p>If you’d like a senior strategist to build a plan around your crews, materials and service area, <a href="/contact/">get in touch</a>. Our {L(SOLAR, 'solar marketing')} and {L(PAINT, 'painting contractor')} guides cover two trades you probably share customers with.</p>"""),
        ],
        "faq": [
            ("How do fence companies get more customers?",
             "Win the Google Maps results for fence searches near you with a complete profile, weekly job photos and steady reviews. Add Local Services Ads under Fencing services and search ads split by wood, iron, vinyl and gates. Use yard signs and neighbor offers after every install, and ask customers to recommend you on Nextdoor. Track every estimate to a signed contract so you know which sources pay off."),
            ("Do I need a permit to build a fence in Houston?",
             "Inside the City of Houston, a residential fence permit is required for fences more than 8 feet above grade and for any fence that is partly or wholly masonry or concrete. Most standard 6-foot wood fences don’t need a city permit. Deed restrictions and HOA rules may still apply, and nearby cities and villages set their own rules, so check the address before quoting."),
            ("What are the fence rules in The Woodlands?",
             "The Woodlands Residential Standards require prior approval when more than eight linear feet of fence is replaced or changed. Solid fences are generally limited to 7 feet 6 inches, transparent fences to 6 feet 6 inches, and the finished side must face out. Wood, metal, stone and masonry are acceptable, while plastic, fiberglass and unscreened chain link are prohibited. Paint and solid stains need approval."),
            ("What keywords should a fence company use in Google Ads?",
             "Use material and service keywords with a location, such as wood fence installation near me, cedar fence Cypress, wrought iron fence Sugar Land, automatic gate installation or fence repair near me. Split them into ad groups with matching landing pages. Add negatives for DIY searches, retail stores, fence materials for sale, jobs, rentals, and electric or invisible dog fences if you don’t install them."),
            ("How should fence companies handle lumber price changes in quotes?",
             "Put an expiration date on every quote, often 15 to 30 days, and explain that lumber prices change. Show price-per-foot ranges on your website with a last-updated date instead of a single fixed number. Use the quote expiration as an honest follow-up reason, and promote iron or aluminum when wood prices spike. Duties on Canadian lumber rose sharply in 2025, so price swings are likely to continue."),
        ],
        "figures": {
            "rules": {
                "type": "stats",
                "title": "Fence rules worth knowing cold",
                "stats": [["8 ft", "Houston permit threshold for fence height"], ["8 lin. ft", "replaced in The Woodlands triggers approval"], ["7′6″", "max solid fence height on most Woodlands lots"], ["2 days", "business days’ notice to Texas811"]],
                "note": "Sources: Houston Permitting Center, The Woodlands Township, Texas811",
                "alt": "Stats on fence permit and HOA rules in Houston and The Woodlands for fence company marketing",
                "caption": f"From {SRC['hpc']}, {SRC['twp_std']} and {SRC['tx811']}. Check each address; villages and HOAs vary.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for fence company ads",
                "sub": "Add before launch, then review weekly",
                "items": ["DIY: how to build, diy, how to install, calculator", "Retail: home depot, lowes, menards, tractor supply", "Materials for sale: pickets for sale, fence panels, posts price", "Jobs: jobs, hiring, fence installer salary", "Rentals: temporary fence rental, construction fence", "Pets: invisible fence, electric dog fence, if you don’t sell them", "Farm: barbed wire, cattle fence, if you’re residential only", "Legal: fence laws, neighbor dispute, property line"],
                "alt": "Checklist of negative keywords for fence company Google Ads campaigns in Houston and The Woodlands",
                "caption": "Then read the search terms report weekly for the first month.",
            },
            "neighbor": {
                "type": "steps",
                "title": "Turn one fence into the next three",
                "sub": "The neighbor loop after every install",
                "steps": [["Finish and photograph", "Before-and-after from the street and the yard."], ["Sign the yard", "Two weeks, with its own tracked number."], ["Reach the neighbors", "Card or door hanger for the houses that can see it."], ["Ask for a review", "Google first, then a Nextdoor recommendation."], ["Post the job", "Profile photo and social post naming the area."]],
                "alt": "Steps for turning a finished fence install into neighbor referrals in Houston, Cypress and The Woodlands",
                "caption": "Fences age together in a subdivision. The neighbors are often next.",
            },
            "funnel": {
                "type": "funnel",
                "title": "Fence estimates to installs",
                "stages": [["Leads", "120"], ["Estimates scheduled", "80"], ["Estimates delivered", "70"], ["Signed contracts", "28"], ["Installed", "26"]],
                "note": "Illustrative example",
                "alt": "Funnel of fence company leads, estimates, contracts and installs for a Houston fence contractor",
                "caption": "Illustrative numbers. Track your own by source and the right budget moves become obvious.",
            },
        },
    },
]
