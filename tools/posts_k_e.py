"""Batch 11 (Restaurants and Hospitality): restaurant direct online ordering vs. delivery apps, and hotel/resort
group sales marketing for weddings, corporate meetings and events.

Research, restaurant post: DoorDash merchant pricing page (Basic 15%, Plus 25%, Premier 30%, pickup 6%, Online Ordering
by DoorDash at 0% commission plus processing); Uber Eats US merchant pricing page (Lite 20%, Plus 25% with +5% on Uber
One orders, Premium 30%, pickup 7% with validated in-store pricing or 10% without, Webshop 2.5% + $0.29, Uber Direct from
$7.99) and Restaurant Dive on the March 2026 Uber Eats increase; Houston Chronicle (Jan 2021) on HB 598 and Phat Eatery;
LegiScan (HB 598 died in committee); Texas Legislature bill analysis of SB 911 (Bus. & Com. Code ch. 114, written fee
agreements, 10-day removal, local preemption, effective Jan 1, 2022); ChowNow pricing page (plans from $229, 2.95% +
$0.29 processing, Flex Delivery $7.98); Toast online ordering product page (commission-free, flat delivery fee, Google
integration, loyalty); Square online ordering page (free plan, no added monthly fees); Olo’s Spendgo press release
(750+ brands); Google Business Profile help on managing food ordering; Google Ads help on local actions conversions;
National Restaurant Association 2025 off-premises report press release; Morgan Lewis on Texas SB 140.
Hotel post: Cvent press release on 2024 CSN group sourcing ($16.5B, room nights +16% vs 2019, 80% expect a reply within
four days); Cvent 2026 Planner Sourcing Report blog (1,650+ planners, four business days, 24% frustrated by slow
replies, specs 50% / photos and video 48% / floor plans 46%, 48% sourcing non-hotel venues); Cvent CSN advertising page
(155K+ sourcing planners, nearly 340,000 venues, Diamond Listings, competitive ads); Hotel Online’s 2027 group sales
stats roundup (CoStar group demand, shrinking booking windows, 39% drop a non-responding venue within two days for
small meetings, 86% online booking, ~70% use AI tools); Houston First on the U.S. News Best Conference Cities ranking
(No. 5, 517 meetings and 881,737 room nights booked in 2025); Axios Houston on the GRB expansion (700,000 sq ft, 60,000
sq ft ballroom, May 2028); OTC’s 2026 wrap release (nearly 25,000 attendees); RODEOHOUSTON 2026 dates; Community Impact
on The Woodlands Waterway Marriott (65,000 sq ft of meeting space); The Knot 2026 Real Weddings Study ($34,000 average,
117 guests, $292 per guest, 13 vendors); LinkedIn’s ad targeting page.
Case studies read: site/case-studies/the-toasted-yolk-cafe/ and site/case-studies/viceroy-los-cabos/ (numbers quoted
only as they appear there).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # restaurant post
    "dd": A("https://merchants.doordash.com/en-us/products/pricing", "DoorDash’s merchant pricing page"),
    "ue": A("https://merchants.ubereats.com/us/en/pricing/", "Uber Eats’ merchant pricing page"),
    "ue_dive": A("https://www.restaurantdive.com/news/uber-eats-increases-marketplace-fees/814294/", "Restaurant Dive"),
    "chron": A("https://www.pressreader.com/usa/houston-chronicle/20210118/282441351739635", "the Houston Chronicle"),
    "hb598": A("https://legiscan.com/TX/bill/HB598/2021", "died in committee"),
    "sb911": A("https://capitol.texas.gov/tlodocs/87R/analysis/html/SB00911F.htm", "the Legislature’s bill analysis of SB 911"),
    "chownow": A("https://get.chownow.com/pricing/", "ChowNow’s pricing page"),
    "toast": A("https://pos.toasttab.com/products/online-ordering", "Toast’s online ordering page"),
    "square": A("https://squareup.com/us/en/online-ordering", "Square’s online ordering page"),
    "olo": A("https://www.businesswire.com/news/home/20251222826702/en", "more than 750 restaurant brands"),
    "gbp": A("https://support.google.com/business/answer/10842217", "Google’s help page on food ordering"),
    "localact": A("https://support.google.com/google-ads/answer/9013908", "Google Ads’ local actions documentation"),
    "nra": A("https://restaurant.org/research-and-media/media/press-releases/from-trend-to-transformation-off-premises-dining-now-essential-for-restaurant-consumers,-operators/", "National Restaurant Association’s 2025 off-premises report"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    # hotel post
    "cvent24": A("https://cvent.com/en/press-release/cvent-group-sourcing-volume-sets-new-record-2024", "Cvent’s 2024 sourcing release"),
    "cvent26": A("https://www.cvent.com/en/blog/hospitality/2026-Global-Cvent-Planner-Sourcing-Report", "Cvent’s 2026 Planner Sourcing Report"),
    "csnads": A("https://www.cvent.com/supplier-venue/advertising", "Cvent’s advertising page"),
    "ho": A("https://www.hotel-online.com/news/20-stats-every-hotel-group-sales-team-should-know-to-prepare-for-2027", "Hotel Online’s roundup of group sales stats"),
    "hfirst": A("https://www.houstonfirst.com/news/houston-among-nations-top-5-best-convention-cities-says-us-news-world-report", "Houston First"),
    "axios": A("https://www.axios.com/local/houston/2026/04/16/houston-convention-center-renovations-george-r-brown", "Axios Houston"),
    "otc": A("https://www.otcnet.org/press-releases/otc-2026-wraps-four-days-dialogue-offshore-energys-next-frontiers", "OTC’s closing release"),
    "rodeo": A("https://www.rodeohouston.com/plan-your-visit/international-days/", "RODEOHOUSTON"),
    "ci_marriott": A("https://communityimpact.com/the-woodlands/business/take-a-look-inside-the-renovated-the-woodlands-waterway-marriott-hotel-convention-center/", "Community Impact"),
    "knot": A("https://www.theknotww.com/press-releases/the-knot-worldwide-unveils-2026-real-weddings-study", "The Knot’s 2026 Real Weddings Study"),
    "li": A("https://business.linkedin.com/advertise/ads/targeting", "LinkedIn’s targeting options"),
}

ORDER = "/blog/restaurant-direct-online-ordering-vs-delivery-apps/"
GROUP = "/blog/hotel-group-sales-marketing-weddings-meetings-events/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: direct online ordering
    {
        "slug": "restaurant-direct-online-ordering-vs-delivery-apps",
        "title": "Restaurant Online Ordering: Winning Direct Orders Back From Delivery Apps",
        "seo_title": "Restaurant Direct Ordering vs. Delivery Apps: Win Orders",
        "desc": "Win direct online orders back from DoorDash and Uber Eats: 2026 commission math, Google ordering links, loyalty, SMS, menu pricing and channel mix tracking.",
        "category": "Strategy",
        "icons": ["Google Business Profile", "Google Ads", "Instagram"],
        "art": "b2",
        "hero": "receipt",
        "hero_alt": "Illustration of an order receipt for restaurant direct online ordering in Houston and The Woodlands",
        "related": ["restaurant-marketing-the-woodlands-houston", "sms-marketing-small-business-texas-rules", "google-business-profile-number-one-asset"],
        "sections": [
            (None, f"""<p>Friday, 6:40 p.m. Three tablets on the pass are chirping at once. The expo is reading tickets off DoorDash, Uber Eats and your own ordering page, and the driver for order #4471 is leaning on the counter asking how much longer.</p>
<p>Order #4471 is a woman who has eaten at your place in Spring every other Friday for four years. She ordered through the app because the app was on her phone and your website wasn’t. On a $46 order, the app kept somewhere between $7 and $14 of your money, and it kept her email address too.</p>
<p>That’s the problem this post is about. You probably can’t quit the delivery apps, and we wouldn’t tell you to. They find you new customers, and some of those customers will only ever order through an app. What you can do is stop paying a marketplace commission on regulars who already know you. The job is to make your own ordering channel the easiest way to order for anyone who has ordered before, and then to measure the mix every week like it’s food cost.</p>
<p>Our {L('/blog/restaurant-marketing-the-woodlands-houston/', 'general restaurant marketing guide')} covers reviews, social and slow nights. This one stays on ordering.</p>"""),

            ("The commission math, per order, at 2026 rates", f"""<p>Start with what each order actually costs. The published marketplace rates as of this writing:</p>
<ul>
<li><b>DoorDash.</b> Basic is 15% of the order subtotal, Plus is 25% and Premier is 30%. Pickup orders are 6% on every plan. There’s no activation or subscription fee, and payment processing is included in the commission, per {SRC['dd']}.</li>
<li><b>Uber Eats.</b> Lite went from 15% to 20% in March 2026, Plus stayed at 25% with Uber One member orders moving to 30%, and Premium stayed at 30%, per {SRC['ue_dive']}. Pickup went from 6% to 7% when you have validated in-store pricing, and 10% when you don’t. {SRC['ue']} also notes Lite rates are lower in some cities, so check the rate for your address.</li>
</ul>
<p>The tiers aren’t identical products. Each plan comes with different reach and perks, so read what yours includes on the pricing page. A cheaper tier that brings fewer orders isn’t cheaper, so compare what you paid per order you actually got, not the headline rate.</p>
<p>Here’s what a $40 subtotal costs you by channel. The direct rows use ChowNow’s published processing fee and Uber’s Webshop fee as examples; your own processor will differ a little.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Fee rate</th><th>Fee on $40</th><th>You keep</th></tr></thead>
<tbody>
<tr><td>DoorDash Premier or Uber Eats Premium, delivery</td><td>30%</td><td>$12.00</td><td>$28.00</td></tr>
<tr><td>DoorDash Plus or Uber Eats Plus, delivery</td><td>25%</td><td>$10.00</td><td>$30.00</td></tr>
<tr><td>Uber Eats Lite, delivery</td><td>20%</td><td>$8.00</td><td>$32.00</td></tr>
<tr><td>DoorDash Basic, delivery</td><td>15%</td><td>$6.00</td><td>$34.00</td></tr>
<tr><td>Uber Eats pickup, no validated in-store pricing</td><td>10%</td><td>$4.00</td><td>$36.00</td></tr>
<tr><td>DoorDash pickup</td><td>6%</td><td>$2.40</td><td>$37.60</td></tr>
<tr><td>Your own site, pickup (2.95% + $0.29 processing)</td><td>~3.7%</td><td>$1.47</td><td>$38.53</td></tr>
</tbody></table></div>
<!--fig:commission-->
<p>Two things fall out of that table. The biggest saving is moving a regular from app delivery to direct pickup, about $8.50 to $10.50 an order at the common tiers. And app pickup is already fairly cheap, so if a guest insists on the app, nudging them to pickup inside the app still helps.</p>
<p>Direct delivery is a different calculation. You still need a driver. Uber Direct starts at $7.99 per delivery, ChowNow lists Flex Delivery at $7.98 an order, and Toast sells delivery as a flat fee per order. Most restaurants pass some or all of that to the guest as a delivery fee. Even then the direct order is usually cheaper than a 25% or 30% commission on anything above about $30.</p>"""),

            ("Is there a delivery fee cap in Houston?", f"""<p>No. We get this question a lot because Chicago, San Francisco, New York and others capped delivery commissions during the pandemic, and some kept the caps. Houston never did, and Texas went the other way.</p>
<p>In 2021, a bill to cap delivery app fees in Texas at 15% (HB 598) drew plenty of press. Katy restaurateur Alex Au-yeung of Phat Eatery told {SRC['chron']} at the time, “If you give 30 percent away, how can we survive?” The bill {SRC['hb598']}.</p>
<p>What passed instead was SB 911, which created Chapter 114 of the Business and Commerce Code and took effect January 1, 2022, per {SRC['sb911']}. In plain terms:</p>
<ul>
<li>A delivery service can’t charge you a fee, or make you absorb one, unless a written agreement authorizes it and states each fee.</li>
<li>It can’t use your name or logo in a way that suggests you endorse it.</li>
<li>If you have no agreement and ask to be removed, it has 10 days to take you down, and it can’t re-add you without written consent.</li>
<li>Cities and counties can’t adopt rules that affect the terms of those agreements, which effectively rules out a local Houston cap.</li>
</ul>
<p>So in Houston the fee is whatever you signed. Pull your current agreement, find the tier, and check whether marketing programs or promotions add charges on top. Then decide on the tier with real order data in front of you. We’re marketers, not your lawyer, so anything contractual goes past them.</p>"""),

            ("Choosing a first-party ordering platform", f"""<p>You need an ordering page that’s yours, plugged into your POS, fast on a phone, and able to remember a guest. Most independents and small groups end up with one of these:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Option</th><th>What it is</th><th>Published pricing notes</th><th>Best fit</th></tr></thead>
<tbody>
<tr><td>Toast Online Ordering</td><td>Ordering built into Toast POS, with loyalty and a Google ordering integration</td><td>Commission-free ordering and flat delivery fees, per {SRC['toast']}; pricing by quote</td><td>Restaurants already on Toast</td></tr>
<tr><td>Square Online</td><td>Ordering site tied to Square POS</td><td>Free plan with no added monthly fees, paid plans above it, per {SRC['square']}</td><td>Counter service, cafés, food trucks on Square</td></tr>
<tr><td>ChowNow</td><td>Standalone ordering, branded apps and marketing tools</td><td>Entry plan listed at $229 to $249 a month, setup $119 to $499, 2.95% + $0.29 processing, per {SRC['chownow']}</td><td>Independents on a POS without strong native ordering</td></tr>
<tr><td>Olo</td><td>Enterprise ordering, payments and loyalty for multi-unit brands</td><td>Custom contracts; Olo says it serves {SRC['olo']}</td><td>Franchise and multi-unit groups</td></tr>
<tr><td>Online Ordering by DoorDash / Uber Eats Webshop</td><td>Commission-free ordering sites run by the apps</td><td>DoorDash: 0% commission plus processing; Uber: 2.5% + $0.29 per order</td><td>Fast start; you stay inside the app company’s system</td></tr>
</tbody></table></div>
<p>How we’d pick. Native to your POS beats bolted on, because menu changes, 86’d items and prep times sync without someone retyping them at 5 p.m. The checkout should take a returning guest under a minute on a phone. And make sure you own the guest list: name, phone, email and order history, exportable. If you can’t download your customers, you’ve swapped one landlord for another.</p>
<p>Speed matters more than design. We’ve seen ordering pages that took eight seconds to load on LTE in a parking lot on Kuykendahl. Test yours on your own phone, off Wi-Fi, before you spend a dollar sending people to it.</p>"""),

            ("Make Google send orders to you", f"""<p>Plenty of “order online” journeys start on Google, not on an app. Someone searches your name or “pho near me,” sees your Business Profile, and taps Order. Which provider that button opens is a setting most owners have never looked at.</p>
<p>Per {SRC['gbp']}, in your Business Profile go to <b>Food ordering</b>, pick your own ordering provider (or add your link at the bottom with <b>Add a link</b>), then select <b>Set as preferred</b> and turn on <b>Preferred for pickup</b> and <b>Preferred for delivery</b>. You can also choose <b>Show provider to customers</b> on any third-party provider and switch it off for pickup, delivery or both. Changes usually show up in Search and Maps within a few hours.</p>
<!--fig:google-->
<p>Hiding the apps entirely is a judgment call. If 30% of your delivery volume comes through Google and you don’t run your own drivers, hiding DoorDash may just send that guest to the next restaurant. A middle path we like: set your own link as preferred for pickup, keep one app visible for delivery, and revisit after a month of data.</p>
<p>The rest of Google matters too. Put a large “Order pickup” button at the top of your website on mobile, ahead of the hero photo. Make sure the menu on your profile matches the menu on your ordering page. If you run Google Ads with location assets, the “Order” clicks from your profile show up as a local actions conversion, though Google treats it as reporting-only and won’t bid on it, per {SRC['localact']}. It’s still a free read on how many people try to order from Maps.</p>
<p>When we opened locations for {L('/case-studies/the-toasted-yolk-cafe/', 'The Toasted Yolk Cafe')}, location pages and Business Profiles went live before the doors opened, and the case study shows 21 days to No. 1 in the local map pack. A profile that ranks is only half the job. The order button has to point somewhere you keep the margin. More on profiles in our {L('/blog/google-business-profile-number-one-asset/', 'Google Business Profile guide')}.</p>"""),

            ("Menu pricing parity: what to charge where", f"""<p>A lot of restaurants mark up their app menus 15% to 25% to cover commission. That’s a normal practice and nothing to be embarrassed about. The question is what you show on your own channel.</p>
<p>Our default: your direct ordering page matches in-store prices, and the apps carry the markup. Then the guest who compares sees that ordering direct is cheaper, and you can say so in plain words on the bag, the receipt and the website. “Same menu, lower prices when you order from us.”</p>
<!--fig:parity-->
<p>Watch one rule. Uber Eats now ties its pickup rate to price parity: 7% with validated in-store pricing and 10% without, per {SRC['ue']}. If your Uber menu is marked up, your Uber pickup orders cost more. Some restaurants keep a separate, unmarked pickup menu for that reason. Your POS or menu management tool should make that a setting rather than a second menu someone forgets to update.</p>
<p>Don’t try to win on discounts alone. A permanent 20%-off code on direct orders teaches guests to wait for a code. Price parity plus a loyalty reward gets you there with less margin given away.</p>"""),

            ("Loyalty and SMS: give the regular a reason", f"""<p>Here’s where direct ordering pays for itself. Your regulars already like the food. They need a reason to open your link instead of the app, and the reason is usually a perk the app can’t match.</p>
<p>The National Restaurant Association’s 2025 off-premises report says more than 60% of takeout and delivery customers say a membership program affects where they order, and nearly 9 in 10 would use limited-time, app-only offers, per the {SRC['nra']}. The same report puts off-premises at nearly 75% of all restaurant traffic.</p>
<p>A loyalty design that works for most independents:</p>
<ul>
<li>Points on direct orders only. Spend $100, get $10 off. Simple enough to explain at the register in one sentence.</li>
<li>A sign-up reward the first time someone orders direct (a free side, a dessert, a drink).</li>
<li>A birthday reward, which earns you the birthday field and a reason to text once a year.</li>
<li>A “we miss you” offer at 30 or 45 days since the last order, sent automatically.</li>
</ul>
<p>Toast Loyalty, Square Loyalty, ChowNow’s marketing tools and Olo’s loyalty product (Olo bought Spendgo in late 2025) all handle this. Pick the one your ordering platform already talks to.</p>
<p>Text messages move direct orders faster than email, and they need care. Get marketing consent separately from order updates, keep the record, and send fewer messages than you think you should (we like two or three a month at most). Texas brought marketing texts under its telephone solicitation law with SB 140, effective September 1, 2025, with some exemptions, per {SRC['sb140']}. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} walks through the consent setup.</p>
<p>A sample text that works: “Gino’s: Friday pickup is open till 9. Order direct and your 4th order this month is on us. [link] Reply STOP to opt out.”</p>"""),

            ("Packaging inserts: the bag is your best ad", f"""<p>Every delivery bag is a direct mail piece that lands in the hands of someone who just bought from you. It costs you a few cents to print. Most restaurants put nothing in it.</p>
<p>The NRA report found 90% of consumers would order a wider variety of items if food held its quality in delivery, and more than half would pay more for packaging that protects it. So the bag carries two messages: the food travels well, and next time order from us.</p>
<!--fig:insert-->
<p>Keep the card small and the ask single. One QR code, one offer, one sentence. Use a unique tracked link (a UTM-tagged URL or a short link for each app) so you can tell whether DoorDash bags or Uber bags convert better. Pickup is the easiest ask, because the guest saves the delivery fee and you save the commission.</p>
<p>Read your marketplace agreement before you start. Platform terms on customer data and in-bag promotions change, and you want to know where the lines are before you print 5,000 cards.</p>"""),

            ("Ads that point to direct ordering", f"""<p>Paid ads for ordering are cheap to run and easy to get wrong. The goal is narrow: catch people who already want your food and send them to your link, not the app.</p>
<p><b>Google brand search.</b> In accounts we’ve looked at, delivery apps and aggregators sometimes show up on a restaurant’s own name. A small brand campaign on terms like “[name] menu,” “[name] order online,” “[name] delivery” and “[name] Spring TX,” sending clicks to your ordering page, usually costs very little and puts your link above theirs. Add negatives like jobs, hiring, careers, application, nutrition and calories.</p>
<p><b>Meta to people who know you.</b> Upload your opted-in customer list as a Custom Audience and retarget website visitors, then run a simple offer to them: the direct-order reward, a new item, a rainy-day pickup special. Keep a broad radius campaign for discovery small. The apps already do discovery, and you’re paying them for it.</p>
<p>Sample ad copy for Meta:</p>
<ul>
<li>Primary text: “Same tacos. Lower prices when you order direct. Pickup in 15 minutes on Woodlands Parkway.”</li>
<li>Headline: “Order pickup direct and save”</li>
<li>Button: Order Now, linked to your ordering page with a UTM tag.</li>
</ul>
<p>An illustrative starting budget for a single location: $300 to $600 a month on brand search and $500 to $1,500 on Meta retargeting and customer-list ads. It’s an example to adjust, not a benchmark. Track direct orders as the conversion in both platforms, which our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'conversion tracking guide')} covers. If you want a team to run it, that’s our {L('/services/paid-social-advertising/', 'paid social')} and {L('/services/search-marketing/', 'search marketing')} work.</p>"""),

            ("Measure channel mix like a P&L line", f"""<p>If you only look at total sales, you’ll never see the shift. Put these on one sheet and review it every Monday with the same weight as food and labor.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Formula</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Direct share</td><td>Direct off-premises orders ÷ all off-premises orders</td><td>The number you’re trying to move</td></tr>
<tr><td>Effective commission rate</td><td>All marketplace fees ÷ marketplace sales</td><td>Shows what your tier really costs once promos and fees are in</td></tr>
<tr><td>Contribution per order, by channel</td><td>Order subtotal − fees − packaging − food cost</td><td>Some app orders lose money; this shows which</td></tr>
<tr><td>Direct repeat rate</td><td>Direct guests with 2+ orders in 60 days ÷ direct guests</td><td>Whether loyalty is working</td></tr>
<tr><td>Cost per new direct guest</td><td>Direct-ordering ad and insert spend ÷ first-time direct guests</td><td>Whether your marketing pays back</td></tr>
</tbody></table></div>
<p>Illustrative example: a Katy café does 600 app delivery orders a month at a $38 average on a 25% tier, or $5,700 in commission. Move 120 of those regulars to direct pickup at about $1.41 in processing each, and it saves roughly $970 a month, close to $11,700 a year, before counting the loyalty cost. Your numbers will differ. The direction usually doesn’t.</p>
<!--fig:mix-->
<p>Don’t judge it in a week. Direct share tends to climb slowly over two or three months as regulars try the link once, get their reward, and switch for good.</p>"""),

            ("The first 90 days", f"""<p>If we were starting your direct ordering push on Monday:</p>
<ol>
<li><b>Days 1 to 30.</b> Pull your delivery agreements and a month of orders by channel. Pick or fix your ordering platform. Set your own link as preferred in Business Profile food ordering. Put an Order pickup button at the top of the mobile site. Set in-store pricing on direct ordering.</li>
<li><b>Days 31 to 60.</b> Launch loyalty with a first-direct-order reward. Start bag inserts with tracked QR codes. Turn on SMS opt-in at checkout. Launch the brand search campaign.</li>
<li><b>Days 61 to 90.</b> Add Meta customer-list and retargeting ads. Review the channel mix sheet weekly. Revisit your marketplace tier with three months of real data.</li>
</ol>
<p>None of this means turning off the apps. It means using them to find people and keeping the regulars yourself. If you want a senior strategist to look at your order mix and build a plan around it, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much does DoorDash charge restaurants in 2026?",
             "DoorDash’s published Marketplace plans charge 15% of the order subtotal on Basic, 25% on Plus and 30% on Premier for delivery, and 6% on pickup orders across all plans. There are no activation or subscription fees, and payment processing is included in the commission. Its commission-free Online Ordering product charges a processing fee instead. Check your own signed agreement, since that controls what you pay."),
            ("How much does Uber Eats charge restaurants?",
             "As of March 2026, Uber Eats’ published U.S. delivery rates are 20% on Lite, 25% on Plus with Uber One member orders at 30%, and 30% on Premium. Pickup is 7% when you have validated in-store pricing and 10% when you don’t. Lite can be lower in some cities. Its Webshop ordering site charges 2.5% plus $0.29 per order instead of a marketplace commission."),
            ("Does Houston cap delivery app fees for restaurants?",
             "No. Houston has no cap, and a 2021 bill to cap delivery fees in Texas at 15% died in committee. Texas instead passed SB 911, effective January 1, 2022, which requires delivery companies to have a written agreement that states each fee, lets restaurants demand removal within 10 days, and stops cities and counties from adopting rules that change those agreements."),
            ("How do I get the Order button on Google to use my own online ordering?",
             "In your Google Business Profile, open Food ordering, choose your ordering provider or use Add a link at the bottom to add your ordering page, then select Set as preferred and turn on Preferred for pickup and Preferred for delivery. You can also hide third-party providers for pickup, delivery or both. Changes usually appear on Search and Maps within a few hours."),
            ("Should my online ordering prices match my in-store menu?",
             "We usually recommend matching in-store prices on your own ordering page and keeping any markup on the delivery apps. That makes ordering direct visibly cheaper, which is the easiest message to put on bags and receipts. On Uber Eats, pickup orders cost 7% with validated in-store pricing and 10% without it, so parity on pickup menus also lowers your fees."),
        ],
        "figures": {
            "commission": {
                "type": "bars",
                "title": "What a $40 order costs you, by channel",
                "sub": "Fee on a $40 subtotal at published 2026 rates",
                "items": [["App delivery, 30% tier", 12, "$12.00"], ["App delivery, 25% tier", 10, "$10.00"], ["Uber Eats Lite, 20%", 8, "$8.00"], ["DoorDash Basic, 15%", 6, "$6.00"], ["App pickup, 6% to 10%", 4, "$2.40 to $4.00"], ["Direct pickup, processing only", 1.47, "$1.47"]],
                "highlight": [5],
                "note": "Source: DoorDash and Uber Eats merchant pricing pages; direct row uses ChowNow’s 2.95% + $0.29",
                "alt": "Bar chart of delivery app commission versus direct online ordering cost on a $40 restaurant order in Houston",
                "caption": "Moving a regular from app delivery to direct pickup saves roughly $8.50 to $10.50 on this order.",
            },
            "google": {
                "type": "steps",
                "title": "Point Google’s Order button at your own link",
                "sub": "Google Business Profile, Food ordering",
                "steps": [["Open Food ordering", "From your Business Profile, select Food ordering."], ["Add your link", "Pick your provider or choose Add a link at the bottom."], ["Set as preferred", "Turn on Preferred for pickup and for delivery."], ["Decide on apps", "Use Show provider to customers to hide or keep each app."], ["Check Maps", "Changes usually appear within a few hours."]],
                "alt": "Steps to set direct online ordering as preferred in Google Business Profile for a Houston or The Woodlands restaurant",
                "caption": f"Menu path from {SRC['gbp']}.",
            },
            "parity": {
                "type": "compare",
                "title": "Pricing across channels",
                "left": {"title": "Common setup", "items": ["Same marked-up menu everywhere", "Direct costs the guest the same as the app", "20% off codes to push direct", "One menu for app pickup and delivery", "No message about ordering direct"]},
                "right": {"title": "What we’d do", "items": ["In-store prices on direct ordering", "Markup only on app menus", "Loyalty reward instead of discounts", "Unmarked pickup menu where it lowers fees", "“Lower prices when you order from us”"]},
                "alt": "Comparison of restaurant menu pricing setups for delivery apps and direct online ordering in Houston",
                "caption": "Parity on your own channel gives the guest a plain reason to switch.",
            },
            "insert": {
                "type": "checklist",
                "title": "The bag insert that brings orders back",
                "sub": "Small card, one ask",
                "items": ["One QR code to your ordering page", "Unique tracked link per delivery app", "One offer: a free side on the first direct order", "Say why: lower prices when you order direct", "Push pickup; it saves the guest and you", "Pickup address and hours", "Loyalty sign-up in one line", "Check your marketplace agreement first"],
                "alt": "Checklist for a restaurant delivery bag insert promoting direct online ordering in The Woodlands and Houston",
                "caption": "Track each app’s cards separately so you know which bags convert.",
            },
            "mix": {
                "type": "stats",
                "title": "Illustrative channel shift, one location",
                "stats": [["600", "app delivery orders a month"], ["$5,700", "monthly commission at 25%"], ["120", "regulars moved to direct pickup"], ["~$970", "saved per month"]],
                "note": "Illustrative example, $38 average order",
                "alt": "Illustrative stats showing savings when a Houston restaurant shifts delivery app orders to direct online ordering",
                "caption": "Savings before loyalty costs. Run the same math on your own order report.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: hotel group sales
    {
        "slug": "hotel-group-sales-marketing-weddings-meetings-events",
        "title": "Hotel Group Sales Marketing: Filling Weddings, Corporate Meetings and Events",
        "seo_title": "Hotel Group Sales Marketing: Weddings, Meetings, Events",
        "desc": "Hotel and resort group sales marketing in Houston and The Woodlands: Cvent, planner search habits, LinkedIn and Google Ads, venue pages and response time.",
        "category": "Strategy",
        "icons": ["LinkedIn", "Google Ads", "Google Analytics"],
        "art": "b4",
        "hero": "key",
        "hero_alt": "Illustration of a hotel key for group sales marketing to weddings and meetings in Houston and The Woodlands",
        "related": ["hotel-marketing-houston-direct-bookings", "wedding-venue-marketing-houston-montgomery-county", "speed-to-lead-response-time-follow-up-crm"],
        "sections": [
            (None, f"""<p>Monday, 8:12 a.m. The director of sales at a 250-room hotel in The Woodlands opens Cvent and finds 14 RFPs from the weekend. One is a 60-person leadership offsite for an energy company in the Energy Corridor, two nights in April. One is a 150-guest October wedding that came through The Knot. There’s a church conference, a youth volleyball team block and a pharmaceutical dinner that may or may not be real.</p>
<p>She answers two before lunch. The rest wait until Wednesday, after the BEO meeting, a site visit and a revenue call. By Wednesday the energy offsite has a proposal from a resort on Lake Conroe and a hotel in Sugar Land. Nobody calls her back.</p>
<p>Group business rarely gets lost in the ad account. It gets lost between the RFP and the reply. This post is about filling weddings, corporate meetings and social events at hotels and resorts: where planners and couples look, what they want to see before they ask, how fast you need to answer, and how to tell which marketing turns into signed contracts.</p>
<p>If you’re after transient direct bookings, our {L('/blog/hotel-marketing-houston-direct-bookings/', 'hotel direct bookings guide')} covers that side. This one is the sales office.</p>"""),

            ("How meeting planners actually find a venue", f"""<p>A planner sourcing a 60-person offsite isn’t browsing. She has a date range, a budget, a headcount and an approval chain, and she wants three to five credible options fast.</p>
<p>{SRC['cvent26']} surveyed more than 1,650 planners in July 2025. A few findings that should change how you market:</p>
<ul>
<li>Attendee engagement and satisfaction now rank above cost management as the top priority.</li>
<li>Meeting room specifications (50%), photos and video (48%) and floor plans or diagrams (46%) most influence whether a planner sends an RFP at all.</li>
<li>Almost half (48%) are sourcing non-hotel venues like restaurants, galleries and wineries, so your competition includes the event space down the street.</li>
<li>Most want answers within four business days, and 24% call slow replies one of the most frustrating parts of the process.</li>
</ul>
<p>Two more from {SRC['ho']}: CoStar has seen some group booking windows that used to run 30 to 60 days shrink to two or three weeks, and nearly 70% of planners in a 2026 industry study use AI tools like ChatGPT when sourcing destinations. So a planner may never type “meeting space The Woodlands” into Google. She may ask an assistant for “a hotel north of Houston with a 70-person boardroom setup and breakout rooms,” and the answer depends on what your website, Cvent profile and listings actually say. Our {L('/blog/show-up-in-chatgpt-ai-search-aeo/', 'AI search guide')} covers how to be the property that gets named.</p>"""),

            ("Cvent Supplier Network: fix the profile before you buy ads", f"""<p>For corporate and association business, Cvent is the marketplace. Group business sourced through the Cvent Supplier Network hit about $16.5 billion in 2024, a record, with room nights up 16% over 2019, per {SRC['cvent24']}. Cvent’s own page cites 155,000-plus sourcing planners and nearly 340,000 hotels and venues on the network, per {SRC['csnads']}.</p>
<p>That second number is the problem. A planner searching Houston north sees dozens of properties, and the profile is your first sales call. Before spending anything on Cvent advertising, make sure the free profile has:</p>
<ul>
<li>Every meeting room with dimensions, ceiling height and capacity by setup (theater, classroom, banquet rounds, U-shape, reception).</li>
<li>Current floor plans, real photos of each room set for an event, and a short video walkthrough.</li>
<li>Guest room count, the number you’ll commit to a group block, and airport drive times to IAH and Hobby.</li>
<li>F&amp;B minimums or a sample menu range, AV options, and outdoor or unique spaces (a lawn, a rooftop, a lakeside deck).</li>
<li>Recent renovations, with dates.</li>
</ul>
<p>Then look at paid options. Cvent sells Diamond Listings for premium placement and richer content in search results, and competitive ads that show your property to planners looking at a competitor set you choose, plus off-platform retargeting. We’d test competitive ads against the two or three hotels you lose to most often. Judge it on what Cvent itself reports: RFP volume, RFP value, room nights requested and business awarded. Leads alone will flatter it.</p>"""),

            ("Venue pages, floor plans and virtual tours on your own site", f"""<p>Most hotel websites are built for the leisure guest, with a meetings page tacked on: one stock photo of a ballroom and a form. Planners and couples go looking for specifics and leave when they don’t find them.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Page</th><th>Who it’s for</th><th>What it needs</th></tr></thead>
<tbody>
<tr><td>Meetings and events hub</td><td>Corporate and association planners</td><td>Capacity chart for every room, downloadable floor plans and fact sheet, guest room count, AV, parking, airport times, RFP form and a direct phone number</td></tr>
<tr><td>A page per major space</td><td>Planners comparing rooms</td><td>Photos in several setups, dimensions, capacity by setup, 360 tour or walkthrough video</td></tr>
<tr><td>Small meetings page</td><td>Executive assistants booking 10 to 30 people</td><td>Day-meeting packages with a starting price per person, and online booking or instant availability</td></tr>
<tr><td>Weddings</td><td>Couples and parents</td><td>Ceremony and reception spaces, rain plan, starting package price, guest capacity, room block terms, real weddings gallery</td></tr>
<tr><td>Social and SMERF</td><td>Reunions, faith groups, sports teams</td><td>Group rate rules, minimum rooms, meal options, bus parking</td></tr>
</tbody></table></div>
<p>The small meetings page is underused. Per {SRC['ho']}, 86% of planners in Cvent’s 2026 report are more likely to choose a venue for a simple meeting when online booking is available. An executive assistant booking a 16-person board meeting doesn’t want to wait three days for a proposal. Give her a package price and a calendar.</p>
<p>On virtual tours: a 360 tour is nice. A two-minute phone video of the ballroom set for 200 rounds, walking from the pre-function space to the restrooms, is often more useful, and it takes an afternoon. Put both on the space pages and in your Cvent profile. Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} builds these, and the {L('/blog/landing-pages-101/', 'landing pages primer')} covers the form side.</p>"""),

            ("Response time: four days is the floor", f"""<p>Back to Monday morning. The 2025 Cvent report found 80% of planners expect an RFP response within four days, per {SRC['cvent24']}. For meetings of 50 attendees or fewer, 39% will drop a venue that hasn’t replied within two days, per {SRC['ho']}.</p>
<p>Four days is what planners tolerate. The hotel that answers the same day with real dates and a real rate usually sets the frame that everyone else is compared to. A standard we’d hold a sales team to:</p>
<!--fig:response-->
<p>The fix is mostly process. Route RFPs by segment and size so small meetings don’t sit in the same queue as a 400-room citywide. Build proposal templates by room and package so a manager can turn one around in 20 minutes. Give someone backup coverage for days when the DOS is on a site visit. And answer wedding inquiries by phone or text within the hour if you can, because couples often email five venues on the same night.</p>
<p>We cover the follow-up side in {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'our speed-to-lead post')}. The short version: the second and third touches win almost as much business as the first.</p>"""),

            ("Google Ads for group business", f"""<p>Search ads work for group business when the keywords say “event,” not “room.” A campaign that mixes “hotels in The Woodlands” with “conference venue The Woodlands” will spend its budget on transient travelers and send them to an RFP form.</p>
<p>Build separate campaigns:</p>
<ul>
<li><b>Meetings:</b> meeting space The Woodlands, conference venue north Houston, corporate retreat near Houston, offsite venue Houston, hotel with meeting rooms Spring TX, board meeting room rental.</li>
<li><b>Weddings:</b> wedding venue The Woodlands, hotel wedding venue Houston, wedding reception venue with hotel rooms, Lake Conroe wedding venue.</li>
<li><b>Social:</b> holiday party venue The Woodlands, rehearsal dinner venue, quinceañera venue Houston, reunion hotel Houston.</li>
</ul>
<p>Negatives for the meetings campaign: jobs, careers, hiring, salary, apartments, tonight, cheap, “near me now,” free, virtual, Zoom, and your competitors’ room-booking terms. For weddings, add “courthouse,” “elopement” (unless you sell it), “DIY” and “backyard.”</p>
<p>Sample responsive search ad copy for meetings: “Meeting Space in The Woodlands” / “Breakouts for 10 to 300” / “Reply With a Proposal in 24 Hours.” Description: “Board rooms to ballroom, 250 guest rooms on site, 35 min to IAH. Send your dates and get a proposal fast.” Land it on the meetings hub, not the homepage.</p>
<p>An illustrative test budget is $1,500 to $4,000 a month across meetings and weddings for a single full-service property, more around peak wedding planning in January and February. It’s an example, not a benchmark. Track RFP form fills, wedding inquiries and calls as separate conversions, then import signed contracts as offline conversions so Google learns which clicks became business. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} covers setup, and {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} will help you size the test.</p>"""),

            ("LinkedIn for corporate meetings", f"""<p>LinkedIn is expensive per click and still the best way to reach the people who book corporate meetings before they open an RFP. {SRC['li']} include job title, company, industry and seniority, plus matched audiences from your website visitors, contact lists and target account lists.</p>
<p>How we’d set it up for a hotel north of Houston:</p>
<ul>
<li><b>Audience one, titles.</b> Executive assistants, event and meeting planners, HR and training managers, sales operations and sales enablement leaders, in Houston-area companies with 200 or more employees.</li>
<li><b>Audience two, accounts.</b> A list of 100 to 300 companies within an hour’s drive that hold offsites, sales meetings and training: energy, engineering, healthcare systems, chemical and industrial firms, and law and accounting offices.</li>
<li><b>Audience three, retargeting.</b> Visitors to your meetings pages.</li>
</ul>
<p>Creative that works: a short video walkthrough of the boardroom, a “Q3 offsite package from $X per person” offer, and a lead gen form with three questions (dates, headcount, overnight or day only). We’d budget LinkedIn as the slow, steady pipeline builder and judge it over a full quarter. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston energy and industrial')} has more on reaching that audience.</p>"""),

            ("Weddings: marketplaces, Instagram and the room block", f"""<p>Weddings bring a different buyer and a different clock. {SRC['knot']} put the 2025 average wedding cost at $34,000 with 117 guests, or $292 per guest, and found couples hire an average of 13 vendors. Thirty-seven percent reached out to more vendors than they planned to, looking for budget-friendly options. So your inquiry is one of many sent the same evening.</p>
<p>The Knot and WeddingWire are still where many Houston couples shortlist venues, and Zola lists venues too. A listing works when it has real photos from weddings at your property, starting package prices, a capacity range and fast replies. Our {L('/blog/wedding-venue-marketing-houston-montgomery-county/', 'wedding venue marketing guide')} goes deep on marketplaces, Instagram and tours.</p>
<p>A hotel has one advantage a barn venue doesn’t: guest rooms. Sell it. A 150-guest wedding often brings a block of 30 to 50 room nights across Friday and Saturday, plus a rehearsal dinner and a farewell brunch. Put that on the wedding page in plain terms: room block on site, no shuttles, a suite for getting ready, late checkout for the couple. Then make the block terms simple, whether courtesy or contracted, and explain attrition in one sentence before anyone signs.</p>"""),

            ("Need periods and the Houston group calendar", f"""<p>Group marketing should follow your need periods, not the calendar the brand sends you. Houston’s is unusual.</p>
<p>The city hosts big compression events. The Offshore Technology Conference drew nearly 25,000 people to NRG Park May 4 to 7, 2026, per {SRC['otc']}. RODEOHOUSTON ran March 2 to 22 in 2026, per {SRC['rodeo']}. Houston ranked No. 5 on U.S. News’ first Best Conference Cities list, and Houston First’s sales team booked 517 future meetings and conventions worth 881,737 hotel room nights in 2025, a record, per {SRC['hfirst']}. The George R. Brown expansion adds 700,000 square feet, including a 60,000-square-foot ballroom, with a target opening of May 2028, per {SRC['axios']}.</p>
<!--fig:houston-->
<p>For a hotel in The Woodlands, Spring or Katy, compression downtown means overflow and higher rates on those dates. Don’t spend group marketing dollars chasing business into weeks you’d sell out anyway. Spend them on the gaps:</p>
<!--fig:calendar-->
<ul>
<li><b>July and August.</b> The heat keeps leisure and weddings down. Market indoor corporate training, summer sales meetings and youth sports blocks.</li>
<li><b>Thanksgiving to New Year’s.</b> Holiday parties fill evenings in early December, then the last two weeks go quiet. Sell holiday parties in August and September.</li>
<li><b>Sunday to Tuesday nights.</b> Pitch day meetings and short corporate stays to companies within 30 minutes.</li>
<li><b>Hurricane season, June 1 to November 30.</b> Have flexible terms ready. Planners remember who was reasonable after the last storm.</li>
</ul>
<p>In The Woodlands, you’re also competing with the Waterway Marriott and its 65,000 square feet of meeting space, per {SRC['ci_marriott']}, plus resorts and conference centers around Lake Conroe. A smaller hotel wins on the 20-to-80-person meeting with a quick answer and a fair package.</p>"""),

            ("The group sales funnel and the numbers to watch", f"""<p>Most sales offices track leads and revenue and nothing in between. You need the middle to know which marketing works.</p>
<!--fig:funnel-->
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Formula</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td>Response time</td><td>Median hours from RFP received to proposal sent</td><td>The number planners feel first</td></tr>
<tr><td>Lead-to-proposal rate</td><td>Proposals sent ÷ qualified leads</td><td>If good business is being declined or ignored</td></tr>
<tr><td>Proposal-to-contract rate</td><td>Contracts signed ÷ proposals sent</td><td>Price, package and follow-up quality</td></tr>
<tr><td>Lead-to-contract rate</td><td>Contracts signed ÷ qualified leads, by source</td><td>Which channel actually sells</td></tr>
<tr><td>Group pace</td><td>Group revenue on the books for a future month vs. same point last year</td><td>Whether you need more demand for that month</td></tr>
<tr><td>Pickup (actualization)</td><td>Room nights used ÷ room nights contracted</td><td>Block sizing and attrition risk</td></tr>
</tbody></table></div>
<p>Tag every lead with its source (Cvent, The Knot, Google Ads, LinkedIn, website organic, referral, walk-in) in your sales system, and keep that tag through to the signed contract. Then cost per contract by source becomes a number you can act on.</p>
<p>We built the same discipline on the transient side for {L('/case-studies/viceroy-los-cabos/', 'Viceroy Los Cabos')}, where booking-engine tracking let us measure true room-night return: 11.4x return on ad spend and a 212% increase in direct bookings. Group is harder to track because contracts close weeks later and offline, which is exactly why the source tag matters.</p>
<p>If you want help building the group plan for your property, a senior strategist can map your need periods and channels with you. <a href="/contact/">Get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do hotels get more group business?",
             "Start with your listings and website: a complete Cvent profile with room specs, floor plans, photos and video, and venue pages on your own site with capacity charts and package prices. Then answer RFPs fast, ideally the same business day. Add Google Ads on event keywords, LinkedIn for corporate planners and wedding marketplaces for couples, and track every lead to a signed contract by source."),
            ("How fast should a hotel respond to an RFP?",
             "Cvent’s planner research found 80% of planners expect a reply within four days, and for meetings of 50 or fewer attendees, 39% will drop a venue that hasn’t responded within two days. We recommend acknowledging within an hour during business hours and sending a real proposal within 24 hours. The first credible proposal often sets the terms the others get compared to."),
            ("Is Cvent advertising worth it for a hotel?",
             "It can be, once your free Cvent Supplier Network profile is complete. Planners decide whether to send an RFP based largely on room specs, photos and video, and floor plans, so fix those first. Then test competitive ads against the two or three properties you lose to most and judge results on RFP value and awarded business, not lead count."),
            ("Should hotels use LinkedIn ads for meetings and events?",
             "LinkedIn is useful for corporate meetings because you can target by job title, company, industry and seniority, and upload lists of target companies. Reach executive assistants, meeting planners, HR and sales operations leaders at companies within driving distance. Clicks are expensive, so judge LinkedIn over a full quarter on proposals and contracts rather than on cost per click."),
            ("When should a Houston-area hotel market group business?",
             "Market into your need periods, not your busy weeks. In Greater Houston that often means July and August, the last two weeks of December, and Sunday through Tuesday nights. Compression events like OTC in May and the rodeo in March fill rooms on their own. Sell holiday parties in late summer, and plan wedding pushes for January and February when couples start booking."),
        ],
        "figures": {
            "response": {
                "type": "steps",
                "title": "An RFP response standard that wins",
                "sub": "What we’d hold a hotel sales team to",
                "steps": [["Within 1 hour", "Acknowledge by email or phone, confirm dates and headcount."], ["Same day", "Check availability and displacement with revenue."], ["Within 24 hours", "Send a real proposal with rates, space and F&B."], ["Day 2 to 3", "Call to walk through it and offer a site visit or video tour."], ["Day 5 to 7", "Follow up with one change: a date option or package tweak."]],
                "alt": "Steps for a fast hotel RFP response process for group sales in Houston and The Woodlands",
                "caption": "Planners tolerate four days. Same-day proposals tend to set the frame.",
            },
            "calendar": {
                "type": "columns",
                "title": "Where group marketing dollars belong",
                "sub": "Example need index for a hotel north of Houston (higher = more need)",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [55, 40, 20, 35, 25, 60, 85, 80, 45, 30, 50, 70],
                "highlight": [6, 7, 11],
                "y_label": "Need",
                "note": "Illustrative example",
                "alt": "Illustrative monthly need periods for hotel group sales marketing in The Woodlands and north Houston",
                "caption": "Build your own from last year’s on-the-books data. Spend where the bars are tall.",
            },
            "funnel": {
                "type": "funnel",
                "title": "A month of group leads, illustrated",
                "stages": [["Inquiries and RFPs", "120"], ["Qualified (dates, size, budget fit)", "70"], ["Proposals sent", "55"], ["Site visits or video tours", "22"], ["Contracts signed", "12"]],
                "note": "Illustrative example",
                "alt": "Illustrative hotel group sales funnel from RFP to signed contract for a Houston-area property",
                "caption": "Track each stage by lead source so you can see which channel sells.",
            },
            "houston": {
                "type": "stats",
                "title": "Houston’s group business backdrop",
                "stats": [["881,737", "room nights booked by Houston First in 2025"], ["~25,000", "OTC 2026 attendees"], ["No. 5", "U.S. News Best Conference Cities"], ["May 2028", "GRB expansion target"]],
                "note": "Source: Houston First, OTC, Axios Houston",
                "alt": "Stats on Houston convention and meeting demand that shape hotel group sales marketing in The Woodlands",
                "caption": f"From {SRC['hfirst']}, {SRC['otc']} and {SRC['axios']}.",
            },
        },
    },
]
