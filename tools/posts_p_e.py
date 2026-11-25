"""Batch 16 (module e): food truck marketing in Houston, brewery/winery/taproom marketing in Houston and The
Woodlands, and catering company marketing in Houston.

Research, food trucks: DSHS mobile food vendor page (HB 2844, statewide license from July 1, 2026, Type I $309,
Type II $618 + $400 pre-licensing inspection, Type III $876 + $500); Texas Tribune on HB 2844 (local fire codes and
zoning stay local, public database of inspections and complaints); Houston Health Department MFU page (city
medallions not valid after July 1, 2026, DSHS license first then city inspection, daily servicing at approved
areas, restroom letter); Houston Fire Marshal food truck basics (LP-gas trucks 10 ft from buildings and 25 ft from
other LP trucks, 3A:40BC extinguisher, Type K for fryers); Houston Health Department council presentation, March 3,
2025 (1,369 permitted MFUs); The Woodlands Township special event policies (Township property only, insurance
certificate for every food and beverage vendor, $1M coverage, $1,000/$500 permit fee, 30-day pre-application);
Community Impact, March 2023 (400+ mobile food permits in Montgomery County, food truck parks off Sawdust Road and
FM 1488, Kirby Ice House rotating trucks); Whitespark on food trucks and Google Business Profile eligibility (no
direct guideline); Google's service-area help page (20 areas, about 2 hours' drive); Google Maps prohibited content
policy (review incentives and gating).
Brewery/winery: Axios on Texas brewery counts (440 in 2024 to 420 in 2025, production 1.422M barrels in 2025);
Axios Houston on 2024 closures and Saint Arnold; TABC marketing practices FAQ (no alcohol coupons, no mailed drink
coupons, one complimentary drink per legal-age customer per day without a coupon, no on-premise two-for-one, happy
hour ends 11 p.m., meal package rules, tier rules on advertising and $500 entertainment occasions); TABC
administrative rules (16 TAC 45.122 prohibited statements, 45.105(d) retailer internet advertising, 45.103 on-premises
promotions); Sprout Social, Aug 2026, on Meta (set 21+ manually in the US), Google and TikTok alcohol ad policies;
Houstonia on the 2019 beer-to-go law (288 ounces per day); Dallas Morning News on the Sept 1, 2019 start date;
Brewers Association, May 30, 2025 (HB 2441 direct shipping and HB 4773 interfacility transfer failed); TABC wine
shipping page (Texas G permit wineries ship statewide, 9 gallons a month and 36 a year per consumer, adult
signature); Untappd for Business pricing page (Essentials and Premium features, quote-based pricing); Visit Houston
on the Texas Bluebonnet Wine Trail; Islands, July 2025 ("over 10 member wineries").
Catering: Texas Medical Center about page (120,000+ employees, 10 million patient encounters); Energy Corridor
District (56,000+ jobs, employers listed); Owner.com, June 2026 (third-party estimate of ezCater commissions at
roughly 15%-25%, Grubhub catering marketing tiers); LinkedIn's budget page ($10 minimum daily budget); Houston Health
Department food permit FAQ (food dealer's permit for anyone who sells or serves food, home kitchens prohibited) and
Houston Permitting Center food dealer fees ($224.44 to $739.44 by risk); 93Q Country on 2027 RodeoHouston dates
(March 2-21, 2027).
Competitor/PAA phrasing read for "food truck marketing", "how to get more food truck customers", "food truck
google business profile", "brewery marketing ideas", "taproom marketing", "winery marketing", "TABC advertising
rules", "catering marketing ideas", "how to get corporate catering clients", "catering google ads".
Not used (couldn't verify from a primary page): ezCater's own published commission rates, Meta's and Google's alcohol
policy pages directly, current Montgomery County food truck movement rules after HB 2844.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # food truck post
    "dshs": A("https://www.dshs.texas.gov/mobile-food-vendors", "DSHS’s mobile food vendor page"),
    "tt": A("https://www.texastribune.org/2026/04/06/texas-food-truck-statewide-licensing-fee", "the Texas Tribune"),
    "hhd": A("https://www.houstonhealth.org/services/permits/food-permits/mobile-food-units", "Houston Health Department’s mobile food unit page"),
    "hfmo": A("https://cohips.houstontx.gov/fire/HFMO/FoodTrucks/1 Fire Permit - Food Trucks Basic Information.pdf", "Houston Fire Marshal’s food truck basics"),
    "hhdcouncil": A("https://311.houstontx.gov/council/committees/qol/20250303/mobile-food-units-health.pdf", "a March 2025 Health Department presentation to City Council"),
    "twp": A("https://www.thewoodlandstownship-tx.gov/files/sharedassets/main/v/1/parks-amp-recreation/documents/special-events/sep-policies-and-procedures.pdf", "the Township’s special event policies"),
    "ci_trucks": A("https://communityimpact.com/the-woodlands/dining/food-truck-popularity-rises-in-south-montgomery-county/", "Community Impact"),
    "whitespark": A("https://whitespark.ca/blog/are-food-trucks-eligible-for-a-google-business-profile/", "Whitespark’s look at food truck eligibility"),
    "gsab": A("https://support.google.com/business/answer/9157481?hl=en", "Google’s service-area help page"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    # brewery post
    "axios_tx": A("https://www.axios.com/local/austin/2026/08/28/texas-breweries-craft-beer-slowdown", "Axios"),
    "axios_hou": A("https://www.axios.com/local/houston/2025/05/09/houston-texas-craft-beer-market-saint-arnold", "Axios Houston"),
    "tabcfaq": A("https://www.tabc.texas.gov/faqs/alcohol-marketing-practices-faqs/", "TABC’s marketing practices FAQ"),
    "tabcrules": A("https://www.tabc.texas.gov/static/329891c3c2da233b5a6d710a6f442363/tabc-administrative-rules.pdf", "TABC’s administrative rules"),
    "sprout": A("https://sproutsocial.com/insights/social-media-alcohol-marketing/", "Sprout Social’s rundown of platform alcohol policies"),
    "houstonia": A("https://www.houstoniamag.com/articles/take-beer-home-from-your-favorite-houston-brewery-starting-sunday", "Houstonia"),
    "dmn": A("https://www.dallasnews.com/news/texas-politics/2019/06/15/texas-breweries-will-finally-get-sell-beer-go-starting-sept-1", "starting September 1, 2019"),
    "ba": A("https://www.brewersassociation.org/current-issues/texas-interfacility-transfer-beers-for-steers-and-beers-to-you-bills-fail-to-advance/", "the Brewers Association"),
    "wineship": A("https://www.tabc.texas.gov/texas-alcohol-laws-regulations/wine-shipping/", "TABC’s wine shipping page"),
    "untappd": A("https://utfb.untappd.com/get-pricing/", "Untappd for Business’s pricing page"),
    "visithou": A("https://www.visithoustontexas.com/travel-planning/itineraries-and-trip-ideas/food-and-drink/wine-trail-escape/", "Visit Houston’s wine trail itinerary"),
    "islands": A("https://www.islands.com/1914006/texas-delectable-bluebonnet-wine-trail-best-wine-state-southeast/", "Islands"),
    # catering post
    "tmc": A("https://www.tmc.edu/about-tmc/", "Texas Medical Center"),
    "ecd": A("https://energycorridor.org/energy-corridor-largest-employers/", "the Energy Corridor District"),
    "owner": A("https://www.owner.com/blog/catering-delivery-apps", "Owner.com’s 2026 comparison of catering apps"),
    "li": A("https://business.linkedin.com/advertise/ads/best-practices/maximize-your-budget", "LinkedIn’s budget guidance"),
    "hhdfaq": A("https://www.houstonhealth.org/services/permits/food-permits/faq", "Houston Health Department’s food permit FAQ"),
    "hpc": A("https://www.houstonpermittingcenter.org/hhd1003", "Houston Permitting Center"),
    "rodeo": A("https://93qcountry.com/1705006/2027-houston-livestock-show-and-rodeo-dates/", "March 2 through 21, 2027"),
}

TRUCK = "/blog/food-truck-marketing-houston/"
BREW = "/blog/brewery-winery-taproom-marketing-houston-the-woodlands/"
CATER = "/blog/catering-company-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: food trucks
    {
        "slug": "food-truck-marketing-houston",
        "title": "Food Truck Marketing in Houston: Permits, Posting Habits and Bookings That Fill the Calendar",
        "seo_title": "Food Truck Marketing in Houston: A Working Playbook",
        "desc": "Food truck marketing for Houston and The Woodlands: the 2026 state license, daily location posts, Google Business Profile, corporate and apartment bookings.",
        "category": "Local marketing",
        "icons": ["Instagram", "Google Business Profile", "Facebook"],
        "art": "b2",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for food truck marketing in Houston, The Woodlands and Spring",
        "related": ["restaurant-marketing-the-woodlands-houston", "party-event-rental-marketing-houston-the-woodlands", "geo-fencing-ads-target-customers-nearby"],
        "sections": [
            (None, f"""<p>Friday, 4:50 p.m., an apartment complex off Kuykendahl in Spring. The window opens at 5. The property manager promised “at least 60 residents,” and the generator is already humming. Your Instagram story with today’s spot went up at 4:45. Meanwhile, somebody in Building C googles your truck’s name, and Google says you’re closed, listed at an address in Tomball where you parked once in March.</p>
<p>By 6:15 you’ve served 22 people.</p>
<p>Most food truck marketing problems look like that evening. The food is fine. The information about where you are and when is scattered across three apps, and none of them agree.</p>
<p>Food truck marketing in Houston comes down to four habits: post your location the same way every day, keep your Google listing honest, book enough guaranteed private events (offices, apartments, breweries) that the slow days don’t sink the month, and pick festivals with a calculator instead of a gut feeling. Below is how we’d set each one up for a truck working Houston, The Woodlands, Cypress or Katy, starting with the rule change every Texas truck had to deal with in 2026.</p>"""),

            ("The 2026 rule change: one Texas license, but Houston still decides where you park", f"""<p>Until mid-2026, a truck that worked Houston, Harris County and Montgomery County could be juggling a separate permit for each one. House Bill 2844 changed that. Per {SRC['dshs']}, every mobile food vendor in Texas must hold a license from the Department of State Health Services starting July 1, 2026, with a pre-licensing inspection before it’s issued. Fees run by type: $309 for Type I (prepackaged food, no pre-licensing inspection fee), $618 plus a $400 pre-licensing inspection for Type II, and $876 plus $500 for Type III, which covers trucks that cook.</p>
<p>The city side didn’t disappear. The {SRC['hhd']} says City of Houston medallions stop being valid after July 1, 2026, and that operators should get the DSHS license and then schedule the city inspection. The same page still describes daily servicing at an approved central preparation facility and a signed restroom letter from a business near where you operate. As {SRC['tt']} reported, local fire codes and zoning stay local, so cities still control where and when trucks can set up.</p>
<p>Fire is its own permit inside city limits. The {SRC['hfmo']} requires a Fire Marshal’s permit for every food truck, at least one 3A:40BC extinguisher, a Type K extinguisher if you fry, and a hood and suppression system for grease-producing cooking. Trucks running propane must stay at least 10 feet from buildings and 25 feet from any other propane truck.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Who</th><th>What they control</th><th>Why it matters for marketing</th></tr></thead>
<tbody>
<tr><td>Texas DSHS</td><td>The statewide mobile food vendor license and inspections</td><td>A public database will list trucks, inspection results and complaints, per the Texas Tribune. Customers and event planners can look you up.</td></tr>
<tr><td>City of Houston (Health and Fire Marshal)</td><td>City inspection, fire permit, propane spacing, zoning</td><td>Event organizers inside the city will ask for your fire permit before they ask for your menu.</td></tr>
<tr><td>Other cities (Sugar Land, Pearland, Shenandoah, Conroe)</td><td>Their own zoning and fire rules</td><td>Check before you post a spot. Getting moved along mid-service is a marketing problem, too.</td></tr>
<tr><td>Private property owners and HOAs</td><td>Whether you can park there at all</td><td>Get written permission for any recurring spot, and keep it in the truck.</td></tr>
</tbody></table></div>
<!--fig:license-->
<p>Houston had 1,369 permitted mobile food units at the time of {SRC['hhdcouncil']}, which gives you a sense of the competition on a busy Saturday. Put your state license number and city fire permit on your catering and booking page. Planners at offices and apartment complexes are nervous about liability, and you can calm them down before they have to ask.</p>"""),

            ("The Woodlands and Montgomery County: events, parks and private lots", f"""<p>The Woodlands is a special case, because the Township isn’t a city. {SRC['ci_trucks']} reported in 2023 that the Township “does not have the authority to enact ordinances involving the operation of food trucks” except on Township-owned property, where park events usually need a special-use permit. The same story counted more than 400 active mobile food permits in Montgomery County and described food truck parks opening off Sawdust Road and FM 1488, plus venues like Kirby Ice House that rotate trucks instead of running a kitchen.</p>
<p>If you’re working an event in a Township park, {SRC['twp']} say an insurance certificate is required for every food and beverage vendor, with event coverage of at least $1 million single limit and the Township named as additional insured. Organizers pay a $1,000 permit fee for commercial festivals ($500 for nonprofits) and have a 30-day pre-application deadline for events with food. Some facilities also have exclusive concession contracts, so the organizer needs the concessionaire’s consent before you sell anything.</p>
<p>For your marketing, that means two things. Keep a current certificate of insurance ready to email in five minutes, because it’s the first thing a Woodlands event organizer will ask for. And don’t announce a Township park appearance until the organizer confirms the permit; we’ve watched trucks promote a Saturday in Northshore Park that never got approved.</p>
<p>Shenandoah, Oak Ridge North and Conroe each have their own rules. HOAs in Creekside Park, Harmony and the newer Conroe master-planned communities often allow trucks only through an HOA or lifestyle director booking. Those lifestyle directors are worth knowing by name.</p>"""),

            ("Posting your location: the daily habit that decides how many people show up", f"""<p>A restaurant has an address. You have a feed. If your followers can’t tell in three seconds where you are tonight, they’ll eat somewhere that has an address.</p>
<p>What we’d set up for any Houston truck:</p>
<!--fig:posting-->
<p>Keep the format identical every time: the same template graphic, the same order (spot name, street, hours, one menu highlight), and the location sticker on every Instagram story. Pin a weekly schedule post to the top of your Instagram grid and Facebook page every Monday, then update the story daily. When plans change because of rain or a cancelled event, post the change before you post anything else.</p>
<p>Facebook matters more for food trucks than most owners think. Neighborhood groups in Cypress, Kingwood, Atascocita and The Woodlands are where residents ask “any food trucks around tonight?” Read each group’s rules before posting. Many allow vendor posts one day a week, and the trucks that follow that rule get recommended by members instead of reported.</p>
<p>Build a text list as well. A QR code at the window that says “text TACO to get our weekly spots” turns a one-time customer into somebody you can reach Monday morning. Texting has rules: get clear opt-in for marketing messages and keep the record. Texas also brought marketing texts under its telephone solicitation law in 2025, so read our {L('/blog/sms-marketing-small-business-texas-rules/', 'SMS marketing rules for Texas businesses')} before you send the first one.</p>"""),

            ("Google Business Profile for a truck that moves", f"""<p>Google’s guidelines don’t mention food trucks directly. {SRC['whitespark']} (March 2025) found no line about them in the current rules. In practice, most trucks set up the profile like a service-area business: the address that matches your business documents, hidden from the public, with service areas listed instead.</p>
<p>Per {SRC['gsab']}, you can list up to 20 service areas, and the overall area shouldn’t extend more than about two hours of driving from where you’re based. For a truck based in Spring, a realistic list is Spring, The Woodlands, Tomball, Cypress, Klein, Humble, Kingwood, Conroe and north Houston. Listing Galveston and Austin won’t help anyone find you.</p>
<p>What to fill in, in order of how much it helps:</p>
<ul>
<li><b>Category.</b> Type “food truck” into the category field and see what Google offers, then compare it with the cuisine category that fits (“Taco restaurant,” “Barbecue restaurant”). Add “Caterer” as a secondary category if you do private events.</li>
<li><b>Hours.</b> Don’t set fake “open 11 to 9 every day” hours to look busy. Set the hours for your recurring spot if you have one, and use Google posts for the week’s schedule.</li>
<li><b>Menu and photos.</b> Upload the menu and a photo of the truck itself, so people at a festival can match the wrap to the listing.</li>
<li><b>Booking link.</b> Point the website button at a catering and events page with a quote form. That’s where the money is.</li>
</ul>
<p>If you park at the same food truck park or brewery five days a week, you’re closer to a fixed-location business, and some trucks list that address. Ask whether you can receive mail there and whether the property owner is fine with it before you try. A suspended profile is a long fix; our {L('/blog/google-business-profile-suspended-reinstatement/', 'reinstatement guide')} explains why. For the ranking side, see {L('/blog/rank-in-google-map-pack-houston/', 'how to rank in the Houston map pack')}.</p>"""),

            ("Corporate lunches and apartment complex events: the weekday money", f"""<p>Street service is fun and unpredictable. A booked office lunch with a guaranteed minimum pays the commissary bill. Most trucks we talk to want more of the second kind and don’t know how to ask for it.</p>
<p>Houston has plenty of buyers. Office parks along Research Forest and Lake Robbins in The Woodlands, the Energy Corridor along I-10, hospital campuses, distribution centers out by the Grand Parkway, and school districts with teacher appreciation weeks all book trucks. So do apartment complexes. Property managers run resident events monthly and have a budget line for them.</p>
<p>Make the yes easy:</p>
<!--fig:pitchkit-->
<p>Then send it to people who can say yes. For apartments, that’s the community manager or the regional marketing manager for a management company with ten properties in Spring and Cypress. For offices, it’s the office manager or HR coordinator. A short email with your one-pager, three dates you have open and a photo of a line at your window will outperform any ad you could buy for that audience.</p>
<p>Price it simply. Most trucks use one of two models: a guaranteed minimum (the host covers the gap if sales fall short) or a prepaid per-person package. Put both on your events page with “starting at” numbers. Write “[your price]” in your draft and fill it in; planners skip trucks that say “call for pricing.” Our {L(CATER, 'catering marketing guide')} covers the corporate side in more depth if you’re growing into full catering.</p>"""),

            ("Brewery partnerships: the easiest recurring spot in Houston", f"""<p>Plenty of Houston-area taprooms don’t run a kitchen, and their customers get hungry around the second pint. That’s a weekly spot with built-in traffic, shelter from the sun, restrooms and a host who wants you to succeed.</p>
<p>How to make it work for both sides:</p>
<ul>
<li>Agree on a recurring day (every Thursday beats “sometime next month”) and put it on both calendars.</li>
<li>Post together. A collab post on Instagram shows up on both accounts, which doubles reach for free.</li>
<li>Ask the brewery to list you in their event listing and their Untappd or website calendar.</li>
<li>Build a pairing special around their new release. You’re selling food; they handle anything with alcohol in it.</li>
<li>Track your sales by brewery night, and drop the ones that don’t work after six weeks.</li>
</ul>
<p>Breweries have their own advertising rules from TABC, so let them write anything about beer prices or drink specials. Our {L(BREW, 'brewery and taproom marketing post')} explains the brewery side of that partnership.</p>"""),

            ("Festival booking: run the math before you pay the fee", f"""<p>Festival season around Houston runs hardest in spring and fall, when the weather cooperates. The vendor application looks the same every time: an application fee, a booth fee or a percentage of sales, sometimes both, and a requirement to stay open for the whole event.</p>
<p>Before you apply, estimate four numbers. Attendance, how many other food vendors there will be, how many people you can actually serve per hour, and the hours you’ll be open. Throughput caps your upside no matter how big the crowd is.</p>
<!--fig:festival-->
<p>The illustrative chart above compares three kinds of bookings on net take for one day after fees and food cost. Big festivals can be great, but they’re also where trucks lose the most money on a rainy day. A private booking with a minimum often nets more with no risk.</p>
<p>Ask organizers for last year’s attendance and vendor count, and ask a truck that worked it. Use festivals for what they’re best at: putting your truck in front of thousands of people who’ll follow you afterward. That only works if your Instagram handle and text-list QR code are bigger on the truck than your logo.</p>"""),

            ("Reviews: ask at the window, not in a coupon", f"""<p>A truck with 300 Google reviews at 4.7 stars gets booked by office managers who’ve never tasted the food. Reviews are your sales team for private events.</p>
<p>The rules are the same as for any business. {SRC['gpol']} prohibits offering incentives for reviews (no free drink for a five-star review) and prohibits selectively asking only happy customers. Ask everyone, the same way.</p>
<p>What works at a truck:</p>
<ol>
<li>A QR code sticker on the pickup window that goes straight to your Google review form.</li>
<li>One line when you hand over the order: “If you liked it, a Google review helps us get booked for events.”</li>
<li>After every private event, a text or email to the host with the review link and a thank-you.</li>
<li>Reply to every review within a couple of days. Planners read the replies to see how you handle a cold burger.</li>
</ol>
<p>Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has reply templates you can copy.</p>"""),

            ("Houston weather: heat, rain and hurricane season", f"""<p>Weather is the one variable every Houston truck owner complains about, and most of them don’t plan their marketing around it.</p>
<p>Summer heat pushes lunch traffic down and dinner traffic later. Shift your street schedule to evenings in July and August and promote shade, misting fans or indoor seating at your brewery partners. Afternoon thunderstorms in summer and fall will kill a service in 20 minutes, so keep a “rain plan” post template ready and use it the moment the radar turns green.</p>
<p>Write weather into your private booking terms: what happens if it rains (move under cover, reschedule or cancel with notice) and what the minimum guarantee looks like on a stormy day. Putting it on your events page saves you from awkward conversations later.</p>
<p>Hurricane season runs June through November. Some trucks book work feeding crews and volunteers after storms, but that depends on fuel, power and whether your commissary is open. Have a plan and a post ready, and don’t promise anything you can’t deliver when the power’s out across Harris County.</p>"""),

            ("Paid ads: small budgets, tight radius, two jobs", f"""<p>Most trucks don’t need much ad spend. When they do, it’s for two jobs: getting new followers near a recurring spot and getting private event inquiries.</p>
<p><b>Meta ads around your regular spots.</b> A radius of a few miles around the brewery or truck park you’re at every week, a short video of the food being made, and a message like “Every Thursday at [brewery], 5 to 9.” Budget something like $5 to $15 a day for a few weeks, and judge it on follower growth and Thursday sales. The {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads guide for local businesses')} covers setup.</p>
<p><b>Google Ads for event bookings.</b> Search terms like “food truck catering Houston,” “food truck for party The Woodlands,” “taco truck catering Katy” and “food truck for corporate event.” Send them to your events page with the quote form. Add negatives on day one: for sale, used, rental, jobs, hiring, permit, license, “how to start,” commissary and wrap. A few hundred dollars a month is a reasonable test in our experience. See {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'our Houston CPC benchmarks')} for a sense of click costs, and our {L('/services/paid-social-advertising/', 'paid social team')} if you’d rather not run it yourself.</p>"""),

            ("What to do in your first 30 days", f"""<p>If you’re starting from a messy setup, here’s the order we’d fix things in:</p>
<!--fig:plan-->
<p>Then track three numbers every week: private event inquiries, bookings and average sales per street service. Those tell you where to spend the next hour and the next dollar.</p>
<p>If you’d like a senior strategist to build a plan around your truck, your spots and your booking goals, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Do Houston food trucks need a state permit now?",
             "Yes. Under House Bill 2844, every mobile food vendor in Texas needs a license from the Department of State Health Services starting July 1, 2026. Fees depend on the type of food, from $309 for prepackaged food up to $876 plus a $500 pre-licensing inspection for trucks that cook. Houston’s Health Department still schedules a city inspection, and the Houston Fire Marshal still requires its own permit inside city limits."),
            ("Can a food truck have a Google Business Profile?",
             "Usually, yes. Google’s guidelines don’t address food trucks directly, so most trucks set up a service-area profile with the business address hidden and up to 20 service areas listed, within about two hours’ drive of their base. Add your menu, photos of the truck, a catering or events link, and keep hours honest. If you park at one permanent spot daily, ask about listing that address first."),
            ("How do food trucks get booked for corporate events in Houston?",
             "Build a simple events page with packages, minimums, your license and insurance, then email office managers, HR coordinators and apartment community managers directly. Include photos of a line at your window, three open dates and starting prices. Office parks in The Woodlands, the Energy Corridor and hospital campuses all book trucks. Follow up after each event with a review link and an offer to rebook."),
            ("Are festivals worth it for a food truck?",
             "Sometimes. Before applying, estimate attendance, the number of other food vendors, how many people you can serve per hour and the hours you’ll be open, then subtract the booth fee, any percentage of sales and food cost. Throughput limits your upside. Big festivals are best for gaining followers; private bookings with a guaranteed minimum often net more with far less weather risk."),
            ("What should a food truck post on Instagram every day?",
             "Post the same thing in the same format every day: where you are, the street or cross streets, your hours and one menu highlight, with a location sticker on the story. Pin a weekly schedule post every Monday, and post any change before anything else. Short videos of food being made and lines at the window work better than polished graphics."),
        ],
        "figures": {
            "license": {
                "type": "stats",
                "title": "Texas mobile food vendor license fees",
                "stats": [["$309", "Type I, prepackaged food"], ["$618", "Type II, plus $400 pre-licensing inspection"], ["$876", "Type III, plus $500 pre-licensing inspection"], ["Jul 1", "2026 start date statewide"]],
                "note": "Source: Texas DSHS",
                "alt": "Stats on the Texas statewide food truck license fees that affect food truck marketing in Houston and The Woodlands",
                "caption": f"Application fees from {SRC['dshs']}. City fire permits are separate.",
            },
            "posting": {
                "type": "steps",
                "title": "A daily location-posting routine",
                "sub": "Ten minutes a day, same order every time",
                "steps": [["Monday: weekly schedule", "Pin one post with every spot and time for the week on Instagram and Facebook."], ["Morning: today’s spot", "Story with the location sticker, cross streets, hours and one menu item."], ["One hour before open", "A short video of prep or the first order, tagged to the host."], ["During service", "Repost tagged customer stories; reply to messages asking where you are."], ["Changes: post first", "Rain, sellout or cancellation goes up before anything else."]],
                "alt": "Steps for a daily food truck location posting routine on Instagram and Facebook in Houston and The Woodlands",
                "caption": "Consistency matters more than design. People learn where to look.",
            },
            "pitchkit": {
                "type": "checklist",
                "title": "Corporate and apartment booking kit",
                "sub": "Have it ready before the first email",
                "items": ["One-page PDF with packages and starting prices", "Guaranteed-minimum and prepaid options", "State license and Houston fire permit numbers", "Certificate of insurance, ready to email", "Space needs: footprint, power, generator noise", "Photos of the truck and a line at the window", "Rain and heat policy in writing", "Review link and three open dates"],
                "alt": "Checklist for a food truck corporate and apartment event booking kit in Houston and The Woodlands",
                "caption": "Office and property managers say yes faster when nothing is missing.",
            },
            "festival": {
                "type": "bars",
                "title": "Net take for one day, three booking types",
                "sub": "After booth fees, percentage of sales and food cost",
                "items": [["Large festival, good weather", 1900, "$1,900"], ["Office lunch, guaranteed minimum", 1100, "$1,100"], ["Brewery night, regular spot", 700, "$700"], ["Large festival, rained out", -400, "-$400"]],
                "highlight": [1],
                "note": "Illustrative example. Your numbers will differ.",
                "alt": "Bar chart comparing illustrative food truck earnings from festivals, office lunches and brewery nights in Houston",
                "caption": "The rained-out festival is the one owners forget to model.",
            },
            "plan": {
                "type": "steps",
                "title": "First 30 days for a Houston food truck",
                "steps": [["Week 1: clean up Google", "Fix category, hours, service areas, photos and the booking link."], ["Week 1: one posting template", "Same graphic and order for daily location posts."], ["Week 2: events page", "Packages, minimums, license, insurance, weather policy, quote form."], ["Week 3: outreach", "Email 20 office and apartment contacts and two breweries."], ["Week 4: reviews and texts", "Window QR code for reviews and a text list sign-up."]],
                "alt": "Thirty-day food truck marketing plan for Houston, The Woodlands and Spring",
                "caption": "Ads come after this list, not before it.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: breweries, wineries, taprooms
    {
        "slug": "brewery-winery-taproom-marketing-houston-the-woodlands",
        "title": "Brewery, Winery and Taproom Marketing in Houston and The Woodlands",
        "seo_title": "Brewery & Taproom Marketing in Houston & The Woodlands",
        "desc": "Brewery, winery and taproom marketing in Houston and The Woodlands: TABC ad rules, 21+ ad targeting, events, beer to go, Untappd and Google Business Profile.",
        "category": "Local marketing",
        "icons": ["Meta", "Google Business Profile", "Instagram"],
        "art": "b4",
        "hero": "ticket",
        "hero_alt": "Illustration of an event ticket for brewery, winery and taproom marketing in Houston and The Woodlands",
        "related": ["restaurant-marketing-the-woodlands-houston", "how-to-sell-more-event-tickets-houston", "sms-marketing-small-business-texas-rules"],
        "sections": [
            (None, f"""<p>Thursday, trivia night, a taproom off the Grand Parkway. Thirty-eight people, which is fine, but last spring it was 70. The Meta ad for the new hazy IPA got rejected because the audience was set to 18 and up. The Untappd menu still lists the Oktoberfest that kicked two weeks ago. Somebody asks the bartender whether the “Two for Tuesday” post on Instagram is real, and the bartender isn’t sure that’s even legal.</p>
<p>It isn’t, at least not on-premise.</p>
<p>Brewery, winery and taproom marketing in Houston and The Woodlands works when you give people a reason to show up on a specific night, keep your menus and hours accurate everywhere they look, and stay inside TABC’s advertising rules and the ad platforms’ alcohol policies. Beer to go and wine shipping turn one visit into a second sale. The rest of this post is the detail: what’s allowed, what to post, and how to tell which nights are earning their keep.</p>"""),

            ("The Houston craft beer market you’re selling into", f"""<p>The boom years are over. Texas had 440 breweries in 2024 and 420 in 2025, per Brewers Association figures reported by {SRC['axios_tx']}. Openings fell below 25 in each of those years while closures stayed at 25 or more. Production dipped 8.7% in 2024, then recovered to about 1.42 million barrels in 2025. The same story notes that Texas heat and long summers are hard on taprooms with patios that aren’t climate controlled, and that attractions like a soccer field or an arcade have become “table stakes.”</p>
<p>Houston felt it. {SRC['axios_hou']} listed Buffalo Bayou Brewing, Ingenious Brewing and Twisted Acre Brewery among the area’s recent closures or mergers, while Saint Arnold, the city’s oldest craft brewer, grew its barrels 5.2% in 2024.</p>
<!--fig:market-->
<p>What that tells us: the taprooms that keep winning give people a plan for the evening. Trivia, run clubs, food trucks, a release party, a patio with shade and fans, space for kids and dogs. Beer quality is the entry ticket, and most Houston drinkers already have three good breweries within 20 minutes.</p>"""),

            ("TABC advertising rules: what a taproom or tasting room can and can’t say", f"""<p>This is the part most brewery and winery marketing guides skip, and it’s where Texas is stricter than people expect. We’re marketers, not lawyers, and your permit type matters, so run anything borderline past TABC or your attorney. Here’s what the commission’s own materials say.</p>
<p><b>What an ad can’t contain.</b> Under 16 TAC §45.122 in {SRC['tabcrules']}, alcohol advertising can’t include false or misleading statements, statements disparaging a competitor’s product, anything obscene or indecent, or statements about intoxicating qualities. Curative or therapeutic claims are also out. So “the strongest beer in Montgomery County” and “our red wine is good for your heart” are both problems.</p>
<p><b>Online counts.</b> The same rules apply to advertising on the internet, and §45.105(d) says retailer internet advertising has to follow the on-premise promotion, coupon and sweepstakes rules. Your Instagram post is an ad as far as TABC is concerned.</p>
<p><b>Promotions.</b> {SRC['tabcfaq']} says coupons for alcohol purchases aren’t allowed and mailing a drink coupon is prohibited. A retailer can give one complimentary drink per legal-age customer per business day, but not through a ticket or coupon. On-premise two-for-one sales are illegal, and reduced drink prices have to end by 11 p.m. A meal package with a discounted or free drink is fine if no coupon is required to get it, and you can advertise that package on social media.</p>
<!--fig:promos-->
<p><b>The tier rules, if you also distribute.</b> If your beer or wine is in bars, restaurants or H-E-B, the FAQ is clear that you can’t pay a retailer for featuring your brand, and you can’t give retailers branded apparel or glassware for free (promotional items have to be sold). Entertaining a retailer is capped at an “occasion” worth no more than $500 per person, and you have to be there. Listing the bars that carry you on your website is fine, as long as nobody pays for the listing.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Promotion idea</th><th>How TABC’s FAQ treats it</th><th>A safer way to run it</th></tr></thead>
<tbody>
<tr><td>“Show this post for $2 off a pint”</td><td>A coupon for alcohol, not allowed</td><td>“$2 off pints until 7 p.m. Thursday,” no post required</td></tr>
<tr><td>BOGO pints on Tuesday</td><td>On-premise two-for-one is illegal</td><td>A Tuesday price on one featured pour</td></tr>
<tr><td>Half-price drinks until midnight</td><td>Reduced prices must end at 11 p.m.</td><td>End the special at 10 or 11</td></tr>
<tr><td>Free beer for a five-star review</td><td>Also breaks Google’s review rules</td><td>Ask everyone for a review, no reward</td></tr>
<tr><td>Burger and a pint for one price</td><td>Meal package is allowed if no coupon is needed</td><td>Advertise the package; don’t require a code</td></tr>
</tbody></table></div>"""),

            ("Meta and Google alcohol ad policies: 21+ and nothing that looks like excess", f"""<p>The ad platforms add their own layer. According to {SRC['sprout']} (August 2026), Meta allows alcohol ads that follow local laws and use age and country targeting, but Meta’s default minimum age is 18, so U.S. advertisers set 21+ themselves. Google allows alcohol ads but bars targeting minors and promoting excessive or underage drinking. TikTok has allowed alcohol ads since August 2024 and bans offering alcohol as a prize.</p>
<p>The setup we’d use on Meta:</p>
<!--fig:meta-->
<p>Creative matters as much as targeting. Show people of obvious legal age, keep drinking in a social setting, and leave out anything about getting drunk, chugging or driving. Food, music, trivia teams and dogs on the patio all perform well for taprooms in our experience, and they’re easy to approve.</p>
<p>On Google, the most useful campaigns for a taproom or winery are small search campaigns on terms like “brewery near me,” “breweries in The Woodlands,” “winery near Magnolia TX,” “trivia night Spring TX” and “wine tasting near Houston,” sent to a landing page that shows tonight’s events and hours. Our {L('/services/search-marketing/', 'search marketing team')} sets these up with the right exclusions, and our {L('/services/paid-social-advertising/', 'paid social team')} handles the Meta side.</p>"""),

            ("Beer to go, wine shipping and direct sales in Texas", f"""<p>The to-go fridge is a marketing channel, and Texas law shapes how big it can be.</p>
<p>Texas breweries have been allowed to sell beer to go {SRC['dmn']}. {SRC['houstonia']} reported the cap at the time as 288 ounces per person per day, which is 24 cans, a case, or nine 32-ounce crowlers. That limit is why release-day posts should say “limit one case per person” in plain words, so nobody drives in from Katy expecting more.</p>
<p>Shipping beer directly to consumers still isn’t legal in Texas. {SRC['ba']} reported on May 30, 2025 that HB 2441, the direct-to-consumer shipping bill nicknamed “Beers To You,” failed in the 2025 session, along with HB 4773, which would have let breweries move beer between their own locations.</p>
<p>Wineries have more room. Per {SRC['wineship']}, a Texas winery with a Winery Permit (G) can ship to consumers anywhere in the state, up to 9 gallons per consumer per month and 36 gallons in any 12-month period. A carrier with a Carrier’s Permit has to deliver, and an adult of at least 21 has to sign with valid ID.</p>
<!--fig:dtc-->
<p>For a winery, that makes a wine club with shipping the most valuable thing your marketing can build. Every Houston day-tripper who joins is a customer who doesn’t have to drive back to Plantersville to buy again. For a brewery, the equivalent is a release list (email and text) that turns new cans into a reason to come in this weekend.</p>"""),

            ("Events, trivia nights and a calendar people can plan around", f"""<p>Recurring events are the backbone of taproom marketing. A weekly trivia night, a Tuesday run club and a monthly makers’ market give regulars a habit and give you something new to post every week.</p>
<!--fig:calendar-->
<p>A few things we’ve seen work in north Houston:</p>
<ul>
<li>Keep the weekly lineup stable for at least three months before you judge it. Trivia nights take a while to build teams.</li>
<li>Put every event on a single events page on your website, then copy it to Facebook events, Google Business Profile posts and Untappd. One source, many places.</li>
<li>For ticketed events (release parties, wine dinners, beer and food pairings), sell through a ticketing link and track sales back to the ad. Our {L('/blog/how-to-sell-more-event-tickets-houston/', 'guide to selling event tickets in Houston')} covers the setup.</li>
<li>Plan around the weather. Patio events do well in March through May and October through November; summer events belong indoors or after sunset.</li>
<li>Family-friendly hours with a playground or yard games bring in parents from Creekside Park, Harmony and Woodforest on weekend afternoons, and those visits often turn into regulars.</li>
</ul>"""),

            ("Food truck partnerships", f"""<p>If you don’t have a kitchen, a reliable food truck rotation keeps people from leaving after one pint. The best setups we see have a fixed truck on fixed nights and a shared posting plan: a collab post on Instagram, both calendars updated, and the truck tagged in every story.</p>
<p>Keep the money simple. In the setups we’ve seen, many taprooms don’t charge the truck at all; others take a small flat fee or ask for a minimum number of nights. Whatever you agree, write it down, and keep the beer-price messaging on your side of the partnership since TABC rules apply to you, not the truck. We wrote a whole guide on {L(TRUCK, 'food truck marketing in Houston')} that covers the truck’s side, and it’s worth sending to the trucks you work with.</p>"""),

            ("Untappd, Google Business Profile and the menu problem", f"""<p>Beer drinkers check three places before they come in: your Instagram, Google Maps and Untappd. If those three say different things, you look closed.</p>
<p><b>Untappd.</b> Per {SRC['untappd']}, the Essentials plan includes verified venue status, digital, print and QR menus, one-click menu publishing to your website and the app, POS integrations (Toast, Square, GoTab and others), push alerts to Untappd followers when your menu changes, and an events manager. Premium adds wine, spirits and ready-to-drink support, unlimited menu items and API access. Pricing is by quote and varies by market. For a brewery with a rotating tap list, the menu sync alone saves an hour a week and stops the “is the Oktoberfest still on?” question.</p>
<p><b>Google Business Profile.</b> Pick the primary category that matches what you are: Brewery, Brewpub, Winery or Wine bar. Add secondary categories only for things you really do, like Beer garden or Event venue. Keep hours exact, including holiday hours. Upload photos of the taproom, the patio, the kids’ area if you have one and the to-go fridge. Post every event. Answer the common questions (dogs, kids, outside food, parking) in your profile description and on your website.</p>
<p>Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers the ranking side, and {L('/blog/complete-guide-google-reviews/', 'our reviews guide')} covers getting more of them without breaking Google’s rules. A taproom with 900 reviews at 4.7 stars tends to outrank one with 140 at 4.9 for “brewery near me,” in our experience.</p>"""),

            ("Wine trails, day-trippers and tourism north of Houston", f"""<p>Wineries and some breweries north and west of The Woodlands sell to visitors as much as locals. {SRC['visithou']} describes the Texas Bluebonnet Wine Trail as running between I-45 and U.S. 290, with wineries in towns like Plantersville, Navasota, Chappell Hill, New Waverly and Huntsville, and the closest group about an hour and a half from Houston. {SRC['islands']} counted more than 10 member wineries in July 2025.</p>
<!--fig:trail-->
<p>Visitors plan these trips on their phones the week before, with searches like “wineries near The Woodlands,” “winery near Magnolia TX,” “day trip from Houston wine” and “wine tasting near Montgomery TX.” So:</p>
<ul>
<li>Build a “Plan your visit” page with hours, tasting prices, reservations, group policy, the drive time from The Woodlands and Houston, and nearby stops (other wineries, a lunch spot, Lake Conroe or downtown Montgomery).</li>
<li>Run search ads on day-trip terms on Thursdays and Fridays, when people plan the weekend.</li>
<li>Use Meta video of the vineyard, the porch and the tasting room, targeted 21+ to Houston, The Woodlands, Katy and Cypress.</li>
<li>Partner with neighboring wineries and B&Bs on a shared itinerary page. Visitors want a whole day, and you get links from it.</li>
</ul>"""),

            ("Email, texts and the mug club", f"""<p>Your best customers already gave you their email when they joined the mug club or the wine club. Most taprooms send them one newsletter a quarter. Send a short one every week instead: what’s on tap, what’s new, this week’s events.</p>
<p>Texts work for release days and sellouts. Get explicit opt-in, keep marketing texts separate from order texts, and remember TABC: no drink coupons in the text. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'SMS rules for Texas businesses')} covers the consent side.</p>"""),

            ("What to track, and a first-month plan", f"""<p>Track four things weekly: door count or transactions by night, to-go sales, event attendance by event, and new email or text sign-ups. Tie ads to those, not to likes.</p>
<p>A first month we’d run for a taproom in The Woodlands, Spring, Conroe or Tomball:</p>
<ol>
<li>Week one: fix Google Business Profile, Untappd and website hours so they match. Set Meta ad accounts to 21+.</li>
<li>Week two: audit every promotion on your social accounts against the TABC FAQ and take down anything that reads like a coupon or a two-for-one.</li>
<li>Week three: lock a weekly event lineup and a food truck rotation for the next 12 weeks, on one events page.</li>
<li>Week four: start a small search campaign for brewery-near-me and event terms, and a Meta campaign for your biggest weekly event.</li>
</ol>
<p>If you’d like a senior strategist to build a plan for your brewery, winery or taproom, <a href="/contact/">get in touch</a>. Our {L('/industries/beverage-spirits/', 'beverage work')} has a bit more about how we think about drink brands.</p>"""),
        ],
        "faq": [
            ("Can a Texas brewery or bar post drink specials on social media?",
             "Yes, with limits. TABC treats online posts as advertising, so the same promotion rules apply. You can post prices and specials, but not alcohol coupons, on-premise two-for-one offers, or reduced drink prices after 11 p.m. A meal package with a discounted drink is allowed if no coupon is needed. Ads also can’t make claims about intoxicating effects or health benefits. Check borderline promotions with TABC."),
            ("How do I target alcohol ads to 21+ on Facebook and Instagram?",
             "Meta’s default minimum age is 18, so U.S. breweries, wineries and bars should set the age range to 21 and older in every ad set and use the age restriction setting on the Facebook Page and Instagram account. Keep creative focused on people of clear legal age in social settings, and avoid anything that suggests excessive drinking or driving, which both Meta and Google prohibit."),
            ("How much beer can a Texas brewery sell to go?",
             "Texas breweries have been allowed to sell beer to go since September 1, 2019, with a limit reported at the time of 288 ounces per person per day, which is 24 cans or one case. Direct shipping of beer to consumers is still not allowed; a 2025 bill to permit it failed. Texas wineries with a G permit can ship wine to consumers anywhere in Texas."),
            ("What are the best marketing ideas for a taproom in The Woodlands or Houston?",
             "Run a stable weekly lineup like trivia, run clubs and food trucks for at least three months, keep Google, Untappd and your website menu and hours identical, and post every event in all three places. Add family and dog-friendly hours if your space allows. Build an email and text list for releases, and run small search ads on brewery-near-me and event terms."),
            ("Is Untappd for Business worth it for a small brewery?",
             "For most breweries with a rotating tap list, yes. The Essentials plan includes verified venue status, menus that publish to your website and the Untappd app in one click, POS integrations, push alerts to followers when your menu changes and an events manager. Pricing is quote-based and varies by market, so judge it by the staff time it saves and whether menus stay accurate."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "Texas craft beer, by the numbers",
                "stats": [["420", "Texas breweries in 2025, down from 440"], ["1.42M", "barrels brewed in Texas in 2025"], ["8.7%", "production drop in 2024"], ["5.2%", "Saint Arnold’s barrel growth in 2024"]],
                "note": "Source: Brewers Association data via Axios",
                "alt": "Stats on the Texas craft beer market for brewery and taproom marketing in Houston and The Woodlands",
                "caption": f"Figures from {SRC['axios_tx']} and {SRC['axios_hou']}.",
            },
            "promos": {
                "type": "compare",
                "title": "Taproom promotions under TABC rules",
                "left": {"title": "Likely problems", "items": ["“Show this post for $2 off”", "BOGO pints on Tuesday", "Half-price drinks until midnight", "“Strongest beer in town”", "Free pint for a review"]},
                "right": {"title": "Safer versions", "items": ["A posted price, no coupon needed", "One featured pour at a set price", "Specials that end by 11 p.m.", "Describe flavor, style and ingredients", "Ask everyone for a review, no reward"]},
                "alt": "Comparison of risky and safer taproom promotions under TABC advertising rules for Houston and The Woodlands breweries",
                "caption": "Based on TABC’s marketing practices FAQ. Your permit type matters; ask TABC when unsure.",
            },
            "meta": {
                "type": "steps",
                "title": "Setting up Meta ads for a taproom",
                "sub": "Do this before the first ad, or it gets rejected",
                "steps": [["Age-restrict the Page and Instagram", "Set the account age restriction for alcohol to 21+."], ["Ad set age: 21 to 65+", "Meta defaults to 18. Change it every time."], ["Location: where drinkers live", "A radius around the taproom plus nearby suburbs."], ["Creative: social, not excess", "Clearly adult people, food, games, music. No chugging or driving."], ["Offer: event or release", "No coupons, no two-for-one. Link to the events page."]],
                "alt": "Steps to set up Meta alcohol ads targeted 21+ for a brewery or taproom in Houston and The Woodlands",
                "caption": f"Policy summary from {SRC['sprout']}.",
            },
            "dtc": {
                "type": "stats",
                "title": "Direct sales limits in Texas",
                "stats": [["288 oz", "beer to go per person per day"], ["9 gal", "wine shipped per consumer per month"], ["36 gal", "wine per consumer per 12 months"], ["21+", "adult signature on wine delivery"]],
                "note": "Sources: Houstonia (2019 law), TABC wine shipping page",
                "alt": "Stats on Texas beer to go and wine shipping limits for brewery and winery marketing near Houston and The Woodlands",
                "caption": "Beer still can’t be shipped to consumers in Texas.",
            },
            "calendar": {
                "type": "checklist",
                "title": "A weekly taproom lineup that builds habits",
                "sub": "Pick four or five and keep them for 12 weeks",
                "items": ["Tuesday: run club with a post-run pour", "Wednesday: trivia, same host every week", "Thursday: fixed food truck night", "Friday: new release or tap takeover", "Saturday afternoon: family and dog hours", "Sunday: yoga, makers’ market or game day", "Monthly: ticketed pairing dinner", "Every event on one page, copied everywhere"],
                "alt": "Checklist of weekly taproom events for brewery marketing in The Woodlands, Spring and Houston",
                "caption": "A lineup people can remember beats a new idea every week.",
            },
            "trail": {
                "type": "map",
                "title": "Day-trip territory north of Houston",
                "sub": "Where taproom and winery visitors drive from and toward",
                "highlight": ["The Woodlands", "Magnolia", "Montgomery", "Conroe", "Willis", "Tomball", "Houston"],
                "alt": "Map of north Houston and Montgomery County towns for winery and brewery tourism marketing near The Woodlands",
                "caption": f"The Texas Bluebonnet Wine Trail runs between I-45 and U.S. 290, per {SRC['visithou']}.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: catering
    {
        "slug": "catering-company-marketing-houston",
        "title": "Catering Company Marketing in Houston: Win Corporate Orders, Weddings and Repeat Clients",
        "seo_title": "Catering Company Marketing in Houston: Get More Orders",
        "desc": "Catering company marketing in Houston: corporate clients in the Energy Corridor and Medical Center, ezCater, Google Ads, LinkedIn, pricing pages and peaks.",
        "category": "Strategy",
        "icons": ["Google Ads", "LinkedIn", "Google Business Profile"],
        "art": "b6",
        "hero": "restaurant",
        "hero_alt": "Illustration of a restaurant table for catering company marketing in Houston and The Woodlands",
        "related": ["wedding-venue-marketing-houston-montgomery-county", "restaurant-marketing-the-woodlands-houston", "b2b-marketing-houston-energy-industrial"],
        "sections": [
            (None, f"""<p>Tuesday, 7:12 a.m. An executive assistant at a research office in the Texas Medical Center emails your general inbox: lunch for 40 on Thursday, six vegetarian, two gluten-free, individually labeled, invoice to a PO number. You see it at 11:30, after the morning deliveries. You reply with a menu PDF at noon.</p>
<p>She booked someone on ezCater at 8:05.</p>
<p>That gap, about four hours, is where most Houston caterers lose corporate business. The food is good. The answer just came too late, and nothing on the website could have answered it sooner.</p>
<p>Catering company marketing in Houston works when you make it easy for the people who order (office managers, executive assistants, event planners, couples) to see prices, check dates and book fast. Then you earn the repeat order. This post covers corporate catering in the Energy Corridor and the Medical Center, weddings, marketplaces like ezCater, Google Ads and LinkedIn, pricing pages, tastings, venue preferred-vendor lists and the Houston catering calendar.</p>"""),

            ("Who actually buys catering in Houston", f"""<p>Houston has a lot of big workplaces close together, which is good news for caterers. {SRC['tmc']} describes itself as the largest medical complex in the world, with more than 120,000 employees and about 10 million patient encounters a year. {SRC['ecd']} says its employers, including bp, Shell, ConocoPhillips, CITGO, Baker Hughes and MD Anderson West Houston, account for more than 56,000 local jobs. Add the office towers along Research Forest, Lake Robbins and Hughes Landing in The Woodlands, the Westchase and Greenway Plaza offices, and the plants and engineering firms on the east side, and you have a steady weekday market.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Buyer</th><th>What they search or ask</th><th>What wins the order</th></tr></thead>
<tbody>
<tr><td>Office manager or executive assistant</td><td>“Corporate lunch catering Houston,” “boxed lunches Energy Corridor”</td><td>Online ordering, per-person prices, labeled meals, PO and invoice billing, on-time delivery</td></tr>
<tr><td>Hospital and research departments (TMC)</td><td>“Catering near Texas Medical Center,” “breakfast catering for staff meeting”</td><td>Early delivery windows, dietary labels, vendor setup paperwork, parking and loading know-how</td></tr>
<tr><td>Corporate event planners</td><td>“Holiday party catering Houston,” “company picnic catering The Woodlands”</td><td>Packages, staffing, bar partners, certificates of insurance, references</td></tr>
<tr><td>Couples and wedding planners</td><td>“Wedding catering Houston,” “wedding caterer Montgomery County”</td><td>Tastings, sample menus with price ranges, venue experience, reviews</td></tr>
<tr><td>Families, schools and churches</td><td>“Graduation party catering Katy,” “BBQ catering Spring TX”</td><td>Simple packages, quick quotes, pickup or drop-off options</td></tr>
</tbody></table></div>
<!--fig:market-->
<p>Each row needs a slightly different page and a different ad, but corporate is where most caterers we talk to want to grow, because it repeats.</p>"""),

            ("Corporate catering: what admins and office managers need from you", f"""<p>The person ordering corporate lunch isn’t a foodie. They’re someone with a dozen other jobs who will be blamed if lunch is late or the vegan option is missing. Your marketing should promise them a quiet Thursday.</p>
<!--fig:corporate-->
<p>Two things set caterers apart in this market.</p>
<p>First, speed. If someone emails at 7 a.m., an auto-reply with your online ordering link and a phone number that a human answers will save half those orders. Better still, put online ordering for drop-off catering on your own site, with a cutoff time and per-person pricing, so the admin can finish the order without you. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the response side.</p>
<p>Second, paperwork. Hospitals, universities and big energy companies often need vendor setup before they can pay you: a W-9, a certificate of insurance, sometimes a vendor portal registration. Put a “Corporate accounts” page on your site that lists what you can provide and how billing works. Admins forward that page to their accounts payable team, and you look like a vendor who’s done this before.</p>
<p>Then keep them. A standing Thursday lunch for a 30-person team is worth more than any one-off wedding over a year. After the third order, offer a standing order or a monthly menu rotation and a dedicated contact.</p>"""),

            ("ezCater and the marketplaces: what they cost and how to use them", f"""<p>ezCater is where many corporate orders start. Admins like it because it handles billing, receipts and reviews in one place, and some companies require it. You can’t ignore it, and you shouldn’t build your whole business on it either.</p>
<p>ezCater doesn’t publish a single commission rate for every caterer, and its fees depend on the services you use. One third-party estimate, from {SRC['owner']} (a company that sells a competing ordering product), puts ezCater commissions at roughly 15% to 25% per order, higher with marketing or delivery support. The same piece lists Grubhub catering marketing tiers at 5%, 15% and 20%. Ask for your current rate in writing before you sign, and run your own numbers.</p>
<!--fig:fees-->
<p>How we’d use marketplaces:</p>
<ul>
<li>Treat them as a discovery channel for new corporate clients, and price your marketplace menu so the commission doesn’t erase your margin.</li>
<li>Build ratings there. Admins sort by rating and on-time delivery, so those reviews are worth earning.</li>
<li>Make your own channel better for repeat orders: faster ordering, saved preferences, net-30 billing for approved accounts. Read your marketplace agreement on what you can and can’t say to customers you met there, then compete on service.</li>
<li>Track which clients came from where. A client who finds you on ezCater and then books a 300-person holiday party directly is a good outcome.</li>
</ul>
<p>Our {L('/blog/restaurant-direct-online-ordering-vs-delivery-apps/', 'post on direct ordering vs. delivery apps')} runs the same math for restaurants.</p>"""),

            ("Google Ads for catering: keywords, negatives and settings", f"""<p>Search is where Houston catering buyers tell you exactly what they need. Split campaigns by buyer type, because a wedding search and a boxed lunch search need different pages and convert on different timelines.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Corporate drop-off</td><td>corporate catering Houston, office lunch catering The Woodlands, boxed lunch catering near me, breakfast catering for meeting</td><td>Corporate menu with per-person prices and online ordering</td></tr>
<tr><td>Corporate events</td><td>holiday party catering Houston, company picnic catering, corporate event caterer Katy</td><td>Event packages, staffing, bar partners, quote form</td></tr>
<tr><td>Weddings</td><td>wedding catering Houston, wedding caterer The Woodlands, rehearsal dinner catering</td><td>Sample wedding menus with ranges, tasting booking</td></tr>
<tr><td>Social and family</td><td>graduation party catering, BBQ catering Spring TX, taco bar catering Cypress</td><td>Simple party packages with pickup and delivery</td></tr>
<tr><td>Brand</td><td>your business name, plus “menu” and “prices”</td><td>Homepage or menu page</td></tr>
</tbody></table></div>
<p>Negatives to add before launch: jobs, hiring, careers, salary, “catering supplies,” chafing dish, trays, rental, “how to,” recipes, DIY, “start a catering business,” license, permit, insurance (as a searcher term) and “food truck” unless you run one. Add “free” too. Then read the search terms report weekly for the first month.</p>
<p>Settings that matter: target people in or regularly in your delivery area, set ad schedules around when someone answers the phone, and add call assets and lead forms on mobile. Count only real quote requests and orders as conversions, and import booked events as offline conversions if your CRM allows it. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} explains the setup, and our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} help with the budget.</p>"""),

            ("LinkedIn for corporate catering: small budget, specific people", f"""<p>LinkedIn isn’t for weddings. It’s good for one thing caterers need: reaching the specific people who order lunch for Houston offices before they need lunch.</p>
<p>Per {SRC['li']}, the minimum daily budget is $10 for any ad format. Small budgets can work if the audience is tight. Target job titles like office manager, executive assistant, administrative assistant, HR coordinator, workplace experience manager and events coordinator, in the Houston metro, at companies with 50 or more employees. Narrow further by industry (oil and energy, hospitals and health care, engineering) when you have menus and references that fit.</p>
<p>What to say:</p>
<ul>
<li>A short video of a boxed lunch delivery being set up in a conference room.</li>
<li>A downloadable corporate menu with per-person pricing.</li>
<li>A first-order offer for new corporate accounts (a free dessert tray or delivery fee waived).</li>
</ul>
<p>Organic LinkedIn helps too. The owner posting photos of a Research Forest office breakfast setup, with the client’s permission, reaches the people who order for the office down the hall. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston energy and industrial firms')} explains how those buyers think.</p>"""),

            ("Menus and pricing pages that book events", f"""<p>The single biggest fix on most caterer websites is pricing. Couples and admins compare three caterers in one evening, and the one with no prices gets skipped.</p>
<!--fig:pricing-->
<p>What a good pricing page shows:</p>
<ul>
<li>Per-person “starting at” prices for each package, with what’s included.</li>
<li>Order minimums, delivery fees by area (inside the Loop, The Woodlands, Katy, Sugar Land), and the cutoff for orders.</li>
<li>Service charge vs. gratuity, explained in a sentence. Clients get annoyed when they think they’re tipping twice.</li>
<li>Staffing, rentals and bar service as add-ons, with ranges.</li>
<li>A downloadable PDF, plus the same menu as text on the page so Google can read it.</li>
</ul>
<p>Use “[your price]” in drafts if you’re building this page from scratch; never leave a placeholder live. A range is better than “call for pricing.”</p>"""),

            ("Tasting appointments for weddings and big events", f"""<p>For weddings and large corporate events, the tasting is the sale. Marketing’s job is to get qualified people into one.</p>
<p>Put a tasting booking link on every wedding and event page, with available dates. Some caterers charge a tasting fee and credit it to the booking, which filters out people who aren’t serious. Ask three questions before you confirm: date, guest count and venue. Then follow up within a day of the tasting with a written proposal, and again a week later.</p>
<p>Our {L('/blog/wedding-venue-marketing-houston-montgomery-county/', 'wedding venue marketing guide')} covers how couples plan, how long they take and where The Knot and WeddingWire fit. Rather than repeat it here, we’d point you there and focus on the piece caterers control: being on the venue’s list.</p>"""),

            ("Getting on venue preferred-vendor lists", f"""<p>Many Houston and Montgomery County venues give couples a short list of approved caterers, and some don’t allow anyone else. Getting on those lists can bring a steady stream of weddings and corporate events without ad spend.</p>
<!--fig:venues-->
<p>Venue coordinators recommend caterers who make their day easier. Arrive on time, follow load-in rules, clean up completely, and send the coordinator good photos from the event within a week (they need content too). Ask after your second or third event at a venue whether they keep a preferred list and what it takes to get on it.</p>
<p>Then build a page on your site for each venue you work often: “Catering at [venue name],” with photos from events there, a sample menu that fits their kitchen setup, and notes about the space. Couples search that exact phrase, and coordinators like having a link to send.</p>"""),

            ("The Houston catering calendar", f"""<p>Catering demand in Houston has a rhythm, and your marketing should move ahead of it.</p>
<!--fig:calendar-->
<ul>
<li><b>November and December.</b> Holiday parties. Corporate planners book in September and October, so start holiday party ads and LinkedIn in early September.</li>
<li><b>Rodeo season.</b> RodeoHouston runs {SRC['rodeo']}. Offices host Go Texan days and team lunches around it, and barbecue and Tex-Mex caterers can promote rodeo-themed packages in February.</li>
<li><b>Spring.</b> Weddings, galas and graduation parties. May is busy with graduations across Cy-Fair, Katy, Conroe and The Woodlands school districts.</li>
<li><b>Summer.</b> Slower for weddings in the heat, but corporate training and summer intern events continue. Indoor venues and drop-off menus do better.</li>
<li><b>Fall.</b> The second wedding peak, plus corporate kickoffs and conferences.</li>
<li><b>Hurricane season.</b> June through November. Put a weather and rescheduling policy in your contracts and on your site.</li>
</ul>
<p>Our {L('/blog/seasonal-marketing-greater-houston/', 'seasonal marketing guide for Greater Houston')} covers the broader calendar.</p>"""),

            ("Reviews and permits: the trust details", f"""<p>Reviews do more for caterers than for most restaurants, because a corporate buyer is risking their reputation on you. Ask every client for a Google review after the event, with the same link and no incentive, per {SRC['gpol']}. Ask happy corporate clients for a short written testimonial with their title and company (with permission) for your corporate page. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has templates.</p>
<p>Permits are a trust signal too. In the City of Houston, the {SRC['hhdfaq']} says anyone who sells or serves food needs a food dealer’s permit, and food prepared in an unlicensed private home is prohibited. Fees through the {SRC['hpc']} range from $224.44 to $739.44 by risk level, plus inspection fees. Outside the city, Harris County, Fort Bend County and Montgomery County and the cities within them have their own processes. Put “Licensed and inspected commercial kitchen” and your insurance coverage on your corporate page. Office managers at the Medical Center and the Energy Corridor will ask, and it’s better if they don’t have to.</p>"""),

            ("What to track, and where to start", f"""<p>Track these monthly: quote requests by source, booked events by source, average order value, repeat corporate clients and marketplace share of revenue. If marketplace share keeps climbing while direct orders stay flat, your own site needs work.</p>
<p>Where we’d start this month:</p>
<ol>
<li>Publish pricing and a corporate accounts page.</li>
<li>Set up an auto-reply and online ordering for drop-off catering.</li>
<li>Launch a small Google Ads search campaign for corporate catering in your delivery area.</li>
<li>Email five venue coordinators you’ve worked with about their preferred lists.</li>
<li>Plan your holiday party campaign for early September.</li>
</ol>
<p>If you’d like a senior strategist to build a plan around your kitchen, your capacity and your mix of corporate and wedding work, <a href="/contact/">get in touch</a>. Our {L('/services/search-marketing/', 'search marketing')} and {L('/services/web-design-seo-pr/', 'web design and SEO')} teams do most of the work above.</p>"""),
        ],
        "faq": [
            ("How do I get corporate catering clients in Houston?",
             "Make ordering easy for office managers and executive assistants: per-person prices online, online ordering for drop-off catering, labeled meals, invoice and PO billing, and a corporate accounts page with insurance and vendor paperwork. Then reach them through Google search ads, LinkedIn ads targeted by job title, and marketplaces like ezCater. Offer standing orders after the third order, since repeat corporate lunches are where caterers make steady money."),
            ("How much does ezCater charge caterers?",
             "ezCater doesn’t publish one commission rate for every caterer; fees depend on the services you use. A 2026 third-party estimate from Owner.com, which sells a competing product, put ezCater commissions at roughly 15% to 25% per order. Ask ezCater for your current rate in writing, price your marketplace menu so the commission doesn’t erase your margin, and track which clients come from the marketplace."),
            ("Should a catering company put prices on its website?",
             "Yes. Buyers compare several caterers at once and skip the ones that say call for pricing. Show starting-at per-person prices for each package, order minimums, delivery fees by area, and how service charges and gratuity work. Add staffing, rentals and bar service as add-ons with ranges. Put the menu as text on the page, not only in a PDF, so Google can read it."),
            ("Do I need a permit to run a catering business in Houston?",
             "Yes. The Houston Health Department says anyone who sells or serves food in the city needs a food dealer’s permit, and food prepared in an unlicensed private home is prohibited. Permit fees range from about $224 to $739 depending on risk level, plus inspection fees. Outside city limits, check with Harris, Fort Bend or Montgomery County and your city."),
            ("When is catering season in Houston?",
             "Holiday parties in November and December are the biggest corporate peak, and planners book in September and October. Rodeo season in late February and March brings team lunches and Go Texan events. Spring and fall are wedding peaks, and May is busy with graduation parties. Summer is slower for weddings but corporate drop-off continues. Plan campaigns six to eight weeks ahead of each peak."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "Houston’s corporate catering market",
                "stats": [["120K+", "Texas Medical Center employees"], ["10M", "TMC patient encounters a year"], ["56K+", "Energy Corridor jobs"], ["$10", "LinkedIn minimum daily budget"]],
                "note": "Sources: Texas Medical Center, Energy Corridor District, LinkedIn",
                "alt": "Stats on the Texas Medical Center and Energy Corridor workforce for catering company marketing in Houston",
                "caption": "Two districts, a lot of weekday lunches.",
            },
            "corporate": {
                "type": "checklist",
                "title": "What corporate catering buyers check",
                "sub": "Build these into your site and your process",
                "items": ["Per-person prices and minimums online", "Online ordering with a clear cutoff time", "Labeled meals for dietary needs", "PO, invoice and net-30 billing", "W-9 and certificate of insurance on request", "Delivery windows that fit early meetings", "Fast reply, even at 7 a.m.", "One named contact for repeat orders"],
                "alt": "Checklist of what corporate catering buyers in Houston, the Energy Corridor and the Medical Center look for",
                "caption": "Admins choose the caterer who makes their week easier.",
            },
            "fees": {
                "type": "bars",
                "title": "What a marketplace fee does to an $800 order",
                "sub": "Revenue kept after commission, before food and labor",
                "items": [["Direct order on your site", 800, "$800"], ["Marketplace at 15%", 680, "$680"], ["Marketplace at 25%", 600, "$600"]],
                "highlight": [0],
                "note": "Illustrative example using the 15%-25% third-party estimate. Get your actual rate in writing.",
                "alt": "Bar chart showing how catering marketplace commissions change revenue on an order for a Houston catering company",
                "caption": "Use marketplaces to find clients, and your own site to keep them.",
            },
            "pricing": {
                "type": "compare",
                "title": "Catering pricing pages",
                "left": {"title": "Pages that lose the quote", "items": ["“Call for pricing”", "Menu only in a PDF", "No minimums or delivery fees listed", "Service charge explained at invoice", "No way to book a tasting"]},
                "right": {"title": "Pages that book", "items": ["Starting-at prices per person", "Menu as text plus a PDF", "Minimums and delivery fees by area", "Service charge vs. gratuity, upfront", "Tasting link with available dates"]},
                "alt": "Comparison of weak and strong catering pricing pages for catering companies in Houston and The Woodlands",
                "caption": "A range beats no number every time.",
            },
            "venues": {
                "type": "steps",
                "title": "Getting on a venue’s preferred list",
                "steps": [["Work the room well", "On time, follow load-in rules, clean up completely."], ["Send photos within a week", "Coordinators need content, and they remember who sends it."], ["Ask after event two or three", "Does the venue keep a list, and what does it take?"], ["Build a venue page", "“Catering at [venue]” with photos and a fitting sample menu."], ["Stay in touch", "A quarterly check-in and a holiday thank-you."]],
                "alt": "Steps for a catering company to get on venue preferred vendor lists in Houston and Montgomery County",
                "caption": "Being easy to work with is the whole pitch.",
            },
            "calendar": {
                "type": "columns",
                "title": "Catering demand through the year",
                "sub": "Relative inquiry volume for a Houston caterer doing corporate and weddings",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [40, 55, 70, 80, 85, 55, 40, 45, 65, 85, 95, 100],
                "highlight": [10, 11],
                "y_label": "Relative demand",
                "note": "Illustrative example",
                "alt": "Column chart of illustrative catering demand by month for a catering company in Houston and The Woodlands",
                "caption": "Start campaigns six to eight weeks before each peak.",
            },
        },
    },
]
