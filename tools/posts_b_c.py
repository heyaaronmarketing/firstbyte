"""Two local industry posts: restaurant marketing (The Woodlands / Houston) and wedding venue marketing
(Montgomery County / Greater Houston).

Research (October 2026): DoorDash and Uber Eats published merchant pricing pages, Google Business Profile
help (menu editor, booking links), Google Ads location targeting help, BrightLocal Local Consumer Review
Survey 2026, Toast restaurant statistics, The Knot Real Weddings Study 2026 (2025 weddings) and the 2025
study as reported by FOX, Curate's estimates of The Knot listing costs, and Census QuickFacts for
Montgomery County. Search phrasing taken from "restaurant marketing houston", "how to get more customers to
my restaurant", "wedding venue marketing" and "how to get more wedding venue bookings" results.
"""

SRC = {
    "doordash": '<a href="https://merchants.doordash.com/en-us/products/pricing" target="_blank" rel="noopener">DoorDash’s merchant pricing page</a>',
    "ubereats": '<a href="https://merchants.ubereats.com/us/en/pricing/" target="_blank" rel="noopener">Uber Eats’ merchant pricing page</a>',
    "menu": '<a href="https://support.google.com/business/answer/9455840?hl=en" target="_blank" rel="noopener">Google’s menu editor help page</a>',
    "booking": '<a href="https://support.google.com/business/answer/7475773?hl=en" target="_blank" rel="noopener">Google’s booking setup help page</a>',
    "geo": '<a href="https://support.google.com/google-ads/answer/2453995?hl=en" target="_blank" rel="noopener">Google Ads location targeting</a>',
    "brightlocal": '<a href="https://www.brightlocal.com/research/local-consumer-review-survey/" target="_blank" rel="noopener">BrightLocal’s 2026 Local Consumer Review Survey</a>',
    "toast": '<a href="https://pos.toasttab.com/blog/on-the-line/restaurant-industry-statistics" target="_blank" rel="noopener">Toast’s restaurant industry research</a>',
    "knot26": '<a href="https://www.theknot.com/content/wedding-data-insights/real-weddings-study" target="_blank" rel="noopener">The Knot Real Weddings Study</a>',
    "knotcost": '<a href="https://www.theknot.com/content/average-wedding-cost" target="_blank" rel="noopener">The Knot’s cost breakdown from its 2026 Real Weddings Study</a>',
    "curate": '<a href="https://curate.co/blog/the-knot-advertising-cost/" target="_blank" rel="noopener">estimates compiled by Curate</a>',
    "census": '<a href="https://www.census.gov/quickfacts/fact/table/montgomerycountytexas/PST045224" target="_blank" rel="noopener">Census Bureau QuickFacts</a>',
}

POSTS = [
    # ------------------------------------------------------------------------------------------
    {
        "slug": "restaurant-marketing-the-woodlands-houston",
        "title": "Restaurant Marketing in The Woodlands & Houston: Fill More Tables in 2026",
        "seo_title": "How to Get More Restaurant Customers in The Woodlands",
        "desc": "Restaurant marketing for The Woodlands and Houston: rank in Google Maps, cut delivery-app fees, use short video and email, and fill slow weeknights.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Instagram", "TikTok"],
        "art": "b3",
        "hero": "restaurant",
        "hero_alt": "Illustration of a restaurant table and storefront for a guide to restaurant marketing in The Woodlands and Houston",
        "related": ["grand-opening-marketing-plan-30-days", "rank-in-google-map-pack-houston", "complete-guide-google-reviews"],
        "sections": [
            (None, """<p>Friday is full. Saturday is full. Tuesday, you're looking at a half-empty dining room and a line cook scrolling his phone. And every week a little more of your revenue goes out the door to a delivery app.</p>
<p>When an owner in The Woodlands asks us "how do I get more customers to my restaurant?", awareness is rarely the real gap. People already know you're there. What you need is for more of them to pick you on a Tuesday, order from you directly instead of through an app, and come back without a coupon every time. Below is how we'd go at it if we were running your marketing, with published numbers where they exist and clearly labeled examples where they don't.</p>"""),
            ("How diners in The Woodlands actually pick a restaurant", f"""<p>Think about the last time you searched "restaurants in The Woodlands" or "brunch near me." You probably looked at three places on a map, opened two of them, scrolled the photos, glanced at the stars, and checked whether they took reservations. That took under a minute.</p>
<p>That minute is your real storefront, and the survey numbers line up with it. {SRC['brightlocal']} found that 97% of consumers read reviews for local businesses, 74% look for reviews written in the last three months, and 31% will only use a business rated 4.5 stars or higher, up from 17% the year before. And {SRC['toast']} reports that 50% of diners say social media played a role in discovering a restaurant.</p>
<!--fig:diners-->
<p>So you're fighting on two screens: the Google map results and a feed of short videos. Both reward the same habit, which is showing fresh, real, appetizing proof that people enjoy eating at your place, week after week.</p>"""),
            ("How to rank higher in Google Maps for “restaurants near me”", f"""<p>Google ranks map results on three things: how relevant your profile is to the search, how close you are to the person searching, and how prominent you are (reviews, links, mentions). You can't move your building, so put your effort into the other two.</p>
<h3>Set up your Google Business Profile like it's your front door</h3>
<ol>
<li><b>Pick the most specific primary category.</b> "Mexican restaurant" or "Sushi restaurant" beats plain "Restaurant." Add secondary categories only if they're true (Bar, Brunch restaurant, Caterer).</li>
<li><b>Load the menu with the menu editor.</b> Google's menu editor is built for food and drink businesses and lets you add items, descriptions and prices grouped into sections, per {SRC['menu']}. Changes can take 24 to 48 hours to show. A typed menu beats a blurry photo of a paper one, because the text can match searches like "birria tacos" or "gluten free pizza."</li>
<li><b>Add your reservation and order links.</b> If you use a reservation platform, connect it, or add your own link, as described on {SRC['booking']}. Point the order link at your own online ordering, not a delivery app.</li>
<li><b>Upload photos every week.</b> Dishes, the dining room, the patio, the bar, staff. Real photos from your phone are fine. Ten new photos a month keeps the profile looking alive.</li>
<li><b>Fill in attributes and holiday hours.</b> Outdoor seating, kid-friendly, happy hour, vegetarian options. Set special hours for Thanksgiving, Christmas Eve and Fourth of July before the day, not after the one-star review.</li>
<li><b>Post weekly.</b> A new special, an event, a seasonal dish. Posts won't rank you on their own, but they give searchers a reason to choose you.</li>
</ol>
<!--fig:profile-->
<p>Our <a href="/blog/rank-in-google-map-pack-houston/">guide to ranking in the Houston map pack</a> goes deeper on categories and proximity if you want the full playbook.</p>"""),
            ("Market Street, Waterway Square and Hughes Landing: competing in a crowded dining district", """<p>The Woodlands has an odd problem for restaurants. If yours sits on Market Street, along The Woodlands Waterway or at Hughes Landing, you're within a short walk of a dozen other good places to eat. Proximity stops being an advantage when everyone is close. A diner standing outside Waterway Square sees the same map you do.</p>
<p>In a cluster like that, the tie-breakers are your photos, your review count and recency, and how clearly your profile says what you're best at. "Great food and drinks" describes everyone. "Wood-fired pizza and a dog-friendly patio on the lake" is a reason to walk past three other doors.</p>
<p>A few things we see work in these districts:</p>
<ul>
<li><b>Own an occasion.</b> Pre-show dinner before a concert at the Cynthia Woods Mitchell Pavilion. Post-shopping lunch near The Woodlands Mall. Business lunch for the office towers. Pick one and say it in your profile description, posts and ads.</li>
<li><b>Show the walk.</b> Visitors and hotel guests along the Waterway don't know the area. A photo of your entrance and a line like "two minutes from the Waterway Square fountain" helps.</li>
<li><b>Mind the parking question.</b> If you have a garage nearby or validate parking, say so. It answers an objection before anyone asks.</li>
</ul>
<p>If you're out on FM 1488 in Magnolia, along Rayford Road in Spring, or off I-45 in Conroe, you have the opposite situation: fewer neighbors, longer drives. There, the work is making sure you show up for the broader "restaurants near me" searches across a wider radius, and giving people a reason to drive 15 minutes.</p>"""),
            ("Delivery apps vs. direct online ordering: do the math", f"""<p>Delivery apps are a customer acquisition channel. They're also expensive, and many owners have never sat down and priced it out per order. Here are the published rates as of this writing:</p>
<div class="bp-tbl"><table><thead><tr><th>Platform and plan</th><th>Delivery commission</th><th>Pickup commission</th></tr></thead><tbody>
<tr><td>DoorDash Basic</td><td>15%</td><td>6%</td></tr>
<tr><td>DoorDash Plus</td><td>25%</td><td>6%</td></tr>
<tr><td>DoorDash Premier</td><td>30%</td><td>6%</td></tr>
<tr><td>Uber Eats Lite</td><td>20% (15% in some cities)</td><td>7%</td></tr>
<tr><td>Uber Eats Plus</td><td>25%</td><td>7%</td></tr>
<tr><td>Uber Eats Premium</td><td>30%</td><td>7%</td></tr>
</tbody></table></div>
<p>Rates from {SRC['doordash']} and {SRC['ubereats']}. Uber Eats says its 7% pickup rate requires in-app prices to match in-store prices; otherwise it's 10%. DoorDash notes that orders through its own online ordering storefront are commission-free but carry a payment processing fee.</p>
<!--fig:fees-->
<p>On a $40 order, the difference between a 30% plan and your own website is about $10 or more, every single time. If you do 150 delivery orders a week, that's a real number.</p>
<p>We wouldn't tell most restaurants to quit the apps. They bring in people who have never heard of you. The play is to use the apps to get discovered, then move repeat customers to direct ordering:</p>
<ul>
<li>Put a card in every delivery bag: "Order direct next time at [your site] and get a free dessert." Keep it simple.</li>
<li>Make the order button on your Google profile and Instagram bio go to your own ordering page.</li>
<li>Run a slightly better deal on direct orders, since you can afford it.</li>
<li>Collect the email address at checkout so the customer becomes yours.</li>
</ul>"""),
            ("Restaurant social media marketing that fills seats", f"""<p>Short video on Instagram Reels and TikTok is where most people under 45 find a new place to eat. You don't need a production crew. You need a phone, decent light and a steady habit.</p>
<h3>A shot list that works for almost any restaurant</h3>
<ul>
<li>The "money shot": the cheese pull, the pour, the sizzle, the torch on the crème brûlée. Five to eight seconds.</li>
<li>A cook or bartender making one signature item start to finish, sped up.</li>
<li>The owner or chef saying one sentence about why a dish exists.</li>
<li>What $25 gets you at lunch. People love a price.</li>
<li>The room on a busy night. Social proof is visual.</li>
<li>A walk from the parking lot to the table, so first-timers know where they're going.</li>
</ul>
<p>Three to four short videos a week is a realistic pace for a small team. Post the same clip to Reels, TikTok and YouTube Shorts. Put the city in the caption ("best tacos in The Woodlands" is a phrase people type into TikTok search), and tag your location.</p>
<h3>Local creators</h3>
<p>Houston has a deep bench of food creators, from accounts with a few thousand followers in Spring and Katy to large metro-wide pages. In our experience the smaller local ones are usually the better deal: their followers actually live nearby, and many will come in for a comped meal and a modest fee. Invite five creators to a tasting night instead of paying one big account. And make sure every paid or comped post is disclosed, because the FTC treats a free meal as a material connection. Our <a href="/blog/ftc-rules-influencer-partnerships/">guide to FTC rules for influencer partnerships</a> covers what to require in writing, and <a href="/blog/micro-influencers-vs-big-names/">micro-influencers vs. big names</a> covers how to choose.</p>"""),
            ("Build an email and SMS list you own", """<p>Followers belong to Instagram. Delivery customers belong to the app. An email list belongs to you, and it's the cheapest way to fill a Tuesday.</p>
<h3>Ways to collect contacts without being annoying</h3>
<ul>
<li>Online ordering checkout (the easiest source, and the highest quality).</li>
<li>A birthday club: "Tell us your birthday and get a free entrée that week." People happily give up an email for that.</li>
<li>Guest Wi-Fi login that asks for an email.</li>
<li>Reservation platforms, if your settings allow marketing opt-in.</li>
<li>A QR code on the check presenter for a monthly giveaway.</li>
</ul>
<p>Send one email a week at most. Make it about something: a new seasonal dish, a wine dinner, a Monday deal, the Thanksgiving pie pre-order deadline. Text messages get read faster, so save SMS for time-sensitive offers, and only text people who gave clear permission to receive marketing texts. If you're starting from zero, our <a href="/blog/email-marketing-basics/">email marketing basics</a> post walks through the setup.</p>"""),
            ("Events and slow-night offers that work in Houston", """<p>Every restaurant has its slow nights. For most places around here it's Monday through Wednesday, plus the weeks after the holidays, plus the stretch of July and August when it's too hot to sit outside and families are traveling.</p>
<!--fig:week-->
<p>Discounting your busiest night teaches people to wait for a deal. Aim your offers at the empty nights instead, and give people a reason that isn't just "cheaper":</p>
<ul>
<li><b>Recurring theme nights:</b> trivia Tuesday, a half-price bottle Wednesday, a kids-eat-free Monday. Consistency matters more than cleverness. It takes six to eight weeks for a weekly event to catch on.</li>
<li><b>Industry night:</b> a discount for restaurant and hospitality workers on their night off.</li>
<li><b>Prix fixe or chef's table:</b> a set menu on a slow night that feels like an event.</li>
<li><b>Ride the local calendar:</b> Pavilion concert nights, high school football Fridays, holiday lighting events, the RodeoHouston run in March, watch parties for the Texans and Astros.</li>
<li><b>Summer indoor push:</b> when the patio is unbearable, promote the air-conditioned bar, a happy hour that runs later, or a lunch combo for the office crowd.</li>
</ul>
<p>Then tell people. Email the list, post the event to your Google profile, make a short video, and run a small radius ad for the week of the event.</p>"""),
            ("Review management for restaurants", f"""<p>In a crowded map result, reviews break most ties, and the survey numbers near the top of this post say the recent ones count most. A 4.6 with forty reviews from this summer will often win the click over a 4.7 whose newest review mentions a menu you retired in 2023.</p>
<p>Restaurants get plenty of reviews without asking, but the unprompted ones skew toward people who were annoyed. To balance that out:</p>
<ul>
<li>Have servers mention it at the close of a great meal, with a QR code on the check presenter that opens your Google review form.</li>
<li>Add a review link to the online ordering confirmation email.</li>
<li>Reply to every review within a couple of days. Thank the happy ones by name and mention the dish. For the angry ones, apologize once, take it offline, and don't argue in public.</li>
<li>Never pay for reviews or offer a discount in exchange for a 5-star rating. The FTC's rule on fake reviews applies to restaurants too; see <a href="/blog/fake-reviews-rule-local-businesses/">what the fake reviews rule means for local businesses</a>.</li>
</ul>
<p>Our <a href="/blog/complete-guide-google-reviews/">complete guide to Google reviews</a> has scripts for replies and asking.</p>"""),
            ("Simple ads for restaurants: a radius around your door", f"""<p>Restaurant advertising gets overbuilt. Most independent restaurants we talk to need two campaigns set up carefully, not ten set up in a hurry.</p>
<h3>Google Search and Maps ads</h3>
<p>Target searches like "restaurants near me," "[cuisine] near me," "[cuisine] the woodlands" and "happy hour [your area]." Set a tight radius, usually 3 to 8 miles depending on how far people drive to you. In the {SRC['geo']} settings, choose to reach people in or regularly in your area ("presence") rather than people merely interested in it, or you'll pay for clicks from someone in Dallas reading about Houston. Add your location so the ad can show in Google Maps with directions. See our <a href="/services/search-marketing/">search marketing</a> page for how we manage this.</p>
<h3>Meta (Instagram and Facebook) radius ads</h3>
<p>Take your best-performing short video and run it to people within 5 to 10 miles. Use it to promote a specific thing (the new brunch, Thursday trivia, the holiday catering menu), not "come eat with us." This is where <a href="/services/paid-social-advertising/">paid social</a> earns its keep for restaurants.</p>
<div class="bp-tbl"><table><thead><tr><th>Campaign</th><th>Typical starting budget</th><th>What to measure</th></tr></thead><tbody>
<tr><td>Google Search and Maps, 3-8 mile radius</td><td>$15-$40 a day</td><td>Calls, direction requests, reservation and order clicks</td></tr>
<tr><td>Meta video ads, 5-10 mile radius</td><td>$10-$30 a day</td><td>Event RSVPs, offer redemptions, direct online orders</td></tr>
<tr><td>Event or holiday push (1-2 weeks)</td><td>$150-$500 total</td><td>Covers on that night vs. a normal week</td></tr>
</tbody></table></div>
<p>These are typical ranges we'd start a single-location restaurant with, not a rule. A busy Houston location near the Galleria will need more than a neighborhood café in Shenandoah. The point is to start small, measure what you can tie to covers and orders, and add money to what works.</p>"""),
            ("Where to start this week", """<p>If you only do a few things before the weekend, do these:</p>
<ol>
<li>Change your Google order button to your own online ordering page and type your menu into the menu editor.</li>
<li>Upload ten fresh photos and set holiday hours through New Year's.</li>
<li>Pick your slowest night and give it a weekly reason to come in.</li>
<li>Print a "order direct next time" card for every delivery bag.</li>
<li>Film three short videos with the dish people photograph most.</li>
</ol>
<p>We work with restaurants and hospitality brands across the area (see our <a href="/industries/restaurants/">restaurant marketing</a> page and the new-location launches in our <a href="/case-studies/the-toasted-yolk-cafe/">Toasted Yolk Cafe case study</a>). If you're already boosting posts or running Google ads and can't tell whether they moved covers, our free <a href="/contact/">Ad Spend Leak Check</a> is a quick way to find out. We record about 10 minutes of video going through your actual Google or Meta account, pointing at the spend that isn't earning its keep, and it lands in your inbox within 48 hours.</p>"""),
        ],
        "faq": [
            ("How do I get more customers to my restaurant?",
             "Start with your Google Business Profile: the most specific category, a typed menu, weekly photos, and reservation and order links. Then build reviews steadily, post short videos three or four times a week, collect emails at checkout, and give your slowest night a recurring event. Small radius ads on Google and Instagram help once those basics are in place."),
            ("How do restaurants rank higher on Google Maps?",
             "Google weighs relevance, distance and prominence. You can control relevance with a specific primary category, accurate menu items, attributes and a clear description, and prominence with a steady flow of recent reviews, fresh photos and local links. Distance you can't change, so in dense areas like Market Street, reviews and photos are usually the tie-breaker."),
            ("How much do DoorDash and Uber Eats charge restaurants?",
             "As of late 2026, DoorDash's published delivery commissions are 15%, 25% or 30% depending on plan, with 6% for pickup. Uber Eats lists 20% for its Lite plan (15% in some cities), 25% for Plus and 30% for Premium, with 7% for pickup when in-app prices match in-store prices. Your own online ordering usually only costs card processing."),
            ("Is social media marketing worth it for a small restaurant?",
             "Yes, if you treat it as short video and not as a posting chore. Toast reports that half of diners say social media played a role in discovering a restaurant. Three or four short clips a week of your best dishes, your staff and the room on a busy night will do more than daily photos with long captions."),
            ("How much should a restaurant spend on marketing?",
             "There is no single right number, but a single-location restaurant can test Google and Meta ads for roughly $25 to $70 a day combined before deciding what to scale. Free work comes first: your Google profile, reviews, email list and short videos. Spend on ads only where you can tie results to calls, reservations, orders or covers."),
        ],
        "figures": {
            "diners": {
                "type": "stats",
                "title": "How diners decide before they arrive",
                "stats": [["97%", "read reviews for local businesses"], ["74%", "look for reviews from the last 3 months"], ["31%", "only use businesses rated 4.5+ stars"], ["50%", "of diners say social media helped them find a restaurant"]],
                "note": "Source: BrightLocal 2026 Local Consumer Review Survey; Toast",
                "alt": "Stat tiles showing how diners use reviews and social media to choose restaurants in The Woodlands and Houston",
                "caption": "Reviews and social video do most of the selling before a guest walks in.",
            },
            "profile": {
                "type": "checklist",
                "title": "Restaurant Google Business Profile checklist",
                "sub": "What a map result needs to win the click",
                "items": ["Most specific primary category", "Full menu typed into the menu editor", "Reservation link connected", "Order button pointed at your own site", "10+ new photos a month", "Attributes: patio, happy hour, kid-friendly", "Holiday hours set in advance", "Weekly post with a special or event", "Reply to every review"],
                "alt": "Checklist of Google Business Profile settings that help restaurants rank in Google Maps in The Woodlands",
                "caption": "Every item here is free and takes less than an hour to set up.",
            },
            "fees": {
                "type": "bars",
                "title": "What a $40 delivery order costs you",
                "sub": "Platform commission on one order, by plan",
                "items": [["DoorDash Basic (15%)", 6, "$6.00"], ["Uber Eats Lite (20%)", 8, "$8.00"], ["DoorDash or Uber Plus (25%)", 10, "$10.00"], ["DoorDash Premier or Uber Premium (30%)", 12, "$12.00"], ["Your own online ordering (about 3% processing)", 1.2, "about $1.20"]],
                "highlight": [4],
                "note": "Source: DoorDash and Uber Eats published rates; 3% processing is an assumption",
                "alt": "Bar chart comparing delivery app commissions with direct online ordering costs for Houston restaurants on a $40 order",
                "caption": "Commission rates come from each platform's merchant pricing page; card processing varies by provider.",
            },
            "week": {
                "type": "columns",
                "title": "Where the empty seats usually are",
                "sub": "Example dinner covers by night, single-location restaurant",
                "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                "values": [38, 42, 50, 68, 96, 100, 72],
                "highlight": [0, 1, 2],
                "y_label": "Covers vs. peak night",
                "note": "Illustrative example",
                "alt": "Column chart of example restaurant covers by night showing slow Monday to Wednesday dinners in The Woodlands",
                "caption": "Aim offers and events at the slow nights, not the ones that are already full.",
            },
        },
    },
    # ------------------------------------------------------------------------------------------
    {
        "slug": "wedding-venue-marketing-houston-montgomery-county",
        "title": "Wedding Venue Marketing in Houston & Montgomery County: Book More Tours",
        "seo_title": "Wedding Venue Marketing in Houston & Montgomery County",
        "desc": "Wedding venue marketing for Conroe, Magnolia, Tomball, The Woodlands and Houston: SEO, Google Ads, Instagram, faster replies and more booked tours.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Instagram"],
        "art": "b5",
        "hero": "wedding",
        "hero_alt": "Illustration of a wedding venue with an arch and string lights for a guide to wedding venue marketing in Houston and Montgomery County",
        "related": ["reaching-customers-conroe-montgomery", "landing-pages-101", "google-ads-cost-per-click-houston-benchmarks"],
        "sections": [
            (None, """<p>Your calendar for next October filled up fast. Next June has gaps. Most of your Fridays and Sundays are empty, the inquiries that come in want a price you won't give over email, and half the couples who book a tour never show.</p>
<p>Most venue owners who ask us "how do I get more wedding venue bookings?" have already tried posting more on Instagram. It rarely moves the calendar. What does is planning around how long the booking cycle really is, being where couples look in January, and answering faster than anyone else in the first hour after an inquiry. Below is how we'd market a venue in Conroe, Magnolia, Montgomery, Tomball, The Woodlands or anywhere else around Houston.</p>"""),
            ("Wedding venue marketing runs on a long clock", f"""<p>A restaurant can run an ad tonight and see covers tomorrow. A venue is marketing to couples who'll walk down the aisle a year or more from now.</p>
<p>The wedding-planning data from {SRC['knot26']} explains why:</p>
<ul>
<li>Couples are typically engaged for well over a year. The Knot has put the average at around <b>15 months</b> in recent editions.</li>
<li><b>December</b> is the most popular month to get engaged.</li>
<li>The venue is usually one of the first things couples book, because the date depends on it.</li>
<li>Most weddings land between May and October, and fall is the most popular season.</li>
</ul>
<p>Put that together and you get a predictable rhythm. Engagements spike over the holidays, so inquiries surge from late December through March. Those couples are shopping for dates 12 to 18 months out. Your marketing needs to be at full strength in January, not in May when you notice the gaps.</p>
<!--fig:season-->
<p>Texas adds its own twist. Our peak seasons are spring (March through early May) and fall (October and November). July and August heat makes outdoor ceremonies a hard sell, and June 1 through November 30 is hurricane season, which some couples weigh for September dates. If you have a climate-controlled hall, that's a summer selling point worth putting front and center.</p>"""),
            ("What couples are spending (and what that means for you)", f"""<p>Know your buyer's budget before you set your ad budget. According to {SRC['knotcost']}, couples who married in 2025 spent an average of <b>$34,200</b>. The average guest count was <b>117</b>, about <b>$292 per guest</b>, and the average reception venue cost <b>$12,900</b>.</p>
<!--fig:spend-->
<p>That's a big-ticket, considered purchase, often paid for by more than one family. A few things follow from it:</p>
<ul>
<li>A single booking can be worth $8,000 to $20,000 or more to a Montgomery County venue, so paying $150 to $400 to get one qualified tour is often a fine trade if your tour-to-booking rate is healthy.</li>
<li>An average hides a wide spread. Plenty of couples around Houston are working with half that budget or less, whatever the glossy photos suggest. Fridays, Sundays and off-season dates are how you serve them without discounting Saturdays in October.</li>
<li>Parents are often in the decision. Your website and tour need to answer their questions too: parking, accessibility, what's included, the rain plan.</li>
</ul>"""),
            ("The Knot and WeddingWire vs. channels you own", f"""<p>A lot of couples start their venue search on The Knot or WeddingWire, so for most venues the directories aren't optional. They are rented ground, though. You're listed next to every competitor, couples can compare you side by side, and leads often go to several venues at once.</p>
<p>The Knot doesn't publish its vendor pricing. Third-party {SRC['curate']} put paid listings anywhere from roughly $100 to $700+ a month, with costs rising in bigger, more competitive markets and with more coverage areas. Houston is a big, competitive market. Ask your rep for a clear per-month cost, contract length and lead count from last year before you renew.</p>
<div class="bp-tbl"><table><thead><tr><th>Channel</th><th>Who owns the lead</th><th>What it's good for</th><th>The catch</th></tr></thead><tbody>
<tr><td>The Knot / WeddingWire</td><td>Shared with the platform</td><td>Being seen by couples actively shopping</td><td>Side-by-side comparison, leads sent to many venues</td></tr>
<tr><td>Google Business Profile</td><td>You</td><td>"Wedding venues near me" and map searches</td><td>Needs steady photos and reviews</td></tr>
<tr><td>Your website and SEO</td><td>You</td><td>Searches by town, style and price</td><td>Takes months to build up</td></tr>
<tr><td>Google Ads</td><td>You</td><td>High-intent searches during engagement season</td><td>Wasted spend without tight keywords and tracking</td></tr>
<tr><td>Instagram and Pinterest</td><td>You</td><td>Showing the space, inspiring the date</td><td>Slow to turn into tours unless you push them to book</td></tr>
</tbody></table></div>
<!--fig:owned-->
<p>We'd keep a directory listing that's paying for itself and track it honestly. Ask every couple on the tour how they found you, and log it. Then put the next dollar into channels where the couple is yours.</p>"""),
            ("Wedding venue SEO and your Google Business Profile", f"""<p>Couples search the way they talk: "wedding venues in Magnolia TX," "barn wedding venue near Conroe," "outdoor wedding venues Houston under $10,000," "small wedding venue The Woodlands." Each of those is a page you could have.</p>
<h3>Google Business Profile</h3>
<ul>
<li>Use "Wedding venue" as the primary category. Add "Event venue" or "Banquet hall" as secondary only if you really host those events.</li>
<li>Upload photos from every season and every setup: ceremony, reception, getting-ready suites, the rain plan, a small 40-guest dinner and a full 200-guest reception. Couples want to see their size of wedding.</li>
<li>Connect a tour-booking link, not just "Contact us."</li>
<li>List your services: ceremony, reception, rehearsal dinner, bridal portraits, corporate events.</li>
</ul>
<h3>Your website</h3>
<ul>
<li>A pricing page with real starting prices (more on that below).</li>
<li>A page for each event type you want more of: weddings, elopements and micro weddings, quinceañeras, corporate events, holiday parties.</li>
<li>A page for the areas couples search from. A Magnolia venue should still have content that answers "wedding venues near The Woodlands" and "near Tomball" honestly, with drive times.</li>
<li>A real FAQ: capacity, vendor rules, alcohol policy, end time, rain plan, deposits, accessibility, lodging nearby.</li>
<li>Galleries of real weddings, with the photographer's credit and permission.</li>
</ul>
<p>Montgomery County is growing fast. The county grew from 620,551 residents in April 2020 to an estimated 781,194 in July 2025, a 25.9% jump, per {SRC['census']}. More households means more weddings, and more venues competing for them. Our <a href="/services/web-design-seo-pr/">web design and SEO</a> team builds these pages, and our <a href="/blog/reaching-customers-conroe-montgomery/">guide to reaching customers in Conroe and Montgomery</a> covers the local search side.</p>"""),
            ("Wedding venue Google Ads that bring tours, not tire-kickers", f"""<p>Google Ads works well for venues because the searches are so specific. Someone typing "wedding venues conroe tx pricing" is ready to tour. The trick is keeping your budget away from everything else.</p>
<h3>How we'd set it up</h3>
<ol>
<li><b>Keywords by intent:</b> "wedding venue [town]," "outdoor wedding venue near me," "barn wedding venue houston," "small wedding venue the woodlands." Use phrase and exact match.</li>
<li><b>Negative keywords from day one:</b> jobs, careers, free, DIY, "venue coordinator salary," and competitor venue names unless you mean to bid on them.</li>
<li><b>Location:</b> Montgomery County plus the Houston suburbs couples drive from. For venues, the "presence or interest" option in {SRC['geo']} can make sense, because a couple in Austin planning a hometown wedding in Tomball is a real buyer. Watch the location report and trim what doesn't convert.</li>
<li><b>Send clicks to a landing page,</b> not your homepage. Starting price, capacity, photos, reviews and a tour calendar above the fold. Our <a href="/blog/landing-pages-101/">landing pages guide</a> explains why this matters.</li>
<li><b>Count tours as the conversion,</b> not page views or form fills. Track calls too.</li>
<li><b>Front-load the budget</b> from late December through March, and again in late summer for holiday party bookings.</li>
</ol>
<p>Typical starting budgets for a single venue in this area run $1,000 to $3,000 a month during engagement season. That's an example range, not a rule; a Houston city venue will pay more per click than one in Montgomery. See our <a href="/services/search-marketing/">search marketing</a> page for how we manage it.</p>"""),
            ("Instagram and Pinterest: sell the date before the tour", """<p>Couples spend months collecting ideas before they ever contact a venue. Instagram and Pinterest are where your space becomes "the one" before they've seen it in person.</p>
<ul>
<li><b>Post real weddings, tagged.</b> Tag the couple (with permission), the photographer, the florist and the planner. Vendors share, and that's free reach to their followers.</li>
<li><b>Show the same space many ways.</b> Ceremony at golden hour, the reception flip, a rainy-day setup, a 50-guest dinner. Reels of a timelapse room flip do well.</li>
<li><b>Pin everything.</b> Every gallery image on your site should be pinnable, with a description like "outdoor wedding ceremony under oaks in Magnolia, Texas." Pinterest acts like a search engine for wedding ideas, and pins keep sending traffic for years.</li>
<li><b>Answer questions in Stories:</b> "What does $12,000 include here?" "Can we bring our own caterer?" Save them as Highlights.</li>
<li><b>Run paid social in engagement season.</b> A short video tour of the property, aimed at engaged people within your drive radius on Meta, with "Book a tour" as the button. Our <a href="/services/paid-social-advertising/">paid social</a> team runs these.</li>
</ul>"""),
            ("Tours are the conversion: speed-to-lead wins", """<p>Most venues lose bookings in the first hour, long before anyone walks the property. The couple sends an inquiry on a Tuesday night. They also sent it to four other venues. The first venue to reply with a real answer and an easy way to book a tour usually gets the visit. The one that replies Thursday with "Thanks for your interest! When can you chat?" usually doesn't.</p>
<!--fig:tour-->
<h3>A speed-to-lead process you can run with a small team</h3>
<ol>
<li><b>Auto-reply in under a minute</b> with your pricing guide, available dates near the one they asked for, and a link to self-book a tour.</li>
<li><b>Personal follow-up within an hour</b> during business hours, by text if they gave a number. Short and human: "Hi Maria, this is Jen at the venue. October 17 next year is open. Want to see it this Saturday?"</li>
<li><b>Offer tours on weekends and weekday evenings.</b> Most couples work.</li>
<li><b>Send a reminder</b> the day before the tour with directions and parking. Rural venues off FM roads are easy to miss in the dark.</li>
<li><b>Follow up after the tour</b> the same day with a recap, the proposal and a soft hold deadline.</li>
<li><b>Keep nurturing the ones who didn't book</b> with an email every couple of weeks: a real wedding feature, an opening on a Friday, a price for a smaller guest count.</li>
</ol>
<p>Track your numbers at each step. If you get plenty of inquiries but few tours, the problem is your reply speed or your pricing clarity. If you get tours but few bookings, it's the tour itself or the proposal. That's where you put your effort.</p>
<h3>Put your pricing on your website</h3>
<p>Venue owners hate this advice, so here's the argument. Couples on a $20,000 total budget don't want to tour a place that costs $18,000 for the venue alone. If you hide your price, those couples still find out, they just find out after taking your time on a tour. And the couples who can afford you often skip venues without prices, because they assume the worst.</p>
<p>You don't have to publish a full rate card. Do publish:</p>
<ul>
<li>A "starting at" price for Saturday peak season, plus Friday, Sunday and off-season starting prices.</li>
<li>What's included: hours, tables and chairs, setup and teardown, coordinator, bridal suite.</li>
<li>Guest capacity ranges for each package.</li>
<li>Deposit and payment schedule in plain English.</li>
</ul>
<p>Showing a lower Friday or Sunday price is also the simplest way to fill those days. A couple with a smaller budget sees a path to your venue instead of a dead end.</p>"""),
            ("Fill weekdays with corporate events and holiday parties", f"""<p>Saturdays from March through May and October through November sell themselves. The rest of the calendar is where a venue makes or loses its year.</p>
<ul>
<li><b>Corporate holiday parties.</b> Companies around The Woodlands, Springwoods Village and the I-45 corridor often start booking in August and September for December dates. Run a separate Google Ads campaign for "holiday party venue the woodlands" and "corporate event venue houston" starting in late summer, and reach office managers and HR leads with a LinkedIn or Meta campaign.</li>
<li><b>Weekday corporate use:</b> offsites, training days, company awards dinners and client appreciation events.</li>
<li><b>Other celebrations:</b> quinceañeras, rehearsal dinners, showers, milestone birthdays, vow renewals, celebrations of life.</li>
<li><b>Elopement and micro-wedding packages</b> on weekdays: a short ceremony, photos and a small dinner at a fixed price.</li>
</ul>
<p>Each of these deserves its own page on your site and its own ad group, because the people searching for them use different words and care about different things. A corporate planner wants AV, Wi-Fi, parking and an invoice. A quinceañera family wants capacity, a dance floor and whether outside catering is allowed.</p>"""),
            ("Reviews: ask at the right moment", """<p>Reviews matter twice for venues: once on Google, where they help you rank and get chosen in the map results, and once on The Knot and WeddingWire, where couples compare venues side by side.</p>
<ul>
<li><b>Ask during the glow.</b> The best time is within a week after the wedding, often when you send a thank-you note or share the first sneak-peek photos.</li>
<li><b>Make it one tap.</b> Send a direct link to your Google review form, and a second link for The Knot.</li>
<li><b>Ask the parents too.</b> They paid for a lot of it and are often happy to write a long review.</li>
<li><b>Write a real reply to each one</b> that mentions a detail from the day, like the sparkler exit or the rain plan that saved the ceremony. Future couples read the replies.</li>
<li><b>Ask vendors</b> who work your venue often (planners, photographers, caterers) for a Google review about what it's like to work there. Couples trust planners.</li>
</ul>
<p>Our <a href="/blog/complete-guide-google-reviews/">complete guide to Google reviews</a> has wording you can copy.</p>"""),
            ("Get ready before the ring photos hit Instagram", """<p>Proposal season runs roughly from Thanksgiving to Valentine's Day, so the prep happens now: put starting prices on your website, set up a self-booking tour calendar, write a one-minute auto-reply, and plan your Google Ads budget to peak in January. Then ask every couple on every tour how they found you, and write it down.</p>
<p>We work with hospitality and event businesses across Montgomery County and Greater Houston, from <a href="/digital-marketing-agency-conroe-tx/">Conroe</a> and <a href="/digital-marketing-agency-magnolia-tx/">Magnolia</a> to <a href="/digital-marketing-agency-montgomery-tx/">Montgomery</a> and <a href="/digital-marketing-agency-tomball-tx/">Tomball</a>. See our <a href="/industries/hospitality/">hospitality marketing</a> page for more. And if you're paying for Google or Meta ads but couldn't say how many tours they produced last year, start with a free <a href="/contact/">Ad Spend Leak Check</a>. We look through the account and send you a 10-minute video of where the money is leaking and what we'd change before January, within 48 hours.</p>"""),
        ],
        "faq": [
            ("How do I get more bookings for my wedding venue?",
             "Reply to inquiries within minutes with pricing and a self-booking tour link, publish starting prices on your website, and make sure your Google Business Profile and site show your space in every season and at different guest counts. Then put your ad budget into engagement season, from late December through March, and add Friday, Sunday and off-season packages to fill the calendar."),
            ("When do couples book wedding venues?",
             "Most couples choose the venue first, soon after they get engaged. December is consistently the most popular month to get engaged, the venue is usually booked early because the date depends on it, and The Knot has put the average engagement at around 15 months. That means a big wave of venue inquiries from late December through March for dates the following year."),
            ("Is The Knot worth it for wedding venues?",
             "It can be, since many couples start their venue search on planning sites like The Knot and WeddingWire. But listings aren't cheap in a big market like Houston, and leads often go to several venues at once. Ask your rep for last year's lead count, track how many tours and bookings came from it, and compare that cost to Google Ads and SEO."),
            ("Do Google Ads work for wedding venues?",
             "Yes, when the campaign targets specific searches like wedding venue plus a town name, blocks irrelevant searches with negative keywords, and sends clicks to a landing page with pricing and a tour calendar. Count booked tours as the conversion. Venues in Montgomery County often start around $1,000 to $3,000 a month during engagement season, then adjust based on results."),
            ("Should wedding venues show prices on their website?",
             "We think so. Showing starting prices for Saturday peak season, plus Friday, Sunday and off-season rates, filters out couples who can't afford you before they take up a tour slot, and it gives smaller-budget couples a path to your off-peak dates. You don't need a full rate card, just honest starting points and what's included."),
            ("How can a wedding venue fill weekdays?",
             "Market weekday packages for corporate events, holiday parties, rehearsal dinners, quinceañeras, showers and micro weddings. Give each a page on your site and its own ad group. Corporate holiday parties around The Woodlands and Houston often book in August and September, so start that campaign in late summer."),
        ],
        "figures": {
            "season": {
                "type": "columns",
                "title": "When venue inquiries come in",
                "sub": "Example inquiry volume by month for a Houston-area venue",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [100, 88, 74, 58, 46, 40, 38, 44, 52, 56, 60, 72],
                "highlight": [0, 1, 2],
                "y_label": "Inquiries vs. peak",
                "note": "Illustrative example",
                "alt": "Column chart of example wedding venue inquiries by month peaking January to March for Houston and Montgomery County venues",
                "caption": "Engagements peak in December, so venue inquiries usually surge in the first quarter.",
            },
            "spend": {
                "type": "stats",
                "title": "What US couples spent in 2025",
                "stats": [["$34K", "average wedding cost ($34,200)"], ["$13K", "average reception venue ($12,900)"], ["117", "average guest count"], ["$292", "average cost per guest"]],
                "note": "Source: The Knot Real Weddings Study 2026",
                "alt": "Stat tiles showing average wedding cost, venue cost, guest count and cost per guest for wedding venue marketing in Houston",
                "caption": "Figures cover US couples married in 2025, from The Knot Real Weddings Study.",
            },
            "owned": {
                "type": "compare",
                "title": "Rented leads vs. owned leads",
                "left": {"title": "Directory-only marketing", "items": ["Listed beside every competitor", "Leads sent to several venues", "Costs rise in big markets", "Visibility ends when you stop paying"]},
                "right": {"title": "Owned channels added", "items": ["Google profile and site rank by town", "Couple contacts only you", "Pricing and tours on your terms", "Pages keep working for years"]},
                "alt": "Comparison of directory listings versus owned marketing channels for wedding venues in Montgomery County and Houston",
                "caption": "Keep the directories that pay for themselves, and build the channels you own alongside them.",
            },
            "tour": {
                "type": "funnel",
                "title": "Where venue bookings are won or lost",
                "stages": [["Inquiries", "100"], ["Replied within an hour", "85"], ["Tours booked", "40"], ["Tours attended", "32"], ["Contracts signed", "12"]],
                "note": "Illustrative example",
                "alt": "Funnel showing example wedding venue inquiries turning into tours and booked weddings for a Houston area venue",
                "caption": "Track every step so you know whether to fix your reply speed, your tour or your proposal.",
            },
        },
    },
]
