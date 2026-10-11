"""Long-tail post: "google business profile suspended after changing address" (preventing suspension when moving,
renaming, or switching to a service-area business).

Research: forum threads that rank for the query (Local Search Forum, Google Business Profile Help Community) and
practitioner guides compared. Facts verified against Google Business Profile Help (Edit your Business Profile; Move your
reviews across Business Profiles; Resolve duplicate profiles; Guidelines for representing your business, incl. the
Rebranding section and name examples; Verify your business, incl. live video requirements and the 5-business-day review;
Manage your service areas; Mark your business as closed), Whitespark's moving guide (postcard timing, order of
operations), BrightLocal's suspension guide (risk factors, call-drop claim), Local Search Forum threads (2022-2023) and
COGENCY GLOBAL on Texas HB 3609 assumed-name filings.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "edit": A("https://support.google.com/business/answer/3039617?hl=en", "Google’s “Edit your Business Profile” page"),
    "reviews": A("https://support.google.com/business/answer/3098204?hl=en", "Google’s page on moving reviews across profiles"),
    "dupes": A("https://support.google.com/business/answer/12755979?hl=en", "Google’s duplicate-profile help page"),
    "guide": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s guidelines for representing your business"),
    "verify": A("https://support.google.com/business/answer/7107242?hl=en", "Google’s verification help page"),
    "sab": A("https://support.google.com/business/answer/9157481?hl=en", "Google’s service-area help page"),
    "closed": A("https://support.google.com/business/answer/15300196?hl=en", "Google’s page on marking a business closed"),
    "ws": A("https://whitespark.ca/?p=4477", "Whitespark’s moving guide"),
    "bl": A("https://www.brightlocal.com/learn/google-business-profile/optimization/google-business-profile-suspensions/", "BrightLocal’s suspension guide"),
    "lsf_tree": A("https://localsearchforum.com/threads/can-a-business-keep-its-reviews-after-a-nap-change-and-suspension.60238/latest", "a 2023 Local Search Forum thread"),
    "lsf_new": A("https://localsearchforum.com/threads/moved-to-new-location-need-to-move-reviews-gb-support-keeps-ignoring-requests.60162/", "another Local Search Forum thread"),
    "lsf_moved": A("https://localsearchforum.com/threads/is-google-marking-businesses-as-moved-anymore.58518/latest", "practitioners on Local Search Forum"),
    "hb3609": A("https://cogencyglobal.com/blog/changes-to-county-level-assumed-name-filing-requirements-in-texas", "Texas HB 3609"),
}

# Sibling posts in this batch (absolute URLs so the validator doesn't need them built yet).
SIB = {
    "video": '<a href="/blog/google-business-profile-video-verification/">video verification guide</a>',
    "lsa": '<a href="/blog/google-guaranteed-vs-google-verified/">Google Verified badge</a>',
}

POSTS = [
    {
        "slug": "change-business-address-google-without-suspension",
        "title": "Google Business Profile Suspended After Changing Address? How to Avoid It",
        "seo_title": "Google Business Profile Suspended After Changing Address?",
        "desc": "Google Business Profile suspended after changing address? The safe order for moving, renaming or going service-area in Houston, without losing reviews.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google", "Yelp"],
        "art": "b3",
        "hero": "search",
        "hero_alt": "Illustration of a Google search and map listing for a guide on changing a business address on Google without suspension",
        "related": ["google-business-profile-suspended-reinstatement", "how-to-rebrand-without-losing-customers", "local-seo-checklist-the-woodlands"],
        "sections": [
            (None, f"""<p>A Google Business Profile suspended after changing address usually means Google couldn’t confirm the new details were real. Moving or renaming forces a fresh review, and suspensions tend to follow edits that arrive before the website, signage and paperwork agree with them, or several big edits made at once. Update the real world first, change one thing on the existing profile, re-verify, then leave it alone.</p>
<p>Already suspended? Jump to the second-to-last section, and keep our {'<a href="/blog/google-business-profile-suspended-reinstatement/">reinstatement walkthrough</a>'} open for the appeal itself. Everything else here is about getting through a move or rename without needing it.</p>"""),

            ("Why Google suspends profiles after an address or name change", f"""<p>The rules are written down. {SRC['edit']} says Google reviews your changes “before we update them live on your profile.” It also says that if you move to a new address after verification, “you must verify your business again,” and that after a name change “you might need to verify your business again.” A re-verification prompt after a move is expected. It doesn’t mean anything is wrong.</p>
<p>A suspension is Google deciding the profile may not represent a real business at a real location. {SRC['bl']} lists the patterns that raise the odds: an address or hours that don’t match your website, keyword stuffing in the name, switching from a storefront to a service-area business, and lots of edits in a short window. BrightLocal also estimates calls can fall by as much as 90% while a profile is suspended.</p>
<p>The usual ways a move goes wrong:</p>
<ul>
<li>The owner changes the Google address the week the lease is signed, while the new space is still drywall and no sign.</li>
<li>The name, address and phone all change in the same sitting. {SRC['lsf_tree']} describes a tree service that did exactly this to keep roughly 150 reviews and ended up suspended, with a denied first appeal.</li>
<li>The new address is a virtual office or an unstaffed coworking desk, which {SRC['guide']} say isn’t eligible.</li>
<li>Someone creates a brand-new profile at the new address, leaving two listings for one business.</li>
<li>The website still shows the old suite number for a month after Google has the new one.</li>
</ul>
<p>Every one of those is a sequencing mistake, which means every one is avoidable.</p>"""),

            ("How to change business address on Google without losing reviews", f"""<p>The short answer: edit the address on the profile you already have. Don’t make a new one.</p>
<p>{SRC['dupes']} is blunt about it: “If your business relocates, do not create a new Business Profile for the new location.” And {SRC['reviews']} explains why that matters for your reputation: “If you move to a new address and keep the same business name, Google will transfer your reviews automatically.” The exceptions Google names are categories like hotels, golf courses and scenic attractions, where reviews describe the place itself.</p>
<p>Reviews stay with the profile as long as you move it instead of replacing it. The order we work in:</p>
<!--fig:order-->
<ol>
<li><b>Before moving day, clean up the new address.</b> Search Google Maps for the new street address and suite. If a previous tenant’s listing is still there, suggest it as closed or moved. {SRC['ws']} calls this out, and it’s a step almost everyone skips.</li>
<li><b>Get the space real.</b> Permanent signage up, the door open during your posted hours, a utility bill or lease in the business name. If Google asks for a video, it wants signage, the business in operation and proof you control the space (our {SIB['video']} has a full shot list). You can’t film what isn’t there yet.</li>
<li><b>Update your website first.</b> Contact page, footer, location page, embedded map, schema markup, title tags that mention the neighborhood. When Google checks the new address against your site, it should match to the suite number.</li>
<li><b>Edit the address on the existing profile.</b> One change. Keep the same name, phone number and primary category.</li>
<li><b>Verify, then stop editing.</b> Google picks the verification method, not you. If it’s a postcard, don’t touch the name, address or category until you enter the code; editing those voids it.</li>
<li><b>Update citations after the new address is live.</b> Apple Business Connect, Bing Places, Yelp, Facebook, Nextdoor, your chamber listing and any industry directories.</li>
<li><b>Watch for duplicates for a month.</b> Google sometimes auto-creates a listing at a new address from outside data. If one shows up, ask support to merge it into yours.</li>
</ol>
"""),

            ("Will I lose my Google reviews if I move?", f"""<p>Not if you edit the existing profile and keep the same business name. Google moves the reviews with you, per the help page above.</p>
<p>Where owners lose reviews is when they open a second profile at the new location. Then the old reviews sit on the old listing and you’re stuck asking support to move them. {SRC['lsf_new']} follows a multi-doctor practice that did this in 2023: support closed the old location while the reviews were still waiting to move. The Whitespark account in that thread replied that updating the old profile’s address and re-verifying would have kept the reviews along with the listing’s age and trust.</p>
<p>Distance doesn’t change the process. Google’s review-transfer page lists no distance limit, so a move across town and a move from Spring to Katy work the same way. The competition is what changes. Your reviews come with you, but your map rankings are now measured against a different set of nearby businesses, so expect a few weeks of movement. Whitespark advises waiting a few weeks before judging the effect.</p>
<p>And if your count drops after a move for reasons that seem unrelated, our guide on {'<a href="/blog/why-are-my-google-reviews-disappearing/">why Google reviews disappear</a>'} walks through the other causes.</p>"""),

            ("Edit, mark as moved, or create new: which one you need", f"""<p>Most owners only need the first row. The rest cover the messy cases.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Your situation</th><th>What to do on Google</th><th>What happens to reviews</th></tr></thead>
<tbody>
<tr><td>Same business, new address</td><td>Edit the address on your existing profile, then re-verify</td><td>Transfer automatically (same name)</td></tr>
<tr><td>Small name tweak, same services and category</td><td>Edit the name on the existing profile; keep proof ready</td><td>Stay on the profile</td></tr>
<tr><td>Brand-new name with different proper nouns</td><td>Google’s rules treat it as a new business: mark the old profile closed, create a new one</td><td>Stay with the old, closed profile</td></tr>
<tr><td>Storefront switching to service-area</td><td>Remove the address, add service areas</td><td>Stay on the profile</td></tr>
<tr><td>Accidentally made a second profile</td><td>Contact support to move reviews or merge</td><td>Can be moved; replies may be lost in a merge</td></tr>
<tr><td>Location closing, business continuing elsewhere</td><td>Edit the address instead of closing, unless a separate location stays open</td><td>Transfer with the edit</td></tr>
</tbody></table></div>
<p>A word on the “moved” label. {SRC['closed']} only offers “Temporarily closed” and “Permanently closed.” There’s no self-serve “moved” button, because when you edit the address there’s no old listing left to mark. The “moved” status only comes up when you end up with two listings. Then support can mark the old one as moved to the new one, though {SRC['lsf_moved']} reported in 2021 and 2022 that support sometimes closes it instead. Another reason to avoid ending up with two.</p>
<!--fig:paths-->"""),

            ("How to change business name on Google (and stay inside the naming rules)", f"""<p>Name changes are where most of the “google business profile suspended after name change” threads come from. The rules here are stricter than most owners expect.</p>
<p>{SRC['guide']} include a Rebranding section. A profile can keep its history through “a minor name change, in which the proper nouns and services described in the business name remain unchanged” and “the business category remains unchanged.” Multi-location brands that rename everything may also qualify. If the change doesn’t meet that bar, Google says “it’s considered a new business,” and you “must mark the existing Business Profile as closed” and create a new one.</p>
<p>If you’re planning a full rebrand, that sentence matters more than anything else in this post. Under the written rule, a completely new name means a new profile without your reviews. Plenty of businesses edit the name anyway and pass verification, but know the rule before you pay to wrap new trucks.</p>
<h3>Don’t stuff the new name</h3>
<p>A rename is when owners are most tempted to slip in keywords. Google’s naming rules ban marketing taglines, phone numbers, URLs, service descriptors and location information. Its own “not acceptable” examples include “Midas Auto Service Experts” and “Holiday Inn (I-93 at Exit 2).” The name on Google should match your sign, your Texas filings and your invoices, character for character.</p>
<h3>Get the paperwork changed first</h3>
<p>If your LLC or corporation operates under a new name, file an assumed name certificate with the Texas Secretary of State. Since {SRC['hb3609']} took effect on September 1, 2019, entities like LLCs and corporations no longer also file at the county. Sole proprietors and general partnerships file with the county clerk, which in Conroe means the Montgomery County Clerk. That filing becomes your proof if Google asks.</p>
<h3>A hypothetical Conroe rebrand</h3>
<p>Say a roofing contractor off Loop 336 in Conroe has run as “Ridgeline Roofing” for nine years with 140 reviews. They add siding and gutters and want to become “Ridgeline Exteriors.” The proper noun stays, but the service word changes, so it sits in a gray zone. Our approach: change the sign, trucks, website and assumed name certificate first, keep the primary category as Roofing contractor, make the name edit alone, and have the filing and sign photos ready for verification. If they wanted a name with no Ridgeline in it at all, we’d talk through the new-profile tradeoff before anything else. Our {'<a href="/blog/how-to-rebrand-without-losing-customers/">rebranding guide</a>'} covers telling customers about the change, which matters as much as Google does.</p>"""),

            ("Moving business: Google Business Profile steps for a Woodlands med spa", f"""<p>To put the whole sequence on a calendar, take a hypothetical med spa that has spent six years in a suite off Research Forest Drive and signed a lease at Hughes Landing on Lake Woodlands Drive. Same name, same phone, same owners, a few miles away.</p>
<p><b>Six weeks out.</b> List every place the old address lives: Google, Apple, Bing, Yelp, Facebook, the booking software, the Chamber directory. Search Maps for the new suite and flag any old tenant listings. Order permanent signage with the business name for the storefront.</p>
<p><b>Two weeks out.</b> Draft the website changes, but don’t publish them yet. Write the email and text to clients with the new address, where to park, and the date the old suite closes. The parking note alone saves the front desk a week of calls.</p>
<p><b>Moving week.</b> Sign goes up. First day treating clients at the new suite, publish the website changes in the morning and edit the Google address that afternoon. If Google asks for a video, the Hughes Landing storefront sign, the lobby and opening the back office with your key, all in one take, cover most of it.</p>
<p><b>The two weeks after.</b> Hands off the profile until the new address is approved. Then update citations in one batch, add photos of the new space, and post about the move. The old Research Forest suite needs nothing on Google, because the profile moved with you.</p>
<!--fig:numbers-->"""),

            ("Switching from a storefront to a service-area business", f"""<p>This is the change people underestimate. A contractor gives up the shop in Spring and goes mobile, or a mobile IV company stops seeing walk-ins. On Google, that means removing the address and listing service areas instead.</p>
<p>{SRC['sab']} says that if you don’t serve customers at your address, you should “remove your address and only enter your service area.” If customers still come to you and you also travel to them, you’re a hybrid and keep both. Service areas go in by city or ZIP code (Google caps the list and the drive time from your base), and approved edits can take up to 48 hours to show.</p>
<p>BrightLocal lists this switch as a suspension risk factor, so make it a single edit with nothing else changing that week. And be honest about the map. A Conroe crew that lists Willis, Montgomery, Magnolia and The Woodlands looks like a real business. Add Sugar Land and Baytown and it looks like someone padding the list.</p>
"""),

            ("Google Business Profile suspended after changing address? Do this next", f"""<p>First, stop editing. Every change now muddies the picture for whoever reviews the appeal.</p>
<ul>
<li>Read the notice in your profile. It usually names the policy involved.</li>
<li>Make sure the profile matches reality: real name, real staffed address or service area, matching website.</li>
<li>Gather proof that names the business at the new address: lease, utility bill, Texas filing, photos of the permanent sign, a short video from the street to your door.</li>
<li>File one appeal through the link in the notice. Don’t file three.</li>
<li>Don’t create a fresh profile while you wait. A second profile for the same location is its own violation.</li>
</ul>
<p>The {'<a href="/blog/google-business-profile-suspended-reinstatement/">reinstatement guide</a>'} covers the appeal, the evidence and what to do after a denial. Reviews usually come back with a reinstated profile (Google notes a few may not), which is another reason to appeal rather than start over. If you run Local Services Ads, the suspension also cuts the profile’s link to your ads and your {SIB['lsa']}, so expect those leads to stop until it’s resolved.</p>"""),

            ("Moving-day checklist for your Google Business Profile", f"""<p>Tape it next to the box of business cards with the old address on them.</p>
<!--fig:checklist-->
<p>Once you’re settled, go back through the basics in our {'<a href="/blog/local-seo-checklist-the-woodlands/">local SEO checklist for The Woodlands</a>'}. And if you need a reminder why this profile deserves the care, read why your {'<a href="/blog/google-business-profile-number-one-asset/">Google Business Profile is your number one asset</a>'}.</p>
<p>If a move or rebrand is on the calendar in The Woodlands, Conroe or elsewhere around Houston, our {'<a href="/services/web-design-seo-pr/">web design and SEO team</a>'} can sequence the profile, website and citations with you so nothing goes dark.</p>
<p>Ads are the piece people forget. Old addresses hide in ad text, location targeting drawn around the old suite and landing pages that still show the old map, and none of that updates when Google approves your profile edit. If you’re running Google or Meta ads through the move, request a free {'<a href="/contact/">Ad Spend Leak Check</a>'} the week you change the address. We’ll record a walkthrough of the account that flags anything still pointing customers to the place you just left.</p>"""),
        ],
        "faq": [
            ("Will I lose my Google reviews if I move my business?",
             "No, as long as you edit the address on your existing profile and keep the same business name. Google says it transfers reviews automatically in that case, except for some categories like hotels or golf courses. You lose them when you create a second profile at the new location, which leaves the reviews on the old listing and forces you to ask support to move them."),
            ("How long does Google take to approve a new business address?",
             "It varies. Google’s verification page says verification reviews can take up to 5 business days, and occasionally longer. Postcard verification adds mailing time, which Whitespark says can take 10 business days. Service-area edits can take up to 48 hours to appear once approved. Avoid other edits until the new address is live."),
            ("Why was my Google Business Profile suspended after a name change?",
             "Usually because the new name didn’t match anything Google could confirm, or the change went beyond what Google’s rebranding rules allow. Names with added keywords, taglines or locations break the naming guidelines. Change your signage, website and Texas filings first, then edit only the name on Google, and keep proof ready for verification."),
            ("Should I create a new Google Business Profile when I move?",
             "No. Google’s help pages say not to create a new profile because of a change in physical location. Edit the address on the profile you already have and re-verify it. That keeps your reviews, photos and the listing’s history. A second profile for the same business creates a duplicate, which can lead to a suspension."),
            ("Can I change my business address on Google before I move in?",
             "We wouldn’t. Google may ask you to verify by video, showing exterior signage, your tools or products, and access to staff-only areas. If the space is empty, you can’t pass that check, and an address that doesn’t match your website invites trouble. Make the edit the day you start serving customers there."),
        ],
        "figures": {
            "order": {
                "type": "steps",
                "title": "Safe order for moving your Google profile",
                "sub": "Real world first, Google second, citations third",
                "steps": [
                    ["Clear the new address", "Find old tenant listings at your new suite and flag them closed."],
                    ["Make the space real", "Permanent sign up, open during your hours, lease or utility bill in hand."],
                    ["Update the website", "Contact page, footer, map embed and schema, down to the suite number."],
                    ["Edit one thing on Google", "Change only the address on your existing profile."],
                    ["Verify, then wait", "No more edits until the new address is approved and live."],
                    ["Update citations", "Apple, Bing, Yelp, Facebook and your directories in one pass."],
                ],
                "alt": "Six-step order for changing a business address on Google without suspension for businesses in The Woodlands",
                "caption": "Doing these out of order is how most move-related suspensions start.",
            },
            "paths": {
                "type": "compare",
                "title": "Moving with a new profile vs. editing yours",
                "left": {
                    "title": "Create a new profile",
                    "items": [
                        "Reviews stay on the old listing",
                        "Two listings for one business",
                        "Support tickets to move reviews",
                        "Listing age and history reset",
                    ],
                },
                "right": {
                    "title": "Edit the existing profile",
                    "items": [
                        "Reviews transfer with the same name",
                        "One listing, no duplicate",
                        "One re-verification to pass",
                        "Photos and history stay put",
                    ],
                },
                "alt": "Comparison of creating a new Google Business Profile versus editing the address when a Houston business moves",
                "caption": "Google’s help pages say not to create a new profile because of a location change.",
            },
            "numbers": {
                "type": "stats",
                "title": "Google’s rules for moves, in numbers",
                "stats": [
                    ["5 days", "Business days a verification review can take"],
                    ["48 hr", "For approved service-area edits to appear"],
                    ["2", "Closed statuses offered, neither one “moved”"],
                    ["None", "Distance limit listed for moving reviews"],
                ],
                "note": "Source: Google Business Profile Help",
                "alt": "Google Business Profile timing and rules for Woodlands businesses changing address or switching to a service-area model",
                "caption": "Plan the move so the profile isn’t mid-review during your busiest week.",
            },
            "checklist": {
                "type": "checklist",
                "title": "Moving-day Google profile checklist",
                "sub": "Tick these off in order",
                "items": [
                    "Permanent sign with your exact business name is up",
                    "Lease or utility bill in the business name at the new address",
                    "Website contact page, footer and map show the new address",
                    "Old tenant listings at the new suite flagged as closed",
                    "Address edited on the existing profile, nothing else",
                    "Phone ready for a verification call or text",
                    "Short video: street sign, storefront, staff-only area",
                    "Client email and text about the move sent",
                    "Citations queued for after Google approves",
                ],
                "alt": "Moving-day checklist for changing a Google Business Profile address for a Houston area business",
                "caption": "Hold every other profile edit until the new address is approved.",
            },
        },
    },
]
