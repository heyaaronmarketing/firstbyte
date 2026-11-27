"""Batch 17 (module q_c): three non-niche posts in different formats.
1. Cost guide with worked examples: EDDM and direct mail costs in The Woodlands and Houston.
2. Playbook: new-mover marketing in The Woodlands and Houston.
3. B2B event guide with a timeline: trade show marketing in Houston (OTC, Reliant Park, George R. Brown).

Research, EDDM post: MailPro's July 2026 rate table (EDDM Retail $0.247 to $0.260 on July 12, 2026; Marketing Mail
5-digit letters $0.372 to $0.395); MailPro's EDDM guide ($390 annual mailing fee plus $390 permit imprint application
fee as of July 12, 2026; 12 x 15 inch and 0.75 inch maximums); DMM 143 (EDDM Retail flat eligibility: longer than
10-1/2 in., higher than 6-1/8 in. or thicker than 1/4 in.; 3.3 oz max; 200-piece minimum; 5,000 pieces per day per
5-digit ZIP; no personal information); DMM 145 (bundles of 50-100, facing slips, route sortation); DMM 144 (indicia
above and to the right of the simplified address); USPS April 9, 2026 release (July 12 price change); Quad's July 2026
postal update (USPS motion to move the next market-dominant increase to January 2027; about 6.5% estimated for Marketing
Mail Flats); USPS Informed Delivery campaign best practices (free, ride-along image, 3 days before and after in-home);
PostalPro Informed Delivery saturation campaign guide (PostalOne! eDoc); Google Customer Match policy (90 days and
$50,000 lifetime spend for targeting); The Woodlands Township village association list.
New-mover post: NAHB / Eye on Housing (July-Aug 2026, Consumer Expenditure Survey 2020-2023: $26,882 new-home buyers,
$18,673 existing-home buyers, $9,457 non-movers; appliance, furnishing, repair splits); Axios on the record-low 11%
mover rate (Point2Homes analysis of Census data); ABC13 (Houston metro +126,720, July 2024 to July 2025); Axios Houston
(Harris County +~49,000, most of any U.S. county); Census QuickFacts Montgomery County (781,194 on July 1, 2025, +25.9%
since April 2020; 71.8% owner-occupied); USPS-required NCOALink text via Precisely (may not be used to create new movers
lists); USPS privacy policy ("We do not sell customer or mailing lists to outside parties, including marketers");
Social Media Today on Meta's detailed targeting removals (latest effective January 15, 2026); CFPB RESPA FAQs.
Trade show post: OTC 2027 site (OTC + URTeC co-located May 3-5, 2027, Reliant Park); JPT on the co-location; OTC 2026
wrap release (nearly 25,000 attendees, nearly 1,000 exhibitors, 100+ countries); Visit Houston and ABC13 on NRG Park
becoming Reliant Park (August 1, 2026); Oil & Gas Journal event listing (NAPE Summit Feb 3-5, 2027, George R. Brown);
TPS event info (Oct 18 short courses, Oct 19-21, 2027, GRB); S&P Global release (CERAWeek 2026, March 23-27, Houston);
Houston First GRB page (1.9 million usable sq ft, Hilton Americas ~1,200 rooms, Marriott Marquis 1,000 rooms,
skybridges); Google Ads location targeting help (radius at least 1 km); Meta Marketing API basic targeting (custom
location radius .63 to 50 miles / 1 to 80 km).
Not used because we couldn't verify them: EDDM BMEU per-piece price after July 12, 2026 (Notice 123 file blocked);
CERAWeek 2027 dates from an official source; whether Meta's "Recently moved" life event survived the January 2026
removals; direct mail response-rate benchmarks (ANA report is members-only).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # EDDM post
    "mp_jul": A("https://www.mailpro.org/post/usps-rate-changes-july-2026/", "MailPro’s July 2026 rate table"),
    "mp_eddm": A("https://www.mailpro.org/post/every-door-direct-mail-eddm/", "MailPro’s EDDM guide"),
    "dmm143": A("https://pe.usps.com/cpim/ftp/manuals/dmm300/143.pdf", "USPS Domestic Mail Manual section 143"),
    "dmm145": A("https://pe.usps.com/text/dmm300/145.htm", "DMM section 145"),
    "dmm144": A("https://pe.USPS.com/text/dmm300/144.htm", "DMM section 144"),
    "usps_jul": A("https://about.usps.com/newsroom/national-releases/2026/0409-usps-recommends-new-prices-for-july.htm", "USPS announced in April"),
    "quad": A("https://www.quad.com/insights/postal-optimization/postal-paper-logistics-update-july-2026", "Quad’s July 2026 postal update"),
    "eddm": A("https://www.usps.com/business/every-door-direct-mail.htm", "USPS’s EDDM page"),
    "idp": A("https://www.usps.com/business/pdf/informed-delivery-campaign-best-practices.pdf", "USPS’s Informed Delivery campaign guide"),
    "idsat": A("https://postalpro.usps.com/promotions/dscng", "saturation campaign mailer guide"),
    "cm": A("https://support.google.com/adspolicy/answer/6299717?hl=en", "Google’s Customer Match policy"),
    "twp": A("https://www.thewoodlandstownship-tx.gov/villageassociations", "The Woodlands Township’s village association page"),
    # new-mover post
    "nahb": A("https://eyeonhousing.org/2026/07/what-do-home-buyers-purchase-after-they-move-in/", "NAHB’s analysis of Consumer Expenditure Survey data"),
    "nahb2": A("https://www.nahb.org/news-and-economics/housing-economics-plus/special-studies/special-studies-pages/how-much-buyers-spend-after-moving-in", "NAHB’s August 2026 special study"),
    "axmove": A("https://www.axios.com/2025/11/30/us-moving-rate-map", "Axios"),
    "abc13c": A("https://abc13.com/post/houston-area-tops-latest-us-census-growth-estimates-despite-slowing-population-data-shows/18791745/", "ABC13"),
    "axhou": A("https://www.axios.com/local/houston/2026/04/02/houston-harris-population-growth-2025-census-immigration-policy", "Axios Houston"),
    "qfmc": A("https://census.gov/quickfacts/montgomerycountytexas", "Census QuickFacts"),
    "ncoa": A("https://docs.precisely.com/docs/sftw/verimove/3.9/en-us/webhelp/Introduction/USPSRequiredText.html", "the license text USPS requires NCOA vendors to publish"),
    "uspspriv": A("https://about.usps.com/who/legal/privacy-policy/welcome.htm", "USPS’s privacy policy"),
    "smt": A("https://www.socialmediatoday.com/news/meta-removes-more-detailed-ad-targeting-options-facebook-instagram/757856/", "Social Media Today"),
    "respa": A("https://consumerfinance.gov/compliance/compliance-resources/mortgage-resources/real-estate-settlement-procedures-act/real-estate-settlement-procedures-act-faqs", "the CFPB’s RESPA FAQs"),
    # trade show post
    "otc27": A("https://2027.otcnet.org/attend/otc-urtec-2027", "OTC’s 2027 site"),
    "jpt": A("https://jpt.spe.org/otc-and-urtec-announce-strategic-co-location-to-accelerate-energy-innovation", "JPT"),
    "otc26": A("https://www.otcnet.org/press-releases/otc-2026-wraps-four-days-dialogue-offshore-energys-next-frontiers", "OTC’s 2026 wrap-up release"),
    "reliant": A("https://www.visithoustontexas.com/blog/post/nrg-park-is-now-reliant-park/", "Visit Houston"),
    "abc13r": A("https://abc13.com/post/nrg-stadium-home-houston-texans-rodeo-renamed-reliant-august-2026-company-announces/18893525/", "ABC13"),
    "nape": A("https://www.ogj.com/events/event/55395079/2027-nape-summit", "Oil &amp; Gas Journal’s event listing"),
    "tps": A("https://tps.tamu.edu/event-info", "the Turbomachinery &amp; Pump Symposia site"),
    "cera": A("https://press.spglobal.com/2026-02-17-CERAWeek-by-S-P-Global-2026-to-Convene-Energy-CEOs,-Government-Officials-and-Business-and-Technology-Leaders-in-Houston,-March-23-27", "S&amp;P Global"),
    "grb": A("https://www.houstonfirst.com/venues-1/george-r-brown-convention-center/", "Houston First"),
    "grad": A("https://support.google.com/google-ads/answer/1722043?hl=en", "Google’s location targeting help page"),
    "mrad": A("https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting", "Meta’s targeting documentation"),
}

EDDM = "/blog/eddm-direct-mail-cost-the-woodlands-houston/"
MOVER = "/blog/new-mover-marketing-the-woodlands-houston/"
SHOW = "/blog/trade-show-marketing-houston-otc-conventions/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: EDDM cost guide
    {
        "slug": "eddm-direct-mail-cost-the-woodlands-houston",
        "title": "EDDM and Direct Mail Costs in The Woodlands and Houston: 2026 Rates and Worked Examples",
        "seo_title": "EDDM & Direct Mail Cost in The Woodlands & Houston, 2026",
        "desc": "What EDDM and direct mail cost in The Woodlands and Houston in 2026: USPS rates, size rules, print estimates and three worked examples for 5,000 homes.",
        "category": "Strategy",
        "icons": ["Google Ads", "Meta", "Google Analytics"],
        "art": "b3",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for EDDM and direct mail costs in The Woodlands and Houston",
        "related": ["billboard-advertising-cost-houston", "retargeting-explained", "geo-fencing-ads-target-customers-nearby"],
        "sections": [
            (None, f"""<p>$1,300.</p>
<p>That’s the postage, and only the postage, to put one flyer in 5,000 mailboxes in The Woodlands at the current Every Door Direct Mail Retail rate. Printing, design and your time come on top. Most owners who ask us about mail have a lower number in their head, and a printing quote that somehow never made it into the math.</p>
<p>This is a cost guide, so it’s built around arithmetic. We’ll cover the 2026 USPS rates and size rules, the difference between dropping mail at the counter and going through a Business Mail Entry Unit, labeled printing estimates, how carrier routes work in the EDDM mapping tool, and when a targeted list beats saturation even though it costs more per piece. Then three worked examples for a 5,000-home drop across Woodlands villages, break-even math, and how to tie mail to your Google and Meta campaigns so you can tell whether any of it worked.</p>
<p>Prices below are as of November 2026. USPS changes them at least once a year, so check before you print.</p>"""),

            ("The 2026 EDDM rates and size rules in The Woodlands and Houston", f"""<p>The postage piece is the easy part, because USPS sets one price for everyone. On July 12, 2026, the EDDM Retail rate went from $0.247 to $0.260 per piece, per {SRC['mp_jul']}. {SRC['usps_jul']} that the July changes would cover Marketing Mail, which is the class EDDM travels in.</p>
<!--fig:rates-->
<p>The physical rules matter more than people expect, because a piece that doesn’t qualify gets turned away at the counter. Under {SRC['dmm143']}, an EDDM Retail piece is a flat. It has to be longer than 10-1/2 inches, or taller than 6-1/8 inches, or thicker than 1/4 inch. It can weigh no more than 3.3 ounces. A mailing needs at least 200 pieces (unless the area you’re mailing has fewer than 200 addresses), and you can drop no more than 5,000 pieces per day per 5-digit ZIP Code. On the big end, {SRC['mp_eddm']} puts the maximum at 12 by 15 inches and 0.75 inch thick.</p>
<p>A few rules trip up first-timers. EDDM Retail pieces can’t carry personal information, bills or handwritten notes. There’s no forwarding and no return service, so undeliverable pieces just don’t get delivered. And the postage indicia has to sit above and to the right of the simplified address block, per {SRC['dmm144']}. Your printer will have a template. Use it.</p>
<p>What’s next for prices? In July, USPS asked the Postal Regulatory Commission to move the next market-dominant increase from July 2027 up to January 2027, and estimates at the time pointed to roughly 6.5% for Marketing Mail Flats, according to {SRC['quad']}. That was a request, not a decision. If you’re planning a spring campaign, price it at today’s rate plus a cushion of about 7% and you won’t be surprised.</p>"""),

            ("EDDM Retail vs. BMEU: which door your mail walks through", f"""<p>There are two ways to send EDDM, and the choice affects cost, volume and how much work lands on your desk.</p>
<p><b>EDDM Retail</b> is the do-it-yourself version. You pick routes online, pay online, print the pieces with the retail indicia, bundle them by route and carry them to the post office that serves those routes. {SRC['dmm145']} spells out the prep: bundles of 50 to 100 pieces, a facing slip on top of each bundle under the straps with the piece count written on it, and a separate stack for each route. Nobody needs a permit. The catch is that 5,000-per-day-per-ZIP cap and the fact that you are now, briefly, a mail clerk.</p>
<p><b>EDDM BMEU</b> (sometimes called commercial EDDM) goes in through a Business Mail Entry Unit under a mailing permit. Most small businesses do this through a printer or mail house that already holds the permit. If you hold your own, {SRC['mp_eddm']} lists a $390 annual mailing fee plus a one-time $390 permit imprint application fee as of July 12, 2026. BMEU removes the daily cap and lets heavier pieces mail at a per-pound price.</p>
<!--fig:retailbmeu-->
<p>BMEU postage is priced by entry point and runs below the retail rate. We couldn’t get the current Notice 123 BMEU figure from USPS directly, so we won’t print one. Ask your mail house to show postage as its own line on the quote. If they won’t, that tells you something.</p>
<p>Our rule of thumb: under roughly 10,000 pieces a drop, with routes inside one or two ZIP Codes, Retail is fine and the savings from BMEU barely cover a mail house’s prep fee. Above that, or if you’re mailing every month, a mail house earns its money. Going through a mail house also makes Informed Delivery campaigns realistic, since USPS’s {SRC['idsat']} runs through PostalOne! eDoc files that most owners will never touch themselves.</p>"""),

            ("Printing costs for Houston direct mail (estimates, not quotes)", f"""<p>Printing is where quotes swing the most. Paper stock, coating, quantity, turnaround and whether the printer also handles bundling all move the price. The ranges below are our rough estimates for 5,000 pieces, full color on both sides, on a standard postcard-weight stock. They’re meant to keep you from being shocked. Get at least three real quotes, including one from a local Houston-area printer who can tell you what the post office counter in Spring or Conroe will accept.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Size</th><th>Qualifies for EDDM Retail?</th><th>Estimated print cost per piece (5,000)</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>4 x 6 or 5 x 7 postcard</td><td>No, too small to be a flat</td><td>n/a for EDDM</td><td>Targeted-list mail at letter rates</td></tr>
<tr><td>6.25 x 9</td><td>Yes (taller than 6-1/8 in.)</td><td>About $0.07 to $0.14</td><td>One offer, one photo, tight budgets</td></tr>
<tr><td>6.25 x 11</td><td>Yes</td><td>About $0.09 to $0.17</td><td>The default for most service businesses</td></tr>
<tr><td>8.5 x 11</td><td>Yes</td><td>About $0.10 to $0.20</td><td>Menus, before-and-after photos, price lists</td></tr>
<tr><td>9 x 12</td><td>Yes</td><td>About $0.14 to $0.26</td><td>Real estate, grand openings, premium brands</td></tr>
</tbody></table></div>
<p>All figures are estimates. Design is separate. A freelancer might charge a few hundred dollars for a postcard; an agency that also writes the offer and builds the landing page behind it will charge more. Our {L('/services/creative-branding/', 'creative and branding team')} does that work, and we’d rather you spend on a good offer than a fancy fold.</p>
<p>Two hidden costs show up later. Rush turnaround carries a premium at most printers, and a typo on 5,000 cards is a reprint, not an edit. Order a hard proof for anything above about $1,000.</p>"""),

            ("Carrier routes and the EDDM mapping tool, with The Woodlands as the example", f"""<p>EDDM doesn’t mail to neighborhoods. It mails to carrier routes, which are the set of addresses one letter carrier covers. A route might be 300 homes or 700, and it follows streets, not village lines. That’s the first thing to get used to.</p>
<p>The Woodlands Township lists eight village associations: Alden Bridge, Cochran’s Crossing, College Park, Creekside Park, Grogan’s Mill, Indian Springs, Panther Creek and Sterling Ridge, per {SRC['twp']}. They make sensible units for planning, but a carrier route can cross a village boundary, and Creekside Park sits on the Harris County side of Spring Creek. When you zoom into the mapping tool on {SRC['eddm']}, you’ll see routes as colored shapes with residential and business counts, plus Census-based filters for age, household income and household size.</p>
<!--fig:map-->
<p>Here’s how we’d use the tool for a 5,000-home drop:</p>
<!--fig:tool-->
<p>A Woodlands-specific note: routes near Market Street, Hughes Landing and the Research Forest corridor carry a lot of business addresses and apartments. If you want only single-family homes, turn businesses off and look hard at routes with unusually high counts for their footprint. In Spring, Tomball and Magnolia, rural routes cover huge areas with fewer homes each, so your 5,000 pieces stretch further on the map than you’d guess.</p>"""),

            ("Worked examples: three ways to reach 5,000 homes in The Woodlands", f"""<p>Here are three versions of the same goal. A home services company (pick your trade) wants 5,000 single-family homes across Alden Bridge, Cochran’s Crossing and Sterling Ridge. Postage figures use the rates cited above. Everything else is an estimate and marked that way.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>A: EDDM Retail, one drop, 6.25 x 11</th><th>B: Targeted homeowner list, 6 x 9 postcard</th><th>C: EDDM Retail, three drops, same routes</th></tr></thead>
<tbody>
<tr><td>Postage</td><td>5,000 x $0.260 = $1,300</td><td>5,000 x about $0.395 = $1,975 (5-digit Marketing Mail letter rate)</td><td>15,000 x $0.260 = $3,900</td></tr>
<tr><td>Printing (estimate)</td><td>$450 to $850</td><td>$350 to $700</td><td>$1,100 to $2,000</td></tr>
<tr><td>List rental (estimate)</td><td>$0</td><td>$250 to $600</td><td>$0</td></tr>
<tr><td>Mail prep or presort (estimate)</td><td>Your time, about 4 to 6 hours</td><td>$200 to $450 at a mail house</td><td>Your time, three times</td></tr>
<tr><td>Design (estimate)</td><td>$300 to $800</td><td>$300 to $800</td><td>$500 to $1,200 for three versions</td></tr>
<tr><td><b>Total (estimate)</b></td><td><b>About $2,050 to $2,950</b></td><td><b>About $3,075 to $4,525</b></td><td><b>About $5,500 to $7,100</b></td></tr>
<tr><td>Cost per household</td><td>About $0.41 to $0.59</td><td>About $0.62 to $0.91</td><td>About $1.10 to $1.42 for three touches</td></tr>
</tbody></table></div>
<p>Example A is the classic. It’s the cheapest way to hit every door, and it’s the right call for a restaurant, a gym or a pest control company where nearly every household is a prospect.</p>
<p>Example B costs about half again as much, and it can still be the cheaper campaign. A list lets you mail only owner-occupied homes, or only homes built before 2005 for an HVAC replacement offer, or only households that moved in recently (see our {L(MOVER, 'new-mover marketing playbook')}). If half the homes on a saturation drop could never buy from you, you paid for them anyway.</p>
<p>Example C is what we’d recommend to most service businesses that can afford it. One postcard is a coin flip. Three to the same homes, a few weeks apart, with the same offer and a consistent look, give people a chance to notice you before they need you. Our {L('/blog/billboard-advertising-cost-houston/', 'billboard cost guide')} makes the same point about frequency on I-45.</p>"""),

            ("Targeted lists vs. saturation: when paying more per piece is cheaper", f"""<p>Saturation mail (EDDM) goes to every address on a route with no names. Targeted mail goes to specific addresses from a list, usually with a name, at Marketing Mail or First-Class rates. MailPro’s table shows commercial Marketing Mail letters at $0.395 per piece at 5-digit presort after July 12, 2026, rising to $0.435 and $0.467 at the looser presort tiers, per {SRC['mp_jul']}. Your mail house will tell you which tier your list hits.</p>
<p>The trade is simple to state. Saturation is cheaper per piece and wasteful by design. A list is pricier per piece and wastes less. Which wins depends on how much of a route is a real prospect.</p>
<ul>
<li><b>Saturation tends to win</b> for restaurants, coffee shops, dentists, gyms, pest control, lawn care and anything with broad appeal in a tight radius.</li>
<li><b>Lists tend to win</b> for pool builders, remodelers, solar, financial advisors, senior living and any offer where homeowner status, age or home value decides whether someone can buy.</li>
<li><b>Lists are the only option</b> when you want to mail people by name, follow up with the same people online, or reach new movers.</li>
</ul>
<p>Lists also open a door that EDDM can’t. Because you have names and addresses, you can match them to Facebook and Instagram audiences or Google Customer Match and show ads to the same households. Google requires 90 days of account history and more than $50,000 in lifetime spend for Customer Match targeting; smaller accounts get observation and exclusions only, per {SRC['cm']}. Meta’s customer list audiences have no such spend threshold, though match rates on purchased postal lists are often modest.</p>"""),

            ("What a response costs: break-even math for a Houston mail drop", f"""<p>Response rates for mail vary so much by offer, list and design that we won’t quote a benchmark. The more useful question is how many customers you need for the drop to pay for itself.</p>
<p>Take Example A at about $2,500 all in. If a new customer is worth $250 in gross profit on the first job, you need 10 customers from 5,000 homes, which is one in 500. If a customer is worth $1,000 (an AC tune-up plan that turns into a replacement, say), you need three.</p>
<!--fig:breakeven-->
<p>Use gross profit, not revenue. And count lifetime value only if you actually have repeat business you can measure. A lawn care company in Cochran’s Crossing that keeps customers for four seasons can justify a mail program a one-time junk removal job never could. Our {L('/blog/understanding-cost-per-lead/', 'cost per lead guide')} has the same math for digital channels, so you can compare mail against your Google Ads on the same terms.</p>"""),

            ("Tracking direct mail responses without fooling yourself", f"""<p>Most mail “doesn’t work” because nobody could see it working. Fix that before the cards are printed.</p>
<ol>
<li><b>A unique phone number</b> on the card, forwarding to your main line and recorded. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers setup.</li>
<li><b>A QR code and a short URL</b> that land on a page made for the mailer, with UTM tags (utm_source=mail, utm_medium=eddm, utm_campaign=woodlands-fall) so Google Analytics can separate the traffic.</li>
<li><b>An offer code</b> that front-desk staff type into the booking system. Short and spoken-friendly: WOODLANDS25, not WD-25-OCT-B.</li>
<li><b>A matchback</b> after 60 to 90 days. Export new customers’ addresses and compare them to the routes or list you mailed. Many people who respond to mail never scan or quote a code; they just search your name. Matchback catches them.</li>
<li><b>A holdout group.</b> Skip a few comparable routes on purpose and compare new-customer rates in mailed vs. unmailed routes. It’s the only honest way to see lift.</li>
</ol>
<!--fig:funnel-->
<p>The matchback is the step people skip, and it often changes the verdict. Branded search and direct traffic usually rise in the week a mailer lands, so watch your Google Business Profile calls and branded search clicks in Search Console for those ZIP Codes too.</p>"""),

            ("Direct mail design that works in a Woodlands mailbox", f"""<p>Your card gets a couple of seconds between the mailbox and the recycling bin. People in The Woodlands get a lot of mail from realtors, roofers and HVAC companies, especially after a storm, so the bar is real.</p>
<!--fig:design-->
<p>Two notes from accounts we’ve run. The side with the address block gets read first, so put the offer there, not a logo. And photos of a real local job or a real team beat stock imagery, because people can tell the difference between a Woodlands street and a stock-photo cul-de-sac in Phoenix.</p>"""),

            ("Pairing mail with digital: retargeting, matchback and Informed Delivery", f"""<p>Mail does better when it isn’t alone. Three pairings are worth setting up for any drop over a couple thousand dollars.</p>
<p><b>Geo-targeted ads on the same streets.</b> EDDM has no names, so you can’t upload it as an audience. You can target the same ZIP Codes or a radius around those routes on Meta and Google from a few days before the in-home date until two weeks after, with creative that matches the card. Our {L('/blog/geo-fencing-ads-target-customers-nearby/', 'geofencing guide')} explains what tight radius targeting can and can’t do, and {L('/blog/retargeting-explained/', 'retargeting explained')} covers following up with people who visited the mailer’s landing page.</p>
<p><b>Informed Delivery.</b> Households enrolled in USPS Informed Delivery get a morning email with images of the day’s mail. Mailers can add a clickable “ride-along” image and a link to that preview at no charge, and USPS suggests running the campaign from 3 days before to 3 days after the in-home date, per {SRC['idp']}. For saturation mail, that generally means going through a mail service provider who submits eDoc files.</p>
<p><b>Matchback into your ad platforms.</b> If you mailed a named list, upload the list as a custom audience and as a conversion exclusion for existing customers. Then compare cost per new customer for households that got mail plus ads against households that got ads alone.</p>
<p>If you’d like a senior strategist to price out mail alongside your search and social budget, <a href="/contact/">get in touch</a> and tell us what you sell and where. Our {L('/services/paid-social-advertising/', 'paid social')} and {L('/services/search-marketing/', 'search')} teams build the digital half of these campaigns.</p>"""),
        ],
        "faq": [
            ("How much does EDDM cost in The Woodlands and Houston in 2026?",
             "EDDM Retail postage is $0.260 per piece since July 12, 2026, so 5,000 homes costs $1,300 in postage alone. Add printing, which we estimate at roughly $0.09 to $0.17 per piece for a 6.25 by 11 card at that quantity, plus design. A realistic all-in figure for one 5,000-home drop is around $2,000 to $3,000. USPS has asked to move its next increase to January 2027, so check rates before printing."),
            ("What size does an EDDM postcard have to be?",
             "An EDDM Retail piece must be a flat, which means it is longer than 10-1/2 inches, taller than 6-1/8 inches or thicker than 1/4 inch. It can weigh up to 3.3 ounces, and the maximum size is generally 12 by 15 inches. Common sizes are 6.25 by 9, 6.25 by 11 and 8.5 by 11. A standard 4 by 6 postcard does not qualify for EDDM."),
            ("Is there a limit on how many EDDM pieces I can drop off in Houston?",
             "Yes. EDDM Retail allows no more than 5,000 pieces per day per 5-digit ZIP Code, and each mailing needs at least 200 pieces unless the area has fewer addresses. Pieces go to the post office that serves the routes, bundled in groups of 50 to 100 with facing slips. Larger drops usually go through a mail house using EDDM BMEU, which has no daily cap."),
            ("Is EDDM or a targeted mailing list better for a Woodlands business?",
             "EDDM is cheaper per piece and works when nearly every household is a prospect, like restaurants, gyms or pest control. A targeted list costs more per piece but lets you mail only homeowners, certain home ages or new movers, and lets you follow up with the same households in Meta and Google ads. If half of a route could never buy from you, the list is often cheaper per customer."),
            ("How do I track whether a direct mail campaign worked?",
             "Put a unique tracked phone number, a QR code with UTM tags and a simple offer code on every piece. After 60 to 90 days, match new customers' addresses against the routes or list you mailed, because many responders just search your business name. Leave a few comparable routes unmailed as a holdout group so you can compare new-customer rates and see the real lift."),
        ],
        "figures": {
            "rates": {
                "type": "stats",
                "title": "EDDM Retail rules at a glance, 2026",
                "stats": [["$0.260", "per piece since July 12, 2026"], ["3.3 oz", "maximum weight per piece"], ["5,000", "pieces per day per ZIP Code"], ["200", "minimum pieces per mailing"]],
                "note": "Source: MailPro rate table, USPS DMM 143",
                "alt": "Stats on 2026 EDDM Retail postage rate, weight limit and quantity rules for direct mail in The Woodlands and Houston",
                "caption": f"From {SRC['mp_jul']} and {SRC['dmm143']}.",
            },
            "retailbmeu": {
                "type": "compare",
                "title": "EDDM Retail vs. EDDM BMEU",
                "left": {"title": "EDDM Retail", "items": ["$0.260 per piece, no permit", "5,000 pieces per day per ZIP", "You bundle, label and drop off", "Pieces up to 3.3 oz", "Best under about 10,000 pieces"]},
                "right": {"title": "EDDM BMEU", "items": ["Lower postage, priced by entry point", "No daily cap", "Mail house usually preps and enters it", "Heavier pieces at a per-pound price", "Best for big or monthly drops"]},
                "alt": "Comparison of EDDM Retail and EDDM BMEU options for direct mail campaigns in The Woodlands and Houston",
                "caption": "Ask any mail house to show postage as its own line so you can compare quotes.",
            },
            "map": {
                "type": "map",
                "title": "Where a 5,000-home drop lands north of Houston",
                "sub": "The Woodlands villages and nearby towns where carrier routes vary most in size",
                "highlight": ["The Woodlands", "Spring", "Shenandoah", "Tomball", "Magnolia", "Conroe"],
                "alt": "Map of The Woodlands, Spring, Tomball, Magnolia and Conroe for planning EDDM carrier routes north of Houston",
                "caption": "Suburban Woodlands routes are dense. Rural routes around Magnolia and Montgomery cover far more ground per home.",
            },
            "tool": {
                "type": "steps",
                "title": "Planning a drop in the EDDM mapping tool",
                "sub": "How we pick about 5,000 homes in The Woodlands",
                "steps": [["Start from your shop or service area", "Enter an address or ZIP Code, then zoom to street level."], ["Turn off business addresses", "Keep residential only unless you sell to businesses."], ["Filter by the Census data", "Use age, income and household size to drop poor-fit routes."], ["Add routes until you hit the count", "Watch the running total. Stop near 5,000 if dropping in one day per ZIP."], ["Export the route list", "Save it for bundling, for matchback, and for matching ad geo-targets."]],
                "alt": "Five steps to plan an EDDM carrier route mailing in The Woodlands and Houston using the USPS mapping tool",
                "caption": "Save the route list. You’ll need it again for tracking and for digital targeting.",
            },
            "breakeven": {
                "type": "bars",
                "title": "Customers needed to break even on $2,500",
                "sub": "By gross profit per new customer",
                "items": [["$100 profit per customer", 25, "25"], ["$250 profit per customer", 10, "10"], ["$500 profit per customer", 5, "5"], ["$1,000 profit per customer", 2.5, "3"]],
                "highlight": [1],
                "note": "Illustrative example",
                "alt": "Bar chart of break-even customers for a direct mail campaign in The Woodlands and Houston by profit per customer",
                "caption": "Know your gross profit per customer before you pick a mail budget.",
            },
            "funnel": {
                "type": "funnel",
                "title": "How a mail drop shows up in your data",
                "stages": [["5,000 homes mailed", "100%"], ["Card read, not tossed", "Unknown"], ["Searched or scanned", "Tracked"], ["Called or booked", "Tracked"], ["Matched new customers", "Matchback"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how an EDDM direct mail drop in The Woodlands turns into tracked calls, bookings and matchback customers",
                "caption": "The bottom row is the one that counts. Everything above it is a hint.",
            },
            "design": {
                "type": "checklist",
                "title": "Mail design checklist",
                "sub": "What we check before a card goes to print",
                "items": ["One offer, stated in under ten words", "Offer on the address side", "A deadline with a real date", "Phone number big enough to read at arm’s length", "QR code tested on two phones", "A local photo, not stock", "Service area named: The Woodlands, Spring, Conroe", "Reviews or rating, if they’re strong", "Indicia and address block from the printer’s template"],
                "alt": "Checklist for designing EDDM and direct mail postcards for businesses in The Woodlands and Houston",
                "caption": "If your card needs a paragraph to explain the offer, the offer needs work.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: new-mover playbook
    {
        "slug": "new-mover-marketing-the-woodlands-houston",
        "title": "New-Mover Marketing in The Woodlands and Houston: Reaching People the Month They Move In",
        "seo_title": "New-Mover Marketing in The Woodlands & Houston",
        "desc": "A new-mover marketing playbook for The Woodlands and Houston: where mover data really comes from, HOA and realtor routes, Meta limits and a 90-day sequence.",
        "category": "Local marketing",
        "icons": ["Meta", "Facebook", "Google Ads"],
        "art": "b2",
        "hero": "house",
        "hero_alt": "Illustration of a house for new-mover marketing in The Woodlands, Houston, Spring and Conroe",
        "related": ["real-estate-agent-marketing-the-woodlands-houston", "moving-company-marketing-houston", "grand-opening-marketing-plan-30-days"],
        "sections": [
            (None, f"""<p><b>Myth:</b> the post office will sell you a list of everyone who filed a change of address in your ZIP Code.</p>
<p>It won’t. {SRC['uspspriv']} says it plainly: “We do not sell customer or mailing lists to outside parties, including marketers.” The change-of-address data that does leave USPS goes to licensed vendors, and the license forbids using it to build new-mover lists. More on that below.</p>
<p>New-mover marketing in The Woodlands and Houston still works. It just runs on different pipes than most people assume: compiled lists from licensed data companies, the people who hand new residents their keys (realtors, title companies, builders, leasing offices, HOAs), and ads aimed at the streets where people are moving in. This playbook covers why the first months after a move matter so much, how many people are landing in Montgomery and Harris counties, where the data comes from, a day-by-day timing sequence, and which businesses get the most out of it.</p>"""),

            ("Why new movers in Houston matter more than almost any other audience", f"""<p>Moving resets a household’s defaults. The dentist, the pest control company, the vet, the pizza place, the gym: all of it gets chosen again, usually within a few weeks, usually by whoever shows up first with a decent offer and good reviews.</p>
<p>The spending is real, and it’s measurable. NAHB looked at Consumer Expenditure Survey data from 2020 through 2023 and found that buyers of newly built single-family homes spent $26,882 on appliances, furnishings and alterations or repairs in their first year, nearly three times the $9,457 spent by owners who didn’t move. Buyers of existing homes spent $18,673, about double, per {SRC['nahb']}.</p>
<!--fig:spend-->
<p>The split matters for who should care. New-home buyers spent $14,285 on alterations and repairs, mostly customization like landscaping and patios, while existing-home buyers leaned toward replacing things: HVAC, flooring, paint and roofs. Furnishings jumped to $8,254 for new-home buyers against $1,192 for non-movers. NAHB’s {SRC['nahb2']} adds that appliance spending mostly fades after year one. If you sell any of that, the window is short.</p>
<!--fig:stats-->
<p>And movers are getting scarcer nationally. About 11% of Americans moved in 2024, roughly one in nine, which {SRC['axmove']} reported as a record low in data going back to 1948. Fewer movers means each one is worth more to the businesses competing for them.</p>"""),

            ("How many people are moving into Houston and The Woodlands", f"""<p>Nationally, people are staying put. Houston didn’t get the memo.</p>
<p>The Houston metro added 126,720 people between July 2024 and July 2025, the largest gain of any U.S. metro, according to Census estimates reported by {SRC['abc13c']}. Growth slowed compared with the year before, and {SRC['axhou']} put Harris County’s gain at nearly 49,000, still the most of any county in the country. Montgomery County reached an estimated 781,194 residents on July 1, 2025, up 25.9% since April 2020, per {SRC['qfmc']}. About 71.8% of its homes are owner-occupied.</p>
<!--fig:map-->
<p>Those are net figures. The number of households that actually change addresses is much larger, because people also move within the region: a family trades a Spring starter home for a bigger house in Creekside Park, a couple leaves an apartment near Hughes Landing for a townhome in Conroe, someone relocates from Katy to be closer to an employer on Research Forest. Every one of those households is a new mover to the businesses around their new address.</p>
<p>The growth isn’t evenly spread. New subdivisions along the Grand Parkway, I-45 north of Conroe, FM 1488 toward Magnolia and the 249 corridor through Tomball produce whole streets of new movers at once. Older Woodlands villages like Grogan’s Mill and Panther Creek turn over a few houses at a time.</p>"""),

            ("Where new-mover data actually comes from", f"""<p>Back to the myth. USPS licenses its National Change of Address data to a limited set of vendors, but only as a list-cleaning tool. The text USPS requires those vendors to publish says NCOALink processing exists “to provide a mailing list correction tool,” and that it “may not be used to create, generate, or maintain new movers lists,” per {SRC['ncoa']}.</p>
<p>So NCOA is useful for one thing: if a customer already on your list moves, NCOA processing can update their address before your next mailing. It will not tell you who just arrived on your street.</p>
<!--fig:pipes-->
<p>For finding the people who just arrived, there are other sources. Here’s how they compare:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Source</th><th>What you get</th><th>How fresh</th><th>Watch out for</th></tr></thead>
<tbody>
<tr><td>Compiled new-homeowner lists from licensed data companies</td><td>Name and address of recent buyers, often weekly or monthly updates by ZIP</td><td>Days to weeks after a deed records</td><td>Ask each vendor for its sources in writing and how often it updates</td></tr>
<tr><td>Compiled new-renter lists</td><td>Recent renters by building or ZIP</td><td>Varies widely</td><td>Coverage of apartments is patchier than homeowners</td></tr>
<tr><td>Pre-mover lists (homes newly listed for sale)</td><td>Households about to leave, useful for movers, cleaners, storage</td><td>Before the move</td><td>They’re leaving your area, so they’re a different audience</td></tr>
<tr><td>NCOA processing of your own list</td><td>Updated addresses for existing customers</td><td>When you run it</td><td>Can’t be used to build a new-mover list</td></tr>
<tr><td>EDDM to new-construction routes</td><td>Every door on routes in a new subdivision</td><td>As routes fill in</td><td>No names; new routes may not appear until homes are occupied</td></tr>
<tr><td>Partners: realtors, title, builders, leasing offices, HOAs</td><td>Your offer in the welcome packet or closing bag</td><td>The week they move</td><td>Rules on gifts and referrals, covered below</td></tr>
</tbody></table></div>
<p>A good list vendor will sell by ZIP Code and radius, filter homeowners from renters, and deliver new records on a schedule so you can mail every week or two. Price varies by vendor and filter; get it per record, and ask whether you can suppress records you’ve already mailed. Our {L(EDDM, 'EDDM and direct mail cost guide')} has the postage and printing math for small weekly drops.</p>"""),

            ("HOA, village association and welcome-packet routes", f"""<p>Some of the best new-mover placements cost nothing but a relationship.</p>
<p>In The Woodlands, the Township lists eight village associations, from Alden Bridge to Sterling Ridge, per {SRC['twp']}. Village associations hold events and run newsletters, and they’re run by residents who care about local businesses being decent neighbors. Sponsor something useful (a cleanup day, a National Night Out table) before you ask for anything. In master-planned communities around Cypress, Katy, Conroe and Montgomery County, the HOA or the developer’s lifestyle team often runs new-resident events and welcome packets. Ask the community manager what’s allowed. Some accept local business inserts; some don’t, and pushing will get you remembered for the wrong reason.</p>
<p>What to put in a welcome packet: a single card or magnet with a specific first-visit offer, an expiration date about 60 days out, and a QR code to a page that says “Welcome to [community name].” Skip the trifold brochure. It goes into the junk drawer with the cable company’s.</p>"""),

            ("Realtors and title companies: partnerships that stay on the right side of the rules", f"""<p>Realtors and title companies see every buyer in the week that matters. Plenty of them hand out closing gifts and “welcome to the neighborhood” guides, and a well-made local guide with your business in it is a gift agents are happy to give.</p>
<p>A few patterns that work in Houston and The Woodlands:</p>
<ul>
<li>A co-branded neighborhood guide that a team of agents gives every buyer in Spring, The Woodlands or Conroe, with five to ten trusted local businesses and a real offer from each.</li>
<li>A closing-day item from you that’s useful (an HVAC filter-size sticker and first-service discount, a pest control “first spray” certificate, a restaurant gift card).</li>
<li>Monthly agent lunches or short educational sessions where you teach something buyers ask agents about, like foundation movement in Houston clay or what a home warranty does and doesn’t cover.</li>
</ul>
<p>The legal caution applies to anyone in the real estate settlement business: title companies, lenders, home warranty providers and some inspectors. The Real Estate Settlement Procedures Act’s Section 8 bars giving or accepting anything of value in exchange for referrals of settlement service business on federally related mortgage loans. {SRC['respa']} walk through how that applies to marketing arrangements. If you’re a restaurant or a dentist, RESPA generally isn’t your issue, but the agent you partner with may have brokerage rules about what they can promote. Ask. Our {L('/blog/real-estate-agent-marketing-the-woodlands-houston/', 'post on how local agents market themselves')} helps you pitch something they’ll actually want.</p>"""),

            ("Apartment move-ins: Houston’s overlooked new movers", f"""<p>Renters move more often than owners, and Houston builds a lot of apartments. A new building in Spring, along the Grand Parkway or near Hughes Landing in The Woodlands can lease hundreds of units in a year, which means hundreds of households choosing a gym, a dry cleaner, a vet and a place to get tacos.</p>
<p>Three ways in. First, the leasing office: offer something residents like (a resident appreciation breakfast you cater, a pet-wash day) and ask to be in the move-in bag. Second, EDDM to the building’s carrier route once it’s occupied, though some large complexes have centralized mailrooms that change how mail is delivered, so check the route counts. Third, tight radius ads around buildings in lease-up, which is where the next section picks up.</p>"""),

            ("Meta and Google targeting for new movers: what’s left in 2026", f"""<p>Facebook used to let you target people who had “recently moved” with a few clicks. Don’t build a plan on that anymore.</p>
<p>Meta has been cutting detailed targeting options in waves: a batch in early 2024, detailed targeting exclusions in August 2024, another round announced in June 2025, with the latest removals taking effect January 15, 2026, when ad sets still using them stopped delivering, per {SRC['smt']}. Meta hasn’t published a full list. Open Ads Manager, search detailed targeting for “moved,” and see what your account shows today. If a life-event option is still there, treat it as a weak hint layered on a tight location, not a list of movers.</p>
<p>If you sell housing itself (builders, apartments, realtors), your ads run under Meta’s Housing special ad category, with its own limits on location and audience options.</p>
<p>What still works on Meta:</p>
<ul>
<li><b>Upload your new-mover list</b> as a custom audience every time you mail it, and run ads to the same households during the mail window.</li>
<li><b>Radius targeting around new subdivisions and apartment buildings</b> in lease-up, with creative that names the community.</li>
<li><b>Creative that speaks to movers.</b> “New to The Woodlands? Your first cleaning is $49” does more targeting work than any setting.</li>
</ul>
<p>On Google, new movers do the targeting for you by searching. “Dentist near me,” “pest control Conroe,” “vet Spring TX” spike when people arrive. Make sure your Google Business Profile is complete and your reviews are strong, and run search campaigns on the services people need in the first month. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} and {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads guide')} cover the setup.</p>"""),

            ("The new-mover timing sequence: day 0 to day 90", f"""<p>Speed matters, and so does repetition. Here’s the sequence we’d run for a household-services business with a weekly new-homeowner list for a handful of ZIP Codes around The Woodlands, Spring and Conroe:</p>
<!--fig:sequence-->
<p>Two details make or break it. Suppress anyone who becomes a customer, immediately, so you don’t send a “welcome, here’s 20% off” card to someone who paid full price last week. And keep the offer and look consistent across all touches so the third one feels familiar.</p>"""),

            ("Which businesses get the most from new-mover marketing", f"""<p>Anything people choose once and keep for years benefits most. Anything bought on impulse benefits least.</p>
<!--fig:fit-->
<p>A Woodlands dentist who wins a family of four in their first month might keep them for a decade. An HVAC company that does the first tune-up on a 2006 system in Indian Springs is first in line when that system dies in August. A restaurant gets a lift too, but a smaller one per household, so it should lean on cheaper channels like EDDM and welcome packets rather than paying for weekly list drops.</p>"""),

            ("What to track and what a new-mover program costs", f"""<p>Run the program as a sequence and judge it as one. Track the cost per mover reached (list record, printing, postage and any ads to that household), the share of movers who became customers within 90 days, and the gross profit those customers produced in their first year.</p>
<!--fig:track-->
<p>Program costs depend on volume. A weekly list for three Woodlands ZIP Codes might mean a few hundred records a month in busy seasons, and summer is usually busiest because families move between school years. Budget for postage at the current Marketing Mail rate, small-batch printing (which costs more per piece than a 5,000-card run), the list itself and a modest ad budget for the custom audience. Make the offer specific and time-limited, and route calls to a person who answers. New movers call the first number that picks up, which is why our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} matters here as much as for any ad campaign.</p>
<p>If you want a senior strategist to design a new-mover program around your service area, <a href="/contact/">get in touch</a> and tell us what a new customer is worth to you. We’ll build the plan from there.</p>"""),
        ],
        "faq": [
            ("Can I buy a list of new movers from the post office?",
             "No. USPS says it does not sell customer or mailing lists to marketers, and its National Change of Address data is licensed only as a mailing list correction tool. The license text says it may not be used to create or maintain new-mover lists. Businesses in The Woodlands and Houston buy compiled new-homeowner and new-renter lists from licensed data companies instead, usually by ZIP Code and updated weekly or monthly."),
            ("How much do new homeowners spend after moving?",
             "NAHB analysis of Consumer Expenditure Survey data from 2020 to 2023 found that buyers of newly built homes spent $26,882 on appliances, furnishings and alterations or repairs in their first year, about three times the $9,457 spent by owners who did not move. Buyers of existing homes spent $18,673, about double. Appliance spending mostly fades after the first year, so timing matters."),
            ("Can I still target people who recently moved on Facebook?",
             "Don't count on it. Meta has removed detailed targeting options in several waves, most recently on January 15, 2026, and has not published a full list. Check Ads Manager to see what your account shows. The more reliable approach is to upload a purchased new-mover list as a custom audience, target tight radiuses around new subdivisions, and write ads that speak directly to people new to the area."),
            ("Which Houston businesses benefit most from new-mover marketing?",
             "Businesses people choose once and keep for years: dentists, pediatricians, vets, HVAC, pest control, lawn care, pool service, insurance agents, gyms, hair salons, churches and auto repair shops. Furniture, window covering and home improvement companies benefit because spending in those categories jumps in the first year. Restaurants benefit too, but should use cheaper channels like EDDM and welcome packets."),
            ("When should I contact new movers in The Woodlands?",
             "As soon as possible after they arrive, ideally within the first two weeks, then again at about 30 and 60 days. A good sequence is a welcome postcard with a specific first-visit offer, matching ads to the same households, a reminder card before the offer expires and a final touch around day 60 to 90. Stop contacting anyone the moment they become a customer."),
        ],
        "figures": {
            "spend": {
                "type": "bars",
                "title": "First-year home spending after a move",
                "sub": "Appliances, furnishings and alterations or repairs, single-family homes",
                "items": [["Bought a newly built home", 26882, "$26,882"], ["Bought an existing home", 18673, "$18,673"], ["Did not move", 9457, "$9,457"]],
                "highlight": [0],
                "note": "Source: NAHB analysis of Consumer Expenditure Survey data, 2020-2023",
                "alt": "Bar chart of first-year spending by new home buyers versus non-movers, relevant to new-mover marketing in The Woodlands and Houston",
                "caption": f"From {SRC['nahb']}.",
            },
            "stats": {
                "type": "stats",
                "title": "New movers by the numbers",
                "stats": [["$8,254", "furnishings, new-home buyers, year one"], ["$14,285", "alterations and repairs, new-home buyers"], ["11%", "of Americans moved in 2024, a record low"], ["781K", "Montgomery County residents, 2025"]],
                "note": "Sources: NAHB, Axios, Census QuickFacts",
                "alt": "Stats on new mover spending and Montgomery County growth for new-mover marketing in The Woodlands and Houston",
                "caption": f"From {SRC['nahb']}, {SRC['axmove']} and {SRC['qfmc']}.",
            },
            "map": {
                "type": "map",
                "title": "Where Houston’s new movers are landing",
                "sub": "Growth corridors with streets of new households at once",
                "highlight": ["The Woodlands", "Conroe", "Magnolia", "Montgomery", "Tomball", "Cypress", "Katy", "Fulshear", "Porter"],
                "alt": "Map of Greater Houston growth areas for new-mover marketing, including The Woodlands, Conroe, Magnolia, Cypress and Katy",
                "caption": "New subdivisions produce movers in batches. Established villages turn over a few homes at a time.",
            },
            "sequence": {
                "type": "steps",
                "title": "A 90-day new-mover sequence",
                "sub": "For a household-services business in The Woodlands, Spring and Conroe",
                "steps": [["Days 0-14: welcome card", "Postcard with a specific first-visit offer, a 60-day deadline and a welcome landing page."], ["Days 0-30: matching ads", "Upload the same list as a Meta custom audience; run ads that name the community."], ["Day 30: reminder", "Second card or letter with the same offer and a customer review."], ["Day 45-60: last call", "A short card before the offer expires, plus your Google reviews link."], ["Day 90: hand-off", "Non-responders move to your regular seasonal mail or EDDM."]],
                "alt": "Five-step 90-day timing sequence for new-mover marketing in The Woodlands and Houston",
                "caption": "Suppress new customers at every step.",
            },
            "fit": {
                "type": "checklist",
                "title": "Businesses that gain most from new movers",
                "sub": "Chosen once, kept for years",
                "items": ["Dentists, orthodontists and pediatricians", "Veterinarians and pet groomers", "HVAC and plumbing service plans", "Pest control and lawn care", "Pool service", "Insurance agents", "Gyms, yoga and pilates studios", "Hair salons and barbers", "Auto repair shops", "Furniture and window coverings"],
                "alt": "Checklist of business types that benefit most from new-mover marketing in The Woodlands and Houston",
                "caption": "If a customer stays for years, a new-mover program can pay for itself on a handful of wins.",
            },
            "track": {
                "type": "funnel",
                "title": "Judging a new-mover program",
                "stages": [["Movers reached", "List + ads"], ["Visited or called", "Tracked"], ["First visit booked", "CRM"], ["Customer at 90 days", "Matchback"], ["Still a customer at 1 year", "Profit"]],
                "note": "Illustrative example",
                "alt": "Funnel for tracking a new-mover marketing program in The Woodlands and Houston from movers reached to first-year customers",
                "caption": "The last row decides whether the program stays.",
            },
            "pipes": {
                "type": "compare",
                "title": "What people assume vs. how it works",
                "left": {"title": "The assumption", "items": ["USPS sells new-mover lists", "NCOA finds new residents", "Facebook targets movers in one click", "One welcome card is enough"]},
                "right": {"title": "How it works", "items": ["Licensed data companies compile lists", "NCOA only updates your own customers", "Upload lists and use tight radiuses", "Three or four touches over 90 days"]},
                "alt": "Comparison of new-mover marketing myths and how it really works for businesses in The Woodlands and Houston",
                "caption": f"USPS policy from {SRC['uspspriv']} and {SRC['ncoa']}.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: trade show guide
    {
        "slug": "trade-show-marketing-houston-otc-conventions",
        "title": "Trade Show Marketing in Houston: OTC, Reliant Park and George R. Brown Conventions",
        "seo_title": "Trade Show Marketing in Houston: OTC, Reliant Park & GRB",
        "desc": "A trade show marketing guide for Houston: OTC 2027 dates, Reliant Park and GRB shows, a 90-day timeline, geofencing limits, follow-up and cost per lead.",
        "category": "Strategy",
        "icons": ["LinkedIn", "Google Ads", "HubSpot"],
        "art": "b1",
        "hero": "industry",
        "hero_alt": "Illustration of industrial equipment for trade show marketing at OTC and Houston conventions",
        "related": ["b2b-marketing-houston-energy-industrial", "geo-fencing-ads-target-customers-nearby", "speed-to-lead-response-time-follow-up-crm"],
        "sections": [
            (None, f"""<p>Nearly 25,000 people attended OTC in Houston in May 2026. Nearly 1,000 companies exhibited, and attendees came from more than 100 countries, per {SRC['otc26']}. Most of those exhibitors went home with a stack of badge scans, and a lot of those scans were never called.</p>
<p>That’s the pattern we see with trade show marketing in Houston. Companies spend most of their budget and energy on the four days on the floor, and very little on the 90 days before and after, which is where meetings get booked and pipeline gets made.</p>
<p>This guide is built as a timeline. It starts with the 2027 Houston calendar, including verified OTC dates, then the venues, then a week-by-week plan from 90 days out to 90 days after. Along the way: pre-show outreach that fills a calendar, booth design and lead capture, what geofencing around Reliant Park and the George R. Brown can and can’t do, a follow-up cadence, how to measure cost per lead and pipeline, and cheaper alternatives for companies that can’t justify a booth.</p>"""),

            ("The 2027 Houston trade show calendar", f"""<p>Start with the dates, since everything else counts backward from them.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Show</th><th>2027 dates</th><th>Venue</th><th>Who walks it</th></tr></thead>
<tbody>
<tr><td>NAPE Summit</td><td>February 3-5</td><td>George R. Brown Convention Center</td><td>Upstream deal-makers: land, minerals, prospects, A&amp;D</td></tr>
<tr><td>CERAWeek by S&amp;P Global</td><td>Check ceraweek.com (2026 ran March 23-27)</td><td>Hilton Americas-Houston and GRB</td><td>Energy executives, policymakers, investors, tech</td></tr>
<tr><td>OTC + URTeC (co-located)</td><td>May 3-5</td><td>Reliant Park</td><td>Offshore and unconventional engineers, operators, suppliers</td></tr>
<tr><td>Turbomachinery &amp; Pump Symposia</td><td>October 18 (short courses), 19-21</td><td>George R. Brown Convention Center</td><td>Rotating equipment engineers, maintenance and reliability</td></tr>
</tbody></table></div>
<p>Sources: {SRC['nape']}, {SRC['cera']} for 2026, {SRC['otc27']} and {SRC['tps']}.</p>
<p>The big change for 2027 is OTC itself. It drops from four days to three, May 3-5, and shares the site with URTeC, the Unconventional Resources Technology Conference. Each keeps its own technical program, and the organizers are pitching broader exhibition access across both, per {SRC['jpt']}. For an exhibitor, that likely means more unconventional and shale operators walking past booths that used to see mostly offshore traffic. Rewrite your booth headline for both audiences, or pick one on purpose.</p>
<!--fig:otc-->
<p>Houston hosts plenty of other industry meetings at the GRB and the hotels downtown and in the Galleria area every month. Check {SRC['grb']} and the event calendars of your own trade associations for the ones your buyers attend.</p>"""),

            ("Reliant Park vs. George R. Brown: the two venues that matter", f"""<p>First, the name. NRG Park became Reliant Park on August 1, 2026, returning to the name it had when it opened in 2002, per {SRC['reliant']} and {SRC['abc13r']}. Same buildings, same parking lots off the 610 Loop and Kirby. Your 2027 materials should say Reliant Park, and your ad copy and landing pages should too, because attendees will search for the new name.</p>
<p>Reliant Park is a campus of a stadium, a convention center, an arena and the Astrodome, south of downtown. People drive, park and stay all day. Lunch options on site are limited, which is why so many OTC side meetings happen at hotels and restaurants nearby, or downtown and in the Galleria in the evening.</p>
<p>The George R. Brown is downtown on the east side, next to Discovery Green. Houston First lists 1.9 million usable square feet, the 1,200-room Hilton Americas-Houston as the headquarters hotel and the 1,000-room Marriott Marquis, both connected by skybridge, per {SRC['grb']}. That matters for planning. At a GRB show, buyers walk between the hall and two big hotel lobbies all day, so a lobby meeting or a suite is a short walk instead of a drive.</p>
<!--fig:map-->
<p>Where your buyers work matters as much as where the show is. Houston’s energy and industrial buyers cluster in the Energy Corridor along I-10 west, downtown, the Galleria and Westchase, The Woodlands (Research Forest and the offices around Hughes Landing), Sugar Land, and the plants and fabrication yards east toward Baytown and down toward Clear Lake. Many of them commute to the show every day, which shapes when your ads and emails should run.</p>"""),

            ("The timeline: 90 days out to 90 days after", f"""<p>Here’s the full plan in one view. The sections after this go deeper on each phase.</p>
<!--fig:timeline-->
<p>If you’re reading this in late November 2026, OTC is about 23 weeks away and NAPE about 10. For NAPE you’re already inside the 90-day window.</p>"""),

            ("Pre-show outreach that fills your calendar before you arrive", f"""<p>The best booth traffic is a meeting someone agreed to three weeks earlier. Walk-up traffic is a bonus.</p>
<p>Build a target account list first. Fifty to 150 named companies, with two or three named people at each: the engineer who specs your product, the person who approves the purchase, and the operations person who lives with it. Pull them from your CRM, your sales team’s wish list and LinkedIn. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston energy and industrial companies')} covers building this list properly.</p>
<p>Then run three waves:</p>
<ul>
<li><b>Six to eight weeks out:</b> a personal email from the salesperson who owns the account, not a marketing blast. One line on what you’re showing, one on why it matters to them, and a specific ask.</li>
<li><b>Three to four weeks out:</b> LinkedIn ads to a matched list of the same accounts, plus a second email with a booking link for 20-minute slots.</li>
<li><b>The week before:</b> a short reminder to confirmed meetings with booth number, parking or skybridge directions, and the salesperson’s cell.</li>
</ul>
<p>Sample email, which works because it’s short and specific:</p>
<blockquote><p>Subject: 20 minutes at OTC, booth [number]?</p>
<p>Mark, we’re showing the new subsea connector at OTC, May 3-5 at Reliant Park. [One sentence on a result you can prove.] Would Tuesday at 10:30 or Wednesday at 2:00 work for a quick look? Here’s my calendar if neither does.</p></blockquote>
<p>Fill the bracket with a real result, a customer name you have permission to use, or a spec that beats the alternative. If you don’t have one yet, cut the line rather than inventing it.</p>"""),

            ("Booth design and lead capture", f"""<p>Booths fail in predictable ways: too much text, no clear reason to stop, a table across the front like a border checkpoint, and staff looking at their phones.</p>
<p>Design for a three-second read from the aisle. One headline that says what you do and for whom, a product or demo people can touch, and an open front. At OTC + URTeC that headline should make sense to a shale completions engineer as well as a subsea project manager.</p>
<p>Lead capture is where the money is made or lost. Most shows rent lead retrieval apps that scan badges. A scan is a name, not a lead. Set up the app (or a simple form on a tablet) with qualifying fields your staff fill in during the conversation:</p>
<!--fig:capture-->
<p>Grade every lead A, B or C before the person walks away. A means a named project and a timeline, B means real interest without a project, C means a badge scan for the raffle. The grade decides how fast follow-up happens, and it keeps sales from ignoring the whole list because half of it is raffle entries.</p>"""),

            ("Geofencing Reliant Park and the George R. Brown: what the platforms allow", f"""<p>Agencies love to sell “geofence the convention center.” The platforms are more modest than the pitch.</p>
<p>Google Ads requires a radius of at least 1 km around any location, per {SRC['grad']}. Meta’s custom location targeting runs from 0.63 to 50 miles, which is 1 to 80 km, per {SRC['mrad']}. So the smallest circle you can draw on either platform is about 0.6 mile in radius. Around Reliant Park, that circle takes in the stadium, the parking lots, a stretch of the 610 Loop and surrounding neighborhoods. Around the GRB, it covers much of east downtown, Discovery Green, the hotels, the ballpark and nearby offices and apartments.</p>
<!--fig:geofence-->
<p>That doesn’t make it useless. It makes it a branding and reminder play, not precision targeting. What works:</p>
<ul>
<li>Run geo-targeted ads only during show days and hours, with creative that names the show and your booth number.</li>
<li>Use Google’s “presence” setting (people in the location) rather than the default that includes people interested in it.</li>
<li>Layer the geography with your matched account list on LinkedIn, and with show-name keywords on Google Search (“OTC 2027 exhibitors,” “OTC booth map”).</li>
<li>Keep the budget small. A few hundred dollars a day is plenty for a 1 km circle, and more just buys repeats to the same phones.</li>
</ul>
<p>Our {L('/blog/geo-fencing-ads-target-customers-nearby/', 'geofencing guide')} goes deeper on how location ads work and how to measure them.</p>"""),

            ("Post-show follow-up cadence", f"""<p>The week after a Houston show is when competitors forget to call. That’s your opening.</p>
<div class="bp-tbl"><table>
<thead><tr><th>When</th><th>Who it goes to</th><th>What it says</th></tr></thead>
<tbody>
<tr><td>Same evening</td><td>A leads</td><td>Personal email from the salesperson they met, referencing the conversation, with the promised file or quote date</td></tr>
<tr><td>Day 1-2</td><td>A leads</td><td>Phone call to set the next meeting</td></tr>
<tr><td>Day 3-5</td><td>B leads</td><td>Personal email with one useful resource and a soft ask</td></tr>
<tr><td>Day 7</td><td>All leads</td><td>Show recap email: what you showed, a short video, a booking link</td></tr>
<tr><td>Day 14-21</td><td>A and B non-responders</td><td>Second personal touch, plus LinkedIn ads to the uploaded list</td></tr>
<tr><td>Day 30-90</td><td>B and C leads</td><td>Monthly nurture email; hand back to sales when they engage</td></tr>
</tbody></table></div>
<p>Load every lead into your CRM before you leave Houston, tagged with the show, the grade and the person who met them. In HubSpot that’s a campaign plus a list per show; in Salesforce, a campaign with member status. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} explains why the first 24 hours count so much.</p>"""),

            ("Measuring trade show cost per lead and pipeline", f"""<p>Add up every cost: space, booth build or rental, drayage and labor, electrical and internet, travel, hotels, staff time, giveaways, sponsorships, ads and the dinner on Tuesday night. Then divide by qualified leads (A and B), meetings held, opportunities created and, eventually, revenue closed.</p>
<!--fig:funnel-->
<p>Our {L('/blog/understanding-cost-per-lead/', 'cost per lead guide')} covers the math in more detail, and {L('/blog/measure-marketing-success-metrics/', 'measuring marketing success')} covers which numbers to put in front of leadership.</p>
<p>Track pipeline for at least six months, longer if your sales cycle runs a year. Industrial deals that start at OTC in May often close the following spring. Credit the show for any opportunity where a contact from the show list is attached, and also report “influenced” pipeline for existing deals where the show meeting moved things forward.</p>
<!--fig:cpl-->
<p>The comparison that usually surprises people is cost per qualified lead by approach. A big booth produces the most raw scans, but a well-run hospitality suite or a calendar of hotel lobby meetings can produce more A leads per dollar. The numbers above are illustrative, not benchmarks; your own will depend on the show and how good your pre-show outreach is.</p>"""),

            ("Small-budget alternatives: hospitality suites, lobby meetings and dinners", f"""<p>Not every Houston company needs a booth at OTC. If your buyers attend but you can’t justify the floor, there are cheaper ways to be there.</p>
<ul>
<li><b>Hotel lobby meetings.</b> Book 20-minute meetings in the lobbies of the Hilton Americas or Marriott Marquis during a GRB show, or at a hotel near Reliant Park during OTC. The pre-show outreach is identical; you just name a lobby instead of a booth number.</li>
<li><b>A hospitality suite or private room.</b> A suite in a nearby hotel with coffee in the morning and drinks after the floor closes. Invite your target accounts, not the whole show.</li>
<li><b>A customer dinner.</b> Twelve people, a private room, no slides. Downtown, Midtown or the Galleria works for most shows.</li>
<li><b>Speaking or a technical paper.</b> For OTC, URTeC and TPS, a paper or panel gets your engineers in front of the right room for the cost of the work.</li>
</ul>
<p>Read the show’s rules first. Most shows prohibit soliciting on the exhibit floor without a booth (known as suitcasing) and may restrict events that compete with official programming. Stay off the floor with your pitch and you’ll stay on good terms.</p>
<p>If you want a senior strategist to build a pre-show and post-show plan around your next Houston event, <a href="/contact/">get in touch</a> and tell us which show, who you sell to and what a good year looks like. Our {L('/services/paid-social-advertising/', 'paid social')} and {L('/services/search-marketing/', 'search')} teams run the LinkedIn, Meta and Google side.</p>"""),
        ],
        "faq": [
            ("When is OTC 2027 in Houston?",
             "OTC 2027 runs May 3-5, 2027, at Reliant Park in Houston, co-located with URTeC, the Unconventional Resources Technology Conference. That's three days, down from four in 2026, and each event keeps its own technical program. Reliant Park is the former NRG Park, renamed on August 1, 2026. OTC 2026 drew nearly 25,000 attendees and nearly 1,000 exhibiting companies."),
            ("Can I geofence a Houston convention center with ads?",
             "Only loosely. Google Ads requires a radius of at least 1 km, and Meta's minimum custom location radius is 0.63 miles, which is also about 1 km. Around Reliant Park or the George R. Brown that circle covers the venue plus surrounding roads, hotels, offices and homes. Use it for show-day reminders with your booth number, layered with matched account lists and show-name search keywords."),
            ("How soon should I follow up with trade show leads?",
             "The same evening for your best leads, with a personal email from the salesperson they met, followed by a phone call within one to two days. Send everyone a recap email within a week, then a second personal touch around day 14 to 21 for anyone who has not replied. Load leads into your CRM with a grade before you leave Houston so nothing sits."),
            ("How do I measure trade show ROI?",
             "Add every cost, including space, booth, drayage, travel, hotels, staff time, giveaways and ads. Divide by qualified leads, meetings held, opportunities created and revenue closed. Track pipeline for at least six months, longer for industrial sales cycles, and report both sourced and influenced pipeline. Compare cost per qualified lead across booths, hospitality suites and lobby meetings to see what works best."),
            ("What are cheaper alternatives to a booth at a Houston trade show?",
             "Book pre-arranged meetings in the Hilton Americas or Marriott Marquis lobbies during George R. Brown shows, host a hospitality suite or a small customer dinner, or submit a technical paper. These need the same pre-show outreach as a booth but cost far less. Read the show's rules first, since most prohibit soliciting on the exhibit floor without a booth."),
        ],
        "figures": {
            "otc": {
                "type": "stats",
                "title": "OTC by the numbers",
                "stats": [["25K", "attendees at OTC 2026"], ["~1,000", "exhibiting companies"], ["100+", "countries represented"], ["May 3-5", "OTC + URTeC 2027"]],
                "note": "Source: OTC 2026 wrap-up release, OTC 2027 site",
                "alt": "Stats on OTC Offshore Technology Conference attendance and 2027 dates for trade show marketing in Houston",
                "caption": f"From {SRC['otc26']} and {SRC['otc27']}.",
            },
            "map": {
                "type": "map",
                "title": "Where Houston’s industrial buyers work",
                "sub": "Offices and plants your trade show audience commutes from",
                "highlight": ["The Woodlands", "Memorial", "Katy", "Galleria", "Sugar Land", "Baytown", "Clear Lake", "Houston"],
                "alt": "Map of Houston energy and industrial business areas for trade show marketing, including The Woodlands, Energy Corridor and Baytown",
                "caption": "Many attendees commute to the show daily, so morning and evening ads reach them near home and office as well.",
            },
            "timeline": {
                "type": "steps",
                "title": "Trade show timeline for Houston events",
                "sub": "From 90 days out to 90 days after",
                "steps": [["90-60 days out", "Pick the show, set goals, build the target account list, book space, hotels and suites."], ["60-30 days out", "Personal outreach wave one, booth headline and graphics, lead fields set up in the app."], ["30-7 days out", "LinkedIn ads to matched accounts, booking links, staff briefing, confirmations."], ["Show days", "Meetings, graded lead capture, geo-targeted reminders, nightly lead upload."], ["Days 1-21 after", "Same-day emails to A leads, calls, recap email, second touches."], ["Days 30-90 after", "Nurture B and C leads, report cost per lead and pipeline."]],
                "alt": "Six-phase timeline for trade show marketing in Houston at OTC, Reliant Park and George R. Brown events",
                "caption": "The days on the floor are one row of six.",
            },
            "capture": {
                "type": "checklist",
                "title": "Lead fields to fill in at the booth",
                "sub": "Ask during the conversation, type it before they leave",
                "items": ["Company and role", "Active project? Name and location", "Timeline: this quarter, this year, later", "Decision role: specifies, approves, uses", "What they asked about", "Promised next step and date", "Lead grade: A, B or C", "Staff member who met them"],
                "alt": "Checklist of lead capture fields for trade show booths at Houston events like OTC and George R. Brown shows",
                "caption": "Eight fields take about thirty seconds once staff practice them.",
            },
            "geofence": {
                "type": "compare",
                "title": "Venue geofencing: the pitch vs. the platforms",
                "left": {"title": "What gets pitched", "items": ["Ads only to people on the show floor", "Every booth visitor sees your ad", "Precise targeting of attendees", "More budget means more attendees"]},
                "right": {"title": "What Google and Meta allow", "items": ["Minimum radius about 1 km (0.6 mile)", "Circle includes roads, hotels and homes", "A reminder layer during show hours", "Small daily budget; more buys repeats"]},
                "alt": "Comparison of geofencing claims versus Google and Meta radius minimums for Houston trade show venues",
                "caption": f"Radius minimums from {SRC['grad']} and {SRC['mrad']}.",
            },
            "funnel": {
                "type": "funnel",
                "title": "From badge scans to closed deals",
                "stages": [["Badge scans", "400"], ["Qualified A and B leads", "90"], ["Meetings held after", "35"], ["Opportunities created", "14"], ["Closed within a year", "4"]],
                "note": "Illustrative example",
                "alt": "Funnel of trade show leads from badge scans to closed deals for a Houston industrial exhibitor",
                "caption": "Judge the show on the bottom three rows.",
            },
            "cpl": {
                "type": "bars",
                "title": "Cost per qualified lead by approach",
                "sub": "One show, three ways to attend",
                "items": [["10 x 20 booth, full staff", 480, "$480"], ["Hospitality suite plus outreach", 310, "$310"], ["Hotel lobby meetings only", 190, "$190"]],
                "highlight": [2],
                "note": "Illustrative example, not a benchmark",
                "alt": "Bar chart comparing cost per qualified lead for booth, hospitality suite and lobby meetings at Houston trade shows",
                "caption": "Fewer total leads, but often better ones per dollar.",
            },
        },
    },
]
