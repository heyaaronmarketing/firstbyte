"""Refresh batch (module c): three existing posts rewritten in depth for Houston and The Woodlands owners.

1. call-tracking-which-ads-make-phone-ring (setup + cost guide). Research: CallRail's pricing page (Nov 2026: four plans
   from $50 to $195 a month, 5 local numbers and 250 minutes included, $3 per extra local number, 5-6 cents a minute);
   Google Ads help "About phone call conversion tracking" (calls from ads, calls to a website number, clicks on a
   number, imported calls; forwarding numbers required for three of them); Google Ads help on the move from call ads
   to call assets (no new call ads from February 2026, existing ones stop serving February 2027); Google Business
   Profile help "Manage your contact info" (primary number plus up to 2 more); Whitespark (Darren Shaw) on tracking
   numbers in the primary field; Texas State Law Library and the RCFP Reporter's Recording Guide on one-party consent
   (Texas Penal Code 16.02); ABC13 on the 621 overlay (Jan. 23, 2025); PPC Land on LSA missed-call charges from
   Oct. 1, 2026.
2. local-services-ads-vs-google-ads-home-services (decision guide). Research: Google Ads help on the LSA transition to
   Performance Max pay-per-lead (Aug 2026 first phase, late 2026 broader, 2027 rest; weekly budget / 7; monthly cap
   daily x 30.4; manual bidding removed; one campaign-level Target CPA; Leads page under Goals; Search and Maps only;
   BBB callouts gone); Search Engine Journal (July 20, 2026); PPC Land (Sept 25, 2026) on missed-call billing; Google's
   LSA ad ranking page (bid, likelihood of a lead, profile quality); Google's "How leads work" page; Google Verified
   badge page; LocaliQ 2025 home services search benchmarks (medians, April 2024 to March 2025); TDLR A/C and
   electrical contractor pages; TSBPE; Jobber on Texas roofing licenses; Google's call ads sunset page.
3. fake-reviews-rule-local-businesses (rules guide). Research: FTC Consumer Reviews and Testimonials Rule Q&A
   (effective Oct. 21, 2024; sections 465.2-465.8; gating, incentives, insiders, suppression, knowledge standard);
   FTC's August 2024 announcement; FTC Federal Register notice (Sept. 2026) that 2026 penalty amounts were not
   adjusted, so the 2025 figure ($53,088, per Benesch's April 2026 alert quoting the warning letters) stands; FTC's
   December 2025 warning letters; FTC v. TruHeight (April 13, 2026); DOJ complaint against Premium Home Service
   (May 11, 2026, 15,000+ fake Business Profiles); Texas AG suit against Solvera in Harris County (DTPA, 2017);
   Google Maps prohibited content policy (incentives, conflicts of interest, selective solicitation, staff quotas,
   on-premises pressure); PPC Land on the April 2026 staff language; Google's April 2026 Maps safety post (2025
   figures); Business Profile restrictions page; Search Engine Land on Google's review extortion report form;
   BrightLocal Local Consumer Review Survey 2026 and its review platform guidelines page.
Not used (could not verify): a published Google default for minimum call length, any source-backed Houston LSA cost
per lead, whether pay-per-lead campaigns and Search campaigns share an auction, and any FTC penalty actually
assessed against a local service business under the rule.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

SRC = {
    # call tracking
    "callrail": A("https://www.callrail.com/pricing", "CallRail’s pricing page"),
    "gcalls": A("https://support.google.com/google-ads/answer/6100664?hl=en", "Google’s phone call conversion tracking page"),
    "callads": A("https://support.google.com/google-ads/answer/16598240?hl=en", "Google’s notice on retiring call ads"),
    "gbpphone": A("https://support.google.com/business/answer/16750496?hl=en", "Google’s Business Profile contact info page"),
    "whitespark": A("https://whitespark.ca/blog/call-tracking-numbers-google-business/", "Darren Shaw at Whitespark"),
    "sll": A("https://www.sll.texas.gov/faqs/tape-phone-conversation", "Texas State Law Library"),
    "rcfp": A("https://www.rcfp.org/reporters-recording-guide/texas/", "the Reporters Committee’s Texas recording guide"),
    "abc621": A("https://abc13.com/post/new-area-code-621-will-join-greater-houston-metro-starting-jan-23-2025/15625208/", "ABC13"),
    "missed": A("https://ppc.land/google-lsa-advertisers-face-missed-call-charges-from-october-1/", "PPC Land"),
    # LSA vs Google Ads
    "move": A("https://support.google.com/google-ads/answer/17213585", "Google’s transition guide"),
    "sej": A("https://www.searchenginejournal.com/google-is-bringing-local-service-ads-into-google-ads/582816/", "Search Engine Journal"),
    "rank": A("https://support.google.com/localservices/answer/7527305?hl=en", "Google’s LSA ad ranking page"),
    "leads": A("https://support.google.com/google-ads/answer/7195435?hl=en", "Google’s “How leads work” page"),
    "gv": A("https://support.google.com/localservices/answer/16498018?hl=en", "Google’s Verified badge page"),
    "localiq": A("https://localiq.com/blog/home-services-search-advertising-benchmarks/", "LocaliQ’s 2025 home services search benchmarks"),
    "tdlracr": A("https://www.tdlr.texas.gov/acr/contractor-apply.htm", "A/C and refrigeration contractors"),
    "tdlrelec": A("https://www.tdlr.texas.gov/electricians/apply/businesses/contractor-elec.htm", "electrical contractors"),
    "tsbpe": A("https://tsbpe.texas.gov/", "Texas State Board of Plumbing Examiners"),
    "roof": A("https://getjobber.com/academy/roofing-license/texas/", "no statewide roofing license"),
    # fake reviews
    "ftcqa": A("https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers", "FTC’s Q&A on the rule"),
    "ftcrule": A("https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials", "FTC’s August 2024 announcement"),
    "fr26": A("https://public-inspection.federalregister.gov/2026-18853.pdf", "a September 2026 Federal Register notice"),
    "benesch": A("https://www.beneschlaw.com/insight/five-stars-zero-tolerance-ftc-turns-up-enforcement-under-consumer-review-rule/", "Benesch’s summary of the letters"),
    "ftcwarn": A("https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-warns-10-companies-about-possible-violations-agencys-new-consumer-review-rule", "warning letters to 10 companies"),
    "truheight": A("https://ftc.gov/news-events/news/press-releases/2026/04/ftc-takes-action-against-truheight-deceptive-unsubstantiated-advertising-supposed-height-enhancing", "the FTC’s TruHeight case"),
    "phs": A("https://www.justice.gov/opa/pr/department-justice-files-complaint-against-best-gdr-llc-doing-business-premium-home-service", "a Justice Department complaint"),
    "solvera": A("https://www.texasattorneygeneral.gov/news/releases/ag-paxton-files-suit-against-reputation-management-company", "sued a reputation management company"),
    "gpolicy": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s Maps content policy"),
    "staff": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
    "gblog": A("https://blog.google/products-and-platforms/products/maps/new-ways-were-protecting-businesses-on-maps/", "Google’s April 2026 Maps safety update"),
    "restrict": A("https://support.google.com/business/answer/14114287?hl=en", "Business Profile restrictions page"),
    "extort": A("https://searchengineland.com/with-negative-review-extortion-scams-on-the-rise-use-googles-report-form-464515", "Search Engine Land"),
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "blplat": A("https://brightlocal.com/learn/review-platform-guidelines/", "BrightLocal’s platform-by-platform summary"),
}

CALLS = "/blog/call-tracking-which-ads-make-phone-ring/"
LSA = "/blog/local-services-ads-vs-google-ads-home-services/"
FAKE = "/blog/fake-reviews-rule-local-businesses/"

POSTS = [
    # ------------------------------------------------------------------ post 1: call tracking
    {
        "slug": "call-tracking-which-ads-make-phone-ring",
        "date": "2026-09-11",
        "modified": "2026-11-27",
        "title": "Call Tracking for Houston Businesses: Know Which Ads Make the Phone Ring",
        "seo_title": "Call Tracking in Houston: Which Ads Make the Phone Ring",
        "desc": "Call tracking for Houston and The Woodlands businesses: what it costs, which numbers you need, Google Business Profile setup, Google Ads calls and Texas law.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google Business Profile", "Google Analytics"],
        "art": "b2",
        "hero": "phone",
        "hero_alt": "Illustration of a ringing phone for a guide to call tracking for Houston and The Woodlands businesses",
        "related": ["track-form-submissions-phone-calls-ga4-google-ads", "speed-to-lead-response-time-follow-up-crm", "google-ads-not-converting-clicks-no-calls"],
        "sections": [
            (None, f"""<p>Try this before reading further. Open your call log for last week, pick out the calls from new customers, and write next to each one where that person found you. Google Ads, your Google Business Profile, the truck wrap, the mailer, a neighbor on Nextdoor.</p>
<p>Most owners we sit down with in Houston and The Woodlands get through three or four before they start guessing. The phone is their best lead source and the one they know least about.</p>
<p><b>The short answer:</b> call tracking gives each marketing source its own phone number (or swaps the number on your website for each visitor), forwards every call to your real line, and records which source produced it. A small business setup typically runs $50 to $250 a month with a provider like CallRail, and Google’s forwarding numbers for ad calls cost nothing extra.</p>
<p>That’s the whole idea. The rest of this guide is the setup we’d actually run for a service company, clinic or shop in Greater Houston: what it costs, which numbers to buy, how to keep it from hurting your map rankings, how to feed calls back into Google Ads, and what Texas law says about recording.</p>"""),

            ("How much does call tracking cost for a small business?", f"""<p>Less than one bad lead, usually. Per {SRC['callrail']} as of November 2026, CallRail sells four plans at $50, $95, $150 and $195 a month. Each includes five local numbers and 250 minutes. Extra local numbers are $3 each, and extra minutes run 5 to 6 cents (the page lists both rates in different spots, so confirm on your quote). Competitors like CallTrackingMetrics and WhatConverts price in the same neighborhood.</p>
<p>Minutes are where the bill grows. A plumbing company answering 600 calls a month at four minutes each burns 2,400 minutes, which is about 2,150 over the included amount.</p>
<!--fig:cost-->
<p>Two pieces cost nothing beyond your ad spend. Google Ads gives you Google forwarding numbers for calls from ads and for calls to your website number after an ad click. And Local Services Ads already assign a tracked number to every lead. You still want a call tracking provider for everything Google doesn’t see: organic visitors, your Business Profile, Facebook, Nextdoor, the billboard on I-45 and the yard signs in Spring.</p>
<p>Is it worth $100 to $200 a month? If you spend more than about $1,500 a month on marketing, yes, without much debate. Below that, start with one static number on your Business Profile and Google’s free ad tracking, then add the rest when spend grows.</p>"""),

            ("How does call tracking work?", f"""<p>There are two kinds of tracking numbers, and most businesses need both.</p>
<p><b>Static numbers</b> are one number per source that never changes. One on the truck wrap, one on the EDDM mailer, one on the Business Profile. Anyone who dials it came from that source (or saved it from that source, which is close enough).</p>
<p><b>Dynamic number insertion</b> (DNI) handles your website. A small script reads how each visitor arrived, using the referrer, UTM tags or Google’s click ID, and swaps the phone number on the page for one from a pool assigned to that source. When the visitor calls, the provider knows the source, the landing page and often the keyword.</p>
<!--fig:how-->
<p>Pool size matters. If two visitors share one number at the same time, the provider can’t tell them apart. Providers size the pool from your traffic, and for most local service sites that means somewhere between four and ten numbers. Set it too small and you’ll see a pile of calls labeled “unknown.”</p>
<p>The caller never notices any of this. The call rings through to your normal line (you can add a short whisper message only your staff hear, like “Google Ads call”), and it lands in your call log with the source attached.</p>"""),

            ("Which tracking numbers does a Houston business actually need?", f"""<p>Buy numbers that look local. Houston’s overlay now has five area codes, 713, 281, 832, 346 and, since January 23, 2025, 621, per {SRC['abc621']}. Conroe, Willis and Montgomery are mostly 936 territory. A 936 number on a Conroe roofer’s mailer reads as a neighbor. A toll-free number reads as a call center in another state, and in our experience answer rates on outbound callbacks drop with it too.</p>
<!--fig:map-->
<p>Here’s the number plan we’d set for a typical home service company or clinic north of Houston:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Source</th><th>Number type</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Website visitors (all sources)</td><td>DNI pool, 4 to 10 numbers</td><td>One pool covers organic, paid, social and email visitors, split by source in reports</td></tr>
<tr><td>Google Business Profile</td><td>1 static number</td><td>Primary number on the profile; your main line goes in “additional”</td></tr>
<tr><td>Google Ads call assets</td><td>Google forwarding number</td><td>Free; counts as a conversion when the call meets your minimum length</td></tr>
<tr><td>Local Services Ads</td><td>Google-assigned</td><td>Already tracked; turn call recording on in settings</td></tr>
<tr><td>Facebook and Instagram ads</td><td>DNI via UTM tags, or 1 static number for call-button ads</td><td>Tag every ad link with utm_source and utm_campaign</td></tr>
<tr><td>Truck wraps and yard signs</td><td>1 static number each, easy to remember</td><td>Wraps outlive campaigns; never let this number lapse</td></tr>
<tr><td>Mailers, billboards, radio</td><td>1 static number per piece or flight</td><td>A mailer to Kingwood and one to Katy should get different numbers</td></tr>
<tr><td>Yelp, Nextdoor, Angi paid listings</td><td>1 static number each</td><td>Free citations keep your main number for consistency</td></tr>
</tbody></table></div>
<p>That’s usually 8 to 15 numbers, which fits the cost estimate above. The truck wrap row is the one people regret. A wrap stays on the road for five years. If you cancel the provider and the number goes away, every truck on the Grand Parkway is advertising a dead line. Port the wrap number to your carrier before you ever switch providers.</p>"""),

            ("Will call tracking hurt my Google Business Profile ranking?", f"""<p>Not if you set it up the way local SEO people have for years. Google lets you list a primary number and up to two more, per {SRC['gbpphone']}. Put the tracking number in the primary field and your real main number in the first additional slot. {SRC['whitespark']} has recommended that setup since 2018 and reports no ranking harm in the accounts he’s watched. That’s anecdotal, but it matches what we see.</p>
<!--fig:gbp-->
<p>The additional slot is what keeps your name, address and phone consistent with your citations on Yelp, the BBB, the Greater Conroe or Woodlands chamber directory and the rest. Google can still connect those listings to your profile. Don’t spray a different tracking number across every free directory. That’s how citation messes start.</p>
<p>Two more Business Profile details. Add UTM tags to your profile’s website link (something like utm_source=google, utm_medium=organic, utm_campaign=gbp) so profile visitors who call from your site get credited to the profile, not lumped into “organic.” And don’t judge the profile by its own “Calls” number in the Performance report. That counts taps on the call button. The tracking number counts calls that connected, how long they lasted, and what was said.</p>
<p>If you’re working on map rankings at the same time, our {L('/blog/rank-in-google-map-pack-houston/', 'guide to the Houston map pack')} covers the rest.</p>"""),

            ("How do I track phone calls from Google Ads?", f"""<p>Google offers four kinds of call conversions, per {SRC['gcalls']}:</p>
<ul>
<li><b>Calls from ads.</b> Calls made directly from a call asset on your ad. Needs call reporting turned on.</li>
<li><b>Calls to a phone number on your website.</b> Google swaps in a forwarding number after an ad click, much like DNI.</li>
<li><b>Clicks on a mobile website number.</b> Only the tap, not the call. Useful as a backup signal, weak as a primary goal.</li>
<li><b>Imported calls.</b> Calls logged in another system (your call tracking provider or CRM) sent back to Google Ads, ideally only the ones that became booked jobs or sales, with values.</li>
</ul>
<p>Two of these matter more than the others. Calls from ads and website calls give Google fast feedback. Imported calls tell it which callers actually paid you. If Smart Bidding only sees “a call happened,” it will happily find you more 45-second calls from people asking if you sell parts.</p>
<p>Set the minimum call length to fit your business. We usually start at 60 to 90 seconds for home services and adjust after listening to a week of recordings. A dental office scheduling a new patient might need two minutes; a locksmith’s real calls can be short.</p>
<p>One change to plan for: call-only ads are going away. Google removed the option to create new call ads in February 2026, and existing ones stop serving in February 2027, per {SRC['callads']}. If you still run them, rebuild them now as responsive search ads with call assets, before February forces it.</p>
<p>For forms, tap-to-call tags and GA4 key events, see {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'how to track forms and calls in GA4 and Google Ads')}.</p>"""),

            ("What counts as a qualified call?", f"""<p>Call length alone is a blunt filter. A 3-minute call can be a vendor pitching SEO. A 50-second call can be a homeowner in Tomball who just wants you there Thursday.</p>
<p>A better definition combines a few signals. First-time caller (not an existing customer calling about an invoice). Long enough to be a real conversation. And either a tag from staff or an automated score that says it was about a service you sell. Most providers now offer AI call summaries and keyword spotting, so “asked about AC replacement” or “booked appointment” can be tagged without anyone listening to every call.</p>
<!--fig:funnel-->
<p>The junk is predictable, and it’s worth knowing your mix. Vendors and robocalls. Existing customers. Wrong numbers. Job seekers, especially the week after you post on Indeed. Callers from outside your service area, a common one for Houston companies whose ads drift into Beaumont or Bryan. If a source sends mostly junk, that’s a finding, and often a cheaper one to fix than you’d think.</p>"""),

            ("Is it legal to record customer calls in Texas?", f"""<p>Texas is a one-party consent state. Per the {SRC['sll']}, a recording generally needs the consent of just one participant, and the statute is Section 16.02 of the Texas Penal Code. Your business is a party to the call, so recording your own customer calls is generally allowed here.</p>
<p>The catch is the caller. Some states require every party to consent, and people from California, Illinois or Florida call Houston businesses all the time. {SRC['rcfp']} is a good place to read how those rules can collide. The simple, cheap fix is a short greeting before the call connects: “This call may be recorded for quality.” Every major provider supports it.</p>
<p>A few practical rules we follow. Limit who can play recordings. Set retention to what you need (90 days to a year covers most coaching and dispute needs). Medical, dental and therapy offices should treat recordings as patient information and loop in whoever handles compliance before turning recording on. This is general information, not legal advice.</p>"""),

            ("What call reports show that nothing else will", f"""<p>The first month of call data usually changes one decision right away, and it’s rarely the one the owner expected.</p>
<p>Often it’s missed calls. A tracking report sorted by hour shows exactly when the phone rings and nobody picks up: lunch, the 4:30 to 6 p.m. stretch when techs are calling in, and Saturdays.</p>
<!--fig:missed-->
<p>Missed calls now cost money directly on Local Services Ads. Since October 1, 2026, a missed call during your business hours where the caller stays on the line more than 20 seconds can be charged as a valid lead, per {SRC['missed']}. Paying for leads you didn’t answer is a bad trade. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers overflow answering, missed-call text-back and callback rules.</p>
<p>The other reports worth a monthly look: first-time callers by source (the real “leads by channel” chart), keywords and landing pages that produce calls versus forms, and average call length by source. A billboard that produces 30 calls averaging 40 seconds is telling you something different from a Business Profile producing 30 calls averaging four minutes.</p>"""),

            ("Call tracking mistakes we see in Houston accounts", f"""<ul>
<li><b>Counting every call as a lead.</b> Existing customers and vendors inflate results and teach Google the wrong lesson.</li>
<li><b>Tracking numbers on free citations.</b> A different number on every directory breaks your name-address-phone consistency.</li>
<li><b>A DNI pool that’s too small.</b> Lots of “unknown source” calls usually means this.</li>
<li><b>Forgetting offline media.</b> The mailer to Sugar Land and the radio flight share one number, so neither can be judged.</li>
<li><b>Letting numbers lapse.</b> Old wraps, signs and magazine ads keep ringing for years.</li>
<li><b>Never listening.</b> Fifteen minutes of recordings a week is the cheapest sales training you’ll find.</li>
<li><b>Two systems, two answers.</b> Google Ads, the provider and the CRM all count calls differently. Pick one as the source of truth for booked jobs and import from it.</li>
</ul>"""),

            ("A 30-day call tracking setup plan", f"""<p>This is roughly how we roll it out for a new client. Nothing here needs a developer if your site runs on WordPress, Webflow or Squarespace.</p>
<!--fig:plan-->
<p><b>Week 1:</b> pick a provider, buy local numbers (DNI pool plus one per offline source), and set forwarding and the recording greeting.</p>
<p><b>Week 2:</b> install the DNI script, update the Business Profile (tracking primary, main number additional, UTM on the website link), and swap numbers on wraps, signs and print going forward.</p>
<p><b>Week 3:</b> connect the provider to Google Ads and GA4, set call conversion actions and minimum lengths, and make one of them primary.</p>
<p><b>Week 4:</b> define a qualified call, set up tags or scoring, and start importing booked jobs back into Google Ads.</p>
<p>After that it’s a 30-minute monthly review alongside your form leads. If you’d like a senior strategist to build the tracking and the reporting around your goals, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Does call tracking work with Google Local Services Ads?",
             "Local Services Ads assign their own tracked number to every lead, so you don’t need a provider number inside LSA. Turn on call recording in your LSA or Google Ads settings and review leads there. Your provider still tracks everything else, and you can forward LSA calls through the same line so your staff see one call log. Just don’t replace Google’s number, or LSA can’t count or charge leads correctly."),
            ("Can I use call tracking numbers on Yelp and other directories in Houston?",
             "Use tracking numbers on paid listings, like Yelp ads or a paid Angi profile, where you need to judge the spend. Keep your main business number on free citations so your name, address and phone stay consistent across the web. If a directory lets you add a second number, you can add the tracking number there, but the main number should be the one that matches your Google Business Profile’s additional number."),
            ("How many tracking numbers do I need for dynamic number insertion?",
             "Enough that two visitors from the same source rarely see the same number at the same time. For most local service websites in Houston and The Woodlands, that’s four to ten numbers in the pool, depending on traffic. Your provider will suggest a size. If your reports show many calls with an unknown source, the pool is probably too small. Add a few numbers and check again after two weeks."),
            ("Will customers notice I’m using a call tracking number?",
             "No. A local tracking number looks like any other local number, and the call rings straight through to your line. Buying numbers in the area codes your customers use, such as 281, 832 or 713 in Houston and 936 around Conroe, keeps it that way. The only thing callers might hear is a short recording disclosure, which most people expect from a business anyway."),
            ("Is CallRail worth it for a small business in The Woodlands?",
             "For a business spending more than about $1,500 a month on marketing, almost always. Its plans start at $50 a month with five local numbers and 250 minutes, which covers a small clinic or a service company getting started. The value is knowing which ads produce booked jobs, so you can cut the ones that don’t. Competitors such as CallTrackingMetrics and WhatConverts do the same job at similar prices."),
        ],
        "figures": {
            "cost": {
                "type": "bars",
                "title": "What call tracking costs per month",
                "sub": "Three business sizes priced at CallRail’s published November 2026 rates",
                "items": [["Small clinic: 150 calls, 5 numbers", 60, "$60"], ["Home services: 600 calls, 8 numbers", 212, "$212"], ["Multi-location: 2,000 calls, 20 numbers", 583, "$583"]],
                "highlight": [1],
                "note": "Illustrative example. Assumes 3 to 4 minutes per call, 5 cents per extra minute and $3 per extra number. Taxes and add-ons not included.",
                "alt": "Bar chart of estimated monthly call tracking costs for small businesses in Houston and The Woodlands, from $60 to $583",
                "caption": f"Rates from {SRC['callrail']}. Minutes, not numbers, drive most of the bill.",
            },
            "how": {
                "type": "steps",
                "title": "How dynamic number insertion credits a call",
                "sub": "What happens between a Google search and a ringing phone",
                "steps": [["Visitor arrives", "From an ad, the map pack, Facebook or an email, carrying a click ID or UTM tags."], ["Script swaps the number", "Your site shows a number from the pool assigned to that source."], ["Customer calls", "The call forwards to your normal line, with an optional whisper to staff."], ["Provider logs it", "Source, landing page, keyword, duration and recording are saved."], ["Results flow back", "Qualified calls go to Google Ads and GA4 as conversions."]],
                "alt": "Five steps showing how call tracking with dynamic number insertion works for a Houston or The Woodlands business website",
                "caption": "Static numbers cover offline sources. DNI covers everything that reaches your website.",
            },
            "map": {
                "type": "map",
                "title": "Buy tracking numbers that look local",
                "sub": "Houston overlay codes (713, 281, 832, 346, 621) to the south; 936 around Conroe, Willis and Montgomery",
                "highlight": ["Conroe", "Willis", "Montgomery", "The Woodlands", "Spring", "Katy", "Houston"],
                "alt": "Map of Greater Houston and The Woodlands showing where 936 and Houston overlay area codes fit for call tracking numbers",
                "caption": f"The 621 code joined Houston’s overlay in January 2025, per {SRC['abc621']}.",
            },
            "gbp": {
                "type": "compare",
                "title": "Tracking numbers on your Business Profile",
                "left": {"title": "Causes problems", "items": ["Main number replaced, nowhere else listed", "New tracking number on every directory", "Toll-free number as primary", "No UTM tag on the website link", "Number changed every few months"]},
                "right": {"title": "Safe setup", "items": ["Tracking number as primary", "Main number in first additional slot", "Local area code (281, 832, 936)", "UTM-tagged website link", "Same number kept for years"]},
                "alt": "Comparison of risky and safe ways to add a call tracking number to a Google Business Profile in Houston and The Woodlands",
                "caption": f"Google allows a primary number plus two more, per {SRC['gbpphone']}.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From rings to revenue",
                "stages": [["Calls to tracking numbers", "400"], ["Answered", "310"], ["New-customer conversations", "190"], ["Qualified for a service you sell", "120"], ["Booked", "70"]],
                "note": "Illustrative example of one month for a Houston home service company.",
                "alt": "Funnel showing how total calls narrow to booked jobs in call tracking for a Houston and The Woodlands business",
                "caption": "Bid and budget on the bottom two rows. The top row flatters every channel.",
            },
            "missed": {
                "type": "columns",
                "title": "Where missed calls hide",
                "sub": "Share of calls going unanswered by time of day",
                "labels": ["7-9a", "9-11a", "11a-1p", "1-3p", "3-5p", "5-7p", "Sat"],
                "values": [12, 8, 24, 10, 18, 41, 33],
                "highlight": [2, 5, 6],
                "y_label": "% missed",
                "note": "Illustrative example. Pull your own from your call tracking report sorted by hour.",
                "alt": "Column chart of missed call rates by time of day for a Houston and The Woodlands service business using call tracking",
                "caption": "Lunch, early evening and Saturday are the usual leaks.",
            },
            "plan": {
                "type": "checklist",
                "title": "Call tracking setup checklist",
                "sub": "Everything a Houston or The Woodlands business needs in the first 30 days",
                "items": ["Provider picked, local numbers bought", "Recording greeting and whisper set", "DNI script installed and tested", "Business Profile: tracking primary, main additional", "UTM tags on profile and ad links", "Separate numbers for wraps, mailers, radio", "Google Ads call conversions and minimum length set", "Qualified-call definition written down", "Booked jobs imported back into Google Ads"],
                "alt": "Checklist for setting up call tracking for a business in Houston and The Woodlands in 30 days",
                "caption": "The last two items are the ones that change your ad results.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: LSA vs Google Ads
    {
        "slug": "local-services-ads-vs-google-ads-home-services",
        "date": "2026-09-08",
        "modified": "2026-11-27",
        "title": "Local Services Ads vs. Google Ads for Houston Home Services: Which Pays Off in 2026",
        "seo_title": "Local Services Ads vs. Google Ads: Houston Home Services",
        "desc": "Local Services Ads vs. Google Ads for Houston and The Woodlands home services: costs, 2026 changes, ranking, who qualifies and how to split a budget.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google Business Profile", "Google"],
        "art": "b4",
        "hero": "scale",
        "hero_alt": "Illustration of a balance scale comparing Local Services Ads and Google Ads for Houston and The Woodlands home services",
        "related": ["local-services-ads-lead-disputes-credits", "google-guaranteed-vs-google-verified", "hvac-marketing-houston-the-woodlands"],
        "sections": [
            (None, f"""<p>Verdict first. If you’re a licensed HVAC, plumbing, electrical or similar company in Houston with a decent pile of reviews and someone who reliably answers the phone, start with Local Services Ads. Add regular Google Ads search campaigns for the high-ticket jobs LSA can’t single out. Most companies that stick with one or the other end up running both.</p>
<p><b>The direct answer:</b> Local Services Ads charge per lead, sit at the top of Google for eligible home services, and rank on reviews, responsiveness and verification, with almost no control over keywords or copy. Google Ads search campaigns charge per click and give you full control over keywords, ads and landing pages. LSA is usually cheaper per lead; Search is better for choosing which jobs you get.</p>
<p>That comparison changed a lot in 2026. LSA moved inside Google Ads, the dispute button is gone, missed calls can now be charged, and call-only ads are on their way out. Below is what’s different now, what each one really costs in Houston, and how we’d split a budget between them for a company in The Woodlands, Spring, Cypress or Katy.</p>"""),

            ("What changed for Local Services Ads in 2026", f"""<p>If you set up LSA a few years ago and haven’t looked closely since, a lot moved.</p>
<p><b>LSA now lives in Google Ads.</b> Starting in August 2026, Local Services campaigns began migrating into Google Ads as Performance Max campaigns with pay-per-lead goals. The first phase covered select U.S. home and storefront services such as plumbing, HVAC and roofing; a broader rollout follows in late 2026 and the rest in 2027, per {SRC['move']}. You still pay per lead, and the ads still show only on Search and Maps, keywordless, based on your service categories and areas.</p>
<p><b>Bidding got simpler, and blunter.</b> Weekly budgets become daily averages (weekly divided by seven), monthly spend is capped at the daily average times 30.4, manual bidding is gone, and per-category targets are replaced by one campaign-level Target CPA. {SRC['sej']} flagged the obvious problem: a company selling $90 drain cleanings and $12,000 AC systems now shares one cost target unless it splits campaigns.</p>
<!--fig:changes-->
<p><b>Disputes are over.</b> Manual lead disputes aren’t supported in the new setup. Google credits some invalid leads automatically, and leads for job types or areas you don’t serve aren’t credited at all. We covered how that works in {L('/blog/local-services-ads-lead-disputes-credits/', 'our LSA lead credits guide')}.</p>
<p><b>Missed calls cost money.</b> Since October 1, 2026, an unanswered call during business hours where the caller stays on more than 20 seconds can be charged, per {SRC['missed']}.</p>
<p><b>One badge.</b> Google Guaranteed, Google Screened and license verification were folded into a single Google Verified badge in October 2025, per {SRC['gv']}. Details in {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs. Google Verified')}.</p>
<!--fig:timeline-->
<p>And on the regular Google Ads side, call-only ads can’t be created anymore and stop serving in February 2027. Calls now come from call assets on responsive search ads.</p>"""),

            ("Local Services Ads vs. Google Ads, side by side", f"""<div class="bp-tbl"><table>
<thead><tr><th></th><th>Local Services Ads</th><th>Google Ads search campaigns</th></tr></thead>
<tbody>
<tr><td>You pay for</td><td>A valid lead: answered call, qualifying missed call, message or booking</td><td>A click, whether or not they call</td></tr>
<tr><td>Where it shows</td><td>Top of Search for eligible categories, plus Maps</td><td>Above and below organic results; can include Maps and partners</td></tr>
<tr><td>Targeting</td><td>Service categories, job types and service area; no keywords</td><td>Your keywords, match types, negatives, locations, schedule, devices</td></tr>
<tr><td>Ad copy</td><td>Generated from your profile: name, rating, years, badge, hours</td><td>You write headlines and descriptions, with call, sitelink and callout assets</td></tr>
<tr><td>Landing page</td><td>None; the lead goes straight to your phone or inbox</td><td>Your page, which you can test and improve</td></tr>
<tr><td>Ranking</td><td>Bid, likelihood of a lead, profile quality (reviews, response time, verification)</td><td>Bid, ad quality, landing page experience, expected click-through</td></tr>
<tr><td>Setup time</td><td>Background, license and insurance checks; can take weeks</td><td>Live in a day</td></tr>
<tr><td>Best for</td><td>“Plumber near me,” emergencies, trust-driven calls</td><td>Specific high-value jobs, new services, seasonal pushes</td></tr>
</tbody></table></div>
<p>The tradeoff fits in a sentence. LSA trades control for trust and a lower cost per lead. Search trades a higher cost per lead for the ability to pick exactly which jobs you pay to hear about.</p>"""),

            ("How much do Local Services Ads cost compared with Google Ads in Houston?", f"""<p>Start with the side that has public numbers. {SRC['localiq']}, based on campaigns from April 2024 through March 2025, put median search ad costs per lead at $127.74 for AC installation and repair, $129.02 for plumbing, $93.69 for electricians and $228.15 for roofing. Median clicks ran about $9.70 to $12.20. Those are national medians; competitive Houston suburbs often run higher in July.</p>
<!--fig:cpl-->
<p>LSA cost per lead is harder to pin down because Google doesn’t publish it and it moves with trade, job type, area and season. It’s generally lower than search for the same trade, which is why LSA is the usual starting point. But a cheaper lead isn’t automatically a cheaper job. What matters is cost per booked job, and that depends on how many leads you actually close.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Same $3,000 month</th><th>Local Services Ads</th><th>Search campaign</th></tr></thead>
<tbody>
<tr><td>Cost per lead</td><td>$75</td><td>$125</td></tr>
<tr><td>Leads</td><td>40</td><td>24</td></tr>
<tr><td>Booking rate</td><td>50% (more tire-kickers, wrong job types)</td><td>60% (picked keywords, better-fit callers)</td></tr>
<tr><td>Booked jobs</td><td>20</td><td>14</td></tr>
<tr><td>Cost per booked job</td><td>$150</td><td>$214</td></tr>
<tr><td>Average ticket</td><td>$450 (repairs)</td><td>$1,900 (mix includes replacements)</td></tr>
</tbody></table></div>
<p><i>Illustrative example, not benchmarks.</i> Notice what happens on the last row. LSA wins on cost per job; Search wins on revenue because it was aimed at replacements. That’s the whole argument for running both, and for tracking every lead to a booked job so you can see which way your own numbers fall.</p>
<p>Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} go deeper on the search side.</p>"""),

            ("Which shows up first: Local Services Ads or Google Ads?", f"""<p>For eligible categories, the LSA unit usually sits at the very top of the results, above the text ads, then the map pack, then organic results. On a phone in Spring searching “water heater repair,” that LSA box can fill most of the screen.</p>
<p>That placement is why LSA leads feel “warmer.” The searcher sees your rating, review count, years in business and the Verified badge before they ever see an ad headline. It’s also why reviews matter so much more here than in Search.</p>
<p>The layout isn’t fixed. Google tests it constantly, and AI Overviews can push everything down on informational searches. Don’t build a plan that depends on any one position.</p>"""),

            ("How Local Services Ads decide who gets the lead", f"""<p>Per {SRC['rank']}, LSA ranks providers on three things: your bid, how likely your ad is to produce a lead, and your profile quality. “Likely to produce a lead” covers your responsiveness, how relevant your services and bio are to the search, and whether you turn on messages or booking. Profile quality covers your rating, number of reviews, response time, photos and completed verification.</p>
<!--fig:ranking-->
<p>A few Houston-specific notes. If you have locations in Katy and The Woodlands that both serve Cypress, only your highest-ranking ad shows for a given search, so overlapping service areas don’t buy you two spots. And your business hours come from your Business Profile, so if your profile says 7 to 7 but the office stops answering at 5, those last two hours are where missed-call charges and ranking damage pile up.</p>
<p>Reviews do the heavy lifting. A company with 300 reviews at 4.8 has a hard-to-beat edge over one with 40 at 4.9. If you need a review process that holds up, {L('/blog/complete-guide-google-reviews/', 'start with our Google reviews guide')}.</p>"""),

            ("Who can run Local Services Ads in Houston, and what Google checks", f"""<p>LSA is open to a list of home service categories, from HVAC, plumbing and electrical to roofing, pest control, cleaning, garage doors, locksmiths and more. To show, you pass Google’s screening, which can include a background check, insurance and a license check where the trade is licensed.</p>
<p>In Texas, that means TDLR licenses for {SRC['tdlracr']} and {SRC['tdlrelec']}, and a license from the {SRC['tsbpe']} for plumbing companies. Roofers have {SRC['roof']}, so verification leans on insurance and business checks instead. Make sure the name on your license matches your Google Business Profile exactly; mismatched DBAs are the most common reason we see verification stall.</p>
<p>After migration, your name, address and hours sync from your Business Profile and have to be edited there, per {SRC['move']}. Big name or address changes can trigger a fresh review that pauses the campaign for a day or two, so don’t rebrand the week before a heat wave.</p>"""),

            ("When Local Services Ads win, and when Search campaigns win", f"""<p>Here’s how we decide where the next dollar goes for a home service company in Greater Houston.</p>
<!--fig:fit-->
<p>LSA is the better first dollar for emergency and repair work, for companies with strong reviews and someone answering every call, and for owners who don’t have time to manage keywords. Search earns its place for high-ticket jobs (AC replacements, whole-home generators, repipes, tankless conversions), for services LSA lumps together, for new service areas where your reviews are thin, and for seasonal pushes like pre-summer AC tune-ups.</p>
<p>A search campaign that complements LSA looks like this: keywords such as “ac replacement the woodlands,” “generator installation kingwood,” “tankless water heater install spring tx” and “repipe house katy.” Negatives like jobs, salary, training, school, license, diy, how to, parts, home depot, lowes, used and free. A landing page per service with prices or price ranges, financing and real photos. That campaign isn’t fighting LSA for the “plumber near me” call. It’s going after the $9,000 job.</p>"""),

            ("Should I run both? How we split a Houston home services budget", f"""<p>Usually, yes. Our default for a company new to paid search is roughly 60% LSA and 40% Search for the first 60 days, then shift monthly toward whichever has the lower cost per booked job. There’s no magic in 60/40. It just gives both enough budget to produce data.</p>
<p>Houston’s calendar should shape the split. AC demand climbs from May through September. Freezes (think February 2021) make January and February spike for plumbers. Hurricane season runs June through November, and after a storm, roofing, tree and generator searches jump overnight. Our {L('/blog/hurricane-season-marketing-playbook-houston-the-woodlands/', 'hurricane season playbook')} covers that side.</p>
<!--fig:season-->
<p>Two rules for the busy months. Raise LSA budgets only if you can answer the extra calls, because missed calls during business hours can now be billed. And use Search to protect margin: in July, a dollar is better spent on “ac replacement” than on a fourth tune-up call you can’t schedule until August.</p>
<p>Keep service areas honest in both. Leads from outside your areas aren’t credited on LSA, and a Search campaign aimed at all of Harris County from a shop in Magnolia wastes money on drive time.</p>
<!--fig:area-->"""),

            ("Putting LSA and Search on one scoreboard", f"""<p>The two systems count differently. LSA counts leads. Search counts whatever conversions you set up. Your bank account counts booked jobs. Pick that last one as the scoreboard.</p>
<ul>
<li>Turn on call recording for LSA and listen to a sample weekly.</li>
<li>Use {L(CALLS, 'call tracking')} on your website and Business Profile so Search, organic and profile calls are separated.</li>
<li>Tag each lead in your CRM or field service software (ServiceTitan, Housecall Pro, Jobber) with its source.</li>
<li>Import booked jobs back into Google Ads so Search bidding learns from revenue, not rings.</li>
<li>Review cost per booked job by channel every month, not cost per lead.</li>
</ul>
<p>If the numbers say LSA is beating Search for everything, move the money. If Search is bringing in the replacements that pay the bills, protect it. Either way, decide from booked jobs.</p>"""),

            ("Mistakes we see in Houston LSA and Google Ads accounts", f"""<ul>
<li><b>Leaving every job type on in LSA.</b> Services you don’t do produce charged leads you can’t get credited.</li>
<li><b>One Target CPA for everything.</b> After migration, split high-ticket and low-ticket work into separate campaigns if the costs differ a lot.</li>
<li><b>Search campaigns on broad “near me” terms only.</b> That’s LSA’s turf. Aim Search at specific, valuable jobs.</li>
<li><b>Profile hours that don’t match reality.</b> Missed calls in those hours can be charged.</li>
<li><b>No negatives.</b> Houston search terms are full of job seekers and DIYers.</li>
<li><b>Judging by leads.</b> A $60 lead that never books costs more than a $140 lead that does.</li>
</ul>
<p>If you’d like a senior strategist to map out the LSA and Search mix for your trade, service area and season, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much do Local Services Ads cost per lead in Houston?",
             "Google doesn’t publish LSA lead prices, and they vary by trade, job type, area and season, so a Woodlands plumbing lead and a Katy roofing lead can be priced very differently. LSA leads are usually cheaper than search ad leads for the same trade. For comparison, LocaliQ’s 2025 search benchmarks put median search costs per lead around $94 to $228 for home services. Track cost per booked job to see your real number."),
            ("Can I run Local Services Ads and Google search ads at the same time?",
             "Yes, and most home service companies that get good results do. They’re separate products with separate placements and billing, even now that LSA lives in Google Ads. The trick is giving each a different job. Let LSA handle broad, trust-driven searches like “plumber near me,” and aim search campaigns at specific high-value jobs, such as AC replacement or repipes, with your own landing pages."),
            ("Why am I being charged for missed calls on Local Services Ads?",
             "Since October 1, 2026, Google can charge a missed call during your business hours as a valid lead if the caller stays on the line more than 20 seconds. Calls outside your hours aren’t covered. If you use a phone menu, the timer starts after the caller presses a key. The fix is coverage: overflow answering, accurate hours in your Business Profile and fast callbacks."),
            ("Are Local Services Ads worth it for roofers in Houston?",
             "Often, especially after storms, when roofing searches spike across Houston and Montgomery County. Texas has no statewide roofing license, so Google’s checks lean on insurance and business verification. The risk is lead quality, since storm season brings many insurance-claim tire-kickers and out-of-area calls. Keep your service area tight, record calls and judge LSA on inspections booked and roofs sold, not raw leads."),
            ("Do I need a Google Business Profile for Local Services Ads?",
             "In practice, yes. After the move into Google Ads, your LSA business name, address and hours sync from your Google Business Profile and are edited there. A complete, verified profile with accurate hours, real photos and a steady flow of reviews also helps your LSA ranking, because Google weighs rating, review count and responsiveness when it decides which providers to show."),
        ],
        "figures": {
            "changes": {
                "type": "stats",
                "title": "Local Services Ads in 2026, by the numbers",
                "stats": [["20 sec", "Missed call during business hours that can be charged"], ["÷ 7", "How weekly budgets convert to daily"], ["× 30.4", "Monthly cap on the daily average"], ["Feb ’27", "Call-only ads stop serving in Google Ads"]],
                "alt": "Key 2026 Local Services Ads and Google Ads changes for Houston and The Woodlands home service companies",
                "caption": f"From {SRC['move']}, {SRC['leads']} and Google’s call ads notice.",
            },
            "timeline": {
                "type": "steps",
                "title": "How we got here",
                "sub": "Local Services Ads changes that matter to Houston home service companies",
                "steps": [["July 2024", "Manual disputes replaced by automatic credits."], ["October 2025", "Three badges merged into one Google Verified badge."], ["February 2026", "No new call-only ads in Google Ads."], ["August 2026", "LSA starts moving into Google Ads as pay-per-lead Performance Max."], ["October 2026", "Qualifying missed calls during business hours can be charged."]],
                "alt": "Timeline of Local Services Ads changes from 2024 to 2026 for home service businesses in Houston and The Woodlands",
                "caption": "Non-U.S. accounts and remaining categories move in 2027.",
            },
            "cpl": {
                "type": "bars",
                "title": "Median search ad cost per lead by trade",
                "sub": "Google search campaigns, U.S., April 2024 to March 2025",
                "items": [["Roofing and gutters", 228.15, "$228"], ["Plumbing", 129.02, "$129"], ["AC install and repair", 127.74, "$128"], ["Electricians", 93.69, "$94"]],
                "highlight": [1, 2],
                "alt": "Bar chart of median Google search ad cost per lead for home services trades, a benchmark for Houston and The Woodlands",
                "caption": f"Source: {SRC['localiq']}. National medians; Houston summers often run higher.",
            },
            "ranking": {
                "type": "checklist",
                "title": "What moves your LSA ranking",
                "sub": "Factors Google lists, and how Houston companies fix them",
                "items": ["Answer calls and messages fast, all business hours", "Turn on messaging or booking", "Steady flow of new Google reviews", "Business Profile hours that match reality", "Bio and services that match what you sell", "Real job photos, not stock", "All verification checks complete", "Bid high enough to compete in your area"],
                "alt": "Checklist of Local Services Ads ranking factors for home service businesses in Houston and The Woodlands",
                "caption": f"Based on {SRC['rank']}.",
            },
            "fit": {
                "type": "compare",
                "title": "Where the next dollar goes",
                "left": {"title": "Search campaigns win", "items": ["AC replacements, generators, repipes", "New service areas with few reviews", "Services LSA lumps together", "Seasonal offers and tune-up pushes", "You need your own landing page"]},
                "right": {"title": "Local Services Ads win", "items": ["Emergency and repair calls", "Strong reviews and fast answering", "Little time to manage keywords", "Trust matters more than price", "You want to pay per lead, not click"]},
                "alt": "Comparison of when Local Services Ads or Google search campaigns work best for Houston and The Woodlands home services",
                "caption": "Most companies end up funding both columns.",
            },
            "season": {
                "type": "columns",
                "title": "AC repair demand through a Houston year",
                "sub": "Relative search interest by month",
                "labels": ["Jan", "Mar", "May", "Jun", "Jul", "Aug", "Sep", "Nov"],
                "values": [18, 30, 70, 90, 100, 96, 72, 25],
                "highlight": [3, 4, 5],
                "y_label": "Index",
                "note": "Illustrative example. Check Google Trends and your own call data for your trade.",
                "alt": "Column chart of seasonal AC repair search demand in Houston and The Woodlands for planning Local Services Ads budgets",
                "caption": "Shift budget toward the months you can staff, not just the months people search.",
            },
            "area": {
                "type": "map",
                "title": "Keep service areas inside a real drive",
                "sub": "An example service area for a company based in The Woodlands",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Magnolia", "Shenandoah", "Kingwood"],
                "note": "Illustrative example. Out-of-area leads aren’t credited on LSA.",
                "alt": "Map of an example Local Services Ads and Google Ads service area around The Woodlands, Spring, Conroe and Tomball near Houston",
                "caption": "If a tech can’t get there and back in a reasonable window, leave it out.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: FTC fake review rule
    {
        "slug": "fake-reviews-rule-local-businesses",
        "date": "2026-09-29",
        "modified": "2026-11-27",
        "title": "The FTC Fake Review Rule: What Houston and The Woodlands Businesses Can and Can’t Do",
        "seo_title": "The FTC Fake Review Rule for Houston Local Businesses",
        "desc": "The FTC fake review rule for Houston and The Woodlands businesses: what’s banned, penalties, incentives, review gating, staff reviews and Google’s own rules.",
        "category": "SEO & AI search",
        "icons": ["Google Business Profile", "Yelp", "Google"],
        "art": "b6",
        "hero": "stars",
        "hero_alt": "Illustration of review stars for a guide to the FTC fake review rule for Houston and The Woodlands businesses",
        "related": ["complete-guide-google-reviews", "why-are-my-google-reviews-disappearing", "ftc-rules-influencer-partnerships"],
        "sections": [
            (None, f"""<p>“Can I give people $10 off their next visit for leaving a Google review?”</p>
<p>It’s the review question we hear most from owners in Houston and The Woodlands, and the honest answer is annoying. Under federal law, maybe. Under Google’s rules, no. Under Yelp’s, you shouldn’t even be asking.</p>
<p><b>The short answer:</b> the FTC’s Consumer Reviews and Testimonials Rule, in effect since October 21, 2024, bans fake reviews, buying positive or negative reviews, undisclosed reviews from staff and owners, fake “independent” review sites, review suppression and fake followers. Knowing violations can cost up to $53,088 each. Asking every real customer for an honest review is still fine.</p>
<p>This guide goes through the rule section by section with local examples, then covers what the FTC has actually enforced, where Google’s and Yelp’s rules are stricter, and how to run a review program that holds up everywhere. It’s general information, not legal advice.</p>"""),

            ("What does the FTC fake review rule ban?", f"""<p>The rule (16 CFR Part 465) has six main prohibitions. The {SRC['ftcqa']} walks through each. Here they are in plain language, with the kind of example we’d actually worry about at a local business.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Section</th><th>What it bans</th><th>Local example that crosses the line</th></tr></thead>
<tbody>
<tr><td>465.2 Fake reviews</td><td>Writing, buying or selling reviews from people who don’t exist or didn’t use the business, or that misstate their experience</td><td>Paying a “review service” for 40 five-star reviews for a Conroe roofer</td></tr>
<tr><td>465.4 Buying sentiment</td><td>Incentives conditioned on a positive (or negative) review</td><td>A Katy restaurant offering free dessert “for a 5-star review”</td></tr>
<tr><td>465.5 Insider reviews</td><td>Reviews by owners, managers or employees, or their solicited relatives, without a clear disclosure</td><td>A Spring med spa’s front desk team reviewing the spa from personal accounts</td></tr>
<tr><td>465.6 Fake “independent” sites</td><td>Claiming a site you control offers independent reviews</td><td>A “Best Plumbers in The Woodlands” site secretly owned by one plumber</td></tr>
<tr><td>465.7 Review suppression</td><td>Unfounded legal threats, intimidation or false accusations to remove reviews; hiding negatives while implying you show them all</td><td>Threatening a customer with a defamation suit over a truthful 2-star review</td></tr>
<tr><td>465.8 Fake social influence</td><td>Buying or selling fake followers, views or engagement</td><td>Buying 10,000 Instagram followers for a new boutique on Market Street</td></tr>
</tbody></table></div>
<p>The {SRC['ftcrule']} called out AI-generated fake reviews by name. If a tool writes reviews from customers who never wrote them, that’s a fake review no matter how real the customer was.</p>
<p>Who can be liable is broader than owners expect. Per the FTC’s Q&A, review brokers, marketing agencies, PR firms and reputation management companies can be on the hook too. Ordinary customers can’t be liable for what they write.</p>"""),

            ("How big are the penalties for fake reviews?", f"""<p>The rule’s main teeth is civil penalties, which the FTC couldn’t usually seek for a first offense before. The current maximum is $53,088 per violation, the figure the FTC cited in its December 2025 warning letters, per {SRC['benesch']}. The FTC didn’t adjust penalty amounts for 2026 because the government shutdown delayed the inflation data, so 2025 levels still apply, per {SRC['fr26']}.</p>
<!--fig:numbers-->
<p>“Per violation” is the scary part. Forty bought reviews could be argued as forty violations.</p>
<p>Penalties apply to knowing violations. For buying reviews, the FTC uses a “knew or should have known” standard and lists red flags in its Q&A: reviews posted very fast after a purchase, a sudden burst, or reviews about the wrong product. There’s no private right of action under the rule, so a competitor can’t sue you under it, but they can report you to the FTC, to Google, and to the Texas Attorney General, who enforces the state’s Deceptive Trade Practices Act.</p>"""),

            ("Has the FTC actually enforced the rule?", f"""<p>Yes, and the cases are getting closer to Main Street.</p>
<!--fig:timeline-->
<p>In December 2025, the FTC sent {SRC['ftcwarn']} about possible violations, its first public use of the rule. Recipients had five days to confirm in writing what they’d fixed.</p>
<p>In April 2026, {SRC['truheight']} alleged a supplement company posted thousands of fake five-star reviews written by employees and gave away free or discounted product in exchange for five-star reviews. The proposed order required a $750,000 payment against a larger, partly suspended judgment, and bans buying reviews conditioned on any sentiment.</p>
<p>The one that should make home service owners sit up came in May 2026. On an FTC referral, {SRC['phs']} accused an Illinois company doing business as Premium Home Service of creating more than 15,000 fake Google Business Profiles for plumbing, heating and electrical work, using local-looking addresses and phone numbers that routed to overseas call centers, and posting fake reviews on them. It cites the reviews rule alongside the FTC Act. Those are allegations, not findings, but Houston contractors have been competing with exactly this kind of lead-gen listing for years.</p>
<p>Texas has its own history. The Texas Attorney General {SRC['solvera']} in Harris County district court in 2017, alleging it used lawsuits with fictitious parties to get online reviews taken down, under the Deceptive Trade Practices Act. Same idea as the federal rule’s suppression section, years earlier.</p>"""),

            ("Can I offer a discount or gift card for a review?", f"""<p>This is where federal law and the platforms split, and it’s the source of most confusion.</p>
<p><b>Under the FTC rule,</b> incentives aren’t banned unless they’re tied, openly or by implication, to a particular sentiment. “$10 off for any review, good or bad” can be legal federally. Generalized requests sent to all your customers are exempt from the insider rules even if an incentive is offered, per the FTC’s Q&A.</p>
<p><b>Under Google’s rules,</b> it’s flatly out. {SRC['gpolicy']} says merchants may not offer payment, discounts, or free goods or services in exchange for a review, an edit, or removing a negative one. Incentivized reviews get removed, and a pattern can get your profile restricted.</p>
<p><b>Under Yelp’s rules,</b> you shouldn’t ask for reviews at all, incentive or not, per {SRC['blplat']}. Facebook, Tripadvisor and Angi also prohibit incentives.</p>
<!--fig:incentives-->
<p>For a local business, Google is the platform that pays the bills, so Google’s rule is the one to follow. No discounts, no drawings, no “review us and get a free car wash.” If you want to thank customers, thank all of them the same way, whether they review or not.</p>"""),

            ("Is review gating illegal?", f"""<p>Review gating is when a survey asks “How did we do?” and only sends happy customers to Google while unhappy ones go to a private feedback form. Plenty of review software still offers it as a setting.</p>
<p>The FTC rule doesn’t name gating specifically, but the FTC says the practice could violate the FTC Act. Google is explicit: merchants may not “selectively solicit positive reviews from customers,” per its policy. So the answer for practical purposes is don’t.</p>
<p>The fix is easy. Send every customer the same review link. If you also want private feedback, put a second, separate line in the message (“Something not right? Reply here or call Dana at the office”). Both options go to everyone.</p>"""),

            ("Can my employees, friends or family review my business?", f"""<p>Under the FTC rule, insiders can post only with a clear and conspicuous disclosure of the relationship. Family members can review your business if they disclose they’re family. The FTC doesn’t expect you to vet every reviewer, but red flags should prompt a question.</p>
<p>Google is stricter. Its policy removes content based on a conflict of interest, including current or former employment or a contractual relationship. Practically, that means no staff reviews of your own business on Google, disclosure or not.</p>
<p>Google tightened the staff side in April 2026. The policy now bars merchants from asking staff to collect a set number of reviews, or reviews with specific content, “including content that identifies a staff member,” per {SRC['staff']}. That hits a habit we see all over Houston: techs and stylists told to get five reviews a week that mention them by name. It also says merchants shouldn’t pressure customers to review while on the premises, so the “can you do it right now while I’m standing here” move at checkout is out too.</p>
<p>Asking customers is fine. Setting staff quotas or scripting what customers say is the line.</p>"""),

            ("How do I handle negative reviews without breaking the rule?", f"""<p>Respond publicly, calmly and briefly. The FTC’s Q&A says businesses can respond to negative reviews, contact the customer to fix the problem, and ask satisfied customers to update a review. What they can’t do is use intimidation, unfounded legal threats or knowingly false accusations to get reviews removed. Paying someone to take down a truthful negative review may be unfair under the FTC Act.</p>
<p>Fake negative reviews are a separate problem. If someone floods your profile with one-star reviews and then demands payment to stop, Google has a dedicated report form for review extortion, per {SRC['extort']}. Use it, don’t pay, and keep screenshots. Google says it now detects more of these scams before they publish, per {SRC['gblog']}.</p>
<p>For reviews that break Google’s policy, flag them through your Business Profile. For a deeper look at why legitimate reviews vanish and how to get them back, see {L('/blog/why-are-my-google-reviews-disappearing/', 'why Google reviews disappear')}.</p>"""),

            ("What Google does to profiles that cheat", f"""<p>The FTC is slow. Google isn’t. Per {SRC['gblog']}, Google blocked or removed more than 292 million policy-violating reviews in 2025, took down over 13 million fake Business Profiles and restricted more than 782,000 accounts.</p>
<p>When Google decides a profile bought or faked reviews, its {SRC['restrict']} says the profile can be blocked from getting new reviews for a set period, have existing reviews unpublished, and show a warning telling shoppers fake reviews were removed. For a dentist in Sugar Land or an HVAC company in Cypress, that warning banner costs more than any FTC fine is likely to.</p>
<p>Customers notice too. {SRC['bl']} found 97% of consumers read reviews for local businesses, and 97% think businesses caught faking them should face consequences.</p>
<!--fig:consumers-->"""),

            ("Does the rule apply to my marketing agency or review software?", f"""<p>Yes. Agencies and reputation management firms can be liable under the rule, per the FTC’s Q&A, and you’re not off the hook because a vendor did it for you. Before you sign with anyone promising reviews, ask:</p>
<ul>
<li>Where do the reviews come from? (The only right answer is your real customers.)</li>
<li>Does the software gate by rating, or send everyone the same link?</li>
<li>Does it write, suggest or “polish” review text for customers?</li>
<li>Do you guarantee a number of reviews or a star rating? (If yes, walk.)</li>
<li>Will you post reviews from accounts you control?</li>
</ul>
<p>The same logic covers creators and influencers. Paid or gifted posts are endorsements and need disclosure; we cover that in {L('/blog/ftc-rules-influencer-partnerships/', 'FTC rules for influencer partnerships')}.</p>
<p>Your own website counts too. The FTC’s Q&A is clear that putting testimonials in your advertising isn’t “hosting” reviews, so the testimonials page, the quotes on your landing pages and the reviews in your Facebook ads all have to be real customers describing real experiences. Copy them word for word, get permission, and don’t stitch two customers into one glowing quote. Our {L('/blog/social-proof-reviews-testimonials/', 'guide to reviews and testimonials on your site')} covers how to display them well, and {L('/blog/complete-guide-google-reviews/', 'the Google reviews guide')} covers the asking side in more depth.</p>"""),

            ("A review program that’s legal everywhere", f"""<p>The program that satisfies the FTC, Google and common sense is boring, and it works because it’s steady. BrightLocal’s survey found 74% of consumers only care about reviews from the last three months, so a slow, constant flow beats a burst.</p>
<!--fig:recency-->
<!--fig:program-->
<p>Sample text message, sent the day the job closes: “Hi Maria, thanks for choosing us for your AC repair today. If you have a minute, an honest review helps other Woodlands families find us: [link]. Anything not right? Just reply here.” Same message to every customer. No incentive, no tech name prompt.</p>
<p>Then reply to every review within a couple of business days. BrightLocal found 89% of consumers expect owners to respond, and half are put off by templated replies, so write them like a person.</p>
<!--fig:audit-->
<p>If you’d like a senior strategist to build a review and reputation plan around your business and your goals, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Is it illegal to ask customers for Google reviews in Texas?",
             "No. Asking real customers for honest reviews is legal under the FTC rule and allowed by Google, as long as you ask everyone, don’t offer incentives, and don’t filter out unhappy customers. Texas doesn’t add a ban on asking. What gets businesses in trouble is fake reviews, paid reviews, staff reviews, review gating and threatening people over negative reviews. Yelp is the exception: it asks businesses not to request reviews at all."),
            ("Can I get fined for fake Google reviews my old marketing company posted?",
             "Possibly. The FTC rule covers businesses that buy or procure fake reviews, and the FTC says agencies and reputation firms can be liable too, so both sides can be exposed. Penalties apply to knowing violations, including when you should have known. If you suspect a past vendor posted fake reviews, stop the practice, document what happened and talk to an attorney about cleanup before Google restricts your profile."),
            ("Can my employees leave Google reviews for my business?",
             "Not on Google. Google removes reviews based on a conflict of interest, including current or former employment. The FTC rule allows insider reviews only with a clear disclosure, but that doesn’t override Google’s policy. Since April 2026, Google also bars asking staff to collect a set number of reviews or reviews that name them. Have employees ask customers to review instead, using the same link for everyone."),
            ("What is the penalty for fake reviews under the FTC rule in 2026?",
             "Up to $53,088 per violation for knowing violations. The FTC did not make its usual inflation adjustment for 2026 because the government shutdown delayed the data it relies on, so 2025 amounts still apply. Each fake or bought review can be counted as a separate violation. Courts decide the actual amount, and the FTC can also seek refunds for customers and orders that change how a business operates."),
            ("Are review management tools that filter unhappy customers allowed?",
             "Filtering, or review gating, is prohibited by Google, which bars merchants from selectively soliciting positive reviews. The FTC rule doesn’t name gating, but the FTC says it could violate the FTC Act. Many tools still offer the setting, so check yours. Send every customer the same review link, and offer private feedback as a separate option shown to everyone, not as a detour for unhappy customers."),
        ],
        "figures": {
            "numbers": {
                "type": "stats",
                "title": "The FTC review rule in four numbers",
                "stats": [["$53,088", "Maximum civil penalty per violation"], ["Oct 2024", "Rule took effect (October 21)"], ["10", "Warning letters sent in December 2025"], ["15,000+", "Fake Business Profiles alleged in one home services case"]],
                "alt": "Key numbers on the FTC fake review rule for Houston and The Woodlands local businesses, including the $53,088 penalty",
                "caption": f"From the {SRC['ftcqa']}, {SRC['fr26']} and {SRC['phs']}.",
            },
            "timeline": {
                "type": "steps",
                "title": "From rule to real cases",
                "sub": "How enforcement has moved toward local businesses",
                "steps": [["October 2024", "Consumer Reviews and Testimonials Rule takes effect."], ["December 2025", "FTC sends warning letters to 10 companies."], ["April 2026", "TruHeight case: employee reviews and product for five stars."], ["April 2026", "Google bars staff review quotas and staff-name prompts."], ["May 2026", "DOJ and FTC sue a home services lead seller over 15,000+ fake profiles."]],
                "alt": "Timeline of FTC fake review rule enforcement and Google review policy changes relevant to Houston and The Woodlands businesses",
                "caption": "The home services case is a complaint, not a finding, but it shows where enforcement is looking.",
            },
            "incentives": {
                "type": "compare",
                "title": "Review incentives: federal law vs. Google",
                "left": {"title": "Can be legal under the FTC rule", "items": ["$10 off for any review, good or bad", "Gift card drawing for all reviewers", "Disclosed family member review", "Disclosed employee review", "Asking at checkout"]},
                "right": {"title": "What Google allows", "items": ["No discounts or freebies for reviews", "No drawings or contests", "No conflict-of-interest reviews", "No staff quotas or name prompts", "Ask everyone, with no pressure on site"]},
                "alt": "Comparison of review incentives allowed under the FTC fake review rule and Google policy for Houston and The Woodlands businesses",
                "caption": "Follow the stricter column. Google enforces its rules daily.",
            },
            "consumers": {
                "type": "bars",
                "title": "What local customers think about reviews",
                "sub": "U.S. consumers surveyed in 2026",
                "items": [["Read reviews for local businesses", 97, "97%"], ["Want businesses that fake reviews punished", 97, "97%"], ["Expect owners to respond", 89, "89%"], ["Put off by templated responses", 50, "50%"]],
                "highlight": [1],
                "alt": "Bar chart of 2026 consumer attitudes toward online reviews and fake reviews, relevant to Houston and The Woodlands businesses",
                "caption": f"Source: {SRC['bl']}.",
            },
            "recency": {
                "type": "columns",
                "title": "How fresh reviews need to be",
                "sub": "Share of consumers who only care about reviews from...",
                "labels": ["Last week", "Last 2 weeks", "Last 3 months"],
                "values": [18, 32, 74],
                "highlight": [2],
                "y_label": "% of consumers",
                "alt": "Column chart of how recent online reviews must be for consumers choosing a business in Houston and The Woodlands",
                "caption": f"Source: {SRC['bl']}. A steady flow of honest reviews beats a burst.",
            },
            "program": {
                "type": "steps",
                "title": "A review program that passes every rule",
                "sub": "FTC, Google and Yelp compliant",
                "steps": [["Trigger on job close", "Send the request automatically when the visit or job is marked done."], ["Same link for everyone", "No rating filter, no incentive, no staff name prompts."], ["One reminder", "A short follow-up two or three days later, then stop."], ["Separate help line", "Offer a reply or phone option to everyone, not just unhappy customers."], ["Respond to all", "Reply to every review within a couple of business days, in your own words."]],
                "alt": "Five steps for a compliant Google review program under the FTC fake review rule for Houston and The Woodlands businesses",
                "caption": "Skip Yelp in the request; its guidelines ask businesses not to solicit.",
            },
            "audit": {
                "type": "checklist",
                "title": "Ten-minute review compliance audit",
                "sub": "Run this on your own Houston or The Woodlands business today",
                "items": ["Review tool sends one link to every customer", "No discounts, drawings or freebies tied to reviews", "No staff review quotas or name prompts", "No reviews from owners, staff or relatives on Google", "No bought followers or engagement", "Responses to negatives are calm and factual", "No legal threats over truthful reviews", "Vendor contracts ban fake or gated reviews", "Website testimonials are real and permitted"],
                "alt": "Checklist to audit review practices against the FTC fake review rule for a Houston or The Woodlands business",
                "caption": "Any “no” on this list is worth fixing before Google or the FTC notices.",
            },
        },
    },
]
