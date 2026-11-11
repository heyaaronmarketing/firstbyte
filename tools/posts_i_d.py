"""Batch 9: orthodontist marketing in The Woodlands and Houston (independent practices vs. DSOs and direct-to-consumer
aligners), and daycare / child care center enrollment marketing in Houston and The Woodlands.

Research: 22 Tex. Admin. Code 108.54 (advertising of specialties: CODA-accredited 2+ year program or board
certification, "specialist in" / "practice limited to", practice limited to the specialty) and 108.55 (general
dentists must show "General Dentist" after the name, no smaller than the largest service font) via Cornell LII;
Orthodontic Products podcast (June 2025) on Align's Invisalign trademark enforcement (May 2024 suit against a Portland
practice, active-customer rule, website/GBP/ads references); Align's social media guidelines (no Invisalign in handles,
disclose affiliation); Google Ads trademark policy (keywords not restricted, ad text can be); AAO (first check-up by
age 7, no referral needed; one in three orthodontic patients are adults); DrBicuspid on SmileDirectClub's December
2023 shutdown after its September 2023 Chapter 11; Holland & Knight on AHA v. Becerra (N.D. Tex., June 20, 2024);
LexBlog on HHS dropping its appeal (Aug. 29, 2024); Google Analytics HIPAA help page; Fierce Healthcare on Elite
Dental Associates' $10,000 OCR settlement over Yelp replies; Google's "Health in personalized advertising" policy;
Jon Loomer on Meta's personal attributes policy and special ad categories.
Daycare post: Texas HHS news release on TXChildCareSearch.org (Jan 2020, five years of compliance history); KPRC
Click2Houston (Aug 2025) on deficiency weights and narratives; Texas HHS parent page; Texas Rising Star certification
levels (mandatory for CCS providers, Entry Level 24 months, no enhanced rate at Entry Level); Texas Child Care
Services scholarships page (families choose any CCS provider, 14 days); Workforce Solutions Gulf Coast (13-county
region, waitlist, KinderConnect) and its April 2026 note on ~30,000 Harris County children on waitlists; First Five
Years Fund ratio table from the FY2025-2027 CCDF plan; ABC13 (April 2025) on 43 Houston child care deserts; KPRC (June
2026) on the desert definition; Social Media Today on Meta's Jan 15, 2026 targeting consolidation; Google Maps
prohibited content policy; PPC Land on the April 2026 staff-quota rule.
Competitor/PAA phrasing read for "orthodontist marketing", "how to get more orthodontic patients", "orthodontic
google ads", "daycare marketing", "how to increase enrollment in daycare", "child care center advertising ideas".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # ortho post
    "tx5454": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-108-54", "22 Tex. Admin. Code § 108.54"),
    "tx5455": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-108-55", "§ 108.55"),
    "op_pod": A("https://orthodonticproductsonline.com/resource-center/podcasts/invisalign-trademark-crackdown-what-it-means-for-your-orthodontic-practice-marketing/", "an Orthodontic Products podcast on Align’s trademark enforcement"),
    "align_sm": A("https://www.invisalign.com/social-media-guidelines", "Align’s social media guidelines"),
    "gtm": A("https://support.google.com/adspolicy/answer/6118?hl=en", "Google’s trademark policy"),
    "aao7": A("https://aaoinfo.org/child-orthodontics/", "the American Association of Orthodontists"),
    "aao_adult": A("https://aaoinfo.org/blog/number-of-adults-seeing-an-orthodontist-is-at-an-all-time-high/", "the AAO"),
    "sdc": A("https://www.drbicuspid.com/dental-business/industry-updates/article/15659977/smiledirectclub-shuts-down", "DrBicuspid"),
    "hk": A("https://www.hklaw.com/en/insights/publications/2024/06/american-hospital-assn-v-becerra-are-tracking-tools-ok-again", "Holland & Knight’s summary of the ruling"),
    "appeal": A("https://www.lexblog.com/2024/09/27/shortly-after-its-online-tracking-technologies-bulletin-is-declared-unlawful-hhs-ocr-stands-down-withdraws-appeal/", "dropped its appeal"),
    "ga_hipaa": A("https://support.google.com/analytics/answer/13297105?hl=en", "Google’s own HIPAA page for Analytics"),
    "elite": A("https://www.fiercehealthcare.com/practices/dental-practice-pays-10k-to-settle-complaint-it-disclosed-patient-information-social", "paid $10,000 to settle with HHS"),
    "ghealth": A("https://support.google.com/adspolicy/answer/16701855?hl=en", "health in personalized advertising policy"),
    "pattr": A("https://www.jonloomer.com/qvt/personal-attributes-and-ad-rejections/", "personal attributes policy"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy"),
    # daycare post
    "txsearch": A("https://content.govdelivery.com/accounts/TXHHSC/bulletins/2769e35", "Texas HHS"),
    "kprc_safe": A("https://www.click2houston.com/news/2025/08/04/how-to-find-a-safe-day-care-facility-in-texas", "KPRC’s walkthrough of the search"),
    "hhs_parents": A("https://www.hhs.texas.gov/node/207611", "Texas HHS tells parents"),
    "trs": A("https://www.childcare.texas.gov/texas-rising-star/about-texas-rising-star/certification-levels", "Texas Rising Star’s certification page"),
    "ccs": A("https://www.childcare.texas.gov/for-families/child-care-scholarships", "the state’s Child Care Services page"),
    "wsgc": A("https://wrksolutions.com/childcare-financial-assistance", "Workforce Solutions Gulf Coast"),
    "wsgc_13": A("https://www.wrksolutions.com/who-we-are", "13-county Houston-Galveston region"),
    "wsgc_wait": A("https://wrksolutions.com/news/workforce-solutions-gulf-coast-helps-lead-regional-effort-to-expand-child-care-access", "Workforce Solutions Gulf Coast"),
    "ffyf": A("https://www.ffyf.org/wp-content/uploads/2026/05/Ratios-By-State.pdf", "First Five Years Fund’s ratio table"),
    "abc13": A("https://abc13.com/post/child-care-centers-shutting-down-texas-because-arent-receiving-sufficient-funding-officials-warn/16172595/", "ABC13"),
    "kprc_desert": A("https://www.click2houston.com/news/local/2026/06/04/families-have-to-make-hard-decisions-new-report-highlights-child-care-gaps-in-houston/", "KPRC"),
    "smt": A("https://www.socialmediatoday.com/news/meta-removes-more-detailed-ad-targeting-options-facebook-instagram/757856/", "Social Media Today"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to special ad categories"),
    "ppcl": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
}

ORTHO = "/blog/orthodontist-marketing-the-woodlands-houston/"
DAYCARE = "/blog/daycare-marketing-houston-the-woodlands/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: orthodontists
    {
        "slug": "orthodontist-marketing-the-woodlands-houston",
        "title": "Orthodontist Marketing in The Woodlands and Houston: How Independent Practices Win New Starts",
        "seo_title": "Orthodontist Marketing in The Woodlands & Houston",
        "desc": "Orthodontist marketing for The Woodlands and Houston: Google Ads, Invisalign trademark rules, Texas specialist ad rules, referrals, HIPAA and cost per start.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Instagram"],
        "art": "b5",
        "hero": "medical",
        "hero_alt": "Illustration of a medical practice for orthodontist marketing in The Woodlands, Spring and Houston",
        "related": ["dental-marketing-the-woodlands-houston", "medical-practice-marketing-houston", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Thursday, 4:15 p.m., at a practice off Research Forest. A mom calls because her son’s general dentist in Spring mentioned a crossbite at his cleaning. She has already called two other offices. Her first question isn’t about the doctor’s training or the technology. It’s “do you take our insurance, and what’s the monthly payment?”</p>
<p>Ten minutes later a 34-year-old engineer books a consult from an Instagram ad. In the notes field she writes that she started aligners with a mail-order company years ago, never finished, and wants to know if that’s fixable.</p>
<p>Those two people are most of orthodontist marketing in Houston. One is a parent making a decision for a child, usually on a referral, and shopping on price and convenience. The other is an adult choosing for themselves, often after a bad experience somewhere cheaper.</p>
<p>To get more orthodontic patients as an independent practice, win the Google Maps results for “orthodontist near me” in your part of town and treat your general dentist referrers like your best customers. Run search ads on braces and clear aligner terms (carefully, because of trademark rules). Make the free exam easy to book and the monthly payment easy to understand. Then measure everything by cost per start rather than cost per lead.</p>
<p>We’ve worked with dental specialists, including Omega Dental Specialists, and this is how we’d set up a single- or two-office ortho practice from Conroe down to Katy.</p>"""),

            ("Who you’re actually competing with", f"""<p>An independent orthodontist in north Houston has three kinds of competition, and each needs a different answer.</p>
<p><b>DSO-backed ortho groups.</b> Multi-office brands with central call centers, big ad budgets and Saturday hours. They usually win on convenience and spend. You beat them with the doctor’s face and name, faster callbacks, and the referral relationships they can’t buy.</p>
<p><b>General dentists offering aligners.</b> Plenty of family dentists in The Woodlands, Cypress and Sugar Land now treat simple aligner cases in-house. That can feel like losing referrals. In practice it means your marketing has to explain, without trashing anyone, which cases need a specialist.</p>
<p><b>Direct-to-consumer aligners.</b> SmileDirectClub filed for Chapter 11 in September 2023 and shut down in December 2023, canceling pending orders and telling patients to arrange follow-up care with local dentists, per {SRC['sdc']}. Other mail-order brands remain. The collapse left a lot of adults with unfinished treatment and a healthy distrust of “cheap and fast.” That’s an audience, and a respectful “started treatment elsewhere?” page speaks to it directly.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Competitor</th><th>Where they win</th><th>Where an independent wins</th></tr></thead>
<tbody>
<tr><td>DSO ortho group</td><td>Ad spend, hours, call center, brand recognition</td><td>Same doctor every visit, local reputation, referral network, faster personal follow-up</td></tr>
<tr><td>General dentist doing aligners</td><td>Existing patient trust, convenience</td><td>Complex cases, kids’ growth timing, braces and aligners both, specialist training</td></tr>
<tr><td>Mail-order aligners</td><td>Price, no office visits</td><td>In-person supervision, X-rays, refinements, a doctor who answers when something goes wrong</td></tr>
</tbody></table></div>"""),

            ("Two buyers: parents and adults", f"""<p><b>Parents.</b> {SRC['aao7']} recommends kids have their first check-up with an orthodontist by age 7, and its site tells parents they can book directly without a dentist’s referral. That gives you a clean, non-salesy message. “Free orthodontic check-up for kids 7 and up. No referral needed.” Most won’t start treatment that year, but they enter your recall system.</p>
<p>Parents shop on a few practical things: insurance, the monthly payment, how many school days the appointments eat, and whether the office is on the way from school.</p>
<p><b>Adults.</b> According to {SRC['aao_adult']}, about one in three orthodontic patients is now over 18. Adults decide faster than parents, research more online, and care a lot about discreet options, the total timeline and whether they’ll need to miss work.</p>
<!--fig:stats-->
<p>Give these two groups separate pages, ad groups and follow-up sequences.</p>"""),

            ("Google Business Profile and reviews for an ortho practice", f"""<p>For “orthodontist near me,” the map pack is the first thing most people see. Set the primary category to <b>Orthodontist</b>. Add services in plain words: braces, clear aligners, early (Phase I) treatment, adult orthodontics, retainers, second opinions. Upload real photos of the office, the doctor and the team, and a street-view shot of the entrance so a parent can find it at 3:45 with a carpool behind them.</p>
<p>Two offices means two verified profiles with their own hours. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest of the ranking work.</p>
<p>Reviews matter even more in ortho than in general dentistry, because treatment runs 12 to 24 months and families talk at school pickup the whole time. The best moments to ask are when braces come off and at the first aligner check where the patient can see a difference.</p>
<p>The rules: under {SRC['gpol']} for Maps, you can’t offer anything for a review, can’t ask only happy patients, and can’t discourage negative ones. Retire the “leave a review for a gift card” sign at the front desk and the debond-day prize wheel if it’s tied to reviews.</p>
<p>Replying is where practices get into HIPAA trouble. Elite Dental Associates in Dallas {SRC['elite']} after its Yelp replies disclosed patients’ names and treatment details. A safe reply never confirms someone is a patient. “Thanks for the kind words, we love hearing this” works. “Glad your daughter’s expander went well!” does not. For angry reviews: “We take every concern seriously. Please call our office manager at [number] so we can talk directly.” Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("Google Ads for braces and clear aligners", f"""<p>Search is where most new-patient intent shows up. Split campaigns by what the person is asking for, and send each one to a page that matches.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Orthodontist (general)</td><td>orthodontist near me, orthodontist the woodlands, orthodontist spring tx, best orthodontist conroe</td><td>Homepage-style page with free exam booking</td></tr>
<tr><td>Braces</td><td>braces near me, braces for kids, braces cost houston, how much are braces</td><td>Braces page with payment range and insurance info</td></tr>
<tr><td>Clear aligners</td><td>clear aligners near me, invisible braces, clear braces for adults</td><td>Adult aligner page with timeline and consult booking</td></tr>
<tr><td>Early treatment</td><td>orthodontist for 7 year old, expander for kids, crossbite treatment child</td><td>Parent page built around the age-7 check-up</td></tr>
<tr><td>Second opinion / restart</td><td>finish aligner treatment, aligners didn’t work, orthodontic second opinion</td><td>“Started treatment elsewhere?” page</td></tr>
</tbody></table></div>
<p>Use the negative list below from day one, and keep adding from the search terms report weekly for the first month.</p>
<!--fig:negatives-->
<p>Settings that matter: target “Presence: people in or regularly in your included locations,” keep the radius to how far families will drive monthly (usually 8 to 12 miles in suburban Montgomery County, tighter inside the Beltway), and schedule call assets only for hours someone answers. Track booked exams and calls longer than about a minute as conversions, not page views. If you need help setting that up, our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} walks through it, and the {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give you a feel for click costs.</p>
<p>One policy note on retargeting. Google treats health as a sensitive category under its {SRC['ghealth']}, which limits advertiser-built audiences like remarketing lists and Customer Match for ads about health conditions and medical procedures. Orthodontics isn’t named on that page, but ad reviews aren’t always predictable, and HIPAA (below) is a separate concern. We keep ortho retargeting simple and creative generic, or skip it.</p>"""),

            ("Invisalign trademark rules: what you can and can’t say", f"""<p>Most patients search “Invisalign,” and many practices want to bid on it and say it everywhere. Align Technology has gotten stricter about who can.</p>
<p>According to {SRC['op_pod']} (June 2025), Align sued a Portland, Oregon practice in May 2024 for placing Invisalign next to another aligner brand, and has sent cease-and-desist letters to practices that hadn’t ordered Invisalign treatment recently. The guests described Align allowing brand use only by active customers with recent case starts, and the letters covering website text, URLs, meta tags, image alt text, Google Business Profile, social accounts, Yelp and print. Their advice: confirm the current requirements with your Align rep, because thresholds can differ by practice type.</p>
<p>Separately, {SRC['align_sm']} tell doctors not to put “Invisalign” in any username or handle, and to disclose their relationship with Align when they post about it. So @WoodlandsInvisalignSmiles is out.</p>
<p>On the Google side, {SRC['gtm']} doesn’t restrict trademarks as keywords, but a trademark owner can restrict their use in ad text. In practice:</p>
<ul>
<li>If you’re an active Invisalign provider, using the name on a dedicated page is generally fine. Follow Align’s current brand guidelines and keep your provider status current.</li>
<li>If you also offer other aligner brands, give each its own page under a “Clear aligners” menu. Don’t put brands side by side in a way that implies they’re the same thing.</li>
<li>In ad text, “clear aligners” is the safe phrase. Bidding on the keyword “invisalign” is a separate question from writing it in the headline, and the podcast guest’s view was that you shouldn’t put Invisalign in your ads at all. Check with your rep before you do.</li>
<li>If you stop offering Invisalign, clean the name out of everything, including old blog posts and image file names, and redirect any URLs that contained it.</li>
</ul>"""),

            ("Texas specialist advertising rules", f"""<p>Texas has specific rules on who can call themselves a specialist, and they work in your favor.</p>
<p>Under {SRC['tx5454']}, a dentist may advertise as a specialist in orthodontics and dentofacial orthopedics only if they completed a CODA-accredited specialty program of two or more years or hold diplomate status from a qualifying specialty board. A specialist should use phrases like “specialist in” or “practice limited to” and limit their practice to the advertised specialty. Under {SRC['tx5455']}, a general dentist advertising specific services must put “General Dentist” or “General Dentistry” right after their name, in type no smaller than the largest font used for the services, and say it clearly in broadcast ads.</p>
<p>What that means for your marketing:</p>
<!--fig:claims-->
<p>Specialist status is a real differentiator, so say it plainly: “Dr. Name is a specialist in orthodontics. After dental school, she completed a [X]-year orthodontic residency at [program].” Skip “the best” and “the only.”</p>
<p>If your marketing person writes copy for multiple offices or a group that includes general dentists, the practice owner carries the burden of avoiding any suggestion that the general dentists are specialists. Have someone who knows the rule read every ad. We’re marketers, not your attorney, so run anything borderline past one.</p>"""),

            ("General dentist referrals still drive the practice", f"""<p>In most independent ortho practices we’ve seen, referring dentists produce the biggest share of new starts. Ads rarely beat a family dentist who tells a parent “go see Dr. Name, she’s great.” Yet referral marketing is the part almost nobody tracks.</p>
<p>What works in The Woodlands, Spring and Conroe:</p>
<ol>
<li><b>Know your top 20 referrers by name.</b> Pull a report from your practice software of starts by referring office for the last 12 months. Most practices find a handful of offices send a large share.</li>
<li><b>Close the loop fast.</b> Send the referring dentist a short note after the exam and again at the start, with the treatment plan. A referrer who hears back keeps referring.</li>
<li><b>Visit in person.</b> Lunch for the hygiene team once a quarter. Hygienists spot crossbites and crowding and are the ones who actually say your name to the parent.</li>
<li><b>Make referring easy.</b> A one-page online referral form, a referral pad with your QR code, and a direct line that skips the phone tree.</li>
<li><b>Send patients back.</b> Remind every patient about cleanings, and route families without a dentist to your referrers. It’s the reason they keep sending you kids.</li>
</ol>
<p>And never bid on a referring dentist’s practice name.</p>"""),

            ("The price question: financing and payment plans", f"""<p>Back to the Thursday call. Before anything else, the mom wants to know the payment. Practices that hide all pricing until the exam lose a lot of these callers to the one that gives a range on the phone.</p>
<ul>
<li>Publish a range for comprehensive treatment and a typical monthly payment with your in-house plan, along with the down payment options. “Most comprehensive treatment plans in our office fall between $X and $Y, with in-house payment plans starting around $Z a month” is far better than nothing.</li>
<li>Say whether the first exam is free, and what it includes (X-rays, photos, a treatment-fee estimate).</li>
<li>Explain how ortho insurance usually works: a lifetime maximum, sometimes an age cap. Offer to check benefits before the exam.</li>
<li>List third-party financing if you offer it, plus HSA and FSA payments. Houston’s energy employers often offer FSAs, and November and December are when families try to spend them down.</li>
<li>Train whoever answers the phone to give the range, then book the exam.</li>
</ul>
<p>A price page also helps with search, since people type “how much are braces in Houston” all day.</p>"""),

            ("Instagram and Facebook ads for adult aligners and parents", f"""<p>Meta works better for adult aligner cases than for kids’ braces, because adults are choosing for themselves and respond to before-and-after stories and to the doctor on camera. For parents, Meta works best as a reminder of the free age-7 check-up and around back-to-school.</p>
<p>What to run:</p>
<ul>
<li>Short videos of the doctor explaining one thing, like what happens at the first visit.</li>
<li>Patient stories, with written consent and a HIPAA authorization on file, and nothing that identifies a patient without it.</li>
<li>A free consult offer with two qualifying questions on the form (who is the patient, adult or child; any previous treatment).</li>
</ul>
<p>Watch Meta’s {SRC['pattr']}. Ads can’t assert or imply things about the viewer’s personal attributes, which includes health. “Embarrassed by your crooked teeth?” implies the viewer has crooked teeth and tends to get rejected. “Straighter teeth in as little as [timeline] with clear aligners. Free consult in The Woodlands” describes the service and usually clears.</p>
<p>For forms, our post on {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'fixing low-quality Facebook leads')} covers the questions that filter out people who aren’t serious.</p>"""),

            ("HIPAA and tracking pixels on an orthodontic website", f"""<p>This is the part most marketing agencies get wrong with medical and dental clients. An ortho practice is a HIPAA covered entity, and its website is in scope.</p>
<p>In 2022 HHS’s Office for Civil Rights issued guidance on online tracking technologies like the Meta Pixel and Google Analytics, revised it in March 2024, and then lost part of it in court. On June 20, 2024, the Northern District of Texas vacated the portion that treated an IP address plus a visit to a public health information page as protected health information, per {SRC['hk']}. HHS {SRC['appeal']} in August 2024. The rest of the guidance, including the position that identifiable health information collected through a provider’s website or app is generally PHI, still stands.</p>
<p>Google also says on {SRC['ga_hipaa']} that it makes no representation that Analytics meets HIPAA requirements and that customers shouldn’t put Analytics tags on authenticated pages or pages likely to be HIPAA-covered.</p>
<p>What we do for health practices:</p>
<ul>
<li>No ad pixels or analytics tags on the patient portal, online forms that collect health information, or the booking flow after the patient starts entering details.</li>
<li>Booking and intake through a HIPAA-compliant vendor that signs a business associate agreement.</li>
<li>Conversion tracking based on “thank-you page loaded” or a server-side event that carries no health details, rather than form contents.</li>
<li>Call tracking from a vendor that offers a BAA, if calls are recorded or transcribed.</li>
<li>A written list of every script on the site, reviewed with the practice’s compliance advisor.</li>
</ul>"""),

            ("Measuring cost per start, and a first 90 days", f"""<p>Cost per lead lies in orthodontics. A Facebook form fill from someone who “just wanted to know the price” and a referral from a dentist with a crossbite diagnosis count the same. Cost per start is the number to run the practice on.</p>
<!--fig:funnel-->
<p>To see it, you need four counts by source every month: leads (calls, forms, chats), exams booked, exams kept, and starts. Your practice management software has exams and starts. Your call tracking and ad platforms have leads. Somebody has to match them, usually the treatment coordinator in a shared sheet, until you can automate it.</p>
<p>Speed matters at the lead stage. A parent who filled out a form at 9 p.m. is often calling another office at 8:30 the next morning. Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')} covers the follow-up system.</p>
<p>A sensible first 90 days for an independent practice:</p>
<ol>
<li><b>Days 1 to 30:</b> fix the Business Profile, build the parent, adult and “started elsewhere” pages, publish price ranges, clean Invisalign references to match your provider status, audit pixels, and set up call tracking and exam-booking conversions.</li>
<li><b>Days 31 to 60:</b> launch search campaigns by ad group above, start the review-request process at debond and first aligner check, and visit your top 10 referring offices.</li>
<li><b>Days 61 to 90:</b> add Meta for adult aligners, build the cost-per-start sheet by source, and move budget toward whatever produces starts.</li>
</ol>
<p>On budget, many single-office practices we’d talk to spend somewhere between $2,000 and $6,000 a month on paid media, more in a new market. Treat that as illustrative. The right number comes from your measured cost per start and how many starts a month the doctor wants.</p>
<p>For the general dentistry side of the business, see our {L('/blog/dental-marketing-the-woodlands-houston/', 'dental marketing guide')}, and our {L('/services/search-marketing/', 'search marketing team')} handles campaigns like these. If you’d like a plan built around your offices and your referral base, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do orthodontists get more new patients?",
             "Most new starts come from general dentist referrals, Google Maps results for orthodontist near me, and search ads on braces and clear aligner terms. Independent practices grow fastest by keeping referrers informed after every exam, collecting reviews at debond, publishing price ranges and payment plans, and making the free exam easy to book online. Track every source through to treatment starts so you know what works."),
            ("Can I use the word Invisalign in my Google Ads?",
             "Google does not block trademarks as keywords, but trademark owners can restrict their use in ad text, and Align Technology actively enforces its Invisalign trademark against practices that are not active providers. Many practices use clear aligners in ad text to stay safe. If you are a current provider, check Align’s brand guidelines and your rep before putting the name in ads, URLs or social handles."),
            ("Can a general dentist advertise as an orthodontist in Texas?",
             "Not as a specialist. Texas Board rules allow only dentists with a CODA-accredited specialty program of two or more years or qualifying board certification to advertise as specialists in orthodontics. A general dentist who advertises orthodontic services must show General Dentist or General Dentistry after their name, in type at least as large as the largest service text in the ad."),
            ("Is the Meta Pixel allowed on an orthodontist’s website?",
             "It depends on where it fires and what it collects. A 2024 Texas court decision limited federal guidance about public pages, but identifiable health information collected through a practice’s site is still generally protected health information. Keep pixels and analytics off patient portals, intake forms and booking flows, use HIPAA-compliant vendors with business associate agreements, and review every script with your compliance advisor."),
            ("How much should an orthodontist spend on marketing?",
             "There is no fixed rule. Many single-office practices spend somewhere around $2,000 to $6,000 a month on paid media, plus website and SEO work, but that is only a starting range. Work backward from the starts you want each month and your measured cost per start by channel, and keep investing in referral relationships, which often cost the least per start."),
        ],
        "figures": {
            "stats": {
                "type": "stats",
                "title": "The two orthodontic buyers",
                "stats": [["Age 7", "AAO’s recommended first ortho check-up"], ["1 in 3", "orthodontic patients are adults"], ["Dec 2023", "SmileDirectClub shut down"], ["No referral", "needed for a first check-up"]],
                "note": "Source: American Association of Orthodontists, DrBicuspid",
                "alt": "Stats for orthodontist marketing in The Woodlands and Houston: age 7 check-up, one in three patients adults",
                "caption": f"From {SRC['aao7']}, {SRC['aao_adult']} and {SRC['sdc']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for orthodontic search ads",
                "sub": "Add these before launch, then review search terms weekly",
                "items": ["Jobs: jobs, hiring, salary, assistant, residency", "School: orthodontic school, how to become", "DIY: at home, diy, rubber bands, fix teeth yourself", "Retail: retainer case, amazon, kit, cheap aligners", "Products: dental wax, braces tools, brush", "Pain only: braces pain relief, sore teeth", "Wrong service: dentures, implants, veneers", "Brands you don’t offer, by name"],
                "alt": "Checklist of negative keywords for orthodontist Google Ads in The Woodlands and Houston",
                "caption": "Your search terms report will add a dozen more in the first month.",
            },
            "claims": {
                "type": "compare",
                "title": "Specialist claims in Texas ads",
                "left": {"title": "Risky", "items": ["“The best orthodontist in The Woodlands”", "“Only real experts straighten teeth”", "General dentist ad with no “General Dentist” label", "Implying referring dentists do poor work", "“Board certified” without a qualifying board"]},
                "right": {"title": "Factual and compliant", "items": ["“Specialist in orthodontics”", "“Practice limited to orthodontics”", "Residency program and years stated plainly", "Respectful second-opinion language", "Board certification named exactly"]},
                "alt": "Comparison of risky and compliant specialist advertising wording for orthodontists in Texas, The Woodlands and Houston",
                "caption": f"Based on {SRC['tx5454']} and {SRC['tx5455']}. Not legal advice.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From lead to treatment start",
                "stages": [["Leads (calls, forms, chats)", "120"], ["Exams booked", "60"], ["Exams kept", "48"], ["Treatment accepted", "26"], ["Starts this month", "22"]],
                "note": "Illustrative example",
                "alt": "Funnel showing orthodontic leads, exams and starts for a practice in The Woodlands and Houston",
                "caption": "Divide total marketing spend by starts, by source, to get cost per start.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: daycare / child care
    {
        "slug": "daycare-marketing-houston-the-woodlands",
        "title": "Daycare Marketing in Houston and The Woodlands: How to Fill Enrollment and Waitlists",
        "seo_title": "Daycare Marketing in Houston & The Woodlands",
        "desc": "Daycare marketing for Houston and The Woodlands: tour bookings, Google Business Profile, reviews, public inspection history, Texas Rising Star, CCS families.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Facebook", "Google Ads"],
        "art": "b6",
        "hero": "play",
        "hero_alt": "Illustration of play and learning for daycare and child care center marketing in Houston and The Woodlands",
        "related": ["back-to-school-marketing-woodlands", "rank-in-google-map-pack-houston", "facebook-lead-ads-bad-leads-fix-quality"],
        "sections": [
            (None, f"""<p>Second Monday in August at a center in Cypress. The director has a waitlist of 14 for infants and can’t take any of them, because she’s one infant teacher short. Meanwhile the 3-year-old room has five open spots, and the pre-K room just lost four kids to the school district’s program.</p>
<p>Saturday, a couple touring with a newborn pulls out a phone in the hallway. They’ve already looked up her state inspection history, and they want to ask about a citation from last spring.</p>
<p>That’s child care marketing in Houston. The problem is rarely “not enough interest.” It’s getting the right families into the classrooms you can staff, at the time of year they’re deciding, with a tour process that turns a curious parent into a signed enrollment.</p>
<p>To increase enrollment at a daycare or child care center, market the specific classrooms with open seats and staff to cover them. Win the Google Maps results within a few miles of home and work routes, and make tours bookable online. Own your public inspection record instead of hoping parents won’t look. Then follow up fast, because parents tour three or four centers before they choose.</p>
<p>This guide is for independent centers and small multi-site operators from Conroe to Pearland.</p>"""),

            ("How Houston parents actually search for child care", f"""<p>Parents pick child care near home or on the drive to work, and almost never somewhere far from both. A family in Spring commuting down I-45 might consider centers near home, near the Grand Parkway, or close to an office in Greenspoint. Very few will consider one in Tomball.</p>
<p>The searches are local and specific: “daycare near me,” “infant care the woodlands,” “preschool spring tx,” “daycare that accepts CCS,” “montessori cypress,” “after school care near [school name].” Parents search on their phones during lunch, read reviews, look at photos, and then look up the center in the state database.</p>
<p>Supply is tight in parts of the region. Advocacy group Children at Risk identified 43 child care deserts in Houston, and 56% of low-income children under six with working parents live in them, per {SRC['abc13']} in April 2025. The group defines a desert as a ZIP code where young children with working parents outnumber licensed capacity by more than three to one, per {SRC['kprc_desert']}. If your center sits in or near one of those ZIPs, your problem is mostly operations and staffing, not marketing. In the suburbs with heavy competition, like parts of The Woodlands, Katy and Sugar Land, the fight is for the map pack and the tour.</p>
<!--fig:map-->"""),

            ("Market the classrooms you can staff", f"""<p>This is the step most centers skip. Before you spend a dollar, list each classroom’s licensed capacity, current enrollment, staffed capacity and expected openings for the next 90 days.</p>
<p>Texas sets child-to-caregiver ratios by age. Per the {SRC['ffyf']}, drawn from the state’s FY2025-2027 child care plan, Texas centers run 1:4 for infants up to 11 months, 1:5 for 12 to 17 months, 1:9 for 18 to 23 months, 1:11 for 2-year-olds, 1:15 for 3-year-olds and 1:18 for 4-year-olds. Check the current Chapter 746 minimum standards for group sizes and exceptions.</p>
<!--fig:ratios-->
<p>The marketing math falls out of that table. One infant teacher can cover four babies; one teacher in the 4s room covers 18 kids. So:</p>
<ul>
<li>If you’re short on infant teachers, stop advertising infant openings. Run a waitlist page instead and put your ad money into the 3s and pre-K rooms.</li>
<li>If you just hired, advertise that specific room with a specific start date. “Two infant openings starting October 6” fills faster than “Now enrolling all ages.”</li>
<li>If the pre-K room is losing 4-year-olds to free public pre-K, market what the school program doesn’t offer: full-day hours, summer care, before and after care, sibling care in the same building.</li>
</ul>
<p>Keep a simple waitlist form on the site (child’s birth date, desired start date, schedule needed, phone) and actually call families when a spot opens. A waitlist nobody works is a list of families who enrolled somewhere else.</p>"""),

            ("Google Business Profile for a child care center", f"""<p>The map pack is where most “daycare near me” searches end. Pick the primary category that matches your main program: <b>Day care center</b>, <b>Preschool</b>, <b>Child care agency</b> or <b>Montessori school</b>. Add the others as secondary categories only if they’re true.</p>
<ul>
<li>Hours that match your real drop-off and pick-up window (6:30 a.m. to 6:30 p.m. is common). Parents filter by this.</li>
<li>A “Book a tour” appointment link that goes to a real scheduler, not the homepage.</li>
<li>Photos of classrooms, the playground, the kitchen, the secure entry and your staff. Never post a child’s face without written parent permission, and keep a permission list by child at the front desk.</li>
<li>Services and attributes: infant care, toddler care, pre-K, after-school, summer camp, meals provided, transportation to specific schools, Spanish spoken if true.</li>
<li>Weekly posts: an open seat in a specific room, a tour day, a new curriculum unit.</li>
</ul>
<p>If you run several centers, each needs its own profile and its own page on your site. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest.</p>"""),

            ("Reviews from parents, inside the rules", f"""<p>Parents read reviews more closely for child care than for nearly anything else they buy. They’re looking for specific words: safe, communication, teachers stay, my child loves it.</p>
<p>Under {SRC['gpol']}, you can’t offer anything for a review (no tuition credit, no free week), can’t ask only happy families, and can’t discourage negative reviews. In April 2026 Google also added language against telling staff to collect a set number of reviews or reviews with specific content, per {SRC['ppcl']}. Don’t run a teacher contest for reviews that mention their names.</p>
<p>When to ask: after a family’s first month, when the transition tears are over, and at the end of the school year. A simple text from the director works:</p>
<p><i>“Hi [Name], it’s [Director] at [Center]. We’ve loved having [child] in the Bluebird room this year. If you have a minute, an honest Google review helps other families find us: [link]. Thank you!”</i></p>
<p>Reply to every review. For critical ones, don’t argue and don’t share details about a child or family. Thank them, say you take it seriously, and invite them to call the director. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("Your inspection history is public. Own it.", f"""<p>Texas HHS Child Care Regulation runs TXChildCareSearch.org, and {SRC['hhs_parents']} to use it to find regulated providers and review inspection results. Since January 2020 the site has shown five years of an operation’s compliance history, including the number of inspections, deficiencies cited and corrective actions, per {SRC['txsearch']}. {SRC['kprc_safe']} notes that the operation details page shows the weights of deficiencies cited in the past three years, and parents can open a narrative of each incident.</p>
<p>Plenty of parents now look this up before the tour. Hoping they won’t is not a plan. What we’d do:</p>
<ul>
<li>Pull your own record every quarter and read it the way a nervous parent would.</li>
<li>Prepare a short, honest answer for any citation: what happened, what you changed, and who checks it now. Train the director and assistant director to give it calmly on tours.</li>
<li>Put a “Safety and licensing” page on your website with your license number, a link to your state record, your ratios, your staff training and background check policy, and your secure-entry and pick-up procedures.</li>
<li>Don’t claim “zero violations” or “perfect inspections” anywhere. Records change, and parents can check.</li>
</ul>"""),

            ("Texas Rising Star and CCS families", f"""<p>Child Care Services (CCS) scholarships are a big part of enrollment for many Houston centers. Families who qualify can choose any provider that accepts CCS, and once approved they have 14 days to pick one if they haven’t already, per {SRC['ccs']}.</p>
<p>In this area the program runs through {SRC['wsgc']}, which serves the {SRC['wsgc_13']}. Families apply through the statewide KinderConnect system, and there is a waitlist. In April 2026, {SRC['wsgc_wait']} cited an estimated 30,000 eligible children on scholarship waitlists in Harris County alone.</p>
<p>Texas Rising Star is the state’s quality rating for CCS providers. Per {SRC['trs']}, all regulated CCS providers must participate. New providers start at Entry Level and have 24 months to earn a star rating; Entry Level programs don’t get enhanced payment rates. The star levels are Two-Star, Three-Star and Four-Star, scored across four categories, with teacher-child interactions weighted at 40%.</p>
<p>For marketing, that means:</p>
<ul>
<li>If you accept CCS, say so clearly on your site and Business Profile. “We accept Child Care Services (CCS) scholarships through Workforce Solutions” is a phrase families search for, in English and Spanish.</li>
<li>If you’re Three- or Four-Star, put the rating on your homepage, tour page and ads. Workforce Solutions itself points families to Texas Rising Star certification as a quality credential.</li>
<li>Build a short “How CCS works at our center” page: how to apply, what documents families need, what happens if they’re on the waitlist, and whether you hold a spot.</li>
</ul>
<p>Families on the waitlist are still families. Many are working and paying privately while they wait, and they’ll remember the center that explained the process. If you serve a lot of Spanish-speaking families, our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'guide to Spanish-language marketing in Houston')} is worth a read.</p>"""),

            ("Google Ads for child care: keywords and negatives", f"""<p>Search ads work well for child care because the intent is clear and local. Keep campaigns tight.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Daycare (general)</td><td>daycare near me, child care the woodlands, daycare spring tx</td><td>Center page with tour booking</td></tr>
<tr><td>Infant care</td><td>infant daycare near me, infant care cypress, daycare for 6 month old</td><td>Infant room page (only when staffed)</td></tr>
<tr><td>Preschool / pre-K</td><td>preschool near me, pre k the woodlands, full day pre k</td><td>Preschool page with curriculum and hours</td></tr>
<tr><td>After-school</td><td>after school care near [school], after school program spring</td><td>After-school page with pickup schools</td></tr>
<tr><td>CCS families</td><td>daycare that accepts ccs, daycare that accepts workforce</td><td>CCS page</td></tr>
<tr><td>Summer camp</td><td>summer camp for kids the woodlands, summer day camp</td><td>Camp page (start in February)</td></tr>
</tbody></table></div>
<p>The negatives matter a lot here, because “daycare” collides with other searches:</p>
<ul>
<li><b>Pets:</b> dog daycare, doggy, pet, kennel, boarding.</li>
<li><b>Adults:</b> adult day care, senior, elderly, memory care.</li>
<li><b>Jobs:</b> jobs, hiring, teacher jobs, salary, CDA classes (run hiring separately).</li>
<li><b>Starting a business:</b> license, how to open, home daycare requirements, for sale.</li>
<li><b>Free or wrong program:</b> free daycare, Head Start (unless you are one), church nursery.</li>
</ul>
<p>Keep the radius to a few miles around the center and along the main commute route. Track booked tours and calls over a minute as conversions. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} explains the setup, and {L('/services/search-marketing/', 'our search team')} runs campaigns like these.</p>"""),

            ("Facebook and Instagram ads for parents, and what Meta won’t let you do", f"""<p>Meta is where Houston parents spend their phone time, and it’s good for tour days, open-seat announcements and summer camp. Ad targeting has gotten blunter, though.</p>
<p>Meta keeps removing and consolidating detailed targeting options. The latest round took effect January 15, 2026, and ad sets that used removed options stopped delivering, per {SRC['smt']}. Parent-based options still appear under Demographics in many accounts, but check what’s there in Ads Manager before you plan around it. In our experience, a tight radius around the center plus creative that clearly says “infant care in Shenandoah” finds parents better than stacked interests do.</p>
<p>Two policy traps:</p>
<ul>
<li><b>Personal attributes.</b> Meta ads can’t assert or imply things about the viewer, such as their age, financial situation or family status. “Struggling single mom?” gets rejected. “Full-day child care from 6:30 a.m., CCS accepted” is fine.</li>
<li><b>Hiring ads.</b> Teacher recruiting ads must run under the Employment special ad category, which fixes age at 18 to 65+, includes all genders, requires at least a 15-mile radius and removes lookalike audiences, per {SRC['loomer']}. Keep hiring and enrollment campaigns separate.</li>
</ul>
<p>What works: a 20-second phone video walking through a classroom with the teacher explaining the day, a tour-day event with a date and time, and a lead form with two questions (child’s age, desired start date). Our post on {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'fixing bad Facebook leads')} covers form settings, and {L('/services/paid-social-advertising/', 'our paid social team')} can run this side for you.</p>"""),

            ("The enrollment calendar: August, January and summer", f"""<p>Child care enrollment in Houston follows the school calendar more than the weather. Most districts here start in mid-August, which sets off a wave: 4-year-olds leave for public pre-K or kindergarten, older kids move up a room, and new families need full-day care when parents go back to work.</p>
<!--fig:season-->
<ul>
<li><b>February to April:</b> summer camp marketing and fall enrollment for families who plan ahead. Start tour campaigns here, especially for infant rooms.</li>
<li><b>May to July:</b> peak touring for August starts. This is when your tour follow-up has to be perfect.</li>
<li><b>August:</b> fill the gaps left by kids moving to school. Advertise specific open rooms with start dates.</li>
<li><b>September to November:</b> after-school programs and the families whose plans fell through.</li>
<li><b>January:</b> the second wave. Parents return to work after holidays and parental leave ends, and some families switch centers. Plan a tour push for the first two weeks of the year.</li>
</ul>
<p>Hurricane season is also real here. Have a closure and reopening communication plan ready for families, and update your Business Profile hours the same day you close. Our {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing guide')} covers the August push in more detail.</p>"""),

            ("From tour request to enrolled: the follow-up", f"""<p>Most of the money in daycare marketing is won or lost after the inquiry. Parents tour several centers, and the one that responds first and follows up best usually gets the deposit.</p>
<!--fig:tour-->
<p>Practical details:</p>
<ul>
<li>Respond to tour requests within the hour during business hours. A parent who requested a tour at lunch has probably requested two more.</li>
<li>Offer tour times before 9 a.m. and after 4:30 p.m. Working parents can’t always tour at 10.</li>
<li>Have the director, not whoever’s free, run the tour. Show the secure entry, the classroom the child will be in, and introduce the actual teacher.</li>
<li>Send a follow-up the same day with tuition, the enrollment packet, the safety page link and a deadline for holding the spot.</li>
<li>Call or text at day 3 and day 7. Most centers stop after the tour.</li>
</ul>
<p>Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead and follow-up')} goes deeper on building this into a CRM or child care management software.</p>"""),

            ("What to spend, and a first 90 days", f"""<p>For a single independent center in Houston or The Woodlands, this is an illustrative starting budget. Treat the ranges as examples, not quotes.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>Google Ads</td><td>$500 to $1,500</td><td>Search campaigns for open rooms, tours and CCS</td></tr>
<tr><td>Meta ads</td><td>$300 to $1,000</td><td>Tour days, open seats, summer camp</td></tr>
<tr><td>Local SEO and Business Profile</td><td>$400 to $1,200</td><td>Classroom pages, posts, photos, reviews</td></tr>
<tr><td>Hiring ads (separate)</td><td>$200 to $600</td><td>Teacher recruiting under the Employment category</td></tr>
</tbody></table></div>
<p>The first 90 days:</p>
<ol>
<li><b>Days 1 to 30:</b> map capacity by room, fix the Business Profile, build the safety and licensing page, set up online tour booking, and pull your state record.</li>
<li><b>Days 31 to 60:</b> launch search ads for staffed rooms only, start the review requests, and write the tour follow-up sequence.</li>
<li><b>Days 61 to 90:</b> add Meta tour-day campaigns, track tours to enrollment by source, and shift money toward what fills seats.</li>
</ol>
<p>The number to manage is cost per enrolled child, by classroom. Once you see that, you’ll stop paying to advertise a room you can’t staff.</p>
<p>If you run a center or a few and want a plan built around your rooms and your season, <a href="/contact/">get in touch</a>. For practices that work with kids, our {L(ORTHO, 'orthodontist marketing guide')} covers the parent decision from another angle.</p>"""),
        ],
        "faq": [
            ("How do I increase enrollment at my daycare?",
             "Start by listing which classrooms have open seats and staff to cover them, then market those rooms specifically. Fix your Google Business Profile, add an online tour scheduler, collect parent reviews after the first month, and build a safety and licensing page that links to your state record. Respond to tour requests within an hour and follow up at day 3 and day 7."),
            ("Can parents see my daycare’s inspection history in Texas?",
             "Yes. Texas HHS Child Care Regulation runs TXChildCareSearch.org, where parents can look up any regulated center and see inspections, deficiencies cited and corrective actions, with several years of compliance history and narratives for incidents. Many parents check before touring, so read your own record regularly and prepare honest, calm answers for any citation."),
            ("Do I need Texas Rising Star to accept CCS families?",
             "Yes. Texas requires all regulated Child Care Services providers to participate in Texas Rising Star. New providers start at Entry Level and have 24 months to earn a Two-, Three- or Four-Star certification, and Entry Level programs do not receive enhanced payment rates. Families can choose any provider that accepts CCS, so state clearly on your site and profile that you do."),
            ("Can I target parents with Facebook ads for my child care center?",
             "Partly. Meta still offers some parent-related demographic options in many accounts, but it keeps removing detailed targeting choices, so check Ads Manager first. A tight radius around your center with very specific creative usually works well. Ad copy cannot imply the viewer’s personal attributes, and teacher hiring ads must run under Meta’s Employment special ad category with its targeting limits."),
            ("When is the best time to advertise a daycare in Houston?",
             "Start tour campaigns in February for families planning fall enrollment, push hardest from May through August as the school year approaches, and run a second push in the first weeks of January when parental leave ends and families switch centers. Summer camp marketing should start in February too. Always advertise only rooms you can staff."),
        ],
        "figures": {
            "map": {
                "type": "map",
                "title": "Where parents look for child care",
                "sub": "Near home or on the commute: a few miles, not a county",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Cypress", "Tomball", "Katy", "Sugar Land", "Pearland", "Kingwood"],
                "alt": "Map of Houston and The Woodlands areas for daycare marketing, including Spring, Cypress, Katy and Pearland",
                "caption": "Target a tight radius around each center plus its main commute route.",
            },
            "ratios": {
                "type": "bars",
                "title": "Texas center ratios: children per caregiver",
                "sub": "Same-age groups, per the state’s FY2025-2027 child care plan",
                "items": [["Infants 0-11 months", 4, "1:4"], ["12-17 months", 5, "1:5"], ["18-23 months", 9, "1:9"], ["2-year-olds", 11, "1:11"], ["3-year-olds", 15, "1:15"], ["4-year-olds", 18, "1:18"]],
                "highlight": [0],
                "note": "Source: First Five Years Fund, from the Texas CCDF plan",
                "alt": "Bar chart of Texas child care center ratios by age for daycare marketing in Houston and The Woodlands",
                "caption": f"From the {SRC['ffyf']}. Check current Chapter 746 standards for group sizes.",
            },
            "season": {
                "type": "columns",
                "title": "When tour requests come in",
                "sub": "Relative tour demand by month for a suburban center",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [70, 55, 60, 65, 80, 90, 100, 85, 50, 40, 30, 20],
                "highlight": [0, 6],
                "y_label": "Relative demand",
                "note": "Illustrative example",
                "alt": "Column chart of seasonal daycare tour demand in Houston and The Woodlands, peaking in summer and January",
                "caption": "Your own inquiry data beats this shape. Pull it from last year’s tour log.",
            },
            "tour": {
                "type": "steps",
                "title": "From tour request to enrollment",
                "sub": "The follow-up most centers skip",
                "steps": [["Respond within an hour", "Text or call, offer early and late tour slots."], ["Confirm the day before", "Send directions, parking and who they’ll meet."], ["Director-led tour", "Secure entry, the actual classroom, the actual teacher."], ["Same-day follow-up", "Tuition, enrollment packet, safety page, hold deadline."], ["Day 3 and day 7", "A short check-in, then a final call before releasing the spot."]],
                "alt": "Five steps from tour request to enrollment for a daycare or child care center in Houston and The Woodlands",
                "caption": "Speed and the director’s tour do most of the selling.",
            },
        },
    },
]
