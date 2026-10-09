"""Long-tail post: "how much is a billboard in houston" (static, digital, Blip self-serve, mobile trucks, CPM math).

Research: competitor pages (AdQuick Houston TX and Houston MO cost pages, AdQuick Houston DOOH, BillboardsIn,
Alluvit), Blip pricing, cost and city pages (Houston, Baytown, Conroe), Movia truck rates, AdQuick truck help
article, Houston Permitting Center off-premise sign page, Harris County Engineer sign rules, Billboard Insider and
Houston Heights Association on Houston's 1980 billboard ban, Houston City Council's June 2026 digital OOH
presentation and Community Impact's coverage, OAAA 2025 revenue (MediaPost), OAAA/Harris Poll digital billboard
survey, YouGov OOH effectiveness data, TTI 2025 most congested roadways (Spectrum News), TxDOT traffic count
maps, and AdWave's 2026 CTV CPM benchmark.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "aq": A("https://adquick.com/billboard-locations/texas/houston", "AdQuick’s Houston rate ranges"),
    "aqdooh": A("https://adquick.com/dooh-advertising/houston-tx", "AdQuick’s Houston digital out-of-home page"),
    "bbin": A("https://www.billboardsin.com/market/houston-texas/billboards/", "BillboardsIn"),
    "alluvit": A("https://www.alluvitmedia.com/billboard-advertising/tx/houston.php", "Alluvit Media"),
    "blipcost": A("https://www.blipbillboards.com/cost/", "Blip’s billboard cost guide"),
    "blippricing": A("https://www.blipbillboards.com/pricing/", "Blip’s pricing page"),
    "blipblog": A("https://www.blipbillboards.com/blog/how-much-does-digital-billboard-advertising-cost/", "Blip"),
    "blipbaytown": A("https://www.blipbillboards.com/billboard-locations/texas/baytown", "Blip’s Baytown page"),
    "blipconroe": A("https://www.blipbillboards.com/billboard-locations/texas/conroe/", "Blip’s Conroe page"),
    "movia": A("https://movia.media/?p=10659", "Movia’s published truck rates"),
    "aqtruck": A("https://help.adquick.com/en/articles/15961207-how-do-mobile-billboard-trucks-work-routes-pricing-and-booking", "AdQuick"),
    "hpc": A("https://www.houstonpermittingcenter.org/node/2251/printable/print", "Houston Permitting Center"),
    "hcounty": A("https://oce.harriscountytx.gov/About/Divisions/Permits/Permits-A-to-Z/Signs-Extra-Territorial-Jurisdiction-Scenic-Toll-Roads", "Harris County Engineering Department"),
    "bbi": A("https://billboardinsider.com/billboards-in-houston/", "Billboard Insider"),
    "hha": A("https://houstonheights.org/digital-billboards-coming-to-a-freeway-or-street-near-you", "Scenic Houston, via the Houston Heights Association"),
    "council": A("https://preflight.houstontx.gov/council/committees/econdev/20260617/houston_digital_OOH_presentation.pdf", "presentation to a City Council committee"),
    "ci": A("https://communityimpact.com/heights-river-oaks-montrose/government/houston-city-council-to-possibly-discuss-adding-digital-billboards-throughout-the-city/", "Community Impact"),
    "oaaa": A("https://www.mediapost.com/publications/article/413543/oaaa-reports-ooh-advertising-rose-36-in-2025.html", "OAAA, as reported by MediaPost"),
    "harris": A("https://oaaa.org/wp-content/uploads/2024/04/Digital-Billboard-Ads-4.29.2024.pdf", "a Harris Poll for the OAAA"),
    "yougov": A("https://yougov.com/en-us/articles/55200-ooh-effectiveness-americans-frequently-notice-out-of-home-advertising-many-act-on-what-they-see", "YouGov"),
    "tti": A("https://spectrumlocalnews.com/tx/austin/news/2025/11/25/most-congested-roadways-in-texas-2025", "Texas A&amp;M Transportation Institute’s 2025 list"),
    "txdot": A("https://www.txdot.gov/data-maps/traffic-count-maps.html", "TxDOT’s traffic count maps"),
    "ctv": A("https://adwave.com/resources/average-ctv-cpm-q2-2026", "AdWave’s 2026 benchmark, citing eMarketer"),
}

POSTS = [
    {
        "slug": "billboard-advertising-cost-houston",
        "title": "How Much Is a Billboard in Houston? Real 2026 Prices by Type",
        "seo_title": "How Much Is a Billboard in Houston? 2026 Costs",
        "desc": "How much is a billboard in Houston? 2026 prices for static, digital, Blip and mobile billboard trucks, plus CPM math and how to buy smart.",
        "category": "Paid ads",
        "icons": ["Google Ads", "YouTube", "Google Analytics"],
        "art": "b4",
        "hero": "billboard",
        "hero_alt": "Illustration of a highway billboard for a guide to how much a billboard costs in Houston in 2026",
        "related": ["streaming-tv-ads-worth-it-small-business", "geo-fencing-ads-target-customers-nearby", "call-tracking-which-ads-make-phone-ring"],
        "sections": [
            (None, f"""<p>So how much is a billboard in Houston? In 2026, a static bulletin on a major freeway like I-45, I-10 or the 610 Loop typically runs about $4,000 to $14,000 for a four-week period, an arterial poster about $1,200 to $3,800, and a slot on a digital board anywhere from roughly $1,800 to $18,000, according to {SRC['aq']}. Self-serve digital through Blip starts at a few dollars a day, and mobile billboard trucks usually price by the day.</p>
<p>Those ranges are wide for a reason. A board facing inbound traffic on the Katy Freeway and a poster on a side street in Pasadena are different products, even if both get called “a billboard.” And Houston adds a twist most cities don’t have: the city stopped permitting new billboards decades ago, so the good faces rarely go on sale.</p>
<p>We buy out-of-home for clients across the region, so this guide sticks to what you’ll actually be quoted and the questions that get you a better number.</p>"""),

            ("How much is a billboard in Houston? Prices by format", f"""<p>Nobody in Houston publishes a single rate card. Operators like Clear Channel Outdoor, OUTFRONT Media and Lamar quote each face individually. The public marketplaces are the closest thing to a price list.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Format</th><th>Typical cost (4 weeks)</th><th>Typical CPM</th><th>Where the number comes from</th></tr></thead>
<tbody>
<tr><td>Highway bulletin (14' x 48'), I-10, I-45, I-69, 610</td><td>$4,000 to $14,000</td><td>$4 to $8</td><td>AdQuick Houston ranges</td></tr>
<tr><td>Arterial poster (about 10'5" x 22'8")</td><td>$1,200 to $3,800</td><td>$5 to $10</td><td>AdQuick Houston ranges</td></tr>
<tr><td>Digital bulletin, premium freeway (shared rotation)</td><td>$4,500 to $18,000</td><td>$4 to $11</td><td>AdQuick Houston ranges</td></tr>
<tr><td>Digital bulletin, secondary road</td><td>$1,800 to $4,500</td><td>$4 to $9</td><td>AdQuick Houston ranges</td></tr>
<tr><td>Self-serve digital (Blip)</td><td>From about $0.01 per 8-second play, no minimum</td><td>Varies by board</td><td>Blip pricing page</td></tr>
<tr><td>Mobile billboard truck</td><td>$300 to $700 per day static, $700 to $1,800 per day digital</td><td>Varies by route</td><td>Movia published rates</td></tr>
<tr><td>Print and install for a static face</td><td>$400 to $1,200 per unit</td><td>n/a</td><td>AdQuick Houston ranges</td></tr>
</tbody></table></div>
<p>Other directories land in the same neighborhood. {SRC['alluvit']} puts the average Houston board at $5,544.74 per four-week period across 85 listed faces, with an average CPM of $3.02. {SRC['bbin']} estimates $3,500 a month for a bulletin, $1,500 for a poster and $800 for a junior poster. The rep’s quote on a specific face is the only number that matters.</p>
<!--fig:costs-->
<p>Billboards are usually sold in four-week periods, so a year is thirteen periods, not twelve. Budget accordingly.</p>"""),

            ("Billboard cost Houston: static bulletins and posters", f"""<p>Static is the classic printed vinyl board. You own the face 24 hours a day with nobody else in rotation, which is why it still makes sense for a business that wants to be the landmark at an exit.</p>
<p>Bulletins are the big 14-by-48-foot boards along the freeways. Posters are smaller, around 10 by 22 feet, and live on arterials and surface streets where traffic moves slower. A poster on FM 1960 or Westheimer can get read in a way a bulletin at 70 mph on the Hardy Toll Road never will.</p>
<p>Static pricing has a few extras that catch first-time buyers:</p>
<ul><li><b>Production.</b> You pay to print and hang the vinyl. Blip’s cost guide lists vinyl printing at $200 to $800 and installation or removal at $200 to $500, and AdQuick’s Houston page shows $400 to $1,200 per unit for print and install. Change your message three times a year and you pay three times.</li>
<li><b>Contract length.</b> Most operators want 12 weeks or more on static, and longer terms bring the price down. {SRC['blipcost']} says longer terms typically cut per-period prices by 10 to 20 percent.</li>
<li><b>Design.</b> Budget for someone who designs for a five-second read.</li></ul>
<p>We’d treat a static bulletin as a lease, because that’s basically what it is. If you haven’t tested your message on a digital board first, you’re betting several months of rent and a print bill on copy you’ve never seen work.</p>"""),

            ("How much does a digital billboard cost in Houston?", f"""<p>Digital boards are LED screens that rotate several advertisers. Your ad holds for about eight seconds, then the next advertiser’s ad comes up. You’re buying a share of the loop, not the whole board.</p>
<p>According to {SRC['blipcost']}, a typical digital face rotates one advertiser in every six to eight spots, and digital usually runs 20 to 40 percent more than a static board in the same spot. Do the math on an eight-slot loop of eight-second ads and your message comes up roughly every 64 seconds. If the board runs around the clock, that’s about 1,350 plays a day.</p>
<p>For that premium you skip print fees (AdQuick notes digital has no production charge), can swap creative mid-flight or by daypart, and usually commit to just four weeks, which makes digital the right place to test.</p>
<p>What you give up is certainty. A driver can pass during a car dealer’s eight seconds and never see yours.</p>
<p>Timing matters too. {SRC['aqdooh']} says CPMs during the Houston Livestock Show and Rodeo window carry a 20 to 40 percent premium. Booking a spring campaign? Lock it in before February.</p>"""),

            ("Billboard advertising cost Houston businesses can test: Blip and self-serve digital", f"""<p>With Blip, you upload your ad, pick boards on a map, set a daily budget and pay only when your ad plays. There’s no contract and no minimum, per {SRC['blippricing']}, which lists plays starting at $0.01 each.</p>
<p>In practice, Houston-area boards cost more than a penny. {SRC['blipbaytown']} estimates about 99 plays a day on a $20 budget, roughly 20 cents a play, and a 2022 article from {SRC['blipblog']} put a typical blip at about $0.30 depending on the board. Prices shift by time of day and how many other advertisers want that board.</p>
<p>The inventory is mostly suburban. Blip has location pages for Conroe, Spring, Tomball, Humble, Katy, Sugar Land, Pearland, Baytown, Pasadena and League City, among others. {SRC['blipconroe']} calls out I-45, SH-105 and SH-336, which is useful if your customers live in Montgomery County.</p>
<!--fig:where-->
<p>Picture a pizza place just off I-45 in Conroe. The owner puts $20 a day on two nearby boards from 4 to 7 p.m. on weekdays for a month, about $440 all in, with a message pointing people to the SH-105 exit. If dinner orders don’t budge, she’s out the cost of a slow Tuesday. A 12-week static contract would have cost ten times that to learn the same thing.</p>
<p>Self-serve has limits. You bid against other advertisers, you get fewer plays at rush hour when demand peaks, and you only see boards listed on the platform. We use it to learn, then buy direct once the numbers justify it.</p>"""),

            ("Mobile billboard truck Houston: what trucks cost", f"""<p>A mobile billboard truck is a box truck with printed or LED panels that drives your route or parks where crowds gather: Rodeo traffic around NRG, game days near Toyota Center, a grand opening on Market Street.</p>
<p>Trucks are quoted per campaign. {SRC['aqtruck']} says the price comes down to four things: number of trucks, number of days, hours per day and the route. Digital LED trucks cost more than static panels. {SRC['movia']} put static trucks at $300 to $700 per truck per day and digital at $700 to $1,800 per day. BillboardsIn lists Houston digital truck campaigns starting at $2,499.</p>
<p>Trucks make sense when you need a specific crowd for a few hours, like a trade show at the George R. Brown, or a spot with no billboard inventory. A truck stuck on 610 at 5 p.m. is just another truck. Ask the vendor for GPS route logs after the campaign, and ask how they handle parking. Rules vary by city and venue, so get that in writing.</p>"""),

            ("Why billboard space in Houston is scarce", f"""<p>National pricing guides skip this, and it explains most of what you’ll see in Houston quotes. This is one of the hardest places in the country to build a new billboard.</p>
<p>The city amended its sign code in 1980 to stop new billboard construction, and existing boards were grandfathered, according to {SRC['bbi']}. The {SRC['hpc']} still states plainly that no new permits are issued for billboards. The count fell from more than 13,000 in the 1980s to about 1,309 by around 2021, per {SRC['hha']}. Unincorporated Harris County is just as strict: the {SRC['hcounty']} says construction of all off-premise signage is prohibited in the county.</p>
<p>Digital is also off the table inside Houston for now. In June 2026, Clear Channel and OUTFRONT asked a City Council committee to allow existing printed billboards to convert to LED, with three structures removed for every one converted. Their {SRC['council']} called Houston “one of the last major U.S. cities” without digital billboards on its roadways. As of {SRC['ci']}’s report, no ordinance had been drafted.</p>
<p>For buyers, fixed supply keeps prices firm on the best freeway faces, and most digital inventory sits in suburban cities and nearby counties with their own sign rules. If a directory claims digital boards “inside the Loop,” ask for the exact location.</p>
<p>If council approves conversions, the industry’s own deck says the build-out would take several years.</p>"""),

            ("What drives billboard advertising cost in Houston", f"""<p>Price follows eyeballs. The Texas A&amp;M Transportation Institute’s 2025 ranking of the state’s most congested roads put four Houston segments in the top five, led by the West Loop (610), per {SRC['tti']}. Slow traffic means longer looks, and operators price that in.</p>
<p>Beyond traffic, five things move the quote:</p>
<ul><li><b>Corridor.</b> I-10/Katy Freeway, I-45 North, 610, US-59/I-69 and US-290 command the most. Beltway 8 and the Grand Parkway (SH-99) usually come in cheaper per face, and AdQuick’s DOOH page puts those bulletins a step below the inner freeways.</li>
<li><b>Traffic counts and impressions.</b> Operators quote impressions from Geopath audience data, which starts with traffic counts. You can sanity-check the raw volume yourself on {SRC['txdot']}.</li>
<li><b>Facing and read.</b> Right-hand read (passenger side) beats left. Inbound morning traffic beats outbound for some businesses and is worse for others.</li>
<li><b>Size and share.</b> Bulletin vs poster, and one of six in a digital loop costs more than one of eight.</li>
<li><b>Contract length and season.</b> Longer terms get discounts. Rodeo, the holidays and election season get premiums.</li>
</ul>
<p>Ask every rep for the face ID, the 4-week impressions, the audience data source and a photo of the board from the driver’s view. If they can’t send that, keep shopping.</p>"""),

            ("How to buy a Houston billboard without wasting money", f"""<p>This is the order we work in when a client asks us about <a href="/services/ctv-ooh-streaming-radio/">out-of-home and streaming</a>.</p>
<!--fig:buy-->
<h3>Do the CPM math first</h3>
<p>CPM is cost per thousand impressions: price divided by impressions, times 1,000. Say a rep quotes $5,000 for a bulletin on I-45 near Spring with 1.2 million impressions over four weeks. That’s about $4.17 per thousand. Cheap compared with almost any digital channel.</p>
<p>Now be honest about who’s in that traffic. If you sell kitchen remodels and one driver in five owns a home in your service area, your real cost per thousand people you care about is closer to $21. Still reasonable, but not the number on the proposal.</p>
<h3>Test on digital before you commit to static</h3>
<p>Run your message on two or three digital faces for four weeks. If branded searches and calls don’t move, a 12-month static contract won’t fix it.</p>
<h3>Write for five seconds</h3>
<p>Seven words or fewer, one image, and a name you can read from three lanes over. Skip the phone number; an exit number or short web address works better.</p>
<h3>Track it like any other ad</h3>
<ul><li>Use a vanity URL that only appears on the board, like yoursite.com/45, and redirect it to a page with UTM tags so it shows up in Google Analytics.</li>
<li>Give the board its own call tracking number. Our <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking guide</a> explains the setup.</li>
<li>Watch branded search volume in Google Ads and Search Console for the weeks before, during and after the flight.</li></ul>
<h3>Pair it with digital follow-up</h3>
<p>The sale happens later, on a phone. Back the board with <a href="/blog/geo-fencing-ads-target-customers-nearby/">geo-fenced mobile ads</a> in the same ZIP codes, retargeting for site visitors, and streaming TV in the same area so the board isn’t the only place they’ve seen your name. Data from {SRC['yougov']} shows 35 percent of U.S. adults have researched a product on their phone after seeing an out-of-home ad. If your <a href="/services/search-marketing/">Google Ads</a> aren’t catching that search, a competitor will.</p>"""),

            ("When billboards beat CTV or Google Ads, and when they don’t", f"""<p>Out-of-home is growing. U.S. OOH ad revenue hit a record $9.46 billion in 2025, up 3.6 percent, with digital making up 36.3 percent, per {SRC['oaaa']}. And {SRC['harris']} found 79 percent of consumers notice digital billboard ads. People do look up from the dashboard.</p>
<!--fig:stats-->
<p>Billboards tend to win when:</p>
<ul><li>Your customers are almost everyone driving a corridor: restaurants near an exit, urgent care, car dealers, injury law, large employers hiring.</li>
<li>You need directions as much as awareness (“Next exit, right on Woodlands Parkway”).</li>
<li>Your search and local SEO are already working, and you need more people to search for you by name.</li></ul>
<p>They lose when:</p>
<ul><li>Customers search when they have the problem. A broken AC in August is a Google search, not a billboard memory. Search ads catch intent a board can’t. See our <a href="/blog/google-ads-cost-per-click-houston-benchmarks/">Houston CPC benchmarks</a>.</li>
<li>Your audience is narrow, like B2B or a single ZIP code.</li>
<li>Your total marketing budget is under a few thousand dollars a month. One board can eat all of it.</li></ul>
<p>Against streaming TV, it’s a trade of price for precision. The average connected TV CPM is about $26, with most campaigns between $25 and $35, according to {SRC['ctv']}. That buys you a full-screen ad aimed at households in specific ZIP codes. A freeway board costs a fraction of that per thousand but reaches everyone. More in <a href="/blog/streaming-tv-ads-worth-it-small-business/">are streaming TV ads worth it for small businesses</a>.</p>"""),

            ("Your first move this week", f"""<p>Pick the one corridor your customers actually drive, say I-45 between Rayford Road and Woodlands Parkway, or the Grand Parkway through Cypress. Ask two operators for every available face on that stretch, with face IDs and four-week impressions. Then open a free Blip account and price two boards in the same area. Inside a day you’ll know whether a direct buy or a self-serve test makes more sense for your budget.</p>
<p>One more thing before you sign. Billboard money usually comes out of the same pot as your search budget, and the board will send people to Google looking for you. If that search spend is already leaking on junk clicks or out-of-area traffic, the billboard just feeds the leak. Our free <a href="/contact/">Ad Spend Leak Check</a> is a quick way to find out: a 10-minute recorded look at your Google or Meta account, back to you within 48 hours. When you’re ready to plan the board itself, in <a href="/digital-marketing-agency-houston-tx/">Houston</a>, <a href="/digital-marketing-agency-conroe-tx/">Conroe</a>, <a href="/digital-marketing-agency-katy-tx/">Katy</a> or elsewhere, our <a href="/services/ctv-ooh-streaming-radio/">CTV, OOH and radio team</a> buys and measures it.</p>"""),
        ],
        "faq": [
            ("How much does a billboard cost in Houston?",
             "A static freeway bulletin in Houston typically costs about $4,000 to $14,000 per four-week period, posters about $1,200 to $3,800, and digital rotations about $1,800 to $18,000, based on AdQuick's 2026 Houston ranges. Printing and installation add roughly $400 to $1,200 for each static face. Exact prices depend on the corridor, traffic and contract length."),
            ("How much does a billboard cost in Texas?",
             "It depends on the market. Large metros like Houston, Dallas and Austin run thousands of dollars per four-week period for a freeway board, while boards on rural highways can cost a few hundred dollars a month. Blip's cost guide puts rural highway boards at $250 to $750 a month and major-metro boards at $5,000 to $25,000."),
            ("Can you rent a billboard for one day in Houston?",
             "Not on most static boards, which are sold in four-week periods. You can buy single days on self-serve digital platforms like Blip, which charge per eight-second play with no minimum or contract, or book a mobile billboard truck for a day. Both are good ways to test a message before signing a longer contract."),
            ("How much is a mobile billboard truck in Houston?",
             "Mobile billboard trucks are usually quoted per truck per day. Published industry rates put static trucks at about $300 to $700 per day and digital LED trucks at about $700 to $1,800 per day. Total cost depends on the number of trucks, days, hours per day and route. Ask for GPS route reports after the campaign."),
            ("Are there digital billboards in Houston?",
             "Not inside Houston city limits. The city stopped new billboards in 1980 and does not allow digital displays on off-premise signs. In June 2026, outdoor companies asked City Council to allow conversions of existing boards to LED, but no ordinance had been drafted. Most digital boards in the region sit in suburban cities and nearby counties."),
        ],
        "figures": {
            "costs": {
                "type": "bars",
                "title": "Houston billboard cost per 4 weeks",
                "sub": "Midpoint of typical 2026 ranges, by format",
                "items": [
                    ["Premium digital freeway slot", 11250, "$4.5K–$18K"],
                    ["Static freeway bulletin", 9000, "$4K–$14K"],
                    ["Secondary digital slot", 3150, "$1.8K–$4.5K"],
                    ["Arterial poster", 2500, "$1.2K–$3.8K"],
                    ["Print and install (static)", 800, "$400–$1.2K"],
                ],
                "highlight": [1],
                "note": "Source: AdQuick Houston rate ranges",
                "alt": "Bar chart of how much a billboard costs in Houston per four weeks for digital, static bulletins and posters",
                "caption": "Ranges are wide because corridor and traffic drive the price; always get a quote on the exact face.",
            },
            "where": {
                "type": "map",
                "title": "Where self-serve digital boards are listed",
                "sub": "Houston-area cities with Blip location pages",
                "highlight": ["Conroe", "Spring", "Tomball", "Humble", "Katy", "Sugar Land", "Pearland", "Baytown", "League City"],
                "alt": "Map of Houston-area suburbs with self-serve digital billboard listings, including Conroe, Spring, Katy and Pearland",
                "caption": "Houston and unincorporated Harris County ban new billboards, so most digital faces sit in suburban cities.",
            },
            "buy": {
                "type": "steps",
                "title": "How to buy a billboard in Houston",
                "sub": "Our order of operations for a first campaign",
                "steps": [
                    ["Fix search first", "Make sure Google Ads and your Business Profile catch people who look you up."],
                    ["Get three quotes", "Ask for face IDs, 4-week impressions, data source and a driver’s-view photo."],
                    ["Run the CPM math", "Divide price by impressions, then adjust for how much traffic fits your customer."],
                    ["Test digital for 4 weeks", "Use Blip or a short direct buy before any long static contract."],
                    ["Track and follow up", "Vanity URL, tracking number, geo-fenced mobile and CTV in the same ZIPs."],
                ],
                "alt": "Five steps to buy a billboard in Houston, from fixing search to testing digital and tracking results",
                "caption": "A cheap four-week test tells you more than any rep’s impression estimate.",
            },
            "stats": {
                "type": "stats",
                "title": "Do people actually notice billboards?",
                "stats": [
                    ["79%", "of consumers notice digital billboard ads (Harris Poll for OAAA)"],
                    ["35%", "of U.S. adults researched a product on their phone after an OOH ad (YouGov)"],
                    ["36.3%", "of 2025 U.S. out-of-home revenue came from digital (OAAA)"],
                ],
                "note": "Sources: OAAA/Harris Poll, YouGov, OAAA via MediaPost",
                "alt": "Stat tiles showing billboard attention and phone research rates relevant to billboard advertising in Houston",
                "caption": f"Attention turns into phone searches, which is why billboards work best next to search ads ({A('https://yougov.com/en-us/articles/55200-ooh-effectiveness-americans-frequently-notice-out-of-home-advertising-many-act-on-what-they-see', 'YouGov')}).",
            },
        },
    },
]
