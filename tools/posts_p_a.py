"""Batch 16a: irrigation and sprinkler company marketing (Houston and The Woodlands), pool cleaning and service company
marketing (Houston and The Woodlands), and appliance repair marketing (Houston).

Research, irrigation post: 30 TAC 344.70 (license number on vehicles and all advertising) and 344.71 (contracts, bids
and invoices must carry license number and the TCEQ notice; pass-through contracts must name the irrigator) via
Justia's Texas Administrative Code mirror; TCEQ landscape irrigation licensing page (LI, IT, II; $111 fee; three-year
license; license search); TCEQ GI-632c for builders; Houston Public Works Cross Connection Control Program (annual
backflow tests, TCEQ-licensed testers on the city's list, SwiftComply, citations up to $2,000 a day); Houston Public
Works current watering restrictions (Stage One rescinded May 29, 2024) and its Rachio smart controller discount
(2026 pricing and promo weeks); Community Impact on the Woodlands Water Agency defined irrigation schedule (10 MUDs,
in place since 2013); The Woodlands Township water conservation page (1 inch summer, half inch spring/fall);
ABC13 on Tomball Stage 2 (Aug. 2026) and Katy Stage 1 (Aug. 2026); ABC13 on 2023 heat and ~50 days without rain;
Texas Comptroller on the May 23-25, 2026 water-efficient products sales tax holiday; Google LSA category list (no
irrigation category; lawn care and landscaping categories exist).
Pool post: Google LSA list ("Pool cleaner," "Pool contractor"); TDLR 2019 guidance on residential appliance
installers and pool electrical devices; PoolDial on Texas having no statewide pool service license; Skimmer on
route buying (sliding multiple of monthly service revenue, density) and its 2026 State of Pool Service release
(1,600+ pros, 80%+ expect higher revenue, monthly billing most common); Texas Tribune on CenterPoint's 2.26 million
outages after Beryl; Google Maps prohibited content policy on reviews.
Appliance post: Google LSA list ("Appliance repair services"); Google Ads trademark policy (keywords unrestricted,
ad text restrictions, reseller exception covers replacement parts and compatible products or services); Google
Ads local services restricted businesses page (advanced verification applies to locksmith and garage door in the
U.S., not appliance repair); CBC Marketplace investigation of fake appliance repair listings; CBS News on Google's
March 2025 lawsuit over 10,000+ fake listings; Google Business Profile guidelines (service-area businesses hide
address, no virtual offices); EPA Section 608 Type I certification; TDLR electrician licensing exemptions for
appliance dealers, manufacturers and designees; ABC13 on Houston's record 2023 summer; PPC Land on Google's April
2026 review policy update.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # irrigation post
    "tac70": A("https://regulations.justia.com/states/texas/title-30/part-1/chapter-344/subchapter-g/section-344-70", "30 TAC §344.70"),
    "tac71": A("https://regulations.justia.com/states/texas/title-30/part-1/chapter-344/subchapter-g/section-344-71", "30 TAC §344.71"),
    "tceqli": A("https://www.tceq.texas.gov/goto/irrigator", "TCEQ’s landscape irrigation licensing page"),
    "gi632c": A("https://www.tceq.texas.gov/downloads/publications/gi/gi-632c.pdf/@@download/file/GI-632c Hiring Licensed for Builders.pdf", "TCEQ’s guide for builders hiring irrigators"),
    "hpwbf": A("https://houstonpublicworks.org/cross-connection-control-program", "Houston Public Works’ Cross Connection Control Program"),
    "hpwrest": A("https://www.houstonpublicworks.org/current-watering-restrictions", "Houston Public Works’ watering restrictions page"),
    "hpwsmart": A("https://houstonpublicworks.org/smart-irrigation-controller-program", "Houston Public Works’ smart controller program"),
    "ciwwa": A("https://communityimpact.com/houston/the-woodlands/weather/2023/09/25/the-woodlands-follows-existing-irrigation-schedule-as-drought-persists-in-montgomery-county", "Community Impact"),
    "twtwater": A("https://www.thewoodlandstownship-tx.gov/Departments/Environmental-Services/Water-Conservation", "The Woodlands Township’s water conservation page"),
    "tomball": A("https://abc13.com/story/tomball-enters-stage-2-drought-restrictions-amid-dry-conditions/19630530/", "ABC13 reported"),
    "katy": A("https://abc13.com/story/city-katy-enters-stage-1-drought-contingency-plan-officials-say/19733811/", "Katy moved to Stage 1"),
    "heat23": A("https://abc13.com/texas-weather-2023-events-top-moments-in-southeast-record-heat/14227015/", "ABC13’s 2023 weather recap"),
    "taxhol": A("https://comptroller.texas.gov/about/media-center/news/20260519-sales-tax-holidays-for-water-efficient-and-energy-starr-products-set-for-may-23-25-1779119182554", "Texas Comptroller"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    # pool post
    "tdlrpool": A("https://www.tdlr.texas.gov/news/2019/01/08/residential-appliance-installers-authorized-scope-of-work-and-service-pool-related-electrical-devices", "TDLR’s guidance on pool electrical devices"),
    "pooldial": A("https://www.pooldial.com/resources/articles/business/texas-pool-contractor-license", "PoolDial’s rundown of Texas pool licensing"),
    "skroutes": A("https://www.getskimmer.com/blog/buying-and-selling-pool-service-routes", "Skimmer’s guide to buying and selling routes"),
    "sk2026": A("https://www.getskimmer.com/blog/skimmer-releases-2026-state-of-pool-service-report-highlighting-a-more-disciplined-digital-industry", "Skimmer’s 2026 State of Pool Service report"),
    "beryl": A("https://texastribune.org/2024/07/11/centerpoint-power-restore-texas-houston-when-why-timeline", "the Texas Tribune"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    # appliance post
    "tm": A("https://support.google.com/adspolicy/answer/6118?hl=en", "Google’s trademark policy"),
    "lsrestrict": A("https://support.google.com/adspolicy/answer/13527633?hl=en", "Google’s restricted local services page"),
    "cbc": A("https://amp.cbc.ca/news/canada/appliance-repair-industry-online-listings-1.5762489", "a CBC Marketplace investigation"),
    "cbs": A("https://www.cbsnews.com/news/google-maps-fake-listings-lawsuit-scams/", "CBS News"),
    "gbpguide": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s Business Profile guidelines"),
    "epa608": A("https://www.epa.gov/section608/types-technician-certification", "EPA Section 608"),
    "tdlrex": A("https://www.tdlr.texas.gov/ELECTRICIANS/exemptions.htm", "TDLR’s electrician licensing exemptions"),
    "ppcl": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
}

IRR = "/blog/irrigation-sprinkler-marketing-houston-the-woodlands/"
POOL = "/blog/pool-cleaning-service-marketing-houston-the-woodlands/"
APPL = "/blog/appliance-repair-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: irrigation
    {
        "slug": "irrigation-sprinkler-marketing-houston-the-woodlands",
        "title": "Irrigation and Sprinkler Company Marketing in Houston and The Woodlands",
        "seo_title": "Irrigation & Sprinkler Marketing: Houston, The Woodlands",
        "desc": "Marketing for irrigation and sprinkler companies in Houston and The Woodlands: TCEQ ad rules, backflow testing, watering schedules, Google Ads and builders.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google Analytics"],
        "art": "b2",
        "hero": "lawn",
        "hero_alt": "Illustration of a green lawn for irrigation and sprinkler company marketing in Houston and The Woodlands",
        "related": ["how-to-get-more-lawn-care-customers-the-woodlands", "local-services-ads-vs-google-ads-home-services", "how-to-get-commercial-landscaping-contracts-houston"],
        "sections": [
            (None, f"""<p>Monday morning in late July, after a weekend in the upper 90s. Fourteen voicemails. Three are broken heads the mow crew clipped on Friday. Two are controllers blinking after a power blip. One is a homeowner in Alden Bridge with a letter from the HOA about a brown front yard. One is a builder’s superintendent asking whether you can take six new installs in a Conroe subdivision next month.</p>
<p>And your Google Ads account spent $212 over the weekend on people searching “how to fix a sprinkler head yourself.”</p>
<p>Irrigation and sprinkler company marketing in Houston and The Woodlands comes down to three jobs. Win the repair call when something breaks. Turn that call into a yearly maintenance and backflow account. Build a short list of builders and landscapers who hand you installs. Most sprinkler companies we talk to are decent at the first job, accidental at the second and lucky at the third.</p>
<p>This post covers all three, starting with the Texas licensing rules that shape your ads before you write a word of copy.</p>"""),

            ("What sprinkler customers in Houston and The Woodlands actually search for", f"""<p>Irrigation demand isn’t one market. A homeowner in Spring with a geyser in the side yard is a very different buyer from a builder in Magnolia pricing 40 lots, and they search differently.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Job type</th><th>What they type</th><th>Urgency</th><th>Where it usually comes from</th></tr></thead>
<tbody>
<tr><td>Repair</td><td>sprinkler repair near me, broken sprinkler head, sprinkler zone not working Spring TX</td><td>High. Water bill or HOA letter is on the counter.</td><td>Google Maps, search ads, Nextdoor</td></tr>
<tr><td>Controller and smart upgrades</td><td>sprinkler controller replacement, smart irrigation controller install</td><td>Medium</td><td>Search, existing customers, rebate season</td></tr>
<tr><td>Backflow testing</td><td>backflow testing Houston, backflow test The Woodlands</td><td>Deadline-driven</td><td>Utility notices, reminders, property managers</td></tr>
<tr><td>New install</td><td>sprinkler system installation Katy, irrigation installation cost</td><td>Low to medium, price shopped</td><td>Search, builders, landscapers, pool builders</td></tr>
<tr><td>Drainage and drip</td><td>yard drainage Houston, drip irrigation for flower beds</td><td>Spikes after big rain or a dry month</td><td>Search, landscapers</td></tr>
<tr><td>Commercial and HOA</td><td>commercial irrigation maintenance, irrigation contractor for HOA</td><td>Contract cycles</td><td>Outreach, property managers, bids</td></tr>
</tbody></table></div>
<p>Repair is where most companies should spend first, because the intent is obvious and the ticket often turns into a maintenance plan. Installs are worth chasing too, but they’re the most price-shopped job you do, and builders and landscapers will send you more of them than ads will.</p>
<p>One Houston quirk: a lot of summer “sprinkler” searches are really about a shocking MUD water bill. If you do leak detection, say so in plain words on your Business Profile.</p>"""),

            ("Your TCEQ license number belongs on every ad", f"""<p>Texas is stricter about irrigation advertising than most owners realize. Under {SRC['tac70']}, every advertisement for irrigation services, in any medium, must include the license number. If the ad names a company or person other than the licensed irrigator, it has to name the irrigator and show that person’s license number too. Vehicles used for irrigation work need the license number with the “LI” prefix in block letters at least two inches high on both sides, and trailers that advertise irrigation services need the number as well.</p>
<p>Paperwork gets the same treatment. {SRC['tac71']} requires bids, proposals, estimates and invoices for installing or repairing a system to show the irrigator’s name, license number, business address and phone, along with the TCEQ notice that begins “Irrigation in Texas is regulated by the Texas Commission on Environmental Quality.” Installation contracts must be written, signed, carry the irrigator’s seal and state the warranty dates.</p>
<!--fig:license-->
<p>{SRC['tceqli']} explains who can do what. A Landscape Irrigator (LI) can sell, design, install, maintain, repair and service systems. An Irrigation Technician (IT) can connect systems to the water supply and do repairs, but works under an LI’s supervision. An Irrigation Inspector (II) checks systems for compliance and can’t work for an irrigation company at the same time. Licenses cost $111, run three years, and anyone can look one up on TCEQ’s license search.</p>
<p>We treat this as a marketing asset. Hardly anyone checks a plumber’s license before calling. Irrigation is different, because HOAs, builders and property managers do check, and a homeowner who just got burned by a mow-and-blow crew “fixing” their system often looks too. So we put the LI number in the Google Business Profile description, the website footer, every landing page, the truck wrap and the Meta ad image. Search ads have tight character limits, but a callout like “TCEQ Licensed Irrigator LI [your number]” fits, and the landing page carries the rest.</p>
"""),

            ("Backflow testing in Houston: the reminder that sells itself", f"""<p>Backflow testing is the most underrated revenue line in the business, because the customer doesn’t have to be persuaded. The utility persuades them.</p>
<p>In the City of Houston, testable backflow assemblies have to be tested at least once a year and again whenever they’re installed, repaired or relocated, according to {SRC['hpwbf']}. Testers must hold a current TCEQ backflow prevention assembly tester license and be approved on the city’s testing company list, and results get uploaded through SwiftComply. Properties that fall out of compliance can face citations of up to $2,000 per day and possible suspension of water service. Many MUDs and suburban utilities in Cypress, Katy, Pearland and Montgomery County run their own programs with their own deadlines, so check each one you serve.</p>
<!--fig:backflow-->
<p>The marketing is mostly a calendar. Every test you run creates a due date 12 months out. Put it in your field software, send a reminder text 45 days ahead, then 21, then 7. Offer a combined “backflow test plus system check” visit, which is how a [your price] compliance call turns into the summer repair work you’d otherwise have chased with ads.</p>
<p>Landing pages help here too. Build one page per utility area you test in (“Backflow testing in the City of Houston,” “Backflow testing in The Woodlands”), each explaining that area’s process in plain English and linking to the official source. Those pages rank for low-competition searches all year, and property managers bookmark them.</p>"""),

            ("Watering schedules by city and MUD are free content", f"""<p>Watering rules around Houston change by city, by MUD and by summer. That’s a headache for homeowners and an opening for you.</p>
<p>In The Woodlands, the Woodlands Water Agency manages the 10 municipal utility districts and has run a defined irrigation schedule since 2013, per {SRC['ciwwa']}. Odd-numbered addresses run automatic sprinklers overnight starting Tuesday and Saturday evenings, and even-numbered addresses start Wednesday and Saturday evenings, with drip and hand watering allowed any time. {SRC['twtwater']} suggests about an inch of water a week in summer, half an inch in spring and fall, and none in winter, split across your two allowed days.</p>
<p>Other cities move in and out of stages. In August 2026, {SRC['tomball']} that Tomball entered Stage 2, limiting automatic irrigation to 7 p.m. to 5 a.m. on two designated days by address. The same month, {SRC['katy']}, asking residents to water only overnight hours. As of this writing, {SRC['hpwrest']} shows Stage One was rescinded effective May 29, 2024, with no active stage listed. All of that can change in a dry week, so link to the official page rather than copying the rules word for word and forgetting to update them.</p>
<!--fig:map-->
<p>What we’d build: a short “watering schedule” page for each city or MUD you serve, with the current rule, a link to the source, and a line about how to program a controller to match it. Add a “Reprogram my controller” booking button. When a stage changes, update the page, post it to your Google Business Profile and send it to your customer list the same day. Nextdoor posts in the affected neighborhoods do well here because neighbors are already arguing about it.</p>
<p>Keep the tone helpful. Nobody books the company that scolds them about water waste.</p>"""),

            ("Drought summers, wet springs and when to spend", f"""<p>Houston irrigation demand swings harder than most home services. Summer 2023 was the warmest on record for Houston, the city hit 109°F twice in August, and it went almost 50 days without measurable rain from early July into August, per {SRC['heat23']}. Sprinkler companies couldn’t answer the phone fast enough. Then a wet spring arrives and nobody thinks about their sprinklers for six weeks.</p>
<!--fig:season-->
<p>A rough seasonal plan for the north Houston area, which you should adjust once you have your own call data:</p>
<ul>
<li><b>February and March.</b> Spring startup and system checks. Push maintenance plan sign-ups to past customers, and quote installs for homeowners who want them in before summer.</li>
<li><b>April through June.</b> Repair search volume climbs with the heat. Raise search budgets, and keep the controller and smart upgrade offers running.</li>
<li><b>July through September.</b> Peak repair season. Your problem becomes capacity, not demand. Tighten your service radius in Google Ads so techs aren’t driving from Montgomery to Pearland for a single head replacement.</li>
<li><b>October and November.</b> Fall audits, drainage work and commercial contract renewals.</li>
<li><b>December and January.</b> Freeze prep and backflow insulation. Hard freezes in Houston are rare enough that people forget, and frequent enough that every few years they crack assemblies across the region. Have a freeze-repair page ready to switch on.</li>
</ul>
<p>Rainy stretches are when you should be selling maintenance plans and rain sensors to the people who called you in August. They remember the bill.</p>"""),

            ("Smart controllers, utility discounts and the tax holiday", f"""<p>Smart controllers are a good upsell because they sell on the customer’s own complaint. “My water bill is crazy” is the opening line of half your summer calls.</p>
<p>Some Houston-area programs help. {SRC['hpwsmart']} offers residential customers who get their water bill from the city a discount on Rachio controllers: in 2026, the 8-zone model was $169.99 against a regular $199.99, with lower pricing during promotional weeks (May 4 to 11 and June 8 to 15). The program is built around DIY installation, which is exactly why there’s a market for “we’ll install and program the one you bought.”</p>
<p>The state chips in once a year. The {SRC['taxhol']} set the 2026 water-efficient products sales tax holiday for May 23 to 25, covering WaterSense-labeled landscape irrigation controls, plus residential soaker and drip hoses, moisture controls for sprinkler systems, mulch and plants. Whether your installation labor qualifies is a question for your accountant, so we wouldn’t advertise “tax free installs.”</p>
<!--fig:rebate-->
<p>Utility programs change every year, and many MUDs and suburban utilities in Montgomery and Harris County don’t have one at all. Before you put any discount in an ad, confirm it’s current and that it applies where the customer lives. Then make it the headline, not a footnote.</p>"""),

            ("Google Business Profile, Google Ads and Local Services Ads for sprinkler repair", f"""<p>Start with the Business Profile, because most repair calls come through Maps. Pick the primary category that matches sprinkler work as closely as possible (type “sprinkler” or “irrigation” into the category field and choose the nearest real match), and add landscaping or drainage categories only if you actually do that work. Fill the services list with plain entries like “sprinkler head replacement,” “zone valve repair,” “backflow testing,” “controller installation” and “leak detection.” Put the LI number in the description. If you work from home and don’t serve customers there, hide the address and set a service area. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest.</p>
<p>For Google Ads, split campaigns by job type so you can control the budget for each. Repair and backflow campaigns should be call-focused with ad scheduling that matches when someone answers. Installs can lean on forms and a quote page.</p>
<p>Sample repair ad, for illustration:</p>
<ul>
<li>Headline 1: Sprinkler Repair in The Woodlands</li>
<li>Headline 2: TCEQ Licensed Irrigator</li>
<li>Headline 3: Same-Week Repairs, Upfront Pricing</li>
<li>Description: Broken heads, leaking valves, dead zones. Licensed LI on every job. Call now or book online.</li>
</ul>
<p>The negatives matter as much as the keywords. Start with: how to, diy, yourself, youtube, manual, parts, Home Depot, Lowe’s, Rain Bird or Hunter part numbers, wiring diagram, jobs, hiring, salary, license class, test prep and “free” (unless you do free estimates). Read the search terms report weekly for the first month. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} will help you set a starting budget.</p>
<p>Local Services Ads are less clear-cut. {SRC['lsa']} has no standalone irrigation or sprinkler category. It does list lawn care services and landscaping services, and some irrigation companies run under those with matching job types. Start the sign-up with your address to see what’s offered. If the job types don’t match sprinkler repair, skip it and put the money into search. We compare the two in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</p>"""),

            ("Builder, landscaper and pool builder partnerships", f"""<p>The installs you want most rarely come from a Google search. They come from a superintendent who trusts you to show up before the sod goes down.</p>
<p>Builders have their own reasons to care about licensing. {SRC['gi632c']} tells them to check the irrigator’s name, license number and contact details on bids and invoices, look for the license number on the truck, confirm local permits on new installs, and hand the design, maintenance checklist and warranties to the homeowner at closing. It also warns that unlicensed irrigators often lack insurance, which leaves the builder exposed. That’s your pitch, written by the regulator.</p>
<p>So make it easy. A one-page builder sheet with your LI number, insurance certificate, typical lead time per lot, how you handle punch-list calls and warranty visits, and a sample closing packet. Builders in Conroe, Magnolia, Montgomery and the Grand Parkway corridor are adding lots fast; our {L('/blog/home-builder-marketing-houston-montgomery-county/', 'home builder marketing post')} explains how they think about vendors and timelines.</p>
<p>Landscapers are the other half. Plenty of landscape companies in Spring, Tomball and Cypress don’t hold an irrigator license and can’t legally do the work. Under {SRC['tac71']}, a pass-through contract that includes irrigation has to name the licensed irrigator doing it, with license number and a way to reach them for warranty work. Offer those landscapers a clean subcontract arrangement and a referral fee policy in writing, and they’ll send you every bed renovation that needs drip.</p>
<p>Pool builders and outdoor living contractors tear up irrigation on every backyard job. A short list of them who know your number is worth more than another month of install ads.</p>"""),

            ("Maintenance plans: one repair becomes a yearly account", f"""<p>The repair call is the cheapest customer you’ll ever acquire, because they found you. What you do in the next 30 days decides whether they’re worth $150 or $1,500 over five years.</p>
<!--fig:plan-->
<p>A simple residential plan might include a spring startup and full-zone inspection, a midsummer audit and controller adjustment, a fall check, freeze prep in December, and the annual backflow test where it’s required. Price it at [your price] a year or monthly, include a discount on repairs, and give plan members priority scheduling in July. That last perk sells the plan better than any discount, because everyone has waited a week for a sprinkler tech in August.</p>
<p>How to sell it without a sales script:</p>
<ol>
<li>The tech shows the customer one or two photos on the invoice: a misaligned head watering the street, a zone running 40 minutes in a shaded bed.</li>
<li>The invoice includes a one-line plan offer with a link.</li>
<li>A text two days later asks how the yard looks, links the plan, and asks for a review.</li>
<li>A follow-up email before the next season reminds them of the startup visit.</li>
</ol>
<p>On reviews, follow Google’s rules: ask every customer the same way, never offer discounts for reviews, and never filter out unhappy customers before sending the link. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has templates, and {L('/blog/sms-marketing-small-business-texas-rules/', 'our post on Texas texting rules')} covers what consent you need before you send marketing texts.</p>"""),

            ("What to track and a first 90 days", f"""<p>Track calls by job type. Total calls hide too much. A month with 120 calls that were mostly head replacements 40 minutes away is worse than 70 calls that turned into nine maintenance plans and two installs.</p>
<p>The short list: booked jobs by source, revenue by job type, maintenance plan sign-ups and renewals, backflow tests due versus completed, and builder or landscaper referrals by partner. Recorded calls and form tracking make this possible; our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} walks through the setup.</p>
<p>A first 90 days we’d run for a sprinkler company in The Woodlands, Spring or north Houston:</p>
<ul>
<li><b>Days 1 to 30.</b> Put the LI number everywhere it’s required. Fix the Business Profile categories and services. Build repair, backflow and controller landing pages. Launch call-focused repair search ads with a full negative list.</li>
<li><b>Days 31 to 60.</b> Load every past backflow test into a reminder sequence. Publish watering schedule pages for your top three areas. Launch the maintenance plan offer to past customers.</li>
<li><b>Days 61 to 90.</b> Build the builder and landscaper one-pager and visit ten of each. Review search terms and cut the waste. Decide whether LSA job types fit your work.</li>
</ul>
<p>If you’d like a senior strategist to build that plan around your crews, service area and season, <a href="/contact/">get in touch</a> and tell us where your calls come from now. For the lawn side of the business, our {L('/blog/how-to-get-more-lawn-care-customers-the-woodlands/', 'lawn care marketing post')} is a good companion read.</p>"""),
        ],
        "faq": [
            ("Do irrigation ads in Texas have to show a license number?",
             "Yes. Under 30 TAC 344.70, every advertisement for irrigation services in any medium must include the irrigator's license number, and vehicles used for irrigation work must show it with the LI prefix in letters at least two inches high on both sides. Bids, invoices and contracts must also show the license number and the TCEQ notice statement. That rule covers websites, social media ads and yard signs too."),
            ("How often is backflow testing required in Houston?",
             "In the City of Houston, testable backflow assemblies must be tested at least once a year and again when installed, repaired or relocated. Testers must hold a TCEQ tester license and be on the city's approved testing company list, and results are uploaded through SwiftComply. Many MUDs and suburban utilities near Houston and The Woodlands run their own programs, so check each utility's rules."),
            ("What is the watering schedule in The Woodlands?",
             "The Woodlands Water Agency runs a defined irrigation schedule by address across the 10 MUDs it manages. Odd-numbered addresses water overnight starting Tuesday and Saturday evenings, and even-numbered addresses starting Wednesday and Saturday evenings. Drip irrigation and hand watering are allowed any time. Rules can change during drought, so check the Woodlands Water website for the current schedule before programming a controller."),
            ("Can a sprinkler company use Google Local Services Ads?",
             "Google's Local Services Ads list has no standalone irrigation or sprinkler category. It does include lawn care services and landscaping services, and some irrigation companies run under those with matching job types. Start the sign-up with your business address to see what is offered in your part of Houston. If the job types don't fit sprinkler repair, regular search ads are usually the better choice."),
            ("How do irrigation companies get more customers in Houston?",
             "Win repair calls through Google Maps and call-focused search ads with strong negative keywords. Then turn each repair into a maintenance plan and an annual backflow reminder. Publish helpful pages on local watering schedules, show your TCEQ license number everywhere, and build referral relationships with home builders, landscapers and pool builders, who send most of the installs worth having."),
        ],
        "figures": {
            "license": {
                "type": "checklist",
                "title": "Where your TCEQ license number has to show up",
                "sub": "Based on 30 TAC 344.70 and 344.71",
                "items": ["Every ad, in any medium", "Both sides of work vehicles, LI prefix, 2-inch letters", "Trailers that advertise irrigation", "Bids, proposals and estimates", "Invoices for installs and repairs", "Installation contracts, with seal and warranty dates", "TCEQ notice statement on paperwork", "Pass-through contracts naming the irrigator"],
                "alt": "Checklist of where a TCEQ irrigator license number must appear for sprinkler companies in Houston and The Woodlands",
                "caption": f"From {SRC['tac70']} and {SRC['tac71']}. We add it to the Business Profile and website too.",
            },
            "backflow": {
                "type": "steps",
                "title": "A backflow reminder program",
                "sub": "Turn every test into next year’s booked visit",
                "steps": [["Log the test", "Record the due date in your field software."], ["45 days out", "Reminder text with a booking link."], ["21 days out", "Second text, offer test plus system check."], ["7 days out", "Phone call from the office."], ["After the test", "Confirm the report was uploaded, ask for a review."]],
                "alt": "Steps for a backflow testing reminder program for irrigation companies in Houston and The Woodlands",
                "caption": "The utility creates the deadline. Your job is to be the name they already have.",
            },
            "map": {
                "type": "map",
                "title": "Watering rules differ across the area",
                "sub": "Cities and utilities mentioned in this post",
                "highlight": ["The Woodlands", "Houston", "Tomball", "Katy", "Spring", "Conroe"],
                "alt": "Map of Houston, The Woodlands, Tomball and Katy where sprinkler watering rules differ for irrigation companies",
                "caption": "Build one schedule page per city or MUD you serve, and link the official source.",
            },
            "season": {
                "type": "columns",
                "title": "Sprinkler repair demand by month",
                "sub": "Relative call volume for a north Houston company",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [20, 30, 45, 60, 75, 90, 100, 100, 80, 55, 35, 25],
                "highlight": [6, 7],
                "y_label": "Relative calls",
                "note": "Illustrative example",
                "alt": "Column chart of seasonal sprinkler repair demand for irrigation companies in Houston and The Woodlands",
                "caption": "Use your own call data once you have a year of it. Dry springs shift the curve earlier.",
            },
            "rebate": {
                "type": "stats",
                "title": "Smart controller incentives in 2026",
                "stats": [["$30", "off an 8-zone Rachio for Houston water customers"], ["$50", "off during 2026 promo weeks"], ["May 23", "start of the 3-day Texas tax holiday"], ["$0", "sales tax on WaterSense irrigation controls that weekend"]],
                "note": "Source: Houston Public Works, Texas Comptroller",
                "alt": "Stats on smart irrigation controller discounts and the Texas tax holiday for sprinkler companies in Houston",
                "caption": f"From {SRC['hpwsmart']} and the {SRC['taxhol']}. Confirm each program is current before advertising it.",
            },
            "plan": {
                "type": "funnel",
                "title": "From one repair call to a yearly account",
                "stages": [["Repair call", "100"], ["Photo report on invoice", "100"], ["Plan offer opened", "45"], ["Plan sign-up", "15"], ["Renewed next year", "11"]],
                "note": "Illustrative example",
                "alt": "Funnel showing sprinkler repair customers becoming maintenance plan members for an irrigation company in The Woodlands",
                "caption": "Even modest conversion here beats paying for the same customer again next summer.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: pool service
    {
        "slug": "pool-cleaning-service-marketing-houston-the-woodlands",
        "title": "Pool Cleaning and Service Company Marketing in Houston and The Woodlands",
        "seo_title": "Pool Service Marketing in Houston & The Woodlands",
        "desc": "Pool cleaning and service marketing for Houston and The Woodlands: route density, green-pool offers, storm cleanups, Google Ads, LSA, Nextdoor and reviews.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Nextdoor", "Google Business Profile"],
        "art": "b4",
        "hero": "pool",
        "hero_alt": "Illustration of a backyard pool for pool cleaning and service company marketing in Houston and The Woodlands",
        "related": ["pool-builder-marketing-houston-the-woodlands", "is-nextdoor-advertising-worth-it", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Thursday, late May, 2:15 p.m. Your tech is at stop 11 of 16. The next pool is 38 minutes away in Magnolia because a customer signed up from a Facebook ad last month, and the one after that is back in Spring. Meanwhile the office has three voicemails from new homeowners in Cypress with green pools, and a weekly customer in Sterling Ridge just canceled because they’re moving.</p>
<p>That afternoon is the whole business. Pool service runs on routes, and the marketing that matters most decides where your next customer lives.</p>
<p>Pool cleaning and service marketing in Houston and The Woodlands works when it fills the streets your trucks already drive, uses one-time jobs like green-pool cleanups to start weekly accounts, and keeps those accounts long enough to pay back what you spent to get them. Equipment repair is where the margin lives. Reviews and neighbors do more selling than ads.</p>
<p>Below is how we’d set that up for a service company working anywhere from Kingwood to Katy.</p>"""),

            ("Route density is the marketing strategy", f"""<p>Every pool service owner knows drive time eats profit. Fewer of them run their marketing like they know it.</p>
<p>{SRC['skroutes']} puts density near the top of what makes a route valuable: pools close together with close service days cut travel time between stops. A customer three streets from your Tuesday cluster is worth more than the same customer 20 minutes off-route, even at the same monthly price. So stop targeting “Houston” in your ads.</p>
<!--fig:density-->
<p>What that looks like in practice:</p>
<ul>
<li>Map your current customers by service day (see the example map below). Most routes have three to six clusters, often a subdivision or a few adjacent ones, like Creekside Park, a couple of Cypress neighborhoods off Fry Road, or a pocket of Kingwood.</li>
<li>Draw ad targeting as radius circles around those clusters, a mile or two each, instead of one big circle around your shop.</li>
<li>Set a “route-fill” offer only for those circles, such as a first month at [your price] for homes in neighborhoods you already service.</li>
<li>Quote off-route customers honestly, with a higher price or a waitlist. Some will still say yes, and those are profitable.</li>
</ul>
<!--fig:map-->
<p>Door hangers still work for this, oddly well. When a tech finishes a pool, a few hangers on neighboring doors saying “we service a pool on your street every Tuesday” costs almost nothing and targets exactly the right houses.</p>"""),

            ("The recurring revenue math behind every ad decision", f"""<p>A weekly customer isn’t a $160 sale. It’s a monthly payment that might last four or five years, plus repairs. Until you know that number, you can’t judge any ad.</p>
<p>The industry is in a confident mood. {SRC['sk2026']}, based on more than 1,600 pool pros, found more than 80% expect higher revenue in 2026, monthly billing remains the most common pricing model, and most companies plan increases under 10%. Your own numbers matter more than anyone’s survey, though.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line</th><th>Illustrative value</th><th>Where to find yours</th></tr></thead>
<tbody>
<tr><td>Monthly service price</td><td>$160</td><td>Average across your weekly accounts</td></tr>
<tr><td>Gross margin on service</td><td>45%</td><td>Price minus chemicals, labor and drive time</td></tr>
<tr><td>Average customer life</td><td>36 months</td><td>Start and cancel dates in your software</td></tr>
<tr><td>Repair and equipment margin per year</td><td>$300</td><td>Repair invoices per customer per year</td></tr>
<tr><td>Lifetime gross profit</td><td>About $3,500</td><td>($160 x 45% x 36) + 3 years of repair margin</td></tr>
<tr><td>Comfortable cost to acquire</td><td>$350 to $700</td><td>10% to 20% of lifetime gross profit</td></tr>
</tbody></table></div>
<p>Every value in that table is an illustrative example. The method is the point. If your lifetime gross profit per weekly account is around $3,500, paying $400 in ads and a cleanup discount to land one isn’t expensive. Most owners we talk to are spending far too little to get new accounts and far too much time chasing one-off jobs that never convert.</p>
<!--fig:value-->
<p>Cancellations are the other half. The main reasons we hear are moving, price, and “the tech stopped showing up on the same day.” You can’t fix moving, but you can ask the departing customer to introduce you to the buyer. That’s a weekly account that literally comes with the house.</p>"""),

            ("Green-pool cleanups, startups and other front-door offers", f"""<p>Nobody searches for “weekly pool service” with urgency. They search for it when something has gone wrong: a green pool, a new house, a bad experience with the last company.</p>
<p>Green-pool cleanups are the best front door in the business. The customer is motivated, the before and after photos sell themselves, and once the pool is clear the obvious next question is “who’s going to keep it this way?” Build a dedicated landing page for green-pool recovery with honest pricing ranges (“most cleanups run [your price] to [your price] depending on size and condition”), a short gallery, and a clear offer to credit part of the cleanup if they start weekly service within 30 days.</p>
<p>Other front doors worth a page and an ad group:</p>
<ul>
<li><b>New homeowners.</b> Houston relocations often land in houses with a pool the buyer has never maintained. A “new to pool ownership” visit that walks them through the equipment builds trust fast.</li>
<li><b>Foreclosures, rentals and listings.</b> Agents and investors need pools cleaned before photos or showings, often in a hurry.</li>
<li><b>Spring startup.</b> Many Houston pools run year-round, but plenty of owners let them slide over winter, and March through May brings a wave of “get it ready” calls.</li>
<li><b>Switchers.</b> “Unhappy with your pool service?” is blunt and works, as long as you can actually promise the same day and the same tech each week.</li>
</ul>
<p>Every cleanup or startup job should end with a written weekly-service offer and a text the next day. That handoff is where most companies lose the account.</p>"""),

            ("Houston’s pool calendar: freeze nights, hurricane season and cleanups", f"""<p>Houston pools don’t close for winter the way northern pools do, so “opening season” is softer here. What we get instead are weather spikes.</p>
<p>Freeze nights come first. When forecasters call for a hard freeze, customers want to know whether to run the pump, cover the equipment or call you. A short freeze guide on your site, emailed and posted to your Business Profile the day a freeze watch is issued, earns trust and fills the week after with repair calls for cracked equipment. Anyone who lived through February 2021 reads that email.</p>
<p>Hurricane season runs June 1 to November 30. When Beryl came ashore on July 8, 2024, CenterPoint was working on 2.26 million power outages, according to {SRC['beryl']}. Pumps sit off when the power is out, storms fill pools with leaves and limbs, and a Houston pool in July doesn’t stay clear for long without circulation. Storm cleanups are a real business line for a few weeks, and they’re a recruiting event for weekly accounts if you handle them well.</p>
<!--fig:storm-->
<p>Weekly customers come first after a storm, and saying so in advance is good marketing. A line on your service page like “weekly customers get priority after storms” sells the plan to people who remember Beryl.</p>"""),

            ("Licensing: what Texas requires, and what to say in your ads", f"""<p>Texas has no statewide license for pool cleaning or maintenance, and none for pool construction either, as {SRC['pooldial']} lays out. Anyone can start a route. That’s why so many homeowners have a story about a pool guy who disappeared.</p>
<p>Equipment work is a different matter. {SRC['tdlrpool']} says that if a pool system needs a new or upgraded line circuit, only a licensed electrical contractor with a designated master electrician can do that work. Holders of a residential appliance installer license can install and replace devices such as pumps, motors, heaters, lights, GFCIs and automation on the load side of the control center, and add devices like salt systems or variable-speed motors that don’t increase amperage or need the main panel. The same guidance says maintenance and repair by an authorized party uses components of the same type and ampacity as the originals. It’s dated 2019, so check with TDLR before you build a pitch around it. Gas lines and plumbing connections bring in other licenses, and commercial and HOA pools fall under public pool rules and local health departments.</p>
<!--fig:license-->
<p>For marketing, the rule is simple: say exactly what you hold. “Insured, with a TDLR-licensed residential appliance installer on staff for equipment work” is specific, checkable and better than a vague “licensed and insured.” If you don’t do electrical work, say who you bring in. Homeowners who’ve been burned before will notice the honesty.</p>"""),

            ("Equipment repair upsells without being the pushy pool guy", f"""<p>The weekly visit pays the bills. Equipment is where a good year comes from: pumps, filters, salt cells, heaters, automation and the occasional leak hunt.</p>
<p>The trick is to make the upsell feel like information. Most service software sends a visit report with chemistry readings and a photo. Use it. A photo of a cracked pump lid or a salt cell scaled over, with a one-line note and a link to a quote, does the selling for you. Customers trust the tech they see every week. They don’t trust a cold call about a variable-speed pump.</p>
<!--fig:upsell-->
<p>Two cautions. Don’t make every report a sales pitch, or customers learn to ignore them. And price repairs clearly before the work, because a surprise equipment bill is the most common reason we see behind a one-star pool review in Houston.</p>"""),

            ("Google Business Profile, Local Services Ads and Google Ads for pool service", f"""<p>For a route business, Google Maps visibility matters mostly in your clusters. Set your service area to the cities and ZIP codes you actually want, hide your home address if you don’t serve customers there, add photos of real trucks and real pools, and list services one by one: weekly pool cleaning, green pool cleanup, filter cleaning, salt cell cleaning, pool equipment repair, pump replacement.</p>
<p>{SRC['lsa']} includes both “Pool cleaner” and “Pool contractor,” so service companies can run Local Services Ads in the right category. You pay per lead rather than per click, and you can dispute leads that weren’t real customers (our {L('/blog/local-services-ads-lead-disputes-credits/', 'post on LSA disputes')} explains how). Set your LSA service area to the same clusters you target elsewhere, because LSA will happily send you a lead in Pearland when your route is in Tomball.</p>
<p>In Google Ads, split campaigns by intent:</p>
<ul>
<li><b>Recurring service:</b> weekly pool service The Woodlands, pool cleaning service near me, pool maintenance Spring TX.</li>
<li><b>Cleanups:</b> green pool cleanup, pool cleaning after storm, algae pool cleaning Houston.</li>
<li><b>Repair:</b> pool pump repair, pool heater repair Katy, salt cell replacement, pool leak detection.</li>
</ul>
<p>Negatives on day one: pool supply, pool store, chlorine price, pool robot, robotic cleaner, Leslie’s, Home Depot, above ground (unless you service them), DIY, how to, YouTube, jobs, hiring, pool cleaner salary, CPO class, and builder terms like “pool installation cost” if you don’t build. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give you a feel for click costs, and {L('/services/search-marketing/', 'our search marketing team')} can run it if you’d rather be on a route.</p>"""),

            ("Nextdoor, neighbors and reviews", f"""<p>Pool service is a neighborhood business, and Nextdoor is where neighborhoods ask for recommendations. “Who do you use for your pool?” threads in The Woodlands and Kingwood can run 60 comments deep. You can’t buy your way into those, but you can earn your way in by doing good work for people who post.</p>
<p>Paid Nextdoor ads are worth testing in route clusters, especially with an offer framed around the street (“two openings on our Thursday route in Alden Bridge”). Our {L('/blog/is-nextdoor-advertising-worth-it/', 'Nextdoor advertising review')} covers what to expect and when to stop.</p>
<p>Reviews do the rest. Ask every weekly customer for a review around their third visit, once they’ve seen consistency, and ask every cleanup customer the day the pool turns blue. {SRC['gpol']} bans offering incentives for reviews, discouraging negative reviews and selectively asking only happy customers, so send the same link to everyone. Reply to every review with specifics. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has request scripts you can copy.</p>
<p>A sample review text, for illustration: “Hi Dana, it’s Marcus with [company]. Your pool’s been on our Tuesday route a month now. If you have a minute, a Google review helps us a lot: [link]. Thanks for having us.”</p>"""),

            ("Buying routes vs. building them", f"""<p>Sometimes the fastest way to add density is to buy it. Routes trade on what {SRC['skroutes']} describes as a sliding scale based on a multiple of monthly service revenue, with denser, cleaner routes commanding a higher multiple.</p>
<p>From a marketing view, a purchased route is a retention problem on day one. Customers didn’t choose you. A good transition looks like this: the seller introduces you by letter or email before the switch, your tech is on the same day of the week, the first three visit reports are extra thorough with photos, and you ask nobody for anything in the first month. After that, the normal review and repair flow kicks in.</p>
<p>When you compare buying with building, use the lifetime value table above. If building a weekly account through ads and cleanups costs you $400 and buying one costs more than that once you account for the customers who leave after the sale, build. If the route fills a hole in your existing clusters, the math often flips.</p>"""),

            ("Pool builders, realtors and the referral network", f"""<p>New pools need someone to take over after startup, and many builders don’t want the service calls. A relationship with two or three pool builders in your area can be worth a steady stream of new weekly accounts each spring. Our {L('/blog/pool-builder-marketing-houston-the-woodlands/', 'pool builder marketing post')} covers how builders market themselves; from your side, the pitch is a clean handoff, a startup visit and no stealing their remodel work.</p>
<p>Realtors are the other referral source. A one-page “pool inspection before listing” offer for agents in The Woodlands, Spring and Cypress turns into service accounts with the buyers. Home inspectors often recommend a pool specialist too, so introduce yourself to the ones who work your area.</p>"""),

            ("What to track, and a first 90 days", f"""<p>Track three numbers above everything else: new weekly accounts by source, cancellations by reason, and average drive minutes between stops. If marketing adds accounts and drive time goes up, you’re growing the wrong way.</p>
<ul>
<li><b>Days 1 to 30.</b> Map customers by service day. Rebuild Google Ads and LSA targeting around those clusters. Build pages for weekly service, green-pool cleanup and equipment repair.</li>
<li><b>Days 31 to 60.</b> Start the review request flow. Launch a door hanger routine for techs. Test a Nextdoor route-fill offer in your densest cluster.</li>
<li><b>Days 61 to 90.</b> Write a storm and freeze page and keep it ready. Visit two pool builders and five realtors. Review cancellations and fix the top reason.</li>
</ul>
<p>Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} is worth reading before you scale ads, because green-pool callers call the next company if you don’t answer. If you want a senior strategist to build a plan around your routes, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Do you need a license to clean pools in Texas?",
             "Texas has no statewide license for pool cleaning or maintenance, so anyone can start a route. Equipment work is different. TDLR guidance says new or upgraded electrical circuits need a licensed electrical contractor, and residential appliance installer license holders can replace pool devices like pumps and heaters within limits. Commercial and HOA pools also fall under public pool rules and local health departments."),
            ("How do pool service companies get more customers in Houston and The Woodlands?",
             "Fill the neighborhoods your routes already cover. Target ads around existing service clusters, use green-pool cleanups and startups as front-door offers that convert into weekly service, ask every customer for a Google review, and build referrals with pool builders and realtors. Nextdoor and door hangers near current stops are cheap ways to add density without adding drive time."),
            ("Is there a Google Local Services Ads category for pool cleaning?",
             "Yes. Google's Local Services Ads category list includes Pool cleaner and Pool contractor. You pay per lead instead of per click and can dispute leads that weren't real customers. Set the service area to match your route clusters in Houston, The Woodlands and nearby suburbs, because LSA can send leads anywhere in a broad area if you let it."),
            ("How much should I spend to get a new weekly pool customer?",
             "Work it out from lifetime value. Multiply your monthly price by your service margin and average months a customer stays, then add repair margin. If that comes to a few thousand dollars, spending a few hundred to land a weekly account is reasonable. Track cost per new weekly account by source rather than cost per lead, since many cleanup leads never convert."),
            ("Should pool companies market storm cleanups after hurricanes?",
             "Yes, carefully. After a storm like Beryl, many Houston pools sat without power for days and filled with debris. Have a storm cleanup page ready before hurricane season, serve weekly customers first, and post updates on your Business Profile and social pages. Price cleanups clearly and offer a credit toward weekly service, since storm customers can become long-term accounts."),
        ],
        "figures": {
            "density": {
                "type": "bars",
                "title": "Same route, different density",
                "sub": "Stops per day a tech can finish",
                "items": [["Tight clusters (avg 4 min between stops)", 18, "18"], ["Mixed clusters (avg 10 min)", 14, "14"], ["Scattered (avg 20 min)", 10, "10"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart showing how route density changes daily pool stops for pool service companies in Houston and The Woodlands",
                "caption": "Ads targeted around existing clusters add stops without adding drive time.",
            },
            "value": {
                "type": "stats",
                "title": "What the industry expects in 2026",
                "stats": [["1,600+", "pool pros surveyed"], ["80%+", "expect higher revenue in 2026"], ["<10%", "planned price increase for most"], ["Monthly", "most common billing model"]],
                "note": "Source: Skimmer 2026 State of Pool Service",
                "alt": "Stats from the 2026 State of Pool Service report relevant to pool cleaning companies in Houston and The Woodlands",
                "caption": f"From {SRC['sk2026']}.",
            },
            "storm": {
                "type": "steps",
                "title": "A storm cleanup playbook",
                "sub": "Set this up before June 1",
                "steps": [["Before the season", "Storm cleanup page and ad group built, paused."], ["Storm watch", "Email and post: prep tips, what to do with the pump."], ["First 48 hours", "Check weekly customers first, photo report each."], ["Week one", "Switch on cleanup ads in your clusters."], ["After", "Offer storm customers a weekly-service credit."]],
                "alt": "Steps for a hurricane storm cleanup marketing plan for pool service companies in Houston",
                "caption": "Weekly customers first, then new ones. Saying that out loud sells the weekly plan.",
            },
            "license": {
                "type": "compare",
                "title": "Pool work and Texas licensing",
                "left": {"title": "No state license required", "items": ["Weekly cleaning and chemistry", "Brushing, vacuuming, skimming", "Filter cleaning", "Green-pool cleanups", "Water testing reports"]},
                "right": {"title": "Check licensing first", "items": ["New or upgraded circuits (electrical contractor)", "Pump, heater, light replacement (RAIL or electrician)", "Gas heater connections", "Plumbing and potable water connections", "Commercial and HOA pool operation"]},
                "alt": "Comparison of pool service tasks that need a Texas license and those that don't, for pool companies in Houston",
                "caption": f"Based on {SRC['tdlrpool']} and {SRC['pooldial']}. Confirm with TDLR before advertising equipment work.",
            },
            "upsell": {
                "type": "checklist",
                "title": "Visit report items that lead to repairs",
                "sub": "Show a photo and a one-line note",
                "items": ["Cracked or leaking pump lid", "Filter pressure higher than normal", "Scaled or worn salt cell", "Heater not firing", "Automation panel errors", "Loose or damaged light niche", "Visible leak at equipment pad", "Skimmer or return damage"],
                "alt": "Checklist of pool equipment issues to include in visit reports for pool service companies in The Woodlands and Houston",
                "caption": "Inform first. The quote link does the selling.",
            },
            "map": {
                "type": "map",
                "title": "Build routes in clusters",
                "sub": "Example service clusters for a north Houston company",
                "highlight": ["The Woodlands", "Spring", "Kingwood", "Cypress", "Tomball", "Magnolia"],
                "note": "Illustrative example",
                "alt": "Map of example pool service route clusters around The Woodlands, Spring, Kingwood and Cypress in Houston",
                "caption": "Target ads around clusters you already drive, not a radius around the shop.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: appliance repair
    {
        "slug": "appliance-repair-marketing-houston",
        "title": "Appliance Repair Marketing in Houston: Win the Call Before the Fake Listings Do",
        "seo_title": "Appliance Repair Marketing in Houston: Win More Calls",
        "desc": "Appliance repair marketing for Houston: fake listings, Local Services Ads, brand and problem keywords, trademark rules, reviews and landlord accounts.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google", "Google Business Profile"],
        "art": "b6",
        "hero": "tools",
        "hero_alt": "Illustration of repair tools for appliance repair marketing in Houston, Kingwood and The Woodlands",
        "related": ["google-business-listing-scam-calls", "local-services-ads-vs-google-ads-home-services", "property-management-company-marketing-houston"],
        "sections": [
            (None, f"""<p>Saturday, 2 p.m., the second week of August. A family in Kingwood opens the fridge and it’s 52 degrees inside. Someone searches “refrigerator repair near me” and calls the first listing with decent stars. It says “Kingwood Appliance Repair.” It’s a call center two states away that sells the job to whichever tech it can reach, and the family pays a $129 “service fee” before anyone looks at the compressor.</p>
<p>You were 11 minutes away with an open slot. You never got the call.</p>
<p>Appliance repair marketing in Houston comes down to being the real, visible, answerable company in a category crowded with fakes and lead brokers. That means a Google Business Profile that proves you exist, Local Services Ads where you can get them, and search ads built on brand plus problem keywords that stay inside Google’s trademark rules. Clear diagnostic fees and honest parts timelines do the rest, along with a book of landlords and property managers who call you before anyone else.</p>
<p>Below is how we’d set it up for an independent or brand-authorized shop anywhere from Sugar Land to Conroe.</p>"""),

            ("Brand-authorized or independent: pick the story you tell", f"""<p>The first marketing decision is what you are. Both models work in Houston, and they sell differently.</p>
<!--fig:model-->
<p>Brand-authorized shops get warranty dispatches and a credibility line they can use (“factory-authorized for [brand]”), but warranty work tends to pay less per job and comes with paperwork and parts rules set by the manufacturer. Independents can service everything, set their own prices and market harder on speed, but they have to earn trust without a logo.</p>
<p>Whatever you are, say it precisely. If you’re authorized for two brands, name those two and nothing more. “Factory trained” and “authorized” mean specific things to customers, and stretching them invites complaints, chargebacks and, if a manufacturer notices, a letter from their lawyers. Independents do better with “we repair all major brands, including [list],” which is true and descriptive.</p>
<p>A lot of Houston shops do both: warranty work for one or two brands to keep techs busy midweek, and direct work at full price for everything else. That’s fine. Just track the two separately so you know which one actually pays.</p>"""),

            ("Warranty and home-warranty work: volume, not a marketing plan", f"""<p>Manufacturer warranty jobs and home-warranty company dispatches can fill a schedule. In the accounts we’ve seen across home services, they rarely build a business by themselves, because the customer belongs to the warranty company and the rate is set for you.</p>
<p>Use that volume deliberately:</p>
<ul>
<li>Every warranty customer is a real person in a real Houston neighborhood who can leave a real review. Ask them the same way you ask direct customers.</li>
<li>Leave a magnet or a sticker with your direct number on every appliance you touch. The next repair, out of warranty, is often a direct call.</li>
<li>Use warranty jobs to fill gaps in routes near your direct customers, not to send a tech from Pearland to Tomball for a flat fee.</li>
</ul>
<p>If more than half your revenue comes through warranty companies, the most valuable marketing you can do is anything that shifts that mix toward direct calls. That’s the rest of this post.</p>"""),

            ("The fake-listing problem, and how real shops fight it", f"""<p>Appliance repair sits in the same corner of Google Maps as locksmiths and garage doors: urgent jobs, unfamiliar companies, lots of money in the call. That attracts fakes.</p>
<p>A {SRC['cbc']} found that in some areas up to 50% of appliance repair companies returned in a Google Maps search appeared to be fake, with local-sounding names pinned to coffee shops, banks and strip malls, and calls routed to a single call center. In March 2025, Google sued a network behind more than 10,000 illegitimate listings and said scams cluster in “duress verticals,” services people need urgently, according to {SRC['cbs']}. Unlike locksmith and garage door companies, appliance repair isn’t on {SRC['lsrestrict']} that requires advanced verification to run search ads in the U.S., so lead brokers can still buy their way in.</p>
<!--fig:scam-->
<p>You can’t out-fake the fakes, and you shouldn’t try. You win by being obviously real:</p>
<ul>
<li>Follow {SRC['gbpguide']} to the letter. Service-area businesses should hide their address, virtual offices aren’t eligible unless staffed during business hours, and the business name must match the real-world name without extra keywords. “Bayou City Appliance Repair Same Day Fridge Washer Dryer” is a suspension waiting to happen.</li>
<li>Upload photos a fake can’t produce: your techs by name, your trucks with your logo, your parts shelves, real jobs in real Houston kitchens.</li>
<li>Put your owner’s name, your license and certification details, and a physical photo of the team on your website’s About page.</li>
<li>Report fake listings near you with “Suggest an edit” in Google Maps. It’s slow, but it works over time.</li>
</ul>
<p>Our {L('/blog/google-business-listing-scam-calls/', 'post on Google listing scam calls')} covers the scam calls owners get from fake “Google” reps, and {L('/blog/google-business-profile-video-verification/', 'our video verification guide')} explains how to get through Google’s checks without a suspension.</p>"""),

            ("Same-day service, diagnostic fees and parts delays", f"""<p>Callers ask three questions, in this order. Can you come today? What’s it going to cost to look at it? How long will the part take?</p>
<p>Answer all three on your website and on the phone before a competitor does.</p>
<p><b>Same-day.</b> If you can do it, say so with conditions (“same-day when booked by noon, most of Houston and Spring”). If you can’t, say “next-day” and mean it. Customers forgive a later slot if it’s a real one.</p>
<p><b>Diagnostic fee.</b> Publish it. State if the fee is credited toward the repair if they approve the work, and say it in one line on every landing page. The fake listings hide their fees until the tech arrives. Your transparency is the contrast.</p>
<p><b>Parts.</b> This is where reviews go wrong. A control board on back-order for three weeks turns a five-star tech visit into a one-star review if nobody calls the customer. Text a parts update at a set rhythm, even when there’s no news. “Still waiting on the board from the distributor, next update Thursday” prevents more bad reviews than any reputation software.</p>
<!--fig:timeline-->
<p>Train whoever answers the phone to give the fee, the soonest real slot and a plain expectation on parts. Then book the visit before hanging up. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} explains why the first company to answer usually gets the job.</p>"""),

            ("Google Local Services Ads for appliance repair", f"""<p>{SRC['lsa']} includes “Appliance repair services,” so Houston shops can run Local Services Ads in their own category. LSAs sit above regular search ads on many queries, you pay per lead (a call or message) instead of per click, and you can dispute leads that weren’t real customers.</p>
<p>The screening that comes with LSA is the point. Background checks plus license and insurance checks (which vary by category and state) all work against the fake-listing problem, and customers see the result in the ad. Ranking leans heavily on reviews and how fast you answer, so a shop with 200 reviews that picks up in three rings beats a bigger competitor with 40.</p>
<p>Set your LSA service area tighter than you think. A lead in Katy is no good to a shop in Humble on a Saturday. Choose the appliance job types you actually want (refrigerators and washers, maybe not built-in wine coolers), and set hours to match when someone answers. Our {L('/blog/local-services-ads-vs-google-ads-home-services/', 'comparison of LSA and Google Ads')} and {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified explainer')} go deeper.</p>"""),

            ("Google Ads: brand plus problem keywords, and the trademark rules", f"""<p>Appliance searches are unusually specific. People type the brand, the appliance and the symptom, sometimes the error code off the display. That’s a gift: every one of those searches tells you what the job is.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Refrigerator, not cooling</td><td>refrigerator not cooling Houston, Samsung fridge not cold, Whirlpool refrigerator repair</td><td>Highest urgency in summer. Call-focused.</td></tr>
<tr><td>Ice maker</td><td>ice maker not working, LG ice maker repair</td><td>Often bundled with fridge visits.</td></tr>
<tr><td>Washer</td><td>washer won’t drain, washing machine repair Katy, Maytag washer error code</td><td>Steady year-round.</td></tr>
<tr><td>Dryer</td><td>dryer not heating, dryer repair The Woodlands</td><td>Mention vent cleaning only if you do it.</td></tr>
<tr><td>Dishwasher</td><td>dishwasher not draining, Bosch dishwasher repair Sugar Land</td><td>Higher-income areas skew toward premium brands.</td></tr>
<tr><td>Oven and range</td><td>oven not heating, GE range repair, oven repair before Thanksgiving</td><td>Spikes in November and December.</td></tr>
</tbody></table></div>
<p>Now the trademark question. Under {SRC['tm']}, using brand names as keywords isn’t restricted. Ad text is different: if a trademark owner files a complaint, ads using that term in the headline or description can be restricted. The policy carves out resellers and informational sites, and the reseller exception explicitly covers “components, replacement parts, or compatible products or services corresponding to the trademark,” with the landing page making the relationship clear. The policy text doesn’t mention repair services by name, which is why repair ads with brand names sometimes get limited.</p>
<p>What we do in practice: brand names in keywords freely, brand names in ad text only when it’s descriptive and accurate (“We Repair Samsung Refrigerators”), never “Samsung Service” or “Official” anything, and a landing page that says plainly you’re independent (or exactly which brands you’re authorized for). If an ad gets limited, try the generic version of the headline and keep the brand in the keyword and on the page.</p>
<!--fig:negatives-->
<p>Error code pages are excellent SEO for appliance shops, by the way. A page that explains what “OE on an LG washer” means, what the owner can safely check, and when to call you ranks well and brings in exactly the right customer. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} help with budgeting, and {L('/services/search-marketing/', 'our search marketing team')} can build the account.</p>"""),

            ("Houston heat turns a dead fridge into an emergency", f"""<p>Appliance repair has a weather pattern here like everything else. Summer 2023 was the warmest summer on record for Houston, with the city hitting 109°F twice in August and triple digits on all but three days that month, per {SRC['heat23']}. Refrigerators and freezers in hot garages work hardest in exactly those weeks, and a failed compressor costs a family a week of groceries.</p>
<p>Power events add to it. After Beryl in July 2024, CenterPoint was working through 2.26 million outages, according to {SRC['beryl']}. In our experience across home services, the days after power returns bring a wave of calls about fridges, ice makers and electronics that don’t come back right.</p>
<!--fig:season-->
<p>So shift budget with the season. Raise refrigerator and ice maker bids from May through September and after any big outage. Push oven and range ads in the two weeks before Thanksgiving and before Christmas. Run dryer and washer campaigns steadily, since those don’t care about weather. And keep a short “after the power comes back” page ready for hurricane season.</p>"""),

            ("Certifications and licenses: say what you hold", f"""<p>Two credentials come up most in appliance marketing.</p>
<p>For sealed-system refrigerator and freezer work, the EPA requires technicians who could release refrigerant to be certified, and Type I certification covers servicing small appliances, per {SRC['epa608']}. “EPA 608 certified technicians” is a credibility line worth adding to refrigerator pages, as long as it’s true for the techs doing that work.</p>
<p>On the electrical side, Texas licenses residential appliance installers and installation contractors through TDLR, and {SRC['tdlrex']} notes that residential appliance dealers, manufacturers or their authorized designees performing electrical work while repairing or servicing an existing appliance are exempt from electrician licensing. Where your shop falls depends on how you’re set up, so check with TDLR before you put “licensed” in an ad. Precise beats vague here too.</p>"""),

            ("Landlord and property manager accounts", f"""<p>Houston has a lot of rental homes and apartments, and every one has a fridge, a washer and a dishwasher that will fail at some point. Property managers don’t search Google each time. They call the vendor who made the last job easy.</p>
<!--fig:pm-->
<p>What property managers in Houston, Katy and The Woodlands want from an appliance vendor is boring and specific: a not-to-exceed amount they can approve without a call, photos before and after, an invoice that names the unit and the tenant issue, and a tech who contacts the tenant directly to schedule. Bonus points if you’ll quote “repair vs. replace” with a real number, because many of them would rather replace a 14-year-old washer than pay to fix it twice.</p>
<p>Start with a vendor packet: W-9, certificate of insurance, service area, rates and diagnostic fee, response times, and an onboarding contact. Then email it to the 30 property management companies nearest your shop and follow up by phone. Our {L('/blog/property-management-company-marketing-houston/', 'property management marketing post')} explains how those companies think about vendors from their side.</p>"""),

            ("Reviews that sell the next call", f"""<p>Reviews are the clearest signal that you’re real, and the fakes either have none or a suspicious wall of five-star reviews posted the same week.</p>
<p>Ask every customer, by text, shortly after the repair is done, with the same link for everyone. Google’s policy bans incentives and review gating, and in April 2026 Google added language against telling staff to collect a set number of reviews or reviews with specific content, per {SRC['ppcl']}. So don’t script “please mention the Samsung fridge and Sugar Land.” Customers usually mention the appliance and the speed on their own. Our {L('/blog/fake-reviews-rule-local-businesses/', 'post on the FTC fake reviews rule')} covers what else is off limits.</p>
<p>Reply to every review. On a bad one about parts delays, explain what happened in a sentence and offer to call. The next customer reads that reply and decides if you’re the kind of company that communicates, which is the whole worry with appliance repair.</p>"""),

            ("What to track, and a first 90 days", f"""<p>Track booked jobs by source and by appliance, completed versus canceled, average ticket, and the share of revenue from direct customers versus warranty dispatch. Record calls so you can hear which ones you lost and why. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers setup.</p>
<ul>
<li><b>Days 1 to 30.</b> Clean up the Business Profile (real name, hidden address if you’re a service-area business, real photos). Publish your diagnostic fee and same-day terms. Apply for Local Services Ads.</li>
<li><b>Days 31 to 60.</b> Launch Google Ads with appliance and symptom ad groups and a full negative list. Start the review request flow. Write the first five error code or symptom pages for the brands you see most.</li>
<li><b>Days 61 to 90.</b> Build and send the property manager packet. Set seasonal budget rules for summer and the holidays. Review lost calls and fix the phone script.</li>
</ul>
<p>If you want a senior strategist to build that plan around your techs and service area, <a href="/contact/">get in touch</a> and tell us how many calls you get now and how many you’d like.</p>"""),
        ],
        "faq": [
            ("How do appliance repair companies get more customers in Houston?",
             "Look obviously real on Google. Keep a Business Profile with your real name, real photos and steady reviews, apply for Local Services Ads in the appliance repair category, and run search ads on appliance and symptom keywords with brand names where they're accurate. Publish your diagnostic fee and same-day terms, and build accounts with property managers who send repeat work."),
            ("Can I use brand names like Samsung or Whirlpool in my Google Ads?",
             "Using brand names as keywords isn't restricted under Google's trademark policy. Ad text is different: if a trademark owner has filed a complaint, ads using the term can be limited. The reseller exception covers replacement parts and compatible products or services, so keep usage descriptive, such as We Repair Samsung Refrigerators. Never say official or authorized unless the manufacturer has actually authorized you."),
            ("Is there a Local Services Ads category for appliance repair?",
             "Yes. Google's Local Services Ads list includes Appliance repair services. You pay per lead rather than per click, and businesses go through background, license and insurance screening, which helps separate real Houston shops from lead brokers. Ranking depends heavily on reviews and responsiveness, so answer every lead quickly and keep your service area tight enough to reach customers the same day."),
            ("Why are there so many fake appliance repair listings on Google Maps?",
             "Appliance repair is an urgent, high-value job, so lead brokers create local-sounding listings and route calls to call centers. A CBC investigation found up to half of appliance repair listings in some areas appeared fake, and Google sued a network behind more than 10,000 fake listings in 2025. Report suspect listings with Suggest an edit and make your own profile unmistakably real."),
            ("Should an appliance repair company publish its diagnostic fee?",
             "Yes. Callers want to know what it costs to have someone look at the appliance, and many fake listings hide their fees until the tech arrives. Publish the fee, say whether it is credited toward the repair if the customer approves the work, and have whoever answers the phone say the same thing. Clear fees reduce no-shows and bad reviews in Houston."),
        ],
        "figures": {
            "model": {
                "type": "compare",
                "title": "Authorized vs. independent appliance shops",
                "left": {"title": "Brand-authorized", "items": ["Warranty dispatches fill the schedule", "Lower rates set by the manufacturer", "Parts and paperwork rules", "Can say “authorized for [brand]”", "Customer belongs to the warranty"]},
                "right": {"title": "Independent", "items": ["Services all major brands", "Sets its own prices", "Markets on speed and service", "Says “we repair [brands]”, never “official”", "Customer belongs to you"]},
                "alt": "Comparison of brand-authorized and independent appliance repair businesses for appliance repair marketing in Houston",
                "caption": "Many Houston shops run both. Track them separately so you know which one pays.",
            },
            "scam": {
                "type": "stats",
                "title": "The fake-listing problem in numbers",
                "stats": [["50%", "of appliance repair Maps results looked fake in some areas"], ["10,000+", "fake listings in Google’s 2025 lawsuit"], ["2025", "year Google sued the network"]],
                "note": "Source: CBC Marketplace, CBS News",
                "alt": "Stats on fake appliance repair listings on Google Maps affecting appliance repair marketing in Houston",
                "caption": f"From {SRC['cbc']} and {SRC['cbs']}.",
            },
            "timeline": {
                "type": "steps",
                "title": "Keep customers informed on parts",
                "sub": "The update rhythm that prevents bad reviews",
                "steps": [["Diagnosis", "Text the finding, the price and the part ETA."], ["Part ordered", "Confirm the order and next update date."], ["Every few days", "Status text, even if nothing changed."], ["Part arrives", "Offer the next two slots right away."], ["Repair done", "Photo of the fix and a review link."]],
                "alt": "Steps for communicating appliance parts delays to customers for appliance repair companies in Houston",
                "caption": "Silence during a back-order is where most one-star reviews start.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for appliance repair ads",
                "sub": "Add these before launch, then read search terms weekly",
                "items": ["DIY: how to, diy, yourself, youtube, video", "Manuals: manual, wiring diagram, schematic", "Parts shoppers: part number, parts store, buy part", "New appliances: sale, deals, Best Buy, Lowe’s, Home Depot", "Used: used refrigerator, for sale, Facebook Marketplace", "Jobs: jobs, hiring, technician salary, training", "Warranty lookups: registration, recall check", "Brands or appliances you don’t service"],
                "alt": "Checklist of negative keywords for appliance repair Google Ads campaigns in Houston",
                "caption": "Appliance searches attract DIYers and shoppers. Cut them early.",
            },
            "season": {
                "type": "columns",
                "title": "Appliance calls by month in Houston",
                "sub": "Refrigerator and ice maker share of calls",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [35, 35, 40, 50, 65, 85, 100, 100, 80, 55, 45, 40],
                "highlight": [6, 7],
                "y_label": "Relative calls",
                "note": "Illustrative example",
                "alt": "Column chart of seasonal refrigerator repair demand for appliance repair companies in Houston",
                "caption": "Ovens spike before Thanksgiving and Christmas; washers and dryers stay steady.",
            },
            "pm": {
                "type": "steps",
                "title": "Win a property manager account",
                "sub": "What Houston property managers ask for",
                "steps": [["Vendor packet", "W-9, insurance, rates, diagnostic fee, service area."], ["Not-to-exceed", "Approve work under a set amount without a call."], ["Tenant scheduling", "Tech contacts the tenant directly."], ["Photo invoices", "Unit, issue, before and after photos."], ["Repair or replace", "A real number when the unit is old."]],
                "alt": "Steps for appliance repair companies to win landlord and property manager accounts in Houston",
                "caption": "Make the property manager’s job easier and the calls keep coming.",
            },
        },
    },
]
