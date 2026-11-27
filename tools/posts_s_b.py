"""Refresh batch (s_b): rewrites three thin existing posts in place, same slugs.

1. complete-guide-google-reviews (step-by-step system with scripts)
2. rank-in-google-map-pack-houston (diagnostic guide: symptom, cause, fix)
3. google-ads-cost-per-click-houston-benchmarks (cost guide / data story)

Research: BrightLocal Local Consumer Review Survey 2026 (published Feb 11, 2026; 1,002 U.S. adults: 97% read reviews,
47% won't use a business with fewer than 20 reviews, 74% care about the last three months, 89% expect replies, 78%
were asked to review in the past year and 83% of those did, Google share 71%, ChatGPT/AI 45%, Apple Maps 27%);
Google Maps user-generated content policy (incentives, selective soliciting, staff quotas and requested content);
Google Business Profile help on review links and QR codes (Read reviews > Get more reviews, QR on desktop only),
on replying to reviews (moderation up to 30 days), on local ranking (relevance, distance, prominence; can't pay for
ranking) and on profile guidelines (no taglines in names, no virtual offices, SAB area about 2 hours' drive);
Venable on the FTC Consumer Review rule (penalties up to $53,088 per violation, warning letters to ten companies);
Search Engine Roundtable on Google Maps spam fighting in 2025 (292M reviews blocked or removed, 13M fake profiles,
79M edits) and on the removal of Q&A in favor of the Ask button (Dec 2025); Whitespark 2026 Local Search Ranking
Factors (published Nov 6, 2025; top pack factors and scores); ABC13 on Census estimates (Houston metro +126,720,
July 2024 to July 2025); LocaliQ / WordStream 2026 search advertising benchmarks (13,474 campaigns, April 1, 2025 to
March 31, 2026; $5.42 CPC, 6.64% CTR, 8.18% CVR, $66.69 CPL and industry figures); Google Ads help on actual CPC and
Ad Rank, Keyword Planner top-of-page bid ranges (20th and 80th percentiles) and location options (Presence or
interest is the default). Search phrasing read for "how to get more google reviews", "google review link",
"how to rank in google map pack", "google maps ranking houston", "google ads cost houston", "average cpc by industry".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

SRC = {
    # shared / reviews
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "bl_short": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 survey"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s Maps content policy"),
    "glink": A("https://support.google.com/business/answer/16816815?hl=en", "Google’s help page on review links and QR codes"),
    "greply": A("https://support.google.com/business/answer/3474050?hl=en", "Google’s guide to managing reviews"),
    "ftc": A("https://www.venable.com/insights/publications/2025/12/ftc-signals-heightened-enforcement-of-new", "Venable’s summary of the FTC’s Consumer Review rule"),
    "spam": A("https://www.seroundtable.com/google-maps-spam-fighting-2025-41176.html", "Search Engine Roundtable’s write-up of Google’s 2025 Maps numbers"),
    "ws": A("https://whitespark.ca/local-search-ranking-factors/", "Whitespark’s 2026 Local Search Ranking Factors"),
    # map pack
    "g7091": A("https://support.google.com/business/answer/7091", "Google’s own help page on local ranking"),
    "gguide": A("https://support.google.com/business/answer/3038177", "Google’s Business Profile guidelines"),
    "qa": A("https://www.seroundtable.com/google-maps-qa-feature-ask-40594.html", "Search Engine Roundtable"),
    "abc13": A("https://abc13.com/post/houston-area-tops-latest-us-census-growth-estimates-despite-slowing-population-data-shows/18791745/", "ABC13’s report on the Census estimates"),
    # cpc
    "liq": A("https://localiq.com/blog/search-advertising-benchmarks/", "LocaliQ’s 2026 search advertising benchmarks"),
    "wsb": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream’s version of the same report"),
    "gcpc": A("https://support.google.com/google-ads/answer/6297", "Google’s explanation of actual CPC"),
    "gkp": A("https://support.google.com/google-ads/answer/3022575", "Google’s Keyword Planner help"),
    "gloc": A("https://support.google.com/google-ads/answer/1722038", "Google’s location options help page"),
}

REVIEWS = "/blog/complete-guide-google-reviews/"
MAPPACK = "/blog/rank-in-google-map-pack-houston/"
CPC = "/blog/google-ads-cost-per-click-houston-benchmarks/"

POSTS = [
    # ================================================================== post 1: Google reviews
    {
        "slug": "complete-guide-google-reviews",
        "date": "2025-06-19",
        "modified": "2026-11-27",
        "title": "The Complete Guide to Google Reviews for Houston and The Woodlands Businesses",
        "seo_title": "How to Get More Google Reviews: The Complete Guide",
        "desc": "How to get more Google reviews in Houston and The Woodlands: the review link, ask scripts, timing, replies, bad reviews, and the 2026 Google and FTC rules.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google", "Yelp"],
        "art": "b2",
        "hero": "stars",
        "hero_alt": "Illustration of five stars for a guide to getting more Google reviews in Houston and The Woodlands",
        "related": ["fake-reviews-rule-local-businesses", "why-are-my-google-reviews-disappearing", "rank-in-google-map-pack-houston"],
        "sections": [
            (None, f"""<p>Forty-seven percent. That’s the share of consumers who say they won’t use a business with fewer than 20 reviews, according to {SRC['bl']}. Seventy-four percent only care about reviews from the last three months.</p>
<p>So a Spring dentist with 140 reviews, the newest from last March, can lose to a newer practice in The Woodlands with 38 reviews and three from this week. We see that pattern in Houston map results constantly.</p>
<p>This guide is the system we set up for local businesses: how to get your review link, when and how to ask, what to say back, what to do about the one-star from someone who was never a customer, and which rules changed in 2025 and 2026.</p>"""),

            ("How do you get more Google reviews?", f"""<p class="bp-answer"><b>Short answer:</b> ask every customer, every time, within a day of finishing the job, by text or email, with your direct Google review link. Make it one tap. Reply to every review within a few days. Don’t offer anything in exchange and don’t only ask the happy ones; both break Google’s rules and, for incentives, federal law.</p>
<p>That’s the whole method. The rest of this page is the detail that makes it work at a 20-truck HVAC company in Conroe or a two-chair salon on Market Street.</p>
<p>Most businesses don’t have a review problem. They have an asking problem. In BrightLocal’s 2026 numbers, 78% of consumers were asked for a review in the past year and 83% of those people left one. The customers are willing. Somebody has to send the link.</p>
<!--fig:expect-->"""),

            ("Why Google reviews matter so much in Houston right now", f"""<p>Reviews do two jobs, and owners usually only think about one of them.</p>
<p>The first is ranking. Google says plainly that “more reviews and positive ratings can help your business’s local ranking” on {SRC['g7091']}. Practitioners agree: in {SRC['ws']}, high Google ratings, the number of native Google reviews with text, and review recency all landed in the top 11 factors for the map pack, and review signals gained weight compared with the prior survey. “Sustained review flow” (steady reviews over months rather than a burst) ranked 14th.</p>
<p>The second job is conversion. The bar keeps rising. In the same BrightLocal survey, 68% of consumers want at least four stars before they’ll use a business, up from 55% a year earlier, and 31% want 4.5 or better.</p>
<p>And Google isn’t the only place people read them anymore. Google’s share as a review source fell from 83% to 71%, while ChatGPT and other AI tools jumped from 6% to 45%. Those AI answers pull heavily from reviews, so the words your customers use matter too. A review that says “they fixed our slab leak in Kingwood the same day” is doing more work than “great service!!”</p>
<!--fig:sources-->
<p>Houston adds its own pressure. The metro added more people than any other in the country between mid-2024 and mid-2025, per {SRC['abc13']}. New residents in Cypress, Conroe and along the Grand Parkway don’t have a neighbor to ask, so they read reviews, and they read the recent ones first.</p>"""),

            ("Step 1: get your Google review link and QR code", f"""<p>Per {SRC['glink']}, the steps are short. Sign in at business.google.com, open your profile, select <b>Read reviews</b>, then <b>Get more reviews</b>. You’ll get a link to copy and a QR code to download. The QR code only generates from a computer browser, not the phone app, which trips people up.</p>
<p>Things to do with that link the same afternoon:</p>
<ul>
<li>Save it as a text shortcut on every phone that talks to customers. On an iPhone that’s Settings, General, Keyboard, Text Replacement; type “rvw” and it expands to the full link.</li>
<li>Put it in your invoice template, your job-complete email and your email signature.</li>
<li>Add it to your CRM or field service software’s follow-up automation (most of them, from Jobber to the dental practice systems, have a review-request field).</li>
<li>Print the QR code on a small counter card for walk-in businesses, and on leave-behind cards for techs.</li>
</ul>
<p>Customers need to be signed in to a Google account to post. Most are. The ones who aren’t can create one with any email address, and a link that opens straight to the star screen helps a lot.</p>"""),

            ("Step 2: build the ask into the job, not your memory", f"""<p>Here’s the uncomfortable pattern we see when we look at review histories. Reviews arrive in clumps: the week after the owner read an article like this one, then nothing for four months. That’s exactly the “burst” Google and the ranking surveys don’t love.</p>
<!--fig:system-->
<p>The fix is to tie the ask to an event that already happens every time. Job marked complete in the dispatch software. Patient checked out. Invoice paid. Order delivered. The request goes out automatically within an hour or two, with one reminder two or three days later if nothing happened. No third reminder; that’s where people start to get annoyed.</p>
<p>Timing matters more than wording. In accounts we’ve run, review requests sent the same day convert far better than requests sent a week later, when the AC is just “working” again and nobody remembers how hot the house got. For a remodel, ask at the final walkthrough, while the client is standing in the new kitchen.</p>
<p>A personal ask in person, followed by the text, beats either one alone. The tech says, “If you’ve got 30 seconds, a Google review really helps a small company like ours. I’ll text you the link.” Then the text arrives before they’ve pulled out of the driveway.</p>"""),

            ("Review request scripts that work (copy these)", f"""<p>Short, specific and signed by a person. Those three things beat every template trick we’ve tested. Here are versions by situation.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Situation</th><th>Channel</th><th>Script</th></tr></thead>
<tbody>
<tr><td>Home service job done</td><td>Text, same day</td><td>“Hi Maria, it’s Josh from [company]. Thanks for having us out to fix the AC in Spring today. If you have a minute, a Google review helps us a lot: [link]. Thank you!”</td></tr>
<tr><td>Patient or client visit</td><td>Text or email, 2 hours after</td><td>“Thanks for coming in today, Daniel. We’d appreciate a quick Google review about your visit: [link]. Reply here if anything wasn’t right and we’ll call you.”</td></tr>
<tr><td>Restaurant or retail</td><td>Counter card with QR</td><td>“Enjoyed it? Tell Houston on Google. Scan to leave a review.”</td></tr>
<tr><td>Big project (remodel, pool, build)</td><td>In person, then email</td><td>“Would you be willing to write a Google review about the project? Mentioning what we built and where helps other homeowners in The Woodlands find us: [link].”</td></tr>
<tr><td>Reminder</td><td>Text, 2-3 days later</td><td>“Hi Maria, just a quick reminder in case the link got buried: [link]. No worries if not!”</td></tr>
</tbody></table></div>
<p>Notice what the remodel script does. Asking customers to mention the project and the area is fine. Telling them what to say, or asking for five stars, isn’t (more on that below). And the “reply here if anything wasn’t right” line in the second script offers a service recovery path without blocking anyone from reviewing. Every customer still gets the link.</p>
<p>Texting customers in Texas has its own rules, especially for anything promotional. A transactional review request to someone you just served is different from a marketing blast, but read our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules guide')} before you automate texts at scale.</p>"""),

            ("What does Google not allow when asking for reviews?", f"""<p>This is where good businesses get hurt, usually by a well-meaning office manager.</p>
<p>{SRC['gpol']} prohibits offering “incentives such as payment, discounts, free goods and/or services” for reviews. It bans discouraging negative reviews and “selectively solicit[ing] positive reviews from customers,” which is review gating: the “How did we do? 1-5” screen that only sends happy customers to Google. It bans pressuring people to review while on the premises. And since 2026 it explicitly bans asking staff to collect a certain number of reviews, and soliciting reviews that include specific content.</p>
<!--fig:rules-->
<p>That staff-quota rule matters for anyone who runs review contests among techs or hygienists. Recognizing the tech who gets named in reviews is fine. A $50 bonus for whoever brings in the most reviews this month is now squarely against the policy.</p>
<p>Federal law sits on top of Google’s rules. The FTC’s Consumer Review rule bans fake reviews, buying reviews, incentives tied to positive or negative sentiment, undisclosed reviews from employees and insiders, and suppressing negative reviews with threats. Civil penalties run up to $53,088 per violation, per {SRC['ftc']}, and the FTC sent warning letters to ten companies in late 2025. Our {L('/blog/fake-reviews-rule-local-businesses/', 'breakdown of the fake reviews rule')} goes through it line by line.</p>
<p>Google enforces at scale, too. It blocked or removed more than 292 million policy-violating reviews and took down over 13 million fake Business Profiles in 2025, according to {SRC['spam']}. If your reviews have been vanishing, {L('/blog/why-are-my-google-reviews-disappearing/', 'this post on disappearing reviews')} covers the usual causes, including review filters that catch legitimate reviews sent from one Wi-Fi network in your lobby.</p>"""),

            ("How should you respond to Google reviews?", f"""<p>Reply to all of them. In BrightLocal’s 2026 survey, 89% of consumers expect owners to respond, 80% are likely to use a business that responds to all reviews, and half are put off by templated replies. Nineteen percent now expect a same-day response.</p>
<p>The mechanics, from {SRC['greply']}: open your profile, select <b>Read reviews</b>, then the reply icon. Google checks replies against its content policies; most clear in about ten minutes, some take up to 30 days. The reviewer gets notified when your reply posts.</p>
<p>For positive reviews, two or three sentences. Thank them by first name, mention the actual job, and where it’s natural, the service and area: “Thanks, Chris. Glad the new water heater in your Tomball house is working well, and thanks for the kind words about Luis.” Don’t paste the same paragraph 40 times. Readers notice, and it wastes the one place you get to talk publicly.</p>
<p>Never include patient details in a reply, even to confirm someone was a patient. Medical, dental, therapy and chiropractic practices should use a single neutral reply for clinical complaints. HIPAA doesn’t stop applying because the patient brought it up first.</p>"""),

            ("How to handle a negative Google review", f"""<p>A one-star review stings more than it hurts. A business at 4.7 with a few honest complaints and calm replies often looks more believable than a perfect 5.0. What hurts is a defensive reply, or a pile of recent bad reviews with no answers.</p>
<!--fig:negative-->
<p>A reply that works has four parts. Thank them for the feedback, own the part that’s fair without arguing the rest, say what you changed, and give a direct way to reach a named person. Keep it under 80 words. You’re writing for the next 500 people who read it, not for the reviewer.</p>
<p>Example: “Mr. Davis, you’re right that we missed the arrival window twice, and that’s on us. We’ve changed how we schedule Friday afternoon calls in Cypress. I’d like to make this right; please call me directly at [number]. Kevin, Service Manager.”</p>
<p>What about reviews that aren’t real? Someone who was never a customer, a competitor, a former employee, or a review with hate speech or personal info can be reported. From the review, use the flag or “Report review” option, and track it in Google’s reviews management tool (linked from the same help page). Reviews that are merely unfair, or that describe a real bad experience, will not come down. Don’t pay anyone who promises to remove them. That’s a scam category of its own.</p>
<p>Then do the boring thing that actually fixes ratings: keep asking. One bad review against 15 new good ones in a quarter barely moves the average.</p>"""),

            ("How many Google reviews do you need to compete in Houston?", f"""<p>There’s no magic number, but there are useful targets.</p>
<p>Start with 20. That’s the line where 47% of consumers start considering you at all. Then look at who’s in the map pack for your top search in your town (say, “dentist The Woodlands” or “roofer Pearland”) and note their counts. Your 12-month goal is to land inside that range with more recent reviews than any of them.</p>
<!--fig:pace-->
<p>Recency is the cheaper race to win. A competitor with 600 reviews built over nine years might be getting four a month now. If you get 12 a month, you’ll look more alive to searchers and to Google long before you catch their total. For most service businesses, a review rate of 10% to 20% of completed jobs is realistic with an automated ask; in accounts we’ve run, businesses that add a personal in-person ask land toward the top of that range.</p>
<p>Multi-location businesses should track this per location. A strong average across four offices can hide a Katy office that hasn’t had a review since summer.</p>"""),

            ("Your first 30 days: a review system that runs itself", f"""<p>If you only do one section of this page, do this one.</p>
<ol>
<li><b>Day 1.</b> Get the link and QR code. Fix anything wrong on the profile while you’re in there (hours, categories, phone). Our {L('/blog/google-business-profile-number-one-asset/', 'Business Profile guide')} has the full list.</li>
<li><b>Days 2-5.</b> Pick the trigger (job complete, checkout, invoice paid) and set up the automated text or email with one reminder. Write two scripts from the table above in your own voice.</li>
<li><b>Week 2.</b> Train the people who finish jobs on the 15-second in-person ask. Print counter or leave-behind cards.</li>
<li><b>Week 2.</b> Reply to every review from the last 90 days that you haven’t answered. Yes, the old ones.</li>
<li><b>Weeks 3-4.</b> Check the numbers: requests sent, reviews received, average rating, reply time. Fix the step that’s leaking.</li>
<li><b>Monthly after that.</b> Five minutes to compare your count and recency with the three businesses in your map pack.</li>
</ol>
<p>Reviews also feed the rest of your marketing. The best ones belong on your website’s service pages and in ads (with permission), which we cover in {L('/blog/social-proof-reviews-testimonials/', 'using reviews as social proof')}. And because reviews are one of the biggest map pack levers, read {L(MAPPACK, 'how to rank in the Google Map Pack in Houston')} next.</p>
<p>If you’d like a senior strategist to set this up with your software and staff, tell us about your business and goals and we’ll build a custom plan. You can <a href="/contact/">get in touch</a> here.</p>"""),
        ],
        "faq": [
            ("How do I get a direct link for customers to leave a Google review?",
             "Sign in at business.google.com, open your Business Profile, select Read reviews, then Get more reviews. You can copy the link or download a QR code, though the QR code only generates in a computer browser. Save the link as a text shortcut on staff phones and add it to invoices, follow-up emails and your CRM so every customer gets it automatically."),
            ("Can I offer a discount or gift card for Google reviews in Texas?",
             "No. Google’s policy prohibits payment, discounts, free goods or services in exchange for reviews, and the FTC’s Consumer Review rule bans incentives tied to positive or negative sentiment, with civil penalties above $53,000 per violation. Raffles for reviewers fall in the same category. Ask every customer the same way, with no reward, and put your effort into timing and making the link easy."),
            ("Is it against Google policy to only ask happy customers for reviews?",
             "Yes. Google’s policy bans selectively soliciting positive reviews, which includes the common review gating setup where a survey sends only four- and five-star customers to Google. You can ask unhappy customers to contact you, but every customer must still receive the same review link. Profiles caught gating can lose reviews or face restrictions, so use one link for everyone."),
            ("How long does it take Google to remove a fake review of my business?",
             "It varies from a few days to several weeks, and many reports are declined. Flag the review from your profile, then track it in Google’s reviews management tool, where you can appeal a decision once. Reviews from non-customers, competitors, former employees, or with hate speech or personal information have the best chance. Reviews describing a real bad experience usually stay, so reply calmly instead."),
            ("Do Google reviews help my business show up in the map pack in The Woodlands?",
             "Yes. Google says more reviews and positive ratings can help local ranking, and Whitespark’s 2026 ranking factors survey put ratings, review count and review recency among the top factors for the map pack. Reviews won’t overcome distance or a wrong primary category, though. A business in The Woodlands still needs an accurate profile and service pages, with reviews pushing it up among nearby competitors."),
        ],
        "figures": {
            "expect": {
                "type": "stats",
                "title": "What local customers expect from your reviews",
                "stats": [["97%", "read reviews for local businesses"], ["47%", "won’t use a business with under 20 reviews"], ["74%", "only care about the last three months"], ["89%", "expect the owner to respond"]],
                "note": "Source: BrightLocal Local Consumer Review Survey 2026",
                "alt": "Stats on how consumers in Houston and The Woodlands read Google reviews: 97% read reviews, 47% want 20 or more",
                "caption": f"From {SRC['bl_short']} of 1,002 U.S. consumers.",
            },
            "sources": {
                "type": "bars",
                "title": "Where people read reviews now",
                "sub": "Share of consumers using each source, 2026",
                "items": [["Google", 71, "71%"], ["ChatGPT and other AI", 45, "45%"], ["Local news sites", 29, "29%"], ["Apple Maps", 27, "27%"]],
                "highlight": [0, 1],
                "note": "Source: BrightLocal Local Consumer Review Survey 2026",
                "alt": "Bar chart of review sources used by consumers, relevant to Google reviews for Houston and The Woodlands businesses",
                "caption": "Google still leads, but AI tools now summarize your reviews for nearly half of searchers.",
            },
            "system": {
                "type": "steps",
                "title": "A review system that runs without you",
                "sub": "Tie the ask to something that already happens every time",
                "steps": [["Trigger", "Job complete, checkout or invoice paid in your software."], ["Personal ask", "The tech or front desk asks in person, in one sentence."], ["Text or email", "Direct review link within two hours, signed by a person."], ["One reminder", "Two or three days later if no review. Then stop."], ["Reply", "Answer every review within a few days, by name."]],
                "alt": "Five-step automated Google review request system for Houston and The Woodlands local businesses",
                "caption": "Steady monthly reviews beat a burst every few months.",
            },
            "rules": {
                "type": "compare",
                "title": "Review requests: banned vs. allowed",
                "left": {"title": "Against Google policy or FTC rules", "items": ["Discounts or gift cards for reviews", "Only sending happy customers to Google", "Staff quotas or review contests", "Asking for five stars or set wording", "Employee or family reviews, undisclosed"]},
                "right": {"title": "Allowed and effective", "items": ["Same link to every customer", "Asking right after the job", "One polite reminder", "Asking them to mention the project", "Thanking staff named in reviews"]},
                "alt": "Comparison of banned and allowed Google review request practices for businesses in Houston and The Woodlands",
                "caption": f"Based on {SRC['gpol']} and the FTC rule.",
            },
            "negative": {
                "type": "checklist",
                "title": "Replying to a one-star review",
                "sub": "Write for the next 500 readers, not the reviewer",
                "items": ["Wait an hour, then reply within a day or two", "Thank them, by name if they used one", "Own the fair part without arguing the rest", "Say what you changed", "Give a named person and direct number", "No customer or patient details, ever", "Under 80 words", "Report it only if it breaks Google policy"],
                "alt": "Checklist for responding to a negative Google review for a Houston or The Woodlands business",
                "caption": "A calm reply often does more for trust than the review did damage.",
            },
            "pace": {
                "type": "columns",
                "title": "Recency beats total count",
                "sub": "New reviews per month: you vs. three map pack competitors",
                "labels": ["You", "Comp A", "Comp B", "Comp C"],
                "values": [60, 20, 35, 15],
                "highlight": [0],
                "y_label": "Reviews per month",
                "note": "Illustrative example: you at 12/month vs. competitors at 4, 7 and 3",
                "alt": "Column chart comparing monthly Google review pace for a business in The Woodlands against Houston competitors",
                "caption": "You can out-pace a competitor’s recent reviews in a quarter, long before you catch their total.",
            },
        },
    },

    # ================================================================== post 2: map pack
    {
        "slug": "rank-in-google-map-pack-houston",
        "date": "2025-06-05",
        "modified": "2026-11-27",
        "title": "How to Rank in the Google Map Pack Across Greater Houston and The Woodlands",
        "seo_title": "How to Rank in the Google Map Pack in Houston (2026)",
        "desc": "How to rank in the Google Map Pack in Houston and The Woodlands: what Google weighs, why you vanish 5 miles away, and a fix list for categories and reviews.",
        "category": "SEO & AI search",
        "icons": ["Google Business Profile", "Google", "Search Console"],
        "art": "b4",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for ranking in the Google Map Pack in Houston, The Woodlands and Spring",
        "related": ["google-business-profile-number-one-asset", "local-seo-myths-houston-the-woodlands", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Search “AC repair” standing on Market Street in The Woodlands, then drive 25 minutes to Kingwood and search it again. Different three businesses. Search it from Hughes Landing and from Conroe’s downtown square and you’ll probably get a third set.</p>
<p>That’s the first thing to understand about the map pack in Houston. There isn’t one ranking. There are thousands of them, one for every spot someone searches from, and your job is to win as many of those spots as your location and profile allow.</p>
<p>This guide is set up as a diagnosis: what Google says it weighs, what practitioners say matters most in 2026, the symptoms we see when a Houston business can’t get in, and the fixes in the order we’d do them.</p>"""),

            ("How do you rank in the Google Map Pack?", f"""<p class="bp-answer"><b>Short answer:</b> pick the most accurate primary category, keep your Business Profile complete and consistent with your website, earn a steady stream of recent reviews, and build a service page for each thing you sell. You’ll rank best near your address. Ranking farther out takes more reviews, stronger pages and local links.</p>
<p>Google is unusually direct about this. Per {SRC['g7091']}, local results are based on relevance, distance and prominence, and “there’s no way to request or pay for a better local ranking on Google.” Ads can appear above or inside the map results, but they don’t change where your organic listing ranks.</p>
<!--fig:factors-->
<p>The chart above comes from {SRC['ws']}, where 47 local search experts scored 187 factors. Look at the top four: your primary category, how close you are to the searcher, keywords in your business name, and whether your address is in the city being searched. Three of those are mostly fixed by decisions you made when you signed a lease.</p>
<p>That’s not a reason to give up. It’s a reason to put effort into the factors you control and to be realistic about the ones you don’t.</p>"""),

            ("Relevance: tell Google exactly what you do", f"""<p>Relevance is how well your profile matches the search. The biggest lever is your primary category, and it’s also the most common mistake we find.</p>
<p>A family dental practice in Sugar Land categorized as “Dental clinic” when “Dentist” is the category its competitors use. An HVAC company listed as “Contractor.” A med spa on “Beauty salon.” Each one is fighting with one hand tied. Search your main keyword, click into the three businesses in the pack, and see which primary category they use (free browser extensions will show you). Match the one that describes your core business. Then add secondary categories for real services, keeping in mind that {SRC['gguide']} ask you to “use as few categories as possible.”</p>
<p>Beyond categories, relevance comes from:</p>
<ul>
<li><b>Services and products in the profile.</b> List each one with a short description.</li>
<li><b>Your website.</b> The page your profile links to should name the service and the area in its title and headings. A plumber whose homepage title is “Welcome!” is giving Google nothing to work with. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} shows how to build service and area pages that support the profile.</li>
<li><b>Review text.</b> When customers mention “water heater” and “Cypress” in reviews, that’s relevance Google can read.</li>
</ul>
<p>About keywords in your business name: they do help, which is exactly why so many fake listings are named “Best Plumber Houston TX 24/7.” Google’s guidelines say your name should reflect your real-world name with no taglines. If your legal and signage name is “Spring Garage Door Repair,” great. Adding keywords to a name that isn’t yours is a fast route to a suspension, and we’ve watched it cost businesses months.</p>"""),

            ("Distance: why you disappear five miles away", f"""<p>This is the factor owners argue with most, and the one they can change least.</p>
<p>Google measures distance from the searcher (or the place named in the search) to your business address. Service-area businesses that hide their address are still ranked from that hidden address. Listing 20 towns in your service area tells Google where you work. It doesn’t move your pin.</p>
<!--fig:rings-->
<p>The map shows the pattern we typically see for a single-location business near the center of The Woodlands. Strong in The Woodlands, Shenandoah and much of Spring. Patchy in Conroe and Tomball. Rarely in the pack in Katy, Pearland or Kingwood without a much larger review count than the local competitors there.</p>
<p>What you can do about distance:</p>
<ul>
<li><b>Win close-in first.</b> Make sure you own the 3-5 mile radius around your address before worrying about the far edge of the metro.</li>
<li><b>Rank organically farther out.</b> The regular results under the map pack aren’t tied to your pin the same way. A well-built “AC repair in Katy” page can rank there even when your profile can’t.</li>
<li><b>Use ads for the far towns.</b> Search ads and Local Services Ads cover the places your pin won’t reach. See {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</li>
<li><b>Open a real second location</b> only if you’d actually staff it. Virtual offices and coworking desks you never use aren’t eligible, per Google’s guidelines, and they get caught.</li>
</ul>
<p>One Houston-specific wrinkle: mailing addresses. Plenty of businesses in The Woodlands have Spring or Conroe mailing addresses, and that affects which “city” Google thinks you’re in. We wrote up {L('/blog/the-woodlands-spring-conroe-address-local-seo/', 'how The Woodlands, Spring and Conroe addresses affect local SEO')}. If you’re moving, read {L('/blog/change-business-address-google-without-suspension/', 'how to change your address without a suspension')} first.</p>"""),

            ("Prominence: reviews, links and real-world reputation", f"""<p>Prominence is Google’s read on how well known and trusted you are. Google’s help page lists reviews, links and articles about your business, and notes that your standing in regular web results counts too.</p>
<p>For most local businesses, reviews are the fastest prominence lever you control. Whitespark’s survey put high ratings at No. 6, the number of Google reviews with text at No. 9, and recency at No. 11 among map pack factors. Our {L(REVIEWS, 'complete guide to Google reviews')} has the system and scripts.</p>
<p>Links and mentions are slower but compound. In Houston, the realistic ones are your chamber of commerce membership pages (The Woodlands Area Chamber, Greater Conroe, Katy Area and the rest), local sponsorships, supplier and manufacturer dealer locators, and coverage in Community Impact or the Houston Chronicle. Whitespark’s 2026 survey also noted that for AI search visibility, citations and mentions mattered more than ever. Our posts on {L('/blog/get-press-coverage-houston-the-woodlands/', 'getting press coverage in Houston')} and {L('/blog/local-sponsorships-youth-sports-the-woodlands-houston/', 'local sponsorships')} cover the practical side.</p>
<!--fig:clean-->"""),

            ("Why isn’t my business showing up in the Google Map Pack?", f"""<p>Here are the symptoms we see most often in Houston and The Woodlands, with the cause we usually find and the fix.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Symptom</th><th>Likely cause</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Not in the pack even for searches next to your office</td><td>Wrong primary category, or the profile is unverified or suspended</td><td>Match competitors’ primary category; check status in your profile; see our {L('/blog/google-business-profile-suspended-reinstatement/', 'reinstatement guide')}</td></tr>
<tr><td>In the pack near the office, gone two exits up I-45</td><td>Normal distance effect, plus fewer reviews than the local leaders there</td><td>Build review pace; add an area page; use ads for those towns</td></tr>
<tr><td>Show for your brand name, not for the service</td><td>Thin relevance: website page and profile don’t name the service</td><td>Service list in the profile, a dedicated service page, review text that names it</td></tr>
<tr><td>Rankings dropped suddenly</td><td>Profile edit triggered a review, a competitor’s new location, or a filter (two businesses at one address)</td><td>Check edit history and notifications; undo risky edits; separate shared suites clearly</td></tr>
<tr><td>A keyword-stuffed competitor outranks you</td><td>Their name breaks Google’s guidelines</td><td>Suggest an edit with the real name, or use the business redressal complaint form with evidence</td></tr>
<tr><td>Rank fine at 9 a.m., gone at 9 p.m.</td><td>Hours: “open at time of search” is a top-five factor</td><td>Accurate hours, holiday hours, and 24-hour hours only if someone really answers</td></tr>
</tbody></table></div>
<p>That “open at time of search” row surprises people. Whitespark ranked it fifth overall. An emergency plumber who says they close at 5 can lose the 8 p.m. slab leak search in Humble to someone who honestly lists 24 hours.</p>"""),

            ("Do photos, posts and the other profile extras help you rank?", f"""<p>Less than the people selling them say, and more than zero.</p>
<p>Photos don’t appear anywhere near the top of the ranking factor lists. They matter for the second half of the job, which is getting the click once you’re in the pack. A profile with real photos of your trucks in a Magnolia driveway, your front desk and your team gets chosen over one with three stock images and a logo. Add a few new ones each month. Skip the photo geotagging tricks; we’ve never seen them move a ranking.</p>
<p>Google posts (offers, updates, events) are similar. They won’t move you from seventh to second, but a current post with a seasonal offer or a hurricane-prep reminder makes the profile look alive, and an expired one from 2023 makes it look abandoned. Once or twice a month is plenty.</p>
<p>Two extras do matter more. Products and services: fill them in, because they’re relevance Google can read directly. And the profile description: with Q&amp;A gone, it’s one of the main sources the Ask button pulls from, so write it plainly with what you do, where and for whom.</p>
<p>Shared addresses are worth a warning. Two businesses in one suite at a Research Forest office park, or a husband-and-wife pair of companies at one house in Spring, can trigger Google’s filter so only one shows. If that’s you, use clearly separate suite numbers, phone numbers and signage, and expect Google to ask for proof.</p>"""),

            ("What changed on Google Business Profiles in 2025 and 2026", f"""<p>Some of the older advice you’ll find online is now out of date.</p>
<ul>
<li><b>Q&amp;A is gone from public view.</b> Google removed the public Q&amp;A section and replaced it with an AI-powered “Ask” button that answers from your business information and relevant reviews, per {SRC['qa']} in December 2025. Your profile description, services and reviews now do the work Q&amp;A used to.</li>
<li><b>Video verification is common.</b> New profiles and edited ones often get asked for a short video of signage, the location and proof of management. Our {L('/blog/google-business-profile-video-verification/', 'video verification guide')} walks through what passes.</li>
<li><b>Spam fighting got more aggressive.</b> Google removed over 13 million fake profiles and blocked 79 million inaccurate edits in 2025, per {SRC['spam']}. Good news for honest businesses, bad news for anyone with a virtual office listing.</li>
<li><b>Reviews show up in more places.</b> Per {SRC['bl']}, 45% of consumers now use AI tools as a review source and 27% use Apple Maps. Claim Apple Business Connect and Bing Places too; they take an hour.</li>
</ul>
<!--fig:stats-->
<p>None of this changes the three core factors. It does mean AI Overviews and chat answers increasingly decide which businesses get mentioned before anyone sees the map. We cover that in {L('/blog/ai-overviews-local-search-houston/', 'AI Overviews and local search in Houston')}.</p>"""),

            ("How to track your map pack ranking (properly)", f"""<p>Searching from your own phone at the office tells you almost nothing. Google personalizes, and you’re standing on top of your own pin.</p>
<p>Use a grid rank tracker (Local Falcon, BrightLocal and Whitespark all sell them). It checks your rank for a keyword at points across a grid, say a 7x7 grid with a mile between points, and shows you a heat map. Run it monthly for your three most valuable searches. The goal is a growing share of grid points where you’re in the top three.</p>
<!--fig:grid-->
<p>Then watch what matters more than rank. In your Business Profile’s Performance view: calls, website clicks and direction requests, plus the search terms people used. In Google Search Console, filter for the URL your profile links to (add a UTM tag so you can separate profile traffic in GA4). Our guide to {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking calls and form submissions in GA4')} shows the setup. A grid that turns greener while calls stay flat means you’re ranking for the wrong searches.</p>"""),

            ("A 90-day plan to climb the map pack in Houston", f"""<!--fig:plan-->
<p>Most stuck profiles move within a few months once the basics are fixed, if the business is reasonably close to the searches it wants. How fast depends on how strong the three businesses ahead of you are. A new roofer in Pearland against competitors with 900 reviews each is a longer project than a new dentist in Magnolia.</p>
<p>A few things we’d skip: buying citations in bulk from hundreds of directories nobody visits, “GMB posting” packages that publish daily filler, fake suites, and anything sold as a guaranteed No. 1. The {L('/blog/local-seo-myths-houston-the-woodlands/', 'local SEO myths post')} has more of those.</p>
<p>If you want help, our {L('/services/web-design-seo-pr/', 'SEO team')} does this work for Houston-area businesses. Tell us about your business and goals and a senior strategist will build a custom plan. Just <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("Why does my business show up in Google Maps in The Woodlands but not in Houston?",
             "Distance from the searcher is one of Google’s three core local ranking factors, and your profile is ranked from your actual address even if it’s hidden. A business in The Woodlands will usually rank well nearby and fade toward Houston, Katy or Pearland. To reach farther, build area service pages that rank in regular results, increase your review count, and use search ads for distant towns."),
            ("Does adding cities to my service area help me rank in more Houston suburbs?",
             "Not much. The service area tells customers and Google where you work, but rankings are still calculated from your business address. Google’s guidelines say the overall area shouldn’t extend beyond about two hours of driving time. Listing Katy, Sugar Land and Pearland won’t put a Spring-based business in those map packs. Area pages on your website and ads do more."),
            ("How long does it take to get into the Google 3-pack?",
             "If the problem is a wrong category, missing info or a suspended profile, fixes can show results within weeks. Building enough reviews and links to beat established competitors usually takes three to nine months, depending on how strong they are and how close you are to the searches. A grid rank tracker run monthly will show if you’re gaining ground."),
            ("Is it OK to put keywords in my Google Business Profile name?",
             "Only if they’re part of your real business name as it appears on your signage, website and legal documents. Google’s guidelines prohibit adding taglines, service keywords or locations that aren’t part of your actual name. Keywords in the name do help rankings, which is why competitors abuse it, but the risk of a suspension isn’t worth it. You can report violators with a suggested edit."),
            ("Can I pay Google to rank higher in the map pack in Houston?",
             "No. Google states there is no way to request or pay for a better local ranking. You can pay for ads that appear above or within the map results, including search ads with location assets and Local Services Ads, but those don’t change your organic position. Organic map rankings come from relevance, distance and prominence, which means categories, address, reviews, content and links."),
        ],
        "figures": {
            "factors": {
                "type": "bars",
                "title": "What experts say moves map pack rankings",
                "sub": "Top local pack factors, Whitespark 2026 survey score",
                "items": [["Primary GBP category", 227, "227"], ["Proximity to searcher", 225, "225"], ["Keywords in business name", 223, "223"], ["Address in city searched", 213, "213"], ["Open at time of search", 189, "189"], ["High Google rating", 181, "181"]],
                "highlight": [0, 4, 5],
                "note": "Source: Whitespark Local Search Ranking Factors 2026. Highlighted: factors you control",
                "alt": "Bar chart of the top Google Map Pack ranking factors for Houston and The Woodlands businesses from Whitespark 2026",
                "caption": "Category, hours and reviews are yours to fix. Distance and address mostly aren’t.",
            },
            "rings": {
                "type": "map",
                "title": "Where a Woodlands business usually ranks",
                "sub": "Typical map pack reach for one location near The Woodlands",
                "highlight": ["The Woodlands", "Shenandoah", "Spring", "Conroe", "Tomball"],
                "note": "Illustrative example: highlighted towns are where a single location typically competes",
                "alt": "Map of Greater Houston showing typical Google Map Pack reach for a business based in The Woodlands",
                "caption": "Close-in towns come first. Katy, Pearland and Kingwood usually take ads or area pages.",
            },
            "clean": {
                "type": "checklist",
                "title": "Business Profile checklist for Houston",
                "sub": "The basics we check on every profile",
                "items": ["Primary category matches the pack leaders", "Real business name, no added keywords", "Accurate hours, holiday hours set", "Every service listed with a description", "Profile links to the matching service page", "Same name, address and phone everywhere", "Real photos of team, vehicles and work", "Apple Business Connect and Bing claimed", "Review link in every follow-up", "Every review answered"],
                "alt": "Google Business Profile checklist for ranking in the map pack in Houston and The Woodlands",
                "caption": f"Built from {SRC['gguide']} and the factors above.",
            },
            "stats": {
                "type": "stats",
                "title": "Google’s 2025 Maps clean-up, by the numbers",
                "stats": [["13M", "fake Business Profiles removed"], ["292M", "policy-violating reviews blocked or removed"], ["79M", "inaccurate edits blocked"], ["127K", "new Houston metro residents, 2024 to 2025"]],
                "note": "Sources: Google via Search Engine Roundtable; U.S. Census via ABC13",
                "alt": "Stats on Google Maps fake listings removed and Houston population growth affecting map pack competition",
                "caption": "Fewer fake competitors, more new customers searching. Both favor honest local profiles.",
            },
            "grid": {
                "type": "columns",
                "title": "Share of grid points in the top 3",
                "sub": "7x7 rank grid for one keyword, month by month",
                "labels": ["Start", "Month 1", "Month 2", "Month 3", "Month 4", "Month 5"],
                "values": [18, 22, 31, 39, 45, 51],
                "highlight": [5],
                "y_label": "% of grid in top 3",
                "note": "Illustrative example, not a client result",
                "alt": "Column chart of map pack grid rank improvement for a local business in The Woodlands and Houston over five months",
                "caption": "Track the share of the grid you win, then check it against calls.",
            },
            "plan": {
                "type": "steps",
                "title": "90 days to climb the Houston map pack",
                "sub": "In the order we’d do it",
                "steps": [["Week 1", "Category, name, hours, services. Check status and edits."], ["Weeks 2-3", "Service pages and an area page for your top town."], ["Weeks 2-4", "Automated review requests, every review answered."], ["Month 2", "Citations cleaned up; Apple, Bing, chamber listings."], ["Month 3", "Local links and press; grid tracking against calls."]],
                "alt": "Five-step 90-day plan to rank in the Google Map Pack for businesses in Houston and The Woodlands",
                "caption": "Fix the profile first. Reviews and links take longer but keep paying.",
            },
        },
    },

    # ================================================================== post 3: CPC benchmarks
    {
        "slug": "google-ads-cost-per-click-houston-benchmarks",
        "date": "2026-10-02",
        "modified": "2026-11-27",
        "title": "How Much Do Google Ads Cost in Houston? Cost-Per-Click Benchmarks by Industry (2026)",
        "seo_title": "Google Ads Cost in Houston: CPC by Industry (2026)",
        "desc": "2026 Google Ads cost per click in Houston by industry: national benchmarks, what Houston and The Woodlands advertisers pay, budget math and how to pay less.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Google Analytics", "Microsoft Ads"],
        "art": "b6",
        "hero": "receipt",
        "hero_alt": "Illustration of a receipt for Google Ads cost per click benchmarks in Houston and The Woodlands",
        "related": ["google-ads-quality-score-lower-cost-per-click", "google-ads-management-houston-cost", "understanding-cost-per-lead"],
        "sections": [
            (None, f"""<p>$5.42. That’s the average cost per click on search ads across all industries in the latest data, from {SRC['liq']}. It’s also close to useless for planning a budget in Houston, because nobody pays the average.</p>
<p>A lawyer bidding on “18 wheeler accident attorney Houston” and a bakery in Tomball bidding on “custom birthday cakes” are in completely different auctions. One might pay more for a single click than the other spends in a week.</p>
<p>This guide gives you the 2026 benchmarks by industry, what we see Houston and The Woodlands advertisers actually pay, the math to turn a click price into a budget, and the levers that push your cost down.</p>"""),

            ("How much does Google Ads cost per click in Houston?", f"""<p class="bp-answer"><b>Short answer:</b> most Houston-area businesses pay somewhere between $2 and $12 per click on Google search ads in 2026, with the national average at $5.42. Legal, home services and dental sit at the top; restaurants and travel near the bottom. Competitive Houston terms like personal injury or emergency HVAC can run far higher.</p>
<p>The national numbers come from LocaliQ’s analysis of 13,474 U.S. search campaigns running from April 1, 2025, to March 31, 2026 (the figures are medians, which keeps a few extreme accounts from skewing them), per {SRC['wsb']}. Across all industries: $5.42 per click, a 6.64% click-through rate, an 8.18% conversion rate and $66.69 per lead.</p>
<!--fig:topline-->
<p>The direction is worth noting. Clicks got a bit more expensive again, but cost per lead fell overall for the first time in five years, because conversion rates improved. Better-built campaigns are absorbing the price increases. Sloppy ones aren’t.</p>"""),

            ("Average Google Ads cost per click by industry (2026)", f"""<p>Here are the 2026 averages for the industries we get asked about most, from the same LocaliQ data.</p>
<!--fig:cpc-->
<div class="bp-tbl"><table>
<thead><tr><th>Industry</th><th>Avg. CPC</th><th>Conv. rate</th><th>Avg. cost per lead</th><th>What we see in Houston</th></tr></thead>
<tbody>
<tr><td>Attorneys &amp; legal</td><td>$9.87</td><td>5.55%</td><td>$131.63</td><td>Personal injury and trucking terms run well above this; family law and estate planning are closer</td></tr>
<tr><td>Home &amp; home improvement</td><td>$8.33</td><td>8.05%</td><td>$90.92</td><td>HVAC in summer, roofing after hail or hurricanes, and foundation repair spike hardest</td></tr>
<tr><td>Dentists &amp; dental</td><td>$8.00</td><td>10.67%</td><td>$72.97</td><td>Implants and Invisalign cost far more per click than “dentist near me”</td></tr>
<tr><td>Personal services</td><td>$7.17</td><td>12.34%</td><td>$54.60</td><td>Med spa terms in The Woodlands and River Oaks are crowded</td></tr>
<tr><td>Health &amp; fitness</td><td>$6.17</td><td>n/a</td><td>$67.36</td><td>Up about 23% year over year nationally; January is the priciest month for gyms</td></tr>
<tr><td>Business services</td><td>$5.87</td><td>4.85%</td><td>$93.69</td><td>B2B terms tied to energy and industrial buyers can be expensive</td></tr>
<tr><td>Physicians &amp; surgeons</td><td>$4.76</td><td>12.43%</td><td>$40.04</td><td>Elective specialties (plastic surgery, weight loss) cost more than primary care</td></tr>
<tr><td>Beauty &amp; personal care</td><td>$4.62</td><td>n/a</td><td>$39.25</td><td>Usually manageable with a tight radius</td></tr>
<tr><td>Automotive repair</td><td>$4.35</td><td>15.51%</td><td>$29.96</td><td>Specific services (transmission, brakes) convert best</td></tr>
<tr><td>Real estate</td><td>$3.22</td><td>3.70%</td><td>$102.51</td><td>Cheap clicks, low conversion; up 27% nationally</td></tr>
<tr><td>Restaurants &amp; food</td><td>$2.05</td><td>n/a</td><td>$30.57</td><td>Catering and private events are the terms worth paying for</td></tr>
</tbody></table></div>
<p>Source for the dollar figures: {SRC['liq']}. The Houston column is our experience running and reviewing local accounts, not survey data. “n/a” means we didn’t verify a conversion rate for that category.</p>
<p>Real estate and the fitness and personal services categories saw the biggest CPC increases nationally (about 27% and 23%). If you run ads in those categories and your costs jumped this year, the market moved, not just your account.</p>
<p>Two cautions on reading any benchmark table. These are medians across thousands of accounts, many of them small, so a well-run account in your category should beat the conversion rate column. And category averages blur huge differences inside a category. “Home improvement” lumps together a $40,000 pool build and a $90 gutter cleaning, which is why the number you really need is the click price for your own five or ten best keywords in your own service area.</p>"""),

            ("Why Google Ads cost more in some parts of Houston", f"""<p>Google doesn’t publish CPCs by city. What we can tell you from inside accounts is where competition stacks up.</p>
<!--fig:map-->
<p>Clicks get pricier where three things overlap: high household incomes, lots of new homes, and lots of advertisers in the same trades. The Woodlands, Katy, Cypress, Sugar Land and the Memorial and Galleria corridor all tick those boxes. Home services, med spas, dentists and orthodontists in those areas compete with each other and with metro-wide companies bidding across all of Harris, Montgomery and Fort Bend counties.</p>
<p>Growth adds bidders. The Houston metro gained 126,720 residents in the year to July 2025, the most of any U.S. metro, per {SRC['abc13']}. New subdivisions along the Grand Parkway, in Conroe and out past Cypress bring new customers and, a few months later, new competitors chasing them.</p>
<p>Weather is the other Houston multiplier. In the HVAC accounts we’ve run, the first week of real heat in May or June and any power outage during a storm push emergency search volume and click prices up at the same time. Roofing and water damage restoration see the same thing after hail or a hurricane. Our {L('/blog/hurricane-season-marketing-playbook-houston-the-woodlands/', 'hurricane season playbook')} covers how to budget for those weeks.</p>
<!--fig:season-->"""),

            ("What actually decides your cost per click", f"""<p>Google Ads is an auction, but you don’t pay your bid. Per {SRC['gcpc']}, your actual CPC is the minimum needed to clear the Ad Rank thresholds and beat the advertiser below you. Ad Rank combines your bid with ad quality (expected click-through rate, ad relevance and landing page experience), the competitiveness of the auction, the context of the search, and the expected impact of your assets.</p>
<p>Translated into things you can change:</p>
<ul>
<li><b>Keyword intent.</b> “Emergency AC repair Spring TX” costs more than “how does an AC work,” and is worth far more. Pay for the first kind.</li>
<li><b>Ad quality.</b> A relevant ad sending people to a matching page lowers what you pay for the same position. Our {L('/blog/google-ads-quality-score-lower-cost-per-click/', 'Quality Score guide')} goes deep on this.</li>
<li><b>Location settings.</b> Google’s default option is “Presence or interest,” which can show your ads to people who are only interested in Houston, per {SRC['gloc']}. For most local businesses we switch it to “Presence” so you’re not paying for a click from someone in Ohio.</li>
<li><b>Schedule.</b> Running 24/7 when nobody answers the phone after 6 p.m. pays for clicks you can’t convert.</li>
<li><b>Campaign type.</b> Search, Performance Max and Local Services Ads all price differently. See {L('/blog/performance-max-vs-search-campaigns-local/', 'Performance Max vs. Search')} and {L('/blog/local-services-ads-vs-google-ads-home-services/', 'Local Services Ads vs. Google Ads')}.</li>
</ul>
<p>To estimate your own CPCs before spending, use Keyword Planner. Its “top of page bid” columns show roughly the 20th and 80th percentile of past top-of-page bids for a keyword, filtered to your location, per {SRC['gkp']}. Set the location to your actual service area, not all of Texas. Expect to pay toward the high end in your first few weeks while the account builds history.</p>"""),

            ("How much should a small business spend on Google Ads in Houston?", f"""<p>Work backward from customers, not forward from a number that feels comfortable.</p>
<!--fig:math-->
<p>The funnel above uses the home improvement averages: $8.33 per click and an 8.05% conversion rate. At $3,000 a month, that’s about 360 clicks and 29 leads. If your team closes 40% of leads, that’s roughly 11 or 12 jobs. Whether that’s a good deal depends entirely on what a job is worth to you. For a $9,000 AC replacement, it’s great. For a $150 service call with no follow-on work, it’s tight.</p>
<p>Rough monthly ad spend ranges we see for single-location Houston businesses (ad spend only, not management):</p>
<ul>
<li><b>$1,500-$3,000:</b> one service, one area, tight keyword list. Enough to learn, not enough to cover the metro.</li>
<li><b>$3,000-$7,500:</b> two or three service campaigns across your core towns. Where most home service and dental accounts we look at sit.</li>
<li><b>$7,500 and up:</b> competitive categories (legal, roofing, HVAC in summer) or multiple locations.</li>
</ul>
<p>Below about $1,000 a month in a category with $8-10 clicks, you’re buying around 100 clicks, which isn’t enough data for Google’s bidding to learn or for you to judge. Put that money into your Business Profile and reviews first. Our {L('/blog/set-a-marketing-budget-small-business/', 'marketing budget guide')} and {L('/blog/google-ads-management-houston-cost/', 'what Google Ads management costs in Houston')} cover the rest of the math.</p>"""),

            ("Which Houston keywords are worth the click (and which to block)?", f"""<p>The cheapest way to lower your average CPC is to stop paying for searches that were never going to become customers. The most expensive way is to chase low-intent keywords because they look cheap.</p>
<p>Here’s how we’d sort keywords for a Houston plumbing company, as an example. The pattern holds for most local services.</p>
<ul>
<li><b>Bid hard:</b> “emergency plumber near me,” “slab leak repair Spring TX,” “water heater replacement The Woodlands,” “burst pipe repair Houston.” Urgent, specific, local. These are the clicks you can afford to pay $15 or more for if your jobs are worth it.</li>
<li><b>Bid carefully:</b> “plumber Houston,” “plumbing company Katy.” Broad but local. Worth it with tight ad copy and a page per town.</li>
<li><b>Usually skip:</b> “how to fix a running toilet,” “plumbing cost,” “water heater sizes.” Research searches. Content on your website can win these for free.</li>
<li><b>Block with negatives:</b> jobs, hiring, salary, apprenticeship, license test, DIY, YouTube, parts, supply house names, free, and any town you don’t serve (Galveston, Beaumont, Huntsville if you stop at Willis).</li>
</ul>
<p>Write ads that sort people before they click. “Licensed Houston plumbers. Slab leak detection from [your price]. Same-day in Spring, The Woodlands and Conroe.” A price, a service and a set of towns will scare off some clicks, and they’re the ones you didn’t want to pay for.</p>
<p>And judge match types by results. Broad match paired with smart bidding can work well once you have 30 or more tracked conversions a month. Before that, phrase and exact match on a short list give you control while the account learns. Check the search terms report every week either way.</p>
<p>Track five numbers monthly: cost per click, conversion rate, cost per lead, cost per booked job, and search impression share lost to budget. That last one tells you whether more budget would buy more leads or just more expensive clicks.</p>"""),

            ("Cost per lead matters more than cost per click", f"""<p>A $12 click that converts at 20% costs $60 per lead. A $3 click that converts at 2% costs $150. Owners who fixate on CPC tend to buy cheap, broad keywords and wonder why the phone doesn’t ring.</p>
<!--fig:cheap-->
<p>The two numbers to watch every month are cost per lead and cost per customer. You can only see them if calls and forms are tracked as conversions, so start with {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking calls and form submissions')}. If you’re getting clicks but no calls, read {L('/blog/google-ads-not-converting-clicks-no-calls/', 'why Google Ads clicks don’t turn into calls')}. And some “leads” aren’t; {L('/blog/google-ads-click-fraud-spam-leads/', 'our click fraud and spam leads post')} covers what to filter.</p>
<p>Our {L('/blog/understanding-cost-per-lead/', 'cost per lead guide')} explains how to work out what you can afford to pay for one.</p>"""),

            ("How to lower your Google Ads cost per click", f"""<!--fig:lower-->
<p>A few notes on those steps from accounts we’ve run.</p>
<p>Negatives come first because they’re the fastest money. In a typical Houston home services account, the first search terms report shows clicks on “jobs,” “salary,” “how to,” “DIY,” competitor supply houses and towns you don’t serve. Add negatives weekly for the first two months, then monthly.</p>
<p>Splitting campaigns by service lets you write an ad that matches the search and send it to a page that matches the ad. That’s the main thing that moves ad relevance and landing page experience, two of the three parts of Quality Score. The page matters more than people expect; see {L('/blog/landing-pages-101/', 'landing pages 101')}.</p>
<p>Don’t forget Microsoft Ads. The LocaliQ figures blend Google and Microsoft campaigns, and in our experience Bing clicks for local services often cost less, with an older audience that converts well for some trades. Our post on {L('/blog/are-microsoft-ads-worth-it-small-business/', 'whether Microsoft Ads are worth it')} has the trade-offs.</p>
<p>If your costs feel high and you can’t tell why, our {L('/services/search-marketing/', 'search marketing team')} can take a look. Tell us about your business and goals and a senior strategist will build a custom plan. Just <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("What is a good cost per click for Google Ads in Houston?",
             "It depends on your industry. In 2026 the national average is $5.42, with legal around $9.87, home improvement $8.33, dental $8.00 and restaurants $2.05, per LocaliQ. A good CPC in Houston is one that produces leads at a cost you can afford, so judge it against cost per lead and cost per customer. A higher click price is fine if those clicks convert well."),
            ("How much does a Google Ads click cost for HVAC companies in Houston?",
             "There’s no published Houston HVAC average. Nationally, home and home improvement clicks average $8.33 in 2026. In Houston HVAC accounts we’ve run, emergency and repair terms run above that during the first heat waves and storm outages, while maintenance and tune-up terms cost less. Use Keyword Planner with your exact service area to see current top-of-page bid ranges before setting a budget."),
            ("Why are my Google Ads so expensive in The Woodlands?",
             "The Woodlands has high household incomes, many new homes and lots of advertisers in home services, healthcare and med spas, so auctions are competitive. Costs also rise when ads are broad, run 24/7, target interest in the area instead of presence, or send clicks to a generic homepage. Tightening keywords, negatives, location settings and landing pages usually lowers costs within weeks."),
            ("Is $1,000 a month enough for Google Ads for a small business in Houston?",
             "In low-cost categories like restaurants, auto repair or beauty, $1,000 can produce useful leads with a tight radius and narrow keyword list. In categories averaging $8 to $10 per click, it buys only about 100 to 125 clicks a month, which is thin for learning. In that case, start with your Business Profile and reviews, or focus on one high-value service."),
            ("Do Google Ads cost more during hurricane season in Houston?",
             "For some trades, yes. Roofing, water damage restoration, generator and tree service searches surge after storms, and so do competing advertisers, which pushes click prices up for days or weeks. Many other categories see little change. Set aside budget for storm weeks, prepare ads and landing pages before June, and watch search terms closely when demand spikes so you don’t pay for irrelevant clicks."),
        ],
        "figures": {
            "topline": {
                "type": "stats",
                "title": "Google search ads in 2026, all industries",
                "stats": [["$5.42", "average cost per click"], ["6.64%", "average click-through rate"], ["8.18%", "average conversion rate"], ["$66.69", "average cost per lead"]],
                "note": "Source: LocaliQ / WordStream 2026 benchmarks, 13,474 U.S. campaigns, April 2025 to March 2026",
                "alt": "Stats showing 2026 Google Ads benchmarks used to estimate cost per click in Houston and The Woodlands",
                "caption": "National medians. Your auction in Houston will differ by industry, service and area.",
            },
            "cpc": {
                "type": "bars",
                "title": "Average cost per click by industry, 2026",
                "sub": "U.S. search campaigns",
                "items": [["Attorneys & legal", 9.87, "$9.87"], ["Home improvement", 8.33, "$8.33"], ["Dentists", 8.00, "$8.00"], ["Personal services", 7.17, "$7.17"], ["Health & fitness", 6.17, "$6.17"], ["Business services", 5.87, "$5.87"], ["Auto repair", 4.35, "$4.35"], ["Real estate", 3.22, "$3.22"], ["Restaurants", 2.05, "$2.05"]],
                "highlight": [0, 1, 2],
                "note": "Source: LocaliQ Search Advertising Benchmarks 2026",
                "alt": "Bar chart of 2026 Google Ads cost per click by industry for Houston and The Woodlands advertisers",
                "caption": "Legal, home services and dental top the list in Houston too.",
            },
            "map": {
                "type": "map",
                "title": "Where Houston Google Ads auctions get crowded",
                "sub": "Areas where we most often see competitive local auctions",
                "highlight": ["The Woodlands", "Katy", "Cypress", "Sugar Land", "Memorial", "Galleria"],
                "note": "Based on our account experience, not published city-level CPC data",
                "alt": "Map of Houston and The Woodlands areas with competitive Google Ads auctions, including Katy, Cypress and Sugar Land",
                "caption": "High incomes, new homes and many advertisers in the same trades push clicks up.",
            },
            "season": {
                "type": "columns",
                "title": "Houston HVAC click costs through the year",
                "sub": "Relative cost per click for emergency AC repair terms",
                "labels": ["Jan", "Mar", "May", "Jun", "Jul", "Aug", "Oct", "Dec"],
                "values": [45, 50, 75, 95, 100, 90, 55, 45],
                "highlight": [3, 4, 5],
                "y_label": "Relative CPC",
                "note": "Illustrative example based on the seasonal pattern we see, not a measured index",
                "alt": "Column chart of seasonal Google Ads cost per click for HVAC companies in Houston and The Woodlands",
                "caption": "Plan for summer and storm weeks; prices and volume rise together.",
            },
            "math": {
                "type": "funnel",
                "title": "From budget to booked jobs",
                "stages": [["Monthly ad spend", "$3,000"], ["Clicks at $8.33", "~360"], ["Leads at 8.05%", "~29"], ["Jobs at 40% close", "~11"]],
                "note": "Illustrative example using 2026 home improvement averages; close rate is an assumption",
                "alt": "Funnel showing how a Google Ads budget turns into leads and jobs for a Houston home services business",
                "caption": "Swap in your own close rate and job value to see what a click is worth to you.",
            },
            "cheap": {
                "type": "compare",
                "title": "Cheap clicks vs. cheap leads",
                "left": {"title": "Chasing low CPC", "items": ["Broad keywords like “AC”", "Ads shown to anyone interested in Houston", "Runs 24/7, nobody answers at night", "Traffic sent to the homepage", "Judged on clicks and impressions"]},
                "right": {"title": "Chasing low cost per lead", "items": ["Service plus town keywords", "Presence-only location targeting", "Schedule matched to who picks up", "Dedicated service landing pages", "Judged on calls, forms and jobs"]},
                "alt": "Comparison of low cost per click versus low cost per lead strategies for Google Ads in Houston and The Woodlands",
                "caption": "A $12 click converting at 20% beats a $3 click converting at 2%.",
            },
            "lower": {
                "type": "steps",
                "title": "Six ways to lower your Google Ads costs",
                "sub": "Roughly in order of how fast they pay off",
                "steps": [["Negatives", "Cut jobs, DIY, how-to and wrong-town searches weekly."], ["Location", "Switch to Presence and trim towns you don’t serve."], ["Schedule", "Run when someone answers the phone."], ["Split by service", "One ad group and page per service."], ["Track leads", "Calls and forms as conversions for smart bidding."], ["Test ads", "Better CTR lowers what you pay per position."]],
                "alt": "Six steps to lower Google Ads cost per click for businesses in Houston and The Woodlands",
                "caption": "Most accounts we review are missing at least three of these.",
            },
        },
    },
]
