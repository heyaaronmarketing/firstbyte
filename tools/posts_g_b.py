"""Batch 7 (agency intent): fractional CMO vs agency vs in-house hire, and how long SEO takes (month-by-month, local).

Research: BLS OEWS May 2023 area page for Houston-The Woodlands-Sugar Land MSA (marketing managers 11-2021, marketing
specialists 13-1161; the May 2024/2025 metro tables now load only in BLS's JS data tool, so the 2023 page is the latest
metro row we could open), BLS OOH (national median, May 2025), BLS ECEC news release (June 2026 benefits share),
Gallup on replacement cost, MarketerHire and Go Fractional fractional CMO pricing, Webtonic's compiled hourly-rate
stats. Google Search Central SEO starter guide, "Do you need an SEO?", Ask Google to recrawl, Page Indexing report help,
Performance report help, Business Profile local ranking and verification help pages.
Competitors read: MarketerHire fractional CMO vs agency, Webtonic Houston fractional CMO, generic "how long does local SEO
take" pages (Top4, Seologist, W3era).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "oews": A("https://www.bls.gov/oes/2023/may/oes_26420.htm", "BLS wage data for the Houston-The Woodlands-Sugar Land metro"),
    "ooh": A("https://www.bls.gov/ooh/management/advertising-promotions-and-marketing-managers.htm", "BLS Occupational Outlook Handbook"),
    "ecec": A("https://www.bls.gov/news.release/ecec.nr0.htm", "BLS Employer Costs for Employee Compensation release"),
    "gallup": A("https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx", "Gallup"),
    "mh": A("https://marketerhire.com/blog/fractional-cmo-cost", "MarketerHire’s pricing guide"),
    "gf": A("https://gofractional.com/blog/fractional-cmo-salary", "Go Fractional"),
    "wt": A("https://www.webtonic.io/blog/fractional-cmo-cost-pricing-statistics", "Webtonic’s roundup of fractional rate data"),
    "starter": A("https://developers.google.com/search/docs/fundamentals/seo-starter-guide", "SEO Starter Guide"),
    "needseo": A("https://developers.google.com/search/docs/fundamentals/do-i-need-seo", "“Do you need an SEO?” page"),
    "recrawl": A("https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl", "recrawl documentation"),
    "pir": A("https://support.google.com/webmasters/answer/7440203?hl=en", "Page Indexing report help"),
    "perf": A("https://support.google.com/webmasters/answer/7576553?hl=en", "Performance report"),
    "local": A("https://support.google.com/business/answer/7091?hl=en", "local ranking help page"),
    "verify": A("https://support.google.com/business/answer/7107242?hl=en", "verification help page"),
}

CMO = "/blog/fractional-cmo-vs-agency-vs-in-house-houston/"
SEO = "/blog/how-long-does-seo-take-houston-the-woodlands/"

POSTS = [
    # ------------------------------------------------------------------ post 1: fractional CMO vs agency vs hire
    {
        "slug": "fractional-cmo-vs-agency-vs-in-house-houston",
        "title": "Fractional CMO vs Agency vs In-House Hire: A Houston Owner’s Guide",
        "seo_title": "Fractional CMO vs Agency vs In-House Hire (Houston)",
        "desc": "Fractional CMO vs agency vs a marketing hire in Houston and The Woodlands: real salary data, fractional pricing, hidden costs and a decision table by revenue.",
        "category": "Strategy",
        "icons": ["Google Ads", "HubSpot", "Google Analytics"],
        "art": "b2",
        "hero": "growth",
        "hero_alt": "Illustration of a rising growth chart for a guide comparing a fractional CMO, an agency and an in-house marketing hire in Houston",
        "related": ["diy-vs-hiring-an-agency", "questions-before-hiring-marketing-agency", "digital-marketing-cost-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>It’s Sunday night, you’re approving payroll, and the Google Ads invoice is bigger than last month. Nobody can say if it worked. So you start pricing help: a marketing manager, an agency, or the “fractional CMO” a friend mentioned over lunch at Hughes Landing.</p>
<p>The short answer to fractional CMO vs agency vs an in-house hire: a fractional CMO sells senior judgment by the hour, an agency sells execution by the month, and a full-time hire sells one person’s full attention by the year. In the Houston metro, marketing managers averaged <b>$154,220 a year</b> in the most recent metro-level {SRC['oews']} we could open, before benefits. Fractional CMOs commonly quote $3,000 to $15,000 a month. Agencies vary with the work.</p>
<p>Our opinion, for most owners in The Woodlands, Spring, Conroe and greater Houston doing under about $5 million a year: an agency for execution plus one person inside the company who owns the numbers beats both a pricey full-time hire and a part-time strategist with nobody to do the work. Above that, the math changes. Below is how to tell which side of the line you’re on.</p>"""),

            ("Fractional CMO vs agency vs in-house hire: what you’re actually buying", f"""<p>The three options get compared as if they were one product at three prices. They aren’t, and most bad marketing hires come from buying the wrong thing well.</p>
<h3>A fractional CMO buys direction</h3>
<p>A fractional chief marketing officer is a senior marketer who works for you part time, usually a set number of hours a week, on a monthly retainer. Expect a plan, a budget split across channels, a sane reporting setup, and someone who can interview candidates and fire a vendor. Don’t expect them to build your Meta campaigns at 10 p.m. Most won’t touch the ad accounts at all; they manage the people who do.</p>
<h3>An agency buys hands and specialists</h3>
<p>An agency gives you a team: someone who lives inside Google Ads, someone who designs, someone who writes, someone who knows why your conversion tracking double-counts calls. You get breadth that no single hire has. The trade-off is attention. Your account is one of many, and the person you met in the pitch is rarely the person pulling the levers. (That’s true of us too, to a degree. Ask who will actually run your account.)</p>
<h3>An in-house hire buys context</h3>
<p>A full-time marketing person knows your techs by name, hears the customer complaints, and can shoot a reel at the job site on a Tuesday afternoon. Nobody outside the building can match that. The weakness is range. One person is rarely strong at paid search, Meta, SEO, design, analytics and email at once, and the ones who are cost a lot more than the job posting says.</p>
<p>So the real question isn’t which is “best.” It’s which gap is hurting you right now: lack of a plan, lack of hands, or lack of someone who cares about this every single day.</p>"""),

            ("What a marketing manager costs in Houston (salary is only the start)", f"""<p>Owners almost always underestimate this one.</p>
<p>The {SRC['oews']} (May 2023 estimates, the latest metro-level page we could verify) shows 7,890 marketing managers working in the Houston-The Woodlands-Sugar Land area, with a mean wage of $74.15 an hour and a mean salary of $154,220. The median hourly wage was $65.85, which works out to roughly $137,000 a year. Nationally, the {SRC['ooh']} puts the median for marketing managers at $166,790 as of May 2025, so the Houston figure has very likely moved up since 2023.</p>
<!--fig:houston-->
<p>“But I don’t need a manager, I need a marketing person.” Fair. The same Houston data shows market research analysts and marketing specialists (the category most “marketing coordinator” roles fall into) at a mean of $71,550 and a median of about $62,650. That person can post, schedule, update the website and coordinate vendors. They usually can’t set strategy or rescue a Performance Max campaign that’s spending on junk placements.</p>
<p>Then add what isn’t on the offer letter. The {SRC['ecec']} for June 2026 found benefits made up 30.0 percent of what private employers spend on compensation: $14.07 an hour in benefits against $32.82 in wages. Senior salaried roles often run a little lower as a percentage, so we use 30 percent on top of salary as a planning number. On a $137,000 manager that’s about $178,000 a year in real cost, before a laptop, software, recruiting fees or the bonus they’ll ask for in year two.</p>
<p>And the Houston market makes this harder than it looks. Plenty of strong marketers here work for energy, healthcare and engineering firms that pay corporate salaries. A local HVAC company or a dental group in Kingwood is competing with those offers, and with the commute: a great candidate in Katy is not going to drive the Grand Parkway to The Woodlands every morning for long.</p>"""),

            ("How much does a fractional CMO cost?", f"""<p>Fractional pricing is less standardized than salaries, and almost all of the published numbers come from firms that sell fractional executives. Keep that in mind. Here’s what we could verify.</p>
<ul>
<li>{SRC['mh']} lists $3,000 to $15,000 a month, with most fractional CMOs working 10 to 20 hours a week per client. Their tiers: strategy only at 5 to 10 hours a week runs about $3,000 to $6,000 a month; strategy plus oversight of execution at 15 to 20 hours runs about $7,000 to $12,000.</li>
<li>{SRC['gf']} puts the typical retainer at $4,000 to $20,000 a month, with an average of $12,000 a month ($144,000 a year), and says its people average around 20 hours a week.</li>
<li>{SRC['wt']} cites a median hourly rate for fractional marketing leadership of $175, with the middle half of rates between $130 and $220, and a typical commitment of about nine hours a week.</li>
</ul>
<p>Those numbers don’t perfectly agree (Go Fractional’s own page lists an average hourly rate of $325), which tells you how wide the market is. A former Fortune 500 CMO and a marketer who ran one regional brand will both call themselves fractional CMOs.</p>
<p>What the hours buy matters more than the rate. Five hours a week is an advisor: a monthly planning session, a look at the dashboard, a call when something breaks. Fifteen to twenty hours a week is a real leader who runs your weekly marketing meeting and holds vendors accountable. If you have no one to execute and no budget for an agency, paying for the advisor tier mostly buys you a very well-informed to-do list.</p>
<p>Houston note: local fractional CMOs exist, and so do national firms that will match you with someone remote. For a home services company in Montgomery County, we’d weight local knowledge (storm seasons, which suburbs actually buy, what a Conroe homeowner expects from a contractor) above a résumé full of SaaS launches.</p>"""),

            ("What agencies cost, and where the money goes", f"""<p>Agency pricing has two parts that get blurred together in proposals: the management fee you pay the agency, and the media budget that goes to Google, Meta or a TV network. We broke down typical channel costs in our <a href="/blog/digital-marketing-cost-the-woodlands-houston/">digital marketing cost guide</a>, so we won’t repeat it here. The short version for a local business is that management for one or two channels often lands in the low thousands a month, and a full-service retainer covering ads, SEO, content and design climbs from there.</p>
<p>What owners don’t see in the proposal:</p>
<ul>
<li><b>Who does the work.</b> A senior strategist sells the deal; a coordinator two years out of school may run it. Ask for names.</li>
<li><b>Setup fees and minimum terms.</b> A 12-month contract on a channel you’ve never tested is a bet on the agency, not on the channel.</li>
<li><b>Account ownership.</b> Your Google Ads account, Meta Business Manager, Google Business Profile and analytics should be in your name, with the agency added as a user. If they own it, leaving costs you your history.</li>
<li><b>Media markups.</b> Some agencies take a percentage of ad spend on top of the fee. That’s fine if it’s disclosed. It’s a problem if the invoice from Google never reaches you.</li>
<li><b>Account manager turnover.</b> Agencies lose people too. Every handoff costs you a month of someone relearning your business.</li>
</ul>
<p>Our list of <a href="/blog/questions-before-hiring-marketing-agency/">questions to ask before hiring a marketing agency</a> covers how to pressure-test a proposal. We’d add one more for this decision: ask the agency what they would <i>not</i> do for you. A good one will say, plainly, that they don’t replace someone inside the business who answers the phone well and follows up on leads.</p>"""),

            ("Side-by-side: what each option costs in a year", f"""<p>Here’s the comparison we’d sketch on a whiteboard for an owner. Salaries come from the BLS Houston data above with our 30 percent benefits planning figure; fractional numbers come from the published ranges; agency numbers are typical local ranges, not quotes.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Option</th><th>Typical annual cost</th><th>Hours of attention</th><th>Best at</th><th>Weak at</th></tr></thead>
<tbody>
<tr><td>Full-time marketing manager</td><td>About $178,000 loaded (on a ~$137K median salary)</td><td>40+ a week, all yours</td><td>Context, culture, speed on small things</td><td>Breadth across channels; one person to replace if they leave</td></tr>
<tr><td>Marketing coordinator / specialist</td><td>About $81,000 loaded (on a ~$62.6K median)</td><td>40 a week</td><td>Content, social, vendor coordination</td><td>Strategy, paid media, analytics</td></tr>
<tr><td>Fractional CMO, advisory</td><td>$36,000 to $72,000 ($3K to $6K a month)</td><td>5 to 10 a week</td><td>Plan, budget, vendor accountability</td><td>Doing the work</td></tr>
<tr><td>Fractional CMO, hands-on lead</td><td>$84,000 to $144,000 ($7K to $12K a month)</td><td>15 to 20 a week</td><td>Running marketing as a function</td><td>Still needs people or an agency to execute</td></tr>
<tr><td>Agency, one or two channels</td><td>Roughly $24,000 to $60,000 in fees, plus media</td><td>Shared team</td><td>Specialist execution, tools included</td><td>Knowing your business as deeply as staff</td></tr>
<tr><td>Agency, full service</td><td>Roughly $60,000 to $150,000+ in fees, plus media</td><td>Shared team</td><td>Breadth: ads, SEO, web, creative</td><td>Strategy if nobody inside sets goals</td></tr>
</tbody></table></div>
<!--fig:cost-->
<p>Two things jump out. A good fractional CMO at full engagement costs about what a coordinator does, and gives you senior thinking instead of junior hands. And a full-time manager costs more than most local businesses spend on media in a year, which is backwards. If your ad budget is $3,000 a month, a $178,000 person managing it is hard to justify.</p>"""),

            ("Should I hire a marketing manager or an agency? A decision table by revenue and team size", f"""<p>This is the table we wish more owners saw before posting a job ad. The revenue bands are our rule of thumb from working with local businesses around Houston, not an industry standard, and margins matter as much as revenue. A $3 million med spa has more room than a $3 million general contractor.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Stage</th><th>Typical team</th><th>What usually works</th><th>What we’d skip</th></tr></thead>
<tbody>
<tr><td>Under $1M revenue</td><td>Owner plus 1 to 5 staff</td><td>Owner runs it with a short checklist, or a specialist for the one channel that drives leads (often Google Ads or the Business Profile)</td><td>Any CMO, full-time or fractional</td></tr>
<tr><td>$1M to $5M</td><td>5 to 25 staff, an office manager</td><td>Agency for execution; an office manager or GM owns lead follow-up and reporting</td><td>A $150K manager with a $2K media budget</td></tr>
<tr><td>$5M to $20M</td><td>25 to 100 staff, several locations or service lines</td><td>Fractional CMO plus agency, or an in-house coordinator plus agency</td><td>Five separate freelancers with nobody steering</td></tr>
<tr><td>$20M+</td><td>100+ staff</td><td>Full-time marketing leader with a small team, plus specialist agencies</td><td>Handing all strategy to an agency with no internal owner</td></tr>
</tbody></table></div>
<p>If the table and your gut disagree, run the questions below. They take ten minutes and they’re the same ones we’d ask on a first call.</p>
<!--fig:decide-->
<p>One honest caveat. If you’re early and the problem is “we don’t get enough leads,” you may not need any of these yet. Our post on <a href="/blog/diy-vs-hiring-an-agency/">DIY vs hiring an agency</a> covers when doing it yourself stops paying off.</p>"""),

            ("Hidden costs nobody puts in the proposal", f"""<p>Every option has costs that don’t show up on the first invoice. These are the ones we see owners miss most often.</p>
<p><b>Your own management time.</b> A new hire needs onboarding, weekly one-on-ones and a boss who understands marketing well enough to judge their work. If that boss is you, budget three to five hours a week for the first few months. A fractional CMO needs less of your time; an agency needs a monthly review and fast answers when they ask for photos or approvals.</p>
<p><b>Software.</b> An agency usually brings its own SEO tools, call tracking and reporting dashboards. An in-house person needs those subscriptions in your name (SEO tool, scheduler, design software, maybe a CRM upgrade), often a few hundred to a couple thousand dollars a month.</p>
<p><b>Turnover.</b> {SRC['gallup']} estimates that replacing an employee can cost one-half to two times their annual salary. For a $137,000 marketing manager that’s a range of roughly $68,000 to $274,000, counting recruiting, ramp time and work that stalls while the seat is empty. Agencies and fractional CMOs can leave too, but the replacement cost is a few weeks of transition, not a six-month search.</p>
<p><b>Ramp time.</b> Anyone new needs 60 to 90 days to learn your customers, your seasons (hello, hurricane season and August heat) and your numbers. Plan for that quarter to be slow no matter which option you pick.</p>
<!--fig:hidden-->
<p><b>Conflicts of interest.</b> Some fractional CMOs are owned by, or refer work to, an agency. That’s not automatically bad, but ask directly. A fractional lead who recommends their own shop for every channel isn’t really independent oversight.</p>"""),

            ("Combinations that work (and one that usually doesn’t)", f"""<p>The best setups we see around The Woodlands and Houston are hybrids. A few that hold up:</p>
<h3>Fractional lead plus agency execution</h3>
<p>The fractional CMO sets the plan and budget, sits in the monthly agency review, and asks the uncomfortable questions (“why did cost per lead go up 40 percent in September?”). The agency runs the campaigns. This works well for companies in the $5 million to $20 million range with several service lines, say a home services company doing HVAC, plumbing and electrical across Montgomery and north Harris counties.</p>
<h3>In-house coordinator plus agency</h3>
<p>The coordinator handles everything that needs to be local and fast: job-site photos, review requests, social posts, Business Profile updates, the Waterway Square event booth. The agency handles paid media, SEO and web work. This is the most common setup we’d recommend for growing local businesses, and it costs far less than a manager.</p>
<h3>In-house manager plus specialist agencies</h3>
<p>At larger companies, a full-time marketing leader manages two or three specialist firms (paid media, SEO, creative) instead of one full-service agency. More coordination, sharper specialists.</p>
<h3>The one that usually doesn’t work</h3>
<p>Hiring one junior “marketing person” and expecting them to own strategy, ads, SEO, the website, social and analytics, with no senior help. They’re set up to fail, they usually leave within a year or two, and the owner concludes “marketing doesn’t work for us.” If you can only afford one junior hire, pair them with an agency or a few hours of a fractional lead.</p>
<p>Whatever the mix, someone needs patience with the slow channels. If SEO is part of the plan, our <a href="{SEO}">month-by-month SEO timeline</a> shows what progress should look like before you judge anyone on it.</p>"""),

            ("How to make the call this month", f"""<p>You don’t need a consultant to make this decision. You need about two hours and your last 12 months of numbers.</p>
<ol>
<li><b>Write down what marketing cost last year</b>, all in: media, agency fees, software, the hours your office manager spent posting on Facebook.</li>
<li><b>Count your leads and booked jobs by source</b>, even roughly. If you can’t, tracking is the first problem to solve, before hiring anyone.</li>
<li><b>Name the gap.</b> No plan? Look at fractional. No hands? Look at an agency. No one who cares daily? Look at a coordinator.</li>
<li><b>Price the loaded cost</b> using the table above, not the salary or the retainer alone.</li>
<li><b>Test before you commit.</b> A 90-day agency engagement or a three-month fractional trial beats a 12-month contract or a hire you can’t easily unwind.</li>
</ol>
<p>If paid ads are already part of your spend, start by finding out what they’re actually returning. Our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours. Whatever you decide about people, it’s worth knowing which dollars are working first. You can also see how we run <a href="/services/search-marketing/">Google Ads management</a> for local businesses.</p>"""),
        ],
        "faq": [
            ("How much does a fractional CMO cost in Houston?", "Published ranges run about $3,000 to $15,000 a month, with averages near $12,000 for roughly 20 hours a week. Advisory roles at five to ten hours a week sit around $3,000 to $6,000. Houston rates follow national ranges because many fractional CMOs work remotely, so the bigger driver is hours per week and the person’s experience, not the zip code."),
            ("Is a fractional CMO worth it for a small business?", "Usually only once you have several channels, a real budget and someone to do the work. Below about $5 million in revenue, most local businesses get more from an agency plus an internal owner of the numbers. A fractional CMO pays off when you have vendors or staff who need direction and nobody senior setting goals or judging results."),
            ("Should I hire a marketing manager or an agency?", "Compare loaded cost to what you spend on media. A Houston marketing manager costs around $178,000 a year with benefits, more than many local businesses spend on ads. If your media budget is modest, an agency for execution plus a coordinator or office manager who follows up on leads is typically the better use of money."),
            ("What does a fractional CMO actually do?", "They build the marketing plan, split the budget across channels, set up reporting, manage agencies and freelancers, and help hire. Most do not run ad campaigns or design content themselves. Think of them as a part-time head of marketing who makes decisions and holds people accountable, working a set number of hours each week."),
            ("Can a fractional CMO work with my existing agency?", "Yes, and that pairing is one of the most effective setups. The fractional CMO sets goals and reviews the agency’s work each month, while the agency handles execution. Ask whether the fractional CMO has any financial ties to agencies they recommend, so their oversight stays independent."),
        ],
        "figures": {
            "houston": {
                "type": "stats",
                "title": "Marketing pay in the Houston metro",
                "stats": [["$154K", "Mean salary, marketing managers"], ["7,890", "Marketing managers employed"], ["$72K", "Mean salary, marketing specialists"], ["30%", "Of employer pay costs go to benefits"]],
                "note": "Source: BLS OEWS May 2023 (Houston MSA); BLS ECEC June 2026",
                "alt": "Stat tiles showing marketing manager and specialist pay in the Houston metro and the benefits share of employer costs",
                "caption": f"Salary figures from the {A('https://www.bls.gov/oes/2023/may/oes_26420.htm', 'BLS Houston-The Woodlands-Sugar Land area page')}; benefits share is the national private-industry average.",
            },
            "cost": {
                "type": "bars",
                "title": "Rough annual cost of each option",
                "sub": "Thousands of dollars per year, before ad spend",
                "items": [["Marketing manager", 178, "~$178K"], ["Fractional CMO, avg", 144, "~$144K"], ["Marketing specialist", 81, "~$81K"], ["Fractional advisor", 54, "$36K-$72K"], ["Agency, 1-2 channels", 42, "$24K-$60K"]],
                "highlight": [1],
                "note": "Illustrative ranges; salaries from BLS plus 30% benefits",
                "alt": "Bar chart comparing the annual cost of a fractional CMO, an agency and an in-house marketing hire for a Houston business",
                "caption": "Salaries include our 30 percent benefits planning figure; fractional figures come from MarketerHire and Go Fractional ranges.",
            },
            "decide": {
                "type": "steps",
                "title": "Pick your marketing setup in 5 questions",
                "sub": "Answer in order and stop at the first yes",
                "steps": [
                    ["Is media spend under $2K a month?", "Fix tracking and your Business Profile yourself, or hire one specialist for one channel."],
                    ["Do you lack hands more than ideas?", "Start with an agency for the channel that drives most leads."],
                    ["Are 3+ vendors or channels unmanaged?", "Add a fractional CMO at 10 to 20 hours a week to steer them."],
                    ["Is local content constantly late?", "Hire a coordinator to work alongside the agency."],
                    ["Revenue over $20M with a team to lead?", "Hire a full-time marketing leader and keep specialist agencies."],
                ],
                "alt": "Five-step decision guide for choosing a fractional CMO, an agency or an in-house marketing hire in The Woodlands",
                "caption": "Our rule of thumb from local client work; your margins and growth goals can move the lines.",
            },
            "hidden": {
                "type": "checklist",
                "title": "Hidden costs to price before you decide",
                "sub": "Add these to the salary or retainer",
                "items": [
                    "Benefits and payroll taxes, about 30% on top",
                    "Recruiting fees or weeks of your time",
                    "60 to 90 days of ramp before results",
                    "Software subscriptions in your name",
                    "Your weekly management hours",
                    "Turnover: half to 2x salary to replace",
                    "Agency setup fees and contract minimums",
                    "Media markups and who owns the ad accounts",
                ],
                "alt": "Checklist of hidden costs when comparing a fractional CMO vs agency vs in-house marketing hire in Houston",
                "caption": f"Turnover range from {A('https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx', 'Gallup')}; benefits share from BLS.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: how long does SEO take
    {
        "slug": "how-long-does-seo-take-houston-the-woodlands",
        "title": "How Long Does SEO Take? A Month-by-Month Timeline for Houston Businesses",
        "seo_title": "How Long Does SEO Take? A Houston Month-by-Month Timeline",
        "desc": "How long does SEO take for a local business in Houston or The Woodlands? A month-by-month timeline, what Google says, and the Search Console signs to watch.",
        "category": "SEO & AI search",
        "icons": ["Search Console", "Google Business Profile", "Google"],
        "art": "b5",
        "hero": "clock",
        "hero_alt": "Illustration of a clock for a guide to how long SEO takes for local businesses in Houston and The Woodlands",
        "related": ["seo-cost-houston-the-woodlands", "rank-in-google-map-pack-houston", "local-seo-checklist-the-woodlands"],
        "sections": [
            (None, f"""<p>You launched the new website in March. It’s June. You search “roof repair Conroe” from your phone in the truck and you’re on page four, behind a directory, two franchises and a guy who hasn’t updated his site since 2019.</p>
<p>So how long does SEO take? For most local businesses in Houston and The Woodlands, the first measurable movement shows up in one to three months (impressions in Search Console, views on your Business Profile), steady calls start somewhere around months four to six, and the gains keep compounding through month twelve. Business Profile fixes can move map pack rankings within weeks. A brand-new domain in a crowded category like roofing or personal injury can take a year or more to reach page one for the big terms.</p>
<p>That’s a wide range, and anyone who gives you a single number without asking about your site, your category and your competitors is guessing. Below is what Google actually says, what happens month by month, and how to read Search Console for progress long before the phone rings.</p>"""),

            ("What Google says about how long SEO takes", f"""<p>Google doesn’t publish a timeline, but its documentation is more useful than most agency blog posts on the subject.</p>
<p>The {SRC['starter']} says: “Some changes might take effect in a few hours, others could take several months.” It also says you “likely want to wait a few weeks to assess whether your work had beneficial effects.” That second line matters. If you rewrite a page on Monday and check rankings on Friday, you’re reading noise.</p>
<p>On new or updated pages, Google’s {SRC['recrawl']} says “crawling can take anywhere from a few days to a few weeks,” and that “requesting a recrawl multiple times for the same URL won’t get it crawled any faster.” Clicking “Request indexing” ten times is a very common way to spend an afternoon. It doesn’t help.</p>
<p>And on the local side, Google’s {SRC['local']} says rankings come from relevance, distance and prominence, and that “there’s no way to request or pay for a better local ranking on Google.” Prominence (reviews, links, how well known you are) is the slow one. It builds over months, not days.</p>
<p>We’d add one thing Google doesn’t say outright: SEO is a race against competitors who are also working. Six months is fast if the plumber ahead of you has 900 reviews and a 15-year-old domain. It’s slow if nobody in your niche has touched their site since COVID.</p>"""),

            ("How long for a new website to rank on Google?", f"""<p>Before a page can rank it has to be found, crawled and indexed. With a new site, each step can stall, and owners rarely look at where.</p>
<p>Google’s {SRC['starter']} notes that Google “primarily finds pages through links from other pages it already crawled.” A new domain has almost no links pointing at it, so discovery is slow. A sitemap helps Google find your URLs, but Google itself says it isn’t required and it doesn’t guarantee anything gets indexed.</p>
<p>Then there’s the status that confuses everyone. In the {SRC['pir']}, two labels show up constantly on new sites:</p>
<ul>
<li><b>Discovered - currently not indexed:</b> “The page was found by Google, but not crawled yet.” Google says this typically happens when crawling the URL “was expected to overload the site,” so it rescheduled. On a small local site, it often means Google doesn’t yet see the page as worth the trip.</li>
<li><b>Crawled - currently not indexed:</b> “The page was crawled by Google but not indexed.” Google says it “may or may not be indexed in the future,” and there’s no need to resubmit.</li>
</ul>
<p>Google is blunt about the rest: “Don’t expect every URL on your site to be indexed.” If you published 40 near-identical city pages (“Plumber in Spring,” “Plumber in Tomball,” same text with the town swapped), don’t be surprised when most of them sit in those two buckets for months.</p>
<!--fig:pipeline-->
<p>What to do about it: link every important page from your main navigation or service pages, cut or merge thin pages, and give each city page something real (jobs you’ve done there, neighborhoods you serve, a photo from the job site). Then wait. A new site getting most of its core pages indexed within the first month or two is normal. Ranking them is the next, longer step.</p>"""),

            ("How long does local SEO take to work? Map pack vs organic", f"""<p>Local search has two sets of results, and they move at different speeds.</p>
<p><b>The map pack</b> (the three businesses under the map) runs off your Google Business Profile. Fixes there can show up fast. Changing a wrong primary category, adding services, correcting hours, filling in the description and uploading real photos can move map visibility within a few weeks. A brand-new profile has to be verified first, and Google’s {SRC['verify']} says verification reviews take up to 5 business days, sometimes longer.</p>
<p>The catch is distance, which you can’t optimize. If your shop is off Research Forest Drive, you can rank well in the map for searchers in The Woodlands and Spring and still never show up for someone in Pearland. That’s Google working as designed. Our guide to <a href="/blog/rank-in-google-map-pack-houston/">ranking in the Google map pack in Houston</a> goes deeper on what you can control.</p>
<p><b>The organic results</b> (the blue links below the map) run off your website. Service pages, city pages, links and content all feed them, and they usually take longer: two to four months for a new service page to settle on a site that already has some history, longer on a new domain or in a tough category.</p>
<p>Say you run a two-truck HVAC company in Spring. A cleaned-up Business Profile and a steady stream of new reviews might put you in the map pack for “ac repair spring tx” within a couple of months, at least for searchers close to you. Ranking your website on page one for “ac repair houston” is a different job, probably a year or more of work, and maybe not worth chasing at all compared with the suburbs you actually serve.</p>"""),

            ("A realistic month-by-month SEO timeline", f"""<p>This is the timeline we’d give a local service business starting from an existing site with a basic Business Profile. A brand-new domain should add a few months to every row. A low-competition niche in a smaller town (a pool service in Magnolia, a dog groomer in Montgomery) may run ahead of it.</p>
<div class="bp-tbl"><table>
<thead><tr><th>When</th><th>The work</th><th>What you’ll likely see</th><th>Leading indicator to check</th></tr></thead>
<tbody>
<tr><td>Month 1</td><td>Business Profile cleanup, Search Console and sitemap set up, fix broken pages, titles, speed and tracking</td><td>Little in rankings. Maybe more profile views.</td><td>Page indexing: are core pages indexed? Business Profile verified?</td></tr>
<tr><td>Month 3</td><td>Service pages built or rewritten, first city pages, review requests running, citations fixed</td><td>Impressions rising, new long-tail queries appearing, a few map pack wins near your address</td><td>Search Console: total queries and impressions vs the prior 3 months; non-brand queries in positions 11-30</td></tr>
<tr><td>Month 6</td><td>Local links (sponsorships, suppliers, chamber), more city pages with real proof, content answering customer questions</td><td>Clicks and calls from organic and the map pack start to show up in your lead log</td><td>Non-brand clicks; queries moving into positions 4-10; calls and website clicks in Business Profile Performance</td></tr>
<tr><td>Month 12</td><td>Keep publishing, keep earning reviews and links, prune what doesn’t work</td><td>SEO is a steady lead source; bigger terms within reach in suburbs you serve</td><td>Leads and booked jobs from organic and the map pack, compared with month 1</td></tr>
</tbody></table></div>
<!--fig:curve-->
<p>The shape is the important part. Most of the visible payoff arrives in the back half of the year, after months where the only proof is a rising line in Search Console. That gap is where most owners quit, and also where most SEO budgets do their work. Our <a href="/blog/seo-cost-houston-the-woodlands/">SEO cost guide for Houston and The Woodlands</a> covers what a year of this should cost.</p>"""),

            ("Leading indicators to watch in Search Console", f"""<p>You don’t have to wait for leads to know whether SEO is working. Here’s the 15-minute monthly check we’d have any owner do, using the free {SRC['perf']} in Google Search Console.</p>
<ol>
<li><b>Open Performance, then Search results.</b> Set the date range to “Compare” and pick the last 3 months vs the previous 3 months. Short ranges bounce around; Google even flags the newest data as preliminary.</li>
<li><b>Filter out your brand.</b> Click “+ Add filter,” choose Query, pick “Queries not containing,” and type your business name. Brand searches come from people who already know you. Non-brand impressions show whether new people are finding you.</li>
<li><b>Look at impressions before clicks.</b> Impressions count how many times your site appeared in results. They rise first, often months before clicks do.</li>
<li><b>Sort the Queries tab by impressions</b> and check the average position column. Queries sitting at positions 11 to 20 are page-two terms that a better page or a few links could push onto page one.</li>
<li><b>Click the Pages tab.</b> Are your service and city pages each getting impressions, or is the home page doing all the work?</li>
<li><b>Check Indexing, then Pages.</b> Watch the indexed count and the “Discovered” and “Crawled” not-indexed lists from the section above.</li>
</ol>
<p>For the map pack, open your Business Profile, go to Performance, and compare calls, website clicks and direction requests month over month. Note any spike around storms or the first heat wave so you don’t confuse weather with SEO progress. (In Houston, a busy July for an AC company says more about the thermometer than your rankings.)</p>"""),

            ("What speeds SEO up (and what slows it down)", f"""<p>Some things reliably shorten the timeline. Others quietly add months.</p>
<!--fig:speed-->
<h3>What speeds it up</h3>
<ul>
<li><b>A complete Business Profile.</b> Right primary category, every relevant secondary category, services listed, accurate hours, real photos. Google says businesses with complete and accurate info are more likely to show up in local results.</li>
<li><b>Steady review velocity.</b> Ten reviews a month for six months beats sixty in one week followed by silence. Ask every happy customer, by text, the day the job is done. Google says more reviews and positive ratings can help local ranking.</li>
<li><b>One page per service, and real city pages.</b> A page for “water heater replacement” will rank for that phrase far faster than a single “Services” page listing twelve things.</li>
<li><b>Local links.</b> Sponsor a youth league in Tomball, join the chamber, get listed by your suppliers and the manufacturers you’re certified with. A handful of genuine local links moves a small site more than hundreds of directory links.</li>
<li><b>An older domain with clean history.</b> If you have one, keep it. Don’t rebrand onto a new domain without page-by-page redirects.</li>
</ul>
<h3>What slows it down</h3>
<ul>
<li><b>A brand-new domain.</b> No links, no history, no reviews tied to a site. Expect the slow end of every range.</li>
<li><b>Thin or duplicate pages.</b> Copy-paste city pages and 200-word service pages tend to sit unindexed.</li>
<li><b>Competitive niches.</b> Personal injury, roofing, HVAC, plumbing and med spas in Houston have competitors with years of reviews and links. Plan for twelve months or more for the head terms.</li>
<li><b>Migrations done wrong.</b> A redesign that changes every URL without redirects can erase years of progress in a week. We see it every few months.</li>
<li><b>Inconsistent name, address and phone.</b> Moving from a suite on Woodlands Parkway to a warehouse in Conroe and only updating half your listings confuses Google about where you are.</li>
</ul>
<p>Our <a href="/blog/local-seo-checklist-the-woodlands/">local SEO checklist for The Woodlands</a> lists the setup items in order, if you want to work through them yourself.</p>"""),

            ("Red flags when an SEO company promises a timeline", f"""<p>A fair agency will give you a range and explain what drives it. A bad one will give you a guarantee. Google’s own {SRC['needseo']} is direct: “No one can guarantee a #1 ranking on Google,” and if an SEO guarantees their changes will give you first place, “find someone else.”</p>
<!--fig:redflags-->
<p>Other things that should make you nervous:</p>
<ul>
<li>“Page one in 30 days” for a competitive Houston term. Possible for your own business name; not for “roofer houston.”</li>
<li>Talk of a “special relationship” with Google, or a “priority submit” service. Google calls both out by name.</li>
<li>Reports that show only rankings for phrases nobody searches, with no Search Console data, calls or leads.</li>
<li>Hundreds of links per month for a small local business, or a requirement that you link to the agency from your site. Google says you should never have to link to an SEO.</li>
<li>A refusal to tell you what they changed on your website. Google suggests asking whether they will share every change they make.</li>
<li>A long contract with no early exit, signed before they’ve seen your Search Console data.</li>
</ul>
<p>Google also suggests asking a prospective SEO, “What kind of results do you expect to see, and in what timeframe? How do you measure your success?” We like that question. Bring it to every sales call, ours included.</p>"""),

            ("What to do while you wait for SEO to work", f"""<p>Six months is a long time to wait on leads. Most local businesses we work with run paid search alongside SEO in the early months, then lean on organic more as it takes over. Ads also tell you which keywords actually turn into booked jobs, which is useful when you decide which service pages to build first.</p>
<p>This week, if you do nothing else:</p>
<ol>
<li>Confirm you have Search Console access and that your sitemap is submitted.</li>
<li>Open the Page indexing report and write down how many pages are indexed today. That’s your baseline.</li>
<li>Check your Business Profile primary category against the top three map results for your main service.</li>
<li>Text five recent customers and ask for a review.</li>
<li>Put a reminder on your calendar for 90 days from now to run the Search Console check above.</li>
</ol>
<p>If you’re running Google or Meta ads to cover the gap, make sure they aren’t wasting money while SEO ramps up. Our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your budget is leaking, delivered within 48 hours. And if you’re weighing who should own all of this long term, our comparison of a <a href="{CMO}">fractional CMO vs an agency vs an in-house hire</a> walks through the costs. When you’re ready for help with the site itself, see our <a href="/services/web-design-seo-pr/">web design and SEO services</a>.</p>"""),
        ],
        "faq": [
            ("How long does SEO take to show results?", "Most local businesses see early signs in one to three months, such as more impressions and new queries in Search Console. Calls and form leads from organic search usually build between months four and six, and results keep compounding through the first year. Competitive categories and brand-new domains sit at the slow end of that range."),
            ("How long does local SEO take to work?", "Google Business Profile fixes such as the right primary category, complete services, accurate hours and new reviews can move map pack rankings within a few weeks. Website rankings for service and city pages usually take two to four months on an established site. A new profile also needs verification, which Google says can take up to five business days."),
            ("How long does it take for a new website to rank on Google?", "Google says crawling new pages can take a few days to a few weeks, and not every page will be indexed. For a new local business site, expect core pages indexed in the first month or two, long-tail rankings in three to six months, and competitive terms in a year or more, depending on links, reviews and competitors."),
            ("Can SEO results be guaranteed?", "No. Google states that no one can guarantee a number one ranking and advises finding another provider if an SEO promises first place. A trustworthy agency gives a realistic range, explains what drives it, and reports on Search Console data, calls and leads rather than a handful of cherry-picked keyword rankings."),
            ("Why is my page discovered but not indexed?", "Google found the URL but hasn’t crawled it yet, often because it doesn’t see the page as a priority. On small local sites this usually points to thin or duplicate content or weak internal links. Link to the page from your main navigation or service pages, add unique content, merge near-duplicates, and give Google a few weeks."),
        ],
        "figures": {
            "pipeline": {
                "type": "funnel",
                "title": "From published page to phone call",
                "stages": [["Published", "40 pages"], ["Discovered", "38"], ["Indexed", "28"], ["Getting impressions", "20"], ["Getting clicks", "9"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how pages on a new Houston business website move from published to indexed to getting clicks over time",
                "caption": f"Every step takes time; Google’s {A('https://support.google.com/webmasters/answer/7440203?hl=en', 'Page Indexing help')} says not every URL will be indexed.",
            },
            "curve": {
                "type": "columns",
                "title": "Typical first-year SEO curve, local business",
                "sub": "Non-brand impressions, indexed to month 12 = 100",
                "labels": ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"],
                "values": [4, 7, 12, 20, 29, 38, 48, 58, 68, 78, 89, 100],
                "highlight": [2, 5, 11],
                "y_label": "Impressions",
                "note": "Illustrative example",
                "alt": "Column chart of a typical first-year SEO timeline for a local business in The Woodlands, rising slowly then faster",
                "caption": "An illustration of the shape, not a promise; competitive niches and new domains run slower.",
            },
            "speed": {
                "type": "compare",
                "title": "What sets your SEO timeline",
                "left": {"title": "Slows it down", "items": ["Brand-new domain, no links", "Copy-paste city pages", "Redesign without redirects", "Reviews in one burst, then none", "Half-updated address listings"]},
                "right": {"title": "Speeds it up", "items": ["Complete Business Profile", "Steady reviews every month", "One page per service", "Real local links", "Old domain kept and redirected"]},
                "alt": "Comparison of factors that slow down or speed up how long SEO takes for a Houston local business",
                "caption": "Most of the fast wins are in your Business Profile and your service pages.",
            },
            "redflags": {
                "type": "checklist",
                "title": "SEO sales pitch red flags",
                "sub": "Walk away if you hear these",
                "items": [
                    "Guaranteed #1 ranking",
                    "Page one in 30 days for a big Houston term",
                    "A “special relationship” with Google",
                    "“Priority submit” to Google",
                    "You must link to the agency’s site",
                    "Won’t share what they change",
                    "Rank reports with no Search Console data",
                    "12-month contract before an audit",
                ],
                "alt": "Checklist of red flags when an SEO company in Houston or The Woodlands promises how long SEO will take",
                "caption": f"Several come straight from Google’s {A('https://developers.google.com/search/docs/fundamentals/do-i-need-seo', 'advice on hiring an SEO')}.",
            },
        },
    },
]
