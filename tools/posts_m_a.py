"""Batch 13: problem-driven posts. Meta ad account disabled or restricted, and Google Ads account suspended.

Research, Meta post: Meta Business Help Center article titles and URLs (Troubleshoot a disabled or restricted account;
Request a review if you are restricted from advertising on Meta platforms; My Facebook Account, Page, or Business Manager
Account has Advertising Restrictions; Troubleshoot a Disabled Ad Account Due to Payment Failure; Troubleshoot
Unrecognized Activity on Your Ad Account; Verify Your Business in Meta Business Suite; Best Practices for Preventing
Payment Failures). facebook.com blocks automated fetching (robots), so page text was verified through a mirror of
Meta's help content (About Meta Business Support Home; Best practices for making a business portfolio more secure;
Turn on the two-factor authentication requirement; About business verification) and two vendor guides that quote Meta's
review guidance (Leadsie, Oct 2026; AdsInfra, Aug/Oct 2026: "most cases reviewed within 48 hours"). Also: Meta
newsroom on video-selfie recovery (Oct 2024, Mar 2025 UK/EU/South Korea) and the Feb 2023 penalty-system change;
TechCrunch on the Oversight Board's June 2026 account-disable findings; WSMV on Meta's March 2026 support hub; Jon
Loomer on an "unusual activity" restriction and failed ID check, and on Daily Spending Limits; Search Engine Land on
the FT report about high-spender moderation guardrails (Meta disputes it); KPRC Click2Houston (July 2021) on a Houston
boutique's hijacked business page.
Research, Google post: Google Ads Help (account suspensions overview 9841640; billing and payment suspensions 13704200;
ads paused for suspicious payment activity 16204275; account pausing 9872152; advertiser verification 9703665 and its
timelines 15588490; repeat-violation strikes 10922738; Circumventing systems 15938075 and the Nov 4, 2025 update
16698137; Unacceptable business practices 15938071; Misrepresentation 6020955). TechCrunch on Google's 2025 Ads Safety
Report (8.3B ads blocked, 3.3M US advertiser accounts suspended, Google's claim of 80% fewer incorrect suspensions);
Search Engine Roundtable on the 2024 report (39.2M accounts); Harris County's business roadmap on assumed-name filings.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # Meta post
    "m_troubleshoot": A("https://www.facebook.com/business/help/422289316306981", "Troubleshoot a disabled or restricted account"),
    "m_review": A("https://www.facebook.com/business/help/530209463124901", "Request a review if you are restricted from advertising"),
    "m_restrict": A("https://www.facebook.com/business/help/975570072950669", "advertising restrictions help page"),
    "m_payfail": A("https://www.facebook.com/business/help/268196136699959", "Troubleshoot a Disabled Ad Account Due to Payment Failure"),
    "m_payprevent": A("https://www.facebook.com/business/help/2726198024366416", "Best Practices for Preventing Payment Failures"),
    "m_unrec": A("https://www.facebook.com/business/help/524424920973484", "Troubleshoot Unrecognized Activity on Your Ad Account"),
    "m_verify": A("https://www.facebook.com/business/help/2058515294227817", "Verify Your Business in Meta Business Suite"),
    "m_bsh": A("https://business.facebook.com/business-support-home", "Meta’s Business Support Home"),
    "m_secure": A("https://www.facebook.com/business/help", "Meta’s Business Help Center (business portfolio security)"),
    "m_2fa": A("https://www.facebook.com/business/help", "Meta’s Business Help Center (two-factor authentication requirement)"),
    "m_bv": A("https://www.facebook.com/business/help", "Meta’s Business Help Center (business verification)"),
    "leadsie": A("https://www.leadsie.com/blog/recover-disabled-facebook-ad-account", "Leadsie’s recovery guide"),
    "adsinfra": A("https://adsinfra.io/guides/meta-ad-account-restricted", "AdsInfra’s restriction guide"),
    "selfie": A("https://about.fb.com/news/2024/10/testing-combat-scams-restore-compromised-accounts/", "Meta’s newsroom"),
    "penalty": A("https://about.fb.com/news/2023/02/meta-is-improving-facebooks-penalty-system/", "changed its penalty system in 2023"),
    "oversight": A("https://techcrunch.com/2026/06/04/metas-oversight-board-says-account-bans-lack-due-process-transparency/", "TechCrunch"),
    "hub": A("https://www.wsmv.com/2026/03/06/facebook-account-disabled-meta-is-rolling-out-new-support-hub-locked-out-users/", "reported in March 2026"),
    "loomer_id": A("https://www.jonloomer.com/qvt/meta-restricted-my-account/", "Jon Loomer described"),
    "loomer_dsl": A("https://www.jonloomer.com/glossary/daily-spending-limit/", "Daily Spending Limit"),
    "sel_ft": A("https://searchengineland.com/meta-special-content-moderation-treatment-top-advertisers-450316", "Search Engine Land’s summary of a Financial Times report"),
    "kprc": A("https://www.click2houston.com/news/local/2021/07/29/houston-woman-says-her-facebook-business-page-was-hijacked-moments-after-it-launched", "told KPRC Click2Houston"),
    # Google post
    "g_over": A("https://support.google.com/google-ads/answer/9841640", "Google Ads account suspensions overview"),
    "g_bill": A("https://support.google.com/google-ads/answer/13704200", "billing and payment suspensions page"),
    "g_susp": A("https://support.google.com/adspolicy/answer/16204275", "Ads paused for suspicious payment activity"),
    "g_pause": A("https://support.google.com/adspolicy/answer/9872152", "account pausing page"),
    "g_verif": A("https://support.google.com/adspolicy/answer/9703665", "advertiser verification page"),
    "g_vtime": A("https://support.google.com/adspolicy/answer/15588490", "verification timelines page"),
    "g_strike": A("https://support.google.com/adspolicy/answer/10922738", "strike system"),
    "g_circ": A("https://support.google.com/adspolicy/answer/15938075", "Circumventing systems policy"),
    "g_nov25": A("https://support.google.com/adspolicy/answer/16698137", "a November 4, 2025 update"),
    "g_ubp": A("https://support.google.com/adspolicy/answer/15938071", "Unacceptable business practices policy"),
    "g_misrep": A("https://support.google.com/adspolicy/answer/6020955", "Misrepresentation policy"),
    "g_comp": A("https://support.google.com/google-ads/contact/compromised_account", "compromised account form"),
    "tc_safety": A("https://www.techcrunch.com/2026/04/16/google-blocked-more-ads-but-banned-fewer-advertisers-as-ai-reshapes-enforcement/", "TechCrunch’s coverage of Google’s 2025 Ads Safety Report"),
    "ser_2024": A("https://www.seroundtable.com/blog/google-ads-safety-report-39242.html", "Search Engine Roundtable"),
    "harris": A("https://hcoed.harriscountytx.gov/docs/BusinessRoadMap/HarrisCounty_Roadmap_HowToStartABusiness_2025.pdf", "Harris County’s business roadmap"),
}

META = "/blog/meta-ad-account-disabled-restricted-fix/"
GOOG = "/blog/google-ads-account-suspended-fix/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: Meta
    {
        "slug": "meta-ad-account-disabled-restricted-fix",
        "title": "Meta Ad Account Disabled or Restricted: How to Get It Back",
        "seo_title": "Meta Ad Account Disabled or Restricted? How to Get It Back",
        "desc": "Meta ad account disabled or restricted? Find what was hit in Business Support Home, request a review the right way, fix payment flags and prevent a repeat.",
        "category": "Paid social",
        "icons": ["Meta", "Facebook", "Instagram"],
        "art": "b1",
        "hero": "shield",
        "hero_alt": "Illustration of a shield for recovering a disabled or restricted Meta ad account in Houston and The Woodlands",
        "related": ["facebook-lead-ads-bad-leads-fix-quality", "facebook-instagram-ads-local-businesses", "google-business-profile-suspended-reinstatement"],
        "sections": [
            (None, f"""<p>First week of July, 7:40 a.m. An AC company in Spring has its tune-up campaign queued for the heat wave the forecast has been promising all weekend. The owner opens Ads Manager and gets a red banner instead: “Your ad account has been disabled. We noticed unusual activity.” Nobody on the team changed anything. Leads stop by lunch.</p>
<p>We get some version of that call every few weeks from business owners around The Woodlands and Houston. The panic is understandable, and it pushes people to do the two things that make it worse: firing off a pile of appeals, or opening a brand-new account the same afternoon.</p>
<p>To get a disabled or restricted Meta ad account back, find out exactly which asset was restricted (ad account, Page, personal profile or business portfolio) in Meta Business Support Home, read the stated reason, then fix anything you can fix: clear a failed payment, secure a compromised login, complete identity or business verification. Then request one review from an admin, write it plainly, and wait. Most restrictions that come from payment hiccups, security flags or mistaken policy calls can be reversed. Some can’t, and it helps to know which kind you have before you spend a week on it.</p>"""),

            ("First, figure out what actually got restricted", f"""<p>Meta uses “disabled” and “restricted” for several different things, and the fix depends on which layer got hit. People lose days appealing an ad account when the real problem is the personal profile of the person who runs it.</p>
<div class="bp-tbl"><table>
<thead><tr><th>What’s restricted</th><th>What it usually looks like</th><th>What it affects</th><th>Who has to act</th></tr></thead>
<tbody>
<tr><td>Ad account</td><td>“Ad account disabled” banner in Ads Manager; campaigns stop</td><td>That one ad account and its campaigns</td><td>An admin on the ad account or its business portfolio</td></tr>
<tr><td>Facebook Page</td><td>Page can’t run ads or boost posts; ads from that Page get rejected</td><td>Every ad account that runs ads from that Page</td><td>A Page admin</td></tr>
<tr><td>Personal profile (your Facebook account)</td><td>“You’re restricted from advertising” when you open any ad tool</td><td>Your ability to create or manage ads anywhere, including client accounts</td><td>You, from your own profile</td></tr>
<tr><td>Business portfolio (formerly Business Manager)</td><td>Portfolio shows as disabled or restricted; assets inside go dark together</td><td>All ad accounts, Pages, catalogs and shops the portfolio owns</td><td>A person with full control of the portfolio</td></tr>
</tbody></table></div>
<p>Meta’s own help center has separate articles for these: {SRC['m_troubleshoot']}, plus a {SRC['m_restrict']} that covers a Facebook account, Page or Business Manager account with advertising restrictions. Meta’s documentation says the business portfolio’s status affects the ad accounts and assets it owns, and your personal Facebook account’s status affects your personal ad account and your access to some advertising tools, per {SRC['m_bsh']}.</p>
<p>Restrictions also come in degrees. Guides that quote Meta’s restriction page list four levels: a daily spend limit or lower payment threshold, loss of some payment features, loss of some advertising features, and losing the ability to advertise at all (see {SRC['adsinfra']} and {SRC['leadsie']}). A spend cap is annoying. A full disable is a different conversation.</p>"""),

            ("Where to look: Business Support Home (the old Account Quality)", f"""<p>Meta Business Support Home is the dashboard for all of this, at facebook.com/business-support-home. Older guides, and a few menus, still call it Account Quality. Per {SRC['m_bsh']}, it shows the status of your business portfolios, ad accounts, commerce accounts, catalogs and Pages, whether any of them are disabled or restricted, rejected ads, and your feedback score.</p>
<p>The path we use every time:</p>
<!--fig:triage-->
<p>Two notes from doing this a lot. Set the date range (top right, 14, 30 or 90 days) to 90, because the restriction that matters sometimes started weeks ago as a small rejected-ad pattern. And screenshot everything: the reason text, the asset ID, the date. Meta’s wording can change after a review starts, and you’ll want the original.</p>
<p>Business Support Home also matters for a less obvious reason. Scammers send fake “your Page will be disabled” emails and Messenger notes constantly, with a link to an appeal form that steals your login. Meta’s documentation says to check the account overview in Business Support Home to confirm a warning is real before you act on it. If the warning isn’t there, it isn’t real.</p>"""),

            ("Reading the reason: unusual activity, policy, payment or identity", f"""<p>The reason line usually falls into one of four buckets, and each wants a different first move.</p>
<p><b>“Unusual activity” or “integrity” flags.</b> This is Meta’s systems deciding something about the account looks like fraud, a takeover or automation. A new device or location for an admin, a sudden jump in spend, a payment method that was recently used somewhere Meta didn’t like, or a pile of new users added in one day can all trigger it. {SRC['loomer_id']} getting “Certain actions have been restricted due to unusual activity” on his own profile after sharing a link to Meta’s documentation in his group, followed by a driver’s-license check that failed with no reason given. If it can happen to one of the best-known Meta ads educators, it can happen to a roofer in Conroe.</p>
<p><b>Policy (Advertising Standards).</b> A run of rejected ads, or one ad Meta treats as severe, can restrict the account. Look at the rejected ads list in Business Support Home for the pattern. Common local-business culprits we see: before-and-after weight loss or skin photos, “are you struggling with…” copy that implies a personal attribute, and housing, employment or credit ads run without the right special ad category.</p>
<p><b>Payment.</b> A declined card, a balance Meta couldn’t collect, or a payment method that was reported. Meta has a dedicated article, {SRC['m_payfail']}, and it’s usually the most fixable bucket.</p>
<p><b>Identity or security.</b> Meta wants an admin to confirm who they are, or thinks a login was compromised. Unrecognized charges or campaigns you didn’t create go to {SRC['m_unrec']} first, before any appeal.</p>"""),

            ("How to request a review, step by step", f"""<p>Meta’s article {SRC['m_review']} is the official version. Here is how the flow works in practice, as also described by {SRC['leadsie']}:</p>
<!--fig:review-->
<p>Only admins can request the review, so if your agency or a former employee was the only admin, that’s problem number one. (Our {L('/blog/who-owns-google-ads-account-switch-agencies/', 'post on who owns your ad accounts')} is about Google, but the same rule applies on Meta: the business should own the portfolio, and the agency should be a partner.)</p>
<p>If there’s a free-text box, keep it short and factual. Something like this:</p>
<blockquote><p>We’re a licensed HVAC contractor in Spring, Texas (business portfolio ID 1234…). Our ad account was disabled on July 2 for unusual activity. On July 1 our office manager logged in from a new laptop and added a second card after our primary card expired. Both cards are in the business’s name. We have turned on two-factor authentication for all admins and removed one former employee. Our ads promote AC repair and maintenance and follow the Advertising Standards. Please review and restore the account.</p></blockquote>
<p>No anger, no “I spend $5,000 a month,” no threats to leave. The reviewer, human or automated, is checking whether the flag was right. Give them the reason it wasn’t.</p>
<p>After a restriction is lifted, campaigns don’t restart by themselves. Go turn them back on in Ads Manager and check that budgets and schedules came back intact.</p>"""),

            ("Identity verification: get it right the first time", f"""<p>Plenty of reviews now start with a “confirm your identity” step, usually in the mobile app, with a photo of a government ID. Retries can be limited, so treat the first attempt carefully.</p>
<ul>
<li>Use the ID that matches the name on the Facebook profile exactly. If your profile says “Mike” and your license says “Michael,” expect trouble. Fix the profile name first if Meta allows it.</li>
<li>Photograph the ID flat, in good light, all four corners visible, no glare from the Texas license’s hologram.</li>
<li>Do it from a device and network you normally use. A hotel Wi-Fi in Cabo or a VPN is the wrong place to prove you’re you (that’s our experience, but it’s consistent).</li>
<li>Expect silence afterward. Jon Loomer’s check failed and he still had no clear path five days later.</li>
</ul>
<p>Meta has been testing video selfies for recovering compromised accounts, matched against your profile photos. Per {SRC['selfie']}, it launched in the UK, EU and South Korea in March 2025, so don’t count on it for a Houston account yet.</p>
<p>Business verification is a separate thing, done for the portfolio in Meta Business Suite’s Security Center. It confirms the business is real and that you’re authorized to act for it. Meta’s {SRC['m_bv']} lists the requirements: a business registered with local authorities, an official business phone number or mailing address, and the ability to receive a code at that number or email (or verify your domain). For a Texas LLC, that means the legal name on your Secretary of State filing, or the assumed name you filed, matching what you type in. Start at {SRC['m_verify']}.</p>"""),

            ("Payment-related disables", f"""<p>These are the most common disables we see for small local advertisers, and the most recoverable. A typical sequence: the card on file expires or a bank’s fraud filter blocks a Meta charge, the balance can’t be collected, ads stop, and a few days later the account flips from “payment failed” to “disabled.”</p>
<ol>
<li>Pay the outstanding balance with a working method, from Billing and payments in Ads Manager or the prompt in Business Support Home.</li>
<li>Call your bank and tell them to stop blocking Meta. Business cards from local banks sometimes flag a burst of ad charges as fraud.</li>
<li>Don’t dispute a legitimate Meta charge with your bank to “get Meta’s attention.” In our experience a chargeback on an active ad account almost always deepens the restriction.</li>
<li>Then request the review, noting the balance is paid.</li>
</ol>
<p>Meta’s {SRC['m_payprevent']} page covers prevention. Our version: one business credit card in the company’s name as primary, a second as backup, both with the same billing name and address, and someone who gets the billing emails and actually reads them.</p>
<p>New accounts have a related issue. Meta applies a {SRC['loomer_dsl']} to new ad accounts, Pages and portfolios that rises with time in good standing, per Jon Loomer. A brand-new account that tries to spend $1,500 on day one looks exactly like a stolen card to Meta’s systems. Ramp up.</p>"""),

            ("What an appeal can and can’t fix", f"""<p>Setting expectations saves a lot of grief.</p>
<!--fig:canfix-->
<p>Meta’s enforcement is heavily automated, and the appeal path isn’t always generous. In June 2026 Meta’s Oversight Board said account disablements lack due process and clear notice, and that even Meta Verified subscribers paying for support weren’t getting meaningful help, per {SRC['oversight']}. Separately, {SRC['sel_ft']} described internal guardrails that routed high spenders’ content to human reviewers. Meta called that reporting inaccurate. Either way, a small local advertiser should assume the first look is automated and write the appeal so it’s easy to approve.</p>"""),

            ("How long Meta reviews take", f"""<p>Meta’s review guidance, as quoted by both {SRC['leadsie']} and {SRC['adsinfra']}, says most cases are reviewed within 48 hours and some take longer. We’d treat 48 hours as the good case. In accounts we’ve helped with, payment and security cases often clear in a few days, and policy cases can take one to three weeks, especially if Meta asks for more information midway.</p>
<!--fig:stats-->
<p>Track the request under Your Support Cases in Business Support Home and answer any follow-up there. A second, third and fourth request doesn’t speed anything up, and review requests can be limited. In March 2026, WSMV {SRC['hub']} that Meta was rolling out a centralized 24/7 support hub on Facebook and Instagram, which may make the chat-with-support route easier to find. If you spend enough to have a Meta rep, this is the moment to use them.</p>
<p>Don’t sit on it either. Third-party guides citing Meta’s help center put the window to request a review at roughly six months, and prepaid funds on an account that stays disabled can be forfeited. Request the review the same week.</p>"""),

            ("Hacked accounts are a separate track", f"""<p>If you see campaigns you didn’t create, charges you don’t recognize, or admins you’ve never heard of, it’s a takeover, and an appeal comes second. Secure the personal Facebook logins of every admin, remove unknown users and partners from the portfolio, remove payment methods you don’t recognize, then follow {SRC['m_unrec']}. Call your card issuer about the fraudulent charges.</p>
<p>This happens to local businesses constantly. A Houston boutique owner {SRC['kprc']} in 2021 that she was locked out of her new business page moments after it launched, with her password and recovery email changed, and that Facebook never responded to her. Most of the takeovers we’ve cleaned up started with one admin clicking a fake “copyright violation” or “Page will be disabled” message.</p>"""),

            ("Backup admins and the setup that prevents most of this", f"""<p>Most of the long, ugly recoveries we’ve seen had one thing in common: a single person held every key. Meta’s {SRC['m_secure']} recommend keeping two people with full control (ideally no more than 10), removing people who haven’t logged in for 90 days, requiring two-factor authentication, and removing users with personal email domains that aren’t tied to the business.</p>
<p>To require 2FA: in Meta Business Suite, go to Settings, then Business portfolio info, scroll to Business options, and use the Two-factor authentication dropdown to require it for admins or everyone. Only people with full control can change it, and Meta says certain portfolios older than 90 days must have it on, per {SRC['m_2fa']}.</p>
<!--fig:prevent-->
<p>Creative matters too. Meta {SRC['penalty']} for personal profiles to give more warnings before restrictions, but ad accounts still accumulate rejected ads, and the pattern counts. Run anything borderline past someone who reads the Advertising Standards for a living before it goes live. Our {L('/blog/facebook-instagram-ads-local-businesses/', 'guide to Facebook and Instagram ads for local businesses')} and {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'post on fixing bad lead ad quality')} show what compliant, working local creative looks like.</p>"""),

            ("When to stop appealing and start fresh", f"""<p>Sometimes the honest answer is that this account is gone. Signs you’re there: the review came back “we’ve reviewed your account and it doesn’t comply,” with no further option; the business portfolio itself is permanently disabled; or the restriction sits on a personal profile that failed identity checks.</p>
<p>Starting fresh legitimately means a new asset under the people and business Meta has no problem with. If an old agency-built ad account was disabled and your own portfolio and profile are clean, creating a new ad account inside your verified portfolio is normal. If the restriction is on you or your business, making a new profile or portfolio to keep advertising is the kind of thing Meta’s Advertising Standards treat as an account integrity problem, and in our experience the new asset gets linked and disabled within days, often taking your Page with it.</p>
<!--fig:causes-->
<p>If Meta is off the table for a while, don’t go dark. Search ads and your Google Business Profile carry most local lead flow anyway. Our {L(GOOG, 'guide to Google Ads suspensions')} covers the other platform’s version of this mess, and {L('/blog/google-business-profile-suspended-reinstatement/', 'this one covers Business Profile suspensions')}.</p>
<p>Our {L('/services/paid-social-advertising/', 'paid social team')} sets up portfolios with the business as owner, backup admins and 2FA from day one, and we’ve walked a fair number of owners through these reviews. If your account is stuck, <a href="/contact/">get in touch</a> and tell us what the banner says.</p>"""),
        ],
        "faq": [
            ("Why was my Meta ad account disabled for unusual activity?",
             "Unusual activity usually means Meta’s systems suspect fraud, a takeover or automation. Common triggers are a login from a new device or location, a sudden spend increase, a new or recently flagged payment method, or many users added at once. Check Business Support Home for the exact reason, secure every admin’s login with two-factor authentication, clear any payment issue, then request one review explaining what changed and why it was legitimate."),
            ("How long does a Meta ad account review take?",
             "Meta’s review guidance says most cases are reviewed within 48 hours and some take longer. In accounts we’ve helped with, payment and security cases often clear within a few days, while policy cases can take one to three weeks, especially if Meta asks for more information. Track the case in Business Support Home under your support cases and avoid submitting duplicate requests, since review requests can be limited."),
            ("Where is Account Quality in Meta now?",
             "Account Quality has been folded into Meta Business Support Home, found at facebook.com/business-support-home. It shows the status of your business portfolios, ad accounts, Pages, catalogs and commerce accounts, any advertising restrictions, rejected ads and your feedback score. Open the Outstanding tab under recent account issues to see current problems and the actions available, including requesting a review."),
            ("Should I create a new ad account if mine is disabled?",
             "Only if the restriction is limited to that ad account and your profile, Page and business portfolio are in good standing. In that case a new ad account in your own verified portfolio is normal. If the restriction is on you or your business, creating new profiles or portfolios to keep advertising is treated as circumvention, and the new assets tend to get linked and disabled, sometimes along with your Page."),
            ("How do I prevent my Meta ad account from being restricted?",
             "Keep two trusted people with full control of the business portfolio, require two-factor authentication, remove inactive users and anyone using a personal email that isn’t tied to the business, and complete business verification. Pay with a business card in the company name and keep a backup card on file. Ramp new accounts up gradually, and review borderline creative against Meta’s Advertising Standards before it runs."),
        ],
        "figures": {
            "triage": {
                "type": "steps",
                "title": "The first 30 minutes after a disable",
                "sub": "Inside Meta Business Support Home",
                "steps": [["Open Business Support Home", "facebook.com/business-support-home, set the range to 90 days."], ["Find the asset", "Recent account issues, Outstanding tab. Ad account, Page, profile or portfolio?"], ["Record the reason", "Screenshot the reason, asset ID and date."], ["Fix what you can", "Pay the balance, secure logins, finish verification."], ["Then request review", "One request, from an admin, with a short factual note."]],
                "alt": "Steps to diagnose a disabled Meta ad account in Business Support Home for Houston and The Woodlands businesses",
                "caption": "Fix first, appeal second. A review of an account with an unpaid balance or open security issue rarely goes well.",
            },
            "review": {
                "type": "steps",
                "title": "Requesting a Meta review",
                "sub": "How the flow typically runs",
                "steps": [["Select the restricted item", "In Business Support Home, under the account overview."], ["What you can do", "Choose Request review if Meta shows it."], ["Complete the prompts", "Identity check, verification or account security steps."], ["Explain briefly", "What happened, what you fixed, what you sell."], ["Track the case", "Your Support Cases; answer follow-ups there."], ["Restart ads", "Lifted restrictions don’t restart campaigns. Turn them on."]],
                "alt": "Step by step process to request a review of a restricted Meta ad account for a Houston area business",
                "caption": "If Request review isn’t showing, waiting won’t make it appear. Look for a required verification or security step first.",
            },
            "canfix": {
                "type": "compare",
                "title": "What a Meta appeal can and can’t fix",
                "left": {"title": "Usually not reversible", "items": ["Repeated or severe policy violations", "Portfolio permanently disabled after review", "Failed identity checks with no retry", "Assets linked to a banned person", "New accounts made to get around a ban"]},
                "right": {"title": "Usually reversible", "items": ["Failed or expired payment, now paid", "Security flag after a new login or device", "Hacked account, now secured", "Ad rejected by mistake, then restriction", "Missing verification, now completed"]},
                "alt": "Comparison of which Meta ad account restrictions can be reversed by appeal for Houston and The Woodlands advertisers",
                "caption": "Based on our experience with local advertisers. Meta doesn’t publish reversal rates.",
            },
            "prevent": {
                "type": "checklist",
                "title": "Meta account protection checklist",
                "sub": "Set this up before you need it",
                "items": ["Business owns the portfolio; agency is a partner", "Two people with full control, 10 or fewer total", "2FA required for everyone (authenticator app)", "Recovery codes saved somewhere offline", "Remove users inactive for 90 days", "Business verification completed", "Business card primary, second card as backup", "Billing emails go to someone who reads them", "New accounts ramp spend gradually", "Borderline ads reviewed before launch"],
                "alt": "Checklist to prevent Meta ad account restrictions for small businesses in Houston and The Woodlands",
                "caption": f"Several items come straight from {SRC['m_secure']}.",
            },
            "causes": {
                "type": "bars",
                "title": "Why Meta ad accounts get disabled",
                "sub": "Share of disabled accounts in one vendor’s data",
                "items": [["Policy violations", 45, "45%"], ["Payment issues", 34, "34%"], ["Compromised accounts", 9, "9%"], ["Inactivity", 7, "7%"]],
                "highlight": [1],
                "note": "Source: Leadsie internal data (vendor figures, not Meta’s)",
                "alt": "Bar chart of reasons Meta ad accounts are disabled, for Houston and The Woodlands business owners",
                "caption": f"From {SRC['leadsie']}. Payment problems are the bucket most small businesses can fix themselves.",
            },
            "stats": {
                "type": "stats",
                "title": "Numbers worth knowing",
                "stats": [["48 hrs", "typical review time Meta cites"], ["2", "people with full control, recommended"], ["90 days", "inactive users to remove"], ["~6 mo", "window to request a review"]],
                "note": "Sources: Meta help content and guides quoting it",
                "alt": "Key numbers for Meta ad account reviews and security for businesses in Houston and The Woodlands",
                "caption": "The six-month figure comes from third-party guides citing Meta. Request your review the same week regardless.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: Google
    {
        "slug": "google-ads-account-suspended-fix",
        "title": "Google Ads Account Suspended: Causes and How to Appeal",
        "seo_title": "Google Ads Account Suspended: Causes and How to Appeal",
        "desc": "Google Ads account suspended? The suspension types, what Google reviews, how to write an appeal that works, linked accounts, timelines and what never to do.",
        "category": "Search marketing",
        "icons": ["Google Ads", "Google", "Google Analytics"],
        "art": "b6",
        "hero": "bolt",
        "hero_alt": "Illustration of a shield for appealing a suspended Google Ads account in Houston and The Woodlands",
        "related": ["google-business-profile-suspended-reinstatement", "who-owns-google-ads-account-switch-agencies", "google-ads-not-converting-clicks-no-calls"],
        "sections": [
            (None, f"""<p>A new dental office in Conroe opens its first Google Ads account on a Monday. The office manager sets it up on her personal Gmail, enters the doctor’s credit card, and launches a campaign pointing at a website that went live Friday. Wednesday morning the email arrives: “Your Google Ads account has been suspended due to a violation of the Circumventing systems policy.” Nobody circumvented anything. They don’t even know what it means.</p>
<p>This is one of the most stressful emails a business owner gets, because the account goes completely dark and the notice says almost nothing useful. We’ve worked a lot of these for businesses around Houston, and most of them were fixable once someone figured out which kind of suspension it was.</p>
<p>When a Google Ads account is suspended, all ads stop everywhere and the account becomes read-only until an appeal succeeds. To appeal, use the Contact Us link in the in-account notice, fix the actual problem first (payment verification, advertiser verification, a misleading website, a linked account), and submit one thorough, honest appeal per suspended account. Don’t open a new account while you wait. Google treats that as multiple account abuse, which is itself a reason for suspension.</p>"""),

            ("What a suspension actually does", f"""<p>Per Google’s {SRC['g_over']}, a suspended account can’t serve ads in any location. You get an in-account notice and an email naming the policy and linking to the appeal. The account goes read-only, but you can still make payments, add a payment method, download tax documents and reports, update security settings, complete advertiser verification, appeal, or cancel and request a refund.</p>
<p>Two lines on that page deserve a slow read. A suspension “is considered permanent” unless an appeal succeeds. And you have at least six months from the suspension date to appeal, which is plenty of time to do it right instead of fast. Suspended accounts may become inaccessible after an extended period, so don’t leave it a year.</p>
<p>Suspended is also different from paused. Google’s {SRC['g_pause']} says an account can be paused for failed or missed verification, a brief investigation, or being linked to a manager account that breaks the third-party policy. Paused accounts can’t run ads either, but a pause usually lifts once you finish the task. Read the notice for which word it uses.</p>"""),

            ("The suspension types, and what Google reviews for each", f"""<p>Google groups suspensions into a few families. The table is our summary of the official pages.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Type</th><th>Examples</th><th>Warning first?</th><th>What usually fixes it</th></tr></thead>
<tbody>
<tr><td>Egregious policy</td><td>Circumventing systems, unacceptable business practices, counterfeit, malicious software, unauthorized pharmacies, coordinated deceptive practices</td><td>No. Suspended on detection.</td><td>An appeal showing the call was a mistake, plus whatever verification Google asks for</td></tr>
<tr><td>Repeat violations</td><td>Clickbait, misleading ad design, credit repair, personal loans, bail bonds and other strike-system policies</td><td>Yes. Warning, then strikes.</td><td>Removing violating ads and acknowledging the strike; appealing if it was wrong</td></tr>
<tr><td>Billing and payment</td><td>Unpaid balance, suspicious payment activity, chargebacks, promo code abuse</td><td>Sometimes a pause first</td><td>Paying, verifying each payment method, then appealing</td></tr>
<tr><td>Unauthorized activity</td><td>Someone else got into the account</td><td>No. Temporary suspension to protect you.</td><td>Securing the login and filing the compromised account form</td></tr>
<tr><td>Verification failure</td><td>Missed deadline, mismatched documents, false information</td><td>A deadline notice</td><td>Completing verification correctly; three failed identity attempts ends the right to appeal</td></tr>
</tbody></table></div>
<p>Google says it may review your ads, website, accounts and third-party sources for the egregious policies, and that egregious suspensions mean you can’t advertise with Google again unless the appeal succeeds. That is why reading the exact policy name in the email matters more than anything else you do today.</p>"""),

            ("Circumventing systems: the one that confuses everybody", f"""<p>Google’s {SRC['g_circ']} covers attempts to get around or interfere with its ad systems. The named examples are cloaking (showing Google’s reviewer different content than users see), multiple account abuse (new accounts after a suspension, or spreading violating ads across accounts), resubmitting disapproved ads in slight variations, and false information in verification. With {SRC['g_nov25']}, Google added an example making clear that false information during Advertiser Verification is a circumventing violation, with no change to enforcement.</p>
<p>Most local businesses that get hit with it did none of that on purpose. The innocent triggers we see most:</p>
<ul>
<li>A landing page or redirect that behaves differently for bots, often from a page builder, tracking redirect or geo-redirect someone forgot about.</li>
<li>A domain that was parked or showing “coming soon” when the ad was reviewed.</li>
<li>A payment card, phone number or login shared with an account that was suspended before, sometimes a previous owner’s or an old agency’s.</li>
<li>Editing a disapproved ad over and over instead of fixing the landing page it was disapproved for.</li>
<li>A brand-new account, brand-new website and brand-new card, set up from a VPN or a shared office network.</li>
</ul>
<p>None of these is a guaranteed suspension, and we can’t see Google’s scoring. They’re just the patterns that keep showing up in the accounts we’re asked to fix.</p>"""),

            ("Misrepresentation and unacceptable business practices", f"""<p>The {SRC['g_misrep']} has ten sub-policies, including misleading representation, dishonest pricing, unreliable claims and unavailable offers. Two of them, Unacceptable business practices and Coordinated deceptive practices, are labeled egregious.</p>
<p>The {SRC['g_ubp']} covers implying an affiliation with a brand or government agency you don’t have, offering products or services you can’t deliver (including ones that need a license you lack), phishing, and impersonating public figures, including with AI-generated likenesses.</p>
<p>For Houston-area service businesses, the version that bites is subtler. A “Texas Homeowner Relief Program” headline for a roofing company. A website for an HVAC or electrical business with no license number, no physical address and no real phone. A “Google Partner” badge you aren’t entitled to. Before-and-after photos borrowed from another company. To an automated reviewer, a thin site with no business details and a big promise looks a lot like a scam. Put your legal business name, address, phone, license numbers and real photos on the site before you appeal, and before you advertise at all.</p>"""),

            ("Payment suspensions and suspicious payment activity", f"""<p>Per the {SRC['g_bill']}, billing suspensions come from unpaid balances, declined payments, suspicious payment activity, chargebacks against a legitimate Google Ads balance, and promo code abuse (selling codes or using more than one on an account). Often the account is paused first, and only admins can complete the challenge to unpause it.</p>
<p>Google’s page on {SRC['g_susp']} lays out the steps: open the in-account notice, answer questions about your payment history, then confirm the payment method if asked (documents or a code), make a payment if asked, or enter a six-digit code from a temporary $1.95 charge on your card. You may be asked to verify each payment method within 30 days before your appeal is reviewed. The verification task lives under Admin, then Policy, then Account, as “Confirm your payment method.” Uploaded documents must show the same full name, be unexpired and legible, and show all four corners in color.</p>
<p>Don’t file a chargeback because you’re frustrated with a charge. Google lists chargebacks as a suspension reason on their own. Call Google billing support instead.</p>"""),

            ("Advertiser verification, and why the name has to match", f"""<p>Google can ask any advertiser to verify who they are and who pays. The {SRC['g_verif']} says tasks depend on your account and billing setup, may include documents, and can come back after big changes like a new payments profile, billing address or legal name. Mismatched organization names and expired documents are named as common reasons tasks fail.</p>
<p>The {SRC['g_vtime']} is blunt: your account will be paused if you aren’t verified by the deadline, the deadline “can’t be extended,” and reviews take up to five business days per task (in rare cases up to 30 days). Google’s suspension page adds that if your identity can’t be verified after three attempts, you can’t appeal.</p>
<p>The Texas wrinkle is DBAs. If your payments profile says “Smith Plumbing” but your documents say “JS Mechanical LLC,” that’s a mismatch. {SRC['harris']} notes that an assumed name certificate gets filed with the county clerk where the business operates. Keep a copy of the certificate of formation and any assumed name filing ready, and make the payments profile’s legal name match them exactly.</p>"""),

            ("Strikes: the slow path to suspension", f"""<p>For policies on Google’s {SRC['g_strike']} list, you get a warning first. Keep violating the same policy and the strikes escalate:</p>
<!--fig:strikes-->
<p>To clear a hold, remove or fix every violating ad and asset and submit the acknowledgement form. New violating ads during a hold earn another strike. If the strike itself was wrong, appeal it; a successful appeal removes the strike and releases the hold immediately.</p>"""),

            ("Why new accounts get flagged", f"""<p>The Conroe dental office from the opening isn’t unusual. New accounts have no history, so Google’s systems lean hard on everything else: does the payment method’s name match the business, does the website look like a real business, is the account connected to anything that was suspended before.</p>
<p>The scale is large. In 2024 Google suspended about 39.2 million advertiser accounts worldwide, per {SRC['ser_2024']}. For 2025, per {SRC['tc_safety']}, Google blocked 8.3 billion ads and suspended 3.3 million advertiser accounts in the United States alone, while saying its AI-driven enforcement cut incorrect suspensions by 80% year over year. That’s Google’s claim, not an independent number, and it still leaves plenty of real businesses caught by mistake.</p>
<!--fig:numbers-->
<p>Before launching a new account, we’d have the website fully live with business details, set the account up on a business Google login (not someone’s personal Gmail), use a card in the business’s name, complete advertiser verification promptly when asked, and start with a modest budget. Our {L('/blog/small-business-guide-google-ads-2026/', 'small business Google Ads guide')} walks through the setup.</p>"""),

            ("Linked and related accounts", f"""<p>Google connects accounts that share payment methods, identity documents, logins, manager accounts and websites. Its suspension page says related accounts may also be suspended, and that before appealing you should make sure all linked accounts, current and previous, comply with policy. The {SRC['g_pause']} adds that accounts sharing a payment method may be paused together, and linked Merchant Center accounts can be paused too.</p>
<ul>
<li>Submit a separate appeal for each suspended account.</li>
<li>If your account was suspended because other accounts using the same identity documents were suspended, Google says yours is reinstated automatically once those are successfully appealed. Appeal the root account first.</li>
<li>If you’re linked to an agency’s manager account and the agency’s other clients are the problem, unlinking may be the fix. This is one more reason the business should own its account outright, which we cover in {L('/blog/who-owns-google-ads-account-switch-agencies/', 'who owns your Google Ads account')}.</li>
</ul>"""),

            ("How to write a Google Ads appeal that works", f"""<p>Google says reinstatement happens only in compelling circumstances, such as a mistake, and asks appeals to be “thorough, accurate, and honest.” Here’s our process:</p>
<!--fig:appeal-->
<p>Evidence that helps, depending on the policy: business registration and any assumed name filing, a Texas license number with a link to the state lookup (TDLR, TSBDE, the Texas Medical Board), a utility bill or lease for the address, screenshots showing the landing page as users see it, proof the payment card belongs to the business, and a plain list of what you changed. Here’s a sample for a circumventing-systems suspension:</p>
<blockquote><p>We are a family dental practice in Conroe, Texas, operating as [legal name] (Texas SOS file no. …). Our account was suspended on March 4 under Circumventing systems. We believe this was triggered by our website, which launched March 1 and briefly redirected mobile visitors to a scheduling page on a different domain. We removed that redirect on March 5. The account was created on a personal Gmail; we have since added a business login with 2FA. The card on file belongs to the practice. We have no other Google Ads accounts. Attached: registration, dental license lookup, website screenshots.</p></blockquote>
<p>Submit one appeal at a time. Google says excessive appeals may not be processed and suspected misuse can pause appeal processing for seven days. If it’s rejected, you can appeal again, but only once you’ve changed something real.</p>"""),

            ("What never to do while suspended", f"""<!--fig:never-->
<p>Opening a new account is the big one. Google’s Circumventing systems policy names creating new accounts after a suspension as multiple account abuse, and the suspension page says new accounts you create may also be suspended, recommending you reinstate the existing account first. A new account opened the same day almost always gets linked by card, login, domain or address, and now you have two suspensions, one of them for an egregious policy.</p>
<p>The other one: hiring a “reinstatement guaranteed” service that asks for your login, or offers to submit fresh documents for you. Verification fraud is itself a circumventing violation. If you want help, hire someone who will tell you what’s wrong with your account and your website, and let you submit truthful information yourself. If you think the account was hacked, use Google’s {SRC['g_comp']} and secure the login before anything else.</p>"""),

            ("Timelines Google actually publishes", f"""<p>Google doesn’t publish a standard turnaround for suspension appeals. It does publish timelines for the steps around them:</p>
<!--fig:timelines-->
<p>Its pausing page says pause-related appeals typically take five to seven business days, longer for complex cases. In our experience, payment and verification cases often resolve in a week or two, and egregious-policy appeals can stretch to several weeks. Plan your marketing for at least a month without Google Ads while an egregious appeal is pending: lean on your {L('/blog/google-business-profile-suspended-reinstatement/', 'Google Business Profile')}, Local Services Ads if you qualify (see {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads')}), Microsoft Ads and {L(META, 'Meta ads, as long as that account is healthy')}.</p>"""),

            ("Prevention checklist", f"""<p>Nearly every suspension we’ve helped unwind would have been avoided by some boring setup work.</p>
<!--fig:prevent-->
<p>Once you’re back, the account still has to make money. If clicks aren’t turning into calls, start with {L('/blog/google-ads-not-converting-clicks-no-calls/', 'why Google Ads clicks don’t become calls')}. Our {L('/services/search-marketing/', 'search marketing team')} sets accounts up so the business owns them, verification is done early and the site matches what the ads say. If you’re staring at a suspension notice now, <a href="/contact/">get in touch</a> and send us the exact policy name from the email.</p>"""),
        ],
        "faq": [
            ("How long does a Google Ads suspension appeal take?",
             "Google doesn’t publish a standard turnaround for suspension appeals. Its pausing page says pause-related appeals typically take five to seven business days, verification tasks take up to five business days each, and suspicious payment reviews usually get a decision within five business days. In our experience, egregious-policy appeals such as circumventing systems can take several weeks. You have at least six months from the suspension date to appeal."),
            ("Can I open a new Google Ads account if mine is suspended?",
             "No. Google’s Circumventing systems policy treats creating new accounts after a suspension as multiple account abuse, an egregious violation. Google says new accounts you create may also be suspended and recommends reinstating the existing suspended account first. New accounts usually get linked through the payment card, login, domain or address, which turns one suspension into two and makes the original appeal harder."),
            ("What does circumventing systems mean in Google Ads?",
             "It means Google believes the advertiser tried to get around or interfere with its ad review systems. Examples include cloaking, where reviewers see different content than users, creating new accounts after a suspension, resubmitting disapproved ads in variations, and giving false information during advertiser verification. Innocent triggers include unexpected redirects, parked or unfinished websites and payment methods shared with previously suspended accounts. The account is suspended without prior warning."),
            ("How many times can I appeal a Google Ads suspension?",
             "You can appeal again after a rejection, but submit one appeal at a time. Google says excessive appeals may not be processed and suspected misuse of the appeals function can pause appeal processing for seven days. Each new appeal should follow a real change, such as fixing the website or completing verification. If advertiser verification fails three times, Google says you can no longer appeal."),
            ("Why was my brand new Google Ads account suspended?",
             "New accounts have no history, so Google weighs other signals: whether the payment method matches the business, whether the website shows real business details, and whether the account links to anything previously suspended. Common triggers are a parked or unfinished website, redirects, a personal card or Gmail, and shared payment methods. Fix those, complete any requested verification, then file one detailed appeal through the in-account notice."),
        ],
        "figures": {
            "strikes": {
                "type": "funnel",
                "title": "Google Ads strike ladder",
                "stages": [["Warning (first violation)", "Email, no hold"], ["Strike 1", "3-day hold"], ["Strike 2, within 90 days", "7-day hold"], ["Strike 3, within 90 days", "Suspension"]],
                "note": "Applies to policies on Google’s strike-system list, not egregious ones",
                "alt": "Funnel showing the Google Ads warning and strike system leading to suspension for Houston advertisers",
                "caption": f"From Google’s {SRC['g_strike']}. Egregious policies skip straight to suspension.",
            },
            "numbers": {
                "type": "stats",
                "title": "Google ad enforcement at scale",
                "stats": [["3.3M", "US advertiser accounts suspended, 2025"], ["8.3B", "ads blocked worldwide, 2025"], ["80%", "fewer incorrect suspensions (Google’s claim)"], ["6 mo", "minimum window to appeal"]],
                "note": "Sources: Google 2025 Ads Safety Report via TechCrunch; Google Ads Help",
                "alt": "Stats on Google Ads account suspensions and appeals relevant to Houston and The Woodlands businesses",
                "caption": f"From {SRC['tc_safety']} and the {SRC['g_over']}.",
            },
            "appeal": {
                "type": "steps",
                "title": "Our appeal process",
                "sub": "For any suspension type",
                "steps": [["Read the exact policy", "The email and in-account notice name it. Open that policy page."], ["Check linked accounts", "Shared cards, logins, manager accounts, old accounts."], ["Fix the cause", "Website, payment, verification, redirects, ad copy."], ["Gather evidence", "Registration, license lookup, screenshots, card ownership."], ["Appeal once", "Contact Us in the notice. Thorough, accurate, honest."], ["Wait and watch email", "Appeal pending shows in the account. Don’t resubmit."]],
                "alt": "Steps to appeal a suspended Google Ads account for businesses in Houston and The Woodlands",
                "caption": "The fixing happens before the appeal, not after.",
            },
            "never": {
                "type": "compare",
                "title": "While you’re suspended",
                "left": {"title": "Don’t", "items": ["Open a new Google Ads account", "Submit appeal after appeal", "File a chargeback on Google charges", "Hand your login to a “guaranteed” service", "Edit the disapproved ad over and over"]},
                "right": {"title": "Do", "items": ["Appeal the existing account first", "One appeal, then wait for the email", "Pay balances and verify payment methods", "Submit truthful documents yourself", "Fix the landing page and business details"]},
                "alt": "Comparison of what not to do and what to do while a Google Ads account is suspended, for Houston businesses",
                "caption": "Most second suspensions we see came from the left column.",
            },
            "timelines": {
                "type": "bars",
                "title": "Timelines Google publishes",
                "sub": "Maximum or typical days, per Google Ads Help",
                "items": [["Payment code decision", 2, "2 business days"], ["Verification task review", 5, "Up to 5 business days"], ["Suspicious payment review", 5, "About 5 business days"], ["Pause-related appeal", 7, "5 to 7 business days"], ["$1.95 code charge refund", 14, "Within 14 days"], ["Verify each payment method", 30, "Within 30 days"]],
                "highlight": [3],
                "note": "No standard turnaround is published for suspension appeals",
                "alt": "Bar chart of Google Ads verification and appeal timelines for advertisers in Houston and The Woodlands",
                "caption": f"From Google’s {SRC['g_susp']}, {SRC['g_bill']}, {SRC['g_vtime']} and {SRC['g_pause']}.",
            },
            "prevent": {
                "type": "checklist",
                "title": "Google Ads suspension prevention",
                "sub": "Do these before you launch",
                "items": ["Business owns the account, on a business login with 2FA", "Payments profile legal name matches registration or DBA", "Card in the business’s name; no shared cards with old accounts", "Website live with address, phone, license numbers", "No redirects or pages that differ for bots", "Complete advertiser verification before the deadline", "Fix disapprovals at the landing page, not by resubmitting", "Never use promo codes you bought or more than one", "Ramp new accounts up gradually", "Audit manager account links and old agency access"],
                "alt": "Checklist to prevent Google Ads account suspension for small businesses in Houston and The Woodlands",
                "caption": "Boring, and it works.",
            },
        },
    },
]
