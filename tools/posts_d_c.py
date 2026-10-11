"""One long-tail post: Google Guaranteed vs Google Verified, what the October 2025 badge consolidation changed for Houston LSA advertisers.

Research: top results for "google guaranteed vs google verified" / "google verified badge" (SEJ, Search Engine Land,
Search Engine Roundtable, Location3, LocalSplash, HigherVisibility). Facts verified against Google's Local Services
help pages ("About Google Verified badge" 16498018, "Understand the Google Guarantee" 7125526, "Understand the
screening and verification process" 6226575, "Business screening and verification requirements" 12174778, "About ad
rankings" 7527305), Google Business Profile's "Verify your business on Google" page, Search Engine Roundtable on the
October 20, 2025 date (Google advertiser email) and the October 1, 2026 missed-call charge, Search Engine Land's 2019
Google Screened explainer ($2,000 lifetime cap; Houston test market), and TDLR pages for electrical and A/C
contractor licenses and insurance minimums. Texas roofing license status from Jobber's Texas roofing license guide.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "gvbadge": A("https://support.google.com/localservices/answer/16498018?hl=en", "Google’s “About Google Verified badge” page"),
    "gguar": A("https://support.google.com/localservices/answer/7125526?hl=en", "Google’s Guarantee help page"),
    "process": A("https://support.google.com/localservices/answer/6226575?hl=en", "Google’s screening and verification process page"),
    "reqs": A("https://support.google.com/localservices/answer/12174778?hl=en", "Google’s business screening and verification requirements"),
    "rank": A("https://support.google.com/localservices/answer/7527305?hl=en", "Google’s “About ad rankings” page"),
    "gbpverify": A("https://support.google.com/business/answer/7107242?hl=en", "Google’s Business Profile verification page"),
    "ser": A("https://seroundtable.com/google-verified-local-service-ads-badge-39975.html", "Search Engine Roundtable"),
    "sermissed": A("https://seroundtable.com/google-lsa-missed-subsequent-calls-41940.html", "Search Engine Roundtable reported"),
    "sel": A("https://searchengineland.com/google-local-services-ads-verified-badge-461001", "Search Engine Land"),
    "sel2019": A("https://searchengineland.com/what-is-google-screened-and-how-does-it-differ-from-google-guaranteed-320954", "Search Engine Land’s 2019 explainer"),
    "tdlrelec": A("https://www.tdlr.texas.gov/electricians/apply/businesses/contractor-elec.htm", "TDLR’s electrical contractor requirements"),
    "tdlracr": A("https://www.tdlr.texas.gov/acr/contractor-apply.htm", "TDLR’s A/C contractor license page"),
    "qualify": A("https://support.google.com/localservices/answer/6230381?hl=en", "Google’s “How providers qualify” page"),
    "loc3": A("https://location3.com/blog/google-is-retiring-the-google-guarantee-for-lsa/", "Location3 noted"),
    "roof": A("https://getjobber.com/academy/roofing-license/texas/", "Jobber’s Texas roofing license guide"),
}

# Sibling post in this batch (absolute URL so the validator doesn't need it built yet).
SIB = {
    "video": '<a href="/blog/google-business-profile-video-verification/">our Business Profile video verification guide</a>',
    "move": '<a href="/blog/change-business-address-google-without-suspension/">moving or renaming without a suspension</a>',
}

POSTS = [
    {
        "slug": "google-guaranteed-vs-google-verified",
        "title": "Google Guaranteed vs Google Verified: What Changed and What It Costs",
        "seo_title": "Google Guaranteed vs Google Verified: What Changed",
        "desc": "Google Guaranteed vs Google Verified explained: what the 2025 badge switch changed, what it costs, and how Houston contractors get verified.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Google Business Profile", "Google"],
        "art": "b3",
        "hero": "shield",
        "hero_alt": "Illustration of a shield with a check mark for a guide to Google Guaranteed vs Google Verified badges for Houston contractors",
        "related": ["local-services-ads-vs-google-ads-home-services", "angi-vs-thumbtack-leads-worth-it-contractors", "hvac-marketing-houston-the-woodlands"],
        "sections": [
            (None, f"""<p>Google Guaranteed vs Google Verified: there’s no longer a choice to make. On October 20, 2025, Google retired the Google Guaranteed, Google Screened and License Verified by Google badges on Local Services Ads and replaced all of them with one badge, Google Verified. The money-back guarantee that came with Google Guaranteed was discontinued too, and the badge itself still costs nothing. You earn it by passing Google’s screening, and you pay only for the leads your ad brings in.</p>
<p>If you searched your own trade recently, saw the green check missing and assumed you’d been dropped, you probably weren’t. Occasionally the cause is a lapsed insurance certificate. For Texas contractors the checks behind the badge also depend on the trade, because the state licenses some trades and not others.</p>"""),

            ("What changed: Google Guaranteed, Google Screened and License Verified are now one badge", f"""<p>Before October 2025, a Local Services Ad carried one of several trust marks, depending on category:</p>
<ul>
<li><b>Google Guaranteed</b> for home services like HVAC, plumbing, cleaning and locksmiths. It came with a money-back guarantee for customers who booked through the ad.</li>
<li><b>Google Screened</b> for professional services such as lawyers, financial planners and real estate agents. No money-back guarantee. Per {SRC['sel2019']}, Houston and San Diego were the two test markets when Google Screened launched.</li>
<li><b>License Verified by Google</b>, a lighter mark showing Google had checked a license.</li>
</ul>
<p>Google announced the change in August 2025. {SRC['ser']} published the advertiser email, which said the old badges end “as of 10/20/2025” and that “the Money Back Guarantee associated with the Google Guarantee badge will also be discontinued.” {SRC['gvbadge']} describes the new approach as “launching a single badge for all advertisers.”</p>
<!--fig:oldnew-->
<p>Customers now see one Google Verified badge on your LSA profile, with the specific checks you passed listed. {SRC['sel']} adds that the icon “may also display dynamically” on ads when Google thinks it will influence a decision, which is why it comes and goes on individual searches.</p>"""),

            ("What does the Google Verified badge mean now?", f"""<p>It means your business passed every screening step Google requires for your category and location. Depending on the trade, the steps Google lists on {SRC['process']} include:</p>
<ul>
<li>A Google Business Profile matched to the ad that you own or manage.</li>
<li>Business registration, usually through a D-U-N-S number in the U.S. (Google also accepts Secretary of State registration, an EIN or a state revenue registration).</li>
<li>A business representative check through Dun &amp; Bradstreet, plus an identity check with a government photo ID.</li>
<li>Criminal background checks on all business owners, and in some categories on the field techs who do the work. Office and customer support staff are excluded.</li>
<li>License verification against state databases where a license exists, and a certificate of insurance.</li>
<li>Ongoing re-checks. Google can ask you to repeat steps at any time.</li>
</ul>
<p>It does not mean Google inspected your work or will pay a customer if a job goes wrong. Under Google Guaranteed a homeowner could at least file a claim. Google Verified is a screening signal and nothing more.</p>
<p>If your office still answers the phone with “we’re Google Guaranteed,” retire the line. It hasn’t been true since October 2025.</p>"""),

            ("Google guaranteed badge gone? What happened to the money-back guarantee", f"""<p>It’s gone, with a short wind-down. {SRC['gguar']} says consumers can still request reimbursement for services booked through Local Services Ads before December 7, 2025, and that requests must be filed “within 30 days of the initial service completion date.” By now, in late 2026, that window has closed for practically every job.</p>
<p>For reference, the old guarantee covered up to $2,000 over a customer’s lifetime, according to that same Search Engine Land explainer. Google reimbursed the customer, not the contractor, and {SRC['loc3']} that most consumers weren’t even aware of it and refund claims were rare.</p>
<p>There’s nothing to cancel in your account; existing verified advertisers got the new badge automatically. The cleanup is in your own marketing. Pull “Google Guaranteed” logos and “backed by Google’s guarantee” lines off the website, truck wraps, yard signs and quote templates. If you want to make a promise, make it yours. A written workmanship warranty says more than the badge ever did.</p>"""),

            ("Google Guaranteed vs Google Verified (and Google Screened), side by side", f"""<p>Plenty of articles still ranking were written before the switch. This table translates them.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Google Guaranteed (retired)</th><th>Google Screened (retired)</th><th>Google Verified (current)</th></tr></thead>
<tbody>
<tr><td>Who got it</td><td>Home service LSAs</td><td>Professional service LSAs</td><td>Every LSA advertiser that passes screening</td></tr>
<tr><td>Money-back guarantee</td><td>Yes, up to $2,000 lifetime</td><td>No</td><td>No</td></tr>
<tr><td>Cost of the badge</td><td>Free with LSA</td><td>Free with LSA</td><td>Free with LSA; you pay per lead</td></tr>
<tr><td>Where it shows</td><td>LSA ads and profile</td><td>LSA ads and profile</td><td>LSA profile, and on ads when Google expects it to help</td></tr>
<tr><td>End date</td><td>October 20, 2025</td><td>October 20, 2025</td><td>Active</td></tr>
</tbody></table></div>
"""),

            ("Google verified badge cost: is it free?", f"""<p>Yes. There’s no fee for the badge, and {SRC['process']} says businesses aren’t charged for the background checks either. What you pay for is Local Services Ads leads: calls, messages and booking requests from customers in your service area. You set a budget and a bid, and Google charges per valid lead.</p>
<p>The real costs of getting verified are indirect. You need a certificate of insurance valid for at least 14 days after you submit it, with the policy number visible. Someone has to round up the license number, the COI and IDs for every owner (and for some trades, the techs). If you pay an agency, you’re paying for the paperwork chase, since the process itself is free.</p>
<p>Lead prices vary by trade, ZIP code and lead type, with no public rate card. And {SRC['sermissed']} that since October 1, 2026, some unanswered business-hours calls count as charged leads. We went through what is and isn’t billed in our <a href="/blog/angi-vs-thumbtack-leads-worth-it-contractors/">Angi vs Thumbtack comparison</a>, and how LSA stacks up against regular search ads in <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs Google Ads</a>.</p>
<!--fig:numbers-->"""),

            ("What Google checks for Texas contractors, trade by trade", f"""<p>{SRC['reqs']} lists the U.S. checks by category, and every license line carries the qualifier “where applicable by local law.” In Texas that qualifier does a lot of work.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Trade</th><th>Texas state license</th><th>Google’s background checks</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Electrician</td><td>Yes, TDLR (contractor license plus a master electrician)</td><td>Business and owner (select users)</td><td>Google treats it as an urgent category</td></tr>
<tr><td>HVAC</td><td>Yes, TDLR A/C and refrigeration contractor, Class A or B</td><td>Business, owner and service professionals</td><td>Techs who do the work get checked too</td></tr>
<tr><td>Plumbing</td><td>Yes, Texas State Board of Plumbing Examiners</td><td>Owner checks plus service professional checks</td><td>Urgent category with extra screening</td></tr>
<tr><td>Garage door</td><td>No statewide trade license we know of</td><td>Business, owner and service professionals, all users</td><td>Urgent category</td></tr>
<tr><td>Locksmith</td><td>Yes, Texas DPS Private Security Program</td><td>Business, owner and service professionals</td><td>Also requires Google’s Advanced Verification</td></tr>
<tr><td>Roofing</td><td>No state license</td><td>Business and owner (select users)</td><td>Insurance and registration carry more weight</td></tr>
<tr><td>House cleaning, handyman, landscaping</td><td>No state license</td><td>Business and owner (select users)</td><td>Liability insurance still required</td></tr>
</tbody></table></div>
<p>Every row requires general and professional liability insurance. Google doesn’t publish dollar minimums, only that coverage must meet the requirement for your category and location.</p>
<h3>Licensed trades: TDLR electricians and HVAC</h3>
<p>For electricians, {SRC['tdlrelec']} say you must employ a licensed master electrician and carry liability insurance of at least $300,000 per occurrence, $600,000 aggregate and $300,000 for products and completed operations. A/C contractors carry the same minimums for Class A and lower ones for Class B, per {SRC['tdlracr']}. Google checks licenses against state databases where it can, so the business name on your TDLR record should match your Business Profile.</p>
<h3>Unlicensed trades: roofing in Texas</h3>
<p>{SRC['roof']} states it plainly: Texas does not require a state roofing license, and TDLR doesn’t regulate roofers. With no state license to check, a Montgomery County roofer’s badge rests on business registration, insurance and any required background checks. A newer crew from outside the area can, in principle, clear the same bar, so in roofing the badge separates you less than reviews and local job photos do. More on that in <a href="/blog/roofing-marketing-houston-storm-season/">roofing marketing for Houston storm season</a>.</p>"""),

            ("How to get the Google verified badge (and how long it takes)", f"""<p>You get it by signing up for Local Services Ads and finishing every screening step for your category. There’s no separate application for the badge. Google says on {SRC['reqs']} that the process takes 3 to 4 weeks on average after you submit your documents. Two things can stretch it: a D-U-N-S number application, which Google says can take up to 30 days, and a Business Profile that isn’t verified yet.</p>
<!--fig:path-->
<p>Some U.S. advertisers get a shortcut: {SRC['process']} describes a risk-based review that can grant the badge right away, followed by 14 days to finish the remaining steps. Don’t let that deadline slide.</p>
<h3>A hypothetical: a two-truck electrician in Tomball</h3>
<p>Say you own a residential electrical shop off FM 2920 in Tomball, with a current TDLR contractor license, a master electrician on staff and two trucks covering Cypress, Magnolia, Spring and The Woodlands. A realistic path:</p>
<!--fig:area-->
<ol>
<li><b>Day 1:</b> Confirm your Google Business Profile is verified and the name matches your TDLR record exactly. If it isn’t verified yet, start there; {SIB['video']} covers the methods and timing.</li>
<li><b>Day 1:</b> Look up your D-U-N-S number. If you don’t have one, apply now, because that’s your longest wait.</li>
<li><b>Day 2:</b> Create the LSA account, pick the job types you want (panel upgrades, maybe not doorbell swaps) and your ZIP codes.</li>
<li><b>Day 2:</b> Upload the COI. If the policy renews next week, wait for the new one.</li>
<li><b>Days 3 to 10:</b> Each owner completes the background check invitation the day it arrives.</li>
<li><b>Weeks 2 to 4:</b> Google checks your license against the state database and reviews everything. Your ad goes live with the badge once it clears.</li>
</ol>
<p>When this drags past six weeks, the hold-up is usually on the shop’s side: an unopened background check email, or a COI with the wrong business name. If Google denies a background check, {SRC['process']} says you wait 30 days to reapply, and 180 days after a second denial.</p>"""),

            ("How the badge affects LSA ranking and clicks", f"""<p>Google says two things that sound contradictory. {SRC['gvbadge']} says “Local Services Ads ranking won’t be affected by this change,” meaning the switch from the old badges didn’t reshuffle anyone. Meanwhile, {SRC['rank']} lists profile quality as an auction factor, and profile quality includes “the verification checks you have completed,” along with your rating, review count, response time and photos. Higher-quality profiles, Google says, may rank higher and pay less per lead.</p>
<p>Both are true. The rename itself was neutral, and completed checks still feed profile quality. Since you can’t run an LSA without passing the required checks anyway, the practical ranking levers are the other ones Google lists: your bid, reviews and responsiveness (“missed calls may negatively affect your responsiveness”). Our <a href="/blog/complete-guide-google-reviews/">guide to Google reviews</a> covers that side.</p>
<p>As for clicks, we haven’t found a trustworthy public study isolating the badge’s effect, so we won’t quote one. What we can say is that a line like “background-checked technicians” speaks directly to what a Kingwood homeowner worries about before letting a stranger into the attic.</p>"""),

            ("Google verified badge missing? What to check first", f"""<p>Work down this list before you call Google support:</p>
<ol>
<li><b>Look at your profile, not one search result.</b> The badge shows on ads dynamically, so one search from your own phone proves little.</li>
<li><b>Check the LSA dashboard for verification tasks.</b> Google re-evaluates advertisers and can ask you to repeat checks. Leave one unfinished and the badge, or the ad, is at risk.</li>
<li><b>Check your insurance dates.</b> An expired certificate is a frequent culprit. Upload the renewal before the old policy ends.</li>
<li><b>Check your license renewal.</b> TDLR electrical contractor licenses renew every year. A lapse in the state database can fail Google’s check.</li>
<li><b>Did ownership change?</b> A new partner or owner means a new background check.</li>
<li><b>Is your Business Profile healthy?</b> A suspended or unverified profile breaks the link to your ad. A recent move or name change is a common trigger; see our guides on {SIB['move']} and <a href="/blog/google-business-profile-suspended-reinstatement/">getting a suspended profile reinstated</a>.</li>
<li><b>Are you on a partner program?</b> Per {SRC['qualify']}, some providers come through partners like Networx or Top Rated Local, which screen under their own rules and show the partner’s logo instead.</li>
</ol>
<p>Still missing from your profile? Open a case from the LSA account, ask which step is incomplete, and keep the case number.</p>
"""),

            ("Is Google Guaranteed (now Google Verified) worth it?", f"""<p>For licensed trades that answer the phone, yes. The badge is free, and it comes attached to the most prominent paid placement a home service company can buy on Google.</p>
<p>We’d hesitate in two cases. If nobody can pick up during business hours, you’ll pay for calls you never speak to. And if your best work is large, planned projects, LSA leans toward urgent jobs; a search campaign with your own landing pages usually does better for a $30,000 remodel.</p>
<p>For HVAC specifically, LSA plus a well-built search campaign is the setup we usually recommend; see <a href="/blog/hvac-marketing-houston-the-woodlands/">HVAC marketing in Houston and The Woodlands</a>. And if you want someone to manage both, that’s our <a href="/services/search-marketing/">search marketing</a> team’s daily work for <a href="/industries/service/">home service companies</a> from Tomball to Pearland.</p>"""),

            ("Your Google Verified checklist", f"""<p>Hand this to whoever runs your office.</p>
<!--fig:checklist-->
<p>Today, put two dates on the office calendar: 30 days before the insurance renews and 30 days before the state license does. Those two reminders prevent most badge outages we’d otherwise be chasing.</p>
<p>Then pull the lead report from your LSA account for the last 60 days and listen to five of the charged calls. If some are for work you don’t want, like a doorbell swap billed as an electrical lead, switch off the job types that attract them. If you also run regular Google search campaigns, send us a request for a free <a href="/contact/">Ad Spend Leak Check</a>. We’ll record a walkthrough showing where the search side pays for calls LSA already brings in, or for jobs you’d turn down.</p>"""),
        ],
        "faq": [
            ("Is Google Guaranteed still a thing?",
             "No. Google retired the Google Guaranteed badge on October 20, 2025, along with Google Screened and License Verified by Google. All Local Services Ads advertisers who pass screening now get one Google Verified badge. The money-back guarantee was discontinued, with reimbursement requests accepted only for services booked before December 7, 2025 and filed within 30 days of the job being completed."),
            ("Google Guaranteed vs Google Screened: what was the difference?",
             "Google Guaranteed covered home services like HVAC, plumbing and cleaning, and came with a money-back guarantee of up to $2,000 per customer lifetime. Google Screened covered professional services like lawyers, financial planners and real estate agents, and had no guarantee. Both were replaced by Google Verified in October 2025."),
            ("How much does the Google Verified badge cost?",
             "The badge is free, and Google does not charge for the background checks. You pay for Local Services Ads leads, which are priced by trade, location and lead type. Indirect costs are the liability insurance Google requires, the time to gather licenses and IDs, and any agency fee for setup."),
            ("How long does it take to get Google Verified?",
             "Google says screening takes three to four weeks on average after you submit documents. A new D-U-N-S number can add up to 30 days, and an unverified Business Profile adds more. Some U.S. advertisers get accelerated verification after a risk review and receive the badge sooner, but then have 14 days to finish the remaining steps."),
            ("Do roofers in Texas need a license to get Google Verified?",
             "Texas has no state roofing license, so there is no state license for Google to check. Roofers still go through Google's business and owner checks where required, business registration, and a certificate of general and professional liability insurance. Some cities have their own contractor registration rules, so check where you work."),
            ("Why did my Google Verified badge disappear?",
             "Start with your LSA profile, since the badge shows on ads only when Google expects it to help. If it is missing from the profile, look for open verification tasks, an expired insurance certificate, a lapsed state license, an ownership change that needs a new background check, or a suspended Business Profile. Fix the item and ask support which step is incomplete."),
        ],
        "figures": {
            "oldnew": {
                "type": "compare",
                "title": "Before and after October 20, 2025",
                "left": {"title": "Old badges", "items": ["Google Guaranteed for home services", "Google Screened for professional services", "License Verified by Google", "Money-back guarantee up to $2,000"]},
                "right": {"title": "Google Verified", "items": ["One badge for all LSA advertisers", "Shows the specific checks you passed", "Same screening, simpler label", "No money-back guarantee"]},
                "alt": "Comparison of retired Google Guaranteed and Google Screened badges with the current Google Verified badge for Houston contractors",
                "caption": "Three badges and a guarantee became one badge with no guarantee, per Google’s October 2025 change.",
            },
            "numbers": {
                "type": "stats",
                "title": "Google Verified by the numbers",
                "stats": [["$0", "cost of the badge and background checks"],
                          ["3-4 wk", "average screening time after documents"],
                          ["14", "days to finish steps after accelerated approval"],
                          ["$2,000", "old lifetime guarantee cap, now retired"]],
                "note": "Source: Google Local Services help pages; Search Engine Land",
                "alt": "Stat tiles on Google Verified badge cost, screening time and missed call charges for Houston Local Services Ads advertisers",
                "caption": "The badge and checks are free; the guarantee that used to come with it is gone.",
            },
            "path": {
                "type": "steps",
                "title": "How to get the Google Verified badge",
                "sub": "Typical order for a licensed Texas trade",
                "steps": [
                    ["Verify your Business Profile", "Name and address should match your state license record."],
                    ["Get a D-U-N-S number", "Apply first; Google says it can take up to 30 days."],
                    ["Set up Local Services Ads", "Pick job types and ZIP codes you actually want."],
                    ["Upload license and insurance", "COI valid 14+ days out, policy number visible."],
                    ["Finish background checks", "Every owner, plus field techs in some trades."],
                    ["Wait for review", "About 3 to 4 weeks on average, then the badge goes live."],
                ],
                "alt": "Six steps to get the Google Verified badge for a licensed Texas contractor running Local Services Ads in Houston",
                "caption": "Most delays come from the D-U-N-S number and owners who don’t open the background check email.",
            },
            "area": {
                "type": "map",
                "title": "A Tomball electrician's LSA service area",
                "sub": "Hypothetical two-truck shop; set by ZIP code in your LSA account",
                "highlight": ["Tomball", "Magnolia", "Cypress", "The Woodlands", "Spring"],
                "note": "Illustrative example",
                "alt": "Map of a hypothetical Tomball electrician's Local Services Ads service area covering Magnolia, Cypress, Spring and The Woodlands",
                "caption": "Pick ZIP codes your trucks can reach fast; a badge won't save a two-hour drive.",
            },
            "checklist": {
                "type": "checklist",
                "title": "Google Verified checklist",
                "sub": "For Houston-area contractors running Local Services Ads",
                "items": [
                    "Business Profile verified, name matches license",
                    "D-U-N-S number or state registration on hand",
                    "State license current (TDLR, TSBPE or DPS)",
                    "COI with policy number, valid 14+ days",
                    "Background check done for every owner",
                    "Tech checks done where your trade requires them",
                    "Renewal reminders 30 days before expiry",
                    "Old Google Guaranteed logos removed",
                    "Phones answered during listed hours",
                ],
                "alt": "Checklist of steps for Houston contractors to get and keep the Google Verified badge on Local Services Ads",
                "caption": "Most badge problems come from the renewal items, not the initial setup.",
            },
        },
    },
]
