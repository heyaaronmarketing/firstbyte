"""Batch 8: home builder marketing for Houston and Montgomery County custom/semi-custom/small production builders,
and auto repair shop marketing in Houston (independent, tire, transmission, collision).

Research: Community Impact on Zonda's June 2025 GHBA Houston briefing (quick move-ins 3-3.2 per community, 44 days on
market, prices 5% off peak and 40% above 2019); Houston Agent Magazine on RCLCO's 2025 top-selling MPCs (Sunterra No. 5,
1,024 sales); NAHB Eye on Housing (186,000 custom starts in 2025, almost 20% of single-family starts); Community
Impact on Conroe MPCs (Grand Central Park, Evergreen, Cielo, The Woodlands Hills, Artavia); Jon Loomer on Meta's
Housing special ad category; Google's housing/employment/credit personalized ads FAQ; 24 CFR 100.75 (govinfo);
Zillow Listing Connect / Promoted Communities; Zonda's BDX/NewHomeSource acquisition (Feb 2024).
Auto post: Google Local Services Ads category list (auto verticals, no Google Verified badge for auto); Search Engine
Roundtable Aug 2026 on LSA pre-badge ads and split auto categories; Google Maps prohibited content policy (incentives,
gating); PPC Land on the April 2026 staff-quota/staff-content rule; TxDMV bulletin on HB 3297 (safety inspections
ended Jan 1, 2025; 17 emissions counties; $7.50 replacement fee; $16.75 for new vehicles); S&P Global Mobility (12.8
year average vehicle age, 289 million vehicles); ABC13 on Houston heat and battery life; Morgan Lewis on Texas SB 140.
Competitor/PAA phrasing read for "home builder marketing", "how to market a custom home builder", "builder lead
generation", "auto repair shop marketing", "how to get more customers for auto repair shop", "auto repair google ads".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # builder post
    "ci_zonda": A("https://communityimpact.com/bay-area/development/houstons-housing-market-stabilizing-incentives-price-cuts-still-driving-sales/", "Community Impact’s write-up of Zonda’s Houston briefing"),
    "rclco": A("https://houstonagentmagazine.com/2026/01/08/sunterra-houstons-top-selling-mpc/", "Houston Agent Magazine’s summary of RCLCO’s 2025 rankings"),
    "nahb": A("https://eyeonhousing.org/2026/03/custom-home-building-expanded-in-2025/", "NAHB’s Eye on Housing"),
    "conroe": A("https://communityimpact.com/conroe-montgomery/development/5-master-planned-communities-growing-in-conroe/", "Community Impact"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "gfaq": A("https://support.google.com/adspolicy/answer/9997418?hl=en", "Google’s housing, employment and credit policy FAQ"),
    "cfr": A("https://www.govinfo.gov/content/pkg/CFR-2019-title24-vol1/pdf/CFR-2019-title24-vol1-sec100-75.pdf", "24 CFR 100.75"),
    "zlc": A("https://www.zillow.com/resources/new-construction/introducing-listing-connect", "Zillow’s Listing Connect page"),
    "bdx": A("https://zondahome.com/zonda-acquires-bdx/", "bought BDX in February 2024"),
    # auto post
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "ser": A("https://seroundtable.com/google-lsa-prebadge-new-verticals-41920.html", "Search Engine Roundtable"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    "ppcl": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
    "txdmv": A("https://content.govdelivery.com/accounts/TXDMV/bulletins/3b3121b", "TxDMV’s bulletin on the change"),
    "spg": A("https://press.spglobal.com/2025-05-21-U-S-Vehicle-Age-Rises-Again-to-12-8-Years-in-2025,-According-to-S-P-Global-Mobility", "S&P Global Mobility"),
    "abc13": A("https://abc13.com/13519595/", "told ABC13"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
}

BUILDER = "/blog/home-builder-marketing-houston-montgomery-county/"
AUTO = "/blog/auto-repair-shop-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: home builders
    {
        "slug": "home-builder-marketing-houston-montgomery-county",
        "title": "Home Builder Marketing in Houston and Montgomery County: A Working Playbook",
        "seo_title": "Home Builder Marketing in Houston & Montgomery County",
        "desc": "Home builder marketing for Houston and Montgomery County custom and small production builders: community pages, Google Ads, Meta housing rules, co-op.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Analytics"],
        "art": "b3",
        "hero": "house",
        "hero_alt": "Illustration of a new house for home builder marketing in Houston, The Woodlands and Montgomery County",
        "related": ["real-estate-agent-marketing-the-woodlands-houston", "pool-builder-marketing-houston-the-woodlands", "how-to-get-more-remodeling-leads-houston"],
        "sections": [
            (None, f"""<p>Saturday at the model home off FM 1488. Eleven groups walked through. Your sales counselor thinks three of them mentioned seeing “an ad,” one came with an agent from Katy, and the rest “just drove by.” Monday, your marketing person shows you a Meta report with 214 leads for the month.</p>
<p>Nobody in the building can connect those two numbers. That’s the real problem in most home builder marketing.</p>
<p>Home builder marketing that works in Houston and Montgomery County gets your communities and quick move-in homes in front of buyers already searching a specific area, then stays in front of them for the six to twelve months they take to decide. Small builders can win that part by being sharper than the big guys (louder is off the table anyway). Where almost everyone leaks money is the tracking: who actually walked the model, and who signed.</p>
<p>This playbook is for custom, semi-custom and small production builders with one to maybe eight active communities.</p>"""),

            ("Why marketing a home builder is different from marketing a contractor", f"""<p>A roofer’s customer decides in a week. Your buyer might take a year, and most of that year they’re not ready to talk to you.</p>
<p>Before a family signs on a new build, a lot has to line up: the area (often a school district first), a lot or plan they like (for custom work, maybe land they already own near Lake Conroe), financing that often depends on selling their current house, and enough trust in you to hand over the biggest check of their lives.</p>
<p>So a lead from a Facebook form in March is rarely a sale in April. Fine, as long as nobody in the company judges campaigns by 30-day results.</p>
<!--fig:journey-->
<p>Every campaign needs a “not yet” path. Usually that’s an email sequence and a retargeting audience, plus some reason to come back, like a plan release, a phase opening or an incentive deadline. Judge the whole thing on appointments and model visits. Raw lead counts will lie to you for months.</p>
"""),

            ("The Houston new-home market you’re selling into right now", f"""<p>At a Greater Houston Builders Association luncheon in June 2025, Zonda’s chief economist said quick move-in homes were averaging 3 to 3.2 per community in Houston against a national average of 2.3, days on market had risen to 44, and new-home prices were about 5% below their peak while still roughly 40% above 2019. Rate buydowns and closing-cost help were everywhere. That’s per {SRC['ci_zonda']}. With that much finished inventory sitting longer, your quick move-in page and the ad budget behind it matter a lot more than they did in 2021.</p>
<p>The master-planned communities set the tone. RCLCO’s 2025 list of the nation’s top-selling MPCs had Sunterra in Katy at No. 5 with 1,024 sales and Tamarron at No. 9 with 974, plus Anniston, The Grand Prairie, Meridiana, Sienna, Elyson, Lago Mar and Jordan Ranch further down, according to {SRC['rclco']}. Bridgeland in Cypress keeps showing up in those rankings too.</p>
<p>North of Houston, the growth is along I-45 and SH 242. {SRC['conroe']} profiled Grand Central Park (Johnson Development, at I-45 and Loop 336), The Woodlands Hills (Howard Hughes), Artavia (planned for more than 6,500 homes), Evergreen from Shea Homes at SH 242 and FM 1314, and Cielo off Airport Road. Add Woodforest in Montgomery and the smaller subdivisions around Magnolia and Willis, and a buyer has a lot of choices within a 20-minute drive.</p>
<!--fig:map-->
<p>For custom builders there’s better news. NAHB counted 186,000 custom home starts nationally in 2025, up 3% while total single-family starts fell more than 6%, and custom work was almost 20% of single-family starts, per {SRC['nahb']}. Buyers with land and equity kept building.</p>
<p>You can’t outspend a 3,000-acre MPC’s lifestyle campaign, and we wouldn’t try. What you can do is pick up the phone on Saturday and put real prices and lot premiums online, next to a quick move-in page that’s accurate as of this morning. Fewer builders manage that than you’d guess.</p>"""),

            ("Community pages, plan pages and quick move-in pages: the builder website that sells", f"""<p>Most builder websites we look at are gorgeous and nearly useless for search. A hero video, community pages full of lifestyle copy, and no price anywhere.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Page type</th><th>What the buyer is asking</th><th>What the page must show</th></tr></thead>
<tbody>
<tr><td>Community page (one per community)</td><td>“Is this area right for us, and can we afford it?”</td><td>Price range “from,” lot sizes, school district, HOA dues, MUD or PID tax rate, model address and hours, drive times to I-45, the Grand Parkway or the Hardy Toll Road</td></tr>
<tr><td>Plan page (one per plan)</td><td>“Does this layout work?”</td><td>Square footage, beds/baths, base price, which communities offer it, floor plan image, video walkthrough, options with typical upgrade costs</td></tr>
<tr><td>Quick move-in page (one per home)</td><td>“What can we close on soon?”</td><td>Address or lot, price, completion date, current incentive with its end date, photos of <i>this</i> house, a “schedule a tour” button</td></tr>
<tr><td>Build-on-your-lot page</td><td>“Will you build on our land in Montgomery County?”</td><td>Areas served, minimum lot requirements, septic/well experience, process and timeline, starting price per square foot range</td></tr>
<tr><td>Area pages (Conroe, Magnolia, Tomball, Willis)</td><td>“New homes in Magnolia under $500K”</td><td>Your communities and inventory in that town, with links down to each</td></tr>
</tbody></table></div>
<p>The MUD tax rate line is a Houston-specific one. Out-of-state buyers from California or the Northeast get blindsided when a MUD tax stacks on top of county, city and school district rates, and builders who explain it up front lose fewer contracts at the option period. We’d rather a buyer learn it from you on page one than from their lender in week three.</p>
<p>Quick move-in pages need to come down (or switch to “Sold”) the day the home goes under contract. Stale inventory burns a lead’s trust and your ad spend at the same time. And each community page should carry the model’s exact address and hours, because “new homes near me” searches pull from Google Maps, and your model or sales office listing is how you show up there. Our team builds these sites under {L('/services/web-design-seo-pr/', 'web design and SEO')}, and the {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} goes deeper on area pages.</p>"""),

            ("Google Ads for “new homes in [community]” searches", f"""<p>Search is where buyers tell you exactly what they want. “New homes in Grand Central Park.” “Quick move in homes Conroe.” “Custom home builder Magnolia TX.” “Build on your own lot Montgomery County.” Each deserves its own ad group and a landing page from the table above.</p>
<p>How we’d structure it for a builder with three communities:</p>
<ul>
<li>One campaign per community, with keywords like the community name plus “new homes,” “homes for sale” and the builder names you compete with there. Send that traffic to the community’s page, never the homepage.</li>
<li>An area campaign for searches like “new construction homes Conroe TX,” “new homes Magnolia” and “new build homes Montgomery TX,” landing on the area page that lists everything you have in that town.</li>
<li><b>Quick move-in.</b> “Move in ready homes,” “quick move in homes,” “spec homes” plus town names. When inventory is high this is often the best-converting campaign you’ll run, and it pays to push it hardest near month-end and quarter-end incentive deadlines.</li>
<li>Custom or build-on-your-lot: “custom home builder [town],” “build on your lot,” and “barndominium builder” only if you actually build them.</li>
<li>Brand. It’s cheap, and it stops a competitor or a listing portal from sitting on top of your own name.</li>
</ul>
<p>Build the negative list on day one. Rent, rental, apartments, “for lease,” jobs, careers, “superintendent,” “floor plans free,” manufactured, mobile, modular (unless you sell them), foreclosure and HUD homes.</p>
<p>Now the policy part. Housing ads in the U.S. fall under Google’s personalized advertising restrictions. You can’t exclude by age, gender or parental status, you can’t target marital status or life events like “recently married,” and ZIP code targeting has to be replaced with city, county or radius targeting, per {SRC['gfaq']}. The rule applies to Search, Display and video. In practice that shifts the targeting work onto keywords and locations, where the intent lives anyway.</p>
<p>If you build inside someone else’s MPC, bid on the community name; just keep other companies’ trademarks out of your ad text. Our {L('/services/search-marketing/', 'search marketing team')} sets these up, and our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} will give you a feel for click costs before you set a budget.</p>"""),

            ("Facebook and Instagram ads for builders: living with the Housing special ad category", f"""<p>Every Meta ad for a home for sale has to run under the Housing special ad category. Builders who skip the declaration get ads rejected, and repeat offenders risk the ad account.</p>
<p>The restrictions, as summarized in {SRC['loomer']}: age is locked to 18 to 65+, gender is locked to all, location targeting must include at least a 15-mile radius around any point you choose, there’s no ZIP code targeting, many detailed targeting options disappear and you can’t exclude any, and lookalike audiences aren’t available. Special Ad Audiences, the old workaround, were discontinued in 2022.</p>
<p>So on Meta, the creative does the targeting. That’s the part most builders get wrong. A pretty drone shot of a community pool reaches everyone within 15 miles, and everyone ignores it. An ad that says “4-bed, 2,450 sq ft, Conroe ISD, from the low $400s, move in by March” finds the right people because the wrong people scroll past.</p>
<p>What tends to work for small builders:</p>
<ul>
<li>Short walkthrough videos of a specific quick move-in home, filmed on a phone, with the price and completion date on screen.</li>
<li>Plan-release and phase-opening announcements with a real date.</li>
<li>Instant forms with two or three qualifying questions (timeline, whether they own a home they need to sell, whether they own land). Higher-intent questions mean fewer leads and better ones.</li>
<li>Retargeting website visitors and video viewers.</li>
</ul>
<p>We’d budget Meta as the warm-up and the reminder, and Google as the closer. If you only have $3,000 a month, the bulk of it belongs on search and quick move-in campaigns. See {L('/services/paid-social-advertising/', 'our paid social service')} if you’d rather hand this part off.</p>"""),

            ("Fair Housing Act rules for builder ads, photos included", f"""<p>The ad platforms enforce their rules with targeting restrictions. Federal law goes further and covers what your ad says and shows, everywhere.</p>
<p>Under {SRC['cfr']}, discriminatory advertising includes using “words, phrases, photographs, illustrations, symbols or forms” that suggest a home is or isn’t available to people because of race, color, religion, sex, handicap, familial status or national origin. It also includes “selecting media or locations for advertising” that deny segments of the market information about housing. Texas has its own Fair Housing Act with the same protected classes, so there’s no relief at the state level.</p>
<p>For builders, the traps are usually small and accidental:</p>
<!--fig:wording-->
<p>Describe the home and the location, and leave the buyer you’re imagining out of the copy. “Walk to the elementary school” describes a fact. “Perfect for young families” describes people, and familial status is protected. If you photograph people for your marketing, use a range of real-looking buyers across all your materials (the same young couple and golden retriever in every shot is its own problem). Put the Equal Housing Opportunity logo or statement on your site, brochures and print ads. And if you sell an active-adult or 55+ section, have your attorney confirm it qualifies for the housing-for-older-persons exemption before your ads say “adult community.”</p>
<p>If a phrase makes you hesitate, cut it. We’re marketers, and that’s the cheapest legal advice we’ve got.</p>"""),

            ("Realtor co-op and broker outreach still matter", f"""<p>A big share of new-home buyers in Houston show up with an agent. Ignoring agents doesn’t save you the commission. It just sends their clients to the builder down the road who treats agents well.</p>
<p>Since the NAR settlement practice changes took effect in August 2024, offers of compensation no longer go on the MLS, and buyers sign written agreements with their agents before touring. Builders still decide their own co-op policy, and agents now ask about it up front. Put yours where agents can find it: a broker page on your website with the co-op terms, the registration rule (most builders require the agent to register the client on the first visit), and a downloadable inventory sheet.</p>
<p>The old-fashioned stuff still works in The Woodlands and Conroe. A quarterly broker lunch at the model still fills chairs. So does a monthly agent email with updated quick move-ins and incentives. Mostly it comes down to knowing, by name, the agents who actually sell your area on HAR. Our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how local agents market themselves')} is worth reading to see the world from their side.</p>"""),

            ("Zillow New Construction, NewHomeSource and the listing sites", f"""<p>Plenty of buyers browse the portals before they ever search a builder name. Two matter most for new construction.</p>
<p><b>Zillow New Construction.</b> Builders can send community and plan data through Zillow’s new home feed, and paid Promoted Communities placement puts your communities in front of shoppers in your area. Per {SRC['zlc']}, spec homes need to be listed in an MLS to appear alongside agent listings, and Listing Connect ties those MLS listings back to your community so leads still route to you. Pricing is negotiated, so get a quote and treat it like any other ad buy.</p>
<p><b>NewHomeSource.</b> The new-construction-only portal run by BDX, which Zonda {SRC['bdx']}. Buyers on it are by definition shopping new, which tends to mean better lead quality and fewer leads.</p>
<p>We wouldn’t pay for both until you can measure one. Run the portal your buyers mention most for a full quarter and judge it on cost per appointment. Cost per lead flatters portals, because their leads are often early-stage and only turn into anything if your follow-up is good.</p>"""),

            ("Tracking model home visits back to the ad", f"""<p>Back to the Saturday-versus-Monday problem. You want every model visit and every contract tied to the first and last place that buyer came from.</p>
<!--fig:tracking-->
<p>A simple version any builder can run:</p>
<ol>
<li>Give each channel its own tracked phone number (Google Ads, Meta, Zillow, NewHomeSource, signs, website) and record calls. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers setup.</li>
<li>Put an appointment scheduler on every community and quick move-in page. A booked tour is the best mid-funnel signal you’ll get.</li>
<li>Register every model visitor on a tablet with name, email, phone, how they heard about you, and whether they have an agent.</li>
<li>Keep every lead and visitor in one CRM with the original source attached. Match walk-ins to earlier online leads by email or phone.</li>
<li>Send appointments, visits and contracts back to Google Ads and Meta as offline conversions, so the platforms learn which clicks turn into buyers.</li>
</ol>
<p>Below is an illustrative monthly funnel for a small builder with two active communities. The numbers aren’t a benchmark, just a picture of what to count and where it lives.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Stage</th><th>What counts</th><th>Where it’s tracked</th><th>Example month</th></tr></thead>
<tbody>
<tr><td>Interest</td><td>Form fills, calls, chats, portal leads</td><td>Ad platforms, call tracking, CRM</td><td>180</td></tr>
<tr><td>Qualified lead</td><td>Real timeline, budget and area fit</td><td>CRM, after first conversation</td><td>60</td></tr>
<tr><td>Appointment</td><td>Booked tour or design meeting</td><td>Scheduler, CRM</td><td>28</td></tr>
<tr><td>Model visit</td><td>Showed up and registered</td><td>Tablet sign-in, CRM</td><td>22</td></tr>
<tr><td>Contract</td><td>Signed purchase or build agreement</td><td>CRM, uploaded to ad platforms</td><td>3</td></tr>
</tbody></table></div>
<p>Once the table is real for three months, budget decisions get easy. If Meta produces lots of leads and no visits, change the creative or the form questions before you kill it.</p>
<p>On spend, plenty of small builders put somewhere around 1% to 2% of revenue into marketing, with more during a community launch. Treat that loosely. The better number is marketing cost per closing, which you can only see once the funnel above is wired up.</p>
<p>If you want a second set of eyes before you spend more, our free Ad Spend Leak Check is a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours. {L('/contact/', 'Request one here')}, and send us your quick move-in page while you’re at it.</p>"""),
        ],
        "faq": [
            ("How do home builders get leads?",
             "Most builder leads come from Google searches for a community or town plus new homes, listing portals like Zillow and NewHomeSource, Facebook and Instagram ads, realtor referrals, and drive-by traffic at the model. The best-performing source is usually search traffic landing on an accurate community or quick move-in page. Track every lead to a model visit and a contract so you know which source actually sells homes."),
            ("How much should a home builder spend on marketing?",
             "Many small builders spend somewhere around 1% to 2% of revenue on marketing, with extra during a community or phase launch. Treat that as a starting point. A better method is to work backward from your closing goal and your measured cost per closing by channel, which only works once appointments, visits and contracts are tracked to their source."),
            ("Can I target by age or ZIP code in Facebook ads for new homes?",
             "No. Meta requires new-home ads to run under the Housing special ad category, which locks age to 18 to 65+, includes all genders, removes ZIP code targeting and requires at least a 15-mile radius. Lookalike audiences are unavailable and detailed targeting is limited. Google has similar housing restrictions on age, gender, parental status and ZIP codes. Write ads specific enough that the right buyers recognize themselves."),
            ("What is the best way to market a custom home builder?",
             "Show finished work and real numbers. A custom builder needs a build-on-your-lot page with areas served and a price-per-square-foot range, a portfolio organized by style and size, strong Google reviews, and search ads for phrases like custom home builder plus a town name. Meta works well for video walkthroughs of finished homes. Respond fast, because custom buyers interview several builders."),
            ("Should a small builder list homes on Zillow and NewHomeSource?",
             "Usually yes, but test one at a time. Zillow reaches the most shoppers, and spec homes must be on the MLS to appear alongside agent listings. NewHomeSource reaches buyers who are only shopping new construction. Run one for a full quarter and judge it by cost per appointment and cost per contract rather than cost per lead, since portal leads are often early in their search."),
        ],
        "figures": {
            "journey": {
                "type": "funnel",
                "title": "A new-home buyer’s long road",
                "stages": [["Picks an area or school district", "Months 1-3"], ["Shortlists communities and builders", "Months 2-5"], ["Gets pre-approved, lists current home", "Months 3-8"], ["Tours models and quick move-ins", "Months 4-9"], ["Signs a contract", "Months 6-12"]],
                "note": "Illustrative example",
                "alt": "Funnel of a typical new home buyer journey in Houston and Montgomery County from choosing an area to signing",
                "caption": "Timelines vary a lot. Plan campaigns for the months between first click and first tour.",
            },
            "map": {
                "type": "map",
                "title": "Where north Houston is building",
                "sub": "Areas with active master-planned communities named in this post",
                "highlight": ["Conroe", "Montgomery", "Willis", "Magnolia", "The Woodlands", "Cypress", "Katy", "Fulshear"],
                "alt": "Map of Greater Houston new home growth areas for home builder marketing, including Conroe, Montgomery and Katy",
                "caption": f"Communities from {SRC['conroe']} and RCLCO’s 2025 rankings.",
            },
            "wording": {
                "type": "compare",
                "title": "Builder ad copy: risky vs. safer",
                "left": {"title": "Describes people (risky)", "items": ["Perfect for young families", "Ideal for empty nesters", "Exclusive, private neighborhood", "Great for professionals", "Every photo shows one type of buyer"]},
                "right": {"title": "Describes the home (safer)", "items": ["4 bedrooms, game room upstairs", "Single-story plan, no stairs", "Gated entry, 2-acre lots", "15 minutes to the Grand Parkway", "Varied, real-looking people across ads"]},
                "alt": "Comparison of risky and safer Fair Housing ad wording for home builder marketing in Houston and Montgomery County",
                "caption": "Describe features, places and facts. When in doubt, cut the phrase.",
            },
            "tracking": {
                "type": "steps",
                "title": "Tie model visits back to ads",
                "sub": "The tracking setup a small builder can run",
                "steps": [["Tracked numbers", "One call tracking number per channel, calls recorded."], ["Online scheduling", "Book-a-tour on every community and inventory page."], ["Model sign-in", "Tablet registration with source and agent question."], ["One CRM", "Every lead and visitor with original source attached."], ["Offline conversions", "Visits and contracts sent back to Google and Meta."]],
                "alt": "Five steps to track model home visits back to Google and Meta ads for a Houston home builder",
                "caption": "Steps four and five are where most small builders stop. They’re worth finishing.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: auto repair
    {
        "slug": "auto-repair-shop-marketing-houston",
        "title": "Auto Repair Shop Marketing in Houston: How to Fill More Bays",
        "seo_title": "Auto Repair Shop Marketing in Houston: Fill More Bays",
        "desc": "Auto repair shop marketing for Houston: Google Business Profile, reviews, Local Services Ads, Google Ads keywords and negatives, pricing, fleets, retention.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google"],
        "art": "b5",
        "hero": "wrench",
        "hero_alt": "Illustration of a wrench for auto repair shop marketing in Houston, The Woodlands and Spring",
        "related": ["rank-in-google-map-pack-houston", "local-services-ads-vs-google-ads-home-services", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Tuesday, 10:40 a.m. Four bays, two of them empty. The phone rings and it’s the third person today asking “how much for brakes?” Your service writer says “depends on the car, bring it in,” and the caller says thanks and hangs up.</p>
<p>That call is most of auto repair shop marketing in one moment.</p>
<p>To get more customers for an auto repair shop in Houston, win the Google Maps results for the services you’re best at and keep a steady stream of honest reviews coming in. Run search ads only on high-intent repair keywords, with hard negatives for DIY, parts and job seekers. Answer the price question better than the shop down the street does.</p>
<p>Then keep the customers you already have coming back, which is cheaper than everything above. Independent shops, tire shops, transmission specialists and collision centers all run on the same engine. The weights change.</p>
<p>Below is how we’d set it up for a shop in Spring, The Woodlands, Cypress or anywhere inside the Beltway, with the actual settings.</p>"""),

            ("Where Houston drivers actually find a mechanic", f"""<p>Nobody browses for a mechanic. Something breaks, a light comes on, or the car makes a new noise on I-45, and the driver searches. “Auto repair near me.” “Brake repair Spring TX.” “Transmission shop Conroe.” The top of that results page is ads, then the map pack, then the websites.</p>
<p>The cars are getting older, which is good for independents. {SRC['spg']} put the average age of U.S. light vehicles at 12.8 years in 2025, with passenger cars at 14.5, across 289 million vehicles on the road, and noted the repair opportunity as vehicles roll off warranty. A 12-year-old Silverado isn’t going back to the dealer for brakes. It’s going to whoever shows up first in Google Maps with good reviews and an open bay.</p>
<p>Location matters more than shops like to admit. Houston drivers drop cars near home or near work, then Uber or get a ride. A shop on FM 1960 or near the SH-249 and Grand Parkway interchange can pull commuters as well as neighbors, and your marketing should say so. “Drop off on your way to the Energy Corridor, we’ll text you photos by lunch.”</p>
<p>So the map pack is the first fight. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the full playbook, and the next two sections are the shop-specific parts.</p>"""),

            ("Google Business Profile categories and services for repair shops", f"""<p>Your primary category is the single strongest setting you control. Pick the one that matches the work you most want.</p>
<ul>
<li>General repair: <b>Auto repair shop</b> as primary.</li>
<li>Specialists: <b>Transmission shop</b>, <b>Brake shop</b>, <b>Tire shop</b>, <b>Auto body shop</b>, <b>Oil change service</b>, <b>Auto air conditioning service</b> or <b>Car battery store</b> as primary when that really is your main business.</li>
<li>Secondary categories: add the other real services you do. A general shop that does a lot of AC work in July should have the AC category. Don’t add categories for work you send out.</li>
</ul>
<p>Then fill in the Services list under each category with plain-English entries and a short description: “Brake pad and rotor replacement, most cars and light trucks, same-day when parts are in stock.” Add your hours accurately, including Saturdays (Saturday is when a lot of commuters can actually drop off). Add the “appointment” link to a real booking page. Upload photos of your bays, your techs at work, your waiting area and your sign from the street, so a first-timer can find the driveway.</p>
<p>Two shop mistakes we see constantly. Hours that say “open 24 hours” because someone hit the wrong button, which sends angry 9 p.m. callers your way. And a profile that lists the owner’s cell number, so every Maps call goes to a phone in a pocket under a car.</p>"""),

            ("Reviews: how to ask without breaking Google’s rules", f"""<p>Reviews win map rankings and they win the phone call. Most shops are terrible at asking.</p>
<p>The rules first, from {SRC['gpol']}: you can’t offer incentives for reviews (no $10 off the next oil change), you can’t discourage negative reviews, and you can’t “selectively solicit positive reviews,” which means no review gating where only happy customers get the link. In April 2026, Google also added language against merchants telling staff to collect a set number of reviews or reviews with specific content, which may include asking customers to name a particular tech, per {SRC['ppcl']}. The scope isn’t fully settled, so we’d stop running “get 10 reviews mentioning your name” contests.</p>
<p>What works and stays inside the lines:</p>
<ol>
<li>Send every customer the same review link by text within an hour of pickup, when the car feels good and the bill is fresh.</li>
<li>Have the service writer mention it at checkout in one sentence. No script, no pressure.</li>
<li>Reply to every review, especially the bad ones, with specifics and an offer to call. Future customers read the reply more closely than the complaint.</li>
<li>Put the link on the invoice and the digital inspection report.</li>
</ol>
<p>Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has templates you can copy.</p>"""),

            ("Local Services Ads for auto repair: what changed in 2026", f"""<p>Local Services Ads are the pay-per-lead boxes at the very top of some searches. For years they were mainly a home services product. Auto is very much in now.</p>
<p>{SRC['lsa']} includes Auto Repair Shop, Auto Body Shop, Auto Glass Repair Service, Brake Shop, Car Battery Store, Car Inspection Service, Oil Change Service, Tire Shop, Transmission Shop, Towing and several more. In August 2026, {SRC['ser']} reported Google split the old generic auto categories into those specific services and introduced “pre-badge” ads that can start serving after preliminary checks while onboarding finishes. Google’s own page notes that the Google Verified badge isn’t available for auto verticals, so auto LSAs run without it.</p>
<p>You pay per lead (a call or message) rather than per click, and you can dispute leads that weren’t real customers. Availability still varies by service and area, so the only way to know for your shop is to start the sign-up and enter your address.</p>
<p>With strong Google reviews, we’d test LSA alongside regular search ads, starting with your most profitable service category. If you have 14 reviews and a 3.9 rating, fix that first. LSA ranking leans hard on reviews and responsiveness. We compare the two ad types in detail in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}; the logic carries over to auto.</p>"""),

            ("Auto repair Google Ads: keywords by service, and the negatives that save you", f"""<p>Generic “auto repair” keywords are expensive and mixed-intent. Service keywords are where the money is, because the searcher has already told you what’s wrong.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Service</th><th>Example keywords</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Brakes</td><td>brake repair near me, brake pad replacement Spring TX, grinding brakes</td><td>High volume, price-shopped. Show a starting price.</td></tr>
<tr><td>Check engine / diagnostics</td><td>check engine light diagnosis, car diagnostic near me</td><td>State your diagnostic fee and if it’s credited to the repair.</td></tr>
<tr><td>AC</td><td>car ac repair Houston, car ac blowing hot air</td><td>Raise budget May through September.</td></tr>
<tr><td>Transmission</td><td>transmission repair Conroe, transmission slipping, transmission shop near me</td><td>High ticket. Calls matter more than forms.</td></tr>
<tr><td>Batteries and electrical</td><td>car battery replacement near me, car won’t start</td><td>Urgent intent. Call-focused ads with hours scheduling.</td></tr>
<tr><td>Tires and alignment</td><td>tires near me, wheel alignment The Woodlands</td><td>Competes with big-box tire chains; lean on speed and service.</td></tr>
<tr><td>Collision</td><td>auto body shop near me, collision repair Katy, insurance claim body shop</td><td>Mention insurance work and rental coordination.</td></tr>
</tbody></table></div>
<p>The negatives are where most shop accounts leak. Start with these and add from your search terms report every week for the first month:</p>
<!--fig:negatives-->
<p>A few settings that matter for a repair shop. Use “Presence: People in or regularly in your included locations” rather than the default that includes people merely interested in your area. Draw your radius around how far people will actually drive a broken car, usually tighter than you think. Schedule call assets only for hours when someone answers. And track calls as conversions, because most repair customers call. Our {L('/services/search-marketing/', 'Google Ads management')} handles this for shops that don’t want to live in the search terms report.</p>"""),

            ("The “how much for brakes?” problem: pricing and estimates", f"""<p>Back to Tuesday’s phone call. Every shop knows you can’t quote a brake job blind. Every customer knows “bring it in” sometimes means “we’ll find $1,400 of other stuff.” The shop that wins is the one that closes that trust gap.</p>
<!--fig:pricing-->
<p>Practical version:</p>
<ul>
<li>Publish “starting at” prices online for routine work: oil change by oil type, front brake pads per axle, battery installed, alignment, diagnostic fee. Add “most cars and light trucks, parts vary by vehicle.” A range is far better than nothing.</li>
<li>Say plainly whether the diagnostic fee is credited toward the repair if they approve it. Many callers are really asking “will I pay you just to tell me what’s wrong?”</li>
<li>Send a digital inspection with photos and short notes by text before you ask for approval. A photo of a worn pad next to a new one sells the job honestly.</li>
<li>Split the estimate into “do now,” “soon” and “watch.” It cuts the feeling of being upsold, and the “soon” list becomes your follow-up marketing.</li>
<li>Train whoever answers the phone to give the range and then ask for the appointment.</li>
</ul>
<p>Shops worry that showing prices invites shoppers. Some of them will shop. But a page that answers the price question also gets more calls from the people who just wanted a straight answer, and your ads will convert better because the landing page matches the search.</p>"""),

            ("Texas inspection changes, Houston heat and the seasons that drive repair demand", f"""<p>For decades, the annual safety inspection sent a stream of cars into shops, and a good writer could turn a sticker visit into a brake job. That changed. Under House Bill 3297, Texas ended the safety inspection program for non-commercial vehicles on January 1, 2025, per {SRC['txdmv']}. Drivers now pay a $7.50 Inspection Program Replacement Fee at registration instead ($16.75 for a new vehicle, covering two years).</p>
<!--fig:texas-->
<p>Emissions testing didn’t go away. It’s still required before registration in 17 counties, including Harris, Montgomery, Fort Bend, Brazoria and Galveston. So if you’re a certified emissions station in the Houston area, those visits continue; the bundled safety check doesn’t. And the repeal covered non-commercial vehicles only, so check with DPS on what still applies to commercial vehicles you service.</p>
<p>So replace the lost touchpoint on purpose. A free courtesy inspection with any oil change does most of the work. A pre-road-trip check promoted before Thanksgiving and spring break helps too, and the emissions visit deserves a digital inspection report like any other service.</p>
<p>Then plan around Houston’s seasons. The July and August heat is hard on batteries and AC systems; one Houston shop owner {SRC['abc13']} in 2023 that local heat can cut a battery’s expected life by about a third. Push AC and battery campaigns in late spring, before the first heat wave. Wait until everyone’s stranded and you’re bidding against every shop in town. Hurricane season runs June 1 to November 30, so if you do flood or storm damage work, have that page and ad group ready to switch on the same afternoon.</p>"""),

            ("Fleet and commercial accounts: steady work between walk-ins", f"""<p>A walk-in customer might visit twice a year. A plumbing company with 12 vans might bring you a vehicle every week. North Houston is full of service fleets (HVAC, plumbing, pest control, landscaping, electrical), plus oilfield service trucks, delivery vans and church and school buses.</p>
<p>Fleet work comes from outreach and decent terms. Ads barely figure in.</p>
<ol>
<li>Build a fleet page: services, turnaround promise, pickup and delivery, monthly invoicing, and who to call.</li>
<li>Make a list of 40 local fleets within five miles. Drive the lot after hours if you have to, then ask for the operations manager rather than the owner.</li>
<li>Offer a first-vehicle inspection at no charge and a written priority-bay policy.</li>
<li>Report by vehicle each month (mileage, work done, what’s coming due). Fleet managers stay where the paperwork is easy.</li>
</ol>
<p>Many of those fleets are businesses we work with on the other side, so we see what they care about: downtime. If you can say “van in at 7, back by 3 or we tell you by 10 a.m.,” you have a pitch. Our {L('/industries/service/', 'home services industry page')} shows the kinds of companies that run these fleets.</p>"""),

            ("Retention: service reminders, texts and consent", f"""<p>The cheapest car to fill a bay is one that’s already been in your bay. Retention is where shops make their margin, and it’s mostly automation your shop management software already supports.</p>
<ul>
<li>Service reminders by mileage or date for oil changes, tire rotations and the “soon” items from the last inspection.</li>
<li><b>Declined-work follow-up</b> at 30 and 90 days, with the inspection photo attached. This one pays for the software by itself in most shops we’ve seen.</li>
<li>A once-a-month email with something useful, like an AC check before summer or a hurricane-season prep list. Nobody misses another coupon blast.</li>
</ul>
<p>Texting needs care. Service updates about a car the customer just dropped off are different from marketing texts. Get clear opt-in for marketing messages, separate from the service-update consent, and keep the record. Texas also brought marketing texts under its telephone solicitation law through SB 140, effective September 1, 2025, with a registration requirement and a private right of action for violations, though there are exemptions (including some tied to current or former customers and businesses that mostly sell from a physical location), per {SRC['sb140']}. Ask your attorney which applies to your shop before you start a promo text program.</p>
<p>Our {L('/blog/email-marketing-basics/', 'email marketing basics')} post covers list building if you’re starting from zero.</p>"""),

            ("What a Houston repair shop should spend on marketing", f"""<p>There’s no honest single number. For a single-location independent shop with four to eight bays, this is an illustrative starting point. Treat the ranges as examples; they aren’t quotes or benchmarks.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>Google Ads (search, call-focused)</td><td>$1,000 to $2,500</td><td>Service keyword campaigns in a tight radius</td></tr>
<tr><td>Local Services Ads</td><td>$500 to $1,500</td><td>Pay-per-lead tests in one or two categories</td></tr>
<tr><td>Local SEO and Business Profile work</td><td>$500 to $1,500</td><td>Service pages, photos, posts, review replies</td></tr>
<tr><td>Review and reminder software</td><td>$100 to $400</td><td>Review texts, reminders, declined-work follow-up</td></tr>
<tr><td>Fleet outreach materials</td><td>$0 to $300</td><td>Fleet page, a one-pager, a lunch or two</td></tr>
</tbody></table></div>
<!--fig:budget-->
<p>Start with the profile, reviews and retention, because they cost the least and pay back the fastest. Add paid search once your landing pages show prices and your phone is answered every time. Then test LSA. Shops that start with a big ad budget and a 3.9-star profile usually just pay more to lose the call.</p>
<p>If you’re already spending and not sure it’s working, our free Ad Spend Leak Check is a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours. {L('/contact/', 'Ask for one here')}. And if you also run detail bays, our {L('/blog/auto-detailing-marketing-the-woodlands-houston/', 'auto detailing marketing post')} covers that side.</p>"""),
        ],
        "faq": [
            ("How do I get more customers for my auto repair shop?",
             "Start with your Google Business Profile: the right primary category, accurate hours, real photos and a steady flow of reviews requested by text after pickup. Then add search ads on specific service keywords like brake repair or transmission repair near your shop, with negatives for DIY, parts and jobs. Publish starting prices for routine work, and use service reminders to bring past customers back."),
            ("Are Google Local Services Ads available for auto repair?",
             "Yes. Google’s Local Services Ads list now includes Auto Repair Shop, Brake Shop, Transmission Shop, Tire Shop, Oil Change Service, Auto Body Shop and other auto categories, and Google split the old generic auto categories into specific services in 2026. Availability varies by area and service, and the Google Verified badge isn’t offered for auto verticals. Start the sign-up with your address to check your shop."),
            ("What keywords should an auto repair shop use in Google Ads?",
             "Bid on specific services with local or near-me terms, such as brake repair near me, check engine light diagnosis, car AC repair Houston or transmission shop Conroe. These convert better than broad auto repair keywords. Add negative keywords for DIY searches (how to, YouTube, manual), parts shoppers (parts, AutoZone, junkyard) and job seekers (jobs, hiring, salary), and review the search terms report weekly."),
            ("Does Texas still require vehicle inspections?",
             "Texas ended safety inspections for non-commercial vehicles on January 1, 2025, and drivers now pay a $7.50 Inspection Program Replacement Fee at registration. Emissions testing is still required in 17 counties, including Harris, Montgomery, Fort Bend, Brazoria and Galveston. Commercial vehicles were not part of that repeal, so shops should check current DPS rules for commercial inspections."),
            ("Can I offer a discount for Google reviews at my shop?",
             "No. Google’s policy prohibits offering discounts, free services or payment in exchange for reviews, and it also bans discouraging negative reviews or only asking happy customers. Since April 2026 Google also discourages telling staff to collect a set number of reviews or reviews with specific content. Send every customer the same review link after pickup and reply to every review instead."),
        ],
        "figures": {
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for repair shops",
                "sub": "Add these before you spend a dollar",
                "items": ["DIY: how to, diy, yourself, youtube, video", "Manuals: manual, diagram, wiring, torque specs", "Parts: parts, autozone, o’reilly, part number", "Salvage: junkyard, pick and pull, used engine", "Jobs: jobs, hiring, salary, mechanic school", "Free: free, cheap only if you don’t sell on price", "Wrong service: mobile mechanic if you aren’t mobile", "Dealers: dealership names you can’t service"],
                "alt": "Checklist of negative keywords for auto repair Google Ads in Houston, covering DIY, parts, jobs and salvage searches",
                "caption": "Then read your search terms report weekly and keep adding.",
            },
            "pricing": {
                "type": "compare",
                "title": "Answering “how much for brakes?”",
                "left": {"title": "The usual answer", "items": ["“Depends, bring it in”", "No prices anywhere online", "Diagnostic fee mentioned at checkout", "Approval call with no photos", "One big total on the estimate"]},
                "right": {"title": "The answer that books cars", "items": ["A starting range, then an appointment", "Starting-at prices on service pages", "Diagnostic fee and credit stated up front", "Digital inspection photos by text", "Do now, soon and watch, itemized"]},
                "alt": "Comparison of how Houston auto repair shops answer price questions, from vague quotes to transparent starting prices",
                "caption": "Transparency costs you a few shoppers and wins you a lot more callers.",
            },
            "texas": {
                "type": "stats",
                "title": "Texas inspection and the aging fleet",
                "stats": [["17", "counties still require emissions tests"], ["$7.50", "yearly replacement fee at registration"], ["2025", "safety inspections ended Jan 1"], ["12.8", "years, average U.S. vehicle age"]],
                "note": "Source: TxDMV, S&P Global Mobility",
                "alt": "Stats on Texas vehicle inspection changes and average vehicle age that affect Houston auto repair shop marketing",
                "caption": f"From {SRC['txdmv']} and {SRC['spg']}.",
            },
            "budget": {
                "type": "bars",
                "title": "Example monthly marketing mix",
                "sub": "Single-location shop, midpoint of each range",
                "items": [["Google Ads", 1750, "$1,750"], ["Local Services Ads", 1000, "$1,000"], ["Local SEO and profile", 1000, "$1,000"], ["Reviews and reminders", 250, "$250"], ["Fleet outreach", 150, "$150"]],
                "highlight": [0],
                "note": "Illustrative ranges",
                "alt": "Bar chart of an example monthly marketing budget for an auto repair shop in Houston across ads, SEO and retention",
                "caption": "Midpoints of the illustrative ranges in the table above. Your mix should follow your tracked results.",
            },
        },
    },
]
