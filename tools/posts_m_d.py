"""Batch 13 (module m_d): Google Ads click fraud and spam leads, and Google Ads Quality Score / lowering CPC.

Research, click fraud post: Google Ads Help "Managing invalid traffic" (answer 11182074: definition and examples incl.
competitor clicks, automated filters plus Ad Traffic Quality team, no charge for pre-billing detections, "Invalid
activity" adjustments in Billing > Summary, Invalid clicks column path, Invalid traffic card, Click Quality Form covering
the last 60 days, data to prepare, investigations won't confirm individual clicks, reCAPTCHA / server-side validation /
double opt-in for invalid leads, spikes and NAT notes); Google Ads Help "Exclude IP addresses" (answer 2456098: 500 per
campaign, account-level list covers PMax/Demand Gen/Search/Shopping/Display/YouTube, campaign-level not available for
video, hotel, app, PMax or Smart Display); Google Ads Help "Exclude placements at the account level" (answer 7331110:
65,000 per account, covers Search Partner Network sites since March 2024, applies to PMax, Tools > Content suitability >
Advanced settings); PPC Land on Search Partner Network placement reporting (Aug 19, 2025) and on PMax partner
controls (parked domains removed Feb 10, 2026; channel prioritization from Oct 15, 2026; "Partners" alpha); Google Ads
Help "Offline conversion imports FAQs" (answer 10029210: GCLID 90 days, enhanced conversions 63 days, upload daily for
Smart Bidding, start with enhanced conversions for leads); Google Ads Help "Track calls from ads" (answer 6095882:
minimum duration, recording US/Canada); PPC Land on AI-qualified call conversions (Help Center doc April 21, 2026);
Google reCAPTCHA v3 developer docs (score 0.0-1.0, start at 0.5).

Research, Quality Score post: Google Ads Help "About Quality Score for Search campaigns" (answer 6167118: 1-10 scale,
keyword level, three components rated Above average / Average / Below average, exact searches over 90 days, "not an
input in the ad auction", "—" status, column path, (hist.) columns, match type changes don't affect it); "About ad
quality" (answer 156066: "Higher quality ads typically cost less per click", bids/account structure/ad frequency/reported
conversions don't affect ad quality); "About Ad Rank" (answer 1722122: six factors, calculated every search, twice per
auction); "Actual cost-per-click (CPC): Definition" (answer 6297: pay what's minimally required, reserve price, max CPC
cap and exceptions); "About responsive search ads" (answer 7684791: 3-15 headlines of 30 characters, 2-4 descriptions of
90, pinning, 15% more clicks and conversions Poor to Excellent); "Optimise your ads and landing pages" (answer 6238826).
Competitor/PAA phrasing read for "google ads click fraud", "google ads spam leads", "competitor clicking my ads",
"google ads invalid clicks refund", "google ads quality score", "how to lower cpc google ads", "how is cpc calculated".
Not used (couldn't verify or not current): any industry-wide "percent of clicks are fraudulent" figure, Google's old
published actual-CPC formula, specific third-party tool pricing.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # click fraud post
    "ivt": A("https://support.google.com/google-ads/answer/11182074?hl=en", "Google’s invalid traffic help page"),
    "ivt2": A("https://support.google.com/google-ads/answer/11182074?hl=en", "same Google page"),
    "ip": A("https://support.google.com/google-ads/answer/2456098?hl=en-AU", "Google’s IP exclusion help page"),
    "plex": A("https://support.google.com/adwords/answer/7331110", "Google’s account-level placement exclusion page"),
    "spn": A("https://ppc.land/google-enables-full-placement-reporting-for-search-partner-network/", "PPC Land"),
    "pmax": A("https://ppc.land/googles-pmax-opt-out-for-display-and-partners-still-in-alpha-after-5-months/", "PPC Land’s timeline of the Performance Max partner controls"),
    "oci": A("https://support.google.com/google-ads/answer/10029210", "Google’s offline conversion import FAQ"),
    "calls": A("https://support.google.com/google-ads/answer/6095882?hl=en", "Google’s call tracking help page"),
    "aicall": A("https://ppc.land/google-ads-now-uses-ai-to-qualify-phone-call-leads/", "PPC Land"),
    "recap": A("https://developers.google.com/recaptcha/docs/v3", "Google’s reCAPTCHA v3 documentation"),
    # quality score post
    "qs": A("https://support.google.com/google-ads/answer/6167118?hl=en", "Google’s Quality Score help page"),
    "adq": A("https://support.google.com/google-ads/answer/156066", "Google’s ad quality page"),
    "rank": A("https://support.google.com/google-ads/answer/1722122?hl=en", "Google’s Ad Rank page"),
    "cpc": A("https://support.google.com/google-ads/answer/6297?hl=en", "Google’s actual CPC definition"),
    "rsa": A("https://support.google.com/google-ads/answer/7684791", "Google’s responsive search ads page"),
    "opt": A("https://support.google.com/google-ads/answer/6238826?hl=en-GB", "Google’s guide to optimizing ads and landing pages"),
}

FRAUD = "/blog/google-ads-click-fraud-spam-leads/"
QS = "/blog/google-ads-quality-score-lower-cost-per-click/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: click fraud and spam leads
    {
        "slug": "google-ads-click-fraud-spam-leads",
        "title": "Google Ads Click Fraud and Spam Leads: What’s Real and How to Stop It",
        "seo_title": "Google Ads Click Fraud & Spam Leads: How to Stop It",
        "desc": "Google Ads click fraud and spam leads: what Google filters and credits, Search Partners and PMax junk, competitor clicks, IP limits, form and call spam fixes.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google Analytics", "Tag Manager"],
        "art": "b4",
        "hero": "clock",
        "hero_alt": "Illustration of a shield for stopping Google Ads click fraud and spam leads in Houston and The Woodlands",
        "related": ["google-ads-not-converting-clicks-no-calls", "facebook-lead-ads-bad-leads-fix-quality", "track-form-submissions-phone-calls-ga4-google-ads"],
        "sections": [
            (None, f"""<p>Monday, 7:15 a.m., at a plumbing company in Katy. The owner opens the CRM to 23 weekend form fills from Google Ads. Nine are gibberish (“asdf asdf,” a phone number of 1234567890). Four are offers to “rank your website #1.” Three are real people who wanted a water heater quote and never got a call back because everyone assumed the whole batch was junk. The rest are hard to tell.</p>
<p>By 7:30 he’s convinced the guy across FM 1463 is clicking his ads.</p>
<p>Maybe. More often, what’s going on is a mix of three separate problems that get lumped together as “click fraud”: invalid clicks that Google mostly catches and doesn’t bill, form and call spam that Google can’t see at all, and campaign settings that buy cheap, low-quality traffic on purpose. Each has a different fix. The worst move is the common one, which is counting all those junk form fills as conversions and letting Smart Bidding go find more of them.</p>
<p>Below: what Google actually filters, where the junk comes from, how to block it, and how to file a claim when you think Google missed something.</p>"""),

            ("Invalid clicks, spam leads and bad targeting are three different problems", f"""<p>Google defines invalid traffic as traffic that “doesn’t represent genuine interest in your business,” and its examples include bots, accidental clicks, fraudulent placements like clickjacking and ad stacking, and deliberate clicks by competitors or people paid to click, per {SRC['ivt']}. That’s the click side.</p>
<p>The lead side is different. A bot that skips your ad entirely and hammers your contact form isn’t a click problem, and neither is a human in another country filling out forms for a few cents each. Google says plainly that it can’t control what visitors do after the click, and it recommends reCAPTCHA, server-side validation and double opt-in for invalid leads (same page).</p>
<p>Then there’s the third bucket, which isn’t fraud at all: real people who were never going to buy. Somebody who searched “plumber salary Houston” and clicked, or a kid on a mobile game who tapped a Display ad by accident. Those are targeting problems, and they’re usually the biggest of the three.</p>
<!--fig:types-->
<p>Sorting your junk into these buckets is the first job, because the fixes don’t overlap much. A click-fraud tool won’t stop form spam from a bot that never clicked an ad. A reCAPTCHA won’t stop you from paying for clicks on a parked domain.</p>"""),

            ("What Google already filters, and how to see it in your account", f"""<p>Google runs automated filters and machine learning on every click, and its Ad Traffic Quality team does manual reviews on top of that. Clicks it flags before your billing cycle closes are never charged. Clicks it catches later are credited “when appropriate and possible,” usually in the next billing cycle, and they show up on your invoice as “Invalid activity” adjustments, per {SRC['ivt']}.</p>
<p>You can see the filtered clicks yourself. Most owners never have.</p>
<ol>
<li>In Google Ads, go to <b>Campaigns</b> in the Campaigns menu.</li>
<li>Click the <b>Columns</b> icon above the table.</li>
<li>Search “Invalid clicks” in the column picker and add <b>Invalid clicks</b> and <b>Invalid click rate</b>.</li>
<li>Click <b>Apply</b>, then set the date range to the last 90 days.</li>
</ol>
<p>Those numbers are clicks Google already threw out. You weren’t charged for them, and they aren’t in your Clicks column. Google’s Overview page is also rolling out an Invalid traffic card with “Estimated savings” and “Credited cost,” and the credits themselves live under <b>Billing &gt; Summary</b>, in the Adjustments dropdown on the Month card.</p>
<p>A couple of things Google’s page says that are worth knowing before you panic. There’s no industry standard for a “normal” invalid click rate. Traffic spikes aren’t automatically fraud; demand, competitor budget changes and your own keyword changes cause them too. That matters in Houston, where a freeze warning or a storm in the Gulf can triple plumbing and roofing searches overnight. And zero-second visits in your analytics are often real people whose session never registered a second hit, while shared IP addresses are normal on office and mobile networks that route lots of users through one address.</p>
<!--fig:stats-->"""),

            ("Is a competitor clicking your ads?", f"""<p>Sometimes, yes. Google lists deliberate competitor clicks as invalid traffic, so it isn’t a myth. In local accounts we’ve run, though, the competitor clicking an owner is sure about rarely shows up in the data. What does show up is the competitor’s office manager searching your company name once a week to see your ads, which costs you a few dollars a month. Repeated clicks from the same source on the same day are exactly the pattern Google’s filters are built to catch.</p>
<p>If you suspect someone specific, the evidence you want is in your web server logs or analytics: the same IP address or device hitting your landing page from paid clicks several times in a short window, with no form fill and no call.</p>
<p>IP exclusions have real limits, and they’re worth knowing before anyone sells you a tool built around them. Per {SRC['ip']}:</p>
<ul>
<li>You can exclude up to <b>500 IP addresses per campaign</b>. An asterisk in place of the last part of an address blocks a range.</li>
<li>An <b>account-level</b> IP exclusion list (Admin &gt; Account settings &gt; IP exclusions) applies to every campaign, including Performance Max, Demand Gen, Search, Shopping, Display and YouTube.</li>
<li><b>Campaign-level</b> exclusions (campaign Settings &gt; Additional settings &gt; IP exclusions) aren’t available for video, hotel, app, Performance Max or Smart Display campaigns.</li>
<li>If both lists exist, Google merges them.</li>
</ul>
<p>Now the practical problem. Most phone traffic in Houston comes through carrier networks where thousands of people share and rotate addresses, so blocking a mobile IP can block your neighbors and won’t stop the person you were after for long. IP blocking works well against a fixed office connection or a hosting provider’s range. Against a determined person on a phone, it barely works. And don’t block your own office: just have your staff stop clicking your ads to “check on them.” Use the Ad Preview and Diagnosis tool instead.</p>"""),

            ("Search Partners, Display and Performance Max: where most junk comes from", f"""<p>When we look at a lead-gen account full of spam, the source is usually network settings rather than a fraud ring. A Search campaign created with the defaults opts you into Google Search Partners and often the Display Network too. Performance Max serves across Search, Display, YouTube, Gmail, Maps and partner sites by design.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Source</th><th>What the junk looks like</th><th>The control</th></tr></thead>
<tbody>
<tr><td>Search Partners (Search campaigns)</td><td>Cheap clicks, low engagement, odd form fills at odd hours</td><td>Segment by Network; uncheck “Include Google search partners” in campaign Settings &gt; Networks if it doesn’t produce real leads</td></tr>
<tr><td>Display Network (opted in from a Search campaign)</td><td>Accidental taps in mobile games and apps, near-zero time on site</td><td>Uncheck “Include Google Display Network” on Search campaigns; run Display separately, on purpose, if at all</td></tr>
<tr><td>Performance Max placements</td><td>Lead forms from apps and low-quality sites, spam that converts “cheaply”</td><td>Account-level placement exclusions, brand-safe content settings, offline conversion data, and the newer channel controls</td></tr>
<tr><td>Google lead form assets</td><td>Fast, prefilled submissions from people who barely read the ad</td><td>Add qualifying questions and call every lead fast; judge on booked jobs</td></tr>
<tr><td>Your own website form</td><td>Bot submissions that never came from an ad at all</td><td>reCAPTCHA, honeypot, server-side validation (next section)</td></tr>
</tbody></table></div>
<p>Google has added more visibility here. In August 2025 it announced full placement reporting for the Search Partner Network across Search, Shopping and App campaigns, listing each partner site with impressions, according to {SRC['spn']}. It ended parked domains as a Search Partner surface on February 10, 2026, and in October 2026 it started rolling out channel prioritization controls in Performance Max that let you set Search partners and Display to low priority with a best-effort budget cap, per {SRC['pmax']}.</p>
<p>For placements you’ve identified as junk, account-level placement exclusions are the tool. Per {SRC['plex']}, they live under <b>Tools &gt; Content suitability &gt; Advanced settings &gt; Excluded placements</b>, they override campaign settings, they apply to Performance Max, they’ve covered Search Partner sites since March 2024, and you can have up to 65,000 per account.</p>
<!--fig:networks-->
<p>Our rule of thumb for a local service business: run Search with partners off until you have clean conversion data, then test partners on in one campaign and compare cost per <i>booked job</i>, which is a different number from cost per form fill. We cover the network checks in more detail in {L('/blog/google-ads-not-converting-clicks-no-calls/', 'our clicks-but-no-calls audit')}, and the Search vs. PMax trade-off in {L('/blog/performance-max-vs-search-campaigns-local/', 'Performance Max vs. Search for local businesses')}.</p>"""),

            ("Stop form spam at the form", f"""<p>Form spam is the one problem you own outright. Google can’t filter a bot that submits your contact form directly, and plenty of spam on a typical Woodlands or Sugar Land service-business site never touched an ad. It still pollutes your lead count, and if your conversion tag fires on the thank-you page, it pollutes your Google Ads data too.</p>
<p>The fixes stack. None of them is enough alone.</p>
<!--fig:formdefense-->
<p>A few notes on the list. {SRC['recap']} describes v3 as invisible to visitors and returning a score where 1.0 is very likely a good interaction and 0.0 is very likely a bot; Google suggests starting your cutoff at 0.5 and adjusting from your own traffic. Google has since moved reCAPTCHA documentation under Google Cloud, so check which version your form plugin uses. A honeypot is a hidden field that people never see and bots fill in; any submission with that field filled gets dropped. Server-side validation means your website rejects a fake phone number or a disposable email domain before the lead is stored, not just with a JavaScript warning a bot can skip.</p>
<p>The biggest single change, though, is moving the conversion. If Google Ads counts a conversion every time the thank-you page loads, every bot that reaches it is a “lead.” Fire the conversion only on validated submissions, and then send back which leads were real (the offline conversion section below). Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'form and call tracking guide')} shows the setup in GA4 and Tag Manager.</p>
<p>One caution: don’t add so much friction that real customers give up. A homeowner in Spring with water on the kitchen floor won’t solve a puzzle. Invisible checks first, and a visible challenge only for submissions that already look suspicious.</p>"""),

            ("Call spam and junk calls", f"""<p>Calls are harder to fake at scale than forms, but Houston businesses still get plenty of junk: robocalls offering business loans, “Google listing” scam calls, wrong numbers, and real people looking for a different company with a similar name.</p>
<p>For years, Google Ads counted a call as a conversion if it lasted longer than a minimum duration you set, per {SRC['calls']}. That meant a three-minute robocall pitch could count as a lead. In April 2026, Google documented AI-qualified call conversions: when call recording is on, Google reviews the recording for signs of real interest and only counts calls that pass, falling back to the duration threshold when a call can’t be recorded, per {SRC['aicall']}. Recording only works when both numbers are in the U.S. or Canada, and the setting is under Admin &gt; Account settings &gt; Call ads &gt; Call recording.</p>
<p>What we’d do for a Houston service business:</p>
<ul>
<li>Check your call conversion action’s duration threshold. If your real booking calls take four minutes, a 30-second threshold is counting a lot of noise.</li>
<li>Use a call tracking platform with recordings and tag each call (booked, quote, spam, existing customer, wrong number). Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers options.</li>
<li>Schedule call assets only for hours someone answers, so after-hours spam doesn’t ring to a voicemail nobody checks.</li>
<li>Don’t confuse ad-driven spam with Business Profile scam calls, which have their own fix in our post on {L('/blog/google-business-listing-scam-calls/', 'Google listing scam calls')}.</li>
</ul>"""),

            ("Train bidding on real leads with offline conversion imports", f"""<p>This is the fix that matters most and gets skipped most. Smart Bidding strategies like Maximize conversions and Target CPA chase whatever you tell them is a conversion. If spam form fills count, the algorithm learns that the cheapest “conversions” come from junk placements, and it buys more of them. You end up with a lower cost per lead and fewer customers. We see this constantly in accounts we take over.</p>
<p>The answer is to tell Google which leads turned into something real. Two ways to do it:</p>
<ul>
<li><b>GCLID import.</b> Your form captures the Google click ID, your CRM stores it, and you upload qualified leads and closed jobs back to Google Ads. Per {SRC['oci']}, Google keeps the click ID for 90 days, so uploads must happen within 90 days of the click.</li>
<li><b>Enhanced conversions for leads.</b> Instead of the click ID, Google matches hashed email or phone numbers from your form to the click. Google’s FAQ recommends starting here if you haven’t set up offline imports yet, because it’s easier, and notes uploads with that personal data can go back 63 days.</li>
</ul>
<p>Google also recommends uploading daily for Smart Bidding, or on a steady schedule if you can’t, and uploading a new conversion action consistently for one to two conversion cycles before you make it the one bids optimize to (same FAQ).</p>
<!--fig:oci-->
<p>Once real lead and booked-job conversions are flowing, change your primary conversion goal to the qualified one and demote raw form fills to secondary. It’s the same idea we describe for Meta in {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'how to fix bad Facebook lead quality')}: the platform finds more of what you reward. Fast follow-up matters here too, since a lead nobody calls can’t be qualified. See {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'our speed-to-lead post')}.</p>"""),

            ("Third-party click-fraud tools: when they’re worth paying for", f"""<p>There’s a whole category of click-protection software (ClickCease, ClickGUARD, Fraud Blocker, Lunio and TrafficGuard are names you’ll run into). We don’t have affiliate deals with any of them, and we don’t think every account needs one.</p>
<p>What they generally do: put a script on your site, fingerprint visitors who arrive from paid clicks, score them, and push suspicious IP addresses into your Google Ads exclusion list automatically. Several also help you assemble refund claims.</p>
<p>The honest caveats:</p>
<ul>
<li>They’re working with the same 500-per-campaign IP limit and the same rotating mobile addresses described above.</li>
<li>Their dashboards often count clicks Google already filtered and didn’t charge you for, which makes the “fraud saved” number look bigger than the money you’d actually have lost.</li>
<li>They don’t fix bad network settings or thank-you-page conversion tags, which cause more junk than fraud does in most local accounts.</li>
</ul>
<p>Where they can pay for themselves: high-CPC niches like legal, emergency restoration or HVAC in July, where a few dozen bad clicks a month cost real money, or accounts that keep seeing the same suspicious patterns after the basic fixes are in. If you try one, use the trial period to compare your cost per booked job before and after. If it doesn’t move that number, cancel it.</p>"""),

            ("How to request an invalid activity investigation", f"""<p>If you’ve done the basics and still believe Google charged you for clicks it shouldn’t have, file a claim. Per {SRC['ivt']}, you submit it through Google’s Click Quality Form, it covers activity from the <b>last 60 days</b>, reviews typically take several business days, and the findings come by email.</p>
<!--fig:claim-->
<p>Gather this before you open the form, from that same Google page: your 10-digit Customer ID, the exact date range, the campaign and ad group names, the keywords you’re suspicious of, web server logs showing IP addresses, devices and GCLIDs, any relevant lead details, and the trends that made you suspicious. A vague “I think my competitor is clicking” claim with no logs rarely gets anywhere. A spreadsheet of 40 paid clicks from three IPs in two hours, with GCLIDs, is something an investigator can check.</p>
<p>Set expectations. Google says investigations won’t confirm whether specific clicks were marked valid or invalid, and credited clicks don’t retroactively change your campaign metrics, which are frozen at month end. If they find something, the credit appears as an Invalid activity adjustment. And since the 60-day window is fixed, don’t sit on a suspicion for a quarter.</p>"""),

            ("A first-month cleanup plan", f"""<p>If you’re looking at a messy account right now, this is the order we’d go in.</p>
<p><b>Week 1.</b> Add the Invalid clicks columns and check the last 90 days. Segment every Search campaign by Network and look at Search Partners and Display separately. Pull a list of the last 100 leads and tag each one real, spam or unclear. That gives you a baseline.</p>
<p><b>Week 2.</b> Turn off the Display Network on Search campaigns. Turn off Search Partners on any campaign where partner leads are mostly junk. Add account-level placement exclusions for the worst Performance Max placements. Add reCAPTCHA v3 and a honeypot to every form, and move the conversion tag so it fires only on validated submissions.</p>
<p><b>Week 3.</b> Set up enhanced conversions for leads or GCLID capture. Start tagging leads as qualified in your CRM and uploading them daily. Fix call conversion thresholds and turn on call recording if your business type allows it.</p>
<p><b>Week 4.</b> If anything still looks wrong, pull the server logs and file a Click Quality Form claim inside the 60-day window. Then decide whether a third-party tool is worth a trial.</p>
<p>After that, judge everything on cost per booked job. If the spam is gone and leads still aren’t closing, the problem has moved to the landing page or the phones, and our {L('/blog/google-ads-quality-score-lower-cost-per-click/', 'Quality Score guide')} is a good next read. Our {L('/services/search-marketing/', 'search marketing team')} does this cleanup for businesses across Greater Houston; if you’d like a senior strategist to look at your account and build a plan around your goals, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Does Google refund invalid clicks?",
             "Google doesn’t charge for clicks its filters flag before your billing cycle closes, so no refund is needed for those. Clicks found invalid later are credited when appropriate and possible, usually in the next billing cycle, and appear as Invalid activity adjustments under Billing, Summary. You can see filtered clicks by adding the Invalid clicks and Invalid click rate columns at the campaign level."),
            ("How do I know if a competitor is clicking my Google Ads?",
             "Look for repeated paid clicks from the same IP address or device in a short window, with no calls or form fills, in your server logs or analytics. Google treats deliberate competitor clicks as invalid traffic and filters many automatically. If the pattern comes from a fixed office connection, exclude that IP. If you believe you were charged, file a Click Quality Form claim within 60 days."),
            ("How many IP addresses can I exclude in Google Ads?",
             "Google allows up to 500 IP address exclusions per campaign, and you can block a range by using an asterisk for the last part of an address. An account-level IP exclusion list applies to every campaign type, including Performance Max. Campaign-level exclusions aren’t available for video, hotel, app, Performance Max or Smart Display campaigns. Mobile IPs rotate, so blocking them is unreliable."),
            ("Why am I getting so many spam leads from Google Ads?",
             "The usual causes are Search Partners and Display placements opted in by default, Performance Max serving on low-quality apps and sites, and bots submitting your website form directly. Counting every form fill as a conversion makes it worse, because Smart Bidding learns to find more cheap junk. Add reCAPTCHA and a honeypot, tighten network settings, and import qualified leads as your main conversion."),
            ("Are click fraud protection tools worth it?",
             "Sometimes. They fingerprint paid visitors and add suspicious IPs to your exclusion list automatically, which helps in high-cost niches like legal, restoration or summer HVAC. They still face the 500-IP limit and rotating mobile addresses, and they don’t fix network settings or bad conversion tracking. Use a trial and compare cost per booked job before and after. Keep it only if that number improves."),
        ],
        "figures": {
            "types": {
                "type": "compare",
                "title": "Bot clicks vs. form spam",
                "left": {"title": "Invalid clicks (Google’s side)", "items": ["Bots and click farms hitting ads", "Accidental taps in apps", "Repeat clicks by a competitor", "Mostly filtered, not billed", "Claim via Click Quality Form"]},
                "right": {"title": "Spam leads (your side)", "items": ["Bots submitting your form directly", "Fake names, numbers and emails", "Robocalls and wrong numbers", "Google can’t see or credit these", "Fix with validation and lead import"]},
                "alt": "Comparison of Google Ads invalid clicks and spam leads for Houston and The Woodlands businesses, with who fixes each",
                "caption": "Most junk-lead complaints are the right-hand column. Different problem, different fix.",
            },
            "stats": {
                "type": "stats",
                "title": "The limits that shape your options",
                "stats": [["60", "days back a click investigation can cover"], ["500", "IP exclusions per campaign"], ["65,000", "account-level placement exclusions"], ["90", "days to upload a GCLID conversion"]],
                "note": "Source: Google Ads Help",
                "alt": "Stats on Google Ads invalid click investigation, IP exclusion and offline conversion limits for Houston advertisers",
                "caption": f"From {SRC['ivt']}, {SRC['ip']}, {SRC['plex']} and {SRC['oci']}.",
            },
            "networks": {
                "type": "bars",
                "title": "Where spam leads came from",
                "sub": "Share of leads tagged spam, by network, in one example lead-gen account",
                "items": [["Google Search", 8, "8%"], ["Search Partners", 31, "31%"], ["Display (via Search campaign)", 46, "46%"], ["Performance Max", 27, "27%"]],
                "highlight": [2],
                "note": "Illustrative example",
                "alt": "Bar chart of an illustrative share of spam leads by Google Ads network for a Houston service business",
                "caption": "Illustrative. Run this split on your own last 100 leads; your numbers will differ.",
            },
            "formdefense": {
                "type": "checklist",
                "title": "Form spam defenses, in order",
                "sub": "Stack these; none is enough alone",
                "items": ["reCAPTCHA v3 with a score cutoff (start near 0.5)", "Hidden honeypot field that drops bot submissions", "Server-side checks on phone number and email format", "Block disposable email domains", "Reject forms submitted in under 3 seconds", "Fire the Ads conversion only on validated leads", "Optional confirmation text or email for high-value forms", "Tag every lead real or spam in your CRM"],
                "alt": "Checklist of website form spam defenses for Google Ads lead generation in Houston and The Woodlands",
                "caption": "Invisible checks first. Don’t make a homeowner with a flooded kitchen solve a puzzle.",
            },
            "oci": {
                "type": "steps",
                "title": "Teach Smart Bidding what a real lead is",
                "sub": "Offline conversion import loop",
                "steps": [["Capture the click", "Store GCLID or hashed email and phone with every lead."], ["Qualify in the CRM", "Mark leads real, booked or closed. Mark spam too."], ["Upload daily", "Send qualified leads back within Google’s window."], ["Switch the goal", "Make qualified leads primary; demote raw form fills."], ["Judge on booked jobs", "Watch cost per booked job, not cost per form."]],
                "alt": "Steps to import offline conversions into Google Ads so a Houston business trains bidding on real leads",
                "caption": f"Upload windows: 90 days with GCLID, 63 days with enhanced conversions data, per {SRC['oci']}.",
            },
            "claim": {
                "type": "steps",
                "title": "Filing an invalid activity claim",
                "steps": [["Check the window", "Only the last 60 days are covered."], ["Pull server logs", "IPs, devices, timestamps and GCLIDs for paid clicks."], ["Note the pattern", "Campaigns, ad groups, keywords and dates."], ["Submit the form", "Click Quality Form with your 10-digit Customer ID."], ["Watch for credits", "Invalid activity adjustments under Billing."]],
                "alt": "Steps for a Houston business to request a Google Ads invalid click investigation and credit",
                "caption": "Specific logs get investigated. A hunch without data usually doesn’t.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: quality score
    {
        "slug": "google-ads-quality-score-lower-cost-per-click",
        "title": "Google Ads Quality Score: How to Lower Your Cost per Click",
        "seo_title": "Google Ads Quality Score: How to Lower Your CPC",
        "desc": "How Google Ads Quality Score works: expected CTR, ad relevance and landing page experience, how Ad Rank sets your CPC, and the fixes that lower what you pay.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google", "Google Analytics"],
        "art": "b3",
        "hero": "search",
        "hero_alt": "Illustration of a search bar for Google Ads Quality Score and lowering cost per click in Houston and The Woodlands",
        "related": ["google-ads-cost-per-click-houston-benchmarks", "landing-pages-101", "small-business-guide-google-ads-2026"],
        "sections": [
            (None, f"""<p>Second week of July in The Woodlands. It’s 98 degrees, every AC company in Montgomery County has raised its Google Ads budget, and an HVAC owner is looking at his keyword report. “AC repair The Woodlands” shows a Quality Score of 3. His average cost per click on it has crept past what he was paying for whole jobs’ worth of leads a few summers ago.</p>
<p>His agency says Quality Score “doesn’t really matter anymore.” A forum thread says it’s the only thing that matters. Both are partly wrong.</p>
<p>Quality Score is Google’s 1-to-10 report card on how your ads and landing pages compare with other advertisers on the same searches. The score itself isn’t used in the auction. The quality it summarizes is, and Google says plainly that higher quality ads typically cost less per click. So you don’t chase the number. You fix what it’s pointing at, and the price comes down.</p>
<p>This guide covers how Google actually reports Quality Score, how Ad Rank and your cost per click are set, and the specific changes to ad groups, ads and landing pages that move it. If you want the price side first, our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} show what local businesses typically pay.</p>"""),

            ("What Quality Score is, in Google’s own words", f"""<p>From {SRC['qs']}: Quality Score “is a diagnostic tool meant to give you a sense of how well your ad quality compares to other advertisers.” It’s measured from 1 to 10 and reported at the keyword level, for Search campaigns. It isn’t reported for an ad group or a campaign, and Performance Max doesn’t have it at all.</p>
<p>It has three components, each rated <b>Above average</b>, <b>Average</b> or <b>Below average</b>:</p>
<ul>
<li><b>Expected clickthrough rate</b>: how likely your ad is to be clicked when it shows.</li>
<li><b>Ad relevance</b>: how closely your ad matches the intent behind the search.</li>
<li><b>Landing page experience</b>: how relevant and useful your page is to the people who click.</li>
</ul>
<p>The comparison is against other advertisers whose ads showed for the exact same search over the last 90 days, based on historical impressions for exact searches. That has a few consequences people miss. Changing a keyword’s match type doesn’t change its Quality Score. A broad match keyword can show a score with no impressions of its own if a matching exact keyword in the same ad group has data. And if there aren’t enough exact-match searches, you’ll see a “—” instead of a number. That’s common on long-tail local terms like “tankless water heater install Magnolia,” and it isn’t a problem.</p>
<!--fig:basics-->
<p>Google also says Quality Score is “not a key performance indicator” and shouldn’t be aggregated with other data. Treat it like the warning lights on a dashboard. A light tells you where to look.</p>"""),

            ("How to see Quality Score and its components", f"""<p>The columns are hidden by default. Per {SRC['qs']}:</p>
<ol>
<li>Go to <b>Keywords</b> under the Campaigns menu.</li>
<li>Click the <b>Columns</b> icon at the top right of the table.</li>
<li>Under “Modify columns for keywords,” open the <b>Quality score</b> section.</li>
<li>Add <b>Quality Score</b>, <b>Landing Page Exp.</b>, <b>Exp. CTR</b> and <b>Ad Relevance</b>.</li>
<li>Click <b>Apply</b>.</li>
</ol>
<p>The current columns show today’s snapshot. The “(hist.)” versions (Quality Score (hist.), Exp. CTR (hist.) and so on) show what the score was during the date range you pick, and you can segment by day to see when a change kicked in. That’s how you check whether last month’s landing page rebuild actually moved anything.</p>
<p>When we review an account, we sort keywords by cost, not by Quality Score. A QS of 4 on a keyword that spent $60 last quarter isn’t worth an afternoon. A QS of 4 on the keyword eating 30% of your budget is the whole project.</p>"""),

            ("Reported Quality Score vs. the quality the auction actually uses", f"""<p>This is the part that confuses everyone, so it’s worth being precise.</p>
<p>The 1-to-10 number is a summary built from history. The auction doesn’t read it. What the auction uses is a fresh, real-time estimate of ad quality for that particular search. Google’s {SRC['adq']} says ad quality “varies with the context of every search,” and the Quality Score page lists things the score may not capture: the searcher’s device, location and time of day, and your assets.</p>
<p>So the same keyword can have very different auction-time quality at 2 p.m. on a desktop in the Energy Corridor and at 11 p.m. on a phone in Conroe. Your QS of 6 is an average across all of that. It’s useful for finding weak spots, and useless as a target.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Reported Quality Score</th><th>Auction-time ad quality</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>A 1-10 diagnostic, per keyword</td><td>A live estimate, per search</td></tr>
<tr><td>Based on</td><td>Exact-match searches, last 90 days</td><td>That search’s context: query, device, location, time, assets</td></tr>
<tr><td>Used in the auction?</td><td>No</td><td>Yes, as part of Ad Rank</td></tr>
<tr><td>Where you see it</td><td>Keyword columns</td><td>Only indirectly, through CPC, impression share and position</td></tr>
<tr><td>How to use it</td><td>Find weak components on expensive keywords</td><td>Improve ads and pages; let the auction reward it</td></tr>
</tbody></table></div>"""),

            ("Ad Rank, and how your cost per click is actually set", f"""<p>Where your ad shows, and whether it shows at all, comes from Ad Rank. Per {SRC['rank']}, Ad Rank uses six factors:</p>
<ol>
<li>Your bid (the most you’re willing to pay for a click).</li>
<li>The quality of your ad and landing page.</li>
<li>Ad Rank thresholds, the minimum an ad must clear to show.</li>
<li>How competitive the auction is.</li>
<li>The context of the search: terms, location, device, time and other signals.</li>
<li>The expected impact of your assets and other ad formats, like sitelinks and call assets.</li>
</ol>
<p>Ad Rank is calculated every time someone searches, and twice per auction: once for eligibility and once for ranking.</p>
<p>Then the price. Per {SRC['cpc']}, you “only pay what’s minimally required to clear the Ad Rank thresholds,” which in practice means beating the Ad Rank of the advertiser just below you. With nobody below you, you pay the reserve price. On manual bidding you’re never charged more than your max CPC, though Enhanced CPC and bid adjustments can push past it. Google no longer publishes an exact formula.</p>
<p>That’s why quality lowers cost. If your quality is higher, you need less bid to reach the same Ad Rank, and the amount you need to beat the next advertiser is smaller. Google says “higher quality ads typically cost less per click than lower quality ads,” and that low-quality ads can push your actual CPC close to your max even with little competition ({SRC['adq']}).</p>
<p>Here’s a deliberately simplified model to show the mechanics. It treats Ad Rank as bid times a quality factor and ignores thresholds, assets and context, so read it as a teaching example and nothing more.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Advertiser</th><th>Max bid</th><th>Quality factor</th><th>“Ad Rank”</th><th>Position</th><th>Pays (enough to beat the next one down)</th></tr></thead>
<tbody>
<tr><td>A (tight ad group, fast page)</td><td>$14</td><td>8</td><td>112</td><td>1</td><td>about $11.26 (90 ÷ 8, plus a cent)</td></tr>
<tr><td>B (generic ad, homepage)</td><td>$18</td><td>5</td><td>90</td><td>2</td><td>about $14.41 (72 ÷ 5, plus a cent)</td></tr>
<tr><td>C</td><td>$12</td><td>6</td><td>72</td><td>3</td><td>whatever beats the next ad, or the reserve</td></tr>
</tbody></table></div>
<!--fig:auction-->
<p>Illustrative numbers. Advertiser A bids less than B, ranks higher, and pays about $3 less per click. Over 400 clicks a month on one keyword, that’s roughly $1,260. The real auction is messier, but the direction holds.</p>"""),

            ("Expected CTR: write ads people pick", f"""<p>Expected CTR is Google’s prediction of how often your ad gets clicked when it shows, compared with others on the same search. You raise it by making the ad the obvious choice for the searcher.</p>
<p>What moves it in local service accounts we’ve run:</p>
<ul>
<li><b>The search term in the headline.</b> Someone typing “emergency plumber Katy” should see “Emergency Plumber in Katy” or close to it. That isn’t a trick; it’s confirmation they found what they asked for.</li>
<li><b>A concrete reason to click.</b> “Same-day AC repair, upfront pricing, 4.9 stars from 600+ reviews” beats “Quality Service You Can Trust.” Google’s {SRC['opt']} recommends specific calls to action and differentiators like guarantees and offers.</li>
<li><b>Assets.</b> Sitelinks, callouts, call assets, location and structured snippets make the ad bigger and more useful, and their expected impact is one of the six Ad Rank factors.</li>
<li><b>Negative keywords.</b> Every impression on “ac repair jobs” or “how to recharge car ac” that doesn’t get clicked drags your CTR down. Clean the search terms report weekly at first.</li>
<li><b>Honest location and schedule settings.</b> Showing ads to people outside your service area, or at 2 a.m. when you can’t answer, earns impressions nobody clicks.</li>
</ul>"""),

            ("Ad relevance: tighten the ad groups", f"""<p>Ad relevance is the easiest component to fix and the one most often rated Below average in small accounts. The cause is almost always one big ad group with 60 keywords and two ads trying to speak to all of them.</p>
<!--fig:groups-->
<p>You don’t need single-keyword ad groups. That habit made sense years ago; with close variants and broad match, it mostly creates clutter. What you need is ad groups tight enough that one set of headlines honestly answers every keyword in them. For a Houston plumbing company, that might mean separate ad groups for water heater repair, water heater replacement, tankless installs, slab leak detection, drain cleaning and emergency service, each with its own ads and its own landing page. “Slab leak” is very much a Houston search, by the way; the clay soil here moves foundations and pipes with it.</p>
<p>A quick test: read each keyword in the ad group, then read your Headline 1. If a searcher typing that keyword would think “close, but not what I asked for,” the keyword belongs somewhere else.</p>"""),

            ("A responsive search ad strategy that helps instead of hurting", f"""<p>Responsive search ads let you give Google up to 15 headlines of 30 characters each and up to 4 descriptions of 90 characters, and Google mixes them, per {SRC['rsa']}. Up to three headlines can show at once, and only Headline 1 and Description 1 reliably appear.</p>
<p>How we write them for a local service ad group:</p>
<ul>
<li>Three or four headlines that contain the keyword theme (“Water Heater Repair Spring TX,” “Same-Day Water Heater Repair”).</li>
<li>Three or four that state proof: review count and rating, years in business, licensed and insured, your Texas license number if your trade has one.</li>
<li>Three or four with the offer or call to action: “Upfront Price Before We Start,” “Call Now, Tech Today.”</li>
<li>A couple about service area (“Serving The Woodlands to Tomball”).</li>
<li>Descriptions that read fine in any order and each make one clear point.</li>
</ul>
<p>Go easy on pinning. Google says pinning isn’t recommended for most advertisers and limits which assets can show; if you must pin, pin two or three options to a position, not one. The common exception is a legal or brand line that has to appear. Google also reports that advertisers who moved Ad Strength from Poor to Excellent saw 15% more clicks and conversions on average, from its own internal data. Treat Ad Strength as a nudge toward variety; the search terms report is still the better guide to what to write.</p>"""),

            ("Landing page experience: speed and message match", f"""<p>Landing page experience is the component most tied to whether a click becomes a customer, and it’s where most Houston small-business accounts lose. The usual sin is sending every ad to the homepage.</p>
<p>Google’s {SRC['opt']} lists the basics: a page that closely matches the ad and keywords, mirrors the ad’s call to action, is mobile-friendly and fast, keeps contact details easy to find, keeps navigation simple, avoids clutter and pop-ups, and is clear about what you do.</p>
<!--fig:landing-->
<p>In practice, message match means the page headline repeats the promise of the ad. If the ad says “Same-Day AC Repair in Cypress,” the page says that above the fold, with a phone number you can tap and a short form. Speed matters most on phones; heavy sliders, autoplay video and five tracking scripts on a cheap shared host are what we see slowing local sites down. Our {L('/blog/how-fast-should-your-website-load/', 'site speed guide')} and {L('/blog/landing-pages-101/', 'landing pages 101')} go further, and our {L('/services/web-design-seo-pr/', 'web design team')} builds pages for exactly this.</p>"""),

            ("What Quality Score doesn’t affect, and what doesn’t affect it", f"""<p>A lot of bad advice comes from treating QS as more than it is. A few things Google states outright:</p>
<ul>
<li><b>It isn’t an auction input.</b> The 1-10 number itself doesn’t set your price ({SRC['qs']}).</li>
<li><b>Bids don’t change ad quality.</b> Bids affect Ad Rank, but not Google’s assessment of your ad’s quality ({SRC['adq']}).</li>
<li><b>Account structure, ad frequency and reported conversions don’t affect it either</b> (same page). Restructuring into more campaigns doesn’t raise QS by itself; better-matched ads and pages do.</li>
<li><b>Match type changes don’t change it</b>, since it’s based on exact searches.</li>
<li><b>It isn’t a KPI.</b> A keyword with QS 5 that books jobs at a good cost is a better keyword than a QS 9 that books none.</li>
</ul>
<p>And it doesn’t exist for Performance Max, Display or Demand Gen. If most of your spend runs through Performance Max, QS tells you nothing about it; see {L('/blog/performance-max-vs-search-campaigns-local/', 'Performance Max vs. Search')} for how to judge those campaigns.</p>"""),

            ("A 30-day plan to raise Quality Score on the keywords that cost you most", f"""<p>Here’s how we’d run it.</p>
<!--fig:plan-->
<p><b>Days 1-3.</b> Add the Quality Score columns. Sort keywords by cost over the last 90 days. Mark the top 20 and note which component is Below average on each.</p>
<p><b>Days 4-10.</b> Split ad groups where ad relevance is weak. Write new responsive search ads for each split group with the keyword theme in several headlines. Add negatives from the search terms report.</p>
<p><b>Days 11-20.</b> Build or fix a dedicated landing page for each major service, matched to the ad. Check mobile speed. Make the phone number tappable and the form short.</p>
<p><b>Days 21-30.</b> Let data come in. Compare Quality Score (hist.) and average CPC on those 20 keywords to the prior period, and watch conversion rate and cost per lead alongside them.</p>
<p>If junk traffic is part of the problem, fix that in parallel using our {L('/blog/google-ads-click-fraud-spam-leads/', 'click fraud and spam leads guide')}, because spam conversions will distort any test. Our {L('/services/search-marketing/', 'search marketing team')} runs this work for businesses across The Woodlands and Greater Houston. If you’d like a senior strategist to build a plan around your goals and budget, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("What is a good Quality Score in Google Ads?",
             "Google reports Quality Score from 1 to 10 for each Search keyword. Scores of 7 and up usually mean your ads and landing pages compare well with competitors on the same searches, and a score of 4 or lower on a high-spend keyword is worth fixing. Google calls Quality Score a diagnostic, not a KPI, so judge keywords by cost per lead and booked jobs first."),
            ("Does Quality Score affect cost per click?",
             "Indirectly, yes. The 1 to 10 number isn’t used in the auction, but the ad quality it summarizes is part of Ad Rank, which decides your position and what you pay. Google says higher quality ads typically cost less per click than lower quality ads. Better expected CTR, ad relevance and landing page experience let you reach the same position with a lower bid."),
            ("How is cost per click calculated in Google Ads?",
             "Google says you pay only what’s minimally required to clear the Ad Rank thresholds and beat the Ad Rank of the advertiser just below you. If nobody is below you, you pay the reserve price. With manual bidding you won’t be charged more than your max CPC, though Enhanced CPC and bid adjustments can exceed it. Google no longer publishes an exact formula."),
            ("How long does it take for Quality Score to improve?",
             "Quality Score is based on exact-match search history over the last 90 days, so changes to ads and landing pages show up gradually as new impressions build. On busy keywords you may see movement within a few weeks. On low-volume local terms it can take longer, and some will show a dash because there isn’t enough data. Check the historical columns segmented by day."),
            ("Why does my keyword show a dash instead of a Quality Score?",
             "A dash means there haven’t been enough exact-match searches for Google to calculate a score. It’s common on long-tail local keywords like a specific service plus a small town name. It doesn’t hurt your ads. Google suggests finding higher-volume keywords in Keyword Planner or broadening match types if you want the keyword to enter more auctions and collect data."),
        ],
        "figures": {
            "basics": {
                "type": "stats",
                "title": "Quality Score at a glance",
                "stats": [["1-10", "scale, reported per Search keyword"], ["3", "components rated Above, Average or Below"], ["90", "days of exact-match search history"], ["6", "factors in Ad Rank, which sets position and price"]],
                "note": "Source: Google Ads Help",
                "alt": "Stats on how Google Ads Quality Score is reported, for Houston and The Woodlands advertisers",
                "caption": f"From {SRC['qs']} and {SRC['rank']}.",
            },
            "auction": {
                "type": "bars",
                "title": "Higher quality, lower price",
                "sub": "Simplified auction model: actual CPC paid by each advertiser",
                "items": [["A: bids $14, quality 8, ranks 1st", 11.26, "$11.26"], ["B: bids $18, quality 5, ranks 2nd", 14.41, "$14.41"]],
                "highlight": [0],
                "note": "Illustrative example. Google doesn’t publish its exact formula.",
                "alt": "Bar chart of an illustrative Google Ads auction where higher Quality Score lowers cost per click for a Houston business",
                "caption": "The better ad bids less, ranks higher and pays less per click.",
            },
            "groups": {
                "type": "compare",
                "title": "Ad group structure and ad relevance",
                "left": {"title": "One big ad group", "items": ["“Plumbing” with 60 keywords", "Two ads written for everything", "All traffic to the homepage", "Ad relevance: Below average", "High CPC on the top keywords"]},
                "right": {"title": "Tight themed ad groups", "items": ["Water heater, slab leak, drains, emergency", "Headlines that echo each theme", "A matching landing page per service", "Ad relevance: Above average", "Same position at a lower bid"]},
                "alt": "Comparison of loose and tight Google Ads ad group structure for a Houston plumbing company and its Quality Score",
                "caption": "Group keywords so one set of headlines honestly answers all of them.",
            },
            "landing": {
                "type": "checklist",
                "title": "Landing page checks for a better score",
                "sub": "Run these on every page your ads send traffic to",
                "items": ["Headline repeats the ad’s promise and service", "Town or service area named near the top", "Tap-to-call phone number above the fold", "Short form, three to five fields", "Reviews and license info visible", "Loads fast on a phone over cellular", "No pop-ups covering the content", "One clear action, minimal navigation"],
                "alt": "Checklist for Google Ads landing page experience and Quality Score for businesses in Houston and The Woodlands",
                "caption": f"Based on {SRC['opt']}, plus what we see in local accounts.",
            },
            "plan": {
                "type": "steps",
                "title": "30 days to a better Quality Score",
                "sub": "Start with the keywords that spend the most",
                "steps": [["Days 1-3: Diagnose", "Add QS columns, sort by cost, note weak components."], ["Days 4-10: Regroup", "Split loose ad groups, write themed RSAs, add negatives."], ["Days 11-20: Pages", "Matched landing pages, mobile speed, tappable phone."], ["Days 21-30: Measure", "Compare QS (hist.), CPC and cost per lead."]],
                "alt": "Four-step 30-day plan to improve Google Ads Quality Score and lower CPC for a business in The Woodlands or Houston",
                "caption": "Fix the expensive keywords first. Low-spend keywords can wait.",
            },
        },
    },
]
