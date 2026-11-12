"""Batch 11 (Live Events & Entertainment vertical): selling out a touring family exhibition or show city by city, and
tracking ticket sales from Meta and Google ads across Ticketmaster, Eventbrite, AXS, Etix and Universe.

Research, touring post: Eventbrite data via Pollstar (57% of tickets bought a week or less out, 2024); Nielsen's August
2026 Gauge (streaming 49.6% of TV watch-time, YouTube 15.8%); TikTok Spark Ads creation guide (creator authorization
codes, Business Center); Instagram's partnership ads page for creators; FTC Endorsement Guides FAQ (free products and
tickets need disclosure, disclosure in the video itself); FTC fees rule FAQ (live-event tickets, total price in ads,
effective May 12, 2025); Google Ads location targeting help (Presence vs Presence or interest, 1 km radius minimum);
NOAA National Hurricane Center climatology (June 1 to November 30, peak September 10); 93Q Country on RodeoHouston 2027
(March 2-21, 2027, NRG Park). First Byte's live entertainment page (250+ tour markets a year) and the Viceroy Los Cabos
case study (+212% direct bookings, feeder-market CTV, streaming audio and DOOH).
Research, tracking post: Eventbrite help (getting started with tracking pixels: Meta, Google Analytics, Google Ads,
X, TikTok, image pixel; Meta pixel PageView + Purchase, added standard events, server-side tracking with a Conversions
API access token, no domain verification; GA4 event_listing, event_register, purchase; Google Ads conversion ID and
label; refunds, transfers and manual transactions missing; embedded checkout pixels disabled in Europe and UK; tracking
links); TikTok's Ticketmaster pixel implementation guide (TM1 Marketing Pixel Tool, Complete Payment with face value,
currency, quantity; no PII or Add to Cart); MNTN's Ticketmaster pixel guide (TM1 Marketing tab, page types,
Confirmation Page-Primary/Resale, face value without fees); Ticketmaster Business on TM1 self-serve tools (came-from
codes); Universe help on Meta pixel and CAPI; Etix pages on Google Analytics and cross-domain funnel; Meta developer docs
(Purchase requires value and currency; dedup via event_id within 48 hours; action_source values; 7-day event_time
limit); Jon Loomer on 2026 Meta attribution defaults and on the Offline Conversions API discontinuation (May 2025);
Google help on GA4 cross-domain measurement, GA4 attribution settings and lookback windows, URL builder UTM parameters,
Google Ads conversion windows, and offline conversion imports / enhanced conversions for leads / Data Manager.
AXS: no public client-facing tracking documentation found, so the post tells readers to ask their AXS rep.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # touring post
    "pollstar": A("https://news.pollstar.com/2024/06/04/last-minute-ticket-buying-eventbrite-releases-study-at-niva-24/", "Eventbrite data reported by Pollstar"),
    "gauge": A("https://www.nielsen.com/news-center/2026/tv-viewing-cools-off-in-nielsens-august-gauge-reports-as-sports-take-a-breather-and-school-resumes/", "Nielsen’s August 2026 Gauge"),
    "spark": A("https://ads.tiktok.com/help/article/spark-ads-creation-guide?lang=en", "TikTok’s Spark Ads guide"),
    "igpa": A("https://creators.instagram.com/earn-money/partnership-ads", "Instagram’s partnership ads page"),
    "ftcend": A("https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking", "FTC’s Endorsement Guides FAQ"),
    "ftcfees": A("https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions", "FTC’s fees rule FAQ"),
    "geo": A("https://support.google.com/google-ads/answer/1722043?hl=en", "Google’s location targeting help"),
    "nhc": A("https://www.nhc.noaa.gov/climo/", "NOAA’s National Hurricane Center"),
    "rodeo": A("https://93qcountry.com/1705006/2027-houston-livestock-show-and-rodeo-dates/", "93Q Country"),
    # tracking post
    "ebpix": A("https://www.eventbrite.com/help/en-us/articles/598933/", "Eventbrite’s tracking pixel overview"),
    "ebmeta": A("https://www.eventbrite.ca/help/en-ca/articles/558547/how-to-create-a-tracking-pixel-with-meta/", "Eventbrite’s Meta pixel article"),
    "ebga": A("https://www.eventbrite.com/help/en-us/articles/475328/", "Eventbrite’s Google Analytics article"),
    "ebads": A("https://www.eventbrite.com/help/en-us/articles/604328/", "Eventbrite’s Google Ads pixel article"),
    "eblinks": A("https://www.eventbrite.com/blog/eventbrite-unique-tracking-links/", "Eventbrite’s tracking links"),
    "tttm": A("https://ads.tiktok.com/help/article/tiktok-ticketmaster-pixel-implementation-guide?lang=en", "TikTok’s Ticketmaster pixel guide"),
    "mntn": A("https://help.mountain.com/en/articles/6789573-install-pixels-in-ticketmaster", "MNTN’s Ticketmaster pixel guide"),
    "tmself": A("https://business.ticketmaster.com/client-marketing-self-serve-tools/", "Ticketmaster Business"),
    "universe": A("https://support.universe.com/hc/en-us/articles/360002452312-Use-Facebook-Pixel-on-your-Universe-event", "Universe’s Meta pixel guide"),
    "etix": A("https://hello.etix.com/clients/reporting-analytics", "Etix’s reporting and analytics page"),
    "metastd": A("https://developers.facebook.com/docs/meta-pixel/reference", "Meta’s standard events reference"),
    "dedup": A("https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events", "Meta’s deduplication docs"),
    "srvevt": A("https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event", "Meta’s server event parameters"),
    "loomeratt": A("https://www.jonloomer.com/meta-ads-attribution-2026/", "Jon Loomer’s 2026 attribution rundown"),
    "loomeroff": A("https://www.jonloomer.com/qvt/offline-conversions-api-deprecation-delayed/", "Jon Loomer"),
    "xdomain": A("https://support.google.com/analytics/answer/10071811?hl=en", "Google’s cross-domain measurement help"),
    "ga4attr": A("https://support.google.com/analytics/answer/10597962?hl=en", "GA4 attribution settings"),
    "utm": A("https://support.google.com/analytics/answer/10917952?hl=en", "Google’s URL builder help"),
    "gawin": A("https://support.google.com/google-ads/answer/3123169?hl=en", "Google Ads conversion windows"),
    "oci": A("https://support.google.com/google-ads/answer/2998031?hl=en", "Google’s offline conversion import help"),
}

TOUR = "/blog/touring-event-marketing-sell-out-every-city/"
TRACK = "/blog/track-ticket-sales-meta-google-ads-ticketing-platforms/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: touring events
    {
        "slug": "touring-event-marketing-sell-out-every-city",
        "title": "Touring Event Marketing: How to Sell Out Every City on the Route",
        "seo_title": "Touring Event Marketing: How to Sell Out Every City",
        "desc": "Touring event marketing for family exhibitions, fan conventions and shows: city launch timelines, budget per city, channel mix, pacing and when to move spend.",
        "category": "Paid ads",
        "icons": ["Meta", "TikTok", "Google Ads"],
        "art": "b2",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for touring event marketing across cities, planned from Houston and The Woodlands",
        "related": ["how-to-sell-more-event-tickets-houston", "streaming-tv-ads-worth-it-small-business", "find-the-right-influencers"],
        "sections": [
            (None, f"""<p>Monday morning tour call. The dinosaur expo has 14 stops on the spring route. Last weekend’s city sold 91% of capacity. This weekend’s is at 64% with five days to go. The city after that opens in 19 days and sits at 22%. Same creative, same budget formula, same ticket price, three completely different weeks.</p>
<p>Someone suggests adding a couple grand everywhere. Most tours do exactly that, and it’s usually wrong.</p>
<p>Selling out a touring event city by city comes down to treating every stop as its own small launch with its own calendar, budget and pacing target, then moving money between cities based on how each one is tracking against a curve you built from past stops. The creative and the playbook can be shared across the route. The decisions can’t.</p>
<p>This is written for marketing leads at touring family exhibitions, fan conventions, LEGO-style building festivals, bubble and science shows, holiday light experiences and similar productions that play a city for a weekend to a few weeks and move on. If you run one event in one town, our {L('/blog/how-to-sell-more-event-tickets-houston/', 'Houston event ticket playbook')} is the better fit.</p>"""),

            ("Why a tour is harder to market than a single event", f"""<p>Every city behaves differently, often for reasons that have nothing to do with your ads:</p>
<ul>
<li><b>Familiarity.</b> A city that hosted you two years ago has a past-buyer list and word of mouth. A first-time market has neither.</li>
<li><b>Venue.</b> A convention center downtown with paid parking sells differently from a fairground hall off the interstate with free lots.</li>
<li><b>Drive radius.</b> Families will drive farther for a two-hour exhibit on a Saturday than for an evening show on a school night.</li>
<li><b>What else is happening that weekend.</b> Spring break, a big rodeo, a college football home game, a church festival. You find these out late if nobody looks.</li>
<li><b>Lead time.</b> Late venue confirmations mean some cities get ten weeks of runway and others five.</li>
</ul>
<p>The budget side is messy too. Ad platforms reward stable campaigns, and tours keep starting and stopping them, so each new city starts learning from almost nothing. Proven creative is what carries over.</p>"""),

            ("The city launch timeline: announce, presale, on-sale, last chance", f"""<p>Every stop on the route should run on the same skeleton, anchored to its own dates. We plan backward from opening day. The phases below assume a stop that plays one to three weekends. Longer runs repeat the final-push pattern every weekend.</p>
<!--fig:timeline-->
<div class="tbl"><table>
<thead><tr><th>Phase</th><th>Timing (days before opening)</th><th>Share of city paid budget</th><th>Main jobs</th></tr></thead>
<tbody>
<tr><td>Announce</td><td>70 to 56</td><td>10%</td><td>Video announcing the city and dates, landing page live, presale signup form, press release to local media</td></tr>
<tr><td>Presale</td><td>56 to 49</td><td>5%</td><td>Email and SMS to opted-in past buyers and signups, presale code, retargeting signups who haven’t bought</td></tr>
<tr><td>Public on-sale</td><td>49 to 42</td><td>15%</td><td>Meta and TikTok prospecting, branded Google search, creator posts go live, early bird price clearly dated</td></tr>
<tr><td>The middle</td><td>42 to 15</td><td>20%</td><td>Group sales outreach, morning TV and radio, streaming TV in larger cities, steady retargeting</td></tr>
<tr><td>Last chance</td><td>14 to 0</td><td>40%</td><td>Heaviest spend, date-and-slot specific ads, “selling fast” only when true, weather messaging</td></tr>
<tr><td>Reserve</td><td>Held</td><td>10%</td><td>Moves to whichever weekend or city is closest to selling out at a good cost per order</td></tr>
</tbody></table></div>
<p>The heavy back end isn’t a guess. Per {SRC['pollstar']}, 57% of U.S. tickets sold from January to April 2024 were bought a week or less before the event. That was music data. Family exhibitions in accounts we’ve run follow a similar shape, because parents pick a weekend activity days ahead, not months.</p>
<p>Our rule across a route: no first-time city announces later than about seven weeks out. Return markets with a big past-buyer list can get away with less.</p>"""),

            ("How to set a budget per city", f"""<p>Most tours set a flat number per stop, something like $15,000 a city. It’s easy to manage and nearly always wrong, because a stop with 30,000 sellable tickets and a stop with 9,000 shouldn’t get the same money.</p>
<p>Start from each city’s gross potential instead:</p>
<ol>
<li><b>Sellable capacity.</b> Sessions or time slots times capacity per session, minus comps and holds.</li>
<li><b>Gross potential.</b> Sellable capacity times your average all-in ticket price.</li>
<li><b>Target gross.</b> Gross potential times your realistic sell-through goal (we usually plan to 80% to 90% and treat anything above as upside).</li>
<li><b>Paid media budget.</b> Target gross times the share of revenue you’re willing to spend on paid media. For touring family shows, a planning range of 8% to 15% is common in our experience, higher for first-time markets and lower for return markets with a strong list.</li>
</ol>
<p>Then set a target cost per order. If the average order is four tickets at $29 all in, an order is worth $116. At a 12% media share, you can afford roughly $14 in ad cost per order. Anything consistently above that in a city means the problem is creative, offer, date or tracking, and more money won’t fix it.</p>
<!--fig:budget-->
<div class="tbl"><table>
<thead><tr><th>City type</th><th>Sellable tickets</th><th>Target gross (85%)</th><th>Media share</th><th>Paid budget</th></tr></thead>
<tbody>
<tr><td>Large metro, first visit</td><td>32,000</td><td>$788,800</td><td>13%</td><td>$102,500</td></tr>
<tr><td>Large metro, return visit</td><td>32,000</td><td>$788,800</td><td>9%</td><td>$71,000</td></tr>
<tr><td>Mid-size metro, first visit</td><td>14,000</td><td>$345,100</td><td>12%</td><td>$41,400</td></tr>
<tr><td>Smaller market, return visit</td><td>8,000</td><td>$197,200</td><td>9%</td><td>$17,700</td></tr>
</tbody></table></div>
<p>Illustrative numbers, built on a $29 average ticket. The formula scales money to the opportunity, and media share is the dial for how hard a market is.</p>"""),

            ("The channel mix: Meta, Google, TikTok and streaming", f"""<p>The channels don’t change much from city to city. Their weights do, by phase and by market size.</p>
<p><b>Meta (Facebook and Instagram)</b> carries most touring family shows. That’s where parents are, and it’s where the purchase pixel data from your ticketing platform does the most good. A few structure choices that matter on a tour:</p>
<ul>
<li>One campaign per city, with the Sales objective optimized for Purchase. Name it consistently, like <code>tour26_tulsa_sales</code>, so reporting rolls up.</li>
<li>Location targeting by the ZIP codes and towns inside a realistic drive, not a lazy 50-mile circle. A Saturday exhibit pulls from much farther than a weeknight show.</li>
<li>Exclude overlapping metros when two stops are close together on the route. Otherwise one city’s budget pays to sell the other city’s tickets, and your pacing data gets muddy.</li>
<li>Reuse winning creative across cities, swapping only the city, venue and dates.</li>
</ul>
<p><b>Google Ads</b> catches the searches your other channels create. Run brand search on the show name plus each city (“dinosaur expo Tulsa,” “bubble show tickets Omaha”), category searches (“dinosaur exhibit near me,” “LEGO event this weekend”) and planner searches (“things to do with kids this weekend [city]”). {SRC['geo']} explains the Presence and “Presence or interest” options; for a tour stop, interest-based targeting can catch grandparents in another state planning a visit, so we usually leave it on for brand terms and use Presence for the broad planner terms. Brand search also keeps resellers from buying the top spot on your own show name.</p>
<p><b>TikTok</b> earns budget where the audience skews younger parents and where you have good creator content. Spark Ads let you run a creator’s own post as an ad; per {SRC['spark']}, the creator generates an authorization code in the app or you link the account through Business Center. Creator posts from local parents usually beat polished brand video on TikTok.</p>
<p><b>Streaming TV and YouTube</b> make sense in larger markets and longer runs. Streaming was 49.6% of TV watch-time in August 2026 and YouTube alone took 15.8%, per {SRC['gauge']}, so a ZIP-targeted :15 or :30 now reaches the family couch the way broadcast used to. We put CTV in the middle phase, where it builds the branded searches you then harvest in the last two weeks. Our {L('/blog/streaming-tv-ads-worth-it-small-business/', 'streaming TV explainer')} covers costs and measurement.</p>
<div class="tbl"><table>
<thead><tr><th>Phase</th><th>Meta</th><th>Google</th><th>TikTok</th><th>Streaming / YouTube</th></tr></thead>
<tbody>
<tr><td>Announce and on-sale</td><td>45%</td><td>15%</td><td>20%</td><td>20%</td></tr>
<tr><td>The middle</td><td>40%</td><td>15%</td><td>15%</td><td>30%</td></tr>
<tr><td>Last chance</td><td>55%</td><td>30%</td><td>15%</td><td>0%</td></tr>
</tbody></table></div>
<p>That split is illustrative, for a large metro spending above roughly $40,000. In smaller cities, cut streaming and TikTok first. Our {L('/services/paid-social-advertising/', 'paid social team')} and {L('/services/ctv-ooh-streaming-radio/', 'streaming TV team')} plan these splits market by market.</p>"""),

            ("Local media and influencer families", f"""<p>Paid media sells most of the tickets, but local voices make it cheaper. In our experience, a city with a morning-show segment and a few local parent creators posting shows a lower cost per order than one with ads alone.</p>
<p>For each city, about eight weeks out:</p>
<ul>
<li><b>Local TV and radio.</b> Pitch morning shows with something visual and a hook (an animatronic in the studio, a kid-builder contest). Send the press kit with b-roll, dates, prices and a contact who answers on weekends.</li>
<li><b>Family calendars and parent groups.</b> Get listed early on the metro’s family-events sites, and ask big parent Facebook groups about a giveaway post.</li>
<li><b>Creator families.</b> Pick three to six local parents with engaged followings in that metro, not one big national account. Our {L('/blog/find-the-right-influencers/', 'guide to finding the right influencers')} covers vetting.</li>
</ul>
<p>Give creators comp tickets for opening weekend and a short brief. Ours fits on one page: the dates and venue, the two or three moments worth filming, the all-in price and the promo code, the deadline for posting, and what not to say. Then ask for whitelisting rights so you can put paid budget behind the best posts as Spark Ads on TikTok or partnership ads on Instagram, which {SRC['igpa']} describes as brands running a creator’s content as an ad to reach beyond the creator’s followers.</p>
<p>Disclosure isn’t optional. The {SRC['ftcend']} treats free products and perks as connections that need disclosure, says a vague disclosure isn’t enough when free tickets are involved, and says the disclosure “has the best chance of being clear and conspicuous if it’s included in the video itself.” Put “#ad” or “we got free tickets from [show]” in the brief, and check the posts. Our {L('/blog/ftc-rules-influencer-partnerships/', 'post on FTC rules for influencer partnerships')} has more.</p>"""),

            ("The pacing dashboard: tickets sold vs. days out", f"""<p>This is the tool that turns a Monday tour call from opinions into decisions. You need one chart per city, and one curve that says where a typical city should be at each point.</p>
<p>Build the curve from your own history. Take every past stop that sold at least 80% of target, and for each one calculate cumulative tickets sold as a share of final tickets at 56, 42, 28, 21, 14, 7 and 3 days before opening. Average them. If you have different show types (a weekend-only stop vs. a three-week run), build a curve for each.</p>
<!--fig:pacing-->
<p>Then for every live city, every morning:</p>
<ul>
<li><b>Expected to date</b> = target tickets × curve share at today’s days-out.</li>
<li><b>Pace index</b> = tickets sold to date ÷ expected to date. 100 means on curve. 120 means ahead. 75 means trouble.</li>
<li><b>Cost per order to date</b> = paid spend in that city ÷ online orders in that city (from the ticketing platform, not the ad platform).</li>
<li><b>Sell-through by session.</b> Saturday 11 a.m. can be sold out while Thursday 4 p.m. is at 30%. Totals hide that.</li>
</ul>
<div class="tbl"><table>
<thead><tr><th>City</th><th>Days out</th><th>Sold</th><th>Target</th><th>Curve share</th><th>Pace index</th><th>Cost per order</th></tr></thead>
<tbody>
<tr><td>City A</td><td>5</td><td>17,400</td><td>27,000</td><td>66%</td><td>98</td><td>$11.20</td></tr>
<tr><td>City B</td><td>19</td><td>3,900</td><td>12,000</td><td>40%</td><td>81</td><td>$17.80</td></tr>
<tr><td>City C</td><td>33</td><td>2,600</td><td>9,000</td><td>27%</td><td>107</td><td>$9.40</td></tr>
</tbody></table></div>
<p>Illustrative example. City B is the one to talk about on Monday. City C is ahead and cheap, so it’s a candidate to receive money if City B can’t use it well.</p>
<p>The ticketing platform is the source of truth for tickets and revenue. Our companion post on {L(TRACK, 'tracking ticket sales from Meta and Google ads')} covers why those numbers never match and how to reconcile them.</p>"""),

            ("When to add spend, and when to cut it", f"""<p>Moving money between cities is the whole advantage of running a tour as one program. Write the rules down before the route starts, so nobody makes them up at 9 p.m. on a Thursday.</p>
<!--fig:rules-->
<p>The trickiest one is the city that’s behind. The instinct is to throw money at it. Run the diagnosis first, in this order:</p>
<ol>
<li><b>Tracking.</b> Are purchases still reaching Meta and Google? A broken pixel looks exactly like a bad market.</li>
<li><b>Offer.</b> Is the all-in price in the ad? Is there a reason to buy now (early bird ending, a slot selling out)?</li>
<li><b>Creative.</b> Is the city’s version running the hooks that won elsewhere, or a tired variant?</li>
<li><b>Geography.</b> Is the targeting map drawn around where buyers actually live? Pull ZIP codes from the ticketing report and compare.</li>
<li><b>Calendar.</b> Did something big land on your weekend? If so, shift budget to the other weekend or weekday slots rather than fighting it.</li>
</ol>
<p>If all five check out and the city is still under 80 on pace at 21 days out, add money in measured steps (20% to 30% a few days apart) and watch cost per order. If cost per order climbs past your ceiling as budget goes up, stop. You’ve hit the ceiling of demand at that price, and the next lever is price tiers, group sales or added value, not media.</p>
<p>Cutting matters too. Pull sold-out sessions from the ads that day, and when a weekend passes 95%, move the creative to the next weekend or city.</p>"""),

            ("Weather and date competition", f"""<p>A tour runs into each city’s calendar and climate. Some of it you can plan for months ahead. Some of it you find out about Tuesday.</p>
<p>Check each city’s calendar before you confirm dates, and again at announce: school spring breaks and holidays, big rodeos and state fairs, college and NFL home games, marathons that close roads near the venue, and other family shows playing the same month. Here at home, RodeoHouston runs March 2 to 21, 2027 at NRG Park, per {SRC['rodeo']}. A family exhibition in Houston during those three weeks is competing with the biggest family outing of the year for weekend time and spending money. You can still play it. Price and message it differently, lean on weekday sessions and school groups, and don’t expect pacing to match a quiet month.</p>
<p>Weather cuts both ways. For an indoor show, a rainy or brutally hot weekend can be the best sales weekend of the run, so build a “beat the heat” or “rainy day plan” ad set and keep it paused until the forecast turns. For outdoor stops, weather is a risk to the whole date. In the Gulf states, hurricane season runs June 1 to November 30 with the peak around September 10, according to {SRC['nhc']}. Have a written reschedule plan and pre-built ads and emails ready, including the refund and transfer rules, so you can switch the message within hours if a storm hits.</p>
<p>Late buyers check the forecast, so say on the landing page what happens in bad weather.</p>"""),

            ("Venue partners: what to ask for before you sign", f"""<p>The venue’s email list, social accounts, marquee and ticketing setup are all part of your marketing. Most of it is negotiable before the deal is signed and much harder after.</p>
<p>What we’d put on the list for every venue:</p>
<ul>
<li><b>Ticketing access.</b> Which platform the venue uses, who controls the event page, and whether you can place your own Meta, Google and TikTok tags on the confirmation page. On Ticketmaster, tags are placed through the TM1 account holder’s pixel tool, which is often the venue, not the touring show. Ask before on-sale, not after.</li>
<li><b>Daily sales reporting</b> by session and by ZIP code, delivered automatically. You can’t pace a city on weekly PDFs.</li>
<li><b>Venue email and social.</b> A dedicated email to their list at announce and in the final week, plus a set number of posts and stories.</li>
<li><b>On-site and outdoor assets.</b> Marquee, digital screens, lobby posters, and any outdoor boards they control.</li>
<li><b>Group sales.</b> Who handles school, scout and church groups, and whether the venue’s group desk will work your show.</li>
</ul>
<p>Answer the ticketing question first. If purchases can’t reach your ad accounts, you’re running that city half blind.</p>"""),

            ("Pricing in ads, and mistakes we see on tours", f"""<p>One rule now applies to every city. Since May 12, 2025, the FTC’s fees rule has required any business that “offers, displays, or advertises live-event tickets” to show the total price, mandatory fees included, more prominently than other pricing information, per the {SRC['ftcfees']}. Taxes can come later as long as they’re disclosed before payment. If an ad says “tickets from $24,” $24 needs to be the all-in price of a ticket somebody can actually buy.</p>
<p>The mistakes we see most often on touring campaigns:</p>
<ul>
<li>Flat budgets per city regardless of capacity or market history.</li>
<li>One national campaign with every city lumped together, so nobody can tell which city is working.</li>
<li>Spending evenly across weeks instead of saving 40% or more for the final two.</li>
<li>Judging cities by ad-platform purchases instead of ticketing-platform sales.</li>
<li>Creator posts with no disclosure, or comp tickets with no brief.</li>
</ul>
<p>This is the kind of work First Byte does most weeks: our live entertainment team plans and buys more than 250 tour markets a year (see our {L('/industries/live-entertainment/', 'live entertainment page')}). The same feeder-market flighting works outside events too: the {L('/case-studies/viceroy-los-cabos/', 'Viceroy Los Cabos case study')} pairs connected TV, streaming audio and DOOH in feeder markets with paid social and search, and reports +212% direct bookings.</p>
<p>If you’re planning a route and want a senior strategist to build the city-by-city plan with you, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How far in advance should a touring event start marketing in each city?",
             "For most touring family shows and exhibitions, announce each city about eight to ten weeks before opening, run a short presale to past buyers and signups, open the public on-sale about seven weeks out, and save roughly 40 percent of the paid budget for the final fourteen days. Return markets with a big past-buyer list can work with a shorter runway. First-time markets rarely can."),
            ("How much should a touring show spend on ads per city?",
             "Base it on each city’s gross potential instead of a flat number. Multiply sellable capacity by the average all-in ticket price, apply a realistic sell-through goal, then apply a media share. Many touring family shows plan somewhere between 8 and 15 percent of target gross for paid media, higher for first visits and lower for return markets. Then set a maximum cost per order and hold to it."),
            ("What is a pacing dashboard for ticket sales?",
             "A pacing dashboard compares each city’s tickets sold to date against where a typical city should be at the same number of days before opening. You build the expected curve from past stops, then calculate a pace index: tickets sold divided by expected tickets to date. A pace index of 100 is on track, above 110 is ahead, and below 80 needs a diagnosis before more spend."),
            ("Should a touring event use influencers in every city?",
             "Usually yes, but local ones. Three to six parent creators with real followings in that metro tend to beat one big national account for family shows. Give them comp tickets, a one-page brief and a posting deadline, ask for rights to run their posts as ads, and make sure every post discloses the free tickets in the video itself, as the FTC’s endorsement guidance recommends."),
            ("When should we move ad budget from one tour city to another?",
             "Move money when one city is ahead of pace with a low cost per order and another is behind for reasons more media can fix. Before adding budget to a lagging city, check tracking, the offer, the creative, the targeting map and the local calendar. Add in steps of 20 to 30 percent and stop if cost per order climbs past your ceiling."),
        ],
        "figures": {
            "timeline": {
                "type": "steps",
                "title": "One city’s launch, from announce to last chance",
                "sub": "Days before opening, for a stop that plays one to three weekends",
                "steps": [["Announce (70-56)", "City video, landing page, presale signup, local press release."], ["Presale (56-49)", "Email and SMS to opted-in past buyers with a code."], ["On-sale (49-42)", "Meta and TikTok prospecting, brand search, creators post."], ["The middle (42-15)", "Group sales, morning TV, streaming TV, retargeting."], ["Last chance (14-0)", "Heaviest spend, slot-specific ads, weather messaging."]],
                "note": "Illustrative example",
                "alt": "Timeline of a touring event city launch from announce to last chance, as planned by a Houston and The Woodlands agency",
                "caption": "The same skeleton runs in every city, anchored to that city’s opening day.",
            },
            "budget": {
                "type": "bars",
                "title": "Paid budget scales with the city",
                "sub": "Example paid media budget per stop from the formula in this section",
                "items": [["Large metro, first visit", 102500, "$102,500"], ["Large metro, return", 71000, "$71,000"], ["Mid-size, first visit", 41400, "$41,400"], ["Smaller market, return", 17700, "$17,700"]],
                "highlight": [0],
                "note": "Illustrative example built on a $29 average all-in ticket",
                "alt": "Bar chart of illustrative paid media budgets per touring event city, from a Houston and The Woodlands marketing agency",
                "caption": "Capacity, price and market history set the budget. A flat number per city does not.",
            },
            "pacing": {
                "type": "columns",
                "title": "A sales curve to pace every city against",
                "sub": "Cumulative share of final tickets sold, by days before opening",
                "labels": ["56", "42", "28", "21", "14", "7", "3", "Open"],
                "values": [8, 18, 30, 37, 46, 58, 76, 100],
                "highlight": [5, 6],
                "y_label": "% of final tickets",
                "note": "Illustrative example. Build yours from past stops that hit at least 80% of target.",
                "alt": "Column chart of a touring event ticket sales curve by days out, used for pacing by a Houston and The Woodlands agency",
                "caption": f"Late buying is normal. {SRC['pollstar']} found 57% of tickets bought a week or less out.",
            },
            "rules": {
                "type": "checklist",
                "title": "Budget rules to write before the route starts",
                "sub": "So nobody improvises at 9 p.m. on a Thursday",
                "items": ["Pace index 110+ and cost per order under target: city can receive reserve", "Pace index under 80 at 21 days out: diagnose before adding", "Add budget in 20% to 30% steps, a few days apart", "Cost per order above ceiling after an increase: stop adding", "Session sold out: remove it from ads that day", "Weekend above 95%: shift creative to the next weekend or city", "Big local event announced: move spend to other dates", "Reserve released only by the tour marketing lead"],
                "alt": "Checklist of budget reallocation rules for touring event marketing from a Houston and The Woodlands agency",
                "caption": "Your thresholds may differ. Having them written down is what matters.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: tracking ticket sales
    {
        "slug": "track-ticket-sales-meta-google-ads-ticketing-platforms",
        "title": "How to Track Ticket Sales From Meta and Google Ads on Ticketmaster, Eventbrite, AXS and Etix",
        "seo_title": "Track Ticket Sales From Meta & Google Ads, by Platform",
        "desc": "How to track ticket sales from Meta and Google ads on Ticketmaster, Eventbrite, AXS, Etix and Universe: pixels, Conversions API, GA4, UTMs and reconciliation.",
        "category": "Paid ads",
        "icons": ["Meta", "Google Analytics", "Google Ads"],
        "art": "b4",
        "hero": "ticket",
        "hero_alt": "Illustration of a ticket for tracking event ticket sales from Meta and Google ads, from a Houston and The Woodlands agency",
        "related": ["how-to-sell-more-event-tickets-houston", "track-form-submissions-phone-calls-ga4-google-ads", "measure-marketing-success-metrics"],
        "sections": [
            (None, f"""<p>Post-tour wrap meeting. The Meta report says the campaign drove 1,240 purchases in one city. GA4 says 610. Google Ads claims 380. The ticketing settlement says 3,900 tickets were sold online in that city, from about 1,050 orders. The promoter asks which number is real, and the room goes quiet.</p>
<p>They’re all real. They’re just counting different things, over different windows, with different blind spots.</p>
<p>To track ticket sales from Meta and Google ads, put each ad platform’s pixel on your ticketing platform’s confirmation step (and the server-side version where the platform supports it), make sure the purchase passes order value and currency, tag every link with consistent UTMs, and then reconcile everything weekly against the ticketing platform’s own sales report, which is the only source of truth for tickets and revenue.</p>
<p>What each major platform supports varies a lot, and some of it isn’t documented publicly. Below is what we could verify from each platform’s help pages, and what to ask your rep where we couldn’t.</p>"""),

            ("Why ad platforms and ticketing reports never match", f"""<p>Before fixing anything, know which gaps are normal. Every one of these shows up in event accounts we’ve worked in:</p>
<ul>
<li><b>Orders vs. tickets.</b> Ad platforms count purchases (orders). Ticketing reports count tickets. A family of four is one purchase and four tickets.</li>
<li><b>Face value vs. all-in.</b> Some platforms pass face value without fees. Your settlement may show gross with fees, or net after them.</li>
<li><b>Attribution windows.</b> Meta credits a purchase within its click, engagement and view windows. Google Ads uses its own. GA4 uses another. One sale can be claimed by all three.</li>
<li><b>Privacy and blocking.</b> Eventbrite says plainly that tracking pixels “aren’t able to track every purchase,” because buyers who disable tracking or use strict privacy settings aren’t tracked, per {SRC['ebpix']}.</li>
<li><b>Refunds, transfers and manual sales.</b> Eventbrite’s GA4 ecommerce data “doesn’t account for refunds, transfers, or manual transactions,” per {SRC['ebga']}. Box office and group sales never touch a pixel.</li>
<li><b>Broken journeys.</b> A buyer clicks an ad on their phone and buys on a laptop, or the session breaks when they hop from your site to the ticketing domain.</li>
</ul>
<!--fig:leak-->
<p>So the goal isn’t to make the numbers match. It’s to know how big each gap normally is, so that when one moves you notice.</p>"""),

            ("What each ticketing platform supports", f"""<p>We verified each of these against the platform’s own help pages or a partner’s official setup guide as of November 2026. Ticketing platforms change these features often, so confirm before a big on-sale.</p>
<div class="tbl"><table>
<thead><tr><th>Platform</th><th>Meta</th><th>Google (GA4 / Google Ads)</th><th>Other notes</th></tr></thead>
<tbody>
<tr><td>Eventbrite</td><td>Pixel fires PageView and Purchase by default; extra standard events can be mapped to listing, order form, confirmation or seat selection; optional server-side tracking with a Conversions API access token</td><td>GA4 sends page views, event_listing, event_register and purchase with total and currency; Google Ads pixel takes a conversion ID and label</td><td>TikTok, X and image pixels too; can’t verify Eventbrite’s domain with Meta; tracking links per campaign</td></tr>
<tr><td>Ticketmaster</td><td>Placed through the TM1 Marketing Pixel Tool by the TM1 client; confirm Meta tag options and any server-side setup with your rep</td><td>Same pixel tool; confirm GA4 and Google Ads tag types with your rep</td><td>TikTok tag type documented; confirmation pixel gets face value, currency and quantity; no PII or Add to Cart data</td></tr>
<tr><td>Universe</td><td>Pixel plus optional Conversions API; Viewed Tickets, Added Tickets and Purchase with order value, currency and ticket count</td><td>Not covered in the pixel guide; check Universe’s integration settings</td><td>Embedded widgets need the pixel base code and Universe’s listener script on your site</td></tr>
<tr><td>Etix</td><td>Not documented publicly; ask your rep</td><td>Etix documents a Google Analytics integration covering the funnel from your site to Etix.com</td><td>Ask about GA4 ecommerce fields and cross-domain setup</td></tr>
<tr><td>AXS</td><td>Not documented publicly; ask your rep</td><td>Not documented publicly; ask your rep</td><td>Get answers in writing before on-sale</td></tr>
</tbody></table></div>
<p><b>Eventbrite.</b> The setup lives under your event’s Marketing section, Tracking pixels. Per {SRC['ebmeta']}, the Meta pixel fires PageView on the listing and Purchase on order confirmation, and you can add standard events like InitiateCheckout tied to the order form. To turn on server-side tracking, flip the Server side tracking toggle and paste a Conversions API access token from Meta Events Manager (Eventbrite won’t help generate it). Eventbrite also notes you can’t verify its domain with Meta, so some Meta features may be unavailable. For Google Ads, {SRC['ebads']} asks only for the conversion ID (the digits after “AW-”) and the conversion label, includes total and currency when ecommerce data is available, and says Google Tag Manager isn’t used on Eventbrite. Pixels are also disabled with embedded checkout in some regions, such as Europe and the UK.</p>
<p><b>Ticketmaster.</b> Ticketmaster clients place tags through the pixel manager in TM1. {SRC['mntn']} walks through it: Marketing tab, Add New, Pixel, then pick page types such as Event Detail Page and Confirmation Page-Primary or Confirmation Page-Resale. {SRC['tttm']} documents a Complete Payment event on the confirmation page with value (sum of face value), currency and quantity, and says no PII or Add to Cart data is shared. The practical catch for a touring show: the TM1 account often belongs to the venue or the promoter, so you may need them to place your tags. Ticketmaster’s self-serve tools also include came-from codes for source tracking, per {SRC['tmself']}.</p>
<p><b>Universe.</b> Per {SRC['universe']}, a Pixel ID is required and a Conversions API token is optional. If you use Universe’s embedded widget on your own site, you need both the Meta base code and Universe’s listener script, or the widget’s events won’t be captured.</p>
<p><b>Etix and AXS.</b> {SRC['etix']} describes viewing “the entire patron purchase funnel, from your website to Etix.com, through your own Google Analytics account.” We couldn’t find current public documentation for Meta pixel or Conversions API support on Etix, or for client-side tag support on AXS, so we won’t guess. Use the questions in the checklist below and get the answers in writing.</p>
<!--fig:questions-->"""),

            ("Pixel plus Conversions API, and why you want both", f"""<p>A browser pixel depends on the buyer’s browser cooperating. Ad blockers, privacy settings and in-app browsers all drop events. The Conversions API sends the same purchase from the ticketing platform’s server, which those blockers don’t touch.</p>
<p>When both run, Meta needs to know they’re the same purchase. Per {SRC['dedup']}, the pixel’s eventID must match the server event’s event_id, and the event names must match; events are only deduplicated if they arrive within 48 hours of the first one with that ID. On a ticketing platform that handles both sides for you (Eventbrite and Universe both describe server-side as an add-on to the pixel), you don’t set the IDs yourself, but you should still check Events Manager for duplicate purchase counts after turning it on.</p>
<p>The value matters as much as the count. Meta’s {SRC['metastd']} lists currency and value as required parameters for the Purchase event. Without value, you can’t see return on ad spend in Ads Manager, and you can’t optimize for value. Test it with a real order and look at the event details in Events Manager’s Test Events tab before you spend a dollar.</p>"""),

            ("GA4 cross-domain tracking when the checkout lives somewhere else", f"""<p>Most tours send buyers from their own site (city pages, date finders) to a ticketing domain to check out. Without cross-domain measurement, GA4 sees the jump as a new user arriving from a referral, and the original ad click gets lost.</p>
<p>Per {SRC['xdomain']}, the setup is Admin, Data collection and modification, Data streams, select your web stream, Configure tag settings, Configure your domains, then add each domain. The linker passes IDs in a <code>_gl</code> URL parameter. The tag on every domain must use the same G- tag ID from the same web data stream.</p>
<p>That last requirement is where ticketing platforms get tricky. You can only do true cross-domain tracking if you can put your own GA4 tag on the ticketing pages. Some platforms let you add a GA4 measurement ID (Eventbrite does). Others won’t. Google also warns that redirects or pages that strip query parameters can drop <code>_gl</code>, and that JavaScript-driven navigation isn’t covered, so test the full path from your city page into checkout and confirm the parameter survives.</p>
<p>If you can’t get your tag onto the checkout, add the ticketing domain to GA4’s unwanted referrals list (also under Configure tag settings) so it isn’t credited as a traffic source, mark clicks on your “Buy tickets” buttons as an event, and rely on UTMs and the ticketing platform’s own source reports for sales. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads conversion guide')} covers marking events as key events and importing them.</p>"""),

            ("Passing purchase value, and deciding what revenue means", f"""<p>Decide once, across the whole tour, which revenue number counts. Then make sure every platform reports that one, or note clearly which one it reports.</p>
<div class="tbl"><table>
<thead><tr><th>Revenue definition</th><th>What it includes</th><th>Where you’ll see it</th></tr></thead>
<tbody>
<tr><td>Face value</td><td>Ticket price before fees</td><td>Ticketmaster confirmation pixels (per TikTok’s and MNTN’s guides); many settlements</td></tr>
<tr><td>Order total</td><td>What the buyer paid, which may include fees</td><td>Platforms that pass “total amount” to pixels, such as Eventbrite</td></tr>
<tr><td>Net to show</td><td>After platform fees and refunds</td><td>Settlement reports only</td></tr>
</tbody></table></div>
<p>For media decisions, face value or order total is fine as long as it’s consistent. For return on ad spend at settlement, use net from the ticketing report and divide by total ad spend. Two other settings to check in Google Ads: count every conversion for purchases (not one per click), and use the value passed by the tag instead of a fixed value.</p>"""),

            ("UTMs and naming for a multi-city tour", f"""<p>UTMs are the boring backbone. When pixels fail, the ticketing platform’s source report and GA4 still show where buyers came from, as long as the links were tagged.</p>
<p>Google’s {SRC['utm']} lists the supported parameters (utm_source, utm_medium, utm_campaign, utm_id, utm_term, utm_content and utm_source_platform) and notes that values are case sensitive, so <code>Facebook</code> and <code>facebook</code> become two sources. Use lowercase everywhere.</p>
<!--fig:utms-->
<p>A convention that works for tours: <code>utm_source=meta</code>, <code>utm_medium=paid_social</code>, <code>utm_campaign=tour26_tulsa_lastchance</code>, <code>utm_content=dino_reveal_15s</code>. City and phase in the campaign, creative in the content. Keep the list in a shared sheet and generate links from it.</p>
<p>Ticketing platforms have their own source tools that sit beside UTMs. {SRC['eblinks']} report page views, tickets and sales per link, with sales reported immediately. Ticketmaster has came-from codes. Use them for creators, partners and the venue’s email, where you want sales per partner without relying on a pixel.</p>"""),

            ("Offline sales, box office and manual uploads", f"""<p>Box office walk-ups, group sales and phone orders never fire a pixel. On a family show with heavy school-group business, that can be a meaningful share of revenue. You can still send them back to the ad platforms, as long as you collected an email or phone number and have permission to use it for this.</p>
<p><b>Google Ads.</b> {SRC['oci']} describes saving the Google Click ID (GCLID) with the customer record and importing it later with the conversion. Google now recommends enhanced conversions for leads, which matches on hashed customer data like email, and points to Data Manager as the quickest setup. For ticketing, this works best for group sales that start with a form on your site.</p>
<p><b>Meta.</b> The separate Offline Conversions API was discontinued in May 2025, per {SRC['loomeroff']}, and offline events now go through the main Conversions API. {SRC['srvevt']} lists action_source values including physical_store and phone_call, and says events can be sent up to seven days after they happen; send a request with anything older and the whole request errors. Upload at least weekly.</p>
<p>For most touring shows, a weekly CSV of group and box office orders through a connector is plenty. Don’t build a custom pipeline until you know that slice is big enough to matter.</p>"""),

            ("Attribution windows, and why short ones suit ticketing", f"""<p>Each platform credits a purchase within its own time windows after someone clicks or sees an ad.</p>
<div class="tbl"><table>
<thead><tr><th>Platform</th><th>Defaults</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Meta</td><td>7-day click, 1-day engage-through, 1-day view</td><td>Since March 2026, click-through counts link clicks only; engage-through covers reactions, comments, shares, saves and engaged video views; 28-day click is no longer an optimization option (per {SRC['loomeratt']})</td></tr>
<tr><td>Google Ads</td><td>30-day click, 3-day engaged-view, 1-day view</td><td>Click windows can be shortened or extended up to 90 days, per {SRC['gawin']}</td></tr>
<tr><td>GA4</td><td>90-day lookback for key events like purchase</td><td>Data-driven or rules-based models; lookback can be set to 30 or 60 days (per {SRC['ga4attr']})</td></tr>
</tbody></table></div>
<p>Ticket buying is compressed. Most purchases happen within days of the decision, and late in the cycle. Shortening Google Ads’ purchase window to 7 days brings it closer to Meta’s and stops campaigns from claiming credit for a click five weeks before the show. Whatever you choose, use the same windows across every city on the tour, and write them on the report so nobody compares a 30-day number to a 7-day one.</p>
<p>View-through and engage-through purchases are real but generous. We report them separately and judge prospecting on click-through plus the blended numbers below.</p>"""),

            ("Reconciling platform-reported vs. ticketing-reported sales", f"""<p>Once a week, per city, line the numbers up. It takes 20 minutes with a decent sheet.</p>
<!--fig:reconcile-->
<p>Three metrics do most of the work:</p>
<ul>
<li><b>Tracking coverage</b> = ad-platform purchases (click-through only) ÷ online orders in the ticketing report. It tells you what share of orders your pixels see. Track it over time; a sudden drop usually means a broken tag, not a bad campaign.</li>
<li><b>Blended cost per order</b> = total paid spend in the city ÷ all online orders in the city. Ad-platform cost per purchase flatters or punishes campaigns depending on tracking. Blended cost doesn’t care.</li>
<li><b>Media efficiency ratio</b> = ticketing revenue in the city ÷ total paid spend in the city. Same idea, in revenue terms.</li>
</ul>
<p>For a bigger question (is this channel actually adding sales?), run a holdout. Pick two comparable cities on the route, keep everything identical except one channel, say streaming TV, and compare pace and blended cost per order. It’s not a lab experiment, but it beats arguing about attribution.</p>"""),

            ("A reporting template you can copy", f"""<p>One row per city per week. Keep spend and ad-platform columns on the left, ticketing columns on the right, and the calculated columns at the end.</p>
<div class="tbl"><table>
<thead><tr><th>Column</th><th>Source</th><th>Example</th></tr></thead>
<tbody>
<tr><td>City, week, days out</td><td>Tour plan</td><td>Tulsa, wk of Mar 8, 19</td></tr>
<tr><td>Spend by channel</td><td>Meta, Google Ads, TikTok, CTV invoices</td><td>$4,100 / $1,300 / $700 / $1,500</td></tr>
<tr><td>Ad-platform purchases (click)</td><td>Meta, Google Ads</td><td>288 / 96</td></tr>
<tr><td>Ad-platform purchase value</td><td>Meta, Google Ads</td><td>$31,900 / $11,200</td></tr>
<tr><td>Online orders and tickets</td><td>Ticketing report</td><td>540 orders, 2,050 tickets</td></tr>
<tr><td>Online gross</td><td>Ticketing report</td><td>$59,400</td></tr>
<tr><td>Box office and group tickets</td><td>Ticketing report</td><td>310</td></tr>
<tr><td>Tracking coverage</td><td>Calculated</td><td>(288 + 96) ÷ 540 = 71%</td></tr>
<tr><td>Blended cost per order</td><td>Calculated</td><td>$7,600 ÷ 540 = $14.07</td></tr>
<tr><td>Media efficiency ratio</td><td>Calculated</td><td>$59,400 ÷ $7,600 = 7.8</td></tr>
<tr><td>Pace index</td><td>From the tour pacing sheet</td><td>81</td></tr>
</tbody></table></div>
<p>Illustrative example. Note that the coverage formula adds Meta and Google purchases, which can double-count a buyer who clicked both; read it as a trend, not a precise share. The pace index comes from the curve in our {L(TOUR, 'touring event marketing playbook')}.</p>"""),

            ("Test before every on-sale, and mistakes we see", f"""<p>Before each city’s on-sale, buy a real ticket through a real ad click. Watch Meta’s Test Events tab and Google’s Tag Assistant while you do it, then confirm the purchase shows the right value and currency and appears once, not twice. Refund yourself after. Our {L('/blog/how-to-sell-more-event-tickets-houston/', 'Houston event ticket post')} has the hidden $1 ticket version of this for platforms that allow it.</p>
<p>The mistakes we see most:</p>
<ul>
<li>Pixels placed on the event page but not the confirmation page, so purchases never fire.</li>
<li>A new event created by copying an old one, but pixel scope set to “this event only,” so the new city has no tracking. Eventbrite notes that event-only pixels don’t carry over when an event is copied.</li>
<li>Value missing from Purchase, so nobody can see return on ad spend.</li>
<li>UTMs typed by hand in mixed case, splitting one source into three.</li>
<li>Comparing Meta’s 7-day click number to Google’s 30-day click number as if they were the same thing.</li>
<li>Waiting for the venue to place tags on Ticketmaster until the week of on-sale.</li>
<li>Judging a city by ad-platform purchases when the ticketing report says something else.</li>
</ul>
<p>Our {L('/blog/measure-marketing-success-metrics/', 'guide to marketing metrics')} goes broader on what to report, and our {L('/services/search-marketing/', 'search marketing team')} sets up the Google side. If your tour’s numbers don’t line up and you want a senior strategist to build a tracking and reporting plan around your ticketing platform, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Can I put a Meta pixel on Ticketmaster?",
             "Ticketmaster clients place marketing tags through the pixel manager in TM1, under the Marketing tab, choosing page types such as the event detail page and the confirmation page. Access usually sits with the venue or promoter that holds the TM1 account, so a touring show may need them to place its tags. Confirm which tag types and server-side options your account supports with your Ticketmaster rep before on-sale."),
            ("Does Eventbrite support the Meta Conversions API?",
             "Yes. In Eventbrite’s Tracking pixels settings under Marketing, you add your Meta pixel ID and can switch on server-side tracking by pasting a Conversions API access token from Meta Events Manager. The pixel fires PageView and Purchase by default, and you can map extra standard events. Eventbrite notes you cannot verify its domain with Meta, so a few Meta features may be unavailable."),
            ("Why does Meta report more ticket purchases than my ticketing platform?",
             "Meta counts purchases within its attribution windows, including one-day view-through and engage-through, so it can credit sales that other channels also claim. Your ticketing platform counts every order once, including ones from email, organic search and the box office. Compare Meta’s click-through purchases with online orders in the ticketing report, and judge overall results on blended cost per order."),
            ("How do I track ticket sales in GA4 when checkout is on another domain?",
             "If you can add your own GA4 tag to the ticketing pages, set up cross-domain measurement under Admin, Data streams, Configure tag settings, Configure your domains, using the same G- tag ID on both sites. If the platform won’t accept your tag, exclude it as a referral, track Buy tickets clicks as an event, and use UTMs plus the platform’s own source reports for sales."),
            ("Can I upload box office or group ticket sales to Meta and Google?",
             "Yes, if you collected contact details with permission. Meta now takes offline events through the main Conversions API, with an action source such as physical_store, and events must be sent within seven days. Google Ads supports offline conversion imports using the Google Click ID, and recommends enhanced conversions for leads set up through Data Manager. A weekly upload is enough for most tours."),
        ],
        "figures": {
            "leak": {
                "type": "funnel",
                "title": "Where tracked ticket purchases go missing",
                "stages": [["Orders in the ticketing report", "1,050"], ["Orders a pixel could see (no blocking)", "about 850"], ["Seen and inside an attribution window", "about 700"], ["Credited to Meta click-through", "about 420"], ["Credited to Google Ads click", "about 240"]],
                "note": "Illustrative example. Gaps vary by platform, audience and setup.",
                "alt": "Funnel showing how event ticket purchases drop out of ad platform tracking, from a Houston and The Woodlands marketing agency",
                "caption": "Platforms overlap, so the bottom rows can add up to more or less than you expect.",
            },
            "questions": {
                "type": "checklist",
                "title": "Ask your ticketing rep before on-sale",
                "sub": "Get the answers in writing",
                "items": ["Can we place Meta, Google Ads and TikTok tags ourselves, or who does?", "Which pages: event page, checkout, confirmation, resale?", "Is there a server-side or Conversions API option?", "Does Purchase pass order value, currency and quantity?", "Is value face value or the all-in total?", "Can we add our own GA4 tag for cross-domain tracking?", "Do UTMs survive into checkout and the source report?", "Can we get daily sales by session and ZIP code?"],
                "alt": "Checklist of ticket tracking questions for Ticketmaster, AXS, Etix and Eventbrite reps, from a Houston and The Woodlands agency",
                "caption": "Ask in the deal stage. After on-sale, changes take longer.",
            },
            "utms": {
                "type": "compare",
                "title": "UTM naming for a tour",
                "left": {"title": "What we usually find", "items": ["Facebook, facebook, FB", "Campaign = Spring Promo", "No city in the link", "Creative name missing", "Links typed by hand"]},
                "right": {"title": "What reports cleanly", "items": ["utm_source=meta, lowercase", "utm_campaign=tour26_tulsa_lastchance", "City and phase in every campaign", "utm_content=dino_reveal_15s", "Links built from one shared sheet"]},
                "alt": "Comparison of messy and clean UTM naming for touring event ticket tracking, from a Houston and The Woodlands agency",
                "caption": f"UTM values are case sensitive in GA4, per {SRC['utm']}.",
            },
            "reconcile": {
                "type": "steps",
                "title": "The weekly reconciliation, per city",
                "sub": "About 20 minutes with a decent sheet",
                "steps": [["Pull ticketing", "Online orders, tickets, gross, box office and group sales."], ["Pull ad platforms", "Spend, click-through purchases and value, same windows."], ["Calculate", "Tracking coverage, blended cost per order, efficiency ratio."], ["Compare to last week", "A coverage drop usually means a broken tag."], ["Decide", "Feed pace and blended cost into the budget rules."]],
                "alt": "Five-step weekly reconciliation of ad platform and ticketing sales for event marketing, from a Houston and The Woodlands agency",
                "caption": "The ticketing report is the source of truth. Ad platforms explain it.",
            },
        },
    },
]
