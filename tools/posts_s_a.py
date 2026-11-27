"""Refresh batch (posts_s_a): three existing thin posts rewritten in place, same slugs.

1. grand-opening-marketing-plan-30-days (countdown / day-by-day format)
2. small-business-marketing-ideas-the-woodlands (ranked directory by cost and effort)
3. med-spa-marketing-the-woodlands-houston (rules-first channel guide)

Research: Google Business Profile help on future opening dates (date up to a year ahead, profile shows 90 days before,
"Recently opened" for 90 days, no reviews or photo edits before opening); The Woodlands Commercial Planning and Design
Standards (Aug 2026, grand opening banner rule 6.7.H) and Houston's Limited Use Banner application, as summarized in
our sign rules post; The Woodlands Area Chamber join page (ribbon cutting at Small Business and Community tiers);
Community Impact's "now open / coming soon" roundups; FTC Disclosures 101 for influencers; Google Maps prohibited
content policy (review incentives); Morgan Lewis on the FTC consumer reviews rule (effective Oct 21, 2024); Texas
Secretary of State telephone solicitation FAQ and National Law Review on SB 140; BrightLocal Local Consumer Review
Survey 2026 (97% read reviews, 47% avoid businesses with fewer than 20 reviews, 74% only consider reviews from the last
three months, 31% only use 4.5 stars or higher, 45% use AI tools for recommendations); Census QuickFacts for The
Woodlands CDP (114,436 in 2020, $140,701 median household income, 2.73 persons per household); The Woodlands Township
village associations page; Woodlands Online Sports sponsorship notice; Township 2026 Red, Hot & Blue release;
Community Impact on the Waterway Arts Festival; USPS EDDM page.
Med spa: TDLR medical spa page (TDLR licenses establishments and estheticians, not med spas; injectables and medium or
deep peels are medical acts under the Texas Medical Board); TDLR laser hair removal FAQ (facility per location,
consulting physician contract, four certificate levels); Texas Health & Safety Code 401.518 (no "free from risk" or
"medical benefit" claims for laser hair removal); Polsinelli on HB 3749 (Jenifer's Law, effective Sept 1, 2025);
ABC13 on a Magnolia med spa operator's 2025 arrest; AmSpa 2024 State of the Industry recap (10,488 med spas in 2023,
$1,398,833 average revenue, $527 per visit, 73% repeat patients); AmSpa summary of ASPS 2025 statistics
(neuromodulators 50% and HA fillers 30% of minimally invasive procedures); Google Ads restricted drug terms and
prescription drug services policies; Meta's cosmetic procedures (18+) and personal health and appearance policies.
First Byte case studies cited are the published SkinLab by Dr. Roth, Toasted Yolk and Equinox pages on this site.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

SRC = {
    # grand opening
    "gbp_open": A("https://support.google.com/business/answer/9174409?hl=en", "Google’s help page on opening dates"),
    "tw_std": A("https://www.thewoodlandstownship-tx.gov/files/sharedassets/main/v/2/covenant-administration/documents/commercial-planning-and-design-standards-aug-2026-recorded.pdf", "The Woodlands Commercial Planning and Design Standards"),
    "hou_lub": A("https://www.houstonpermittingcenter.org/media/5611/download", "Limited Use Banner application"),
    "chamber": A("https://www.woodlandschamber.org/join/", "The Woodlands Area Chamber’s join page"),
    "ci_round": A("https://communityimpact.com/the-woodlands/business/26-businesses-now-open-coming-soon-and-announcing-news-in-the-woodlands-area/", "a March 2024 Woodlands roundup"),
    "ftc101": A("https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers", "the FTC’s Disclosures 101 guide"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy for Maps"),
    "ftc_rev": A("https://www.morganlewis.com/pubs/2024/08/ftc-issues-final-rule-on-consumer-reviews-and-testimonials", "the FTC’s consumer reviews rule"),
    "sos": A("https://www.sos.texas.gov/statdoc/faqs3400.shtml", "the Texas Secretary of State’s FAQ"),
    "nlr140": A("https://natlawreview.com/article/texas-sb-140-after-november-settlement-consent-cold-texting-out", "National Law Review"),
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    # small business ideas
    "census": A("https://www.census.gov/quickfacts/fact/table/thewoodlandscdptexas/PST045224", "Census QuickFacts for The Woodlands"),
    "villages": A("https://www.thewoodlandstownship-tx.gov/villageassociations", "The Woodlands Township’s village association page"),
    "wos": A("https://business.woodlandschamber.org/news/details/woodlands-online-sports-2025-26-sponsorships-opportunities-start-august-1-07-17-2025", "Woodlands Online Sports’ 2025-26 sponsorship notice"),
    "rhb": A("https://www.thewoodlandstownship-tx.gov/Township-News/2026-Press-Releases/June/061826-Red-Hot-Blue", "the Township’s 2026 Red, Hot &amp; Blue release"),
    "waaf": A("https://communityimpact.com/the-woodlands/arts-entertainment/the-woodlands-waterway-arts-festival-brings-outdoor-art-to-the-woodlands-since-2005/", "Community Impact"),
    "eddm": A("https://www.usps.com/business/every-door-direct-mail.htm", "USPS’s EDDM page"),
    "mag": A("https://www.thewoodlandstownship-tx.gov/Departments/Communications/Community-Magazine", "the Township’s community magazine page"),
    # med spa
    "tdlr_ms": A("https://www.tdlr.texas.gov/barbering-and-cosmetology/medical-spas.htm", "TDLR’s medical spa page"),
    "tdlr_lhr": A("https://www.tdlr.texas.gov/las/lasfaq.htm", "TDLR’s laser hair removal FAQ"),
    "hsc518": A("https://texas.public.law/statutes/tex._health_and_safety_code_section_401.518", "Section 401.518 of the Health and Safety Code"),
    "hb3749": A("https://www.polsinelli.com/publications/new-texas-iv-therapy-law", "Polsinelli’s summary of HB 3749"),
    "abc13": A("https://abc13.com/post/conroe-woman-accused-practicing-medicine-injecting-botox-other-procedures-license-records-state/17732424/", "ABC13 reported"),
    "amspa": A("https://www.americanmedspa.org/blog/2024-medical-spa-state-of-the-industry-executive-report", "AmSpa’s 2024 State of the Industry recap"),
    "asps": A("https://www.americanmedspa.org/news/asps-2025-statistics-report-highlights-continued-demand-for-aesthetic-treatments-volume-restoration-and-healthy-aging/", "AmSpa’s summary of the ASPS 2025 statistics"),
    "g_drug": A("https://support.google.com/adspolicy/answer/15595717?hl=en", "Google’s restricted drug terms policy"),
    "g_rxsvc": A("https://support.google.com/adspolicy/answer/15598647", "prescription drug services policy"),
    "meta_cos": A("https://transparency.meta.com/policies/ad-standards/content-specific-restrictions/cosmetic-procedures-and-wellness", "Meta’s cosmetic procedures policy"),
    "meta_pha": A("https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-health-and-appearance", "personal health and appearance policy"),
}

GO = "/blog/grand-opening-marketing-plan-30-days/"
IDEAS = "/blog/small-business-marketing-ideas-the-woodlands/"
MEDSPA = "/blog/med-spa-marketing-the-woodlands-houston/"

POSTS = [
    # ------------------------------------------------------------------ post 1: grand opening countdown
    {
        "slug": "grand-opening-marketing-plan-30-days",
        "date": "2026-09-14",
        "modified": "2026-11-27",
        "title": "The 30-Day Grand Opening Marketing Plan for Houston and The Woodlands Businesses",
        "seo_title": "30-Day Grand Opening Marketing Plan: Houston & The Woodlands",
        "desc": "A day-by-day 30-day grand opening marketing plan for Houston and The Woodlands: Google profile, waitlist, local ads, banners, ribbon cutting and reviews.",
        "category": "Strategy",
        "icons": ["Google Business Profile", "Meta", "Instagram"],
        "art": "b2",
        "hero": "clock",
        "hero_alt": "Illustration of a countdown clock for a 30-day grand opening marketing plan in Houston and The Woodlands",
        "related": ["gym-presale-new-location-membership-launch", "get-press-coverage-houston-the-woodlands", "business-sign-rules-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Thirty days is enough time to open busy. It is not enough time to get a Google Business Profile verified if you start on day 29 and the video gets rejected twice.</p>
<p>That’s the pattern we see with most openings around Houston and The Woodlands. The build-out runs late, the owner is buried in inspections and hiring, and marketing starts when the sign goes up. By then the cheap wins are gone.</p>
<p><b>The short answer:</b> a 30-day grand opening marketing plan gets your Google Business Profile verified with an opening date, puts a location page live, builds a waitlist with a real reason to join, runs tight-radius Meta and Google ads, hosts a soft opening for neighbors and creators, makes opening week an event, and plans for the dip in week three.</p>
<p>Below is the countdown we’d run for a café, salon, clinic, gym or shop opening anywhere from Market Street to Katy. Every step has a day number. Steal the table, put your opening date at the top, and work backward.</p>
<!--fig:gbpdates-->"""),

            ("What should you do before the 30-day countdown starts?", f"""<p>Three things take longer than owners expect, so start them as soon as you have a signed lease and a realistic opening month.</p>
<p><b>Your Google Business Profile.</b> Google lets you enter an opening date up to one year ahead, and only the year and month are required. Once the profile is verified, it shows on Google 90 days before that date, and after you open it carries a “Recently opened” tag for 90 days, per {SRC['gbp_open']}. Before opening, you can post announcements and opening offers and add construction photos. Customers can’t leave reviews until you’re open. Verification is often a video now, and our {L('/blog/google-business-profile-video-verification/', 'video verification shot list')} covers what Google wants on camera (hard when the storefront is still drywall).</p>
<p><b>Signs and banners.</b> In The Woodlands, a grand opening banner needs approval before it goes up. Under Section 6.7.H of {SRC['tw_std']}, it can be up to 3 by 8 feet on a neutral background, displayed from four weeks before opening to two weeks after. Inside the City of Houston, the closest thing is a Limited Use Banner: seven consecutive days in any 30, up to 40 square feet, flush on the wall, with a permit each time, per the city’s {SRC['hou_lub']}. Our {L('/blog/business-sign-rules-the-woodlands-houston/', 'sign rules guide')} has the rest, including unincorporated Harris County.</p>
<p><b>A phone number and an inbox someone actually answers.</b> Get the permanent number before anything prints. Changing it later splits your listings.</p>
<p>If you’re reading this with fewer than 30 days left, do these first anyway and accept that the profile may go live late. Everything else in the plan still works.</p>"""),

            ("The 30-day grand opening countdown at a glance", f"""<p>Here’s the whole plan on one page. “T” is opening day. Owners are suggestions; in a small business it’s often the same person in four hats.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Day</th><th>Task</th><th>Who</th><th>Done when</th></tr></thead>
<tbody>
<tr><td>T-30</td><td>Profile verified with opening date; location page live; waitlist form and offer live</td><td>Owner, web</td><td>You can find yourself on Google Maps and sign up for the list on a phone</td></tr>
<tr><td>T-28</td><td>Claim Apple Business Connect, Bing Places, Yelp and Facebook; same name, address, phone everywhere</td><td>Owner</td><td>Listings match character for character</td></tr>
<tr><td>T-28</td><td>Submit banner for approval (Township or city)</td><td>Owner, sign shop</td><td>Approval in writing</td></tr>
<tr><td>T-25</td><td>Pixel and conversion tracking on the site; waitlist ads start in a tight radius</td><td>Marketing</td><td>Test sign-up shows in Meta Events Manager and Google Ads</td></tr>
<tr><td>T-21</td><td>Pitch the opening to Community Impact and local outlets; book the chamber ribbon cutting</td><td>Owner</td><td>Date on the chamber calendar</td></tr>
<tr><td>T-18</td><td>Invite neighbors, HOAs, nearby offices and 6-10 local creators to a preview</td><td>Owner, marketing</td><td>RSVPs in a spreadsheet</td></tr>
<tr><td>T-10</td><td>Soft opening or preview night; film everything</td><td>Everyone</td><td>Raw footage and photos in one shared folder</td></tr>
<tr><td>T-7</td><td>Ads switch from waitlist to RSVP, booking or order-ahead; creator posts go live</td><td>Marketing</td><td>New ads approved and spending</td></tr>
<tr><td>T-3</td><td>Staff trained on the review ask, phones and the opening offer</td><td>Manager</td><td>Every person can say the offer in one sentence</td></tr>
<tr><td>T</td><td>Opening day: ribbon cutting, offer, content capture, Google Ads on</td><td>Everyone</td><td>You counted visitors, not just sales</td></tr>
<tr><td>T+7</td><td>Second-visit offer to everyone who came; waitlist follow-up to no-shows</td><td>Marketing</td><td>Email and SMS sent to opted-in contacts</td></tr>
<tr><td>T+30</td><td>Review the numbers; set the always-on budget</td><td>Owner</td><td>One-page scorecard</td></tr>
</tbody></table></div>
<!--fig:countdown-->"""),

            ("Days 30 to 22: get found and start the list", f"""<p>Before anyone sees an ad, three pages need to exist. People will look you up the second they hear about you.</p>
<p><b>A location page</b> on your own site with the address, a map, hours (opening week and normal), parking, the opening date and the offer. If you’re in a center with a parking garage or a confusing entrance, say which entrance. If you’re off Research Forest or Woodlands Parkway, say which side of the road. Small stuff, and it saves you from a lot of “where are you?” calls. Our guide to {L('/blog/power-of-local-landing-pages/', 'local landing pages')} goes deeper.</p>
<p><b>The Google Business Profile</b> filled out the way you’d fill out a lease application: primary category chosen carefully, services listed, a description that says what you sell and where, the opening date, exterior photos so people recognize the building.</p>
<p><b>A waitlist form</b> with a reason to join. “Sign up for updates” gets you your mom and two employees. Something with a limit works better:</p>
<ul>
<li>A café: free drip coffee for the first week for the first 300 on the list.</li>
<li>A salon or med spa: founding-client pricing on one service, good through the first 60 days.</li>
<li>A gym or studio: a founding rate with a hard cap. Our {L('/blog/gym-presale-new-location-membership-launch/', 'gym presale guide')} covers this model end to end.</li>
<li>A shop: an invite to a preview night plus a small credit.</li>
</ul>
<p>Collect name, email and mobile, and add a separate unchecked box for text messages. Texas SB 140 brought marketing texts under the state’s telephone solicitation law in September 2025; after a November 2025 court order, {SRC['sos']} says a business texting with prior consent doesn’t need to file the registration statement. {SRC['nlr140']} is clear that cold texting and purchased lists are still exposed. So text people who opted in, and nobody else. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} has the details.</p>
<p>Start the waitlist ads around day 25, once tracking fires on a test sign-up. Before that you’re paying for clicks you can’t count.</p>"""),

            ("Days 21 to 8: build local buzz without burning the budget", f"""<p>This is where most of the money goes, and where most of it gets wasted on people who will never drive to you.</p>
<p><b>Keep the radius honest.</b> People in The Woodlands rarely cross I-45 for a coffee. They’ll drive 15 minutes for a dentist and 25 for a specialist. Set your Meta and Google radius by category, and exclude what doesn’t fit. A Hughes Landing café might target three to five miles. A clinic in Spring might reach Klein, Tomball and The Woodlands. Don’t pick “Houston” as the target, ever. Houston is 600-plus square miles.</p>
<!--fig:radius-->
<p><b>Creator preview.</b> Invite six to ten local creators who actually live here (check their audience location if they’ll share it) and a few nearby business owners. Give them the real experience, not a special one. They post if they want to, and any free product or service gets disclosed as a paid or gifted partnership. {SRC['ftc101']} spells out what “clear and conspicuous” means. Ask permission to run their best clip as an ad from their handle in opening week; it tends to beat anything your brand account posts. See our {L('/blog/ftc-rules-influencer-partnerships/', 'influencer disclosure guide')} for the paperwork.</p>
<p><b>Local press.</b> Community Impact runs “now open, coming soon” roundups; {SRC['ci_round']} listed 26 businesses, each with an address, a date and a short description. That’s the easiest press slot in town. Send the reporter covering your edition a short email three to four weeks out with the name, address, date, what you sell and one good photo. Our {L('/blog/get-press-coverage-houston-the-woodlands/', 'press coverage guide')} lists the other outlets.</p>
<p><b>The ribbon cutting.</b> Per {SRC['chamber']}, the $500 Small Business membership includes a ribbon cutting at the Chamber office, and the $1,000 Community tier includes one within 12 miles, which means at your door. If your customers are local, that photo and the chamber’s social post are worth more than the scissors suggest. The {L('/blog/chambers-networking-groups-the-woodlands-houston/', 'chamber directory')} compares the Spring, Tomball, Conroe and Houston options.</p>
<p><b>Neighbors.</b> Walk the center with a flyer and a free-item card for the staff of every business near you. Email the property manager. If you’re near a village center, reach the village association; {SRC['villages']} lists them. Office parks off Research Forest and Lake Robbins have hundreds of people who eat lunch somewhere.</p>"""),

            ("How much should a grand opening marketing budget be in Houston?", f"""<p>Honest answer: it depends on what one customer is worth to you over a year, and there isn’t a published Houston benchmark worth trusting. What we can give you is how we’d split it.</p>
<p>For a small café, salon or shop, we’d plan somewhere around $1,500 to $5,000 in ad spend across the six weeks around opening, plus the cost of the offer itself. A clinic, gym or anything with a high lifetime value can justify more, and often has to, because the competitors bidding on “near me” searches are established. Treat those ranges as our experience, not a rule. Our {L('/blog/set-a-marketing-budget-small-business/', 'budget guide')} shows how to work it from your own numbers.</p>
<!--fig:budget-->
<p>Two things we’d keep out of the opening budget. A billboard, because one opening week isn’t long enough for outdoor to work. And a big print run of flyers with a QR code nobody tracks. If you want mail, our {L('/blog/eddm-direct-mail-cost-the-woodlands-houston/', 'EDDM cost guide')} shows how to do it with routes you can measure.</p>"""),

            ("Days 7 to 1: turn interest into plans", f"""<p>A week out, the ads change jobs. Awareness is done. Now each ad should ask for one action: RSVP for the ribbon cutting, book an appointment, order ahead, claim the founding rate.</p>
<ul>
<li>Retarget everyone who watched your videos, visited the location page or joined the list. These are small audiences, so cap frequency or they’ll see you six times a day.</li>
<li>Run the creator clips you got permission for as ads.</li>
<li>Email the waitlist twice: once with the date and offer, once the day before. Text the people who opted in, between normal hours.</li>
<li>Answer every comment and DM within the hour. New businesses get questions about parking, pricing and whether you take insurance, and slow answers look like a business that isn’t ready. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the math on response time.</li>
</ul>
<p>Then train the staff. Every person who touches a customer should be able to say the opening offer in one sentence and ask for a review without sounding like a script. A version that works:</p>
<p><i>“We just opened and Google reviews make a huge difference for us. If you had a good time, would you leave one? The QR code on the counter goes straight there.”</i></p>
<!--fig:openday-->"""),

            ("Opening week: make it an event people can plan around", f"""<p>A ribbon cutting at 10 a.m. on a Tuesday gets the chamber photo and not much else. Pick the time your customers are free. For most Woodlands consumer businesses that means Saturday morning, or a weekday evening if you sell to people who work.</p>
<p>Make the offer time-boxed and simple. “Free kids’ meal with any entrée through Sunday” beats “20% off” because it’s easier to repeat and doesn’t train people to wait for a discount. Turn on Google Ads for your brand name and your main category plus your area (“brunch The Woodlands,” “nail salon Spring TX”) so the people who heard about you find you instead of the competitor bidding on their way in.</p>
<p>Capture content all week: the line, the first customer, staff in action, the ribbon. Vertical video, natural light. That footage feeds your ads and posts for the next month.</p>
<p>And ask for reviews, in person, all week. Don’t trade anything for them. {SRC['gpol']} bans offering incentives for reviews, and {SRC['ftc_rev']} (in effect since October 2024) prohibits buying reviews conditioned on what they say. A free cookie for a five-star review breaks both. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} covers the ask and the replies.</p>"""),

            ("Days 8 to 30 after opening: plan for the dip", f"""<p>Almost every opening has the same shape. A big first week, a decent second week, and then a third week that makes the owner nervous. The excitement wears off and the regular habits haven’t formed yet.</p>
<!--fig:dip-->
<p>The fix is boring and it works:</p>
<ul>
<li>Send a second-visit offer to everyone who came during opening week, good for the next 21 days.</li>
<li>Follow up with waitlist sign-ups who never showed. A short “we saved your spot” note converts more than you’d think.</li>
<li>Keep search ads on for your category and area. Pull back on awareness ads; keep retargeting.</li>
<li>Post on your Business Profile weekly and reply to every review the same day.</li>
<li>Keep asking for reviews. {SRC['bl']} found 47% of consumers won’t use a business with fewer than 20 reviews, 74% only consider reviews from the last three months, and 31% will only use a business rated 4.5 stars or higher. A brand-new profile with six reviews is losing customers it never hears from.</li>
</ul>
<p>Review velocity in the first month also helps your map pack position. Our guide on {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Houston map pack')} explains the rest of that picture.</p>"""),

            ("What does a grand opening look like when it works?", f"""<p>Two openings we’ve run show the range. For {L('/case-studies/the-toasted-yolk-cafe/', 'The Toasted Yolk Cafe')}, location pages and Business Profiles went live before the doors opened, then grand-opening paid social, creator tastings and RSVP campaigns ran around each launch. Across seven new locations, the case study reports 21 days to No. 1 in the local map pack and 3,200 grand-opening week guests. For {L('/case-studies/equinox/', 'Equinox')}, geo-fenced social and search started 90 days before each new club, with a founding-member offer and an SMS and email nurture; the case study reports 94% capacity on opening day.</p>
<p>The common thread isn’t budget. In both cases the search listings were ready before the hype started, and the follow-up kept going after the ribbon.</p>
<!--fig:quietvsplanned-->"""),

            ("What to track, and the grand opening mistakes we see most", f"""<p>Keep a one-page scorecard. Before opening: waitlist sign-ups, cost per sign-up, RSVPs. Opening week: visitors (count them, even with a clicker), bookings or covers, Business Profile calls and direction requests, reviews collected. Days 8 to 30: repeat visits from the opening-week list, cost per new customer by channel, average rating and review count. If you take calls, give each channel its own tracked number; our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')} covers forms and calls.</p>
<p>The mistakes we see most:</p>
<ul>
<li><b>Starting the Google profile last.</b> No profile, no map listing, no reviews during the one week people are most willing to leave them.</li>
<li><b>Targeting all of Houston.</b> Spend gets spread across Pearland and Baytown when your customers are within ten minutes.</li>
<li><b>A deep discount as the whole plan.</b> You fill the room with deal hunters and teach everyone your real price is 40% off.</li>
<li><b>No one assigned to the phone.</b> Opening week is when calls spike and voicemail fills up.</li>
<li><b>Stopping everything in week two.</b> The dip comes either way. It’s shallower if search and retargeting stay on.</li>
</ul>
<p>If you’re opening a location in The Woodlands, Spring, Conroe or anywhere around Houston and want a senior strategist to build the countdown around your date and budget, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How far in advance should I start marketing a grand opening?",
             "Start the Google Business Profile as soon as you have a lease and an opening month, because Google lets you set an opening date up to a year ahead and shows a verified profile 90 days before it. Paid ads and the waitlist usually start 25 to 30 days out. Banner approvals, chamber ribbon cuttings and press pitches need three to four weeks of lead time in The Woodlands and Houston."),
            ("Can I put up a grand opening banner in The Woodlands?",
             "Yes, with approval first. The Woodlands commercial standards allow a grand opening banner up to 3 by 8 feet on a neutral background, from four weeks before opening to two weeks after, and it must be approved by the Township’s review committee before you install it. Inside the City of Houston, temporary banners go through a Limited Use Banner permit with its own size and time limits."),
            ("Can I give customers a discount for leaving a Google review at my grand opening?",
             "No. Google’s Maps content policy bans offering incentives in exchange for reviews, and the FTC’s consumer reviews rule prohibits paying for reviews that express a particular sentiment. A discount for a five-star review breaks both. Ask every happy customer in person, put a QR code at the counter and send a link afterward, but keep the offer separate from the review ask."),
            ("How do I get my new business in Community Impact in The Woodlands?",
             "Email the reporter who covers business for your edition three to four weeks before you open. Put the news in the first sentence, then the business name, address, opening date, what you sell, a phone number and one good photo. Community Impact runs regular roundups of businesses that are new or coming soon, and a firm opening date with real details is the easiest way into one."),
            ("How do I get a new business on Google Maps before it opens?",
             "Create your Google Business Profile, add the opening date under Edit profile, and complete verification, which is often a short video. Once verified, the profile appears on Google up to 90 days before the date you entered. You can post announcements, opening offers and construction photos before you open, but customers can’t leave reviews until the business is officially open."),
        ],
        "figures": {
            "gbpdates": {
                "type": "stats",
                "title": "Google’s clock for a new business",
                "stats": [["1 year", "How far ahead you can set an opening date"], ["90 days", "Profile shows on Google before opening"], ["90 days", "“Recently opened” tag after you open"], ["0", "Reviews allowed before opening day"]],
                "note": "Source: Google Business Profile help, opening dates",
                "alt": "Stat tiles showing Google Business Profile opening date rules for a grand opening in Houston and The Woodlands",
                "caption": "Get verified early. The 90-day window before opening is free visibility most new businesses never use.",
            },
            "countdown": {
                "type": "steps",
                "title": "The grand opening countdown in five moves",
                "sub": "T is opening day",
                "steps": [["T-30: Get found", "Verified profile with opening date, location page and a waitlist with a capped offer."], ["T-25: Start the list", "Tracking first, then tight-radius waitlist ads on Meta."], ["T-21: Build buzz", "Press pitch, ribbon cutting booked, creator and neighbor preview invites."], ["T-7: Ask for action", "Ads switch to RSVP, booking or order-ahead. Staff trained on the review ask."], ["T+8 to T+30: Beat the dip", "Second-visit offer, waitlist follow-up, search on, reviews every day."]],
                "alt": "Five-step grand opening marketing countdown for a new business in The Woodlands and Houston",
                "caption": "Work backward from your opening date and put a real day number on each step.",
            },
            "radius": {
                "type": "map",
                "title": "Set your ad radius by how far people will drive",
                "sub": "Rings are 10, 20 and 30 miles from The Woodlands",
                "highlight": ["The Woodlands", "Spring", "Shenandoah", "Conroe", "Tomball"],
                "note": "A café should stay well inside the first ring. A specialist clinic might reach the second.",
                "alt": "Map of The Woodlands, Spring, Conroe and Tomball with distance rings for grand opening ad targeting near Houston",
                "caption": "Targeting “Houston” spends your opening budget in places your customers don’t live.",
            },
            "budget": {
                "type": "bars",
                "title": "How we’d split a $3,000 opening ad budget",
                "sub": "Six weeks around opening day, small consumer business",
                "items": [["Meta waitlist and RSVP ads", 1200, "$1,200"], ["Google Search (brand + category)", 900, "$900"], ["Creator clips run as ads", 500, "$500"], ["Retargeting after opening", 400, "$400"]],
                "highlight": [0],
                "note": "Illustrative example. The offer itself, printing and the event are separate costs.",
                "alt": "Bar chart of an illustrative grand opening ad budget split for a small business in The Woodlands and Houston",
                "caption": "Weight the money toward the waitlist early and search once you’re open.",
            },
            "openday": {
                "type": "checklist",
                "title": "Opening-day checklist",
                "sub": "Tape it to the back office door",
                "items": ["Profile hours match the door", "Google Ads brand and category campaigns on", "Review QR code at every register", "Every staffer can say the offer in one line", "Someone owns the phone and DMs all day", "Clicker or count sheet at the door", "One person filming vertical video", "Second-visit offer cards ready to hand out"],
                "alt": "Grand opening day checklist for a new business in Houston and The Woodlands",
                "caption": "Most of these take five minutes. Skipping them costs you the week.",
            },
            "dip": {
                "type": "columns",
                "title": "The week-three dip",
                "sub": "Weekly visits after a typical opening, as a share of opening week",
                "labels": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 6", "Week 8"],
                "values": [100, 78, 55, 62, 70, 74],
                "highlight": [2],
                "y_label": "Visits",
                "note": "Illustrative example of the pattern, not a benchmark.",
                "alt": "Column chart showing the week-three traffic dip after a grand opening in The Woodlands and Houston",
                "caption": "Second-visit offers and always-on search make the dip shallower and the recovery faster.",
            },
            "quietvsplanned": {
                "type": "compare",
                "title": "Quiet opening vs. planned opening",
                "left": {"title": "Opened quietly", "items": ["Profile verified after opening", "Ads target all of Houston", "One big discount", "Reviews trickle in", "Marketing stops in week two"]},
                "right": {"title": "Ran the countdown", "items": ["Profile live 30-90 days early", "Radius set by drive time", "Capped founding offer", "Review ask trained and daily", "Search and retargeting stay on"]},
                "alt": "Comparison of a quiet opening and a planned grand opening for businesses in Houston and The Woodlands",
                "caption": "Same rent, same build-out. Very different first quarter.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: small business marketing ideas
    {
        "slug": "small-business-marketing-ideas-the-woodlands",
        "date": "2026-10-02",
        "modified": "2026-11-27",
        "title": "25 Small Business Marketing Ideas for The Woodlands, Ranked by Cost and Effort",
        "seo_title": "25 Small Business Marketing Ideas for The Woodlands",
        "desc": "25 small business marketing ideas for The Woodlands and North Houston, ranked by cost and weekly effort, with a 90-day plan for picking the three that fit.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Nextdoor", "Instagram"],
        "art": "b4",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for small business marketing ideas in The Woodlands and North Houston",
        "related": ["chambers-networking-groups-the-woodlands-houston", "local-sponsorships-youth-sports-the-woodlands-houston", "eddm-direct-mail-cost-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>“I’ve got maybe five hours a week and a few hundred bucks a month. What do I do first?”</p>
<p>Some version of that question comes from almost every small business owner in The Woodlands who calls us. The honest answer is that a list of 25 ideas is useless until you know which three to do, so this version ranks every idea by what it costs, how many hours a week it takes, and who it suits.</p>
<p><b>The short answer:</b> the best small business marketing ideas in The Woodlands are the cheap ones done consistently. Complete your Google Business Profile, ask every happy customer for a review, build a page for each service and nearby town, and show up locally through the chamber, youth sports and village events. Add paid ads only once you can track calls and forms.</p>
<p>The ideas are grouped in three tiers: free, under $500 a month, and $500 to $2,500 a month. Pick from the top tier first.</p>
<!--fig:market-->"""),

            ("Who you’re marketing to in The Woodlands", f"""<p>The Woodlands had 114,436 residents at the 2020 census, a median household income of $140,701 and 2.73 people per household, per {SRC['census']}. That describes a lot of families with two incomes, kids in activities and not much free time. They’re picky, they read reviews, and they ask neighbors.</p>
<p>The trade area is bigger than the Township, though. Shenandoah, Oak Ridge North and Spring sit on the south and east, Conroe to the north, Magnolia and Tomball to the west. People cross those lines all the time for work and school, and a business near Research Forest or Woodlands Parkway might draw from all of them. They don’t cross I-45 for everything, and they rarely drive down to the Galleria for something they can get on Market Street.</p>
<!--fig:tradearea-->
<p>The Township is also split into villages, each with its own association, listed on {SRC['villages']}. That matters for anything hyperlocal: Nextdoor, sponsorships, mail routes and village events all line up with those boundaries more than with ZIP codes.</p>"""),

            ("All 25 ideas at a glance", f"""<p>Costs are rough and in our experience; hours are a typical week once the thing is set up.</p>
<div class="bp-tbl"><table>
<thead><tr><th>#</th><th>Idea</th><th>Cost</th><th>Hours/week</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>1</td><td>Complete Google Business Profile</td><td>$0</td><td>2 (once)</td><td>Everyone</td></tr>
<tr><td>2</td><td>Weekly Business Profile posts</td><td>$0</td><td>0.5</td><td>Everyone</td></tr>
<tr><td>3</td><td>Ask every customer for a review</td><td>$0</td><td>0.5</td><td>Everyone</td></tr>
<tr><td>4</td><td>Reply to every review</td><td>$0</td><td>0.5</td><td>Everyone</td></tr>
<tr><td>5</td><td>One page per service</td><td>$0-$1,500</td><td>2 (once)</td><td>Service businesses</td></tr>
<tr><td>6</td><td>Town pages for Spring, Conroe, Magnolia, Tomball</td><td>$0-$1,500</td><td>2 (once)</td><td>Businesses that travel</td></tr>
<tr><td>7</td><td>FAQ sections for search and AI answers</td><td>$0</td><td>1</td><td>Everyone</td></tr>
<tr><td>8</td><td>Fix site speed and the phone layout</td><td>$0-$800</td><td>Once</td><td>Everyone</td></tr>
<tr><td>9</td><td>Nextdoor business page and helpful answers</td><td>$0</td><td>1</td><td>Home services, retail</td></tr>
<tr><td>10</td><td>Join a chamber and actually go</td><td>$500+/yr</td><td>2</td><td>B2B, professional services</td></tr>
<tr><td>11</td><td>Sponsor a youth team or school event</td><td>$150-$1,500</td><td>0.5</td><td>Family-facing businesses</td></tr>
<tr><td>12</td><td>Partner with a complementary business</td><td>$0-$200</td><td>1</td><td>Retail, wellness, home</td></tr>
<tr><td>13</td><td>Show up at village and Township events</td><td>$100-$1,000</td><td>Event days</td><td>Consumer brands</td></tr>
<tr><td>14</td><td>Seasonal hooks (hurricane, back to school, holidays)</td><td>$0</td><td>1</td><td>Everyone</td></tr>
<tr><td>15</td><td>Short phone videos, twice a week</td><td>$0</td><td>1.5</td><td>Anyone with a visual product</td></tr>
<tr><td>16</td><td>A monthly email</td><td>$0-$50/mo</td><td>1</td><td>Repeat-purchase businesses</td></tr>
<tr><td>17</td><td>A referral program</td><td>Cost of reward</td><td>0.5</td><td>Services with high ticket</td></tr>
<tr><td>18</td><td>Geo-targeted Meta ads</td><td>$300-$900/mo</td><td>1</td><td>Restaurants, retail, fitness</td></tr>
<tr><td>19</td><td>Google Search ads</td><td>$500-$2,500/mo</td><td>1</td><td>Anyone people search for</td></tr>
<tr><td>20</td><td>Local Services Ads</td><td>Pay per lead</td><td>1</td><td>Home and professional services</td></tr>
<tr><td>21</td><td>Paid local creators</td><td>$200-$1,500/post</td><td>1</td><td>Restaurants, beauty, fitness</td></tr>
<tr><td>22</td><td>EDDM postcards on chosen routes</td><td>From postage + print</td><td>Per drop</td><td>Home services, new openings</td></tr>
<tr><td>23</td><td>Retargeting site visitors</td><td>$150-$400/mo</td><td>0.5</td><td>Anyone with web traffic</td></tr>
<tr><td>24</td><td>Call and form tracking</td><td>$30-$100/mo</td><td>Once</td><td>Anyone running ads</td></tr>
<tr><td>25</td><td>Memberships or maintenance plans</td><td>$0</td><td>2 (once)</td><td>Services with repeat need</td></tr>
</tbody></table></div>
<!--fig:tiers-->"""),

            ("Free small business marketing ideas (cost: your time)", f"""<h3>1. Complete your Google Business Profile</h3>
<p>Every category that’s true, every service, hours including holidays, attributes, a description, products if you sell them, 20-plus real photos. It’s the listing people see before your website, and in The Woodlands it’s often the only thing they see. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers the ranking side.</p>
<!--fig:gbpcheck-->
<h3>2. Post on your profile weekly</h3>
<p>An offer, a new project, an event. Five minutes, a photo from your phone. It keeps the profile looking alive to people comparing you with the shop next door.</p>
<h3>3. Ask every happy customer for a review</h3>
<p>In person first, then a text or email with the direct link. No discounts in exchange; Google bans review incentives outright. {SRC['bl']} found 97% of consumers read reviews for local businesses and 74% only consider ones from the last three months, so a steady trickle beats a burst every spring. The {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has scripts.</p>
<h3>4. Reply to every review</h3>
<p>Thank the good ones by name and mention the service. Answer the bad ones once, calmly, with a way to reach you offline. Future customers read the replies more than the complaint.</p>
<h3>5. Build one page per service</h3>
<p>A plumber with one “Services” page listing 14 things will lose “water heater replacement The Woodlands” to someone with a page about water heaters. Each page: what it is, what it costs (a range is fine), how long it takes, photos, FAQs.</p>
<h3>6. Build town pages that are actually about the town</h3>
<p>Spring, Conroe, Magnolia, Tomball, Kingwood. Each page should mention real work you’ve done there, drive times, anything local that matters to the service (septic in rural Magnolia, older plumbing in Panther Creek). Swapping the town name into the same paragraph doesn’t count. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages post')} shows the difference.</p>
<h3>7. Add FAQ sections</h3>
<p>Write down the questions customers ask on the phone and answer them on the site in plain language. It helps with search, and {SRC['bl']} found 45% of consumers now use ChatGPT or similar tools for local recommendations. Those tools pull from pages that answer questions clearly. See {L('/blog/show-up-in-chatgpt-ai-search-aeo/', 'how to show up in AI search')}.</p>
<h3>8. Fix the phone experience</h3>
<p>Tap-to-call at the top, a form with four fields or fewer, a page that loads in a couple of seconds on a phone in a parking lot. Our {L('/blog/how-fast-should-your-website-load/', 'site speed guide')} has the targets.</p>
<h3>9. Be useful on Nextdoor</h3>
<p>Claim the business page, then answer recommendation threads like a neighbor, not a billboard. One helpful answer in a village group can outperform a month of posts. Whether to pay for Nextdoor ads is a separate question we cover in {L('/blog/is-nextdoor-advertising-worth-it/', 'is Nextdoor advertising worth it')}.</p>"""),

            ("Small business marketing ideas under $500 a month", f"""<h3>10. Join a chamber and show up</h3>
<p>{SRC['chamber']} lists a $500 Small Business tier that includes a ribbon cutting and a networking breakfast credit. The membership only pays off if you go to things. For B2B and professional services it’s often the best $500 you’ll spend; for a café it’s mostly goodwill. Compare the options in our {L('/blog/chambers-networking-groups-the-woodlands-houston/', 'chamber guide')}.</p>
<h3>11. Sponsor a youth team or school event</h3>
<p>Booster clubs and neighborhood leagues sell banners and jersey spots for a few hundred dollars. {SRC['wos']} shows what the broadcast side looks like. Sponsor the team your customers’ kids play on, and ask for something trackable: a code, a QR on the banner, a mention in the league email. The {L('/blog/local-sponsorships-youth-sports-the-woodlands-houston/', 'sponsorship pricing guide')} lists more.</p>
<h3>12. Partner with a business that shares your customer</h3>
<p>A boutique and a med spa. A gym and a smoothie shop. A roofer and a realtor. Swap referral cards, co-host one event a quarter, and feature each other in your emails. Costs almost nothing and borrows trust you’d otherwise spend years earning.</p>
<h3>13. Show up where people already gather</h3>
<p>The Township’s 2026 Red, Hot &amp; Blue Festival ran across five sites, from Town Green Park to Hughes Landing, per {SRC['rhb']}. The Waterway Arts Festival draws about 200 artists to Town Green Park, according to {SRC['waaf']}. Headline sponsorships aren’t cheap, but site-level sponsorships and booths often are. Bring a sign-up offer, not just a tablecloth and candy.</p>
<h3>14. Use the Houston calendar</h3>
<p>Hurricane prep in June, back-to-school in late July, rodeo season in March, the first cold snap, the holidays. A message that matches what people are already thinking about is cheaper to get noticed. Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal calendar')} has dates.</p>
<h3>15. Film short videos on your phone</h3>
<p>A 20-second clip of you fixing, making or explaining something beats a polished brand video for most small businesses. Twice a week, same day, so it becomes habit. Which platform? Our {L('/blog/facebook-vs-instagram-vs-tiktok-local-business/', 'Facebook vs. Instagram vs. TikTok comparison')} helps.</p>
<h3>16. Send one email a month</h3>
<p>One tip, one offer, one bit of news. Plain text is fine. The list you build here is the only audience you own. Our {L('/blog/email-marketing-basics/', 'email basics guide')} covers the setup. If you add texts, only send to people who opted in; Texas brought marketing texts under its telephone solicitation law in 2025.</p>
<h3>17. Run a referral program</h3>
<p>Reward the customer who sends a friend, after the friend buys. Make the reward something you’d be glad to give: a service credit, a free add-on. Track it with a simple code.</p>"""),

            ("Small business marketing ideas for $500 to $2,500 a month", f"""<p>Only move into this tier once ideas 1 through 4 are done and you can track calls and forms. Otherwise you’re paying to send people to a profile with nine reviews.</p>
<h3>18. Geo-targeted Meta ads</h3>
<p>$10 to $30 a day around your location can reach a meaningful share of nearby adults. Use a radius that matches drive time, not a whole county. Our {L('/blog/geo-fencing-ads-target-customers-nearby/', 'geo-fencing guide')} explains what’s realistic.</p>
<h3>19. Google Search ads</h3>
<p>For anything people search for, this is where intent lives. Start narrow: your best two or three services, your area, a strict negative keyword list. Check our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} before you set a budget.</p>
<h3>20. Local Services Ads</h3>
<p>For home and professional services, you pay per lead instead of per click and get the badge at the top. Read {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs. Google Ads')} to see which fits.</p>
<h3>21. Pay local creators</h3>
<p>A creator with 8,000 followers who actually live in The Woodlands is worth more to a local café than one with 200,000 followers in Dallas. Ask for their audience location before you pay. Run the best post as an ad. See {L('/blog/ugc-vs-influencers-creator-content/', 'UGC vs. influencers')}.</p>
<h3>22. EDDM postcards to chosen routes</h3>
<p>Every Door Direct Mail lets you mail every address on a carrier route without a list, per {SRC['eddm']}. Pick routes that match your customer and include a code or URL so you can count responses. Our {L('/blog/eddm-direct-mail-cost-the-woodlands-houston/', 'EDDM cost guide')} has current postage.</p>
<h3>23. Retarget your site visitors</h3>
<p>Cheap, small, and it catches the people who almost booked. Cap frequency so you don’t follow anyone around for a month.</p>
<h3>24. Track every call and form</h3>
<p>Not glamorous, and it’s the idea that makes the other 24 measurable. A tracked number per channel and form conversions in GA4. See {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking')}.</p>
<h3>25. Sell a membership or maintenance plan</h3>
<p>HVAC tune-ups, monthly facials, lawn plans, car wash clubs. Recurring revenue lowers how much you need to spend chasing new customers every month.</p>"""),

            ("Which marketing ideas fit which kind of Woodlands business?", f"""<p>Different businesses get customers in different ways. A rough guide from what we’ve seen:</p>
<ul>
<li><b>Home services</b> (HVAC, plumbing, roofing, pest): 1, 3, 6, 19 or 20, 22, 24. People search when something breaks. Be on the map and in the ads.</li>
<li><b>Restaurants and cafés:</b> 1, 3, 13, 15, 18, 21. Visual, impulse, local. Our {L('/blog/restaurant-marketing-the-woodlands-houston/', 'restaurant marketing guide')} goes further.</li>
<li><b>Wellness and beauty</b> (med spa, salon, massage): 1, 3, 5, 12, 21, 25. Trust and rebooking matter most.</li>
<li><b>Professional services</b> (CPA, law, insurance, financial): 1, 5, 7, 10, 17, 19. Reputation and referrals, then search.</li>
<li><b>Retail and boutiques:</b> 1, 9, 12, 13, 15, 16. Foot traffic and repeat visits.</li>
</ul>
<!--fig:hours-->"""),

            ("How to pick three ideas and run them for 90 days", f"""<p>Pick three. One from the free tier that you haven’t finished, one that builds local trust, and one that you can measure. Then do them every week for 90 days before judging them. Most small business marketing fails because it gets abandoned in week five, not because the idea was bad.</p>
<!--fig:plan90-->
<p>Write down a baseline before you start: calls per week, form fills, Business Profile calls and direction requests (Google shows these in the profile’s performance view), review count and rating. At day 90 compare against it. Keep what moved, drop what didn’t, and pick the next one.</p>"""),

            ("Small business marketing mistakes we see in The Woodlands", f"""<p>A few patterns come up again and again.</p>
<!--fig:picks-->
<ul>
<li><b>Boosting posts as the ad strategy.</b> The Boost button optimizes for likes from anyone, often far from your location. Use Ads Manager with a radius and a real objective.</li>
<li><b>Listing the Township as one big market.</b> A business near Creekside Park and one near Panther Creek can have different customers. Village-level thinking helps.</li>
<li><b>Paying for a directory listing that promised “page one.”</b> If a caller says they’re “from Google,” they aren’t.</li>
<li><b>Ignoring the quiet months.</b> August heat and the week after a storm change who’s buying. Plan for it instead of pausing everything.</li>
<li><b>Doing everything at once.</b> Twenty-five half-done ideas lose to three done properly.</li>
</ul>
<p>Want help picking the three that fit your business, your budget and your part of town? A senior strategist will build a plan around your goals. <a href="/contact/">Get in touch</a>.</p>"""),
        ],
        "faq": [
            ("What is the cheapest way to market a small business in The Woodlands?",
             "Start with your Google Business Profile, reviews and your website, which cost time instead of money. Complete every field on the profile, post weekly, ask every happy customer for a review and reply to each one. Then add a page for each service and nearby town like Spring, Conroe and Magnolia. Those steps usually bring more calls than a small ad budget would."),
            ("Is joining The Woodlands Area Chamber of Commerce worth it for a small business?",
             "It depends on who your customers are and whether you’ll show up. The chamber’s Small Business tier is listed at $500 and includes a ribbon cutting and a networking breakfast credit. It tends to pay off for B2B and professional services whose clients are other local businesses. For consumer businesses like cafés, it’s more about local goodwill than direct sales."),
            ("How much should a small business in The Woodlands spend on marketing per month?",
             "Many small local businesses start somewhere between a few hundred and a couple of thousand dollars a month, plus the owner’s time. A better approach is to work backward from what a customer is worth and how many new ones you need. Don’t move into paid ads until your Google profile, reviews and call and form tracking are in place, or you can’t tell what’s working."),
            ("Do Nextdoor recommendations help a small business in The Woodlands?",
             "Yes, especially for home services, pet care and neighborhood retail. Woodlands residents ask for recommendations in their village groups all the time, and a few genuine recommendations from neighbors carry a lot of weight. Claim your free business page, encourage happy customers to recommend you, and answer questions helpfully. Paid Nextdoor ads are a separate decision worth testing on a small budget first."),
            ("What marketing works best for a new small business near Houston with no reviews yet?",
             "Focus on getting found and getting reviewed before spending much on ads. Verify your Google Business Profile, ask every early customer for a review, build service and location pages, and tell neighbors, nearby businesses and local groups you’re open. Once you have 20 or more recent reviews, small search or geo-targeted social campaigns tend to convert much better."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "The Woodlands in three numbers",
                "stats": [["114,436", "Residents at the 2020 census"], ["$140,701", "Median household income"], ["2.73", "People per household"]],
                "note": "Source: U.S. Census Bureau QuickFacts, The Woodlands CDP",
                "alt": "Stat tiles with The Woodlands population, income and household size for small business marketing",
                "caption": "Busy, two-income households with kids. They read reviews and they ask neighbors.",
            },
            "tradearea": {
                "type": "map",
                "title": "A Woodlands trade area is bigger than the Township",
                "sub": "Where customers of a Woodlands small business usually come from",
                "highlight": ["The Woodlands", "Shenandoah", "Spring", "Conroe", "Magnolia", "Tomball"],
                "note": "Rings are 10, 20 and 30 miles. Most local customers come from inside the first ring.",
                "alt": "Map of The Woodlands small business trade area including Spring, Conroe, Magnolia, Tomball and Shenandoah near Houston",
                "caption": "Build town pages and ad radiuses around this map, not around all of Houston.",
            },
            "tiers": {
                "type": "bars",
                "title": "How the 25 ideas split by cost",
                "sub": "Number of ideas in each tier",
                "items": [["Free (your time)", 9, "9 ideas"], ["Under $500 a month", 8, "8 ideas"], ["$500 to $2,500 a month", 8, "8 ideas"]],
                "highlight": [0],
                "alt": "Bar chart of 25 small business marketing ideas for The Woodlands grouped by monthly cost tier",
                "caption": "More than a third of the list costs nothing but time. Start there.",
            },
            "gbpcheck": {
                "type": "checklist",
                "title": "Google Business Profile: is yours done?",
                "items": ["Primary category is the thing you most want to be found for", "Every true secondary category added", "Every service listed with a description", "Hours, holiday hours and attributes current", "20+ real photos, refreshed monthly", "Description says what you do and where", "A post in the last seven days", "Every review answered"],
                "alt": "Checklist for a complete Google Business Profile for small businesses in The Woodlands and Houston",
                "caption": "Idea No. 1, broken into the parts most owners skip.",
            },
            "hours": {
                "type": "columns",
                "title": "Weekly owner hours by tier",
                "sub": "Typical time once each idea is set up",
                "labels": ["Free ideas", "Under $500", "$500-$2,500"],
                "values": [80, 55, 35],
                "highlight": [0],
                "y_label": "Hours",
                "note": "Illustrative example. Paid tiers trade money for time; free tiers trade time for money.",
                "alt": "Column chart of weekly hours needed for small business marketing ideas in The Woodlands by cost tier",
                "caption": "If you have time and no budget, the free tier is plenty. If you have neither, pick one idea.",
            },
            "plan90": {
                "type": "steps",
                "title": "A 90-day plan for three ideas",
                "steps": [["Week 1: Baseline", "Write down calls, forms, profile actions, reviews and rating."], ["Weeks 1-2: Set up", "Finish the free idea you skipped. Get tracking working."], ["Weeks 3-12: Repeat", "Same tasks, same day, every week. No switching."], ["Day 90: Compare", "Keep what moved the baseline. Drop what didn’t."], ["Next quarter: Add one", "Pick the next idea from the table."]],
                "alt": "Five-step 90-day small business marketing plan for businesses in The Woodlands and Houston",
                "caption": "Consistency beats variety. Ninety days is about the shortest fair test.",
            },
            "picks": {
                "type": "compare",
                "title": "Random acts of marketing vs. three ideas done well",
                "left": {"title": "Trying everything", "items": ["New platform every month", "Boosted posts to anyone", "No baseline numbers", "Reviews when someone remembers", "Quits in week five"]},
                "right": {"title": "Three ideas, 90 days", "items": ["One free, one local, one measurable", "Radius ads tied to drive time", "Baseline written on day one", "Review ask built into checkout", "Judged at day 90"]},
                "alt": "Comparison of scattered marketing and a focused three-idea plan for small businesses in The Woodlands",
                "caption": "The right column is less exciting. It also works.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: med spa marketing
    {
        "slug": "med-spa-marketing-the-woodlands-houston",
        "date": "2026-09-05",
        "modified": "2026-11-27",
        "title": "Med Spa Marketing in The Woodlands and Houston: The Texas Rules and the Channels That Book Consults",
        "seo_title": "Med Spa Marketing in The Woodlands & Houston",
        "desc": "Med spa marketing for The Woodlands and Houston: Texas rules for injectables, lasers and IV, Google and Meta ad policies, treatment pages and a 90-day plan.",
        "category": "Strategy",
        "icons": ["Google Business Profile", "Instagram", "Google Ads"],
        "art": "b6",
        "hero": "spa",
        "hero_alt": "Illustration of a med spa treatment room for med spa marketing in The Woodlands and Houston",
        "related": ["iv-therapy-marketing-the-woodlands-houston", "esthetician-marketing-ideas-houston-the-woodlands", "dermatology-practice-marketing-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Most med spa ad problems in Texas start with one word: Botox.</p>
<p>It’s the treatment patients search for, the word owners want on every ad, and a prescription drug brand that Google won’t let most advertisers bid on. Get that wrong and half your search campaign sits in “limited” while a competitor down Woodlands Parkway books the consults.</p>
<p><b>The short answer:</b> med spa marketing in The Woodlands and Houston works when it’s built on the treatment, not the spa. One page per treatment with provider credentials and price ranges, a Business Profile full of treatment-specific reviews, search ads that respect Google’s drug-term rules, Meta ads aimed at adults 18 and up, local creators, and memberships that bring patients back.</p>
<p>This guide puts the Texas rules next to each channel, because in this category the two can’t be separated.</p>
<!--fig:industry-->"""),

            ("Who regulates a med spa in Texas, and why your marketing should care", f"""<p>Texas has no single “med spa license.” Different services fall under different agencies, and your marketing has to match what each person on staff is allowed to do.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Service</th><th>Who regulates it</th><th>What it means for marketing</th></tr></thead>
<tbody>
<tr><td>Facials, waxing, lash extensions, light peels</td><td>TDLR (esthetician license and establishment license)</td><td>Fine to market by esthetician name. Estheticians can’t inject, use needles for fillers, or use lasers for hair removal or resurfacing</td></tr>
<tr><td>Neuromodulators, fillers, medium and deep peels</td><td>Texas Medical Board (medical acts, physician order and delegation)</td><td>Name the supervising physician and the injector’s credentials on the treatment page</td></tr>
<tr><td>Laser hair removal</td><td>TDLR certificate program; DSHS for device radiation safety</td><td>No claims that it’s free from risk or has a medical benefit</td></tr>
<tr><td>Elective IV therapy</td><td>HB 3749 (Jenifer’s Law), since Sept. 1, 2025</td><td>Administered only by a physician, PA, APRN or RN under physician supervision. Say who places the IV</td></tr>
<tr><td>Tanning, permanent makeup</td><td>DSHS</td><td>Separate rules; check before advertising</td></tr>
</tbody></table></div>
<p>The first two rows come from {SRC['tdlr_ms']}, which says plainly that TDLR “does not have jurisdiction over all the services provided at a medspa,” and that Botox and fillers must be provided under the order and delegation of a licensed physician. For laser hair removal, {SRC['tdlr_lhr']} requires a separate facility application for each location, a consulting physician contract and an individual certificate for anyone performing the procedure. {SRC['hsc518']} bars a facility from advertising that laser hair removal is free from risk or provides any medical benefit, and from false or misleading advertising generally. For IV therapy, see {SRC['hb3749']}.</p>
<p>Why care, beyond staying out of trouble? Patients are checking. In September 2025, {SRC['abc13']} that a Montgomery County woman who ran a med spa in Magnolia was arrested on felony charges of practicing medicine without a license after giving Botox and filler at in-home parties. Stories like that make credentials a selling point. A treatment page that names the medical director, the injector and their license type converts better than one with a stock photo and the word “experts.”</p>"""),

            ("What can a med spa say in Google and Meta ads?", f"""<p><b>Google.</b> In the U.S., {SRC['g_drug']} lets advertisers use prescription drug terms in ad text and on landing pages without certification, but keyword-targeting those terms requires certification. Google’s {SRC['g_rxsvc']} is aimed at online prescribing, dispensing and pharmacies, which most med spas aren’t. In practice, that means you can mention a brand name in copy and on the page, while keywords built on the brand name tend to get limited or disapproved.</p>
<p>So we build search campaigns around the treatment and the outcome instead:</p>
<ul>
<li>“wrinkle relaxer The Woodlands,” “forehead lines treatment Spring TX,” “lip filler near me,” “laser hair removal The Woodlands,” “microneedling Conroe,” “med spa near Market Street”</li>
<li>Negatives from day one: training, course, certification, jobs, salary, school, DIY, at home, kit, wholesale, “how to become,” free</li>
</ul>
<p><b>Meta.</b> {SRC['meta_cos']} requires ads for cosmetic procedures to target people 18 and older. Meta’s {SRC['meta_pha']} also bars ad content that implies or tries to generate negative self-perception, and its examples flag before-and-after images in weight-loss ads. In aesthetics accounts, we treat before-and-afters as something to test carefully rather than lead with, and keep copy away from “fix your…” framing.</p>
<!--fig:copy-->
<p>If you offer GLP-1 weight loss, the rules tighten further on both platforms; our {L('/blog/weight-loss-clinic-marketing-houston-the-woodlands/', 'weight loss clinic guide')} covers that separately. Same for IV drips in our {L('/blog/iv-therapy-marketing-the-woodlands-houston/', 'IV therapy marketing post')}.</p>"""),

            ("What treatments drive med spa revenue?", f"""<p>Injectables. Neuromodulators made up 50% of minimally invasive cosmetic procedures in the American Society of Plastic Surgeons’ 2025 data, and hyaluronic acid fillers another 30%, per {SRC['asps']}. Laser skin treatments, IPL and laser hair removal were among the other most-performed procedures.</p>
<!--fig:mix-->
<p>That shapes where marketing money goes. Neuromodulator patients come back every few months. A first injectables visit is the start of a relationship, so the real cost per patient you can afford is much higher than the price of one appointment. Laser hair removal and facial packages are good entry points for people nervous about needles, and a natural path to injectables later.</p>"""),

            ("Treatment pages that book consultations", f"""<p>Patients rarely search for “med spa” alone. They search for the treatment, the problem, or the treatment plus a place. Each core treatment needs its own page, and each page should answer what a nervous first-timer actually wants to know.</p>
<!--fig:pagecheck-->
<p>Price is the one owners resist. Patients compare. A “from” price or a per-unit range on the page filters out people who’d never book and builds trust with the ones who will. If you won’t publish a price, at least publish what the consultation costs and if it’s credited toward treatment.</p>
<p>Connect each page to the matching service on your Google Business Profile and link the booking button straight into your scheduler, preferably without a phone call. Our {L('/blog/power-of-local-landing-pages/', 'landing pages guide')} and {L('/services/web-design-seo-pr/', 'web and SEO service')} cover the build.</p>"""),

            ("How do med spas get more clients in The Woodlands and Houston?", f"""<p>Four channels do most of the work. In rough order of what we’d build first:</p>
<p><b>1. The Business Profile and reviews.</b> “Med spa near me” and “Botox near me” searches pull from the map. Add every service with a description, upload real photos of the rooms and providers monthly, and keep the booking link current. Ask every patient for a review and nudge them to mention the treatment and provider; reviews that say “lip filler with Sarah” help the profile show for “lip filler.” Never trade discounts for reviews. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} and {L('/blog/fake-reviews-rule-local-businesses/', 'FTC fake reviews rule post')} cover the lines.</p>
<p><b>2. Search ads for treatment terms.</b> As above, built around treatments and outcomes, with tight location targeting.</p>
<p><b>3. Local creators.</b> Aesthetics is a trust purchase, and a creator who lives in The Woodlands showing her own appointment does more than any brand ad. Disclose every gifted treatment, get permission to run the content as ads, and send creator traffic to a page with a code so you can count it.</p>
<p><b>4. Memberships and rebooking.</b> {SRC['amspa']} put the average spend per visit at $527 and the average share of repeat patients at 73%. The money is in the second through tenth visit. A membership, a rebook prompt at checkout, and a text when they’re due do more for revenue than another ad campaign.</p>
<p>Geography matters more than owners expect. Patients will drive a bit farther for a provider they trust, but a Market Street patient isn’t driving to the Galleria for a touch-up.</p>
<!--fig:map-->"""),

            ("How much should a med spa spend on marketing in Houston?", f"""<p>Work it backward from what a patient is worth rather than from a percentage someone quoted at a conference. AmSpa’s average of $527 per visit and 73% repeat patients means a new injectables patient who rebooks a few times a year is worth well over $1,000 in year one. Your own numbers will differ, so pull them from your booking system.</p>
<p>Then ask what you can afford to pay for a booked, shown consultation. A simple illustrative funnel:</p>
<!--fig:funnel-->
<p>If you know your show rate and your consult-to-treatment rate, you know your ceiling. For many single-location med spas that leads to an ad budget somewhere in the low thousands a month, plus creator and content costs. Start smaller in one area and scale what you can measure. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} help with the search side, and {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking')} with the measurement.</p>"""),

            ("Why med spa leads go cold, and the reply that saves them", f"""<p>Here’s a scene we’d bet happens at most med spas around Houston every week. A woman in Spring fills out a lip filler form at 9:40 p.m. on a Tuesday, after the kids are in bed. The front desk sees it at 10 the next morning, calls, gets voicemail, and leaves a message. She already booked with the place that texted her back at 9:43.</p>
<p>Aesthetics leads are impulse-adjacent. The interest is real, but it cools fast, and the person is usually comparing two or three spas at once. Speed matters more than the perfect script. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} has the broader research; for med spas, we’d set it up like this:</p>
<ul>
<li>An automatic text within a minute of any form, from a real local number, with the booking link and a question that invites a reply.</li>
<li>A human follow-up during business hours the same day, by text first. Many patients would rather not take a call at work.</li>
<li>Online booking with a deposit for first visits, credited toward treatment. Deposits cut no-shows without scaring off serious patients.</li>
<li>A reminder the day before, with parking directions and what to expect.</li>
</ul>
<p>A first reply that works:</p>
<p><i>“Hi Jess, this is Maria at [your spa] on Market Street. Thanks for asking about lip filler! First visits start with a quick consult with our nurse injector. Want to grab a time this week? Here’s the link, or just text back a day that works.”</i></p>
<p>Only text people who gave you their number for that purpose, and keep marketing texts to people who opted in. Texas updated its telephone solicitation law in 2025, and our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} explains what changed.</p>
<p>One more Houston-specific note on timing. Laser hair removal and resurfacing patients are usually told to stay out of the sun around treatment, which is a tough ask in a Texas summer. Many spas push laser packages in the fall and winter and lean on injectables, facials and memberships in the hottest months. Plan your ad calendar around that instead of running the same offer all year.</p>"""),

            ("What results look like for a Woodlands med spa", f"""<p>When {L('/case-studies/skinlab-by-dr-roth/', 'SkinCeuticals SkinLab by Dr. Roth')} opened on Market Street next to established med spas, we combined a local creator program, Business Profiles and treatment pages, and creator videos run as Reels and TikTok ads geo-fenced within 10 miles, with promo codes and store-visit tracking tying posts to visits. The published case study reports in-store visits from Google and social up 186%, No. 1 in the map pack for “med spa The Woodlands,” and cost per booked consultation down 41%.</p>
<p>None of the pieces were unusual. What made it work was that each one pointed at the same booking page, and every channel was measured on consultations, not likes.</p>"""),

            ("A 90-day med spa marketing plan", f"""<p>If we were starting from scratch with a single-location med spa in The Woodlands, Spring or Conroe, the order would look like this:</p>
<!--fig:plan-->
<p>The mistakes we see most often, so you can skip them:</p>
<ul>
<li><b>One “Services” page listing 20 treatments.</b> It ranks for nothing.</li>
<li><b>Brand-name keywords that never serve.</b> Check the policy status column weekly.</li>
<li><b>Ads that call out flaws.</b> “Tired of your wrinkles?” is the kind of copy Meta’s self-perception rule is aimed at, and patients don’t love it either.</li>
<li><b>No provider names anywhere.</b> In a category with Houston headlines about unlicensed injectors, anonymity reads as a red flag.</li>
<li><b>Discount-only promotions.</b> They fill the calendar with one-time bargain hunters. Membership offers and first-visit packages bring back patients instead.</li>
</ul>
<p>If you run an aesthetics practice in The Woodlands or Houston and want a senior strategist to build a plan around your treatments, providers and goals, <a href="/contact/">get in touch</a>. Our {L('/services/paid-social-advertising/', 'paid social')} and {L('/services/search-marketing/', 'search')} teams work together on it.</p>"""),
        ],
        "faq": [
            ("Can a med spa advertise Botox on Google Ads in Texas?",
             "You can mention prescription drug brand names in ad text and on landing pages in the U.S., but Google requires certification to keyword-target prescription drug terms, and most med spas don’t fit its certification categories. That’s why brand-name keywords often get limited. Build campaigns around treatment and outcome terms like wrinkle relaxer, forehead lines or lip filler plus your city, and name the brand on the page."),
            ("Do med spas need a license in Texas?",
             "Texas doesn’t issue a single med spa license. TDLR licenses estheticians and the establishment for cosmetology services, and runs the laser hair removal certificate program with a separate application for each facility. Injectables and medium or deep peels are medical acts under the Texas Medical Board, done under a physician’s order and delegation. Elective IV therapy has had its own rules since September 1, 2025."),
            ("Can med spas post before and after photos on Instagram ads?",
             "It’s risky. Meta requires cosmetic procedure ads to target people 18 and older and bars ad content that implies or generates negative self-perception, with before-and-after images flagged as non-compliant in its weight-loss examples. Organic posts with patient consent are a different matter. For ads, lead with the provider, the experience and the treatment process, and test before-and-afters carefully if you use them at all."),
            ("How do I get more med spa clients in The Woodlands?",
             "Build one page per treatment with provider credentials and price ranges, fill your Google Business Profile with every service and treatment-specific reviews, run search ads on treatment terms around your location, and use local creators who live in The Woodlands. Then push rebooking and memberships, since AmSpa reports most med spa patients are repeat patients and the revenue is in return visits."),
            ("How much do med spas spend on marketing per month in Houston?",
             "There’s no reliable Houston benchmark, so work backward from patient value. AmSpa reports an average of $527 per visit and 73% repeat patients, which makes a retained injectables patient worth well over $1,000 a year. Use your show rate and consult-to-treatment rate to find what you can pay per booked consult. Many single-location med spas end up spending in the low thousands a month on ads."),
        ],
        "figures": {
            "industry": {
                "type": "stats",
                "title": "The med spa business in three numbers",
                "stats": [["10,488", "U.S. med spas in 2023"], ["$527", "Average spend per patient visit"], ["73%", "Average share of repeat patients"]],
                "note": "Source: AmSpa 2024 Medical Spa State of the Industry recap",
                "alt": "Stat tiles on med spa industry size, spend per visit and repeat patients for med spa marketing in The Woodlands and Houston",
                "caption": "Repeat patients are the business. Marketing should be judged on who comes back.",
            },
            "copy": {
                "type": "compare",
                "title": "Med spa ad copy: risky vs. safer",
                "left": {"title": "Likely to get flagged", "items": ["“Tired of your wrinkles?”", "Brand-name keywords without certification", "Before-and-after as the main image", "“Painless, zero risk” laser claims", "Targeting under 18 or no age set"]},
                "right": {"title": "Safer and still persuasive", "items": ["“Smooth forehead lines, 15-minute visit”", "Treatment and outcome keywords", "Provider on camera explaining the visit", "Real downtime and what to expect", "Adults 18+, radius around the spa"]},
                "alt": "Comparison of risky and compliant med spa ad copy for Google and Meta in Houston and The Woodlands",
                "caption": "Describe the treatment and the experience. Let the patient decide what they want fixed.",
            },
            "mix": {
                "type": "bars",
                "title": "Where minimally invasive procedures come from",
                "sub": "Share of U.S. minimally invasive cosmetic procedures, 2025",
                "items": [["Neuromodulators", 50, "50%"], ["Hyaluronic acid fillers", 30, "30%"], ["Everything else (lasers, IPL, peels, more)", 20, "20%"]],
                "highlight": [0],
                "note": "Source: AmSpa summary of ASPS 2025 statistics",
                "alt": "Bar chart of minimally invasive cosmetic procedure share for med spa marketing in The Woodlands and Houston",
                "caption": "Injectables are eight in ten procedures. Build the funnel around them, with lasers and facials as entry points.",
            },
            "pagecheck": {
                "type": "checklist",
                "title": "What every med spa treatment page needs",
                "items": ["What it treats, in plain words", "Who performs it, with license type", "Supervising physician named", "Price range or consult fee", "How long it takes and downtime", "What to expect before and after", "Real FAQs (pain, results timing, who it’s not for)", "Book button straight into the scheduler"],
                "alt": "Checklist for med spa treatment pages that book consultations in The Woodlands and Houston",
                "caption": "One of these per core treatment. The credentials line matters more in Texas than most owners think.",
            },
            "map": {
                "type": "map",
                "title": "How far patients drive for aesthetics",
                "sub": "Rings are 10, 20 and 30 miles from The Woodlands",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Magnolia", "Tomball", "Kingwood"],
                "note": "Plan new-patient ads within about 10-15 miles. Loyal patients travel farther for a trusted injector.",
                "alt": "Map of med spa patient drive areas around The Woodlands, Spring, Conroe, Magnolia, Tomball and Kingwood near Houston",
                "caption": "A Market Street med spa competes with Spring and Conroe, not with the Galleria.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From ad click to returning patient",
                "stages": [["Ad clicks", "1,000"], ["Consult requests", "60"], ["Consults that show", "42"], ["First treatments", "30"], ["Rebook within 4 months", "20"]],
                "note": "Illustrative example. Use your own show and conversion rates.",
                "alt": "Funnel from ad clicks to returning med spa patients for practices in The Woodlands and Houston",
                "caption": "Count shows and rebooks, not leads. That’s where the cost per patient becomes real.",
            },
            "plan": {
                "type": "steps",
                "title": "A 90-day med spa marketing plan",
                "steps": [["Days 1-14: Foundation", "Treatment pages, provider credentials, Business Profile services and booking links."], ["Days 15-30: Reviews", "Review ask at checkout and by text. Reply to every one."], ["Days 31-60: Search", "Treatment-term campaigns with tight radius and negatives."], ["Days 45-75: Creators", "Three to five local creators, disclosed, content run as ads."], ["Days 60-90: Retention", "Membership offer, rebook reminders, monthly email."]],
                "alt": "Five-step 90-day med spa marketing plan for The Woodlands and Houston aesthetics practices",
                "caption": "Foundation first. Ads perform better once the pages and reviews can close the sale.",
            },
        },
    },
]
