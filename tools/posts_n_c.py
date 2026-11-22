"""Batch 14 (c): dermatology practice marketing in The Woodlands and Houston, and bakery and coffee shop marketing in
The Woodlands and Houston.

Research, dermatology: AMN Healthcare / Merritt Hawkins 2025 physician appointment wait-time survey (dermatology 36.5
days across 15 metros; Houston 9 days average, 1 to 65 day range, 21 offices, 62% Medicare, 5% Medicaid); Texas
Medical Board's board certification advertising page (ABMS, BOS, ABOMS, or TMB-approved boards); TMLT risk alert on
TMB Rule 164 ("board eligible" and "board qualified" prohibited); American Board of Dermatology on certification
(one-year internship plus three years of dermatology residency, one of 24 ABMS boards); Tex. Occ. Code 104.003
(M.D./D.O. designations); Texas Medical Association on prescriptive authority agreements for PAs and APRNs; HHS OCR
online tracking guidance and the June 20, 2024 AHA v. Becerra vacatur note; HHS marketing guidance (authorization);
HHS OCR Manasa Health Center $30,000 settlement over review replies; Google's Health in personalized advertising
policy (Customer Match and data segments not supported; cosmetic injections are health content); Google restricted
drug terms page and Search Engine Roundtable on the October 29, 2025 change; Search Engine Land on Meta's health and
wellness event restrictions; AAD skin cancer statistics (1 in 5 lifetime, about 9,500 diagnoses a day, 99% five-year
survival when caught early, 2026 melanoma estimates); AAD Skin Cancer Awareness Month (Melanoma Monday May 4, 2026);
Space City Weather on Houston's extreme summer UV.
Research, bakery: Texas DSHS cottage food page and SB 541 enrolled text (89R; $150,000 cap adjusted annually by
CPI-U, effective Sept. 1, 2025; TCS foods with registration; mail order struck; personal delivery; label statement;
local governments can't require permits); DoorDash merchant pricing (15/25/30% delivery, 6% pickup); Google Business
Profile menu editor help; The Woodlands Township listing for The Woodlands Farmers Market (Grogan's Mill, Saturdays);
TechCrunch on TikTok's U.S. Local Feed (Feb. 11, 2026); Toast loyalty data (July 2026) and Toast coffee survey
(fielded Sept. 2025); Texas Comptroller Publication 94-117 on bakery items and sales tax.
Left out (unverified): exact status of Texas HB 3415 (2025 health-practitioner advertising bill); Houston-specific
UV index numbers; TMB-specific before/after photo rules; ezCater fees.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # dermatology post
    "amn": A("https://www.amnhealthcare.com/siteassets/amn-insights/physician/ps-2025-physician-appt-wait-times---wp-v6.pdf", "AMN Healthcare’s 2025 appointment wait-time survey"),
    "tmb_bc": A("https://tmb.state.tx.us/page/resources-advertisement-board-certification", "Texas Medical Board’s board certification advertising rules"),
    "tmlt": A("https://www.tmlt.org/risk-alerts/texas-rules-on-physician-advertising", "TMLT’s summary of TMB Rule 164"),
    "abd": A("https://www.abderm.org/public/what-does-it-mean-to-be-board-certified-by-the-abd", "the American Board of Dermatology"),
    "occ104": A("https://texas.public.law/statutes/tex._occ._code_section_104.003", "Texas Occupations Code §104.003"),
    "tma": A("https://www.texmed.org/Template.aspx?id=45849", "the Texas Medical Association"),
    "hhs_track": A("https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/", "HHS’s online tracking guidance"),
    "hhs_mkt": A("https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/marketing", "HHS’s marketing guidance"),
    "appeal": A("https://proskauer.com/blog/shortly-after-its-online-tracking-technologies-bulletin-is-declared-unlawful-hhs-ocr-stands-down-withdraws-appeal", "HHS later withdrew its appeal"),
    "manasa": A("https://www.hhs.gov/about/news/2023/06/05/hhs-office-civil-rights-reaches-agreement-health-care-provider-new-jersey-disclosed-phi-response-negative-online-reviews.html", "paid HHS $30,000"),
    "g_health": A("https://support.google.com/adspolicy/answer/16701855?hl=en", "Google’s Health in personalized advertising policy"),
    "g_drug": A("https://support.google.com/adspolicy/answer/15595717", "Google’s restricted drug terms page"),
    "ser_drug": A("https://www.seroundtable.com/google-ads-prescription-drug-terms-policy-40272.html", "Search Engine Roundtable"),
    "sel_meta": A("https://searchengineland.com/meta-ads-restrictions-health-wellness-campaigns-453094", "Search Engine Land’s breakdown"),
    "aad_stats": A("https://aad.org/media/stats-skin-cancer", "the American Academy of Dermatology"),
    "aad_month": A("https://aad.org/public/public-health/awareness-campaigns/skin-cancer-awareness-month", "AAD’s Skin Cancer Awareness Month page"),
    "scw": A("https://spacecityweather.com/theres-going-to-be-a-lot-of-it-in-the-days-ahead-so-lets-talk-about-the-sun/", "Space City Weather"),
    # bakery post
    "dshs_cf": A("https://www.dshs.texas.gov/foodestablishments/cottagefood/", "Texas DSHS cottage food page"),
    "sb541": A("https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00541F.htm", "SB 541"),
    "dd": A("https://merchants.doordash.com/en-us/products/pricing", "DoorDash’s merchant pricing page"),
    "gbp_menu": A("https://support.google.com/business/answer/9455840?hl=en", "Google’s menu editor help page"),
    "wfm": A("https://www.thewoodlandstownship-tx.gov/Events-directory/2026/2026-The-Woodlands-Farmers-Market", "The Woodlands Township’s listing"),
    "tiktok": A("https://techcrunch.com/2026/02/11/tiktok-launches-an-opt-in-local-feed-in-the-u-s-leveraging-users-precise-location", "TechCrunch"),
    "toast_loyal": A("https://pos.toasttab.com/zh-us/blog/data/restaurant-loyalty-program-return-rate", "Toast’s 2026 loyalty data"),
    "toast_coffee": A("https://pos.toasttab.com/ko-us/blog/data/consumer-coffee-preferences", "a Toast consumer survey"),
    "comptroller": A("https://comptroller.texas.gov/taxes/publications/94-117.php", "Texas Comptroller Publication 94-117"),
}

DERM = "/blog/dermatology-practice-marketing-the-woodlands-houston/"
BAKERY = "/blog/bakery-coffee-shop-marketing-the-woodlands-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: dermatology
    {
        "slug": "dermatology-practice-marketing-the-woodlands-houston",
        "title": "Dermatology Practice Marketing in The Woodlands and Houston",
        "seo_title": "Dermatology Marketing in The Woodlands & Houston",
        "desc": "Dermatology marketing for The Woodlands and Houston: medical vs. cosmetic funnels, wait times, TMB and board certification rules, HIPAA pixels, reviews.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b3",
        "hero": "medical",
        "hero_alt": "Illustration of a medical clinic for dermatology practice marketing in The Woodlands and Houston",
        "related": ["medical-practice-marketing-houston", "med-spa-marketing-the-woodlands-houston", "plastic-surgeon-marketing-houston"],
        "sections": [
            (None, f"""<p>Monday, 8:05 a.m., at a dermatology office off Research Forest. Thirty-one voicemails from the weekend. Nine are people who found a spot on their back and want it looked at. Six are existing patients needing a refill. Four are asking what a syringe of filler costs. The front desk books the mole checks for late January, because that’s the doctor’s first opening, and three of those callers quietly book somewhere in Spring instead.</p>
<p>Nobody calls that a marketing problem. It is one.</p>
<p>Dermatology practice marketing in The Woodlands and Houston comes down to running two businesses through one front desk. Medical dermatology needs to be findable, in-network and bookable fast. Cosmetic dermatology needs a sales funnel with a consult, a price conversation and follow-up. Both sit under Texas Medical Board advertising rules, HIPAA, and ad platform health policies that are stricter than most practices realize.</p>
<p>This guide is for independent and small-group practices with one to four locations around Montgomery County and north Harris County, plus anyone inside the Loop who’s tired of competing with the big systems on their terms.</p>"""),

            ("Medical and cosmetic dermatology are two different marketing jobs", f"""<p>A patient searching “dermatologist near me that takes Aetna” and a patient searching “lip filler The Woodlands” have almost nothing in common except your logo. Treat them as one audience and you’ll write mushy pages that work for neither.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Medical dermatology</th><th>Cosmetic dermatology</th></tr></thead>
<tbody>
<tr><td>Typical searches</td><td>dermatologist near me, skin cancer screening Houston, eczema doctor Spring TX, mole removal Conroe</td><td>Botox The Woodlands, chemical peel near me, laser hair removal Kingwood, melasma treatment</td></tr>
<tr><td>Who pays</td><td>Insurance, with copays and deductibles</td><td>The patient, often with financing or a membership</td></tr>
<tr><td>What decides it</td><td>In-network, soonest appointment, distance, reviews</td><td>Results photos, price, the injector, how the consult felt</td></tr>
<tr><td>Speed</td><td>Days. They want in this week.</td><td>Weeks to months. Lots of browsing.</td></tr>
<tr><td>Best channels</td><td>Google Business Profile, search ads, insurance pages, referrals from PCPs</td><td>Instagram, search ads by treatment, email and SMS, events</td></tr>
<tr><td>What to measure</td><td>New-patient appointments kept</td><td>Consults booked, consults converted, repeat visits</td></tr>
</tbody></table></div>
<p>We’d build the website and the ad account around that split. Medical service pages answer “do you take my insurance and when can I get in.” Cosmetic pages answer “what will it look like, who does it, and what does it cost.” The homepage can serve both, but the paths have to separate within one click.</p>"""),

            ("Your new-patient wait time is a marketing problem", f"""<p>Most practices think of the schedule as an operations issue. From the patient’s side, a seven-week wait is a reason to keep scrolling.</p>
<p>Houston actually looks good on paper. In {SRC['amn']}, researchers called 21 Houston dermatology offices in early 2025 and found an average wait of 9 days for a new patient, against 36.5 days across all 15 metros surveyed. The same Houston sample ranged from 1 day to 65 days. That spread is the story. Patients here know someone can see them sooner, and Google will happily show them who.</p>
<!--fig:waits-->
<p>What we’d do about it:</p>
<ul>
<li><b>Market the provider with openings.</b> If your physician is booked to February and your PA has slots Thursday, the skin-check ads and the booking page should lead with the PA. More on that below.</li>
<li><b>Show “next available” on the site.</b> Online scheduling that displays real openings converts better than a form that promises a callback. A callback at 4:45 p.m. on Friday is how you lose the patient to a practice in Cypress.</li>
<li><b>Run a cancellation list.</b> Text the waitlist when slots open. It fills holes and makes the long wait feel shorter.</li>
<li><b>Stop paying for demand you can’t serve.</b> If the medical schedule is full for six weeks, pause or trim the medical search campaigns and push cosmetic, where the injector may have room.</li>
</ul>
<p>Speed matters after the click, too. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up side, and it applies to web forms just as much as phone calls.</p>"""),

            ("Skin cancer screening seasonality and the Texas sun", f"""<p>Skin checks are the front door of medical dermatology. They’re also seasonal in a way you can plan around.</p>
<p>The numbers give you plenty to say. Per {SRC['aad_stats']}, about one in five Americans will develop skin cancer in their lifetime, roughly 9,500 people in the U.S. are diagnosed every day, and the five-year survival rate is 99% for melanoma caught before it reaches the lymph nodes. The AAD projects 234,680 new melanoma cases in 2026.</p>
<p>Houston’s sun does the rest. {SRC['scw']} has pointed out that unprotected skin can burn in half an hour or less around midday in summer and that extreme UV hangs around well into late August. Add pool season in The Woodlands, weekends on Lake Conroe and a lot of outdoor workers, and you have an audience that already knows they should get checked and keeps putting it off.</p>
<p>The calendar we’d use:</p>
<!--fig:season-->
<ul>
<li><b>April:</b> Start building. Write the skin check page, film a short video of what a full-body exam involves (patients worry about this more than they say), and line up an email to past patients.</li>
<li><b>May:</b> Skin Cancer Awareness Month. Melanoma Monday falls on the first Monday in May, which was May 4 in 2026, per {SRC['aad_month']}. Raise search budgets on skin check terms and post every week.</li>
<li><b>June through August:</b> Sunburn, sun spots and “new mole” searches. Good time for content about sunscreen and spot checks for kids before camp.</li>
<li><b>October through December:</b> Deductible season. Patients who’ve met their deductible want to get in before January. Say so plainly in emails.</li>
<li><b>January:</b> New deductibles, new insurance cards, lots of “do you take my plan” calls. Update insurance pages before the first week.</li>
</ul>
<p>One caution on copy. Fear sells skin checks and it also reads cheap. “Most skin cancers are very treatable when caught early. Book a 15-minute check” works better for us than a stock photo of a melanoma.</p>"""),

            ("Texas Medical Board advertising rules and board certification claims", f"""<p>Texas has specific rules about the phrase “board certified,” and dermatology is a specialty where they come up constantly, because so many people do skin treatments.</p>
<p>Per the {SRC['tmb_bc']}, a physician can advertise as board certified only when the certifying board is an ABMS member board, a member board of the AOA Bureau of Osteopathic Specialists, the American Board of Oral and Maxillofacial Surgery, or an organization the TMB has found substantially equivalent. {SRC['tmlt']} adds that “board eligible” and “board qualified” are prohibited in Texas advertising, and that claims like “most highly qualified” need objective data behind them.</p>
<p>The American Board of Dermatology is the one that matters here. According to {SRC['abd']}, its diplomates complete a one-year internship plus at least three years of dermatology residency, pass its exams, and keep up continuing certification. It’s one of the 24 ABMS boards. So “board-certified dermatologist” on your site means a specific thing, and patients can check it on the ABD’s own lookup.</p>
<!--fig:claims-->
<p>A few practical rules we follow on dermatology sites:</p>
<ul>
<li>Name the board: “Board certified by the American Board of Dermatology.” It’s specific and verifiable.</li>
<li>Use the degree. {SRC['occ104']} requires Texas physicians to identify the healing art they practice with designations like “M.D.” or “D.O.” on signs and printed materials. Put it on every provider page and bio.</li>
<li>Don’t let “dermatology” blur who does what. If a nurse injector or aesthetician performs a treatment, the page should say so.</li>
<li>Avoid superlatives you can’t prove. “Best dermatologist in Houston” is an invitation to a complaint. “Seeing patients in The Woodlands since 2011” is a fact.</li>
</ul>
<p>We wrote more on credentials, consult fees and procedure ads in our {L('/blog/plastic-surgeon-marketing-houston/', 'plastic surgeon marketing guide')}. The same TMB framework applies; this post sticks to what’s different for dermatology.</p>"""),

            ("Provider pages for PAs and nurse practitioners", f"""<p>Physician assistants and nurse practitioners often carry a big share of new medical visits in Houston dermatology practices. Most websites bury them on a team page with a headshot and two sentences. That’s a waste of your most available providers.</p>
<p>In Texas, PAs and APRNs in a practice like yours prescribe under a written prescriptive authority agreement with a supervising physician, as {SRC['tma']} explains. That structure is worth explaining to patients in plain words, because some are nervous about seeing “not the doctor.” A good provider page turns that nervousness into a booking.</p>
<!--fig:provider-->
<p>Give each provider a Google Business Profile if they see patients at a regular location and Google’s rules allow it for your setup; our {L('/blog/medical-practice-marketing-houston/', 'medical practice marketing post')} covers practitioner listings and how to keep them from competing with the practice listing. Then point skin-check ads at the provider with the soonest openings, and let reviews mention them by name when patients choose to (you can’t script that).</p>"""),

            ("Insurance pages patients can actually use", f"""<p>“Do you take my insurance?” might be the most-asked question in medical dermatology. Most sites answer it with a logo wall that hasn’t been updated since 2022.</p>
<p>Insurance acceptance varies a lot here. In the same AMN survey, 62% of the Houston dermatology offices called accepted Medicare and 5% accepted Medicaid. If you take Medicare, that’s worth a dedicated page, since a lot of retirees in The Woodlands, Montgomery and Kingwood are actively looking for a skin cancer doctor who does.</p>
<p>What a useful insurance section includes:</p>
<ul>
<li>One page per major carrier you’re in network with, naming the specific plans (an HMO and a PPO from the same carrier are different answers).</li>
<li>A clear line on cosmetic services: insurance doesn’t cover them, and here’s how pricing and financing work.</li>
<li>What patients should bring, and what to do if they’re switching plans in January.</li>
<li>A “last updated” date. Patients trust it more, and it reminds your staff to keep it current.</li>
</ul>
<p>These pages rank surprisingly well for “dermatologist that takes [carrier] Houston” searches, which competitors rarely target. They’re also the pages your front desk can text to callers, which shortens calls.</p>"""),

            ("Google Ads and Meta for dermatology: the health policy limits", f"""<p>Search ads work well for dermatology because people describe the problem. Structure campaigns by service and keep medical and cosmetic in separate campaigns with separate budgets.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Example keywords</th><th>Negatives to add early</th></tr></thead>
<tbody>
<tr><td>Skin checks</td><td>skin cancer screening near me, mole check The Woodlands, dermatologist Spring TX</td><td>free (unless you run free screenings), self exam, app, pictures</td></tr>
<tr><td>Medical conditions</td><td>eczema dermatologist Houston, acne doctor near me, psoriasis treatment Conroe</td><td>home remedy, cream, over the counter, reddit</td></tr>
<tr><td>Mohs and surgical</td><td>Mohs surgeon Houston, basal cell carcinoma removal</td><td>jobs, fellowship, salary, training</td></tr>
<tr><td>Cosmetic</td><td>wrinkle injections The Woodlands, chemical peel near me, laser hair removal Kingwood</td><td>course, certification, at home, kit, groupon</td></tr>
<tr><td>Brand</td><td>your practice and provider names</td><td>reviews of competitors, lawsuit (monitor these instead)</td></tr>
</tbody></table></div>
<p>Then the policies. {SRC['g_health']} treats health conditions and invasive procedures, explicitly including cosmetic injections, as a sensitive category. Customer Match lists, your own data segments and lookalike segments aren’t supported for that kind of promotion. In practice, uploading your patient list to target “people like our Botox patients” is off the table. Keywords and location do the targeting.</p>
<p>Prescription product names have their own rule. In the U.S., you can use prescription drug terms in ad text and landing pages for promotion, but keyword-targeting them requires certification, per {SRC['g_drug']}. {SRC['ser_drug']} reported the updated policy was enforced starting October 29, 2025. So an ad can name a prescription neurotoxin in the copy (trademark rules permitting), while the keyword list leans on terms like “wrinkle injections” and “forehead lines treatment” unless you hold the certification.</p>
<p>Meta is tighter. Practices classified as health and wellness advertisers can lose the ability to optimize for mid- and lower-funnel standard events, and some lose custom parameters and URL data in the pixel, according to {SRC['sel_meta']}. Instant forms on Meta and upper-funnel video tend to be the workable path, with the booking happening on your site. Our {L('/services/paid-social-advertising/', 'paid social team')} and {L('/services/search-marketing/', 'search team')} set these up so policy problems show up before launch, not after a disapproval.</p>
<p>Budget, as a starting point we’d plan with (illustrative): $2,000 to $4,000 a month on search for a single-location practice, split by what the schedule can absorb, plus $1,000 to $2,500 on Meta if you have a cosmetic program with open injector time. Your click costs depend on competition near you; our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a feel for ranges.</p>"""),

            ("HIPAA and tracking pixels on a dermatology website", f"""<p>Tracking is where dermatology sites quietly get into trouble, usually because someone installed a pixel in 2021 and nobody looked again.</p>
<p>The rules shifted in 2024. {SRC['hhs_track']} still says tracking technologies on user-authenticated pages (patient portals, logged-in booking) generally have access to protected health information, that vendors receiving PHI need a business associate agreement, and that a cookie banner is not a HIPAA authorization. But on June 20, 2024, a federal court in the Northern District of Texas vacated the part of that guidance saying HIPAA is triggered when a tracker links an IP address to a visit on a public, unauthenticated page about a health condition. {SRC['appeal']}, per Proskauer.</p>
<p>That ruling helps, and it doesn’t make everything safe. Your booking flow, intake forms and anything behind a login are still the risky parts, and Meta’s own health rules apply no matter what a court said.</p>
<!--fig:pixels-->
<p>Counting conversions without sending health details is doable. Fire a generic “appointment requested” event with no condition or service in it, keep URLs free of terms like “melanoma” or “acne,” and track calls through a provider that will sign a BAA. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} covers the mechanics. Have your compliance counsel sign off on the final setup; we’re marketers, not your lawyers.</p>"""),

            ("Before-and-after photos and patient consent", f"""<p>Cosmetic dermatology sells with photos. So does a lot of medical dermatology, honestly: acne scarring, melasma and psoriasis results are some of the most convincing images a practice can post.</p>
<p>Under HIPAA, using a patient’s information for marketing generally requires their written authorization, per {SRC['hhs_mkt']}. Full-face photos are identifiers, and a distinctive tattoo or birthmark can be too. Treatment consent forms don’t cover marketing use.</p>
<p>The process we’d set up:</p>
<ol>
<li>A separate marketing authorization that names where photos may appear (website, Instagram, ads, printed materials) and lets the patient choose.</li>
<li>Same lighting, angle and background for before and after, with no filters or retouching on the result.</li>
<li>A note on each image of the treatment, the number of sessions and the time between photos.</li>
<li>A log of who signed what, and a way to pull a photo everywhere if a patient revokes.</li>
</ol>
<p>If you offer injectables or lasers through a med spa arm, the {L('/blog/med-spa-marketing-the-woodlands-houston/', 'med spa marketing guide')} has more on content that sells treatments.</p>"""),

            ("Reviews and HIPAA-safe replies", f"""<p>Dermatology reviews are emotional. People write about the scar, the bill, the wait, or the doctor who caught something early. Your reply is read by every future patient, and it can be a HIPAA violation if you get defensive.</p>
<p>This isn’t theoretical. A New Jersey practice {SRC['manasa']} after its replies to negative online reviews disclosed patients’ health information, according to HHS. Confirming that someone is a patient can be enough of a disclosure to cause problems.</p>
<p>A reply pattern that works:</p>
<ul>
<li><b>Positive review:</b> “Thank you for taking the time to write this. We’re glad you’re happy with your experience at our Woodlands office.” No mention of the treatment, even if they named it.</li>
<li><b>Negative review:</b> “We take every concern seriously and would like to talk. Please call our practice manager at [number].” Nothing about the visit, the diagnosis or the bill.</li>
</ul>
<p>To get more reviews, send every patient the same link by text after the visit, and don’t gate it. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has request scripts you can adapt.</p>"""),

            ("The cosmetic services funnel, from first look to membership", f"""<p>Cosmetic patients in The Woodlands, Sugar Land and Memorial shop around. They follow your Instagram for months, book a consult, ask about price, leave and think about it. The practices that win are the ones that follow up.</p>
<!--fig:funnel-->
<p>Where we see dermatology practices leak:</p>
<ul>
<li>No prices online. You don’t need a full menu, but “starting at” pricing for neurotoxin, filler and peels filters tire-kickers and builds trust.</li>
<li>Consults with no next step. Every consult should end with a booked treatment, a quote sent by email, or a scheduled follow-up text.</li>
<li>No reason to come back. A membership or a simple treatment plan (“every 12 weeks”) keeps the schedule full between campaigns.</li>
<li>The medical patients never hear about cosmetic. Your skin-check patients already trust you. A quiet mention at checkout and in one email a quarter is fine, and nobody needs a hard sell.</li>
</ul>
<p>A first 90 days for a practice starting from scratch: month one fixes the profile, insurance pages, provider pages and tracking. Month two launches search by service, split by medical and cosmetic, and starts review requests. Month three adds Meta for cosmetic, the email list, and the seasonal calendar. If you’d like a senior strategist to build that plan around your schedule and providers, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do dermatologists in The Woodlands and Houston get more patients?",
             "Make it easy to find you, verify you and book you. That means a complete Google Business Profile, separate pages for medical and cosmetic services, insurance pages by carrier, provider pages for PAs and NPs with open schedules, online booking with real availability, and steady review requests. Then add search ads by service, timed around skin cancer season in May and deductible season in the fall."),
            ("Can a Texas dermatologist advertise as board certified?",
             "Yes, if the certifying board qualifies under Texas Medical Board rules. That means an ABMS member board such as the American Board of Dermatology, an AOA Bureau of Osteopathic Specialists board, or an organization the TMB has approved as substantially equivalent. Texas doesn’t allow the terms board eligible or board qualified in advertising. Naming the specific board is the safest wording."),
            ("Can I use my patient list for Google or Meta ad targeting?",
             "Generally no, for health-related promotion. Google’s Health in personalized advertising policy doesn’t support Customer Match, your own data segments or lookalikes for health conditions or invasive procedures, which includes cosmetic injections. Meta restricts health and wellness advertisers too. Patient lists also raise HIPAA questions. Target with keywords and location instead, and email patients who opted in."),
            ("Are tracking pixels allowed on a Houston dermatology website?",
             "Some are, with care. A June 2024 federal court ruling vacated the part of HHS guidance covering public, unauthenticated pages, but tracking on patient portals, logged-in booking and intake forms still raises HIPAA issues, and vendors that receive health information need a business associate agreement. Keep condition names out of events and URLs and have counsel review the setup."),
            ("When should a dermatology practice run skin cancer screening ads?",
             "Start building in April and push hardest in May, which is Skin Cancer Awareness Month and includes Melanoma Monday on the first Monday. Keep a steady presence through Houston’s summer, then run a second push from October to December when patients who met their deductible want appointments. In January, focus on insurance updates. Scale every push to the openings you actually have."),
        ],
        "figures": {
            "waits": {
                "type": "bars",
                "title": "New-patient dermatology waits, 2025",
                "sub": "Average days to a new-patient appointment, selected metros",
                "items": [["Portland", 103, "103 days"], ["Boston", 93, "93 days"], ["Minneapolis", 87, "87 days"], ["15-metro average", 36.5, "36.5 days"], ["Dallas", 20, "20 days"], ["Houston", 9, "9 days"]],
                "highlight": [5],
                "note": "Source: AMN Healthcare 2025 survey. Houston sample ranged from 1 to 65 days.",
                "alt": "Bar chart of 2025 dermatology new patient wait times, with Houston at 9 days, relevant to dermatology marketing in The Woodlands",
                "caption": f"From {SRC['amn']}. A short average still hides practices with two-month waits.",
            },
            "season": {
                "type": "columns",
                "title": "A skin check marketing calendar",
                "sub": "Relative push by month for a Houston-area practice",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [45, 30, 35, 60, 100, 75, 70, 65, 40, 70, 80, 75],
                "highlight": [4, 10],
                "y_label": "Push",
                "note": "Illustrative example",
                "alt": "Column chart of a monthly skin cancer screening marketing calendar for dermatology practices in Houston and The Woodlands",
                "caption": "May and the fall deductible months get the most budget. Match every push to real openings.",
            },
            "claims": {
                "type": "compare",
                "title": "Dermatology ad claims in Texas",
                "left": {"title": "Risky", "items": ["“Board eligible dermatologist”", "“Best dermatologist in Houston”", "“Board certified” with no board named", "Injector’s credentials left vague", "Provider name with no degree"]},
                "right": {"title": "Safer", "items": ["“Board certified by the American Board of Dermatology”", "“Seeing patients in The Woodlands since 2011”", "Board named, verifiable on ABD’s lookup", "“Treatment by [name], RN, under Dr. [name]”", "“[Name], M.D.” or “[Name], PA-C” everywhere"]},
                "alt": "Comparison of risky and safer advertising claims for dermatology practice marketing in The Woodlands and Houston under Texas rules",
                "caption": f"Based on the {SRC['tmb_bc']} and {SRC['tmlt']}. Have counsel review final copy.",
            },
            "provider": {
                "type": "checklist",
                "title": "What a PA or NP page needs",
                "sub": "For each non-physician provider at a dermatology practice",
                "items": ["Full name and credential (PA-C, FNP-C)", "Supervising or collaborating physician named", "Conditions and treatments they see", "Locations and days in clinic", "Next available appointment, live", "Insurance accepted for their visits", "A short video or real photo", "Plain-English note on training"],
                "alt": "Checklist for physician assistant and nurse practitioner provider pages on a dermatology website in Houston and The Woodlands",
                "caption": "The provider with openings should be the easiest one to book.",
            },
            "pixels": {
                "type": "steps",
                "title": "Safer conversion tracking for dermatology",
                "sub": "How to count bookings without sending health details",
                "steps": [["Inventory every tag", "List each pixel, script and tag on the site, including old ones."], ["Separate the risky pages", "Booking, intake and portal pages get no ad pixels."], ["Use generic events", "“Appointment requested,” with no condition or service name."], ["Clean the URLs", "No condition terms in URLs or query strings that tags can read."], ["Sign BAAs", "Call tracking, CRM and any vendor that touches PHI."]],
                "alt": "Five steps for HIPAA-conscious conversion tracking on a dermatology practice website in The Woodlands and Houston",
                "caption": f"Based on {SRC['hhs_track']}. Not legal advice.",
            },
            "funnel": {
                "type": "funnel",
                "title": "The cosmetic dermatology funnel",
                "stages": [["Sees your work on Instagram or search", "1,000"], ["Visits a treatment page", "220"], ["Books a consult", "30"], ["Treats", "18"], ["Returns within 6 months", "11"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how cosmetic dermatology patients in The Woodlands and Houston move from first view to repeat treatment",
                "caption": "The last two steps usually decide profit, and they’re mostly follow-up.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: bakery and coffee
    {
        "slug": "bakery-coffee-shop-marketing-the-woodlands-houston",
        "title": "Bakery and Coffee Shop Marketing in The Woodlands and Houston",
        "seo_title": "Bakery & Coffee Shop Marketing in The Woodlands",
        "desc": "Bakery and coffee shop marketing for The Woodlands and Houston: morning traffic, Google menus, Instagram and TikTok, custom cakes, catering, cottage food law.",
        "category": "Local marketing",
        "icons": ["Instagram", "TikTok", "Google Business Profile"],
        "art": "b2",
        "hero": "restaurant",
        "hero_alt": "Illustration of a cafe storefront for bakery and coffee shop marketing in The Woodlands and Houston",
        "related": ["restaurant-marketing-the-woodlands-houston", "restaurant-direct-online-ordering-vs-delivery-apps", "facebook-vs-instagram-vs-tiktok-local-business"],
        "sections": [
            (None, f"""<p>Saturday, 7:10 a.m. The line is out the door, the kolaches are gone by 8:30, and someone is asking if you can do a two-tier unicorn cake for next Saturday. Tuesday at 2 p.m., you can hear the espresso machine hum in an empty room. And there’s an Instagram DM from Thursday asking about 60 dozen cookies for a company event on Research Forest. Nobody has answered it.</p>
<p>Most bakery and coffee shop owners we talk to don’t have a traffic problem on Saturday morning. They have a Tuesday problem, an order-taking problem, and no idea which of their marketing actually brings people in.</p>
<p>Bakery and coffee shop marketing in The Woodlands and Houston works best when you treat the business as three revenue streams. Walk-in traffic runs on Google Maps, photos and the morning commute. Custom cakes and special orders run on Instagram and fast replies. Catering and office orders run on relationships and a simple ordering page. Each needs its own marketing, and the last two usually carry the margin.</p>
<p>This guide is for independent bakeries, cafés and coffee shops, plus home bakers working under Texas cottage food law, from Market Street to Old Town Spring to Katy.</p>"""),

            ("Three businesses behind one counter", f"""<p>Before spending a dollar, know which stream you’re trying to grow. They behave very differently.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Walk-in counter</th><th>Custom cakes and orders</th><th>Catering and office</th></tr></thead>
<tbody>
<tr><td>Ticket size</td><td>Small, high frequency</td><td>Larger, occasional</td><td>Largest, repeatable</td></tr>
<tr><td>How they find you</td><td>Google Maps, walking past, a friend</td><td>Instagram, Google search, a party they attended</td><td>Office managers, referrals, Google search</td></tr>
<tr><td>What decides it</td><td>Hours, distance, photos, line length</td><td>Portfolio, reply speed, price clarity</td><td>Reliability, invoicing, delivery</td></tr>
<tr><td>Lead time</td><td>Minutes</td><td>Days to weeks</td><td>Days, then recurring</td></tr>
<tr><td>Marketing that works</td><td>Business Profile, short video, loyalty</td><td>Portfolio posts, search ads, inquiry form</td><td>Direct outreach, a catering page, follow-up</td></tr>
</tbody></table></div>
<p>A pastry case can be full and the business can still struggle, because walk-in margins are thin after labor and rent in a place like Hughes Landing. Custom and catering orders are planned, made in batches and paid up front. We’d put at least half of any marketing effort there.</p>"""),

            ("Foot traffic in Market Street, Hughes Landing and Town Center districts", f"""<p>A shop in a walkable district plays a different game than one in a strip center on FM 2920. In The Woodlands Town Center, along Market Street, around Hughes Landing and the Waterway, and in places like Sugar Land Town Square or Kingwood Town Center, you’re selling to people who are already out. Shoppers, office workers, families at a weekend event, hotel guests.</p>
<p>What matters there:</p>
<ul>
<li><b>Your Google Maps pin and photos.</b> People standing on the sidewalk search “coffee near me” and pick from the map. Accurate pin placement and a street-view photo of your door matter more than you’d think when you’re tucked behind a fountain.</li>
<li><b>District events.</b> Holiday events, concerts and weekend markets in these districts bring crowds that aren’t regulars. Post the day before (“open until 9 during the event, hot chocolate by the door”) and extend hours when it pays.</li>
<li><b>Parking reality.</b> If customers have to use a garage, say which one and how long it takes to walk. It reduces “too hard to get there” friction.</li>
<li><b>Neighbor tenants.</b> Salons, boutiques and fitness studios nearby are natural partners for a punch card swap or a morning pastry drop.</li>
</ul>
<p>Strip-center shops along Woodlands Parkway, Kuykendahl or 1488 win differently. Drive-by visibility, a sign that’s readable at 40 mph, and being the obvious stop on the way to work or school. The {L('/blog/restaurant-marketing-the-woodlands-houston/', 'restaurant marketing guide')} has more on competing in a crowded dining district; this post focuses on what’s specific to bakeries and coffee.</p>"""),

            ("The morning commute and the school run", f"""<p>Coffee is a habit business. {SRC['toast_coffee']} fielded in September 2025 found about 90% of respondents buy coffee out at least once a week, 36% buy three to five times a week, and 16% buy every single morning. The same survey found brand loyalty was the top reason for only 1% of people. Convenience and habit win.</p>
<p>In the Houston suburbs, habit follows the commute and the school run. Parents drop off at a Conroe ISD or Tomball ISD campus, then head to I-45, the Grand Parkway or the Hardy Toll Road. If you’re on that route and they know you can get them in and out in four minutes, you’re in the habit. If they have to turn left across three lanes, you’re not.</p>
<!--fig:hours-->
<p>Practical moves:</p>
<ul>
<li>Open early enough. If the nearest elementary drop-off ends at 7:45, a 7:30 opening misses most of it. Check your nearest campuses’ bell schedules.</li>
<li>Run order-ahead with a pickup shelf, and say “order ahead, skip the line” on the door, on Google and in every post for a month.</li>
<li>Schedule ads for the morning. A small Meta or Google budget from 6 to 9 a.m. inside a three-mile radius is a cheap way to stay top of mind with commuters.</li>
<li>Fix the slow afternoon with a reason. An after-school deal for kids, a 2 p.m. cold brew special in summer, or a remote-worker table.</li>
</ul>
<p>We’ve run breakfast-daypart marketing for Toasted Yolk, and the pattern holds: morning customers decide fast and come back on routine, so being easy beats being clever.</p>"""),

            ("Google Business Profile: menu, photos, hours and categories", f"""<p>For a bakery or coffee shop, the Google Business Profile is the front window for everyone who hasn’t walked past yet. Most we look at are half-finished.</p>
<p>Start with the menu. Food and drink businesses can use Google’s menu editor to add sections, items, descriptions and prices, and changes can take 24 to 48 hours to show on Maps and Search, per {SRC['gbp_menu']}. You can upload a photo or PDF of the menu, and if Google finds menus from several sources, you can pick your preferred one. Pick yours. A third-party delivery menu with marked-up prices showing as your “official” menu costs you walk-ins.</p>
<!--fig:gbp-->
<p>Two bakery-specific things. Seasonal items should show up the week they launch: king cake in January, pan de muerto in late October, pumpkin anything in September. And holiday hours need updating as special hours before Thanksgiving and Christmas, when “is it open” searches spike and a wrong answer means a family drove across Spring for nothing.</p>
<p>Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest of local ranking. For a bakery the short version is photos, reviews, accurate hours and a category that matches what you mostly sell (Bakery, Coffee shop, Cake shop, Donut shop or Café as primary, and the others as secondary only if true).</p>"""),

            ("Instagram and TikTok content that sells pastries", f"""<p>Food is the easiest content category there is, and most bakeries still post the same flat-lay of a croissant on marble. The content that brings people in shows motion, timing and a reason to come today.</p>
<!--fig:content-->
<p>TikTok has made local discovery more direct. In February 2026 it launched an opt-in Local Feed in the U.S. that ranks posts about nearby dining, events and shopping by location, topic and timing, per {SRC['tiktok']}. The feed is limited to users 18 and older who share precise location. If your videos are tagged to your location and posted when things are happening (“fresh batch at 3,” “the Saturday line moves fast, here’s proof”), they have a better shot at reaching people within driving distance.</p>
<p>A workable posting rhythm for a two-person shop:</p>
<ul>
<li>Three short videos a week, filmed on a phone: something coming out of the oven, a cake decorating time-lapse, a regular’s order being made.</li>
<li>One Story a day with what’s in the case right now, or what’s sold out.</li>
<li>One finished custom cake post a week, with the occasion and the lead time in the caption (“booked 10 days out, starts at $X for 20 servings”).</li>
</ul>
<p>Use the same videos on Instagram Reels and TikTok, minus watermarks. Our {L('/blog/facebook-vs-instagram-vs-tiktok-local-business/', 'platform comparison for local businesses')} goes deeper on which platform suits which audience; for most bakeries in the Houston suburbs, Instagram carries the custom orders and TikTok brings the new walk-ins.</p>"""),

            ("Custom cake orders: the high-margin funnel", f"""<p>Custom cakes are where independent bakeries make real money, and where they lose the most through slow replies. A mom planning a sixth birthday in Cypress messages four bakeries. The first to answer with a price range and an open date usually wins.</p>
<!--fig:cakes-->
<p>How we’d build it:</p>
<ol>
<li><b>A custom order page</b> with “starting at” prices by size or servings, lead times, a gallery, and an inquiry form that asks for date, servings, flavor, design idea and budget. The budget field saves everyone time.</li>
<li><b>A reply standard.</b> Answer every inquiry within a few hours during business hours, even if it’s “got it, quote by tonight.” Set an auto-reply on Instagram DMs that points to the form.</li>
<li><b>Deposits.</b> Take a deposit to hold the date. It turns a maybe into a booking and cuts no-shows.</li>
<li><b>Search ads for high-intent terms.</b> “Custom cakes The Woodlands,” “birthday cake near me,” “wedding cake Conroe,” “smash cake Spring TX,” “gender reveal cake Katy.” Negatives: recipe, how to, Walmart, Costco, HEB, cake mix, classes, jobs.</li>
<li><b>Follow-up after pickup.</b> Ask for a review and a photo from the party. Party photos with real kids and real tables make better portfolio posts than studio shots (get permission before posting).</li>
</ol>
<p>A Google Ads test for custom cakes doesn’t need to be big: $500 to $1,000 a month in a tight radius is enough to learn (illustrative, and it depends on how many orders you can take). Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers why a fast reply often matters more than the ad itself.</p>"""),

            ("Catering and office orders", f"""<p>The Woodlands has a lot of offices: Research Forest, Hughes Landing, the towers around Lake Robbins and Timberloch, plus medical offices along I-45. Every one has someone ordering breakfast for a Monday meeting or a client visit. Office managers want one thing: an order that shows up on time, with an invoice they can expense.</p>
<p>What makes you the easy choice:</p>
<ul>
<li>A catering page with boxed packages and per-person prices (“breakfast box for 10, pastries, fruit, coffee for 10”), minimum order, lead time and delivery area.</li>
<li>Online ordering with invoicing or a company card on file. Phone tag loses office orders.</li>
<li>Drop-offs. Bring a sample box to the front desks of nearby offices and medical practices with a menu and a QR code. It’s old-fashioned and it works.</li>
<li>A reorder reminder. If a company orders every quarter for board meetings, a reminder email two weeks ahead is easy money.</li>
</ul>
<p>One tax detail worth asking your CPA about: {SRC['comptroller']} says bakery items sold without plates or eating utensils aren’t subject to Texas sales tax, while ready-to-eat food generally is. Catering packages with plates, coffee service and setup can be taxed differently from a box of muffins. Price your quotes accordingly.</p>"""),

            ("Loyalty apps and the regulars you already have", f"""<p>Regulars are the cheapest marketing a coffee shop has. A loyalty program just makes sure you can reach them again.</p>
<p>Point-of-sale companies have numbers on this, with the usual vendor caveat. {SRC['toast_loyal']} reports that enrolling a guest in loyalty raised return rates from about 7% to nearly 30% in its own platform study, and that more than half of diners in a 2026 survey left a program because rewards were too hard to earn. Treat the exact figures as a vendor’s, and the direction as believable.</p>
<p>What we’d set up:</p>
<ul>
<li>Use the loyalty built into your POS (Square, Toast, Clover) before buying a separate app. One system means one customer list.</li>
<li>Keep the reward close. Something like “every 8th drink free” beats a points system nobody can calculate.</li>
<li>Collect phone and email at sign-up, then actually use them: new seasonal items, holiday preorder deadlines, a slow-day offer.</li>
<li>Preorders for Thanksgiving pies and Christmas cookies go to loyalty members first. It fills your production schedule early.</li>
</ul>
<p>Texas has specific rules for marketing texts, including registration requirements for some senders. Read our {L('/blog/sms-marketing-small-business-texas-rules/', 'SMS marketing guide for Texas businesses')} before you blast your list.</p>"""),

            ("Local events and farmers markets", f"""<p>Farmers markets are where a lot of Houston bakeries started, and they’re still one of the best ways to get a product into new mouths.</p>
<p>In The Woodlands, the farmers market runs Saturdays at the Grogan’s Mill shopping center, 7 Switchbud Place, sponsored by the Grogan’s Mill Village Association. Per {SRC['wfm']}, hours are 9 a.m. to 1 p.m. from October through June and 9 a.m. to noon in July through September, rain or shine. Tomball, Conroe, Kingwood and Houston’s inner-loop neighborhoods all have their own markets with different crowds.</p>
<p>Make a market booth do marketing work:</p>
<ul>
<li>A QR code on the table that goes to your custom order page and loyalty sign-up.</li>
<li>Samples of the thing you most want people to come back for, not just whatever’s left.</li>
<li>A “market regulars” email or text: what you’re bringing this Saturday, with preorder pickup at the booth.</li>
<li>Photos and video from the booth for Sunday’s posts.</li>
</ul>
<p>School carnivals, HOA events, church fundraisers and youth sports tournaments in Spring and Magnolia are worth a look too. A donated cookie tray with your name on it reaches families who will need a birthday cake within the year.</p>"""),

            ("Texas cottage food law for home bakers after the 2025 changes", f"""<p>Texas changed its cottage food law in 2025, and the changes matter for anyone baking from home in Montgomery or Harris County.</p>
<p>Under {SRC['sb541']}, effective September 1, 2025, the annual gross income cap for a cottage food operation rose from $50,000 to $150,000, with the state adjusting it annually for inflation using CPI-U. According to the {SRC['dshs_cf']}, operators can now sell most foods except a list of exclusions (meat, poultry, seafood, ice cream and other frozen ice products, low-acid canned goods, raw milk products, and CBD or THC products). Foods that need time and temperature control for safety are allowed only if the operation registers with DSHS. Local governments can no longer require permits or fees for cottage food production or direct sales.</p>
<!--fig:cottage-->
<p>The marketing-relevant parts:</p>
<ul>
<li><b>Online sales are fine, shipping isn’t.</b> The bill struck mail order. Internet sales are allowed when you, an employee or a household member personally deliver the food. So your ads and website should target the area you can actually drive to.</li>
<li><b>Labels go online first.</b> For online sales, required labeling information has to be posted on your website before the customer pays. Every product page needs it.</li>
<li><b>The disclosure.</b> Labels must include a statement that the product was made in a private residence not subject to governmental licensing or inspection. Don’t hide it; customers who buy from home bakers expect it.</li>
<li><b>Training.</b> Operators need an accredited food handler course.</li>
<li><b>A registration number can replace your home address</b> on labels if you register with DSHS. Good for privacy if you’re posting your work publicly.</li>
</ul>
<p>Home bakers can run Instagram, TikTok, Google Ads and a Google Business Profile like any other business. If you deliver and don’t want your address public, you can set the profile up as a service-area business with no address shown.</p>"""),

            ("Delivery apps vs. direct ordering for bakeries", f"""<p>Delivery apps bring new customers and take a big slice. Per {SRC['dd']}, DoorDash Marketplace delivery commissions run 15%, 25% or 30% depending on the plan, with pickup orders at 6%.</p>
<!--fig:commission-->
<p>Bakeries have a few quirks that make apps less attractive than they are for a burger place. Cakes and delicate pastries don’t travel well with a stranger driving. Morning coffee orders are small, so the percentage hurts more. And the people ordering a dozen cookies for an office are usually happy to pick up or pay a delivery fee to you directly.</p>
<p>What we’d do:</p>
<ul>
<li>Use apps for discovery, with a limited menu of items that travel well.</li>
<li>Push direct order-ahead pickup everywhere else: Google, Instagram bio, the door, the bag.</li>
<li>Put a card in every app order with a reason to order direct next time.</li>
<li>Keep custom cakes and catering off the apps entirely.</li>
</ul>
<p>We ran the full commission math, platform options and pricing parity questions in our {L('/blog/restaurant-direct-online-ordering-vs-delivery-apps/', 'direct ordering vs. delivery apps post')}, and the same logic applies to cafés.</p>
<p>A starting monthly budget we’d plan with for a single-location shop (illustrative): $300 to $800 on morning-radius social ads, $500 to $1,000 on custom cake and catering search ads, and the rest of your effort on content, Google Business Profile and loyalty, which mostly cost time. If you want a senior strategist to turn that into a plan around your shop, your hours and the orders you want more of, <a href="/contact/">get in touch</a>. Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} can build the custom order and catering pages too.</p>"""),
        ],
        "faq": [
            ("How do I get more customers for my bakery in The Woodlands or Houston?",
             "Finish your Google Business Profile with the menu, fresh photos and accurate hours, then post short videos of what’s coming out of the oven. Build a custom order page with starting prices and a fast reply process, since custom cakes carry the best margins. Add a catering page for nearby offices, a simple loyalty program, and small morning ads around your shop during commute hours."),
            ("What is the Texas cottage food sales limit in 2025 and 2026?",
             "Senate Bill 541 raised the annual gross income limit for Texas cottage food operations from $50,000 to $150,000, effective September 1, 2025, and the state adjusts it each year for inflation. Operators can sell most foods except listed exclusions such as meat, seafood and ice cream, and time and temperature controlled foods require DSHS registration. Mail-order shipping isn’t allowed; personal delivery is."),
            ("Should a coffee shop use DoorDash and Uber Eats?",
             "They can help with discovery, but the fees are steep for small coffee orders. DoorDash Marketplace charges 15%, 25% or 30% on delivery depending on the plan, and 6% on pickup. Most coffee shops do better listing a short menu of items that travel well on apps while pushing direct order-ahead pickup through Google, Instagram and in-store signs."),
            ("How do bakeries get more custom cake orders?",
             "Show your work, show your prices and answer fast. Post a finished custom cake each week with the lead time, build a custom order page with starting prices and an inquiry form that asks for date, servings and budget, and reply within a few hours. Search ads for terms like custom cakes or birthday cake near me in a tight radius around your shop work well."),
            ("What should a bakery put on its Google Business Profile?",
             "Pick a primary category that matches what you mostly sell, such as Bakery, Coffee shop or Cake shop. Add your menu through Google’s menu editor with prices, upload fresh photos of the case, drinks, storefront and parking, set accurate hours plus special holiday hours, and add order-ahead and custom order links. Reply to reviews and post seasonal items the week they launch."),
        ],
        "figures": {
            "hours": {
                "type": "columns",
                "title": "Where a suburban coffee shop’s day goes",
                "sub": "Share of daily transactions by hour, weekday",
                "labels": ["6a", "7a", "8a", "9a", "10a", "11a", "12p", "1p", "2p", "3p", "4p", "5p"],
                "values": [45, 100, 90, 60, 40, 35, 40, 30, 20, 35, 25, 15],
                "highlight": [1, 2],
                "y_label": "Traffic",
                "note": "Illustrative example",
                "alt": "Column chart of weekday coffee shop traffic by hour near The Woodlands and Houston, peaking with the morning commute and school run",
                "caption": "Your POS has your real curve. Ad schedules and staffing should follow it.",
            },
            "gbp": {
                "type": "checklist",
                "title": "Google Business Profile for a bakery",
                "sub": "The settings that decide walk-ins",
                "items": ["Primary category that matches your main sales", "Menu in Google’s editor, with prices", "Your own menu chosen as preferred", "Fresh photos of the case each week", "Storefront and parking photos", "Special hours for every holiday", "Order-ahead and custom order links", "Seasonal items posted at launch"],
                "alt": "Checklist of Google Business Profile settings for bakery and coffee shop marketing in The Woodlands and Houston",
                "caption": f"Menu details from {SRC['gbp_menu']}.",
            },
            "content": {
                "type": "compare",
                "title": "Bakery content: what flops and what sells",
                "left": {"title": "Usually flops", "items": ["Flat-lay of one croissant on marble", "“Happy Monday!” graphics", "Stock coffee photos", "Posting whenever you remember", "No location tag"]},
                "right": {"title": "Usually sells", "items": ["Tray coming out of the oven, with sound", "“Fresh batch at 3, there are 24”", "Real regulars and real orders", "Same three days every week", "Location tagged, timed to events"]},
                "alt": "Comparison of social media content that flops and content that sells for bakeries and coffee shops in The Woodlands and Houston",
                "caption": "Motion, timing and a reason to come today beat pretty stills.",
            },
            "cakes": {
                "type": "funnel",
                "title": "The custom cake order funnel",
                "stages": [["Inquiries (DMs, forms, calls)", "40"], ["Replied within 3 hours", "34"], ["Quote sent with date held", "24"], ["Deposit paid", "15"], ["Review or photo after the party", "7"]],
                "note": "Illustrative example",
                "alt": "Funnel of custom cake inquiries to paid orders for a bakery in The Woodlands and Houston",
                "caption": "Most lost orders disappear between the first two steps.",
            },
            "cottage": {
                "type": "stats",
                "title": "Texas cottage food law after SB 541",
                "stats": [["$150K", "annual gross income cap, adjusted for inflation"], ["Sept. 1, 2025", "date the changes took effect"], ["$0", "local permit fees allowed for direct sales"], ["No", "mail-order shipping; personal delivery only"]],
                "note": "Source: Texas DSHS, SB 541 (89th Legislature)",
                "alt": "Stats on the 2025 Texas cottage food law changes that affect home bakers marketing in The Woodlands and Houston",
                "caption": f"From the {SRC['dshs_cf']} and {SRC['sb541']}.",
            },
            "commission": {
                "type": "bars",
                "title": "What a $40 order costs on DoorDash",
                "sub": "Commission only, before payment processing or promotions",
                "items": [["Premier delivery (30%)", 12, "$12.00"], ["Plus delivery (25%)", 10, "$10.00"], ["Basic delivery (15%)", 6, "$6.00"], ["Pickup (6%)", 2.4, "$2.40"], ["Direct order-ahead", 0.1, "Processing only"]],
                "highlight": [4],
                "note": "Commission rates from DoorDash’s published merchant pricing",
                "alt": "Bar chart of DoorDash commission on a $40 bakery order versus direct ordering for coffee shops in The Woodlands and Houston",
                "caption": f"Rates from {SRC['dd']}. Your card processor still takes its cut on direct orders.",
            },
        },
    },
]
