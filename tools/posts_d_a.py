"""Long-tail post: "google business profile video verification" (shot list, rejections, fallbacks, special cases).

Research: Google Business Profile Help pages fetched and confirmed (video verification requirements and steps
#14271705; verification methods and timing #7107242; verification status #15698162; guidelines for representing
your business #3038177 incl. virtual offices and co-working; service-area businesses #9157481; bulk verification
#4490296; appeals #13597551; edit profile #3039617). Competitor/vendor pages read: Local Falcon, UENI help,
Digital Shift Media example, Whitespark. Search Engine Land (video previews). Local Search Forum threads (Sept and
Nov 2025) on "No more ways to verify" and the verification status tool's Contact us route (moderator advice,
framed as practitioner reports, not Google policy).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "video": A("https://support.google.com/business/answer/14271705?hl=en", "Google’s video verification help page"),
    "video2": A("https://support.google.com/business/answer/14271705?hl=en", "the same help page"),
    "methods": A("https://support.google.com/business/answer/7107242?hl=en", "Google’s main verification page"),
    "status": A("https://support.google.com/business/answer/15698162?hl=en", "verification status page"),
    "guide": A("https://support.google.com/business/answer/3038177?hl=en", "guidelines for representing your business"),
    "sab": A("https://support.google.com/business/answer/9157481?hl=en", "service-area business help page"),
    "bulk": A("https://support.google.com/business/answer/4490296?hl=en", "bulk verification page"),
    "appeals": A("https://support.google.com/business/answer/13597551?hl=en", "appeals help page"),
    "edit": A("https://support.google.com/business/answer/3039617?hl=en", "Google’s editing instructions"),
    "sel": A("https://searchengineland.com/video-previews-come-to-google-business-profile-verfication-454471", "Search Engine Land"),
    "ueni": A("https://help.ueni.com/en/articles/13141745-how-to-complete-video-verification-for-a-google-business-profile", "UENI’s help doc"),
    "lsf1": A("https://localsearchforum.com/threads/no-more-ways-to-verify-google-business-profile-error-message.62905", "a Local Search Forum moderator"),
    "lsf2": A("https://localsearchforum.com/threads/verification-needed-no-other-options-available.62744/", "another thread"),
}

# Sibling posts in this batch (absolute URLs so the validator doesn't need them built yet).
SIB = {
    "move": '<a href="/blog/change-business-address-google-without-suspension/">changing your address on Google without a suspension</a>',
    "lsa": '<a href="/blog/google-guaranteed-vs-google-verified/">Google Verified badge guide</a>',
}

POSTS = [
    {
        "slug": "google-business-profile-video-verification",
        "title": "Google Business Profile Video Verification: A Shot List That Passes",
        "seo_title": "Google Business Profile Video Verification Guide",
        "desc": "Google Business Profile video verification, step by step: what Google wants on camera, why videos fail, and fixes for Houston home-based and service-area pros",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google", "Search Console"],
        "art": "b5",
        "hero": "phone",
        "hero_alt": "Illustration of a phone recording a clip for Google Business Profile video verification by a Houston-area business",
        "related": ["google-business-profile-number-one-asset", "google-business-profile-suspended-reinstatement", "get-found-near-me-google"],
        "sections": [
            (None, f"""<p>Google Business Profile video verification is one unedited clip, at least 30 seconds long, recorded live inside your Business Profile on a phone. It has to show where the business is, that the business exists, and that you’re the one in charge of it. Google says it reviews the video within up to 5 business days and tells you what was missing if it turns you down.</p>
<p>Plenty of owners are on their third or fourth take before one sticks.</p>
<p>The trouble is that Google wrote the instructions for a shop with a sign over the door. A plumber working out of a house in Spring, or a mobile groomer in Cypress with a van and no lobby, has to guess what “show your location” means when the location is a cul-de-sac. What follows is the version we’d hand a client before they hit record.</p>"""),

            ("Google Business Profile video verification requirements", f"""<p>{SRC['video']} breaks the video into separate proofs, worded a little differently for storefronts than for service-area businesses.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Proof</th><th>Storefront or hybrid business</th><th>Service-area business (no customer-facing location)</th></tr></thead>
<tbody>
<tr><td>Location</td><td>Street signs, building numbers or nearby familiar places that match your spot on Google Maps</td><td>Street signs, landmarks or other identifiers at your business address; home-based businesses can film nearby landmarks and signs</td></tr>
<tr><td>Business exists</td><td>Storefront, showroom or signage with the business name on a permanent fixture, matching your profile</td><td>Professional tools, equipment, workspace, business cards or branded apparel</td></tr>
<tr><td>Proof of management</td><td>Things only staff can do: opening the register, entering the kitchen or stockroom, using the point-of-sale system</td><td>Performing a service, accessing business-only assets like a branded van, or showing a permit, invoice or utility bill that matches your profile name</td></tr>
</tbody></table></div>
<p>The clip itself has its own rules. It must be recorded live (no pre-recorded or offline clips), unedited, unique and complete with no breaks, at least 30 seconds long, and recorded and uploaded from a mobile device through your Business Profile. It must not show sensitive information such as bank account, tax or ID numbers, private information about you or others, or other people’s faces.</p>
<p>“No breaks” means you can’t pause, walk out to the truck and resume. “Other people’s faces” means a customer at the counter can sink an otherwise perfect take.</p>
<p>One more line on that page catches people out: online-only businesses aren’t eligible for a Business Profile at all.</p>"""),

            ("How video verification works in the app and on desktop", f"""<p>The recording has to happen on a phone. Google’s steps, from {SRC['video2']}:</p>
<ol>
<li>On your mobile device, open your Business Profile.</li>
<li>Tap <b>Get verified</b>. You may need to enter your phone number first.</li>
<li>Tap <b>Business video</b>, then <b>Next</b>.</li>
<li>Read the requirements and allow access to location, camera and microphone.</li>
<li>Tap <b>Next</b>, then <b>Start recording</b>. Tap stop when you’re done.</li>
<li>Watch it back. Tap <b>Try again</b> to re-record if anything is missing.</li>
<li>Tap <b>Upload video</b>.</li>
</ol>
<p>To find your profile on the phone, {SRC['edit']} say to open the Google Maps app and tap <b>Business</b> at the bottom right, or use business.google.com in the phone’s browser. Sign in with the account that owns the profile. A lot of first attempts die right here, on a personal Gmail, while the profile actually lives under the office manager’s account.</p>
<p>If you start on a computer, you’ll get as far as choosing the method and then need your phone. {SRC['ueni']} describes scanning a QR code from the desktop screen with a phone signed in to the same account. Google reshuffles this screen often, so go with whatever it shows you.</p>
<p>Google added a preview before submitting, reported by {SRC['sel']}. Use it. If you can’t read your own van lettering on playback, neither can the reviewer.</p>"""),

            ("A video verification example: the Spring plumber with a wrapped van", f"""<p>Say you run a one-truck plumbing company out of your house in a Spring subdivision off Kuykendahl. No storefront. Your address is hidden on your profile, as it should be (more on that below). Your van is wrapped with the business name and phone number, and you keep your tools in the van and the garage.</p>
<p>We’d script about 90 seconds. That’s three times the minimum, and it gives you room to move slowly.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Time</th><th>Shot</th><th>Proves</th></tr></thead>
<tbody>
<tr><td>0:00-0:15</td><td>Start at the corner street sign nearest your house, then pan to the subdivision entrance or another fixed landmark. Walk toward the house.</td><td>Location</td></tr>
<tr><td>0:15-0:30</td><td>Walk up the driveway to the van. Hold steady on the business name on both sides and the back doors for a few seconds each.</td><td>Business exists</td></tr>
<tr><td>0:30-0:50</td><td>Open the van with your keys. Show organized tools, a pipe threader, fittings bins, the water heater dolly.</td><td>Management and tools of the trade</td></tr>
<tr><td>0:50-1:10</td><td>Pull a blank invoice or business card from the console and a utility bill or permit with the business name on it. Keep account numbers covered with your thumb.</td><td>Management (documents)</td></tr>
<tr><td>1:10-1:30</td><td>Open the garage with the remote, show stock and equipment, and finish on a branded shirt or hat hanging up (or a quick mirror shot of you in it).</td><td>Business exists, workspace</td></tr>
</tbody></table></div>
<p>Look at what we left out. No customer’s house, which films someone else’s property and maybe their face. No neighbor waving from the next driveway. No driver’s license close-up.</p>
<p>Film in daylight, early, before the July heat and before the neighbors are out walking dogs. Wash the van first. A wrap under a coat of yellow pine pollen is hard to read on a phone screen.</p>
<p>If Google comes back saying the location was weak, start wider next time: the subdivision monument sign, two street signs instead of one, a longer walk to the house.</p>
<!--fig:shots-->"""),

            ("Video verification guidelines for home-based, co-working and multi-location businesses", f"""<p>If the listing type is wrong for how you operate, no video will save it.</p>
<h3>Home-based and service-area businesses</h3>
<p>Google’s {SRC['guide']} uses a plumber as the example: if you run the business from home and don’t serve customers there, clear the address from the profile and list service areas instead (the {SRC['sab']} has the limits). Google still sees the address during verification. Customers don’t.</p>
<p>For the video, that means the van, the garage and the paperwork carry the weight. If you’re converting an old storefront listing to service-area at the same time, do that edit first and let it settle; our guide to {SIB['move']} explains why stacking changes is risky.</p>
<h3>Co-working spaces and virtual offices</h3>
<p>No setup causes more grief than this one. Google’s guidelines say a rented mailing address you don’t operate from isn’t eligible, that P.O. boxes or mailboxes at remote locations aren’t acceptable, and that a co-working office only qualifies if it maintains clear signage and receives customers there during business hours. Service-area businesses can’t list a virtual office unless it’s staffed during business hours.</p>
<p>In practice, a co-working office off Six Pines Drive can work if your name is on the door, you’re there during listed hours and clients meet you there. A mail suite on FM 1960 won’t, and putting it on camera invites a closer look at everything else on the profile.</p>
<h3>Multi-location businesses</h3>
<p>Google’s {SRC['bulk']} allows bulk verification for 10 or more locations of the same business, through Business Profile Manager under <b>Verifications</b>, then <b>Chain</b>. Service-area businesses don’t qualify. A three-office dental group in The Woodlands, Conroe and Kingwood verifies each office separately, usually with a video at each, filmed by someone with keys.</p>"""),

            ("Why verification videos get rejected (and what “couldn’t verify” means)", f"""<p>Google doesn’t publish rejection statistics. This list is built from its stated requirements plus the failure patterns practitioners report.</p>
<ul>
<li><b>The name doesn’t match.</b> The van says “Gulf Coast Plumbing,” the profile adds “&amp; Drain Services Spring TX.” Signage, documents and profile name should agree.</li>
<li><b>The location can’t be tied to the map.</b> Close-ups of a garage door could be anywhere. Wide shots of street signs can’t.</li>
<li><b>No proof you’re in charge.</b> Walking past a building is not the same as opening it with your own keys.</li>
<li><b>It was cut, paused or uploaded from the camera roll.</b> Google wants one live take recorded in the profile.</li>
<li><b>Private details on screen.</b> Account numbers, ID cards, customer names on a work order, a customer’s face.</li>
<li><b>Shaky, dark or rushed.</b> Signs filmed at walking pace blur.</li>
</ul>
<!--fig:compare-->
<p>What the messages mean, using Google’s wording. A <b>Review issues</b> notice means the video wasn’t accepted. Google says it shares the reasons, and you fix them by tapping Review issues, then recording a new video that includes everything from the first one plus what was missing. If the <b>Get verified</b> button reappears, the {SRC['status']} says Google couldn’t completely verify the business, and you can retry or pick a different method if one is offered.</p>
<p>Neither is a suspension. That’s a separate process, covered further down.</p>"""),

            ("Verification video not uploading? Try this first", f"""<p>Google’s advice for a failed upload is one line: try again. Here’s what we’d check, roughly in this order:</p>
<ol>
<li><b>Don’t cancel.</b> Google’s help page says if you cancel the upload, you and Google both lose access to the video. Let it sit.</li>
<li><b>Get on solid Wi-Fi.</b> A 90-second video is a large file, and one bar of LTE at the end of a cul-de-sac is a common culprit.</li>
<li><b>Keep the screen on and the app in front.</b> Switching apps or letting the phone lock can stall the upload.</li>
<li><b>Update the app and check permissions.</b> Free some storage, and confirm camera, microphone and location are allowed.</li>
<li><b>Re-record if the upload truly dies.</b> You can’t attach a saved file, so a new live take is the only way back.</li>
</ol>
<p>If the app crashes on Business video every time, switch routes: Maps app instead of the browser, or the reverse.</p>"""),

            ("Google business video verification not working? What to do next", f"""<p>After two rejections, stop re-shooting the same video. Read the reasons. If Google flagged location, a third lap around the van won’t change anything. If you keep failing, or the screen says “No more ways to verify,” work down this list:</p>
<!--fig:fallback-->
<p>Google’s {SRC['methods']} says live video calls aren’t available for every business and are only offered during local business hours. A rep has you show location and proof of management in real time, which is often easier for home-based owners because you can answer questions.</p>
<p>When the profile shows no options at all, {SRC['lsf1']} reported in November 2025 that Google’s verification status tool has become the main way in: click through to the end and choose <b>Contact us</b>, and you may be offered a live video call. In {SRC['lsf2']}, the same moderator suggested having signage photos, a utility bill, LLC or DBA paperwork, a license, and an email address on your business domain ready. That’s practitioner advice, not Google policy, but it’s the same pile of documents we’d collect. In Texas, a sole proprietor’s assumed name certificate from the county clerk is a good document to have scanned.</p>
<p>Whatever you do, don’t open a second profile to start over. Duplicates are a fast route to a suspension.</p>
<h3>If the profile is suspended, not just unverified</h3>
<p>That goes through Google’s appeals tool instead. Per the {SRC['appeals']}, decisions can take up to five working days, you shouldn’t file multiple appeals for the same issue, and evidence must be uploaded within 60 minutes of submitting. Our <a href="/blog/google-business-profile-suspended-reinstatement/">suspension and reinstatement guide</a> walks through it step by step.</p>
<p>While you’re stuck, expect “Google verification” sales calls. Google doesn’t charge to verify. See <a href="/blog/google-business-listing-scam-calls/">Google Business listing scam calls</a>.</p>"""),

            ("Google Business Profile verification without video", f"""<p>You can’t choose your method. Google’s main verification page says the methods “are automatically determined by Google and can’t be changed,” based on business type, public information, region and hours, and you may need more than one. If video is the only option on your screen, that’s the option.</p>
<p>If other options do show up, this is what each one involves:</p>
<ul>
<li><b>Phone or text:</b> a code by call or SMS. Phone trees (IVR) can’t receive it, so use a number that rings a person.</li>
<li><b>Email:</b> sent to the address shown on the verification screen, which you need access to.</li>
<li><b>Postcard:</b> a 5-digit code by mail. Google says it usually arrives within 14 days and expires after 30. Requesting another one cancels the first, so be patient.</li>
<li><b>Live video call:</b> covered above, not always offered.</li>
<li><b>Instant verification:</b> sometimes available if you’ve already verified your website in Google Search Console, or through bulk verification.</li>
</ul>
<!--fig:timeline-->
<p>Verify your site in Search Console regardless. It costs nothing and it’s part of the basic setup in <a href="/blog/google-business-profile-number-one-asset/">why your Google Business Profile is your number one asset</a>.</p>"""),

            ("After you’re verified, don’t trip it again", f"""<p>Google warns that changes to business info may trigger re-verification, so if a move or rebrand is coming, read our guide to {SIB['move']} first. Day to day, add managers through the profile’s user settings instead of sharing the owner login, and keep the shot list. You’ll want it again.</p>
<p>If you plan to run Local Services Ads, a verified profile is one of the screening steps, and our {SIB['lsa']} covers the rest. For organic visibility, ranking for “plumber near me” in Spring or Tomball comes down to categories, reviews, photos and your website; our guide on <a href="/blog/get-found-near-me-google/">getting found for “near me” searches</a> starts there.</p>
<p>Before you open the app again, write the shot list on an index card and walk the route once with the phone in your pocket. Our <a href="/services/web-design-seo-pr/">local SEO team</a> sets up and verifies profiles for service businesses across <a href="/digital-marketing-agency-spring-tx/">Spring</a>, The Woodlands and <a href="/service-areas/">Greater Houston</a> if you’d rather hand it off.</p>
<p>One thing to line up while you wait on Google: if you already pay for search ads, check where those clicks come from. A profile that lists six service areas next to an ad campaign targeting all of Harris County is a common mismatch. Ask us for a free <a href="/contact/">Ad Spend Leak Check</a> and we’ll record a short walkthrough of your Google Ads account showing the clicks landing outside the area you actually serve.</p>"""),
        ],
        "faq": [
            ("How long does Google Business Profile video verification take?",
             "Google says it reviews verification videos within up to 5 business days, and occasionally longer. You'll get a notification and email when the business is verified. If the video doesn't meet the requirements, you'll see a Review issues notice with the reasons, and you can record and upload a new video that covers everything the first one did plus what was missing."),
            ("Can I verify a home-based business without showing my home address?",
             "Yes. A home-based service business should remove its address from the profile and list service areas instead. The verification video still needs to show where you operate, so start at nearby street signs and landmarks, then show your branded vehicle, tools and a document with the business name. The address stays hidden from customers on Google even though Google sees it during verification."),
            ("Can I upload a pre-recorded video for Google verification?",
             "No. Google requires the video to be recorded live through your Business Profile on a mobile device, in one continuous take with no edits or breaks, and at least 30 seconds long. Clips from your camera roll, edited compilations and screen recordings aren't accepted. You can preview the recording before uploading and tap Try again to re-record if something is missing."),
            ("Does Google allow a virtual office or co-working space on a Business Profile?",
             "Only in limited cases. Google says a rented mailing address you don't operate from isn't eligible, and remote mailboxes aren't acceptable. A co-working office can qualify if it has clear signage and you receive customers there during business hours. Service-area businesses can't list a virtual office unless it's staffed during business hours."),
            ("What if video verification is the only option and it keeps failing?",
             "Read the rejection reasons and fix that specific gap, usually location shots or proof of management, then record a fresh take. If it still fails or no options remain, use Google's verification status tool and its Contact us option, where you may be offered a live video call. Have a utility bill, business registration and signage photos ready. Don't create a duplicate profile."),
        ],
        "figures": {
            "shots": {
                "type": "checklist",
                "title": "Shot list for a home-based service business",
                "sub": "One take, in this order",
                "items": [
                    "Nearest street sign and a fixed landmark",
                    "Walk to the house without cutting",
                    "Business name on the van, both sides and rear",
                    "Open the locked van with your keys",
                    "Tools and equipment of your trade",
                    "Invoice, permit or utility bill with the business name",
                    "Account numbers and ID covered",
                    "Garage or workspace with stock",
                    "Branded shirt or hat",
                    "No customers, neighbors or faces in frame",
                ],
                "alt": "Checklist shot list for Google Business Profile video verification by a home-based Spring TX service business",
                "caption": "A plan for a hypothetical Spring plumber; swap in the tools of your own trade.",
            },
            "compare": {
                "type": "compare",
                "title": "Videos that get rejected vs. videos that pass",
                "left": {
                    "title": "Likely rejected",
                    "items": [
                        "Close-up of a garage door, no street context",
                        "Van name differs from profile name",
                        "Walks past the building, never opens it",
                        "Paused mid-take or uploaded from camera roll",
                        "Customer’s face or account numbers on screen",
                    ],
                },
                "right": {
                    "title": "Built to pass",
                    "items": [
                        "Opens on street signs and a fixed landmark",
                        "Name matches signage, van and documents",
                        "Opens the van, office or register with keys",
                        "One live take, previewed before upload",
                        "No faces, private documents covered",
                    ],
                },
                "alt": "Comparison of Google Business Profile verification videos that get rejected versus pass for Woodlands businesses",
                "caption": "Left column reflects Google’s stated requirements and common failure patterns we see.",
            },
            "fallback": {
                "type": "steps",
                "title": "When video verification keeps failing",
                "sub": "Work through these before starting over",
                "steps": [
                    ["Read the Review issues reasons", "Fix the specific gap: location, business proof or management."],
                    ["Record a fuller new take", "Everything from the first video plus what was missing."],
                    ["Check for other methods", "Phone, text, email, postcard or a live video call if offered."],
                    ["Use the status tool’s Contact us", "Ask about a live video call; have documents ready."],
                    ["Suspended? Use the appeals tool", "A different process with its own evidence window."],
                ],
                "alt": "Steps to take when Google business video verification is not working for a Houston area service business",
                "caption": f"Step four follows practitioner reports from {SRC['lsf1']}, not a published Google policy.",
            },
            "timeline": {
                "type": "bars",
                "title": "Google’s stated verification time windows",
                "sub": "Days, from Google Business Profile Help",
                "items": [
                    ["Video review", 7, "Up to 5 business days"],
                    ["Appeal decision", 7, "Up to 5 working days"],
                    ["Postcard arrival", 14, "Usually within 14 days"],
                    ["Postcard code expires", 30, "After 30 days"],
                ],
                "highlight": [0],
                "note": "Source: Google Business Profile Help",
                "alt": "Bar chart of Google Business Profile video verification review time compared with postcard and appeal timelines",
                "caption": f"Business-day windows shown as roughly seven calendar days; figures from {SRC['methods']} and the {SRC['appeals']}.",
            },
        },
    },
]
