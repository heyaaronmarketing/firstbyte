"""Pest control pair: "how to get more pest control customers" (seasonal Houston plan) + "pest control google ads" (setup guide).

Research: Texas A&M AgriLife urban entomology pages (Formosan termites swarm at night late May to early June; native
subterranean swarmers March-April in daylight), Texas A&M IPM on flood hazards (fire ant rafts, mosquitoes returning
weeks after water recedes), AgriLife Today on cold-weather invaders, Harris County Public Health via The Leader
(mosquito peak May-October, 56 species), TDA Structural Pest Control Service business license page and current-license
reports, 4 Tex. Admin. Code 7.152 (advertising) and 7.176 (real estate WDI reports) via Cornell LII, Google Business
Profile local ranking help, Google Local Services Ads category list, Google Ads Advanced Verification policy (garage
door and locksmith only), Google Ads help on location targeting, call conversions and seasonality adjustments, LocaliQ
home services benchmarks (pest and rodent control, 2020-2021 data) and a PCT Online piece by Evergrow Marketing with
2025 pest control Google Ads numbers.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "formosan": A("https://urbanentomology.tamu.edu/urban-pests/termites/formosan/", "Texas A&amp;M’s urban entomology program"),
    "native": A("https://citybugs.tamu.edu/factsheets/household/termites/ent-6002/", "Texas A&amp;M AgriLife’s termite fact sheet"),
    "flood": A("https://ipm.tamu.edu/2017/08/texas-am-agrilife-entomologists-floating-fire-ants-insect-pests-among-flood-hazards/", "Texas A&amp;M AgriLife entomologists"),
    "cold": A("https://agrilifetoday.tamu.edu/2015/11/26/agrilife-extension-entomologists-expect-invaders-as-weather-gets-colder/", "AgriLife Extension"),
    "hcph": A("https://www.theleadernews.com/health/beat-the-bite-hcph-reminds-residents-mosquito-season-is-here/article_858214bc-fc12-11ee-bbe0-8f2bf4477458.html", "Harris County Public Health"),
    "tda": A("https://texasagriculture.gov/RegulatoryPrograms/Pesticides/StructuralPestControlService/StructuralPestControlBusiness.aspx", "Texas Department of Agriculture’s Structural Pest Control Service"),
    "tdalist": A("https://texasagriculture.gov/Regulatory-Programs/Pesticides/Structural-Pest-Control-Service/Structural-Pest-Control-Reports-Current-Licenses", "TDA’s current license reports"),
    "adrule": A("https://www.law.cornell.edu/regulations/texas/4-Tex-Admin-Code-SS-7-152", "Texas advertising rule for pest control licensees (4 TAC § 7.152)"),
    "wdi": A("https://www.law.cornell.edu/regulations/texas/4-Tex-Admin-Code-SS-7-176", "4 TAC § 7.176"),
    "gbp": A("https://support.google.com/business/answer/7091", "Google’s own local ranking guidance"),
    "lsa": A("https://support.google.com/localservices/answer/6224841?hl=en", "Google’s Local Services category list"),
    "av": A("https://support.google.com/adspolicy/answer/7167922?hl=en", "Advanced Verification policy"),
    "geo": A("https://support.google.com/google-ads/answer/1722043", "Google’s location targeting help"),
    "calls": A("https://support.google.com/google-ads/answer/6100664", "Google’s call conversion help"),
    "season": A("https://support.google.com/google-ads/answer/10369906", "seasonality adjustments"),
    "localiq": A("https://localiq.com/blog/home-services-advertising-benchmarks/", "LocaliQ’s home services benchmarks"),
    "pct": A("https://www.pctonline.com/google-ads-mistakes-that-cost-pcos-thousands", "PCT Online"),
}

SIB1 = "/blog/how-to-get-more-pest-control-customers-houston/"
SIB2 = "/blog/pest-control-google-ads-guide/"

POSTS = [
    # ------------------------------------------------------------------ post 1
    {
        "slug": "how-to-get-more-pest-control-customers-houston",
        "title": "How to Get More Pest Control Customers in Houston: A Seasonal Plan",
        "seo_title": "How to Get More Pest Control Customers in Houston",
        "desc": "How to get more pest control customers in Houston: a month-by-month plan built on termite, mosquito and rodent seasons, plus reviews, LSA and recurring plans.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Nextdoor"],
        "art": "b2",
        "hero": "pest",
        "hero_alt": "Illustration of a pest control technician’s tools for a guide on how to get more pest control customers in Houston",
        "related": ["local-services-ads-vs-google-ads-home-services", "is-nextdoor-advertising-worth-it", "seasonal-marketing-greater-houston"],
        "sections": [
            (None, f"""<p>Houston homeowners call an exterminator when they see the bug, so the way to get more pest control customers in Houston is to advertise each pest in the weeks it shows up, then offer every one-time caller a quarterly plan before the technician leaves the driveway. Termites swarm in spring. Mosquitoes and fire ants run from May into fall. Rats and mice move into attics after the first real cool front.</p>
<p>Below is that calendar turned into a working plan for a residential shop north of Houston: what to push each month, where to spend, how to keep the phone busy in February, and one Texas advertising rule that a lot of borrowed ad copy breaks.</p>"""),

            ("How to get more pest control customers: follow Houston’s pest calendar", f"""<p>Pest demand here comes in waves, and the waves arrive on roughly the same dates every year. Texas A&amp;M’s entomologists have already mapped most of them.</p>
<ul>
<li><b>March and April:</b> native subterranean termite swarmers show up, usually in daylight, according to {SRC['native']}. Homeowners find wings on a windowsill and panic.</li>
<li><b>Late May and early June:</b> Formosan termites swarm at night and are drawn to lights, per {SRC['formosan']}. Formosans were first found in Texas near the Houston Ship Channel in Pasadena back in 1956, and a single colony can top a million termites.</li>
<li><b>May through October:</b> {SRC['hcph']} says mosquito activity typically peaks in these months, and the county has 56 mosquito species.</li>
<li><b>November through February:</b> mice, rats, squirrels and raccoons move into attics and walls as it cools, which {SRC['cold']} warns about every year.</li>
<li><b>After any big storm:</b> flooding brings floating fire ant colonies and, a few weeks after the water drops, a wave of mosquitoes.</li>
</ul>
<!--fig:calendar-->
<p>Here’s how we’d turn that into a working plan for a shop covering The Woodlands, Spring and Conroe.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Months</th><th>What customers notice</th><th>What to push</th><th>Where to spend</th></tr></thead>
<tbody>
<tr><td>Jan to Feb</td><td>Rodents in the attic, roaches indoors</td><td>Exclusion and rodent plans</td><td>Search ads, reviews, renewal emails</td></tr>
<tr><td>Mar to Apr</td><td>Termite swarmers in daylight, ants</td><td>Termite inspections, quarterly plans</td><td>Search, LSA, realtor outreach</td></tr>
<tr><td>May to Jun</td><td>Formosan swarms around porch lights</td><td>Termite treatment, mosquito pre-sales</td><td>Heaviest search budget of the year</td></tr>
<tr><td>Jul to Sep</td><td>Mosquitoes, fire ants, storm damage</td><td>Mosquito programs, fire ant lawn treatments</td><td>Search, Nextdoor, door hangers</td></tr>
<tr><td>Oct to Dec</td><td>First rodents, fall invaders</td><td>Rodent exclusion, annual plan renewals</td><td>Search, email to past customers</td></tr>
</tbody></table></div>
<p>Shops that run the same ads on the same budget twelve months a year overpay in December and run dry in May.</p>"""),

            ("How to get more pest control leads in termite season", f"""<p>Termite work is the highest-ticket job most residential pest companies sell, and Houston gets two swarm windows. For many shops, March through June pays for the rest of the year.</p>
<h3>Get ready in February</h3>
<ol>
<li>Write a termite page for your site that answers the questions people ask after they find wings: “Are these termites or flying ants?”, “Do swarmers mean my house is infested?”, “What does treatment cost?” Give a real price range or a clear inspection offer.</li>
<li>Add “Termite inspection” and “Termite treatment” as services on your Google Business Profile, with a short description of each.</li>
<li>Line up three or four photos of real swarmer evidence from your own jobs: wings on sills, mud tubes on slab edges. Post them to your profile during swarm weeks.</li>
<li>Build a separate termite campaign in Google Ads with its own budget so it can’t be starved by general pest clicks. We walk through that in our <a href="{SIB2}">pest control Google Ads setup guide</a>.</li>
</ol>
<h3>Work the swarm nights</h3>
<p>Formosan swarms happen at dusk and after dark around lights. That means the searches happen at 9 p.m. on a muggy evening in late May, when the homeowner is standing on the back patio in Kingwood or Spring watching a cloud around the porch light. If your ads shut off at 6 p.m. and nobody answers the phone, you hand those calls to whoever does.</p>
<p>During swarm weeks, run ads until 10 or 11 p.m. and route after-hours calls to a person or an answering service that can book a morning inspection. A 9 p.m. caller who reaches a human usually books; one who reaches a recording usually calls someone else.</p>"""),

            ("Summer: mosquitoes, fire ants and the post-storm spike", f"""<p>Mosquito service is the easiest recurring program to sell in Houston because nobody needs to be convinced the problem exists. Price and sell it as a season of visits. A monthly or every-three-weeks program from spring into fall lines up with the county’s May to October peak.</p>
<p>Fire ants are the other summer seller. Mounds pop up in every new-build yard from Magnolia to Katy, and a lawn treatment plan is easy to bundle with mosquito service for the same visit.</p>
<h3>Storms change everything for a few weeks</h3>
<p>After Harvey in 2017, {SRC['flood']} warned about fire ant colonies floating in floodwater as living rafts, and said nuisance mosquitoes would surge a few weeks after the water receded. Hurricane season runs June 1 through November 30, and Beryl in July 2024 showed how fast a storm can reshuffle everyone’s week.</p>
<p>Have a short storm plan written down before you need it:</p>
<ul>
<li>A pre-written Google Business Profile post and Nextdoor post about fire ants and standing water, ready to publish once roads are open.</li>
<li>A budget bump for mosquito and fire ant campaigns for the two to four weeks after flooding.</li>
<li>A rule for your team: help first, sell second. People remember who was useful after a storm.</li>
</ul>"""),

            ("Fall and winter: rodents and the renewal push", f"""<p>When the first real cool front comes through, rodent calls start. Rodent exclusion is a good winter product because it has a clear before and after, it often leads to attic cleanup work and the customer is usually ready for a plan once they’ve heard scratching above the bedroom.</p>
<p>Winter is also when you should be most active with customers you already have. Send renewal reminders. Ask for reviews from everyone you serviced in the summer. Call last spring’s one-time termite and mosquito customers and offer a quarterly plan starting in January. That list costs you nothing to market to, and it’s usually the cheapest new revenue you’ll find all year.</p>"""),

            ("Turn one-time jobs into quarterly plans", f"""<p>Pest control is a subscription business, and a lot of small shops still run it like a repair business.</p>
<p>Say you charge $175 for a one-time general pest service and $125 a quarter for a plan (illustrative numbers; use yours). The one-time customer is worth $175. The plan customer is worth $500 in year one, and if they stay three years, $1,500. The same ad click bought both.</p>
<!--fig:recurring-->
<p>Ways to raise your conversion from one-time to recurring:</p>
<ul>
<li><b>Offer the plan on the first call.</b> Quote both prices side by side. Many people pick the plan once they see the per-visit math.</li>
<li><b>Credit the first service.</b> “Your $175 today becomes your first quarterly visit if you sign up this week.”</li>
<li><b>Give technicians a script and a reason.</b> A small bonus per plan signed on site gets more results than a sales training video.</li>
<li><b>Follow up within seven days.</b> A text with a one-tap sign-up link catches people who said “let me talk to my wife.”</li>
<li><b>Make cancel and pause easy.</b> It sounds backwards, but customers sign up more readily when leaving isn’t a fight.</li>
</ul>
<p>Once you know your plan conversion rate and average customer lifetime, you can work out what a new lead is really worth, which tells you how much you can afford to pay for one. Our guide to <a href="/blog/understanding-cost-per-lead/">understanding cost per lead</a> shows the math.</p>"""),

            ("Google Business Profile and reviews: your free lead source", f"""<p>When someone in Tomball searches “exterminator near me,” the three map results get most of the calls. {SRC['gbp']} says plainly that more reviews and positive ratings can help a business rank locally, and it recommends replying to them.</p>
<p>What we’d do on a pest control profile:</p>
<ul>
<li>Pick “Pest control service” as the primary category and add secondary ones you truly offer, like termite control.</li>
<li>List every service you sell, with a sentence each: termite inspections, mosquito programs, rodent exclusion, fire ant treatment, bed bugs.</li>
<li>Set your service area to the cities and ZIP codes you actually drive to, not all of Greater Houston.</li>
<li>Post weekly in season. Short and timely beats polished: “Formosan swarms are starting around Lake Conroe. Here’s how to tell them from flying ants.”</li>
<li>Ask for a review after every first service and every plan sign-up, by text, with a direct link. Technicians who ask in person get the most.</li>
</ul>
<p>For the full process, see our <a href="/blog/complete-guide-google-reviews/">guide to Google reviews</a> and <a href="/blog/rank-in-google-map-pack-houston/">how to rank in the Houston map pack</a>.</p>"""),

            ("Pest control marketing in Houston: lead with your TDA license", f"""<p>In Texas, the {SRC['tda']} licenses pest control businesses. Each business location needs its own license, the commercial license costs $300, and the state says you can’t conduct business or advertise until it’s issued. Every commercial licensee also has to name a responsible certified applicator and carry at least $500,000 in bodily injury and property damage coverage with a $1,000,000 aggregate.</p>
<p>Most homeowners have no idea any of this exists. Tell them. Put your TDA business license number on your site footer, your Google Business Profile description, your truck and your door hangers. Explain in one line that the state keeps public records of licensed businesses (it publishes them in {SRC['tdalist']}). Fly-by-night operators can’t match that, and it’s a better trust signal than a stock photo of a smiling tech.</p>
<p>Watch your claims, though. The {SRC['adrule']} lists “safe,” “harmless” and “non-toxic to humans and pets” among the prohibited claims, and adding “when used as directed” doesn’t fix it. It also lists “environmentally friendly,” “organic” and “contain all natural ingredients,” and it requires every ad to include your business name as it appears on your license. Plenty of franchise and national templates say “pet-safe treatments.” In Texas, that line has to go.</p>"""),

            ("Local Services Ads, search ads and Nextdoor", f"""<p>Pest control is one of the categories in {SRC['lsa']}, and you pay for leads instead of clicks. Local Services Ads sit above everything else on many “pest control near me” searches, and they lean hard on reviews and responsiveness. If your review count is decent and you answer the phone, start there. Our comparison of <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs. Google Ads</a> explains how the two work together, and our post on the <a href="/blog/google-guaranteed-vs-google-verified/">Google Verified badge</a> covers the screening.</p>
<p>Search ads give you what LSA doesn’t: control over which pests you promote, which hours you run and which landing page people see. That’s where your termite and mosquito seasons get their own budgets. If you want help with that side, it’s what our <a href="/services/search-marketing/">search marketing team</a> does every day.</p>
<p>Nextdoor is worth a test for recurring plans because neighbors talk about bugs constantly, and one happy customer’s recommendation in a Woodlands village group can bring several calls. We wrote an honest take on <a href="/blog/is-nextdoor-advertising-worth-it/">whether Nextdoor advertising is worth it</a> if you’re weighing paid posts there.</p>"""),

            ("Real estate termite inspections and door-to-door, done right", f"""<p>Every home sale in termite country is a chance to meet a new customer. Texas requires wood destroying insect reports in real estate deals to be issued on a state-prescribed form by the licensed business (see {SRC['wdi']}), and many buyers, agents and lenders ask for one. The inspection itself is a small ticket. The customer who just bought a 1990s house in Spring and hears “we found old tube activity” is a treatment and a plan.</p>
<!--fig:wdi-->
<p>How to build the referral side:</p>
<ol>
<li>Make a list of the 20 most active listing and buyer agents in your area, plus the home inspectors they use.</li>
<li>Offer a real service promise: report back within 48 hours, photos included, online scheduling.</li>
<li>Drop off a one-page explainer on Formosan versus native termites agents can forward to buyers.</li>
<li>Send a thank-you and an update after every referred job. Agents keep sending work to people who make them look good.</li>
</ol>
<h3>Door-to-door works better with digital behind it</h3>
<p>Summer door knocking still sells plans across Montgomery County subdivisions. It works better when the homeowner can look you up on the spot and see 200 reviews and a TDA license number. Before a door team hits a neighborhood, make sure your profile is current, run a small search campaign in those ZIP codes and leave a door hanger with a short web address that goes to a page built for that offer. Then track sign-ups by neighborhood so you know which streets to revisit.</p>
<!--fig:towns-->"""),

            ("Work backward from the next swarm", f"""<p>Open a calendar to the next swarm window or the next big storm and count back four weeks. That’s your deadline for the termite page, the separate campaign, the evening call coverage and the review texts. Put the next season’s deadline on the same calendar while you’re there.</p>
<p>Then look at last spring honestly. If your search budget was gone by the third week of May, right when Formosans were swarming, our free <a href="/contact/">Ad Spend Leak Check</a> will show where it went. We record a 10-minute walkthrough of your Google or Meta account and send it within 48 hours. We work with <a href="/industries/service/">home service companies</a> across <a href="/digital-marketing-agency-conroe-tx/">Conroe</a>, <a href="/digital-marketing-agency-spring-tx/">Spring</a> and the rest of the north Houston suburbs.</p>"""),
        ],
        "faq": [
            ("What are the best pest control marketing ideas for a small company?",
             "Start with what costs little: a complete Google Business Profile, a review request after every service, and calls to past one-time customers offering a quarterly plan. Then add seasonal search ads for termites in spring and mosquitoes in summer, a realtor and home inspector referral program for termite inspections, and door hangers in neighborhoods where you already have customers. Measure each idea by booked jobs, not by clicks or likes."),
            ("What pest control marketing strategies work best in Houston?",
             "Strategies that follow Houston’s pest calendar work best. Push termite inspections from March through June, mosquito and fire ant programs from May through October, and rodent exclusion once the weather cools. Keep a storm plan ready for flooding, show your Texas Department of Agriculture license everywhere, and convert first-time callers into recurring plans so each new customer is worth several visits."),
            ("How do I grow a pest control business?",
             "Growth in pest control comes mostly from recurring revenue. Get more first calls through Google, reviews and referrals, then turn as many of them as you can into quarterly or monthly plans and keep them with good service and easy renewals. Once your plan conversion rate and customer lifetime are known, you can spend more confidently on advertising and add technicians, routes and new service areas."),
            ("How much should a pest control company spend on marketing?",
             "There is no single right number, but many small home service companies budget a share of revenue and adjust by season. A better method is to start from what a new customer is worth over their lifetime, decide what you can pay to win one, and set ad budgets to hit that cost. Spend more in termite and mosquito season and less in slow winter weeks."),
            ("Do I need to show my license in pest control ads in Texas?",
             "Texas rules say you can’t advertise structural pest control services without a license, and every ad must include your business name as it appears on your license. Showing your license number on your site, profile, trucks and printed pieces is also a smart trust signal. Avoid claims like safe, non-toxic or organic, which the state’s advertising rule prohibits."),
        ],
        "figures": {
            "calendar": {
                "type": "columns",
                "title": "Houston pest demand by month",
                "sub": "Relative call volume for a typical north Houston residential shop",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [35, 38, 62, 80, 100, 92, 78, 74, 66, 50, 44, 36],
                "highlight": [4, 5],
                "y_label": "Relative demand",
                "note": "Illustrative example, shaped by Texas A&M swarm timing and the county’s mosquito season",
                "alt": "Column chart of pest control demand peaking in Houston termite season, when to get more pest control customers",
                "caption": f"Formosan swarms in late May and early June usually make that stretch the busiest, per {SRC['formosan']}.",
            },
            "recurring": {
                "type": "funnel",
                "title": "Where a pest control lead’s value comes from",
                "stages": [
                    ["One-time service", "$175"],
                    ["Quarterly plan, year one", "$500"],
                    ["Plan kept two years", "$1,000"],
                    ["Plan kept three years", "$1,500"],
                ],
                "note": "Illustrative example using a $175 one-time price and $125 per quarter",
                "alt": "Funnel showing how a quarterly plan multiplies the value of a pest control customer for a Houston pest company",
                "caption": "The same ad click can be worth $175 or $1,500, depending on what you sell on the first visit.",
            },
            "wdi": {
                "type": "checklist",
                "title": "Realtor referral kit for termite inspections",
                "sub": "What to hand agents and inspectors in your area",
                "items": [
                    "Online booking link for WDI inspections",
                    "48-hour report turnaround with photos",
                    "One-page Formosan vs. native termite explainer",
                    "Your TDA business license number",
                    "Treatment price ranges so buyers can plan",
                    "A direct cell number for agents",
                    "Thank-you note after each referred job",
                ],
                "alt": "Checklist for a realtor referral program that helps a pest control company in Houston win termite inspection customers",
                "caption": "Agents refer the company that makes closing easier, so make the paperwork painless.",
            },
            "towns": {
                "type": "map",
                "title": "Where a north Houston pest route might run",
                "sub": "Fast-growing suburbs with lots of new builds and wooded lots",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Magnolia", "Tomball", "Kingwood", "Montgomery"],
                "note": "Illustrative service area",
                "alt": "Map of The Woodlands, Spring, Conroe and nearby towns where a Houston pest control company can find more customers",
                "caption": "Tight routes keep drive time down, so market hardest where your trucks already go.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2
    {
        "slug": "pest-control-google-ads-guide",
        "title": "Pest Control Google Ads: A 2026 Setup Guide for Houston Exterminators",
        "seo_title": "Pest Control Google Ads: 2026 Setup Guide",
        "desc": "Pest control Google Ads, set up right: campaign structure, negative keywords, Texas-compliant ad copy, ZIP targeting, call tracking and Houston budget math.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Tag Manager", "Google Analytics"],
        "art": "b4",
        "hero": "growth",
        "hero_alt": "Illustration of a rising growth chart for a pest control Google Ads setup guide for Houston exterminators",
        "related": ["google-ads-cost-per-click-houston-benchmarks", "call-tracking-which-ads-make-phone-ring", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>Pest control Google Ads work when you split campaigns by pest (termite, general pest, mosquito, rodent), use exact and phrase match with a long negative keyword list, target only the ZIP codes your trucks serve and count phone calls as conversions. Skip any one of those and most of your budget goes to people looking for bug spray at Home Depot.</p>
<p>Below is the account we’d build for a residential pest company in The Woodlands, Spring or Conroe, in the order we’d build it, with the cost figures we could actually verify and the ad copy limits Texas puts on pest companies.</p>"""),

            ("What pest control Google Ads cost in Houston", f"""<p>Real pest control numbers are hard to find, so here’s what we could verify.</p>
<ul>
<li>{SRC['localiq']} put pest and rodent control search ads at a $6.55 average cost per click, a 4.31% click-through rate and a $39.25 cost per lead, with a typical spend of $1,250 a month. That data is from 2020 and 2021, so treat it as a floor. Costs have climbed since.</li>
<li>An agency that runs pest control accounts, writing in {SRC['pct']}, reported a $5.99 average CPC across its clients and an average cost per lead of about $98 in 2025, with mosquito leads as low as $30 in some months.</li>
</ul>
<!--fig:numbers-->
<p>Neither source breaks out Houston, and we wouldn’t assume our suburbs come in under those figures during swarm weeks. Keyword Planner’s top-of-page bid ranges for your own ZIP codes are a better starting point than any national average. For broader context, see our <a href="/blog/google-ads-cost-per-click-houston-benchmarks/">Houston Google Ads cost per click benchmarks</a>.</p>
<h3>Budget math you can check yourself</h3>
<p>Here’s an illustrative month for a two-truck shop. Plug in your own numbers.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line</th><th>Example</th><th>How it’s figured</th></tr></thead>
<tbody>
<tr><td>Monthly ad spend</td><td>$3,000</td><td>Your budget</td></tr>
<tr><td>Average CPC</td><td>$7.50</td><td>From your account; assume higher in swarm season</td></tr>
<tr><td>Clicks</td><td>400</td><td>$3,000 ÷ $7.50</td></tr>
<tr><td>Lead rate (calls + forms)</td><td>12%</td><td>Leads ÷ clicks</td></tr>
<tr><td>Leads</td><td>48</td><td>400 × 12%</td></tr>
<tr><td>Cost per lead</td><td>$62.50</td><td>$3,000 ÷ 48</td></tr>
<tr><td>Booked jobs (50% close)</td><td>24</td><td>Leads × close rate</td></tr>
<tr><td>Cost per new customer</td><td>$125</td><td>$3,000 ÷ 24</td></tr>
</tbody></table></div>
<p>If a third of those 24 customers take a quarterly plan, a $125 acquisition cost is a bargain. If none of them do, it’s a coin flip. That’s why we tie ad budgets to plan conversion, which we cover in our companion post on <a href="{SIB1}">how to get more pest control customers in Houston</a>.</p>"""),

            ("Campaign structure: termite, general pest, mosquito, rodent", f"""<p>The single best structural decision is giving termite work its own campaign. Termite jobs are worth far more than a general pest visit, the season is short and the cost per click can spike in swarm weeks. Lumped in with “roach exterminator” keywords, termite searches compete for the same daily budget and lose.</p>
<p>The PCT Online piece warns against splitting every pest into its own campaign, because most searchers use general phrases like “pest control near me.” We agree. Separate campaigns only for pests that have their own season, price or budget.</p>
<!--fig:structure-->
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Ad groups</th><th>Landing page</th><th>Peak months</th></tr></thead>
<tbody>
<tr><td>Termite</td><td>Inspection, treatment, Formosan, swarmers</td><td>Termite page with inspection booking</td><td>Mar to Jun</td></tr>
<tr><td>General pest</td><td>Exterminator, pest control, roaches, ants, spiders</td><td>Quarterly plan page with both prices</td><td>Year-round</td></tr>
<tr><td>Mosquito</td><td>Mosquito control, yard spraying service</td><td>Seasonal program page</td><td>Apr to Oct</td></tr>
<tr><td>Rodent</td><td>Rat removal, mice, exclusion, attic</td><td>Exclusion page with photos</td><td>Oct to Feb</td></tr>
</tbody></table></div>
<p>Bed bugs and wildlife can sit as ad groups under general pest unless you sell them at volume.</p>"""),

            ("Pest control PPC keywords: match types and negatives", f"""<p>Use exact and phrase match. Broad match on a small pest budget tends to find every DIY search in Texas. The agency writing in PCT Online reported that six words (spray, repellant, trap, killer, bait and poison) were eating more than a quarter of its clients’ budgets before they were blocked.</p>
<h3>Starter negative keyword list</h3>
<p>Add these as broad match negatives at the account level, then read your search terms report weekly and keep adding.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Theme</th><th>Negatives to add</th></tr></thead>
<tbody>
<tr><td>DIY intent</td><td>diy, how to get rid of, home remedy, homemade, yourself</td></tr>
<tr><td>Products</td><td>spray, killer, trap, bait, poison, repellent, repellant, fogger, bomb, dunks, granules</td></tr>
<tr><td>Retail</td><td>home depot, lowes, walmart, amazon, ace hardware</td></tr>
<tr><td>Jobs</td><td>jobs, hiring, salary, career, technician training, license test, exam</td></tr>
<tr><td>Research</td><td>pictures, identify, life cycle, what do, symptoms</td></tr>
<tr><td>Wrong service</td><td>bee removal (if you don’t do it), car, plants, garden, chickens</td></tr>
</tbody></table></div>
<p>Careful with “spray.” As a broad negative it also blocks “mosquito spraying service,” which is exactly what your mosquito campaign sells, so use a phrase negative like “mosquito spray” there instead. And leave “cost” and “price” alone. Someone searching “termite treatment cost Spring TX” is close to buying.</p>"""),

            ("Pest control ads examples that follow Texas rules", f"""<p>Before you copy a template, read the {SRC['adrule']}. Its list of prohibited claims includes “safe,” “harmless,” “non-toxic to humans and pets,” “environmentally friendly” and “organic,” and it requires every ad to show your business name as it appears on your TDA license. The rule’s definition of advertising covers digital ads, so a Google headline counts the same as a truck wrap. A lot of national pest ad templates break it in headline one.</p>
<!--fig:copy-->
<p>Some headlines that stay within the rules (swap in your name and towns):</p>
<ul>
<li>Termite Inspection in The Woodlands</li>
<li>Formosan Swarmers? Book Today</li>
<li>Licensed by the Texas Dept. of Ag</li>
<li>Quarterly Pest Plans From $125</li>
<li>Same-Week Service in Spring &amp; Conroe</li>
<li>Rodent Exclusion and Attic Sealing</li>
<li>Locally Owned in Montgomery County</li>
<li>Call Now, Real People Answer</li>
</ul>
<p>A description line might read: “Formosan termites swarm at night in late May and June. Our licensed techs inspect, photograph and explain your options. Book online or call.” Specific, local and nothing the state would object to.</p>
<p>Responsive search ads take up to 15 headlines. We like a mix of roughly a third service, a third location and a third call to action, and we pin only the headline that carries the licensed business name so the rule is met every time the ad shows. Test “Schedule an inspection” against “Get a free estimate” on termite ads; the PCT Online piece describes a call-to-action change like that paying off. Prices in ads only work if they match your landing page and what the phone team quotes.</p>"""),

            ("Assets that make the phone ring", f"""<p>Assets (Google’s new name for extensions) are where pest ads win the click.</p>
<ul>
<li><b>Call asset:</b> your tracking number, scheduled for hours someone actually answers. Extend it into the evening during swarm season.</li>
<li><b>Location asset:</b> link your Google Business Profile so your address and rating can show.</li>
<li><b>Sitelinks:</b> Termite Inspections, Mosquito Program, Quarterly Plans, Service Areas, Reviews.</li>
<li><b>Callouts:</b> TDA licensed, locally owned, free re-service between visits, online booking.</li>
<li><b>Structured snippets:</b> Services header listing termites, ants, roaches, rodents, mosquitoes, bed bugs.</li>
</ul>
<p>Each sitelink should go to its own page. Sending everything to your homepage is one of the most common leaks we see. Our <a href="/blog/landing-pages-101/">landing page guide</a> covers what those pages need.</p>"""),

            ("Location targeting by ZIP across Montgomery and Harris counties", f"""<p>{SRC['geo']} confirms that in the U.S. you can target postal codes, and it describes two options: “Presence or interest,” which also reaches people who have shown interest in your area, and “Presence,” which limits ads to people physically there. For pest control, set it to Presence. Someone in Dallas reading about Houston termites won’t book you.</p>
<p>Then target by ZIP rather than a big radius. A 25-mile ring around The Woodlands pulls in north Houston neighborhoods you may never drive to. ZIPs let you add 77380, 77381 and 77382 for The Woodlands, 77375 for Tomball, 77354 for Magnolia, 77301 for Conroe and 77339 and 77345 for Kingwood, and then compare cost per lead by area.</p>
<!--fig:zips-->
<p>After 30 days, check the location report. Raise bids in ZIPs that book well and are close to your routes. Cut ZIPs where the drive eats the profit. If you serve both sides of the county line, keep Montgomery County and Harris County ZIPs in separate campaigns or ad groups so you can see each clearly.</p>"""),

            ("Google ads for exterminators vs. Local Services Ads", f"""<p>Pest control is a Local Services category, listed in {SRC['lsa']}, and LSA charges per lead. On many “exterminator near me” searches it shows above regular search ads. Most pest companies should run both. LSA is often the cheaper lead, while search ads let you push termite season, choose your landing pages and run specific offers.</p>
<p>Watch for overlap. If LSA is already eating the generic “pest control near me” calls at a good price, move search ad budget toward termite and mosquito keywords LSA covers less well. Our <a href="/blog/local-services-ads-vs-google-ads-home-services/">LSA vs. Google Ads comparison</a> goes deeper.</p>
<p>On approvals: pest control isn’t one of the categories in Google’s {SRC['av']} (that program covers garage door and locksmith services), but LSA runs its own background and license screening, and Texas wants your TDA license issued before you advertise at all.</p>"""),

            ("Conversion tracking for calls", f"""<p>Most pest leads arrive as phone calls, so an account that only counts form fills is flying blind. {SRC['calls']} explains that you set a minimum call length, and every call lasting at least that long counts as a conversion. Tracking calls from ads and your website requires Google forwarding numbers, so turn on call reporting in account settings.</p>
<!--fig:tracking-->
<p>For pest, we set the minimum call length around 60 to 90 seconds so wrong numbers and robocalls don’t count. Then go a step further: import booked jobs from your scheduling software as offline conversions, so Google learns which clicks became customers. Our post on <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking</a> covers the tools.</p>"""),

            ("Your first 30 days in the account", f"""<p>A new pest account is never right on day one. Here’s the routine we follow in the first month, and it’s the same one we’d hand an owner running ads in-house.</p>
<h3>Week 1</h3>
<p>Check that calls are being recorded as conversions by placing a test call from an ad preview and staying on past your minimum length. Look at the search terms report every day. You’ll find DIY and product searches the starter list missed, especially brand names of retail sprays. Add them.</p>
<h3>Week 2</h3>
<p>Listen to a sample of recorded calls if your tracking tool allows it. Are people asking for services you sell, in towns you serve? Are calls going unanswered at lunch or after 5 p.m.? Missed calls are wasted clicks, and they’re usually a staffing fix, not an ads fix.</p>
<h3>Weeks 3 and 4</h3>
<p>Compare cost per lead by campaign and by ZIP. Pause keywords that spent twice your target cost per lead without a single call. Rewrite the weakest headlines, keeping your best performers. If the termite campaign is limited by budget during swarm weeks, move money from general pest rather than raising the total.</p>
<p>By day 30 you should know three things: your real cost per lead, which pest brings the cheapest booked jobs, and which areas are worth more budget. If you can’t answer those, the tracking is the problem, and that’s the first thing to fix. Our guide to <a href="/blog/performance-max-vs-search-campaigns-local/">Performance Max vs. Search for local businesses</a> explains why we hold off on Performance Max until those answers are clear.</p>"""),

            ("Seasonality: shifting bids and budgets by month", f"""<p>Smart Bidding already learns regular seasonal patterns. Google’s own help on {SRC['season']} says they’re built for short events of one to seven days and may not work as well past 14. So don’t set a “termite season” adjustment for three months. Use one for a two or three day burst, like the first big Formosan swarm nights or the week after a flood.</p>
<p>For the longer seasons, move budget between campaigns instead. Raise the termite budget in March, let mosquito take over in summer, lift rodent in late fall. Expect cost per click to rise when everyone else does the same, and decide your ceiling in advance with a maximum CPC limit.</p>
<p>If you already have an account running, start with two checks before you build anything new. Under campaign settings, open Locations and confirm the option is “Presence,” not “Presence or interest.” Then pull the last 90 days of search terms, sort by cost and read the top 50 out loud. You’ll know within ten minutes whether DIY searches are eating the budget.</p>
<p>Prefer someone else do that pass? Our free <a href="/contact/">Ad Spend Leak Check</a> covers the same ground, including your location option, negatives and the minimum call length you count as a conversion, in a 10-minute recorded video sent within 48 hours. Our <a href="/services/search-marketing/">search marketing</a> team manages Google Ads for <a href="/industries/service/">home service companies</a> around Houston if you want help after that.</p>"""),
        ],
        "faq": [
            ("How much should a pest control company spend on Google Ads?",
             "Start from what you can pay for a new customer. If a customer is worth $500 or more over a year on a plan, spending $100 to $150 to win one is reasonable. A small shop can test with a few thousand dollars a month, spending more from March through June for termites. LocaliQ data from 2020 and 2021 showed pest companies spending about $1,250 a month."),
            ("What is a good cost per lead for pest control Google Ads?",
             "It varies by pest and season. LocaliQ’s 2020 and 2021 benchmark put pest and rodent control at about $39 per lead, while an agency writing in PCT Online in 2025 reported an average near $98, with mosquito leads as low as $30 in some months. Termite leads usually cost more but are worth more. Judge cost per booked job, not just cost per lead."),
            ("Is the Reddit advice on pest control Google Ads right about broad match?",
             "Mostly, yes. The common advice on Reddit and in trade forums is to avoid broad match on small budgets, and that matches what we see. Broad match tends to pull DIY searches for sprays, traps and poisons. Use exact and phrase match, add negative keywords from day one and review the search terms report every week before trying broad match with Smart Bidding later."),
            ("What are good pest control advertising ideas besides Google Ads?",
             "Local Services Ads are the closest cousin and often the cheapest lead. Beyond Google, try realtor and home inspector partnerships for termite inspections, door hangers and door-to-door teams in neighborhoods where you already service homes, Nextdoor for recurring plans, and email or text reminders to past one-time customers. Make sure every channel points to the same reviews and license number."),
            ("Do pest control companies need special approval to run Google Ads?",
             "Google’s Advanced Verification program applies to garage door and locksmith advertisers, not pest control. You will go through screening if you run Local Services Ads. In Texas, the bigger requirement is your Structural Pest Control Service business license from the Department of Agriculture, which you need before you advertise, plus following the state’s rules on safety and environmental claims."),
        ],
        "figures": {
            "numbers": {
                "type": "stats",
                "title": "Pest control search ad numbers we could verify",
                "stats": [
                    ["$6.55", "avg. CPC, pest and rodent control (LocaliQ, 2020–21)"],
                    ["$5.99", "avg. CPC across one agency’s pest clients, 2025"],
                    ["$98", "avg. cost per lead in that agency’s 2025 data"],
                    ["25%+", "of budget lost to six DIY words before negatives"],
                ],
                "note": "Sources: LocaliQ home services benchmarks; Evergrow Marketing in PCT Online",
                "alt": "Stat tiles with pest control Google Ads cost per click and cost per lead benchmarks for Houston exterminators",
                "caption": f"Benchmarks from {SRC['localiq']} and {SRC['pct']}; Houston’s suburbs usually run higher.",
            },
            "structure": {
                "type": "steps",
                "title": "How we build a pest control Google Ads account",
                "sub": "Order of operations for a Houston-area residential shop",
                "steps": [
                    ["Set up call tracking", "Turn on call reporting and count calls over 60 to 90 seconds."],
                    ["Build four campaigns", "Termite, general pest, mosquito and rodent, each with its own budget."],
                    ["Load negatives first", "Block DIY, product, retail and job searches before launch."],
                    ["Target ZIPs, not radius", "Use Presence targeting and only the ZIPs your routes cover."],
                    ["Write compliant ads", "Use your licensed business name and skip safety claims."],
                    ["Review weekly", "Search terms, cost per booked job and ZIP performance."],
                ],
                "alt": "Six steps for setting up pest control Google Ads in Houston, from call tracking to weekly search term reviews",
                "caption": "Tracking comes first, because every later decision depends on knowing which clicks booked jobs.",
            },
            "copy": {
                "type": "compare",
                "title": "Pest control ad copy in Texas",
                "left": {"title": "Common template copy", "items": ["Pet-safe, non-toxic treatments", "Eco-friendly pest control", "All-natural, organic options", "No business name in the ad"]},
                "right": {"title": "Copy that fits the rules", "items": ["Licensed by the Texas Dept. of Ag", "Formosan swarmers? Book today", "Quarterly plans from $125", "Your licensed business name shown"]},
                "alt": "Comparison of pest control ads examples that break Texas advertising rules and Google Ads copy that follows them",
                "caption": f"Texas bans safety and natural claims in pest control advertising under {SRC['adrule']}.",
            },
            "zips": {
                "type": "map",
                "title": "ZIP targeting across two counties",
                "sub": "Example Montgomery and Harris County areas for a north Houston route",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Magnolia", "Tomball", "Kingwood"],
                "note": "Illustrative service area",
                "alt": "Map of The Woodlands, Conroe, Tomball and Kingwood areas targeted by ZIP code in pest control Google Ads",
                "caption": "Compare cost per lead by ZIP after 30 days and move budget toward the areas your trucks already cover.",
            },
            "tracking": {
                "type": "checklist",
                "title": "Call tracking checklist for pest control ads",
                "sub": "Set these before you spend the first dollar",
                "items": [
                    "Call reporting on with Google forwarding numbers",
                    "Calls from ads counted at 60 to 90 seconds",
                    "Website call tracking on every landing page",
                    "Form fills tracked with the Google tag",
                    "Booked jobs imported as offline conversions",
                    "Separate conversion values for termite jobs",
                    "Missed-call alerts sent to the office",
                ],
                "alt": "Checklist for tracking phone calls from pest control Google Ads so Houston exterminators know which ads book jobs",
                "caption": "Calls are most pest leads, so an account that only counts forms can’t optimize.",
            },
        },
    },
]
