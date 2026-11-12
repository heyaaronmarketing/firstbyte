"""Batch 12: optometrist and eye care practice marketing in Houston (independent ODs vs. retail optical and online eyewear).

Research: WordStream/LocaliQ 2026 Google Ads benchmarks (no optometry category; Physicians & Surgeons $4.76 CPC,
12.43% CVR, $40.04 CPL; Dentists $8.00; Health & Fitness $6.17; all-industry $5.42); Texas Occupations Code 351.403
(false advertising, "prescription required" notice, price-ad disclosures) and 351.155 (board may not restrict truthful
statements about accepted insurance or health plans, hours, languages, etc.) via texas.public.law; 22 TAC 279.9
(board-certified claims must name the certifying organization; contact lens price ads state the number of lenses) and
279.10 (name display) via Justia; Google Local Services Ads category list (Optometrist is a US category; no booking
leads for health care) and LSA screening requirements for optometrists (background checks, state practice and provider
licenses, NPI for select users); Google Business Profile help on booking links; Google Ads personalized advertising
policy and its Health sensitive-category page; Holland & Knight on AHA v. Becerra (N.D. Tex., June 20, 2024) and HIPAA
Journal on OCR withdrawing its appeal; Cardinal Digital Marketing on Meta’s 2025 health data restrictions; HHS OCR’s
New Vision Dental resolution ($23,000, review responses); BrightLocal Local Consumer Review Survey 2026; VSP’s consumer
page on where VSP is accepted (Eyeconic) and EyeMed’s online in-network providers (EssilorLuxottica footnote); Myopia
Profile on the FDA’s Sept. 25, 2025 De Novo authorization of Essilor Stellest (ages 6-12) and MiSight 1 day (2019,
ages 8-12); OMIC on the FTC’s updated Eyeglass Rule (effective Sept. 24, 2024); Texas DSHS vision screening schedule;
Community Impact on an online-first eyewear brand’s 18th Texas store, with exams, at LaCenterra in Katy (Jan. 2023).
Left out (could not verify): VSP/EyeMed member counts, a Houston-specific optometry CPC, dry eye prevalence figures,
Texas optometrist headcounts.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "wordstream": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream and LocaliQ’s 2026 Google Ads benchmarks"),
    "occ403": A("https://texas.public.law/statutes/tex._occ._code_section_351.403", "Texas Occupations Code §351.403"),
    "occ155": A("https://texas.public.law/statutes/tex._occ._code_section_351.155", "§351.155 of the Optometry Act"),
    "tac279": A("https://regulations.justia.com/states/texas/title-22/part-14/chapter-279/section-279-9", "Texas Optometry Board Rule 279.9"),
    "tob": A("https://tob.texas.gov/board-rules", "Texas Optometry Board’s rules page"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "lsareq": A("https://support.google.com/localservices/answer/12174778?hl=en", "Google’s screening requirements"),
    "gbplinks": A("https://support.google.com/business/answer/6218037", "Google’s help page on booking links"),
    "ghealth": A("https://support.google.com/adspolicy/answer/16701855", "Google treats health as a sensitive interest category"),
    "gpers": A("https://support.google.com/adspolicy/answer/143465", "personalized advertising policy"),
    "aha": A("https://hklaw.com/en/insights/publications/2024/06/american-hospital-assn-v-becerra-are-tracking-tools-ok-again", "Holland & Knight’s summary of AHA v. Becerra"),
    "appeal": A("https://www.hipaajournal.com/ocr-to-appeal-district-court-ruling-in-aha-tracking-technology-case/", "withdrew its appeal"),
    "meta": A("https://www.cardinaldigitalmarketing.com/healthcare-resources/blog/meta-announces-major-changes-healthcare-advertising/", "Meta started restricting the data health advertisers can send"),
    "newvision": A("https://www.hipaajournal.com/ocr-fines-california-dental-practice-for-phi-disclosures-on-yelp/", "paid $23,000 to settle with HHS"),
    "brightlocal": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "vsp": A("https://www.vspdirect.com/ena/vision-hub/where-is-vsp-insurance-accepted", "VSP’s own consumer guide"),
    "eyemed": A("https://www.eyemed.com/en-us/blog/benefits-101/setting-sights-on-the-online-eyewear-experience-32966", "EyeMed’s list of online in-network stores"),
    "stellest": A("https://www.myopiaprofile.com/articles/essilor-stellest-fda-market-authorization", "Myopia Profile"),
    "eyeglassrule": A("https://omic.com/ftc-updates-the-eyeglass-rule", "the FTC’s updated Eyeglass Rule"),
    "dshs": A("https://www.dshs.texas.gov/vhss-vision-hearing-and-spinal-screening/vhss-screening-schedule", "Texas DSHS screening schedule"),
    "ci": A("https://communityimpact.com/houston/katy/business/2023/01/13/warby-parker-eyewear-brand-opening-18th-texas-store-in-lacenterra-at-cinco-ranch", "Community Impact"),
}

L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    {
        "slug": "optometrist-marketing-houston",
        "title": "Optometrist Marketing in Houston: SEO, Google Ads & Online Booking for Eye Care Practices",
        "seo_title": "Optometrist Marketing in Houston: SEO, Ads & Booking",
        "desc": "How Houston optometrists book more eye exams: local SEO, vision plan pages, Google Ads costs, LSAs, Texas Optometry Board ad rules, HIPAA-safe tracking.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Search Console"],
        "art": "b3",
        "hero": "medical",
        "hero_alt": "Illustration of an eye care practice for optometrist marketing in Houston and The Woodlands",
        "related": ["medical-practice-marketing-houston", "dental-marketing-the-woodlands-houston", "rank-in-google-map-pack-houston"],
        "sections": [
            (None, f"""<p>There’s no optometry category in the big Google Ads benchmark studies, but the closest one, Physicians &amp; Surgeons, runs a median of <b>$4.76 per click</b> and <b>$40.04 per lead</b>, per {SRC['wordstream']}. That’s cheaper than dental. The hard part in Houston and The Woodlands is who you’re bidding against: retail optical chains, big-box vision centers, and online eyewear brands that now have storefronts with exam lanes.</p>
<p>A Tuesday in late August at an independent practice in Spring: four open exam slots tomorrow. A mom in Cypress types “eye doctor that takes VSP near me” because her kid failed the school vision screening. The first three results are a mall chain, a warehouse-store vision center and a directory site. Your practice is fourth on the map, and she never scrolls that far.</p>
<p>Winning that search means showing up for exam and insurance queries, making it obvious you take her plan, letting her book at 9:40 p.m., and giving her reasons to buy glasses from you instead of a website. This guide is for independent ODs with one to five offices.</p>"""),

            ("Rank for eye exam and eye doctor searches", f"""<p>The searches that fill exam chairs are local and specific, so you need a page for each service and each office, plus a Google Business Profile complete enough to win the map pack.</p>
<ul>
<li><b>One page per service:</b> comprehensive exams, contact lens fittings, pediatric exams, dry eye, myopia control, diabetic exams, red-eye and urgent visits.</li>
<li><b>One page per office</b> with address, hours, the doctors who see patients there, and the plans accepted at that location.</li>
<li><b>Doctor bio pages</b> with the licensed name, school and any certifications, named correctly (see the Texas rules below).</li>
<li><b>Answers to pre-booking questions:</b> how long an exam takes, whether dilation is included, what a contact lens fitting costs.</li>
</ul>
<p>The map-pack basics are the same as any local practice: “Optometrist” as the primary category, real photos, steady reviews, accurate hours. Our guide to {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Google map pack in Houston')} has the checklist, and {L('/services/web-design-seo-pr/', 'our web design and SEO team')} builds these pages.</p>"""),

            ("Build vision plan pages that answer “do you take my insurance?”", f"""<p>Lots of routine exam searches start with a vision plan, so a patient-friendly page for each plan you accept is often the best-converting page an independent practice can add.</p>
<p>Texas law is on your side. {SRC['occ155']} bars the Texas Optometry Board from restricting truthful statements about accepted insurance or health plans, office hours, languages spoken or installment payments.</p>
<ul>
<li><b>A page per in-network plan</b> (VSP, EyeMed and the rest) explaining what’s typically covered and what to bring.</li>
<li><b>Vision vs. medical insurance.</b> A short explainer on why a dry eye visit bills to the medical plan heads off billing-day surprises and bad reviews.</li>
<li><b>A plain “plans we don’t take” note.</b> It saves your front desk a dozen calls a week.</li>
</ul>
<p>The plans sell glasses too. {SRC['vsp']} points members to Eyeconic, its in-network online store, and {SRC['eyemed']} includes Glasses.com, ContactsDirect and LensCrafters.com, with a footnote that EyeMed and those stores share a parent, EssilorLuxottica. “We take VSP” gets a patient in the door. The exam, fitting and follow-up are what keep them.</p>"""),

            ("Market medical eye care, not just glasses", f"""<p>Medical eye care is the easiest way for an independent practice to stand apart from chains, because a website can’t do it.</p>
<ul>
<li><b>Dry eye.</b> A dedicated page and a symptom checklist, written the way patients describe it after a day in cold office air followed by Houston humidity.</li>
<li><b>Myopia control.</b> The FDA authorized Essilor Stellest spectacle lenses for kids 6 to 12 on Sept. 25, 2025, and MiSight 1 day contacts were approved in 2019 for kids 8 to 12, per {SRC['stellest']}. A page on options, costs and how progress is measured will get found by parents.</li>
<li><b>School screenings.</b> Texas requires vision screening at age 4, kindergarten, for new entrants and in grades 1, 3, 5 and 7, per the {SRC['dshs']}. Run a pediatric push from late July through September around Katy, Cy-Fair, Conroe and Humble ISDs (timing in our {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school guide')}).</li>
<li><b>Same-day visits.</b> “Pink eye doctor near me” is an urgent search. If you hold same-day slots, say so.</li>
</ul>
<p>One catch: {SRC['ghealth']}, and its {SRC['gpers']} bars advertiser-curated audiences like Customer Match and remarketing lists there. Assume dry eye campaigns fall under it and build them on keywords.</p>"""),

            ("Set up Google Business Profile and online booking", f"""<p>Patients book eye exams at night and on weekends, so a booking button that opens a real calendar is worth more than most ads.</p>
<ul>
<li><b>Add the link.</b> In Search choose “Booking” on your profile (in Maps, “Edit profile”), then “Add link,” paste the URL and save, per {SRC['gbplinks']}.</li>
<li><b>Show real slots.</b> A “request” form your staff returns tomorrow loses to a competitor that confirms instantly.</li>
<li><b>One profile per office</b>, with the right suite number.</li>
<li><b>Update hours the morning a storm or freeze closes you.</b> Nobody forgets driving to a dark office.</li>
</ul>
<p>And answer the phone. Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')} explains why the first practice to respond usually gets the appointment.</p>"""),

            ("Use Local Services Ads for optometrists", f"""<p>Google offers Local Services Ads for optometrists: “Optometrist” is on {SRC['lsa']}, so they’re worth testing for exam bookings.</p>
<ul>
<li><b>Verification takes paperwork.</b> {SRC['lsareq']} for optometrists include provider and practice background checks and state licenses, plus insurance and NPI checks for some accounts.</li>
<li><b>Leads are calls and messages.</b> Google says booking leads aren’t available for health care, so someone has to pick up.</li>
<li><b>You pay per lead</b>, not per click, and can dispute invalid ones.</li>
</ul>
<p>Run LSAs next to search ads for a quarter and compare cost per booked exam. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads comparison')} was written for home services, but the trade-offs carry over.</p>"""),

            ("Run Google Ads with tight controls", f"""<p>Keep Google Ads on exam, insurance and medical-visit keywords in the areas you serve; “glasses” and “contacts” searches mostly want a shopping cart.</p>
<!--fig:cpc-->
<div class="tbl"><table>
<thead><tr><th>Campaign</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Exams by area</td><td>eye exam The Woodlands, optometrist Katy</td><td>Location page with booking</td></tr>
<tr><td>Insurance</td><td>eye doctor that takes VSP, EyeMed optometrist near me</td><td>Plan page</td></tr>
<tr><td>Medical</td><td>dry eye treatment Houston, pink eye doctor</td><td>Condition page, phone first</td></tr>
<tr><td>Kids</td><td>pediatric eye exam Sugar Land, myopia control for kids</td><td>Pediatric or myopia page</td></tr>
<tr><td>Brand</td><td>practice and doctor names</td><td>Booking page</td></tr>
</tbody></table></div>
<p>Day-one negatives: free, cheap glasses, Walmart, Costco, “1-800,” Zenni, online, jobs, careers, salary, optometry school, technician, LASIK. Read the search terms report weekly for the first month.</p>
<p>Sample ad (illustrative): “Eye Exams in The Woodlands | VSP &amp; EyeMed Accepted | Book Online Tonight.” Treat the national median as a floor in Houston and check Keyword Planner; our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} explain how, and our {L('/services/search-marketing/', 'search marketing team')} can run the account.</p>"""),

            ("Follow Texas Optometry Board advertising rules", f"""<p>Texas optometry ads must follow the Texas Optometry Act and Texas Optometry Board rules, and price-ad disclosures are where practices slip most.</p>
<ul>
<li><b>Nothing false or misleading.</b> {SRC['occ403']} bans deceptive statements about ophthalmic services or materials in any medium.</li>
<li><b>Prescription notice.</b> Ads for prescription glasses or contacts must say a prescription is required to buy them.</li>
<li><b>Price disclosures.</b> A price ad must say whether the exam and follow-up are included, plus any time limit under 30 days, quantity or per-customer limits, and for contacts the number of lenses.</li>
<li><b>“Board certified” needs a name.</b> {SRC['tac279']} requires naming the certifying organization.</li>
</ul>
<!--fig:pricead-->
<p>Under {SRC['eyeglassrule']}, effective Sept. 24, 2024, prescribers who sell eyewear must get a signed confirmation that the patient received their prescription and keep it three years. Patients leave with it, so plan on earning the sale.</p>
<p>Check current wording on the {SRC['tob']}. This isn’t legal advice; have counsel review price promotions.</p>"""),

            ("Keep tracking pixels away from patient data", f"""<p>HIPAA still limits ad pixels on eye care websites, especially on patient portals and booking flows.</p>
<ul>
<li><b>What the court changed.</b> In June 2024 a federal court in Fort Worth vacated part of HHS’s tracking bulletin (IP addresses plus visits to public health-condition pages) and left the rest, per {SRC['aha']}. HHS later {SRC['appeal']}.</li>
<li><b>Keep Meta and TikTok pixels off the portal and scheduler.</b> Record bookings as conversions with no health details.</li>
<li><b>Meta has its own limits.</b> In early 2025 {SRC['meta']}; check your categorization in Events Manager.</li>
<li><b>Get a BAA</b> from any vendor that touches patient data.</li>
</ul>
<p>Our guide to {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking forms and calls in GA4')} shows the setup.</p>"""),

            ("Build reviews the right way", f"""<p>Patients weigh how recent your reviews are as much as the stars.</p>
<ul>
<li><b>The bar is high.</b> In {SRC['brightlocal']}, 31% only use businesses rated 4.5 stars or higher, 74% only care about reviews from the last three months, and 47% won’t use one with fewer than 20.</li>
<li><b>Ask at pickup,</b> when the patient can suddenly read the sign across the street, then text a direct link.</li>
<li><b>Never offer anything for a review.</b></li>
<li><b>Never confirm someone is a patient in a reply.</b> A California dental practice {SRC['newvision']} after its owner disclosed patient details answering Yelp reviews.</li>
</ul>
<p>Script (illustrative): “Thanks for coming in today, Maria. If our team took good care of you, a quick Google review helps other Pearland families find us: [link].” More in our {L('/blog/complete-guide-google-reviews/', 'guide to Google reviews')}.</p>"""),

            ("Sell more glasses in your own optical", f"""<p>Your optical can’t beat the internet on price, so sell fit, adjustments and repairs. The competition is local now too: an online-first brand opened its 18th Texas store, with exams, at LaCenterra in Katy in January 2023, per {SRC['ci']}.</p>
<ul>
<li><b>Show your frame brands online.</b> Patients search them by name.</li>
<li><b>Advertise the warranty and lifetime adjustments.</b></li>
<li><b>Track capture rate</b> (exams that end in an optical sale) by doctor and month. We don’t know of a reliable benchmark, so watch your own trend.</li>
<li><b>Send recall and contact lens reorder texts.</b> They’re the cheapest marketing you have.</li>
</ul>"""),

            ("What to budget for optometry marketing in Houston", f"""<div class="tbl"><table>
<thead><tr><th>Practice</th><th>Monthly ad spend (illustrative)</th><th>Where it goes</th></tr></thead>
<tbody>
<tr><td>One office</td><td>$1,500-$3,000</td><td>Exam, insurance and brand search; LSA test</td></tr>
<tr><td>One office pushing medical eye care</td><td>$3,000-$5,000</td><td>Plus dry eye, myopia and back-to-school</td></tr>
<tr><td>Two to five offices</td><td>$2,000-$4,000 per office</td><td>Per-location campaigns, shared brand</td></tr>
</tbody></table></div>
<p>These are planning ranges from our experience with local practices, not benchmarks. At the $4.76 median, $3,000 buys roughly 630 clicks before Houston competition pushes prices up. Our {L('/blog/medical-practice-marketing-houston/', 'medical practice marketing guide')} covers splitting budget across channels.</p>"""),

            ("Your first 90 days", f"""<p>Fix booking, plan pages and tracking before spending on ads, then add medical eye care once the basics book.</p>
<!--fig:plan-->"""),

            ("Mistakes we see in eye care marketing", f"""<ul>
<li><b>Bidding on “glasses” and “contacts.”</b></li>
<li><b>Price ads with no disclosures</b>, like “2 pairs $99” with nothing about the exam.</li>
<li><b>A Meta pixel on the booking page.</b></li>
<li><b>One location page</b> for offices in Tomball, Magnolia and Conroe.</li>
<li><b>Judging by clicks</b> instead of kept exams.</li>
</ul>"""),

            ("Measure what matters", f"""<p>Track booked exams, show rate, cost per kept exam by channel, new vs. returning patients, and optical capture rate. Clicks and calls are leading indicators; kept exams are the result.</p>
<p>If you’d like a senior strategist to build a custom plan for your offices and goals, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much should an optometrist spend on Google Ads in Houston?",
             "Many single-office practices can start with $1,500 to $3,000 a month in ad spend, focused on exam, insurance and medical eye care searches. The closest benchmark category, Physicians and Surgeons, has a median of $4.76 per click and $40.04 per lead nationally. Houston often runs higher, so measure cost per booked exam and adjust."),
            ("Are Local Services Ads worth it for optometrists?",
             "They’re worth testing. Optometrist is an eligible Local Services Ads category in the US, and you pay per lead instead of per click. Google says booking leads aren’t available for health care, so leads arrive as calls and messages. They only pay off if your front desk answers quickly and you compare them against regular search ads."),
            ("Do Texas optometrists have advertising rules?",
             "Yes. The Texas Optometry Act bans false or misleading ads, requires ads for prescription eyewear to say a prescription is required, and requires price ads to disclose whether the exam is included, time limits and, for contacts, the number of lenses. Board Rule 279.9 requires naming the organization behind any board certified claim."),
            ("Can an eye care practice use the Meta pixel on its website?",
             "Carefully, and not everywhere. Keep pixels off patient portals, scheduling flows and pages where patients enter health information, and get a business associate agreement from vendors that handle patient data. A 2024 court ruling narrowed HHS’s tracking guidance but left most of it in place, and Meta now limits data from health advertisers too."),
            ("How can an independent optometrist compete with online glasses and retail chains?",
             "Compete on what a website can’t do. Market medical eye care like dry eye treatment and myopia control, make online booking fast, show which vision plans you accept on dedicated pages, and stand behind fittings, adjustments and warranties in your optical. Steady recent reviews help you win the map pack against chain locations."),
        ],
        "figures": {
            "cpc": {
                "type": "bars",
                "title": "Median Google Ads cost per click, 2026",
                "sub": "No optometry category exists; Physicians & Surgeons is the closest",
                "items": [["Physicians & Surgeons", 4.76, "$4.76"], ["All industries", 5.42, "$5.42"], ["Health & Fitness", 6.17, "$6.17"], ["Dentists & Dental Services", 8.00, "$8.00"]],
                "highlight": [0],
                "note": "Source: WordStream/LocaliQ 2026 Google Ads benchmarks (medians). Houston CPCs may run higher.",
                "alt": "Bar chart of Google Ads cost per click for optometrist marketing in Houston using the closest benchmark categories",
                "caption": f"National medians from {SRC['wordstream']}. Use them as a floor for Houston planning.",
            },
            "pricead": {
                "type": "checklist",
                "title": "Before a Texas eyewear price ad runs",
                "sub": "From Texas Occupations Code §351.403 and Board Rule 279.9",
                "items": ["States that a prescription is required", "Says whether the exam and follow-up are included", "Gives the end date if the offer runs under 30 days", "Discloses limited quantities with no rain checks", "Notes any per-customer limit", "For contacts, states how many lenses the price covers", "Disclosures readable or audible to an average person", "Any board certified claim names the certifying group"],
                "alt": "Checklist of Texas Optometry Board price advertising disclosures for optometrist marketing in Houston and The Woodlands",
                "caption": f"Summarized from {SRC['occ403']} and {SRC['tac279']}. Not legal advice.",
            },
            "plan": {
                "type": "steps",
                "title": "First 90 days for an eye care practice",
                "sub": "Foundation first, then ads, then medical eye care",
                "steps": [["Profile and booking", "Fix Google Business Profile, add a real booking link."], ["Plan pages", "VSP, EyeMed and other plans, one page each."], ["Tracking", "Call tracking and HIPAA-safe booking conversions."], ["Search and LSAs", "Exam, insurance and brand campaigns; apply for LSAs."], ["Medical eye care", "Dry eye and myopia pages and campaigns."], ["Review and cut", "Compare cost per kept exam; drop what doesn’t book."]],
                "alt": "Six-step 90-day marketing plan for an optometrist practice in Houston and The Woodlands",
                "caption": "Most practices skip step three. It’s the one that tells you what works.",
            },
        },
    },
]
