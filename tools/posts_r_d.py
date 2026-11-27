"""Batch 18 (module d): a TikTok Ads setup guide for Houston and The Woodlands businesses, and a video production
cost guide for Houston.

Research, TikTok post: TikTok Business Help Center on budgets (campaign daily budget over $50, ad group over $20,
lifetime ad group minimum = days x $20, 40%/30% budget increase guidance, two days between changes), location
targeting (state, DMA, county, city, ZIP; no location or ZIP exclusions; no ZIP+4; 3,000 selections per ad group;
small areas reduce reach), learning phase (volatility declines after about 25 results or 7 days), choosing an
objective (Reach, Traffic, Video views, Community interaction, App promotion, Lead generation, Sales), Spark Ads and the
Spark Ads creation guide (Ad settings > Generate code; TikTok posts tab > Add post; up to 20 codes at once), Lead
generation with Instant Form and building an Instant Form (More Volume vs Higher Intent; required privacy policy;
CRM sync), auction in-feed video specs (9:16 recommended, 540x960 minimum, up to 10 minutes, 500 MB, no links or
hashtags in non-Spark captions), the Commercial Music Library (1 million pre-cleared songs for business use), and
setting up the web data connection (Tools > Events Manager > Connect Data Source > Web; Pixel Helper; Test Events;
Events API). Pew Research Center, "8 facts about Americans and TikTok" (March 2026; 37% of U.S. adults, 63% under 30,
44% 30-49, 30% 50-64, 12% 65+; survey Feb. 5-June 18, 2025).
Research, video post: Houston Film Commission production FAQ (registration form for filming on public property in
city limits, $1 million per incident liability certificate, off-duty "film cops" for traffic control, parks permits,
Fire Marshal for pyrotechnics, noise permit for amplified playback; 713-853-8386); The Woodlands Area Film
Commission FAQ (permit for commercial filming on real property including public spaces; online application at least
5 business days ahead in the current version, 10 in an older one; certificate of insurance; off-duty officers paid
directly by the applicant); Texas Film Commission permitting overview (no statewide permit; private property needs a
location agreement; TPWD state parks need several weeks); Governor's office on The Woodlands' Film Friendly Texas
designation (Sept. 3, 2020); FAA commercial drone operators page (Part 107 certificate, $5 registration valid 3
years) and LAANC page; BLS Occupational Outlook Handbook (May 2025 medians: camera operators $74,990, film and video
editors $75,420; 35% self-employed); U.S. Copyright Office "What Musicians Should Know" (musical work vs. sound
recording); YouTube Audio Library help; Epidemic Sound Business plan terms (paid online ads covered; OOH, radio,
livestreams excluded; revenue eligibility limits); TikTok Commercial Music Library.
Facts we could not verify and left out: TikTok's Spark Ads authorization period options (only third-party sources),
any published TikTok CPM or CPL benchmarks (only unsourced third-party ranges), City of Houston film permit fees and
lead times (HFC does not publish them), and whether commercials qualify for the Texas Moving Image Industry Incentive
Program (the page would not load). Production price ranges are labeled as our planning ranges.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # TikTok post
    "budget": A("https://ads.tiktok.com/help/article/budget?lang=en", "TikTok's budget help page"),
    "loc": A("https://ads.tiktok.com/help/article/location-targeting", "TikTok's location targeting page"),
    "learn": A("https://ads.tiktok.com/help/article/learning-phase", "TikTok's learning phase article"),
    "obj": A("https://ads.tiktok.com/help/article/choose-right-objective?lang=en", "TikTok's guide to choosing an objective"),
    "spark": A("https://ads.tiktok.com/help/article/spark-ads", "TikTok's Spark Ads overview"),
    "sparkhow": A("https://ads.tiktok.com/help/article/spark-ads-creation-guide?lang=en", "Spark Ads creation guide"),
    "leadgen": A("https://ads.tiktok.com/help/article/set-up-lead-generation-with-instant-form?lang=en", "lead generation setup guide"),
    "form": A("https://ads.tiktok.com/help/article/build-instant-form?lang=en", "Instant Form help page"),
    "specs": A("https://ads.tiktok.com/help/article/video-ads-specifications?lang=en", "TikTok's in-feed ad specs"),
    "cml": A("https://ads.tiktok.com/help/article/commercial-music-library", "Commercial Music Library"),
    "pixel": A("https://ads.tiktok.com/help/article/get-started-pixel?lang=en", "TikTok's pixel setup guide"),
    "pew": A("https://www.pewresearch.org/short-reads/2026/03/02/8-facts-about-americans-and-tiktok/", "Pew Research Center"),
    # video post
    "hfc": A("https://www.houstonfilmcommission.com/production-and-resources/production-faq/", "Houston Film Commission's production FAQ"),
    "hfcform": A("https://www.houstonfilmcommission.com/production-and-resources/registration-form/", "registration form"),
    "wfc": A("https://assets.simpleviewinc.com/simpleview/image/upload/v1/clients/woodlands/The_Woodlands_Film_Commission_Frequently_Asked_Questions_Updated_5_16_22_0062a6db-aabf-4b4d-8091-750923654cdf.pdf", "The Woodlands Area Film Commission's FAQ"),
    "wfcapp": A("https://www.visitthewoodlands.com/film/application/", "online application"),
    "tfc": A("https://gov.texas.gov/film/page/permitting_overview", "Texas Film Commission's permitting overview"),
    "ffw": A("https://gov.texas.gov/es/film/post/governor-abbott-announces-film-friendly-texas-designation-for-the-woodlands", "Film Friendly Texas community"),
    "faa": A("https://www.faa.gov/uas/commercial_operators", "FAA's commercial operator page"),
    "laanc": A("https://www.faa.gov/uas/getting_started/laanc", "LAANC"),
    "bls": A("https://www.bls.gov/ooh/media-and-communication/film-and-video-editors-and-camera-operators.htm", "Bureau of Labor Statistics"),
    "copy": A("https://copyright.gov/engage/musicians/", "U.S. Copyright Office"),
    "ytal": A("https://support.google.com/youtube/answer/3376882?hl=en", "YouTube Audio Library help page"),
    "epi": A("https://www.epidemicsound.com/our-plans/business-plan/", "Epidemic Sound's Business plan page"),
}

TT = "/blog/tiktok-ads-local-business-houston/"
VP = "/blog/video-production-cost-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: TikTok ads setup guide
    {
        "slug": "tiktok-ads-local-business-houston",
        "title": "TikTok Ads for Houston and The Woodlands Businesses: Costs, Setup and What Works",
        "seo_title": "TikTok Ads for Houston Businesses: Costs and Setup",
        "desc": "TikTok ads for Houston and The Woodlands businesses: real minimum budgets, Ads Manager setup, ZIP targeting limits, Spark Ads, lead forms and tracking.",
        "category": "Paid ads",
        "icons": ["TikTok", "Meta", "Google Analytics"],
        "art": "b4",
        "hero": "phone",
        "hero_alt": "Illustration of a phone showing a short video for TikTok ads for local businesses in Houston and The Woodlands",
        "related": ["facebook-vs-instagram-vs-tiktok-local-business", "youtube-ads-cost-local-business-houston", "ugc-vs-influencers-creator-content"],
        "sections": [
            (None, f"""<p>“Can I run TikTok ads only to people in The Woodlands, for like $10 a day?”</p>
<p>It's one of the most common TikTok questions Houston owners ask. The answer is yes to the first half and no to the second. TikTok will let you target a handful of ZIP codes. It won't let you spend $10 a day doing it.</p>
<p><b>The short answer:</b> TikTok ads for a Houston or Woodlands business start at a $50 daily campaign budget and a $20 daily ad group budget, so a real local test runs about $1,000 to $1,500 a month. You can target ZIP codes, cities, counties or the Houston DMA, but you can't exclude areas. It works best for visual businesses whose customers are under 50.</p>
<p>This is a setup guide. It walks through Ads Manager in the order you'll click through it, with the settings we'd pick for a local business and the places TikTok's defaults will cost you money. If you're still deciding between platforms, read our {L('/blog/facebook-vs-instagram-vs-tiktok-local-business/', 'Facebook vs. Instagram vs. TikTok comparison')} first and come back.</p>
<!--fig:minimums-->"""),

            ("How much do TikTok ads cost for a Houston business?", f"""<p>TikTok doesn't publish average prices, and the third-party “average CPM” numbers floating around rarely say where they came from. What TikTok does publish are the floors. Per {SRC['budget']}, a campaign's daily budget has to be more than $50 and an ad group's daily budget more than $20. On a lifetime budget, the ad group minimum is $20 times the number of days in the flight, so a 31-day ad group needs at least $620.</p>
<p>Those floors shape everything. One campaign at the minimum is roughly $1,500 a month. Split it into two ad groups (Spring and Klein ZIPs in one, The Woodlands and Shenandoah in the other) and each gets thinner.</p>
<p>A few budget rules from the same page that trip people up:</p>
<ul>
<li>Keep the campaign budget at or above the ad group budget, or delivery gets weird.</li>
<li>While an ad group is in its learning phase, raise the budget no more than 40% at a time. After it exits, no more than 30%. Wait at least two days between changes.</li>
<li>You can't switch between daily and lifetime budgets once something is live. Pick daily for a first test.</li>
</ul>
<p>The learning phase matters for small accounts. {SRC['learn']} says volatility starts to come down after about 25 results or 7 days. If you're optimizing for leads and you get four a week, you'll be “learning” for a long time. That's why we often start local accounts on a more frequent event, like landing page views, and move to lead optimization once there's volume.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Goal</th><th>Setup</th><th>Planning budget</th><th>Judge it on</th></tr></thead>
<tbody>
<tr><td>Local awareness test</td><td>Reach or Video views, one ad group, 10 to 20 ZIPs</td><td>$1,000 to $1,500 a month for 60 days</td><td>Cost per 1,000 local views, profile visits, branded Google searches</td></tr>
<tr><td>Lead generation</td><td>Lead generation objective, Instant Form, Higher Intent</td><td>$1,500 to $3,000 a month</td><td>Cost per lead, then cost per booked appointment</td></tr>
<tr><td>Website bookings or sales</td><td>Sales objective with pixel and Events API firing</td><td>$2,000 a month and up</td><td>Booked or purchased events, matched against your booking system</td></tr>
<tr><td>Grand opening or event</td><td>Reach plus Spark Ads of creator posts, lifetime budget</td><td>$620 minimum for a 31-day ad group, more for a short push</td><td>Reach in target ZIPs, RSVPs, opening-week traffic</td></tr>
</tbody></table></div>
<p>The table is our planning ranges, not benchmarks. Your real costs depend on how good the videos are, how small the area is and what time of year it is. In accounts we've run, ad prices climb from Black Friday through Christmas, and a Houston boutique running its first test the week before Thanksgiving is paying holiday prices to learn.</p>
<p>Budget for the videos too. Phone content shot by the owner costs an afternoon. Creator content and edited batches cost more, which our {L(VP, 'Houston video production cost guide')} breaks down.</p>"""),

            ("Is your customer on TikTok?", f"""<p>Before any setup, check the age math. {SRC['pew']} found 37% of U.S. adults use TikTok, up from 21% in 2021. Use falls hard with age:</p>
<!--fig:ages-->
<p>That's national data, and your own customer list is the better guide. Still, a business that sells mostly to people over 60 will find more of them on Facebook and YouTube.</p>
<p>Businesses we think are good TikTok candidates in the Houston area:</p>
<ul>
<li><b>Restaurants, bars, coffee and dessert spots.</b> The food is the ad. A 12-second pour or a cheese pull near Market Street sells itself. Our {L('/blog/restaurant-marketing-the-woodlands-houston/', 'restaurant marketing post')} covers the rest of the mix.</li>
<li><b>Med spas, salons, lash and brow studios, gyms.</b> Before-and-after (where it's allowed), trainer tips and treatment walk-throughs. See {L('/blog/med-spa-marketing-the-woodlands-houston/', 'med spa marketing')} for the policy side.</li>
<li><b>Visual home services.</b> Pressure washing, pool remodels, epoxy floors, landscape lighting. Satisfying transformations are basically a TikTok genre.</li>
<li><b>Boutiques and local retail</b>, especially with new arrivals weekly.</li>
</ul>
<p>Weaker fits: estate planning attorneys, commercial B2B, anything sold to a procurement department, and emergency services where the customer is searching on Google with water on the floor. Someone whose slab leak just started isn't scrolling for inspiration.</p>"""),

            ("Setting up TikTok Ads Manager, click by click", f"""<p>Here's the order we'd set things up in, before spending a dollar.</p>
<!--fig:setup-->
<p><b>1. Create the account at ads.tiktok.com.</b> Use a company email that won't leave when an employee does, and add a second admin. Set the time zone to Central so daily budgets and reports line up with your business day instead of someone else's midnight.</p>
<p><b>2. Connect the pixel before the first campaign.</b> The path, per {SRC['pixel']}: <i>Tools</i> &gt; <i>Events Manager</i> &gt; <i>Connect Data Source</i> &gt; <i>Web</i>, then enter your URL and pick <i>Partner Integration</i> (Shopify and Google Tag Manager are both listed) or <i>Manual Setup</i>. TikTok recommends setting up the Events API alongside the pixel, which sends events from your server and survives ad blockers and browser privacy settings better.</p>
<p><b>3. Pick an objective.</b> Go to the <i>Campaign</i> tab and click <i>+ Create</i>. {SRC['obj']} lists Reach under Awareness; Traffic, Video views, Community interaction and Branded Mission under Consideration; and App promotion, Lead generation and Sales under Conversion. For most local businesses it's one of three:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Objective</th><th>Use it when</th><th>Skip it when</th></tr></thead>
<tbody>
<tr><td>Reach</td><td>You want as many locals as possible to see a new location, menu or offer</td><td>You need leads this month</td></tr>
<tr><td>Video views</td><td>You're building a warm audience to retarget later</td><td>The video is weak; you'll just pay to prove it</td></tr>
<tr><td>Traffic</td><td>You have a fast mobile landing page and no reliable conversion event yet</td><td>Your site takes four seconds to load on a phone</td></tr>
<tr><td>Lead generation</td><td>You sell consultations, estimates or appointments</td><td>Nobody can call the lead back within the hour</td></tr>
<tr><td>Sales</td><td>Online booking or ecommerce, with the pixel firing on the confirmation page</td><td>Fewer than a handful of conversions a week</td></tr>
</tbody></table></div>
<p><b>4. Set up the ad group.</b> This is where placement, targeting, budget, schedule and optimization live. Leave TikTok as the placement and turn off the partner app placements for a first local test; it keeps the reporting readable. Set location (next section), age if your business genuinely has a floor (a med spa's 18+ is reasonable), and leave interests broad. TikTok's delivery does a decent job of finding the right people inside a small area, and stacking interests on top of ten ZIP codes starves the ad group.</p>
<p><b>5. Build the ad.</b> Upload videos or add Spark posts, write the caption, choose a call to action and a destination. Use UTM parameters on every URL so Google Analytics can see the traffic. Then click <i>Publish all</i> and expect a review before ads go live.</p>"""),

            ("Local targeting in Houston and The Woodlands: what TikTok can and can't do", f"""<p>{SRC['loc']} lists the U.S. options: country, state, DMA region, county, city and ZIP code. That's better than many owners expect. But there are three rules every Houston advertiser needs to know before setup:</p>
<ol>
<li><b>No exclusions.</b> “TikTok does not support the exclusion of locations or zip codes.” If you target Harris County, you get all of it, from Baytown to Katy. To leave something out, you have to build the area from smaller pieces.</li>
<li><b>No ZIP+4</b>, and some ZIP codes may not be targetable at all.</li>
<li><b>Small areas cost more.</b> The page warns that targeting small areas or small sets of ZIP codes can significantly reduce reach and may raise your cost per result.</li>
</ol>
<p>Radius and pin targeting aren't mentioned on TikTok's page, so don't plan around a 5-mile circle like you would on Meta or Google. ZIP codes are the tool. Up to 3,000 selections per ad group, so you'll never run out.</p>
<!--fig:zips-->
<p>How we'd build a few common service areas:</p>
<ul>
<li><b>The Woodlands core:</b> 77380, 77381, 77382, 77384, 77385, then 77389 if you want Creekside Park. Add 77354 for Magnolia and 77386 for Spring north of the Grand Parkway if you serve them.</li>
<li><b>North Houston suburbs along I-45:</b> the list above plus Spring (77373, 77379, 77388) and Conroe ZIPs, rather than the Houston DMA, which drags in counties you'll never drive to.</li>
<li><b>West side:</b> Katy and Cypress ZIP codes for a Grand Parkway corridor business. Don't use “Katy, Texas” the city alone; many Katy addresses sit outside city limits.</li>
</ul>
<p>Size check. Ten Woodlands-area ZIPs is plenty for $50 a day. Three ZIPs at $50 a day means the same few thousand people see your ad until they're sick of it, so watch frequency and widen the area early.</p>
<p>One more limit: TikTok's location page notes some advertisers fall under its housing, employment and credit policy. Home builders, apartment communities, lenders and job ads should expect fewer targeting options.</p>"""),

            ("Spark Ads: put money behind real posts", f"""<p>If you take one thing from this guide, make it this. {SRC['spark']} describes Spark Ads as a native format that lets you advertise organic TikTok posts, with the views, likes and follows credited to the original post. The ad shows your real handle and a real follow button and reads like any other post on the For You feed.</p>
<!--fig:spark-->
<p>Two ways to use them:</p>
<ul>
<li><b>Your own posts.</b> Post organically first, see which videos hold attention, then boost the winners. Your organic account becomes the test kitchen.</li>
<li><b>Creator or customer posts.</b> A local creator or a happy customer posts about you, then authorizes you to run it as an ad. Per the {SRC['sparkhow']}, the creator taps the three dots on the video, taps <i>Ad settings</i>, and taps <i>Generate</i> to create a code. In Ads Manager you open the <i>TikTok posts</i> tab in the creative section, click <i>Add post</i>, and paste it. You can add up to 20 codes at once, and the authorization period shows under each post.</li>
</ul>
<p>The catch: a Spark Ad's display name and text come from the original post and can't be edited in Ads Manager. If the caption says “OMG best tacos in Katy!!” that's your ad copy. Agree on captions with creators before they post, and put the agreement (pay, usage period, whether you can edit) in writing. Our {L('/blog/ugc-vs-influencers-creator-content/', 'UGC vs. influencers post')} covers what those deals usually look like.</p>"""),

            ("Lead generation with Instant Forms, and keeping the leads real", f"""<p>For appointment businesses, TikTok's lead forms can work. They can also fill your CRM with people who tapped through without reading. The setup, from TikTok's {SRC['leadgen']}: choose the Lead generation objective, set the ad group's <i>Optimization Location</i> to <i>Instant Form</i>, then create or attach a form in the ad's <i>Destination</i> section.</p>
<p>The setting that matters most is the form type. Per the {SRC['form']}, <b>More Volume</b> is the default and skips any review screen. <b>Higher Intent</b> adds a review screen and a CAPTCHA after someone taps Submit. For a local service business, we pick Higher Intent nearly every time. Fewer leads, but you can call them back without wasting a morning.</p>
<p>Other form choices we'd make:</p>
<ul>
<li>One qualifying question that a casual tapper won't bother with. “Which service are you interested in?” with real options, or “What part of town are you in?” with The Woodlands, Spring, Conroe, Tomball and “Somewhere else.”</li>
<li>The required privacy section: your company name and a link to a real privacy policy page on your site.</li>
<li>CRM sync. TikTok supports real-time CRM sync, and leads are also available by CSV download. CSV downloads mean someone has to remember to check, and a lead from Tuesday that gets a call on Friday is mostly gone.</li>
</ul>
<p>Speed is the whole game with social leads. These people weren't searching for you; they were watching dog videos. Call within five minutes if you can and text right away. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the follow-up sequence, and {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'fixing bad Facebook lead ads')} has form tactics that carry over to TikTok almost word for word. If you text these leads later for marketing, read our notes on {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules')} first.</p>"""),

            ("What creative works for local businesses on TikTok", f"""<p>On TikTok the ads that work look like posts. The ones that flop look like TV commercials somebody shrank down.</p>
<p>The technical floor from {SRC['specs']}: vertical 9:16 is recommended (at least 540 x 960 pixels; we shoot 1080 x 1920), files up to 500 MB, and videos up to 10 minutes. Non-Spark captions can't include clickable links, @ mentions or hashtags. Most local ads we'd run are 9 to 30 seconds.</p>
<!--fig:creative-->
<p>Hooks we've seen hold attention for Houston service businesses, all of them specific to a place or a moment:</p>
<ul>
<li>“This is what three Houston summers do to a pool deck.” (Then the pressure washer.)</li>
<li>“Things I'd never let a patient do before a filler appointment.” (A med spa nurse injector, talking to camera.)</li>
<li>“New on our menu this week, and yes it comes with queso.” (Owner holding the plate, Market Street patio behind.)</li>
<li>“You asked what a [your price] bathroom refresh looks like in Spring. Here.” (Before, after, price on screen.)</li>
</ul>
<p>Say the town out loud. A viewer in Kingwood who hears “Kingwood” in the first two seconds stops scrolling at a much higher rate in our experience than one who hears “the Greater Houston area.”</p>
<p>Music: business accounts should use the {SRC['cml']}, TikTok's pre-cleared library of about a million songs for organic posts, video ads and branded content. TikTok says businesses can't use the general music library commercially. That trending audio your 22-year-old employee wants to use is often off limits for a business ad.</p>
<p>Plan on fresh videos every two to four weeks; a small ZIP set sees the same ad a lot. Ten rough verticals beat one polished spot here.</p>"""),

            ("Pixel, Events API and measuring TikTok honestly", f"""<p>TikTok's reporting is generous to itself, like every platform's.</p>
<p>Start in Events Manager. After the pixel is in, verify it with the TikTok Pixel Helper Chrome extension and the <i>Test Events</i> tool, then check the <i>Diagnostics</i> tab, all described in {SRC['pixel']}. Set up events that mean money: a booked appointment, a submitted estimate form, a completed order. A “ViewContent” event on your homepage is not a conversion.</p>
<!--fig:funnel-->
<p>Then cross-check outside TikTok:</p>
<ul>
<li><b>UTMs into Google Analytics</b>, with TikTok traffic as its own source. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 tracking guide')} covers forms and calls.</li>
<li><b>Branded search.</b> Most TikTok viewers don't tap the ad. They remember your name and Google it later. Watch branded searches in Google Search Console and branded clicks in Google Ads during the test, by week.</li>
<li><b>Ask at intake.</b> “How did you hear about us?” with TikTok as a choice, on the form and at the front desk. Crude, and it catches things no pixel will.</li>
</ul>
<p>Give a test 45 to 60 days before you judge it. One week of TikTok data at $50 a day is mostly noise, especially when the algorithm is still in its learning phase.</p>"""),

            ("When TikTok ads aren't worth it for a Houston business", f"""<p>We'd tell you to skip TikTok ads, or wait, if any of these are true:</p>
<ul>
<li><b>Your budget is under about $1,500 a month in total marketing.</b> At that level, Google Business Profile, reviews and a small search campaign almost always come first.</li>
<li><b>You can't produce new videos at least monthly.</b> One ad on repeat will burn out in a few weeks.</li>
<li><b>Your customers are searching, not browsing.</b> AC repair in August, emergency plumbing, towing. Those are Google problems.</li>
<li><b>No one answers leads quickly.</b> TikTok leads go cold faster than search leads do.</li>
<li><b>Your landing page is slow or confusing on a phone.</b> Nearly every TikTok click is on a phone.</li>
</ul>
<p>And if what attracts you is the format more than the app (short video, sound on, local targeting), YouTube Shorts gets you vertical video inside Google's ad system with ZIP and radius targeting. Our {L('/blog/youtube-ads-cost-local-business-houston/', 'YouTube ads cost guide for Houston')} covers that side, and we'd often run the same videos on both.</p>"""),

            ("A first 30 days on TikTok ads", f"""<p>How we'd run the first month for a typical Woodlands or north Houston business:</p>
<ul>
<li><b>Days 1 to 7:</b> Pixel and Events API installed and tested. Organic account posting three to five times. Ten vertical videos shot in one session.</li>
<li><b>Days 8 to 21:</b> One campaign, one ad group, 8 to 15 ZIP codes, $50 a day. Three to five videos running, preferably as Spark Ads of your best organic posts.</li>
<li><b>Days 22 to 30:</b> Cut the weakest two videos. Add a lead form or switch to the Sales objective if your event volume supports it. Compare branded search and “how did you hear” answers with the month before.</li>
</ul>
<p>Our {L('/services/paid-social-advertising/', 'paid social team')} builds and runs TikTok alongside Meta for businesses across Greater Houston, and our creative team shoots the videos. If you want a plan built around your service area and budget, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("What is the minimum budget for TikTok ads?",
             "TikTok requires a campaign daily budget above $50 and an ad group daily budget above $20, according to its Business Help Center. On a lifetime budget, each ad group needs at least $20 times the number of days it runs, so a 31-day ad group needs $620. In practice, a meaningful local test for a Houston business is about $1,000 to $1,500 a month for two months."),
            ("Can I target TikTok ads by ZIP code in Houston?",
             "Yes. TikTok lets U.S. advertisers target by state, DMA, county, city and ZIP code, with up to 3,000 location selections per ad group. It does not support excluding locations or ZIP codes and does not support ZIP+4. Very small sets of ZIP codes can limit reach and raise costs, so most Woodlands or Houston businesses do better with 8 to 20 ZIPs than with two or three."),
            ("Are TikTok ads worth it for a small business in The Woodlands?",
             "They can be for visual businesses with customers under about 50, like restaurants, med spas, salons, gyms, boutiques and transformation-style home services. They're a weak fit for emergency services, B2B and businesses that can't make new videos monthly. If your total marketing budget is under about $1,500 a month, put the money into Google Business Profile, reviews and search first."),
            ("What are Spark Ads on TikTok?",
             "Spark Ads let you run an organic TikTok post as an ad, either from your own account or from a creator who authorizes it with a code. The ad shows the original handle, and the engagement counts toward the original post. The caption and display name come from the post and can't be edited in Ads Manager, so agree on captions with creators before they post."),
            ("Do TikTok lead ads give good leads for service businesses?",
             "They can if you set them up for quality. Choose the Higher Intent form type, which adds a review screen and CAPTCHA, include one real qualifying question such as service type or neighborhood, and sync leads to your CRM so they get a call within minutes. Default settings and slow follow-up are the usual reasons TikTok leads disappoint local businesses."),
        ],
        "figures": {
            "minimums": {
                "type": "stats",
                "title": "TikTok's budget floors",
                "stats": [["$50", "minimum campaign daily budget"], ["$20", "minimum ad group daily budget"], ["$620", "minimum for a 31-day lifetime ad group"], ["~25", "results before delivery settles"]],
                "note": "Source: TikTok Business Help Center (budgets, learning phase)",
                "alt": "Stats showing TikTok ads minimum budgets for local businesses in Houston and The Woodlands",
                "caption": f"From {SRC['budget']} and {SRC['learn']}. Budgets must exceed the minimums.",
            },
            "ages": {
                "type": "columns",
                "title": "Who uses TikTok, by age",
                "sub": "Share of U.S. adults in each age group who say they use TikTok",
                "labels": ["18-29", "30-49", "50-64", "65+"],
                "values": [63, 44, 30, 12],
                "highlight": [0, 1],
                "y_label": "% using TikTok",
                "note": "Source: Pew Research Center, survey Feb. 5-June 18, 2025",
                "alt": "Column chart of TikTok use by age group, for planning TikTok ads for Houston and The Woodlands businesses",
                "caption": f"National numbers from {SRC['pew']}. Overall, 37% of U.S. adults use TikTok.",
            },
            "setup": {
                "type": "steps",
                "title": "TikTok Ads Manager setup order",
                "sub": "What to finish before the first dollar is spent",
                "steps": [["Account", "Company email, second admin, Central time zone."], ["Pixel", "Tools > Events Manager > Connect Data Source > Web."], ["Objective", "Campaign tab > + Create. Reach, Lead generation or Sales."], ["Ad group", "TikTok placement only, ZIP codes, broad interests, budget."], ["Ad", "Spark posts or uploads, CTA, UTM-tagged URL, Publish all."]],
                "alt": "Five steps to set up TikTok Ads Manager for a local business in Houston and The Woodlands",
                "caption": "Doing the pixel before the first campaign saves you a month of blind spending.",
            },
            "zips": {
                "type": "map",
                "title": "Build service areas from ZIP codes",
                "sub": "TikTok can't exclude areas, so add only the places you serve",
                "highlight": ["The Woodlands", "Shenandoah", "Spring", "Magnolia", "Conroe", "Tomball"],
                "note": "Example service area for a north Houston business",
                "alt": "Map of a north Houston and The Woodlands service area built from ZIP codes for TikTok ads targeting",
                "caption": f"TikTok supports state, DMA, county, city and ZIP targeting, with no exclusions, per {SRC['loc']}.",
            },
            "spark": {
                "type": "compare",
                "title": "Regular in-feed ad vs. Spark Ad",
                "left": {"title": "Regular in-feed ad", "items": ["Uploaded straight to Ads Manager", "Shows an ad display name", "Engagement stays with the ad", "Caption can't hold links or hashtags", "Easy to spot as an ad"]},
                "right": {"title": "Spark Ad", "items": ["Runs a real organic post", "Shows your or a creator's handle", "Views and likes count on the post", "Caption comes from the post", "Looks like the rest of the feed"]},
                "alt": "Comparison of regular TikTok in-feed ads and Spark Ads for Houston and The Woodlands businesses",
                "caption": "Spark Ads are our default for local accounts. Fix the caption before the creator posts.",
            },
            "creative": {
                "type": "checklist",
                "title": "Before a TikTok ad goes live",
                "sub": "Creative checks for a local business",
                "items": ["Vertical 9:16, shot at 1080 x 1920", "Town or neighborhood named in the first 2 seconds", "A person on camera, not a logo slideshow", "Captions burned in for sound-off viewers", "Song from the Commercial Music Library", "Price or offer on screen if you have one", "9 to 30 seconds for most local ads", "Three to five versions, not one"],
                "alt": "Checklist for TikTok ad creative for local businesses in Houston and The Woodlands",
                "caption": f"Specs from {SRC['specs']}; the rest is what we've seen work.",
            },
            "funnel": {
                "type": "funnel",
                "title": "What a month of local TikTok can look like",
                "stages": [["Views in target ZIPs", "60,000"], ["Profile visits or clicks", "900"], ["Leads or bookings", "35"], ["Showed up", "22"], ["Became customers", "11"]],
                "note": "Illustrative example",
                "alt": "Illustrative funnel of TikTok ad results for a local business in The Woodlands and Houston",
                "caption": "Track the bottom three rows yourself. TikTok only sees the top two well.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: video production cost guide
    {
        "slug": "video-production-cost-houston",
        "title": "How Much Does Video Production Cost in Houston? Commercials, Social Clips and Testimonials",
        "seo_title": "Video Production Cost in Houston: A Price Guide",
        "desc": "What video production costs in Houston and The Woodlands: phone, freelancer and production company tiers, permits, drones, music licensing and a shot list.",
        "category": "Branding",
        "icons": ["YouTube", "Instagram", "TikTok"],
        "art": "b3",
        "hero": "play",
        "hero_alt": "Illustration of a video play button for video production cost in Houston and The Woodlands",
        "related": ["youtube-ads-cost-local-business-houston", "streaming-tv-ads-worth-it-small-business", "ugc-vs-influencers-creator-content"],
        "sections": [
            (None, f"""<p>Ask three Houston production companies to quote “a 30-second commercial” and you can easily get numbers like $1,800, $9,500 and $38,000. All three can be legitimate. None of them is necessarily wrong.</p>
<p>They were quoting three different jobs that happened to share a name. That's the problem with asking what video production costs.</p>
<p><b>The short answer:</b> in Houston and The Woodlands, expect roughly $500 to $2,500 for a freelancer half day with simple editing, $3,000 to $12,000 for a one-day shoot with a small crew and a finished spot plus cut-downs, and $15,000 to $75,000 and up for a scripted commercial with talent, locations and a full crew. Phone-shot content can cost almost nothing but time.</p>
<p>Those are our planning ranges from quotes we've seen and bid, not a survey. The rest of this guide is about what moves a quote up or down, so you can compare bids that look nothing alike.</p>
<!--fig:tiers-->"""),

            ("Video production price tiers in Houston", f"""<p>Most local business video falls into one of four tiers. The big difference between them is how many people are on set and how many days the job takes. Camera gear matters less than people think.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Tier</th><th>Who's on set</th><th>Typical Houston range</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>Phone and UGC</td><td>Owner, staff or a paid creator</td><td>$0 to $300 per video (creator fees vary widely)</td><td>TikTok, Reels, Shorts, testing hooks</td></tr>
<tr><td>Solo freelancer</td><td>One shooter-editor, maybe an assistant</td><td>$500 to $2,500 per half or full day, editing included or extra</td><td>Testimonials, event recaps, a batch of social clips</td></tr>
<tr><td>Small crew</td><td>Director or producer, camera, sound, lighting/grip, editor</td><td>$3,000 to $12,000 for one day plus edit</td><td>A 30-second spot with 15- and 6-second cut-downs, website hero video</td></tr>
<tr><td>Production company, scripted</td><td>Full crew, talent, hair and makeup, art department</td><td>$15,000 to $75,000+</td><td>Broadcast or streaming TV, multi-location brands, a spot you'll run for a year</td></tr>
</tbody></table></div>
<p>For a sense of labor costs behind those rates, the {SRC['bls']} put the national median wage for camera operators at $74,990 and for film and video editors at $75,420 in May 2025, and about 35% of people in both jobs are self-employed. Houston has a deep freelance pool thanks to its energy, medical and news sectors, which keeps day rates more reasonable than in Los Angeles or New York.</p>
<!--fig:labor-->
<p>Where should a local service business start? Usually tier one or two. A plumber, a dental office or a gym in Spring gets more from 12 honest clips a quarter than from one beautiful spot a year, especially on social. Production money earns its keep when the video plays on a TV screen, when your brand sells on polish (luxury remodels, custom homes, plastic surgery), or when one spot will run across YouTube, streaming TV and maybe broadcast for a long time.</p>"""),

            ("What drives the cost of a video shoot?", f"""<p>When two bids for the same idea are $8,000 apart, it's almost always one of these.</p>
<!--fig:drivers-->
<p><b>Crew days.</b> The single biggest line. A one-day shoot with four people costs far less than a two-day shoot with eight. Ask every bidder how many shoot days and how many crew they're planning, by role. The cheapest way to cut a budget is to fit the shoot into one day, which usually means one or two locations near each other.</p>
<p><b>Pre-production.</b> Scripts, storyboards, location scouting, casting. Cheap bids often skip this, and you pay for it on set when nobody knows what the next shot is.</p>
<p><b>Locations.</b> Your own office, shop or job site is free. Renting a home in The Woodlands for a day, a restaurant before opening, or a studio in the Heights adds a location fee, and anything on public property adds permits and insurance (next section).</p>
<p><b>Talent.</b> Real employees and customers are free and usually better. Paid actors add day rates, and union talent adds usage fees tied to where and how long the ad runs. Always ask whether the quote covers usage for your planned run.</p>
<p><b>Post-production.</b> Editing, color, sound mix, motion graphics, captions. Make sure the quote states how many revision rounds are included; two is normal. A third and fourth round at hourly rates is where budgets quietly double.</p>
<p><b>Deliverables.</b> One 30-second horizontal spot is one edit. The same spot plus 15- and 6-second cuts, vertical versions for TikTok and Reels, and a captioned version for the website is six or more. Each costs editing time, so list them up front.</p>
<p><b>Houston weather.</b> Summer heat and afternoon storms push outdoor shoots into early mornings, and a June shoot in Katy needs a rain date in the contract. Hurricane season runs through November. Ask who pays when weather cancels a day.</p>"""),

            ("Do you need a film permit in Houston or The Woodlands?", f"""<p>It depends on where you're standing. There's no statewide permit; the {SRC['tfc']} says the Texas Film Commission doesn't issue them and that public property like sidewalks, streets and parks is usually handled by the city. Filming entirely on private property needs only a location agreement with the owner, unless your crew or gear spills onto public space.</p>
<!--fig:permitmap-->
<p><b>Inside City of Houston limits.</b> The {SRC['hfc']} asks productions filming on general public property to submit a {SRC['hfcform']} before production, which gets a registration number you keep on set. You also need a liability insurance certificate of one million dollars per incident on file before filming. Blocking a lane or controlling traffic means hiring City of Houston police officers through the office. Most city parks need a separate permit, amplified playback needs a noise permit, and squibs or pyrotechnics need a Fire Marshal on set. The FAQ doesn't publish fees or lead times, so call them at 713-853-8386 early.</p>
<p><b>In The Woodlands.</b> The Woodlands has been a {SRC['ffw']} since September 2020, and the Film Commission runs through Visit The Woodlands. Per {SRC['wfc']}, a permit is needed when filming is commercial, will be seen by the public and takes place on property including public spaces. Apply through the {SRC['wfcapp']} with a certificate of insurance. The current FAQ asks for at least 5 business days' notice, an older version said 10, and complex or multi-location shoots need more, so we plan on two weeks. Traffic interruptions need off-duty officers, paid directly by you, and road closures go through Montgomery or Harris County depending on the spot.</p>
<p><b>Unincorporated areas</b> (much of Spring, Cypress, Klein and Magnolia) fall to the county for roads, and HOA-run parks and pools have their own rules. Shopping centers like Market Street and Hughes Landing are private property; ask management in writing.</p>
<!--fig:permitsteps-->
<p>State parks are slow. The Texas Parks and Wildlife Department typically needs several weeks, so Lake Houston Wilderness Park or Brazos Bend is not a next-Tuesday idea.</p>
<p><b>Drones</b> are their own category. Anyone flying for a business needs an FAA Part 107 remote pilot certificate, and each drone must be registered ($5, good for three years), per the {SRC['faa']}. A lot of the Houston area sits under controlled airspace around Bush Intercontinental, Hobby, Ellington, Sugar Land Regional and Conroe-North Houston Regional, which means an airspace authorization, usually through {SRC['laanc']}. Ask any drone operator for their certificate number and proof of insurance. A cousin with a DJI doesn't count.</p>"""),

            ("Deliverables checklist: what to get in writing", f"""<p>Most disputes over video come from vague scopes. Before you sign, the quote should name every one of these:</p>
<!--fig:deliverables-->
<p>Two items owners forget most. First, <b>raw footage</b>. Many shops keep it unless you ask, and it's the cheapest way to make more cuts later. Second, <b>usage rights</b>. You should own the finished videos outright or have a perpetual license for your business, and any paid talent or music license should match where the video will run. A spot licensed for “social media only” can't go on streaming TV without another check.</p>"""),

            ("A shot list for a local service business", f"""<p>Here's the shot list we'd hand a crew for one day at a typical Houston service business (a plumbing company, a dental practice, a roofing contractor). It produces a 30-second spot, two 15s, a 6-second bumper, a testimonial and a dozen vertical clips.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Shot</th><th>What it shows</th><th>Used in</th></tr></thead>
<tbody>
<tr><td>Owner to camera, 3 to 5 takes of the opening line</td><td>The problem, said in the customer's words, with the town named</td><td>Every spot, TikTok and Shorts hooks</td></tr>
<tr><td>Truck or storefront arriving</td><td>Clean vehicle, logo readable, a recognizable street or neighborhood</td><td>Spot opener, website hero</td></tr>
<tr><td>Hands doing the work</td><td>Close-ups: the tool, the part, the before and after</td><td>Cut-downs, B-roll everywhere</td></tr>
<tr><td>Tech or staff explaining one thing</td><td>A real employee answering a common question in 20 seconds</td><td>Social clips, FAQ page</td></tr>
<tr><td>Customer testimonial, seated</td><td>Two or three customers, 10 minutes each, asked open questions</td><td>Testimonial video, spot proof point</td></tr>
<tr><td>Customer handshake or reaction</td><td>The moment the job is done</td><td>Closing shot</td></tr>
<tr><td>Office, phones, front desk</td><td>A real person answering the phone</td><td>“Call us” closing line</td></tr>
<tr><td>Vertical versions of the above</td><td>Same setups, phone or second camera rotated</td><td>TikTok, Reels, Shorts</td></tr>
</tbody></table></div>
<p>For testimonials, ask questions that can't be answered with “they were great.” What was going on before you called? What almost made you pick someone else? What would you tell a neighbor? Get a signed release from every customer on camera. Our {L('/blog/social-proof-reviews-testimonials/', 'post on reviews and testimonials')} covers how to use the finished clips.</p>
<!--fig:oneday-->"""),

            ("Music licensing basics for business video", f"""<p>Music is where small businesses get burned, usually months later when a video gets muted or a letter shows up.</p>
<p>A recorded song usually has two copyrights. The {SRC['copy']} explains that a <b>musical work</b> is the composition and lyrics, while a <b>sound recording</b> is the specific recorded performance, and they're often owned and licensed separately. Putting a hit song in your ad means clearing both, which is a negotiation with a publisher and a label, priced well beyond most local budgets.</p>
<p>The practical options:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Option</th><th>Cost</th><th>Watch out for</th></tr></thead>
<tbody>
<tr><td>YouTube Audio Library</td><td>Free</td><td>Some tracks need artist credit in the description; the {SRC['ytal']} covers use in YouTube videos, so check before using it elsewhere</td></tr>
<tr><td>TikTok Commercial Music Library</td><td>Free for businesses</td><td>About a million pre-cleared songs for TikTok posts and ads; businesses can't use TikTok's general library commercially</td></tr>
<tr><td>Subscription library (Epidemic Sound and similar)</td><td>Monthly or annual plan</td><td>Per {SRC['epi']}, its Business plan covers paid online ads and client work but excludes out-of-home, radio and livestreams, with revenue limits on who qualifies</td></tr>
<tr><td>Single-track license from a stock library</td><td>Per track, priced by use</td><td>Pick the license tier for broadcast or streaming TV if the spot will air there</td></tr>
<tr><td>Original music from a composer</td><td>Quoted per project</td><td>Get a written buyout or license for all the places the spot will run</td></tr>
</tbody></table></div>
<p>Ask your production company which license they're using and whose name it's in. If the license sits in their account and they stop paying, your ad's music rights can get murky. For broadcast and streaming spots, our {L('/blog/radio-tv-advertising-cost-houston/', 'radio and TV advertising cost guide')} covers what the airtime side costs.</p>"""),

            ("How to get more for the same video budget", f"""<p>A few habits that stretch a Houston video budget further than haggling over day rates:</p>
<ul>
<li><b>Batch.</b> One well-planned day can feed a quarter of social posts, a spot and a website video. Three separate half days cost more and look less consistent.</li>
<li><b>Shoot vertical and horizontal on purpose.</b> A second camera rotated for 9:16 costs a little extra crew time and saves a reshoot for TikTok and Shorts.</li>
<li><b>Write the script around what you already have.</b> Your location, your trucks, your staff. A rented mansion in Carlton Woods doesn't sell AC repair.</li>
<li><b>Test cheap, then produce.</b> Run phone versions of three messages as ads for a few weeks. Spend production money on the one that got calls. Our {L('/blog/youtube-ads-cost-local-business-houston/', 'YouTube ads guide')} and {L(TT, 'TikTok ads setup guide')} cover how to run those tests.</li>
<li><b>Plan the edits before the shoot.</b> Every cut-down and vertical version you list up front is cheaper than one requested after the edit is locked.</li>
</ul>
<p>If the video's main home is a TV screen, read our take on {L('/blog/streaming-tv-ads-worth-it-small-business/', 'whether streaming TV ads are worth it')} before you budget for a broadcast-grade spot.</p>"""),

            ("Should you hire a production company or a marketing agency?", f"""<p>A pure production company makes the video and hands it to you. An agency with in-house creative writes the script around a campaign, shoots it, and then runs and measures the ads. The second costs more per video and usually less per customer, because the edit is built for the placement from the start.</p>
<p>Either way, ask for a reel with work for businesses like yours, a line-item quote with crew roles, shoot days, revision rounds and deliverables, and a straight answer about who owns the footage.</p>
<p>Our {L('/services/creative-branding/', 'creative and branding team')} shoots commercials, testimonials and social batches across Houston, The Woodlands and Montgomery County, and our {L('/services/ctv-ooh-streaming-radio/', 'streaming TV team')} places them. If you'd like a plan built around what you're trying to sell and where the video will run, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much does a 30-second commercial cost to produce in Houston?",
             "A simple 30-second spot shot in one day by a small Houston crew, with a few cut-downs, often lands between $3,000 and $12,000 in our experience. A scripted commercial with actors, multiple locations and a full crew commonly runs $15,000 to $75,000 or more. The biggest factors are crew size, number of shoot days, talent usage and how many edited versions you need."),
            ("Do I need a permit to film a commercial in Houston?",
             "If you film on public property inside City of Houston limits, the Houston Film Commission asks for a registration form and a liability insurance certificate of one million dollars per incident before production. Parks, amplified sound, pyrotechnics and traffic control need extra permits or hired officers. Filming entirely on private property usually needs only the owner's written permission. Call the Film Commission to confirm your plan."),
            ("Do I need a permit to film in The Woodlands, TX?",
             "Usually yes for commercial filming on property including public spaces. The Woodlands Area Film Commission, run through Visit The Woodlands, takes applications online with a certificate of insurance and asks for at least five business days of notice, more for complex or multi-location shoots. Shoots that interrupt traffic must hire off-duty officers, and road closures go through Montgomery or Harris County."),
            ("How much does a customer testimonial video cost?",
             "A testimonial video filmed by a Houston freelancer in a half day, with two or three customers and a short edit for each, often costs $800 to $3,000 in our experience. Costs rise with multiple locations, a second camera, lighting and more edited versions. Prepare open-ended questions, get signed releases and ask for vertical cuts so the clips also work on social media."),
            ("Can I use popular music in my business's video ads?",
             "Not without licenses for both the composition and the recording, which are often owned separately and rarely affordable for local ads. Use music you're licensed for instead: TikTok's Commercial Music Library for TikTok, the YouTube Audio Library for YouTube videos, or a paid library whose plan covers paid ads and the channels you'll use, such as streaming TV or broadcast."),
        ],
        "figures": {
            "tiers": {
                "type": "bars",
                "title": "Typical video cost tiers in Houston",
                "sub": "Top of each planning range, per project",
                "items": [["Phone or UGC clip", 300, "$0-$300"], ["Freelancer day", 2500, "$500-$2.5K"], ["Small crew, one day", 12000, "$3K-$12K"], ["Scripted commercial", 75000, "$15K-$75K+"]],
                "highlight": [2],
                "note": "Illustrative planning ranges, not a survey",
                "alt": "Bar chart of video production cost tiers in Houston and The Woodlands from phone clips to scripted commercials",
                "caption": "The small-crew tier is where most local business spots land.",
            },
            "labor": {
                "type": "stats",
                "title": "Who you're paying for",
                "stats": [["$74,990", "median pay, camera operators"], ["$75,420", "median pay, video editors"], ["35%", "of both jobs are self-employed"]],
                "note": "Source: BLS Occupational Outlook Handbook, May 2025, national",
                "alt": "Stats on camera operator and video editor pay behind video production costs in Houston",
                "caption": f"National medians from the {SRC['bls']}. Freelance day rates build in gear, insurance and slow weeks.",
            },
            "drivers": {
                "type": "columns",
                "title": "Where a one-day shoot budget goes",
                "sub": "Share of a typical small-crew commercial budget",
                "labels": ["Crew", "Pre-pro", "Gear", "Location", "Talent", "Post"],
                "values": [35, 10, 12, 8, 10, 25],
                "highlight": [0, 5],
                "y_label": "% of budget",
                "note": "Illustrative example",
                "alt": "Column chart of what drives video production cost in Houston, from crew and gear to editing",
                "caption": "Crew days and editing are the two lines worth questioning on any quote.",
            },
            "permitmap": {
                "type": "map",
                "title": "Who you call depends on where you shoot",
                "sub": "City of Houston, The Woodlands and county areas have different rules",
                "highlight": ["Houston", "The Woodlands", "Spring", "Cypress", "Magnolia"],
                "note": "Houston: Houston Film Commission. The Woodlands: Visit The Woodlands film office. Unincorporated roads: county.",
                "alt": "Map of film permit jurisdictions for video production in Houston, The Woodlands and unincorporated Harris and Montgomery County",
                "caption": f"From the {SRC['hfc']}, {SRC['wfc']} and {SRC['tfc']}.",
            },
            "deliverables": {
                "type": "checklist",
                "title": "Get these in the quote",
                "sub": "Video production deliverables checklist",
                "items": ["Number of shoot days and crew by role", "Every edited version, with length and aspect ratio", "Revision rounds included (two is normal)", "Captioned and uncaptioned files", "Music license type and whose name it's in", "Talent usage terms and duration", "Raw footage delivery, and how", "Ownership or license of the finished video", "Weather and reschedule policy", "Permits, insurance and drone certificate"],
                "alt": "Checklist of video production deliverables for businesses hiring a videographer in Houston and The Woodlands",
                "caption": "If a line isn't in writing, assume it's not included.",
            },
            "oneday": {
                "type": "funnel",
                "title": "One shoot day, many assets",
                "stages": [["Shoot day at your business", "1 day"], ["Finished horizontal spot", "1 x :30"], ["Cut-downs", "2 x :15, 1 x :06"], ["Testimonials", "2 to 3"], ["Vertical social clips", "10 to 12"]],
                "note": "Illustrative example",
                "alt": "Diagram of the assets one video shoot day can produce for a Houston service business",
                "caption": "Plan every version before the shoot and the edit gets cheaper.",
            },
            "permitsteps": {
                "type": "steps",
                "title": "Permits for a Houston-area shoot",
                "sub": "Order of operations when public property is involved",
                "steps": [["Pin the locations", "City of Houston, The Woodlands, county or private."], ["Call the film office", "HFC 713-853-8386 or The Woodlands film office."], ["Insurance certificate", "Liability coverage on file before filming."], ["Officers and permits", "Traffic control, parks, noise, Fire Marshal as needed."], ["Drone check", "Part 107 certificate and airspace authorization."]],
                "alt": "Five steps to get film permits for video production in Houston and The Woodlands",
                "caption": "Start two weeks out. State parks take longer.",
            },
        },
    },
]
