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

TRACK = "/blog/track-ticket-sales-meta-google-ads-ticketing-platforms/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: touring events

    # ------------------------------------------------------------------ post 2: tracking ticket sales
    {
        "slug": "track-ticket-sales-meta-google-ads-ticketing-platforms",
        "title": "How to Track Ticket Sales From Meta and Google Ads on Ticketmaster, Eventbrite, AXS and Etix",
        "seo_title": "Track Ticket Sales From Meta & Google Ads, by Platform",
        "desc": "How to track ticket sales from Meta and Google ads on Ticketmaster, Eventbrite, AXS, Etix and Universe: pixels, Conversions API, GA4, UTMs and reconciliation.",
        "category": "Paid ads",
        "icons": ["Meta", "Google Analytics", "Google Ads"],
        "art": "b2",
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
<p>Illustrative example. Note that the coverage formula adds Meta and Google purchases, which can double-count a buyer who clicked both; read it as a trend, not a precise share. The pace index compares tickets sold to where the same date stood on past runs at the same number of days out; our {L('/blog/how-to-sell-more-event-tickets-houston/', 'guide to selling more event tickets')} covers building that curve.</p>"""),

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
