"""Batch 17 (module e): a data-built community guide to marketing to Houston's Asian American communities, a Q&A
roundup of the marketing questions Houston and The Woodlands owners ask most, and an A-Z digital marketing glossary.

Research, Asian American guide: Rice University Kinder Institute, Jan 12, 2026 (655,000+ Asian residents in the
region, share up from 1.8% to 9.9% over about four decades, Asian Indians the largest group at 150,000+, Fort Bend
+117% and Montgomery County +180% from 2010 to 2023, 2,100-person survey, 46% of households over $100K); ABC13 on the
same study (Jan 14, 2026); Asian Chamber of Commerce Houston stats page (713,430 Asian residents, 9.5% in 2023; 2023
subgroup counts: Asian Indian 167,084, Vietnamese 158,957, Chinese 122,546, Filipino 78,540, Pakistani 50,887,
Korean 28,045); City of Houston "Top 25 Houston Languages 2021" (2021 ACS 1-year, city limits: Vietnamese 29,060,
Chinese 27,838, Hindi 10,936, Tagalog 6,433, Urdu 6,230, Telugu 4,676, Gujarati 4,357, Korean 3,760, Tamil 2,851);
Community Impact, Sept 2021 (Fort Bend 22.2% Asian in 2020, Katy Asian Town opened 2018, Katy ISD Asian enrollment
11.1% to 16.1%); Community Impact, May 2017 (Katy Asian Town, H Mart anchor); Southwest Management District on the
Mahatma Gandhi District (Hillcroft and Harwin, named Jan 16, 2010) and Chinatown; Houston Landing, Apr 2025 (Little
Saigon beside Chinatown, South Vietnamese flag, Black April); ABC13 on Radio Saigon Houston (May 2021) and on Voice
of Asia (founded 1987, Koshy Thomas); VOA on Southern News Group (Wea Lee, ITV); scdaily.com (Houston yellow pages);
Pew Research Center fact sheet on Vietnamese Americans (56% English proficient, 36% of immigrants) and key facts
about Asian Americans (74% English proficient, May 2025); Sinch, Nov 2025 (WeChat, KakaoTalk, Zalo, WhatsApp,
Messenger, LINE by country); Tuoi Tre, Dec 2025 (Zalo 79.2M MAU, Q3 2025); Search Engine Land on Meta's Jan 19, 2022
removal of sensitive detailed targeting; Meta multi-language ads docs; Google Ads language targeting page (Sept 2026
change); Google multilingual sites guidance; Royal Museums Greenwich (Lunar New Year Sat Feb 6, 2027, Year of the
Goat); Bao Nghe An lunar calendar (Tet Dinh Mui on Feb 6, 2027); Office Holidays (Holi Mar 22-23, 2027; Mid-Autumn
Sept 15, 2027; Diwali Fri Oct 29, 2027).
Q&A and glossary: WordStream/LocaliQ 2026 Google Ads benchmarks (all-industry $5.42 CPC, 8.18% CVR, $66.69 CPL; legal
$9.87/$131.63; business services $5.87/$93.69; home $8.33/$90.92; dental $8.00/$72.97; personal services
$7.17/$54.60); BrightLocal 2026 Local Consumer Review Survey (97% read reviews, 74% only last three months, 47% won't
use a business with fewer than 20, 31% only 4.5+, 45% use AI tools for local recommendations); Google SEO Starter
Guide ("a few hours ... several months", "wait a few weeks"); Google local ranking help (relevance, distance,
prominence; can't pay for local rank); Google AI features page (no special optimization or schema, Web search type
in Search Console); Pew 2025 social media use (YouTube 84%, Facebook 71%, Instagram 50%, TikTok 37%, WhatsApp 32%);
Google Core Web Vitals page; Google Quality Score help; Performance Max help; GA4 key events (renamed March 2024, 30
per standard property); UTM help; LocalBusiness structured data; Maps prohibited content policy; LSA lead charging
(from Google's "How leads work" page as summarized in earlier verified modules).
Not used (couldn't verify from a primary or reliable local page): a Houston Filipino-language newspaper, Korean
neighborhood boundaries, Eid al-Fitr 2027 date, Pew's Asian-specific WhatsApp rates, Filipino English-proficiency
share, KREH call letters and frequency for Radio Saigon Houston.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    # Asian American guide
    "rice": A("https://news.rice.edu/news/2026/kinder-institute-releases-comprehensive-study-one-houston-areas-fastest-growing", "Rice University’s Kinder Institute"),
    "abc13rice": A("https://abc13.com/post/fast-growth-diverse-views-what-new-study-reveals-houstons-asian-population/18397954/", "ABC13’s coverage of the study"),
    "chamber": A("https://asianchamber-hou.org/stats", "Asian Chamber of Commerce Houston"),
    "langs": A("https://311.houstontx.gov/ispeakhouston/Top-25-Houston-Languages-2021.pdf", "City of Houston’s top-25 languages table"),
    "cikaty": A("https://communityimpact.com/katy/data-reference/katy-area-fort-bend-county-see-notable-increase-in-asian-population-data-shows/", "Community Impact"),
    "ciasian": A("https://communityimpact.com/katy-fulshear/katy-asian-town-brings-new-multicultural-hub/", "Community Impact’s 2017 report"),
    "gandhi": A("https://southwestmanagementdistrict.org/gandhi-district/", "Southwest Management District"),
    "landing": A("https://houstonlanding.org/50-years-later-the-fall-of-saigon-still-resonates-throughout-houstons-vietnamese-diaspora/", "Houston Landing"),
    "saigon": A("https://abc13.com/radio-saigon-houston-vietnamese-americans-in-our-america/10585248", "Radio Saigon Houston"),
    "voa": A("https://abc13.com/post/publisher-of-texas-largest-asian-american-newspaper-turns-86/5671454/", "Voice of Asia"),
    "sng": A("https://www.voanews.com/a/chinese-publisher-profits-from-growth-houston-asian-population/2437843.html", "Southern News Group"),
    "scd": A("https://scdaily.com/post/95430", "Southern Chinese Daily News"),
    "pewviet": A("https://www.pewresearch.org/race-and-ethnicity/fact-sheet/asian-americans-vietnamese-in-the-u-s/", "Pew Research Center"),
    "pewasian": A("https://www.pewresearch.org/short-reads/2025/05/01/key-facts-about-asians-in-the-us/", "Pew’s key facts about Asian Americans"),
    "sinch": A("https://sinch.com/blog/most-popular-messaging-apps-by-country/", "Sinch’s country-by-country rundown"),
    "zalo": A("https://news.tuoitre.vn/vietnams-80-million-user-messaging-giant-zalo-puts-spotlight-on-parent-vngs-business-103251229150347905.htm", "Tuoi Tre"),
    "sel": A("https://searchengineland.com/meta-will-remove-targeting-options-for-sensitive-topics-on-january-19-378095", "Search Engine Land"),
    "mml": A("https://developers.facebook.com/docs/marketing-api/multi-language-ads", "multi-language ads"),
    "glang": A("https://support.google.com/google-ads/answer/1722078?hl=en", "language targeting help page"),
    "gsc": A("https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites", "guidance on multilingual sites"),
    "rmg": A("https://www.rmg.co.uk/stories/time/lunar-new-year-dates-animals-zodiac", "Royal Museums Greenwich"),
    "tet": A("https://baonghean.vn/en/am-duong-lich-ngay-6-thang-2-nam-2027.html", "Vietnam’s lunar calendar"),
    "holi": A("https://www.officeholidays.com/amp/holidays/holi", "Office Holidays"),
    "moon": A("https://www.officeholidays.com/amp/holidays/taiwan/mid-autumn-festival", "Mid-Autumn Festival"),
    "diwali": A("https://www.officeholidays.com/amp/calendars/2027/10/29", "Diwali"),
    # Q&A and glossary
    "ws": A("https://www.wordstream.com/blog/2026-google-ads-benchmarks", "WordStream/LocaliQ’s 2026 Google Ads benchmarks"),
    "bl": A("https://www.brightlocal.com/research/local-consumer-review-survey/", "BrightLocal’s 2026 Local Consumer Review Survey"),
    "starter": A("https://developers.google.com/search/docs/fundamentals/seo-starter-guide", "SEO Starter Guide"),
    "rank": A("https://support.google.com/business/answer/7091?hl=en", "local ranking help page"),
    "aif": A("https://developers.google.com/search/docs/appearance/ai-features", "page on AI features"),
    "pew": A("https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/", "Pew Research Center’s 2025 survey"),
    "cwv": A("https://developers.google.com/search/docs/appearance/core-web-vitals", "Core Web Vitals page"),
    "qs": A("https://support.google.com/google-ads/answer/6167118?hl=en", "Quality Score help page"),
    "pmax": A("https://support.google.com/google-ads/answer/10724817?hl=en", "Performance Max help page"),
    "keyev": A("https://support.google.com/analytics/answer/13965727?hl=en", "events and key events page"),
    "utm": A("https://support.google.com/analytics/answer/10917952?hl=en", "URL builder help"),
    "lbschema": A("https://developers.google.com/search/docs/appearance/structured-data/local-business", "LocalBusiness structured data documentation"),
    "policy": A("https://support.google.com/contributionpolicy/answer/7400114?hl=en", "prohibited content policy"),
    "lsaleads": A("https://support.google.com/localservices/answer/7195435?hl=en", "“How leads work” page"),
}

ASIAN = "/blog/asian-american-marketing-houston/"
QA = "/blog/houston-the-woodlands-business-marketing-questions-answered/"
GLOSS = "/blog/digital-marketing-glossary-houston-business-owners/"
L = lambda href, text: f'<a href="{href}">{text}</a>'  # noqa: E731

POSTS = [
    # ------------------------------------------------------------------ post 1: Asian American communities
    {
        "slug": "asian-american-marketing-houston",
        "title": "Marketing to Houston’s Asian American Communities: Chinese, Vietnamese, Indian, Filipino and More",
        "seo_title": "Asian American Marketing in Houston: A Data-Built Guide",
        "desc": "Marketing to Houston’s Asian American communities: Census data, Bellaire Blvd to Katy Asian Town, in-language media, WeChat and Zalo, and 2027 holiday dates.",
        "category": "Strategy",
        "icons": ["Facebook", "YouTube", "Google"],
        "art": "b2",
        "hero": "pins",
        "hero_alt": "Illustration of map pins for marketing to Asian American communities in Houston, Sugar Land, Katy and The Woodlands",
        "related": ["hispanic-marketing-houston-spanish-ads-seo", "marketing-your-business-katy-cypress-tx", "standing-out-houston-competitive-market"],
        "sections": [
            (None, f"""<p>713,430. That’s how many Asian residents the {SRC['chamber']} counts in the Houston area for 2023, about 9.5% of everyone here. Rice University’s {SRC['rice']} put the share at 1.8% back in 1980.</p>
<p>Most Houston and The Woodlands businesses still market to that group as one audience called “Asian,” usually with a red-and-gold graphic in late January. That single audience doesn’t exist.</p>
<p>A Vietnamese grandmother in Alief who reads Radio Saigon Houston’s Facebook posts, a Telugu-speaking software engineer in Katy and a Filipino nurse in Pearland don’t share a language or a holiday calendar. They don’t use the same apps or the same grocery store either. What they share is a census checkbox.</p>
<p>This guide is built from the numbers first: who lives where, which languages are actually spoken at home, and where each community gets its information. Then it covers the practical part: platforms, translation, the 2027 holiday calendar and the mistakes we’d steer any client away from. It’s a companion to our {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'guide to Hispanic marketing in Houston')}, and a lot of the mechanics (separate language pages, phones answered in-language) carry over.</p>"""),

            ("How many Asian Americans live in Houston, and from where?", f"""<p>Start with the size. Rice’s Kinder Institute released the first findings from its Asian American Community Study in January 2026, covering Harris, Fort Bend, Montgomery and Brazoria counties. It counted more than 655,000 Asian residents in the region, with Asian Indians the largest group at over 150,000. Fort Bend’s Asian population grew 117% from 2010 to 2023. Montgomery County’s grew 180%, which surprises people in The Woodlands until they look around Creekside Park or the Grand Parkway corridor.</p>
<!--fig:size-->
<p>The groups are close in size, which is what makes Houston unusual. The Asian Chamber’s 2023 figures, drawn from Census data, put Asian Indian residents at 167,084 and Vietnamese at 158,957, with Chinese residents at 122,546. Filipino (78,540) and Pakistani (50,887) residents come next, then Korean (28,045). Pew’s analysis of 2017-2019 Census data put Houston’s Vietnamese population second among U.S. metros, tied with San Jose and behind only Los Angeles.</p>
<!--fig:groups-->
<p>Income and education vary a lot inside the total. In the Kinder survey of 2,100 residents, 46% of Asian households earned over $100,000 a year and 25% earned under $50,000. Among Vietnamese households, 30% earned over $100,000 and 19% earned under $25,000. Party identification split almost evenly in thirds, per {SRC['abc13rice']}, and most respondents described themselves as moderate. Any campaign built on a single “affluent Asian professional” persona misses a big share of the market.</p>"""),

            ("Which languages Houston’s Asian American residents speak at home", f"""<p>Population tells you who. Language tells you what to write. Inside Houston city limits, the {SRC['langs']} (2021 American Community Survey) shows Vietnamese as the third most spoken language at home, after English and Spanish, with 29,060 speakers. Chinese, which the Census groups together (Mandarin and Cantonese), is fourth at 27,838.</p>
<!--fig:langs-->
<p>Below those two, South Asian languages spread out: Hindi, Urdu, Telugu, Gujarati and Tamil all show up in the city’s top 20. That fragmentation is the point. An Indian American audience in Sugar Land or Katy doesn’t have one home language, and most of them read English comfortably, so English-language marketing with the right cultural cues usually beats a Hindi translation. The same is true for many Filipino families, where Tagalog is spoken at home but English is the default for business.</p>
<p>Vietnamese is different. {SRC['pewviet']} found 56% of Vietnamese Americans age 5 and older are proficient in English, and only 36% of Vietnamese immigrants are, against 74% of Asian Americans overall per {SRC['pewasian']}. If your customers include older Vietnamese homeowners in Alief, Mission Bend or southwest Houston, Vietnamese-language ads, pages and phone answering will reach people that English never will.</p>
<p>Two details catch first-timers. Chinese comes in two scripts: Simplified for most mainland Chinese immigrants, Traditional for many Taiwanese, Hong Kong and older Cantonese-speaking families. And Vietnamese depends on its diacritics. “Ma,” “má,” “mà” and “mã” are different words, so a font or a CMS that strips accent marks turns your copy into nonsense.</p>"""),

            ("Community hubs: Bellaire Blvd, Alief, Hillcroft, Sugar Land and Katy Asian Town", f"""<p>Asian Houston started in the southwest and spread outward along the freeways. Knowing the hubs matters for radius targeting, for event sponsorships, and for knowing where flyers still work.</p>
<!--fig:map-->
<div class="bp-tbl"><table>
<thead><tr><th>Hub</th><th>Where</th><th>Who you’ll reach</th><th>Notes for marketers</th></tr></thead>
<tbody>
<tr><td>Chinatown / Asiatown</td><td>Bellaire Blvd, roughly Gessner to Beltway 8 and beyond</td><td>Chinese, Taiwanese and Vietnamese shoppers, plus Korean, Thai and other businesses</td><td>The {SRC['gandhi']} defines Chinatown as about 2.37 square miles. Plaza bulletin boards and Chinese yellow pages still matter here.</td></tr>
<tr><td>Little Saigon / Alief</td><td>Bellaire Blvd west toward Alief, next to Chinatown</td><td>Vietnamese families, many of them multigenerational</td><td>{SRC['landing']} notes businesses here fly the South Vietnamese flag; see the mistakes section.</td></tr>
<tr><td>Mahatma Gandhi District</td><td>Hillcroft Ave and Harwin Dr, near the Southwest Freeway</td><td>Indian, Pakistani and broader South Asian shoppers</td><td>Named in a January 16, 2010 ceremony. Sari shops, jewelers, grocers and sweets shops; busiest before Diwali and Eid.</td></tr>
<tr><td>Sugar Land and Missouri City</td><td>Fort Bend County, US-59 / I-69 southwest</td><td>Chinese, Indian, Vietnamese and Pakistani families</td><td>Fort Bend was 22.2% Asian in the 2020 Census, per {SRC['cikaty']}.</td></tr>
<tr><td>Katy Asian Town</td><td>Off the Grand Parkway near I-10</td><td>Chinese, Korean, Vietnamese and Indian families on the west side</td><td>Opened in 2018 with an H Mart anchor ({SRC['ciasian']}). Katy ISD’s Asian enrollment went from 11.1% to 16.1% in a decade.</td></tr>
<tr><td>North Houston and The Woodlands</td><td>Spring, Cypress, Tomball, The Woodlands</td><td>Fast-growing, mostly professional families</td><td>Montgomery County’s Asian population grew 180% from 2010 to 2023. Fewer hubs, more Facebook groups and HOA channels.</td></tr>
</tbody></table></div>
<p>For a business in The Woodlands, the takeaway isn’t to open a branch on Bellaire. It’s to stop assuming your customers there look like your customers in 2010. A radius around Sugar Land or the Grand Parkway west of I-10 reaches a very different mix than one around Market Street, and your ad creative should know that. Our {L('/blog/marketing-your-business-katy-cypress-tx/', 'Katy and Cypress marketing guide')} has more on the west side.</p>"""),

            ("Local in-language media in Houston", f"""<p>Houston has a real in-language media scene, and for some audiences it outperforms anything you can buy on Meta. A few outlets with documented local roots:</p>
<ul>
<li><b>Chinese.</b> {SRC['sng']}, founded in Houston by Wea Lee, publishes community newspapers and runs the ITV channel. Its {SRC['scd']} site still publishes the Houston Chinese yellow pages (休斯顿黄页) as an e-book, which tells you something about how many Chinese-speaking customers still look up a dentist or a roofer.</li>
<li><b>Vietnamese.</b> {SRC['saigon']} is a Vietnamese-language AM station that ABC13 profiled in 2021 as a connection point for the area’s Vietnamese community. Call-in shows and paid segments with a host who speaks to your service are worth more than a 30-second spot.</li>
<li><b>South Asian.</b> {SRC['voa']}, a weekly founded in 1987 by Koshy Thomas, covers the Houston Asian American community, and the Indo-American News has been published weekly from southwest Houston for decades. Both are mostly English.</li>
<li><b>Filipino.</b> In our experience the reach here runs through community associations, parishes and Facebook groups more than a single publication. We couldn’t verify a current Houston Filipino-language paper, so we won’t name one.</li>
</ul>
<p>Rates and circulation change, so ask each outlet for current numbers and a sample of an ad that ran for a business like yours. Then give every placement its own phone number or landing page URL so you can tell what worked. The {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking guide')} covers how.</p>"""),

            ("Platforms: WeChat, Zalo, KakaoTalk, WhatsApp and in-language Facebook and YouTube", f"""<p>Each community’s home country has its own default messaging app, and immigrants often keep it because that’s where family is. {SRC['sinch']} lists WeChat as the most popular messaging app in China, KakaoTalk in South Korea, Zalo in Vietnam, WhatsApp in India and Messenger in the Philippines. Zalo alone had 79.2 million monthly active users in the third quarter of 2025, per {SRC['zalo']}.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Platform</th><th>Strongest with</th><th>What a Houston business can realistically do</th></tr></thead>
<tbody>
<tr><td>WeChat</td><td>Mainland Chinese immigrants and their parents</td><td>Organic: a business account, QR code at checkout, posts shared into community groups. Paid WeChat ads are built mostly for reaching users in China, so for a local shop the organic side is what’s practical.</td></tr>
<tr><td>Zalo</td><td>Recent Vietnamese arrivals and people with close ties to Vietnam</td><td>Mostly one-to-one messaging. Offer it as a contact option if your staff speaks Vietnamese. Facebook is still the bigger Vietnamese channel in Houston in our experience.</td></tr>
<tr><td>KakaoTalk</td><td>Korean Americans, especially first generation</td><td>Contact option and community group sharing. Korean churches and H Mart-area businesses are the usual connectors.</td></tr>
<tr><td>WhatsApp</td><td>Indian, Pakistani and many Filipino families</td><td>A WhatsApp Business number for quotes and appointments. Click-to-WhatsApp ads run through Meta Ads Manager.</td></tr>
<tr><td>Facebook and YouTube (in-language)</td><td>Everyone, especially Vietnamese and Filipino adults</td><td>Vietnamese-language Facebook ads and video, and YouTube ads next to in-language content. Nationally, {SRC['pew']} found 84% of adults use YouTube and 71% use Facebook.</td></tr>
</tbody></table></div>
<p>On Meta, you can’t target by ethnicity. Meta removed detailed targeting options tied to race and ethnicity, among other sensitive topics, on January 19, 2022, per {SRC['sel']}. What you can target is language and location. Meta’s {SRC['mml']} feature lets one ad carry a Vietnamese, Chinese and English version and shows each person the one that matches their language setting.</p>
<p>On Google, the rules changed this fall. Google’s {SRC['glang']} says that starting September 2026, the campaign-level language setting for Search is gone, and Search ads match based on the language of the ads themselves. So a Vietnamese Search campaign now lives or dies on Vietnamese ad text and Vietnamese keywords like “nha khoa gần tôi” (dentist near me) or “sửa máy lạnh” (AC repair). Our {L('/services/search-marketing/', 'search team')} builds these as separate campaigns so the reporting stays clean.</p>"""),

            ("Translation vs. transcreation for Houston’s Asian languages", f"""<p>Machine translation gets you words. It doesn’t get you an ad that a Vietnamese speaker in Alief would believe was written for them.</p>
<!--fig:transcreate-->
<p>Transcreation means a native speaker rewrites the message for the audience, keeping the intent and changing whatever needs changing: the headline, the offer, the photo, sometimes the call to action. A “Free estimate!” headline translated word for word into Vietnamese can read stiff or even suspicious. A native writer might lead with the fact that your technicians speak Vietnamese, because to an older homeowner that’s the actual benefit.</p>
<p>For the website, Google’s {SRC['gsc']} recommends a separate URL for each language version, links between them, and no automatic redirects based on a guessed language. So build /vi/ or /zh-hans/ pages. A Google Translate dropdown in the footer doesn’t count, because Google can’t index it as a Vietnamese page and your Vietnamese ads have nowhere good to land.</p>
<p>The rule we give every client: don’t launch a language until someone answers the phone in it. A Vietnamese ad that leads to an English-only voicemail costs you the click and some trust. If you can only staff one language, start with the one your best current customers already speak. Our {L('/services/web-design-seo-pr/', 'web design and SEO team')} handles multilingual builds.</p>"""),

            ("The 2027 holiday calendar: Lunar New Year, Tết, Diwali and more", f"""<p>Holidays are where most brands show up, and where most of the cringe happens. These are the 2027 dates, verified, with what we’d do around each.</p>
<!--fig:calendar-->
<p><b>Lunar New Year and Tết, Saturday, February 6, 2027.</b> Per {SRC['rmg']}, it opens the Year of the Goat. {SRC['tet']} puts Tết Nguyên Đán on the same day this year. Call it Lunar New Year, or Tết in Vietnamese-language materials. “Chinese New Year” is accurate for Chinese customers and wrong for Vietnamese and Korean ones (Koreans call it Seollal). Start campaigns two to three weeks early. Families buy gifts, book restaurants and schedule home repairs before the holiday, not on it.</p>
<p><b>Holi, March 22, 2027</b> (some regions mark March 23, per {SRC['holi']}). A spring festival of colors, big with Hindu families. Fine for a light social post; most businesses shouldn’t build a promotion around it.</p>
<p><b>Asian American, Native Hawaiian and Pacific Islander Heritage Month, May.</b> Better used for spotlighting staff or local partners than for discounts.</p>
<p><b>{SRC['moon']}, Wednesday, September 15, 2027.</b> Mooncake season for Chinese families and Tết Trung Thu for Vietnamese families, when kids carry lanterns. Bakeries, gift shops and restaurants should plan for the two weeks before.</p>
<p><b>{SRC['diwali']}, Friday, October 29, 2027.</b> The biggest shopping moment for many Indian American households: jewelry, clothes, sweets, home cleaning and decor, even cars. Local temples sometimes publish slightly different dates based on U.S. time zones, so confirm with a temple calendar before you print anything.</p>
<p>Plan these on the same calendar as everything else. Our {L('/blog/seasonal-marketing-greater-houston/', 'Greater Houston seasonal marketing calendar')} has the rest of the year.</p>"""),

            ("Mistakes to avoid (we’ve seen all of these)", f"""<p>Most of the damage comes from shortcuts rather than bad intentions. These are the ones we’d catch in a creative review.</p>
<!--fig:mistakes-->
<p>The flag one deserves a sentence. Many Vietnamese Americans in Houston are refugees or children of refugees from the fall of Saigon in 1975. {SRC['landing']} describes businesses in Little Saigon flying the yellow flag with three red stripes of the former South Vietnam, while the current red flag with a yellow star is rarely seen. Use the wrong one in a Tết ad and you’ll hear about it within the hour.</p>
<p>Stock photos are the other common one. A Sugar Land dental practice that shows a generic East Asian family for its Diwali post has told its Indian patients it wasn’t paying attention. Use photos of your real staff and customers (with permission), and when you use stock, match it to the actual audience.</p>"""),

            ("A first-quarter plan for a Houston business", f"""<p>Here’s how we’d start, for a business that already serves some Asian American customers and wants more:</p>
<ol>
<li><b>Weeks 1 and 2: look at your own data.</b> Pull customer ZIP codes and names from your CRM, and ask your front desk which languages callers prefer. You’re looking for a pattern rather than a demographic report.</li>
<li><b>Weeks 3 to 5: pick one language and staff it.</b> One bilingual employee on the phones beats a five-language website.</li>
<li><b>Weeks 6 to 9: build the landing page and transcreated ads.</b> Separate URL, native-speaker copy, the right script for Chinese, correct diacritics for Vietnamese.</li>
<li><b>Weeks 10 to 13: run and measure.</b> Meta multi-language ads in a radius around your hub, Google Search ads in that language, one in-language media test with its own tracking number. Judge each on booked appointments or jobs.</li>
</ol>
<p>Time it so the launch lands two weeks before Lunar New Year or Diwali, and you get a built-in reason to talk to people. Our {L('/services/paid-social-advertising/', 'paid social team')} runs the Meta side for clients across Greater Houston.</p>
<p>If you want help figuring out which community and which language makes sense for your business, <a href="/contact/">get in touch</a> and tell us who your customers are today. A senior strategist will build a plan around that.</p>"""),
        ],
        "faq": [
            ("How large is the Asian American population in Houston?",
             "Rice University’s Kinder Institute counted more than 655,000 Asian residents in Harris, Fort Bend, Montgomery and Brazoria counties in its 2026 study, nearly 10% of the population. The Asian Chamber of Commerce Houston puts the Houston area at 713,430 for 2023. Asian Indians are the largest group, followed closely by Vietnamese and Chinese residents, then Filipino, Pakistani and Korean residents."),
            ("What Asian languages are most spoken in Houston?",
             "Inside Houston city limits, Vietnamese is the third most spoken language at home after English and Spanish, and Chinese is fourth, according to the City of Houston’s table of 2021 American Community Survey data. Hindi, Tagalog, Urdu, Telugu, Gujarati, Korean and Tamil also rank in the city’s top 20. Many South Asian and Filipino residents read English comfortably, so the language choice depends on the audience."),
            ("Can I target Asian Americans with Facebook ads in Houston?",
             "Not by ethnicity. Meta removed detailed targeting options tied to race and ethnicity in January 2022. You can target by language and location, such as Vietnamese speakers within a radius of Alief or Sugar Land, and Meta’s multi-language ads feature shows each person the version of an ad in their own language. Strong in-language creative does most of the targeting work."),
            ("When is Lunar New Year and Diwali in 2027?",
             "Lunar New Year, called Tết by Vietnamese families and Seollal by Korean families, falls on Saturday, February 6, 2027, the start of the Year of the Goat. Diwali falls on Friday, October 29, 2027, though some Houston temples may publish a slightly different date based on U.S. time zones. Start holiday campaigns two to three weeks before each date."),
            ("Should my Houston business translate its website into Vietnamese or Chinese?",
             "Only if someone on your team can answer calls and messages in that language. If you can, build separate pages at their own URLs, such as a /vi/ section, written by a native speaker rather than machine translated. Use Simplified or Traditional Chinese depending on your audience, and make sure Vietnamese diacritics display correctly. A translate widget alone won’t rank or convert."),
        ],
        "figures": {
            "size": {
                "type": "stats",
                "title": "Houston’s Asian American population at a glance",
                "stats": [["713K", "Asian residents in the Houston area, 2023"], ["9.5%", "share of the area’s population"], ["22.2%", "share of Fort Bend County, 2020 Census"], ["+180%", "Montgomery County growth, 2010-2023"]],
                "note": "Sources: Asian Chamber of Commerce Houston, Community Impact, Rice Kinder Institute",
                "alt": "Stats on the Asian American population in Houston, Fort Bend County and Montgomery County near The Woodlands",
                "caption": f"From the {SRC['chamber']}, {SRC['cikaty']} and {SRC['rice']}.",
            },
            "groups": {
                "type": "bars",
                "title": "Houston-area Asian residents by origin, 2023",
                "sub": "Largest six groups",
                "items": [["Asian Indian", 167084, "167,084"], ["Vietnamese", 158957, "158,957"], ["Chinese", 122546, "122,546"], ["Filipino", 78540, "78,540"], ["Pakistani", 50887, "50,887"], ["Korean", 28045, "28,045"]],
                "highlight": [0, 1, 2],
                "note": "Source: Asian Chamber of Commerce Houston, from Census data",
                "alt": "Bar chart of Houston Asian American population by origin: Asian Indian, Vietnamese, Chinese, Filipino, Pakistani, Korean",
                "caption": f"Three groups of similar size lead. Figures from the {SRC['chamber']}.",
            },
            "langs": {
                "type": "bars",
                "title": "Asian languages spoken at home in Houston",
                "sub": "City of Houston residents age 5+, 2021",
                "items": [["Vietnamese", 29060, "29,060"], ["Chinese (Mandarin, Cantonese)", 27838, "27,838"], ["Hindi", 10936, "10,936"], ["Tagalog", 6433, "6,433"], ["Urdu", 6230, "6,230"], ["Telugu", 4676, "4,676"], ["Gujarati", 4357, "4,357"], ["Korean", 3760, "3,760"]],
                "highlight": [0, 1],
                "note": "Source: City of Houston, 2021 American Community Survey 1-year. City limits only.",
                "alt": "Bar chart of Asian languages spoken at home in Houston, led by Vietnamese and Chinese",
                "caption": f"Vietnamese is the third most spoken home language in the city, after English and Spanish. From the {SRC['langs']}.",
            },
            "map": {
                "type": "map",
                "title": "Where Houston’s Asian American hubs are",
                "sub": "Southwest Houston first, then Fort Bend, Katy and the north side",
                "highlight": ["Bellaire", "Sugar Land", "Missouri City", "Katy", "Galleria", "Cypress", "Spring"],
                "note": "Chinatown, Little Saigon and Alief sit along Bellaire Blvd west of the city of Bellaire; the Gandhi District is on Hillcroft.",
                "alt": "Map of Asian American community hubs in Greater Houston including Bellaire Blvd, Sugar Land, Katy and The Woodlands",
                "caption": "Use these areas for radius targeting and event sponsorships, then check your own customer ZIP codes.",
            },
            "transcreate": {
                "type": "compare",
                "title": "Translation vs. transcreation",
                "left": {"title": "Word-for-word translation", "items": ["English headline run through a translator", "Same offer and photo as the English ad", "One “Chinese” version for everyone", "Accent marks dropped by the CMS", "Translate widget instead of real pages"]},
                "right": {"title": "Transcreation", "items": ["Native speaker rewrites the message", "Leads with what matters to that audience", "Simplified or Traditional, chosen on purpose", "Vietnamese diacritics checked on every device", "Separate /vi/ or /zh-hans/ pages that rank"]},
                "alt": "Comparison of translation versus transcreation for marketing to Vietnamese and Chinese speakers in Houston",
                "caption": "Budget for a native-speaker review of every ad, page and script.",
            },
            "calendar": {
                "type": "steps",
                "title": "2027 Asian American holiday calendar",
                "sub": "Dates verified; start campaigns two to three weeks early",
                "steps": [["Feb 6: Lunar New Year and Tết", "Year of the Goat. Gifts, dining, home prep in the weeks before."], ["Mar 22: Holi", "Spring festival of colors. Light social content."], ["May: AANHPI Heritage Month", "Staff and partner spotlights rather than discounts."], ["Sep 15: Mid-Autumn Festival", "Mooncakes and lanterns for Chinese and Vietnamese families."], ["Oct 29: Diwali", "Peak shopping for many Indian American households."]],
                "alt": "Timeline of 2027 Lunar New Year, Tet, Holi, Mid-Autumn Festival and Diwali dates for Houston marketing",
                "caption": "Confirm Diwali timing with a local temple calendar before printing.",
            },
            "mistakes": {
                "type": "checklist",
                "title": "Mistakes to avoid",
                "sub": "What we catch most often in creative reviews",
                "items": ["Treating “Asian” as one audience", "Calling Tết or Seollal “Chinese New Year”", "Using the current Vietnam flag in Little Saigon ads", "East Asian stock photos for a Diwali post", "Machine translation with no native review", "Wrong Chinese script for the audience", "Ads in a language nobody on staff speaks", "Holiday promos that start the day of"],
                "alt": "Checklist of mistakes to avoid when marketing to Asian American communities in Houston and The Woodlands",
                "caption": "Each one is cheap to avoid and expensive to apologize for.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: Q&A roundup
    {
        "slug": "houston-the-woodlands-business-marketing-questions-answered",
        "title": "Marketing Questions Houston and The Woodlands Business Owners Ask Us Most (Answered)",
        "seo_title": "Houston & The Woodlands Marketing Questions, Answered",
        "desc": "Straight answers to the marketing questions Houston and The Woodlands owners ask most: budget, SEO timelines, Google Ads vs LSA, social, reviews, AI search.",
        "category": "Strategy",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b4",
        "hero": "speech",
        "hero_alt": "Illustration of speech bubbles for marketing questions from Houston and The Woodlands business owners",
        "related": ["set-a-marketing-budget-small-business", "how-long-does-seo-take-houston-the-woodlands", "questions-before-hiring-marketing-agency"],
        "sections": [
            (None, f"""<p>Twenty questions. That’s roughly how many come up again and again when Houston and The Woodlands business owners talk to us, whether they run a dental practice off Research Forest, an HVAC company in Spring or a boutique on Market Street.</p>
<p>They’re good questions, and most of them have shorter answers than the internet suggests. The longer answers usually start with “it depends,” and then the agency stops talking. We’d rather tell you what it depends on. So here they are, grouped by topic, each with a direct answer and a link to the longer post if you want the detail. Where we quote a number, it’s sourced. Where it’s our opinion, we say so.</p>
<!--fig:index-->"""),

            ("Budget and cost questions from Houston owners", f"""<h3>1. How much should a small business in Houston spend on marketing?</h3>
<p>There’s no universal percentage that holds up. Work backward instead: what’s a customer worth to you, how many more do you want a month, and what does one cost to win in your category? A plumber who nets $400 a job can afford a very different cost per lead than a med spa selling $3,000 packages. Our {L('/blog/set-a-marketing-budget-small-business/', 'budget-setting guide')} walks through the math, and {L('/blog/digital-marketing-cost-the-woodlands-houston/', 'what digital marketing costs in The Woodlands and Houston')} covers typical ranges.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Business stage</th><th>Illustrative monthly ad spend</th><th>Where we’d put it first</th></tr></thead>
<tbody>
<tr><td>New or one-location, under $1M revenue</td><td>$1,000 to $3,000</td><td>Google Business Profile, reviews, one tight Google Ads or LSA campaign</td></tr>
<tr><td>Established local business, $1M to $5M</td><td>$3,000 to $10,000</td><td>Search plus LSA, retargeting, service pages for SEO</td></tr>
<tr><td>Multi-location or regional</td><td>$10,000 and up</td><td>Location pages, Meta and YouTube for demand, tracked offline conversions</td></tr>
</tbody></table></div>
<p>Those ranges are illustrative, not quotes. Your category and your close rate move them a lot.</p>
<p>One more piece most owners skip: budget for the agency or the person running it separately from the media. A $2,000 ad budget with nobody reading the search terms report is usually worse than $1,200 with someone who does.</p>
<h3>2. What does a lead actually cost on Google Ads?</h3>
<p>Nationally, {SRC['ws']} put the all-industry averages at $5.42 per click, an 8.18% conversion rate and $66.69 per lead. Home services ran $8.33 a click and $90.92 a lead; attorneys, $9.87 and $131.63. Competitive Houston categories like roofing, personal injury and emergency AC in August often run above those averages. See our {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')} and {L('/blog/understanding-cost-per-lead/', 'cost per lead explainer')}.</p>
<!--fig:cpl-->
<h3>3. Is marketing supposed to pay for itself right away?</h3>
<p>Paid search often can within a couple of months, if tracking is right. SEO and brand work usually can’t, and judging them on 30-day results kills them early. We’d hold each channel to a payback window that fits it. A rough version: search ads judged at 60 to 90 days, Meta at 90, SEO at six to twelve months, streaming TV and billboards on whether branded searches and direct calls rise over a quarter. {L('/blog/marketing-that-pays-for-itself/', 'Marketing that pays for itself')} has the framework.</p>"""),

            ("SEO and Google Maps questions", f"""<h3>4. How long does SEO take to work?</h3>
<p>For most local businesses in Houston and The Woodlands, first movement shows up in one to three months, steady calls around months four to six, and gains keep compounding through month twelve. Google’s own {SRC['starter']} says some changes “could take several months” and that you “likely want to wait a few weeks” before judging a change. Full breakdown in {L('/blog/how-long-does-seo-take-houston-the-woodlands/', 'how long SEO takes in Houston')}.</p>
<!--fig:seo-->
<h3>5. Why don’t I show up in the Google map pack?</h3>
<p>Google’s {SRC['rank']} says local results are based on relevance, distance and prominence, and that you can’t pay for a better local ranking. In practice that means the right primary category, a complete profile, steady reviews and a website page for each service. Distance you can’t change, which is why a business in Conroe rarely ranks in Sugar Land. It’s also why your ranking looks great from your office and mediocre from a customer’s kitchen in Magnolia; check it from several spots across your service area. Start with {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Houston map pack')}.</p>
<h3>6. What does SEO cost?</h3>
<p>For a single-location local business, monthly retainers usually run $800 to $2,000; competitive categories like law, HVAC and dental often run $2,000 to $5,000. Our {L('/blog/seo-cost-houston-the-woodlands/', 'SEO cost guide')} explains what should be included at each level.</p>"""),

            ("Google Ads vs. Local Services Ads", f"""<h3>7. Should I run Google Ads or Local Services Ads?</h3>
<p>If your category qualifies for LSA (most home services, many legal and some auto categories), run both and compare cost per booked job. LSA charges per lead instead of per click, and Google’s {SRC['lsaleads']} explains what counts as a charged lead and what gets credited. Search ads give you control over keywords, copy, landing pages and schedule. LSA ranks heavily on reviews and how quickly you answer, so a company with 15 reviews that lets calls roll to voicemail will struggle there no matter what it spends. Details in {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs Google Ads')}.</p>
<!--fig:lsa-->
<h3>8. Why am I getting clicks but no calls?</h3>
<p>Usually it’s one of four things: the keywords are too broad, the ad sends people to the homepage, the landing page is slow on a phone, or calls aren’t being tracked so you can’t see the ones you did get. {L('/blog/google-ads-not-converting-clicks-no-calls/', 'Google Ads not converting')} has the full checklist.</p>
<h3>9. Is Performance Max right for a local business?</h3>
<p>Sometimes. Google’s {SRC['pmax']} describes it as a goal-based campaign that runs across YouTube, Display, Search, Discover, Gmail and Maps from one campaign. That reach is useful when your conversion tracking is clean. When it isn’t, PMax happily optimizes toward junk. We usually start local service businesses on Search, then add PMax once calls and booked jobs are flowing back into the account as conversions. Compare them in {L('/blog/performance-max-vs-search-campaigns-local/', 'PMax vs Search for local businesses')}.</p>"""),

            ("Social media questions", f"""<h3>10. Which social platform should a local business use?</h3>
<p>The one your customers already scroll, which for most Houston adults means Facebook, Instagram and YouTube. LinkedIn earns a spot only if you sell to other businesses. {SRC['pew']} found 84% of U.S. adults use YouTube, 71% use Facebook, 50% use Instagram and 37% use TikTok. A restaurant in The Woodlands and a B2B supplier in the Energy Corridor will answer this differently. {L('/blog/facebook-vs-instagram-vs-tiktok-local-business/', 'Facebook vs Instagram vs TikTok')} compares them.</p>
<h3>11. Are Facebook leads any good?</h3>
<p>They can be, but instant forms make it easy for people to submit without meaning it. Someone in Humble scrolling at 11 p.m. taps a pre-filled form and forgets about it by breakfast. Add a qualifying question or two, turn on higher-intent form settings, and call within minutes. {L('/blog/facebook-lead-ads-bad-leads-fix-quality/', 'Fixing bad Facebook leads')} goes step by step.</p>
<h3>12. How often should we post?</h3>
<p>Less often than you think, if the posts are good. Two or three useful posts a week beats a daily stream of stock graphics. For most local service businesses, organic social builds trust, and paid social is what actually reaches new people.</p>
<p>What counts as useful: a 30-second video of your tech explaining why Houston clay soil cracks slabs, a before-and-after from a job in Kingwood, your crew at a Township event. In most accounts we’ve run, real people and real places beat stock photos by a wide margin.</p>
<h3>13. Is Nextdoor or Yelp advertising worth it?</h3>
<p>Sometimes, for specific categories. Nextdoor can work for home services in neighborhoods where people actively ask for referrals, which describes a lot of The Woodlands villages and Cypress subdivisions. Yelp matters more for restaurants and some personal services than for contractors. Test either one with a small budget and its own tracking number before you sign a long contract. We break them down in {L('/blog/is-nextdoor-advertising-worth-it/', 'is Nextdoor advertising worth it')} and {L('/blog/is-yelp-advertising-worth-it-small-business/', 'is Yelp advertising worth it')}.</p>"""),

            ("Website questions", f"""<h3>14. Do I need a new website?</h3>
<p>Not always. If it loads fast on a phone, has a page for each service, shows your phone number at the top and tracks calls and forms, fix the content before you rebuild. Google’s {SRC['cwv']} sets the “good” thresholds at 2.5 seconds for Largest Contentful Paint, 200 milliseconds for Interaction to Next Paint and 0.1 for Cumulative Layout Shift. {L('/blog/signs-your-website-needs-a-redesign/', 'Signs your website needs a redesign')} lists the real triggers.</p>
<!--fig:site-->
<h3>15. How much does a website cost?</h3>
<p>For a small business in The Woodlands or Houston, a professional build usually runs from a few thousand dollars for a simple service site to well above that for custom design, e-commerce or many locations. {L('/blog/how-much-does-a-website-cost-the-woodlands/', 'Website cost in The Woodlands')} has the breakdown. Ask who owns the domain and the hosting account before you sign; it saves a painful conversation later.</p>
<h3>16. Do we need a blog?</h3>
<p>You need pages that answer the questions your customers search, and a blog is one place to put them. A Spring foundation repair company doesn’t need “5 Fun Facts About Concrete.” It needs a page on why slabs crack after a dry Houston summer, one on what a repair costs, and one on how to read an engineer’s report. Two strong posts a month beat eight thin ones. See {L('/blog/blogging-for-local-seo/', 'blogging for local SEO')}.</p>"""),

            ("Reviews and reputation", f"""<h3>17. How many Google reviews do we need?</h3>
<p>Enough to look current and credible next to your competitors. {SRC['bl']} found 74% of consumers only consider reviews from the last three months, 47% won’t use a business with fewer than 20 reviews, and 31% will only use a business rated 4.5 stars or higher. A steady trickle matters more than a big old total. A Cypress HVAC company with 300 reviews, the latest from 2023, looks closed next to a competitor with 90 and three from last week.</p>
<p>Reply to every one, good and bad. People read the replies to the one-star reviews more carefully than the reviews themselves.</p>
<!--fig:reviews-->
<h3>18. Can we offer a discount for reviews?</h3>
<p>No. Google’s {SRC['policy']} bans incentives for reviews and bans asking only happy customers. Ask every customer the same way, by text, soon after the job. {L('/blog/complete-guide-google-reviews/', 'The complete guide to Google reviews')} has scripts, and {L('/blog/fake-reviews-rule-local-businesses/', 'the FTC fake reviews rule')} covers the federal side.</p>"""),

            ("Agencies and AI search", f"""<h3>19. How do I choose a marketing agency?</h3>
<p>Write a one-page brief first: the outcome you’re buying, your budget split into fees and ad spend, and who owns your logins. Send the same brief to every agency. Insist that you own your Google Ads account, analytics and domain. Ask who will actually do the work each week, and whether you’ll ever talk to that person. A senior strategist on the sales call and a rotating junior team after signing is a common pattern, in Houston and everywhere else. {L('/blog/choose-digital-marketing-agency-the-woodlands-houston/', 'Choosing an agency in The Woodlands')} and {L('/blog/marketing-agency-contract-red-flags/', 'contract red flags')} cover the rest.</p>
<!--fig:agency-->
<h3>20. How do I show up in ChatGPT and Google’s AI Overviews?</h3>
<p>Mostly by doing good SEO. Google’s {SRC['aif']} says there are no extra requirements or special schema to appear in AI Overviews or AI Mode; a page needs to be indexed and eligible for a snippet. Clear answers to real questions, consistent business details everywhere, and reviews all help. A page that plainly answers “how much does a water heater replacement cost in Houston” is the kind of thing AI tools quote, while vague marketing copy gets skipped. It’s becoming a real channel, too: {SRC['bl']} found 45% of consumers use ChatGPT or other AI tools for local recommendations. See {L('/blog/show-up-in-chatgpt-ai-search-aeo/', 'showing up in AI search')} and {L('/blog/ai-overviews-local-search-houston/', 'AI Overviews for Houston businesses')}.</p>
<p>Not sure which of these applies to you first? Our {L(GLOSS, 'digital marketing glossary')} translates the jargon, and if you’d rather talk it through, <a href="/contact/">get in touch</a> with your goals and a senior strategist will build a plan for your business.</p>"""),
        ],
        "faq": [
            ("How much does marketing cost for a small business in The Woodlands?",
             "Most small local businesses we see in The Woodlands and Houston spend somewhere between $1,000 and $10,000 a month on ads, plus management or agency fees, but the right number depends on what a customer is worth to you and what one costs to win in your category. Work backward from your goals and your measured cost per customer instead of picking a percentage of revenue."),
            ("How long does it take to see results from Google Ads in Houston?",
             "Clicks start the day a campaign goes live, and with good tracking you can usually judge lead quality within four to eight weeks. Smart bidding needs conversion data to learn, so the first month is often the most expensive. Plan to review search terms weekly, add negative keywords, and evaluate the account on cost per booked job rather than cost per click."),
            ("Is SEO worth it for a local Houston business?",
             "Usually, if you can give it six to twelve months. SEO builds rankings in the map pack and organic results that keep producing calls without paying per click. It works best alongside paid search, which covers the months while SEO builds. Categories with very high click costs, like roofing and legal, tend to get the most value from it."),
            ("Do Google reviews help my business rank higher?",
             "Reviews are part of what Google calls prominence, one of the three factors behind local rankings along with relevance and distance. They also decide whether people call. Surveys show most consumers focus on reviews from the last three months, so ask every customer consistently after each job, reply to every review, and never offer incentives for them."),
            ("Should a Houston business hire an agency or do marketing in-house?",
             "It depends on your budget and how much time you have. One in-house marketer can rarely cover ads, SEO, design and analytics well, while an agency brings specialists for less than several hires. Whatever you choose, keep ownership of your ad accounts, analytics, website and domain, and make sure reporting shows cost per lead and cost per customer."),
        ],
        "figures": {
            "index": {
                "type": "bars",
                "title": "The 20 questions, by topic",
                "sub": "Number of questions in each group",
                "items": [["Budget and cost", 3, "3"], ["SEO and Google Maps", 3, "3"], ["Google Ads vs. LSA", 3, "3"], ["Social media", 4, "4"], ["Websites", 3, "3"], ["Reviews", 2, "2"], ["Agencies and AI search", 2, "2"]],
                "highlight": [0, 1, 2],
                "alt": "Bar chart of the 20 marketing questions Houston and The Woodlands business owners ask, grouped by topic",
                "caption": "Budget, SEO and ads come up most. Jump to whichever section fits.",
            },
            "cpl": {
                "type": "bars",
                "title": "Average Google Ads cost per lead by industry",
                "sub": "National averages, 2026",
                "items": [["Attorneys and legal", 131.63, "$131.63"], ["Business services", 93.69, "$93.69"], ["Home and home improvement", 90.92, "$90.92"], ["Dentists and dental", 72.97, "$72.97"], ["All industries", 66.69, "$66.69"], ["Personal services", 54.60, "$54.60"]],
                "highlight": [4],
                "note": "Source: WordStream/LocaliQ 2026 Google Ads benchmarks",
                "alt": "Bar chart of Google Ads cost per lead by industry for Houston and The Woodlands businesses to benchmark against",
                "caption": f"National averages from {SRC['ws']}. Competitive Houston terms often run higher.",
            },
            "seo": {
                "type": "steps",
                "title": "A typical local SEO timeline in Houston",
                "sub": "What to expect, and what to check",
                "steps": [["Weeks 1-4", "Profile fixes, service pages, tracking. Business Profile changes can move map rankings within weeks."], ["Months 1-3", "Impressions climb in Search Console and Business Profile views rise."], ["Months 4-6", "Steady calls and forms from organic and map results."], ["Months 6-12", "Gains compound as reviews and links build prominence."]],
                "alt": "Timeline of how long local SEO takes for businesses in Houston and The Woodlands, month by month",
                "caption": "A brand-new domain in a crowded category can take a year or more for the biggest terms.",
            },
            "lsa": {
                "type": "compare",
                "title": "Google Ads vs. Local Services Ads",
                "left": {"title": "Search ads", "items": ["Pay per click", "You pick keywords and write the ads", "Your own landing page", "Works for almost any business", "Needs weekly search term review"]},
                "right": {"title": "Local Services Ads", "items": ["Pay per lead, with credits for invalid ones", "Google matches you by category and area", "Ranks on reviews and responsiveness", "Limited to eligible categories", "Requires screening and a verified profile"]},
                "alt": "Comparison of Google Search ads and Local Services Ads for Houston and The Woodlands service businesses",
                "caption": "For eligible home services we’d run both and compare cost per booked job.",
            },
            "site": {
                "type": "checklist",
                "title": "Website checks before you redesign",
                "sub": "Fix these first; rebuild only if you can’t",
                "items": ["Loads in under 2.5 seconds on a phone (LCP)", "Responds to taps within 200 ms (INP)", "Layout doesn’t jump around (CLS under 0.1)", "Phone number tappable at the top", "One page per service you sell", "Service-area or location pages", "Calls and forms tracked as conversions", "You own the domain and hosting login"],
                "alt": "Checklist of website basics for Houston and The Woodlands businesses before paying for a redesign",
                "caption": f"Speed thresholds from Google’s {SRC['cwv']}.",
            },
            "reviews": {
                "type": "stats",
                "title": "What customers expect from reviews",
                "stats": [["97%", "read reviews for local businesses"], ["74%", "only consider the last three months"], ["47%", "won’t use a business with under 20"], ["45%", "use AI tools for local recommendations"]],
                "note": "Source: BrightLocal 2026 Local Consumer Review Survey",
                "alt": "Stats on how consumers use Google reviews and AI tools to choose local businesses in Houston and The Woodlands",
                "caption": f"From {SRC['bl']}.",
            },
            "agency": {
                "type": "compare",
                "title": "Agency red flags vs. green flags",
                "left": {"title": "Walk away", "items": ["They own your Google Ads account", "Long contract with no exit clause", "Reports show clicks, not leads", "Guaranteed page-one rankings", "Won’t say who does the work"]},
                "right": {"title": "Good signs", "items": ["You own every account and login", "Month-to-month or a clear exit", "Reports on cost per lead and customer", "Honest timelines with caveats", "You meet the people on your account"]},
                "alt": "Comparison of red flags and green flags when hiring a marketing agency in Houston or The Woodlands",
                "caption": "Ask about each of these before you sign anything.",
            },
        },
    },

    # ------------------------------------------------------------------ post 3: glossary
    {
        "slug": "digital-marketing-glossary-houston-business-owners",
        "title": "Digital Marketing Glossary for Houston Business Owners: 60+ Terms in Plain English",
        "seo_title": "Digital Marketing Glossary for Houston Business Owners",
        "desc": "A plain-English A-Z digital marketing glossary for Houston and The Woodlands owners: CPC, CPL, ROAS, MER, GBP, LSA, PMax, AI Overviews, UTMs and more.",
        "category": "Strategy",
        "icons": ["Google Analytics", "Google Ads", "Search Console"],
        "art": "b6",
        "hero": "layout",
        "hero_alt": "Illustration of a page layout for a digital marketing glossary for Houston and The Woodlands business owners",
        "related": ["measure-marketing-success-metrics", "clicks-to-customers-conversion-funnel", "understanding-cost-per-lead"],
        "sections": [
            (None, f"""<p>Your agency’s monthly report says ROAS is up, CTR is down, PMax is “still learning” and you picked up 14 key events. You run a roofing company in Spring. Which of those numbers means more roofs?</p>
<p>This glossary is for Houston and The Woodlands business owners who want to read their own reports without a translator. Each term gets a plain-English definition and a local example, and many link to a longer post. Terms are grouped A to Z, and the figures group related terms together, starting with the one that matters most: how the money metrics connect.</p>
<!--fig:funnel-->
<p>If you only learn five terms, make them conversion, CPL, CAC, ROAS and MER. Most of the others explain why those five moved.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Acronym</th><th>Stands for</th><th>Formula or meaning</th></tr></thead>
<tbody>
<tr><td>CTR</td><td>Click-through rate</td><td>Clicks ÷ impressions</td></tr>
<tr><td>CPC</td><td>Cost per click</td><td>Spend ÷ clicks</td></tr>
<tr><td>CVR</td><td>Conversion rate</td><td>Conversions ÷ clicks</td></tr>
<tr><td>CPL</td><td>Cost per lead</td><td>Spend ÷ leads</td></tr>
<tr><td>CAC</td><td>Customer acquisition cost</td><td>All marketing cost ÷ new customers</td></tr>
<tr><td>ROAS</td><td>Return on ad spend</td><td>Revenue ÷ ad spend (one campaign or platform)</td></tr>
<tr><td>MER</td><td>Marketing efficiency ratio</td><td>Total revenue ÷ total marketing spend</td></tr>
<tr><td>GBP, LSA, PMax</td><td>Google Business Profile, Local Services Ads, Performance Max</td><td>Google’s free listing, pay-per-lead ads and all-channel campaign type</td></tr>
</tbody></table></div>"""),

            ("A: from A/B test to Average order value", f"""<h3>A/B test</h3>
<p>Running two versions of an ad, page or email at the same time to see which performs better. A Katy dentist tests “Same-week appointments” against “Most insurance accepted” as a headline, and keeps the winner.</p>
<h3>Ad Rank</h3>
<p>Google’s calculation of where your ad shows and whether it shows at all, based on your bid, ad quality, landing page and context. It’s why a better ad from a small Humble plumber can sit above a national franchise that bids more.</p>
<h3>AEO (answer engine optimization)</h3>
<p>Making your content easy for AI tools like ChatGPT and Google’s AI features to quote. A Conroe HVAC company’s page that plainly answers “how much does AC repair cost in Conroe” is AEO. See {L('/blog/show-up-in-chatgpt-ai-search-aeo/', 'showing up in AI search')}.</p>
<h3>AI Overviews and AI Mode</h3>
<p>Google’s AI-generated answers at the top of some search results (AI Overviews) and its conversational search tab (AI Mode). Google’s {SRC['aif']} says there are no special optimizations or schema needed to appear, and the traffic is counted in Search Console under the Web search type. More in {L('/blog/ai-overviews-local-search-houston/', 'AI Overviews for Houston businesses')}.</p>
<h3>Attribution</h3>
<p>The rules for giving credit to the ads and channels that led to a sale. If a Sugar Land customer saw your Instagram ad, then searched your name and called, attribution decides which one gets the credit.</p>
<h3>Average order value (AOV)</h3>
<p>Total revenue divided by number of orders. A bakery in The Woodlands with $18,000 from 600 online orders has a $30 AOV, which caps what it can pay per click.</p>"""),

            ("B and C: Broad match through CTR", f"""<h3>Backlink</h3>
<p>A link to your website from another site. A mention in Community Impact or a link from the Greater Houston Builders Association counts for far more than 50 links from directories nobody reads.</p>
<h3>Broad match</h3>
<p>A Google Ads keyword setting that lets your ad show for searches related to your keyword, not just the keyword itself. “Plumber Spring TX” on broad match might also show for “plumbing jobs Spring.” Pair it with negative keywords and smart bidding, or don’t use it.</p>
<h3>CAC (customer acquisition cost)</h3>
<p>Everything you spent to win a customer, divided by new customers. If a Tomball med spa spends $6,000 in ads and fees and gets 20 new clients, CAC is $300. This is the number to compare against what a customer is worth.</p>
<h3>Call tracking</h3>
<p>Unique phone numbers that show which ad, page or flyer made the phone ring, often with recordings. Essential for any business where customers call instead of filling out forms. See {L('/blog/call-tracking-which-ads-make-phone-ring/', 'call tracking explained')}.</p>
<h3>Citation</h3>
<p>Any online listing of your business name, address and phone number: Yelp, Apple Maps, Bing, your local chamber of commerce directory in The Woodlands or Katy. Consistent citations help Google trust your details.</p>
<h3>Consent mode</h3>
<p>A Google setting that adjusts how tags behave when a visitor declines cookies. Matters more if you have visitors from places with stricter privacy laws, like a Galveston hotel that books European travelers.</p>
<h3>Conversion</h3>
<p>The action you count as a win: a call over 60 seconds, a form, a booking, a purchase. In Google Ads, it’s a conversion action. A Woodlands law firm that counts every page view as a conversion is fooling itself.</p>
<h3>Conversion rate (CVR)</h3>
<p>Conversions divided by clicks. {SRC['ws']} put the all-industry Google Ads average at 8.18%. If 400 people click a Pearland orthodontist’s ad and 32 book a consult, CVR is 8%.</p>
<h3>Core Web Vitals</h3>
<p>Google’s three page-experience measurements: loading (LCP), responsiveness (INP) and visual stability (CLS). Google’s {SRC['cwv']} lists “good” as 2.5 seconds, 200 milliseconds and 0.1. See {L('/blog/how-fast-should-your-website-load/', 'how fast your website should load')}.</p>
<h3>CPC (cost per click)</h3>
<p>What you pay each time someone clicks your ad. The 2026 national average was $5.42, per the same WordStream data, and emergency AC terms in Houston in July run far higher. See {L('/blog/google-ads-cost-per-click-houston-benchmarks/', 'Houston CPC benchmarks')}.</p>
<h3>CPL (cost per lead)</h3>
<p>Spend divided by leads. The national Google Ads average was $66.69 in 2026. More in {L('/blog/understanding-cost-per-lead/', 'understanding cost per lead')}.</p>
<h3>CPM (cost per thousand impressions)</h3>
<p>What you pay for 1,000 ad views. The standard price unit for streaming TV, billboards, YouTube and most social ads. A billboard on I-45 near the Woodlands Parkway exit is priced on impressions, too. See {L('/blog/billboard-advertising-cost-houston/', 'billboard costs in Houston')}.</p>
<h3>CRM (customer relationship management)</h3>
<p>The software that holds your leads and customers, such as HubSpot or a field-service tool. It’s where you find out which leads actually bought. A Spring HVAC company that logs every call in its CRM can tell which ZIP codes book maintenance plans.</p>
<h3>CTR (click-through rate)</h3>
<p>Clicks divided by impressions. A high CTR means the ad matches what people searched; it doesn’t mean they bought. A “Free pizza” ad for a Katy restaurant gets a great CTR and terrible margins.</p>
<!--fig:worked-->"""),

            ("D to G: Display Network through Google Verified", f"""<h3>Display Network</h3>
<p>Google’s network of websites and apps that show banner and image ads. Cheap reach, low intent. Fine for retargeting, risky as a primary channel for a local service business. A Conroe roofer’s banner on a mobile game app mostly buys accidental taps.</p>
<h3>Engagement rate</h3>
<p>In GA4, the share of sessions that lasted over 10 seconds, viewed two or more pages or triggered a key event. It replaced bounce rate as the main quality signal. If Facebook traffic to a Sugar Land salon’s site shows 20% engagement and Google traffic shows 65%, that tells you something.</p>
<h3>Enhanced conversions</h3>
<p>A Google Ads feature that sends hashed customer details (like an email) with a conversion so Google can match it more accurately. Helps when cookies drop off, such as when a Kingwood customer clicks on a phone and fills out the form on a laptop that evening.</p>
<h3>Frequency</h3>
<p>How many times the average person saw your ad. If people in Kingwood have seen your Facebook ad 11 times this month, they’re tired of it.</p>
<h3>Funnel</h3>
<p>The path from first seeing you to buying, usually drawn as awareness, consideration and conversion. See {L('/blog/clicks-to-customers-conversion-funnel/', 'from clicks to customers')}.</p>
<h3>GA4 (Google Analytics 4)</h3>
<p>Google’s current analytics platform. It tracks events, not page views, as its basic unit. A Tomball landscaper’s GA4 might show a form_submit event, a click_to_call event and a page_view for the pricing page.</p>
<h3>GBP (Google Business Profile)</h3>
<p>Your free listing on Google Search and Maps: hours, photos, reviews, categories. For most Houston local businesses it’s the single most valuable marketing asset. See {L('/blog/google-business-profile-number-one-asset/', 'the Google Business Profile guide')}.</p>
<h3>GCLID</h3>
<p>The Google Click ID added to a URL when someone clicks your ad. Save it with the lead in your CRM and you can tell Google later which clicks became customers. That’s how a Houston law firm teaches Google the difference between a signed case and a wrong number.</p>
<h3>Geo-fencing</h3>
<p>Showing ads to phones inside a drawn boundary, like the NRG Park area during the rodeo. See {L('/blog/geo-fencing-ads-target-customers-nearby/', 'geo-fencing ads')}.</p>
<h3>Google Guaranteed and Google Verified</h3>
<p>Badges shown on Local Services Ads after Google screens a business, such as license and background checks for a Katy electrician. See {L('/blog/google-guaranteed-vs-google-verified/', 'Google Guaranteed vs Google Verified')}.</p>"""),

            ("I to L: Impressions through LSA", f"""<h3>Impressions</h3>
<p>The number of times your ad or listing was shown. Not the same as people, and not the same as anyone looking. Your Business Profile can rack up thousands of impressions from people searching “coffee Market Street” who never notice you.</p>
<h3>Impression share</h3>
<p>The percentage of eligible impressions you actually got. A Pearland plumber at 40% search impression share is missing six in ten chances, usually because of budget or ad rank.</p>
<h3>Indexing</h3>
<p>Google adding a page to its search database. A page that isn’t indexed can’t rank, no matter how good it is. Search Console shows which pages are indexed. A new “AC repair Magnolia” page that isn’t indexed after three weeks needs a look.</p>
<h3>Key event</h3>
<p>GA4’s name for an important action, like a form submission. Google renamed GA4 conversions to key events in March 2024, and its {SRC['keyev']} explains how to mark them. A key event becomes a conversion only when you import it into Google Ads.</p>
<h3>Keyword</h3>
<p>The word or phrase you bid on or optimize for. “Foundation repair Houston” is a keyword. So is “why is my door sticking,” which a smart foundation company in Katy should have a page for.</p>
<h3>KPI (key performance indicator)</h3>
<p>The few numbers you agree to judge marketing by. Pick three at most: booked jobs, CPL and CAC is a good start.</p>
<h3>Landing page</h3>
<p>The page someone lands on after clicking an ad. It should match the ad exactly: an ad for “emergency plumber Cypress” lands on an emergency plumbing page that mentions Cypress, not the homepage. See {L('/blog/landing-pages-101/', 'landing pages 101')}.</p>
<h3>Lead</h3>
<p>A potential customer who contacted you or gave their details. A lead is not a customer, and a form from a spam bot isn’t a lead. Neither is a call from someone in Dallas asking if you’re hiring.</p>
<h3>Lookalike audience</h3>
<p>A Meta audience of people similar to a list you upload, such as past customers. Not available for housing, employment or credit ads, which matters to Montgomery County home builders and lenders.</p>
<h3>LSA (Local Services Ads)</h3>
<p>Google’s pay-per-lead ads at the top of searches for plumbers, roofers, lawyers and other eligible services. You pay per lead, not per click, and can dispute invalid ones. See {L('/blog/local-services-ads-vs-google-ads-home-services/', 'LSA vs Google Ads')}.</p>
<!--fig:local-->"""),

            ("M to O: Map pack through Organic", f"""<h3>Map pack (local pack)</h3>
<p>The three business listings with a map that show for local searches. Google’s {SRC['rank']} says rankings come from relevance, distance and prominence. See {L('/blog/rank-in-google-map-pack-houston/', 'ranking in the Houston map pack')}.</p>
<h3>Match types</h3>
<p>Google Ads settings (broad, phrase, exact) that control how closely a search must match your keyword before your ad can show. Exact match on [roof repair the woodlands] is tight; broad match on the same words can wander into “roof repair jobs Houston.”</p>
<h3>MER (marketing efficiency ratio)</h3>
<p>Total revenue divided by total marketing spend, across every channel. A Woodlands boutique with $90,000 in monthly sales and $9,000 in total marketing has a MER of 10. It’s harder to game than ROAS because no platform gets to grade its own homework.</p>
<h3>Meta Pixel and Conversions API</h3>
<p>The code (Pixel) and server connection (Conversions API) that tell Meta what people did on your site after clicking an ad. Without them, a Woodlands med spa can’t tell whether its Instagram ads booked anyone.</p>
<h3>NAP</h3>
<p>Name, address, phone. It should match exactly on your website, Google Business Profile and citations. “Suite 200” on one and “Ste. 200” is fine; a different phone number is not.</p>
<h3>Negative keyword</h3>
<p>A word that stops your ad from showing. For most service businesses: jobs, salary, free, DIY, how to. Every Houston account needs a list on day one.</p>
<h3>Offline conversion import</h3>
<p>Sending sales that happened later, in your CRM or at the counter, back to Google Ads or Meta so their bidding learns which clicks turned into revenue.</p>
<h3>Organic</h3>
<p>Traffic or results you didn’t pay for per click: SEO rankings, map listings, unpaid social posts. A Pearland bakery ranking for “king cake Pearland” every January is organic.</p>"""),

            ("P to R: PMax through ROI", f"""<h3>PMax (Performance Max)</h3>
<p>A Google Ads campaign type that its {SRC['pmax']} describes as accessing all Google Ads inventory, including YouTube, Display, Search, Discover, Gmail and Maps, from a single campaign. Powerful with clean conversion data, wasteful without it. See {L('/blog/performance-max-vs-search-campaigns-local/', 'PMax vs Search')}.</p>
<h3>PPC (pay per click)</h3>
<p>Any ad model where you pay per click. Usually shorthand for Google Ads or Microsoft Ads search campaigns. When a Houston agency says “we do PPC,” this is what they mean. See {L('/blog/are-microsoft-ads-worth-it-small-business/', 'whether Microsoft Ads are worth it')}.</p>
<h3>Primary category</h3>
<p>The main category on your Google Business Profile, and one of the strongest local ranking signals. A Conroe roofer should pick “Roofing contractor,” not “Contractor.”</p>
<h3>Quality Score</h3>
<p>A 1-10 Google Ads score per keyword based on expected CTR, ad relevance and landing page experience. Google’s {SRC['qs']} calls it a diagnostic tool. A 3 on “dentist The Woodlands” usually means the landing page doesn’t mention The Woodlands or the service. See {L('/blog/google-ads-quality-score-lower-cost-per-click/', 'Quality Score and CPC')}.</p>
<h3>Reach</h3>
<p>The number of different people who saw your ad at least once. Pair it with frequency. A streaming TV campaign that reaches 40,000 households in Montgomery County four times each is a reach-and-frequency buy.</p>
<h3>Retargeting (remarketing)</h3>
<p>Showing ads to people who already visited your site or engaged with you. A Cypress pool builder retargets everyone who looked at the pricing page. See {L('/blog/retargeting-explained/', 'retargeting explained')}.</p>
<h3>ROAS (return on ad spend)</h3>
<p>Revenue divided by ad spend for a specific campaign or platform. A ROAS of 4 means $4 back for every $1 spent. Platform-reported ROAS tends to run optimistic, which is why we check it against MER.</p>
<h3>ROI (return on investment)</h3>
<p>Profit minus cost, divided by cost. Unlike ROAS, it uses profit and includes every cost, so it’s the number your accountant cares about. A Katy remodeler with a 5x ROAS on $40,000 kitchens might still lose money if the jobs run at thin margins.</p>
<!--fig:roas-->"""),

            ("S and T: Schema through Transcreation", f"""<h3>Schema (structured data)</h3>
<p>Code that labels your page content so search engines understand it: your hours, address, reviews, FAQs. Google’s {SRC['lbschema']} covers the local business version. A Tomball vet clinic’s site should mark up its address, hours and phone number this way.</p>
<h3>Search Console</h3>
<p>Google’s free tool that shows which searches your site appears for, your clicks and positions, and indexing problems. Every business should have it set up. It’s where a Woodlands CPA finds out people search “tax preparer near me” far more than “accounting firm.”</p>
<h3>Search terms report</h3>
<p>The list of actual searches that triggered your Google Ads. Reading it weekly is how you find the “plumbing school Houston” clicks you’re paying for.</p>
<h3>SERP</h3>
<p>Search engine results page. Today it can include ads, LSAs, an AI Overview, the map pack and organic results all on one screen. Search “water heater repair Houston” on a phone and organic results may not appear until the third scroll.</p>
<h3>Service area business</h3>
<p>A business that serves customers at their location and hides its address on Google, like a mobile groomer in Magnolia. You list up to 20 service areas instead.</p>
<!--fig:area-->
<h3>Smart Bidding</h3>
<p>Google’s automated bidding strategies, such as Maximize Conversions and Target CPA, which set bids per auction using conversion data. They learn from what you count, so a Sugar Land clinic counting page views as conversions trains Google to buy page views.</p>
<h3>Speed to lead</h3>
<p>How fast you respond to a new inquiry. The difference between five minutes and two hours decides a lot of Houston service jobs. See {L('/blog/speed-to-lead-response-time-follow-up-crm/', 'speed to lead')}.</p>
<h3>Target CPA</h3>
<p>A Smart Bidding strategy that aims for an average cost per conversion you set. Set it too low and the campaign stops spending. A Houston pest control company asking for $15 leads in a $60 market will watch impressions dry up.</p>
<h3>Transcreation</h3>
<p>Rewriting an ad for another language and culture, rather than translating word for word. See {L(ASIAN, 'marketing to Houston’s Asian American communities')} and {L('/blog/hispanic-marketing-houston-spanish-ads-seo/', 'Hispanic marketing in Houston')}.</p>"""),

            ("U to Z: UTM through Zero-click search", f"""<h3>UGC (user-generated content)</h3>
<p>Photos, videos and reviews made by customers instead of the brand, like a customer’s video of their new patio cover in Cypress. See {L('/blog/ugc-vs-influencers-creator-content/', 'UGC vs influencers')}.</p>
<h3>UTM parameters</h3>
<p>Tags added to the end of a link (utm_source, utm_medium, utm_campaign) so GA4 knows where a visit came from. Google’s {SRC['utm']} explains each one. Put them on every email, social post and QR code. A door hanger in Kingwood with a UTM-tagged QR code is a trackable door hanger.</p>
<!--fig:utm-->
<h3>Zero-click search</h3>
<p>A search where the person gets an answer without clicking any result: from the map pack, a phone number or an AI Overview. For a local business, a call from the map pack is a zero-click search that still pays.</p>
<p>If your reports are full of terms that don’t connect to booked jobs, we can help sort out which ones matter. <a href="/contact/">Get in touch</a> and tell us about your business and goals; a senior strategist will build a plan around them. And if you have more questions than terms, our {L(QA, 'Houston marketing Q&amp;A')} answers the common ones.</p>"""),
        ],
        "faq": [
            ("What is the difference between ROAS and MER?",
             "ROAS is revenue divided by ad spend for one campaign or platform, usually as reported by that platform. MER is total revenue divided by total marketing spend across every channel. ROAS helps you compare campaigns, while MER tells you whether marketing as a whole is working. Because platforms often over-credit themselves, Houston businesses should check ROAS against MER every month."),
            ("What is a good cost per lead for a Houston business?",
             "It depends on your industry and what a customer is worth. National Google Ads averages in 2026 ran about $67 per lead across all industries, about $91 for home services and about $132 for legal. Competitive Houston categories often run higher. A good CPL is one where your close rate and job value still leave a healthy profit after marketing costs."),
            ("What is the difference between a GA4 key event and a Google Ads conversion?",
             "A key event is an important action you mark in Google Analytics 4, such as a form submission or phone call click. Google renamed GA4 conversions to key events in 2024. A key event only becomes a Google Ads conversion when you import it into your Google Ads account, or you can track conversions directly in Google Ads with its own tag."),
            ("What does NAP mean in local SEO?",
             "NAP stands for name, address and phone number. Your NAP should match exactly across your website, Google Business Profile and directory listings like Yelp, Apple Maps and Bing. Consistent details help Google trust that your business is real and located where you say. Mismatched phone numbers or old addresses are a common problem for Houston businesses that have moved."),
            ("What are UTM codes and why do they matter?",
             "UTM codes are tags added to the end of a link, such as utm_source and utm_campaign, that tell Google Analytics where a visitor came from. They let you see which email, social post, QR code or print piece drove traffic and leads. Without them, much of that traffic shows up as direct or unassigned, and you can’t tell what worked."),
        ],
        "figures": {
            "funnel": {
                "type": "funnel",
                "title": "The funnel of metrics",
                "stages": [["Impressions: CPM, reach, frequency", "Seen"], ["Clicks: CTR, CPC", "Visited"], ["Leads: CVR, CPL", "Asked"], ["Customers: close rate, CAC", "Bought"], ["Revenue: ROAS, MER, ROI", "Paid"]],
                "alt": "Funnel showing how digital marketing metrics like CPM, CTR, CPC, CPL, CAC, ROAS and MER connect for Houston businesses",
                "caption": "Each stage has its own metrics. The lower in the funnel, the closer the number is to money.",
            },
            "worked": {
                "type": "stats",
                "title": "One month, worked through",
                "stats": [["$5.45", "CPC: $3,000 spend, 550 clicks"], ["8.2%", "CVR: 45 leads from 550 clicks"], ["$67", "CPL: $3,000 / 45 leads"], ["$250", "CAC: 12 customers from 45 leads"]],
                "note": "Illustrative example",
                "alt": "Worked example of CPC, conversion rate, cost per lead and customer acquisition cost for a The Woodlands business",
                "caption": "Same $3,000, four different numbers. Only the last one tells you if it was worth it.",
            },
            "local": {
                "type": "checklist",
                "title": "Local SEO terms in one checklist",
                "sub": "What each term looks like done right",
                "items": ["GBP: verified, complete, right primary category", "NAP: identical everywhere", "Citations: Apple Maps, Bing, Yelp, Chamber", "Reviews: steady, recent, all replied to", "Schema: LocalBusiness markup on the site", "Service pages: one per service", "Map pack: tracked by area, not one spot", "Search Console: connected and checked monthly"],
                "alt": "Checklist of local SEO terms like GBP, NAP, citations and schema for Houston and The Woodlands businesses",
                "caption": "Most of local SEO is these eight things, kept up month after month.",
            },
            "roas": {
                "type": "compare",
                "title": "Platform metrics vs. business metrics",
                "left": {"title": "What platforms report", "items": ["Impressions and reach", "CTR and CPC", "Platform ROAS", "Conversions as the platform counts them", "Engagement and video views"]},
                "right": {"title": "What pays the bills", "items": ["Booked jobs or sales", "CPL from your CRM", "CAC across every cost", "MER across all channels", "ROI after margin"]},
                "alt": "Comparison of ad platform metrics versus business metrics like CAC, MER and ROI for Houston businesses",
                "caption": "Use the left column to fix campaigns. Use the right column to decide budgets.",
            },
            "utm": {
                "type": "steps",
                "title": "How a click becomes a conversion",
                "sub": "The tracking terms, in order",
                "steps": [["UTM or GCLID", "The link carries where the visit came from."], ["GA4 event", "The visit and actions get recorded."], ["Key event", "You mark the form or call as important."], ["Conversion", "Imported into Google Ads, it trains Smart Bidding."], ["Offline conversion", "CRM sales sent back so bidding learns what paid."]],
                "alt": "Steps showing how UTM tags, GA4 events, key events and conversions connect for a Houston business",
                "caption": f"Google’s {SRC['utm']} and {SRC['keyev']} cover the first three steps.",
            },
            "area": {
                "type": "map",
                "title": "Radius, service area and proximity",
                "sub": "Example: a business based in The Woodlands",
                "highlight": ["The Woodlands", "Spring", "Conroe", "Tomball", "Magnolia", "Shenandoah"],
                "note": "Illustrative example",
                "alt": "Map of an example service area and radius targeting around The Woodlands, Spring, Conroe, Tomball and Magnolia",
                "caption": "Ads use a radius or listed towns; map rankings depend on distance from the searcher.",
            },
        },
    },
]
