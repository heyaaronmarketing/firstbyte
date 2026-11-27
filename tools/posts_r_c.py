"""Batch 18 (module c): a step-by-step Google Ad Grants how-to for Houston and The Woodlands nonprofits, and a
short-term rental direct booking playbook for Lake Conroe, Galveston and The Woodlands hosts.

Research, Ad Grants post: Google for Nonprofits eligibility guidelines (501(c)(3), Goodstack validation, ineligible
government, hospital and school entities, fiscal sponsorship not eligible); Google's Goodstack verification help
page (3 to 5 business days, documents); TechSoup's notice that it stopped Google for Nonprofits validations in
August 2023; Ad Grants activation guide (welcome video, do not create your own Ads account, several business days);
Ad Grants account management policy (5% account CTR, two consecutive months, conversion-based Smart Bidding for
accounts since April 22, 2019, one conversion per month, geo-targeting, two sitelinks, program survey, automatic
suspension); Ad Grants policy compliance guide (quality score 1 or 2, single-word and generic keywords, two ad
groups); single keyword exceptions page; Ad Grants conversion tracking guide (30-second calls, "Other" category);
website policy (owned domain, HTTPS, original content, no AdSense); budgets page ($10,000 monthly, $329 daily).
Research, STR post: Airbnb help center on service fees (3% split host fee, 14.1%-16.5% guest fee, 15.5% single
fee) and Airbnb's fee explainer ($100 nets $84.50); Expedia Group newsroom on Vrbo's 12% pay-per-booking
commission from October 29, 2026; Airbnb off-platform policy; Texas Comptroller hotel tax FAQ (6% state rate,
29 days or less, platform collection); City of Galveston STR FAQ handout ($250, December 31, GVR numbers, 24-hour
contact within one hour); Avalara on Galveston's ordinance ($500 late fee, Class C fines, city took over Oct 1,
2025); Airbnb's Galveston tax page (9% city HOT); The Woodlands Township tax page (9% plus 6%); ABC13 on Houston's
registration ordinance and Galveston's STR growth; HVS on Galveston lodging and cruise growth; TWDB on Lake Conroe;
Google's vacation rentals help pages (free booking links, connectivity partners); Stripe pricing.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # Ad Grants post
    "elig": A("https://support.google.com/nonprofits/answer/3215869?hl=en", "Google for Nonprofits eligibility guidelines"),
    "goodstack": A("https://support.google.com/nonprofits/answer/12016036", "Google’s Goodstack verification page"),
    "techsoup": A("https://support.techsoup.org/hc/en-us/articles/47310665892123-Google-for-Nonprofits-Validations-No-Longer-Supported-by-TechSoup", "TechSoup’s own notice"),
    "activate": A("https://support.google.com/nonprofits/answer/6077350?hl=en", "Google’s Ad Grants activation guide"),
    "policy": A("https://support.google.com/grants/answer/117827?hl=en", "Ad Grants account management policy"),
    "compliance": A("https://support.google.com/nonprofits/answer/9314402?hl=en", "Ad Grants policy compliance guide"),
    "single": A("https://support.google.com/nonprofits/answer/7587473?hl=en-GB", "single keyword exceptions page"),
    "conv": A("https://support.google.com/grants/answer/9038650", "Ad Grants conversion tracking guide"),
    "website": A("https://support.google.com/nonprofits/answer/1657899?hl=en", "Ad Grants website policy"),
    "budget": A("https://support.google.com/nonprofits/answer/1332166", "Google’s budgets and bidding page"),
    # STR post
    "abnb_fees": A("https://www.airbnb.com/help/article/1857", "Airbnb’s help center"),
    "abnb_746": A("https://www.airbnb.com/resources/hosting-homes/a/simplifying-airbnb-service-fees-746", "Airbnb’s own fee explainer"),
    "vrbo": A("https://www.expedia.com/newsroom/vrbo-compensation-model-changes/", "Expedia Group’s announcement"),
    "offplat": A("https://airbnb.com/help/article/2799/", "Airbnb’s off-platform policy"),
    "comptroller": A("https://comptroller.texas.gov/taxes/hotel/faq.php", "Texas Comptroller’s hotel tax FAQ"),
    "gfaq": A("https://www.galvestontx.gov/DocumentCenter/View/21263/Short-Term-Rental-FAQ-Final-Handout", "City of Galveston’s STR FAQ"),
    "avalara": A("https://www.avalara.com/mylodgetax/en/blog/2026/01/galveston-short-term-rental-operators-face-new-rules-under-latest-ordinance.html", "Avalara’s summary of the ordinance"),
    "galtax": A("https://airbnb.com/help/article/3080", "Airbnb’s Galveston tax page"),
    "twp": A("https://www.thewoodlandstownship-tx.gov/Government/Financials/Taxes", "The Woodlands Township"),
    "abc13": A("https://abc13.com/post/houston-city-council-vote-ordinance-requiring-short-term-rentals-register/16116934/", "ABC13"),
    "hvs": A("https://www.hvs.com/article/10242-galvestons-lodging-sector-evolves-with-cruise-growth-supply-changes-and-regulatory-shifts", "HVS"),
    "twdb": A("https://www.twdb.texas.gov/surfacewater/rivers/reservoirs/conroe", "Texas Water Development Board"),
    "gvr": A("https://support.google.com/hotelprices/answer/10062327?hl=en", "Google’s vacation rentals help page"),
    "gpartners": A("https://support.google.com/hotelprices/answer/10224602?hl=en", "connectivity partners"),
    "stripe": A("https://stripe.com/pricing", "Stripe’s standard rate"),
}

GRANTS = "/blog/google-ad-grants-nonprofits-houston/"
STR = "/blog/short-term-rental-direct-booking-lake-conroe-galveston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: Google Ad Grants how-to
    {
        "slug": "google-ad-grants-nonprofits-houston",
        "title": "Google Ad Grants for Houston and The Woodlands Nonprofits: Get $10,000 a Month in Free Ads",
        "seo_title": "Google Ad Grants for Houston Nonprofits: $10K/Month Guide",
        "desc": "Step-by-step Google Ad Grants guide for Houston and The Woodlands nonprofits: eligibility, Goodstack, the 5% CTR rule, conversions and avoiding suspension.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Google Analytics", "Tag Manager"],
        "art": "b2",
        "hero": "search",
        "hero_alt": "Illustration of a search bar for Google Ad Grants nonprofit advertising in Houston and The Woodlands",
        "related": ["small-business-guide-google-ads-2026", "google-ads-account-suspended-fix", "google-ads-quality-score-lower-cost-per-click"],
        "sections": [
            (None, f"""<p>The question came from the volunteer coordinator at a small Spring nonprofit: “Google turned off our free ads. Can you turn them back on?”</p>
<p>The account had run for three years. The board member who set it up had moved to Austin, nobody had logged in since, the click-through rate had been under 5% since spring, and the only conversion it counted was a homepage view. None of that is unusual. We see some version of it every few months.</p>
<p><b>The short answer:</b> Google Ad Grants gives eligible 501(c)(3) nonprofits up to $10,000 a month in Google Search text ads. To get it, register with Google for Nonprofits, pass validation through Goodstack, bring your website up to Google’s policy and request activation. To keep it, hold a 5% account click-through rate, record at least one real conversion every month and follow the keyword rules.</p>
<p>Below is the whole process in order, with the menu paths and the rules as Google currently writes them. It’s written for Houston, The Woodlands and Montgomery County nonprofits, but the steps are the same anywhere in the U.S.</p>
<!--fig:numbers-->"""),

            ("Is Google Ad Grants worth it for a small Houston nonprofit?", f"""<p>Usually, yes. With a caveat about time.</p>
<p>The grant is a cap, not a deposit. Google’s {SRC['budget']} says it plainly: the $10,000 is “a limit, not a guarantee of spend,” with a daily ceiling of $329. Most small accounts we look at spend a fraction of it, because there are only so many people in north Houston searching “volunteer at an animal shelter near me” on a given Tuesday. That’s fine. A food pantry in Conroe that spends $1,800 of grant money a month and gets 40 volunteer sign-ups is doing well.</p>
<p>The cost is attention. Somebody has to log in, read the search terms, pause bad keywords and check that conversions are firing. Figure two to four hours a month once it’s set up, more in the first 60 days. If nobody on staff or on the board can own that, the account will drift toward suspension the way the Spring one did.</p>
<p>And it’s Search only. No display banners, no YouTube. You’re reaching people who type a need into Google, which for most nonprofits is exactly who you want.</p>"""),

            ("Step 1: Confirm your nonprofit is eligible", f"""<p>Per {SRC['elig']}, U.S. organizations must be registered with the IRS as exempt under Section 501(c)(3). Group exemptions count if you can prove affiliation with a central 501(c)(3). Fiscally sponsored projects without their own 501(c)(3) status are not currently eligible, which catches a lot of young Houston community groups that operate under a sponsor’s umbrella.</p>
<p>Three kinds of organizations are excluded outright:</p>
<ul>
<li>Government entities and organizations (a city parks department, a county library).</li>
<li><b>Hospitals and health care organizations.</b> Their charitable arms or foundations may be eligible.</li>
<li><b>Schools, academic institutions and universities.</b> Their philanthropic arms may be eligible, so a school district’s education foundation can apply even though the district can’t.</li>
</ul>
<p>That foundation exception matters in the Houston area, where most big hospital systems and many ISDs have a separate foundation with its own EIN. If you work for one, apply as the foundation, with the foundation’s website.</p>"""),

            ("Step 2: Register with Google for Nonprofits and get through Goodstack", f"""<p>Go to Google for Nonprofits, sign in with a Google account tied to your organization’s domain email (a Gmail address works but invites more questions), and submit your organization’s legal name, EIN and address.</p>
<p>Google’s validation partner is Goodstack. If you remember TechSoup handling this, that’s out of date: per {SRC['techsoup']}, TechSoup stopped performing new Google for Nonprofits validations in August 2023.</p>
<p>According to {SRC['goodstack']}, Google sends your legal name, registration number and address to Goodstack, which checks them against official registries in the background. Most applications are reviewed within 3 to 5 business days. If Goodstack can’t match you through public databases, it emails asking for documents such as bylaws, a government registration certificate or your IRS determination letter. If you applied from a personal email address, expect a request for a signed letter from a board member or executive confirming your role.</p>
<p>Two things slow Houston applicants down, in our experience. The legal name doesn’t match the IRS record (“Hope Center of Montgomery County” on the form, “Hope Ctr Inc” at the IRS), and the confirmation email lands in spam. Watch for mail from verifications@mail.goodstack.org.</p>"""),

            ("Step 3: Fix your website before you apply", f"""<p>This is where most rejections come from, and it’s the step people skip because the site “already exists.”</p>
<p>The {SRC['website']} requires, among other things, that your nonprofit owns the domain your ads point to, that the entire site is served over HTTPS, and that the site has “a significant amount of original content.” It also says not to display AdSense ads, not to host excessive third-party ads, and that donation links must work and go to a secure page dedicated to donations.</p>
<!--fig:website-->
<p>A Facebook page doesn’t count as your website, and neither does a donation portal page. Neither does a one-page site with a logo, a PayPal button and three paragraphs. If your site is thin, add real pages before you apply: one per program, a volunteer page with actual shifts and requirements, an events page, an about page with your service area. Those pages become your ad landing pages later anyway.</p>
<p>Speed counts too. The policy asks that pages load quickly across devices, and plenty of nonprofit sites run on a page builder with 40 plugins and a 9 MB hero photo of the gala. Our post on {L('/blog/how-fast-should-your-website-load/', 'how fast a website should load')} covers the fixes, and {L('/services/web-design-seo-pr/', 'our web team')} builds sites that pass this review.</p>"""),

            ("Step 4: Request Ad Grants activation, and don’t open your own Ads account", f"""<p>Once Google for Nonprofits approves you, follow {SRC['activate']}:</p>
<!--fig:apply-->
<ol>
<li>Confirm the site is on HTTPS and meets the website policy.</li>
<li>Sign in to Google for Nonprofits, find Google Ad Grants and click <b>Get started</b>. Enter the website you’ll advertise.</li>
<li>Watch the welcome video (Google says about 5 minutes) and tick the box confirming you did.</li>
<li>Click <b>Submit activation request</b>.</li>
</ol>
<p>Google’s guide is blunt on one point: “Do not create a Google Ads account at any time during the Google Ad Grants activation process.” An Ad Grants account is provisioned for you. People who make their own account first end up with a regular paid account that wants a credit card, then a support ticket to untangle it.</p>
<p>Review “may take several business days.” After activation you can invite other users. Add at least two people from the organization as admins, plus your agency if you use one, so the account never depends on one volunteer’s login again.</p>"""),

            ("Step 5: Set up conversion tracking that actually counts", f"""<p>Conversion tracking is a requirement now. Before you write a single ad, get this part right.</p>
<p>The {SRC['policy']} says accounts must have at least one qualifying conversion type and “accrue at least 1 conversion per month.” Accounts created on or after April 22, 2019 must also use conversion-based Smart Bidding on all campaigns: Maximize conversions, Maximize conversion value, Target CPA or Target ROAS. Smart Bidding needs conversion data to work, so a broken tag means ads that barely serve.</p>
<p>What counts, per the {SRC['conv']}: donations, newsletter sign-ups, volunteer sign-ups, support line calls, purchases at a charity shop, app downloads. Track a form by its thank-you page where possible, and fall back to tracking the button click only if there’s no confirmation page. Phone calls need a minimum 30-second call length.</p>
<p>What doesn’t count as a primary conversion: time on site, homepage visits and similar soft signals. You can add them, but they belong in the “Other” category and shouldn’t be marked as conversions. Google also says that if your conversion rate looks very high, you should confirm it reflects a meaningful action. A 60% conversion rate on “visited the donate page” is the kind of thing that gets an account flagged.</p>
<p>Our setup is Google Tag Manager with GA4, a thank-you page for each form, and a donation platform that fires a purchase event with the gift amount. The {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'form and call tracking guide')} walks through the tag setup step by step.</p>"""),

            ("Step 6: Decide what to advertise: volunteers, donations or programs", f"""<p>Most nonprofits start with “donate” keywords. It’s usually the weakest campaign in the account.</p>
<p>People rarely search Google to find a new charity to give to. They search for help, for something to do on Saturday, or for a place to drop off a couch. So build around the three things people really look for, in roughly this order of performance in accounts we’ve run:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Who’s searching</th><th>Example keywords</th><th>Conversion to track</th></tr></thead>
<tbody>
<tr><td>Programs and services</td><td>People who need what you offer</td><td>food pantry Conroe, free ESL classes Spring TX, grief support group The Woodlands, low cost spay neuter Montgomery County</td><td>Intake form, call of 30+ seconds, appointment</td></tr>
<tr><td>Volunteers</td><td>Individuals, families, church and corporate groups</td><td>volunteer opportunities The Woodlands, food bank volunteer Houston, volunteer with dogs near me, court appointed special advocate volunteer</td><td>Volunteer sign-up form, orientation registration</td></tr>
<tr><td>In-kind donations</td><td>People clearing out a house or holding a drive</td><td>donate furniture Houston, where to donate baby clothes Katy, school supply donation drop off</td><td>Pickup request form, drop-off page call</td></tr>
<tr><td>Events</td><td>Locals looking for something to do</td><td>5K The Woodlands March, charity golf tournament Montgomery County, gala tickets Houston</td><td>Registration or ticket purchase</td></tr>
<tr><td>Donations</td><td>People already leaning your way, often after a news event</td><td>donate to hurricane relief Houston, [your cause] charity Houston, your own name</td><td>Completed gift with value</td></tr>
</tbody></table></div>
<p>The seasonal pattern here is specific to the Gulf Coast. Searches for relief, shelters and supply drop-offs spike after a storm, and you want relief ad groups written and paused before June 1 so you can switch them on the afternoon the power comes back. After Hurricane Beryl in July 2024, the organizations that had pages and ads ready were the ones that caught that traffic. Our {L('/blog/hurricane-season-marketing-playbook-houston-the-woodlands/', 'hurricane season marketing playbook')} has the prep list. Year-end is the other spike, which makes right now (the week of Giving Tuesday) a good time to check that your donation conversion is firing.</p>"""),

            ("Step 7: Build campaigns and keywords that pass the rules", f"""<p>The keyword rules trip up more Houston accounts than anything else. From the {SRC['compliance']}:</p>
<ul>
<li>Keywords with a quality score of 1 or 2 must be paused or removed. Keywords showing “—” aren’t scored yet and aren’t monitored.</li>
<li>Single-word keywords aren’t permitted, with exceptions for your own brand terms, recognized medical conditions and a short list on the {SRC['single']}: charity, charities, donate, donation, ngo, ngos, nonprofit, nonprofits, volunteer and volunteering.</li>
<li>Overly generic keywords that don’t show intent must be paused or removed. Google’s own examples are “free videos,” “e-books” and “today’s news.”</li>
<li>Each campaign needs at least 2 ad groups, and the account needs at least 2 sitelink assets.</li>
</ul>
<!--fig:keywords-->
<p>Geo-targeting is in the main policy: show ads where people would actually use your services. A Montgomery County food pantry shouldn’t be serving ads in Galveston. If you have a local program and a national advocacy arm, split them into separate campaigns by geography. In <b>Campaign settings &gt; Locations</b>, use “Presence: people in or regularly in your included locations,” and target the cities or counties you serve rather than “United States.”</p>
<!--fig:geo-->
<p>Build each ad group tight: one theme, five to fifteen keywords, phrase and exact match, and a landing page that matches. “Volunteer with seniors The Woodlands” goes to the senior companion volunteer page, never the homepage. That tightness is also how you keep quality scores above 2. The {L('/blog/google-ads-quality-score-lower-cost-per-click/', 'quality score guide')} explains the three components if you want the mechanics.</p>
<p>Add negatives from day one. Volunteer campaigns pick up job seekers (“jobs,” “salary,” “hiring,” “paid”) unless you actually have paid roles. Food assistance campaigns pick up searches for SNAP office hours and grocery coupons. Donation campaigns attract “tax deduction calculator” and “how to start a nonprofit.” Read the search terms report every week for the first month.</p>"""),

            ("Step 8: Write ads that clear the 5% CTR line", f"""<p>The rule: “maintain a 5% click-through rate (CTR) each month,” measured across the whole account. Miss it two consecutive months and the account is temporarily deactivated, per the {SRC['policy']}. Accounts running only Smart campaigns are exempt, though we rarely recommend that route.</p>
<p>Five percent is hard with sloppy keywords and easy with tight ones. What moves it in accounts we’ve run:</p>
<ul>
<li>Put the place and the action in headline one. “Volunteer in The Woodlands This Saturday” beats “Make a Difference Today” every time.</li>
<li>Use concrete details: shift length, age minimum, parking, whether groups are welcome. “2-Hour Shifts, Ages 12+ With a Parent.”</li>
<li>Fill every asset slot: four or more sitelinks, callouts, structured snippets, a call asset during office hours. Bigger ads get clicked more.</li>
<li>Pause any keyword that has a few hundred impressions and a CTR under 2%. It’s dragging the account average down, and a paused keyword costs you nothing.</li>
<li>Cut brand-adjacent fluff like “charity” or “nonprofit Houston” on their own, which pull huge impressions and low clicks.</li>
</ul>
<p>Sample responsive search ad for a volunteer ad group:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Asset</th><th>Text</th></tr></thead>
<tbody>
<tr><td>Headline 1</td><td>Volunteer at Our Conroe Food Pantry</td></tr>
<tr><td>Headline 2</td><td>Saturday Shifts, 9 to 11 a.m.</td></tr>
<tr><td>Headline 3</td><td>Groups and Families Welcome</td></tr>
<tr><td>Description 1</td><td>Sort and pack food for Montgomery County families. Sign up online in two minutes.</td></tr>
<tr><td>Description 2</td><td>No experience needed. Free parking, closed-toe shoes required, ages 12+ with an adult.</td></tr>
</tbody></table></div>"""),

            ("Step 9: Run the monthly compliance check", f"""<p>Fifteen minutes on the first business day of the month prevents almost every suspension we’ve seen. Our version:</p>
<!--fig:monthly-->
<p>One item on that list is easy to forget: the program survey. Google sends a periodic survey and you must respond to stay in the program. If the notification email goes to a person who left, you won’t see it. Keep a shared inbox like marketing@ on the account and make sure notification emails are opted in.</p>
<p>Also keep a simple change log. When a new executive director asks why volunteer sign-ups doubled in October, “we split the youth and adult volunteer ad groups on October 3” is a better answer than a shrug.</p>"""),

            ("Why do Google Ad Grants accounts get suspended?", f"""<p>Google says accounts that violate program policies are “subject to automatic suspension without notification.” So the first sign is often just that the ads stopped and the dashboard shows the account as paused or suspended. Here are the causes we see, roughly in order of frequency:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Cause</th><th>What it looks like</th><th>How to fix it</th></tr></thead>
<tbody>
<tr><td>CTR under 5% for two months</td><td>Account-level CTR around 2% to 4%, broad keywords, few assets</td><td>Pause low-CTR keywords, tighten ad groups, add sitelinks and callouts, then request reactivation</td></tr>
<tr><td>No valid conversions</td><td>Zero conversions, or only page views and time on site marked as conversions</td><td>Set up a real form or donation conversion, move soft signals to “Other”</td></tr>
<tr><td>Keyword violations</td><td>Single-word keywords, quality score 1 or 2, generic terms</td><td>Remove or pause; an automated rule can pause QS 1 to 2 keywords weekly</td></tr>
<tr><td>Missing structure</td><td>One ad group in a campaign, fewer than 2 sitelinks</td><td>Add the second ad group and sitelinks</td></tr>
<tr><td>Missed survey</td><td>Account deactivated with no performance issue</td><td>Opt in to notification emails and complete the survey</td></tr>
<tr><td>Website problems</td><td>Expired SSL, domain lapsed, donate button broken</td><td>Fix the site first, then submit a reactivation request</td></tr>
</tbody></table></div>
<p>Reinstatement means fixing the problem and submitting a reactivation request from the account. Fix everything at once. Requests that fix the CTR but leave a single-word keyword live just get bounced. If your account is suspended for something that isn’t on this list, our {L('/blog/google-ads-account-suspended-fix/', 'Google Ads suspension guide')} covers the broader policy side.</p>"""),

            ("When the grant isn’t enough", f"""<p>Ad Grants is a great base. It has limits. It’s Search only and text only, and the policy restrictions mean some valuable searches (single-word causes, broad awareness terms) are off the table.</p>
<p>Plenty of Houston nonprofits pair the grant with a small paid Google Ads account for gala ticket sales or a capital campaign, plus Meta ads to reach volunteers who wouldn’t think to search. Keep the two Google accounts separate and keep the grant account clean. For a sense of what paid clicks cost around here, see our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')}, and the {L('/blog/small-business-guide-google-ads-2026/', 'small business Google Ads guide')} for setting up a paid account properly.</p>
<p>If you’d like a senior strategist to look at your nonprofit’s goals and build a plan that uses the grant well, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How long does it take to get Google Ad Grants approved?",
             "Plan on two to three weeks if your paperwork and website are in order. Goodstack validation for Google for Nonprofits usually takes 3 to 5 business days, and the Ad Grants activation review takes several more business days after you submit. Delays usually come from a legal name that doesn’t match IRS records, a document request sitting in a spam folder, or a website that fails the HTTPS or content requirements."),
            ("Can a Houston church or school get Google Ad Grants?",
             "Schools, academic institutions and universities are not eligible, but their philanthropic arms, such as an ISD education foundation with its own 501(c)(3), may be. Churches aren’t named as an excluded category, but every applicant must be recognized by the IRS as a 501(c)(3) and pass Goodstack validation. Many churches never file for a determination letter, so check your status before applying."),
            ("What happens if my Ad Grants CTR drops below 5%?",
             "One month under 5% is a warning sign, not a suspension. If the account-level click-through rate stays below 5% for two consecutive months, Google temporarily deactivates the account. To recover, pause low-performing keywords, tighten ad groups, add more sitelinks and callouts, and submit a reactivation request. Accounts that only run Smart campaigns are exempt from the CTR rule."),
            ("Do I need a 501(c)(3) to get free Google ads in Texas?",
             "Yes. In the United States, Google for Nonprofits requires registration with the IRS as exempt under Section 501(c)(3), or a group exemption with proven affiliation to a 501(c)(3) parent. Fiscally sponsored projects without their own status are currently not eligible. Government entities, hospitals and health care organizations, and schools are excluded, though their charitable foundations may qualify."),
            ("Can someone else manage our Google Ad Grants account?",
             "Yes. After activation you can invite additional users, including staff, board members or an agency, to manage the account. We recommend at least two admins from the organization so access never depends on one person. Google offers no payment for management, so an agency’s fee comes from your budget, and the account should stay owned by the nonprofit."),
        ],
        "figures": {
            "numbers": {
                "type": "stats",
                "title": "Google Ad Grants by the numbers",
                "stats": [["$10,000", "monthly cap on Search text ads"], ["$329", "daily budget ceiling"], ["5%", "account CTR to hold each month"], ["1", "real conversion needed per month"]],
                "note": "Source: Google Ad Grants help center",
                "alt": "Key Google Ad Grants numbers for Houston and The Woodlands nonprofits: monthly cap, daily cap, CTR and conversion rule",
                "caption": f"From Google’s {SRC['budget']} and {SRC['policy']}. The $10,000 is a ceiling, not a guaranteed spend.",
            },
            "website": {
                "type": "checklist",
                "title": "Website checks before you apply",
                "sub": "Based on Google’s Ad Grants website policy",
                "items": ["You own the domain the ads point to", "Every page loads over HTTPS", "Real, original content on each program", "No AdSense or excess third-party ads", "Donate button goes to a secure donation page", "No broken links or 404s", "Pages load fast on a phone", "Clear menu: programs, volunteer, give, about"],
                "alt": "Checklist of Google Ad Grants website requirements for Houston and The Woodlands nonprofit websites",
                "caption": "A Facebook page or a donation portal page doesn’t count as your site.",
            },
            "apply": {
                "type": "steps",
                "title": "From 501(c)(3) to live Ad Grants",
                "sub": "The order that avoids rework",
                "steps": [["Check eligibility", "IRS 501(c)(3), not a government, hospital or school entity."], ["Google for Nonprofits", "Register with your legal name and EIN."], ["Goodstack validation", "Usually 3 to 5 business days."], ["Fix the website", "HTTPS, owned domain, real content."], ["Request activation", "Welcome video, then submit. No self-made Ads account."]],
                "alt": "Steps to apply for Google Ad Grants as a Houston or Montgomery County nonprofit, from eligibility to activation",
                "caption": "Fixing the website before step five saves a rejection and a second review.",
            },
            "keywords": {
                "type": "compare",
                "title": "Ad Grants keywords: rejected vs. compliant",
                "left": {"title": "Breaks the rules or the CTR", "items": ["food (single word)", "help (single word, generic)", "free videos (generic)", "nonprofit houston (huge, low CTR)", "Quality score 1 or 2 left running"]},
                "right": {"title": "Passes and performs", "items": ["food pantry conroe tx", "volunteer opportunities the woodlands", "donate furniture houston pickup", "volunteer (exempt single word)", "Your organization’s own name"]},
                "alt": "Comparison of Google Ad Grants keywords that violate policy versus compliant keywords for Houston nonprofits",
                "caption": f"Single-word exceptions come from Google’s {SRC['single']}.",
            },
            "geo": {
                "type": "map",
                "title": "Target where you actually serve",
                "sub": "Example service area for a Montgomery County nonprofit",
                "highlight": ["The Woodlands", "Conroe", "Spring", "Magnolia", "Willis", "Montgomery", "Shenandoah"],
                "note": "Illustrative example",
                "alt": "Map of an example Google Ad Grants geo-targeting area for a nonprofit serving The Woodlands, Conroe and Montgomery County near Houston",
                "caption": "Ad Grants policy requires location settings that match where people can use your services.",
            },
            "monthly": {
                "type": "checklist",
                "title": "The monthly Ad Grants check",
                "sub": "First business day of every month",
                "items": ["Account CTR for last month is 5% or higher", "At least 1 real conversion recorded", "No keywords with quality score 1 or 2", "No single-word keywords outside the exceptions", "Every campaign has 2+ ad groups", "Account has 2+ sitelinks", "Search terms read, new negatives added", "Survey and policy emails checked in the shared inbox"],
                "alt": "Monthly Google Ad Grants compliance checklist for nonprofits in Houston and The Woodlands",
                "caption": "Fifteen minutes a month. It catches nearly every suspension before it happens.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: STR direct bookings
    {
        "slug": "short-term-rental-direct-booking-lake-conroe-galveston",
        "title": "Short-Term Rental Marketing Around Houston: Direct Bookings for Lake Conroe, Galveston and The Woodlands Hosts",
        "seo_title": "Short-Term Rental Direct Bookings: Lake Conroe & Galveston",
        "desc": "Short-term rental marketing for Lake Conroe, Galveston and The Woodlands hosts: Airbnb and Vrbo fees vs direct booking, Google listings, taxes, repeat guests.",
        "category": "Strategy",
        "icons": ["Google", "Google Ads", "Meta"],
        "art": "b4",
        "hero": "key",
        "hero_alt": "Illustration of a key for short-term rental direct booking marketing at Lake Conroe, Galveston and The Woodlands near Houston",
        "related": ["hotel-marketing-houston-direct-bookings", "boat-dealer-marina-marketing-lake-conroe", "email-marketing-basics"],
        "sections": [
            (None, f"""<p>$84.50.</p>
<p>That’s what {SRC['abnb_746']} says a host keeps from a $100 nightly price under its single 15.5% host-paid fee, if the host didn’t raise prices when the fee changed. On a $2,400 July week at a lake house on Lake Conroe, that gap is real money. And Vrbo just moved too.</p>
<p><b>The short answer:</b> direct bookings pay off for Houston-area hosts once you have repeat guests or a property people remember. Keep Airbnb and Vrbo for discovery, build a simple booking site, get listed on Google’s vacation rental results through a connectivity partner, and email past guests before every peak season. Budget for the taxes and admin the platforms used to handle.</p>
<p>This playbook is for owners and small managers with one to maybe fifteen units around Lake Conroe, Galveston, The Woodlands, Montgomery and the Bolivar side. It covers the money first, then the local rules, then the marketing.</p>"""),

            ("How much do Airbnb and Vrbo really cost a Houston-area host?", f"""<p>More than most hosts think, and the math changed twice in the last year.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>What the host pays</th><th>What the guest pays on top</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Airbnb, split fee</td><td>Most hosts 3%</td><td>14.1% to 16.5% guest service fee</td><td>{SRC['abnb_fees']}</td></tr>
<tr><td>Airbnb, single (host-only) fee</td><td>Most hosts 15.5%, others typically 14% to 16%</td><td>No separate guest service fee; taxes still added</td><td>{SRC['abnb_fees']}</td></tr>
<tr><td>Vrbo, pay-per-booking</td><td>Flat 12% (12% to 15% by region and brand), payment processing included, from October 29, 2026</td><td>A traveler fee Vrbo says will typically be lower</td><td>{SRC['vrbo']}</td></tr>
<tr><td>Your own site</td><td>Card processing, e.g. 2.9% + 30¢ per charge, plus booking software</td><td>Nothing beyond your price, fees and taxes</td><td>{SRC['stripe']}</td></tr>
</tbody></table></div>
<p>Airbnb says the split fee is being phased out, and the single fee is mandatory for hosts who use property management software. Once you switch, you can’t switch back. Vrbo is retiring its annual subscription option and moving everyone to pay-per-booking; subscription hosts move over at the end of their term.</p>
<!--fig:payout-->
<p>Two cautions before you get excited about that chart. First, the platforms bring guests you’d never find alone. A first-time Houston family searching “Galveston beach house with pool” is on Airbnb, and they’re not typing your URL. Second, direct bookings come with costs the chart ignores: software, your time, a damage policy you enforce yourself, chargebacks, and taxes you now have to collect. More on that next.</p>
<!--fig:fees-->
<p>So the realistic goal for most hosts isn’t leaving the platforms. It’s getting 20% to 40% of nights booked direct within a couple of years (that’s the range we’d aim for, not a benchmark), mostly from repeat guests and their friends.</p>"""),

            ("What changes when a guest books direct", f"""<p>The biggest one is tax. Per the {SRC['comptroller']}, the state hotel occupancy tax is 6% and applies to rentals of 29 days or less. When a short-term rental platform agrees to collect and remit state HOT for you, and you rent only through that platform, you aren’t required to collect and remit it yourself. Take one direct booking and that’s no longer true. You collect the 6% state tax on that stay, file with the Comptroller, and handle any city or county tax too.</p>
<p>Other things you inherit:</p>
<ul>
<li><b>Payments and disputes.</b> A guest who disputes a charge with their bank is now your problem, not Airbnb’s. A signed rental agreement and a clear cancellation policy at checkout are your evidence.</li>
<li><b>Damage.</b> There’s no AirCover. Use a refundable deposit or a damage waiver product, and confirm what your insurance covers for direct-booked guests.</li>
<li><b>Guest screening.</b> No platform reviews of the guest. Ask for ID and the names of adults staying.</li>
<li><b>Calendar sync.</b> Your booking site has to block dates on Airbnb and Vrbo instantly, or you will double-book a July 4 weekend. A channel manager or PMS does this; iCal alone can lag.</li>
</ul>
<p>None of that is a reason not to do it. It’s a reason to set it up properly once.</p>"""),

            ("Galveston short-term rental rules: registration, GVR numbers and hotel tax", f"""<p>Galveston is the most regulated STR market in the Houston area, and the rules got stricter in 2025.</p>
<p>Some context: {SRC['abc13']} reported in April 2025 that Galveston went from about 27 short-term rentals in 2019 to about 4,900 in 2024, per the Park Board’s CFO, with roughly 1,000 still unregistered. {SRC['hvs']} noted cruise passenger volume hit a record 1.7 million in 2024. That’s a lot of competition and a lot of enforcement attention.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Rule</th><th>What it says</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Annual registration</td><td>$250 per year; renewals open December 1 and are due December 31</td><td>{SRC['gfaq']}</td></tr>
<tr><td>Late fee</td><td>$500 for missing the deadline</td><td>{SRC['avalara']}</td></tr>
<tr><td>GVR number</td><td>“A GVR # is required for all listings,” each unit gets its own, and a new owner means a new number</td><td>{SRC['gfaq']}</td></tr>
<tr><td>Local contact</td><td>A 24-hour contact who lives within one hour of the property</td><td>{SRC['gfaq']}</td></tr>
<tr><td>City hotel tax</td><td>9% on gross rental revenue, including cleaning and pet fees</td><td>{SRC['galtax']}</td></tr>
<tr><td>State hotel tax</td><td>6%, filed with the Texas Comptroller unless a platform collects it all</td><td>{SRC['comptroller']}</td></tr>
<tr><td>Filing frequency</td><td>Monthly; quarterly allowed only under $500 a month or $1,500 a quarter</td><td>{SRC['gfaq']}</td></tr>
<tr><td>Penalties</td><td>Class C misdemeanor, up to $500 per offense or $2,000 for health, sanitation, zoning or fire safety; each day counts</td><td>{SRC['avalara']}</td></tr>
</tbody></table></div>
<p>Regulation moved from the Park Board to the City of Galveston on October 1, 2025, per {SRC['avalara']}, so older blog posts telling you to register with the Park Board are out of date.</p>
<!--fig:galveston-->
<p>For your marketing: put the GVR number on your own booking site, on every listing page, and on any Facebook or Instagram post that advertises a specific property. Platforms are required to pull listings without valid numbers when the city asks, and the city is checking. And when a guest books direct, that 9% city tax plus 6% state tax (15% combined) is yours to collect and file. Build it into your checkout so the guest sees it as a line item rather than a surprise.</p>
<p>If December 31 is a few weeks away when you’re reading this, renew now.</p>"""),

            ("Lake Conroe, The Woodlands and Montgomery County: what to check", f"""<p>North of Houston the rules are less centralized, which makes them easier to miss.</p>
<p><b>The Woodlands.</b> {SRC['twp']} levies a 9% hotel occupancy tax, with the state’s 6% on top, for 15% combined. It applies to anyone collecting payment for stays under 30 days in the Township, which includes short-term rentals. Starting January 1, 2026, filers who consistently collect less than $2,500 a month can file quarterly. A host with a guest house near Hughes Landing who takes a direct booking for a big event weekend owes that tax.</p>
<p><b>Lake Conroe.</b> The lake covers roughly 19,640 acres on the West Fork of the San Jacinto River in Montgomery and Walker counties, per the {SRC['twdb']}. Rental homes around it sit in the city of Conroe, the city of Montgomery, Willis, or unincorporated county land, and each can mean a different local tax picture and different HOA rules. The state’s 6% applies to all of them. For local tax, ask the city you’re in, and if you’re unincorporated, ask the county; we’re not going to guess at rates we couldn’t confirm. Many Lake Conroe subdivisions also have deed restrictions on short-term rentals, which matter more than any marketing plan.</p>
<p><b>Houston.</b> In April 2025, {SRC['abc13']} reported Houston City Council was set to vote on requiring short-term rental owners to register, with $1.6 million for software that matches online listings to registrations. If you have a unit inside the city limits, check the city’s current requirements before you advertise direct.</p>
<p>Not legal or tax advice. A CPA who files hotel tax for other hosts is worth the fee in your first year.</p>"""),

            ("Build the direct booking site guests trust", f"""<p>A direct booking site has one job: make a guest who already likes your place feel safe paying you instead of Airbnb. That’s a trust problem more than a design problem.</p>
<!--fig:site-->
<p>What we’d put on it, page by page:</p>
<ul>
<li><b>One page per property</b> with 25+ real photos, a floor plan sketch, bed sizes per room, the dock or beach access explained honestly (“four-minute walk to the seawall, one street to cross”), and the GVR number if it’s in Galveston.</li>
<li><b>A live calendar and instant booking</b> through your PMS or booking engine. “Email us for availability” loses most direct guests.</li>
<li><b>Total price before the last step,</b> with nightly rate, cleaning fee and taxes itemized. Hidden fees feel worse on a small site than on a platform.</li>
<li><b>Reviews from Airbnb and Vrbo</b>, quoted with the platform and date. You can’t embed them all, but you can quote them, and a page showing 140 five-star stays does more than any headline.</li>
<li><b>House rules, cancellation policy and the rental agreement</b> visible before checkout.</li>
<li><b>Local guide pages</b>: boat rentals and launch spots on Lake Conroe, Strand and Seawall restaurants in Galveston, Market Street and the Waterway in The Woodlands. These pages pull in search traffic and they’re useful to guests already booked.</li>
</ul>
<p>Use your own domain and a real email address at that domain. A Gmail address and a PayPal link on a free site builder looks like a scam to a cautious guest. Our {L('/blog/how-much-does-a-website-cost-the-woodlands/', 'website cost guide')} gives honest ranges if you’re pricing this out.</p>"""),

            ("Get listed on Google’s vacation rental results", f"""<p>Search “Galveston vacation rentals” or “Lake Conroe cabin” and Google shows a vacation rentals module with photos, prices and a map. That’s free distribution most independent hosts never claim.</p>
<p>Per {SRC['gvr']}, vacation rentals show across Google Search, Maps and Google’s travel lodging search, with filters for price, amenities and guest rating. You connect through an integration that sends Google your rates, availability and content. The booking links can point to your own website, and Google says “there are no fees for Google-generated referrals or bookings.”</p>
<p>Individual hosts usually get there through one of Google’s {SRC['gpartners']}, which are often the same property management and booking-site companies you’d use anyway. When you’re shopping for direct booking software, ask each vendor if it’s a Google vacation rentals partner. That one question can decide which tool you pick.</p>
<p>Then keep the data clean. Wrong prices or a calendar that shows open dates you’ve already sold will hurt you with Google and with the guest who clicks.</p>"""),

            ("Turn platform guests into direct repeat guests, without breaking Airbnb’s rules", f"""<p>This is where direct bookings actually come from. Not ads. Past guests.</p>
<p>But be careful. {SRC['offplat']} prohibits asking guests to communicate off-platform before booking, offering discounts to book outside Airbnb, putting links in listings or messages that take people off the platform, and rebooking an existing stay outside Airbnb. Penalties range from warnings to removing listings or accounts. So no “book direct next time and save 10%” message in the Airbnb inbox, and no URL in the listing.</p>
<p>What works and stays clean:</p>
<!--fig:repeat-->
<ul>
<li>A branded property name and a printed welcome book in the house with your website, so the guest remembers where they stayed.</li>
<li>A guest Wi-Fi splash page or a QR code on the fridge for the local guide, which offers an email list sign-up for “first notice on summer dates.” Opt-in, clearly worded.</li>
<li>Everyone who books direct goes on the list automatically, with consent at checkout.</li>
<li>Email the list before each booking window: late January for spring break and summer, mid-summer for Labor Day and fall weekends, September for Thanksgiving and holidays. Four to six emails a year is plenty.</li>
</ul>
<p>Texts need extra care. Texas brought marketing texts under its telephone solicitation law in 2025, and the {L('/blog/email-marketing-basics/', 'email marketing basics')} post covers list building if you’re starting from zero. Email is the safer, cheaper channel for this.</p>"""),

            ("Paid ads for direct bookings around Houston: keep them small and specific", f"""<p>Most hosts shouldn’t start with ads. Once you have a booking site, a Google listing and a guest list, a small paid budget can fill gaps.</p>
<p><b>Google Ads.</b> Bid on your property name (cheap, and it stops Airbnb and Vrbo ads from sitting above your own name) and on specific phrases: “Lake Conroe lake house rental with boat dock,” “Galveston beach house sleeps 12,” “pet friendly rental The Woodlands.” Negatives: jobs, apartments, “for sale,” long term, monthly, RV, campground and hotel brand names. Our {L('/services/search-marketing/', 'search team')} sets these up.</p>
<p><b>Meta.</b> Facebook and Instagram are good for retargeting people who looked at your site and didn’t book, and for reaching Houston audiences with a short dock-at-sunset video when you have open midweek dates. Keep targeting to the Houston metro, which is where most drive-to guests start. See {L('/services/paid-social-advertising/', 'our paid social service')}.</p>
<p>An illustrative starting budget for a two-to-five unit host is $300 to $800 a month in peak season and close to zero in slow months. That’s our starting point, not a benchmark. Judge it by booked nights, not clicks.</p>
<p>Lake Conroe hosts can also partner locally. Boat rental outfits and marinas see the same guests, and our {L('/blog/boat-dealer-marina-marketing-lake-conroe/', 'boat dealer and marina marketing post')} shows how they market. A “10% off a pontoon day with your stay” arrangement is a better direct-booking perk than a coupon. Hotels around Houston face the same platform math with Expedia and Booking.com, and our {L('/blog/hotel-marketing-houston-direct-bookings/', 'hotel direct booking guide')} covers tactics that carry over.</p>"""),

            ("Seasonality map: when Houston guests book the lake and the beach", f"""<p>Most guests at Lake Conroe, Galveston and The Woodlands drive in from the Houston metro, so the calendar follows Houston school schedules, Houston weather and Houston events.</p>
<!--fig:region-->
<p>What we’d plan around, based on the markets we work in (patterns, not data):</p>
<div class="bp-tbl"><table>
<thead><tr><th>Period</th><th>Galveston</th><th>Lake Conroe</th><th>The Woodlands</th><th>Marketing move</th></tr></thead>
<tbody>
<tr><td>January to February</td><td>Quiet, then Mardi Gras weekends</td><td>Quiet; fishing weekends</td><td>Business travel, youth sports</td><td>Email list for spring break and summer; open summer dates</td></tr>
<tr><td>March</td><td>Spring break spike</td><td>Spring break and early boating</td><td>Family visits, events</td><td>Fill gaps with Meta to Houston families</td></tr>
<tr><td>April to May</td><td>Weekends build, graduation stays</td><td>Lake season starts, Memorial Day</td><td>Spring events, graduations</td><td>Raise rates on event weekends; push midweek deals</td></tr>
<tr><td>June to early August</td><td>Peak</td><td>Peak, July 4 sells out</td><td>Steady</td><td>Minimal ads; focus on reviews and guest experience</td></tr>
<tr><td>Late August to October</td><td>Hurricane season risk, softer midweek</td><td>Labor Day, then fall weekends</td><td>Fall events</td><td>Flexible cancellation messaging; fall weekend packages</td></tr>
<tr><td>November to December</td><td>Holiday events, slow midweek</td><td>Thanksgiving family groups</td><td>Holiday visitors to family</td><td>Email past guests for holidays; renew Galveston registration by December 31</td></tr>
</tbody></table></div>
<!--fig:season-->
<p>Hurricane season runs June 1 to November 30, and a named storm in the Gulf can trigger a wave of cancellations even if it misses. A clear storm policy on your site (what happens if there’s a mandatory evacuation) books more direct guests in August than a discount does. Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing calendar')} has more dates.</p>"""),

            ("A 90-day plan for your first direct bookings", f"""<ul>
<li><b>Days 1 to 30.</b> Confirm registrations and tax accounts: Galveston GVR, Texas Comptroller, Township or city as needed. Choose a PMS or booking engine that syncs calendars and is a Google vacation rentals partner. Buy your domain.</li>
<li><b>Days 31 to 60.</b> Launch the booking site with full property pages, itemized pricing and taxes, rental agreement and storm policy. Connect to Google vacation rentals. Put the welcome book and QR code in every unit.</li>
<li><b>Days 61 to 90.</b> Send the first email to past direct guests and opt-ins ahead of the next season. Start a brand-name Google Ads campaign. Track direct nights as a share of total nights each month.</li>
</ul>
<p>If you want a senior strategist to look at your properties and build a direct booking plan around your seasons, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Do I have to collect hotel tax on direct bookings in Texas?",
             "Yes. The Texas state hotel occupancy tax is 6% on stays of 29 days or less. If you rent only through a platform that collects state tax for you, you don’t have to collect and remit it yourself, but direct bookings change that. You collect and file state tax with the Comptroller, plus any local tax, such as Galveston’s 9% city tax or The Woodlands Township’s 9%."),
            ("How do I register a short-term rental in Galveston?",
             "Register each unit with the City of Galveston, which took over from the Park Board on October 1, 2025. The annual fee is $250, renewals open December 1 and are due December 31, and a $500 late fee applies. Each unit gets a GVR number that must appear on all listings, and you need a 24-hour local contact who lives within one hour of the property."),
            ("Can I ask Airbnb guests to book directly next time?",
             "Not through Airbnb. Its off-platform policy prohibits asking guests to communicate off-platform before booking, offering discounts to book outside Airbnb, and putting links in listings or messages that lead off the platform. Instead, brand your property, leave a welcome book with your website, and offer an opt-in email list through a QR code or Wi-Fi page in the home."),
            ("How do I get my vacation rental on Google?",
             "Google shows vacation rentals in Search, Maps and its travel lodging search, and the booking links can go to your own website at no charge for referrals or bookings. Individual hosts usually connect through one of Google’s connectivity partners, often a property management system or booking-site provider. Ask software vendors whether they’re a Google vacation rentals partner before you choose one."),
            ("What does Vrbo charge hosts in 2026?",
             "Starting October 29, 2026, Vrbo moved hosts to a pay-per-booking commission, typically a flat 12% in the U.S. that includes payment processing, with rates of 12% to 15% depending on region and brand. Vrbo is retiring its subscription model, and subscription hosts switch at the end of their term. Vrbo says the traveler service fee will typically be lower."),
        ],
        "figures": {
            "payout": {
                "type": "bars",
                "title": "What a host keeps from a $1,000 stay",
                "sub": "Before taxes, cleaning and software costs",
                "items": [["Direct booking", 970.70, "$970.70"], ["Airbnb split fee", 970, "$970"], ["Vrbo 12%", 880, "$880"], ["Airbnb single fee", 845, "$845"]],
                "highlight": [0],
                "note": "Illustrative example. Under the split fee the guest also pays a 14.1% to 16.5% service fee.",
                "alt": "Bar chart of host payout on a $1,000 short-term rental booking in Houston, Lake Conroe or Galveston by channel: direct, Airbnb and Vrbo",
                "caption": f"Fee rates from {SRC['abnb_fees']}, {SRC['vrbo']} and {SRC['stripe']}. Direct bookings add costs this chart doesn’t show.",
            },
            "galveston": {
                "type": "checklist",
                "title": "Galveston STR compliance checklist",
                "sub": "Before you advertise a single direct booking",
                "items": ["Each unit registered with the City of Galveston", "GVR number on every listing and your own site", "$250 renewal paid by December 31", "24-hour local contact within one hour", "City HOT account set up for 9% city tax", "Texas Comptroller account for 6% state tax", "Taxes applied to cleaning and pet fees too", "Occupancy, parking and noise rules posted for guests"],
                "alt": "Checklist of Galveston short-term rental registration and hotel occupancy tax rules for hosts near Houston",
                "caption": f"From the {SRC['gfaq']}, {SRC['galtax']} and {SRC['avalara']}.",
            },
            "site": {
                "type": "steps",
                "title": "A direct booking site guests trust",
                "sub": "In the order a cautious guest checks",
                "steps": [["Own domain", "Your property name, real email at that domain."], ["Property pages", "25+ photos, beds, access, GVR number."], ["Live calendar", "Instant booking, synced with Airbnb and Vrbo."], ["Full price", "Rate, cleaning fee and taxes itemized."], ["Proof", "Quoted platform reviews, policies, agreement."]],
                "alt": "Steps to build a short-term rental direct booking website for Lake Conroe, Galveston and The Woodlands hosts",
                "caption": "Trust is what converts. A beautiful site that hides the total price won’t.",
            },
            "repeat": {
                "type": "funnel",
                "title": "How platform guests become direct guests",
                "stages": [["Books on Airbnb or Vrbo", "100 stays"], ["Remembers your property name", "60"], ["Joins your email list in the home", "25"], ["Opens a pre-season email", "15"], ["Books direct next year", "6"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how short-term rental guests at Lake Conroe or Galveston near Houston turn into repeat direct bookings",
                "caption": "Every step happens off the platform’s messaging, so it stays within Airbnb’s rules.",
            },
            "region": {
                "type": "map",
                "title": "Where Houston’s drive-to rentals are",
                "sub": "Lake Conroe up I-45 north; Galveston past League City on I-45 south, off the bottom of this map",
                "highlight": ["The Woodlands", "Conroe", "Montgomery", "Willis", "League City", "Clear Lake"],
                "alt": "Map of short-term rental markets near Houston including Lake Conroe, Montgomery, The Woodlands and the route to Galveston",
                "caption": "Most guests drive in from the Houston metro, so target ads and emails there first.",
            },
            "season": {
                "type": "columns",
                "title": "Galveston rental demand by month",
                "sub": "Relative demand, peak month = 100",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [25, 40, 65, 55, 70, 95, 100, 75, 40, 45, 35, 40],
                "highlight": [5, 6],
                "y_label": "Demand",
                "note": "Illustrative example based on typical patterns, not published data",
                "alt": "Column chart of illustrative monthly short-term rental demand in Galveston for Houston-area hosts",
                "caption": "Plan email sends six to ten weeks before each rise.",
            },
            "fees": {
                "type": "stats",
                "title": "The platform fee numbers",
                "stats": [["15.5%", "Airbnb single host-only fee"], ["12%", "Vrbo commission from Oct 29, 2026"], ["6%", "Texas state hotel tax, 29 days or less"], ["$250", "Galveston annual registration"]],
                "note": "Source: Airbnb, Expedia Group, Texas Comptroller, City of Galveston",
                "alt": "Stats on Airbnb and Vrbo fees, Texas hotel tax and Galveston registration for short-term rental hosts near Houston",
                "caption": "The numbers that decide whether direct bookings are worth your time.",
            },
        },
    },
]
