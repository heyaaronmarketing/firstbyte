"""Batch 9: veterinary clinic marketing for independent practices in The Woodlands and Houston, and physical therapy
clinic marketing in Houston.

Research (vet): Frontiers in Veterinary Science (2025) citing Brakke Consulting's 2022 overview (about 25% of primary
care practices and about 75% of specialty/emergency practices corporate-owned; corporate primary care about 50% of
revenue); AVMA News Oct 2024 on the 2024 Pet Ownership and Demographic Sourcebook (45.5% dog households, 32.1% cat,
74.2%/57.3% visited a vet, 86.8%/77.1% have a regular vet, vet spending down 4%); AVMA News Nov 2023 (visits down
2.7% while revenue rose 5.7%, 19% of owners planning fewer visits, lapsing patients up); Texas Tribune and Axios on
2025 Census estimates (Houston metro +126,720, Harris +48,695, Montgomery and Fort Bend in the top 10 counties);
22 TAC 573.30 and 573.32 (TBVME advertising and specialty listing rules, via Cornell LII); JD Supra on advertising
24/7 vet clinics in Texas; dvm360 Apr 2026 on the AHS incidence map (Texas first in heartworm incidence); Google
Local Services Ads category list (Veterinarian, Physical therapist; no booking leads for health care); Google Maps
prohibited content policy; WordStream/LocaliQ 2026 Google Ads benchmarks; Morgan Lewis on Texas SB 140.
Research (PT): HB 4099 bill analysis (30 consecutive calendar days without referral, effective Sept 1, 2025);
Texas PT board adopted rule 322.1 (effective Nov 1, 2025; one year licensed, $100k/$300k liability coverage, DPT or
30 CCUs in differential diagnosis, signed disclosure form); APTA on Medicare's 2025 plan-of-care certification
exception; Texas PT board advertising FAQ (322.4(b)(12)); Holland & Knight on AHA v. Becerra (N.D. Tex., June 20,
2024); Google's Health in personalized advertising policy; Freshpaint on Meta's 2025 health data restrictions;
HHS press release on the Manasa Health Center review-response settlement ($30,000); Hall Render on OIG's nominal
value policy ($15 per item, $75 per year). Not used: HHS's own tracking-technology page (could not load it).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # vet post
    "frontiers": A("https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2025.1558745/full", "a 2025 paper in Frontiers in Veterinary Science"),
    "avma24": A("https://www.avma.org/news/pet-population-continues-increase-while-pet-spending-declines", "AVMA’s 2024 pet ownership data"),
    "avma23": A("https://avma.org/news/facing-economic-uncertainty-clients-delay-veterinary-visits", "AVMA News"),
    "tribune": A("https://www.texastribune.org/2026/03/26/texas-population-census-migration-waller-county/", "the Texas Tribune"),
    "axios": A("https://www.axios.com/local/houston/2026/04/02/houston-harris-population-growth-2025-census-immigration-policy", "Axios Houston"),
    "tac573": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-573-30", "22 TAC §573.30"),
    "tac57332": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-573-32", "§573.32"),
    "jds": A("https://production.jdsupra.com/legalnews/is-there-a-veterinarian-in-the-house-8965875", "a JD Supra analysis of 24/7 clinic advertising in Texas"),
    "hw": A("https://www.dvm360.com/view/new-heartworm-incidence-map-shows-shifting-hotspots", "dvm360"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy"),
    "ws": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream and LocaliQ’s 2026 benchmarks"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    # PT post
    "hb4099": A("https://capitol.texas.gov/tlodocs/89R/analysis/html/HB04099E.htm", "the HB 4099 bill analysis"),
    "r3221": A("https://ptot.texas.gov/wp-content/uploads/2025/10/§322.1-Provision-of-Services_website-adopted.pdf", "the board’s adopted rule §322.1"),
    "apta": A("https://www.apta.org/your-practice/payment/medicare-payment/coding-billing/medicares-new-exception-plan-of-care-certification-requirement", "APTA’s explainer"),
    "ptadv": A("https://ptot.texas.gov/1-are-there-any-advertising-guidelines-for-my-physical-therapy-practice", "the Texas PT board’s advertising FAQ"),
    "hk": A("https://www.hklaw.com/en/insights/publications/2024/06/american-hospital-assn-v-becerra-are-tracking-tools-ok-again", "Holland & Knight’s summary of the ruling"),
    "ghealth": A("https://support.google.com/adspolicy/answer/16701855?hl=en", "Google’s health in personalized advertising policy"),
    "fresh": A("https://freshpaint.io/blog/meta-data-restrictions", "Freshpaint"),
    "manasa": A("https://www.hhs.gov/about/news/2023/06/05/hhs-office-civil-rights-reaches-agreement-health-care-provider-new-jersey-disclosed-phi-response-negative-online-reviews.html", "HHS announced a $30,000 settlement"),
    "oig": A("https://hallrender.com/2016/12/07/oig-increases-nominal-value-dollar-limit-cmp-law/", "OIG’s nominal value policy"),
}

VET = "/blog/veterinary-clinic-marketing-the-woodlands-houston/"
PT = "/blog/physical-therapy-clinic-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: veterinary clinics
    {
        "slug": "veterinary-clinic-marketing-the-woodlands-houston",
        "title": "Veterinary Clinic Marketing in The Woodlands and Houston: How Independent Practices Win New Clients",
        "seo_title": "Veterinary Clinic Marketing in The Woodlands & Houston",
        "desc": "Veterinary marketing for independent clinics in The Woodlands and Houston: Business Profile, reviews, vet Google Ads, new movers, wellness plans, retention.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Meta"],
        "art": "b2",
        "hero": "pet",
        "hero_alt": "Illustration of a pet for veterinary clinic marketing in The Woodlands, Spring and Houston",
        "related": ["dog-daycare-boarding-marketing-houston", "how-to-get-more-dog-grooming-clients-houston", "dental-marketing-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Monday, 8:05 a.m. All three phone lines are lit. One is a regular whose lab ate a sock over the weekend. One wants to move a nail trim. The third is a woman who closed on a house in Grand Central Park two weeks ago, has a new puppy and two cats, and is calling the first three clinics Google showed her. She gets put on hold. By 8:09 she’s booked somewhere else, at the corporate hospital off the interstate with the app that let her pick a time without talking to anyone.</p>
<p>That caller was worth thousands of dollars over the next decade. Nobody at your front desk will ever know she called.</p>
<p>Veterinary clinic marketing for an independent practice in The Woodlands or Houston comes down to a few jobs done well. Show up in Google Maps for “vet near me” in the neighborhoods you actually serve. Have more recent reviews than the hospital down the road, and let a new client book in under two minutes, by phone or online. Then keep every pet on a reminder schedule so the client never drifts. Ads help, but they come after those basics.</p>
<p>This is how we’d set it up for a one- to three-doctor practice in Spring, Conroe, Magnolia, Cypress or inside the Loop.</p>"""),

            ("Independent vs. corporate: where you can actually win", f"""<p>The corporate groups have real advantages. Bigger ad budgets, a call center that answers on the second ring, slick apps, and in-house marketing teams that test landing pages all year.</p>
<p>They also own a lot of the market. Citing Brakke Consulting’s 2022 industry overview, {SRC['frontiers']} put corporate ownership at about 25% of primary care practices, which account for about half of veterinary revenue nationally, and about 75% of specialty and emergency practices. In practice, many of the polished “animal hospital” brands you compete with in north Houston belong to a group, even when the sign says a local name.</p>
<p>Independents tend to win on things a group can’t standardize:</p>
<ul>
<li>The same doctor at every visit. Put your doctors’ faces and names everywhere, and say plainly who owns the practice.</li>
<li>A local story. “Family-owned in Spring since 2009” is a fact you can advertise. A group can’t.</li>
<li>Reviews that mention people by name. Twelve reviews a month saying “Dr. Patel spent forty minutes with us” beat any ad.</li>
<li>Flexibility: same-day sick visits, a callback from the doctor, house calls for an elderly cat.</li>
</ul>
<p>Where independents lose is almost always operational. Unanswered phones, no online booking, no reminders, a Business Profile last touched in 2021. Those are fixable, and they’re cheaper than outspending anyone.</p>"""),

            ("Who’s looking for a new vet, and why", f"""<p>Most pet owners already have a vet. In {SRC['avma24']}, 86.8% of dog owners and 77.1% of cat owners said they had a regular veterinarian or practice. About 45.5% of U.S. households own a dog and 32.1% own a cat. In the past year, 74.2% of dog owners took their dog to a vet, against just 57.3% of cat owners.</p>
<!--fig:pets-->
<p>So new-client marketing mostly targets moments when someone is between vets:</p>
<ul>
<li><b>They just moved.</b> This is the big one in north Houston, and it gets its own section below.</li>
<li><b>They just got a pet.</b> Puppy and kitten season peaks in spring, and adoption events at local shelters create bursts any time of year.</li>
<li><b>Their old vet let them down.</b> A long wait for an appointment, a bill that surprised them, or a practice that changed after a sale.</li>
<li><b>Something is wrong right now.</b> Their regular vet can’t see them today, so they search “vet open now” or “emergency vet near me.”</li>
</ul>
<p>Cat owners are the underserved group. Over a quarter of cat owners reported no veterinary spending in a typical year, per the same AVMA data. A clinic with a cat-friendly exam room, separate waiting area or cat-only hours has something real to advertise, and few competitors bother.</p>"""),

            ("New movers: the growth engine in north Houston suburbs", f"""<p>The Houston metro added 126,720 people between 2024 and 2025, the largest numerical gain of any U.S. metro area, per {SRC['tribune']}. Harris County alone added 48,695, and Montgomery and Fort Bend both ranked among the ten fastest-growing counties in the country. {SRC['axios']} noted that growth slowed from the year before as international migration fell, and it’s still more new households than almost anywhere else.</p>
<!--fig:map-->
<p>Every one of those households with a pet needs a new vet within a few months of moving, usually sooner, because the old clinic in Dallas or Denver won’t refill heartworm prevention without an exam. They don’t know the area. They search, they read reviews, and they pick the closest clinic that looks competent.</p>
<p>What we’d do for a clinic near the growth areas around Conroe, Montgomery, Magnolia, Tomball, Cypress or Katy:</p>
<ol>
<li>Draw a map of the new subdivisions within a 10- to 15-minute drive. Community Impact covers openings, and your own new-client records will show which ZIP codes are growing.</li>
<li>Run Meta ads to a tight radius around those communities with a “new to the neighborhood?” message, the drive time, and a first-exam offer that’s clearly priced.</li>
<li>Get into the welcome packets. HOA and MUD newsletters, apartment leasing offices, builder closing gifts and realtor move-in baskets all take local inserts. A magnet with your number and a QR code to book lasts longer than a postcard.</li>
<li>Show up on Nextdoor. New residents ask “who’s a good vet?” there constantly. Your clients will answer if you’ve given them a reason to.</li>
<li>Build a “New to Conroe?” page (or Magnolia, or Cypress) that answers what a mover needs: which pet services you offer, how to transfer records, what heartworm and flea prevention looks like on the Gulf Coast, and the closest 24-hour emergency hospital you trust.</li>
</ol>
<p>New-mover mailing lists exist, too. We’d test them against the digital options above before committing, and judge them on booked first exams per dollar.</p>"""),

            ("Google Business Profile setup for a vet clinic", f"""<p>The map pack is where most new clients pick their vet. Your profile settings matter more there than anything on your website.</p>
<p>Categories first. Use <b>Veterinarian</b> as primary for a general practice. <b>Animal hospital</b> is a reasonable secondary if you do surgery and hospitalize. Only add <b>Emergency veterinarian service</b> if you really see emergencies during posted hours, because people search that in a panic and a wrong category earns the one-star reviews you’d expect. Add <b>Pet groomer</b> or <b>Pet boarding service</b> as secondaries only if you offer them on site.</p>
<p>Then the rest of the profile:</p>
<ul>
<li><b>Services:</b> list each one with a sentence. Wellness exams, vaccines, spay and neuter, dental cleanings, surgery, ultrasound, laser therapy, exotics if you see them. Searchers type “exotic vet near me” and “rabbit vet The Woodlands,” and listing it helps.</li>
<li><b>Description:</b> species you see, doctors’ names, ownership, and the neighborhoods you serve.</li>
<li><b>Hours:</b> accurate, with holiday hours set before Thanksgiving and Christmas. Mark which days you take same-day sick visits in the description.</li>
<li><b>Appointment link:</b> straight to online booking, not your homepage.</li>
<li><b>Photos:</b> the exam rooms, the doctors with real patients (with the owner’s permission), the parking lot, and the front of the building so a first-timer finds the door.</li>
</ul>
<p>Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers proximity, reviews and links in more depth.</p>"""),

            ("Reviews, and what the Texas board says about your ads", f"""<p>Pet owners read vet reviews closely. They’re trusting you with a family member. Recency matters as much as rating, and a 4.9 with the newest review from last spring loses to a 4.7 with twenty from this month.</p>
<p>Google’s rules, from {SRC['gpol']}: no discounts or freebies in exchange for reviews, no discouraging negative reviews, no asking only happy clients, and no asking reviewers to include specific content. So skip the “mention Dr. Kim by name” push.</p>
<p>A request that works, sent by text an hour after checkout:</p>
<blockquote>Thanks for bringing Biscuit in today. If you have a minute, we’d really appreciate a Google review about your visit: [link]. And if anything wasn’t right, reply here and Dr. Alvarez will call you.</blockquote>
<p>Send it to everyone, every visit, from your practice software. Don’t send it after a euthanasia appointment. Handle those with a handwritten card instead, and suppress them from automated messages for a few months.</p>
<p>The board has its own rules for what your ads say. Under {SRC['tac573']}, a licensee can’t run advertising that is false, deceptive or misleading, and that includes guaranteeing a cure or satisfaction, claiming superior quality the public can’t verify, creating “an inflated or unjustified expectation,” or implying you’re a certified specialist unless the vet is board certified in an AVMA-recognized specialty. Under {SRC['tac57332']}, a board-certified vet advertises as “Board Certified” followed by the specialty, and has to name the specialty whenever claiming to be a specialist.</p>
<p>One Texas-specific trap: “24/7” or “always open.” According to {SRC['jds']}, Texas law doesn’t require a vet to be on site during posted hours, but advertising round-the-clock care can mislead clients into thinking a veterinarian is present and available, which runs into those same misleading-advertising rules.</p>
<!--fig:claims-->
<p>Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has reply templates, including ones for the angry billing review every clinic gets eventually.</p>"""),

            ("Google Ads for “vet near me” and emergency searches", f"""<p>Search ads are the fastest way to fill a new doctor’s schedule. They’re also an easy way to buy clicks from people who want free shots at a pet store.</p>
<p>A structure we’d start with for a general practice:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Example keywords</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>New client (general)</td><td>vet near me, veterinarian Spring TX, animal hospital The Woodlands, new patient vet</td><td>Land on a new-client page with online booking and first-exam pricing.</td></tr>
<tr><td>Same-day and sick</td><td>vet open today, same day vet appointment, dog vomiting vet</td><td>Run only during hours you can see them. Call-focused.</td></tr>
<tr><td>Emergency</td><td>emergency vet near me, after hours vet</td><td>Only if you take emergencies. Otherwise, skip it.</td></tr>
<tr><td>Services</td><td>dog dental cleaning cost, spay neuter Conroe, exotic vet, cat vet near me</td><td>One ad group per service, each with its own page.</td></tr>
<tr><td>Brand</td><td>your clinic and doctor names</td><td>Cheap insurance against groups bidding on you.</td></tr>
</tbody></table></div>
<p>Add negatives on day one:</p>
<!--fig:negatives-->
<p>Sample ad copy for the new-client campaign. Headlines: “New Patients Welcome in Spring,” “Book Online in 2 Minutes,” “Family-Owned Since 2009.” Description: “Same doctors every visit. Dogs and cats, wellness to surgery. New-client exam $XX. Book online or call.” A real price in the ad filters out bargain shoppers and lifts the click-through rate from people who just want a clear answer.</p>
<p>Settings that matter: target people “in or regularly in” your locations, keep the radius to a realistic drive (people won’t cross the Grand Parkway at rush hour for a vaccine), schedule call assets only when someone answers, and count booked appointments and calls over 60 seconds as conversions. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} shows the setup.</p>
<p>For a sense of cost, {SRC['ws']} reported a median cost per click of $4.06, a 16.22% conversion rate and a $31.50 cost per lead for Animals &amp; Pets search campaigns between April 2025 and March 2026. That category mixes vets with groomers and pet stores, so treat it as a ballpark. Houston “emergency vet” clicks usually run higher.</p>
<p>Google’s Local Services Ads list includes a Veterinarian category, per {SRC['lsa']}. Those are pay-per-lead and lean heavily on reviews, so test them once your profile is strong. Our {L('/services/search-marketing/', 'search marketing team')} runs both.</p>"""),

            ("Online booking and the phone: where new clients leak", f"""<p>Back to that Monday caller. She didn’t want to wait on hold, and she didn’t need to talk to anyone to book a new-puppy exam.</p>
<p>Online booking is no longer optional for new clients. Most practice management systems offer it or integrate with a booking tool. Limit it to appointment types that are safe to self-book (wellness exams, vaccines, new-client visits, nail trims) and route sick visits to a call. Put the booking button on your Business Profile, at the top of every page and in every ad.</p>
<p>The phone still matters for everything else. Three fixes we’d make in week one:</p>
<ul>
<li>Track every call by source and listen to a sample of new-client calls. Most practices have never heard how their own phones sound to a stranger. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers setup.</li>
<li>Answer new-client calls first. A separate line or a menu option for “new client” lets the front desk prioritize the call that’s worth the most.</li>
<li>Text back every missed call within five minutes with a booking link. See our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')}.</li>
</ul>"""),

            ("Wellness plans as a marketing tool", f"""<p>Price sensitivity is real. At the AVMA’s 2023 economics forum, data reported by {SRC['avma23']} showed the share of owners who strongly agreed they’d go to the vet less over the next year to save money rose from 10% to 19%. Client visits fell 2.7% over two years even as practice revenue rose 5.7%. Later AVMA data showed average household vet spending down 4%.</p>
<p>A wellness plan answers the price objection by spreading predictable care into a monthly payment. It also gives your marketing a concrete offer that a corporate group’s generic “membership” can’t beat on local relevance.</p>
<p>Heartworm is the Houston hook. Texas led the country in heartworm incidence for the first time in the American Heartworm Society’s latest survey, reported by {SRC['hw']} in April 2026. A plan that bundles year-round prevention, the annual test, vaccines and two exams speaks to a real local risk, and it keeps the pet on your schedule.</p>
<p>How we’d build and market one:</p>
<ul>
<li>Two or three tiers at most (puppy/kitten, adult, senior). More than that and the front desk can’t explain them.</li>
<li>Price it monthly, show the annual savings against à la carte, and list exactly what’s included.</li>
<li>Present it as a prepaid package of your own services, not as insurance, and have your attorney review the contract terms for cancellation and refunds.</li>
<li>Market it to new clients at the first exam and to existing clients in the reminder emails, rather than through cold ads.</li>
</ul>"""),

            ("Reminders, retention and lapsed clients", f"""<p>Keeping a client costs far less than finding one, and retention is where most independent practices quietly lose ground. The same AVMA data found lapsing patients (no visit in 14 to 18 months) rising significantly per practice from 2020 to 2023, with the average patient making 2.39 visits a year.</p>
<p>Your practice software can automate most of this:</p>
<ol>
<li>Reminders for vaccines, heartworm tests and dental cleanings at four weeks, two weeks and three days before due, by email and text.</li>
<li>A lapsed-client sequence at 13, 15 and 18 months with a direct booking link.</li>
<li>Prevention refill reminders tied to the dispensing date.</li>
<li>Seasonal emails timed to Houston: heatstroke and paw-pad burns in June, hurricane season prep (which runs June 1 to November 30) with a pet go-bag list and a records download, fireworks anxiety before the Fourth and New Year’s.</li>
</ol>
<p>Texts need consent. Appointment reminders about a pet you’re already treating are different from promotional texts, and Texas brought marketing texts under its telephone solicitation law through SB 140 effective September 1, 2025, with exemptions that may cover some businesses, per {SRC['sb140']}. Keep promotional consent separate and ask your attorney which exemptions apply. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} goes into the details.</p>"""),

            ("Client lifetime value: the number that sets your budget", f"""<p>Most clinics judge marketing on cost per new client. That’s the right instinct with the wrong ceiling, because a new client isn’t worth one visit.</p>
<p>Here’s an illustrative calculation. Your own numbers will differ, so pull them from your practice software:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Input</th><th>Illustrative value</th></tr></thead>
<tbody>
<tr><td>Average revenue per client per year</td><td>$650</td></tr>
<tr><td>Average pets per client</td><td>1.6</td></tr>
<tr><td>Average years a client stays</td><td>5</td></tr>
<tr><td>Gross margin on services</td><td>About 60%</td></tr>
<tr><td>Lifetime gross profit per client</td><td>About $1,950</td></tr>
</tbody></table></div>
<p>With numbers like those, paying $150 to $250 to acquire a client who stays is a good trade, which is far more than most practices allow themselves. The catch is the word “stays.” Lifetime value depends on retention, so the reminder system above is part of your acquisition budget.</p>
<!--fig:funnel-->
<p>An illustrative monthly marketing mix for a two-doctor independent practice: $1,500 to $3,000 on Google Ads, $500 to $1,000 on Meta for new movers, a few hundred on reviews and reminder software, and local SEO work on the website and profile. Judge it on booked first exams and on how many of those clients are still active a year later. Our {L('/services/paid-social-advertising/', 'paid social team')} runs the new-mover ads, and {L('/services/web-design-seo-pr/', 'web design and SEO')} covers the pages.</p>
<p>If you own an independent practice and want a plan built around your clinic and your neighborhoods, <a href="/contact/">get in touch</a>. A senior strategist will look at what you’re running and lay out what we’d change.</p>"""),
        ],
        "faq": [
            ("How do veterinary clinics get new clients?",
             "Most new clients find a vet through Google Maps after moving, getting a new pet or leaving a previous clinic. Win there with the Veterinarian primary category, accurate hours and services, a booking link, and a steady flow of recent reviews. Add Google search ads for new-client and service keywords, Meta ads around new subdivisions, and make sure every new-client call or online booking request is answered quickly."),
            ("What should an independent vet clinic do to compete with corporate hospitals?",
             "Compete on what a corporate group can’t standardize: the same doctors at every visit, local ownership, reviews that describe real people, and flexibility like same-day sick visits. Then fix the operational gaps that usually cost independents clients, such as unanswered phones, no online booking and no reminders. Those fixes cost less than trying to match a group’s ad budget."),
            ("Can a Texas veterinarian advertise as 24/7 or as a specialist?",
             "Be careful with both. Texas Board of Veterinary Medical Examiners rules ban advertising that is false, deceptive or misleading, including claims that create inflated expectations. Advertising round-the-clock care can imply a vet is always available. Only a veterinarian board certified in an AVMA-recognized specialty can claim to be a specialist, using wording such as Board Certified followed by the specialty."),
            ("How much should a vet clinic spend on Google Ads?",
             "Many independent practices start somewhere around $1,500 to $3,000 a month on search ads, depending on competition and how many new clients they can see. Industry benchmarks put Animals and Pets clicks around $4 on average, though Houston emergency searches cost more. Set your budget from client lifetime value and track booked first exams, not clicks, to decide whether to spend more."),
            ("Do wellness plans help a vet practice grow?",
             "They can. A wellness plan spreads predictable care into monthly payments, which eases price worries and keeps pets on your schedule. In Houston, bundling year-round heartworm prevention and testing is an easy story to tell, since Texas led the country in heartworm incidence in the latest survey. Keep it to two or three tiers and have an attorney review the contract terms."),
        ],
        "figures": {
            "pets": {
                "type": "stats",
                "title": "Who already has a vet",
                "stats": [["45.5%", "of U.S. households own a dog"], ["86.8%", "of dog owners have a regular vet"], ["57.3%", "of cat owners saw a vet last year"], ["4%", "drop in household vet spending"]],
                "note": "Source: AVMA 2024 Pet Ownership and Demographic Sourcebook (preliminary)",
                "alt": "Stats on pet ownership and veterinary visits that shape veterinary clinic marketing in The Woodlands and Houston",
                "caption": f"From {SRC['avma24']}. Most owners already have a vet, so timing matters.",
            },
            "map": {
                "type": "map",
                "title": "Where new pet owners are moving",
                "sub": "Fast-growing suburbs where clinics can reach new movers",
                "highlight": ["Conroe", "Montgomery", "Magnolia", "Tomball", "Cypress", "Katy", "Fulshear", "Spring"],
                "alt": "Map of fast-growing Greater Houston suburbs for veterinary clinic new-mover marketing near The Woodlands, Conroe and Katy",
                "caption": "Harris, Montgomery and Fort Bend all ranked among the fastest-growing U.S. counties in 2025 Census estimates.",
            },
            "claims": {
                "type": "compare",
                "title": "Vet ad claims: risky vs. safer",
                "left": {"title": "Risky under TBVME rules", "items": ["“Best vet in Houston”", "“Open 24/7” with no vet on site", "“Specialist in dermatology” (not boarded)", "“Guaranteed to cure allergies”", "“Pain-free surgery”"]},
                "right": {"title": "Safer, factual wording", "items": ["“4.9 stars from 600 Google reviews”", "“Open until 9 p.m., vet on site”", "“Board Certified (Veterinary Dermatology)”", "“Allergy testing and treatment plans”", "“Pain management with every surgery”"]},
                "alt": "Comparison of risky and safer veterinary ad claims under Texas Board of Veterinary Medical Examiners rules in The Woodlands and Houston",
                "caption": "State facts the public can check. Leave out guarantees and superiority claims.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for vet clinics",
                "sub": "Add before launch, then check search terms weekly",
                "items": ["Jobs: jobs, hiring, salary, vet tech school", "DIY: home remedy, how to, can I give", "Free: free, free clinic (unless you run one)", "Pet store clinic names you don’t compete with", "Shelter and rescue searches you can’t serve", "Livestock or equine if you’re small animal only", "Pet insurance quotes", "Online pharmacy and prescription searches"],
                "alt": "Checklist of negative keywords for veterinary clinic Google Ads in The Woodlands and Houston",
                "caption": "Keep low-cost spay and neuter terms only if you’re priced to compete on them.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From search to a client who stays",
                "stages": [["Clicks and Maps actions", "400"], ["Calls and booking requests", "80"], ["Booked first exams", "45"], ["Showed up", "38"], ["Active after 12 months", "27"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how veterinary clinic marketing in The Woodlands and Houston turns searches into long-term clients",
                "caption": "The last stage is the one that pays. Track it.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: physical therapy
    {
        "slug": "physical-therapy-clinic-marketing-houston",
        "title": "Physical Therapy Clinic Marketing in Houston: More Evaluations, Fewer Empty Slots",
        "seo_title": "Physical Therapy Clinic Marketing in Houston",
        "desc": "Physical therapy marketing in Houston: Texas direct access, physician referrals, Google Ads and SEO by condition, HIPAA-safe tracking, reviews, cost per eval.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Google Analytics"],
        "art": "b4",
        "hero": "chiro",
        "hero_alt": "Illustration of a spine and joints for physical therapy clinic marketing in Houston, The Woodlands and Katy",
        "related": ["chiropractor-marketing-the-woodlands-houston", "medical-practice-marketing-houston", "gym-fitness-studio-marketing-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Thursday, 4:30 p.m. Two cancellations in the last hour and a 5:15 that won’t show. The orthopedic group in Memorial City that used to send you fifteen referrals a month opened its own therapy department in the spring, and you’ve felt it ever since. Your Google Ads dashboard says 63 conversions last month. Your front desk booked nine new evaluations.</p>
<p>Both numbers are “true.” Only one of them pays rent.</p>
<p>Physical therapy clinic marketing in Houston has two halves. One is the referral relationships with physicians, surgeons and athletic trainers that most clinics were built on. The other is reaching patients directly, which got a lot more practical in Texas in 2025. Clinics that grow do both, and they measure one thing: cost per arrived evaluation.</p>
<p>This guide is for outpatient clinics with one to five locations across Houston, The Woodlands, Katy, Sugar Land, Pearland or Kingwood.</p>"""),

            ("Direct access in Texas: what changed in 2025", f"""<p>For years, Texas let a PT treat without a referral for only 10 consecutive business days, which was barely long enough to be worth marketing. HB 4099 changed that. Per {SRC['hb4099']}, the limit became 30 consecutive calendar days, the separate 15-business-day exception was repealed, and a referral is still required to keep treating past the limit. The law took effect September 1, 2025.</p>
<p>The board’s implementing rule spells out who qualifies. Under {SRC['r3221']}, effective November 1, 2025, the PT must have been licensed for at least one year, carry professional liability insurance of at least $100,000 per claim and $300,000 aggregate, and either hold a doctoral degree in physical therapy or have completed at least 30 CCUs in differential diagnosis. The patient also signs a board-prescribed disclosure form before treatment starts.</p>
<!--fig:direct-->
<p>What it means for marketing:</p>
<ul>
<li>You can advertise “no referral needed” honestly, as long as your treating PTs qualify and your intake handles the disclosure form.</li>
<li>Thirty days covers a real episode of care for many simple cases (ankle sprains, mild low back pain, early running injuries). Say what happens if they need more.</li>
<li>Insurance is a separate question. Plenty of commercial and managed plans still require a referral or prior authorization no matter what Texas law allows. Your intake team should check the plan before the first visit, and your website should say so.</li>
<li>Medicare runs on its own rules. A physician or qualified practitioner still has to certify the plan of care. For referred patients, Medicare added an exception in 2025: a signed and dated order in the record, plus evidence the plan of care went to the referring provider within 30 days of the evaluation, satisfies certification, per {SRC['apta']}.</li>
</ul>"""),

            ("Physician referrals are still the backbone", f"""<p>Direct access is a growth channel. For most clinics, referrals are still the base, and they erode quietly when nobody tends them.</p>
<p>What keeps a referral source sending patients is mostly boring:</p>
<ol>
<li><b>Fast scheduling.</b> Surgeons’ offices want their post-op patients seen within days. If your next opening for a new ACL reconstruction is two weeks out, they’ll send the next one elsewhere.</li>
<li><b>Clean communication.</b> Send the eval summary and plan of care promptly, then progress notes at set intervals. For Medicare patients the 30-day plan-of-care window gives you a natural deadline.</li>
<li><b>One point of contact.</b> Someone at your clinic owns each referring office, knows the MA and the scheduler by name, and visits in person.</li>
<li><b>Tracking by source.</b> Count referrals by physician each month. A drop from eight to three is a phone call this week, not a surprise in December.</li>
</ol>
<p>Where you look matters in Houston. Orthopedic and sports medicine groups cluster around the Texas Medical Center, Memorial City, The Woodlands and Sugar Land, and many now own therapy services. Independent surgeons, pain management practices, OB-GYNs (for pelvic health), podiatrists and primary care groups are often the better targets. So are high school and club athletic trainers in Katy ISD, Cy-Fair ISD and Conroe ISD territory.</p>
<p>Keep it clean. Gifts, free services or anything of value given to referral sources raise federal anti-kickback questions, especially with Medicare patients. A lunch-and-learn about your post-op protocols is normal practice; anything more generous needs a call to your healthcare attorney first.</p>"""),

            ("Insurance and cash-pay patients need different marketing", f"""<p>A patient with a PPO looking for help after a rotator cuff repair cares about “in network,” “near me” and “how soon.” A runner training for the Chevron Houston Marathon who wants a gait analysis and dry needling cares about expertise and results, and will often pay cash to skip the insurance hassle.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Insurance-based patient</th><th>Cash-pay patient</th></tr></thead>
<tbody>
<tr><td>What they search</td><td>physical therapy near me, PT that takes Blue Cross, post-surgery physical therapy Katy</td><td>sports physical therapy, pelvic floor therapist The Woodlands, dry needling Houston</td></tr>
<tr><td>What the page must show</td><td>Plans accepted, how to check benefits, referral and authorization rules, next opening</td><td>Price per session or package, the therapist’s training, what a visit includes, results timeline</td></tr>
<tr><td>Best channels</td><td>Physician referrals, Google Maps, search ads, LSA</td><td>Search ads, Instagram and YouTube video, running and pickleball clubs, gyms</td></tr>
<tr><td>Key number</td><td>Cost per arrived eval, visits per plan of care</td><td>Cost per eval, package conversion rate</td></tr>
</tbody></table></div>
<p>Pelvic health is the clearest cash-pay or out-of-network opportunity we see, and it’s underserved in the suburbs. Postpartum patients in Cypress or Pearland often drive into the city for it. A clinic in those areas with a trained pelvic health therapist has a real reason to advertise.</p>
<p>A note on free offers. A “free 15-minute injury screen” is common and can work. If you see Medicare or Medicaid patients, giveaways to those beneficiaries are limited by {SRC['oig']}, which caps gifts of nominal value at $15 per item and $75 per year per beneficiary, with no cash or cash equivalents. Have your compliance person sign off on the offer before it runs.</p>"""),

            ("SEO for condition-specific searches", f"""<p>Patients search by problem, rarely by profession. “Lower back pain treatment Sugar Land.” “Physical therapy for sciatica.” “Knee replacement rehab near me.” “Vertigo treatment Houston.” A clinic with a single “Services” page listing twenty conditions in bullet points won’t rank for any of them.</p>
<p>Build one page per condition you want more of, and make each one useful:</p>
<ul>
<li>What the problem usually is and how you evaluate it, in plain language.</li>
<li>What treatment looks like, typical number of visits, and when to expect improvement (as a range, without promises).</li>
<li>Whether they need a referral, with the direct access rules in a sentence.</li>
<li>Insurance accepted and cash-pay pricing if you offer it.</li>
<li>Which therapist leads that program, with credentials.</li>
<li>A booking button and a phone number at the top.</li>
</ul>
<p>Good starting pages for most Houston clinics: low back pain, neck pain, sciatica, post-surgical rehab (ACL, rotator cuff, total knee and hip), sports injuries, running injuries, pelvic health, vestibular and vertigo, and work injuries if you take workers’ comp. Then add location pages for each clinic, since “physical therapy Katy” and “physical therapy Kingwood” are separate searches with separate map packs.</p>
<p>Keep the claims factual. The Texas PT board can discipline advertising that’s false, misleading or deceptive under rule 322.4(b)(12), and {SRC['ptadv']} lists claims of superiority and promises that a patient will get better fast as examples of what not to say. “Our therapists have treated thousands of post-op knees” is fine if true. “The best PT in Houston, back to normal in two weeks” isn’t.</p>
<p>Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} covers location pages, and {L('/blog/seo-cost-houston-the-woodlands/', 'what SEO costs in Houston')} will help you budget for the content.</p>"""),

            ("Google Ads for physical therapy clinics", f"""<p>Search ads work for PT because the intent is so specific. Someone typing “physical therapy for shoulder pain near me” is a patient, today.</p>
<p>A starting structure:</p>
<ul>
<li><b>General:</b> physical therapy near me, physical therapist [town], PT clinic [neighborhood].</li>
<li><b>Condition:</b> one ad group per condition page above, sending traffic to that page.</li>
<li><b>Post-surgical:</b> ACL rehab, rotator cuff surgery physical therapy, knee replacement physical therapy.</li>
<li><b>Specialty programs:</b> pelvic floor physical therapy, vestibular therapy, dry needling, sports PT.</li>
<li><b>Brand:</b> your clinic names.</li>
</ul>
<p>Negatives matter more in PT than most niches, because so many searches come from students and job seekers:</p>
<!--fig:negatives-->
<p>Sample copy for a condition ad group. Headlines: “Back Pain Physical Therapy, Katy,” “No Referral Needed for Most Patients,” “Evaluations This Week.” Description: “One-on-one sessions with a doctor of physical therapy. Most major plans accepted. Book your evaluation online.”</p>
<p>For a sense of cost, {SRC['ws']} reported a median $4.76 cost per click, a 12.43% conversion rate and a $40.04 cost per lead for Physicians &amp; Surgeons search campaigns from April 2025 to March 2026. PT doesn’t have its own category in that report, so treat it as a rough proxy. A lead isn’t an eval, and the section on measurement below is where the real number lives.</p>
<p>Two policy limits shape targeting. {SRC['ghealth']} bars advertiser-curated audiences for health content, including Customer Match lists and your data segments (the lists remarketing runs on), along with lookalikes and audience expansion. In practice that pushes PT clinics toward keyword and location targeting, which is where the intent is anyway. And Google’s Local Services Ads include a Physical therapist category, per {SRC['lsa']}, though booking leads aren’t available for health care verticals, so you’ll get calls and messages. Our {L('/services/search-marketing/', 'search marketing team')} manages both.</p>"""),

            ("HIPAA, pixels and remarketing: what you can and can’t track", f"""<p>This is where PT clinics get into real trouble, usually by accident. A website builder or a well-meaning agency installs the Meta pixel and Google tags on every page, including the appointment request form and the intake paperwork. Now a third party gets the fact that a named person booked pelvic floor therapy.</p>
<p>The federal guidance has a history. HHS’s Office for Civil Rights issued a bulletin on tracking technologies in 2022 and revised it in March 2024. In June 2024, a federal court in Fort Worth vacated the part that treated an IP address plus a visit to an unauthenticated public page about a health condition as protected health information. The rest of the bulletin wasn’t vacated, and it still applies to logged-in patient portals and other authenticated pages, per {SRC['hk']}.</p>
<p>So the practical lines, in our experience working with health clients and their counsel:</p>
<!--fig:tracking-->
<p>Meta adds its own layer. Starting in 2025, Meta began restricting which events health and wellness advertisers can send, with events like Schedule commonly affected and custom events requiring review, according to {SRC['fresh']}, which notes Meta hasn’t publicly confirmed all the details. If your Meta campaigns suddenly can’t optimize for bookings, that’s likely why.</p>
<p>The answer for most clinics: track conversions as “a booking happened” without the condition or the person attached, use a vendor that will sign a business associate agreement for anything touching patient data, keep pixels off forms and portals, and import arrived evaluations from your EMR as offline conversions without health details. Talk to your compliance advisor before you change any of it. Our {L('/blog/medical-practice-marketing-houston/', 'medical practice marketing guide')} covers more of the healthcare-specific setup.</p>"""),

            ("Reviews without a HIPAA problem", f"""<p>Reviews drive map rankings for PT the same way they do for anyone. PT has two extra constraints.</p>
<p>First, how you reply. In 2023, {SRC['manasa']} with a New Jersey provider that replied to negative online reviews with details of patients’ diagnoses and treatment. Never confirm that a reviewer is a patient, and never mention their condition or care, even if they did. A safe reply: “Thank you for the feedback. We take every concern seriously and would like to talk. Please call our clinic manager at [number].” Same reply for a glowing review, minus the concern.</p>
<p>Second, how you ask. Google’s policy bars incentives, gating and asking for specific content, per {SRC['gpol']}. The best moment is the discharge visit or the session where a patient hits a milestone (first pain-free run, back to golf at Woodforest). A text that evening with the link does the rest.</p>
<p>Patient stories on your website and social media are different from Google reviews. Get a signed HIPAA authorization before using anyone’s name, photo, video or story, keep it on file, and don’t publish results that read as a promise. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has more templates.</p>"""),

            ("Measuring cost per evaluation", f"""<p>Back to Thursday: 63 conversions, nine evals. That gap is what most PT marketing reports hide.</p>
<p>Define the stages and count each one every month:</p>
<!--fig:funnel-->
<p>Then divide. Cost per arrived evaluation is total marketing spend for a channel divided by evals that actually happened from it. Track it by channel (Google Ads, LSA, Meta, organic, each referring physician) and you’ll know where to put the next dollar.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Illustrative month (one clinic)</th></tr></thead>
<tbody>
<tr><td>Google Ads spend</td><td>$3,000</td></tr>
<tr><td>Calls and form requests</td><td>75</td></tr>
<tr><td>Booked evaluations</td><td>32</td></tr>
<tr><td>Arrived evaluations</td><td>26</td></tr>
<tr><td>Cost per arrived evaluation</td><td>About $115</td></tr>
<tr><td>Average visits per plan of care</td><td>9</td></tr>
</tbody></table></div>
<p>Those numbers are made up for illustration, and your reimbursement mix decides what a good number is. An arrived eval that turns into nine visits is worth far more than one that drops after two. Watch plan-of-care completion alongside cost per eval, because no-shows after visit three are a scheduling and retention problem marketing can’t fix.</p>
<p>The fastest improvement is usually at the front desk: how quickly new requests get a call back, whether insurance is verified the same day, and whether the first appointment is offered within 48 hours. Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')} applies directly, and {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'our tracking guide')} covers wiring calls and forms into Google Ads.</p>"""),

            ("A first 90 days for a Houston PT clinic", f"""<!--fig:plan-->
<p>Budget-wise, we’d start a single-location clinic at roughly $2,000 to $4,000 a month in search ads plus content work on condition pages, then scale the channels with the best cost per arrived evaluation. That range is illustrative and depends on your area. Katy and The Woodlands are more competitive than a clinic in Humble or Conroe.</p>
<p>If you run a PT clinic and want a plan that covers referrals, direct access and tracking that won’t get you a letter from a lawyer, <a href="/contact/">get in touch</a>. Tell us about your clinics and goals, and a senior strategist will build a plan around them. If you also own a chiropractic practice, our {L('/blog/chiropractor-marketing-the-woodlands-houston/', 'chiropractor marketing post')} covers that side.</p>"""),
        ],
        "faq": [
            ("Can you see a physical therapist without a referral in Texas?",
             "Yes, within limits. Since HB 4099 took effect in September 2025, a qualified Texas physical therapist can treat a patient without a referral for up to 30 consecutive calendar days. The PT must have been licensed at least a year, carry required liability insurance, and hold a doctoral degree or 30 CCUs in differential diagnosis. A referral is required to continue, and insurance plans may have their own rules."),
            ("How do physical therapy clinics get more patients?",
             "Most grow through two channels at once. Physician referrals still matter, so schedule post-op patients fast and send plans of care promptly. Direct-to-patient marketing fills the rest: a strong Google Business Profile, a page for each condition you treat, search ads on condition keywords, and steady reviews. Track arrived evaluations by source, because leads alone hide where patients actually come from."),
            ("Can a physical therapy clinic use Facebook pixel and Google remarketing?",
             "Carefully. HHS guidance on tracking technologies still applies to logged-in portals and authenticated pages, so keep pixels off intake forms, booking flows and portals. Google bars Customer Match and remarketing lists for health content, and Meta restricts some events for health advertisers. Track conversions without health details, use vendors that sign business associate agreements, and have a compliance advisor review your setup."),
            ("How much does Google Ads cost for physical therapy?",
             "Recent benchmarks for Physicians and Surgeons search campaigns show median clicks near $4.76 and leads near $40, which is a rough proxy for PT. Many single-location Houston clinics start around $2,000 to $4,000 a month. The number that matters is cost per arrived evaluation, so track how many leads become booked and attended evals before deciding to spend more."),
            ("How should a PT clinic respond to online reviews?",
             "Never confirm that the reviewer is a patient or mention their condition or treatment, even if they did. HHS settled with a provider for $30,000 over review replies that disclosed patient details. Thank the reviewer, say you take concerns seriously, and invite them to call the clinic manager. Ask every discharged patient for a review by text, without incentives or screening for happy patients."),
        ],
        "figures": {
            "direct": {
                "type": "stats",
                "title": "Texas direct access after HB 4099",
                "stats": [["30", "consecutive calendar days without referral"], ["1 yr", "minimum licensure to qualify"], ["$100K", "per-claim liability coverage required"], ["Nov 1", "2025 board rule effective date"]],
                "note": "Source: HB 4099 bill analysis; Texas PT board rule 322.1",
                "alt": "Stats on Texas physical therapy direct access rules after HB 4099 for PT clinic marketing in Houston",
                "caption": f"From {SRC['hb4099']} and {SRC['r3221']}. Insurance rules still apply separately.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for PT clinics",
                "sub": "Add before launch",
                "items": ["Jobs: jobs, hiring, salary, travel PT, PRN", "School: DPT program, PTA school, prerequisites", "Licensing: NPTE, CEU, license renewal", "DIY: exercises pdf, at home, YouTube, stretches", "Equipment: TENS unit, foam roller, for sale", "Pets: canine rehab, dog physical therapy", "Free: free (unless you run a free screen)", "Massage-only searches, if you don’t offer it"],
                "alt": "Checklist of negative keywords for physical therapy Google Ads in Houston and The Woodlands",
                "caption": "Then read the search terms report weekly for the first month.",
            },
            "tracking": {
                "type": "compare",
                "title": "PT website tracking: risky vs. safer",
                "left": {"title": "Risky setup", "items": ["Meta pixel on the intake form", "Tags inside the patient portal", "Condition names in conversion events", "Patient emails uploaded to ad platforms", "No BAA with tracking vendors"]},
                "right": {"title": "Safer setup", "items": ["Pixels kept off forms and portals", "Generic ‘booking’ conversion only", "Offline conversions without health details", "Keyword and location targeting", "Vendors that sign a BAA"]},
                "alt": "Comparison of risky and safer website tracking setups for HIPAA and physical therapy clinic marketing in Houston",
                "caption": "Our experience, not legal advice. Have your compliance advisor review your setup.",
            },
            "funnel": {
                "type": "funnel",
                "title": "Where PT leads actually go",
                "stages": [["Ad clicks and Maps actions", "600"], ["Calls and form requests", "75"], ["Booked evaluations", "32"], ["Arrived evaluations", "26"], ["Completed plan of care", "17"]],
                "note": "Illustrative example",
                "alt": "Funnel of physical therapy clinic leads in Houston from clicks to arrived evaluations and completed plans of care",
                "caption": "Platform “conversions” sit at the second stage. Revenue sits at the last two.",
            },
            "plan": {
                "type": "steps",
                "title": "First 90 days for a PT clinic",
                "sub": "Fix the base, then add paid reach",
                "steps": [["Days 1-15: tracking", "Call tracking, pixel cleanup, offline eval imports, one funnel report."], ["Days 1-30: profile and intake", "Business Profile categories and services, 48-hour first visit, same-day insurance checks."], ["Days 15-45: referrals", "Referral counts by physician, an owner for each office, faster post-op scheduling."], ["Days 30-60: pages", "Four to six condition pages and a page per location."], ["Days 45-90: ads", "Condition search campaigns, LSA test, budget moved toward the lowest cost per eval."]],
                "alt": "Ninety-day marketing plan steps for a physical therapy clinic in Houston and The Woodlands",
                "caption": "The order matters. Ads sent into a broken intake process just cost more.",
            },
        },
    },
]
