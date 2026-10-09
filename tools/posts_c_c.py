"""Long-tail post: is Yelp advertising worth it for small business (Houston / The Woodlands angle).

Research: Yelp's own local-business pricing, Yelp Ads and Upgrades product pages (2026), Yelp Q3 2025 shareholder
letter and Q4/FY2025 results (Business Wire), Yelp 2025 Trust & Safety Report (Business Wire), Yelp Terms of Service
clause on advertising and the recommendation software, TechCrunch on the FTC closing its inquiry (Jan 2015),
Search Engine Land's Yelp vs AdWords call-quality case study, WordStream/LocaliQ 2026 Google Ads benchmarks,
Google's Local Services Ads help page, BrightLocal 2026 Local Consumer Review Survey, Statcounter US search share,
MarTech on Yelp's review rules, and an Alignable owner-forum thread on Yelp ads (2017-2019).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "pricing": A("https://business.yelp.com/local-business-pricing/", "Yelp’s local business pricing page"),
    "ads": A("https://business.yelp.com/products/yelp-ads/", "Yelp Ads product page"),
    "upgrades": A("https://business.yelp.com/products/upgrades/", "Yelp’s Upgrades page"),
    "q4": A("https://www.businesswire.com/news/home/20260212812443/en", "Yelp’s full-year 2025 results"),
    "q3": A("https://s24.q4cdn.com/521204325/files/doc_financials/2025/q3/Yelp-Q3-2025-Letter-to-Shareholders.pdf", "Q3 2025 shareholder letter"),
    "trust": A("https://www.businesswire.com/news/home/20260225039344/en/Yelp-Releases-2025-Trust-Safety-Report/", "Yelp’s 2025 Trust &amp; Safety Report"),
    "tos": A("https://www.yelp.com/static?p=tos", "Yelp’s Terms of Service"),
    "ftc": A("https://techcrunch.com/2015/01/06/ftc-yelp", "TechCrunch"),
    "sel": A("https://searchengineland.com/yelp-ads-worth-paying-case-study-292521/", "Search Engine Land"),
    "wordstream": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream/LocaliQ’s 2026 Google Ads benchmarks"),
    "lsa": A("https://support.google.com/google-ads/answer/6224841", "Google’s Local Services Ads help page"),
    "brightlocal": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "statcounter": A("https://gs.statcounter.com/search-engine-market-share/all/united-states-of-america", "Statcounter"),
    "martech": A("https://martech.org/5-yelp-facts-business-owners-should-know/", "MarTech"),
    "alignable": A("https://www.alignable.com/forum/to-yelp-or-not-to-yelp", "“To Yelp or not to Yelp?”"),
    "press": A("https://www.yelp-press.com/company", "Yelp’s press page"),
}

POSTS = [
    {
        "slug": "is-yelp-advertising-worth-it-small-business",
        "title": "Is Yelp Advertising Worth It for Small Business? A 2026 Answer",
        "seo_title": "Is Yelp Advertising Worth It for Small Business?",
        "desc": "Is Yelp advertising worth it for small business? Real 2026 Yelp ad costs, Yelp vs Google Ads, the review filter, and a 90-day test for Houston owners.",
        "category": "Paid ads",
        "icons": ["Yelp", "Google Ads", "Google Business Profile"],
        "art": "b2",
        "hero": "stars",
        "hero_alt": "Illustration of review stars and a business listing card for a guide on whether Yelp advertising is worth it in Houston",
        "related": ["local-services-ads-vs-google-ads-home-services", "call-tracking-which-ads-make-phone-ring", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Is Yelp advertising worth it for small business? Sometimes. It tends to pay off for restaurants, salons, med spas, movers, auto shops and some home services where customers already shop on Yelp, and it rarely pays off for B2B companies or anyone whose buyers start on Google. The only reliable way to know is a 60 to 90 day test on a budget you can afford to lose, measured with your own call tracking rather than Yelp’s dashboard.</p>
<p>A lot of owners land on this question right after a Yelp rep calls with a “special rate for businesses in The Woodlands.” If that’s you, don’t say yes or no on that call. Yelp publishes more about its pricing and its own ad results than most people realize, and a half hour with those numbers will tell you whether a test is even worth running.</p>"""),
            ("How Yelp Ads work in 2026", f"""<p>Yelp Ads are pay-per-click ads that show inside Yelp. According to the {SRC['ads']}, your ad can appear in the “Sponsored Results” sections above and below the regular search results, on competitors’ business pages, and to people searching off Yelp. You pick a goal (calls and messages, website visits, or map directions), target by location and keyword, and either write the ad yourself or let Yelp build it.</p>
<p>You pay when someone clicks. Yelp sets the click price through its own auction, and you set a budget. The same page says you can “adjust your budget to any maximum amount, when you want and as often as you want,” and that “there are no term contracts with self-serve advertisers.”</p>
<p>Notice the word <b>self-serve</b>. It means you set it up yourself in Yelp for Business. Plans sold over the phone by a rep can come with their own agreement, so read what you sign.</p>
<p>Separate from ads, Yelp sells page upgrades. The {SRC['upgrades']} lists up to seven features depending on your category: Business Highlights, removing competitor ads from your page, a Call to Action button, your logo, a photo slideshow, Yelp Connect posts, and a Portfolio for eligible categories. Older articles call this “Enhanced Profile.” Same idea, new name.</p>"""),
            ("How much does Yelp advertising cost?", f"""<p>Yelp lists four tiers on its {SRC['pricing']}. Every paid tier says “cancel anytime,” and the page notes that “minimum budgets subject to change.”</p>
<div class="bp-tbl"><table>
<thead><tr><th>Yelp product</th><th>Published price</th><th>What you get</th></tr></thead>
<tbody>
<tr><td>Yelp Business Page</td><td>Free</td><td>Claimed page, respond to reviews and messages, quote requests</td></tr>
<tr><td>Yelp Ads</td><td>From $150/month</td><td>Sponsored placements, location and keyword targeting, ad reporting</td></tr>
<tr><td>Upgrade Package</td><td>$180/month</td><td>Visual upgrades, special offers, no competitor ads on your page</td></tr>
<tr><td>Yelp Ads + Upgrade Package</td><td>From $270/month</td><td>Both, plus a Verified License badge</td></tr>
</tbody></table></div>
<p>The table leaves out the number you most need: what a click costs. Yelp doesn’t publish it. It depends on your category, your area and how many competitors are bidding. Yelp’s investor reports do show the direction, though: average cost per click rose 10% in 2025, driven by advertiser demand in Services categories, while total ad clicks fell 7%, per {SRC['q4']}. In the third quarter alone, CPC was up 14% year over year, according to the {SRC['q3']}. More businesses paying more for fewer clicks.</p>
<p>Treat $150 a month as the entry fee rather than a budget. If your clicks cost $8, that’s fewer than 20 clicks. For a fair test, we’d plan on something closer to $500 to $1,000 a month for a home-service company and $300 to $600 for a restaurant or salon. Those are our planning ranges, not Yelp’s numbers.</p>
<p>The Upgrade Package is the easier call, partly because the {SRC['upgrades']} offers a 14-day free trial. The one feature we’d actually pay for is removing competitor ads from your own page, because otherwise your best reviews can sit next to a rival’s ad. If you have strong reviews and real Yelp traffic, it can be worth it. If your page gets a few dozen views a month, skip it.</p>"""),
            ("Is Yelp advertising worth it for small business? How effective it is by industry", f"""<p>The best clue comes from Yelp’s own revenue, because businesses vote with their budgets. In 2025, Yelp’s Services advertising revenue hit a record $948 million, up 8%, while Restaurants, Retail &amp; Other fell 6% to $444 million, per {SRC['q4']}. By the third quarter of 2025, Services had 258,000 paying advertising locations and restaurants-retail-other had 254,000, down from 272,000 a year earlier, according to the {SRC['q3']}.</p>
<p>Service businesses are adding money on Yelp. Restaurants and retailers, the categories Yelp built its name on, are pulling back, and 18,000 fewer of them were paying to advertise in Q3 2025 than a year earlier. That’s a lot of owners deciding the return wasn’t there.</p>
<p>For businesses around Houston, we’d sort it this way:</p>
<ul>
<li><b>Usually worth testing:</b> restaurants and bars with a strong review count (think Market Street, Hughes Landing or a Heights patio), med spas, salons, barbers, nail and lash studios, movers, auto repair, locksmiths, pest control, plumbers and appliance repair.</li>
<li><b>Mixed:</b> HVAC, roofing and pool companies. Yelp can produce calls, but Google Local Services Ads usually wins on cost for emergency work. Test both and compare.</li>
<li><b>Rarely worth it:</b> B2B services, industrial suppliers in the Energy Corridor, accountants and consultants selling to companies, ecommerce, and anything with a long sales cycle. Your buyers aren’t browsing Yelp.</li>
</ul>
<p>One more filter: your reviews. An ad sends people to your Yelp page. If that page shows 3.2 stars and nine reviews, you’re paying to show people a reason to call somebody else. Fix the page before you buy traffic to it.</p>"""),
            ("Yelp traffic in Houston vs Google", f"""<p>We looked for Houston-specific Yelp usage data and couldn’t find any public numbers we trust. Yelp doesn’t publish traffic by city, and the third-party estimates we found didn’t show their methods.</p>
<p>Google handled 85.19% of U.S. search in September 2026, per {SRC['statcounter']}. In {SRC['brightlocal']}, 71% of consumers said they use Google to read reviews of local businesses (down from 83% the year before, as AI tools and Apple Maps take a share), and 24% said they’d written a review on Yelp in the past year. Yelp’s own {SRC['press']} reports 28 million monthly app unique devices on average in 2025, a big audience, but a fraction of Google’s.</p>
<!--fig:reach-->
<p>The practical takeaway for a business in Spring, Katy or The Woodlands: most local customers will meet you on Google first. Yelp is a second shelf, crowded for food, beauty and movers and thin for most others.</p>
<p>To check your own market, compare two numbers for the last 90 days: page views in your free Yelp for Business dashboard, and profile views in your Google Business Profile performance report. If Yelp is a tenth of Google or less, paid Yelp clicks are unlikely to move your business. If they’re close, Yelp deserves a test.</p>"""),
            ("The review filter and the “Yelp punishes non-advertisers” question", f"""<p>Every owner has heard the rumor that your good reviews vanish the month you stop advertising. The public record says less than the rumor does.</p>
<p>Yelp runs automated recommendation software that decides which reviews show on your main page. In 2025, about 22 million reviews were submitted to Yelp. About 70% were recommended, 17% went to “not currently recommended,” and 11% were removed by Yelp’s team, per {SRC['trust']}. Not-recommended reviews don’t count toward your star rating.</p>
<!--fig:filter-->
<p>On advertising, {SRC['tos']} says that “any purchase of advertising or other paid features from Yelp does not and will not influence the Recommendation Software.” Regulators have looked at this. In early 2014 the FTC opened an inquiry after 2,045 complaints alleging Yelp manipulated reviews to favor advertisers, and it closed the inquiry without taking action, as reported by {SRC['ftc']} in January 2015. The same article notes a 2014 federal appeals court ruling that even if Yelp did rank advertisers higher, that alone wouldn’t be illegal.</p>
<p>So the honest answer is that there’s no public finding that ad spend changes your reviews, and there’s plenty of owner frustration with the filter anyway. What the filter does reliably punish is review patterns that look solicited: a burst of five-star reviews from first-time Yelp accounts. Yelp’s guidance says not to ask customers for Yelp reviews at all, as {SRC['martech']} summarizes. That’s very different from Google, where asking is allowed. Our {A('/blog/complete-guide-google-reviews/', 'Google reviews guide')} covers that side.</p>
<p>Don’t buy ads to fix your filter. It won’t.</p>"""),
            ("Yelp ads vs Google Ads vs Local Services Ads", f"""<p>The money you put in Yelp usually comes out of a Google budget, so this is the comparison that matters.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Yelp Ads</th><th>Google Search Ads</th><th>Google Local Services Ads</th></tr></thead>
<tbody>
<tr><td>How you pay</td><td>Per click</td><td>Per click</td><td>Per lead (call, message, booking)</td></tr>
<tr><td>Where it shows</td><td>Yelp search, competitor pages, some off-Yelp</td><td>Google search results</td><td>Top of Google results, with a Google Verified badge</td></tr>
<tr><td>Published starting point</td><td>From $150/month</td><td>No minimum</td><td>No minimum; you set the budget</td></tr>
<tr><td>Targeting control</td><td>Location and keyword</td><td>Keywords, match types, schedule, location, negatives</td><td>Service types and areas; Google picks the matches</td></tr>
<tr><td>Best fit</td><td>Restaurants, beauty, movers, auto, some trades</td><td>Nearly any local business with search demand</td><td>Home services and some professional services</td></tr>
<tr><td>Biggest weakness</td><td>Smaller audience; loose “lead” counting</td><td>Wasted clicks if set up badly</td><td>Limited control; lead quality varies</td></tr>
</tbody></table></div>
<p>For a Houston home-services business, the usual order we’d spend in is Local Services Ads first, Google Search second, Yelp third. With LSA you pay for leads related to your services rather than clicks, per {SRC['lsa']}. Our {A('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs Google Ads breakdown')} goes deeper on that pair.</p>
<p>For a restaurant or salon, Yelp moves up the list. Google CPCs in those categories are low, and so is the ticket, so neither channel needs a big budget to show you something.</p>"""),
            ("Conversion rate: Yelp ads vs Google Ads", f"""<p>Neither company publishes a conversion rate you can line up against the other. Yelp counts a “lead” as any of several actions on your page, and Google benchmarks count conversions the advertiser defines. Comparing those two numbers directly is comparing a phone call to a map tap.</p>
<p>What we do have is Google’s side. {SRC['wordstream']} put the average Google Ads conversion rate at 8.18% and the average cost per lead at $66.69, with big swings by industry:</p>
<!--fig:cpl-->
<p>For Yelp, the best documented comparison we know of is older but still instructive. In a case study on {SRC['sel']} (2018), a Florida auto repair shop spent $700 a month on Yelp. Yelp’s dashboard showed 964 “leads” over two years, but 58% of those were directions and map views. When the shop put a tracking number on its Yelp listing for a month, 50 calls came in, and only 5 were real prospects. The analysis estimated about $350 per Yelp lead versus about $106 per lead from Google Ads for the same shop.</p>
<p>One shop, eight years ago. The lesson that holds up: Yelp’s lead count and your booked jobs are two different numbers, and you only learn the second one by tracking it yourself.</p>"""),
            ("How to test Yelp ads for 60 to 90 days", f"""<p>If the category fits and your page is in decent shape, run a real test. Service businesses with lower call volume need 90 days; restaurants and salons can usually read results in 60.</p>
<!--fig:test-->
<p>A few details that make or break it:</p>
<ul>
<li><b>Use a dedicated tracking number</b> on the Yelp listing, separate from your Google number, and record calls. Our {A('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} explains the setup and how to avoid confusing your listings.</li>
<li><b>Tag your website link</b> from Yelp with UTM parameters so form fills show up in Google Analytics as Yelp traffic.</li>
<li><b>Ask every new customer</b> how they found you, and log it next to the job value.</li>
<li><b>Write down your baseline first.</b> Yelp sends some calls for free. You’re paying for the increase, so note your free Yelp calls and messages for the 60 days before ads start.</li>
<li><b>Set your break-even before day one.</b> Average job profit times close rate equals the most you can pay per qualified call. If a job nets you $400 and you close one in three calls, that’s about $133 per qualified call.</li>
</ul>
<p>At the end, compare cost per booked job from Yelp against the same number from Google. If Yelp is close or better, keep it. If it’s double, cut it back to the free page and put the money into {A('/services/search-marketing/', 'Google Ads')}.</p>"""),
            ("Negotiating with a Yelp sales rep", f"""<p>Yelp’s sales team has a reputation for persistence. In the long-running owner-forum thread {SRC['alignable']} on Alignable (answers from 2017 to 2019), most replies complained about persistent sales calls and thin results, while a couple of owners said trial periods or specific categories did bring customers. That’s a self-selected, older sample, so treat it as a warning about the sales process, not proof about results.</p>
<!--fig:pitch-->
<p>What we’d say on the callback:</p>
<ol>
<li>“Is this self-serve, or a sales-assisted plan with an agreement? Send me the terms in writing.”</li>
<li>“I want month-to-month, no auto-renewal, and I want my budget cap in writing.”</li>
<li>“Which keywords and which ZIP codes will my ads show for?” Ask for Spring, The Woodlands and Conroe by name if that’s your area, so your budget isn’t spent on clicks from the other side of Houston.</li>
<li>“What’s the expected cost per click in my category here?” They can usually give an estimate. Write it down and compare it to your actual numbers in month one.</li>
<li>“Can I trial the Upgrade Package for the full 14 days before paying?”</li>
<li>“How do I cancel, and what notice do you need?” Get the answer by email.</li>
</ol>
<p>And never let a rep tie ads to your reviews. If anyone suggests advertising will help your rating, that contradicts Yelp’s own terms.</p>
<p>Before that callback, do one thing: pull your last 90 days of Yelp page views and Google Business Profile views and put them side by side. That ratio settles most Yelp decisions before the rep finishes the pitch.</p>
<p>And remember where a Yelp budget usually comes from. It’s money you’d otherwise spend on Google, so the fair comparison is Yelp against a well-run Google account, not a leaky one. If you aren’t sure yours is clean, our free <a href="/contact/">Ad Spend Leak Check</a> will show you. We record a 10-minute walkthrough of your Google or Meta account pointing out the clicks and settings that waste money, so you can judge Yelp against the real cost of a lead.</p>"""),
        ],
        "faq": [
            ("What do business owners say about Yelp advertising?",
             "The owner forum discussions we read, mainly a long Alignable thread, lean negative, mostly about persistent sales calls, small jobs and weak lead quality, with a few owners saying a trial period or their category did bring customers. Those threads are self-selected, since unhappy owners post more. Use them as a reason to test carefully with your own call tracking, not as a final verdict for your business."),
            ("Is Yelp paid advertising worth it compared with the free Yelp page?",
             "Claim and complete the free page first, since it already gets you found and lets you answer reviews and quote requests. Paid ads only make sense once that page has solid photos and a healthy rating. Measure the free calls and messages you already get, then judge paid ads on the extra jobs they produce above that baseline."),
            ("How much does Yelp advertising cost per month?",
             "Yelp lists ads from $150 a month, the Upgrade Package at $180 a month, and both together from $270 a month, with cancel anytime terms on its pricing page. Actual cost per click varies by category and area, and Yelp reported its average CPC rose 10% in 2025. Most service businesses need more than the minimum to run a meaningful test."),
            ("Does advertising on Yelp affect your reviews?",
             "Yelp’s Terms of Service say buying ads does not and will not influence its recommendation software, and the FTC closed an inquiry into those complaints in 2015 without taking action. Reviews still get filtered for other reasons, such as coming from new or inactive accounts. Advertising will not move filtered reviews back onto your page."),
            ("Can I cancel Yelp ads anytime?",
             "Yelp says self-serve advertisers have no term contracts and can cancel anytime, and its pricing page lists cancel anytime on every paid tier. If a sales rep set up your plan, read that agreement for notice periods or renewal terms, and get the cancellation steps in writing by email before you sign up for anything."),
        ],
        "figures": {
            "reach": {
                "type": "bars",
                "title": "Google vs Yelp in review habits",
                "sub": "Share of U.S. consumers, BrightLocal 2026",
                "items": [["Google", 71, "71%"], ["Local news sites", 29, "29%"], ["Apple Maps", 27, "27%"], ["Wrote a Yelp review", 24, "24%"]],
                "highlight": [0],
                "note": "Source: BrightLocal Local Consumer Review Survey 2026",
                "alt": "Bar chart comparing 71 percent reading Google reviews with 24 percent writing Yelp reviews, for Yelp advertising decisions",
                "caption": f"Google still leads, per {SRC['brightlocal']}. The survey reported Yelp as a place people wrote reviews, so that bar measures writing, not reading.",
            },
            "filter": {
                "type": "stats",
                "title": "What happened to Yelp reviews in 2025",
                "stats": [["22M", "reviews submitted to Yelp"], ["70%", "recommended by the software"], ["17%", "sent to not recommended"], ["11%", "removed by Yelp’s team"]],
                "note": "Source: Yelp 2025 Trust & Safety Report",
                "alt": "Stat tiles showing 70 percent of Yelp reviews recommended and 17 percent filtered in 2025, relevant to Yelp advertising decisions",
                "caption": f"Roughly one in six reviews lands in the not-recommended section, per {SRC['trust']}.",
            },
            "cpl": {
                "type": "bars",
                "title": "Google Ads cost per lead by industry",
                "sub": "U.S. averages, 2026 benchmarks",
                "items": [["Business services", 93.69, "$93.69"], ["Home improvement", 90.92, "$90.92"], ["Health & fitness", 67.36, "$67.36"], ["Beauty", 39.25, "$39.25"], ["Restaurants", 30.57, "$30.57"], ["Auto repair", 29.96, "$29.96"]],
                "highlight": [5],
                "note": "Source: WordStream/LocaliQ 2026",
                "alt": "Bar chart of Google Ads cost per lead by industry, the benchmark to compare against Yelp ads vs Google Ads for small business",
                "caption": "Auto repair is the category in the Yelp case study below, and it’s among the cheapest Google leads.",
            },
            "test": {
                "type": "steps",
                "title": "A 90-day Yelp ads test",
                "sub": "Measure booked jobs, not Yelp’s lead count",
                "steps": [
                    ["Record a baseline", "Log free Yelp calls, messages and quote requests for 60 days before ads."],
                    ["Fix the page", "Fresh photos, accurate hours and service areas, replies to recent reviews."],
                    ["Track separately", "Dedicated call tracking number and UTM-tagged website link on Yelp."],
                    ["Run a fixed budget", "Same monthly cap for 90 days, targeted to the ZIP codes you serve."],
                    ["Score every lead", "Mark each call as real prospect, spam, or existing customer, with job value."],
                    ["Compare and decide", "Cost per booked job on Yelp vs Google. Keep, trim or cancel."],
                ],
                "alt": "Six-step plan for testing whether Yelp advertising is worth it for a small business in The Woodlands over 90 days",
                "caption": "The baseline step is the one most owners skip, and it’s the one that tells you what you actually bought.",
            },
            "pitch": {
                "type": "compare",
                "title": "Buying Yelp ads on your terms",
                "left": {"title": "How the pitch often goes", "items": ["Pressure to decide on the call", "Terms explained by phone", "Dashboard lead counts as proof", "Broad metro targeting", "Cancellation details left vague"]},
                "right": {"title": "What to ask for", "items": ["Self-serve or month-to-month", "No auto-renewal, cap in writing", "Booked jobs as proof", "Only your ZIP codes", "Cancellation steps by email"]},
                "alt": "Comparison of a typical Yelp sales pitch versus better terms to request when deciding if Yelp advertising is worth it",
                "caption": "Yelp’s own pricing page says cancel anytime, so there’s no reason to accept less.",
            },
        },
    },
]
