"""Batch 10: senior living / assisted living marketing in Houston and The Woodlands, plastic surgeon marketing in
Houston, and urgent care clinic marketing in Houston.

Research: Senior Housing News on NIC MAP 3Q 2026 occupancy (90.4% primary markets, assisted living 89.1%, Houston
87.3%); CareScout 2025 Cost of Care (assisted living national median $6,200/month); Texas HHS assisted living page
(Type A/Type B, violations data); Texas Health & Safety Code 247.029 (Alzheimer's classification required to advertise
memory care); KPRC 2 Investigates on the Texas HHS LTC Provider Search; Texas SB 1383 (89R) enrolled text, Business &
Commerce Code ch. 121 (referral agency disclosures, three-year cap on referral periods) and BillTrack50 status (enacted
June 20, 2025); Senior Housing News on Sen. Casey's 2024 letter to A Place for Mom ("the community only pays for first
month's rent and care"); Jon Loomer on Meta housing special ad category; Mannix Marketing on senior living falling under
housing; Google housing personalized ads FAQ; HHS covered entity definition.
Plastic surgery post: ASPS 2024 procedural statistics press release (1.6 million cosmetic surgical procedures, top five)
and 2024 average surgeon fee ranges; Texas Medical Board board certification advertising page (Rule 164.4: ABMS, AOA BOS,
substantially equivalent); 22 TAC 164.3 via Justia ("board eligible" banned, testimonial disclaimers, models identified,
cost claims); TMA on testimonials; ABPS verification page; HHS marketing authorization guidance; Fierce Healthcare on the
Elite Dental Associates (Dallas) $10,000 OCR settlement over Yelp replies; Morgan Lewis on the FTC reviews rule (effective
Oct 21, 2024, $51,744 per violation); Search Engine Land on Meta health and wellness event restrictions; OuterBox on Meta
cosmetic procedure and personal attributes policies; PPC Land on Google removing mature cosmetic procedures from the sexual
content policy (Sept 2025); HHS online tracking bulletin.
Urgent care post: UCA's The Check In (15,309 centers end of 2025, 611 opened, Texas led with 66); HB 2041 (86R) enrolled
text (FSER notice language, insurance advertising limits, website "Insurance Information" page); Texas Tribune on 2019
FSER laws (200+ FSERs, AARP 77% finding, HB 1941 200% rule); Texas HHS Form 3226 instructions; Google Business Profile
guidelines (one profile per location, special hours, practitioners); CDC flu season page (peaks Dec-Feb, February most
common); UIL Section 1205 (physical in first and third years of high school, yearly medical history); FMCSA on National
Registry examiners (May 21, 2014); CMS No Surprises Act provider responsibilities (good faith estimate, $400 dispute
threshold); HHS online tracking bulletin and AHA v. Becerra (June 20, 2024).
Competitor and PAA phrasing read for "senior living marketing", "assisted living marketing ideas", "how to increase
occupancy assisted living", "plastic surgery marketing", "plastic surgeon google ads", "urgent care marketing", "urgent
care google ads", "how to increase urgent care patient volume".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # senior living post
    "nic": A("https://seniorhousingnews.com/2026/10/01/more-than-half-of-primary-markets-have-90-average-senior-living-occupancy-or-higher/", "Senior Housing News’ write-up of NIC MAP’s third-quarter 2026 data"),
    "carescout": A("https://www.businesswire.com/news/home/20260302283881/en/CareScout-Releases-2025-Cost-of-Care-Survey-Results", "CareScout’s 2025 Cost of Care Survey"),
    "hhsalf": A("https://www.hhs.texas.gov/node/2306", "Texas HHS’s assisted living page"),
    "hsc247": A("https://texas.public.law/statutes/tex._health_and_safety_code_section_247.029", "Texas Health and Safety Code § 247.029"),
    "kprc": A("https://gmg-kprc-prod.cdn.arcpublishing.com/news/investigates/2025/05/12/2-investigates-finding-the-best-care-facility-for-your-loved-ones-how-to-check-past-issues/", "KPRC 2’s guide for families"),
    "sb1383": A("https://capitol.texas.gov/tlodocs/89R/billtext/html/SB01383F.htm", "SB 1383"),
    "sb1383s": A("https://www.billtrack50.com/billdetail/1837462", "enacted in June 2025"),
    "casey": A("https://seniorhousingnews.com/2024/06/20/us-senator-probes-a-place-for-mom-alleging-deceptive-practices/", "Senior Housing News"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "mannix": A("https://mannixmarketing.com/blog/senior-living-special-ads-category", "most senior living marketers read it"),
    "gfaq": A("https://support.google.com/adspolicy/answer/9997418?hl=en", "Google’s housing policy FAQ"),
    "hhsce": A("https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html", "HHS’s definition of a covered entity"),
    # plastic surgery post
    "asps": A("https://www.plasticsurgery.org/news/press-releases/interest-in-aesthetic-health-remained-consistent-despite-economic-uncertainty-in-2024-according-to-new-report-from-american-society-of-plastic-surgeons", "ASPS’s 2024 procedural statistics"),
    "aspsfee": A("https://www.plasticsurgery.org/documents/news/statistics/2024/cosmetic-procedures-average-cost-2024.pdf", "ASPS’s 2024 average fee ranges"),
    "tmbcert": A("https://tmb.state.tx.us/page/resources-advertisement-board-certification", "the Texas Medical Board’s board certification advertising page"),
    "tmb1643": A("https://regulations.justia.com/states/texas/title-22/part-9/chapter-164/section-164-3", "TMB Rule 164.3"),
    "tma": A("https://www.texmed.org/template.aspx?id=1688", "the Texas Medical Association"),
    "abps": A("https://abplasticsurgery.org/public/verify-certification/", "ABPS’s public verification tool"),
    "hhsmkt": A("https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/marketing/index.html", "HHS’s marketing guidance"),
    "elite": A("https://www.fiercehealthcare.com/practices/dental-practice-pays-10k-to-settle-complaint-it-disclosed-patient-information-social", "paid $10,000 to settle"),
    "ftcrule": A("https://www.morganlewis.com/pubs/2024/08/ftc-issues-final-rule-on-consumer-reviews-and-testimonials", "the FTC’s consumer reviews rule"),
    "sel": A("https://searchengineland.com/meta-ads-restrictions-health-wellness-campaigns-453094", "Search Engine Land"),
    "outerbox": A("https://www.outerboxdesign.com/articles/digital-marketing/how-health-and-wellness-brands-can-keep-their-ads-compliant-on-meta-and-other-social-media-platforms/", "OuterBox’s summary of Meta’s health ad rules"),
    "ppcl": A("https://ppc.land/google-removes-mature-cosmetic-procedure-restrictions-from-sexual-content-policy/", "PPC Land"),
    "hhstrack": A("https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html", "HHS’s bulletin on online tracking technologies"),
    # urgent care post
    "uca": A("https://thecheckin.urgentcareassociation.org/2025-recap-new-urgent-care-centers/", "the Urgent Care Association’s 2025 recap"),
    "hb2041": A("https://capitol.texas.gov/tlodocs/86R/billtext/html/HB02041F.HTM", "HB 2041"),
    "tt": A("https://www.texastribune.org/2019/06/03/freestanding-emergency-centers-bills-legislature/", "the Texas Tribune"),
    "form3226": A("https://www.hhs.texas.gov/node/280776", "Texas HHS"),
    "gbp": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s Business Profile guidelines"),
    "cdc": A("https://www.cdc.gov/flu/about/season/", "the CDC"),
    "uil": A("https://www.uiltexas.org/policy/constitution/athletics/eligibility", "UIL Section 1205"),
    "fmcsa": A("https://www.fmcsa.dot.gov/newsroom/dot-reminds-commercial-drivers-physicals-must-now-be-performed-certified-medical-examiners", "FMCSA"),
    "cmsgfe": A("https://www.cms.gov/files/document/nsa-key-responsibilities-providers.pdf", "CMS’s No Surprises Act summary for providers"),
}

SENIOR = "/blog/senior-living-marketing-houston-the-woodlands/"
PLASTIC = "/blog/plastic-surgeon-marketing-houston/"
URGENT = "/blog/urgent-care-clinic-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: senior living
    {
        "slug": "senior-living-marketing-houston-the-woodlands",
        "title": "Senior Living and Assisted Living Marketing in Houston and The Woodlands",
        "seo_title": "Senior Living Marketing in Houston & The Woodlands",
        "desc": "Senior living and assisted living marketing for Houston and The Woodlands: adult-child buyers, tours, referral agency fees, Meta housing rules, move-in math.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b5",
        "hero": "house",
        "hero_alt": "Illustration of caregiving for senior living and assisted living marketing in Houston and The Woodlands",
        "related": ["how-do-home-care-agencies-get-clients", "home-care-seo-the-woodlands-houston", "speed-to-lead-response-time-follow-up-crm"],
        "sections": [
            (None, f"""<p>Tuesday, 9:20 p.m. A daughter in Katy gets home from a 12-hour shift. Her mother fell again last week, this time in the garage of the house in Spring she won’t leave. The daughter types “memory care near The Woodlands” into her phone, taps the first big directory result, and fills out a form with her name and number.</p>
<p>By 9:30 four communities have called her. By Thursday she’s toured two. Your community’s sales director calls Wednesday at 10 a.m., gets voicemail, and logs the lead as “attempted.”</p>
<p>That’s senior living marketing in Houston in one week. The family is in a hurry and emotionally wrung out. The person deciding is often not the person moving in. The first community to have a real conversation usually gets the tour, and the tour is where move-ins come from.</p>
<p>This guide is for assisted living, memory care and independent living operators in Greater Houston, from single 40-bed Type B buildings in Tomball to larger campuses in The Woodlands, Sugar Land and Kingwood. It covers who you’re really selling to, what referral agencies cost you, what Texas licensing means for your marketing, the ad platform rules, and how to measure cost per move-in instead of cost per lead.</p>"""),

            ("Who’s actually buying: the adult child, then the parent", f"""<p>Most of the people searching for assisted living aren’t the future resident. They’re daughters and sons in their 40s, 50s and 60s, often juggling jobs and kids, sometimes living in Dallas or Denver while mom lives in Conroe. Spouses are the second big group. The prospective resident usually comes in later, and sometimes reluctantly.</p>
<p>That changes nearly everything about the marketing:</p>
<ul>
<li><b>The search happens at night and on phones.</b> In accounts we’ve run for appointment-based businesses, evening and weekend form fills are a large share of the total. Senior living inquiries skew the same way, which is exactly when most sales offices are closed.</li>
<li><b>Two audiences, two messages.</b> The adult child wants safety, staffing, cost and proof. The parent wants to know they’ll keep their dignity, their routines, maybe their dog. Your site and your tour need both.</li>
<li><b>The trigger is usually a crisis.</b> A fall, a hospital discharge, a diagnosis, a caregiver burning out. Families that call after a hospital stay may need a decision within days. Families researching “before it gets bad” may take a year.</li>
<li><b>Siblings vote.</b> The daughter who toured has to sell it to her brother in Austin. Give her something to forward: a pricing sheet, a care-level explainer, a short video of the actual apartment.</li>
</ul>
<p>So you’re running two sales cycles at once. One is a fast crisis placement where speed and availability win. The other is a slow considered purchase where nurture wins. Most marketing plans only build for one of them.</p>"""),

            ("Houston occupancy and the math of a move-in", f"""<p>Houston has more open apartments than most big senior housing markets right now. NIC MAP’s third-quarter 2026 numbers put average occupancy across the 31 primary markets at 90.4%, with assisted living at 89.1% and independent living at 91.7%. Houston averaged 87.3%, one of the three lowest of those markets, ahead of only Atlanta and Miami, per {SRC['nic']}.</p>
<!--fig:market-->
<p>For your marketing budget, that gap is the whole story. Here’s the math we walk operators through. These are illustrative numbers, so swap in your own:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Input</th><th>Illustrative value</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Units</td><td>100</td><td>Each occupancy point is one apartment</td></tr>
<tr><td>Average monthly rate (rent plus care)</td><td>$6,200</td><td>CareScout’s 2025 national assisted living median</td></tr>
<tr><td>Average length of stay</td><td>20 months</td><td>Use your own move-out data</td></tr>
<tr><td>Lifetime revenue per move-in</td><td>$124,000</td><td>Rate times length of stay</td></tr>
<tr><td>Going from 87% to 92% occupancy</td><td>5 more residents</td><td>About $31,000 more revenue a month</td></tr>
</tbody></table></div>
<p>The $6,200 figure is the national median monthly cost for assisted living in 2025, up 5% from 2024, according to {SRC['carescout']}. Houston rates vary widely by building age, location and care level, so use your own rent roll.</p>
<p>With lifetime value in six figures, a cost per move-in of several thousand dollars can still be a great deal. The trouble is that most operators can’t tell you their cost per move-in by channel. They know cost per lead, which tells you very little. Everything below is built to fix that.</p>"""),

            ("Referral agencies: A Place for Mom and the others, and what they cost you", f"""<p>Referral and placement agencies are the reason that daughter in Katy got four calls in ten minutes. National directories and local placement agents capture a large share of the families searching online, then pass those families to partner communities. The community pays when the resident moves in.</p>
<p>The fee is large. When Sen. Bob Casey opened a Senate Aging Committee inquiry into A Place for Mom in June 2024, his letter quoted the company’s own website saying that on move-in, “the community only pays for first month’s rent and care,” and argued that communities pass those costs on to families, per {SRC['casey']}. Contracts vary by agency, so read yours line by line.</p>
<p>Texas now regulates these agencies. {SRC['sb1383']}, {SRC['sb1383s']}, added Chapter 121 to the Business and Commerce Code. Among other things, an agency has to give the family a written disclosure at the time of referral covering its services, who pays the fee, that the family can stop using the agency at any time, and that its list may not include every community that fits. Agencies can’t require a community to contract with them, can’t collect after the referral period in the contract expires, and that period can’t exceed three years after the referral. They also have to notify you in writing of each referral, with the date and time, on or before admission.</p>
<p>What we’d do with that as an operator:</p>
<ul>
<li><b>Log every lead’s first touch with a timestamp.</b> If a family found you directly on Google in March and an agency refers them in May, you want proof of who came first. Most agency contracts have a process for this, and it only works if your CRM is clean.</li>
<li><b>Check referral periods.</b> A referral from 2024 shouldn’t produce a fee on a 2027 move-in. The Texas cap is three years, and your contract may be shorter.</li>
<li><b>Treat agencies as a channel with a price.</b> If an agency move-in costs a month of rent and care and your own Google Ads move-in costs a fraction of that, shift budget. If you’re at 78% occupancy with no direct pipeline, keep the agencies while you build one.</li>
</ul>
<!--fig:referral-->
<p>The goal is rarely to cut agencies off. It’s to stop needing them for most of your move-ins.</p>"""),

            ("Texas licensing, memory care claims and the inspection data families read", f"""<p>Texas licenses assisted living facilities through Health and Human Services, and the license type should shape what you promise in your ads. Per {SRC['hhsalf']}, a Type A facility cares for residents who don’t need routine attendance during sleeping hours and can follow directions in an emergency. A Type B facility serves residents who may not be able to follow directions in an emergency, need help to evacuate, and need nighttime attendance.</p>
<p>Memory care has its own rule. Under {SRC['hsc247']}, the state sets up a separate classification and license for a facility that “advertises, markets, or otherwise promotes” that it provides personal care to residents with Alzheimer’s disease or related disorders. Read that as a marketing rule: if your Google ads, Facebook posts or website say “memory care” or “Alzheimer’s care,” make sure your certification covers it. Your administrator and attorney should sign off on the wording before your agency writes a single ad.</p>
<p>Families also do their homework now. The Texas HHS Long-term Care Provider Search shows inspection information for assisted living facilities, and KPRC 2 walked Houston families through using it, along with open records requests and the long-term care ombudsman, in {SRC['kprc']}. Texas HHS also posts a statewide assisted living violations data file on its assisted living page.</p>
<p>So assume the adult child has looked you up. Our advice is to address it on the tour instead of hoping it doesn’t come up. If you had a citation, say what changed. Families forgive a fixed problem far more readily than a dodge.</p>"""),

            ("The website: pricing, care levels and a tour button on every page", f"""<p>Most senior living websites we review have beautiful photos of a dining room and a “contact us for pricing” button. The adult child at 9:20 p.m. wants something else: what does it cost, what’s included, do you have an opening, and can I see it Saturday.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Page</th><th>What the family is asking</th><th>What it should show</th></tr></thead>
<tbody>
<tr><td>Pricing and what’s included</td><td>“Can we afford this?”</td><td>Starting rates by apartment type, how care levels are assessed and priced, community fee, what’s extra (incontinence care, medication management, second person)</td></tr>
<tr><td>Assisted living</td><td>“What help will Mom get?”</td><td>Daily care, staffing pattern by shift, nurse coverage, medication management, license type</td></tr>
<tr><td>Memory care</td><td>“Is it safe for Dad?”</td><td>Secured environment, staff training, programming, Alzheimer’s certification, how residents move between levels</td></tr>
<tr><td>Floor plans</td><td>“Will her furniture fit?”</td><td>Dimensions, photos of a real apartment, current availability by plan</td></tr>
<tr><td>Respite stays</td><td>“Can we try it first?”</td><td>Minimum stay, daily rate, what the family needs to bring</td></tr>
<tr><td>Area page</td><td>“Assisted living near Spring”</td><td>Drive times from Spring, Kingwood, Tomball or Conroe, nearby hospitals, the church or senior center you partner with</td></tr>
</tbody></table></div>
<p>Publishing starting prices scares a lot of operators. But the families you lose by showing $5,800 a month were never going to move in at $5,800. And the families who stay on the page now trust you a little more than the community hiding its number. Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} builds these pages, and the {L('/blog/home-care-seo-the-woodlands-houston/', 'home care SEO guide')} covers ranking for the same family searches from the in-home side.</p>
<p>Every page needs a “schedule a tour” button that actually books a time. A calendar beats a form that says “we’ll be in touch.”</p>"""),

            ("Google Ads for “assisted living near me” and “memory care [town]”", f"""<p>Search is where crisis families show up. The terms are specific and the intent is high: “assisted living The Woodlands,” “memory care Sugar Land,” “respite care for elderly Houston,” “independent living Kingwood,” and the near-me versions of all of them.</p>
<p>How we’d set up a single community:</p>
<ul>
<li>Separate ad groups by care level (assisted living, memory care, independent living, respite), each landing on its own page.</li>
<li>Town and neighborhood keywords for a realistic radius. Families usually want mom within 20 to 30 minutes of whoever visits most.</li>
<li><b>Location setting.</b> This is the rare business where Google’s “presence or interest” option can make sense, because the daughter in Dallas searching for “assisted living Conroe TX” is a real buyer. Watch the search terms closely if you turn it on.</li>
<li>A brand campaign, so directories don’t sit above your own name.</li>
<li>Call assets scheduled only for hours when a sales counselor or trained receptionist answers. After hours, send people to the tour calendar.</li>
</ul>
<p>Negatives to add on day one: jobs, hiring, careers, CNA, caregiver jobs, salary, “certification class,” nursing school, “free,” Medicaid and “low income” (only if you don’t accept Medicaid waiver residents), “nursing home abuse,” lawsuit, attorney, and “how to start an assisted living.”</p>
<p>On policy: {SRC['gfaq']} defines housing as homes, apartments and other housing for sale or rent and doesn’t mention senior living by name. If Google flags your campaigns as housing, you’ll lose ZIP code targeting and demographic targeting, which hurts less than you’d think, because a keyword like “memory care Tomball” already says who’s searching. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a sense of click prices, and our {L('/services/search-marketing/', 'search marketing team')} runs these campaigns.</p>"""),

            ("Facebook and Instagram: the Housing special ad category", f"""<p>Meta requires ads for housing opportunities, including listings for the rental of a home or apartment, to run under the Housing special ad category. Assisted and independent living apartments are rentals with services attached, and that’s how {SRC['mannix']}. We’d declare Housing on any ad promoting your apartments, availability or move-in specials, and ask Meta if you’re unsure about a particular ad.</p>
<p>Under Housing, per {SRC['loomer']}, age is locked to 18 to 65+, gender to all, location targeting has to include at least a 15-mile radius, ZIP code targeting is off, many detailed targeting options disappear and none can be excluded, and lookalike audiences aren’t available.</p>
<p>For senior living, losing age targeting is less painful than it sounds. You weren’t going to target 80-year-olds anyway; you want their 55-year-old kids, and the creative finds them. Ads that work in our experience:</p>
<ul>
<li>A two-minute walkthrough of a real one-bedroom apartment, shot on a phone, with the starting price on screen.</li>
<li>A short video of your memory care director answering “what does a normal day look like?”</li>
<li>Event invitations for a caregiver support group, a Medicare and long-term care Q&amp;A, or a lunch-and-tour. Events give the slow-cycle family a low-pressure reason to walk in.</li>
<li>Retargeting site visitors with a pricing guide download.</li>
</ul>
<p>If you use instant forms, ask a qualifying question or two (who is the care for, and how soon). Our post on {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'fixing bad Facebook lead quality')} covers the settings. See {L('/services/paid-social-advertising/', 'our paid social service')} if you’d rather hand it off.</p>"""),

            ("HIPAA, privacy and the details families share on your forms", f"""<p>Whether HIPAA applies to your community depends on what you do and how you bill. Under {SRC['hhsce']}, a health care provider is a covered entity only if it transmits health information electronically in connection with a transaction HHS has adopted a standard for, such as billing a health plan. Plenty of private-pay assisted living communities aren’t covered entities. Some are, especially those with licensed home health or that bill insurers. Ask your compliance lead which side you’re on.</p>
<p>Either way, families tell you sensitive things on inquiry forms: “Dad has Lewy body dementia and wanders at night.” Handle it as if HIPAA applies:</p>
<ul>
<li>Don’t pass form contents to ad platforms. Send a “lead” or “tour booked” event with no medical detail.</li>
<li>Keep diagnosis questions out of Facebook instant forms. Ask them on the phone.</li>
<li>Reply to online reviews without confirming that the reviewer’s parent lived with you or describing their care.</li>
<li>Get written permission before a resident appears in any photo or video, and keep it on file.</li>
</ul>"""),

            ("The tour is the conversion: speed, the visit and the long nurture", f"""<p>Every number worth tracking in senior living sits around the tour. Leads that tour move in at a far higher rate than leads that don’t, so the marketing job is to get the right families through the door fast, then stay with them until they’re ready.</p>
<p>Speed first. The daughter in Katy toured with whoever called her first. Answer web leads within minutes during business hours, and have a plan for nights and weekends: an answering service trained on your community, or a text that offers tour times. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} goes deeper on the follow-up systems.</p>
<!--fig:funnel-->
<p>Then the long tail. A family that tours and says “not yet” is your cheapest future move-in, and most communities drop them after two phone calls. A nurture plan that works:</p>
<!--fig:nurture-->
<p>Keep notes on what mattered to each family (the dog, the garden, the Catholic Mass schedule) and use them. A follow-up that says “we just started a gardening club, and I thought of your mom” beats a monthly newsletter every time. Our {L('/blog/email-marketing-basics/', 'email marketing basics')} post covers the plumbing.</p>"""),

            ("Reviews, Google Business Profile and the families who already chose you", f"""<p>Your Google Business Profile is often the first thing the adult child sees after the ads. Use the most specific category that applies (assisted living facility, retirement community, or senior citizen center if that’s really what you are), list accurate tour hours, and post photos of real apartments, the dining room at lunch, and staff people will meet.</p>
<p>Reviews come mostly from family members. Ask after a good care conference, after a move-in settles, or at a family event, and send the same link to everyone. Google doesn’t allow review gating or incentives, and our {L('/blog/complete-guide-google-reviews/', 'guide to Google reviews')} has request templates you can adapt.</p>
<p>Your current families are also your cheapest referral source, since a family referral costs close to nothing per move-in. Make it easy: a mention at family nights and a thank-you note when it happens.</p>"""),

            ("A first 90 days for a Houston senior living community", f"""<p>If we were starting fresh with a community at 85% occupancy, here’s the order we’d work in.</p>
<p><b>Days 1 to 30.</b> Audit lead handling: who answers, how fast, what happens at night. Put every lead source into one CRM with first-touch dates. Publish pricing and care-level pages. Fix the Google Business Profile. Pull your referral agency contracts and list each one’s fee and referral period.</p>
<p><b>Days 31 to 60.</b> Launch Google search campaigns by care level and town, with tour booking as the conversion. Start Meta under Housing with apartment walkthrough videos and an event. Build the nurture sequence for toured families.</p>
<p><b>Days 61 to 90.</b> Start reporting cost per tour and cost per move-in by channel, agencies included. Shift budget toward the cheapest move-ins. Start a family referral program.</p>
<p>After that it’s a monthly rhythm: occupancy, tours, move-ins and cost per move-in, by source. If you want a senior strategist to build that plan around your building and your census, <a href="/contact/">get in touch</a>. Home care agencies chasing the same families may also find our post on {L('/blog/how-do-home-care-agencies-get-clients/', 'how home care agencies get clients')} useful.</p>"""),
        ],
        "faq": [
            ("How do assisted living communities get more residents?",
             "Most move-ins come from families who toured, so the work is getting qualified families to a tour fast and staying in touch with the ones who aren’t ready. That means search ads for care level plus town, a website with real pricing and a tour calendar, quick lead response including nights and weekends, a written nurture plan, and a family referral program. Track cost per move-in by source."),
            ("How much do senior living referral agencies charge?",
             "It varies by contract. A Place for Mom’s website, quoted in a 2024 Senate Aging Committee letter, said that on move-in the community pays the company the first month’s rent and care. Texas SB 1383, enacted in 2025, requires agencies to disclose who pays the fee and limits referral periods to three years after the referral. Read your contracts carefully."),
            ("Do senior living ads fall under Meta’s housing special ad category?",
             "Ads that promote senior living apartments or availability are housing opportunities under Meta’s definition, and most senior living marketers run them under the Housing special ad category. That locks age to 18 to 65 plus, includes all genders, removes ZIP code targeting and lookalikes, and requires at least a 15-mile radius. Strong creative aimed at adult children works well despite the limits."),
            ("Can an assisted living facility in Texas advertise memory care?",
             "Texas Health and Safety Code section 247.029 sets up a separate classification and license for facilities that advertise, market or promote personal care for residents with Alzheimer’s disease or related disorders. If your ads or website say memory care or Alzheimer’s care, confirm your Alzheimer’s certification covers it, and have your administrator and attorney review the wording before campaigns go live."),
            ("What is a good cost per move-in for senior living?",
             "There’s no single benchmark, because it depends on your rates and length of stay. Multiply your average monthly rate by your average length of stay to get lifetime revenue per resident, which often lands in six figures. Compare each channel’s cost per move-in against that, and against what your referral agency contracts cost per placement, then move budget toward the cheapest move-ins."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "Senior living occupancy, third quarter 2026",
                "stats": [["90.4%", "average, 31 primary markets"], ["89.1%", "assisted living"], ["87.3%", "Houston average"], ["$6,200", "U.S. median monthly assisted living cost, 2025"]],
                "note": "Sources: NIC MAP via Senior Housing News; CareScout",
                "alt": "Stats on senior living occupancy in Houston and nationally for assisted living marketing in Houston and The Woodlands",
                "caption": f"Houston trails most big markets on occupancy, per {SRC['nic']} and {SRC['carescout']}.",
            },
            "referral": {
                "type": "compare",
                "title": "Agency leads vs. leads you own",
                "left": {"title": "Referral agency move-in", "items": ["Family gets several calls at once", "Fee due at move-in", "Family may be shown competitors first", "Referral period set by contract", "Duplicates need proof of first touch"]},
                "right": {"title": "Direct move-in", "items": ["Family called you first", "Cost is ad spend plus staff time", "Your story, your pricing page", "Lead history lives in your CRM", "Nurture continues for years"]},
                "alt": "Comparison of referral agency leads and direct leads for senior living marketing in Houston and The Woodlands",
                "caption": "Keep agencies as a channel while you build a direct pipeline that costs less per move-in.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From inquiry to move-in",
                "stages": [["Inquiries (calls, forms, agency)", "120"], ["Reached and qualified", "70"], ["Toured", "30"], ["Deposit or assessment", "9"], ["Moved in", "7"]],
                "note": "Illustrative example",
                "alt": "Illustrative funnel of senior living inquiries, tours and move-ins for an assisted living community in Houston",
                "caption": "Count every stage by source. Cost per move-in is the number that matters.",
            },
            "nurture": {
                "type": "steps",
                "title": "Nurturing families who aren’t ready",
                "sub": "For toured families who said “not yet”",
                "steps": [["Same day", "Thank-you text with the pricing sheet and a photo from their tour."], ["Week 1", "Call to answer the sibling’s questions. Offer a lunch visit."], ["Month 1", "Invite to an event: caregiver group, music night, holiday meal."], ["Months 2 to 6", "Personal notes tied to what mattered to them, plus availability updates."], ["Any crisis", "Fast path: assessment within 48 hours and respite stay options."]],
                "alt": "Steps for nurturing senior living prospects after a tour in Houston and The Woodlands",
                "caption": "Most move-ins from this list happen after a fall or hospital stay. Be the community they already know.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: plastic surgeons
    {
        "slug": "plastic-surgeon-marketing-houston",
        "title": "Plastic Surgeon Marketing in Houston: Getting Consults That Turn Into Surgeries",
        "seo_title": "Plastic Surgeon Marketing in Houston: Consults to Surgery",
        "desc": "Plastic surgeon marketing in Houston: Texas Medical Board ad rules, before-and-after consent, Instagram, Google and Meta health ad limits, HIPAA-safe reviews.",
        "category": "Strategy",
        "icons": ["Instagram", "Google Ads", "Google Analytics"],
        "art": "b4",
        "hero": "medical",
        "hero_alt": "Illustration of aesthetics for plastic surgeon and cosmetic surgery marketing in Houston and The Woodlands",
        "related": ["med-spa-marketing-the-woodlands-houston", "medical-practice-marketing-houston", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Thursday is consult day. Fourteen on the books. Three no-show. Two came in with screenshots from other surgeons’ Instagram accounts and a quote from a practice near the Galleria, and mostly wanted to know if you’d beat it. One wanted a procedure you don’t do. Four said they’d “think about it.” Your patient coordinator booked one surgery and has a deposit on another.</p>
<p>Your marketing report says Instagram followers are up and cost per lead is $38. Nobody can tell you which of those 14 consults came from which ad, or what a booked surgery actually cost you.</p>
<p>Plastic surgeon marketing in Houston works when it brings in fewer, better consults: people who already trust your work, know roughly what it costs, and are ready to pick a date. That takes a portfolio people can verify, compliant before-and-after content, procedure-specific search ads, and tracking that follows a patient from first click to surgery date without leaking their health information.</p>
<p>This guide is for board-certified plastic surgeons and cosmetic surgery practices from the Medical Center and River Oaks out to The Woodlands, Sugar Land, Katy and Clear Lake.</p>"""),

            ("Houston is a crowded aesthetic market", f"""<p>Houston has a deep bench of plastic surgeons, plus dermatologists, facial plastic surgeons, oculoplastic surgeons, OB-GYNs and med spas all chasing some of the same patients. Then there are the practices in Miami, Mexico and Colombia advertising to Houstonians directly on Instagram.</p>
<p>Nationally, demand is steady. ASPS members performed nearly 1.6 million cosmetic surgical procedures in 2024, up 1%, led by liposuction (349,728), breast augmentation (306,196), tummy tuck (171,064), breast lift (153,616) and eyelid surgery (120,755), per {SRC['asps']}. Minimally invasive procedures topped 28.5 million.</p>
<p>Price shopping is real, so it helps to know where the market sits. These are ASPS’s average surgeon fee ranges for 2024, which exclude things like anesthesia and facility fees:</p>
<!--fig:fees-->
<p>Those ranges are wide, and Houston pricing spreads across them depending on neighborhood, surgeon reputation and what’s bundled. We’d use them to set expectations on your site (more on pricing below), never as a quote.</p>
<p>In a market this crowded, the practices that win usually own two or three signature procedures in their marketing instead of listing 40 services. “The tummy tuck and mommy makeover surgeon in The Woodlands” is a position people remember, and it’s far easier to rank for.</p>"""),

            ("Board certification claims and Texas Medical Board advertising rules", f"""<p>Credentials are the first filter for a lot of patients, and Texas regulates how you claim them.</p>
<p>Under TMB Rule 164.4, as explained on {SRC['tmbcert']}, a physician can advertise as “board certified” when the certifying board is a member board of the American Board of Medical Specialties, a member board of the American Osteopathic Association Bureau of Osteopathic Specialists, or the American Board of Oral and Maxillofacial Surgery. There’s also a path for boards the TMB has found substantially equivalent, and a grandfather clause for certifications granted before September 1, 2010 by boards approved before then. The American Board of Plastic Surgery is an ABMS member board, and patients can check a surgeon’s status with {SRC['abps']}.</p>
<p>{SRC['tmb1643']} adds a list of things that make an ad misleading. The ones we see trip up aesthetic practices:</p>
<ul>
<li>Using “board eligible,” “board qualified” or similar wording to suggest board certification.</li>
<li>Testimonials without a disclaimer about the person’s credentials, or without disclosing that they were paid.</li>
<li>Failing to identify models or actors as models, instead of actual patients. Stock photos of perfect abs on a liposuction page are a problem.</li>
<li>Untruthful or deceptive claims about costs and fees, and claims of “free” services when a third party gets billed.</li>
<li>Claiming a unique or exclusive skill without substantiation. “Houston’s only surgeon who…” needs proof.</li>
<li>Failing to disclose that an article or infomercial is a paid presentation.</li>
</ul>
<p>{SRC['tma']} also notes the tension between the Occupations Code and TMB rules on testimonials and calls their use a substantial legal risk. Before a campaign goes live, we’d have the surgeon or practice counsel review credential language, testimonial use and every “best” claim. If your practice includes non-plastic-surgeon cosmetic surgeons, spell out each doctor’s actual board, and don’t let an ad imply everyone holds the same one.</p>"""),

            ("Before-and-after photos: consent, honesty and the rules", f"""<p>Before-and-after galleries sell surgery. They’re also where practices take the most risk.</p>
<p>Patient photos taken in your practice are protected health information, and full-face photos are an identifier on their own. Under {SRC['hhsmkt']}, with limited exceptions HIPAA requires a patient’s written authorization before PHI is used for marketing. A general photo consent signed at intake for the medical record isn’t the same thing. You want a separate, specific marketing authorization that says where the photos will appear (website, Instagram, paid ads), whether the face will show, and how the patient can revoke it.</p>
<!--fig:photos-->
<p>Honesty rules apply too. Don’t retouch results. Keep lighting, angle and posture the same before and after. Label how long after surgery the after photo was taken. And show typical results, not your single best case, because results that don’t reflect what comparable patients get are the classic way testimonials and galleries become misleading.</p>
<p>A practical note: an organized gallery by procedure, body type and age range does more selling than a carousel of 200 random photos. Patients look for someone who looks like them.</p>"""),

            ("Instagram: the portfolio patients actually check", f"""<p>For aesthetic surgery, Instagram is the portfolio, the reference check and often the first DM. Many patients find a surgeon on Google and then go straight to Instagram to see if the work is any good.</p>
<p>What works on organic Instagram for a Houston practice, in our experience:</p>
<ul>
<li><b>Consented before-and-afters</b>, posted with the procedure, timeline and a short caption from the surgeon about the goal.</li>
<li>The surgeon talking to camera about one question at a time: recovery after a tummy tuck, implant sizing, what a consult covers. Patients book with someone they feel they’ve already met.</li>
<li><b>Patient coordinator content.</b> Who they’ll talk to, how financing works, what to bring.</li>
<li>Story highlights by procedure so a new visitor can find “BBL,” “Breast,” “Face” and “Pricing” in two taps.</li>
</ul>
<p>Treat DMs as a lead channel. Someone needs to answer within the hour during business hours, move the conversation to a phone call or booking link, and never discuss a specific patient’s care in a public comment. Our {L('/blog/med-spa-marketing-the-woodlands-houston/', 'med spa marketing guide')} covers content for the nonsurgical side of the same audience.</p>"""),

            ("Meta ads under the health and wellness rules", f"""<p>Paid Meta ads for cosmetic surgery face three layers of rules.</p>
<p>First, the ad content. Meta’s policies, summarized by {SRC['outerbox']}, require cosmetic procedure ads to exclude people under 18, bar ads that generate negative self-perception to promote a procedure, and forbid copy that asserts or implies knowledge of someone’s personal attributes, including medical conditions. “Tired of your muffin top?” gets rejected. “Tummy tuck consults in The Woodlands, financing available” doesn’t.</p>
<p>Second, the tracking. Meta has rolled out restrictions on data from health and wellness advertisers. {SRC['sel']} describes tiers ranging from limits on custom parameters and URL data, to blocking optimization for mid- and lower-funnel standard events, to fully restricting events in some cases. Practices that relied on pixel-based “lead” or “purchase” optimization saw delivery change. Lead ads that collect information on Meta itself are largely unaffected.</p>
<p>Third, HIPAA. Even where Meta allows an event, {SRC['hhstrack']} says pixels on pages where people book appointments or enter health information can capture PHI. Don’t put a Meta pixel on your consult request form without a compliance review.</p>
<p>The workable setup for most practices: Meta lead ads with two or three qualifying questions (procedure, timeline, whether they’ve had a consult elsewhere), a CRM that receives the lead directly, and offline conversion uploads that send back “consult booked” or “surgery booked” without any health detail. {L('/services/paid-social-advertising/', 'Our paid social team')} sets these up.</p>"""),

            ("Google Ads by procedure, and the negatives that save you", f"""<p>Search intent in aesthetics is unusually specific. Someone searching “breast augmentation cost Houston” or “mommy makeover surgeon The Woodlands” has done some homework. Build campaigns by procedure, each with its own landing page that shows your gallery, a price range and a consult booking button.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Procedure</th><th>Example keywords</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Breast augmentation</td><td>breast augmentation Houston, breast implants cost Houston, breast augmentation surgeon near me</td><td>Price-shopped. Show a range and financing.</td></tr>
<tr><td>Tummy tuck and mommy makeover</td><td>tummy tuck The Woodlands, mommy makeover Houston cost</td><td>High ticket. Calls and consult bookings matter more than forms.</td></tr>
<tr><td>Liposuction</td><td>liposuction Houston, lipo surgeon Katy</td><td>Competes with nonsurgical body contouring. Be clear it’s surgery.</td></tr>
<tr><td>Facial surgery</td><td>facelift surgeon Houston, eyelid surgery Sugar Land, rhinoplasty Houston</td><td>Older, less price-sensitive searchers. Credentials and galleries carry it.</td></tr>
<tr><td>Brand</td><td>your name, your practice name</td><td>Cheap. Stops competitors and directories from sitting on your name.</td></tr>
</tbody></table></div>
<p>Negatives to start with: gone wrong, botched, death, lawsuit, malpractice, Mexico, Tijuana, Colombia, Dominican Republic (unless you want revision cases), jobs, residency, fellowship, salary, school, “free,” “cheap,” insurance coverage terms for cosmetic procedures you don’t bill, and DIY or exercise searches like “how to lose belly fat.”</p>
<p>A policy change worth knowing: in September 2025 Google announced it would remove mature cosmetic procedures, including female breast augmentation and buttock implants, from its sexual content policy, so those ads no longer face the old location and SafeSearch restrictions, per {SRC['ppcl']}. Images still have to follow Google’s nudity and sexually suggestive content rules, so keep before-and-after photos off image and display ads unless they’re clearly within policy. Our {L('/services/search-marketing/', 'Google Ads team')} manages this for practices that want it handled.</p>"""),

            ("Consult fees, pricing pages and financing", f"""<p>Whether to charge for consults is a real debate. A consult fee, often credited toward surgery if the patient books, cuts no-shows and filters out pure price shoppers. A free consult books more appointments and fills the calendar with lower-intent visits. We’ve seen both work. The deciding factor is usually how much surgeon time each consult takes.</p>
<p>Whatever you choose, say it plainly on the site and in the ad. TMB Rule 164.3 treats deceptive claims about costs and fees as misleading, so don’t advertise a “free consultation” if it’s only free when someone else is billed or if the fine print says otherwise.</p>
<p>On pricing, publish “starting at” or typical ranges for your main procedures and say what’s included: surgeon fee, anesthesia, facility, garments, follow-up visits. A patient comparing your all-in range with another practice’s surgeon-only number will think you’re more expensive unless you explain the difference.</p>
<p>Financing deserves its own page. Patient financing companies let many patients turn a $12,000 surgery into a monthly payment, and the page should explain the options, link to the application, and say that approval doesn’t commit anyone to surgery.</p>"""),

            ("Patient reviews and HIPAA: how to reply without a fine", f"""<p>Reviews carry enormous weight in elective surgery. They’re also the place practices most often expose patient information by accident.</p>
<p>A Texas example: Elite Dental Associates in Dallas {SRC['elite']} with the HHS Office for Civil Rights after replies to Yelp reviews disclosed patients’ last names, treatment details and insurance and cost information. A plastic surgery practice replying “we’re sorry you’re unhappy with your breast revision, but as we discussed at your two-week post-op…” is making the same mistake.</p>
<!--fig:replies-->
<p>The FTC also regulates how you collect reviews. {SRC['ftcrule']}, effective October 21, 2024, bans fake reviews, buying reviews conditioned on a positive sentiment, undisclosed insider reviews and most review suppression, with civil penalties of up to $51,744 per violation. Our post on {L('/blog/fake-reviews-rule-local-businesses/', 'the FTC fake reviews rule')} explains it in plain English, and the {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has request scripts.</p>
<p>A request that works: a text from the patient coordinator at the three-month visit, when the patient is happy with how things are settling. “We loved having you as a patient. If you’re comfortable sharing your experience, here’s the link. No pressure at all.” Send it to every patient, not only the happy ones.</p>"""),

            ("Measuring cost per surgery booked", f"""<p>Cost per lead is a vanity number in aesthetics. A $25 lead that never books a consult is worthless, and a $300 lead that turns into a $14,000 mommy makeover is a bargain. The number to manage is cost per surgery booked, by channel.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Stage</th><th>Illustrative month</th><th>Where it’s tracked</th></tr></thead>
<tbody>
<tr><td>Leads (calls, forms, DMs, lead ads)</td><td>220</td><td>Call tracking, CRM</td></tr>
<tr><td>Consults booked</td><td>70</td><td>Scheduling system, CRM</td></tr>
<tr><td>Consults attended</td><td>56</td><td>Practice management system</td></tr>
<tr><td>Surgeries booked (deposit paid)</td><td>16</td><td>CRM, uploaded to ad platforms</td></tr>
<tr><td>Ad spend</td><td>$24,000</td><td>Google, Meta</td></tr>
<tr><td>Cost per surgery booked</td><td>$1,500</td><td>Spend divided by surgeries</td></tr>
</tbody></table></div>
<!--fig:measure-->
<p>To get there you need tracked phone numbers per channel (see our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')}), a CRM that stores lead source for every patient, and a monthly upload of booked consults and surgeries back to Google and Meta as offline conversions using only identifiers and event names. Keep diagnoses and procedure details out of what you send. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking post')} covers the conversion setup, and {L('/blog/medical-practice-marketing-houston/', 'our medical practice marketing guide')} has more on HIPAA-safe analytics.</p>"""),

            ("A first 90 days for a Houston plastic surgery practice", f"""<p><b>Month one.</b> Review every credential claim, testimonial and gallery photo against TMB rules and your consent forms. Pick two or three signature procedures. Build or rebuild those procedure pages with price ranges, financing and a booking button. Audit your tracking for pixels on booking and intake pages.</p>
<p><b>Month two.</b> Launch procedure-specific Google search campaigns with a hard negative list. Start Meta lead ads with qualifying questions. Set a DM response standard for Instagram. Start the three-month review request.</p>
<p><b>Month three.</b> Report cost per consult attended and cost per surgery booked by channel. Cut what doesn’t book surgeries, even if it produces cheap leads. Feed booked surgeries back to the platforms.</p>
<p>If you want a senior strategist to build that around your procedures and your surgery calendar, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do plastic surgeons get more patients?",
             "Pick a few signature procedures and build the marketing around them: a strong gallery with proper marketing consent, procedure pages with price ranges and financing, procedure-specific Google search ads, Instagram content featuring the surgeon, and fast replies to calls and DMs. Then track every lead through consult to surgery booked, so budget goes to the channels that produce surgeries rather than cheap leads."),
            ("Can a plastic surgeon advertise as board certified in Texas?",
             "Under Texas Medical Board Rule 164.4, a physician can advertise board certification from an ABMS member board, an AOA Bureau of Osteopathic Specialists member board, the American Board of Oral and Maxillofacial Surgery, or a board the TMB finds substantially equivalent, with a grandfather clause for some older certifications. The American Board of Plastic Surgery is an ABMS member. Board eligible wording is prohibited."),
            ("Do I need patient consent to post before and after photos?",
             "Yes. Patient photos are protected health information, and HIPAA generally requires written authorization before PHI is used for marketing. Use a separate marketing authorization that names where the photos will appear, whether the face will show and how to revoke consent. Don’t retouch results, keep lighting and angles consistent, and show typical outcomes rather than only your best case."),
            ("How should a plastic surgeon respond to a negative review?",
             "Reply without confirming the person was a patient or mentioning any treatment details. Thank them, say you take feedback seriously, and invite them to call the practice manager directly. A Dallas dental practice paid HHS $10,000 after review replies disclosed patient names, treatment and cost details. Never offer incentives tied to positive reviews, which the FTC’s 2024 reviews rule prohibits."),
            ("Can cosmetic surgery practices run Facebook and Instagram ads?",
             "Yes, with limits. Meta requires cosmetic procedure ads to exclude people under 18 and prohibits ads that create negative self-perception or imply knowledge of someone’s medical conditions. Meta also restricts some conversion tracking for health and wellness advertisers. Lead ads with qualifying questions, plus offline conversion uploads of booked consults that contain no health details, usually work best."),
        ],
        "figures": {
            "fees": {
                "type": "bars",
                "title": "Average surgeon fee ranges, 2024",
                "sub": "ASPS member survey, surgeon fee only (bar shows top of range)",
                "items": [["Facelift", 19000, "$12,000-$19,000"], ["Tummy tuck", 13500, "$8,000-$13,500"], ["Rhinoplasty", 12500, "$7,500-$12,500"], ["Breast lift", 11000, "$6,500-$11,000"], ["Breast augmentation", 8000, "$4,575-$8,000"], ["Liposuction", 7500, "$4,300-$7,500"]],
                "highlight": [1],
                "note": "Source: American Society of Plastic Surgeons, 2024. Excludes anesthesia, facility and other costs.",
                "alt": "Bar chart of 2024 average plastic surgeon fee ranges by procedure for plastic surgeon marketing in Houston",
                "caption": f"From {SRC['aspsfee']}. Houston pricing varies by practice and what’s bundled.",
            },
            "photos": {
                "type": "checklist",
                "title": "Before-and-after photo checklist",
                "sub": "Run every gallery image through this",
                "items": ["Separate written marketing authorization on file", "Consent names website, social and paid ads", "Face shown only if consent says so", "No retouching of results", "Same lighting, angle and pose", "Time since surgery labeled", "Typical results, not just best cases", "Models and stock images labeled as models"],
                "alt": "Checklist for compliant before and after photos for plastic surgery marketing in Houston and The Woodlands",
                "caption": "Ask your attorney to review the authorization form itself.",
            },
            "replies": {
                "type": "compare",
                "title": "Replying to a bad review",
                "left": {"title": "Risky reply", "items": ["“As we discussed at your post-op…”", "Names the procedure or revision", "Mentions cost, balance or insurance", "Argues with the patient’s account", "Confirms they were a patient"]},
                "right": {"title": "Safer reply", "items": ["“We take every concern seriously.”", "No procedure or visit details", "No money details", "Invites a direct call to the practice manager", "Same tone for every reviewer"]},
                "alt": "Comparison of risky and HIPAA-safer review replies for plastic surgeons and cosmetic surgery practices in Houston",
                "caption": "Future patients read your replies. Keep them calm and generic.",
            },
            "measure": {
                "type": "funnel",
                "title": "From lead to surgery booked",
                "stages": [["Leads", "220"], ["Consults booked", "70"], ["Consults attended", "56"], ["Surgeries booked", "16"]],
                "note": "Illustrative example",
                "alt": "Illustrative funnel from leads to surgeries booked for a plastic surgery practice in Houston",
                "caption": "Judge channels on surgeries booked. Cheap leads that don’t attend consults cost the most.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: urgent care
    {
        "slug": "urgent-care-clinic-marketing-houston",
        "title": "Urgent Care Clinic Marketing in Houston: More Visits Per Location",
        "seo_title": "Urgent Care Clinic Marketing in Houston: More Visits",
        "desc": "Urgent care marketing for Houston clinics: Google Business Profile hours, online check-in, near-me Google Ads, freestanding ER confusion, HIPAA and pixels.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google"],
        "art": "b3",
        "hero": "clock",
        "hero_alt": "Illustration of a clock for urgent care clinic marketing and wait times in Houston and The Woodlands",
        "related": ["medical-practice-marketing-houston", "multi-location-local-seo-houston-franchises", "rank-in-google-map-pack-houston"],
        "sections": [
            (None, f"""<p>Monday, 8:05 a.m., second week of January. Your Cypress clinic’s online check-in queue is already full, with a two-hour wait and a lobby of coughing kids. Your Tomball clinic, 15 minutes away, has one patient. Google is showing the Tomball listing as “Closes 5 p.m.” because someone never updated it after you extended hours in the fall. A mom in Spring searches “urgent care near me,” sees a freestanding ER with a shorter wait, and goes there. She’ll find out about the facility fee in March.</p>
<p>Urgent care marketing in Houston is mostly operations wearing a marketing hat. To get more patients you need accurate Google listings for every location, a check-in system people can see and trust, and ads that run only when a location can take patients. Then you have to be clearer than anyone else about what you are, what you take and what it costs.</p>
<p>This guide is for independent urgent care operators with one to a dozen locations across Greater Houston: The Woodlands, Spring, Katy, Cypress, Pearland, Sugar Land, Humble, Kingwood and the rest.</p>"""),

            ("The Houston urgent care market: independents, hospital systems and freestanding ERs", f"""<p>The country added 611 urgent care centers in 2025 and ended the year at 15,309, a net gain of 277 after closures and consolidation. Texas led every state with 66 new centers, per {SRC['uca']}.</p>
<!--fig:stats-->
<p>In Houston you’re competing with three groups: other independents and franchises, hospital-system urgent cares with big brands and in-network contracts, and freestanding emergency rooms, which look a lot like urgent cares from the street.</p>
<p>Hospital systems win on brand, network and referrals into their specialists. You can win on convenience: shorter waits, accurate hours, easy online check-in, clear self-pay prices, and a location page that tells a parent exactly what you treat. Those are things a big system often does worse, because its urgent cares are a small part of a large website.</p>"""),

            ("Freestanding ER confusion, and how to use it honestly", f"""<p>Texas was the first state to license independent freestanding emergency rooms, and just over 200 had opened by 2019, some looking like urgent care clinics while charging ER prices, according to {SRC['tt']}. The same article cited a 2018 AARP Texas survey finding 77% of freestanding ERs said online that they accepted insurance while being out of network with all major plans.</p>
<p>The Legislature responded. {SRC['hb2041']}, effective September 1, 2019, requires freestanding emergency facilities to post a notice that the facility “charges rates comparable to a hospital emergency room and may charge a facility fee,” and to disclose network status at the entrance, in treatment rooms, at payment locations and on the website (on the home page or a prominent “Insurance Information” page). It bars them from saying they “take” or “accept” an insurer unless they’re in network, and from using an out-of-network insurer’s name or logo in marketing. A companion bill, HB 1941, let the attorney general go after “unconscionable” ER charges, defined in the article as more than 200% above the average hospital charge for similar treatment.</p>
<p>For an urgent care, the lesson is that patients in Houston are already confused, and many have been burned by a surprise bill. Clarity is a selling point:</p>
<!--fig:fser-->
<p>Put “We are an urgent care clinic, not an emergency room” on every location page, with a short list of what you treat and a separate list of symptoms that mean “call 911 or go to an ER.” Show self-pay prices for a basic visit. List the insurance plans you’re actually in network with, and update that list when contracts change. Never imply ER capability you don’t have. The goal is a parent who trusts you to tell them when they need the ER, and who comes back for everything else.</p>"""),

            ("Google Business Profile for every location, with hours that are actually right", f"""<p>Most urgent care visits start in Google Maps. Your profiles are the most important marketing you own, and one wrong hour can send a whole evening of patients elsewhere.</p>
<p>{SRC['gbp']} say each location gets one profile, no more, and that you can set special hours for holidays and events. Doctors and other public-facing practitioners can have their own profiles, separate from the location’s. For a multi-location group, the practical checklist:</p>
<!--fig:gbp-->
<p>The hours problem deserves its own paragraph. Urgent cares often stop checking in patients before they close. If your doors close at 8 p.m. but you stop taking walk-ins at 7:30, say that on the location page and in the profile description, and make sure the online check-in shuts off at the same time. A patient who drives from Atascocita to a closed door leaves the kind of review you’ll be answering for a year.</p>
<p>Set holiday hours weeks ahead for Thanksgiving, Christmas, New Year’s, Memorial Day, July 4th and Labor Day, and update for hurricane closures the same hour you decide. Our {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO guide')} and {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} go deeper on ranking each location.</p>"""),

            ("Online check-in and wait times", f"""<p>Online check-in has become table stakes for urgent care. Patients want to wait at home, not in a lobby with flu season in full swing. A visible wait time or next available slot on your site is one of the strongest conversion tools you have.</p>
<p>What we’d get right:</p>
<ul>
<li>Put the check-in link in each Google Business Profile as the appointment link, pointing to that specific location.</li>
<li>Show the current wait or the next available time on each location page, and on the locations list so people can pick the shortest one.</li>
<li>Make the check-in flow short. Name, date of birth, phone, reason for visit. Insurance details can wait until arrival.</li>
<li>Send a text when it’s time to head over, and another if the wait changes.</li>
<li>Spread demand. When Cypress is backed up and Tomball is empty, the site and the front desk should say so. “Our Tomball clinic has a 15-minute wait right now” fills empty rooms for free.</li>
</ul>
<p>One caution, which we’ll come back to: the check-in flow is where patients type in health information, so it’s the worst possible place for an advertising pixel.</p>"""),

            ("Google Ads for “urgent care near me”", f"""<p>The search terms are short and urgent: “urgent care near me,” “urgent care open now,” “walk in clinic Katy,” “urgent care Pearland,” “strep test near me,” “stitches near me,” “x-ray urgent care.” Most of the volume is near-me and open-now searches on phones, so ads need to be tightly tied to location and hours.</p>
<p>How we’d set it up for a group with several clinics:</p>
<ul>
<li><b>One campaign per location</b> with a radius drawn around realistic drive times (often 5 to 8 miles in Houston traffic), and location assets so each ad shows the right address.</li>
<li><b>Ad schedules that match check-in hours</b>, ending 30 minutes before the last patient is accepted. No ads at 9 p.m. for a clinic that closed at 8.</li>
<li>Service ad groups for the things people search by name: x-rays, stitches, strep and flu tests, COVID tests, sports physicals, DOT physicals, drug screens, IV fluids if you offer them.</li>
<li><b>Call assets with call reporting</b>, since many urgent care patients call to ask about wait times or insurance first.</li>
<li>A pause rule for days when a location is at capacity or short-staffed. Paying for clicks to a two-hour wait does nothing but generate bad reviews.</li>
</ul>
<p>Negatives to start with: jobs, hiring, nurse, medical assistant, salary, “urgent care near me hiring,” vet, animal, pet, emergency vet, dental (unless you do dental), eye doctor, “free clinic,” and the names of hospital systems if their brand searches keep showing up. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} will help you size a budget, and our {L('/services/search-marketing/', 'search marketing team')} can run the campaigns.</p>"""),

            ("Seasonal demand: flu season, back-to-school and sports physicals", f"""<p>Urgent care demand follows a calendar you can plan around. Per {SRC['cdc']}, flu season usually happens in fall and winter, and most of the time activity peaks between December and February. February was the most common peak month from the 1982-83 season through 2023-24.</p>
<!--fig:season-->
<p>The other big wave is late summer. {SRC['uil']} requires a physical exam signed by a physician (or a PA, APRN or chiropractor) upon entering the first and third years of high school, plus a medical history form every year before any practice. Fall sports start in late summer, so July and early August is when parents search “sports physical near me.”</p>
<p>A rough marketing calendar we’d use for a Houston group:</p>
<ul>
<li><b>June to August.</b> Sports and school physicals: a dedicated page with price, what form to bring (the UIL form or the district’s), and walk-in hours. Search ads on “sports physical [town]” and Meta posts to local parents.</li>
<li><b>September to October.</b> Flu shots and the start of respiratory season. Push online check-in.</li>
<li><b>November to March.</b> Flu, strep and RSV season. Increase search budgets, keep wait times visible, and use load-balancing messages between locations.</li>
<li><b>Hurricane season, June through November.</b> After storms, people show up with cuts, sprains and heat-related problems from cleanup. Keep a storm-hours plan for your profiles and site.</li>
</ul>
<p>Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing guide')} and {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing post')} have more on timing.</p>"""),

            ("Occupational medicine and employer accounts", f"""<p>Walk-in volume rises and falls with flu season. Employer work is steadier and books during your slow hours. Houston has a lot of it, between the refineries and plants along the Ship Channel, the Energy Corridor, construction crews across the suburbs, and trucking and logistics companies along every highway.</p>
<p>The common services: pre-employment physicals, drug and alcohol screens, DOT physicals, workers’ comp injury care, and return-to-work evaluations. DOT physicals have a specific rule. Since May 21, 2014, new commercial driver physicals have to be performed by a medical examiner listed on the National Registry of Certified Medical Examiners, per {SRC['fmcsa']}. If your providers are on the registry, say so on the page and in your Google profile’s services.</p>
<p>Employer marketing looks more like B2B sales than consumer advertising:</p>
<ol>
<li>Build an employer services page: services, turnaround on results, billing terms, and a direct contact.</li>
<li>Make a list of 50 employers within ten minutes of each clinic. Safety managers and HR are your buyers.</li>
<li>Offer a dedicated check-in path for employer-sent patients so they don’t sit in the flu lobby.</li>
<li>Report results fast. Employers stay with the clinic that gets drug screen results back quickly and never loses paperwork.</li>
</ol>
<p>Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing for Houston energy and industrial')} post covers how to reach those buyers.</p>"""),

            ("Insurance pages and price transparency", f"""<p>“Do you take my insurance?” is the most common question urgent cares get. Answer it on the site so the front desk doesn’t have to answer it 80 times a day.</p>
<ul>
<li>Build an insurance page listing the plans you’re in network with, by name, including Medicare, Medicaid managed care plans and marketplace plans if you take them. Date it and keep it current.</li>
<li>Add a sentence on what to expect: copays, deductibles, and that coverage depends on the patient’s specific plan.</li>
<li>Publish self-pay prices for a basic visit and common add-ons (strep test, x-ray, stitches, physicals). Houston has a large uninsured and high-deductible population, and a visible price wins those patients.</li>
<li>Add a Spanish version of your insurance and pricing pages. Our post on {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Spanish-language marketing in Houston')} explains why it matters here.</li>
</ul>
<p>There’s also a federal rule to follow. Under the No Surprises Act, providers have to tell uninsured and self-pay patients about their right to a good faith estimate and give one in writing when it’s requested or when a service is scheduled at least three business days ahead. The notice has to be posted on your website and in the office, and patients billed at least $400 more than the estimate can use a dispute process, per {SRC['cmsgfe']}. Walk-in visits rarely trigger the scheduling clause, but any discussion of cost counts as a request, so the website notice and a front-desk process belong in place.</p>"""),

            ("HIPAA and tracking pixels on check-in pages", f"""<p>This is where urgent care marketing gets into legal trouble most often. {SRC['hhstrack']}, first issued in November 2022, says tracking tools on pages where patients schedule appointments or enter health information can collect protected health information, and that vendors handling PHI generally need a business associate agreement. In June 2024, a federal court in the Northern District of Texas, in American Hospital Association v. Becerra, vacated the part of the guidance dealing with an IP address linked to a visit to a public health page. The rest, including the parts about scheduling and patient portals, still stands.</p>
<p>What that means in practice for an urgent care:</p>
<ul>
<li>No Meta pixel, TikTok pixel or similar ad tags on the online check-in flow, the patient portal, or any page where someone types a reason for visit.</li>
<li>Count conversions without health details. A “check-in completed” event with no reason-for-visit data, sent from a vendor that will sign a BAA, is the safer route.</li>
<li>Audit your tag manager. Many urgent care sites we look at have tags someone added years ago and forgot.</li>
<li>Ask your check-in vendor what tracking it supports and whether it signs BAAs before you connect it to ad platforms.</li>
</ul>
<p>Our {L('/blog/medical-practice-marketing-houston/', 'medical practice marketing guide')} covers HIPAA-safe analytics in more detail, and our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} covers call and form conversions.</p>"""),

            ("What to track, and a first 90 days", f"""<p>The metric that runs an urgent care is visits per location per day. Marketing should report against it, by location, along with cost per visit by channel, online check-in share, review rating and count by location, and the percentage of hours each location was at capacity.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Illustrative location</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td>Visits per day</td><td>42</td><td>The number everything else serves</td></tr>
<tr><td>Online check-ins</td><td>45% of visits</td><td>How much the website and Maps listing drive</td></tr>
<tr><td>Ad spend per month</td><td>$3,000</td><td>Per location, with ad schedules tied to hours</td></tr>
<tr><td>Visits attributed to ads</td><td>230 per month</td><td>From check-ins and calls tracked to ads</td></tr>
<tr><td>Cost per ad-driven visit</td><td>About $13</td><td>Compare with your average reimbursement per visit</td></tr>
</tbody></table></div>
<p><b>Days 1 to 30.</b> Audit every Google profile for hours, categories and the check-in link. Fix location pages with services, insurance, self-pay prices and the “not an ER” section. Remove ad pixels from check-in and portal pages.</p>
<p><b>Days 31 to 60.</b> Launch per-location search campaigns with schedules that match check-in hours. Add wait times to the site. Start review requests by text after every visit, as covered in our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')}.</p>
<p><b>Days 61 to 90.</b> Build the employer page and start outreach. Plan the next seasonal push. Start reporting visits and cost per visit by location every month.</p>
<p>If you want a senior strategist to build that plan around your locations and your busy season, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do urgent care clinics get more patients?",
             "Start with an accurate Google Business Profile for every location, with correct hours, holiday hours and an online check-in link. Show wait times on your site, list the insurance plans you’re in network with and publish self-pay prices. Run Google Ads per location only during check-in hours. Then add seasonal campaigns for flu season and sports physicals, plus employer services like drug screens and DOT physicals."),
            ("What is the difference between urgent care and a freestanding ER in Texas?",
             "Freestanding emergency rooms are licensed emergency facilities. Texas requires them to post that they charge rates comparable to a hospital emergency room and may charge a facility fee, and to disclose their network status. Urgent care clinics treat non-emergency illnesses and injuries, usually at much lower cost. Urgent cares should say clearly that they aren’t ERs and list symptoms that need emergency care."),
            ("Is it OK to put a Facebook pixel on an urgent care website?",
             "Not on pages where patients check in, schedule, log in or describe symptoms. HHS guidance says tracking tools on those pages can capture protected health information, and a 2024 court ruling only vacated the part about public pages. Keep ad pixels off check-in and portal pages, track conversions without health details, and use vendors that sign business associate agreements."),
            ("When is the busiest season for urgent care in Houston?",
             "Respiratory illness season, roughly November through March, is the biggest wave. The CDC says flu activity most often peaks between December and February, with February the most common peak month. Late July and August bring a second wave of sports physicals, since UIL requires a physical in the first and third years of high school plus a yearly medical history form."),
            ("Do urgent cares have to give price estimates?",
             "Under the No Surprises Act, providers must tell uninsured and self-pay patients about their right to a good faith estimate, post that notice on their website and in the office, and provide a written estimate on request or when a service is scheduled at least three business days ahead. Publishing self-pay prices for common visits also helps convert patients comparing options."),
        ],
        "figures": {
            "stats": {
                "type": "stats",
                "title": "Urgent care growth in 2025",
                "stats": [["15,309", "U.S. urgent care centers at end of 2025"], ["611", "new centers opened in 2025"], ["66", "new centers in Texas, most of any state"]],
                "note": "Source: Urgent Care Association",
                "alt": "Stats on urgent care center growth in Texas and the U.S. for urgent care clinic marketing in Houston",
                "caption": f"From {SRC['uca']}.",
            },
            "fser": {
                "type": "compare",
                "title": "What patients need to see from you",
                "left": {"title": "What confuses Houston patients", "items": ["ER-looking building, urgent care feel", "“We accept all insurance” banners", "Insurer logos with no network detail", "No prices anywhere", "Facility fee found on the bill"]},
                "right": {"title": "What a clear urgent care shows", "items": ["“Urgent care, not an emergency room”", "In-network plans listed by name", "Self-pay prices for common visits", "When to go to the ER instead", "Wait time and check-in link"]},
                "alt": "Comparison of confusing freestanding ER messaging and clear urgent care messaging for Houston urgent care marketing",
                "caption": f"Texas requires freestanding ERs to post fee and network notices under {SRC['hb2041']}. Use the same clarity as your selling point.",
            },
            "gbp": {
                "type": "checklist",
                "title": "Per-location Google profile checklist",
                "sub": "Check every location, every quarter",
                "items": ["One profile per location, no duplicates", "Primary category: urgent care center", "Regular hours match check-in cutoff", "Holiday and storm hours set ahead", "Check-in link points to that location", "Services list: x-ray, stitches, physicals, DOT", "Photos of entrance, lobby and parking", "Reviews answered without patient details"],
                "alt": "Checklist for Google Business Profiles for each urgent care clinic location in Houston and The Woodlands",
                "caption": f"Based on {SRC['gbp']} and the hours mistakes we see most.",
            },
            "season": {
                "type": "columns",
                "title": "When Houston urgent care demand shifts",
                "sub": "Relative visit demand by month for a typical clinic",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [95, 100, 80, 60, 55, 55, 70, 80, 60, 65, 75, 90],
                "highlight": [0, 1, 7, 11],
                "y_label": "Relative demand",
                "note": "Illustrative example",
                "alt": "Illustrative chart of seasonal urgent care visit demand by month in Houston, with flu season and back-to-school peaks",
                "caption": "Flu season and sports physicals drive the peaks. Use your own visit data to set budgets.",
            },
        },
    },
]
