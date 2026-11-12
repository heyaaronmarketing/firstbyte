"""Batch 11 (eCommerce vertical): a Meta ads creative testing and scaling system for DTC/Shopify brands, and the
Klaviyo email and SMS flows that make money.

Research, Meta post: Meta Engineering's Dec. 2, 2024 Andromeda post (10,000x retrieval model capacity, +6% recall,
+8% ads quality on selected segments); Jon Loomer on Andromeda (retrieval narrows tens of millions of ads to a few
thousand; Meta calls creative diversification the best lever; the old six-ads-per-ad-set guidance dropped) and on
creative diversification (Flexible format up to 10 images/videos, 5 text and 5 headline variations); Meta for
Developers June 3, 2025 post on the Advantage+ campaign experience (Advantage+ ON = Advantage+ campaign budget,
Advantage+ audience in at least one ad set, Advantage+ placements in all ad sets; ASC/AAC creation ends across all API
versions with v25.0 in Q1 2026; Existing Customer Budget Cap deprecated); Jon Loomer on Advantage+ sales replacing
Advantage+ shopping (ad sets return, 50 ads per ad set vs. 150 per ASC campaign); Jon Loomer on Meta's Creative Testing
tool (2-5 ads, test budget "no more than 20%", 7-day default, Highest Volume only, one test ad per person); Jon Loomer
on significant edits ($100 to $101 vs. $100 to $1,000); PPC Land on Meta's Oct. 21, 2026 peak-season post (~50
conversions a week; ad sets under it ~28% more per purchase, no method published; weekly budget / (CPR x 50) ceiling);
Runneth (formerly Motion) creative metric formulas (hook rate, hold rate); Social Media Today May 21, 2024 on catalog
ads (formerly dynamic ads) adding video. First Byte case studies: Vital Proteins, Celsius.

Research, email/SMS post: Klaviyo 2026 email benchmarks (183,000+ customers; flows 32.2% open / 5.58% click vs.
campaigns 31% / 1.69%; flow RPR nearly 18x campaigns; top 10% flows up to $7.79 RPR); Klaviyo 2026 SMS benchmarks
(flows 9.65% click, 1.9% order rate; campaigns 5.6% / 0.27%; flows ~8x campaign RPR); Klaviyo 2026 abandoned cart
report (email RPR $6.77 avg / $13.70 top 10%, SMS $4.48 / $8.69, email click 6.0% / 11.3%); Klaviyo help on browse
abandonment (Viewed Product trigger, filters, 1-hour minimum delay), predictive analytics (500 customers, 180 days of
history with orders in last 30 days, some 3+ order customers), sunset flows (prebuilt Sunset segment, max 3 emails,
Unengaged property, manual suppression), Apple Privacy Open property, attribution defaults (5-day email open/click,
5-day SMS click), SMS quiet hours (profile location default, 8 a.m.-9 p.m. guidance, state-level option); Klaviyo blog on
state-aware quiet hours and 3-per-24-hour caps in FL, OK, OR, MD (Jan. 14, 2026) and on sign-up forms (3% benchmark,
3-8% standard popups, 10-13% exit-intent/phone-only, 5-second + 20% scroll); Google's Oct. 3, 2023 Gmail announcement;
Yahoo sender best practices; Red Sift on Gmail enforcement ramp (Nov. 2025, 0.1%/0.3%); Spam Resource on Microsoft's
May 5, 2025 rules; govregs 47 CFR 64.1200 (8 a.m.-9 p.m.); Texas SOS telephone solicitation FAQ; National Law Review on
SB 140 after the November 2025 settlement. First Byte case studies: Equinox, Vital Proteins.
Left out (could not verify from a primary or reliable secondary source): Meta's partnership-ad CPA/CTR lift figures,
a specific Meta budget-change percentage, Klaviyo per-flow benchmarks for welcome, browse, post-purchase and winback.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # Meta post
    "andromeda": A("https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/", "Meta’s engineering post on Andromeda"),
    "loomer_andromeda": A("https://www.jonloomer.com/meta-andromeda/", "Jon Loomer’s breakdown of Andromeda"),
    "loomer_div": A("https://www.jonloomer.com/meta-andromeda-creative-diversification/", "Jon Loomer’s post on creative diversification"),
    "dev_adv": A("https://developers.facebook.com/blog/post/2025/06/03/advantage-plus-campaign-experience-for-sales-and-app/", "Meta’s developer announcement"),
    "loomer_sales": A("https://www.jonloomer.com/qvt/advantage-sales-replaces-advantage-shopping/", "Jon Loomer"),
    "loomer_test": A("https://www.jonloomer.com/meta-creative-testing/", "Jon Loomer’s walkthrough of the Creative Testing tool"),
    "loomer_edits": A("https://www.jonloomer.com/facebook-ads-edits-learning-phase/", "Meta’s own examples, collected by Jon Loomer"),
    "ppcland": A("https://ppc.land/meta-says-ad-sets-under-50-weekly-conversions-cost-28-more-per-purchase/", "PPC Land’s report on Meta’s October 2026 peak-season post"),
    "runneth": A("https://runneth.com/blog/key-creative-performance-metrics", "Runneth (formerly Motion)"),
    "smt_catalog": A("https://www.socialmediatoday.com/news/meta-adds-video-automated-catalog-ads/716802/", "Social Media Today"),
    # email/SMS post
    "kl_email": A("https://www.klaviyo.com/products/email-marketing/benchmarks", "Klaviyo’s 2026 email benchmarks"),
    "kl_sms": A("https://www.klaviyo.com/products/sms-marketing/benchmarks", "Klaviyo’s 2026 SMS benchmarks"),
    "kl_cart": A("https://www.klaviyo.com/blog/abandoned-cart-benchmarks", "Klaviyo’s 2026 abandoned cart benchmark report"),
    "kl_browse": A("https://help.klaviyo.com/hc/en-us/articles/115002775252", "Klaviyo’s browse abandonment guide"),
    "kl_predict": A("https://help.klaviyo.com/hc/en-us/articles/360020919731", "Klaviyo’s predictive analytics requirements"),
    "kl_sunset": A("https://help.klaviyo.com/hc/en-us/articles/360017518492", "Klaviyo’s sunset flow guide"),
    "kl_mpp": A("https://help.klaviyo.com/hc/en-us/articles/4416791883163", "Klaviyo’s help page on Apple privacy opens"),
    "kl_attr": A("https://help.klaviyo.com/hc/en-us/articles/1260804504250", "Klaviyo’s attribution settings"),
    "kl_quiet": A("https://help.klaviyo.com/hc/en-us/articles/4408737146651-Guide-to-SMS-Quiet-Hours-in-Flows", "Klaviyo’s quiet hours guide"),
    "kl_state": A("https://www.klaviyo.com/blog/state-aware-sms-quiet-hours-frequency-capping", "Klaviyo’s state-aware quiet hours"),
    "kl_forms": A("https://www.klaviyo.com/blog/sign-up-form-best-practices", "Klaviyo’s sign-up form guide"),
    "gmail": A("https://blog.google/products/gmail/gmail-security-authentication-spam-protection/", "Google’s October 2023 announcement"),
    "yahoo": A("https://senders.yahooinc.com/best-practices/", "Yahoo’s sender best practices"),
    "redsift": A("https://redsift.com/blog/gmails-enforcement-ramps-up-what-bulk-senders-need-to-know", "Red Sift"),
    "msft": A("https://www.spamresource.com/2025/04/microsoft-joins-club-top-four-b2c-mbps.html", "Spam Resource"),
    "cfr": A("https://www.govregs.com/regulations/47/64.1200", "47 CFR 64.1200"),
    "hklaw": A("https://www.hklaw.com/en/insights/publications/2026/03/tcpa-reset-fifth-circuit-rejects-prior-express-written-consent-rule", "Holland &amp; Knight’s summary"),
    "sos": A("https://www.sos.texas.gov/statdoc/faqs3400.shtml", "Texas Secretary of State’s FAQ"),
    "nlr": A("https://natlawreview.com/article/texas-sb-140-after-november-settlement-consent-cold-texting-out", "National Law Review"),
}

META = "/blog/meta-ads-ecommerce-creative-testing-scaling/"
FLOWS = "/blog/ecommerce-email-sms-flows-klaviyo/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: Meta creative testing
    {
        "slug": "meta-ads-ecommerce-creative-testing-scaling",
        "title": "Meta Ads for eCommerce Brands: A Creative Testing System That Scales",
        "seo_title": "Meta Ads for eCommerce: A Creative Testing System",
        "desc": "A Meta ads creative testing system for eCommerce and Shopify brands: Advantage+ sales setup, test budgets, hook and hold rates, MER and scaling rules.",
        "category": "Paid social",
        "icons": ["Meta", "Instagram", "Facebook"],
        "art": "b2",
        "hero": "play",
        "hero_alt": "Illustration of a play button for Meta ads creative testing for eCommerce brands, from First Byte in The Woodlands, Houston",
        "related": ["ugc-vs-influencers-creator-content", "retargeting-explained", "google-shopping-ads-shopify-setup-guide"],
        "sections": [
            (None, f"""<p>Monday, 8:15 a.m. The founder opens Ads Manager before coffee. Blended ROAS slid all weekend. The video that carried March, the one where the customer unboxes the product in her car, is sitting at a frequency of 5 and its cost per purchase has doubled.</p>
<p>Someone on the team says “we need new creative.” Three new videos go into the winning ad set by lunch. The ad set drops back into learning, spend lurches toward one of the new ads, and by Thursday nobody can say whether the new videos are bad or the account is just recovering from being poked.</p>
<p>That week is the problem this post solves. Most eCommerce brands don’t have a creative problem so much as a creative <i>system</i> problem: no fixed place to test, no rule for when a test is over, and no agreed way to move a winner into the campaign that scales.</p>
<p>Below is the system we run for DTC and Shopify brands on Meta, from campaign structure and test budgets to the metrics that tell you why an ad failed, plus the scaling rules, a weekly calendar and the brief template our team uses.</p>"""),

            ("What changed in Meta’s delivery: Andromeda and creative as targeting", f"""<p>In December 2024 Meta published {SRC['andromeda']}, the system that picks which ads are even considered for a person before the auction ranks them. Meta said it delivered a 10,000x increase in retrieval model capacity, a 6% recall improvement and an 8% ads quality improvement on selected segments. Per {SRC['loomer_andromeda']}, retrieval narrows tens of millions of ads down to a few thousand candidates for each person.</p>
<p>The practical result is that your ad itself does more of the targeting than your audience settings do. Meta’s own guidance has shifted to calling creative diversification the best lever available, and the old recommendation of no more than six ads per ad set quietly disappeared, again per Loomer.</p>
<p>What “diversification” means matters. Five versions of the same video with different captions look like one ad to a retrieval system. Five genuinely different concepts (a founder story, a problem-and-fix demo, a customer testimonial, a comparison against the thing people use now, a static with a price and an offer) give Meta five different shots at five different kinds of buyer. {SRC['loomer_div']} makes the same point: variations that aren’t distinctly different are unlikely to change performance much.</p>
<p>So the unit of testing in this system is the <b>concept</b>. Hooks, edits and formats are iterations inside a concept, and we test those after a concept has earned it.</p>"""),

            ("Advantage+ sales campaigns: what the name means now", f"""<p>If you learned Meta in 2023 or 2024, you learned Advantage+ shopping campaigns (ASC). That product has been folded into what Meta now calls <b>Advantage+ sales campaigns</b>. Per {SRC['dev_adv']} from June 2025, a sales campaign counts as “Advantage+ on” when it uses three things: Advantage+ campaign budget, Advantage+ audience in at least one ad set, and Advantage+ placements in all ad sets. Creating or updating the old ASC campaign type through the API ended across all versions with v25.0 in the first quarter of 2026, and the Existing Customer Budget Cap was deprecated along with it.</p>
<p>A few practical differences, as summarized by {SRC['loomer_sales']}: ad sets are back, there’s no fixed limit on how many you create, and each ad set holds up to 50 ads. Old ASC campaigns held up to 150 ads in one place. You can add audience suggestions and custom audience exclusions, which ASC never handled well.</p>
<p>In Ads Manager, the path is short. Click <b>Create</b>, choose the <b>Sales</b> objective, and keep the campaign budget, audience and placement settings on Advantage+ if you want the automated version. Ads Manager shows whether the campaign is running as Advantage+. Turn any of those off and you have a manual sales campaign, which is still useful for structured tests.</p>
<p>For most Shopify brands spending $20,000 to $300,000 a month, we want exactly one Advantage+ sales campaign doing the heavy lifting. Splitting budget across five similar campaigns just splits the learning.</p>"""),

            ("The account structure that keeps tests readable", f"""<p>Testing only works if new ads have somewhere to prove themselves without disturbing the ads that pay the bills. This is the three-part structure we use:</p>
<div class="tbl"><table>
<thead><tr><th>Campaign</th><th>Job</th><th>Settings</th><th>Share of spend (starting point)</th></tr></thead>
<tbody>
<tr><td>Scaling (Advantage+ sales)</td><td>Spend efficiently on proven ads</td><td>Advantage+ budget, audience and placements; 8 to 20 live ads; edited as little as possible</td><td>65% to 75%</td></tr>
<tr><td>Testing</td><td>Find new winning concepts</td><td>Manual sales campaign, one ad set per concept, or Meta’s Creative Testing tool inside the scaling campaign</td><td>15% to 25%</td></tr>
<tr><td>Catalog</td><td>Show viewed and related products</td><td>Advantage+ catalog ads with a clean product feed</td><td>5% to 15%</td></tr>
</tbody></table></div>
<!--fig:mix-->
<p>Those percentages come from accounts we’ve run. They aren’t a Meta rule. A brand launching a new product line might push testing to 30% for a month, and a brand with one hero SKU and a deep library of proven ads might run testing at 10%.</p>
<p>There’s a budget ceiling to respect, too. In an October 2026 peak-season post, Meta said ad sets need roughly 50 conversions a week to learn, and that ad sets under that threshold ran about 28% more expensive per purchase. Meta published no method for that figure, as {SRC['ppcland']} pointed out, but the same post gave a useful formula: weekly budget divided by (cost per result × 50) is about how many ad sets your budget can support. At $20,000 a week and a $40 cost per purchase, that’s 10 ad sets. At $100 per purchase, it’s four. Most accounts we inherit have twice as many ad sets as their budget can feed.</p>"""),

            ("How many creatives, and how to structure the test", f"""<p>The right number of new ads per week depends on your test budget and your cost per purchase. The rule we use: each concept needs enough spend to buy two to three purchases at your target CPA before you judge it. Fewer than that and you’re reading noise.</p>
<p>An illustrative example. A brand spends $60,000 a month, puts 20% into testing ($12,000, or about $2,800 a week) and has a $45 target CPA. At roughly $135 per concept to reach a judgment, that budget supports about 20 ads a week. In practice we’d run four to six concepts with three or four executions each, rather than 20 unrelated ads.</p>
<p>There are two clean ways to run the test.</p>
<ul>
<li><b>A separate testing campaign.</b> A manual sales campaign, ad set budgets, one ad set per concept, broad targeting with your existing customers excluded if you want a cleaner read on new buyers. Winners get moved into the scaling campaign using the existing post ID, so the likes and comments come with them.</li>
<li><b>Meta’s Creative Testing tool.</b> Inside an ad’s settings there’s now a Creative Testing section with a <b>Set up test</b> button. Per {SRC['loomer_test']}, you can test two to five ads, Meta recommends setting the test budget at no more than 20% of the campaign or ad set budget, the default length is seven days, it requires the Highest Volume bid strategy, and each person sees only one of the test ads. Results show up under Experiments.</li>
</ul>
<p>We use the built-in tool for head-to-head questions inside a concept (hook A versus hook B) and the separate campaign for new concepts. Each test gets one written hypothesis before launch, such as “A 30-second founder story will beat our UGC testimonial on new-customer CPA.” If you can’t write the sentence, you’re not testing anything.</p>
<!--fig:matrix-->"""),

            ("Reading results: the metrics and the formulas", f"""<p>ROAS tells you whether an ad is working. It doesn’t tell you why. The creative metrics do, and most of them are simple ratios you can build as custom columns in Ads Manager. The formulas below follow the definitions used by {SRC['runneth']}, plus the business metrics we hold every account to.</p>
<div class="tbl"><table>
<thead><tr><th>Metric</th><th>Formula</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td>Hook rate (thumbstop)</td><td>3-second video plays ÷ impressions</td><td>Did the first three seconds stop the scroll?</td></tr>
<tr><td>Hold rate</td><td>15-second plays (ThruPlays) ÷ 3-second plays</td><td>Did the middle keep them watching?</td></tr>
<tr><td>Outbound CTR</td><td>Outbound clicks ÷ impressions</td><td>Did the ad make them want to see the product page?</td></tr>
<tr><td>Conversion rate</td><td>Purchases ÷ outbound clicks (or landing page views)</td><td>Did the page and offer close the sale?</td></tr>
<tr><td>CPA</td><td>Spend ÷ purchases</td><td>What a purchase costs in-platform</td></tr>
<tr><td>ROAS</td><td>Attributed purchase value ÷ spend</td><td>Platform-reported return</td></tr>
<tr><td>MER (blended ROAS)</td><td>Total store revenue ÷ total marketing spend</td><td>Whether the business is actually growing profitably</td></tr>
<tr><td>New-customer CPA</td><td>Total paid spend ÷ first-time customers</td><td>What it really costs to buy a new customer</td></tr>
</tbody></table></div>
<p>Read them in order, like a funnel. Each stage points to a different fix:</p>
<!--fig:diagnose-->
<p>A low hook rate means you rewrite or reshoot the first three seconds and leave the rest alone. A strong hook with weak hold usually means the video promised one thing and then wandered off into brand talk. Good hold and weak CTR is an offer or call-to-action problem. Strong CTR with a weak conversion rate is almost always the product page, the price or shipping cost, not the ad.</p>
<p>We don’t publish universal “good” numbers for these, because they swing with category, price point and placement. Benchmark against your own account’s last 90 days instead. Your top quartile of ads is the bar.</p>
<p>And keep MER above the ad-level numbers. Meta’s attributed ROAS can rise while store revenue stays flat, especially when spend drifts toward people who were going to buy anyway. If MER and new-customer CPA hold while you scale, the platform numbers are telling the truth. Our {L('/blog/measure-marketing-success-metrics/', 'guide to marketing metrics')} covers how to set targets from your margins.</p>"""),

            ("Kill, iterate or graduate: the decision rules", f"""<p>Every test needs a pre-agreed exit. These are the defaults we start with, adjusted per account:</p>
<ul>
<li><b>Kill</b> when an ad has spent two to three times your target CPA with no purchase, or when hook rate sits in your account’s bottom quartile after a few thousand impressions.</li>
<li><b>Iterate</b> when one stage is strong and another is weak. A great hook with a bad middle gets a re-edit. A great video with a weak CTR gets a new offer or end card.</li>
<li><b>Graduate</b> when CPA is at or under target across at least five to ten purchases (more for low-price products), and the new-customer share looks healthy.</li>
</ul>
<p>Graduated ads go into the scaling campaign using the same post ID. Don’t duplicate the winning ad set to “scale” it. And don’t turn off the old winner the same day; let Meta shift spend between them.</p>"""),

            ("UGC vs. studio creative, and where creators fit", f"""<p>We get asked this every week. The honest answer is that the format matters less than the concept, and most winning accounts run both.</p>
<!--fig:ugc-->
<p>UGC-style video (a real person, a phone camera, talking straight to the viewer) tends to win on hook rate and on cold audiences, because it looks like the rest of the feed. Studio work wins when the product is visual (apparel, jewelry, home goods) or when price and positioning need it to look expensive. Static images are underrated. A clean product shot with a price, a review quote and an offer is cheap to make and often beats video on CPA for repeat buyers.</p>
<p>Creators add something else: their own audience and their own handle on the ad. On our {L('/case-studies/vital-proteins/', 'Vital Proteins launch')}, we seeded product to more than 1,200 wellness, fitness and food creators, then ran the best posts as whitelisted creator ads (Spark and partnership ads). Those creator ads returned 6.2x ROAS. The lesson we took from it wasn’t “creators always work.” It was that a large pool of creator content gives the testing system far more distinct concepts to choose from than any single shoot could.</p>
<p>Two practical notes. Get usage rights in writing before you put a creator’s video behind paid spend, and keep the disclosure intact; our {L('/blog/ftc-rules-influencer-partnerships/', 'post on FTC rules for influencer partnerships')} covers the details. And our {L('/blog/ugc-vs-influencers-creator-content/', 'UGC vs. influencers guide')} goes deeper on cost and sourcing.</p>"""),

            ("Catalog ads: the quiet workhorse", f"""<p>Advantage+ catalog ads (Meta’s name for what used to be dynamic ads) pull products from your catalog and show people the items they viewed, or items Meta predicts they’ll want. Since May 2024 they can include product video as well as images, per {SRC['smt_catalog']}.</p>
<p>For most Shopify stores, catalog ads do two jobs. They retarget product viewers and cart abandoners (the classic use), and they prospect broadly when the catalog is large enough for Meta to find matches. A store with 12 products gets less from broad catalog prospecting than a store with 1,200.</p>
<p>Catalog ads are only as good as the feed. Connect the catalog through Shopify’s Facebook &amp; Instagram channel, check Commerce Manager for rejected items weekly, and write titles a human would want to read. Add frames or overlays with a review score or free-shipping line if your category is crowded. The feed work overlaps heavily with Google Shopping, so if you’ve done our {L('/blog/google-shopping-ads-shopify-setup-guide/', 'Google Shopping setup for Shopify')}, most of it carries over. And our {L('/blog/retargeting-explained/', 'retargeting explainer')} covers the basics if this is new.</p>"""),

            ("Budget scaling rules that don’t break the account", f"""<p>Meta doesn’t publish a percentage for how big a budget change resets learning. It gives examples instead: going from $100 to $101 isn’t likely to put an ad set back into learning, and going from $100 to $1,000 may, per {SRC['loomer_edits']}. Everything between those is judgment.</p>
<p>Ours, from accounts we’ve managed:</p>
<ol>
<li>Raise the scaling campaign budget 15% to 20% at a time, no more often than every two to three days, while CPA and MER hold.</li>
<li>Scale on the business numbers. If MER drops more than about 10% after a raise and stays there for a week, step back to the last budget that worked.</li>
<li>Batch your edits. One change on Tuesday is better than four changes spread across the week, because every edit costs learning time.</li>
<li>Feed the scaling campaign new graduates every week. Budget increases without new creative are how frequency climbs and CPA follows.</li>
<li>Plan peak season early. Meta’s own peak-season advice was to pick your biggest campaign, set it up and leave it alone through the run-up.</li>
</ol>
<p>Houston brands get one extra seasonal wrinkle. When a hurricane or a hard freeze hits the Gulf Coast, local attention and delivery promises both change for a week or two. If a meaningful share of your customers are in Texas, have a pause-or-adjust plan ready rather than discovering it in the CPA chart.</p>"""),

            ("The weekly testing calendar and the brief template", f"""<p>A system is mostly a calendar people actually follow. This is the week we run for eCommerce clients:</p>
<div class="tbl"><table>
<thead><tr><th>Day</th><th>What happens</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Monday</td><td>Read last week’s tests against the decision rules. Kill, iterate or graduate. Check MER and new-customer CPA.</td><td>Media buyer</td></tr>
<tr><td>Tuesday</td><td>Move graduates into the scaling campaign. Make any budget change for the week (one change).</td><td>Media buyer</td></tr>
<tr><td>Wednesday</td><td>Creative review: what won, why, and what to brief next. Write four to six briefs.</td><td>Strategist and creative lead</td></tr>
<tr><td>Thursday</td><td>Production: edits, new hooks on proven concepts, creator requests, statics.</td><td>Editors and creators</td></tr>
<tr><td>Friday</td><td>Launch new tests so they get a full week, weekend included.</td><td>Media buyer</td></tr>
</tbody></table></div>
<p>Every new concept starts with a one-page brief. Ours has these fields:</p>
<!--fig:brief-->
<p>The “why we think it will win” line is the one people skip, and it’s the one that makes the Monday review useful. When a test loses, you learn whether the idea was wrong or the execution was.</p>"""),

            ("Mistakes we see in eCommerce Meta accounts", f"""<ul>
<li><b>Adding new ads to the winning ad set.</b> It resets learning on the thing that’s working. Test somewhere else.</li>
<li><b>Testing tiny variations.</b> Changing the button color isn’t a test Andromeda can tell apart. Test concepts.</li>
<li><b>Judging on day two.</b> Meta reallocates spend in the first days. Set the test length before launch and stick to it.</li>
<li><b>Ignoring the product page.</b> When CTR is strong and purchases aren’t, the ad has done its job. Look at the page, price and shipping.</li>
<li><b>Running everything off platform ROAS.</b> Without MER and new-customer CPA, it’s easy to scale spend into people who would have bought anyway.</li>
<li><b>No creative pipeline.</b> Brands that brief on Wednesday because the numbers dropped on Monday are always two weeks behind.</li>
</ul>
<p>A first month on this system looks like this: week one, rebuild the structure and set up custom metric columns; week two, launch the first four to six concepts; weeks three and four, run the calendar and graduate the first winners. By day 30 you should know which two or three concepts your customers respond to, which is worth more than any single winning ad.</p>
<p>We run this for DTC and Shopify brands through our {L('/services/paid-social-advertising/', 'paid social team')}, and our {L('/industries/ecommerce/', 'eCommerce page')} shows the rest of the playbook. If you’d like a senior strategist to look at your account and build a testing plan around your margins and catalog, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How many creatives should I test on Meta each week?",
             "It depends on your test budget and target CPA. Give each concept enough spend to buy two to three purchases at your target CPA before judging it. A brand spending $60,000 a month with 20% in testing and a $45 CPA can support about 20 new ads a week, which in practice means four to six distinct concepts with a few executions each. Concepts matter more than raw ad count."),
            ("What is the difference between Advantage+ shopping and Advantage+ sales campaigns?",
             "Advantage+ shopping campaigns were folded into Advantage+ sales campaigns. A sales campaign runs as Advantage+ when it uses Advantage+ campaign budget, Advantage+ audience in at least one ad set and Advantage+ placements in all ad sets. Ad sets are back, each holding up to 50 ads, the Existing Customer Budget Cap was deprecated, and the old campaign type could no longer be created through the API after early 2026."),
            ("What is a good hook rate for Facebook and Instagram video ads?",
             "Hook rate is 3-second video plays divided by impressions. Good varies a lot by category, price point and placement, so we benchmark against the account’s own last 90 days rather than a universal number. Treat your top quartile of ads as the bar. If a new ad sits in your bottom quartile after a few thousand impressions, rework the first three seconds before changing anything else."),
            ("How fast can I increase my Meta ads budget?",
             "Meta doesn’t publish a threshold. Its examples say a $100 to $101 change is unlikely to restart learning while $100 to $1,000 may. In accounts we run, we raise budgets 15% to 20% at a time, no more than every two to three days, while CPA and MER hold. If MER drops about 10% and stays there for a week, we step back."),
            ("What is MER and why does it matter more than ROAS?",
             "MER, or marketing efficiency ratio, is total store revenue divided by total marketing spend. It’s sometimes called blended ROAS. Platform ROAS only counts sales Meta attributes to itself, which can rise even while the business stays flat. MER shows whether total revenue is growing with spend. Pair it with new-customer CPA so you know the spend is buying new customers rather than repeat orders."),
        ],
        "figures": {
            "mix": {
                "type": "bars",
                "title": "Starting budget split for Meta",
                "sub": "Share of monthly Meta spend by campaign type",
                "items": [["Scaling (Advantage+ sales)", 70, "70%"], ["Testing", 20, "20%"], ["Catalog", 10, "10%"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of an example Meta ads budget split for an eCommerce brand, from First Byte in The Woodlands, Houston",
                "caption": "A starting point from accounts we’ve run. Adjust for launches and catalog size.",
            },
            "matrix": {
                "type": "checklist",
                "title": "A weekly concept test, laid out",
                "sub": "Five concepts, each with a few executions",
                "items": ["Founder story: why we made it (60s and 30s cuts)", "Problem and fix demo: before, after, how", "Customer testimonial: UGC, phone-shot, captioned", "Us vs. the usual: side-by-side comparison", "Offer static: product, price, review quote", "Each concept: 2 to 4 hooks on the same body", "One written hypothesis per concept", "Fixed test length set before launch"],
                "alt": "Checklist of a Meta ads creative test matrix for eCommerce brands, used by First Byte in Houston and The Woodlands",
                "caption": "Concepts first, then hooks. Near-duplicate ads don’t teach you much.",
            },
            "diagnose": {
                "type": "funnel",
                "title": "Where an ad loses the sale",
                "stages": [["Impressions", "10,000"], ["3-second views (hook rate 30%)", "3,000"], ["15-second views (hold rate 25%)", "750"], ["Outbound clicks (CTR 1.2%)", "120"], ["Purchases (CVR 3%)", "4"]],
                "note": "Illustrative example",
                "alt": "Funnel showing hook rate, hold rate, CTR and conversion rate for a Meta video ad, eCommerce example from First Byte, Houston",
                "caption": "Fix the first stage that falls below your account’s norm, and leave the rest alone.",
            },
            "ugc": {
                "type": "compare",
                "title": "One format vs. a creative portfolio",
                "left": {"title": "One look for everything", "items": ["Only polished studio video", "Same model, same set, every ad", "New ads are caption swaps", "Statics treated as an afterthought", "Creators used only for organic posts"]},
                "right": {"title": "A portfolio Meta can match", "items": ["UGC, studio and statics side by side", "Different people and settings", "New concepts every week", "Offer statics for warm buyers", "Best creator posts run as partnership ads"]},
                "alt": "Comparison of single-format versus diversified Meta ad creative for eCommerce brands, by First Byte in The Woodlands, Houston",
                "caption": "Variety in concept and format gives Meta’s delivery system more to work with.",
            },
            "brief": {
                "type": "steps",
                "title": "The one-page creative brief",
                "sub": "Fill this in before anything gets shot or edited",
                "steps": [["Concept and angle", "One sentence: the idea, and which customer it speaks to."], ["Hypothesis", "What it should beat, on which metric, and why we think so."], ["Hook options", "Two to four first-three-second openers, written out."], ["Body and proof", "Demo, testimonial, claim support, offer, call to action."], ["Specs", "Formats (9:16, 4:5, 1:1), lengths, captions, usage rights."], ["Success rule", "Kill, iterate or graduate thresholds for this test."]],
                "alt": "Six-step creative brief template for Meta ads testing for eCommerce brands, from First Byte in Houston and The Woodlands",
                "caption": "The hypothesis line is the one that makes Monday’s review useful.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: Klaviyo flows
    {
        "slug": "ecommerce-email-sms-flows-klaviyo",
        "title": "eCommerce Email and SMS Flows That Make Money: A Klaviyo Build Guide",
        "seo_title": "Klaviyo Email & SMS Flows for eCommerce That Make Money",
        "desc": "The Klaviyo email and SMS flows that make money for Shopify brands: build order, timing, revenue per recipient math, Gmail and Yahoo rules, SMS consent.",
        "category": "Growth",
        "icons": ["Google", "Meta", "Google Analytics"],
        "art": "b4",
        "hero": "sms",
        "hero_alt": "Illustration of a text message for eCommerce email and SMS flows in Klaviyo, from First Byte in The Woodlands, Houston",
        "related": ["email-marketing-basics", "sms-marketing-small-business-texas-rules", "landing-pages-101"],
        "sections": [
            (None, f"""<p>Tuesday afternoon, the week after a big Meta push. The store pulled 9,000 sessions and a few hundred new email signups. The founder opens Klaviyo to see what happened to all those people.</p>
<p>The welcome flow is one email, built in 2023, with a 10% code that expired in the spring. The abandoned checkout flow sends a single message four hours later. There’s no browse abandonment, no post-purchase series, nothing for the customer who bought once and never came back. Every week, paid traffic fills a bucket with a hole in the bottom.</p>
<p>This guide is the build list we use for Shopify and DTC brands on Klaviyo: which flows to build first, how to time them, how to tell whether each one is earning its keep, and the deliverability and SMS consent rules that can quietly shut the whole thing off. If you’re starting from zero, our {L('/blog/email-marketing-basics/', 'email marketing basics')} post covers list building and campaign habits. This one is about automation that sells.</p>"""),

            ("Why flows come before campaigns", f"""<p>Campaigns are the emails you send to a list on a schedule. Flows are the automated messages triggered by what a person does: signs up, views a product, starts checkout, buys, goes quiet. Flows reach people at the moment they’re paying attention, which is why they earn so much more per message.</p>
<p>The numbers back that up. {SRC['kl_email']}, drawn from more than 183,000 Klaviyo customers, put average flow click rates at 5.58% against 1.69% for campaigns, and flow revenue per recipient at nearly 18 times campaign revenue per recipient. On text messages, {SRC['kl_sms']} show flows averaging a 9.65% click rate and a 1.9% order rate, against 5.6% and 0.27% for SMS campaigns, with flows earning roughly eight times the revenue per recipient.</p>
<!--fig:bench-->
<p>Campaigns still matter for launches, restocks and sales. But a store with six good flows and a sensible campaign calendar beats a store with daily campaigns and a broken welcome series almost every time.</p>"""),

            ("Revenue per recipient: the one number to manage flows by", f"""<p>Open rates are close to useless now. Apple Mail Privacy Protection preloads tracking pixels, which, per {SRC['kl_mpp']}, artificially inflates open rates; Klaviyo flags those events with an Apple Privacy Open property you can filter on. Clicks are better. Revenue per recipient (RPR) is best.</p>
<div class="tbl"><table>
<thead><tr><th>Metric</th><th>Formula</th></tr></thead>
<tbody>
<tr><td>Revenue per recipient</td><td>Attributed revenue ÷ recipients (delivered)</td></tr>
<tr><td>Monthly flow revenue</td><td>Monthly people entering the flow × RPR</td></tr>
<tr><td>Placed order rate</td><td>Orders ÷ recipients</td></tr>
<tr><td>Email share of revenue</td><td>Email and SMS attributed revenue ÷ total store revenue</td></tr>
</tbody></table></div>
<p>A worked example. {SRC['kl_cart']} put average abandoned cart email RPR at $6.77, with the top 10% at $13.70. If 1,500 shoppers a month enter your abandoned checkout flow, the average flow earns about $10,155 a month and a top-10% flow about $20,550. That gap, roughly $10,000 a month from one flow, is why we rebuild these before touching anything else.</p>
<!--fig:rpr-->
<p>Two cautions on the math. Klaviyo’s default attribution credits an order to an email opened or clicked within five days, and to a text clicked within five days, per {SRC['kl_attr']}. Some of those buyers would have purchased anyway. For big flows, hold out 10% of entrants with a random split for a few weeks and compare order rates. And watch total store revenue, not only Klaviyo’s attributed number.</p>"""),

            ("The flow build order for a new store", f"""<p>If you’re launching a Shopify store or rebuilding a neglected Klaviyo account, build in this order. Each step is ranked by how much money it touches and how quickly it pays.</p>
<!--fig:order-->
<div class="tbl"><table>
<thead><tr><th>Flow</th><th>Klaviyo trigger</th><th>Messages and timing (our starting point)</th><th>Key filters</th></tr></thead>
<tbody>
<tr><td>Welcome</td><td>Added to list (from your sign-up form)</td><td>3 to 5 emails over 7 to 10 days; 1 to 2 texts for SMS subscribers</td><td>Placed Order zero times since starting flow (or branch buyers out)</td></tr>
<tr><td>Abandoned checkout</td><td>Started Checkout</td><td>Email at 1 hour, 24 hours, 72 hours; text at 30 to 60 minutes</td><td>Placed Order zero times since starting flow</td></tr>
<tr><td>Abandoned cart</td><td>Added to Cart</td><td>Email at 2 to 4 hours and 24 hours</td><td>No Started Checkout or order since starting flow</td></tr>
<tr><td>Browse abandonment</td><td>Viewed Product</td><td>1 to 2 emails, first at least 1 hour later</td><td>No order, checkout or cart since starting; not in flow in last 30 days</td></tr>
<tr><td>Post-purchase</td><td>Placed Order</td><td>Thank-you, how-to, review ask, cross-sell over 2 to 4 weeks</td><td>Split first-time and repeat buyers</td></tr>
<tr><td>Replenishment</td><td>Placed Order (or predicted next order date)</td><td>1 to 2 messages before the product runs out</td><td>Product purchased; no order since</td></tr>
<tr><td>Winback</td><td>Date-based: days since last order</td><td>2 to 3 emails</td><td>No order since entering</td></tr>
<tr><td>Sunset</td><td>Klaviyo’s Sunset segment</td><td>Up to 3 emails, then mark unengaged</td><td>No opens or clicks since starting flow</td></tr>
</tbody></table></div>
<p>Timings and message counts are where we start in accounts we run. Test from there.</p>"""),

            ("Welcome, browse, cart and checkout: catching the intent", f"""<p><b>Welcome.</b> The first email goes immediately and delivers whatever the form promised. The rest should tell the brand story, show the best sellers, answer the objections you hear in customer service (sizing, ingredients, shipping times, returns) and show reviews. Whether to lead with a discount depends on your margins. A 10% code trains people to wait for codes; a free-shipping threshold or a gift with first order often converts as well without cheapening the product. Split buyers out of the series the moment they purchase.</p>
<p><b>Browse abandonment.</b> Per {SRC['kl_browse']}, this flow triggers on the Viewed Product metric, should wait at least an hour, and should exclude anyone who has ordered, started checkout or been in the flow in the last 30 days. Klaviyo also recommends keeping it a lighter touch than cart emails, since viewing is weaker intent. One or two emails showing the product, its reviews and two related items is plenty.</p>
<p><b>Abandoned cart vs. abandoned checkout.</b> These are separate flows with separate triggers. Started Checkout means the person reached Shopify’s checkout and usually gave an email, which makes it the stronger signal and the first flow to build. Added to Cart catches people earlier and needs Klaviyo’s onsite tracking to identify them. Use flow filters so nobody gets both. If Klaviyo is running checkout recovery, turn off Shopify’s own abandoned checkout email so customers don’t get two.</p>
<p>What goes in the messages: the exact products with images and price, a clear button back to the cart, reviews, and answers to the reason people abandon (shipping cost, delivery date, returns). Save any incentive for the last message, and only for first-time buyers. Repeat customers who learn the third email has a code will wait for the third email.</p>"""),

            ("Post-purchase, replenishment and winback: the repeat-order engine", f"""<p><b>Post-purchase.</b> The first order is where most DTC brands lose money and the second order is where they make it. A good post-purchase series sets expectations (shipping, what’s in the box), teaches people to use the product so they don’t return it, asks for a review once it has arrived and been used, and only then suggests what to buy next. Split first-time buyers from repeat buyers. A loyal customer on her fifth order doesn’t need the brand story again.</p>
<p><b>Replenishment.</b> For consumables like supplements, coffee, skincare or pet food, this is often the most profitable flow in the account. Klaviyo’s predictive analytics can estimate each customer’s expected date of next order, but per {SRC['kl_predict']}, the account needs at least 500 customers who have placed orders, at least 180 days of order history with orders in the last 30 days, and some customers with three or more orders. Until you hit that, use a fixed delay based on the product: if a bag lasts 30 days, send the reminder around day 24 or 25, and a second one at day 30 if they haven’t reordered.</p>
<p><b>Winback.</b> Time it from your real repurchase cycle, not a template. Pull the median days between first and second orders from Shopify, then trigger winback at roughly one and a half to two times that number. A brand whose customers reorder every 45 days might start winback at day 75. Lead with what’s new; hold the bigger offer for the last email.</p>
<p>Subscription brands should coordinate all of this with their subscription app so subscribers don’t get “running low?” emails for a box that ships Tuesday.</p>"""),

            ("Sunset flows and list hygiene", f"""<p>Mailing people who never open costs more than the platform fee. Gmail and Yahoo watch how recipients respond, and a list full of dead addresses drags down inbox placement for everyone else.</p>
<p>Klaviyo’s prebuilt Sunset (Email) segment, as described in {SRC['kl_sunset']}, includes profiles created at least 180 days ago that received at least five emails in the last 72 weeks and have no recorded opens, clicks, site activity, product views, checkouts or orders. The guide recommends no more than three emails in the flow, a short wait after the last one, and a property update that sets Unengaged to true. Suppression isn’t automatic: you build a segment of Unengaged profiles and suppress its current members yourself.</p>
<p>Because of Apple’s privacy opens, we also build engaged segments with the filter “Apple Privacy Open is false,” which Klaviyo itself recommends, so a pixel prefetch doesn’t count as a real person reading.</p>"""),

            ("Deliverability: what Gmail, Yahoo and Microsoft now require", f"""<p>In October 2023, Google announced that starting in February 2024, anyone sending more than 5,000 messages a day to Gmail addresses would have to authenticate their email, offer one-click unsubscribe and process unsubscribes within two days, per {SRC['gmail']}. {SRC['yahoo']} sets matching rules: SPF and DKIM, a DMARC policy of at least p=none that passes, alignment with the From domain, a List-Unsubscribe header with one-click support, unsubscribes honored within two days, and a spam complaint rate kept below 0.3%.</p>
<p>Enforcement has tightened since. {SRC['redsift']} reported that starting in November 2025, Gmail ramped up enforcement on non-compliant traffic with temporary rate limits and outright rejections, and recommended keeping the user-reported spam rate below 0.1% and never letting it reach 0.3%. Gmail treats bulk sender status as permanent once you cross 5,000 a day. Microsoft joined in May 2025 for domains sending more than 5,000 messages a day to Outlook.com, with SPF, DKIM, DMARC at p=none or stronger and alignment, and said it would reject non-compliant bulk mail, per {SRC['msft']}.</p>
<!--fig:deliver-->
<p>In Klaviyo, that means setting up a branded sending domain instead of sending on Klaviyo’s shared domain, publishing a DMARC record with your DNS provider, and checking that the one-click unsubscribe header is on. Then watch spam complaints in Google Postmaster Tools. A store that grew its list with a giveaway is the classic case of a spam rate that creeps up without anyone noticing.</p>"""),

            ("SMS consent: TCPA, Texas SB 140 and quiet hours", f"""<p>SMS earns well, and it carries legal risk email doesn’t. We wrote a full {L('/blog/sms-marketing-small-business-texas-rules/', 'guide to Texas SMS marketing rules')}; here’s the short version for eCommerce brands.</p>
<p><b>Consent.</b> FCC rules under the TCPA call for prior express written consent for marketing texts sent with automated systems, and the consent can’t be a condition of purchase. A February 2026 Fifth Circuit decision (the circuit that covers Texas) held that the statute itself doesn’t require the consent to be written for telemarketing calls, per {SRC['hklaw']}. We wouldn’t build a text program on that: carriers and platforms still require documented opt-in. That’s why Klaviyo’s SMS forms carry compliance language and a separate SMS opt-in from email. Keep the record of when and where each number opted in.</p>
<p><b>Quiet hours.</b> {SRC['cfr']} bars telephone solicitations before 8 a.m. or after 9 p.m. in the recipient’s local time. Some states are stricter. {SRC['kl_quiet']} explains that flows hold messages until quiet hours end, using the profile’s time zone or, in the U.S. and Canada, the phone’s area code. Klaviyo also offers state-level quiet hours, which are the default for new customers, and caps promotional texts at three per rolling 24 hours for recipients in Florida, Oklahoma, Oregon and Maryland, per {SRC['kl_state']}.</p>
<p><b>Texas.</b> SB 140 brought text messages under the state’s telephone solicitation law in September 2025, with a registration scheme that carries a $200 fee and a $10,000 security deposit. After a November 2025 settlement, the {SRC['sos']} now says a business sending texts with the consumer’s prior consent isn’t required to register. {SRC['nlr']} still flags cold texting and purchased lists as squarely covered, notes that private lawsuits under the Texas Deceptive Trade Practices Act remain possible, and recommends applying Texas calling hours (9 a.m. to 9 p.m. Monday through Saturday, noon to 9 p.m. Sunday) to texts as a precaution. We schedule Texas sends inside those hours.</p>
<!--fig:consent-->
<p>This is our reading as marketers, not legal advice. If you text customers in many states, have counsel review your opt-in language once and your sending rules once a year.</p>"""),

            ("Growing the list: popups that work without annoying people", f"""<p>Every flow above depends on list size, and most list growth comes from the popup. {SRC['kl_forms']} calls a 3% submit rate a low bar, puts standard popups in a 3% to 8% range, and says exit-intent and phone-number-only forms run 10% to 13%. It recommends against firing the form on page load and suggests something like a five-second delay combined with 20% scroll depth.</p>
<p>What we set up for most stores:</p>
<ul>
<li>A two-step form: email first, then a second step asking for a phone number with SMS consent. People who give one often give the other.</li>
<li>A different form for mobile and desktop, since most DTC traffic is mobile and a desktop-sized popup is the fastest way to lose it.</li>
<li>A teaser tab, so someone who closes the form can still find it.</li>
<li>A clear exchange: first-order offer, early access, a quiz result or a sample. “Join our newsletter” isn’t an offer.</li>
<li>Paid traffic in mind. If you’re sending Meta traffic to a landing page, the form timing and offer should match the ad. Our {L(META, 'Meta creative testing system')} pairs with this.</li>
</ul>
<p>Lists built around a launch can work extremely well when nurture is ready before the traffic arrives. For {L('/case-studies/equinox/', 'Equinox club launches')}, our team ran CRM, SMS and email nurture that turned waitlists into signed members, part of a program that produced 11,400 founding-member leads. The same principle applies to a product drop: build the flows first, then turn on the ads.</p>"""),

            ("What to track, and a first 90 days", f"""<p>A monthly flow report needs only a handful of numbers per flow: recipients, click rate, placed order rate, RPR and total revenue, plus account-wide spam complaint rate, unsubscribe rate and list growth. Compare RPR month over month for each flow and against {SRC['kl_cart']} and the other Klaviyo benchmarks cited above where they exist. Klaviyo doesn’t publish separate benchmarks for every flow type, so for welcome, post-purchase and winback, your own trend line is the benchmark.</p>
<p><b>Days 1 to 30.</b> Authenticate the sending domain and set DMARC. Build or rebuild welcome and abandoned checkout. Launch the two-step popup. Turn off Shopify’s duplicate checkout email.</p>
<p><b>Days 31 to 60.</b> Add abandoned cart, browse abandonment and post-purchase. Add SMS to welcome and checkout for consented subscribers, with quiet hours on. Set up the holdout split on checkout recovery.</p>
<p><b>Days 61 to 90.</b> Build replenishment and winback from your real reorder timing. Launch the sunset flow and suppress the dead weight. Start A/B testing subject lines and offers in the highest-volume flows.</p>
<p>If you also run Google Shopping, our {L('/blog/google-shopping-ads-shopify-setup-guide/', 'Shopify Shopping setup guide')} covers the paid side of the same funnel, and our {L('/industries/ecommerce/', 'eCommerce work')} shows how we tie it together. If you’d like a senior strategist to look at your store, your list and your goals and build a custom flow plan, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("What Klaviyo flows should a new Shopify store build first?",
             "Start with a welcome series and an abandoned checkout flow, because they reach the most people at the highest intent. Then add abandoned cart, browse abandonment and post-purchase. Replenishment and winback come next, timed from your real reorder cycle, and a sunset flow keeps the list clean. Authenticate your sending domain before any of it so the messages reach the inbox."),
            ("What is a good revenue per recipient for an abandoned cart flow?",
             "Klaviyo’s 2026 abandoned cart benchmark report puts average email revenue per recipient at $6.77 and the top 10% at $13.70, with SMS at $4.48 and $8.69. Treat those as reference points, not targets, because price point and category change them a lot. Track your own RPR monthly and use a holdout group to check how much of that revenue the flow really created."),
            ("What are the Gmail and Yahoo bulk sender requirements?",
             "Since February 2024, senders of more than 5,000 messages a day to Gmail must authenticate with SPF and DKIM, publish a DMARC policy of at least p=none, align with the From domain, offer one-click unsubscribe and honor it within two days. Yahoo has matching rules and a 0.3% spam complaint ceiling. Gmail tightened enforcement in November 2025, and Microsoft added similar rules for Outlook.com in May 2025."),
            ("Do I need to register in Texas to send marketing texts?",
             "SB 140 brought text messages under Texas telephone solicitation law in September 2025. After a November 2025 settlement, the Texas Secretary of State’s FAQ says businesses that text consumers with prior consent aren’t required to register. Cold texting and purchased lists remain covered, and private lawsuits under the Texas Deceptive Trade Practices Act are still possible. Keep consent records and ask your attorney about your situation."),
            ("How often should an eCommerce brand send SMS?",
             "Most brands do well with flow texts plus two to six campaign texts a month, but frequency should follow results and unsubscribe rates. Respect quiet hours: federal rules bar solicitations before 8 a.m. or after 9 p.m. local time, and some states are stricter. Klaviyo caps promotional texts at three per 24 hours for Florida, Oklahoma, Oregon and Maryland recipients."),
        ],
        "figures": {
            "bench": {
                "type": "stats",
                "title": "Flows vs. campaigns in Klaviyo",
                "stats": [["5.58%", "average email flow click rate"], ["1.69%", "average email campaign click rate"], ["~18x", "email flow RPR vs. campaigns"], ["9.65%", "average SMS flow click rate"]],
                "note": "Source: Klaviyo 2026 email and SMS benchmarks",
                "alt": "Stats comparing Klaviyo email and SMS flow and campaign benchmarks for eCommerce brands, from First Byte in Houston",
                "caption": f"From {SRC['kl_email']} and {SRC['kl_sms']}.",
            },
            "order": {
                "type": "steps",
                "title": "Flow build order for a new store",
                "sub": "Highest intent and fastest payback first",
                "steps": [["Welcome", "Deliver the signup promise, tell the story, split out buyers."], ["Abandoned checkout", "Started Checkout trigger; email plus SMS for consented subscribers."], ["Cart and browse", "Added to Cart and Viewed Product, with filters so nobody gets both."], ["Post-purchase", "Expectations, how-to, review ask, then cross-sell."], ["Replenishment and winback", "Timed from your real reorder cycle."], ["Sunset", "Up to three emails, then suppress the unengaged."]],
                "alt": "Six-step Klaviyo flow build order for a new Shopify store, from First Byte in The Woodlands, Houston",
                "caption": "Authenticate your sending domain before step one.",
            },
            "rpr": {
                "type": "bars",
                "title": "Abandoned cart revenue per recipient",
                "sub": "Klaviyo 2026 benchmark report",
                "items": [["Email, top 10%", 13.70, "$13.70"], ["SMS, top 10%", 8.69, "$8.69"], ["Email, average", 6.77, "$6.77"], ["SMS, average", 4.48, "$4.48"]],
                "highlight": [0],
                "note": "Source: Klaviyo 2026 Abandoned Cart Benchmark Report",
                "alt": "Bar chart of Klaviyo abandoned cart revenue per recipient benchmarks for email and SMS, eCommerce guide from First Byte, Houston",
                "caption": f"From {SRC['kl_cart']}.",
            },
            "deliver": {
                "type": "checklist",
                "title": "Bulk sender checklist",
                "sub": "Gmail, Yahoo and Outlook.com requirements for 5,000+ a day",
                "items": ["SPF passes for your sending domain", "DKIM signs every message", "DMARC published, at least p=none", "From domain aligns with SPF or DKIM", "One-click unsubscribe header on", "Unsubscribes honored within 2 days", "Spam rate under 0.1%, never 0.3%", "Branded sending domain in Klaviyo"],
                "alt": "Checklist of Gmail, Yahoo and Microsoft bulk email sender requirements for eCommerce brands, from First Byte in The Woodlands, Houston",
                "caption": "Check Google Postmaster Tools monthly once you’re sending at volume.",
            },
            "consent": {
                "type": "compare",
                "title": "SMS list building: risky vs. safer",
                "left": {"title": "Risky", "items": ["Texting numbers from orders without opt-in", "Buying or renting phone lists", "Consent buried in terms of service", "Sending at 7 a.m. or 10 p.m.", "No record of when someone opted in"]},
                "right": {"title": "Safer", "items": ["Separate SMS checkbox or keyword opt-in", "Only numbers that opted in to you", "Clear disclosure on the form itself", "Quiet hours and state rules switched on", "Consent timestamp and source stored"]},
                "alt": "Comparison of risky and safer SMS consent practices for eCommerce brands texting customers in Texas, from First Byte, Houston",
                "caption": "Our reading as marketers. Have counsel review your opt-in language.",
            },
        },
    },
]
