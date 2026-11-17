"""Batch 13 (module e): a 2027 month-by-month marketing plan for Houston small businesses, and how Local Services Ads
lead credits, ratings and the move into Google Ads actually work in late 2026.

Research, plan post: 93Q Country and Click2Houston on RODEOHOUSTON 2027 (March 2-21, 2027; Downtown Rodeo Parade
Feb. 27, 2027); Conroe ISD's adopted 2026-27 calendar PDF (spring break March 15-19, 2027; last day May 27);
Community Impact on Cy-Fair ISD's 2026-27 calendar (same spring break, last day May 27); My Neighborhood News on
CFISD's 2027-28 calendar (first day Aug. 11, 2027, approved Nov. 9, 2026); ABC13 on the 2027 Chevron Houston
Marathon (Jan. 17, 2027); NOAA's 2026 outlook release (season June 1 to November 30); Texas Comptroller publication
98-490 (2027 sales tax holiday Aug. 6-8) and 98-1017 (2026 emergency supplies holiday April 25-27); Google's May 20,
2026 ads blog post on AI Mode formats; PPC Land on Google Marketing Live 2026 (AI Max requirement, DSA upgrade in
September 2026) and on Chrome retiring Privacy Sandbox (Oct. 17, 2025; third-party cookies kept April 22, 2025);
Texas Attorney General's TDPSA page; Morgan Lewis on Texas SB 140; Google Ads help on the LSA transition.
Research, LSA post: Google help pages "How leads work" (7195435), lead credits (7435486, 15100654), invalid lead
troubleshooter (11390630), LSA transition to Performance Max pay-per-lead goals (17213585), pay-per-lead goals
(17325249), best practices (17326561), campaign settings (17325051), ad rankings (7527305), LSA bidding (10125017),
managing leads (6224859), call recording settings (16913427), AI-qualified call leads (16913326); Search Engine Land
and Search Engine Roundtable on automated credits (2024) and lead-quality complaints (Feb. 2025); PPC Land on the
lead-rating survey and bonus-credit outcomes, and on dashboard access ending at migration; Search Engine Journal on
the migration (July 20, 2026).
Not used (unverified): exact 2027 dates for the April emergency-supplies tax holiday, Houston-area 2027-28 calendars
other than Cy-Fair, any published cap on LSA bonus credits, and Google's full legacy "valid lead" policy text beyond
what the help pages above state.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # plan post
    "rodeo": A("https://93qcountry.com/1705006/2027-houston-livestock-show-and-rodeo-dates/", "93Q Country’s rundown of the 2027 dates"),
    "parade": A("https://www.click2houston.com/news/local/2026/10/29/the-voice-of-rodeohouston-named-as-2027-downtown-parade-grand-marshal/", "Click2Houston"),
    "cisd": A("https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5052/Cisd/e83881e1-1d85-43d1-b350-7fb41cffd1c1/26-27-CISD-Calendar.pdf", "Conroe ISD’s 2026-27 calendar"),
    "cfisd": A("https://communityimpact.com/cypress/education/cy-fair-isd-students-staff-to-get-fall-break-in-2026/", "Community Impact on Cy-Fair ISD’s calendar"),
    "cfisd28": A("https://myneighborhoodnews.com/cfisd-board-approves-2027-2028-school-calendar-first-day-of-school-fall-break-thanksgiving-and-key-dates-for-cypress-fairbanks-families", "approved in November 2026"),
    "marathon": A("https://abc13.com/post/chevron-houston-marathon-2027-what-know-plan-run-full-race-aramco-half-are-5k/19221034/", "ABC13"),
    "noaa": A("https://www.noaa.gov/news-release/noaa-predicts-below-normal-2026-atlantic-hurricane-season", "NOAA"),
    "taxhol": A("https://comptroller.texas.gov/taxes/publications/98-490/", "the Texas Comptroller"),
    "emerg": A("https://comptroller.texas.gov/taxes/publications/98-1017.php", "emergency-supplies tax holiday"),
    "gads_ai": A("https://blog.google/products/ads-commerce/a-new-generation-of-ads-for-the-ai-era-of-search/", "Google’s May 2026 announcement"),
    "gml": A("https://ppc.land/google-marketing-live-2026-every-announcement-that-actually-matters", "PPC Land’s Google Marketing Live recap"),
    "sandbox": A("https://ppc.land/chrome-kills-most-privacy-sandbox-technologies-after-adoption-fails/", "PPC Land"),
    "tdpsa": A("https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act", "the Texas Attorney General"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    # LSA post
    "leads": A("https://support.google.com/google-ads/answer/7195435?hl=en", "Google’s “How leads work” page"),
    "credits": A("https://support.google.com/google-ads/answer/7435486", "Google’s lead credit page"),
    "auto": A("https://support.google.com/localservices/answer/15100654?hl=en", "Google’s automated credits page"),
    "trouble": A("https://support.google.com/localservices/troubleshooter/11390630?hl=en", "Google’s invalid-lead troubleshooter"),
    "move": A("https://support.google.com/google-ads/answer/17213585", "Google’s transition guide"),
    "ppl": A("https://support.google.com/google-ads/answer/17325249?hl=en", "Google’s pay-per-lead goals page"),
    "best": A("https://support.google.com/google-ads/answer/17326561?hl=en", "Google’s pay-per-lead best practices"),
    "settings": A("https://support.google.com/google-ads/answer/17325051", "Google’s campaign settings page"),
    "rank": A("https://support.google.com/localservices/answer/7527305?hl=en", "Google’s ad ranking page"),
    "bid": A("https://support.google.com/localservices/answer/10125017?hl=en", "Google’s LSA bidding page"),
    "manage": A("https://support.google.com/localservices/answer/6224859?hl=en", "Google’s lead management page"),
    "rec": A("https://support.google.com/google-ads/answer/16913427", "Google’s call recording settings page"),
    "aiq": A("https://support.google.com/google-ads/answer/16913326", "AI-qualified call leads"),
    "sel": A("https://searchengineland.com/google-automates-lead-credits-local-services-ads-443468", "Search Engine Land"),
    "ser": A("https://www.seroundtable.com/google-lsa-lead-quality-drops-38884.html", "Search Engine Roundtable"),
    "rating": A("https://ppc.land/lead-rating/", "PPC Land’s breakdown of the rating survey"),
    "access": A("https://ppc.land/google-local-services-advertisers-lose-dashboard-access-14-days-after-email/", "PPC Land"),
    "sej": A("https://www.searchenginejournal.com/google-is-bringing-local-service-ads-into-google-ads/582816/", "Search Engine Journal"),
}

PLAN = "/blog/marketing-plan-2027-small-business-houston/"
LSA = "/blog/local-services-ads-lead-disputes-credits/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: 2027 marketing plan
    {
        "slug": "marketing-plan-2027-small-business-houston",
        "title": "2027 Marketing Plan for Houston Small Businesses: A Month-by-Month Template",
        "seo_title": "2027 Marketing Plan Template for Houston Small Businesses",
        "desc": "A 2027 marketing plan for Houston small businesses: budget split, a 12-month calendar with rodeo, spring break and hurricane dates, KPIs and a one-page plan.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b5",
        "hero": "growth",
        "hero_alt": "Illustration of a growth chart for a 2027 marketing plan for small businesses in Houston and The Woodlands",
        "related": ["2026-local-marketing-game-plan-woodlands", "set-a-marketing-budget-small-business", "seasonal-marketing-greater-houston"],
        "sections": [
            (None, f"""<p>The second week of December, a little after 9 p.m. The owner of a plumbing company in Spring has last year’s P&amp;L open in one tab and a blank spreadsheet in the other. The 2026 “plan” was a sticky note: post more, boost a few things, maybe try those Google boxes. It went fine. March was a scramble, July was great, and October was quiet enough that he paid two techs to sit in the shop.</p>
<p>He doesn’t need a 40-page strategy deck. He needs to know what to spend each month, what it should produce, and which weeks in Houston will make or break the year.</p>
<p>That’s what this template is. A 2027 marketing plan for a Houston-area small business comes down to five decisions: an annual budget, a split across always-on, demand-capture and demand-creation work, a month-by-month calendar weighted to your real seasonality, four quarterly goals, and a short list of numbers you check every month. Everything below fits on one page when you’re done.</p>
<p>If you read our {L('/blog/2026-local-marketing-game-plan-woodlands/', '2026 local marketing priorities')}, this is the next layer down: dates, dollars and the changes that landed in 2026. For how to pick the total number in the first place, start with {L('/blog/set-a-marketing-budget-small-business/', 'how to set a marketing budget')}. We won’t repeat either here.</p>"""),

            ("Step 1: split the budget before you pick channels", f"""<p>Most small business plans start with channels. “We should do TikTok.” Start with the money instead, and divide it into four buckets that do different jobs.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Bucket</th><th>What it pays for</th><th>Illustrative share</th><th>Cut it when</th></tr></thead>
<tbody>
<tr><td><b>Base</b> (always on)</td><td>Website hosting and fixes, Google Business Profile upkeep, review requests, call tracking, CRM, email platform</td><td>15% to 25%</td><td>Never. This is the plumbing everything else runs through.</td></tr>
<tr><td><b>Capture</b> (people already looking)</td><td>Google Search ads, pay-per-lead (formerly Local Services Ads), local SEO, Microsoft Ads for some trades</td><td>40% to 55%</td><td>Cost per booked job rises for two straight months with no seasonal reason</td></tr>
<tr><td><b>Create</b> (people not looking yet)</td><td>Meta and Instagram, TikTok, YouTube, streaming TV, mailers, sponsorships</td><td>15% to 30%</td><td>You can’t staff the work capture is already sending</td></tr>
<tr><td><b>Test</b></td><td>One new channel or offer per quarter, with a stop date</td><td>5% to 10%</td><td>The stop date arrives and it hasn’t earned a second quarter</td></tr>
</tbody></table></div>
<p>The shares are our starting point for a local service business, not a benchmark. A restaurant or boutique flips capture and create, because nobody searches “new brunch spot” the way they search “water heater repair Spring TX.” A CPA firm might put almost everything in capture and referrals.</p>
<!--fig:split-->
<p>Then spread the annual number across the months using a seasonality index. Give each month a weight based on your last two years of revenue or leads, make the 12 weights add up to 100, and multiply. A $60,000 year with July weighted at 11 gets $6,600 in July. January at 6 gets $3,600. Simple, and it stops you from spending evenly into a lopsided year.</p>
<!--fig:season-->
<p>One rule we hold to: spend ramps up two to four weeks before demand does. Google’s ad systems need a little time to settle after a budget jump, and your best-ranking competitors are already there when the first heat wave or the first freeze hits.</p>"""),

            ("The Houston dates that shape 2027", f"""<p>Generic marketing calendars are built around national holidays. Houston has its own calendar, and three stretches of it matter more than any of those holidays for most local businesses.</p>
<p><b>Rodeo season.</b> RODEOHOUSTON runs March 2 to March 21, 2027 at NRG Park, back to a 20-day format, per {SRC['rodeo']}. The Downtown Rodeo Parade is Saturday, February 27, per {SRC['parade']}. For restaurants, bars, boot and western-wear shops, hotels near NRG and anyone selling to the visitors, that’s your Super Bowl. For many service businesses it’s a distraction: three weeks when half your customers’ evenings are spoken for.</p>
<p><b>Spring break lands inside the last week of rodeo.</b> Conroe ISD’s break is March 15 to 19, 2027, per {SRC['cisd']}, and Cy-Fair ISD’s is the same week, per {SRC['cfisd']}. Check your own district (Katy, Klein, Tomball, Humble and Houston ISD set their own). That week, family-entertainment, tutoring camps, pet boarding and travel-adjacent businesses get busy, and appointment-based businesses see no-shows climb.</p>
<p><b>Hurricane season</b> runs June 1 to November 30, per {SRC['noaa']}. Restoration, roofing, tree service, generator installers and insurance agents should have storm pages and paused ad groups built in May, ready to switch on the same afternoon. Everyone else needs a plan for the opposite: pausing promotions, swapping creative and posting real hours when the power’s out.</p>
<!--fig:dates-->
<p>Smaller dates worth putting on the plan now: the Chevron Houston Marathon on January 17, 2027 ({SRC['marathon']} expects about 40,000 participants across race weekend), the last day of school on May 27 in both Conroe ISD and Cy-Fair ISD, Texas’ sales tax holiday from August 6 to 8, 2027, according to {SRC['taxhol']}, and Cy-Fair’s first day of the 2027-28 school year on August 11, a calendar {SRC['cfisd28']}. The state also runs an {SRC['emerg']} each spring; it was April 25 to 27 in 2026, so watch for the 2027 announcement if you sell generators, batteries or storm gear.</p>"""),

            ("The 12-month calendar", f"""<p>Here’s the template. Copy the rows you need, delete the rest, and add your own dates (your anniversary sale, your busiest week last year, the week your lease renews).</p>
<div class="bp-tbl"><table>
<thead><tr><th>Month</th><th>Houston dates for 2027</th><th>What to run</th><th>Most relevant for</th></tr></thead>
<tbody>
<tr><td>January</td><td>Marathon weekend Jan. 13-17; new-year resolutions</td><td>Review requests from December customers, new-year offers, set up the year’s tracking</td><td>Fitness, med spas, dental, financial and tax pros</td></tr>
<tr><td>February</td><td>Valentine’s Day (Sun., Feb. 14); parade Feb. 27; freeze risk</td><td>Gift cards and date-night offers; freeze and pipe pages ready to go live</td><td>Restaurants, florists, salons, plumbers</td></tr>
<tr><td>March</td><td>RODEOHOUSTON Mar. 2-21; spring break Mar. 15-19 (Conroe and Cy-Fair ISD); Easter Mar. 28</td><td>Rodeo tie-ins if your customers go; otherwise ride capture and keep creative spend light</td><td>Hospitality, retail, family entertainment</td></tr>
<tr><td>April</td><td>Emergency-supplies tax holiday (late April, confirm dates); spring projects</td><td>Spring home-project pushes; hurricane-prep content drafted</td><td>Remodelers, landscapers, pool, HVAC tune-ups</td></tr>
<tr><td>May</td><td>Mother’s Day May 9; graduations; last day of school May 27; Memorial Day May 31</td><td>AC and pool season ramps; summer camp and program enrollment; storm ad groups built and paused</td><td>HVAC, pool, camps, restaurants</td></tr>
<tr><td>June</td><td>Hurricane season starts June 1; Juneteenth (Sat., June 19); Father’s Day June 20</td><td>Peak budget for heat-driven trades; storm-prep messaging</td><td>HVAC, roofing, restoration, insurance</td></tr>
<tr><td>July</td><td>July 4 (Sunday); peak heat</td><td>Hold capture budgets; members-only and loyalty offers for slow-season businesses</td><td>HVAC, plumbing, electrical; restaurants fight the slump</td></tr>
<tr><td>August</td><td>Sales tax holiday Aug. 6-8; Cy-Fair ISD starts Aug. 11</td><td>Back-to-school offers, after-school programs, fall enrollment</td><td>Retail, tutoring, dance, martial arts, pediatric care</td></tr>
<tr><td>September</td><td>Labor Day Sept. 6; hurricane season continues</td><td>Fall reset: new creative, retarget summer customers, Q4 offers locked</td><td>Fitness, home services, professional services</td></tr>
<tr><td>October</td><td>Halloween (Sun., Oct. 31); cooler weekends start</td><td>Holiday party and catering bookings open; HVAC heating tune-ups</td><td>Venues, caterers, HVAC, event businesses</td></tr>
<tr><td>November</td><td>Thanksgiving Nov. 25; Black Friday Nov. 26; Small Business Saturday Nov. 27; Cyber Monday Nov. 29; hurricane season ends Nov. 30</td><td>Gift cards, holiday offers, email to past customers, review requests</td><td>Retail, restaurants, salons and spas</td></tr>
<tr><td>December</td><td>Holiday parties; year-end spending</td><td>Year-end service pushes, 2028 plan drafted, tracking audit</td><td>Most businesses</td></tr>
</tbody></table></div>
<p>We keep a longer seasonal breakdown in {L('/blog/seasonal-marketing-greater-houston/', 'our guide to Houston’s marketing seasons')} and {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing in The Woodlands')}, and {L('/blog/holiday-marketing-checklist/', 'a holiday checklist')} for November and December.</p>"""),

            ("Quarterly goals that actually steer the year", f"""<p>Monthly tasks keep you busy. Quarterly goals tell you whether the busy-ness is working. Write one outcome per quarter, with a number attached, and one “fix” project that makes the next quarter cheaper.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Quarter</th><th>Outcome goal (example)</th><th>Fix project</th><th>Houston factor</th></tr></thead>
<tbody>
<tr><td>Q1 (Jan-Mar)</td><td>Hit January-March booked jobs at last year’s level or better, with 10% less spend per job</td><td>Call tracking and CRM sources cleaned up so every lead has a source</td><td>Rodeo and spring break pull attention in March</td></tr>
<tr><td>Q2 (Apr-Jun)</td><td>Grow new customers 15% over Q2 2026</td><td>Storm and heat landing pages built; review volume doubled</td><td>Heat starts in May; hurricane season June 1</td></tr>
<tr><td>Q3 (Jul-Sep)</td><td>Hold cost per booked job flat at peak demand</td><td>Retention: reminder and win-back emails or texts switched on</td><td>Peak storm months; back to school in August</td></tr>
<tr><td>Q4 (Oct-Dec)</td><td>Fill the slow months with past customers (target: 30% of Q4 revenue from repeat buyers)</td><td>2028 plan drafted from real numbers</td><td>Holiday weekends; hurricane season ends Nov. 30</td></tr>
</tbody></table></div>
<p>The numbers in that table are examples. Use yours. If you don’t have last year’s numbers by quarter, Q1’s fix project is getting them.</p>"""),

            ("Channel mix by business type", f"""<p>The split from Step 1 tells you how much. This table tells you where, as a starting mix we’d sketch for a single-location business in The Woodlands, Katy or Sugar Land before seeing its data.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Business type</th><th>Lead with</th><th>Support with</th><th>Usually skip at first</th></tr></thead>
<tbody>
<tr><td>Home services (HVAC, plumbing, roofing, pest)</td><td>Google Search ads, pay-per-lead campaigns, Google Business Profile and reviews</td><td>Meta retargeting, Nextdoor, yard signs and wraps</td><td>Broad awareness video</td></tr>
<tr><td>Restaurants and bars</td><td>Google Business Profile, Instagram and TikTok, email and SMS to regulars</td><td>Meta ads around events and launches, local creators</td><td>Search ads beyond brand and catering</td></tr>
<tr><td>Health, dental, med spa, chiropractic</td><td>Search ads, Business Profile, reviews</td><td>Meta and Instagram for elective services, email</td><td>Pay-per-lead (no lead credits in health care)</td></tr>
<tr><td>Professional services (CPA, law, financial)</td><td>Search, referrals, a site that answers real questions</td><td>LinkedIn, email newsletter, local sponsorships</td><td>TikTok</td></tr>
<tr><td>Retail and boutiques</td><td>Instagram and Meta, Google Business Profile with products, email</td><td>Google Shopping and local inventory, creators</td><td>Generic search terms</td></tr>
<tr><td>Fitness and studios</td><td>Meta and Instagram, Business Profile, referral offers</td><td>Search for class types, January and September pushes</td><td>Print</td></tr>
</tbody></table></div>
<p>Two notes on that table. The health care line is based on Google’s own credit rules, which we cover in the {L(LSA, 'Local Services Ads disputes and credits guide')}. And “skip at first” means until the core channels are tracked and profitable, not forever. If you want help with the search side, that’s {L('/services/search-marketing/', 'our search marketing team')}; for social, {L('/services/paid-social-advertising/', 'paid social')}.</p>"""),

            ("What changed going into 2027", f"""<p>Four shifts from 2026 belong in your plan. We’ve kept this to what we could verify.</p>
<p><b>Google’s search ads are moving into AI answers.</b> On May 20, 2026, Google said it was testing new ad formats inside AI Mode, including ads that answer a specific question and “Highlighted Answers” that can appear in AI Mode’s recommendation lists, per {SRC['gads_ai']}. According to {SRC['gml']}, those placements require AI Max for Search or Performance Max, and Dynamic Search Ads were set to upgrade to AI Max automatically in September 2026. For a small business, the practical move is to keep a well-run Search campaign with good conversion tracking, and to make sure your website plainly answers the questions customers ask. We wrote about the organic side in {L('/blog/ai-overviews-local-search-houston/', 'AI Overviews and local search')} and {L('/blog/show-up-in-chatgpt-ai-search-aeo/', 'showing up in AI search')}.</p>
<p><b>Local Services Ads now live inside Google Ads.</b> Starting in August 2026, Google began moving LSA accounts into Google Ads as Performance Max campaigns with pay-per-lead goals, with later phases in late 2026 and 2027, per {SRC['move']}. Manual bidding is gone, budgets are daily instead of weekly, and old performance reports don’t transfer. Export yours before your migration date. Budget lines in your plan that said “LSA” now sit inside Google Ads, which makes it easier to compare cost per lead side by side with regular search.</p>
<!--fig:changes-->
<p><b>Cookies stayed, but measurement still runs on your own data.</b> Google decided in April 2025 to keep third-party cookies in Chrome, then in October 2025 retired most Privacy Sandbox ad technologies, per {SRC['sandbox']}. That removed a deadline without fixing the underlying problem: browsers, phones and consent banners still drop a lot of tracking. Plan for first-party measurement: tracked phone numbers, forms that pass the lead source into your CRM, and offline conversion uploads. Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} walks through the setup.</p>
<p><b>Texas privacy and texting rules apply to more of your marketing than you think.</b> The Texas Data Privacy and Security Act took effect July 1, 2024. Small businesses as defined by the SBA are generally exempt, but even a small business must get consent before selling a consumer’s sensitive data, per {SRC['tdpsa']}. Separately, SB 140 brought marketing text messages under Texas’ telephone solicitation law as of September 1, 2025, with exemptions that may or may not cover you, per {SRC['sb140']}. If texting past customers is in your Q3 retention plan, get clear opt-in and ask your attorney before launch. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'SMS marketing rules post')} has more.</p>"""),

            ("The KPIs to put on the plan", f"""<p>Pick five or six numbers and check them on the same day each month. More than that and nobody looks.</p>
<div class="bp-tbl"><table>
<thead><tr><th>KPI</th><th>Why it matters</th><th>Where it comes from</th></tr></thead>
<tbody>
<tr><td>Booked jobs or new customers</td><td>The outcome. Leads are only a step toward it.</td><td>CRM, booking system, POS</td></tr>
<tr><td>Cost per booked job (or per new customer)</td><td>The one number that lets you compare Google, Meta and pay-per-lead fairly</td><td>Ad spend divided by booked jobs by source</td></tr>
<tr><td>Lead-to-booking rate</td><td>Separates a marketing problem from a phone-answering problem</td><td>Call tracking, CRM</td></tr>
<tr><td>Speed to first response</td><td>Slow replies lose jobs and, on pay-per-lead, hurt your ranking</td><td>CRM timestamps, call logs</td></tr>
<tr><td>New Google reviews per month and average rating</td><td>Drives map rankings and the click</td><td>Google Business Profile</td></tr>
<tr><td>Repeat customer share of revenue</td><td>Tells you whether retention is paying for itself</td><td>CRM or POS</td></tr>
</tbody></table></div>
<p>If speed to response looks bad, start with {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'our speed-to-lead guide')} before buying more leads. And for setting targets, {L('/blog/measure-marketing-success-metrics/', 'measuring marketing success')} goes further than we can here.</p>
<!--fig:review-->"""),

            ("The one-page plan", f"""<p>Fill this in and tape it to the wall. If a row is blank, that’s your first task of January.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line</th><th>Your 2027 answer</th><th>Example (illustrative HVAC company, Spring and The Woodlands)</th></tr></thead>
<tbody>
<tr><td>Revenue or customer goal</td><td>&nbsp;</td><td>600 new customers; 35% of revenue from repeat customers</td></tr>
<tr><td>Annual marketing budget</td><td>&nbsp;</td><td>$60,000</td></tr>
<tr><td>Split (base / capture / create / test)</td><td>&nbsp;</td><td>20% / 50% / 22% / 8%</td></tr>
<tr><td>Core offer</td><td>&nbsp;</td><td>Same-day AC repair; $X tune-up in April and October</td></tr>
<tr><td>Q1 focus</td><td>&nbsp;</td><td>Tracking cleanup; heating and freeze calls; reviews</td></tr>
<tr><td>Q2 focus</td><td>&nbsp;</td><td>AC ramp from early May; storm pages built</td></tr>
<tr><td>Q3 focus</td><td>&nbsp;</td><td>Peak capture; maintenance-plan sign-ups</td></tr>
<tr><td>Q4 focus</td><td>&nbsp;</td><td>Past-customer email; heating tune-ups; 2028 plan</td></tr>
<tr><td>Lead channels</td><td>&nbsp;</td><td>Google Search, pay-per-lead, Business Profile, Meta retargeting</td></tr>
<tr><td>Test of the year</td><td>&nbsp;</td><td>Streaming TV in Montgomery County, Q2 only</td></tr>
<tr><td>Monthly KPIs</td><td>&nbsp;</td><td>Booked jobs, cost per booked job, speed to response, reviews</td></tr>
<tr><td>Owner and review date</td><td>&nbsp;</td><td>Owner plus office manager, first Tuesday of each month</td></tr>
</tbody></table></div>
<!--fig:steps-->"""),

            ("Mistakes we see in small business plans", f"""<ul>
<li><b>Even monthly budgets.</b> A pool company spending the same in January and June is overpaying in one and starving the other.</li>
<li><b>No stop dates on tests.</b> A channel tried “for a while” never gets judged. Put the end date in the plan when you start it.</li>
<li><b>Planning around national holidays only.</b> In Houston, rodeo, spring break and storm season move more money than Presidents’ Day does.</li>
<li><b>Lead counts as the scoreboard.</b> A month with 120 leads and 9 jobs is worse than a month with 40 leads and 15 jobs. Track all the way to booked work.</li>
<li><b>No room for a storm.</b> Every Houston plan needs a line for what happens if a hurricane, a freeze or a long outage hits: what pauses, what turns on and who posts updates.</li>
<li><b>Writing the plan once.</b> Re-forecast at the end of each quarter. A plan that doesn’t change after real data comes in is a wish list.</li>
</ul>
<p>If you’d like a second set of eyes, tell us about your business and what you want 2027 to look like, and a senior strategist will build a custom plan with you. Just <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I make a marketing plan for a small business in 2027?",
             "Start with an annual budget, then split it into always-on basics, demand capture like search ads, demand creation like social ads, and a small test budget. Spread it across the months using your own seasonality, set one measurable goal per quarter, and choose five or six KPIs to check monthly. For a Houston business, add local dates like rodeo season, spring break and hurricane season."),
            ("When is RODEOHOUSTON in 2027?",
             "The 2027 Houston Livestock Show and Rodeo runs March 2 through March 21 at NRG Park, returning to a 20-day format. The Downtown Rodeo Parade is Saturday, February 27, 2027. Several large districts, including Conroe ISD and Cy-Fair ISD, have spring break March 15 to 19, which falls inside the rodeo’s final week, so plan family-focused promotions and staffing around that overlap."),
            ("How should a small business split its marketing budget?",
             "One practical method is four buckets: 15% to 25% for always-on basics like your website, Google Business Profile, reviews and tracking; 40% to 55% for capturing people already searching; 15% to 30% for reaching people not yet looking; and 5% to 10% for one test per quarter. Those shares are a starting point for local service businesses. Adjust them for your own industry and results."),
            ("What marketing changes should small businesses plan for in 2027?",
             "Google began moving Local Services Ads into Google Ads as pay-per-lead Performance Max campaigns in August 2026, with more accounts following into 2027. Google is also testing ads inside AI Mode answers. Chrome kept third-party cookies but tracking gaps remain, so first-party measurement matters. Texas privacy and texting rules, including SB 140 for marketing texts, also deserve a check with your attorney."),
            ("When is the Texas sales tax holiday in 2027?",
             "According to the Texas Comptroller, the 2027 sales tax holiday runs from Friday, August 6 through midnight Sunday, August 8. Qualifying clothing, footwear, school supplies and backpacks under the price limit are exempt. Retailers and businesses selling to families should plan back-to-school promotions and ad budgets around that weekend, along with local school start dates in the second week of August."),
        ],
        "figures": {
            "split": {
                "type": "bars",
                "title": "An example budget split for a $60,000 year",
                "sub": "Local service business, midpoints of the ranges in the table",
                "items": [["Capture (search, pay-per-lead, SEO)", 30000, "$30,000"], ["Create (social, video, mail)", 13200, "$13,200"], ["Base (site, profile, tracking)", 12000, "$12,000"], ["Test (one per quarter)", 4800, "$4,800"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of an example 2027 marketing budget split for a Houston small business across capture, create, base and test",
                "caption": "Fund the base first, then capture. Creation and tests get what’s left.",
            },
            "season": {
                "type": "columns",
                "title": "Weight the months, not just the year",
                "sub": "Example seasonality index for a Houston HVAC company (peak month = 100)",
                "labels": ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"],
                "values": [55, 55, 64, 73, 91, 100, 100, 100, 82, 64, 64, 64],
                "highlight": [4, 5, 6, 7],
                "y_label": "Relative budget",
                "note": "Illustrative example. Build yours from two years of your own leads or revenue.",
                "alt": "Column chart of an example monthly marketing budget index for a Houston and The Woodlands HVAC business in 2027",
                "caption": "Spend ramps in May, two to four weeks before the heat drives calls.",
            },
            "dates": {
                "type": "stats",
                "title": "Houston dates to plan 2027 around",
                "stats": [["Mar 2-21", "RODEOHOUSTON at NRG Park"], ["Mar 15-19", "Spring break, Conroe and Cy-Fair ISD"], ["Jun 1-Nov 30", "Atlantic hurricane season"], ["Aug 6-8", "Texas sales tax holiday"]],
                "note": "Sources: 93Q Country, Conroe ISD, Community Impact, NOAA, Texas Comptroller",
                "alt": "Key 2027 dates for Houston small business marketing plans: rodeo, spring break, hurricane season and the sales tax holiday",
                "caption": "Check your own school district; spring break dates vary across Greater Houston.",
            },
            "changes": {
                "type": "compare",
                "title": "A 2026 plan vs. a 2027 plan",
                "left": {"title": "Last year’s habits", "items": ["LSA managed in its own dashboard", "Max per-lead bids set by hand", "Keyword-only search campaigns", "Waiting on a cookie deadline", "Texts sent to anyone who called once"]},
                "right": {"title": "What 2027 needs", "items": ["Pay-per-lead campaigns inside Google Ads", "Daily budgets and automated bidding", "Search set up for AI Mode placements", "First-party tracking: calls, forms, CRM", "Documented opt-in for marketing texts"]},
                "alt": "Comparison of 2026 and 2027 marketing plan habits for Houston small businesses, covering Google Ads, tracking and texting",
                "caption": "Most of the change is plumbing: where campaigns live and how results get measured.",
            },
            "review": {
                "type": "checklist",
                "title": "The monthly plan review",
                "sub": "First week of every month, about 45 minutes",
                "items": ["Booked jobs vs. goal, by source", "Cost per booked job, by channel", "Lead-to-booking rate and missed calls", "New reviews and replies posted", "Next month’s dates and offers confirmed", "Budget shifted toward what booked work", "Test channel: keep, change or stop"],
                "alt": "Checklist for a monthly marketing plan review for small businesses in Houston and The Woodlands",
                "caption": "Same day, same numbers, every month. That’s most of the discipline.",
            },
            "steps": {
                "type": "steps",
                "title": "Build the 2027 plan in an afternoon",
                "sub": "The order we use with Houston-area owners",
                "steps": [["Set the number", "Annual budget from revenue goals and past results."], ["Split it", "Base, capture, create, test."], ["Weight the months", "Seasonality index from your own data."], ["Add Houston dates", "Rodeo, spring break, storms, school."], ["Pick KPIs", "Five or six, checked monthly."], ["Re-forecast", "End of each quarter, with real numbers."]],
                "alt": "Six steps to build a 2027 marketing plan for a small business in Houston and The Woodlands",
                "caption": "Steps one through five take an afternoon. Step six is the part that makes the plan work.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: LSA disputes and credits
    {
        "slug": "local-services-ads-lead-disputes-credits",
        "title": "How to Dispute Local Services Ads Leads and Actually Get Credited",
        "seo_title": "Local Services Ads Lead Disputes and Credits: How It Works",
        "desc": "How Local Services Ads lead credits work now: valid vs. invalid leads, rating leads in Google Ads, time windows, call recordings, bidding and ranking.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Google", "Google Business Profile"],
        "art": "b4",
        "hero": "tools",
        "hero_alt": "Illustration of a receipt for Local Services Ads lead disputes and credits for Houston and The Woodlands businesses",
        "related": ["local-services-ads-vs-google-ads-home-services", "google-guaranteed-vs-google-verified", "speed-to-lead-response-time-follow-up-crm"],
        "sections": [
            (None, f"""<p>Monday morning at a plumbing company in Katy. The office manager scrolls last week’s Local Services Ads leads. A man selling “Google Maps ranking.” A woman asking for a water heater install in Beaumont. A call about sprinkler repair, which they don’t do. Two calls from the same number, both charged. Somewhere in there are four real jobs, and she’d like the other money back.</p>
<p>She goes looking for the “dispute” button. It isn’t there anymore.</p>
<p>The short version: Google stopped taking manual Local Services Ads disputes in July 2024 and replaced them with automatic credits. You can still rate every lead, which feeds Google’s models and can earn a bonus credit, but you can’t file a case and argue for a refund. Since August 2026, LSA accounts have been moving into Google Ads as Performance Max campaigns with pay-per-lead goals, and the same rules carry over. So getting credited now comes down to three habits: rate every bad lead, set your account up so fewer bad leads arrive, and watch the charge status column so you know what Google already refunded.</p>
<p>Here’s how each piece works, with the actual menu paths for both the old dashboard and Google Ads. If you’re still deciding whether LSA is worth it at all, start with {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</p>"""),

            ("What Google charges for, and what it doesn’t", f"""<p>Google’s rules on charges are more specific than most owners realize. Per {SRC['leads']}, you’re charged for a valid lead, which means one of these:</p>
<ul>
<li>You answer a call, or call the customer back and talk to them.</li>
<li>You miss a call during business hours and the caller stays on the line more than 20 seconds.</li>
<li>The customer sends a text, email or voicemail.</li>
<li>You receive a booking request (U.S. and Canada).</li>
</ul>
<p>And you shouldn’t be charged for these:</p>
<ul>
<li>Leads Google’s systems flag as spam or duplicates at first contact.</li>
<li>Missed calls under 20 seconds.</li>
<li>Callers who hang up on your phone menu without pressing a key.</li>
<li>Unanswered calls outside your business hours or ad schedule.</li>
<li>Repeat contact from the same phone number or email within 15 days of the last interaction. After 15 days of no contact, a new call becomes a new lead.</li>
</ul>
<!--fig:valid-->
<p>Two details trip people up. The phone-menu timer starts at the first key press, so a long greeting before “press 1” isn’t counted against you. And “business hours” means the hours in your Google Business Profile, so if your profile says 7 a.m. to 7 p.m. and you stop answering at 5, those two hours of missed calls can be charged.</p>"""),

            ("Why the dispute button disappeared", f"""<p>Until mid-2024, you could dispute a charged lead within 30 days and a person or a model would review it. In July 2024, Google switched to automated credits: its models review every lead and credit invalid ones, typically within 30 days, per {SRC['sel']}. Google said the new system would credit the same number of leads or more on average.</p>
<p>Not everyone agreed it worked. In February 2025, {SRC['ser']} reported complaints from agencies about out-of-area and out-of-industry leads they could no longer dispute. Google’s Ads Liaison, Ginny Marvin, said Google credits more leads overall than under the manual process, and that manual disputes had been underused by most advertisers and overused by a few.</p>
<p>Then came the bigger change. Google removed credits for two categories outright: “job type not serviced” and “geo not serviced,” per {SRC['credits']}. Those used to be the most common disputes. Now they’re your problem to prevent with settings, which is the most important thing in this whole post.</p>
<!--fig:timeline-->
<p>Credits also aren’t available at all for health care verticals, tax specialists or advertisers in EMEA, per {SRC['auto']}. If you’re a dentist or a chiropractor in The Woodlands running LSA, every charged lead is final.</p>"""),

            ("How automatic credits work now", f"""<p>Per {SRC['auto']}, Google checks a lead when the customer first makes contact, and anything it judges invalid or low quality isn’t charged. Charged leads are then reassessed over time, and Google’s “How leads work” page describes that reassessment running over 30 days. Some poor-quality leads are charged and then credited within the first 24 hours.</p>
<p>When a credit happens, it goes to your account balance, usually within 30 days. Your invoice still shows the original charge. That catches bookkeepers off guard: the invoice won’t match your spend, and the credit shows up as a separate balance adjustment.</p>
<p>To see where each lead stands, look at the charge status. It reads one of four values: <b>Charged</b>, <b>Not charged</b>, <b>In review</b> or <b>Credited</b>. “In review” means Google hasn’t decided yet; per {SRC['trouble']}, if the lead isn’t a good match a credit will be applied.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Bad lead type</th><th>Can it be credited?</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Spam, robocalls, sales pitches</td><td>Often filtered or auto-credited</td><td>Rate it as spam or solicitation; check the status in a week</td></tr>
<tr><td>Duplicate contact</td><td>Not charged within 15 days of the last interaction</td><td>Rate it as a duplicate if you were charged</td></tr>
<tr><td>Missed call under 20 seconds</td><td>Not charged</td><td>Nothing, but fix why the phone wasn’t answered</td></tr>
<tr><td>Wrong service (“job type not serviced”)</td><td>No longer credited</td><td>Turn off service types you don’t do</td></tr>
<tr><td>Outside your area (“geo not serviced”)</td><td>No longer credited</td><td>Tighten locations; keep within two hours’ drive</td></tr>
<tr><td>Health care, tax specialist accounts</td><td>No credits at all</td><td>Judge LSA on cost per booked patient or client</td></tr>
</tbody></table></div>"""),

            ("How to rate a lead (old dashboard and Google Ads)", f"""<p>Rating is the closest thing left to a dispute. It doesn’t guarantee money back, but it’s the only feedback channel Google built for this, and it can trigger a bonus credit.</p>
<p><b>In the old Local Services Ads dashboard:</b> sign in, open the menu, select <b>Leads</b>, open the lead, and select <b>Rate this lead</b> in the top right to open the survey, per {SRC['auto']}.</p>
<p><b>In Google Ads, after your account migrates:</b> go to <b>Goals</b>, then <b>Conversions</b>, then <b>Leads</b>, per {SRC['move']}. That page replaces the LSA inbox. You can read and reply to message leads there, download a CSV, and, according to {SRC['access']}, it keeps a lead feedback form on each lead.</p>
<p>The survey runs from very satisfied to very dissatisfied. According to {SRC['rating']}, the dissatisfied reasons are geo mismatch, job type mismatch, not ready to book, spam, duplicate and solicitation, and “other” needs a written comment. Satisfied reasons include booked customer and high-value service. The same source says a rating can produce a bonus credit up to an unpublished cap, and that autocrediting runs on its own whether you rate or not. Agencies with many accounts can also send ratings through the Google Ads API.</p>
<!--fig:rate-->
<p>Our advice is to rate every lead, good and bad, within a few days. The good ratings matter too: they tell the model what a booked job looks like for you. And when you choose “other,” write something specific: “Caller wanted irrigation repair; we only do residential plumbing; service type is off.” Vague comments teach the system nothing.</p>
<p>What not to do: don’t mark a real customer as spam because they didn’t book. “Not ready to book” exists for that. Misusing ratings doesn’t get you more money, and it can make your lead matching worse.</p>"""),

            ("Fix the settings that create unpaid-for junk", f"""<p>Since geo and job-type mismatches aren’t credited anymore, your settings are your refund policy. In Google Ads these live under <b>Campaigns</b>, then <b>Settings</b>, per {SRC['settings']}.</p>
<ul>
<li><b>Service types.</b> Each business category has service type chips you can switch on or off. A plumber who doesn’t do septic or irrigation should turn those off today. You need at least one active per category.</li>
<li><b>Locations.</b> Target cities, counties or ZIP codes you actually serve. Google’s {SRC['best']} say not to set service areas more than two hours of driving from your business. In Greater Houston, that limit is far wider than most companies should go. A Conroe company that lists all of Harris County will get calls from Pearland it doesn’t want.</li>
<li><b>Ad schedule.</b> Run all the time, use a custom schedule, or sync to your Business Profile hours. If nobody answers after 6 p.m., don’t run after 6 p.m.</li>
<li><b>Business categories.</b> These come from your Business Profile. Opt out of any category that brings the wrong work.</li>
<li><b>Direct business search.</b> When it’s on, your ads can show for searches of your own business name, and Google says it screens out returning customers. If existing customers keep calling through your ad, check this setting.</li>
<li><b>Contact information.</b> Make sure call leads route to a phone a person answers, not the owner’s cell under a sink.</li>
</ul>
<p>Houston adds one twist: storms. After a hurricane or a hard freeze, volume spikes and so do out-of-area calls, because people from Galveston, Beaumont or Baytown search for anyone who can come. Decide in advance whether you’ll widen your area for those weeks, and change it back when the surge ends.</p>"""),

            ("Call recordings: your best evidence", f"""<p>In the U.S. and Canada, Google records inbound calls that come through the Google forwarding number on Local Services Ads, and callers hear a pre-recorded notice before you hear the “Call from Google” announcement, per {SRC['manage']}. Listening to recordings is available in the U.S. Recordings and messages aren’t available for health care or tax specialists. Older recordings carry over into Google Ads when your account migrates, per {SRC['move']}.</p>
<p>Use them. Before you rate a lead as spam or solicitation, listen to 20 seconds. You’ll find that some “bad” leads were real customers who got a bad first answer, which is a training problem, not a lead-quality one.</p>
<p>Regular Google Ads campaigns now handle recording a bit differently. Google turned call recording on by default so its AI can judge whether calls are qualified, and only qualified calls count as conversions, per its page on {SRC['aiq']}. Recording stays off if you turned it off before, or if Google identifies you as health care or financial services. To change it, go to <b>Admin</b>, then <b>Account settings</b>, open <b>Call ads</b>, and set <b>Call recording</b>, per {SRC['rec']}. If you turn it off, conversions fall back to call duration. Callers hear an automated notice, and you’re expected to tell your staff calls are recorded.</p>
<!--fig:numbers-->"""),

            ("Budgets and bidding: old modes and new", f"""<p>Bidding affects which leads you get as much as how many. The old LSA dashboard had three modes, per {SRC['bid']}:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Mode</th><th>How it worked</th><th>After migration to Google Ads</th></tr></thead>
<tbody>
<tr><td>Maximize leads</td><td>Google set bids to get the most leads for your budget; Google suggested a budget that supports at least 10 leads a week</td><td>Becomes Maximize Conversions, the default</td></tr>
<tr><td>Target cost per lead</td><td>Automated, with an optional target</td><td>One campaign-level Target CPA replaces per-category targets</td></tr>
<tr><td>Max per lead</td><td>You set the most you’d pay for any lead</td><td>Gone. Manual bidding isn’t supported.</td></tr>
</tbody></table></div>
<p>Budgets change too. Weekly budgets become a daily average (the weekly number divided by seven), and monthly spend won’t exceed that daily average times 30.4, per {SRC['move']}. Because you pay per lead, daily spend swings with demand. Google’s {SRC['best']} recommend considering a Target CPA only if you consistently get more than 15 leads a month.</p>
<p>The single Target CPA is a real issue for multi-trade companies. If you do HVAC and plumbing, an AC replacement lead is worth far more than a faucet repair, and one target across both will under-bid one and over-bid the other. Google’s answer is separate campaigns per vertical, which you set up through the Local Services page, since new pay-per-lead campaigns can’t be created inside Google Ads yet. Splitting gives each campaign less data, so only do it when the value gap is large.</p>"""),

            ("Ranking: reviews and responsiveness", f"""<p>Per {SRC['rank']}, LSA ranking comes down to your bid, how likely your ad is to produce a lead, and profile quality. “Likely to produce a lead” includes your responsiveness to calls and messages, what the customer searched for, how relevant your services and bio are, and whether you offer message and booking leads. Profile quality covers your rating, number of reviews, average response time, photos and completed verification. If you have several locations serving the same area, only the highest-ranking one shows.</p>
<p>The new Google Ads guidance says the same thing in plainer words: “Missed calls and slow response times can lower your ranking and visibility,” and aim for five or more reviews on your Business Profile, per {SRC['best']}. Review ratings now pull straight from your Business Profile into the ad, per {SRC['ppl']}.</p>
<ul>
<li><b>Answer the phone.</b> A missed call can cost you twice: a possible charge if they hold past 20 seconds, and a ranking hit. If you can’t staff the line, narrow the ad schedule.</li>
<li><b>Reply to messages in minutes.</b> If you opted into message leads, they count toward responsiveness too. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers how to set up alerts.</li>
<li><b>Ask every customer for a review.</b> Same link, every time, sent by text after the job. The {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has scripts, and {L('/blog/fake-reviews-rule-local-businesses/', 'the fake reviews rule')} covers what not to do.</li>
<li><b>Keep verification current.</b> The Google Verified badge carries over when you migrate. If you’re unsure which badge you have, see {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified')}.</li>
</ul>"""),

            ("Before and after your migration date", f"""<p>Google emails the account administrator 14 days before migration, then a reminder seven days before, per {SRC['move']}. On the day, the old dashboard stops working and logins redirect to Google Ads, per {SRC['access']}. {SRC['sej']} notes historical reports don’t transfer, so anyone who needs year-over-year numbers has to export them first.</p>
<!--fig:migrate-->
<p>After it moves, check the daily budget, Target CPA, service types and locations, ad schedule, lead phone number, photos and callouts. Better Business Bureau callouts are no longer supported, and Google recommends at least six other callouts. Business name, address and hours sync from your Business Profile and can only be edited there; a significant name or address change can trigger a 24 to 48 hour review that pauses the campaign. Google lists migration support at +1-844-205-0011, weekdays 9 a.m. to 8 p.m. Eastern.</p>"""),

            ("A weekly routine that keeps your cost per lead honest", f"""<p>This is what we’d have the office manager in Katy do every Monday, in about 20 minutes:</p>
<!--fig:weekly-->
<p>Then once a month, compare LSA’s cost per booked job with your regular Google Search campaigns. If you track both properly (our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'call and form tracking guide')} shows how), you’ll know where the next dollar should go, and you can stop arguing with Google about $40 leads and start deciding with real numbers. Our {L('/services/search-marketing/', 'search marketing team')} runs this for Houston-area home service companies, including during the migration.</p>
<p>If your LSA account feels like it’s billing you for someone else’s customers, <a href="/contact/">get in touch</a>. Tell us your trade, your service area and what you’re spending, and a senior strategist will build a plan with you.</p>"""),
        ],
        "faq": [
            ("Can you still dispute Local Services Ads leads?",
             "Not in the old sense. Google ended manual disputes in July 2024 and replaced them with automatic credits. Its models review every lead, don’t charge for leads judged invalid at first contact, and credit charged leads later found to be low quality, usually within 30 days. You can still rate each lead, which feeds Google’s models and may earn a bonus credit, but there’s no case to file."),
            ("Why won’t Google credit leads outside my service area?",
             "Google no longer offers credits for leads marked job type not serviced or geo not serviced. The fix is in your settings: turn off service types you don’t perform, target only the cities, counties or ZIP codes you serve, and keep your area within a realistic drive. Google’s guidance says not to set service areas more than two hours of driving from your business."),
            ("How long does it take to get an LSA credit?",
             "Credits usually appear in your account balance within 30 days, and some poor-quality leads are credited within the first 24 hours. The original charge still appears on your invoice, so the credit shows as a separate balance adjustment. Check the charge status on each lead, which reads charged, not charged, in review or credited, to see where it stands."),
            ("Where do I rate Local Services Ads leads in Google Ads?",
             "After your account migrates to Google Ads, go to Goals, then Conversions, then Leads. That page replaces the old LSA inbox, and each lead keeps a feedback form. In the old dashboard, open Leads, choose the lead and select Rate this lead. Rate every lead, good and bad, and add a specific comment when you choose other."),
            ("Does answering calls affect my Local Services Ads ranking?",
             "Yes. Google ranks Local Services Ads on your bid, how likely your ad is to produce a lead and your profile quality. Responsiveness is part of that, and Google says missed calls and slow response times can lower your ranking. Your rating, number of reviews and average response time also count, so answer during your ad schedule and reply to messages quickly."),
        ],
        "figures": {
            "valid": {
                "type": "compare",
                "title": "Charged vs. not charged",
                "left": {"title": "Not charged", "items": ["Spam or duplicate flagged at first contact", "Missed call under 20 seconds", "Hang-up on your phone menu, no key pressed", "Unanswered call outside your hours", "Same caller again within 15 days"]},
                "right": {"title": "Charged (valid lead)", "items": ["Call you answer or return and talk", "Missed call over 20 seconds in business hours", "Text, email or voicemail", "Booking request", "Same caller after 15 days of no contact"]},
                "alt": "Comparison of charged and not charged Local Services Ads leads for Houston and The Woodlands home service businesses",
                "caption": f"From {SRC['leads']}.",
            },
            "timeline": {
                "type": "steps",
                "title": "How LSA disputes turned into ratings",
                "sub": "The changes that matter, in order",
                "steps": [["Before July 2024", "Manual disputes within 30 days of a lead."], ["July 2024", "Automated credits replace disputes."], ["Since then", "No credits for wrong job type or wrong area."], ["August 2026", "Accounts start moving into Google Ads."], ["2027", "Remaining categories and non-U.S. accounts move."]],
                "alt": "Timeline of Local Services Ads lead dispute and credit changes affecting Houston and The Woodlands advertisers",
                "caption": "Every step moved the work from filing claims to preventing bad leads.",
            },
            "rate": {
                "type": "funnel",
                "title": "What happens to a bad lead",
                "stages": [["Customer makes contact", "Screened at first contact"], ["Charged lead", "Shows as Charged"], ["Google reassesses it", "Over about 30 days"], ["You rate it", "Feedback form, optional"], ["Credited or not", "Auto credit or bonus credit"]],
                "note": "Autocrediting runs whether or not you rate the lead.",
                "alt": "Funnel showing how a Local Services Ads lead moves from contact to credit for Houston and The Woodlands businesses",
                "caption": "Rating is optional. It’s also the only feedback channel left, so use it.",
            },
            "numbers": {
                "type": "stats",
                "title": "The LSA numbers worth memorizing",
                "stats": [["20 sec", "missed-call threshold for a charge"], ["15 days", "repeat contact isn’t a new lead"], ["30 days", "typical window for a credit to post"], ["30.4", "daily budget multiplier for the monthly cap"]],
                "note": "Source: Google Ads and Local Services Ads help pages",
                "alt": "Key Local Services Ads lead charge and credit time windows for Houston and The Woodlands advertisers",
                "caption": "Most surprise charges trace back to one of these four numbers.",
            },
            "migrate": {
                "type": "checklist",
                "title": "LSA to Google Ads migration checklist",
                "sub": "Do the first three before your date",
                "items": ["Export performance reports (they don’t transfer)", "Screenshot bids, budgets and category settings", "Make sure the admin email is monitored", "Confirm the new daily budget and Target CPA", "Check service types, locations and ad schedule", "Verify the lead routing phone number", "Replace BBB callouts with six other callouts", "Turn on lead notifications for the right people"],
                "alt": "Checklist for migrating Local Services Ads into Google Ads for Houston and The Woodlands businesses",
                "caption": f"Based on {SRC['move']}.",
            },
            "weekly": {
                "type": "checklist",
                "title": "The 20-minute Monday LSA routine",
                "sub": "For whoever owns the leads inbox",
                "items": ["Rate every lead from last week", "Listen to 20 seconds of any call you’d mark spam", "Check charge status on last month’s bad leads", "Turn off any service type that sent wrong work", "Trim locations that sent out-of-area calls", "Note missed calls and who was on the phone", "Log booked jobs by lead so cost per job is real"],
                "alt": "Weekly checklist for managing Local Services Ads lead quality and credits for Houston and The Woodlands businesses",
                "caption": "The ratings get you credits. The settings changes stop you needing them.",
            },
        },
    },
]
