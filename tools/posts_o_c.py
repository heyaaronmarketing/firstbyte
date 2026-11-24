"""Batch 15: interior designer marketing in The Woodlands and Houston, and photographer marketing in Houston and
The Woodlands (wedding, family, newborn, headshot, real estate).

Research, designer post: Texas Occupations Code ch. 1053 (Justia mirror: sec. 1053.151 title restriction on
"registered interior designer", sec. 1053.002 exemptions, sec. 1053.003 scope, Class C misdemeanor); House
Research/committee analysis of HB 1484 (81R, 2009) narrowing the title act and dropping the "interior design" term
restriction; TBAE Registered Interior Designers page (CIDQ certificate required before applying); KBB on the 2026
U.S. Houzz & Home study (54% renovated in 2025, $20,000 median, top 10% at $150,000+, 91% hire pros, 20,000+
respondents); KBB on Best of Houzz 2026 (four categories, ~2% of 3 million+ pros); Pinterest Q3 2026 release on
SEC EDGAR (661M global MAU, 107M U.S. and Canada); PPC Land on Instagram professional-account indexing from July 10,
2025; Community Impact (July 28, 2025) on Montgomery County growth (51,000 homes across 27 developments, RCLCO 2024:
12 of top 50 MPCs in Houston metro); Google Local Services Ads category list (Interior designer: California and
Florida only); Google Business Profile service-area help (20 areas, ~2 hours' drive, remove address);
Google Maps prohibited content policy (incentives, discouraging negatives, selective solicitation).
Photographer post: Lady Bird Johnson Wildflower Center bluebonnet FAQ (end of March to mid/late April, peak early
April, picking not illegal); City of Houston Parks photography/filming request form ($154.42 per park, per date,
covers engagements and weddings); Hermann Park Conservancy photography policy (permit via City, no professional
photography in the Japanese Garden, no drones); Memorial Park Conservancy film and photography permits ($250/day,
$1,200/year, pay two weeks ahead); The Woodlands Township park rules order (no selling services without a
concessionaire contract or Special Event permit); Visit The Woodlands Film Commission FAQ (apply and the review
decides whether a permit is needed); The Knot cost guide ($3,000 average photographer spend, 2025 Real Weddings
Study, 10,474 couples); U.S. Copyright Office "What Photographers Should Know" (ownership, work made for hire,
group registration up to 750 photos); Know Before You Fly on commercial drone use (Part 107, $5 registration,
real estate listed); KBB on Best of Houzz Photography category; plus the Google, Instagram and Pinterest sources
above. Unverified and left out: Texas sales tax treatment of design fees, Google Business Profile category names
beyond common ones, Woodlands Township photo-permit fees (none published), current ASID chapter structure.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # designer post
    "oc1053": A("https://law.justia.com/codes/texas/2017/occupations-code/title-6/subtitle-b/chapter-1053/", "Chapter 1053 of the Texas Occupations Code"),
    "hb1484": A("https://capitol.texas.gov/tlodocs/81R/analysis/html/HB01484H.htm", "the committee analysis of HB 1484"),
    "tbae": A("https://www.tbae.texas.gov/rids/", "TBAE’s Registered Interior Designers page"),
    "houzz_study": A("https://kbbonline.com/business-people-news/renovation-activity-holds-steady-houzz-study-finds/168428", "KBB’s summary of the 2026 Houzz & Home study"),
    "boh": A("https://kbbonline.com/award-news/best-of-houzz-2026-powered-by-houzz-pro-winners-announced/167118/", "KBB’s Best of Houzz 2026 announcement"),
    "pins": A("https://www.sec.gov/Archives/edgar/data/0001506293/000150629326000151/q3-26xpressrelease.htm", "Pinterest’s third-quarter 2026 results"),
    "ig_index": A("https://ppc.land/instagram-content-becomes-searchable-on-google-starting-july-10/", "PPC Land"),
    "ci_mc": A("https://communityimpact.com/conroe-montgomery/real-estate/new-homes-new-hurdles-cities-work-on-infrastructure-as-single-family-homes-surge-in-montgomery-county/", "Community Impact"),
    "lsa": A("https://support.google.com/localservices/answer/6224841", "Google’s Local Services Ads category list"),
    "sab": A("https://support.google.com/business/answer/9157481", "Google’s service-area help page"),
    "gpol": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google’s prohibited content policy"),
    # photographer post
    "bluebonnet": A("https://www.wildflower.org/bluebonnet-faq", "Lady Bird Johnson Wildflower Center"),
    "hpard": A("https://cohips.houstontx.gov/parks/pdfs/PhotographyFilmingRequestForm.pdf", "City of Houston Parks photography and filming request form"),
    "hermann": A("https://hermannpark.org/?p=77", "Hermann Park Conservancy’s photography policy"),
    "mpc": A("https://www.memorialparkconservancy.org/?p=3728", "Memorial Park Conservancy"),
    "twp_rules": A("https://www.thewoodlandstownship-tx.gov/files/assets/main/v/1/parks-amp-recreation/documents/parks-amp-pathways/park-rules-amended-order-no-019-09.pdf", "The Woodlands Township’s park rules"),
    "film": A("https://assets.simpleviewinc.com/simpleview/image/upload/v1/clients/woodlands/The_Woodlands_Film_Commission_Frequently_Asked_Questions_Updated_5_16_22_0062a6db-aabf-4b4d-8091-750923654cdf.pdf", "The Woodlands Film Commission’s FAQ"),
    "knot": A("https://www.theknot.com/content/average-cost-wedding-photographer", "The Knot’s cost guide"),
    "copyright": A("https://www.copyright.gov/engage/photographers", "U.S. Copyright Office"),
    "drone": A("https://knowbeforeyoufly.org/whos-flying/commercial/", "Know Before You Fly"),
}

DESIGN = "/blog/interior-designer-marketing-the-woodlands-houston/"
PHOTO = "/blog/photographer-marketing-houston-the-woodlands/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: interior designers
    {
        "slug": "interior-designer-marketing-the-woodlands-houston",
        "title": "Interior Designer Marketing in The Woodlands and Houston: Fewer Inquiries, Better Projects",
        "seo_title": "Interior Designer Marketing in The Woodlands & Houston",
        "desc": "Interior designer marketing for The Woodlands and Houston: Texas title rules, portfolio photos, Houzz, Pinterest, Instagram, builder partners, consult fees.",
        "category": "Local marketing",
        "icons": ["Instagram", "Google Business Profile", "Google Ads"],
        "art": "b2",
        "hero": "remodel",
        "hero_alt": "Illustration of a remodeled room for interior designer marketing in The Woodlands and Houston",
        "related": ["kitchen-bath-remodeling-marketing-the-woodlands", "home-builder-marketing-houston-montgomery-county", "real-estate-agent-marketing-the-woodlands-houston"],
        "sections": [
            (None, f"""<p>Thursday afternoon, between a tile pickup in Spring and a walkthrough in Creekside Park. Three new inquiries came in today. One is a DM that says “love your work, how much for a living room?” One is a form fill from a couple who closed on a new build in The Woodlands Hills last month and want “help with everything.” The third wants you to pick paint colors for free and asked if you could stop by Saturday.</p>
<p>Only one of those is a project. You won’t know which for two weeks, and you’ll spend six hours finding out.</p>
<p>Interior designer marketing in The Woodlands and Houston has a quality problem more than a volume problem. A good portfolio on Instagram will get you messages. Getting the right ones means saying more, earlier: what you do, where you work, what a project typically costs and what the first step costs. Then you need a nurture path for the clients who take eight months to say yes.</p>
<p>This guide is for independent designers and small studios, from a one-person e-design business in Magnolia to a five-person firm near Hughes Landing. The legal part comes first, since it decides what you can print on your own website.</p>"""),

            ("“Registered interior designer” vs. “interior designer” in Texas: what you can say in your marketing", f"""<p>Texas has a title law for interior designers, and it’s narrower than a lot of people think. Under {SRC['oc1053']} (section 1053.151), a person who isn’t registered with the Texas Board of Architectural Examiners may not represent themselves as a “registered interior designer,” by using that title or words that imply it. A knowing violation is a Class C misdemeanor.</p>
<p>It used to be broader. Before 2009, only architects and registered designers could call themselves “interior designers” at all. HB 1484 changed that. Per {SRC['hb1484']}, the bill restricted only the “licensed interior designer” and “registered interior designer” titles, removed the language covering the term “interior design,” and exempted anyone who doesn’t use those titles.</p>
<p>So, in plain marketing terms:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Phrase in your ad, bio or website</th><th>Not registered with TBAE</th><th>Registered (RID)</th></tr></thead>
<tbody>
<tr><td>Interior designer</td><td>Fine</td><td>Fine</td></tr>
<tr><td>Interior decorator, stylist, home stager</td><td>Fine</td><td>Fine</td></tr>
<tr><td>Interior design services, e-design</td><td>Fine</td><td>Fine</td></tr>
<tr><td>Registered interior designer, RID</td><td>Don’t</td><td>Yes, and say it</td></tr>
<tr><td>Licensed interior designer, “state-licensed”</td><td>Don’t</td><td>Avoid “licensed”; “registered” is the Texas term</td></tr>
<tr><td>“Certified” anything</td><td>Only if you hold that specific certification, named</td><td>Same</td></tr>
</tbody></table></div>
<p>Registration has teeth beyond the title. {SRC['tbae']} says applicants need to qualify for and hold a CIDQ certificate (the NCIDQ exam route) before they apply. And the statute is clear that registration doesn’t authorize anyone to design architectural interior construction or practice architecture or engineering. That matters for how you describe space-planning and remodel work on your service pages.</p>
<p>If you are registered, that’s a real differentiator for commercial clients, medical offices and the builder design centers that care about credentials. Put “Registered Interior Designer” in your title tag and Google Business Profile description, list your registration number on the About page, and link to TBAE’s public lookup so a skeptical client can check it in ten seconds. If you aren’t registered, don’t apologize for it. Most residential clients in Sugar Land or Kingwood hire on portfolio, process and price. We’re marketers, not lawyers, so if your situation is unusual (say, you’re licensed in another state and taking Texas projects), call TBAE before you print the brochure.</p>"""),

            ("Who’s hiring a designer in The Woodlands and Houston right now", f"""<p>The 2026 Houzz & Home study, covering 2025 projects, found 54% of homeowners renovated, with a median spend of $20,000 and the top 10% of projects at $150,000 or more. Ninety-one percent of renovating homeowners hired professionals. That’s from more than 20,000 U.S. respondents, per {SRC['houzz_study']}. Your clients mostly live in that top slice, and they’re reachable.</p>
<!--fig:market-->
<p>Around here we’d split them into four groups, because each one searches and decides differently:</p>
<ul>
<li><b>New-build buyers.</b> Closing on a house in a master-planned community, with empty rooms and a deadline (usually a holiday or a family visit). Fast decisions, furnishing-heavy projects.</li>
<li><b>Relocation families.</b> Energy and medical transfers landing in The Woodlands, Memorial and Katy. They need someone local who already knows the showrooms and the installers. They find you through their agent or a Google search the week after closing.</li>
<li><b>Remodel clients.</b> A 2006 kitchen in Sterling Ridge or a dated primary bath in Cinco Ranch. Long timelines, contractor coordination, selections. Our {L('/blog/kitchen-bath-remodeling-marketing-the-woodlands/', 'kitchen and bath remodeling marketing post')} covers the contractor side of this buyer.</li>
<li><b>Second homes and lake houses.</b> Lake Conroe and Montgomery County weekend places, often furnished from scratch, often for owners who live inside the Loop.</li>
</ul>
<p>Pick one or two to build around. “We furnish new builds in The Woodlands, Spring and Conroe in eight to twelve weeks” is easier to hire than “residential and commercial design of all kinds.”</p>"""),

            ("Portfolio and photography: the asset everything else runs on", f"""<p>Every channel in this post (Instagram, Houzz, Pinterest, your website, a pitch to a builder) runs on the same thing, which is professional photos of finished rooms. Phone photos at install are useful for Stories. They don’t sell a $90,000 project.</p>
<p>Hire an architectural or interiors photographer for your best two or three projects a year, and budget it like a marketing expense rather than a project cost. Houzz even runs a separate Best of Houzz award for photography, for architecture and interior photographers whose images are most popular on the platform, per {SRC['boh']}. Look at who wins locally and you’ll find your shortlist. Our {L(PHOTO, 'photographer marketing post')} explains how those photographers think about bookings and licensing, which helps when you negotiate.</p>
<p>What to get from each shoot:</p>
<ul>
<li>Wide, medium and detail shots of every room, plus a few vertical frames for Pinterest and Reels covers.</li>
<li>Before photos you took yourself, from the same angles. Before-and-after pairs outperform finished-only images almost everywhere we’ve tested them.</li>
<li>A license that covers your website, social, award entries and print. Ask in writing whether builders or vendors can use them too.</li>
</ul>
<p>Then organize the portfolio by project type and area, with a budget band if the client agrees. “Whole-home furnishing, 3,800 sq ft, Woodforest, eleven weeks” tells a prospect more than any adjective.</p>"""),

            ("Your website and Google Business Profile in the Houston market", f"""<p>Somebody typing “interior designer The Woodlands” on a Tuesday night has already decided to hire someone. The pages a studio needs:</p>
<ul>
<li>One page per service: full-service design, new-build furnishing, remodel selections, e-design, styling or refresh. Each with process, timeline, a starting investment and three project examples.</li>
<li>Area pages for where you actually work (The Woodlands, Spring, Tomball, Montgomery, Memorial, River Oaks, Katy), each showing projects in that area. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} covers how to make these useful instead of copy-pasted.</li>
<li>An inquiry page with a real form (more on the questions below) and a clear statement of what happens next.</li>
</ul>
<p>On Google Business Profile, choose “Interior designer” as the primary category. Most independent designers work from a home office or meet clients at the job site, so per {SRC['sab']}, if you don’t serve customers at your address, you should remove it and set a service area instead. You can list up to 20 areas, and the whole thing shouldn’t extend much beyond about two hours’ drive from your base. A studio with a sign on the door and posted hours can keep its address. Upload project photos to the profile every month; it’s one of the few free places a homeowner sees your work next to your reviews.</p>
<p>One Houston-specific note. Google’s Local Services Ads do include an interior designer category, but {SRC['lsa']} shows it as available in California and Florida only. Texas designers can’t buy it yet, so regular search ads and the map pack are the game. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} goes deeper.</p>"""),

            ("Google Ads for interior designers: keywords, negatives and a realistic budget", f"""<p>Design keywords attract people who want ideas, not a designer. Filter them out from day one.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Ad group</th><th>Example keywords</th><th>Land on</th></tr></thead>
<tbody>
<tr><td>Core local</td><td>interior designer the woodlands, interior design firm houston, interior designer spring tx</td><td>Homepage or area page</td></tr>
<tr><td>New build</td><td>new home interior designer, furnish new home houston, interior designer for new construction</td><td>New-build furnishing page</td></tr>
<tr><td>Remodel</td><td>kitchen remodel designer the woodlands, bathroom design houston</td><td>Remodel selections page</td></tr>
<tr><td>Brand</td><td>your studio name, your name plus “design”</td><td>Homepage</td></tr>
</tbody></table></div>
<p>Negatives to load before launch: jobs, hiring, salary, internship, school, degree, course, certification, “how to become,” ideas, inspiration, software, app, free, cheap, DIY, Pinterest, “interior design styles,” and furniture store names you don’t sell. Set location targeting to “Presence: people in or regularly in your included locations,” and draw it around the ZIP codes where your projects actually are. A designer in The Woodlands rarely wants clicks from Baytown.</p>
<p>Budget honestly. In accounts we’ve run for high-ticket local services, $1,500 to $3,000 a month is where search starts to produce a steady trickle of qualified consults in one metro area. Check our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} before you set a number, and track form fills and calls as conversions with the setup in our {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'GA4 and Google Ads tracking guide')}. Judge the campaign on paid consultations booked, not clicks.</p>
<!--fig:budget-->"""),

            ("Houzz, Pinterest and Instagram: three visual channels doing three different jobs", f"""<p><b>Houzz</b> is where homeowners in the middle of a project go to find and vet pros. Best of Houzz 2026 recognized about 2% of the platform’s more than 3 million home building, remodeling and design professionals, across Design, Customer Service, Innovator and Photography categories, per {SRC['boh']}. Customer Service winners are chosen on overall rating and client reviews, so a Houzz profile with twelve reviews earns more than one with a beautiful cover photo and none. A free profile with complete projects and reviews is worth maintaining. A paid Houzz Pro plan is an ad buy, and we’d judge it by consults booked over a full quarter.</p>
<p><b>Pinterest</b> is a search engine people use months before they hire. Pinterest reported 661 million monthly active users globally and 107 million in the U.S. and Canada for the third quarter of 2026, per {SRC['pins']}. A pin from a 2024 project can still send traffic in 2027, which is something an Instagram post can’t do.</p>
<!--fig:pins-->
<p><b>Instagram</b> is where people decide whether they like you. Process Reels, sourcing trips to the trade showrooms, a sixty-second reveal, the ugly “before” on install day. It now does a bit of search work too: since July 10, 2025, public photos and videos from professional accounts of users over 18 can appear in Google results, per {SRC['ig_index']}. The setting is under Settings, Privacy, “Allow public photos and videos to appear in search engine results,” and it starts on. So write captions like a person searching would read them: “Whole-home refresh in Creekside Park, The Woodlands: new lighting, built-ins, white oak floors.”</p>
<p>Paid Instagram works best as retargeting for designers. Show finished projects to people who visited your website or watched most of a Reel, inside a radius around your service area. Cold Instagram ads for “hire a designer” rarely pay back at small budgets. See our {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads guide')} for the setup.</p>"""),

            ("Builder and realtor partnerships in the new master-planned communities", f"""<p>North of Houston, the new-build pipeline is enormous. {SRC['ci_mc']} counted about 51,000 homes expected across 27 developments in its Conroe and Montgomery coverage area over the next decade, in communities like Cielo, Chapel Run, The Woodlands Hills and Two Step Farm, with prices from $250,000 to $1 million. The same piece noted that RCLCO’s 2024 year-end report put 12 of the nation’s top 50 master-planned communities by sales in the Houston metro, with more than 7,500 sales.</p>
<p>Every one of those closings is a family standing in an empty house. The people who meet them first are the builder’s sales counselor, the design center and the buyer’s agent.</p>
<!--fig:partners-->
<p>How we’d approach it:</p>
<ul>
<li><b>Builders.</b> Most production builders run their own design center for selections, so don’t pitch selections. Pitch what happens after closing: furnishing packages, window treatments, lighting upgrades the design center didn’t offer. Custom and semi-custom builders around Montgomery and Magnolia are different. Many will refer a designer who keeps their schedule on track and makes their homes photograph well.</li>
<li><b>Realtors.</b> Agents selling relocation buyers in The Woodlands, Kingwood and Katy are asked “do you know a designer?” every month. Give them a one-page PDF with your new-build package, a starting price and a phone number. Offer vacant-home staging advice before listing photos. Ask their broker before offering anything of value for referrals; agents have their own rules on that.</li>
</ul>
<p>Keep a partner sheet: who referred, what project, what it closed for. After a year you’ll know which three relationships matter.</p>"""),

            ("Design consultation fees and project minimums: say them out loud", f"""<p>Back to the person who wanted free paint colors on Saturday. The fastest way to stop spending your weekends on unpaid consults is to publish what the first meeting costs and what projects usually start at.</p>
<p>A number on the website will scare some people off. Mostly the ones who would have taken two hours of your time and then bought the sofa at a big-box store.</p>
<!--fig:consult-->
<p>What we’d put on the site:</p>
<ul>
<li>“Initial design consultation: [your price], credited toward your design fee if we work together.” A credit makes a paid consult feel like a deposit instead of a toll.</li>
<li>“Full-service projects typically start at [your price] in design fees, plus furnishings.” Or a range by project type.</li>
<li>How you bill (flat fee, hourly, or a fee plus product markup) in one honest sentence. Clients are less bothered by markup than by finding out about it late.</li>
<li>What the consult includes: walkthrough, a short written summary, a rough budget range. Something they keep.</li>
</ul>
<p>Minimums do the same filtering. If you don’t take single-room projects under [your price], say so on the inquiry page. Point smaller clients to an e-design package instead; some call back later for the whole house.</p>"""),

            ("High-ticket nurture: the inquiry form and the eight-month client", f"""<p>A $60,000 furnishing project rarely closes in a week. Lots of clients are waiting on a closing date, a bonus, a remodel bid or a spouse. Your marketing has to stay useful the whole time.</p>
<p>Start with the inquiry form. Ask for project type, address or neighborhood, timeline, approximate budget range (as ranges, never a blank box), whether the home is new construction and the closing date if so, and how they found you. Five or six questions is plenty. More than that and good clients bail.</p>
<!--fig:nurture-->
<p>Then the follow-up:</p>
<ol>
<li>Reply the same business day, ideally within the hour, with a link to book the consult. Designers lose more projects to slow replies than to price. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead post')} explains why.</li>
<li>If they don’t book, send one short email a week for three weeks: a relevant project, your process, a client review.</li>
<li>Then move them to a monthly email with one finished project and one useful note, like ordering lead times for custom upholstery before the holidays.</li>
<li>Tag the closing date for new-build clients and reach out three weeks before it. Timing beats persistence.</li>
</ol>
<p>Track inquiries, consults, proposals and signed projects in a spreadsheet or CRM. Your consult-to-signed rate tells you what a lead is worth.</p>"""),

            ("Reviews that sell the next project", f"""<p>Designers get fewer reviews than a restaurant, so each one carries more weight.</p>
<p>Google’s rules are simple: merchants may not offer incentives such as discounts or free services for reviews, may not discourage negative reviews and may not “selectively solicit positive reviews,” per {SRC['gpol']}. Ask every client, the same way.</p>
<p>Timing that works for designers: mention it at the reveal while they’re walking through, then send the link about two weeks later once they’ve lived with the rooms and had people over. A script you can copy:</p>
<p><i>“It was a joy working on your house. If you have two minutes, a Google review helps other families in The Woodlands find us. Here’s the link: [link]. Mentioning the kind of project helps people most.”</i></p>
<p>Ask for a Houzz review too, a month later, since Houzz recognition leans on reviews. Reply to every review with something specific about the project. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates.</p>"""),

            ("A first 90 days for a Houston interior design studio", f"""<p>If you’re starting from a pretty Instagram and not much else, this order works:</p>
<ul>
<li><b>Month one.</b> Fix the title language on your site and profiles. Publish your consult fee and starting investment. Build service and area pages. Set up Google Business Profile properly and upload your best twenty project photos. Add the inquiry form with real questions.</li>
<li><b>Month two.</b> Book a professional shoot of your best recent project. Pin every image to keyword-named Pinterest boards. Write one partner one-pager and hand it to five agents and two custom builders. Start the review ask with every finished client.</li>
<li><b>Month three.</b> Launch a small Google Ads search campaign on your core local and new-build keywords, plus Instagram retargeting. Start the monthly email. Review the inquiry-to-signed numbers and cut whatever produced no consults.</li>
</ul>
<p>None of this is glamorous, and it compounds. If you want a senior strategist to build that plan around your studio, <a href="/contact/">get in touch</a>. Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} and {L('/services/search-marketing/', 'search marketing team')} handle the build and the ads.</p>"""),
        ],
        "faq": [
            ("Can I call myself an interior designer in Texas without being registered?",
             "Yes. Since HB 1484 took effect in 2009, Texas restricts only the titles registered interior designer and licensed interior designer, plus words that imply registration. You can call yourself an interior designer, decorator or stylist without registering with the Texas Board of Architectural Examiners. Using the registered title without registration is a Class C misdemeanor, so leave registered and licensed out of your bio unless you hold TBAE registration."),
            ("How do interior designers in The Woodlands and Houston get clients?",
             "Most projects come from referrals, Google searches like interior designer The Woodlands, Instagram, Houzz and Pinterest. The designers who grow fastest pair a strong professional portfolio with clear pricing on their website, a properly set up Google Business Profile, steady Google and Houzz reviews, and referral relationships with realtors and custom builders in new master-planned communities around Conroe, Spring and Montgomery."),
            ("Should an interior designer charge for the first consultation?",
             "In our view, yes, for most established designers. A published consultation fee filters out people looking for free advice and signals that your time has value. Crediting the fee toward your design fee if the client signs makes it feel like a deposit. Make the consult worth paying for with a walkthrough, a written summary and a rough budget range the client keeps."),
            ("Are Google Local Services Ads available for interior designers in Texas?",
             "Not currently. Google lists an interior designer category for Local Services Ads, but only in California and Florida. Designers in Houston and The Woodlands should rely on regular Google search ads, a strong Google Business Profile and reviews to show up for searches like interior designer near me. Check Google’s category list from time to time, since it does expand."),
            ("Is Houzz worth it for interior designers in Houston?",
             "A free, complete Houzz profile with project photos and reviews is worth keeping, because homeowners use it to vet pros and Best of Houzz service awards lean on reviews. A paid Houzz Pro plan is an advertising decision. Run it for a full quarter and judge it by paid consultations and signed projects, not by profile views or message counts, before you renew."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "Who’s renovating, and how much",
                "stats": [["54%", "of homeowners renovated in 2025"], ["$20K", "median renovation spend"], ["$150K+", "top 10% of projects"], ["91%", "hire professionals"]],
                "note": "Source: 2026 U.S. Houzz & Home study",
                "alt": "Stats from the Houzz and Home study on renovation spending relevant to interior designer marketing in Houston and The Woodlands",
                "caption": f"From {SRC['houzz_study']}. Your clients tend to live in the top slice.",
            },
            "budget": {
                "type": "bars",
                "title": "Example monthly mix for a small studio",
                "sub": "Single metro, design firm doing $500K to $1M a year",
                "items": [["Google Ads search", 2000, "$2,000"], ["Instagram retargeting", 500, "$500"], ["Photography (spread monthly)", 400, "$400"], ["Email and CRM tools", 100, "$100"], ["Partner lunches and one-pagers", 150, "$150"]],
                "highlight": [0],
                "note": "Illustrative example",
                "alt": "Bar chart of an example monthly marketing budget for an interior designer in The Woodlands and Houston",
                "caption": "Not a quote. Your mix should follow what your tracked consults show.",
            },
            "pins": {
                "type": "checklist",
                "title": "Pinterest setup for a design studio",
                "sub": "An afternoon of work that keeps sending traffic",
                "items": ["Business account, website claimed", "Boards named like searches: “Modern farmhouse kitchen Houston”", "Every portfolio image pinned, linked to its project page", "Vertical images (2:3) for most pins", "Keyword-rich pin titles and descriptions", "Location in the description: The Woodlands, Memorial", "Pin new projects weekly for a month, then monthly", "Check Pinterest Analytics for outbound clicks"],
                "alt": "Checklist for setting up Pinterest for an interior designer in The Woodlands and Houston",
                "caption": "Pinterest rewards consistency more than volume.",
            },
            "partners": {
                "type": "steps",
                "title": "Turning new-build closings into projects",
                "sub": "Partner path in Montgomery County master-planned communities",
                "steps": [["List partners", "Ten agents and five custom builders who sell where you work."], ["Make a one-pager", "New-build furnishing package, starting price, timeline, phone."], ["Show up", "Broker opens, model events, a lunch near Hughes Landing."], ["Deliver fast", "Reply to every referral the same day, report back to the partner."], ["Track it", "Referrer, project, value. Keep the three that matter."]],
                "alt": "Steps for interior designers to build builder and realtor referral partnerships in The Woodlands, Conroe and Houston",
                "caption": "Referral partners judge you on how their clients are treated.",
            },
            "consult": {
                "type": "compare",
                "title": "The free consult vs. the paid consult",
                "left": {"title": "Free, unpriced", "items": ["Saturdays full of maybe-clients", "Advice given away on the walkthrough", "Budget shock at the proposal", "Hard to tell buyers from browsers", "Lower close rate, more hours"]},
                "right": {"title": "Paid, credited, published", "items": ["Fewer, better-qualified meetings", "Client gets a written summary", "Starting investment known up front", "Fee credited if they sign", "Higher close rate, fewer hours"]},
                "alt": "Comparison of free and paid design consultations for interior designers in Houston and The Woodlands",
                "caption": "Our experience across high-ticket service clients. Your numbers will tell you more.",
            },
            "nurture": {
                "type": "funnel",
                "title": "Where a design project comes from",
                "stages": [["Inquiries", "40"], ["Qualified (fit, area, budget)", "18"], ["Paid consults", "9"], ["Proposals sent", "6"], ["Signed projects", "3"]],
                "note": "Illustrative example, one quarter",
                "alt": "Funnel of interior design inquiries to signed projects for a small studio in The Woodlands and Houston",
                "caption": "Count every stage for a quarter and you’ll know what a lead is worth.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: photographers
    {
        "slug": "photographer-marketing-houston-the-woodlands",
        "title": "Photographer Marketing in Houston and The Woodlands: Bookings Beyond Bluebonnet Season",
        "seo_title": "Photographer Marketing in Houston & The Woodlands",
        "desc": "Photographer marketing for Houston and The Woodlands: Google Business Profile, Instagram and Pinterest SEO, mini sessions, park permits, pricing, reviews.",
        "category": "Local marketing",
        "icons": ["Instagram", "Google Business Profile", "Meta"],
        "art": "b4",
        "hero": "wedding",
        "hero_alt": "Illustration for photographer marketing in Houston and The Woodlands, covering wedding, family and portrait sessions",
        "related": ["wedding-venue-marketing-houston-montgomery-county", "complete-guide-google-reviews", "rank-in-google-map-pack-houston"],
        "sections": [
            (None, f"""<p>Second Saturday of October, 7:05 a.m., a park bench in The Woodlands. You have six fall mini sessions back to back, twenty minutes each, and the light is good until about 9:15. By the third family your phone has four DMs asking if you have “anything left in November,” and a realtor in Spring has texted about a listing shoot for Tuesday.</p>
<p>Then January arrives, and the calendar looks like a parking lot at 2 a.m.</p>
<p>That swing is the core problem in photographer marketing in Houston. Demand piles into a few weeks (bluebonnets, fall, holidays, wedding season) and leaves long, quiet stretches between. The photographers who do well here spend less energy on October, which sells itself, and more on steady lines of work that don’t care about the season, like headshots, real estate and newborns. And they make it easy to book and pay without three days of back-and-forth messages.</p>
<p>This guide covers wedding, family and portrait, newborn, headshot and real estate photographers working around Houston, The Woodlands, Spring, Cypress, Katy and Conroe.</p>"""),

            ("Five businesses under one camera", f"""<p>Most photographers market as “a photographer.” Clients don’t search that way. A bride, a new mom and a listing agent want different things, on different timelines, and type different words into Google.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Work</th><th>What clients search</th><th>How far ahead they book</th><th>Where they find you</th><th>What they buy</th></tr></thead>
<tbody>
<tr><td>Weddings</td><td>wedding photographer houston, the woodlands wedding photographer</td><td>Often a year or more</td><td>Instagram, venue and planner referrals, Google, The Knot</td><td>Collections, engagement session</td></tr>
<tr><td>Family and portrait</td><td>family photographer the woodlands, fall mini sessions spring tx</td><td>Weeks</td><td>Instagram, Facebook groups, past clients, Google</td><td>Sessions, minis, prints</td></tr>
<tr><td>Newborn and maternity</td><td>newborn photographer houston, maternity photos katy</td><td>Booked during pregnancy</td><td>Google, referrals, OB and pediatric offices</td><td>Packages, often bundled</td></tr>
<tr><td>Headshots</td><td>headshot photographer the woodlands, corporate headshots houston</td><td>Days to two weeks</td><td>Google, LinkedIn, HR and office managers</td><td>Per person, team days</td></tr>
<tr><td>Real estate</td><td>real estate photographer houston, drone listing photos conroe</td><td>Next day to a week</td><td>Agent referrals, brokerages, Google</td><td>Per listing, monthly volume</td></tr>
</tbody></table></div>
<p>You don’t have to do all five. But each one you do needs its own page, its own keywords and its own pitch. The family photographer who adds headshots on weekday mornings has a January. The wedding photographer who never mentions engagement sessions on Google is leaving the cheapest bookings on the table.</p>"""),

            ("The Houston photography calendar: bluebonnets, fall families and holiday minis", f"""<p>Houston has a photography season shaped by heat. Nobody wants family photos in a field at 6 p.m. in August with a heat index over 105, and you don’t either.</p>
<p><b>Bluebonnets.</b> Per the {SRC['bluebonnet']}, bluebonnets in Central and East Texas typically start blooming toward the end of March and run through mid- to late April, with the peak in early April. A cool spring slows them down and a warm one speeds them up. So announce bluebonnet minis in February with “dates confirmed once the fields bloom,” not a fixed date in January. And for the record, the Wildflower Center says picking them isn’t illegal, though it asks people to leave them. The real hazards are private property, fire ants and roadside shoulders. Your booking page should say where you’ll shoot and that it’s legal to be there.</p>
<p><b>Fall family photos.</b> October and November, once the evenings stop feeling like a sauna. This is the busiest stretch for most family photographers in The Woodlands and Cypress, and the minis sell out to people who planned ahead.</p>
<p><b>Holiday minis.</b> Mid-November into early December, often on a styled set or a studio backdrop so the weather doesn’t matter. Card-printing deadlines drive urgency for you.</p>
<!--fig:calendar-->
<p><b>Spring and fall weddings.</b> Houston couples tend to avoid July and August outdoors, so spring and fall weekends fill first. Graduation and senior portraits pile into March through May. Newborns are the one category that ignores the calendar, which is exactly why they’re worth marketing in summer. Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing guide')} covers how other businesses plan around the same weather.</p>"""),

            ("Location permits in Houston and The Woodlands parks", f"""<p>This is the part a lot of photographers skip, until a ranger walks over mid-session.</p>
<p><b>City of Houston parks.</b> The {SRC['hpard']} covers professional filming or photography at any City of Houston park, and explicitly lists engagements, weddings, graduations and quinceañeras. The current form lists a fee of $154.42 per park, per date, booked through the city’s ActiveNet system.</p>
<p><b>Hermann Park.</b> Per {SRC['hermann']}, any commercial use of city property needs a permit, professional photographers must get one from the City, professional photography isn’t permitted in the Japanese Garden, and drones are banned in the park.</p>
<p><b>Memorial Park.</b> {SRC['mpc']} requires a permit for any commercial or professional photo shoot. Commercial film and photography runs $250 a day, or $1,200 for an annual photography permit, and the fee has to be paid at least two weeks before the shoot.</p>
<p><b>The Woodlands.</b> The Township’s rules are less specific about portraits. {SRC['twp_rules']} prohibit selling services in parks unless you’re a licensed concessionaire or contractor or have a Special Event permit, and they don’t address photo sessions directly. {SRC['film']} says to submit an application and the review will determine whether a permit is needed for each location. Our advice: call before you sell minis at a Township park, and get the answer in writing. Shopping areas like Market Street and Hughes Landing are private property with their own management, so ask them separately.</p>
<!--fig:permits-->
<p>Here’s the marketing angle. Permits are a cost and a selling point. Build the permit fee into session pricing, and say on your booking page “all locations permitted.” Then write location guide pages (“Best family photo spots in The Woodlands,” “Engagement photo locations in Houston”) with the permit rules for each. Couples and parents search those phrases constantly, and a page that answers the permit question honestly ranks and earns trust at the same time.</p>"""),

            ("Google Business Profile for photographers", f"""<p>When someone searches “newborn photographer near me” in Katy, the map pack is the first thing they see. Your profile needs to be there.</p>
<ul>
<li><b>Address or service area.</b> If you shoot on location and don’t meet clients at your home, {SRC['sab']} says to remove the address and set a service area: up to 20 cities or ZIP codes, not much beyond about two hours’ drive. A studio with signage and set hours can show its address and a service area together.</li>
<li><b>Primary category.</b> Choose the most specific category that matches the work you want most. A wedding-first business should lead with wedding photographer. A studio doing mostly newborns and families might lead with portrait studio. Add secondary categories only for work you actually do.</li>
<li><b>Services and photos.</b> List each session type with a starting price. Upload new work weekly in peak season, with real locations people recognize.</li>
<li><b>Booking link.</b> Point the appointment link at a page where they can see availability or request a date.</li>
</ul>
<p>Reviews are the biggest ranking and conversion factor you control. More on that below. The full map playbook is in our {L('/blog/rank-in-google-map-pack-houston/', 'Houston map pack guide')}.</p>"""),

            ("Pricing pages that book sessions", f"""<p>The “Investment” page with no numbers and a contact form is a photography-industry tradition. In our experience it mostly produces inquiries from people who leave the moment they see the PDF.</p>
<p>Clear starting prices won’t make you look cheap. They save you from writing forty quotes a month to people who were never going to book.</p>
<!--fig:pricing-->
<p>A pricing page that works shows, for each session type: a starting price (“Family sessions from [your price]”), what’s included (time, locations, number of edited images, delivery time), what costs extra (permits, travel past Conroe, prints, rush delivery), and one clear button. For weddings, show your lowest collection and say most couples spend between two figures. For context, The Knot’s 2025 Real Weddings Study put the average spend on a wedding photographer at $3,000 across 10,474 U.S. couples, per {SRC['knot']}. Your price may be well above or below that. Couples will compare you against it anyway.</p>
<p>Our {L('/services/web-design-seo-pr/', 'web design team')} builds these pages so they load fast on a phone, which matters when most of your traffic comes from Instagram’s in-app browser.</p>"""),

            ("Instagram and Pinterest SEO for Houston photographers", f"""<p>Instagram is your portfolio, but it’s also become searchable outside the app. Since July 10, 2025, public photos, videos, carousels and Reels from professional accounts of users over 18 can show up in Google search, per {SRC['ig_index']}. Check Settings, Privacy and make sure “Allow public photos and videos to appear in search engine results” is on.</p>
<p>That changes how you caption. “Golden hour with the Garcias!” tells a search engine nothing. “Fall family session at a Woodlands park, sunrise, matching neutrals for a family of five” matches what parents search. Put your niche and city in your profile name field (“Ana | Houston Newborn Photographer”), add alt text to posts under advanced settings, and tag the location.</p>
<p>Pinterest is slower and lasts longer. It reported 661 million monthly active users globally and 107 million in the U.S. and Canada in the third quarter of 2026, per {SRC['pins']}. Brides plan on it. So do moms picking outfits for fall photos. Make boards that match searches (“Houston engagement photo ideas,” “What to wear for family photos in Texas,” “Bluebonnet photo ideas”), pin every gallery’s best vertical frames, and link each pin to the matching page on your site. A pin from April can still be sending traffic the next March, right before bluebonnet season.</p>
<!--fig:reach-->"""),

            ("Mini-session marketing that sells out without discounting", f"""<p>Minis are the best marketing tool most portrait photographers have. They bring in new families at a lower price, fill a weekend, and turn into full sessions and newborn bookings later.</p>
<p>They also burn people out when they’re marketed as a scramble. The structure that works:</p>
<!--fig:minis-->
<ol>
<li><b>Lock the location and permit first.</b> Then pick the dates. Nothing kills trust like moving forty families to a new park.</li>
<li><b>Tell past clients first.</b> Email and text your list 48 hours before you post publicly. Only text people who opted in for marketing messages; our {L('/blog/sms-marketing-small-business-texas-rules/', 'Texas SMS rules post')} covers consent.</li>
<li><b>Then Instagram and Facebook.</b> Post the dates, what’s included, the price and the booking link. Stories with a countdown work. So does a Reel from last year’s minis.</li>
<li><b>Small paid push.</b> A Meta ad to a radius around the location, aimed at the booking page. In accounts we’ve run for local service businesses, a few hundred dollars over ten days is enough to tell whether paid helps fill the last slots. Our {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads guide')} has the setup.</li>
<li><b>Pay to book.</b> Full payment or a meaningful retainer at booking, with a written reschedule policy for weather. Houston thunderstorms are not hypothetical.</li>
</ol>
<p>Then follow up. Every mini family gets an offer for a full session or a holiday add-on within a week of gallery delivery.</p>"""),

            ("Booking and deposit flows that don’t leak inquiries", f"""<p>The average photographer inquiry goes like this: Instagram DM, “what are your prices,” you reply three hours later with a PDF, they say “thanks!” and disappear. The client didn’t hate your work. You gave them a document and homework.</p>
<p>A cleaner flow:</p>
<!--fig:booking-->
<ul>
<li>Inquiry form on your site asks for session type, date or season, location area and how they found you. Keep it short.</li>
<li>An automatic reply goes out within minutes with starting prices and a booking or call link.</li>
<li>A real reply from you within a few hours on weekdays. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead post')} explains why the first hour matters.</li>
<li>Contract and retainer online in one step, so “yes” turns into a booking the same evening.</li>
<li>A questionnaire and reminder sequence before the session: what to wear, parking, the permit, weather plan.</li>
</ul>
<p>Put the retainer terms in the contract in plain words and have a lawyer look at it once. Use a client management tool that handles contracts, payments and reminders together. And track where each booked client came from. After one season you’ll know whether Instagram, Google or your venue friends are paying the bills.</p>"""),

            ("Wedding vendor referrals in Houston", f"""<p>Wedding photographers live and die by referrals from venues, planners, florists and DJs. We cover how the venue side markets itself in our {L('/blog/wedding-venue-marketing-houston-montgomery-county/', 'wedding venue marketing guide')}, so here’s just the photographer’s half of the relationship.</p>
<ul>
<li><b>Send galleries to the venue.</b> Within two weeks of a wedding, send the venue coordinator a web-sized set of images of their space, with permission to use and credit. That’s how photographers get onto preferred vendor lists.</li>
<li><b>Credit every vendor</b> on Instagram and in blog posts. Planners notice who tags them.</li>
<li><b>Styled shoots</b> only if they produce images a venue or planner will actually use. Otherwise they’re an expensive Saturday.</li>
<li><b>Show up at the venues you want.</b> An open house at a Montgomery County barn venue or a downtown Houston hotel is where planners meet photographers who aren’t on their list yet.</li>
</ul>
<p>Keep a referral log. Most photographers find that two or three planners and a handful of venues produce most of their weddings.</p>"""),

            ("Headshots and real estate: the work that fills Tuesdays", f"""<p>These two lines keep the lights on between peak seasons, and they’re marketed to businesses, not families.</p>
<p><b>Headshots.</b> The offices along Research Forest, Woodloch Forest and in the Energy Corridor hire new people every month. Build a page for individual headshots and one for team days on site. Run a small Google Ads campaign on “headshot photographer the woodlands” and “corporate headshots houston,” with negatives like free, app, AI, DIY, booth, school pictures and jobs. Email office managers and HR leads a one-page offer with per-person pricing. A team day for twenty people can beat a mini-session weekend on revenue.</p>
<p><b>Real estate.</b> Agents in The Woodlands, Spring and Conroe need photos fast and consistently. Your marketing is mostly turnaround time, consistency, and being easy to book. If you fly a drone for listings, that’s commercial use. {SRC['drone']} lists real estate aerial photography as an example and says commercial operators need an FAA Remote Pilot Certificate under Part 107 and must register the drone ($5, good for three years). Put “FAA Part 107 certified” on your real estate page; agents and brokerages ask.</p>
<p>Spell out licensing too. Per the {SRC['copyright']}, the photographer is generally the author and initial owner of a photo unless it’s a work made for hire, and it offers group registration of up to 750 photos per application. Your agreement should say the agent and listing brokerage may use the images to market that listing, and say what happens when a builder or a later agent wants them. Clear terms prevent the awkward phone call after you find your photos on someone else’s listing. Interior and architectural shooters also pick up work from design studios; our {L(DESIGN, 'interior designer marketing post')} explains what designers want from a shoot.</p>"""),

            ("Reviews: ask at gallery delivery", f"""<p>The moment a client opens their gallery is the high point. That’s when to ask.</p>
<p>Google’s rules: no incentives (no “free print for a review”), no discouraging negative reviews, and no asking only the happy clients, per {SRC['gpol']}. Same ask, every client.</p>
<p>A script you can send with the gallery link:</p>
<p><i>“Your gallery is ready, and I loved this one. If you have a minute, a Google review helps other Houston families find me: [link]. Mentioning the type of session and the location helps people most.”</i></p>
<p>Wedding clients can get a second ask on The Knot or WeddingWire a few weeks later. Reply to every review with a detail from the session. Our {L('/blog/complete-guide-google-reviews/', 'complete guide to Google reviews')} has more templates, and our {L('/blog/fake-reviews-rule-local-businesses/', 'post on the FTC fake reviews rule')} covers what not to do.</p>"""),

            ("A first 90 days for a Houston or Woodlands photographer", f"""<p>If you’re booked in October and anxious in January, this order works:</p>
<ul>
<li><b>Month one.</b> Build one page per session type with starting prices. Fix your Google Business Profile category, service area and photos. Turn on Instagram search indexing and rewrite your profile name. Start the review ask on every gallery.</li>
<li><b>Month two.</b> Write three location guide pages with permit notes. Set up Pinterest boards and pin your best twenty galleries. Send a headshot or real estate one-pager to twenty local offices or agents.</li>
<li><b>Month three.</b> Plan the next mini season with permits in hand. Launch a small Google Ads campaign on your steadiest niche. Review bookings by source and cut what didn’t produce a single paid session.</li>
</ul>
<p>Do that and the next quiet stretch gets shorter. If you’d like a senior strategist to build a plan around your niche and calendar, <a href="/contact/">get in touch</a>. Our {L('/services/paid-social-advertising/', 'paid social team')} runs the Instagram and Facebook side.</p>"""),
        ],
        "faq": [
            ("Do I need a permit to photograph clients in Houston parks?",
             "Usually, yes. The City of Houston’s photography and filming request form covers professional sessions at any city park, including engagements and weddings, with a fee of $154.42 per park per date on the current form. Hermann Park requires a city permit and bans professional photography in the Japanese Garden. Memorial Park charges $250 a day or $1,200 a year for photography permits, paid two weeks ahead."),
            ("Can photographers do sessions in The Woodlands Township parks?",
             "Check first. The Woodlands Township’s park rules prohibit selling services in parks without a concessionaire contract or a Special Event permit, and they don’t address photo sessions directly. The Woodlands Film Commission says to submit an application and its review will decide whether a permit is needed. Call before you sell mini sessions at a Township park, and get the answer in writing."),
            ("When is bluebonnet season for photos near Houston?",
             "According to the Lady Bird Johnson Wildflower Center, bluebonnets in Central and East Texas usually start blooming toward the end of March and run through mid- to late April, peaking in early April. Timing shifts with the weather each year. Announce bluebonnet minis in February with dates confirmed once fields bloom, and shoot only where you have permission to be."),
            ("How do photographers in The Woodlands and Houston get more clients?",
             "The steadiest photographers combine a complete Google Business Profile with steady reviews, a pricing page with real starting prices, Instagram captions and Pinterest boards written around what clients search, and referral relationships with venues, planners and realtors. Mini sessions bring in new families, and headshots and real estate work fill the slow months between bluebonnet season and fall family photos."),
            ("Should photographers show prices on their website?",
             "We think so. Starting prices for each session type filter out people who were never going to book and make the inquiries you get more likely to convert. Show what’s included, what costs extra and a clear booking button. For weddings, show your lowest collection and a typical range. The Knot’s 2025 data put average wedding photographer spending at $3,000, and couples will compare you to it."),
        ],
        "figures": {
            "calendar": {
                "type": "columns",
                "title": "Houston portrait demand by month",
                "sub": "Relative inquiry volume for a family and portrait photographer",
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "values": [20, 30, 60, 85, 55, 30, 20, 25, 55, 100, 90, 45],
                "highlight": [3, 9, 10],
                "y_label": "Relative demand",
                "note": "Illustrative example: bluebonnets, fall families and holiday minis drive the peaks",
                "alt": "Column chart of photography demand by month in Houston and The Woodlands, peaking in April, October and November",
                "caption": "Shape based on our experience with seasonal local businesses, not survey data. Your bookings will tell you your own curve.",
            },
            "permits": {
                "type": "checklist",
                "title": "Before you announce a location",
                "sub": "Permit checks for Houston-area sessions",
                "items": ["City of Houston park: request form, $154.42 per park, per date", "Hermann Park: city permit, no pro shoots in the Japanese Garden", "Memorial Park: $250/day or $1,200/year, pay two weeks ahead", "Woodlands Township park: call first, get it in writing", "Market Street, Hughes Landing: ask property management", "No drones in Hermann Park or Memorial Park", "Private fields: written landowner permission", "Build the fee into your session price"],
                "alt": "Checklist of photography permit rules for parks in Houston and The Woodlands",
                "caption": f"From the {SRC['hpard']}, {SRC['hermann']} and {SRC['mpc']}. Fees change, so confirm before you book.",
            },
            "pricing": {
                "type": "compare",
                "title": "Pricing page: hidden vs. clear",
                "left": {"title": "“Contact for investment”", "items": ["Every visitor has to ask", "Dozens of quotes a month", "Price shock after the PDF", "Ghosting after you reply", "Hard to tell what’s included"]},
                "right": {"title": "Starting prices, shown", "items": ["Visitors self-qualify", "Fewer, warmer inquiries", "No surprise at the contract", "Book or call button right there", "Inclusions and extras spelled out"]},
                "alt": "Comparison of hidden and clear pricing pages for photographers in Houston and The Woodlands",
                "caption": "You’ll lose a few browsers and gain a lot of bookings, in our experience.",
            },
            "reach": {
                "type": "stats",
                "title": "Why visual search is worth the work",
                "stats": [["661M", "Pinterest monthly users, Q3 2026"], ["107M", "Pinterest users, U.S. and Canada"], ["$3,000", "average wedding photographer spend, 2025"], ["2025", "Instagram posts began showing in Google"]],
                "note": "Sources: Pinterest Q3 2026 results, The Knot, PPC Land",
                "alt": "Stats on Pinterest users, Instagram search indexing and wedding photography spending for Houston photographers",
                "caption": f"From {SRC['pins']}, {SRC['knot']} and {SRC['ig_index']}.",
            },
            "minis": {
                "type": "steps",
                "title": "Mini-session launch sequence",
                "sub": "A fall or holiday mini season for The Woodlands or Houston",
                "steps": [["Permit and place", "Confirm the location and permit before picking dates."], ["Past clients first", "Email and opted-in texts 48 hours before public posts."], ["Post publicly", "Dates, price, inclusions and booking link on Instagram and Facebook."], ["Small ad push", "Meta ad to a radius around the location for the last slots."], ["Pay to book", "Payment at booking, written weather reschedule policy."], ["Follow up", "Full-session or holiday offer within a week of delivery."]],
                "alt": "Six steps to market a mini session for photographers in Houston and The Woodlands",
                "caption": "The follow-up step is where minis turn into a year of bookings.",
            },
            "booking": {
                "type": "funnel",
                "title": "Inquiry to booked session",
                "stages": [["Inquiries", "60"], ["Got pricing and replied", "36"], ["Call or consult", "20"], ["Contract and retainer", "12"], ["Session shot", "11"]],
                "note": "Illustrative example, one month",
                "alt": "Funnel of photography inquiries to booked sessions for a photographer in Houston and The Woodlands",
                "caption": "The biggest drop is usually between the inquiry and the first reply. Speed fixes most of it.",
            },
        },
    },
]
