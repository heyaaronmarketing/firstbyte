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
    "ebmeta": A("https://support.eventbrite.com/hc/it/articles/34863669333650-Add-a-Meta-Pixel-to-your-event", "Eventbrite’s Meta pixel help page"),
    "ebga": A("https://support.eventbrite.com/hc/it/articles/34863659861778-Set-up-a-tracking-pixel-with-Google-Analytics", "Google Analytics setup"),
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
<p>If you want to know how to sell more event tickets online, the short answer is that timing beats tactics. Spend hard at the announcement and again in the last ten days, keep past buyers warm in between, make sure Meta and Google can actually see a purchase, and give Google enough structured information to show your event to someone typing “things to do this weekend.” Everything below is the how: settings, budget splits, the Texas texting rules, the FTC’s pricing rule, and the Houston weather problem nobody writes into the plan.</p>
<p>This is for the people selling the tickets: touring exhibitions, family shows, festivals, concert series, holiday light walks. We’ll flag where the mechanics differ.</p>"""),

            ("The ticket sales curve: why the middle weeks feel dead", f"""<p>Ticket sales don’t climb in a straight line. They spike when you announce, bump again at the early bird deadline, go quiet for what feels like forever, then surge in the final week. Promoters know this, and panic anyway.</p>
<p>The last-week surge has also gotten bigger. In {SRC['pollstar']}, 57% of US tickets sold from January to April 2024 were bought a week or less before the show. The gap between purchase date and event date shrank 26% from 2022 to 2024, and the window between on-sale and show date shrank 41%. That was music data, but we see the same shape on family events and exhibitions. Parents decide on Wednesday what Saturday looks like.</p>
<!--fig:pace-->
<!--fig:curve-->
<p>A slow middle is normal. Spending evenly across the run is how budgets get wasted, since week-five money mostly reaches people who already decided to wait.</p>
<p>What we’d do instead:</p>
<ul><li><b>Create real deadlines.</b> An early bird price that actually ends, a past-buyer presale, a group rate that requires booking 14 days out. Each one makes a small spike in the dead zone.</li>
<li><b>Hold 40 to 50% of paid media for the last 10 to 14 days.</b> That’s where the buyers are, and that’s when your retargeting pools are biggest.</li>
<li><b>Fill the lull with cheap work.</b> Group sales calls, email, creator content, local press and community calendars cost time, not media dollars.</li></ul>
<p>Multi-week exhibitions differ a little: a mini-curve every weekend, then a bigger “last chance” rush at the end. Budget them as weekend pushes.</p>"""),

            ("How much to spend on event ads, and when", f"""<p>Start from the math of the event. Say you’re running a family exhibition in a Houston-area hall for two weekends, with an average order of three tickets at $28 each. That’s $84 an order. If you’re willing to spend 20% of gross ticket revenue on ads, you can afford about $17 in ad cost per order. If Meta delivers orders at $25, fix that before raising the budget.</p>
<p>Here’s how we’d split an example $8,000 paid budget for that event. Your percentages will move, but the shape shouldn’t.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Phase</th><th>Timing</th><th>Share of paid</th><th>Main channels</th><th>What to watch</th></tr></thead>
<tbody>
<tr><td>Announce</td><td>Weeks 8 to 6</td><td>15%</td><td>Meta, TikTok, email to past buyers</td><td>Presale signups, add-to-cart rate</td></tr>
<tr><td>Early bird close</td><td>Week 5</td><td>15%</td><td>Meta retargeting, email, Google search on the event name</td><td>Orders before the price change</td></tr>
<tr><td>The lull</td><td>Weeks 4 to 3</td><td>15%</td><td>Group outreach, creators, streaming TV for family shows</td><td>Group inquiries, video views</td></tr>
<tr><td>Final push</td><td>Last 14 days</td><td>45%</td><td>Meta, Google search, retargeting</td><td>Cost per order, daily pace vs goal</td></tr>
<tr><td>Reserve</td><td>Held back</td><td>10%</td><td>Wherever cost per order is lowest</td><td>Weather forecast, sell-through by date</td></tr>
</tbody></table></div>
<p>That reserve line matters more in Houston than most places. If the forecast turns ugly, you haven’t spent it. If Saturday looks perfect, push it into Thursday and Friday, when last-minute buyers make plans.</p>
<p>Below roughly $1,500 in paid media, skip the channel spread: Meta retargeting, Google search on your event name, and email. Spreading $1,200 across five platforms buys five half-trained campaigns.</p>"""),

            ("How to promote an event on Facebook and Instagram so it sells tickets", f"""<p>Boosting the Facebook event post is the most common move and the weakest. It optimizes for engagement, and people who will never buy love to tap “Interested.”</p>
<p>Set it up in Ads Manager instead:</p>
<ol><li><b>Use the Sales objective</b> with the Purchase event from your ticketing platform’s pixel as the conversion. (No Purchase event firing? Fix that first; see the tracking section below.)</li>
<li><b>Turn on Advantage+ audience and give it suggestions.</b> As {SRC['loomer']} explains, custom audiences and lookalikes go in as suggestions Meta tries first, while location, minimum age and excluded custom audiences act as hard controls. Upload your past buyer list as a custom audience and suggest it, plus a 1% lookalike. Meta needs a source of {SRC['lal']}, and Meta recommends 1,000 to 5,000 for a lookalike that’s actually useful.</li>
<li><b>Exclude people who already bought</b> for single-date shows. For multi-date exhibitions, don’t: week-one families come back with grandparents.</li>
<li><b>Draw the map by drive time, not by a circle.</b> Meta doesn’t target by drive time, so build it from zip codes and towns. A Saturday matinee at the Cynthia Woods Mitchell Pavilion pulls easily from Spring, Conroe, Magnolia, Tomball and Kingwood. A 7 p.m. Friday show there asks a lot of someone in Katy or Pearland. A 25-mile radius looks tidy and ignores I-45 at rush hour.</li></ol>
<p>Small events hit a quieter problem. Meta’s guidance points to roughly 50 optimization events in a week to exit the learning phase, and a 400-seat show might sell 60 tickets through ads total. We’ll often optimize for initiated checkout early, then switch to Purchase for the final two weeks. Not perfect. Better than a campaign stuck in learning forever.</p>
<p>Creative matters more than targeting here. Vertical video of the actual experience (the exhibit floor, the crowd at the chorus, a kid in the light tunnel) beats a flyer every time, with date, venue and total price in the first two seconds. Building this out is what our {'<a href="/services/paid-social-advertising/">paid social team</a>'} does every week.</p>"""),

            ("Google Ads for “[event] near me” and “things to do this weekend”", f"""<p>Google search catches demand other channels create. Someone sees your poster on Market Street or scrolls past a TikTok, then Googles the name. If a reseller shows up first, you paid for that search and someone else collected it.</p>
<p>A sensible event search setup has three ad groups:</p>
<ul><li><b>Your event name and its misspellings.</b> Cheapest clicks you will ever buy, and they protect you from resale sites bidding on your name.</li>
<li><b>The performer, exhibit or festival category.</b> “Dinosaur exhibit Houston,” “jazz festival Houston,” “Christmas lights The Woodlands.”</li>
<li><b>Intent phrases from planners.</b> “Things to do in Houston this weekend,” “indoor things to do with kids Houston,” “events near me tonight.” Pricier and broader, so schedule them Wednesday through Saturday.</li></ul>
<p>Google’s {SRC['geo']} explains the difference between “Presence” and “Presence or interest.” For a concert, Presence or interest can help, because it catches the parent in Beaumont or College Station planning a Houston weekend. For a neighborhood holiday market, use Presence. Radius targeting needs at least 1 km, so tiny geofences around one venue won’t work here.</p>
<p>Start bidding on Maximize clicks with a max CPC cap until purchases are tracking, then move to Maximize conversions. We’d skip Performance Max for a one-off event. Your event is over before it learns anything.</p>
<p>Running a touring exhibition with daily time slots? Ask your ticketing provider whether it connects to Google’s {SRC['ttd']}, which shows bookable activities through connectivity partners. We haven’t confirmed which platforms qualify, so ask. Our {'<a href="/services/search-marketing/">search marketing</a>'} page covers how we run Google Ads more broadly.</p>"""),

            ("TikTok and streaming TV for events: when each is worth it", f"""<p>TikTok earns its spot for concerts, festivals, nightlife and anything aimed at people under 35. The ads that sell look like regular posts: a creator walking the venue, a clip of last year’s crowd. Spark Ads put paid budget behind a creator’s own post, which reads as more credible than your brand account.</p>
<p>Confirm your ticketing platform can pass purchases to TikTok. If it can’t, judge TikTok by the lift in branded searches and sales during flights. And plan fresh videos every week or two in the final month; TikTok burns creative fast.</p>
<p>For family events, streaming TV deserves a real look. A 15-second spot on a streaming app reaches the whole household on the couch, targeted by zip code. We wrote a full piece on {'<a href="/blog/streaming-tv-ads-worth-it-small-business/">whether streaming TV ads are worth it</a>'}; for events, our rule is that it makes sense once total paid media passes about $10,000 and the event runs long enough (two weekends or more) for awareness to turn into searches. For a single-night club show, we’d keep that money on Meta.</p>
<p>Either way, check branded search volume every few days. When these channels work, more people search your event’s name.</p>"""),

            ("Email and texts to past attendees (and the Texas consent rules)", f"""<p>Your best audience already bought from you. A past-buyer list routinely outsells every paid channel per dollar, and most promoters email it twice per event.</p>
<p>A better sequence for a typical event:</p>
<ol><li><b>Presale invite,</b> with a code, 48 hours before public on-sale.</li>
<li><b>Early bird deadline,</b> sent the day before the price goes up.</li>
<li><b>A content email in the lull:</b> a behind-the-scenes video, the set times, the parking plan.</li>
<li><b>Final week:</b> “Saturday is close to sold out” only if it’s true, plus the weather and parking details.</li></ol>
<p>Texts work even better and carry real legal risk. Federal law (the TCPA) generally requires prior express written consent before you send marketing texts using automated systems, so text only people who opted in to texts specifically. Buying a ticket isn’t the same as opting in.</p>
<p>Texas tightened things too. According to {SRC['sb140']}, the law took effect September 1, 2025, brought text messages under the state’s telephone solicitation rules, added a registration requirement with penalties up to $5,000 per violation, and lets consumers sue under the Texas Deceptive Trade Practices Act. The write-up notes an exemption for texts to current or former customers. Whether your list fits that exemption is a question for your lawyer. Ask before the first blast.</p>
<p>For people who visited your ticket page and didn’t buy, retargeting ads do the follow-up with no consent risk. Our explainer on {'<a href="/blog/retargeting-explained/">how retargeting works</a>'} covers the basics.</p>"""),

            ("Tracking ticket sales: pixels on Eventbrite, Universe and Ticketmaster", f"""<p>This is the part most promoters get wrong, and it quietly ruins everything above. If Meta can’t see purchases, it optimizes for the wrong people. Here’s what the major platforms support, per their help pages:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform</th><th>Meta</th><th>Google</th><th>Watch out for</th></tr></thead>
<tbody>
<tr><td>Eventbrite</td><td>Pixel fires PageView and Purchase by default; server-side tracking with a Conversions API token</td><td>GA4 sends event_listing, event_register and purchase; separate Google Ads conversion setup</td><td>Can’t verify Eventbrite’s domain with Meta; pixels don’t catch every purchase</td></tr>
<tr><td>Universe</td><td>Pixel plus optional Conversions API; sends viewed tickets, added tickets and purchase with order value</td><td>Check current integrations tab</td><td>Embedded widgets on your own site need the pixel base code in your header</td></tr>
<tr><td>Ticketmaster</td><td colspan="2">Depends on the venue’s or promoter’s account and contract</td><td>Ask your Ticketmaster rep what you can place before you plan media</td></tr>
</tbody></table></div>
<p>The details come from {SRC['ebmeta']}, its {SRC['ebga']} article and {SRC['universe']}. Eventbrite says plainly that “tracking pixels aren’t able to track every purchase” and that GA4 purchase data won’t reflect refunds or manual transactions, so reconcile against your sales report weekly.</p>
<!--fig:tracking-->
<p>Then test it the unglamorous way. Create a hidden $1 ticket type, buy one yourself through an ad click, and watch Meta Events Manager’s Test Events tab and Google’s Tag Assistant. Refund yourself after.</p>"""),

            ("Getting your event into Google’s event listings", f"""<p>Search “things to do in Houston this weekend” and Google often shows an events panel. Getting in is mostly a structured data job.</p>
<p>Google’s {SRC['schema']} require three properties: <i>name</i>, <i>startDate</i> (with date and time) and <i>location</i> with a venue name and address. Recommended properties include <i>offers</i> with price, currency, availability, a <i>validFrom</i> on-sale date and a ticket <i>url</i>, plus <i>eventStatus</i>, <i>image</i>, <i>organizer</i> and <i>performer</i>. A few rules trip people up:</p>
<ul><li>Mark up one event per page, not a schedule page listing many.</li>
<li>The event must be open to the public and at a physical place. Invite-only and virtual events aren’t eligible.</li>
<li>If your listing lives on a ticketing site that already works with Google’s event search, Google says that listing can carry you. Mark up your own page anyway.</li>
<li>When plans change, update <i>eventStatus</i>: EventCancelled, EventPostponed (new date unknown) or EventRescheduled (with the new <i>startDate</i> and an optional <i>previousStartDate</i>).</li></ul>
<p>Two free extras: an Event post on the venue’s Google Business Profile with the ticket link, and the community calendars locals actually read.</p>"""),

            ("Pricing, scarcity and group sales (with the FTC’s all-in rule)", f"""<p>Since May 12, 2025, the FTC’s fees rule has required the total ticket price, mandatory fees included, upfront and more prominent than any partial price ({SRC['btlaw']}). The {SRC['ftcfaq']} says it covers “any business that offers, displays, or advertises live-event tickets,” venues included, and that ads with pricing must give the total. You can advertise the lowest general admission total “only if people can actually buy tickets at that price.” Taxes may be left out of the upfront figure as long as they’re disclosed before payment.</p>
<p>So if your ad says “Tickets from $25,” $25 had better be the all-in price of a ticket people can buy. Fix ad copy and email headers first.</p>
<p>For family events we prefer published price tiers (early bird, general, final) over algorithmic surge pricing. Surge pricing can work for hot concerts, but a parent who sees the price jump overnight posts about it in the neighborhood Facebook group.</p>
<p>Scarcity works when it’s true. “Only 60 tickets left for the 2 p.m. Saturday slot” is honest urgency if your ticketing report says 60. Resetting countdown timers lose you the repeat audience.</p>
<p>Group sales are the most underused tool in the lull. Churches, PTOs, scout troops, youth sports teams and company outings (think Energy Corridor HR teams) buy in tens and twenties. Build a group page with a 10-ticket rate and a short form, and reply within a day. Two afternoons calling youth sports leagues can outsell a week of ads.</p>"""),

            ("Houston weather: plan for the storm before you sell the ticket", f"""<p>Hurricane season runs June 1 to November 30, summer afternoons can turn from clear to lightning in an hour, and Beryl knocked out power across the region in July 2024. Late buyers (remember that 57%) check the forecast before they commit, so the weather plan is a marketing document too.</p>
<p>The {SRC['nws']} says experts agree people “should wait at least 30 minutes after the last thunder before resuming outdoor activities,” that organized events should “have a lightning safety plan and follow it without exception,” and that if thunderstorms are forecast, organizers should consider canceling or postponing.</p>
<!--fig:weather-->
<p>Indoor events get the flip side. An air-conditioned exhibition in August, or a covered venue on a rainy Saturday, is a selling point. Build a “rainy weekend” ad set on searches like “indoor things to do Houston” and keep it paused until the forecast turns.</p>"""),

            ("Where to start this week, and when to get help", f"""<p>If you only do three things before your next on-sale, do these: buy a $1 test ticket and confirm Purchase shows up in Meta and Google, pull your past-buyer list into a custom audience and an email presale, and move half your remaining budget into the final 14 days.</p>
<p>Plenty of promoters can run all of this themselves, especially with a total ad budget under about $2,000 and one platform to manage. Hiring help makes more sense when you’re running several events a quarter, spending enough that a 20% swing in cost per order is real money, or when tracking is so tangled nobody trusts the numbers. Our {'<a href="/industries/live-entertainment/">live entertainment</a>'} page shows the kind of work we do for venues and promoters.</p>
<p>If you’re mid-campaign and the numbers feel off, our free Ad Spend Leak Check is a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours. {'<a href="/contact/">Request one here</a>'}, and send it before the final push, not after.</p>"""),
        ],
        "faq": [
            ("How far in advance should you start promoting an event?",
             "For most local concerts and family events, six to eight weeks of promotion is plenty, with the heaviest spending in the final ten to fourteen days. Festivals and touring exhibitions can announce months out, but should still save a big share of budget for the end, when most tickets sell."),
            ("How much should I spend on ads to sell event tickets?",
             "Work backward from your average order. Decide what share of gross ticket revenue you can spend on ads, often 10 to 25 percent, and divide by orders to get an affordable cost per order. A family show with $84 orders and a 20 percent ad share can afford about $17 per order. If your ads cost more than that, fix tracking, creative or targeting before adding budget."),
            ("Why are my event ticket sales slow?",
             "Usually it is normal. Sales spike at announcement, go quiet in the middle weeks and surge in the last week. If you are close to the date and still behind, check whether your pixel records purchases, whether ads show the all-in price, whether past buyers got a presale, and whether you are targeting people within a realistic drive of the venue."),
            ("Is Facebook or Google better for selling event tickets?",
             "They do different jobs. Meta and Instagram create demand by putting the event in front of people who were not looking for it. Google search captures demand from people already searching your event name or things to do this weekend. Most events need both, with Meta getting more budget early and Google search on your event name running the whole time."),
            ("Can I text past attendees about my next event?",
             "Only if they agreed to receive marketing texts from you. Federal rules generally require prior express written consent for automated marketing texts, and Texas SB 140, effective September 1, 2025, brought texts under state telephone solicitation rules with registration and lawsuit risk. Email past buyers freely, text only opted-in contacts, and ask your lawyer about the Texas exemptions."),
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
                "caption": f"Based on {A('https://support.eventbrite.com/hc/it/articles/34863669333650-Add-a-Meta-Pixel-to-your-event', 'Eventbrite')} and {A('https://support.universe.com/hc/en-us/articles/360002452312-Use-Facebook-Pixel-on-your-Universe-event', 'Universe')} help pages.",
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
<p>That’s the most common story we hear from Shopify owners, and it’s fixable. Google Shopping ads for Shopify work like this: the Google &amp; YouTube app sends your products to Google Merchant Center, Merchant Center turns them into free listings and ad inventory, and a Performance Max or Standard Shopping campaign in Google Ads decides which products show, to whom, and at what price per click. Most of the results are decided before you ever set a bid, in the product feed and in conversion tracking.</p>
<p>This guide walks through setup, the feed fields that matter, the disapprovals that stall new stores, how to choose between Performance Max and Standard Shopping, and the margin math behind a ROAS target that actually makes you money.</p>"""),

            ("How Google Shopping works for a Shopify store (and what’s free)", f"""<p>Three pieces, and it helps to keep them separate in your head.</p>
<p><b>Google Merchant Center</b> holds your product data: titles, prices, images, availability, shipping and return policies. Google spent two years calling the rebuilt version “Merchant Center Next,” then {SRC['next']}, so older tutorials and the current interface won’t always match. Same tool.</p>
<p><b>Free listings</b> come first. According to {SRC['shopifyhelp']}, eligible US stores’ synced products can show in Google Shopping tab listings for free. They won’t carry a store on their own, but they cost nothing, and they’ll tell you which products Google likes before you spend a dollar.</p>
<p><b>Paid Shopping ads</b> run from Google Ads, through either a Standard Shopping campaign or Performance Max. Both pull from the same Merchant Center feed. A bad feed hurts both equally.</p>
<p>Where you live doesn’t matter much here, which is part of the appeal. A candle maker in Tomball or a western boot shop in Conroe competes nationally on the same auction. What matters is price, product data, images and how fast the store loads. (If your product pages take five seconds on a phone, read {'<a href="/blog/how-fast-should-your-website-load/">our page speed guide</a>'} before you spend.)</p>"""),

            ("Google Merchant Center setup on Shopify, step by step", f"""<p>Google’s {SRC['onboard']} lays out the sequence. In plain terms:</p>
<!--fig:setup-->
<p>The details that hang people up:</p>
<ul><li><b>Remove the storefront password.</b> Google can’t review a store it can’t see. Stores in pre-launch mode fail here constantly.</li>
<li><b>Publish a refund policy, terms of service and contact details</b> on the store before you start. The app checks for them.</li>
<li><b>Use a standalone Merchant Center account.</b> Google says multi-client accounts (MCAs) can’t link to the app. If an old agency set you up under their MCA, you may need a fresh account.</li>
<li><b>Map conversion events during setup.</b> When the app is linked to Google Ads, it lists Shopify’s standard events (purchase, add_to_cart, begin_checkout) and lets you map each to a conversion action. Turn on Enhanced Conversions while you’re there.</li>
<li><b>Set shipping in Merchant Center to match your store.</b> If checkout charges $8.95 and Merchant Center says free shipping, expect a mismatch warning.</li></ul>
<p>Shipping is also where Texas sellers can get ahead of trouble. Add realistic handling time, and update it during hurricane season if carriers stall. A missed delivery estimate is a refund request, and enough of those become a review problem on Google.</p>"""),

            ("Product feed optimization: titles, GTIN, product_type and custom labels", f"""<p>This is the part most Shopify stores skip, and it’s where we find the most money. Shopping has no keywords. Google matches searches to your product data, so the feed is your keyword list.</p>
<h3>Titles</h3>
<p>The {SRC['title']} allows up to 150 characters, and Google notes shoppers usually see only the first 70 or fewer. Put the words people search first: brand (if people search it), product type, then the details that separate one variant from another, like material, size, color or count. “Willow Tote” tells Google almost nothing. “Large Leather Tote Bag, Cognac, Zip Top, 15 in Laptop Pocket” matches a dozen real searches.</p>
<!--fig:titles-->
<h3>GTIN</h3>
<p>If a product has a manufacturer barcode, submit it. Google’s {SRC['gtin']} says products with missing or incorrect GTINs “may have limited visibility,” and a product could be disapproved if a GTIN exists and you leave it off. For your own handmade or private-label goods without one, leave the field blank. Never invent a number. In Shopify, the variant’s barcode field is where this usually lives.</p>
<h3>product_type and google_product_category</h3>
<p>Google’s {SRC['ptype']} explains that <i>google_product_category</i> uses Google’s fixed taxonomy, while <i>product_type</i> is your own classification, such as “Home &gt; Candles &gt; Soy Candles.” Product types can be subdivided up to five levels in campaign {SRC['listing']}, which makes them the cleanest way to split bids and budgets by category.</p>
<h3>Custom labels</h3>
<p>You get five {SRC['labels']} (custom_label_0 to custom_label_4), each with up to 1,000 unique values. Shoppers never see them. They exist so you can group products in campaigns. The ones we set on almost every store:</p>
<ul><li><b>Margin band:</b> high, mid, low. This one drives bidding, and it should be set before anything else.</li>
<li><b>Price band:</b> under $25, $25 to $75, over $75.</li>
<li><b>Seasonality:</b> holiday, summer, evergreen.</li>
<li><b>Performance:</b> hero, steady, zombie (products that never get impressions).</li></ul>
<p>Your margin data doesn’t live in a standard Shopify field, so plan to add labels with a feed app, a supplemental feed (a Google Sheet works), or Merchant Center rules.</p>"""),

            ("Merchant Center disapprovals: misrepresentation, shipping and returns", f"""<p>New stores get a “Misrepresentation” suspension more than any other, and the message rarely tells you why. Google’s {SRC['misrep']} gives the general rules: real business identity and contact details, a return policy you honor, the full cost shown (taxes, fees, shipping including return shipping), clear delivery timelines, and only listing products you can actually fulfill.</p>
<p>For egregious violations, Google says accounts can be suspended without warning. For most others, you get a warning email and 7 or 28 days to fix it, and account reviews typically take about 7 business days. Don’t burn appeals by requesting review before everything is fixed.</p>
<!--fig:disapprovals-->
<p>Sales tax used to be another common snag. Since July 1, 2025, Google’s {SRC['tax2025']} says US merchants are no longer required to submit sales tax in the feed or Merchant Center tax settings. You still have to collect it properly at checkout. For in-state basics, the {SRC['txtax']} sets the state rate at 6.25%, local jurisdictions can add up to 2%, and the combined maximum is 8.25%. Get a Texas sales tax permit and set up Shopify Tax (or your accountant’s preferred method) before launch. Remote-seller rules in other states are a separate conversation for your CPA.</p>"""),

            ("Performance Max vs Standard Shopping for Shopify stores", f"""<p>This is the argument every ecommerce forum is having, and the honest answer depends on budget and how much you trust your conversion data. We wrote about the local-business version in {'<a href="/blog/performance-max-vs-search-campaigns-local/">Performance Max vs Search campaigns</a>'}. For Shopify stores, it plays out like this:</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Standard Shopping</th><th>Performance Max</th></tr></thead>
<tbody>
<tr><td>Where ads show</td><td>Shopping results and Shopping tab</td><td>Shopping plus YouTube, Display, Gmail, Discover and Search</td></tr>
<tr><td>Control</td><td>Manual CPC by product group, or campaign-level Target ROAS; full search terms report</td><td>Campaign-level Target ROAS; partial search term insights</td></tr>
<tr><td>Data it needs</td><td>Works with thin data</td><td>Wants steady conversion volume</td></tr>
<tr><td>Best fit</td><td>New stores, tight budgets, testing which products sell</td><td>Stores with clean tracking and dozens of conversions a month</td></tr>
<tr><td>Risk</td><td>More hands-on work</td><td>Spend drifts to brand searches and remarketing that look great but add little</td></tr>
</tbody></table></div>
<p>One change worth knowing: since October 2024, Performance Max no longer automatically wins over Standard Shopping when both campaigns carry the same products. As {SRC['adrank']} reported, Ad Rank now decides. That makes running both side by side far more workable than it used to be.</p>
<p>Our default for a new Shopify store: start with Standard Shopping on your best 20 to 50 products, broken out by product_type or margin label, until you have 30 or more purchases a month. Then test Performance Max on the proven products.</p>
<p>When we do run Performance Max, we often start feed-only: an asset group with product listing groups and no uploaded videos or images, so spend leans toward Shopping placements. Two caveats. Google may still auto-create assets unless you switch off automatically created assets, and feed-only isn’t an official campaign type, just a common practitioner setup. Check placement reports after two weeks.</p>"""),

            ("Setting a ROAS target from your margins", f"""<p>ROAS is revenue divided by ad spend. A 4x ROAS means $4 in sales per $1 in ads. Whether that’s good depends entirely on your margin, and most stores set targets by copying a number from a podcast.</p>
<p>The math that matters: break-even ROAS equals 1 divided by your gross margin (after product cost, shipping you pay, payment fees and typical returns). At a 40% margin, every $100 sale leaves $40 to cover ads, so $40 of ad spend per $100 of revenue is break-even, which is a 2.5x ROAS. Anything below that loses money on the first order.</p>
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
<p>Look at the 25% row. Low-margin products (resold name brands, mostly) are brutal on Shopping, because big retailers bid on the same GTINs. Bid those down or leave them out, and point budget at high-margin items, which is exactly what the margin custom label is for.</p>
<p>One adjustment we’ll defend: if repeat purchase rates are strong (consumables, coffee, skincare), you can accept a first-order ROAS near break-even, because the second order is where the profit lives. Know your repeat rate before you make that bet.</p>"""),

            ("Negative keywords in Shopping and Performance Max", f"""<p>Shopping doesn’t use keywords to target, but you can still block searches. Three layers:</p>
<ul><li><b>Account level.</b> Google’s {SRC['acctneg']} apply across Search, Performance Max, Shopping and other campaign types, with a limit of 1,000 per account. Find them under Admin, then Account settings, then Negative keywords. This is where “free,” “DIY,” “pattern,” “used,” “jobs” and competitor names you never want to pay for belong.</li>
<li><b>Campaign level in Performance Max.</b> PMax negative keyword limits were {SRC['pmaxneg']}, matching Search. Use them for campaign-specific exclusions, like blocking brand terms in a prospecting campaign.</li>
<li><b>Standard Shopping campaigns</b> take negatives the normal way, and their full search terms report makes finding them easy.</li></ul>
<p>A practical habit: every Monday, sort search terms by cost with zero conversions, and add anything irrelevant as a negative. Our {'<a href="/blog/small-business-guide-google-ads-2026/">small business Google Ads guide</a>'} covers match types if negatives are new to you.</p>
<p>On brand: decide on purpose whether Shopping campaigns should spend on your own brand name. Brand searches convert well and inflate ROAS, which makes a mediocre campaign look great. We usually split brand into its own budget so you can see what the non-brand work is really doing.</p>"""),

            ("Shopify Google Ads not working? A diagnostic table", f"""<p>When an owner tells us their Shopify Google Ads aren’t working, it’s almost always one of these. Work top to bottom, since earlier problems hide later ones.</p>
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
<p>The double-counting issue deserves special mention. Many stores have the Shopify app’s purchase conversion and an imported GA4 purchase both set as primary goals, so Google sees two sales for every one. Your reported ROAS doubles, Target ROAS bidding gets confused, and you scale a campaign that isn’t profitable. Also check what “value” means. If the conversion value includes shipping and tax, your real ROAS is lower than the report says, so set targets from the same definition.</p>"""),

            ("What to budget for Google Shopping, and when to get help", f"""<p>Budget follows margin and price point. As a rule of thumb (ours, not Google’s), a campaign needs enough daily budget to buy several conversions a week at your target cost, or bidding never has data to learn from. If your average order is $60 and you’re aiming for a 3x ROAS, each order can cost about $20 in ads. Ten orders a week means roughly $200 a week, or about $30 a day, as a realistic floor for one campaign.</p>
<p>Give a new Standard Shopping setup 30 to 45 days before making big calls. Week one tells you about feed problems. Weeks three through six tell you about products.</p>
<p>A Shopify owner can absolutely run this alone with a clean feed, tracking checked, and an hour a week on search terms. Hiring help is worth it when spend passes a few thousand a month, when the catalog is large enough that feed work is a project, or when tracking is broken and nobody knows which number to believe. Our {'<a href="/industries/ecommerce/">ecommerce</a>'} page and {'<a href="/services/search-marketing/">search marketing</a>'} page describe how we handle those accounts.</p>
<p>If you already have campaigns running and something feels off, start with our free Ad Spend Leak Check: a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours. {'<a href="/contact/">Request it here</a>'}. Double-counted conversions are usually the first thing we look for.</p>"""),
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
