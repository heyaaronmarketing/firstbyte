"""Batch 13 (module c): two agency-relationship posts for Houston-area business owners.

1. Marketing agency contract red flags: what to check before you sign.
2. Signs your marketing agency isn't working, and what to do about it.

Research: Google Search Central "Do you need an SEO?" (no one can guarantee a #1 ranking; warnings about guaranteed
rankings, "priority submit" and "special relationship" claims; questions to ask an SEO); Google Ads advertiser guide
to working with third parties (right to know clicks, impressions and total cost; no one can guarantee an ad position;
red flags list; get the agreement in writing); Google third-party policy (separate account per end-advertiser,
honesty about costs and expected results); Google Ads access levels (Admin vs. Standard vs. Read only vs. Billing);
Google Ads unlinking rules (accounts on monthly invoicing stop serving when unlinked from the paying manager; history
stays with the account); U.S. Copyright Office Circular 30 (nine categories of commissioned works that can be works
made for hire, signed written agreement required); 17 U.S.C. 204(a) (transfers of copyright need a signed writing);
Texas Supreme Court, Marsh USA v. Cook (2011) on Tex. Bus. & Com. Code 15.50 (non-solicitation covenants are
restraints governed by the Act; time, area and scope must be reasonable).
Post 2: Google Ads change history (two years of data, user column, filters); search terms report path (Campaigns >
Insights and reports > Search terms; low-volume terms omitted); auto-apply recommendations (History tab, change
history); Experiments page and experiment types; phone call conversion types (clicks on a number count clicks, not
calls; advertiser sets minimum call length); GA4 key events (Admin > Data display > Events; 30 key events on standard
properties; renamed from conversions, announced March 22, 2024 per Search Engine Roundtable).
Not used: Texas auto-renewal rules for business-to-business contracts (could not verify a general statute), any
agency churn statistic (no reliable source), and Meta partner-access specifics (covered in the ownership post).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # shared
    "g3p": A("https://support.google.com/adspolicy/answer/9457109?hl=en", "Google’s advertiser guide to working with third parties"),
    "access": A("https://support.google.com/google-ads/answer/9978556?hl=en", "Google’s access level page"),
    # contract post
    "seo": A("https://developers.google.com/search/docs/beginner/do-i-need-seo", "Google’s own “Do you need an SEO?” guidance"),
    "pol3p": A("https://support.google.com/adspolicy/answer/6086450", "Google’s third-party policy"),
    "unlink": A("https://support.google.com/google-ads/answer/7458428?hl=en", "Google’s unlinking rules"),
    "circ30": A("https://www.copyright.gov/circs/circ30.pdf", "U.S. Copyright Office Circular 30"),
    "s204": A("https://www.govinfo.gov/content/pkg/USCODE-2023-title17/html/USCODE-2023-title17-chap2-sec204.htm", "17 U.S.C. § 204(a)"),
    "marsh": A("https://law.justia.com/cases/texas/supreme-court/2011/2001724.html", "Marsh USA v. Cook"),
    # signs post
    "hist": A("https://support.google.com/google-ads/answer/19888", "Google’s change history page"),
    "terms": A("https://support.google.com/google-ads/answer/2472708", "Google’s search terms report documentation"),
    "auto": A("https://support.google.com/google-ads/answer/10279006", "Google’s page on auto-applied recommendations"),
    "exp": A("https://support.google.com/google-ads/answer/10682377", "Google’s Experiments page documentation"),
    "calls": A("https://support.google.com/google-ads/answer/6100664?hl=en", "Google’s phone call conversion guide"),
    "keyev": A("https://support.google.com/analytics/answer/13128484", "Google’s key events help page"),
    "keydef": A("https://support.google.com/analytics/answer/13965727?hl=en", "Google’s events and key events page"),
    "rename": A("https://www.seroundtable.com/google-analytics-ads-conversion-metrics-37096.html", "Search Engine Roundtable"),
}

CONTRACT = "/blog/marketing-agency-contract-red-flags/"
SIGNS = "/blog/signs-your-marketing-agency-isnt-working/"
OWN = "/blog/who-owns-google-ads-account-switch-agencies/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: contract red flags
    {
        "slug": "marketing-agency-contract-red-flags",
        "title": "Marketing Agency Contract Red Flags: What to Check Before You Sign",
        "seo_title": "Marketing Agency Contract Red Flags to Check Before Signing",
        "desc": "Agency contract red flags: auto-renewal, termination, who owns accounts and creative, ad spend markups, guarantees and non-solicits. Not legal advice.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google", "Google Analytics"],
        "art": "b2",
        "hero": "receipt",
        "hero_alt": "Illustration of a signed document for marketing agency contract red flags for businesses in Houston and The Woodlands",
        "related": ["who-owns-google-ads-account-switch-agencies", "marketing-agency-pricing-models-retainer-vs-percentage", "questions-before-hiring-marketing-agency"],
        "sections": [
            (None, f"""<p>Thursday afternoon, a dental office in Spring. The proposal looked great in the meeting: a clean deck, a friendly account lead, a promise to “own page one.” Now the practice manager has a 14-page PDF on her screen and a DocuSign deadline of Friday at 5. She skims it. Twelve months. Something about a “platform fee.” Section 9 says the agency keeps “all work product.” She’s not sure whether that’s normal.</p>
<p>It might be. Most agency contracts are written by people who have been burned by clients that didn’t pay, so they protect the agency. That isn’t sinister. But a few clauses decide whether you can leave cleanly in a year, and those are worth twenty minutes before you sign.</p>
<p>The short version: before you sign a marketing agency contract, check the term and renewal, how much notice you owe to cancel, who owns the ad accounts, data, creative and website, whether ad spend is billed straight to you or marked up, what the setup fee actually buys, what’s promised as a result, what reports you’re owed, and whether a non-solicit clause stops you from hiring someone later.</p>
<p>We’re a marketing agency in The Woodlands, and we sign these from the other side every month. This is how we’d read one if we were the client. It isn’t legal advice. For anything large or unusual, a Texas business attorney is worth the hour.</p>"""),

            ("Read it in this order", f"""<p>Agency contracts usually have a short statement of work up front and a long block of standard terms at the back. The standard terms are where the trouble hides, because nobody reads them in the meeting.</p>
<!--fig:order-->
<p>We read in this order: term and renewal, termination, ownership, money (fees, markups, setup), promises, reporting, then the restrictive clauses (non-solicit, exclusivity, confidentiality). If the first three are clean, the rest is usually fine. If ownership is murky, nothing else in the contract really matters, because you’re renting your own marketing.</p>
<p>Before any of that, check that the statement of work names the actual deliverables. “Digital marketing services” is not a scope. “Management of Google Search campaigns, up to $8,000 monthly spend, two new ad variations per month, monthly report and call” is a scope. If the scope is vague, every disagreement later turns into “that wasn’t included.” Our {L('/blog/questions-before-hiring-marketing-agency/', 'questions to ask before hiring an agency')} cover the sales conversation; this post is about the paper.</p>"""),

            ("Term length and auto-renewal", f"""<p>Minimum terms are normal. Paid search needs a few weeks to gather data, and SEO takes months before it shows anything (we wrote about that in {L('/blog/how-long-does-seo-take-houston-the-woodlands/', 'how long SEO takes')}). An agency that commits people and setup time to your account wants some assurance you won’t walk after week three.</p>
<p>What we consider reasonable for a small or mid-size Houston business, from the contracts we see:</p>
<ul>
<li><b>Paid ads:</b> three months, then month-to-month.</li>
<li><b>SEO:</b> six months, then month-to-month.</li>
<li><b>Website build:</b> a project contract tied to milestones, with no ongoing term unless you choose hosting or maintenance.</li>
</ul>
<p>The real flag is automatic renewal for another full term. A 12-month contract that renews for another 12 months unless you cancel in a 30-day window, 60 days before the anniversary, is built to be missed. Owners don’t put that date on a calendar, and the renewal letter (if there is one) gets lost in a shared inbox.</p>
<p>Ask for it to roll to month-to-month after the first term. Most agencies will agree, because a good agency doesn’t want a client who feels trapped. If they won’t, put the cancellation window on your calendar the day you sign, with a reminder two weeks before it opens.</p>"""),

            ("Termination: notice, cause and what happens on the way out", f"""<p>Look for two kinds of exit. Termination for cause (they miss deliverables, you don’t pay) and termination for convenience (either side just wants out). A fair contract has both, with the same notice period for each side.</p>
<p>Thirty days’ notice is common and fine. Sixty is livable. Ninety days for a monthly retainer is a lot of money to spend on a relationship that’s already over.</p>
<p>Then read what happens after notice is given. This is the part almost no one checks, and it’s where most ugly exits come from. A good termination clause says the agency will:</p>
<ul>
<li>Hand over admin access to every account it created for you, within a set number of days.</li>
<li>Export any data held in its own tools (call recordings, lead lists, reports) in a usable format.</li>
<li>Keep campaigns running, unchanged, through the notice period unless you ask otherwise.</li>
<li>Not pause, delete or restructure anything during the handover.</li>
</ul>
<p>If the contract also has an early termination fee, check if it’s a reasonable fee or simply every remaining month due at once. A fee equal to one month is a negotiation point. “All remaining fees become due” on a 12-month term is a walk-away clause for most small businesses.</p>"""),

            ("Ownership of accounts, data, creative and the website", f"""<p>This is the clause that matters most, and the one most often left vague. We have a whole post on {L(OWN, 'who owns your Google Ads account when you switch agencies')}, asset by asset, so here we’ll stick to what the contract should say.</p>
<p><b>Ad accounts.</b> The contract should say the accounts are yours and created in your name, with the agency given access. In Google Ads, ownership in practice means Admin access. Per {SRC['access']}, Admins can add and remove users, change access levels and unlink manager accounts, while Standard users can edit campaigns but can’t do those things. You want your own Admin login, not a promise. {SRC['pol3p']} also requires agencies to use “a separate account for each end-advertiser,” so if an agency proposes running your ads inside its own shared account, that’s a policy problem as well as an ownership one.</p>
<p><b>Billing.</b> Check whose card or invoice pays Google. If your account runs on monthly invoicing through the agency’s manager account, {SRC['unlink']} say the account “will stop serving” once it’s unlinked from that paying manager. That isn’t a reason to refuse agency billing, but the contract should commit the agency to help you move billing before any unlink.</p>
<p><b>Data.</b> GA4, Tag Manager, Search Console, call tracking, CRM records. The contract should say data generated for your business belongs to you and will be exported on exit.</p>
<p><b>Creative and the website.</b> This one surprises people. Paying for a logo or a website does not automatically make you the copyright owner. Under {SRC['circ30']}, a commissioned work from an outside contractor is only a “work made for hire” if it falls into one of nine specific categories and both parties sign a written agreement saying so. A website or a logo usually doesn’t fit those categories neatly. The safer route is a plain assignment, and under {SRC['s204']}, a transfer of copyright ownership isn’t valid without a written, signed document. So look for words like “assigns to Client all right, title and interest” in the deliverables, effective on payment.</p>
<!--fig:own-->
<p>Agencies fairly keep ownership of their own templates, internal tools and stock photo licenses (which are licensed, not owned, by anyone). That’s fine as long as you get a license to use what’s on your site forever. What you don’t want is a site built on an agency’s proprietary platform that can’t be moved, with “all work product” retained by the agency.</p>"""),

            ("Ad spend handling and markups", f"""<p>There are two common ways ad spend gets paid. Your card goes on file in Google Ads and Meta and the agency bills you only its fee. Or the agency pays the platforms and invoices you for spend plus fee. Both are legitimate. The second can hide a markup.</p>
<p>A markup isn’t automatically wrong. Some agencies float the spend and charge for the cash flow and risk. The problem is when it isn’t disclosed. {SRC['g3p']} says that, at a minimum, you have the right to know “the number of clicks, impressions, and the total cost” of your Google ads, and it encourages advertisers to understand total cost including any fees the partner charges. If your invoice says “Google Ads: $6,000” and the Google Ads account says $5,100, you’re owed an explanation.</p>
<!--fig:markup-->
<p>The contract should state which billing method applies, the exact management fee, and that any markup or “platform fee” on media is written as a percentage. Better still, ask for read access to billing in the ad accounts so you can match the invoice yourself. Our {L('/blog/marketing-agency-pricing-models-retainer-vs-percentage/', 'post on agency pricing models')} runs the math on percentage-of-spend fees if you’re comparing proposals.</p>"""),

            ("Setup fees: what they should buy", f"""<p>Setup fees are normal for ad accounts, SEO and websites. The first month of an account is real work: tracking, structure, negative keywords, landing page fixes. The test is whether the setup produces something you keep.</p>
<p>A setup fee should be tied to a short written list, for example:</p>
<ul>
<li>Conversion tracking for calls, forms and bookings, tested, with the right actions set as primary.</li>
<li>Call tracking numbers assigned by channel, in an account you own.</li>
<li>Campaigns built or rebuilt, with location settings and negative keyword lists documented.</li>
<li>A one-page account map you could hand to the next agency.</li>
</ul>
<p>“Onboarding fee” with no list is an ask. A setup fee that’s refundable if the agency never launches is a nice sign. A setup fee that’s charged again if you pause and restart is a little greedy.</p>"""),

            ("Performance guarantees, and why “guaranteed rankings” is a red flag", f"""<p>Everyone wants a guarantee. Some agencies sell one because it closes deals.</p>
<p>For SEO, Google is unusually blunt. {SRC['seo']} says “No one can guarantee a #1 ranking on Google,” and if an SEO guarantees their changes will put you in first place, “find someone else.” The same page warns about anyone who claims a “special relationship” with Google or advertises a “priority submit.” For paid ads, Google’s third-party guide says “it’s not possible to guarantee a specific ad position” on search results, because position is set by an auction on every search, and it lists guaranteed placement as a red flag.</p>
<!--fig:google-->
<p>So a guaranteed ranking clause tells you one of three things. The agency doesn’t understand how search works, or it plans to rank you for a phrase nobody searches (“best family dentist Spring Cypress Creek Parkway Saturday”), or the guarantee has so many exits it’s meaningless. Read the fine print of any guarantee and you’ll usually find that it’s a refund of the management fee after 12 months if you stayed and did everything they asked.</p>
<p>What a reasonable agency can commit to in writing: the work (a number of pages, ad tests, posts or reports per month), response times, and that tracking will be set up and verified so you can judge results yourself. Some will agree to a performance review point, like “if cost per lead isn’t under $X by month four, either side may exit with 15 days’ notice.” That’s a useful clause and a fair one.</p>"""),

            ("Reporting obligations", f"""<p>A contract that says “monthly reporting” and nothing else lets the agency send a PDF of impressions forever. Spell out what’s in it.</p>
<p>We’d ask the contract to commit to:</p>
<ul>
<li>Spend, clicks and impressions per platform (the minimum Google says you’re entitled to).</li>
<li>Conversions by type: calls over a set length, form fills, bookings. Not one blended “conversions” number.</li>
<li>Cost per lead, and cost per booked job if you share sales data back.</li>
<li>What changed this month and what’s planned next month.</li>
<li>A standing call, monthly at least, with the person who actually runs the account.</li>
</ul>
<p>And read-only access to everything, all the time, so the report is never your only view. If you’re already in a contract and these reports feel thin, our companion post on {L(SIGNS, 'signs your marketing agency isn’t working')} walks through a 30-minute check you can run yourself.</p>"""),

            ("Non-solicit clauses, plus the Texas notes we could verify", f"""<p>Many agency contracts say you can’t hire the agency’s employees during the contract and for a period after, often 12 months. Agencies include this because training an account manager is expensive and clients do sometimes poach them. It’s a reasonable clause in moderate form.</p>
<p>Watch for three things. The length (12 months after the end is common; 24 or 36 is a lot). Whether it covers contractors and freelancers the agency used, who may have worked for you directly before. And whether the penalty is a fixed “placement fee” such as a year of the person’s salary. A placement fee is often fairer than a flat ban, because it gives you a way to hire someone who wants to come work for you.</p>
<p>In Texas, restrictive covenants are governed by the Covenants Not to Compete Act in the Business and Commerce Code, section 15.50. In {SRC['marsh']} (2011), the Texas Supreme Court said covenants restricting solicitation of a former employer’s customers and employees “are restraints on trade and are governed by the Act,” and the statute requires reasonable limits on time, geographic area and scope of activity. The court also noted a trial court can reform an overbroad covenant. That case involved an employee rather than an agency client, so how it applies to your contract is a question for a lawyer, but it tells you Texas courts look at reasonableness.</p>
<p>A few other clauses worth a glance: exclusivity (you can’t use another agency for anything, even an unrelated billboard buy), venue (disputes heard in another state, which makes small claims impractical), and auto-approval of creative if you don’t respond in 48 hours.</p>"""),

            ("Clause by clause: fine, ask, or walk away", f"""<p>Here’s the whole contract in one table. “Ask” means raise it before signing; most agencies will adjust. “Walk away” means we’d pass unless it’s changed.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Clause</th><th>Fine</th><th>Ask</th><th>Walk away</th></tr></thead>
<tbody>
<tr><td>Term</td><td>3 months for ads, 6 for SEO, then monthly</td><td>12 months with a performance exit</td><td>12+ months with no exit for cause</td></tr>
<tr><td>Renewal</td><td>Rolls to month-to-month</td><td>Renews for a term, with a reminder notice</td><td>Silent renewal for a full term, short cancel window</td></tr>
<tr><td>Termination notice</td><td>30 days, both sides</td><td>60 days, or a one-month exit fee</td><td>All remaining fees due on exit</td></tr>
<tr><td>Account ownership</td><td>Accounts in your name, you hold Admin</td><td>Agency holds Admin but must transfer on request</td><td>Accounts belong to agency, or a shared account</td></tr>
<tr><td>Creative and website</td><td>Assigned to you on payment</td><td>Licensed to you forever; agency keeps templates</td><td>“All work product” retained, site can’t be moved</td></tr>
<tr><td>Data</td><td>Yours, exported on exit</td><td>Export on request for a fee</td><td>Call recordings and leads stay with agency</td></tr>
<tr><td>Ad spend</td><td>Billed to your card</td><td>Agency-billed with a written markup %</td><td>Agency-billed, markup undisclosed, no billing access</td></tr>
<tr><td>Setup fee</td><td>Tied to a written list</td><td>“Onboarding” with no list</td><td>Re-charged on every pause</td></tr>
<tr><td>Guarantees</td><td>Commitments to work and response times</td><td>Lead or cost targets with an exit if missed</td><td>Guaranteed #1 rankings or ad positions</td></tr>
<tr><td>Reporting</td><td>Leads, cost per lead, changes, access</td><td>“Monthly report” only</td><td>No account access, PDFs only</td></tr>
<tr><td>Non-solicit</td><td>12 months, employees only</td><td>Placement fee instead of a ban</td><td>Multi-year ban including freelancers</td></tr>
</tbody></table></div>
<!--fig:verdict-->
<p>If you get a contract with more than two “walk away” rows, it’s fine to say so and ask for a revised version. A good agency will send one by Monday. If they won’t change anything, you’ve learned what the relationship will be like.</p>
<p>And if you’d rather talk through a proposal with someone who writes these for a living, <a href="/contact/">get in touch</a>; tell us about the business and what you want the marketing to do, and a senior strategist will put together a plan you can compare against it.</p>"""),
        ],
        "faq": [
            ("What should I look for in a marketing agency contract?",
             "Check the minimum term and whether it auto-renews, the notice needed to cancel, and who owns the ad accounts, data, creative and website. Confirm whether ad spend is billed to your card or marked up, what the setup fee buys, what reports you are owed, and whether a non-solicit clause limits hiring. Ownership and termination terms matter most because they decide how cleanly you can leave."),
            ("Is a 12-month marketing agency contract normal?",
             "It happens, but for most small businesses we think it is longer than needed. Three months for paid ads and six for SEO, then month-to-month, covers the agency's setup time without locking you in. If you do sign 12 months, ask for a performance exit and make sure it rolls to month-to-month rather than renewing automatically for another full year."),
            ("Can an SEO agency guarantee first-page rankings?",
             "No. Google's own guidance says no one can guarantee a number one ranking on Google, and tells site owners to find someone else if an SEO guarantees first place. Google also says nobody can guarantee a specific paid ad position because ads are ranked in an auction on every search. A reasonable agency commits to the work it will do and to tracking you can check, not to a ranking."),
            ("Do I own the website my agency built?",
             "Not automatically. Under U.S. copyright law, commissioned work is only a work made for hire in nine specific categories with a signed written agreement, and a website usually does not fit. The safer approach is a written clause assigning the website, design and content to you on payment. Agencies can reasonably keep their own templates and tools as long as you have a permanent license."),
            ("Is a non-solicitation clause in an agency contract enforceable in Texas?",
             "It may be, depending on the details. Texas treats non-solicitation covenants as restraints governed by its Covenants Not to Compete Act, which requires reasonable limits on time, area and scope, and courts can reform overbroad terms. How that applies to a client-agency contract is a question for a Texas business attorney. Practically, ask for a 12-month limit or a placement fee."),
        ],
        "figures": {
            "order": {
                "type": "steps",
                "title": "Read an agency contract in this order",
                "sub": "Twenty minutes before you sign",
                "steps": [["Scope", "Are deliverables named, with numbers?"], ["Term and renewal", "How long, and does it roll to monthly?"], ["Termination", "Notice period, exit fee, handover duties."], ["Ownership", "Accounts, data, creative, website in your name."], ["Money", "Fee, setup list, how ad spend is billed."], ["Promises and limits", "Guarantees, reporting, non-solicit."]],
                "alt": "Six steps for reading a marketing agency contract before signing, for business owners in Houston and The Woodlands",
                "caption": "If ownership is murky, fix that before you worry about anything else.",
            },
            "own": {
                "type": "checklist",
                "title": "Ownership clauses to look for",
                "sub": "Words that should be in the contract",
                "items": ["Ad accounts created in the client’s name", "Client holds Admin access in Google Ads", "Client owns GA4, Tag Manager and Search Console", "Call tracking numbers can be ported or transferred", "Website and creative assigned to client on payment", "Domain registered to the client", "Data exported on exit in a usable format", "Agency keeps campaigns live through notice"],
                "alt": "Checklist of marketing agency contract ownership clauses for Houston and The Woodlands businesses: accounts, data, website",
                "caption": f"Details for each asset are in our {L(OWN, 'account ownership guide')}.",
            },
            "markup": {
                "type": "bars",
                "title": "What an undisclosed markup costs in a year",
                "sub": "$5,000 a month in Google Ads spend, same $1,000 management fee",
                "items": [["Spend billed to your card", 72000, "$72,000"], ["Agency-billed, 10% markup", 78000, "$78,000"], ["Agency-billed, 20% markup", 84000, "$84,000"]],
                "highlight": [0],
                "note": "Illustrative example: 12 months of $5,000 spend plus $1,000/month fee, markup applied to spend",
                "alt": "Bar chart showing how ad spend markups change yearly marketing agency costs for a Houston business",
                "caption": "A markup can be fair if it’s written down. The problem is the one you only find by matching invoices.",
            },
            "google": {
                "type": "stats",
                "title": "What Google and the law actually say",
                "stats": [["#1", "ranking no one can guarantee, per Google"], ["3", "numbers you can always ask for: clicks, impressions, cost"], ["9", "categories where commissioned work can be work for hire"]],
                "note": "Sources: Google Search Central, Google Ads third-party guide, U.S. Copyright Office",
                "alt": "Stats on SEO guarantees, ad reporting rights and work for hire rules for marketing agency contracts in Houston",
                "caption": f"From {SRC['seo']}, {SRC['g3p']} and {SRC['circ30']}.",
            },
            "verdict": {
                "type": "compare",
                "title": "Two contracts, same monthly fee",
                "left": {"title": "Built for the agency", "items": ["12 months, renews for 12", "90 days’ notice, fees accelerate", "Agency owns accounts and work", "Spend billed with a hidden markup", "Guaranteed page-one rankings"]},
                "right": {"title": "Built for both sides", "items": ["3 months, then month-to-month", "30 days’ notice, clean handover", "Client owns accounts, agency has access", "Spend on client card, fee itemized", "Commitments to work and tracking"]},
                "alt": "Comparison of agency-friendly and fair marketing agency contracts for small businesses in Houston and The Woodlands",
                "caption": "Most good agencies already write the right-hand version. Ask for it if they don’t.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: signs your agency isn't working
    {
        "slug": "signs-your-marketing-agency-isnt-working",
        "title": "Signs Your Marketing Agency Isn’t Working (and What to Do About It)",
        "seo_title": "Signs Your Marketing Agency Isn’t Working and What to Do",
        "desc": "Signs your marketing agency isn’t working: vanity metrics, no account access, stale reports, vague spend. A 30-minute self-check and how to switch cleanly.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google Analytics", "Meta"],
        "art": "b4",
        "hero": "filter",
        "hero_alt": "Illustration of a funnel filter for checking whether a marketing agency is working for a business in Houston and The Woodlands",
        "related": ["who-owns-google-ads-account-switch-agencies", "google-ads-not-converting-clicks-no-calls", "measure-marketing-success-metrics"],
        "sections": [
            (None, f"""<p>Monday morning at an HVAC company in Katy. The agency report landed over the weekend: impressions up 18%, click-through rate “strong,” a green arrow next to “conversions.” The owner scrolls past it and looks at the dispatch board. Same number of booked calls as last June, in a hotter June, with more spent on ads than ever.</p>
<p>He’s not sure if the agency is bad, or if the market is just tough, or if he’s reading the report wrong. That uncertainty is the real problem. He can’t judge the work, so he either keeps paying or fires them on a hunch.</p>
<p>The signs your marketing agency isn’t working are usually these: reports built on impressions and clicks instead of leads and revenue, no access to your own accounts, reports that look the same every month, a new junior account manager every quarter, vague answers about where the money went, and no evidence of testing. Most of those you can confirm yourself in about 30 minutes, inside Google Ads and GA4, without anyone’s permission.</p>
<p>We’re an agency, so take this with whatever salt you like. We’ve also inherited a lot of accounts from other agencies, and we’d rather owners knew how to check our work than trusted us blindly. Plenty of agencies do good work. Some relationships just drift, and nobody notices until the renewal.</p>"""),

            ("First, give it a fair window", f"""<p>Not every slow month is the agency’s fault. Before you judge, check a few things on your own side.</p>
<ul>
<li><b>How long has it been?</b> A new Google Ads account usually needs a few weeks of data before the bidding settles. SEO takes months. Three months is a fair first look for ads; six for SEO.</li>
<li><b>Did anything change at your end?</b> A new receptionist, a phone tree, slower callbacks, a price increase, a website edit that broke the form.</li>
<li><b>Did the season move?</b> A pool company in Magnolia and a roofer after a hailstorm in Cypress have very different Januaries.</li>
<li><b>Are leads being answered?</b> If calls go to voicemail at lunch, the ads can be perfect and still look broken. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers this side.</li>
</ul>
<p>If those check out and results are still flat after a fair window, it’s time to look at the agency’s side.</p>"""),

            ("Sign 1: the report is all vanity metrics", f"""<p>Impressions, reach, clicks, click-through rate, “engagement,” follower growth, average position. These describe activity. Some are useful for diagnosing a campaign. None of them pays your payroll.</p>
<!--fig:vanity-->
<p>A report that’s working for you leads with the numbers you’d recognize from the business: calls over a minute, form fills, booked appointments, cost per lead, and ideally cost per job or sale once you share that data back. If the report has those and the vanity numbers underneath, great. If the vanity numbers are all there is, ask why.</p>
<p>Watch the word “conversions” too. In Google Ads, a conversion is whatever someone set it to be. Per {SRC['calls']}, one type of call tracking, “clicks on a number on your mobile website,” records only the click on the phone number, not whether a call happened or how long it lasted. Page views, scroll depth or a click on a “Contact” button can also be set as conversions. Ask the agency to list every action counted as a conversion and which ones are primary. Our {L('/blog/measure-marketing-success-metrics/', 'post on measuring marketing success')} has a fuller list of metrics worth tracking.</p>"""),

            ("Sign 2: you don’t have access to your own accounts", f"""<p>If you can’t log into Google Ads, GA4, your Google Business Profile and your Meta ad account with your own email, you can’t check anything in this post. That alone is a sign, even if the work is good, because it means the relationship runs on trust only.</p>
<p>You want at least read-only access to everything, and Admin on the accounts you own. Per {SRC['access']}, Read-only users can see campaigns, billing details and performance reports without being able to change anything, which is exactly what an owner needs for spot checks. We won’t repeat the whole ownership walkthrough here; our post on {L(OWN, 'who owns your Google Ads account when you switch agencies')} goes account by account. If an agency resists giving you read-only access to your own ads, that’s about as clear a sign as you’ll get.</p>"""),

            ("Sign 3: reports that never change", f"""<p>Open three monthly reports side by side. Same commentary with the dates swapped? Same “next steps” every month (“continue optimizing,” “monitor performance”)? Same campaigns, same ads, same landing pages for a year?</p>
<p>Markets move. Houston has hurricane season, a long summer, school calendars in Conroe and Cy-Fair, and competitors who change their bids every week. An account that’s actively managed changes too. Reports that don’t change usually mean the account doesn’t either.</p>
<p>You can confirm it in change history, which we cover in the 30-minute check below.</p>
<!--fig:changes-->"""),

            ("Sign 4: a new junior account manager every few months", f"""<p>Agencies have turnover. Ours included, occasionally. A new contact once a year is normal. A new contact every quarter, each one younger than the last and each one asking you to re-explain your business, is a pattern.</p>
<p>The cost isn’t just your time. Each handoff loses context: why a keyword was excluded, which service area doesn’t pay, that Tuesday calls are slow because your techs are on install jobs. The new person often “refreshes” the account to show activity, which resets what was working.</p>
<p>Ask who actually makes changes in the account. Change history shows the email address of every user who edits it, so you can see whether the senior person from the sales pitch has touched it at all. Ask what happens to your account when your contact leaves, and whether notes are kept. A good agency has an answer.</p>"""),

            ("Sign 5: questions about spend get vague answers", f"""<p>“Where did the $7,000 go last month?” should have a straight answer within a day: which campaigns, which searches, what came back. {SRC['g3p']} says you have the right to know, at a minimum, the clicks, impressions and total cost of your Google ads, and it lists “not sharing the cost and performance of advertising campaigns” as a red flag.</p>
<p>The vague answers sound like this: “The algorithm is learning.” “Performance Max doesn’t really show that.” “Brand awareness is hard to measure.” Each can be partly true. None should be the whole answer every time. If the agency bills your ad spend, match its invoice to the billing summary inside Google Ads. They should match, or the difference should be a fee you agreed to in writing.</p>"""),

            ("Sign 6: nothing is ever tested", f"""<p>Good accounts are always testing something: a new ad message, a different landing page, a bid strategy, a new offer. Google gives agencies a built-in way to do this. The Experiments page sits in the left menu of Google Ads, and per {SRC['exp']}, it supports ad variations, custom experiments for bidding, match types and landing pages, Performance Max experiments and more.</p>
<p>An empty Experiments page isn’t proof of neglect. Plenty of good managers test by rotating ads or splitting campaigns. But ask: “What did we test in the last 90 days, and what did we learn?” If there’s no answer, there was probably no test.</p>
<p>Related tell: lots of changes made by “Google Ads system” in change history. Google can apply recommendations automatically when someone opts in, and per {SRC['auto']}, applied recommendations show on the History tab and in change history. Some auto-applied items are fine. An account run mostly on auto-apply is an account nobody is steering, and you’re paying a management fee for it.</p>"""),

            ("Run your own 30-minute check", f"""<p>You don’t need to be an expert to do this. You need your own login and half an hour. Do it on a quiet afternoon with a notepad.</p>
<!--fig:check-->
<h3>Minutes 1-8: Google Ads change history</h3>
<p>In Google Ads, open Change history from the Campaigns menu. Set the date range to the last 90 days. Per {SRC['hist']}, it covers up to two years, shows the email address of whoever made each change in the User column, and lets you filter by change type and campaign.</p>
<p>What to look for: are there changes every week or two? Who’s making them, a person or “Google Ads system”? Are they meaningful (new negative keywords, ad tests, budget shifts toward what works) or cosmetic? Twelve changes in 90 days on a $10,000-a-month account would worry us.</p>
<h3>Minutes 9-16: the search terms report</h3>
<p>Go to Campaigns, then Insights and reports, then Search terms. This is the list of what people actually typed before they clicked your ad. {SRC['terms']} notes some low-volume terms are left out for privacy, so you won’t see everything.</p>
<p>Sort by cost. Read the top 50. You’re looking for money spent on searches you’d never want: job seekers (“HVAC technician jobs Houston”), DIY (“how to recharge AC”), competitors you can’t serve, towns outside your area, wrong services. A few are normal. Pages of them, months in, mean nobody is adding negative keywords. This is the single fastest test of whether a search account is managed. Our {L('/blog/google-ads-not-converting-clicks-no-calls/', 'post on Google Ads clicks with no calls')} covers what to do with what you find.</p>
<h3>Minutes 17-24: GA4 key events</h3>
<p>In GA4, go to Admin, then Data display, then Events, and look at the Key events tab. Key events are what GA4 used to call conversions; {SRC['rename']} reported the rename on March 22, 2024, and {SRC['keydef']} explains that you then create Google Ads conversions from the key events that matter. Standard properties allow up to 30 key events, per {SRC['keyev']}.</p>
<p>Check that each one is a real business action (form submitted, call, booking confirmed), not page_view or scroll. Then look at the counts over the last month. Do they look like reality? If GA4 says 140 form leads and your inbox got 31, something is double-counting.</p>
<h3>Minutes 25-30: call tracking</h3>
<p>Call the number in your ads and on your website from your cell. Does it ring through? Does it show up in the call tracking or Google Ads call report within the hour? Then pull last month’s call log and listen to five recordings. Are they customers, or spam and vendors? Check the minimum call length your conversion is set to count; per {SRC['calls']}, that’s a number the advertiser sets, and a very short one counts hang-ups.</p>
<!--fig:facts-->
<p>When you’re done, write down what you found in four lines. That page is the start of the conversation.</p>"""),

            ("How to have the conversation", f"""<p>Go in with specifics and a fair tone. The goal is to find out whether the agency can fix it, not to win an argument. Some of the best client relationships we have started with a hard call like this.</p>
<ul>
<li><b>Lead with numbers.</b> “We spent $21,000 over three months and booked 38 jobs from ads. Last year we booked about the same with less. I want to understand why.”</li>
<li><b>Bring the evidence.</b> “There are $1,900 of clicks on job-seeker searches in the search terms report.” “Change history shows six changes since August.”</li>
<li><b>Ask for a plan, in writing, with dates.</b> What will change in the next 30 days, and what result should you expect to see by day 60?</li>
<li><b>Ask who will do it.</b> Name the person.</li>
<li><b>Agree on how you’ll judge it.</b> Booked jobs or qualified leads, by source, at a cost you can live with.</li>
</ul>
<p>Then give it the 30 to 60 days. A good agency will come back with changes you can see in change history within a week. If the reply is defensive, or the plan is “keep optimizing,” you have your answer.</p>"""),

            ("How to switch cleanly", f"""<p>If you decide to move, the order matters more than the speed. Most messy exits come from cancelling first and asking for access second.</p>
<!--fig:switch-->
<div class="bp-tbl"><table>
<thead><tr><th>When</th><th>Do this</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Before you give notice</td><td>Read the termination and ownership clauses. Confirm you have Admin on Google Ads, GA4, Tag Manager, Business Profile and Meta.</td><td>Access is easiest to get while everyone’s still friendly.</td></tr>
<tr><td>Before you give notice</td><td>Check billing. If ads are paid through the agency’s manager account, set up your own billing first.</td><td>Accounts on agency invoicing can stop serving when unlinked.</td></tr>
<tr><td>Before you give notice</td><td>Export reports, call recordings and lead lists you may not keep access to.</td><td>Tool accounts in the agency’s name may close.</td></tr>
<tr><td>Notice day</td><td>Give written notice per the contract. Ask for a handover list and a date.</td><td>Starts the clock cleanly.</td></tr>
<tr><td>During notice</td><td>Ask that campaigns stay live and unchanged. Bring the new team in with their own access.</td><td>Avoids a dark week of no leads.</td></tr>
<tr><td>After the last day</td><td>Remove old users and unlink their manager account. Keep the account and its history.</td><td>Years of data stay with your account.</td></tr>
</tbody></table></div>
<p>The full asset-by-asset version, including domains, call tracking numbers and Meta, is in {L(OWN, 'our account ownership guide')}. If you’re signing with someone new, read our list of {L(CONTRACT, 'marketing agency contract red flags')} first so the next exit is easier than this one.</p>
<p>Don’t start the new agency in a brand-new Google Ads account if you can avoid it. The history in the old one (search terms, conversion data) is worth keeping, and a new agency that insists on starting over should explain why.</p>"""),

            ("What “working” looks like", f"""<p>To be fair to agencies, here’s what a healthy relationship looks like from our side of the table. You can see every account. The report leads with leads and cost per lead, and it changes because the account changes. You know the name of the person running your ads, and they’ve been there a while. Spend questions get a straight answer in a day. Something is being tested most months, and you hear what was learned, including the tests that lost.</p>
<!--fig:healthy-->
<p>Results still go up and down. Houston’s summers, storms and school calendars see to that. But you understand why, and you trust the explanation because you can check it.</p>
<p>If you want a second opinion from people who’ll show you the search terms report rather than a slide about it, <a href="/contact/">get in touch</a>. Tell us about the business and your goals, and a senior strategist will build a plan around them. Our {L('/services/search-marketing/', 'search marketing')} and {L('/services/paid-social-advertising/', 'paid social')} pages show how we run accounts day to day.</p>"""),
        ],
        "faq": [
            ("How do I know if my marketing agency is doing a good job?",
             "Look at leads and revenue rather than impressions and clicks. A good agency gives you access to your own accounts, reports calls, forms and bookings with cost per lead, and makes regular changes you can see in Google Ads change history. Read your search terms report: if it is full of irrelevant searches months in, the account probably is not being managed closely."),
            ("How long should I give a new marketing agency before judging results?",
             "For Google Ads, about three months is a fair first look, since accounts need a few weeks of data before bidding settles. SEO usually needs six months or more. In the meantime you can still judge the process: tracking set up and verified, regular changes in change history, clear answers about spend, and a written plan with dates."),
            ("What is Google Ads change history and how do I find it?",
             "Change history is a log of every edit made to your Google Ads account over the past two years. Open it from the Campaigns menu in Google Ads. It shows what changed, when, and the email address of the user who made the change, and you can filter by date, change type and campaign. It is the quickest way to see whether an account is actively managed."),
            ("Should I tell my agency I am unhappy or just switch?",
             "Usually tell them first, with specifics. Bring numbers, such as spend versus booked jobs, and evidence from the search terms report or change history, then ask for a written plan with dates. Give it 30 to 60 days. If changes show up quickly and results move, the relationship may be worth keeping. If the response is defensive or vague, start planning a clean switch."),
            ("How do I switch marketing agencies without losing my Google Ads data?",
             "Keep the existing Google Ads account rather than starting a new one, because campaign history stays with the account. Before giving notice, confirm you hold Admin access, move billing to your own payments setup if the agency pays Google, and export anything held in the agency's tools. Ask that campaigns stay live during the notice period, then remove old users after the handover."),
        ],
        "figures": {
            "vanity": {
                "type": "compare",
                "title": "Vanity metrics vs. business metrics",
                "left": {"title": "Looks busy", "items": ["Impressions and reach", "Clicks and click-through rate", "Followers and engagement", "“Conversions” with no definition", "Average position"]},
                "right": {"title": "Pays the bills", "items": ["Calls over a set length", "Form fills you actually received", "Booked appointments or jobs", "Cost per lead by channel", "Cost per sale, from your data"]},
                "alt": "Comparison of vanity metrics and lead and revenue metrics in marketing agency reports for Houston and The Woodlands businesses",
                "caption": "Left-side numbers are fine for diagnosis. They shouldn’t be the headline.",
            },
            "changes": {
                "type": "columns",
                "title": "What a drifting account looks like",
                "sub": "Changes logged per month in Google Ads change history",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "values": [64, 48, 22, 9, 6, 4],
                "highlight": [3, 4, 5],
                "y_label": "changes",
                "note": "Illustrative example",
                "alt": "Column chart of declining monthly Google Ads changes, a sign a marketing agency isn’t working for a Houston business",
                "caption": "Heavy work at launch, then a slow fade. The reports kept looking the same the whole time.",
            },
            "check": {
                "type": "steps",
                "title": "Your 30-minute agency check",
                "sub": "All you need is your own login",
                "steps": [["Change history (8 min)", "Last 90 days. Who changes what, and how often?"], ["Search terms (8 min)", "Sort by cost, read the top 50 for junk."], ["GA4 key events (8 min)", "Real actions only? Do counts match reality?"], ["Call tracking (6 min)", "Test-call the ads number; listen to five calls."]],
                "alt": "Four steps for a 30-minute check of a marketing agency’s Google Ads and GA4 work for Houston and The Woodlands owners",
                "caption": "Write what you found in four lines. That’s your agenda for the agency call.",
            },
            "facts": {
                "type": "stats",
                "title": "Numbers worth knowing for your check",
                "stats": [["2 yrs", "of edits kept in Google Ads change history"], ["30", "key events allowed in a standard GA4 property"], ["5", "types of phone call conversions in Google Ads"]],
                "note": "Sources: Google Ads Help, Google Analytics Help",
                "alt": "Stats on Google Ads change history, GA4 key events and call conversions for checking a marketing agency in Houston",
                "caption": f"From {SRC['hist']}, {SRC['keyev']} and {SRC['calls']}.",
            },
            "switch": {
                "type": "funnel",
                "title": "Switching agencies, in order",
                "stages": [["Confirm Admin access and billing", "Week 0"], ["Export data from agency tools", "Week 0"], ["Give written notice", "Week 1"], ["Overlap: new team gets access", "Weeks 1-4"], ["Remove old users, keep the account", "Final day"]],
                "note": "Illustrative timeline for a 30-day notice period",
                "alt": "Timeline for switching marketing agencies cleanly for a business in Houston or The Woodlands without losing data",
                "caption": "Access and billing first. Notice second.",
            },
            "healthy": {
                "type": "checklist",
                "title": "Signs the relationship is healthy",
                "sub": "What we’d hold any agency to, including us",
                "items": ["You can log into every account yourself", "Reports lead with leads and cost per lead", "Change history shows regular human edits", "Search terms are clean of obvious junk", "Same account lead for a year or more", "Spend questions answered within a day", "A test most months, with results shared"],
                "alt": "Checklist of signs a marketing agency relationship is working for a business in Houston and The Woodlands",
                "caption": "Seven yeses is a good agency. Four or fewer is worth a conversation.",
            },
        },
    },
]
