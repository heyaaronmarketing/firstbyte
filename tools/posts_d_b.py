"""Long-tail post: is Nextdoor advertising worth it (Houston / The Woodlands angle, 2026).

Research: Nextdoor's own small-business pages (free Business Page features, Nextdoor Ads quick-create and
"broad" landing pages, the v4 how-to page with billing and placements, the Local Deals transition page,
Opportunity Alerts product page), Nextdoor's Neighborhood Ad Center quickstart guide (CPM/CPC bids), Nextdoor's
ad policy (housing/employment/credit rules), Nextdoor's August 19, 2026 self-promotion policy update, the
August 4, 2026 "What's new on Nextdoor" product post, Nextdoor's Q2 2026 results release, the 2026 Fave Awards
release, Pew Research's 2025 social media fact sheet, Jon Loomer on Meta's housing special ad category, Houston
Agent Magazine on Grand Central Park (Conroe), and Harbert Group on Woodlands villages by ZIP.
Competitor pages read: tech.co (2022), Power Digital (2024), PipelineOn (2026).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "local": A("https://business.nextdoor.com/local", "Nextdoor’s small business page"),
    "qc": A("https://business.nextdoor.com/en-us/local/advertise-with-nextdoor-ads-qc", "Nextdoor’s ad setup page"),
    "broad": A("https://business.nextdoor.com/en-us/local/advertise-with-nextdoor-broad", "Nextdoor’s local ads page"),
    "howto": A("https://business.nextdoor.com/en-us/local/advertise-with-nextdoor-ads-v4-naccta-nb-5pday-how-to", "Nextdoor’s ad how-to page"),
    "deals": A("https://business.nextdoor.com/en-us/local/localdealstransition", "Nextdoor’s Local Deals transition page"),
    "nadc": A("https://business.nextdoor.com/en-us/neighborhood-ad-center/blog/quickstart-guide-to-the-neighborhood-ad-center", "Nextdoor’s Ads Manager quickstart guide"),
    "alerts": A("https://business.nextdoor.com/en-us/small-business/product/opportunity-alerts", "Opportunity Alerts page"),
    "selfpromo": A("https://blog.nextdoor.com/self-promotion-update", "self-promotion policy update"),
    "whatsnew": A("https://blog.nextdoor.com/whats-new-on-nextdoor-product-updates-2", "August 2026 product update"),
    "q2": A("https://about.nextdoor.com/press-releases/nextdoor-reports-second-quarter-2026-results", "Q2 2026 results"),
    "faves": A("https://about.nextdoor.com/press-releases/nextdoor-opens-voting-for-the-2026-fave-awards", "2026 Fave Awards announcement"),
    "policy": A("https://business.nextdoor.com/en-us/enterprise/ad-policy", "Nextdoor’s ad policy"),
    "pew": A("https://www.pewresearch.org/internet/fact-sheet/social-media/", "Pew Research Center"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s guide to Meta’s special ad categories"),
    "gcp": A("https://houstonagentmagazine.com/2026/01/21/grand-central-park-nears-close-final-lots-go-to-builders/", "Houston Agent Magazine"),
    "harbert": A("https://www.harbertgroup.com/blog/992/Living+In+The+Woodlands+77381+In+2026%3A+Grogan%27s+Mill%2C+Panther+Creek%2C+Cochran%27s+Crossing%2C+Indian+Springs", "a local real estate guide"),
}

POSTS = [
    {
        "slug": "is-nextdoor-advertising-worth-it",
        "title": "Is Nextdoor Advertising Worth It? An Honest 2026 Answer for Houston",
        "seo_title": "Is Nextdoor Advertising Worth It? 2026 Local Guide",
        "desc": "Is Nextdoor advertising worth it? 2026 Nextdoor ad costs, the free Business Page, Nextdoor vs Facebook ads, and a 60-day test for Woodlands businesses.",
        "category": "Paid ads",
        "icons": ["Nextdoor", "Facebook", "Google Ads"],
        "art": "b5",
        "hero": "realestate",
        "hero_alt": "Illustration of suburban homes for a guide on whether Nextdoor advertising is worth it for businesses in The Woodlands",
        "related": ["facebook-instagram-ads-local-businesses", "is-yelp-advertising-worth-it-small-business", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>Is Nextdoor advertising worth it? For a local business that serves homeowners in a defined area, a small, tracked test usually is, and the free Business Page is worth claiming either way. Paid Nextdoor ads do best for home services, pet care, neighborhood retail and listing agents in owner-heavy suburbs. For emergency trades, B2B companies or anyone selling statewide, we’d keep the money on Google and Meta.</p>
<p>Most of what ranks for this question is out of date. Between 2024 and 2026, Local Deals was folded into a new ad flow, a paid lead product called Opportunity Alerts appeared, and in August 2026 Nextdoor stopped letting owners promote their businesses from personal accounts. This is how it works now for a business in The Woodlands, Spring, Conroe or elsewhere around Houston.</p>"""),

            ("How Nextdoor for Business works in 2026", f"""<p>Nextdoor sells four separate things to local businesses, and owners tend to blur them together.</p>
<ul>
<li><b>The free Business Page.</b> {SRC['local']} lists a Business Page, free Business Posts that appear in the neighborhood newsfeed, visibility in Search and Discover, and customer recommendations, all marked free.</li>
<li><b>Recommendations and Faves.</b> When a neighbor who has hired you vouches for you, that shows on your page as a Fave. Nextdoor’s {SRC['faves']} says more Faves raise a business’s position in search, and that neighbor-to-neighbor recommendations make up nearly 30% of all content on the platform.</li>
<li><b>Nextdoor Ads.</b> Self-serve feed ads, launched for small businesses in 2022. Local Deals now lives here as the “Promote a sale or discount” goal.</li>
<li><b>Opportunity Alerts.</b> A monthly subscription for home-service categories that texts or emails you when a nearby neighbor posts asking for your kind of service.</li>
</ul>
<!--fig:stats-->
<p>One rule change shapes everything else. In its {SRC['selfpromo']} dated August 19, 2026, Nextdoor said promotion “must be done from a free Business Page, not a personal neighbor account.” Plug your company in a “who does good fence work?” thread from your personal profile and the post can get flagged, which means fewer neighbors see it.</p>"""),

            ("Is a Nextdoor business page free?", f"""<p>Yes. Claiming, verifying and posting from a Business Page costs nothing. Nextdoor’s self-promotion update says verification takes about a minute, and freelancers and home-based businesses are welcome to set one up. Nextdoor’s Fave Awards release says nearly 6.6 million businesses have claimed a free page.</p>
<p>A few setup details that matter more than they look:</p>
<ol>
<li>Claim the existing page first. Neighbors may have created one when they recommended you, and a second page splits your recommendations.</li>
<li>Pick categories the way a neighbor would describe you. “Pool service” beats “aquatic maintenance solutions.”</li>
<li>Set a real service area. Business Posts use a radius you can widen or shrink, plus neighborhoods you pick. Include your own, or you won’t see your posts from your member account.</li>
<li>Upload photos of actual jobs in recognizable settings. A finished patio with pine trees behind it reads as local in The Woodlands in a way a stock photo never will.</li>
<li>Casual services such as dog walking need business documents to verify before posting to the nearby feed.</li>
</ol>
<p>Then ask 20 recent nearby customers for a recommendation. In month one, that does more than any ad budget will.</p>"""),

            ("How much does Nextdoor advertising cost?", f"""<p>Nextdoor doesn’t publish a rate card. You set a daily budget, and what you pay depends on reach and competition. {SRC['qc']} advertises budgets of “as little as $5/day,” and turning ads off means you’re only charged for impressions already served. The Ads Manager quickstart says bids are CPM or CPC depending on the objective you choose.</p>
<p>The billing setup depends on which door you walk through, which trips up a lot of owners:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Product</th><th>How you pay</th><th>Targeting</th></tr></thead>
<tbody>
<tr><td>Business Page and Business Posts</td><td>Free</td><td>Radius around your business, plus picked neighborhoods</td></tr>
<tr><td>Nextdoor Ads (simple setup from your business dashboard)</td><td>Daily budget, charged 30 days up front, then renews every 30 days until you cancel</td><td>Neighbors within up to 30 miles, adjusted with a slider</td></tr>
<tr><td>Nextdoor Ads Manager (ads.nextdoor.com)</td><td>Pay as you go: billed at a spending threshold or your monthly billing date</td><td>State, city, DMA or postal code, plus age, income, homeownership and interests</td></tr>
<tr><td>“Promote a sale or discount” (the old Local Deals)</td><td>Daily budget</td><td>ZIP codes (old neighborhood targets were converted to ZIPs)</td></tr>
<tr><td>Opportunity Alerts</td><td>Monthly subscription, price shown at checkout, cancel anytime</td><td>20-mile radius from an address you choose, up to 3 categories</td></tr>
</tbody></table></div>
<p>Sources: {SRC['broad']}, {SRC['howto']}, {SRC['deals']}, {SRC['nadc']} and the {SRC['alerts']}.</p>
<p>Watch the 30-day prepay on the simple flow. Set $15 a day there and $450 leaves your card on day one.</p>
<p>Ignore the old numbers floating around, like Local Deals “from $1” or Neighborhood Sponsorships at $32 a month. Those products were renamed or retired, and the per-lead ranges we’ve seen published cite no data.</p>
<p>For planning, we use $10 to $20 a day for one service in a handful of ZIP codes, or $600 to $1,200 over 60 days. That’s our working range from setting these up, not a Nextdoor figure.</p>"""),

            ("Is Nextdoor advertising worth it for your business? Who it fits", f"""<p>Nextdoor ads work when the buyer owns the house, plans a few days out and cares what the neighbors think. They fall flat when the buyer is in a hurry.</p>
<p>Nextdoor’s own products point the same way. Its {SRC['howto']} lists a Real Estate section placement for real estate and home services advertisers, and Opportunity Alerts covers 33 service categories from plumbing and roofing to movers and pet sitting.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Usually a good fit</th><th>Usually a poor fit</th></tr></thead>
<tbody>
<tr><td>Lawn care, landscaping, pool service, pest control, house cleaning</td><td>Emergency plumbing, water damage, lockouts (people search Google in a panic)</td></tr>
<tr><td>Remodelers, painters, fence and patio builders</td><td>B2B services, payroll, IT, commercial janitorial</td></tr>
<tr><td>Dog walkers, groomers, vets, pet sitters</td><td>Ecommerce brands shipping statewide or nationally</td></tr>
<tr><td>Neighborhood restaurants, bakeries, boutiques, fitness studios</td><td>Anything with an audience that skews under 25</td></tr>
<tr><td>Listing agents who farm specific subdivisions</td><td>Cannabis, CBD, tobacco and vape shops (barred by Nextdoor’s ad policy)</td></tr>
</tbody></table></div>
<p>Restaurants are a mixed case. A neighborhood-only offer can fill a slow Tuesday, but Google and Instagram usually matter more. Our <a href="/industries/restaurants/">restaurant marketing page</a> covers the rest of the mix.</p>
<p>Real estate needs one extra check. Nextdoor’s {SRC['policy']} says housing ads must not assert or imply that ZIP code, age, familial status or several other traits are relevant. Write about the home, never about who belongs there.</p>"""),

            ("Nextdoor ads vs Facebook ads (and Google LSA)", f"""<p>This one comes down to reach against context. Facebook and Instagram reach far more of your neighbors. Nextdoor reaches fewer of them, in a feed where people are already talking about their houses and asking who to hire.</p>
<!--fig:reach-->
<p>{SRC['pew']} found 71% of U.S. adults use Facebook and 50% use Instagram in 2025. Its latest Nextdoor figure is 13%, from 2021. Nextdoor reports 22.9 million platform weekly active users in its {SRC['q2']}, and its business pages claim one in three U.S. households is on the platform, with no footnote.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Nextdoor Ads</th><th>Facebook / Instagram ads</th><th>Google Local Services Ads</th></tr></thead>
<tbody>
<tr><td>What you pay for</td><td>Impressions or clicks from a daily budget</td><td>Impressions or clicks from a daily budget</td><td>Leads (calls, messages, bookings)</td></tr>
<tr><td>Buyer mindset</td><td>Browsing neighborhood news, often asking for referrals</td><td>Scrolling friends and entertainment</td><td>Searching right now</td></tr>
<tr><td>Local targeting</td><td>Radius, ZIP or postal code</td><td>Radius, ZIP, city (restricted for housing ads)</td><td>Service area you set</td></tr>
<tr><td>Audience size here</td><td>Smaller</td><td>Largest</td><td>Only people searching</td></tr>
<tr><td>Best for</td><td>Trust, repeat services, neighborhood offers</td><td>Volume, video, retargeting</td><td>Urgent home services</td></tr>
</tbody></table></div>
<p>For real estate the targeting gap is real. Meta’s housing special ad category, per {SRC['loomer']}, requires a 15-mile minimum radius and no ZIP targeting. Nextdoor’s published policy covers what housing ads say and doesn’t list a radius minimum. Check what your campaign settings actually allow before you build a plan on that gap.</p>
<p>For urgent jobs, Google wins easily. Nobody with a dead AC in August opens Nextdoor first. For that work, start with our breakdown of <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs Google Ads</a>. For the Meta side, see our guide to <a href="/blog/facebook-instagram-ads-local-businesses/">Facebook and Instagram ads for local businesses</a>. We’d rarely run Nextdoor on its own. It earns its spot as a third channel after Google and Meta are in good shape.</p>"""),

            ("Why Nextdoor may be unusually active in The Woodlands", f"""<p>This part is our hypothesis. Nextdoor doesn’t publish usage by city, and we haven’t found anyone who has for this area.</p>
<p>The reasoning goes like this. Nextdoor organizes around neighborhoods, and The Woodlands is already divided into named villages with their own associations: Grogan’s Mill, Panther Creek, Cochran’s Crossing and Indian Springs on the older east side, Alden Bridge, Sterling Ridge and Creekside Park to the west, per {SRC['harbert']}. People here say “I live in Sterling Ridge” the way people elsewhere name a street. Strong shared identity, lots of single-family owners and steady new arrivals are the conditions that produce “who do you use for…” posts.</p>
<!--fig:area-->
<p>The same pattern shows up in master-planned communities nearby. Grand Central Park in Conroe, for example, is a Johnson Development community of about 2,000 acres with more than 1,500 homes so far, and its final lots went to builders in early 2026, according to {SRC['gcp']}. New arrivals need a pest service, a pool company, a vet and a handyman, and they ask their neighbors first.</p>
<p>You can check it for your own category in ten minutes. Search the app for your category plus “recommend” and count the asks in your service area over the last 90 days. If you find several a week, Nextdoor deserves a test. If you find two all year, keep the free page and spend the money elsewhere. For businesses north of the county line, our <a href="/digital-marketing-agency-conroe-tx/">Conroe marketing page</a> covers the wider Montgomery County picture.</p>"""),

            ("A 60-day Nextdoor test plan with budget and tracking", f"""<p>Nextdoor’s dashboard reports impressions, clicks and messages, not booked jobs. Set up tracking before the first dollar goes out.</p>
<!--fig:test-->
<h3>The setup</h3>
<ul>
<li><b>A dedicated call tracking number</b> on the ad and on your Business Page. Our guide to <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking</a> explains how to do this without hurting your Google listing.</li>
<li><b>UTM tags on every link</b>, for example <i>?utm_source=nextdoor&amp;utm_medium=paid&amp;utm_campaign=sterling-ridge-fall</i>. Use utm_medium=organic for free Business Posts so you can compare the two.</li>
<li><b>A Nextdoor-only promo code</b> such as ND25. It catches the people who see the ad, then call your main number or walk in.</li>
<li><b>The Nextdoor pixel</b>, if you book online. Ads Manager can optimize toward conversions and now shows ROAS reporting, per Nextdoor’s {SRC['whatsnew']}.</li>
</ul>
<h3>The budget</h3>
<p>Say you run a two-crew lawn and landscape company in Alden Bridge. You’d run $15 a day for 60 days, about $900 total, aimed at five or six ZIP codes you can reach in 20 minutes. Keep one offer, say a fall aeration package, for the full test so you’re measuring the channel, not the creative.</p>
<h3>The scorecard</h3>
<p>At day 60, count booked jobs from the tracking number, UTM links and promo code, and divide $900 by that count. If Nextdoor lands within 30% of your best channel’s cost per booked job and the customers rebook, keep it. If it’s double, cut the ads and keep the free page.</p>
<p>We judge <a href="/blog/is-yelp-advertising-worth-it-small-business/">Yelp ads</a> the same way.</p>"""),

            ("What to post on Nextdoor for free", f"""<p>Free Business Posts land in the main newsfeed, the most visible part of the app. Write them the way a neighbor would and they can pull as well as a paid ad.</p>
<ul>
<li><b>Useful seasonal reminders.</b> “Hurricane season runs through November 30. Here’s the five-minute check we’d do on your gutters before the next storm.” No hard pitch.</li>
<li><b>Local job photos with permission.</b> A before-and-after from a street people recognize, with the homeowner’s okay and no house number showing.</li>
<li><b>Offers tied to a place.</b> A first-visit discount for Creekside Park only reads like it was meant for the reader. “10% off for new customers” reads like an ad.</li>
<li><b>Community stuff,</b> like a school fundraiser you sponsor.</li>
</ul>
<p>Skip daily posting, copy pasted from Facebook and all-caps “LIMITED TIME” offers. Neighbors mute that fast.</p>"""),

            ("Neighborhood etiquette and the risk of a negative thread", f"""<p>Nextdoor’s biggest risk comes from the same place as its value: people talk. A recommendation thread can send you four jobs in a week, and a complaint about a missed appointment can top a neighborhood feed for days. Our rules before spending a dollar:</p>
<ol>
<li><b>Reply from the Business Page, once, calmly.</b> “Thanks for flagging this, Jen. I’ve sent you a message so we can make it right.” Then fix it offline.</li>
<li><b>Never argue facts in public,</b> even when you’re right. Neighbors judge the tone, not the invoice.</li>
<li><b>Don’t ask friends to pile on.</b> Coordinated praise is obvious.</li>
<li><b>Don’t pay or discount for Faves.</b> Ask every happy customer, but don’t trade anything for it.</li>
<li><b>Watch threads weekly.</b> Search your business name in the app every Monday so a problem doesn’t sit unanswered.</li>
<li><b>Answer recommendation requests fast,</b> but only ones you actually fit.</li>
</ol>
<p>Paid ads put more eyes on those threads. If your crew is already behind on callbacks, fix that before you buy attention.</p>"""),

            ("Before you spend a dollar on Nextdoor", f"""<p>Do the free part tonight: the 90-day search for recommendation asks described above, plus claiming your page. If the asks are scarce, you’ve saved yourself $900 and kept a free listing. If they’re steady, run the 60-day test with its own number, UTMs and promo code. Our <a href="/services/paid-social-advertising/">paid social team</a> sets up Nextdoor next to Meta for <a href="/industries/service/">home service companies</a> across Greater Houston if you want help.</p>
<p>One warning about the scorecard. The day-60 comparison only works if the benchmark is honest, and Meta accounts are often the weak spot: a form that counts every open as a lead, or a campaign optimizing for cheap clicks instead of calls, makes Facebook look cheaper than it is and Nextdoor look worse. Before the test starts, request a free <a href="/contact/">Ad Spend Leak Check</a> on your Meta or Google account. We’ll record a walkthrough of what it’s really counting, so the number you compare Nextdoor against holds up.</p>"""),
        ],
        "faq": [
            ("Are Nextdoor business ads worth it?",
             "They can be for local businesses that serve homeowners nearby, such as lawn care, pool service, pest control, pet care and remodelers. They are rarely worth it for emergency services or B2B companies. Run a 60-day test with a dedicated call tracking number, UTM links and a Nextdoor-only promo code, then compare cost per booked job with Google and Meta before you commit."),
            ("How much does Nextdoor advertising cost?",
             "Nextdoor does not publish a rate card. You set a daily budget, and Nextdoor advertises starting points of about five dollars a day. The simple dashboard flow charges 30 days up front, while Ads Manager bills as you spend. For a meaningful local test we usually plan on ten to twenty dollars a day for about 60 days."),
            ("Is a Nextdoor business page free?",
             "Yes. Creating, claiming and verifying a Nextdoor Business Page is free, and so are Business Posts to the neighborhood feed and customer recommendations. Since August 2026, Nextdoor requires businesses to promote themselves from a Business Page rather than a personal account, so the free page is the starting point."),
            ("Do Nextdoor ads work better than Facebook ads?",
             "Not across the board. Facebook and Instagram reach far more people, so they usually win on volume. Nextdoor reaches a smaller audience already asking neighbors who to hire, which can mean better leads for home services. Test both with the same offer and tracking."),
            ("What is Nextdoor Opportunity Alerts?",
             "Opportunity Alerts is a paid monthly subscription for home service businesses. It sends a text or email when a nearby neighbor posts asking for your type of service, within a 20-mile radius of an address you choose and up to three categories. Nextdoor shows the price at signup and lets you cancel anytime. Track the jobs it produces like any other paid channel."),
        ],
        "figures": {
            "reach": {
                "type": "bars",
                "title": "Share of U.S. adults using each platform",
                "sub": "Pew Research Center surveys",
                "items": [["Facebook (2025)", 71, "71%"], ["Instagram (2025)", 50, "50%"], ["Nextdoor (2021)", 13, "13%"]],
                "highlight": [2],
                "note": "Source: Pew Research Center",
                "alt": "Bar chart comparing Facebook, Instagram and Nextdoor usage among U.S. adults, for judging whether Nextdoor advertising is worth it",
                "caption": f"Pew hasn’t published a newer Nextdoor figure, so that bar is dated. Data from {SRC['pew']}.",
            },
            "stats": {
                "type": "stats",
                "title": "Nextdoor by its own numbers",
                "stats": [["22.9M", "platform weekly active users, Q2 2026"], ["~30%", "of content is business recommendations"], ["6.6M", "businesses with a claimed page"]],
                "note": "Source: Nextdoor Q2 2026 results and 2026 Fave Awards release",
                "alt": "Stat tiles with Nextdoor weekly users, recommendation share and claimed business pages, context for Nextdoor ads in Houston",
                "caption": f"Company-reported figures from Nextdoor’s {SRC['q2']} and {SRC['faves']}.",
            },
            "area": {
                "type": "map",
                "title": "Where we’d test Nextdoor first",
                "sub": "Owner-heavy suburbs north of Houston",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Magnolia", "Kingwood"],
                "alt": "Map of The Woodlands, Spring, Conroe and nearby suburbs where a Nextdoor advertising test makes sense for local businesses",
                "caption": "A hypothesis based on village and master-planned community density, not Nextdoor usage data.",
            },
            "test": {
                "type": "steps",
                "title": "A 60-day Nextdoor ads test",
                "sub": "Judge it on booked jobs, not clicks",
                "steps": [
                    ["Claim and fill the page", "Real photos, categories neighbors use, your own neighborhood included."],
                    ["Collect recommendations", "Ask 20 nearby customers before spending anything."],
                    ["Wire up tracking", "Call tracking number, UTM links and a Nextdoor-only promo code."],
                    ["Run one offer", "Fixed daily budget on a few ZIP codes for the full 60 days."],
                    ["Score every lead", "Tag each call or message as booked, quote only, or junk."],
                    ["Compare and decide", "Cost per booked job against Google and Meta. Keep, trim or stop."],
                ],
                "alt": "Six-step 60-day plan for testing whether Nextdoor advertising is worth it for a business in The Woodlands",
                "caption": "Most owners skip the tracking step and end up judging Nextdoor on its own dashboard.",
            },
        },
    },
]
