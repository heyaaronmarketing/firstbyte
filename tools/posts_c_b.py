"""One trust post: Google business listing scam calls, what Google really does by phone, and how to stop them.

Research: top results for "google business listing scam calls" (LocaliQ, Hiya, assorted thin posts) plus PAA-style
variants; facts verified against Google Business Profile Help (fraudulent calls/texts page 6212928, profile
protection 14509283, verification 7107242, owners & managers 3403100, review extortion 16404809), Google's Keyword
blog and The Record on the 2022 G Verifier lawsuit, Hiya's Scam of the Month (Aug 2023), FTC (Do Not Call FAQs,
impersonation rule press release, June 2026 imposter-scam data, call blocking, what to do if scammed), Hunton on
the 2024 TSR business-to-business amendment, Search Engine Land and Search Engine Roundtable, and the Texas
Attorney General complaint page.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "gcalls": A("https://support.google.com/business/answer/6212928?hl=en", "Google’s help page on fraudulent calls and texts"),
    "gprotect": A("https://support.google.com/business/answer/14509283?hl=en", "Google’s profile protection guidance"),
    "gverify": A("https://support.google.com/business/answer/7107242?hl=en", "Google’s verification help page"),
    "gusers": A("https://support.google.com/business/answer/3403100?hl=en", "Google’s owners and managers help page"),
    "gextort": A("https://support.google.com/business/answer/16404809?hl=en", "Google’s review extortion report page"),
    "gblog": A("https://blog.google/technology/safety-security/protecting-small-businesses-from-scammers/", "Google’s own announcement"),
    "record": A("https://therecord.media/google-files-lawsuit-accusing-g-verifier-scammers-of-impersonating-company/", "The Record"),
    "hiya": A("https://blog.hiya.com/scam-of-the-month-google-business-profile-scam", "Hiya"),
    "dnc": A("https://consumer.ftc.gov/articles/national-do-not-call-registry-faqs", "FTC’s Do Not Call FAQ"),
    "tsr": A("https://www.hunton.com/insights/legal/telemarketing-sales-rule-changes-remove-exception-for-business-to-business-calls-and-impose-new-recordkeeping-requirements", "Hunton’s summary of the 2024 rule change"),
    "ftc26": A("https://ftc.gov/news-events/news/press-releases/2026/06/ftc-data-show-people-reported-losing-3-point-5-billion-imposter-scams-2025", "FTC data released in June 2026"),
    "ftcblock": A("https://consumer.ftc.gov/articles/how-block-unwanted-calls", "FTC’s call-blocking guide"),
    "ftcscammed": A("https://consumer.ftc.gov/articles/what-do-if-you-were-scammed", "FTC’s “what to do if you were scammed” page"),
    "sel": A("https://searchengineland.com/with-negative-review-extortion-scams-on-the-rise-use-googles-report-form-464515", "Search Engine Land"),
    "verified": A("https://seroundtable.com/google-verified-local-service-ads-badge-39975.html", "Search Engine Roundtable"),
    "lsa": A("https://support.google.com/localservices/answer/6224841?hl=en", "Google’s Local Services Ads page"),
    "txag": A("https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint", "Texas Attorney General’s complaint page"),
}

POSTS = [
    {
        "slug": "google-business-listing-scam-calls",
        "title": "Google Business Listing Scam Calls: What Google Really Does",
        "seo_title": "Google Business Listing Scam Calls: How to Stop Them",
        "desc": "Getting Google business listing scam calls? What Google really does by phone, the scripts to hang up on, how to stop them, and what to do if you paid.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google", "Google Ads"],
        "art": "b2",
        "hero": "phone",
        "hero_alt": "Illustration of a ringing smartphone with a blocked call symbol for a guide to Google business listing scam calls",
        "related": ["google-business-profile-number-one-asset", "google-business-profile-suspended-reinstatement", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Almost every Google business listing scam call follows the same pattern: a recorded voice says your listing is unverified, about to be removed, or “needs attention,” and asks you to press 1. Google doesn’t make that call. Your Business Profile is free, Google won’t threaten to remove it over a fee, and per {SRC['gcalls']}, Google never asks for payment information over the phone.</p>
<p>What makes this confusing is that Google really does call businesses sometimes. So it helps to know what a legitimate call sounds like, which scripts to hang up on, and what to do if someone on your team already gave out a card number or a code. If you only have a minute, skip to the profile health check near the bottom and run it today.</p>
"""),
            ("Does Google call you about your business listing?", f"""<p>Sometimes, but the real calls are narrow, boring and never about money. According to {SRC['gcalls']}, Google’s calls fall into a few buckets:</p>
<ul>
<li><b>Automated fact-check calls.</b> A recorded system calls to confirm details for Maps: your hours, whether you take reservations, prices or availability. These only go to businesses that list a public phone number. The call says it’s from Google, says why it’s calling, and says it’s being recorded.</li>
<li><b>Calls on behalf of a customer.</b> Google’s automated system can call to book a reservation or appointment for someone.</li>
<li><b>Calls from a person.</b> Some calls come from a live Google operator, and Google staff may call about Google Ads or other Google accounts. If you opened a support ticket or work with an Ads rep, expect a callback.</li>
<li><b>Verification calls you requested.</b> You press “Get verified” first, then the code arrives. Covered in detail below.</li>
</ul>
<p>Google also publishes what it never does on a call: ask for payment details, ask you to sign up for a service or pay money, guarantee you a special spot in its products, or ask for private or sensitive information. Google’s {SRC['gprotect']} adds that it won’t charge you to maintain, verify or reinstate a profile, and it never asks for a one-time password or PIN.</p>
<div class="bp-tbl"><table>
<thead><tr><th>What the caller says or asks</th><th>Real Google?</th></tr></thead>
<tbody>
<tr><td>“Are you open until 6 on Saturdays?” (recorded, says it’s Google and recorded)</td><td>Possibly real. No money or codes involved.</td></tr>
<tr><td>A callback from support about a ticket you opened</td><td>Real, if you opened one. Verify in your account.</td></tr>
<tr><td>“Your listing will be removed unless you verify today”</td><td>No.</td></tr>
<tr><td>“Press 1 to speak to a listing specialist”</td><td>No.</td></tr>
<tr><td>“Read me the code we just texted you”</td><td>No. Google says it will never ask for your code.</td></tr>
<tr><td>“We can get you to the top of Maps for $299”</td><td>No. Google doesn’t sell rankings.</td></tr>
</tbody></table></div>
"""),
            ("Why do I keep getting calls about my Google Business listing?", f"""<p>Because your number is public, and that’s the whole point of a listing. A typical Business Profile shows a name, a category, a city and a phone number. Anyone can scrape that, and lists of “businesses with a Google listing” are cheap to build. For a home-service company in Spring or Magnolia, that public number is often the owner’s own cell phone, which is why these calls feel so personal.</p>
<p>The scale is real. {SRC['hiya']}, a call-screening company, said in 2023 that its honeypot numbers had caught more than 17,000 of these robocalls in a few months, logged more than 100 script variations, and received over 2,000 user reports a month. Some of the people reporting them don’t own a business at all, which suggests a lot of the dialing is random. Hiya also logged one caller asking $399 to “verify” a business.</p>
<!--fig:scale-->
<p>It also pays. In 2022 Google sued a company operating as “G Verifier.” Per {SRC['record']}, victims were told they had to pay $99 or their account would be suspended, and some were told they’d lose their five-star reviews. Google said “hundreds and hundreds” of merchants had complained. In {SRC['gblog']}, Google said it was suing scammers who tried to charge people for profiles Google provides for free.</p>
<p>Business impersonation is a big category across the board. The {SRC['ftc26']} show people reported losing nearly $1 billion to business impersonators in 2025, out of $3.5 billion lost to imposter scams overall.</p>
<p>Pressing 9 to “opt out” doesn’t help either. Google’s own guidance is to hang up without pressing anything, because pressing buttons can lead to more of these calls. Our guess is that any response tells the dialer a human picked up.</p>"""),
            ("The scripts you’ll hear, and what each one is after", f"""<p>The wording changes weekly. The goals don’t.</p>
<div class="bp-tbl"><table>
<thead><tr><th>The script</th><th>What they actually want</th></tr></thead>
<tbody>
<tr><td>“Your Google listing will be removed / suspended”</td><td>A “verification” or “renewal” fee, often $99 to $399 in reported cases.</td></tr>
<tr><td>“Your business is not verified with Google” or “has not been registered”</td><td>Your verification code, so they can claim or take over the profile.</td></tr>
<tr><td>“Press 1 to update your listing so customers can find you”</td><td>A live transfer to a salesperson selling listing or SEO packages.</td></tr>
<tr><td>“We’re a Google partner and can get you to the top of Maps”</td><td>A monthly contract for rankings no one can promise.</td></tr>
<tr><td>“You qualify for the Google Guaranteed badge”</td><td>An upfront fee for something you can apply for yourself.</td></tr>
<tr><td>“We can remove your bad reviews” or “add 50 five-star reviews”</td><td>Money for fake reviews, which can get your profile penalized.</td></tr>
<tr><td>A message that one-star reviews will stop if you pay</td><td>Extortion. Report it, don’t pay.</td></tr>
</tbody></table></div>
<h3>The “Google Guaranteed” pitch is out of date on its face</h3>
<p>Google retired the Google Guaranteed, Google Screened and License Verified badges and moved to a single “Google Verified” badge on October 20, 2025, according to {SRC['verified']}. Anyone still selling “Google Guaranteed” in 2026 is reading an old script. The real program is Local Services Ads, which you sign up for yourself. {SRC['lsa']} describes it as pay-per-lead: you pay when a customer contacts you through the ad, not for the badge. If you’re weighing it, our <a href="/blog/local-services-ads-vs-google-ads-home-services/">Local Services Ads vs Google Ads breakdown</a> covers the actual costs.</p>
<h3>Review removal and review extortion</h3>
<p>One version is a sales call offering to delete bad reviews or add good ones. Nobody outside Google can delete a review, and bought reviews break Google’s policies and federal rules (see our post on <a href="/blog/fake-reviews-rule-local-businesses/">the FTC’s fake reviews rule</a>).</p>
<p>The nastier version: a sudden pile of one- and two-star reviews, then a WhatsApp message or email demanding money to stop. Google launched a dedicated report form for this in fall 2025, per {SRC['sel']}. {SRC['gextort']} says don’t pay, don’t engage, collect screenshots, and report. Paying guarantees nothing and invites another round.</p>"""),
            ("Calls to verify my Google listing: how real verification works", f"""<p>This script catches careful people, because verification is real. The difference is who starts it.</p>
<p>Per {SRC['gverify']}, verification methods include phone or text, email, a live video call, a recorded video and, for some businesses, a postcard. Google decides which options you get. If phone or text is offered, <i>you</i> select “Get verified” inside your profile, then the call or text arrives with a code, and <i>you</i> type that code into your profile. Google’s page is blunt about it: “Google will never ask for your verification code,” and you shouldn’t share it with anyone, including people who manage your profile.</p>
<p>So if your phone rings with a code you didn’t request, and then someone calls asking you to read it back, that’s a takeover attempt. Somebody else just started verification on your business and needs the code to finish. Don’t read it to them. Go to business.google.com yourself and check who has access (steps below).</p>
<!--fig:realfake-->
<p>Tape this next to the office phone: a person asking for a code is never Google.</p>"""),
            ("How to stop Google business listing scam calls", f"""<p>You won’t get them to zero. You can get them down to a few a week and make sure none of them costs you anything.</p>
<h3>Know what the Do Not Call Registry won’t do</h3>
<p>Most owners try this first. The {SRC['dnc']} is clear: “The Registry is for personal phone numbers. Business phone numbers and fax lines are not covered.” If your business line is listed on Google, registering it won’t do much. If the number on your profile is also your personal cell, you can register it, though scammers ignore the list anyway.</p>
<p>Two things do help you legally. The FTC says a robocall selling something without your written permission is illegal and probably a scam, registry or no registry. And as of 2024, the FTC’s Telemarketing Sales Rule bans misrepresentations and false statements on business-to-business calls too, per {SRC['tsr']}. That’s why your reports are worth filing.</p>
<h3>Turn on blocking and labeling</h3>
<ul>
<li><b>Carrier tools.</b> Call your carrier or check its app for spam labeling and blocking. The {SRC['ftcblock']} notes some are free and some cost extra.</li>
<li><b>Phone settings.</b> iPhone has Silence Unknown Callers and Android has caller ID and spam protection in the Phone app. Careful: on a business line these can bury real customer calls. We’d use labeling over hard blocking on any number customers dial.</li>
<li><b>VoIP and office lines.</b> Most business VoIP systems have spam filters and block lists in the admin panel.</li>
</ul>
<h3>Change how you answer</h3>
<p>Hang up without pressing anything, including the “opt out” option. Don’t call back numbers from voicemails. If a caller claims to be Google support, ask for their name, hang up, and contact support through your Business Profile instead.</p>
<h3>Consider what number is on your profile</h3>
<p>If your cell is the public number, a separate business line (a VoIP line, or a call-tracking number that forwards to you) lets you screen differently on that line and keeps your personal phone out of scraped lists. It also shows which calls came from Google. We explain the setup in <a href="/blog/call-tracking-which-ads-make-phone-ring/">our call tracking guide</a>.</p>
<p>And if you’d like the real Google automated calls to stop too, Google says you can opt out by saying so on the call.</p>"""),
            ("How to report them: Google, the FTC, the FCC and the Texas AG", f"""<p>Reporting takes five minutes. Note the number, time, company name used and what they asked for first.</p>
<ol>
<li><b>Google.</b> {SRC['gcalls']} links to a form to report a violation of Business Profile third-party policies. Include the caller’s company name, contact details and any emails or invoices.</li>
<li><b>FTC.</b> Report unwanted calls at donotcall.gov or 1-888-382-1222, and fraud (especially if you lost money) at ReportFraud.ftc.gov.</li>
<li><b>FCC.</b> File an informal complaint at fcc.gov/complaints, especially for spoofed or repeat robocalls.</li>
<li><b>Spam texts.</b> Forward them to 7726 (SPAM).</li>
<li><b>Texas Attorney General.</b> The {SRC['txag']} takes complaints online. Your reference number doesn’t mean an investigation has opened, and complaints are public under Texas law, so leave out account numbers and IDs.</li>
</ol>
"""),
            ("Already paid or gave them access? Do this today", f"""<p>This catches careful people too. Picture a Conroe roofer answering between jobs on a 100-degree August afternoon, hearing that his listing will disappear right before hurricane season. Card number given, call over in two minutes. If that was you or someone on your crew, work through this in order.</p>
<!--fig:paid-->
<p>For the money: the {SRC['ftcscammed']} says to contact your card issuer or bank right away using the number on the back of the card and ask for a refund. Bank transfers, Zelle, gift cards and wires are harder to reverse, so call the same day.</p>
<p>For the profile: go to business.google.com, choose <b>More</b>, then <b>Business Profile settings</b>, then <b>People and access</b>. Per {SRC['gusers']}, only owners can remove other users, and new owners or managers have to wait 7 days before they can remove other people or transfer primary ownership. That waiting period works in your favor if you move fast. Remove anyone you don’t recognize, then check your name, phone number, website link and hours for edits you didn’t make.</p>
<p>If you’ve lost access, or the profile got suspended after someone’s edits, our walkthrough on <a href="/blog/google-business-profile-suspended-reinstatement/">getting a suspended Google Business Profile reinstated</a> covers the appeal process.</p>"""),
            ("A 10-minute Google Business Profile health check", f"""<p>Almost everything scam callers threaten, you can check yourself in about ten minutes. Do it once a quarter.</p>
<!--fig:check-->
<ol>
<li>Search your business name on Google and Maps. If you see your profile and the edit options, it’s claimed and you’re signed in to the right account.</li>
<li>Look for a “Verified” status in your profile dashboard. If Google wants something, it will say so there, not in a robocall.</li>
<li>Open People and access. You should recognize every owner and manager. One owner should be you, on an account you control (not a former employee’s or an old agency’s).</li>
<li>Check the phone number, website link and address. Hijackers often swap just the phone or website.</li>
<li>Read reviews from the last 30 days. A sudden cluster of one-stars from strangers is the extortion pattern; report it.</li>
<li>Check that 2-Step Verification is on for the Google account that owns the profile.</li>
</ol>
<p>Your profile likely brings in more calls than your website, as we argue in <a href="/blog/google-business-profile-number-one-asset/">why your Google Business Profile is your number one asset</a>. For review habits that hold up, see our <a href="/blog/complete-guide-google-reviews/">complete guide to Google reviews</a>.</p>"""),
            ("What legitimate help looks like", f"""<p>Your next step is the health check above. Put it on the calendar for the first Monday of each quarter and have whoever answers your phones read this page once.</p>
<p>If you run it and something looks wrong, like a manager you don’t recognize or a phone number you never entered, <a href="/contact/">tell us what you found</a> and we’ll say plainly what we’d do. We’re a local agency in The Woodlands, so you can look us up before you reply to anything. Any legitimate agency works the same way: you add them as a manager from your own account, you can remove them any time, and nobody ever needs your verification code or password to help.</p>
<p>The same goes for our free <a href="/contact/">Ad Spend Leak Check</a>, for owners who also run Google or Meta ads. It only happens if you request it, and what comes back is a 10-minute recorded video of what we found in the account. What you do with it is up to you. Ongoing profile upkeep sits with our <a href="/services/web-design-seo-pr/">SEO team</a>.</p>"""),
        ],
        "faq": [
            ("How do I stop Google business listing robocalls?",
             "You can reduce them but rarely stop them completely. Turn on your carrier’s spam labeling, use your phone’s screening tools carefully on business lines, never press a button on a robocall, and hang up. Report repeat callers to Google, the FTC at donotcall.gov or ReportFraud.ftc.gov, and the FCC. Moving your public profile number to a separate business or call-tracking line also keeps your personal cell off scraped lists."),
            ("Can I put my business phone number on the Do Not Call Registry?",
             "The FTC says the registry is for personal phone numbers and that business lines are not covered. If your profile lists your personal cell, you can register it, though scammers ignore the list. Robocalls that sell something without your written permission are illegal either way, and since 2024 federal telemarketing rules also ban lies on business-to-business sales calls, so reporting still matters."),
            ("What happens if I pressed 1 on a Google listing call?",
             "Usually you were transferred to a salesperson, and your number was marked as one a live person answers, so expect more calls. Pressing 1 alone doesn’t give anyone access to your profile. The damage comes from what you shared after that. If you gave a card number, call your card issuer today. If you read out a verification code, check People and access in your Business Profile and remove anyone you don’t know."),
            ("Does Google charge to verify or keep a Business Profile?",
             "No. Google Business Profiles are free to create, verify and keep. Google’s help center says it won’t ask you to pay to maintain, verify or reinstate a profile, and it never asks for payment details over the phone. Anyone charging a renewal fee, a verification fee or a fee to stop your listing from being removed is not Google, even if they use Google’s name or logo."),
            ("Is the call real if they know my business name and address?",
             "Not necessarily. Your business name, address, category and phone number are all public on your listing, so any caller can read them off Google in seconds. Knowing your details proves nothing. Judge the call by what it asks for. A request for money, a code, a password, or a quick decision means hang up, then check your profile yourself at business.google.com."),
        ],
        "figures": {
            "scale": {
                "type": "stats",
                "title": "How big the fake Google call problem is",
                "stats": [
                    ["17K+", "robocalls caught by Hiya honeypots in a few months"],
                    ["100+", "script variations Hiya recorded"],
                    ["2K+", "user reports a month to Hiya"],
                    ["$1B", "lost to business impersonators in 2025 (FTC)"],
                ],
                "note": "Source: Hiya Scam of the Month (2023); FTC (June 2026)",
                "alt": "Stat tiles on the volume of Google business listing scam calls and business impersonation losses reported to the FTC",
                "caption": "These calls are mass-dialed, which is why owners in Houston and everywhere else get them on repeat.",
            },
            "realfake": {
                "type": "compare",
                "title": "Scam caller vs real Google contact",
                "left": {"title": "Scam caller", "items": [
                    "Calls out of the blue about removal or suspension",
                    "Asks you to press 1 or read back a code",
                    "Wants a card number or a fee",
                    "Promises top rankings or review removal",
                    "Pushes you to act today",
                ]},
                "right": {"title": "Real Google", "items": [
                    "Confirms hours or prices, says it’s recorded",
                    "Sends codes only after you click Get verified",
                    "Never asks for payment by phone",
                    "Shows profile issues in your dashboard",
                ]},
                "alt": "Comparison of Google business listing scam call tactics against how real Google verification and calls work",
                "caption": "If a human voice asks for a code or a card number, it isn’t Google.",
            },
            "paid": {
                "type": "steps",
                "title": "Already paid or shared access? Fix it today",
                "sub": "Work top to bottom, same day if you can",
                "steps": [
                    ["Call your card issuer or bank", "Use the number on the back of the card, report fraud and ask for a refund or dispute."],
                    ["Remove unknown users", "Business Profile settings, then People and access. Remove anyone you don’t recognize."],
                    ["Check what changed", "Phone, website, address, hours and category. Fix any edit you didn’t make."],
                    ["Lock the account", "New Google password, then turn on 2-Step Verification."],
                    ["Report it", "Google’s third-party policy form, ReportFraud.ftc.gov and the Texas AG."],
                ],
                "alt": "Five steps for business owners who paid a Google business listing scam caller or shared profile access",
                "caption": "New owners must wait 7 days before removing others, so moving quickly keeps you in control.",
            },
            "check": {
                "type": "checklist",
                "title": "10-minute Business Profile health check",
                "sub": "Free, no phone call required, once a quarter",
                "items": [
                    "Profile shows edit options when you search your name",
                    "Dashboard shows the profile as verified",
                    "You recognize every owner and manager",
                    "You are an owner on an account you control",
                    "Phone, website and address are correct",
                    "No unexplained spike of one-star reviews",
                    "2-Step Verification is on for the owner account",
                ],
                "alt": "Checklist for a Google Business Profile health check that answers most scam call threats for Woodlands businesses",
                "caption": "Everything a scam caller threatens about, you can confirm yourself in a few minutes.",
            },
        },
    },
]
