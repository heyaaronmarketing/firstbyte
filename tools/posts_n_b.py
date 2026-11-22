"""Batch 14: window and door replacement company marketing in Houston and The Woodlands, and used car dealer
(independent, buy-here-pay-here) marketing in Houston.

Research for the window post: NAHB on Section 25C ending for property placed in service after Dec. 31, 2025 under the
2025 reconciliation law; ENERGY STAR's windows and skylights tax credit page (30%, $600 cap, $1,200 envelope limit,
2023-2025); CenterPoint Energy Houston Electric's residential efficiency page (programs run through contractors, no
window rebate listed, ENERGY STAR windows promoted at up to 31% savings in the Houston zone) and CenterPoint's
Minnesota gas-only window rebate page; TDI windstorm pages (14 first-tier counties, Harris County east of SH 146, WPI-8,
glass replacement exemption, TWIA opening-protection discount); ABC13 on 2,500+ downtown windows and skylights lost in
the May 2024 derecho; Utility Dive on 2.26 million CenterPoint customers out after Beryl; WordStream's 2025 Google Ads
benchmarks (home and home improvement CPC $7.85, CPL $90.92); Google's Local Services Ads category list (window repair
and window cleaning only); CFPB Regulation Z 1026.24 triggering terms; Texas Attorney General on the 3-day right to
cancel home solicitation sales; The Woodlands Township Covenant Administration permitting pages; Jon Loomer on Meta's
Financial Products and Services category; Google Maps prohibited content policy.
Research for the dealer post: Cox Automotive's June 2026 independent-dealer buyer research; Google Merchant Center
vehicle ads overview and vehicle ads policies; Motor1 on Facebook Marketplace ending business-page vehicle listings
(Jan. 2023); Meta Marketing API automotive inventory ads overview; Meta's 2025 out-of-cycle changes (CREDIT replaced by
FINANCIAL_PRODUCTS_SERVICES on Jan. 14, 2025); TxDMV's dealer advertising presentation (43 TAC Chapter 215,
Subchapter F) and 43 TAC 215.250 text; Texas Finance Code 348.006 doc fee notice; OCCC's 2024 doc fee adoption ($225)
and MVSF licensing page; Holland & Knight and NADA on the Fifth Circuit vacating the CARS Rule (Jan. 27, 2025);
Auto Dealer Today on adverse action notices; WardsAuto and Cybersecurity Dive on the FTC Safeguards Rule; Census
QuickFacts for Harris County; Morgan Lewis on Texas SB 140.
Not used (could not verify from a primary page in this session): per-door 25C amounts, any CenterPoint Houston window
incentive, specific TDI inspection requirements for full window replacement, Texas rules on doc fee treatment in
advertised prices.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # window post
    "nahb": A("https://www.nahb.org/blog/2025/07/expiring-energy-tax-credits", "NAHB"),
    "estar": A("https://www.energystar.gov/about/federal_tax_credits/windows_skylights", "ENERGY STAR’s tax credit page"),
    "cnp": A("https://www.centerpointenergy.com/en-us/residential/save-energy-money/electric-efficiency-programs/residential-electric-efficiency?sa=ho", "CenterPoint’s Houston efficiency page"),
    "cnpmn": A("https://www.centerpointenergy.com/en-us/residential/save-energy-money/efficiency-programs-and-rebates/window-rebates?sa=mn", "CenterPoint window rebate page"),
    "tdi": A("https://tdi.texas.gov/tips/need-windstorm-inspection.html", "TDI’s windstorm inspection page"),
    "tdiq": A("https://tdi.texas.gov/WIND/generalquestio.html", "TDI’s windstorm FAQ"),
    "derecho": A("https://abc13.com/post/houston-destructive-storm-aftermath-city-asks-houstonians-avoid/14846869/", "ABC13 reported"),
    "beryl": A("https://www.utilitydive.com/news/texas-restoration-efforts-underway-beryl-almost-3-million-without-power/720816/", "Utility Dive"),
    "ws": A("https://www.wordstream.com/blog/2025-google-ads-benchmarks", "WordStream’s 2025 Google Ads benchmarks"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "regz": A("https://www.consumerfinance.gov/rules-policy/regulations/1026/24/", "Regulation Z, section 1026.24"),
    "oag": A("https://www.texasattorneygeneral.gov/cpd/the-3-day-right-to-cancel-a-purchase", "Texas Attorney General"),
    "twp": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/Permitting-Process", "The Woodlands Township’s permitting page"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy"),
    # dealer post
    "cox": A("https://www.coxautoinc.com/news/new-cox-automotive-research-reveals-independent-dealership-buyers-are-driven-by-necessity-not-aspiration/", "Cox Automotive research released in June 2026"),
    "gva": A("https://support.google.com/merchants/answer/11189169?hl=en", "Google’s vehicle ads overview"),
    "gvap": A("https://support.google.com/merchants/answer/11544533?hl=en", "Google’s vehicle ads policies"),
    "motor1": A("https://www.motor1.com/news/665056/facebook-marketplace-bans-dealers/", "Motor1"),
    "metaauto": A("https://developers.facebook.com/docs/marketing-api/auto-ads/overview", "Meta’s automotive ads documentation"),
    "metaocc": A("https://developers.facebook.com/docs/marketing-api/out-of-cycle-changes/occ-2025", "Meta’s developer changelog"),
    "gfaq": A("https://support.google.com/adspolicy/answer/9997418?hl=en", "Google’s housing, employment and credit policy FAQ"),
    "txdmv": A("https://www.txdmv.gov/sites/default/files/body-files/Dealer_Advertising_Presentation.pdf", "TxDMV’s dealer advertising guide"),
    "tac250": A("https://regulations.justia.com/states/texas/title-43/part-10/chapter-215/subchapter-f/section-215-250", "43 TAC §215.250"),
    "fc348": A("https://texas.public.law/statutes/tex._fin._code_section_348.006", "Texas Finance Code §348.006"),
    "occcfee": A("https://occc.texas.gov/sites/default/files/2024-06/mvsf-docfee-adoption-fc-071124.pdf", "the OCCC’s 2024 rule adoption"),
    "occc": A("https://occc.texas.gov/industry/motor-vehicle-sales-finance-mvsf", "the OCCC’s licensing page"),
    "hk": A("https://hklaw.com/en/insights/publications/2025/02/fifth-circuit-strikes-down-ftcs-auto-retail-scam-rule", "Holland & Knight’s summary"),
    "adt": A("https://www.autodealertodaymagazine.com/articles/when-you-must-issue-an-adverse-action-notice", "Auto Dealer Today"),
    "wards": A("https://www.wardsauto.com/news/archive-wards-dealers-face-new-safeguards-rule-requirement/797662/", "WardsAuto"),
    "csd": A("https://cybersecuritydive.com/news/ftc-car-dealers-data-security-reminder/750915", "Cybersecurity Dive"),
    "census": A("https://www.census.gov/quickfacts/fact/table/harriscountytexas,montgomerycountytexas,houstoncitytexas/PST045224", "Census QuickFacts"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
}

WIN = "/blog/window-door-replacement-marketing-houston-the-woodlands/"
CAR = "/blog/car-dealership-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: windows and doors
    {
        "slug": "window-door-replacement-marketing-houston-the-woodlands",
        "title": "Window and Door Replacement Marketing in Houston and The Woodlands",
        "seo_title": "Window & Door Company Marketing in Houston & The Woodlands",
        "desc": "Marketing for window and door replacement companies in Houston and The Woodlands: Google Ads, impact windows, the end of 25C, financing ads and appointments.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b2",
        "hero": "house",
        "hero_alt": "Illustration of a house for window and door replacement marketing in Houston and The Woodlands",
        "related": ["how-to-get-more-remodeling-leads-houston", "roofing-marketing-houston-storm-season", "solar-company-marketing-houston"],
        "sections": [
            (None, f"""<p>Tuesday, 7:15 p.m., a living room in Kingwood. Your rep has measured 19 windows, laid out the sample corner on the coffee table and walked through the quote. The homeowner likes it. Her husband is in Dallas until Friday. “We’ll talk it over.”</p>
<p>That appointment cost you somewhere north of $300 in ad spend to set, plus the rep’s evening. It will probably never close.</p>
<p>Window and door replacement marketing in Houston and The Woodlands comes down to one number most companies don’t track honestly: cost per <i>sat</i> appointment, meaning a demo where every decision-maker was at the table. Leads are cheap to buy and expensive to waste. The companies that grow here pick narrow, high-intent searches, sell the problem Houston homeowners actually feel (heat, storms, noise, ugly 1980s aluminum frames), and run a confirmation process tight enough that the rep isn’t driving to Kingwood for half a household.</p>
<p>This is how we’d set up marketing for a local window and door company competing with the national brands from Katy to Conroe. It includes the 2026 changes to the tax credit pitch that a lot of websites still haven’t caught up with.</p>"""),

            ("What Houston homeowners are really buying when they replace windows", f"""<p>Nobody wakes up wanting windows. They want the back bedroom to stop hitting 82 degrees at 5 p.m. in August. They want to stop hearing trucks on the Grand Parkway. They want the fogged double-pane units in the breakfast nook gone before they list the house in Cypress.</p>
<p>In the accounts we’ve run for home services companies around Houston, four motivations show up again and again in calls and form comments:</p>
<ul>
<li><b>Heat and the electric bill.</b> West- and south-facing glass in a Houston summer is the most common complaint by a mile. Single-pane aluminum frames from the 1970s and ’80s are still all over older parts of Houston, Spring and Humble.</li>
<li><b>Storms.</b> Houston remembers. In the May 16, 2024 derecho, {SRC['derecho']} that more than 2,500 windows or skylights were lost or damaged in downtown high-rises alone. Two months later, Hurricane Beryl knocked out power to more than 2.26 million CenterPoint customers, per {SRC['beryl']}. A homeowner who sat through either storm thinks about glass differently.</li>
<li><b>Noise.</b> Houses backing onto I-45, the Hardy Toll Road or a busy stretch of FM 1960.</li>
<li><b>Resale and looks.</b> Fogged seals, rotted wood doors, a front entry that looks like 1994.</li>
</ul>
<p>Your ads and landing pages should pick one of these per campaign. “Energy efficient vinyl windows” is a product description. “Back bedroom too hot? We fix that one first” is a reason to call.</p>
<!--fig:season-->"""),

            ("The federal tax credit pitch is over, so update your site", f"""<p>For three years, “30% federal tax credit!” carried a lot of window ads. That credit is gone for new jobs. Under the 2025 reconciliation law, the Section 25C energy efficient home improvement credit ended for property placed in service after December 31, 2025, per {SRC['nahb']}. Before the change it would have run through 2032.</p>
<p>For reference, the old rules were 30% of product cost with a $600 yearly cap for windows and skylights, inside a $1,200 annual limit for envelope improvements, and only for windows that met ENERGY STAR Most Efficient criteria, per {SRC['estar']}. Homeowners who installed in 2025 may still be claiming it on their 2025 return this spring. Nobody installing in 2026 gets it.</p>
<!--fig:credit-->
<p>What we’d do this week:</p>
<ol>
<li>Search your own site for “tax credit,” “25C” and “IRS.” Rewrite every page that implies a current credit.</li>
<li>Pause or edit ad copy, sitelinks and Meta ads that still mention it. Old Performance Max assets are a common hiding spot.</li>
<li>Tell your reps. A homeowner who later learns there was no credit remembers who said there was.</li>
</ol>
<p>Utility rebates are the next thing homeowners ask about, and here Houston is confusing. CenterPoint runs a window rebate page that pays per window, but it’s for natural-gas customers in the Northern Climate Zone with Minnesota installer numbers, per the {SRC['cnpmn']}. It shows up when people in Spring search “CenterPoint window rebate,” and it doesn’t apply to them. {SRC['cnp']} lists programs for HVAC, smart thermostats, insulation and pool pumps, delivered through participating contractors because Texas law keeps CenterPoint from offering them directly to homeowners. It promotes ENERGY STAR windows as saving up to 31% in the Houston zone compared with noncertified products, but it doesn’t list a window rebate. If you want to mention incentives, say “we’ll check what’s currently available for your home” and leave the dollar figures out.</p>"""),

            ("Impact windows and TDI windstorm rules belong in a coastal campaign", f"""<p>A lot of Houston window companies muddle this part of their marketing. They run one “hurricane impact windows” campaign across the whole metro, and the copy hints at code requirements that apply to some customers and not others.</p>
<p>The Texas Department of Insurance treats 14 first-tier coastal counties as a designated catastrophe area, including Brazoria, Galveston, Chambers, Matagorda and Jefferson, plus the part of Harris County east of State Highway 146, per {SRC['tdi']} and {SRC['tdiq']}. In that area, new construction, alterations, additions and repairs have to be built and inspected to TDI’s specifications for the home to qualify for a Texas Windstorm Insurance Association policy. A WPI-8 is the certificate of compliance issued after an inspection during the work. TDI’s own list notes that simply replacing the glass in a window or door doesn’t require an inspection. Whether a full window replacement does is a question for TDI’s Windstorm Inspections Program (800-248-6032, option 3), and we’d have your operations manager get that answer in writing before marketing promises anything.</p>
<p>There’s also a selling point. TWIA offers an optional discount for existing homes that retrofit exterior openings with windborne-debris-resistant products, with each product inspected, per {SRC['tdiq']}. For a homeowner in League City or Dickinson paying TWIA premiums, “ask us whether impact windows could lower your windstorm premium” is a far better hook than “hurricane proof.”</p>
<!--fig:coast-->
<p>So split it:</p>
<ul>
<li><b>Coastal campaign</b> (Galveston County towns like League City, Dickinson and Kemah, Brazoria County towns like Pearland and Alvin, and the parts of Seabrook, La Porte and Baytown east of SH 146, so check each address): impact windows, WPI-8 handling, insurance discounts, before-hurricane-season scheduling. Landing page explains the paperwork in plain English.</li>
<li><b>North and west campaign</b> (The Woodlands, Spring, Conroe, Tomball, Magnolia, Cypress, Katy): impact glass sold on storm peace of mind, security and noise. No hint of a code requirement, because there isn’t one tied to TWIA there.</li>
</ul>
<p>Don’t write “meets Texas windstorm code” unless the product and install method do, and you can show the documentation. Homeowners forward that line to their insurance agent.</p>"""),

            ("Google Ads for window replacement: expensive clicks, so choose the searches", f"""<p>Window and door keywords sit in one of the pricier corners of home services. {SRC['ws']}, based on U.S. search campaigns from April 2024 through March 2025, put the median home and home improvement cost per click at $7.85 and cost per lead at $90.92. In the window accounts we’ve seen, replacement keywords in Houston run well above that category median, especially for “near me” searches in the summer. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} have more context.</p>
<p>At those prices you can’t afford mixed intent. Structure campaigns by what the searcher is ready to buy:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Send them to</th></tr></thead>
<tbody>
<tr><td>Replacement windows</td><td>window replacement Houston, replacement windows The Woodlands, vinyl window replacement Spring TX</td><td>Replacement page with price ranges and a booking form</td></tr>
<tr><td>Impact windows</td><td>impact windows League City, hurricane windows Pearland</td><td>Coastal page with TDI and TWIA explanation</td></tr>
<tr><td>Entry and patio doors</td><td>front door replacement Katy, sliding patio door replacement, french door installation Conroe</td><td>Doors page with photos of local installs</td></tr>
<tr><td>Problem searches</td><td>foggy windows between panes, drafty windows fix, hot room windows</td><td>Article-style page answering repair vs. replace honestly</td></tr>
<tr><td>Brand</td><td>your company name, plus “reviews”</td><td>Homepage or reviews page</td></tr>
</tbody></table></div>
<p>Then the negatives, which matter more here than in almost any trade. “Windows” is also a Microsoft product, a car part and a cleaning service.</p>
<!--fig:negatives-->
<p>Settings worth checking: location targeting set to “Presence: people in or regularly in your included locations,” a radius drawn around where your install crews will actually drive (a crew based in Tomball may not want Pearland jobs), call assets scheduled to answered hours, and conversion tracking on booked appointments rather than form fills. The {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'call and form tracking guide')} walks through the setup.</p>
<p>A quick note on Local Services Ads. {SRC['lsa']} has “Window repair services” and “Window cleaning services,” and no window installation or replacement category. The only door category is garage doors. A replacement company can’t lean on LSA the way a plumber can, which is one more reason regular search has to be tight. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads comparison')} covers the trade-offs for trades that do have both.</p>"""),

            ("Bought leads vs. your own booked appointments", f"""<p>Most window companies in Houston have tried buying leads from a lead aggregator. The pitch is easy: pay per lead, no ad management. The reality, in our experience, is shared leads sold to three or four companies, homeowners who “just wanted a ballpark,” and phone numbers that were typed in by thumb on a phone at a red light. Our {L('/blog/angi-vs-thumbtack-leads-worth-it-contractors/', 'post on paid lead platforms')} goes into the math.</p>
<p>Your own leads cost more per lead and less per sale, usually. The difference is control: you choose the questions on the form, the area, and how fast someone calls back.</p>
<!--fig:funnel-->
<p>The parts that decide whether a lead becomes a sat appointment:</p>
<ul>
<li><b>Speed.</b> Call within five minutes during business hours. After an hour, the homeowner has usually booked whoever called first. See our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')}.</li>
<li><b>The all-owners question.</b> Ask politely at booking whether everyone on the title will be there. “We like to have everyone who’ll make the decision see the samples, so nobody has to relay the details” works fine.</li>
<li><b>Confirmation.</b> A text the day before and a call the morning of. Reschedule rather than send a rep to half a household.</li>
<li><b>Qualifying on the form.</b> Number of windows (a range is fine), homeowner or renter, and timeline. Fewer leads, better appointments.</li>
</ul>
<p>Track sales net of cancellations, too. In Texas, a sale over $25 made somewhere other than the seller’s place of business, including the buyer’s home, is a home solicitation transaction with a three-day right to cancel, and the seller has to tell the buyer about it orally and in writing, per the {SRC['oag']}. If a lead source produces signed contracts that cancel on day three, it isn’t producing sales.</p>"""),

            ("Showroom or in-home: what to promote", f"""<p>Some Houston window companies run a showroom off the Katy Freeway or I-45 and others are in-home only. Both work. The marketing changes, though.</p>
<p>With a showroom, your Google Business Profile can be a storefront with an address and posted hours, which helps you show up in the map pack for searches near that location. Put the showroom on the website with photos of the actual door wall and window displays, and offer “visit the showroom Saturday” as a second call to action for people who aren’t ready to have a stranger measure their house. The {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers the profile side.</p>
<p>In-home only, you’re a service-area business: hide the address, list the cities you serve, and lean harder on reviews and photos of completed jobs. Some companies now offer a short video consult first, with a phone walkaround of the house, then send the rep for measurements. It filters out the tire-kickers and cuts drive time from The Woodlands to Sugar Land.</p>"""),

            ("Financing ads: the words that trigger disclosures", f"""<p>Financing sells windows. A $14,000 job feels different at a monthly number. It’s also where window ads most often break federal rules without anyone noticing.</p>
<p>Under {SRC['regz']}, if a closed-end credit ad states the amount or percentage of a down payment, the number of payments or the repayment period, the amount of any payment, or the amount of any finance charge, it has to also disclose the down payment terms, the repayment terms over the full loan, and the annual percentage rate (using that phrase or “APR”), including whether it can go up. So “Windows from $89 a month!” on a Meta ad without the rest of the terms is a problem. “Financing available, ask for details” isn’t.</p>
<!--fig:financing-->
<p>Practical rules:</p>
<ul>
<li>Get the approved ad language from your finance partner and use it word for word. Deferred-interest and “no payments for 12 months” promos carry their own disclosure rules.</li>
<li>Put the full disclosure on the landing page next to the offer, not in a footer.</li>
<li>On Meta, an ad whose main message is a credit offer may need to run under the Financial Products and Services special ad category. That locks age to 18 to 65+, includes all genders, removes ZIP targeting, requires at least a 15-mile radius and takes away lookalikes, per {SRC['loomer']}. We usually keep financing as a secondary line in the ad and the full offer on the landing page.</li>
</ul>"""),

            ("Reviews: how a local window company beats the national brands", f"""<p>The national window brands have bigger budgets, TV spots and brand recognition. A local Houston company has something they struggle to fake: a crew that lives here, an owner who answers the phone, and reviews that mention The Woodlands, Kingwood and Sugar Land by name. Our {L('/blog/why-local-businesses-outrank-national-brands/', 'post on outranking national brands')} covers the search side.</p>
<p>Review volume is the lever. Window jobs are infrequent, so you can’t wait for reviews to show up on their own. Ask twice:</p>
<ol>
<li>At the end of install day, after the walkthrough, when the house is clean and the homeowner is happy.</li>
<li>Two weeks later, after the first hot afternoon, when they’ve noticed the difference.</li>
</ol>
<p>A text that works: “Hi Karen, it’s Mike from [company]. Thanks again for having our crew out Tuesday. If you have a minute, a Google review helps a small Houston company more than you’d think: [link]. And if anything isn’t right, text me back first and we’ll fix it.”</p>
<p>Stay inside {SRC['gpol']}: no discounts or gift cards for reviews, no asking only the happy customers, and no discouraging negative ones. The {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has more scripts and reply templates.</p>
<p>And photograph every job. Before-and-after pairs from a real Cypress house beat stock photos of a lake house in Minnesota on every channel we’ve tested.</p>"""),

            ("HOA approvals in The Woodlands and the master-planned suburbs", f"""<p>A lot of jobs stall at the HOA. Homeowners in The Woodlands, Kingwood, Cinco Ranch, Bridgeland and most newer Montgomery County subdivisions live under deed restrictions, and a color change on window frames or a new front door style can need sign-off.</p>
<p>In The Woodlands, {SRC['twp']} says any alteration or repair of a structure on a lot with an existing single-family home needs prior written approval, with applications filed through the Township’s Civic Access Portal. Some items in the Residential Development Standards are pre-approved, so check before assuming.</p>
<p>Turn that into marketing. A page titled something like “Window replacement in The Woodlands: what Covenant Administration needs” answers a question nobody else in the market answers, and it ranks for searches the national brands ignore. Offer to prepare the application with spec sheets and color samples. “We handle the HOA paperwork” is a line we’d put in ads in the master-planned areas.</p>"""),

            ("Budget, tracking and the first 90 days", f"""<p>An illustrative starting budget for a local window and door company doing a few million a year in Greater Houston. These are examples, not quotes.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>What it covers</th></tr></thead>
<tbody>
<tr><td>Google Search</td><td>$4,000 to $10,000</td><td>Replacement, impact and door campaigns by area</td></tr>
<tr><td>Meta (Facebook and Instagram)</td><td>$1,500 to $4,000</td><td>Before-and-after video, retargeting, showroom events</td></tr>
<tr><td>SEO and Business Profile</td><td>$1,000 to $2,500</td><td>Area pages, HOA pages, photos, review replies</td></tr>
<tr><td>Call tracking and CRM</td><td>$200 to $600</td><td>Recorded calls, appointment status, source data</td></tr>
</tbody></table></div>
<p>First 30 days: fix the tax credit language, set up call tracking by channel, rebuild the search campaigns around the ad groups above, load the negatives, and write the confirmation script. Days 31 to 60: launch the coastal and north-side landing pages, start the two-touch review requests, and send sat appointments and sales back to Google Ads as offline conversions. Days 61 to 90: cut any campaign or lead source with a poor cost per sat appointment, add Meta retargeting with real install videos, and publish the HOA page.</p>
<p>Judge everything on cost per sat appointment and cost per net sale after cancellations. Cost per lead will tell you a nice story that doesn’t match the bank account. If you want a senior strategist to build that plan around your crews and service area, <a href="/contact/">get in touch</a>. Running an auto lot too? Our {L(CAR, 'used car dealer marketing guide')} is the other post in this batch.</p>"""),
        ],
        "faq": [
            ("How do window companies in Houston get more leads?",
             "Focus Google Ads on high-intent searches like window replacement plus a town name, load heavy negative keywords for cleaning, tint, car windows and Microsoft Windows, and send each search to a matching landing page. Build reviews with two requests per job, track calls by channel, and judge results on sat appointments with all decision-makers present rather than raw lead counts."),
            ("Is the federal tax credit for replacement windows still available?",
             "No, not for new installs. The Section 25C energy efficient home improvement credit ended for property placed in service after December 31, 2025. Under the old rules it covered 30% of qualifying window costs up to $600 a year. Homeowners who installed qualifying windows in 2025 may still claim it on that year's return, so window companies should remove current-credit claims from ads and websites."),
            ("Do impact windows require a windstorm inspection in Houston?",
             "It depends on the address. TDI's windstorm program covers 14 coastal counties and the part of Harris County east of State Highway 146, where work must meet TDI specifications for TWIA coverage. Most of Houston, including The Woodlands, Katy and Cypress, is outside that area. TDI says glass-only replacement doesn't need an inspection; confirm full replacements with TDI's Windstorm Inspections Program."),
            ("What does Google Ads cost for a window replacement company?",
             "WordStream's 2025 benchmarks put the median home and home improvement cost per click at $7.85 and cost per lead at $90.92, and window replacement keywords in Houston often run higher than that median. Many local window companies spend several thousand dollars a month on search. The number that matters is cost per sat appointment and per net sale after the three-day cancellation window."),
            ("Can window companies advertise monthly payments?",
             "Yes, with full disclosures. Under Regulation Z, stating a monthly payment, down payment, number of payments or finance charge in an ad triggers required disclosures: down payment terms, full repayment terms and the APR. Use the exact language your finance partner approves, put the full terms beside the offer on the landing page, and expect Meta to treat credit-focused ads as a special ad category."),
        ],
        "figures": {
            "season": {
                "type": "columns",
                "title": "When Houston homeowners shop for windows",
                "sub": "Relative search and lead demand by month",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [45, 55, 70, 78, 85, 92, 100, 96, 80, 68, 50, 30],
                "highlight": [5, 6, 7],
                "y_label": "Relative demand",
                "note": "Illustrative example based on patterns in home services accounts; storms cause spikes",
                "alt": "Column chart of illustrative monthly demand for window replacement in Houston and The Woodlands, peaking in summer",
                "caption": "Heat drives summer demand, and a big storm can spike any month. Set budgets to move with it.",
            },
            "credit": {
                "type": "stats",
                "title": "What the old 25C credit offered",
                "stats": [["30%", "of qualifying window costs"], ["$600", "yearly cap for windows and skylights"], ["$1,200", "annual limit for envelope items"], ["12/31/2025", "last placed-in-service date"]],
                "note": "Sources: ENERGY STAR, NAHB. Not available for 2026 installs.",
                "alt": "Stat tiles on the expired 25C window tax credit, relevant to window replacement marketing in Houston and The Woodlands",
                "caption": f"Old rules from {SRC['estar']}; end date per {SRC['nahb']}.",
            },
            "coast": {
                "type": "map",
                "title": "Where windstorm rules come into play",
                "sub": "Coastal counties and Harris County east of SH 146",
                "highlight": ["League City", "Pearland"],
                "note": "Stylized. Check TDI’s maps for any specific address.",
                "alt": "Map of Houston coastal areas where TDI windstorm rules affect impact window marketing, compared with The Woodlands and north Houston",
                "caption": f"County list from {SRC['tdi']}. Harris County coverage is limited to the area east of SH 146.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for window companies",
                "sub": "Load these before launch, then check search terms weekly",
                "items": ["Software: microsoft, windows 10, windows 11, laptop, update", "Cars: car window, windshield, auto glass, power window", "Cleaning: window cleaning, washing, squeegee", "Tint and film: tint, tinting, film", "Coverings: blinds, shutters, curtains, shades", "DIY: how to, diy, install yourself, youtube", "Jobs: jobs, hiring, installer salary", "Small fixes: screen repair, window AC (unless you do them)"],
                "alt": "Checklist of negative keywords for window replacement Google Ads in Houston and The Woodlands",
                "caption": "The Microsoft and auto glass lists alone save most accounts real money in week one.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From lead to net sale",
                "stages": [["Leads (calls and forms)", "100"], ["Appointments set", "45"], ["Sat with all owners", "30"], ["Signed contracts", "11"], ["Net sales after 3 days", "10"]],
                "note": "Illustrative example",
                "alt": "Funnel showing leads to sat appointments to net sales for a window and door company in Houston and The Woodlands",
                "caption": "The drop from set to sat is where confirmation calls earn their keep.",
            },
            "financing": {
                "type": "compare",
                "title": "Financing ad copy: risky vs. safer",
                "left": {"title": "Triggers disclosures", "items": ["“Windows from $89/month”", "“Only $0 down”", "“60 easy payments”", "“Low monthly payments” with a number in the image", "Terms buried in the footer"]},
                "right": {"title": "Safer approach", "items": ["“Financing available”", "Full lender-approved terms on the landing page", "APR stated as “annual percentage rate” when terms appear", "Terms shown next to the offer", "Credit-focused Meta ads in the right category"]},
                "alt": "Comparison of risky and safer financing ad copy for window replacement companies in Houston and The Woodlands",
                "caption": f"Triggering terms from {SRC['regz']}. Your lender’s compliance team gets the final word.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: used car dealers
    {
        "slug": "car-dealership-marketing-houston",
        "title": "Used Car Dealer Marketing in Houston: Ads, Listings and the Rules",
        "seo_title": "Used Car Dealer Marketing in Houston: Ads, Listings, Rules",
        "desc": "Used car dealer marketing in Houston: Google vehicle ads, Meta inventory ads, TxDMV advertising rules, financing ad limits, BHPH, Spanish and cost per sale.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b4",
        "hero": "car",
        "hero_alt": "Illustration of a car for used car dealer marketing in Houston, Spring and The Woodlands",
        "related": ["auto-repair-shop-marketing-houston", "hispanic-marketing-houston-spanish-ads-seo", "facebook-lead-ads-bad-leads-fix-quality"],
        "sections": [
            (None, f"""<p>Saturday, 11 a.m., a lot on the North Freeway feeder. Sixty-two cars, two salespeople, and a phone buzzing with Messenger notifications. Forty-one people have asked “is this still available?” about the same 2016 F-150 since Thursday. Three of them will actually show up. One has a $1,500 down payment.</p>
<p>That’s the independent dealer’s marketing problem in a single morning: plenty of attention, very little of it ready to buy.</p>
<p>Used car dealer marketing in Houston works when your inventory shows up where buyers search (Google vehicle ads, listing sites, Meta inventory ads), every ad follows the Texas Department of Motor Vehicles advertising rules, financing messages stay inside federal and Meta limits, and someone follows up with every lead in minutes, in English or Spanish. Then you judge it all by cost per car sold. Cost per lead doesn’t pay the floor plan.</p>
<p>This guide is for independent and buy-here-pay-here dealers from Pasadena to Conroe. Franchise stores have co-op rules and OEM programs that are a different post.</p>"""),

            ("Who buys from Houston’s independent lots", f"""<p>Start with the buyer, because most dealer ads are written for somebody else. {SRC['cox']} on independent-dealer buyers found that 79% said they needed a vehicle rather than simply wanting one, and 77% of buyers of 11- to 20-year-old vehicles had household incomes under $75,000. They averaged 16.5 hours researching online, 77% used third-party listing sites, and 83% started without knowing which vehicle they wanted. Only 21% said they’d return to the same dealer next time.</p>
<!--fig:buyers-->
<p>Read those together. Your buyer is often in a hurry because the old car died, flexible on make and model, budget-driven, and comparing you to five other lots on their phone. They want to know three things fast: is it here, what will it cost me per month and up front, and will you approve me.</p>
<p>Houston adds two more. Harris County is 46.1% Hispanic or Latino, and 45.0% of residents age 5 and up speak a language other than English at home, per {SRC['census']}. And a lot of buyers commute long distances on I-45, US-59 and the Beltway, which is why high-mileage trucks and reliable sedans move and two-seat convertibles sit.</p>"""),

            ("Google vehicle ads: put the inventory in the search results", f"""<p>Google’s vehicle ads show a car’s photo, price, mileage and your dealership name right in Google results, and a click goes to that car’s page on your site. Per {SRC['gva']}, they’re fully released in the U.S., support new and used vehicles from dealers (brokers and private sellers aren’t allowed), and run through Performance Max or Standard Shopping campaigns. You link Google Ads to Merchant Center and to your Google Business Profile.</p>
<p>The fine print from {SRC['gvap']} trips up independents more than franchise stores:</p>
<ul>
<li>The price in your feed has to exactly match the price on the vehicle’s landing page.</li>
<li>Vehicles with title defects, such as salvage titles, aren’t eligible.</li>
<li>You need a valid dealer license where required and a brick-and-mortar location in the state where you list cars.</li>
<li>Each Merchant Center account can list vehicles in only one state.</li>
<li>Mileage must be accurate in both the feed and on the page.</li>
</ul>
<!--fig:setup-->
<p>Most independents get the feed from their website or inventory management provider. Ask yours whether they’re set up for Google vehicle ads, and check that the price your website shows is the same number the feed sends. Mismatches are the most common reason we see cars get disapproved.</p>
<p>Run regular search campaigns next to it for the searches that aren’t about a specific car: “buy here pay here Houston,” “used trucks Pasadena TX,” “car lots that finance near me,” “carros usados en Houston,” “dealer sin crédito Houston” (only if your financing honestly fits that search). Negatives to load on day one: parts, junkyard, salvage, auction, rental, “for rent,” jobs, salesman salary, Carfax free, KBB, “sell my car” (unless you buy cars), and the names of national online retailers. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} will help you set a starting budget.</p>"""),

            ("Facebook Marketplace and Meta inventory ads", f"""<p>Marketplace is where a lot of Houston car shopping happens, and the rules for dealers changed in early 2023. Per {SRC['motor1']}, dealers can no longer publish vehicle listings through a Facebook business page; Meta moved dealers toward paid advertising for used inventory. Individuals selling their own cars weren’t affected.</p>
<p>Plenty of lots still have salespeople post cars from personal profiles. We wouldn’t build a business on that. It can run against Meta’s commerce rules, the listings aren’t tracked, and when that salesperson leaves, their Marketplace audience leaves with them.</p>
<p>The paid route is automotive inventory ads. You upload a vehicle catalog, and Meta shows relevant cars from your inventory to people whose activity suggests interest, per {SRC['metaauto']}. Meta recommends optimizing toward vehicle detail page views and measured actions through the Meta Pixel. In practice:</p>
<ul>
<li>Keep the catalog synced daily so sold cars drop out. Nothing burns a lead faster than “sorry, that one just sold” on a car you’re still paying to advertise.</li>
<li>Use real lot photos, front three-quarter first. Twenty photos per car beats six.</li>
<li>Put the price, mileage and a short honest description in the catalog fields.</li>
<li>Retarget people who viewed a car on your site with that car, plus similar ones in their price range.</li>
</ul>
<p>Messenger leads are high volume and low intent. Set up an instant reply that asks for a phone number and offers a test drive time, and route them into the same CRM as everything else. Our post on {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'fixing bad Facebook leads')} covers form questions that cut the noise. If you’d rather hand off Meta, that’s our {L('/services/paid-social-advertising/', 'paid social team')}.</p>"""),

            ("Financing ads on Meta and Google: the special category rules", f"""<p>Once an ad is about credit (“we finance everyone,” “bad credit OK,” “$500 down drives today”), the platforms treat it differently from an inventory ad.</p>
<p>On Meta, the old Credit special ad category was replaced by Financial Products and Services on January 14, 2025, per {SRC['metaocc']}. Ads promoting credit opportunities, including auto loans, fall under it. Age is locked to 18 to 65+, gender to all, location targeting must include a 15-mile radius around any point, ZIP code targeting is gone, many detailed targeting options disappear, and lookalike and saved audiences aren’t available, per {SRC['loomer']}. For a dealer in Humble, a 15-mile minimum radius reaches a long way into Houston.</p>
<p>Google applies similar restrictions to credit ads in the U.S.: no targeting or excluding by age, gender, parental status or marital status, and no ZIP code targeting, per {SRC['gfaq']}.</p>
<p>So let the creative do the targeting. A video of the actual lot with a salesperson saying, in Spanish and English, “first job, no credit history, come talk to us” finds the right people without a demographic filter. Keep the inventory ads in their own campaigns with normal targeting, and keep financing ads in the special category. Mixing them is how ad accounts get restricted.</p>"""),

            ("TxDMV advertising rules every Texas dealer ad has to follow", f"""<p>Texas has detailed dealer advertising rules in 43 Texas Administrative Code Chapter 215, Subchapter F, and they apply to internet and social ads, not just newspaper ads. {SRC['txdmv']} summarizes them. The ones independents break most:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Rule</th><th>What it means for your ads</th></tr></thead>
<tbody>
<tr><td>§215.250, featured price</td><td>The advertised price must be available to any retail buyer and include dealer prep and markup. Only taxes, title, registration and license fees, and other fees expressly allowed by law can be excluded. No “with trade” or “with dealer-arranged financing” qualifiers.</td></tr>
<tr><td>§215.250, “internet price”</td><td>Terms like “internet price” or “e-price” that imply a different price online are prohibited.</td></tr>
<tr><td>§215.250, savings claims</td><td>Savings claims are allowed only on new vehicles. No “Was $18,995, now $15,995” or book-value comparisons on used cars.</td></tr>
<tr><td>§215.245, availability</td><td>Price ads for a specific vehicle need the stock number or VIN, and a used car can only be advertised once you have it and the title is assigned to you.</td></tr>
<tr><td>§215.251 and §215.254</td><td>Disclose year, make, model and say “used” or “pre-owned.” “Program car” alone doesn’t count.</td></tr>
<tr><td>§215.247</td><td>“Everybody financed” and “guaranteed approval” are prohibited statements.</td></tr>
<tr><td>§215.263, financing terms</td><td>Mentioning a down payment, payment amount, number of payments, term or finance charge requires the down payment, repayment terms and APR.</td></tr>
<tr><td>§215.266, superlatives</td><td>“Lowest price in Houston” and “best deal” are out. “Meet or beat” offers must disclose the conditions.</td></tr>
</tbody></table></div>
<p>Per the same guide, an online disclosure can work on hover or one click away if the ad clearly says where to click and the disclosure sits close to the claim. The Board can impose civil penalties of up to $10,000 per violation, with each day counting as a separate violation, though a first violation generally gets a cure letter. The full text of {SRC['tac250']} is worth printing for whoever writes your ads.</p>
<!--fig:copy-->
<p>Doc fees come up constantly. Under {SRC['fc348']}, you must charge the doc fee to cash and credit buyers alike, the buyer’s order and contract must carry the required notice (“A documentary fee is not an official fee...”), and the notice must be posted where sales are finalized. A Texas fee of $225 or less needs no cost filing with the Office of Consumer Credit Commissioner, per {SRC['occcfee']}. How the doc fee interacts with your advertised price under §215.250 is a question to put to your dealer association or attorney, and the answer should go in writing to whoever builds your ads.</p>"""),

            ("The FTC CARS Rule is gone. Deceptive-ad enforcement isn’t.", f"""<p>The FTC’s Combating Auto Retail Scams (CARS) Rule would have required offering price disclosures and banned certain add-on practices. On January 27, 2025, the Fifth Circuit vacated it 2-1 before it took effect, finding the FTC skipped a required advance notice of proposed rulemaking, per {SRC['hk']}. The court didn’t rule on the substance.</p>
<p>That doesn’t make hidden fees and bait pricing legal. The FTC has continued to go after dealers over misleading financing terms, add-on charges and bait-and-switch ads, and state regulators work alongside it, per the same summary. In Texas, TxDMV’s own rules already ban most of what the CARS Rule targeted in ads. Write your ads as if a buyer will screenshot them and bring them to the desk, because they will.</p>"""),

            ("Credit applications: FCRA, Reg B and the Safeguards Rule", f"""<p>A lot of independent dealer websites have a “get pre-approved” form that collects a Social Security number, date of birth and income, then emails it to a Gmail inbox. That form is a compliance problem dressed up as a lead magnet.</p>
<p>Three things to know, none of them legal advice:</p>
<ul>
<li><b>Adverse action notices.</b> Most dealers count as creditors under the Equal Credit Opportunity Act because they participate in credit decisions. Notices are required when credit is denied, not offered on the terms requested, or when an application isn’t submitted for approval at all, and courts have said a lender’s notice doesn’t cover the dealer’s obligation, per {SRC['adt']}. If your website collects an application and nobody acts on it, that can be an adverse action.</li>
<li><b>“Pre-approved” language.</b> Don’t promise approval in ads or on forms. Texas bans “guaranteed approval,” and federal credit-reporting rules govern prescreened offers. Let your compliance vendor write those words.</li>
<li><b>The FTC Safeguards Rule.</b> It covers car dealers who finance or lease, requires encryption of customer information at rest and in transit, and since May 13, 2024 requires notifying the FTC within 30 days of a breach involving 500 or more customers’ unencrypted information, per {SRC['wards']}. In June 2025 the FTC reminded dealers that they must also oversee their service providers, per {SRC['csd']}. Your website host, form plugin, CRM and marketing agency are service providers.</li>
</ul>
<!--fig:creditapp-->
<p>The fix is usually simple: send credit applications through your F&amp;I or credit-app provider’s secure form, keep your marketing forms to name, phone, email and the car they’re interested in, and make sure nobody forwards applications by email.</p>"""),

            ("Buy-here-pay-here and Spanish-language buyers", f"""<p>If you hold the paper, you’re a lender as well as a retailer. Texas requires a Motor Vehicle Sales Finance license from the OCCC for businesses that hold retail installment contracts, as in a buy-here-pay-here model, even when no finance charge is charged, per {SRC['occc']}. Your marketing should match that seriousness.</p>
<p>BHPH ads that work in Houston tend to be specific about the process and quiet about promises: what documents to bring (pay stubs, proof of residence, references), how long approval takes, how payments work (weekly or biweekly, in person or by app), and what the cars are. Skip “no credit check” unless it’s literally true and your attorney is fine with it. And remember that a down payment amount is a triggering term, so “$500 down” in an ad needs the full financing disclosures.</p>
<p>For Spanish-speaking buyers, a translated homepage isn’t enough. What we’d set up:</p>
<ul>
<li>Spanish search campaigns with Spanish ad copy and a Spanish landing page, not Google’s auto-translate.</li>
<li>A bilingual person answering the phone and Messenger on Saturdays, the busiest day for most lots.</li>
<li>Spanish versions of every financing disclosure in a Spanish ad. That’s our view of the safer course.</li>
<li>Paperwork that matches the conversation. Texas law already requires that if the sales presentation is in a different language than the contract, the buyer gets a written copy of the doc fee notice in the language used, per {SRC['fc348']}.</li>
</ul>
<p>Our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'guide to Hispanic marketing in Houston')} goes deeper on bilingual campaigns and why matching the customer’s chosen language beats guessing from a last name.</p>"""),

            ("Reviews and CRM follow-up: where most car sales are won or lost", f"""<p>Buyers shopping five lots read reviews on all five. Ask every buyer on delivery day, by text, while they’re still in the car: “Thanks for buying from us today. If we did right by you, a Google review helps a lot: [link].” Ask service and BHPH payment customers too, since they visit more often. Stay inside {SRC['gpol']}: no gas cards for reviews, and no sending the link only to happy buyers. Reply to every negative review with specifics and a name to call. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has templates, and {L('/blog/fake-reviews-rule-local-businesses/', 'the FTC fake reviews rule')} explains what not to do.</p>
<p>Then follow-up. A lead from a Google vehicle ad at 9 p.m. Thursday needs a reply that night, by text if they asked for text, with the car’s photos and a test drive time. Every lead goes into one CRM tagged with source and stock number, so you can tell which channel sold which car. Set tasks for day 1, 3, 7 and 14, then move cold leads into a monthly “new arrivals in your price range” email. See our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} for scripts.</p>
<p>Texting is regulated. Texas brought marketing texts under its telephone solicitation law through SB 140, effective September 1, 2025, with registration requirements and a private right of action, though some exemptions apply, per {SRC['sb140']}. Get consent for marketing texts separate from transaction updates, and our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} covers the rest.</p>"""),

            ("Cost per sale: the only number that matters", f"""<p>Divide total marketing spend for a channel by the cars it sold in the same month (matched by phone, email or stock number in the CRM). That’s cost per sale. Below is an illustrative month for a 60-car independent lot. The numbers are made up to show the method, not benchmarks.</p>
<!--fig:cps-->
<p>Two things usually show up once dealers measure this way. Listing sites look expensive per lead and fine per sale. Messenger looks cheap per lead and mediocre per sale. Neither is obvious from the ad dashboards.</p>
<p>A first 90 days we’d run: month one, audit every live ad against the TxDMV table above, fix feed and landing page price mismatches, move credit apps to a secure form, and set up call tracking. Month two, launch Google vehicle ads and Meta inventory ads with a daily catalog sync, split financing ads into the special categories, and start delivery-day review requests. Month three, add Spanish search campaigns and landing pages, build the CRM follow-up cadence, and cut whatever has the worst cost per sale. Our {L('/services/search-marketing/', 'search marketing team')} handles the Google side for dealers who’d rather sell cars.</p>
<p>If you want a senior strategist to build that plan around your lot, inventory and financing model, <a href="/contact/">get in touch</a>. And if you also run a service bay, our {L('/blog/auto-repair-shop-marketing-houston/', 'auto repair shop marketing guide')} picks up from there.</p>"""),
        ],
        "faq": [
            ("How do used car dealers in Houston get more customers?",
             "List every car where Houston buyers search: Google vehicle ads, major listing sites and Meta automotive inventory ads, with prices that match your website exactly. Run search campaigns for financing and Spanish-language searches, keep every ad inside TxDMV advertising rules, answer leads within minutes in the buyer's language, ask every buyer for a Google review on delivery day, and measure cost per car sold."),
            ("Can independent dealers use Google vehicle ads in Texas?",
             "Yes. Google vehicle ads are fully released in the U.S. for new and used vehicles from dealers. You need Merchant Center linked to Google Ads and your Business Profile, a valid dealer license, a physical location in the state, prices that match the landing page exactly, and no salvage or other title-defect vehicles. Each Merchant Center account can list cars in only one state."),
            ("Is the FTC CARS Rule in effect for car dealers?",
             "No. The Fifth Circuit vacated the FTC's CARS Rule on January 27, 2025, before it took effect, because the FTC skipped a required advance notice of proposed rulemaking. The court did not rule on the substance. The FTC and state regulators still pursue deceptive pricing and financing ads, and Texas dealers must follow TxDMV advertising rules in 43 TAC Chapter 215."),
            ("Can a Texas dealer advertise guaranteed approval or a Was/Now price on a used car?",
             "No. TxDMV's advertising rules prohibit statements like guaranteed approval and everybody financed, and savings claims such as Was and Now prices are allowed only on new vehicles. Advertised prices must be available to every retail buyer, can't require a trade or dealer financing, and can exclude only taxes, title, registration and license fees, and other fees expressly allowed by law."),
            ("Do car financing ads on Facebook have targeting limits in Houston?",
             "Yes. Ads promoting auto loans or other credit run under Meta's Financial Products and Services special ad category, which replaced the Credit category in January 2025. Age is locked to 18 to 65+, all genders are included, ZIP targeting is removed, location targeting needs at least a 15-mile radius, and lookalike audiences aren't available. Inventory ads without credit offers can run separately."),
        ],
        "figures": {
            "buyers": {
                "type": "stats",
                "title": "Who buys from independent dealers",
                "stats": [["79%", "needed a vehicle rather than wanted one"], ["16.5 hrs", "average time researching online"], ["77%", "used third-party listing sites"], ["21%", "would return to the same dealer"]],
                "note": "Source: Cox Automotive, independent dealer buyer research, June 2026",
                "alt": "Stat tiles on independent used car buyers, context for used car dealer marketing in Houston",
                "caption": f"From {SRC['cox']}.",
            },
            "setup": {
                "type": "steps",
                "title": "Getting Google vehicle ads running",
                "sub": "For an independent dealer in Houston",
                "steps": [["Merchant Center", "Create it and enable the vehicle ads add-on."], ["Link accounts", "Connect Google Ads and your Business Profile."], ["Vehicle feed", "From your website or inventory provider, synced daily."], ["Match prices", "Feed price equals the landing page price, exactly."], ["Campaign", "Performance Max or Standard Shopping, tracked to leads."]],
                "alt": "Five steps to set up Google vehicle ads for a used car dealer in Houston and The Woodlands",
                "caption": f"Requirements from {SRC['gva']} and {SRC['gvap']}.",
            },
            "copy": {
                "type": "compare",
                "title": "Texas dealer ad copy: risky vs. compliant",
                "left": {"title": "Breaks TxDMV rules", "items": ["“Guaranteed approval!”", "“Was $18,995, now $15,995” on a used car", "“Internet price $12,900”", "“Lowest prices in Houston”", "“$249/mo” with no APR or terms", "“$13,500 with trade”"]},
                "right": {"title": "Safer version", "items": ["“Financing options for many credit situations”", "One price, available to every buyer", "Same price online and on the lot", "Specific, provable claims", "Payment shown with down payment, term and APR", "Stock number or VIN on single-car price ads"]},
                "alt": "Comparison of risky and compliant car dealer ad copy under TxDMV rules for used car dealer marketing in Houston",
                "caption": f"Based on {SRC['txdmv']}. Have your attorney review templates once, then reuse them.",
            },
            "creditapp": {
                "type": "checklist",
                "title": "Credit app and lead data hygiene",
                "sub": "What we check on a dealer website",
                "items": ["Credit apps only through a secure, encrypted provider form", "Marketing forms ask name, phone, email and vehicle only", "No applications forwarded by email", "No “guaranteed” or “pre-approved” promises", "Process for adverse action notices on every app", "Service provider list kept for the Safeguards Rule", "Separate consent for marketing texts"],
                "alt": "Checklist for credit application and lead data handling for used car dealers in Houston",
                "caption": "Not legal advice. Your compliance provider should sign off.",
            },
            "cps": {
                "type": "bars",
                "title": "Example cost per car sold by channel",
                "sub": "Illustrative month, 60-car independent lot",
                "items": [["Google vehicle ads", 310, "$310"], ["Google search", 380, "$380"], ["Listing sites", 420, "$420"], ["Meta inventory ads", 460, "$460"], ["Messenger leads", 540, "$540"]],
                "highlight": [0],
                "note": "Illustrative example, not a benchmark",
                "alt": "Bar chart of illustrative cost per car sold by marketing channel for a used car dealer in Houston",
                "caption": "Your order will differ. The point is to measure cost per sale, not cost per lead.",
            },
        },
    },
]
