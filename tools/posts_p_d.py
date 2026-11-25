"""Batch 16 (module d): yoga studio marketing in The Woodlands and Houston, dance studio marketing in The Woodlands and
Houston, and music lessons school marketing in The Woodlands and Houston.

Research (yoga): ClassPass partner FAQ (lower per-spot rate than direct, confidential floor as a percentage of direct
pricing, SmartRate, SmartSpot decides spot counts, paid on late cancels with a 12-hour window, one spot one payment);
ClassPass SmartRate explainer; Mindbody press release (ClassPass acquisition completed October 15, 2021); ClassPass
2025 Look Back release (11 a.m. to 1 p.m. bookings up 38% globally); Yoga Alliance RYT standards (200-hour training at
an RYS, trainings can't be combined) and RYS standards (150 of 200 hours by Lead Trainers holding E-RYT 500, 15%
synchronous for distance programs, $400 application, $240 a year); Houston Public Media via KEDT (145 days at or above
90 degrees in 2025, NWS Houston/Galveston); ACE-sponsored Bikram study (105 F, 40% humidity, seven of 20 above 103 F,
peak 104.1 F); Meta personal health and appearance ad standard; Google Business Profile booking links help; Google's
March 2017 fitness booking announcement (Mindbody among partners); Google Maps prohibited content policy (incentives,
selective solicitation, staff quotas and staff-name content); Google Ads advanced location options; Morgan Lewis on
Texas SB 140.
Dance: Conroe ISD 2026-27 calendar PDF (Aug 12 start, Oct 9-12, Nov 23-27, Dec 21-Jan 5, Mar 15-19, May 27 last day);
My Neighborhood News on Katy ISD 2026-27 (Aug 12 start, May 20 last day; Oct 9-13 fall break added Jan 2026); Dance
Teacher on recital fee structures ($120, $129, $12/month) and costume pricing ($70, $80-$90, $350 rental, disclose at
registration); Meta January 2023 teen ads post (age and location only from February 2023, gender removed); Linear
Design on detailed targeting exclusions removed in 2025; Meta July 2025 child safety post (adult-managed accounts that
primarily feature children); KPRC May 2026 (18 youth camps fully licensed); DSHS youth camp parent resource
(single-activity, no-outdoor and HHSC child care programs outside the law); Texas Human Resources Code 42.041(b)(18).
Music: TMEA Plan Your Visit (convention Feb 10-13, 2027, San Antonio); TMEA All-State student information (January
recorded seating auditions); Kingwood High School choir All-State audition page (Sept 12 district, Oct 19 region at
Atascocita HS, Dec 3 pre-area, Jan 9 area at The Woodlands HS); UIL TSSEC page (May 29 and 31, 2027, Austin area,
registration April 1-15).
Blocked or unverified and left out: ClassPass payout blog (permission timeout; used the FAQ and SmartRate pages
instead), ClassPass 2025 Look Back report page itself (fetch failed; used the release), yoga-specific booking
rankings, Texas licensing of yoga teachers, GBP instructor category names, search volumes for lesson keywords.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # yoga post
    "cpfaq": A("https://classpass.com/partners/faqs", "ClassPass’s partner FAQ"),
    "smartrate": A("https://classpass.com/partners/blog/what-is-smartrate", "ClassPass’s SmartRate explainer"),
    "mbcp": A("https://www.mindbodyonline.com/company/press/mindbody-completes-acquisition-of-classpass", "completed its acquisition of ClassPass"),
    "cprel": A("https://blog.classpass.com/classpass-releases-its-2025-look-back-report-revealing-the-global-fitness-and-wellness-trends-that-defined-the-year/", "ClassPass’s 2025 Look Back release"),
    "ryt": A("https://yogaalliance.org/Standards-for-RYT-Credentials", "Yoga Alliance’s RYT standards"),
    "rys": A("https://www.yogaalliance.org/Standards-for-RYS-Credentials", "Yoga Alliance’s school standards"),
    "hpm": A("https://www.kedt.org/texas-news/2026-01-05/houston-saw-more-90-plus-degree-days-in-2025-than-ever-before", "Houston Public Media"),
    "ace": A("https://www.acefitness.org/continuing-education/prosource/may-2015/5355/ace-study-examines-effects-of-bikram-yoga-on-core-body-temps/", "ACE-sponsored study"),
    "metahealth": A("https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-health-and-appearance", "Meta’s personal health and appearance ad standard"),
    "gbpbook": A("https://support.google.com/business/answer/6218037", "Google’s help page on booking links"),
    "rwg": A("https://blog.google/products-and-platforms/products/maps/book-fitness-classes-anywhere-us-google/", "March 2017"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited and restricted content policy"),
    "loc": A("https://support.google.com/google-ads/answer/1722038?hl=en", "Google’s advanced location options"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    # dance post
    "cisd": A("https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5052/Cisd/e83881e1-1d85-43d1-b350-7fb41cffd1c1/26-27-CISD-Calendar.pdf", "Conroe ISD’s 2026-27 calendar"),
    "katy": A("https://myneighborhoodnews.com/katy-isd-approves-2026-2027-instructional-calendar-key-dates-and-comparisons-to-2025-2026", "My Neighborhood News on Katy ISD’s calendar"),
    "katyfall": A("https://myneighborhoodnews.com/katy-isd-approves-october-fall-breaks-for-202627-and-202728-school-years-following-community-feedback", "its January 2026 fall break vote"),
    "dt_fee": A("https://dance-teacher.com/ask-the-experts-how-much-is-your-recital-fee/", "Dance Teacher"),
    "dt_cost": A("https://dance-teacher.com/dance-costume-pricing/", "another Dance Teacher piece"),
    "metateen": A("https://about.fb.com/news/2023/01/age-appropriate-ads-for-teens/", "Meta’s announcement"),
    "linear": A("https://lineardesign.com/blog/facebook-detailed-targeting-list-2024/", "Linear Design’s running list of Meta targeting changes"),
    "metakids": A("https://about.fb.com/news/2025/07/expanding-teen-account-protections-child-safety-features/", "Meta’s July 2025 safety update"),
    "kprc": A("https://www.click2houston.com/news/local/2026/05/12/only-18-texas-youth-camps-fully-licensed-weeks-before-summer-but-many-can-still-legally-operate/", "KPRC"),
    "dshs": A("https://www.dshs.texas.gov/sites/default/files/youthcamp/pdf/youth-camp-parent-resource-2-12.pdf", "the DSHS parent resource on youth camps"),
    "hrc": A("https://texas.public.law/statutes/tex._human_resources_code_section_42.041", "Texas Human Resources Code § 42.041(b)(18)"),
    # music post
    "tmea": A("https://www.tmea.org/convention/plan-your-visit/", "TMEA"),
    "tmeaas": A("https://www.tmea.org/?p=17096", "TMEA’s All-State student page"),
    "khs": A("https://sites.google.com/humbleisd.net/khschoir/all-state-auditions/all-state-audition-information", "the Kingwood High School choir site"),
    "tssec": A("https://www.uiltexas.org/music/tssec", "UIL"),
}

YOGA = "/blog/yoga-studio-marketing-the-woodlands-houston/"
DANCE = "/blog/dance-studio-marketing-the-woodlands-houston/"
MUSIC = "/blog/music-lessons-school-marketing-the-woodlands-houston/"
PIL = "/blog/pilates-studio-marketing-the-woodlands-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: yoga
    {
        "slug": "yoga-studio-marketing-the-woodlands-houston",
        "title": "Yoga Studio Marketing in The Woodlands and Houston: Intro Offers, ClassPass and Members Who Stay",
        "seo_title": "Yoga Studio Marketing in The Woodlands & Houston",
        "desc": "Yoga studio marketing for The Woodlands and Houston: intro offers that convert, ClassPass tradeoffs, teacher training, hot yoga, Google profile and churn.",
        "category": "Strategy",
        "icons": ["Instagram", "Google Business Profile", "Google Ads"],
        "art": "b2",
        "hero": "spa",
        "hero_alt": "Illustration for yoga studio marketing in The Woodlands, Spring and Houston",
        "related": ["pilates-studio-marketing-the-woodlands-houston", "gym-fitness-studio-marketing-the-woodlands-houston", "cryotherapy-recovery-studio-marketing-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Sunday, 9 a.m. heated flow. Thirty-one mats down, six people on the waitlist, and the room is already at temperature when the first car pulls in from Creekside Park. Wednesday at 1 p.m., your yin class has three people in it, and one of them is the teacher’s neighbor.</p>
<p>In January you sold 44 intro months. It’s March, and your booking software says 11 of those people bought a membership.</p>
<p>That second number is the one we’d want to talk about first.</p>
<p>Yoga studio marketing in The Woodlands and Houston has two jobs. Get people who live or work a short drive away to buy an intro offer, then turn a good share of them into members who are still around next year. Instagram, Google, ClassPass, teacher training and community events all feed those two jobs, and each of them should be able to tell you roughly what it costs you per member.</p>
<p>This guide is for independent yoga studios, heated and not, from Spring and The Woodlands down through the Heights and out to Katy and Sugar Land. If you run a reformer studio, our {L(PIL, 'Pilates studio guide')} covers bed-capacity math and reformer-specific ads, so we won’t repeat that here.</p>"""),

            ("What a yoga studio in The Woodlands actually sells", f"""<p>A yoga room is more forgiving than a reformer room. You can always squeeze four more mats into a busy Sunday. That flexibility hides a problem: a room that can always take a few more people never forces you to look at which classes pay the rent.</p>
<p>Most studios have more revenue lines than they market. This is how we’d think about each one.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Revenue line</th><th>Who buys it</th><th>Its marketing job</th></tr></thead>
<tbody>
<tr><td>Unlimited or monthly membership</td><td>Locals who come twice a week or more</td><td>The goal of nearly every other line</td></tr>
<tr><td>Class packs and drop-ins</td><td>Travelers, shift workers, people still deciding</td><td>Upsell to membership once visits pass about six a month</td></tr>
<tr><td>Intro offer</td><td>People new to you</td><td>The front door, judged by conversion to members rather than sales</td></tr>
<tr><td>Teacher training</td><td>Committed members, plus a few from other studios</td><td>Big tuition, few buyers, months of lead time</td></tr>
<tr><td>Workshops and series</td><td>Members and lapsed members</td><td>Re-engagement and content</td></tr>
<tr><td>Privates and corporate classes</td><td>Nervous beginners, athletes, office teams</td><td>Higher revenue per teacher hour</td></tr>
<tr><td>Retail</td><td>Members already in the lobby</td><td>Not worth ad money; sell it at the desk</td></tr>
</tbody></table></div>
<p>Build the marketing calendar around the first three rows. Training and workshops get their own launches, because they’re bought on a different timeline.</p>"""),

            ("Intro offers that turn into memberships", f"""<p>Most yoga studios sell either an intro month (unlimited for 30 days at a discount) or a short pack, like three classes in two weeks. The month fits heated studios selling a daily habit. The pack works better when you want every new person in a specific beginner class.</p>
<p>Whichever you pick, the drop that hurts is between class one and class two. Here’s an illustrative funnel for 100 intro buyers.</p>
<!--fig:intro-->
<p>What moves those numbers:</p>
<ul>
<li><b>Book class two before they leave.</b> At the desk, out loud. “Thursday’s 6:15 slow flow is a good next one. Want me to put you in?” An email the next morning is too late for a lot of people.</li>
<li><b>Teachers learn the new person’s name</b> and use it twice in class. It costs nothing and people remember it.</li>
<li><b>A text from a human after class one.</b> Two lines: how did it feel, and what to bring next time (a towel and more water, if it was heated).</li>
<li><b>A week-three check-in</b> for anyone with fewer than four visits. This is where intro months quietly die.</li>
<li><b>A conversion offer tied to the intro deadline.</b> “Join before your intro ends and we’ll waive the [your price] enrollment fee,” or a discounted first month. Have the teacher mention it at the end of class, because a sign on the desk does nothing.</li>
</ul>
<p>Judge the intro on intro-to-member rate, measured about 45 days after purchase and tracked by month and by source. Our rule of thumb (not an industry benchmark) is that under 20% means the in-studio experience needs work before the ad budget goes up. Ads only send more people through the same leak.</p>
<p>We’d skip a free first class as the main offer. Charging something filters for intent, and the payment gives your ads a purchase event to optimize for.</p>"""),

            ("ClassPass and the aggregators: what you’re really trading", f"""<p>ClassPass fills empty mats. It can also teach your neighbors that they never need to buy a membership. Both happen, and which one wins at your studio depends on how you set it up.</p>
<p>The payment model, as {SRC['cpfaq']} describes it: ClassPass “often pays a lower per-spot rate than a direct booking,” and each partner agrees to a confidential floor rate calculated as a percentage of its direct pricing. SmartRate moves the credit price of each spot up or down with demand in real time but can’t go below that floor, per {SRC['smartrate']}. Partners usually get paid when a ClassPass user cancels late or doesn’t show, using a standard 12-hour window, and a spot is only paid once if another ClassPass user rebooks it.</p>
<p>Two details owners tend to miss. The FAQ says partners don’t directly choose how many spots go to ClassPass; a tool called SmartSpot decides that from attendance history and availability. So before you sign, ask your rep exactly which classes and times you can keep off the platform and how. And ClassPass and Mindbody are one company now, since Mindbody {SRC['mbcp']} on October 15, 2021. That doesn’t make either product bad. It does mean the company that may run your booking software also sells your open spots on an aggregator, so read the settings with that in mind.</p>
<!--fig:classpass-->
<p>Our rules for a yoga studio:</p>
<ul>
<li>Open ClassPass in the classes that usually run under half full: weekday middays, Friday evenings, some weekend afternoons. Keep the Sunday morning and weeknight 6 p.m. classes for members.</li>
<li>Work out your real per-visit payout from your own statements, since ClassPass doesn’t publish rates. Compare it with what a member visit is worth to you (monthly price divided by average monthly visits).</li>
<li>Treat every ClassPass visitor as an intro lead. Get their name at check-in and mention your intro offer once. Once.</li>
<li>Check the share of visits coming from ClassPass every quarter. If it climbs while memberships stay flat, the platform is replacing your direct funnel.</li>
</ul>
<p>The {L(PIL, 'Pilates guide')} has more on ClassPass caps and late-cancel settings; the logic carries over to mats.</p>"""),

            ("Teacher training as a revenue line", f"""<p>A 200-hour teacher training can be the biggest revenue event of a studio’s year. It’s also easy to market badly, because owners promote it like a workshop, three weeks out.</p>
<p>Start with the standards, because trainees will ask. To earn Yoga Alliance’s RYT 200 credential, a teacher completes a 200-hour training registered with Yoga Alliance at a Registered Yoga School, and separate trainings can’t be combined to reach the 200, per {SRC['ryt']}. On the school side, {SRC['rys']} require 150 of the 200 hours to be taught by Lead Trainers who hold the E-RYT 500 credential, and distance or hybrid programs must deliver at least 15% of hours live, which is 30 hours for a 200-hour program. Fees listed there are a $400 one-time application and $240 a year in dues. Registration is voluntary, but plenty of prospective trainees look for it, so say plainly whether your program is registered.</p>
<p>Who buys training: mostly your own members, a year or more in. That changes the marketing. Your best audience is a report from your booking software of everyone with 100 or more classes, and the best ad you’ll ever run is a personal note from the lead trainer.</p>
<!--fig:ytt-->
<p>The page should answer what trainees would otherwise email about: every weekend date and the hours, how makeups work, full tuition at [your price] with any payment plan, the refund policy, and who teaches each module. Put the recorded info session on it for people who can’t make a Tuesday night.</p>
<p>Search ads on “yoga teacher training Houston” or “200 hour yoga teacher training The Woodlands” are worth a small separate budget. Expect competition from online programs and destination retreats, and add negatives like online (if you’re in person only), free, retreat, Bali, India and Costa Rica.</p>"""),

            ("Hot yoga in Houston heat", f"""<p>Selling a 105-degree room in a city that already feels like one is a real marketing problem, and a seasonal one.</p>
<p>Houston logged 145 days at or above 90 degrees in 2025, beating the 2011 record, according to the National Weather Service figures reported by {SRC['hpm']}. Expect a split: some regulars love the hot room more in August, and a lot of first-timers decide it sounds like punishment.</p>
<!--fig:heat-->
<p>The traditional Bikram-style room runs at 105°F with 40% humidity. An {SRC['ace']} of 20 regular practitioners found core temperatures climbing through a 90-minute class, with seven people passing 103°F and one reaching 104.1°F. The researchers suggested shorter classes, lower room temperatures and letting students drink whenever they want. You don’t have to run a Bikram room to take the hint.</p>
<p>What that means for your marketing:</p>
<ul>
<li>Build a “your first heated class” page: the temperature your rooms actually run, what to bring, how to hydrate, when to eat, and that lying down is allowed. Link it from every intro ad. Nervous beginners buy when they know what they’re walking into.</li>
<li>Offer a warm or unheated beginner option and say so in ads from June through September.</li>
<li>Sell the heat honestly: flexibility, focus, a hard workout, an hour off your phone. Skip detox and calorie claims. Meta’s rules say health ads “must not imply or attempt to generate negative self-perception,” per {SRC['metahealth']}, and burn-the-fat creative invites rejections.</li>
<li>Talk about the A/C. In July, a cold lobby, cold showers and chilled towels are a selling point. Put them in the ad.</li>
</ul>
<p>Outdoor classes belong to fall and spring here. A donation class on a lawn in October brings in people who’d never walk into a heated room. The same class at noon in July is a liability.</p>"""),

            ("Google Business Profile: schedule, booking button and reviews", f"""<p>Most people searching “yoga near me” or “hot yoga The Woodlands” pick from the map, so your Business Profile does more selling than your homepage.</p>
<ul>
<li><b>Category.</b> Yoga studio as primary. Add secondary categories only for what you really offer.</li>
<li><b>Booking link.</b> In your profile, choose Booking, then Add link, paste your schedule or intro-offer URL and save. Then use Set preferred link so yours shows as “Business preferred.” Per {SRC['gbpbook']}, booking providers can attach links to your profile automatically, and you can’t delete those from your settings; you opt out with the provider.</li>
<li><b>The schedule.</b> There’s no timetable field, so the booking link has to land on a page where today’s classes and the intro offer are visible without scrolling. Google opened fitness class booking through partner scheduling software in {SRC['rwg']}, with Mindbody among the named partners, so check what your software supports today.</li>
<li><b>Photos.</b> The room with mats down, the lobby, parking, restrooms and showers. For a heated studio, the showers matter more than the sunset pose shot.</li>
<li><b>Posts.</b> Workshops, training info sessions, holiday schedules, and storm closures posted the same morning.</li>
</ul>
<p>Reviews win the map and the click. Send the same link to everyone after their third or fourth visit. Google’s rules ban incentives for reviews, discouraging negative ones, asking only happy customers, and telling staff to collect a set number of reviews or reviews that name a staff member, per {SRC['gpol']}. So no “mention your teacher” contests. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} and {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} cover the rest.</p>"""),

            ("Instagram and Meta ads that fill classes", f"""<p>Instagram is where people check whether your studio feels like them. They look at your grid before they buy the intro, so the grid should answer four things: who teaches, what the room looks like, what a class feels like, and who else goes.</p>
<ul>
<li>Teacher clips, 20 seconds each, talking to camera about their class. “My Thursday 6:15 is for people who sit at a desk all day.” That sells a slot; a handstand on a beach sells nothing.</li>
<li>Real members, with permission, of varied ages and bodies. If every photo is a 25-year-old in matching sets, the 50-year-old from Sterling Ridge assumes it isn’t for her.</li>
</ul>
<p>For ads, keep it simple. One Meta campaign selling the intro offer, aimed at a radius around the studio (we’d start at 5 to 8 miles in The Woodlands and tighter inside the Loop, where traffic decides everything), optimized for a purchase on your booking checkout rather than leads or clicks. Creative: a teacher talking, the room, the price. Our {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads guide')} walks through setup, and {L('/services/paid-social-advertising/', 'our paid social team')} runs campaigns like this.</p>
<p>Lunch is an opening. Per {SRC['cprel']}, bookings between 11 a.m. and 1 p.m. rose 38% globally in 2025. The offices around Research Forest and Hughes Landing, or the Energy Corridor in Houston, are full of people who’d take a 45-minute noon class. Run a small ad set for that class alone, with “back at your desk by 1” in the copy.</p>"""),

            ("Google Ads for yoga searches", f"""<p>Search ads catch people who already decided they want yoga this week. Keep the account small and tidy.</p>
<ul>
<li><b>Classes campaign.</b> Keywords like yoga studio near me, yoga classes The Woodlands, hot yoga Spring TX, beginner yoga Houston, yin yoga The Woodlands, and prenatal yoga only if you teach it. Send it to the intro offer page.</li>
<li><b>Teacher training campaign</b> with its own budget and page, switched on for the 12 weeks before each cohort.</li>
<li><b>Brand campaign</b> on your studio name. It’s cheap and keeps competitors off the top of your own search.</li>
</ul>
<p>Before launch, change the location setting to people in or regularly in your targeted locations, described in {SRC['loc']}. The default also counts people who merely show interest in your area, which is how a studio in Spring ends up paying for clicks from Dallas.</p>
<!--fig:negatives-->
<p>An illustrative first test for one studio is $15 to $35 a day. Judge it on intro purchases first and on members 45 days later. Our {L('/services/search-marketing/', 'search marketing team')} sets these up, and the {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} help you sanity-check what you’re paying.</p>"""),

            ("Community events that reach people who don’t follow you yet", f"""<p>Community counts as marketing when it puts you in front of people who aren’t already on your list.</p>
<ul>
<li><b>Co-hosted donation classes.</b> Partner with a local nonprofit, school PTO or running club so they promote it to their people. Your list already knows you.</li>
<li><b>Run club stretch sessions.</b> Twenty minutes after a Saturday group run in The Woodlands, with a QR code for your intro.</li>
<li><b>Workshops for lapsed members.</b> A fundamentals series or an arm balance workshop, emailed to everyone who cancelled in the last year.</li>
</ul>
<p>Make every free event require a $0 registration in your booking software so you get names and emails, then count how many attendees bought an intro within 30 days. Zero after three events means it was a nice morning and nothing more.</p>"""),

            ("Churn decides whether you need more marketing", f"""<p>This is the part most yoga marketing advice skips, and it decides whether you need much marketing at all.</p>
<p>Say you have 180 members. At 6% monthly churn you lose about 11 a month, so you need 11 new members just to stay where you are. At 3%, you need about 5. Same studio, same ad budget, half the pressure.</p>
<!--fig:churn-->
<p>What lowers it:</p>
<ul>
<li><b>Attendance alerts.</b> Pull a weekly report of members whose visits dropped sharply, say from eight a month to two. A personal text from their regular teacher beats an automated “we miss you.”</li>
<li><b>Freeze instead of cancel.</b> Houston families travel in July. A summer freeze keeps the billing relationship and the habit.</li>
<li><b>Teacher continuity.</b> Losing a favorite teacher’s slot loses members. Announce changes two weeks ahead and have the new teacher co-teach once.</li>
<li><b>One exit question.</b> Ask everyone who cancels why, in one tap. You’ll learn more than any survey.</li>
</ul>
<p>Be careful with promotional texts. Texas brought marketing texts under its telephone solicitation law through SB 140, effective September 1, 2025, with a registration requirement and a private right of action, though there are exemptions, including some for current or former customers and businesses that sell mostly from a physical location, per {SRC['sb140']}. Class reminders aren’t the same as promos, but ask your attorney before you start a promo text program. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} has more.</p>"""),

            ("What to track, and a first 90 days", f"""<p>Every Monday, look at five numbers: intro sales by source, intro-to-member rate (45-day lag), active members, members lost last month, and ClassPass share of visits. Monthly, check fill rate by class slot so marketing goes to the 12:15 and the Wednesday 1 p.m., and leaves the full classes alone.</p>
<p>A first 90 days for a studio starting from scratch:</p>
<ol>
<li><b>Days 1 to 30.</b> Fix the Business Profile and booking link, build the intro page and the first-heated-class page, set up purchase tracking in your booking software, and start the review ask.</li>
<li><b>Days 31 to 60.</b> Launch Google Search and one Meta intro campaign. Train the desk on booking class two. Start week-three check-ins.</li>
<li><b>Days 61 to 90.</b> Read the 45-day conversion numbers by source. Shift money toward whatever produced members. Set ClassPass limits, and plan the next teacher training launch 16 weeks out.</li>
</ol>
<p>If you’d like a senior strategist to build that plan around your actual schedule and numbers, <a href="/contact/">get in touch</a>. Running a dance or music program in the same building? Our {L(DANCE, 'dance studio guide')} and {L(MUSIC, 'music school guide')} cover those.</p>"""),
        ],
        "faq": [
            ("How do I get more members for my yoga studio in The Woodlands?",
             "Sell a paid intro offer, like an intro month or a three-class pack, through Google Search, Meta ads and your Google Business Profile booking link, aimed at people within a short drive. Then work on conversion: book the second class before people leave, text them after class one, and check in during week three. Measure intro-to-member rate 45 days after purchase and improve it before raising ad spend."),
            ("Is ClassPass worth it for a yoga studio in Houston?",
             "It can be, for classes that usually run under half full. ClassPass says it often pays less per spot than a direct booking, with a confidential floor based on your direct pricing and dynamic credit prices above it. Ask which classes you can keep off the platform, treat every ClassPass visitor as an intro lead, and watch whether its share of visits rises while memberships stay flat."),
            ("How much should a yoga studio spend on advertising?",
             "For one location, an illustrative first test is about $15 to $35 a day on Google Search plus a modest Meta campaign selling the intro offer. Judge both on intro purchases and, about 45 days later, on how many buyers became members. If conversion to membership is low, fix the first-class experience and follow-up before spending more, because more ads only push more people through the same leak."),
            ("How do I market a yoga teacher training?",
             "Start about 16 weeks before the first weekend. Build a page with every date, the full tuition, payment plans, refund policy and lead trainers, and say whether the program is registered with Yoga Alliance. Hold an info session and record it. Your best prospects are members with 100 or more classes, so send them personal invitations, then add small search and retargeting campaigns."),
            ("How can a yoga studio reduce membership churn?",
             "Watch for members whose attendance drops sharply and have their regular teacher reach out personally. Offer a freeze option for summer travel instead of only cancel, announce teacher and schedule changes two weeks ahead, and ask one quick question when people cancel. Even a couple of points lower monthly churn sharply cuts how many new members you need just to stay level."),
        ],
        "figures": {
            "intro": {
                "type": "funnel",
                "title": "Where intro buyers drop off",
                "sub": "100 intro buyers at a single yoga studio",
                "stages": [["Bought the intro", "100"], ["Came to class two", "68"], ["Took four or more classes", "44"], ["Became members", "24"], ["Still members at 6 months", "17"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how yoga studio intro offer buyers in The Woodlands and Houston convert to members",
                "caption": "The biggest single loss is between class one and class two. Fix that before buying more traffic.",
            },
            "classpass": {
                "type": "compare",
                "title": "When ClassPass helps and when it hurts",
                "left": {"title": "Hurts your studio", "items": ["Spots open in your prime-time classes", "Members can’t get in, visitors can", "No name capture or intro mention", "ClassPass share rising, members flat", "Never checking your real payout per visit"]},
                "right": {"title": "Helps your studio", "items": ["Spots in classes under half full", "Prime-time classes kept for members", "Every visitor treated as an intro lead", "Quarterly check on share of visits", "Payout compared with member visit value"]},
                "alt": "Comparison of ClassPass setups that help or hurt a yoga studio in The Woodlands and Houston",
                "caption": f"Payout mechanics from {SRC['cpfaq']}.",
            },
            "ytt": {
                "type": "steps",
                "title": "A teacher training launch timeline",
                "sub": "Counting back from the first training weekend",
                "steps": [["16 weeks out", "Training page and waitlist live: dates, tuition, payment plan, trainers, registration status."], ["12 weeks out", "Info session in the studio and on video; record it and post it on the page."], ["10 weeks out", "Personal invitations to members with 100+ classes; early tuition deadline."], ["8 to 2 weeks out", "Search ads and retargeting on; short interview call with every applicant."], ["Final week", "Last call email, then lock the cohort and start onboarding."]],
                "alt": "Timeline for marketing a yoga teacher training at a studio in The Woodlands or Houston",
                "caption": "Training is bought on a months-long timeline. Promote it like a class and you’ll run a half-empty cohort.",
            },
            "heat": {
                "type": "stats",
                "title": "Hot yoga and Houston heat",
                "stats": [["145", "days at or above 90°F in Houston in 2025"], ["105°F", "traditional Bikram-style room temperature"], ["40%", "humidity in that room"], ["104.1°F", "highest core temp in an ACE study"]],
                "note": "Sources: NWS via Houston Public Media; ACE",
                "alt": "Stats on Houston summer heat and hot yoga room conditions for yoga studio marketing in The Woodlands",
                "caption": f"From {SRC['hpm']} and the {SRC['ace']}.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for yoga studio ads",
                "sub": "Add these before the first click",
                "items": ["Gear: mat, mats, pants, leggings, blocks", "At home: youtube, video, app, at home, poses pdf", "Free hunters: free, free class (if you don’t offer one)", "Jobs: jobs, hiring, instructor salary", "Training searches in the classes campaign", "Goat yoga, beer yoga, unless you run them", "Kids yoga, unless you teach it", "Hotel and retreat searches"],
                "alt": "Checklist of negative keywords for yoga studio Google Ads in The Woodlands, Spring and Houston",
                "caption": "Then read the search terms report weekly for the first month and keep adding.",
            },
            "churn": {
                "type": "bars",
                "title": "New members needed just to stay level",
                "sub": "Studio with 180 members, by monthly churn rate",
                "items": [["3% monthly churn", 5.4, "5"], ["4% monthly churn", 7.2, "7"], ["6% monthly churn", 10.8, "11"], ["8% monthly churn", 14.4, "14"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of new members a yoga studio in The Woodlands or Houston needs each month at different churn rates",
                "caption": "Retention work shrinks the marketing problem before you spend anything on ads.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: dance
    {
        "slug": "dance-studio-marketing-the-woodlands-houston",
        "title": "Dance Studio Marketing in The Woodlands and Houston: Fall Registration, Recitals and Parents",
        "seo_title": "Dance Studio Marketing in The Woodlands & Houston",
        "desc": "Dance studio marketing in The Woodlands and Houston: fall registration timing, recital and costume fees, Meta rules for minors, trials, camps and retention.",
        "category": "Local marketing",
        "icons": ["Facebook", "Instagram", "Google"],
        "art": "b4",
        "hero": "ticket",
        "hero_alt": "Illustration for dance studio marketing in The Woodlands, Conroe, Katy and Houston",
        "related": ["martial-arts-studio-marketing-the-woodlands-houston", "daycare-marketing-houston-the-woodlands", "back-to-school-marketing-woodlands"],
        "sections": [
            (None, f"""<p>The second Tuesday in August, 9:40 p.m. Six voicemails, four web forms and a Facebook message that just says “price?” Most are about a 4-year-old and a ballet class. Two are from parents who left another studio after a recital bill they didn’t see coming.</p>
<p>That week decides a lot of your year. Conroe ISD and Katy ISD both start school on August 12, 2026, and families in The Woodlands, Conroe, Katy and Cypress settle their after-school schedules within a couple of weeks of the first bell.</p>
<p>Dance studio marketing in The Woodlands and Houston comes down to three jobs. Be in front of parents before that schedule hardens. Make the full cost of a dance year easy to understand. And keep families through the recital so they re-enroll in the fall without being sold again.</p>
<p>This is written for studio owners with recreational classes, maybe a competition team, and a spring recital, anywhere from Magnolia and Tomball down to Pearland and Sugar Land.</p>"""),

            ("Your marketing calendar is the school calendar", f"""<p>Parents buy dance the way they buy every after-school activity: around school dates. Here’s how the 2026-27 year lines up for two big districts, and what we’d run in each stretch.</p>
<div class="bp-tbl"><table>
<thead><tr><th>When</th><th>School dates</th><th>What parents are deciding</th><th>What the studio should run</th></tr></thead>
<tbody>
<tr><td>July</td><td>Summer</td><td>Fall activities, comparing studios</td><td>Registration open, fees page live, search ads on</td></tr>
<tr><td>August</td><td>Conroe ISD and Katy ISD start Aug 12</td><td>The final after-school schedule</td><td>Trial week, same-day replies, evening phone coverage</td></tr>
<tr><td>September</td><td>School settled</td><td>Late starters, kids who quit another activity</td><td>Rolling enrollment, open trial classes</td></tr>
<tr><td>October</td><td>Fall break: Conroe Oct 9-12, Katy Oct 9-13</td><td>Break plans</td><td>One- or two-day mini camp</td></tr>
<tr><td>November to December</td><td>Thanksgiving week; Conroe winter break Dec 21 to Jan 5</td><td>Gifts, holiday shows</td><td>Showcase video, gift certificates, January class list</td></tr>
<tr><td>January</td><td>Back to school</td><td>Mid-year starts, quitting</td><td>New-session push, costume deposit reminders</td></tr>
<tr><td>February to March</td><td>Conroe spring break Mar 15-19</td><td>Summer plans</td><td>Spring break camp, summer camp registration open</td></tr>
<tr><td>May</td><td>Katy’s last day May 20, Conroe’s May 27</td><td>Fall commitments</td><td>Recital, fall re-registration with deposit</td></tr>
</tbody></table></div>
<p>Dates come from {SRC['cisd']}, {SRC['katy']} and {SRC['katyfall']}. Cy-Fair, Tomball, Magnolia, Humble and Klein all publish their own calendars and don’t line up perfectly, so pull the districts your families actually attend each spring and adjust. If your recital lands in late May, it sits right on top of the last week of school, so start the re-registration push early enough that it isn’t buried under graduations and end-of-year events.</p>
<p>The bigger point: registration should open in July, not the week school starts. A parent who books a spot on July 20 doesn’t take the 9:40 p.m. call from the studio down the road on August 12. Our {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing post')} covers the broader season.</p>"""),

            ("Parents are the buyer", f"""<p>The dancer might be four. The buyer is a parent juggling a sibling’s soccer practice, a drive on FM 2978 or the Grand Parkway, and a budget. Before they call, they want answers to a short list, and your website should give them without a phone call:</p>
<ul>
<li>Can I get there from school pickup? Show class times by age on one page.</li>
<li>What does the whole year cost, recital included? (Next section.)</li>
<li>Is this a competition studio or a fun one? Most studios are both. Say which track a new student starts on.</li>
<li>Can I watch? A viewing window or a monthly watch week answers a lot of nerves.</li>
<li>What do they wear, and where do I buy it?</li>
<li>Do boys take class here? Studios that show boys in classes get more boys.</li>
</ul>
<p>Write class descriptions for parents. “Ballet and Tap Combo, ages 3 to 5, 45 minutes. Kids learn to follow directions, take turns and stand in a line, and they think they’re just dancing.” That last line sells more spots than “introduction to ballet technique.”</p>"""),

            ("Recital economics and why costume fees belong on your website", f"""<p>The recital is the finale of your product, your biggest marketing event of the year and, for many studios, a real chunk of revenue. It’s also where parents feel nickel-and-dimed if nobody told them the numbers in August.</p>
<p>Fee structures vary a lot. In {SRC['dt_fee']}, the owners of one studio described three models they’ve used: a $120 flat recital fee covering two tickets, a performance DVD, a T-shirt, flowers and a program; a $129 fee including a costume, tights and accessories, with extra costumes at $85; and a $12 monthly fee across a nine-month season that folded in registration, a costume, a T-shirt and a DVD. Costume prices covered in {SRC['dt_cost']} ranged from $70 per costume for elementary students at a Minnesota studio (families kept them) to a $350 nonrefundable costume rental fee at a Connecticut ballet school. The advice from those owners: disclose costume costs at registration, give an amount and a due date, and say whether the family keeps the costume.</p>
<!--fig:fees-->
<p>We’d go a step further and publish a “what a dance year costs” page. It doesn’t lose you enrollments. It loses you the families who would have left angry in March and told every parent at pickup. A simple version:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Cost</th><th>Amount</th><th>When it’s due</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Registration fee</td><td>[your price] per family</td><td>At enrollment</td><td>Once a year</td></tr>
<tr><td>Monthly tuition</td><td>[your price] per class</td><td>1st of each month</td><td>Sibling and multi-class discounts</td></tr>
<tr><td>Costume</td><td>[your price] per class</td><td>Deposit in October or November</td><td>Say whether families keep it</td></tr>
<tr><td>Recital fee</td><td>[your price] per dancer</td><td>March</td><td>List what it covers</td></tr>
<tr><td>Recital tickets</td><td>[your price] each</td><td>April or May</td><td>Say if any are included</td></tr>
<tr><td>Shoes and dancewear</td><td>Varies by class</td><td>Before the first class</td><td>Link the exact items</td></tr>
<tr><td>Competition fees</td><td>Competition team only</td><td>Per event</td><td>Separate page with a season estimate</td></tr>
</tbody></table></div>
<p>Put the costume deposit date in your billing system and send a reminder two weeks before. The deposit is a cancellation moment for some families, so it helps if it lands after the winter showcase, when kids are excited, rather than right after the holiday credit card bills.</p>"""),

            ("Trial classes that turn into fall enrollments", f"""<p>Most studios offer a trial class. Fewer run it like a sale.</p>
<ul>
<li><b>Book a specific class.</b> “Come try any class” produces no-shows. A booked Tuesday 4:30 with a name on the roster gets kids in the door.</li>
<li><b>The first ten minutes matter most.</b> Greet the child by name at the door, name tag on, teacher hands-on with the new kid in the first exercise. The parent at the window is watching their child’s face, not the choreography.</li>
<li><b>Older kids get placement.</b> A 10-year-old who danced elsewhere wants to know she won’t be with the 6-year-olds. Offer a placement class and say so.</li>
<li><b>Follow up the same day.</b> A text from the front desk with the enrollment link and “we’re holding her spot in Tuesday 4:30 until Friday.” Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} explains why hours matter.</li>
<li><b>Run trial weeks in August and January</b> when demand peaks, and keep a standing trial option the rest of the year.</li>
</ul>
<!--fig:trial-->
<p>Track the whole chain by source: inquiries, trials booked, trials attended, enrolled, and still enrolled at the recital. The last step is the one that tells you whether a channel brings families who stay.</p>"""),

            ("Meta ads, minors and the rules you work within", f"""<p>Facebook and Instagram are where parents of young dancers spend their scrolling time, so they’re the main paid channel for most studios. A few rules shape how you can use them.</p>
<p>Targeting teens is restricted. Since February 2023, advertisers can only use age and location to reach teens on Facebook and Instagram, and gender is no longer an option, per {SRC['metateen']}. Interest-based teen targeting was already gone. So for a 15-year-old’s contemporary class, you advertise to the parent.</p>
<p>Targeting adults is less precise than it used to be, too. Meta removed detailed targeting exclusions from Ads Manager in 2025 and has been consolidating interest options, per {SRC['linear']}. In practice we target adults in a radius around the studio and let the creative do the filtering. An ad that says “Ballet and tap for ages 3 to 5, Tuesdays at 4:30, five minutes from Kuykendahl and Research Forest” finds the right parents because everyone else scrolls past.</p>
<p>Then there’s the content itself. Your best creative is kids dancing. That’s fine with consent and some care.</p>
<!--fig:minors-->
<p>Meta has also added protections around accounts that mostly feature children. In July 2025 it said adult-managed accounts that primarily feature children would be placed in its strictest message settings, get Hidden Words turned on to filter offensive comments, be harder to find in search, and not be recommended to potentially suspicious adults, per {SRC['metakids']}. The announcement talks about parents and talent managers, and we don’t know exactly how Meta treats a studio business account. The direction is clear anyway. Keep the public feed a mix of teachers, the studio, older students and group shots, and save the close-ups for your private parent app or group.</p>
<p>For lead forms, keep them short and ask one qualifying question (child’s age). Our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'post on fixing bad Facebook leads')} covers the settings.</p>"""),

            ("Competition teams need their own marketing", f"""<p>Recreational families and competition families want different things, and one Instagram feed rarely serves both. A grid full of trophies and tricks can scare off the parent of a shy 5-year-old. A grid full of tutus doesn’t recruit a serious 12-year-old.</p>
<ul>
<li><b>Recruit comp mostly from inside.</b> Your rec classes are the pipeline. Invite promising students and their parents to watch a team rehearsal, and hold auditions on a published date in late spring.</li>
<li><b>Give the team its own page.</b> Commitment (hours a week, required classes), the travel calendar, a season cost estimate with [your price] placeholders filled in honestly, and the audition date.</li>
<li><b>Post results, accurately.</b> Real placements from real events, with parent permission for any names. Never round up.</li>
<li><b>Use Instagram highlights</b> to split the feed: “Rec classes,” “Competition team,” “Recital.” Parents go straight to the one they care about.</li>
</ul>
<p>Comp parents are also your loudest reviewers and your most active referrers. Treat the team parents’ group chat as a channel you’re part of, with a clear weekly update from the studio, so rumors don’t fill the gap.</p>"""),

            ("Summer camps and the Texas rules to check first", f"""<p>Summer camps cover the June and July revenue gap and introduce kids who’ll enroll in the fall. They also sit near two sets of Texas rules worth reading before you print a flyer.</p>
<p>The first is youth camp licensing. Texas tightened youth camp requirements after the July 2025 Hill Country floods, and {SRC['kprc']} reported only 18 youth camps were fully licensed in mid-May 2026 as camps worked through new emergency plan rules. But {SRC['dshs']} says the law doesn’t apply to programs HHSC regulates as child care, programs that don’t offer outdoor activities, or programs that focus on one specific activity “like gymnastics, baseball, or music.” An indoor, dance-only camp looks like it falls outside the youth camp law. A “dance, crafts and splash day” camp might not. DSHS has a lookup tool; check before you plan the week.</p>
<p>The second is child care licensing. Texas exempts single-skill programs only when they meet conditions, including that the program doesn’t advertise or present itself as a child-care facility, day-care center or licensed before- or after-school program, tells parents it isn’t state-licensed and about the physical risks involved, and runs DPS background checks on employees and volunteers who work with children, per {SRC['hrc']}. So the words in your marketing matter. Say “dance camp,” “ballet intensive” or “musical theater week.” Don’t say “summer care” or “after-school pickup and care.” Have your attorney read the camp page.</p>
<p>Marketing the camps themselves is simple. Open registration in February or March, sell current families first with an early deadline, then run Meta ads to parents in your radius with the themed weeks, times and price. Half-day options sell well for 3- to 6-year-olds. Post each week as a Business Profile update.</p>"""),

            ("Google Business Profile, search ads and reviews", f"""<p>When a parent types “dance classes for kids near me,” the map results usually beat the websites. Get the profile right first.</p>
<ul>
<li><b>Category.</b> Dance school as primary. Add others only for what you actually run.</li>
<li><b>Booking link</b> to your trial class or registration page, set as the preferred link, per {SRC['gbpbook']}.</li>
<li><b>Photos</b> of the lobby, the viewing window, each studio room, the parking lot at pickup time and a recital group shot. Parents check whether drop-off looks safe.</li>
<li><b>Posts</b> for registration dates, camps and recital tickets.</li>
</ul>
<p>Search ads work well for dance because the searches are specific: ballet classes The Woodlands, toddler dance classes Spring TX, hip hop dance classes for kids Katy, competitive dance studio Cypress, adult ballet Houston. Build an ad group per style or age, each pointing at that class’s page, and set location to people in or regularly in your area using {SRC['loc']}.</p>
<p>Negatives to add on day one: dance club, nightclub, salsa night, dance shoes, dancewear store, jobs, teacher, free, YouTube, TikTok tutorial, and quinceañera or pole unless you offer them. Run ads hardest from mid-July through September and again in early January; trim them in March and April unless you’re selling camps.</p>
<p>Reviews come easiest after the first month and after the recital, from the same link sent to every family. Google’s rules ban incentives, asking only happy families, and staff quotas or staff-name contests, per {SRC['gpol']}. Our {L('/blog/complete-guide-google-reviews/', 'reviews guide')} has request scripts, and {L('/services/search-marketing/', 'our search team')} can run the ads.</p>"""),

            ("Retention: the recital is your re-enrollment campaign", f"""<p>Dance studios have predictable cliffs. September, when a kid who never settled in quits. January, after the holiday break. Around the costume deposit. And the weeks after the recital, when summer starts and the habit breaks.</p>
<!--fig:drops-->
<p>What we’d do about each:</p>
<ul>
<li><b>Open fall re-registration before the recital,</b> with a deposit that holds the family’s current day and time. The slot is the thing they’re afraid to lose.</li>
<li><b>Send a short progress note from each teacher in December.</b> Two sentences about what the child learned. It lands right before the January decision.</li>
<li><b>Keep summer contact.</b> One summer class or a camp week keeps the habit alive. Families who disappear from June to August are the ones who don’t come back.</li>
<li><b>Recital week is review week.</b> Families are proud and filming everything. Send the review link the next day.</li>
<li><b>Pick one communication channel</b> (an app or email) and send a weekly update on a fixed day. Surprises cause cancellations, especially money surprises.</li>
</ul>
<p>If you text families about promotions, read our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} first. Schedule updates and promo blasts aren’t treated the same.</p>"""),

            ("What to spend, what to track, and a first 90 days", f"""<p>The number that matters is cost per enrolled student, by source, and how many of those students were still dancing at the recital. Cost per lead flatters Meta forms and hides the families who never showed up.</p>
<p>For a single-location studio, an illustrative paid budget is $600 to $1,500 a month from mid-July through September, split between Google Search and Meta, then a lighter level the rest of the year with bumps in January and for camp registration. Your own tracked results should replace those numbers within one season.</p>
<!--fig:plan-->
<p>If you want a senior strategist to build a season plan around your classes, calendar and budget, <a href="/contact/">get in touch</a>. Running yoga or music programs too? See our {L(YOGA, 'yoga studio guide')} and {L(MUSIC, 'music school guide')}.</p>"""),
        ],
        "faq": [
            ("When should a dance studio in The Woodlands start fall registration marketing?",
             "Open registration and turn on ads in July. Conroe ISD and Katy ISD both start school on August 12, 2026, and parents in The Woodlands, Conroe and Katy set after-school schedules within a couple of weeks of that date. Families who book in July are off the market by August. Keep a trial week and fast phone and text replies running through August and September for late deciders."),
            ("Can I target teenagers with Facebook ads for my dance studio?",
             "Only in a very limited way. Since February 2023, Meta lets advertisers reach teens using only age and location, and gender targeting for teens was removed. Interest targeting for teens was already gone. For most studios it works better to advertise to parents in a radius around the studio, with creative that names the class, age range, day and time so the right families recognize it."),
            ("Should a dance studio publish its costume and recital fees?",
             "Yes. Parents compare studios on the full cost of a dance year, and surprise recital and costume bills are a common reason families leave or post angry reviews. Publish registration, tuition, costume, recital fee and ticket costs with due dates, and say whether families keep costumes. Studio owners quoted by Dance Teacher recommend disclosing costume costs at registration with an amount and due date."),
            ("Do dance summer camps in Texas need a youth camp license?",
             "Possibly not, but check. A Texas DSHS parent resource says the youth camp law doesn’t apply to programs focused on one specific activity, programs without outdoor activities, or programs regulated as child care. A dance-only indoor camp may fall outside it, while a mixed-activity camp might not. Separately, single-skill programs exempt from child care licensing must not advertise as child care. Confirm with DSHS and your attorney."),
            ("How do I get more students for my dance studio in Houston?",
             "Be visible before the school year locks in: open registration in July, run Google Search ads on specific class and age searches, and advertise to parents near the studio on Facebook and Instagram. Make costs and class times easy to find online, book trial classes into specific sessions, follow up the same day, and open fall re-registration before the recital so current families stay."),
        ],
        "figures": {
            "fees": {
                "type": "compare",
                "title": "How studios handle recital and costume costs",
                "left": {"title": "Fees that cause cancellations", "items": ["Costume cost first mentioned in November", "Recital fee and tickets billed separately, late", "Nobody says who keeps the costume", "Comp team costs explained at the first meet", "Different answers from different staff"]},
                "right": {"title": "Fees parents plan for", "items": ["“What a year costs” page at registration", "Amounts and due dates on one page", "Costume ownership stated up front", "Separate comp team cost estimate", "Reminders two weeks before each charge"]},
                "alt": "Comparison of dance studio recital and costume fee practices for studios in The Woodlands and Houston",
                "caption": f"Based on advice from studio owners in {SRC['dt_cost']} and our own view of what parents ask.",
            },
            "trial": {
                "type": "funnel",
                "title": "From inquiry to recital",
                "sub": "100 fall inquiries at a single studio",
                "stages": [["Inquiries", "100"], ["Trial booked", "62"], ["Trial attended", "48"], ["Enrolled", "33"], ["Danced in the recital", "26"]],
                "note": "Illustrative example",
                "alt": "Funnel of dance studio inquiries, trial classes and enrollments for a studio in The Woodlands or Houston",
                "caption": "Judge each ad source on the last row, not the first.",
            },
            "minors": {
                "type": "checklist",
                "title": "Before a student appears in an ad",
                "sub": "Consent and care for photos of minors",
                "items": ["Photo and video release in the registration form, with an opt-out", "Separate yes for paid ads, not just social posts", "No last names, schools or class times beside a child’s face", "Group and stage shots over costume close-ups", "Comments watched and filtered on posts with kids", "Teachers and adult dancers in most paid creative", "Remove any image the day a parent asks"],
                "alt": "Checklist for using photos of child dancers in Meta ads for a dance studio in The Woodlands and Houston",
                "caption": "Our practice, not a legal standard. Have your attorney review your release form.",
            },
            "drops": {
                "type": "bars",
                "title": "When families tend to leave",
                "sub": "Share of a season’s dropouts by period",
                "items": [["September: never settled in", 18, "18%"], ["January: after winter break", 30, "30%"], ["Costume deposit and spring break", 14, "14%"], ["June: after the recital", 38, "38%"]],
                "highlight": [3],
                "note": "Illustrative example",
                "alt": "Bar chart of when families leave a dance studio in The Woodlands or Houston during the season",
                "caption": "Your own billing data will show your pattern. The post-recital drop is the one re-registration fixes.",
            },
            "plan": {
                "type": "steps",
                "title": "A first 90 days for a dance studio",
                "sub": "Starting in May for the fall season",
                "steps": [["Weeks 1-2", "Fees page, class finder by age, Business Profile booking link and photos."], ["Weeks 3-4", "Fall re-registration with deposit opens to current families before the recital."], ["Weeks 5-8", "Summer camp sales to families, then Meta ads to parents in your radius."], ["Weeks 9-10", "Search campaigns by style and age, negatives, call and form tracking."], ["Weeks 11-13", "Trial week scheduled for August, same-day follow-up script, review requests."]],
                "alt": "Ninety-day marketing plan for a dance studio in The Woodlands and Houston ahead of fall registration",
                "caption": "Starting in May means you’re ready when parents start comparing in July.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: music lessons
    {
        "slug": "music-lessons-school-marketing-the-woodlands-houston",
        "title": "Music Lesson School Marketing in The Woodlands and Houston: Fill Slots and Keep Students",
        "seo_title": "Music School Marketing in The Woodlands & Houston",
        "desc": "Music lesson school marketing for The Woodlands and Houston: Google Ads, Business Profile, trial lessons, recitals, TMEA season and teacher retention.",
        "category": "Paid ads",
        "icons": ["Google Ads", "Google Business Profile", "YouTube"],
        "art": "b6",
        "hero": "play",
        "hero_alt": "Illustration for music lessons school marketing in The Woodlands, Spring and Houston",
        "related": ["tutoring-center-marketing-houston", "martial-arts-studio-marketing-the-woodlands-houston", "private-school-enrollment-marketing-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Tuesday, 4:15 p.m. Every room is booked, the piano teacher has a waitlist of eight, and a parent in the lobby is asking whether her son can move to 5:00 because of tennis. Tuesday at 11 a.m., the building is empty except for one adult guitar student and the owner doing payroll.</p>
<p>Then the voice teacher tells you she’s moving to Austin in June. Nineteen students are hers.</p>
<p>Music school marketing in The Woodlands and Houston is mostly a scheduling problem in disguise. You need to fill the hours outside 3:30 to 7:30 on weekdays, keep students long enough to reach their first recital and then their second year, and make sure students feel attached to the school as well as the teacher. Google Ads and a solid Business Profile bring in the inquiries. Most of this guide is about turning those inquiries into students who stay.</p>
<p>It’s written for independent lesson schools and studios with a handful of teachers, from Spring and The Woodlands to Katy, Cypress, Kingwood and Pearland.</p>"""),

            ("Your lesson schedule is your inventory", f"""<p>A lesson school sells teacher hours in rooms. The after-school block fills itself. Everything else needs marketing, and each block has a different buyer.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Time block</th><th>Who can come</th><th>Typical demand</th><th>Marketing move</th></tr></thead>
<tbody>
<tr><td>Weekdays 3:30 to 7:30 p.m.</td><td>School-age kids</td><td>Full, with waitlists</td><td>No ads. Waitlist, then a price review.</td></tr>
<tr><td>Weekdays 9 a.m. to 2 p.m.</td><td>Adults, homeschool families, retirees, shift workers</td><td>Mostly empty</td><td>Adult and homeschool campaigns</td></tr>
<tr><td>Weekdays 7:30 to 9 p.m.</td><td>Working adults, high schoolers after rehearsal</td><td>Partly full</td><td>Adult beginners, audition prep</td></tr>
<tr><td>Saturday morning</td><td>Everyone</td><td>Full</td><td>Group classes and band rehearsals</td></tr>
<tr><td>Saturday afternoon</td><td>Families with packed weekdays</td><td>Partly full</td><td>Group programs, make-up lessons</td></tr>
</tbody></table></div>
<!--fig:fill-->
<p>Before spending on ads, look at your own fill rate by block. Advertising “piano lessons for kids” when every after-school slot is taken just builds a waitlist you’ll lose. Advertising adult lessons at 10 a.m. sells hours you’d otherwise waste.</p>"""),

            ("Private lessons vs. group programs", f"""<p>Most schools start with private lessons and add group programs later, if ever. We’d add them sooner. They do different marketing jobs.</p>
<!--fig:format-->
<p>Private lessons are the core: flexible, personal, and priced per half hour or hour. Their weakness is that the student’s loyalty sits with one teacher, and the room earns one tuition per hour.</p>
<p>Group programs, like early childhood music, group piano for beginners, ukulele for 7-year-olds or a rock band program, fill a room with several tuitions at once. They also give kids friends at your school, and kids with friends there stay longer. A rock band program in particular is a retention product and a content engine. Kids practice because they don’t want to let the band down, and every end-of-season show at a local venue in The Woodlands or Spring is a night of video, parent posts and grandparents asking where the kid takes lessons.</p>
<p>A good structure: group classes as the low-cost front door for young beginners, private lessons as the main product, and bands or ensembles as the reason students stay into high school.</p>"""),

            ("Kids vs. adult students: two different buyers", f"""<p>Parents buy lessons for kids. Adults buy lessons for themselves. The searches, fears and best times are different, so the ads and pages should be too.</p>
<ul>
<li><b>Parents</b> search “piano lessons for kids near me,” “guitar lessons for kids The Woodlands,” “violin lessons Katy.” They care about the teacher’s background and background check, whether they can sit in, location against school pickup, and progress they can see. They buy in August and January.</li>
<li><b>Adults</b> search “adult piano lessons,” “guitar lessons for beginners,” “voice lessons Houston.” Their fear is being the only grown-up beginner in a lobby full of 9-year-olds. They want weekday daytime or late-evening slots, an optional recital (never mandatory), and a teacher who’s patient with rust. They buy in January and whenever something reminds them they always meant to learn.</li>
</ul>
<p>Sample ad copy for the adult daytime campaign:</p>
<p><i>Headline:</i> Adult Piano Lessons, The Woodlands | Weekday Mornings Available | Beginners Welcome<br>
<i>Description:</i> Private 30- or 45-minute lessons with patient teachers. No recital required. Book a trial lesson this week.</p>
<p>And for parents: <i>Kids’ Piano and Guitar Lessons | Background-Checked Teachers | Trial Lesson Credited to Month One.</i></p>"""),

            ("Trial lessons that turn into students", f"""<p>We lean toward a paid trial lesson with the fee credited to the first month, at [your price]. It filters out people shopping for something free and still feels low risk.</p>
<ul>
<li><b>The trial is a match.</b> Pick the teacher for the student’s age and goal before they arrive. A 7-year-old and a 45-year-old shouldn’t get the same teacher by default.</li>
<li><b>Thirty minutes is plenty.</b> The parent or adult student should leave having played something, even three notes.</li>
<li><b>End with a plan.</b> One sentence from the teacher: “In eight weeks she’ll play this with both hands.” That sentence closes more enrollments than the front desk does.</li>
<li><b>Book the weekly slot before they leave,</b> and hold it for 48 hours if they need to check the family calendar.</li>
<li><b>Follow up the same day</b> if they didn’t book. Inquiries go cold fast; our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} covers the timing.</li>
</ul>
<!--fig:trial-->"""),

            ("Google Ads for “piano lessons near me”", f"""<p>Lesson searches are local and specific, which makes Google Search the most direct paid channel for a music school.</p>
<ul>
<li><b>One ad group per instrument</b> (piano, guitar, voice, violin, drums), each sending traffic to that instrument’s page with teacher photos, times and the trial offer. Never the homepage.</li>
<li><b>Kids and adult versions</b> of your biggest instruments, with different landing pages.</li>
<li><b>Location set to presence.</b> Choose people in or regularly in your targeted locations, per {SRC['loc']}. Then draw the radius around a realistic weekly drive. In The Woodlands, a family off Research Forest won’t drive to Kingwood every Tuesday.</li>
<li><b>Ad schedule</b> matched to when someone answers the phone, with forms covering the rest.</li>
<li><b>Calls and trial bookings tracked as conversions.</b> Our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking guide')} shows how.</li>
</ul>
<!--fig:negatives-->
<p>An illustrative starting budget for one location is $500 to $1,200 a month, weighted toward August, September and January. Judge it on cost per enrolled student and on how many are still enrolled six months later. We’d skip national keywords like “online piano lessons” entirely; you’d be bidding against apps and marketplaces for students who’ll never visit. Our {L('/services/search-marketing/', 'search marketing team')} runs accounts like this, and our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} help set expectations.</p>"""),

            ("Google Business Profile for a lesson school", f"""<p>“Guitar lessons near me” on a phone usually shows the map first. Your profile is the first impression.</p>
<ul>
<li><b>Category.</b> Music school as primary. Type each instrument into the category field to see what instructor categories Google offers, and add the ones that match what you teach.</li>
<li><b>Services.</b> List each instrument and program with a one-line description and age range.</li>
<li><b>Booking link</b> to your trial lesson page, set as the preferred link, per {SRC['gbpbook']}.</li>
<li><b>Photos</b> of lesson rooms, instruments, the waiting area, recitals and band shows (with permission), and the building from the parking lot.</li>
<li><b>Posts</b> for recital dates, summer programs, audition prep and new teachers.</li>
</ul>
<p>Reviews from parents carry the most weight. Ask after the first month and after each recital, with the same link to everyone. Google’s policy bans incentives for reviews, selectively asking happy customers, and asking staff to collect a set number of reviews or reviews that name a staff member, per {SRC['gpol']}. So “leave a review mentioning Mr. Daniel” is out, even if Mr. Daniel is the reason they stay. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} goes further.</p>"""),

            ("School band, orchestra and choir season is your best content calendar", f"""<p>Texas school music runs on an audition calendar, and parents of serious middle and high school students feel every date. That makes it the most useful content and offer calendar a lesson school has.</p>
<p>The TMEA All-State path starts with region auditions in the fall, continues through area auditions for high schoolers in winter, and ends at the TMEA Clinic/Convention in San Antonio, which runs February 10 to 13, 2027, per {SRC['tmea']}. For a local example, {SRC['khs']} in Humble ISD lists its 2026-27 choir dates: district auditions September 12, region October 19 at Atascocita High School, pre-area December 3, and area January 9 at The Woodlands High School. Band and orchestra run their own region schedules, and for the 2026 cycle, {SRC['tmeaas']} had band and orchestra students recording All-State seating auditions online in a January window.</p>
<p>In spring, solo and ensemble season takes over. The Texas State Solo &amp; Ensemble Contest for state-qualifying solos and small ensembles runs May 29 and 31, 2027, at sites in the Austin area, with registration April 1 to 15, per {SRC['tssec']}.</p>
<!--fig:dates-->
<p>How to use it:</p>
<!--fig:season-->
<p>Write a short, practical page for each stage: how to prepare for region auditions, what a mock audition is and why it helps, how to find an accompanist for solo and ensemble. Parents search those questions, and band directors in Conroe ISD, Katy ISD and Cy-Fair ISD get asked for private teacher recommendations constantly. Introduce yourself to local directors, ask how their district handles private lesson teachers, and make it easy to recommend you. Celebrate students who advance only with parent permission, and never claim results you can’t back up.</p>"""),

            ("Recitals, rock shows and performances as marketing", f"""<p>A recital is a retention tool first. Students practice harder when a date is on the calendar, and parents see progress they paid for. It’s a referral tool second, because grandparents, neighbors and classmates are in the audience.</p>
<ul>
<li>Hold recitals twice a year, at a real venue if you can (a church sanctuary or a school auditorium in The Woodlands or Spring looks and sounds better than your lobby).</li>
<li>Film every performance with permission and send families their clip. They’ll share it, and the share tags you.</li>
<li>Make adult recitals optional and low-key. An evening “adult student open mic” keeps adults from feeling dragged into a kids’ event.</li>
<li>Send the review request and the fall or summer re-enrollment link within two days of each recital, when pride is highest.</li>
</ul>
<p>If you sell tickets to band shows, our {L('/blog/how-to-sell-more-event-tickets-houston/', 'event ticket guide')} covers the basics.</p>"""),

            ("Teacher retention is a marketing problem too", f"""<p>Back to the voice teacher moving to Austin. When a teacher leaves, students follow, or they quit. Nineteen students at [your price] a month is a big hole, and no ad campaign refills it quickly.</p>
<p>The marketing fix is making the school, not only the teacher, the thing families are attached to:</p>
<ul>
<li>A front desk that knows every family and handles scheduling, so the teacher isn’t the only relationship.</li>
<li>Group programs, bands and recitals that tie students to friends and events at the school.</li>
<li>Short progress reports from the school each semester, in the school’s voice.</li>
<li>Teacher pages on your site that build each teacher up as part of a team.</li>
</ul>
<p>The operations side matters as much. Teachers stay where their schedule is dense (no single 4:30 lesson with nothing after), pay is fair, recital time is paid, and there’s a path to more students. When someone does leave, announce it early, introduce the new teacher in a joint lesson, and keep the student’s day and time. Non-solicitation terms in teacher agreements, and whether teachers are employees or contractors, are questions for your attorney and CPA, not your marketing agency.</p>"""),

            ("Referral programs and online lessons", f"""<p>Referrals are the cheapest students you’ll get. A simple program works: a lesson credit for the referring family when a referred student enrolls and stays a month, plus a sibling discount. Give out referral cards at recitals and band shows, and run a bring-a-friend week for group classes. Keep referrals and reviews completely separate, though. Rewarding a referral is fine. Rewarding a review breaks Google’s rules, per {SRC['gpol']}.</p>
<p>Online lessons are a retention tool more than a growth channel. Use them for summer travel, sick days, storm closures and students who move to Conroe or Magnolia and don’t want to lose their teacher. Mention the option on your site and profile as “in studio, or online when you can’t make it.” Building a national online business is a different company with different competitors.</p>"""),

            ("What to track, and a first 90 days", f"""<p>Track six numbers monthly: inquiries by source, trial-to-enrolled rate, cost per enrolled student, six-month retention, fill rate by time block, and teacher turnover. If fill rate in the daytime block isn’t rising, the adult and homeschool campaigns aren’t working, whatever the click numbers say.</p>
<ol>
<li><b>Days 1 to 30.</b> Business Profile cleanup, instrument pages, a trial lesson page with booking, call and form tracking, and review requests to current families.</li>
<li><b>Days 31 to 60.</b> Google Search by instrument with negatives in place, an adult daytime campaign, and a same-day follow-up routine for trials.</li>
<li><b>Days 61 to 90.</b> Launch one group program or band season, map the school music calendar for your districts, and plan the next recital with re-enrollment built in.</li>
</ol>
<p>If you’d like a senior strategist to build a plan around your rooms, teachers and schedule, <a href="/contact/">get in touch</a>. Sharing a building with a dance or yoga program? Our {L(DANCE, 'dance studio guide')} and {L(YOGA, 'yoga studio guide')} cover those.</p>"""),
        ],
        "faq": [
            ("How do I get more students for my music school in The Woodlands?",
             "Start with the hours you can actually fill. Run Google Search ads by instrument with tight local targeting, keep your Google Business Profile complete with a trial lesson booking link, and ask every family for a review. Offer a trial lesson credited to the first month, book the weekly slot before they leave, and build adult daytime and group programs to fill hours outside the after-school rush."),
            ("What keywords should a music school use in Google Ads?",
             "Use instrument plus audience plus place, such as piano lessons for kids near me, guitar lessons The Woodlands, voice lessons Houston or adult piano lessons Spring TX, with each instrument in its own ad group and landing page. Add negatives for free, YouTube, app, chords, tabs, sheet music, for sale, tuning, movers and jobs, and avoid national terms like online piano lessons."),
            ("Should a music school offer free trial lessons?",
             "A paid trial credited to the first month usually works better than a free one. It filters out people collecting free lessons and still feels low risk to parents. Match the teacher to the student before the trial, keep it to about 30 minutes, end with a one-sentence plan from the teacher, and book the weekly slot before the family leaves."),
            ("When are TMEA region and All-State auditions?",
             "Region auditions happen in the fall, area auditions for high schoolers follow in winter, and All-State students perform at the TMEA Clinic/Convention in San Antonio, scheduled for February 10 to 13, 2027. Exact dates vary by region and division; a Humble ISD choir page lists region on October 19, 2026 and area on January 9, 2027 at The Woodlands High School. Check your region’s calendar each year."),
            ("How do music schools keep students when a teacher leaves?",
             "Tie families to the school, not only the teacher. Use a front desk that handles scheduling, group programs and recitals, school progress reports and teacher pages that present a team. When a teacher leaves, announce it early, introduce the new teacher in a joint lesson and keep the student’s day and time. Dense schedules and fair, paid recital time help keep teachers longer."),
        ],
        "figures": {
            "fill": {
                "type": "bars",
                "title": "Lesson room fill rate by time block",
                "sub": "A five-room music school, one typical week",
                "items": [["Weekdays 3:30 to 7:30 p.m.", 96, "96%"], ["Saturday morning", 90, "90%"], ["Weekdays 7:30 to 9 p.m.", 55, "55%"], ["Saturday afternoon", 40, "40%"], ["Weekdays 9 a.m. to 2 p.m.", 12, "12%"]],
                "highlight": [4],
                "note": "Illustrative example",
                "alt": "Bar chart of lesson room fill rates by time block at a music school in The Woodlands or Houston",
                "caption": "The marketing opportunity is the bottom rows. The top ones need a waitlist.",
            },
            "format": {
                "type": "compare",
                "title": "Private lessons vs. group programs",
                "left": {"title": "Private lessons only", "items": ["One tuition per room hour", "Loyalty sits with one teacher", "No friends at the school", "Recital is the only event", "Hard to fill daytime hours"]},
                "right": {"title": "Private plus group programs", "items": ["Several tuitions per room hour", "Ties to the school, bands and friends", "Low-cost front door for beginners", "Shows that double as marketing", "Group classes for daytime and Saturdays"]},
                "alt": "Comparison of private lessons and group music programs for a lesson school in The Woodlands and Houston",
                "caption": "Group programs are the on-ramp and the glue. Private lessons stay the core.",
            },
            "trial": {
                "type": "funnel",
                "title": "From inquiry to a student who stays",
                "sub": "100 lesson inquiries",
                "stages": [["Inquiries", "100"], ["Trial booked", "55"], ["Trial attended", "46"], ["Enrolled", "33"], ["Enrolled at six months", "23"]],
                "note": "Illustrative example",
                "alt": "Funnel of music lesson inquiries, trial lessons and enrollments for a music school in The Woodlands or Houston",
                "caption": "Six-month retention tells you which ad sources bring students who stay.",
            },
            "negatives": {
                "type": "checklist",
                "title": "Negative keywords for music lesson ads",
                "sub": "Add these before you launch",
                "items": ["Free: free, free online, youtube, app", "Self-teaching: chords, tabs, tutorial, sheet music", "Buying: for sale, used, keyboard, store", "Services: piano tuning, piano movers, repair", "Jobs: jobs, hiring, teacher salary", "College: degree, university, certification", "National: online piano lessons (unless you sell them)", "Instruments you don’t teach"],
                "alt": "Checklist of negative keywords for music school Google Ads in The Woodlands and Houston",
                "caption": "Then read the search terms report weekly for the first month.",
            },
            "dates": {
                "type": "stats",
                "title": "Texas school music dates, 2026-27",
                "stats": [["Oct 19", "region choir auditions at Atascocita HS"], ["Jan 9", "area auditions at The Woodlands HS"], ["Feb 10", "TMEA convention opens in San Antonio"], ["May 29", "state solo and ensemble begins"]],
                "note": "Sources: Kingwood HS choir, TMEA, UIL",
                "alt": "Key Texas school music audition and contest dates for music lesson marketing in The Woodlands and Houston",
                "caption": f"Choir dates from {SRC['khs']}; band and orchestra regions keep their own calendars.",
            },
            "season": {
                "type": "steps",
                "title": "Turn the school music year into offers",
                "sub": "Content and lesson packages by season",
                "steps": [["Summer", "Region prep lesson packages for students learning this year’s audition music."], ["Early fall", "A Saturday mock audition with your teachers as the panel, weeks before region."], ["Winter", "Extra lessons for students who advance to area and All-State."], ["Spring", "Solo and ensemble coaching and accompanist booking."], ["May", "State qualifiers get coaching; everyone else gets a summer lesson plan."]],
                "alt": "Seasonal music lesson offers built around TMEA and UIL calendars for schools in The Woodlands and Houston",
                "caption": "Each step is also a page parents search for and a post band directors can share.",
            },
        },
    },
]
