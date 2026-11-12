"""Batch 11 (CPG vertical): driving retail sell-through after a grocery launch (Kroger, H-E-B, Walmart), and
compliant creator marketing for beverage and supplement brands.

Research, retail post: Grocery Dive on Kroger Precision Marketing's September 2025 managed offsite expansion
(programmatic CTV via Roku, Samsung and others; audio via Pandora, iHeartRadio; measurement of ROAS, household
penetration, uplift); 84.51° press release on KPM's in-house self-service platform (June 28, 2023; product listing
ads and onsite display; 75% of targeted onsite display impressions/clicks from new-to-brand households); Epsilon
press release on H-E-B Retail Media self-service (June 11, 2025; promoted products on heb.com and the My H-E-B app;
onsite, offsite, in-store, email; 8M+ households weekly; 455+ stores in Texas and Mexico); Walmart Connect goals
page (Sponsored Products, Sponsored Brands, Sponsored Videos, Onsite Display, Offsite media, Store ads, Brand Shop
and Shelf, closed-loop measurement); Walmart corporate on VIZIO (acquired 2024) at Cannes 2026; Supermarket News on
the FTC's 2003 slotting report (under $1M to over $2M for a national launch; one in ten ice cream items short of
first-year fees); Shelby Report on H-E-B's 2026 Quest for Texas Best (13th year, 978 entries, 500+ companies,
$50,000 grand prize, shelf placement); Shelby Report on Kroger's combined Texas division (207 supermarkets, Aug. 1,
2025 merger of Dallas and Houston divisions); Mass Market Retailers on Kroger's planned Hockley Marketplace store
(early 2028, first new Houston-area store in 10 years); Big Eye Agency on Meta drop-pin radius (1 to 50 miles);
TABC marketing practices FAQ on cooperative advertising.
Creator post: FTC Endorsement Guides FAQ ("What People Are Asking," 2023 revision); Keller and Heckman on the Nov.
13, 2023 FTC warning letters to AmeriBev, the Canadian Sugar Institute and a dozen influencers; Covington on the
FTC Health Products Compliance Guidance (Dec. 20, 2022, replacing the 1998 supplement guide; RCT standard);
Mintz on April 2023 notices of penalty offenses to ~670 advertisers; FDA structure/function claims page; FDA
caffeine consumer update (400 mg/day; 54-328 mg per 16 oz in energy drinks); American Beverage Association energy
drink guidance (no marketing to children under 12, no K-12, advisory statement, total caffeine, no mixing with
alcohol); TTB industry circulars list and the Nov. 1, 2024 Industry Circular 2024-1 on social media; Beer
Institute/Brewers Association 73.6% audience standard (July 2022); DISCUS 73.8% (2023); Sprout Social on Meta's 18
floor and 21+ setting for U.S. alcohol; Marketing Brew and TikTok's alcohol policy (U.S. ads to 25+, no people
under 25, responsible drinking message); Fast Company on TikTok alcohol creator content arriving in early 2026;
Meta unsafe supplements policy; Meta health and wellness policy (18+); TikTok weight management policy; TikTok
Spark Ads authorization (7, 30, 60 or 365 days); Morgan Lewis on the FTC consumer reviews and testimonials rule.
Left out (could not verify current status): Kroger's Go Fresh & Local accelerator in 2026; hemp-THC beverage
rules in Texas; Meta's current treatment of non-alcoholic beer.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # retail post
    "kpm_offsite": A("https://www.grocerydive.com/news/kroger-precision-marketing-offsite-programmatic-advertising-retail-media/760993/", "Grocery Dive"),
    "kpm_platform": A("https://www.8451.com/press-releases/kroger-precision-marketing-builds-in-house-advertising-platform-to-power-the/", "84.51°’s announcement"),
    "heb_rm": A("https://www.epsilon.com/us/about-us/pressroom/h-e-b-launches-new-self-service-capabilities", "H-E-B Retail Media’s self-service announcement"),
    "wmc": A("https://www.walmartconnect.com/goals", "Walmart Connect’s own product list"),
    "vizio": A("https://corporate.walmart.com/news/2026/06/23/walmart-connect-at-cannes-lions", "Walmart’s Cannes 2026 recap"),
    "slotting": A("https://supermarketnews.com/grocery-operations/slotting-fees-can-top-2-million-ftc", "Supermarket News’ summary of the FTC’s slotting report"),
    "qftb": A("https://theshelbyreport.com/2026/10/12/sol-dias-ice-cream-wins-grand-prize-in-h-e-bs-2026-quest-for-texas-best/", "The Shelby Report"),
    "kroger_tx": A("https://theshelbyreport.com/2026/02/20/the-past-70-years-strong-kroger-texas-division-paves-path-of-progress", "207 supermarkets"),
    "hockley": A("https://massmarketretailers.com/kroger-plans-first-new-houston-area-store-in-a-decade/", "first new Houston-area store in a decade"),
    "radius": A("https://www.bigeyeagency.com/insights/geographic-targeting-for-meta-ads-guide-2026", "anywhere from 1 to 50 miles"),
    "tabc": A("https://www.tabc.texas.gov/faqs/alcohol-marketing-practices-faqs/", "TABC’s marketing practices FAQ"),
    # creator post
    "ftc_faq": A("https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking", "FTC’s Endorsement Guides FAQ"),
    "ftc_letters": A("https://www.khlaw.com/insights/ftc-warns-two-trade-associations-and-12-online-influencers-better-disclose-financial", "Keller and Heckman’s write-up"),
    "hpcg": A("https://www.cov.com/en/news-and-insights/insights/2023/01/ftc-issues-new-guidance-on-health-related-claims-to-replace-the-dietary-supplements-advertising-guide", "Covington’s summary of the guidance"),
    "nopo": A("https://www.mintz.com/insights-center/viewpoints/2191/2023-04-13-ftc-sends-notice-potential-penalties-approximately-670", "notices of penalty offenses"),
    "fda_sf": A("https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/structurefunction-claims", "FDA’s structure/function claims page"),
    "fda_caf": A("https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much", "FDA"),
    "aba": A("https://www.americanbeverage.org/files/resources/2014-energy-drinks-guidance-approved-by-bod-43020c.pdf", "American Beverage Association’s energy drink guidance"),
    "ttb_ic": A("https://www.ttb.gov/advertising/industry-circulars", "TTB’s industry circulars"),
    "ttb_2024": A("https://www.ttb.gov/public-information/featured-stories/ttb-issues-updated-industry-circular-use-social-media", "Industry Circular 2024-1"),
    "bi": A("https://www.beerinstitute.org/press-releases/beer-institute-and-brewers-association-revise-advertising-standards-based-on-updated-u-s-census-data/", "73.6%"),
    "discus": A("https://advertisinglaw.fkks.com/post/102ig73/discus-raises-adult-demographic-placement-standard-to-73-8", "73.8%"),
    "sprout": A("https://sproutsocial.com/insights/social-media-alcohol-marketing/", "Sprout Social’s rundown"),
    "tt_alc": A("https://ads.tiktok.com/help/article/tiktok-ads-policy-alcohol?lang=en", "TikTok’s alcohol ad policy"),
    "mbrew": A("https://www.marketingbrew.com/stories/2024/08/12/tiktok-allow-alcohol-advertisers-where-are-they", "Marketing Brew"),
    "fastco": A("https://www.fastcompany.com/91533064", "Fast Company"),
    "meta_unsafe": A("https://transparency.meta.com/policies/ad-standards/dangerous-content/unsafe-supplements", "unsafe supplements policy"),
    "meta_health": A("https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness", "health and wellness policy"),
    "tt_weight": A("https://ads.tiktok.com/help/article/tiktok-ads-policy-weight-management", "weight management policy"),
    "spark": A("https://ads.tiktok.com/help/article/how-to-create-spark-ads-for-smart-campaigns-on-tiktok-ads-manager", "TikTok’s Spark Ads instructions"),
    "partner": A("https://help.instagram.com/ipad-app/1168446653551639", "Instagram’s partnership ads help page"),
    "reviews": A("https://www.morganlewis.com/pubs/2024/08/ftc-issues-final-rule-on-consumer-reviews-and-testimonials", "consumer reviews and testimonials rule"),
}

RETAIL = "/blog/cpg-retail-launch-sell-through-kroger-heb/"
CREATOR = "/blog/beverage-supplement-marketing-creators-claims/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: retail sell-through
    {
        "slug": "cpg-retail-launch-sell-through-kroger-heb",
        "title": "Launching a CPG Brand at Retail: How to Drive Sell-Through at Kroger, H-E-B and Other Grocers",
        "seo_title": "CPG Retail Launch: Drive Sell-Through at Kroger & H-E-B",
        "desc": "How CPG brands drive sell-through after landing Kroger, H-E-B or Walmart: velocity math, retail media, geo-targeted social, store locators, demos and lift.",
        "category": "Strategy",
        "icons": ["Meta", "Google Ads", "Google Analytics"],
        "art": "b5",
        "hero": "cart",
        "hero_alt": "Illustration of a grocery cart for CPG retail launch marketing and sell-through at Kroger and H-E-B in Houston",
        "related": ["geo-fencing-ads-target-customers-nearby", "streaming-tv-ads-worth-it-small-business", "measure-marketing-success-metrics"],
        "sections": [
            (None, f"""<p>It’s a Tuesday in March and your broker forwards the first scan report. You’re in 140 stores across the Houston area. The four-pack is doing 0.7 units per store per week, which sounds fine until the broker reminds you the buyer wants roughly double that before the next category review. Thirty-one stores show zero sales in week two. Two of them, you find out later, never set the planogram.</p>
<p>(Illustrative numbers. The shape of the problem is real.)</p>
<p>Everyone told you getting the shelf was the hard part. It’s half of it. Once you’re in, the retailer gives you a few months to prove the item earns its slot, and the only proof it accepts is units moving through the register.</p>
<p>Driving sell-through at Kroger, H-E-B and other grocers comes down to three jobs in the first 26 weeks: make sure the product is actually on the shelf in every store that took it, send shoppers to those specific stores, and show the buyer the lift came from you. Retail media, geo-targeted social, store locator pages, demos and digital coupons are the tools. Velocity is the scoreboard.</p>
<p>We’ve run campaigns for {L('/case-studies/kroger/', 'Kroger itself')} and for {L('/case-studies/celsius/', 'Celsius')} when it needed sell-through at big-box retailers, so this is written from both sides of the shelf.</p>"""),

            ("Velocity is the number your buyer actually reads", f"""<p>Your buyer manages a category, not your brand. Every item in the set gets ranked, and the bottom of the list is where the next new item’s space comes from. You need to know the same numbers the buyer sees, defined the same way.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Formula</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Units per store per week (U/S/W)</td><td>Units sold ÷ (stores scanning × weeks)</td><td>The headline velocity number. Compared directly with the items next to you.</td></tr>
<tr><td>%ACV distribution</td><td>All-commodity volume of stores carrying you ÷ ACV of all stores in the market</td><td>Weights stores by size. Being in the 20 biggest stores beats being in 40 small ones.</td></tr>
<tr><td>Sales per point of distribution ($/SPP)</td><td>Dollar sales ÷ %ACV</td><td>Velocity that doesn’t get distorted as you add stores. Brokers and investors like it.</td></tr>
<tr><td>In-stock rate</td><td>Stores with product on shelf ÷ stores authorized</td><td>A store with no product on the shelf drags your average down for reasons no ad can fix.</td></tr>
<tr><td>Base vs. promo velocity</td><td>U/S/W in non-promo weeks vs. promo weeks</td><td>Buyers discount items that only move on deal.</td></tr>
<tr><td>Repeat rate</td><td>Households buying 2+ times ÷ households buying once</td><td>Trial without repeat looks great for eight weeks and then falls off a cliff.</td></tr>
</tbody></table></div>
<p>Two things trip up first-time brands. Adding stores mid-quarter usually pulls U/S/W down, because new stores ramp slowly and the denominator jumps right away. And a handful of zero-scan stores can sink an otherwise healthy average, so the first job is always finding out why those stores are at zero. Usually it’s an unset planogram, product stuck in the back room, or an out-of-stock on the distributor side. None of that shows up in Ads Manager.</p>
<!--fig:funnel-->"""),

            ("Before you spend on ads: slotting, set dates and the promo calendar", f"""<p>Grocery shelf space has always cost money. When the FTC studied slotting allowances back in 2003, it found fees for a national new-product introduction could run from a little under $1 million to more than $2 million, and about one in ten ice cream items didn’t earn enough in their first year to cover their fees, per {SRC['slotting']}. Regional deals are smaller and often mix cash, free fill and promotional commitments. Your broker will know the current terms for your category. What matters for marketing is that you’ve already paid to be there, so wasting the first eight weeks hurts twice.</p>
<p>Three things to lock down before any media goes live:</p>
<ul>
<li><b>The set date.</b> Ads that run before the planogram resets send people to a shelf that doesn’t have you yet. Get the reset window in writing and start paid media a week after it, not on it.</li>
<li><b>Set verification.</b> Send someone (a merchandising service, a rep, or you in your car) to walk a sample of stores in the first two weeks and photograph the shelf. Spring, The Woodlands, Katy and Pearland stores in one Saturday is doable. If 15% of stores didn’t set, you want to know before you buy geo-targeted ads around them.</li>
<li><b>The promo calendar.</b> Temporary price reductions, digital coupons and ad circular features are planned well ahead. Line your heaviest media weeks up with your promo weeks. In accounts we’ve run, a geo-targeted push during a price-reduction week moves noticeably more units than the same spend at full shelf price.</li>
</ul>
<p>If you’re a Texas brand still trying to get in, H-E-B’s Quest for Texas Best is a real path. The 2026 edition, the program’s 13th, drew a record 978 entries from more than 500 companies, and the grand prize winner got $50,000 plus placement on H-E-B shelves, according to {SRC['qftb']}.</p>"""),

            ("Retail media networks: Kroger Precision Marketing, H-E-B Retail Media and Walmart Connect", f"""<p>Retail media is advertising sold by the retailer, using the retailer’s shopper data, and measured against the retailer’s own sales. Buyers notice who spends in their network. That’s not supposed to affect category decisions, and nobody says it out loud, but it doesn’t hurt.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Network</th><th>What you can buy</th><th>What it reports</th></tr></thead>
<tbody>
<tr><td>Kroger Precision Marketing (KPM), powered by Kroger’s data arm 84.51°</td><td>Product listing ads and onsite display through an in-house self-service platform, per {SRC['kpm_platform']}. Since September 2025, managed-service offsite CTV (Roku and Samsung among the partners) and audio (Pandora, iHeartRadio), per {SRC['kpm_offsite']}.</td><td>ROAS, household penetration, uplift, and dollar and unit sales effects.</td></tr>
<tr><td>H-E-B Retail Media</td><td>Self-service promoted-product campaigns on heb.com and the My H-E-B app since June 2025, plus onsite, offsite, in-store and email placements. H-E-B says the network reaches more than 8 million households weekly across 455-plus stores in Texas and Mexico, per {SRC['heb_rm']}.</td><td>Always-on reporting on sales, CPC and click-through rate, with pacing by time period.</td></tr>
<tr><td>Walmart Connect</td><td>Sponsored Products, Sponsored Brands, Sponsored Videos and Onsite Display, plus Offsite media, Store ads and Brand Shop and Shelf for larger advertisers, per {SRC['wmc']}. Walmart also owns VIZIO, which powers its CTV offering, per {SRC['vizio']}.</td><td>Closed-loop measurement from impression to purchase.</td></tr>
</tbody></table></div>
<p>Where we’d start with a small budget: sponsored product ads on your own items for the category searches shoppers type into the retailer’s app (“sparkling water,” “protein bar,” “electrolyte powder”). Pickup and delivery shoppers search; they don’t browse aisles. If a competitor’s sponsored listing sits above yours on “energy drink” in the H-E-B app, you’re losing trial you already paid slotting for.</p>
<p>Two cautions. First, a retail media report sees every purchase in the loyalty data, so it can claim credit for shoppers who would have bought anyway. Kroger has reported that 75% of targeted onsite display impressions and clicks in a study of thousands of campaigns came from new-to-brand households. That’s Kroger’s own measurement, and it’s still worth asking your rep for new-to-brand and incremental numbers on your campaign specifically. Second, retail media dollars often come out of the same trade budget as your promotions. Decide the split on purpose.</p>"""),

            ("Geo-targeted social around the stores that carry you", f"""<p>Retail media reaches people already shopping the retailer. Social reaches the people who haven’t heard of you yet and live two miles from a store that has you. That second group is where new households come from.</p>
<p>How we set it up:</p>
<ol>
<li><b>Get the authorized store list.</b> Store numbers and addresses for every location that took the item, from your broker or distributor. Then remove the stores you couldn’t verify.</li>
<li><b>Build location targeting.</b> In Meta Ads Manager, go to the ad set, then Audience, then Locations, and drop pins on each address (or add them in bulk). Meta lets you set a radius {SRC['radius']}. In suburban Houston, two to three miles around a store in Cypress or Kingwood is a reasonable start. Inside the Loop, one mile.</li>
<li><b>Split ad sets by retailer.</b> Kroger stores in one ad set, H-E-B in another, so the creative can name the right store and you can read results by banner.</li>
<li><b>Write the creative to send them somewhere specific.</b> “Now at H-E-B. Cold drinks aisle, next to the sparkling water.” Name the store, show the package on the shelf, and give one reason to try it. Vague awareness creative wastes the precision you just paid for.</li>
<li><b>Mirror it on Google.</b> Search campaigns on “[brand] near me,” “where to buy [brand]” and “[brand] H-E-B,” with the same radius targeting, sending clicks to your store locator.</li>
</ol>
<p>That’s close to what we ran for Celsius: geo-fenced paid social and search around big-box stores in priority DMAs, “find it near you” ads pointing at live store-locator pages, and weekly sell-through data fed back into spend by region. Across 2,850 geo-targeted stores, sell-through in target regions rose 41%, store-locator visits rose 3.4x and cost per store visit fell 37%. The full write-up is in the {L('/case-studies/celsius/', 'Celsius case study')}, and our {L('/blog/geo-fencing-ads-target-customers-nearby/', 'geo-fencing guide')} covers the targeting mechanics.</p>
<p>Two rules to check first. Ask your buyer before you put the retailer’s logo in an ad; many chains have brand guidelines and some would rather you run that kind of work through their own network. And if you sell beer, wine or spirits in Texas, read {SRC['tabc']} before running anything that names a store. TABC treats supplier advertising that promotes a specific retailer as an illegal inducement, while still letting upper-tier members advertise where their products are sold. That line matters for “find it at” ads, so get it reviewed.</p>
<!--fig:map-->"""),

            ("Store locator pages that send people to a shelf", f"""<p>Every geo ad and every “where to buy” search ends at your store locator, and most CPG store locators are bad. They show every store a distributor ever shipped to, including ones that dropped you last year, and they don’t say which flavors are where.</p>
<p>A store locator that earns its keep:</p>
<ul>
<li>Uses current store-level data. Retailer point-of-sale data through your data provider is best, distributor data is second, and a hand-kept list updated weekly is better than nothing.</li>
<li>Shows the three nearest stores with distance, which SKUs each carries, and where in the store to look.</li>
<li>Links to the product page on the retailer’s pickup and delivery site, so “add to cart” is one tap from your ad.</li>
<li>Shows any live digital coupon with a link to clip it.</li>
<li>Has retailer pages (/where-to-buy/heb/, /where-to-buy/kroger/) that can rank for “[brand] at H-E-B” searches.</li>
<li>Fires tracked events on “get directions,” “shop online” and “clip coupon,” which become your conversion events in Meta and Google Ads.</li>
</ul>
<p>Those three events are the closest thing a CPG brand has to a lead. Tracking them properly lets the ad platforms optimize toward shoppers who looked for a store, not people who watched three seconds of a video. If your site needs the work, that’s part of our {L('/services/web-design-seo-pr/', 'web and SEO service')}.</p>
<p>Online pickup orders count too. The Kroger campaign we ran used recipe creators to drive straight into Kroger pickup and delivery, with every ingredient a tap away. Shoppers who can buy the whole recipe in one cart don’t have to remember your brand name in aisle nine.</p>"""),

            ("Demos and sampling still move product", f"""<p>Some people won’t buy a $3.49 drink they haven’t tasted. A Saturday demo still converts better than almost anything you can buy online, and the effect shows up in that store’s scan data the same week.</p>
<p>Most grocery demos run through demo companies the retailer approves, so your broker or the retailer’s supplier portal is where you start. A few things we’d do differently from most brands:</p>
<ul>
<li><b>Pick demo stores by upside, not convenience.</b> Big-ACV stores with decent foot traffic and weak current velocity. The store closest to your office is rarely the right one.</li>
<li><b>Run geo ads around the demo store for three days.</b> “Try it free Saturday at Kroger in Spring, 11 to 3.” A two-mile radius, a small budget, real foot traffic.</li>
<li><b>Plan for Houston weather.</b> Cold samples in July sell beverages. A sampling table outside the entrance in August doesn’t. Keep demos inside, near the cooler.</li>
<li><b>Measure every demo.</b> Compare the demo store’s next four weeks with a similar store that didn’t get one. If demos don’t show lift, stop paying for them.</li>
</ul>
<p>Event sampling (a 5K in The Woodlands, a youth tournament in Katy) builds awareness. It only drives sell-through when the nearest stores have product and your locator tells people where they are.</p>"""),

            ("Digital coupons and the promo stack", f"""<p>Kroger and H-E-B both run digital coupons that shoppers clip in the app and redeem with their loyalty account. For a launch, a digital coupon does three things at once: it lowers the trial barrier, it puts your item in front of shoppers browsing coupons, and every redemption lands in the retailer’s data with a household attached.</p>
<p>Brands usually fund these through the retailer’s media network or a coupon partner, and your rep can tell you the current formats and minimums. A few rules from experience:</p>
<ul>
<li>Pair the coupon with your geo ads. “Clip $1 off in the Kroger app” gives the ad a reason to act today.</li>
<li>Use modest values for trial. Deep discounts teach people to wait for the next deal, and your buyer reads base velocity separately from promo velocity.</li>
<li>Don’t stack a coupon, a price reduction and a demo in the same week unless you want a spike you can’t explain. Space them out so you can tell which one worked.</li>
</ul>"""),

            ("Measuring lift so the buyer believes it", f"""<p>Your buyer has seen plenty of decks claiming a campaign “drove awareness.” What gets attention is a clean test: stores that got the media against similar stores that didn’t.</p>
<p>The setup we use:</p>
<ol>
<li>Split the authorized stores into test and control groups matched on pre-launch traffic, store size and neighborhood. For a Houston rollout, that might be Spring, Tomball and Atascocita stores as the test group, with comparable stores in Pearland and League City held out.</li>
<li>Run the geo-targeted media only around test stores for six to eight weeks.</li>
<li>Calculate lift as (test post ÷ test pre) ÷ (control post ÷ control pre) − 1, on U/S/W.</li>
<li>Cross-check with the retailer network’s own sales-lift reporting and with Meta’s Experiments tool if you’re running a conversion lift study.</li>
</ol>
<!--fig:lift-->
<p>This is how we approached the Kroger work. It ran a recipe-creator program, digital billboards near stores in 38 markets and CTV and streaming radio bought by DMA, then measured store visits. The result was a 24% store-visit lift on 212 million impressions, with a 97% completion rate on CTV. The {L('/case-studies/kroger/', 'Kroger case study')} has the details. A brand can run the same logic at a smaller scale: one city, a few dozen stores, two months.</p>
<!--fig:kroger-->
<p>Put the result on one page for the buyer: velocity in test vs. control, in-stock rate, base vs. promo, new households if the network gives you that, and what you’ll do next quarter.</p>"""),

            ("A 26-week launch plan, with budget pacing", f"""<p>Here’s how we’d pace a regional grocery launch from eight weeks before the set date through the first review.</p>
<!--fig:plan-->
<div class="bp-tbl"><table>
<thead><tr><th>Phase</th><th>Weeks</th><th>Share of launch budget</th><th>Main channels</th></tr></thead>
<tbody>
<tr><td>Prep</td><td>-8 to 0</td><td>5%</td><td>Store locator, creative, coupon booking, retail media plan</td></tr>
<tr><td>Verify</td><td>0 to 2</td><td>5%</td><td>Store walks, retailer search ads on your own items</td></tr>
<tr><td>Trial push</td><td>2 to 8</td><td>45%</td><td>Geo social, search, retail media, demos, first digital coupon</td></tr>
<tr><td>Optimize</td><td>8 to 16</td><td>30%</td><td>Shift spend to responding store clusters, CTV burst on promo weeks</td></tr>
<tr><td>Repeat and review</td><td>16 to 26</td><td>15%</td><td>Retargeting past locator visitors, second coupon, buyer recap</td></tr>
</tbody></table></div>
<p>The percentages are illustrative. The point is to front-load: the trial window decides whether you get a second year, and money saved for month six doesn’t help if the item’s already on the discontinue list. If you’re adding streaming or billboards, our posts on {L('/blog/streaming-tv-ads-worth-it-small-business/', 'streaming TV ads')} and {L('/blog/billboard-advertising-cost-houston/', 'Houston billboard costs')} cover pricing.</p>
<p>Houston is a good place to run this. Kroger’s combined Texas division runs {SRC['kroger_tx']} across north, east and southeast Texas and southwest Louisiana, and is planning its {SRC['hockley']} in Hockley. H-E-B has deep coverage across the region too. Two big grocers in one metro gives you a natural comparison between banners.</p>"""),

            ("Mistakes we see on CPG launches", f"""<ul>
<li><b>Spending on national awareness for a regional shelf.</b> If you’re in 140 Houston stores, a national TikTok campaign mostly reaches people who can’t find you.</li>
<li><b>Running ads before the set.</b> The planogram date slips more often than anyone admits.</li>
<li><b>Ignoring zero-scan stores.</b> Fix distribution first. Ads can’t sell product sitting in a back room.</li>
<li><b>Judging social by clicks to the homepage.</b> Optimize for locator actions and retailer cart clicks.</li>
<li><b>Treating retail media as the whole plan.</b> It harvests demand well and creates less of it.</li>
<li><b>No control group.</b> Without one, every result is an argument.</li>
</ul>
<p>Our {L('/industries/beverage-spirits/', 'beverage')} and {L('/industries/ecommerce/', 'eCommerce and CPG')} pages show the kinds of brands we work with, and if you’re planning creator content for the launch, read our companion piece on {L(CREATOR, 'creator marketing for beverage and supplement brands')} before anyone posts. If you’ve got a set date coming and want a launch plan built around your store list, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("What is a good velocity for a new grocery item?",
             "It depends entirely on the category and retailer. A good velocity is one that ranks your item in the top half of its set, since buyers cut from the bottom. Ask your broker for the category average units per store per week at that retailer, and compare yourself on base weeks, not promo weeks. Also check sales per point of distribution so store additions don’t distort the picture."),
            ("How do I advertise my product at Kroger?",
             "Kroger sells advertising through Kroger Precision Marketing, its retail media network powered by 84.51°. Options include product listing ads and onsite display through a self-service platform, plus managed offsite CTV and audio added in 2025. Outside Kroger’s network, brands can run geo-targeted Meta and Google ads around the stores that carry them, sending shoppers to a store locator or the Kroger pickup page."),
            ("Does H-E-B have a retail media network?",
             "Yes. H-E-B Retail Media sells promoted-product campaigns on heb.com and the My H-E-B app, plus onsite, offsite, in-store and email placements. It added a self-service option in June 2025, and H-E-B says the network reaches more than 8 million households weekly. Brands can also fund digital coupons and work with the retailer on demos. Ask your broker or H-E-B contact about current formats and minimums."),
            ("How long does a new product get on the shelf before it is cut?",
             "There is no universal rule, and timing varies by retailer and category. Most new items get reviewed at the next category review, often six months to a year after the set, and buyers look at velocity, in-stock rate and promo dependence. Plan your heaviest marketing for the first eight to twelve weeks, when trial decides whether repeat purchase has a chance to show up in the data."),
            ("How do I measure whether my ads increased in-store sales?",
             "Use a test and control design. Split your authorized stores into matched groups, run geo-targeted media only around the test stores for six to eight weeks, then compare units per store per week before and after in both groups. Lift equals the test change divided by the control change, minus one. Cross-check against the retailer media network’s sales-lift report and any platform lift study you run."),
        ],
        "figures": {
            "funnel": {
                "type": "funnel",
                "title": "Where launch velocity leaks",
                "stages": [["Stores authorized", "140"], ["Planogram actually set", "122"], ["Product on shelf, in stock", "109"], ["Shoppers who notice it", "Varies by store"], ["Households who buy again", "The real test"]],
                "note": "Illustrative example",
                "alt": "Funnel showing where CPG retail launch velocity leaks from authorized stores to repeat buyers in Houston grocery stores",
                "caption": "Fix the top three stages before you buy media for the bottom two.",
            },
            "map": {
                "type": "map",
                "title": "Geo-targeting around carrying stores",
                "sub": "Example store clusters for a Houston-area grocery launch",
                "highlight": ["The Woodlands", "Spring", "Cypress", "Katy", "Kingwood", "Pearland", "Sugar Land", "Tomball"],
                "note": "Illustrative example",
                "alt": "Map of example Houston and The Woodlands store clusters for geo-targeted CPG sell-through ads around Kroger and H-E-B",
                "caption": "Split clusters by retailer so creative can name the right store and results read cleanly.",
            },
            "lift": {
                "type": "columns",
                "title": "Test vs. control stores, units per store per week",
                "sub": "Indexed to the pre-launch average of each group",
                "labels": ["Test pre", "Test post", "Control pre", "Control post"],
                "values": [50, 72, 50, 56],
                "highlight": [1],
                "y_label": "Index",
                "note": "Illustrative example",
                "alt": "Column chart comparing test and control store velocity for measuring CPG ad lift in Houston grocery stores",
                "caption": "Here, lift is (72 ÷ 50) ÷ (56 ÷ 50) − 1, or about 29%. The control group keeps you honest.",
            },
            "kroger": {
                "type": "stats",
                "title": "Kroger: creators, billboards and streaming",
                "stats": [["212M", "impressions delivered"], ["38", "markets activated"], ["+24%", "store-visit lift"], ["97%", "CTV completion rate"]],
                "note": "Source: First Byte Kroger case study",
                "alt": "Results from First Byte's Kroger campaign, managed from The Woodlands near Houston, including store-visit lift and CTV completion",
                "caption": "From our Kroger case study. Lift was measured on store visits.",
            },
            "plan": {
                "type": "steps",
                "title": "A 26-week grocery launch",
                "sub": "From eight weeks before the set date to the first review",
                "steps": [["Prep", "Store list, locator, creative, coupons booked."], ["Verify", "Walk stores, confirm sets, defend retailer search."], ["Trial push", "Geo social, retail media, demos, first coupon."], ["Optimize", "Move spend to store clusters that respond."], ["Review", "Retarget, second coupon, one-page buyer recap."]],
                "alt": "Five-step 26-week plan for launching a CPG brand at Kroger and H-E-B in Houston and The Woodlands",
                "caption": "Front-load the budget. The trial window decides whether you get a second year.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: creators and claims
    {
        "slug": "beverage-supplement-marketing-creators-claims",
        "title": "Marketing Beverage and Supplement Brands With Creators (Without Getting in Trouble)",
        "seo_title": "Beverage & Supplement Creator Marketing: Claims Rules",
        "desc": "Creator marketing for beverage and supplement brands: FTC disclosures, health claim substantiation, FDA structure/function rules, alcohol limits and ROI.",
        "category": "Influencer",
        "icons": ["Instagram", "TikTok", "Meta"],
        "art": "b6",
        "hero": "shield",
        "hero_alt": "Illustration of a shield for compliant creator marketing for beverage and supplement brands in Houston and The Woodlands",
        "related": ["ftc-rules-influencer-partnerships", "measuring-influencer-marketing-roi", "micro-influencers-vs-big-names"],
        "sections": [
            (None, f"""<p>Thursday afternoon. A creator you seeded two weeks ago posts a 40-second TikTok about your magnesium gummies. It’s great. Natural, funny, 300,000 views by dinner. Somewhere around second 28 she says they “basically cured” her anxiety, and the only disclosure is the platform’s paid partnership label under the caption.</p>
<p>Your growth lead wants to put $5,000 behind it as a Spark Ad tonight. Your co-founder wants to know whether that’s a problem.</p>
<p>It is. Two problems, actually, and they’re the two that sink most beverage and supplement creator programs: the claim and the disclosure. Both are easy to get right if you build them into the brief instead of finding them in the comments.</p>
<p>To market a beverage or supplement brand with creators without getting in trouble, disclose every material connection clearly inside the content itself, keep creators to claims your company can substantiate (structure/function language for supplements, never disease claims), follow the extra rules for caffeine and alcohol, and check platform ad policies before you turn organic posts into paid ads. Then measure creator spend like any other channel.</p>
<p>We ran a 1,200-creator launch for {L('/case-studies/vital-proteins/', 'Vital Proteins')} and creator bursts for {L('/case-studies/celsius/', 'Celsius')}, so this is the checklist we actually work from. It isn’t legal advice; your regulatory counsel signs off on claims.</p>"""),

            ("The FTC rules: free product counts, and the label isn’t enough", f"""<p>The FTC’s Endorsement Guides were revised in 2023, and the agency’s plain-English {SRC['ftc_faq']} answers most of the questions brands ask. The parts that matter most for CPG:</p>
<ul>
<li><b>Free product is a material connection.</b> It doesn’t matter whether you mailed it, gave a discount code or handed it out at an event. If a creator got your product free and posts about it, they need to disclose that.</li>
<li><b>Platform tools may not be enough.</b> The FAQ says it’s “always best to add your own disclosure” even when a platform offers a paid partnership label.</li>
<li><b>Video needs disclosure in the video.</b> A disclosure shown on screen and said out loud is more likely to be clear and conspicuous. A hashtag buried at the end of a caption is easy to miss.</li>
<li><b>Put it up front.</b> A disclosure in the middle or at the end of a post is less likely to work.</li>
<li><b>Brands have to train and monitor.</b> Advertisers need “reasonable programs” to train and monitor the people promoting them, and health claims call for closer oversight.</li>
</ul>
<p>The FTC has shown it means this for food and beverage. In November 2023 it sent warning letters to the American Beverage Association, the Canadian Sugar Institute and a dozen dietitians and influencers over paid TikTok and Instagram posts about aspartame and sugar. None of the videos the FTC reviewed had a disclosure inside the video, tags like “#ad” and “Paid partnership” required scrolling to see, and some posts named the sponsor only as “ameribev.” The letters noted penalties of up to $50,120 per violation, per {SRC['ftc_letters']}.</p>
<p>If you collect reviews on your site or Amazon, the FTC’s {SRC['reviews']} (effective October 2024) also bans buying fake reviews and undisclosed insider reviews. Seeded creators who leave product reviews count. Our {L('/blog/ftc-rules-influencer-partnerships/', 'FTC influencer rules post')} and {L('/blog/fake-reviews-rule-local-businesses/', 'fake reviews rule explainer')} cover both in more depth.</p>
<!--fig:disclosure-->"""),

            ("Health claims: what a creator can say about your product", f"""<p>Here’s the part brands underestimate. A creator saying something about your product in a post you paid for, shipped product for or turned into an ad is legally your claim. If you can’t back it up, they can’t say it.</p>
<p><b>The FTC standard.</b> In December 2022 the FTC replaced its 1998 supplement advertising guide with the Health Products Compliance Guidance. Health claims need “competent and reliable scientific evidence,” which generally means randomized, controlled human clinical trials. The same standard applies whether the product is a food, a beverage or a supplement, and it covers social media and influencer marketing. A “clinically tested ingredient” claim implies the finished product delivers the benefit at the dose you sell, not just that some study exists on the ingredient. That’s from {SRC['hpcg']}.</p>
<p>The FTC followed up in April 2023 by sending {SRC['nopo']} to roughly 670 marketers of supplements, functional foods, OTC drugs and homeopathic products. The letters don’t accuse anyone of anything. They do mean a company that later makes unsupported claims can face civil penalties.</p>
<p><b>The FDA layer for supplements.</b> Per {SRC['fda_sf']}, a supplement can make structure/function claims (how a nutrient affects the normal structure or function of the body, like “calcium builds strong bones”) without FDA approval. The company must have substantiation, must notify FDA of the claim within 30 days of marketing it, and the label must carry the disclaimer: “This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.” Disease claims aren’t allowed for supplements at all, because only drugs can make them. Conventional foods and beverages can make structure/function claims tied to nutritive value without notifying FDA.</p>
<!--fig:claims-->
<p>Creators don’t think in those categories. They think in stories: “my joints stopped hurting,” “I haven’t been sick all winter,” “this fixed my bloating.” Each of those drifts toward a disease or treatment claim. That’s why the brief needs an approved claims list in plain language, and a do-not-say list next to it.</p>"""),

            ("Energy drinks and caffeine: extra care with audience and dose", f"""<p>Energy drinks get more scrutiny than almost any other beverage, mostly because of who’s watching. The {SRC['fda_caf']} says 400 milligrams a day is an amount not generally associated with negative effects in healthy adults, that energy drinks generally run 54 to 328 milligrams per 16 ounces, and that medical experts advise against energy drinks for children and teens.</p>
<p>Mainstream brands that belong to the trade group follow the {SRC['aba']}: no marketing to children under 12, no selling or marketing in K-12 schools, a label advisory that the product isn’t recommended for children, pregnant or nursing women or people sensitive to caffeine, total caffeine from all sources declared on the label, and no promoting mixing with alcohol.</p>
<p>For a creator program, that turns into a few working rules:</p>
<ul>
<li>Check each creator’s audience age breakdown before you sign. A gaming or dance creator whose audience skews young is the wrong partner, however good the views look.</li>
<li>No content filmed at or about schools, and no high school athletes.</li>
<li>No “drink three before the game” bits. Show one can, in a normal adult context.</li>
<li>No mixing with alcohol on camera.</li>
<li>Restrict paid amplification to adults even where the platform would let you go younger.</li>
</ul>
<p>Performance and focus claims (“clean energy,” “helps you push through a workout”) still need support. If your can has 200 milligrams of caffeine, “energy” is easy to substantiate. “Burns fat” is a much harder claim, and it pulls you into weight-loss ad policies too.</p>"""),

            ("Alcohol is a different rulebook", f"""<p>If you make beer, wine, spirits, hard seltzer or canned cocktails, the federal regulator for advertising is the Alcohol and Tobacco Tax and Trade Bureau (TTB), not just the FTC. TTB’s advertising rules apply to social media, and its current guidance is {SRC['ttb_2024']}, published November 1, 2024. It says brands can satisfy mandatory statements (name, address, class designation) through links or link-sharing pages, and that influencers can tag a compliant brand page to meet those requirements. The full list is on {SRC['ttb_ic']} page.</p>
<p>The industry codes add audience rules. The Beer Institute and Brewers Association require placements where at least {SRC['bi']} of the audience is of legal drinking age, and DISCUS raised the spirits standard to {SRC['discus']} in 2023. In practice that means every creator needs audience data showing about three-quarters of followers are 21 or older, checked before contract.</p>
<p>Platforms layer on more:</p>
<ul>
<li><b>Meta</b> sets its floor at 18, so U.S. alcohol brands have to set 21+ targeting themselves on ads and Pages, per {SRC['sprout']}.</li>
<li><b>TikTok</b> opened U.S. alcohol ads in 2024 with targeting to users 25 and older, per {SRC['mbrew']}. {SRC['tt_alc']} requires a responsible drinking message on the ad and landing page, and bars featuring anyone under 25, pregnant people, excessive drinking, or alcohol as a prize. Creator content for alcohol began running on TikTok by early 2026, per {SRC['fastco']}. Cast creators 25 and up for TikTok alcohol work.</li>
<li><b>Texas</b> has its own rules through TABC, including limits on suppliers paying for advertising that promotes a specific retailer. Our {L(RETAIL, 'retail sell-through post')} covers how that affects “find it at” ads.</li>
</ul>
<p>Non-alcoholic brands don’t carry these rules, but a mocktail brand that films creators in a bar setting may still get reviewed like an alcohol ad. Keep the context unambiguous.</p>"""),

            ("Meta and TikTok ad policies for supplements", f"""<p>Organic posts and paid ads face different reviewers. A creator post that’s fine on its own can get rejected the moment you boost it.</p>
<ul>
<li><b>Meta</b> bans ads for products on its {SRC['meta_unsafe']} list, which includes anabolic steroids, chitosan, comfrey, DHEA, ephedra and human growth hormone. Its {SRC['meta_health']} restricts weight-loss and dietary supplement ads to people 18 and older and prohibits content that makes people feel bad about their appearance. Before-and-after weight shots are where most supplement ads get flagged.</li>
<li><b>TikTok</b> allows supplements in the U.S. subject to age restrictions and policy compliance, according to its {SRC['tt_weight']}. Weight-loss or muscle-gain claims must target 18 and older, and ads can’t claim the product alone, without diet or exercise, causes results, or that results are easy or guaranteed. Body-shaming and “perfect body” framing is prohibited.</li>
</ul>
<p>Our rule: write the paid version of the brief first. If the creator’s content would pass as an ad, it’ll pass as an organic post. The reverse isn’t true.</p>"""),

            ("Running a seeding program that stays clean", f"""<p>Seeding is how most beverage and supplement brands start with creators: send product to a lot of people, see who posts, pay the ones whose content works. It’s also where disclosure falls apart, because nobody signed anything.</p>
<!--fig:seeding-->
<p>How we structure it:</p>
<ol>
<li><b>Tier the creators.</b> Nano (under 10,000 followers) for volume and authenticity, micro for niche credibility (dietitians, trainers, run clubs), macro for reach on launch day. Our {L('/blog/micro-influencers-vs-big-names/', 'micro vs. macro post')} and {L('/blog/find-the-right-influencers/', 'creator vetting guide')} go deeper.</li>
<li><b>Put a one-page note in every box.</b> What the product is, the approved claims, the do-not-say list, and a plain request to disclose (“If you post, please say #gifted or #ad at the start and out loud in videos.”).</li>
<li><b>Get usage rights in writing before paying anyone.</b> The Vital Proteins program had usage rights built into the nano-to-macro tiers from the start, which is what made scaling the winners as ads possible.</li>
<li><b>Monitor what goes live.</b> Check every post within 48 hours. If a claim or a missing disclosure shows up, ask for an edit. Keep a record that you asked.</li>
<li><b>Move the best creators to paid, always-on contracts.</b> Monthly content drops beat one-off posts for both performance and compliance, because the creator learns your rules.</li>
</ol>
<p>A sample brief for a hydration powder, to show the level of specificity we mean:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Brief field</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Hook ideas</td><td>Post-run in July heat on the Waterway, a mid-morning slump at a desk, a youth soccer sideline (adult drinking, not the kids)</td></tr>
<tr><td>Approved claims</td><td>“Electrolytes to help you rehydrate,” “1,000 mg sodium per stick,” “no added sugar”</td></tr>
<tr><td>Do not say</td><td>Cures cramps, treats dehydration illness, better than an IV, safe for kids, any medical condition</td></tr>
<tr><td>Disclosure</td><td>“#ad” in the first line, spoken in the first five seconds, plus the platform’s paid partnership label</td></tr>
<tr><td>Usage rights</td><td>Paid ads for 90 days, organic reposts for 12 months</td></tr>
</tbody></table></div>
<p>The claims in that example are placeholders. Your own approved list comes from your label, your substantiation file and your counsel.</p>"""),

            ("Whitelisting: partnership ads and Spark Ads", f"""<p>Whitelisting means running paid ads through a creator’s handle, so the ad shows their name and face instead of your logo. It’s usually where creator programs start paying for themselves.</p>
<ul>
<li><b>Meta partnership ads</b> run on Facebook and Instagram with both the creator and the brand on the ad. The creator grants permission through Meta’s branded content tools; {SRC['partner']} covers the process.</li>
<li><b>TikTok Spark Ads</b> let you boost a creator’s actual post. Per {SRC['spark']}, the creator turns on ad authorization, generates a code, and picks an authorization period of 7, 30, 60 or 365 days. You paste the code into Ads Manager under Tools, then Creative library, then Spark ads posts.</li>
</ul>
<p>Two compliance points people miss. A whitelisted ad is your ad, so it has to pass the claims review and the platform’s ad policy, including the age restrictions above. And the disclosure inside the video has to survive the edit; if you trim the first five seconds for a tighter hook, you may have cut the spoken “ad.”</p>
<p>For Vital Proteins, whitelisted creator ads through Spark and partnership formats scaled the winning posts and returned 6.2x ROAS. For Celsius, creator and CTV bursts were timed to in-store promos and endcap resets, so the paid creator content pushed people toward shelves that were already stocked. Our {L('/services/paid-social-advertising/', 'paid social team')} runs both formats.</p>"""),

            ("Measuring creator ROI without fooling yourself", f"""<p>Creator programs produce a lot of numbers, and most of them flatter. Earned media value is the worst offender. It’s a modeled estimate of what the impressions would have cost as ads, useful for comparing creators to each other and not much else.</p>
<p>Numbers that hold up:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Formula</th><th>Use it for</th></tr></thead>
<tbody>
<tr><td>Cost per thousand views (organic)</td><td>Creator fees + product cost ÷ (views ÷ 1,000)</td><td>Comparing creators and tiers</td></tr>
<tr><td>Creator ad ROAS</td><td>Attributed revenue ÷ ad spend on whitelisted posts</td><td>Deciding which posts to scale</td></tr>
<tr><td>Fully loaded ROAS</td><td>Attributed revenue ÷ (ad spend + fees + product + management)</td><td>Judging the program as a whole</td></tr>
<tr><td>Hook rate</td><td>3-second views ÷ impressions</td><td>Spotting creative worth testing as ads</td></tr>
<tr><td>Code and link revenue</td><td>Revenue on creator codes and tracked links</td><td>A floor on direct sales, never the full picture</td></tr>
<tr><td>Incremental lift</td><td>Exposed group sales ÷ holdout group sales − 1</td><td>Proving the program grows the business</td></tr>
</tbody></table></div>
<p>If you sell mostly at retail, add the store metrics from our {L(RETAIL, 'sell-through guide')}: locator visits, retailer cart clicks and velocity in markets where creators ran versus markets where they didn’t.</p>
<!--fig:vp-->
<p>The Vital Proteins numbers show the pattern. Seeding to more than 1,200 creators produced 480 million organic and paid impressions and $14.6 million in earned media value, and the number we’d actually defend in a budget meeting is the 6.2x ROAS on creator ads. Our post on {L('/blog/measuring-influencer-marketing-roi/', 'measuring influencer ROI')} has the full framework, and {L('/blog/ugc-vs-influencers-creator-content/', 'UGC vs. influencers')} helps if you’re deciding between the two.</p>"""),

            ("Your pre-flight checklist", f"""<p>Before any creator content goes live or gets amplified, run it through this:</p>
<ul>
<li>Is there a disclosure at the start, on screen and spoken, in addition to the platform label?</li>
<li>Is every claim on the approved list, and is there substantiation in the file for it?</li>
<li>Any disease, cure, treatment or prevention language? Cut it.</li>
<li>For energy drinks: is the creator’s audience overwhelmingly adult, with no school settings and no mixing with alcohol?</li>
<li>For alcohol: is the audience at least about 74% 21+, is the creator 25+ for TikTok, and are the TTB mandatory statements reachable?</li>
<li>Does the paid version pass Meta and TikTok ad policy, including 18+ targeting for weight and supplement claims?</li>
<li>Do you have usage rights in writing for the way you plan to use it?</li>
</ul>
<p>Back to Thursday’s TikTok. The fix is a polite note asking the creator to re-cut without the “cured my anxiety” line, with a spoken disclosure at the top, then running the new version as a Spark Ad. It costs you a day. The alternative could cost a lot more.</p>
<p>If you’re planning a creator launch and want it built with the claims and disclosure work done up front, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Do influencers have to disclose free products?",
             "Yes. Under the FTC’s Endorsement Guides, free product is a material connection, whether it arrived in a seeding box, through a discount code or at an event. Creators should disclose it clearly at the start of the post, and in videos both on screen and out loud. The FTC recommends adding your own disclosure even when the platform offers a paid partnership label, so build that into every brief."),
            ("Can supplement influencers make health claims?",
             "Only claims the brand can substantiate. The FTC’s 2022 Health Products Compliance Guidance generally expects randomized, controlled human trials for health claims, and that applies to creator posts the brand pays for or amplifies. Supplements can make structure/function claims, such as supporting normal joint function, with the FDA disclaimer and notification. Disease claims like curing anxiety or preventing colds are not allowed for supplements."),
            ("What is the FDA supplement disclaimer?",
             "Supplements making structure/function claims must carry this statement: This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease. The company must also have substantiation for the claim and notify FDA within 30 days of first marketing it. Conventional foods and beverages making similar claims do not need the disclaimer."),
            ("Can alcohol brands work with influencers on TikTok and Instagram?",
             "Yes, with limits. TTB’s Industry Circular 2024-1 covers alcohol advertising on social media, including how influencers can meet mandatory statement rules by tagging a compliant brand page. Industry codes require audiences that are roughly 74 percent legal drinking age. Meta requires brands to set 21-plus targeting in the U.S., and TikTok limits U.S. alcohol ads to users 25 and older and bars featuring anyone under 25."),
            ("How do you measure ROI on creator marketing for a CPG brand?",
             "Track creator ad ROAS on whitelisted posts, fully loaded ROAS including fees and product, cost per thousand views by creator tier, and code and link revenue as a floor. For retail brands, add store locator visits and velocity in markets where creators ran compared with markets where they did not. Treat earned media value as a comparison tool between creators, not as revenue."),
        ],
        "figures": {
            "disclosure": {
                "type": "checklist",
                "title": "Creator disclosure checklist",
                "sub": "What every paid or gifted post needs",
                "items": ["#ad, #sponsored or #gifted in the first line of the caption", "Spoken disclosure in the first few seconds of video", "On-screen text disclosure in the video itself", "Platform paid partnership label turned on as well", "Sponsor named in words people recognize", "Disclosure kept when the post is edited into an ad", "Brand reviews every post within 48 hours"],
                "alt": "Checklist of FTC creator disclosure requirements for beverage and supplement brands, from a Houston and The Woodlands agency",
                "caption": f"Based on the {SRC['ftc_faq']} and the FTC’s 2023 warning letters.",
            },
            "claims": {
                "type": "compare",
                "title": "Supplement claims: disease vs. structure/function",
                "left": {"title": "Disease claims (not allowed)", "items": ["Cures anxiety", "Prevents colds and flu", "Treats arthritis pain", "Lowers cholesterol", "Heals leaky gut"]},
                "right": {"title": "Structure/function (with substantiation)", "items": ["Supports a sense of calm", "Supports normal immune function", "Supports joint comfort and mobility", "Part of a heart-healthy routine (with evidence)", "Supports digestive health"]},
                "alt": "Comparison of disease claims and structure/function claims for supplement creator marketing, from a Houston agency",
                "caption": "The right column still needs evidence and the FDA disclaimer. Have counsel approve your list.",
            },
            "seeding": {
                "type": "steps",
                "title": "A seeding program that stays compliant",
                "sub": "From product box to paid creator ads",
                "steps": [["Tier creators", "Nano, micro and macro, with audience age checked."], ["Brief in the box", "Approved claims, do-not-say list, disclosure ask."], ["Rights first", "Usage rights in writing before any payment."], ["Monitor", "Review every post within 48 hours."], ["Scale winners", "Partnership ads and Spark Ads on approved posts."]],
                "alt": "Five steps for a compliant creator seeding program for beverage and supplement brands, from The Woodlands near Houston",
                "caption": "Monitoring is the step most brands skip, and it’s the one the FTC asks about.",
            },
            "vp": {
                "type": "stats",
                "title": "Vital Proteins: a 1,200-creator launch",
                "stats": [["1,200+", "creators activated"], ["480M", "organic + paid impressions"], ["$14.6M", "earned media value"], ["6.2x", "ROAS on creator ads"]],
                "note": "Source: First Byte Vital Proteins case study",
                "alt": "Results from First Byte's Vital Proteins creator program, run from The Woodlands near Houston, including 6.2x ROAS on creator ads",
                "caption": "From our Vital Proteins case study. ROAS on whitelisted ads is the number to plan budgets around.",
            },
        },
    },
]
