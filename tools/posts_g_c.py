"""Batch 7: Hispanic / Spanish-language marketing in Houston, and B2B marketing for Houston energy, industrial and oilfield services firms.

Research for post 1: Census QuickFacts (Harris and Montgomery counties, V2025 estimates and 2020-2024 ACS), City of Houston
Planning "Language Spoken at Home" table (2020-2024 ACS 5-year), Greater Houston Partnership Economy at a Glance (Oct 2023,
Oct 2024), Pew Research Center's Sept 2023 report on Latinos and the Spanish language, Google Ads "About language targeting"
(removal of the campaign-level language setting for Search starting September 2026), TechWyse write-up of that change
(Aug 14, 2026), Google Ads advanced location options, Google Search Central on multi-regional and multilingual sites, Google's
guidelines for representing your business, Local Search Forum and Synup on bilingual GBP limits, Bloomberg (via BNN) on Meta
removing Hispanic Affinity targeting (Aug 2020), Meta Marketing API multi-language ads doc, Wikipedia entries for KXLN-DT,
KTMD, KLTN and KOVE-FM.
Research for post 2: LinkedIn "maximize your budget" page ($10 daily minimum, $100 lifetime minimum), LinkedIn Marketing API
company list docs (300,000 records per CSV, 300 matched members, 24-48 hours), LinkedIn document ads and Lead Gen Forms pages,
Metadata.io 2025 B2B advertising benchmarks, OTC 2027 social media toolkit and AIME event page (May 3-5, 2027), FRED annual
WTI prices 2014-2025, Community Impact on ExxonMobil's move to its Spring campus, Google Ads advanced location options.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

S1 = {
    "qfh": A("https://www.census.gov/quickfacts/fact/table/harriscountytexas,montgomerycountytexas,houstoncitytexas/PST045224", "Census QuickFacts"),
    "qfm": A("https://www.census.gov/quickfacts/fact/table/montgomerycountytexas/PST045224", "the same Census source"),
    "coh": A("https://311.houstontx.gov/planning/Demographics/2024-council-district-tables/19-language-spoken-at-home.pdf", "City of Houston Planning table"),
    "ghp": A("https://houston.org/houston-data/economy-glance-october-2024", "Greater Houston Partnership"),
    "pew": A("https://www.pewresearch.org/race-and-ethnicity/2023/09/20/latinos-views-of-and-experiences-with-the-spanish-language/", "Pew Research Center"),
    "glang": A("https://support.google.com/google-ads/answer/1722078?hl=en", "language targeting help page"),
    "tw": A("https://www.techwyse.com/?p=77898", "TechWyse"),
    "gloc": A("https://support.google.com/google-ads/answer/1722038?hl=en", "advanced location options"),
    "gsc": A("https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites", "guidance on multilingual sites"),
    "gbpg": A("https://support.google.com/business/answer/3038177", "guidelines for representing your business"),
    "lsf": A("https://localsearchforum.com/threads/looking-for-tips-regarding-bilingual-or-multi-lingual-gbp-optimization.60374/", "a Local Search Forum thread"),
    "bbg": A("https://www.bnnbloomberg.ca/facebook-limits-ad-targeting-some-marketers-linked-to-race-1.1478700", "Bloomberg reported"),
    "mml": A("https://developers.facebook.com/docs/marketing-api/multi-language-ads", "multi-language ads"),
    "kxln": A("https://en.wikipedia.org/wiki/KXLN-DT", "Univision 45 (KXLN)"),
    "ktmd": A("https://en.wikipedia.org/wiki/KTMD", "Telemundo Houston (KTMD, channel 47)"),
    "kltn": A("https://en.wikipedia.org/wiki/KLTN", "Que Buena 102.9 (KLTN)"),
    "kove": A("https://en.wikipedia.org/wiki/KOVE-FM", "Amor 106.5 (KOVE-FM)"),
}

S2 = {
    "libud": A("https://business.linkedin.com/marketing-solutions/best-practices/ad-tips/maximize-your-budget", "LinkedIn’s own budget guide"),
    "licl": A("https://learn.microsoft.com/en-us/linkedin/marketing/usecases/matched-audiences/company-lists?view=li-lms-2024-04", "LinkedIn’s company list documentation"),
    "lidoc": A("https://business.linkedin.com/advertise/ads/sponsored-content/document-ads", "Document Ads"),
    "lilgf": A("https://business.linkedin.com/advertise/cx/21/10/lead-gen-ads", "Lead Gen Forms"),
    "meta": A("https://metadata.io/b2b-advertising-benchmarks", "Metadata.io’s 2025 B2B benchmarks"),
    "otc": A("https://2027.otcnet.org/social-media-toolkit", "OTC’s 2027 site"),
    "aime": A("https://aimehq.org/how-to-get-involved/events/offshore-technology-conference-2027", "AIME’s event listing"),
    "fred": A("https://fred.stlouisfed.org/data/ACOILWTICO", "FRED"),
    "xom": A("https://communityimpact.com/spring-klein/business/exxonmobil-announces-relocation-of-corporate-headquarters-to-city-place-in-spring/", "Community Impact"),
    "gloc": A("https://support.google.com/google-ads/answer/1722038?hl=en", "Google’s location options page"),
}

HISP = "hispanic-marketing-houston-spanish-ads-seo"
B2B = "b2b-marketing-houston-energy-industrial"

POSTS = [
    # ------------------------------------------------------------------ post 1: Hispanic marketing
    {
        "slug": HISP,
        "title": "Hispanic Marketing in Houston: Spanish Google Ads, Meta, SEO and GBP",
        "seo_title": "Hispanic Marketing in Houston: Spanish Ads & SEO",
        "desc": "Hispanic marketing in Houston, done right: Spanish Google Ads after the 2026 language change, Meta, bilingual SEO, Google Business Profile and calls.",
        "category": "Local marketing",
        "icons": ["Google Ads", "Google Business Profile", "Meta"],
        "art": "b2",
        "hero": "speech",
        "hero_alt": "Illustration of two speech bubbles for a guide to Hispanic marketing in Houston with Spanish-language ads and SEO",
        "related": ["plumbing-seo-keywords-houston", "radio-tv-advertising-cost-houston", "call-tracking-which-ads-make-phone-ring"],
        "sections": [
            (None, f"""<p>Tuesday, 7:15 p.m., somewhere off Airline Drive. A water heater quits. Someone types “plomero cerca de mi,” taps the first ad (which is in Spanish), and lands on an English homepage with a little Translate dropdown in the corner. She calls anyway. The phone menu offers Spanish as option four, after billing.</p>
<p>She hangs up and calls the next company.</p>
<p>That’s how most Hispanic marketing in Houston fails. The ad was fine. Everything after the click wasn’t.</p>
<p>Spanish-language marketing works when you treat Spanish as its own channel: Spanish keywords and ads, Spanish pages at their own URLs, a Google Business Profile that reads naturally to a Spanish speaker, and a person who can answer the phone in Spanish. Owners usually ask us about the ads first. We’d start with the phone, honestly, and then work backward.</p>
<p>Below is how each piece works in 2026, including a Google Ads change from this September that most Spanish campaigns haven’t caught up with yet.</p>"""),

            ("How many Houston customers speak Spanish at home?", f"""<p>The numbers are bigger than most owners guess, and they mislead in a specific way.</p>
<p>According to {S1['qfh']}, 46.1% of Harris County residents are Hispanic or Latino, and 45.0% of residents age 5 and up speak a language other than English at home. Montgomery County, where we’re based, is 30.2% Hispanic per {S1['qfm']}. Inside Houston city limits, the {S1['coh']} built on the 2020-2024 American Community Survey counts 808,128 residents age 5 and older who speak Spanish at home, or 37%. For the whole metro, the {S1['ghp']} put it at 29.5% speaking Spanish at home.</p>
<!--fig:market-->
<p>Now the misleading part. Hispanic and Spanish-dominant are different audiences. In its 2023 report, {S1['pew']} found that 75% of U.S. Latinos say they can carry on a conversation in Spanish pretty well or very well. Among third-generation-or-later Latinos, though, 65% say they can’t. And 72% of second-generation Latinos say they use Spanglish at least sometimes.</p>
<p>So the customer in Cypress whose grandparents moved here from Monterrey may be reached perfectly well by your English campaigns. A family that arrived in Gulfton three years ago needs Spanish from the ad all the way through the invoice. We plan by language, never by last name or ethnicity.</p>
<p>To size your own opportunity, pull your last 200 calls or CRM records and count how many people asked for Spanish. Around 5% means a solid Spanish page and a bilingual person on the phone. Around 30% means a full Spanish program.</p>"""),

            ("Spanish Google Ads after the September 2026 language change", f"""<p>Until this fall, every Search campaign had a language setting, and the usual advice was “make a Spanish campaign and set it to Spanish.” Google’s {S1['glang']} explains that it judges which languages someone understands from the search term language, their language settings and preferences.</p>
<p>Starting in September 2026, Google removed the campaign-level language setting for Search. Per the same page, “Search ads will automatically match based on the language of your ads,” and Google prioritizes ads that match the language of the search term. In Performance Max, the setting no longer applies on the Search Network, though it still governs YouTube, Display, Discover and Gmail. {S1['tw']} points out a gap: Google hasn’t announced reporting that shows which language an ad actually served in.</p>
<p>What we’re doing about it:</p>
<ul><li><b>Keep Spanish in its own campaign anyway.</b> The reason is no longer targeting. It’s budget and reporting. When Spanish and English ad groups share a budget, one starves the other and you can’t tell which one paid off.</li>
<li><b>Write the ads and the landing page in Spanish.</b> Those are now the main signals Google reads. A Spanish ad that sends people to an English page is a mismatch, and Google can see it now.</li>
<li><b>Check auto-generated text.</b> If AI Max or automatically created assets are turned on, read what Google wrote. TechWyse flags that generated creative in one language can serve to someone searching in another.</li>
<li><b>Set location to “Presence.”</b> Google’s {S1['gloc']} default to “Presence or Interest,” which includes people merely interested in Houston. Switch it.</li></ul>
<p>Then build keywords the way people actually search, which is messier than any textbook Spanish:</p>
<div class="bp-tbl"><table>
<thead><tr><th>How they search</th><th>Examples</th><th>Where it goes</th></tr></thead>
<tbody>
<tr><td>Spanish</td><td>plomero cerca de mi, dentista en Pasadena TX, aseguranza de carro barata</td><td>Spanish campaign, Spanish landing page</td></tr>
<tr><td>Spanglish</td><td>dentista near me, roofing en español, mecánico near me</td><td>Spanish campaign; these show up in the search terms report, so add the good ones</td></tr>
<tr><td>English, Spanish intent</td><td>spanish speaking dentist houston, bilingual lawyer near me</td><td>Own ad group, English ad that says “Se habla español,” bilingual page</td></tr>
<tr><td>Brand</td><td>your name + “en español”</td><td>Brand campaign, Spanish page</td></tr>
</tbody></table></div>
<p>“Aseguranza” is a good example of why native speakers should build the list. It’s everyday Texas Spanish for insurance, and a translator trained on formal Spanish would write “seguro” and miss it.</p>
<p>The “spanish speaking ___ near me” searches are our favorite. They’re in English, the intent is unmistakable, and in a lot of trades few competitors bid on them. We’ve generally seen lower Spanish CPCs than English ones in Houston service categories, but that’s our experience, not a published benchmark, so check Keyword Planner for your own zip codes. Our <a href="/blog/plumbing-seo-keywords-houston/">plumbing keyword guide</a> has a worked Spanish cluster, and our <a href="/services/search-marketing/">search marketing team</a> builds these accounts every week.</p>"""),

            ("Translation vs transcreation: why word-for-word Spanish ads flop", f"""<p>Translation swaps the words. Transcreation rewrites the message so it lands the way the English version does. For ads, only the second one works.</p>
<p>A few examples we fix all the time. “Free estimates” translated literally is fine, but “cotización gratis” is what a lot of Houston customers actually say. “Licensed and insured” needs to mention the Texas license by name, because trust carries more weight when someone is calling a company they’ve never used in a second language. And the tone matters: “usted” reads polite and safe for most service businesses, while “tú” suits a gym or a taquería with a younger crowd. Pick one and use it everywhere.</p>
<!--fig:transcreate-->
<p>Spanish also runs longer than English, so write Spanish headlines to the 30-character limit instead of squeezing a translation into it.</p>
<p>Houston’s Hispanic community isn’t one dialect either. It’s heavily Mexican-heritage, with large Central American communities too. Plain, neutral Spanish with a few Texas terms is the safe middle. We’d have a native speaker who lives here review every ad, page and script before it goes live. Machine translation is fine for a first draft. It isn’t fine as the final one.</p>"""),

            ("Bilingual website SEO: /es/ pages, hreflang and the translate widget", f"""<p>If your Spanish plan is a Google Translate dropdown, you don’t have Spanish pages as far as search is concerned. The widget translates in the visitor’s browser; there’s no Spanish URL for Google to crawl, rank or send an ad to.</p>
<p>Google’s {S1['gsc']} is direct about the alternative: it recommends “using different URLs for each language version of a page” rather than switching language with cookies or browser settings. It also says to avoid automatically redirecting people based on guessed language, to link between language versions, and to keep each page in a single language rather than side-by-side translations.</p>
<p>In practice, for a small business site:</p>
<ul><li>Put Spanish pages in a folder, like <i>/es/plomeria/</i> next to <i>/plumbing/</i>. It’s the simplest setup to manage and to point ads at.</li>
<li>Add hreflang annotations so each English page names its Spanish twin and vice versa (codes “en-us” and “es-us”, plus an x-default). Each page has to list both versions, including itself, or Google ignores the pair.</li>
<li>Put a plain “Español” link in the header. Don’t auto-redirect based on browser language; a bilingual customer with an English phone may want the Spanish page and vice versa.</li>
<li>Translate the title tag, meta description, image alt text, form labels, error messages and the thank-you page. The thank-you page is the one everybody forgets.</li></ul>
<!--fig:pages-->
<p>You don’t need the whole site in Spanish on day one. Start with the pages that make money: your top three services, a contact page, and a page for each area you serve. A Spanish page for Pasadena or Channelview will do more than a Spanish “About us.” Our post on <a href="/blog/power-of-local-landing-pages/">local landing pages</a> covers the structure, and our <a href="/services/web-design-seo-pr/">web design and SEO</a> team builds bilingual sites this way.</p>"""),

            ("Google Business Profile in Spanish: what’s possible and what isn’t", f"""<p>There’s no Spanish toggle in Google Business Profile, and a few of the obvious workarounds will get you in trouble.</p>
<p>Google’s {S1['gbpg']} list “repeating the same business name in multiple scripts or languages” as something you can’t do, and they allow one profile per location. So “Rodriguez Plumbing / Plomería Rodriguez” as the name is out, and a second Spanish-language profile for the same address is a duplicate listing. If your sign and website really do say both, talk to us before you touch the name field.</p>
<p>What does work:</p>
<ul><li><b>A bilingual description.</b> You get 750 characters. Put the primary language first and a short Spanish version after it.</li>
<li><b>Spanish posts.</b> Posts don’t translate themselves. Publish Spanish ones on their own, linking to the Spanish page.</li>
<li><b>Spanish reviews.</b> Ask Spanish-speaking customers for a review in Spanish, by text, in Spanish. Reply in the language the review was written in.</li>
<li><b>Language attributes.</b> Some categories now offer attributes about languages spoken by staff. In {S1['lsf']}, a GBP specialist pointed to these as a cleaner option than splitting the profile. Check under Edit profile to see whether yours shows them.</li>
<li><b>Photos with Spanish signage</b>, if you actually have it. “Se habla español” on the door, photographed, is a trust signal.</li></ul>
<p>Google does translate standardized fields, like categories, attributes and hours, for people whose phones are set to Spanish. Your free-text fields stay as you wrote them. That’s another reason the description should carry a Spanish paragraph. For everything else on the profile, our <a href="/blog/google-business-profile-number-one-asset/">Google Business Profile guide</a> covers the basics.</p>"""),

            ("Facebook and Instagram ads in Spanish", f"""<p>Meta used to offer a “Hispanic Affinity” targeting option. {S1['bbg']} that Facebook retired it in August 2020. We wouldn’t want it back. Ethnicity is the wrong proxy anyway, for the Pew reasons above.</p>
<p>Target by language and place instead. In the ad set’s audience controls there’s a Languages field, which is normally left blank. For a Spanish campaign, set it to Spanish (All) and pair it with Spanish creative. Meta also supports {S1['mml']}, where one ad carries several language versions and each viewer sees the one that matches their language setting. For an ongoing Spanish program we still prefer separate ad sets, so budget and reporting stay clean.</p>
<p>Creative is where Spanish ads on Meta win or lose:</p>
<ul><li>Use real staff, real trucks, real Houston streets. Stock photos of “Hispanic families” in a beige kitchen read as fake to everyone.</li>
<li>Film the bilingual tech or front-desk person talking to camera in Spanish. One 30-second phone video often beats a polished production.</li>
<li>Run instant forms in Spanish, with Spanish questions and a Spanish thank-you screen. Then make sure the person who calls the lead back speaks Spanish.</li>
<li>Add captions. Plenty of people watch with the sound off.</li></ul>
<p>If your ads fall under Meta’s special ad categories (housing, employment, credit or financial products), targeting is restricted further, so language and creative do more of the work. Our <a href="/services/paid-social-advertising/">paid social team</a> handles those reviews.</p>"""),

            ("Spanish-language radio, TV and streaming in Houston", f"""<p>Houston has a deep Spanish-language media market, and it’s the one place in this guide where broad reach is still cheap enough to test for some businesses.</p>
<ul><li>{S1['kxln']} is licensed to Rosenberg and owned by TelevisaUnivision, with UniMás on its second channel.</li>
<li>{S1['ktmd']} is owned by NBCUniversal’s Telemundo Station Group and licensed to Galveston.</li>
<li>{S1['kltn']} plays Regional Mexican and is part of TelevisaUnivision’s Uforia group.</li>
<li>{S1['kove']} is Spanish adult contemporary, also Uforia, licensed to Galveston.</li></ul>
<p>Spanish-language streaming, like TelevisaUnivision’s ViX, can be reached through programmatic connected TV.</p>
<p>Our opinion: get Spanish search, Spanish pages and the phones working before you buy a radio flight. Radio makes people search for you, and if that search lands on an English-only site, you’ve paid for someone else’s lead. After that, a two-month test with a dedicated tracking number is fair. Our <a href="/blog/radio-tv-advertising-cost-houston/">Houston radio and TV cost guide</a> has the pricing side, and our <a href="/services/ctv-ooh-streaming-radio/">CTV, streaming and radio</a> page covers how we buy it.</p>"""),

            ("Answering the phone in Spanish (where most campaigns break)", f"""<p>This is the part most shops get wrong, and it’s the cheapest one to fix.</p>
<p>If a Spanish-speaking caller hits an English greeting, a buried Spanish option or an English-only voicemail, they don’t leave a message. They call the next ad.</p>
<!--fig:phones-->
<p>Here’s the setup we’d use for a shop with one or two bilingual people:</p>
<ol><li>Give the Spanish campaigns their own tracking number. You’ll know how many Spanish calls the ads produced.</li>
<li>Route that number straight to the bilingual staff first, then to the main line. No menu.</li>
<li>Record a short bilingual greeting and voicemail on every line, with Spanish in the first five seconds.</li>
<li>Put the Spanish hours in the ads (“Hablamos español, lunes a sábado”). If nobody speaks Spanish on Sundays, say so; it’s better than a confused call.</li>
<li>Send missed-call texts in Spanish from the Spanish number.</li>
<li>Score a handful of Spanish calls every month. Were they answered? Booked? Was the price explained clearly?</li></ol>
<p>Our <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking guide</a> explains the tools. A part-time bilingual dispatcher costs a lot less than a Spanish ad budget that leaks.</p>"""),

            ("Cultural do’s and don’ts that don’t rely on stereotypes", f"""<p>Most bad Hispanic marketing is lazy rather than malicious. Papel picado clip art, a mariachi stock photo, a “¡Feliz Cinco de Mayo!” post from a company that ignores Spanish the other 364 days.</p>
<p>What we’d do instead:</p>
<ul><li><b>Show up consistently.</b> A steady Spanish presence all year beats a burst during Hispanic Heritage Month (September 15 to October 15). People notice who was there in February.</li>
<li><b>Match the customer’s language, every time.</b> If someone filled out the English form, follow up in English. Sending Spanish to someone because of their last name is exactly the assumption that annoys bilingual customers. Pew found that 54% of Latinos who speak little or no Spanish say another Latino has made them feel bad about it. Don’t make language a test.</li>
<li><b>Be clear about price, warranty and payment.</b> Those questions are universal. Spell out financing, deposits and what happens if something goes wrong.</li>
<li><b>Use your real Spanish-speaking customers</b> (with permission) in reviews and testimonials, in their own words.</li>
</ul>
<p>Keep humor and slang out of ads unless a native speaker from here wrote them.</p>"""),

            ("What Hispanic marketing in Houston costs", f"""<p>These are illustrative ranges for a single-location service business in Greater Houston, not quotes. Your trade and service area change them a lot.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Typical range</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Transcreated Spanish pages</td><td>$1,500 to $5,000 one time</td><td>Top services, contact, area pages, thank-you page, native-speaker review</td></tr>
<tr><td>Spanish Google Ads spend</td><td>$750 to $3,000 a month</td><td>Its own campaign and budget; often lower CPCs than English</td></tr>
<tr><td>Spanish Meta ads spend</td><td>$500 to $2,000 a month</td><td>Language set to Spanish, Spanish instant forms</td></tr>
<tr><td>Tracking number and call routing</td><td>$50 to $150 a month</td><td>Separate Spanish number, bilingual voicemail</td></tr>
<tr><td>Bilingual phone coverage</td><td>Staff time</td><td>The piece that decides whether the rest works</td></tr>
<tr><td>Spanish radio or CTV test</td><td>Varies by station and flight</td><td>Only after the basics above are live</td></tr>
</tbody></table></div>
<p>Should you hire help? If you have a bilingual person in the office who enjoys writing, you can do much of this yourself: build five Spanish pages, launch one Spanish search campaign at a modest budget, fix the phones and read the search terms every week. Hire help when the Spanish campaign is spending real money and you can’t tell whether it works, or when nobody on staff has time to write.</p>
<p>A sensible first week: count your Spanish calls, call your own number and press nothing, and look at what your Spanish ad (if you have one) actually links to. If you’d like a second set of eyes, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your Google or Meta budget is leaking, Spanish campaigns included, in your inbox within 48 hours.</p>"""),
        ],
        "faq": [
            ("Should I use Google Translate on my website for Spanish customers?",
             "Not as your Spanish strategy. A translate widget converts text in the visitor’s browser, so there is no Spanish URL for Google to index or for ads to link to, and the translations are often clumsy. Google recommends separate URLs for each language version. Build real Spanish pages for your main services and contact page, reviewed by a native speaker, and link them with hreflang."),
            ("Do Spanish Google Ads cost less than English ads in Houston?",
             "Often, but not always. Fewer advertisers bid on Spanish keywords in many service categories, so cost per click tends to be lower, but search volume is also smaller. Prices vary by trade and zip code, so check Keyword Planner for your own terms. The bigger cost factor is what happens after the click: a Spanish ad that leads to an English page or English-only phone line wastes the savings."),
            ("Can I have a Google Business Profile in Spanish and English?",
             "Not as two separate profiles for one location. Google allows one profile per location and does not allow repeating your business name in multiple languages. You can write a bilingual description, publish Spanish posts, collect and reply to Spanish reviews, add photos of Spanish signage, and use language-related attributes if your category offers them. Google translates standardized fields like categories and hours automatically."),
            ("How do I target Hispanic customers on Facebook?",
             "Target by language and location, not ethnicity. Meta removed its Hispanic Affinity option in 2020. In the ad set audience settings, set Languages to Spanish for Spanish campaigns and pair it with Spanish creative, Spanish instant forms and a Spanish-speaking follow-up. Many Hispanic customers in Houston prefer English, so your English campaigns should already reach them with relevant, inclusive creative."),
            ("What is the difference between translation and transcreation?",
             "Translation converts the words from one language to another. Transcreation rewrites the message for the audience so it carries the same meaning, tone and persuasion, which can mean different headlines, examples or local terms. For ads and landing pages, transcreation by a native speaker who knows Houston usually performs better than a literal translation, which can sound stiff or miss common Texas Spanish words."),
        ],
        "figures": {
            "market": {
                "type": "stats",
                "title": "Spanish and Hispanic Houston, by the numbers",
                "stats": [["46.1%", "Harris County residents who are Hispanic or Latino"], ["30.2%", "Montgomery County residents who are Hispanic or Latino"], ["37%", "City of Houston residents 5+ who speak Spanish at home"], ["29.5%", "Metro Houston residents 5+ who speak Spanish at home"]],
                "note": "Sources: Census QuickFacts; City of Houston Planning (2020-2024 ACS); Greater Houston Partnership",
                "alt": "Stat tiles showing the Hispanic population share and Spanish spoken at home across Harris County, Montgomery County and Houston, context for Hispanic marketing in Houston",
                "caption": f"County figures from {A('https://www.census.gov/quickfacts/fact/table/harriscountytexas,montgomerycountytexas,houstoncitytexas/PST045224', 'Census QuickFacts')}; city figure from the {A('https://311.houstontx.gov/planning/Demographics/2024-council-district-tables/19-language-spoken-at-home.pdf', 'City of Houston')}.",
            },
            "transcreate": {
                "type": "compare",
                "title": "Spanish ad copy: translated vs transcreated",
                "left": {"title": "Literal translation", "items": ["Formal Spain-style vocabulary", "English headline squeezed to fit", "Mixes tú and usted", "Generic stock family photo", "Links to the English homepage"]},
                "right": {"title": "Transcreated for Houston", "items": ["Words people here use, like aseguranza", "Headline written to Spanish length", "One register, used everywhere", "Real staff and real Houston streets", "Links to a matching Spanish page"]},
                "alt": "Comparison of literally translated Spanish ads and transcreated Spanish ads for Hispanic marketing in Houston",
                "caption": "A native speaker who lives in Houston should review every Spanish ad and page before it runs.",
            },
            "pages": {
                "type": "steps",
                "title": "Building Spanish pages that rank",
                "sub": "The order we’d follow for a bilingual website in Houston",
                "steps": [["Pick the money pages", "Top services, contact, and one page per area you serve."], ["Transcreate, then review", "Draft any way you like; a native speaker signs off."], ["Publish at /es/ URLs", "One language per page, with its own title and meta description."], ["Add hreflang pairs", "Each English page names its Spanish twin, and the reverse, plus x-default."], ["Link and track", "Español link in the header, Spanish forms, Spanish thank-you page."]],
                "alt": "Step-by-step diagram for building Spanish pages and bilingual website SEO for Houston businesses",
                "caption": f"Based on Google’s {A('https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites', 'multilingual site guidance')}: separate URLs, no auto-redirects, one language per page.",
            },
            "phones": {
                "type": "checklist",
                "title": "Spanish call-handling check",
                "sub": "Run this before you spend another dollar on Spanish ads",
                "items": ["Separate tracking number for Spanish campaigns", "Spanish calls route to bilingual staff first", "Spanish heard in the first five seconds", "Bilingual voicemail on every line", "Spanish hours stated in the ads", "Missed-call texts sent in Spanish", "Monthly review of recorded Spanish calls"],
                "alt": "Checklist for answering Spanish-language calls, a key step in Hispanic marketing for Houston businesses",
                "caption": "Most Spanish campaigns we audit leak here, after the click, not in the ad account.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: B2B energy & industrial
    {
        "slug": B2B,
        "title": "B2B Marketing in Houston for Energy, Industrial and Oilfield Services",
        "seo_title": "B2B Marketing in Houston for Energy & Industrial Firms",
        "desc": "B2B marketing in Houston for energy, industrial and oilfield services firms: LinkedIn Ads costs, Google Ads, technical content, OTC, ABM and pipeline.",
        "category": "Strategy",
        "icons": ["LinkedIn", "Google Ads", "HubSpot"],
        "art": "b5",
        "hero": "industry",
        "hero_alt": "Illustration of an industrial plant for a guide to B2B marketing for Houston energy and oilfield services companies",
        "related": ["measure-marketing-success-metrics", "understanding-cost-per-lead", "google-ads-cost-per-click-houston-benchmarks"],
        "sections": [
            (None, f"""<p>The sales VP at a 60-person valve and actuator distributor off the Sam Houston Tollway (a hypothetical, but you’ve met him) forwards the monthly marketing report. 212 leads. He replies with one line: “Which of these turned into a PO?”</p>
<p>Nobody can answer.</p>
<p>That’s the usual state of B2B marketing in Houston’s energy, industrial and oilfield services companies. The work is real. The reporting measures the wrong thing. And the sales cycle runs long enough that by the time a deal closes, nobody remembers which campaign or trade show started it.</p>
<p>Industrial B2B marketing in Houston works when you aim at the whole buying committee and plan for a long cycle. LinkedIn reaches the named accounts and job titles. Google Ads catches the few searches that signal a live project. Technical content does the selling engineers actually want. Trade shows like OTC create the meetings, and a CRM tracks pipeline instead of form fills. Here’s how we’d set up each piece, with current costs, and where we think firms waste money.</p>"""),

            ("Long sales cycles and buying committees: who you’re really selling to", f"""<p>A pump, a coating contract or a turnaround crew is rarely bought by one person. At an operator, a midstream company or a Ship Channel plant, the decision usually touches engineering, operations, procurement and safety, and someone above them signs. Add vendor prequalification (many operators require contractors to be approved through platforms like ISNetworld or Avetta before a PO can be cut) and an MSA that legal has to bless, and six months is fast.</p>
<p>Each of those people needs something different from your marketing:</p>
<div class="bp-tbl"><table>
<thead><tr><th>Role</th><th>What they care about</th><th>Content that answers it</th></tr></thead>
<tbody>
<tr><td>Engineer / technical lead</td><td>Specs, tolerances, standards, compatibility</td><td>Spec sheets, drawings, data sheets, test reports</td></tr>
<tr><td>Operations or maintenance manager</td><td>Downtime, response time, crew quality</td><td>Case studies with timelines, service area map, response guarantees</td></tr>
<tr><td>Procurement / supply chain</td><td>Price, lead times, terms, approved vendor status</td><td>Capability statement, line card, certifications, insurance limits</td></tr>
<tr><td>HSE</td><td>Safety record and programs</td><td>EMR, TRIR, safety program summary, prequal status</td></tr>
<tr><td>Executive sponsor</td><td>Risk, cost over the life of the asset</td><td>Short ROI case study, references, company stability</td></tr>
</tbody></table></div>
<p>Most industrial websites only talk to one of these people, usually the engineer, and usually with a PDF from 2017. The firms that win longer contracts give each role something to forward to the others.</p>
<p>The buyers are also less local than you’d think. Houston is where many of them work, from the Energy Corridor along I-10 to Greenspoint and ExxonMobil’s campus in Spring, which {S2['xom']} reported would become its corporate headquarters. But an oilfield services firm based in Conroe may sell into Midland, Lafayette and Oklahoma City too. Build your targeting around where the buyers sit, not where your yard is.</p>"""),

            ("LinkedIn Ads for B2B: targeting, formats and cost", f"""<p>LinkedIn is the only major ad platform where you can say “show this to maintenance managers and reliability engineers at these 150 companies” and have it mostly work. That’s why it’s expensive.</p>
<h3>Targeting that matters for energy and industrial firms</h3>
<ul><li><b>Company and job filters.</b> In Campaign Manager you can target by company name, industry and company size, then layer job title, job function, seniority or skills. Start with titles and functions; skills targeting gets broad fast.</li>
<li><b>Matched Audiences.</b> Upload a list of target companies. Per {S2['licl']}, a CSV can hold up to 300,000 records, audiences take 24 to 48 hours to build, and a campaign can serve once the list matches at least 300 members. LinkedIn suggests at least 1,000 companies for best results, which is more than most Houston service firms have; a list of 150 named operators still works, but expect higher costs.</li>
<li><b>Contact lists and website retargeting.</b> Upload your CRM contacts and target people who visited your spec sheet pages.</li></ul>
<p>Before launch, uncheck Audience Expansion and look hard at the LinkedIn Audience Network setting. Both widen delivery beyond the people you picked, which defeats the point of a tight industrial audience.</p>
<h3>Formats worth testing</h3>
<p>{S2['lidoc']} let people read a document in the feed, and you can gate it behind a lead form or share it openly. A six-page technical brief on, say, corrosion under insulation inspection intervals is a good fit. {S2['lilgf']} pre-fill with the member’s LinkedIn profile data, which is why they convert better than sending a field engineer to a website form on a phone. LinkedIn says 90% of its pilot customers beat their cost-per-lead goals with them.</p>
<h3>How much do LinkedIn ads cost for B2B?</h3>
<p>Per {S2['libud']}, the minimum daily budget is $10 for any format, and a new campaign needs at least a $100 lifetime budget. Those minimums are not a realistic budget. {S2['meta']}, drawn from 138 advertisers on LinkedIn in 2025, show what real spend buys:</p>
<!--fig:linkedin-->
<p>At around $200 a lead, a $5,000 month buys you about 25 leads, some of which will be students, competitors and vendors. That’s fine if your average contract is $250,000. It’s a bad deal if you sell $3,000 jobs. We’d spend LinkedIn money on a defined account list and let Google handle broader demand. Our <a href="/services/paid-social-advertising/">paid social team</a> runs LinkedIn alongside Meta for exactly this reason.</p>"""),

            ("Google Ads for high-intent industrial searches", f"""<p>Industrial search volume is small. That’s fine. One search for “hydrostatic testing services houston” or “api 6a gate valve supplier” from the right person is worth more than a thousand impressions on LinkedIn.</p>
<p>How we’d build it:</p>
<ul><li><b>Exact and phrase match on service + location and product + spec terms.</b> Part numbers, standards (API, ASME, NACE), material grades, “rental,” “repair,” “supplier,” “near me,” and city names like Pasadena, Baytown, La Porte and Channelview.</li>
<li><b>A heavy negative list from day one.</b> Jobs, careers, salary, training, certification, course, OSHA 10, PDF, free, used, Wikipedia, definition. Industrial terms attract job seekers and students like nothing else.</li>
<li><b>Location set to “Presence.”</b> {S2['gloc']} shows the default is “Presence or Interest,” which includes people who are merely interested in your area. For a field service company, that wastes money.</li>
<li><b>Send product searches to product pages.</b> Not the homepage, not the capability PDF.</li>
<li><b>Keep Performance Max off</b> until you have real conversion data. With a handful of conversions a month, it has nothing to learn from and drifts toward cheap, irrelevant traffic.</li></ul>
<p>Microsoft Advertising is worth a test here. Its LinkedIn profile targeting lets you adjust bids by company, industry and job function on search campaigns, and a lot of corporate desktops in Houston still default to Bing.</p>
<p>One note on the {S2['meta']}: their Google Ads cost per lead was $524, higher than LinkedIn’s $202. Don’t read that as “Google is worse.” Search leads often arrive with a project already in hand. Judge each channel on opportunities and revenue, not cost per form. For local CPC context, see our <a href="/blog/google-ads-cost-per-click-houston-benchmarks/">Houston CPC benchmarks</a> and our <a href="/services/search-marketing/">search marketing</a> service.</p>"""),

            ("Technical content engineers actually use: spec sheets, case studies, capability statements", f"""<p>Engineers don’t want a brochure. They want the answer to “will this work in my application?” and they want it without calling a salesperson.</p>
<ul><li><b>Spec sheets as web pages, with a PDF download.</b> A spec sheet buried in a PDF is invisible to search and miserable on a phone. Put the specs in HTML, with the PDF as a download link. Don’t gate it.</li>
<li><b>Case studies with real numbers.</b> Problem, constraints, what you did, how long it took, the result. “Completed a 21-day turnaround scope in 17 days” beats “delivered exceptional value.” Get the client’s written approval, and anonymize if they won’t be named.</li>
<li><b>A capability statement.</b> One or two pages: what you do, where, NAICS codes, certifications (ISO 9001, API Q1 or Q2, ASME stamps, whatever applies), insurance limits, safety stats like EMR and TRIR, prequal platforms, and a contact. Procurement will ask for this anyway; have it on the site.</li>
<li><b>A line card</b> if you distribute. Brands, product lines, stocking locations.</li>
<li><b>Application notes.</b> Short pieces on a specific problem: sour service, high-temperature sealing, H2S monitoring. These are the pages that rank for long-tail technical searches.</li></ul>
<p>Gate only the deep stuff: a detailed technical guide, a calculator, a webinar recording. Gating a spec sheet just sends the engineer to a competitor’s site that doesn’t.</p>
<p>For energy tech and SaaS firms selling into operators, the same structure applies, with product demos in place of spec sheets; our <a href="/industries/technology/">technology industry</a> page covers that side.</p>"""),

            ("Account-based marketing for a target list of operators", f"""<p>ABM sounds like enterprise software. For a 40-person industrial firm it’s mostly a spreadsheet and some discipline.</p>
<!--fig:abm-->
<p>The list matters more than anything. Fifty accounts that actually buy what you sell, in places you can serve, beat 2,000 pulled from a database. Pick them with your sales team, not for them.</p>
<p>The other habit we’d push hard: sales and marketing looking at the same account list every two weeks. LinkedIn’s reporting shows which companies are seeing and clicking your ads. When an account on your list suddenly has five people reading your document ad, that’s a reason for your salesperson to call, with something specific to say.</p>
<p>What doesn’t work: running ABM ads with no sales follow-up and calling it brand awareness. We’ve watched that burn a year of budget at more than one industrial company.</p>"""),

            ("Trade shows in Houston: OTC and the rest of the calendar", f"""<p>The Offshore Technology Conference is the big one. {S2['otc']} and {S2['aime']} list OTC 2027 for May 3 to 5, 2027, in Houston at NRG Park (the 2027 toolkit still uses the venue’s old name, Reliant Park). Houston also hosts CERAWeek every March and the Turbomachinery and Pump Symposium, among many smaller regional shows. Check each show’s site for the current year’s dates before you book anything.</p>
<p>Trade shows are expensive, and most of the money is wasted after the show, not at it. Here’s how we’d run one:</p>
<ol><li><b>Four weeks out:</b> start a LinkedIn campaign to your account list and to relevant titles in Greater Houston, with your booth number and a link to book a meeting. Pre-booked meetings are the real goal.</li>
<li><b>Two weeks out:</b> email your customers and open opportunities. Offer something specific at the booth, like a live demo or a technical session.</li>
<li><b>Show days:</b> scan badges into a form that tags every contact with the show name and a note on what they asked about. A location-based campaign around NRG Park can add reach, but keep expectations modest; our <a href="/blog/geo-fencing-ads-target-customers-nearby/">geofencing guide</a> explains why.</li>
<li><b>Within five business days:</b> follow up with every scan, personally for the good ones. Load them into the CRM tagged “OTC 2027” so you can see what the show produced 12 months later.</li></ol>
<p>If you can’t afford a booth, walk the floor with a meeting schedule. Some of the best industrial relationships we know of started in a hallway.</p>"""),

            ("Getting leads into the CRM and out to sales", f"""<p>This is where B2B campaigns quietly fail. The lead exists, but it sits in a LinkedIn download or an inbox nobody checks.</p>
<ul><li><b>Connect lead sources directly to the CRM.</b> LinkedIn Lead Gen Forms sync with HubSpot, Salesforce and other tools. Website forms should write straight to the CRM, not just send an email.</li>
<li><b>Capture the source.</b> Hidden form fields for UTM parameters and the Google click ID (gclid), so each record shows the campaign, keyword or ad it came from.</li>
<li><b>Agree on definitions.</b> What counts as a qualified lead? Who calls it, and how fast? Write it down.</li>
<li><b>Route by territory or product line.</b> A Permian inquiry shouldn’t sit in the Gulf Coast rep’s queue.</li>
<li><b>Close the loop.</b> When an opportunity is created or won, send that back to Google Ads (offline conversion import) and LinkedIn (its Conversions API or offline uploads), so the platforms learn which clicks produced real business.</li></ul>
<p>We’d rather a client have a simple HubSpot setup that sales actually uses than a complex Salesforce instance nobody updates. Our <a href="/blog/landing-pages-101/">landing page guide</a> covers form design, which affects lead quality more than most people expect.</p>"""),

            ("Measuring pipeline, not leads", f"""<p>Lead counts are easy to inflate. Pipeline is hard to fake.</p>
<!--fig:pipeline-->
<p>The numbers we’d put on a monthly B2B report:</p>
<ul><li>Target accounts engaged (anyone from the account clicked, downloaded or met with you)</li>
<li>Meetings held with qualified contacts</li>
<li>Opportunities created, with dollar value</li>
<li>Pipeline by source (LinkedIn, search, trade show, referral, outbound)</li>
<li>Win rate and average sales cycle length</li>
<li>Cost per opportunity, alongside cost per lead</li></ul>
<p>Expect a lag. A campaign that starts in January may not show closed revenue until the following fall. That’s normal in industrial sales, and it’s why opportunity creation is the best early signal. If you’ve read our posts on <a href="/blog/measure-marketing-success-metrics/">marketing metrics</a> and <a href="/blog/understanding-cost-per-lead/">cost per lead</a>, this is the B2B version of the same idea: the cheapest leads are rarely the best ones.</p>"""),

            ("When oil prices move, marketing budgets move", f"""<p>Anyone who has worked in Houston energy knows the pattern. Prices drop, capex gets cut, and marketing is the first line item to go.</p>
<!--fig:wti-->
<p>Per {S2['fred']}, the annual average WTI price fell from $93.17 a barrel in 2014 to $43.29 in 2016, hit $39.16 in 2020, rebounded to $94.90 in 2022, and averaged $65.39 in 2025. Service companies feel those swings on a delay, as operators adjust drilling and maintenance budgets.</p>
<p>Some practical advice for planning around it:</p>
<ul><li><b>Keep a floor.</b> Cut ad spend in a downturn if you have to, but keep your website, GBP, case studies and LinkedIn company page active. Rebuilding visibility from zero costs more than holding it.</li>
<li><b>Shift toward efficiency messaging.</b> In a downturn, operators want lower cost per barrel, less downtime and fewer people on site. Your case studies should say how you deliver that.</li>
<li><b>Use the cheaper media.</b> When competitors pull out, LinkedIn and search auctions often get less crowded.</li>
<li><b>Diversify your targets.</b> LNG, petrochemicals, power, water and industrial manufacturing buy many of the same services. A firm that sells only to upstream operators lives and dies by the rig count.</li></ul>"""),

            ("B2B marketing budgets in Houston, and when to hire help", f"""<p>These are illustrative monthly ranges for a small-to-mid-size Houston industrial firm, not quotes. A firm selling multimillion-dollar contracts can justify the top of the range; a local service company often shouldn’t.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Line item</th><th>Typical monthly range</th><th>What it buys</th></tr></thead>
<tbody>
<tr><td>LinkedIn Ads</td><td>$2,500 to $10,000 in spend</td><td>Account list and title targeting, document ads, lead forms</td></tr>
<tr><td>Google Ads</td><td>$1,500 to $6,000 in spend</td><td>High-intent product and service searches</td></tr>
<tr><td>Microsoft Ads</td><td>$300 to $1,500 in spend</td><td>Desktop search with LinkedIn profile adjustments</td></tr>
<tr><td>Technical content</td><td>$2,000 to $6,000</td><td>Spec pages, case studies, application notes</td></tr>
<tr><td>CRM and tracking</td><td>Software plus setup time</td><td>Source capture, routing, offline conversion uploads</td></tr>
<tr><td>Trade shows</td><td>Varies widely</td><td>Get the exhibitor prospectus; budget for follow-up too</td></tr>
</tbody></table></div>
<p>You can do a lot of this in-house. If you have an engineer who writes clearly and a sales manager who updates the CRM, start with the capability statement, five spec pages and one Google Ads campaign with a strong negative list. Hire help when you’re spending real money on LinkedIn and Google and still can’t say which campaigns created opportunities, or when the technical content never gets written because everyone is billable.</p>
<p>A reasonable first step this week: pull your last 20 closed deals and ask where each one first came from. If nobody knows, fix tracking before you spend more. And if you want an outside look at where your Google or LinkedIn budget is going, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your spend is leaking, in your inbox within 48 hours. You can also see how we report results on our <a href="/case-studies/">case studies</a> page.</p>"""),
        ],
        "faq": [
            ("How much do LinkedIn ads cost for B2B companies?",
             "LinkedIn’s minimum is $10 a day and $100 lifetime for a new campaign, but real B2B budgets are much higher. Metadata.io’s 2025 benchmarks across 138 LinkedIn advertisers show an average cost per click of $9.39, a CPM of $63.19 and a cost per lead around $202. Most Houston industrial firms we would advise start somewhere between $2,500 and $10,000 a month in spend."),
            ("Is LinkedIn or Google Ads better for oil and gas companies?",
             "They do different jobs. LinkedIn lets you reach specific companies and job titles, so it suits account-based campaigns and long sales cycles. Google Ads catches people already searching for a product, part or service, often with a project in hand. Most energy and industrial firms benefit from both, judged by opportunities and revenue rather than cost per lead."),
            ("What should an oil and gas service company put on its website?",
             "Give each member of the buying committee something useful: spec sheets as web pages with PDF downloads, case studies with real timelines and results, a capability statement with certifications, safety statistics and insurance limits, a service area map, and clear contact options. Avoid gating spec sheets. Engineers want answers without a sales call, and procurement wants your prequalification details in one place."),
            ("How long is the sales cycle for industrial B2B sales?",
             "It varies by deal size and customer, but six to eighteen months is common for larger industrial and energy contracts, especially when vendor prequalification and a master service agreement are involved. Smaller repair or rental jobs can close in days. Plan marketing around opportunity creation as the early signal, because closed revenue may lag a campaign by a year or more."),
            ("Is the Offshore Technology Conference worth it for small companies?",
             "It can be, if you treat it as a meeting engine rather than a booth. OTC 2027 is scheduled for May 3 to 5 at NRG Park in Houston. Book meetings with target accounts weeks ahead, scan and tag every contact, and follow up within five business days. If a booth is out of budget, attending with a full meeting schedule is often the better return."),
        ],
        "figures": {
            "linkedin": {
                "type": "stats",
                "title": "LinkedIn B2B ad benchmarks, 2025",
                "stats": [["$9.39", "Average cost per click"], ["$63", "Average cost per 1,000 impressions"], ["0.67%", "Click-through rate"], ["$202", "Cost per lead"]],
                "note": "Source: Metadata.io 2025 B2B advertising benchmarks (138 LinkedIn advertisers)",
                "alt": "Stat tiles showing 2025 LinkedIn Ads cost per click, CPM, CTR and cost per lead for B2B marketing in Houston",
                "caption": f"From {A('https://metadata.io/b2b-advertising-benchmarks', 'Metadata.io')}. Spend-weighted figures; your industry and audience size will move them.",
            },
            "abm": {
                "type": "steps",
                "title": "ABM for a Houston industrial firm",
                "sub": "A version that fits a small marketing team",
                "steps": [["Build the list", "50 to 200 accounts your sales team agrees are worth winning."], ["Map the committee", "Engineering, operations, procurement, HSE and a sponsor at each."], ["Upload to LinkedIn", "Company list plus titles; check the 300-member minimum."], ["Serve role-based content", "Spec pages for engineers, capability statements for procurement."], ["Review every two weeks", "Marketing and sales look at engaged accounts together."], ["Call with a reason", "Sales reaches out to accounts showing real activity."]],
                "alt": "Step-by-step diagram of account-based marketing for Houston energy and industrial B2B companies",
                "caption": f"List limits from {A('https://learn.microsoft.com/en-us/linkedin/marketing/usecases/matched-audiences/company-lists?view=li-lms-2024-04', 'LinkedIn’s company list documentation')}.",
            },
            "pipeline": {
                "type": "funnel",
                "title": "What a quarter of ABM might produce",
                "stages": [["Target accounts", "150"], ["Accounts engaged", "60"], ["Meetings held", "18"], ["Opportunities", "9"], ["Won", "3"]],
                "note": "Illustrative example",
                "alt": "Funnel showing target accounts to won deals, measuring pipeline for B2B marketing in Houston industrial firms",
                "caption": "Illustrative numbers. The point is the shape: report each stage, not just the top.",
            },
            "wti": {
                "type": "columns",
                "title": "Average WTI oil price by year",
                "sub": "Dollars per barrel, annual average, 2014 to 2025",
                "labels": ["’14", "’15", "’16", "’17", "’18", "’19", "’20", "’21", "’22", "’23", "’24", "’25"],
                "values": [93.17, 48.66, 43.29, 50.80, 65.23, 56.99, 39.16, 68.13, 94.90, 77.58, 76.63, 65.39],
                "highlight": [6, 8],
                "y_label": "$ per barrel",
                "note": "Source: FRED, WTI Cushing annual average",
                "alt": "Column chart of annual WTI oil prices from 2014 to 2025, showing the cycles that shape B2B marketing budgets for Houston energy firms",
                "caption": f"Data from {A('https://fred.stlouisfed.org/data/ACOILWTICO', 'FRED')}. The 2020 low and 2022 high are highlighted.",
            },
        },
    },
]
