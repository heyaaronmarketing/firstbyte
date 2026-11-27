"""Batch 18 (module r_e): a month-by-month 2027 marketing calendar for Houston and The Woodlands businesses, and a
cost guide to website maintenance for Houston-area small businesses.

Research, calendar post: Fox 26 on RODEOHOUSTON 2027 (March 2-21; lineup Jan. 7; tickets Jan. 14); Click2Houston on
the Downtown Rodeo Parade (Sat., Feb. 27, 2027); ABC13 on the 2027 Chevron Houston Marathon (race weekend Jan. 13-17,
marathon and half Jan. 17, 5K Jan. 16, about 40,000 participants); Slowtwitch on IRONMAN's 2027 North American
schedule (IRONMAN Texas Sat., April 24, 2027); Visit The Woodlands/Community Impact on the IRONMAN extension through
2030; PGA Tour 2027 schedule (Texas Children's Houston Open, March 22-28, 2027, Memorial Park); Royal Museums
Greenwich (Lunar New Year Sat., Feb. 6, 2027, Year of the Goat); Texas Comptroller publication 98-490 (sales tax
holiday Aug. 6-8, 2027), 98-1017 (emergency supplies holiday was April 25-27, 2026; no 2027 dates yet) and the May
2026 release on ENERGY STAR/water-efficient holidays (May 23-25, 2026); Conroe ISD 2026-27 calendar PDF (spring break
March 15-19, last day May 27, student holidays Feb. 12, Feb. 15, March 26, March 29, April 30); Community Impact on
Cy-Fair ISD's 2026-27 calendar (spring break same week); My Neighborhood News on CFISD's 2027-28 calendar approved
Nov. 9, 2026 (first day Aug. 11, fall break Oct. 11-15, Thanksgiving break Nov. 22-26, winter break Dec. 20-31) and
Katy ISD's adopted 2027-28 calendar (first day Aug. 11, fall break Oct. 8-12, last day May 24, 2028); Click2Houston on
Houston Restaurant Weeks 2026 (Aug. 1 to Sept. 7, nearly 400 restaurants); NOAA's 2026 outlook release (season June 1
to Nov. 30, peak mid-September through October). Conroe ISD's 2027-28 calendar was not published at writing, so its
first day is given as "typically."

Research, maintenance post: SiteGround WordPress hosting page (Nov. 2026 promo $1.99/$3.99/$5.99, renewal $17.99/
$29.99/$44.99); WordPress.com pricing (Personal $4/$9, Premium $8/$18, Business $25/$40, Commerce $45/$70);
Squarespace pricing (Basic $19/$25, Core $29/$39, Plus $49/$65, Advanced $99/$139); Wix plans page (Light to Business,
location-dependent USD); Webhosting.today on Verisign's .com wholesale price ($10.26 to $10.97 on Nov. 1, 2026);
Cloudflare Registrar (at-cost pricing); Let's Encrypt (free certificates); Google's Chrome security blog (HTTPS by
default for public sites in Chrome 154, October 2026); php.net supported versions (8.2 security support ends Dec. 31,
2026; 8.3 ends Dec. 31, 2027); WordPress.org requirements (PHP 8.3+ recommended); Patchstack State of WordPress
Security in 2026 (11,334 new vulnerabilities, 91% plugins, 9% themes, 6 in core, 46% unpatched at disclosure, 5-hour
median to mass exploitation); Texas Tribune on Hurricane Beryl (about 2.26 million CenterPoint outages at peak).
Care-plan tiers and hourly ranges are labeled as our experience; WP Engine's plan page showed EUR only from here, so it
was left out.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # calendar post
    "rodeo": A("https://www.fox26houston.com/news/2027-houston-rodeo-genre-calendar-concert-lineup", "Fox 26"),
    "parade": A("https://www.click2houston.com/news/local/2026/10/29/the-voice-of-rodeohouston-named-as-2027-downtown-parade-grand-marshal/", "Click2Houston"),
    "marathon": A("https://abc13.com/post/chevron-houston-marathon-2027-what-know-plan-run-full-race-aramco-half-are-5k/19221034/", "ABC13"),
    "ironman": A("https://www.slowtwitch.com/triathlon/ironman-releases-full-2027-american-and-canadian-race-schedule/", "IRONMAN’s 2027 schedule, via Slowtwitch"),
    "imext": A("https://communityimpact.com/houston/the-woodlands/government/2024/11/20/visit-the-woodlands-extends-ironman-dates-through-2030", "Community Impact"),
    "pga": A("https://www.pgatour.com/article/news/latest/2026/08/26/pga-tour-announces-2027-schedule-through-tour-championship", "the PGA Tour’s 2027 schedule"),
    "lny": A("https://www.rmg.co.uk/stories/time/lunar-new-year-dates-animals-zodiac", "Royal Museums Greenwich"),
    "taxhol": A("https://comptroller.texas.gov/taxes/publications/98-490/", "the Texas Comptroller"),
    "emerg": A("https://comptroller.texas.gov/taxes/publications/98-1017.php", "the Comptroller’s emergency supplies page"),
    "estar": A("https://comptroller.texas.gov/about/media-center/news/20260519-sales-tax-holidays-for-water-efficient-and-energy-starr-products-set-for-may-23-25-1779119182554", "the Comptroller’s 2026 announcement"),
    "cisd": A("https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5052/Cisd/e83881e1-1d85-43d1-b350-7fb41cffd1c1/26-27-CISD-Calendar.pdf", "Conroe ISD’s 2026-27 calendar"),
    "cfisd": A("https://communityimpact.com/cypress/education/cy-fair-isd-students-staff-to-get-fall-break-in-2026/", "Community Impact"),
    "cfisd28": A("https://myneighborhoodnews.com/cfisd-board-approves-2027-2028-school-calendar-first-day-of-school-fall-break-thanksgiving-and-key-dates-for-cypress-fairbanks-families", "Cy-Fair ISD’s 2027-28 calendar"),
    "katy28": A("https://myneighborhoodnews.com/katy-isd-approves-october-fall-breaks-for-202627-and-202728-school-years-following-community-feedback", "Katy ISD’s adopted 2027-28 calendar"),
    "hrw": A("https://www.click2houston.com/news/local/2026/07/30/houston-restaurant-weeks-2026-begins-aug-1-with-nearly-400-restaurants-signed-on/", "Click2Houston"),
    "noaa": A("https://www.noaa.gov/news-release/noaa-predicts-below-normal-2026-atlantic-hurricane-season", "NOAA"),
    # maintenance post
    "sg": A("https://www.siteground.com/wordpress-hosting.htm", "SiteGround’s WordPress hosting page"),
    "wpcom": A("https://wordpress.com/pricing/", "WordPress.com’s pricing page"),
    "sqs": A("https://www.squarespace.com/pricing", "Squarespace’s pricing page"),
    "wix": A("https://www.wix.com/plans", "Wix’s plans page"),
    "verisign": A("https://webhosting.today/2026/05/21/verisign-starts-a-four-year-com-price-cycle-the-first-7-hits-in-november/", "Webhosting.today"),
    "cf": A("https://www.cloudflare.com/products/registrar/", "Cloudflare Registrar"),
    "le": A("https://letsencrypt.org/about/", "Let’s Encrypt"),
    "chrome": A("https://blog.google/security/https-by-defau/", "Google’s Chrome security team"),
    "php": A("https://www.php.net/supported-versions.php", "php.net"),
    "wpreq": A("https://wordpress.org/about/requirements/", "WordPress.org’s requirements page"),
    "patch": A("https://www.patchstack.com/whitepaper/state-of-wordpress-security-in-2026/", "Patchstack’s 2026 security report"),
    "beryl": A("https://www.texastribune.org/2024/07/08/hurricane-beryl-texas-damage-updates-rain/", "the Texas Tribune"),
}

L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: 2027 calendar
    {
        "slug": "houston-marketing-calendar-2027",
        "title": "2027 Marketing Calendar for Houston and The Woodlands Businesses: Every Date Worth Planning Around",
        "seo_title": "2027 Marketing Calendar for Houston & The Woodlands",
        "desc": "Every 2027 date Houston and The Woodlands businesses should plan around: Rodeo, marathon, IRONMAN, tax holidays, school starts, hurricanes and Black Friday.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Business Profile"],
        "art": "b2",
        "hero": "clock",
        "hero_alt": "Illustration of a clock for the 2027 marketing calendar for Houston and The Woodlands businesses",
        "related": ["rodeo-season-marketing-houston-the-woodlands", "marketing-plan-2027-small-business-houston", "hurricane-season-marketing-playbook-houston-the-woodlands"],
        "sections": [
            (None, f"""<p>Six weeks. That’s roughly how far ahead of a big date most Houston campaigns need to start, and it’s the number almost everyone forgets. The Black Friday ad that goes live on Thanksgiving morning is bidding against people who started warming up their lists in October.</p>
<p>So this calendar does two things. It lists the 2027 dates we could actually confirm for Houston and The Woodlands, with a link to the source for each one. And for every month it tells you what you should be <i>starting</i>, which is usually a different thing from what’s happening that month.</p>
<p><b>The short version:</b> the 2027 dates that move the most money for Houston and The Woodlands businesses are the Houston Marathon (Jan. 17), RODEOHOUSTON (March 2-21), spring break (March 15-19 in Conroe and Cy-Fair ISD), IRONMAN Texas (April 24), hurricane season (from June 1), the sales tax holiday (Aug. 6-8), the first day of school (Aug. 11 in Katy and Cy-Fair ISD) and Black Friday (Nov. 26).</p>
<!--fig:bigdates-->
<p>Where a date wasn’t published when we wrote this, we say “typically” and give last year’s date. Check those before you print anything.</p>"""),

            ("How to use this Houston calendar, and what we left out", f"""<p>Work backward from each date. The event is the deadline. The campaign starts weeks earlier, and the offer, the landing page and the creative have to exist before that.</p>
<!--fig:countback-->
<p>We left out things we couldn’t verify for 2027, like most festival dates that organizers announce in the spring, and we skipped dates that matter to almost nobody’s marketing (sorry, Groundhog Day). We also didn’t repeat the full rodeo playbook here. That lives in our {L('/blog/rodeo-season-marketing-houston-the-woodlands/', 'rodeo season marketing guide')}, and the budget side of the year is in the {L('/blog/marketing-plan-2027-small-business-houston/', '2027 marketing plan for Houston small businesses')}. This page is the calendar you tape next to both.</p>
<div class="bp-tbl"><table>
<thead><tr><th>2027 date</th><th>Event</th><th>Status</th><th>Start planning by</th></tr></thead>
<tbody>
<tr><td>Jan. 13-17</td><td>Chevron Houston Marathon weekend (race Sun., Jan. 17)</td><td>Confirmed</td><td>Early December 2026</td></tr>
<tr><td>Sat., Feb. 6</td><td>Lunar New Year</td><td>Confirmed</td><td>Early January</td></tr>
<tr><td>Sat., Feb. 27</td><td>Downtown Rodeo Parade</td><td>Confirmed</td><td>Mid-January</td></tr>
<tr><td>March 2-21</td><td>RODEOHOUSTON at NRG Park</td><td>Confirmed</td><td>Early January</td></tr>
<tr><td>March 15-19</td><td>Spring break, Conroe and Cy-Fair ISD</td><td>Confirmed</td><td>Early February</td></tr>
<tr><td>March 22-28</td><td>Texas Children’s Houston Open, Memorial Park</td><td>Confirmed</td><td>Mid-February</td></tr>
<tr><td>Sat., April 24</td><td>IRONMAN Texas, The Woodlands</td><td>Confirmed</td><td>Early March</td></tr>
<tr><td>Late April</td><td>Emergency supplies sales tax holiday</td><td>Typically last weekend of April</td><td>Early April</td></tr>
<tr><td>Memorial Day weekend</td><td>ENERGY STAR and water-efficient tax holidays</td><td>Typically</td><td>Late April</td></tr>
<tr><td>June 1</td><td>Hurricane season starts (ends Nov. 30)</td><td>Confirmed</td><td>Early May</td></tr>
<tr><td>Aug. 6-8</td><td>Back-to-school sales tax holiday</td><td>Confirmed</td><td>Late June</td></tr>
<tr><td>Wed., Aug. 11</td><td>First day of school, Katy and Cy-Fair ISD</td><td>Confirmed</td><td>Early July</td></tr>
<tr><td>Nov. 25-29</td><td>Thanksgiving through Cyber Monday</td><td>Confirmed</td><td>Late September</td></tr>
</tbody></table></div>"""),

            ("January 2027: marathon weekend and rodeo tickets", f"""<p>The Chevron Houston Marathon and Aramco Houston Half run on Sunday, Jan. 17, with the We Are Houston 5K on Saturday, Jan. 16, and a race weekend that runs from Jan. 13, per {SRC['marathon']}. Organizers expect around 40,000 participants, their most ever. That’s a lot of out-of-town runners in downtown hotels, plus their families looking for breakfast, massages, physical therapy and somewhere to eat a very large dinner on Sunday night.</p>
<p>What to run: for restaurants, recovery studios and PT clinics near downtown, Google Ads on “near me” searches that week, and Business Profile posts with race-weekend hours. Book it in December. By the second week of January, everyone who planned is already live.</p>
<p>January is also when the rodeo goes from rumor to calendar. The nightly concert lineup is announced Jan. 7 and individual tickets go on sale Jan. 14, per {SRC['rodeo']}. If you’re running a rodeo-night promotion, those are your two content days. And it’s resolution season, the one month a gym, a med spa or a meal-prep business doesn’t need to explain why someone should start now.</p>
<p>Start this month: Lunar New Year and Valentine’s creative, rodeo-season offers, and your spring break plan.</p>"""),

            ("February 2027: Lunar New Year, Valentine’s, the parade", f"""<p>Lunar New Year falls on Saturday, Feb. 6, and 2027 is the Year of the Goat, per {SRC['lny']}. In Houston that’s a big weekend along Bellaire Boulevard and in Sugar Land, Katy and Pearland, where a lot of Chinese and Vietnamese American families live. Restaurants, bakeries, salons and jewelry stores are the obvious players. If you’re marketing to those audiences, language and cultural details matter more than the date itself; our post on {L('/blog/asian-american-marketing-houston/', 'Asian American marketing in Houston')} covers what we’d get right before spending a dollar.</p>
<p>Valentine’s Day is a Sunday, Feb. 14. A Sunday Valentine’s spreads restaurant demand across Friday and Saturday, so sell the whole weekend. Conroe ISD students are out Friday, Feb. 12 and Monday, Feb. 15 (Presidents’ Day), per {SRC['cisd']}, which makes it a four-day weekend for a lot of families in The Woodlands, Conroe and Montgomery County. Kids’ activity businesses should notice that before the week arrives.</p>
<p>The Downtown Rodeo Parade is Saturday, Feb. 27, per {SRC['parade']}. Then freeze risk: Houston typically gets at least one hard freeze threat in January or February. Plumbers, HVAC companies and pool services should have a freeze landing page and a paused ad group built in December, ready to flip on the afternoon the forecast turns.</p>"""),

            ("March 2027: rodeo, spring break and the Houston Open", f"""<p>RODEOHOUSTON runs March 2 to 21 at NRG Park, per {SRC['rodeo']}. For restaurants, bars, western wear, hotels and anyone near NRG, it’s the biggest three weeks of the first half. For many service businesses it’s a distraction, because your customers’ evenings are booked. The full week-by-week plan is in our {L('/blog/rodeo-season-marketing-houston-the-woodlands/', 'rodeo season guide')}, so we won’t repeat it.</p>
<p>Spring break lands inside the last week of rodeo. Conroe ISD is out March 15 to 19, per {SRC['cisd']}, and Cy-Fair ISD has the same week, per {SRC['cfisd']}. Katy, Klein, Tomball, Humble and Houston ISD set their own calendars, so check yours. That week, camps, trampoline parks, pet boarding and tutoring get busy, while appointment businesses see no-shows climb. Send reminder texts two days out instead of one.</p>
<p>Daylight saving time starts Sunday, March 14. One more hour of evening light matters to patio restaurants, landscapers and anyone selling outdoor projects.</p>
<p>The Texas Children’s Houston Open is March 22 to 28 at Memorial Park, per {SRC['pga']}. Easter is Sunday, March 28. Conroe ISD has student holidays on Friday, March 26 and Monday, March 29, which makes another four-day weekend north of the Grand Parkway.</p>
<p>Start this month: IRONMAN weekend plans if you’re in The Woodlands, and your Mother’s Day offer.</p>"""),

            ("April 2027: IRONMAN Texas in The Woodlands, and tax day", f"""<p>Memorial Hermann IRONMAN Texas is Saturday, April 24, per {SRC['ironman']}. The race stays in The Woodlands through 2030 under an extension Visit The Woodlands approved in 2024, per {SRC['imext']}. Race day changes the whole town: the swim is in Lake Woodlands, the bike course heads out to the Hardy Toll Road, and the run loops around the Waterway and its trails until late at night.</p>
<p>That cuts both ways. Hotels, restaurants near Market Street and Hughes Landing, bike shops, massage and recovery studios get a weekend of athletes and families. A salon on Woodlands Parkway might lose half its Saturday to road closures. If you’re in the second group, tell your customers early which streets will be closed and when you’re open; it saves you a day of no-shows and confused phone calls. If you’re in the first group, run Business Profile posts and tight-radius search ads from Wednesday on, when athletes start arriving.</p>
<!--fig:map-->
<p>Tax day is Thursday, April 15, which matters for CPAs, bookkeepers and financial advisors, who should have stopped advertising for new returns weeks earlier and started advertising extensions and next-year planning.</p>
<p>The emergency supplies sales tax holiday typically falls on the last weekend of April. It ran April 25 to 27 in 2026, per {SRC['emerg']}; the 2027 dates weren’t posted when we wrote this. Hardware stores, generator dealers and anyone selling batteries or storm gear should watch for the announcement. Conroe ISD students also have a holiday on Friday, April 30.</p>"""),

            ("May 2027: Mother’s Day, the last day of school and storm prep", f"""<p>Mother’s Day is Sunday, May 9. Florists, restaurants, spas and boutiques in The Woodlands and Kingwood already know. What they often miss is that the gift-card shopper is a procrastinator. Run gift-card ads on the Thursday and Friday before, aimed at people within a few miles, with “buy online, print at home” in the headline.</p>
<p>The ENERGY STAR and water-efficient products tax holidays typically run over Memorial Day weekend (May 23 to 25 in 2026, per {SRC['estar']}). HVAC companies, appliance stores and irrigation contractors can build an offer around them, as long as the ad is specific about which items qualify.</p>
<p>The last day of school is Thursday, May 27, in Conroe ISD, per {SRC['cisd']}. Memorial Day is Monday, May 31. Summer camps should be almost full by now; if they’re not, the enrollment push started too late.</p>
<p>May is also the month to build every storm asset before you need it.</p>
<!--fig:storm-->
<p>Start this month: hurricane-season pages, back-to-school creative for July and your Houston Restaurant Weeks application if you run a restaurant.</p>"""),

            ("June and July 2027: hurricane season, Juneteenth and peak heat", f"""<p>Hurricane season runs June 1 to Nov. 30, and the historical peak is mid-September through October, per {SRC['noaa']}. If a storm heads for the Gulf Coast, your plan should already say which campaigns pause, which turn on and what you post. Our {L('/blog/hurricane-season-marketing-playbook-houston-the-woodlands/', 'hurricane season marketing playbook')} walks through it phase by phase.</p>
<p>Juneteenth falls on Saturday, June 19. The holiday started in Galveston, and Houston’s celebrations in Emancipation Park and around the city draw big crowds. If your business takes part, show up with something real, like a sponsorship, a featured local vendor or an event. A logo with a flag on it doesn’t count. Father’s Day is the next day, Sunday, June 20.</p>
<p>July 4 is a Sunday. Expect most offices to close Monday, July 5, and many families to stretch it into a long weekend at Lake Conroe or Galveston.</p>
<p>July is peak heat, peak AC calls and the slowest month of the year for plenty of restaurants and retail. If you’re in the slow group, this is the month for a members-only offer to your email list rather than new-customer ads in a quiet market. If you’re an HVAC or pool company, keep the budget steady and answer the phone.</p>
<p>Start in June: the sales tax holiday offer and back-to-school ads. Start in July: Black Friday planning, honestly. Ten weeks out is not too early to pick the offer.</p>"""),

            ("When does school start in Katy, Cy-Fair and Conroe ISD in 2027?", f"""<p>Katy ISD and Cy-Fair ISD both start the 2027-28 school year on Wednesday, Aug. 11, 2027, per {SRC['katy28']} and {SRC['cfisd28']} (Cy-Fair’s was approved Nov. 9, 2026). Conroe ISD hadn’t published its 2027-28 calendar when we wrote this; it typically starts in the second week of August, and the 2026-27 year began Aug. 12.</p>
<div class="bp-tbl"><table>
<thead><tr><th>District</th><th>First day 2027-28</th><th>Fall break</th><th>Other dates</th></tr></thead>
<tbody>
<tr><td>Katy ISD</td><td>Wed., Aug. 11, 2027</td><td>Oct. 8-12, 2027</td><td>Last day May 24, 2028</td></tr>
<tr><td>Cy-Fair ISD</td><td>Wed., Aug. 11, 2027</td><td>Oct. 11-15, 2027</td><td>Thanksgiving break Nov. 22-26; winter break Dec. 20-31</td></tr>
<tr><td>Conroe ISD</td><td>Typically 2nd week of August</td><td>Check district calendar</td><td>2026-27 last day is May 27, 2027</td></tr>
</tbody></table></div>
<p>The sales tax holiday runs Friday, Aug. 6 through Sunday, Aug. 8, per {SRC['taxhol']}. It falls the weekend before Katy and Cy-Fair start, so that weekend is the peak for clothing, shoes and school supplies in Katy, Cypress and the Tomball and FM 1960 corridors. If you sell qualifying items, your ads should run the week before, and they should say which items are tax-free. Vague “tax-free weekend sale” headlines are everywhere that week.</p>
<p>Back-to-school also means after-school enrollment: dance, martial arts, tutoring, music lessons and youth sports. Parents decide in late July, not the second week of school. Our {L('/blog/back-to-school-marketing-woodlands/', 'back-to-school marketing post')} has more for The Woodlands specifically.</p>
<p>Restaurants: Houston Restaurant Weeks typically runs through August into Labor Day. In 2026 it ran Aug. 1 to Sept. 7 with nearly 400 restaurants, per {SRC['hrw']}. It’s a good way to get first-timers in the door during a slow month, as long as you plan how to bring them back.</p>"""),

            ("September and October 2027: storm peak, fall breaks and holiday bookings", f"""<p>Labor Day is Monday, Sept. 6. After it, the calendar fills with Q4 decisions: holiday party bookings for venues and caterers, year-end appointments for medical and dental practices whose patients have met their deductibles, and the gift-card plan for anyone in retail or services.</p>
<p>It’s also the heart of hurricane season. Keep storm creative ready and keep a little budget in reserve. A storm in late September can wipe out a week of sales and then create a month of demand for roofers, tree services and restoration companies.</p>
<p>Fall breaks arrive in October: Katy ISD is out Oct. 8 to 12 and Cy-Fair Oct. 11 to 15, per the district calendars above. That’s a mini spring break for camps, family entertainment and travel. Halloween is a Sunday, which pushes parties and events to Friday and Saturday, Oct. 29 and 30.</p>
<p>October is when serious Black Friday work starts. Grow your email and SMS lists (with proper consent), decide on your offer and line up the creative. Our {L('/blog/holiday-marketing-checklist/', 'holiday marketing checklist')} is a useful way to make sure nothing is missing.</p>"""),

            ("When should Houston businesses start Black Friday marketing?", f"""<p>Start planning the offer in September and start building your audience in early October. Warm-up ads and emails go out in the first two weeks of November, and the main push runs Thanksgiving week. For 2027, Thanksgiving is Thursday, Nov. 25, Black Friday is Nov. 26, Small Business Saturday is Nov. 27 and Cyber Monday is Nov. 29.</p>
<!--fig:bfunnel-->
<p>Why so early? Ad prices on Meta and Google climb through November as the big retailers pile in. If your first contact with a shopper is a cold ad on Black Friday, you’re paying the year’s highest prices to reach someone who doesn’t know you. If they already saw your October content and joined your list, Black Friday is an email that costs you nothing to send.</p>
<p>A few other November dates. Daylight saving time ends Sunday, Nov. 7 (dark at 5:30 is bad news for evening foot traffic). Cy-Fair ISD is out the whole week of Nov. 22 to 26. And hurricane season ends Nov. 30, which is a good day to switch off storm ad groups you forgot about.</p>
<p>Small Business Saturday is the one to own if you’re a shop on Market Street, in Old Town Spring or downtown Conroe or Tomball. Lean into being local. The national chains can’t copy that.</p>"""),

            ("December 2027: winter break, reviews and the 2028 plan", f"""<p>Cy-Fair ISD’s winter break runs Dec. 20 to 31, per {SRC['cfisd28']}, and most districts are close. Christmas is a Saturday. For retail and restaurants it’s gift cards and last-minute shopping through Dec. 23. For most service businesses December is slow on new leads and busy on year-end jobs.</p>
<p>Use the slow part. Send review requests to everyone you served this fall while the job is fresh; a strong January on Google Maps starts in December. Clean up your tracking so every 2028 lead has a source. And draft next year’s calendar now, with the dates that worked this year marked and the ones that flopped crossed out.</p>
<!--fig:leadtimes-->"""),

            ("Which 2027 dates matter for your kind of Houston business", f"""<p>Nobody needs every date on this page. Pick the three or four that move your revenue and build the year around them.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Business type</th><th>Dates that matter most in 2027</th><th>Start by</th></tr></thead>
<tbody>
<tr><td>Restaurants and bars</td><td>Marathon weekend, Valentine’s weekend, rodeo, Mother’s Day, Restaurant Weeks</td><td>December for January; six weeks before the rest</td></tr>
<tr><td>Retail and boutiques</td><td>Lunar New Year, tax holiday Aug. 6-8, Small Business Saturday Nov. 27</td><td>Late June for August; October for November</td></tr>
<tr><td>Home services</td><td>Freeze risk, Memorial Day tax holidays, hurricane season, first cool front</td><td>Build storm and freeze assets in May and December</td></tr>
<tr><td>Kids’ activities and education</td><td>Spring break March 15-19, last day of school, first day Aug. 11, fall breaks</td><td>Eight weeks before each</td></tr>
<tr><td>Fitness and wellness</td><td>New year, marathon weekend, IRONMAN Texas, back to school</td><td>Early December and early March</td></tr>
<tr><td>Medical, dental and professional services</td><td>Tax day, back to school, year-end deductibles</td><td>Early March and September</td></tr>
</tbody></table></div>
<!--fig:mindset-->
<p>Once you know your four dates, put the start dates on the calendar, not the event dates. That one change does more than any campaign idea we could give you. For the wider seasonal picture, our {L('/blog/seasonal-marketing-greater-houston/', 'guide to Houston’s marketing seasons')} covers the slow and busy months by industry, and our {L('/services/search-marketing/', 'search')} and {L('/services/paid-social-advertising/', 'paid social')} teams build the campaigns.</p>
<p>If you’d like a senior strategist to turn this calendar into a plan for your business, <a href="/contact/">get in touch</a> and tell us which dates matter to you.</p>"""),
        ],
        "faq": [
            ("When is the Houston Rodeo in 2027?",
             "RODEOHOUSTON runs from Tuesday, March 2 through Sunday, March 21, 2027, at NRG Park. The Downtown Rodeo Parade is Saturday, February 27. The nightly concert lineup is announced January 7 and individual tickets go on sale January 14. Businesses that want rodeo traffic should have offers and creative ready in early January, because most of the planning by customers happens before the gates open."),
            ("When is the Texas sales tax holiday in 2027?",
             "The back-to-school sales tax holiday runs Friday, August 6 through Sunday, August 8, 2027, according to the Texas Comptroller. The emergency supplies holiday is typically the last weekend of April and the ENERGY STAR and water-efficient holidays typically fall on Memorial Day weekend, but those 2027 dates had not been posted when we wrote this. Check the Comptroller’s site before you advertise them."),
            ("When does school start in Cy-Fair ISD and Katy ISD in 2027?",
             "Both Cy-Fair ISD and Katy ISD start the 2027-28 school year on Wednesday, August 11, 2027. Cy-Fair’s fall break is October 11 to 15 and Katy’s is October 8 to 12. Conroe ISD had not released its 2027-28 calendar at the time of writing; it typically starts in the second week of August. Back-to-school ads should start in early to mid July."),
            ("When is IRONMAN Texas 2027 in The Woodlands?",
             "IRONMAN Texas is Saturday, April 24, 2027, and the race is set to stay in The Woodlands through 2030. Expect athletes and families to arrive midweek and road closures on race day around Lake Woodlands, the Hardy Toll Road and the Waterway. Nearby businesses should post race-day hours on Google and warn regular customers about closures a week ahead."),
            ("How far in advance should a small business plan holiday marketing in Houston?",
             "Pick your holiday offer in September, start growing your email and text lists in October, and begin warm-up ads in early November. The main push runs Thanksgiving week, which in 2027 means Thanksgiving on November 25 through Cyber Monday on November 29. Ad costs rise through November, so reaching people before Black Friday is much cheaper than reaching them on it."),
        ],
        "figures": {
            "bigdates": {
                "type": "stats",
                "title": "Four 2027 dates to circle first",
                "stats": [["Mar 2", "RODEOHOUSTON opens, runs through March 21"], ["Apr 24", "IRONMAN Texas in The Woodlands"], ["Aug 6-8", "Texas back-to-school tax holiday"], ["Nov 26", "Black Friday, two days before Cyber Monday"]],
                "note": "Sources: Fox 26, IRONMAN, Texas Comptroller",
                "alt": "Key 2027 marketing dates for Houston and The Woodlands businesses: rodeo, IRONMAN Texas, tax holiday and Black Friday",
                "caption": "The four dates that shift the most local spending. The full table is below.",
            },
            "countback": {
                "type": "steps",
                "title": "Count back from the date",
                "sub": "Our usual timeline for a seasonal campaign in Houston",
                "steps": [["8 weeks out", "Pick the offer and the audience. Write it in one sentence."], ["6 weeks out", "Brief the creative: photos, video, ad copy, email."], ["4 weeks out", "Build the landing page and ad campaigns; set up tracking."], ["2 weeks out", "Launch warm-up ads, posts and the first email."], ["The date", "Main push, updated Business Profile hours, staff ready."], ["1 week after", "Review requests, thank-you email, notes for 2028."]],
                "alt": "Six-step timeline for planning seasonal marketing campaigns for Houston and The Woodlands businesses",
                "caption": "Short on time? Cut the creative, keep the landing page and the tracking.",
            },
            "map": {
                "type": "map",
                "title": "Where the 2027 calendar happens",
                "sub": "Rodeo at NRG, IRONMAN in The Woodlands, school starts in Katy and Cypress",
                "highlight": ["The Woodlands", "Conroe", "Katy", "Cypress", "Bellaire", "Sugar Land", "Spring"],
                "alt": "Map of Greater Houston showing where 2027 marketing dates land, from The Woodlands and Conroe to Katy, Cypress and Bellaire",
                "caption": "Each date has its own geography. Target the radius where the people actually are that week.",
            },
            "storm": {
                "type": "checklist",
                "title": "Build these in May, before June 1",
                "sub": "Hurricane season prep for your marketing",
                "items": ["Storm landing page drafted and unpublished", "Paused Google Ads ad group for storm searches", "Pre-written posts: closed, reopened, how to reach us", "Business Profile special hours ready to set", "Customer email and text templates approved", "Promotions you would pause listed in one place", "Backup way to answer phones if the office loses power", "Login list for every account kept off-site"],
                "alt": "Checklist of hurricane season marketing prep for Houston and The Woodlands businesses to finish in May",
                "caption": f"Season dates from {SRC['noaa']}. Peak risk is mid-September through October.",
            },
            "bfunnel": {
                "type": "funnel",
                "title": "Black Friday 2027, working backward",
                "stages": [["Pick the offer", "September"], ["Grow the email and SMS list", "October"], ["Warm-up ads and teaser emails", "Nov. 1-19"], ["Early access for subscribers", "Nov. 22-24"], ["Black Friday to Cyber Monday", "Nov. 26-29"]],
                "alt": "Funnel timeline of Black Friday 2027 marketing for Houston and The Woodlands retailers from September to Cyber Monday",
                "caption": "The cheapest Black Friday customer is one who joined your list in October.",
            },
            "leadtimes": {
                "type": "bars",
                "title": "How early to start, by event",
                "sub": "Weeks between campaign start and the date",
                "items": [["Black Friday and holiday season", 10, "10 weeks"], ["RODEOHOUSTON", 8, "8 weeks"], ["Spring break camps and programs", 8, "8 weeks"], ["Back to school, Aug. 11", 5, "5 weeks"], ["Sales tax holiday, Aug. 6-8", 4, "4 weeks"], ["Mother’s Day, May 9", 4, "4 weeks"], ["IRONMAN Texas weekend", 3, "3 weeks"]],
                "highlight": [0],
                "note": "Our recommended lead times, not a benchmark",
                "alt": "Bar chart of recommended marketing lead times for 2027 Houston events, from Black Friday to IRONMAN Texas in The Woodlands",
                "caption": "Bigger purchase, bigger crowd of advertisers, longer runway.",
            },
            "mindset": {
                "type": "compare",
                "title": "Two ways to use a marketing calendar",
                "left": {"title": "Calendar of events", "items": ["Writes down the date of Black Friday", "Notices the rodeo when traffic backs up", "Builds storm pages after landfall", "Starts back-to-school ads on Aug. 11", "Same plan next year, no notes"]},
                "right": {"title": "Calendar of start dates", "items": ["Writes down the day to pick the offer", "Has rodeo creative live in early January", "Storm pages built and paused in May", "Back-to-school ads live in early July", "Notes on what worked, kept for 2028"]},
                "alt": "Comparison of event-based and start-date-based marketing calendars for Houston and The Woodlands small businesses",
                "caption": "Same dates. The second calendar wins most of them.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: website maintenance cost
    {
        "slug": "website-maintenance-cost-houston",
        "title": "How Much Does Website Maintenance Cost in Houston and The Woodlands?",
        "seo_title": "Website Maintenance Cost in Houston & The Woodlands",
        "desc": "What website maintenance costs in Houston and The Woodlands: hosting, domain, SSL, updates, backups and care-plan tiers, with real prices from official pages.",
        "category": "Websites",
        "icons": ["Google", "Search Console", "Google Analytics"],
        "art": "b6",
        "hero": "browser",
        "hero_alt": "Illustration of a browser window for website maintenance cost in Houston and The Woodlands",
        "related": ["how-much-does-a-website-cost-the-woodlands", "wordpress-vs-wix-vs-squarespace-vs-webflow-small-business", "get-website-domain-back-from-web-designer"],
        "sections": [
            (None, f"""<p>“Why am I still paying every month for a website that’s already built?”</p>
<p>We hear some version of that from a Houston business owner most weeks. It’s a fair question, and the honest answer is that some of those monthly charges are real costs, some are insurance, and a few are padding. This guide splits them apart, with prices from the platforms’ own pages as of late November 2026.</p>
<p><b>The short answer:</b> website maintenance for a typical small-business site in Houston or The Woodlands costs about $20 to $50 a month on a hosted builder like Squarespace or Wix, where updates are included. A WordPress site with a professional care plan usually runs $100 to $350 a month in our experience. Add a domain at roughly $11 to $25 a year. SSL should cost nothing.</p>
<p>The cheapest option is rarely the one that costs least over three years. The rest of this post is about why.</p>"""),

            ("How much does website maintenance cost in Houston? The line items", f"""<p>Every site, on any platform, has the same handful of costs. What changes is who pays for each one, and which ones come bundled.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>What it is</th><th>Typical cost</th><th>Where the price comes from</th></tr></thead>
<tbody>
<tr><td>Domain</td><td>Your yourbusiness.com address</td><td>About $11 to $25 a year for a .com</td><td>Wholesale .com price plus registrar markup</td></tr>
<tr><td>SSL certificate</td><td>The padlock; makes the site HTTPS</td><td>$0 on most hosts</td><td>Free certificates from Let’s Encrypt and others</td></tr>
<tr><td>Hosting or platform plan</td><td>Where the site lives</td><td>$4 to $45 a month for small sites</td><td>Official plan pages below</td></tr>
<tr><td>Updates and security</td><td>Software, plugin and theme updates, monitoring</td><td>Included on builders; on WordPress, your time or a care plan</td><td>Our experience</td></tr>
<tr><td>Backups</td><td>Copies you can restore from</td><td>Often included; off-site copies extra</td><td>Host plan pages</td></tr>
<tr><td>Content changes and fixes</td><td>New photos, prices, pages, broken forms</td><td>Your time, a care-plan allowance, or hourly</td><td>Our experience</td></tr>
<tr><td>Business email</td><td>you@yourbusiness.com</td><td>Usually billed per user, per month</td><td>Google Workspace or Microsoft 365</td></tr>
</tbody></table></div>
<p>If you’re still budgeting the build itself, our {L('/blog/how-much-does-a-website-cost-the-woodlands/', 'guide to what a website costs in The Woodlands')} covers that. This post is about year two and beyond.</p>"""),

            ("Domain names: the cheapest line, and the one that causes the most trouble", f"""<p>A .com domain doesn’t cost much. Verisign, which runs the .com registry, raised its wholesale price from $10.26 to $10.97 on Nov. 1, 2026, per {SRC['verisign']}. Registrars add their markup on top. {SRC['cf']} says it sells at cost with no markup, while plenty of the big consumer registrars advertise a cheap first year and renew at two or three times that.</p>
<p>The price isn’t the real risk, though. Ownership is. When a web designer registers your domain in their own account, they control your website address and your email. When they retire, move to Austin or stop answering, you find out how much that matters. It happens more often than you’d think: the renewal notice goes to a designer’s old inbox, the domain lapses, and the website and email go dark together.</p>
<p>Three things to check today. Make sure the domain is registered in your business’s name, with an email address you control. Turn on auto-renew with a card that won’t expire next month. And write down the registrar login somewhere other than your office computer. If someone else has it now, our post on {L('/blog/get-website-domain-back-from-web-designer/', 'getting your domain back from a web designer')} walks through ICANN’s process.</p>"""),

            ("Do you need to pay for an SSL certificate?", f"""<p>Almost never, for a small business. {SRC['le']} issues trusted certificates at zero cost, and most hosts and every major website builder include free, auto-renewing SSL. If someone is billing you $80 to $150 a year for “SSL,” ask what you’re getting that the free certificate doesn’t give you. For a brochure site or a lead-gen site, the answer is usually nothing.</p>
<p>What you do need is for SSL to work everywhere, all the time. In October 2026, Chrome 154 turned on “Always Use Secure Connections” for public sites by default, which means Chrome now shows a warning and asks visitors to confirm before loading a site over plain HTTP, per {SRC['chrome']}. A lapsed certificate or an old page that still loads over HTTP now costs you visitors at the door, before they see a thing.</p>
<p>This is a maintenance task, not a purchase. Someone should check that the certificate renews, that every page redirects to HTTPS and that your forms submit securely.</p>"""),

            ("Hosting and platform prices from the official pages", f"""<p>These are the list prices on each company’s own pricing page as we wrote this, in late November 2026. Black Friday sales were running, which turns out to be a useful lesson.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform and plan</th><th>Price shown</th><th>Updates included?</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>SiteGround StartUp (WordPress)</td><td>$1.99/mo promo, then $17.99/mo</td><td>Server and WordPress core; plugins still need attention</td><td>One site, free SSL and backups</td></tr>
<tr><td>SiteGround GrowBig</td><td>$3.99/mo promo, then $29.99/mo</td><td>Same</td><td>Unlimited sites, on-demand backups</td></tr>
<tr><td>WordPress.com Business</td><td>$25/mo yearly, $40/mo monthly</td><td>Hosting and core handled; you manage plugins</td><td>Real-time backups, staging site</td></tr>
<tr><td>Squarespace Core</td><td>$29/mo yearly, $39/mo monthly</td><td>Yes</td><td>Basic is $19/$25 but charges 2% on store sales</td></tr>
<tr><td>Wix Light to Business</td><td>About $17 to $40/mo yearly</td><td>Yes</td><td>Wix notes USD prices vary by location</td></tr>
</tbody></table></div>
<p>Sources: {SRC['sg']}, {SRC['wpcom']}, {SRC['sqs']} and {SRC['wix']}.</p>
<!--fig:promo-->
<p>Look at SiteGround’s numbers. The promo is real, and prepaid for 12 months. Then StartUp renews at $17.99 a month, about nine times the first-year rate. Nothing shady about it (it’s printed right there), but a lot of owners budget from the promo and get surprised in year two. Always budget from the renewal price.</p>
<p>Whether a hosted builder or WordPress is right for you is its own decision, and we compared them platform by platform in {L('/blog/wordpress-vs-wix-vs-squarespace-vs-webflow-small-business/', 'WordPress vs. Wix vs. Squarespace vs. Webflow')}. For maintenance costs, the key difference is simple: on Squarespace and Wix, the company does the updates. On WordPress, somebody on your side does, or nobody does.</p>"""),

            ("Updates and security: what you’re actually paying for", f"""<p>Most of a WordPress care plan is updates, and the numbers explain why.</p>
<!--fig:vulns-->
<p>{SRC['patch']} counted 11,334 new vulnerabilities in the WordPress ecosystem in 2025, up 42% from 2024. Of those, 91% were in plugins, 9% in themes, and only six were in WordPress core. Nearly half (46%) had no fix available from the developer when they were made public. For heavily exploited flaws, the weighted median time to mass exploitation was five hours.</p>
<p>Five hours. That’s why “we update plugins every quarter” isn’t a maintenance plan. It’s also why the count of plugins on your site matters more than the brand of your host. A site with 12 well-maintained plugins is far easier to keep safe than one with 45, a few of them last updated back when the iPhone 8 was new.</p>
<!--fig:security-->
<p>Then there’s the software underneath WordPress. PHP 8.2 reaches the end of its security support on Dec. 31, 2026, and PHP 8.3 follows on Dec. 31, 2027, per {SRC['php']}. {SRC['wpreq']} recommends PHP 8.3 or newer. When a host moves your site to a newer PHP version (and they will), an old theme or an abandoned plugin can break with it, which usually shows up as a blank white page or a contact form that quietly stops sending. If your site hasn’t been touched since 2022, that upgrade is coming for it within the next year.</p>"""),

            ("Backups, and the Houston reason to keep them off-site", f"""<p>Most hosts include automatic backups. Good. The questions that matter are where the backups live, how long they’re kept, and whether anyone has ever restored one.</p>
<p>A backup that sits on the same server as the site disappears with the site if the server account is compromised or cancelled. Keep at least one copy somewhere else, such as cloud storage you own, and keep 30 days of history so you can go back to before a hack you didn’t notice for a week.</p>
<p>Houston adds its own reason. When Hurricane Beryl hit in July 2024, CenterPoint had about 2.26 million outages at the peak, and some customers were still dark more than a week later, per {SRC['beryl']}. Websites on commercial hosting stayed up. Sites (and email servers, and the only copy of the logo files) running on a machine in a back office in Pearland or Humble did not. If anything about your website lives on hardware in your building, fix that before next June.</p>
<p>Test a restore once a year. It takes an hour on a staging site, and it’s the only way to know the backups actually work.</p>"""),

            ("What’s in a website care plan? Typical tiers and prices", f"""<p>Agencies and freelancers package maintenance as monthly care plans. Names vary, but the tiers usually look like this. The prices are ranges from what we see across the Houston market and our own work, not a published benchmark.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Tier</th><th>Typical monthly range</th><th>What’s usually included</th><th>Good fit</th></tr></thead>
<tbody>
<tr><td>Basic</td><td>$75 to $150</td><td>Updates, daily backups, uptime monitoring, security scans, a monthly report</td><td>Brochure sites that rarely change</td></tr>
<tr><td>Standard</td><td>$150 to $350</td><td>Basic plus off-site backups, an hour or two of edits, form and speed checks, PHP upgrade testing</td><td>Most service businesses getting leads from the site</td></tr>
<tr><td>Growth</td><td>$400 to $1,000+</td><td>Standard plus new pages, landing pages for ads, conversion tracking checks, SEO fixes</td><td>Sites with ad spend or lots of service-area pages</td></tr>
</tbody></table></div>
<p>Two things separate a good plan from a bad one. The first is whether updates are tested. Clicking “update all” on a live site is how forms break on a Friday afternoon. Good plans update on a staging copy first, or at least check the key pages right after.</p>
<p>The second is whether anyone checks the stuff that makes you money. A site can be fully updated and still have a contact form sending leads to an inbox nobody reads. We’d want the monthly report to include a test form submission and a test click-to-call, along with a check that your {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'form and call tracking')} still fires.</p>
<p>Hourly work outside a plan usually runs somewhere in the $75 to $175 range around Houston, again in our experience. A hacked-site cleanup almost always costs more than a year of the basic tier.</p>"""),

            ("What breaks when nobody maintains a website", f"""<p>Unmaintained sites rarely crash all at once. They decay, and the owner usually notices last.</p>
<!--fig:decay-->
<p>The expensive part is the stretch in the middle, when the site looks fine to you and has quietly stopped working for customers. A form that stopped sending in April doesn’t announce itself. You just have a slow summer and blame the heat.</p>
<p>Speed slides too. Images get added at full camera size, scripts pile up from old ad campaigns, and the plugin that once made the site fast is now three versions behind. Our guide on {L('/blog/how-fast-should-your-website-load/', 'how fast your website should load')} has the numbers to check. And if the site has decayed far enough that a rebuild makes more sense, read {L('/blog/website-redesign-without-losing-seo-rankings/', 'how to redesign without losing your rankings')} before anyone touches a URL.</p>"""),

            ("Who should own the logins?", f"""<p>You should. Your vendor should have access, under their own user account, that you can remove in two minutes. Shared passwords and “the developer set it all up” are how businesses end up negotiating to get their own website back.</p>
<!--fig:logins-->
<p>Keep this list in a password manager the business owns, with at least two people at the company who can open it. When you change vendors, remove the old vendor’s users the same day and change any shared passwords. Our post on {L('/blog/who-owns-google-ads-account-switch-agencies/', 'who owns your marketing accounts when you switch agencies')} covers Google Ads, Analytics and Business Profile in the same way.</p>"""),

            ("Is it cheaper to maintain a website yourself?", f"""<p>On a hosted builder, yes, usually. Squarespace and Wix handle the software, so your job is content: hours, prices, photos, the occasional new page. An owner who’s comfortable with the editor can do that in an hour or two a month.</p>
<p>On WordPress, DIY is cheaper only if you actually do it. That means checking for updates weekly, updating carefully, keeping off-site backups, watching for PHP changes from your host, and testing your forms after every change. Call it two to four hours a month for a simple site, in our experience, plus the occasional evening when an update breaks something.</p>
<!--fig:diy-->
<p>The math most owners skip is what an hour of their time is worth, and what a broken form costs during your busy season. A Conroe HVAC company that misses a week of leads in July has lost more than a year of care-plan fees. A Montgomery County photographer whose site is mostly a portfolio probably hasn’t.</p>
<p>Before you sign anything, ask what happens to your site if you cancel, whether you keep the files and the domain, and who holds the admin login. Our list of {L('/blog/marketing-agency-contract-red-flags/', 'marketing agency contract red flags')} applies to web contracts too.</p>
<p>Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} builds and maintains sites for businesses around Houston and The Woodlands, and we’ll tell you plainly if a $29 Squarespace plan is all you need. If you want a senior strategist to look at your site, your costs and your goals and put together a plan, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How much does WordPress website maintenance cost per month in Houston?",
             "Hosting alone runs about $18 to $45 a month at regular renewal prices for a small WordPress site. A professional care plan covering updates, backups, monitoring and small edits usually costs $100 to $350 a month for a Houston small business in our experience, and more if it includes new pages or ad landing pages. Doing it yourself costs less in cash but takes a few hours a month."),
            ("Do I need to pay for an SSL certificate for my small business website?",
             "Usually not. Free certificates from Let’s Encrypt are trusted by every major browser, and most hosts and website builders include free SSL that renews on its own. What matters is that it stays valid and every page loads over HTTPS, because Chrome now warns visitors before loading plain HTTP public sites by default. Paid certificates rarely add anything a local business needs."),
            ("What happens if I stop paying for website maintenance?",
             "On Squarespace or Wix, the platform keeps updating the software, so the main risk is stale content. On WordPress, plugins and themes fall behind, security holes stay open, and a forced PHP upgrade from your host can break the site. Forms often fail silently first. If you cancel a care plan, make sure you have admin access, the domain login and a recent off-site backup."),
            ("How much does a .com domain cost per year in 2027?",
             "Verisign raised the wholesale price of a .com domain to $10.97 on November 1, 2026, and registrars add their own markup on top. At-cost registrars charge close to the wholesale price, while many consumer registrars advertise a cheap first year and renew at $20 or more. Budget from the renewal price, and make sure the domain is registered in your business’s name."),
            ("Can my web designer keep my domain if I stop working with them?",
             "If the designer registered the domain in their own name or account, they control it, and getting it back may take cooperation or a formal transfer process. That is why the domain should be registered to your business, using an email address you control, from day one. If the designer already holds it, ask for a transfer in writing and document the request."),
        ],
        "figures": {
            "promo": {
                "type": "bars",
                "title": "First-year promo vs. renewal price",
                "sub": "SiteGround WordPress plans, per month, late November 2026",
                "items": [["StartUp, promo", 1.99, "$1.99"], ["StartUp, renewal", 17.99, "$17.99"], ["GrowBig, promo", 3.99, "$3.99"], ["GrowBig, renewal", 29.99, "$29.99"], ["GoGeek, promo", 5.99, "$5.99"], ["GoGeek, renewal", 44.99, "$44.99"]],
                "highlight": [1, 3, 5],
                "note": "Source: SiteGround’s WordPress hosting page",
                "alt": "Bar chart comparing promotional and renewal hosting prices for website maintenance budgets in Houston and The Woodlands",
                "caption": f"Prices from {SRC['sg']}. Budget from the renewal line.",
            },
            "vulns": {
                "type": "columns",
                "title": "Where WordPress vulnerabilities were found in 2025",
                "sub": "Share of 11,334 new vulnerabilities",
                "labels": ["Plugins", "Themes", "WordPress core"],
                "values": [91, 9, 0.1],
                "highlight": [0],
                "y_label": "Percent",
                "note": "Source: Patchstack, State of WordPress Security in 2026 (core: 6 vulnerabilities)",
                "alt": "Column chart showing most WordPress vulnerabilities are in plugins, relevant to website maintenance for Houston businesses",
                "caption": "Fewer, better plugins cut more risk than any security add-on.",
            },
            "security": {
                "type": "stats",
                "title": "Why WordPress updates can’t wait",
                "stats": [["11,334", "new WordPress ecosystem vulnerabilities in 2025"], ["46%", "had no fix when they were made public"], ["5 hrs", "median time to mass exploitation"], ["Dec 31", "2026 end of PHP 8.2 security support"]],
                "note": "Sources: Patchstack 2026 report, php.net",
                "alt": "Stats on WordPress security and PHP end of life that drive website maintenance costs in Houston and The Woodlands",
                "caption": f"From {SRC['patch']} and {SRC['php']}.",
            },
            "decay": {
                "type": "steps",
                "title": "How an unmaintained site decays",
                "sub": "A typical WordPress site with no one assigned to it",
                "steps": [["Months 1-3", "Looks fine. Plugin updates start piling up."], ["Months 4-6", "A form stops sending after an auto-update. Nobody notices."], ["Months 7-12", "Speed slips; an outdated plugin has a public vulnerability."], ["Year 2", "Host forces a PHP upgrade. Old theme breaks the layout."], ["Any time", "Hack: spam pages, redirects, a Google warning."]],
                "note": "Illustrative example",
                "alt": "Timeline of what breaks on an unmaintained small business website in Houston and The Woodlands",
                "caption": "Not every site follows this path. Most neglected ones we inherit are somewhere on it.",
            },
            "logins": {
                "type": "checklist",
                "title": "Logins your business should own",
                "sub": "Vendors get their own user accounts, never your password",
                "items": ["Domain registrar, with auto-renew on", "Hosting account or website builder account", "WordPress admin (your own administrator user)", "DNS provider, if separate from the registrar", "Business email admin (Google Workspace or Microsoft 365)", "Google Analytics and Search Console", "Google Business Profile", "Backup storage and any paid plugin licenses"],
                "alt": "Checklist of website logins a Houston or The Woodlands small business should own instead of its web designer",
                "caption": "Two people at your company should be able to open every one of these.",
            },
            "diy": {
                "type": "compare",
                "title": "DIY maintenance vs. a care plan",
                "left": {"title": "Doing it yourself", "items": ["Lowest cash cost", "Updates when you remember", "Backups on the host only, often", "Find broken forms when leads dry up", "Hack cleanup billed by the hour"]},
                "right": {"title": "A tested care plan", "items": ["$100 to $350 a month, typically", "Weekly updates, tested on staging", "Off-site backups with 30 days of history", "Monthly form and call-tracking tests", "Fixes and cleanup included or capped"]},
                "alt": "Comparison of DIY website maintenance and an agency care plan for small businesses in Houston and The Woodlands",
                "caption": "On Squarespace or Wix, the left column is usually fine. On WordPress, it depends on you.",
            },
        },
    },
]
