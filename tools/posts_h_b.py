"""Batch 8 (agency intent): how marketing agencies charge (retainer vs percentage of ad spend vs pay-per-lead vs
performance vs project fees), and speed to lead (response times, follow-up cadence, after-hours handling, CRM fit).

Research: Lunio's 2021 PPC Agencies Pricing Survey (883 responses: 35% fixed retainer, 21% percentage of spend,
4% performance, most percentage agencies at 6-10%, retainers mostly $1,001-$4,000, 52% under $1,001), SE Ranking's
2023 Marketing and SEO Agency Pricing Models Survey (135 agencies; US/Canada median retainer $1,863, project $3,625,
hourly $112; 47.9% of US/Canada agencies retainer-only; performance used by 6% alongside other models), Google's
advertiser guide to working with third parties. Speed-to-lead post: the 2007 MIT/InsideSales Lead Response
Management study summary (Elkington and Oldroyd; 15,000+ leads, 100,000+ call attempts, 6 companies, 100x / 21x),
the March 2011 HBR article "The Short Life of Online Sales Leads" (Oldroyd, McElheran, Elkington; BYU record and
SmartCompany coverage for the 2,241-company audit, 37% within an hour, 42-hour average, 7x and 60x) with MediaPost
for the 23% never responded, Pied Piper's 2026 home services LHE study via Green Industry Pros (3,211 evaluations,
72% no follow-up in 24 hours), Jobber / Housecall Pro / HighLevel / HubSpot pricing pages, ServiceTitan demo page,
Twilio A2P 10DLC docs, K&L Gates and National Law Review on Texas SB 140, Pro Remodeler on the vacated FCC rule.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "lunio": A("https://www.lunio.ai/blog/ppc-agencies-pricing-survey", "Lunio’s 2021 PPC agency pricing survey"),
    "lunio2": A("https://www.lunio.ai/blog/ppc-agencies-pricing-survey", "the same Lunio survey"),
    "ser": A("https://knowledge.seranking.com/hubfs/Survey/2023-Marketing-and-SEO-Agency-Pricing-Models-Survey_c.pdf", "SE Ranking’s 2023 agency pricing survey"),
    "ser2": A("https://knowledge.seranking.com/hubfs/Survey/2023-Marketing-and-SEO-Agency-Pricing-Models-Survey_c.pdf", "SE Ranking’s survey"),
    "gguide": A("https://support.google.com/adspolicy/answer/9457109?hl=en", "Google’s guide for advertisers working with third parties"),
    "gguide2": A("https://support.google.com/adspolicy/answer/9457109?hl=en", "Google’s own advertiser guide"),
    # speed to lead
    "mit": A("https://www.mortech.com/hs-fs/hub/25649/file-13535879-pdf/docs/mit_study.pdf", "Lead Response Management Study"),
    "hbr": A("https://scholarsarchive.byu.edu/facpub/9711", "“The Short Life of Online Sales Leads”"),
    "smart": A("https://www.smartcompany.com.au/marketing/20110704-are-you-letting-online-leads-go-cold/", "SmartCompany’s write-up of the study"),
    "mediapost": A("https://www.mediapost.com/publications/article/147757/customer-leads-cant-wait-forever.html", "MediaPost"),
    "pied": A("https://www.greenindustrypros.com/business-management/marketing/press-release/22965698/pied-piper-management-co-llc-home-services-lead-failure-rate-hits-42-in-2026", "Pied Piper’s 2026 home services study"),
    "jobber": A("https://www.getjobber.com/pricing/", "Jobber’s pricing page"),
    "hcp": A("https://housecallpro.com/?p=388", "Housecall Pro’s pricing page"),
    "ghl": A("https://www.gohighlevel.com/pricing", "HighLevel’s pricing page"),
    "hubspot": A("https://www.hubspot.com/pricing/suite?tier=starter", "HubSpot’s pricing page"),
    "st": A("https://www.servicetitan.com/demo", "pricing comes through a demo"),
    "twilio": A("https://www.twilio.com/docs/messaging/compliance/a2p-10dlc", "Twilio’s A2P 10DLC documentation"),
    "klg": A("https://www.klgates.com/thought-leadership/Litigation-Minute-Text-Message-Marketing-in-Texas-One-Year-After-SB-140-9-14-2026", "K&amp;L Gates’ one-year review of SB 140"),
    "nlr": A("https://natlawreview.com/article/texas-sb-140-after-november-settlement-consent-cold-texting-out", "National Law Review"),
    "fcc": A("https://www.proremodeler.com/home/article/55263761/eleventh-circuit-vacates-fcc-one-to-one-consent-rule", "Pro Remodeler"),
}

PRICING = "/blog/marketing-agency-pricing-models-retainer-vs-percentage/"
SPEED = "/blog/speed-to-lead-response-time-follow-up-crm/"

POSTS = [
    # ------------------------------------------------------------------ post 1: agency pricing models
    {
        "slug": "marketing-agency-pricing-models-retainer-vs-percentage",
        "title": "Marketing Agency Pricing Models: Retainer vs % of Ad Spend vs Pay-Per-Lead",
        "seo_title": "Marketing Agency Pricing Models: Retainer vs % of Spend",
        "desc": "Marketing agency pricing models compared: retainer, % of ad spend, pay-per-lead, revenue share and project fees, with real math and contract red flags.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Analytics"],
        "art": "b4",
        "hero": "receipt",
        "hero_alt": "Illustration of an itemized receipt representing marketing agency pricing models for businesses in The Woodlands and Houston",
        "related": ["google-ads-management-houston-cost", "who-owns-google-ads-account-switch-agencies", "questions-before-hiring-marketing-agency"],
        "sections": [
            (None, f"""<p>Three proposals on the desk. One says 15% of ad spend. One says $2,500 a month, flat, six-month term. The third says no retainer at all, just $65 for every lead they send you.</p>
<p>They look impossible to compare, and that's partly by design.</p>
<p>Here's the direct answer. Marketing agencies charge in five main ways: a <b>monthly retainer</b> (a flat fee for ongoing work), a <b>percentage of ad spend</b> (usually somewhere between 6% and 20% of what you pay Google or Meta), <b>pay per lead</b>, <b>performance or revenue share</b>, and <b>project fees</b> for one-time work like a website or an account build. Most local businesses end up on a retainer or a percentage of spend. Which one is fair for you depends mostly on how much you spend on ads and how cleanly a lead can be counted in your business.</p>
<p>Below we walk through each of the marketing agency pricing models, the incentive each one creates (every model nudges the agency toward something), the math at small and large budgets, what's normally included versus billed extra, and the contract terms we'd push back on. We won't quote our own prices here. The goal is that you can read any proposal from any agency in The Woodlands or Houston and know what you're really buying.</p>"""),

            ("Marketing agency pricing models at a glance", f"""<p>Start with the whole menu. The ranges below come from two published surveys of agencies plus what we see in proposals that local owners forward to us, and we've labeled which is which.</p>
<div class="bp-tbl"><table><thead><tr><th>Model</th><th>How you're billed</th><th>Agency is rewarded for</th><th>Main risk to you</th><th>Usually fits</th></tr></thead><tbody>
<tr><td>Monthly retainer</td><td>Flat fee each month for a defined scope</td><td>Keeping you as a client</td><td>Paying the same for less effort over time</td><td>Most local businesses with steady budgets</td></tr>
<tr><td>Percentage of ad spend</td><td>Commonly 6% to 20% of media, often with a monthly minimum</td><td>Your budget going up</td><td>Advice to spend more instead of spend better</td><td>Larger or fast-scaling ad budgets</td></tr>
<tr><td>Pay per lead</td><td>A set price per form fill or call</td><td>Lead volume</td><td>Junk, duplicate or shared leads</td><td>Testing a new market or service line</td></tr>
<tr><td>Performance / revenue share</td><td>Percent of sales, or a base plus a bonus</td><td>Closed revenue (as they can measure it)</td><td>Attribution fights; high-ticket bias</td><td>Businesses with clean sales data in a CRM</td></tr>
<tr><td>Project fee</td><td>One price for a scoped deliverable</td><td>Finishing on scope</td><td>Change orders; nobody owns results after launch</td><td>Websites, account builds, branding</td></tr>
</tbody></table></div>
<p>How common is each? The best-sized dataset we found is {SRC['lunio']}, with 883 responses. It found 35% of agencies charge a fixed retainer regardless of spend, 21% charge a percentage of ad spend, and only 4% use performance-based pricing. Two caveats: the survey is from 2021, and a large share of respondents were in the UK, where rates run lower.</p>
<!--fig:survey-->
<p>A smaller, newer dataset is {SRC['ser']}. It polled only 135 agencies (the authors say that's too few for statistical significance), but it breaks out the US and Canada: a median monthly retainer of $1,863, a median project of $3,625 and a median hourly rate of $112. Nearly half of the US and Canadian agencies (47.9%) priced on a monthly retainer only.</p>"""),

            ("Is a marketing retainer worth it?", f"""<p>A retainer is a flat monthly fee for an agreed scope: say, managing Google Ads and Meta, a monthly report and a call, and up to a set number of ad creatives. You know exactly what you'll pay, and so does the agency. That predictability is the main reason it's the most common model.</p>
<p>The incentive problem is quiet. Once the fee is locked, the agency earns the most by keeping you happy with the least hours. In month two, someone is in your account every few days. By month fourteen, a junior account manager might log in on Thursday afternoons. Nothing in the price changes, so nothing forces the effort to stay up.</p>
<p>It's worth it when three things are true:</p>
<ul><li>The scope is written down in deliverables you can check (how often search terms are reviewed, how many new ads per month, what the report contains).</li>
<li>You can see the work. You own the ad accounts and can look at the change history whenever you want.</li>
<li>The fee is sensible relative to your media budget.</li></ul>
<p>That last one is where small budgets get hurt. A $1,500 flat fee on $3,000 of monthly ad spend means half again on top of every dollar you give Google. On $20,000 of spend, the same fee is 7.5%. Neither number is wrong by itself, but at small budgets you should ask whether the retainer covers more than the ads (SEO, your Business Profile, landing pages) or whether a lighter setup would do.</p>
<p>A rough rule we use: if the management fee is more than the ad budget, the plan is upside down unless there's a lot of non-ad work in it.</p>"""),

            ("Percentage of ad spend agency fees: the math at $3k vs $30k", f"""<p>Percentage pricing is simple to explain and scales automatically. Spend more, pay more. Lunio found most agencies on this model charge between 6% and 10% of spend, and you'll see 15% to 20% from agencies that work with smaller local accounts, usually with a monthly minimum attached.</p>
<p>Here is what a 15% fee does at two very different budgets:</p>
<!--fig:feemath-->
<div class="bp-tbl"><table><thead><tr><th>Monthly ad spend</th><th>15% fee</th><th>Flat $1,500 fee</th><th>Flat fee as % of spend</th></tr></thead><tbody>
<tr><td>$3,000</td><td>$450</td><td>$1,500</td><td>50%</td></tr>
<tr><td>$10,000</td><td>$1,500</td><td>$1,500</td><td>15%</td></tr>
<tr><td>$30,000</td><td>$4,500</td><td>$1,500</td><td>5%</td></tr>
</tbody></table></div>
<p>At $3,000, 15% is only $450 a month. Very few agencies will manage an account properly for that, which is why percentage contracts almost always carry a floor ("15% of spend or $1,000, whichever is greater"). Read the floor before you read the percentage. On a small budget, the floor is your real price.</p>
<p>At $30,000, the same 15% is $4,500 a month. A $30,000 account doesn't take ten times the work of a $3,000 account. It takes more, but not ten times. This is why bigger advertisers push for tiers (say 15% on the first $10,000, then 10%, then 7%) or a flat fee.</p>
<p>The conflict is obvious once you see it. If the agency's income rises when your budget rises, then "you should spend more" is always slightly self-serving advice. Sometimes it's correct. A Spring HVAC company that runs out of budget at 11 a.m. every weekday in July is leaving calls on the table. But you want the recommendation backed by numbers like impression share lost to budget and cost per booked job, not by a hunch.</p>
<p>Three questions to ask on any percentage deal:</p>
<ol><li>Is the fee calculated on actual spend or on the budget you approved? (Actual is fairer.)</li>
<li>Which platforms count? Google Ads, Meta, Local Services Ads, Microsoft? LSA in particular needs very little management, so 15% of it is a lot.</li>
<li>Is any of the media billed through the agency, with a markup on top of the fee? If they pay Google and invoice you, ask to see the Google invoice.</li></ol>"""),

            ("Pay per lead marketing agencies: what you're really buying", f"""<p>Pay per lead sounds like the agency finally has skin in the game. No leads, no bill. For some businesses it's genuinely fine. For most, the details decide if it's a good deal or a slow leak.</p>
<p>The detail that matters most is the definition of a lead. Is it any form fill? A call of any length? A call over 60 seconds? Does a second form from the same person count again? What about the caller who wanted a job, or the one selling SEO? If the contract says "a lead is a submitted form or a phone call," you will pay for spam and wrong numbers.</p>
<p>Next is ownership. Many pay-per-lead outfits run the ads in their own account, send traffic to their own landing page, and route calls through their own tracking number. That means when you stop paying, the phone number and the page and every bit of data walk away. Some sell the same lead to two or three companies in your area. (If you've used Angi or Thumbtack, you already know how that feels; we compared them in <a href="/blog/angi-vs-thumbtack-leads-worth-it-contractors/">Angi vs Thumbtack leads</a>.)</p>
<p>Then do the math against running it yourself. Say an agency charges $75 per lead and you buy 40 a month: $3,000. If your own Google Ads account produces leads at $50 including management, you're paying a $1,000-a-month premium for not owning the asset. If it produces them at $110, the per-lead deal is cheaper, at least until they raise the price.</p>
<p>Where we think pay per lead makes sense: testing a new service line or a new part of town before you commit, or a business that truly can't take on any fixed cost right now. Insist on exclusive leads, a written lead definition, a dispute window (credits for spam and duplicates within a set number of days), and recordings of the calls.</p>"""),

            ("Performance-based and revenue-share pricing", f"""<p>Paying a slice of revenue sounds like perfect alignment. In practice it's rare for local service businesses, and the surveys agree: 4% of the agencies in {SRC['lunio2']} priced on performance, and in {SRC['ser2']} only 6% used performance pricing, always alongside another model.</p>
<p>Why so rare? Because a revenue share only works if both sides trust the revenue number. The agency needs access to your CRM or invoicing, every lead has to be tagged by source, and you need an agreement on what counts. Is a repeat customer who first found you through an ad two years ago "theirs"? What about the homeowner who saw a Meta ad, then searched your name on Google, then called from your truck wrap? Each answer moves money.</p>
<p>There's also a selection bias. An agency paid on revenue will chase whatever closes biggest and fastest. If you're a remodeler, that might mean full kitchen jobs in Creekside Park while the bathroom refreshes that keep your crews busy get starved.</p>
<p>The version we see work is a hybrid: a smaller base retainer to cover the real labor, plus a bonus tied to a number you can both see without arguing, like booked appointments in your scheduling software or cost per booked job below a target. That keeps the agency motivated without turning every month into an audit.</p>"""),

            ("Project fees, setup fees and minimum terms", f"""<p>Project pricing covers work with a clear finish line: a website, a brand identity, a Google Ads account build, a landing page set. SE Ranking's US and Canada median of $3,625 per project is a reasonable midpoint for small jobs. Websites run far wider; we covered that in <a href="/blog/how-much-does-a-website-cost-the-woodlands/">what a website costs in The Woodlands</a>.</p>
<p>Setup fees are the hybrid between a project and a retainer. They're normal, and they're fair when the setup produces something you keep. A good setup fee should buy you:</p>
<ul><li>Conversion tracking installed and tested (calls, forms, bookings), with the right actions set as primary goals.</li>
<li>Call tracking numbers assigned to each channel.</li>
<li>Campaigns built from scratch or rebuilt, with negative keyword lists and location settings documented.</li>
<li>A written account map you could hand to the next agency.</li></ul>
<p>If a setup fee buys "onboarding" and nothing on that list, ask what it pays for.</p>
<p>Minimum terms are where owners feel trapped. Three months is reasonable for paid ads, because the first few weeks are spent learning and the algorithm needs data. Six months is common for SEO, which takes longer to show anything (see <a href="/blog/how-long-does-seo-take-houston-the-woodlands/">how long SEO takes</a>). Twelve months for a small local account is more than we'd sign. Whatever the term, look for what happens after it: month-to-month with 30 days' notice is the friendly version. An automatic renewal for another full term is the unfriendly one.</p>"""),

            ("What's normally included and what costs extra", f"""<p>Two proposals with the same monthly price can contain very different work. This is the table we'd use to line them up.</p>
<div class="bp-tbl"><table><thead><tr><th>Item</th><th>Usually included in management</th><th>Often billed extra</th><th>What to ask</th></tr></thead><tbody>
<tr><td>Ad spend</td><td>No, paid to Google or Meta</td><td>Sometimes marked up if billed through the agency</td><td>Is media billed straight to my card?</td></tr>
<tr><td>Campaign management</td><td>Yes</td><td>Extra platforms (Microsoft, TikTok, LSA)</td><td>Which platforms are in the fee?</td></tr>
<tr><td>Ad creative</td><td>Text ads, a few static images</td><td>Video, photo shoots, motion graphics</td><td>How many new creatives per month?</td></tr>
<tr><td>Landing pages</td><td>Small edits, sometimes one page</td><td>New page builds, A/B testing tools</td><td>Who owns the pages if we part ways?</td></tr>
<tr><td>Call tracking and software</td><td>Varies widely</td><td>Tracking numbers, reporting dashboards, SEO tools</td><td>Whose name are the tool accounts in?</td></tr>
<tr><td>Reporting</td><td>Monthly report</td><td>Custom dashboards, extra meetings</td><td>Does the report show leads and cost per lead?</td></tr>
<tr><td>SEO / Business Profile</td><td>Rarely, unless sold together</td><td>Monthly SEO retainer</td><td>Is any organic work in scope?</td></tr>
</tbody></table></div>
<p>Pay particular attention to the tools row. A call tracking account or reporting dashboard set up under the agency's name can be a hostage when you leave, because the phone numbers printed on your trucks and in your Google Business Profile belong to whoever owns that account. We wrote a whole piece on <a href="/blog/who-owns-google-ads-account-switch-agencies/">who owns your Google Ads account when you switch agencies</a>; the same thinking applies here.</p>
<p>For the bigger budget picture (what to spend on ads versus management versus SEO), see <a href="/blog/digital-marketing-cost-the-woodlands-houston/">what digital marketing costs in The Woodlands and Houston</a> and, for Google Ads specifically, <a href="/blog/google-ads-management-houston-cost/">Google Ads management cost in Houston</a>.</p>"""),

            ("Contract red flags we'd push back on", f"""<p>Most agency contracts are fine. A few clauses show up often enough that we'd read for them specifically.</p>
<!--fig:redflags-->
<p>Some of these aren't just our opinion. {SRC['gguide']} says that, at a minimum, you have the right to know the clicks, impressions and total cost of your Google ads, that a partner must set up a separate Ads account for you, and that nobody can guarantee a specific ad position on Google. It also tells advertisers to understand the total cost of advertising including the partner's fees, and to get the agreement in writing.</p>
<p>Two more that aren't on Google's list. Watch for termination fees that equal the remaining months of the term, and for language that makes the agency's ad copy, landing pages or audiences their "intellectual property." You paid for them. You should be able to keep them.</p>
<p>And one soft red flag: a proposal that leads with the price and buries the scope. If you can't tell what someone will do each week, you can't tell whether the price is fair.</p>"""),

            ("Which pricing model fits you? A quick decision tool", f"""<p>Use this in order. Stop at the first step that clearly applies.</p>
<!--fig:decide-->
<div class="bp-tbl"><table><thead><tr><th>Your situation</th><th>Model we'd lean toward</th><th>Why</th></tr></thead><tbody>
<tr><td>Under about $3,000/month in ads, one location</td><td>Flat retainer with a narrow scope, or DIY with a periodic audit</td><td>Percentage minimums eat small budgets</td></tr>
<tr><td>$5,000 to $20,000/month, steady</td><td>Flat retainer or tiered percentage</td><td>Predictable; fee stays a sane share of spend</td></tr>
<tr><td>$20,000+/month or scaling fast</td><td>Tiered percentage or flat fee with a review every six months</td><td>Straight percentage overpays at the top end</td></tr>
<tr><td>Testing a new service or area</td><td>Pay per lead with exclusive leads, short term</td><td>Low commitment while you learn</td></tr>
<tr><td>Clean CRM data, clear revenue per job</td><td>Base retainer plus a performance bonus</td><td>Alignment without monthly arguments</td></tr>
<tr><td>Need a website or account rebuild first</td><td>Project fee, then decide on ongoing work</td><td>Separates the build from the results</td></tr>
</tbody></table></div>
<p>Whatever model you choose, the questions in <a href="/blog/questions-before-hiring-marketing-agency/">our list of questions before hiring a marketing agency</a> still apply. And if you're unsure whether you need an agency at all, <a href="/blog/diy-vs-hiring-an-agency/">DIY vs hiring an agency</a> lays out the trade.</p>
<p>A practical next step: pull your last three agency invoices and your last three months of spend from Google Ads and Meta. Add them up. Divide the total by the number of booked jobs (not leads) in your scheduling software. That cost per booked job is the number every pricing model should be judged against.</p>
<p>If you'd like an outside read first, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video of your Google or Meta account showing where budget is leaking, in your inbox within 48 hours, so you can judge what any agency (including us) would actually be fixing. You can also see how we run <a href="/services/search-marketing/">Google Ads management</a>.</p>"""),
        ],
        "faq": [
            ("What percentage of ad spend do marketing agencies charge?",
             "Most agencies that price this way charge somewhere between 6% and 20% of monthly ad spend. Lunio's 2021 survey of PPC agencies found 6% to 10% was most common, while agencies serving smaller local accounts often charge 15% to 20% with a monthly minimum. On small budgets, the minimum is usually the real price, so read it first."),
            ("Is a marketing retainer worth it for a small business?",
             "It can be, if the scope is written as checkable deliverables, you own the ad accounts and can see the work, and the fee is reasonable next to your ad budget. A retainer larger than your monthly ad spend only makes sense if it also covers non-ad work such as SEO, your Google Business Profile or landing pages."),
            ("Is pay per lead better than a monthly retainer?",
             "Only if the lead definition is tight and the leads are exclusive to you. Pay per lead shifts risk to the agency, but many providers keep the ad account, landing page and tracking number, so you own nothing when you stop. Compare the price per lead with what your own account produces, including management, before choosing it."),
            ("What is a normal minimum contract length for a marketing agency?",
             "Three months is common and reasonable for paid ads, since campaigns need a few weeks of data. Six months is typical for SEO. We'd be cautious about twelve-month terms for a small local account, and about auto-renewal for another full term. Month-to-month with 30 days' notice after the first term is the friendliest version."),
            ("Should an agency charge a setup fee?",
             "A setup fee is normal when it buys something you keep: tested conversion tracking, call tracking by channel, rebuilt campaigns with documented settings, and an account map. If the fee only covers onboarding meetings, ask what it pays for. Either way, the accounts and tracking set up with that fee should be in your name."),
        ],
        "figures": {
            "survey": {
                "type": "stats",
                "title": "How PPC agencies priced their work",
                "stats": [["35%", "charged a fixed retainer regardless of spend"], ["21%", "charged a percentage of ad spend"], ["6-10%", "most common percentage-of-spend fee"], ["4%", "used performance-based pricing"]],
                "note": "Source: Lunio PPC Agencies Pricing Survey 2021 (883 responses)",
                "alt": "Survey stats on marketing agency pricing models: retainers, percentage of ad spend and performance fees, for Houston owners",
                "caption": f"From {SRC['lunio']}; many respondents were UK agencies, so US rates tend to run higher.",
            },
            "feemath": {
                "type": "bars",
                "title": "Monthly management fee at two budgets",
                "sub": "15% of spend vs a flat $1,500 retainer",
                "items": [["15% of $3,000 spend", 450, "$450"], ["Flat fee, $3,000 spend", 1500, "$1,500"], ["Flat fee, $30,000 spend", 1500, "$1,500"], ["15% of $30,000 spend", 4500, "$4,500"]],
                "highlight": [3],
                "note": "Illustrative example",
                "alt": "Bar chart comparing a percentage of ad spend agency fee and a flat retainer at $3,000 and $30,000 for Houston businesses",
                "caption": "The same percentage is cheap at small budgets and expensive at large ones, which is why floors and tiers exist.",
            },
            "redflags": {
                "type": "checklist",
                "title": "Agency contract red flags",
                "sub": "Read for these before you sign",
                "items": ["Ad accounts created under the agency's name", "No access to change history or search terms", "Media billed through the agency with no invoice", "Vague lead definition on pay-per-lead deals", "Auto-renews for another full term", "Termination fee equal to remaining months", "Agency claims ownership of ads and pages", "Guaranteed top position on Google"],
                "alt": "Checklist of marketing agency contract red flags for business owners in The Woodlands and Houston comparing pricing models",
                "caption": f"The last item is one {SRC['gguide2']} says no partner can promise.",
            },
            "decide": {
                "type": "steps",
                "title": "Which agency pricing model fits you",
                "sub": "Stop at the first step that clearly applies",
                "steps": [["Check your monthly ad spend", "Under about $3,000, avoid percentage deals with high minimums."], ["Check your data", "If revenue per job is clean in a CRM, a base plus bonus can work."], ["Check your goal", "Testing a new area or service? Short pay-per-lead with exclusive leads."], ["Check what's broken", "No tracking or a dated site? Pay a project fee first."], ["Default", "Flat retainer with written deliverables and accounts in your name."]],
                "alt": "Decision steps for choosing between marketing agency pricing models for a Houston or The Woodlands small business",
                "caption": "A starting point, not a rule; your cost per booked job is the final judge.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: speed to lead
    {
        "slug": "speed-to-lead-response-time-follow-up-crm",
        "title": "Speed to Lead: How Fast to Respond, and the Follow-Up System That Works",
        "seo_title": "Speed to Lead: Response Times, Follow-Up & CRM Setup",
        "desc": "Speed to lead for service businesses: how fast to answer web leads and missed calls, a day-by-day follow-up cadence, and honest CRM picks for Houston teams.",
        "category": "Strategy",
        "icons": ["HubSpot", "Google Ads", "Google Business Profile"],
        "art": "b5",
        "hero": "bolt",
        "hero_alt": "Illustration of a lightning bolt and stopwatch for speed to lead and fast follow-up at Houston service businesses",
        "related": ["call-tracking-which-ads-make-phone-ring", "google-ads-not-converting-clicks-no-calls", "turn-your-website-into-a-lead-machine"],
        "sections": [
            (None, f"""<p>2:40 on a Tuesday. A homeowner in Kingwood fills out your website form: water heater leaking, can someone come today. You see it at 6:15, after your last job, and call back. She's polite about it. Someone else is already there.</p>
<p>That's what speed to lead means in a service business. It's the time between a customer reaching out and a human from your company actually talking to them.</p>
<p>How fast should it be? During business hours, aim to call a web lead back within five minutes, and answer phone calls live or return a missed call within five minutes with a text going out in the first minute. After hours, send an instant text or email acknowledgment and have a person call at opening, or use an answering service if your work is urgent. Then keep following up for about two weeks, because plenty of people don't pick up the first time.</p>
<p>The rest of this guide covers what the research actually says (it's older than most people quoting it admit), the math for a typical Houston-area service company, after-hours handling that stays on the right side of Texas texting rules, a follow-up cadence you can copy, and which CRM fits which kind of shop.</p>"""),

            ("What the speed to lead research actually found (and how old it is)", f"""<p>Almost every "respond in five minutes" claim online traces back to two studies. Both are real. Both are old.</p>
<p>The first is the {SRC['mit']}, presented in 2007 by Dave Elkington of InsideSales.com and James Oldroyd, then at MIT. It used three years of data from six companies, more than 15,000 leads and more than 100,000 call attempts. The summary reports that the odds of contacting a lead drop 100 times when you call at 30 minutes instead of 5, and the odds of qualifying the lead drop 21 times. The study summary doesn't explain how those multiples were calculated, and each company defined "qualified" its own way. Treat the exact multipliers loosely. The direction is not in doubt.</p>
<p>The second is {SRC['hbr']}, published in Harvard Business Review in March 2011 by Oldroyd, Kristina McElheran and Elkington. According to {SRC['smart']}, the authors audited 2,241 US companies by submitting web leads: only 37% responded within an hour, and the average response time among those that answered within 30 days was 42 hours. {SRC['mediapost']} reported that 23% never responded at all. In a separate dataset of 1.25 million leads, firms that contacted a lead within an hour were nearly seven times as likely to qualify it as firms that waited an hour longer, and more than 60 times as likely as firms that waited a day or more.</p>
<!--fig:studies-->
<p>Neither study was about plumbers or roofers. Both mixed B2B and consumer sales, and both predate texting as a normal way to reach a business. So is any of it current? The closest recent evidence for home services is {SRC['pied']}, which made 3,211 mystery-shop inquiries to locations of 31 large home services brands between October 2025 and January 2026. Follow-up was tracked for 24 hours across phone, text and email. 72% of the time there was no follow-up at all. Appointments were offered only 28% of the time when it would have been appropriate.</p>
<p>That's the opportunity in one number. You don't have to beat a five-minute benchmark from 2007. You have to beat competitors who, most of the time, never call back.</p>"""),

            ("How fast should you respond to leads? Targets by channel", f"""<p>Leads don't all arrive the same way, and they don't all deserve the same clock. These are the targets we set with service businesses around The Woodlands and Houston:</p>
<div class="bp-tbl"><table><thead><tr><th>Lead source</th><th>First touch</th><th>Human contact</th><th>Notes</th></tr></thead><tbody>
<tr><td>Inbound phone call</td><td>Answered live</td><td>Immediately</td><td>Anything else is a missed lead; measure the rate</td></tr>
<tr><td>Missed call (business hours)</td><td>Auto-text within 1 minute</td><td>Call back within 5 minutes</td><td>Most missed callers dial the next company</td></tr>
<tr><td>Website form</td><td>Auto-text and email instantly</td><td>Call within 5 minutes</td><td>Call first; text if no answer</td></tr>
<tr><td>Local Services Ads message or lead</td><td>Reply within minutes</td><td>Call if a number is given</td><td>Treat it like a form fill, not an email</td></tr>
<tr><td>Facebook / Instagram lead form</td><td>Auto-text instantly</td><td>Call within 5 to 15 minutes</td><td>Lower intent; people forget they submitted</td></tr>
<tr><td>After hours (any channel)</td><td>Auto-text or answering service</td><td>First thing next morning, before 8:30</td><td>Urgent trades need a live after-hours option</td></tr>
</tbody></table></div>
<p>Five minutes is a target, not a law of physics. A two-person pool service with both owners on a job site in Magnolia can't hit it every time, and we'd rather you hit 15 minutes on 95% of leads than 5 minutes on half of them. Consistency beats the occasional sprint.</p>
<p>One opinion: call first. A text is a great backup and a good first touch after hours, but a phone call during business hours books more jobs because you can answer questions and offer a time on the spot. Texting back-and-forth about availability often takes an hour to settle what a 90-second call settles.</p>"""),

            ("The response-time math for a local service business", f"""<p>Let's put dollars on it with a hypothetical. Say you run a three-truck HVAC company in Spring. You buy 60 leads a month from Google Ads and Meta at an average of $80 each, so $4,800 in lead cost. Your average ticket on a booked job is $600.</p>
<p>Now compare two versions of the same month. In one, leads get a call within five minutes and 45% of them book. In the other, leads get called back after the last job of the day and 25% book. (Those booking rates are illustrative. Use your own from your CRM or scheduling software.)</p>
<!--fig:math-->
<p>Same ad spend, same leads. The fast version books 27 jobs and $16,200 in revenue. The slow version books 15 jobs and $9,000. The difference, $7,200 a month, is larger than the entire ad budget. Put another way, your effective cost per booked job drops from $320 to about $178 without changing a single campaign setting.</p>
<p>This is why we look at follow-up before we touch bids. When an owner tells us "Google Ads doesn't work," the leads are often fine and the phone is the problem. Our <a href="/blog/google-ads-not-converting-clicks-no-calls/">Google Ads not converting audit</a> walks through that diagnosis step by step.</p>"""),

            ("Missed calls and after-hours leads", f"""<p>The cheapest fix in this whole guide is a missed-call text back. When a call to your business number isn't answered, your phone system sends a text within a minute: "Sorry we missed you, this is Mike at [your company]. Are you calling about a repair or a new system? We'll call you right back." It buys you five minutes and tells the caller a real company exists.</p>
<p>For after-hours leads, you have three options, and the right one depends on how urgent your work is:</p>
<ul><li><b>Auto-acknowledgment plus a morning call.</b> Fine for remodelers, landscapers, pool builders and anyone whose customers aren't standing in water.</li>
<li><b>A live answering service.</b> People answer with your script, take details and either book into your calendar or page the on-call tech. Most charge per call or per minute, so get quotes and ask for call recordings.</li>
<li><b>An AI receptionist.</b> Several field-service tools now sell one. {SRC['jobber']} lists its AI Receptionist as a $29-a-month add-on on most plans, and Housecall Pro sells a separate CSR AI product. Test it hard before trusting it with a Friday night in August: in the Pied Piper study, about 1 in 10 shoppers hit an AI, and 73% of those conversations needed a human to finish.</li></ul>
<!--fig:afterhours-->
<p><b>Texting rules, briefly (we're marketers, not lawyers).</b> Replying by text to someone who just called or filled out a form asking you to contact them is a very different thing from blasting promotions. Marketing texts need prior consent under the federal TCPA. In early 2025 a federal appeals court struck down the FCC's stricter "one-to-one" consent rule before it took effect, as {SRC['fcc']} reported, but the underlying consent rules still apply. Texas added its own layer: SB 140 took effect September 1, 2025 and brought text messages into the state's telephone solicitation law. After a November 2025 dismissal of the industry challenge, the State's position is that genuinely consent-based texting is exempt from the registration and bond requirements, while cold texting is not. {SRC['klg']} notes that this position isn't binding on courts, and {SRC['nlr']} has a plain-language summary. Our take: put a consent checkbox on your forms, keep records of it, honor STOP replies, and don't text purchased lists.</p>
<p>Separately, if your texting tool sends from a regular local number, it has to be registered for A2P 10DLC. {SRC['twilio']} says anyone sending application-to-person texts over a 10DLC number to the US must register, and unregistered traffic gets extra carrier fees and heavier filtering. Most CRMs walk you through it. Do it before you turn on automation, or your texts quietly won't arrive.</p>"""),

            ("A lead follow-up process you can copy", f"""<p>Speed gets you the first conversation. Persistence gets you the people who were in a meeting, at the pool or driving down I-45 when you called. This is the cadence we'd start with for a home service lead that hasn't booked yet:</p>
<div class="bp-tbl"><table><thead><tr><th>When</th><th>Call</th><th>Text</th><th>Email</th></tr></thead><tbody>
<tr><td>Minute 0-1</td><td></td><td>Auto: "Got it, calling you in a few minutes"</td><td>Auto confirmation with your photo and license number</td></tr>
<tr><td>Minute 2-5</td><td>Call 1; leave a short voicemail</td><td>If no answer: "Just tried you, when's a good time?"</td><td></td></tr>
<tr><td>Hour 1</td><td>Call 2</td><td></td><td></td></tr>
<tr><td>Day 1 (next morning)</td><td>Call 3</td><td>Offer two specific time slots</td><td>Short note with reviews and what to expect</td></tr>
<tr><td>Day 2</td><td>Call 4 at a different time of day</td><td></td><td></td></tr>
<tr><td>Day 4</td><td></td><td>"Still need help with the AC?"</td><td>One helpful tip or price range</td></tr>
<tr><td>Day 7</td><td>Call 5</td><td></td><td>"Should I close this out?" email</td></tr>
<tr><td>Day 14</td><td></td><td>Final check-in text</td><td></td></tr>
<tr><td>Day 30+</td><td colspan="3">Move to a monthly or seasonal email list (with consent), not more calls</td></tr>
</tbody></table></div>
<p>Stop the sequence the moment someone books, says no, or replies STOP. Nothing annoys a customer like a "still interested?" text the day after the job is done, which is why this needs to live in software rather than someone's memory.</p>
<p>Quotes need their own track. A homeowner with a $14,000 remodel estimate isn't ignoring you; they're comparing. A call two days after the quote, a short text a week later, and an email with photos of a similar job usually does more than any discount.</p>
<p>Write the scripts down. Your office manager shouldn't have to invent the Day 4 text every time. We'd keep each one under 160 characters, name the person sending it, and end with a question.</p>"""),

            ("Best CRM for a service business: honest fit notes", f"""<p>You don't need a CRM to start. You need every lead in one place with a timestamp and an owner. That said, once you have more than a handful of leads a day, a spreadsheet stops working. Prices below come from each vendor's pricing page as of November 2026 and do change.</p>
<div class="bp-tbl"><table><thead><tr><th>Tool</th><th>Published price</th><th>Best fit</th><th>Watch out for</th></tr></thead><tbody>
<tr><td>Jobber</td><td>From $29/mo billed annually (Core, 1 user); Grow from $149/mo annually</td><td>Small home service teams that want quoting, scheduling and invoicing in one app</td><td>Two-way texting is on Grow and Plus; automated quote follow-ups start on Connect</td></tr>
<tr><td>Housecall Pro</td><td>Basic $59/mo annually ($79 monthly), Essentials $149, Max $299</td><td>HVAC, plumbing, electrical and cleaning shops of 1 to 8 users</td><td>Extra users on Max cost $35/mo each; CSR AI is a separate product</td></tr>
<tr><td>ServiceTitan</td><td>Not published; {SRC['st']}</td><td>Larger trades businesses with call centers, dispatchers and multiple crews</td><td>Heavy to implement; overkill for most shops under about ten techs</td></tr>
<tr><td>HubSpot</td><td>Free tools for up to 2 users; Starter listed per seat; Professional from $1,300/mo</td><td>Businesses with longer sales cycles: remodelers, B2B, med spas</td><td>No scheduling or dispatch; you'll still need field-service software</td></tr>
<tr><td>GoHighLevel</td><td>$97/mo Starter, $297/mo Unlimited, plus usage for texts and calls</td><td>Marketing automation: missed-call text back, sequences, pipelines</td><td>Built for agencies; setup quality varies a lot, and it's not a field-service tool</td></tr>
</tbody></table></div>
<p>Sources: {SRC['jobber']}, {SRC['hcp']}, {SRC['hubspot']}, {SRC['ghl']}.</p>
<p>Our honest read: if you're a trade business under ten trucks, start with the field-service tool you'll actually use every day (Jobber or Housecall Pro), turn on its automated follow-ups, and only add a separate marketing CRM if the built-in follow-ups can't do what the cadence table above needs. Two systems that don't talk to each other will double-book follow-ups, which is worse than none.</p>
<p>If you sell bigger tickets with longer decision times (a $60,000 pool, a whole-home remodel), a sales-pipeline CRM like HubSpot earns its keep, because the follow-up happens over weeks, not hours.</p>"""),

            ("How to measure speed to lead (and set it up in a week)", f"""<p>What you don't measure drifts. Here's a setup you can finish in about a week:</p>
<ol><li><b>Route every lead into one place.</b> Website forms, Facebook lead forms, chat and LSA leads all land in the CRM or one shared inbox, not three people's phones.</li>
<li><b>Track the calls.</b> Give each ad channel its own tracking number so you can see answered versus missed calls by source. We cover how in <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking: which ads make the phone ring</a>. If you run Google Ads, the call details report shows each ad call and whether it was missed.</li>
<li><b>Turn on instant notifications</b> to whoever is on lead duty that day, by text, not just email.</li>
<li><b>Set up the missed-call text back and the form auto-reply</b>, after 10DLC registration.</li>
<li><b>Load the cadence</b> as an automated sequence that stops when a job is booked.</li>
<li><b>Mystery shop yourself.</b> Have a friend fill out your form at 2 p.m. on a Wednesday and call at 5:45 p.m. on a Friday. Time both.</li></ol>
<p>Then watch these numbers every week:</p>
<!--fig:scorecard-->
<p>Use the median response time, not the average. One lead that sat over a holiday weekend will wreck an average and hide the fact that the other 49 got called in four minutes.</p>
<p>Your website plays a part, too. A form that asks for eleven fields slows down the lead before your clock even starts; see <a href="/blog/turn-your-website-into-a-lead-machine/">turn your website into a lead machine</a> for the form and call-button fixes.</p>
<p>A good first move this week: look at your last 20 web leads and write down when each came in and when someone first spoke to that person. If the median is over an hour, fixing that is worth more than any new campaign. If you'd like us to check the ad side at the same time, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video of your Google or Meta account, in your inbox within 48 hours, and we'll flag missed ad calls if they show up in the data. It's part of how we approach <a href="/industries/service/">marketing for home service companies</a>.</p>"""),
        ],
        "faq": [
            ("How fast should you respond to a lead?",
             "During business hours, call web leads back within five minutes and return missed calls within five minutes, with an automatic text going out in the first minute. After hours, send an instant acknowledgment and call first thing the next morning, or use an answering service if your work is urgent. Consistency matters more than an occasional fast response."),
            ("What is speed to lead?",
             "Speed to lead is the time between a potential customer contacting your business, by form, call, text or chat, and a real person from your company reaching them. It is usually measured in minutes. Track the median across all leads each week, since a single slow lead can distort an average."),
            ("Is the five-minute lead response rule still true?",
             "The five-minute figure comes from a 2007 MIT and InsideSales study, and a 2011 Harvard Business Review article found similar urgency within the first hour. Both are old and not specific to home services. But a 2026 mystery-shop study of large home services brands found no follow-up 72% of the time, so being fast still sets you apart."),
            ("What is the best CRM for a small service business?",
             "For trade businesses under about ten trucks, a field-service tool like Jobber or Housecall Pro usually fits best because quoting, scheduling and follow-up live in one app. ServiceTitan suits larger operations with dispatchers. HubSpot fits longer sales cycles, and GoHighLevel is strong for automated follow-up but is not a scheduling or dispatch tool."),
            ("Can I automatically text people who call my business and I miss?",
             "Generally, replying to someone who just called you is treated differently from marketing texts, but you should still follow consent rules, honor STOP replies and register your number for A2P 10DLC. Texas SB 140 brought texts into the state's telephone solicitation law in 2025, so keep consent records and avoid texting purchased lists. Ask a lawyer about your specific setup."),
        ],
        "figures": {
            "studies": {
                "type": "stats",
                "title": "What lead response studies found",
                "stats": [["37%", "of 2,241 US companies replied to a web lead within an hour (HBR, 2011)"], ["42h", "average response time among companies that replied"], ["72%", "of 2026 home services inquiries got no follow-up within 24 hours"]],
                "note": "Source: Oldroyd, McElheran and Elkington, HBR 2011; Pied Piper 2026",
                "alt": "Speed to lead statistics on how slowly companies respond to web leads, relevant for Houston service businesses",
                "caption": f"The 2026 figure is from {SRC['pied']}, based on 3,211 mystery-shop inquiries.",
            },
            "math": {
                "type": "bars",
                "title": "Same 60 leads, two response speeds",
                "sub": "$80 per lead, $600 average job",
                "items": [["Called within 5 min (45% book)", 16200, "$16,200"], ["Called end of day (25% book)", 9000, "$9,000"], ["Monthly lead cost", 4800, "$4,800"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart showing revenue from fast versus slow lead response for a Spring, TX HVAC company buying 60 leads",
                "caption": "Swap in your own booking rates and average ticket from your scheduling software.",
            },
            "afterhours": {
                "type": "compare",
                "title": "A missed call at 6:40 p.m.",
                "left": {"title": "Goes to voicemail", "items": ["Caller hangs up without a message", "They call the next company on Google", "You see a missed number at 8 a.m.", "No record of what they needed"]},
                "right": {"title": "Gets a text back in 60 seconds", "items": ["Caller knows a real person will respond", "They reply with the problem and address", "On-call tech or morning call is lined up", "Lead is logged in the CRM with a timestamp"]},
                "alt": "Comparison of a missed call going to voicemail versus an instant text back for after-hours leads in The Woodlands and Houston",
                "caption": "A missed-call text back is usually the cheapest speed-to-lead fix, once your number is registered.",
            },
            "scorecard": {
                "type": "checklist",
                "title": "Weekly speed-to-lead scorecard",
                "sub": "Pull these from your CRM and call tracking",
                "items": ["Median minutes to first human contact", "Share of leads contacted within 15 minutes", "Missed-call rate during business hours", "Missed calls returned within 5 minutes", "Contact rate (leads you actually spoke with)", "Booked rate by lead source", "Leads with no follow-up logged", "Quotes followed up within 48 hours"],
                "alt": "Weekly scorecard checklist for measuring speed to lead and follow-up at a Houston-area home service business",
                "caption": "Eight numbers, ten minutes on a Monday morning.",
            },
        },
    },
]
