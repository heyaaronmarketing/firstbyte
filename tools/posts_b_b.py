"""Two industry posts (Oct 2026): pool builders/service companies and real estate agents in The Woodlands / Houston.

Research: Google LSA category list (Pool cleaner, Pool contractor, Real estate services), Anthony & Sylvan Houston
pool cost guide, Blue Haven build timelines, The Woodlands Township permitting page, Community Impact on Conroe
master-planned communities, Census QuickFacts (Montgomery County), WordStream/LocaliQ 2026 Google Ads benchmarks,
BrightLocal 2026 Local Consumer Review Survey, NAR 2025 Profile of Home Buyers and Sellers (via NAR and BAM),
HAR August 2026 market report, TREC advertising rules and 22 TAC 531.18, Google restricted-targeting policy,
Data Axle and ZAG summaries of Meta special ad categories, HUD Fair Housing Act overview, The Close on Zillow Flex,
Hart Energy on Chevron's HQ move, Business Facilities on ExxonMobil's Spring campus move.
"""


def L(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


SRC = {
    "sylvan": L("https://anthonysylvan.com/cost-to-build-a-pool-houston-texas/", "Anthony &amp; Sylvan’s Houston pool cost guide"),
    "bluehaven": L("https://www.bluehaven.com/blog/how-long-does-it-take-to-build-a-gunite-pool-8-delay-factors", "Blue Haven Pools"),
    "township": L("https://www.thewoodlandstownship-tx.gov/Community/Permitting/Home-Modifications", "The Woodlands Township’s permitting page"),
    "ci_conroe": L("https://communityimpact.com/houston/conroe-montgomery/development/2023/07/25/5-master-planned-communities-growing-in-conroe", "Community Impact"),
    "census": L("https://www.census.gov/quickfacts/montgomerycountytexas", "Census Bureau QuickFacts"),
    "lsa": L("https://support.google.com/localservices/answer/6224841?hl=en", "Google’s Local Services Ads category list"),
    "wordstream": L("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream/LocaliQ’s 2026 Google Ads benchmarks"),
    "brightlocal": L("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "dataaxle": L("https://www.data-axle.com/resources/blog/meta-special-ad-categories-rules/", "Data Axle’s summary of Meta’s special ad category rules"),
    "zag": L("https://www.zaginteractive.com/insights/articles/january-2025/2025-changes-for-meta-ads", "replaced the old Credit category"),
    "nar": L("https://www.nar.realtor/news/economists-outlook/top-10-takeaways-from-nars-2025-profile-of-home-buyers-and-sellers", "NAR’s 2025 Profile of Home Buyers and Sellers"),
    "bam": L("https://nowbam.com/how-home-buyers-and-sellers-find-their-agents-in-2025/", "the same NAR report, broken down by BAM"),
    "har": L("https://www.har.com/s/mrz7p4brVEcM", "HAR’s August 2026 market report"),
    "trec_ads": L("https://www.trec.texas.gov/article/trecs-advertising-rules-what-you-need-know", "TREC’s advertising rules"),
    "trec_cpn": L("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-531-18", "22 TAC §531.18"),
    "google_policy": L("https://support.google.com/adspolicy/answer/143465?hl=en", "Google’s restricted targeting policy"),
    "hud": L("https://www.hud.gov/helping-americans/fair-housing-act-overview", "HUD’s Fair Housing Act overview"),
    "close": L("https://theclose.com/zillow-flex/", "The Close’s June 2026 review of Zillow Flex"),
    "chevron": L("https://hartenergy.com/exclusives/chevron-moving-hq-ceo-california-houston-210008", "Hart Energy"),
    "exxon": L("https://businessfacilities.com/exxonmobil-is-moving-headquarters-to-houston/", "its Spring campus"),
    "villages": L("https://www.thewoodlandstownship-tx.gov/villageassociations", "The Woodlands Township"),
    "loomer": L("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to special ad categories"),
    "gbp": L("https://support.google.com/business/answer/3038177?hl=en", "Google’s Business Profile guidelines"),
}

POSTS = [
    # ------------------------------------------------------------------------------------------ pools
    {
        "slug": "pool-builder-marketing-houston-the-woodlands",
        "title": "Pool Builder Marketing in Houston & The Woodlands: How to Get Pool Leads",
        "seo_title": "Pool Builder Marketing in Houston & The Woodlands",
        "desc": "Pool builder and pool service marketing for Houston and The Woodlands: when to advertise, Google Ads, Meta targeting, reviews and nurturing long-cycle leads.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b3",
        "hero": "pool",
        "hero_alt": "Illustration of a backyard swimming pool for a pool builder marketing guide in Houston and The Woodlands",
        "related": ["local-services-ads-vs-google-ads-home-services", "facebook-instagram-ads-local-businesses", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Your phone rings off the hook in May, and every caller wants to swim by the Fourth of July. You can’t build that fast, so half of them go to whoever promised a date, and the other half sit on a waitlist that goes cold by August. Then January comes, the yard is quiet, and the ad budget feels like money thrown into a ditch.</p>
<p>The buyers who swim in summer are the ones who signed in winter. Most pool companies around Houston and The Woodlands advertise as if it worked the other way around. Below is how we’d market a pool builder or a pool service company north of Houston: when to spend, where, what to say, and how to keep a $70,000 lead warm for the four months it takes them to decide.</p>"""),
            ("Why pool leads behave differently from other home services", f"""<p>An AC repair call is an emergency. A pool is a family decision with a second mortgage-sized price tag. {SRC['sylvan']} puts a Houston inground pool at roughly <b>$40,000 to $120,000 or more</b>, with a common 12x24 pool landing around <b>$54,000 to $84,000</b>. One builder’s numbers, yes, but they match what most homeowners hear in their first round of quotes.</p>
<p>A price like that changes the marketing in a few ways:</p>
<ul><li><b>The decision takes weeks or months.</b> Couples compare three or four builders, ask the HOA, talk to the bank, and wait for a tax refund or bonus.</li>
<li><b>Visuals do the selling.</b> Nobody buys a pool from a paragraph. They buy from a photo of a pool that looks like the one they want, in a backyard that looks like theirs.</li>
<li><b>One closed job pays for a lot of ads.</b> You can afford a cost per lead that would make a plumber faint, as long as you track which leads actually sign.</li>
<li><b>The build itself has a long tail.</b> {SRC['bluehaven']} says most gunite projects run three to six months from first shovel to first swim, and permits alone can swing from days to months.</li></ul>
<p>That last point matters more than anything else on this page. If the swim date is Memorial Day and the build takes three to six months, the contract needs to be signed around the holidays. Your marketing calendar has to run backwards from that.</p>"""),
            ("When to advertise a pool company in Houston", f"""<p>Most pool companies spend the most when the phone is already ringing. By April, homeowners who want to swim this summer are already late, and you’re paying peak prices for people you can’t schedule.</p>
<!--fig:season-->
<p>Here’s the calendar we’d run for a builder in The Woodlands, Spring or Conroe:</p>
<ul><li><b>October to December:</b> start the conversation. “Swim by Memorial Day” offers, design consultations, and retargeting everyone who visited your gallery during the summer.</li>
<li><b>January to March:</b> heaviest spend. Tax refunds land, New Year’s plans get serious, and there’s still time to permit and build before school lets out.</li>
<li><b>April to June:</b> keep search running for high-intent queries, but shift the message to “book now for fall” so you aren’t promising dates you can’t hit.</li>
<li><b>July to September:</b> pull back on builder ads, lean into pool service, repairs, and remodels, and collect photos and reviews from every finished job.</li></ul>
<p>For timing that applies to every local business here, see our <a href="/blog/seasonal-marketing-greater-houston/">seasonal marketing guide for Greater Houston</a>.</p>
<h3>Work backwards from the swim date</h3>
<p>In The Woodlands, there’s an extra step most out-of-town builders forget. {SRC['township']} says work on a lot with an existing home needs prior written approval from the Residential Design Review Committee, and it specifically names pools, pool decking and pool equipment. A few Grogan’s Forest sections fall under both the Township and the City of Shenandoah, and the Township’s page says pool applications there start at Shenandoah city hall. Building that review time into your “swim by” promise, and saying so in your ads, makes you look like the builder who knows the neighborhood.</p>
<!--fig:timeline-->"""),
            ("Google Ads for pool builders: keywords, budgets and lead quality", f"""<p>Search is still where the highest-intent pool buyers show up. Someone typing “pool builders near me” or “custom pool cost The Woodlands” is further along than someone scrolling Instagram. The catch is that the same search box also brings you people looking for above-ground pools, pool supplies, public pools and summer jobs.</p>
<p>A few settings we’d check first in any pool builder’s account:</p>
<ul><li><b>Split campaigns by job type.</b> New construction, remodels and resurfacing, and weekly service should each have their own campaign and budget. They have different values and different searchers.</li>
<li><b>Build a negative keyword list on day one.</b> “Above ground,” “supply,” “store,” “public,” “jobs,” “hiring,” “membership,” “waterpark,” “lessons,” “inflatable.” Add to it every week from the search terms report.</li>
<li><b>Location options set to “presence.”</b> The default also counts people merely interested in your area, which is how a builder in Spring ends up paying for a click from Ohio.</li>
<li><b>Send leads to a page with a gallery and a price frame.</b> “Most of our pools land between X and Y” filters tire-kickers better than any form question.</li>
<li><b>Import closed jobs back into Google Ads.</b> If Google only learns from form fills, it will find you more form fills. If it learns from signed contracts, it finds more buyers.</li></ul>
<p>On cost, the closest public benchmark is the broad home-improvement category, which {SRC['wordstream']} put a little over $8 a click and about $91 a lead. Pool construction terms usually run well above that, because each job is worth so much and the builders bidding know it. Even at $200 or $300 per lead, the math works if one in ten leads signs a $60,000 contract. It falls apart if you never find out which ones did.</p>
<h3>Local Services Ads for pool companies</h3>
<p>{SRC['lsa']} includes both “Pool contractor” and “Pool cleaner” in the US. Those are the listings with the Google Verified badge at the very top of the page, and you pay per lead instead of per click. For a service company, it’s often the cheapest new-customer channel. For builders, it can work, but expect a mix of repair and service calls you’ll need to dispute or route. We compare the two in <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs. Google Ads</a>, and our <a href="/services/search-marketing/">Google Ads management</a> team sets up both.</p>"""),
            ("Meta ads to homeowners in new subdivisions and specific ZIP codes", f"""<p>Google catches people already looking. Facebook and Instagram reach the ones who aren’t yet, and for pools they live in very specific places.</p>
<p>North of Houston, a lot of it lives in newer master-planned communities with fresh backyards and no pool yet. {SRC['ci_conroe']} has profiled several growing around Conroe, including Grand Central Park off I-45 and Loop 336, Evergreen near Hwy. 242 and FM 1314, The Woodlands Hills, Artavia and Cielo. Add Bridgeland out in Cypress and the newer sections along the Grand Parkway, and you have a target list. Montgomery County alone grew <b>25.9%</b> between April 2020 and July 2025, to about 781,000 people, according to {SRC['census']}.</p>
<!--fig:map-->
<p>How we’d set it up:</p>
<ol><li><b>Check the Housing category question first.</b> Meta’s Housing special ad category lists “housing repairs” among its examples, per {SRC['loomer']}, and home-improvement ads sometimes get swept in. Many pool construction ads run outside it with ZIP or tight-radius targeting, but that’s Meta’s call, not yours. If Ads Manager puts your campaign in Housing, accept it and plan around a 15-mile minimum radius instead of trying to sneak around the review.</li>
<li><b>Lead with video.</b> A 20-second dig-to-splash timelapse from a real job in a recognizable neighborhood beats any stock photo.</li>
<li><b>Use a lead form with one qualifying question,</b> like “When would you like to be swimming?” with options from “This summer” to “Just browsing.” It sorts your follow-up for you.</li>
<li><b>Retarget gallery visitors for 90 to 180 days.</b> The long cycle means the person who looked in October may sign in February.</li></ol>
<h3>Careful with the financing line</h3>
<p>Financing is a real selling point when the average quote is the price of a car or two. But Meta now has a Financial Products and Services special ad category, which {SRC['zag']} in early 2025. If your ad is mostly about a loan, with rates, monthly payments and “apply now,” you can get pushed into that category, and it limits targeting much like housing does: no ZIP codes, full 18 to 65+ age range, all genders, per {SRC['dataaxle']}. Our approach is to keep the ad about the pool and put the payment details on the landing page. More on running these campaigns well is in our <a href="/services/paid-social-advertising/">paid social</a> overview.</p>"""),
            ("Google Business Profile, photos and reviews for pool companies", f"""<p>When someone searches “pool builder Spring TX,” the map pack usually shows up before the ads they scroll past. Your Business Profile is often the first gallery a homeowner sees.</p>
<ul><li><b>Pick the right primary category.</b> “Swimming pool contractor” for builders, “Swimming pool repair service” or “Pool cleaning service” for service companies. Secondary categories cover the rest.</li>
<li><b>Upload project photos every week during build season,</b> tagged by neighborhood in the description. “Freeform pool with tanning ledge, Alden Bridge” does more than “IMG_4471.”</li>
<li><b>Answer the questions people actually ask,</b> like price ranges, HOA approval, how long the build takes and whether you handle permits.</li></ul>
<p>Reviews are harder for builders than for almost any other contractor, for a dull mathematical reason. If you finish 35 pools a year, your newest review can easily be two or three months old, and a homeowner comparing you with a service company that gets five reviews a week notices. So ask at more than one moment: after the design meeting, at the dig, at the first swim, and again after the first full season, when the family has actually lived with the pool.</p>
<p>Answer each review yourself, and where it fits naturally, mention the neighborhood and the style of pool. A reply like “Thanks, Dana. That beach entry turned out great, and the design review in Panther Creek went faster than any of us expected” reads like a real builder. We cover the full system in our <a href="/blog/complete-guide-google-reviews/">guide to Google reviews</a>.</p>"""),
            ("Nurturing a lead that takes four months to decide", """<p>Most of the money pool companies waste isn’t in the ads at all. It’s in what happens after the quote. A homeowner fills out a form in October, gets a call and a quote, says “we’re thinking about it,” and never hears from you again. In February they sign with someone else, who simply happened to text them that week.</p>
<p>A long-cycle lead needs a long-cycle follow-up plan. It doesn’t have to be fancy. Here’s a sequence we’d set up in whatever CRM you already use:</p>
<div class="bp-tbl"><table><thead><tr><th>When</th><th>Channel</th><th>What to send</th></tr></thead><tbody>
<tr><td>Within 5 minutes</td><td>Text + call</td><td>Confirm the request, offer two consult times</td></tr>
<tr><td>Day 2</td><td>Email</td><td>Gallery of pools in their neighborhood or a similar lot size</td></tr>
<tr><td>Week 1</td><td>Email</td><td>“What a pool really costs here” with honest price ranges and what drives them</td></tr>
<tr><td>Week 3</td><td>Text</td><td>Short check-in, one question: “Still aiming for next summer?”</td></tr>
<tr><td>Monthly</td><td>Email</td><td>One finished project, one tip (HOA approval, financing, backyard drainage)</td></tr>
<tr><td>January</td><td>Text + email</td><td>“Last call to swim by Memorial Day” with a real cutoff date</td></tr>
</tbody></table></div>
<p>Two rules make it work. Every message should be useful on its own, not “just following up.” And someone on your team has to own the list, look at it weekly, and call the people who open three emails in a row. That’s a buyer warming up.</p>
"""),
            ("Builder vs. weekly service: market them as two businesses", """<p>If you build pools and also run service routes, you have two businesses with different buyers, calendars and economics. Lumping them into one campaign usually means the cheaper service clicks eat the budget while the builder leads starve.</p>
<!--fig:split-->
<p>What each side needs:</p>
<ul><li><b>Builder side:</b> big-ticket search terms, galleries, video, Meta prospecting in new subdivisions, long nurture sequences, price framing, financing on the landing page.</li>
<li><b>Service side:</b> Local Services Ads, “pool cleaning near me” searches, route density (a new customer three houses from an existing stop is worth more than one across Lake Conroe), recurring billing, and referral offers.</li></ul>
<p>Service also has its own seasonal spikes that builders don’t. Spring openings, green-pool cleanups, and storm cleanups after a tropical system are real moments. After Beryl in July 2024, plenty of pools across Houston sat full of debris with pumps off for days. A service company with a ready-to-go “storm cleanup” ad and a landing page could turn on spend the morning after. Write that campaign now, pause it, and keep it on the shelf for hurricane season, June 1 through November 30.</p>
<p>The two sides still feed each other. Every service customer is a remodel or equipment lead, and every new pool should leave with a service agreement offer.</p>"""),
            ("Your website: the gallery is the sales pitch", """<p>Most pool builder sites we review have a slow homepage slider, 200 unlabeled gallery photos and a form that asks for everything but a blood type. And almost none of them give a price frame, so a homeowner with a $35,000 budget and a builder whose average job is $95,000 end up wasting each other’s evening at a kitchen table.</p>
<p>A pool site that converts usually has:</p>
<ul><li><b>A gallery filtered by style and budget,</b> like freeform, geometric, small yards, with spas, under $75K. People want to find “one like mine.”</li>
<li><b>Neighborhood project pages.</b> “Pools we’ve built in Sterling Ridge” or “Pool builder in Conroe” pages rank for local searches and reassure buyers you know their HOA.</li>
<li><b>A plain-English process page</b> covering design, HOA approval, permits, dig, steel, gunite, tile and coping, plaster, startup.</li>
<li><b>A short form,</b> with name, phone, ZIP code and “when do you want to swim?”</li>
<li><b>Fast load on a phone,</b> because that’s where most of these clicks come from. Compress those gallery images.</li></ul>
<p>If you work the north side of the county, a page aimed at Conroe and Lake Conroe homeowners is worth building. We’ve written about what works in that market on our <a href="/digital-marketing-agency-conroe-tx/">Conroe page</a>, and our <a href="/industries/service/">home services</a> page shows how we approach contractors in general.</p>"""),
            ("A sample budget for a pool builder north of Houston", """<p>Every company is different, so treat this as a starting framework, not a quote. Say you build 30 to 40 pools a year from a shop in The Woodlands and want to add ten more:</p>
<div class="bp-tbl"><table><thead><tr><th>Channel</th><th>Example monthly spend (peak season)</th><th>Job</th></tr></thead><tbody>
<tr><td>Google Search (new construction)</td><td>$3,000–$6,000</td><td>Catch high-intent “pool builder” searches</td></tr>
<tr><td>Meta (video + lead forms)</td><td>$1,500–$3,000</td><td>Reach homeowners in target subdivisions and ZIP codes</td></tr>
<tr><td>Retargeting (Google + Meta)</td><td>$300–$600</td><td>Keep gallery visitors warm through the long cycle</td></tr>
<tr><td>Local Services Ads (service/remodel)</td><td>$500–$1,500</td><td>Pay-per-lead calls for service and repair</td></tr>
<tr><td>Email/text nurture</td><td>CRM cost only</td><td>Turn fall leads into winter contracts</td></tr>
</tbody></table></div>
<p>These are illustrative ranges, not benchmarks. In slow months, cut search and keep retargeting and nurture running. Spend hardest from October through March.</p>"""),
            ("Before the winter buying season opens", """<p>October is the right time to do this, not February. In order:</p>
<ol><li>Pull last year’s signed contracts and note the month each lead first came in. You’ll probably see the fall and winter pattern in your own data.</li>
<li>Split builder and service into separate campaigns with separate budgets.</li>
<li>Write the “swim by Memorial Day” offer with a real sign-by date that accounts for HOA review and permits.</li>
<li>Set up a six-month nurture sequence for every lead who didn’t sign.</li>
<li>Shoot one dig-to-splash video on your next job.</li></ol>
<p>Running ads already and can’t say which ones turned into signed contracts? That’s the question our free <a href="/contact/">Ad Spend Leak Check</a> is built for. We go through your Google or Meta account and record a 10-minute video of where the budget is leaking, whether it’s service clicks eating builder money or forms nobody follows up on, and send it within 48 hours.</p>"""),
        ],
        "faq": [
            ("How do pool builders get more leads?",
             "Most of them come from a mix of Google search ads for high-intent terms like pool builder near me, a strong Google Business Profile with fresh project photos and reviews, and Facebook and Instagram video ads aimed at homeowners in newer subdivisions. The biggest gain usually comes from following up on old leads for several months, since many buyers take a full season to decide."),
            ("When is the best time to advertise a pool company in Houston?",
             "Start in October and spend the most from January through March. Builds commonly take three to six months, and HOA and permit approvals add time, so homeowners who want to swim by summer need to sign in winter. Keep search running in spring but sell fall build slots, and shift summer spend toward service, repairs and remodels."),
            ("How much should a pool builder spend on marketing?",
             "It depends on job size and capacity, but many builders north of Houston can test with a few thousand dollars a month on Google search plus one to three thousand on Meta during peak season. Judge it by signed contracts, not form fills. One closed pool can cover months of ad spend if you track which leads actually bought."),
            ("Do Google Local Services Ads work for pool companies?",
             "Google lists Pool contractor and Pool cleaner as Local Services Ads categories in the US, and you pay per lead rather than per click. They tend to work very well for weekly service and repair companies. Builders can use them too, but expect some service calls mixed in and plan to dispute leads that are not a fit."),
            ("Can I target specific neighborhoods with Facebook ads for my pool company?",
             "Often, but not always. Many pool construction ads run outside Meta's Housing category, which allows ZIP or tight-radius targeting around new communities. Meta lists housing repairs as a Housing example, though, and may place home-improvement ads there, which means a 15-mile minimum radius. Ads built around loans or monthly payments can also land in the Financial Products and Services category, which removes ZIP, age and gender targeting."),
        ],
        "figures": {
            "season": {
                "type": "columns",
                "title": "When pool buyers decide vs. when they swim",
                "sub": "Relative builder lead value by month for a Houston-area pool company",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [88, 100, 92, 70, 52, 38, 28, 26, 34, 58, 66, 62],
                "highlight": [0, 1, 2, 9, 10, 11],
                "y_label": "Lead value",
                "note": "Illustrative example",
                "alt": "Column chart showing pool builder leads in Houston and The Woodlands are most valuable from October through March",
                "caption": "Builder leads that sign in fall and winter are the ones you can finish before summer.",
            },
            "timeline": {
                "type": "steps",
                "title": "Working back from a Memorial Day swim",
                "sub": "A typical schedule for a gunite pool in The Woodlands",
                "steps": [
                    ["Nov to Dec: design and sign", "Consult, 3D design, price and contract. This is when your ads need to be running."],
                    ["Dec to Jan: HOA and permits", "Residential Design Review Committee approval in The Woodlands, plus city or county permits."],
                    ["Jan to Feb: dig, steel and plumbing", "Excavation, rebar and plumbing, with Houston winter rain delays built in."],
                    ["Feb to Mar: gunite, tile and coping", "Shell sprayed and cured, then tile, coping and decking."],
                    ["Apr to May: plaster and startup", "Interior finish, fill, chemical startup and the first swim."],
                ],
                "alt": "Step timeline showing how a pool in The Woodlands must be signed in late fall to be ready by Memorial Day",
                "caption": f"Most gunite builds run three to six months, per {SRC['bluehaven']}, before HOA review.",
            },
            "map": {
                "type": "map",
                "title": "Where new backyards are north of Houston",
                "sub": "Areas with fast-growing master-planned communities worth targeting",
                "highlight": ["The Woodlands", "Conroe", "Willis", "Spring", "Cypress", "Tomball", "Magnolia", "Montgomery"],
                "alt": "Map of pool marketing target areas around The Woodlands, Conroe, Cypress and Magnolia north of Houston",
                "caption": f"Montgomery County grew 25.9% from 2020 to 2025, per {SRC['census']}.",
            },
            "split": {
                "type": "compare",
                "title": "One pool campaign vs. two",
                "left": {"title": "Builder and service lumped together", "items": [
                    "Cheap service clicks eat the budget",
                    "One landing page tries to sell everything",
                    "No idea which leads became $60K contracts",
                    "Same spend in July as in January",
                ]},
                "right": {"title": "Split by business line", "items": [
                    "Separate budgets for builds and service",
                    "Galleries for buyers, booking pages for service",
                    "Signed contracts imported into Google Ads",
                    "Builder spend peaks October to March",
                    "Service runs year-round with storm ads ready",
                ]},
                "alt": "Comparison of one combined pool company campaign versus separate builder and pool service marketing in Houston",
                "caption": "Builders and service routes have different buyers, calendars and margins, so give each its own budget.",
            },
        },
    },
    # ------------------------------------------------------------------------------------------ real estate
    {
        "slug": "real-estate-agent-marketing-the-woodlands-houston",
        "title": "Real Estate Agent Marketing in The Woodlands & Houston: Own Your Leads",
        "seo_title": "Real Estate Marketing in The Woodlands & Houston",
        "desc": "Real estate agent marketing for The Woodlands and Houston: village guides, Business Profile, Meta housing ad rules, TREC compliance and owning your leads.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Meta", "YouTube"],
        "art": "b5",
        "hero": "realestate",
        "hero_alt": "Illustration of a home for sale for a real estate agent marketing guide in The Woodlands and Houston",
        "related": ["google-business-profile-number-one-asset", "power-of-local-landing-pages", "email-marketing-basics"],
        "sections": [
            (None, f"""<p>You paid for the lead. Then you paid again at closing, a slice of your commission handed back to the portal that sent it. And the next time that buyer moves, there’s a fair chance they’ll start the search on the same app and get matched with someone else.</p>
<p>Plenty of agents in The Woodlands and Houston have quietly accepted that deal. Portal leads can fill a calendar, but you’re renting a pipeline, and the rent goes up when the market slows. Below is how we’d build one you own instead: village and neighborhood content, a Business Profile that ranks, video, Meta ads that stay inside the housing rules, and the TREC fine print that catches even agents with 15 years in.</p>
<p>A quick reality check on the market first. {SRC['har']} shows Greater Houston single-family sales down 11.5% year over year to 7,100 in August 2026, with a median price of $330,000, 5.3 months of inventory and homes averaging 54 days on market. A slower market rewards agents who already have a list of people who know them.</p>
<!--fig:market-->"""),
            ("Zillow leads vs. your own leads: what you’re really paying for", f"""<p>Start with what a portal lead actually costs. According to {SRC['close']}, Zillow’s Flex program charges no upfront fee but takes a success fee at closing based on a percentage of your commission. Its example is a 35% fee on a $12,000 commission, or $4,200 on a single deal. The exact rate varies by market, and you also need its required CRM.</p>
<p>That can still be worth it, especially for a newer agent with time and no sphere. But look at where buyers actually come from. In {SRC['nar']}, 88% of buyers used an agent. And in {SRC['bam']}, the top source for finding that agent was a referral from a friend, neighbor or relative (43%), followed by an agent they’d used before (15%). Sellers were even more loyal: 37% came from referrals and 29% went back to a previous agent.</p>
<!--fig:sources-->
<p>So the biggest pipeline in real estate is people who already know you or know someone who does. Portals can be a supplement. The thing worth building is a list, a reputation and a local presence that keeps you top of mind for the five to ten years between moves.</p>
<!--fig:own-->"""),
            ("Hyperlocal content: village and neighborhood guides for The Woodlands", f"""<p>A national portal can’t tell a relocating family the real difference between Sterling Ridge and Alden Bridge. You can. That’s your content advantage.</p>
<p>Start with the villages. {SRC['villages']} lists eight village associations: Alden Bridge, Cochran’s Crossing, College Park, Creekside Park, Grogan’s Mill, Indian Springs, Panther Creek and Sterling Ridge. Harper’s Landing, which plenty of locals and listings call the ninth village, doesn’t have its own entry on that list, so check how a specific address is classified with the Township’s lookup tool before you write it up. Getting that kind of detail right is what earns trust from someone who’s about to move here.</p>
<p>A strong village guide answers what buyers actually search and ask:</p>
<ul><li>Which schools serve it (link to the district’s own boundary tool rather than guessing).</li>
<li>Commute times at rush hour to the Energy Corridor, the Medical Center, Springwoods Village and downtown.</li>
<li>Which county it’s in. Creekside Park is in Harris County, the rest of The Woodlands is in Montgomery County, and that changes taxes and services.</li>
<li>Pools, parks, trails, and the nearest grocery store.</li>
<li>What’s sold recently and in what price range, updated quarterly.</li>
<li>Your own photos and a short walking video, not stock images.</li></ul>
<p>Then go beyond The Woodlands: Spring, Tomball, Magnolia, Conroe, Kingwood, Cypress. One solid page per area beats 40 thin ones. We go deeper on this approach in <a href="/blog/power-of-local-landing-pages/">the power of local landing pages</a>.</p>
<h3>Write for AI answers too</h3>
<p>{SRC['brightlocal']} found 45% of consumers now use ChatGPT or other AI tools to find local business recommendations, up from 6% the year before. AI tools pull from pages that answer questions clearly. A guide with a short, direct answer to “What’s the difference between Sterling Ridge and Creekside Park?” is the kind of thing those tools quote.</p>"""),
            ("Relocation buyers and the energy industry", f"""<p>Houston gets a steady stream of corporate relocations, and a big share connects to energy. ExxonMobil moved its headquarters from Irving to {SRC['exxon']}. Chevron announced in August 2024 that it was moving its headquarters and top leadership from San Ramon, California, to Houston, according to {SRC['chevron']}, which noted the company already had roughly 7,000 employees in the Houston area.</p>
<p>Relocation buyers are a different kind of client. They often shop from another state, on a deadline, with a relocation package and little sense of the map. What they search looks like this:</p>
<ul><li>“best neighborhoods near ExxonMobil campus Spring TX”</li>
<li>“The Woodlands vs Katy for families”</li>
<li>“moving to Houston from California”</li>
<li>“what is a MUD tax”</li>
<li>“does The Woodlands flood”</li></ul>
<p>Each of those is a page or a video. A “Moving to The Woodlands” guide that covers commutes, property taxes, MUDs, hurricane season (June 1 to November 30), flood zones and the summer heat honestly, without sugarcoating it, will outlast any ad you run. Put a simple “relocation call” booking link at the bottom.</p>"""),
            ("Google Business Profile for real estate agents", f"""<p>Agents can have their own profiles. {SRC['gbp']} name real estate agents as an example of individual practitioners who can get a dedicated profile, as long as they’re public-facing and can be contacted directly during stated hours. If you work from home, you’re a service-area business and should hide your home address and set service areas instead.</p>
<p>What makes an agent profile work:</p>
<ul><li><b>Primary category: “Real estate agent.”</b> Brokerages use “Real estate agency.”</li>
<li><b>Service areas that match where you sell,</b> like The Woodlands, Spring, Conroe and Tomball, not all of Texas.</li>
<li><b>Photos of you, your listings and the neighborhoods,</b> added steadily. Sold signs, closing-day photos (with permission) and village landmarks.</li>
<li><b>Weekly posts:</b> a new listing, an open house, a short market update.</li>
<li><b>Reviews that mention the neighborhood and the situation,</b> like “sold our Panther Creek home in a week” or “helped us relocate from Denver.”</li></ul>
<p>On reviews, the bar is rising. {SRC['brightlocal']} also found 31% of consumers will only use a business with 4.5 stars or more, and 50% are put off by templated replies. Write each reply yourself. Our <a href="/blog/google-business-profile-number-one-asset/">Google Business Profile guide</a> covers setup in detail.</p>
<p>One more Google option: the US Local Services Ads list includes a “Real estate services” category, per {SRC['lsa']}. Check whether it’s live for your area before building a plan around it.</p>"""),
            ("Video tours and short-form content that actually works", """<p>Listings get the attention, but they aren’t the content that builds your business. Your listing is gone in a month. A good neighborhood video can bring in clients for years.</p>
<p>Formats we’d prioritize for an agent in The Woodlands or Houston:</p>
<ul><li><b>Village drive-throughs:</b> five minutes, narrated, on YouTube. “Living in Alden Bridge: a drive-through tour.” Long, searchable, and great for relocation buyers.</li>
<li><b>60-second cuts</b> of the same video for Instagram, Facebook and TikTok.</li>
<li><b>Listing walkthroughs</b> shot vertical on a gimbal, with the price and village name in the first two seconds.</li>
<li><b>“What $450K buys in…” comparisons</b> across Spring, Conroe and The Woodlands.</li>
<li><b>Market updates</b> you record once a month, with HAR numbers on screen and a 30-second takeaway.</li></ul>
<p>A phone, a gimbal and a decent lav mic will cover all of it. What matters is the calendar. One long video a month and three or four short clips a week, posted for a year, will do more than a $5,000 brand video that runs once.</p>"""),
            ("Facebook ads for real estate in Houston: the Housing category rules", f"""<p>This is where a lot of agents get their ads rejected or, worse, run them illegally without knowing it. Any ad for listings, home sales or related services in the US has to run under Meta’s Housing special ad category. According to {SRC['dataaxle']}, that means:</p>
<ul><li>No ZIP code targeting, and you can’t exclude locations.</li>
<li>Age must span 18 to 65+, and all genders must be included.</li>
<li>Detailed targeting is limited, and lookalike audiences based on Meta’s data are unavailable.</li>
<li>Location targeting must include everything within a 15-mile radius of any point you pick, per {SRC['loomer']}. A pin in The Woodlands reaches well into Spring, Conroe and north Houston.</li></ul>
<p>Google runs similar rules. {SRC['google_policy']} says housing ads in the US and Canada can’t target by gender, age, parental status, marital status or ZIP code.</p>
<h3>What still works under the rules</h3>
<ul><li><b>Let the creative do the targeting.</b> An ad that says “Sterling Ridge homes under $600K” speaks to the right people even when Meta shows it to a wider audience.</li>
<li><b>Retarget your own website visitors</b> and video viewers, who have already raised a hand.</li>
<li><b>Use lead forms with a qualifying question</b> about timeline or pre-approval.</li>
<li><b>Promote your content, not just listings.</b> A “Moving to The Woodlands” guide ad builds your list for months.</li></ul>
<p>If you’d rather not wrestle with the setup, our <a href="/services/paid-social-advertising/">paid social team</a> runs Housing category campaigns for agents and brokerages.</p>"""),
            ("TREC and Fair Housing: the advertising rules that trip up agents", f"""<p>Texas real estate advertising has its own rules, and they apply to every Instagram post, Facebook ad and email you send. {SRC['trec_ads']} define advertising to include email, text messages, social media and the internet. A few that come up constantly:</p>
<ul><li><b>Broker name size.</b> The broker’s name has to appear in at least half the size of the largest contact information for the agent or team in the ad.</li>
<li><b>Team names</b> must end in “team” or “group” and can’t include words like “brokerage,” “company” or “associates.”</li>
<li><b>Homepage links.</b> Your website homepage needs a link to the Information About Brokerage Services form, labeled “Texas Real Estate Commission Information About Brokerage Services” in at least 10-point font, or the shorter “TREC Information About Brokerage Services” in at least 12-point font, per TREC’s guidance. {SRC['trec_cpn']} also requires a Consumer Protection Notice link on the homepage.</li>
<li><b>“Sold” claims.</b> You can only say you sold a property if you actually worked on that transaction.</li></ul>
<p>Fair Housing applies on top of that. {SRC['hud']} lists the protected classes: race, color, national origin, religion, sex, familial status and disability. In practice, describe the property and the amenities, not the people you imagine living there. “Walk to Rob Fleming Park” is fine. Phrases that suggest who should or shouldn’t live somewhere aren’t.</p>
<!--fig:compliance-->
<p>This is a summary, not legal advice. TREC updates its rules, your sponsoring broker is responsible for supervising your advertising, and anything borderline belongs with the broker or a real estate attorney. A two-minute check before an ad goes live still catches most of the common mistakes.</p>"""),
            ("Email, IDX and the long game", f"""<p>The average seller in {SRC['nar']} had owned their home for 11 years. That’s a long time to stay remembered. Email is the cheapest way to do it.</p>
<ol><li><b>Collect every contact into one CRM,</b> including past clients, open-house sign-ins, guide downloads and sphere.</li>
<li><b>Send a monthly email that’s actually useful:</b> a short market update for their village, one new listing, one local event at Market Street or Waterway Square.</li>
<li><b>Send a yearly home value check-in</b> on the anniversary of their closing.</li>
<li><b>Use IDX saved searches</b> so buyers get new listings from your site, not a portal. Make sure your IDX pages are indexable and fast on a phone.</li>
<li><b>Ask for referrals by name,</b> twice a year, with a specific prompt like “know anyone relocating for work?”</li></ol>
<p>None of that requires a big budget. It requires showing up every month. Our <a href="/blog/email-marketing-basics/">email marketing basics</a> post covers the setup, and our <a href="/services/web-design-seo-pr/">web design and SEO</a> team builds agent sites with IDX that ranks.</p>"""),
            ("A simple monthly plan for an agent or small brokerage", """<div class="bp-tbl"><table><thead><tr><th>Activity</th><th>Example monthly cost</th><th>Time</th></tr></thead><tbody>
<tr><td>One new neighborhood or village guide</td><td>$0–$500 (writing, photos)</td><td>4–6 hours</td></tr>
<tr><td>One long YouTube video + 12 short clips</td><td>$0–$750 (editing)</td><td>4–8 hours</td></tr>
<tr><td>Meta Housing ads (content + retargeting)</td><td>$500–$1,500</td><td>1–2 hours</td></tr>
<tr><td>Google Business Profile posts and review replies</td><td>$0</td><td>2 hours</td></tr>
<tr><td>Monthly email to sphere and past clients</td><td>$20–$100 (email tool)</td><td>2 hours</td></tr>
</tbody></table></div>
<p>These are illustrative ranges for a solo agent or a small team, not benchmarks. For context on paid search, {SRC['wordstream']} put Real Estate at about $3.22 per click and $102.51 per lead on average, which is cheaper per click than most local categories but expensive per lead. That’s another reason content and your own list matter.</p>
<p>If you’re based in Spring or along the I-45 corridor, our <a href="/digital-marketing-agency-spring-tx/">Spring page</a> has more on that market.</p>"""),
            ("Pick one village and own it", """<p>Choose the one village or neighborhood you know better than any other agent. Write the guide, shoot the drive-through, and get both onto your Business Profile and website before the end of the month. Then send the first monthly email to everyone who already knows you, even if the list is 80 people. Do that for a year and the portal invoice starts to matter a lot less.</p>
<p>If part of your budget already goes to Meta or Google ads, a free <a href="/contact/">Ad Spend Leak Check</a> will show you whether it’s working. We record a 10-minute video walking through your account, including Housing category setup, and you’ll have it within 48 hours.</p>"""),
        ],
        "faq": [
            ("Are Zillow leads worth it for agents in The Woodlands?",
             "They can be, especially for newer agents with time and a thin sphere. But programs like Zillow Flex take a share of your commission at closing, and the client relationship often stays with the portal. Most agents do better long term by putting part of that money into their own website, neighborhood content, video and an email list they control."),
            ("How do real estate agents get leads in Houston?",
             "According to NAR's 2025 buyer and seller profile, referrals from friends and family and repeat clients are the biggest sources by far. Beyond that, agents in Houston get leads from a well-reviewed Google Business Profile, neighborhood guides and videos that rank in search, Meta ads run under the Housing category, open houses, and portals."),
            ("Can real estate agents target ZIP codes on Facebook?",
             "No. Ads for listings and housing-related services in the US must run under Meta's Housing special ad category, which blocks ZIP code targeting, requires the full 18 to 65+ age range and all genders, and limits detailed targeting. You can still target a radius of at least 15 miles, retarget your own site visitors, and use creative that names the neighborhood."),
            ("What does TREC require in real estate ads?",
             "TREC treats social media, email, text messages and websites as advertising. The broker's name must appear in at least half the size of the largest agent or team contact information, team names must end in team or group, and your website homepage needs links to the Information About Brokerage Services form and the Consumer Protection Notice."),
            ("What are the villages in The Woodlands?",
             "The Woodlands Township lists eight village associations: Alden Bridge, Cochran's Crossing, College Park, Creekside Park, Grogan's Mill, Indian Springs, Panther Creek and Sterling Ridge. Creekside Park is in Harris County, while the rest are in Montgomery County. Many locals also count Harper's Landing as a ninth village, though it has no separate association on the Township's list, so check specific addresses with the Township."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "Greater Houston housing, August 2026",
                "stats": [["$330K", "median single-family price"], ["7,100", "single-family sales, down 11.5% year over year"], ["5.3", "months of inventory"], ["54", "average days on market"]],
                "note": "Source: HAR",
                "alt": "Stat tiles with HAR August 2026 Houston housing numbers for real estate agent marketing in The Woodlands",
                "caption": f"Numbers from {SRC['har']}.",
            },
            "sources": {
                "type": "bars",
                "title": "How buyers found their agent",
                "sub": "Share of all buyers, 2025",
                "items": [
                    ["Referral from friend or family", 43, "43%"],
                    ["Agent they used before", 15, "15%"],
                    ["Referral from another agent", 7, "7%"],
                    ["Online property inquiry", 7, "7%"],
                    ["Website, no referral", 6, "6%"],
                    ["Open house", 5, "5%"],
                ],
                "highlight": [0, 1],
                "note": "Source: NAR 2025 Profile of Home Buyers and Sellers",
                "alt": "Bar chart of how home buyers found their real estate agent, relevant to real estate leads in Houston",
                "caption": f"Referrals and repeat clients dominate, per {SRC['bam']}.",
            },
            "own": {
                "type": "compare",
                "title": "Renting leads vs. owning them",
                "left": {"title": "Portal-first", "items": [
                    "Pay a share of commission at closing",
                    "Lead may be sent to several agents",
                    "Next move starts on the portal again",
                    "Stops the day you stop paying",
                ]},
                "right": {"title": "Own your pipeline", "items": [
                    "Village guides that rank for years",
                    "Business Profile with neighborhood reviews",
                    "Email list of sphere and past clients",
                    "IDX saved searches on your own site",
                    "Referrals asked for twice a year",
                ]},
                "alt": "Comparison of Zillow leads vs own leads for real estate agents in The Woodlands and Houston",
                "caption": "Portal leads can fill gaps, but the long-term pipeline comes from assets you control.",
            },
            "compliance": {
                "type": "checklist",
                "title": "Before any real estate ad goes live",
                "sub": "A quick TREC, Fair Housing and Meta check for Texas agents",
                "items": [
                    "Broker name at least half the size of your contact info",
                    "Team name ends in team or group",
                    "Meta campaign set to the Housing special ad category",
                    "No ZIP targeting, full age range, all genders",
                    "Copy describes the home, not who should live there",
                    "Only claim sold if you worked the deal",
                    "Homepage links to IABS and Consumer Protection Notice",
                    "Sponsoring broker has reviewed it",
                ],
                "alt": "Checklist of TREC and Fair Housing advertising rules for real estate Facebook ads in Houston and The Woodlands",
                "caption": f"Based on {SRC['trec_ads']} and Meta’s Housing category rules. Not legal advice.",
            },
        },
    },
]
