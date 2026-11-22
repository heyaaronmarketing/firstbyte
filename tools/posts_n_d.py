"""Batch 14 (d): party and event rental marketing in Houston and The Woodlands (bounce houses, tents, tables,
chairs, linens), and boutique retail store marketing in The Woodlands (clothing, gift and home boutiques).

Research, party rental post: TDI amusement ride FAQ (continuous air-flow inflatables are Class B rides, $1,000,000 per
occurrence, Form AR-100, NAARSO inspectors, sticker valid one year, $40 per ride filing fee, quarterly AR-800 injury
reports, Class B misdemeanor) and TDI's consumer tips plus its public list of current stickers; CPSC 2019 release (more
than 18,000 ER-treated bounce house injuries in 2018, 12 deaths 2003-2013, 15-25 mph wind ceiling); Event Rental
Systems on GBP categories (Party equipment rental service, Tent rental service, Bounce house rental); Google's Local
Services Ads category list (no event or party rental category); Google Ads advanced location options; FOX 26 on the
2027 rodeo dates (March 2-21, 2027); Jackson Walker and National Law Review on Texas SB 140 (Sept. 1, 2025, $10,000
bond, two-year same-name exemptions, November 2025 settlement on consent-based texts).
Research, boutique post: Community Impact on Market Street and Hughes Landing openings (Draper James, Varley, Bowtique);
Visit The Woodlands on Market Street in Lights (Nov. 19 tree lighting, 70-foot tree); Google Business Profile help on
in-store products (Local Inventory app, UPC/EAN barcodes, wired scanner) and the product editor (no barcode needed);
Shopify changelog on Google local inventory sync; Shopify help on the Instagram channel (Meta catalog, Shopify checkout,
tax responsibility since Aug. 26, 2025); FTC Disclosures 101 for influencers; Morgan Lewis on the FTC consumer reviews
rule (effective Oct. 21, 2024, up to $51,744 per violation, fake followers); Google Ads help on store visit conversions
and store sales eligibility (30,000 uploaded transactions in 90 days, allowlist); NRF 2026 holiday forecast (4.2%,
$1.013 trillion, Nov. 1-Dec. 31) and 2026 back-to-school survey ($43.3 billion K-12, $250.29 on clothing, 62% started by
early July, 50% online); Texas Comptroller on the Aug. 7-9, 2026 sales tax holiday ($142.5 million, items under $100).
Not verified and left out: Shopify POS Pro pricing (page blocked), NWS lightning guidance (page blocked), Houston-area
tent permit thresholds (varies by city and county; we tell readers to ask the fire marshal).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # party rental post
    "tdi_faq": A("https://www.tdi.texas.gov/COMMERCIAL/lcamuseinfo.html", "TDI’s amusement ride FAQ"),
    "tdi_tips": A("https://tdi.texas.gov/tips/amusement-rides.html", "TDI’s consumer tips on amusement rides"),
    "tdi_list": A("https://www.tdi.texas.gov/commercial/lcamcurrentsticker.html", "TDI’s public list of current ride stickers"),
    "cpsc": A("https://www.cpsc.gov/Newsroom/News-Releases/2019/Dont-Get-Swept-Away-CPSC-Reminds-Consumers-to-Be-Grounded-in-Safety-When-Using-Bounce-Houses", "the U.S. Consumer Product Safety Commission"),
    "ers": A("https://eventrentalsystems.com/get-more-party-rental-bookings-with-a-google-business-profile/", "Event Rental Systems’ guide to Business Profiles for rental companies"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "loc": A("https://support.google.com/google-ads/answer/1722038", "Google’s advanced location options"),
    "rodeo": A("https://www.fox26houston.com/news/2027-houston-rodeo-genre-calendar-concert-lineup", "FOX 26"),
    "sb140": A("https://www.jw.com/news/insights-texas-tcpa-sb-140/", "Jackson Walker’s summary of SB 140"),
    "sb140b": A("https://natlawreview.com/article/texas-sb-140-after-november-settlement-consent-cold-texting-out", "National Law Review"),
    # boutique post
    "ci_dj": A("https://communityimpact.com/houston/the-woodlands/business/2025/12/05/draper-james-opens-at-market-street-in-the-woodlands", "Community Impact"),
    "ci_bow": A("https://communityimpact.com/the-woodlands/business/bowtique-relocates-clothing-store-to-hughes-landing-in-the-woodlands/", "moved from Market Street to Hughes Landing"),
    "msl": A("https://www.visitthewoodlands.com/events/holiday/market-street-in-lights/", "Visit The Woodlands"),
    "gbp_inv": A("https://support.google.com/business/answer/9934993?hl=en", "Google’s in-store products help page"),
    "gbp_pe": A("https://support.google.com/business/answer/9330323?hl=en", "product editor"),
    "shop_lis": A("https://changelog.shopify.com/posts/google-local-inventory-sync", "local inventory sync"),
    "shop_ig": A("https://help.shopify.com/manual/sell-online/instagram", "Shopify’s Instagram channel docs"),
    "ftc101": A("https://ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers/", "FTC’s Disclosures 101 for influencers"),
    "ftc_rev": A("https://www.morganlewis.com/pubs/2024/08/ftc-issues-final-rule-on-consumer-reviews-and-testimonials", "Morgan Lewis’s summary of the FTC reviews rule"),
    "gsv": A("https://support.google.com/google-ads/answer/6100636", "Google’s store visit conversion requirements"),
    "gss": A("https://support.google.com/google-ads/answer/15885010", "store sales measurement"),
    "nrf_h": A("https://nrf.com/media-center/press-releases/nrf-forecasts-2026-holiday-sales-growth-as-consumers-remain-resilient", "NRF’s 2026 holiday forecast"),
    "nrf_b": A("https://nrf.com/media-center/press-releases/majority-of-back-to-school-shoppers-get-a-head-start-on-the-season", "NRF’s 2026 back-to-school survey"),
    "tax": A("https://comptroller.texas.gov/about/media-center/news/20260804-texas-comptroller-don-huffines-announces-1425-million-in-expected-savings-during-texas-sales-tax-holiday-aug-7-9-1785850980791", "the Texas Comptroller"),
}

PARTY = "/blog/party-event-rental-marketing-houston-the-woodlands/"
BOUTIQUE = "/blog/boutique-retail-store-marketing-the-woodlands/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: party and event rentals
    {
        "slug": "party-event-rental-marketing-houston-the-woodlands",
        "title": "Party and Event Rental Marketing in Houston and The Woodlands",
        "seo_title": "Party Rental Marketing in Houston & The Woodlands",
        "desc": "Party and event rental marketing for Houston and The Woodlands: bounce house and tent bookings, TDI rules, online availability, Google Ads, Maps and seasons.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Facebook"],
        "art": "b2",
        "hero": "ticket",
        "hero_alt": "Illustration for party and event rental marketing in Houston and The Woodlands, covering bounce houses, tents and tables",
        "related": ["wedding-venue-marketing-houston-montgomery-county", "rank-in-google-map-pack-houston", "seasonal-marketing-greater-houston"],
        "sections": [
            (None, f"""<p>Thursday, 4:50 p.m. You have 14 deliveries on the board for Saturday, two crews, one box truck that needs a new tire, and a forecast showing a 60% chance of storms after lunch. Your phone has six missed calls. Three are customers asking what happens if it rains. Two are new people asking if the castle combo is “still available Saturday.” One is a church in Spring wanting a quote for a fall festival.</p>
<p>Meanwhile, in a Facebook group for moms in Cypress, someone has posted “anyone know a bounce house place that has something for this Saturday??” and 31 people have answered. Your competitor got tagged nine times. You got tagged once, by your cousin.</p>
<p>That’s party rental marketing in one afternoon. Demand is spiky, last-minute and weather-dependent. The company that wins is the one whose availability, prices and rain policy are easiest to see at 10 p.m. on a phone, and whose name keeps coming up when locals ask each other.</p>
<p>To get more bookings for a party or event rental business in Houston and The Woodlands, put live availability and real prices online, show your Texas inflatable compliance up front, win the Google Maps results for your delivery area, and run search ads only on “rental” intent with tight negatives. Then build the repeat side: schools, churches, HOAs and companies that book the same event every year. Below is how we’d set that up, with the settings and the math.</p>"""),

            ("How Houston families and event planners actually book rentals", f"""<p>Almost nobody plans a birthday party three months out. In accounts we’ve looked at, the bulk of residential bounce house bookings land in the two weeks before the date, and a surprising number land in the last 72 hours. Corporate and school events book further ahead, often four to ten weeks.</p>
<p>The residential customer is usually a parent on a phone. Their search goes something like “bounce house rental near me,” then “water slide rental Spring TX,” then a look at the Maps results, then two or three websites. If they can’t see a price and a calendar within about 30 seconds, they hit back. They also ask friends, which in Houston mostly means neighborhood Facebook groups and Nextdoor.</p>
<p>The planner (a PTO volunteer, an HOA social chair, an office manager in the Energy Corridor) needs a certificate of insurance, a W-9, an invoice the district can pay and someone who answers email. They’ll pay more for that, and they come back every year if you don’t blow it.</p>
<p>So you’re running two businesses with one inventory, and the marketing has to serve both.</p>"""),

            ("Texas inflatable rules, and why they belong in your marketing", f"""<p>Bounce houses and inflatable slides are amusement rides under Texas law. Per {SRC['tdi_faq']}, continuous air-flow inflatables are Class B rides that need liability insurance of at least $1,000,000 per occurrence, an inspection by a qualified inspector (TDI doesn’t inspect rides itself), and a Form AR-100 certificate. Once the paperwork is filed with TDI and the $40-per-ride fee is paid, each unit gets a compliance sticker that’s good for one year from the inspection and has to be visible to riders. Owners also file quarterly injury reports. Operating without meeting the requirements is a Class B misdemeanor.</p>
<!--fig:tdi-->
<p>Most operators treat this as overhead. We think it’s one of the best selling points you have, because the state is literally telling your customers to ask. {SRC['tdi_tips']} advise renters to check for a current compliance sticker, look the company up, ask about injury history and ask whether the owner will set the ride up and supervise it. And TDI publishes {SRC['tdi_list']}, searchable by operator and ride name.</p>
<p>The safety numbers give parents reason to care. {SRC['cpsc']} estimated more than 18,000 emergency room-treated bounce house injuries in 2018 and counted 12 deaths from 2003 to 2013.</p>
<p>So answer the questions before anyone asks them:</p>
<ul>
<li>Put a “Texas compliance” section on every inflatable’s product page, with its sticker number and expiration date.</li>
<li>Build one “Safety and insurance” page that explains the TDI requirements in plain English and links to TDI’s list.</li>
<li>Keep a sample certificate of insurance ready to send, and say on the page that you’ll add a school, church, HOA or venue as additional insured.</li>
<li>Show your setup crew in uniform, staking a unit in a real backyard. Photos of anchoring do more than a paragraph about it.</li>
</ul>
<p>Plenty of people rent out one bounce house from a garage without any of this. Make your compliance visible enough that the difference is obvious.</p>"""),

            ("Online booking with live availability: the website that books Saturdays", f"""<p>A rental website has one job: pick a date, see what’s available, see the total, pay a deposit.</p>
<p>Rental software like Event Rental Systems, InflatableOffice, Goodshuffle Pro or TapGoods will handle availability, deposits, delivery fees and contracts. Pick one and plug it into the site properly, so the calendar sits on the product pages rather than behind a “Request a quote” form that a human answers on Monday.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Page</th><th>What the customer is asking</th><th>What it must show</th></tr></thead>
<tbody>
<tr><td>Product page (one per unit)</td><td>“Is this one free Saturday, and what does it cost?”</td><td>Photos of the actual unit set up, dimensions and space needed, power needs, age range, price, live date picker, TDI sticker number</td></tr>
<tr><td>Category pages</td><td>“Show me water slides” / “Show me 20x40 tents”</td><td>Filter by date first, then by size or price, with “available” badges</td></tr>
<tr><td>Packages</td><td>“What do I need for 60 people?”</td><td>Bundles like tent + 8 tables + 64 chairs + linens, priced as a set</td></tr>
<tr><td>Delivery area pages</td><td>“Do you deliver to Magnolia?”</td><td>Towns served, delivery fee by zone, setup surface rules (grass, concrete, turf)</td></tr>
<tr><td>Weather policy</td><td>“What if it rains?”</td><td>Who decides, by what time, and what the customer gets back (more below)</td></tr>
<tr><td>Schools, churches and HOAs</td><td>“Can you invoice us and send a COI?”</td><td>W-9, sample COI, net terms if you offer them, past event types, a contact who answers email</td></tr>
</tbody></table></div>
<!--fig:product-->
<p>Delivery fees deserve a note. A flat fee that works for The Woodlands and Shenandoah will lose money in Katy on a Saturday morning. Price by zone (rings out from your warehouse, or by town) and put the zones on the page.</p>
<p>Our {L('/services/web-design-seo-pr/', 'web design team')} builds these sites, and the {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} covers the delivery-area pages in more depth.</p>"""),

            ("Google Business Profile and Maps for a rental company in The Woodlands, Katy or Pearland", f"""<p>Most rental companies are service-area businesses. You deliver to the customer, so you’ll usually hide your warehouse address and list the cities you serve instead. Per {SRC['ers']}, “Party equipment rental service” makes sense as the primary category, with “Tent rental service” and “Bounce house rental” as secondary options where they fit. Avoid sitting only in a generic “rental” category.</p>
<p>Some practical points for a Houston operator:</p>
<ul>
<li>List the towns you really deliver to (The Woodlands, Spring, Conroe, Tomball, Magnolia, Cypress, Kingwood). Ranking still leans on where Google thinks you’re based, so a warehouse in Conroe will struggle to rank in Pearland. Pick the area where you’re based to fight hardest.</li>
<li>Add every service you offer, in plain English, with a starting price: “Water slide rental, from $289, delivery and setup included in The Woodlands.”</li>
<li>Upload setup photos every week in season. A unit in a real Spring backyard with the date and the neighborhood in the caption beats a manufacturer’s stock photo.</li>
<li>Use the booking link field to send people straight to your availability calendar.</li>
</ul>
<p>Don’t wait for Local Services Ads. {SRC['lsa']} has no party, event or tent rental category, so regular search ads and the map pack are where you compete. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the full setup.</p>
<p>Reviews win the map and the click. Text a review link the evening after pickup, when the parent is still riding the good-party feeling. Something like: “Thanks for having us out for Mia’s party! If the crew did a good job, a quick Google review helps a small Houston company a lot: [link].” Same link to every customer, no discounts for reviews, no filtering out the unhappy ones. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("Google Ads for party rentals: keywords, negatives and settings", f"""<p>Search ads work well for rentals because the intent is right there in the query. The trick is that “bounce house” on its own mostly means people buying one, and “party” on its own means almost anything.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Send traffic to</th></tr></thead>
<tbody>
<tr><td>Bounce houses</td><td>bounce house rental near me, bounce house rental The Woodlands, moonwalk rental Spring TX</td><td>Inflatables category, filtered by date</td></tr>
<tr><td>Water slides</td><td>water slide rental Houston, inflatable water slide rental Cypress</td><td>Water slide category (run May to September)</td></tr>
<tr><td>Tents</td><td>tent rental Houston, 20x40 tent rental, party tent rental Conroe</td><td>Tents with size guide and package pricing</td></tr>
<tr><td>Tables and chairs</td><td>table and chair rentals near me, chair rental Katy</td><td>Packages page</td></tr>
<tr><td>Corporate and school</td><td>company picnic rentals Houston, school carnival rentals, fall festival rentals</td><td>Schools, churches and HOAs page</td></tr>
</tbody></table></div>
<!--fig:negatives-->
<p>A few settings matter more than the rest. Under {SRC['loc']}, choose “Presence: People in or regularly in your included locations,” so you’re not paying for clicks from people who are merely interested in Houston. Draw your locations around the delivery zones you actually serve. Schedule ads to run late in the evening, because that’s when parents plan parties, and keep running them on Friday nights in season if you have last-minute inventory. Track booked deposits as the main conversion, with calls as a secondary one. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'call and form tracking guide')} walks through the setup.</p>
<p>Sample ad copy that’s worked in the format we’d use:</p>
<ul>
<li>Headline: “Bounce House Rentals, The Woodlands” / “See Saturday Availability” / “TDI-Inspected and Insured”</li>
<li>Description: “Live calendar, delivery and setup included in our zone. Rain policy posted. Book with a deposit online.”</li>
</ul>
<p>For click costs, see our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')}. Rental clicks tend to be cheaper than home services, but the profit per booking is smaller too, so the margin for waste is thin. Our {L('/services/search-marketing/', 'search marketing team')} runs these campaigns if you don’t want to live in the search terms report.</p>"""),

            ("Facebook groups, Nextdoor and Meta ads", f"""<p>The neighborhood Facebook group is the biggest referral network in suburban Houston. You can’t buy your way into it, and most groups ban business posts outside a weekly promo thread. What you can do:</p>
<ul>
<li>Post in the allowed promo threads every week with one photo and one sentence about open dates. “Still have the tropical slide open for Saturday the 14th, Spring and The Woodlands delivery.” Short and specific gets tagged.</li>
<li>Answer from your business page or your own profile with a straight answer and a link to the calendar, never a copy-paste sales pitch.</li>
</ul>
<p>Nextdoor works similarly; our {L('/blog/is-nextdoor-advertising-worth-it/', 'Nextdoor advertising review')} covers whether the paid side is worth it.</p>
<p>Meta ads work best for rentals as a reminder and a seasonal push. Party rentals aren’t a special ad category, so you can target by age, location and interests. Good uses:</p>
<ul>
<li>Retarget website visitors who looked at a date but didn’t book, with the unit they viewed.</li>
<li>Push water slides in May, before the first hot weekend, and tents and heaters in October for church and school fall events.</li>
<li>Run short phone videos of a setup from arrival to inflated. Twenty seconds, real yard, captions on.</li>
</ul>
<p>We’d keep Meta to 20% to 30% of a small rental budget, with search doing the heavy lifting. If you want it run for you, that’s our {L('/services/paid-social-advertising/', 'paid social service')}.</p>"""),

            ("The Greater Houston rental calendar", f"""<p>In Houston, summer is busy for water slides and slow for everything else. Spring and fall are where the money is.</p>
<!--fig:season-->
<ul>
<li><b>Spring (March to May).</b> Birthday parties come back, schools run carnivals and field days, and churches do Easter events. The Houston Livestock Show and Rodeo runs March 2 to 21 in 2027, per {SRC['rodeo']}, and rodeo-themed parties and school “go Texan” events book around it.</li>
<li><b>Graduation (late May to June).</b> Tents, tables, chairs and linens for backyard grad parties. These book earlier than birthdays, often as soon as the ceremony date is posted.</li>
<li><b>Summer (June to August).</b> Water slides and dunk tanks. Afternoon heat and storms cut into dry units. Hurricane season starts June 1, so keep a cancellation script ready.</li>
<li><b>Fall (September to November).</b> HOA fall festivals, church trunk-or-treats, school carnivals and corporate picnics once the heat breaks. This is the best B2B window of the year.</li>
<li><b>Holidays (December).</b> Company parties and tents with sidewalls and heaters.</li>
</ul>
<p>Shift budget with the calendar. A flat monthly ad budget means overspending in August and running out in October. Our {L('/blog/seasonal-marketing-greater-houston/', 'seasonal marketing guide for Greater Houston')} has a month-by-month version for other local businesses.</p>"""),

            ("Schools, churches, HOAs and corporate events: the repeat business", f"""<p>A birthday party is a one-time sale with a maybe on next year. A school carnival is often the same date, the same units and the same PTO every year, as long as you don’t give them a reason to switch.</p>
<!--fig:b2b-->
<p>A few things we’d build specifically for these buyers:</p>
<ul>
<li>An “event planner packet” PDF: W-9, sample certificate of insurance, TDI compliance for each unit, attendant pricing, power and space requirements, and a photo of a past school or church setup.</li>
<li>A simple list of every school, church, HOA and large employer inside your delivery area, with the event they run and the month. Between The Woodlands’ villages and the master-planned subdivisions in Spring, Cypress and Katy, that list gets long fast.</li>
<li>A once-a-year email in July to every past B2B customer: “Your fall festival was October 18 last year. Want us to hold the same units for this year?” This one email outperforms most ad campaigns we’ve seen for rental businesses.</li>
</ul>
<p>Corporate customers want on-time setup before employees arrive and invoicing their accounts payable team accepts. Say so on the page.</p>"""),

            ("Rain and wind policies as marketing", f"""<p>Houston weather is the single biggest source of stress for your customers and your crews. Most rental companies hide the policy in the contract. We’d put it on the homepage.</p>
<p>Safety first. {SRC['cpsc']} advises against using bounce houses in windy conditions, with a ceiling around 15 to 25 mph depending on the unit, and says that if treetops are swaying, it’s probably too windy. The manufacturer’s manual sets each unit’s limit, and your crew needs the authority to say no.</p>
<!--fig:rain-->
<p>A clear policy answers three questions. Who makes the call, and by when? (“We’ll text you by 7 a.m. on event day, or you can call it by then.”) What does the customer get back? (A full credit to rebook within 12 months, a refund minus the deposit, or a refund in full if we cancel.) What happens if weather turns mid-party? (Crew comes back, deflates, and the customer gets a partial credit.)</p>
<p>Then use it. “Rain policy posted, decide by 7 a.m.” in your ads and on your Business Profile is a reason to pick you on a Thursday with a 60% storm forecast. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the follow-up side, which matters on those Thursdays more than any other day.</p>"""),

            ("Texts, reminders and Texas SB 140", f"""<p>Text messages run this business: confirmations, delivery windows, weather calls, review requests. Those are transactional messages about an order the customer placed. Marketing texts (“Book your fall festival now, 10% off!”) are a different category and need clear opt-in.</p>
<p>Texas expanded its telephone solicitation law to cover marketing texts through SB 140, effective September 1, 2025. It can require registration with the Secretary of State and a $10,000 bond, and violations tie back to the Texas Deceptive Trade Practices Act, per {SRC['sb140b']}. There are exemptions, including one for businesses that only solicit current or former customers and have operated under the same name for at least two years, per {SRC['sb140']}. The same article notes a November 2025 settlement under which consent-based marketing texts are treated as exempt, though it isn’t binding on courts. A warehouse-based rental company probably won’t fit the retail exemption, so ask your attorney before starting promotional texts. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} goes further.</p>"""),

            ("Cost per booking: the number to run the business on", f"""<p>Cost per click and cost per lead flatter bad campaigns. The number that matters is cost per booked deposit, by channel, next to the average order value of those bookings.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Monthly spend</th><th>Booked deposits</th><th>Cost per booking</th><th>Average order</th></tr></thead>
<tbody>
<tr><td>Google Ads (search)</td><td>$1,800</td><td>48</td><td>$38</td><td>$340</td></tr>
<tr><td>Meta ads (retargeting and seasonal)</td><td>$600</td><td>11</td><td>$55</td><td>$290</td></tr>
<tr><td>Google Maps (organic, time spent)</td><td>$400</td><td>35</td><td>$11</td><td>$310</td></tr>
<tr><td>B2B email and outreach</td><td>$150</td><td>9</td><td>$17</td><td>$1,150</td></tr>
</tbody></table></div>
<p>That table is an illustrative example for a mid-size operator in spring, not a benchmark. The pattern is common, though: Maps and B2B follow-up cost the least per booking and get the least attention, while paid search fills gaps on specific dates.</p>
<p>A first 90 days we’d run for a rental company starting from scratch:</p>
<ol>
<li><b>Month one.</b> Fix the website: live availability on every product page, delivery zones, rain policy, TDI compliance section. Clean up the Business Profile and start the review texts.</li>
<li><b>Month two.</b> Launch search campaigns by category with the negatives above, tracked to deposits. Build the B2B list and the planner packet.</li>
<li><b>Month three.</b> Add Meta retargeting and a seasonal push timed six weeks ahead of the next peak. Send the July or January email to past B2B customers.</li>
</ol>
<p>If you’d like a senior strategist to build that plan around your inventory, delivery area and season, <a href="/contact/">get in touch</a> and tell us what you rent.</p>"""),
        ],
        "faq": [
            ("How do I get more bounce house rental bookings in Houston?",
             "Put live availability and prices on every product page so parents can book a deposit at night on a phone. Then win Google Maps for your delivery area with the right categories, weekly setup photos and steady reviews. Add search ads on rental keywords like bounce house rental near me with negatives for buying and DIY searches, and post open dates in neighborhood Facebook group promo threads."),
            ("Do bounce houses need to be inspected and insured in Texas?",
             "Yes. The Texas Department of Insurance treats continuous air-flow inflatables as amusement rides. Each needs an inspection by a qualified inspector, liability insurance of at least $1,000,000 per occurrence, a filed Form AR-100 and a compliance sticker that is valid for one year and visible to riders. Operating without meeting these requirements is a Class B misdemeanor. TDI publishes a list of current stickers."),
            ("Can party rental companies use Google Local Services Ads?",
             "Not currently. Google’s Local Services Ads category list does not include party rental, event rental, tent rental or bounce house categories. Rental companies in Houston and The Woodlands compete through regular Google search ads and the Google Maps results instead, which makes a complete Business Profile, accurate service areas and a steady flow of reviews especially important."),
            ("What should a party rental rain policy include?",
             "Say who makes the weather call and by what time on event day, what the customer gets back (a credit to rebook, a partial refund or a full refund if you cancel), and what happens if weather turns mid-event. CPSC advises against bounce house use in winds above roughly 15 to 25 mph. Post the policy on your site, Business Profile and ads, since it reassures customers during storm forecasts."),
            ("How much should a party rental company spend on Google Ads?",
             "Many small and mid-size operators in Houston start somewhere between $1,000 and $3,000 a month in peak season and less in slow months, but the right number depends on inventory, margins and delivery area. Track every booked deposit back to its source and judge campaigns by cost per booking against average order value. Shift budget toward spring and fall peaks rather than spending evenly."),
        ],
        "figures": {
            "tdi": {
                "type": "stats",
                "title": "Texas inflatable rules at a glance",
                "stats": [["$1M", "liability per occurrence, per TDI"], ["1 year", "life of a compliance sticker"], ["$40", "TDI filing fee per ride"], ["18,000+", "ER-treated bounce house injuries, 2018"]],
                "note": "Sources: Texas Department of Insurance, U.S. CPSC",
                "alt": "Stats on Texas TDI inflatable amusement ride insurance and inspection rules for party rental companies in Houston and The Woodlands",
                "caption": f"From {SRC['tdi_faq']} and {SRC['cpsc']}.",
            },
            "product": {
                "type": "checklist",
                "title": "What every rental product page needs",
                "sub": "Bounce houses, slides, tents and packages",
                "items": ["Photos of this unit set up in a real yard", "Dimensions plus the space and clearance needed", "Power needs and blower count", "Age range and rider limit", "Price, delivery zone fee and deposit", "Live date picker with availability", "TDI sticker number and expiration date", "Link to the rain and wind policy"],
                "alt": "Checklist for party rental product pages in Houston and The Woodlands with availability, pricing and TDI compliance",
                "caption": "If a parent has to call to learn any of these, a competitor’s calendar gets the booking.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for rental ads",
                "sub": "Add these before launch, then read search terms weekly",
                "items": ["Buyers: buy, for sale, price of, wholesale, commercial grade", "Retail: walmart, amazon, costco, target", "DIY: how to, diy, homemade, patch, repair", "Used: used, craigslist, marketplace", "Jobs: jobs, hiring, salary, driver", "Car rentals: car, truck, u-haul, uhaul", "Venues: party venue, hall rental (unless you want them)", "Free: free, giveaway"],
                "alt": "Checklist of negative keywords for party and event rental Google Ads in Houston and The Woodlands",
                "caption": "“Bounce house” without “rental” is mostly shoppers buying one for the backyard.",
            },
            "season": {
                "type": "columns",
                "title": "Rental demand through a Houston year",
                "sub": "Relative booking volume by month for a mixed inventory",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [25, 35, 70, 95, 100, 75, 55, 40, 55, 100, 70, 50],
                "highlight": [3, 4, 9],
                "y_label": "Relative demand",
                "note": "Illustrative example",
                "alt": "Column chart of seasonal party and event rental demand in Houston and The Woodlands, peaking in spring and October",
                "caption": "Spring and October usually carry the year. Plan ad budget and crews around the peaks.",
            },
            "b2b": {
                "type": "steps",
                "title": "Winning repeat school, church and HOA events",
                "sub": "A yearly loop for event planners",
                "steps": [["Build the list", "Schools, churches, HOAs and employers in your zones."], ["Send the packet", "W-9, COI, TDI compliance, past setups."], ["Deliver early", "Set up before the volunteers arrive."], ["Follow up", "Thank-you note and a review request."], ["Rebook", "Email in July: same date, same units?"]],
                "alt": "Five steps for party rental companies to win repeat school, church and HOA events in Houston and The Woodlands",
                "caption": "Step five is where most of the profit is, and it costs one email.",
            },
            "rain": {
                "type": "compare",
                "title": "Weather policy: vague vs. clear",
                "left": {"title": "Policy that loses bookings", "items": ["Buried on page 3 of the contract", "“Weather cancellations at our discretion”", "No decision time", "Deposit lost, no credit", "Customer learns policy when it rains"]},
                "right": {"title": "Policy that wins bookings", "items": ["On the homepage and in ads", "Wind and lightning limits stated", "Decision by 7 a.m. by text", "Credit to rebook within 12 months", "Same message in every confirmation"]},
                "alt": "Comparison of vague and clear rain and wind policies for party rental companies in Houston and The Woodlands",
                "caption": "The clear policy costs you almost nothing and wins the Thursday-before-a-storm bookings.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: boutique retail
    {
        "slug": "boutique-retail-store-marketing-the-woodlands",
        "title": "Boutique Retail Store Marketing in The Woodlands: Foot Traffic, Instagram and the Holidays",
        "seo_title": "Boutique Retail Marketing in The Woodlands, TX",
        "desc": "Boutique marketing in The Woodlands and Houston: Instagram and TikTok, Google local inventory, Shopify POS, trunk shows, creators, SMS rules and holidays.",
        "category": "Strategy",
        "icons": ["Instagram", "TikTok", "Google Business Profile"],
        "art": "b4",
        "hero": "cart",
        "hero_alt": "Illustration of a shopping cart for boutique retail store marketing in The Woodlands and Houston",
        "related": ["holiday-marketing-checklist", "ftc-rules-influencer-partnerships", "sms-marketing-small-business-texas-rules"],
        "sections": [
            (None, f"""<p>Saturday, 1:15 p.m., a boutique a few blocks from Market Street. A woman walks in holding her phone up. On the screen is the Reel you posted Tuesday: the rust-colored midi dress, the one your assistant modeled by the window. “Do you still have this in a medium?”</p>
<p>You sold the last medium Wednesday. You have a small and a large. She says thanks, she’ll “look online,” and walks out. You know exactly where she’s going to look.</p>
<p>That moment has most of boutique marketing in it. Your content worked. It got a stranger to drive to your store. What broke was everything around it: no way to see stock, no way to reserve, no way to follow up with her later when the medium came back in.</p>
<p>To market a boutique retail store in The Woodlands, make your inventory visible where people search (Instagram, TikTok and Google), connect your register and website so stock is accurate in both, and give people reasons to come in that a website can’t match: fit help, events, gift wrap, a person who remembers them. Then build an email and text list you own, legally, and measure what your ads do to foot traffic with methods a single store can actually use. Below is how we’d set that up.</p>"""),

            ("Foot traffic vs. online: what a Woodlands boutique is really selling", f"""<p>The Woodlands is a hard place to be a small shop and a good one. Market Street keeps adding national brands; {SRC['ci_dj']} reported Draper James opening there in late 2025, with Varley announced for early 2026. The Woodlands Mall, Hughes Landing and Waterway Square pull from the same shoppers. Local boutiques move around inside that mix too; Bowtique {SRC['ci_bow']} in 2023.</p>
<p>You won’t beat those chains on selection or ad budget. You don’t need to. A boutique wins on things a national store can’t do well:</p>
<!--fig:vs-->
<p>Your online presence mostly exists to start in-store visits and to keep you in front of people between visits. Some boutiques do real online volume, and if you’re one of them, great. For most, the website and Instagram are the shop window, and the sale happens at the counter. That changes how you judge everything. A Reel with 900 views that sends six people in the door beat a Reel with 40,000 views from a different state.</p>"""),

            ("Instagram and TikTok product content that brings people in", f"""<p>The boutiques we see doing well on social post like a person, not a catalog. The owner or a regular staff member is on camera, talking about why they bought a piece, how it fits and what to wear it with. That’s the part a chain can’t copy.</p>
<!--fig:content-->
<p>Some specifics that tend to work:</p>
<ul>
<li><b>Try-ons on more than one body.</b> If you carry XS to XL, show XS to XL. Fit is the main reason people buy in a store, so lean on it.</li>
<li><b>Say the size runs and the price on screen.</b> “Runs small, size up. $68.” People who can afford it come in; people who can’t don’t waste your Saturday.</li>
<li><b>Name the place.</b> “New at the shop on Woodlands Parkway” or “five minutes from Market Street.” It tells the viewer you’re a real place they can drive to.</li>
<li><b>Post stock updates as Stories.</b> “Two mediums left in the rust dress” creates urgency that’s honest.</li>
<li><b>Hook in the first second.</b> On TikTok especially, open on the outfit, not on a logo or a slow pan of the store.</li>
</ul>
<p>Product tagging on Instagram is worth setting up if you’re on Shopify. Per {SRC['shop_ig']}, products need to be in both your Meta catalog and your Shopify online store to be tagged, Instagram Shopping now sends buyers to your Shopify checkout, and since August 26, 2025 you’re responsible for the sales tax setup on those orders. Product stickers only work on image Stories, not video.</p>
<p>Whether you spend more time on Instagram or TikTok depends on who buys from you. In the retail accounts we’ve seen, stores selling to women 30 to 55 in The Woodlands and Spring still get more from Instagram and Facebook, while a younger store selling to Conroe and Tomball high school and college shoppers may get more from TikTok. Our {L('/blog/facebook-vs-instagram-vs-tiktok-local-business/', 'platform comparison for local businesses')} goes through the trade-offs.</p>"""),

            ("Google Business Profile, products and local inventory", f"""<p>When someone searches “boutiques in The Woodlands” or “women’s clothing store near me,” Google shows the map pack first. A boutique’s Business Profile should look as good as its front window: real photos of the store and racks, accurate hours (including holiday hours, which most stores forget), and products.</p>
<p>There are three ways to get products onto Google, and boutiques often pick the wrong one.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Option</th><th>How it works</th><th>Fits a boutique when</th><th>Catch</th></tr></thead>
<tbody>
<tr><td>Product editor in Business Profile</td><td>Upload photos, name, price and a link by hand</td><td>You have no barcodes or online store</td><td>Manual. Shows on your profile, without live stock</td></tr>
<tr><td>Local Inventory app (POS integration)</td><td>Syncs from POS systems like Clover, Square and Lightspeed</td><td>Your products carry manufacturer UPC or EAN barcodes</td><td>Needs a wired barcode scanner or compatible POS; store-label items won’t match</td></tr>
<tr><td>Shopify Google channel with local inventory</td><td>Shopify sends products and store-level stock to Merchant Center</td><td>You run Shopify POS and the Shopify online store</td><td>Merchant Center setup and product data have to be clean</td></tr>
</tbody></table></div>
<p>The barcode issue catches a lot of small shops. {SRC['gbp_inv']} says the automatic in-store product feature needs products with manufacturer barcodes, and items with only your own labels won’t match its database. Many boutique pieces come from small designers or markets and carry no UPC at all. For those, Google’s {SRC['gbp_pe']} exists specifically for sellers without barcodes or stock data.</p>
<p>If you’re on Shopify, its Google channel has offered {SRC['shop_lis']} since 2022, linking store locations and stock counts so products can show in Search, Maps, Shopping and local inventory ads. That’s the setup we’d aim for, because it’s the one that would have told Saturday’s customer the medium was gone, or that it was back. Our {L('/blog/google-shopping-ads-shopify-setup-guide/', 'Shopify Google Shopping setup guide')} covers Merchant Center in detail.</p>"""),

            ("Shopify POS and the online store: one inventory, one customer list", f"""<p>Most boutique headaches come from running the register and the website as two separate businesses. Stock goes out of sync, the website sells a piece that left the store an hour ago, and the email list only includes online buyers.</p>
<!--fig:flow-->
<p>If you’re on Shopify POS with the Shopify online store, use what’s already there:</p>
<ul>
<li>Turn on local pickup so online buyers in The Woodlands, Spring and Conroe can collect same day. It’s also a reason for them to walk past the new arrivals.</li>
<li>Ask for an email or phone number at checkout, every time, with a reason: “so we can text you when your size comes back in.” That’s a far better pitch than “join our list.”</li>
<li>Use the customer profile. Note sizes, favorite brands and what they bought. A text that says “your size in the new Free People arrived” sells clothes. A blast that says “NEW ARRIVALS!!” mostly gets muted.</li>
<li>Use a “hold for me” or reserve option for social traffic. Even a simple form that sends a DM-style request to staff saves the sale.</li>
</ul>
<p>If you’re not on Shopify, the same logic applies to Lightspeed, Square or Clover: one system of record for stock and customers.</p>"""),

            ("Events, trunk shows and the Market Street calendar", f"""<p>Events are where a boutique beats Amazon outright. Nobody drives to a warehouse for a glass of wine and a jewelry designer’s trunk show.</p>
<p>The ones we’d run:</p>
<ul>
<li><b>Trunk shows</b> with a designer or a brand rep, ideally with pieces you don’t carry every day. Ask the brand to share it with their own followers.</li>
<li><b>Private shopping nights</b> for your top 50 customers. A list in your POS sorted by last-12-month spend makes this a ten-minute job.</li>
<li><b>Styling nights</b> co-hosted with a nearby salon, lash studio or med spa. Each side brings its list.</li>
<li><b>Holiday calendar tie-ins.</b> Market Street’s 70-foot tree lighting ran November 19 this year, per {SRC['msl']}, and the area fills with holiday shoppers through December. Plan late-hours events on those nights, and on Small Business Saturday, the Saturday after Thanksgiving.</li>
</ul>
<p>Promote every event three ways: an Instagram post and Stories countdown, an email and (with consent) a text to your list, and an in-store sign two weeks ahead. Then collect emails at the door. An event that adds 40 new names to your list paid for itself even if the night’s sales were flat.</p>"""),

            ("Creator and influencer partnerships, with FTC disclosure", f"""<p>The creators who move product for a Woodlands boutique usually aren’t the ones with 500,000 followers. They’re local moms, teachers and fitness instructors with 3,000 to 30,000 followers who mostly live in Montgomery County and northwest Harris County. Our posts on {L('/blog/micro-influencers-vs-big-names/', 'micro-influencers vs. big names')} and {L('/blog/find-the-right-influencers/', 'finding the right influencers')} go deeper on choosing them.</p>
<p>Gifting a dress is a material connection, and so is a store credit or a discount. Per the {SRC['ftc101']}, creators have to disclose any financial, employment, personal or family relationship with a brand. The disclosure goes in the post itself (a bio mention or a line hidden behind “more” isn’t enough), and in videos it belongs in the video (spoken and on screen is best). “Ad,” “advertisement” and “sponsored” work; “collab,” “sp” or a lone “thanks” don’t. The FTC also says not to rely on a platform’s built-in disclosure tool alone.</p>
<!--fig:ftc-->
<p>Don’t try to shortcut social proof either. The FTC’s rule on reviews and testimonials took effect October 21, 2024, and bans fake reviews, buying reviews conditioned on a positive sentiment, undisclosed insider reviews and buying fake followers or likes, with penalties of up to $51,744 per violation, per {SRC['ftc_rev']}. Our {L('/blog/ftc-rules-influencer-partnerships/', 'FTC rules for influencer partnerships')} post has contract language you can borrow.</p>
<p>Put the deal in writing even when it’s a friend: what you’re giving, what they post and when, the disclosure wording, and whether you can reuse the content in ads.</p>"""),

            ("Email and SMS lists, and Texas SB 140", f"""<p>Instagram can change its feed tomorrow. Your list can’t be taken away. For a boutique, a healthy list is the difference between a slow Tuesday and a sold-out restock.</p>
<p>Texts are powerful and regulated. Texas SB 140, effective September 1, 2025, brought marketing texts under the state’s telephone solicitation law. Covered sellers can need to register with the Secretary of State and post a $10,000 bond, and violations link to the Texas Deceptive Trade Practices Act, per {SRC['sb140b']}. Retailers get a few possible exemptions. Per {SRC['sb140']}, one covers businesses with a physical location operating under the same name for at least two years where most sales happen at that location; another covers businesses that only solicit current or former customers after two years under the same name. A November 2025 settlement treats consent-based marketing texts as exempt, though National Law Review notes it isn’t binding on courts.</p>
<p>A store-based boutique that’s been open a couple of years may well fit an exemption. A newer shop, or one doing most sales online, may not. Either way, federal consent rules still apply, so:</p>
<ul>
<li>Collect texting consent separately from email, with clear wording at the register or on the site.</li>
<li>Keep records of when and how each person opted in.</li>
<li>Honor STOP immediately and keep sends to reasonable hours.</li>
<li>Ask your attorney which exemption, if any, fits your store before you launch.</li>
</ul>
<p>We cover the rules in more depth in our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS marketing rules post')}, and automated flows (welcome, back-in-stock, post-purchase) in {L('/blog/ecommerce-email-sms-flows-klaviyo/', 'our email and SMS flows guide')}.</p>"""),

            ("Holiday and back-to-school: the two seasons that make the year", f"""<p>For most gift and clothing boutiques, November and December carry the year. NRF forecast 2026 holiday sales growth of 4.2%, to $1.013 trillion for November and December, per {SRC['nrf_h']}.</p>
<!--fig:seasons-->
<p>Back-to-school matters more for boutiques in The Woodlands than people think, especially stores selling to teens and to moms buying for themselves at the same time. {SRC['nrf_b']} put K-12 spending at a record $43.3 billion, with families planning $250.29 on clothing, 62% already shopping by early July and 50% planning to shop online. Texas’s sales tax holiday ran August 7 to 9 in 2026, exempting most clothing, footwear, school supplies and backpacks under $100, with $142.5 million in expected savings, per {SRC['tax']}. Promote that weekend early, and make sure your POS is set up to apply the exemption.</p>
<!--fig:calendar-->
<p>Planning tips for both seasons:</p>
<ul>
<li>Start holiday content and ads in early November, not the week of Thanksgiving. Gift guides by price (“under $50,” “for her,” “hostess gifts”) do well in both Reels and email.</li>
<li>Publish holiday hours on Google, Instagram and your site the same day.</li>
<li>Offer free gift wrap and same-day local pickup through December 23. Those two lines beat most discounts.</li>
<li>For back-to-school, run a “mom and daughter” event on the tax-free weekend and push it two weeks out.</li>
</ul>
<p>Our {L('/blog/holiday-marketing-checklist/', 'holiday marketing checklist')} and {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing guide for The Woodlands')} have the full calendars.</p>"""),

            ("Competing with Amazon and the national chains", f"""<p>The shopper who leaves your store to “look online” isn’t disloyal. She’s busy. You win her back by removing the reasons she left.</p>
<ul>
<li><b>Stock visibility.</b> Local inventory on Google and accurate online stock mean she can check before she drives.</li>
<li><b>Reserve and hold.</b> Let her hold a size for 24 hours from a DM or a website button.</li>
<li><b>Back-in-stock texts.</b> The rust dress medium comes back Thursday; she hears about it Thursday.</li>
<li><b>Local delivery.</b> Same-day delivery inside The Woodlands, Shenandoah and Spring on orders over a threshold is something Amazon does too, but not with a handwritten note.</li>
<li><b>Easy returns and alterations.</b> Say what your policy is in plain words, on the site and at the counter.</li>
</ul>
<p>Local search can tilt in your favor too. Google ranks local results on relevance, distance and prominence, and reviews feed prominence; a chain store’s listing often has fewer reviews than a well-loved local shop. Our post on {L('/blog/why-local-businesses-outrank-national-brands/', 'why local businesses outrank national brands')} explains the mechanics.</p>"""),

            ("Measuring in-store visits from your ads", f"""<p>This is where most boutique ad spend goes unmeasured. You run a Meta campaign, Saturday feels busier, and nobody can say whether those were related.</p>
<p>Google’s built-in options mostly aren’t built for one store. Store visit conversions need location assets, verified Business Profile locations and enough clicks, impressions and foot traffic to meet privacy thresholds, and the results are modeled, per {SRC['gsv']}. Google’s {SRC['gss']} goes further: it requires an allowlisted account and, for uploaded transactions, at least 30,000 transactions in the last 90 days. A single boutique won’t get close.</p>
<p>What a boutique can measure instead:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Method</th><th>How</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td>Offer codes by channel</td><td>A unique code or phrase per campaign (“mention the Reel”), entered at the POS</td><td>Direct in-store sales from a campaign. Undercounts, but it’s real</td></tr>
<tr><td>POS customer match</td><td>Compare emails and phones of new POS customers against people who clicked or signed up from an ad</td><td>How many ad-driven leads became buyers</td></tr>
<tr><td>Google Business Profile insights</td><td>Direction requests, calls and website clicks by month</td><td>Whether search visibility is rising before sales do</td></tr>
<tr><td>Holdout test</td><td>Run ads in alternating two-week blocks and compare store sales and traffic counts</td><td>A rough lift estimate for a single location</td></tr>
<tr><td>Door counter or POS transaction count</td><td>Track traffic and conversion rate daily</td><td>Whether more people came in, versus the same people buying more</td></tr>
</tbody></table></div>
<p>An illustrative first-year mix for a single-location boutique: $600 to $1,500 a month in Meta ads (mostly local Reels and retargeting), $300 to $800 in Google search and local inventory or Performance Max once your product data is clean, plus your time on content and email. Treat those as starting ranges, not benchmarks. Our {L('/blog/geo-fencing-ads-target-customers-nearby/', 'geofencing ads post')} covers the hyperlocal targeting side.</p>
<p>A first 90 days we’d follow:</p>
<ol>
<li><b>Month one.</b> Clean up the Business Profile, connect POS and online inventory, and start collecting email and text consent at the register.</li>
<li><b>Month two.</b> Commit to three Reels and two TikToks a week with sizes and prices on screen. Sign two local creators on written, disclosed deals. Plan one event.</li>
<li><b>Month three.</b> Launch Meta ads on the best-performing organic posts, set up offer codes by channel and run your first holdout test.</li>
</ol>
<p>If you want a senior strategist to build that plan around your store, your customers and your season, <a href="/contact/">get in touch</a>. Our {L('/services/paid-social-advertising/', 'paid social team')} handles the Instagram and TikTok side for retailers who’d rather be on the floor.</p>"""),
        ],
        "faq": [
            ("How do I get more customers into my boutique in The Woodlands?",
             "Post Instagram and TikTok try-ons that show sizes, prices and your location, keep your Google Business Profile current with photos, hours and products, and connect your register to your website so stock is accurate. Then give people reasons to visit that online stores can’t match, like trunk shows, private shopping nights, fit help and free gift wrap, and collect emails and text consent at every checkout."),
            ("Can a small boutique show its inventory on Google Maps?",
             "Yes. Google’s product editor lets you add products by hand, even without barcodes. Its Local Inventory app syncs stock from compatible POS systems, but it needs manufacturer UPC or EAN barcodes. Shopify stores can sync store-level stock through Shopify’s Google channel and Merchant Center, which can show products in Search, Maps and local inventory ads."),
            ("Do influencers need to disclose free clothes from a boutique?",
             "Yes. The FTC treats free products, store credit and discounts as material connections. Creators should disclose the relationship in the post itself, not only in a bio, using clear words like ad, advertisement or sponsored. In videos the disclosure should appear in the video, ideally spoken and on screen. Platform disclosure tools alone may not be enough."),
            ("Does Texas SB 140 apply to boutique text marketing?",
             "It can. SB 140, effective September 1, 2025, brought marketing texts under Texas’s telephone solicitation law, which can require registration and a $10,000 bond. There are exemptions, including one for businesses with a physical location under the same name for two years where most sales happen in store, and a November 2025 settlement treats consent-based texts as exempt. Ask your attorney which applies."),
            ("How can a boutique track whether ads bring people into the store?",
             "Google’s store visit and store sales reports require volume thresholds most single stores can’t meet. Instead, use unique offer codes or phrases per campaign at the register, match new POS customers against people who clicked or signed up from ads, watch Business Profile direction requests and calls, and run on-off holdout tests comparing store sales and traffic during ad and no-ad weeks."),
        ],
        "figures": {
            "vs": {
                "type": "compare",
                "title": "Where a Woodlands boutique beats the chains",
                "left": {"title": "National chains win on", "items": ["Ad budget and reach", "Selection and size depth", "Online checkout and free shipping", "Brand recognition", "Price matching and promos"]},
                "right": {"title": "Boutiques win on", "items": ["Curation and one-of-a-kind pieces", "Fit help from someone who knows you", "Events, trunk shows and private nights", "Back-in-stock texts from a real person", "Gift wrap and same-day local pickup"]},
                "alt": "Comparison of national chain and local boutique advantages for retail marketing in The Woodlands and Houston",
                "caption": "Market the right column hard. Don’t fight on the left one.",
            },
            "content": {
                "type": "checklist",
                "title": "A weekly content plan for a boutique",
                "sub": "Instagram Reels, Stories and TikTok",
                "items": ["New arrivals Reel with sizes and prices on screen", "Try-on across at least three sizes", "Owner or staff styling one piece three ways", "Stock-left Stories (“two mediums left”)", "A customer photo, shared with permission", "One local tie-in: event, neighbor shop, Market Street", "Behind the scenes: unboxing, steaming, merchandising", "A clear call to visit, DM to hold, or shop online"],
                "alt": "Checklist of weekly Instagram and TikTok content for boutique retail stores in The Woodlands and Houston",
                "caption": "Five or six posts a week from this list beats one polished shoot a month.",
            },
            "flow": {
                "type": "steps",
                "title": "From a Reel to a sale at the counter",
                "sub": "The connected setup for a single-location boutique",
                "steps": [["Post", "Reel or TikTok with size, price and location."], ["Check stock", "Local inventory on Google and the website."], ["Hold or pick up", "DM to hold, or buy online for same-day pickup."], ["Buy in store", "POS captures email, phone and texting consent."], ["Follow up", "Back-in-stock and new-arrival texts by size."]],
                "alt": "Five steps from Instagram content to in-store purchase for a boutique retail store in The Woodlands",
                "caption": "Saturday’s lost medium dress breaks at step two. Fix that one first.",
            },
            "ftc": {
                "type": "compare",
                "title": "Creator disclosure: weak vs. clear",
                "left": {"title": "Likely not enough", "items": ["Disclosure only in the bio", "#collab or #sp buried in hashtags", "“Thanks!” with no context", "Mention only in the video caption", "Relying on the platform’s tag alone"]},
                "right": {"title": "Clear disclosure", "items": ["“Ad” or “Sponsored” at the start", "“Thanks to [store] for the free dress”", "Spoken and on screen in video", "On every Story frame with the product", "Platform tag plus your own words"]},
                "alt": "Comparison of weak and clear FTC influencer disclosures for boutique creator partnerships in The Woodlands and Houston",
                "caption": f"Based on the {SRC['ftc101']}.",
            },
            "seasons": {
                "type": "stats",
                "title": "The two big retail seasons, 2026",
                "stats": [["$1.013T", "NRF holiday sales forecast, Nov.-Dec."], ["4.2%", "forecast holiday growth"], ["$250", "K-12 clothing spend per family"], ["Aug 7-9", "Texas sales tax holiday, 2026"]],
                "note": "Sources: NRF, Texas Comptroller",
                "alt": "Stats on 2026 holiday and back-to-school retail spending for boutique marketing in The Woodlands and Houston",
                "caption": f"From {SRC['nrf_h']}, {SRC['nrf_b']} and {SRC['tax']}.",
            },
            "calendar": {
                "type": "columns",
                "title": "A boutique’s year in sales",
                "sub": "Relative monthly revenue for a gift and clothing boutique",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [35, 50, 55, 60, 65, 45, 40, 60, 45, 55, 85, 100],
                "highlight": [1, 4, 7, 10, 11],
                "y_label": "Relative revenue",
                "note": "Illustrative example",
                "alt": "Column chart of seasonal boutique retail sales in The Woodlands with peaks for Valentine’s, Mother’s Day, back-to-school and holidays",
                "caption": "Valentine’s, Mother’s Day, back-to-school and the holidays. Plan content and ads six weeks ahead of each.",
            },
        },
    },
]
