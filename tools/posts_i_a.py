"""Batch 9: foundation repair company marketing in Houston, and garage door company marketing in Houston.

Research: Houston Geological Society Bulletin (Garcia, Oct. 1995) on the Beaumont Formation and expansive clays; KPRC
Click2Houston July 2022 (Olshan: call volume almost doubled, average repair about $11,000, most insurance doesn't cover
foundation repair, 17% of Harris County in extreme drought); KPRC Click2Houston Sept. 18, 2026 (repairs $3,000 to over
$20,000, severe $40,000-$50,000, soaker hose advice); 22 Tex. Admin. Code 535.228 (TREC inspectors must render a written
opinion of foundation performance); Texas Board of Professional Engineers policy advisory opinion EAOR #43 (Feb. 2018);
House Bill 613 analysis, 83rd Legislature (no state standards for foundation repair contractors; proposed TDLR license);
Texas Section ASCE residential foundation guidelines (Ver. 3, effective April 1, 2022); Google Local Services Ads
category list and screening requirements (Foundations services; Garage door services with extra screening).
Garage door post: Google Ads policy on restricted local services (locksmiths and garage door repair need advanced
verification); Google Ads advanced verification help page (6-8 weeks, video call, licenses); Google's June 16, 2023 blog
post on its lawsuit (350+ fraudulent profiles, 14,000+ fake reviews, 20 million fake-profile attempts stopped in 2022);
DASMA fall 2023 summary (2017 Dallas Morning News story and advanced verification, 2019 WSJ, renamed listings, staged
props); Google Business Profile guidelines (names, service-area businesses, virtual offices); JLC Cost vs. Value 2025
Houston figures and Clopay's summary of the national 268% return; TDI windstorm inspection page and garage door repair
guidance; Google Maps prohibited content policy and PPC Land on the April 2026 staff-quota rule.
Competitor/PAA phrasing read for "foundation repair marketing", "foundation repair leads", "foundation repair google ads",
"garage door marketing", "garage door leads", "garage door google ads", "garage door advanced verification".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # foundation post
    "hgs": A("https://archives.datapages.com/data/HGS/vol38/no02/images/vol38no2p8.pdf", "a Houston Geological Society Bulletin article"),
    "kprc22": A("https://www.click2houston.com/news/local/2022/07/09/houston-home-foundation-repair-company-sees-uptick-in-business-amid-drought-conditions/", "KPRC 2 in July 2022"),
    "kprc26": A("https://www.click2houston.com/news/local/2026/09/18/should-you-water-your-foundation-houston-experts-explain-why-it-may-save-you-thousands/", "KPRC 2 this September"),
    "sop": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-535-228", "TREC’s standards of practice"),
    "tbpe": A("https://www.pels.texas.gov/nm/PAO43Final.pdf", "a 2018 advisory opinion from the Texas engineering board"),
    "hb613": A("https://capitol.texas.gov/tlodocs/83R/analysis/html/HB00613H.htm", "the bill analysis for House Bill 613"),
    "asce": A("https://www.texasce.org/resources/publications/residential-foundations/", "Texas Section of ASCE’s residential foundation guidelines"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "lsascreen": A("https://support.google.com/localservices/answer/12174778?hl=en", "Google’s screening requirements page"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    "ppcl": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
    # garage door post
    "restricted": A("https://support.google.com/adspolicy/answer/13527633?hl=en", "Google’s restricted local services policy"),
    "advver": A("https://support.google.com/google-ads/answer/7167635", "Google’s advanced verification page"),
    "gblog": A("https://blog.google/outreach-initiatives/public-policy/legal-action-stop-fake-review-scams/", "Google’s own announcement"),
    "dasma": A("https://www.dasma.com/wp-content/uploads/2023/09/GoogleandFTCTakeAction_Fall2023.pdf", "DASMA’s write-up of the case"),
    "gbpg": A("https://support.google.com/business/answer/3038177?hl=en", "Google Business Profile guidelines"),
    "cvv": A("https://www.jlconline.com/cost-vs-value/2025/west-south-central/houston-tx/", "the 2025 Cost vs. Value report’s Houston data"),
    "cvvnat": A("https://www.clopaydoor.com/blog/post/blog/2025/09/24/garage-door-replacement-top-ROI-in-cost-vs-value-report", "the top spot nationally for the second year running"),
    "tdi": A("https://tdi.texas.gov/tips/need-windstorm-inspection.html", "the Texas Department of Insurance"),
    "tdigarage": A("https://www.tdi.texas.gov/wind/documents/RepairingGarage.pdf", "TDI’s garage door guidance"),
}

FOUND = "/blog/foundation-repair-marketing-houston/"
GARAGE = "/blog/garage-door-company-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: foundation repair
    {
        "slug": "foundation-repair-marketing-houston",
        "title": "Foundation Repair Marketing in Houston: How to Get More Foundation Leads",
        "seo_title": "Foundation Repair Marketing in Houston: Get More Leads",
        "desc": "Foundation repair marketing for Houston pier and slab companies: Google Ads keywords, LSA, SEO pages, realtor and inspector leads, and what to track.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Google"],
        "art": "b1",
        "hero": "house",
        "hero_alt": "Illustration of a house on a slab for foundation repair marketing in Houston, The Woodlands and Katy",
        "related": ["local-seo-contractors-houston", "angi-vs-thumbtack-leads-worth-it-contractors", "speed-to-lead-response-time-follow-up-crm"],
        "sections": [
            (None, f"""<p>Thursday, 4:15 p.m. A listing agent in Kingwood calls. The buyer’s inspection report flagged “indications of adverse foundation performance,” the option period ends Tuesday, and the buyer wants an engineer’s letter and a repair bid before then. Meanwhile, a homeowner in Pearland who filled out a form on a lead site this morning has already heard from three of your competitors. You haven’t called her yet.</p>
<p>Those two leads tell you most of what you need to know about foundation repair marketing in Houston.</p>
<p>To get more foundation repair leads, you need to show up in Google search and Maps when a homeowner first notices a crack, and to be the company local agents and inspectors call when a sale is on the line. Then you have to follow up for weeks, because a $12,000 decision rarely gets made on the first visit. Ads and SEO cover the first part. Relationships and a disciplined follow-up process cover the rest, and most companies only do one of the three well.</p>
<p>This is for owners of pier and slab repair companies, from two-crew shops to outfits running estimators across the whole metro.</p>"""),

            ("Why foundation demand in Houston comes in waves", f"""<p>Houston sits on some of the worst soil in the country for a slab. Much of the city is built on the Beaumont Formation, whose clay-rich soils shrink when dry and swell when wet, according to {SRC['hgs']} by a University of Houston-Clear Lake geologist. The same piece notes that about a quarter of the U.S. sits on some kind of expansive soil and calls the Texas Coastal Plain the most notable area for it. Combine that clay with long dry spells followed by downpours and you get slabs that move.</p>
<p>The movement shows up in your phone log. During the summer 2022 drought, the general manager of a large foundation company in Cypress told {SRC['kprc22']} that call volume had “almost doubled,” the busy season started about a month early, and crews were booked four weeks out. He put the average repair at about $11,000, with some reaching $30,000, and noted that most insurance policies don’t cover foundation repair. In {SRC['kprc26']}, a League City repair owner described doing seven evaluations in a single day after six dry weeks, and the station put typical repairs between $3,000 and more than $20,000, with severe cases at $40,000 to $50,000.</p>
<!--fig:stats-->
<p>Two marketing consequences follow. First, demand spikes after a dry stretch, and a smaller second wave tends to arrive when heavy rain returns and soil swells unevenly. Your budget should be able to move with the weather instead of sitting flat at the same amount every month. Second, the homeowner is facing a five-figure bill that insurance probably won’t touch. That buyer researches, gets several bids and takes their time. Your marketing has to support a long decision, and a lead from the first click is just the start.</p>"""),

            ("The three kinds of foundation leads (and what each one needs)", f"""<p>Most foundation companies lump every inquiry together. They behave very differently.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Lead type</th><th>How it starts</th><th>Urgency</th><th>What wins it</th></tr></thead>
<tbody>
<tr><td>Homeowner-noticed</td><td>A sticking door, a diagonal crack over a window, a gap between brick and trim. Searches “foundation repair near me” or “cracks in wall above door.”</td><td>Low to medium. Weeks to months.</td><td>Search and Maps visibility, education, reviews, patient follow-up</td></tr>
<tr><td>Real estate transaction</td><td>An inspection report flags the foundation during the buyer’s option period. The agent calls someone they trust.</td><td>Very high. Days.</td><td>Agent and inspector relationships, fast bids, engineer coordination, a transferable warranty</td></tr>
<tr><td>Engineer or referral</td><td>A structural engineer’s report recommends repairs, or a past customer sends a neighbor.</td><td>Medium. The scope is already defined.</td><td>Being on the engineer’s short list, clean paperwork, a bid that follows the report</td></tr>
</tbody></table></div>
<p>The real estate lead deserves its own section. Texas home inspectors must “render a written opinion as to the performance of the foundation” and report the visible indications behind it, such as doors that bind, sloping floors and cracked masonry, under {SRC['sop']}. But inspectors can’t give an engineering opinion on the cause or the fix unless they’re also licensed engineers, per {SRC['tbpe']}. So a flagged report usually sends the buyer to an engineer and then to repair companies, all inside a short option period. The company that answers on a Thursday afternoon and has a bid out by Saturday gets the job far more often than the one with the nicest website.</p>"""),

            ("A foundation repair website that earns the call", f"""<p>Foundation buyers are scared and skeptical. They’ve heard stories about companies that “find” $25,000 of work. Your site has to answer the questions they’re too embarrassed to ask on the phone.</p>
<p>Texas doesn’t license foundation repair contractors at the state level. A 2013 bill, House Bill 613, would have created a TDLR license, and {SRC['hb613']} noted the lack of any state standards for the trade. It didn’t pass. That means your site has to do the trust-building a license would otherwise do. Pages we’d build for a Houston pier company:</p>
<ul>
<li><b>Warning signs page.</b> Photos of the real symptoms: stair-step cracks in brick, doors that won’t latch, gaps at the frieze board, tile cracking across a room. This page ranks for the searches people make before they know they need you.</li>
<li><b>Repair methods page.</b> Pressed concrete pilings, steel piers, drilled bell-bottom piers, mudjacking or foam for flatwork, pier-and-beam shimming. What you install, why, and when you don’t recommend one.</li>
<li><b>Cost page.</b> Honest ranges by job type, what drives price (number of piers, access, breakouts inside the house, plumbing tests), and what the free inspection includes. Yes, a cost page. People search “foundation repair cost Houston” far more than they search your name.</li>
<li><b>Warranty page.</b> The actual terms in plain English: length, what’s covered, what voids it (no watering, plumbing leaks), and whether and how it transfers to a new owner, with any transfer fee. Real estate agents look for this page.</li>
<li><b>Engineers and process page.</b> Whether you work with independent engineers, who pays for the engineer’s letter, whether you pull permits where required, and how post-repair elevations are documented. Mention that your work follows {SRC['asce']} if it does, because buyers’ engineers often reference them.</li>
<li><b>Real estate page.</b> Turnaround time for bids during an option period, how you coordinate with the buyer’s engineer, sample warranty transfer letter, a direct line for agents.</li>
<li><b>Area pages</b> for the places where you have jobs, reviews and photos: Kingwood and Humble, Katy, Cypress, Sugar Land, Pearland, League City, Spring and The Woodlands. Write about what you actually see there, like older pier-and-beam homes in the Heights versus newer slabs in Cypress subdivisions. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} covers how to keep these from becoming thin copies of each other.</li>
</ul>
<p>Every page needs a phone number at the top, a short form that asks for address and what they’re seeing, and a photo upload so the homeowner can send pictures of the crack. That upload alone lets your estimator triage before driving to Tomball.</p>"""),

            ("Google Ads for foundation repair: keywords, negatives, settings", f"""<p>Search ads are where foundation companies spend the most and waste the most. The searches are expensive and full of DIY researchers, renters and people looking for a different kind of foundation.</p>
<p>Structure we’d start with:</p>
<ul>
<li><b>Core repair campaign:</b> foundation repair near me, foundation repair Houston, foundation repair company, slab repair, house leveling, foundation contractor plus town names (Katy, Pearland, Spring, Kingwood).</li>
<li><b>Symptom campaign:</b> cracks in brick wall house, doors sticking foundation, foundation settling, foundation cracks. Lower intent, cheaper, and best sent to your warning signs page with a “send us photos” form.</li>
<li><b>Pier-and-beam campaign:</b> pier and beam repair, pier and beam leveling, crawl space repair. Only if you do it well.</li>
<li><b>Real estate campaign:</b> foundation inspection for home sale, foundation repair before selling house, foundation engineer report Houston. Small volume, very high value.</li>
<li><b>Brand.</b> Cheap, and it keeps lead sites from sitting on top of your name.</li>
</ul>
<!--fig:negatives-->
<p>Settings that matter. Set location targeting to “Presence: people in or regularly in your included locations,” and draw it around where your crews will actually drive. Track calls from ads and from the website as conversions, with a minimum call length so wrong numbers don’t count. And because a signed job can come six weeks after the click, import booked inspections and signed contracts from your CRM as offline conversions. Without that, Google optimizes for form fills from people who just wanted a free opinion. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'guide to tracking calls and forms')} walks through the setup.</p>
<p>Sample responsive search ad headlines (each under 30 characters):</p>
<ul>
<li>Foundation Repair in Katy</li>
<li>Free Foundation Inspection</li>
<li>Transferable Warranty</li>
<li>Bids Fast During Option Period</li>
<li>Send Us Photos of the Crack</li>
<li>Steel and Concrete Piers</li>
</ul>
<p>On cost, foundation keywords are among the pricier home services clicks we see, and in accounts we’ve run a qualified inspection often costs several hundred dollars in ad spend. That only makes sense if you know your close rate and average ticket. Check our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} before you set a budget, and our {L('/services/search-marketing/', 'search marketing team')} can build the account if you’d rather not.</p>"""),

            ("Local Services Ads and the map pack", f"""<p>“Foundations services” is one of the categories in {SRC['lsa']}, so you can run pay-per-lead ads above the regular search ads in most of Houston. Per {SRC['lsascreen']}, foundation companies go through business and owner background checks, business registration checks and a general liability insurance check, with state-level license checks applying only where a license exists. That last part mostly doesn’t apply in Texas.</p>
<p>LSA rewards reviews, responsiveness and booking. If your rating is strong and someone answers the phone every time, test it alongside search ads and dispute the leads that aren’t real customers. Our comparison of {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')} goes deeper.</p>
<p>The Google Business Profile matters more than most foundation companies treat it. A few specifics:</p>
<ul>
<li>Pick the primary category that most closely describes foundation repair (type “foundation” into the category field and choose the contractor option), and add secondary categories only for work you do in-house, like concrete or drainage.</li>
<li>If you don’t meet customers at your yard, set up as a service-area business with your address hidden, and list the areas you serve.</li>
<li>Upload job photos weekly. Pier holes, steel going in, the before-and-after crack. Real crews in real Houston yards beat stock photos every time.</li>
<li>Answer the Q&amp;A and keep your hours honest. A profile that says “open 24 hours” gets 10 p.m. calls you can’t serve.</li>
</ul>
<p>Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} has the full checklist.</p>"""),

            ("Reviews for a business customers only use once", f"""<p>A foundation customer won’t hire you twice, so reviews are your repeat business. They also answer the biggest fear a homeowner has: being upsold.</p>
<p>Two moments to ask. Right after the crew cleans up and the final elevations are done, while the homeowner is watching doors close properly for the first time in a year. And again, gently, if you come back for a warranty adjustment and handle it well. That second review is gold because it proves the warranty means something.</p>
<p>A text that works: “Thanks for trusting us with your home, Ms. Alvarez. If you have two minutes, a Google review helps neighbors in Kingwood find an honest foundation company: [link]. Either way, your warranty paperwork is attached.”</p>
<p>The rules, from {SRC['gpol']}: no discounts or gifts for reviews, no discouraging negative ones, and no asking only the happy customers. Google also added language in April 2026 against telling staff to collect a set number of reviews or reviews with specific content, per {SRC['ppcl']}. So skip the “estimator with the most five-star reviews wins a bonus” contests. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more scripts.</p>"""),

            ("Lead-seller platforms and the speed problem", f"""<p>Back to the Pearland homeowner who heard from three companies before you. That’s how most shared lead platforms work: one form, several contractors, and the first one to call usually books the inspection.</p>
<p>We don’t tell foundation companies to quit lead platforms on principle. Some do well with them. But judge them on cost per signed job, not cost per lead, and only after you’ve fixed your response time. If a platform lead sits for two hours, you’re paying to hand it to a competitor. Our breakdown of {L('/blog/angi-vs-thumbtack-leads-worth-it-contractors/', 'Angi and Thumbtack leads')} covers the math, and the {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the process fix.</p>
<!--fig:sources-->
<p>Over time, the goal is to shift your mix toward leads you own: your own search ads, your Maps profile, agents, engineers and past customers. Those leads aren’t being shopped to four companies at once, and they close at better margins.</p>"""),

            ("Working with realtors, inspectors and engineers", f"""<p>This is the channel almost every foundation company says matters and almost none works on purpose.</p>
<ol>
<li><b>Make a list.</b> The 50 agents who list the most homes in your strongest areas (HAR makes this easy), the busiest inspectors, and the independent structural engineers who write foundation letters in your service area.</li>
<li><b>Give agents a reason to call you.</b> A promise you can keep, like “written bid within 48 hours during an option period,” plus a one-page explainer they can hand a nervous buyer, and a sample warranty transfer letter.</li>
<li><b>Show up.</b> Brokerage sales meetings in Kingwood, The Woodlands and Katy often welcome a 10-minute talk on reading the foundation section of an inspection report. Bring photos, skip the pitch.</li>
<li><b>Respect the engineers.</b> Bid to the engineer’s report instead of redesigning it, send post-repair elevations without being asked, and never badmouth a design. Engineers remember which contractors make them look good.</li>
<li><b>Track it.</b> Put “referring agent” and “referring engineer” fields in your CRM so you can see who actually sends signed work.</li>
</ol>
<p>Our post on {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'how local agents market themselves')} is a useful look at the other side of this relationship.</p>"""),

            ("Following up on a long, expensive decision", f"""<p>A homeowner facing a $14,000 bid gets two more bids, talks to their brother-in-law, reads about watering their foundation and waits for the next paycheck. The companies that win are the ones still in touch in week five.</p>
<p>A follow-up sequence that doesn’t feel pushy:</p>
<ul>
<li>Same day: the written bid by email, with photos from the inspection and a plain explanation of each line.</li>
<li>Day 3: a short text asking if they have questions about the bid or the warranty.</li>
<li>Week 2: an email on how to compare foundation bids fairly (pier count, pier type, depth, warranty, transferability). Helpful even if they don’t pick you.</li>
<li>Week 4: financing options, if you offer them.</li>
<li>Month 2 and 3: a check-in, and a reminder that dry weather makes symptoms worse.</li>
</ul>
<p>Meanwhile, retarget site visitors with short videos of your crews and testimonials on YouTube and Meta. Retargeting won’t create demand, but it keeps you in the shortlist while they decide. Our {L('/services/paid-social-advertising/', 'paid social team')} runs these if you’d rather hand it off.</p>"""),

            ("What to spend, and a first 90 days", f"""<p>There’s no honest single number. For a two- to four-crew pier company in Greater Houston, this is an illustrative starting point. It isn’t a quote or a benchmark.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>Google Ads (search)</td><td>$3,000 to $8,000</td><td>Core, symptom and real estate campaigns in your crew radius</td></tr>
<tr><td>Local Services Ads</td><td>$1,000 to $3,000</td><td>Pay-per-lead test in the Foundations category</td></tr>
<tr><td>SEO and content</td><td>$1,500 to $3,000</td><td>Cost, warranty, methods and area pages, profile upkeep</td></tr>
<tr><td>Retargeting</td><td>$300 to $800</td><td>Video and testimonial reminders during the decision window</td></tr>
<tr><td>Agent and engineer outreach</td><td>$200 to $500</td><td>Printed explainers, lunches, a few hours a week of someone’s time</td></tr>
</tbody></table></div>
<!--fig:budget-->
<p>A sensible first 90 days:</p>
<ul>
<li><b>Days 1-30:</b> Set up call tracking and a CRM stage for inspection booked, bid sent and signed. Fix the Business Profile. Publish the cost and warranty pages. Launch the core search campaign with the negatives above.</li>
<li><b>Days 31-60:</b> Add the symptom and real estate campaigns. Start the review text after every completed job. Build the agent list and book your first two brokerage meetings.</li>
<li><b>Days 61-90:</b> Start offline conversion imports. Test LSA. Write area pages for your three best towns. Compare cost per signed job by source and move money toward what closes.</li>
</ul>
<p>Mistakes we see over and over: judging campaigns on lead count when half the leads were renters; one landing page for every keyword; no photo upload on the form; estimators who never log the referring agent; and budgets that stay flat through a drought, when every competitor is getting their best month of the year. Our {L('/blog/seo-cost-houston-the-woodlands/', 'SEO cost guide')} explains how to judge the content line.</p>
<p>If you want a plan built around your crews, service area and close rate, <a href="/contact/">get in touch</a> and tell us what you’re running now. A senior strategist will put together a plan for your company.</p>"""),
        ],
        "faq": [
            ("How do foundation repair companies get more leads?",
             "Most foundation leads come from Google searches, the Maps pack, Local Services Ads, lead platforms and referrals from real estate agents, inspectors and engineers. The companies that grow fastest pair search visibility with honest cost and warranty pages, answer calls within minutes, and build relationships with agents who need quick bids during option periods. Track every lead to a signed job so you know which sources pay."),
            ("Is Google Ads worth it for foundation repair?",
             "It can be, because people searching foundation repair plus a town name usually have a real problem. Clicks are expensive, though, so use tight location targeting, a long negative keyword list for DIY, jobs and other meanings of foundation, and dedicated landing pages. Import booked inspections and signed contracts as offline conversions so Google learns which clicks become customers, not just form fills."),
            ("Do foundation repair contractors need a license in Texas?",
             "Texas does not license foundation repair contractors at the state level. A 2013 bill, House Bill 613, would have created a license through TDLR, but it did not pass. Some cities require permits for certain work, and the engineering side is regulated: Texas inspectors can describe foundation performance but cannot give an engineering opinion on causes or repairs unless they are licensed engineers."),
            ("Can foundation companies use Google Local Services Ads?",
             "Yes. Foundations services is one of Google's Local Services Ads categories. Companies go through business and owner background checks, a business registration check and a general liability insurance check, with license checks where a state license exists. You pay per lead rather than per click and can dispute leads that are not real customers. Strong reviews and fast responses help your ranking."),
            ("How do I get foundation leads from real estate agents?",
             "Make it easy for agents to send you work during a buyer's option period. Promise and deliver written bids within a day or two, coordinate with the buyer's engineer, explain your warranty transfer process in writing, and give agents a direct phone line. Speak at brokerage meetings about reading the foundation section of an inspection report, and record the referring agent on every job."),
        ],
        "figures": {
            "stats": {
                "type": "stats",
                "title": "Houston soil and foundation repair costs",
                "stats": [["~25%", "of the U.S. sits on expansive soil"], ["2x", "call volume one Cypress firm saw in the 2022 drought"], ["$3K-$20K+", "typical repair range KPRC reported in 2026"], ["$40K-$50K", "severe cases"]],
                "note": "Sources: Houston Geological Society Bulletin, KPRC 2",
                "alt": "Stats on expansive clay soil and foundation repair costs that shape foundation repair marketing in Houston",
                "caption": f"From {SRC['hgs']}, {SRC['kprc22']} and {SRC['kprc26']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for foundation repair ads",
                "sub": "Add before launch, then mine the search terms report weekly",
                "items": ["DIY: how to, diy, yourself, youtube, kit", "Makeup and charity: makeup, liquid foundation, charitable foundation, nonprofit", "Jobs: jobs, hiring, salary, estimator jobs", "Renters: landlord, apartment, rent", "New build: pour a slab, new foundation cost, footing design", "Classes: course, training, certification, engineering degree", "Other trades: pool, retaining wall (unless you do them)", "Free only: free foundation (if you charge for engineer letters)"],
                "alt": "Checklist of negative keywords for foundation repair Google Ads in Houston and The Woodlands",
                "caption": "The word foundation has more meanings than you think. Your search terms report will prove it.",
            },
            "sources": {
                "type": "compare",
                "title": "Shared leads vs. leads you own",
                "left": {"title": "Shared lead platforms", "items": ["Same lead sold to several companies", "First caller usually wins", "Judged on cost per lead", "No relationship after the job", "Price pressure from competing bids"]},
                "right": {"title": "Owned sources", "items": ["Your search ads, Maps profile and site", "Agents and engineers who call you first", "Judged on cost per signed job", "Reviews and referrals compound", "Better close rates and margins"]},
                "alt": "Comparison of shared lead platforms and owned lead sources for foundation repair companies in Houston",
                "caption": "Keep platforms if they close. Build the right side so you depend on them less each quarter.",
            },
            "budget": {
                "type": "bars",
                "title": "Example monthly marketing mix",
                "sub": "Two- to four-crew pier company, midpoint of each range",
                "items": [["Google Ads", 5500, "$5,500"], ["Local Services Ads", 2000, "$2,000"], ["SEO and content", 2250, "$2,250"], ["Retargeting", 550, "$550"], ["Agent outreach", 350, "$350"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of an example monthly marketing budget for a foundation repair company in Houston and The Woodlands",
                "caption": "Midpoints of the illustrative ranges above. Let tracked cost per signed job decide the real mix.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: garage doors
    {
        "slug": "garage-door-company-marketing-houston",
        "title": "Garage Door Company Marketing in Houston: Beating the Fake Listings",
        "seo_title": "Garage Door Company Marketing in Houston",
        "desc": "Garage door company marketing in Houston: advanced verification, Local Services Ads, fake Google Maps listings, reviews, ad keywords and install vs. repair.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google Ads", "Google"],
        "art": "b3",
        "hero": "tools",
        "hero_alt": "Illustration of a key for garage door company marketing in Houston, Cypress and The Woodlands",
        "related": ["google-business-profile-video-verification", "google-guaranteed-vs-google-verified", "local-services-ads-vs-google-ads-home-services"],
        "sections": [
            (None, f"""<p>Tuesday, 6:50 a.m. in Cypress. A torsion spring snaps with a bang that wakes the house, and the minivan is stuck behind a door that won’t move. The parent who has to get two kids to school searches “garage door repair near me” on a phone. Near the top of the map is a listing called something like “Garage Door Repair Cypress TX,” no street address, 41 five-star reviews that all read the same. They call. A dispatcher in another state takes the job and sells it to whichever tech picks up.</p>
<p>Your shop is eight minutes away with a truck full of springs. You never got the call.</p>
<p>Garage door company marketing in Houston comes down to winning that 6:50 a.m. search against competitors who aren’t always real businesses. To get more garage door customers, pass Google’s advanced verification so you can run search ads and Local Services Ads, then build a Maps profile and review base that look unmistakably local. Answer the phone every time, and turn repair calls into the install work where the margin is.</p>"""),

            ("The fake listing problem, and why Google treats your category differently", f"""<p>Garage door repair is one of the most abused categories on Google Maps, and Google knows it.</p>
<p>In 2017, after a Dallas Morning News story on door businesses violating Google’s policies, Google started requiring garage door companies in key markets to pass an advanced verification process, according to {SRC['dasma']} from the industry’s trade association. A 2019 Wall Street Journal investigation put fake Maps listings in the national spotlight. And in June 2023, Google sued an operator it said had created more than 350 fraudulent Business Profiles backed by over 14,000 fake reviews, per {SRC['gblog']}. DASMA’s summary says the listings included garage door repair, that one profile went from maid service to garage door company 42 days after it was created, and that the same tool bench appeared in verification photos for two different businesses. The profiles were allegedly sold as lead sources to real companies.</p>
<p>Google said it stopped 20 million attempts to create fake Business Profiles in 2022. Plenty still get through, especially in emergency trades where a single call can be worth several hundred dollars.</p>
<p>For a real Houston company, that means a few practical things:</p>
<ul>
<li>You’re competing with call centers and lead networks as well as the shop down the road. They’re fast and they’re everywhere, and they play by different rules.</li>
<li>Google’s systems are suspicious of your whole category, so your own profile gets more scrutiny. Expect verification by video and the occasional suspension. Our post on {L('/blog/google-business-profile-video-verification/', 'Business Profile video verification')} covers how to prepare.</li>
<li>Copying the spammers backfires. Google’s {SRC['gbpg']} say unnecessary information in a business name isn’t permitted, virtual offices aren’t eligible, and each business gets one profile. Keyword-stuffed names and extra listings at mailbox stores are how real companies lose their profiles.</li>
<li>You can report fake competitors through the guidelines page’s link for reporting third-party policy violations. Document it with screenshots, the phone number, and proof the address is a vacant lot or a UPS Store. It’s slow, and sometimes it works.</li>
</ul>"""),

            ("Advanced verification: the gate before any Google ad runs", f"""<p>This is the step that trips up the most new garage door advertisers. Per {SRC['restricted']}, ads for garage door repair services in the U.S. are restricted, and to advertise you must apply for advanced verification.</p>
<p>From {SRC['advver']}:</p>
<!--fig:verify-->
<ul>
<li>Passing Business Profile verification doesn’t count. Neither do Local Services background and license checks. Advanced verification is a separate process.</li>
<li>You submit a request form with your Google Ads customer ID, business name, owner, address, phone and a working website. If the account is new, build at least one campaign first.</li>
<li>You may get a video call with a Google agent, so be at your shop (or near your branded vehicle) when they call.</li>
<li>You must hold any licenses your location legally requires.</li>
<li>Google says it typically takes six to eight weeks. Until you pass, your ads won’t show on garage door searches.</li>
<li>Report changes to your name, address or license promptly, or you can fall out of compliance.</li>
</ul>
<p>Plan for that six-to-eight-week gap. If you’re opening a new location in Katy or Conroe, start verification before the sign goes up. And if an agency tells you it can “get around” verification for you, find another agency.</p>"""),

            ("Local Services Ads for garage door companies", f"""<p>“Garage door services” is one of the categories in Google’s Local Services Ads list, and for an emergency trade, LSA is often the best-converting paid placement you can buy. You pay per lead rather than per click, the ads sit at the top of the page, and the person who calls already sees your reviews and hours.</p>
<p>The screening is heavier than for most trades. {SRC['lsascreen']} flags garage door as an urgent category with an extra level of screening that includes service professional background checks, on top of advanced verification. Google’s category list also notes that “pre-badge” ads, which let some newer advertisers start serving early, aren’t available for garage door services. So you won’t get any head start. Budget the onboarding time.</p>
<p>Once you’re live:</p>
<ul>
<li>Set your hours to match when someone really answers. LSA punishes missed calls.</li>
<li>Pick job types you actually want. If you don’t do commercial roll-up doors, turn them off.</li>
<li>Dispute leads that weren’t real customers (wrong service, spam, out of area). Do it every week.</li>
<li>Ask every LSA customer for a review. LSA reviews and responsiveness drive where you rank.</li>
</ul>
<p>We explain the badge differences in {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified')} and when to run LSA alongside regular search ads in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</p>"""),

            ("A Business Profile that looks as local as it is", f"""<p>When a homeowner compares your listing to a lead network’s, small signals decide the call. Make yours obviously real.</p>
<ul>
<li><b>Name:</b> your legal or branded name, exactly as it appears on your trucks and invoices. No “24/7” or city names added.</li>
<li><b>Address:</b> if customers don’t come to your shop, set up as a service-area business with the address hidden, as the guidelines require. If you have a showroom, show it, with hours.</li>
<li><b>Service areas:</b> the towns your trucks really reach in an hour. Cypress, Jersey Village, Tomball, Spring, Klein, The Woodlands and so on. Don’t list the whole metro from one truck in Magnolia.</li>
<li><b>Photos:</b> your branded trucks, your techs in uniform, real installs in real neighborhoods, your warehouse shelves. Upload a few every week. Lead networks don’t have these.</li>
<li><b>Services:</b> spring replacement, opener repair and installation, cable and roller repair, off-track doors, new door installation, insulated doors, commercial if you do it. Each with a sentence in plain English.</li>
<li><b>Website link:</b> a real page with your Texas address, team photos and license or insurance info where it applies.</li>
</ul>
<p>The {L('/blog/rank-in-google-map-pack-houston/', 'Houston map pack guide')} covers the ranking side, and our post on {L('/blog/google-business-listing-scam-calls/', 'Google listing scam calls')} explains the robocalls you’ll get the minute your profile goes live.</p>"""),

            ("Reviews that read like real customers", f"""<p>Fake profiles tend to have reviews that sound alike, arrive in bursts and never mention a street or a person. Real reviews mention the tech, the neighborhood, the time of day and the specific part. That texture matters more in this category than in almost any other.</p>
<p>The rules, from {SRC['gpol']}: no incentives for reviews, no discouraging negative ones, no asking only the happy customers. In April 2026 Google added language against telling staff to collect a set number of reviews or reviews with specific content, which may include asking customers to name a particular tech, per {SRC['ppcl']}. The scope isn’t settled, so we’d drop tech review-count bonuses and simply ask every customer.</p>
<p>A text that goes out within an hour of the job: “Thanks for having us out today. If the door’s running smoothly, would you mind leaving us a quick Google review? It helps people in Spring find a real local company: [link]. If anything’s off, reply here and we’ll come back.”</p>
<p>Reply to every review with something specific. And if a lead network has been collecting reviews under a lookalike name, don’t respond in kind. Report it and keep stacking real ones. Our {L('/blog/fake-reviews-rule-local-businesses/', 'post on the fake reviews rule')} covers the legal side.</p>"""),

            ("Google Ads keywords for repair and install", f"""<p>Split your account in two. Emergency repair and new door installation are different customers with different budgets and different landing pages.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Example keywords</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Emergency repair</td><td>garage door repair near me, garage door spring repair, broken garage door spring, garage door won’t open, garage door off track</td><td>Call-focused. Run 24/7 only if someone answers 24/7.</td></tr>
<tr><td>Openers</td><td>garage door opener repair, garage door opener installation, LiftMaster repair (only brands you service)</td><td>Mid ticket. Good for upgrades to battery backup and smart openers.</td></tr>
<tr><td>New doors</td><td>new garage door installation Katy, garage door replacement, insulated garage doors, garage door quote</td><td>Longer decision. Send to a gallery and quote page.</td></tr>
<tr><td>Wind-rated doors</td><td>wind rated garage doors, hurricane garage door Galveston, windstorm certified garage door</td><td>Mostly coastal counties. Small volume, high ticket.</td></tr>
<tr><td>Commercial</td><td>commercial overhead door repair, roll up door repair Houston, dock door repair</td><td>Only if you have the equipment and crew.</td></tr>
</tbody></table></div>
<!--fig:negatives-->
<p>Settings: “Presence” location targeting, a radius your trucks can reach within an hour, call assets on a schedule that matches your phone coverage, and calls over 60 seconds counted as conversions. Send repair clicks to a page that loads fast on a phone and shows your number in big type. Send install clicks to a page with photos and a quote form.</p>
<p>Sample headlines (under 30 characters each): “Broken Spring? Same-Day Fix,” “Local Cypress Garage Doors,” “Real Techs, Real Trucks,” “Upfront Pricing Before Work,” “New Doors Installed in Katy.” Keep claims you can back up. If you say same-day, mean it.</p>
<p>Our {L('/services/search-marketing/', 'Google Ads team')} manages accounts like this, and our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} shows how to tell which campaign made the phone ring.</p>"""),

            ("Repair calls pay the bills. Installs build the business", f"""<p>A spring replacement gets you in the driveway. A new door is where garage door companies make real money, and the best time to sell one is while you’re standing in front of the old one.</p>
<p>Homeowners have a good reason to listen. Garage door replacement took {SRC['cvvnat']} in the 2025 Cost vs. Value report, with an estimated 268% of cost recouped at resale. In {SRC['cvv']}, the project averaged about $4,607 with an estimated resale value of about $11,307, or roughly 245% recouped. Those are estimates from appraisers and agents, not a promise, but they make a strong talking point on an install page and in a tech’s conversation.</p>
<!--fig:value-->
<p>How we’d connect the two:</p>
<ul>
<li>Train techs to give an honest repair-or-replace opinion with a written quote for both, photographed and texted. No pressure. Most owners decide later.</li>
<li>Follow up on every replacement quote at 3 days, 2 weeks and 6 weeks, with photos of similar doors you’ve installed in their area.</li>
<li>Run Meta and YouTube ads with before-and-after videos of installs in your neighborhoods, aimed at homeowners near your best ZIP codes. Curb appeal is visual, and these ads sell it far better than a search ad can. Our {L('/services/paid-social-advertising/', 'paid social team')} builds these.</li>
<li>Show insulated door options. In a Houston summer, a lot of people use the garage as a workshop or gym, and a door with real insulation is an easy upgrade to explain.</li>
</ul>
<!--fig:repair-->
<p>One more thing on price. The category is full of “$29 service call” ads that turn into $900 invoices, and Houston homeowners have learned to distrust them. Publishing honest starting prices for spring replacement and opener installs costs you a few bargain hunters and earns you a lot of trust.</p>"""),

            ("Hurricane season and wind-rated doors on the coast", f"""<p>On the Texas coast, a garage door replacement comes with paperwork. Per {SRC['tdi']}, properties in 14 coastal counties and in parts of Harris County east of Highway 146 are in a designated catastrophe area, where most new construction, major repairs and other alterations require a windstorm inspection. Most homes need a certificate of compliance (a WPI-8 or WPI-8-E) to be insured through the Texas Windstorm Insurance Association.</p>
<p>{SRC['tdigarage']} notes that most major garage door manufacturers have product listings with TDI, that published wind ratings matter in high wind areas, and that doors must be installed in strict accordance with the manufacturer’s instructions. If you sell in Galveston, League City, Kemah or Brazoria County, build a wind-rated door page that explains product listings, the inspection, and what paperwork the homeowner gets at the end. Have your installers confirm the requirements for each job, and tell homeowners to check with their insurance agent.</p>
<p>Inland in Spring or The Woodlands, wind-rated doors aren’t the same requirement, but plenty of homeowners still want a sturdier door after a bad storm year. Schedule an install promotion before June 1 and keep a storm-damage ad group paused and ready for the morning after.</p>"""),

            ("What to spend, and the first 90 days", f"""<p>For a single-location residential garage door company with three to six trucks, this is an illustrative starting point. These are examples, not quotes or benchmarks.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>Local Services Ads</td><td>$1,500 to $4,000</td><td>Pay-per-lead emergency calls, after verification</td></tr>
<tr><td>Google Ads (search)</td><td>$2,000 to $5,000</td><td>Repair, opener and install campaigns</td></tr>
<tr><td>Meta and YouTube</td><td>$500 to $1,500</td><td>Install videos and retargeting</td></tr>
<tr><td>Local SEO and profile</td><td>$750 to $2,000</td><td>Service and area pages, photos, review replies</td></tr>
<tr><td>Review and follow-up software</td><td>$100 to $400</td><td>Review texts, quote follow-ups</td></tr>
</tbody></table></div>
<p>First 90 days:</p>
<ul>
<li><b>Days 1-30:</b> Submit advanced verification and LSA onboarding on day one. Clean up the Business Profile, add real photos, publish starting prices. Set up call tracking and recorded calls.</li>
<li><b>Days 31-60:</b> Start the review text after every job. Build repair and install landing pages. Prepare search campaigns with the negatives above so they launch the day verification clears.</li>
<li><b>Days 61-90:</b> Launch LSA and search. Start install video ads in your best neighborhoods. Review recorded calls weekly for missed bookings, and compare cost per booked job by source.</li>
</ul>
<p>Mistakes we see: letting calls roll to a voicemail at 7 a.m.; one landing page for repair and install; counting every 10-second call as a lead; adding city names to the profile name; and pausing ads in winter when spring breaks don’t care what month it is. The {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers phone coverage options.</p>
<p>If you’re ready to compete with the lookalike listings, <a href="/contact/">get in touch</a> and tell us about your trucks, service area and goals. A senior strategist will build a plan for your company. If you also run a foundation or concrete crew, our {L(FOUND, 'foundation repair marketing post')} covers that side.</p>"""),
        ],
        "faq": [
            ("Why can't my garage door company run Google Ads?",
             "Google restricts ads for garage door repair services in the United States. Before your ads can show on those searches, you must pass advanced verification, which is separate from Business Profile verification and from Local Services Ads screening. You submit a request form, may complete a video call at your business, and must hold any required licenses. Google says it typically takes six to eight weeks."),
            ("Are Local Services Ads good for garage door companies?",
             "Often, yes. Garage door services is a Local Services Ads category, and emergency callers like seeing reviews and hours at the top of the page. Screening is heavier than most trades, with service professional background checks plus advanced verification, and pre-badge ads are not available. Answer every call, keep hours accurate, dispute bad leads weekly and ask every customer for a review."),
            ("How do I deal with fake garage door listings on Google Maps?",
             "Report them through the Business Profile guidelines page link for reporting third-party policy violations, with screenshots, the phone number and proof the address is fake, like a vacant lot or a mailbox store. Do not copy their tactics, since keyword-stuffed names, virtual offices and duplicate profiles violate Google's guidelines. Focus on real photos, branded trucks and detailed reviews that fake listings cannot match."),
            ("What keywords should a garage door company bid on?",
             "Split repair and installation. Repair keywords include garage door repair near me, broken garage door spring, garage door won't open and opener repair. Installation keywords include garage door replacement, new garage door installation plus a town name and insulated garage doors. Add negatives for DIY, parts, jobs, car door and rental searches, and review the search terms report weekly during the first month."),
            ("Do I need a wind-rated garage door in Houston?",
             "It depends on location. The Texas Department of Insurance says properties in 14 coastal counties and parts of Harris County east of Highway 146 are in a designated catastrophe area, where most major repairs and alterations need a windstorm inspection, and most homes need a certificate of compliance for windstorm association coverage. Homeowners should confirm with their installer and insurance agent before buying."),
        ],
        "figures": {
            "verify": {
                "type": "steps",
                "title": "Getting a garage door company approved to advertise",
                "sub": "Advanced verification for Google Ads, per Google’s help pages",
                "steps": [["Build a campaign", "New accounts create at least one campaign first."], ["Submit the form", "Customer ID, owner, address, phone, live website."], ["Show your licenses", "Any license your location requires."], ["Video call", "Be at the shop or near your branded truck."], ["Wait 6-8 weeks", "No ads on garage door searches until approved."]],
                "alt": "Steps for Google Ads advanced verification for a garage door company in Houston and The Woodlands",
                "caption": "Local Services Ads screening and Business Profile verification are separate. You need all three.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for garage door ads",
                "sub": "Add before launch",
                "items": ["DIY: how to, diy, yourself, youtube, video", "Parts: parts, spring kit, home depot, lowes, amazon", "Manuals: manual, wiring diagram, reset code, remote programming", "Jobs: jobs, hiring, technician salary, training", "Wrong door: car door, shower door, garage door paint", "Rentals: storage unit, apartment, landlord", "Brands you don’t service", "Commercial terms if you’re residential only"],
                "alt": "Checklist of negative keywords for garage door company Google Ads in Houston and Cypress",
                "caption": "Remote programming searches alone can eat a small budget. Watch the search terms report.",
            },
            "repair": {
                "type": "compare",
                "title": "Repair call vs. install job",
                "left": {"title": "Emergency repair", "items": ["Urgent, decides in minutes", "Searches near me, calls first result", "LSA and call-focused search", "Lower ticket, high volume", "Wins on speed and trust"]},
                "right": {"title": "New door install", "items": ["Plans over weeks", "Compares styles, photos and quotes", "Search, Meta and YouTube video", "Higher ticket and margin", "Often starts as a repair call"]},
                "alt": "Comparison of garage door repair and installation customers for garage door company marketing in Houston",
                "caption": "Run them as separate campaigns with separate pages. Use the repair visit to quote the install.",
            },
            "value": {
                "type": "stats",
                "title": "Garage door replacement value, 2025",
                "stats": [["$4,607", "average job cost, Houston"], ["$11,307", "estimated resale value, Houston"], ["~245%", "cost recouped, Houston"], ["268%", "cost recouped, national"]],
                "note": "Source: Cost vs. Value 2025 (JLC), Clopay summary",
                "alt": "Stats on garage door replacement cost and resale value in Houston from the 2025 Cost vs Value report",
                "caption": f"From {SRC['cvv']} and Clopay’s national summary. Estimates, not guarantees.",
            },
        },
    },
]
