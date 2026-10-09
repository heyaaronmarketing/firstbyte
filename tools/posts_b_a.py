"""Two home-services posts: HVAC marketing in Houston / The Woodlands and roofing marketing for storm season.

Research: search phrasing for "hvac marketing houston", "how to get more hvac leads", "roofing leads houston",
"how to get roofing leads after a storm"; facts verified against NWS Houston/Galveston climate summaries,
ABC13 (Beryl outages), NOAA NHC, IBHS hail data (via Roofing Contractor), TDI, CBS Texas, TDLR rule 16 TAC 75.71
(Cornell LII), Google Ads / Business Profile help pages, Search Engine Roundtable, WordStream 2026 benchmarks,
BrightLocal 2026 review survey, ENERGY STAR, and Jon Loomer's summary of Meta's Special Ad Categories.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "nws23": A("https://www.weather.gov/media/hgx/climate/summary/Top%20Weather%20Events%202023.pdf", "National Weather Service Houston/Galveston"),
    "beryl": A("https://abc13.com/post/centerpoint-energy-customers-grow-frustrated-no-power/15049540/", "ABC13"),
    "lsa": A("https://support.google.com/google-ads/answer/6224841", "Google’s Local Services Ads help page"),
    "verified": A("https://seroundtable.com/google-verified-local-service-ads-badge-39975.html", "Search Engine Roundtable"),
    "wordstream": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream/LocaliQ’s 2026 benchmarks"),
    "brightlocal": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "energystar": A("https://www.energystar.gov/saveathome/heating-cooling/maintenance-checklist", "ENERGY STAR"),
    "tdlr": A("https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-75-71", "TDLR rule 16 TAC §75.71"),
    "gbpsab": A("https://support.google.com/business/answer/9157481", "Google’s service-area guidelines"),
    "metasac": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Meta’s Housing special ad category"),
    "ibhs": A("https://www.roofingcontractor.com/articles/100873-texas-remains-no-1-for-most-major-hail-events", "IBHS data reported by Roofing Contractor"),
    "nhc": A("https://www.nhc.noaa.gov/climo/", "NOAA’s National Hurricane Center"),
    "derecho": A("https://weather.gov/media/hgx/climate/summary/May_2024_Regional_Climate_Summary.pdf", "NWS Houston/Galveston’s May 2024 summary"),
    "tdi": A("https://www.tdi.texas.gov/consumer/storms/roofing-and-insurance-know-the-law.html", "Texas Department of Insurance"),
    "cbs": A("https://www.cbsnews.com/texas/news/how-to-hire-a-reputable-roofer-in-texas-and-why-its-so-easy-to-get-scammed/", "CBS Texas"),
    "ghousing": A("https://support.google.com/adspolicy/answer/16701755?hl=en", "Google’s housing ad policy"),
}

POSTS = [
    # ------------------------------------------------------------------------------------------ HVAC
    {
        "slug": "hvac-marketing-houston-the-woodlands",
        "title": "HVAC Marketing in Houston & The Woodlands: More Calls, All Year",
        "seo_title": "HVAC Marketing Houston & The Woodlands",
        "desc": "HVAC marketing for Houston and The Woodlands: Local Services Ads vs Google Ads, service-area pages, call tracking and how to stay busy outside of summer.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b3",
        "hero": "hvac",
        "hero_alt": "Illustration of an air conditioning condenser unit for an HVAC marketing guide for Houston and The Woodlands",
        "related": ["local-services-ads-vs-google-ads-home-services", "call-tracking-which-ads-make-phone-ring", "seasonal-marketing-greater-houston"],
        "sections": [
            (None, f"""<p>In July your phones ring off the hook and you’re turning down jobs. In November the techs are sitting in the shop, and you’re wondering why the same ads that worked in summer have gone quiet.</p>
<p>Cooling demand around Houston is enormous and badly lumpy, and most of the HVAC marketing plans we audit were built for August and nothing else. Below is how we’d set things up for a shop in The Woodlands, Spring, Conroe or anywhere else in Greater Houston: where the leads come from, which ones are worth paying for, and how to keep trucks rolling when it’s 65 degrees outside.</p>"""),
            ("Why HVAC marketing in Houston runs on the weather", f"""<p>Houston summers are getting harder on equipment and on homeowners. In 2023, Houston-Hobby logged 18 consecutive days at 100 degrees or hotter, a new record, and Houston had its hottest summer on record, according to the {SRC['nws23']}. When a system fails in that kind of heat, nobody shops around for a week. They call whoever shows up first and looks trustworthy.</p>
<p>Then there are the outage events. After Hurricane Beryl in July 2024, CenterPoint reported 2.26 million customers affected, the largest outage in its history, per {SRC['beryl']}. Equipment that sits through days of heat and then a power surge doesn’t always come back quietly, so the calls don’t stop when the lights come back on. The shops with ads, a Business Profile update and somebody on the phones ready to go were the ones booking that work. Pausing ads during a storm to “save money” mostly hands those calls to a competitor.</p>
<p>So the calendar looks roughly like this for a typical cooling-heavy shop north of Houston:</p>
<!--fig:season-->
<p>Everybody sees the summer peak. Fewer shops plan for the two shoulders, spring tune-ups in March and April and fall heating checks in October and November, and plenty of competitors cut their budgets in exactly those months. Clicks get cheaper and the people searching are easier to book.</p>"""),
            ("Google Local Services Ads vs Google Search ads for HVAC", f"""<p>Most HVAC owners we talk to ask the same thing first: should I run Local Services Ads, regular Google Ads, or both? For most shops in Houston, the answer is both, with different jobs.</p>
<p>Local Services Ads (LSA) sit at the very top of the page for searches like “ac repair near me” or “hvac company spring tx.” You pay per lead, not per click, and Google says you pay “only for leads related to your business and the services you offer” ({SRC['lsa']}). Since October 20, 2025, the old Google Guaranteed and Google Screened badges have been folded into a single <b>Google Verified</b> badge, according to {SRC['verified']}. Google also says your ranking can suffer if you regularly miss calls or messages, which matters a lot in July when the office is slammed.</p>
<p>Search ads are the regular text ads under the LSA box. You pay per click, and you control far more: keywords, ad copy, landing pages, schedules and bids by location. For the home and home improvement category, {SRC['wordstream']} put the average cost per click at $8.33 and the average cost per lead at $90.92. Emergency AC terms in Houston in August will often run higher than that average.</p>
<div class="bp-tbl"><table><thead><tr><th></th><th>Local Services Ads</th><th>Google Search ads</th></tr></thead><tbody>
<tr><td>You pay for</td><td>A lead (call or message)</td><td>A click</td></tr>
<tr><td>Control over targeting</td><td>Job types and service area</td><td>Keywords, ZIP codes, schedule, devices, bids</td></tr>
<tr><td>Ranking depends on</td><td>Responsiveness, reviews, profile</td><td>Bid, ad quality, landing page</td></tr>
<tr><td>Best for</td><td>Repair and “near me” calls</td><td>Replacements, maintenance plans, financing, specific brands</td></tr>
<tr><td>Weak spot</td><td>Little control over lead quality</td><td>Wasted spend without tight negative keywords</td></tr>
</tbody></table></div>
<p>Our take: start LSA first if you can answer the phone fast, then build Search campaigns for the higher-ticket work LSA doesn’t sort well, like full system replacements. We go deeper on the trade-offs in <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs Google Ads for home services</a>.</p>
<h3>Five Search ads settings we check on every HVAC account</h3>
<ol><li><b>Location options:</b> set to “Presence: people in or regularly in your included locations.” The default lets people who are merely interested in Houston see your ads, which can mean clicks from out of state.</li>
<li><b>Separate campaigns for repair and replacement.</b> A $9,000 system and a $189 service call shouldn’t share a budget.</li>
<li><b>Negative keywords:</b> “jobs,” “salary,” “school,” “certification,” “parts,” “Home Depot,” “DIY.” HVAC attracts a lot of job seekers and tinkerers.</li>
<li><b>Call conversions with a minimum length.</b> Count a call from an ad as a conversion only after 60 seconds or so, so hang-ups and wrong numbers don’t teach Google to buy more of them.</li>
<li><b>Ad schedule that matches your phones.</b> If nobody answers after 7 p.m., either staff an after-hours line or pull back bids at night.</li></ol>"""),
            ("Google Business Profile: the free listing that books the most calls", f"""<p>For “ac repair near me” searches, your Business Profile in the map pack often gets more calls than any ad. It’s free, and most HVAC profiles we see are half-finished.</p>
<p>If you don’t serve customers at your shop, Google says to remove the address and list a service area instead. You can list up to 20 service areas, and the total area shouldn’t reach more than about two hours of driving from your base, per {SRC['gbpsab']}. For a shop off I-45 near The Woodlands, that easily covers Spring, Conroe, Tomball, Magnolia, Montgomery, Kingwood and Humble.</p>
<ul><li>Pick “HVAC contractor” or “Air conditioning contractor” as the primary category based on what you want to rank for most, then add the others as secondary categories.</li>
<li>Fill in every service, with a short description: AC repair, heat pump installation, duct cleaning, indoor air quality, furnace repair.</li>
<li>Post photos weekly. Real trucks, real techs, real installs in real neighborhoods. Stock photos don’t help anyone.</li>
<li>Turn on messaging only if someone will reply within the hour.</li>
<li>Answer the questions homeowners actually ask: do you charge a trip fee, do you offer financing, do you service Trane or Carrier.</li></ul>
<p>Our <a href="/blog/rank-in-google-map-pack-houston/">map pack guide for Houston</a> walks through the rest.</p>"""),
            ("Service-area pages for Spring, Conroe, Tomball, Katy and the rest", f"""<p>Your Business Profile can show a service area, but your website has to prove you work there. That means a real page for each city or area you want calls from, and not a copy-pasted page with the city name swapped.</p>
<!--fig:areas-->
<p>A strong service-area page for HVAC includes:</p>
<ul><li>The neighborhoods and roads you actually cover. For Spring that might be Gleannloch Farms, Champion Forest and the FM 2920 corridor; for Conroe, the areas off Loop 336 and around Lake Conroe.</li>
<li>Something true and local: older homes in that area with systems old enough to still run on R-22, two-story homes with upstairs rooms that won’t cool, attic installs in Tomball.</li>
<li>Photos from jobs in that city, with a sentence about the job.</li>
<li>Reviews from customers in that city.</li>
<li>Your phone number at the top and a short booking form. No one scrolls to the bottom of a page in July.</li></ul>
<p>Also, Texas requires your license number in your advertising. {SRC['tdlr']} says advertising “designed to solicit air conditioning or refrigeration business must include the affiliated licensee’s license number,” and it must appear on both sides of your trucks. Put it in the site footer, on landing pages and in your ad creative where it fits. It also happens to build trust.</p>
<p>If your site can’t support pages like this, that’s usually where we start. See our <a href="/services/web-design-seo-pr/">web design and SEO services</a> and <a href="/blog/power-of-local-landing-pages/">why local landing pages matter</a>.</p>"""),
            ("Call tracking: know which ads make the phone ring", f"""<p>HVAC is a phone business. If you can’t tie each call to the ad, listing or page that produced it, you’re budgeting by gut.</p>
<p>The setup we use for most service shops:</p>
<ol><li>A unique tracking number for Google Ads, one for the Business Profile (the tracking number as the primary number and your main line listed as an additional number, so your listings stay consistent), one for Meta and one for any truck wraps, mailers or radio.</li>
<li>Dynamic number swapping on the website, so a visitor from a Google ad sees a different number than someone who typed in your URL.</li>
<li>Call recording, with a disclosure message.</li>
<li>A weekly listen to 10 random calls. You’ll learn more about your marketing in 30 minutes than from any dashboard: missed calls, “we don’t do that” calls, CSRs who never ask for the appointment.</li>
<li>Booked jobs and revenue fed back from your field software (ServiceTitan, Housecall Pro, Jobber) so you can see cost per booked job, not just cost per call.</li></ol>
<p>Skip that last step and Google will happily optimize for the wrong calls. A $60 lead that books a $12,000 replacement is cheap. A $25 lead that turns into a free estimate for someone price-shopping three companies isn’t. More detail in <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking: which ads make the phone ring</a>.</p>"""),
            ("How to budget HVAC ads across Houston’s seasons", f"""<p>Most HVAC ad budgets are flat: the same monthly number all year. That’s backwards in Houston. You want to spend heavy when demand peaks and keep a steady floor in the shoulder months so you don’t lose your position.</p>
<p>Here’s an example of how a shop spending about $60,000 a year on Google might split it. These are illustrative numbers, not a rule, and your mix will shift with your crew size and close rate.</p>
<div class="bp-tbl"><table><thead><tr><th>Period</th><th>Share of annual budget</th><th>Monthly at $60k/year</th><th>Main focus</th></tr></thead><tbody>
<tr><td>Jan–Feb</td><td>10%</td><td>$3,000</td><td>Heating repair, freeze prep, replacements</td></tr>
<tr><td>Mar–Apr</td><td>14%</td><td>$4,200</td><td>AC tune-ups, maintenance plan sign-ups</td></tr>
<tr><td>May–Sep</td><td>58%</td><td>$6,960</td><td>Emergency AC repair, replacements, financing</td></tr>
<tr><td>Oct–Nov</td><td>12%</td><td>$3,600</td><td>Heating tune-ups, IAQ, replacement offers</td></tr>
<tr><td>Dec</td><td>6%</td><td>$3,600</td><td>Heating calls, year-end financing offers</td></tr>
</tbody></table></div>
<p>Two practical notes. First, raise budgets ahead of the forecast, not after. When the extended forecast shows a heat wave, increase Search budgets two or three days early. Second, never go dark during a storm. During outages, people search on their phones. Have a short storm message ready for your Business Profile and ads (“Power back on and AC not cooling? We’re running calls in Spring and The Woodlands today.”).</p>
<p>If you’re unsure what a reasonable spend looks like, our post on <a href="/blog/google-ads-cost-per-click-houston-benchmarks/">Google Ads costs in Houston</a> has more benchmarks.</p>"""),
            ("Keep the phones busy in the shoulder months", f"""<p>From October through April the repair calls thin out, but the work doesn’t vanish. Most of it is sitting in your own customer list, waiting for someone to ask.</p>
<!--fig:shoulder-->
<p><b>Maintenance plans.</b> {SRC['energystar']} recommends annual pre-season check-ups, with the cooling system checked in spring and the heating system in the fall. That’s a ready-made pitch. A plan with two visits a year gives you a reason to contact every member twice, and it fills your schedule with paid work when repair calls are slow. Promote the plan on your site, in every invoice email, and in a small Google Search campaign targeting “ac maintenance plan” and “hvac tune up near me.”</p>
<p><b>Heating tune-ups.</b> Houston doesn’t think about heat until the first cold front. People here still remember February 2021 and Winter Storm Uri. A November email and text to past customers (“Get your heat checked before the first freeze”) costs almost nothing.</p>
<p><b>Indoor air quality.</b> Humidity, allergies and post-flood concerns are real here. IAQ offers (whole-home dehumidifiers, filtration, duct cleaning) work well in Meta ads because people don’t search for them until they’re told they exist.</p>
<p><b>Replacement and financing offers.</b> Fall and winter are the best time to sell a replacement to someone whose system barely survived August. Use your service records: every customer with a system over 12 years old and a repair this summer is a lead.</p>
<p>One Meta detail to know: {SRC['metasac']} lists housing repairs among its examples, and HVAC ads can land in that category. When they do, you can’t target by ZIP code or narrow age, and location targeting needs at least a 15-mile radius. Write the creative so it names the area and the problem, because the targeting can’t do that work for you. If you’d rather not argue with Ads Manager over the category, our <a href="/services/paid-social-advertising/">paid social team</a> can set it up.</p>"""),
            ("Reviews and retargeting: winning the second look", f"""<p>Homeowners rarely book the first HVAC company they see. They check reviews, maybe a second company, maybe your website. Two things win that moment.</p>
<!--fig:reviews-->
<p><b>Reviews.</b> According to {SRC['brightlocal']}, 74% of consumers only consider reviews from the last three months, 47% won’t use a business with fewer than 20 reviews, and 80% are more likely to use a business that responds to all of its reviews. For HVAC, that means a steady flow, not a burst. Have techs ask at the end of every job, then send a text with the review link within an hour. Reply to every review, and mention the city and service in your reply when it’s natural. Our <a href="/blog/complete-guide-google-reviews/">complete guide to Google reviews</a> covers the details.</p>
<p><b>Retargeting.</b> Replacements take days or weeks to decide. Show people who visited your replacement or financing pages short videos of your techs, a financing offer and a few reviews on Meta and YouTube for 30 days. Keep the frequency modest. The goal is to be the name they remember when they’re ready, not to follow them around the internet. See <a href="/blog/retargeting-explained/">retargeting explained</a>.</p>"""),
            ("Start with last year’s call log", f"""<p>Pull last year’s call log and booked jobs by month and set them next to what you spent on ads each month. If spend stayed flat while calls spiked in July and fell off a cliff in November, you have a budget-timing problem, and no new ad copy will fix it. Mark the three slowest months and decide now what offer you’ll run in each.</p>
<p>If you want someone outside the shop to look at the accounts too, send us a request for the free <a href="/contact/">Ad Spend Leak Check</a>. Within 48 hours you’ll get a 10-minute recorded walkthrough of your Google or Meta account with the leaks called out, things like out-of-area clicks, junk search terms and calls counted twice. More on how we work with <a href="/industries/service/">home service companies</a> and on our <a href="/services/search-marketing/">Google Ads management</a> if you want to read first.</p>"""),
        ],
        "faq": [
            ("How do I get more HVAC leads in Houston?",
             "Start with a complete Google Business Profile and a steady stream of recent reviews, then add Local Services Ads for repair calls and Google Search ads for replacements and maintenance plans. Build a page for each city you serve, track every call, and keep spending in the spring and fall shoulder months instead of only in summer."),
            ("Are Google Local Services Ads worth it for HVAC companies?",
             "For most Houston HVAC companies, yes, as long as someone answers the phone quickly. You pay per lead rather than per click, and the ads show above regular search ads. The trade-off is limited control over lead quality, so pair LSA with regular Search campaigns and mark bad leads in your account."),
            ("How much should an HVAC company spend on Google Ads?",
             "It depends on your crew size, close rate and average ticket. As a reference, WordStream and LocaliQ put the 2026 average cost per lead for home and home improvement at about $91. Many Houston shops spend several thousand dollars a month, with the largest share from May through September and a steady floor the rest of the year."),
            ("What is the best time of year to market an HVAC business in Texas?",
             "Peak demand in Houston runs May through September, so that is when ads need the most budget. The best return often comes in March and April for AC tune-ups and October and November for heating checks, when competition is lighter and maintenance plans are easier to sell."),
            ("Does an HVAC company need its license number in ads in Texas?",
             "Yes. TDLR rules say advertising designed to solicit air conditioning or refrigeration business must include the affiliated licensee's license number, with a few exceptions such as nationally placed TV and small promotional items. The number must also be on both sides of service vehicles in letters at least two inches high."),
        ],
        "figures": {
            "season": {
                "type": "columns",
                "title": "HVAC call volume by month, north Houston",
                "sub": "Relative demand for a cooling-heavy shop (peak month = 100)",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [38, 35, 42, 52, 72, 90, 100, 98, 78, 50, 40, 36],
                "highlight": [5, 6, 7],
                "y_label": "Relative calls",
                "note": "Illustrative example",
                "alt": "Column chart of HVAC call volume by month in Houston, peaking in July and August",
                "caption": "Houston HVAC demand is heavy May through September; the shoulder months are where planning pays off.",
            },
            "areas": {
                "type": "map",
                "title": "One profile, many service-area pages",
                "sub": "A shop based in The Woodlands can reasonably cover all of these",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Magnolia", "Kingwood", "Humble", "Cypress", "Katy"],
                "alt": "Map of Greater Houston highlighting HVAC service areas from The Woodlands to Spring, Conroe, Tomball and Katy",
                "caption": "Google allows up to 20 service areas within about two hours of driving from your base.",
            },
            "shoulder": {
                "type": "checklist",
                "title": "Shoulder-month HVAC offers that fill the schedule",
                "sub": "October through April, when repair calls slow down",
                "items": [
                    "Spring AC tune-up campaign to past customers",
                    "Maintenance plan with two visits a year",
                    "First-cold-front heating check email and text",
                    "Indoor air quality and dehumidifier offers on Meta",
                    "Replacement offers for systems over 12 years old",
                    "Financing promos on replacement landing pages",
                    "Duct cleaning and attic insulation add-ons",
                ],
                "alt": "Checklist of shoulder-month HVAC marketing offers for Houston companies, from tune-ups to financing",
                "caption": "Every item here uses customers and service records you already have.",
            },
            "reviews": {
                "type": "stats",
                "title": "What homeowners look for in reviews",
                "stats": [["74%", "only consider reviews from the last three months"],
                          ["47%", "won’t use a business with fewer than 20 reviews"],
                          ["80%", "prefer a business that responds to all reviews"]],
                "note": "Source: BrightLocal Local Consumer Review Survey 2026",
                "alt": "Stat tiles on review recency, review count and owner responses for HVAC companies in Houston",
                "caption": "Recent, frequent reviews matter more than a big total from years ago.",
            },
        },
    },
    # ------------------------------------------------------------------------------------------ ROOFING
    {
        "slug": "roofing-marketing-houston-storm-season",
        "title": "Roofing Marketing in Houston: How to Win Leads After a Storm",
        "seo_title": "Roofing Marketing Houston: Storm Season Leads",
        "desc": "Roofing marketing for Houston and The Woodlands: the 72 hours after hail or a hurricane, Google LSA, Meta rules, reviews and beating storm chasers.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Facebook", "Nextdoor"],
        "art": "b4",
        "hero": "roof",
        "hero_alt": "Illustration of a residential roof for a roofing marketing guide for Houston storm season",
        "related": ["local-seo-contractors-houston", "local-services-ads-vs-google-ads-home-services", "geo-fencing-ads-target-customers-nearby"],
        "sections": [
            (None, f"""<p>A hail cell crosses Tomball at 4 p.m. By 7 p.m. there are out-of-state trucks in the neighborhood, door hangers on every handle, and your phone hasn’t rung once.</p>
<p>Some version of that story comes up with almost every local roofer we sit down with. The storm creates the demand, the leads go to whoever is loudest in the first few days, and homeowners trust all of them a little less each season. What follows is how a roofing company based in The Woodlands, Spring, Conroe, Katy or anywhere else around Houston can be set up before the hail, win the three days after it, and keep retail jobs coming in the long quiet stretches between storms.</p>"""),
            ("Why roofing marketing in Houston is a storm business", f"""<p>Texas leads the country in hail. Using Storm Prediction Center data, the Insurance Institute for Business &amp; Home Safety counted 1,123 major hail events (hailstones over one inch) in Texas in 2023, a record, and 878 in 2024, according to {SRC['ibhs']}.</p>
<!--fig:hail-->
<p>Hail is only part of it. Hurricane season runs June 1 to November 30, with the peak around September 10, per {SRC['nhc']}. And Houston gets wind events that aren’t hurricanes at all: the May 16, 2024 derecho brought damaging winds across the metro, with the strongest gusts estimated near 100 mph, according to {SRC['derecho']}. Less than two months later Beryl came through.</p>
<p>So the year has two kinds of demand. <b>Storm work</b> comes in sudden spikes, often paid through insurance claims. <b>Retail work</b> (aging roofs, home sales, upgrades, leaks) is steadier and usually higher margin per hour of sales time. A healthy roofing company markets for both, and the mistake we see most often is a company that only knows how to do one.</p>"""),
            ("The storm-chaser problem, and how local roofers win trust", f"""<p>Houston homeowners have seen the pattern. Crews show up after a storm, knock on every door, promise a free roof, and they’re gone before the warranty matters. That reputation lands on every roofer, including the ones who’ve been here 20 years.</p>
<p>Part of the reason is that Texas doesn’t license roofers at the state level. {SRC['cbs']} reported that roofers aren’t required to be licensed in Texas, though some choose voluntary licensing through the Roofing Contractors Association of Texas (RCAT). That gives homeowners very little to go on, which is exactly why your marketing should hand them proof.</p>
<!--fig:trust-->
<p>Proof that works for a local roofer:</p>
<ul><li>Your physical address and how long you’ve been at it, on every page and every ad.</li>
<li>Photos and short videos of jobs in named neighborhoods: “Replaced this roof in Imperial Oaks after the April hail.”</li>
<li>Manufacturer certifications and RCAT licensing, if you have them, with logos and a link to verify.</li>
<li>Insurance certificates available on request, and a line saying so.</li>
<li>Reviews that mention the city, the insurance process and the cleanup.</li>
<li>A real person’s face. Owner videos do better than polished brand spots for roofing.</li></ul>
<p>Make sure you’re not sounding like a chaser yourself. The {SRC['tdi']} is clear that Texas doesn’t allow a roofer or contractor to act as a public adjuster, and that it’s illegal for a contractor to offer to waive, rebate or absorb a homeowner’s deductible. TDI also notes that advertisements include websites. So ad copy like “We handle your claim for you” or “No out-of-pocket cost” can cross the line. Something closer to “We’ll meet your adjuster and document the damage” is the kind of language we’d bring to your attorney for a yes or no. We’re marketers, not lawyers, and the insurance rules here change often enough that a quick legal review of your storm ads is money well spent.</p>"""),
            ("What to do in the 72 hours after a storm", f"""<p>The roofers who win after a storm made their decisions weeks before it hit. This is the order we’d run it in:</p>
<!--fig:hours72-->
<ol><li><b>Hour 0–6: confirm where it hit.</b> Use NWS storm reports and hail maps to list the ZIP codes and subdivisions affected. Don’t guess from the news.</li>
<li><b>Hour 6–12: switch on storm campaigns.</b> Have paused Google Ads campaigns ready with storm copy, targeted to the affected ZIP codes. Raise LSA budgets. Post a Business Profile update with photos and a clear offer: free inspection, local crew, response times.</li>
<li><b>Hour 12–24: tell your past customers.</b> Text and email everyone in the affected area. Past customers and their neighbors are your warmest leads, and they already trust you.</li>
<li><b>Day 2–3: get crews and canvassers out with something to leave behind.</b> Door hangers with a QR code to a storm landing page, your address, and a text number.</li>
<li><b>Day 3 onward: follow up digitally.</b> Retarget landing page visitors, run Meta video ads of your crew in the area, and keep the inspection calendar moving.</li></ol>
<p>Your phones matter more than your ads in this window. If calls hit voicemail, LSA rankings can suffer (Google says so on its {SRC['lsa']}) and the homeowner calls the next name. Add a temporary answering service if you have to.</p>"""),
            ("Google Ads and Local Services Ads for roofers", f"""<p>For roofers, Google is where intent lives. Someone typing “roof repair the woodlands” or “hail damage roof inspection near me” has a problem now.</p>
<p><b>Local Services Ads</b> work well for roof repair and inspection calls. You pay per lead, and since October 2025 all advertisers carry the single Google Verified badge ({SRC['verified']}). Dispute junk leads through lead feedback in your account, every week.</p>
<p><b>Search campaigns</b> give you the control you need for storm response. Google’s housing ad restrictions are written around homes for sale or rent, per {SRC['ghousing']}, and repair work isn’t on its list of examples. As of this writing, that means roofing Search campaigns generally keep ZIP code targeting, so you can aim at the subdivisions that actually got hit. Policies shift, so if Google ever flags a campaign as housing, switch it to radius targeting rather than fighting the review.</p>
<div class="bp-tbl"><table><thead><tr><th>Campaign</th><th>When it runs</th><th>Example keywords</th><th>Goes to</th></tr></thead><tbody>
<tr><td>Storm response</td><td>Paused, switched on after hail or wind</td><td>hail damage roof, storm damage roof repair, roof inspection after storm</td><td>Storm landing page with inspection form</td></tr>
<tr><td>Roof repair</td><td>Year-round</td><td>roof leak repair, roof repair near me, emergency roof tarp</td><td>Repair page with phone number up top</td></tr>
<tr><td>Retail replacement</td><td>Year-round, heavier in spring and fall</td><td>roof replacement cost, new roof financing, metal roof</td><td>Replacement page with financing and photos</td></tr>
<tr><td>Brand</td><td>Always</td><td>Your company name</td><td>Home page</td></tr>
</tbody></table></div>
<p>Add negatives for “jobs,” “training,” “shingles for sale,” “DIY,” and “insurance agent.” Then plan for storm-week prices. Every roofer in the county bids on the same dozen phrases the morning after hail, so clicks that cost you a few dollars in a quiet week can cost several times that. Set aside a storm reserve in the budget before the season starts, so you aren’t deciding how much to spend at 6 a.m. with the phone already ringing. If you want help building this, see our <a href="/services/search-marketing/">Google Ads management</a> or read <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs Google Ads</a>.</p>"""),
            ("Meta ads for roofers: the ZIP code catch", f"""<p>A lot of roofing marketing advice says to run Facebook lead ads by ZIP code right after a storm. In practice, that usually isn’t allowed.</p>
<p>Meta lists housing repairs among the examples in its Housing special ad category, according to {SRC['metasac']}. Ads in that category can’t target by ZIP code, can’t narrow age or gender, and location targeting has to include at least a 15-mile radius. Roofing ads generally belong there, and running them outside it risks rejected ads or a restricted account.</p>
<p>What still works on Meta:</p>
<ul><li><b>A radius around the storm path.</b> Fifteen miles from a point in Cypress still covers a lot of hail damage. Let the creative do the targeting: name the storm, the date and the neighborhoods in the video and copy.</li>
<li><b>Your own customer list</b> as a custom audience, as long as it isn’t built to exclude people in a discriminatory way.</li>
<li><b>Retargeting</b> people who visited your storm landing page or scanned the door hanger QR code.</li>
<li><b>Lead forms with a qualifying question</b> or two (“Do you own the home?” “Have you filed a claim yet?”) so you’re not calling renters.</li></ul>
<p>Short phone video of your crew on a real roof in that area outperforms polished graphics almost every time. Our <a href="/services/paid-social-advertising/">paid social team</a> handles the category setup so you don’t get flagged in the middle of a storm push.</p>"""),
            ("Door hangers plus digital follow-up", f"""<p>Canvassing still works in Houston, especially in master-planned communities where neighbors watch each other’s roofs go up. The problem is that a door hanger is usually a one-shot touch. Most end up in the recycling bin.</p>
<p>Turn it into the start of a sequence instead:</p>
<!--fig:sequence-->
<ul><li>Put a QR code on the hanger that goes to a page about that specific storm, with photos of damage in that area and a two-field form.</li>
<li>Add a text number. Many homeowners would rather text a photo of their shingles than call.</li>
<li>Retarget everyone who scans with Meta and YouTube video for two to three weeks.</li>
<li>Send a follow-up postcard to the street a week later showing a roof you replaced nearby.</li></ul>
<p>Check local rules before you send canvassers out. Some cities and HOAs in the area restrict door-to-door solicitation or require permits, and getting reported does real damage to the “trusted local company” story. Want to reach the neighborhood without knocking? <a href="/blog/geo-fencing-ads-target-customers-nearby/">Geo-fencing ads</a> are another option, with the same housing-category caveats on Meta.</p>"""),
            ("Retail replacement work keeps you alive between storms", f"""<p>Storm work is feast or famine. Retail replacement is what pays the bills in a quiet year, and it needs a different message.</p>
<p>Retail customers aren’t in a hurry and often aren’t filing a claim. They’re selling a house and the inspector flagged the roof. They’re tired of a leak over the garage. They want a metal roof or better attic ventilation for the energy bill. They search phrases like “roof replacement cost,” “how long does a roof last in Texas,” and “roofing company the woodlands.”</p>
<p>What works for retail:</p>
<ul><li>A replacement page with honest price ranges, materials and financing terms.</li>
<li>SEO content that answers real questions, built around service-area pages for Spring, Conroe, Magnolia, Kingwood and the rest. See <a href="/blog/local-seo-contractors-houston/">local SEO for contractors in Houston</a>.</li>
<li>Relationships with real estate agents and home inspectors who need fast, reliable roof reports.</li>
<li>Google Search campaigns that run all year, with more budget in spring and fall when homeowners plan projects.</li></ul>
<p>Our <a href="/services/web-design-seo-pr/">web design and SEO team</a> builds these pages for contractors across <a href="/digital-marketing-agency-spring-tx/">Spring</a>, <a href="/digital-marketing-agency-conroe-tx/">Conroe</a> and <a href="/digital-marketing-agency-katy-tx/">Katy</a>.</p>"""),
            ("Reviews and photos: your proof after the trucks leave", f"""<p>After a storm, a homeowner might get five inspection offers in a week. The one they pick is usually the company with the most recent, most believable reviews.</p>
<p>Recency does more of the work than the total. A roofer with 300 reviews and nothing new since last spring looks, to a nervous homeowner, like a company that might not be around next year. So ask for a review the day the job is done, while the dumpster is still in the driveway, and replying to each one with the neighborhood and the work (“Thanks, Maria. Glad we got your Kingwood roof done before the next round of storms.”).</p>
<p>Photos matter just as much. Before, during and after shots of every job, uploaded to your Business Profile and to the matching city page on your site, give both Google and homeowners proof that you actually work there. Ask your crew lead to take ten photos per job. It takes five minutes. More in our <a href="/blog/complete-guide-google-reviews/">guide to Google reviews</a>.</p>"""),
            ("Build the storm kit before spring", f"""<p>Before the next hail cell shows up on radar, build the storm campaign, write the landing page, print the door hangers with QR codes, and put a name next to “answers the phone after hours.” Then leave it all paused. When the storm comes, your job is flipping switches, not writing ad copy in a parking lot.</p>
<p>Already running Google or Meta and not sure it would hold up in a storm week? A free <a href="/contact/">Ad Spend Leak Check</a> is a good place to find out. We record a 10-minute video of your account showing where the budget is slipping away, and it’s in your inbox within 48 hours. You can also see how we work with <a href="/industries/service/">home service companies</a>.</p>"""),
        ],
        "faq": [
            ("How do I get roofing leads after a storm?",
             "Have storm campaigns built and paused before the season, then switch them on within hours of hail or high wind, targeting the affected ZIP codes in Google Ads. Raise Local Services Ads budgets, text past customers in the area, leave door hangers with a QR code, and retarget everyone who visits your storm page."),
            ("Are Google Local Services Ads good for roofers?",
             "Yes, for repair and inspection calls. You pay per lead instead of per click and appear above regular ads with the Google Verified badge. They work best when someone answers every call quickly, because Google says missed calls can hurt ranking. Pair them with Search campaigns for replacements and storm response."),
            ("Can roofers target Facebook ads by ZIP code?",
             "Usually not. Meta includes housing repairs in its Housing special ad category, which blocks ZIP code targeting, narrowed age or gender, and requires at least a 15-mile radius. Roofers can still use radius targeting, customer lists, retargeting and lead forms. Google's housing rules currently focus on homes for sale or rent, so roofing Search campaigns generally keep ZIP targeting."),
            ("Do roofers need a license in Texas?",
             "Texas does not require a state license for roofers. Some companies choose voluntary licensing through the Roofing Contractors Association of Texas, and some cities require permits for roof work. Because homeowners have little to verify, local roofers should show their address, insurance, certifications and recent reviews in all marketing."),
            ("Can a roofer pay or waive my insurance deductible in Texas?",
             "No. The Texas Department of Insurance says it is illegal for a contractor to offer to waive, rebate or absorb a deductible, and roofers cannot act as public adjusters on claims for their own work. Contracts of $1,000 or more involving an insurance claim must include a notice that the homeowner pays the deductible."),
        ],
        "figures": {
            "hail": {
                "type": "bars",
                "title": "Major hail events in Texas by year",
                "sub": "Hailstones over one inch, per IBHS using Storm Prediction Center data",
                "items": [["2015", 783, "783"], ["2018", 508, "508"], ["2023", 1123, "1,123"], ["2024", 878, "878"]],
                "highlight": [2],
                "note": "Source: IBHS via Roofing Contractor",
                "alt": "Bar chart of major hail events in Texas by year, a record 1,123 in 2023, driving roofing leads in Houston",
                "caption": "Texas has led the country in major hail events for years, which keeps Houston roofers busy and competitive.",
            },
            "trust": {
                "type": "compare",
                "title": "How local roofers beat storm chasers online",
                "left": {"title": "What chasers rely on", "items": ["Door knocks and pressure", "“We handle your claim”", "No local address", "Generic stock photos", "Gone after the job"]},
                "right": {"title": "What local roofers show", "items": ["Address and years in business", "Photos from named neighborhoods", "Recent reviews by city", "Certifications and insurance", "Owner and crew on video"]},
                "alt": "Comparison of storm chaser tactics and local roofer trust signals for roofing marketing in Houston",
                "caption": "Homeowners can’t check a state roofing license, so your marketing has to supply the proof.",
            },
            "hours72": {
                "type": "steps",
                "title": "The first 72 hours after a storm",
                "sub": "A roofing marketing plan you build before the season",
                "steps": [
                    ["Confirm the hit zone", "Use NWS storm reports and hail maps to list ZIPs and subdivisions."],
                    ["Switch on storm ads", "Unpause Google storm campaigns and raise LSA budgets."],
                    ["Text past customers", "Reach everyone you’ve worked for in the affected area."],
                    ["Canvass with QR codes", "Door hangers link to a storm page and a text number."],
                    ["Follow up online", "Retarget visitors and run crew videos for two to three weeks."],
                ],
                "alt": "Five-step plan for roofing leads in the 72 hours after a Houston hail or wind storm",
                "caption": "Most of this is set up in advance, so the storm day is about switching things on.",
            },
            "sequence": {
                "type": "funnel",
                "title": "Turn a door hanger into a booked inspection",
                "stages": [["Door hanger with QR", "Day 0"], ["Storm page or text", "Day 0–2"], ["Retargeting video", "Day 2–21"], ["Neighbor postcard", "Day 7"], ["Inspection booked", "Goal"]],
                "note": "Illustrative example",
                "alt": "Funnel showing door hanger, storm page, retargeting and postcard steps toward booked roofing inspections in Houston",
                "caption": "Each touch points back to the same storm page, so you can measure what the canvassing produced.",
            },
        },
    },
]
