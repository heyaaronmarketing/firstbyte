"""Batch 12: therapist and counseling practice marketing in Houston (solo and group practices: LPCs, LMFTs, LCSWs,
psychologists).

Research: WordStream/LocaliQ 2026 Google Ads benchmarks (no counseling category; Physicians & Surgeons $4.76 CPC and
$40.04 CPL, Health & Fitness $6.17 and $67.36); 22 TAC 681.49 (LPC advertising: testimonials, licensure status, LPC
Associate plus supervisor name, responsibility for hired advertisers); 22 TAC 465.6 (psychologists may not solicit
testimonials from current clients); 22 TAC 882.23 (practice occurs where the client is located; out-of-state telehealth
follows that jurisdiction's rules); BHEC MFT social media guidelines (July 2025); ACA Code of Ethics C.3.b; APA Ethics
Code 5.05; Google healthcare and medicines policy (US addiction services require LegitScript certification); Google's
Health in personalized advertising policy (counseling for depression, anxiety and addiction is a sensitive category; no
advertiser-curated audiences such as Customer Match); Search Engine Land on running sensitive categories without
remarketing; Google LSA category list (no therapist/counselor category in the US); Google Business Profile guidelines
(individual practitioners, solo practitioner naming); Holland & Knight on AHA v. Becerra (N.D. Tex., June 20, 2024);
Search Engine Land on Meta's health and wellness data restrictions; Meta personal attributes policy; TMLT on the Elite
Dental Associates (Dallas) $10,000 OCR settlement over Yelp replies; ClearHealthCosts on Psychology Today referrals
($29.95/month); BHEC PSYPACT page (Texas joined via HB 1501, 2019); Counseling Compact map (Texas not a member); Texas
Counseling Association 89th session report (SB 498 died); BHEC page on the social work compact (bills died in 2025);
American Psychiatric Association summary of No Surprises Act good faith estimates; University of Houston study on
mental health deserts (39 of 96 ZIP codes with no licensed professionals listed).
PAA/competitor phrasing read for "therapist marketing", "how to get more therapy clients", "private practice marketing",
"counseling practice google ads", "therapist seo", "psychology today worth it".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "wordstream": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream and LocaliQ’s 2026 Google Ads benchmarks"),
    "tac681": A("https://law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-681-49", "22 TAC §681.49"),
    "tac465": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-465-6", "22 TAC §465.6"),
    "tac882": A("https://law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-882-23", "22 TAC §882.23"),
    "mftsocial": A("https://bhec.texas.gov/wp-content/uploads/2025/07/MFT-Guidelines-for-Using-Social-Media-20250715_rr.pdf", "social media guidelines for MFTs"),
    "aca": A("https://manifold.counseling.org/read/aca-code-of-ethics/section/5403851f-9eea-4961-91f4-a1e22670043f", "ACA Code of Ethics, C.3.b"),
    "apa": A("https://www.apa.org/ethics/code", "APA Ethics Code, Standard 5.05"),
    "gaddict": A("https://support.google.com/adspolicy/answer/176031?hl=en", "Google’s healthcare and medicines policy"),
    "ghealth": A("https://support.google.com/adspolicy/answer/16701855?hl=en", "Health in personalized advertising"),
    "selgoogle": A("https://searchengineland.com/google-ads-sensitive-categories-without-remarketing-473065", "Search Engine Land’s rundown"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "gbp": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s Business Profile guidelines"),
    "hklaw": A("https://www.hklaw.com/en/insights/publications/2024/06/american-hospital-assn-v-becerra-are-tracking-tools-ok-again", "Holland &amp; Knight’s summary of the ruling"),
    "selmeta": A("https://searchengineland.com/meta-ads-restrictions-health-wellness-campaigns-453094", "Search Engine Land"),
    "metapa": A("https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-attributes/", "personal attributes policy"),
    "tmlt": A("https://www.tmlt.org/resource/practice-fined-for-response-to-social-media-review", "TMLT’s write-up"),
    "pt": A("https://clearhealthcosts.com/blog/2025/12/therapists-say-psychology-today-referrals-have-dried-up-and-express-concern/", "ClearHealthCosts"),
    "psypact": A("https://bhec.texas.gov/texas-state-board-of-examiners-of-psychologists/psypact", "PSYPACT"),
    "compact": A("https://counselingcompact.gov/map/", "Counseling Compact map"),
    "tca": A("https://higherlogicdownload.s3.amazonaws.com/TXCA/9a94f13f-4453-47fd-a4ab-77e8307c79b3/UploadedImages/TCA_89th_Session_Legislative_Report.pdf", "Texas Counseling Association’s session report"),
    "swcompact": A("https://bhec.texas.gov/interstate-licensing-compact", "Social work compact bills"),
    "gfe": A("https://www.psychiatry.org/psychiatrists/practice/practice-management/no-surprises-act-implementation", "American Psychiatric Association’s summary"),
    "uh": A("https://www.uh.edu/news-events/stories/2025/november/11192025-houston-mental-health-deserts.php", "a University of Houston study"),
}

L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    {
        "slug": "therapist-counseling-practice-marketing-houston",
        "title": "Therapist and Counseling Practice Marketing in Houston: SEO, Google Ads & Directories for Group and Solo Practices",
        "seo_title": "Therapist Marketing in Houston: SEO, Ads & Directories",
        "desc": "How Houston therapists and counseling practices get more clients: specialty SEO, Google Ads rules, Psychology Today, HIPAA-safe tracking and Texas BHEC rules.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google Business Profile", "Search Console"],
        "art": "b5",
        "hero": "speech",
        "hero_alt": "Illustration of a conversation bubble for therapist and counseling practice marketing in Houston and The Woodlands",
        "related": ["medical-practice-marketing-houston", "physical-therapy-clinic-marketing-houston", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Google’s benchmark data has no counseling category, so the closest numbers are healthcare: a median <b>$4.76 per click and $40.04 per lead</b> for Physicians &amp; Surgeons and <b>$6.17 and $67.36</b> for Health &amp; Fitness, per {SRC['wordstream']}. Therapy leads cost more than that to turn into a first session, because a “lead” is often a nervous person who never calls back. Houston is crowded at the top and thin at the bottom: {SRC['uh']} found 39 of 96 Houston ZIP codes had no licensed mental health professional listed, while prosperous ZIP codes averaged 11 each.</p>
<p>It’s Tuesday at a four-clinician group practice in The Woodlands. Two voicemails from Monday night, both “looking for someone for my teenager.” A Psychology Today email from someone in Spring who wants a Saturday couples session. And an LPC Associate with six open hours who keeps asking whether the website is “doing anything.” This guide is for that practice, and for the solo LPC in Katy.</p>"""),

            ("Rank for the specialty searches clients actually type", f"""<p>Therapy clients search for a problem and a place, so the practice that has one strong page per specialty and per area wins most of the organic traffic.</p>
<ul>
<li><b>One page per specialty:</b> anxiety, couples counseling, teen therapy, EMDR, trauma, postpartum. Describe who you see, what a first session looks like, the approach in plain words, fees and which clinicians do this work.</li>
<li><b>Area pages that are real:</b> “couples counseling Katy,” “teen therapist Cypress,” “EMDR therapist The Woodlands.” Each names the office, parking and whether telehealth is offered.</li>
<li><b>Clinician bio pages</b> with license type, Texas license status, training, specialties and the age groups each person sees.</li>
<li><b>Answers before the call:</b> “What is a superbill?” “How is EMDR different from talk therapy?” AI search tools quote pages like these.</li>
<li><b>Structured data</b> for the practice and each clinician, matching the name, address and phone on your Google Business Profile.</li>
</ul>
<p>A single “Services” page listing fifteen specialties won’t rank for any of them. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} covers area pages.</p>"""),

            ("Set up Google Business Profile for a therapy practice", f"""<p>Your Business Profile decides whether you appear in the map results for “therapist near me,” and Google’s rules for practitioners are specific.</p>
<ul>
<li><b>Solo practitioner:</b> if you’re the only clinician at a branded practice, {SRC['gbp']} say to use one shared profile named like “[Practice name]: [Your name].”</li>
<li><b>Group practice:</b> the practice gets a profile for the location, and each public-facing clinician who can be reached there during stated hours can have one in their own name. No separate profiles per specialty.</li>
<li><b>Telehealth-only practices:</b> Google requires a location customers can visit or a business that travels to customers. A virtual office doesn’t qualify, so a home-based telehealth practice shouldn’t create a fake suite address.</li>
<li><b>Primary category and services:</b> pick the closest category for your practice type, then list each specialty as a service and link it to the matching page.</li>
</ul>
<p>Add real office photos and evening hours. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers the rest.</p>"""),

            ("Use Psychology Today and directories, but don’t depend on them", f"""<p>Psychology Today is still worth $29.95 a month per clinician for most practices, but it shouldn’t be your only source of clients.</p>
<p>That price has been unchanged since 2004, according to {SRC['pt']}, which in December 2025 reported therapists describing referral drops of 50% or more since around mid-2024. Psychology Today told the outlet overall directory visits and contacts were steady. Judge it by your own numbers.</p>
<ul>
<li><b>Track every directory separately.</b> Give each profile its own tracked phone number and a URL with UTM tags, so you know which listing produced which first session.</li>
<li><b>Write the profile like a landing page.</b> First line names who you help and where (“Teens and parents in Cypress and Tomball”), then fees, insurance and openings.</li>
<li><b>Check your own listing details.</b> Some therapists told ClearHealthCosts they found platform phone numbers in place of their own.</li>
</ul>
<p>Keep your payers’ “find a provider” listings current too. They’re free.</p>"""),

            ("Run Google Ads with tight controls", f"""<p>Google Ads works for therapy practices when it’s Search-only, built around specialty and area keywords, and set up for the fact that health is a restricted category.</p>
<p>Two policy facts shape the whole account. First, {SRC['ghealth']} lists counseling for depression, anxiety and addiction as a sensitive interest. Advertisers in that category can’t use their own remarketing lists or Customer Match, per Google and {SRC['selgoogle']}. Second, if you treat drug or alcohol addiction, {SRC['gaddict']} requires US advertisers to be certified through LegitScript before those ads can run, and not every provider is eligible. There’s also no Local Services Ads category for therapists or counselors in the US, per {SRC['lsa']}, so regular Search is the paid option.</p>
<ul>
<li><b>Keywords:</b> “couples counseling the woodlands,” “anxiety therapist katy,” “EMDR therapist houston,” “teen counselor cypress tx,” “marriage counselor sugar land,” plus payer terms if you’re in-network.</li>
<li><b>Negatives:</b> free, jobs, salary, careers, “how to become,” degree, CEU, internship, supervisor, “EMDR training,” “EMDR certification” (that’s clinicians shopping for courses), app, online chat, and Medicaid if you don’t accept it.</li>
<li><b>Crisis searches:</b> don’t bid on them. Put 988 and emergency instructions on every page instead.</li>
<li><b>Sample ad:</b> “Couples Counseling in The Woodlands | Licensed LMFTs, Evening Hours | In-Person or Telehealth in Texas.” No promised outcomes.</li>
</ul>
<p>Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} help with budgeting, and our {L('/services/search-marketing/', 'search marketing team')} builds accounts like this.</p>"""),

            ("Follow Texas BHEC advertising rules", f"""<p>The Texas Behavioral Health Executive Council (BHEC) regulates Texas therapists, and each profession’s rules set advertising standards for your site, profiles and ads.</p>
<ul>
<li><b>LPCs:</b> {SRC['tac681']} bars advertising that is false, misleading or “not readily verifiable,” representations that create unjustified expectations about results, and testimonials that are false or misleading. Ads and directory listings must state licensure status, such as “LPC.”</li>
<li><b>LPC Associates:</b> the same rule says associate status must appear on all advertising, with the associate’s name followed by the supervisor’s name. Group practices miss this constantly.</li>
<li><b>Your agency is your problem:</b> §681.49 also makes licensees responsible for statements made by people they hire to advertise. That includes us.</li>
<li><b>Psychologists:</b> {SRC['tac465']} says licensees may not solicit testimonials from current clients or engage in uninvited in-person solicitation.</li>
<li><b>Ethics codes go further:</b> the current {SRC['aca']} says counselors don’t solicit testimonials from current or former clients, and the {SRC['apa']} bars soliciting them from current clients. LMFTs and LCSWs have their own chapters and codes to check.</li>
</ul>
<p>In practice, we write therapy websites with no client testimonials at all. This isn’t legal advice; have ethics counsel review anything you’re unsure about.</p>
<!--fig:rules-->"""),

            ("Keep tracking and reviews HIPAA-safe", f"""<p>Tracking pixels and review replies are where therapy practices create privacy problems by accident.</p>
<p>The federal rules on tracking moved in 2024. In <i>American Hospital Association v. Becerra</i>, a federal court in Fort Worth vacated the part of HHS’s tracking guidance that treated an IP address plus a visit to a public health page as protected information, but the rest of the March 2024 bulletin stands, per {SRC['hklaw']}. Logged-in pages, intake forms and scheduling flows remain risky.</p>
<ul>
<li><b>No ad pixels on intake forms, client portals or booking confirmations</b> without a compliance sign-off.</li>
<li><b>Count conversions without content.</b> A tracked call or a “form submitted” event without the form fields is enough. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} shows how.</li>
<li><b>Expect Meta to limit you.</b> {SRC['selmeta']} describes Meta’s tiered restrictions on health and wellness advertisers, which can block lower-funnel optimization. Meta’s {SRC['metapa']} also forbids ads implying the viewer has a condition, with “Depression getting you down? Get help now.” given as a rejected example.</li>
</ul>
<p>Reviews are harder. If you can’t ask clients for testimonials, you also shouldn’t be running review-request campaigns to them. Let reviews arrive on their own. A Dallas dental practice paid $10,000 to settle with HHS’s Office for Civil Rights in 2019 after Yelp replies disclosed patient details, per {SRC['tmlt']}. BHEC’s {SRC['mftsocial']} also list derogatory online remarks about a client as unprofessional.</p>
<!--fig:reply-->
<p>A reply that works for five stars or one: “Thank you for sharing this. Our policy is not to confirm or discuss whether anyone is a client. Please call the office if you’d like to talk with our practice director.” See our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} for more.</p>"""),

            ("Decide insurance or private pay before you write the site", f"""<p>Your payment model changes your keywords and pages, so decide it first.</p>
<ul>
<li><b>In-network practices</b> win on insurance searches. Build a page per major payer you accept and keep payer directories current.</li>
<li><b>Private-pay practices</b> win on specialty depth, evening hours and clinician credentials. Publish fees, explain superbills and out-of-network benefits, and lead with specialties like EMDR and couples work.</li>
<li><b>Good faith estimates:</b> under the No Surprises Act, practices must give uninsured and self-pay clients a written estimate and post a prominent notice in the office and on the website that one is available, per the {SRC['gfe']}. Put it on your fees page.</li>
</ul>"""),

            ("Market telehealth across Texas, carefully", f"""<p>A Texas license lets you serve clients anywhere in Texas by telehealth, so statewide pages and ads are fair game.</p>
<p>BHEC’s {SRC['tac882']} says practice happens where the client is located, and telehealth to a client outside Texas is subject to that other state’s rules. Psychologists have more room: Texas joined {SRC['psypact']} through HB 1501 in 2019. Counselors don’t yet. Texas isn’t on the {SRC['compact']}, and SB 498 died in 2025, per the {SRC['tca']}. {SRC['swcompact']} also died.</p>
<p>So a Woodlands practice can run telehealth ads to Austin, Dallas and the Rio Grande Valley but should exclude other states and confirm Texas residency at booking.</p>"""),

            ("Speed up intake", f"""<p>The practice that calls back first usually books the first session, because most people searching for a therapist contact several at once.</p>
<ul>
<li><b>Answer live during business hours,</b> or use an intake coordinator.</li>
<li><b>Same-day callback</b> for voicemails and forms, with a short consult call script that covers fit, fees, availability and next steps.</li>
<li><b>Match quickly.</b> In a group practice, intake should know who has openings this week, by specialty.</li>
</ul>
<p>Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up cadence.</p>"""),

            ("What a therapy practice should budget", f"""<p>Ranges we’d start from in Greater Houston. They aren’t benchmarks.</p>
<div class="tbl"><table>
<thead><tr><th>Practice</th><th>Google Ads (media)</th><th>Directories</th><th>SEO and content</th></tr></thead>
<tbody>
<tr><td>Solo LPC or LMFT, private pay</td><td>$600 to $1,500 a month on one or two specialties</td><td>$29.95/month Psychology Today, plus free payer directories</td><td>A few specialty pages done well, written once and updated</td></tr>
<tr><td>Group practice, 4 to 10 clinicians</td><td>$2,000 to $6,000 a month, split by specialty with openings</td><td>One profile per clinician</td><td>Specialty and area pages, monthly content, GBP management</td></tr>
<tr><td>Multi-office group (e.g. The Woodlands and Katy)</td><td>$5,000+ a month with campaigns per office</td><td>Per clinician, per office</td><td>Location pages per office, plus statewide telehealth pages</td></tr>
</tbody></table></div>
<p>Spend follows capacity. If a clinician is full, pause that specialty. See {L('/blog/seo-cost-houston-the-woodlands/', 'what SEO costs in Houston')} for the organic side.</p>"""),

            ("Your first 90 days", f"""<!--fig:plan-->
<p>Compliance and tracking come first, ads second, and the honest review in month three decides which directories and specialties stay.</p>"""),

            ("Mistakes we see", f"""<ul>
<li><b>Testimonials on the homepage.</b> Even anonymous ones. Under the codes above, take them down.</li>
<li><b>Associates listed like fully licensed clinicians,</b> without “LPC Associate” and the supervisor’s name.</li>
<li><b>Meta pixel on the intake form</b> because a website template installed it by default.</li>
<li><b>Ads that diagnose the reader,</b> which Meta’s personal attributes policy rejects.</li>
<li><b>Bidding on “EMDR” alone</b> and paying for clinicians looking for training.</li>
<li><b>Running ads for a clinician who’s full,</b> then sending new clients to a six-week waitlist.</li>
</ul>"""),

            ("Measure cost per intake, not cost per lead", f"""<p>The number that matters is cost per first session attended, by source, because a therapy “lead” has a long way to go before it’s a client.</p>
<!--fig:funnel-->
<p>Track inquiries, consult calls held, first sessions booked and first sessions attended in a spreadsheet or your EHR’s referral field, monthly by source. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} explains how to tie calls back to campaigns without recording clinical content. If you’d like a senior strategist to build a plan around your specialties, openings and payer mix, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much should a therapist spend on Google Ads in Houston?",
             "A solo private-pay therapist can test with about $600 to $1,500 a month in ad spend focused on one or two specialties. Group practices often spend $2,000 to $6,000. There’s no counseling category in the 2026 WordStream benchmarks; the closest healthcare categories show median clicks of about $4.76 to $6.17. Judge results by cost per first session attended."),
            ("Is Psychology Today worth it for therapists in Houston?",
             "Usually yes, at $29.95 a month per clinician, as long as it isn’t your only source of clients. Some therapists have reported fewer referrals since 2024, while Psychology Today says overall traffic is steady. Give your profile its own tracked phone number and check after three months how many first sessions it actually produced."),
            ("Can therapists use client testimonials in Texas?",
             "Generally, no. Texas psychologists may not solicit testimonials from current clients under 22 TAC 465.6, and the ACA Code of Ethics says counselors don’t solicit them from current or former clients. Texas LPC rules also bar misleading testimonials. Most practices skip testimonials and describe their clinicians and methods instead. Check your own board rules and code."),
            ("Can therapists run Google remarketing ads?",
             "No, not for mental health services. Google treats counseling for conditions like depression, anxiety and addiction as a sensitive health category, so you can’t use your own remarketing lists or Customer Match. Search campaigns built on specialty and location keywords still work well. Addiction treatment ads in the US also need LegitScript certification."),
            ("Can a Texas LPC see clients in other states by telehealth?",
             "Only if the other state allows it. Texas rules say telehealth to a client outside Texas is subject to that state’s regulations, and Texas isn’t part of the Counseling Compact. Psychologists can use PSYPACT, which Texas joined in 2019. Most Texas counselors should target ads to Texas only and confirm residency at intake."),
        ],
        "figures": {
            "rules": {
                "type": "checklist",
                "title": "Texas therapist advertising checklist",
                "sub": "Based on BHEC rules and ACA/APA ethics codes cited in this post",
                "items": [
                    "License type shown on every ad, bio and directory profile",
                    "“LPC Associate” plus supervisor’s name for associates",
                    "No testimonials solicited from clients",
                    "No promised results or timelines",
                    "Board certification claims name the full specialty board",
                    "Agency copy reviewed by the licensee before it runs",
                    "Addiction services kept out of ads unless LegitScript certified",
                    "Good faith estimate notice on the fees page",
                ],
                "alt": "Checklist of Texas BHEC advertising rules for therapist and counseling practice marketing in Houston and The Woodlands",
                "caption": "A starting checklist, not legal advice. Each profession’s BHEC chapter has its own details.",
            },
            "reply": {
                "type": "compare",
                "title": "Replying to a therapy practice review",
                "left": {"title": "Risky reply", "items": ["“We’re sorry your sessions with Dr. Lee felt rushed”", "“As we discussed at your last visit...”", "Mentions insurance, diagnosis or fees", "Argues the facts in public", "Thanks them “for being a client”"]},
                "right": {"title": "Safer reply", "items": ["Doesn’t confirm anyone is a client", "Same short reply for good and bad reviews", "Invites a call to the practice director", "No clinician names tied to the reviewer", "Reviewed by whoever handles compliance"]},
                "alt": "Comparison of risky and HIPAA-safer review replies for therapist practice marketing in Houston and The Woodlands",
                "caption": f"A Dallas practice paid $10,000 over Yelp replies that disclosed patient details, per {SRC['tmlt']}.",
            },
            "plan": {
                "type": "steps",
                "title": "First 90 days for a Houston therapy practice",
                "sub": "In this order, because compliance fixes come before ad spend",
                "steps": [
                    ["Days 1-15", "Fix bios, license labels, associate supervisor names and testimonials."],
                    ["Days 15-30", "Business Profiles per Google’s practitioner rules; tracked numbers on directories."],
                    ["Days 30-45", "Remove pixels from intake and portal pages; set call and form conversions."],
                    ["Days 45-75", "Launch Search for the two specialties with the most open hours."],
                    ["Days 75-90", "Review cost per first session by source; cut or scale."],
                ],
                "alt": "Five-step 90-day marketing plan for a therapist or counseling practice in Houston and The Woodlands",
                "caption": "Specialty pages get written alongside steps three and four.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From click to first session",
                "stages": [["Ad clicks ($2,000 spend)", "400"], ["Calls and forms", "32"], ["Consult calls held", "18"], ["First sessions booked", "12"], ["First sessions attended", "10 ($200 each)"]],
                "note": "Illustrative example",
                "alt": "Funnel showing cost per intake for therapist Google Ads in Houston and The Woodlands from clicks to first sessions",
                "caption": "Illustrative only. About $63 per inquiry becomes $200 per attended first session.",
            },
        },
    },
]
