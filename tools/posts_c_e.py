"""Long-tail post: "why are my google reviews disappearing" (diagnosis, recovery, and collecting reviews that stick).

Research: top-ranking pages (Trustmary, Thrive, NiceJob, Redsearch) compared; facts verified against Google Business
Profile Help (missing or delayed reviews, profile restrictions for fake engagement, Reviews Management Tool, review
link/QR code), Google Maps contribution policy and appeals pages, Google's April 2026 Maps safety blog (2025 data),
Search Engine Land (Feb 2025 display bug; July 2026 missing-review investigation), PinMeTo (July 2026 timeline),
Search Engine Roundtable (July 2026 "Review not posted" emails), Sterling Sky (filter patterns, practitioner view),
FTC (Consumer Reviews and Testimonials Rule Q&A; Dec 2025 warning letters) and BrightLocal's 2026 consumer survey.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "missing": A("https://support.google.com/business/answer/10313341?hl=en", "Google’s help page on missing or delayed reviews"),
    "policy": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s Maps content policy"),
    "restrict": A("https://support.google.com/business/answer/14114287?hl=en", "Business Profile restrictions page"),
    "rmt": A("https://support.google.com/business/answer/4596773?hl=en", "Reviews Management Tool"),
    "appeal": A("https://support.google.com/maps/answer/16673099?hl=en", "Google’s Maps appeals page"),
    "link": A("https://support.google.com/business/answer/16816815?hl=en", "Google’s review link instructions"),
    "blog26": A("https://blog.google/products-and-platforms/products/maps/new-ways-were-protecting-businesses-on-maps/", "Google’s April 2026 Maps safety update"),
    "sel25": A("https://searchengineland.com/google-bug-cause-reviews-to-drop-out-of-local-listings-451736", "Search Engine Land"),
    "sel26": A("https://searchengineland.com/google-is-investigating-reports-of-reviews-going-missing-and-pausing-reviews-on-local-listings-481616", "Search Engine Land"),
    "pinmeto": A("https://www.pinmeto.com/news/google-reviews-missing-pause-investigation-july-2026/", "PinMeTo"),
    "ser": A("https://seroundtable.com/google-review-not-posted-email-41734.html", "Search Engine Roundtable"),
    "sterling": A("https://www.sterlingsky.ca/google-reviews-not-publishing/", "Joy Hawkins at Sterling Sky"),
    "ftcqa": A("https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers", "FTC’s own Q&A on the rule"),
    "ftcwarn": A("https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-warns-10-companies-about-possible-violations-agencys-new-consumer-review-rule", "warning letters to 10 companies"),
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
}

POSTS = [
    {
        "slug": "why-are-my-google-reviews-disappearing",
        "title": "Why Are My Google Reviews Disappearing? A Calm Diagnostic Guide",
        "seo_title": "Why Are My Google Reviews Disappearing? (2026)",
        "desc": "Why are my Google reviews disappearing? The real causes, how to diagnose yours as a Houston business, what you can recover, and how to make reviews stick.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google", "Search Console"],
        "art": "b2",
        "hero": "stars",
        "hero_alt": "Illustration of five review stars for a guide on why Google reviews are disappearing for Houston businesses",
        "related": ["complete-guide-google-reviews", "fake-reviews-rule-local-businesses", "google-business-profile-suspended-reinstatement"],
        "sections": [
            (None, f"""<p>If you’re asking “why are my Google reviews disappearing,” the most likely answer is Google’s automated spam filter. It removes reviews it thinks break policy (paid, incentivized, written by staff, or posted in suspicious patterns), and it sometimes catches real ones. Less often, the cause is a display bug, a reviewer deleting their account, a profile merge, or a restriction Google placed on your profile.</p>
<p>Each cause leaves a different fingerprint, and what you should do next depends entirely on which one you’re looking at.</p>
<p>Maybe your count dropped from 212 to 187 overnight. Or a customer swears she left five stars last Tuesday and it’s nowhere. It feels personal, especially when a competitor down Woodlands Parkway still has every one of theirs. Before you email Google or ask anyone to re-post, take ten minutes to figure out which bucket you’re in. Most of the time the answer is in Google’s own help pages and your own review history.</p>"""),

            ("Why did my Google reviews disappear? The real causes", f"""<p>Start with scale, because it explains a lot. Google says it blocked or removed more than 292 million policy-violating reviews in 2025 and took down over 13 million fake Business Profiles, according to {SRC['blog26']}. Filters at that volume make mistakes, and some land on honest shops in Spring and Conroe.</p>
<!--fig:scale-->
<p>In our experience, these are the causes, roughly from most to least common:</p>
<h3>Google’s automated filter removed them</h3>
<p>{SRC['missing']} says reviews are checked for policy compliance and are “usually removed” for violations like spam or inappropriate content. The filter also re-checks old reviews, which is why one that sat on your profile for eight months can vanish on a random Thursday.</p>
<h3>They broke a specific rule</h3>
<p>{SRC['policy']} bans reviews that were paid for “directly or in kind,” reviews from people with a conflict of interest (current or former employees, contractors, consultants), and reviews posted from multiple accounts by one person. It also bars businesses from “selectively” soliciting positive reviews.</p>
<h3>The reviewer deleted the review or their account</h3>
<p>Customers can delete their own review anytime. If someone deletes their Google account, every review they wrote goes with it, and you get no notice.</p>
<h3>Profile changes: merges, moves and reinstatements</h3>
<p>Google’s help page says reviews can take a few days to reappear after two profiles are merged, and may be removed after a profile is reinstated. If you moved and created a new profile instead of updating the old address, the reviews stayed on the old listing.</p>
<h3>A display bug, or a restriction</h3>
<p>Sometimes nothing was removed at all and the count is simply wrong for a few days. At the other end, Google can restrict a profile it believes bought reviews. Both get their own sections below.</p>"""),

            ("What Google actually says vs. what gets repeated in forums", f"""<p>Much of the advice online is pattern-spotting by people who manage hundreds of profiles. Some is useful. None of it is Google policy, so know which is which.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Claim</th><th>Status</th><th>What we’d do with it</th></tr></thead>
<tbody>
<tr><td>Paid or incentivized reviews get removed</td><td>Google policy, in writing</td><td>Stop any discount, raffle or gift card tied to reviews today</td></tr>
<tr><td>Employee and ex-employee reviews violate policy</td><td>Google policy (conflict of interest)</td><td>Ask staff not to review, and not to leave reviews for friends on their phones</td></tr>
<tr><td>Asking only happy customers is a violation</td><td>Google policy (“selectively solicit”)</td><td>Ask everyone, using the same message</td></tr>
<tr><td>Reviews written on your Wi-Fi or at an in-store tablet get filtered</td><td>Practitioner observation, not confirmed by Google</td><td>Skip review kiosks; let customers review from their own phone, later</td></tr>
<tr><td>Reviewers far from your location get filtered</td><td>Practitioner observation</td><td>Normal for tourists; nothing to fix unless the reviews aren’t real</td></tr>
</tbody></table></div>
<p>On Wi-Fi: {SRC['sterling']} has written that reviews often fail to show when Google links the network managing the listing to the network customers are on, and that onsite review stations “don’t work.” That matches what we’ve seen, but it’s a practitioner’s read of the filter, not published Google policy.</p>
<p>Take a dental office off Research Forest Drive that hands patients an iPad at checkout. Every review comes from one device, one network, minutes after a visit, in similar words. Even if every patient meant it, that looks like what the filter hunts for. We’d retire the iPad.</p>"""),

            ("Why did all my Google reviews disappear at once?", f"""<p>Losing a handful of reviews is the filter doing its periodic sweep. Losing all of them, or a rating of zero, points to something bigger.</p>
<p><b>A profile restriction for fake engagement.</b> Google’s {SRC['restrict']} lists what can happen to a profile found violating the fake engagement policy: it “will not be able to receive new reviews or ratings for set period of time,” its existing reviews “will be unpublished for set period of time,” and it may “display a warning to let consumers know that fake reviews were removed.” Google says it emails owners first, so check that inbox and its spam folder.</p>
<p><b>A spam attack on your profile.</b> Per {SRC['blog26']}, when a profile gets a sudden spike of spam reviews, Google removes them, pauses new reviews, alerts the owner and shows shoppers a banner. That can happen to an innocent business someone targeted.</p>
<p><b>A known Google problem.</b> In July 2026, owners reported counts collapsing overnight, some to zero stars, with new reviews blocked. A Google spokesperson told {SRC['sel26']}: “We are investigating the issue and will restore any reviews that were incorrectly removed.” {SRC['pinmeto']} noted many affected profiles had recently seen a burst of spam reviews.</p>
<p><b>The profile itself is gone or suspended.</b> If the whole listing disappeared, reviews aren’t really the problem. Follow our <a href="/blog/google-business-profile-suspended-reinstatement/">Google Business Profile suspension and reinstatement guide</a> first.</p>
<p>A hypothetical: a Spring roofer finishes 60 jobs in three weeks after a hailstorm and texts every homeowner the same afternoon. Forty real reviews land in ten days on a profile that normally gets four a month. That spike looks like a purchased batch. Spreading the requests over a few weeks would have been safer.</p>"""),

            ("Google reviews disappeared today? Check for a bug first", f"""<p>When many businesses lose reviews the same day, it’s usually Google’s side. Wait a few days before changing anything.</p>
<p>In February 2025, Google acknowledged that some profiles were showing lower review counts because of a display issue. Its forum statement, reported by {SRC['sel25']}, said: “The reviews themselves have not actually been removed.” The July 2026 problem was different (reviews were really pulled), but in both cases the trigger was on Google’s end.</p>
<p>To check whether it’s just you:</p>
<ul>
<li>Search your business name in a private window and compare the counts on Search and Maps. If they disagree, a display glitch is likely.</li>
<li>Check the Google Business Profile Help Community and Search Engine Roundtable for same-day reports.</li>
<li>Ask a couple of owners you know in The Woodlands or Kingwood whether their counts moved too.</li>
</ul>
<p>If it’s widespread, screenshot your count, note the date, and don’t ask customers to re-post. A wave of reposts during a filter problem can make things worse.</p>"""),

            ("Why are my Google reviews disappearing? A 10-minute diagnosis", f"""<p>When it’s only your profile, work through it in this order. Each step rules out a cause, and most owners have an answer by step four.</p>
<!--fig:diagnose-->
<p>A few details that make the steps easier:</p>
<ul>
<li><b>Know your baseline.</b> Log your count and rating every Monday. It turns “I think we lost some” into “we lost 11 between March 3 and March 10.”</li>
<li><b>Find out which reviews went.</b> Screenshot your reviews monthly. Patterns jump out fast: all from one week, all left at your counter, all from one employee’s friends.</li>
<li><b>Be honest about history.</b> A promotion that mentioned reviews, a vendor who “boosted” them, staff reviewing the business. Nobody else will see your answer.</li>
<li><b>Check email.</b> Google notifies owners before a profile restriction, and reviewers may get a “Review not posted” email when the filter removes their review, as {SRC['ser']} reported in July 2026.</li>
</ul>
<p>Once you know the likely cause, this table tells you what to expect:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Cause</th><th>What it looks like</th><th>Can they come back?</th></tr></thead>
<tbody>
<tr><td>Display bug</td><td>Many businesses affected the same day; counts differ between Search and Maps</td><td>Usually, once Google fixes it</td></tr>
<tr><td>Filter removed real reviews</td><td>A few reviews gone, often clustered by date or source</td><td>Sometimes, if the reviewer appeals</td></tr>
<tr><td>Policy violation (paid, staff, gated)</td><td>Reviews tied to a promotion or to insiders disappear</td><td>No; Google says these “won’t be restored”</td></tr>
<tr><td>Reviewer deleted it or their account</td><td>One or two reviews missing, no pattern</td><td>No, unless the customer reposts</td></tr>
<tr><td>Profile merge</td><td>Reviews missing right after duplicates were combined</td><td>Usually within a few days</td></tr>
<tr><td>Profile restriction</td><td>Email from Google, warning banner, new reviews blocked</td><td>After the set period, or via appeal</td></tr>
</tbody></table></div>"""),

            ("Can you get deleted Google reviews back?", f"""<p>Sometimes. It depends on who removed them and why, and owners have fewer tools than they expect.</p>
<p><b>Reviews removed for policy violations.</b> Google’s help page says these “won’t be restored.” If they were incentivized or written by staff, let them go.</p>
<p><b>Real reviews the filter caught by mistake.</b> The appeal belongs to the reviewer, not to you. Google’s {SRC['appeal']} says content removals can be tracked and appealed from the contributor’s own Google Maps profile, that a removal can only be appealed once, and that appeals are only available for certain violations and accounts. If a customer’s review vanished, point her to the “Review not posted” email or her Maps profile.</p>
<p><b>The appeal tool owners do get.</b> The {SRC['rmt']} lets you report a review on your profile for removal, track its status, and file a one-time appeal (up to 10 reviews at a time) if Google decides a review you flagged doesn’t violate policy. It’s for taking bad reviews down, not restoring your own. For those, Google just says to contact support.</p>
<p><b>Profile restrictions.</b> The restrictions page links to an appeal form where Google re-reviews the profile and any context you provide. If reviews were bought, stop that before you appeal. If you did nothing wrong, say so plainly and include proof.</p>
<p>Before contacting support, pull this together:</p>
<!--fig:evidence-->
<p>Set expectations: support can confirm a bug or escalate a restriction review, but it rarely explains why one specific review was filtered.</p>"""),

            ("Where the FTC’s fake reviews rule fits in", f"""<p>The FTC’s Consumer Reviews and Testimonials Rule took effect October 21, 2024. It bans fake reviews, incentives conditioned on a positive (or negative) review, undisclosed insider reviews, and review suppression. In December 2025 the FTC sent {SRC['ftcwarn']} it suspected of violating the rule, noting penalties of up to $53,088 per violation. We broke the rule down in our <a href="/blog/fake-reviews-rule-local-businesses/">guide to the FTC fake reviews rule</a>.</p>
<p>The part that trips owners up: Google is stricter than the FTC. The {SRC['ftcqa']} allows a disclosed incentive for a review as long as it isn’t tied to a positive or negative rating. Google bans incentives for reviews, full stop.</p>
<p>So “$10 off your next visit for any review, good or bad” can be legal under federal law and still get your reviews removed and your profile restricted. For Google reviews, follow Google’s rule.</p>
<p>Review gating is similar. The FTC says asking only happy customers “could violate the FTC Act,” and Google bans selectively soliciting positive reviews. Software that sends 5-star customers to Google and everyone else to a private form is exactly what both warn about.</p>"""),

            ("How to collect Google reviews that stick", f"""<p>The habits that keep reviews from being filtered also get you more of them. The full playbook is in <a href="/blog/complete-guide-google-reviews/">our complete guide to Google reviews</a>; here’s the version tuned for keeping them.</p>
<!--fig:stick-->
<h3>Use Google’s own link</h3>
<p>Per {SRC['link']}, sign in at business.google.com, choose <b>Read reviews</b>, then <b>Get more reviews</b>, and copy the link or download the QR code (the QR code only generates on a computer). Use it in texts, receipts and email signatures, and skip “review us” pages that pre-filter by star rating.</p>
<h3>Ask everyone, the same way</h3>
<p>One neutral message to every customer: “Thanks for choosing us. If you have a minute, we’d appreciate an honest review on Google.” No “if you were happy,” no “5 stars helps us,” no suggested wording.</p>
<h3>Let them review later, on their own phone</h3>
<p>For a Woodlands restaurant, that’s a text the next morning instead of a QR code on the check presenter scanned on your Wi-Fi. For a home service company, it’s a text after the tech leaves the driveway.</p>
<h3>Keep the pace steady</h3>
<p>Ten reviews a month beats 40 in one week. A spike is exactly the pattern Google’s spam systems react to, and a steady pace also means your newest review is never months old, which is the first thing a shopper scrolling on Maps sees. Build the ask into a routine (every invoice, every completed job) instead of running review drives.</p>
<h3>Keep staff and family out of it</h3>
<p>No reviews from employees, ex-employees, spouses, or the friend who did your logo. That’s a conflict of interest under Google’s policy, and the filter is good at spotting it.</p>
<p>And vet any vendor promising “50 five-star reviews a month.” Google restricts your profile, not theirs. Reviews also feed rankings, so if your count is sliding, read <a href="/blog/rank-in-google-map-pack-houston/">how to rank in the Google Map Pack in Houston</a> too.</p>"""),

            ("Start a review log today", f"""<p>The most useful thing you can do in the next five minutes costs nothing. Open a spreadsheet, write today’s date, your review count and your star rating, and screenshot your ten newest reviews. Do it again every Monday. The next time reviews disappear, you’ll know exactly which ones, when, and whether the drop lines up with something you changed. That turns a vague support ticket into one Google can act on.</p>
<p>Watch your ad costs in the same weeks. Google’s <a href="https://support.google.com/localservices/answer/7527305?hl=en" target="_blank" rel="noopener">Local Services Ads ranking page</a> lists your rating and number of reviews as ranking factors, so a profile that loses a chunk of reviews can see lead costs creep up before anyone connects the two. If you run Google or Meta ads and want to know whether something like that is happening, request our free <a href="/contact/">Ad Spend Leak Check</a>. We record a 10-minute walkthrough of the account showing where money is slipping, delivered within 48 hours. For the profile itself, we handle Business Profiles for businesses across The Woodlands, <a href="/digital-marketing-agency-spring-tx/">Spring</a>, <a href="/digital-marketing-agency-conroe-tx/">Conroe</a> and Greater Houston as part of our <a href="/services/web-design-seo-pr/">local SEO work</a>.</p>"""),
        ],
        "faq": [
            ("Why are my Google reviews missing after a customer says they posted one?",
             "New reviews are checked for policy compliance before they appear, which Google says can take a few days. If it never shows, the filter likely held it back, often because it was posted on your premises or came during a burst of reviews. The customer may receive a Review not posted email and can appeal once from their own Google Maps profile."),
            ("Can you get deleted Google reviews back?",
             "Only in some cases. Reviews hidden by a Google bug usually return once it is fixed, and merged profiles show their reviews again within a few days. Real reviews removed by the filter can be appealed once by the reviewer, not the business. Reviews removed for policy violations, such as paid or employee reviews, will not be restored, and reviews a customer deletes are gone unless they post again."),
            ("Why did all my Google reviews disappear overnight?",
             "Losing every review at once usually means a profile restriction for fake engagement, a pause after a spam attack, a widespread Google problem, or a suspended or merged profile. Check the email tied to your profile for a restriction notice, look for a warning banner, and search the Help Community for same-day reports."),
            ("Does Google remove reviews from employees or people on the same Wi-Fi?",
             "Google's policy prohibits reviews from current or former employees and anyone with a conflict of interest, so those can be removed. The Wi-Fi part is not written Google policy. Experienced local SEO practitioners report that reviews posted on a business's own network or at in-store kiosks are often filtered, so it is safer to let customers review later from their own phones."),
            ("Can I offer a discount for an honest Google review?",
             "No, not for Google reviews. The FTC allows incentives that are not tied to a positive review and are disclosed, but Google's policy bans offering free or discounted goods or services in exchange for reviews of any kind. Incentivized reviews get removed, and a pattern of them can get your profile restricted, with new reviews blocked and a warning shown to shoppers."),
        ],
        "figures": {
            "scale": {
                "type": "stats",
                "title": "Google’s review filter works at huge scale",
                "stats": [
                    ["292M", "policy-violating reviews blocked or removed by Google in 2025"],
                    ["13M+", "fake Business Profiles Google removed in 2025"],
                    ["782K", "accounts Google put posting restrictions on in 2025"],
                    ["1B+", "helpful reviews Google published in 2025"],
                ],
                "note": "Source: Google Maps safety update (April 2026)",
                "alt": "Stat tiles showing Google removed 292 million reviews in 2025, context for why Google reviews are disappearing",
                "caption": f"For every review Google pulled in 2025, it published more than three, per its {SRC['blog26']}.",
            },
            "diagnose": {
                "type": "steps",
                "title": "Why did my reviews disappear? Check in order",
                "sub": "Most owners find the cause by step four",
                "steps": [
                    ["Rule out a Google bug", "Compare counts on Search and Maps, and check the Help Community and SEO news for same-day reports."],
                    ["Check your email", "Look for a Google restriction notice or ask customers about a Review not posted email."],
                    ["Find which reviews went", "Compare against last month’s screenshot. Look for clusters by date, source or reviewer."],
                    ["Match them to your history", "Promotions, staff reviews, kiosks, a review vendor or a sudden spike of requests."],
                    ["Check for profile changes", "Recent merges, duplicate removals, address moves or a reinstatement."],
                    ["Act on the cause", "Wait out bugs, stop violations, have reviewers appeal, or appeal a restriction."],
                ],
                "alt": "Six-step diagnostic flow for working out why Google reviews are disappearing from a Houston business profile",
                "caption": "Work top to bottom; each step rules out a cause before you change anything.",
            },
            "evidence": {
                "type": "checklist",
                "title": "What to gather before contacting Google support",
                "sub": "Specifics get answers; “my reviews are gone” doesn’t",
                "items": [
                    "Before-and-after review counts with dates",
                    "Screenshots of the missing reviews, if you have them",
                    "Reviewer names and roughly when each was posted",
                    "Any Google emails about restrictions or removals",
                    "Proof the customers are real: invoices or appointment records",
                    "Dates of recent profile edits, merges or moves",
                    "Your review request message and how it was sent",
                ],
                "alt": "Checklist of evidence a Woodlands business should gather before asking Google support about missing reviews",
                "caption": "Keep customer records private; you only need to show they exist if Google asks.",
            },
            "stick": {
                "type": "compare",
                "title": "Review asks that get filtered vs. ones that stick",
                "left": {
                    "title": "Likely to vanish",
                    "items": [
                        "Tablet or QR code at the counter, on your Wi-Fi",
                        "Discount or raffle entry for a review",
                        "Only asking customers who seemed happy",
                        "40 requests sent the same afternoon",
                        "Staff and family reviewing the business",
                    ],
                },
                "right": {
                    "title": "Built to stick",
                    "items": [
                        "Text with Google’s own link, sent the next day",
                        "No incentive of any kind",
                        "Same neutral message to every customer",
                        "Steady weekly pace all year",
                        "Reviews only from real, unrelated customers",
                    ],
                },
                "alt": "Comparison of review requests that disappear from Google versus ones that stick for The Woodlands businesses",
                "caption": "The left column describes patterns Google’s policy or its filter targets; the right is what we set up for clients.",
            },
        },
    },
]
