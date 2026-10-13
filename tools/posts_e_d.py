"""Two remodeler posts: "how to get more remodeling leads" (owning leads vs renting them, Houston/Woodlands proof)
and "kitchen remodeling marketing" (high-ticket kitchen and bath projects, long cycle, cost per signed project).

Research: Harvard JCHS LIRA releases (May 2026 press release; July 2026 release as republished by NARI), 2025 U.S.
Houzz & Home Study as reported by Pro Remodeler and Contractor magazine, JLC/Remodeling Cost vs. Value 2025
(West South Central and national pages), NAHB Eye on Housing age-of-housing-stock post (2024 ACS), HCFCD Harvey
damage figures via Community Impact, The Woodlands Township Covenant Administration and RDRC pages, Visit The
Woodlands history page, City of Houston Super Neighborhood 43 (Kingwood annexation), Houston Permitting Center's
residential remodel permit page, Google Business Profile local ranking help, Google Local Services Ads category list,
Google Ads data segment membership duration help, Meta Marketing API special ad category restrictions, Jon Loomer on
Meta's category definitions, Wipfli on Regulation Z triggering terms. Competitors read: Jobber, JobNimbus, Angi,
Mightysites and several small-agency kitchen marketing posts.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SIB1 = "how-to-get-more-remodeling-leads-houston"
SIB2 = "kitchen-bath-remodeling-marketing-the-woodlands"

SRC = {
    "lira": A("https://nari.org/nari-blog-main/remodeling-spending-slowdown/", "Harvard’s Joint Center for Housing Studies, in its July 2026 forecast"),
    "lira_may": A("https://www.jchs.harvard.edu/press-releases/remodeling-growth-slow-sharply-early-2027", "the Joint Center’s May 2026 release"),
    "houzz": A("https://proremodeler.com/home/article/55285504/study-shows-kitchens-and-bathrooms-still-most-popular-remodels", "the 2025 Houzz &amp; Home Study"),
    "houzz2": A("https://www.contractormag.com/bath-kitchen/article/55285019/houzz-home-renovation-activity-remains-strong-amid-softening-spend", "Contractor magazine’s summary of the Houzz study"),
    "harvey": A("https://communityimpact.com/news/2018/06/08/hurricane-harvey-damage-report-harris-county", "Harris County Flood Control District figures"),
    "nahb": A("https://eyeonhousing.org/2026/03/age-of-housing-stock-by-state/", "NAHB’s analysis of 2024 Census data"),
    "twhist": A("https://visitthewoodlands.com/about/history", "Visit The Woodlands"),
    "cov": A("https://thewoodlandstownship-tx.gov/Departments/Covenant-Administration", "Township’s Covenant Administration page"),
    "rdrc": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/RDRC", "Residential Design Review Committees"),
    "hpc": A("https://www.houstonpermittingcenter.org/hpwcode1135", "Houston Permitting Center"),
    "kingwood": A("https://houstontx.gov/superneighborhoods/43.html", "the City of Houston’s Kingwood page"),
    "gbp": A("https://support.google.com/business/answer/7091?hl=en", "Google’s own help page on local ranking"),
    "lsa": A("https://support.google.com/localservices/answer/6224841?hl=en", "Google’s Local Services Ads category list"),
    "cvv": A("https://www.jlconline.com/cost-vs-value/2025/west-south-central/", "the 2025 Cost vs. Value Report for the West South Central region"),
    "cvvnat": A("https://www.jlconline.com/cost-vs-value/2025/national/", "national Cost vs. Value figures"),
    "regz": A("https://www.wipfli.com/insights/articles/fi-understand-triggering-terms-to-keep-your-advertising-in-compliance", "Regulation Z’s “triggering terms”"),
    "loomer": A("https://www.jonloomer.com/special-ad-categories-meta-ads/", "Jon Loomer’s summary of Meta’s categories"),
    "metadev": A("https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category", "Meta’s developer documentation"),
    "gads": A("https://support.google.com/google-ads/answer/2472738?hl=en", "Google Ads lets you keep a website visitor"),
}

POST1 = {
    "slug": SIB1,
    "title": "How to Get More Remodeling Leads in Houston (and Stop Renting Them)",
    "seo_title": "How to Get More Remodeling Leads in Houston",
    "desc": "How to get more remodeling leads in Houston and The Woodlands: the lead-cost math, project pages, Google Business Profile, reviews and referral partners.",
    "category": "Local marketing",
    "icons": ["Google Business Profile", "Google Ads", "Facebook"],
    "art": "b2",
    "hero": "remodel",
    "hero_alt": "Illustration of remodeling tools and plans for a guide on how to get more remodeling leads in Houston and The Woodlands",
    "related": ["angi-vs-thumbtack-leads-worth-it-contractors", "local-seo-contractors-houston", "complete-guide-google-reviews"],
    "sections": [
        (None, f"""<p>The fastest way to get more remodeling leads is to buy them. The way to get more remodeling leads that actually sign, at a margin you like, is to own them: a portfolio website with a real page for every finished project, a Google Business Profile you feed with job photos and reviews every week, and three or four referral partners who send you homeowners nobody else is bidding on. Lead marketplaces can fill a slow month. They shouldn’t be the plan.</p>
<p>We’ll start with the math, because once you see what a shared lead costs per signed job, the rest of this guide reads differently. Everything below is written for remodelers working Houston, The Woodlands, Kingwood, Spring and Conroe.</p>"""),

        ("How to get more remodeling leads you own instead of rent", f"""<p>A rented lead is one you pay for every time: a marketplace match, a click, a shared form fill. Stop paying and it stops coming. An owned lead comes from something you built once and keep compounding, like a project page that ranks, a profile with 140 reviews, or a realtor who has sent you six kitchens.</p>
<p>Both cost money. The difference shows up a year later. Rented leads cost the same in month 13 as in month one (usually more, as competitors bid up the same homeowners). Owned sources get cheaper per job as the photos, reviews and relationships pile up.</p>
<p>The market makes this more urgent. {SRC['lira']}, expects U.S. home improvement spending to grow from $517 billion to $519 billion between mid-2026 and mid-2027, an annual growth rate of just 0.5%. That’s flat. In a flat market you don’t get more jobs by waiting for demand to rise. You take them from the remodeler down the road, and the ones who win are the ones homeowners already trust before they call.</p>
<!--fig:rentown-->
<p>Demand for professionals isn’t the problem. In {SRC['houzz']}, about nine in ten renovating homeowners hired one. The question is whether they find you first and believe you quickly.</p>"""),

        ("The lead-cost math: marketplace leads vs. leads you own", f"""<p>We covered Angi and Thumbtack pricing, billing and the FTC’s HomeAdvisor order in detail in <a href="/blog/angi-vs-thumbtack-leads-worth-it-contractors/">our guide to whether Angi and Thumbtack leads are worth it</a>, so we won’t repeat it here. The short version: you pay for the match, not the job, and on Angi’s own earnings call pros were winning about one in six leads.</p>
<p>What matters for a remodeler is cost per <i>signed</i> job, and how much margin you give up to get it. Here’s a worked example with round numbers. Say you run a four-person remodeling company in Spring and your average bathroom job is $25,000 at a 30% gross margin, so each signed job is worth about $7,500 in gross profit.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Lead source</th><th>Cost per lead</th><th>Leads per signed job</th><th>Cost per signed job</th><th>Who else is bidding</th></tr></thead>
<tbody>
<tr><td>Shared marketplace lead</td><td>$100</td><td>12</td><td>$1,200</td><td>2 to 4 other pros, same day</td></tr>
<tr><td>Google search ad lead</td><td>$150</td><td>5</td><td>$750</td><td>Whoever else they call</td></tr>
<tr><td>Google Business Profile call</td><td>About $40 in photo and review time</td><td>4</td><td>$160</td><td>Usually 1 or 2</td></tr>
<tr><td>Realtor or designer referral</td><td>A lunch and a thank-you gift</td><td>2</td><td>Under $150</td><td>Often nobody</td></tr>
</tbody></table></div>
<p>These are illustrative numbers, not benchmarks, so plug in your own. The pattern is what to watch: the further a lead comes from a paid marketplace, the fewer people it’s shared with, and the less you discount to win it. A marketplace homeowner collecting four bids on a hall bath will push you on price. A homeowner whose realtor said “call this guy, he did my last three listings” mostly wants a start date.</p>
<!--fig:costper-->
<p>Paid search still has a place: the homeowner searched, and the click lands on your site, not a marketplace. See <a href="/services/search-marketing/">our Google Ads management</a> page for how we set it up.</p>"""),

        ("Are exclusive remodeling leads worth paying for?", """<p>“Exclusive remodeling leads” is the pitch lead vendors use once contractors get tired of shared ones. Sometimes it means the vendor sells the lead to only you. Sometimes it means only you <i>this hour</i>. Ask for the definition in writing, and ask how the vendor generated the lead, because a homeowner who filled out a “get three free quotes” form expects three quotes, no matter what the vendor promised you.</p>
<p>Here’s how we’d test an exclusive lead vendor:</p>
<ol><li>Buy a small batch, 20 leads or fewer, before signing any term contract.</li>
<li>Call every lead within ten minutes and log whether the homeowner remembers asking.</li>
<li>Ask each homeowner, “How many remodelers have reached out so far?” Their answer tells you how exclusive it was.</li>
<li>Track each lead through to signed or lost in your CRM, not in the vendor’s dashboard.</li>
<li>Compare cost per signed job against your Google Ads and referral numbers after 60 to 90 days.</li></ol>
<p>The only truly exclusive remodeling lead is a homeowner who looked you up by name. The rest of this page is about producing more of those.</p>"""),

        ("Build a portfolio site that sells the job before the call", f"""<p>Most remodeling websites have one “Gallery” page of 60 unlabeled photos. Google can’t tell what they show, and homeowners can’t tell whether that kitchen was $40,000 or $140,000.</p>
<p>Build a page for each finished project instead. One kitchen, one page. It ranks for searches like “kitchen remodel Alden Bridge” or “walk-in shower Kingwood,” it gives your Business Profile posts somewhere to link, and it answers the questions a homeowner is too polite to ask on the first call.</p>
<!--fig:projectpage-->
<p>Then build service pages that pull those projects together. A homeowner searching for kitchen remodeling leads you to a <b>kitchen remodeling</b> page with your five best kitchen projects, a realistic price range, your process and a consult form. Do the same for bathrooms, additions, whole-home remodels and anything else you want more of. If you serve several cities, our guide to <a href="/blog/power-of-local-landing-pages/">local landing pages</a> covers how to build city pages that aren’t thin copies of each other.</p>
<p>A couple of details change lead quality more than design does:</p>
<ul><li><b>Publish a price frame.</b> “Most of our primary bathroom remodels land between $35,000 and $70,000” scares off a few shoppers and saves you a dozen wasted site visits.</li>
<li><b>Ask one qualifying question on the form.</b> “What’s your rough budget?” with ranges, or “When would you like to start?” Both help you prioritize callbacks without adding friction.</li></ul>
<p>If your site can’t do this today, that’s what our <a href="/services/web-design-seo-pr/">web design and SEO team</a> builds for contractors.</p>"""),

        ("Google Business Profile: the free remodeling lead source most shops starve", f"""<p>{SRC['gbp']} is blunt about it: “more reviews and positive ratings can help your business’s local ranking.” For a remodeler that means a weekly routine, not a profile you set up once and forget:</p>
<ul><li><b>Categories.</b> Pick the primary category that matches the work you want most (for many shops that’s a remodeler category, with kitchen and bathroom remodeler as secondaries if you do them). Don’t add categories for work you turn down.</li>
<li><b>Service area.</b> List the cities and ZIP codes you’ll drive to and hide your address if clients don’t visit. A shop in The Woodlands might list Spring, Conroe, Magnolia, Tomball and Kingwood.</li>
<li><b>Project photos every week.</b> Before, during and after. Tradespeople on site, not stock images. Name the neighborhood in the caption when the homeowner agrees.</li>
<li><b>One post per finished project</b>, linking to that project’s page on your site.</li>
<li><b>A review request on the day of the final walkthrough</b>, while the homeowner is standing in the new kitchen. Our <a href="/blog/complete-guide-google-reviews/">guide to Google reviews</a> has the text-message wording.</li></ul>
<p>Google’s Local Services Ads now include both kitchen remodeling and bathroom remodeling, plus general contractor, countertop and flooring categories, per {SRC['lsa']}. LSA leads are pay-per-lead and come with the Google Verified badge, so they’re a reasonable paid layer on top of a strong profile. We compare them with regular search ads in <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs. Google Ads</a>, and our <a href="/blog/local-seo-contractors-houston/">local SEO guide for Houston contractors</a> covers the rest of the map-pack setup.</p>"""),

        ("Houston selling points: Harvey rebuilds, aging finishes and The Woodlands’ design review", f"""<h3>The Harvey rebuild is now eight or nine years old</h3>
<p>Hurricane Harvey flooded 154,170 homes in Harris County in 2017, and a little less than half of them sat outside the 100- and 500-year floodplains, according to {SRC['harvey']}. Many were gutted and rebuilt in 2018 and 2019, quickly and often to an insurance budget, and some of those rushed kitchens and baths are now due for a proper redo. A page or ad that speaks to “your post-Harvey kitchen, done properly this time” lands in a way a generic offer doesn’t. Be tactful; some of these owners lost a lot.</p>
<h3>Young housing stock, old neighborhoods</h3>
<p>Texas has the second-newest housing in the country, with a median owner-occupied home age of 28 years against 42 nationally, per {SRC['nahb']}. But The Woodlands opened on October 19, 1974, with Grogan’s Mill as its first village ({SRC['twhist']}), and Friendswood Development built Kingwood through the 1970s. Those original houses are around 50 years old: dated layouts, closed kitchens, small primary baths. Market specific projects to specific neighborhoods.</p>
<!--fig:area-->
<h3>The Woodlands’ design review is a selling point</h3>
<p>The {SRC['cov']} says work on a lot with an existing home “must have the prior written approval of the Residential Design Review Committee or their designated staff.” Each village has its own committee (the Township lists nine), they meet at least monthly per the {SRC['rdrc']} page, and only the Development Standards Committee can grant variances. Applications go through the Township’s online Civic Access Portal.</p>
<p>Most homeowners find this confusing. Put “We prepare and submit your RDRC application” on your Woodlands pages and build the meeting calendar into the timeline you quote. That line separates you from the out-of-town crew who learns about the committee after demo day.</p>
<h3>Permits change at the city line</h3>
<p>Inside Houston city limits, the {SRC['hpc']} requires a residential permit with plan review for remodels, conversions and additions, and licensed contractors schedule the trade inspections. That includes Kingwood, which Houston annexed in 1996 ({SRC['kingwood']}). Conroe, Shenandoah, Tomball and other cities run their own offices, and many unincorporated subdivisions answer to an HOA instead. Saying plainly who pulls the permit and who handles the HOA, on every service page, answers a question homeowners are already worried about.</p>"""),

        ("How to get more remodeling jobs from realtors, designers and past clients", f"""<p>Referral partners send the best leads you’ll ever get, and most remodelers treat them as luck. Treat them as a channel with a process.</p>
<ul><li><b>Listing agents.</b> They need pre-listing fixes done fast and buyers who want changes after closing. Offer a two-week turnaround on paint, fixtures and small bath refreshes, and a one-page “what it would cost to open this kitchen” estimate their buyers can take to showings.</li>
<li><b>Interior designers and kitchen showrooms.</b> Many have clients and no installer they trust. Offer to handle the RDRC paperwork and protect their design on site.</li>
<li><b>Restoration and water-mitigation companies.</b> They dry out the house after a leak or storm and often don’t do the rebuild.</li>
<li><b>Past clients.</b> Most renovators aren’t selling soon, so the family who loved their new kitchen is a good bet for the primary bath in two or three years. Put a reminder in the CRM.</li></ul>
<p>The process: keep a list of partners in your CRM, send each one a short project recap with photos when you finish a job near them, and track which partner sent which signed contract. Jobber’s guide suggests a referral relationship takes months to pay off, and that matches what we see. Three partners sending four jobs a year each is a dozen remodels with no competing bids.</p>"""),

        ("Is Houzz worth it for remodelers in Houston?", """<p>Houzz is where a lot of affluent homeowners save photos before they call anyone, so a complete Houzz profile with your best projects and reviews is worth an afternoon. It also gives you a second, independent review source that design-minded clients trust.</p>
<p>Houzz Pro’s paid advertising is a different question. Judge it like Angi: get your market’s pricing in writing, run it for a set period, and count signed jobs in your own CRM. Our view: the free profile pulls its weight, and the paid tier has to earn its renewal.</p>"""),

        ("Home remodeling leads from paid ads: where to start", f"""<p>Once the owned pieces are in place, paid ads add speed. A sensible order for a remodeler new to paid ads:</p>
<ol><li><b>Local Services Ads</b> in the kitchen and bathroom remodeling categories, if they’re available in your ZIPs.</li>
<li><b>Google search ads</b> on specific project searches (kitchen remodel, bathroom remodel, room addition plus your cities), sent to the matching service page, never the homepage.</li>
<li><b>Retargeting</b> everyone who viewed a project page, with more project photos and a consult offer.</li></ol>
<p>Kitchen and bath projects deserve their own campaigns, keywords and follow-up, because the ticket is higher and the decision takes months. We cover that in <a href="/blog/{SIB2}/">our kitchen and bath remodeling marketing guide</a>. If you also want to reach homeowners on Facebook and Instagram, read the special ad category notes there and in our <a href="/services/paid-social-advertising/">paid social</a> overview first.</p>"""),

        ("Tie each remodeling lead to the contract it became", f"""<p>Most remodelers know their lead count and their revenue and nothing in between, so they can’t tell which source actually signed. A few habits close that gap:</p>
<ul><li>Use a call tracking number on your website, your Business Profile and each ad channel. Our <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking guide</a> shows the setup.</li>
<li>Record the source on every lead in your CRM, and update the status when it becomes a consult, a proposal, a signed job or a loss.</li>
<li>Once a quarter, divide what you spent on each source by the jobs it signed. Cut the bottom one. Feed the top one.</li></ul>
<p>Start this week with the cheapest fix: post the last three finished projects to your Business Profile, each linked to its own page. If you’re also running Google or Meta ads, check what the account counts as a conversion. When a form fill from a $3,000 bath shopper and a booked design consult both register as one “lead,” the campaigns optimize toward the cheap one. Our free <a href="/contact/">Ad Spend Leak Check</a> looks at exactly that, in a 10-minute recorded video of your account sent within 48 hours. More on how we work with contractors is on our <a href="/industries/service/">home services page</a>.</p>"""),
    ],
    "faq": [
        ("Where do remodelers get the best leads?",
         "Referrals from past clients, realtors and designers usually close at the highest rate and the best margin, because the homeowner arrives already trusting you and is rarely collecting four bids. After that come calls from your Google Business Profile and project pages on your own site. Paid search and Local Services Ads add volume, and shared marketplace leads tend to close lowest and push hardest on price."),
        ("How much should a remodeling lead cost?",
         "There is no fair single number, because a $4,000 bath refresh and a $90,000 kitchen are different businesses. Work backward instead. Decide what you can spend to sign one job, often 5 to 10 percent of its gross profit, then divide by how many leads it takes you to sign one. That gives you a ceiling per lead for each project type."),
        ("How do I get kitchen remodeling leads without Angi?",
         "Build a dedicated kitchen remodeling page with five or more real local projects and a price range, post each finished kitchen to your Google Business Profile, and ask every happy client for a review on the day of the final walkthrough. Add Google Local Services Ads in the kitchen remodeling category, then search ads on kitchen remodel terms for your cities, and retarget site visitors with more project photos."),
        ("Do I need approval to remodel a home in The Woodlands?",
         "For exterior work, yes. The Woodlands Township says improvements on a lot with an existing home need prior written approval from the village Residential Design Review Committee or its staff, applied for through the Township's online portal. Each village committee meets at least monthly. Interior-only remodels are a different question, so check with Covenant Administration before you start, and build review time into the schedule."),
        ("Are bathroom remodeling leads cheaper than kitchen leads?",
         "Usually, because the jobs are smaller and more companies compete for them, including tub-to-shower specialists. Bathroom leads also tend to decide faster. That makes them good for keeping crews busy, but price pressure is higher, so lean on reviews, project pages and partner referrals instead of shared leads where four bids are the norm."),
    ],
    "figures": {
        "rentown": {
            "type": "compare",
            "title": "Renting remodeling leads vs. owning them",
            "left": {"title": "Rented leads", "items": [
                "Pay for every lead, every month",
                "Shared with other remodelers",
                "Homeowner is collecting bids",
                "Stops the day you stop paying",
            ]},
            "right": {"title": "Owned leads", "items": [
                "Project pages and reviews compound",
                "Homeowner found you by name",
                "Less price pressure on the bid",
                "Keeps working in a slow month",
            ]},
            "alt": "Comparison of rented marketplace leads and owned sources for remodelers learning how to get more remodeling leads",
            "caption": "Both cost money. Only one gets cheaper per job over time.",
        },
        "costper": {
            "type": "bars",
            "title": "Cost per signed bathroom job, by source",
            "sub": "Worked example for a $25,000 average job",
            "items": [
                ["Shared marketplace", 1200, "$1,200"],
                ["Google search ads", 750, "$750"],
                ["Business Profile calls", 160, "$160"],
                ["Partner referrals", 150, "Under $150"],
            ],
            "highlight": [3],
            "note": "Illustrative example",
            "alt": "Bar chart comparing cost per signed job for home remodeling leads from marketplaces, Google ads, profiles and referrals",
            "caption": "Use your own close rates; the order of the bars rarely changes.",
        },
        "projectpage": {
            "type": "checklist",
            "title": "What every remodeling project page needs",
            "sub": "One finished job, one page",
            "items": [
                "Neighborhood or city, with the owner’s OK",
                "Before, during and after photos",
                "Scope in plain words: what changed and why",
                "Timeline from demo to final walkthrough",
                "Budget range for this kind of project",
                "The homeowner’s review or a short quote",
                "Who handled permits and HOA approval",
                "A consult button for a similar project",
            ],
            "alt": "Checklist for a remodeling project page that helps a Houston remodeler get more kitchen and bathroom remodeling leads",
            "caption": "Twenty pages like this beat a gallery of 200 unlabeled photos.",
        },
        "area": {
            "type": "map",
            "title": "Where older homes meet remodeling budgets",
            "sub": "Communities with 1970s and 1980s housing north and west of Houston",
            "highlight": ["The Woodlands", "Kingwood", "Spring", "Memorial", "Humble", "Conroe"],
            "alt": "Map of The Woodlands, Kingwood, Spring and Memorial for marketing remodeling services and getting remodeling leads in Houston",
            "caption": f"The Woodlands and Kingwood both date to the 1970s ({A('https://visitthewoodlands.com/about/history', 'Visit The Woodlands')}).",
        },
    },
}

POST2 = {
    "slug": SIB2,
    "title": "Kitchen Remodeling Marketing for High-End Jobs in The Woodlands",
    "seo_title": "Kitchen Remodeling Marketing in The Woodlands",
    "desc": "Kitchen remodeling marketing for $50K+ kitchen and bath jobs in The Woodlands, Kingwood and Memorial: video, Google Ads, financing and long-cycle nurture.",
    "category": "Paid ads",
    "icons": ["Google Ads", "Instagram", "YouTube"],
    "art": "b4",
    "hero": "browser",
    "hero_alt": "Illustration of a browser window for a guide to kitchen remodeling marketing and bathroom remodeling marketing in The Woodlands",
    "related": ["retargeting-explained", "pool-builder-marketing-houston-the-woodlands", "landing-pages-101"],
    "sections": [
        (None, f"""<p>Kitchen remodeling marketing for high-end projects comes down to proof and patience. Show finished local kitchens and baths in video and on detailed project pages, buy Google searches from homeowners who are ready to talk, stay in front of them for the six to twelve months they take to decide, and measure what each signed project cost you, not each lead.</p>
<p>That’s different from marketing a $9,000 tub-to-shower conversion, and it’s why generic “10 kitchen remodeling marketing ideas” lists don’t help much. Below is how we’d market a kitchen and bath company selling to homeowners in The Woodlands, Kingwood and the Memorial area, with real cost data, ad settings and the follow-up that closes long decisions. If you’re after more leads of every kind first, start with <a href="/blog/{SIB1}/">our guide on how to get more remodeling leads in Houston</a>.</p>"""),

        ("What kitchen and bath remodels cost, and why that shapes your marketing", f"""<p>According to {SRC['cvv']} (the region that includes Texas), an average midrange minor kitchen remodel cost $26,762, a midrange major kitchen $77,742 and an upscale major kitchen $151,557. A midrange bath remodel came in at $22,995 and an upscale bath at $73,185. Custom work in places like Carlton Woods or Bunker Hill Village can run well past those averages.</p>
<!--fig:costs-->
<p>Now look at resale. In the same regional report, the upscale major kitchen recouped just 34.6% of its cost at sale. People spending $150,000 on a kitchen aren’t doing it for the appraisal. In {SRC['houzz']}, 61% of renovating homeowners planned to stay at least 11 more years, and the median spend on large kitchens (200 square feet or more) was $55,000.</p>
<p>So the marketing has to sell living in the house, not return on investment. “Add value to your home” is the message of a flipper. “Finally cook for twelve at Thanksgiving without bumping into each other” is the message of the person who’s about to sign.</p>"""),

        ("Who you’re marketing to in The Woodlands, Kingwood and Memorial", f"""<p>High-end kitchen and bath buyers north and west of Houston fall into a few groups, and each one needs a slightly different pitch:</p>
<ul><li><b>Original owners in 1970s and 1980s villages.</b> Grogan’s Mill, Panther Creek and Cochran’s Crossing in The Woodlands, older sections of Kingwood. Closed kitchens, small primary baths, soffits. They want walls opened up.</li>
<li><b>Owners of 2000s builder homes.</b> Sterling Ridge, Creekside Park and newer Kingwood sections. The layout works, but the finishes are builder grade and tired. These buyers want a design refresh more than demolition.</li>
<li><b>Memorial and the Villages.</b> Bunker Hill, Hunters Creek, Piney Point and the other Memorial Villages are separate small cities with their own permit rules, and larger lots. More full-gut and addition work.</li>
<li><b>Empty nesters planning to age in place.</b> Curbless showers, wider doors, better lighting. They often decide faster than families.</li></ul>
<p>According to the Houzz data, Baby Boomers and Gen X homeowners did most of the renovating, Gen X was the most likely to take on projects of $150,000 or more, and 56% of renovating homeowners owned their homes outright. That’s a buyer with equity and time to deliberate, which is exactly why the consideration cycle runs long.</p>"""),

        ("Kitchen remodeling marketing ideas built for a long decision", f"""<p>A kitchen buyer usually moves through the same stages: saving photos, shortlisting three or four remodelers, a design consultation, proposals and financing, then a signature. That can take a few months or more than a year. Most remodelers market only to the last stage and lose the people who weren’t ready the day they clicked.</p>
<!--fig:cycle-->
<p>Marketing ideas that fit each stage:</p>
<ul><li><b>Inspiration stage:</b> short before/after videos on Instagram and YouTube, a Houzz profile full of finished local projects, and project pages on your site that Google can index.</li>
<li><b>Shortlist stage:</b> Google search ads and a strong Business Profile, so you’re one of the names they write down.</li>
<li><b>Consult stage:</b> a design-consult offer with a clear deliverable, like “a floor plan and a budget range in 10 days,” rather than “free estimate.”</li>
<li><b>Proposal stage:</b> retargeting and email that answer the questions people sit on: timeline, what living through a remodel is like, how RDRC approval works in The Woodlands, financing.</li></ul>
<p>Pool builders deal with the same long cycle. Our <a href="/blog/pool-builder-marketing-houston-the-woodlands/">pool builder marketing guide</a> walks through working backward from a finish date, which works the same way for a kitchen promised before the holidays.</p>"""),

        ("Before/after video and project pages that sell a $90,000 kitchen", """<p>Nobody signs a six-figure contract from a paragraph. They sign because they saw a kitchen like theirs, in a house like theirs, finished by a crew that looked like it knew what it was doing.</p>
<p>A simple video plan that a small company can actually keep up:</p>
<ol><li><b>Shoot the “before” every time</b>, from the same three spots, before demo. Phone, horizontal and vertical. This is the step everybody forgets.</li>
<li><b>Capture one or two mid-project clips</b>: the wall coming out, cabinets going in, a tile detail.</li>
<li><b>Shoot the “after” from the same three spots</b> in good daylight, plus a slow 60-second walkthrough.</li>
<li><b>Cut three versions:</b> a 15 to 30 second vertical before/after for Reels and Shorts, a 60 to 90 second walkthrough for YouTube and your site, and stills for Houzz and Google.</li>
<li><b>Ask the homeowner for a one-minute on-camera review</b> at the final walkthrough. Video reviews from a real neighbor beat any script.</li></ol>
<p>Then give every project its own page with the video embedded, the scope, the budget range, the timeline and who handled permits and HOA approval. For page structure that converts, see <a href="/blog/landing-pages-101/">Landing Pages 101</a>. If you’d rather not shoot it yourselves, our <a href="/services/creative-branding/">creative team</a> produces this kind of project content.</p>"""),

        ("Houzz vs. Instagram vs. Google for kitchen and bath marketing", """<p>Each channel catches the buyer at a different stage. Here’s how we’d split time and money for a Woodlands-area kitchen and bath company:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Channel</th><th>Buyer stage</th><th>What to post or run</th><th>How you pay</th><th>Our take</th></tr></thead>
<tbody>
<tr><td>Houzz</td><td>Inspiration, shortlist</td><td>Full project galleries, reviews, credentials</td><td>Free profile; paid Pro tier</td><td>Keep the profile complete; make paid prove itself</td></tr>
<tr><td>Instagram and Facebook</td><td>Inspiration, retargeting</td><td>Before/after Reels, crew clips, finished walkthroughs</td><td>Free posting; ads by impression</td><td>Best for staying top of mind during a long decision</td></tr>
<tr><td>YouTube</td><td>Inspiration, proposal</td><td>Full walkthroughs and “what it cost” explainers</td><td>Free; ads by view</td><td>Underused by local remodelers, so easier to stand out</td></tr>
<tr><td>Google search ads</td><td>Shortlist</td><td>Ads on project and city searches to matching pages</td><td>Per click</td><td>The highest-intent paid channel you can buy</td></tr>
<tr><td>Google Business Profile</td><td>Shortlist, consult</td><td>Weekly project photos, posts, reviews</td><td>Free</td><td>Non-negotiable; it’s where many calls start</td></tr>
</tbody></table></div>
<p>If you only have budget and time for two, pick Google (search ads plus your profile) and Instagram. Houzz is the third, and it’s worth it mainly for the profile.</p>"""),

        ("Kitchen remodeling PPC: Google Ads keyword themes that find buyers", f"""<p>Kitchen remodeling PPC works when the campaign is built around project intent and ticket size, not one big “remodeling” ad group. These themes are where we’d start for a high-end kitchen and bath company:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Campaign</th><th>Keyword themes</th><th>Send clicks to</th></tr></thead>
<tbody>
<tr><td>Kitchen remodel, by city</td><td>kitchen remodel the woodlands, kitchen remodeling kingwood, kitchen renovation spring tx</td><td>Kitchen service page with local projects</td></tr>
<tr><td>Kitchen design</td><td>kitchen designer near me, custom kitchen design, open concept kitchen remodel</td><td>Design consult page</td></tr>
<tr><td>Primary bath</td><td>primary bathroom remodel, walk-in shower remodel, curbless shower installation</td><td>Bathroom service page</td></tr>
<tr><td>Aging in place</td><td>aging in place bathroom, accessible shower remodel, universal design bathroom</td><td>Aging-in-place page</td></tr>
<tr><td>Brand</td><td>your company name and misspellings</td><td>Homepage or contact page</td></tr>
</tbody></table></div>
<p>Settings we’d check in any kitchen and bath account:</p>
<ul><li><b>Negative keywords from day one:</b> ideas, pictures, cheap, diy, ikea, home depot, lowes, cabinets for sale, jobs, salary, rental, plus “refacing” and “countertops only” if you don’t sell them on their own.</li>
<li><b>Location set to “Presence: people in or regularly in your targeted locations,”</b> so you aren’t paying for someone in another state researching kitchens.</li>
<li><b>Separate budgets for kitchen and bath.</b> Bath campaigns usually get more, cheaper leads and will eat the whole budget if you let them share.</li>
<li><b>Exact and phrase match first.</b> Broad match on “kitchen” finds a lot of people shopping for toasters.</li>
<li><b>Ad copy with a price frame and your process:</b> “Most kitchens $60K to $150K. Design, RDRC approval and build, one team.”</li></ul>
<p>Google’s Local Services Ads also cover kitchen and bathroom remodeling ({SRC['lsa']}). They’re worth testing for bath work; for high-end kitchens, search ads give you more control over who you reach. Our <a href="/services/search-marketing/">Google Ads team</a> builds and manages these campaigns.</p>"""),

        ("Bathroom remodeling marketing: a smaller ticket and a faster decision", f"""<p>Bathroom remodeling marketing runs on the same pieces with a shorter clock. A midrange bath in the region averaged $22,995 in the Cost vs. Value data, and a universal design bath (wider doors, a curbless shower, grab bars built in) averaged $42,183 in the {SRC['cvvnat']}. Homeowners often decide on a primary bath in weeks, not months.</p>
<p>A few adjustments for bath campaigns:</p>
<ul><li>Lead with timeline (“most primary baths finished in four to six weeks”), because living without the main shower is the biggest fear.</li>
<li>Split hall-bath refreshes from primary-bath remodels in your ads and forms. They’re different budgets and often different buyers.</li>
<li>Use aging-in-place as its own campaign and page. These buyers search differently, respond well to video of a finished curbless shower, and care about safety more than tile.</li>
<li>Expect more competition from tub-to-shower franchises on price. Your answer is design, reviews and finished local work, not a lower number.</li></ul>"""),

        ("Financing messaging that helps without breaking ad rules", f"""<p>Financing helps close kitchens, but most of these buyers don’t lead with it. In the Houzz study, 84% of renovating homeowners paid with savings, 29% used credit cards and 12% took out a secured home loan, per {SRC['houzz2']}. Higher-end projects were the most likely to use loans of $50,000 to $200,000.</p>
<!--fig:pay-->
<p>So mention financing, but don’t make it the headline for a Woodlands kitchen campaign. “Financing available” on the project page and in follow-up email is enough for most of this audience.</p>
<p>If you do advertise payments, the wording has rules attached:</p>
<ul><li><b>Truth in Lending.</b> Under {SRC['regz']}, phrases like “payments as low as $299 a month” or “terms up to 120 months” require nearby disclosure of the APR and repayment terms. Get the exact wording from your finance partner, and use “financing available” in ads if you can’t fit the disclosure.</li>
<li><b>Meta’s special ad categories.</b> Per {SRC['loomer']}, Meta’s housing category lists “housing repairs” and its credit category lists “long-term financing.” Ads in those categories can’t target by ZIP code, age or gender and need at least a 15-mile radius, per {SRC['metadev']}. A financing-led ad aimed only at affluent ZIP codes is the kind Meta may reject. Our pool builder guide covers how to work within this.</li></ul>"""),

        ("Retargeting and nurturing for six- to twelve-month decisions", f"""<p>Retargeting is how you stay in the room while a homeowner thinks it over. {SRC['gads']} in an audience segment for up to 540 days, but the default is 30. For a kitchen buyer who takes nine months, a 30-day list forgets them before they’ve finished collecting bids. Change it. For the basics of how it works, see <a href="/blog/retargeting-explained/">retargeting explained</a>.</p>
<!--fig:nurture-->
<p>A nurture sequence doesn’t need to be fancy. A monthly email with one finished project, one useful explainer (“How RDRC approval works in Alden Bridge,” “What it’s like to live through a kitchen remodel”), and an invitation to a showroom visit or a design consult will keep you on the shortlist. Showroom events and open houses at a just-finished project, with the homeowner’s blessing, are some of the best offline conversion points this business has.</p>"""),

        ("The number that matters: cost per signed project", f"""<p>A kitchen and bath company can have great-looking lead numbers and an awful cost per signed project, or the reverse. Measure the whole chain. Say you spend $4,000 a month on Google Ads and get 40 leads at $100 each. Fourteen book a design consult, six get a proposal and two sign kitchens at $85,000. Your cost per signed project is $2,000, about 2.4% of the contract value. That’s a healthy number, even though $100 a lead might have looked expensive to you.</p>
<p>To see it in Google Ads, mark consults and signed contracts as offline conversions and import them, so Google learns to find people who sign, not people who fill out forms. Use call tracking so phone leads aren’t invisible. Our guide to <a href="/blog/understanding-cost-per-lead/">cost per lead</a> covers the math in more detail.</p>
<p>Before next month’s budget meeting, pull your last ten signed kitchen and bath projects, write down where each one came from, and set that list beside where the ad money went. They rarely match on the first try. Two settings are worth a look while you’re in there: how long your website audiences last, and whether any Meta ads that mention remodeling or financing are running under the right special ad category. Our free <a href="/contact/">Ad Spend Leak Check</a> covers both, in a 10-minute recorded walkthrough of your Google or Meta account that arrives within 48 hours. You can read more about how we work with remodelers and other trades on our <a href="/industries/service/">home services page</a>.</p>"""),
    ],
    "faq": [
        ("What is the best marketing for a kitchen remodeling company?",
         "For high-end kitchens, the best mix is finished local projects shown in video and on individual project pages, Google search ads on project and city terms, a Google Business Profile updated with weekly photos and reviews, and retargeting plus monthly email for the months homeowners take to decide. Measure cost per signed project, because cheap leads that never sign cost more than expensive leads that do."),
        ("How much should a remodeling company spend on marketing?",
         "Many remodelers budget a few percent of revenue, but a better approach is to work from signed jobs. Decide what you can afford to spend to sign one kitchen or bath, then multiply by the number of projects you want each month. A company signing four $80,000 kitchens a month can justify far more ad spend than one doing four $15,000 hall baths."),
        ("Does Google Ads work for kitchen remodelers?",
         "Yes, when the campaigns are split by project type, use exact and phrase match keywords with a strong negative list, and send clicks to a kitchen page with real local projects. It works poorly when one broad remodeling campaign sends everyone to the homepage. Import signed contracts as offline conversions so Google learns to find buyers instead of browsers."),
        ("Is Houzz or Instagram better for kitchen and bath marketing?",
         "They do different jobs. Houzz is where design-minded homeowners compare remodelers and read reviews, so a complete free profile matters. Instagram keeps you in front of people during a long decision with before and after Reels and retargeting ads. Most kitchen and bath companies should keep a strong Houzz profile and spend their time and ad money on Instagram and Google."),
        ("Should I advertise financing for kitchen remodels?",
         "Mention it, but don't lead with it for high-end buyers. The 2025 Houzz study found most renovating homeowners paid with savings. If an ad states a monthly payment or loan term, federal Truth in Lending rules require APR and repayment disclosures nearby, and Meta may require a special ad category with limited targeting. Financing available on the page and in follow-up email is usually enough."),
    ],
    "figures": {
        "costs": {
            "type": "bars",
            "title": "Average remodel cost in Texas’s region, 2025",
            "sub": "West South Central averages, Cost vs. Value Report",
            "items": [
                ["Midrange bath", 22995, "$22,995"],
                ["Minor kitchen", 26762, "$26,762"],
                ["Upscale bath", 73185, "$73,185"],
                ["Major kitchen", 77742, "$77,742"],
                ["Upscale kitchen", 151557, "$151,557"],
            ],
            "highlight": [4],
            "note": "Source: Remodeling/JLC Cost vs. Value 2025",
            "alt": "Bar chart of average kitchen and bathroom remodel costs in the Texas region for kitchen remodeling marketing in The Woodlands",
            "caption": f"An upscale kitchen recouped just 34.6% at resale in the region ({A('https://www.jlconline.com/cost-vs-value/2025/west-south-central/', 'Cost vs. Value 2025')}).",
        },
        "cycle": {
            "type": "funnel",
            "title": "How a high-end kitchen buyer decides",
            "stages": [
                ["Saving photos and ideas", "Months 1-6"],
                ["Shortlisting remodelers", "3-4 names"],
                ["Design consultation", "1-2 meetings"],
                ["Proposal and financing", "2-8 weeks"],
                ["Signed contract", "1 winner"],
            ],
            "note": "Illustrative example",
            "alt": "Funnel showing the long consideration cycle a homeowner follows, a key part of kitchen remodeling marketing in The Woodlands",
            "caption": "Most remodelers only market to the bottom two stages.",
        },
        "pay": {
            "type": "stats",
            "title": "How renovating homeowners paid",
            "stats": [
                ["84%", "used savings"],
                ["29%", "used credit cards"],
                ["12%", "took a secured home loan"],
                ["56%", "owned their home outright"],
            ],
            "note": "Source: 2025 U.S. Houzz & Home Study, 2024 projects",
            "alt": "Stat tiles on how homeowners paid for renovations, useful for kitchen and bathroom remodeling marketing and financing ads",
            "caption": f"Figures from the Houzz study as reported by {A('https://www.contractormag.com/bath-kitchen/article/55285019/houzz-home-renovation-activity-remains-strong-amid-softening-spend', 'Contractor magazine')}.",
        },
        "nurture": {
            "type": "steps",
            "title": "A nurture plan for kitchen and bath leads",
            "sub": "What happens after the first click or call",
            "steps": [
                ["Extend audiences", "Set Google Ads website segments to 540 days and build Meta site audiences."],
                ["Retarget with projects", "Show finished local kitchens and baths, not discounts."],
                ["Send a monthly email", "One project, one explainer, one consult or showroom invite."],
                ["Offer a real consult", "A floor plan and budget range in ten days beats a free estimate."],
                ["Track to signature", "Log consults, proposals and signed jobs back to the source."],
            ],
            "alt": "Five-step nurture plan for kitchen remodeling marketing leads in The Woodlands, from retargeting to signed contract",
            "caption": "The remodeler who is still in touch in month nine usually gets the job.",
        },
    },
}

POSTS = [POST1, POST2]
