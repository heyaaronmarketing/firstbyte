"""One long-tail post: is Angi Leads worth it for contractors, Thumbtack vs Angi, and Angi vs Google Local Services Ads.

Research: top results for "is angi leads worth it for contractors" / "thumbtack vs angi" (Hatch, Phonely, Housecall
Pro, Superdupr, Jobber community); facts verified against Angi's pro help center (lead credit and billing FAQ
articles on intercom.help/angi), Angi Leads membership FAQ (prohelp.homeadvisor.com), Angi Inc.'s FY2025 Form 10-K
(SEC), Angi's Q2 2026 earnings call as reported by MarketBeat, Thumbtack's own pro pages (thumbtack.com/pro and
/pro/jobs) and pro community forum, Google's Local Services Ads "How leads work" help page, PPC Land on the
October 1, 2026 missed-call charge change, FTC press releases on the HomeAdvisor final order (April 2023) and
refunds (November 2023), and WordStream/LocaliQ 2026 Google Ads benchmarks. Reddit could not be fetched, so no
Reddit claims are made.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "angibill": A("https://intercom.help/angi/en/articles/11024858", "Angi’s billing FAQ for pros"),
    "angicredit": A("https://intercom.help/angi/en/articles/11403440", "Angi’s lead credit help article"),
    "angimember": A("https://prohelp.homeadvisor.com/membership-faq", "Angi Leads membership FAQ"),
    "angifaq": A("https://pro.homeadvisor.com/help/faqs", "Angi Leads’ service professional FAQ"),
    "tenk": A("https://www.sec.gov/Archives/edgar/data/1705110/000170511026000011/angi-20251231.htm", "Angi’s 2025 annual report (Form 10-K)"),
    "q2": A("https://www.marketbeat.com/instant-alerts/angi-q2-earnings-call-highlights-2026-08-05/", "Angi’s Q2 2026 earnings call"),
    "ftcorder": A("https://www.ftc.gov/node/80884", "the FTC"),
    "ftcrefund": A("https://www.ftc.gov/node/82041", "FTC refund announcement"),
    "ttpro": A("https://www.thumbtack.com/pro", "Thumbtack’s pro page"),
    "ttjobs": A("https://www.thumbtack.com/pro/jobs", "Thumbtack’s pricing page for pros"),
    "ttprice": A("https://community.thumbtack.com/discussion/2397/how-leads-are-priced", "a thread on Thumbtack’s own pro community"),
    "ttopps": A("https://community.thumbtack.com/discussion/2360/leads-vs-opportunities", "Thumbtack’s community moderators"),
    "lsaleads": A("https://support.google.com/localservices/answer/7195435?hl=en", "Google’s “How leads work” page"),
    "lsa20": A("https://ppc.land/google-lsa-advertisers-face-missed-call-charges-from-october-1/", "PPC Land"),
    "lsahelp": A("https://support.google.com/google-ads/answer/6224841", "Google’s Local Services Ads help page"),
    "wordstream": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream/LocaliQ’s 2026 benchmarks"),
    "hatch": A("https://www.usehatchapp.com/blog/is-angi-leads-worth-it", "Hatch, citing Jobber"),
    "jobber": A("https://community.getjobber.com/discussions/marketing-forum/is-angi-worth-it-for-home-service-business-owners/13803", "Jobber’s community forum"),
}

POSTS = [
    {
        "slug": "angi-vs-thumbtack-leads-worth-it-contractors",
        "title": "Is Angi Leads Worth It for Contractors? Angi vs Thumbtack vs LSA",
        "seo_title": "Is Angi Leads Worth It for Contractors? (2026)",
        "desc": "Is Angi Leads worth it for contractors? How Angi, Thumbtack and Google LSA charge in 2026, plus a cost-per-booked-job worksheet for Houston pros.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Google Business Profile", "Google Analytics"],
        "art": "b4",
        "hero": "tools",
        "hero_alt": "Illustration of a contractor toolbox with a wrench and screwdriver for a guide on whether Angi leads are worth it for Houston contractors",
        "related": ["local-services-ads-vs-google-ads-home-services", "understanding-cost-per-lead", "call-tracking-which-ads-make-phone-ring"],
        "sections": [
            (None, f"""<p>Is Angi Leads worth it for contractors? For most established Houston shops, only as a gap-filler. Angi matches each homeowner request with more than one pro, it doesn’t publish its lead prices, and you pay for the lead whether or not you win the job. It can pay off for a new business with few reviews, or to fill a slow month, as long as you call back within minutes and judge it on cost per booked job instead of cost per lead.</p>
<p>Thumbtack and Google Local Services Ads charge differently, and for most trades we’d put the first marketing dollar into LSA and a Google Business Profile before either marketplace.</p>
<p>Picture a three-truck plumbing company in Spring. An Angi rep calls to say how many homeowners in 77379 asked for a plumber last month. The owner’s Google profile has 40 reviews and brings in a few calls a week. Where should the next $1,500 a month go? Each platform’s own help pages and filings answer more of that than the sales calls do, and the worksheet further down turns it into your numbers.</p>"""),

            ("Is Angi Leads worth it for contractors in your situation?", f"""<p>It depends mostly on how many reviews you have and how fast you answer the phone. For Houston-area trades, we’d call it like this:</p>
<ul>
<li><b>Brand-new business, under 15 reviews.</b> Often yes, for a few months. Every job you win can become a Google review.</li>
<li><b>Established shop, 50+ reviews, steady calls.</b> Usually no, except to fill a known slow stretch. You’d be paying to race other pros for customers who might find you on Google anyway.</li>
<li><b>Emergency trades (HVAC repair, plumbing, electrical).</b> Only if someone answers within minutes, every time, including Saturdays in August.</li>
<li><b>High-ticket trades (roofing, remodeling, pools).</b> Mixed. The ticket can absorb a pricey lead, but homeowners collecting three bids push hard on price.</li>
<li><b>Small jobs (handyman, cleaning, mowing).</b> The lead fee eats too much of a small ticket.</li>
</ul>
<p>One number worth knowing: on {SRC['q2']} in August 2026, CEO Jeff Kip said pros are now winning about one in six leads, up from roughly one in nine two summers earlier, according to MarketBeat’s summary. That’s real progress. It still means the average pro pays for five leads that go to someone else for every one they win.</p>
<p>If your average job brings in enough gross profit to cover six lead fees with room to spare, Angi can work. If it doesn’t, no amount of hustle fixes the math.</p>"""),

            ("How much does Angie’s List charge for leads in 2026?", f"""<p>Angi doesn’t publish a rate card, and that’s the first thing to understand. {SRC['angibill']} says only that “lead pricing varies based on task, homeowner location, and demand for the work.” The older {SRC['angifaq']} just says different sized jobs carry different lead fees. A replacement AC system lead in Cypress will cost more than a faucet repair lead in Conroe; you see your price in your account or from a rep.</p>
<p>What Angi does spell out:</p>
<ul>
<li><b>Monthly budget is a target, not a cap on opportunities.</b> Your budget is “the target dollar value of leads that Angi will match you with each month.” If you accept extra “Opportunities,” the lead fee is charged right away and billed on top of that budget.</li>
<li><b>Billing schedule.</b> Without an annual subscription you’re billed weekly (Wednesday for bank accounts, Friday for cards). With an annual subscription, automatic leads bill monthly on your agreement date.</li>
<li><b>Membership is annual.</b> The {SRC['angimember']} says you can cancel any time, but the membership “is still active the length of the paid term,” and it auto-renews unless stated otherwise.</li>
</ul>
<p>Third-party guides fill the gap with estimates. {SRC['hatch']} puts typical Angi leads at $15 to $85 each with an annual membership around $300. Treat those as rough, older ranges; your quote is what counts.</p>
<h3>Angi, HomeAdvisor and Angie’s List are one company</h3>
<p>HomeAdvisor and Angie’s List combined years ago, the company rebranded as Angi, and HomeAdvisor’s pro product now goes by Angi Leads. {SRC['tenk']} says the company still operates under the Angi, Angie’s List, HomeAdvisor and Handy brands, and that IAC completed its spin-off of Angi on March 31, 2025. The same filing reports about 16 million projects in 2025 and roughly 111,000 average monthly active pros.</p>
<!--fig:scale-->
<p>The filing says lead revenue “comprises fees paid by Pros for consumer matches.” Read that twice. Angi gets paid when it matches you, and winning the job is on you.</p>"""),

            ("What the FTC’s HomeAdvisor order means for you", f"""<p>In March 2022 the FTC filed an administrative complaint against HomeAdvisor, and in April 2023 {SRC['ftcorder']} approved a final order. The agency alleged that since at least mid-2014, HomeAdvisor made false, misleading or unsubstantiated claims about the quality and source of the leads it sold, and told pros its leads turned into jobs at rates it couldn’t back up. It also alleged sales agents described an optional one-month mHelpDesk subscription as free when it wasn’t.</p>
<p>The order required up to $7.2 million in redress and bars the company from misrepresenting its leads, including claiming they come from people ready to hire. In November 2023, the {SRC['ftcrefund']} said more than $3 million in checks were going to 110,372 businesses, with a separate claims process for mHelpDesk payments.</p>
<p>In practice: get any close-rate promise from a rep in writing, read the term and renewal date before you sign, and check your first statement for add-ons you didn’t ask for. We don’t think the order means Angi leads are fake today. It does mean a lead marketplace’s own description of its leads isn’t evidence. Your call log is.</p>"""),

            ("How much does Thumbtack charge contractors?", f"""<p>Thumbtack has no signup or subscription fee. According to {SRC['ttjobs']}, “you pay when a new customer contacts or hires you,” and what you’re charged “depends on the size of the job and your location.” You set how much you’re willing to spend each week, and during signup Thumbtack shows what a lead costs in your area.</p>
<p>Thumbtack doesn’t publish a per-lead price list either. These details matter more than the sticker price:</p>
<ul>
<li><b>Direct leads vs Opportunities.</b> A direct lead is a customer who picked you and reached out. Opportunities are requests where you weren’t the customer’s pick, and you can pay to respond. {SRC['ttopps']} have acknowledged pros confuse the two.</li>
<li><b>Competition per request.</b> {SRC['ttpro']} tells pros that “customers get quotes from up to 5 pros.” So a direct lead is still a competitive lead.</li>
<li><b>Max lead price settings.</b> You can cap what you pay by service. In {SRC['ttprice']}, a furniture-assembly pro posted an $83.25 charge for a two-hour job that was also sent to two other pros. The moderator’s fix: revisit max lead price settings. Set caps on day one.</li>
<li><b>Refunds aren’t automatic.</b> A lead that doesn’t book is still a charged lead.</li>
</ul>
<p>In our read, Thumbtack’s mix leans toward smaller, single-visit jobs. Great for a handyman in Tomball filling Tuesdays, a harder fit for a remodeler chasing a $40,000 kitchen.</p>"""),

            ("Thumbtack vs Angi for contractors: side by side", f"""<p>We put both marketplaces next to Google Local Services Ads, using only what each company states on its own pages.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Angi Leads</th><th>Thumbtack</th><th>Google LSA</th></tr></thead>
<tbody>
<tr><td>Signup cost</td><td>Annual membership on many plans; price quoted by sales</td><td>No signup or subscription fee</td><td>No fee; Google screening and verification</td></tr>
<tr><td>What you pay for</td><td>Each consumer match, plus any Opportunities you accept</td><td>When a new customer contacts or hires you</td><td>Calls, messages and bookings from your ad</td></tr>
<tr><td>Published lead prices?</td><td>No; varies by task, location, demand</td><td>No; varies by job size and location</td><td>No; varies by location, job type, lead type</td></tr>
<tr><td>Who else gets the lead</td><td>Matched with multiple pros</td><td>Customers get quotes from up to 5 pros</td><td>Customer chose your listing (may call others)</td></tr>
<tr><td>Budget control</td><td>Monthly target budget</td><td>Weekly budget, max price per lead</td><td>Average weekly budget, monthly max</td></tr>
<tr><td>Bad-lead credits</td><td>Request within 45 days for listed reasons; not for annual subscribers</td><td>Not automatic for leads that don’t book</td><td>Automatic review over 30 days</td></tr>
<tr><td>Contract</td><td>Annual terms common; auto-renews</td><td>None</td><td>None</td></tr>
</tbody></table></div>
<p>For most Houston trades, Thumbtack is the lower-commitment test because there’s no membership and you can set a price ceiling. With Angi you’re often signing up for a year. If you only try one marketplace, try the one you can walk away from.</p>"""),

            ("Angi vs Google Local Services Ads", f"""<p>This is the comparison that matters most. LSA puts your listing at the top of Google for searches like “water heater repair Kingwood,” with your reviews and the Google Verified badge, and the homeowner picks you instead of an algorithm handing their request to several pros.</p>
<p>{SRC['lsaleads']} lays out what you pay for:</p>
<ul>
<li>Calls you answer, or calls you return and connect on.</li>
<li>Messages, voicemails and booking requests.</li>
<li>Missed calls during business hours when the caller stays on the line more than 20 seconds. {SRC['lsa20']} reported Google started charging for these on October 1, 2026.</li>
</ul>
<p>And what you don’t: spam and duplicates, follow-up contacts from the same customer within 15 days, missed calls outside your hours, and callers who hang up at a phone menu without pressing a key. Google reviews charged leads over 30 days and credits low-quality or invalid ones automatically. Message leads are usually priced lower than phone leads.</p>
<p>LSA has its own discipline. {SRC['lsahelp']} says that if you regularly fail to answer calls or respond to messages, your ad ranking may be affected. So it rewards the same fast-answer habits shared leads do, minus the race against four other pros.</p>
<p>For HVAC, plumbing, electrical, roofing and most other eligible trades, LSA is where we’d start; see <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs Google Ads for home services</a>.</p>"""),

            ("Shared leads vs exclusive leads, and the speed-to-lead reality", f"""<p>A shared lead is one request sold to several businesses. An exclusive lead is a person who contacted you and only you: a call from your Google profile, a form on your website, an LSA call. They may still shop around, but you start without four competitors calling the same minute.</p>
<p>With shared leads, the first pro to reach a homeowner often sets the price and the appointment. Angi builds that into its credit rules: per {SRC['angicredit']}, you should try to call the homeowner within 24 hours of receiving the lead to be eligible for a credit. Twenty-four hours is far too slow to win. Picture a Katy homeowner with a dead AC on a 98-degree afternoon. They’ll book whoever calls back while they’re still standing in the hallway.</p>
<p>Before buying a single shared lead, we’d have this routine running:</p>
<!--fig:speed-->
<p>On credits: Angi requires the lead to be under 45 days old, reviews requests within five business days, and credits expire after six months. Read the fine print on that same page, too. It says pros on an annual subscription can report bad leads but don’t receive credits, which is worth knowing before a rep talks you into the annual plan.</p>
<p>If nobody can answer within minutes on a Tuesday afternoon in July, don’t buy shared leads on any platform. You’ll pay for the lead and someone else will book the job.</p>"""),

            ("A cost-per-booked-job worksheet (with illustrative math)", f"""<p>Cost per lead is what the platforms show you. Cost per booked job is what pays your techs:</p>
<p><b>Cost per booked job = total spend for the month ÷ jobs sold from that source</b></p>
<p>Compare it with the gross profit on an average job from that source (more on the lead side in <a href="/blog/understanding-cost-per-lead/">understanding cost per lead</a>). The table models a hypothetical HVAC repair shop north of Houston. Every number is an illustrative assumption, not a quote from any platform.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Illustrative example</th><th>Angi (shared)</th><th>Thumbtack</th><th>Google LSA</th><th>Google Search ads</th></tr></thead>
<tbody>
<tr><td>Assumed cost per lead</td><td>$65</td><td>$45</td><td>$70</td><td>$91</td></tr>
<tr><td>Leads in the month</td><td>20</td><td>20</td><td>20</td><td>15</td></tr>
<tr><td>Monthly spend</td><td>$1,300</td><td>$900</td><td>$1,400</td><td>$1,365</td></tr>
<tr><td>Reached a live person</td><td>12</td><td>14</td><td>17</td><td>13</td></tr>
<tr><td>Appointments set</td><td>6</td><td>7</td><td>11</td><td>9</td></tr>
<tr><td>Jobs sold</td><td>3</td><td>3</td><td>6</td><td>5</td></tr>
<tr><td><b>Cost per booked job</b></td><td><b>$433</b></td><td><b>$300</b></td><td><b>$233</b></td><td><b>$273</b></td></tr>
<tr><td>Left after lead cost ($450 gross profit per job)</td><td>$17</td><td>$150</td><td>$217</td><td>$177</td></tr>
</tbody></table></div>
<p>Every figure in that table is an assumption chosen to show the mechanics, and Angi’s line leaves out any annual membership. For real search benchmarks, see our <a href="/blog/google-ads-cost-per-click-houston-benchmarks/">Houston Google Ads CPC numbers</a>.</p>
<!--fig:funnel-->
<p>Notice what moves the result. A cheaper lead didn’t win. The source where more people picked up and booked did.</p>
<!--fig:cpbj-->
<p>To fill this in for real, you need to know which calls came from where. Use a tracking number per source; see our guide to <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking</a>. Run each source for at least 60 days before deciding, and longer if your trade is seasonal.</p>"""),

            ("When lead marketplaces make sense, and when to move to owned channels", f"""<p>Marketplaces are a tool with a specific job. Good times to use them:</p>
<ul>
<li><b>Your first six months.</b> A new electrician in Magnolia with eight reviews won’t win the map pack yet. Marketplace jobs pay bills while you build reviews.</li>
<li><b>Known slow months.</b> A cooling-heavy HVAC shop that’s busy May through September can buy leads in January and February, then pause. See our <a href="/blog/hvac-marketing-houston-the-woodlands/">HVAC marketing guide for Houston</a>.</li>
<li><b>Testing a new service or area.</b> Thinking about adding gutters, or pushing from The Woodlands into Katy along the Grand Parkway? A month of leads tells you if demand is there.</li>
<li><b>Overflow after a storm.</b> Roofers see demand jump after spring hail. See <a href="/blog/roofing-marketing-houston-storm-season/">roofing marketing for Houston storm season</a>.</li>
</ul>
<p>Signs it’s time to shift budget to channels you own:</p>
<ul>
<li>Your cost per booked job on the marketplace is higher than on LSA or Search for two months running.</li>
<li>You have 30 or more recent Google reviews and show up in the map pack for your main service in your home town.</li>
<li>You’re losing jobs on price to the same competitors every week.</li>
</ul>
<p>Owned channels, in the order we’d build them:</p>
<ol>
<li>A complete <a href="/blog/google-business-profile-number-one-asset/">Google Business Profile</a> with photos, services and a steady review routine.</li>
<li>Google Local Services Ads with accurate hours and someone answering.</li>
<li><a href="/services/search-marketing/">Google Search ads</a> for high-value services like replacements, repipes and roof replacements.</li>
<li>A fast website with a page for each service and each town you serve. Our <a href="/services/web-design-seo-pr/">web design and SEO team</a> builds these for contractors.</li>
</ol>
<!--fig:shift-->
<p>The difference shows up in year two. Stop paying a marketplace and the leads stop the same week. A review from a Magnolia homeowner or a service page that ranks for “water heater replacement Spring” keeps working after you stop spending on it.</p>"""),

            ("What contractors say about Angi and Thumbtack", f"""<p>We read contractor threads on {SRC['jobber']} and Thumbtack’s own pro community. The repeat complaints:</p>
<ul>
<li>Low yield. A landscaper on Jobber’s forum wrote that over a year he’d “only gotten 5 or 6 good leads.”</li>
<li>Shared leads that turn every call into a price war, and homeowners who were only browsing.</li>
<li>Not realizing the Angi agreement ran a full year until trying to cancel. One owner said early termination can cost about 35% of the remaining contract.</li>
<li>Billing after the fact. On the same forum, a Thumbtack user reported a $91 charge months after cancelling.</li>
</ul>
<p>Forum posts skew negative, and these are individual accounts, so treat them as things to check in your own contract rather than a verdict.</p>
<p>A next step that takes one evening: pull your last three months of marketplace statements, count the jobs you actually sold from them, and divide. That’s your real cost per booked job. Do the same for LSA and Google Ads if you run them. If the Google side looks expensive too, our free <a href="/contact/">Ad Spend Leak Check</a> can tell you whether that’s the channel or the setup. We record a 10-minute video of your Google or Meta account showing where the money is going, and you’ll have it within 48 hours. You can also see how we work with <a href="/industries/service/">home service companies</a> across Greater Houston.</p>"""),
        ],
        "faq": [
            ("What do contractors say about Angi leads?",
             "In the contractor forums we read, including Jobber's community and Thumbtack's pro community, the repeated complaints were shared leads that turn into price wars, homeowners who never answer, annual contracts that are hard to exit, and early termination fees. Forum posts skew negative and any single story deserves a grain of salt, so track your own cost per booked job for 60 days instead."),
            ("Does Angi refund bad leads?",
             "Angi offers credits, not cash refunds, for specific reasons: invalid contact info, a ZIP code outside your service area, a service you do not offer, duplicates within 45 days, or leads charged while paused. The lead must be under 45 days old and you should try to call within 24 hours. Requests are reviewed within five business days, credits expire after six months, and annual subscribers can report leads but do not get credits."),
            ("Are Angi leads exclusive?",
             "Usually not. Angi says homeowners are connected with multiple service professionals, and Angi's CEO said in 2026 that pros win about one in six leads. A homeowner who contacts you directly from your profile is closer to exclusive, so ask your rep how your leads are delivered. Treat most Angi leads as shared and call back within minutes."),
            ("Are Google Local Services Ads cheaper than Angi?",
             "Not always per lead, but often per booked job. LSA leads come from customers who chose your listing, Google automatically credits invalid leads after review, and there is no annual membership. Since October 1, 2026, Google also charges for missed business-hours calls longer than 20 seconds, so LSA only works out cheaper if someone answers the phone."),
        ],
        "figures": {
            "scale": {
                "type": "stats",
                "title": "Angi’s marketplace by the numbers",
                "stats": [["16M", "projects requested on Angi in 2025"],
                          ["111K", "average monthly active pros, Q4 2025"],
                          ["1 in 6", "leads won by pros, per Angi’s CEO (2026)"]],
                "note": "Source: Angi 2025 Form 10-K; Q2 2026 earnings call",
                "alt": "Stat tiles showing Angi project volume, active pro count and lead win rate for contractors weighing Angi leads",
                "caption": "Pros winning one in six leads means paying for five that go to someone else. Source: Angi’s 2025 10-K and Q2 2026 call.",
            },
            "speed": {
                "type": "steps",
                "title": "A speed-to-lead routine for shared leads",
                "sub": "Set this up before you buy a single marketplace lead",
                "steps": [
                    ["Route alerts to a person", "Notifications go to a phone someone carries during business hours."],
                    ["Call within five minutes", "No answer? Text your name, company and a link to your reviews."],
                    ["Follow up twice", "Call again that evening and the next morning. Log every attempt."],
                    ["Record the outcome", "Reached, booked, sold or lost, and why, for every lead."],
                    ["Claim credits", "Flag wrong numbers, wrong ZIPs and duplicates while they qualify."],
                ],
                "alt": "Five-step speed-to-lead routine for Houston contractors buying shared Angi and Thumbtack leads",
                "caption": "Angi’s credit rules expect a call within 24 hours; winning usually takes minutes.",
            },
            "funnel": {
                "type": "funnel",
                "title": "Where 20 shared leads go",
                "stages": [["Leads bought", "20"], ["Reached a person", "12"], ["Appointments", "6"], ["Jobs sold", "3"]],
                "note": "Illustrative example",
                "alt": "Funnel chart showing 20 shared contractor leads narrowing to three sold jobs in an illustrative Angi example",
                "caption": "Shared leads lose people at every step because the homeowner already heard from other pros.",
            },
            "cpbj": {
                "type": "bars",
                "title": "Cost per booked job by source",
                "sub": "Hypothetical HVAC repair shop, 20 leads a month per source",
                "items": [["Angi (shared)", 433, "$433"], ["Thumbtack", 300, "$300"], ["Google Search ads", 273, "$273"], ["Google LSA", 233, "$233"]],
                "highlight": [3],
                "note": "Illustrative example",
                "alt": "Bar chart comparing illustrative cost per booked job for Angi, Thumbtack, Google Search ads and Local Services Ads",
                "caption": "Made-up numbers, real mechanics: the source with more answered calls wins, not the cheapest lead.",
            },
            "shift": {
                "type": "compare",
                "title": "Marketplace leads vs channels you own",
                "left": {"title": "Marketplace leads", "items": ["Same request sent to several pros", "Price set by the platform", "Annual terms on many plans", "Reviews live on their site"]},
                "right": {"title": "Owned channels", "items": ["Customer picked you on Google", "You control bids and budget", "Pause any time", "Reviews and rankings stay yours"]},
                "alt": "Comparison of shared marketplace leads with owned channels like Google Business Profile and Local Services Ads for contractors",
                "caption": "Use marketplaces to fill gaps; build the right column so your cost per job falls over time.",
            },
        },
    },
]
