"""Batch 6: IV therapy marketing (drip bars + mobile IV, The Woodlands/Houston) and weight loss clinic marketing (GLP-1 programs, Houston).

Research: Texas HB 3749 enrolled text (elective IV therapy, Sec. 172.051 delegation to PA/APRN/RN, effective Sept 1, 2025),
Frier Levitt client alert on who is excluded, TMB February 2025 bulletin (IV hydration covered by med spa delegation
standards, advertising must feature the supervising physician's name), 22 TAC 169.25, 169.26, 169.28 and 164.3 via Cornell
LII, FTC 2018 iV Bars action (Texas clinics), Google Ads healthcare & medicines policy, restricted drug terms page and the
Oct 2025 policy update (US: Rx terms allowed in ads/landing pages, certification needed to keyword-target), Google's Health
sensitive-category page (no advertiser-curated audiences), Meta health & wellness, personal attributes and prescription drug
policies, Cardinal Digital on Meta's 2025 health data restrictions, Sterling Sky GBP category log ("IV therapy service",
Oct 2024), NWS Houston Aug 2023 summary, Community Impact on Ironman Texas dates through 2030, KFF Nov 2025 GLP-1 poll,
Foley on the Feb 21, 2025 semaglutide shortage resolution, Holland & Knight on FDA's Sept 2025 letters, Fierce Pharma on
the Feb 2026 batch of 30 letters, FTC NextMed final order (Dec 2025), LegitScript certification page.
Competitors read: PatientNow (IV therapy marketing), Valley Marketing Group (GLP-1 Google Ads 2026).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "hb": A("https://capitol.texas.gov/tlodocs/89R/billtext/html/HB03749F.HTM", "House Bill 3749"),
    "frier": A("https://www.frierlevitt.com/articles/client-alert-texas-medical-spas-must-prepare-for-new-regulations-on-elective-iv-therapy-effective-september-1-2025/", "Frier Levitt’s client alert"),
    "tmbb": A("https://www.tmb.texas.gov/index.php/file/bulletin-february-2025", "Texas Medical Board’s February 2025 bulletin"),
    "r16926": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-169-26", "22 TAC §169.26"),
    "r16928": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-169-28", "22 TAC §169.28"),
    "r1643": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-164-3", "22 TAC §164.3"),
    "ivbars": A("https://ftc.gov/news-events/press-releases/2018/09/ftc-brings-first-ever-action-targeting-iv-cocktail-therapy", "the FTC’s 2018 case against iV Bars"),
    "ghealth": A("https://support.google.com/adspolicy/answer/176031?hl=en", "healthcare and medicines policy"),
    "gterms": A("https://support.google.com/adspolicy/answer/15595717?hl=en", "restricted drug terms page"),
    "goct": A("https://support.google.com/adspolicy/answer/16606361", "October 2025 policy update"),
    "gsens": A("https://support.google.com/adspolicy/answer/16701855?hl=en", "Health sensitive-interest category"),
    "mattr": A("https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-attributes/", "personal attributes policy"),
    "mhw": A("https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/", "health and wellness ad policy"),
    "mrx": A("https://transparency.meta.com/policies/ad-standards/content-specific-restrictions/prescription-drugs", "prescription drug policy"),
    "cardinal": A("https://www.cardinaldigitalmarketing.com/healthcare-resources/blog/meta-announces-major-changes-healthcare-advertising/", "Cardinal Digital Marketing’s write-up"),
    "ssky": A("https://www.sterlingsky.ca/google-my-business-category-changes/", "Sterling Sky’s category change log"),
    "sab": A("https://support.google.com/business/answer/9157481?hl=en", "Google’s service area rules"),
    "nws": A("https://www.weather.gov/media/hgx/climate/summary/Aug_2023_Regional_Climate_Summary.pdf", "National Weather Service’s August 2023 summary"),
    "iron": A("https://communityimpact.com/houston/the-woodlands/government/2024/11/20/visit-the-woodlands-extends-ironman-dates-through-2030", "Community Impact"),
    "kff": A("https://www.kff.org/public-opinion/poll-1-in-8-adults-say-they-are-currently-taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-half-say-the-drugs-are-difficult-to-afford/", "KFF’s November 2025 poll"),
    "foley": A("https://www.foley.com/insights/publications/2025/02/glp-1-drugs-fda-removes-semaglutide-from-drug-shortage-list", "Foley & Lardner"),
    "hk": A("https://www.hklaw.com/en/insights/publications/2025/09/fda-hhs-taking-action-against-telehealths-compounded-drug-advertising", "Holland & Knight"),
    "fierce": A("https://www.fiercepharma.com/pharma/fda-ramps-crackdown-glp-1-drug-compounders-fresh-batch-30-warning-letters", "Fierce Pharma"),
    "nextmed": A("https://www.ftc.gov/node/326733", "final order against NextMed"),
    "legit": A("https://www.legitscript.com/certification/healthcare-certification/welcome-to-legitscript-certification/", "LegitScript"),
}

IV = "/blog/iv-therapy-marketing-the-woodlands-houston/"
WL = "/blog/weight-loss-clinic-marketing-houston-the-woodlands/"

POSTS = [
    # ------------------------------------------------------------------ post 1: IV therapy
    {
        "slug": "iv-therapy-marketing-the-woodlands-houston",
        "title": "IV Therapy Marketing in The Woodlands & Houston: A 2026 Playbook",
        "seo_title": "IV Therapy Marketing in The Woodlands & Houston",
        "desc": "IV therapy marketing for drip bars and mobile IV in The Woodlands and Houston: Texas rules after HB 3749, Google and Meta ad limits, memberships and seasons.",
        "category": "Paid ads",
        "icons": ["Google Business Profile", "Google Ads", "Meta"],
        "art": "b3",
        "hero": "iv",
        "hero_alt": "Illustration of an IV drip bag for a guide to IV therapy marketing in The Woodlands and Houston",
        "related": ["med-spa-marketing-the-woodlands-houston", "medical-practice-marketing-houston", "rank-in-google-map-pack-houston"],
        "sections": [
            (None, f"""<p>It’s 11:40 on a Sunday in late July. Someone at a brunch table on Market Street, still feeling Saturday night, types “iv hydration near me” into their phone. Whoever shows up first in the map pack, with a booking link and an RN who can be at their condo by 1:30, gets that client. Everyone else paid for a website.</p>
<p>IV therapy marketing in The Woodlands and Houston comes down to four jobs. You need to own the Google Maps results for “iv therapy near me” and turn one-time drips into memberships. You want corporate and event bookings that don’t depend on ad clicks. And every ad and page has to survive Texas’s 2025 IV law, Texas Medical Board rules, Google and Meta review, and the FTC.</p>
<p>Most drip bars skip that last one. It can shut down a campaign, or a clinic.</p>
<p>So we’ll start with the rules, since they decide which headlines you’re even allowed to run.</p>"""),

            ("What changed for Texas IV clinics in 2025, and why your ads care", f"""<p>Two things landed in 2025. In January, the Texas Medical Board’s reorganized rules took effect, and the {SRC['tmbb']} spelled out that its medical spa standards “now apply to all delegated medical acts, including IV Hydration therapy.” Then {SRC['hb']} took effect on September 1, 2025. It covers “elective intravenous therapy,” meaning IV fluids, nutrients or medications a patient seeks to relieve temporary discomfort or improve temporary wellness, given outside a physician’s office or licensed facility. That is the drip bar and the mobile IV van.</p>
<p>Under the law, a physician can delegate <i>ordering</i> elective IV therapy only to a PA or an APRN, and <i>administering</i> it only to a PA, APRN or RN, each under adequate physician supervision. {SRC['frier']} reads that as shutting out LVNs, paramedics, medical assistants and aestheticians from administering elective IVs. If your mobile model was built on paramedics, that’s a staffing problem first and a marketing problem second.</p>
<p>The parts that touch your marketing directly:</p>
<ul><li><b>Name the physician.</b> The TMB bulletin says “all advertising materials must feature the supervising physician’s name.” Separately, {SRC['r1643']} treats it as deceptive to hide medical directorship or delegation to non-physicians when care happens away from the physician’s primary practice under standing orders. Put the medical director’s name on the site footer, the booking page and the GBP description. Careful clients look for it, and they notice when it’s missing.</li>
<li>{SRC['r16928']} requires the delegating physician’s name and Texas license number, plus how to file a complaint with the TMB, posted in public areas and treatment rooms, and name tags showing each person’s credentials. Your lounge and team photos will show all of this, so get it right before the photographer shows up.</li>
<li><b>Drop “walk in and drip in 10 minutes.”</b> {SRC['r16926']} requires the physician, PA or APRN to establish a practitioner-patient relationship and keep a medical record before the delegated act, with someone BLS-trained on site. “Same-day appointments, intake takes about 15 minutes” is honest. “No questions asked” is a problem.</li>
<li>One upside: “Every IV started by a Texas RN” is now a claim you can actually back up. Put it in the headline.</li></ul>
<!--fig:rules-->
<p>We’re marketers, not lawyers. Have your healthcare attorney read your medical director agreement against HB 3749 before you spend on ads, and keep a copy of the delegation protocols handy. Ad reviewers and the TMB both ask about this stuff after a complaint, never before.</p>"""),

            ("IV therapy claims you can’t make (the FTC already sued a Texas drip bar)", f"""<p>This isn’t hypothetical. In {SRC['ivbars']}, the FTC went after A &amp; O Enterprises, doing business as iV Bars, which ran clinics in north Texas, New Braunfels and Vail. The company had advertised its “iV Cocktails” as treatments for cancer, congestive heart failure and multiple sclerosis. The FTC described the product as “a simple mix of water, vitamins, minerals, and herbs injected directly into the bloodstream,” and the order barred health claims without competent and reliable scientific evidence. Then-Chairman Joe Simons put it in one line: “Health claims must be supported by competent and reliable scientific evidence.”</p>
<p>Most Houston drip bars won’t claim to cure MS. The everyday risks are softer, and you’ve probably seen them on a sandwich board this week. “Boosts immunity.” “Detox.” “Cures your hangover.” “Anti-aging glutathione.” “Clinically proven.” Every one of those is a health claim, and if you can’t hand a regulator the study behind it, rewrite it.</p>
<!--fig:claims-->
<p>What tends to be safer is describing the service, the ingredients and the experience: fluids and electrolytes, B vitamins, the 45 minutes in a recliner, who starts the IV, what intake involves. “Feel ready for Monday” is a mood. “Eliminates hangover symptoms in 30 minutes” is a claim. We’d also keep testimonials honest; {SRC['r1643']} treats testimonials as deceptive without a note on the person’s credentials and a disclosure of any compensation, and models have to be identified as models. Our guide to the <a href="/blog/fake-reviews-rule-local-businesses/">FTC fake reviews rule</a> covers the review side.</p>"""),

            ("Can you run Google Ads for IV therapy?", f"""<p>Yes. There’s no IV-specific certification in Google Ads, and most drip bars run search campaigns without much trouble. Where they do hit friction, it traces back to Google’s {SRC['ghealth']}.</p>
<p><b>Prescription drug names.</b> Some add-ons are prescription drugs, such as ondansetron (Zofran) for nausea. Per Google’s {SRC['gterms']} and the {SRC['goct']}, US advertisers no longer need certification to mention prescription drug terms in ads and landing pages, but you “must be certified in order to keyword-target these terms.” So “anti-nausea add-on” in your ad text is fine, while bidding on “zofran iv near me” can get disapproved. We just don’t bid on drug names.</p>
<p><b>Audiences.</b> Google lists “invasive medical procedures, such as cosmetic surgery, surgery, or injections” under its {SRC['gsens']}. If your ads land in that bucket, advertiser-curated audiences, including Customer Match and your own remarketing lists, can’t be used. So the account runs on search intent and location, and your client list stays in your email and text tools where it belongs.</p>
<p>Telehealth is the third wrinkle. If you sell virtual consults that end in a prescription, Google treats you as a telemedicine provider, which in the US needs LegitScript accreditation plus Google certification. Most in-person drip bars aren’t in that group.</p>
<p>The campaign we’d build for a single-location drip bar in The Woodlands:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Core “near me”</td><td>iv therapy near me, iv hydration near me, iv drip the woodlands</td><td>Highest intent. Send to a booking page, not the homepage.</td></tr>
<tr><td>Mobile</td><td>mobile iv therapy, iv therapy at home, concierge iv spring tx</td><td>Separate ad group so you can show travel areas and minimums.</td></tr>
<tr><td>Recovery and wellness</td><td>iv hydration after workout, vitamin drip, b12 shot near me</td><td>Mixed intent. Watch the search terms report weekly.</td></tr>
<tr><td>Group and event</td><td>iv party, bachelorette iv hydration, corporate iv hydration</td><td>Low volume, high ticket. Use a quote form.</td></tr>
<tr><td>Negatives</td><td>jobs, certification, course, how to start, nurse salary, pole</td><td>Add on day one. “IV therapy” pulls a lot of job seekers.</td></tr>
</tbody></table></div>
<p>Set location targeting to “Presence: people in or regularly in your included locations.” The default also includes people merely interested in an area, and you don’t want to pay for someone in Ohio researching drip bars. Run call assets during staffed hours only. If you want a team that does this every day, that’s our <a href="/services/search-marketing/">search marketing</a> work.</p>"""),

            ("IV spa advertising on Facebook and Instagram", f"""<p>Meta works for IV, but mostly for awareness, offers and events. Someone who needs a drip in the next two hours is on Google, not scrolling Reels.</p>
<p>The policy that kills the most IV ads is Meta’s {SRC['mattr']}, which bans ads that assert or imply a personal health attribute. Its own rejected examples include “Do you have diabetes?” So “Hungover?” or “Feeling run down?” aimed at the viewer is the classic rejection, and we still see agencies submit it every summer. Describe the service: “Hydration drips in The Woodlands, started by an RN, about 45 minutes.”</p>
<p>The {SRC['mhw']} doesn’t mention IV at all. It does require 18+ targeting for weight loss and cosmetic offers and bans “negative self-perception” tactics, so if you bundle a beauty or slimming drip, those rules follow that ad. For anything that references drinking, we set the age floor at 21 by choice.</p>
<p>Then there’s data. Starting in early 2025, Meta began classifying health advertisers’ data sources and limiting which pixel events they can send; {SRC['cardinal']} describes tiers where some providers lose lower-funnel conversion events and custom conversions entirely. Meta instant forms and on-platform engagement carry more weight now. Before you assume your “Booked” event is still reaching Meta, open Events Manager and look.</p>
<p>A typical IV campaign from us is a short video of the actual lounge and the actual RN (no stock nurse in a lab coat), an intro offer for new clients and a lead form or booking link. We swap the creative every few weeks in summer because people tire of it fast. Our <a href="/services/paid-social-advertising/">paid social team</a> handles the policy back-and-forth so you don’t have to.</p>"""),

            ("How to get more clients for an IV hydration business from Google Maps", f"""<p>Most first-time IV clients search, scan the map pack, check reviews and book. Your Google Business Profile is the cheapest ad you’ll ever run.</p>
<ul><li><b>Primary category.</b> Google added “IV therapy service” as a category in October 2024, according to {SRC['ssky']}. If you still sit under “Medical spa” or “Health and beauty shop” from when you opened, test switching the primary to IV therapy service and keeping the others as secondary.</li>
<li><b>Mobile IV setup.</b> If you don’t see clients at an address, run as a service-area business. {SRC['sab']} allow up to 20 areas and an overall area no more than about two hours’ drive from your base. A Woodlands-based van might list The Woodlands, Spring, Conroe, Shenandoah, Oak Ridge North, Tomball, Magnolia and Kingwood.</li>
<li>List each drip as a service with a plain description and a starting price. People compare, and the bar that hides prices loses to the one that doesn’t.</li>
<li>Put the medical director’s name and “IVs started by Texas-licensed RNs” in the description. Those are the two things careful clients want to know.</li></ul>
<p>For photos, shoot the lounge, the team in name tags, the van and the bags (with brand-name drug labels turned away from the camera). Ask every client for a review by text about an hour after the session, with no incentive attached.</p>
<p>A GBP won’t rank you in Katy if you’re based off Woodlands Parkway. Distance still counts, and no amount of keyword stuffing changes that. For the ranking factors in more detail, see our guide to <a href="/blog/rank-in-google-map-pack-houston/">ranking in the Houston map pack</a>, and if you also sell injectables, our <a href="/blog/med-spa-marketing-the-woodlands-houston/">med spa marketing guide</a> covers that side.</p>"""),

            ("When IV demand spikes around The Woodlands and Houston", f"""<p>IV demand up here is predictable. You can usually see the busy weeks coming a month out.</p>
<p>Heat is the big one, and July and August are the long stretch. The {SRC['nws']} called August 2023 the warmest August on record at Bush Intercontinental, with an average high of 102.7°F and a peak of 109°F. Outdoor workers, golfers, weekend soccer parents and anyone who spent Saturday at a pool party end up searching for hydration.</p>
<!--fig:heat-->
<p>Race calendars come next. The 2027 Chevron Houston Marathon weekend is January 16 and 17. Ironman Texas is The Woodlands’ big one; {SRC['iron']} reported proposed race dates through 2030, including April 24, 2027, with athletes from all 50 states and 25 countries. Race weeks bring visitors in hotels near the Waterway, which is mobile IV territory. Be careful with athlete marketing, though: say “hydration and recovery drips,” not “perform better.”</p>
<p>Market Street and Waterway Square brunch traffic is steady every weekend. The group-booking peaks are December office parties, New Year’s Day, wedding weekends and bachelorette groups at the hotels.</p>
<!--fig:season-->
<p>For a typical Woodlands bar we’d raise search budgets in late June and hold them through Labor Day. Race-week mobile offers go live two weeks before each event, and group packages start getting pushed around mid-November, which feels early until you watch the December calendar fill. Pull your own booking history by month before you set any of this. It beats our chart.</p>"""),

            ("IV membership pricing that keeps clients coming back", f"""<p>One-off drips make for a jumpy calendar. A membership smooths it out, and the membership page is the one page on your site we’d fight hardest for.</p>
<p>Keep the structure simple. One drip a month at a member rate, a discount on add-ons and extra drips, priority mobile booking on weekends, and a guest pass every quarter (which is your referral program in disguise). Members should be able to see on one page what they pay, what they get, when they’re billed and how to cancel. The FTC’s recent weight-loss telehealth case, which we cover in our <a href="{WL}">weight loss clinic marketing guide</a>, turned largely on hidden recurring charges and slow cancellations. Don’t give anyone that opening.</p>
<p>A hypothetical to size it: a drip bar near Hughes Landing signs 120 members at $149 a month. That’s $17,880 a month before a single walk-in, with a known staffing load. Your price will differ. But “120 members” is a number you can plan ads around. “More clients” isn’t.</p>
<p>Rebooking matters as much as signing. We’d text clients about three to four weeks after each visit and check in when a member skips a month. A short note before the heat arrives in June works well too, as long as it doesn’t drift into health claims.</p>"""),

            ("Corporate, event and mobile IV: the channels that don’t need ad clicks", f"""<p>The drip bars we’d bet on get a third of their revenue from somewhere other than paid search. What these channels cost is phone calls and coffee meetings.</p>
<ul><li><b>Corporate wellness.</b> The office parks along Research Forest, Lake Robbins and the Springwoods Village campuses near I-45 and the Grand Parkway are full of HR teams planning health fairs and summer events. Offer an on-site hydration day with a set number of chairs and a per-person price. Check whether the employer’s benefits or legal team wants anything in writing first.</li>
<li><b>Hotels and concierges.</b> Business travelers and wedding parties staying near the Waterway ask the front desk. A one-page sheet with your RN credentials, medical director’s name and response time does more than a discount code.</li>
<li>Race expos, golf tournaments and charity runs. Get a booth at the expo. Skip the recovery tent at the finish line; medical tents are a different conversation.</li>
<li>CrossFit boxes, Pilates studios and run clubs will cross-promote if you bring them something, even just a member discount. Our <a href="/industries/sports-fitness/">sports and fitness</a> page shows how we market that crowd.</li>
<li><b>Bachelorette and wedding groups.</b> Build a group page with a minimum headcount, a travel fee and a deposit. These book months out.</li></ul>
<p>For mobile, publish your travel zones and minimums plainly. A flat travel fee inside The Woodlands, Spring and Shenandoah and a higher one for Conroe or Kingwood avoids awkward calls. And staff it to the law: under HB 3749 the person starting the IV at a client’s house has to be a PA, APRN or RN.</p>"""),

            ("What a starter IV therapy marketing budget looks like", f"""<p>These are ranges we’d plan with for a single location north of Houston. They’re illustrative, not quotes, and your clinic’s capacity should set the ceiling.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Typical monthly range</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>Google Ads search</td><td>$1,500 to $4,000 in ad spend</td><td>“Near me,” mobile and group searches in your service area</td></tr>
<tr><td>Meta ads</td><td>$800 to $2,500 in ad spend</td><td>Intro offers, membership promos, event pushes</td></tr>
<tr><td>GBP and reviews</td><td>Staff time, plus review software if you want it</td><td>Map pack visibility, the cheapest leads you’ll get</td></tr>
<tr><td>Website and booking</td><td>One-time build, then upkeep</td><td>Service pages, membership page, mobile zones, real booking</td></tr>
<tr><td>Corporate and events</td><td>Mostly time, plus booth fees</td><td>Group days, hotel and gym partnerships</td></tr>
</tbody></table></div>
<p>We’d rather a new drip bar spend $1,500 on tight search campaigns plus a real membership page than $4,000 on broad Meta ads pointed at a homepage. And we’ll admit we don’t have great data on how much mobile IV demand exists in the far suburbs like Magnolia or Montgomery. Test it with a small geo-targeted campaign before you add a second van.</p>
<p>Your next step: open your Google Ads search terms report for the last 30 days and count the clicks from job seekers, “how to start an IV business” and drug-name searches. If that number makes you wince, our free <a href="/contact/">Ad Spend Leak Check</a> goes further. We record a 10-minute video of your Google or Meta account and send it within 48 hours, showing exactly where the budget is leaking. We work with clinics across <a href="/digital-marketing-agency-spring-tx/">Spring</a>, <a href="/digital-marketing-agency-conroe-tx/">Conroe</a> and the rest of the north Houston suburbs.</p>"""),
        ],
        "faq": [
            ("How do I get more clients for my IV hydration business?", "Start with Google Maps: choose the IV therapy service category, list every drip with a price, name your medical director and ask every client for a review. Then run tight Google search ads on near-me and mobile terms, sell a monthly membership, and build corporate, hotel and gym partnerships. Memberships and partnerships usually add more steady revenue than extra ad spend."),
            ("Can you advertise IV therapy on Google Ads?", "Yes. There is no IV-specific certification. You can describe your drips and mention prescription add-ons in ad text and landing pages, but keyword-targeting prescription drug names requires Google certification. Health-related ads also can't use Customer Match or your own remarketing lists, and virtual prescribing services need LegitScript accreditation. Avoid disease or cure claims in every ad."),
            ("Do I need a medical director for an IV therapy business in Texas?", "Yes. Texas treats IV hydration as the practice of medicine, so a Texas-licensed physician must delegate and supervise it. Under HB 3749, effective September 1, 2025, only PAs and APRNs can be delegated ordering, and only PAs, APRNs and RNs can administer elective IVs. The Texas Medical Board also expects advertising to name the supervising physician."),
            ("Can paramedics or LVNs start IVs for a mobile IV company in Texas?", "Not for elective IV therapy under HB 3749. The law lets a physician delegate administration only to physician assistants, advanced practice registered nurses and registered nurses under adequate supervision. Healthcare attorneys read that as excluding LVNs, paramedics and medical assistants. Check your staffing and medical director agreement with a Texas healthcare attorney before you advertise mobile service."),
            ("What can't you say in IV therapy ads?", "Avoid claims that a drip treats, cures or prevents a disease, boosts immunity, detoxes the body or is clinically proven unless you have solid scientific evidence. The FTC took action against a Texas IV chain over claims like these in 2018. On Meta, also avoid copy that implies the viewer has a condition, such as asking if they are hungover or sick."),
        ],
        "figures": {
            "rules": {
                "type": "checklist",
                "title": "Texas IV ad compliance check",
                "sub": "What we confirm before an IV clinic’s ads go live",
                "items": [
                    "Supervising physician named on site, GBP and ads",
                    "Physician name, TX license and TMB complaint notice posted",
                    "Staff name tags show credentials",
                    "Only PAs, APRNs or RNs start elective IVs",
                    "Intake and exam happen before the first drip",
                    "No disease, cure, detox or immunity claims",
                    "Testimonials disclose any compensation",
                    "No bidding on prescription drug names",
                ],
                "alt": "Checklist of Texas rules to confirm before running IV therapy marketing in The Woodlands and Houston",
                "caption": f"Based on HB 3749 and Texas Medical Board rules; see the {A('https://www.tmb.texas.gov/index.php/file/bulletin-february-2025', 'TMB February 2025 bulletin')}.",
            },
            "claims": {
                "type": "compare",
                "title": "IV ad copy: risky vs safer",
                "left": {"title": "Claims that invite trouble", "items": ["Boosts your immune system", "Detoxes your body", "Cures your hangover fast", "Clinically proven results", "Hungover? We fix that."]},
                "right": {"title": "Copy we’d run instead", "items": ["Fluids, electrolytes and B vitamins", "Started by a Texas-licensed RN", "About 45 minutes in a recliner", "Medical director: Dr. [Name]", "Mobile service across The Woodlands"]},
                "alt": "Comparison of risky health claims and safer ad copy for IV therapy marketing in Houston and The Woodlands",
                "caption": f"The FTC’s position in {A('https://ftc.gov/news-events/press-releases/2018/09/ftc-brings-first-ever-action-targeting-iv-cocktail-therapy', 'the iV Bars case')}: health claims need competent and reliable scientific evidence.",
            },
            "heat": {
                "type": "stats",
                "title": "August 2023 at Bush Intercontinental",
                "stats": [["91°F", "Average temperature for the whole month"], ["109°F", "Peak temperature, reached twice"], ["#1", "Warmest August on record at IAH"]],
                "note": "Source: NWS Houston/Galveston, August 2023 climate summary",
                "alt": "Stat tiles on Houston's record August 2023 heat, a driver of IV hydration demand in The Woodlands and Houston",
                "caption": f"From the {A('https://www.weather.gov/media/hgx/climate/summary/Aug_2023_Regional_Climate_Summary.pdf', 'NWS August 2023 summary')}. Plan summer budgets before the heat, not during it.",
            },
            "season": {
                "type": "columns",
                "title": "A hypothetical Woodlands drip bar’s bookings",
                "sub": "Race weeks, summer heat and holiday parties set the peaks",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [74, 55, 60, 72, 66, 82, 96, 100, 70, 60, 64, 88],
                "highlight": [6, 7, 11],
                "y_label": "Relative bookings",
                "note": "Illustrative example",
                "alt": "Illustrative monthly bookings for an IV hydration spa in The Woodlands, peaking in July, August and December",
                "caption": "Your own booking history by month is the version of this chart to plan around.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: weight loss clinics
    {
        "slug": "weight-loss-clinic-marketing-houston-the-woodlands",
        "title": "Weight Loss Clinic Marketing in Houston & The Woodlands: GLP-1 Rules",
        "seo_title": "Weight Loss Clinic Marketing in Houston & The Woodlands",
        "desc": "Weight loss clinic marketing in Houston: what Google, Meta, the FDA, FTC and Texas Medical Board allow for GLP-1 ads, plus SEO, consult funnel and retention.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b5",
        "hero": "scale",
        "hero_alt": "Illustration of a bathroom scale for a guide to weight loss clinic marketing in Houston and The Woodlands",
        "related": ["medical-practice-marketing-houston", "med-spa-marketing-the-woodlands-houston", "landing-pages-101"],
        "sections": [
            (None, f"""<p>Scroll Instagram in Kingwood for ten minutes and you’ll see it: “$199 semaglutide, no insurance needed,” a smiling stock model, a countdown timer. Some of those ads come from out-of-state telehealth brands. Some come from clinics off FM 1960 that will be getting a letter. Your clinic is competing with both, for the same patient, with a fraction of their budget.</p>
<p>You won’t out-shout them on price. Weight loss clinic marketing in Houston and The Woodlands works when you compete on the things an app can’t fake, starting with a local physician who actually sees patients and follow-up visits that happen in a building. A straight answer about cost helps more than most clinics expect.</p>
<p>On the ad side, you need to know what Google, Meta, the FDA, the FTC and the Texas Medical Board each allow in a GLP-1 ad in 2026. Most clinics get at least one of those wrong, and a few manage all five.</p>
<p>Below is the playbook we’d run for a physician-led medical weight loss clinic north of Houston, rules first.</p>"""),

            ("Who is actually buying GLP-1 programs, and where", f"""<p>{SRC['kff']} found 12% of US adults currently taking a GLP-1 drug and 18% who had ever taken one. More than half of users (56%) said the drugs were difficult to afford, and 27% of insured users paid the full cost themselves.</p>
<p>The interesting number for you is where people got them. Most (76%) got them from a doctor, but 17% went through an online provider or website and 9% through a medical spa or aesthetic center. That 26% is your competitive set, and it’s why your ads keep running into theirs.</p>
<!--fig:kff-->
<p>Price is the first question, so hiding it costs you leads.</p>
<p>And because a big share of patients have already tried an app or a med spa, “in-person visits with a physician who checks your labs” actually means something to them. Plenty of the people calling you are on their second attempt, and they remember what the first one lacked.</p>"""),

            ("Can you advertise GLP-1 on Google?", f"""<p>Yes, with limits that changed in late 2025. Google’s {SRC['goct']} and its current {SRC['gterms']} say that for US campaigns, “you don’t need to be certified in order to use prescription drug terms in ads and landing pages.” So an ad or page can say semaglutide or tirzepatide. But “you must be certified in order to keyword-target these terms,” and certification is still required for online pharmacies, telemedicine providers and drug manufacturers.</p>
<p>In a real account, that plays out like this:</p>
<ul><li><b>Bid on the service, not the molecule.</b> “Medical weight loss near me,” “weight loss clinic the woodlands,” “weight loss doctor spring tx” and “glp-1 weight loss program” are where we start. Bidding on “semaglutide near me” or “ozempic clinic” without certification will draw disapprovals.</li>
<li>Under Google’s {SRC['ghealth']}, US telemedicine providers need LegitScript accreditation plus Google certification. If your program prescribes after a video visit with no in-person component, talk to us and your attorney about whether that applies before you launch.</li>
<li><b>No hCG.</b> Google’s unapproved substances list specifically includes products containing hCG “in relation to weight loss or weight control.” That old hCG diet page from 2014 still sitting on your site can get ads disapproved.</li>
<li>Health is a sensitive interest category. Google’s {SRC['gsens']} page covers chronic conditions and injections, and blocks advertiser-curated audiences like Customer Match, so whatever retargeting you do happens through content and email.</li></ul>
<p>Look at the search terms report and you’ll see how often “ozempic” searches still match your broad keywords. In uncertified accounts we add the brand drug names as negatives and move on. Our <a href="/services/search-marketing/">search marketing</a> team sets this up for clinics every month.</p>"""),

            ("How to advertise semaglutide without getting a warning letter", f"""<p>The compounding boom grew out of shortages, and the shortages are over. Per {SRC['foley']}, FDA declared the semaglutide shortage resolved on February 21, 2025, with enforcement discretion ending April 22, 2025 for 503A pharmacies and May 22, 2025 for 503B outsourcing facilities. Whether a pharmacy can still compound for a specific patient is a legal and pharmacy question. How you <i>advertise</i> it is a marketing question, and that’s where FDA has been looking.</p>
<p>On September 9, 2025, FDA and HHS announced a crackdown on misleading drug advertising, and {SRC['hk']} reported warning letters to several GLP-1 telehealth companies. Phrases FDA flagged included “Semaglutide (the same ingredient in Wegovy &amp; Ozempic),” “TIRZEPATIDE (GENERIC MOUNJARO)” and “Clinically proven ingredients.” In February 2026, {SRC['fierce']} reported another 30 letters, citing claims of the same active ingredients as the brand drugs, claims of clinical trial testing and implied FDA approval. The letters state plainly: “Compounded drug products are not FDA-approved.”</p>
<!--fig:timeline-->
<p>Copy rules we follow for any clinic that offers compounded medication:</p>
<ul><li>Never call a compounded product “generic Ozempic,” “the same as Wegovy” or anything similar.</li>
<li>Never say or imply it’s FDA-approved or clinically proven.</li>
<li>Lead with the program (physician visits, labs, dosing, nutrition support), not the drug.</li>
<li>If you offer both brand-name and compounded options, say which is which on the pricing page, in plain English.</li></ul>
<p>We’re not your regulatory counsel, and FDA’s position keeps moving. A healthcare attorney should look at your pricing page at least once a year (twice wouldn’t hurt, the way 2025 went).</p>"""),

            ("Meta’s rules for weight loss ads", f"""<p>Meta is where most clinics burn money, usually on rejected ads. The {SRC['mhw']} requires weight loss ads to target people 18 or older, bans a “side-by-side comparison after the use of a product or transformation for weight loss,” and prohibits ads that “imply or attempt to generate negative self-perception.” Add the {SRC['mattr']}, which bans ads that assert or imply a health condition about the viewer, and the usual weight loss headlines are gone: “Tired of your belly fat?”, “Struggling to lose weight?”, before-and-after splits.</p>
<p>Prescription drugs are another layer. Meta’s {SRC['mrx']} requires prior written permission for ads promoting prescription drugs, which it grants to online pharmacies, telehealth providers and drug manufacturers, and bars targeting under-18s. {SRC['legit']} certification is the usual route those businesses use to apply. For a brick-and-mortar clinic without that permission, the safe approach is to advertise the medical weight loss program and the consult, and keep drug names off Meta.</p>
<!--fig:copy-->
<p>Tracking got harder as well. Since early 2025, Meta has been restricting which conversion events health advertisers can send, and {SRC['cardinal']} describes condition-specific providers losing lower-funnel events altogether. Weight loss clinics tend to land in the stricter tiers, so Meta’s instant forms (which keep the lead on-platform) and a fast callback often beat a pixel-optimized landing page. More on running social for clinics on our <a href="/services/paid-social-advertising/">paid social</a> page.</p>"""),

            ("What the FTC and Texas Medical Board expect from your claims", f"""<p>The FTC’s {SRC['nextmed']} is the case every GLP-1 marketer should read. The FTC alleged that the telehealth company sold weight loss programs with undisclosed costs and membership commitments, made unsupported claims about how much weight clients lost, used fake testimonials and distorted reviews, and didn’t process cancellations and refunds promptly. The December 2025 order included $150,000 for consumer refunds and requires competent and reliable evidence for any average or typical results claim.</p>
<p>Texas adds its own layer. Under {SRC['r1643']}, the Medical Board treats these as deceptive advertising:</p>
<ul><li>Testimonials without a note on the person’s credentials and a disclosure of any compensation they received</li>
<li>Models or actors who aren’t identified as such (that stock photo of a smiling woman on a scale)</li>
<li>“Free consult” claims when a third party is billed</li>
<li>Claiming a unique or exclusive skill you can’t back up</li>
<li>Hiding medical directorship or delegation to non-physicians when care runs on standing orders away from the physician’s main practice</li></ul>
<p>If nurses or medical assistants give injections under delegation, {SRC['r16928']} also requires the delegating physician’s name and license number posted where patients can see it, and staff name tags showing credentials.</p>
<p>We use a blunt rule with clients. Every number in an ad (“patients lose an average of 15%”) needs your own documented patient data or a cited study, plus a clear “results vary.” If you can’t produce it in an afternoon, don’t print it. Our guide to the <a href="/blog/fake-reviews-rule-local-businesses/">FTC fake reviews rule</a> covers testimonials and review requests.</p>"""),

            ("Ranking for “medical weight loss near me”", f"""<p>Ads stop the day you stop paying. Your Google Business Profile and site pages keep working, and for “medical weight loss near me” the map pack usually gets the first look anyway.</p>
<p><b>Business Profile.</b> “Weight loss service” is the category most clinics in this space use as primary; if you’re a primary care or internal medicine practice adding a program, keep your medical category primary and add weight loss as secondary. Check the options in your own dashboard, since Google edits its category list. List your program as a service with a starting price, name the physician in the description, and post photos of the real clinic and staff. If you have a physician who sees most weight loss patients, an individual practitioner profile can rank alongside the clinic’s.</p>
<p>On the site, build one solid page per real search intent, written so a patient can follow it without a pharmacology degree.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Page</th><th>Target searches</th><th>Must include</th></tr></thead>
<tbody>
<tr><td>Medical weight loss program</td><td>medical weight loss near me, weight loss clinic the woodlands</td><td>Physician, visit schedule, labs, what happens at week 1, 4 and 12</td></tr>
<tr><td>GLP-1 options</td><td>glp-1 weight loss program, semaglutide program houston</td><td>Brand vs compounded explained honestly, who is a candidate, side effects</td></tr>
<tr><td>Pricing</td><td>semaglutide cost houston, weight loss clinic prices</td><td>Monthly price, what’s included, labs, cancellation terms</td></tr>
<tr><td>Insurance</td><td>does insurance cover wegovy, weight loss doctor that takes insurance</td><td>What you bill, what you don’t, prior authorization help</td></tr>
<tr><td>Location pages</td><td>weight loss clinic spring tx, medical weight loss kingwood</td><td>Only for towns where you have an office or real patient base</td></tr>
</tbody></table></div>
<p>The pricing page is the one most clinics refuse to build, and it’s usually the one that ranks. People search price because the online brands advertise price. Answer it. For the bigger SEO picture, our <a href="/services/web-design-seo-pr/">web design and SEO</a> team builds these pages, and our <a href="/blog/medical-practice-marketing-houston/">medical practice marketing guide</a> covers HIPAA-safe tracking on them.</p>"""),

            ("The consult funnel: from ad click to first dose", f"""<p>A weight loss lead cools off fast. Someone who filled out your form at 9 p.m. has probably also filled out two telehealth forms, and one of those will text them by 9:05.</p>
<!--fig:funnel-->
<p>The funnel we’d build:</p>
<ol><li>A short form or a call. Name, phone, email, best time. Keep health questions out of the ad form and collect them in your HIPAA-compliant intake.</li>
<li><b>Callback inside 15 minutes</b> during business hours, and a text that goes out automatically after hours with a booking link.</li>
<li>A paid consult. A modest fee, credited toward the first month, cuts no-shows. (If a third party is billed, don’t call it free.)</li>
<li>Labs and the visit, where the physician or APRN decides candidacy. Some people will hear no. Your marketing should never promise everyone qualifies.</li>
<li><b>First dose and week-one call.</b> Nausea in week one is where many patients quit, and a nurse call on day three keeps a surprising number of them.</li></ol>
<p>Measure each step weekly: leads, contacted, consults booked, shows, starts. If 60 leads become 8 starts, the leak is usually between “lead” and “contacted,” not in the ads. Our guide to <a href="/blog/landing-pages-101/">landing pages</a> covers the form side.</p>"""),

            ("Retention: months two through twelve are the business", f"""<p>A GLP-1 program’s profit is in the months after the first. Clinics that market well and retain poorly end up buying the same number of new patients every month just to stand still.</p>
<p>What keeps patients enrolled:</p>
<ul><li>Scheduled check-ins tied to dose changes, not just refills</li>
<li>Body composition or measurement tracking, so progress shows even when the scale stalls</li>
<li>Nutrition and strength support, in person or in small groups</li>
<li>A plateau script for staff, written with your physician, so nobody improvises medical advice</li>
<li>A maintenance plan for patients who reach their goal, so “done” doesn’t mean “gone”</li>
<li>Billing that matches the sign-up page exactly, with an easy cancel path</li></ul>
<p>A hypothetical: a clinic in The Woodlands starts 25 patients a month at $399 a month. If average stay goes from 4 months to 7, that’s an extra $29,925 in revenue from each month’s group with no extra ad spend. Your price and margins will differ.</p>
<p>Ask for reviews at a milestone visit. At sign-up, nobody has anything to say yet. And keep reviews and photos within the rules above: no paid testimonials without disclosure, and on Meta, no side-by-side transformations at all.</p>"""),

            ("Budget and timeline for a Houston weight loss clinic", f"""<p>Ranges we’d plan with for one location, illustrative and not a quote:</p>
<ul><li><b>Google search:</b> $2,000 to $6,000 a month in ad spend, focused on program and near-me terms in a tight radius around your office.</li>
<li><b>Meta:</b> $1,000 to $3,000 a month, program-focused creative with instant forms, refreshed every three to four weeks.</li>
<li>A pricing page and program page in month one, then insurance, location and FAQ pages over the next quarter.</li>
<li>Someone on staff who owns callbacks. This is not optional, and it’s the line item clinics most often leave blank.</li></ul>
<p>Search ads usually produce consults within the first couple of weeks. Meta takes a month or so of creative testing before it settles. Organic pages need three to six months to rank, sometimes longer in a crowded zip code.</p>
<p>We can’t predict how GLP-1 pricing from manufacturers and insurers will move next year, and we’re suspicious of anyone who says they can. So we’d build the brand on your physician and your follow-up. A $199 headline can be undercut by Friday.</p>
<p>Your next step: pull your Google Ads search terms for the last 60 days and look for “ozempic,” “wegovy,” “mounjaro” and “cheap.” Each one is either a policy risk or wasted spend. Want a second set of eyes? Our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute recorded video of your Google or Meta account, sent within 48 hours, showing where the budget is leaking. If you also run a drip lounge, our <a href="{IV}">IV therapy marketing guide</a> covers that side, and we work with clinics from <a href="/digital-marketing-agency-kingwood-tx/">Kingwood</a> to <a href="/digital-marketing-agency-katy-tx/">Katy</a>.</p>"""),
        ],
        "faq": [
            ("Can you advertise GLP-1 drugs on Google Ads?", "Yes, for US campaigns. Since Google's October 2025 update, advertisers don't need certification to mention prescription drug terms like semaglutide in ads and landing pages, but they must be certified to keyword-target those terms. Telemedicine providers and online pharmacies still need certification, which for telehealth includes LegitScript. Most local clinics bid on program terms like medical weight loss near me instead."),
            ("Do I need LegitScript certification to advertise semaglutide?", "It depends on your business model. Google requires LegitScript accreditation for US telemedicine providers, and Meta requires prior written permission for prescription drug ads, granted to online pharmacies, telehealth providers and manufacturers. A brick-and-mortar clinic that advertises its program without bidding on drug names usually doesn't need it, but confirm your model with your attorney before launching."),
            ("Can I use before and after photos in weight loss ads?", "Not on Facebook or Instagram. Meta's health and wellness policy bans side-by-side comparisons after weight loss, and bans ads that create negative self-perception. On your own website, real patient photos can be used with written consent and a results-vary note, and Texas Medical Board rules require disclosing any compensation and identifying models who aren't actual patients."),
            ("How do weight loss clinics get more patients?", "The clinics that grow steadily rank in Google Maps for medical weight loss near me, publish clear pricing, run search ads on program terms, and call new leads back within minutes. They also keep patients longer with scheduled check-ins, nutrition support and a maintenance plan. Retention often adds more revenue than extra ad spend because each patient stays for months."),
            ("Can I say compounded semaglutide is the same as Ozempic?", "No. FDA warning letters in 2025 and 2026 cited phrases such as the same ingredient in Wegovy and Ozempic and generic Mounjaro, along with claims of clinical testing or implied approval. Compounded drug products are not FDA-approved. Describe your program, your physician oversight and your pricing instead, and label brand and compounded options clearly."),
        ],
        "figures": {
            "kff": {
                "type": "stats",
                "title": "GLP-1 use among US adults",
                "stats": [["12%", "Currently taking a GLP-1 drug"], ["56%", "Of users say it was hard to afford"], ["17%", "Of users got it from an online provider"], ["9%", "Of users got it from a med spa"]],
                "note": "Source: KFF Health Tracking Poll, November 2025",
                "alt": "Stat tiles on GLP-1 use and cost from a KFF poll, context for weight loss clinic marketing in Houston",
                "caption": f"From {A('https://www.kff.org/public-opinion/poll-1-in-8-adults-say-they-are-currently-taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-half-say-the-drugs-are-difficult-to-afford/', 'KFF')}. Price and trust are the two things your marketing has to answer.",
            },
            "timeline": {
                "type": "steps",
                "title": "What changed for GLP-1 advertising",
                "sub": "The dates behind today’s rules",
                "steps": [
                    ["Feb 21, 2025", "FDA declares the semaglutide shortage resolved."],
                    ["Apr 22 and May 22, 2025", "Compounding enforcement discretion ends for 503A, then 503B."],
                    ["Sep 9, 2025", "FDA and HHS announce a crackdown on misleading drug ads, with GLP-1 telehealth letters."],
                    ["Oct 2025", "Google lets US ads name Rx drugs without certification; keyword targeting still needs it."],
                    ["Feb 2026", "FDA sends 30 more letters over compounded GLP-1 marketing claims."],
                ],
                "alt": "Timeline of FDA and Google changes that shape weight loss clinic marketing and GLP-1 ads in Houston",
                "caption": f"Sources: {A('https://www.foley.com/insights/publications/2025/02/glp-1-drugs-fda-removes-semaglutide-from-drug-shortage-list', 'Foley')}, {A('https://support.google.com/adspolicy/answer/16606361', 'Google Ads')} and {A('https://www.fiercepharma.com/pharma/fda-ramps-crackdown-glp-1-drug-compounders-fresh-batch-30-warning-letters', 'Fierce Pharma')}.",
            },
            "copy": {
                "type": "compare",
                "title": "Weight loss ad copy on Meta",
                "left": {"title": "Gets rejected or flagged", "items": ["Tired of your belly fat?", "Before and after split photo", "Generic Ozempic for $199", "Lose 30 lbs guaranteed", "Stock model as a patient"]},
                "right": {"title": "What we’d run", "items": ["Physician-led weight loss in Spring", "Real clinic, real staff on video", "Monthly price, what’s included", "Results vary, consult required", "Book a consult this week"]},
                "alt": "Comparison of rejected and compliant Meta ad copy for weight loss clinic marketing in Houston and The Woodlands",
                "caption": f"Based on Meta’s {A('https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/', 'health and wellness policy')} and FDA warning letter language.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From lead to first dose, one month",
                "stages": [["Leads", "60"], ["Reached by phone", "42"], ["Consults booked", "24"], ["Showed up", "17"], ["Started program", "12"]],
                "note": "Illustrative example",
                "alt": "Illustrative consult funnel for a Houston medical weight loss clinic from leads to patients starting a program",
                "caption": "Track these five numbers weekly; the biggest drop is usually before the first phone call.",
            },
        },
    },
]
