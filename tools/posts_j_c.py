"""Batch 10: CPA and accounting firm marketing in Houston, mortgage loan officer and broker marketing in Houston,
and funeral home marketing in Houston.

Research, CPA post: 22 TAC 501.82 (TSBPA advertising rule: misleading claims, unverifiable testimonials, 36-month
retention of electronic and direct mail) and 22 TAC 501.75 (confidential client communications), via Cornell LII;
The Tax Adviser (Jan. 2024) on IRC Sec. 7216 (marketing use of return information needs consent, stricter separate
consent for 1040 filers, criminal penalties); Google Local Services Ads category list ("Tax services," "Financial
planning services," "Funeral home"); Google's government documents and services policy (tax preparation excluded);
IRS IR-2024-191 on Hurricane Beryl relief (Harris and Montgomery counties, deadlines to Feb. 3, 2025); TXCPA on SB 262
and the bachelor's-plus-experience pathway (licensure under it from Aug. 1, 2026); Google Maps prohibited content
policy for reviews.
Mortgage post: 7 TAC 56.203 and 57.203 (Texas SML advertising: company and originator names and NMLS IDs, social
media profile option, team names at substantially equivalent prominence); Texas SML social media requirements PDF;
OCCC RMLO licensing page; 12 CFR 1024.14 on consumerfinance.gov (RESPA Section 8); Consumer Finance Monitor on the
CFPB's 2020 Section 8 FAQs; Consumer Compliance Outlook on Reg Z 1026.24 triggering terms; Jon Loomer on Meta's
Financial Products and Services special ad category; Google's housing/employment/credit personalized ads FAQ; PPC Land
on Google's Oct. 20, 2026 announcement of financial services verification for the U.S. in early 2027; City of Houston
HAP Guidelines 8.0 (up to $75,000, 80% AMI, 8-hour course, participating lender); TSAHC Homes for Texas Heroes and
Home Sweet Texas pages (up to 5% DPA, 15% MCC, participating lenders).
Funeral post: NFDA 2025 Cremation & Burial Report (63.4% cremation, 31.6% burial) and statistics page (82.3% by 2045);
NFDA 2023 GPL study ($8,300 burial, $6,280 cremation medians); NFDA on the FTC's October 2022 ANPR; Federal Register
May 14, 2026 Funeral Rule PRA notice; Starmark (Sept. 2026) noting online pricing is still not finalized; Tex. Occ.
Code 651.405 and 22 TAC 203.46 (printed price lists, phone prices); TFSC consumer information page (Facts About
Funerals brochure, Banking vs. TDI for preneed); Texas Department of Banking prepaid funeral site; Pew Research 2025
social media use (71% of adults on Facebook, majority in every age group); Malwarebytes on fake funeral livestream
scams (Aug. 2024).
Competitor/PAA phrasing read for "accounting firm marketing", "how to get more clients as a CPA", "CPA google ads",
"mortgage loan officer marketing", "how to get mortgage leads", "mortgage marketing compliance", "funeral home
marketing", "how to market pre-need", "funeral home SEO".
Left out (unverified): any Texas rule requiring online posting of funeral prices; a Harris County Hispanic share
figure; current status of the CFPB's 2020 Section 8 FAQs after the May 2025 guidance withdrawals.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # CPA post
    "tsbpa_adv": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-501-82", "22 TAC §501.82"),
    "tsbpa_conf": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-501-75", "22 TAC §501.75"),
    "s7216": A("https://www.thetaxadviser.com/issues/2024/jan/the-many-implications-of-sec-7216/", "The Tax Adviser’s rundown of Sec. 7216"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "govpol": A("https://support.google.com/adspolicy/answer/9736337?hl=en", "Google’s government documents and services policy"),
    "beryl": A("https://irs.gov/newsroom/irs-provides-relief-to-hurricane-beryl-victims-in-texas-various-deadlines-postponed-to-feb-3-2025", "the IRS announcement"),
    "sb262": A("https://www.tx.cpa/news/latest-news/news/article/2025/09/26/new-additional-pathway-rules-adopted-by-state-board", "TXCPA"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    # mortgage post
    "sml56": A("https://www.law.cornell.edu/regulations/texas/7-Tex-Admin-Code-SS-56-203", "7 TAC §56.203"),
    "sml57": A("https://www.law.cornell.edu/regulations/texas/7-Tex-Admin-Code-SS-57-203", "7 TAC §57.203"),
    "smlsocial": A("https://www.sml.texas.gov/wp-content/uploads/2025/04/rmlo_social_media_requirements_and_best_practices_v3.pdf", "the SML’s social media guidance"),
    "occc": A("https://occc.texas.gov/industry/rmlos/", "the OCCC’s originator page"),
    "respa": A("https://www.consumerfinance.gov/rules-policy/regulations/1024/14/", "12 CFR 1024.14"),
    "faq2020": A("https://www.consumerfinancemonitor.com/2020/10/08/cfpb-issues-respa-section-8-faqs-and-rescinds-2015-marketing-services-agreement-bulletin/", "Consumer Finance Monitor’s summary of the CFPB’s 2020 Section 8 FAQs"),
    "regz": A("https://www.consumercomplianceoutlook.org/articles/2021/first-issue-2021/understanding-regulation-zs-advertising-requirements", "Consumer Compliance Outlook"),
    "metafps": A("https://www.jonloomer.com/qvt/financial-products-and-services/", "Jon Loomer"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "his special ad categories guide"),
    "gfaq": A("https://support.google.com/adspolicy/answer/9997418?hl=en", "Google’s housing, employment and credit policy FAQ"),
    "gfsv": A("https://ppc.land/google-forces-us-and-canadian-financial-advertisers-to-prove-licences-in-2027/", "PPC Land"),
    "hap": A("https://cohips.houstontx.gov/housing/plans-reports/guidelines/hap/Homebuyer_Assistance_Program_HAP_Guidelines-8.0-Entitlement-072126.pdf", "the city’s HAP guidelines (version 8.0)"),
    "heroes": A("https://www.tsahc.org/homebuyers-renters/homes-for-texas-heroes-program", "Homes for Texas Heroes"),
    "hst": A("https://www.tsahc.org/homebuyers-renters/home-sweet-texas-home-loan-program", "Home Sweet Texas"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis"),
    # funeral post
    "nfda_cb": A("https://nfda.org/app-pages/nfda-news/id/9787/nfda-releases-2025-cremation-burial-report-comprehensive-insights-to-guide-the-future-of-funeral-service", "NFDA’s 2025 Cremation & Burial Report"),
    "nfda_stats": A("https://nfda.org/news/statistics", "NFDA’s statistics page"),
    "nfda_cost": A("https://nfda.org/news/media-center/nfda-news-releases/articletype/articleview/articleid/8134", "NFDA’s 2023 price list study"),
    "anpr": A("https://nfda.org/news/in-the-news/nfda-news/id/6632/ftc-to-move-forward-with-rulemaking-process-to-modernize-the-funeral-rule", "NFDA’s report on the FTC vote"),
    "fr2026": A("https://www.govinfo.gov/content/pkg/FR-2026-05-14/html/2026-09705.htm", "the FTC’s May 2026 Federal Register notice"),
    "starmark": A("https://starmarkcp.com/blogs/industry-insights/ftc-funeral-rule-2026-firm-compliance", "a September 2026 industry summary"),
    "occ651": A("https://texas.public.law/statutes/tex._occ._code_section_651.405", "Texas Occupations Code §651.405"),
    "tac203": A("https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-203-46", "22 TAC §203.46"),
    "tfsc": A("https://tfsc.texas.gov/ConsumerInformation", "the Texas Funeral Service Commission"),
    "dob": A("https://www.prepaidfunerals.texas.gov/", "the Texas Department of Banking’s prepaid funeral site"),
    "pew": A("https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/", "Pew Research Center’s 2025 survey"),
    "scam": A("https://www.malwarebytes.com/blog/news/2024/08/fake-funeral-live-stream-scams-target-grieving-users", "Malwarebytes described in 2024"),
}

CPA = "/blog/cpa-accounting-firm-marketing-houston/"
MORT = "/blog/mortgage-loan-officer-marketing-houston/"
FUN = "/blog/funeral-home-marketing-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: CPA firms
    {
        "slug": "cpa-accounting-firm-marketing-houston",
        "title": "CPA and Accounting Firm Marketing in Houston: Better Clients, Fewer 1040s",
        "seo_title": "CPA & Accounting Firm Marketing in Houston",
        "desc": "CPA and accounting firm marketing for Houston: picking a niche, Texas board ad rules, Sec. 7216 and reviews, Google Ads keywords, LinkedIn and pricing pages.",
        "category": "Strategy",
        "icons": ["Google Ads", "LinkedIn", "Google Business Profile"],
        "art": "b3",
        "hero": "receipt",
        "hero_alt": "Illustration of a receipt for CPA and accounting firm marketing in Houston and The Woodlands",
        "related": ["law-firm-marketing-houston", "b2b-marketing-houston-energy-industrial", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>March 11, a little after 9 p.m., in a four-partner firm off Research Forest Drive. The conference room table is covered in folders: 1040s for people who found the firm by searching “tax preparer near me” in January, each paying a few hundred dollars and each convinced their return is the most urgent one in the building.</p>
<p>In the inbox sits an email from the owner of a $6 million HVAC company in Spring. Her bookkeeper quit, her current CPA doesn’t return calls until May, and she wants monthly financials, quarterly planning and someone to talk to about buying a second location. She came through a client referral. She’s the client the firm actually wants, and right now nobody has time to call her back.</p>
<p>That gap is most of what CPA marketing in Houston is about. You probably don’t need more clients. You need the right ones, arriving in the months when you can serve them, already knowing roughly what you charge.</p>
<p>For a small or mid-size accounting firm, that means picking one or two industries you’re good at and saying so publicly. Publish pricing that filters out bad fits. Bid on business-intent searches instead of “CPA near me” in February, and do your content and outreach in the off-season, when your people have time. The rest of this post is how we’d set that up, with the Texas rules that shape it.</p>"""),

            ("Why “more clients” is the wrong goal for most firms", f"""<p>Accounting has a capacity problem that most service businesses don’t. A plumber can add a truck. You can’t add a senior manager in February, and every new client in tax season competes for the same 70-hour weeks.</p>
<p>So start with the math, not the ads. Look at last year’s client list and sort it by fee per hour of staff time. In most firms we talk to, a small group of business clients carries the profit, and a long tail of simple individual returns eats the calendar in exactly the weeks when the business clients need you most.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Client type</th><th>Illustrative annual fee</th><th>When the work lands</th><th>Marketing verdict</th></tr></thead>
<tbody>
<tr><td>Simple individual 1040</td><td>$300 to $600</td><td>Feb to April</td><td>Stop advertising for it</td></tr>
<tr><td>Complex individual (rentals, K-1s, equity comp)</td><td>$1,200 to $3,500</td><td>March to October</td><td>Keep, via referrals and niche content</td></tr>
<tr><td>Small business tax only</td><td>$1,500 to $4,000</td><td>March and September</td><td>Upsell or price up</td></tr>
<tr><td>Monthly accounting plus tax</td><td>$12,000 to $40,000</td><td>Spread across the year</td><td>Main target for ads and content</td></tr>
<tr><td>Advisory, CFO-level work</td><td>$25,000 and up</td><td>Mostly off-season</td><td>LinkedIn, events, referrals</td></tr>
</tbody></table></div>
<p>Those fee ranges are illustrative. Use your own numbers. The point is the third column: monthly and advisory work spreads across the year, so marketing aimed at it smooths your capacity instead of piling more onto April.</p>"""),

            ("Pick a niche that Houston actually has", f"""<p>Generalist firms compete on price and proximity. Firms with a niche compete on “they already know my business,” which is a much easier sale and supports a much higher fee.</p>
<p>Houston gives you a lot of niches with real depth:</p>
<ul>
<li><b>Energy contractors and oilfield services.</b> Fabrication shops, trucking, inspection and rental companies along the Beltway and up I-45 have job costing, equipment depreciation, fuel tax and boom-bust cash flow problems a generalist won’t speak to. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for energy and industrial companies')} explains how these owners buy.</li>
<li><b>Restaurants and franchise operators.</b> Tip reporting, sales tax, food cost and multi-unit rollups. Owners in The Woodlands, Katy and Sugar Land talk to each other, so one good restaurant client tends to bring three more. See how they market themselves in our {L('/blog/restaurant-marketing-the-woodlands-houston/', 'restaurant marketing post')}.</li>
<li><b>Real estate investors.</b> Rental portfolios, short-term rentals, cost segregation, 1031 exchanges and entity structure. Houston’s rental market is big enough that a firm can live on this alone, and property managers are a natural referral source (our {L('/blog/property-management-company-marketing-houston/', 'property management marketing post')} shows who those managers are trying to reach).</li>
<li><b>Medical and dental practices.</b> The Texas Medical Center and the suburban specialty practices around it.</li>
<li><b>Construction and home services trades.</b> Remodelers, HVAC and plumbing companies with WIP schedules, retainage and fleet costs.</li>
</ul>
<!--fig:niche-->
<p>You don’t have to turn away everyone else. The niche is what you market. Referrals from existing clients can stay broad. But your website, your ads and your LinkedIn posts should make one kind of owner think “these people get it.”</p>"""),

            ("Texas State Board of Public Accountancy advertising rules", f"""<p>Texas CPAs work under the Board’s advertising rule, {SRC['tsbpa_adv']}. It bars communications that are false, fraudulent, misleading or deceptive, and its list of what counts as misleading is worth reading slowly, because a lot of standard marketing copy sits close to the line. The examples include claims of unjustified favorable results, self-praise not based on verifiable facts, untrue comparisons with other accountants and testimonials that can’t be verified.</p>
<p>What that means on a website or in an ad:</p>
<ul>
<li>Drop “Houston’s best CPA” and “top-rated tax firm” unless you can point to the verifiable source. “Rated 4.9 on Google from 140 reviews” is a fact. “Best” is self-praise.</li>
<li>Don’t promise outcomes. “We’ll cut your tax bill” or “average client saves $18,000” invites a misleading-results problem unless you can back it up for the claim as written.</li>
<li>Use testimonials only from real, identifiable clients who gave written permission, and keep the permission on file.</li>
<li>Skip comparisons to named or implied competitors (“unlike big-box tax chains, we…” is borderline; describe what you do instead).</li>
</ul>
<p>The rule also has a record-keeping piece that catches firms off guard. For electronic or direct mail communications, you’re expected to keep a copy and a list of recipients for at least 36 months after the last distribution, and broadcasts must be recorded and kept for the same period. There are exceptions, including communications to current clients and ones the recipient asked for. In practice: save every email campaign and its send list, and keep your ad creative in a dated folder. We’re marketers, not your ethics counsel, so run anything unusual past the Board’s rules or your attorney.</p>"""),

            ("Confidentiality, Section 7216 and reviews", f"""<p>Two sets of rules matter here, and they reach further into marketing than most firms assume.</p>
<p>The Texas confidentiality rule, {SRC['tsbpa_conf']}, says a CPA shall not voluntarily disclose information communicated by a client without the client’s permission, with exceptions for things like subpoenas, peer review and Board investigations. Federal law adds Internal Revenue Code Sec. 7216, a criminal provision covering preparers who knowingly or recklessly disclose or use tax return information. Per {SRC['s7216']}, using return information to market nontax services generally requires the taxpayer’s consent, and for individual 1040 filers that consent has to be a separate written document with mandatory language, signed before the use. Penalties can include a fine of up to $1,000 and up to a year in prison.</p>
<p>So before you build a marketing program, check these:</p>
<ul>
<li><b>Email lists.</b> Pulling your 1040 client list into a newsletter that pitches bookkeeping or advisory is a marketing use. Get 7216 consent first, or build the list from people who opt in on your website.</li>
<li><b>Ad platform uploads.</b> Uploading client emails to Google or Meta for retargeting or lookalikes is a disclosure to a third party. Don’t do it with tax clients unless counsel has signed off on the consent you have.</li>
<li><b>Case studies.</b> Even an anonymized story can identify a client in a small industry. Get written permission.</li>
</ul>
<p>Reviews are where firms slip most often. You can and should ask for Google reviews, but your replies can’t confirm that the reviewer is a client or mention anything about their situation. A safe reply to an angry review looks like this:</p>
<p><i>“Thanks for taking the time to write. We take every concern seriously, and because of our confidentiality obligations we can’t discuss any client matter here. Please call our office manager at [number] so we can talk directly.”</i></p>
<p>For asking, Google’s rules apply like anywhere else: no discounts for reviews and no asking only the happy clients, per {SRC['gpol']}. The best moment is right after a deliverable the client values, like a finished return with a smaller balance due than they feared or a clean first set of monthly financials. Send one short email with the review link. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has the full request sequence.</p>"""),

            ("Google Ads: “CPA near me” vs. “small business accountant”", f"""<p>Search ads work for accounting firms, but only if you pick the searches that bring your target client. The two most obvious keywords bring very different people.</p>
<p>“CPA near me” and “tax preparer near me” are mostly individuals, mostly in February through April, and mostly price shopping a 1040. “Small business accountant Houston,” “outsourced bookkeeping for contractors” and “restaurant CPA” are business owners, spread across the year, looking for an ongoing relationship. If your goal is the HVAC owner from the opening, the second group is where your budget belongs.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Keyword group</th><th>Examples</th><th>Who searches</th><th>Our take</th></tr></thead>
<tbody>
<tr><td>Generic individual</td><td>cpa near me, tax preparer near me, tax filing help</td><td>Individuals, Jan to April</td><td>Pause in season unless you want 1040s</td></tr>
<tr><td>Business accounting</td><td>small business accountant houston, bookkeeping services the woodlands, outsourced accounting firm</td><td>Owners, year-round</td><td>Core campaign</td></tr>
<tr><td>Niche</td><td>cpa for real estate investors houston, oilfield accounting firm, restaurant accountant katy</td><td>Owners in your niche</td><td>Highest intent, lowest volume</td></tr>
<tr><td>Problem</td><td>irs letter help, back taxes accountant, unfiled returns business</td><td>Urgent, mixed</td><td>Good if you do resolution work</td></tr>
<tr><td>Advisory</td><td>fractional cfo houston, business valuation for sale</td><td>Larger owners</td><td>Test with a small budget</td></tr>
</tbody></table></div>
<p>Negatives matter more than usual, because “CPA” is also an exam, a career and a word people type when they want to reach the IRS:</p>
<!--fig:negatives-->
<p>A few settings we’d use. Run business campaigns weekdays, roughly 7 a.m. to 7 p.m., when owners search and someone can answer. Use location targeting set to people in or regularly in your area, drawn around where your clients actually are: The Woodlands, Spring, Conroe and north Harris County for a Woodlands firm, or Katy, Cypress and the Energy Corridor for a west side one. Send every ad group to a page about that service or niche. Never the homepage.</p>
<p>Two platform notes. Google’s Local Services Ads list includes a “Tax services” category (and “Financial planning services”), per {SRC['lsa']}, so test it if individual tax work is something you want. And {SRC['govpol']} specifically says tax preparation services aren’t restricted by it, though we’d still keep anything that looks like an IRS seal out of your ads. For click costs before you set a budget, see our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')}, and our {L('/services/search-marketing/', 'search marketing team')} can run it if you’d rather not.</p>"""),

            ("Off-season content: May through December is your marketing season", f"""<p>Your marketing calendar should be the inverse of your workload. In tax season, nobody at the firm has time to write, film or call. In May, June, July and the weeks after the October extension deadline, they do.</p>
<!--fig:calendar-->
<p>What to make in those months:</p>
<ul>
<li><b>Niche pages.</b> One solid page per niche explaining the problems you solve, what an engagement looks like and a starting price. These pages rank, and they convert the ad traffic above.</li>
<li><b>Year-end planning content in October and November.</b> Entity selection, equipment purchases, retirement plan deadlines. Business owners search this before December, and it’s the best season to start an advisory relationship.</li>
<li><b>Houston disaster content, ready to publish.</b> After Hurricane Beryl, the IRS postponed a range of federal filing and payment deadlines to Feb. 3, 2025, for taxpayers in Texas counties including Harris and Montgomery, per {SRC['beryl']}. A plain-English “what this means for your business” page published within a day or two is exactly what worried owners search for after a storm. Keep a template ready for the next one.</li>
<li><b>A short monthly email</b> to people who opted in, with one useful thing per issue. Our {L('/blog/email-marketing-basics/', 'email marketing basics')} covers list building.</li>
</ul>
<p>Batch it. One partner and one marketing person can record four short videos and outline six articles in a single afternoon in June, then publish through the fall. Our post on {L('/blog/content-marketing-service-businesses/', 'content marketing for service businesses')} has a simple workflow.</p>"""),

            ("LinkedIn for accountants: partners, not the firm page", f"""<p>In accounts we’ve seen, firm pages on LinkedIn get very little reach. Partners and managers posting as themselves do much better, and business owners and CFOs are already there.</p>
<p>What we’d have each partner do, about 30 minutes a week:</p>
<ul>
<li>Post once a week about one real issue you see in your niche, written in plain language with no client details. “Three things I see in every contractor’s WIP schedule” beats a reshared firm announcement.</li>
<li>Comment on posts from owners, bankers, attorneys and wealth managers in your niche. Comments get you seen by their networks.</li>
<li>Connect with the bankers and commercial lenders at local banks. They refer more business clients than almost anyone.</li>
<li>Keep the profile headline specific: “CPA for Houston real estate investors and property managers,” not “Partner at XYZ CPAs.”</li>
</ul>
<p>Paid LinkedIn ads are expensive per click. They can work for advisory or a firm with a high-fee niche, targeted by job title and company size, but we’d start organic and add paid only once your niche page converts.</p>"""),

            ("Pricing pages: filter out bad fits before the first call", f"""<p>Most CPA websites say “contact us for pricing.” Owners read that as “expensive and slow.” A pricing page with starting ranges does two things: it tells the right clients you’re in their range and tells the wrong ones to keep looking.</p>
<p>A simple structure that works:</p>
<ul>
<li><b>Packages by client type</b>, each with “starting at” monthly pricing, what’s included (bookkeeping cadence, payroll, sales tax, tax returns, a planning meeting) and what isn’t.</li>
<li>Minimums, stated plainly: “Our business engagements start at $1,000 a month.” That one line saves your partners hours of discovery calls.</li>
<li>A short intake form asking revenue range, industry, current accounting setup and timeline. Use the answers to route and prioritize.</li>
<li><b>Individual tax pricing</b>, if you still do it, with a clear floor.</li>
</ul>
<p>Firms worry that posting prices invites shoppers. Some will shop. But the calls you do get are better, and your Google Ads conversion rate goes up because the landing page answers the main question. We’ve seen the same pattern across professional services, including in our {L('/blog/law-firm-marketing-houston/', 'law firm marketing post')}.</p>"""),

            ("Capacity planning around tax season", f"""<p>The worst thing marketing can do for a CPA firm is work in February. If your ads produce a dozen good business leads during the second week of March and nobody calls them back until May, you paid for leads that went to someone else.</p>
<!--fig:capacity-->
<p>Practical moves:</p>
<ul>
<li>Cut or pause generic campaigns from February through mid-April, and keep only your niche and business campaigns running at a lower budget.</li>
<li>Change your form confirmation in season: “We’re booking new business clients for consultations starting April 21. Pick a time now.” Then actually hold those slots.</li>
<li>Have one person own new-business follow-up in season, even if it’s only a 10-minute call to qualify and schedule. Speed still matters; our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} shows why.</li>
<li>Track inquiries by source with call tracking and form tracking, so you know in May which channel produced the clients you kept. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} covers setup.</li>
</ul>
<p>Hiring may get slightly easier. Texas passed SB 262 in 2025, adding a licensure pathway with a bachelor’s degree, two years of experience and the CPA exam alongside the 150-hour route, and candidates can be licensed under it starting Aug. 1, 2026, per {SRC['sb262']}. We wouldn’t build a growth plan on that, though. Plan marketing around the team you have.</p>"""),

            ("A first 90 days for a Houston accounting firm", f"""<p>If we were starting from scratch with a 3-to-15-person firm:</p>
<ol>
<li><b>Days 1 to 30.</b> Sort clients by fee per hour and pick one niche. Write the niche page and the pricing page. Fix the Google Business Profile: primary category, accurate hours, real photos of the team, and services listed. Start asking business clients for reviews after deliverables.</li>
<li><b>Days 31 to 60.</b> Launch one business search campaign and one niche campaign with the negatives above. Set up call and form tracking. Have each partner start the weekly LinkedIn routine.</li>
<li><b>Days 61 to 90.</b> Publish two or three niche articles, start a monthly email to opted-in contacts, and review search terms weekly. Book coffees with five bankers and three attorneys in your niche.</li>
</ol>
<p>Judge it by consultations booked with your target client type and by engagement letters signed. Leads don’t count until they’re the right leads.</p>
<p>If you want help building this around your firm’s capacity and the clients you want more of, <a href="/contact/">get in touch</a>. Tell us about the practice and your goals, and a senior strategist will put together a plan that fits around tax season.</p>"""),
        ],
        "faq": [
            ("How do CPA firms get more clients?",
             "Most good CPA clients still come from referrals, so start by asking happy business clients and building relationships with bankers and attorneys. Then add a niche page and pricing page on your website, Google Ads on business-intent searches like small business accountant plus your area, a steady flow of Google reviews and partner posts on LinkedIn. Schedule most marketing work for the off-season when your staff has time to follow up."),
            ("Should an accounting firm use Google Ads?",
             "Yes, if you choose the keywords carefully. Searches like CPA near me bring mostly individual tax clients in February through April, while searches like outsourced bookkeeping Houston or restaurant accountant bring business owners year-round. Run business and niche campaigns, add negatives for jobs, the CPA exam and IRS phone searches, and send each ad group to a matching service page. Google Local Services Ads also offer a Tax services category."),
            ("What are the Texas advertising rules for CPAs?",
             "The Texas State Board of Public Accountancy rule at 22 TAC 501.82 bars false, misleading or deceptive communications. Examples include unjustified favorable results, self-praise not based on verifiable facts, untrue comparisons with other accountants and unverifiable testimonials. It also expects firms to keep copies and recipient lists of electronic and direct mail communications for at least 36 months, with some exceptions. Check unusual claims with the Board rules or your attorney."),
            ("Can a CPA respond to Google reviews?",
             "Yes, but carefully. Texas confidentiality rules and federal Sec. 7216 limit what you can disclose, so a reply should never confirm the reviewer is a client or mention their situation. Thank them, say confidentiality prevents discussing any client matter publicly, and offer a phone number to talk directly. You can ask clients for reviews, but Google prohibits incentives and asking only happy clients."),
            ("Should CPA firms put prices on their website?",
             "We think so. Starting-at prices by client type, a stated engagement minimum and a short intake form help the right business owners see you fit their budget and keep poor fits from booking discovery calls. You get fewer inquiries but better ones, and paid search converts better because the page answers the price question. Keep the numbers accurate and note what each package includes."),
        ],
        "figures": {
            "niche": {
                "type": "compare",
                "title": "Generalist firm vs. niche firm",
                "left": {"title": "Generalist", "items": ["“Tax and accounting for individuals and businesses”", "Competes on price and location", "Every inquiry needs discovery from scratch", "Busy season decides everything", "Referrals are random"]},
                "right": {"title": "Niche", "items": ["“Accounting for Houston oilfield service companies”", "Competes on knowing the industry", "Inquiries arrive pre-qualified", "Monthly work spreads the year", "Clients refer peers in the same industry"]},
                "alt": "Comparison of generalist and niche CPA firm marketing for accounting firms in Houston and The Woodlands",
                "caption": "Your referral network can stay broad. Your marketing should pick a lane.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for CPA firms",
                "sub": "Add these before the first click",
                "items": ["Careers: jobs, hiring, salary, internship", "Exam: cpa exam, becker, review course, cpe", "IRS: irs phone number, where’s my refund, refund status", "DIY software: turbotax, free file, freetaxusa", "Chains you aren’t: h&r block, jackson hewitt", "Free: free tax filing, vita (unless you volunteer)", "Learning: how to become a cpa, accounting degree", "Wrong service: payroll software, quickbooks login"],
                "alt": "Checklist of negative keywords for CPA and accounting firm Google Ads in Houston",
                "caption": "Then read the search terms report every week for the first month.",
            },
            "calendar": {
                "type": "columns",
                "title": "Workload vs. marketing effort by month",
                "sub": "When to make content and run outreach",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [70, 90, 100, 95, 40, 35, 35, 45, 75, 80, 45, 55],
                "highlight": [4, 5, 6, 10],
                "y_label": "Staff workload",
                "note": "Illustrative example",
                "alt": "Chart of CPA firm workload by month showing the off-season marketing window for Houston accounting firms",
                "caption": "Highlighted months are where most firms have the time to write, film and network.",
            },
            "capacity": {
                "type": "steps",
                "title": "Marketing around tax season",
                "sub": "Keep leads from dying in March",
                "steps": [["Jan: trim", "Pause generic 1040 keywords, keep business campaigns."], ["Feb to Apr: hold", "Book consultations into reserved post-season slots."], ["One owner", "One person qualifies new-business leads within a day."], ["May: restart", "Raise budgets, publish the content you drafted."], ["Oct to Nov: plan", "Year-end planning content and banker outreach."]],
                "alt": "Steps for planning CPA firm marketing around tax season capacity in Houston and The Woodlands",
                "caption": "Reserve the slots before the season, and the leads still convert after it.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: mortgage
    {
        "slug": "mortgage-loan-officer-marketing-houston",
        "title": "Mortgage Loan Officer Marketing in Houston: Referrals, Compliance and Leads That Close",
        "seo_title": "Mortgage Loan Officer Marketing in Houston",
        "desc": "Mortgage loan officer and broker marketing in Houston: realtor partnerships under RESPA, Texas NMLS ad rules, Reg Z trigger terms, Meta and Google ad limits.",
        "category": "Paid ads",
        "icons": ["Meta", "Google Ads", "Facebook"],
        "art": "b2",
        "hero": "key",
        "hero_alt": "Illustration of a house key for mortgage loan officer and broker marketing in Houston and Cypress",
        "related": ["real-estate-agent-marketing-the-woodlands-houston", "home-builder-marketing-houston-montgomery-county", "facebook-lead-ads-bad-leads-fix-quality"],
        "sections": [
            (None, f"""<p>Thursday, 6:40 p.m., in Cypress. A loan officer has bought 14 internet leads since lunch. She’s called each one twice. Two picked up, one already locked with someone else, one wanted to know the rate on a $90,000 cash-out on a house with a 580 score.</p>
<p>Meanwhile, the buyer a Bridgeland agent sent over on Saturday has already uploaded pay stubs and asked when he can get a pre-approval letter.</p>
<p>Anyone who has originated in Houston for more than a year knows which of those leads closes. Mortgage loan officer marketing works when it builds more of the second kind (warm referrals from agents, builders, past clients and people who trust you before they call) and treats the first kind as a numbers game with tight rules. It also has more compliance tripwires than almost any local business we write about. Your ads touch RESPA, Texas licensing rules, Regulation Z and special ad restrictions on both Google and Meta.</p>
<p>This guide is for individual loan officers, small brokerages and branch managers in Greater Houston. It isn’t legal advice; your compliance department or attorney has the final word on anything here.</p>"""),

            ("Rate-shopper leads vs. referral leads", f"""<p>The two lead types behave so differently that they need separate budgets, separate scripts and separate success metrics.</p>
<!--fig:leads-->
<p>Rate-shopper leads (purchased internet leads, rate-table placements, broad “mortgage rates” search ads) arrive in volume and close at low rates. They reward speed above all else: the first loan officer to have a real conversation usually wins. If you buy them, plan on calling within five minutes, six or more touches across two weeks, and a contact rate that will disappoint you. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the follow-up cadence we’d use.</p>
<p>Referral leads come from agents, builders, financial planners, CPAs and past clients. Fewer of them, and they close at several times the rate, because someone the borrower trusts already vouched for you. Most of your marketing budget should make referral partners look good and make past clients remember you. Paid ads can fill gaps, but they shouldn’t be the whole business.</p>"""),

            ("Realtor and builder partnerships under RESPA Section 8", f"""<p>Every loan officer wants more agent referrals, and RESPA Section 8 is the rule that decides how you can go after them. Under {SRC['respa']}, no person shall give and no person shall accept any fee, kickback or other thing of value under an agreement to refer settlement service business. Paying for goods or services actually furnished is allowed, but anything above market value is treated as not being for services actually performed. So are “normal promotional and educational activities” that aren’t conditioned on the referral of business.</p>
<p>The CFPB’s 2020 Section 8 FAQs added some practical color, per {SRC['faq2020']}. A gift to a consumer for doing business with you isn’t prohibited, but an incentive for referring other business is. Gifts to referral sources in exchange for referrals are prohibited, and there’s no exception based on how small the gift is. Marketing services agreements aren’t automatically illegal, but they aren’t presumed legal either.</p>
<p>How that plays out in Houston co-marketing:</p>
<ul>
<li><b>Joint ads and flyers.</b> If you and an agent split a Facebook ad or an open-house flyer, pay your share of the actual cost based on your share of the space, and keep the invoice. Paying for the whole thing while the agent gets the exposure is the classic problem.</li>
<li><b>Open houses.</b> Showing up to answer financing questions is fine. Paying for the agent’s signs, food or listing photos is the agent’s expense you’d be defraying.</li>
<li><b>Lunch-and-learns and CE classes.</b> Education open to agents generally, not conditioned on referrals, is the textbook promotional activity. Keep the agenda, sign-in sheet and costs.</li>
<li><b>Builders.</b> Preferred lender arrangements in master-planned communities like Bridgeland, Towne Lake or the Conroe MPCs raise their own Section 8 and affiliated business questions. Get counsel involved before you sign anything that ties marketing spend to a builder’s buyer traffic.</li>
</ul>
<!--fig:respa-->
<p>What reliably works and stays clean is boring: be the lender who answers on a Sunday, closes on time and keeps the agent updated without being asked. Then give agents tools they can use (a fast pre-approval turnaround, a one-page program summary in English and Spanish, a quick text when the appraisal comes in). Our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how Woodlands and Houston agents market themselves')} shows what they’re juggling, and our {L('/blog/home-builder-marketing-houston-montgomery-county/', 'home builder marketing playbook')} explains the builder side.</p>"""),

            ("Texas license and NMLS disclosures in every ad", f"""<p>Texas puts specific identifying requirements on mortgage advertising. For residential mortgage loan companies under the Texas Department of Savings and Mortgage Lending (SML), {SRC['sml56']} requires an ad to include the company’s name and NMLS ID, its website address if it has one, and the sponsored originator’s name and NMLS ID. Mortgage bankers have a parallel rule at {SRC['sml57']}. Ads made directly by the company to the public don’t need the individual originator’s details.</p>
<p>Social media gets a practical exception. You can meet the requirement by prominently displaying the required information on your home page, profile page or similar, and it has to be easy to find without scrolling through old posts. Per {SRC['smlsocial']}, social accounts should show the company name and NMLS ID, your name and NMLS ID, and the corporate website.</p>
<p>Team names trip up a lot of Houston loan officers. “The Bayou City Home Loans Team” is allowed for advertising only, and the legal company name and NMLS ID have to appear with it in substantially equivalent prominence. You can’t bury the company name in light gray 6-point type under a big logo, and team names can’t appear on applicant documents.</p>
<p>If you originate second liens, home equity or manufactured housing loans under a company licensed by the Office of Consumer Credit Commissioner instead, your license comes from the OCCC, per {SRC['occc']}, and you should confirm your advertising requirements with that agency and your compliance team.</p>
<p>Our practical checklist: NMLS IDs in every social profile bio and every paid ad, the company name at equal weight next to any team logo, and the NMLS Consumer Access link in your website footer.</p>"""),

            ("Reg Z trigger terms: the words that force more disclosure", f"""<p>Regulation Z’s advertising rule, 12 CFR 1026.24, is why so many mortgage ads read like legal documents. State certain terms and you have to state a lot more. Per {SRC['regz']}, the triggering terms for closed-end credit are the down payment (only if one is actually required), the number of payments or repayment period, the amount of any payment, and the amount of any finance charge. When an ad uses one, it must also disclose the down payment, the repayment terms and the APR, plus whether the APR may increase.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad copy</th><th>Triggers?</th><th>Why</th></tr></thead>
<tbody>
<tr><td>“Only 3.5% down”</td><td>Yes</td><td>States a down payment</td></tr>
<tr><td>“80% financing available”</td><td>Yes</td><td>Implies a 20% down payment</td></tr>
<tr><td>“$1,950 a month”</td><td>Yes</td><td>States a payment amount</td></tr>
<tr><td>“30-year fixed”</td><td>Yes</td><td>States the repayment period</td></tr>
<tr><td>“No down payment options for eligible veterans”</td><td>No</td><td>“No down payment” isn’t a trigger</td></tr>
<tr><td>“Low monthly payments”</td><td>No</td><td>No dollar amount</td></tr>
<tr><td>“No closing costs”</td><td>No</td><td>Saying there’s no charge isn’t a trigger</td></tr>
</tbody></table></div>
<p>Also, if you state a rate, the APR has to appear too, and the interest rate can’t be more conspicuous than the APR. On a 125-character Facebook headline, that’s very hard to do well. Our approach is to keep paid ads trigger-free and move the numbers to a landing page that can carry every required disclosure.</p>
<p>Trigger-free headlines that still work:</p>
<ul>
<li>“Buying your first home in Katy? See which Texas down payment programs you may qualify for.”</li>
<li>“Pre-approved in 24 hours. Local loan officer, answers on weekends.”</li>
<li>“VA loans explained by a Houston veteran. Book a 15-minute call.”</li>
</ul>"""),

            ("Facebook and Instagram ads under the Financial Products and Services category", f"""<p>Meta replaced its old Credit special ad category with a broader Financial Products and Services category, and U.S. ads for loans and other financial products must declare it or get rejected, per {SRC['metafps']}. The restrictions, as {SRC['loomer']} describes them: age fixed at 18 to 65+, all genders, some detailed targeting unavailable and no exclusions, location targeting that must include a 15-mile radius around any point, no ZIP code targeting and no lookalike audiences.</p>
<p>So on Meta, your creative does the targeting. A stock photo of a smiling couple holding keys reaches everyone and converts no one. A 30-second phone video of you standing in front of a new build in Elyson explaining one specific program finds the right people because everyone else scrolls past.</p>
<p>What we’d run:</p>
<ul>
<li>Short educational videos, one topic each: the Houston HAP, TSAHC programs, VA loans, buying with student debt, what pre-approval actually means.</li>
<li>Instant forms with two or three qualifying questions (timeline, whether they’ve talked to a lender, whether they’re working with an agent). Harder forms mean fewer leads and better ones; our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'guide to fixing bad Facebook leads')} has the details.</li>
<li>Retargeting of website visitors and video viewers with a calendar link.</li>
<li>Your NMLS ID in the page profile and, where your compliance team wants it, in the ad text.</li>
</ul>
<p>Our {L('/services/paid-social-advertising/', 'paid social team')} runs campaigns inside these restrictions if you’d rather hand it off.</p>"""),

            ("Google Ads for mortgages: targeting limits and verification", f"""<p>Google applies similar limits. Under {SRC['gfaq']}, credit ads in the U.S. can’t target or exclude by age, gender, parental status or marital status, and ZIP code targeting is off the table, so you’ll target by city, county or radius. Search keywords carry most of the intent anyway.</p>
<p>More verification is coming. On Oct. 20, 2026, Google announced it will bring its Financial Services Verification program to the U.S. and Canada in early 2027, requiring certain financial advertisers to show they’re authorized by relevant regulators, per {SRC['gfsv']}. Google has only named some product types so far, and it hasn’t said whether NMLS-licensed lenders will be covered or what the deadlines are. We’d make sure your Google Ads account name, website and business details match your NMLS records now, so there’s nothing to untangle later.</p>
<p>Keywords we’d build around in Houston:</p>
<ul>
<li>Program searches: “first time home buyer programs houston,” “houston down payment assistance,” “tsahc lender near me,” “houston hap lender.”</li>
<li>Loan types: “fha loan houston,” “va loan lender cypress,” “jumbo loan the woodlands,” “self employed mortgage houston.”</li>
<li>Broker and local intent: “mortgage broker the woodlands,” “local mortgage lender katy.”</li>
</ul>
<p>And negatives: jobs, salary, “loan officer license,” “nmls course,” “pay my mortgage,” “mortgage login,” servicer names, “reverse mortgage” if you don’t do them, and “calculator” on campaigns where budget is tight. See our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} before you set a budget; mortgage clicks are some of the most expensive in any market.</p>"""),

            ("First-time buyer programs make the best content", f"""<p>The most useful content a Houston loan officer can publish is a clear explanation of the assistance programs buyers have heard about and don’t understand. Two are worth a page each.</p>
<p><b>City of Houston Homebuyer Assistance Program (HAP).</b> Per {SRC['hap']}, effective June 23, 2026, HAP offers up to $75,000 as a forgivable loan. Buyers generally need household income at or below 80% of area median income (up to 120% for some TIRZ-funded assistance), the home must be within the City of Houston’s incorporated areas, buyers must finish an 8-hour homebuyer course from a HUD-approved counseling agency, and the mortgage must be a fixed-rate loan from a participating lender. That city-limits rule matters: plenty of buyers searching “Houston” are shopping in Cypress, Spring or Pearland.</p>
<p><b>Texas State Affordable Housing Corporation (TSAHC).</b> {SRC['heroes']} serves full-time teachers, school staff in certain roles, police, firefighters, EMS, certain corrections officers, nursing faculty and veterans. {SRC['hst']} serves low- and moderate-income buyers. Both offer down payment assistance of up to 5% of the loan amount, as a grant or a forgivable second lien, and a Mortgage Credit Certificate for first-time buyers worth a federal tax credit of 15% of the mortgage interest paid each year. Buyers apply through a TSAHC-approved participating lender.</p>
<!--fig:programs-->
<p>Only build content around programs you can actually originate. If you aren’t an approved lender for TSAHC or HAP, either get approved or don’t publish the page. A buyer who finds out on the second call that you can’t do the program they came for won’t give you a third.</p>
<p>Spanish-language versions of these pages pay off in Houston. Our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing guide')} covers Spanish SEO and ads, and the same Reg Z and NMLS rules apply in either language.</p>"""),

            ("Follow-up, texts and the past-client database", f"""<p>Your past clients are the cheapest source of your next loan, and most loan officers barely talk to them.</p>
<ul>
<li>Send a short annual check-in on the loan anniversary with the client’s rough equity picture and a reminder that you’re around.</li>
<li>Mail a holiday card and a hurricane-season prep list in June. Houston homeowners will open the second one.</li>
<li>When rates move, call the clients who benefit. Use a list, not a blast.</li>
<li>Ask for referrals by name after closing, when the client is happiest. A gift to the client for doing business with you is fine; rewarding them for referring others is where Section 8 bites.</li>
</ul>
<p>Texting needs consent and care. Loan status updates differ from marketing texts, and Texas brought marketing texts under its telephone solicitation law through SB 140, effective Sept. 1, 2025, per {SRC['sb140']}. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} covers what to check with counsel.</p>"""),

            ("What to track, and a first 90 days", f"""<p>Judge every channel by cost per funded loan. Cost per lead tells you almost nothing in this business.</p>
<!--fig:funnel-->
<ol>
<li><b>Days 1 to 30.</b> Audit every profile and ad for NMLS and company disclosures. Fix your Google Business Profile with your name, company and NMLS ID. Build pages for HAP and TSAHC (if you’re approved) and your top two loan types. Set up call tracking and a CRM stage for each referral partner.</li>
<li><b>Days 31 to 60.</b> Launch one search campaign on program and loan-type keywords and one Meta campaign of educational videos. Book two agent education sessions. Start the past-client anniversary sequence.</li>
<li><b>Days 61 to 90.</b> Compare cost per application and cost per funded loan by source. Shift budget toward whatever is producing funded loans, and drop purchased leads if they aren’t pulling their weight after real follow-up.</li>
</ol>
<p>If you want a plan built around your license type, your referral partners and the programs you actually offer, <a href="/contact/">get in touch</a>. Tell us about your book and your goals, and a senior strategist will lay out what we’d do first.</p>"""),
        ],
        "faq": [
            ("How do mortgage loan officers get more leads?",
             "The leads that close best come from real estate agents, builders, financial professionals and past clients, so most of your effort should go into being easy to refer and staying in touch with past borrowers. Add educational content about local programs, Google search ads on program and loan-type keywords, and Meta video ads under the Financial Products and Services category. Purchased rate-shopper leads can work, but only with very fast follow-up."),
            ("Can a loan officer pay for a realtor’s marketing?",
             "Not in exchange for referrals. RESPA Section 8 bars giving or accepting anything of value under an agreement to refer settlement business, and there is no exception for small gifts. Joint advertising is generally handled by each party paying its fair share of the actual cost for the space it gets. Normal educational events not conditioned on referrals are permitted. Have your compliance team review any co-marketing arrangement."),
            ("Do Texas mortgage ads need an NMLS number?",
             "Yes. Texas SML rules require mortgage advertising to include the company name and NMLS ID, the company website if it has one, and the sponsored originator’s name and NMLS ID, with an exception for ads the company runs directly. On social media, you can meet the requirement by displaying the information prominently on your profile. Team names must appear with the company name and NMLS ID at substantially equivalent prominence."),
            ("What are Reg Z trigger terms in mortgage advertising?",
             "Under Regulation Z, stating a required down payment, the number of payments or repayment period, a payment amount or a finance charge amount triggers extra disclosures: the down payment, the repayment terms and the APR. Phrases like no down payment, low monthly payments or no closing costs do not trigger. If you state an interest rate, the APR must also appear and be at least as prominent."),
            ("Can I target by age or ZIP code in Facebook mortgage ads?",
             "No. Meta requires loan ads in the U.S. to run under the Financial Products and Services special ad category, which fixes age at 18 to 65+, includes all genders, removes ZIP code targeting, requires at least a 15-mile radius and blocks lookalike audiences. Google has similar limits for credit ads. Write specific creative, such as a video about one Houston program, so the right buyers recognize themselves."),
        ],
        "figures": {
            "leads": {
                "type": "compare",
                "title": "Rate-shopper leads vs. referral leads",
                "left": {"title": "Rate-shopper leads", "items": ["High volume, low trust", "Several lenders call within minutes", "Win on speed and price", "Low contact and close rates", "Cost per lead looks cheap"]},
                "right": {"title": "Referral leads", "items": ["Lower volume, borrowed trust", "Often the only lender they call", "Win on service and responsiveness", "Far higher close rates", "Cost per funded loan is lower"]},
                "alt": "Comparison of rate-shopper and referral mortgage leads for loan officers in Houston and Cypress",
                "caption": "Budget for both, but measure each by cost per funded loan.",
            },
            "respa": {
                "type": "checklist",
                "title": "Cleaner co-marketing habits",
                "sub": "Talk to compliance before any arrangement",
                "items": ["Pay your share of joint ads, based on the space you get", "Keep invoices for every shared cost", "Don’t pay for an agent’s signs, photos or open-house food", "No gifts to agents tied to referrals, at any value", "Keep agendas and sign-ins for education events", "Get counsel on builder preferred-lender deals", "Gifts to borrowers for their own loan are fine", "Never reward borrowers for referring others"],
                "alt": "Checklist of RESPA Section 8 co-marketing habits for mortgage loan officers working with Houston realtors and builders",
                "caption": f"Based on {SRC['respa']} and the CFPB’s 2020 FAQs. Not legal advice.",
            },
            "programs": {
                "type": "stats",
                "title": "Houston-area buyer programs at a glance",
                "stats": [["$75,000", "max City of Houston HAP forgivable loan"], ["80%", "AMI limit for most HAP buyers"], ["5%", "max TSAHC down payment assistance"], ["15%", "of yearly mortgage interest as an MCC tax credit"]],
                "note": "Source: City of Houston HAP Guidelines 8.0, TSAHC",
                "alt": "Stats on City of Houston HAP and TSAHC homebuyer assistance programs used in Houston mortgage marketing",
                "caption": "Check current guidelines before publishing; program terms change.",
            },
            "funnel": {
                "type": "funnel",
                "title": "What to count, from lead to funded loan",
                "stages": [["Inquiries (calls, forms, referrals)", "120"], ["Real conversations", "70"], ["Applications", "30"], ["Pre-approvals issued", "24"], ["Funded loans", "9"]],
                "note": "Illustrative example",
                "alt": "Funnel of mortgage leads to funded loans for a loan officer tracking marketing in Houston",
                "caption": "Track each stage by source. Referral and rate-shopper leads will look very different.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: funeral homes
    {
        "slug": "funeral-home-marketing-houston",
        "title": "Funeral Home Marketing in Houston: Pre-Need, Prices and Earning Trust Online",
        "seo_title": "Funeral Home Marketing in Houston: Pre-Need & Trust",
        "desc": "Funeral home marketing for Houston: pre-need campaigns, FTC and Texas price rules, reviews handled with care, obituary SEO and Spanish-speaking families.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Facebook", "Google"],
        "art": "b1",
        "hero": "care",
        "hero_alt": "Illustration representing care for funeral home marketing in Houston, Kingwood and The Woodlands",
        "related": ["hispanic-marketing-houston-spanish-ads-seo", "complete-guide-google-reviews", "facebook-instagram-ads-local-businesses"],
        "sections": [
            (None, f"""<p>Tuesday, 2:15 a.m. The on-call director at a family-owned funeral home in Kingwood takes a call from a hospice nurse. The family chose this home because their grandmother’s service was here in 2011, and they remember how they were treated.</p>
<p>At 3 a.m., one of the grandchildren is on her phone in the hospice parking lot, searching “cremation cost Houston” and reading reviews of three other places, because nobody in the family is sure what the grandmother wanted.</p>
<p>Both of those moments are funeral home marketing. The first is reputation built over decades. The second is a family comparing you online, at the worst hour of their year, on a phone.</p>
<p>For a Houston funeral home, the marketing that pays is mostly about the time before anyone is in crisis: pre-need planning that brings families to you while there’s room to think, a website that publishes prices and answers questions plainly, and Google reviews earned and answered with care. Obituary pages are the most-visited part of most funeral home sites, so they deserve real SEO attention. And Spanish-speaking families, a big part of Houston, should be served in their language. Below is how we’d approach it, with the federal and Texas rules that apply.</p>"""),

            ("At-need vs. pre-need: where marketing actually moves the numbers", f"""<p>At-need calls are decided by reputation, proximity, faith community and family history. Advertising can keep you visible, but a crass at-need ad does more harm than good, and most families in that moment call whoever they already trust.</p>
<p>Pre-need is different. Someone planning ahead has time to compare, attend a seminar, read your website and meet a counselor. That makes it marketable in the normal sense, and a pre-need contract today is usually your at-need family later.</p>
<p>The market keeps shifting under both. NFDA projected the U.S. cremation rate at 63.4% for 2025 and the burial rate at 31.6%, per {SRC['nfda_cb']}, and expects cremation to reach 82.3% by 2045, per {SRC['nfda_stats']}. NFDA’s 2023 price study put the national median for a funeral with viewing and burial at $8,300, and $6,280 for a funeral with viewing and cremation, per {SRC['nfda_cost']}.</p>
<!--fig:market-->
<p>That shift is a marketing problem. Families who choose cremation often assume it should be cheap and simple, then search for the lowest price online. Homes that explain the full range, from direct cremation to cremation with a memorial service and a gathering, keep those families. Homes that hide the options lose them to the cheapest listing on the map.</p>"""),

            ("Prices online: the FTC Funeral Rule and Texas requirements", f"""<p>The FTC Funeral Rule (16 CFR part 453) requires funeral providers to give consumers itemized price information, show price lists at specific points, provide prices by phone and give a statement of the goods and services selected, as summarized in {SRC['fr2026']}. Texas has its own versions. {SRC['occ651']} defines the retail price list as a printed or typewritten list and spells out what it must include, and {SRC['tac203']} requires accurate price answers by phone and printed lists for people who ask in person.</p>
<p>Neither the federal rule nor those Texas provisions requires posting prices on your website today. That may change. In October 2022 the FTC voted to issue an advance notice of proposed rulemaking that asked, among other things, whether funeral homes should have to post prices online, per {SRC['anpr']}. NFDA opposed a mandate. As of {SRC['starmark']}, online price posting still hadn’t been finalized into an enforceable requirement, and we haven’t seen a final rule since.</p>
<p>Our view: post your General Price List online anyway, along with plain-English package summaries. Families are already comparing on their phones. A home that shows prices looks confident and honest, and a home that hides them looks like it has something to hide, even when it doesn’t.</p>
<!--fig:prices-->
<p>A good pricing page has the downloadable GPL with its effective date, three or four common arrangements with a total (“direct cremation,” “cremation with memorial service,” “traditional funeral with burial”) and a sentence on what drives the difference. Add a phone number answered 24 hours a day. If you do post prices, keep them current; an outdated price list online is worse than none.</p>"""),

            ("Texas regulators and pre-need rules that shape your ads", f"""<p>Funeral homes and directors in Texas are licensed by {SRC['tfsc']}, which also requires establishments to give prospective customers its “Facts About Funerals” brochure when funeral services are discussed. The Commission warns consumers that some providers advertise in Texas without a Texas license, and it tells consumers to check the license database before paying. Put your license number and a link to that lookup on your website; it costs nothing and answers a question careful families are asking.</p>
<p>Pre-need is regulated separately. Per {SRC['dob']}, any funeral home or cemetery selling prepaid funeral goods or services in Texas must hold its own trust-funded permit from the Department of Banking or sell through a third party with a trust-funded or insurance-funded permit. The Commission’s consumer page notes that the Department of Banking oversees trust-funded contracts and the Texas Department of Insurance oversees insurance-funded ones.</p>
<p>For marketing, that means a few things:</p>
<ul>
<li>Say plainly how your pre-need plans are funded and who holds the permit. Families ask.</li>
<li>Have your permit holder or insurer review pre-need ad copy, mailers and seminar handouts before they go out. They often have their own rules.</li>
<li>Don’t promise “locked-in prices” or “guaranteed” anything unless your contract terms actually say so, in those words.</li>
</ul>"""),

            ("Marketing pre-need without being morbid", f"""<p>Pre-need marketing works when it treats planning as a kindness to the family, not a sales pitch.</p>
<p>What we see work for Houston-area homes:</p>
<ul>
<li><b>Planning seminars.</b> A free 45-minute session at a church hall, library branch or senior living community in The Woodlands, Sugar Land, Cypress or Pearland, with a practical title like “What your family needs to know: wills, VA benefits and funeral planning.” Invite an estate attorney or a VA benefits counselor to co-present.</li>
<li><b>A planning guide download.</b> A printable workbook that covers wishes, contacts, documents, music and readings. Offer it on your website and in Facebook ads. People who download it are your best pre-need leads.</li>
<li><b>Adult children.</b> A lot of pre-need decisions start with a 50-something daughter worried about her parents. Ads and content can speak to her (“Have you talked with your parents about their wishes?”).</li>
<li><b>Veterans.</b> Explain burial benefits and the Houston National Cemetery process clearly, and you’ll become the home veterans’ families recommend.</li>
<li>Direct mail still works with older households. Keep it plain, warm and specific, with an invitation to a seminar rather than a hard offer.</li>
</ul>
<p>Facebook is where to spend most of the paid budget for pre-need. {SRC['pew']} found 71% of U.S. adults use Facebook, and a majority of every age group uses it. Video works: a two-minute talk from your owner or pre-need counselor about why planning helps families will outperform any stock image. Use instant forms or a landing page to book seminar seats and planning appointments. Our {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads guide')} covers setup.</p>
<p>Avoid fear-based copy. “Don’t leave your family with a $9,000 bill” might get clicks, but it doesn’t fit a business that runs on trust, and it ages badly in a community where people talk.</p>"""),

            ("Google Business Profile and reviews, handled with care", f"""<p>Families searching at 3 a.m. look at the map first. Your Business Profile needs the right primary category (Funeral home), secondary categories for services you really offer such as cremation, real photos of the chapel, lobby and parking, accurate 24-hour phone information and a clear description of services. Our {L('/blog/rank-in-google-map-pack-houston/', 'guide to ranking in the Houston map pack')} covers the rest. Google’s Local Services Ads also include a “Funeral home” category, per {SRC['lsa']}, which some homes use for pre-need and cremation inquiries.</p>
<p>Reviews need a gentler process than most businesses use. Timing matters. Asking at the arrangement conference or right after the service is too soon. Two to four weeks later, with a handwritten card from the director and a printed QR code or short link, is about right. Many families are glad to write something once they’ve had time.</p>
<p>The rules are the same as everywhere: no incentives, no discouraging negative reviews and no asking only the families you think are happy, per {SRC['gpol']}. Ask everyone the same way.</p>
<p>Respond to every review, and keep the reply brief and personal. For a hard review, don’t argue about details of a family’s service in public:</p>
<p><i>“We’re very sorry your family’s experience fell short of what you expected during such a difficult time. I’d like to talk with you personally. Please call me directly at [number]. [Name], Funeral Director.”</i></p>
<p>Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("Obituary pages: your biggest SEO asset", f"""<p>Obituaries bring more visitors to a funeral home website than any other page, in every site we’ve looked at. People search the name of the person who died, find the obituary, read service details, sign the guestbook and send flowers. Each of those visitors is a local person who may one day need you.</p>
<!--fig:obits-->
<p>A few things matter:</p>
<ul>
<li><b>Host obituaries on your own domain.</b> If your obituaries live on a third-party platform’s subdomain, you may be giving away your best traffic. Ask your website provider exactly where they live and who gets the search credit.</li>
<li><b>Write a clear page title</b> with the full name, city and dates (“Maria Elena Garza, 1941–2026, Pasadena, TX”). That matches what people type.</li>
<li><b>Service details at the top:</b> date, time, address with a map link, livestream link, and whether flowers or donations are preferred.</li>
<li><b>Speed and mobile.</b> Most obituary visits are on phones. Compress photos and keep the page fast.</li>
<li><b>Gentle next steps.</b> A small, quiet “Planning ahead?” link at the bottom of each obituary is enough. Don’t put pop-ups on an obituary.</li>
</ul>
<p>Watch for scams. As {SRC['scam']}, scammers comment on funeral home Facebook posts with fake livestream links that lead to phishing pages, often using photos copied from obituaries. Post the official livestream link on the obituary page itself, say in the Facebook post that it’s the only official link, moderate comments, and tell families what to expect. Some homes now post that a service will not be streamed at all, which shuts the scam down.</p>
<p>Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} builds and fixes funeral home sites if your obituary system is holding you back.</p>"""),

            ("Serving Spanish-speaking families", f"""<p>Many Houston families speak Spanish at home, and funeral traditions in many Mexican, Central American and Catholic families come with specific expectations: a rosary or vigil, a funeral Mass, sometimes a novena, and for some families transport of the body to another country for burial.</p>
<p>Marketing to those families well isn’t about running a translated ad. It means:</p>
<ul>
<li>Bilingual staff who can handle an arrangement conference start to finish, named on the website.</li>
<li>Spanish pages written by a native speaker, not machine-translated: services, pricing, pre-need, and repatriation if you offer it.</li>
<li>Spanish-language Google Business Profile posts, Facebook content and review replies when the review is in Spanish.</li>
<li>Relationships with Catholic parishes and Spanish-language congregations, and with the funeral homes or consulates you work with abroad.</li>
</ul>
<p>Our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing guide for Houston')} goes deeper on Spanish SEO and ads.</p>"""),

            ("Community trust and measuring pre-need appointments", f"""<p>Funeral homes win by being known. The homes we see thriving across Houston, Humble, Tomball and Conroe still show up: hospice and nursing home relationships with real education for staff, church and veterans group events, grief support groups open to anyone, holiday remembrance services in December. None of that is an ad, and all of it is marketing.</p>
<p>For the parts you pay for, track them properly. Use separate call tracking numbers for Google, Facebook, direct mail and seminars (our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers setup), record every pre-need lead in one CRM with its source, and count:</p>
<ul>
<li>Planning guide downloads and seminar registrations</li>
<li>Pre-need appointments booked and held</li>
<li>Pre-need contracts written, by source</li>
<li>At-need calls from families who say they found you online</li>
</ul>
<!--fig:preneed-->
<p>Pre-need contracts are your clearest return on marketing. If a Facebook seminar campaign fills two sessions a month and each session produces three appointments, you can see what each contract cost and decide whether to scale it.</p>
<p>A first 90 days we’d recommend: post your GPL and package pages, fix your Business Profile and start the review card process in month one. Launch a planning guide and one seminar campaign in month two. In month three, rebuild obituary page titles and service details, and add Spanish pages if you serve those families.</p>
<p>If you want help putting a plan together that fits your home and your community, <a href="/contact/">get in touch</a>. Tell us about your home and your goals, and a senior strategist will build it with you.</p>"""),
        ],
        "faq": [
            ("How do funeral homes get more families?",
             "Most at-need families choose a funeral home based on reputation, location, faith community and past experience, so the long game is trust. The marketing that moves numbers is pre-need: planning seminars, a downloadable planning guide, Facebook video ads aimed at older adults and their grown children, and a website that answers questions and shows prices. Strong Google reviews and well-built obituary pages keep you visible when families search."),
            ("Do funeral homes have to post prices online?",
             "Not currently under federal rules or the Texas price list provisions. The FTC Funeral Rule requires itemized price lists in person and price information by phone, and Texas law requires printed price lists. The FTC opened a review in 2022 that asked whether online posting should be required, but it had not been finalized as of late 2026. Many homes post their General Price List online anyway because families compare on their phones."),
            ("Who regulates pre-need funeral contracts in Texas?",
             "The Texas Department of Banking oversees trust-funded prepaid funeral contracts, and the Texas Department of Insurance oversees insurance-funded ones. A funeral home or cemetery selling prepaid contracts must hold its own trust-funded permit or sell through a third party with a trust-funded or insurance-funded permit. Funeral homes and directors themselves are licensed by the Texas Funeral Service Commission."),
            ("How should a funeral home ask for Google reviews?",
             "Gently and consistently. Wait two to four weeks after the service, then send a handwritten card from the director with a short review link or QR code. Ask every family the same way, because Google prohibits incentives, discouraging negative reviews and asking only happy customers. Reply to every review briefly and personally, and invite anyone with a complaint to call the director directly rather than discussing details publicly."),
            ("Are obituary pages good for funeral home SEO?",
             "Yes. Obituaries are usually the most visited pages on a funeral home website, because people search for the name of someone who died. Host them on your own domain, use the full name, city and years in the page title, put service details and the official livestream link at the top, and keep pages fast on phones. Moderate social comments to block fake livestream scam links."),
        ],
        "figures": {
            "market": {
                "type": "bars",
                "title": "U.S. cremation keeps climbing",
                "sub": "NFDA projections",
                "items": [["Cremation rate, 2025", 63.4, "63.4%"], ["Burial rate, 2025", 31.6, "31.6%"], ["Cremation rate, 2045 projection", 82.3, "82.3%"]],
                "highlight": [0],
                "note": "Source: NFDA 2025 Cremation & Burial Report",
                "alt": "Bar chart of NFDA cremation and burial rate projections relevant to funeral home marketing in Houston",
                "caption": f"From {SRC['nfda_cb']} and {SRC['nfda_stats']}.",
            },
            "prices": {
                "type": "compare",
                "title": "Hiding prices vs. posting them",
                "left": {"title": "“Call us for pricing”", "items": ["Family assumes the worst", "Lowest-price competitor gets the call", "Phone time spent on basic quotes", "Looks out of step with FTC direction", "Cremation families leave the site"]},
                "right": {"title": "GPL and packages online", "items": ["Family sees options and totals", "Calls come in already informed", "Arrangement time goes to the family", "Ready if online posting becomes required", "Cremation options explained in full"]},
                "alt": "Comparison of hiding versus posting funeral prices online for funeral homes in Houston and The Woodlands",
                "caption": "Keep any posted price list current, with its effective date.",
            },
            "obits": {
                "type": "checklist",
                "title": "Obituary page checklist",
                "sub": "For funeral home SEO and families",
                "items": ["Hosted on your own domain", "Full name, city and years in the title", "Service date, time and map link up top", "Official livestream link, or a note there isn’t one", "Flowers or donations preference", "Guestbook that you moderate", "Fast on phones, compressed photos", "One quiet planning-ahead link, no pop-ups"],
                "alt": "Checklist for obituary page SEO for funeral homes in Houston, Kingwood and The Woodlands",
                "caption": "The page has to work for a grieving family first and for Google second.",
            },
            "preneed": {
                "type": "funnel",
                "title": "Tracking a pre-need seminar campaign",
                "stages": [["People reached on Facebook", "18,000"], ["Seminar registrations", "45"], ["Attendees", "30"], ["Planning appointments held", "9"], ["Pre-need contracts", "4"]],
                "note": "Illustrative example",
                "alt": "Funnel tracking a pre-need planning seminar campaign for a funeral home in Houston",
                "caption": "Count contracts by source so you know which seminars and ads earn their cost.",
            },
        },
    },
]
