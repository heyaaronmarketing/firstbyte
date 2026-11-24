"""Batch 15 (module d): private school enrollment marketing in The Woodlands and Houston, and self storage marketing
in Houston.

Research (private schools): SB 2 (89R) enrolled text on capitol.texas.gov (Sec. 29.358(b)(2) accreditation by an
organization recognized by TEPSAC or TEA, norm-referenced test grades 3-12, two school years of continuous operation;
Sec. 29.361 85% of statewide average funding, $30,000 cap with disability, $2,000 homeschool; Sec. 29.3521 $1 billion
cap for the 2025 biennium; Sec. 29.365 no charging TEFA students more than the standard amount; Sec. 29.368 admissions
independence); Texas Comptroller releases of Dec 22, 2025 (about 600 schools in 10 days, Feb 4 - Mar 17 window,
$10,474), Mar 17, 2026 (deadline extended to Mar 31, 2,200 schools, 229,000+ applications) and Aug 3, 2026 (85,000+
confirmed, 120,000+ waitlisted, four in five under 200% FPL); Community Impact Aug 4, 2026 (274,000 applicants,
tiers, Tier 4 none accepted, Houston ISD 3,327 and Fort Bend ISD 2,024 participants); Texas Private School
Association family page (2027-28 applications expected late winter or spring 2027, schools may charge the gap,
norm-referenced testing, intent to continue); Post Oak School admissions page (Dec 18, 2026 deadline, Mar 5, 2027
decisions, Mar 24 contract deadline); The John Cooper School admission FAQ (January deadline, decisions typically the
first Friday in March, Clarity for aid); PetaPixel on Meta's January 2023 teen ad changes (age and location only);
Social Media Today on Meta's Jan 15, 2026 targeting consolidation; GreatSchools help center (free claimed profile
fields, can respond to but not remove reviews, Enhanced Profiles) and its Dec 2025 parent survey (1,000+ parents, 70%
use school sites and third-party sites); Niche K-12 Premium Profile page (events, reviews, inquiries into Finalsite,
Ravenna, Blackbaud, FACTS); Google Maps prohibited content policy.
Self storage: StorageCafe Houston statistics page (Oct 2026: 405 facilities, 28.5M sq ft, 6.9 sq ft per capita, $97
and $119 10x10 street rates); RentCafe/StorageCafe June 2026 report (Houston 789,519 sq ft forecast for 2026, 3% of
stock; national $135 average street rate, down 1.5%); StorageCafe 40-year apartment analysis via AOL (240,659
apartment units, apartments since 2015 44 sq ft smaller); Public Storage 2025 10-K (3,171 facilities, nearly three
quarters of new rentals via eRental and Rent by Phone); Inside Self Storage on the Extra Space / Life Storage merger
(July 20, 2023, 3,500+ stores); SpareFoot knowledge base on OneTime (Bid x unit price, 50% move-in rate minimum)
and RentPercent pricing; Tex. Prop. Code 59.043 via FindLaw (notice contents, 14-day warning, in person / email /
verified mail, email only with conspicuous lease clause); U-Haul releases (30 days free storage after May 2024
Houston storms and Hurricane Beryl, July 2024); TPWD Lake Conroe page (20,118 acres, Montgomery and Walker counties);
Google Business Profile guidelines; Google Ads location options; Google Maps prohibited content policy.
Not verified and left out: current 59.044 advertising text (2023 and 2025 bills to allow online-only notices could
not be confirmed as enacted), Google Business Profile access-hours field names, Houston storage CPC benchmarks.
Competitor/PAA phrasing read for "private school marketing", "how to increase enrollment in private school",
"private school advertising ideas", "self storage marketing", "how to market a self storage facility",
"self storage google ads", "how to increase occupancy self storage".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # private school post
    "sb2": A("https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00002F.htm", "the enrolled text of Senate Bill 2"),
    "cpa_dec": A("https://comptroller.texas.gov/about/media-center/news/20251222-hundreds-of-texas-schools-already-enrolled-in-education-freedom-accounts-program-1766422819758", "the Comptroller’s December 2025 release"),
    "cpa_mar": A("https://comptroller.texas.gov/about/media-center/news/20260317-texas-education-freedom-account-application-deadline-extended-through-march-31-1773784632313", "the Comptroller’s March 17 update"),
    "cpa_aug": A("https://comptroller.texas.gov/about/media-center/news/20260803-comptroller-don-huffines-reports-record-setting-demand-for-education-freedom-in-texas-au-1785712698352", "the Comptroller’s August 2026 report"),
    "ci_tefa": A("https://communityimpact.com/bellaire-meyerland-west-university/texas-legislature/85k-students-will-use-new-texas-education-freedom-accounts-this-school-year/", "Community Impact’s breakdown of the first-year numbers"),
    "tpsa": A("https://texasprivateschools.org/families/school-choice", "the Texas Private School Association"),
    "postoak": A("https://www.postoakschool.org/admissions/applying", "The Post Oak School’s admissions page"),
    "cooper": A("https://www.johncooper.org/page/admission/admission-faq", "The John Cooper School’s admission FAQ"),
    "teens": A("https://petapixel.com/2023/01/11/instagram-and-facebook-to-limit-adverts-targeting-teens/", "PetaPixel’s report on the change"),
    "smt": A("https://www.socialmediatoday.com/news/meta-removes-more-detailed-ad-targeting-options-facebook-instagram/757856/", "Social Media Today"),
    "gs_help": A("https://intercom.help/greatschools/en-us/articles/18233975-your-guide-to-greatschools-profiles", "GreatSchools’ guide to school profiles"),
    "gs_survey": A("https://blog.greatschools.org/2025/12/09/new-national-survey-finds-parents-want-clearer-school-information-and-are-more-satisfied-when-they-can-find-it/", "a GreatSchools survey of more than 1,000 K-12 parents"),
    "niche": A("https://www.niche.com/about/partners/k12/premium-profile/", "Niche’s Premium Profile page"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy"),
    # self storage post
    "sc_hou": A("https://www.storagecafe.com/self-storage-industry-statistics/us/tx/houston/", "StorageCafe’s Houston market page"),
    "rc_june": A("https://www.rentcafe.com/blog/self-storage/self-storage-report-june-2026/", "Yardi Matrix’s June 2026 self storage report"),
    "sc_apts": A("https://www.aol.com/news/40-apartment-boom-fuels-soaring-143003649.html", "a StorageCafe analysis of 40 years of building"),
    "psa": A("https://s1.q4cdn.com/588671402/files/doc_financials/2025/q4/2025-10-K_FINAL-02-12-16-12PM.pdf", "Public Storage’s 2025 annual report"),
    "exr": A("https://www.insideselfstorage.com/self-storage-investing-real-estate/self-storage-reits-extra-space-life-storage-complete-merger", "Inside Self Storage"),
    "sf_one": A("https://support.sparefoot.com/sparefoot-marketplace/account-management/move-in-fees-and-bidding/how-are-sparefoot-fees-calculated-onetime-pricing", "SpareFoot’s own help article"),
    "sf_rent": A("https://support.sparefoot.com/sparefoot-marketplace/account-management/move-in-fees-and-bidding/how-are-sparefoot-fees-calculated-rentpercent-pricing", "RentPercent pricing"),
    "lien": A("https://codes.findlaw.com/tx/property-code/prop-sect-59-043/", "Texas Property Code Section 59.043"),
    "uhaul_may": A("https://www.uhaul.com/Articles/About/U-Haul-Offers-30-Days-Free-Self-Storage-Following-Houston-Storms-31461/", "after the May 2024 windstorm"),
    "uhaul_beryl": A("https://www.uhaul.com/Articles/About/U-Haul-Offers-Free-Storage-After-Beryl-Causes-Flooding-Damage-IN-3-States-31903", "again after Hurricane Beryl"),
    "tpwd": A("https://tpwd.texas.gov/fishboat/fish/recreational/lakes/conroe/", "Texas Parks and Wildlife"),
    "gbp": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s Business Profile guidelines"),
    "gloc": A("https://support.google.com/google-ads/answer/1722038?hl=en", "Google Ads location options"),
}

SCHOOL = "/blog/private-school-enrollment-marketing-the-woodlands-houston/"
STORAGE = "/blog/self-storage-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: private schools
    {
        "slug": "private-school-enrollment-marketing-the-woodlands-houston",
        "title": "Private School Enrollment Marketing in The Woodlands and Houston",
        "seo_title": "Private School Marketing in The Woodlands & Houston",
        "desc": "Private school enrollment marketing for The Woodlands and Houston: admissions funnel, open house timing, TEFA, Google and Meta ads, Niche and reviews.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b4",
        "hero": "browser",
        "hero_alt": "Illustration of a school website for private school enrollment marketing in The Woodlands and Houston",
        "related": ["daycare-marketing-houston-the-woodlands", "tutoring-center-marketing-houston", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>The Saturday open house went well. Forty-one families signed the iPad in the front hall, the eighth graders gave tours without wandering off, and the coffee held out. On Monday the admissions director exports the sign-ins and starts sorting. Twelve already had an inquiry on file. Nine of the emails bounce or are clearly typed by a toddler. Nobody can say which ones came from the Instagram ads, the mailer that hit Sterling Ridge, or a friend at pickup.</p>
<p>Application deadlines at a lot of Houston schools land between mid-December and the end of January. That leaves about eight weeks to turn those 41 families into applications.</p>
<p>Private school enrollment marketing in The Woodlands and Houston comes down to getting in front of parents during the few months they’re actually comparing schools, making the tour easy to book, and then following up like a person instead of an autoresponder. Everything else (ads, Niche, reviews, the new Education Freedom Accounts) feeds that funnel. This guide is for heads of school, admissions directors and marketing leads at independent, faith-based and Montessori schools from Houston up through Spring, The Woodlands, Conroe and Magnolia.</p>"""),

            ("The admissions funnel: inquiry, tour, application, enrollment", f"""<p>Every school has the same four stages, whatever the software calls them. Each one leaks for a different reason.</p>
<!--fig:funnel-->
<p><b>Inquiry.</b> A form fill, a call, a Niche inquiry or an open house RSVP. The leak here is speed. A parent who fills out your inquiry form at 9:40 p.m. on a Tuesday has usually filled out two others that night. The school that replies by morning with a real name and a tour link tends to get the visit. We cover response times in more detail in our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')}.</p>
<p><b>Tour.</b> The biggest drop-off in most funnels we see is from inquiry to tour. Fix it by making tours bookable online, offering a weekday morning and at least one evening or Saturday slot, and sending a reminder text the day before.</p>
<p><b>Application.</b> Families who tour and don’t apply are usually stuck on cost, a spouse who hasn’t visited, or doubt about getting in. Answer those in the follow-up.</p>
<p><b>Enrollment.</b> An acceptance isn’t a deposit. Between decision letters in March and contract deadlines a few weeks later, families are weighing your offer against other schools, aid packages and the public school down the street. This is where a call from the head of school or a current parent from the same neighborhood earns its keep.</p>
<p>Track all four stages by source, every month. Counting only inquiries keeps you funding channels whose families never visit.</p>"""),

            ("The Houston and The Woodlands admissions calendar", f"""<p>Plenty of Houston private schools run on a fixed cycle. {SRC['postoak']} lists a first-round application deadline of December 18, 2026, supporting documents due January 15, decisions on March 5, 2027 and contracts due March 24. In The Woodlands, {SRC['cooper']} says its deadline is in January and decisions typically go out the first Friday in March, though it accepts applications after the deadline.</p>
<p>Parish schools, Montessori programs and smaller Christian schools in Spring, Tomball and Conroe often run rolling admissions. Your families still live on the selective schools’ calendar, because many applied there too.</p>
<!--fig:season-->
<p>That shape drives the media plan. Here’s how we’d set it for a school with a January deadline:</p>
<ul>
<li><b>August to September.</b> Re-enrollment communication starts for current families, and the first open house dates go live on the website, Google Business Profile and Niche. Light awareness ads.</li>
<li><b>October to mid-January.</b> The main push. Search ads on full budget, Meta ads promoting specific open house dates, and retargeting of everyone who visited the admissions pages.</li>
<li><b>February to March.</b> Ads shift to late applicants and rolling-admission grades. Families who were waitlisted elsewhere start looking again in March, which is a quiet opportunity for schools with seats.</li>
<li><b>April to July.</b> Relocation season. Families transferring to Houston search all summer; keep a smaller campaign running for them.</li>
</ul>
<p>Pre-K and kindergarten families start earlier than you’d expect, often the fall before. If your youngest grades are the ones you need to fill, start those campaigns in September.</p>"""),

            ("Texas Education Freedom Accounts: what changed for private schools", f"""<p>Senate Bill 2, passed in 2025, created Texas Education Freedom Accounts (TEFA), the state’s education savings account program. Here’s what it means for a school’s marketing, kept to what the law and the Comptroller have actually said.</p>
<!--fig:tefa-->
<p><b>The money.</b> Under {SRC['sb2']}, an account receives 85% of the statewide average state and local funding per student, up to $30,000 for a child with a disability, and up to $2,000 for a homeschooled student. Program spending for the biennium starting September 1, 2025 was capped at $1 billion. For 2026-27 that worked out to $10,474 for a private school student, per {SRC['cpa_dec']}. Families receive funds in installments; {SRC['tpsa']} lists October 1, 2026 and February 1, 2027 as the second and third payments.</p>
<p><b>Which schools qualify.</b> Section 29.358 requires a private school to show accreditation by an organization recognized by the Texas Private School Accreditation Commission or the Texas Education Agency, annual administration of a nationally norm-referenced test (or the state test) in grades 3 through 12, and continuous operation of a campus for at least the two school years before it applies. A new microschool in Magnolia that opened last fall isn’t eligible yet, whatever its quality.</p>
<p><b>What you can charge.</b> Section 29.365 says a participating school can’t charge a TEFA student more than its standard amount for the same service. There’s no separate tuition cap, and {SRC['tpsa']} notes that schools can bill families for the gap between the account and tuition or cover it with aid. Section 29.368 protects your admissions standards and religious character from state interference.</p>
<p><b>Who got funded in year one.</b> This is the part that should change your ad copy. More than 274,000 students applied, and when funding ran out, awards went by priority tier, per {SRC['ci_tefa']}.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Priority tier</th><th>Who it covered</th><th>Year-one result</th></tr></thead>
<tbody>
<tr><td>Tier 1</td><td>Students with a disability at or below 500% of the federal poverty line, plus eligible siblings</td><td>About 39% of participants</td></tr>
<tr><td>Tier 2</td><td>Students at or below 200% of the poverty line</td><td>About 60% of participants</td></tr>
<tr><td>Tier 3</td><td>Households between 200% and 500% of the poverty line</td><td>Fewer than 30 students as of July 29, 2026</td></tr>
<tr><td>Tier 4</td><td>Households above 500% of the poverty line</td><td>None accepted</td></tr>
</tbody></table></div>
<p>{SRC['cpa_aug']} counted more than 85,000 students confirmed for 2026-27 and more than 120,000 eligible applicants still waiting. Houston ISD had 3,327 participants and Fort Bend ISD 2,024, the two largest numbers in the Houston area in Community Impact’s list.</p>
<p>So the typical family touring a school off Research Forest Drive, earning well above 200% of the poverty line, didn’t get an account in year one. Ads that shout “Use your TEFA funds here!” to that audience set up a disappointment that lands on your admissions office. What we’d do instead:</p>
<ul>
<li>Build one plain TEFA page on your site: whether you participate, your accreditor, what the account covers against your tuition, how the gap is billed, and a link to the official program. Update it when 2027-28 details come out. The Texas Private School Association expects applications to open in late winter or spring 2027.</li>
<li>Target TEFA messaging where it fits. Schools serving families in Tier 1 and Tier 2 (including many parish schools and schools with strong learning-support programs) have a real story. Say it in English and Spanish; our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Spanish-language marketing guide')} has the details.</li>
<li>Never promise an award. The Comptroller decides eligibility and priority, not you.</li>
<li>Remember funded families don’t reapply each year; they file an intent to continue. Your re-enrollment packet should remind them.</li>
</ul>
<p>Our {L('/blog/tutoring-center-marketing-houston/', 'tutoring center post')} covers the provider side of TEFA for tutors, so we won’t repeat it here.</p>"""),

            ("How parents in Houston search for a private school", f"""<p>Parents search in a few distinct ways, and each one needs a different landing page.</p>
<ul>
<li><b>By place.</b> “Private schools in The Woodlands,” “private schools Spring TX,” “Catholic school Kingwood,” “private school near Grand Parkway and 249.” These are the bulk of searches and they pull heavily from Google Maps.</li>
<li><b>By type or philosophy.</b> “Montessori school Conroe,” “classical Christian school Tomball,” “IB school Houston,” “school for dyslexia Houston.” Low volume, high intent.</li>
<li><b>By money.</b> “Private school tuition Houston,” “private schools that accept TEFA,” “private school financial aid Texas.”</li>
<li><b>By name.</b> Your school’s name, and your competitors’. These searches mean a family is already comparing.</li>
</ul>
<p>Parents read a lot before they call. {SRC['gs_survey']} found 70% turn to official school websites and third-party sites like GreatSchools. In our experience one parent does the early research on a phone, and the second shows up at the tour asking about cost and outcomes.</p>"""),

            ("Google Ads for private school enrollment", f"""<p>Search ads are the closest thing to a sure bet in school marketing, because the parent has told you what they want. A practical setup for a K-12 school in The Woodlands:</p>
<ul>
<li><b>Area campaign.</b> “Private school the woodlands,” “private schools near me,” “private school spring tx,” “best private schools the woodlands.” Land on an admissions overview with dates, tuition range and a tour button.</li>
<li><b>Division campaigns.</b> Separate ad groups for early childhood, lower, middle and upper school, each with its own page. “Private preschool Woodlands” and “private high school Houston” are different parents.</li>
<li><b>Program campaigns.</b> Only for what you truly offer: Montessori, IB, learning differences, a STEM program, a faith tradition.</li>
<li><b>Brand.</b> Cheap, and it keeps a competitor or a directory from sitting above your own name during application season.</li>
</ul>
<p>Negatives to add on day one: jobs, careers, teacher, salary, employment, “public school,” ISD, charter, “free,” online, virtual (unless you run a virtual program), homeschool (unless you serve homeschoolers), college, university, and “calendar” searches from current families looking for the holiday schedule.</p>
<p>Set location to people in or regularly in your area, rather than people merely interested in it (see {SRC['gloc']}). Otherwise you pay for clicks from a grandparent in Ohio. A radius of 10 to 15 miles around campus usually covers a Woodlands school’s real draw, wider for boarding or specialty programs.</p>
<p>Sample ad for October:</p>
<p><i>Headline 1:</i> Private School in The Woodlands<br><i>Headline 2:</i> Open House Sat., Nov. 14<br><i>Headline 3:</i> PK3-12th Grade, Small Classes<br><i>Description:</i> Tour campus, meet teachers and see real classrooms. Applications for 2027-28 due Jan. 15. Book your visit online.</p>
<p>Budget, honestly: in local accounts we’ve run, a few thousand dollars a month from October through January is enough to learn what works for one campus. Measure it by cost per tour and cost per application, never by clicks. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a feel for click costs, and our {L('/services/search-marketing/', 'search marketing team')} builds these campaigns.</p>"""),

            ("Facebook and Instagram: reaching parents with fewer targeting tools", f"""<p>Meta reaches parents who aren’t searching yet, like the family in Creekside Park that’s mildly unhappy with middle school. It’s also gotten blunter to target.</p>
<p>Meta has been removing and consolidating detailed targeting for years, and the latest round took effect January 15, 2026, per {SRC['smt']}. Parent-based options still show up under Demographics in many accounts, but check Ads Manager before you plan around them. Separately, since February 2023 advertisers can target teens only by age and location, with gender and engagement-based targeting removed, per {SRC['teens']}. If your upper school wants to reach students directly, your creative has to do the work.</p>
<p>Meta also won’t approve ads that assert or imply personal attributes about the viewer. That trips up schools more than you’d think.</p>
<!--fig:copy-->
<p>What we see working for schools:</p>
<ul>
<li>Event ads for a specific open house or a “coffee and campus tour” morning, with date, time and a link to RSVP.</li>
<li>Short phone videos: a teacher explaining a project, a lower school morning meeting, the robotics team in the hallway. Polished brand videos rarely beat these.</li>
<li>Lead forms with two or three questions (grade for 2027-28, current school, best time to call). A form with zero questions gets you names, not families. Our post on {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'fixing low-quality Facebook leads')} covers the settings.</li>
<li>Retargeting everyone who viewed the tuition or admissions pages, with the next open house date.</li>
</ul>
<p>“Kindergarten tours in Spring, Wednesdays at 9” finds kindergarten parents in Spring without any interest targeting at all.</p>"""),

            ("Virtual tours and the pages that do the selling", f"""<p>A virtual tour won’t replace a campus visit, but it gets the second parent and the out-of-state relocator to agree to one. A three-minute walk-through led by a student, shot on a good phone, beats a ten-minute drone production.</p>
<!--fig:pages-->
<p>The page parents want most and schools resist most is tuition. Publish it. Families who can’t find a number assume it’s higher than it is, or they assume you’re hiding something. Put tuition by division, fees, what’s included, payment plans, and a clear line on financial aid right next to it. If you participate in TEFA, show the math on the same page.</p>
<p>The rest of the admissions section should answer the questions the admissions office hears on every call: key dates for this cycle, what the application requires by grade, testing, class sizes, before- and after-care, bus routes or carpool from Spring and Conroe, uniforms and lunch. Each division page should link to booking a tour. Our team builds these under {L('/services/web-design-seo-pr/', 'web design and SEO')}.</p>"""),

            ("Reviews, Niche and GreatSchools profiles", f"""<p>Before a family books a tour, they read what other parents say. That happens on three sites more than anywhere else.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform</th><th>What you control</th><th>What you don’t</th><th>Our take</th></tr></thead>
<tbody>
<tr><td>Google Business Profile</td><td>Hours, photos, events, categories, replies to reviews</td><td>Which reviews appear</td><td>The first thing most parents see for “private schools near me.” Ask for reviews.</td></tr>
<tr><td>GreatSchools</td><td>A free claimed profile covers contact details, About section, application info, programs, extracurriculars and review replies</td><td>Ratings and official data; you can flag reviews but not remove them</td><td>Claim it and fill it in. Enhanced Profiles add photos, video and an application link for a fee.</td></tr>
<tr><td>Niche</td><td>Paid Premium Profile adds your story, photos, video, events and inquiry delivery</td><td>Grades and family reviews</td><td>Worth testing for upper schools; judge it on tours and applications, not page views.</td></tr>
</tbody></table></div>
<p>The GreatSchools details come from {SRC['gs_help']}. {SRC['niche']} says Premium Profile inquiries can flow straight into Finalsite, Ravenna, Blackbaud or FACTS, which matters because a lead that sits in a separate inbox goes cold.</p>
<p>For Google reviews, the moments to ask are when a family is happiest: after the first-week welcome, after a strong parent-teacher conference, after a big event. A simple text from the division head works:</p>
<p><i>“Hi Jen, it was great seeing Ava at the science fair last night. If you have a minute, a quick Google review helps other families in The Woodlands find us: [link]. Thank you!”</i></p>
<p>Don’t offer a dress-down day, raffle entry or tuition credit for reviews. {SRC['gpol']} prohibits incentives for reviews. Reply to every review, briefly, and never discuss a specific student’s situation in a public reply. The {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} covers requests and replies in depth.</p>"""),

            ("Re-enrollment is your cheapest enrollment", f"""<p>A family that leaves after fifth grade costs you seven years of tuition. Re-enrollment contracts usually go out in January or February, right when admissions is busiest, so plan it like a campaign:</p>
<ul>
<li>Know your attrition by grade. Transition years (PK to K, 5th to 6th, 8th to 9th) are where families reconsider. If your sixth-grade class shrinks every year, that’s a middle school marketing problem aimed at your own fifth-grade parents.</li>
<li>Run a “next year in middle school” night for current families before contracts go out.</li>
<li>Communicate well all year. The same GreatSchools survey found 90% of parents who would recommend their school are satisfied with its communication, and parents unlikely to recommend their school were far more likely to say they’d missed a deadline or opportunity because of unclear communication.</li>
<li>Call every family that hasn’t returned a contract by the deadline. Admissions or the division head, not an email.</li>
</ul>"""),

            ("Financial aid and tuition messaging", f"""<p>Cost is the most common reason a family that loved the tour doesn’t apply. Say plainly that aid exists and how it works. Many Houston schools use a third-party platform for need-based aid; The John Cooper School, for example, uses Clarity, per its admission FAQ. Name your platform, give the aid deadline (usually close to the application deadline), and explain that applying for aid doesn’t affect admission decisions if that’s your policy.</p>
<p>If you publish an aid statistic, keep it current and be able to show your work. For TEFA-participating schools, a simple example on the tuition page (tuition minus the account amount equals the balance before aid) answers the math parents are doing in their heads.</p>"""),

            ("What to track, and a first 90 days", f"""<p>Your enrollment system already holds most of this data; the work is connecting it to sources. Give each channel a tracked phone number, tag every form with its source, and log open house sign-ins against existing inquiries. Our guide to {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking forms and calls in GA4 and Google Ads')} walks through the setup.</p>
<!--fig:plan-->
<p>The numbers worth a monthly look: inquiries by source, tour rate, application rate, acceptance yield, re-enrollment rate by grade, and marketing cost per enrolled student by channel. After one full cycle you’ll know which channels bring families who enroll and stay, which is the only answer that should move next year’s budget.</p>
<p>If you’d like a senior strategist to build an enrollment plan around your grades, your calendar and your seats, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do private schools in The Woodlands and Houston increase enrollment?",
             "Start with the funnel: reply to inquiries within hours, make tours bookable online, and follow up after every tour with answers about cost and admissions odds. Then fund the channels that bring tours, which for most schools means Google search ads during application season, open house promotion on Facebook and Instagram, a strong Google Business Profile, and claimed Niche and GreatSchools profiles. Protect re-enrollment, especially in transition grades."),
            ("When should a Houston private school start advertising for next year?",
             "For schools with December or January deadlines, the main push runs from October through mid-January, with open house dates published by September. Pre-K and kindergarten families often start the fall before, so those campaigns can start in September. Keep a smaller campaign running from April through July for families relocating to Houston for work, who often decide quickly and enroll for August."),
            ("Can private schools advertise that they accept Texas Education Freedom Accounts?",
             "Only if the school is approved to participate. Under SB 2, a school needs accreditation by an organization recognized by TEPSAC or TEA, annual norm-referenced testing in grades 3 to 12, and two school years of continuous operation. In 2026-27 the account was $10,474 for private school students, and awards went first to students with disabilities and lower-income families, so never promise a family an award."),
            ("Can I target parents with Facebook ads for a private school?",
             "Partly. Meta has removed many detailed targeting options, most recently on January 15, 2026, and parent options vary by account. Teens can only be targeted by age and location. Meta also rejects ads that imply personal attributes about the viewer. Location radius plus specific creative, such as a kindergarten open house date in Spring or The Woodlands, usually finds the right parents."),
            ("Should a private school pay for a Niche Premium Profile?",
             "It can be worth testing, especially for upper schools where families compare many options. Niche's Premium Profile adds your own story, photos, video, events and inquiry delivery into systems like Finalsite, Ravenna, Blackbaud and FACTS. Claim the free GreatSchools profile first, then run Niche for a full admissions cycle and judge it by tours and applications rather than profile views."),
        ],
        "figures": {
            "funnel": {
                "type": "funnel",
                "title": "Where a private school admissions funnel leaks",
                "stages": [["Inquiries", "300"], ["Tours", "120"], ["Applications", "75"], ["Acceptances", "55"], ["Enrolled", "40"]],
                "note": "Illustrative example for one admissions cycle",
                "alt": "Private school admissions funnel from inquiry to enrollment for a school in The Woodlands and Houston",
                "caption": "Inquiry to tour is the biggest drop in most funnels we see. Fix the follow-up before buying more inquiries.",
            },
            "season": {
                "type": "columns",
                "title": "When private school families shop",
                "sub": "Relative admissions activity by month for a school with a January deadline",
                "labels": ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                "values": [30, 50, 80, 100, 85, 90, 45, 40, 30, 30, 35, 35],
                "highlight": [2, 3, 4, 5],
                "y_label": "Activity",
                "note": "Illustrative example",
                "alt": "Monthly private school admissions demand in Houston and The Woodlands peaking October through January",
                "caption": "Heavy from October to the deadline, with a summer bump from families relocating to Houston.",
            },
            "tefa": {
                "type": "stats",
                "title": "Texas Education Freedom Accounts, year one",
                "stats": [["$10,474", "Private school account, 2026-27"], ["274K", "Students who applied"], ["85K+", "Confirmed participants by August 2026"], ["120K+", "Eligible applicants waitlisted"]],
                "note": "Sources: Texas Comptroller, Community Impact, 2025-2026",
                "alt": "Stats on Texas Education Freedom Accounts for private schools in Houston and The Woodlands",
                "caption": f"From {SRC['cpa_dec']} and {SRC['cpa_aug']}. Accounts for students with disabilities can reach $30,000.",
            },
            "copy": {
                "type": "compare",
                "title": "School ad copy Meta may reject vs. copy that runs",
                "left": {"title": "Implies who the viewer is", "items": ["Tired of your child’s public school?", "Single parent? We can help", "Is your son falling behind?", "Can’t afford private school?"]},
                "right": {"title": "Describes the school", "items": ["Small classes, PK3 through 12th grade", "Before- and after-care from 7 a.m.", "Learning support on every campus", "Financial aid and payment plans available"]},
                "alt": "Comparison of private school Facebook ad copy for The Woodlands and Houston under Meta’s personal attributes policy",
                "caption": "Describe your program and let parents recognize themselves.",
            },
            "pages": {
                "type": "checklist",
                "title": "Admissions pages every school site needs",
                "sub": "What Houston parents look for before they book a tour",
                "items": ["Tuition and fees by division", "Financial aid process and deadline", "Key dates for this admissions cycle", "Online tour booking", "Short student-led virtual tour", "Application steps and testing by grade", "TEFA participation and the math", "Carpool, bus and after-care details"],
                "alt": "Checklist of admissions website pages for a private school in The Woodlands and Houston",
                "caption": "If the admissions office answers it on every call, it belongs on the site.",
            },
            "plan": {
                "type": "steps",
                "title": "A first 90 days of enrollment marketing",
                "steps": [["Days 1-15", "Tracked numbers, form sources, tour booking online, open house dates published."], ["Days 15-30", "Claim GreatSchools and Niche, refresh Google Business Profile, start review requests."], ["Days 30-60", "Launch search campaigns by division and open house ads on Meta."], ["Days 60-90", "Tour follow-up sequence, retargeting, first funnel report by source."]],
                "alt": "Ninety-day private school enrollment marketing plan for schools in The Woodlands and Houston",
                "caption": "Start the plan at least 90 days before your application deadline.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: self storage
    {
        "slug": "self-storage-marketing-houston",
        "title": "Self Storage Marketing in Houston: How Independents Win Move-Ins",
        "seo_title": "Self Storage Marketing in Houston: Win More Move-Ins",
        "desc": "Self storage marketing for Houston operators: local SEO per facility, Google Ads, SpareFoot math, online rentals, pricing, storms, lien rules, boat storage.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google"],
        "art": "b3",
        "hero": "key",
        "hero_alt": "Illustration of a key for self storage marketing in Houston, The Woodlands and Conroe",
        "related": ["moving-company-marketing-houston", "rank-in-google-map-pack-houston", "multi-location-local-seo-houston-franchises"],
        "sections": [
            (None, f"""<p>Sunday, 9:15 p.m. A couple in an apartment off Kuykendahl closed on a house in Magnolia that won’t be ready for six weeks, and their lease ends Friday. One of them types “storage units near me” and gets four results. Two are national brands with prices, a “Rent Now” button and a 50%-off first month. One is your facility, where the website says “call for pricing” and the office closed at six. The fourth is a SpareFoot listing for your own facility.</p>
<p>They rent the 10x10 at the national brand before the kids are in bed.</p>
<p>Self storage marketing in Houston works when an independent operator matches the big REITs on the basics (prices online, rent online any hour, a solid Google Business Profile for every facility) and then wins on the things a national brand can’t fake: local answers, specific unit types, and people who pick up the phone. This guide covers how we’d do that, from Google Ads and aggregators to street rates, hurricanes, Texas lien notices and boat storage near Lake Conroe.</p>"""),

            ("What you’re up against: the REITs in Houston", f"""<p>The three big public operators you see on every Houston corner have advantages that would be silly to ignore.</p>
<p>Public Storage held interests in 3,171 facilities at the end of 2025, and nearly three quarters of its new rentals were completed through its eRental and Rent by Phone process that year, per {SRC['psa']}. Extra Space became the largest operator in the industry when it completed its merger with Life Storage on July 20, 2023, creating more than 3,500 stores, per {SRC['exr']}. CubeSmart rounds out the trio. All three run revenue management software that adjusts street rates constantly, and they buy brand search and generic search across the whole metro.</p>
<!--fig:edge-->
<p>Where independents win is everything local. A REIT facility page is a template. Yours can say the gate code works until 10 p.m., the climate-controlled building has a loading dock that fits a 26-foot truck, you have 12-foot-wide drive-up units for a bass boat, and Danny in the office will hold a unit until Saturday if you call. Those details win searches like “boat storage near Lake Conroe” and they win the comparison once a renter is looking at three tabs.</p>"""),

            ("The Houston storage market right now", f"""<p>Houston is one of the most supplied storage markets in the country, which means you’re competing on visibility and price, not on a shortage.</p>
<!--fig:market-->
<p>{SRC['sc_hou']} counted 405 facilities and about 28.5 million rentable square feet in Houston as of October 2026, or 6.9 square feet per person. Its average street rate for a 10x10 was $97 a month non-climate and $119 climate-controlled. The {SRC['rc_june']} forecast about 789,519 square feet of new Houston supply for 2026, roughly 3% of existing stock, and put the national average street rate across all unit sizes at $135, down 1.5% from a year earlier.</p>
<p>Demand has a structural tailwind here. {SRC['sc_apts']} found Houston built more apartments than any other U.S. city from 1985 through 2024 (240,659 units), and apartments built since 2015 average 44 square feet smaller. Smaller apartments, more moves and long commutes from The Woodlands, Katy and Cypress all mean more stuff that needs a home.</p>
<p>In practice, a new facility opening a mile away can change your occupancy faster than any marketing campaign, so watch construction permits and rate changes around your site at least monthly.</p>"""),

            ("Demand drivers: moves, storms and renovations", f"""<p>Storage demand in Houston follows life events more than seasons, though the seasons are real.</p>
<!--fig:season-->
<ul>
<li><b>Moves.</b> Summer is peak, from late May through August, with spikes at month-end when leases turn over. Closings with a gap between houses are the classic 10x15 rental. Partner with movers and apartment communities; our {L('/blog/moving-company-marketing-houston/', 'moving company marketing post')} is written from the mover’s side of that relationship.</li>
<li><b>Storms.</b> After a flood or a roof full of tree limbs, families need somewhere dry for furniture while contractors work. The big operators move fast: U-Haul offered 30 days of free self-storage to affected Houston residents {SRC['uhaul_may']} and {SRC['uhaul_beryl']} in July 2024. Decide your storm offer before June, not during the outage.</li>
<li><b>Renovations and foundation work.</b> Kitchen remodels, flooring jobs and foundation repairs on Houston’s clay soil all empty rooms for weeks. Remodelers and flooring companies make good referral partners.</li>
<li><b>Downsizing, estates and divorce.</b> Steady year-round, longer stays, and the renters most likely to want a human on the phone.</li>
<li><b>Business storage.</b> Contractors, pharma reps and e-commerce sellers who want inventory near I-45 or the Grand Parkway. They care about access hours and deliveries.</li>
</ul>
<p>Write a short storm playbook now: a pre-written Google Business Profile post, an ad that can go live within hours, a landing page for displaced homeowners, and a rule for how long your office stays open after a storm. Our {L('/blog/seasonal-marketing-greater-houston/', 'seasonal marketing guide for Greater Houston')} covers how to plan around the calendar.</p>"""),

            ("Google Business Profile and local SEO for each facility", f"""<p>Most storage rentals start in Google Maps. Each facility needs its own profile, its own page on your website, and its own reviews.</p>
<!--fig:profile-->
<p>Use your real business name exactly as it appears on your signage. {SRC['gbp']} don’t allow keyword stuffing in the business name, so “Main Street Storage” can’t become “Main Street Storage Climate Controlled Boat RV Conroe TX.” Pick “Self-storage facility” as the primary category and add secondary categories only where they’re true (boat storage facility, RV storage facility). Post office hours clearly and explain gate access hours in the description or with whatever additional-hours options your category offers, because “Is it open now?” is a common reason renters skip a listing.</p>
<p>Photos matter more than operators think. Show the gate, the hallways, a 10x10 with the door up, the loading area, the cameras and the drive aisles wide enough for a truck. A renter who’s about to drive a box truck through your gate wants to see the turn.</p>
<p>On the website, give each facility a page with unit sizes and live prices, features, gate and office hours, a map, directions from the nearest landmarks (Hughes Landing, Market Street, the FM 1488 and I-45 interchange), and its own reviews. The REIT pages are thin, and a facility page with real local detail can outrank them for “storage units in Spring TX” or “storage near Woodforest.” Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} explains the ranking factors, and {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO')} covers running several facilities without the profiles cannibalizing each other.</p>"""),

            ("SpareFoot and the aggregators: do the math", f"""<p>Aggregators like SpareFoot put your units in front of renters who are comparison shopping, and they charge you for it. The pricing is clearer than most operators realize.</p>
<p>Under SpareFoot’s OneTime pricing, the move-in fee is your bid multiplied by the unit’s price, so a $100 unit with a bid of 2 costs $200 per move-in, per {SRC['sf_one']}. If your move-in rate (reservations that actually move in) falls below the network average of 50%, an extra fee can apply. Under {SRC['sf_rent']}, you instead pay a monthly percentage of rent for as long as the tenant stays, with the percentage set by your account.</p>
<!--fig:cpmi-->
<p>Three things to check before you decide:</p>
<ul>
<li>How many of your aggregator move-ins would have found you anyway, through your own Google profile or brand search? Ask every new tenant how they found you and record it in your management software.</li>
<li>Your average length of stay. A RentPercent arrangement on a tenant who stays two years costs far more than a one-time fee.</li>
<li>Which units you list. Aggregators are useful for filling hard-to-rent sizes and new facilities in lease-up. They’re expensive for units that rent themselves.</li>
</ul>
<p>We’re not against aggregators. We’re against paying a marketplace for move-ins your own listing would have won.</p>"""),

            ("Online rentals and move-ins at any hour", f"""<p>When a REIT completes most new rentals through an online and phone process, renters learn to expect it everywhere. If your website only takes reservations, or worse, only takes phone calls, you’re losing the 9 p.m. renter.</p>
<p>Most current management software (SiteLink and storEDGE among them) offers an online rental flow that collects ID, signs the lease and takes payment. Turn it on, put the “Rent Now” button next to every price, and test it on your own phone from a parking lot. Count the taps.</p>
<p>A few details that move the needle:</p>
<ul>
<li>A size guide with photos of real furniture in real units. “A 10x10 fits a two-bedroom apartment” is the most useful sentence on a storage site.</li>
<li>Reservation follow-up. Someone who reserves and doesn’t show should get a text that afternoon and a call the next morning. Abandoned online rentals deserve the same.</li>
<li>Call answering. Route after-hours calls to a call center or a staffed line that can rent a unit, not a voicemail box.</li>
<li>Track calls and online rentals by source so you can tie them back to Google Ads and your profile. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers setup.</li>
</ul>"""),

            ("Pricing, street rates and promotions", f"""<p>Price is visible, and renters compare it in seconds. You don’t have to be cheapest, but you have to be clear.</p>
<ul>
<li><b>Show street rates on the site.</b> “Call for pricing” loses to a number almost every time.</li>
<li><b>Show the real cost of moving in.</b> If there’s an admin fee, required lock or required insurance, list it next to the rate. Surprises at the counter turn into one-star reviews.</li>
<li><b>Promotions should be specific and short.</b> “First month $1 on 10x10 climate units at our Spring location through November 30” beats a permanent “specials available.” If the promo applies only to certain sizes, say so on the unit row.</li>
<li><b>Rate increases on existing tenants</b> are a normal part of the business. Give notice the way your lease requires, explain it plainly, and expect some reviews to mention it. Reply calmly.</li>
</ul>
<p>Watch the three or four facilities your renters actually compare you with, by unit type. A weekly check of their 10x10 and 10x20 rates is usually enough for an independent operator.</p>"""),

            ("Google Ads for self storage in Houston", f"""<p>Search ads catch renters at the moment they decide. Structure by facility and by unit type.</p>
<ul>
<li><b>Facility campaigns.</b> “Storage units [town],” “self storage near [landmark],” “storage units near me,” with a radius of roughly three to five miles around each facility. Land on that facility’s page.</li>
<li><b>Unit-type ad groups.</b> Climate-controlled storage, drive-up units, boat storage, RV storage, business or wine storage. Each to a page or a filtered view of those units.</li>
<li><b>Brand.</b> Your name, so aggregators and competitors don’t sit above you.</li>
</ul>
<p>Negatives: storage containers for sale, shed, sheds, bins, totes, cabinets, furniture, “storage auction” (unless you want auction buyers), jobs, careers, manager, cloud storage, iCloud, data, Amazon, PODS (unless you rent portable containers), “free storage” and “cheap storage boxes.” Check your search terms weekly for the first month.</p>
<p>Use presence-based location targeting, so you’re paying for people in or regularly in your area rather than those merely interested in it, per {SRC['gloc']}. The exception is relocation: someone moving to The Woodlands from Dallas may search from Dallas, so a small separate campaign for “storage units The Woodlands TX” with interest targeting can make sense.</p>
<p>Sample ad:</p>
<p><i>Headline 1:</i> Storage Units in Spring, TX<br><i>Headline 2:</i> Climate-Controlled From [your price]<br><i>Headline 3:</i> Rent Online in 5 Minutes<br><i>Description:</i> Gate open 6 a.m. to 10 p.m., cameras throughout, truck-friendly drive aisles. Near I-45 and FM 2920. See sizes and rent online.</p>
<p>Spend: in accounts we’ve run, a single facility can learn a lot on a modest budget because storage searches are tightly local. Set the budget from a target cost per move-in, then compare it against your average tenant value. Be careful with Performance Max for a single facility; we explain why in {L('/blog/performance-max-vs-search-campaigns-local/', 'Performance Max vs. Search for local businesses')}. Our {L('/services/search-marketing/', 'search marketing team')} runs these accounts.</p>"""),

            ("Texas lien notices, auctions and your reputation", f"""<p>Lien sales aren’t marketing, but they show up in your reviews, so they belong in this conversation. This is a summary for marketers, not legal advice; your attorney and your state association should sign off on your process.</p>
<!--fig:lien-->
<p>Under {SRC['lien']}, a lessor’s notice to a delinquent tenant has to include an itemized account of the claim, the lessor’s name, address and phone number, a statement that the contents have been seized under the contractual landlord’s lien, a warning that if the claim isn’t paid within 14 days the property may be sold at public auction (or a vehicle towed under the Occupations Code), and a notice in bold or underlined type asking tenants in military service to report that status immediately. The notice can be delivered in person, by verified mail or by email. Email delivery is allowed only if the rental agreement includes a conspicuous, underlined or bold statement that the tenant may receive notice by email.</p>
<p>That email clause has a marketing side. Collect a working email and mobile number at move-in, make sure your lease language is current, and use the same contact info for autopay reminders and rate-change notices. Tenants who get a friendly payment reminder before day five are much less likely to end up in a lien process and much less likely to write an angry review about one. The rules for advertising the sale itself are in Section 59.044, and the Legislature has considered changes to them recently, so confirm the current version with counsel before your next auction.</p>
<p>When a lien-related review does appear, reply briefly, don’t share account details, and offer an office phone number. Future renters read those replies.</p>"""),

            ("Boat and RV storage near Lake Conroe", f"""<p>Lake Conroe covers 20,118 acres across Montgomery and Walker counties, per {SRC['tpwd']}, and the boats on it have to live somewhere the rest of the year. Many neighborhoods around The Woodlands, Montgomery and Conroe have deed restrictions that keep boats and RVs out of driveways, and in our experience that comes up in almost every boat storage inquiry.</p>
<p>Boat and RV storage is a different customer from household storage. These renters stay longer, care more about covered spaces, security, wash-down areas, dump stations and easy access to FM 1097, SH 105 and the boat ramps, and they’ll drive farther for the right setup.</p>
<ul>
<li>Run a separate ad group for “boat storage Lake Conroe,” “covered boat storage Montgomery TX,” “RV storage Conroe” and “RV storage near me,” landing on a page that lists space lengths, heights and pricing.</li>
<li>Photograph the actual spaces with a boat or trailer in them, plus the turn into the lot.</li>
<li>If you have a waitlist, put a waitlist form on the page and promote it. Covered spaces can fill up by spring, so start your marketing before boating season ramps up.</li>
<li>Partner with marinas, boat dealers and RV service shops in Montgomery County for referrals.</li>
</ul>"""),

            ("Reviews that win the comparison", f"""<p>When a renter has three facilities open in three tabs, review count and recency often decide it. The REITs have volume. You can have warmth and specifics.</p>
<p>Ask at two moments: right after move-in (“Was everything easy today?”) and around 60 days in. A text from the manager works:</p>
<p><i>“Hi Marcus, thanks for choosing us for your move. If the unit and the gate have worked well for you, a quick Google review helps other folks in Conroe find us: [link]. Thanks, Danny”</i></p>
<p>Don’t offer a discount, free month or lock for reviews; {SRC['gpol']} prohibits incentives. Reply to every review, mention the facility and the feature they praised, and keep replies short. More detail is in the {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')}.</p>"""),

            ("Occupancy, cost per move-in and what to track", f"""<p>Storage marketing has an unusually clean scoreboard. Your management software already knows almost everything; you just have to tie it to sources.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>What it tells you</th><th>Where it lives</th></tr></thead>
<tbody>
<tr><td>Physical and economic occupancy by unit type</td><td>Which sizes to promote and which to price up</td><td>Management software</td></tr>
<tr><td>Move-ins and move-outs by month</td><td>Net rental activity, seasonality</td><td>Management software</td></tr>
<tr><td>Move-ins by source</td><td>Which channels actually produce tenants</td><td>Software “how did you hear” field, call tracking, online rental tags</td></tr>
<tr><td>Cost per move-in by channel</td><td>Google Ads vs. aggregators vs. everything else</td><td>Ad spend divided by attributed move-ins</td></tr>
<tr><td>Reservation-to-move-in rate</td><td>Follow-up quality, aggregator fee exposure</td><td>Software, SpareFoot dashboard</td></tr>
<tr><td>Average length of stay</td><td>What a tenant is worth, and how much you can pay for one</td><td>Management software</td></tr>
</tbody></table></div>
<p>The first 30 days we’d spend on basics: fix every facility’s Google Business Profile, put live prices and online rentals on each facility page, set up call tracking, and fill in the “how did you hear about us” field on every move-in. Days 30 to 60, launch search campaigns per facility with the negatives above and start review requests. Days 60 to 90, compare cost per move-in by channel, then trim aggregator listings to the unit types that need help and set your storm playbook before next June.</p>
<p>If you run one facility or a dozen across Houston and Montgomery County and want a senior strategist to build a plan around your occupancy, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I get more customers for my self storage facility in Houston?",
             "Make it easy to choose you online. Give every facility its own Google Business Profile and website page with live prices, photos and gate hours, turn on online rentals so people can rent at night, and ask new tenants for reviews. Then run Google search ads by facility and unit type with strong negatives, and use aggregators like SpareFoot only where they bring move-ins you wouldn't get anyway."),
            ("Is SpareFoot worth it for a self storage facility?",
             "It can be, especially in lease-up or for hard-to-rent sizes. Under SpareFoot's OneTime pricing you pay your bid times the unit price per move-in, so a $100 unit with a bid of 2 costs $200, with an extra fee possible if your move-in rate falls below 50%. RentPercent pricing charges a monthly share of rent for the whole stay. Compare against your own Google cost per move-in."),
            ("What keywords should self storage Google Ads target?",
             "Target local, high-intent searches: storage units plus your town or a nearby landmark, storage units near me, climate controlled storage, drive up storage, and boat or RV storage if you offer it. Add negatives like storage containers for sale, sheds, bins, jobs, cloud storage, iCloud and Amazon. Use presence-based location targeting with a tight radius around each facility in Houston or The Woodlands."),
            ("What notice does Texas law require before a storage lien sale?",
             "Texas Property Code Section 59.043 requires an itemized claim, the lessor's contact details, a statement that contents were seized under the contractual landlord's lien, a 14-day warning that property may be sold at auction or a vehicle towed, and a bold or underlined military-service notice. Delivery can be in person, by verified mail, or by email if the lease has a conspicuous email clause. Confirm details with an attorney."),
            ("How do I market boat and RV storage near Lake Conroe?",
             "Treat it as its own business. Build a page with space lengths, heights, covered versus open pricing and photos of real boats in the spaces, then run a separate ad group for searches like boat storage Lake Conroe and RV storage Conroe. Promote a waitlist before spring, and build referral relationships with marinas, boat dealers and RV service shops in Montgomery County."),
        ],
        "figures": {
            "edge": {
                "type": "compare",
                "title": "Where a REIT is strong vs. where an independent can win",
                "left": {"title": "National REIT strengths", "items": ["Brand recognition and big search budgets", "Revenue management on every rate", "Rent online at any hour", "Huge review counts"]},
                "right": {"title": "Independent operator edge", "items": ["Facility pages with real local detail", "Boat, RV and oversized units", "A person who answers the phone", "Flexible holds and move-in help", "Warmer, specific reviews"]},
                "alt": "Comparison of REIT and independent self storage marketing strengths in Houston and The Woodlands",
                "caption": "Match the left column’s basics, then compete on the right.",
            },
            "market": {
                "type": "stats",
                "title": "Houston self storage at a glance",
                "stats": [["405", "Facilities in Houston"], ["6.9", "Square feet of storage per person"], ["$97", "Average 10x10 non-climate street rate"], ["$119", "Average 10x10 climate-controlled rate"]],
                "note": "Source: StorageCafe, October 2026",
                "alt": "Houston self storage market statistics including facility count and 10x10 street rates",
                "caption": f"From {SRC['sc_hou']}. Rates move monthly; check your own competitors weekly.",
            },
            "season": {
                "type": "columns",
                "title": "When Houston storage demand peaks",
                "sub": "Relative rental activity by month at a typical household-storage facility",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [45, 50, 60, 70, 85, 100, 100, 90, 70, 60, 50, 40],
                "highlight": [4, 5, 6, 7],
                "y_label": "Rentals",
                "note": "Illustrative example. Storm events can add sharp spikes in any month of hurricane season.",
                "alt": "Monthly self storage rental demand in Houston and The Woodlands peaking in summer moving season",
                "caption": "Summer moves set the baseline. Storms, closings and renovations add the spikes.",
            },
            "profile": {
                "type": "checklist",
                "title": "Every facility’s Google profile and page",
                "sub": "The basics that win local storage searches in Houston",
                "items": ["Real business name, no keywords", "Self-storage facility as primary category", "Office hours and gate access hours", "Photos of gate, hallways and units", "Unit sizes with live prices online", "Rent Now button next to every price", "Directions from local landmarks", "Recent reviews with replies"],
                "alt": "Checklist for self storage Google Business Profile and local SEO for facilities in Houston and The Woodlands",
                "caption": "One profile and one page per facility, each with its own details.",
            },
            "cpmi": {
                "type": "bars",
                "title": "What one move-in can cost by channel",
                "sub": "A $120-a-month unit, compared",
                "items": [["Google Business Profile and SEO", 40, "$40"], ["Google search ads", 110, "$110"], ["Aggregator, OneTime bid of 2", 240, "$240"], ["Aggregator, 25% of rent for 12 months", 360, "$360"]],
                "highlight": [0],
                "note": "Illustrative example. Your numbers depend on bids, rates and length of stay.",
                "alt": "Bar chart comparing self storage cost per move-in by marketing channel for a Houston facility",
                "caption": "Aggregator fees scale with unit price and stay length. Know yours before you raise a bid.",
            },
            "lien": {
                "type": "steps",
                "title": "What a Texas lien notice must contain",
                "sub": "Summary of Property Code Section 59.043, not legal advice",
                "steps": [["Itemized claim", "An itemized account of what the tenant owes."], ["Lessor contact", "Name, address and phone of the lessor or agent."], ["Lien statement", "Contents seized under the contractual landlord’s lien."], ["14-day warning", "Unpaid claims may lead to public auction or a vehicle tow."], ["Military notice", "Bold or underlined request to report military service."], ["Proper delivery", "In person, verified mail, or email with a lease clause."]],
                "alt": "Steps in a Texas self storage lien notice under Property Code chapter 59 for Houston facilities",
                "caption": f"From {SRC['lien']}. Confirm your process with an attorney.",
            },
        },
    },
]
