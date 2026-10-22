"""Batch 7 (agency intent): a 12-point self-audit for Google Ads that get clicks but no calls, and who owns your
marketing accounts when you hire (and leave) an agency.

Research: Google Ads help on location options (Presence or interest is the default), the Search Network (search
partners on by default), learning period duration (up to 7 days, 1-2 conversion cycles, what triggers it), Tag
Assistant troubleshooting, website call conversions, call details report fields (call status missed/received),
enhanced conversions for leads; Search Engine Roundtable on the July 2026 conversion status names; Search Engine Land
and PPC Land on PMax negatives (10,000) and 2025 search terms/channel reporting. Ownership post: Google Ads access
levels, manager-account ownership and unlinking pages, Google third-party policy, GA4 "Move a property", Business
Profile owners/managers and request-access pages, ICANN registrant FAQ, Domain Incite on the 2025 Transfer Policy
vote, Leadsie on Meta ad account portability, FCC porting guide, U.S. Copyright Office Circular 30.
Competitors read: ClicksGeek (clicks but no calls), forum threads on agencies withholding Ads access.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "loc": A("https://support.google.com/google-ads/answer/1722038?hl=en", "Google’s location options documentation"),
    "net": A("https://support.google.com/google-ads/answer/1722047?hl=en", "Google’s Search Network help page"),
    "learn": A("https://support.google.com/google-ads/answer/13020501", "Google’s learning period page"),
    "ta": A("https://support.google.com/google-ads/answer/10989978?hl=en", "Tag Assistant troubleshooter"),
    "status": A("https://www.seroundtable.com/google-ads-conversion-tracking-status-updates-41668.html", "Search Engine Roundtable"),
    "webcall": A("https://support.google.com/google-ads/answer/6095883?hl=en", "website call conversions"),
    "calldet": A("https://support.google.com/google-ads/answer/9099302", "call details report"),
    "ecl": A("https://support.google.com/google-ads/answer/15713840?hl=en", "enhanced conversions for leads"),
    "pmaxneg": A("https://searchengineland.com/google-ads-expands-negative-keyword-limits-pmax-453154", "Search Engine Land"),
    "pmax25": A("https://ppc.land/google-wraps-up-performance-max-feature-rollouts-in-2025/", "PPC Land’s 2025 recap"),
    # ownership post
    "levels": A("https://support.google.com/google-ads/answer/9978556?hl=en", "Google’s access level page"),
    "mccown": A("https://support.google.com/google-ads/answer/7476552?hl=en", "Google’s manager account documentation"),
    "unlink": A("https://support.google.com/google-ads/answer/7458428?hl=en", "unlinking rules"),
    "third": A("https://support.google.com/adspolicy/answer/6086450", "third-party policy"),
    "ga4move": A("https://support.google.com/analytics/answer/9305872?hl=en-GB", "Google’s rules for moving a property"),
    "gbproles": A("https://support.google.com/business/answer/3403100?hl=en", "Google’s owners and managers page"),
    "gbpreq": A("https://support.google.com/business/answer/4566671?hl=en", "request-access process"),
    "icann": A("https://www.icann.org/resources/pages/name-holder-faqs-2017-10-10-en", "ICANN’s registrant FAQ"),
    "di": A("https://domainincite.com/tag/transfers-policy", "Domain Incite"),
    "leadsie": A("https://help.leadsie.com/article/131-add-ad-account-meta-business-portfolio", "Leadsie’s summary of Meta’s rules"),
    "fcc": A("https://www.fcc.gov/sites/default/files/porting_-_keeping_your_phone_number_when_you_change_providers.pdf", "FCC’s porting guide"),
    "circ30": A("https://www.copyright.gov/circs/circ30.pdf", "U.S. Copyright Office Circular 30"),
}

AUDIT = "/blog/google-ads-not-converting-clicks-no-calls/"
OWN = "/blog/who-owns-google-ads-account-switch-agencies/"

POSTS = [
    # ------------------------------------------------------------------ post 1: clicks, no calls
    {
        "slug": "google-ads-not-converting-clicks-no-calls",
        "title": "Google Ads Not Converting? A 12-Point Audit for Clicks With No Calls",
        "seo_title": "Google Ads Not Converting? A 12-Point Self-Audit",
        "desc": "Google Ads not converting? Getting clicks but no calls? Run our 12-point self-audit, with real settings and a score sheet, built for Houston-area businesses.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Tag Manager", "Google Analytics"],
        "art": "b2",
        "hero": "tools",
        "hero_alt": "Illustration of tools on a workbench for a Google Ads not converting self-audit for Houston businesses",
        "related": ["call-tracking-which-ads-make-phone-ring", "performance-max-vs-search-campaigns-local", "google-ads-management-houston-cost"],
        "sections": [
            (None, f"""<p>Your Google Ads dashboard says 412 clicks last month. Your phone says nine calls, and two of those were someone offering to “get you to the top of Google.”</p>
<p>When Google Ads is getting clicks but not converting, the cause is almost always one of four things. Tracking doesn’t record what really happens, or you’re paying for traffic you shouldn’t, or the page and the phone line drop the people who did want you. The fourth is a bid strategy and budget that never had enough data to learn. Check them in that order, tracking first, because every other number in the account leans on it.</p>
<p>This is the self-audit we run when an owner in The Woodlands, Spring or anywhere around Houston sends us that exact complaint. Twelve checks with the real menu paths, plus a score sheet at the end. Budget an afternoon.</p>
<p>You don’t need us for any of it.</p>
<p>(If you’re brand new to the platform, our {f'<a href="/blog/small-business-guide-google-ads-2026/">small business guide to Google Ads</a>'} covers the basics. This post assumes the account is already spending.)</p>"""),

            ("Why are my Google Ads getting clicks but no calls?", f"""<p>Because something between the click and the ringing phone is broken, and the account can’t tell you which piece on its own. Clicks are counted perfectly. Calls and form fills are only as real as your tracking, so a campaign can look dead when it’s working, or healthy while it buys junk.</p>
<p>Order matters. If you start by rewriting ads while the conversion tag has been dead since your website update in March, you’re tuning a car with no speedometer.</p>
<!--fig:order-->
<p>Know what “working” means before you judge anything. Our post on {f'<a href="/blog/understanding-cost-per-lead/">understanding cost per lead</a>'} shows how to set a target from your close rate and average job.</p>"""),

            ("Checks 1 and 2: Is conversion tracking actually firing?", f"""<h3>Check 1: Form and website conversions</h3>
<p>In Google Ads, go to <b>Goals → Summary</b> and look at the tracking status beside each conversion action. Google renamed these in mid-2026: you’ll now see <b>Active</b>, <b>Needs attention</b>, <b>Misconfigured</b>, <b>Awaiting conversions</b> (nothing recorded in the last seven days) or <b>Removed</b>, according to {SRC['status']}. Anything other than Active on your main lead action is your first job.</p>
<p>Then test it yourself, on your phone:</p>
<ol><li>Hover over the status and choose <b>Troubleshoot</b>. That opens Google’s {SRC['ta']}.</li>
<li>Enter your landing page URL, click <b>Connect</b>, and submit your own form with a real-looking test entry.</li>
<li>Watch whether Tag Assistant detects the conversion. If you use Tag Manager, you may need <b>Debug live version</b> first.</li>
<li>Give it about 30 minutes, then check the status again.</li></ol>
<p>Around here, the most common culprit is a site redesign that quietly dropped the tag. A form plugin that stopped redirecting to its thank-you page is a close second. The sneaky one is a “conversion” that fires on <i>any</i> visit to the contact page, which makes the account look great while nobody actually contacts you.</p>
<p>Also check which actions are set as <b>Primary</b>. Smart bidding chases primary actions, so if “page view” or “clicked directions” is primary, Google will happily buy you more of those. We’d limit primary to real leads, like submitted forms and calls over a minimum length.</p>
<p>Once forms are clean, look at {SRC['ecl']}. It sends hashed email or phone details from your form and lets you import which leads became real customers from your CRM, so Google learns from sales rather than raw form fills. For a roofer whose form fills are half price shoppers, it’s worth the setup time.</p>

<h3>Check 2: Phone calls</h3>
<p>Most local businesses get more calls than forms, and calls are where tracking is usually thinnest. Start with taps on the call button in the ad itself (a call asset). Set a minimum call length so a two-second hang-up doesn’t count; we usually start at 60 to 90 seconds for home services.</p>
<p>Calls from people who clicked through to your site are separate. Google’s {SRC['webcall']} swap your number for a Google forwarding number for ad visitors, at no cost, and count calls longer than the length you choose.</p>
<p>The most complete option, and the one we prefer, is a call-tracking tool such as CallRail with calls imported as conversions. Our post on {f'<a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking</a>'} covers how to do it without messing up your Business Profile number.</p>
<p>If calls aren’t tracked at all, stop and fix that first. Judging a local campaign without call data is guessing.</p>"""),

            ("Checks 3 and 4: Search terms, negatives and match types", f"""<h3>Check 3: Read the search terms report</h3>
<p>Go to <b>Campaigns → Insights and reports → Search terms</b>, set the date range to the last 60 or 90 days, and sort by cost. This is the single most useful report in Google Ads, and the one most owners have never opened.</p>
<p>Say you run a pool service in Magnolia. Expect to find searches like “pool supply store near me,” “above ground pool,” “pool cleaner jobs,” “how to get rid of green pool water,” and a competitor’s name or two. Each of those is a click you paid for that was never going to call.</p>
<p>Add the obvious losers as negative keywords. Build a shared negative list for the usual suspects (jobs, salary, hiring, DIY, “how to,” free, cheap if you don’t compete on price, cities you don’t serve) and apply it to every campaign. Then review again every two weeks.</p>
<h3>Check 4: Match types that fit your data</h3>
<p>Broad match can work well when it’s paired with smart bidding and accurate conversion data. With broken tracking or a thin budget, it’s a fire hose. If your account has fewer than a few dozen real conversions a month, we’d run phrase and exact match on your core services and add broad later, in a separate campaign, once tracking is trustworthy.</p>
<p>If most of your search terms look nothing like your keywords, your match types are looser than your data can support.</p>"""),

            ("Checks 5 to 7: Location, ad schedule and networks", f"""<h3>Check 5: Location setting</h3>
<p>Open the campaign’s <b>Settings → Locations → Location options</b>. Per {SRC['loc']}, the default is <b>Presence or interest</b>, which reaches people in your area <i>plus</i> people who have shown interest in it. The other option, <b>Presence</b>, limits ads to people who are in, or regularly in, your targeted locations.</p>
<p>For a Kingwood roofer, “interest” can mean someone in Ohio reading about Houston hail. Switch service businesses to Presence. Then go to <b>Insights and reports → When and where ads showed → Locations</b> and look at where clicks actually came from. Also check the shape of your target: a 30-mile radius drawn around The Woodlands takes in a lot of Harris County you may not want to drive to at 5 p.m. on I-45. A list of zip codes or cities you actually serve is often cleaner.</p>
<h3>Check 6: Ad schedule vs. who answers the phone</h3>
<p>This is the one most shops get wrong. Ads run around the clock by default. If your phones are answered 7 to 6 on weekdays, every call-button tap at 9 p.m. or on Sunday goes to voicemail, and most people don’t leave one. They call the next ad.</p>
<p>Under <b>Ad schedule</b>, either limit ads to staffed hours, or keep running after hours with call assets scheduled to your open hours and a form as the main action. For emergency trades (AC in August, a burst pipe on a holiday weekend), an answering service often pays for itself.</p>
<h3>Check 7: Search partners and Display</h3>
<p>{SRC['net']} says plainly that “search partners are included by default” when you create a Search campaign, and that clicks from them “may not always reflect highly targeted traffic.” Many Search campaigns also have the <b>Display Network</b> box ticked from setup.</p>
<p>Add the <b>Network</b> segment to your campaign view and compare cost per conversion by network. If partners or Display spend money with no leads, turn them off. We’d start most local Search campaigns with both unchecked and only test partners later.</p>
<!--fig:leaks-->"""),

            ("Check 8: Is Performance Max spending your budget somewhere else?", f"""<p>Performance Max can show your ads on Search, Maps, YouTube, Display, Gmail and Discover from one campaign. That reach is the appeal. It’s also how a $3,000 month can turn into a pile of YouTube views and junk form fills.</p>
<p>At least you can see far more than you could a couple of years ago. Google added channel-level reporting and full search terms visibility for PMax in 2025, according to {SRC['pmax25']}, and raised the PMax negative keyword limit to 10,000 per campaign, per {SRC['pmaxneg']}.</p>
<p>Open channel performance first. How much went to Search, how much to YouTube and Display, and where did the conversions actually come from? Then read the search terms. If PMax is mostly buying your own brand name, you’re paying for traffic you’d likely get anyway.</p>
<p>Lead quality won’t show up in any report. PMax lead forms and Display placements can produce names with fake numbers, so call ten of last month’s PMax leads and count the real ones.</p>
<p>We’ve written a full comparison in {f'<a href="/blog/performance-max-vs-search-campaigns-local/">Performance Max vs. Search for local businesses</a>'}. For most single-location service businesses, we’d run Search first and add PMax once tracking is clean.</p>"""),

            ("Checks 9 and 10: The landing page and the phone", f"""<h3>Check 9: The landing page</h3>
<p>Click your own ad on your phone, on cellular data, in a parking lot. (Not on the office Wi-Fi, which flatters everything.) Then ask:</p>
<ul><li>Did the page load before you got bored? Our guide on {f'<a href="/blog/how-fast-should-your-website-load/">how fast your website should load</a>'} has the targets and the usual fixes.</li>
<li>Is a tap-to-call number visible without scrolling?</li>
<li>Does the headline match what the person searched? An ad for “AC repair Spring TX” shouldn’t land on a homepage about “comfort solutions.”</li>
<li>Is the form short? Name, phone, a few words on the problem, and zip code is plenty for a first contact.</li>
<li>Can they see reviews and your real trucks or team?</li></ul>
<p>If two or more of those are a no, the page is costing you leads. Our {f'<a href="/blog/landing-pages-101/">landing pages 101</a>'} post walks through a better layout.</p>
<h3>Check 10: Who answers, and how fast</h3>
<p>Google records this for you. Go to <b>Insights and reports → Report editor → Call details</b>. The {SRC['calldet']} lists start time, duration, caller area code and <b>call status: missed or received</b> for calls from your ads. Filter to missed calls. Sort by start time. The pattern is usually lunch hour, early morning and the last hour of the day.</p>
<p>The math is what gets owners’ attention. Say a two-truck HVAC shop in Spring gets 40 ad calls a month at about $45 each, misses a quarter of them, and books 40% of the calls it does answer at a $450 average ticket. Those 10 missed calls cost $450 in ad spend and roughly $1,800 in jobs that probably went to the next company on the page. The numbers are illustrative. Plug in yours.</p>
<!--fig:missed-->
<p>Forms have the same problem with a different clock. A form answered tomorrow morning is a form somebody else answered tonight. Set up a text or email alert for every new lead, and decide who owns the callback.</p>"""),

            ("Checks 11 and 12: Bid strategy learning and a budget that’s too thin", f"""<h3>Check 11: Is the bid strategy learning, or stuck?</h3>
<p>Look at the <b>Bid strategy type</b> column on the campaigns page. If it says <b>Learning</b>, that status can last up to seven days, and Google says performance typically settles “within 1 to 2 conversion cycles,” per {SRC['learn']}. Learning starts again when the strategy is new or reactivated, when campaigns or keywords are added to or removed from it, or when the conversion goals it optimizes toward change significantly. Budget and target changes don’t trigger it.</p>
<p>The pattern we see: an owner (or an impatient agency) swaps from Maximize Clicks to Maximize Conversions to Target CPA in three weeks, while also changing which conversions count. The strategy never gets a clean run. Fix tracking, pick one strategy and leave it alone for a few conversion cycles. Yes, even when week two looks ugly.</p>
<p>Smart bidding on bad tracking is worse than manual bidding on no tracking. If Check 1 or 2 failed, we’d drop to Maximize Clicks with a sensible max CPC, or manual CPC, until the data is real.</p>
<h3>Check 12: Is the budget too thin to learn anything?</h3>
<p>Divide your monthly budget by your average cost per click. At $600 a month and $12 a click you get 50 clicks, under two a day. At a 5% lead rate (illustrative), you’d expect two or three leads a month, and a slow week looks the same as a broken campaign.</p>
<p>You have two honest choices. Raise the budget to what your market costs, or shrink the campaign to fit the budget: one service, one tight area, exact and phrase match only, staffed hours only. Our breakdown of {f'<a href="/blog/google-ads-management-houston-cost/">Google Ads costs in Houston</a>'} has typical ranges. We’d rather see $600 spent well on “water heater replacement” in three zip codes than spread across eight services and the whole metro.</p>"""),

            ("Google Ads audit checklist: score your account", f"""<p>Score each line 0, 1 or 2. Be honest; nobody’s grading you.</p>
<div class="bp-tbl"><table>
<thead><tr><th>#</th><th>Check</th><th>Where to look</th><th>2 points if…</th></tr></thead>
<tbody>
<tr><td>1</td><td>Form conversions firing</td><td>Goals → Summary, Tag Assistant</td><td>Status is Active and your own test was recorded</td></tr>
<tr><td>2</td><td>Calls tracked</td><td>Goals → Summary, call assets</td><td>Ad calls and website calls both counted, with a minimum length</td></tr>
<tr><td>3</td><td>Search terms clean</td><td>Insights and reports → Search terms</td><td>Under 10% of spend on irrelevant terms, negatives reviewed in the last 30 days</td></tr>
<tr><td>4</td><td>Match types fit data</td><td>Keywords</td><td>Search terms mostly resemble your keywords</td></tr>
<tr><td>5</td><td>Location option</td><td>Settings → Locations</td><td>Presence only, and clicks come from areas you serve</td></tr>
<tr><td>6</td><td>Ad schedule</td><td>Ad schedule, call asset hours</td><td>Call buttons only show when someone answers</td></tr>
<tr><td>7</td><td>Networks</td><td>Settings → Networks, Network segment</td><td>Partners and Display off, or proven to convert</td></tr>
<tr><td>8</td><td>PMax leakage</td><td>Channel performance, search terms</td><td>Spend and leads by channel make sense; brand terms controlled</td></tr>
<tr><td>9</td><td>Landing page</td><td>Your phone, on cellular</td><td>Loads fast, call button visible, headline matches the ad</td></tr>
<tr><td>10</td><td>Call handling</td><td>Report editor → Call details</td><td>Under 10% of ad calls missed, forms answered same day</td></tr>
<tr><td>11</td><td>Bid strategy stable</td><td>Bid strategy type column</td><td>Same strategy and goals for at least a few conversion cycles</td></tr>
<tr><td>12</td><td>Budget fits scope</td><td>Budget ÷ average CPC</td><td>At least several clicks a day on each core service</td></tr>
</tbody></table></div>
<p><b>20 to 24:</b> the account is set up right; the problem is probably offer, pricing or competition. <b>13 to 19:</b> fixable leaks, usually in Checks 3, 5, 6 and 10. <b>12 or under:</b> stop changing ads and fix tracking first, because nothing else can be trusted until you do.</p>
<!--fig:sheet-->"""),

            ("Should you fix it yourself or hire help?", f"""<p>Honestly, a lot of this is DIY. Checks 3, 5, 6 and 7 are settings changes most owners can make in under an hour, and they’re often where the fastest wins hide. Check 10 is a staffing conversation, and no agency can fix it for you.</p>
<p>Where outside help earns its fee is the tracking work (Checks 1 and 2, enhanced conversions, call-tracking imports) and the judgment calls: when to trust smart bidding, how to structure PMax, what a realistic cost per lead is in your corner of Houston. If you hire, our post on {f'<a href="/blog/questions-before-hiring-marketing-agency/">questions to ask before hiring an agency</a>'} is a good filter. And before anyone touches the account, make sure it’s actually yours; our guide on {f'<a href="{OWN}">who owns your Google Ads account</a>'} explains how to check.</p>
<p>Next step: open the search terms report today, sort by cost, and add ten negatives. If you’d rather have someone else look first, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video walking through your account, in your inbox within 48 hours. You can see how we run campaigns on our <a href="/services/search-marketing/">Google Ads management</a> page.</p>"""),
        ],
        "faq": [
            ("Why are my Google Ads not converting?", "Usually one of four reasons: conversion tracking is broken or counting the wrong action, you're paying for irrelevant searches or locations, the landing page or phone handling loses people who do want to buy, or the bid strategy and budget are too unstable or too small to learn. Check tracking first, because every other number in the account depends on it, then work through search terms, settings, the page and the phones."),
            ("How do I know if my Google Ads conversion tracking is working?", "Go to Goals, then Summary, and check the tracking status of each conversion action. Active means it's recording. Then run Google's Tag Assistant troubleshooter from that status, submit a test form or place a test call, and confirm the conversion is detected. Allow about 30 minutes for the status to update. If calls aren't tracked at all, set up call conversions before judging results."),
            ("Should I use Presence or Presence or interest in Google Ads?", "For most local service businesses, Presence. The default, Presence or interest, also shows ads to people outside your area who have shown interest in it, which brings clicks from people who will never book a visit. Presence limits ads to people who are in or regularly in your target area. After switching, check the locations report to confirm clicks come from places you serve."),
            ("How long should I wait before judging a Google Ads campaign?", "Give tracking and settings fixes about two to four weeks. Google says a bid strategy's Learning status lasts up to seven days and performance usually settles within one to two conversion cycles. If your sales cycle is long, wait longer. Changing strategies or conversion goals restarts that process, so make one change at a time and judge it against your cost per lead."),
            ("What should be on a Google Ads audit checklist?", "At minimum: conversion tracking for forms and calls, the search terms report and negative keywords, match types, the location option, ad schedule versus staffed hours, search partner and Display settings, Performance Max channel spend, landing page speed and layout, missed calls in the call details report, bid strategy stability, and whether the budget is large enough for the area and services you target."),
        ],
        "figures": {
            "order": {
                "type": "steps",
                "title": "The order we audit a no-calls account",
                "sub": "Fix the measuring stick before you change the campaign",
                "steps": [
                    ["Tracking", "Forms and calls recorded, right actions set as primary."],
                    ["Traffic", "Search terms, match types, location option, networks, PMax."],
                    ["Timing", "Ads and call buttons only when someone answers."],
                    ["Page and phone", "Fast mobile page, short form, missed calls under control."],
                    ["Bidding and budget", "One stable strategy and enough clicks a day to learn."],
                ],
                "alt": "Five-step order for auditing Google Ads not converting into calls, used for Houston and The Woodlands accounts",
                "caption": "Tracking always comes first. Every later check depends on it.",
            },
            "leaks": {
                "type": "funnel",
                "title": "Where 400 clicks can disappear",
                "stages": [["Paid clicks", "400"], ["Relevant searches in your area", "260"], ["Page loads and reads", "200"], ["Call or form attempt", "24"], ["Answered and booked", "9"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how Google Ads clicks shrink to a few booked calls for a Houston-area service business",
                "caption": "Each stage maps to a check in this audit. Your numbers will differ.",
            },
            "missed": {
                "type": "bars",
                "title": "What missed ad calls cost in a month",
                "sub": "40 ad calls, 25% missed, 40% booked, $450 average job",
                "items": [["Ad spend on missed calls", 450, "$450"], ["Jobs lost from missed calls", 1800, "$1,800"], ["An answering service (example)", 300, "~$300"]],
                "highlight": [1],
                "note": "Illustrative example",
                "alt": "Bar chart of missed call costs when Google Ads calls go unanswered at a Spring, TX HVAC company",
                "caption": "Pull your own missed calls from Google Ads’ call details report and redo this math.",
            },
            "sheet": {
                "type": "checklist",
                "title": "Google Ads self-audit, quick version",
                "sub": "Tick each one you can confirm today",
                "items": [
                    "Main lead action shows Active in Goals → Summary",
                    "Calls from ads and from the website both counted",
                    "Search terms reviewed and negatives added this month",
                    "Location option set to Presence",
                    "Ads and call buttons match staffed hours",
                    "Search partners and Display checked by network segment",
                    "PMax channel spend and search terms reviewed",
                    "Landing page tested on a phone over cellular",
                    "Missed ad calls under 10% in call details",
                    "No bid strategy or goal changes in the last few weeks",
                ],
                "alt": "Checklist for a Google Ads audit when ads get clicks but no calls, for businesses in The Woodlands and Houston",
                "caption": "A two-minute version of the score sheet above.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: who owns the accounts
    {
        "slug": "who-owns-google-ads-account-switch-agencies",
        "title": "Who Owns Your Google Ads Account, Website and Domain When You Hire an Agency?",
        "seo_title": "Who Owns Your Google Ads Account? Switch Agencies Safely",
        "desc": "Who owns your Google Ads account, website, domain, GA4 and Business Profile when you hire an agency, and how to switch agencies without losing anything.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google Analytics", "Meta"],
        "art": "b5",
        "hero": "key",
        "hero_alt": "Illustration of a key and lock for a guide to who owns your Google Ads account and website when you hire an agency",
        "related": ["questions-before-hiring-marketing-agency", "diy-vs-hiring-an-agency", "call-tracking-which-ads-make-phone-ring"],
        "sections": [
            (None, f"""<p>The email usually lands on a Friday afternoon. “We’re ending things with our agency. They’re saying the Google Ads account belongs to them. Is that true?”</p>
<p>Sometimes it is. More often, nobody ever decided, and the honest answer depends on whose email address sits in a handful of settings the owner has never seen.</p>
<p>So, who owns your Google Ads account when an agency runs it? You should, along with your website, domain, GA4 property, Google Business Profile, Meta pages and call-tracking numbers, with the agency added as a user or partner. Whether you actually do comes down to who created each account and who holds admin or owner rights today. The time to check is now, while everyone is still friendly.</p>
<p>Our rule with our own clients is simple, and we’d hold any agency you hire to it. The business owns every account and the agency gets access. If the agency vanished tomorrow, nothing would stop working.</p>
<p>Below we go asset by asset, then lay out a 30-day plan for switching agencies without losing your ad history, your reviews or your phone number.</p>"""),

            ("Who owns my Google Ads account if an agency set it up?", f"""<p>The account belongs to whoever has <b>Admin</b> access to it and pays for it. Agencies manage clients through a <b>manager account</b> (still often called an MCC). A manager account linked to yours can see and edit campaigns, but per {SRC['mccown']}, “linking a manager account doesn’t automatically grant administrative ownership.” Some agencies do hold that ownership, and if they do, they can transfer it to another manager account or remove it.</p>
<p>What you want is your own login, on your own business email, with Admin access. Per {SRC['levels']}, Admin users can add and remove users, change access levels, accept or reject manager account link requests, and unlink managers. Standard users can edit campaigns but can’t do those things. Google also notes that an account with a single admin can lose access to tags if that person becomes unavailable, so add a second admin you trust (a partner, your office manager).</p>
<p>How to check, in five minutes:</p>
<ol><li>Sign in at ads.google.com with your own Google account. If you can’t, that’s your answer.</li>
<li>Go to <b>Admin → Access and security</b>. Look at the Users tab for your access level, and the Managers tab for which manager accounts are linked.</li>
<li>Go to <b>Billing → Settings</b> and see whose payments profile and card are on file.</li></ol>
<p>Two billing details catch people. If the agency pays Google and invoices you, your account may run on monthly invoicing through their manager account. Google’s {SRC['unlink']} say an account on that setup stops serving once the paying manager is unlinked, so set up your own billing first. Second, your campaign history stays with the account when a manager is unlinked. That history (years of search terms, conversion data, quality signals) is worth keeping, and it’s the main reason we push clients to own the account rather than start fresh.</p>
<p>Google’s {SRC['third']} for agencies also requires “a separate account for each end-advertiser,” and lists verifying a customer’s account as your own as a significant violation. If your ads run inside an account that also runs other businesses’ ads, you’re a line item in someone else’s account, with nothing to take when you leave.</p>
<!--fig:setup-->"""),

            ("Ownership vs. access: the asset-by-asset table", f"""<p>“Ownership” and “access” get mixed up constantly. Ownership means the asset is in your name or your account and survives without the agency. Access means someone can log in and work on it. You want the first and you give out the second.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Asset</th><th>Who should own it</th><th>What the agency gets</th><th>How to check</th></tr></thead>
<tbody>
<tr><td>Google Ads account</td><td>You, Admin on your business email, your card on file</td><td>Manager account link, or Standard access</td><td>Admin → Access and security; Billing → Settings</td></tr>
<tr><td>Domain name</td><td>You, as registrant, in your own registrar account</td><td>DNS access if needed, never the registrar login</td><td>Registrar account; WHOIS lookup</td></tr>
<tr><td>Hosting and website files</td><td>You, hosting billed to you</td><td>A user login or SFTP</td><td>Hosting invoice; who can download a backup</td></tr>
<tr><td>CMS (WordPress, Squarespace, Wix)</td><td>You, as administrator or site owner</td><td>Editor or contributor login</td><td>Users list in the CMS</td></tr>
<tr><td>GA4 property</td><td>You, Administrator on an account you created</td><td>Editor or Marketer role</td><td>Admin → Account access management</td></tr>
<tr><td>Tag Manager and Search Console</td><td>You, as admin/owner</td><td>Publish or full user</td><td>User management in each tool</td></tr>
<tr><td>Google Business Profile</td><td>You, as primary owner</td><td>Manager role</td><td>Business Profile settings → People and access</td></tr>
<tr><td>Meta business portfolio, Pages, ad account, pixel</td><td>Your portfolio</td><td>Partner access</td><td>Business settings → Accounts and Partners</td></tr>
<tr><td>Call-tracking numbers</td><td>Your call-tracking or carrier account</td><td>User access</td><td>Who gets the invoice for the numbers</td></tr>
<tr><td>Logos, photos, ad creative, site copy</td><td>You, by written assignment</td><td>License to use while working</td><td>The contract</td></tr>
</tbody></table></div>
<p>Go row by row and mark each one “mine,” “theirs” or “no idea.” Every “no idea” is a conversation to have this month.</p>
<!--fig:audit-->
<p>Do the check from your own logins. “Oh, you have access” from the agency doesn’t count until you’ve signed in and seen your name next to the right role.</p>"""),

            ("Your domain name: check the registrant today", f"""<p>If you only fix one thing on this list, fix this one. Your domain controls your website <i>and</i> your email. Whoever controls the registrar account can point both anywhere.</p>
<p>The person or company listed as registrant is the domain holder. Many WHOIS lookups now show “Redacted for privacy,” so the real test is whether you can log in to the registrar (GoDaddy, Namecheap, Squarespace Domains, Cloudflare and so on) with your own account and see the domain listed there.</p>
<p>If the agency registered it in their account, the fastest fix is usually an account change at the same registrar. Most registrars can move a domain from one customer account to another without a transfer.</p>
<p>Moving to a new registrar takes longer. You need an authorization code, and per {SRC['icann']}, your registrar must give it to you within five calendar days of your request. Registrars may refuse a transfer within 60 days of initial registration or a prior transfer, and changes to the registrant name, organization or email can trigger a 60-day lock too.</p>
<p>Those lock rules are being rewritten. ICANN’s policy council voted in March 2025 to drop the 60-day change-of-registrant lock and set a 30-day lock on new and newly transferred domains, per {SRC['di']}, but the new policy takes time to implement. Ask your registrar which rules apply to you before you plan a deadline around them.</p>
<p>DNS is the trap that catches somebody every year. If your domain’s nameservers point to the agency’s Cloudflare or hosting account, your email’s MX records live there too. Before you change anything, export or screenshot every DNS record. Otherwise the website might survive the switch while your email quietly stops arriving.</p>"""),

            ("Website, hosting and CMS: who has the keys?", f"""<p>Websites are messier, because an agency can hold one layer and not another.</p>
<p>Start with hosting. If the agency hosts dozens of client sites on one server and bills you a monthly “care plan,” your site lives in their account. That can be fine while you work together. Make sure the contract says they’ll hand over a full backup (files and database) and help migrate within a set number of days when you leave.</p>
<p>Then the CMS. On WordPress, you want your own Administrator user. On Squarespace or Wix, the site owner should be you, with the agency as a contributor. Watch premium themes and plugins licensed under the agency’s account. They keep working after you leave, but stop updating, which becomes a security problem within a year.</p>
<p>Design and copy are the legal part, and we’re not lawyers. Per {SRC['circ30']}, work by an outside contractor only counts as a “work made for hire” if it falls into one of nine listed categories <i>and</i> both sides sign a written agreement saying so. A website usually doesn’t fit neatly, so the safer route is a contract clause that assigns copyright in the design, code you paid for and content to you on payment. Ask your attorney to look at it.</p>
<p>If a redesign is coming anyway, our post on {f'<a href="/blog/signs-your-website-needs-a-redesign/">signs your website needs a redesign</a>'} helps decide whether to migrate the old site or start over. And our <a href="/services/web-design-seo-pr/">web design service</a> sets every site up in the client’s own hosting account, for exactly this reason.</p>"""),

            ("GA4, Tag Manager and Search Console", f"""<p>GA4 is where agencies most often “own” data without meaning to. Someone creates a property inside the agency’s own Analytics account because it’s quicker, and three years later you discover your history lives somewhere you can’t reach.</p>
<p>Moving a property later is harder than it sounds. {SRC['ga4move']} require Administrator and Editor roles on both the source and destination accounts, and the two accounts must belong to the same Google Marketing Platform organization. Most small businesses don’t have one.</p>
<p>So in practice, get <b>Administrator</b> on the property now, so you can add and remove users yourself. If the agency’s Analytics account holds only your property, have them make you an Administrator at the account level too. If neither happens, create a new property in your own account, run both side by side for a few months, and export the reports you care about from the old one. It’s tedious. It works.</p>
<p>Do the same for Google Tag Manager (you want admin and publish rights on the container) and Search Console (you want to be a verified owner). Tag Manager matters more than people think. Whoever controls it controls your conversion tracking, which is the foundation of everything in our {f'<a href="{AUDIT}">Google Ads self-audit</a>'}.</p>"""),

            ("Google Business Profile: primary owner, owners and managers", f"""<p>Your Business Profile is the asset that’s hardest to replace. The reviews, photos and years of history on it can’t be moved to a new listing. Every profile has exactly one <b>primary owner</b>, can have several owners, and can have managers, per {SRC['gbproles']}. Owners control users and can delete the profile. Managers can edit almost everything but can’t add or remove people.</p>
<p>The setup we recommend: you are primary owner, a second person at your company is an owner, and the agency is a manager. That’s it.</p>
<p>Timing matters if you’re fixing this late. New owners must wait seven days before they can transfer primary ownership or remove other users. So if an agency adds you as owner on day 1, you can’t take primary ownership until day 8. Plan for it.</p>
<p>If the agency won’t respond at all, Google has a {SRC['gbpreq']}: search for your business at business.google.com/add, choose <b>Request access</b>, and the current owner has three days to respond. If they don’t, you may be able to claim the profile, though Google says the option isn’t always available. Whatever you do, don’t create a second profile for the same business. Duplicates are a common path to suspension, which we cover in our {f'<a href="/blog/google-business-profile-suspended-reinstatement/">Business Profile reinstatement guide</a>'}.</p>"""),

            ("Meta business portfolio, Pages and ad accounts", f"""<p>Meta is the platform where an agency-created asset is hardest to get back. According to {SRC['leadsie']}, an ad account created or claimed by a business portfolio can’t be removed or transferred to another portfolio afterward. If your agency created your ad account inside <i>their</i> portfolio, you likely can’t take it with you. You start a new one, and the reporting history stays behind.</p>
<p>Your Facebook Page and Instagram account are more portable, but only if you, as a person, still have full control of them. Check today in <b>Business settings → Accounts</b> in your own portfolio.</p>
<p>The setup we’d insist on:</p>
<ul><li>You create the business portfolio, with two admins from your company.</li>
<li>Your portfolio owns the Page, the Instagram account, the ad account and the pixel (dataset).</li>
<li>Your card is on the ad account.</li>
<li>The agency gets access as a <b>Partner</b>, which you can remove in one click.</li></ul>
<p>If you’re running Meta ads now, our guide to {f'<a href="/blog/facebook-instagram-ads-local-businesses/">Facebook and Instagram ads for local businesses</a>'} covers the campaign side.</p>"""),

            ("Call-tracking numbers and phone porting", f"""<p>Nobody thinks about this one until the line goes dead. Agencies often buy tracking numbers in their own CallRail (or similar) account and put them on your ads, your website, and sometimes your Business Profile and directory listings. When the contract ends and they cancel those numbers, every place they appear now rings nowhere.</p>
<p>Numbers can usually move. Per the {SRC['fcc']}, you can generally keep a number when you change providers if you stay in the same area, you should start service with the new provider before cancelling the old one, simple ports are supposed to be processed in one business day, and the old provider can’t refuse a port over an unpaid balance. The catch for agency-held numbers: the port request comes from the account holder, which is the agency. So ask, in writing, for every tracking number to be ported to your own call-tracking or carrier account before the end date.</p>
<p>Two rules we follow: your main business number is never a tracking number on paper you don’t own, and on your Business Profile a tracking number goes in as primary only with your real number listed as an additional phone. Our {f'<a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking guide</a>'} explains why.</p>
<!--fig:waits-->"""),

            ("Contract clauses to look for, and how to switch marketing agencies", f"""<p>Before you sign with anyone (us included), look for these in the agreement:</p>
<ul><li>All ad, analytics, profile and social accounts are created in the client’s name, or transferred to the client on request.</li>
<li>Copyright in the website, ad creative, photos and copy you paid for passes to you on payment.</li>
<li>You pay Google and Meta directly. If the agency bills media, you get an itemized split of media vs. fees every month.</li>
<li>A notice period you can live with. Thirty days is common; watch for auto-renewing 12-month terms with a short cancellation window.</li>
<li>Exit deliverables (admin access confirmed, backups, DNS records, number ports, reports) due within a set number of business days.</li>
<li>No fee to get your access back. A reasonable charge for migration labor is normal, but you shouldn’t pay ransom for your own accounts.</li></ul>
<p>Our post on {f'<a href="/blog/questions-before-hiring-marketing-agency/">questions to ask before hiring a marketing agency</a>'} adds the performance questions.</p>
<h3>A 30-day offboarding timeline</h3>
<!--fig:timeline-->
<ol><li><b>Day 1 (before you give notice):</b> fill in the ownership table above. Log in to everything you can. Screenshot users, billing and DNS.</li>
<li><b>Days 1 to 7:</b> ask for admin or owner access on anything you don’t own yet, and new owner roles on your Business Profile. Start the seven-day clock.</li>
<li><b>Days 7 to 14:</b> set up your own billing in Google Ads and Meta, start domain and hosting moves, request number ports, and get a full website backup.</li>
<li><b>Days 14 to 21:</b> take primary ownership of the Business Profile, confirm GA4, Tag Manager and Search Console roles, and export reports.</li>
<li><b>Days 21 to 30:</b> give your new agency access, then remove the old one. Unlink their manager account last, after billing is yours.</li></ol>
<p>If an agency refuses access to accounts in your name, stay polite and put the request in writing. Cite the contract. For Google Ads, you can file a report under Google’s third-party policy, and for your Business Profile, use the request-access process. If the domain or site is held hostage, that’s a letter from your attorney.</p>
<p>Next step: spend 20 minutes this week on the table above. If you find gaps and want a second opinion on the Google Ads side, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video of your account, in your inbox within 48 hours, and the first thing we look at is who owns it. More on how we work is on our <a href="/services/search-marketing/">Google Ads management</a> page.</p>"""),
        ],
        "faq": [
            ("Who owns my Google Ads account, me or my agency?", "You should. The account belongs in practice to whoever holds Admin access and pays Google. Ask for your own login with Admin access, check Admin then Access and security to see users and linked manager accounts, and make sure your card is on file. Google's third-party policy also requires agencies to use a separate account for each advertiser they manage."),
            ("How do I transfer my Google Ads account from my agency?", "You usually don't transfer the account itself. Get Admin access on your own email, set up billing in your name if the agency was paying, then unlink the agency's manager account or link your new agency's. Campaign history stays with the account. If the agency's manager account holds administrative ownership, ask them to transfer or remove that ownership."),
            ("What do I do if my agency won't give me access to my website?", "Start with a written request that cites your contract and lists exactly what you need: hosting login, CMS administrator account, a full backup and DNS records. Check whether the domain is registered to you at the registrar. If the agency holds both and refuses, have an attorney send a letter. Meanwhile, keep your Business Profile and ad accounts secured so leads keep coming."),
            ("Can I keep my call-tracking numbers when I switch agencies?", "Usually, if you ask before the contract ends. Tracking numbers sit in whoever's account bought them, so the agency typically has to request the port to your own call-tracking or carrier account. The FCC says simple ports should take one business day and you should not cancel the old service first. Numbers cancelled before porting are often gone for good."),
            ("How do I switch marketing agencies without losing anything?", "Inventory every account before you give notice: Google Ads, GA4, Tag Manager, Search Console, Business Profile, Meta, domain, hosting and tracking numbers. Get admin or owner rights on each, move billing to your name, take backups and DNS records, port numbers, and only then remove the old agency. Allow about 30 days, since some transfers have waiting periods."),
        ],
        "figures": {
            "setup": {
                "type": "compare",
                "title": "Who holds the keys",
                "left": {"title": "Agency-owned setup", "items": ["Ads account in agency’s manager, no client admin", "Domain in the agency’s registrar login", "GA4 property in the agency’s account", "Ad account inside agency’s Meta portfolio", "Tracking numbers on the agency’s bill"]},
                "right": {"title": "Client-owned setup", "items": ["You are Admin, agency linked as manager", "Domain registered to you, your login", "GA4 in your account, agency as editor", "Your Meta portfolio, agency as partner", "Numbers in your call-tracking account"]},
                "alt": "Comparison of agency-owned and client-owned Google Ads, domain, GA4 and Meta setups for Houston businesses",
                "caption": "The right-hand column is what we recommend to every business we talk to.",
            },
            "waits": {
                "type": "bars",
                "title": "Waiting periods when you switch",
                "sub": "Plan your agency exit around these",
                "items": [["Simple phone number port", 1, "1 business day"], ["GBP owner response to access request", 3, "3 days"], ["Registrar must give auth code", 5, "5 days"], ["New GBP owner before primary transfer", 7, "7 days"], ["Possible domain transfer lock", 60, "up to 60 days"]],
                "highlight": [4],
                "note": "Source: FCC, Google Business Profile Help, ICANN",
                "alt": "Bar chart of waiting periods for switching marketing agencies, from phone ports to domain transfer locks",
                "caption": f"From the {SRC['fcc']}, Google’s Business Profile help and {SRC['icann']}. Domain lock rules are changing.",
            },
            "timeline": {
                "type": "steps",
                "title": "A 30-day agency switch",
                "sub": "Start before you give notice",
                "steps": [
                    ["Day 1", "List every account, screenshot users, billing and DNS."],
                    ["Days 1-7", "Request admin and owner access; start the GBP 7-day clock."],
                    ["Days 7-14", "Your billing in Ads and Meta, domain moves, number ports, backups."],
                    ["Days 14-21", "Take GBP primary ownership, confirm GA4 and GTM roles."],
                    ["Days 21-30", "Add the new agency, then remove the old one last."],
                ],
                "alt": "Thirty-day timeline for how to switch marketing agencies in Houston without losing accounts or data",
                "caption": "Order matters most at the end: billing yours first, old agency removed last.",
            },
            "audit": {
                "type": "checklist",
                "title": "Ownership check you can do today",
                "sub": "Log in yourself. Don’t ask the agency.",
                "items": [
                    "Admin on Google Ads with your own email",
                    "Your card on the Google Ads payments profile",
                    "Domain visible in your registrar account",
                    "Administrator user on the website CMS",
                    "Administrator on the GA4 property",
                    "Primary owner of your Business Profile",
                    "Your Meta portfolio owns Page and ad account",
                    "Tracking numbers billed to you",
                ],
                "alt": "Checklist to confirm who owns your Google Ads account, domain and Business Profile before changing agencies",
                "caption": "If any line is a no, add it to your list for this month.",
            },
        },
    },
]
