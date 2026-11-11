"""Batch 10: martial arts studio marketing in The Woodlands and Houston, tutoring and learning center marketing in
Houston, and hair salon and barbershop marketing in The Woodlands and Houston.

Research (martial arts): Meta's January 2023 newsroom post (teens reached by age and location only, gender and
engagement removed from February 2023); Linear Design's detailed targeting guide (parents options, 2022-2025 removals,
detailed targeting exclusions removed in 2025); Texas Human Resources Code 42.041(b)(18) single-skill exemption
conditions (no unrelated services, can't advertise as child care or after-school program, parent notice, DPS
background checks); Texas HHS Child Care Regulation handbook 2300 (programs failing the exemption may be school-age
programs under Chapter 744, forms 2832/2833); KPRC (May 2026) on new youth camp safety laws after the Hill Country
floods, day camps included; Aspen Institute Project Play State of Play 2025 (youth sports costs up 46% since 2019);
Google Maps prohibited content policy; PPC Land on the April 2026 staff-quota review rule; Morgan Lewis on Texas SB 140;
Conroe ISD 2026-27 calendar (My Neighborhood News) and Cy-Fair ISD 2026-27 calendar (Community Impact).
Tutoring: TEA 2026-2027 testing calendar (Dec 1-11 EOC, April 6-30 spring windows, June 15-25 EOC); Texas Public Radio
on HB 8 (STAAR replaced by three shorter tests from 2027-28, results in about two days); College Board SAT dates
2026-27; ACT registration page (Dec 12, 2026 and Feb 27, 2027); Texas Comptroller releases (Nov 25, 2025 final rules,
Mar 16, 2026 200,000 applications); EducationFreedom.Texas.gov (amounts $10,474 / up to $30,000 / up to $2,000, 274,000+
applications, 100,000+ awards, funding July 1 2026 etc.) and its providers-vendors page (rolling applications, Odyssey);
SB 2 enrolled text, Sec. 29.358 (tutor credentials, national criminal history review) and 29.359 (tutoring and
assessment costs allowed); Morgan Lewis on the FTC consumer reviews rule (effective Oct 21, 2024); FTC Endorsement
Guides FAQ (generally expected results); Houston Chronicle on HISD 2026-27 calendar drafts.
Salons: Google's Reserve with Google partner page (Booksy, Fresha, Square Appointments listed; Vagaro not listed when
checked Nov 2026); Google Business Profile bookings help (providers may charge); Square help article 6567 (owner or
tenant only, booth renters don't qualify, no prepayment); Fresha Reserve with Google help (name/address match) and
pricing ($19.95 / $14.95 per member, 20% new client fee, $6 minimum); Booksy US pricing ($29.99, $20 per added user,
Boost 30% of first visit); 16 TAC 83.70(e)-(f) license posting and photo; TDLR's ten most common establishment
violations (83.71(c) renter list, 83.71(l) inspection notice); TDLR mini-establishment FAQ; Texas Occupations Code
1603.208 (remote service disclosures).
Competitor/PAA phrasing read for "martial arts marketing", "how to get more students martial arts school",
"karate school advertising", "tutoring center marketing", "how to get more tutoring clients", "tutoring google ads",
"salon marketing ideas", "how to get more clients at a barbershop", "how to fill slow days at a salon".
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # martial arts post
    "meta_teen": A("https://about.fb.com/news/2023/01/age-appropriate-ads-for-teens/", "Meta’s announcement"),
    "linear": A("https://lineardesign.com/blog/facebook-detailed-targeting-list-2024/", "Linear Design’s running list of Meta targeting changes"),
    "hrc": A("https://statutes.capitol.texas.gov/Docs/HR/htm/HR.42.htm#42.041", "Texas Human Resources Code § 42.041(b)(18)"),
    "hhs_ex": A("https://fhb.hhs.texas.gov/node/310056", "Texas HHS Child Care Regulation’s handbook"),
    "camps": A("https://www.click2houston.com/news/local/2026/05/12/only-18-texas-youth-camps-fully-licensed-weeks-before-summer-but-many-can-still-legally-operate/", "KPRC"),
    "aspen": A("https://projectplay.org/state-of-play-2025", "the Aspen Institute’s Project Play"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy"),
    "ppcl": A("https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/", "PPC Land"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    "cisd": A("https://myneighborhoodnews.com/conroe-isd-approves-2026-2027-school-calendar-heres-whats-new-compared-to-2025-2026", "Conroe ISD’s approved 2026-27 calendar"),
    "cfisd": A("https://communityimpact.com/houston/cypress/education/2025/11/12/cy-fair-isd-students-staff-to-get-fall-break-in-2026", "Cy-Fair ISD’s"),
    # tutoring post
    "tea_cal": A("https://tea.texas.gov/student-assessment/test-administration/2026-2027-testing-calendar.pdf", "TEA’s 2026-2027 testing calendar"),
    "hb8": A("https://www.tpr.org/education/2025-09-18/texas-is-officially-replacing-staar-here-is-what-schools-new-standardized-tests-will-look-like", "Texas Public Radio"),
    "sat": A("https://satsuite.collegeboard.org/sat/dates-deadlines", "College Board’s SAT calendar"),
    "act": A("https://www.act.org/content/act/en/products-and-services/the-act/registration.html", "ACT’s registration page"),
    "hisd": A("https://www.houstonchronicle.com/news/houston-texas/education/hisd/article/academic-calendar-2026-27-year-21245830.php", "the Houston Chronicle"),
    "tefa": A("https://educationfreedom.texas.gov/", "the program’s official site"),
    "tefa_vendor": A("https://educationfreedom.texas.gov/providers-vendors/", "providers and vendors page"),
    "tefa_mar": A("https://comptroller.texas.gov/about/media-center/news/20260316-texas-education-freedom-accounts-reach-200000-student-applications-ahead-of-tomorrows-deadline-1773676264632", "the Comptroller’s March 2026 release"),
    "tefa_nov": A("https://comptroller.texas.gov/about/media-center/news/20251125-acting-texas-comptroller-kelly-hancock-announces-final-rules-and-key-dates-for-texas-education-freedom-accounts-program-1764103747312", "final program rules"),
    "sb2": A("https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00002F.htm", "the enrolled text of SB 2"),
    "ftc_rule": A("https://www.morganlewis.com/pubs/2024/08/ftc-issues-final-rule-on-consumer-reviews-and-testimonials", "Morgan Lewis’s summary of the FTC’s reviews rule"),
    "ftc_end": A("https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking", "FTC’s Endorsement Guides FAQ"),
    # salon post
    "rwg": A("https://www.google.com/maps/reserve/partners", "Google’s Reserve with Google partner page"),
    "gbp_book": A("https://support.google.com/business/answer/7475773?hl=en", "Google’s own bookings help page"),
    "sq_rwg": A("https://squareup.com/help/us/en/article/6567-reserve-with-google", "Square’s help article"),
    "fresha_rwg": A("https://www.fresha.com/help-center/knowledge-base/online-presence/101349-get-booked-on-reserve-with-google", "Fresha’s setup guide"),
    "fresha_price": A("https://www.fresha.com/pricing", "Fresha’s pricing page"),
    "booksy_price": A("https://biz.booksy.com/en-us/pricing-plans", "Booksy’s U.S. pricing page"),
    "tac8370": A("https://regulations.justia.com/states/texas/title-16/part-4/chapter-83/section-83-70", "16 Tex. Admin. Code § 83.70"),
    "tdlr_top": A("https://www.tdlr.texas.gov/barbering-and-cosmetology/establishments/most-common-violations.htm", "TDLR’s list of the ten most common establishment violations"),
    "tdlr_mini": A("https://www.tdlr.texas.gov/barbering-and-cosmetology/establishments/mini-faq.htm", "TDLR’s mini-establishment FAQ"),
    "occ1603": A("https://texas.public.law/statutes/tex._occ._code_section_1603.208", "Texas Occupations Code § 1603.208"),
}

MARTIAL = "/blog/martial-arts-studio-marketing-the-woodlands-houston/"
TUTOR = "/blog/tutoring-center-marketing-houston/"
SALON = "/blog/hair-salon-barbershop-marketing-the-woodlands-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: martial arts
    {
        "slug": "martial-arts-studio-marketing-the-woodlands-houston",
        "title": "Martial Arts Studio Marketing in The Woodlands and Houston: Filling Kids Classes",
        "seo_title": "Martial Arts Studio Marketing in The Woodlands & Houston",
        "desc": "Martial arts studio marketing for The Woodlands and Houston: kids trial offers, Meta ads aimed at parents, Google Maps, reviews, belt tests and retention.",
        "category": "Local marketing",
        "icons": ["Meta", "Google Business Profile", "Instagram"],
        "art": "b4",
        "hero": "fitness",
        "hero_alt": "Illustration of a fitness motif for martial arts studio marketing in The Woodlands, Spring and Houston",
        "related": ["gym-fitness-studio-marketing-the-woodlands-houston", "daycare-marketing-houston-the-woodlands", "back-to-school-marketing-woodlands"],
        "sections": [
            (None, f"""<p>Tuesday, 5:10 p.m. The after-school van is back from two elementary schools in Spring, and fourteen kids in white uniforms are lining up for the Little Dragons class. The lobby is full of parents on their phones. The front desk line rings twice and nobody picks up, because the one person at the desk is tying a six-year-old’s belt. Somewhere in a CRM there’s a Facebook lead from yesterday afternoon that nobody has called yet.</p>
<p>Most martial arts studios in Houston don’t have a traffic problem. They have a desk problem, an offer problem and a retention problem, roughly in that order.</p>
<p>The short version: to get more students at a martial arts school in The Woodlands or Houston, sell the kids program to parents, because they’re the ones paying. Use a simple trial offer that books into real class times online. Run Meta ads aimed at adults (Meta won’t let you target the kids anyway) and win the Google Maps results within a 10 to 15 minute drive. Push hardest in August and January. Then keep students through belt tests and events, since a student who stays two years is worth far more than any lead you’ll buy.</p>
<p>This guide is written for independent karate, taekwondo, jiu-jitsu and mixed-style schools with one or two locations.</p>"""),

            ("The kids program is the business, and parents are the buyer", f"""<p>In most suburban schools we look at, kids and teens make up the majority of active memberships. Adult classes matter for culture and for the instructors’ sanity, but the rent in Shenandoah or Katy gets paid by the 5-to-12-year-olds.</p>
<p>That changes who you’re marketing to. A parent isn’t buying “martial arts.” They’re buying one of a few outcomes:</p>
<ul>
<li><b>Focus and confidence.</b> The kid who won’t make eye contact, or who melts down at homework.</li>
<li><b>Safety and anti-bullying.</b> A real worry, and one that spikes in the first month of school.</li>
<li><b>Activity that isn’t a team sport.</b> Plenty of kids don’t love soccer or baseball and their parents want something structured anyway.</li>
<li><b>Logistics.</b> Classes at 4:30 or 5:15, close to home, with pickup from school if you offer it.</li>
</ul>
<p>Cost sits under all of it. {SRC['aspen']} reported in its State of Play 2025 that youth sports costs have risen 46% since 2019. Parents comparing your monthly tuition to rec league soccer will notice. So your marketing has to show what the monthly fee buys: structure, small classes, a clear belt path, and instructors who know their kid’s name.</p>
<p>Write every page and ad for the parent, who reads it at 9 p.m. on a phone after the kids are in bed.</p>"""),

            ("Back-to-school and New Year: the two enrollment peaks", f"""<p>Martial arts enrollment in Houston follows the school year. In the accounts and studios we’ve seen, two windows produce a big share of the year’s new students, and a couple of smaller bumps fill in around them.</p>
<!--fig:season-->
<p><b>Back-to-school.</b> {SRC['cisd']} has students starting Wednesday, August 12, 2026, and {SRC['cfisd']} calendar uses the same start date, with a new week-long fall break October 12 to 16. Parents start planning fall activities in late July, so that’s when the campaigns should start. The real decisions happen in the two weeks after school starts, once the family’s schedule settles and parents see whether their child has a free afternoon.</p>
<p><b>New Year.</b> January is the second peak. Parents set goals for their kids too, and adults sign themselves up. Start ads the week after Christmas, not January 15.</p>
<p><b>Smaller bumps.</b> Spring break (March 15 to 19 in both Conroe and Cy-Fair this school year) is a good time for a camp or a “bring a friend” week. Summer camp sells in March and April.</p>
<p>Plan your budget around this calendar instead of spending the same amount every month. We go deeper on the school calendar in our {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing guide')}.</p>"""),

            ("Trial class offers that turn into enrollments", f"""<p>Every school runs some version of a trial. The difference between a trial that fills classes and one that fills the mat with no-shows is mostly in the details.</p>
<p>The common options:</p>
<ul>
<li><b>One free trial class.</b> Easy to sell, high no-show rate, and you’re selling the membership at the end of a single 30-minute class.</li>
<li><b>Paid intro program.</b> Something like two weeks of classes plus a uniform for a set fee. Fewer leads, more show-ups, and the family has already paid you once. In the studios we’ve talked to, paid intros usually convert to memberships at a higher rate than free classes.</li>
</ul>
<p>Whatever you choose, the trial needs three things to work:</p>
<ol>
<li><b>A real booking page.</b> Show the next available class times by age group and let the parent pick one. “Fill out this form and we’ll reach out” loses half the people who were ready that night.</li>
<li><b>A reminder sequence.</b> Text the day before and two hours before, with the address, where to park, what to wear and how early to arrive.</li>
<li><b>A planned conversation after class.</b> The instructor gives the parent two minutes of specific feedback about their child (“she listened well, we’ll work on her stance”), then the desk walks through the options. Don’t let the parent leave with “we’ll think about it” and no next step booked.</li>
</ol>
<p>And answer the phone, or call back within minutes. A parent who filled out a form at 8:45 p.m. is often calling the next studio at 9 the next morning. Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')} covers how to set that up without hiring another person.</p>"""),

            ("Meta ads for martial arts: target the parent, never the kid", f"""<p>Facebook and Instagram are usually the biggest lead source for a kids program, and the rules shape everything.</p>
<p>Start with minors. According to {SRC['meta_teen']}, since February 2023 advertisers can only use age and location to reach teens, gender is gone as a teen targeting option, and teens’ activity on Meta’s apps no longer shapes the ads they see. Interest targeting for teens was removed even earlier. Your teen program can still advertise, but the ad has to reach the parent or the teen through broad age and location only.</p>
<p>For parents, the targeting toolbox keeps shrinking. Meta has removed or merged detailed targeting options several times since 2022, including a round of consolidation announced in June 2025, and it removed detailed targeting exclusions from Ads Manager in 2025, per {SRC['linear']}. Parent-related demographic options still show up in many accounts. Check what’s actually there before you build a plan around it.</p>
<p>In practice we’d run it like this:</p>
<ul>
<li>Adults 25 to 54, a radius of roughly 5 to 10 miles around the studio (tighter inside the Loop, wider out toward Magnolia or Montgomery), and either broad targeting or a light parent layer if your account still has it.</li>
<li>Let the creative do the sorting. “Kids karate in Kingwood, ages 5 to 12, classes at 4:30 and 5:15” finds parents because everyone else scrolls past.</li>
<li>Use real video from your mat. A 20-second clip of a class with the instructor explaining what kids learn in week one beats any stock footage.</li>
<li>Retarget website visitors and video viewers with the trial offer and a few short testimonials from parents.</li>
</ul>
<p>Sample ad copy:</p>
<p><i>“Looking for an after-school activity that builds focus? Our Little Ninjas program in The Woodlands is for ages 4 to 6, 30 minutes, twice a week. Two-week intro with a free uniform. Pick a class time online.”</i></p>
<p>One rule we hold firm on: never post a child’s face in an ad or on social media without written permission from a parent. Keep a photo release on file for every student, and keep a “no photos” list at the desk so instructors know whom to keep out of frame.</p>
<p>If your Meta leads look like junk, our {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'guide to fixing bad Facebook leads')} walks through form settings that cut the noise.</p>"""),

            ("Google Business Profile and search ads", f"""<p>Parents who search are further along than parents who scroll past an ad. “Karate for kids near me,” “taekwondo The Woodlands,” “kids jiu jitsu Cypress” and “martial arts classes Katy” are people who have already decided on the activity and are now choosing a school.</p>
<p><b>Business Profile.</b> Use Martial arts school as the primary category unless you really are a single-style school, then add the style-specific categories Google offers that match what you teach. Add each program under Services with ages and class length. Upload photos of the mat, the lobby, the parking lot and the front door, and video of a real class. Put your class schedule in the business description and keep holiday hours current. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers the ranking side in full.</p>
<p><b>Search ads.</b> A small, tight campaign usually does the job:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Kids classes</td><td>kids karate near me, martial arts for kids Spring TX, taekwondo for kids</td><td>Kids program page with ages and times</td></tr>
<tr><td>Teens and adults</td><td>adult jiu jitsu The Woodlands, kickboxing classes Conroe</td><td>Adult program page</td></tr>
<tr><td>After-school</td><td>after school martial arts pickup, karate after school program</td><td>Pickup program page with school list</td></tr>
<tr><td>Brand</td><td>your studio name, your instructor’s name</td><td>Homepage or trial page</td></tr>
</tbody></table></div>
<p>Negatives to add on day one: jobs, hiring, instructor certification, black belt online, UFC, MMA fights, tickets, gear, gi, sparring gloves, Amazon, YouTube, how to, video, belt order, belt colors, free online classes. Check the search terms weekly at first.</p>
<p>Click costs vary a lot by area. Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} give a sense of the range, and our {L('/services/search-marketing/', 'search marketing team')} can set it up if you’d rather not.</p>"""),

            ("Reviews from parents, inside Google’s rules", f"""<p>Parents trust other parents, and a studio with 180 detailed reviews wins the map pack and the phone call.</p>
<p>The rules, per {SRC['gpol']}: no incentives for reviews (no free week, no gear discount), no discouraging negative reviews, and no review gating where only happy families get the link. In April 2026 Google added language against having staff collect a set number of reviews or reviews with specific content, which can include asking families to name a particular instructor, per {SRC['ppcl']}. Drop any instructor review contests.</p>
<p>The best moments to ask are built into your calendar:</p>
<ul>
<li>Right after a belt test, when the family just took photos with the new belt.</li>
<li>At the end of the first month, when the parent has seen a change at home.</li>
<li>After a tournament, camp week or birthday party at the studio.</li>
</ul>
<p>A text script that works: <i>“Congrats to Mason on his yellow belt today! If you have a minute, a Google review helps other parents in Spring find us: [link]. Thank you for being part of the family.”</i> Send that to every family that tested, not just the ones you think loved it.</p>
<p>For templates and reply examples, see our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')}.</p>"""),

            ("After-school pickup programs: market them carefully", f"""<p>A pickup program can be the most profitable thing a studio does. A van loop through three or four elementary schools, two hours of classes and supervised time, and a monthly fee well above regular tuition. It also fills the 3 to 5 p.m. slot that’s otherwise dead.</p>
<p>It also carries a licensing question that affects your marketing copy. Texas exempts some programs from child care licensing. Under {SRC['hrc']}, a program that gives children direct instruction in a single skill can be exempt if it meets every condition: it offers no services unrelated to that skill, it doesn’t advertise or present itself as a child-care facility, day-care center or licensed before- or after-school program, it tells parents it isn’t licensed by the state and describes the physical risks of the activity, and it runs background checks on all employees and volunteers who work with children.</p>
<!--fig:exempt-->
<p>The marketing implications are direct. Words like “after-school care,” “child care” and “daycare” on your website, flyers or ads can work against the exemption. Adding homework time, snacks and general supervision may push you outside it. {SRC['hhs_ex']} notes that a program that doesn’t meet every requirement of the single-skill exemption may meet the definition of a school-age program, which is regulated under Chapter 744, and it lists separate exemption forms for school-year and summer single-skill programs.</p>
<p>We’re marketers, not lawyers. What we’d do: decide what your program actually is with your attorney or a call to Texas HHS Child Care Regulation, then write every page and ad to match. “After-school martial arts program with pickup from these schools” is a different claim from “after-school care.”</p>
<p>Summer camps have their own question. After the 2025 Hill Country floods, Texas passed new youth camp safety laws, and day camps are covered too, per {SRC['camps']}, which reported only 18 camps fully licensed weeks before summer 2026. Check with the Department of State Health Services before you advertise a summer camp.</p>
<p>If you do license as a child care operation, our {L('/blog/daycare-marketing-houston-the-woodlands/', 'daycare marketing guide')} covers the inspection-record and enrollment side.</p>"""),

            ("Retention: belt tests, events and the second year", f"""<p>Lead generation gets the attention, but retention decides whether a school grows. A kids program that loses students in month four is filling a leaky bucket.</p>
<p>What keeps families, in the schools we’ve seen do it well:</p>
<ul>
<li><b>Visible progress.</b> A clear belt path with stripes in between, so a six-year-old earns something every few weeks. Post the curriculum and testing schedule for parents.</li>
<li><b>Belt testing as an event.</b> Invite grandparents, take photos at a branded backdrop, and send the family a photo and a short video that evening. This is your best social content and your best review moment.</li>
<li><b>Buddy weeks.</b> Students bring a friend to class for a week, twice a year. Referrals from current families convert better than any ad.</li>
<li><b>Birthday parties and parents’ night out.</b> Both bring non-students onto the mat.</li>
<li><b>Attendance alerts.</b> When a student misses two weeks in a row, the instructor calls. Most cancellations start as quiet absences.</li>
</ul>
<p>Texting is how most of this reaches parents, so get consent right. Class reminders are different from promotional texts. Get clear opt-in for marketing messages and keep the record. Texas brought marketing texts under its telephone solicitation law through SB 140, effective September 1, 2025, with some exemptions for current customers and businesses that sell from a physical location, per {SRC['sb140']}. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} covers the details.</p>"""),

            ("Cost per enrolled student: the number that matters", f"""<p>Cost per lead is the number ad platforms show you. Cost per enrolled student is the number that runs your business. Track every step:</p>
<!--fig:funnel-->
<p>Below is an illustrative month for a single-location school spending on Meta and Google. The numbers are an example, not a benchmark.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Step</th><th>Count</th><th>Cost per step</th></tr></thead>
<tbody>
<tr><td>Ad spend</td><td>$2,500</td><td></td></tr>
<tr><td>Leads (forms, calls, messages)</td><td>100</td><td>$25 per lead</td></tr>
<tr><td>Trials booked</td><td>45</td><td>$56 per booking</td></tr>
<tr><td>Trials attended</td><td>30</td><td>$83 per show</td></tr>
<tr><td>Enrolled</td><td>15</td><td>$167 per student</td></tr>
</tbody></table></div>
<p>Now the other side. If tuition is $159 a month and the average kid stays 14 months, each student is worth about $2,226 in tuition before testing fees and gear. Against that, $167 to enroll a student is a good trade. Even $300 can be.</p>
<!--fig:value-->
<p>Two consequences. First, the biggest gains usually come from the middle of the funnel: booking more of your leads and getting more of your bookings to show up. A school that moves show rate from 50% to 70% gets 40% more students from the same ad spend. Second, retention changes what you can afford. Add three months to average student tenure and you can outbid every studio in the area for the same parents.</p>
<p>Count enrollments by source in your studio software and tie them back to ad platforms where you can. Our post on {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking forms and calls')} explains the setup.</p>"""),

            ("Mistakes we see at martial arts schools", f"""<ul>
<li><b>Pricing hidden behind a phone call.</b> You don’t have to publish everything, but parents want a ballpark. “Programs start at $X a month” keeps more of them.</li>
<li><b>Ads with no schedule.</b> If a parent can’t tell whether there’s a class at a time that works, they move on.</li>
<li><b>One page for every program.</b> A four-year-old’s parent and a 35-year-old wanting jiu-jitsu need different pages.</li>
<li><b>Nobody owns the follow-up.</b> If leads go into an inbox that three people check “when they can,” the ads aren’t the problem.</li>
</ul>"""),

            ("A first 90 days for a studio starting fresh", f"""<ol>
<li><b>Days 1 to 30:</b> fix the Business Profile, build a page per program with ages, times and the trial offer, add online trial booking, set up text reminders and a photo release process, and start asking for reviews after every belt test.</li>
<li><b>Days 31 to 60:</b> launch Meta ads to parents with real class video and a Google Search campaign on kids and style keywords. Track leads, bookings, shows and enrollments by source.</li>
<li><b>Days 61 to 90:</b> fix whichever funnel step is weakest, run a buddy week, and plan budget for the next peak, whether that’s August or January.</li>
</ol>
<p>If you’d like a second opinion on any of this, tell us about your school and your goals and a senior strategist will put together a plan built around your schedule and your market. You can <a href="/contact/">get in touch</a> here. Our {L('/services/paid-social-advertising/', 'paid social team')} runs the Meta side for local businesses across Greater Houston.</p>"""),
        ],
        "faq": [
            ("How do I get more students for my martial arts school?",
             "Market the kids program to parents, since they make the decision. Offer a simple trial that books into real class times online, call leads back within minutes, and run Facebook and Instagram ads to adults within a few miles of the studio. Win Google Maps for searches like kids karate near me, ask every belt-test family for a review, and push hardest in August and January."),
            ("Can I target kids or teens with Facebook ads for my martial arts studio?",
             "Only in a very limited way. Since February 2023 Meta lets advertisers reach teens under 18 only by age and location, with no gender or interest targeting. Most studios get better results aiming ads at parents, usually adults 25 to 54 near the studio, with creative that names the age group, class times and neighborhood. Never use a child's photo without written parent permission."),
            ("Is a free trial class or a paid intro offer better for a martial arts school?",
             "It depends on your follow-up, but paid intro programs usually produce fewer leads and better show rates, because the family has already committed a small amount. A free class is easier to sell and fills the calendar but brings more no-shows. Whichever you choose, use online booking, text reminders, and a planned conversation with the parent right after the class."),
            ("Does a martial arts after-school pickup program need a child care license in Texas?",
             "It can. Texas exempts single-skill programs only if they meet every condition, including offering no unrelated services, not advertising as child care or an after-school program, notifying parents the program is unlicensed, and running background checks. Adding homework time or general supervision may make it a regulated school-age program. Confirm with Texas HHS Child Care Regulation or an attorney, then write your marketing to match."),
            ("What is a good cost per enrolled student for a martial arts school?",
             "There is no universal benchmark, so work it out from your own numbers. Multiply monthly tuition by how many months the average student stays to get student value, then decide what share you can spend to acquire one. A studio charging $159 a month with 14-month average tenure can comfortably spend a few hundred dollars per enrollment. Improving show rates and retention lowers the cost fastest."),
        ],
        "figures": {
            "season": {
                "type": "columns",
                "title": "When Houston families sign up for martial arts",
                "sub": "Relative new-student demand by month",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [88, 60, 55, 45, 30, 40, 55, 95, 80, 50, 35, 25],
                "highlight": [0, 7, 8],
                "y_label": "Demand",
                "note": "Illustrative example based on patterns we have seen, not measured data",
                "alt": "Column chart of seasonal martial arts enrollment demand for studios in The Woodlands and Houston, peaking in August and January",
                "caption": "Back-to-school and New Year carry the year. Budget for them before they arrive.",
            },
            "exempt": {
                "type": "checklist",
                "title": "Texas single-skill exemption: every box must be checked",
                "sub": "Human Resources Code § 42.041(b)(18), paraphrased",
                "items": ["Direct instruction in one skill, like martial arts", "No services unrelated to that skill", "Not advertised as child care, day care or a licensed after-school program", "Parents told the program isn't state-licensed", "Parents told about the physical risks", "DPS background checks on staff and volunteers"],
                "alt": "Checklist of Texas single-skill child care licensing exemption conditions for martial arts after-school programs in Houston and The Woodlands",
                "caption": f"Paraphrased from {SRC['hrc']}. Confirm your program with Texas HHS or an attorney.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From ad click to enrolled student",
                "stages": [["Leads", "100"], ["Trials booked", "45"], ["Trials attended", "30"], ["Enrolled", "15"]],
                "note": "Illustrative example",
                "alt": "Funnel of leads to enrolled students for a martial arts studio in The Woodlands and Houston",
                "caption": "Most of the upside is in the middle: booking more leads and getting more of them to show.",
            },
            "value": {
                "type": "bars",
                "title": "What a student is worth vs. what one costs",
                "sub": "One student at $159 a month, by months enrolled",
                "items": [["3 months", 477, "$477"], ["6 months", 954, "$954"], ["14 months", 2226, "$2,226"], ["24 months", 3816, "$3,816"], ["Cost to enroll (example)", 167, "$167"]],
                "highlight": [2],
                "note": "Illustrative example. Tuition only, before testing fees and gear",
                "alt": "Bar chart comparing martial arts student lifetime tuition value with cost per enrolled student for a Houston area studio",
                "caption": "Retention changes how much you can afford to spend on every new student.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: tutoring
    {
        "slug": "tutoring-center-marketing-houston",
        "title": "Tutoring Center Marketing in Houston: Getting More Students Through the School Year",
        "seo_title": "Tutoring Center Marketing in Houston: More Students",
        "desc": "Tutoring center marketing in Houston: STAAR, SAT and ACT seasons, district calendars, Google Ads keywords, assessments, honest results claims and TEFA.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google", "Google Analytics"],
        "art": "b3",
        "hero": "growth",
        "hero_alt": "Illustration of a growth chart for tutoring and learning center marketing in Houston, Katy and The Woodlands",
        "related": ["back-to-school-marketing-woodlands", "fake-reviews-rule-local-businesses", "google-ads-cost-per-click-houston-benchmarks"],
        "sections": [
            (None, f"""<p>It’s 9:40 on a Tuesday night in late September. A mom in Cypress has just opened her eighth grader’s first progress report and found a 68 in math. She types “math tutor near me” into Google, opens four tabs, and fills out the form on the one site that tells her what happens next and roughly what it costs. The other three never hear from her.</p>
<p>That search, and what your center does in the 24 hours after it, is most of tutoring center marketing.</p>
<p>To get more tutoring students in Houston, plan your marketing around the school and testing calendar instead of spreading it evenly across the year. Run Google Ads on the specific phrases parents type, with a landing page for each subject and test. Make a diagnostic assessment the main conversion and follow up fast. Ask for reviews honestly, keep results claims you can back up, and get ready for the state’s new education savings accounts if your tutors qualify.</p>
<p>This guide is for independent learning centers and franchise owners across Greater Houston, from Katy and Cypress to The Woodlands, Pearland and inside the Loop.</p>"""),

            ("Your demand calendar is the school calendar", f"""<p>Tutoring demand moves with report cards and test dates. This is the 2026-27 calendar that matters for Houston-area centers:</p>
<div class="bp-tbl"><table>
<thead><tr><th>When</th><th>What happens</th><th>What parents search</th></tr></thead>
<tbody>
<tr><td>Late July to mid-August</td><td>Conroe ISD and Cy-Fair ISD start August 12; HISD’s drafts start the week of August 10</td><td>“tutoring for school year,” “reading tutor before school starts”</td></tr>
<tr><td>Late September to October</td><td>First progress reports and report cards</td><td>“math tutor near me,” “algebra 1 tutor Katy”</td></tr>
<tr><td>October to December</td><td>SAT dates Oct 3, Nov 7 and Dec 5; ACT Dec 12</td><td>“SAT prep The Woodlands,” “ACT tutor near me”</td></tr>
<tr><td>December 1 to 11</td><td>STAAR end-of-course retests</td><td>“algebra 1 EOC retest help”</td></tr>
<tr><td>January to March</td><td>Spring semester push; SAT March 6, ACT Feb 27</td><td>“STAAR tutoring,” “reading tutor 3rd grade”</td></tr>
<tr><td>April 6 to 30</td><td>STAAR spring windows: reading first, then science and social studies, then math</td><td>“STAAR prep near me”</td></tr>
<tr><td>June to July</td><td>June 15 to 25 EOC retests; SAT May 1 and June 5; summer programs</td><td>“summer tutoring,” “summer reading program”</td></tr>
</tbody></table></div>
<p>The STAAR windows come from {SRC['tea_cal']}, the SAT dates from {SRC['sat']}, and the ACT dates from {SRC['act']}. District start dates are from {SRC['cisd']}, {SRC['cfisd']} calendar, and {SRC['hisd']}’s report on HISD’s draft options. Katy ISD’s approved calendar has full-week Thanksgiving and spring breaks and a two-week winter break; check the district site for exact dates.</p>
<!--fig:calendar-->
<p>One big change is coming. Under House Bill 8, signed in September 2025, STAAR will be replaced starting in the 2027-28 school year by three shorter tests given at the beginning, middle and end of the year, with results back in about two days, per {SRC['hb8']}. That shifts tutoring demand. Instead of one spring panic, parents will get three score reports a year, each one a reason to call you. Start building pages and campaigns around “beginning of year test” results now, and keep STAAR pages up through spring 2027.</p>"""),

            ("What parents actually type into Google", f"""<p>Parents describe a problem, a subject, a grade or a test. Rarely the word “learning center.” Build ad groups and pages around those four patterns.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Intent</th><th>Example keywords</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Subject and grade</td><td>math tutor for 5th grader, algebra 2 tutor near me, chemistry tutor Katy</td><td>Subject page with grade bands and tutor bios</td></tr>
<tr><td>Test prep</td><td>SAT prep The Woodlands, ACT tutoring Cypress, PSAT prep</td><td>Test prep page with upcoming dates and course start dates</td></tr>
<tr><td>State tests</td><td>STAAR tutoring Houston, algebra 1 EOC tutor</td><td>STAAR page, updated each year</td></tr>
<tr><td>Reading and skills</td><td>reading tutor near me, tutoring for kids behind in reading, study skills tutor</td><td>Reading program page</td></tr>
<tr><td>Location</td><td>tutoring center Sugar Land, tutors in Pearland, learning center Kingwood</td><td>Location page with map, hours, parking</td></tr>
</tbody></table></div>
<p>Negatives matter in this category, because a lot of tutoring searches come from tutors looking for work and students looking for free answers. Start with: jobs, hiring, become a tutor, tutor salary, tutoring jobs, volunteer, free, answers, answer key, worksheets, printable, Khan Academy, Quizlet, Chegg, homework answers, college tutoring (if you don’t offer it), and any university name. Read the search terms report weekly for the first month.</p>
<p>A few more settings: set location to “Presence: people in or regularly in your included locations,” keep the radius to the drive time parents will tolerate twice a week (usually 15 to 20 minutes in Houston traffic), and schedule ads heavier from 7 to 11 p.m., when parents sit down with the laptop. Click costs vary a lot by area and test season; our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} are a reasonable starting reference.</p>"""),

            ("The assessment is your conversion", f"""<p>Most tutoring centers sell through a diagnostic assessment followed by a parent conference. That’s the right model. Most centers just make the assessment hard to book.</p>
<p>What the assessment page needs:</p>
<ul>
<li>What it is and how long it takes (“a 45-minute skills check, then 20 minutes with the parent”).</li>
<li>What it costs, or that it’s free. Some centers charge a small fee and credit it toward enrollment, which tends to improve show rates.</li>
<li>Online booking with real time slots, including evenings and Saturdays.</li>
<li>What the parent gets: a written summary of strengths, gaps and a recommended plan.</li>
<li>A price range for ongoing programs. Parents who can’t find any number assume it’s expensive and keep shopping.</li>
</ul>
<p>Then measure it like a funnel: leads, assessments booked, assessments completed, enrolled. If plenty of parents book and few show, fix reminders and the booking flow. If they show and don’t enroll, the parent conference is the problem, and that’s a sales training issue rather than a marketing one.</p>
<!--fig:funnel-->
<p>Speed matters more than most center directors think. A parent who filled out a form at 9:40 p.m. will often book wherever answers first the next morning. An automatic text within a minute (“Thanks, Maria. Here’s a link to pick an assessment time, or reply with a good time to call”) catches a lot of them. Our post on {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')} covers the setup, and our guide to {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking forms and calls')} shows how to send booked assessments back to Google Ads as conversions.</p>"""),

            ("Reviews and results claims: keep them honest", f"""<p>Tutoring is sold on outcomes, which makes it easy to cross a line.</p>
<p><b>Reviews.</b> The FTC’s rule on consumer reviews and testimonials took effect October 21, 2024. It bans fake reviews, buying positive reviews, undisclosed insider reviews (staff or tutors’ relatives), review suppression, and incentives conditioned on a review expressing a particular sentiment, with civil penalties of up to $51,744 per violation, adjusted for inflation, per {SRC['ftc_rule']}. Google is stricter still and bans any incentive for a review on Maps, per {SRC['gpol']}. So no gift card for a review, ever, and no asking only the families whose kids improved.</p>
<p>The cleanest ask: at the end-of-term parent conference, after you’ve shown the progress report, send every family the same review link by text.</p>
<p><b>Results claims.</b> “Our students improve two letter grades” or “average SAT score increase of 150 points” are claims the FTC expects you to back up. The {SRC['ftc_end']} explains that when an endorsement shows exceptional results, an advertiser without proof that those results are typical must make clear what people can generally expect. A testimonial from the one student who jumped 300 points needs that context.</p>
<!--fig:claims-->
<p>What to do in practice:</p>
<ul>
<li>If you publish an average improvement, calculate it from every student in the program over a defined period, including the ones who didn’t improve, and say how you measured it.</li>
<li>Name the test and the time frame (“students who completed our 8-week SAT course in 2025-26, first official score vs. second”).</li>
<li>Skip “guaranteed” unless you offer a real, written guarantee with clear terms.</li>
<li>Get written permission from parents before using a student’s name, school, photo or scores.</li>
</ul>
<p>Our post on {L('/blog/fake-reviews-rule-local-businesses/', 'the FTC fake reviews rule')} goes deeper on what changed for local businesses.</p>"""),

            ("Franchise vs. independent: who controls what", f"""<p>The big national tutoring and math-center brands have name recognition, national ad funds and polished curriculum marketing. Independent centers have flexibility and usually a founder who knows every family. Both can win locally, but they play different games.</p>
<p><b>If you own a franchise:</b></p>
<ul>
<li>Read your agreement for who owns the Google Business Profile, the local landing page, the Google Ads account and the call tracking numbers. In some systems corporate controls all of it; in others, owners run local ads within brand rules.</li>
<li>Find out what the national fund actually buys in Houston. Often it’s brand awareness plus a lead-routing system, and local search is still up to you.</li>
<li>Check territory rules before you set ad radiuses. Bidding into a neighboring franchisee’s ZIP codes causes problems.</li>
<li>Make your location page unique: your director, your tutors, your hours, your schools. Corporate templates that read identically across 40 locations don’t rank well for “tutoring near me.”</li>
</ul>
<p><b>If you’re independent:</b></p>
<ul>
<li>Lean into specifics a franchise can’t easily copy: certified teachers from local districts, small groups, flexible scheduling, and test prep tied to the high schools you serve.</li>
<li>Use your founder. A two-minute video of the director explaining how the assessment works converts better than any brand ad.</li>
<li>Build pages for each nearby school and district, like “Tutoring for Conroe ISD students near Oak Ridge High School,” with real content about the courses and tests those students face.</li>
</ul>
<p>Multi-location owners should read our guide to {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO')}.</p>"""),

            ("Texas Education Freedom Accounts: an opening for qualified tutors", f"""<p>Texas created Education Freedom Accounts through Senate Bill 2 in 2025, funded with $1 billion. For 2026-27, {SRC['tefa']} lists $10,474 for private school students, up to $30,000 for students with a disability and an IEP, and up to $2,000 for homeschooled and other students. More than 274,000 applications came in and over 100,000 awards had been made as of our check in November 2026. Tutoring is an allowed expense, per {SRC['tefa_mar']}.</p>
<p>That $2,000 bucket is the interesting part for tutoring centers. It covers homeschoolers and other participating students, and many of those families will spend some of it on tutoring and test prep.</p>
<!--fig:tefa-->
<p>Whether your center can take that money depends on approval. Under Section 29.358 of {SRC['sb2']}, a private tutor or teaching service has to show the comptroller that its tutors are current or retired educators at an accredited school, hold a relevant license or accreditation from a state, regional or national body, or have taught or tutored at a higher education provider. The provider also has to submit a national criminal history review (or authorize one), and the comptroller can only approve providers located in Texas or vendors registered to do business here. Section 29.359 lists tutoring fees and costs related to academic assessments among allowed expenses.</p>
<p>The program’s {SRC['tefa_vendor']} says vendor applications are accepted on a rolling basis through Odyssey, the program’s platform, and the Comptroller reviews each application and offering before it appears in the marketplace. The state issued its {SRC['tefa_nov']} in November 2025, and families receive funds in installments (July 1, October 1 and February 1 for private school students).</p>
<p>How we’d market it:</p>
<ul>
<li>Apply first. Don’t say “TEFA-approved” or “accepts Education Freedom Account funds” anywhere until the Comptroller has approved you.</li>
<li>Once approved, build a page explaining in plain English how a family uses their account with you, which programs qualify and what the $2,000 covers at your prices.</li>
<li>Target homeschool families directly: co-op groups, homeschool Facebook groups (as a member, following their rules), and Google Ads on “homeschool tutoring Houston” and “homeschool math tutor.”</li>
<li>Watch for the 2027-28 application window. The state hadn’t announced dates when we checked, and families can join an interest list on the program site.</li>
</ul>"""),

            ("What to spend, and what to track", f"""<p>An illustrative starting budget for a single-location independent center, before tutoring software:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Illustrative monthly range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Google Ads</td><td>$1,000 to $3,000</td><td>Heavier August to October and January to April</td></tr>
<tr><td>Meta ads to parents</td><td>$500 to $1,500</td><td>Summer programs, SAT course starts, retargeting</td></tr>
<tr><td>Local SEO and content</td><td>$500 to $1,500</td><td>Subject, test and school pages; Business Profile</td></tr>
<tr><td>Reviews and texting tools</td><td>$100 to $300</td><td>Review requests, reminders, follow-up</td></tr>
</tbody></table></div>
<p>These are examples, not quotes. The real test is cost per enrolled student, measured against what a typical student pays over their time with you. A family that enrolls in September and stays through STAAR in April is worth a lot more than a one-month SAT cram, so track both.</p>
<p>Track these weekly: leads by source, assessments booked and completed, enrollments, and average months enrolled. Without the last one you’ll overvalue cheap test-prep leads and undervalue the families who stay all year.</p>
<p>Two mistakes we see across education businesses. Ads pointing to a homepage that lists eight programs, and pricing hidden until the parent conference. Fix those two before you raise the budget.</p>
<p>If you want help building this around your calendar, tell us about your center and your goals and a senior strategist will put together a custom plan. <a href="/contact/">Get in touch</a>. Our {L('/services/search-marketing/', 'search marketing team')} handles Google Ads and SEO for local businesses across Greater Houston.</p>"""),
        ],
        "faq": [
            ("How do I get more students for my tutoring center?",
             "Plan around the school calendar. Advertise hardest in August, after the first report cards in fall, before STAAR in spring, and ahead of SAT and ACT dates. Run Google Ads on specific searches like algebra tutor near me or SAT prep plus your town, send each to its own page, make a diagnostic assessment easy to book online, and follow up within minutes. Then ask every family for a review."),
            ("What keywords should a tutoring center bid on in Google Ads?",
             "Bid on subject and grade phrases such as math tutor for 5th grader, test prep phrases like SAT prep The Woodlands, state test phrases like STAAR tutoring Houston, and location phrases like tutoring center Katy. Add negatives for tutoring jobs, become a tutor, free answers, worksheets and homework help sites, because many tutoring searches come from job seekers and students looking for free help."),
            ("Can tutoring centers accept Texas Education Freedom Account funds?",
             "Tutoring is an allowed expense, but a provider must be approved by the Texas Comptroller first. Under SB 2, tutors must be current or retired educators at an accredited school, hold a relevant license or accreditation, or have taught at a higher education provider, and the provider must complete a national criminal history review. Vendor applications are accepted on a rolling basis through the program's platform."),
            ("Is STAAR going away in Texas?",
             "Yes, on a timeline. House Bill 8, signed in September 2025, replaces STAAR starting in the 2027-28 school year with three shorter tests given at the beginning, middle and end of the year, with results back in about two days. STAAR still runs in 2026-27, with end-of-course tests in December and June and spring testing windows in April 2027."),
            ("Can I advertise average score improvements for my tutoring program?",
             "You can if you can prove them. The FTC expects advertisers to substantiate results claims, and testimonials showing exceptional results need context about what students generally achieve. Calculate any average from every student in a defined program and period, name the test and time frame, avoid the word guaranteed unless you offer a written guarantee, and get parent permission before using a student's name or scores."),
        ],
        "figures": {
            "calendar": {
                "type": "steps",
                "title": "The 2026-27 tutoring calendar in Houston",
                "sub": "When parents start searching",
                "steps": [["August", "School starts Aug 10-12 across Houston-area districts."], ["Fall", "Report cards, SAT Oct-Dec, ACT Dec 12."], ["December", "STAAR EOC retests Dec 1-11."], ["Spring", "STAAR windows April 6-30, SAT March and May."], ["Summer", "EOC retests June 15-25, summer programs."]],
                "alt": "Timeline of the 2026-27 tutoring demand calendar for Houston, Katy, Cypress and The Woodlands tutoring centers",
                "caption": f"Dates from {SRC['tea_cal']}, {SRC['sat']} and district calendars.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From search to enrolled student",
                "stages": [["Leads", "80"], ["Assessments booked", "40"], ["Assessments completed", "28"], ["Enrolled", "14"]],
                "note": "Illustrative example",
                "alt": "Funnel of tutoring center leads to assessments and enrollments for a learning center in Houston",
                "caption": "Measure every step. The fix is different at each one.",
            },
            "claims": {
                "type": "compare",
                "title": "Results claims: risky vs. defensible",
                "left": {"title": "Risky", "items": ["Guaranteed A's", "Raise your SAT score 300 points", "Our students always pass STAAR", "One star student shown as typical", "Gift card for a 5-star review"]},
                "right": {"title": "Defensible", "items": ["Written plan after a skills assessment", "Average gain, all 2025-26 course students, measured how", "Pass rates with the group, year and test named", "Typical results stated beside standout stories", "Same review link sent to every family"]},
                "alt": "Comparison of risky and defensible tutoring results claims under FTC rules for Houston tutoring centers",
                "caption": "If you can't show the math behind a claim, rewrite it.",
            },
            "tefa": {
                "type": "stats",
                "title": "Texas Education Freedom Accounts, 2026-27",
                "stats": [["$1B", "first-year program funding"], ["274,000+", "applications received"], ["$2,000", "for homeschool and other students"], ["$10,474", "for private school students"]],
                "note": "Source: EducationFreedom.Texas.gov, checked November 2026",
                "alt": "Stats on Texas Education Freedom Accounts funding and applications relevant to tutoring centers in Houston",
                "caption": f"From {SRC['tefa']}. Students with a disability and an IEP can receive up to $30,000.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: salons and barbershops
    {
        "slug": "hair-salon-barbershop-marketing-the-woodlands-houston",
        "title": "Hair Salon and Barbershop Marketing in The Woodlands and Houston: Booked Chairs, Fewer Discount Hunters",
        "seo_title": "Hair Salon & Barbershop Marketing: The Woodlands, Houston",
        "desc": "Hair salon and barbershop marketing in The Woodlands and Houston: booking apps, Reserve with Google, Instagram, rebooking, TDLR rules and slow weekdays.",
        "category": "Local marketing",
        "icons": ["Instagram", "Google Business Profile", "Facebook"],
        "art": "b2",
        "hero": "beauty",
        "hero_alt": "Illustration of a beauty motif for hair salon and barbershop marketing in The Woodlands, Spring and Houston",
        "related": ["how-to-get-more-lash-clients-the-woodlands-houston", "esthetician-marketing-ideas-houston-the-woodlands", "complete-guide-google-reviews"],
        "sections": [
            (None, f"""<p>Tuesday, 11 a.m., at a six-chair salon off Research Forest. Two stylists are working. Two are on their phones. One is folding towels for the second time. Saturday is booked solid through December, with a waitlist. Last month the owner posted “20% off for new clients” on Instagram, got nine new faces, and as far as anyone can tell, one of them came back.</p>
<p>Barbershops have the same week with different music. Friday after 3 p.m. and Saturday morning are packed. Tuesday at 10 is a barber watching highlights on his phone.</p>
<p>Most salon and barbershop marketing advice is about getting more new clients. The shops that make money spend most of their effort on three other things: being bookable the moment someone searches, getting first-time clients to rebook before they leave, and filling the weekday hours without training people to wait for a coupon.</p>
<p>Below is how we’d set that up for a salon or barbershop in The Woodlands, Spring, Conroe, Katy, Cypress or anywhere in Houston.</p>"""),

            ("Pick your booking platform with marketing in mind", f"""<p>Your booking app is now part of your marketing. It decides whether people can book from Google, how reminders and rebooking work, and in some cases how much you pay for a new client.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform</th><th>What it costs (as published)</th><th>Marketplace or new-client fee</th><th>Reserve with Google</th></tr></thead>
<tbody>
<tr><td>Square Appointments</td><td>Free, Plus and Premium plans; check current pricing</td><td>Check current terms</td><td>Yes, on all three plans, for the business owner or tenant</td></tr>
<tr><td>Booksy</td><td>$29.99 a month, plus $20 per additional user</td><td>Optional Boost: 30% of a new client’s first visit</td><td>Listed as a Google partner</td></tr>
<tr><td>Fresha</td><td>$19.95 a month for one, $14.95 per team member</td><td>20% of a marketplace client’s first visit, $6 minimum</td><td>Yes, as an add-on</td></tr>
<tr><td>Vagaro</td><td>Check current plans</td><td>Check current terms</td><td>Not on Google’s partner page when we checked</td></tr>
</tbody></table></div>
<p>Pricing is from {SRC['booksy_price']} and {SRC['fresha_price']}, checked in November 2026; plans change, so confirm before you switch. Booksy’s page says Boost is off by default, and that you keep 100% of later visits from a Boost client. Fresha’s fee applies only to clients who find you through its marketplace, not to clients you send there yourself.</p>
<p>Our take: marketplace fees aren’t bad if the clients rebook. Paying 20% or 30% of one first visit for a client who comes back every five weeks for two years is cheap. Paying it for someone who never returns is not. Track marketplace clients separately and check their rebook rate after 90 days before you decide.</p>
<p>And don’t move platforms in November. Switching software right before the holiday rush is how salons lose a month of rebookings.</p>"""),

            ("Reserve with Google and the Book button", f"""<p>When someone searches “hair salon near me” or “barbershop Spring TX,” your Business Profile can show a Book button that lets them pick a service and time without leaving Google.</p>
<p>{SRC['rwg']} lists Booksy, Fresha and Square Appointments among its beauty partners, along with Mindbody and others. Vagaro wasn’t on that page when we checked in November 2026. If your software isn’t listed, you can still add your own booking link as the appointment link in your profile; you just won’t get the built-in booking flow or Google’s booking data.</p>
<p>The details that trip people up:</p>
<ul>
<li><b>Name and address must match.</b> Fresha requires your Business Profile name and address to match your Fresha details exactly, and your marketplace profile to be published, per {SRC['fresha_rwg']}.</li>
<li><b>Booth renters may be shut out.</b> {SRC['sq_rwg']} says only the owner or tenant of the physical location qualifies for Reserve with Google, and booth or room renters don’t. Bookings through Google also can’t require prepayment or no-show protection, and they’re automatically accepted.</li>
<li><b>Fees.</b> Google’s own help page warns that “your provider might charge you” for bookings through Google, per {SRC['gbp_book']}. Ask your platform.</li>
</ul>
<p>Beyond the button, fill in the profile like a menu. Primary category Hair salon or Barber shop (whichever really matches), services with starting prices, hours that match your booking calendar, and photos of the chairs, the front door and real work. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers ranking in full.</p>"""),

            ("Instagram is your portfolio, so organize it like one", f"""<p>For color, cuts and fades, people book from pictures. Your Instagram grid is the portfolio a new client scrolls through before booking, usually while sitting in someone else’s chair.</p>
<p>What separates a portfolio that books from one that just looks nice:</p>
<ul>
<li><b>Pin the three posts that show your best paid work</b>, the services you want more of. If you want more lived-in blondes and fewer box-dye corrections, pin the blondes.</li>
<li><b>Write captions people can search.</b> “Lived-in blonde on fine hair, 3.5 hours, The Woodlands” helps both the client and Instagram’s search. “Obsessed 😍” helps nobody.</li>
<li><b>Short video of the transformation.</b> A 10-second Reel of a taper fade from start to finish, or the color reveal under natural light by the window.</li>
<li><b>Highlights for the questions people DM.</b> Prices, policies, parking, “what to expect at your first appointment,” and before-and-afters by service.</li>
<li><b>A booking link in the bio</b> that opens straight to the booking page, not a link-tree with eight options.</li>
<li><b>Tag the location.</b> Use the salon’s location and the neighborhood: Market Street, Creekside, Old Town Spring, Cypress, the Heights.</li>
</ul>
<p>Don’t buy followers or likes. Beyond being obvious, the FTC’s 2024 rule on reviews and testimonials covers misuse of fake social media indicators, including bot followers and purchased likes, per {SRC['ftc_rule']}.</p>
<p>Paid Instagram and Facebook ads can work, mostly for specific services (extensions, color corrections, men’s grooming) and for retargeting people who visited your booking page. Our post on {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads for local businesses')} covers the setup.</p>"""),

            ("Chair rental vs. commission: who markets what", f"""<p>How your salon is structured changes who owns the marketing, and a lot of salon owners never settle it explicitly.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Commission or hourly salon</th><th>Chair or booth rental salon</th></tr></thead>
<tbody>
<tr><td>Who the client “belongs” to</td><td>Usually the salon</td><td>Usually the stylist</td></tr>
<tr><td>Google Business Profile</td><td>One salon profile, reviews mention stylists</td><td>Salon profile for the space, renters often build their own brand</td></tr>
<tr><td>Instagram</td><td>Salon account plus stylists’ accounts, salon sets the rules</td><td>Each renter runs their own; salon account showcases the space</td></tr>
<tr><td>Booking</td><td>One system, salon-controlled</td><td>Often several different apps under one roof</td></tr>
<tr><td>Paid ads</td><td>Salon pays, fills open chairs</td><td>Salon advertises open chairs to stylists; renters advertise themselves</td></tr>
</tbody></table></div>
<p>For commission salons, the marketing goal is to fill the whole schedule, and the salon brand matters most. New clients should be routed to whoever has openings, and the booking system should show availability across the team.</p>
<p>For rental salons, the owner’s two marketing jobs are recruiting renters (your “customer” is the stylist) and making the space look like a place clients want to visit. Help renters with a shared photo wall and a salon page that lists each renter with a booking link. Keep in mind the Square limitation above: in many setups only the business that holds the lease gets Reserve with Google.</p>
<p>TDLR also has record-keeping rules for rentals. Lessors of independent contractor practitioners must keep a list of renters with their names and license numbers, and owners must provide on request a list of independent contractors and mini-establishment licensees on site, per {SRC['tdlr_top']}. Suite studios inside a larger building are their own case; {SRC['tdlr_mini']} explains that each mini-establishment must be enclosed, licensed and displayed inside the suite.</p>"""),

            ("TDLR licenses: display them, and use them as trust", f"""<p>Texas regulates barbering and cosmetology through the Texas Department of Licensing and Regulation. Most owners think of licensing as an inspection issue. It’s also a marketing asset that few shops use.</p>
<p>The display rule: under {SRC['tac8370']}, a practitioner’s license must either be posted near their workstation in public view or be available at the reception desk, and a current photo at least 1½ by 1½ inches must be attached to the front of the license or displayed digitally with an image of the license. A missing photo is one of TDLR’s ten most common inspection violations, along with failing to post a notice that the latest inspection report is available on request.</p>
<!--fig:tdlr-->
<p>How to turn that into marketing without overdoing it:</p>
<ul>
<li>Put each stylist’s or barber’s license type on their bio page (“Licensed cosmetologist,” “Licensed barber”), and the salon’s establishment license on the about page.</li>
<li>Mention sanitation in plain words on your website. People notice clean tools and clean stations, and a short line about disinfecting between every client answers a question they won’t ask.</li>
<li>If you offer house calls or event styling booked through an app, {SRC['occ1603']} requires remote service businesses to show the practitioner’s name, license number and photo, plus state complaint information, before the service. Build that into your booking confirmation.</li>
</ul>
<p>We’d stop short of making licensing the headline of an ad. It’s a trust detail, and it works best where people are deciding: your bios, your booking page, your Google profile description.</p>"""),

            ("Reviews: automate the ask, follow the rules", f"""<p>Most booking platforms can send an automatic review request after checkout. Turn it on, and point it at Google, since that’s where new clients in The Woodlands and Houston are comparing you.</p>
<p>The rules, per {SRC['gpol']}: no discounts or free services for reviews, no discouraging negative reviews, and no review gating. The FTC rule adds bans on insider reviews that don’t disclose the relationship (a stylist’s cousin, say) and on incentives tied to a positive review, per {SRC['ftc_rule']}.</p>
<p>A script that works at the chair: <i>“If you love it, a Google review that mentions the service really helps people find us. I’ll text you the link.”</i> Then text it to every client that day, not just the ones who gushed.</p>
<p>Reply to every review within a couple of days, by name, and mention the service when you can. Answer bad reviews calmly, offer to fix it and take it offline. Future clients read your reply more closely than the complaint. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has templates.</p>"""),

            ("New-client offers that don’t attract discount hunters", f"""<p>A straight percentage off brings in people who shop by percentage. They’ll leave for the next shop that offers 25%. In our experience the offers that bring in keepers add value to the first visit or reward the second one.</p>
<!--fig:offers-->
<p>Offers that tend to work:</p>
<ul>
<li><b>Value-add on the first visit.</b> A free deep-conditioning treatment with first color, or a free hot-towel shave add-on with a first cut. The client pays full price and gets something extra.</li>
<li><b>Second-visit reward.</b> “Book your next appointment before you leave and get $15 off it.” This rewards the behavior you actually want.</li>
<li><b>Referral credit.</b> Both the client and the friend get a credit after the friend’s first visit. Clients who come from referrals tend to stay.</li>
<li><b>Consultation first, for big services.</b> A free 15-minute consult before extensions or a color correction filters out the people who just wanted a price.</li>
<li><b>Weekday-only intro offers.</b> If you have to discount, limit it to Tuesday through Thursday before 3 p.m., when the chair would otherwise be empty.</li>
</ul>
<p>Whatever you offer, track it: how many redeemed, how many rebooked within 60 days, and how many were still clients after six months. If an offer brings in 40 people and two stay, it’s a bad offer, no matter how good the redemption numbers look.</p>"""),

            ("Rebooking is your best marketing", f"""<p>The cheapest appointment you’ll ever fill is the next one for a client already in your chair. Rebooking before the client leaves does more for revenue than any ad.</p>
<!--fig:rebook-->
<p>The habits that raise rebook rates:</p>
<ol>
<li><b>Stylists ask at the chair, not the front desk.</b> “Your color will want a refresh in about seven weeks. Want me to grab a Thursday for you?” works better than a receptionist asking “do you want to book again?”</li>
<li><b>Use typical intervals by service.</b> Short men’s cuts and fades often come back every two to four weeks; most women’s cuts every six to ten; root touch-ups around five to eight; dimensional color and balayage longer. Your own data beats any rule, so check it.</li>
<li><b>Automated reminders for anyone who didn’t pre-book</b>, timed to their service interval, with a one-tap booking link.</li>
<li><b>Track rebook rate by stylist.</b> Not to shame anyone, but because the stylists with high rebook rates are doing something the others can learn.</li>
</ol>
<p>Texting is how this reaches clients, so get consent right. Appointment reminders are different from promotional texts, and Texas brought marketing texts under its telephone solicitation law through SB 140 starting September 1, 2025, per {SRC['sb140']}. Our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} explains what that means for a small business.</p>"""),

            ("Filling slow weekdays", f"""<p>Every salon and barbershop has the same shape: packed Friday afternoons and Saturdays, empty Tuesday and Wednesday mornings. You won’t flatten it completely, but you can move some demand.</p>
<!--fig:week-->
<p>Who’s free on a weekday morning in north Houston: retirees in The Woodlands and Montgomery, parents during school hours (roughly 8:30 to 3), shift workers from the hospitals and plants, remote workers, and college students. Market to them specifically:</p>
<ul>
<li><b>“School hours” appointments</b> for parents, promoted on Instagram and in your email list, with the times spelled out.</li>
<li><b>Last-minute openings.</b> Post same-day openings to Instagram Stories and text your waitlist. Some booking apps can do this automatically.</li>
<li><b>Weekday-only services.</b> Longer treatments, like color corrections or extensions, booked into weekday mornings so Saturday stays open for cuts.</li>
<li><b>Kids’ cuts after school.</b> Barbershops near elementary schools can fill 3:30 to 5 with kids before the evening rush.</li>
<li><b>Ad scheduling.</b> If you run Google or Meta ads, push more budget toward the days and hours you need to fill, and send them to a page that shows weekday availability.</li>
</ul>
<p>Houston’s weather plays a part too. Summer humidity drives demand for smoothing treatments and shorter cuts, and hurricane season (June through November) means a storm can wipe out a week of appointments. Keep a cancellation list and a plan to rebook everyone the moment you reopen.</p>"""),

            ("What to track, and a first month", f"""<p>The numbers that tell you whether marketing is working:</p>
<ul>
<li><b>New clients by source</b> (Google, Instagram, marketplace, referral, walk-in).</li>
<li><b>Rebook rate</b> at checkout, overall and by stylist or barber.</li>
<li><b>90-day return rate</b> for new clients, by source and by offer.</li>
<li><b>Chair utilization</b> by day and time block.</li>
<li><b>Average ticket</b> and retail per client.</li>
</ul>
<p>A first month for a salon or shop starting fresh:</p>
<ol>
<li><b>Week 1:</b> clean up the Google profile, connect Reserve with Google if your platform supports it, and fix the Instagram bio link and highlights.</li>
<li><b>Week 2:</b> turn on automatic review requests and reminder texts with proper consent, and check every license is posted with a current photo.</li>
<li><b>Week 3:</b> replace any straight-discount offer with a value-add or second-visit reward, and train everyone to rebook at the chair.</li>
<li><b>Week 4:</b> launch one weekday-filling campaign and measure it against the same weeks last year.</li>
</ol>
<p>If you’d like help putting this together for your salon or shop, tell us about your business and goals and a senior strategist will build a plan around your chairs and your calendar. <a href="/contact/">Get in touch</a>. For related ideas, see our posts on {L('/blog/how-to-get-more-lash-clients-the-woodlands-houston/', 'getting more lash clients')} and {L('/blog/esthetician-marketing-ideas-houston-the-woodlands/', 'esthetician marketing')}.</p>"""),
        ],
        "faq": [
            ("How do I get more clients at my hair salon or barbershop?",
             "Make it easy to book from Google with the Book button through a Reserve with Google partner, keep your Instagram organized as a portfolio with a direct booking link, and send every client the same Google review request after checkout. Then focus on keeping clients: ask them to rebook at the chair, send reminders timed to each service, and use second-visit rewards instead of big first-visit discounts."),
            ("Which salon booking apps work with Reserve with Google?",
             "Google's partner page lists Booksy, Fresha, Square Appointments, Mindbody and many others among beauty booking providers. Vagaro was not on that page when we checked in November 2026. Requirements vary: Fresha needs your Google name and address to match exactly, and Square limits Reserve with Google to the business that owns or leases the location, not booth renters."),
            ("What new client offer works best for a salon?",
             "Offers that add value or reward the second visit usually bring in better clients than a straight percentage off. Try a free add-on with a full-price first service, a discount on the next appointment if they book before leaving, or a referral credit for both the client and friend. Track how many offer clients are still coming back after six months, not just how many redeemed."),
            ("Do Texas stylists and barbers have to display their license?",
             "Yes. Under TDLR rules, a practitioner's license must be posted near their workstation in public view or be available at the reception desk, with a current photo at least 1.5 by 1.5 inches attached to the front or displayed digitally with the license. Shops must also post a notice that the latest inspection report is available, and salons that rent chairs must keep a list of renters and license numbers."),
            ("How can a salon fill slow weekdays without discounting?",
             "Market to the people who are free on weekday mornings, such as parents during school hours, retirees, shift workers and remote workers. Book long services like color corrections into weekdays, post same-day openings to Instagram Stories and a text waitlist, and shift ad budget toward the hours you need to fill. If you discount at all, restrict it to specific weekday time blocks."),
        ],
        "figures": {
            "tdlr": {
                "type": "checklist",
                "title": "TDLR items salons and barbershops miss",
                "sub": "From TDLR rules and its most common inspection violations",
                "items": ["License posted near the station or at reception", "Current 1.5 x 1.5 inch photo on the license", "Notice that the latest inspection report is available", "Renter list with names and license numbers", "List of independent contractors on request", "Remote services: name, license number and photo shown before service"],
                "alt": "Checklist of TDLR license display and record rules for hair salons and barbershops in The Woodlands and Houston",
                "caption": f"From {SRC['tac8370']} and {SRC['tdlr_top']}.",
            },
            "offers": {
                "type": "compare",
                "title": "New-client offers: who they attract",
                "left": {"title": "Attracts discount hunters", "items": ["20% off your first visit", "$10 haircuts this week only", "Groupon-style deep discounts", "Discount for a 5-star review", "Same promo every month"]},
                "right": {"title": "Attracts keepers", "items": ["Free add-on with a full-price service", "$15 off your next visit if you rebook today", "Referral credit for both people", "Free consult before big color or extensions", "Weekday-only intro, specific hours"]},
                "alt": "Comparison of salon and barbershop new client offers in The Woodlands and Houston that attract discount hunters versus loyal clients",
                "caption": "Reward the second visit and you get more people who make a third.",
            },
            "week": {
                "type": "columns",
                "title": "A typical salon week, by chair utilization",
                "sub": "Share of available chair hours booked",
                "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
                "values": [35, 45, 50, 70, 90, 98],
                "highlight": [1, 2],
                "y_label": "Booked",
                "note": "Illustrative example",
                "alt": "Column chart of weekday versus weekend chair utilization for a hair salon or barbershop in The Woodlands and Houston",
                "caption": "Tuesday and Wednesday are where the growth is. Saturday is already full.",
            },
            "rebook": {
                "type": "bars",
                "title": "Why rebooking beats new-client ads",
                "sub": "One client, $85 average ticket, visits in a year",
                "items": [["Never returns", 85, "$85"], ["Every 10 weeks", 425, "$425"], ["Every 7 weeks", 595, "$595"], ["Every 4 weeks (barber)", 1105, "$1,105"]],
                "highlight": [2],
                "note": "Illustrative example. Ticket and frequency vary by service",
                "alt": "Bar chart of annual client value by rebooking frequency for a hair salon or barbershop in Houston and The Woodlands",
                "caption": "A marketplace fee on one first visit looks small next to a client who returns all year.",
            },
        },
    },
]
