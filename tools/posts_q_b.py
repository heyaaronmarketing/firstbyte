"""Batch 17 (module b): three non-niche posts for Houston and The Woodlands business owners, each in its own format.

1. PR playbook: getting covered by Houston and The Woodlands media.
   Research: Community Impact corporate/circulation page (founded 2005, 35+ editions, 2M+ mailboxes) and Houston
   advertising page (15 Houston editions, about 1.15 million mailboxes monthly); Community Impact's March 2024
   "26 businesses now open, coming soon" roundup for The Woodlands; InnovationMap About page (Gow Media / CultureMap,
   story-idea link and editor inbox); Hearst's July 2016 release on buying Houston Community Newspapers; Wikipedia on
   The Villager (weekly, Hearst since 2016; current print status not confirmed, so the post tells readers to check);
   University of Houston page on Houston Public Media (NPR and PBS, 2.7M+ monthly audience); Next TV's Feb 2022
   Houston local news close-up (KTRK ABC-owned, KPRC Graham/NBC, KRIV Fox-owned, KHOU Tegna/CBS, Univision 45 led
   10 p.m. household ratings in January 2022, Houston DMA No. 8); Houstonia About page (Hour Media); The Woodlands City
   Lifestyle site (Lifestyle Publications, partner/advertiser model); The Woodlands Township Community Magazine page
   (bimonthly, mailed to every residential address, no ads, in-house content only); Talking Biz News (July 2017) on
   HBJ People on the Move becoming a $250 paid listing; Top Workplaces (189 Chronicle Top Workplaces in 2024);
   Cision 2025 State of the Media (3,000+ journalists; 72% press releases most useful; 86% reject off-beat pitches;
   85% prefer an email introduction); Muck Rack State of Journalism 2026 via University of Minnesota (62% prefer 1:1
   email, 69% under 200 words, 70% beat relevance, 78% before noon); Google spam policies (optimized anchor text in
   press releases distributed on other sites; sponsored links need rel="sponsored" or "nofollow"); KPRC Houston Life
   sponsored-article disclosure (April 2026).
   Left out: reporter names (by design); Villager's current print schedule (could not confirm); a Woodlands-specific
   Community Impact household count (not published on the pages we could read).

2. Directory/comparison table: chambers and networking groups in The Woodlands and Houston.
   Research: The Woodlands Area Chamber join page (Small Business $500 through Corporate Partners $15,000, $50
   enrollment fee, credits and benefits per level); Greater Houston Partnership 2026 Membership Guide (Limited Partner
   $3,000 through Executive Partner $120,000) and small business page (HBX, Export Houston); Houston Hispanic Chamber
   About page (mission; no published dues); Asian Chamber of Commerce 2026 membership levels PDF ($250-$5,000;
   public companies with 250+ employees move to corporate tier); Conroe/Lake Conroe Chamber 2025 member benefits PDF
   ($500-$5,000, nonprofits 20% off); Community Impact on the March 2024 Montgomery Area Chamber merger (about 240
   members, roughly 30% in both); Greater Tomball Area Chamber 2025 investment guide ($350-$10,000); Houston Northwest
   Chamber May 2024 membership packet ($40/month or $400/year up to $10,000); Community Impact (Nov 2021) on Spring-Klein
   Chamber merger talks with Tomball after pandemic losses; City of Houston Economic Development chamber list; BNI About
   page (1985, 355K members, 11,800 chapters, 17.8M referrals, $26.9B reported) and one-per-specialty article;
   Community Impact (June 2026) on a new BNI chapter for New Caney/Porter; GHBA Belong page; IRS EO technical
   instruction text on IRC 162(e)/6033(e) dues and lobbying notices.
   Left out: Katy Area Chamber, Houston Hispanic Chamber, Greater Houston Black Chamber and LGBT Chamber dues (not
   published on pages we could read); BNI fees (set per chapter, not centrally published); GHBA dues (not published).

3. ROI guide with worked calculator: local sponsorships and youth sports.
   Research: The Woodlands Township Adult Sports sponsorship proposal (4,800+ participants; $250 banners to $15,000
   presenting partner; 15%/10% multi-year and renewal discounts); Clear Springs Baseball Booster Club 2026 form (League
   City, 501(c)(3), $500-$2,000 tiers); Woodlands Lacrosse 2025-26 sponsor initiative (fee waivers tied to sponsorship
   amounts); YES to YOUTH 2026 gala page (Aug 8, 2026, Woodlands Waterway Marriott; $5,000-$50,000); Woodlands Online
   Sports 2025-26 sponsorship notice via the Woodlands Chamber (prices on request; audience claims); Township release on
   the 2026 Red, Hot & Blue Festival (five sites, Repsol, Renewal by Andersen at Town Green Park); Community Impact on
   The Woodlands Waterway Arts Festival (about 200 artists, Town Green Park, $1.4M returned); Visit The Woodlands on
   Fidelity Investments as returning title sponsor; Little League local fundraising best practices; GA4 URL builder
   help (utm_source, utm_medium, utm_campaign); IRS Tax Tip 2021-159 on advertising deductions; Treasury final
   regulations on qualified sponsorship payments (Federal Register, April 25, 2002); IRS Publication 526; Greenberg
   Traurig on OBBBA charitable limits from 2026 (corporate 1% floor, 10% cap); Google spam policies on sponsored links.
   Left out: ISD stadium advertising price lists (Fort Bend ISD and Katy ISD PDFs would not load); Waterway Arts
   Festival and Red, Hot & Blue sponsorship prices (not published); the IRS "advertising or qualified sponsorship
   payments" web page (blocked, so we cite the regulation text instead).
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # post 1: PR
    "ci_about": A("https://communityimpact.com/corporate-circulation/", "Community Impact’s company page"),
    "ci_hou": A("https://advertising.communityimpact.com/advertise/houston/print", "Community Impact’s Houston print page"),
    "ci_roundup": A("https://communityimpact.com/the-woodlands/business/26-businesses-now-open-coming-soon-and-announcing-news-in-the-woodlands-area/", "a March 2024 Woodlands roundup"),
    "innomap": A("https://houston.innovationmap.com/about", "InnovationMap’s About page"),
    "hearst": A("https://www.globenewswire.com/news-release/2016/07/29/1009790/0/en/Hearst-Purchases-Locally-Focused-Houston-Community-Newspapers-Media-Group.html", "bought Houston Community Newspapers in 2016"),
    "villager": A("https://en.wikipedia.org/wiki/The_Villager_(The_Woodlands,_Texas)", "The Villager"),
    "hpm": A("https://uh.edu/af/houston-public-media", "a service of the University of Houston"),
    "nexttv": A("https://nexttv.com/features/local-news-close-up-stations-battle-for-booming-houstons-new-arrivals", "Next TV’s 2022 look at Houston local news"),
    "houstonia": A("https://www.houstoniamag.com/about-us", "Houstonia"),
    "citylife": A("https://citylifestyle.com/thewoodlands/", "The Woodlands City Lifestyle"),
    "twpmag": A("https://www.thewoodlandstownship-tx.gov/Departments/Communications/Community-Magazine", "The Township’s community magazine page"),
    "potm": A("https://talkingbiznews.com/they-talk-biz-news/people-on-the-move-becomes-acbj-revenue-stream/", "Talking Biz News"),
    "topwp": A("https://topworkplaces.com/award/chron/2024/", "189 employers in 2024"),
    "cision": A("https://www.cision.com/about/press-releases/2025-press-releases/cisions-2025-state-of-the-media-report-reveals-a-tipping-point-for-trust-technology-and-pr-journalist-partnerships-302448410/", "Cision’s 2025 State of the Media survey"),
    "muckrack": A("https://umarcomm.umn.edu/blog/2026/04/13/pitching-journalists-muck-racks-state-journalism-2026", "Muck Rack’s State of Journalism 2026"),
    "gspam": A("https://developers.google.com/search/docs/essentials/spam-policies", "Google’s spam policies"),
    "hlife": A("https://www.click2houston.com/houston-life/2026/04/14/taking-care-of-business-how-the-houston-hispanic-chamber-helps-local-companies-grow/", "a KPRC Houston Life segment page"),
    # post 2: chambers
    "wacc": A("https://www.woodlandschamber.org/join/", "The Woodlands Area Chamber’s join page"),
    "ghp": A("https://wpb.houston.org/app/uploads/2026/02/2026-Membership-Guide.pdf", "the Partnership’s 2026 membership guide"),
    "ghp_smb": A("https://houston.org/smallbusiness", "the Partnership’s small business page"),
    "hhcc": A("https://www.houstonhispanicchamber.com/about-us/", "the Houston Hispanic Chamber"),
    "acc": A("https://asianchamber-hou.org/wp-content/uploads/2026/08/ACC-2026-Membership-Levels.pdf", "the Asian Chamber’s 2026 membership levels"),
    "clc": A("https://www.conroe.org/website/wp-content/uploads/2025/11/member_benefits_2025_final.pdf", "the Conroe/Lake Conroe Chamber’s member benefits sheet"),
    "merge": A("https://communityimpact.com/conroe-montgomery/business/montgomery-and-conroelake-conroe-chambers-of-commerce-merging/", "Community Impact reported the merger"),
    "tomball": A("https://www.tomballchamber.org/assets/pdf/2025+Investment+Guide_5.8", "the Greater Tomball Area Chamber’s 2025 investment guide"),
    "hnwcc": A("https://www.houstonnwchamber.org/wp-content/uploads/2024/04/Membership-Info-Packet-2024May.pdf", "the Houston Northwest Chamber’s May 2024 packet"),
    "skcc": A("https://communityimpact.com/spring-klein/business/updated-spring-klein-greater-tomball-area-chambers-of-commerce-discussing-merger/", "Community Impact reported in November 2021"),
    "coh": A("https://www.houstontx.gov/ecodev/chambers_of_commerce.html", "the City of Houston’s chamber list"),
    "katy": A("https://www.katychamber.com/what-we-do/", "Katy Area Chamber of Commerce"),
    "bni": A("https://bni.com/about", "BNI’s About page"),
    "bni1": A("https://www.bni.com/the-latest/blog-news/why-bni-allows-only-one-profession-per-chapter/", "one professional per specialty"),
    "bnici": A("https://communityimpact.com/houston/new-caney-porter/business/2026/06/08/bni-global-to-launch-entrepreneur-networking-chapter-in-east-montgomery-county/", "a new chapter for New Caney and Porter"),
    "ghba": A("https://ghba.org/belong", "Greater Houston Builders Association"),
    "irsdues": A("https://www.irs.gov/pub/irs-tege/eotopicl03.pdf", "IRS technical guidance on sections 162(e) and 6033(e)"),
    # post 3: sponsorships
    "twpsports": A("https://irp.cdn-website.com/86dd23dc/files/uploaded/Woodlands-Sports-Sponsorship-Proposal.pdf", "The Woodlands Township’s adult sports sponsorship proposal"),
    "csbb": A("https://media.hometeamsonline.com/photos/baseball/CLEARSPRINGSBASEBALL/2026_CSHS_BaseballBooster_Sponsorship_Form.pdf", "Clear Springs Baseball Booster Club’s 2026 form"),
    "lax": A("https://cdn1.sportngin.com/attachments/document/832a-3447997/FINAL_2526_WOODLANDS_LAX_Sponsor_Initiative_.pdf", "Woodlands Lacrosse’s 2025-26 sponsor initiative"),
    "yes": A("https://app.betterunite.com/yestoyouth-2026gala-everafter", "the YES to YOUTH 2026 gala page"),
    "wol": A("https://business.woodlandschamber.org/news/details/woodlands-online-sports-2025-26-sponsorships-opportunities-start-august-1-07-17-2025", "Woodlands Online Sports’ 2025-26 sponsorship notice"),
    "rhb": A("https://www.thewoodlandstownship-tx.gov/Township-News/2026-Press-Releases/June/061826-Red-Hot-Blue", "the Township’s 2026 Red, Hot &amp; Blue release"),
    "wwaf": A("https://communityimpact.com/the-woodlands/arts-entertainment/the-woodlands-waterway-arts-festival-brings-outdoor-art-to-the-woodlands-since-2005/", "Community Impact"),
    "fidelity": A("https://www.visitthewoodlands.com/articles/post/fidelity-investments-returns-as-title-sponsor-of-the-woodlands-waterway-arts-festival/", "Visit The Woodlands"),
    "ll": A("https://www.littleleague.org/?p=280890", "Little League’s roundup of local league fundraising"),
    "utm": A("https://support.google.com/analytics/answer/10917952", "Google Analytics’ URL builder help page"),
    "irsad": A("https://irs.gov/newsroom/small-business-advertising-and-marketing-costs-may-be-tax-deductible", "IRS Tax Tip 2021-159"),
    "fr513": A("https://www.govinfo.gov/content/pkg/FR-2002-04-25/html/02-9930.htm", "Treasury’s final regulations on corporate sponsorship"),
    "p526": A("https://irs.gov/publications/p526", "IRS Publication 526"),
    "gt": A("https://www.gtlaw.com/en/insights/2025/10/new-limitations-on-charitable-deductions-take-effect-in-2026", "Greenberg Traurig’s summary"),
}

PR = "/blog/get-press-coverage-houston-the-woodlands/"
CHAMBERS = "/blog/chambers-networking-groups-the-woodlands-houston/"
SPONSOR = "/blog/local-sponsorships-youth-sports-the-woodlands-houston/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: PR playbook
    {
        "slug": "get-press-coverage-houston-the-woodlands",
        "title": "How to Get Press Coverage in Houston and The Woodlands: A Local PR Playbook",
        "seo_title": "Get Press Coverage in Houston & The Woodlands: PR Playbook",
        "desc": "Who covers what in Houston and The Woodlands media, news hooks that work, a pitch template, timing, mistakes, and how coverage helps your SEO.",
        "category": "Strategy",
        "icons": ["Google", "Search Console", "LinkedIn"],
        "art": "b2",
        "hero": "speech",
        "hero_alt": "Illustration of a speech bubble for getting press coverage from Houston and The Woodlands media",
        "related": ["grand-opening-marketing-plan-30-days", "show-up-in-chatgpt-ai-search-aeo", "radio-tv-advertising-cost-houston"],
        "sections": [
            (None, f"""<p>“How do we get Community Impact to write about us?”</p>
<p>Some version of that question lands in our inbox most months. Usually it comes from an owner who just opened a second location in Spring, or hit ten years off Research Forest, or watched a competitor show up in the paper and thought, why them?</p>
<p>The answer is shorter than people expect. Pick the one outlet whose readers are your customers. Give its reporter something that is actually news to those readers. Make the story easy to write, with the facts, the photo and a person to talk to, all in one short email. Do that four or five times a year and you will get covered in Houston and The Woodlands. Blast a release to every newsroom in the metro and you mostly won’t.</p>
<p>This playbook covers who covers what, the hooks that work, a pitch you can copy, when to send it, what gets you ignored, and how the coverage keeps paying off in Google long after the print copy is in the recycling bin. We don’t name reporters on purpose. Beats change and people move. The staff page on the outlet’s own site is the only list worth trusting, so check it the day you pitch.</p>"""),

            ("Who covers what: the Houston and The Woodlands media map", f"""<p>Most pitches fail before anyone reads them because they went to the wrong outlet. A restaurant opening is not a Houston Business Journal story. A $4 million Series A is not a Community Impact story. Here is how we sort them.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Outlet</th><th>What it covers</th><th>Best hooks for a local business</th></tr></thead>
<tbody>
<tr><td>Community Impact (The Woodlands edition and neighbors)</td><td>Hyperlocal news mailed monthly, plus daily online: openings, closings, development, roads, local government, schools</td><td>Openings, relocations, expansions, anniversaries, a new service the neighborhood will notice</td></tr>
<tr><td>Houston Chronicle</td><td>Metro daily: business, food, real estate, consumer, weather and news</td><td>Big hiring, trends backed by your own data, expert comment on breaking news</td></tr>
<tr><td>The Villager and The Courier</td><td>Hearst’s community papers for The Woodlands and Montgomery County</td><td>Community milestones, local people, events (check each paper’s current schedule before you pitch)</td></tr>
<tr><td>Houston Business Journal</td><td>Weekly business paper: deals, leases, executives, rankings, awards</td><td>B2B growth with real numbers, commercial real estate moves, award nominations</td></tr>
<tr><td>InnovationMap</td><td>Houston startups, tech, health, energy and social impact</td><td>Funding rounds, product launches, founder profiles</td></tr>
<tr><td>KHOU 11, KPRC 2, ABC13, FOX 26</td><td>TV news and morning shows, with heavy weather and consumer coverage</td><td>Visual stories, quick expert interviews when news breaks, consumer tips</td></tr>
<tr><td>Houston Public Media</td><td>Public radio and TV news, explanatory and policy coverage</td><td>Expert sources who can explain an issue calmly and accurately</td></tr>
<tr><td>Local magazines</td><td>Houstonia (city magazine), The Woodlands City Lifestyle, neighborhood titles</td><td>Profiles, lifestyle and food features, often with long lead times</td></tr>
</tbody></table></div>
<p>A few notes on that table, because the details matter when you pitch.</p>
<!--fig:map-->
<p><b>Community Impact</b> launched its first edition in 2005 and now runs more than 35 editions across more than 65 communities, delivered monthly to mailboxes, per {SRC['ci_about']}. In the Houston area it publishes 15 editions reaching about 1.15 million mailboxes a month, per {SRC['ci_hou']}. Neighboring editions cover Spring and Klein, Conroe and Montgomery, Tomball and Magnolia, Katy and Fulshear, and New Caney and Porter, so a business near the edge of The Woodlands should know which edition its customers actually get. The paper’s “now open, coming soon” roundups are the easiest door in for a local business. {SRC['ci_roundup']} listed 26 businesses with an address, a date and a one-paragraph description each, covering everything from a juice bar to a surgery center.</p>
<p><b>The Houston Chronicle</b> is Hearst’s flagship here, and Hearst {SRC['hearst']}, which brought {SRC['villager']} (a weekly for The Woodlands, founded in 1977) and The Courier in Conroe under the same roof. Community papers have been cut back everywhere, so confirm the current print and web schedule before you build a plan around one.</p>
<p><b>InnovationMap</b> comes from Gow Media and the team behind CultureMap and covers “startups, tech, health, energy, social impact, and more,” per {SRC['innomap']}, which also lists a story-idea link and an editor inbox. If you’re a dental office, skip it. If you built software in a Hughes Landing office, it’s your first call.</p>"""),

            ("TV, public radio and the magazines", f"""<p>Houston was the No. 8 TV market in the country in 2022, according to {SRC['nexttv']}. The main English-language news stations are ABC13 (KTRK, owned by ABC), KPRC 2 (NBC, owned by Graham Media Group), KHOU 11 (CBS) and FOX 26 (KRIV, owned by Fox). The same piece reported that Univision 45 topped the 10 p.m. household ratings in January 2022, which surprises a lot of owners. If your customers speak Spanish, Univision and Telemundo belong on your list, and so does our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'guide to Hispanic marketing in Houston')}.</p>
<p>TV wants pictures and people. A pitch that says “we can have a technician on a roof in Kingwood at 7 a.m. showing what hail does to shingles” beats a pitch about your company’s values every time. TV also moves fast. When a freeze is coming or a storm is in the Gulf, assignment desks need experts within hours, and the business that already sent a short “here’s who to call” note gets the call.</p>
<p>Houston Public Media is {SRC['hpm']}, carrying NPR and PBS programming with a combined monthly audience of more than 2.7 million. It is a poor fit for promotion and a good fit for expertise. A CPA who can explain a property tax change clearly, or an engineer who can talk drainage without jargon, is exactly the kind of source public media uses.</p>
<p>Magazines run on long lead times, often months. {SRC['houstonia']} is Houston’s city magazine, owned by Hour Media, and focuses on the people changing how Houstonians “eat, play, dress, and think.” {SRC['citylife']} is a monthly published by Lifestyle Publications that promotes paid print and digital packages alongside its stories, so ask up front whether a feature is editorial or part of a partner package. And one that trips people up: {SRC['twpmag']} says its bimonthly magazine is mailed to every residential address in The Woodlands, carries no advertising and takes content only from Township departments, villages and government partners. You can’t pitch your business into it, though a Township event you support may appear there.</p>
<!--fig:reach-->"""),

            ("News hooks that work in Houston and The Woodlands", f"""<p>Reporters don’t cover businesses. They cover things that happened, things that are about to happen, and things readers need to know. Your job is to find which of those your business is part of.</p>
<!--fig:hooks-->
<p>A few that work well locally:</p>
<ul>
<li><b>Openings, moves and expansions with a date and an address.</b> “Opening March 14 at 25 Waterway Ave., hiring 18” is a story. “Exciting new chapter” isn’t.</li>
<li><b>Your own numbers.</b> An HVAC company that counted service calls by ZIP code during an August heat wave has data nobody else has. So does a pet clinic tracking heatstroke cases, or a moving company that knows which suburbs people are leaving for. One clean chart beats ten adjectives.</li>
<li><b>Fast expert reaction.</b> Hurricane season runs June 1 to November 30. A roofer, a plumber, an insurance agent or a tree service that can explain what to do in two sentences is useful to every newsroom in Houston during that window.</li>
<li><b>Local people.</b> A third-generation owner in Tomball, a veteran who opened a gym in Conroe, a technician who saved a customer’s house during a freeze. Stories need a face.</li>
<li><b>Awards the outlet runs.</b> The Houston Business Journal runs Best Places to Work, and the Houston Chronicle’s Top Workplaces program (run with Energage) recognized {SRC['topwp']}. Nominations and employee surveys cost you time, and a win comes with coverage built in.</li>
</ul>
<p>If you can’t find a hook, wait. Pitching a non-story burns the relationship you need for the real one.</p>"""),

            ("The pitch template", f"""<p>Reporters told {SRC['muckrack']} that 62% prefer a one-to-one email pitch, 69% want it under 200 words, and 70% value clear relevance to their beat above everything else. {SRC['cision']} of more than 3,000 journalists found 86% will immediately reject a pitch that isn’t aligned with their beat or audience. Short, specific and on-beat, in other words.</p>
<!--fig:wants-->
<p>Here is the template we start from. Change every bracket.</p>
<blockquote>
<p><b>Subject:</b> [Business] opening [date] at [street address], [town]</p>
<p>Hi [first name],</p>
<p>[One sentence of news: what, where, when.] [One sentence on why your readers in [area] will care: the gap it fills, the jobs, the change they’ll see.]</p>
<p>Quick facts: [address and cross street], [opening date], [hours], [number of jobs], [price range or service list], [website].</p>
<p>[Owner name] can talk by phone today or tomorrow, and we have high-resolution photos of the space and the team you’re welcome to use.</p>
<p>Thanks,<br>[Name], [title], [phone]</p>
</blockquote>
<p>That’s about 100 words. Notice what isn’t there: no attachment, no history of the company, no adjectives about passion. Paste the press release below your signature if you have one. Don’t attach it.</p>
<!--fig:pitch-->
<p>Address the reporter whose recent stories match your news. Read three of their pieces first, so you know whether they write openings, development or food. And send it from a real person’s inbox with a phone number that gets answered, because a reporter on deadline will call once.</p>"""),

            ("Timing: when to pitch Houston media", f"""<p>The same Muck Rack survey found 78% of journalists prefer pitches before noon. Beyond that, timing in Houston is mostly about lead time and weather.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Outlet type</th><th>When we pitch (our experience)</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Monthly community papers</td><td>Three to six weeks before the date</td><td>Print pages are planned well ahead; online can move faster</td></tr>
<tr><td>Daily papers and news sites</td><td>One to two weeks ahead, or same day for breaking news</td><td>Reporters juggle many stories and need room to fit yours</td></tr>
<tr><td>TV news and morning shows</td><td>A few days ahead, then a reminder the afternoon before</td><td>Assignment desks plan the next day’s shoots the afternoon before</td></tr>
<tr><td>Weekly business papers</td><td>Two to four weeks ahead for features; right away for deals</td><td>Deal news goes stale fast; features need reporting time</td></tr>
<tr><td>Magazines</td><td>Three to six months ahead</td><td>Issues are planned seasons in advance</td></tr>
</tbody></table></div>
<p>Two Houston-specific rules. First, when a named storm is in the Gulf or the power is out across Harris County, nobody wants your anniversary pitch. Hold it. Second, be ready for those weeks if your business has something useful to say, because that’s when an expert pitch lands. We keep a one-paragraph “storm source” note ready for clients who can genuinely help.</p>
<p>Follow up once, about three business days later, with one new piece of information. Then let it go.</p>"""),

            ("What not to do", f"""<p>Most of the pitches that get ignored are polite and well-meant. They just make the reporter do extra work.</p>
<!--fig:dont-->
<p>A few that deserve their own warning. Don’t ask to review a story before it runs; reporters won’t agree, and asking marks you as someone who doesn’t understand the job. Don’t offer money, gifts or meals in exchange for coverage. Don’t pitch the same story to two reporters at the same outlet. And don’t demand a link in the story. You can politely ask for your website to be included for readers, but the call is theirs.</p>
<p>Also watch the line between earned and paid. Plenty of local “coverage” is paid. KPRC’s Houston Life, for example, publishes sponsored segments with a disclosure that “the advertiser paid a fee to promote this sponsored article,” as on {SRC['hlife']}. Back in 2017, {SRC['potm']} reported the Houston Business Journal was charging $250 for expanded People on the Move listings. Paid placements can be worth buying. Just budget them as advertising, judge them like our {L('/blog/radio-tv-advertising-cost-houston/', 'radio and TV cost guide')} suggests, and don’t confuse them with earning a reporter’s interest.</p>"""),

            ("How press coverage helps your SEO", f"""<p>Here’s the part most PR advice skips. A story in a Houston outlet keeps working for you in search for years, in three ways.</p>
<p><b>Links.</b> A link from a real news site is one of the most trusted signals a local business can earn. Many newsrooms mark outbound links with a nofollow attribute, and that’s fine. You still get referral visits and a citation on a site Google knows is real. What doesn’t work is the shortcut. {SRC['gspam']} name “links with optimized anchor text in articles, guest posts, or press releases distributed on other sites” as link spam. A wire release stuffed with “best plumber Houston” links won’t help you and can count against you.</p>
<p><b>Brand searches.</b> In accounts we’ve worked on, a story often shows up as a bump in people searching the business name in the days after it runs, along with more Google Business Profile views and calls. Those searches are the cheapest customers you’ll ever get, because they already want you. Make sure your profile is complete before the story runs. Our {L('/blog/rank-in-google-map-pack-houston/', 'map pack guide')} covers the basics.</p>
<p><b>AI answers.</b> AI search tools lean on sources that look independent, and local news is about as independent as it gets. Being described accurately in Community Impact or the Chronicle gives those tools something to cite. We cover the rest in {L('/blog/show-up-in-chatgpt-ai-search-aeo/', 'how to show up in ChatGPT and AI search')}.</p>
<!--fig:seo-->
<p>To capture it, add a “Press” or “In the news” page that links to every story. Quote a line from the article on the relevant service page. Share it on your Google Business Profile and LinkedIn. And watch brand-name searches in Search Console for the two weeks after publication, so you can see what the story was worth. Our {L('/services/web-design-seo-pr/', 'web design, SEO and PR team')} builds that page into every site we launch.</p>"""),

            ("A 60-day PR plan for a Houston or The Woodlands business", f"""<p>If you’ve never pitched anyone, this is a realistic start for a business with one or two locations.</p>
<ol>
<li><b>Week 1.</b> List your three best possible stories for the next six months. Be honest about which are news.</li>
<li><b>Week 2.</b> Match each story to one outlet and one reporter whose recent work fits. Read their last five pieces.</li>
<li><b>Week 3.</b> Get assets ready: three good photos (owner, team, space), a 100-word company description, one page of facts, and a named spokesperson who will answer the phone.</li>
<li><b>Week 4.</b> Send the first pitch, using the template above, before noon on a weekday that isn’t a storm day.</li>
<li><b>Weeks 5 to 6.</b> One follow-up with new information. If it runs, share it everywhere and add it to your press page.</li>
<li><b>Weeks 7 to 8.</b> Nominate for one award the outlet runs, and send a short “here’s how I can help” introduction to one TV desk for your area of expertise.</li>
</ol>
<p>Pair the first pitch with a real event if you can. Our {L('/blog/grand-opening-marketing-plan-30-days/', '30-day grand opening plan')} shows how the PR, ads and reviews fit together, and the {L(CHAMBERS, 'chamber and networking directory')} covers the ribbon cuttings that often go with it.</p>
<p>If you’d like a strategist to look at your story angles and the outlets that fit them, <a href="/contact/">get in touch</a>.</p>"""),
        ],
        "faq": [
            ("How do I get my business in Community Impact in The Woodlands?",
             "Send a short email to the reporter who covers business or openings for your edition, with the news in the first sentence, the address, the date and a phone number. Community Impact runs regular roundups of businesses that are new, coming soon, relocating or expanding, so a real opening or move with firm details is the easiest way in. Include good photos and send it several weeks ahead of the date."),
            ("Is a press release still worth sending to Houston media?",
             "Yes, as a reference, not as the pitch. Cision’s 2025 survey found 72% of journalists still call press releases the most useful thing PR teams provide. Lead with a short personal email that explains why the story matters to that outlet’s readers, then paste the release below your signature. Skip mass blasts and paid wire releases stuffed with keyword links, which Google treats as link spam."),
            ("Does press coverage help SEO for a local business?",
             "It helps in three ways. News sites give you a trusted citation and referral visits, even when the link is nofollow. Stories tend to drive searches for your business name, which convert well. And AI search tools often cite local news when describing businesses. Keep a press page on your site, link each story, and watch branded searches in Search Console after each one runs."),
            ("Should I pay for a segment on a Houston morning TV show?",
             "It can be worth it if the audience fits and you treat it as advertising. Some Houston lifestyle shows run sponsored segments with a disclosure that the advertiser paid. Judge them like any ad buy: audience, cost, and a way to track response such as a unique URL or offer code. Don’t confuse a paid spot with earned news coverage, which reporters choose on merit."),
            ("How far ahead should I pitch Houston and The Woodlands media?",
             "In our experience, three to six weeks for monthly community papers, one to two weeks for daily papers, a few days for TV with a reminder the afternoon before, and three to six months for magazines. Pitch before noon on a weekday, avoid weeks when a storm or outage dominates the news, and follow up only once with something new."),
        ],
        "figures": {
            "map": {
                "type": "map",
                "title": "Community Impact editions around The Woodlands",
                "sub": "Neighboring editions mean neighboring audiences. Pitch the one your customers get.",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Montgomery", "Tomball", "Magnolia", "Katy", "Fulshear", "New Caney", "Porter"],
                "alt": "Map of Community Impact newspaper edition areas around The Woodlands and Houston for local press coverage",
                "caption": f"Edition areas taken from Community Impact’s own section names. Houston-wide figures from {SRC['ci_hou']}.",
            },
            "reach": {
                "type": "stats",
                "title": "Houston media, by the numbers",
                "stats": [["1.15M", "Houston mailboxes Community Impact reaches each month"], ["2.7M+", "monthly audience for Houston Public Media"], ["No. 8", "Houston’s TV market rank in 2022"], ["189", "Chronicle Top Workplaces named in 2024"]],
                "note": "Sources: Community Impact, University of Houston, Next TV, Top Workplaces",
                "alt": "Stats on Houston and The Woodlands media reach, including Community Impact mailboxes and Houston Public Media audience",
                "caption": "Reach is only useful when the audience matches your customers.",
            },
            "hooks": {
                "type": "checklist",
                "title": "News hooks that get Houston coverage",
                "sub": "If your pitch has none of these, wait for one",
                "items": ["Opening, move or expansion with date and address", "Hiring a specific number of local people", "Your own data on a local trend", "Expert help during a freeze or storm", "A milestone with a real person behind it", "Community project with a visible result", "An award the outlet itself runs", "A seasonal how-to tied to Houston weather"],
                "alt": "Checklist of news hooks that earn press coverage for businesses in Houston and The Woodlands",
                "caption": "Reporters cover events and information. Your business has to be part of one.",
            },
            "wants": {
                "type": "bars",
                "title": "What journalists say they want",
                "sub": "Share of journalists in two recent surveys",
                "items": [["Reject off-beat pitches", 86, "86%"], ["Prefer an email intro", 85, "85%"], ["Prefer pitches before noon", 78, "78%"], ["Value beat relevance most", 70, "70%"], ["Want under 200 words", 69, "69%"], ["Prefer 1:1 email pitches", 62, "62%"]],
                "highlight": [0],
                "note": "Sources: Cision 2025 State of the Media; Muck Rack State of Journalism 2026",
                "alt": "Bar chart of what journalists want from pitches, useful for getting press coverage in Houston and The Woodlands",
                "caption": f"Data from {SRC['cision']} and {SRC['muckrack']}.",
            },
            "pitch": {
                "type": "steps",
                "title": "Anatomy of a pitch that gets read",
                "sub": "About 100 words, no attachments",
                "steps": [["Subject line", "The news itself: what, where, when."], ["First sentence", "The fact a reader would repeat to a neighbor."], ["Why it matters here", "One line on what changes for that area."], ["Quick facts", "Address, date, hours, jobs, website."], ["The offer", "Who can talk today, and photos ready to use."]],
                "alt": "Five steps of an email pitch for local press coverage in Houston and The Woodlands",
                "caption": "Paste the release under your signature if you have one.",
            },
            "dont": {
                "type": "compare",
                "title": "Pitches that get deleted vs. answered",
                "left": {"title": "Deleted", "items": ["Same release blasted to 200 inboxes", "Big PDF attached", "Three paragraphs of company history", "Daily follow-ups", "Asks to approve the story first", "TV pitch with nothing to film"]},
                "right": {"title": "Answered", "items": ["One reporter, one outlet, on beat", "Facts pasted in the email", "News in the first sentence", "One follow-up with something new", "Spokesperson ready by phone", "A visual and a time to shoot it"]},
                "alt": "Comparison of press pitches that get ignored and pitches that earn coverage from Houston and The Woodlands media",
                "caption": "Every item on the left makes the reporter do more work.",
            },
            "seo": {
                "type": "funnel",
                "title": "How a news story turns into search demand",
                "stages": [["Story runs in a local outlet", "Day 0"], ["Readers search your name", "Days 0-14"], ["Profile views and site visits", "Days 0-30"], ["Calls, bookings, form fills", "Days 0-30"], ["Citations for SEO and AI answers", "Years"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how press coverage in Houston and The Woodlands drives brand searches, calls and SEO value",
                "caption": "Track branded searches in Search Console after each story to see the bump.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: chambers directory
    {
        "slug": "chambers-networking-groups-the-woodlands-houston",
        "title": "Chambers of Commerce and Networking Groups in The Woodlands and Houston: Costs and ROI Compared",
        "seo_title": "Chambers & Networking Groups in The Woodlands & Houston",
        "desc": "Published dues for The Woodlands, Conroe, Tomball, Houston Northwest, Asian and Greater Houston chambers, plus BNI, trade groups and how to judge ROI.",
        "category": "Local marketing",
        "icons": ["LinkedIn", "Google Business Profile", "HubSpot"],
        "art": "b4",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for chambers of commerce and networking groups in The Woodlands and Houston",
        "related": ["small-business-marketing-ideas-the-woodlands", "b2b-marketing-houston-energy-industrial", "measure-marketing-success-metrics"],
        "sections": [
            (None, f"""<p>$250. That’s the cheapest published chamber membership we found in Greater Houston, the Bronze level at the Asian Chamber of Commerce. The most expensive is $120,000 a year for an Executive Partner seat at the Greater Houston Partnership.</p>
<p>Somewhere between those numbers is a membership that will bring your business real customers. There are also plenty that will bring you a plaque, a directory listing nobody reads and a lanyard collection.</p>
<p>Below we put the published dues side by side for The Woodlands, Conroe, Tomball, northwest Houston and the citywide chambers, then cover BNI, industry associations, how to judge the return before you join and how to work a membership so the return actually shows up. Where a group doesn’t publish prices, we say so instead of guessing. Prices change every year, so confirm on the organization’s site before you budget.</p>"""),

            ("The directory: chambers in The Woodlands and Houston, with published dues", f"""<div class="bp-tbl"><table>
<thead><tr><th>Organization</th><th>Home turf and focus</th><th>Published entry level</th><th>Published top level</th><th>Worth knowing</th></tr></thead>
<tbody>
<tr><td>The Woodlands Area Chamber of Commerce</td><td>The Woodlands area</td><td>$500 Small Business</td><td>$15,000 Corporate Partners</td><td>$50 one-time enrollment fee; ad and event credits at most levels</td></tr>
<tr><td>Conroe/Lake Conroe Chamber of Commerce</td><td>Conroe, Lake Conroe, Montgomery</td><td>$500 Business</td><td>$5,000 Platinum</td><td>Nonprofits get 20% off; merged with the Montgomery Area Chamber in 2024</td></tr>
<tr><td>Greater Tomball Area Chamber of Commerce</td><td>Tomball area</td><td>$350 Primary Investor</td><td>$10,000 Elite Investor</td><td>Six levels in the 2025 guide</td></tr>
<tr><td>Houston Northwest Chamber of Commerce</td><td>Northwest Harris County</td><td>$400/year ($40/month) Engage</td><td>$10,000 Platinum Investor</td><td>Monthly billing and two-year new member rates in the May 2024 packet</td></tr>
<tr><td>Asian Chamber of Commerce (Houston)</td><td>Metro-wide, Asian American business community</td><td>$250 Bronze</td><td>$5,000 Titanium</td><td>Public companies with 250+ employees move to a corporate tier</td></tr>
<tr><td>Greater Houston Partnership</td><td>Metro-wide economic development and policy</td><td>$3,000 Limited Partner</td><td>$120,000 Executive Partner</td><td>Six levels in the 2026 guide</td></tr>
<tr><td>Houston Hispanic Chamber of Commerce</td><td>Metro-wide, Hispanic business community</td><td>Not published on its About page</td><td>Not published</td><td>Member application online; ask for current levels</td></tr>
<tr><td>Katy Area Chamber of Commerce</td><td>Katy area</td><td>Not verified</td><td>Not verified</td><td>Check the chamber’s current investment levels</td></tr>
<tr><td>Greater Houston Black Chamber, Greater Houston LGBT Chamber, Houston West Chamber</td><td>Metro-wide or west Houston communities</td><td>Not verified</td><td>Not verified</td><td>Listed by the City of Houston; ask each for dues</td></tr>
</tbody></table></div>
<p>Sources for every price above: {SRC['wacc']}, {SRC['clc']}, {SRC['tomball']}, {SRC['hnwcc']}, {SRC['acc']} and {SRC['ghp']}. The last three rows come from {SRC['hhcc']}, the {SRC['katy']} site and {SRC['coh']}.</p>
<!--fig:entry-->
<p>A note for Spring and Klein businesses: the Spring-Klein Chamber of Commerce told members it was in talks to merge into the Greater Tomball Area Chamber after losing members during the pandemic, as {SRC['skcc']}. If you’re in Spring today, the Houston Northwest, Tomball and Woodlands chambers are the ones to compare.</p>
<!--fig:map-->"""),

            ("The Woodlands Area Chamber: what each level buys", f"""<p>The Woodlands Area Chamber publishes more detail than most, which makes it easier to price. From {SRC['wacc']}:</p>
<ul>
<li><b>Small Business, $500.</b> Meant for micro businesses of ten or fewer employees, nonprofits and individuals. One location and category, one representative, a ribbon cutting at the Chamber office, a $100 advertising credit, one Networking Breakfast credit and a half-day of meeting room time each month.</li>
<li><b>Community, $1,000.</b> Up to two category listings and three representatives, a ribbon cutting within 12 miles, a $350 advertising credit and one membership mailing list.</li>
<li><b>Professional, $1,750.</b> Up to three listings and four representatives, a $550 advertising credit and two mailing lists.</li>
<li><b>Premier, $3,000.</b> Up to five listings and nine representatives, a $1,000 advertising credit, a $400 event sponsorship credit and verbal recognition at Business Connection Events.</li>
<li><b>Executive ($6,000), Signature ($9,000) and Corporate Partners ($15,000).</b> Larger credits, Executive Leadership Council access and, at Signature, a podcast interview.</li>
</ul>
<p>Two things we’d weigh. The number of representatives matters more than it looks, because a membership only produces business when people show up, and a sales team of four can cover four times the events. And the advertising credits are real money only if you would have bought chamber advertising anyway. If you wouldn’t, value them at zero when you do the math.</p>
<p>The ribbon cutting is underrated. It gives you photos, a reason to invite customers and neighbors, and a ready-made hook for {L(PR, 'a pitch to local media')}. Post the photos to your Google Business Profile the same day.</p>"""),

            ("Greater Houston Partnership: when $3,000 makes sense", f"""<p>The Partnership is a different animal. It acts as the region’s chamber and economic development group, and its 2026 guide prices membership at $3,000 (Limited Partner, one committee), $5,000, $10,000, $30,000, $60,000 and $120,000, per {SRC['ghp']}. Higher levels add committee access, briefings, board eligibility and executive programming.</p>
<p>Its small business page describes the Houston Business Exchange (HBX), a member program for small and mid-sized companies that want to build relationships with corporate and institutional decision-makers, plus Export Houston for businesses looking at international markets, per {SRC['ghp_smb']}.</p>
<p>Our view: it’s worth a hard look if you sell to big organizations, such as an engineering services firm, a commercial cleaning company or an industrial supplier chasing energy-sector accounts. Our {L('/blog/b2b-marketing-houston-energy-industrial/', 'B2B marketing guide for Houston energy and industrial companies')} covers the rest of that sales cycle. It’s a poor fit for a nail salon in Magnolia. Consumer businesses get more from a local chamber where the members are also their customers and neighbors.</p>"""),

            ("Identity chambers: Hispanic, Asian, Black and LGBT business groups", f"""<p>Houston has strong chambers built around communities, and for the right business they beat a geographic chamber easily.</p>
<p>{SRC['hhcc']} describes itself as “the leading regional advocate for the economic and civic interests of the Hispanic business community,” with seminars, networking, business panels, mentoring and an Emerging Leaders Institute. It doesn’t publish dues on its About page, so ask.</p>
<p>The Asian Chamber of Commerce does publish them: Bronze $250, Silver $500, Gold $1,000, Diamond $1,500, Platinum $3,000 and Titanium $5,000, per {SRC['acc']}. The useful detail is in the benefits grid. Every tier gets seats in the Supplier Development Academy, Gold and above get email marketing to the chamber’s network, and Diamond and above get exhibitor tables at selected events and at the Business Expo. If supplier diversity programs matter to your sales, those lines are worth more than the luncheon tickets.</p>
<p>The City of Houston also lists the Greater Houston Black Chamber, the Greater Houston LGBT Chamber and the Houston West Chamber among the region’s chambers, per {SRC['coh']}. Pricing wasn’t on the pages we could check, so call.</p>
<p>If your customers are mostly Spanish-speaking, membership pairs well with the work in our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing guide')}.</p>"""),

            ("North and west: Conroe, Montgomery, Tomball, northwest Houston and Katy", f"""<p>The Conroe/Lake Conroe Chamber lists Business ($500), Gold ($1,000), Ruby ($1,225), Sapphire ($1,825), Emerald ($3,000) and Platinum ($5,000), with 20% off any level for nonprofits, per {SRC['clc']}. In March 2024 the Montgomery Area Chamber, with about 240 members (roughly 30% of whom already belonged to both), merged into it, as {SRC['merge']}. For a business in Montgomery, Willis or around the lake, that consolidation means one room to work instead of two.</p>
<p>The Greater Tomball Area Chamber’s 2025 guide runs from Primary Investor ($350) through Principal ($650), Classic ($1,000), President’s Club ($2,500), Chairman’s Circle ($5,000) and Elite ($10,000), per {SRC['tomball']}.</p>
<p>The Houston Northwest Chamber’s May 2024 packet offered monthly billing: Engage at $40 a month or $400 a year, Business Builder at $800, Business Developer at $1,200, then investor levels at $3,200, $6,000 and $10,000, with discounted two-year rates for new members at the lower tiers, per {SRC['hnwcc']}. Check for a newer packet before you join.</p>
<p>Katy and Fulshear businesses should look at the {SRC['katy']}. We couldn’t verify its current price list, so we left it blank above. Our notes on {L('/blog/marketing-your-business-katy-cypress-tx/', 'marketing in Katy and Cypress')} and {L('/blog/reaching-customers-conroe-montgomery/', 'reaching customers in Conroe and Montgomery')} cover the rest of the local picture.</p>"""),

            ("BNI and referral groups", f"""<p>A chamber is a big room with loose ties. A referral group is a small room with an obligation. BNI is the largest of them: founded by Ivan Misner in 1985, it reports 355,000 members in 11,800 chapters, 17.8 million referrals and $26.9 billion in member-generated business, per {SRC['bni']}. Each chapter allows {SRC['bni1']}, so the electrician in your chapter is the only electrician there.</p>
<!--fig:bni-->
<p>Chapters keep opening around here. Community Impact reported in June 2026 on {SRC['bnici']} in east Montgomery County. Chapters meet across the Houston area, and most meet weekly, so visit the one closest to your customers before you commit to a year of mornings.</p>
<p>BNI doesn’t publish one national price. Fees are set at the chapter and region level, so ask the chapter’s director for three numbers before you visit twice: the annual membership fee, any one-time application fee, and the weekly meeting or meal cost. Multiply that last one by about 50 weeks. It often matters more than the membership fee.</p>
<!--fig:compare-->
<p>Referral groups work best for trades and professional services that refer each other naturally: a realtor, a lender, a title company, an inspector, a roofer, an insurance agent. They work poorly for businesses that need volume from strangers, like a restaurant or a retail shop.</p>"""),

            ("Industry associations often beat chambers", f"""<p>If your customers are other businesses in one industry, go where that industry meets. The {SRC['ghba']} describes itself as the place “where Houston’s residential construction industry comes together.” For a cabinet maker, a pool builder, a title company or a marketing firm selling to builders, a GHBA luncheon is a room full of buyers. A general chamber mixer is a room full of other sellers. GHBA doesn’t publish dues on its membership page, though it offers guests a first luncheon or education course.</p>
<p>The same logic applies to dental and medical societies for anyone who sells to practices, property management associations for contractors, and HR or finance groups for B2B service firms. Look for the Houston chapter of the national association your customers belong to, then go as a guest before you join.</p>"""),

            ("How to evaluate chamber ROI before you write the check", f"""<p>Start with total cost, not dues. Then work out how many customers you’d need to break even, and ask whether that’s believable.</p>
<!--fig:questions-->
<p>Here’s a worked example. The numbers are illustrative, not a benchmark.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line</th><th>Example</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Dues</td><td>$1,000</td><td>A mid-level local chamber membership</td></tr>
<tr><td>Events and lunches</td><td>$600</td><td>Two paid events a month at about $25</td></tr>
<tr><td>Owner time</td><td>$3,600</td><td>4 hours a month, 12 months, valued at $75 an hour</td></tr>
<tr><td><b>Total yearly cost</b></td><td><b>$5,200</b></td><td>Most owners only count the first line</td></tr>
<tr><td>Gross profit per new client (first year)</td><td>$1,300</td><td>Revenue minus direct costs</td></tr>
<tr><td><b>Clients to break even</b></td><td><b>4</b></td><td>$5,200 ÷ $1,300</td></tr>
</tbody></table></div>
<p>Four clients a year from a room you visit twice a month is realistic for a lot of service businesses. Fourteen wouldn’t be. If the math needs more clients than you can picture, pick a cheaper level, a different group, or skip it.</p>
<!--fig:roi-->
<p>Then track it. Add “Chamber” and “BNI” as lead sources in your CRM, ask every new client how they found you, and review it at renewal. Our guide to {L('/blog/measure-marketing-success-metrics/', 'measuring marketing success')} covers how to set up that tracking.</p>"""),

            ("How to work a membership so it pays", f"""<p>The members who say their chamber is worthless usually attended three mixers and waited. The ones who get business treat it like a part-time job with a short list of habits.</p>
<!--fig:work-->
<p>A few specifics. Volunteer for the ambassador team or one committee, because the people who run events meet everyone. Bring a referral before you ask for one. Follow up within two days with something useful, not a brochure. Our {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed-to-lead guide')} applies to handshakes as much as web forms. And fill out your directory listing completely, with your website, hours and categories. A chamber directory listing is a legitimate local citation that helps Google confirm your business details, which supports your {L('/blog/rank-in-google-map-pack-houston/', 'map pack rankings')}. It won’t rank you by itself.</p>"""),

            ("A quick tax note on dues", f"""<p>Dues to a business league such as a chamber are generally deductible as a business expense, except the share the organization tells you goes to lobbying or political activity. Under sections 162(e) and 6033(e), chambers that lobby must notify members of that nondeductible share when dues are paid, or pay a proxy tax instead, per {SRC['irsdues']}. Look for that percentage on your invoice and hand it to your CPA. This is general information, not tax advice.</p>
<p>If you want help deciding which rooms fit your sales goals and how they connect to the rest of your marketing, <a href="/contact/">get in touch</a> and a senior strategist will build a plan around your business. We also cover {L(SPONSOR, 'the ROI of local sponsorships')}, which often come bundled with chamber events.</p>"""),
        ],
        "faq": [
            ("How much does it cost to join The Woodlands Area Chamber of Commerce?",
             "The Woodlands Area Chamber publishes levels starting at $500 a year for its Small Business membership, meant for businesses with ten or fewer employees, nonprofits and individuals. Community is $1,000, Professional $1,750 and Premier $3,000, with higher levels up to $15,000. There is a one-time $50 enrollment fee. Check the chamber’s join page for current prices and what each level includes."),
            ("Is the Greater Houston Partnership worth it for a small business?",
             "It depends on who you sell to. The Partnership’s 2026 guide starts at $3,000 a year, and its programs focus on regional economic development, policy and access to corporate and institutional decision-makers. It can pay off for B2B firms selling to large companies. Consumer businesses in The Woodlands, Conroe or Katy usually get more from a local chamber where members are also customers."),
            ("Chamber of commerce or BNI: which brings more business in Houston?",
             "They do different jobs. A chamber gives you a wide local network, visibility and events, with loose obligations. BNI is a weekly referral group with one member per specialty and an expectation that members pass referrals. Trades and professional services that refer each other often do better in BNI. Businesses that want broad local visibility and B2B contacts usually prefer a chamber."),
            ("Are chamber of commerce dues tax deductible?",
             "Generally, dues paid to a chamber of commerce are deductible as an ordinary business expense, except for any portion the chamber reports as going to lobbying or political activity. Chambers that lobby must tell members that nondeductible percentage when dues are paid. Look for it on your invoice and confirm the treatment with your CPA. This is general information, not tax advice."),
            ("Which chamber should a Spring or Conroe business join?",
             "In Spring, compare the Houston Northwest Chamber, the Greater Tomball Area Chamber and The Woodlands Area Chamber, since the old Spring-Klein Chamber announced merger talks with Tomball in 2021. In Conroe, Montgomery or around Lake Conroe, the Conroe/Lake Conroe Chamber absorbed the Montgomery Area Chamber in 2024. Visit two events as a guest before joining, and pick the room where your customers are."),
        ],
        "figures": {
            "entry": {
                "type": "bars",
                "title": "Cheapest published chamber membership",
                "sub": "Entry-level annual dues, Houston and The Woodlands area",
                "items": [["Asian Chamber (Bronze)", 250, "$250"], ["Greater Tomball (Primary)", 350, "$350"], ["Houston Northwest (Engage)", 400, "$400"], ["Woodlands Area (Small Business)", 500, "$500"], ["Conroe/Lake Conroe (Business)", 500, "$500"], ["Greater Houston Partnership", 3000, "$3,000"]],
                "highlight": [3],
                "note": "Published prices; Woodlands adds a $50 one-time fee. Houston Northwest figure from its May 2024 packet.",
                "alt": "Bar chart of entry-level chamber of commerce dues in The Woodlands, Conroe, Tomball and Houston",
                "caption": "Confirm current prices before you budget. They change yearly.",
            },
            "map": {
                "type": "map",
                "title": "Where each chamber’s members are",
                "sub": "Home turf of the local chambers in this directory",
                "highlight": ["The Woodlands", "Conroe", "Montgomery", "Tomball", "Spring", "Cypress", "Katy", "Fulshear"],
                "alt": "Map of chamber of commerce territories around The Woodlands, Conroe, Tomball, Spring and Katy in Greater Houston",
                "caption": "Pick the chamber whose members are your customers, not the one closest to your office.",
            },
            "bni": {
                "type": "stats",
                "title": "BNI at a glance",
                "stats": [["355K", "members worldwide"], ["11.8K", "chapters"], ["1985", "year founded"], ["$26.9B", "member-generated business BNI reports"]],
                "note": "Source: BNI About page",
                "alt": "Stats on BNI referral networking chapters relevant to businesses in The Woodlands and Houston",
                "caption": f"Figures as reported on {SRC['bni']}.",
            },
            "compare": {
                "type": "compare",
                "title": "Chamber vs. referral group",
                "left": {"title": "Chamber of commerce", "items": ["Big rooms, loose ties", "Monthly events, attend when you can", "Many members in your category", "Visibility, ribbon cutting, directory", "Good for B2B and community presence"]},
                "right": {"title": "Referral group (BNI-style)", "items": ["Small room, weekly meetings", "Attendance expected", "One member per specialty", "Referrals passed on purpose", "Good for trades and pro services"]},
                "alt": "Comparison of a chamber of commerce and a BNI referral group for businesses in The Woodlands and Houston",
                "caption": "Plenty of owners do one of each. Few have time for three.",
            },
            "questions": {
                "type": "checklist",
                "title": "Ask before you join any group",
                "sub": "Get answers in writing or from two current members",
                "items": ["Who are the members, by industry?", "How many show up to a typical event?", "How many reps does my level include?", "What does a year cost with events and meals?", "Are ad credits worth anything to me?", "Can I visit twice as a guest first?", "Who in my category already belongs?", "What did members in my field get last year?"],
                "alt": "Checklist of questions to ask before joining a chamber or networking group in The Woodlands or Houston",
                "caption": "If nobody can tell you who shows up, that’s your answer.",
            },
            "roi": {
                "type": "funnel",
                "title": "A year of chamber networking",
                "stages": [["Events attended", "24"], ["Real conversations", "120"], ["Follow-up meetings", "18"], ["Proposals sent", "7"], ["New clients", "4"]],
                "note": "Illustrative example",
                "alt": "Funnel of chamber of commerce networking results from events to new clients for a business in The Woodlands",
                "caption": "Four clients covers the example’s $5,200 total cost at $1,300 each.",
            },
            "work": {
                "type": "steps",
                "title": "Working a membership: first 90 days",
                "sub": "What the members who get business actually do",
                "steps": [["Pick one recurring event", "Same breakfast every month, so faces repeat."], ["Join one committee", "Ambassadors and event teams meet everyone."], ["Give first", "Bring a referral or intro before asking."], ["Follow up in 48 hours", "Something useful, not a brochure."], ["Track it", "Chamber as a lead source in your CRM."]],
                "alt": "Five steps to get business from a chamber of commerce membership in The Woodlands and Houston",
                "caption": "Review the CRM numbers at renewal, then decide.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: sponsorship ROI
    {
        "slug": "local-sponsorships-youth-sports-the-woodlands-houston",
        "title": "Local Sponsorships and Youth Sports in The Woodlands and Houston: What They’re Worth",
        "seo_title": "Youth Sports & Local Sponsorship ROI: The Woodlands, Houston",
        "desc": "Real sponsorship prices in The Woodlands and Houston, a break-even calculator, QR and promo code tracking, when sponsorships beat ads, and tax basics.",
        "category": "Strategy",
        "icons": ["Google Analytics", "Facebook", "Instagram"],
        "art": "b6",
        "hero": "receipt",
        "hero_alt": "Illustration of a receipt for local sponsorship and youth sports ROI in The Woodlands and Houston",
        "related": ["billboard-advertising-cost-houston", "call-tracking-which-ads-make-phone-ring", "set-a-marketing-budget-small-business"],
        "sections": [
            (None, f"""<p>Myth: you can’t measure a sponsorship.</p>
<p>We hear it from owners defending a $3,000 outfield banner and from owners refusing to buy one. Both are wrong for the same reason. Nobody set the sponsorship up to be measured, so of course nobody could measure it.</p>
<p>A sponsorship is an ad you buy from a nonprofit. It has a price, an audience, a placement and, if you plan it, a way to count responses. Some of the best-performing local marketing we see in The Woodlands and Houston is a well-chosen youth league or booster club sponsorship. Some of the worst is a gala table bought because a client asked.</p>
<p>This guide lists real sponsorship prices from around the area, walks through a break-even calculator with worked examples, shows how to track a banner with QR codes, unique URLs, call tracking numbers and promo codes, and covers the tax basics. That last part is general information, not tax advice.</p>"""),

            ("What sponsorships cost around The Woodlands and Houston", f"""<p>Most organizations don’t publish prices, but enough do to give you a feel for the market.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Organization</th><th>Published price range</th><th>What’s included (highlights)</th></tr></thead>
<tbody>
<tr><td>The Woodlands Township Adult Sports (soccer and pickleball)</td><td>$250 banner package to $15,000 presenting partner</td><td>Banners, armbands, T-shirts, trophy or medal presenting rights; top tier adds emails, tabling and category protection</td></tr>
<tr><td>Clear Springs Baseball Booster Club (League City)</td><td>$500 to $2,000</td><td>At $1,000: ballpark signage, media guide ad, home-game announcement, logo on the team page, social posts, golf hole sponsorship</td></tr>
<tr><td>Woodlands Lacrosse</td><td>$500 to $5,000+</td><td>Gift cards at lower levels; larger amounts offset a player’s season or spring break fees</td></tr>
<tr><td>YES to YOUTH Gala (Woodlands Waterway Marriott, Aug. 8, 2026)</td><td>$5,000 to $50,000; underwriting from $1,500</td><td>Tables, program ads, on-screen recognition; a general table was $3,500</td></tr>
<tr><td>Woodlands Online Sports (high school broadcasts)</td><td>Price on request</td><td>Spots in live game streams and shows, site ads, social posts</td></tr>
<tr><td>Township and Waterway events (Red, Hot &amp; Blue, Waterway Arts Festival)</td><td>Not published</td><td>Event and site sponsorships; ask the organizer</td></tr>
</tbody></table></div>
<p>Sources: {SRC['twpsports']}, {SRC['csbb']}, {SRC['lax']}, {SRC['yes']} and {SRC['wol']}.</p>
<!--fig:prices-->
<p>Some details worth knowing. The Township’s adult sports program says its leagues and tournaments welcome more than 4,800 participants a year, and it offers 15% off a two-year commitment and 10% off renewals. The Clear Springs booster club lists its 501(c)(3) status and tax ID on its form, which you want from any group you sponsor. And Woodlands Lacrosse ties sponsorship to fee waivers: $5,000 or more waives the base spring membership fee, listed at $2,250 per player, for one player per family. That is a sponsorship that benefits your own household, which matters for taxes (more on that below).</p>"""),

            ("The Woodlands community events: the Waterway, Town Green Park and July 4th", f"""<p>The big community events draw crowds a youth league can’t, at prices to match.</p>
<p>The Township’s 2026 Red, Hot &amp; Blue Festival ran on July 4 across five sites: Town Green Park, Northshore Park, Waterway Square, Hughes Landing and Rob Fleming Park (fireworks only). Repsol was listed as the festival’s official sponsor and Renewal by Andersen sponsored the Town Green Park location, per {SRC['rhb']}. Notice the pattern. Site-level sponsorships exist below the headline sponsor, and they are often the realistic entry point for a local company.</p>
<p>The Woodlands Waterway Arts Festival, run by The Woodlands Arts Council at Town Green Park, brings in about 200 artists and has returned $1.4 million to the community through arts scholarships for Montgomery County high school students and microgrants for teachers, according to {SRC['wwaf']}. {SRC['fidelity']} has announced Fidelity Investments as its returning title sponsor. A festival like that suits businesses whose customers skew toward homeowners with disposable income: interior designers, remodelers, financial advisors, galleries, restaurants on the Waterway.</p>
<p>Event sponsorships are worth the most when you can do something on site. A booth where people can book, sample or enter a drawing is a lead source. A logo on a step-and-repeat is a picture.</p>"""),

            ("What you actually get, line by line", f"""<p>Sponsorship packets list benefits. Your job is to price each one as if you were buying it on its own.</p>
<ul>
<li><b>Signage.</b> Count the people who will see it and how often. A banner at a home field is seen by the same few hundred families every weekend for a season, which is great for frequency and limited for reach. That makes it a good fit for businesses that sell to families in one school zone.</li>
<li><b>A website link.</b> Useful for referral visits and as a local citation. Not a ranking play. {SRC['gspam']} allow sponsored links as long as they carry a rel="sponsored" or rel="nofollow" attribute, and treat buying links for rankings as spam.</li>
<li><b>Social posts.</b> Ask how many followers the account has and how many likes a typical sponsor post gets. A team account with 400 engaged parents can beat a business page with 4,000 strangers.</li>
<li><b>PA announcements and program ads.</b> Low cost, low attention. Make them specific (your name, “two blocks from the field,” Saturday hours) or skip them.</li>
<li><b>Tables, booths and sampling.</b> Often the most valuable line in the packet, because it creates conversations. The Township’s presenting partner package lists tabling, giveaways and sweepstakes opportunities.</li>
<li><b>Category protection.</b> Being the only dentist or the only realtor on the fence is worth paying extra for.</li>
<li><b>Tickets and tables.</b> Only valuable if you’ll fill the seats with customers or prospects.</li>
</ul>
<!--fig:activate-->
<p>Local leagues are flexible. {SRC['ll']} describes leagues offering fence signs, scoreboard signage, website listings and Opening Day presence for larger donors. If the packet doesn’t include what you want, ask. A first pitch, a table at registration day or a mention in the league’s season email often costs the league nothing.</p>"""),

            ("The worked calculator: what a sponsorship has to return", f"""<p>Every sponsorship decision comes down to one number: how many new customers you need to break even. The formula fits on a sticky note.</p>
<p><b>Break-even customers = total cost ÷ (gross profit per customer × expected purchases per customer)</b></p>
<p>Total cost includes the sponsorship, the banner or printing, any giveaways and the staff time to show up. Gross profit is revenue minus the direct cost of delivering the service. Expected purchases is how many times a typical new customer buys from you in the period you care about (we use two years for most local businesses).</p>
<p>Three worked examples. The businesses are hypothetical and the numbers are illustrative.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Scenario</th><th>Total cost</th><th>Gross profit per purchase</th><th>Purchases in 2 years</th><th>Break-even customers</th></tr></thead>
<tbody>
<tr><td>Family dental office in Spring sponsors a youth baseball booster package, plus a QR sign</td><td>$1,150</td><td>$250</td><td>4 visits</td><td><b>1.2</b></td></tr>
<tr><td>Financial advisor in The Woodlands buys a $5,000 gala table and fills it with prospects</td><td>$5,000</td><td>$2,500 a year</td><td>2 years</td><td><b>1.0</b></td></tr>
<tr><td>Outpatient clinic takes a $15,000 presenting partnership in a large adult sports program</td><td>$16,500</td><td>$450 per patient episode</td><td>1.2 episodes</td><td><b>30.6</b></td></tr>
</tbody></table></div>
<!--fig:breakeven-->
<p>The first two are easy calls if the audience fits. One or two new patients or clients and you’ve paid for it. The third needs about 31 new patients from a sports program, which is possible but only with real activation: a booth at tournaments, a free screening offer and an email to participants. A presenting partnership with only a logo would be a bet, not a plan.</p>
<p>Now compare that to search ads. If your {L('/blog/understanding-cost-per-lead/', 'cost per lead')} on Google is $80 and one in four leads becomes a customer, a customer costs you $320 in ads. The dental sponsorship needs to bring in about four customers to beat that ($1,150 ÷ $320). That’s the test we run for clients: what does a sponsored customer cost compared with the next best channel? Our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston cost-per-click benchmarks')} help fill in your side of that comparison.</p>"""),

            ("How to track a sponsorship", f"""<p>Tracking a banner takes about an hour of setup. Skip it and you’ll be guessing at renewal time.</p>
<!--fig:track-->
<p><b>Unique URL.</b> Make a short page on your site that only the sponsorship uses, like yoursite.com/chargers, with an offer for team families. Print it on the banner. Every visit to that page came from the sponsorship.</p>
<p><b>QR code with UTM tags.</b> Point the QR code at the same page with campaign tags. {SRC['utm']} says to always use utm_source, utm_medium and utm_campaign, so a booster banner might use source clear-springs-baseball, medium sponsorship and campaign spring-2027. Then GA4 reports those visits separately from everything else.</p>
<p><b>A dedicated phone number.</b> A call tracking number on the sign and in the program shows you every call it produced. Our {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers setup, and {L('/blog/track-form-submissions-phone-calls-ga4-google-ads/', 'tracking forms and calls in GA4')} covers the reporting.</p>
<p><b>Promo code.</b> “CHARGERS15” at checkout or on the phone. Give it an end date, so you can see when it was used.</p>
<p><b>Ask.</b> Add a required “How did you hear about us?” field to your booking form, with the sponsorship as an option. People forget QR codes; they remember the field.</p>
<p>Expect the methods to overlap and undercount. Plenty of families will see the banner for a season and then just search your name. Watch for that too: compare branded searches and calls from nearby ZIP codes during the season with the same weeks a year earlier.</p>
<!--fig:methods-->"""),

            ("When a sponsorship beats ads, and when it doesn’t", f"""<p>Sponsorships win when the audience is concentrated, trust matters and you can show up. They lose when you need volume this week.</p>
<!--fig:when-->
<p>Two Houston-specific notes. School zones drive a lot of family decisions here, so a sponsorship tied to one high school feeder pattern in Conroe ISD or Klein ISD reaches exactly the households a pediatric dentist, orthodontist, tutoring center or realtor wants. And Houston families spread out. If your customers drive in from Katy, Pearland and Kingwood, a single neighborhood league won’t reach most of them, and search or {L('/blog/facebook-instagram-ads-local-businesses/', 'Facebook and Instagram ads')} will do better per dollar.</p>
<p>We like sponsorships most as part of a mix: a season-long banner with a QR code, paired with geo-targeted social ads to the same parents and a review push from the families who become customers. If you’re working out how much to spend overall, our guide to {L('/blog/set-a-marketing-budget-small-business/', 'setting a marketing budget')} helps.</p>"""),

            ("Tax basics: advertising, charitable contribution or neither", f"""<p>This section is general information, not tax advice. Talk to your CPA before you decide how to treat any payment.</p>
<p><b>As advertising.</b> The IRS says advertising and marketing costs are deductible when they are ordinary and necessary, and that goodwill advertising that keeps your name before the public is generally deductible when it relates to a reasonable expectation of future business, per {SRC['irsad']}. Many local business sponsorships are treated this way.</p>
<p><b>The nonprofit’s side.</b> For the charity, the IRS separates a “qualified sponsorship payment” from advertising income. An acknowledgment may include your logo, slogans without qualitative or comparative descriptions, your locations, phone number and website address (even as a hyperlink), and value-neutral descriptions of your products. Messages with qualitative or comparative language, price information, endorsements or inducements to buy count as advertising, per {SRC['fr513']}. That’s mostly the nonprofit’s concern, but it explains why some groups will happily print your name, phone number and web address but balk at “Best dentist in Spring, half-price cleanings.”</p>
<p><b>As a charitable contribution.</b> If you receive something of value, you can generally deduct only the amount over that value, per {SRC['p526']}, which covers individuals. Gala tables are the classic case, because the dinner has a value. Starting with tax years after December 31, 2025, corporate charitable deductions also face a new 1% of taxable income floor alongside the 10% cap, under the 2025 tax law, per {SRC['gt']}.</p>
<p><b>When it benefits your family.</b> If a sponsorship waives your own child’s fees, as some team programs offer, you’re receiving a personal benefit. Ask your CPA how that changes things before you write the check.</p>
<!--fig:map-->"""),

            ("A season plan for your next sponsorship", f"""<ol>
<li><b>Before you sign.</b> Ask for the audience numbers, the follower counts and the event calendar. Negotiate one activation (a table, a first pitch, a season email mention) and category exclusivity. Get the group’s 501(c)(3) letter or tax ID.</li>
<li><b>Two weeks out.</b> Build the unique landing page, the QR code with UTM tags, the call tracking number and the promo code. Approve banner art that a parent can read from the bleachers: name, one benefit, URL.</li>
<li><b>During the season.</b> Show up at least twice. Post the team’s wins from your own accounts. Send a thank-you to families who become customers and ask for a Google review.</li>
<li><b>At renewal.</b> Count visits, calls, codes and “how did you hear” answers. Divide total cost by new customers. Compare it with your cost per customer from ads. Renew, renegotiate or walk.</li>
</ol>
<p>If you want a strategist to run the numbers on a sponsorship you’re weighing and fit it into the rest of your plan, <a href="/contact/">get in touch</a>. And if the sponsorship comes with a chamber event or a press angle, our {L(CHAMBERS, 'chamber directory')} and {L(PR, 'local PR playbook')} cover those pieces.</p>"""),
        ],
        "faq": [
            ("How much does it cost to sponsor a youth sports team in The Woodlands or Houston?",
             "Published prices we found range widely. A Houston-area high school baseball booster club lists packages from $500 to $2,000, The Woodlands Township’s adult sports program starts at $250 for a banner package and goes to $15,000, and gala sponsorships in The Woodlands run $5,000 to $50,000. Neighborhood leagues are often cheaper. Ask for audience numbers and an activation before you pay."),
            ("Is a sponsorship tax deductible as advertising or a charitable donation?",
             "Often it can be treated as advertising if it is an ordinary and necessary business expense, and the IRS says goodwill advertising that keeps your name before the public is generally deductible. If you treat it as a charitable gift, you generally deduct only the amount above the value you receive, like a gala dinner. Rules differ for corporations and individuals. Ask your CPA; this is not tax advice."),
            ("How do I track ROI from a local sponsorship?",
             "Give the sponsorship its own landing page and short URL, a QR code tagged with utm_source, utm_medium and utm_campaign, a dedicated call tracking number and a promo code with an end date. Add a required how-did-you-hear field to your booking form. At renewal, divide the total cost by the new customers you can attribute and compare that with your cost per customer from ads."),
            ("Are sponsorships better than Facebook ads for a Houston business?",
             "Sometimes. Sponsorships tend to win when your customers are concentrated in one school zone or neighborhood, trust matters, and you can show up in person. Ads usually win when you need leads quickly or your customers are spread across Houston. Many local businesses do best with both: a season-long sponsorship plus targeted social ads to the same families."),
            ("Do sponsorship backlinks help SEO?",
             "Not much for rankings. Google allows sponsored links as long as they are marked rel=sponsored or nofollow, and it treats buying links for ranking purposes as spam. A link from a local league or charity still helps with referral visits and as a local citation that confirms your business details. Sponsor for the audience and treat the link as a small bonus."),
        ],
        "figures": {
            "prices": {
                "type": "bars",
                "title": "Published sponsorship price points",
                "sub": "Examples from The Woodlands and the Houston area",
                "items": [["Township sports banner package", 250, "$250"], ["Booster club entry tier", 500, "$500"], ["Booster club top tier", 2000, "$2,000"], ["Gala table and quarter-page ad", 5000, "$5,000"], ["Trophy presenting rights", 5000, "$5,000"], ["Adult sports presenting partner", 15000, "$15,000"]],
                "highlight": [1],
                "note": "Sources: Woodlands Township, Clear Springs Baseball Booster Club, YES to YOUTH",
                "alt": "Bar chart of published local sponsorship prices for youth sports and events in The Woodlands and Houston",
                "caption": "Neighborhood leagues and booster clubs are the realistic entry point for most local businesses.",
            },
            "activate": {
                "type": "compare",
                "title": "Logo-only vs. activated sponsorship",
                "left": {"title": "Logo only", "items": ["Logo on a banner", "Name in the program", "Link with no landing page", "No reason to act now", "Nobody from your team attends"]},
                "right": {"title": "Activated", "items": ["Name, one benefit and a short URL", "QR code to a team-family offer", "Dedicated phone number and code", "Table on registration day", "Owner at two games, photos shared"]},
                "alt": "Comparison of a logo-only sponsorship and an activated youth sports sponsorship in The Woodlands and Houston",
                "caption": "Same price, very different results.",
            },
            "breakeven": {
                "type": "stats",
                "title": "Break-even customers, three examples",
                "stats": [["1.2", "patients for a $1,150 youth baseball package"], ["1.0", "client for a $5,000 gala table"], ["30.6", "patients for a $16,500 presenting deal"]],
                "note": "Illustrative example",
                "alt": "Stats showing break-even customers for local sponsorships in The Woodlands and Houston",
                "caption": "Total cost ÷ (gross profit per purchase × purchases in two years).",
            },
            "track": {
                "type": "steps",
                "title": "Tracking a sponsorship from banner to booking",
                "sub": "About an hour of setup per sponsorship",
                "steps": [["Unique landing page", "A short URL only the sponsorship uses."], ["QR code with UTMs", "Source, medium and campaign on every scan."], ["Dedicated number", "Call tracking on the sign and program."], ["Promo code", "Team-specific, with an end date."], ["Ask every customer", "Required how-did-you-hear field."], ["Compare at renewal", "Cost per customer vs. your ads."]],
                "alt": "Six steps to track youth sports and local sponsorship ROI for businesses in The Woodlands and Houston",
                "caption": "Each method undercounts. Together they give you a usable number.",
            },
            "methods": {
                "type": "columns",
                "title": "Where tracked responses came from",
                "sub": "One season of a single banner sponsorship",
                "labels": ["QR scans", "Short URL", "Call number", "Promo code", "Asked"],
                "values": [34, 12, 18, 14, 22],
                "highlight": [0],
                "y_label": "% of tracked",
                "note": "Illustrative example",
                "alt": "Column chart of how sponsorship responses were tracked for a local business in The Woodlands and Houston",
                "caption": "Use several methods. No single one catches everyone.",
            },
            "when": {
                "type": "checklist",
                "title": "Signs a sponsorship will beat ads",
                "sub": "The more boxes you check, the better the bet",
                "items": ["Your customers live in one school zone", "Trust matters more than price", "Customers buy more than once", "You or your staff will show up", "The group allows a table or sampling", "You can get category exclusivity", "You’ll commit for two or more seasons", "You can track it with a URL or code"],
                "alt": "Checklist for deciding whether a local sponsorship beats paid ads for a business in The Woodlands or Houston",
                "caption": "Check fewer than four and put the money into search or social instead.",
            },
            "map": {
                "type": "map",
                "title": "Sponsorship examples in this guide",
                "sub": "Where the published price lists and events are",
                "highlight": ["The Woodlands", "League City", "Willis", "Conroe", "Spring"],
                "alt": "Map of youth sports and community event sponsorship examples in The Woodlands, Conroe, Willis and League City near Houston",
                "caption": "Township sports and Waterway events in The Woodlands, a booster club in League City, school broadcasts covering Willis and Conroe.",
            },
        },
    },
]
