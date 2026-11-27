"""Batch 18 (module r_b): a rules guide to HIPAA-compliant marketing for Houston healthcare practices, and a
playbook for LinkedIn Ads for Houston B2B companies (energy, industrial, professional services).

Research, HIPAA post: HHS OCR's "Use of Online Tracking Technologies by HIPAA Covered Entities and Business
Associates" page (authenticated vs. unauthenticated pages, BAAs, cookie banners not authorizations, CDP alternative,
note on the June 20, 2024 AHA v. Becerra order); Epstein Becker Green on OCR withdrawing its Fifth Circuit appeal
(Aug. 29, 2024); Holland & Knight on the ruling; FTC/OCR joint letter to about 130 hospital systems and telehealth
providers (July 20, 2023); FTC BetterHelp order ($7.8 million, March 2, 2023); HHS resolution agreements with Elite
Dental Associates of Dallas ($10,000, Oct. 2019) and Manasa Health Center ($30,000, June 2023); Google Analytics
HIPAA help page (no BAA, keep tags off authenticated pages); Google Ads "Health in personalized advertising" policy
(no Customer Match, your data segments, lookalikes or audience expansion); Meta's personal attributes ad standard
("Do you have diabetes?" example); Cardinal Digital Marketing and Search Engine Land on Meta's January 2025 health and
wellness data restrictions (Core Setup, restricted events, full restriction; lead ads unaffected so far); Marketing
Brew on cosmetic vs. medical Botox categorization; Texas Optometry Board and HIPAA Journal on HB 300 / Chapter 181
(broad covered entity definition, 90-day training, 15-day EHR access, penalties $5,000 / $25,000 / $250,000, $1.5M
pattern cap); Texas Health & Safety Code 181.152 (marketing authorization, mailing rules, 45-day removal) and
181.154 (electronic disclosure notice and authorization); Texas State Law Library on the TDPSA (effective July 1,
2024, HIPAA-regulated entities exempt, small-business consent to sell sensitive data); HHS covered entity definition;
Texas Medical Center facts (10 million patient encounters, 120,000+ employees).

Research, LinkedIn post: LinkedIn "Maximize your budget" ($10 daily minimum, $30 with Dynamic Group Budget, $100
lifetime minimum); LinkedIn ad bidding tips (auction, relevancy score, maximum delivery / cost cap / manual);
LinkedIn audience page (300-member minimum, 50,000+ recommended for single image and text ads, 15,000+ for message
ads); LinkedIn/Microsoft Learn company list docs (300,000 records per CSV, 300 matched members to serve, 1,000+
companies recommended, 24-48 hours); LinkedIn on Lead Gen Forms (13% average conversion, 3-4 fields recommended,
free-response question drops submissions 3-4%); LinkedIn ads guide (document, thought leader, conversation, event
ads, 12 fields / 3 custom questions); Marketing Week piece by LinkedIn's B2B Institute on the 95:5 rule; Energy
Corridor District employer list (bp, Shell, ConocoPhillips, CITGO and others, 56,000+ jobs); The Real Deal on
Chevron Phillips Chemical's Woodlands HQ move (Research Forest Lakeside, about 950 employees); Huntsman global HQ
page (Woodloch Forest Drive); Community Impact on ExxonMobil's move to its Spring campus; Bisnow on Greenspoint
office vacancy and departures; JPT on OTC and URTeC co-locating May 3-5, 2027 at Reliant Park.
Search phrasing read: "hipaa compliant marketing", "is meta pixel hipaa compliant", "can a dentist respond to
reviews hipaa", "hipaa compliant google analytics", "linkedin ads cost", "linkedin ads for b2b", "linkedin abm",
"are linkedin ads worth it".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # HIPAA post
    "hhs": A("https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html", "HHS OCR’s tracking technologies guidance"),
    "ebg": A("https://www.ebglaw.com/health-law-advisor/ocr-withdraws-appeal-of-district-court-order-declaring-unlawful-and-vacating-the-proscribed-combination-portion-of-its-hipaa-online-tracking-technologies-guidance", "Epstein Becker Green"),
    "hk": A("https://www.hklaw.com/en/insights/publications/2024/06/american-hospital-assn-v-becerra-are-tracking-tools-ok-again", "Holland & Knight’s write-up of the ruling"),
    "ftcletter": A("https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-hhs-warn-hospital-systems-telehealth-providers-about-privacy-security-risks-online-tracking", "joint FTC and HHS letter"),
    "betterhelp": A("https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-ban-betterhelp-revealing-consumers-data-including-sensitive-mental-health-information-facebook", "the FTC’s BetterHelp order"),
    "elite": A("https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/elite/index.html", "Elite Dental Associates in Dallas"),
    "manasa": A("https://www.hhs.gov/about/news/2023/06/05/hhs-office-civil-rights-reaches-agreement-health-care-provider-new-jersey-disclosed-phi-response-negative-online-reviews.html", "Manasa Health Center"),
    "ga": A("https://support.google.com/analytics/answer/13297105?hl=en", "Google’s own HIPAA page for Analytics"),
    "ghealth": A("https://support.google.com/adspolicy/answer/16701855?hl=en", "Google’s health in personalized advertising policy"),
    "metaattr": A("https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-attributes", "Meta’s personal attributes standard"),
    "cardinal": A("https://www.cardinaldigitalmarketing.com/healthcare-resources/blog/meta-announces-major-changes-healthcare-advertising/", "Cardinal Digital Marketing"),
    "sel": A("https://searchengineland.com/meta-ads-restrictions-health-wellness-campaigns-453094", "Search Engine Land"),
    "brew": A("https://marketingbrew.com/stories/2024/12/09/meta-plans-crackdown-on-health-related-user-data", "Marketing Brew"),
    "tob": A("https://tob.texas.gov/protected-health-information-house-bill-300", "Texas Optometry Board’s HB 300 summary"),
    "hj": A("https://www.hipaajournal.com/what-is-texas-hb-300/", "HIPAA Journal"),
    "tx152": A("https://texas.public.law/statutes/tex._health_&_safety_code_section_181.152", "Section 181.152"),
    "tx154": A("https://law.justia.com/codes/texas/health-and-safety-code/title-2/subtitle-i/chapter-181/subchapter-d/section-181-154/", "Section 181.154"),
    "tdpsa": A("https://sll.texas.gov/spotlight/2024/07/texas-data-privacy-and-security-act", "Texas State Law Library"),
    "hhsce": A("https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html", "HHS’s covered entity definition"),
    "tmc": A("https://www.tmc.edu/about-tmc/", "Texas Medical Center"),
    # LinkedIn post
    "libudget": A("https://business.linkedin.com/advertise/ads/best-practices/maximize-your-budget", "LinkedIn’s budget guide"),
    "libid": A("https://business.linkedin.com/advertise/ads/best-practices/ad-bidding-tips", "LinkedIn’s bidding guide"),
    "liaud": A("https://business.linkedin.com/advertise/ads/audience", "LinkedIn’s audience targeting page"),
    "licompany": A("https://learn.microsoft.com/en-us/linkedin/marketing/usecases/matched-audiences/company-lists?view=li-lms-2024-04", "LinkedIn’s company list documentation"),
    "lilgf": A("https://business.linkedin.com/marketing-solutions/blog/best-practices--lead-generation/2017/how-to-use-linkedin-lead-gen-forms", "LinkedIn’s own Lead Gen Forms guide"),
    "liformats": A("https://business.linkedin.com/advertise/ads/ads-guide", "LinkedIn’s ads guide"),
    "li955": A("https://www.marketingweek.com/peter-weinberg-jon-lombardo-95-5-rule", "LinkedIn’s B2B Institute"),
    "ec": A("https://energycorridor.org/energy-corridor-largest-employers/", "Energy Corridor District"),
    "cpchem": A("https://therealdeal.com/texas/houston/2025/07/16/chevron-phillips-chemical-sells-headquarters-in-the-woodlands", "The Real Deal"),
    "huntsman": A("https://www.huntsman.com/locations/detail/6180/the-woodlands-waterway-global-headquarters", "Huntsman’s global headquarters"),
    "exxon": A("https://communityimpact.com/spring-klein/business/exxonmobil-announces-relocation-of-corporate-headquarters-to-city-place-in-spring/", "Community Impact"),
    "bisnow": A("https://www.bisnow.com/news/houston/office/greenspoints-office-market-has-plenty-of-room-and-low-rent-but-few-takers-109174", "Bisnow"),
    "otc": A("https://jpt.spe.org/otc-and-urtec-announce-strategic-co-location-to-accelerate-energy-innovation", "JPT"),
}

HIPAA = "/blog/hipaa-compliant-marketing-healthcare-houston/"
LINKEDIN = "/blog/linkedin-ads-b2b-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: HIPAA rules guide
    {
        "slug": "hipaa-compliant-marketing-healthcare-houston",
        "title": "HIPAA-Compliant Marketing for Houston Healthcare Practices: Pixels, Ads and Reviews",
        "seo_title": "HIPAA-Compliant Marketing for Houston Healthcare",
        "desc": "HIPAA-compliant marketing rules for Houston and The Woodlands practices: OCR pixel guidance, the 2024 ruling, Meta and Google health rules, Texas HB 300.",
        "category": "Strategy",
        "icons": ["Meta", "Google Ads", "Google Analytics"],
        "art": "b2",
        "hero": "shield",
        "hero_alt": "Illustration of a shield for HIPAA-compliant healthcare marketing in Houston and The Woodlands",
        "related": ["medical-practice-marketing-houston", "dental-marketing-the-woodlands-houston", "med-spa-marketing-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Verdict first: you can still run ads, use tracking and ask for reviews as a Houston medical, dental, med spa or therapy practice. What you can’t do is let patient information slide out to Meta or Google while you do it. And since late 2022, the official line on what counts as “sliding out” has moved four times.</p>
<p>Most practice owners got the memo in fragments: a vendor email about “HIPAA-safe pixels,” a Meta notice about restricted events, a colleague in the Texas Medical Center who heard a court “struck down the pixel rule.” Each is partly true, which is how practices end up either afraid of all marketing or careless because they think the rules went away.</p>
<p>This is a rules guide. Each rule gets what it says, what it means for your website and ads, and a Houston example. It’s written for owners and office managers from the Medical Center to Market Street in The Woodlands, and for the marketing people who work for them.</p>
<p><b>Not legal advice.</b> We’re marketers. We read the guidance, the policies and the enforcement actions closely because we have to build campaigns around them, but your situation depends on facts we can’t see. Run your setup past a healthcare attorney or your compliance officer before you change it.</p>"""),

            ("Is HIPAA-compliant marketing possible in Houston? The short answer", f"""<p>Yes. HIPAA-compliant marketing for a Houston practice means keeping ad pixels and Google Analytics off patient portals, booking flows and intake forms; using vendors that sign a business associate agreement for anything touching patient data; writing ads that never imply the viewer has a condition; and answering reviews without confirming anyone is a patient.</p>
<p>The rules behind that answer come from at least seven places, including a Texas layer most national articles skip, and they don’t all apply to the same businesses.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Rule</th><th>Who it applies to</th><th>What it means for your marketing</th></tr></thead>
<tbody>
<tr><td>HIPAA Privacy Rule and the OCR tracking guidance</td><td>Covered entities (most practices that bill insurance electronically) and their vendors</td><td>No patient data to ad or analytics vendors without a BAA or patient authorization. Portals, booking and intake are the danger zone.</td></tr>
<tr><td><i>AHA v. Becerra</i> (N.D. Tex., June 20, 2024)</td><td>Everyone the guidance covered</td><td>Threw out the theory that an IP address plus a visit to a public condition page is automatically PHI. The rest of the guidance stands.</td></tr>
<tr><td>FTC Act and Health Breach Notification Rule</td><td>Health businesses HIPAA doesn’t reach, like many cash-pay med spas and apps</td><td>Sharing health data with ad platforms without clear consent can be deceptive or unfair. BetterHelp paid $7.8 million.</td></tr>
<tr><td>Texas Health &amp; Safety Code Ch. 181 (HB 300)</td><td>A much broader “covered entity” than HIPAA’s</td><td>Marketing authorization, staff training within 90 days, electronic disclosure notice, penalties up to $250,000 per violation.</td></tr>
<tr><td>Texas Data Privacy and Security Act</td><td>Businesses not regulated by HIPAA; small businesses mostly exempt</td><td>“Health condition” is sensitive data. Even small businesses need consent to sell it.</td></tr>
<tr><td>Google Ads health in personalized advertising</td><td>Anyone advertising sensitive health topics</td><td>No Customer Match, remarketing lists, lookalikes or audience expansion on those ads.</td></tr>
<tr><td>Meta ad standards and health data restrictions</td><td>Every Facebook and Instagram advertiser in health and wellness</td><td>No ads that imply a viewer’s condition. Restricted accounts lose lower-funnel optimization from website events.</td></tr>
<tr><td>HIPAA and review responses</td><td>Covered entities</td><td>Never confirm someone is a patient in a public reply. Two OCR settlements so far, one of them in Dallas.</td></tr>
</tbody></table></div>"""),

            ("Rule 1: The OCR tracking guidance, and the part a Texas court threw out", f"""<p><b>What it says.</b> HHS’s Office for Civil Rights published its bulletin on tracking technologies in late 2022 and updated it in March 2024. The core sentence hasn’t changed: regulated entities are not permitted to use tracking technologies in a way that results in impermissible disclosures of PHI to tracking vendors. A vendor that receives PHI on your behalf is a business associate whether or not anyone signed a BAA. A line in your privacy policy isn’t enough, and per {SRC['hhs']}, a cookie banner asking visitors to accept tracking is not a HIPAA authorization.</p>
<p>In July 2023 the FTC and OCR sent a {SRC['ftcletter']} to about 130 hospital systems and telehealth providers naming the Meta pixel and Google Analytics specifically. That’s when a lot of Houston health systems quietly stripped tags from their sites.</p>
<p><b>What the court changed.</b> The American Hospital Association sued in the Northern District of Texas. On June 20, 2024, the court vacated one piece of the guidance, which OCR called the “proscribed combination”: the idea that an IP address connected to a visit on a public, unauthenticated page about a specific condition or provider is enough to trigger HIPAA. OCR appealed to the Fifth Circuit, then withdrew the appeal on August 29, 2024, per {SRC['ebg']}. {SRC['hk']} has more on the reasoning.</p>
<!--fig:timeline-->
<p><b>What it means in practice.</b> Your public pages about knee replacement or Invisalign are in much safer territory than they were in 2023. Everything else in the guidance is still live. OCR still says tracking on user-authenticated pages (patient portals, telehealth logins) generally has access to PHI. Scheduling tools and symptom checkers can collect PHI. A login page is public, but the credentials typed into it are identifiable information. Mobile apps a practice offers generally collect PHI, device IDs included.</p>
<p>The court did nothing for the booking widget that fires a “Schedule” event to Meta with the service name and a hashed patient email in the payload. That one is still the problem.</p>
<!--fig:pages-->
<p>A Houston example: a cardiology group near the Texas Medical Center has a public “AFib treatment” page with a Meta pixel, linking to online booking on the same domain. The page itself is now lower risk. The booking flow, the intake questions and the “Your AFib consult is confirmed” page are where the pixel has to stop.</p>"""),

            ("Rule 2: Is the Meta Pixel HIPAA compliant?", f"""<p>Not on its own, and not on any page where patient information is in play. Meta’s ad tools aren’t offered as a HIPAA service with a BAA you can sign, so treat any PHI that reaches Meta through the pixel or Conversions API as a disclosure with no agreement behind it.</p>
<p>Meta has also built its own fence, separate from HIPAA. Starting in January 2025, Meta began restricting what health and wellness advertisers can send and optimize for, after categorizing data sources late in 2024, according to {SRC['cardinal']}. {SRC['sel']} describes three tiers:</p>
<ul>
<li><b>Core Setup.</b> Custom parameters and the parts of URLs after the domain stop being shared, and automatic advanced matching may be unavailable.</li>
<li><b>Restricted standard events.</b> Mid- and lower-funnel events like purchase and add to cart can’t be used for optimization. Landing page views, view content and custom events still work.</li>
<li><b>Full restriction.</b> Meta says it “may fully restrict all events in specific regions or all regions,” which leaves you with targeting and upper-funnel optimization only.</li>
</ul>
<p>Check yours in Events Manager, under the data source’s Settings tab. If Meta miscategorized you, you can request a review.</p>
<!--fig:metatiers-->
<p>Two things practices miss. First, Meta’s categories don’t follow HIPAA’s. A cash-pay med spa in The Woodlands that isn’t a HIPAA covered entity can still land in a restricted tier. {SRC['brew']} reported on a memo suggesting medical Botox (for migraines) could be restricted while cosmetic Botox might not be. Second, lead ads that run entirely inside Facebook and Instagram appear unaffected so far, per Cardinal, because the form data is generated within Meta. That makes instant forms the most workable conversion path for many Houston practices right now. Keep the questions to name, phone, email and preferred location; a dropdown asking which condition brings them in is the wrong instinct.</p>
<p>Then there’s the creative. {SRC['metaattr']} bans ads that assert or imply personal attributes, physical and mental health included. Meta’s own examples: “Do you have diabetes?” and “Depression getting you down? Get help now.” For a therapy practice in Sugar Land, “Anxiety therapy in Sugar Land, evening appointments, most plans accepted” is fine. “Is anxiety running your life?” gets rejected, and it should.</p>"""),

            ("Rule 3: Can a medical practice use Google Analytics and Google Ads?", f"""<p>Yes, with limits on both. Start with Analytics. {SRC['ga']} says Google doesn’t offer a BAA for it, that authenticated pages are likely HIPAA-covered and shouldn’t carry GA tags, and that HIPAA-regulated customers must not use GA in any way that gives Google access to PHI. That’s Google telling you where the line is, in writing.</p>
<p>In practice: GA4 on public pages, never on the portal, the booking steps or a confirmation URL that names a service. If your booking tool appends <code>?service=botox&amp;provider=dr-lee</code> to the URL, that string goes to Google with every page view.</p>
<p>Now Google Ads. Keyword-targeted search is the cleanest channel in healthcare: “pediatric dentist The Woodlands” tells you what the person wants without you needing to know who they are.</p>
<p>The restriction is on audiences. {SRC['ghealth']} says advertiser-curated audiences (Customer Match, your data segments, lookalike segments and audience expansion) can’t be used on ads promoting sensitive health content, which Google gives examples of: STD treatment, mental health counseling for depression, anxiety and addiction, pregnancy and infertility treatment. Predefined Google audiences and location targeting are still allowed. Uploading your patient list to Customer Match is a bad idea under HIPAA anyway, since a list of your patients is itself PHI.</p>
<p>For conversion tracking, count actions without sending patient detail. A call from the ad, a click on the “Book” button, a generic “appointment request started” event. We cover the mechanics in our guide to {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking forms and calls in GA4 and Google Ads')}; for healthcare, strip anything clinical from the event names and parameters before you follow it.</p>"""),

            ("Rule 4: Server-side tracking fixes the plumbing, not the law", f"""<p>Server-side tracking is the most oversold product in healthcare marketing right now. Here’s what it actually does.</p>
<p>With normal tags, the visitor’s browser talks straight to Meta and Google. With a server-side setup, the browser talks to a server you control, and that server decides what to forward. That’s useful, because you can strip IP addresses, drop URL paths, rename events and refuse to forward anything from the booking flow.</p>
<p>What it doesn’t do is change what counts as a disclosure. If your server forwards “appointment booked, cardiology, this hashed email” to Meta, you disclosed PHI to Meta, just with extra steps. OCR’s guidance points to the legitimate version: a customer data platform or tracking vendor that signs a BAA with you, receives the data, and de-identifies it before anything goes to an ad platform. OCR also notes that a vendor de-identifying data after receiving it doesn’t cure a disclosure that had no BAA behind it.</p>
<p>Our rule for Houston practices is simple. If a vendor sells you “HIPAA-compliant tracking,” ask three things: will they sign a BAA, exactly which fields leave their server for Meta and Google, and can they show you the outbound payload. If any answer is vague, keep shopping.</p>
<p>A cheaper path works for many small practices: no ad pixels past the homepage and service pages, Meta lead ads for social, call tracking under a BAA, and keyword-targeted search. You lose some optimization and a whole category of risk. For a three-provider dental office in Spring, that trade usually makes sense.</p>"""),

            ("Rule 5: Texas HB 300 is stricter than HIPAA in ways marketers feel", f"""<p>Texas passed HB 300 in 2011, amending Chapter 181 of the Health and Safety Code (the Texas Medical Records Privacy Act). It sits on top of HIPAA. Three parts matter for marketing.</p>
<p><b>The covered entity definition is broad.</b> The {SRC['tob']} calls it “very broad.” It reaches anyone who assembles, stores, or comes into possession of Texas residents’ PHI, which can include billing companies, IT vendors and marketing agencies, plus practices that never bill insurance.</p>
<p><b>Marketing needs authorization.</b> Under {SRC['tx152']}, a covered entity generally needs a patient’s written or electronic authorization before using or disclosing PHI for marketing, with narrow exceptions (face-to-face communication, nominal promotional gifts, communication the patient orally requested). Marketing sent by mail must go in an envelope showing only names and addresses, identify the sender, include a toll-free number, and explain how to get off the list. Removal requests must be honored within 45 days.</p>
<p><b>Electronic disclosure needs notice and authorization.</b> {SRC['tx154']} requires notice to patients whose PHI is subject to electronic disclosure, and generally a separate authorization for each electronic disclosure outside treatment, payment, operations and a few other exceptions.</p>
<p>Add the training requirement (staff trained within 90 days of hire and again when the law changes their duties) and the penalties. {SRC['hj']} lists civil penalties of up to $5,000 per violation for negligence, $25,000 for knowing or intentional violations, and $250,000 for intentional violations for financial gain, with up to $1.5 million a year for a pattern. The Texas Attorney General enforces, and licensing boards can discipline on top.</p>
<!--fig:texas-->
<p>What we’d do about it: add a plain-language marketing consent checkbox to new-patient intake (unchecked by default), keep a record of it in the practice management system, and send promotional email or texts only to patients who checked it. Whether a particular appointment-reminder text or a recall email counts as “marketing” under Texas law is a question for your attorney. Getting consent up front makes most of those questions go away.</p>"""),

            ("Does HIPAA apply to a med spa or a cash-pay clinic?", f"""<p>Sometimes not, and people get excited about that too early. Under {SRC['hhsce']}, a health care provider is a HIPAA covered entity only if it transmits health information electronically in connection with standard transactions, which mostly means billing insurance. A cash-only med spa in The Woodlands or an IV hydration lounge in Katy may fall outside HIPAA.</p>
<p>It doesn’t fall outside everything else:</p>
<ul>
<li>Texas Chapter 181’s broader definition can still reach it.</li>
<li>The FTC Act applies. BetterHelp wasn’t a HIPAA entity either, and {SRC['betterhelp']} required it to pay $7.8 million after it shared email addresses, IP addresses and intake questionnaire answers with Facebook and others for advertising, despite promising privacy.</li>
<li>The Texas Data Privacy and Security Act took effect July 1, 2024. It exempts HIPAA-regulated organizations and most small businesses, but per the {SRC['tdpsa']}, “health condition” is sensitive data and even a small business needs consent to sell it.</li>
<li>Meta’s restrictions apply based on Meta’s categories, not your legal status.</li>
</ul>
<p>So a med spa should run the same playbook as a dental office, with slightly more freedom on creative. Before-and-after photos need written patient consent regardless; our {L('/blog/med-spa-marketing-the-woodlands-houston/', 'med spa marketing guide')} covers the rest of the channel mix.</p>"""),

            ("Rule 6: Can a dentist or doctor respond to Google reviews?", f"""<p>Yes, as long as the reply never confirms that the reviewer is a patient or mentions anything about their care. This is the rule practices break most often, usually at 10 p.m., right after reading a one-star review that isn’t fair.</p>
<p>OCR has settled at least two review cases. {SRC['elite']} paid $10,000 in 2019 after responding to Yelp reviews with patient information. In 2023, {SRC['manasa']}, a New Jersey psychiatric practice, paid $30,000 after a reply to a negative review included the patient’s mental health diagnosis and treatment, and OCR found three more patients’ information in other replies. OCR’s director put it bluntly: “Simply put, this is not allowed.”</p>
<!--fig:penalties-->
<p>A reply that works for almost any review, good or bad:</p>
<p><i>“Thank you for taking the time to write this. Our privacy obligations mean we can’t discuss anyone’s care online, but we take every concern seriously. Please call our office manager at [your number] and we’ll talk it through.”</i></p>
<p>For a five-star review, resist “So glad your implant healed well, Maria!” That sentence confirms she’s a patient and names her treatment. “Thank you, we really appreciate this” is plenty.</p>
<!--fig:reviewrules-->
<p>Asking for reviews is fine. Keep the request generic (“Thanks for visiting us today, would you share a quick review?”) and send it only to patients who agreed to receive texts. Don’t offer anything in exchange; the FTC’s review rule covers that, and our post on the {L('/blog/fake-reviews-rule-local-businesses/', 'fake reviews rule')} explains it. The rest of the review process is in our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')}.</p>"""),

            ("What’s still safe for Houston and The Woodlands practices", f"""<p>After all those rules, here’s what we’d happily run tomorrow for a practice anywhere from the Medical Center to Conroe.</p>
<ul>
<li><b>Medical.</b> A specialist group with offices near the Texas Medical Center and in The Woodlands runs keyword search campaigns per location (“orthopedic surgeon The Woodlands,” “sports medicine near Hughes Landing”), with call tracking and a booking button tracked as a click. The {SRC['tmc']} reports about 10 million patient encounters a year, so a lot of north-side patients search for a closer option first.</li>
<li><b>Dental.</b> A Woodlands family dental office runs Google search, Business Profile posts and three-field Meta lead ads for new-patient exams, with no pixel on the booking widget.</li>
<li><b>Med spa.</b> A Market Street area med spa runs Meta lead ads and Instagram creative showing the space, the injectors and pricing, with consented before-and-afters on the website only. Retargeting limited to video viewers and page engagers on Meta.</li>
<li><b>Therapy.</b> A group practice in Sugar Land and the Heights runs search ads on service plus location, writes ads about format and availability (telehealth, evenings, insurance) and never about the viewer’s state of mind. Website analytics on public pages only.</li>
</ul>
<p>SEO is the quiet winner here. A strong service page for “TMJ treatment Spring TX” doesn’t require any tracking of who reads it. Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} builds those, and the {L('/blog/medical-practice-marketing-houston/', 'medical practice marketing guide')}, {L('/blog/dental-marketing-the-woodlands-houston/', 'dental guide')} and {L('/blog/therapist-counseling-practice-marketing-houston/', 'therapist guide')} cover each specialty’s channel mix.</p>"""),

            ("A 30-day cleanup plan for your practice website and ads", f"""<p>If you’ve read this far and suspect your site is leaking, this is the order we’d fix it in.</p>
<!--fig:cleanup-->
<p>The inventory is where the surprises are. Run a tag scanner (or your browser’s developer tools) on the homepage, a service page, the booking flow and the confirmation page. Most practices find tags nobody remembers: an old pixel from a previous agency, a chat widget, a heatmap tool recording form fields. Vendors that touch PHI usually include the booking tool, call tracking, the CRM and the email platform, so those are the BAAs to chase first.</p>
<p>If you want help, our {L('/services/search-marketing/', 'search marketing team')} sets up healthcare campaigns around these limits. Tell us about your practice and your goals and <a href="/contact/">get in touch</a>; a senior strategist will build a plan that fits your specialty and your compliance setup.</p>"""),
        ],
        "faq": [
            ("Is it legal to use Facebook ads for a medical practice in Houston?",
             "Yes. Facebook and Instagram ads are legal for medical practices, but the ads can’t imply the viewer has a condition, and the Meta pixel shouldn’t fire on booking, intake or portal pages where patient information is present. Many Houston practices now rely on Meta lead ads, which keep form data inside Meta. Check Events Manager to see whether Meta has placed your data source in a restricted health category."),
            ("Did the 2024 court ruling make tracking pixels HIPAA compliant?",
             "No. The June 2024 ruling in AHA v. Becerra vacated only the part of OCR’s guidance that treated an IP address plus a visit to a public condition page as protected health information. OCR still says tracking on patient portals, scheduling tools, symptom checkers and practice apps can disclose PHI, and a vendor receiving PHI needs a business associate agreement or patient authorization."),
            ("Does a med spa in The Woodlands have to follow HIPAA?",
             "It depends on billing. A provider is a HIPAA covered entity if it conducts standard electronic transactions, mostly insurance billing, so some cash-only med spas fall outside HIPAA. They still face Texas Chapter 181, which defines covered entities more broadly, plus the FTC Act and Meta’s own health data restrictions. Ask a healthcare attorney to confirm your status before relaxing anything."),
            ("What should a Texas dental office say when replying to a negative Google review?",
             "Say nothing that confirms the reviewer is a patient or describes their care. A safe reply thanks them, says privacy rules prevent discussing anyone’s care online, and invites them to call the office manager directly. A Dallas dental practice paid OCR $10,000 in 2019 over review responses, so write a standard script and make sure everyone who can reply uses it."),
            ("Is Google Analytics 4 allowed on a healthcare website in Texas?",
             "On public pages, generally yes, with care. Google says it won’t sign a business associate agreement for Analytics and tells HIPAA-regulated customers to keep tags off authenticated pages and avoid any use that gives Google access to PHI. Keep GA4 off portals, booking steps and confirmation pages, and keep service names and patient details out of URLs and event parameters."),
        ],
        "figures": {
            "timeline": {
                "type": "steps",
                "title": "How the pixel rules moved, 2022 to 2025",
                "sub": "The guidance Houston practices have been reacting to",
                "steps": [["Late 2022", "OCR bulletin: tracking that discloses PHI to vendors is impermissible."], ["July 2023", "FTC and OCR warn about 130 hospitals and telehealth providers by letter."], ["March 2024", "OCR updates the bulletin with more examples."], ["June 20, 2024", "Texas federal court vacates the IP-plus-public-page theory."], ["Aug. 29, 2024", "OCR drops its appeal. The rest of the guidance stands."], ["January 2025", "Meta starts restricting health advertisers’ data and events."]],
                "alt": "Timeline of HIPAA tracking pixel guidance and the 2024 Texas ruling for Houston and The Woodlands healthcare marketing",
                "caption": f"Dates from {SRC['hhs']}, the FTC and Epstein Becker Green; Meta timing per Cardinal Digital Marketing.",
            },
            "pages": {
                "type": "compare",
                "title": "Where ad pixels can and can’t go on a practice site",
                "left": {"title": "Keep ad and analytics tags off", "items": ["Patient portal and telehealth login", "Online booking steps", "Intake and new-patient forms", "Symptom checkers and quizzes", "Confirmation pages naming a service"]},
                "right": {"title": "Lower risk after the 2024 ruling", "items": ["Homepage and location pages", "General service pages", "Team, careers, visiting hours", "Blog articles", "Contact page without free-text health fields"]},
                "alt": "Comparison of website pages where tracking pixels are risky versus lower risk for Houston and The Woodlands medical practices",
                "caption": "Lower risk still isn’t zero. Strip URL query strings and form-field capture everywhere.",
            },
            "metatiers": {
                "type": "funnel",
                "title": "What a restricted health advertiser can still optimize for on Meta",
                "stages": [["Reach and impressions", "Available"], ["Landing page views", "Available"], ["View content and custom events", "Usually available"], ["Leads and purchases from site events", "Blocked when restricted"], ["Meta lead ads (instant forms)", "Unaffected so far"]],
                "note": "Tiers vary by advertiser and region; check Events Manager",
                "alt": "Funnel of Meta health and wellness ad optimization limits for Houston and The Woodlands healthcare practices",
                "caption": f"Summarized from {SRC['sel']} and Cardinal Digital Marketing.",
            },
            "texas": {
                "type": "map",
                "title": "Texas privacy law follows the patient",
                "sub": "Chapter 181 applies the same in the Medical Center, The Woodlands and Conroe",
                "highlight": ["Houston", "The Woodlands", "Conroe", "Katy", "Sugar Land", "Pearland", "Kingwood", "Cypress"],
                "alt": "Map of Greater Houston showing Texas HB 300 medical privacy rules apply to practices in Houston, The Woodlands, Katy and Sugar Land",
                "caption": "Chapter 181 covers anyone handling Texas residents’ PHI, wherever the business sits. Telehealth included.",
            },
            "penalties": {
                "type": "stats",
                "title": "What getting it wrong has cost",
                "stats": [["$10K", "Elite Dental, Dallas: review replies (2019)"], ["$30K", "Manasa Health: review replies (2023)"], ["$7.8M", "BetterHelp: health data to ad platforms"], ["$250K", "Texas Ch. 181 max per violation"]],
                "alt": "Stats on HIPAA and Texas HB 300 penalties relevant to healthcare marketing in Houston and The Woodlands",
                "caption": "From HHS resolution agreements, the FTC, and HIPAA Journal’s summary of Chapter 181.",
            },
            "reviewrules": {
                "type": "checklist",
                "title": "Review reply rules for Houston practices",
                "sub": "Post this next to whoever answers your reviews",
                "items": ["Never confirm the reviewer is a patient", "Never mention a treatment, visit date or provider", "Don’t correct their account of what happened", "Use one approved reply for complaints", "Move the conversation to a phone call", "Thank five-star reviewers without details", "Ask for reviews generically, with no incentive", "Have the office manager approve every reply"],
                "alt": "Checklist of HIPAA-safe review response rules for dental and medical practices in Houston and The Woodlands",
                "caption": "The urge to set the record straight is exactly how the OCR settlements happened.",
            },
            "cleanup": {
                "type": "steps",
                "title": "A 30-day tracking cleanup",
                "sub": "In the order we’d do it",
                "steps": [["Week 1: inventory", "List every third-party tag on key pages and flows."], ["Week 2: remove", "Pull tags from portal, booking, intake, confirmation."], ["Week 3: vendors", "Get BAAs from anyone touching PHI. Drop refusers."], ["Week 4: rebuild", "Non-clinical conversions, Texas consent, review script."], ["Every 6 months", "Rescan. Plugins and vendors change."]],
                "alt": "Five-step plan to clean up website tracking for HIPAA-compliant marketing at Houston and The Woodlands practices",
                "caption": "Have your attorney or compliance officer sign off on step four before you relaunch ads.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: LinkedIn Ads playbook
    {
        "slug": "linkedin-ads-b2b-houston",
        "title": "LinkedIn Ads for Houston B2B Companies: Energy, Industrial and Professional Services",
        "seo_title": "LinkedIn Ads for Houston B2B: Energy & Industrial",
        "desc": "A LinkedIn Ads playbook for Houston and The Woodlands B2B firms: targeting, real costs, Lead Gen Forms, ABM company lists, OTC timing, when to skip it.",
        "category": "Paid ads",
        "icons": ["LinkedIn", "HubSpot", "Google Analytics"],
        "art": "b1",
        "hero": "industry",
        "hero_alt": "Illustration of industrial facilities for LinkedIn Ads for B2B companies in Houston and The Woodlands",
        "related": ["b2b-marketing-houston-energy-industrial", "trade-show-marketing-houston-otc-conventions", "speed-to-lead-response-time-follow-up-crm"],
        "sections": [
            (None, f"""<p>Ten dollars a day. That’s LinkedIn’s minimum daily budget, and it’s the most misleading number on the platform for a Houston B2B company.</p>
<p>At ten dollars a day you’ll get a trickle of clicks from people who look right on paper, a report full of impressions, and no way to tell whether anything happened. Then someone in the Monday meeting says “we tried LinkedIn, it didn’t work,” and the company goes back to trade shows and golf.</p>
<p>LinkedIn can be the best paid channel a Houston energy services firm, industrial manufacturer or professional services firm has. It’s also the easiest to waste money on. This is a playbook: seven plays in the order we’d run them, with the real platform limits, honest cost math, and the situations where we’d tell you to spend the money somewhere else.</p>"""),

            ("Is LinkedIn advertising worth it for B2B companies in Houston?", f"""<p>Usually, if three things are true: one closed deal is worth $50,000 or more over its life, your buyers can be identified by company and job title, and you can fund at least $3,000 to $5,000 a month for a full quarter. Below that, or for fast transactional sales, Google search and direct outreach usually return more per dollar.</p>
<p>That threshold is our judgment, not a LinkedIn rule. It comes from how the math works when clicks are expensive and sales cycles run six to eighteen months, which is normal for anyone selling to operators, EPCs or chemical plants along the Ship Channel.</p>
<p>LinkedIn’s own research arm makes the same point from a different angle. The 95:5 rule, popularized by {SRC['li955']} and based on work by John Dawes at the Ehrenberg-Bass Institute, holds that about 95% of B2B buyers are out of the market at any given time. LinkedIn is where you stay familiar to the 95% so you’re on the shortlist when they come back in. If you need the 5% this month, that’s a search problem.</p>"""),

            ("Play 1: Build the account list before you touch targeting", f"""<p>Most Houston B2B campaigns start in Campaign Manager’s targeting menu, picking “Oil and Gas” and “Director” and hoping. Start with a spreadsheet instead. Name the 300 to 3,000 companies you’d actually like to sell to, then upload them.</p>
<p>The mechanics, from {SRC['licompany']}: a company list CSV can hold up to 300,000 records, LinkedIn matches it against its company pages, it takes 24 to 48 hours to be ready, and it can serve once the list reaches 300 matched members. LinkedIn recommends at least 1,000 companies for best results. Include the company website and LinkedIn page URL columns where you have them; names alone match poorly for companies with common words or lots of subsidiaries.</p>
<!--fig:abmsteps-->
<p>Houston’s corporate geography matters here, because it tells you where buying committees actually sit.</p>
<ul>
<li><b>Energy Corridor.</b> The {SRC['ec']} lists bp, Shell, ConocoPhillips, CITGO, Baker Hughes, Fluor, Kiewit, McDermott, Enbridge and SBM Offshore among its largest employers, with more than 56,000 jobs in and around the district.</li>
<li><b>The Woodlands.</b> Chevron Phillips Chemical consolidated its global headquarters into the Research Forest Lakeside campus, bringing together nearly 950 employees, per {SRC['cpchem']}. {SRC['huntsman']} is on Woodloch Forest Drive near Waterway Square.</li>
<li><b>Spring.</b> ExxonMobil moved its corporate headquarters from Irving to its 385-acre campus at City Place (the former Springwoods Village), reported by {SRC['exxon']}.</li>
<li><b>Greenspoint.</b> It used to be on every energy target list. ExxonMobil, Noble Energy and Southwestern Energy all left, and {SRC['bisnow']} reported direct office vacancy around 42% in 2021. Today it’s mostly mid-size tenants, so target Greenspoint companies by name and industry, not by assuming a big operator is still there.</li>
</ul>
<!--fig:map-->
<p>One trap with big operators: a company list targets the whole company. Upload Shell and you reach Shell employees in the Netherlands, Singapore and Louisiana. Layer a location (Houston metro, or Texas plus Louisiana for Gulf Coast work) unless global reach is the point. And split your list into tiers. Your top 50 accounts deserve their own campaign and their own creative.</p>"""),

            ("Play 2: Layer job function and seniority, then check audience size", f"""<p>Once the company list is in, narrow it by the people who sign or influence the purchase. The options LinkedIn names on {SRC['liaud']} include job title, skills, years of experience, company and firmographics, plus matched audiences and audience expansion. In Campaign Manager you’ll also find job function, seniority, industry and company size.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Targeting option</th><th>What it does</th><th>Houston B2B use</th><th>Watch out for</th></tr></thead>
<tbody>
<tr><td>Company list</td><td>Your uploaded target accounts</td><td>Operators, EPCs, midstream companies, plant owners you want as clients</td><td>Global reach unless you add location</td></tr>
<tr><td>Job function</td><td>Broad departments like Engineering, Operations, Purchasing</td><td>Engineering plus Operations for equipment; Finance for advisory firms</td><td>Too broad without seniority</td></tr>
<tr><td>Seniority</td><td>Entry through CXO</td><td>Manager, Director, VP for most industrial sales</td><td>Exclude Entry, Training and Unpaid</td></tr>
<tr><td>Job title</td><td>Specific titles members list</td><td>“Reliability Engineer,” “Turnaround Manager,” “HSE Director”</td><td>Titles vary wildly; audiences get tiny</td></tr>
<tr><td>Industry</td><td>Company’s listed industry</td><td>Oil and Gas, Chemical Manufacturing, Utilities</td><td>Service firms list themselves inconsistently</td></tr>
<tr><td>Company size</td><td>Employee count bands</td><td>Mid-market fabricators vs. majors</td><td>Size counts global staff</td></tr>
<tr><td>Contact list</td><td>Your uploaded emails</td><td>Past OTC booth scans, CRM lists, webinar attendees</td><td>Needs 300 matched members to serve</td></tr>
<tr><td>Audience expansion</td><td>Adds similar members</td><td>Rarely, for broad awareness</td><td>Turn it off for ABM</td></tr>
</tbody></table></div>
<p>Check the audience size before launch. LinkedIn’s minimum is 300 members; its recommendation is 50,000 or more for single image and text ads and 15,000 or more for message ads. A focused Houston ABM audience often lands between 5,000 and 30,000, under the recommendation. That’s fine. You’ll pay higher costs for a narrower audience, and you’ll know exactly who you’re paying to reach.</p>
<p>We’d also turn off the LinkedIn Audience Network on ABM campaigns, which extends ads to third-party sites and apps. It’s useful for reach, and murky for an account list where you want to know your ads appeared on LinkedIn itself. Exclude your own employees and your competitors by company name.</p>"""),

            ("How much do LinkedIn ads cost for Houston B2B companies?", f"""<p>Here’s what LinkedIn actually publishes. Per {SRC['libudget']}, the minimum daily budget is $10 for any ad format ($30 per campaign when you use Dynamic Group Budget), and new campaigns need a minimum lifetime budget of $100. Costs come from an auction: per {SRC['libid']}, winning takes “a good relevancy score and an appropriate bid,” and you choose maximum delivery (LinkedIn’s default), cost cap or manual bidding.</p>
<!--fig:costs-->
<p>LinkedIn doesn’t publish average CPCs, and the third-party averages you’ll find vary so much they’re not worth quoting. What we can tell you is that narrow, senior audiences cost more than broad ones, ABM audiences under the recommended size cost more still, and energy and finance titles are among the more contested. Plan with an assumption and replace it with your own numbers after 30 days.</p>
<p>Here’s how we’d sketch it for a Woodlands industrial services company with a $5,000 monthly test.</p>
<!--fig:budget-->
<p>The point of the sketch is the shape. Five thousand dollars might produce one or two real opportunities a month after a ramp-up period. If your average contract is $200,000, that’s a great channel. If it’s $8,000, it isn’t, and no amount of optimization will fix the gap.</p>
<p>Budget rules we’d follow: run at least a quarter before judging, keep 70% or more on your target account list, and don’t split $3,000 across six campaigns. Two or three campaigns with enough budget to produce real data beat a dozen starved ones. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston Google Ads CPC benchmarks')} are a useful comparison when you’re deciding how to split money between the two.</p>"""),

            ("Play 3: Use Lead Gen Forms, with one question that filters", f"""<p>Lead Gen Forms open inside LinkedIn, pre-filled with the member’s name, email, company, title and location. {SRC['lilgf']} puts the average conversion rate at 13%, against 4.02% for landing pages in an Unbounce study it cites. It recommends three or four fields, and warns that a single free-response question can cut submissions by 3 to 4 percent. Forms allow up to 12 fields and three custom questions.</p>
<p>The catch is the same convenience that drives the 13%. Pre-filled forms take one tap, so you get people who were curious for one second. The fix is one multiple-choice qualifying question that a serious buyer answers easily and a casual one has to think about:</p>
<ul>
<li>An industrial valve distributor: “When is your next turnaround or major maintenance window?” (Next 6 months / 6-12 months / Not scheduled)</li>
<li>An engineering firm: “What stage is the project in?” (Feasibility / FEED / Detailed design / Construction)</li>
<li>A Houston law or accounting firm: “What’s driving the question?” (Acquisition / Dispute / Compliance / Just researching)</li>
</ul>
<p>“Just researching” is a valid answer. Those people go into nurture, not to a salesperson’s phone.</p>
<!--fig:lgf-->
<p>Connect the form to your CRM so leads don’t sit in a CSV. LinkedIn integrates with HubSpot, Salesforce and others, and the first call should happen within the hour. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} explains why that hour matters even in slow B2B cycles.</p>"""),

            ("Play 4: Pick formats engineers and operators actually stop for", f"""<p>{SRC['liformats']} lists the formats. The ones we’d use for Houston energy and industrial buyers:</p>
<ul>
<li><b>Document ads.</b> A PDF, DOCX or PPTX previewed in the feed, up to 300 pages. Spec sheets, case studies, a one-page capability statement. You can let people read a few pages and gate the rest with a Lead Gen Form.</li>
<li><b>Thought Leader Ads.</b> Sponsored posts from a real person at your company. A short post from your VP of Engineering about what failed on a project and what you changed will outperform a polished brand ad for most technical audiences, and it reads like LinkedIn instead of an ad.</li>
<li><b>Video.</b> A 45-second shop-floor or job-site clip with captions. Engineers like seeing the actual equipment.</li>
<li><b>Conversation Ads.</b> Messages with up to five buttons, good for routing people (“Book a meeting at OTC” / “Get the spec sheet” / “Talk to an engineer”). Use them sparingly; inbox ads wear out fast.</li>
<li><b>Event Ads.</b> For your own webinar or an event at your booth.</li>
</ul>
<p>Sample copy for a Houston fabrication shop, single image ad: <i>“ASME-certified pressure vessel fabrication in north Houston. 14 weeks from approved drawings to delivery on our last three jobs. See the spec sheet.”</i> Replace the numbers with your real ones. Specific claims a reader can check are what work with engineers.</p>
<p>And for a professional services firm in The Woodlands: <i>“Selling an energy services company in the next two years? Our checklist covers the 11 things buyers’ diligence teams ask for first.”</i> That one runs as a document ad with a two-page preview.</p>"""),

            ("Play 5: Time your spend around OTC", f"""<p>Houston’s B2B calendar has one big spike. OTC and URTeC will co-locate May 3 to 5, 2027 at Reliant Park, per {SRC['otc']}, which puts a big share of offshore and unconventional buyers in one place in the same week.</p>
<p>LinkedIn is the best tool we know for booking meetings before a show. We’d weight spend like this:</p>
<!--fig:otc-->
<p>Eight weeks out, run awareness to your target account list (document ads, Thought Leader posts). Three to four weeks out, switch to a meeting ask: “We’re at booth [number], here’s what we’re showing, grab 20 minutes.” Show week, keep a light campaign running so the name stays in feeds, and put your reps’ Thought Leader posts in front of the list. For two to six weeks after, upload booth scans as a contact list and retarget them with the case study they asked about.</p>
<p>Then cut spend in June and July, when attention drops and the target list has seen your ads a dozen times. Restart in late August as budgets get planned. Our {L('/blog/trade-show-marketing-houston-otc-conventions/', 'trade show marketing guide')} covers the booth side and the venue-level geofencing that LinkedIn can’t do.</p>"""),

            ("Play 6: Retarget, then measure pipeline instead of clicks", f"""<p>Install the LinkedIn Insight Tag on your site and build retargeting audiences from website visitors, video viewers, document ad readers and people who opened a Lead Gen Form without submitting. These are small in Houston B2B, often a few hundred people, which is exactly why they convert. Our {L('/blog/retargeting-explained/', 'retargeting explainer')} covers the basics.</p>
<p>Measurement is where LinkedIn programs live or die. Click-through rate and cost per lead are easy to report and nearly useless on their own. The metrics we’d put in front of a Houston CEO:</p>
<ul>
<li>Target accounts reached and engaged (by account, not by person)</li>
<li>Sales-accepted leads and meetings booked, by campaign</li>
<li>Opportunities and pipeline value where the account engaged with ads in the prior 90 days</li>
<li>Closed revenue, two to four quarters later</li>
</ul>
<p>Tie it together in the CRM, not in Campaign Manager. Our {L('/blog/measure-marketing-success-metrics/', 'guide to measuring marketing')} and the broader {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston energy and industrial companies')} go deeper on attribution for long cycles.</p>"""),

            ("When is LinkedIn not worth it for a Houston company?", f"""<p>We say no to LinkedIn about as often as we say yes. These are the usual reasons.</p>
<!--fig:skip-->
<p>The most common one is the second item. A lot of Houston industrial demand starts on Google: “crane rental Pasadena,” “industrial electrician Baytown,” “emergency valve repair Houston.” Those searches come from people with a problem today, and they’ll call the first credible company they find. LinkedIn can’t compete with that intent.</p>
<p>Professional services sit in the middle. A Houston {L('/blog/law-firm-marketing-houston/', 'law firm')} or {L('/blog/cpa-accounting-firm-marketing-houston/', 'accounting firm')} with an energy or M&amp;A niche can do well with Thought Leader Ads from partners. A firm whose clients are mostly individuals usually can’t.</p>"""),

            ("A 90-day LinkedIn plan for Houston B2B", f"""<p><b>Month one.</b> Build and tier the company list, set up the Insight Tag and CRM sync, create two campaigns (top accounts and wider list), and launch with document ads and one Thought Leader post a week. Judge only delivery and engagement by account.</p>
<p><b>Month two.</b> Add a Lead Gen Form campaign with a qualifying question. Start retargeting engaged visitors. Kill the weakest creative and replace it. Begin tracking meetings and sales-accepted leads.</p>
<p><b>Month three.</b> Review cost per sales-accepted lead and which accounts are engaging. Move budget toward what produced meetings. If OTC is inside the next 90 days, start the pre-show sequence.</p>
<p>At day 90 you won’t have closed revenue yet. You will know whether the right accounts are paying attention, which is the leading indicator that matters.</p>
<p>Our {L('/services/paid-social-advertising/', 'paid social team')} runs LinkedIn alongside Meta and Google. If you’d like a plan built around your target accounts and your sales cycle, tell us about your business and <a href="/contact/">get in touch</a>; a senior strategist will put it together.</p>"""),
        ],
        "faq": [
            ("What is the minimum budget for LinkedIn ads in Houston?",
             "LinkedIn’s platform minimum is $10 a day per campaign, or $30 per campaign with Dynamic Group Budget, and new campaigns need at least a $100 lifetime budget. Those are the floor, not a realistic test. For a Houston B2B company targeting senior energy or industrial buyers, we’d plan at least $3,000 to $5,000 a month for a full quarter to get enough data to judge results."),
            ("Can I target employees of specific companies in the Energy Corridor on LinkedIn?",
             "Yes. Upload a company list with up to 300,000 records and LinkedIn matches it to company pages, usually within 24 to 48 hours. You can’t target an office park directly, so pair the list with a Houston metro location filter. Otherwise a list including bp, Shell or ConocoPhillips reaches their employees worldwide, not just the people working along I-10 west of Houston."),
            ("Are LinkedIn Lead Gen Forms better than sending people to my website?",
             "They usually convert better. LinkedIn reports a 13% average conversion rate because the forms are pre-filled from profiles. The tradeoff is lead quality, since one tap is easy. Add a single multiple-choice qualifying question about timeline or project stage, sync leads into your CRM, and call within the hour. Landing pages still make sense for detailed quote requests."),
            ("When should a Houston company run LinkedIn ads for OTC?",
             "Start about eight weeks before the show with awareness ads to your target account list, then switch to meeting requests three to four weeks out. OTC 2027 runs May 3 to 5 at Reliant Park, co-located with URTeC. Keep a light campaign running during show week, then retarget booth contacts with a contact list upload for several weeks afterward."),
            ("Do LinkedIn ads work for small B2B companies in The Woodlands?",
             "They can, if deal sizes are large and the buyer is identifiable by company and title. A small engineering or consulting firm in The Woodlands selling six-figure contracts to chemical and energy companies is a good fit. A company with small transactional orders, or one whose buyers search Google when something breaks, will usually get more from search ads first."),
        ],
        "figures": {
            "abmsteps": {
                "type": "steps",
                "title": "Building a Houston target account list",
                "sub": "Before you open Campaign Manager",
                "steps": [["Name the accounts", "300 to 3,000 companies you want as clients, from the CRM and sales."], ["Tier them", "Top 50 get their own campaign and creative."], ["Add match fields", "Website domain and LinkedIn page URL, not just names."], ["Upload the CSV", "Up to 300,000 records; ready in 24 to 48 hours."], ["Layer location and roles", "Houston metro plus function and seniority."]],
                "alt": "Five steps to build a LinkedIn ABM company list for B2B companies in Houston and The Woodlands",
                "caption": f"List limits from {SRC['licompany']}.",
            },
            "map": {
                "type": "map",
                "title": "Where Houston energy buying committees sit",
                "sub": "Corporate clusters named in this playbook",
                "highlight": ["The Woodlands", "Spring", "Memorial", "Katy", "Houston", "Galleria"],
                "alt": "Map of Houston corporate headquarters clusters for LinkedIn B2B targeting, including The Woodlands, Spring and the Energy Corridor",
                "caption": "The Energy Corridor runs along I-10 between Memorial and Katy; Greenspoint sits off I-45 near Beltway 8, south of Spring.",
            },
            "costs": {
                "type": "stats",
                "title": "LinkedIn’s published floors",
                "stats": [["$10", "Minimum daily budget, any format"], ["$100", "Minimum lifetime budget, new campaign"], ["300", "Minimum audience size"], ["50K+", "Recommended for image and text ads"]],
                "alt": "Stats on LinkedIn Ads minimum budget and audience size for Houston and The Woodlands B2B advertisers",
                "caption": f"From {SRC['libudget']} and {SRC['liaud']}. Floors, not recommendations for a real test.",
            },
            "budget": {
                "type": "funnel",
                "title": "What $5,000 a month might buy",
                "stages": [["Monthly spend", "$5,000"], ["Clicks at an assumed $12.50", "≈ 400"], ["Form and site leads", "≈ 30"], ["Sales-accepted leads", "≈ 8"], ["New opportunities", "1 to 2"]],
                "note": "Illustrative example. Your CPC and rates will differ; replace with your own after 30 days.",
                "alt": "Funnel showing illustrative LinkedIn Ads budget math for a B2B company in The Woodlands and Houston",
                "caption": "Whether this works depends almost entirely on what one opportunity is worth to you.",
            },
            "lgf": {
                "type": "compare",
                "title": "Lead Gen Form vs. landing page",
                "left": {"title": "Landing page", "items": ["Slower on mobile", "Member retypes contact info", "Room for detail and proof", "Better for complex quote requests", "Lower conversion rate"]},
                "right": {"title": "Lead Gen Form", "items": ["Opens inside LinkedIn", "Pre-filled from the profile", "13% average conversion (LinkedIn)", "Add one qualifying question", "Syncs to HubSpot or Salesforce"]},
                "alt": "Comparison of LinkedIn Lead Gen Forms and landing pages for Houston and The Woodlands B2B lead generation",
                "caption": f"Conversion figure from {SRC['lilgf']}.",
            },
            "otc": {
                "type": "columns",
                "title": "How we’d weight LinkedIn spend around OTC",
                "sub": "Share of spring budget by period, relative to the May show",
                "labels": ["Mar", "Early Apr", "Late Apr", "Show week", "+2 wks", "+6 wks", "Jun-Jul"],
                "values": [45, 60, 90, 55, 75, 50, 15],
                "highlight": [2, 4],
                "y_label": "Relative spend",
                "note": "Illustrative example",
                "alt": "Column chart of LinkedIn ad spend timing around the Offshore Technology Conference in Houston for B2B companies",
                "caption": "Peak before the show to book meetings, and again after it to follow up on booth contacts.",
            },
            "skip": {
                "type": "checklist",
                "title": "Skip LinkedIn (for now) if...",
                "sub": "Signs another channel will do more for a Houston B2B company",
                "items": ["A typical deal is under about $20,000", "Buyers search Google when something breaks", "You need leads this month, not next year", "You can’t fund $3,000+ a month for 90 days", "Nobody will call leads within a day", "You have no proof to show: no case studies, specs or photos", "Your buyer is a homeowner or plant-floor tech, not an office role"],
                "alt": "Checklist of signs LinkedIn Ads are not worth it for a B2B company in Houston or The Woodlands",
                "caption": "Two or more checked? Start with Google search and outbound, and revisit LinkedIn later.",
            },
        },
    },
]
