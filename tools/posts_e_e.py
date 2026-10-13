"""Two posts for non-medical home care / senior care agencies: a referral-source playbook ("how do home care agencies
get clients") and a local SEO guide ("home care seo").

Research: U.S. Census QuickFacts V2025 for Montgomery County (population base, growth, 65+ share), Community Impact's
list of ten hospitals in The Woodlands area, Texas HHSC HCSSA licensing page (license categories), Texas Health &
Safety Code 142.001 and 142.002 (license required for personal assistance services), Texas Occupations Code 102.001
(paid patient solicitation), 42 CFR 482.43(d) discharge-planning lists and patient choice (read via a CFR mirror),
H-GAC Area Agency on Aging provider page, AARP 2024 Home and Community Preferences release, AARP/NAC Caregiving in the
U.S. 2025 release, BLS Occupational Outlook for home health and personal care aides, CareScout 2025 Cost of Care
national and Texas releases, Google Business Profile guidelines, chat retirement notice, review content policy,
Search Console Performance report help, a Local Search Forum thread with Sterling Sky and Joy Hawkins on home care
categories, HHSC Community First Choice page. Competitors read: CareAcademy, HHAeXchange, AxisCare, ShiftCare, Ad Firm.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "census": A("https://www.census.gov/quickfacts/fact/table/montgomerycountytexas/AGE775224", "Census Bureau QuickFacts"),
    "ci": A("https://communityimpact.com/houston/the-woodlands/health-care/2023/06/16/learn-about-10-hospitals-in-the-woodlands-area", "Community Impact"),
    "hhsc": A("https://hhs.texas.gov/node/2724", "Texas HHSC’s HCSSA licensing page"),
    "hsc142": A("https://texas.public.law/statutes/tex._health_and_safety_code_section_142.002", "Health and Safety Code §142.002"),
    "hsc142def": A("https://texas.public.law/statutes/tex._health_and_safety_code_section_142.001", "§142.001"),
    "occ102": A("https://texas.public.law/statutes/tex._occ._code_section_102.001", "Texas Occupations Code §102.001"),
    "cfr": A("https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-482/subpart-C/section-482.43", "42 CFR 482.43"),
    "hgac": A("https://www.h-gac.com/area-agency-on-aging/senior-service-providers", "H-GAC’s Area Agency on Aging"),
    "aarp24": A("https://www.aarp.org/press/releases/2024-12-10-new-aarp-report-majority-adults-50-plus-age-place-policies-communities-catch-up.html", "AARP’s 2024 Home and Community Preferences survey"),
    "aarp25": A("https://www.aarp.org/press/releases/2025-07-24-new-report-reveals-crisis-point-for-americas-63-million-family-caregivers.html", "AARP and the National Alliance for Caregiving"),
    "bls": A("https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm", "Bureau of Labor Statistics"),
    "cs": A("https://investor.genworth.com/news-events/press-releases/detail/1054", "CareScout’s 2025 Cost of Care Survey"),
    "cstx": A("https://www.businesswire.com/news/home/20260302888783/en/", "CareScout’s Texas release"),
    "gbp": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s Business Profile guidelines"),
    "chat": A("https://support.google.com/business/answer/14919062", "Google removed chat from Business Profiles"),
    "lsf": A("https://localsearchforum.com/threads/correcting-categories-interesting-corner-case.53662/latest", "a Local Search Forum thread"),
    "rev": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s review content policy"),
    "gsc": A("https://support.google.com/webmasters/answer/7576553?hl=en", "Performance report"),
    "cfc": A("https://www.hhs.texas.gov/node/42501", "Community First Choice"),
}

SIB1 = "/blog/how-do-home-care-agencies-get-clients/"
SIB2 = "/blog/home-care-seo-the-woodlands-houston/"

POST1 = {
    "slug": "how-do-home-care-agencies-get-clients",
    "title": "How Do Home Care Agencies Get Clients? A Houston Referral Playbook",
    "seo_title": "How Do Home Care Agencies Get Clients? Referral Playbook",
    "desc": "How do home care agencies get clients in The Woodlands and Houston? The referral sources, outreach cadence and tracking that fill caregiver schedules.",
    "category": "Strategy",
    "icons": ["Google Business Profile", "Google Ads", "LinkedIn"],
    "art": "b3",
    "hero": "care",
    "hero_alt": "Illustration of in-home senior care for a guide on how home care agencies get clients in The Woodlands and Houston",
    "related": ["medical-practice-marketing-houston", "complete-guide-google-reviews", "call-tracking-which-ads-make-phone-ring"],
    "sections": [
        (None, f"""<p>How do home care agencies get clients? Mostly through the people who meet a family on its worst week: hospital discharge planners and case managers, skilled nursing and rehab staff, senior living directors, elder-law attorneys, geriatric care managers and physicians’ offices. The rest come from adult children searching Google, usually at night, right after a fall or a worrying phone call with Mom.</p>
<p>The agencies that grow steadily work both channels on a fixed schedule, and they track every referral until it becomes a signed client or a clear no.</p>
<p>Say you own a licensed personal assistance agency in Conroe with 25 caregivers and room for 400 more weekly hours. You need about 30 referral contacts, a calendar that puts you in front of each one at the right rhythm, and a phone that answers when a case manager calls at 4:40 on a Friday.</p>"""),

        ("How do home care agencies get clients around The Woodlands?", f"""<p>Start with the local math, because it decides where you spend your week.</p>
{SRC['census']} puts 14.9% of Montgomery County residents at 65 or older. In a county of more than three-quarters of a million people, that’s well over 110,000 older adults within a short drive of The Woodlands, and the county is still adding rooftops. Most of them want to stay put: {SRC['aarp24']} found 75% of adults 50 and older want to keep living in their current homes as they age.</p>
<!--fig:market-->
<p>The referral side is concentrated too. {SRC['ci']} counted ten hospitals in The Woodlands area, including Memorial Hermann The Woodlands Medical Center, St. Luke’s Health-The Woodlands Hospital, Houston Methodist The Woodlands Hospital and the HCA Houston Healthcare campuses in Conroe and Tomball. Each one sends older patients home every day, many of them weaker than when they arrived and living with a spouse who can’t lift them.</p>
<p>That gives you two jobs: become the agency those hospitals’ professionals trust with a same-week start, and be easy to find and call for the daughter in Spring who has 48 hours to sort out Dad’s discharge.</p>
<p>One more local resource worth knowing: {SRC['hgac']} covers Montgomery and 11 other counties around Houston, while Harris County has its own Area Agency on Aging. Their benefits counselors and care coordinators talk to families constantly. Know them, even though they won’t steer families to one private agency.</p>"""),

        ("Home care referral sources: who sends clients and what they need", f"""<p>Every referral source asks a different question. A case manager wants a start tomorrow. An attorney wants an agency that won’t embarrass her. Here’s how we map them.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Referral source</th><th>Who to ask for</th><th>What they need from you</th><th>How fast it pays off</th></tr></thead>
<tbody>
<tr><td>Hospital case management</td><td>Case managers, social workers, discharge planners</td><td>Next-day starts, a direct after-hours line, proof of license and insurance</td><td>Slow to earn, steady once trusted</td></tr>
<tr><td>Skilled nursing and inpatient rehab</td><td>Social services director, discharge coordinator</td><td>A caregiver in the home on discharge day, follow-through on the therapy plan</td><td>Medium</td></tr>
<tr><td>Senior living (independent and assisted)</td><td>Executive director, resident services, wellness nurse</td><td>Caregivers who follow community rules, short add-on shifts, quick fill-ins</td><td>Fast, because clients are already nearby</td></tr>
<tr><td>Elder-law and estate attorneys</td><td>Attorney and lead paralegal</td><td>Clear rates, clean documentation, familiarity with VA and Medicaid paperwork</td><td>Slow, high value</td></tr>
<tr><td>Geriatric care managers</td><td>Owner or lead care manager</td><td>Consistent caregivers, honest updates, good matching</td><td>Medium, very loyal</td></tr>
<tr><td>Physicians’ offices</td><td>Office manager, nurse or MA</td><td>A one-page explainer and an easy referral form</td><td>Slow</td></tr>
<tr><td>Home health and hospice agencies</td><td>Intake coordinator, community liaison</td><td>Non-medical hours around their skilled visits</td><td>Fast</td></tr>
<tr><td>Past clients and their families</td><td>The adult child who hired you</td><td>Being asked, and being thanked</td><td>Fast</td></tr>
</tbody></table></div>
<p>When you’re small, start with senior living and home health agencies. They pay off fastest and keep caregivers busy while hospital relationships slowly build.</p>"""),

        ("Hospital discharge planners and case managers", f"""<p>This is the source most owners chase first and the one that takes longest to earn. Federal rules explain part of why. Under {SRC['cfr']}, a hospital discharging a Medicare patient to home health or a skilled nursing facility has to give the patient a list of available providers and “must not specify or otherwise limit” the choice. Private-pay non-medical agencies aren’t on that required list, but most case management teams keep a resource sheet of agencies they’ve found reliable. Your goal is to get on that sheet and stay near the top.</p>
<p>What gets you there is rarely a brochure. It’s answering the phone on a Friday afternoon, getting a caregiver to a house in Magnolia by Saturday morning, and calling the case manager back to say it happened.</p>
<!--fig:visit-->
<p>A few practical notes for the hospitals around The Woodlands and Conroe:</p>
<ul><li><b>Register before you visit.</b> Most health systems require vendor check-in. Call case management and ask how they handle outside agencies.</li>
<li><b>Bring the boring proof.</b> Your HCSSA license, liability coverage, how you screen and train caregivers, and your real minimum shift. Case managers are protecting their patients and their own credibility.</li>
<li><b>Know your limits out loud.</b> If your license covers personal assistance services only, say so. Planners remember the agency that said “that’s skilled care, call a home health agency” and pointed them to one.</li>
<li><b>Mind privacy.</b> Updates about a patient need the family’s permission. Our {'<a href="/blog/medical-practice-marketing-houston/">medical practice marketing guide</a>'} covers HIPAA and tracking in detail; if your agency bills Medicaid or another payer electronically, have counsel confirm where HIPAA applies to you.</li></ul>"""),

        ("Skilled nursing, rehab and senior living communities", f"""<p>A two-week rehab stay after a hip replacement ends with a discharge meeting. The social services director in that meeting is deciding whether the patient can safely go home, and a reliable agency can tip the answer toward yes. That makes skilled nursing and inpatient rehab one of the best home care referral sources in Montgomery County, especially for agencies that can start the same day the patient leaves.</p>
<p>Senior living is the fastest win for most agencies. Independent living residents often need a few hours of help a week, and assisted living residents sometimes need more one-on-one time than the community’s staff can give. The executive director wants an outside agency that:</p>
<ul><li>Checks in at the front desk, wears ID and follows the community’s rules.</li>
<li>Can cover a four-hour shift on short notice.</li>
<li>Never poaches residents toward moving out.</li>
<li>Tells the community’s wellness nurse when something changes, with the family’s permission.</li></ul>
<p>Pick three or four communities within 15 minutes of your office and become the agency their staff knows by name. Offer a short family session on fall prevention, with no pitch.</p>
<p>Home health and hospice agencies are the other quick source. Their nurses visit for an hour; the family still needs someone for the other 23. An intake coordinator who knows you can fill non-medical hours will call you often.</p>"""),

        ("Elder-law attorneys, care managers and physicians", f"""<p>These three take longer to build, but a single good relationship can send you clients for years.</p>
<h3>Elder-law and estate attorneys</h3>
<p>Attorneys in The Woodlands and Conroe handle guardianships, trusts, powers of attorney, Medicaid planning and VA benefits. Their clients often need care right now while the paperwork catches up. The National Academy of Elder Law Attorneys has a member directory, which is a good place to build your list. What attorneys want: clear rates in writing, caregiver timesheets that would hold up if anyone asked, and an agency that understands what a VA pension application or long-term care insurance claim needs.</p>
<h3>Geriatric care managers</h3>
<p>Aging life care professionals (the Aging Life Care Association is their professional group) are hired by families to manage everything. They’re demanding, they check your work and they’re fiercely loyal to agencies that keep the same caregiver on a case. Ask one what agencies get wrong. Then don’t do that.</p>
<h3>Physicians’ offices</h3>
<p>Geriatricians, primary care, neurology and cardiology offices see the decline first. The doctor rarely has time for you; the office manager and the nurse do. Leave a one-page sheet that explains what non-medical home care covers, what it doesn’t, how to refer and how fast you can start. Come back every month or two with something useful.</p>"""),

        ("How to get more clients for my home care business online", f"""<p>The other half of your clients never come through a professional. They come from an adult child who searches “home care near me” or “in-home care for elderly parents Spring TX” and calls the first two agencies that look trustworthy.</p>
<p>That person is busy. {SRC['aarp25']} counted 63 million family caregivers in the U.S. in 2025, six in ten of them employed, and nearly one in four providing 40 or more hours of care a week. They are not reading your mission statement. They want to know:</p>
<ul><li>Do you serve my parent’s town, and can you start this week?</li>
<li>What does it cost per hour, and what’s the minimum shift?</li>
<li>Are you licensed by the state, and are caregivers background-checked and trained?</li>
<li>Will a person answer if I call right now?</li></ul>
<p>Put those answers on your homepage and every town page. Then make the phone fast. If a call at 8:30 p.m. goes to voicemail, that family calls the next agency, and the Google ad or referral that produced the call was wasted. We track this with {'<a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking</a>'} for exactly that reason.</p>
<p>Search is the bigger lever over time, and we wrote a separate guide on <a href="{SIB2}">home care SEO in The Woodlands and Houston</a> covering Google Business Profile categories, service-area rules and one page per community. For paid search, start small: brand terms, “home care” plus your towns, and “in home care near me,” with ads scheduled for when someone actually answers. Health-related advertising has extra restrictions on audiences and remarketing; our {'<a href="/blog/medical-practice-marketing-houston/">medical practice post</a>'} explains Google’s rules, and our {'<a href="/services/search-marketing/">Google Ads team</a>'} can check whether they apply to your campaigns.</p>"""),

        ("Marketing plan for home care agency: the monthly outreach cadence", f"""<p>A marketing plan for a home care agency is mostly a calendar. Split your referral list into tiers and give each tier a rhythm you can keep, even in a week when two caregivers call out.</p>
<ul><li><b>Tier A (8 to 10 contacts):</b> sources that already sent you a client or clearly could. In person every two weeks.</li>
<li><b>Tier B (10 to 15):</b> good fits you’re still earning. In person monthly, plus one useful email.</li>
<li><b>Tier C (the rest):</b> quarterly touch, mostly by email or a quick call.</li></ul>
<div class="bp-tbl"><table>
<thead><tr><th>Week</th><th>Referral outreach</th><th>Online and families</th><th>Owner review</th></tr></thead>
<tbody>
<tr><td>Week 1</td><td>Tier A visits: hospitals and rehab near your office</td><td>Ask every family that started last month for a review</td><td>Last month’s referrals by source</td></tr>
<tr><td>Week 2</td><td>Tier B visits: senior living and home health intake</td><td>Publish one answer page (cost, respite, dementia care)</td><td>Missed calls and callback times</td></tr>
<tr><td>Week 3</td><td>Tier A again; attorney or care manager coffee</td><td>Update Business Profile photos, services and hours</td><td>Caregiver capacity for next month</td></tr>
<tr><td>Week 4</td><td>Tier C emails; thank-you notes to anyone who referred</td><td>Check search queries and ad spend</td><td>Which sources move up or down a tier</td></tr>
</tbody></table></div>
<p>Capacity belongs on that calendar. The {SRC['bls']} expects about 760,500 openings a year for home health and personal care aides over the next decade, so every agency in Houston is competing for the same caregivers. Promising a hospital next-day starts you can’t staff burns the relationship faster than never visiting. When recruiting is behind, slow the outreach and say why.</p>"""),

        ("Home care agency marketing ideas that stay inside Texas rules", f"""<p>A few rules shape what you can say and do, and competitors break them all the time.</p>
<p><b>The license comes first.</b> Under {SRC['hsc142']}, nobody may provide personal assistance services for pay in Texas, or tell the public they do, without a home and community support services agency (HCSSA) license for each place of business that directs those services. {SRC['hhsc']} lists the categories: Licensed Home Health, Licensed and Certified Home Health, Hospice, Personal Assistance Services, plus home dialysis designations. If you hold a personal assistance license only, keep “home health” out of your ads, site and profile; home health is a separate license category, and the statute is written around what you represent to the public. Put your license number on your site. Families and planners notice.</p>
<p><b>Paying for referrals is a question for a lawyer.</b> Texas has a patient-solicitation law, {SRC['occ102']}, that deals with paying or accepting something of value for securing patients for a licensed provider, and federal anti-kickback rules can come into play when Medicaid or another federal program pays for care. We’re marketers, so we won’t tell you where the lines sit. Before you sign with a placement service, offer anyone a referral bonus or set a budget for gifts and meals for referral sources, talk to a healthcare attorney.</p>
<p><b>Reviews have rules.</b> {SRC['rev']} bans incentives, asking only happy families, and asking staff to collect reviews that name a specific caregiver. Our {'<a href="/blog/complete-guide-google-reviews/">guide to Google reviews</a>'} has a request script that stays inside the lines.</p>
<p>Inside those limits, plenty works:</p>
<ul><li>A family guide to the first week home from the hospital, printed for discharge planners and posted on your site.</li>
<li>Respite care packages for family caregivers, promoted to churches and caregiver support groups.</li>
<li>A LinkedIn presence for the owner, since case managers and attorneys check who they’re referring to.</li>
</ul>"""),

        ("Score your referral sources every 90 days", f"""<p>Most agencies know how many clients they have. Few know which source sent them, or which sources send inquiries that never turn into care. Without that, you keep buying lunch for the friendliest office instead of the most productive one.</p>
<!--fig:track-->
<p>A spreadsheet works fine at first. Log every inquiry with the fields above. After 90 days you’ll see which three or four sources produce most of your hours. Those move to Tier A. Sources that refer but never convert may be sending clients who need skilled care, which is a conversation worth having.</p>
<p>For online inquiries, separate calls from Google Business Profile, organic search and ads with tracking numbers, so the review push and the ad spend each get credit for what they actually do.</p>
<p>Start with the list. Write down your 30 referral contacts this week, tier them, and put the first month of visits on the calendar. If you’re also paying for Google or Meta ads to reach families, compare the ad schedule with the hours someone answers the intake line. Evening clicks that land on voicemail are a common leak in home care accounts. Our free {'<a href="/contact/">Ad Spend Leak Check</a>'} looks for that and anything else draining the budget, and you get the 10-minute recorded review within 48 hours. We work with agencies from {'<a href="/digital-marketing-agency-conroe-tx/">Conroe</a>'} to Kingwood, and we’ll tell you plainly if the money would do more on the referral side.</p>"""),
    ],
    "faq": [
        ("What are the best referral sources for home care?",
         "For most non-medical agencies around Houston, the fastest sources are senior living communities, home health and hospice intake teams, and past clients' families. Hospital case managers, skilled nursing and rehab social workers, elder-law attorneys, geriatric care managers and physicians' offices take longer to earn but send steady, high-value clients once they trust that you start quickly and staff reliably."),
        ("How long does it take a new home care agency to get clients?",
         "Expect your first clients from personal networks, senior living and online search within the first few months, and hospital or physician referrals to build more slowly as you prove reliability. The agencies that speed this up answer every call live, start care within a day or two, and visit their best referral contacts on a fixed schedule instead of when things get slow."),
        ("Can a home care agency pay for referrals in Texas?",
         "Ask a healthcare attorney before you pay anyone for a referral. Texas has a patient-solicitation law in Occupations Code chapter 102, and federal anti-kickback rules can apply when Medicaid or other federal programs pay for care. Placement-agency fees, referral bonuses and gifts to referral sources can all raise questions, so get advice on your specific arrangement first. Referrals earned through reliable service don't involve paying anyone."),
        ("Do non-medical home care agencies need a license in Texas?",
         "Yes. Texas Health and Safety Code section 142.002 requires a home and community support services agency license to provide personal assistance services for pay or to advertise them, and the license applies to each place of business that directs those services. Texas HHSC lists Personal Assistance Services as its own license category, separate from home health and hospice."),
        ("Should a home care agency use Google Ads?",
         "Usually yes, once your phones are answered and your website shows rates, service towns and your license. Start with branded searches and home care searches in the towns you staff, schedule ads for staffed hours, and track calls. Health-related advertising has audience and remarketing restrictions, so check Google's healthcare and personalized advertising policies before building campaigns."),
    ],
    "figures": {
        "market": {
            "type": "stats",
            "title": "The home care market north of Houston",
            "stats": [["110K+", "Montgomery County residents 65 or older"], ["14.9%", "Share of county residents 65+"], ["75%", "Adults 50+ who want to stay home"], ["63M", "U.S. family caregivers in 2025"]],
            "note": "Source: U.S. Census Bureau QuickFacts (V2025); AARP",
            "alt": "Stat tiles on Montgomery County residents over 65 and family caregivers, context for how home care agencies get clients",
            "caption": f"County figures from {SRC['census']}; preferences and caregiver counts from AARP’s 2024 and 2025 reports.",
        },
        "visit": {
            "type": "steps",
            "title": "A first visit to a hospital case management team",
            "sub": "How we’d approach one near The Woodlands",
            "steps": [
                ["Register as a vendor", "Call the department and follow the hospital’s vendor check-in rules before visiting."],
                ["Bring proof, not swag", "License number, insurance, caregiver screening and training, real minimum shift."],
                ["State what you don’t do", "Explain the line between personal assistance and skilled home health."],
                ["Give one direct number", "A line that a person answers evenings and weekends."],
                ["Follow up after a start", "With family permission, confirm the caregiver arrived and the first shift went well."],
            ],
            "alt": "Five steps for a home care agency to win referrals from hospital case managers and discharge planners in The Woodlands",
            "caption": "Case managers remember the agency that solved a Friday-afternoon discharge, not the one with the nicest pens.",
        },
        "track": {
            "type": "checklist",
            "title": "What to log for every home care inquiry",
            "sub": "Review it monthly to re-tier referral sources",
            "items": [
                "Referral source and the person who sent it",
                "Date and time of the first contact",
                "Assessment scheduled and completed",
                "Care started, or the reason it didn't",
                "Hours per week at start and at 90 days",
                "Hours from first call to first shift",
                "Online channel: profile, organic search or ads",
                "Thank-you sent to the referral source",
            ],
            "alt": "Checklist of what home care agencies should track for each referral source, from first call to hours per week",
            "caption": "Ninety days of this log tells you which referral sources deserve a visit every two weeks.",
        },
    },
}

POST2 = {
    "slug": "home-care-seo-the-woodlands-houston",
    "title": "Home Care SEO: Rank for “Home Care Near Me” in The Woodlands",
    "seo_title": "Home Care SEO for The Woodlands & Houston Agencies",
    "desc": "Home care SEO for agencies in The Woodlands and Houston: Google Business Profile categories, service-area rules, town pages and reviews that rank.",
    "category": "SEO & AI search",
    "icons": ["Google Business Profile", "Search Console", "Google Analytics"],
    "art": "b4",
    "hero": "search",
    "hero_alt": "Search illustration for a home care SEO guide for senior care agencies in The Woodlands and Greater Houston",
    "related": ["rank-in-google-map-pack-houston", "change-business-address-google-without-suspension", "power-of-local-landing-pages"],
    "sections": [
        (None, f"""<p>Home care SEO is the work of showing up when a family searches “home care near me” or “in-home care in Spring TX,” in both the map pack and the regular results. For an agency in The Woodlands or Greater Houston, most of it comes down to a correctly set-up Google Business Profile, one useful page for each community you actually staff, steady reviews from families, and pages that answer cost and payment questions honestly.</p>
<p>Claiming the profile takes ten minutes. The harder calls come after: which category fits your Texas license, what to do when your office is a suite off Sawdust Road and your caregivers cover six towns, and how to compete when a family in Kingwood is comparing you with a franchise that has three listings.</p>
<p>That’s what this post covers. It’s the companion to our <a href="{SIB1}">referral playbook for home care agencies</a>; that one covers hospitals and attorneys, this one covers Google.</p>"""),

        ("What home care SEO has to win", f"""<p>A daughter searching for help for her father sees two kinds of results, and they’re ranked differently.</p>
<ul><li><b>The map pack.</b> Three Business Profiles with stars and a call button. Distance from the searcher weighs heavily, along with your category, your reviews and how well your profile matches the search.</li>
<li><b>Organic results.</b> Websites. Here a page about “home care in Conroe” with real Conroe details beats a homepage that lists 14 towns in the footer.</li></ul>
<p>For “near me” searches the map pack dominates on phones. For longer searches like “24 hour home care for dementia The Woodlands” or “how much does in-home care cost in Houston,” organic pages and AI answers carry more weight, and those are the searches adult children type once they’re past the panic stage.</p>
<p>Our guide to {'<a href="/blog/rank-in-google-map-pack-houston/">ranking in the Google map pack in Houston</a>'} covers the general mechanics. Below is what’s specific to home care.</p>"""),

        ("Home care Google Business Profile: categories and setup", f"""<p>Your primary category is one of the strongest signals your profile has, and home care is a category mess.</p>
<p>Many non-medical agencies use <b>Home health care service</b>. Google also has a newer category, <b>Home help service agency</b>, aimed at non-medical in-home help, which few agencies were using when local SEO practitioners discussed it in {SRC['lsf']}. The same thread is a good reminder not to go “fixing” competitors’ categories through public edits; it’s an easy way to draw attention to your own profile.</p>
<p>In Texas there’s a wrinkle worth raising with your attorney. {SRC['hsc142']} ties licensing to what an agency represents to the public, and home health is a different license category from personal assistance services. If your HCSSA license covers personal assistance only, a primary category that says “home health” is worth a question to your attorney before you pick it. Our usual setup for a personal-assistance-only agency:</p>
<ul><li><b>Primary:</b> Home help service agency, if it fits your services.</li>
<li><b>Secondary:</b> other categories only where they accurately describe a service you provide. Fewer, accurate categories beat a long list of hopeful ones.</li>
<li><b>Business name:</b> your real name only. No “Home Care The Woodlands” tacked on; {SRC['gbp']} don’t allow extra information in the name.</li>
<li><b>Services:</b> companion care, personal care, respite, dementia and Alzheimer’s care, post-hospital care, 24-hour and live-in care, each with a plain description.</li>
<li><b>Photos:</b> real staff, your office and training, shot with permission. Never a client’s face or home without written consent.</li></ul>
<p>One outdated tip to ignore: plenty of articles still recommend Business Profile messaging. {SRC['chat']} on July 31, 2024. Put the effort into answering calls instead.</p>"""),

        ("Service-area rules when you run the agency from an office or a home", f"""<p>Most home care agencies are service-area businesses. Caregivers go to the client; families rarely visit the office. {SRC['gbp']} say a service-area business should hide its address, keep its service area within about two hours’ driving time of its base, and never list a virtual office or a rented mailbox unless it’s staffed during business hours.</p>
<p>What that means in practice:</p>
<ul><li><b>Run from home?</b> Hide the address and list the towns or ZIP codes you staff. Your license address and your Google address should still be the same real place.</li>
<li><b>Real office where families come for consultations during posted hours?</b> You can show the address and add a service area.</li>
<li><b>Thinking about a second listing in Kingwood?</b> Only if it’s a real, staffed office. Texas also requires an HCSSA license for each place of business that directs services, so a fake branch is a problem with Google and with the state.</li>
<li><b>Moving offices?</b> Change it carefully. Our guide to {'<a href="/blog/change-business-address-google-without-suspension/">changing a business address without a Google suspension</a>'} walks through the order of operations.</li></ul>
<p>Service area settings don’t make you rank in a town 25 miles away. They tell Google where you’re willing to work. Ranking in those towns comes from your website, which is the next section.</p>"""),

        ("Home care near me ranking: one location page per community", f"""<p>Since your profile can only sit in one place, your website does the work of showing up in each community. We build one page per town the agency actually staffs, and each page has to earn its keep with details a family in that town would recognize.</p>
<!--fig:towns-->
<div class="bp-tbl"><table>
<thead><tr><th>Community</th><th>Local context for the page</th><th>Searches to target</th></tr></thead>
<tbody>
<tr><td>The Woodlands</td><td>Villages from Panther Creek to Creekside Park; three major hospitals nearby</td><td>home care The Woodlands, senior care The Woodlands TX</td></tr>
<tr><td>Spring</td><td>Straddles Harris and Montgomery counties; I-45 and the Grand Parkway</td><td>in home care Spring TX, caregivers Spring</td></tr>
<tr><td>Conroe</td><td>County seat; near HCA Houston Healthcare Conroe and Lake Conroe</td><td>home care Conroe, elderly care Conroe TX</td></tr>
<tr><td>Magnolia</td><td>FM 1488 corridor; rural lots where drive time matters</td><td>home care Magnolia TX, respite care Magnolia</td></tr>
<tr><td>Tomball</td><td>Harris County; near HCA Houston Healthcare Tomball and SH-249</td><td>in home senior care Tomball</td></tr>
<tr><td>Kingwood</td><td>Part of the City of Houston; near HCA Houston Healthcare Kingwood</td><td>home care Kingwood TX, dementia care Kingwood</td></tr>
</tbody></table></div>
<p>Each page should include how fast you can start in that town, any caregivers who live nearby, the hospitals and rehab facilities you regularly receive clients from, honest notes about coverage (“Magnolia shifts under four hours may have a travel minimum”), a few family reviews from that area with permission, and a clear phone number.</p>
<!--fig:pages-->
<p>Skip the pages for towns you can’t staff. A Katy page that leads to “we don’t have caregivers out there yet” costs you a family’s trust. Our post on {'<a href="/blog/power-of-local-landing-pages/">local landing pages</a>'} goes deeper on structure.</p>"""),

        ("Content that answers adult children’s questions", f"""<p>Location pages catch “near me.” Answer pages catch the questions that come before the call. The adult child searching at 11 p.m. wants to know what this will cost, what a caregiver will and won’t do, and how to start.</p>
<h3>Cost</h3>
<p>Publish your rates, or at least a range and your minimum shift. {SRC['cs']} put the 2025 national median for a non-medical caregiver at $35 an hour, and {SRC['cstx']} put the Texas median at $68,640 a year for 44 hours a week, which works out to about $30 an hour. Houston rates vary by agency and schedule, so show yours and explain what changes it: overnight, weekends, live-in and two-person transfers.</p>
<h3>Pages worth writing</h3>
<ul><li>How much does in-home care cost in Houston, with your own rate table.</li>
<li>Live-in vs 24-hour care: the difference and the cost.</li>
<li>What a non-medical caregiver can and can’t do under your Texas license.</li>
<li>Signs a parent needs help at home, written by your care coordinator.</li>
<li>Bringing a parent home from the hospital: the first 72 hours.</li>
<li>Respite care for family caregivers, including short weekend blocks.</li></ul>
<p>Write them in plain language, sign them with a real name and title, and link each one to the matching town pages. That’s also what AI answers tend to quote: a clear, specific answer from a named local source.</p>"""),

        ("Medicaid, VA and long-term care insurance pages", f"""<p>Only build these if you actually accept the payment source, and keep them accurate.</p>
<ul><li><b>Medicaid.</b> Texas Medicaid pays for attendant care for some people through STAR+PLUS health plans and programs like {SRC['cfc']}, but agencies need contracts with the plans and the rules are detailed. If you’re contracted, say which plans. If you’re not, say so and point families to the H-GAC or Harris County Area Agency on Aging.</li>
<li><b>VA.</b> Veterans may get in-home help through VA community care programs or use a VA pension with Aid and Attendance to pay privately. Explain which applies to your agency and suggest families confirm eligibility with the VA or an accredited representative.</li>
<li><b>Long-term care insurance.</b> Explain how you help with claim paperwork, caregiver timesheets and the waiting period before benefits start. Families often don’t know their policy covers home care until someone asks.</li></ul>
<p>Don’t promise coverage. A page that says “VA pays for everything” will produce angry calls, and possibly a complaint.</p>"""),

        ("Reviews from families without oversharing", f"""<p>Reviews matter for the map pack, and families read them closely. Home care reviews come with privacy problems most businesses don’t have.</p>
<p>{SRC['rev']} prohibits incentives, asking only happy families, and asking staff to collect reviews that mention specific content or name a staff member. So no “please mention Maria!” in your review request, even though families often will on their own.</p>
<p>Our rules for home care clients:</p>
<ul><li>Ask the adult child who hired you, around the 30-day mark, with a plain link.</li>
<li>Never confirm in a reply that the reviewer’s parent is a client. Thank them, keep it general and invite them to call.</li>
<li>Don’t mention diagnoses, addresses, schedules or hospital stays in replies, even if the family did.</li>
<li>Don’t ask caregivers to review the agency. Employment is a conflict of interest under Google’s policy, and the FTC’s rules apply too; see our post on the {'<a href="/blog/fake-reviews-rule-local-businesses/">fake reviews rule</a>'}.</li></ul>
<p>The {'<a href="/blog/complete-guide-google-reviews/">complete guide to Google reviews</a>'} has request templates, and the {'<a href="/blog/medical-practice-marketing-houston/">medical practice post</a>'} covers privacy-safe replies in more depth.</p>"""),

        ("Measuring home care SEO with Search Console", f"""<p>A rank check shows where you appeared from one spot on one day. Search Console shows what families actually typed, across every town, for months.</p>
<p>In the {SRC['gsc']}, use the Queries tab with a filter for “home care,” “in home care” and each town name. Then switch to Pages and check each location page’s impressions, clicks and average position. Do it monthly and write down three numbers per town page.</p>
<!--fig:funnel-->
<p>Search Console stops at the click, so close the loop:</p>
<ul><li>Use a tracking number on the Business Profile and another on the website, so you can see which produces calls.</li>
<li>Mark contact form submissions and call clicks as conversions in Google Analytics.</li>
<li>Ask every new family how they found you and log it next to the source in your intake sheet.</li></ul>
<p>The measure that matters is new weekly care hours by channel, not traffic.</p>"""),

        ("Home care marketing services: what to expect and ask", f"""<p>If you hire help, most single-location agencies fall in the single-location band in our {'<a href="/blog/seo-cost-houston-the-woodlands/">SEO cost guide for Houston and The Woodlands</a>'}. Before you sign with anyone, ask:</p>
<ul><li>Which Business Profile category will you use, and why, given our license?</li>
<li>Which towns get pages, and what will make each one different?</li>
<li>How will you handle reviews and photos without client privacy problems?</li>
<li>Will you report calls and inquiries, or only rankings?</li>
<li>Who owns the website, the profile and the tracking numbers if we part ways?</li></ul>
<p>Be wary of anyone selling a fake address in each suburb or a 50-town page package. Those get profiles suspended and waste money. Our {'<a href="/services/web-design-seo-pr/">web design and SEO team</a>'} builds town pages and profile setups for agencies in {'<a href="/digital-marketing-agency-spring-tx/">Spring</a>'}, {'<a href="/digital-marketing-agency-tomball-tx/">Tomball</a>'} and around The Woodlands.</p>
<p>Today, before anything else: open your Business Profile, read the primary category next to your HCSSA license, and write down the towns you could staff tomorrow morning. Those two lists set the scope of everything above. If you also buy “home care near me” clicks in Google Ads, look at where they come from, because a radius setting will happily pay for searches in towns you can’t cover. Our free {'<a href="/contact/">Ad Spend Leak Check</a>'} maps that out in a 10-minute recorded video, sent within 48 hours.</p>"""),
    ],
    "faq": [
        ("What Google Business Profile category should a home care agency use?",
         "Pick the category that most accurately describes your licensed services. Many non-medical agencies use Home health care service, but Google also offers Home help service agency for non-medical in-home help. In Texas, an agency without a home health license should be careful about any wording that implies one, so check your category choice against your HCSSA license."),
        ("Can I list my home care agency in several cities on Google?",
         "You can show one Business Profile per real, staffed location, and set a service area listing the towns you cover within about two hours' drive. You can't create profiles for virtual offices or mailboxes. To appear in other communities, build a genuinely local page on your website for each town you staff, and let the profile point to your main location."),
        ("How long does home care SEO take?",
         "Profile fixes such as a better category, services and fresh photos can change map visibility within weeks. New town pages usually take two to four months to settle in the organic results, longer in competitive areas like The Woodlands and Kingwood where franchises have been publishing for years. Steady reviews from families keep improving results over time."),
        ("How much does in-home care cost in Houston?",
         "CareScout's 2025 survey put the Texas median for a non-medical caregiver at $68,640 a year for 44 hours a week, roughly $30 an hour, and the national median at $35 an hour. Houston agency rates vary with overnight, weekend and live-in schedules and minimum shift length, so families should compare written rate sheets from two or three licensed agencies."),
        ("Should my home care agency show its address on Google?",
         "Only if families can visit you there during posted hours, such as for consultations at a staffed office. If you run the agency from home or a back office that clients never visit, Google's guidelines say to hide the address and set a service area instead. Either way, the address must be a real place that matches your license."),
    ],
    "figures": {
        "towns": {
            "type": "map",
            "title": "One location page per community you staff",
            "sub": "The six towns we’d start with for a Woodlands-based agency",
            "highlight": ["The Woodlands", "Spring", "Conroe", "Magnolia", "Tomball", "Kingwood"],
            "alt": "Map of The Woodlands, Spring, Conroe, Magnolia, Tomball and Kingwood for home care SEO location pages",
            "caption": "Only build pages for towns where you can actually start care this week.",
        },
        "pages": {
            "type": "compare",
            "title": "Thin town page vs one that ranks",
            "left": {"title": "Swapped-town template", "items": ["Same text with the town name changed", "Stock photos of smiling seniors", "No rates or minimum shift", "Lists towns you can’t staff"]},
            "right": {"title": "Real community page", "items": ["Start time and caregivers nearby", "Hospitals you work with in the area", "Rates, minimums and travel notes", "Reviews from local families, with permission", "One clear phone number"]},
            "alt": "Comparison of a thin template page and a strong home care SEO location page for Spring, Conroe or Kingwood",
            "caption": "Families can tell when a page was written for their town, and so can Google.",
        },
        "funnel": {
            "type": "funnel",
            "title": "From search to weekly care hours",
            "stages": [["Impressions in Search Console", "2,000"], ["Clicks to town pages", "90"], ["Calls and forms", "14"], ["In-home assessments", "6"], ["New clients", "3"]],
            "note": "Illustrative example",
            "alt": "Illustrative funnel from home care SEO impressions to calls, assessments and new clients for an agency near The Woodlands",
            "caption": "An example month for one town page; track your own numbers at each stage.",
        },
    },
}

POSTS = [POST1, POST2]
