"""Batch 17 (module d): a hurricane season crisis playbook for Houston and The Woodlands businesses, a RODEOHOUSTON
season marketing calendar, and a data story on Houston's 2027 growth corridors.

Research (hurricane): NOAA May 21, 2026 outlook release (season June 1 to November 30; 8-14 named storms forecast;
"It only takes one storm"); Fox Weather on the September 10 climatological peak (NHC); Texas Tribune on Beryl
(landfall near Matagorda about 4 a.m. July 8, 2024, Category 1, 80 mph; about 2.26 million CenterPoint outages;
88,000 still out July 16); Community Impact on restoration (98% by July 17); RCR Wireless on FCC data (1,335 of 4,600+
cell sites down in the six-county area July 9, more than 1,100 for lack of power); Houstonia on restaurants during the
Beryl outage (gift cards, Ninfa's Navigation closed all week, Jun's generator waitlist after the May derecho); NPR on
the NHC Harvey report (60.58 inches at Nederland, $125 billion, 68 direct deaths, 300,000+ structures flooded); Texas
State Law Library FAQ on Bus. & Com. Code 17.46(b)(27); Proskauer on the designated disaster period and penalties
($10,000 per violation, up to $250,000 sought where victims were over 65, no cost-increase exception); Google Ads
February 2024 sensitive events policy update; Google Business Profile help (Special hours up to 6 consecutive days,
Temporarily closed for 7+ days and its ranking effect); FDIC TCPA manual (emergency purposes definition, a text is a
call); Morgan Lewis on Texas SB 140; TDI roofing and insurance law page (Ins. Code 4102.163, Bus. & Com. Code 27.02,
28 TAC 21.102 websites as ads); TDI scam signs page (out-of-area contractors can't demand payment before work after a
declared disaster); Houston Permitting Center storm repair tips; Fox 26 on BBB Beryl roofing reports; SBA Aug. 28,
2024 Beryl release (22 counties, $2 million business limit, rates as low as 4%, EIDL without property damage).
Rodeo: RODEOHOUSTON Go Texan Day page (Feb. 26, 2027; 2027 Rodeo March 2-21); RODEOHOUSTON parade page (Saturday,
Feb. 27, 2027, 10 a.m.; Rodeo Run on the route); Click2Houston Oct. 29, 2026 on the 2027 parade; 93Q Country on 2027
dates (20 days; BBQ contest projected Feb. 25-27, not official); RODEOHOUSTON trail rides page (10 rides camp at
Memorial Park the Friday before the parade); Click2Houston on the 2026 BBQ contest (250+ teams, $30 adult tickets);
RODEOHOUSTON attendance page (2,621,765 in 2026; 2,735,690 record in 2025; 2,553,185 in 2024); RODEOHOUSTON 2024
economic study release ($597 million activity, 28% of 1 million+ unique attendees from outside Greater Houston);
RODEOHOUSTON park and ride page (Sawdust Park & Ride, The Woodlands Express, reservations); Houstonia on boot demand
(Republic Boot Co., Lucchese); Click2Houston on rodeo outfit budgets (Patron Western Wear); HISD blog on Go Texan Day
trail riders visiting seven southwest Houston schools; Conroe ISD 2026-27 calendar (spring break March 15-19, 2027);
RODEOHOUSTON 2024-2025 brand standards PDF (third-party logo use requires Marketing Director approval; lockups only
for official sponsors); TrademarkDir on RODEOHOUSTON registration 8209761 (April 14, 2026, classes 41 and 25).
Growth: Census Bureau March 26, 2026 county/metro release (Harris +48,695, Montgomery +30,011, Fort Bend +24,163,
Waller 5.7%, Liberty 4.4%, Houston metro +126,720); Census May 14, 2026 city release (Fulshear 21.0% to 64,630,
+11,196; Houston +11,515 to 2,397,315); Texas Tribune and Axios on Waller and Harris domestic out-migration; Houston
Chronicle on Conroe (about 115,000 in July 2024, 56,207 in 2010, No. 20 U-Haul growth city); Houston Agent Magazine on
RCLCO's 2025 and mid-2026 MPC rankings; TxDOT Grand Parkway Segment B and B-1 pages and newsroom story (184-mile loop,
B-1 about 14 miles, construction expected early 2027, completion 2032); Community Impact on Segments H, I-1 and I-2
(52.5 miles, I-69 New Caney to I-10 Baytown, May 2022); TxDOT SH 249 project sheet (Aggie Expressway, 14.8 miles,
Pinehurst to Todd Mission); Community Impact on the final SH 249 segment (Oct. 2022) and Segment 1B (March 2021);
Community Impact on TEA enrollment 2021-26 (Lamar CISD +9,208 and +23.3%, Katy ISD +6,927, Conroe ISD +4,996, Tomball
and New Caney ISD +14.9%, Splendora ISD +34.6%, HISD -25,795, Region 6 +3.8%, Region 4 -0.9%); ABC13 on Waller ISD
(9,894 to 11,467); Community Impact on Lamar CISD planning (94 active subdivisions, 55,000+ future lots).
Blocked or unverified and left out: statutes.capitol.texas.gov (permission timeout; used the State Law Library and
Proskauer), the AG's price gouging page (fetch failed), NHC climatology page (timeout; used NOAA's release and Fox
Weather), Google Ads trademark policy page (timeout; trademark section relies on the Rodeo's own brand standards and the
USPTO registration), Katy ISD 2026-27 calendar PDF (timeout), official 2027 BBQ contest dates (not yet posted),
district-wide "rodeo days" off school (none found), Brazoria County's 2025 numeric change, Katy and Magnolia city
estimates, and any rideshare, hotel or car wash demand figures for rodeo weeks (presented as our read, not data).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # hurricane post
    "noaa": A("https://www.noaa.gov/news-release/noaa-predicts-below-normal-2026-atlantic-hurricane-season", "NOAA’s 2026 outlook"),
    "peak": A("https://www.foxweather.com/extreme-weather/atlantic-hurricane-season-peak-september-10", "Fox Weather, citing the National Hurricane Center"),
    "tt_beryl": A("https://www.texastribune.org/2024/07/08/hurricane-beryl-texas-damage-updates-rain/", "The Texas Tribune"),
    "ci_beryl": A("https://communityimpact.com/houston/bay-area/weather/2024/07/16/centerpoint-entergy-restore-power-to-98-of-affected-customers-9-days-after-hurricane-beryl/", "Community Impact"),
    "rcr": A("https://rcrwireless.com/20240709/network-infrastructure/post-beryl-cellular-network-power-outages-linger", "RCR Wireless’s write-up of FCC outage data"),
    "houstonia": A("https://www.houstoniamag.com/articles/hurricane-beryl-restaurants-without-power", "Houstonia"),
    "harvey": A("https://www.npr.org/sections/thetwo-way/2018/01/25/580689546/harvey-the-most-significant-tropical-cyclone-rainfall-event-in-u-s-history", "NPR’s summary of the National Hurricane Center’s Harvey report"),
    "sll": A("https://sll.texas.gov/faqs/disaster-price-gouging/", "Texas State Law Library"),
    "proskauer": A("https://www.proskauer.com/blog/dont-mess-with-texas-price-gouging-in-the-lone-star-state", "Proskauer’s analysis of the Texas law"),
    "gsens": A("https://support.google.com/adspolicy/answer/14153911?hl=en", "Google’s sensitive events policy update"),
    "gbp_closed": A("https://support.google.com/business/answer/15300196?hl=en", "Google’s temporary closure help page"),
    "gbp_special": A("https://support.google.com/business/answer/6303076?hl=en", "Google’s special hours help page"),
    "fdic": A("https://www.fdic.gov/consumer-compliance-examination-manual/viii-5-telephone-consumer-protection-act", "the FDIC’s TCPA examination guide"),
    "sb140": A("https://www.morganlewis.com/pubs/2025/09/texas-telephone-solicitation-law-now-covers-text-messages", "Morgan Lewis’s summary of SB 140"),
    "tdi_law": A("https://www.tdi.texas.gov/Consumer/storms/roofing-and-insurance-know-the-law.html", "the Texas Department of Insurance"),
    "tdi_scam": A("https://www.tdi.texas.gov/Consumer/storms/know-signs-of-contractor-scam.html", "TDI’s contractor scam page"),
    "hpc": A("https://houstonpermittingcenter.org/news-events/storm-damage-repair-tips", "the Houston Permitting Center"),
    "bbb": A("https://www.fox26houston.com/news/bbb-roofing-scammers-hurricane-beryl-how-choose-contractors", "told Fox 26"),
    "sba": A("https://legacy.sba.gov/article/2024/08/28/sba-tops-200-million-disaster-assistance-loans-hurricane-beryl", "the SBA"),
    # rodeo post
    "gotexan": A("https://www.rodeohouston.com/go-texan-day", "RODEOHOUSTON’s Go Texan Day page"),
    "parade": A("https://www.rodeohouston.com/parade/", "the Rodeo’s parade page"),
    "k2_parade": A("https://www.click2houston.com/news/local/2026/10/29/the-voice-of-rodeohouston-named-as-2027-downtown-parade-grand-marshal/", "Click2Houston"),
    "q93": A("https://93qcountry.com/1705006/2027-houston-livestock-show-and-rodeo-dates/", "93Q Country"),
    "trail": A("https://www.rodeohouston.com/?p=329952", "the Rodeo’s trail ride page"),
    "bbq": A("https://www.click2houston.com/news/local/2026/02/23/rodeohouston-kicks-off-season-worlds-championship-bar-b-que-contest-what-to-know", "Click2Houston’s 2026 contest guide"),
    "attend": A("https://www.rodeohouston.com/about-us/attendance/", "the Rodeo’s attendance page"),
    "econ": A("https://www.rodeohouston.com/the-rodeo-drives-millions-in-annual-economic-growth-for-greater-houston-area/", "the Rodeo’s 2024 economic study"),
    "pnr": A("https://www.rodeohouston.com/plan-your-visit/park-and-ride/", "the Rodeo’s park and ride page"),
    "boots": A("https://www.houstoniamag.com/style-and-shopping/2026/02/houston-rodeo-boots-boom", "Houstonia"),
    "outfits": A("https://www.click2houston.com/news/local/2026/02/27/rodeo-outfits-can-cost-hundreds-heres-how-houston-shoppers-are-stretching-their-budgets-this-season", "told Click2Houston"),
    "hisd": A("https://blogs.houstonisd.org/news/tag/go-texan-day", "HISD’s news blog"),
    "cisd": A("https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/5052/Cisd/e83881e1-1d85-43d1-b350-7fb41cffd1c1/26-27-CISD-Calendar.pdf", "Conroe ISD’s 2026-27 calendar"),
    "brand": A("https://www.rodeohouston.com/wp-content/uploads/2025/02/2024-2025-Brand-Standards.pdf", "the Rodeo’s own brand standards"),
    "tm": A("https://trademarkdir.com/trademark/rodeohouston-99050499", "registration No. 8209761"),
    # growth post
    "census_co": A("https://census.gov/newsroom/press-releases/2026/2025-popest-metro-micro-counties.html", "Census Bureau’s March 2026 county and metro release"),
    "census_city": A("https://www.census.gov/newsroom/press-releases/2026/vintage-2025-city-town-pop-estimates.html", "Census Bureau’s May 2026 city release"),
    "tt_waller": A("https://www.texastribune.org/2026/03/26/texas-population-census-migration-waller-county/", "The Texas Tribune"),
    "axios": A("https://www.axios.com/local/houston/2026/04/02/houston-harris-population-growth-2025-census-immigration-policy", "Axios Houston"),
    "axios_ful": A("https://www.axios.com/local/houston/2026/05/21/the-great-exurban-surge-fulshear-population-growth-houston-suburbs", "Axios"),
    "chron_conroe": A("https://www.houstonchronicle.com/business/article/conroe-houston-uhaul-growth-21281932.php", "the Houston Chronicle"),
    "rclco25": A("https://houstonagentmagazine.com/2026/01/08/sunterra-houstons-top-selling-mpc/", "Houston Agent Magazine’s summary of RCLCO’s 2025 list"),
    "rclco26": A("https://houstonagentmagazine.com/2026/08/04/tamarron-houston-top-selling-mpc-mid-year-2026/", "RCLCO’s mid-year 2026 ranking"),
    "gp_b": A("https://www.txdot.gov/projects/projects-studies/houston/sh99-grand-parkway/overview/segment-b.html", "TxDOT’s Segment B page"),
    "gp_story": A("https://www.txdot.gov/about/newsroom/stories/construction-planned-for-vital-loop-around-houston.html", "TxDOT"),
    "gp_hi": A("https://communityimpact.com/houston/lake-houston-humble-kingwood/transportation/2022/05/16/txdot-grand-parkway-segments-from-new-caney-to-baytown-set-to-open-may-19", "Community Impact"),
    "sh249": A("https://www.txdot.gov/content/dam/docs/ald/cutsheets/sh249-txdot-adp-hou-district-project-sheet.pdf", "TxDOT’s project sheet"),
    "ci_249": A("https://communityimpact.com/houston/tomball-magnolia/transportation/2022/10/28/final-segment-of-hwy-249-opens-to-drivers", "Community Impact"),
    "ci_tea": A("https://communityimpact.com/new-caney-porter/education/data-most-greater-houston-area-school-districts-saw-enrollment-losses-from-2021-26/", "Community Impact’s look at TEA enrollment data"),
    "waller_isd": A("https://abc13.com/post/waller-independent-school-district-experiences-application-backlog-county-grows/19679258/", "ABC13"),
    "lamar": A("https://communityimpact.com/katy-fulshear/education/data-informed-student-centered-how-lamar-cisd-is-planning-for-nearly-2000-new-students-annually-by-2034/", "Community Impact"),
}

HURRICANE = "/blog/hurricane-season-marketing-playbook-houston-the-woodlands/"
RODEO = "/blog/rodeo-season-marketing-houston-the-woodlands/"
GROWTH = "/blog/houston-growth-corridors-new-customers-2027/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: hurricane crisis playbook
    {
        "slug": "hurricane-season-marketing-playbook-houston-the-woodlands",
        "title": "Hurricane Season Marketing Playbook for Houston and The Woodlands Businesses",
        "seo_title": "Hurricane Marketing Playbook for Houston & The Woodlands",
        "desc": "A phase-by-phase hurricane playbook for Houston and The Woodlands businesses: Google hours, pausing ads, texts, price gouging law and recovery tone.",
        "category": "Strategy",
        "icons": ["Google Business Profile", "Google Ads", "Meta"],
        "art": "b4",
        "hero": "shield",
        "hero_alt": "Illustration of a shield for a hurricane season marketing playbook for Houston and The Woodlands businesses",
        "related": ["roofing-marketing-houston-storm-season", "sms-marketing-small-business-texas-rules", "google-business-profile-number-one-asset"],
        "sections": [
            (None, f"""<p>2.26 million. That’s roughly how many CenterPoint customers lost power after Hurricane Beryl came ashore near Matagorda around 4 a.m. on July 8, 2024, as a Category 1, per {SRC['tt_beryl']}. Eight days later, 88,000 were still in the dark.</p>
<p>Plenty of Houston and The Woodlands businesses learned something that week. Their marketing kept running on autopilot while their doors were locked. Scheduled Instagram posts went out about summer specials, and the Google profile said “Open” to people driving around looking for ice. A few email tools fired off a “Hot deals this week!” blast to customers sitting in 90-degree living rooms.</p>
<p>This is the playbook we wish every client had taped inside the supply closet. It runs in four phases: the 72 hours before a storm, the storm itself, the first week after, and the recovery that follows. Each phase has a short list of marketing moves, a few legal lines you can’t cross, and the mistakes we watched people make after Beryl and Harvey.</p>
<p>One rule sits above all of it. People first. No post, ad or text matters more than your staff getting home before the roads close.</p>
<!--fig:phases-->"""),

            ("Hurricane season dates for Houston, and why you plan in May", f"""<p>The Atlantic hurricane season runs June 1 to November 30, per {SRC['noaa']}. The statistical peak is around September 10, and about 60% of an average season’s activity still lies ahead on that date, according to {SRC['peak']}. Beryl was a July storm. Harvey hit in late August. Ike was September. Houston doesn’t get a safe month in there.</p>
<p>NOAA’s May 2026 forecast leaned below normal, with 8 to 14 named storms expected. The National Weather Service director’s line in the same release is the one to remember: “It only takes one storm to make for a very bad season.”</p>
<p>So the prep work belongs in May, when nobody is scared and you can think straight. Build your templates then. Write down who owns which login and test the text platform. A single afternoon of that saves you from writing a closure notice by phone flashlight.</p>"""),

            ("Phase 1: the 72 hours before landfall", f"""<p>Once the National Hurricane Center’s cone includes the Houston area, you usually have a few days. Use them in this order.</p>
<!--fig:prep72-->
<p><b>Staff first.</b> Decide your closure trigger now (we like “if Harris or Montgomery County schools close, we close”) and tell staff before customers. Nobody should hear about their own day off from your Instagram story.</p>
<p><b>Google Business Profile.</b> Pre-load special hours for the likely closure days. In the profile, go to <i>Edit profile</i>, then <i>Hours</i>, then <i>Special hours</i>, and add each date. Google’s rule is that special hours cover changes of up to six consecutive days; anything seven days or longer, or open-ended, should use <i>Temporarily closed</i> instead, per {SRC['gbp_special']}. Set them early. You may not have power or signal to do it later.</p>
<p><b>Ads.</b> Make the pause list now. Which campaigns stop the moment you close, which keep running, and which change their message (more on that in the ads section below). Write down who has access to Google Ads and Meta Ads Manager on a phone, because the office desktop will be dark.</p>
<p><b>Scheduled content.</b> Open your social scheduler and your email platform and look at everything set to publish in the next ten days. Pause all of it. This is the single most common mistake we see, and it takes four minutes to prevent.</p>
<p><b>Customer message.</b> Send one clear note to customers who expect to hear from you: appointments, pickups, deliveries, reservations. Say what happens to their booking, and how you’ll tell them when you reopen. Keep the sales pitch out of it.</p>
<p>If you sell plywood, generators, water, fuel or hotel rooms, Phase 1 is also when the price gouging law starts mattering. That gets its own section.</p>"""),

            ("Phase 2: during the storm, say less", f"""<p>While the storm is overhead, your marketing job is small. Keep the profile accurate and keep the channels quiet.</p>
<p>Post one short update when you close, pinned to the top of Facebook and Instagram, and the same text as a Google Business Profile update. Then stop. Every brand in Houston posting “Stay safe, Houston!” with a stock photo of clouds adds nothing, and some people will remember who was selling during the worst night of their summer.</p>
<p>Expect your own communication to break. During Beryl, FCC data showed 1,335 of more than 4,600 cell sites in the six-county disaster area out of service on July 9, more than 1,100 of them because they had no commercial power, per {SRC['rcr']}. Texts you schedule may not land. Customers may not see your posts for days. That’s why the profile, the website banner and a sign taped inside the front window all need to say the same thing.</p>
<p>A few things that are fine during the storm:</p>
<ul>
<li>Sharing official information from the National Weather Service, county emergency offices or your city, if your audience follows you for local news.</li>
<li>Answering direct messages from customers about their orders, appointments or deposits.</li>
<li>Telling people where your staff and customers can find help, if you know it’s accurate.</li>
</ul>
<p>Stay away from jokes and promotions during the storm, and don’t post any storm photo that shows someone else’s damaged property.</p>"""),

            ("Pausing or adjusting Google Ads and Meta ads in a hurricane", f"""<p>There’s no single right answer here. It depends on what you sell and whether you can actually deliver it this week.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Business type</th><th>During the storm</th><th>First week after</th></tr></thead>
<tbody>
<tr><td>Restaurant, retail, salon, gym, studio</td><td>Pause everything</td><td>Resume when open, with “we’re open” copy and real hours</td></tr>
<tr><td>Roofing, tree service, water damage, restoration</td><td>Pause or cap budgets if crews can’t safely roll</td><td>Run, but only in ZIPs you can serve this week, with honest response times</td></tr>
<tr><td>HVAC, electrical, plumbing, generator installers</td><td>Keep emergency call campaigns only if phones are staffed</td><td>Raise budgets carefully; schedule ads to staffed hours</td></tr>
<tr><td>Hotels and short-term rentals</td><td>Keep brand search, drop promo offers</td><td>Show availability, keep rates stable, see the pricing section</td></tr>
<tr><td>B2B, professional services, ecommerce</td><td>Pause local campaigns</td><td>Resume gradually; Houston buyers are distracted for a while</td></tr>
</tbody></table></div>
<p>In Google Ads, select the campaigns under <i>Campaigns</i>, then use <i>Edit</i> and <i>Pause</i>. If you serve a wide area and only part of it got hit, you can keep running and exclude the worst-hit ZIP codes under <i>Locations</i> instead. Add a temporary ad schedule that matches the hours you actually have someone answering phones. Paused campaigns keep their history; we’d rather pause for five days than spend money sending calls to a voicemail that’s full.</p>
<p>In Meta Ads Manager, toggle off the campaigns, then check the <i>Ads</i> tab for anything boosted from a post. Boosted posts are the ones people forget.</p>
<p>Google also has rules about what storm-related ads can say. Its sensitive events policy, updated in February 2024, names natural disasters as an example and bars ads that “exploit, dismiss, or condone” the event, including price gouging or artificially inflating prices on vital supplies, per {SRC['gsens']}. Ads can get disapproved for copy that reads like it’s cashing in. If you’re a restoration company, “24/7 water extraction, licensed and insured, local crews” is a service ad. “Hurricane SALE! Don’t miss out!” is the kind of thing that gets flagged.</p>
<p>Our {L('/services/search-marketing/', 'search marketing team')} builds this pause-and-resume plan into accounts before June, so it’s a two-minute job when the cone shifts.</p>"""),

            ("Customer texts and emails: what the rules allow", f"""<p>Texting customers that you’re closed tomorrow feels harmless, and usually it is. The legal details still matter, because storm weeks are when businesses text people they’ve never texted before.</p>
<p>Under the federal TCPA, a text counts as a “call,” and calls made for “emergency purposes” are treated differently. The definition is narrow: “calls made necessary in any situation affecting the health and safety of consumers,” as the FDIC’s summary puts it in {SRC['fdic']}. A boil-water notice from a utility fits that. Your “we’re closed Tuesday” text to existing customers is an informational message about their own business with you. Your “storm prep sale” text is marketing and needs the same consent as any other marketing text.</p>
<p>Texas adds its own layer. SB 140, effective September 1, 2025, brought marketing texts under the state’s telephone solicitation law, with a registration requirement and a private right of action, plus exemptions that include some current-customer and physical-store situations, per {SRC['sb140']}. We cover the practical side in our {L('/blog/sms-marketing-small-business-texas-rules/', 'guide to SMS marketing rules in Texas')}. Ask your attorney before storm season which of your messages are which.</p>
<p>Our working rules for storm messaging:</p>
<ol>
<li>Send closure and reopening notices only to people who have an active relationship with you (bookings, orders, memberships, open jobs).</li>
<li>Keep operational messages free of offers. One coupon line turns an update into an ad.</li>
<li>Send one message per phase. Closing, reopening, and maybe one “we’re back to normal hours” note.</li>
<li>Email is your fallback when texts may not deliver. Send the same content to both.</li>
<li>Anyone who replies STOP gets removed that hour, storm or not.</li>
</ol>
<!--fig:comms-->"""),

            ("Price gouging in Texas: the DTPA rule during a declared disaster", f"""<p>This is the part business owners underestimate. Texas makes it a deceptive trade practice to sell or lease fuel, food, medicine, lodging, building materials, construction tools or another necessity at an exorbitant or excessive price during a disaster declared by the governor or the president. That’s Section 17.46(b)(27) of the Business and Commerce Code, summarized by the {SRC['sll']}.</p>
<p>A few details from {SRC['proskauer']} matter for marketing:</p>
<ul>
<li>The “designated disaster period” starts at the earliest of the disaster itself, the governor’s declaration or a presidential declaration. Don’t assume the clock starts at landfall.</li>
<li>The law also covers <i>demanding</i> an excessive price, so a price posted in an ad or on your website can be the problem even before anything sells.</li>
<li>“Exorbitant or excessive” isn’t defined, and unlike many states, Texas has no written exception for your own higher costs.</li>
<li>Civil penalties run up to $10,000 per violation, and the Attorney General has sought up to $250,000 more where victims were over 65. Buyers can also sue.</li>
</ul>
<p>What that means in practice: if you sell anything on that list, freeze your online prices and promo codes when a declaration lands, and don’t launch “surge” pricing on generators, tarps, water or rooms. If your supplier costs genuinely jump, document them and talk to a lawyer before changing a price tag. For hotels, a stable rate posted on your site is good for your reputation and keeps you clear of the law.</p>
<p>We’re marketers. None of this is legal advice, and the statute is short enough that your attorney can read it in five minutes.</p>"""),

            ("Phase 3: the first week after, and the storm-chaser contractor rules", f"""<p>The first week is about two things: telling people accurately if you’re open, and not looking like the out-of-town crews that show up after every storm.</p>
<p><b>Reopening.</b> If you used special hours, delete them or replace them with real hours. If you marked the profile temporarily closed, reopen it the day you open the doors. Google says temporarily closed businesses can rank below open ones for broad searches, per {SRC['gbp_closed']}. After Beryl, “open near me” searches were how people found ice, gas, hot food and a place to charge a phone. If you were open and your profile said otherwise, you lost those customers to whoever had kept theirs current.</p>
<p>Then post a plain update with what’s running and what isn’t. “Open 10 to 6, kitchen running, AC on, outlets at every table” is a better post than anything a copywriter would write that week.</p>
<p><b>Contractors.</b> If you’re a roofer, tree service, remodeler or restoration company, your ads are about to compete with storm chasers, and Texas has specific rules your marketing must follow.</p>
<!--fig:contractor-->
<p>From {SRC['tdi_law']}: a contractor can’t act as a public insurance adjuster on a job it’s doing, and can’t advertise to adjust claims (Insurance Code 4102.163). Websites count as advertising. Promising to “get every dime you are owed” or offering to negotiate the claim are listed examples of what crosses the line. Contractors also can’t offer to waive, rebate or absorb a policyholder’s deductible (Business and Commerce Code 27.02), and contracts of $1,000 or more involving an insurance settlement must include a notice that the homeowner pays the deductible. TDI adds that after a declared disaster, it’s against the law for out-of-area contractors to demand payment before starting work, per {SRC['tdi_scam']}.</p>
<p>Inside Houston city limits, {SRC['hpc']} notes general contractors don’t need a license, but electrical, mechanical and plumbing contractors must be registered with the city and licensed by the state, and pull permits for repairs. Tarping and most fence replacements under 8 feet don’t need a permit. After Beryl, a BBB spokesperson {SRC['bbb']} the bureau was seeing complaints and scam reports, often homeowners who paid upfront and never saw the contractor again.</p>
<p>The marketing play for local contractors is simple: be visibly local. Show a real street address on your Google profile, photos of your own trucks, and your license numbers where they apply. Mention years in Montgomery or Harris County. Write “we’ll inspect and give you a written estimate; you file your own claim” instead of anything that sounds like claim handling. Our {L('/blog/roofing-marketing-houston-storm-season/', 'roofing storm season guide')} goes deeper on the ad side.</p>"""),

            ("Phase 4: recovery marketing tone for Houston", f"""<p>Recovery can last weeks. Harvey was a different scale than Beryl: up to 60.58 inches of rain at Nederland, more than 300,000 structures flooded in southeast Texas, an estimated $125 billion in damage and at least 68 direct deaths, per {SRC['harvey']}. After that kind of event, some of your customers are rebuilding houses while you’re trying to sell them brunch.</p>
<p>A few tone rules we hold to:</p>
<!--fig:tone-->
<p><b>Talk about what you’re doing, and skip how you feel about it.</b> “We’re donating 10% of this week’s sales to [a specific local relief group]” beats “Our hearts are with Houston.” If you do give, name the group and post the receipt later.</p>
<p><b>Let loyal customers help if they want to.</b> During the Beryl outage, Cochinita &amp; Co. in the East End sold about $1,000 in gift cards in its first hour of asking, per {SRC['houstonia']}. The same piece reported Original Ninfa’s on Navigation was closed all week with projected losses over $150,000, and that Jūn had joined a generator waitlist after the May 2024 derecho. Asking for gift card support is fine when it’s honest about why.</p>
<p><b>Ease back into promotions.</b> We usually wait until most of the metro has power before running anything that looks like a sale. For Beryl, CenterPoint said it expected to restore 98% of affected customers by July 17, nine days after landfall, per {SRC['ci_beryl']}. That’s a reasonable marker for when normal marketing can resume in most of Houston, though hard-hit areas take longer.</p>
<p><b>Point people to real help.</b> After Beryl, {SRC['sba']} offered disaster loans in 22 Texas counties, including Harris, Montgomery, Fort Bend, Brazoria, Waller and Liberty. Businesses could borrow up to $2 million for physical damage at rates as low as 4%, and economic injury loans were available even without property damage. If your own business took a hit, that’s worth knowing too.</p>
<!--fig:sbamap-->"""),

            ("Lessons from Beryl and Harvey we now build into every plan", f"""<p>We’ve watched Houston and The Woodlands businesses get through enough storms to have opinions.</p>
<!--fig:numbers-->
<ul>
<li><b>Assume no power and spotty signal for a week.</b> Beryl made that real for a lot of suburbs. Your plan has to work from a phone on a car charger.</li>
<li><b>Logins live in two places.</b> One owner and one manager can get into Google Business Profile, Google Ads, Meta, the website and the email platform from their phones, with two-factor codes going to two different people.</li>
<li><b>The Google profile is your storm website.</b> People check Maps before they check your site. Accurate hours there are worth more than any post.</li>
<li><b>Scheduled content is the biggest self-inflicted wound.</b> Pause it at the first watch.</li>
<li><b>Know your pricing line in advance.</b> Write down the price list you’ll hold during a declared disaster before one happens.</li>
<li><b>Recovery is when trust is built.</b> In our experience, the businesses people talk about after a storm are the ones that opened early with honest hours, fed crews, or let people charge phones. None of that was an ad.</li>
</ul>
<p>Our {L('/blog/google-business-profile-number-one-asset/', 'Google Business Profile guide')} covers the profile basics, and {L('/blog/seasonal-marketing-greater-houston/', 'seasonal marketing in Greater Houston')} has the rest of the calendar. If you’d like a senior strategist to build your storm plan (logins, templates, ad pause lists and all), <a href="/contact/">get in touch</a> and tell us how your business runs.</p>"""),
        ],
        "faq": [
            ("When is hurricane season in Houston and The Woodlands?",
             "NOAA’s Atlantic hurricane season runs June 1 to November 30. The statistical peak is around September 10, but Houston has been hit in July (Beryl in 2024), late August (Harvey in 2017) and September (Ike in 2008). Build your marketing storm plan in May, while things are calm, so templates, logins and ad pause lists are ready before the first storm enters the Gulf."),
            ("Should I mark my Google Business Profile temporarily closed during a hurricane?",
             "Use special hours if you expect to be closed six days or fewer, and switch to temporarily closed only if the closure will be seven days or longer or has no set end. Google says temporarily closed businesses can rank below open ones for broad searches, so reopen the profile the same day you reopen. Set special hours before landfall, because you may lose power and signal afterward."),
            ("Is it legal to raise prices in Texas after a hurricane?",
             "During a disaster declared by the governor or president, Texas law prohibits selling or demanding exorbitant or excessive prices for fuel, food, medicine, lodging, building materials, construction tools and other necessities. Civil penalties can reach $10,000 per violation. The law has no written exception for higher costs, so freeze advertised prices and talk to a lawyer before changing them during a declared disaster."),
            ("Should a Houston business pause Google Ads during a hurricane?",
             "Most restaurants, retailers, salons and studios should pause all ads while closed and resume with real hours once open. Emergency service businesses like HVAC, restoration and tree service can keep running, but only in areas they can serve and only during staffed hours. Avoid copy that looks like it profits from the storm, since Google’s sensitive events policy can disapprove it."),
            ("Can contractors in Texas waive a homeowner’s insurance deductible after a storm?",
             "No. Texas Business and Commerce Code 27.02 bars contractors from offering to waive, rebate or absorb a deductible, and contracts of $1,000 or more involving an insurance settlement must state that the homeowner pays it. Contractors also can’t act as public adjusters or advertise claim handling. After a declared disaster, out-of-area contractors can’t demand payment before starting work, according to the Texas Department of Insurance."),
        ],
        "figures": {
            "phases": {
                "type": "steps",
                "title": "The four phases of a hurricane marketing plan",
                "sub": "What to do, in order, from the first cone to the last cleanup crew",
                "steps": [["72 hours before", "Staff plan, special hours set, ads and scheduled posts paused, one customer notice."], ["During the storm", "One pinned update, profile accurate, answer DMs, no promos."], ["First week after", "Reopen the profile, post real hours, restart ads only where you can serve."], ["Recovery", "Give specifically, ease back into offers once most of the metro has power."]],
                "alt": "Four-phase hurricane season marketing plan for Houston and The Woodlands businesses from 72 hours before landfall to recovery",
                "caption": "Write each phase’s tasks down in May, with a name next to every one.",
            },
            "prep72": {
                "type": "checklist",
                "title": "72-hour hurricane checklist for marketing",
                "sub": "Houston and The Woodlands businesses, before landfall",
                "items": ["Closure trigger decided and staff told first", "Special hours loaded in Google Business Profile", "Website banner drafted with closure dates", "Scheduled social posts and emails paused", "Ad pause list ready, with phone logins tested", "Boosted Meta posts checked and turned off", "One customer notice sent: bookings and next steps", "Price list locked if you sell necessities", "Sign printed for the front window"],
                "alt": "Checklist of hurricane preparation marketing tasks for Houston and The Woodlands businesses in the 72 hours before a storm",
                "caption": "Every item here works from a phone. That’s the point.",
            },
            "comms": {
                "type": "funnel",
                "title": "Who hears from you, in what order",
                "stages": [["Staff and their families", "First"], ["Customers with bookings or open jobs", "Second"], ["Google profile, website banner, door sign", "Same hour"], ["Social media update, pinned", "Then"], ["Ads and promotions", "Last"]],
                "alt": "Order of hurricane communications for Houston and The Woodlands businesses from staff to customers to ads",
                "caption": "Ads come last because they reach strangers. Everyone above them has a stake in what you do this week.",
            },
            "contractor": {
                "type": "compare",
                "title": "Storm contractor ad copy in Texas",
                "left": {"title": "Crosses the line", "items": ["“We handle your insurance claim”", "“We’ll get every dime you’re owed”", "“We’ll cover your deductible”", "Payment demanded before work starts", "No local address anywhere"]},
                "right": {"title": "Stays inside it", "items": ["“Free inspection and written estimate”", "“You file your claim, we document the damage”", "Deductible notice in every contract", "Payments tied to work milestones", "Real address, trucks and license numbers"]},
                "alt": "Comparison of illegal and compliant storm contractor advertising language in Houston and Texas after a hurricane",
                "caption": f"Rules summarized from {SRC['tdi_law']} and {SRC['tdi_scam']}.",
            },
            "tone": {
                "type": "compare",
                "title": "Recovery tone: what reads badly and what works",
                "left": {"title": "Reads badly", "items": ["“Hurricane sale!” during outages", "Stock photos of storm clouds", "“Our hearts are with Houston” and nothing else", "Photos of customers’ damaged homes", "Promo codes in closure texts"]},
                "right": {"title": "Works", "items": ["Honest hours and what’s running", "Photos of your actual open doors", "A named relief group and a real number", "Help with charging, water, food if you can", "Promotions after most power is back"]},
                "alt": "Comparison of hurricane recovery marketing tone for Houston and The Woodlands businesses",
                "caption": "Recovery posts work best when they read like a neighbor wrote them.",
            },
            "sbamap": {
                "type": "map",
                "title": "Beryl’s SBA disaster area covered the whole metro",
                "sub": "Places in counties named in the SBA’s Aug. 2024 Beryl declaration (Harris, Montgomery, Fort Bend, Brazoria, Waller, Liberty, Galveston and more)",
                "highlight": ["The Woodlands", "Conroe", "Katy", "Cypress", "Sugar Land", "Pearland", "Kingwood", "League City", "Baytown", "Fulshear", "Tomball", "Magnolia"],
                "alt": "Map of Houston and The Woodlands area places in counties covered by the SBA Hurricane Beryl disaster declaration",
                "caption": f"County list from {SRC['sba']}. A storm plan has to assume every location is affected at once.",
            },
            "numbers": {
                "type": "stats",
                "title": "Beryl and Harvey by the numbers",
                "stats": [["2.26M", "CenterPoint outages after Beryl"], ["1,335", "cell sites down in the six-county area, July 9, 2024"], ["60.58\"", "Harvey’s peak rainfall, Nederland"], ["$125B", "Harvey damage estimate"]],
                "note": "Source: Texas Tribune, FCC data via RCR Wireless, NHC via NPR",
                "alt": "Statistics on Hurricane Beryl power and cell outages and Hurricane Harvey rainfall and damage in the Houston area",
                "caption": f"From {SRC['tt_beryl']}, {SRC['rcr']} and {SRC['harvey']}.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: rodeo season calendar
    {
        "slug": "rodeo-season-marketing-houston-the-woodlands",
        "title": "Rodeo Season Marketing for Houston and The Woodlands Businesses: The 2027 Calendar",
        "seo_title": "Rodeo Season Marketing Calendar: Houston & The Woodlands",
        "desc": "Rodeo season marketing for Houston and The Woodlands businesses: 2027 RODEOHOUSTON dates, a week-by-week calendar, ad timing and trademark cautions.",
        "category": "Local marketing",
        "icons": ["Instagram", "TikTok", "Google Ads"],
        "art": "b3",
        "hero": "ticket",
        "hero_alt": "Illustration of a ticket for rodeo season marketing for Houston and The Woodlands businesses",
        "related": ["seasonal-marketing-greater-houston", "restaurant-marketing-the-woodlands-houston", "boutique-retail-store-marketing-the-woodlands"],
        "sections": [
            (None, f"""<p>“Should we do something for the rodeo?” A Woodlands restaurant owner asked us that in the second week of March one year. By then the answer was mostly no. The boots had been bought, the group dinners booked, and every Instagram feed in Houston was already wall-to-wall fringe.</p>
<p>RODEOHOUSTON is the biggest stretch of the year for a long list of Houston and The Woodlands businesses, and most of the money moves before opening day. This post is a calendar. Dates first, then a week-by-week plan running from January through the last concert, then what tends to spike and the trademark line you shouldn’t cross.</p>
<p>All dates below are for 2027. Where the Rodeo hadn’t confirmed a date when we wrote this, we say so.</p>"""),

            ("RODEOHOUSTON 2027 dates and the pre-rodeo events", f"""<p>The 2027 Houston Livestock Show and Rodeo runs <b>Tuesday, March 2 through Sunday, March 21</b>, per {SRC['gotexan']}. That’s a 20-day run, one day shorter than 2026, per {SRC['q93']}.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Event</th><th>2027 date</th><th>Status</th></tr></thead>
<tbody>
<tr><td>World’s Championship Bar-B-Que Contest</td><td>Expected Thu.-Sat., Feb. 25-27</td><td>Not yet official; it runs the weekend before opening day</td></tr>
<tr><td>Go Texan Day and Rodeo Roundup (downtown, 11 a.m. to 1 p.m.)</td><td>Friday, Feb. 26</td><td>Confirmed on the Rodeo’s site</td></tr>
<tr><td>Trail rides arrive and camp at Memorial Park</td><td>Friday, Feb. 26</td><td>Follows the Friday-before-parade pattern</td></tr>
<tr><td>Downtown Rodeo Parade (10 a.m.) and Rodeo Run</td><td>Saturday, Feb. 27</td><td>Confirmed on the Rodeo’s site</td></tr>
<tr><td>RODEOHOUSTON at NRG Park</td><td>Tuesday, March 2 to Sunday, March 21</td><td>Confirmed</td></tr>
<tr><td>Conroe ISD spring break</td><td>March 15-19</td><td>Confirmed on the district calendar</td></tr>
</tbody></table></div>
<p>The parade date comes from {SRC['parade']} and {SRC['k2_parade']}. Ten trail rides gather and camp at Memorial Park the Friday before the parade, per {SRC['trail']}. The barbecue contest drew more than 250 teams in 2026, with adult tickets at $30, per {SRC['bbq']}. For 2027 it’s widely expected on Feb. 25-27, but check rodeohouston.com before you print anything with that date on it.</p>
<p>Spring break matters for planning. {SRC['cisd']} puts it at March 15-19, the third week of the Rodeo. Check your local district too, since a family weekday at NRG Park looks a lot like a family weekday at your trampoline park.</p>
<!--fig:calendar-->"""),

            ("How big rodeo season is for Houston businesses", f"""<p>The scale is the reason to plan. Total grounds attendance was 2,621,765 in 2026, after a record 2,735,690 in 2025, per {SRC['attend']}.</p>
<!--fig:attendance-->
<p>The Rodeo’s 2024 economic study, done by Economics Analytics Consulting, put total economic activity in Greater Houston at $597 million, and found 28% of the more than one million unique attendees came from outside Greater Houston, per {SRC['econ']}. That 28% sleeps somewhere, eats somewhere and buys a hat somewhere.</p>
<!--fig:stats-->
<p>Most of it isn’t spent at NRG Park. It’s spent on the way there and in the weeks before: outfits, group dinners, a car detail before date night, a hotel near the Medical Center for the cousins from Lufkin.</p>"""),

            ("What spikes during rodeo season, and when", f"""<p>Here’s our read on who sees a lift, built from public reporting where it exists and from patterns we’ve watched in Houston accounts. Use it as a starting hypothesis and check it against your own last two years of sales.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Business</th><th>When demand moves</th><th>What people search or ask for</th></tr></thead>
<tbody>
<tr><td>Western wear, boots, hats</td><td>Mid-January to the first week of March</td><td>“western wear near me,” “cowboy boots The Woodlands,” “rodeo outfit”</td></tr>
<tr><td>Restaurants and bars</td><td>Group bookings from early February; pre-concert dinners all three weeks</td><td>“restaurants near NRG,” “brunch before rodeo,” group menus</td></tr>
<tr><td>Hotels</td><td>Concert nights and the out-of-town weekends</td><td>“hotels near NRG Park,” brand searches on concert dates</td></tr>
<tr><td>Rideshare, party buses, limo</td><td>Concert nights, especially weekends</td><td>“party bus to rodeo,” “limo Houston rodeo”</td></tr>
<tr><td>Car washes and detailers</td><td>The week before the BBQ contest and parade; after trail rides</td><td>Truck and trailer washes, “detail near me”</td></tr>
<tr><td>Salons, lash and brow, barbers</td><td>The two weeks before Go Texan Day and big concert nights</td><td>Blowouts, braids, “rodeo hair”</td></tr>
<tr><td>Event rental, catering, BBQ</td><td>Late January through Go Texan Day</td><td>Office Go Texan parties, cook-off supplies</td></tr>
</tbody></table></div>
<p>Western wear is the clearest case. Republic Boot Co. in the Heights estimates boot sales reach the thousands in the weeks before the Rodeo, its busiest season, and a Lucchese executive called rodeo season the “bread and butter” of its selling year, per {SRC['boots']}. A co-owner of Patron Western Wear {SRC['outfits']} in 2026 that customers who used to spend $500 on boots alone are now spreading the same $500 across a full outfit, and advised shopping before the grounds, where prices run high. That shopper is planning a whole look. Sell it to them as one.</p>
<p>Restaurants have a different window. Office groups book Go Texan Day lunches in early February. Concert-night dinners spread across all three weeks, with Friday and Saturday filling first. For The Woodlands, the Township’s Woodlands Express runs a rodeo park and ride from the Sawdust lot at 701 Westridge Drive with reservations required, per {SRC['pnr']}. Restaurants near Sawdust and I-45 can market a “dinner, then the bus” night out.</p>"""),

            ("Week-by-week rodeo marketing calendar for Houston and The Woodlands", f"""<p>Here’s the calendar we’d run, keyed to the 2027 dates. Shift a week either way depending on how your customers buy.</p>
<p><b>Early to mid-January: plan and shoot.</b> Lock offers, book the photo or video shoot (real staff in real boots beats stock every time), and set up landing pages. If you want rodeo-themed Google Ads, write them now so they clear review before demand starts. Pull last year’s February and March numbers by week.</p>
<p><b>Last two weeks of January: start the early buyers.</b> Western wear and salons start social ads and email. Restaurants announce group menus for Go Texan Day and concert nights. Event rental and caterers reach out to HR managers at offices along Research Forest, Hughes Landing and the Energy Corridor, since Go Texan Day parties get planned now.</p>
<p><b>Feb. 1 to 21: the heaviest spend.</b> This is when outfits get bought and dinners get booked. Raise budgets on Meta and Google, push Instagram Reels and TikTok, and run local search ads on “western wear near me”-type terms. Restaurants should have reservation links on the Google Business Profile and in every post.</p>
<p><b>Feb. 22 to 28: kickoff week.</b> BBQ contest, Go Texan Day on Friday the 26th, trail rides into Memorial Park, parade Saturday the 27th. Post daily. Run Go Texan Day offers (“wear your boots, get [your offer]”). Car washes and detailers push truck and trailer washes.</p>
<p><b>March 2 to 21: the run.</b> Shift from “get ready” to “before and after.” Pre-concert dinner, late-night food, recovery brunch, rideshare and party bus bookings. Watch the concert lineup and add budget around the headliners your customers care about. Spring break, March 15-19, brings families out on weekdays.</p>
<p><b>March 22 onward: after.</b> Clearance on western wear. A thank-you post with customer photos (with permission). Tag and save the content you’ll reuse next January, and write down what sold out early.</p>
<p>The figure at the top of this post shows the same calendar in six blocks. Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing guide')} covers the rest of the year around it.</p>"""),

            ("Local ad timing: Google, Meta, TikTok and the rest", f"""<p>A few timing rules that apply across channels in rodeo season.</p>
<ul>
<li><b>Meta and Instagram</b> need a two to three week runway to build frequency in a tight radius. Start in late January, not the day before Go Texan Day. Radius around your store, around 10 to 15 miles in the suburbs, smaller inside the Loop.</li>
<li><b>TikTok</b> works for outfit content and restaurant “where to eat before the rodeo” posts. Organic first; boost what already got traction.</li>
<li><b>Google Search</b> catches people who already decided. Bid on your category plus “near me” and town names (Spring, Conroe, Katy, Cypress, Sugar Land), and add negatives for “tickets,” “lineup,” “schedule,” “livestock show results” and “jobs,” which pull rodeo fans you can’t sell to.</li>
<li><b>Google Business Profile</b> posts and photos need refreshing in early February so Maps shows your rodeo inventory or menu, not your Christmas window.</li>
<li><b>Streaming TV and radio</b> are expensive in February because everyone wants rodeo season. If you buy them, book in December. Our {L('/blog/radio-tv-advertising-cost-houston/', 'Houston radio and TV cost guide')} has ranges.</li>
</ul>
<p>Budget-wise, we’d put most of a small business’s rodeo spend into February. A rough pattern we use for planning (illustrative, not a benchmark) is about 15% in late January, 55% across February, 25% during the run, and 5% for after. The run itself is crowded and expensive, and much of the buying is done.</p>
<!--fig:budget-->"""),

            ("Trademark caution: rodeo logos and “official” claims", f"""<p>This is where local businesses get letters. The Houston Livestock Show and Rodeo owns its names and marks. RODEOHOUSTON is a registered federal trademark, {SRC['tm']}, registered April 14, 2026, covering rodeos, concerts and live entertainment plus clothing like hats and t-shirts.</p>
<p>{SRC['brand']} say third-party use of Rodeo logos requires approval from its Marketing Director, that official sponsors get a provided logo lockup that can’t be altered, and that materials representing the Show go through the marketing department. If you aren’t a sponsor, you don’t have a lockup.</p>
<!--fig:trademark-->
<p>We’re not lawyers, so here’s our practical line. You can say true, plain things about dates and the season: “Open late during rodeo season,” “Boots for Go Texan Day,” “Dinner before the concert at NRG.” Avoid the Rodeo’s logos, its bucking horse art or anything resembling it, the RODEOHOUSTON wordmark styled like theirs, and any phrase that implies a relationship: “official,” “partner,” “presented by,” “the rodeo’s favorite.” Don’t imply a ticket giveaway is connected to the Rodeo, and don’t use performer names or photos to sell your product. If you want a real tie-in, the Rodeo has sponsorship programs. Ask them.</p>
<p>Same goes for ad platforms. A trademark owner can file complaints with Google and Meta about ads using its marks, and an ad that gets flagged in the middle of February is a bad week to lose.</p>"""),

            ("Rodeo content ideas that don’t look like everyone else’s", f"""<p>Every feed in Houston gets the same boot flat-lay in February. A few ideas that tend to perform better:</p>
<!--fig:content-->
<p>Go Texan Day is worth its own plan. The Rodeo encourages people to wear western clothes that day, and encourages organizations to hold western-themed events with dress-up, decor, barbecue or cook-off contests, per {SRC['gotexan']}. Schools get into it too. On Go Texan Day, trail riders visited seven southwest Houston schools as part of HISD’s celebration, per {SRC['hisd']}. We didn’t find any district that closes school for a “rodeo day,” so don’t plan a weekday family promo around one; plan around Go Texan Day dress-up and spring break instead.</p>
<p>School-age demand shows up in other ways: kids’ boots and hats, rodeo-week birthday parties, photographers booking western mini-sessions. Families from Magnolia, Tomball, Conroe and Kingwood drive in on weekends, so suburban businesses can market “on the way home from NRG” as much as “on the way there.”</p>
<p>For restaurants, our {L('/blog/restaurant-marketing-the-woodlands-houston/', 'restaurant marketing guide for The Woodlands and Houston')} covers the reservation and Google setup. For shops, see {L('/blog/boutique-retail-store-marketing-the-woodlands/', 'boutique retail marketing')}, and if you’re selling tickets to your own rodeo-week event, {L('/blog/how-to-sell-more-event-tickets-houston/', 'how to sell more event tickets in Houston')}.</p>"""),

            ("Where rodeo customers come from around Houston", f"""<p>NRG Park is on the south side of the Loop. Your customers aren’t all there. Rodeo traffic flows from every suburb on 288, I-45, US 59/I-69 and the 610 Loop, and much of the spending happens near home.</p>
<!--fig:map-->
<p>For a Woodlands, Spring or Conroe business, the money is in the trip planning: the outfit, the dinner, the park and ride. For a Pearland, Sugar Land or Bellaire business, the money is also in the drive itself, because the trip to NRG is short and a lot of people stop on the way.</p>
<p>If you want help building your rodeo calendar, ads and content before the January rush, <a href="/contact/">get in touch</a> and tell us what sold last year. Our {L('/services/paid-social-advertising/', 'paid social team')} does most of this work on Meta and TikTok.</p>"""),
        ],
        "faq": [
            ("When is the Houston rodeo in 2027?",
             "RODEOHOUSTON 2027 runs Tuesday, March 2 through Sunday, March 21 at NRG Park, a 20-day run. Go Texan Day and Rodeo Roundup are Friday, February 26, the trail rides arrive at Memorial Park that Friday, and the Downtown Rodeo Parade is Saturday, February 27 at 10 a.m. The barbecue contest is expected February 25 to 27, but confirm that on the Rodeo’s website."),
            ("When should Houston and The Woodlands businesses start rodeo marketing?",
             "Plan and shoot content in early January, start ads in the last two weeks of January, and spend the most from February 1 through Go Texan Day weekend. Most outfit shopping and group dinner booking happens before opening day. During the run itself, shift to pre-concert, late-night and after-show offers, and save a small budget for post-rodeo clearance and thank-you posts."),
            ("Can my business use the Houston rodeo logo in ads?",
             "Not without permission. The Houston Livestock Show and Rodeo owns its names and logos, RODEOHOUSTON is a registered trademark, and the Rodeo’s brand standards require approval for third-party logo use. You can describe the season truthfully, such as open late during rodeo season, but avoid logos, look-alike art, and words like official or partner unless you have a sponsorship agreement."),
            ("What businesses get busier during rodeo season in Houston?",
             "Western wear and boot stores see the clearest spike, with local shops reporting boot sales in the thousands before opening day. Restaurants and bars see group bookings and pre-concert dinners, hotels see concert-night and out-of-town demand, and salons, detailers, party buses, caterers and event rental companies often see lifts around Go Texan Day and big concert weekends. Check your own sales history."),
            ("What is Go Texan Day in Houston?",
             "Go Texan Day is the unofficial kickoff of the Houston Livestock Show and Rodeo, held the Friday before opening day. In 2027 it falls on February 26. People wear jeans, boots and hats to work and school, Rodeo Roundup takes place downtown from 11 a.m. to 1 p.m., and trail rides arrive at Memorial Park. Many offices and schools hold western-themed events."),
        ],
        "figures": {
            "calendar": {
                "type": "steps",
                "title": "Rodeo season marketing calendar, 2027",
                "sub": "For Houston and The Woodlands businesses, keyed to the March 2-21 run",
                "steps": [["Early-mid January", "Lock offers, shoot real content, build landing pages, get ads approved."], ["Late January", "Start social ads and email; book office Go Texan Day parties."], ["Feb. 1-21", "Heaviest spend: outfits, group dinners, search ads, fresh Google photos."], ["Feb. 22-28", "BBQ contest, Go Texan Day Feb. 26, parade Feb. 27. Post daily."], ["March 2-21", "Before-and-after offers around concerts; spring break March 15-19."], ["March 22 on", "Clearance, thank-you posts, save content and notes for next year."]],
                "alt": "Week-by-week rodeo season marketing calendar for Houston and The Woodlands businesses for RODEOHOUSTON 2027",
                "caption": "Most of the work happens before opening day. The run itself is the payoff.",
            },
            "attendance": {
                "type": "bars",
                "title": "RODEOHOUSTON total attendance",
                "sub": "All grounds activities, by year",
                "items": [["2024", 2553185, "2.55M"], ["2025 (record)", 2735690, "2.74M"], ["2026", 2621765, "2.62M"]],
                "highlight": [1],
                "note": "Source: RODEOHOUSTON attendance page",
                "alt": "Bar chart of Houston rodeo attendance from 2024 to 2026 for rodeo season marketing in Houston and The Woodlands",
                "caption": f"From {SRC['attend']}.",
            },
            "stats": {
                "type": "stats",
                "title": "Why rodeo season moves Houston’s economy",
                "stats": [["$597M", "economic activity in Greater Houston, 2024"], ["28%", "of unique attendees from outside Greater Houston"], ["20", "days in the 2027 run"], ["250+", "BBQ contest teams in 2026"]],
                "note": "Sources: RODEOHOUSTON 2024 economic study, 93Q Country, Click2Houston",
                "alt": "Statistics on the Houston rodeo economic impact and 2027 schedule for Houston and The Woodlands businesses",
                "caption": f"From {SRC['econ']}, {SRC['q93']} and {SRC['bbq']}.",
            },
            "budget": {
                "type": "bars",
                "title": "Where a small rodeo budget goes",
                "sub": "Share of rodeo-season ad spend by window",
                "items": [["Late January", 15, "15%"], ["February 1-28", 55, "55%"], ["March 2-21 (the run)", 25, "25%"], ["After the run", 5, "5%"]],
                "highlight": [1],
                "note": "Illustrative example",
                "alt": "Bar chart of an example rodeo season advertising budget split for a Houston or The Woodlands small business",
                "caption": "A planning starting point. Restaurants and hotels may weight the run more heavily.",
            },
            "trademark": {
                "type": "compare",
                "title": "Rodeo marketing wording: risky vs. safer",
                "left": {"title": "Asking for a letter", "items": ["The Rodeo’s logo or bucking horse art", "“Official rodeo boots”", "“Proud partner of the rodeo”", "Concert headliner photos in your ads", "Ticket giveaways implying a Rodeo tie"]},
                "right": {"title": "Plain and true", "items": ["“Open late during rodeo season”", "“Boots for Go Texan Day”", "“Dinner before the concert at NRG”", "Your own staff in your own western wear", "Your own giveaway, your own rules"]},
                "alt": "Comparison of risky and safer rodeo trademark wording for Houston and The Woodlands business marketing",
                "caption": f"Based on {SRC['brand']}. Ask an attorney if you’re unsure.",
            },
            "content": {
                "type": "checklist",
                "title": "Rodeo content ideas that perform",
                "sub": "For Houston and The Woodlands shops, restaurants and services",
                "items": ["Staff try-ons: one outfit at three price points", "Go Texan Day office party menu or bundle", "“How to wear boots you already own” reel", "Pre-concert dinner timing guide from your spot", "Customer photos on Go Texan Day (with permission)", "Behind the scenes at the BBQ contest weekend", "Truck and trailer wash before the parade", "Post-rodeo clearance with real markdowns"],
                "alt": "Checklist of rodeo season social media content ideas for Houston and The Woodlands businesses",
                "caption": "Real people in your own space beat stock western imagery every time.",
            },
            "map": {
                "type": "map",
                "title": "Rodeo shoppers spend near home",
                "sub": "Suburbs that feed NRG Park traffic, where the outfit and dinner money often moves",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Katy", "Cypress", "Sugar Land", "Pearland", "Kingwood", "Magnolia", "Tomball", "Bellaire"],
                "alt": "Map of Houston and The Woodlands suburbs where rodeo season customers shop before heading to NRG Park",
                "caption": f"The Woodlands Express runs a rodeo park and ride from the Sawdust lot, per {SRC['pnr']}.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: growth corridors data story
    {
        "slug": "houston-growth-corridors-new-customers-2027",
        "title": "Where Houston Is Growing: The Corridors Bringing New Customers in 2027",
        "seo_title": "Houston Growth Corridors 2027: Where New Customers Live",
        "desc": "Census, school and home sales data on where Houston and The Woodlands area growth is landing in 2027, and what it means for ad targeting and new locations.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google Business Profile", "Google Analytics"],
        "art": "b2",
        "hero": "growth",
        "hero_alt": "Illustration of a growth chart for Houston growth corridors and new customers in 2027 around The Woodlands",
        "related": ["reaching-customers-conroe-montgomery", "marketing-your-business-katy-cypress-tx", "multi-location-local-seo-houston-franchises"],
        "sections": [
            (None, f"""<p>126,720. That’s how many people the Houston metro added between July 2024 and July 2025, the largest numeric gain of any metro in the country, per the {SRC['census_co']}. The metro passed 7.9 million.</p>
<p>The bigger story for a business owner is <i>where</i> those people went. Harris County still added the most of any U.S. county. But look at the map of who’s moving in, and the growth sits in a ring 25 to 45 miles out: Fulshear and west Katy, the Waller County prairie, the SH 249 corridor through Tomball and Magnolia, Conroe and Willis on I-45, and the Grand Parkway’s newer eastern arc around New Caney.</p>
<p>This is a data story with maps. We pulled the latest Census estimates, school enrollment, master-planned community sales and road projects, then translated them into the two questions we get from clients most: where should we advertise, and where should the next location go?</p>
<!--fig:growthmap-->"""),

            ("County growth around Houston: the 2025 Census numbers", f"""<p>Here’s what the Census Bureau’s March 2026 release shows for the Houston-area counties, July 2024 to July 2025.</p>
<!--fig:counties-->
<div class="bp-tbl"><table>
<thead><tr><th>County</th><th>2025 population</th><th>One-year gain</th><th>Growth rate</th><th>National rank</th></tr></thead>
<tbody>
<tr><td>Harris</td><td>5,045,026</td><td>48,695</td><td>About 1.0%</td><td>No. 1 by numeric gain</td></tr>
<tr><td>Montgomery</td><td>781,194</td><td>30,011</td><td>About 4.0%</td><td>No. 4 by numeric gain</td></tr>
<tr><td>Fort Bend</td><td>975,191</td><td>24,163</td><td>About 2.5%</td><td>No. 8 by numeric gain</td></tr>
<tr><td>Waller</td><td>69,858</td><td>3,761</td><td>5.7%</td><td>No. 2 by percent growth</td></tr>
<tr><td>Liberty</td><td>121,364</td><td>5,073</td><td>4.4%</td><td>No. 8 by percent growth</td></tr>
</tbody></table></div>
<p>Rates for Harris, Montgomery and Fort Bend are our arithmetic from the release’s 2024 and 2025 figures. Waller grew 5.7%, second-fastest of any U.S. county with at least 20,000 people, and was the fastest-growing county in Texas, per {SRC['tt_waller']}. Brazoria County didn’t make either top-10 table, though it keeps growing along SH 288, and we come back to it with the master-planned communities.</p>
<p>Two caveats from the reporting. Harris County’s gain was less than half of its 2024 gain, and its domestic migration has been negative for roughly a decade as people move to the surrounding suburbs, per {SRC['axios']}. International migration fell in nine of ten U.S. counties over the same period. In plain terms, the core is still growing, mostly from births and immigration, while people moving from elsewhere in the U.S. are landing in the outer counties.</p>
<p>For marketing, that means a Montgomery County business is sitting in one of the five fastest-growing counties in America by headcount. Roughly 30,000 new neighbors a year need a dentist, a mechanic, a gym and a favorite taco place.</p>"""),

            ("Fast-growing cities: Fulshear, Conroe, and the places that aren’t really cities", f"""<p>City estimates tell a sharper story, with one trap.</p>
<!--fig:cities-->
<p><b>Fulshear</b> grew 21.0% in a year to 64,630 people, adding 11,196, per the {SRC['census_city']}. It was the second-fastest growing U.S. city with 20,000+ people, and seventh in the country by raw numbers, just behind the City of Houston’s 11,515. {SRC['axios_ful']} noted it was Fulshear’s third straight year at No. 2.</p>
<p><b>Conroe</b> has more than doubled since 2010, from 56,207 residents to roughly 115,000 by July 2024, per {SRC['chron_conroe']}, which also reported Conroe ranked No. 20 nationally on U-Haul’s 2025 growth index and first among Houston-area suburbs. The I-45 frontage from League Line to Loop 336 shows it.</p>
<p>Now the trap. <b>Katy</b> and <b>Magnolia</b> grow fast in real life, but much of that growth happens outside their city limits, in unincorporated subdivisions with a Katy or Magnolia mailing address. City population estimates undercount what you see on FM 1488 or along the Grand Parkway west of I-10. School districts are a better yardstick for those areas.</p>
<p>For ad targeting, that trap matters. If you target the “City of Magnolia” in Google Ads, you’re aiming at a small town footprint. Target by radius or ZIP code around where the rooftops actually are, and check the location report after two weeks to see where clicks really came from.</p>"""),

            ("School enrollment: the growth signal that leads everything else", f"""<p>Families with kids drive a huge share of local spending, and school enrollment is the cleanest public count of where they’re going. The Texas Education Agency numbers, as reported by {SRC['ci_tea']}, show two very different metros.</p>
<div class="bp-tbl"><table>
<thead><tr><th>District</th><th>Enrollment change, 2021 to 2026</th><th>Where</th></tr></thead>
<tbody>
<tr><td>Lamar CISD</td><td>+9,208 students (+23.3%)</td><td>Fulshear, Richmond, Rosenberg</td></tr>
<tr><td>Katy ISD</td><td>+6,927</td><td>Katy, west Houston</td></tr>
<tr><td>Conroe ISD</td><td>+4,996</td><td>The Woodlands, Conroe, Willis area</td></tr>
<tr><td>Splendora ISD</td><td>+34.6%</td><td>US 59/I-69 north of New Caney</td></tr>
<tr><td>Tomball ISD</td><td>+14.9%</td><td>SH 249 corridor</td></tr>
<tr><td>New Caney ISD</td><td>+14.9%</td><td>I-69 and Grand Parkway east</td></tr>
<tr><td>Houston ISD</td><td>-25,795</td><td>City core</td></tr>
<tr><td>Aldine ISD</td><td>-9,472</td><td>North Houston</td></tr>
</tbody></table></div>
<p>The same report showed Region 6, which includes Montgomery County, up 3.8% while Region 4, which covers Harris County, fell 0.9%.</p>
<p>Waller ISD makes the newest point. Enrollment went from 9,894 in August 2025 to 11,467 in August 2026, and the district was processing about 60 new applications a day, per {SRC['waller_isd']}. Lamar CISD says it has 94 active subdivisions and more than 55,000 future lots in development, and it’s planning for nearly 2,000 new students a year by 2034, per {SRC['lamar']}. Those future lots are your future customers, and they show up as households before they show up in any city estimate.</p>"""),

            ("Master-planned community sales: where the rooftops are going up", f"""<p>RCLCO ranks the top-selling master-planned communities in the country twice a year, and Houston dominates the list.</p>
<!--fig:mpcbars-->
<p>In {SRC['rclco26']}, nine Houston-area communities made the national top 50 for the first half of 2026, led by Tamarron at No. 6 with 594 sales, Bridgeland at No. 9 with 500 and Sunterra at No. 10 with 450. For all of 2025, ten Houston communities made the top 50, with Sunterra fifth at 1,024 sales and Tamarron ninth at 974, per {SRC['rclco25']}.</p>
<!--fig:mpcmap-->
<p>Look at where those nine sit. Tamarron, Sunterra, Anniston, Elyson and Jordan Ranch are on the Katy-Fulshear side, with Tamarron and Sunterra straddling into Waller County. Bridgeland and The Grand Prairie are in the Cypress-Hockley stretch along US 290. Sienna is in Missouri City, and Meridiana is in Brazoria County off SH 288. Every one of them is west or south of the city.</p>
<p>Montgomery County’s big communities (Woodforest, Grand Central Park, The Woodlands Hills, Artavia) grow too, and the county’s 30,011-person gain proves people are arriving. They just didn’t crack the national top 50 in that half-year. A business on the north side shouldn’t read that as slowdown. It reads as the growth being spread across more, smaller subdivisions, which actually makes targeting by radius more important. Our {L('/blog/home-builder-marketing-houston-montgomery-county/', 'home builder marketing post')} covers the north-side MPCs in more detail.</p>"""),

            ("The road corridors: Grand Parkway, SH 249 and I-69", f"""<p>Houston growth follows pavement. Three corridors explain most of what’s coming in 2027 and after.</p>
<!--fig:roadmap-->
<p><b>Grand Parkway (SH 99).</b> The planned loop is 184 miles, per {SRC['gp_story']}. Segments H, I-1 and I-2 opened in May 2022, adding 52.5 miles from I-69 in New Caney to I-10 near Baytown through Harris, Montgomery, Liberty and Chambers counties, per {SRC['gp_hi']}. That stretch explains a lot of the New Caney, Splendora and Liberty County numbers above. On the south side, Segment B runs 28 miles from I-45 in League City to SH 288 near Rosharon and is environmentally approved but not built, per {SRC['gp_b']}. The first piece, B-1, is about 14 miles from League City to south of FM 2403 in Alvin. TxDOT expects construction to start in early 2027 and finish by 2032.</p>
<p><b>SH 249 and the Aggie Expressway.</b> The tolled extension northwest of Tomball, which TxDOT’s project sheet calls the Aggie Expressway, runs about 14.8 miles from Pinehurst to Todd Mission, per {SRC['sh249']}. Segment 1B from FM 1488 in Magnolia to FM 1774 opened in March 2021, and the final segment opened in fall 2022, per {SRC['ci_249']}. That corridor is why Tomball ISD grew 14.9% in five years and why Magnolia-area rooftops keep climbing.</p>
<p><b>I-69 (US 59).</b> It’s the spine of two growth stories at once. Southwest, it runs through Sugar Land and Rosenberg into Fort Bend’s Lamar CISD territory. Northeast, it runs through Humble and Kingwood to New Caney and Splendora, where it meets the newer Grand Parkway segments.</p>
<p>A business deciding where to open should drive these corridors at 5:30 p.m. on a Tuesday. Where the traffic backs up on the way home, rooftops are already there and services haven’t caught up yet.</p>"""),

            ("What the growth data means for where you advertise", f"""<p>Now the practical part. Here’s how we’d use this data in a campaign for a Houston or The Woodlands business.</p>
<!--fig:playbook-->
<p><b>Target the rings, not just the city.</b> A Woodlands business with a 10-mile radius is missing most of Conroe’s growth and all of Magnolia’s. Extend radius ads to 15 or 20 miles if you can serve those customers, or build separate campaigns for the growth ZIPs so you can see what they cost. Use “presence” targeting (people in or regularly in your locations) so you’re not paying for people merely interested in the area.</p>
<p><b>Reach new movers early.</b> People pick a new dentist, vet, gym and pediatrician in their first few months. Google Business Profile visibility in the new area, local search ads on “near me” terms and Meta ads within a few miles of new subdivisions do most of that work. Our {L('/blog/geo-fencing-ads-target-customers-nearby/', 'guide to geofencing ads')} covers the tighter targeting options and their limits.</p>
<p><b>Make location pages for growth areas.</b> If you serve Fulshear, Magnolia or New Caney, give each a real page with drive times, landmarks and reviews from customers there. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} shows the format.</p>
<p><b>Watch your location reports.</b> Google Ads and GA4 both show where clicks and conversions come from. After a month, compare cost per lead in growth ZIPs against your established ones. Newer areas are often cheaper to reach because fewer competitors bother.</p>
<p><b>Speak to newcomers.</b> A family that moved from Chicago to Fulshear last spring doesn’t know which roads flood, what a MUD tax is, or that you’ve been fixing AC in Fort Bend since 2009. Ads and pages that say “new to Fulshear?” or answer newcomer questions tend to earn clicks that generic copy doesn’t. Spanish-language ads are worth testing in many of these corridors too; our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Spanish-language marketing guide')} covers the setup.</p>
<p><b>Expect thinner competition and thinner data.</b> In a new subdivision, there may be only a handful of reviews for anyone in your category, so 20 good reviews can put you near the top of the map pack. The flip side is that keyword planners show low volumes for brand-new areas. Don’t let a small search volume number talk you out of a ZIP code where 2,000 homes were sold last year.</p>
<p>For more on the north and west sides specifically, see {L('/blog/reaching-customers-conroe-montgomery/', 'reaching customers in Conroe and Montgomery County')} and {L('/blog/marketing-your-business-katy-cypress-tx/', 'marketing in Katy and Cypress')}.</p>"""),

            ("Where to open a new location in Greater Houston", f"""<p>Ads can reach anyone. A building can’t move. Opening a second location is where this data earns its keep.</p>
<!--fig:sitecompare-->
<p>What we’d look at, in order:</p>
<ol>
<li><b>School enrollment trend</b> for the district around the site. Growth of 10% or more over five years means families are arriving faster than most service businesses can open.</li>
<li><b>Active subdivisions and lots</b> within a 10-minute drive. Lamar CISD’s 55,000 future lots are an extreme example. Your local MUD or county permit data gives a closer read.</li>
<li><b>Road timing.</b> A site that’s quiet today may sit next to a Grand Parkway segment opening in five years. Segment B-1 near Alvin and League City is that kind of bet.</li>
<li><b>Competitor density.</b> Search your category in Google Maps from the site and count the results with more than 50 reviews. Growth areas often have one or two established players and a lot of open room.</li>
<li><b>Your own customer data.</b> Map where your current customers already drive from. If 20% of them come from Fulshear to your Katy location, that’s your answer.</li>
</ol>
<p>When you do open, the first 30 days of marketing decide a lot. Our {L('/blog/grand-opening-marketing-plan-30-days/', '30-day grand opening plan')} and {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO guide')} cover the launch side. If you want a senior strategist to map your customers against this growth data and build a plan for the next location or campaign, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("What are the fastest-growing areas around Houston in 2027?",
             "The latest Census estimates show Waller County growing 5.7% in a year and Liberty County 4.4%, while Harris, Montgomery and Fort Bend added the most people. Fulshear was the nation’s second-fastest growing city of its size. School data points to Lamar CISD, Waller ISD, Tomball ISD, New Caney ISD and Splendora ISD, along the Grand Parkway, SH 249 and I-69 corridors."),
            ("How fast is Montgomery County growing near The Woodlands?",
             "Montgomery County added 30,011 people between July 2024 and July 2025, the fourth-largest numeric gain of any U.S. county, reaching 781,194 residents. That’s roughly 4% growth in a year. Conroe has more than doubled since 2010 to about 115,000, and Conroe ISD added nearly 5,000 students from 2021 to 2026. Growth spreads across Conroe, Willis, Magnolia and New Caney."),
            ("Which Houston master-planned communities sell the most homes?",
             "In RCLCO’s mid-2026 ranking, nine Houston-area communities made the national top 50, led by Tamarron, Bridgeland and Sunterra. For all of 2025, Sunterra ranked fifth nationally with 1,024 sales and Tamarron ninth with 974. Most top sellers are on the Katy, Fulshear, Cypress and Hockley side, with Sienna in Missouri City and Meridiana in Brazoria County."),
            ("How should a Houston business change its ad targeting for growth areas?",
             "Target by radius or ZIP code around where new rooftops are, not by small city names like Magnolia or Katy whose limits miss most of the growth. Build separate campaigns for growth ZIPs so you can compare costs, use presence-only location targeting, and add location pages for each growth area. Check Google Ads and GA4 location reports after a month and shift budget toward what converts."),
            ("When will the Grand Parkway Segment B-1 be built?",
             "TxDOT expects construction on Segment B-1 of the Grand Parkway, about 14 miles from League City to south of FM 2403 in Alvin, to start in early 2027 and be completed by 2032. It’s the first piece of Segment B, which will eventually connect I-45 to SH 288 near Rosharon. Businesses in Alvin, League City and Pearland should watch that corridor."),
        ],
        "figures": {
            "growthmap": {
                "type": "map",
                "title": "Where Houston’s new customers are landing",
                "sub": "Fast-growing cities and school districts named in this post",
                "highlight": ["Fulshear", "Katy", "Cypress", "Tomball", "Magnolia", "Conroe", "Willis", "New Caney", "Porter", "Missouri City", "Pearland"],
                "alt": "Map of Houston growth corridors in 2027 around The Woodlands, including Fulshear, Katy, Magnolia, Conroe and New Caney",
                "caption": f"Based on the {SRC['census_city']}, {SRC['chron_conroe']} and {SRC['ci_tea']}.",
            },
            "counties": {
                "type": "bars",
                "title": "Houston-area county gains, July 2024 to July 2025",
                "sub": "New residents in one year",
                "items": [["Harris County", 48695, "48,695"], ["Montgomery County", 30011, "30,011"], ["Fort Bend County", 24163, "24,163"], ["Liberty County", 5073, "5,073"], ["Waller County", 3761, "3,761"]],
                "highlight": [1],
                "note": "Source: U.S. Census Bureau, Vintage 2025 estimates",
                "alt": "Bar chart of Houston area county population growth for Harris, Montgomery, Fort Bend, Liberty and Waller counties near The Woodlands",
                "caption": f"From the {SRC['census_co']}. Waller and Liberty are small in headcount and lead in growth rate.",
            },
            "cities": {
                "type": "stats",
                "title": "City growth around Houston",
                "stats": [["21.0%", "Fulshear’s one-year growth, No. 2 in the U.S."], ["64,630", "Fulshear’s 2025 population"], ["115K", "Conroe, July 2024, up from 56,207 in 2010"], ["11,515", "people added by the City of Houston"]],
                "note": "Source: U.S. Census Bureau; Houston Chronicle",
                "alt": "Statistics on Fulshear, Conroe and City of Houston population growth for businesses in Houston and The Woodlands",
                "caption": f"From the {SRC['census_city']} and {SRC['chron_conroe']}.",
            },
            "mpcbars": {
                "type": "bars",
                "title": "Houston’s top-selling master-planned communities",
                "sub": "Home sales, first half of 2026, RCLCO national top 50",
                "items": [["Tamarron (Fulshear/Katy)", 594, "594"], ["Bridgeland (Cypress)", 500, "500"], ["Sunterra (Katy)", 450, "450"], ["Anniston (Katy)", 313, "313"], ["Meridiana (Brazoria Co.)", 276, "276"], ["The Grand Prairie (Hockley)", 259, "259"], ["Elyson (Katy)", 227, "227"], ["Sienna (Missouri City)", 223, "223"], ["Jordan Ranch (Fulshear)", 207, "207"]],
                "highlight": [0],
                "note": "Source: RCLCO via Houston Agent Magazine",
                "alt": "Bar chart of top-selling master-planned communities in Houston in 2026 for businesses choosing where to advertise",
                "caption": f"From {SRC['rclco26']}.",
            },
            "mpcmap": {
                "type": "map",
                "title": "The top-selling communities sit west and south",
                "sub": "Approximate areas of the nine Houston MPCs in RCLCO’s mid-2026 top 50",
                "highlight": ["Fulshear", "Katy", "Cypress", "Missouri City", "Pearland"],
                "note": "Pearland marks the SH 288 area near Meridiana; Cypress marks Bridgeland and The Grand Prairie.",
                "alt": "Map of top-selling master-planned communities around Houston relative to The Woodlands, concentrated in Katy, Fulshear and Cypress",
                "caption": "North-side growth is real too, spread across more, smaller subdivisions.",
            },
            "roadmap": {
                "type": "map",
                "title": "Corridors to watch: Grand Parkway, SH 249, I-69",
                "sub": "Places on the newer Grand Parkway segments, the SH 249 extension and the I-69 growth stretches",
                "highlight": ["Tomball", "Magnolia", "New Caney", "Porter", "Kingwood", "League City", "Pearland", "Sugar Land"],
                "note": "Grand Parkway Segment B-1 (League City to Alvin) is expected to start construction in early 2027.",
                "alt": "Map of Houston road growth corridors including the Grand Parkway, SH 249 Aggie Expressway and I-69 near The Woodlands",
                "caption": f"Road details from {SRC['gp_story']}, {SRC['gp_hi']} and {SRC['sh249']}.",
            },
            "playbook": {
                "type": "steps",
                "title": "Turning growth data into ad targeting",
                "sub": "For Houston and The Woodlands businesses",
                "steps": [["Map your customers", "Plot where current customers live and how far they already drive."], ["Overlay growth", "Mark growth ZIPs from school, Census and MPC data."], ["Split campaigns", "Separate growth-area campaigns so costs are visible."], ["Build local pages", "One real page per growth area you serve."], ["Read location reports", "After 30 days, move budget toward cheaper leads."]],
                "alt": "Five steps to use Houston growth corridor data for ad targeting for businesses in Houston and The Woodlands",
                "caption": "Step one is the one most businesses skip.",
            },
            "sitecompare": {
                "type": "compare",
                "title": "Picking a second location",
                "left": {"title": "Common approach", "items": ["Near the owner’s house", "Cheapest lease available", "City population as the yardstick", "Today’s traffic counts only", "Gut feel on competitors"]},
                "right": {"title": "Data approach", "items": ["Near where customers already drive from", "Lease priced against growth ahead", "School enrollment and lots as yardsticks", "Road projects in the next five years", "Map pack count of strong competitors"]},
                "alt": "Comparison of ways to choose a new business location in Houston growth corridors near The Woodlands",
                "caption": "Data won’t sign the lease for you. It does make the shortlist shorter.",
            },
        },
    },
]
