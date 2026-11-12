"""Batch 12 (b): financial advisor marketing in Houston for RIAs, independent advisors and broker-dealer reps.

Research: WordStream/LocaliQ 2026 Google Ads benchmarks (Finance & Insurance: $3.39 CPC, 9.83% CTR, 2.64% conversion
rate, $74.44 cost per lead; data April 2025 to March 2026); SEC press release 2020-334 on the amended marketing rule
(testimonial/endorsement disclosures, third-party ratings, net-with-gross performance); SEC Marketing Compliance FAQ
(compliance date Nov. 4, 2022; 1-, 5- and 10-year periods; Jan. 15, 2026 FAQs on model fees and SRO orders); SEC
Division of Examinations risk alert of Dec. 16, 2025 (testimonial disclosures not shown at dissemination, hyperlinked
disclosures, gift cards for reviews, third-party rating dates and payments); FINRA Rule 2210 text (25 retail investors
in 30 days, testimonial disclosures, $100 paid testimonial threshold) and FINRA's filing chart (principal approval,
new member pre-filing); Holland & Knight on FINRA Regulatory Notice 26-14 (July 9, 2026 proposal, comments through
Sept. 11, 2026); Texas State Securities Board on 7 TAC 116.15 adopting the SEC marketing rule by reference (adopted
Feb. 20, 2025, effective March 13, 2025) and its RIA registration page ($100 million threshold, IAR place of business);
Google Local Services Ads category list ("Financial planning services") and screening requirements (license checks
for each financial planner); Search Engine Land on the national professional-services LSA launch after a Houston and
San Diego test; Google's Oct. 2026 announcement of financial services verification for the US and Canada in early
2027; Meta Marketing API special ad category docs and Jon Loomer on the Financial Products and Services category
(investment services included; 15-mile radius, no ZIPs, no lookalikes); The Kitces Report 2024 marketing survey
(median client acquisition cost $3,800 in 2023; $6,263 for $1M+ clients; 11% of revenue; 0.6 efficiency; seminars
$7,679 first-year revenue per new client); ABC13 on Chevron's 575 Houston job cuts after the Hess merger (July 2025).
Left out as unverified: whether Google LSA financial planning ads are currently serving in every Houston ZIP, any
Google Ads US verification rule for investment advisers before 2027, local CPCs for advisor keywords.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "wordstream": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream’s 2026 Google Ads benchmarks"),
    "sec_pr": A("https://www.sec.gov/news/press-release/2020-334", "the SEC’s announcement of the amended rule"),
    "sec_faq": A("https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/marketing-compliance-frequently-asked-questions", "the SEC staff’s Marketing Rule FAQ"),
    "sec_alert": A("https://www.sec.gov/files/exams-riskalert-mrkt-rule-2512-508.pdf", "the SEC Division of Examinations’ December 2025 risk alert"),
    "finra_rule": A("https://www.finra.org/rules-guidance/rulebooks/finra-rules/2210", "FINRA Rule 2210"),
    "finra_chart": A("https://www.finra.org/rules-guidance/key-topics/advertising-regulation/chart", "FINRA’s filing chart"),
    "finra_2614": A("https://www.hklaw.com/en/insights/publications/2026/07/finra-seeks-to-modernize-rule-2210-communications-with-the-public", "Holland &amp; Knight’s summary of Regulatory Notice 26-14"),
    "tssb_rule": A("https://ssb.state.tx.us/news-publications/updates-texas-state-securities-board-rules-concerning-dealers-and-investment", "the Texas State Securities Board"),
    "tssb_reg": A("https://ssb.texas.gov/securities-professionals/dealer-adviser-registration/getting-started-registered-investment-adviser-3", "the TSSB’s registration guidance"),
    "lsa_cats": A("https://support.google.com/localservices/answer/6224841?hl=en", "Google’s Local Services Ads category list"),
    "lsa_screen": A("https://support.google.com/localservices/answer/12174778?hl=en", "Google’s screening requirements"),
    "sel_lsa": A("https://searchengineland.com/google-rolling-out-lsas-and-google-screened-to-select-professional-services-nationally-338354", "Search Engine Land"),
    "g_fsv": A("https://blog.google/products/ads-commerce/financial-services-verification-united-states-canada/", "Google announced in October 2026"),
    "meta_api": A("https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category", "Meta’s special ad category documentation"),
    "loomer": A("https://www.jonloomer.com/qvt/financial-products-and-services/", "Jon Loomer’s breakdown"),
    "kitces": A("https://kitces.com/wp-content/uploads/2024/07/The-Kitces-Report-Marketing-Survey-How-Financial-Planners-Actually-Market-Their-Services-Vol-1-2024.pdf", "The Kitces Report’s 2024 marketing survey"),
    "abc13": A("https://abc13.com/post/more-500-houston-based-employees-will-job-chevron-merger/17295661/", "ABC13"),
}

L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    {
        "slug": "financial-advisor-marketing-houston",
        "title": "Financial Advisor Marketing in Houston: SEO, Google Ads & Compliant Reviews for RIAs and Independent Advisors",
        "seo_title": "Financial Advisor Marketing in Houston: SEO, Ads & Reviews",
        "desc": "How Houston RIAs and independent advisors win new households: SEO, Google Ads costs, LSAs, SEC Marketing Rule reviews, FINRA 2210, Meta rules and seminars.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google Business Profile", "LinkedIn"],
        "art": "b2",
        "hero": "growth",
        "hero_alt": "Illustration of a rising growth chart for financial advisor marketing in Houston and The Woodlands",
        "related": ["cpa-accounting-firm-marketing-houston", "insurance-agency-marketing-houston", "law-firm-marketing-houston"],
        "sections": [
            (None, f"""<p>Finance and insurance advertisers pay a median of <b>$3.39 per click</b> and <b>$74.44 per lead</b> on Google Ads, with a 2.64% conversion rate, per {SRC['wordstream']}, and an advisor’s lead is worth far more than that number suggests because one new household can be a decade of fees. Houston is crowded with wirehouse branches, bank wealth desks, and independent RIAs from the Galleria to Market Street, so the advisors who grow here are the ones who are easy to find, easy to trust, and quick to call back.</p>
<p>Picture a Tuesday in a two-advisor RIA off Research Forest. A prospect who just took a package from an upstream operator emails at 9:40 p.m. asking whether to roll over a 401(k) before year-end. A second one found you on Google, read three reviews, and called while you were in a review meeting. Nobody calls either of them back until Thursday. That gap, more than any ad budget, is where most practices lose households.</p>
<p>This guide is for independent RIAs, hybrid advisors and broker-dealer reps in Greater Houston.</p>"""),

            ("Rank for the searches prospects actually type", f"""<p>Advisor SEO works when every page answers one specific question a Houston prospect types, and when your Google Business Profile looks like a real local office.</p>
<ul>
<li><b>One page per audience and service:</b> retirement income planning, 401(k) rollovers, equity compensation, business owner exit planning, widows and divorce transitions. A generic “Services” page won’t rank for any of them.</li>
<li><b>Town and neighborhood pages with substance:</b> “fee-only financial advisor The Woodlands,” “retirement planner Katy,” “fiduciary advisor Sugar Land.” Say where you meet clients, which ZIPs you serve, and what you actually do there.</li>
<li><b>Advisor bio pages</b> with CRD numbers, designations, and a link to the firm’s Form ADV. Prospects check BrokerCheck before they call.</li>
<li><b>Content tied to Houston paychecks:</b> pension lump sum versus annuity decisions, restricted stock vesting, severance and rollover timing, hurricane-season insurance reviews. Have compliance approve it before it goes live.</li>
<li><b>FinancialService schema</b> and a consistent name, address and phone everywhere. Our {L('/blog/rank-in-google-map-pack-houston/', 'Map Pack guide')} covers the profile side.</li>
</ul>
<p>Plainly written pages also get quoted by AI search; see {L('/blog/show-up-in-chatgpt-ai-search-aeo/', 'how to show up in AI search')}.</p>"""),

            ("Use Local Services Ads for financial planning", f"""<p>Google lists “Financial planning services” as a Local Services Ads category, per {SRC['lsa_cats']}, so a Houston planner can buy pay-per-lead placement above the regular ads.</p>
<ul>
<li><b>Expect license checks.</b> {SRC['lsa_screen']} include business owner identity verification and license checks for each financial planner in the firm, with professional liability insurance where local law requires it.</li>
<li><b>Houston was a test city.</b> {SRC['sel_lsa']} reported that Google tested professional-services LSAs in Houston and San Diego before a national launch for lawyers, financial planners, real estate agents and tax preparers.</li>
<li><b>Check your own ZIPs.</b> Availability and lead volume vary by area, so confirm eligibility for your office’s service area during signup rather than assuming it.</li>
<li><b>Answer the phone.</b> LSA leads are calls and messages. Slow responses tend to mean fewer leads. The badge is now called Google Verified; see {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified')}.</li>
</ul>
"""),

            ("Run Google Ads with tight controls", f"""<p>Google Ads works for advisors when campaigns target high-intent, local searches and every click lands on a page built for that exact question.</p>
<!--fig:benchmarks-->
<ul>
<li><b>Keywords with intent:</b> “fee only financial advisor near me,” “retirement planner the woodlands,” “401k rollover advisor houston,” “financial advisor for business owners katy.”</li>
<li><b>Negatives on day one:</b> jobs, careers, salary, “how to become,” intern, Series 65, CFP exam, “free,” app, robo, login, and the names of custodians whose clients are just trying to sign in.</li>
<li><b>Location targeting by office:</b> a radius around The Woodlands won’t reach Memorial clients who never drive north. Separate campaigns for each office keep the reporting honest.</li>
<li><b>Company names belong in keywords, not ad text.</b> A page about ExxonMobil or Chevron benefits can rank and be bid on, but keep employers’ trademarks out of headlines and never imply an endorsement.</li>
<li><b>Verification is coming.</b> {SRC['g_fsv']} that financial services verification will roll out in the US and Canada in early 2027. The scope hasn’t been fully published, so watch your account notices.</li>
</ul>
<p>Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give local context, and our {L('/services/search-marketing/', 'search marketing team')} runs these accounts.</p>"""),

            ("Build reviews the right way under the SEC Marketing Rule", f"""<p>SEC-registered advisers can use client reviews and testimonials, but only with clear and prominent disclosures, oversight, and no shortcuts on how reviews are gathered.</p>
<p>The amended rule (206(4)-1) requires testimonials and endorsements to disclose whether the person is a client and whether they were compensated, per {SRC['sec_pr']}. The compliance date was November 4, 2022, per {SRC['sec_faq']}. Exams since then keep turning up the same errors. {SRC['sec_alert']} flagged disclosures that weren’t shown when the testimonial was, disclosures tucked behind a hyperlink or set in lighter type, gift cards handed out for reviews, and third-party ratings shown without the date and period they cover.</p>
<!--fig:reviews-->
<ul>
<li><b>Ask after a real milestone,</b> like a completed plan or a retirement date, by email with a direct link. Offer nothing in return. Google’s own rules forbid it too; see {L('/blog/fake-reviews-rule-local-businesses/', 'the fake reviews rule')}.</li>
<li><b>Pulling Google reviews onto your website</b> is using a testimonial. Put the required disclosures right beside them.</li>
<li><b>Ratings and “top advisor” lists</b> need the rating date, period, who created it, and whether you paid anything.</li>
</ul>
<p>Our {L('/blog/complete-guide-google-reviews/', 'review guide')} covers the mechanics. This isn’t legal advice; your CCO has the final word.</p>"""),

            ("Follow Texas and FINRA rules for your registration", f"""<p>Which rulebook applies depends on how you’re registered: the SEC for larger RIAs, the Texas State Securities Board for most smaller ones, and FINRA for anything you do as a broker-dealer rep.</p>
<ul>
<li><b>State-registered RIAs:</b> advisers with less than $100 million under management generally register with the state, per {SRC['tssb_reg']}. Texas amended 7 TAC §116.15 to adopt the SEC Marketing Rule by reference, adopted February 20, 2025 and effective March 13, 2025, per {SRC['tssb_rule']}. That opened testimonials and reviews to Texas-registered firms on the SEC’s terms.</li>
<li><b>Investment adviser reps:</b> an IAR of an SEC-registered firm with a Texas place of business must register in Texas, and the TSSB notes that business cards and directory listings can establish a place of business.</li>
<li><b>Broker-dealer reps:</b> under {SRC['finra_rule']}, anything sent to more than 25 retail investors in 30 days is a retail communication. Testimonials must say they may not be representative and aren’t a guarantee, and must be labeled paid if more than $100 in value changed hands. A principal approves retail communications before use, and new member firms pre-file for their first year, per {SRC['finra_chart']}.</li>
<li><b>Changes in progress:</b> FINRA proposed a risk-based replacement for pre-use principal approval in Regulatory Notice 26-14 on July 9, 2026, per {SRC['finra_2614']}. It’s a proposal, not a rule yet.</li>
</ul>
<p>Hybrid advisors usually live under both regimes. Find out who approves what before you hire anyone, us included.</p>"""),

            ("Know the Meta rules before you boost a post", f"""<p>Facebook and Instagram ads for investment services must run in Meta’s Financial Products and Services special ad category, which strips out most demographic targeting.</p>
<p>The category replaced the old Credit category and became required for US audiences in January 2025, and it includes investment services and insurance, per {SRC['loomer']}. Under {SRC['meta_api']}, age is fixed at 18 to 65+, you can’t pick a gender, locations need at least a 15-mile radius with no ZIP codes, and lookalike audiences aren’t available.</p>
<p>So the creative does the targeting. “Retiring from the refinery or the energy company in the next three years? Join our pension lump sum workshop in Spring” finds the right people, while a stock photo of a couple on a beach reaches no one. A qualifying question on lead forms cuts junk. We’d spend most of a small budget on search and use Meta for event promotion and retargeting. See {L('/services/paid-social-advertising/', 'our paid social service')}.</p>"""),

            ("Pick a Houston niche and market to it", f"""<p>Specialized advisors market more cheaply than generalists because their message, keywords and events all point at one group.</p>
<ul>
<li><b>Energy-industry employees and executives.</b> Pension elections, restricted stock, deferred comp and layoffs. When Chevron filed a WARN notice for 575 Houston employees after the Hess merger, per {SRC['abc13']}, every one of them had a severance and rollover decision. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'energy and industrial marketing post')} covers how that world buys.</li>
<li><b>Pre-retirees in The Woodlands, Kingwood and Sugar Land.</b> Social Security timing, Medicare, income planning, and the hurricane-and-insurance budget conversation every Gulf Coast retiree has.</li>
<li><b>Business owners in Katy, Cypress and Tomball.</b> Exit planning, retirement plans for staff, entity and tax coordination. Partner with CPAs and estate attorneys; our {L('/blog/cpa-accounting-firm-marketing-houston/', 'CPA marketing guide')} shows their side.</li>
</ul>
"""),

            ("Run seminars and webinars that fill and convert", f"""<p>Seminars still work in Houston when the topic is narrow and timely and the follow-up is fast.</p>
<p>In {SRC['kitces']}, seminars produced a median of $7,679 in first-year revenue per new client, among the higher tactics measured. In our experience, 15 people in a Conroe library room who share one decision beat 80 in a ballroom who came for dinner.</p>
<ul>
<li><b>Treat everything as advertising:</b> the invitation, the slides, the replay and the follow-up email all go through compliance.</li>
<li><b>Promote 3 to 4 weeks out</b> with Meta event ads, an email to clients asking them to bring a friend, and a landing page with a short registration form.</li>
<li><b>Webinars for the busy and the far-flung:</b> energy staff on rotation and clients who moved to Montgomery County. Cut approved clips for LinkedIn.</li>
<li><b>Book the next step in the room.</b> A 20-minute call on the calendar before people leave is worth more than a feedback card.</li>
</ul>"""),

            ("Budget and spend: what to expect", f"""<p>The typical advisory practice spent about 11% of revenue on marketing in 2023, roughly $41,429, and 71% of that was advisor and staff time rather than cash, per {SRC['kitces']}. The table below is our planning view for a Houston practice, not a benchmark; your numbers depend on niche, offices and how good intake is.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Practice stage</th><th>Monthly paid media</th><th>Where it goes</th><th>Realistic goal</th></tr></thead>
<tbody>
<tr><td>Solo advisor, one office</td><td>$1,500 to $3,000</td><td>Google Search, Google Business Profile, reviews, one niche page</td><td>Steady booked intro calls; judge after 90 days</td></tr>
<tr><td>Two to four advisors</td><td>$3,000 to $7,500</td><td>Search plus LSA, quarterly seminar, Meta retargeting</td><td>New households each quarter at a known cost</td></tr>
<tr><td>Multi-office RIA</td><td>$7,500+</td><td>Per-office search, niche content, webinars, video</td><td>Cost per household and AUM by office and channel</td></tr>
</tbody></table></div>"""),

            ("Measure cost per new household and AUM", f"""<p>Track marketing by the cost to win a new household and the assets and revenue that household brings, because cost per lead tells you almost nothing in this business.</p>
<p>The median client acquisition cost in the Kitces survey was $3,800 in 2023, rising to $6,263 for clients with $1 million or more in investable assets, and the median practice earned only $0.60 in first-year revenue for each marketing dollar, per {SRC['kitces']}. A retained household pays for years, so 0.6 is fine. You still need to know which channel brings which client.</p>
<!--fig:funnel-->
<ul>
<li><b>Count every stage:</b> lead, intro call, discovery meeting, plan presented, household signed, assets transferred.</li>
<li><b>Track calls and forms by source</b> with call tracking and GA4; see {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking calls and forms')}.</li>
<li><b>Send signed households back to Google Ads</b> as offline conversions so bidding learns which searches turn into clients.</li>
<li><b>Respond within minutes.</b> Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} shows why the first firm to answer usually gets the meeting.</li>
</ul>"""),

            ("A first 90 days plan", f"""<!--fig:plan-->
<p>Compliance review eats much of the early weeks. Put approval time on the calendar from the start.</p>"""),

            ("Mistakes we see", f"""<ul>
<li><b>Embedding a Google review widget</b> on the site with no disclosures beside it.</li>
<li><b>Running Meta ads without the special ad category</b> and losing the ad account’s standing.</li>
<li><b>Judging campaigns at 30 days</b> when a household can take three months from first call to transfer.</li>
</ul>
<p>If you want a senior strategist to look at your market, registration and goals and build a plan around them, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much should a financial advisor spend on Google Ads in Houston?",
             "Most solo and small-team advisors in Houston should plan on $1,500 to $3,000 a month in Google Ads media to learn what works, based on our experience. Finance and insurance clicks average $3.39 and leads $74.44 nationally per WordStream’s 2026 benchmarks, so judge results by cost per new household, which the Kitces survey put at a median of $3,800."),
            ("Are Local Services Ads worth it for financial advisors?",
             "They can be. Google lists Financial planning services as an LSA category, you pay per lead rather than per click, and each planner goes through a license check. They pay off only if someone answers calls and messages quickly, and the profile and reviews still count as advertising under your compliance program."),
            ("Can financial advisors use Google reviews and testimonials?",
             "Yes. SEC-registered advisers can use testimonials under the Marketing Rule, and Texas adopted the same rule for state-registered advisers effective March 13, 2025. Displayed testimonials need clear and prominent disclosures about client status and compensation, and you can’t pay or reward clients for reviews. Have your compliance officer approve the process first."),
            ("Do Texas financial advisors have advertising rules?",
             "Yes. Texas-registered advisers must follow the SEC Marketing Rule, which the Texas State Securities Board adopted by reference in 7 TAC §116.15. SEC-registered advisers follow the federal rule directly, and broker-dealer reps follow FINRA Rule 2210, which requires principal approval of most retail communications. This isn’t legal advice, so confirm details with compliance."),
            ("Can financial advisors target ads by age on Facebook?",
             "No. Meta requires ads for investment services to run in its Financial Products and Services special ad category, which fixes age at 18 to 65+, removes gender and ZIP code targeting, requires at least a 15-mile radius and blocks lookalike audiences. Write ads specific enough, such as a pension workshop for retiring energy employees, that the right people pick themselves."),
        ],
        "figures": {
            "benchmarks": {
                "type": "stats",
                "title": "Google Ads benchmarks for finance and insurance",
                "stats": [["$3.39", "Median cost per click"], ["$74.44", "Median cost per lead"], ["2.64%", "Conversion rate"], ["9.83%", "Click-through rate"]],
                "note": "WordStream/LocaliQ 2026 benchmarks, US campaigns, April 2025 to March 2026",
                "alt": "Google Ads benchmark stats for financial advisor marketing in Houston: $3.39 CPC and $74.44 cost per lead",
                "caption": f"National medians from {SRC['wordstream']}. Houston advisor keywords can run higher.",
            },
            "reviews": {
                "type": "compare",
                "title": "Advisor testimonials: what exams flag vs. what passes",
                "left": {"title": "Flagged in SEC exams", "items": ["Disclosure behind a hyperlink", "Disclosure in lighter, smaller type", "Gift cards for reviews", "Google reviews pasted on site with no labels", "Rating badge with no date or period"]},
                "right": {"title": "Safer practice", "items": ["Client and compensation status shown beside it", "Same size and weight as the quote", "No rewards of any kind", "Disclosures next to embedded reviews", "Rating date, period, source and fees shown"]},
                "alt": "Comparison of compliant and flagged testimonial practices for financial advisor marketing in Houston and The Woodlands",
                "caption": f"Based on {SRC['sec_alert']}. Not legal advice.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From click to new household",
                "stages": [["Leads (calls, forms, LSA)", "60"], ["Intro calls held", "30"], ["Discovery meetings", "14"], ["Plans presented", "8"], ["Households signed", "4"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how leads become new households for a financial advisor in Houston and The Woodlands",
                "caption": "Illustrative quarter for a small practice. Measure each step so you know where prospects drop out.",
            },
            "plan": {
                "type": "steps",
                "title": "First 90 days for a Houston advisory practice",
                "sub": "Compliance review is built into every step",
                "steps": [["Days 1-15", "Confirm who approves what. Fix the Google Business Profile, bios, ADV links and tracking."], ["Days 16-30", "Write and approve one niche page and one town page. Set up call tracking and GA4."], ["Days 31-45", "Launch tight Google Search campaigns and apply for Local Services Ads."], ["Days 46-60", "Start a compliant review request process and add disclosures on the site."], ["Days 61-90", "Run one seminar or webinar. Report cost per meeting and per new household."]],
                "alt": "Five-step first 90 days marketing plan for a financial advisor in Houston and The Woodlands",
                "caption": "Start with search and tracking; add events once intake is tight.",
            },
        },
    },
]
