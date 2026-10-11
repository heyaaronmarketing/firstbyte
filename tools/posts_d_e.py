"""Long-tail post: "radio advertising cost houston" + "how much does a tv commercial cost in houston".

Research: FCC public inspection files opened and read (KTRK-TV invoices from a non-candidate political advertiser,
Feb 2024, with per-program :30 rates; a KTRH-AM political order for fall 2024; a KKBQ-FM/KGLK-FM political schedule
from early 2024). Advertisers are deliberately not named in the post., FCC political
programming fact sheet (lowest unit charge rules), Nexstar's KIAH page citing Nielsen (Houston DMA No. 6, 2.8M TV
homes), Country Aircheck on Nielsen Audio's Fall 2025 market ranks (Houston to No. 5), Radio Online's September 2026
Houston-Galveston PPM ranker, Katz/Nielsen radio reach via Radio Online, Effectv/Comcast Advertising Houston listing
(Houston Northwest Chamber) and MediaPost on Comcast's Houston interconnect, Vibe and Adwave cost guides, eMarketer on
Comcast Universal Ads, Spotify Ads pages (minimum, audio specs), AudioGo (AdsWizz) for Pandora, FitSmallBusiness
radio cost guide, Simulmedia and BeverlyBoy on commercial production costs, Influencer Marketing Hub on Spotify CPMs.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "ktrk": A("https://publicfiles.fcc.gov/api/manager/download/c039ab82-1ef7-9abb-b0a8-ba6c28352e95/169ac5bd-a249-4004-833b-b114f28900de.pdf", "a February 2024 KTRK invoice in the FCC public file"),
    "ktrk2": A("https://publicfiles.fcc.gov/api/manager/download/c039ab82-1ef7-9abb-b0a8-ba6c28352e95/ac6f00da-d839-4261-b96c-ff8aea19d857.pdf", "a second KTRK invoice from the same buyer"),
    "ktrh": A("https://publicfiles.fcc.gov/api/manager/download/22d1da61-75ad-eb85-3dab-9f7fd597c67d/cec7da4a-86c0-49b5-b287-443f6f87b29d.pdf", "a fall 2024 KTRH political order"),
    "kkbq": A("https://publicfiles.fcc.gov/api/manager/download/07f4c270-11be-7c40-fd1b-174a73ac3a99/06e4a2b8-f8d3-4a46-be4d-0f570e0fca33.pdf", "a political advertiser’s 2024 schedule on KKBQ-FM and KGLK-FM"),
    "fcc": A("https://www.fcc.gov/sites/default/files/political_programming_fact_sheet.pdf", "FCC’s political programming fact sheet"),
    "nexstar": A("https://www.nexstar.tv/stations/kiah-d-5", "Nexstar, citing Nielsen"),
    "cac": A("https://www.countryaircheck.com/news/09-25-2025/203255/", "Country Aircheck"),
    "rol": A("https://ratings.radio-online.com/content/arb033", "Radio Online’s Houston-Galveston ratings page"),
    "katz": A("https://news.radio-online.com/articles/n48781/Report-Radio-Remains-Audios-Top-Reach-Medium", "a Katz Radio Group analysis of Nielsen and Edison data"),
    "effectv": A("https://members.houstonnwchamber.org/list/member/effectv-a-comcast-company-11443", "chamber listing"),
    "mp": A("https://www.mediapost.com/publications/article/144998/comcast-reps-att-u-verse-ad-sales.html", "MediaPost"),
    "vibe": A("https://www.vibe.co/blog/how-to/local-tv-advertising-cost", "Vibe’s 2026 local TV cost guide"),
    "adwave": A("https://adwave.com/resources/cable-tv-advertising-rates", "Adwave"),
    "emk": A("https://www.emarketer.com/content/comcast-sees-opportunity-smb-streaming-advertising", "eMarketer"),
    "spot": A("https://help.adanalytics.spotify.com/about-spotify-ads-manager", "Spotify’s own help center"),
    "spotprod": A("https://ads.spotify.com/en-NL/how-it-works", "Spotify’s how-it-works page"),
    "spotspec": A("https://ads.spotify.com/ad-specs/audio-ad-specs/", "Spotify’s audio specs"),
    "audiogo": A("https://www.audiogo.com/lp/pandora-sxm", "AudioGo"),
    "imh": A("https://influencermarketinghub.com/spotify-ads-cost/", "Influencer Marketing Hub"),
    "fsb": A("https://fitsmallbusiness.com/radio-advertising-costs/", "FitSmallBusiness"),
    "sim": A("https://www.simulmedia.com/blog/tv-ad-production-costs", "Simulmedia’s 2026 production guide"),
    "bbp": A("https://beverlyboy.com/how-much-does-it-cost/how-much-does-it-cost-to-produce-a-commercial-in-houston/", "BeverlyBoy Productions"),
}

POSTS = [
    {
        "slug": "radio-tv-advertising-cost-houston",
        "title": "Radio Advertising Cost in Houston, Plus TV: Real 2026 Rates",
        "seo_title": "Radio Advertising Cost in Houston (+TV): 2026 Rates",
        "desc": "Radio advertising cost in Houston for 2026: real station rates from FCC files, TV spot prices, streaming CPMs, production costs and test budgets.",
        "category": "Paid ads",
        "icons": ["YouTube", "Search Console", "Google Analytics"],
        "art": "b5",
        "hero": "tv",
        "hero_alt": "Illustration of a television set for a guide to radio advertising cost and TV commercial cost in Houston",
        "related": ["streaming-tv-ads-worth-it-small-business", "billboard-advertising-cost-houston", "call-tracking-which-ads-make-phone-ring"],
        "sections": [
            (None, f"""<p>Radio advertising cost in Houston runs from about $25 for a :30 in a weekend daytime slot to $225 to $330 for a drive-time spot locked to a specific day on a top FM station. A big news-talk AM station has charged $550 for a non-preemptible :60 in morning drive. On TV, a :30 on a top Houston affiliate ran roughly $200 to $1,400 around the local news and $2,000 to $3,500 in primetime in early 2024.</p>
<p>All of those come from station paperwork filed with the FCC, and all of them are airtime only. Production, frequency and the length of the flight decide what you really spend, so we’ll go channel by channel and finish with the smallest test budget we’d trust.</p>"""),

            ("How much does radio advertising cost in Houston?", f"""<p>Stations don’t post rate cards. The best public evidence is the FCC’s online public inspection file, where stations have to upload political ad orders. We pulled three Houston filings from 2024 and read the line items (we’ve left the advertisers’ names out). Where an order came from a candidate inside an election window, the station had to charge its lowest rate, so read those lines as a floor.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Station and daypart</th><th>Spot</th><th>Rate per spot</th><th>Filing</th></tr></thead>
<tbody>
<tr><td>KKBQ-FM / KGLK-FM, Sunday 9 a.m. to 5 p.m.</td><td>:30</td><td>$25 to $30</td><td>Political schedule, early 2024</td></tr>
<tr><td>KKBQ-FM / KGLK-FM, Mon to Wed 10 a.m. to 3 p.m.</td><td>:30</td><td>$65 to $70</td><td>Political schedule, early 2024</td></tr>
<tr><td>KKBQ-FM / KGLK-FM, single-day morning drive (6 to 10 a.m.)</td><td>:30</td><td>$225 to $310</td><td>Political schedule, early 2024</td></tr>
<tr><td>KKBQ-FM / KGLK-FM, single-day afternoon drive (3 to 6 p.m.)</td><td>:30</td><td>$260 to $330</td><td>Political schedule, early 2024</td></tr>
<tr><td>KTRH-AM, 5 to 8 a.m. and 8 to 11 a.m., non-preemptible</td><td>:60</td><td>$550</td><td>Political order, fall 2024</td></tr>
</tbody></table></div>
<p>The country and classic rock figures come from {SRC['kkbq']}: 67 spots over six weeks for $5,005, or $74.70 a spot on average. The KTRH line is from {SRC['ktrh']}. As a cross-check, {SRC['fsb']} puts the average Houston :30 at $264.</p>
<h3>Why the same station quotes $65 and $310</h3>
<p>On that KKBQ schedule, a midday spot floating Monday through Wednesday cost $65. The same hours locked to Tuesdays cost $210. Pinning a spot to a day costs more than letting it rotate, and the weeks before an election push every rate up.</p>
<p>A few other things move a Houston radio quote:</p>
<ul><li><b>Station size.</b> In the {SRC['rol']} for September 2026, iHeartMedia’s KODA-FM led with a 10.7 share, and KGLK and KKBQ both sat in the top five.</li>
<li><b>Language.</b> The same page puts the Hispanic population at about 2.26 million of 6.2 million in the metro, and Univision’s KOVE-FM ranks in the top 10.</li>
<li><b>Preemptible vs fixed.</b> Cheaper spots can get bumped by a higher bidder; KTRH’s $550 was non-preemptible.</li>
<li><b>Market size.</b> Nielsen Audio moved Houston-Galveston up to the No. 5 radio market with the Fall 2025 survey, per {SRC['cac']}.</li></ul>"""),

            ("How much does a TV commercial cost in Houston?", f"""<p>Houston is the sixth-largest TV market in the country, with about 2.8 million TV homes, according to {SRC['nexstar']}, and broadcast prices reflect it.</p>
<p>The clearest look we found is {SRC['ktrk']} for ABC13, placed in early 2024 by a political advertiser that was not itself a candidate. That distinction matters. Under the {SRC['fcc']}, only legally qualified candidates get the “lowest unit charge,” and only in the 45 days before a primary or 60 days before a general. Other buyers pay commercial rates, so these sit close to market prices during a month of heavy political demand.</p>
<div class="bp-tbl"><table>
<thead><tr><th>KTRK daypart (Feb 2024)</th><th>:30 rate</th></tr></thead>
<tbody>
<tr><td>Overnight (after midnight)</td><td>$50 to $175</td></tr>
<tr><td>Early morning news, 4:30 and 5 a.m.</td><td>$200 to $450</td></tr>
<tr><td>Daytime talk and soaps (Tamron Hall, Live, General Hospital)</td><td>$200 to $400</td></tr>
<tr><td>Good Morning America, 7 to 9 a.m.</td><td>$700 to $800</td></tr>
<tr><td>4 p.m. hour</td><td>$650 to $700</td></tr>
<tr><td>5 p.m. and 6 p.m. news</td><td>$800 to $1,200</td></tr>
<tr><td>10 p.m. news</td><td>$1,300 to $1,400</td></tr>
<tr><td>Primetime entertainment (Will Trent, The Bachelor, American Idol)</td><td>$2,000 to $3,500</td></tr>
</tbody></table></div>
<p>The two invoices from that buyer total more than $250,000 gross over about four weeks. Ten spots in the 6 p.m. news alone came to $12,000.</p>
<!--fig:tvrates-->
<p>Rates move weekly, too. The 6 p.m. slot went from $1,000 to $1,200 inside that flight, so ask for the grid by week.</p>"""),

            ("Houston TV advertising rates on cable", f"""<p>Most local businesses start TV on cable because you can buy just part of the market. In Houston, cable ad time is sold by Comcast’s ad division, previously called Comcast Spotlight and then Effectv, now Comcast Advertising. Its {SRC['effectv']} with the Houston Northwest Chamber gives an office on Pitkin Road in Spring, 77386, and claims reach to 90 percent of Houston households. It has sold other providers’ local inventory here too; {SRC['mp']} reported it taking over AT&amp;T U-verse ad sales in Houston in 2011.</p>
<p>Cable is sold by network and zone, so a Kingwood business doesn’t pay for Sugar Land. The published ranges are vendor estimates:</p>
<ul><li>{SRC['vibe']} puts local cable CPMs at $5 to $15 and monthly packages at $500 to $2,000 in mid-size markets.</li>
<li>{SRC['adwave']} says agencies and cable providers often require $5,000 to $25,000 minimum campaign spends.</li></ul>
<p>Both companies sell self-serve streaming, so weigh their cable numbers accordingly, and on the first call ask the Comcast rep for the zone minimum and a streaming quote alongside it.</p>"""),

            ("Streaming TV advertising cost", f"""<p>Streaming, or connected TV, is bought by CPM, the price per thousand impressions, and you can target a handful of ZIP codes instead of the whole market. {SRC['vibe']} estimates open-exchange CTV CPMs at $15 to $30 before an 18 to 30 percent markup for platform fees, data and verification, and says self-serve platforms start around $50 a day, about $1,400 to $1,500 for a four-week flight. Comcast added its own entry point, Universal Ads, for smaller advertisers in January 2025, per {SRC['emk']}.</p>
<p>Run the math before you buy. At a $30 effective CPM, $3,000 buys about 100,000 impressions: five views each across 20,000 target households, or half a view each across 200,000, which nobody will remember.</p>
<p>Streaming is the most targeted way onto the big screen, and it usually costs more per thousand than broadcast. Our post on <a href="/blog/streaming-tv-ads-worth-it-small-business/">whether streaming TV ads are worth it</a> covers when that trade makes sense.</p>"""),

            ("How much do Spotify and streaming audio ads cost?", f"""<p>Streaming audio has the lowest entry price of anything in this guide.</p>
<ul><li><b>Spotify.</b> Self-serve campaigns start at 250 in your local currency, per {SRC['spot']}. Audio ads run up to 30 seconds, and {SRC['spotspec']} recommend no more than 65 words for a :30. {SRC['spotprod']} says production through its tool is free.</li>
<li><b>Pandora.</b> {SRC['audiogo']}, the AdsWizz self-serve tool for Pandora, starts at $250 with pay-as-you-go billing. Campaigns run by SiriusXM Media’s own team need a $10,000 minimum.</li>
<li><b>iHeartRadio.</b> Its streaming inventory is usually sold by the same local reps who sell iHeart’s Houston stations. Ask for both on one quote.</li></ul>
<p>On price, {SRC['imh']} says Spotify CPMs typically run $15 to $25, and {SRC['fsb']} lists Pandora audio at about $20 per thousand. A $1,500 month at $20 buys roughly 75,000 plays, with room in each :30 for one idea and one call to action.</p>
"""),

            ("How much does a local TV commercial cost to make?", f"""<p>Then there’s making the thing. Typical production ranges:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Asset</th><th>Typical cost</th><th>Source</th></tr></thead>
<tbody>
<tr><td>:30 TV spot, local production</td><td>$3,000 to $15,000</td><td>Simulmedia</td></tr>
<tr><td>:30 TV spot, small Houston budget</td><td>$1,500 to $3,500</td><td>BeverlyBoy Productions</td></tr>
<tr><td>:30 TV spot, higher production value in Houston</td><td>$20,000 to $30,000</td><td>BeverlyBoy Productions</td></tr>
<tr><td>Radio :30 or :60, agency produced</td><td>$350 to $3,500+</td><td>FitSmallBusiness</td></tr>
<tr><td>Spotify :30</td><td>Free in Ad Studio</td><td>Spotify</td></tr>
</tbody></table></div>
<p>{SRC['sim']} adds that music licensing can run $1,000 to $30,000 and talent $500 to $50,000 a day. The Houston figures are from {SRC['bbp']}.</p>
<p>Our habit is to shoot once and cut many. A half-day shoot can yield a :30 for cable, a :15 for streaming, vertical cutdowns for <a href="/services/paid-social-advertising/">Meta and TikTok</a> and stills for the website. For radio, a station-produced spot is cheap and sounds like every other spot in the break; on a flight longer than a month, a custom script from a <a href="/services/creative-branding/">creative team</a> usually earns back its cost.</p>"""),

            ("Reach, frequency and GRPs in plain English", f"""<p><b>Reach</b> is how many different people or homes saw or heard your ad at least once. <b>Frequency</b> is how many times, on average, each of them did. <b>A rating point</b> is 1 percent of the audience you’re measuring. With about 2.8 million TV homes in Houston, one household rating point is roughly 28,000 homes.</p>
<p><b>GRPs</b> (gross rating points) add up the ratings of every spot: a 2-rated spot run ten times is 20 GRPs. They also equal reach times frequency, so 40 percent of homes reached 2.5 times on average is 100 GRPs.</p>
<p>A hypothetical: a 10 p.m. news spot costs $1,400 and earns a 3 household rating. That’s about 84,000 homes, roughly $16.70 per thousand. Cheap per thousand, except you’re paying for Katy, Pearland and Baytown when you only serve Magnolia.</p>
<p>Radio uses AQH (average quarter-hour audience) in place of ratings, but the math is the same. Ask every rep for the CPM in your target age group; a $40 overnight spot nobody hears is the expensive one.</p>
<p>There’s no fixed rule on frequency. We plan for at least three exposures a week per person for four weeks or more before judging anything; thinner schedules rarely produce a readable result.</p>"""),

            ("Minimum test budget for each channel", f"""<p>Our working numbers for a test that can show a result in one part of Greater Houston. These are planning rules of thumb, not published rates.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Minimum test (media)</th><th>Flight</th><th>Production</th></tr></thead>
<tbody>
<tr><td>Spotify or Pandora audio</td><td>$1,000 to $3,000 a month</td><td>6 to 8 weeks</td><td>$0 to $500</td></tr>
<tr><td>Streaming TV (CTV), a few ZIPs</td><td>$3,000 to $6,000 a month</td><td>6 to 8 weeks</td><td>$1,500 to $5,000</td></tr>
<tr><td>Cable, one or two Comcast zones</td><td>$3,000 to $8,000 a month</td><td>4 to 8 weeks</td><td>$1,500 to $15,000</td></tr>
<tr><td>Broadcast radio, one or two stations</td><td>$6,000 to $12,000 a month</td><td>4+ weeks</td><td>$0 to $1,500</td></tr>
<tr><td>Broadcast TV, one station</td><td>$25,000 to $50,000</td><td>3 to 4 weeks</td><td>$3,000 to $15,000</td></tr>
</tbody></table></div>
<p>Broadcast costs more because you’re paying for the whole metro. Twenty radio spots a week at $75 to $150 lands in that range quickly, and one TV week mixing daytime, morning news and a few evening news spots at KTRK’s 2024 rates clears $10,000.</p>
<!--fig:test-->
<p>If those numbers are a big share of your budget, start with streaming. Our guide to <a href="/blog/set-a-marketing-budget-small-business/">setting a marketing budget</a> covers how to size the pot first.</p>"""),

            ("How to buy and track radio and TV in Houston", f"""<h3>Direct, rep firm or agency</h3>
<p><b>Direct</b> means calling the station or Comcast. That works for one station, though every rep will tell you theirs is the right one.</p>
<p><b>Agencies</b> buy across stations and compare them on cost per thousand. Broadcast still runs on a 15 percent agency commission built into the gross rate. You can see it in the filings: the KTRK invoice shows $160,900 gross and a $24,135 commission, and {SRC['ktrh']} shows $46,200 gross with $6,930 commission. Both are exactly 15 percent, and that commission is often baked into the rate whether you use an agency or not. Ask the station what you’d pay direct.</p>
<h3>Check the FCC file yourself</h3>
<p>Before you negotiate, search the station’s call letters at publicfiles.fcc.gov and open Political Files for a recent year. You’ll find invoices like {SRC['ktrk2']}. Keep the rule in mind: a candidate’s order inside the election window runs at the lowest unit charge, so treat it as a floor. Orders from non-candidate political buyers sit closer to what a business would pay.</p>
<h3>Track it like any other ad</h3>
<!--fig:track-->
<p>Broadcast gives you no clicks, so set up measurement before the first spot runs:</p>
<ul><li><b>A dedicated phone number</b> read in the spot and shown on screen. Our <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking guide</a> walks through the setup.</li>
<li><b>A vanity URL</b> like yoursite.com/radio that redirects to a page with UTM tags, so Google Analytics shows the visits.</li>
<li><b>Branded search lift.</b> Record branded queries in Search Console and Google Ads for four weeks before the flight, then compare. It’s usually the clearest signal you’ll get.</li>
<li><b>An offer code</b> that only exists on air (“mention KTRH”).</li>
<li><b>Holdout areas</b> for cable and streaming: run in some zones or ZIPs and not others, then compare calls and leads.</li></ul>"""),

            ("When broadcast beats digital for a local business, and when it doesn’t", f"""<p>Radio still has the reach. AM/FM reaches 93 percent of U.S. adults each month and took 61 percent of ad-supported audio listening time in the fourth quarter of 2025, according to {SRC['katz']}. In a metro where people spend an hour a day on I-45, I-10 and the Grand Parkway, that reach is real.</p>
<!--fig:reach-->
<p>Broadcast earns its price when most adults in the metro are possible customers (injury law, HVAC, roofing after hail, car dealers, big hiring pushes), when several locations spread you across the region, or when you want Spanish-language reach at scale. It also helps once search and your Business Profile already catch demand and the job is getting more people to look you up by name.</p>
<p>It’s the wrong buy if you serve a few ZIP codes, sell to a narrow group like B2B buyers, or one month of broadcast would eat most of your annual budget. Streaming audio and CTV in your ZIPs, with <a href="/services/search-marketing/">Google Ads</a> catching the searches they create, will beat a metro-wide schedule. Billboards sit somewhere in the middle; see our <a href="/blog/billboard-advertising-cost-houston/">Houston billboard cost guide</a>.</p>
<p>To get started, request two four-week proposals, one from a radio station whose audience matches your customers and one from Comcast’s office in <a href="/digital-marketing-agency-spring-tx/">Spring</a>, each with CPMs for your target age group. Check the station’s political file before you answer.</p>
<p>Then sort out measurement, which is where most broadcast tests fall apart. If your Google Ads account mixes branded and generic searches in one campaign, a radio flight can lift your name searches and you’ll never see it. That’s one of the first things we look at in a free <a href="/contact/">Ad Spend Leak Check</a>: we record a walkthrough of your account and tell you whether your brand traffic is separated cleanly enough to measure a flight against. When you’re ready to plan the flight itself, our <a href="/services/ctv-ooh-streaming-radio/">CTV, streaming and radio team</a> buys and tracks it.</p>"""),
        ],
        "faq": [
            ("How much does a 30-second radio ad cost in Houston?",
             "Public FCC filings show Houston FM stations charging roughly $25 to $70 for a :30 in weekend or midweek daytime rotations and $225 to $330 for drive time locked to a specific day. A major news-talk AM station charged $550 for a non-preemptible :60 in morning drive. FitSmallBusiness lists the Houston average :30 at $264. Rates shift with season and demand."),
            ("How much does a local TV commercial cost?",
             "Plan for two costs. Production for a local :30 usually runs $1,500 to $15,000 depending on crew, talent and music. Airtime on a top Houston station ran about $200 to $450 for daytime, $800 to $1,400 for local news and $2,000 to $3,500 for primetime in early 2024 filings. Cable zones and streaming TV cost less and can target part of the metro."),
            ("How much do Spotify ads cost?",
             "Spotify's self-serve tool requires a minimum budget of 250 in your local currency, and its free production tool can make the ad for you. Third-party guides put Spotify CPMs at about $15 to $25 per thousand ads served. Audio ads run up to 30 seconds, and you can target by location, so a Houston business can run a small test without buying the whole market."),
            ("Is radio or TV better for a small business?",
             "For most small businesses with one location, radio and streaming are the more affordable test, and cable or streaming TV beats broadcast TV because you can buy only your area. Broadcast TV makes sense when most adults in the metro could be customers and you can afford three or four weeks at steady frequency. Track every option with a dedicated number and branded search."),
            ("What is a GRP in advertising?",
             "A gross rating point is one percent of a target audience, added up across every ad in a schedule. Ten spots that each reach 2 percent of Houston TV homes total 20 GRPs. GRPs also equal reach times frequency. Stations use GRPs and cost per point to price and compare schedules, so ask for both on any proposal."),
        ],
        "figures": {
            "tvrates": {
                "type": "bars",
                "title": "What a :30 cost on KTRK in early 2024",
                "sub": "Top of each daypart’s range, from an FCC public file invoice",
                "items": [
                    ["Overnight", 175, "$50–$175"],
                    ["Daytime talk", 400, "$200–$400"],
                    ["Good Morning America", 800, "$700–$800"],
                    ["5 and 6 p.m. news", 1200, "$800–$1,200"],
                    ["10 p.m. news", 1400, "$1,300–$1,400"],
                    ["Primetime shows", 3500, "$2,000–$3,500"],
                ],
                "highlight": [4],
                "note": "Source: KTRK invoice, FCC public inspection file, Feb 2024",
                "alt": "Bar chart of how much a TV commercial costs in Houston on KTRK by daypart, from overnight to primetime",
                "caption": f"Rates from {A('https://publicfiles.fcc.gov/api/manager/download/c039ab82-1ef7-9abb-b0a8-ba6c28352e95/169ac5bd-a249-4004-833b-b114f28900de.pdf', 'a non-candidate political buyer’s invoice')}, which paid commercial rates, not the candidate discount.",
            },
            "test": {
                "type": "steps",
                "title": "How we run a first radio or TV test",
                "sub": "Our order of operations for a Houston-area business",
                "steps": [
                    ["Fix the landing spot", "Make sure search ads, your Business Profile and site catch people who look you up."],
                    ["Pick one channel", "Start with streaming audio or CTV unless most of the metro could buy from you."],
                    ["Get CPM quotes", "Ask each rep for cost per thousand in your target age group, by week."],
                    ["Build tracking first", "Dedicated number, vanity URL, offer code and a branded search baseline."],
                    ["Run 4 to 8 weeks", "Hold frequency near three a week, then compare to the weeks before."],
                ],
                "alt": "Five steps for testing radio advertising in Houston, from fixing search to tracking a four to eight week flight",
                "caption": "A short, well-tracked flight tells you more than any station’s ratings book.",
            },
            "track": {
                "type": "checklist",
                "title": "Tracking checklist for broadcast ads",
                "sub": "Set these up before the first spot airs",
                "items": [
                    "Call tracking number used only in the spot",
                    "Vanity URL that redirects with UTM tags",
                    "Branded search baseline from Search Console",
                    "On-air-only offer code",
                    "Holdout ZIPs or cable zones for comparison",
                    "“How did you hear about us?” on every intake",
                ],
                "alt": "Checklist for tracking radio and TV advertising in Houston with call numbers, vanity URLs and branded search",
                "caption": "Branded search lift is usually the clearest sign a broadcast flight is working.",
            },
            "reach": {
                "type": "stats",
                "title": "Why Houston broadcast still gets attention",
                "stats": [
                    ["93%", "of U.S. adults reached by AM/FM radio each month"],
                    ["61%", "of ad-supported audio time went to radio, Q4 2025"],
                    ["2.8M", "TV homes in the Houston market, sixth-largest"],
                ],
                "note": "Sources: Katz Radio Group via Radio Online (Nielsen, Edison); Nexstar citing Nielsen",
                "alt": "Stat tiles showing radio reach and Houston TV homes for radio and TV advertising cost decisions in Houston",
                "caption": f"Reach is broadcast’s strength; paying for the whole metro is its cost ({A('https://news.radio-online.com/articles/n48781/Report-Radio-Remains-Audios-Top-Reach-Medium', 'Radio Online')}).",
            },
        },
    },
]
