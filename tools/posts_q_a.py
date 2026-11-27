"""Batch 17 (module a): three local-rules / local-SEO posts for The Woodlands and Houston business owners.

1. Business sign rules in The Woodlands vs. Houston (rules guide). Research: The Woodlands Township Commercial
   Planning and Design Standards (recorded Aug 2026, Article VI sign standards: 6.3 general rules, 6.4 pre-approved
   A-frames and menu boards, 6.5 signs requiring approval, 6.6.M window and door signs, 6.7 temporary signs incl.
   opening banners, for-lease, now-hiring); Township Commercial Standards and Covenant Administration pages (DSC make-up,
   Civic Access Portal, "does not enforce ordinances"); Community Impact on the Oct 2026 covenant standards review;
   City of Houston Sign Administration page, on-premise sign permit page (5 signs, fees, 4-11 business days), Limited
   Use Banner application (7 consecutive days in any 30, 40 sq ft, flush mount), Sign Administration FAQ CE-1422 (banner
   rules, portable and bandit signs prohibited), Houston Code Ch. 28 secs. 28-37 to 28-39 ($300-$500 per violation,
   impoundment), Houston bandit sign committee presentation; Texas Transportation Code ch. 393 (393.002, 393.003,
   393.007 civil penalty $500-$1,000 per violation, per day); TxDOT ROW manual on illegal signs; Harris County Engineer
   sign permits for unincorporated areas.
2. The Woodlands vs. Spring vs. Conroe addresses for local SEO (explainer). Research: USPS "ZIP Code: The Basics" FAQ;
   USPS ZIP lookup; ZIP databases built from USPS city-state data (zipcodes-us.com, zip-codes.com) for primary and
   acceptable city names of 77380-77389, 77393 and 77354; HAR on Village of Sterling Ridge in 77354; ABC13 and the
   Township's incorporation page (special-purpose district, counties handle roads and police); Community Impact on
   Shenandoah; Google Business Profile guidelines, service area help, local ranking help; Google LocalBusiness
   structured data docs; Google spam policies (doorway abuse, city-list keyword stuffing).
3. Local SEO myths (myth-buster). Research: Google Business Profile guidelines (name rules), local ranking help
   (relevance, distance, prominence; "no way to request or pay"), posts help (archived after 6 months), service area help
   (20 areas, ~2 hours), Google Ads help ("search results are independent of Google's advertising programs"), SEO
   Starter Guide (hours to months, no meta keywords, domain keywords, word count, duplicate content), spam policies,
   reviews help and Maps contribution policy, Search Engine Land on suspension causes.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # sign rules post
    "cpds": A("https://www.thewoodlandstownship-tx.gov/files/sharedassets/main/v/2/covenant-administration/documents/commercial-planning-and-design-standards-aug-2026-recorded.pdf", "The Woodlands Commercial Planning and Design Standards"),
    "tw_comm": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration/Commercial-Standards", "the Township’s Commercial Standards page"),
    "tw_cad": A("https://www.thewoodlandstownship-tx.gov/Departments/Covenant-Administration", "the Township’s Covenant Administration page"),
    "ci_cov": A("https://communityimpact.com/the-woodlands/government/the-woodlands-township-board-reviews-changes-to-covenant-standards/", "Community Impact"),
    "hou_sign": A("https://www.houstonpermittingcenter.org/building-code-enforcement/sign-administration", "Houston Sign Administration"),
    "hou_onprem": A("https://houstonpermittingcenter.org/hpwcode1112", "Houston’s on-premise sign permit page"),
    "hou_lub": A("https://www.houstonpermittingcenter.org/media/5611/download", "Limited Use Banner application"),
    "hou_faq": A("https://www.houstonpermittingcenter.org/media/10866/download", "Sign Administration FAQ"),
    "hou_ch28": A("https://311.houstontx.gov/neighborhoods/banditsigns/sign-code.pdf", "Chapter 28 of the Houston Code"),
    "hou_bandit": A("https://pwehelp.houstontx.gov/council/committees/rna/20210209/Bandit-Signs.pdf", "a City of Houston committee presentation on bandit signs"),
    "tx393": A("https://311.houstontx.gov/neighborhoods/banditsigns/texas-transportation-code.pdf", "Chapter 393 of the Texas Transportation Code"),
    "tx393007": A("https://texas.public.law/statutes/tex._transp._code_section_393.007", "Section 393.007"),
    "txdot": A("https://onlinemanuals.txdot.gov/TxDOTOnlineManuals/TxDOTManuals/use/illegal_signs_on_the_right_of_way.htm", "TxDOT’s right-of-way manual"),
    "hc_oce": A("https://oce.harriscountytx.gov/Services/Permits/Permits-A-to-Z/Signs-Extra-Territorial-Jurisdiction-Scenic-Toll-Roads", "the Harris County Engineer’s sign permit page"),
    # address post
    "usps_faq": A("https://faq.usps.com/articles/Knowledge/ZIP-Code-The-Basics", "USPS’s own ZIP Code FAQ"),
    "usps_lookup": A("https://tools.usps.com/zip-code-lookup.htm?byaddress", "USPS ZIP Code lookup"),
    "z80": A("https://zipcodes-us.com/zip5/77380", "77380"),
    "z84": A("https://zipcodes-us.com/zip5/77384", "77384"),
    "z85": A("https://zipcodes-us.com/zip5/77385", "77385"),
    "z89": A("https://zipcodes-us.com/zip5/77389", "77389"),
    "z54": A("https://zipcodes-us.com/zip5/77354", "77354"),
    "zspring": A("https://www.zip-codes.com/m/city/tx-spring.asp", "zip-codes.com’s Spring list"),
    "har_sr": A("https://www.har.com/pricetrends/woodlands-village-of-sterling-ridge-77354-realestate/11714", "HAR lists Sterling Ridge homes in 77354 under Magnolia"),
    "abc13": A("https://abc13.com/post/the-woodlands-incorporation-election-is-a-city-town-montgomery-county-elections/11174055/", "ABC13"),
    "tw_inc": A("https://www.thewoodlandstownship-tx.gov/Government/Governance/Incorporation", "the Township’s incorporation page"),
    "ci_shen": A("https://communityimpact.com/the-woodlands/government/shenandoah-celebrates-50-years-while-maintaining-small-town-feel/", "Community Impact"),
    "schema": A("https://developers.google.com/webmasters/business-location-pages/schema.org-examples", "Google’s LocalBusiness structured data docs"),
    # Google docs (used in posts 2 and 3)
    "gbp_rules": A("https://support.google.com/business/answer/3038177?hl=en", "Google’s guidelines for representing your business"),
    "gbp_sa": A("https://support.google.com/business/answer/9157481?hl=en", "Google’s service area help page"),
    "gbp_rank": A("https://support.google.com/business/answer/7091?hl=en", "Google’s page on local ranking"),
    "gbp_posts": A("https://support.google.com/business/answer/7342169?hl=en", "Google’s posts help page"),
    "gbp_reviews": A("https://support.google.com/business/answer/3474050?hl=en", "Google’s review management page"),
    "maps_policy": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "Google Maps’ prohibited content policy"),
    "ads_org": A("https://support.google.com/google-ads/answer/1722080", "Google Ads help"),
    "starter": A("https://developers.google.com/search/docs/fundamentals/seo-starter-guide", "Google’s SEO Starter Guide"),
    "spam": A("https://developers.google.com/search/docs/essentials/spam-policies", "Google’s spam policies"),
    "sel": A("https://searchengineland.com/why-google-business-profile-get-suspended-395796", "Search Engine Land"),
}

SIGNS = "/blog/business-sign-rules-the-woodlands-houston/"
ADDR = "/blog/the-woodlands-spring-conroe-address-local-seo/"
MYTHS = "/blog/local-seo-myths-houston-the-woodlands/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: sign rules (rules guide)
    {
        "slug": "business-sign-rules-the-woodlands-houston",
        "title": "Business Sign Rules in The Woodlands (and How They Compare With Houston)",
        "seo_title": "Business Sign Rules in The Woodlands vs. Houston",
        "desc": "Business sign rules in The Woodlands and Houston: Township covenants, A-frames, banners, window signs, Houston permits and the fines for bandit signs.",
        "category": "Local marketing",
        "icons": ["Google Business Profile", "Google", "Meta"],
        "art": "b2",
        "hero": "billboard",
        "hero_alt": "Illustration of a roadside sign for a guide to business sign rules in The Woodlands and Houston",
        "related": ["grand-opening-marketing-plan-30-days", "billboard-advertising-cost-houston", "small-business-marketing-ideas-the-woodlands"],
        "sections": [
            (None, f"""<p>“Can we just stick a few signs out by the road for the grand opening?”</p>
<p>A new client asks us some version of that about once a month, usually a week before they open, usually holding a box of 18-by-24 corrugated signs they already paid for. The short answer in The Woodlands is no. The short answer in Houston is also no. The longer answer is more useful, because a lot of signs <i>are</i> allowed, and the businesses that know the rules get more out of their storefront than the ones who learn them from a code officer.</p>
<p>This is a working guide to business sign rules in The Woodlands, with the City of Houston, unincorporated Harris County and the state highway rules alongside for comparison. We’re marketers, not lawyers, and the rules below come straight from the documents we link. Read the source before you print anything, and treat this as the map rather than the permit.</p>"""),

            ("First question: who controls the ground your sign stands on?", f"""<p>Most sign confusion north of Houston comes from one fact. The Woodlands isn’t a city.</p>
<p>It’s a special-purpose district run by The Woodlands Township, and voters chose to keep it that way in November 2021, per {SRC['tw_inc']}. Roads and policing are handled by Montgomery and Harris counties, as {SRC['abc13']} explained before that vote. So the Township doesn’t write sign ordinances the way Houston does. Commercial property in The Woodlands is governed by recorded covenants and the {SRC['cpds']}, which are deed restrictions that run with the land. {SRC['tw_cad']} says plainly that the Township “does not enforce ordinances,” but it monitors and enforces residential and commercial covenants.</p>
<p>That gives you four different rulebooks within a 20-minute drive of Market Street:</p>
<ul>
<li><b>Inside The Woodlands:</b> Township covenants and the Commercial Planning and Design Standards for anything on the lot. County and state law for anything in the road.</li>
<li><b>Shenandoah, Oak Ridge North, Conroe:</b> incorporated cities with their own sign ordinances and their own permit desks. A shop on the I-45 frontage in Shenandoah is not under Township covenants, even if the mailing address says The Woodlands.</li>
<li><b>Spring, Klein, Cypress and other unincorporated Harris County:</b> Harris County permits on-premise signs.</li>
<li><b>City of Houston:</b> the Houston Sign Code and Houston Sign Administration.</li>
</ul>
<!--fig:jurisdiction-->
<p>Before you design anything, find out which of those you’re in. Your lease, your landlord and your property tax statement will tell you faster than Google will.</p>"""),

            ("Can I put this sign here? The two-minute decision", f"""<p>We use the same sequence with every client opening a location. It catches most problems before they cost money.</p>
<!--fig:decision-->
<p>The table below puts the common sign types side by side. Section numbers refer to the Township standards and the Houston documents linked in each row of this guide.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Sign type</th><th>The Woodlands (Township covenants)</th><th>City of Houston</th></tr></thead>
<tbody>
<tr><td>Permanent building or monument sign</td><td>Submit and get approval before fabrication (6.3.C). Business name or clarifier only; no phone, website or hours (6.3.F, 6.3.L)</td><td>Permit required; usually pulled by a licensed sign contractor. Up to five signs per business</td></tr>
<tr><td>A-frame / sandwich board</td><td>Pre-approved if you follow 6.4.D: one per tenant, max 6 sq ft, near the main entrance, brought inside at close, no prices</td><td>The Sign Administration FAQ lists portable signs as not allowed; ask before you buy one</td></tr>
<tr><td>Grand opening banner</td><td>Needs approval (6.5). Up to 3 ft x 8 ft, neutral background, 4 weeks before to 2 weeks after opening (6.7.H)</td><td>Only as a Limited Use Banner: 7 consecutive days in any 30, max 40 sq ft, flush on the wall, permit each time</td></tr>
<tr><td>Window signs</td><td>Mostly not allowed where visible from outside. Small exceptions: open sign, name graphic, hours (6.6.M)</td><td>Governed by the sign code and the attention-getting device rules; check before you cover the glass</td></tr>
<tr><td>Feather flags, balloons, inflatables</td><td>Balloons, pennants, similar devices and inflatables of any type are prohibited (6.3.I)</td><td>Banners, pennants and balloons fall under the attention-getting device ordinance (Sec. 28-37)</td></tr>
<tr><td>Signs in the road right-of-way</td><td>Not the Township’s call. State law (Ch. 393) prohibits them, and the county or TxDOT removes them</td><td>Prohibited under Secs. 28-38 and 28-39 and state law; $300 to $500 per violation</td></tr>
</tbody></table></div>
<p>The rows that trip people up are the last three. We’ll go through them one rulebook at a time.</p>"""),

            ("The Woodlands commercial sign rules, sign by sign", f"""<p>The {SRC['cpds']} were revised and recorded in August 2026. {SRC['ci_cov']} reported in October 2026 that the commercial standards had been through a three-year revision that touched window graphics, among other things. If you’re working from a PDF a landlord emailed you in 2022, get the current one from {SRC['tw_comm']}.</p>
<p>Article VI holds the sign standards. The general rules in Section 6.3 do most of the work:</p>
<ul>
<li><b>Approval comes before fabrication.</b> Any temporary or permanent sign visible from the outside of a building “must be Submitted and Approved by the Plan Review Committee prior to fabrication and installation” (6.3.C). Order the sign first and you may own a very expensive piece of plastic.</li>
<li><b>Name only.</b> “Only Business Clarifiers or Business Names are permitted on Signs” (6.3.F), and the name must match across your monument sign, building sign and window graphics (6.3.G). Phone numbers, websites, tag lines and hours aren’t permitted on monument or building signs unless specifically allowed (6.3.L).</li>
<li><b>Watch the words “The Woodlands.”</b> The developer holds trademarks on them. Applications that include those words get forwarded to its representative, who has 20 days to object, and an objection blocks approval (6.3.B). “Woodlands Pilates Co.” needs more lead time than “Juniper Pilates.”</li>
<li><b>No sign spinners, no tree signs.</b> Signs can’t be held by people, placed in trees or mounted on structures not built for signs (6.3.H).</li>
</ul>
<!--fig:prohibited-->
<h3>A-frames and menu boards</h3>
<p>Good news for restaurants and retail around Hughes Landing and Market Street: A-frames are pre-approved, so you don’t submit them, as long as you follow Section 6.4.D. One per tenant, near the main entrance. No more than 6 square feet. It can’t block foot traffic or accessibility, it can’t be chained down, and it comes inside every night at close. The message is limited to general products or services and special events, with no prices or specific product names, and only the top 12 inches can carry your name or logo. Restaurants also get one pre-approved menu board up to 4 square feet and no taller than five feet including the stand (6.4.E).</p>
<p>That “no prices” rule surprises people. “Happy hour 3-6” is about a special event. “$5 margaritas” is a price. We’d write the first one.</p>
<h3>Window signs</h3>
<p>Section 6.6.M starts from no. Signs aren’t allowed in exterior windows or doors where they can be seen from outside. The exceptions are small: one “Open” sign per occupied tenant space up to 2 square feet; one white vinyl name graphic up to 2 square feet (two on double doors); and a set of hours, website and emergency info that together can’t exceed 1 square foot. Interior signs should sit about two feet back from the glass so they aren’t primarily visible from outside (6.6.A).</p>
<p>If your Houston location has posters taped to every pane, your Woodlands location won’t.</p>
<h3>Temporary signs, opening banners and leasing signs</h3>
<p>“Coming Soon” signs, business banners and “Now Open” signs are not pre-approved (6.5). They go through review like everything else. Once approved, Section 6.7 sets the limits:</p>
<ul>
<li>Opening banners can go up no more than four weeks before and come down no later than two weeks after initial opening, can’t exceed 3 feet high by 8 feet wide, and use a single neutral background of white, gray or black (6.7.H). A window graphic version can’t exceed 50 square feet.</li>
<li>Temporary signs in general must be on the site they pertain to, can’t carry product, price or other advertising unless specifically allowed, and ground-mounted ones max out at six feet tall and 32 square feet (6.7.A).</li>
<li>For Lease signs: one per vacant space per street frontage, two per site at most, 4 square feet each, and gone within seven days of signing the lease (6.7.E).</li>
<li>Now Hiring for an established business: one sign up to 4 square feet in a window or door (6.7.I).</li>
</ul>
<!--fig:numbers-->
<p>Reviews go through Plan Review Committees, and the Development Standards Committee (four Township-appointed residents and three developer appointees) is the only body that can grant variances, per {SRC['tw_cad']}. Applications go through the Township’s Civic Access Portal, and commercial questions go to Covenant Administration at 281-210-3800. Ask for site-specific sign criteria too (6.3.A); many shopping centers have their own sign criteria layered on top of the Township’s.</p>"""),

            ("A grand opening sign timeline for The Woodlands", f"""<p>Here’s how we’d schedule signs for a business opening in a Woodlands shopping center. The six-week lead time is our working assumption, not a Township promise. Committee meeting dates and your landlord’s own approval are the things that set the real clock.</p>
<!--fig:timeline-->
<p>The trap is the two-week tail. Most owners would happily leave a “Now Open” banner up for three months. The standards say two weeks after initial opening, so plan the rest of your opening buzz around things that aren’t signs: your {L('/blog/grand-opening-marketing-plan-30-days/', '30-day grand opening plan')}, a Google Business Profile that’s verified before the doors open, and some paid social targeted to the surrounding villages. Signs tell people who drive past. Everything else reaches the people who don’t.</p>"""),

            ("Houston sign code basics: permits, contractors and fees", f"""<p>Inside Houston city limits, signs are a permit question first. {SRC['hou_sign']} regulates and permits advertising signs under the Houston Sign Code, with height, size and lighting limits that depend on the street category. Permits are required before signs are erected, altered or repaired, and they generally go to licensed sign contractors.</p>
<p>The numbers that matter for a typical storefront, from {SRC['hou_onprem']}:</p>
<ul>
<li>Up to five signs per business. One ground or projecting sign per frontage, two total, with more allowed only on frontages over 350 feet. Up to four wall signs and three marquee signs.</li>
<li>Off-premises advertising is prohibited. Your sign advertises your business, on your property.</li>
<li>Owners can permit and install their own non-electrical signs only in limited cases: ground signs of 60 square feet or less and 8 feet or less in height, or wall signs no higher than 16 feet above grade. Hire anyone else and they need a sign contractor license.</li>
<li>Fees start around $69.46 for the minimum operating permit, plus a $33.56 administrative fee and $97.25 each for plan review and inspection, covering the first 32 square feet. Operating permits renew annually.</li>
<li>Processing runs 4 to 11 business days. Construction permits are good for 180 days from the site inspection.</li>
</ul>
<p>Banners are where Houston gets strict. The {SRC['hou_faq']} calls the code “very banner prohibitive” and says “a banner by itself can’t be permitted.” Back it and frame it and it becomes a wall sign, permitted as such. The only other route is a Limited Use Banner. Per the {SRC['hou_lub']}, it can be displayed for a maximum of seven consecutive days within any 30-day period, can’t exceed 40 square feet, must be attached flush against the building wall with no ropes or ties, can’t flap in the wind, and only one is allowed per premises at a time. Each seven-day run needs its own permit.</p>
<p>The same FAQ lists portable signs, rolling billboards and bandit signs among signs that aren’t allowed, along with anything banned by the attention-getting device ordinance. That ordinance, Section 28-37 in {SRC['hou_ch28']}, covers banners, pennants, balloons and certain lights. We’d assume the feather flags you see along Westheimer fall under it until Sign Administration tells you otherwise.</p>
<!--fig:compare-->"""),

            ("Spring, Klein and Cypress: unincorporated Harris County", f"""<p>A lot of businesses with a Spring or Cypress address aren’t in any city. In unincorporated Harris County, {SRC['hc_oce']} says permits are required for all new and renovated signs, sorted into toll road, scenic district, major thoroughfare and freeway categories. Construction of off-premise signs is prohibited outright. Expect a site plan showing every existing and proposed sign, a survey for new ground signs, 3 to 5 business days for processing and 180 days to finish construction.</p>
<p>If your shopping center along FM 2920 or the Grand Parkway has an owners’ association, it probably has sign criteria too. As in The Woodlands, private restrictions stack on top of public rules. They don’t replace them.</p>"""),

            ("Bandit signs: the cheapest ad that costs the most", f"""<p>Bandit signs are the corrugated plastic signs on stakes that bloom in esplanades every Saturday morning: “We Buy Houses,” “Roofing $0 Down,” “Grand Opening This Way.” They’re illegal on public right-of-way almost everywhere in Texas, and that includes the medians on Woodlands Parkway and Research Forest.</p>
<p>State law is short. Section 393.002 of {SRC['tx393']} says a person may not place a sign on the right-of-way of a public road unless state law authorizes it. A sheriff, constable or trained volunteer authorized by the county commissioners court can confiscate those signs (393.003), and signs worth under $25 can be thrown away without the usual notice. Under {SRC['tx393007']}, a district, county or municipal attorney can sue for a civil penalty of $500 to $1,000 per violation, and each day of a continuing violation can be a separate penalty.</p>
<p>Houston adds its own. Sections 28-38 and 28-39 of {SRC['hou_ch28']} ban advertising on curbs, sidewalks, utility poles, trees and traffic signs, with fines of $300 to $500 per violation and each day a separate offense. City employees can impound the signs, and lightweight stake signs can be disposed of immediately. {SRC['hou_bandit']} lists the usual illegal spots: esplanades, the strip between sidewalk and curb, overpasses, utility poles, light standards and signal boxes.</p>
<!--fig:penalties-->
<p>On state highways (I-45, SH 242, the Grand Parkway and their frontage roads), {SRC['txdot']} says TxDOT may remove unauthorized signs immediately and without notice, store them, and dispose of unclaimed ones. Inside incorporated cities, the city usually handles removal.</p>
<p>Our opinion, from the marketing side: bandit signs are bad advertising even before the fines. The phone number on a stake sign is right there for any code officer to call. A sign in the median says “this company cuts corners” to the exact homeowners you want to hire you. And the response is untrackable, so you’ll never know whether the 200 signs paid for themselves. If you need roadside reach, a permitted billboard is the legitimate version; our {L('/blog/billboard-advertising-cost-houston/', 'Houston billboard cost guide')} has real numbers.</p>"""),

            ("What we’d do instead of more signs", f"""<p>Signs do one job: they tell people who are already driving past that you exist and where the door is. Build the rest of your local visibility where the rules work in your favor.</p>
<ul>
<li><b>Google Business Profile, verified before opening day.</b> “Near me” searches start in Maps, not in the median. Our guide to {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Houston map pack')} covers the setup.</li>
<li><b>A sign that matches your profile.</b> The Township requires the same name across your signs. Use that exact name on Google too. Mismatched names confuse customers and complicate verification.</li>
<li><b>Paid social and search around the location.</b> A radius around Hughes Landing or your Spring strip center reaches the same people a banner would, for longer than two weeks. Our {L('/services/paid-social-advertising/', 'paid social team')} runs opening campaigns like this.</li>
<li><b>Reviews from your first customers.</b> The {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has scripts that stay inside Google’s rules.</li>
</ul>
<p>If you’re opening in The Woodlands or Houston and want the signs, the profile and the launch campaign to line up, <a href="/contact/">get in touch</a> and tell us your opening date. A senior strategist will put together a plan that fits it.</p>"""),
        ],
        "faq": [
            ("Do I need approval for a business sign in The Woodlands?",
             "Almost always. The Woodlands Commercial Planning and Design Standards require any temporary or permanent sign visible from outside the building to be submitted and approved by the Plan Review Committee before it is fabricated or installed. A few signs are pre-approved, including one compliant A-frame per tenant and a small restaurant menu board. Grand opening, coming soon and now open banners all need approval."),
            ("Can I use an A-frame sign in The Woodlands?",
             "Yes, within limits. Section 6.4.D of the Township standards pre-approves one A-frame per tenant near the main entrance, up to 6 square feet. It cannot block traffic or accessibility, cannot be chained down and must come inside each evening at closing. The message can cover general products, services and special events, but no prices or specific product names, and only the top 12 inches can show your name or logo."),
            ("How long can a grand opening banner stay up in The Woodlands?",
             "Under Section 6.7.H of the Township standards, an opening banner can go up no more than four weeks before initial opening and must come down within two weeks after. It cannot exceed 3 feet by 8 feet and must use one neutral background color, white, gray or black. The banner still needs approval first, because coming soon and now open banners are not pre-approved signs."),
            ("Do I need a permit for a banner in Houston?",
             "Yes. Houston’s sign code is very restrictive on banners. A banner alone cannot be permitted, though a backed and framed banner can be permitted as a wall sign. Otherwise the only option is a Limited Use Banner permit, which allows one banner up to 40 square feet, mounted flush on the building wall, for up to seven consecutive days in any 30-day period. Each display period needs its own permit."),
            ("What is the fine for bandit signs in Houston and Texas?",
             "In Houston, placing advertising signs on curbs, sidewalks, poles or other public property carries a fine of $300 to $500 per violation, and each day counts separately. Texas Transportation Code Chapter 393 bans signs on public road right-of-way statewide and allows a civil penalty of $500 to $1,000 per violation, per day. Signs can also be confiscated and thrown away without notice."),
        ],
        "figures": {
            "jurisdiction": {
                "type": "map",
                "title": "Four sign rulebooks north of Houston",
                "sub": "Who regulates a business sign depends on where the property sits, not the mailing address",
                "highlight": ["The Woodlands", "Shenandoah", "Conroe", "Spring", "Cypress", "Houston"],
                "note": "Township covenants in The Woodlands; city ordinances in Shenandoah, Oak Ridge North and Conroe; Harris County permits in unincorporated Spring and Cypress; Houston Sign Code inside city limits.",
                "alt": "Map of sign rule jurisdictions around The Woodlands and Houston, including Shenandoah, Conroe, Spring and Cypress",
                "caption": "A Woodlands mailing address doesn’t mean Township rules apply. Check the property, not the envelope.",
            },
            "decision": {
                "type": "steps",
                "title": "Can I put this sign here?",
                "sub": "Run every sign through these questions before you order it",
                "steps": [["Is it in the road right-of-way?", "Median, curb strip, utility pole or highway frontage: stop. State law says no."], ["Whose rules cover the lot?", "Township covenants, a city, Harris County or the City of Houston."], ["Is it pre-approved?", "In The Woodlands, a compliant A-frame or menu board is. Most other signs aren’t."], ["Does it need approval or a permit?", "Submit before you fabricate. Houston permits go through licensed contractors."], ["Does it expire?", "Opening banners, leasing signs and Houston banners all have clocks. Calendar the removal date."]],
                "alt": "Decision steps for whether a business sign is allowed in The Woodlands or Houston, from right-of-way to permits",
                "caption": "Most sign trouble starts at question one or question four.",
            },
            "prohibited": {
                "type": "checklist",
                "title": "Not allowed on Woodlands commercial signs",
                "sub": "From Section 6.3 of the Township’s commercial standards",
                "items": ["Signs that move, scroll, play sound or blink", "Balloons, pennants and similar devices", "Inflatables of any type", "Signs held by people (sign spinners)", "Signs in trees or on non-sign structures", "Product ads on light poles or gas pumps", "Phone, website, hours or tag lines on building signs", "Anything other than your business name or clarifier"],
                "alt": "Checklist of prohibited commercial sign types in The Woodlands Township standards compared with Houston",
                "caption": f"Summarized from {SRC['cpds']}. Some items have narrow exceptions, so read the section.",
            },
            "numbers": {
                "type": "stats",
                "title": "The Woodlands sign numbers to remember",
                "stats": [["6 sq ft", "max A-frame, one per tenant"], ["3x8 ft", "max opening banner"], ["4+2 wk", "banner weeks before and after opening"], ["2 sq ft", "max open sign in a window"]],
                "note": "Source: The Woodlands Commercial Planning and Design Standards, Aug 2026",
                "alt": "Key business sign size and time limits in The Woodlands, used to compare with Houston sign rules",
                "caption": "Write these on the sign shop’s order form.",
            },
            "timeline": {
                "type": "funnel",
                "title": "Grand opening signs in The Woodlands",
                "stages": [["Get landlord and center sign criteria", "8+ weeks out"], ["Submit to the Plan Review Committee", "6+ weeks out"], ["Fabricate after approval", "4-5 weeks out"], ["Banner goes up", "Up to 4 weeks before"], ["Banner comes down", "2 weeks after opening"]],
                "note": "Illustrative example. Committee schedules set the real timeline.",
                "alt": "Timeline funnel for grand opening sign approval and banner dates for a business in The Woodlands",
                "caption": "Order nothing until step three.",
            },
            "compare": {
                "type": "compare",
                "title": "Opening-week signs: what gets pulled vs. what lasts",
                "left": {"title": "Gets removed or fined", "items": ["Stake signs in the median", "Zip-tied banner on a fence", "Feather flags at the curb", "Posters covering every window", "Sign spinner at the light"]},
                "right": {"title": "Stays up legally", "items": ["Approved building sign", "Permitted banner, flush on the wall", "One compliant A-frame by the door", "Small open sign and name graphic", "Paid ads and a verified Google profile"]},
                "alt": "Comparison of illegal and legal grand opening signs for businesses in The Woodlands and Houston",
                "caption": "The right column costs more up front and nothing in fines.",
            },
            "penalties": {
                "type": "bars",
                "title": "What a right-of-way sign can cost",
                "sub": "Per violation; each day can count as a separate violation",
                "items": [["Houston Code, minimum fine", 300, "$300"], ["Houston Code, maximum fine", 500, "$500"], ["Texas Ch. 393, minimum penalty", 500, "$500"], ["Texas Ch. 393, maximum penalty", 1000, "$1,000"]],
                "highlight": [3],
                "note": "Sources: Houston Code Secs. 28-38, 28-39; Tex. Transp. Code 393.007",
                "alt": "Bar chart of bandit sign fines and penalties in Houston and under Texas law, relevant to The Woodlands businesses",
                "caption": "Multiply by the number of signs and the number of days. Then add the cost of the signs you lose.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: city and ZIP for local SEO (explainer)
    {
        "slug": "the-woodlands-spring-conroe-address-local-seo",
        "title": "The Woodlands, Spring or Conroe? How to List Your City and ZIP for Local SEO",
        "seo_title": "The Woodlands, Spring or Conroe? City and ZIP for SEO",
        "desc": "Should your address say The Woodlands, Spring or Conroe? USPS city names by ZIP, Google Business Profile rules, citations and what not to fake.",
        "category": "SEO & AI search",
        "icons": ["Google Business Profile", "Google", "Search Console"],
        "art": "b4",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for choosing The Woodlands, Spring or Conroe as a business address for local SEO",
        "related": ["change-business-address-google-without-suspension", "rank-in-google-map-pack-houston", "multi-location-local-seo-houston-franchises"],
        "sections": [
            (None, f"""<p>One dental office, one suite, three addresses. The website footer said The Woodlands, TX 77380. Google Business Profile said Spring, TX 77380. Yelp said Shenandoah. The owner asked us which one was wrong.</p>
<p>Technically, none of them. That’s the whole problem.</p>
<p>The Woodlands is not a city, its ZIP codes belong to post offices named Spring, Conroe and Magnolia, and the U.S. Postal Service will deliver to the same suite under more than one city name. For mail, that’s fine. For local SEO, where Google and every directory try to match your business across the web, three versions of one address look like three businesses, or one sloppy one.</p>
<p>Below: how city names actually work for The Woodlands ZIP codes, what to put on Google, your website and your citations, and the few things you should never do to look more “Woodlands” than you are.</p>"""),

            ("Why The Woodlands has no city limits (and Spring doesn’t either)", f"""<p>The Woodlands is a master-planned community governed by The Woodlands Township, a special-purpose district. Residents voted in November 2021 to keep that model instead of incorporating as a city, per {SRC['tw_inc']}. It spans Montgomery and Harris counties, and the counties handle roads and policing, as {SRC['abc13']} explained before the vote.</p>
<p>Spring isn’t a city either. It’s a large unincorporated area, mostly in Harris County, and “Spring, TX” on an envelope mostly means “served by the Spring post office.” Meanwhile, the small cities wedged against The Woodlands are very real. Shenandoah, for example, is an incorporated city of about 2 square miles along I-45 that celebrated 50 years in 2024, per {SRC['ci_shen']}. Oak Ridge North sits just south of it. Conroe is a city, and a big one.</p>
<!--fig:map-->
<!--fig:facts-->
<p>So when a customer types “dentist The Woodlands,” Google isn’t checking a city limit line, because for most of The Woodlands there isn’t one. It works from where your business is, where the searcher is, and what your profile and the rest of the web say about you.</p>"""),

            ("What USPS actually accepts for The Woodlands ZIP codes", f"""<p>{SRC['usps_faq']} says it directly: “ZIP Codes do not necessarily adhere to city or municipal boundaries.” A ZIP code is built around a post office and its carrier routes. Each ZIP has one default city name, and many have additional acceptable names the post office will also deliver to.</p>
<p>We checked ZIP databases built from USPS city-state data for every ZIP that touches The Woodlands. The pattern is consistent: the default name is usually Spring or Conroe, and The Woodlands is an accepted alternate.</p>
<div class="bp-tbl"><table>
<thead><tr><th>ZIP</th><th>Default USPS city</th><th>Also accepted</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>{SRC['z80']}</td><td>Spring</td><td>The Woodlands, Shenandoah</td><td>Street delivery</td></tr>
<tr><td>77381</td><td>Spring</td><td>The Woodlands, Shenandoah</td><td>Street delivery</td></tr>
<tr><td>77382</td><td>Spring</td><td>The Woodlands</td><td>Street delivery</td></tr>
<tr><td>{SRC['z84']}</td><td>Conroe</td><td>The Woodlands, Shenandoah</td><td>Conroe default surprises people</td></tr>
<tr><td>{SRC['z85']}</td><td>Conroe</td><td>The Woodlands, Shenandoah, Oak Ridge North</td><td>Conroe default</td></tr>
<tr><td>77386</td><td>Spring</td><td>The Woodlands, Oak Ridge North</td><td>Street delivery</td></tr>
<tr><td>{SRC['z89']}</td><td>Spring</td><td>The Woodlands, Klein</td><td>Harris County side, incl. Creekside Park addresses</td></tr>
<tr><td>{SRC['z54']}</td><td>Magnolia</td><td>The Woodlands, Decker Prairie</td><td>Includes part of Sterling Ridge</td></tr>
<tr><td>77387, 77393</td><td>Spring</td><td>The Woodlands</td><td>P.O. boxes only</td></tr>
</tbody></table></div>
<p>The 77381 to 77393 rows come from {SRC['zspring']}; the linked ZIPs go to their individual records. ZIPs don’t follow village lines either. One example: {SRC['har_sr']}, even though they’re squarely inside The Woodlands.</p>
<!--fig:defaults-->
<p>Two caveats. Third-party ZIP sites lag USPS updates, so confirm your exact street address with the {SRC['usps_lookup']}, which returns the standardized address and the recognized city names. And “accepted” isn’t the same as “the only right answer.” For a Woodlands business in 77380, “The Woodlands, TX 77380” and “Spring, TX 77380” will both get your mail. You just have to pick one.</p>"""),

            ("Which city name should a Woodlands business use?", f"""<p>Our rule is simple. If The Woodlands is an accepted USPS city name for your ZIP and your location is physically in The Woodlands, use “The Woodlands.” It’s what customers say, it’s what they search, and it’s what your signage and lease probably say already.</p>
<p>Exceptions we’d make:</p>
<ul>
<li><b>You’re in Shenandoah or Oak Ridge North.</b> You’re in an actual city with its own permits and taxes. Using “The Woodlands” in your mailing address is allowed in ZIPs where USPS accepts it, but your city name in business filings and permits should be the real municipality. We usually keep Shenandoah on the profile for these clients and say “next to The Woodlands” in the copy.</li>
<li><b>You’re in Spring proper, Conroe proper or Magnolia.</b> If your ZIP doesn’t list The Woodlands as acceptable, don’t use it. Full stop.</li>
<li><b>Your address is already established everywhere as Spring.</b> If ten years of citations, your bank, your state filings and your Google profile all say Spring, a switch has a cost. It can be worth doing; just do it once, everywhere, in one push.</li>
</ul>
<!--fig:steps-->
<p>Whatever you pick, the name has to match your Secretary of State filing, your bank, your lease and your Google profile closely enough that a verification reviewer sees one business. If you’re mid-move, read our guide to {L('/blog/change-business-address-google-without-suspension/', 'changing your business address on Google without a suspension')} before you touch the profile.</p>"""),

            ("How Google Business Profile handles your address", f"""<p>Google’s rules on addresses are short and strict. Per {SRC['gbp_rules']}, use “a precise, accurate address and/or service area,” and P.O. boxes or mailboxes at remote locations aren’t acceptable. A virtual office, meaning a rented address where you don’t actually operate, isn’t eligible for a Business Profile. A co-working space only qualifies if you have clear signage, receive customers there during business hours and keep it staffed.</p>
<p>Two things to know about the city field specifically:</p>
<ol>
<li><b>Google places the pin by geography, not by your city label.</b> Ranking leans on distance, which Google describes as how far the business is from the person searching, per {SRC['gbp_rank']}. Typing “The Woodlands” instead of “Spring” doesn’t move your pin one foot.</li>
<li><b>Google may display its own locality.</b> In profiles we manage, Google sometimes shows a different city name on Maps than the one the owner entered, based on its own map data. Don’t fight it with repeated edits. Repeated address edits are one of the things that trigger re-verification.</li>
</ol>
<p>What you control is consistency and relevance: the same name, address and phone everywhere; a primary category that matches what you do; and a website that clearly says where you are and who you serve. Our guide to {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Houston map pack')} goes through the rest.</p>
<!--fig:flow-->"""),

            ("Storefront, service area or hybrid?", f"""<p>A lot of the “which city” anxiety is really a service-area question. A plumber based in a Conroe home office wants to show up for “plumber The Woodlands.” The fix is a service area, and a fake Woodlands address makes things worse.</p>
<p>Google’s rules, from {SRC['gbp_sa']} and {SRC['gbp_rules']}:</p>
<ul>
<li>If you don’t serve customers at your address, remove the address from your profile and set a service area instead.</li>
<li>You can set up to 20 service areas by city, postal code or other area.</li>
<li>The overall area shouldn’t extend more than about 2 hours of driving time from where the business is based.</li>
<li>Hybrid businesses, which serve customers at the address and also go out to them, can show both.</li>
</ul>
<p>To edit it: open your Business Profile, choose Edit profile, then Location, and edit the Service area. Google says the service area “helps people find your Business Profile.” It doesn’t say it boosts ranking in every listed town, and in our experience it doesn’t. A Conroe-based service business will still rank best near Conroe. The way to compete in The Woodlands is with reviews from Woodlands customers, a strong Woodlands service page and, often, paid search covering the gap.</p>
<!--fig:compare-->"""),

            ("Your website and citations: one version, everywhere", f"""<p>Citations are mentions of your name, address and phone on other sites: Yelp, Apple Maps, Bing Places, the Chamber directory, Nextdoor, industry directories. Google says prominence draws on information from across the web, like links, articles and directories, per {SRC['gbp_rank']}. Consistency matters most here, because these sites copy each other.</p>
<p>On your own website:</p>
<ul>
<li>Put the exact chosen address in the footer and on the contact page, as text rather than an image.</li>
<li>Use LocalBusiness structured data with a PostalAddress that matches. {SRC['schema']} list address and name as required properties and the address as “the physical location of the business.” Use the same city there that you use everywhere else.</li>
<li>Write naturally about the area. “Our office is off Research Forest, five minutes from Market Street” helps people and search engines more than a footer stuffed with every ZIP from 77380 to 77393.</li>
</ul>
<!--fig:citations-->
<p>Cleaning up citations is tedious but finite. Start with the big data sources and the sites that rank on page one for your business name, then work down. Don’t create a second listing to “cover” Spring; you’ll just make a duplicate that Google may merge or suspend.</p>"""),

            ("Spring vs. The Woodlands in search: what customers actually type", f"""<p>The city on your address and the city in a customer’s search don’t have to match, and often won’t.</p>
<p>Someone in Creekside Park has a Spring mailing address and still searches “pediatrician The Woodlands.” Someone in Oak Ridge North might search “Spring” or “The Woodlands” depending on which side of I-45 they think of as home. Someone in a Conroe ZIP near the north end of The Woodlands probably doesn’t search “Conroe” at all.</p>
<p>So don’t pick your address city to chase keywords. Pick it for accuracy and consistency, then cover the search terms with content:</p>
<ul>
<li>Your homepage and service pages can say “serving The Woodlands, Spring, Shenandoah and Conroe” once, in a sentence a human would write.</li>
<li>Your Google Business Profile description can name the areas you serve in plain language.</li>
<li>Your reviews will do some of this for you. A customer writing “best plumber in Spring” on a Woodlands profile helps more than anything you’d type yourself, which is one more reason to ask every customer.</li>
</ul>
<p>To see what people actually search before they find you, open Google Search Console, go to Performance, and filter queries containing “woodlands,” then “spring,” then “conroe.” In accounts we’ve looked at, the split is rarely what the owner expects. That report tells you which area page to write next, and which one you don’t need.</p>
<h3>If you’re already listed as Spring</h3>
<p>Switching an established Spring listing to The Woodlands is optional, not urgent. If you decide to do it, do it in this order: confirm the new format with USPS, update your state filing and bank if needed, update Google Business Profile once, update the website footer, contact page and schema the same day, then work through the citation sites over the next few weeks. Expect Google to ask for re-verification. Don’t make other profile changes (name, category, phone) in the same week, so that if something goes sideways you know what caused it.</p>
<p>And if your address is fine as Spring, leave it alone. A consistent Spring address beats an inconsistent Woodlands one every time.</p>"""),

            ("What not to do: fake addresses and city-page spam", f"""<p>Every few months a business owner asks us to set up a Woodlands address “just for Google.” These are the versions we hear, and why we won’t do any of them.</p>
<ul>
<li><b>Virtual offices and mailbox stores.</b> Ineligible under Google’s guidelines, and the most common reason we see listings suspended. {SRC['sel']} lists virtual offices, P.O. boxes and UPS Store boxes among the main suspension causes.</li>
<li><b>An employee’s house.</b> If you don’t serve customers there and there’s no signage or staff, it’s not your business location.</li>
<li><b>City names in the business name.</b> “Smith Plumbing The Woodlands” is not your name. Google’s guidelines don’t allow location information in the name unless it’s part of your real-world brand.</li>
<li><b>Copy-paste city pages.</b> {SRC['spam']} name “pages targeted at specific regions or cities that funnel users to one page” as doorway abuse, and “blocks of text that list cities and regions” as keyword stuffing. A real page about your work in Creekside Park, with real photos and reviews, is fine. Thirty near-identical pages aren’t.</li>
</ul>
<p>If you have more than one real location, each gets its own profile and its own page. Our {L('/blog/multi-location-local-seo-houston-franchises/', 'multi-location local SEO guide')} covers that setup, and {L('/blog/power-of-local-landing-pages/', 'local landing pages')} explains how to write area pages that aren’t spam.</p>
<p>If your listings are a patchwork of Spring, The Woodlands and Shenandoah and you’d like them cleaned up once, properly, <a href="/contact/">get in touch</a>. Tell us where you are and who you serve, and a senior strategist will map out the fix and the {L('/services/web-design-seo-pr/', 'SEO work')} around it.</p>"""),
        ],
        "faq": [
            ("Is The Woodlands, TX a city?",
             "No. The Woodlands is an unincorporated master-planned community governed by The Woodlands Township, a special-purpose district. Voters chose in November 2021 to keep that model instead of incorporating. It spans Montgomery and Harris counties, and the counties handle roads and law enforcement. Nearby Shenandoah, Oak Ridge North and Conroe are incorporated cities, while Spring is an unincorporated area served by the Spring post office."),
            ("Which ZIP codes accept The Woodlands as a city name?",
             "ZIP databases built from USPS data list The Woodlands as an accepted city name for 77380, 77381, 77382, 77384, 77385, 77386, 77389 and 77354, plus the P.O. box ZIPs 77387 and 77393. The default USPS name is usually Spring, Conroe or Magnolia. Confirm your exact street address with the USPS ZIP Code lookup, since third-party ZIP sites can lag behind postal updates."),
            ("Should my Google Business Profile say Spring or The Woodlands?",
             "Use the city name that USPS accepts for your ZIP and that matches where your business really is. For a location inside The Woodlands, we usually recommend The Woodlands. Then use that exact address everywhere, including your website, citations and business filings. The city label does not move your map pin, and Google ranks by distance and relevance, so consistency matters more than the label."),
            ("Can I use a virtual office address in The Woodlands for Google?",
             "No. Google’s guidelines say a virtual office, meaning a rented address where your business does not operate, is not eligible for a Business Profile. P.O. boxes and remote mailboxes are not acceptable either. Co-working spaces only qualify with clear signage, staff on site and customers received during business hours. If you serve customers at their locations, hide your address and set a service area instead."),
            ("How do I show up in The Woodlands if my office is in Conroe or Spring?",
             "Set a service area in Google Business Profile that includes The Woodlands, but expect to rank best near your actual location, since distance is a ranking factor. Build a genuine Woodlands service page with local projects and photos, ask Woodlands customers for reviews, and consider paid search for Woodlands keywords. Do not create a fake address or a second listing to cover the area."),
        ],
        "figures": {
            "map": {
                "type": "map",
                "title": "The Woodlands and the towns on its edges",
                "sub": "Mailing names, city limits and Google’s map labels don’t always agree here",
                "highlight": ["The Woodlands", "Shenandoah", "Spring", "Conroe", "Magnolia", "Tomball"],
                "note": "Shenandoah, Oak Ridge North and Conroe are incorporated cities. The Woodlands and Spring are not.",
                "alt": "Map of The Woodlands with Spring, Conroe, Shenandoah and Magnolia for choosing a business address for local SEO near Houston",
                "caption": "Your pin sits where your door is. The city name is a label on top of it.",
            },
            "defaults": {
                "type": "bars",
                "title": "Default USPS city for Woodlands-area ZIPs",
                "sub": "Count of ZIPs (including P.O. box ZIPs) where The Woodlands is an accepted alternate",
                "items": [["Spring is the default", 7, "7 ZIPs"], ["Conroe is the default", 2, "2 ZIPs"], ["Magnolia is the default", 1, "1 ZIP"], ["The Woodlands is the default", 0, "0"]],
                "highlight": [0],
                "note": "Source: ZIP databases built from USPS city-state data; confirm with USPS",
                "alt": "Bar chart of default USPS city names for The Woodlands ZIP codes, mostly Spring and Conroe, for local SEO",
                "caption": "That’s why so many Woodlands businesses end up listed as Spring without ever choosing it.",
            },
            "steps": {
                "type": "steps",
                "title": "Pick your city name once",
                "sub": "The order we use with clients in The Woodlands, Spring and Shenandoah",
                "steps": [["Run the USPS lookup", "Enter your exact street address and note every accepted city name."], ["Check the real jurisdiction", "Township, Shenandoah, Oak Ridge North, Conroe or county."], ["Match your paperwork", "State filing, lease, bank and signage should line up."], ["Write it down", "One exact format, including suite style and ZIP+4 if you use it."], ["Update in one push", "Google, website, schema, then the citation sites."]],
                "alt": "Steps to choose a consistent city name and ZIP for a business address in The Woodlands, Spring or Conroe",
                "caption": "Step four is the one everybody skips. Suite 200 vs. Ste. 200 vs. #200 is how the mess starts.",
            },
            "compare": {
                "type": "compare",
                "title": "Covering The Woodlands from outside it",
                "left": {"title": "Shortcuts that backfire", "items": ["Virtual office on Lake Robbins", "Second listing for Spring", "City name added to business name", "30 copy-paste city pages", "Editing the address every month"]},
                "right": {"title": "What works", "items": ["Service area that includes The Woodlands", "One profile per real location", "Your real business name", "A few genuine area pages with real jobs", "One address, set once, everywhere"]},
                "alt": "Comparison of risky and effective ways to rank in The Woodlands for businesses based in Spring or Conroe",
                "caption": "The left column gets listings suspended. The right column takes longer and keeps working.",
            },
            "citations": {
                "type": "checklist",
                "title": "Where your address has to match",
                "sub": "Fix these first, in roughly this order",
                "items": ["Google Business Profile", "Website footer and contact page", "LocalBusiness schema on the site", "Apple Business Connect", "Bing Places", "Yelp and Facebook", "Chamber and industry directories", "Texas filings, bank and payment processors"],
                "alt": "Checklist of citation sites where a Woodlands or Spring business address must match for local SEO",
                "caption": "Same name, same address format, same phone number on every one.",
            },
            "facts": {
                "type": "stats",
                "title": "The address facts behind the confusion",
                "stats": [["0", "city limits for The Woodlands"], ["2", "counties: Montgomery and Harris"], ["20", "max service areas on Google"], ["~2 hr", "max drive for a service area"]],
                "note": "Sources: Woodlands Township, ABC13, Google Business Profile Help",
                "alt": "Stats on The Woodlands Township, its two counties and Google service area limits for Houston-area local SEO",
                "caption": "Unincorporated, two counties, and a profile system that cares about where you really are.",
            },
            "flow": {
                "type": "funnel",
                "title": "What Google uses to place you in local results",
                "stages": [["Your real address or service area", "Sets the pin"], ["Your category and profile details", "Relevance"], ["Distance to the searcher", "Biggest local filter"], ["Reviews, links and citations", "Prominence"], ["Who shows in the map pack", "The result"]],
                "note": "Based on Google’s description of relevance, distance and prominence",
                "alt": "Funnel of how Google ranks a The Woodlands or Spring business in local search, from address to map pack",
                "caption": f"From {SRC['gbp_rank']}. Notice that the city label isn’t on the list.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: local SEO myths (myth-buster)
    {
        "slug": "local-seo-myths-houston-the-woodlands",
        "title": "Local SEO Myths Houston and The Woodlands Business Owners Still Believe",
        "seo_title": "Local SEO Myths Houston & The Woodlands Owners Believe",
        "desc": "Ten local SEO myths we still hear from Houston and The Woodlands owners, checked against Google’s own documentation, with what to do instead.",
        "category": "SEO & AI search",
        "icons": ["Google Business Profile", "Google Ads", "Search Console"],
        "art": "b6",
        "hero": "search",
        "hero_alt": "Illustration of a search bar for local SEO myths believed by Houston and The Woodlands business owners",
        "related": ["rank-in-google-map-pack-houston", "how-long-does-seo-take-houston-the-woodlands", "seo-vs-paid-ads-woodlands-business"],
        "sections": [
            (None, f"""<p>Ten myths. All of them came up in a sales call, a client meeting or a networking lunch in The Woodlands or Houston this year. Several came from people who had paid someone to tell them.</p>
<p>Local SEO attracts myths because the results are visible and the reasons aren’t. You can see that the HVAC company in Spring is in the map pack and you aren’t. You can’t see why. So people fill the gap with whatever they heard last.</p>
<p>For each myth below we’ve gone to Google’s own documentation (Business Profile Help, Search Central and Google Ads Help) and linked the page. Each one gets three parts: the myth, what’s actually true, and what to do about it. Where something is our experience rather than Google’s word, we say so.</p>
<!--fig:summary-->
<p>If you only have two minutes, this table is the whole post.</p>
<div class="bp-tbl"><table>
<thead><tr><th>#</th><th>Myth</th><th>Google’s source</th><th>Check this week</th></tr></thead>
<tbody>
<tr><td>1</td><td>Keywords in your business name help</td><td>Business Profile guidelines</td><td>Does your Google name match your sign exactly?</td></tr>
<tr><td>2</td><td>Post on your profile every day</td><td>Posts help page</td><td>Is your last post useful, or just there?</td></tr>
<tr><td>3</td><td>Review count is everything</td><td>Local ranking help</td><td>Are you asking every customer the same way?</td></tr>
<tr><td>4</td><td>You need an office in every suburb</td><td>Guidelines, service area help</td><td>Is every address on your profile staffed?</td></tr>
<tr><td>5</td><td>SEO is one-and-done</td><td>SEO Starter Guide</td><td>When did anyone last update your hours or photos?</td></tr>
<tr><td>6</td><td>Google Ads boosts organic rank</td><td>Google Ads help</td><td>Are you judging ads and SEO separately?</td></tr>
<tr><td>7</td><td>A page for every suburb</td><td>Spam policies</td><td>Would a customer learn anything from your area pages?</td></tr>
<tr><td>8</td><td>Domain keywords, meta keywords, word count</td><td>SEO Starter Guide</td><td>Does each page answer the question fast?</td></tr>
<tr><td>9</td><td>Duplicate content gets you penalized</td><td>SEO Starter Guide</td><td>Is your main location page written for your city?</td></tr>
<tr><td>10</td><td>Number one for you means number one for everyone</td><td>Local ranking help</td><td>Have you checked rankings from across your area?</td></tr>
</tbody></table></div>"""),

            ("Myth 1: Putting “Houston” or “The Woodlands” in your Google business name helps you rank", f"""<p><b>Myth.</b> Rename “Juniper Plumbing” to “Juniper Plumbing The Woodlands Water Heater Repair” and you’ll climb the map pack.</p>
<p><b>What’s actually true.</b> It might work for a while. That’s why the myth survives. But {SRC['gbp_rules']} say your name should reflect your real-world business name, and “including unnecessary information in your business name isn’t permitted.” Google’s own examples ban taglines, service info and location details, such as “Holiday Inn (I-93 at Exit 2).” {SRC['sel']} lists keyword-stuffed names among the top causes of profile suspensions, and competitors can suggest edits to your name whenever they like.</p>
<p><b>What to do.</b> Use the name on your sign, your filing and your invoices. If you want “The Woodlands” in your name, it has to be in your actual brand. (And in The Woodlands, putting it on your sign has its own trademark review; see our {L(SIGNS, 'sign rules guide')}.) Put the keywords in your primary category, your services list and your website instead.</p>"""),

            ("Myth 2: You have to post on Google Business Profile every day", f"""<p><b>Myth.</b> Daily posts tell Google you’re active, and active profiles rank.</p>
<p><b>What’s actually true.</b> {SRC['gbp_posts']} describes three post types (updates, offers and events), explains that posts older than six months are archived unless a date range is set, and makes no claim about posting frequency or ranking. {SRC['gbp_rank']}, which is Google’s own list of what affects local results, doesn’t mention posts at all.</p>
<p><b>What to do.</b> Post when you have something a customer would care about: a seasonal offer, an event, new hours for the holidays, photos of a finished job in Kingwood. In accounts we manage, two to four useful posts a month is plenty. Spend the time you save on photos and review replies, which customers actually look at.</p>"""),

            ("Myth 3: Review count is everything", f"""<p><b>Myth.</b> Whoever has the most reviews wins, so the plan is to get to 500.</p>
<p><b>What’s actually true.</b> Reviews matter. Google says “more reviews and positive ratings can help your business’s local ranking,” per {SRC['gbp_rank']}. But reviews feed one of three factors. The other two are relevance (how well your profile matches the search) and distance (how far you are from the searcher). A business with 900 reviews in Katy will usually lose a “near me” search in Tomball to a business with 90 reviews in Tomball.</p>
<p><b>What to do.</b> Ask every customer, steadily, the same way. Don’t buy reviews, don’t offer discounts for them and don’t only ask happy customers. {SRC['maps_policy']} prohibits incentives and selective solicitation. Reply to reviews too; {SRC['gbp_reviews']} notes that helpful replies show you’re responsive. Our {L('/blog/complete-guide-google-reviews/', 'Google reviews guide')} has scripts.</p>
<!--fig:factors-->
<p>Ranking is only half of what reviews do. The other half happens after a customer finds you.</p>
<!--fig:funnel-->"""),

            ("Myth 4: You need an office in every suburb you want to rank in", f"""<p><b>Myth.</b> To show up in Katy, Cypress, Sugar Land and The Woodlands, you need an address in each. A virtual office will do.</p>
<p><b>What’s actually true.</b> Distance is a real ranking factor, so a physical location does help near that location. But a rented address where you don’t operate “isn’t eligible for a Business Profile,” per {SRC['gbp_rules']}, and P.O. boxes and remote mailboxes aren’t acceptable. Service businesses can list up to 20 service areas, covering no more than about 2 hours of driving from where they’re based, per {SRC['gbp_sa']}.</p>
<p><b>What to do.</b> If you have real, staffed locations, give each its own profile. If you don’t, set your service area honestly, build a genuine page for each area you actually work in, and use paid search to cover suburbs where you won’t win the map pack. Our explainer on {L(ADDR, 'The Woodlands, Spring and Conroe addresses')} covers the north-side version of this problem.</p>
<!--fig:radius-->"""),

            ("Myth 5: SEO is a one-and-done project", f"""<p><b>Myth.</b> Pay for SEO once, during the website build, and you’re set for years.</p>
<p><b>What’s actually true.</b> {SRC['starter']} says some changes “might take effect in a few hours, others could take several months,” and that “there are no secrets here that’ll automatically rank your site first.” Rankings move because competitors keep publishing, Google keeps updating, and your own information goes stale: hours, services, staff, photos.</p>
<p>A composite of what we see in Houston audits: a business pays for a site in 2021, ranks decently in 2022, and by 2025 the hours on Google are wrong, the photos show a storefront that’s been remodeled, the newest review reply is two years old, and three competitors in Cypress have added real service pages. Nothing “broke.” Everyone else just kept going.</p>
<p><b>What to do.</b> Set up a small monthly routine and keep it going. It doesn’t need to be expensive. Before hurricane season and before the holidays, add a quick check of special hours, since those are the weeks people search “open now.” For how long the early work takes to show up, see {L('/blog/how-long-does-seo-take-houston-the-woodlands/', 'how long SEO takes in Houston and The Woodlands')}.</p>
<!--fig:routine-->"""),

            ("Myth 6: Running Google Ads boosts your organic rankings", f"""<p><b>Myth.</b> Spend on Google Ads and Google will reward you in the free results, or stop spending and it will punish you.</p>
<p><b>What’s actually true.</b> {SRC['ads_org']} puts it in one sentence: “Google’s search results are independent of Google’s advertising programs.” On the local side, {SRC['gbp_rank']} says “there’s no way to request or pay for a better local ranking on Google.”</p>
<p>The myth usually comes from a real pattern. When a business runs ads, its name shows up more often, more people search for it by name, and branded traffic rises. That’s demand, not a ranking favor from Google. And if an ad and an organic listing show for the same search, some of the clicks you used to get for free will go to the ad. That’s worth measuring before you assume ads are “helping SEO.”</p>
<p><b>What to do.</b> Treat ads and SEO as two separate tools. Ads buy visibility now, for searches where you can’t rank yet. SEO builds visibility you don’t pay for per click. Many Houston service businesses need both for a while. We compare them in {L('/blog/seo-vs-paid-ads-woodlands-business/', 'SEO vs. paid ads')}, and our {L('/services/search-marketing/', 'search marketing team')} runs both.</p>"""),

            ("Myth 7: You need a page for every suburb and ZIP code", f"""<p><b>Myth.</b> Publish “Plumber Katy,” “Plumber Cypress,” “Plumber Spring” and 40 more pages with the town name swapped, and you’ll rank everywhere.</p>
<p><b>What’s actually true.</b> {SRC['spam']} list “multiple domain names or pages targeted at specific regions or cities that funnel users to one page” as doorway abuse, and “blocks of text that list cities and regions that a web page is trying to rank for” as keyword stuffing. Mass-produced pages with little value fall under scaled content abuse.</p>
<p><b>What to do.</b> Build area pages only where you have something real to say: jobs you did there, local photos, reviews from customers in that town, specifics like “we see a lot of slab leaks in older Meyerland homes.” Five strong pages beat fifty thin ones. Our {L('/blog/power-of-local-landing-pages/', 'local landing pages guide')} shows the difference.</p>"""),

            ("Myth 8: Keywords in the domain name, meta keywords and word count still move rankings", f"""<p><b>Myth.</b> Buy bestplumberhoustontx.com, fill the meta keywords tag and make every page 2,000 words.</p>
<p><b>What’s actually true.</b> {SRC['starter']} is blunt on all three. “Google Search doesn’t use the keywords meta tag.” Keywords in a domain name “have hardly any effect beyond appearing in breadcrumbs.” And “the length of the content alone doesn’t matter for ranking purposes.” There’s no magic heading count either.</p>
<p><b>What to do.</b> Pick a domain that matches your brand and is easy to say on the radio. Write pages as long as they need to be to answer the customer’s question, and no longer. A clear price range and a phone number above the fold usually do more than another 800 words.</p>"""),

            ("Myth 9: Duplicate content gets you penalized", f"""<p><b>Myth.</b> If your service description appears on two pages, or matches your franchisor’s site, Google will penalize you.</p>
<p><b>What’s actually true.</b> Per {SRC['starter']}, duplicate content “is not a violation of our spam policies” and isn’t something that causes a manual action. It’s inefficient: Google picks one version to show, which may not be the one you want.</p>
<p><b>What to do.</b> Don’t panic over a repeated paragraph. Do write unique copy for your most important pages, so they have a reason to rank on their own. Franchise owners in Sugar Land or The Woodlands should make their location page clearly local rather than a copy of corporate.</p>"""),

            ("Myth 10: Once you’re in the map pack, you’re there for everyone", f"""<p><b>Myth.</b> “We’re number one on Google.” Usually said by the owner, searching from their own office.</p>
<p><b>What’s actually true.</b> Distance is one of Google’s three local factors, and Google says it uses the searcher’s location, or what it knows about it, per {SRC['gbp_rank']}. Results for “dentist near me” in Hughes Landing look different from results on the Grand Parkway at 249.</p>
<p><b>What to do.</b> Check rankings from several points across your service area, not just your desk. A grid-based rank tracker does this well. Then judge local SEO on calls, direction requests and booked jobs, which you can see in your profile’s performance report and your call tracking. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} explains how to read those numbers.</p>
<!--fig:check-->"""),

            ("What actually moves local SEO in Houston and The Woodlands", f"""<p>Strip out the myths and what’s left is unglamorous. Google’s own list in {SRC['gbp_rank']} comes down to complete and accurate information, the right categories, reviews you reply to, photos, and a website that other sites link to.</p>
<!--fig:effort-->
<p>We’d add two from experience. First, answer the phone. Ranking well and sending calls to voicemail is the most expensive local SEO mistake we see. Second, measure with real numbers. If you can’t say how many calls came from your Google profile last month, start there; {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'our tracking guide')} shows how.</p>
<p>If you’ve heard a myth that isn’t on this list, or you’re paying someone for one that is, <a href="/contact/">get in touch</a>. Tell us about your business and what you want from search, and a senior strategist will build a plan around what Google actually says works.</p>"""),
        ],
        "faq": [
            ("Does adding Houston or The Woodlands to my Google business name help ranking?",
             "It can appear to help briefly, but Google’s guidelines say your Business Profile name must match your real-world business name and that unnecessary information, including location details and service keywords, is not permitted. Keyword-stuffed names are a common cause of suspensions, and competitors can suggest edits. Use your real name and put keywords in your categories, services and website."),
            ("How often should I post on my Google Business Profile?",
             "Google does not say posting frequency affects ranking, and its list of local ranking factors does not mention posts. Posts older than six months are archived unless they have a date range. Post when you have something useful, such as an offer, an event, holiday hours or photos of recent work. For most Houston and The Woodlands businesses, two to four good posts a month is enough."),
            ("Does Google Ads improve my organic or map rankings?",
             "No. Google Ads Help states that Google’s search results are independent of its advertising programs, and Google Business Profile Help says there is no way to request or pay for a better local ranking. Ads and SEO are separate tools. Many local businesses run ads for searches where they do not rank yet while building organic visibility over time."),
            ("Do I need an office in each Houston suburb to rank there?",
             "Not to appear at all, but distance is a ranking factor, so a real location helps most near that location. Virtual offices and mailbox addresses are not eligible for Google Business Profiles. Service businesses can set up to 20 service areas within about two hours of driving. Build genuine area pages and use paid search for suburbs where you cannot win the map pack."),
            ("Is local SEO a one-time project?",
             "No. Google’s SEO Starter Guide says changes can take anywhere from a few hours to several months to have an effect, and that no secret will automatically rank a site first. Competitors keep publishing, Google keeps updating and your own details go stale. A modest monthly routine of profile updates, review replies, photos and page improvements keeps results from slipping."),
        ],
        "figures": {
            "summary": {
                "type": "compare",
                "title": "Ten local SEO myths at a glance",
                "left": {"title": "What owners hear", "items": ["Keywords in the business name", "Post every day", "Most reviews wins", "An office in every suburb", "SEO is one-and-done"]},
                "right": {"title": "What Google’s docs say", "items": ["Real-world name only", "No posting frequency rule", "Relevance, distance and prominence", "Virtual offices aren’t eligible", "Changes take hours to months"]},
                "alt": "Comparison of common local SEO myths and Google documentation for Houston and The Woodlands businesses",
                "caption": "Myths 6 through 10 are further down: ads, city pages, old-school on-page tricks, duplicate content and rank checking.",
            },
            "factors": {
                "type": "stats",
                "title": "Google’s three local ranking factors",
                "stats": [["1", "Relevance: does the profile match?"], ["2", "Distance: how far from the searcher?"], ["3", "Prominence: reviews, links, reputation"], ["$0", "what you can pay for a better rank"]],
                "note": "Source: Google Business Profile Help, local ranking",
                "alt": "Stats tiles of Google's three local ranking factors for Houston and The Woodlands local SEO",
                "caption": "Reviews live inside one of the three. They’re not the whole game.",
            },
            "radius": {
                "type": "map",
                "title": "One real office, a realistic reach",
                "sub": "A Woodlands-based service business: strong nearby, weaker at the edges",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Magnolia", "Katy", "Sugar Land", "Pearland"],
                "note": "Google allows up to 20 service areas within about 2 hours of driving. Map pack visibility still fades with distance.",
                "alt": "Map of service area reach for a The Woodlands business across Houston suburbs like Spring, Katy and Sugar Land",
                "caption": "Inside the inner ring, SEO does the work. Out by Katy and Pearland, plan on ads.",
            },
            "routine": {
                "type": "steps",
                "title": "A monthly local SEO routine",
                "sub": "About two to four hours a month for a single-location business",
                "steps": [["Check the profile", "Hours, holiday hours, phone, categories and any suggested edits."], ["Reply to every review", "Same week, specific, no copy-paste."], ["Add real photos", "Recent jobs, team, storefront, inside."], ["Improve one page", "Add a price range, FAQ, photos or a recent project."], ["Read the numbers", "Calls, direction requests and booked jobs from Google."]],
                "alt": "Monthly local SEO routine steps for Houston and The Woodlands small businesses",
                "caption": "Boring, repeatable and usually enough to keep you from sliding.",
            },
            "check": {
                "type": "checklist",
                "title": "Before you believe the next SEO tip",
                "sub": "Questions we ask about any local SEO claim",
                "items": ["Is there a Google help page that says it?", "Does it break Google’s name or address rules?", "Would it hold up if a competitor reported you?", "Is the proof one screenshot from one location?", "Can you measure it in calls or bookings?", "Does it help a customer, or only a crawler?"],
                "alt": "Checklist for testing local SEO advice for Houston and The Woodlands business owners",
                "caption": "Most myths fail the first question.",
            },
            "effort": {
                "type": "columns",
                "title": "Where we’d spend the next 10 hours",
                "sub": "Our weighting for a typical single-location Houston business",
                "labels": ["Profile", "Reviews", "Site pages", "Photos", "Citations", "Posts"],
                "values": [90, 80, 70, 45, 35, 20],
                "highlight": [0, 1],
                "y_label": "Relative priority",
                "note": "Illustrative example based on our experience, not a Google ranking formula",
                "alt": "Column chart of local SEO priorities for Houston and The Woodlands businesses, profile and reviews first",
                "caption": "Your mix depends on what’s already done. Fix the profile before anything else.",
            },
            "funnel": {
                "type": "funnel",
                "title": "How a local searcher actually chooses",
                "stages": [["Sees the map pack", "3 businesses"], ["Scans rating and review count", "Trust check"], ["Reads a few recent reviews and replies", "Tone check"], ["Looks at photos or the website", "Fit check"], ["Calls, books or asks for directions", "The lead"]],
                "note": "Illustrative example of a typical path, not measured data",
                "alt": "Funnel of how customers in Houston and The Woodlands choose a local business from Google search results",
                "caption": "Ranking gets you to the first stage. The rest is reviews, replies, photos and a phone that gets answered.",
            },
        },
    },
]
