"""Batch 11 (Sports & Fitness vertical): gym presale marketing for opening a new location with members already signed,
and fitness franchise marketing across multiple locations.

Research: Texas Secretary of State health spa FAQ (registration, $100 fee, $20,000-$50,000 security per location,
31-day exemption, escrow within 14 days of first prepayment kept until 30 days after opening, 90-day closure claims);
Tex. Occ. Code 702.305 (refund notice, 181st day) and 702.307 (cancel by midnight of the third business day, refund
within 30 days) via texas.public.law; Morgan Lewis on Texas SB 140 (texts covered from Sept 1, 2025, $10,000 security,
$200 per location, exemptions, DTPA claims); Meta developer docs on Conversions API for CRM (200 leads/month, daily
uploads, stage within 28 days, 1%-40% conversion rate, instant forms only); Jon Loomer on instant form types and
conditional logic; Big Eye Agency on Meta radius targeting (1-50 miles) and the single "living in or recently in"
option; Google Ads Help on Presence vs. Presence or Interest; HFA 2026 consumer report (81 million members in 2025,
26.1% penetration, 4.6% never used); Community Impact's list of nine new fitness locations in The Woodlands area.
Franchise post: Planet Fitness FY2025 10-K on SEC EDGAR (NAF about 2% of dues, 7% local, franchisees voted 3% NAF and
6% local for 2026, 2,896 clubs, presales); 16 CFR 436.5(k)(4) Item 11 advertising disclosures and 436.5(s) Item 19
(eCFR); IFA 2024 legal symposium paper on marketing funds and local marketing (Anytime Fitness $600/$800/$1,000 local
spend, Stretch Lab $1,500 minimum, admin fees 0.5% to 18%, over 90% of FDDs offer some spending visibility); Meta
Marketing API store traffic guide (placeholders such as {{page.location.city}}, nearest-store serving, 0.7-50 mile
radii); First Byte Equinox case study and Sports & Fitness industry page (only numbers shown there).
Competitor/PAA phrasing read for "gym presale marketing", "how to presell gym memberships", "founding member offer",
"gym pre-sale ideas", "fitness franchise marketing", "franchise marketing fund", "multi-location gym marketing".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # presale post
    "sos": A("https://www.sos.texas.gov/statdoc/faqs3000.shtml", "Texas Secretary of State’s health spa FAQ"),
    "sos_short": A("https://www.sos.texas.gov/statdoc/faqs3000.shtml", "Texas Secretary of State"),
    "s305": A("https://texas.public.law/statutes/tex._occ._code_section_702.305", "Section 702.305 of the Occupations Code"),
    "s307": A("https://texas.public.law/statutes/tex._occ._code_section_702.307", "Section 702.307"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    "capi": A("https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration", "Meta’s Conversions API for CRM documentation"),
    "loomer": A("https://www.jonloomer.com/instant-forms/", "Jon Loomer’s guide to instant forms"),
    "bigeye": A("https://www.bigeyeagency.com/insights/geographic-targeting-for-meta-ads-guide-2026", "Big Eye Agency’s 2026 guide to Meta geo targeting"),
    "gloc": A("https://support.google.com/google-ads/answer/1722038?hl=en", "Google Ads Help"),
    "hfa": A("https://www.healthandfitness.org/81-million-americans-were-members-of-a-fitness-facility-in-2025-new-hfa-report-finds/", "the Health &amp; Fitness Association’s 2026 consumer report"),
    "ci": A("https://communityimpact.com/the-woodlands/business/9-new-fitness-locations-to-visit-in-the-woodlands-area-in-2025/", "Community Impact"),
    # franchise post
    "plnt": A("https://www.sec.gov/Archives/edgar/data/1637207/000163720726000011/plnt-20251231.htm", "Planet Fitness’s 2025 annual report (10-K)"),
    "plnt_short": A("https://www.sec.gov/Archives/edgar/data/1637207/000163720726000011/plnt-20251231.htm", "Planet Fitness 10-K"),
    "item11": A("https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-436/subpart-C", "16 CFR 436.5(k)"),
    "item19": A("https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-436/subpart-C", "Item 19 of the Franchise Rule (16 CFR 436.5(s))"),
    "ifa": A("https://www.franchise.org/wp-content/uploads/2026/04/IFA-Legal-2024-Marketing-Funds-and-Local-Marketing_2.pdf", "a 2024 International Franchise Association legal symposium paper"),
    "ifa_short": A("https://www.franchise.org/wp-content/uploads/2026/04/IFA-Legal-2024-Marketing-Funds-and-Local-Marketing_2.pdf", "IFA paper"),
    "store": A("https://developers.facebook.com/docs/marketing-api/guides/advantage-catalog-ads/store-traffic/", "Meta’s Marketing API guide to store traffic ads"),
}

PRESALE = "/blog/gym-presale-new-location-membership-launch/"
FRANCHISE = "/blog/fitness-franchise-multi-location-marketing/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: gym presale
    {
        "slug": "gym-presale-new-location-membership-launch",
        "title": "Gym Presale Marketing: How to Open a New Location With Members Already Signed",
        "seo_title": "Gym Presale Marketing: Open With Members Already Signed",
        "desc": "Gym presale marketing for a new location: a 90/60/30-day timeline, founding-member offers, Meta lead ads vs. landing pages, follow-up and cost per member.",
        "category": "Paid social",
        "icons": ["Meta", "Instagram", "Google Ads"],
        "art": "b2",
        "hero": "clock",
        "hero_alt": "Illustration of a countdown clock for gym presale marketing before a new location opens in Houston and The Woodlands",
        "related": ["gym-fitness-studio-marketing-the-woodlands-houston", "grand-opening-marketing-plan-30-days", "speed-to-lead-response-time-follow-up-crm"],
        "sections": [
            (None, f"""<p>Thursday, 6:15 p.m., in a leased trailer at the edge of a parking lot off FM 2978. The building behind it is still studs and conduit. Your presale manager has two tours booked, a third walk-in who saw the banner from the road, and 38 new leads from yesterday’s Facebook ads that nobody has called yet.</p>
<p>Opening day is supposedly 74 days away. The contractor said “supposedly” too.</p>
<p>This is what presale marketing actually looks like. A gym presale is the stretch, usually about 90 days, when you sell founding memberships before the doors open, so the club starts with dues already coming in and a floor that isn’t empty. Done well, it pays for a good chunk of the launch. Done badly, you get a list of 4,000 “leads,” 140 members, and a refund problem when the opening slips.</p>
<p>We’ve run club launches for Equinox, so this comes from doing it rather than reading about it. If you want the general gym marketing picture (intro offers, Google profile, retention), our {L('/blog/gym-fitness-studio-marketing-the-woodlands-houston/', 'gym and fitness studio marketing guide')} covers it. This post is only about the presale.</p>"""),

            ("What a presale has to accomplish", f"""<p>A presale has three jobs, and most clubs only plan for the first one.</p>
<ol>
<li><b>Sign members before opening</b>, at a price that still makes sense once the founding rate is locked in for years.</li>
<li><b>Build a waitlist of people who didn’t buy yet</b>, so opening week has a second wave of buyers.</li>
<li><b>Teach the neighborhood the club exists</b>, so you show up in searches, in conversations at the pickup line and on Nextdoor the week you open.</li>
</ol>
<p>The demand is there. The Health &amp; Fitness Association counted a record 81 million U.S. fitness facility members in 2025, up 5.2% from 2024, or 26.1% of Americans age six and up, per {SRC['hfa']}. The same report found the share of members who never use their membership fell to 4.6%. People are joining and showing up.</p>
<p>So is the competition. {SRC['ci']} listed nine new fitness locations in The Woodlands area going into 2025, from a pickleball club in Magnolia to a Pilates studio on Woodlands Parkway. A new club in Spring, Cypress or Katy is never the only new thing in the feed.</p>"""),

            ("The 90/60/30-day presale timeline", f"""<p>Ninety days is the window our {L('/industries/sports-fitness/', 'sports and fitness work')} is built on. Shorter and you open half full. Much longer and people forget they bought, or construction makes a liar of you.</p>
<!--fig:timeline-->
<p><b>Days 120 to 90: setup.</b> Register with the state if you need to (see the Texas section), finalize the founding offer, build the landing page and CRM pipeline, and shoot creative. Put the banner on the building the day you’re allowed to.</p>
<p><b>Days 90 to 60: waitlist and first sales.</b> Ads go live around the site. The goal for the first two weeks is a waitlist big enough to sell from. Open the presale office or trailer as soon as it’s safe and permitted. The first founding-rate tier sells here.</p>
<p><b>Days 60 to 30: the grind.</b> Leads get cheaper, but closing gets harder because the easiest buyers already bought. Follow-up discipline decides the number here. Run your first price-increase deadline and a member-get-member push.</p>
<p><b>Days 30 to 0: urgency and media.</b> Final founding tier, hard-hat tours if allowed, a founders’ preview night, and bigger launch media like the CTV and digital out-of-home bursts we ran for Equinox (our {L('/blog/streaming-tv-ads-worth-it-small-business/', 'streaming TV post')} covers buying it locally).</p>
<p>Below is the weekly shape we expect. It’s an example, not a forecast.</p>
<!--fig:pace-->
<p>Notice the dip in weeks five through eight. Every presale we’ve seen has one. Plan a promotion for it instead of panicking in it.</p>"""),

            ("Founding-member offers that sell without wrecking your pricing", f"""<p>The founding offer is the product you’re actually advertising for 90 days, so design it before anyone writes an ad.</p>
<p>What a good founding offer usually has:</p>
<ul>
<li><b>A rate lock</b> below standard dues, for as long as the membership stays active. This is the thing people buy.</li>
<li><b>Tiers that close.</b> The first 200 members get the lowest rate, the next 300 get a slightly higher one, then standard pricing on opening day. Real caps, publicly counted down, honored exactly.</li>
<li><b>A reduced or waived enrollment fee</b> instead of a lower monthly rate, if your margins are tight. A waived fee costs you once. A low rate costs you every month.</li>
<li><b>Something only founders get</b>: a founder bag, first booking rights for classes, a preview night.</li>
<li><b>Billing that starts on opening day</b> (or a small deposit now), which removes the “why am I paying for a gym I can’t use” objection.</li>
</ul>
<p>What we’d avoid: lifetime rates with no conditions, discounts so deep that standard pricing looks like a ripoff, and “limited spots” claims that aren’t limited. Members at a new club talk.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Tier</th><th>Window</th><th>Offer (illustrative)</th><th>What the ad says</th></tr></thead>
<tbody>
<tr><td>Founders 1</td><td>Days 90-60, first 200 members</td><td>Lowest locked rate, $0 enrollment, founder bag</td><td>“First 200 lock $X/month for as long as you’re a member”</td></tr>
<tr><td>Founders 2</td><td>Days 60-30, next 300</td><td>Rate +$5, $0 enrollment</td><td>“Founders 1 is sold out. 300 founding spots left.”</td></tr>
<tr><td>Final founders</td><td>Days 30-0</td><td>Rate +$10, reduced enrollment, preview night invite</td><td>“Founding rates end on opening day”</td></tr>
<tr><td>Opening</td><td>Day 0 onward</td><td>Standard rate, opening-week enrollment special</td><td>“Now open. Tour today.”</td></tr>
</tbody></table></div>
<p>If you’re a franchise, check what your franchise agreement allows before you set any of this. Some systems set presale pricing rules for every location, and our {L(FRANCHISE, 'fitness franchise marketing guide')} gets into how brand and local marketing split.</p>"""),

            ("The presale office or trailer", f"""<p>A real place to sit down and sign closes more than any landing page. Most of the clubs we’ve seen launch well have a presale office: a trailer on site, a vacant suite in the same center, or a pop-up in a nearby retail space.</p>
<p>What makes it work:</p>
<ul>
<li><b>Visible from the road</b>, with signage that says “Founding memberships, now open” and the hours. Drive-by traffic on Woodlands Parkway or the Grand Parkway frontage is free marketing.</li>
<li><b>Renderings and samples.</b> Floor plans, equipment specs, locker room finishes. People are buying something they can’t see.</li>
<li><b>Hours that match when people come.</b> Evenings and Saturday mornings. A trailer that closes at 5 p.m. misses the commuters coming home from downtown or the Energy Corridor.</li>
<li><b>Booked appointments, not just walk-ins.</b> Every lead gets offered a tour of the presale office. That appointment is the main metric (see the follow-up section).</li>
</ul>
<p>If your presale runs through a Houston summer, budget for real AC and a covered entrance, or rent a suite. A sweaty consult is a short consult.</p>"""),

            ("Meta lead ads vs. landing pages for a presale", f"""<p>Most presale leads come from Facebook and Instagram, because nobody searches for a gym that doesn’t exist yet. The question is where the click goes.</p>
<!--fig:forms-->
<p><b>Instant forms (lead ads)</b> are cheap and fast. People submit without leaving Instagram, so you get a lot of leads for the money, and plenty of them forgot they filled anything out. A few settings help a lot, and {SRC['loomer']} walks through them: choose the <b>Higher intent</b> form type, which adds a review step before submitting; add one or two custom questions (“When are you looking to start?” and “Which location?”); and use conditional logic to send people who say they’re not local to a close-form screen instead of your CRM. For deeper problems, our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'post on fixing bad Facebook leads')} covers more.</p>
<p><b>Landing pages</b> cost more per lead and sell better. The page can show the founding tiers, the countdown, renderings, a booking calendar for the presale office, and a checkout to buy the founding membership online. Optimize the campaign for the purchase or the booked tour, not the form fill, once the pixel and Conversions API are tracking those events.</p>
<p>Our default for a single club: instant forms to build the waitlist in the first month, a landing page campaign optimized for purchases or bookings from day 30 on, and retargeting from both.</p>
<p>One more option worth knowing about. Meta’s “conversion leads” optimization lets you feed lead stages from your CRM back to Meta so it finds people who actually buy, not just people who fill out forms. Per {SRC['capi']}, it works only with instant forms, Meta wants at least 200 leads a month, you should upload data at least daily, and the stage you optimize for should happen within 28 days of the lead with a conversion rate between 1% and 40%. A busy presale clears all of those. “Booked a presale tour” is a good stage to send.</p>"""),

            ("Geo radius and targeting around the site", f"""<p>Geography does most of the targeting work in a presale. People join gyms close to home or work, so the radius decides who sees you.</p>
<p>In Meta Ads Manager, you set it at the ad set level under Audience, then Locations: drop a pin on the site and choose a radius. Meta allows a pin radius between 1 and 50 miles, and the old “living in” versus “traveling in” choices have been folded into one setting, people living in or recently in the location, per {SRC['bigeye']}. That “recently in” part means you’ll reach some people passing through, which is one more reason to qualify on the form.</p>
<p>Radius rules of thumb from accounts we’ve run (our experience, not platform guidance):</p>
<ul>
<li><b>Dense, inside-the-Loop locations:</b> 2 to 4 miles. People won’t cross the city for a gym.</li>
<li><b>Suburban sites</b> in The Woodlands, Spring, Cypress, Katy or Pearland: 5 to 8 miles, then shape it. A pin near I-45 can reach neighborhoods across the freeway that won’t make the drive at 6 a.m.</li>
<li><b>Destination clubs</b> with a pool, courts or a big kids’ club: up to 10 to 12 miles, with a separate, tighter ad set for the closest neighborhoods so they get more frequency.</li>
</ul>
<p>On Google Ads, use radius targeting around the site and set the location option to <b>Presence</b> (people in or regularly in your targeted locations) instead of the default Presence or Interest, which also reaches people merely interested in the area, per {SRC['gloc']}. Search volume is small until the banner goes up. Bid on your brand plus the area (“[brand] The Woodlands”), “new gym [town]” and category terms like “24 hour gym Spring TX,” with the founding rate in the ad. Add negatives for jobs, careers, “hiring” and “day pass” early.</p>"""),

            ("Follow-up and appointment setting", f"""<p>This is where presales are won or lost. A lead called within five minutes and offered a tour is worth far more than one emailed two days later. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the details, and the presale version is simple:</p>
<ol>
<li><b>Instant text</b> when the lead comes in (with consent captured on the form), from a real name, offering two tour times.</li>
<li><b>A call within 15 minutes</b> during staffed hours. The only goal is a booked appointment at the presale office.</li>
<li><b>Reminder text</b> the day before and two hours before the tour.</li>
<li><b>No-show follow-up</b> the same day, with a new time.</li>
<li><b>Weekly nurture for the “not yet” crowd</b>: construction updates, tier countdowns, a class schedule preview.</li>
</ol>
<p>A first text that tends to work:</p>
<blockquote><p>“Hi Maria, it’s Josh with [Club] Spring. Thanks for asking about founding memberships. We have tours at the presale office tomorrow at 6:00 or Saturday at 10:30. Want me to hold one? Founders 1 has 41 spots left.”</p></blockquote>
<p>Specific, short, a real deadline.</p>
<p>Texting has legal strings in Texas. Since September 1, 2025, SB 140 brings text messages under the state’s telephone solicitation law, which means many businesses texting Texans to sell something have to register with the Secretary of State (a $10,000 security and a $200 fee per location), and consumers can sue under the DTPA for violations, per {SRC['sb140']}. There are exemptions, including some for current or former customers and businesses that mostly sell from brick-and-mortar locations, but a presale lead hasn’t bought anything yet and your club isn’t open. Ask your lawyer before you launch the text sequence, and see our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} for the basics.</p>"""),

            ("Texas health spa rules that shape a presale", f"""<p>Texas regulates gyms that sell memberships as “health spas,” and presales get special attention. This isn’t legal advice, but your marketing has to fit inside these rules.</p>
<!--fig:texas-->
<p>Per the {SRC['sos']}, a business selling memberships for an exercise program generally needs a health spa certificate of registration from the Secretary of State before selling memberships ($100 a year), with security of $20,000 to $50,000 per location depending on prepaid memberships, unless it qualifies for an exemption. One exemption covers operators that don’t offer contracts longer than 31 days, don’t take prepayment for longer than 31 days and don’t charge initiation fees, among other conditions. Founding offers with enrollment fees or annual prepay usually fall outside that exemption, so check before you design the offer.</p>
<p>The presale-specific parts, also per the Secretary of State: if you accept prepayments before opening, you have to open an escrow account at an FDIC-insured institution within 14 days of the first prepayment, file a statement about it, and keep it until 30 days after the club opens.</p>
<p>Two contract rules matter to marketers. {SRC['s305']} requires a conspicuous notice telling presale buyers they get a full refund if the spa doesn’t open before the 181st day after they prepaid (with different terms if the operator has a nearby location they can use). And under {SRC['s307']}, members can cancel for a full refund by midnight of the third business day after signing.</p>
<p>So what changes in the marketing:</p>
<ul>
<li><b>Count members net of the three-day cancellations</b> before you celebrate a weekend.</li>
<li><b>Don’t start taking money too early.</b> If you sell on day 120 and construction slips four months, you’re past the 181-day line.</li>
<li><b>Ads promise what the contract says.</b> “Rate locked for as long as you’re a member” has to match the actual terms.</li>
</ul>"""),

            ("When construction runs late", f"""<p>It will. Permits, inspections, a late HVAC unit, a week of August storms. The question is how you handle it.</p>
<ul>
<li><b>Never put a hard opening date in ads until the certificate of occupancy is in sight.</b> Say “Opening this spring” or “Opening early 2027” until you’re sure, then switch to the date.</li>
<li><b>Tell founders first, by email and text</b>, before it shows up on Facebook. Include the new window and what you’re doing for them: an extra free month, a guest pass, an extended founding-rate deadline for their friends.</li>
<li><b>Pull back spend, don’t stop it.</b> Cut prospecting to roughly a maintenance level and keep retargeting and nurture running. Restarting a campaign from zero costs more than idling one.</li>
<li><b>Watch the 181-day refund window</b> for your earliest buyers and plan the communication before anyone asks.</li>
</ul>
<p>Delays are also content. A phone video of the floor going in builds more trust than a render.</p>"""),

            ("Measuring cost per presale member", f"""<p>Cost per lead is the number everybody looks at and the one that matters least. The presale number is cost per net presale member.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>Formula</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Cost per lead</td><td>Media spend ÷ leads</td><td>Early warning only</td></tr>
<tr><td>Lead-to-appointment rate</td><td>Booked tours ÷ leads</td><td>Tests follow-up speed and lead quality</td></tr>
<tr><td>Show rate</td><td>Tours attended ÷ tours booked</td><td>Tests reminders and lead intent</td></tr>
<tr><td>Close rate</td><td>Members sold ÷ tours attended</td><td>Tests the offer and the presale team</td></tr>
<tr><td>Net presale members</td><td>Members sold − three-day cancels − refunds</td><td>The real count</td></tr>
<tr><td>Cost per presale member</td><td>Total presale marketing cost ÷ net presale members</td><td>The number to budget from</td></tr>
<tr><td>Presale pace</td><td>Net members to date ÷ (target × share of presale elapsed)</td><td>Above 1.0 means on track</td></tr>
</tbody></table></div>
<p>Total presale marketing cost should include media, creative, the landing page, CRM and texting tools, and the agency. Presale office rent and staff are your call; just be consistent between launches.</p>
<!--fig:funnel-->
<p>For reference, the Equinox launches our team ran combined geo-targeted paid social and search starting 90 days before opening, a founding-member offer with dedicated landing pages and a waitlist, CRM, SMS and email nurture, and launch-week CTV and digital out-of-home. The {L('/case-studies/equinox/', 'Equinox case study')} reports $4.8M in presale membership revenue, 11,400 founding-member leads, 94% capacity on opening day and cost per lead 62% below benchmark. Your club isn’t Equinox and your numbers won’t match, but the structure transfers.</p>
<p>For setting up the tracking itself (calls, forms and bookings into GA4 and Google Ads), see our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'conversion tracking guide')}.</p>"""),

            ("The ramp after opening day", f"""<p>Opening day is the start of the second campaign.</p>
<p><b>Weeks one and two:</b> the waitlist gets an opening-week offer and an invitation to tour the finished club. Swap renderings for real member footage the first weekend, and push Google search on brand and “gym near me” terms now that your Business Profile is live. Our {L('/blog/grand-opening-marketing-plan-30-days/', 'grand opening plan')} covers the event side.</p>
<p><b>Weeks two through eight:</b> ask founders for Google reviews while the excitement is fresh (our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has the ask), launch a member-get-member offer, and start onboarding: a first-week check-in, a free session with a coach, a class challenge. Founders who don’t build a habit in the first month are your first cancellations.</p>
<p><b>Months three through six:</b> shift from presale urgency to always-on demand, at a cost per member you can sustain.</p>
<p>If you’re planning a launch and want a plan built for your site, offer and opening date, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How far in advance should a gym start a presale?",
             "About 90 days before opening is the window we plan around, with setup work starting a month earlier. That gives time to build a waitlist, sell founding tiers and run launch media. Starting much earlier risks buyers losing interest and, in Texas, getting close to the 181-day refund line if construction slips. Avoid publishing a hard opening date until the certificate of occupancy is close."),
            ("What is a good founding member offer for a new gym?",
             "Most good founding offers lock a lower monthly rate for as long as the membership stays active, sold in tiers with real caps that close on schedule. Waiving the enrollment fee is a cheaper alternative to a lower rate. Add something only founders get, like a preview night or first class booking. Avoid fake scarcity and lifetime rates with no conditions, since members compare notes."),
            ("Should gym presale ads use Facebook lead forms or a landing page?",
             "Use both. Instant forms build a waitlist cheaply in the first month, especially with the Higher intent form type and a qualifying question or two. A landing page with founding tiers, renderings, tour booking and online checkout converts better and lets you optimize for purchases or booked tours. Retarget both audiences, and judge each by cost per net presale member, not cost per lead."),
            ("Do Texas gyms need to register before selling presale memberships?",
             "Generally yes. Texas treats gyms selling memberships as health spas, which need a Secretary of State registration and security of $20,000 to $50,000 per location unless exempt. Prepayments before opening require an escrow account opened within 14 days. Contracts need a refund notice tied to the 181st day after prepayment, and members can cancel within three business days. Have a lawyer review your contract."),
            ("How do you calculate cost per presale member?",
             "Divide total presale marketing cost by net presale members. Include media, creative, landing pages, CRM and texting tools and agency fees, and decide once whether presale office rent and staff belong in it. Net members means members sold minus three-day cancellations and refunds. Track lead-to-tour rate, show rate and close rate alongside it so you can see where the funnel is leaking."),
        ],
        "figures": {
            "timeline": {
                "type": "steps",
                "title": "The 90/60/30-day gym presale timeline",
                "sub": "What happens in each window before opening day",
                "steps": [["Days 120-90: setup", "Registration, founding offer, landing page, CRM, creative, banner."], ["Days 90-60: waitlist", "Ads live around the site, presale office opens, Founders 1 sells."], ["Days 60-30: the grind", "Follow-up discipline, first tier deadline, member-get-member."], ["Days 30-0: urgency", "Final tier, hard-hat tours, preview night, CTV and out-of-home."], ["Day 0 on: ramp", "Waitlist offer, real footage, reviews, onboarding."]],
                "alt": "Timeline of a 90, 60 and 30 day gym presale marketing plan for a new location in Houston and The Woodlands",
                "caption": "Ninety days is our planning window. Setup starts a month before the first ad.",
            },
            "pace": {
                "type": "columns",
                "title": "Weekly presale sign-ups, example club",
                "sub": "Share of the peak week, 13-week presale",
                "labels": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13"],
                "values": [55, 70, 62, 50, 38, 34, 36, 40, 48, 58, 70, 85, 100],
                "highlight": [12],
                "y_label": "% of peak",
                "note": "Illustrative example",
                "alt": "Column chart of weekly gym presale membership sign-ups before a new location opens in Houston, with a mid-presale dip",
                "caption": "A fast start, a dip in the middle, and a final rush as founding rates close.",
            },
            "forms": {
                "type": "compare",
                "title": "Instant forms vs. landing pages for presale ads",
                "left": {"title": "Instant forms", "items": ["Cheapest cost per lead", "Many people forget they signed up", "Builds a waitlist fast", "Needs Higher intent and qualifying questions", "Can use conversion leads optimization"]},
                "right": {"title": "Landing page", "items": ["Higher cost per lead", "Shows tiers, renderings and countdown", "Books presale tours directly", "Sells founding memberships online", "Optimizes for purchases or bookings"]},
                "alt": "Comparison of Meta instant forms and landing pages for gym presale marketing in Houston and The Woodlands",
                "caption": "We run both: forms for the waitlist early, the landing page for sales from day 30 on.",
            },
            "texas": {
                "type": "stats",
                "title": "Texas health spa rules for presales",
                "stats": [["14 days", "to open escrow after the first prepayment"], ["181st day", "refund if not open by then"], ["3 business days", "for members to cancel"], ["$20K-$50K", "security per location unless exempt"]],
                "note": "Source: Texas Secretary of State; Tex. Occ. Code 702.305, 702.307",
                "alt": "Stats on Texas health spa rules that affect gym presale marketing for new locations in Houston and The Woodlands",
                "caption": f"From the {SRC['sos_short']} and the Occupations Code. Not legal advice.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From lead to net presale member",
                "stages": [["Leads", "3,000"], ["Booked presale tours", "900"], ["Tours attended", "600"], ["Members sold", "330"], ["Net after cancels and refunds", "310"]],
                "note": "Illustrative example",
                "alt": "Funnel from leads to net presale members for a gym presale at a new location in Houston and The Woodlands",
                "caption": "Count the bottom row. Cost per presale member is total presale marketing cost divided by it.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: fitness franchise
    {
        "slug": "fitness-franchise-multi-location-marketing",
        "title": "Fitness Franchise Marketing Across Multiple Locations: Brand Fund, Local Ads and Reporting",
        "seo_title": "Fitness Franchise Marketing Across Multiple Locations",
        "desc": "Fitness franchise marketing for multiple locations: brand fund vs. local spend, co-op ads, Meta local ads, per-location tracking, budgets and reporting.",
        "category": "Strategy",
        "icons": ["Meta", "Google Business Profile", "Google Analytics"],
        "art": "b4",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for fitness franchise marketing across multiple gym locations in Houston and The Woodlands",
        "related": ["multi-location-local-seo-houston-franchises", "gym-fitness-studio-marketing-the-woodlands-houston", "measure-marketing-success-metrics"],
        "sections": [
            (None, f"""<p>Monday, 9 a.m., the regional franchisee call. Five owners on the line: Katy, Cypress, Pearland, Kingwood and Sugar Land. Katy is up 60 members this month and doesn’t know why. Pearland is down and wants to know why the brand fund paid for a national campaign instead of more ads in Pearland. Kingwood asks whether the leads in the portal are his or the Humble location’s. Nobody can answer cleanly, because each studio’s numbers come from a different place.</p>
<p>That call is fitness franchise marketing in a nutshell. The ads are rarely the hard part. Who pays for what, who controls which account, and whether every location measures the same things the same way: that’s where it gets hard.</p>
<p>This guide is for franchisor marketing teams and multi-unit franchisees running gyms, studios and boutique fitness concepts. We’ll cover the brand fund and local spend split, co-op advertising, location pages and Google profiles at scale, Meta ads that localize for every location, tracking, budgets by location maturity, and how to report to franchisees so the Monday call goes better.</p>
<p>For the technical local SEO side (Google Business Profile groups, schema, location pages), we wrote a separate {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO guide')}. We won’t repeat it here.</p>"""),

            ("Brand fund vs. local marketing: who pays for what", f"""<p>Most fitness franchise systems split marketing money into two or three buckets:</p>
<ul>
<li><b>The brand fund</b> (also called the national advertising fund, marketing fund or NAF). Franchisees pay a set percentage or flat fee. The franchisor spends it on things that help every location: brand creative, national media, the website, the app, the CRM, ad templates.</li>
<li><b>Local marketing</b>, a required minimum each franchisee spends in their own market, on approved channels.</li>
<li><b>Co-ops</b>, where franchisees in a market pool local money for media that one location couldn’t afford alone.</li>
</ul>
<p>Planet Fitness is the clearest public example because it files a 10-K. Per {SRC['plnt']}, franchisees and corporate-owned clubs generally contribute about 2% of membership dues to the national advertising fund, and franchisees in the U.S. and Canada must spend 7% of monthly dues on local marketing. For 2026, the filing says franchisees voted to raise the national fund to 3% and lower local marketing to 6%. That’s a system with 2,896 clubs as of the end of 2025 deciding that a bit more central spend beats a bit more local spend.</p>
<p>Other fitness systems use flat fees. {SRC['ifa']} that reviewed dozens of franchise disclosure documents cited Anytime Fitness requiring a flat $600, $800 or $1,000 a month in local spend depending on market size, and Stretch Lab requiring at least $1,500 a month. Those figures came from the FDDs the authors reviewed at the time, so check the current documents for any system you’re looking at.</p>
<!--fig:split-->
<p>Our opinion: central money should fund what has economies of scale (creative, technology, brand awareness media, the website), and local money should fund anything that depends on a specific trade area (search, local Meta ads, events, partnerships). Things go sideways when the brand fund tries to buy local results with national media, or when every franchisee builds their own creative because the brand’s templates don’t fit their market.</p>"""),

            ("What the franchise disclosure document says about marketing", f"""<p>If you work on the franchisor side, the FTC Franchise Rule shapes what you can do with the fund, because franchisees read Item 11 of the franchise disclosure document before they sign.</p>
<p>Under {SRC['item11']}, Item 11 has to describe the advertising program, including what media the franchisor may use, whether coverage is local, regional or national, who produces the ads, and when franchisees can use their own materials. For any advertising fund, it has to disclose who contributes and how much, whether franchisor-owned outlets contribute and on the same basis, who administers it, if and when it’s audited, whether financial statements are available to franchisees, and how the money was used in the last fiscal year, including the percentages spent on production, media placement and administration. Local or regional co-ops get their own disclosures: whether participation is required, how contributions are set, who administers the co-op and whether it produces financial statements.</p>
<p>Administrative costs vary widely. The same {SRC['ifa_short']} found fund administrative fees in its sample ranging from 0.5% of annual fund spending at Taco Bell to 18% at Snap Fitness, and estimated that more than 90% of the FDDs it reviewed gave franchisees some way to see how the fund was spent.</p>
<p>What this means for marketers:</p>
<ul>
<li><b>Report fund spending in the same categories Item 11 uses</b> (production, media, administration, other). Franchisees will compare your quarterly report to the FDD.</li>
<li><b>Keep franchise-sales marketing out of the fund unless the FDD allows it.</b> Item 11 also asks for the share of fund money used mainly to sell new franchises.</li>
<li><b>Watch franchise-development ads for earnings claims.</b> Under {SRC['item19']}, financial performance information has to have a reasonable basis and be in the FDD; numbers that differ from Item 19 can only be given in narrow, documented cases. “Owners average $1.2M in revenue” in a recruitment ad is a legal question, not a copywriting one.</li>
</ul>
<p>We’re marketers, not franchise lawyers. Have counsel review anything that touches the fund or franchise sales.</p>"""),

            ("Co-op advertising for franchisees in the same market", f"""<p>Co-ops make sense when the right media covers more than one trade area. In Houston, that’s most of the big media. A streaming TV buy, a radio flight or a billboard on I-45 reaches people from Conroe to Clear Lake, so five franchisees each buying it alone means five overlapping, too-small buys.</p>
<p>Good fits for a Houston co-op:</p>
<ul>
<li><b>Streaming TV</b> targeted to the Houston DMA or a list of ZIP codes around all member locations. Our {L('/services/ctv-ooh-streaming-radio/', 'CTV, radio and billboard team')} handles these.</li>
<li><b>Radio and audio streaming</b> around January and back-to-school, when gym demand moves.</li>
<li><b>Billboards and digital out-of-home</b> on commuter routes, with copy that points to the nearest-location finder.</li>
<li><b>Sponsorships</b>: a high school football stadium sign, a 5K in The Woodlands, a Houston Marathon expo booth.</li>
</ul>
<p>Rules that keep a co-op from turning into a fight:</p>
<ol>
<li><b>Split costs by a formula everyone agreed to in writing</b>: equal shares, share of members, or share of revenue. Member share is usually fairest.</li>
<li><b>Don’t run search through the co-op.</b> Search is location-specific and should stay in each location’s own budget.</li>
<li><b>One media plan, one report.</b> Show reach and frequency by location area, plus brand search volume and website visits per location page before and after each flight.</li>
<li><b>Write down who decides</b>, who breaks ties, and how a new location joins mid-year.</li>
</ol>"""),

            ("Location pages and Google Business Profile at scale", f"""<p>We cover the mechanics in the {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location SEO guide')}. The fitness-specific parts:</p>
<ul>
<li><b>Every location page shows that location’s real class schedule, hours, pricing (or a starting price), amenities, staff and photos.</b> A template with only the address swapped is close to useless for search and doesn’t convert.</li>
<li><b>Presale locations get a page the day the lease is signed</b>, with the founding offer and a waitlist form. That page will own the brand-plus-town search when the banner goes up. Our {L(PRESALE, 'gym presale guide')} covers the rest of a launch.</li>
<li><b>One Google Business Profile per open location</b>, owned by the brand’s organization account with the franchisee as a manager, so nothing is lost when a location changes hands.</li>
<li><b>Review requests run from the CRM per location</b>, and the response templates sound like the local team. A reply signed by the Cypress manager beats “Thank you for your feedback! – The Brand Team.” See our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')}.</li>
<li><b>Hours, holiday closures and class changes update centrally</b>, so a hurricane closure or a holiday schedule doesn’t live in 14 different hands.</li>
</ul>"""),

            ("Meta local ads with dynamic location info", f"""<p>Meta is usually the biggest local spend line for a fitness franchise, and the hardest one to run across many locations. There are three common setups.</p>
<p><b>1. One campaign, one ad set per location.</b> Each ad set has its own pin and radius, budget and creative that names the location. Simple and transparent, and every location gets the spend it paid for. The downside is work: 30 locations means 30 ad sets to build, refresh and report on.</p>
<p><b>2. One campaign with dynamic location ads.</b> Meta can fill in details from the nearest location automatically. Per {SRC['store']}, a brand with its locations set up under a parent Facebook Page can use placeholders such as <code>{{{{page.location.city}}}}</code>, <code>{{{{page.location.street_address}}}}</code>, <code>{{{{page.hours.today}}}}</code> and <code>{{{{page.phone_number}}}}</code> in ad text, and Meta serves each ad from the store closest to the viewer, with radius limits of 0.7 to 50 miles. “Your new gym is on {{{{page.location.street_address}}}}” scales to hundreds of locations with one ad. The catch: that setup depends on a clean Facebook location structure, which many brands don’t have, and budget control by location is weaker.</p>
<p><b>3. A local-ads platform.</b> Several vendors let franchisees pick from brand-approved templates, set their own budget and launch ads in their own name, while the franchisor keeps control of creative. Good for systems with many small owners. Check who owns the ad accounts and data before signing.</p>
<p>One warning on option 1. If you use Advantage campaign budget (campaign budget optimization) across location ad sets, Meta moves money to whichever locations get the cheapest results, which might not be the ones that paid in or the ones that need members. Use ad set spend limits under Advantage campaign budget, or set budgets at the ad set level, so Pearland’s money stays in Pearland.</p>
<!--fig:meta-->
<p>Whichever setup you use, creative should look local even when it’s templated: real footage from that location, the coach’s name, the shopping center everyone knows. In our experience, “Now open next to the H-E-B” outperforms a polished national brand spot in local feeds. Our {L('/services/paid-social-advertising/', 'paid social team')} builds these for multi-location brands.</p>"""),

            ("Consistent tracking for every location", f"""<p>The Monday call problem is a data problem. If each location counts leads differently, no comparison means anything.</p>
<p>The minimum standard we put in place:</p>
<ul>
<li><b>A location ID</b> (a short code like HOU-KTY-01) used everywhere: CRM, UTM tags, ad set names, call tracking, the club management software.</li>
<li><b>One UTM convention</b>: <code>utm_source=meta</code>, <code>utm_medium=paid_social</code>, <code>utm_campaign=2027-01_newyear_HOU-KTY-01</code>. Write it down, and reject links that don’t follow it.</li>
<li><b>One definition per stage.</b> A lead, a booked tour, a show, a trial, a join and a cancel each mean exactly one thing, system-wide.</li>
<li><b>Call tracking numbers per location and per channel</b>, with calls recorded where legal.</li>
<li><b>Lead source written into the member record</b>, so a join in the club management software can be traced back to the ad. Without this, you’ll never know your real cost per member.</li>
<li><b>Offline conversions</b> (tours and joins) sent back to Google Ads and Meta, so the platforms optimize for members instead of form fills.</li>
</ul>
<p>Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'guide to tracking forms and calls in GA4 and Google Ads')} covers the plumbing.</p>
<p>KPI definitions that should be identical everywhere:</p>
<div class="bp-tbl"><table>
<thead><tr><th>KPI</th><th>Formula</th></tr></thead>
<tbody>
<tr><td>Cost per lead</td><td>Local media spend ÷ leads</td></tr>
<tr><td>Lead-to-tour rate</td><td>Booked tours or trials ÷ leads</td></tr>
<tr><td>Close rate</td><td>Joins ÷ tours or trials attended</td></tr>
<tr><td>Cost per join</td><td>Local media spend ÷ new joins attributed to paid media</td></tr>
<tr><td>Net member growth</td><td>Joins − cancels, for the month</td></tr>
<tr><td>Payback months</td><td>Cost per join ÷ average monthly dues</td></tr>
</tbody></table></div>"""),

            ("Budget allocation by location maturity", f"""<p>A two-year-old location with 1,800 members and a new studio in presale shouldn’t get the same budget, even if the franchise agreement requires the same minimum from both. Here’s how we’d think about it. The percentages are illustrative, not a rule.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Stage</th><th>Goal</th><th>Spend level (illustrative)</th><th>Where it goes</th></tr></thead>
<tbody>
<tr><td>Presale (90 days before opening)</td><td>Founding members, waitlist</td><td>Highest, often a separate launch budget</td><td>Meta lead and conversion campaigns, presale office, launch media</td></tr>
<tr><td>Ramp (months 1-12)</td><td>Reach break-even membership</td><td>Above the system minimum</td><td>Meta, Google search, reviews, referral offers</td></tr>
<tr><td>Mature (year 2+)</td><td>Replace churn, grow slowly</td><td>At the minimum, peaks in January</td><td>Search, retargeting, referrals, retention</td></tr>
<tr><td>Turnaround</td><td>Stop the decline</td><td>Temporarily above minimum, with a fix first</td><td>Offer, reviews and location page fixes before more media</td></tr>
</tbody></table></div>
<!--fig:maturity-->
<p>Two notes. First, January is the biggest month for gyms almost everywhere, so most locations should spend unevenly across the year and a flat monthly minimum works against them. If the agreement allows it, measure the minimum annually. Second, “turnaround” locations usually have a problem that more ads won’t fix: bad reviews, a confusing offer, a weak front desk. Fix those first, or the extra spend just buys more people who don’t join. Our {L('/blog/gym-fitness-studio-marketing-the-woodlands-houston/', 'single-location gym marketing guide')} covers the offer and retention side.</p>"""),

            ("Reporting to franchisees", f"""<p>Franchisees don’t need more dashboards. They need one page a month that answers four questions: what did I spend, what did I get, how does it compare, and what changes next month.</p>
<!--fig:report-->
<p>What makes reporting work:</p>
<ul>
<li><b>Same layout for every location</b>, with the system median next to each number so owners can see where they stand.</li>
<li><b>Members first, leads second.</b> Lead counts make bad months look fine.</li>
<li><b>Local spend and brand fund reported separately</b>, with the brand fund in Item 11 categories.</li>
<li><b>One recommendation per location</b>, specific: “Kingwood’s lead-to-tour rate is half the system median. The leads look fine, so the issue is follow-up time. Average first call is 9 hours.”</li>
<li><b>A quarterly review</b> with each multi-unit owner, walking the numbers in person or on video.</li>
</ul>
<p>For the metrics side in general, see our {L('/blog/measure-marketing-success-metrics/', 'guide to measuring marketing')}.</p>"""),

            ("Mistakes we see in fitness franchise marketing", f"""<ul>
<li><b>Franchisees running their own ad accounts with no shared standards.</b> The brand can’t see results, and owners get sold by whichever agency called last.</li>
<li><b>The brand owning everything and sharing nothing.</b> Franchisees pay for ads they can’t see and stop trusting the fund.</li>
<li><b>Campaign budget optimization across locations</b> that quietly starves the new or struggling ones.</li>
<li><b>One national offer everywhere.</b> A price-led offer that works in a value market can underprice a premium location in The Woodlands or River Oaks.</li>
<li><b>No lead source in the member record</b>, so cost per join is a guess.</li>
<li><b>Template location pages</b> with nothing local on them.</li>
<li><b>Judging locations by cost per lead</b> instead of cost per join and net member growth.</li>
</ul>"""),

            ("A first 90 days for a franchisor marketing team", f"""<p><b>Days 1-30:</b> agree on the location ID, UTM convention and stage definitions. Audit who owns every Meta ad account, Google Ads account and Google Business Profile, and move ownership to the brand’s business accounts with franchisees as users. Pick the Meta setup (ad set per location, dynamic location ads or a local-ads platform).</p>
<p><b>Days 31-60:</b> get lead source flowing into the club management software and offline conversions flowing back to the ad platforms for at least a few pilot locations. Rebuild the location page template so it pulls each location’s schedule, pricing and photos. Set up the Houston co-op agreement if there’s more than one owner in the market.</p>
<p><b>Days 61-90:</b> send the first one-page monthly report to every franchisee, run the first quarterly reviews with multi-unit owners, and set next year’s budget by location stage, with January planned early.</p>
<p>If you run a multi-location fitness brand and want a senior strategist to build a plan for your system, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much do fitness franchisees pay into a marketing fund?",
             "It varies by system and is disclosed in Item 11 of the franchise disclosure document. Planet Fitness, for example, generally collected about 2% of membership dues for its national fund and required 7% of monthly dues for local marketing, and franchisees voted to change that to 3% and 6% for 2026. Other fitness systems use flat monthly local spending minimums instead of percentages."),
            ("What is the difference between a brand fund and local marketing?",
             "The brand fund is money franchisees pay to the franchisor for marketing that benefits every location, such as creative, national media, the website and technology. Local marketing is spending each franchisee must do in their own trade area, usually on approved channels like Meta ads, Google search and events. Co-ops sit in between, pooling local money for shared media in one market."),
            ("How should a fitness franchise run Facebook ads for many locations?",
             "Most systems use one of three setups: one ad set per location with its own radius and budget, one campaign using Meta's dynamic location fields so each ad shows the nearest location's details, or a local-ads platform with brand-approved templates. If you use campaign budget optimization across locations, set ad set spend limits so budget stays with the locations that paid for it."),
            ("What should a franchisor report to franchisees about marketing?",
             "Send one page per location each month showing local spend, leads, tours, joins, cost per join and net member growth, with the system median beside each number and one specific recommendation. Report brand fund spending separately, using the same production, media and administration categories as Item 11 of the FDD, so franchisees can compare it to what they were told."),
            ("Does the FTC Franchise Rule affect franchise marketing?",
             "Yes, in two main ways. Item 11 of the disclosure document must describe the advertising fund, including contributions, administration, audits and how money was spent on production, media and administration. And franchise recruitment marketing has to be careful with earnings claims, since financial performance representations need a reasonable basis and must be included in Item 19. Have franchise counsel review fund and recruitment materials."),
        ],
        "figures": {
            "split": {
                "type": "compare",
                "title": "What the brand fund vs. local budget should pay for",
                "left": {"title": "Brand fund (central)", "items": ["Brand creative and templates", "National or regional awareness media", "Website, app and CRM", "Location page template", "Reporting tools"]},
                "right": {"title": "Local budget (each location)", "items": ["Google search around the location", "Meta ads in the trade area", "Local events and partnerships", "Presale and reopening pushes", "Review requests and referral offers"]},
                "alt": "Comparison of brand fund and local marketing spending for a fitness franchise with locations in Houston and The Woodlands",
                "caption": "Central money for scale, local money for anything that depends on a trade area.",
            },
            "meta": {
                "type": "checklist",
                "title": "Meta setup checklist for multi-location fitness brands",
                "sub": "Before you scale local ads across locations",
                "items": ["Brand owns every ad account in its Business Manager", "Clean parent Page with child location Pages", "Location ID in every ad set and campaign name", "Radius set per location, not one radius for all", "Ad set spend limits if using campaign budget", "Templates with real footage from each location", "Lead source passed into the CRM and member record", "Offline joins sent back to Meta"],
                "alt": "Checklist for running Meta ads across multiple fitness franchise locations in Houston and The Woodlands",
                "caption": "The second item is what dynamic location ads depend on, and many brands skip it.",
            },
            "maturity": {
                "type": "bars",
                "title": "Example local spend by location stage",
                "sub": "Monthly local media, per location",
                "items": [["Presale", 100, "$12,000"], ["Ramp (months 1-12)", 50, "$6,000"], ["Turnaround", 42, "$5,000"], ["Mature (year 2+)", 33, "$4,000"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of example fitness franchise local marketing spend by location maturity in Houston, from presale to mature",
                "caption": "Illustrative. Real numbers depend on the concept, the trade area and the franchise agreement.",
            },
            "report": {
                "type": "steps",
                "title": "The one-page monthly franchisee report",
                "sub": "Same layout for every location",
                "steps": [["Spend", "Local media and co-op share, separate from the brand fund."], ["Results", "Leads, tours, joins, cancels, net member growth."], ["Efficiency", "Cost per lead, cost per join, payback months."], ["Comparison", "Each number next to the system median."], ["Next month", "One specific recommendation for this location."]],
                "alt": "Steps in a monthly marketing report for fitness franchise owners in Houston and The Woodlands",
                "caption": "If an owner can’t read it in five minutes, it’s too long.",
            },
        },
    },
]
