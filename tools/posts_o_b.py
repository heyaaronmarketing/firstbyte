"""Batch 15 (module b): collision repair / auto body shop marketing in Houston, and car wash membership marketing in
Houston and The Woodlands.

Research, collision post: Texas Insurance Code 1952.301 and 1952.302 (texas.public.law mirror: insurer may not limit
the choice of repair shop, may not state or imply a specific shop must be used, may not require unreasonable travel,
no referral fees to adjusters); TDI consumer column, Feb 2026 ("Choose the repair shop and parts for your vehicle");
Office of Public Insurance Counsel first-party claims page; State Farm newsroom (more than $5.6B in hail claims in
2025, Texas first at $1.4B); Insurance Journal on Cox Automotive's Harvey estimate (up to 500,000 vehicles, 160,000
auto claims per Insurance Council of Texas); I-CAR Gold Class standards (four roles at ProLevel 2, six credits a year,
ADAS technician for 2026 renewals when calibrating in-house); Google Local Services Ads category list (Auto Body Shop,
Towing, no Google Verified badge for auto); Google Ads help on the LSA-to-Performance-Max pay-per-lead migration
(phase one August 2026 for home services, other categories later); City of Houston Motorist Bill of Rights (choose your
tow destination, tow operators may not solicit); TDLR towing sanctions page; Greater Houston Partnership Economy at a
Glance, Dec 2025 (30.2% of metro residents speak Spanish at home); Insurance Journal on J&D Towing v. American
Alternative Insurance (Tex. 2016, loss-of-use damages in total-loss cases); Google Maps prohibited content policy.
Car wash post: Rinsed Q3 2026 report via Professional Carwashing & Detailing (memberships about 71% of same-store
revenue, retail down 9.6%, 7.8% monthly churn split 4.5% voluntary and 3.3% card, conversion 17.1% / 10.7% / 3.3% by
member count); Rinsed Q2 2026 (7.9% churn, voluntary 4.9%); ICA CAR WASH Pulse Q1 2026 (nearly 90% of members plan to
renew, nearly 79% would accept a price increase, saturation the top concern); ABC13 on the record March 2025 oak
pollen count (7,958 grains per cubic meter on March 20); ABC13 on lovebug flights (April-May and August-September);
KPRC Click2Houston April 2026 on lovebugs (spring and fall, acidic, wash quickly); Morgan Lewis on the Eighth
Circuit vacating the FTC click-to-cancel rule (July 8, 2025); Gibson Dunn on the FTC's March 11, 2026 ANPRM and ROSCA's
requirements; Federal Register notice of March 13, 2026; Jones Day (May 2026) on status and ~30 state laws;
Texas SB 838 (89R) text and BillTrack50 status (died in committee); Meta Marketing API basic targeting (radius 0.63 to
50 miles); Google Business Profile services help; Community Impact on Mint Express Car Wash's fifth Houston-area
location (Katy, Feb 2026) and Suds Deluxe's four new Houston sites.
Unverified and left out: hail claim counts specific to Houston or to auto lines, Texas-specific towing referral-fee
rules for consent tows, average car wash membership prices for Houston, LPR vendor accuracy claims.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # collision post
    "ins301": A("https://texas.public.law/statutes/tex._ins._code_section_1952.301", "Texas Insurance Code §1952.301"),
    "ins302": A("https://texas.public.law/statutes/tex._ins._code_section_1952.302", "§1952.302"),
    "tdi": A("https://tdi.texas.gov/column/insured-texas-drivers-have-a-consumer-bill-of-rights.html", "the Texas Department of Insurance"),
    "opic": A("https://www.opic.texas.gov/auto-insurance/first-party-claims", "Office of Public Insurance Counsel"),
    "sf_hail": A("https://newsroom.statefarm.com/state-farm-paid-over-56-billion-in-hail-claims-in-2025/", "State Farm"),
    "harvey": A("https://www.insurancejournal.com/news/southcentral/2017/09/11/463877.htm", "Insurance Journal"),
    "icar": A("https://info.i-car.com/gold-class/gold-class-collision-repair-standards", "I-CAR’s Gold Class standards"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "pmax": A("https://support.google.com/google-ads/answer/17213585", "Google’s migration notice"),
    "hou_tow": A("https://preflight.houstontx.gov/police/auto_dealers_detail/Forms/Motorist_Bill_of_Rights.pdf", "Motorist Bill of Rights"),
    "tdlr_tow": A("https://www.tdlr.texas.gov/enforcement/towsanctions.htm", "TDLR’s towing sanctions list"),
    "ghp": A("https://houston.org/houston-data/economy-at-a-glance-december-2025", "the Greater Houston Partnership"),
    "jd": A("https://www.insurancejournal.com/magazines/mag-features/2016/02/08/397219.htm", "J&amp;D Towing v. American Alternative Insurance"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy"),
    # car wash post
    "rinsed3": A("https://www.carwash.com/rinsed-q3-2026-quarterly-car-wash-industry-report/", "Rinsed’s Q3 2026 industry report"),
    "rinsed2": A("https://www.carwash.com/rinsed-q2-2026-quarterly-car-wash-industry-report/", "the Q2 report"),
    "ica": A("https://www.carwash.org/car-wash-exchange/car-wash-pulse-q1-2026-stable-demand-persists-as-price-sensitivity-and-market-saturation-rise", "International Carwash Association’s Q1 2026 Pulse survey"),
    "pollen": A("https://abc13.com/post/houston-oak-pollen-count-breaks-record-month-march/16057962/", "ABC13"),
    "lovebug13": A("https://abc13.com/lovebugs-insects-texas-gulf-coast/2332752/", "ABC13’s explainer"),
    "lovebug2": A("https://www.click2houston.com/news/local/2026/04/14/why-lovebugs-are-so-bad-in-houston-right-now-and-when-theyll-go-away/", "KPRC"),
    "ftc_vac": A("https://www.morganlewis.com/pubs/2025/07/ftcs-click-to-cancel-rule-vacated-ahead-of-planned-july-14-effective-date", "vacated the rule on July 8, 2025"),
    "ftc_anprm": A("https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/", "Gibson Dunn’s summary"),
    "fr": A("https://www.govinfo.gov/content/pkg/FR-2026-03-13/html/2026-04952.htm", "advance notice of proposed rulemaking"),
    "jones": A("https://www.jonesday.com/en/insights/2026/05/ftc-revives-clicktocancel-rule-new-risks-for-subscription-businesses", "Jones Day"),
    "sb838": A("https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00838I.htm", "SB 838"),
    "sb838s": A("https://www.billtrack50.com/billdetail/1789983", "died in committee"),
    "meta_r": A("https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting", "Meta’s targeting documentation"),
    "gbp_svc": A("https://support.google.com/business/answer/9455399?hl=en", "services section"),
    "mint": A("https://communityimpact.com/katy-fulshear/business/mint-express-car-wash-to-open-5th-greater-houston-location-in-katy/", "fifth Houston-area location"),
    "suds": A("https://communityimpact.com/bellaire-meyerland-west-university/business/suds-car-wash-to-open-several-new-locations-across-the-houston-area/", "four new Houston sites"),
}

BODY = "/blog/collision-repair-auto-body-marketing-houston/"
WASH = "/blog/car-wash-membership-marketing-houston-the-woodlands/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: collision repair
    {
        "slug": "collision-repair-auto-body-marketing-houston",
        "title": "Collision Repair and Auto Body Shop Marketing in Houston: Win the Claim Before the Adjuster Does",
        "seo_title": "Collision Repair & Auto Body Shop Marketing in Houston",
        "desc": "Auto body shop marketing in Houston: Texas right-to-choose rules, hail and flood demand, OEM certifications, photo estimates, tow partners, ads and reviews.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google"],
        "art": "b2",
        "hero": "shield",
        "hero_alt": "Illustration of a shield for collision repair and auto body shop marketing in Houston and The Woodlands",
        "related": ["auto-repair-shop-marketing-houston", "complete-guide-google-reviews", "hispanic-marketing-houston-spanish-ads-seo"],
        "sections": [
            (None, f"""<p>Monday, 8:15 a.m. A woman calls from a grocery store parking lot on Research Forest. Somebody backed into her Highlander on Saturday. She’s already filed the claim, and the app on her phone listed three “preferred” shops, none of them yours. Her neighbor told her to call you anyway. She wants to know one thing: “Is it going to be a problem with my insurance if I come to you?”</p>
<p>How your front desk answers that question decides more of your car count than any ad you’ll run this year.</p>
<p>Collision repair marketing in Houston comes down to being the shop a driver has already heard good things about before the adjuster suggests someone else. That means a Google profile with a lot of recent, specific reviews, a website that explains a customer’s rights in plain English, a two-minute photo estimate, and relationships with the tow operators and dealers who touch wrecked cars before you do. Paid search matters too, and it works best on top of all that.</p>
<p>We already wrote a broader {L('/blog/auto-repair-shop-marketing-houston/', 'auto repair shop marketing guide')} for mechanical shops. This one is only about body work: claims, storms, certifications and the referral web around a wreck.</p>"""),

            ("Insurance DRPs vs. customer choice: what Texas law says", f"""<p>Most Houston body shops live with a split personality. Some of your work comes through direct repair programs, where an insurer steers its customers to you in exchange for pricing concessions and paperwork rules. The rest comes from people who picked you on their own. Your marketing has to serve both without insulting either.</p>
<p>The legal ground is solid. Under {SRC['ins301']}, an insurer can’t limit a policyholder’s choice of repair person or facility on an auto policy issued in Texas, and on a third-party claim it can’t require the claimant to use a particular shop or particular parts. {SRC['ins302']} goes further: insurers, adjusters and their agents can’t state or imply that a customer must use a specific shop (or one on a preferred list) for the repair to be covered, can’t make someone drive an unreasonable distance, and can’t take a referral fee for steering a claim. A February 2026 consumer column from {SRC['tdi']} puts it simply: Texas drivers can “choose the repair shop and parts for your vehicle,” though insurers aren’t required to pay more than a reasonable amount. The state’s {SRC['opic']} says the same thing on its claims page.</p>
<p>That gives you a fair, true message. You don’t need to trash insurers to use it.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Situation</th><th>What the customer is worried about</th><th>What your page and phone script should say</th></tr></thead>
<tbody>
<tr><td>You’re on their insurer’s DRP</td><td>“Will this be easy?”</td><td>“We’re a direct repair shop for [carrier]. We can start the estimate today and handle the paperwork with your adjuster.”</td></tr>
<tr><td>You’re not on their insurer’s DRP</td><td>“Will they refuse to pay?”</td><td>“In Texas you choose the shop. We work with every major insurer and talk to your adjuster for you.”</td></tr>
<tr><td>Third-party claim (the other driver’s insurer)</td><td>“Their insurance picks, right?”</td><td>“The other driver’s insurer can’t require you to use a particular shop. Bring us the claim number.”</td></tr>
<tr><td>Supplement or parts disagreement</td><td>“Am I going to get a surprise bill?”</td><td>“If we find hidden damage, we send photos to the adjuster and update you by text before anything changes.”</td></tr>
</tbody></table></div>
<p>Two cautions from experience. Don’t put an insurer’s logo on your site as if you’re endorsed unless you actually have that relationship and permission. And don’t tell customers their insurer is “required to pay whatever we charge.” The TDI language about a reasonable amount exists for a reason, and overpromising here generates exactly the one-star review you’re trying to avoid.</p>
<!--fig:rights-->
<p>Put the rights message in three places: a short page called something like “Your right to choose a body shop in Texas,” a two-line block on every estimate page, and the first 20 seconds of how your writers answer the phone.</p>"""),

            ("Hail, flood and the Houston storm calendar", f"""<p>Body shop demand in Houston isn’t smooth. It comes in waves, and the waves are mostly weather.</p>
<!--fig:numbers-->
<p>Texas is the country’s hail state. {SRC['sf_hail']} said it paid more than $5.6 billion in hail-related claims nationally in 2025, and Texas topped its list at $1.4 billion (that figure covers all lines, homes included, not only cars). Spring storms that roll through Cypress, Tomball and The Woodlands can fill every paintless dent repair schedule in the county for weeks.</p>
<p>Floods are the other kind of wave, and they’re worse for most shops than they look. After Harvey, Cox Automotive estimated up to 500,000 cars and trucks were damaged or destroyed, and the Insurance Council of Texas counted 160,000 auto claims, per {SRC['harvey']}. Many flooded cars are totaled and go to auction instead of your bays. What you get is the long tail: electrical work on close calls and a lot of “is my car worth fixing?” calls.</p>
<p>What to do with that, practically:</p>
<ul>
<li><b>Build a hail page before you need it.</b> PDR vs. conventional repair, how hail claims and deductibles work, how long the wait is, and a photo estimate form. Publish it in January, not the Tuesday after a storm, so Google has had time to find it.</li>
<li><b>Pre-write storm ads.</b> Keep a paused campaign with “hail damage repair [town]” and “paintless dent repair near me” keywords, ad copy and a budget. When a storm cell crosses Spring and Klein, turn it on that night and set a geographic target around the path.</li>
<li><b>Expect out-of-town competition.</b> Traveling PDR crews follow big Texas storms. Your angle is permanence: a real shop, a warranty you’ll be around to honor, and reviews from neighbors.</li>
<li><b>After hurricanes and tropical storms</b>, lead with honest triage. A page titled “Was my car in floodwater? What to check before you file” earns trust and links. Most of those owners will need a decision more than a repair.</li>
</ul>"""),

            ("OEM certifications and I-CAR as trust signals", f"""<p>Drivers of newer cars, especially anything with lane-keep cameras, radar behind the bumper or aluminum panels, increasingly search with the brand in the query. “Tesla body shop Houston.” “Ford certified collision repair The Woodlands.” “Honda certified body shop Katy.” If you hold an automaker certification, that search is worth more than almost any generic keyword, and most shops bury the certificate in a footer badge.</p>
<p>Industry training credentials matter too, mostly as proof for the customer who’s never heard of them. {SRC['icar']} require four role-relevant technicians (estimator, refinish, structural and non-structural) trained to ProLevel 2, ongoing training credits every year, welding training for structural techs, and, for 2026 renewals, an ADAS technician on the roster if the shop does calibrations in-house. Customers don’t know any of that, so translate it.</p>
<!--fig:trust-->
<p>How we’d use certifications in marketing:</p>
<ul>
<li>A page per OEM certification you hold, titled with the brand and city, that explains what the program requires in plain language and shows photos of the actual equipment (frame bench, aluminum clean room, calibration targets).</li>
<li>A short paragraph on ADAS calibration on every estimate page. “After a bumper or windshield repair, cameras and sensors may need recalibration. We do it in-house and give you a printout.” That one sentence answers a fear many drivers now have.</li>
<li>Google Business Profile photos of certificates, technicians at work and the calibration bay. Real photos, refreshed monthly.</li>
</ul>"""),

            ("Photo estimates online: the two-minute form that beats “come in sometime”", f"""<p>Nobody wants to take a morning off to get an estimate. A shop that accepts photos from a phone, replies with a rough range, and books the in-person teardown gets the job far more often than one that says “stop by between 8 and 5.”</p>
<!--fig:photo-->
<p>Form design matters more than most shops think. Ask for the minimum: name, mobile number, year/make/model, a short damage description, whether a claim is filed, and four photos (the damage up close, the damage from six feet, the whole side of the car, and the VIN plate or the odometer). Make photo upload work on an iPhone without a separate app. Add an optional Spanish version of the form, more on that below.</p>
<p>Then answer fast. The difference between replying in 15 minutes and replying tomorrow is usually the difference between winning and losing the estimate, because the customer sent the same photos to two other shops. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the follow-up cadence we use, and it carries over to body work almost unchanged.</p>
<p>Be careful with the wording of your reply. A photo estimate is a range, and hidden damage behind the bumper cover is normal. Say so. “Based on your photos this looks like roughly [your price range]. Once we remove the bumper we’ll send your adjuster and you an exact estimate.”</p>"""),

            ("Tow companies, dealerships and the other people who touch a wreck first", f"""<p>A car that’s been towed from a wreck on I-45 or the Grand Parkway goes somewhere, and that first stop often becomes the repair shop by default. So referral partners are worth real effort.</p>
<p>A few ground rules in Houston. The city’s {SRC['hou_tow']} for police-ordered tows tells drivers they can be towed to a location of their choice and that tow operators may not solicit business at the scene. Texas regulates towing through TDLR, and {SRC['tdlr_tow']} includes violations for giving something of value to parking facility owners in connection with tows. We’re marketers, not lawyers, so before you set up any per-tow payment to a tow company, run it past someone who practices in this area. Build the relationship on service instead, which is what lasts anyway.</p>
<ul>
<li><b>Tow operators.</b> Make your shop the easy drop: after-hours key drop, a secured lot, a direct cell number for drivers, fast release of the tow bill so they get paid, and no arguments about storage. Drivers remember which shops make their night shorter.</li>
<li><b>Dealerships without body shops.</b> Many service departments in Spring, Conroe and along the I-45 corridor send collision work out. Dealers want OEM procedures, clean paperwork and a car that comes back without a new problem. Give them a named contact and a status report they can forward to their customer.</li>
<li><b>Insurance agents.</b> Independent agents get the “where should I take my car?” call before the adjuster does. A short visit with a one-page rights sheet and your photo-estimate link goes a long way. Our {L('/blog/insurance-agency-marketing-houston/', 'insurance agency marketing post')} shows what their week looks like from the other side.</li>
</ul>
<p>Track every partner as a lead source in your management system. Six months of real numbers usually beat the gut feeling about which tow company sends the most work.</p>"""),

            ("Google Ads and Local Services Ads for body shops in Houston", f"""<p>Search ads work for collision because the intent is so clear. Someone searching “auto body shop near me” at 9 p.m. has a dented car and a decision to make this week.</p>
<p>Local Services Ads are available for this vertical. {SRC['lsa']} includes Auto Body Shop and Towing among its auto categories, and notes that the Google Verified badge isn’t currently offered for auto categories. In August 2026 Google started moving LSA campaigns into Google Ads as Performance Max campaigns with pay-per-lead goals; per {SRC['pmax']}, the first phase covered home services like plumbing and HVAC, with other categories in later phases. If you run LSA as a body shop, expect an email about your migration and download your LSA reports before it happens, since historical performance reports don’t carry over.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Send to</th></tr></thead>
<tbody>
<tr><td>Core collision</td><td>auto body shop near me, collision repair Spring TX, body shop The Woodlands</td><td>Photo estimate page</td></tr>
<tr><td>Insurance claim</td><td>body shop that works with insurance, can I choose my own body shop Texas</td><td>Right-to-choose page</td></tr>
<tr><td>Hail and dents</td><td>hail damage repair Cypress, paintless dent repair near me</td><td>Hail page (seasonal campaign)</td></tr>
<tr><td>OEM / brand</td><td>Tesla certified body shop Houston, Ford collision repair Conroe</td><td>Matching certification page</td></tr>
<tr><td>Bumper and paint</td><td>bumper repair near me, car scratch repair Katy</td><td>Bumper and paint page with “starting at” ranges</td></tr>
</tbody></table></div>
<p>Negatives we’d add on day one: <i>jobs, hiring, technician, salary, school, class, course, DIY, how to, kit, touch up paint, Bondo, parts, junkyard, salvage, used, for sale, auction, Craigslist</i>. Then read the search terms report weekly for the first month.</p>
<p>Settings matter. Use location targeting for “people in or regularly in” your area, keep the radius to where people will actually bring a car (a shop in Tomball isn’t winning a fender bender in Pearland), and track calls and estimate form submissions as separate conversions. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} covers the setup, and {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} will help you sanity-check what you’re paying. If you’d rather hand the account to someone, that’s what our {L('/services/search-marketing/', 'search marketing team')} does.</p>"""),

            ("Reviews that sell the insurance experience", f"""<p>Collision customers read reviews looking for one thing: proof that you dealt with the insurance company so they didn’t have to. “Great shop!” helps your rating. “They handled everything with my State Farm adjuster and the paint match is perfect” sells the next job.</p>
<p>You can ask for specifics without scripting the customer. Send the review link by text the afternoon of pickup, with a prompt like this:</p>
<p><i>“Hi Maria, thanks for trusting us with your Camry. If you have a minute, a Google review helps other drivers in Spring find us. It’s especially useful if you mention how the insurance part went. [link]”</i></p>
<p>Stay inside {SRC['gpol']}: no discounts or detailing for reviews, no sending the link only to happy customers, no pressure on staff to hit review quotas. Federal rules on fake and incentivized reviews also apply, which we cover in our {L('/blog/fake-reviews-rule-local-businesses/', 'fake reviews rule post')}. Reply to every review, and for the bad ones about cycle time, explain what happened with parts and offer a direct number. The {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has reply templates.</p>"""),

            ("Spanish-language customers in Houston", f"""<p>After English, Spanish is by far the most common language spoken at home in the Houston metro: 30.2% of residents, according to {SRC['ghp']} using 2024 Census estimates. In parts of the metro it’s higher still, so check the numbers for your own ZIP codes.</p>
<p>Shops that serve Spanish-speaking customers well tend to do a few things:</p>
<ul>
<li>Have at least one bilingual estimator or writer, and say so on the Google profile and in ads (“Hablamos español”).</li>
<li>Build real Spanish pages for the right-to-choose explanation and the photo estimate form. Translated by a person, reviewed by someone on your staff. Machine-translated insurance language reads badly and can mislead.</li>
<li>Run a small Spanish search campaign with keywords like “taller de hojalatería y pintura cerca de mí” and “reparación de choques,” plus a Spanish ad set on Meta.</li>
<li>Send status texts in the customer’s preferred language. Ask on the intake form.</li>
</ul>
<p>We go much deeper in our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing in Houston guide')}.</p>"""),

            ("Rental car coordination: the message that settles the decision", f"""<p>The second question every collision customer asks, after “will my insurance pay,” is “what am I supposed to drive?” In a city where almost nobody can get to work without a car, a shop that sets up the rental gets chosen over one that doesn’t, often without a price comparison.</p>
<p>Rental reimbursement on the customer’s own policy is optional coverage with daily and total limits. On a third-party claim, Texas law lets a claimant recover loss-of-use damages, and in {SRC['jd']} in 2016 the Texas Supreme Court held those damages are available even when the vehicle is a total loss. Don’t give legal advice about any of that. Do make it clear that you’ll coordinate with the adjuster and the rental counter.</p>
<p>Copy that works on the site and in ads: <i>“We set up your rental with your insurance and the rental company, often before you drop off. We text you repair updates so you know when to return it.”</i></p>
<p>Then do it. Partner with a nearby rental branch, learn which carriers use which rental programs, and send cycle-time updates by text. Rental days are one of the main things adjusters watch, and a customer whose rental coverage runs out mid-repair writes your worst reviews. Keep those texts transactional; marketing texts need separate consent under Texas rules, covered in our {L('/blog/sms-marketing-small-business-texas-rules/', 'SMS rules post')}.</p>"""),

            ("What to track, what to spend and the first 90 days", f"""<p>Most shops know their car count. Few know which marketing produced it.</p>
<!--fig:funnel-->
<p>Tag every estimate request with its source: Google Ads, LSA, Google Maps, organic site, tow partner, dealer, insurance agent, DRP assignment, repeat customer. Then follow it to a repair order. It takes about three months to have numbers you can make decisions with.</p>
<p>On budgets, there’s no honest single number. For a single-location shop with steady DRP volume, an illustrative starting point might be $1,500 to $4,000 a month in search ads, a few hundred more in a storm season, plus review software and website work. Treat those as examples. Your capacity (how many repair orders you can actually take next month) should set the ceiling, because advertising into a six-week backlog makes your reviews worse.</p>
<!--fig:plan-->
<p>If you run a body shop anywhere from Conroe to Katy and want a plan built around your capacity, certifications and claim mix, <a href="/contact/">get in touch</a> and tell us where your work comes from today.</p>"""),
        ],
        "faq": [
            ("Can my insurance company make me use their body shop in Texas?",
             "No. Texas Insurance Code section 1952.301 says an insurer cannot limit your choice of repair shop under an auto policy issued in Texas, and on a claim against another driver’s insurance, that insurer cannot require you to use a particular shop. Section 1952.302 also bars insurers from implying you must use their preferred shop for coverage. Insurers generally only owe a reasonable amount, so ask your adjuster about any price differences."),
            ("How do auto body shops in Houston get more customers?",
             "The steady sources are Google Maps visibility backed by many specific reviews, a website that explains the customer’s right to choose a shop and offers photo estimates, search ads on collision and hail keywords, and referral relationships with tow operators, dealerships and insurance agents. DRP programs add volume at lower margins. Shops that answer estimate requests within minutes and coordinate rental cars win more of the jobs they’re offered."),
            ("Are Local Services Ads available for collision repair shops?",
             "Yes. Google lists Auto Body Shop as a Local Services Ads category, and Towing is listed separately. The Google Verified badge is not currently offered for auto categories. Google began migrating Local Services Ads into Performance Max campaigns with pay-per-lead goals in August 2026, starting with home services, so body shops should expect that change in a later phase and save their old reports first."),
            ("What should a body shop do after a hailstorm in The Woodlands or Cypress?",
             "Have a hail repair page and a paused hail campaign ready before storm season, then switch the campaign on the night of the storm with a geographic target around the affected area. Offer photo estimates, be honest about wait times, explain paintless dent repair versus conventional repair, and remind customers you’ll still be there to honor your warranty after traveling repair crews leave town."),
            ("Should a collision shop market in Spanish in Houston?",
             "In most of Houston, yes. About 30 percent of Houston metro residents speak Spanish at home, according to the Greater Houston Partnership’s analysis of 2024 Census data. A bilingual estimator, Spanish pages explaining insurance rights and photo estimates, a small Spanish search campaign and status texts in the customer’s preferred language usually pay for themselves. Use human translation for anything about insurance."),
        ],
        "figures": {
            "rights": {
                "type": "compare",
                "title": "Talking about customer choice",
                "left": {"title": "Backfires", "items": ["“Insurance shops cut corners”", "“Your insurer has to pay our price”", "Carrier logos you don’t have rights to", "Arguing with the adjuster in front of the customer"]},
                "right": {"title": "Works", "items": ["“In Texas, you choose the shop”", "“We work with every major insurer”", "“We talk to your adjuster for you”", "Photos of hidden damage sent to both"]},
                "alt": "Comparison of good and bad right-to-choose messaging for collision repair shop marketing in Houston",
                "caption": f"Based on {SRC['ins301']} and {SRC['ins302']}. Calm and factual beats combative.",
            },
            "numbers": {
                "type": "stats",
                "title": "Why Houston body shop demand comes in waves",
                "stats": [["$1.4B", "State Farm hail claims paid in Texas, 2025 (all lines)"], ["500K", "Vehicles Cox estimated Harvey damaged or destroyed"], ["160K", "Auto claims after Harvey (Insurance Council of Texas)"]],
                "alt": "Hail and flood statistics that drive collision repair demand in Houston and The Woodlands",
                "caption": f"Sources: {SRC['sf_hail']} and {SRC['harvey']}.",
            },
            "trust": {
                "type": "checklist",
                "title": "Trust signals a collision customer looks for",
                "sub": "Put each one on your site and Google profile, with real photos",
                "items": ["Current OEM certifications, one page per brand", "I-CAR status explained in plain English", "ADAS calibration done in-house or by a named partner", "Written lifetime or limited warranty", "Recent reviews that mention insurance and paint match", "Photos of your actual frame bench and paint booth", "Bilingual staff named on the profile", "Rental car coordination spelled out"],
                "alt": "Checklist of trust signals for auto body shop websites in Houston and The Woodlands",
                "caption": "Customers can’t judge a weld. They can judge whether you explained it.",
            },
            "photo": {
                "type": "steps",
                "title": "A photo estimate that books the teardown",
                "sub": "What happens in the first hour after a request",
                "steps": [["Short form", "Contact, vehicle, claim status, four photos. Mobile-first."], ["Instant text", "Automatic confirmation with the estimator’s name."], ["Range in 15 minutes", "A rough range and a caveat about hidden damage."], ["Book the visit", "Offer two drop-off times and rental setup."], ["Adjuster contact", "Claim number in, photos sent to the carrier."]],
                "alt": "Five steps of an online photo estimate process for a collision repair shop in Houston",
                "caption": "The range wins the conversation. The teardown wins the job.",
            },
            "funnel": {
                "type": "funnel",
                "title": "A month of collision estimate requests",
                "stages": [["Photo estimate requests and calls", "120"], ["Replied within 15 minutes", "95"], ["In-person estimate or teardown", "58"], ["Repair order opened", "34"]],
                "note": "Illustrative example",
                "alt": "Funnel of collision repair estimate requests to repair orders for a Houston auto body shop",
                "caption": "Illustrative numbers. Measure your own drop-off at each stage before changing ad spend.",
            },
            "plan": {
                "type": "steps",
                "title": "The first 90 days",
                "sub": "Order of work for a single-location body shop",
                "steps": [["Days 1-30", "Fix the Google profile, start review texts, build the right-to-choose page."], ["Days 31-60", "Launch the photo estimate form and core collision search ads."], ["Days 61-90", "Add hail and OEM ad groups, a Spanish page, partner visits."], ["Ongoing", "Source every repair order, review weekly, adjust to capacity."]],
                "alt": "Ninety-day collision repair marketing plan for a body shop in Houston and The Woodlands",
                "caption": "Pages before ads. Ads land better once the questions are answered.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: car wash memberships
    {
        "slug": "car-wash-membership-marketing-houston-the-woodlands",
        "title": "Car Wash Membership Marketing in Houston and The Woodlands: Sign Members, Keep Members",
        "seo_title": "Car Wash Membership Marketing in Houston & The Woodlands",
        "desc": "Car wash membership marketing for Houston and The Woodlands: pollen and lovebug seasons, grand openings, member lanes, churn, cancellation rules, Meta ads.",
        "category": "Local marketing",
        "icons": ["Meta", "Google Business Profile", "Google Ads"],
        "art": "b4",
        "hero": "car",
        "hero_alt": "Illustration of a car for car wash membership marketing in Houston and The Woodlands",
        "related": ["auto-detailing-marketing-the-woodlands-houston", "gym-presale-new-location-membership-launch", "geo-fencing-ads-target-customers-nearby"],
        "sections": [
            (None, f"""<p>Saturday in late March. Every car in Montgomery County is yellow. The retail line at your express tunnel backs up past the pay stations and onto the feeder road, while the member lane on the left moves with nobody in it but a few regulars who wave as they roll through.</p>
<p>Your site manager is happy. You’re doing the math on how many of those 40 cars in the retail line you’ll ever see again.</p>
<p>That’s the whole game in car wash membership marketing. Houston gives you a steady supply of dirty cars (pollen, lovebugs, rain, construction dust on the Grand Parkway). The money is in turning the person who washes once after a pollen storm into someone who pays monthly, and then keeping that card on file working for years.</p>
<p>This guide is for express tunnel operators and small chains in Houston, The Woodlands, Spring, Conroe, Katy, Cypress and the rest of the metro. It covers the numbers that matter, the seasonal calendar, grand openings, member lanes, churn, the current state of cancellation rules, and the ads.</p>"""),

            ("The membership math every Houston car wash should know", f"""<p>Memberships aren’t a side product anymore. According to {SRC['rinsed3']}, which tracks more than 3,000 locations, memberships made up about 71% of same-store revenue in the third quarter of 2026, up from 66% a year earlier. Same-store retail revenue fell 9.6% year over year, the steepest drop in five quarters.</p>
<!--fig:stats-->
<p>The same report shows the problem underneath. Average monthly churn was 7.8%, split between 4.5% voluntary cancellations and 3.3% from failed or expired cards. {SRC['rinsed2']} had churn at 7.9%, driven mostly by voluntary cancellations. And conversion of retail customers into members ran 17.1% at sites with more than 4,000 active members, 10.7% at sites with 2,000 to 4,000, and just 3.3% at sites under 2,000. Big membership bases convert better, which makes sense: the member lane is its own advertisement.</p>
<p>Members are mostly happy. The {SRC['ica']} found nearly 90% of unlimited members plan to renew and nearly 79% of customers say they’d accept a price increase, tied to quality and consistency. The same survey named market saturation as operators’ top concern for 2026.</p>
<p>You can see the saturation driving around Houston. Mint Express opened its {SRC['mint']} on the Grand Parkway in Katy in early 2026, and Suds Deluxe announced {SRC['suds']}. North of the Beltway, there are corners along FM 1960, Kuykendahl and Rayford where three tunnels sit within a couple of miles of each other.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Site</th><th>Active members</th><th>Monthly churn</th><th>Members lost per month</th><th>New members needed just to stay flat</th></tr></thead>
<tbody>
<tr><td>New site, year one</td><td>1,500</td><td>8%</td><td>120</td><td>120 (about 4 a day)</td></tr>
<tr><td>Established site</td><td>3,500</td><td>8%</td><td>280</td><td>280 (about 9 a day)</td></tr>
<tr><td>Same site, churn cut to 6%</td><td>3,500</td><td>6%</td><td>210</td><td>210 (about 7 a day)</td></tr>
</tbody></table></div>
<p>Illustrative example. At a typical churn rate, a busy site needs to sell nine memberships a day just to stand still. That’s why we spend as much time on retention as on acquisition with membership businesses.</p>"""),

            ("Houston’s dirt calendar: pollen, lovebugs and rain", f"""<p>Car washes in the Midwest plan around salt. Houston plans around bugs and trees.</p>
<p><b>Oak pollen.</b> Late February through April, Houston cars turn yellow-green. On March 20, 2025, the city of Houston’s sample hit 7,958 oak pollen grains per cubic meter, the highest March count since its records began in 2013, according to {SRC['pollen']}. Pollen weeks are the best retail traffic of the spring and your best chance to sell memberships to people who’ve just washed their car twice in five days.</p>
<p><b>Lovebugs.</b> They fly for up to about five weeks over April and May, and again over August and September, per {SRC['lovebug13']}. {SRC['lovebug2']} noted in April 2026 that their bodies are acidic and should be washed off quickly, and that they’re attracted to highways and traffic. Every commuter on I-45 and 99 is a prospect twice a year. If you have a bug prep step or a top package with extra front-end treatment, this is when to market it by name.</p>
<p><b>Rain.</b> Retail traffic drops when it rains and spikes on the first sunny day after. Members keep paying through the wet weeks, which is the whole argument for the model.</p>
<!--fig:calendar-->
<p>What to do with the calendar:</p>
<ul>
<li>Plan two big membership pushes a year: pollen season (February to April) and fall lovebugs (late August to September). Put extra budget, signage and attendant incentives behind both.</li>
<li>Write creative that names the problem. “Pollen pass: unlimited washes through spring” works better than a generic “Join today.”</li>
<li>Turn up Meta and search budgets the day after a big rain, and turn them down during it. Weather-based scheduling is simple to do by hand if you check the forecast every morning.</li>
<li>Use hurricane season the honest way. After a storm, cars are covered in debris and people want normal life back. A post about reopening hours and checking the tunnel matters more than an offer.</li>
</ul>"""),

            ("Grand opening free-wash weeks that turn into members", f"""<p>Free-wash weeks are standard for new tunnels across Houston, and most of them are wasted. A thousand free top-package washes buys a thousand people a nice day. Unless you capture who they are and give them a reason to join, you’ve mainly trained the neighborhood to wait for your next promotion.</p>
<!--fig:opening-->
<p>How we’d structure a launch:</p>
<ul>
<li><b>Start pre-selling 30 to 45 days out.</b> A founding-member rate for the first few hundred sign-ups, locked for a year, sold through a landing page and ads to a tight radius. It’s the same playbook as a gym presale, which we cover in our {L('/blog/gym-presale-new-location-membership-launch/', 'gym presale guide')}.</li>
<li><b>Make the free wash require a plate and a phone number.</b> If your system reads plates, the free wash creates a record you can follow up with. Get text consent at the pay station or on the form, separately from the wash itself.</li>
<li><b>Follow up within 48 hours.</b> “Thanks for coming to our opening. Your first month of unlimited is [your price] if you join by Sunday.” Then once more a week later, and stop.</li>
<li><b>Give attendants a reason to sell.</b> A small per-membership bonus during opening month turns greeters into closers. Keep it to explaining the plan, not pressure.</li>
</ul>
<p>Our {L('/blog/grand-opening-marketing-plan-30-days/', '30-day grand opening plan')} covers the broader launch calendar for any storefront.</p>"""),

            ("Member lanes, LPR and RFID: the lane is the ad", f"""<p>The member lane does more selling than any banner. A retail customer sitting in line watches members roll past without stopping, and that’s the pitch.</p>
<p>Most express washes now use either license plate recognition (a camera reads the plate and opens the gate) or an RFID tag on the windshield, sometimes with a barcode sticker as backup. Each one changes your marketing a bit.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>License plate recognition</th><th>RFID windshield tag</th></tr></thead>
<tbody>
<tr><td>Sign-up friction</td><td>Lowest. Sign up on a phone, drive through.</td><td>Needs a tag installed on site.</td></tr>
<tr><td>Online sales</td><td>Easy to sell fully online before the first visit.</td><td>Online sale, then tag install on the first visit.</td></tr>
<tr><td>Plate or vehicle changes</td><td>Paper tags and dealer plates cause misses. Make plate updates self-serve.</td><td>Tag moves only by replacing it. Windshield replacement means a new tag.</td></tr>
<tr><td>Marketing data</td><td>Visit frequency by plate, including retail visits you can match later.</td><td>Visit frequency for members only.</td></tr>
<tr><td>Privacy note</td><td>Say clearly what you capture and how long you keep it.</td><td>Same, simpler to explain.</td></tr>
</tbody></table></div>
<p>Practical moves either way: put the price of membership on a big sign facing the retail line, keep the member lane clear and fast (a slow member lane is anti-marketing), and train the attendant at the pay station to say one line to every retail customer who buys a top package: “Two of these a month and the unlimited plan pays for itself.” That line is usually true, and customers respect simple math.</p>"""),

            ("Churn and recurring billing: where most members actually go", f"""<p>Remember the split: 4.5% of members cancel on purpose each month and 3.3% leave because a card fails, per {SRC['rinsed3']}. The card failures are the easiest money you’ll ever recover, because most of those people never meant to leave.</p>
<!--fig:churn-->
<p>For voluntary churn, look at visit data. A member who washed eight times in March and zero times in June is about to cancel. A text in week three of no visits (“We miss your car. Rain’s done, the tunnel’s open till 8”) brings some back. A pause option for travel or a long summer away saves more than a discount, and a downgrade to a cheaper tier keeps the card on file.</p>
<p>Don’t try to solve voluntary churn by making cancellation hard. Customers who feel trapped leave anyway, then post about it on Nextdoor and Google. And as the next section explains, federal law already requires a simple way to stop recurring charges for online sign-ups.</p>
<p>Track churn by tier, by site and by sign-up month. Members who joined during a $1 first-month promotion often churn very differently from members who paid full price on day one. You need to know that before you run the next promotion.</p>"""),

            ("Click to cancel, ROSCA and Texas: where the rules stand", f"""<p>A lot of car wash operators heard in 2024 that the FTC’s “click to cancel” rule was coming. The status below is as of our last check in November 2026. This is a marketer’s summary; talk to your attorney about your specific sign-up flow.</p>
<ul>
<li><b>The 2024 rule is not in effect.</b> The Eighth Circuit Court of Appeals {SRC['ftc_vac']}, days before it was scheduled to take effect, because the FTC skipped a required preliminary regulatory analysis.</li>
<li><b>The FTC has restarted.</b> On March 11, 2026, the FTC announced an {SRC['fr']} on its Negative Option Rule, with comments due April 13, 2026, per {SRC['ftc_anprm']}. In May 2026, {SRC['jones']} described a new federal rule as likely on the horizon. We haven’t seen a final rule.</li>
<li><b>ROSCA still applies.</b> The Restore Online Shoppers’ Confidence Act requires businesses that sell subscriptions online to clearly disclose material terms before taking billing information, get the customer’s express informed consent, and provide a simple mechanism to stop recurring charges. The FTC keeps enforcing it.</li>
<li><b>Texas has no general auto-renewal statute.</b> {SRC['sb838']} in the 2025 session would have required clear sign-up disclosures, renewal notices for longer contracts, and online cancellation for online sign-ups. It {SRC['sb838s']}. Texas’s general consumer protection law still applies to misleading practices, and roughly 30 other states have their own automatic-renewal laws, according to Jones Day.</li>
</ul>
<p>Our advice is the same no matter how the rulemaking ends. State the price, the billing date and how to cancel right next to the sign-up button. Send a receipt by email or text. Let people cancel online, in the app or at the site without a phone call. It costs you a few members who would have stayed out of inertia, and it saves you the reviews, chargebacks and regulatory attention that inertia-based retention attracts.</p>"""),

            ("Geo-targeted Meta ads for car wash memberships", f"""<p>Car wash marketing is geography. Most of your members live or commute within a few miles of the tunnel, so paid social is about reaching those people often and cheaply.</p>
<p>On Meta, you can target a radius around an address as small as 0.63 miles or as large as 50, per {SRC['meta_r']}. For a single tunnel in The Woodlands near Woodforest or along Research Forest, we’d usually start with a 3- to 5-mile radius around the site and a second ad set around the commuter corridor feeding it (people who pass your exit on I-45 or the Grand Parkway every morning). Car washes aren’t a special ad category, so normal age and interest targeting is available. Broad targeting inside the radius usually works fine.</p>
<p>Creative that tends to work, in our experience:</p>
<ul>
<li>Short vertical video from inside the tunnel. Foam, lights, the dryer. It’s the most watchable 12 seconds you own.</li>
<li>A before-and-after of a pollen-covered or lovebug-covered hood. Specific and local.</li>
<li>Plain price math. “Unlimited washes: [your price]/month. One top wash: [your price]. You do the math.”</li>
<li>Seasonal hooks with an end date: “Pollen Pass, join by April 15.”</li>
</ul>
<p>Sample ad: <i>“Lovebug season on 99 is no joke. Unlimited washes at our Spring tunnel, member lane, no waiting. First month [your price]. Cancel anytime online.”</i></p>
<p>Send traffic to a sign-up page that works in under 90 seconds on a phone, with your plate number as the first field. Track completed sign-ups as the conversion, not page views. For tighter targeting around competitors and events, our {L('/blog/geo-fencing-ads-target-customers-nearby/', 'geo-fencing guide')} explains what’s possible; and if you want help running it, see our {L('/services/paid-social-advertising/', 'paid social services')}.</p>"""),

            ("Google Business Profile and search for car washes", f"""<p>“Car wash near me” is one of the most local searches there is. People type it while driving, and the map pack decides who gets the visit.</p>
<ul>
<li><b>Primary category:</b> Car wash. Add secondary categories only for services you really offer, such as car detailing service if you have a detail bay.</li>
<li><b>Services and products:</b> Use the {SRC['gbp_svc']} of your Business Profile to list each wash package and each membership tier with prices. Many washes leave this blank.</li>
<li><b>Hours:</b> Keep them exact, and update them for rain closures, holidays and maintenance days. A driver who shows up to a closed tunnel doesn’t come back.</li>
<li><b>Photos:</b> The entrance from the road, the member lane, the vacuums, the menu board. People want to know how to get in.</li>
<li><b>Posts:</b> Weekly in pollen and lovebug season, with the membership offer.</li>
</ul>
<p>Search ads are worth a test too. Keywords like “car wash membership near me,” “unlimited car wash The Woodlands” and “express car wash Spring TX” are high intent, and Car Wash also appears on {SRC['lsa']}. Negatives: <i>jobs, hiring, for sale, equipment, franchise, DIY, self service</i> (unless you have bays), <i>mobile</i> (unless you offer it), and competitor brand names if you don’t want to pay for them.</p>
<p>Reviews follow the same rules as everywhere: no free wash for a review, and no sending the link only to happy customers, per {SRC['gpol']}. Ask by text after a member’s third visit, when they’ve formed an opinion. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack ranking guide')} covers the rest of local search for Houston.</p>
<!--fig:area-->"""),

            ("Fleet accounts: memberships that come in bulk", f"""<p>One fleet account can equal 50 retail members, and it usually churns less. North Houston has plenty of candidates:</p>
<ul>
<li>Car dealerships and used-car lots that need inventory and loaner cars washed weekly.</li>
<li>Realtors and title companies, whose cars are part of the pitch.</li>
<li>HVAC, plumbing, pest and pool companies with branded vans that need to look like the business is doing well.</li>
<li>Apartment complexes and HOAs looking for a resident perk.</li>
<li>Rideshare and delivery drivers, who need clean cars for ratings and drive constantly.</li>
</ul>
<p>Build a one-page fleet offer: per-vehicle monthly pricing by fleet size, a single monthly invoice, a visit report by vehicle and a named contact. Then go sell it in person. A lunch drop at a dealership’s service department beats any ad for this. Track fleet accounts separately so their low churn doesn’t hide a retail retention problem.</p>"""),

            ("What to track and a 90-day plan", f"""<p>A short scoreboard, checked weekly:</p>
<ul>
<li>Retail cars, members and total cars per day</li>
<li>Retail-to-member conversion rate (by site, by attendant if you can)</li>
<li>Monthly churn, split voluntary vs. card failures</li>
<li>Card recovery rate on failed payments</li>
<li>Cost per new member from each ad channel</li>
<li>Average member visits per month and revenue per member</li>
</ul>
<!--fig:funnel-->
<p>An illustrative marketing budget for one established tunnel might be $1,500 to $4,000 a month across Meta and Google, with more for a grand opening and during pollen season. That’s an example, not a benchmark. Your real limit is cost per new member compared with what an average member is worth over their lifetime. If your average member pays for 14 months, you can afford to pay a lot more for one than most operators think.</p>
<p>A practical first 90 days: month one, fix the Business Profile, the sign-up page and the cancellation flow, and turn on card recovery. Month two, launch geo-targeted Meta and search ads to the membership page and train the pay station pitch. Month three, add churn texts based on visit data and build the fleet offer.</p>
<p>If you run a tunnel anywhere from Conroe to Katy and want a membership plan built around your sites and your numbers, <a href="/contact/">get in touch</a>. And if you also offer detailing, our {L('/blog/auto-detailing-marketing-the-woodlands-houston/', 'auto detailing marketing post')} covers that side.</p>"""),
        ],
        "faq": [
            ("How do car washes in Houston get more members?",
             "Most new members come from retail customers who already washed with you, so the pay station pitch, membership signage facing the retail line and a fast member lane matter most. Add geo-targeted Meta ads within a few miles of the site, a complete Google Business Profile listing every membership tier, and seasonal pushes during oak pollen season and the spring and fall lovebug flights, when Houston drivers wash most often."),
            ("What is a normal churn rate for car wash memberships?",
             "Rinsed’s Q3 2026 industry report, covering more than 3,000 locations, put average monthly churn at 7.8 percent: 4.5 percent voluntary cancellations and 3.3 percent from failed or expired cards. That means a site with 3,500 members can lose around 270 a month. Card recovery, pause options, downgrades and outreach to members who stop visiting are the main ways operators bring churn down."),
            ("Is the FTC click-to-cancel rule in effect for car wash memberships?",
             "No. The Eighth Circuit vacated the FTC’s 2024 click-to-cancel rule on July 8, 2025. The FTC started a new rulemaking in March 2026, and no final rule had been issued when we last checked. The federal ROSCA law still requires clear disclosure of terms, express consent and a simple way to stop recurring charges for online sign-ups, so easy online cancellation remains the safe practice."),
            ("Does Texas have an automatic renewal law for subscriptions?",
             "Texas has no general automatic-renewal statute for consumer subscriptions as of late 2026. Senate Bill 838 in the 2025 session would have required renewal notices and online cancellation for online sign-ups, but it died in committee. Texas’s general consumer protection law still covers deceptive practices, and federal ROSCA rules apply to online sign-ups. Check with an attorney if you sell memberships into other states."),
            ("When are lovebug seasons in Houston and The Woodlands?",
             "Lovebugs usually appear twice a year along the Texas Gulf Coast, flying for up to about five weeks over April and May and again over August and September. Rain affects how heavy the flights are. Their remains are acidic and stick to bumpers, hoods and windshields, so car washes in Houston, Spring and The Woodlands typically see strong demand and their best membership sign-up chances during those weeks."),
        ],
        "figures": {
            "stats": {
                "type": "stats",
                "title": "Car wash memberships by the numbers",
                "stats": [["71%", "Share of same-store revenue from memberships, Q3 2026"], ["7.8%", "Average monthly member churn, Q3 2026"], ["17.1%", "Retail-to-member conversion at sites with 4,000+ members"], ["~90%", "Members who say they plan to renew"]],
                "alt": "Car wash membership statistics for operators in Houston and The Woodlands: revenue share, churn, conversion",
                "caption": f"Sources: {SRC['rinsed3']} and the {SRC['ica']}.",
            },
            "calendar": {
                "type": "columns",
                "title": "Houston’s car wash demand calendar",
                "sub": "Relative dirt pressure by month: pollen, lovebugs, rain and heat",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [35, 60, 95, 90, 75, 50, 45, 70, 80, 50, 40, 35],
                "highlight": [2, 3, 8],
                "y_label": "Relative demand",
                "note": "Illustrative example based on pollen and lovebug timing; your own wash counts will differ",
                "alt": "Illustrative monthly car wash demand calendar for Houston and The Woodlands showing pollen and lovebug peaks",
                "caption": f"Oak pollen peaks in March ({SRC['pollen']}); lovebugs fly April-May and August-September ({SRC['lovebug13']}).",
            },
            "opening": {
                "type": "steps",
                "title": "Grand opening without wasted free washes",
                "sub": "A launch sequence for a new express tunnel",
                "steps": [["Day -45", "Founding-member presale page and tight-radius ads."], ["Day -14", "Signage, local Facebook groups, Business Profile live."], ["Opening week", "Free wash with plate and phone captured, consent asked."], ["Within 48 hours", "Text offer for the first month, then one reminder."], ["Day 30", "Measure members per free wash and cost per member."]],
                "alt": "Grand opening steps for a new express car wash in Houston, Spring or The Woodlands",
                "caption": "The free wash is the sample. The follow-up is the sale.",
            },
            "churn": {
                "type": "checklist",
                "title": "Churn fixes, roughly in order of payoff",
                "sub": "Start with the members who never meant to leave",
                "items": ["Card account updater turned on with your processor", "Automatic retries on failed payments", "Text and email when a card fails, with a one-tap update link", "Pause option for travel and summers away", "Downgrade path to a cheaper tier", "Text after three weeks with no visits", "Simple online cancellation with a short exit survey", "Churn reported by tier, site and sign-up month"],
                "alt": "Checklist for reducing car wash membership churn for Houston and The Woodlands operators",
                "caption": f"Card failures were 3.3% of members a month in {SRC['rinsed3']}.",
            },
            "area": {
                "type": "map",
                "title": "Membership trade area for a Woodlands-area tunnel",
                "sub": "Homes within a few miles, plus commuters on I-45 and the Grand Parkway",
                "highlight": ["The Woodlands", "Spring", "Shenandoah", "Conroe", "Tomball"],
                "note": "Illustrative example",
                "alt": "Map of an example car wash membership trade area around The Woodlands, Spring and Shenandoah near Houston",
                "caption": "Target where members live and where they drive every day, not the whole metro.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From retail wash to retained member",
                "stages": [["Retail washes in a month", "6,000"], ["Offered the plan at the pay station", "4,200"], ["Joined", "520"], ["Still a member after 6 months", "330"]],
                "note": "Illustrative example",
                "alt": "Funnel from retail car washes to retained members for a car wash in Houston and The Woodlands",
                "caption": "Illustrative numbers. Every stage has its own fix, and the last one is retention.",
            },
        },
    },
]
