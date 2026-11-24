"""Batch 15: home inspector marketing in Houston and The Woodlands, and locksmith marketing in Houston.

Research (inspector post): 22 TAC 535.221 (inspector advertisements: name or registered DBA plus license number on every
ad, including reports, websites on one prominent page, social profile pages; sponsored inspectors name their sponsor);
22 TAC 535.220(b)(3) and (e) (independence; no inspection where compensation or future referrals depend on findings; no
fees or valuable consideration to or from settlement service providers, including agents and brokers, for referrals
or for inclusion on preferred lists); TREC articles on inspector DBAs (Feb 16, 2024) and broker preferred-provider lists
(Sept 17, 2019; paid lists allowed only at market advertising rates with the ranking basis disclosed); TREC inspector
FAQ on advertising WDI inspections without a license; 4 TAC 7.175 (official WDI inspection must be done by a certified
applicator or technician licensed in the Termite and Wood Destroying Insect category, TDA Structural Pest Control
Service); 22 TAC 535.233 (pools, spas, sprinklers, outbuildings, wells and septic are optional systems); Spectora on the
separate Texas WDI form vs. TREC REI 7-6; Google LSA category list (Home inspector listed; Google Verified badge);
HAR September 2026 release (7,030 single-family sales, down 5.7%; 5.5 months of supply; 40,192 active listings; 58 days
on market); My Neighborhood News on HAR's October 2026 update (6,348 sales, down 14.9%; $320,000 median; 7.33% average
rate); KPRC Click2Houston (Sept 2026) on Houston clay shrink-swell and foundation repair costs; Texas Tribune on SB 339
(2019 flood disclosure, Harvey structures outside floodplains).
Research (locksmith post): Google Ads Advanced Verification help page (all US and Canada locksmiths, video call at the
business location, required licenses, typically 6-8 weeks); Google Ads local services restricted-business policy;
Google LSA category list (Locksmiths listed; no pre-badge ads for locksmiths); Google Security Blog 2017 research on
fake Maps listings (fewer than 0.5% of local searches, about 2 in 5 fake listings were contractors like locksmiths,
70% drop from June 2015 peak); Search Engine Land on the NYT fake-locksmith story ($35-$90 phone quotes, 3-4x on site);
Texas House Research Organization analysis of SB 616 (Private Security Board abolished, functions moved to DPS,
advisory committee, Sept 1, 2019); DPS license types (Class B Security Contractor company license covering locksmith
and electronic access; individual Locksmith license, affiliated with a licensed company); Tex. Occ. Code 1702.1056 and
1702.131; 37 TAC 35.8, 35.9, 35.123, 35.172; DPS guidance on tow companies under the Locks & Locksmiths heading; BBB
scam alert (July 2020); InvestigateTV/KBTX (July 2025) on BBB complaint counts and overcharges; KPRC (2015) Katy $19
locksmith case; FTC 2008 locksmith caution release; WordStream/LocaliQ 2026 benchmarks (Home & Home Improvement CPC
$8.33, CPL $90.92).
Not used (couldn't verify): Google Business Profile guideline text (page wouldn't load; linked our own post instead),
locksmith-specific CPC averages, count of TREC-licensed inspectors in Harris and Montgomery counties.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # inspector post
    "t221": A("https://regulations.justia.com/states/texas/title-22/part-23/chapter-535/subchapter-r/section-535-221", "TREC Rule 535.221"),
    "t220": A("https://regulations.justia.com/states/texas/title-22/part-23/chapter-535/subchapter-r/section-535-220", "TREC Rule 535.220"),
    "tdba": A("https://www.trec.texas.gov/article/advertising-rules-inspectors-dbas-and-more", "TREC’s 2024 article on inspector DBAs"),
    "tlist": A("https://www.trec.texas.gov/article/brokers-and-preferred-lists-service-providers-%E2%80%93-what%E2%80%99s-allowed-now%C2%A0", "TREC’s guidance on preferred provider lists"),
    "twdi": A("https://www.trec.texas.gov/node/548", "TREC’s inspector FAQ"),
    "tda": A("https://regulations.justia.com/states/texas/title-4/part-1/chapter-7/subchapter-h/division-5/section-7-175", "4 TAC 7.175"),
    "sop": A("https://regulations.justia.com/states/texas/title-22/part-23/chapter-535/subchapter-r/section-535-233", "TREC Rule 535.233"),
    "spec": A("https://www.spectora.com/r/texas-wdi-reports-what-trec-and-the-tda-require-and-how-to-file-one", "Spectora’s Texas WDI explainer"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "har": A("https://www.har.com/s/mrz7p4brVEcM", "HAR’s September 2026 market report"),
    "haroct": A("https://myneighborhoodnews.com/houston-area-home-sales-drop-149-in-october-2026-as-housing-supply-reaches-14-year-high", "My Neighborhood News’ summary of HAR’s October report"),
    "clay": A("https://www.click2houston.com/news/local/2026/09/18/should-you-water-your-foundation-houston-experts-explain-why-it-may-save-you-thousands/", "KPRC reported in September 2026"),
    "sb339": A("https://www.texastribune.org/2019/08/22/texas-law-requires-buyers-to-disclose-flood-risks/", "the Texas Tribune"),
    # locksmith post
    "av": A("https://support.google.com/google-ads/answer/7167635", "Google’s Advanced Verification page"),
    "gpol": A("https://support.google.com/adspolicy/answer/13527633?hl=en", "Google’s local services ad policy"),
    "gsec": A("https://security.googleblog.com/2017/04/new-research-keeping-fake-listings-off.html", "Google’s own 2017 research"),
    "sel": A("https://searchengineland.com/googles-fake-locksmith-problem-once-again-hits-the-new-york-times-241473", "Search Engine Land"),
    "kprc": A("https://www.click2houston.com/news/2015/03/06/katy-woman-says-locksmith-advertised-19-service-charged-her-200/", "KPRC covered a Katy driver"),
    "sb616": A("https://hro.house.texas.gov/pdf/ba86r/sb0616.pdf", "SB 616"),
    "dps": A("https://www.dps.texas.gov/node/612", "DPS’s list of company license types"),
    "dpsind": A("https://www.dps.texas.gov/node/615", "DPS’s individual license page"),
    "occ": A("https://texas.public.law/statutes/tex._occ._code_section_1702.1056", "Texas Occupations Code 1702.1056"),
    "ad": A("https://www.law.cornell.edu/regulations/texas/37-Tex-Admin-Code-SS-35-9", "37 TAC 35.9"),
    "notice": A("https://www.law.cornell.edu/regulations/texas/37-Tex-Admin-Code-SS-35-8", "37 TAC 35.8"),
    "qual": A("https://www.law.cornell.edu/regulations/texas/37-Tex-Admin-Code-SS-35-123", "37 TAC 35.123"),
    "tow": A("https://www.dps.texas.gov/node/3415", "DPS has told tow companies"),
    "bbb": A("https://www.bbb.org/article/news-releases/22797-bbb-scam-alert-locked-out-dont-fall-for-a-locksmith-cons", "BBB’s locksmith scam alert"),
    "itv": A("https://www.kbtx.com/2025/07/21/predatory-locksmiths-accused-overcharging-customers-locked-out-homes-vehicles/", "InvestigateTV reported in 2025"),
    "ftc": A("https://www.ftc.gov/node/43494", "the FTC told consumers back in 2008"),
    "ws": A("https://wordstream.com/blog/2026-google-ads-benchmarks", "WordStream and LocaliQ’s 2026 benchmarks"),
}

INSP = "/blog/home-inspector-marketing-houston-the-woodlands/"
LOCK = "/blog/locksmith-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: home inspectors
    {
        "slug": "home-inspector-marketing-houston-the-woodlands",
        "title": "Home Inspector Marketing in Houston and The Woodlands: More Inspections Without Breaking TREC Rules",
        "seo_title": "Home Inspector Marketing in Houston & The Woodlands",
        "desc": "Home inspector marketing for Houston and The Woodlands: TREC ad and referral rules, buyer-direct search, sample reports, add-ons, reviews, slow markets.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google"],
        "art": "b2",
        "hero": "house",
        "hero_alt": "Illustration of a house for home inspector marketing in Houston, The Woodlands and Spring",
        "related": ["real-estate-agent-marketing-the-woodlands-houston", "foundation-repair-marketing-houston", "how-to-get-more-pest-control-customers-houston"],
        "sections": [
            (None, f"""<p>Wednesday, 4:15 p.m. You’re in an attic in Spring with a flashlight in your teeth when the phone buzzes twice. One is an agent you’ve worked with for six years, asking if you can do Friday in Cypress. The other is a number you don’t know. You call it back from the driveway an hour later. The buyer already booked someone else, because that someone had a “book now” button and a price on the website.</p>
<p>That second call is where most of the growth in home inspector marketing is hiding.</p>
<p>The short version for Houston and The Woodlands: keep the agent relationships, but earn them the only way TREC allows, which is by being good, fast and easy to schedule. Then build a second pipeline that doesn’t depend on agents at all. That means a Google Business Profile full of reviews, a website with prices, a sample report and online booking, plus add-on services that raise the ticket. Houston’s clay soil and flood history are the content that sets you apart. And you need a plan for months when HAR’s numbers go soft, because they’re soft right now.</p>
<p>This is written for one- to five-inspector companies working Harris and Montgomery counties. We haven’t run marketing for a home inspection company, so where we share numbers from other home service accounts, we say so.</p>"""),

            ("Where Houston home inspection jobs actually come from", f"""<p>Ask most inspectors where their work comes from and you’ll hear “agents” before the question is finished. That’s true, and it’s also a risk. An inspection business that lives on eight agents is one brokerage change away from a bad quarter.</p>
<p>Buyers research everything now. A first-time buyer in Tomball reads three reviews of the dishwasher, so of course they’ll Google “home inspector near me” once the option period starts. Many agents hand over three names, and the buyer checks all three on Google. Your profile and website decide which name gets the call even when the referral was real.</p>
<p>So think of it as two funnels that share a front door:</p>
<ul>
<li><b>Agent-influenced.</b> The agent mentions you, the buyer looks you up, then books. Your reviews and website still close it.</li>
<li><b>Buyer-direct.</b> No agent recommendation, or the buyer ignores it. They search “home inspection The Woodlands” or “home inspector Katy TX,” compare prices and availability, and book whoever makes it easy.</li>
</ul>
<p>A third, smaller stream (pre-listing, new construction and investors) gets its own section below.</p>
<!--fig:sources-->"""),

            ("The TREC rules that shape every inspector’s marketing", f"""<p>Texas inspectors work under rules that most marketing agencies have never read. Read them before you approve a single ad.</p>
<p><b>Your license number goes on everything.</b> Under {SRC['t221']}, an inspector’s advertisement includes a lot more than ads: inspection reports, business cards, invoices, signs, brochures, websites, email, text messages, directory listings and broadcast ads. Every one must show your name (or a DBA registered with TREC) and your license number. Websites can put the license numbers on one prominent page such as the homepage or About page, and on social sites the number can sit on the profile page. If you’re a real estate inspector or apprentice, your ads also have to name your sponsoring professional inspector and say you’re sponsored.</p>
<p><b>Register the DBA with TREC, not just the county.</b> {SRC['tdba']} spells out that filing an assumed name with the Secretary of State doesn’t satisfy TREC. Each inspector registers the company name under their own license, and notifies TREC within 30 days of starting or stopping use of it. If you’re adding a second inspector this year, put that on the onboarding checklist next to the truck magnet.</p>
<p><b>No referral fees, either direction.</b> {SRC['t220']} lists real estate agents and brokers among “settlement service providers,” and inspectors may not pay or receive a fee or other valuable consideration to or from them for referring inspections or for being placed on a list of preferred providers. The same rule bars inspecting a property when your compensation or future referrals depend on what you report, and it asks you to assure clients of your independence from outside influence.</p>
<p><b>Paid vendor lists are a narrow exception.</b> Per {SRC['tlist']}, a brokerage can sell advertising on a vendor list only if the list clearly says placement is based on advertising, the price is a market rate, and any ranking discloses how it was built. A “platinum preferred inspector” package that quietly buys referrals is exactly what the rule targets.</p>
<!--fig:rules-->
<p>None of this is legal advice, and TREC updates its rules, so check the current text before you build a campaign around a gray area. If something feels like a way to pay for referrals with extra steps, it probably is.</p>"""),

            ("Earning agent referrals without paying for them", f"""<p>Agents can’t be bought, at least not legally. They can be made to like working with you. What we hear agents in The Woodlands and Kingwood care about is short and boring.</p>
<ul>
<li>You answer the phone, or call back inside an hour.</li>
<li>Same-week availability, including Saturdays.</li>
<li>A report delivered the same night or the next morning, with a summary page a buyer can actually read.</li>
<li>Findings written in plain, calm language. “Recommend evaluation by a licensed plumber” lands better than three paragraphs of alarm, and it’s still honest.</li>
<li>Scheduling that doesn’t require four texts. An online booking link the agent can forward wins over “call me.”</li>
</ul>
<p>Notice what’s missing from that list. Softening findings to save deals is off the table under 535.220, and agents who want that aren’t referral partners you should keep. Your report is written for your client, who is the buyer.</p>
<p>Ordinary relationship marketing is still fine. A monthly agent email about something useful (what a Houston sewer scope finds, how to read an elevation survey) keeps your name in front of them. Keep coffee and lunches modest and never tie them to referrals, since “valuable consideration” is the phrase in the rule. When unsure, ask your attorney or TREC.</p>
<p>For the agent’s view of all this, our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how local agents market themselves')} shows what their week looks like.</p>"""),

            ("Buyer-direct: winning the Google search in Houston and The Woodlands", f"""<p>The buyer who searches has a deadline. The option period on a TREC contract is often a week to ten days, so they need someone this week, and they decide in minutes.</p>
<p><b>Google Business Profile first.</b> Primary category: <b>Home inspector</b>. Add services one by one with short descriptions (“Buyer’s home inspection, TREC REI 7-6 report, same-day delivery”), list add-ons separately, set accurate hours, and link your booking page as the appointment URL. If you work from home, set it up as a service-area business with the towns you really cover, from The Woodlands and Conroe down to Spring and Cypress. Post photos from real inspections: the attic, the electrical panel, the drone shot of a roof in Magnolia. Our {L('/blog/rank-in-google-map-pack-houston/', 'Houston map pack guide')} covers the ranking side.</p>
<p><b>Search ads for the deadline crowd.</b> The keywords are narrow and the intent is high. A typical starting list:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Core inspection</td><td>home inspector near me, home inspection The Woodlands, home inspector Spring TX, house inspection Katy</td><td>Pricing and booking page</td></tr>
<tr><td>New construction</td><td>new construction inspection Conroe, phase inspection Houston, 11 month warranty inspection</td><td>New build page with phase descriptions</td></tr>
<tr><td>Add-ons</td><td>sewer scope inspection Houston, termite inspection for home purchase, pool inspection Cypress</td><td>Add-on page with license info</td></tr>
<tr><td>Sellers</td><td>pre listing inspection, seller home inspection Sugar Land</td><td>Pre-listing page</td></tr>
<tr><td>Brand</td><td>your company name, your name plus inspector</td><td>Homepage</td></tr>
</tbody></table></div>
<p>Negatives from day one: jobs, career, school, course, license, “how to become,” salary, apprentice, code inspector, city inspection, permit, car inspection, vehicle, state inspection, and “free.” The training-related terms matter more than you’d think. Houston has a steady crop of people researching how to become inspectors, and they click ads.</p>
<p>Set location targeting to people in or regularly in your area, and schedule ads for when someone can answer or the booking page works on its own. Our {L('/services/search-marketing/', 'search team')} runs this kind of tight local account. And if you’re choosing between Google’s two ad types, see below.</p>"""),

            ("The website that books inspections: prices, sample report, online scheduling", f"""<p>Most inspector websites we see have a stock magnifying glass and a contact form. Buyers want three things on the first screen.</p>
<p><b>A price.</b> Even a calculator by square footage and age, or a simple table that starts at [your price] for up to 2,000 square feet. Buyers comparing three inspectors will call the one who shows a number first. Hiding it to “discuss value” mostly loses you the comparison.</p>
<p><b>A sample report.</b> A real, anonymized report from a typical Houston house, with photos and the summary page. The full TREC REI 7-6 format is long and technical, and buyers love seeing how you explain it. This is also your best agent marketing, because agents judge you by how your reports read to nervous buyers.</p>
<p><b>Online scheduling with the add-ons attached.</b> The buyer picks a date and adds the sewer scope, WDI and pool inspection as checkboxes with prices. The booking tool should collect the agent’s name, send the agreement for signature and take a deposit if that’s your policy. Most inspection software does all of this. Turning it on is the marketing.</p>
<!--fig:site-->
<p>Then the trust stuff: your TREC license number on the About page (which also satisfies 535.221(d)), each inspector’s photo and license, and a page per service area. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} shows how to write area pages that aren’t copy-and-paste, and our {L('/services/web-design-seo-pr/', 'web design team')} builds them.</p>
<p>A buyer who gets voicemail at 6 p.m. usually tries the next name. See our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} for the follow-up side.</p>"""),

            ("Add-on services: sewer scope, termite, pool and foundation elevation", f"""<p>Add-ons are how a $400 job becomes a $700 job, and in Houston several of them are close to essential. Each one also gives you a keyword to rank for and a reason for a buyer to pick you over a cheaper inspector who can’t do it.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Add-on</th><th>License or rule to check</th><th>Houston marketing angle</th></tr></thead>
<tbody>
<tr><td>WDI / termite inspection</td><td>Official WDI inspection by a certified applicator or technician in TDA’s Termite and WDI category (4 TAC 7.175)</td><td>Buyers often want it with the main inspection; say clearly who performs it</td></tr>
<tr><td>Sewer scope</td><td>Covered by your inspection agreement; describe limits clearly</td><td>Older homes in Spring Branch, Meyerland and the Heights; tree roots from big oaks</td></tr>
<tr><td>Pool and spa</td><td>Optional system under TREC Rule 535.233, inspected only if you agree to</td><td>Common in The Woodlands, Cypress and Katy backyards</td></tr>
<tr><td>Foundation elevation survey</td><td>Report observations; leave engineering conclusions to engineers</td><td>Clay soil, slab foundations and buyers who’ve heard repair horror stories</td></tr>
<tr><td>Sprinklers, wells, septic, outbuildings</td><td>Also optional systems under 535.233</td><td>Acreage in Magnolia, Montgomery and north of Conroe</td></tr>
</tbody></table></div>
<p>The WDI one has a trap. A TREC license doesn’t cover it. Per {SRC['tda']}, the official WDI inspection has to be done by a TDA Structural Pest Control Service licensee in the right category, and the Texas WDI report is a separate form from REI 7-6, as {SRC['spec']} explains. {SRC['twdi']} even addresses the inspector who advertises WDI inspections when nobody on staff is licensed, and says that can be misleading advertising under both agencies’ rules. If you subcontract to a licensed pest company, say so on the page.</p>
<p>Pools and acreage systems are optional under {SRC['sop']}, so price them separately. Put each add-on on its own page with its own price. “Sewer scope Houston” is a real search, and a single page that says “we offer many services” won’t rank for any of them.</p>"""),

            ("Houston clay soil and flood history: content buyers actually read", f"""<p>Most inspector blogs are generic (“10 things we check”). In Houston, you have better material than that, and buyers are already scared of it.</p>
<p><b>Clay soil and foundations.</b> {SRC['clay']} that Houston’s heavy clay swells when wet and shrinks and cracks when dry, and that repeated cycle contributes to foundation movement. A local foundation contractor in the same story put repair costs anywhere from about $3,000 to $20,000 and up, with severe cases at $40,000 to $50,000. That one sentence explains why a buyer will pay extra for elevation readings. Useful posts: which slab cracks you note and why you write “recommend evaluation by a structural engineer” instead of a diagnosis.</p>
<p><b>Flood history.</b> Since September 1, 2019, SB 339 has required Texas sellers to disclose more about flood risk, including the 500-year floodplain, reservoir proximity and whether the home has flooded before, per {SRC['sb339']}. The same story noted that, based on city of Houston data, most structures affected by Harvey were outside the 100- and 500-year floodplains. So buyers in Kingwood, Katy and Meyerland have good reason to ask what flood clues an inspector looks for. A post on “signs a house may have flooded” (patched drywall at the same height in every room, new baseboards in an older house, rust lines on the water heater) is exactly the kind of practical content buyers share with their spouse.</p>
<p>Stay in your lane: point out evidence and recommend further evaluation. You’re not the floodplain manager or the engineer.</p>
<p>A few other Houston-specific topics that earn links and searches: what the February 2021 freeze did to attic plumbing, radiant barrier and attic heat, polybutylene and galvanized supply lines in 1970s and 1980s homes, and what to check on a new build in a master-planned community before the builder’s walkthrough.</p>"""),

            ("Local Services Ads for home inspectors", f"""<p>{SRC['lsa']} includes <b>Home inspector</b>, so you can run pay-per-lead ads with the Google Verified badge at the very top of the results. Availability still varies by area, and the only way to know for your ZIP code is to start the sign-up and see what Google offers.</p>
<p>Inspection searches are short and urgent, and the LSA box is the first thing a buyer sees. You pay per lead, not per click. Ranking leans on reviews, responsiveness and proximity, so 9 reviews won’t beat a company with 400.</p>
<p>Watch for wrong-service leads (city code or car inspections), answer fast, and dispute the junk. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads comparison')} covers how to run both without them cannibalizing each other.</p>"""),

            ("Reviews: the inspector’s best ad", f"""<p>Reviews do double duty for inspectors. Buyers read them, and agents check them before they put your name on a list.</p>
<p>The timing is tricky. Right after the inspection, the buyer is anxious about your findings. The best moment is usually a day or two after the report, once they’ve read it and maybe used it to negotiate repairs. A text that works:</p>
<blockquote>Hi Maria, this is Dan from [company]. Hope the report helped with your repair request on the Oak Ridge North house. If you have a minute, a Google review helps other buyers find us: [link]. Thanks, and congrats on the house.</blockquote>
<p>Send the same link to every client, not only the happy ones. Google’s rules prohibit review gating and incentives, and filtering out unhappy clients usually backfires anyway. Reply to every review with specifics. If a buyer complains that you “missed” something, explain calmly what was visible and accessible on inspection day; future clients read the reply more closely than the complaint. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("When the market slows: HAR’s numbers and what to do with them", f"""<p>Inspection volume follows contracts, and contracts are down. {SRC['har']} showed 7,030 single-family sales in September 2026, down 5.7% from a year earlier, with active listings up 6.3% to 40,192, a 5.5-month supply and 58 average days on market. October was weaker: {SRC['haroct']} put single-family sales at 6,348, down 14.9%, with a $320,000 median price and an average mortgage rate of 7.33%.</p>
<!--fig:market-->
<p>Fewer contracts means fewer inspections. What we’d do:</p>
<ul>
<li><b>Sell pre-listing inspections.</b> With more than five months of supply, sellers need an edge. A pre-listing inspection lets them fix things before a buyer’s inspector finds them. Pitch it to listing agents, not just buyer’s agents.</li>
<li><b>Go after new construction.</b> Builders have inventory to move and buyers in Conroe and Montgomery are buying new. Phase inspections (foundation pre-pour, pre-drywall, final) and 11-month warranty inspections are steady work that doesn’t care about resale volume.</li>
<li><b>Market to investors and property managers.</b> They buy in all markets and order repeat inspections.</li>
<li><b>Keep the buyer-direct funnel running.</b> Don’t cut search ads the month you need them most; cut wasted keywords instead.</li>
</ul>
"""),

            ("A first 90 days and a realistic budget", f"""<p>Here’s how we’d sequence it for a two-inspector company in The Woodlands that mostly lives on agent referrals today.</p>
<!--fig:plan-->
<p>Budget, as an illustrative starting point for a small Houston-area company (not a quote or a benchmark):</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Google Ads search</td><td>$600 to $1,500</td><td>Core and add-on keywords in a 20- to 30-mile radius</td></tr>
<tr><td>Local Services Ads</td><td>$300 to $1,000</td><td>Pay per lead; depends on availability</td></tr>
<tr><td>Website, pages and content</td><td>$400 to $1,200</td><td>Area pages, add-on pages, one useful post a month</td></tr>
<tr><td>Review and scheduling tools</td><td>$50 to $250</td><td>Often included in inspection software</td></tr>
</tbody></table></div>
<p>Track one number above the rest: cost per booked inspection by source. Leads don’t pay you; inspections do. Give each channel a tracked phone number, tag online bookings by source, and ask “how did you find us?” on every booking form.</p>
<p>If you want a plan built around your service area and the add-ons you actually offer, <a href="/contact/">get in touch</a> and a senior strategist will put one together.</p>"""),
        ],
        "faq": [
            ("How do home inspectors get more clients in Houston?",
             "Most Houston inspectors get work from agent referrals and from buyers who search Google directly. Grow both. Keep agents happy with fast scheduling, same-day reports and clear writing, and build a buyer-direct pipeline with a strong Google Business Profile, steady reviews, a website showing prices and a sample report, online booking, and search ads for terms like home inspector The Woodlands or sewer scope Houston."),
            ("Can a Texas home inspector pay real estate agents for referrals?",
             "No. TREC Rule 535.220 lists real estate agents and brokers as settlement service providers, and inspectors may not pay or receive a fee or other valuable consideration to or from them for referrals or for placement on a preferred provider list. Paid vendor lists are allowed only at market advertising rates with clear disclosure that placement is advertising. Check the current rule or an attorney before any arrangement."),
            ("Do Texas inspectors have to put their license number in ads?",
             "Yes. TREC Rule 535.221 requires an inspector’s name or TREC-registered business name and license number on advertisements, which include reports, business cards, invoices, signs, websites, emails and texts. A website can show license numbers on one prominent page such as the homepage or About page, and social media accounts can show them on the profile page. Sponsored inspectors must also name their sponsor."),
            ("Can a home inspector in Houston and The Woodlands offer termite inspections?",
             "Only if the person doing the official wood destroying insect inspection holds a Texas Department of Agriculture Structural Pest Control Service license in the termite and WDI category. A TREC inspector license alone does not cover it, and TREC warns that advertising WDI inspections without a licensed person on staff can be misleading. Many inspectors get the TDA license or partner with a licensed pest company and disclose it."),
            ("Are Google Local Services Ads available for home inspectors?",
             "Google’s Local Services Ads category list includes Home inspector, so many inspection companies can run pay-per-lead ads with the Google Verified badge. Availability varies by location, so start the sign-up with your business address to see if it’s offered in your Houston area ZIP codes. Ranking depends heavily on reviews and how fast you respond, so build reviews before expecting volume."),
        ],
        "figures": {
            "sources": {
                "type": "columns",
                "title": "Where an inspector’s bookings come from",
                "sub": "Share of booked inspections by first source, before and after building a buyer-direct funnel",
                "labels": ["Agents now", "Agents later", "Google now", "Google later", "Repeat now", "Repeat later"],
                "values": [80, 58, 12, 30, 8, 12],
                "highlight": [3],
                "y_label": "Share of bookings (%)",
                "note": "Illustrative example, not client data",
                "alt": "Column chart of illustrative booking sources for a home inspector in Houston and The Woodlands, agents versus Google search",
                "caption": "Agent work doesn’t have to shrink in count. It just stops being the only pipe.",
            },
            "rules": {
                "type": "compare",
                "title": "Agent marketing under TREC rules",
                "left": {"title": "Off limits", "items": ["Paying agents per referral", "Paying for a spot on a preferred list", "Gift cards tied to referrals", "Softening findings to protect deals", "Ads without your license number"]},
                "right": {"title": "Fair game", "items": ["Fast scheduling and same-day reports", "Readable summary pages", "Useful agent newsletters", "Disclosed ads at market rates", "License number on every ad and report"]},
                "alt": "Comparison of allowed and prohibited agent referral marketing for home inspectors in Houston under TREC rules",
                "caption": "Based on TREC Rules 535.220 and 535.221. Not legal advice; check the current rule text.",
            },
            "site": {
                "type": "checklist",
                "title": "What an inspector’s website needs",
                "sub": "The pages and features that turn a Houston search into a booking",
                "items": ["Price or price calculator on the first screen", "Downloadable sample report", "Online booking with add-on checkboxes", "TREC license number on the About page", "Each inspector’s photo and license", "Separate pages for sewer, WDI, pool, foundation", "Area pages: The Woodlands, Spring, Katy, Cypress", "What we inspect and what we don’t"],
                "alt": "Checklist of website features for a home inspector in Houston and The Woodlands to get more booked inspections",
                "caption": "If you only do two this month, do the price and the booking link.",
            },
            "market": {
                "type": "stats",
                "title": "Houston’s fall 2026 resale market",
                "stats": [["-14.9%", "single-family sales, Oct. vs last year"], ["5.5 mo", "months of supply in Sept."], ["40,192", "active single-family listings, Sept."], ["58", "average days on market, Sept."]],
                "note": "Source: HAR September 2026 report; October figure via My Neighborhood News summary of HAR",
                "alt": "Stats on Houston home sales slowdown in fall 2026 that affect home inspector marketing in Houston and The Woodlands",
                "caption": f"From {SRC['har']} and {SRC['haroct']}.",
            },
            "plan": {
                "type": "steps",
                "title": "A 90-day plan for a small inspection company",
                "sub": "For a team in The Woodlands that mostly runs on agent referrals",
                "steps": [["Days 1-14", "Fix the profile, license number placement, DBA registration and booking link."], ["Days 15-30", "Publish prices, a sample report and add-on pages. Start review texts."], ["Days 31-60", "Launch search ads with negatives. Start the LSA sign-up."], ["Days 61-75", "Write two Houston posts: clay foundations and flood clues."], ["Days 76-90", "Pitch pre-listing and new-build inspections. Judge channels by cost per booking."]],
                "alt": "Five-step 90-day marketing plan for a home inspector in The Woodlands and Houston",
                "caption": "The order matters: ads work better once the website and reviews can close the click.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: locksmiths
    {
        "slug": "locksmith-marketing-houston",
        "title": "Locksmith Marketing in Houston: Getting Found When Google Is Full of Fakes",
        "seo_title": "Locksmith Marketing in Houston: Ads, Maps and Trust",
        "desc": "Locksmith marketing in Houston: Google Advanced Verification, fake listings, Texas DPS license rules for ads, LSA, Google Ads costs and after-hours calls.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Google"],
        "art": "b4",
        "hero": "key",
        "hero_alt": "Illustration of a key for locksmith marketing in Houston, The Woodlands and Katy",
        "related": ["garage-door-company-marketing-houston", "google-business-profile-video-verification", "google-guaranteed-vs-google-verified"],
        "sections": [
            (None, f"""<p>Saturday, 11:40 p.m. A woman is standing outside her townhouse off Market Street in The Woodlands, keys on the kitchen counter, phone at 14%. She searches “locksmith near me” and taps the first thing that says “24/7, $19 service call.” The man who answers says “locksmith service,” not a company name. Your shop is six minutes away with a tech on call. Your phone never rings.</p>
<p>That’s locksmith marketing in Houston: you’re competing against other locksmiths, and also against call centers pretending to be locksmiths.</p>
<p>What works here: get through Google’s Advanced Verification so you can run ads at all, keep a Google Business Profile that’s clean enough to survive suspicions, and put your Texas DPS license number everywhere the law says to (which is everywhere). After that, price the job honestly on the phone and answer every call at 2 a.m. like it’s 2 p.m. Treat commercial rekeys and access control as a separate business with its own marketing, because it pays better and doesn’t wake you up.</p>
<p>We haven’t worked with a locksmith company. We have run Google Ads and local SEO for home service businesses across Greater Houston, and that’s where the experience here comes from.</p>"""),

            ("The fake-listing problem is your marketing problem", f"""<p>Locksmiths have been the poster child for fake Google listings for over a decade. In {SRC['gsec']} with university researchers, the company said fewer than 0.5% of local searches led to fake listings, and that locksmiths, plumbers, electricians and other contractors made up roughly 2 of every 5 fake listings. It also said abusive listings had fallen 70% from their June 2015 peak. Small share of searches, big share of locksmith searches.</p>
<p>The pattern hasn’t changed much. {SRC['sel']} summarized the New York Times reporting: listings with fake local addresses route calls to a remote call center, which quotes $35 to $90 by phone and dispatches a subcontractor who often demands three or four times that on site. Houston has its own versions. {SRC['kprc']} who found a “$19 locksmith” through Google and paid about $185.</p>
<p>Two things follow for a real shop.</p>
<p>First, Google is suspicious of you by default. In our experience with restricted home service categories, profiles get extra verification, edits get flagged, and suspensions hit legitimate businesses too. Keep your profile boringly accurate. Our {L('/blog/google-business-profile-video-verification/', 'guide to Google Business Profile video verification')} walks through what Google wants to see.</p>
<p>Second, trust is the product. Every piece of your marketing should answer the question the customer is silently asking: is this a real local company, and will the price on the phone be the price at the door?</p>
<!--fig:fakes-->"""),

            ("Texas locksmith licensing, and what it means for your ads", f"""<p>Locksmiths in Texas are licensed by the Department of Public Safety under the Private Security Act (Occupations Code chapter 1702). The regulator changed shape in 2019: {SRC['sb616']} abolished the Texas Private Security Board as of September 1, 2019, moved its functions to DPS, and turned the board into an advisory committee. If an old competitor’s website still says “licensed by the Texas Private Security Board,” that tells you how often they update it.</p>
<p>The pieces that matter for marketing:</p>
<ul>
<li><b>Company license.</b> Per {SRC['dps']}, locksmith work falls under the Class B Security Contractor company license, which can cover locksmith, electronic access, alarm and other services. If you’re selling access control, confirm your license covers electronic access too.</li>
<li><b>Individual licenses.</b> {SRC['dpsind']} lists Locksmith as an individual license, and individuals have to be affiliated with a licensed company. Each tech you send out should be licensed.</li>
<li><b>Using the word “locksmith” makes you a locksmith company.</b> Under {SRC['occ']}, advertising services with the term “locksmith,” or having it in the company name, counts as acting as a locksmith company. {SRC['tow']} that an unlicensed outfit opening cars for owners can’t advertise that work with the word, which is one more reason to keep your license number visible.</li>
<li><b>License number in every ad.</b> {SRC['ad']} requires licensee advertisements, including business cards, to show the company name and address as in DPS records (residential addresses excepted) and the company license number.</li>
<li><b>Consumer notice and trucks.</b> {SRC['notice']} requires you to give clients your license number and DPS contact information for complaints, and any vehicle that shows the company name must show the license number in letters at least one inch high on each side.</li>
</ul>
<!--fig:license-->
<p>Qualifying for the company license, per {SRC['qual']}, takes either two consecutive years of full-time locksmith experience or a set of approved courses, an exam and one year of experience. That bar is real. Put it to work in your marketing: “Texas DPS licensed company, every tech individually licensed, license numbers on our trucks” is a sentence a call center can’t truthfully say. Link to the DPS license search so customers can check.</p>
<p>We’re marketers, not lawyers. Read the current rules or ask DPS before you print anything new.</p>"""),

            ("Google Advanced Verification: the gate before any ad runs", f"""<p>You can’t just open a Google Ads account and start bidding on “locksmith near me.” {SRC['gpol']} restricts locksmith ads in the U.S., and {SRC['av']} says all locksmith businesses in the U.S. and Canada must pass Advanced Verification.</p>
<p>The process, per Google:</p>
<!--fig:verify-->
<p>Google says verification typically takes around 6 to 8 weeks, and appeals take about the same. So plan your launch two months out, and don’t promise your partner a busy December if you’re starting the paperwork in November.</p>
<p>A few things we’d have ready before applying. Your DPS license paperwork with the business name exactly as it appears in Google Ads. A real storefront or office with signage, since the agent confirms your business exists and where it operates over video. Someone at the location at the scheduled time. And the customer ID of the account you’ll actually use, so you don’t verify one account and run ads from another. Agencies that “own” your ad account create problems here, so set it up under your own login and give your agency access.</p>"""),

            ("Local Services Ads for locksmiths", f"""<p>{SRC['lsa']} includes Locksmiths, so you can run pay-per-lead ads in the box at the very top of Google. Google also notes that pre-badge ads (the ones that start before checks finish) aren’t available for locksmiths. You wait for full screening.</p>
<p>For a locksmith, LSA has two real advantages. The Google Verified badge answers the trust question before the customer calls. And you pay per lead, not per click, so a curious tap on a $40 keyword doesn’t cost you anything. You can dispute leads that weren’t real customers, which matters in a category full of wrong-number calls. Our {L('/blog/local-services-ads-lead-disputes-credits/', 'guide to LSA lead disputes')} covers how.</p>
<p>The catch is ranking. LSA leans hard on reviews, responsiveness and distance. If you miss calls after midnight, Google notices, and your ads show less. Read our {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified explainer')} if you’re still seeing the old badge in competitors’ screenshots.</p>"""),

            ("Google Ads for locksmiths: costs, structure and negatives", f"""<p>Locksmith clicks are expensive because emergency intent is valuable and the call centers bid too. For context, {SRC['ws']} put the median cost per click for the Home and Home Improvement category at $8.33, with a median cost per lead of $90.92. Emergency lockout terms in large metros run well above that category median in accounts we’ve seen for urgent home services. Expect it, and build the account so you only pay for the searches that turn into jobs. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give more local context.</p>
<p>Split campaigns by job type, because the economics are completely different:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Example keywords</th><th>How to run it</th></tr></thead>
<tbody>
<tr><td>Emergency lockout</td><td>locked out of house, locksmith near me, emergency locksmith Spring TX, car lockout Katy</td><td>Call-focused ads, tight radius, schedule only when someone answers</td></tr>
<tr><td>Car keys and fobs</td><td>car key replacement Houston, key fob programming, lost car keys no spare</td><td>High ticket; list makes you cover and quote a range</td></tr>
<tr><td>Residential rekey and locks</td><td>rekey house Cypress, change locks after moving, smart lock installation The Woodlands</td><td>Daytime, bookable, good for new homeowners</td></tr>
<tr><td>Commercial and access control</td><td>commercial locksmith Houston, access control installation, master key system, door closer repair</td><td>Form plus call, longer sales cycle, business hours</td></tr>
<tr><td>Safes</td><td>safe opening, safe locksmith near me</td><td>Only if you actually do it</td></tr>
</tbody></table></div>
<p>The negative list does as much work as the keywords:</p>
<!--fig:negatives-->
<p>Settings we’d use. Presence targeting set to people in or regularly in your locations, so you don’t pay for someone in Dallas researching locks. A radius drawn around how far your tech can drive in 30 minutes, which on I-45 at 5:30 p.m. is less than you think. Ad schedules that match your actual on-call coverage. Call assets with call reporting on, and calls over 60 seconds counted as conversions. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} explains setup, and our {L('/services/search-marketing/', 'Google Ads team')} can run it for you.</p>
<p>Sample ad copy that leans into what fakes can’t say:</p>
<blockquote>Headline: Local Locksmith in The Woodlands | Licensed Texas DPS Company<br>Headline: Lockouts From [your price] | Price Quoted Before We Roll<br>Description: Real shop on Research Forest Dr. Every tech licensed and background checked. No surprise fees. Call now, we answer 24/7.</blockquote>
<p>Only say “background checked” if it’s true, and only list a street if your customers can actually visit it.</p>"""),

            ("Emergency lockouts and commercial work are two businesses", f"""<p>Most locksmiths market like they only do lockouts, because that’s what the phone rings for. But the lockout customer is a one-time buyer in a panic. The property manager with 14 buildings in the Energy Corridor needs rekeys every time a tenant moves, master key systems, door hardware and access control. That customer calls for years.</p>
<!--fig:split-->
<p>Commercial marketing looks different:</p>
<ul>
<li>A commercial page with real photos of installed hardware, panic bars and access control panels, plus the brands you service.</li>
<li>LinkedIn and direct outreach to property managers, facilities directors, HOA management companies and churches in Sugar Land, Katy and north Houston. Our {L('/blog/property-management-company-marketing-houston/', 'property management marketing post')} shows how those buyers think.</li>
<li>Service agreements with response-time promises.</li>
<li>A dedicated form that asks the number of doors, locations and whether they want a site visit.</li>
</ul>
<p>The emergency side still pays the bills and feeds reviews. Just don’t let it be the only thing your website talks about.</p>"""),

            ("Price transparency beats bait-and-switch", f"""<p>The scam model is built on a low phone quote. {SRC['bbb']} describes it plainly: a very low price to win the call, then extra charges once the tech arrives, often after claiming the lock has to be drilled. The BBB says most consumer complaints concern fees that weren’t disclosed on the call, and that it isn’t routine for a locksmith to insist on drilling. {SRC['itv']} that one BBB region logged 48 locksmith complaints in 2024, with examples like a customer expecting about $150 and billed $1,217.29. And {SRC['ftc']} to research a locksmith before an emergency and save the number.</p>
<p>That gives a legitimate shop an obvious position: say the real price first.</p>
<ul>
<li>Publish a price table on your website: residential lockout from [your price], car lockout from [your price], rekey per cylinder [your price], after-hours fee [your price]. Ranges are fine. A number beats “call for a quote.”</li>
<li>On the phone, quote the total range including the trip fee, and say what would change it.</li>
<li>Write “We quote before we roll, and the price at your door matches” on the site, the ads and the truck. Then make it true.</li>
<li>Explain when drilling is actually needed. Customers who’ve read the BBB warning will ask.</li>
<li>Send a text confirmation with the quote, the tech’s name and photo, and the license number before arrival.</li>
</ul>
<p>Some callers will hang up when they hear an honest $150 after seeing a $19 ad. Let them go. A good share of them call back 40 minutes later when the $19 guy hasn’t shown up, and those are often your five-star reviews.</p>"""),

            ("Reviews and the after-hours phone", f"""<p>Reviews are how a real locksmith separates from a call center in the map pack. Ask every customer by text right after the job, with the same link for everyone and nothing offered in exchange. Lockout customers are often grateful in a way few other service customers are, so the ask rarely feels awkward. Reply to every review, and to negative ones with specifics. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has templates.</p>
<p>Then the phone. Emergency calls come at night, and missed calls cost you the job, the review and some LSA ranking. Options, from cheapest to best:</p>
<ol>
<li>Owner’s cell on forward after hours. Free, and it burns people out by March.</li>
<li>A rotating on-call tech with calls forwarded and a backup if they don’t pick up in four rings.</li>
<li>A 24/7 answering service trained on your price ranges and dispatch rules, which books the job and texts the tech.</li>
</ol>
<p>Whatever you choose, test it. Call your own number at 1 a.m. once a month from a phone they don’t recognize. If it goes to voicemail, your ads shouldn’t be running at 1 a.m. Pause the late-night schedule until coverage is real.</p>"""),

            ("A first 90 days and a starting budget", f"""<p>For a Houston locksmith with a shop, two or three techs and little marketing today, this is the order we’d use. Start the Advanced Verification application on day one, since it takes the longest.</p>
<ol>
<li><b>Weeks 1-2:</b> apply for Advanced Verification and LSA. Audit the Google Business Profile for accuracy. Put the DPS license number on the website, invoices, trucks and profiles.</li>
<li><b>Weeks 3-6:</b> build service pages (lockouts, car keys, rekey, commercial, access control) with prices. Set up call tracking and review texts. Sort out after-hours coverage.</li>
<li><b>Weeks 7-10:</b> once verified, launch emergency and car key campaigns in a tight radius with the full negative list. Turn on LSA.</li>
<li><b>Weeks 11-13:</b> add commercial campaigns and outreach to property managers. Review cost per booked job by campaign and cut what doesn’t pay.</li>
</ol>
<!--fig:budget-->
<p>Treat those as examples for a single-location shop, not quotes. The number that matters is cost per completed job by channel, and you only get it with tracked calls tied to invoices.</p>
<p>If you run garage doors too, our {L('/blog/garage-door-company-marketing-houston/', 'garage door marketing post')} covers the same verification gate from that side. And if you want a plan built for your shop, your service area and your mix of emergency and commercial work, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I get more locksmith customers in Houston?",
             "Pass Google’s Advanced Verification so you can run ads, keep an accurate Google Business Profile, and collect reviews after every job. Show your Texas DPS license number on your website, trucks and ads, publish starting prices, and answer every call around the clock. Then build a commercial side with rekeys, master key systems and access control for property managers, which brings repeat work."),
            ("Do locksmiths need Advanced Verification for Google Ads?",
             "Yes. Google requires all locksmith businesses in the United States and Canada to pass Advanced Verification before their ads can run. You submit business, owner and license details, then complete a video call from your business location so an agent can confirm the business is real. Google says it typically takes about 6 to 8 weeks, so start well before you need the calls."),
            ("Who licenses locksmiths in Texas?",
             "The Texas Department of Public Safety licenses locksmith companies and individual locksmiths under Occupations Code chapter 1702. The Texas Private Security Board was abolished in 2019 and its functions moved to DPS, with an advisory committee in its place. Locksmith companies hold a Class B Security Contractor license, and each individual locksmith must be licensed and affiliated with a licensed company."),
            ("Does a Texas locksmith have to show a license number in ads?",
             "Yes. DPS rules require licensee advertisements, including business cards, to show the company name and address as listed with the department and the company license number. Vehicles that display the company name must also show the license number in letters at least one inch high on each side. Licensees must also give clients their license number and DPS complaint contact information."),
            ("Are Local Services Ads worth it for a Houston and The Woodlands locksmith?",
             "Often, yes. Locksmiths are an eligible Local Services Ads category, and the Google Verified badge helps answer the trust question in a category full of fake listings. You pay per lead rather than per click and can dispute bad leads. Pre-badge ads aren’t available for locksmiths, so you wait for full screening, and ranking depends on reviews and answering calls quickly, including at night."),
        ],
        "figures": {
            "fakes": {
                "type": "stats",
                "title": "The fake locksmith problem in numbers",
                "stats": [["2 in 5", "fake Maps listings were contractors like locksmiths"], ["70%", "drop in abusive listings from June 2015 peak"], ["$185", "paid by a Katy driver after a $19 ad"], ["6-8 wks", "typical Google Advanced Verification time"]],
                "note": "Sources: Google Security Blog (2017), KPRC (2015), Google Ads Help",
                "alt": "Stats on fake locksmith listings and Google verification that affect locksmith marketing in Houston and Katy",
                "caption": f"From {SRC['gsec']}, {SRC['kprc']} and {SRC['av']}.",
            },
            "license": {
                "type": "checklist",
                "title": "Where your DPS license number belongs",
                "sub": "Texas rules and the trust it buys with Houston customers",
                "items": ["Every ad, including business cards", "Website footer and About page", "Google Business Profile description", "Both sides of every branded truck, 1 inch or taller", "Quotes, invoices and confirmation texts", "Consumer notice with DPS complaint contact", "Each tech’s individual license on their ID"],
                "alt": "Checklist of where a Texas locksmith in Houston and The Woodlands should display a DPS license number",
                "caption": f"Based on {SRC['ad']} and {SRC['notice']}. Check current rules before printing.",
            },
            "verify": {
                "type": "steps",
                "title": "Google Advanced Verification for locksmiths",
                "sub": "What Google asks before locksmith ads can run in the U.S.",
                "steps": [["Apply", "Submit the Advanced Verification form with contact details and your Google Ads customer ID."], ["Business and owner info", "Provide business and owner details, plus license information."], ["Licenses", "Hold every license the law requires; in Texas that means DPS."], ["Video call", "Be at your business location so an agent can confirm it exists and where it operates."], ["Wait", "Typically about 6 to 8 weeks, same for appeals."]],
                "alt": "Steps in Google Advanced Verification for locksmith ads in Houston and The Woodlands",
                "caption": f"Summarized from {SRC['av']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for locksmith ads",
                "sub": "Add before launch, then check search terms weekly",
                "items": ["DIY: how to, pick a lock, bump key, youtube", "Training: locksmith school, course, license, apprentice", "Jobs: hiring, jobs, salary, near me jobs", "Products only: lock picks, buy, amazon, home depot", "Key copies if you don’t want them: key copy, duplicate", "Services you don’t offer: safe, automotive, motorcycle", "Unlicensed tow: tow truck, roadside assistance", "Wrong intent: phone passcode, locked account, lock screen"],
                "alt": "Checklist of negative keywords for locksmith Google Ads campaigns in Houston",
                "caption": "Phone passcode and “locked out of account” searches eat budget faster than any other category.",
            },
            "split": {
                "type": "compare",
                "title": "Lockout calls vs. commercial accounts",
                "left": {"title": "Emergency lockouts", "items": ["One-time customer in a panic", "Night and weekend calls", "Price shopped against fakes", "Paid search and LSA", "Wins reviews fast"]},
                "right": {"title": "Commercial and access control", "items": ["Repeat customer for years", "Business-hours work", "Bought on reliability and response time", "Outreach, LinkedIn, service agreements", "Bigger tickets, fewer 2 a.m. calls"]},
                "alt": "Comparison of emergency lockout and commercial access control marketing for a Houston locksmith",
                "caption": "Both matter. Commercial is the one that grows the value of the business.",
            },
            "budget": {
                "type": "bars",
                "title": "Example monthly locksmith marketing mix",
                "sub": "Single-location shop in north Houston, midpoints",
                "items": [["Google Ads search", 2500, "$2,500"], ["Local Services Ads", 1200, "$1,200"], ["Website and local SEO", 900, "$900"], ["Answering service", 400, "$400"], ["Reviews and call tracking", 200, "$200"]],
                "highlight": [0],
                "note": "Illustrative example, not a quote or benchmark",
                "alt": "Bar chart of an illustrative monthly marketing budget for a locksmith in Houston and The Woodlands",
                "caption": "High click costs push search to the top. Track cost per completed job before you scale any line.",
            },
        },
    },
]
