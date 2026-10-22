"""Batch 7 (agency intent): how to sell more event tickets online (Houston events) and Google Shopping ads for Shopify.

Research: Eventbrite Music Edit 24 via Pollstar (57% of tickets sold a week or less out), Eventbrite help on Meta pixel
(server-side/CAPI token, PageView + Purchase, limits) and GA4 pixel (event_listing, event_register, purchase), Universe help
on Meta pixel + Conversions API, Google Search Central Event structured data, Google Ads location targeting help (1 km
minimum radius, Presence vs Presence or interest), Google Things to do overview, FTC fees rule FAQ (all-in price in ads,
effective May 12, 2025), Barnes & Thornburg alert, Paul Hastings on Texas SB 140 (texts, Sept 1, 2025), NWS lightning
safety for sports/organized events, Jon Loomer on Advantage+ audience and lookalikes.
Shopping: Google Merchant Center help (Google & YouTube app onboarding, misrepresentation policy, GTIN, title, custom
labels, product type vs category, 2025 spec update ending required US tax on July 1, 2025), Shopify help (Google & YouTube
channel, free listings), PPC Land on Merchant Center dropping "Next" (July 2026), Search Engine Land on PMax losing
automatic priority over Standard Shopping and the 10,000 PMax negative keyword limit, Google Ads help on account-level
negatives (1,000 per account) and PMax listing groups, Texas Comptroller sales tax rates.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # post 1
    "pollstar": A("https://news.pollstar.com/2024/06/04/last-minute-ticket-buying-eventbrite-releases-study-at-niva-24/", "Eventbrite data reported by Pollstar"),
    "ebmeta": A("https://support.eventbrite.com/hc/en-us/articles/34863669333650-Add-a-Meta-Pixel-to-your-event", "Eventbrite’s Meta pixel help page"),
    "ebga": A("https://support.eventbrite.com/hc/en-us/articles/34863659861778-Set-up-a-tracking-pixel-with-Google-Analytics", "Google Analytics setup"),
    "universe": A("https://support.universe.com/hc/en-us/articles/360002452312-Use-Facebook-Pixel-on-your-Universe-event", "Universe’s pixel guide"),
    "schema": A("https://developers.google.com/search/docs/appearance/structured-data/event", "Event structured data guidelines"),
    "geo": A("https://support.google.com/google-ads/answer/1722043?hl=en", "location targeting help page"),
    "ttd": A("https://developers.google.com/actions-center/verticals/things-to-do/overview", "Things to do program"),
    "ftcfaq": A("https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions", "FTC’s FAQ on the fees rule"),
    "btlaw": A("https://btlaw.com/en/insights/alerts/2025/ftc-finalizes-junk-fees-rule-new-pricing-disclosure-requirements-take-effect-may-12-2025", "Barnes &amp; Thornburg’s summary"),
    "sb140": A("https://www.paulhastings.com/insights/ph-privacy/marketing-texts-in-texas-sb-140-broadens-state-telemarketing-regulations", "Paul Hastings’ write-up of Texas SB 140"),
    "nws": A("https://www.weather.gov/safety/lightning-sports", "National Weather Service"),
    "loomer": A("https://www.jonloomer.com/how-advantage-plus-audience-works/", "Jon Loomer’s breakdown"),
    "lal": A("https://www.jonloomer.com/meta-ads-lookalike-audiences/", "at least 100 people from a single country"),
    # post 2
    "onboard": A("https://support.google.com/merchants/answer/16267554", "Google’s onboarding guide for the app"),
    "shopifyhelp": A("https://help.shopify.com/en/manual/online-sales-channels/google/getting-setup/connect", "Shopify’s help page"),
    "next": A("https://ppc.land/google-drops-the-next-from-merchant-center-name/", "dropped the “Next” in July 2026"),
    "title": A("https://support.google.com/merchants/answer/6324415", "title attribute"),
    "gtin": A("https://support.google.com/merchants/answer/6324461", "GTIN guidance"),
    "ptype": A("https://support.google.com/merchants/answer/6324436", "product category page"),
    "labels": A("https://support.google.com/merchants/answer/6324473", "custom labels"),
    "misrep": A("https://support.google.com/merchants/answer/6150127", "misrepresentation policy"),
    "tax2025": A("https://support.google.com/merchants/answer/16098264", "2025 product data update"),
    "txtax": A("https://comptroller.texas.gov/taxes/sales/", "Texas Comptroller"),
    "adrank": A("https://searchengineland.com/?p=447646", "Search Engine Land"),
    "pmaxneg": A("https://searchengineland.com/google-ads-expands-negative-keyword-limits-pmax-453154", "raised to 10,000 per campaign"),
    "acctneg": A("https://support.google.com/google-ads/answer/11396330?hl=en", "account-level negative keywords"),
    "listing": A("https://support.google.com/google-ads/answer/11596074?hl=en", "listing groups"),
}

TIX = "/blog/how-to-sell-more-event-tickets-houston/"
SHOP = "/blog/google-shopping-ads-shopify-setup-guide/"

POSTS = [
    # ------------------------------------------------------------------ post 1: event tickets
    {
        "slug": "how-to-sell-more-event-tickets-houston",
        "title": "How to Sell More Event Tickets Online: A Houston Promoter’s Playbook",
        "seo_title": "How to Sell More Event Tickets Online in Houston",
        "desc": "How to sell more event tickets online in Houston: when to spend, Meta and Google settings, ticket pixels, Texas texting rules, all-in pricing and weather.",
        "category": "Paid ads",
        "icons": ["Meta", "Google Ads", "TikTok"],
        "art": "b4",
        "hero": "ticket",
        "hero_alt": "Illustration of event tickets for a guide on how to sell more event tickets online in Houston and The Woodlands",
        "related": ["streaming-tv-ads-worth-it-small-business", "retargeting-explained", "facebook-instagram-ads-local-businesses"],
        "sections": [
            (None, f"""<p>Three weeks out, the dashboard says 38% sold. The promoter refreshes Eventbrite every hour, the venue manager keeps texting, and somebody in the group chat suggests boosting a post. Almost every Houston event we’ve been around hits this exact moment.</p>
<p>The honest answer to how to sell more event tickets online is mostly timing. Spend hard at the announcement and again in the last ten days, keep past buyers warm in between, and make sure Meta and Google can actually see a purchase when one happens. Then give Google enough structured data to show your event to someone typing “things to do this weekend.”</p>
<p>Below are the settings, budget splits, Texas texting law, the FTC pricing rule, and the Houston weather problem nobody puts in the plan. It’s for whoever is on the hook for tickets at exhibitions, family shows, festivals, concert series and holiday light walks.</p>"""),

            ("The ticket sales curve: why the middle weeks feel dead", f"""<p>Ticket sales spike when you announce, bump at the early bird deadline, go quiet for what feels like a month, then surge in the final week. Every promoter knows this. Every promoter panics in week four anyway.</p>
<p>That last-week surge keeps getting bigger. In {SRC['pollstar']}, 57% of US tickets sold from January to April 2024 were bought a week or less before the show. The gap between purchase and event shrank 26% from 2022 to 2024, and the on-sale window shrank 41%. It’s music data, but family events and exhibitions follow the same shape in our experience, since parents decide on Wednesday what Saturday looks like.</p>
<!--fig:pace-->
<!--fig:curve-->
<p>So a slow middle is normal. Spreading budget evenly across the run is where the waste comes from, because week-five money mostly reaches people who’ve already decided to wait.</p>
<p>Hold 40 to 50% of paid media for the last 10 to 14 days. The buyers are there, and so are your biggest retargeting pools.</p>
<p>Then create small spikes in the dead zone with real deadlines, like an early bird price that actually ends, a past-buyer presale, or a group rate that requires booking 14 days out. The lull is also for work that costs hours instead of media dollars: group sales calls, creator content, local press, community calendars.</p>
<p>Multi-week exhibitions run a mini-curve every weekend and a bigger “last chance” rush at the end. Budget them as a series of weekend pushes.</p>"""),

            ("How much to spend on event ads, and when", f"""<p>Start with the event’s own math. Say you’re running a family exhibition in a Houston-area hall for two weekends, and the average order is three tickets at $28, so $84. Willing to spend 20% of gross ticket revenue on ads? Then you can afford about $17 in ad cost per order. If Meta is delivering orders at $25, more budget just loses money faster; fix the campaign first.</p>
<p>For that event we’d split an example $8,000 paid budget roughly like the table below. Your percentages will move. The shape shouldn’t.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Phase</th><th>Timing</th><th>Share of paid</th><th>Main channels</th><th>What to watch</th></tr></thead>
<tbody>
<tr><td>Announce</td><td>Weeks 8 to 6</td><td>15%</td><td>Meta, TikTok, email to past buyers</td><td>Presale signups, add-to-cart rate</td></tr>
<tr><td>Early bird close</td><td>Week 5</td><td>15%</td><td>Meta retargeting, email, Google search on the event name</td><td>Orders before the price change</td></tr>
<tr><td>The lull</td><td>Weeks 4 to 3</td><td>15%</td><td>Group outreach, creators, streaming TV for family shows</td><td>Group inquiries, video views</td></tr>
<tr><td>Final push</td><td>Last 14 days</td><td>45%</td><td>Meta, Google search, retargeting</td><td>Cost per order, daily pace vs goal</td></tr>
<tr><td>Reserve</td><td>Held back</td><td>10%</td><td>Wherever cost per order is lowest</td><td>Weather forecast, sell-through by date</td></tr>
</tbody></table></div>
<p>The reserve line earns its keep in Houston. Forecast turns ugly, and you haven’t spent it. Saturday looks perfect, and it goes into Thursday and Friday, when last-minute buyers make plans.</p>
<p>Under roughly $1,500 in paid media, forget the channel spread and run Meta retargeting, Google search on your event name, and email. Spread $1,200 across five platforms and you get five half-trained campaigns.</p>"""),

            ("How to promote an event on Facebook and Instagram so it sells tickets", f"""<p>Boosting the Facebook event post is the most common move and the weakest one. A boost optimizes for engagement, and people who will never buy a ticket love tapping “Interested.”</p>
<p>Build it in Ads Manager.</p>
<ol><li>Pick the <b>Sales</b> objective, with the Purchase event from your ticketing platform’s pixel as the conversion. (No Purchase event firing? Fix that first; the tracking section below covers it.)</li>
<li>Turn on Advantage+ audience and feed it suggestions. As {SRC['loomer']} explains, custom audiences and lookalikes are suggestions Meta tries first, while location, minimum age and excluded audiences are hard controls. Suggest your past-buyer list plus a 1% lookalike. Meta needs a source of {SRC['lal']} and recommends 1,000 to 5,000 for a useful lookalike.</li>
<li>For single-date shows, exclude people who already bought. For multi-date exhibitions, leave them in. Week-one families come back with the grandparents.</li>
<li>Draw the map by drive time, using zip codes and towns since Meta can’t target drive time directly. A Saturday matinee at the Cynthia Woods Mitchell Pavilion pulls easily from Spring, Conroe, Magnolia, Tomball and Kingwood. A 7 p.m. Friday show there asks a lot of someone in Katy or Pearland. A 25-mile radius looks tidy and ignores I-45 at rush hour.</li></ol>
<p>Small events hit a quieter problem. Meta’s guidance points to roughly 50 optimization events a week to exit learning, and a 400-seat show might sell 60 tickets through ads, total. We’ll often optimize for initiated checkout early and switch to Purchase for the last two weeks. A compromise, but better than a campaign stuck in learning forever.</p>
<p>Honestly, creative moves the needle more than any targeting setting. Vertical video of the real thing (the exhibit floor, the crowd at the chorus, a kid in the light tunnel) beats a flyer, and the date, venue and total price belong in the first two seconds. That’s the kind of work our {'<a href="/services/paid-social-advertising/">paid social team</a>'} does every week.</p>"""),

            ("Google Ads for “[event] near me” and “things to do this weekend”", f"""<p>Google search mostly catches demand your other channels create. Someone sees a poster on Market Street or scrolls past a TikTok, then Googles the name. If a reseller shows up first, you paid to create that search and somebody else cashed it.</p>
<p>Start with an ad group on your event name and its misspellings. Cheapest clicks you’ll ever buy, and they keep resale sites from owning your name. Next, the category: “dinosaur exhibit Houston,” “jazz festival Houston,” “Christmas lights The Woodlands.”</p>
<p>Planner phrases like “things to do in Houston this weekend,” “indoor things to do with kids Houston” and “events near me tonight” get their own ad group. They’re pricier and broader, so we schedule them Wednesday through Saturday only.</p>
<p>Google’s {SRC['geo']} explains “Presence” versus “Presence or interest.” For a concert, the broader option can help by catching the parent in Beaumont or College Station planning a Houston weekend. A neighborhood holiday market should use Presence. Radius targeting needs at least 1 km, so tiny geofences around one venue are out.</p>
<p>Bid on Maximize clicks with a max CPC cap until purchases are tracking, then move to Maximize conversions. We’d skip Performance Max for a one-off event; the show is over before it learns anything.</p>
<p>If you run a touring exhibition with daily time slots, ask your ticketing provider whether it connects to Google’s {SRC['ttd']}, which shows bookable activities through connectivity partners. We haven’t confirmed which platforms qualify. Our {'<a href="/services/search-marketing/">search marketing</a>'} page covers how we run Google Ads more broadly.</p>"""),

            ("TikTok and streaming TV for events: when each is worth it", f"""<p>TikTok earns its spot for concerts, festivals, nightlife and anything aimed at people under 35. The ads that sell look like regular posts, say a creator walking the venue or a shaky clip of last year’s crowd. Spark Ads put paid budget behind a creator’s own post, which people trust more than your brand account.</p>
<p>Check whether your ticketing platform can pass purchases to TikTok. If it can’t, judge TikTok by the lift in branded searches and sales during flights. TikTok chews through creative fast, so plan new videos every week or two in the final month.</p>
<p>Streaming TV is worth a real look for family events. A 15-second spot on a streaming app reaches the whole household on the couch, targeted by zip code. Our full take is in {'<a href="/blog/streaming-tv-ads-worth-it-small-business/">whether streaming TV ads are worth it</a>'}. For events, our rule of thumb: total paid media over about $10,000, and a run of two weekends or more so awareness has time to turn into searches. A single-night club show? Keep that money on Meta.</p>
<p>Whichever you run, check branded search volume every few days. It’s the cheapest read on whether either channel is doing anything.</p>"""),

            ("Email and texts to past attendees (and the Texas consent rules)", f"""<p>Your best audience already bought from you once. Per dollar, a past-buyer list outsells every paid channel, yet most promoters email it twice per event. We’d send four.</p>
<ol><li>A presale invite with a code, 48 hours before the public on-sale.</li>
<li>An early bird reminder the day before the price goes up.</li>
<li>Something worth opening in the lull, like a behind-the-scenes video, set times or the parking plan.</li>
<li>A final-week note. “Saturday is close to sold out” goes in only if it’s true, along with weather and parking details.</li></ol>
<p>Texts convert even better, and they come with real legal risk. Federal law (the TCPA) generally requires prior express written consent before you send marketing texts using automated systems, so text only people who opted in to texts specifically. Buying a ticket isn’t the same as opting in.</p>
<p>Texas tightened things too. According to {SRC['sb140']}, the law took effect September 1, 2025, brought text messages under the state’s telephone solicitation rules, added a registration requirement with penalties up to $5,000 per violation, and lets consumers sue under the Texas Deceptive Trade Practices Act. The write-up notes an exemption for texts to current or former customers. Whether your list fits it is a question for your lawyer, and we’d ask before the first blast, not after.</p>
<p>People who visited the ticket page and didn’t buy can be followed up with retargeting ads, which carry no consent risk. Our explainer on {'<a href="/blog/retargeting-explained/">how retargeting works</a>'} covers the basics.</p>"""),

            ("Tracking ticket sales: pixels on Eventbrite, Universe and Ticketmaster", f"""<p>Most promoters get this part wrong, and it quietly undoes everything above. If Meta can’t see purchases, it goes looking for the wrong people. Per their help pages, the major platforms support the following.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform</th><th>Meta</th><th>Google</th><th>Watch out for</th></tr></thead>
<tbody>
<tr><td>Eventbrite</td><td>Pixel fires PageView and Purchase by default; server-side tracking with a Conversions API token</td><td>GA4 sends event_listing, event_register and purchase; separate Google Ads conversion setup</td><td>Can’t verify Eventbrite’s domain with Meta; pixels don’t catch every purchase</td></tr>
<tr><td>Universe</td><td>Pixel plus optional Conversions API; sends viewed tickets, added tickets and purchase with order value</td><td>Check current integrations tab</td><td>Embedded widgets on your own site need the pixel base code in your header</td></tr>
<tr><td>Ticketmaster</td><td colspan="2">Depends on the venue’s or promoter’s account and contract</td><td>Ask your Ticketmaster rep what you can place before you plan media</td></tr>
</tbody></table></div>
<p>Sources: {SRC['ebmeta']}, its {SRC['ebga']} article and {SRC['universe']}. Eventbrite admits that “tracking pixels aren’t able to track every purchase” and that GA4 purchase data misses refunds and manual transactions. Reconcile against your sales report weekly.</p>
<!--fig:tracking-->
<p>Then test it the boring way. Create a hidden $1 ticket type, buy one yourself through an ad click, and watch the Test Events tab in Meta Events Manager alongside Google’s Tag Assistant. Refund yourself after. Tedious, yes. Also the single most useful thing in this post.</p>"""),

            ("Getting your event into Google’s event listings", f"""<p>Search “things to do in Houston this weekend” and Google often shows an events panel. Getting in is mostly a structured data job.</p>
<p>Google’s {SRC['schema']} require three properties: <i>name</i>, <i>startDate</i> (with date and time) and <i>location</i> with a venue name and address. Recommended properties include <i>offers</i> with price, currency, availability, a <i>validFrom</i> on-sale date and a ticket <i>url</i>, plus <i>eventStatus</i>, <i>image</i>, <i>organizer</i> and <i>performer</i>. A few rules trip people up:</p>
<ul><li>Mark up one event per page, not a schedule page listing many.</li>
<li>The event must be open to the public and at a physical place. Invite-only and virtual events aren’t eligible.</li>
<li>If your listing lives on a ticketing site that already works with Google’s event search, Google says that listing can carry you. Mark up your own page anyway.</li>
<li>When plans change, update <i>eventStatus</i>: EventCancelled, EventPostponed (new date unknown) or EventRescheduled (with the new <i>startDate</i> and an optional <i>previousStartDate</i>).</li></ul>
<p>While you’re at it, add an Event post with the ticket link to the venue’s Google Business Profile, and submit to the community calendars locals actually read. Both are free.</p>"""),

            ("Pricing, scarcity and group sales (with the FTC’s all-in rule)", f"""<p>Since May 12, 2025, the FTC’s fees rule has required the total ticket price, mandatory fees included, upfront and more prominent than any partial price ({SRC['btlaw']}). The {SRC['ftcfaq']} says it covers “any business that offers, displays, or advertises live-event tickets,” venues included, and that ads with pricing must give the total. You can advertise the lowest general admission total “only if people can actually buy tickets at that price.” Taxes may be left out of the upfront figure as long as they’re disclosed before payment.</p>
<p>If your ad says “Tickets from $25,” then $25 had better be the all-in price of a ticket someone can buy. Check ad copy and email subject lines first.</p>
<p>For family events we like published price tiers (early bird, general, final) better than algorithmic surge pricing. Surge can work for a hot concert. A parent who watches the price jump overnight posts about it in the neighborhood Facebook group.</p>
<p>Scarcity works when it’s true. “Only 60 tickets left for the 2 p.m. Saturday slot” is honest if your ticketing report says 60. Countdown timers that reset cost you the repeat crowd.</p>
<p>Group sales are the most underused tool in the lull. Churches, PTOs, scout troops, youth sports teams and company outings (Energy Corridor HR teams love a family day) buy in tens and twenties. Put up a group page with a 10-ticket rate and a short form, and answer within a day. Two afternoons of calls to youth sports leagues can outsell a week of ads.</p>"""),

            ("Houston weather: plan for the storm before you sell the ticket", f"""<p>Hurricane season runs June 1 to November 30. A summer afternoon can go from clear to lightning in an hour. Beryl knocked out power across the region in July 2024. Late buyers (that 57% again) check the forecast first, so your weather plan is a marketing document too.</p>
<p>The {SRC['nws']} says people “should wait at least 30 minutes after the last thunder before resuming outdoor activities,” that organized events should “have a lightning safety plan and follow it without exception,” and that organizers should consider canceling or postponing when thunderstorms are forecast.</p>
<!--fig:weather-->
<p>Indoor events get to play the other side of this. Air conditioning in August is a selling point in Houston, and so is a roof on a rainy Saturday. Build a “rainy weekend” ad set around searches like “indoor things to do Houston” and leave it paused until the forecast turns.</p>"""),

            ("Where to start this week, and when to get help", f"""<p>Before your next on-sale, buy a $1 test ticket and confirm Purchase shows up in Meta and Google. Then load your past-buyer list into a custom audience and an email presale. If there’s time left over, move half your remaining budget into the final 14 days.</p>
<p>Plenty of promoters run all of this themselves, especially with under about $2,000 in ads and one platform to manage. Help starts to pay for itself when you’re running several events a quarter, or spending enough that a 20% swing in cost per order is real money. Same if the tracking is so tangled nobody trusts the numbers. Our {'<a href="/industries/live-entertainment/">live entertainment</a>'} page shows the kind of work we do for venues and promoters.</p>
<p>If you’re mid-campaign and the numbers feel off, our free Ad Spend Leak Check is a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours. {'<a href="/contact/">Request one here</a>'}. It’s far more useful before the final push than after it.</p>"""),
        ],
        "faq": [
            ("How far in advance should you start promoting an event?",
             "For most local concerts and family events, six to eight weeks of promotion is plenty, with the heaviest spending in the final ten to fourteen days. Festivals and touring exhibitions can announce months out, but should still save a big share of budget for the end, when most tickets sell."),
            ("How much should I spend on ads to sell event tickets?",
             "Work backward from your average order. Decide what share of gross ticket revenue can go to ads, often 10 to 25 percent, and apply it per order. A family show with $84 orders and a 20 percent ad share can afford about $17 per order. If ads cost more than that, fix tracking, creative or targeting before adding budget."),
            ("Why are my event ticket sales slow?",
             "Usually it is normal. Sales spike at announcement, go quiet in the middle weeks and surge in the last one. If you are close to the date and still behind, check that your pixel records purchases, that ads show the all-in price, that past buyers got a presale, and that you target people within a realistic drive."),
            ("Is Facebook or Google better for selling event tickets?",
             "They do different jobs. Meta and Instagram create demand by showing the event to people who were not looking for it. Google search catches people already searching your event name or things to do this weekend. Most events need both, with Meta getting more budget early and branded Google search running the whole time."),
            ("Can I text past attendees about my next event?",
             "Only if they agreed to receive marketing texts from you. Federal rules generally require prior express written consent for automated marketing texts, and Texas SB 140, effective September 1, 2025, brought texts under state telephone solicitation rules, with registration and lawsuit risk. Email past buyers, text only opted-in contacts, and ask a lawyer about the Texas exemptions."),
        ],
        "figures": {
            "curve": {
                "type": "columns",
                "title": "A typical ticket sales curve",
                "sub": "Share of total sales by week before a hypothetical Houston event",
                "labels": ["Wk 8", "Wk 7", "Wk 6", "Wk 5", "Wk 4", "Wk 3", "Wk 2", "Final"],
                "values": [9, 4, 3, 8, 3, 4, 12, 57],
                "highlight": [0, 3, 7],
                "y_label": "% of tickets",
                "note": "Illustrative example; final-week share matches Eventbrite’s 57% figure",
                "alt": "Column chart of a typical ticket sales curve, showing how to sell more event tickets in Houston with the final-week surge",
                "caption": f"Announcement, early bird deadline, then the final-week surge. The 57% final week comes from {A('https://news.pollstar.com/2024/06/04/last-minute-ticket-buying-eventbrite-releases-study-at-niva-24/', 'Eventbrite via Pollstar')}.",
            },
            "pace": {
                "type": "stats",
                "title": "Ticket buyers are waiting longer",
                "stats": [["57%", "Of tickets bought a week or less before the show"], ["26%", "Shorter gap from purchase to show, 2022 to 2024"], ["41%", "Shorter on-sale window, 2022 to 2024"]],
                "note": "Source: Eventbrite Music Edit 24, US data Jan to Apr 2024, via Pollstar",
                "alt": "Stat tiles showing late ticket buying trends, context for selling more event tickets online in Houston",
                "caption": f"From {A('https://news.pollstar.com/2024/06/04/last-minute-ticket-buying-eventbrite-releases-study-at-niva-24/', 'Pollstar’s report on Eventbrite data')}. Budget for the last week, not the average week.",
            },
            "tracking": {
                "type": "checklist",
                "title": "Ticket tracking check before you spend",
                "sub": "Run this before any paid campaign goes live",
                "items": [
                    "Meta pixel added in the ticketing platform",
                    "Conversions API token added where supported",
                    "Purchase event shows order value",
                    "GA4 or Google Ads conversion receiving purchases",
                    "Hidden $1 test ticket bought through an ad click",
                    "Test purchase visible in Events Manager",
                    "Sales report reconciled with ad platform weekly",
                    "UTM tags on every ad, email and creator link",
                ],
                "alt": "Checklist for ticket pixel and conversion tracking before running ads to sell event tickets in Houston",
                "caption": f"Based on {A('https://support.eventbrite.com/hc/en-us/articles/34863669333650-Add-a-Meta-Pixel-to-your-event', 'Eventbrite')} and {A('https://support.universe.com/hc/en-us/articles/360002452312-Use-Facebook-Pixel-on-your-Universe-event', 'Universe')} help pages.",
            },
            "weather": {
                "type": "steps",
                "title": "A weather plan buyers can see",
                "sub": "For outdoor events in Greater Houston",
                "steps": [
                    ["Publish the policy at on-sale", "State rain, lightning and reschedule rules on the ticket page and in the FAQ."],
                    ["Watch the 5-day forecast", "Hold the 10% reserve until you know which way the weekend is going."],
                    ["Prewrite every message", "Delay, reschedule and cancel versions for email, SMS opt-ins and social."],
                    ["Pause ads and update schema", "Stop spend fast and set eventStatus so Google shows the change."],
                    ["Follow the 30-minute rule", "Resume only 30 minutes after the last thunder, per the NWS."],
                ],
                "alt": "Step-by-step outdoor event weather plan for promoters selling event tickets in Houston and The Woodlands",
                "caption": f"Lightning guidance from the {A('https://www.weather.gov/safety/lightning-sports', 'National Weather Service')}.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: Google Shopping for Shopify
    {
        "slug": "google-shopping-ads-shopify-setup-guide",
        "title": "Google Shopping Ads for Shopify: Setup, Feed Fixes and PMax vs Standard",
        "seo_title": "Google Shopping Ads for Shopify: Setup & Feed Guide",
        "desc": "Google Shopping ads for Shopify, explained: Merchant Center setup, feed fixes, disapprovals, Performance Max vs Standard Shopping, ROAS targets and budgets.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Google", "Google Analytics"],
        "art": "b5",
        "hero": "cart",
        "hero_alt": "Illustration of a shopping cart for a guide to Google Shopping ads for Shopify stores in Houston and beyond",
        "related": ["performance-max-vs-search-campaigns-local", "small-business-guide-google-ads-2026", "how-fast-should-your-website-load"],
        "sections": [
            (None, f"""<p>You installed the Google &amp; YouTube app, clicked through the setup, let it build a Performance Max campaign, and spent $1,100 in a month. Shopify shows four orders from Google. Two of them were people who searched your brand name and would have bought anyway.</p>
<p>We hear that story from Shopify owners more than any other. It’s fixable.</p>
<p>Google Shopping ads for Shopify run on a simple chain. The Google &amp; YouTube app sends your products to Google Merchant Center, which turns them into free listings and ad inventory, and then a Performance Max or Standard Shopping campaign in Google Ads decides which products show and what you pay per click. By the time you set a bid, most of the outcome has already been decided by your product feed and your conversion tracking.</p>
<p>We’ll go through setup and the feed fields that matter, then the disapprovals that stall new stores, the Performance Max vs Standard Shopping question, and the margin math behind a ROAS target that actually makes money.</p>"""),

            ("How Google Shopping works for a Shopify store (and what’s free)", f"""<p>It helps to keep the pieces separate in your head.</p>
<p>Google Merchant Center holds the product data (titles, prices, images, availability, shipping and return policies). Google spent two years calling the rebuilt version “Merchant Center Next,” then {SRC['next']}, so older tutorials won’t always match what you see on screen. It’s the same tool.</p>
<p>Free listings come first. According to {SRC['shopifyhelp']}, eligible US stores’ synced products can show in Google Shopping tab listings at no cost. They won’t carry a store on their own. They will show you which products Google likes before you spend a dollar, which is worth a lot.</p>
<p>Paid Shopping ads run from Google Ads, in a Standard Shopping campaign or Performance Max, and both pull from the same Merchant Center feed. A bad feed sinks both.</p>
<p>Location barely matters, which is part of the appeal. A candle maker in Tomball and a western boot shop in Conroe are in the same national auction as everyone else, and they win or lose on price, product data, images and page speed. (If your product pages take five seconds on a phone, read {'<a href="/blog/how-fast-should-your-website-load/">our page speed guide</a>'} before you spend.)</p>"""),

            ("Google Merchant Center setup on Shopify, step by step", f"""<p>Google’s {SRC['onboard']} lays out the sequence, summarized below.</p>
<!--fig:setup-->
<p>The steps themselves are easy. These details are what actually hang people up.</p>
<ul><li>The storefront password. Google can’t review a store it can’t see, and stores still in pre-launch mode fail here constantly.</li>
<li>Missing policies. Publish a refund policy, terms of service and contact details before you start, because the app checks.</li>
<li>Agency leftovers. Google says multi-client accounts (MCAs) can’t link to the app, so if an old agency set you up under their MCA, you may need a fresh <b>standalone Merchant Center</b> account.</li>
<li>Conversion mapping. Once the app is linked to Google Ads, it lists Shopify’s standard events (purchase, add_to_cart, begin_checkout) and lets you map each to a conversion action. Turn on Enhanced Conversions while you’re in there.</li>
<li>Shipping that doesn’t match. If checkout charges $8.95 and Merchant Center says free shipping, expect a mismatch warning.</li></ul>
<p>Texas sellers can get ahead of one more shipping headache. Set a realistic handling time and bump it during hurricane season if carriers stall. A missed delivery estimate turns into a refund request, and a pile of those turns into a review problem on Google.</p>"""),

            ("Product feed optimization: titles, GTIN, product_type and custom labels", f"""<p>Most Shopify stores skip this part, and it’s where we usually find the most money. Shopping has no keywords; Google matches searches against your product data. Your feed is your keyword list, whether you treat it like one or not.</p>
<h3>Titles</h3>
<p>The {SRC['title']} allows up to 150 characters, and Google notes shoppers usually see only the first 70 or fewer. Lead with the words people search, starting with brand (if anyone searches it) and product type, then whatever separates one variant from the next, like material, size, color or count. “Willow Tote” tells Google almost nothing. “Large Leather Tote Bag, Cognac, Zip Top, 15 in Laptop Pocket” matches a dozen real searches.</p>
<!--fig:titles-->
<h3>GTIN</h3>
<p>If a product has a manufacturer barcode, submit it. Google’s {SRC['gtin']} says products with missing or incorrect GTINs “may have limited visibility,” and a product could be disapproved if a GTIN exists and you leave it off. Handmade or private-label goods without one? Leave the field blank. Never make a number up. In Shopify, the variant’s barcode field is where this usually lives.</p>
<h3>product_type and google_product_category</h3>
<p>Google’s {SRC['ptype']} explains that <i>google_product_category</i> uses Google’s fixed taxonomy, while <i>product_type</i> is your own classification, such as “Home &gt; Candles &gt; Soy Candles.” Product types can be subdivided up to five levels in campaign {SRC['listing']}, which makes them the cleanest way to split bids and budgets by category.</p>
<h3>Custom labels</h3>
<p>You get five {SRC['labels']} (custom_label_0 to custom_label_4), each with up to 1,000 unique values. Shoppers never see them; they’re there so you can group products inside campaigns. On almost every store we set a margin band first (high, mid, low), because that’s the label that drives bidding.</p>
<p>After that, a few more earn their slots:</p>
<ul><li>price band, such as under $25, $25 to $75 and over $75</li>
<li>season (holiday, summer, evergreen)</li>
<li>performance, where we sort products into hero, steady and “zombie,” our name for the ones that never get an impression</li>
<li>clearance or promo, if you run sales often enough to care</li></ul>
<p>Margin data doesn’t live in a standard Shopify field. You’ll add these labels with a feed app, a supplemental feed (a plain Google Sheet works fine) or Merchant Center rules.</p>"""),

            ("Merchant Center disapprovals: misrepresentation, shipping and returns", f"""<p>“Misrepresentation” is the suspension new stores get more than any other, and the notice almost never says why. Google’s {SRC['misrep']} sets out the general rules. You need a real business identity and contact details and a return policy you honor. The full cost has to be shown (taxes, fees, shipping, return shipping), delivery timelines have to be clear, and you can only list what you can actually fulfill.</p>
<p>Egregious violations can mean suspension without warning. For most others Google sends a warning email and gives you 7 or 28 days to fix things, and account reviews typically take about 7 business days. Requesting review before everything is fixed just burns an appeal.</p>
<!--fig:disapprovals-->
<p>Sales tax used to trip people up here too. Since July 1, 2025, Google’s {SRC['tax2025']} says US merchants are no longer required to submit sales tax in the feed or Merchant Center tax settings. You still have to collect it properly at checkout. For in-state basics, the {SRC['txtax']} sets the state rate at 6.25%, local jurisdictions can add up to 2%, and the combined maximum is 8.25%. Get a Texas sales tax permit and set up Shopify Tax (or your accountant’s preferred method) before launch. Remote-seller rules in other states are a separate conversation for your CPA.</p>"""),

            ("Performance Max vs Standard Shopping for Shopify stores", f"""<p>Every ecommerce forum is arguing about this. The honest answer depends on budget and on how much you trust your conversion data. (We covered the local-business version in {'<a href="/blog/performance-max-vs-search-campaigns-local/">Performance Max vs Search campaigns</a>'}.) For Shopify stores, the two compare like so.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Standard Shopping</th><th>Performance Max</th></tr></thead>
<tbody>
<tr><td>Where ads show</td><td>Shopping results and Shopping tab</td><td>Shopping plus YouTube, Display, Gmail, Discover and Search</td></tr>
<tr><td>Control</td><td>Manual CPC by product group, or campaign-level Target ROAS; full search terms report</td><td>Campaign-level Target ROAS; partial search term insights</td></tr>
<tr><td>Data it needs</td><td>Works with thin data</td><td>Wants steady conversion volume</td></tr>
<tr><td>Best fit</td><td>New stores, tight budgets, testing which products sell</td><td>Stores with clean tracking and dozens of conversions a month</td></tr>
<tr><td>Risk</td><td>More hands-on work</td><td>Spend drifts to brand searches and remarketing that look great but add little</td></tr>
</tbody></table></div>
<p>Since October 2024, Performance Max no longer automatically beats Standard Shopping when both campaigns carry the same products. As {SRC['adrank']} reported, Ad Rank decides now, which makes running the two side by side far more workable than it used to be.</p>
<p>For a new Shopify store we start with Standard Shopping on the best 20 to 50 products, split by product_type or margin label, and stay there until purchases reach 30 or more a month. Only then do we test Performance Max, and only on products that have already proven themselves.</p>
<p>When we do run PMax, we often start it feed-only, meaning an asset group with product listing groups and no uploaded videos or images, so spend leans toward Shopping placements. Two caveats. Google may still auto-create assets unless you switch off automatically created assets, and “feed-only” is a practitioner setup rather than an official campaign type. Look at placement reports after two weeks.</p>"""),

            ("Setting a ROAS target from your margins", f"""<p>ROAS is revenue divided by ad spend, so a 4x ROAS means $4 in sales per $1 in ads. Whether that’s good depends entirely on your margin. Most stores we look at set their target by copying a number they heard on a podcast.</p>
<p>Break-even ROAS equals 1 divided by your gross margin (after product cost, shipping you pay, payment fees and typical returns). At a 40% margin, every $100 sale leaves $40 to cover ads, so $40 of ad spend per $100 of revenue is break-even, which is a 2.5x ROAS. Anything below that loses money on the first order.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Gross margin after costs</th><th>Break-even ROAS</th><th>Target for 10% profit</th><th>Target for 20% profit</th></tr></thead>
<tbody>
<tr><td>25%</td><td>4.0x</td><td>6.7x</td><td>20x (unrealistic)</td></tr>
<tr><td>40%</td><td>2.5x</td><td>3.3x</td><td>5.0x</td></tr>
<tr><td>50%</td><td>2.0x</td><td>2.5x</td><td>3.3x</td></tr>
<tr><td>60%</td><td>1.7x</td><td>2.0x</td><td>2.5x</td></tr>
<tr><td>70%</td><td>1.4x</td><td>1.7x</td><td>2.0x</td></tr>
</tbody></table></div>
<p>The formula for a profit target is 1 divided by (margin minus desired profit share). At 40% margin and a 10% profit goal, that’s 1 ÷ 0.30, or 3.3x.</p>
<!--fig:roas-->
<p>Look at the 25% row. Low-margin products, mostly resold name brands, are brutal on Shopping because the big retailers bid on the same GTINs. We’d bid those down or drop them and push budget toward high-margin items. That’s what the margin label was for.</p>
<p>There’s one exception we’ll defend. If repeat purchase rates are strong (consumables, coffee, skincare), you can accept a first-order ROAS near break-even, because the second order is where the profit lives. Know your repeat rate before you make that bet.</p>"""),

            ("Negative keywords in Shopping and Performance Max", f"""<p>Shopping doesn’t target with keywords, but you can still block searches, and you should.</p>
<p>Start at the account level. Google’s {SRC['acctneg']} apply across Search, Performance Max, Shopping and other campaign types, up to 1,000 per account, under Admin, then Account settings, then Negative keywords. That’s the home for “free,” “DIY,” “pattern,” “used,” “jobs” and any competitor names you never want to pay for.</p>
<p>Performance Max campaigns also take their own negatives now; the limit was {SRC['pmaxneg']}, matching Search. Use those for campaign-specific exclusions, like keeping brand terms out of a prospecting campaign. Standard Shopping takes negatives the normal way, and its full search terms report makes them easy to find.</p>
<p>Every Monday, sort search terms by cost with zero conversions and add anything irrelevant as a negative. Ten minutes, tops. Our {'<a href="/blog/small-business-guide-google-ads-2026/">small business Google Ads guide</a>'} covers match types if negatives are new to you.</p>
<p>Decide on purpose whether Shopping should spend on your own brand name. Brand searches convert well and inflate ROAS, so a mediocre campaign can look great on paper. We usually give brand its own budget, which makes it obvious what the non-brand work is really doing.</p>"""),

            ("Shopify Google Ads not working? A diagnostic table", f"""<p>When an owner says their Shopify Google Ads aren’t working, it’s almost always something in this table. Work top to bottom, because the early problems hide the later ones.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Symptom</th><th>Likely cause</th><th>Where to check</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Few or no impressions</td><td>Products disapproved or limited</td><td>Merchant Center, Products, needs attention</td><td>Fix the top issues by product count first</td></tr>
<tr><td>Conversions in Ads don’t match Shopify</td><td>Purchase counted twice (app tag plus GA4 import both set as primary)</td><td>Google Ads, Goals, Summary</td><td>Keep one purchase action as primary, others secondary</td></tr>
<tr><td>Great ROAS, flat sales</td><td>Spend going to brand searches and returning visitors</td><td>Search terms, Insights</td><td>Split brand, add brand negatives to prospecting</td></tr>
<tr><td>Clicks but no sales</td><td>Price uncompetitive or slow mobile pages</td><td>Price competitiveness report, PageSpeed</td><td>Reprice or exclude losers; fix page speed</td></tr>
<tr><td>Spend on a few products only</td><td>Google favoring items with history</td><td>Product-level report</td><td>Separate campaign or listing group for neglected winners</td></tr>
<tr><td>Account suspended</td><td>Misrepresentation, missing policies</td><td>Merchant Center, Account issues</td><td>Fix site policies and contact info, then request review once</td></tr>
</tbody></table></div>
<p>Row two is the one we’d check first. Many stores have the Shopify app’s purchase conversion and an imported GA4 purchase both set as primary goals, so Google counts two sales for every real one. Reported ROAS doubles. Target ROAS bidding gets confused, and the owner scales a campaign that was never profitable. While you’re in there, check what “value” means. If the conversion value includes shipping and tax, your real ROAS is lower than the report says, so set targets from the same definition.</p>"""),

            ("What to budget for Google Shopping, and when to get help", f"""<p>Budget follows margin and price point. As a rule of thumb (ours, not Google’s), a campaign needs enough daily budget to buy several conversions a week at your target cost, or bidding never has data to learn from. If your average order is $60 and you’re aiming for a 3x ROAS, each order can cost about $20 in ads. Ten orders a week means roughly $200 a week, or about $30 a day, as a realistic floor for one campaign.</p>
<p>Give a new Standard Shopping setup 30 to 45 days before making big calls. Week one tells you about feed problems. Weeks three through six tell you about products.</p>
<p>A Shopify owner can absolutely run this alone with a clean feed, verified tracking and an hour a week on search terms. We’d bring in help once spend passes a few thousand a month or the catalog is big enough that feed work becomes a project. Broken tracking, where nobody knows which number to believe, is the other good reason. Our {'<a href="/industries/ecommerce/">ecommerce</a>'} page and {'<a href="/services/search-marketing/">search marketing</a>'} page describe how we handle those accounts.</p>
<p>Campaigns already running and something feels off? Our free Ad Spend Leak Check is a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours. {'<a href="/contact/">Request it here</a>'}. Double-counted conversions are usually the first thing we look for.</p>"""),
        ],
        "faq": [
            ("How do I set up Google Shopping ads on Shopify?",
             "Install the Google and YouTube app from the Shopify App Store, link a standalone Merchant Center account, remove your store password, publish refund and terms policies, verify your phone, and choose country, language and shipping. Once products are approved, connect Google Ads in the app, map the purchase conversion, then build a Standard Shopping or Performance Max campaign."),
            ("Are Google Shopping free listings really free?",
             "Yes. Once your Shopify products sync to Merchant Center and are approved, eligible US stores can appear in the Shopping tab without paying per click. Traffic is usually modest compared with paid ads, but free listings cost nothing, help reveal which products Google matches well, and use the same feed, so fixing your feed improves free and paid results together."),
            ("Should I use Performance Max or Standard Shopping?",
             "New stores and small budgets usually do better starting with Standard Shopping, which gives full search term data and tighter control. Performance Max tends to work once you have clean conversion tracking and steady purchase volume, roughly 30 or more a month. Since October 2024, Ad Rank decides between them when both carry the same products, so running both is practical."),
            ("What is a good ROAS for Google Shopping?",
             "It depends on your margin. Break-even ROAS equals one divided by your gross margin after product cost, shipping, fees and returns. At a 50 percent margin, break-even is 2x and a 3.3x ROAS leaves roughly 20 percent profit. At a 25 percent margin you need 4x just to break even, so a store-wide average target is rarely the right answer."),
            ("Why are my Shopify products disapproved in Google Merchant Center?",
             "The usual causes are missing or mismatched shipping costs, prices that differ between feed and site, missing GTINs for branded products, image problems, and missing refund policy or contact details that trigger misrepresentation reviews. Check Merchant Center’s needs attention list, fix the issues affecting the most products first, and request review only once everything is corrected."),
        ],
        "figures": {
            "setup": {
                "type": "steps",
                "title": "Shopify to Google Shopping setup",
                "sub": "The order that avoids most first-week errors",
                "steps": [
                    ["Install the Google & YouTube app", "From the Shopify App Store, using a Google login with admin rights."],
                    ["Link a standalone Merchant Center", "Multi-client accounts can’t link to the app."],
                    ["Fix the store basics", "Remove the password; add refund policy, terms and contact info."],
                    ["Verify, then set shipping", "Confirm the business phone; match shipping costs to checkout."],
                    ["Connect Google Ads and conversions", "Map purchase, add_to_cart and begin_checkout; enable Enhanced Conversions."],
                ],
                "alt": "Steps for setting up Google Shopping ads for Shopify through the Google and YouTube app and Merchant Center",
                "caption": f"Based on {A('https://support.google.com/merchants/answer/16267554', 'Google’s Merchant Center onboarding guide')} for the Shopify app.",
            },
            "titles": {
                "type": "compare",
                "title": "Shopping titles: weak vs strong",
                "left": {"title": "Titles Google can’t match", "items": ["Willow Tote", "The Classic", "Best Seller Candle", "New! Summer Dress"]},
                "right": {"title": "Titles that match searches", "items": ["Large Leather Tote Bag, Cognac, Zip Top", "Men’s Western Work Boot, Square Toe, Size 10", "Soy Candle, Cedar & Sage, 12 oz, 60 Hr Burn", "Linen Midi Dress, Sage Green, Women’s M"]},
                "alt": "Comparison of weak and strong product titles for Google Shopping ads on Shopify stores",
                "caption": f"Google’s {A('https://support.google.com/merchants/answer/6324415', 'title guidance')}: up to 150 characters, but shoppers usually see 70 or fewer, so front-load.",
            },
            "disapprovals": {
                "type": "checklist",
                "title": "Before you request a Merchant Center review",
                "sub": "Common causes of misrepresentation and policy flags",
                "items": [
                    "Refund policy published and linked in the footer",
                    "Phone, email and address visible on the site",
                    "Shipping costs match between feed and checkout",
                    "Return shipping cost stated clearly",
                    "Delivery times listed before checkout",
                    "Feed prices match product pages",
                    "Out-of-stock items marked out of stock",
                    "No borrowed brand logos or fake trust badges",
                ],
                "alt": "Checklist for fixing Google Merchant Center disapprovals before running Google Shopping ads on Shopify",
                "caption": f"Built from Google’s {A('https://support.google.com/merchants/answer/6150127', 'misrepresentation policy')}.",
            },
            "roas": {
                "type": "bars",
                "title": "Break-even ROAS by gross margin",
                "sub": "Below these numbers, the first order loses money",
                "items": [["25% margin", 4.0, "4.0x"], ["40% margin", 2.5, "2.5x"], ["50% margin", 2.0, "2.0x"], ["60% margin", 1.67, "1.7x"], ["70% margin", 1.43, "1.4x"]],
                "highlight": [1],
                "note": "Calculated: break-even ROAS = 1 ÷ gross margin",
                "alt": "Bar chart of break-even ROAS by gross margin for Google Shopping ads on Shopify stores",
                "caption": "Margin means after product cost, shipping you pay, payment fees and typical returns.",
            },
        },
    },
]
