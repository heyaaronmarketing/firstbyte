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
<p>Spanish-language marketing works when Spanish gets treated as its own channel. That means Spanish keywords and ads, Spanish pages at their own URLs, a Google Business Profile a Spanish speaker can actually read, and somebody who picks up the phone and answers in Spanish. Owners almost always ask us about the ads first. We’d start with the phone and work backward.</p>
<p>Below is how each piece works in 2026, including a September Google Ads change most Spanish campaigns haven’t caught up with.</p>"""),

            ("How many Houston customers speak Spanish at home?", f"""<p>More than most owners guess.</p>
<p>According to {S1['qfh']}, 46.1% of Harris County residents are Hispanic or Latino, and 45.0% of residents age 5 and up speak a language other than English at home. Montgomery County, where we’re based, is 30.2% Hispanic per {S1['qfm']}. Inside Houston city limits, the {S1['coh']} built on the 2020-2024 American Community Survey counts 808,128 residents age 5 and older who speak Spanish at home, or 37%. For the whole metro, the {S1['ghp']} put it at 29.5% speaking Spanish at home.</p>
<!--fig:market-->
<p>The trap is assuming Hispanic and Spanish-dominant mean the same audience. They don’t. In its 2023 report, {S1['pew']} found that 75% of U.S. Latinos say they can carry on a conversation in Spanish pretty well or very well. Among third-generation-or-later Latinos, though, 65% say they can’t. And 72% of second-generation Latinos say they use Spanglish at least sometimes.</p>
<p>A customer in Cypress whose grandparents came up from Monterrey is probably reached just fine by your English campaigns. A family that landed in Gulfton three years ago needs Spanish from the ad all the way to the invoice. We plan by language. Never by last name.</p>
<p>To size it for your shop, pull your last 200 calls or CRM records and count who asked for Spanish. Around 5% calls for a solid Spanish page and one bilingual person on the phone. Closer to 30%, you want a full Spanish program.</p>"""),

            ("Spanish Google Ads after the September 2026 language change", f"""<p>Until this fall, every Search campaign had a language setting, and the standard advice was to build a Spanish campaign and set it to Spanish. Google’s {S1['glang']} says it judges which languages someone understands from the search term, their language settings and preferences.</p>
<p>In September 2026 the campaign-level language setting for Search went away. Per the same page, “Search ads will automatically match based on the language of your ads,” and Google prioritizes ads that match the language of the search term. In Performance Max, the setting no longer applies on the Search Network, though it still governs YouTube, Display, Discover and Gmail. {S1['tw']} points out a gap: Google hasn’t announced reporting that shows which language an ad actually served in.</p>
<p>What we’re doing in our own accounts:</p>
<ul><li><b>Spanish still gets its own campaign.</b> Targeting used to be the reason. Now it’s budget and reporting: when Spanish and English ad groups share a budget, one starves the other, and you can’t tell which paid off.</li>
<li>Ads and landing pages are written in Spanish, since those are now the main signals Google reads. A Spanish ad pointing at an English page is a mismatch Google can see.</li>
<li>Someone reads the auto-generated text. If AI Max or automatically created assets are on, check what Google wrote; TechWyse flags that generated creative in one language can serve to a searcher using another.</li>
<li>Location goes to “Presence.” Google’s {S1['gloc']} default to “Presence or Interest,” which pulls in people who are merely curious about Houston.</li></ul>
<p>Then build keywords the way people really search, which is messier than textbook Spanish.</p>
<div class="bp-tbl"><table>
<thead><tr><th>How they search</th><th>Examples</th><th>Where it goes</th></tr></thead>
<tbody>
<tr><td>Spanish</td><td>plomero cerca de mi, dentista en Pasadena TX, aseguranza de carro barata</td><td>Spanish campaign, Spanish landing page</td></tr>
<tr><td>Spanglish</td><td>dentista near me, roofing en español, mecánico near me</td><td>Spanish campaign; these show up in the search terms report, so add the good ones</td></tr>
<tr><td>English, Spanish intent</td><td>spanish speaking dentist houston, bilingual lawyer near me</td><td>Own ad group, English ad that says “Se habla español,” bilingual page</td></tr>
<tr><td>Brand</td><td>your name + “en español”</td><td>Brand campaign, Spanish page</td></tr>
</tbody></table></div>
<p>“Aseguranza” is why a native speaker should build the list. It’s everyday Texas Spanish for insurance. A translator trained on formal Spanish writes “seguro” and misses half the searches.</p>
<p>Our favorite row is the third. “Spanish speaking ___ near me” is typed in English, the intent couldn’t be clearer, and in many trades almost nobody bids on it. We’ve usually seen Spanish CPCs come in under English ones in Houston service categories, but that’s our experience, not a published benchmark. Run Keyword Planner on your own zip codes. Our <a href="/blog/plumbing-seo-keywords-houston/">plumbing keyword guide</a> has a worked Spanish cluster, and our <a href="/services/search-marketing/">search marketing team</a> builds these accounts every week.</p>"""),

            ("Translation vs transcreation: why word-for-word Spanish ads flop", f"""<p>Translation swaps the words. Transcreation rewrites the message so it hits a Spanish speaker the way the English version hits an English speaker, and for ads it’s the only version that pulls its weight.</p>
<p>We fix the same things over and over. A literal “free estimates” is grammatically fine, but plenty of Houston customers say “cotización gratis.” “Licensed and insured” should name the Texas license, since someone calling a stranger in their second language leans harder on proof. Register trips people up too. “Usted” is polite and safe for most service businesses; “tú” suits a gym or a taquería with a younger crowd. Pick one and stick with it everywhere.</p>
<!--fig:transcreate-->
<p>Spanish runs longer than English. Write Spanish headlines to the 30-character limit from scratch rather than cramming a translation in.</p>
<p>And Houston isn’t one dialect. It’s heavily Mexican-heritage, with big Central American communities on top of that, so plain neutral Spanish with a few Texas terms is the safe middle. Before anything goes live we’d have a native speaker who lives here read every ad, page and phone script. Machine translation is a perfectly good first draft (we use it). We’ve never seen it survive as the last one.</p>"""),

            ("Bilingual website SEO: /es/ pages, hreflang and the translate widget", f"""<p>If your Spanish plan is a Google Translate dropdown, you don’t have Spanish pages as far as search is concerned. The widget translates in the visitor’s browser; there’s no Spanish URL for Google to crawl, rank or send an ad to.</p>
<p>Google’s {S1['gsc']} recommends “using different URLs for each language version of a page” rather than switching language with cookies or browser settings. The same page tells you to skip automatic redirects based on a guessed language, link the language versions to each other, and keep each page in one language instead of running translations side by side.</p>
<p>For a small business site, that works out like this.</p>
<ul><li>Put Spanish pages in a folder, like <i>/es/plomeria/</i> next to <i>/plumbing/</i>. It’s the simplest setup to manage and to point ads at.</li>
<li>Add hreflang so each English page names its Spanish twin and the reverse (“en-us” and “es-us”, plus an x-default). Each page lists both versions, itself included, or Google ignores the pair.</li>
<li>Put a plain “Español” link in the header and skip auto-redirects; a bilingual customer with an English phone may still want the Spanish page.</li>
<li>Translate the title tag, meta description, alt text, form labels, error messages and the thank-you page. Everybody forgets the thank-you page.</li></ul>
<!--fig:pages-->
<p>You don’t need the whole site in Spanish on day one. Start where the money is, which for most shops means the top few services, the contact page and a page per service area. A Spanish page for Pasadena or Channelview will out-earn a Spanish “About us” every time. Our post on <a href="/blog/power-of-local-landing-pages/">local landing pages</a> covers the structure, and our <a href="/services/web-design-seo-pr/">web design and SEO</a> team builds bilingual sites this way.</p>"""),

            ("Google Business Profile in Spanish: what’s possible and what isn’t", f"""<p>There’s no Spanish toggle in Google Business Profile, and a few of the obvious workarounds will get you in trouble.</p>
<p>Google’s {S1['gbpg']} rule out “repeating the same business name in multiple scripts or languages,” and they allow one profile per location. So “Rodriguez Plumbing / Plomería Rodriguez” is out as a name, and a second Spanish profile at the same address is a duplicate. If your sign and website genuinely say both, talk to someone before touching the name field.</p>
<p>What you can do:</p>
<ul><li>Write a bilingual description. You get 750 characters, so lead with your primary language and follow with a short Spanish version.</li>
<li>Publish Spanish posts as their own posts, linking to the Spanish page. Nothing translates them for you.</li>
<li>Ask Spanish-speaking customers for reviews in Spanish (send the request by text, also in Spanish), and reply in whatever language the review came in.</li>
<li>Check for <b>language attributes</b> under Edit profile. Some categories now let you list languages your staff speak, and in {S1['lsf']} a GBP specialist called them a cleaner fix than splitting the profile.</li>
<li>Photograph your Spanish signage, if you really have some. “Se habla español” on the front door does more than you’d think.</li></ul>
<p>For phones set to Spanish, Google translates standardized fields like categories and hours itself. Free-text fields stay as you typed them, hence the Spanish paragraph in the description. For the rest of the profile, our <a href="/blog/google-business-profile-number-one-asset/">Google Business Profile guide</a> covers the basics.</p>"""),

            ("Facebook and Instagram ads in Spanish", f"""<p>Meta used to offer a “Hispanic Affinity” targeting option. {S1['bbg']} that Facebook retired it in August 2020. Good riddance, frankly; ethnicity was the wrong proxy for the Pew reasons above.</p>
<p>Language and place do the job better. The ad set’s audience controls include a Languages field that almost everyone leaves blank. For a Spanish campaign, set it to Spanish (All) and run Spanish creative. Meta also supports {S1['mml']}, where one ad carries several language versions and each viewer sees the one matching their settings. We still prefer separate ad sets for an ongoing program, for clean budgets and reporting.</p>
<p>On Meta, though, the creative decides most of it.</p>
<ul><li>Shoot your own staff and trucks on actual Houston streets. A stock “Hispanic family” in a beige kitchen reads as fake to everybody, Hispanic or not.</li>
<li>Have the bilingual tech or front-desk person talk to the camera in Spanish. A 30-second phone video usually beats the polished one.</li>
<li>Build the instant form in Spanish, down to the thank-you screen, and make sure whoever calls the lead back speaks Spanish.</li>
<li>Caption everything. Lots of people scroll with the sound off.</li></ul>
<p>Ads in Meta’s special ad categories (housing, employment, credit or financial products) get even tighter targeting limits, so language and creative carry more weight. Our <a href="/services/paid-social-advertising/">paid social team</a> handles those reviews.</p>"""),

            ("Spanish-language radio, TV and streaming in Houston", f"""<p>Houston has a deep Spanish-language media market. For some businesses it’s the one place in this guide where broad reach is still cheap enough to test.</p>
<ul><li>{S1['kxln']}, licensed to Rosenberg and owned by TelevisaUnivision, carries UniMás on its second channel.</li>
<li>{S1['ktmd']} belongs to NBCUniversal’s Telemundo Station Group and is licensed to Galveston.</li>
<li>{S1['kltn']} plays Regional Mexican under TelevisaUnivision’s Uforia group.</li>
<li>{S1['kove']} is Spanish adult contemporary, also Uforia, also licensed to Galveston.</li></ul>
<p>Spanish streaming, TelevisaUnivision’s ViX for one, is reachable through programmatic connected TV.</p>
<p>We’d hold off on radio until Spanish search, Spanish pages and the phones work. Radio makes people search for you, and if that search lands on an English-only site, you’ve paid for a competitor’s lead. After that, a two-month test with its own tracking number is fair. Our <a href="/blog/radio-tv-advertising-cost-houston/">Houston radio and TV cost guide</a> has the pricing side, and our <a href="/services/ctv-ooh-streaming-radio/">CTV, streaming and radio</a> page covers how we buy it.</p>"""),

            ("Answering the phone in Spanish (where most campaigns break)", f"""<p>This is the part most shops get wrong, and it’s the cheapest one to fix.</p>
<p>A Spanish-speaking caller who hits an English greeting, a buried menu option or an English-only voicemail does not leave a message. They call the next ad.</p>
<!--fig:phones-->
<p>For a shop with one or two bilingual people on payroll, we’d set it up roughly like this.</p>
<ol><li>Give the Spanish campaigns their own tracking number. You’ll know how many Spanish calls the ads produced.</li>
<li>Route that number straight to the bilingual staff first, then to the main line. No menu.</li>
<li>Record a short bilingual greeting and voicemail on every line, with Spanish in the first five seconds.</li>
<li>Put the Spanish hours in the ads (“Hablamos español, lunes a sábado”). No Spanish on Sundays? Say so.</li>
<li>Send missed-call texts in Spanish from the Spanish number.</li>
<li>Once a month, listen to a handful of Spanish calls. Did someone answer, did the job get booked, and did the caller understand the price?</li></ol>
<p>The tools are covered in our <a href="/blog/call-tracking-which-ads-make-phone-ring/">call tracking guide</a>. For what it’s worth, a part-time bilingual dispatcher is cheaper than most leaky Spanish ad budgets we’ve audited.</p>"""),

            ("Cultural do’s and don’ts that don’t rely on stereotypes", f"""<p>Most bad Hispanic marketing is lazy rather than malicious. Papel picado clip art, a mariachi stock photo, a “¡Feliz Cinco de Mayo!” post from a company that ignores Spanish the other 364 days.</p>
<p>A steady Spanish presence all year beats a burst during Hispanic Heritage Month (September 15 to October 15). People remember who was around in February.</p>
<p>Match the language the customer chose, every time. If someone filled out the English form, follow up in English. Switching to Spanish because of a last name is exactly the assumption that grates on bilingual customers, and it can sting: Pew found that 54% of Latinos who speak little or no Spanish say another Latino has made them feel bad about it. Your follow-up email shouldn’t pile on.</p>
<p>Spell out price, warranty, financing and deposits in plain terms; nobody of any background likes surprises on an invoice. Where you can, feature real Spanish-speaking customers (with permission) in their own words.</p>
<p>Humor and slang stay out of the ads unless a native speaker from here wrote them.</p>"""),

            ("What Hispanic marketing in Houston costs", f"""<p>Illustrative ranges for a single-location service business in Greater Houston. They aren’t quotes, and your trade and service area move them a lot.</p>
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
<p>You may not need to hire anyone. A bilingual person in the office who likes to write can build five Spanish pages, launch one modest search campaign, fix the phones and read the search terms weekly. Bring in help once Spanish spend is real money and you can’t tell if it works, or nobody has time to write.</p>
<p>This week, count your Spanish calls. Call your own number and press nothing. Then click your Spanish ad, if you have one, and see where it lands. If you’d like a second set of eyes, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your Google or Meta budget is leaking, Spanish campaigns included, in your inbox within 48 hours.</p>"""),
        ],
        "faq": [
            ("Should I use Google Translate on my website for Spanish customers?",
             "Not as your Spanish strategy. A translate widget converts text in the visitor’s browser, so there is no Spanish URL for Google to index or for an ad to link to, and the wording is often clumsy. Google recommends separate URLs per language. Build real Spanish pages for your main services and contact page, have a native speaker review them, and pair them with hreflang."),
            ("Do Spanish Google Ads cost less than English ads in Houston?",
             "Often, though not always. Fewer advertisers bid on Spanish keywords in many service categories, so clicks tend to cost less, but there is also less search volume. Prices vary by trade and zip code, so check Keyword Planner for your own terms. What happens after the click matters more. A Spanish ad that leads to an English page or an English-only phone line throws the savings away."),
            ("Can I have a Google Business Profile in Spanish and English?",
             "Not as two profiles for one location. Google allows one profile per location and bans repeating your business name in multiple languages. You can still write a bilingual description, publish Spanish posts, collect and answer Spanish reviews, show Spanish signage in photos, and use language attributes if your category has them. Google translates standardized fields like categories and hours on its own."),
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
<p>We see some version of that at most Houston energy, industrial and oilfield services companies. The marketing work is real enough, but the report counts the wrong thing, and the sales cycle is so long that by the time a deal closes nobody remembers which campaign or trade show started it.</p>
<p>Industrial B2B marketing in Houston works when you aim at the whole buying committee and plan for a long cycle. In practice that usually means LinkedIn for named accounts and job titles, Google Ads for the handful of searches that signal a live project, and technical content that engineers will actually read. Trade shows like OTC produce meetings. A CRM has to track pipeline, because form fills tell you very little.</p>
<p>Below: how we’d set up each piece, current costs, and where firms throw money away.</p>"""),

            ("Long sales cycles and buying committees: who you’re really selling to", f"""<p>A pump, a coating contract or a turnaround crew is rarely bought by one person. At an operator, a midstream company or a Ship Channel plant, the decision usually touches engineering, operations, procurement and safety, and someone above them signs. Add vendor prequalification (many operators require contractors to be approved through platforms like ISNetworld or Avetta before a PO can be cut) and an MSA that legal has to bless, and six months is fast.</p>
<p>Each of them reads your marketing looking for something different.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Role</th><th>What they care about</th><th>Content that answers it</th></tr></thead>
<tbody>
<tr><td>Engineer / technical lead</td><td>Specs, tolerances, standards, compatibility</td><td>Spec sheets, drawings, data sheets, test reports</td></tr>
<tr><td>Operations or maintenance manager</td><td>Downtime, response time, crew quality</td><td>Case studies with timelines, service area map, response guarantees</td></tr>
<tr><td>Procurement / supply chain</td><td>Price, lead times, terms, approved vendor status</td><td>Capability statement, line card, certifications, insurance limits</td></tr>
<tr><td>HSE</td><td>Safety record and programs</td><td>EMR, TRIR, safety program summary, prequal status</td></tr>
<tr><td>Executive sponsor</td><td>Risk, cost over the life of the asset</td><td>Short ROI case study, references, company stability</td></tr>
</tbody></table></div>
<p>Most industrial websites talk to exactly one of these people, usually the engineer, usually through a PDF from 2017. Firms that land the longer contracts tend to give every role something they can forward down the hall.</p>
<p>Buyers are less local than you’d think, too. Houston is where many of them work, from the Energy Corridor along I-10 to Greenspoint and ExxonMobil’s campus in Spring, which {S2['xom']} reported would become its corporate headquarters. But an oilfield services firm based in Conroe may also sell into Midland, Lafayette and Oklahoma City. Your targeting should follow the buyers. Where your yard happens to be is mostly irrelevant.</p>"""),

            ("LinkedIn Ads for B2B: targeting, formats and cost", f"""<p>LinkedIn is the only major ad platform where you can say “show this to maintenance managers and reliability engineers at these 150 companies” and have it mostly work. That’s why it’s expensive.</p>
<h3>Targeting that matters for energy and industrial firms</h3>
<p>Campaign Manager lets you target by company name, industry and company size, then layer on job title, function, seniority or skills. Start with titles and functions. Skills targeting gets broad fast.</p>
<p>The more useful tool for most industrial firms is a Matched Audience built from a company list. Per {S2['licl']}, a CSV can hold up to 300,000 records, audiences take 24 to 48 hours to build, and a campaign can serve once the list matches at least 300 members. LinkedIn suggests 1,000+ companies for best results. Most Houston service firms don’t have 1,000 realistic targets, and a list of 150 named operators still works; expect to pay more for it. You can also upload CRM contacts and retarget people who looked at your spec sheet pages.</p>
<p>Before launch, uncheck Audience Expansion and look hard at the LinkedIn Audience Network setting. Both push delivery past the people you chose, which is the opposite of what a tight industrial audience needs.</p>
<h3>Formats worth testing</h3>
<p>{S2['lidoc']} let people read a document in the feed, and you can gate it behind a lead form or share it openly. A six-page technical brief on, say, corrosion under insulation inspection intervals is a good fit. {S2['lilgf']} pre-fill from the member’s profile, so a field engineer on a phone doesn’t have to thumb-type into your website form. LinkedIn says 90% of its pilot customers beat their cost-per-lead goals with them (a vendor stat, so weigh it accordingly).</p>
<h3>How much do LinkedIn ads cost for B2B?</h3>
<p>Per {S2['libud']}, the minimum daily budget is $10 for any format, and a new campaign needs at least a $100 lifetime budget. Those minimums are not a realistic budget. {S2['meta']}, drawn from 138 advertisers on LinkedIn in 2025, show what real spend buys:</p>
<!--fig:linkedin-->
<p>At around $200 a lead, a $5,000 month buys roughly 25 leads, and a few of those will be students, competitors or somebody trying to sell you software. Fine if your average contract is $250,000. Painful if you sell $3,000 jobs. We’d point LinkedIn money at a defined account list and let Google pick up the broader demand. Our <a href="/services/paid-social-advertising/">paid social team</a> runs LinkedIn alongside Meta for exactly this reason.</p>"""),

            ("Google Ads for high-intent industrial searches", f"""<p>Industrial search volume is tiny, and we’ve stopped apologizing for it. One search for “hydrostatic testing services houston” or “api 6a gate valve supplier” from the right person beats a thousand LinkedIn impressions.</p>
<p>We build these accounts on exact and phrase match, pairing services with locations and products with spec terms: part numbers, standards (API, ASME, NACE), material grades, “rental,” “repair,” “supplier,” “near me,” plus city names like Pasadena, Baytown, La Porte and Channelview.</p>
<p>The negative keyword list goes in on day one, and it’s long. Jobs, careers, salary, training, certification, course, OSHA 10, PDF, free, used, Wikipedia, definition. Nothing attracts job seekers and students quite like industrial search terms.</p>
<ul><li>Set location to “Presence.” {S2['gloc']} shows the default is “Presence or Interest,” which counts people merely interested in your area. For a field service company that’s wasted spend.</li>
<li>Leave <b>Performance Max</b> off until you have real conversion data. On a handful of conversions a month it has nothing to learn from and drifts toward cheap, irrelevant traffic.</li></ul>
<p>And send product searches to product pages, never the homepage or the capability PDF.</p>
<p>Microsoft Advertising deserves a test here. Its LinkedIn profile targeting lets you adjust search bids by company, industry and job function, and plenty of corporate desktops in Houston still default to Bing.</p>
<p>A word on the {S2['meta']}: their Google Ads cost per lead was $524, well above LinkedIn’s $202. We wouldn’t conclude much from that. Search leads often show up with a project already in hand, so we’d compare channels on opportunities and revenue and treat cost per form as a footnote. For local CPC context, see our <a href="/blog/google-ads-cost-per-click-houston-benchmarks/">Houston CPC benchmarks</a> and our <a href="/services/search-marketing/">search marketing</a> service.</p>"""),

            ("Technical content engineers actually use: spec sheets, case studies, capability statements", f"""<p>An engineer wants to know whether your product will work in their application, and would rather find out without a sales call. Brochures don’t help much with that.</p>
<p>Start with spec sheets. One buried in a PDF is invisible to search and miserable on a phone, so put the specs on an HTML page and offer the PDF as a download. Don’t gate it.</p>
<p>Case studies need real numbers: the problem, the constraints, what you did, how long it took. “Completed a 21-day turnaround scope in 17 days” will get forwarded; “delivered exceptional value” won’t. Get the client’s written approval, or anonymize it if they won’t be named.</p>
<ul><li>A <b>capability statement</b>, one or two pages, covering what you do and where, NAICS codes, certifications (ISO 9001, API Q1 or Q2, ASME stamps, whatever applies), insurance limits, EMR and TRIR, prequal platforms and a contact. Procurement will ask for it regardless, so put it on the site.</li>
<li>A line card if you distribute: brands, product lines, stocking locations.</li>
<li>Application notes on narrow problems like sour service, high-temperature sealing or H2S monitoring. Unglamorous, and they’re the pages that rank for long-tail technical searches.</li>
<li>Service area and response-time details for field crews, ideally on a map.</li></ul>
<p>Save the gate for the deep material, like a detailed technical guide, a calculator or a webinar recording. Gate a spec sheet and the engineer just goes to a competitor who didn’t.</p>
<p>For energy tech and SaaS firms selling into operators, the same structure applies, with product demos in place of spec sheets; our <a href="/industries/technology/">technology industry</a> page covers that side.</p>"""),

            ("Account-based marketing for a target list of operators", f"""<p>ABM sounds like enterprise software. For a 40-person industrial firm it’s mostly a spreadsheet and some discipline.</p>
<!--fig:abm-->
<p>The list matters more than anything. Fifty accounts that actually buy what you sell, in places you can serve, beat 2,000 pulled from a database. Pick them with your sales team, not for them.</p>
<p>We’d also push hard for sales and marketing to sit down with the same account list every two weeks. LinkedIn’s reporting shows which companies are seeing and clicking your ads, so when five people at one target account are suddenly reading your document ad, your salesperson has a reason to call and something specific to say.</p>
<p>ABM ads with no sales follow-up, filed under “brand awareness,” are a slow way to spend a year’s budget. We’ve watched it happen at more than one industrial company.</p>"""),

            ("Trade shows in Houston: OTC and the rest of the calendar", f"""<p>The Offshore Technology Conference is the big one. {S2['otc']} and {S2['aime']} list OTC 2027 for May 3 to 5, 2027, in Houston at NRG Park (the 2027 toolkit still uses the venue’s old name, Reliant Park). Houston also hosts CERAWeek every March and the Turbomachinery and Pump Symposium, among many smaller regional shows. Check each show’s site for the current year’s dates before you book anything.</p>
<p>Shows are expensive, and in our experience most of the waste happens in the weeks after the booth comes down. A timeline we’d use:</p>
<ol><li><b>Four weeks out:</b> start a LinkedIn campaign to your account list and to relevant titles in Greater Houston, with your booth number and a link to book a meeting. Pre-booked meetings are the whole game.</li>
<li><b>Two weeks out:</b> email customers and open opportunities with something specific to see at the booth, like a live demo or a technical session.</li>
<li><b>Show days:</b> scan badges into a form that tags each contact with the show name and a note on what they asked about. A location-based campaign around NRG Park can add reach, but keep expectations modest; our <a href="/blog/geo-fencing-ads-target-customers-nearby/">geofencing guide</a> explains why.</li>
<li><b>Within five business days:</b> follow up with every scan, personally for the good ones. Load them into the CRM tagged “OTC 2027” so you can see what the show produced 12 months later.</li></ol>
<p>Can’t justify a booth? Walk the floor with a full meeting schedule. A surprising number of good industrial relationships started in a hallway near the coffee line.</p>"""),

            ("Getting leads into the CRM and out to sales", f"""<p>Plenty of B2B campaigns die right here, quietly. The lead exists. It’s sitting in a LinkedIn CSV download or a shared inbox nobody opens.</p>
<p>Wire every lead source straight into the CRM. LinkedIn Lead Gen Forms sync with HubSpot, Salesforce and others, and website forms should write a CRM record rather than just firing off an email. Add hidden fields for UTM parameters and the Google click ID (gclid) so each record carries the campaign, keyword or ad that produced it.</p>
<ul><li>Write down what counts as a qualified lead, who calls it and how fast.</li>
<li>Route by territory or product line. A Permian inquiry shouldn’t sit in the Gulf Coast rep’s queue for a week.</li>
<li>Close the loop. When an opportunity is created or won, send it back to Google Ads (offline conversion import) and LinkedIn (Conversions API or offline uploads) so the platforms learn which clicks turned into business.</li>
<li>Recheck the form fields quarterly. Someone always adds a mandatory “budget” dropdown.</li></ul>
<p>Honestly, we’d rather see a simple HubSpot setup that sales actually uses than an elaborate Salesforce instance nobody updates. Our <a href="/blog/landing-pages-101/">landing page guide</a> covers form design, which affects lead quality more than most people expect.</p>"""),

            ("Measuring pipeline, not leads", f"""<p>Lead counts are easy to inflate. Pipeline is hard to fake.</p>
<!--fig:pipeline-->
<p>The numbers we’d put on a monthly B2B report:</p>
<ul><li>Target accounts engaged (anyone from the account clicked, downloaded or met with you)</li>
<li>Meetings held with qualified contacts</li>
<li>Opportunities created, with dollar value</li>
<li>Pipeline by source (LinkedIn, search, trade show, referral, outbound)</li>
<li>Win rate and average sales cycle length</li>
<li>Cost per opportunity, alongside cost per lead</li></ul>
<p>Expect a lag. A campaign that launches in January may not show closed revenue until the following fall, which is normal in industrial sales and makes opportunity creation the best early signal you’ll get. Our posts on <a href="/blog/measure-marketing-success-metrics/">marketing metrics</a> and <a href="/blog/understanding-cost-per-lead/">cost per lead</a> make the same case for local businesses. In B2B the gap between cheap leads and good ones is just wider.</p>"""),

            ("When oil prices move, marketing budgets move", f"""<p>Anyone who has worked in Houston energy knows the pattern. Prices drop, capex gets cut, and marketing is the first line item to go.</p>
<!--fig:wti-->
<p>Per {S2['fred']}, the annual average WTI price fell from $93.17 a barrel in 2014 to $43.29 in 2016, hit $39.16 in 2020, rebounded to $94.90 in 2022, and averaged $65.39 in 2025. Service companies feel those swings on a delay, as operators adjust drilling and maintenance budgets.</p>
<p>Nobody knows where the price goes next, whatever your brother-in-law at the operator says. You can still plan for it.</p>
<p>Keep a floor. Cut ad spend if you must, but keep the website, GBP, case studies and LinkedIn company page alive, because rebuilding visibility from zero costs more than holding it. Downturns also tend to thin out the LinkedIn and search auctions as competitors pull back, so the dollars you do keep often go further.</p>
<ul><li>Lean into efficiency in your messaging. When prices drop, operators care about cost per barrel, downtime and headcount on site, and your case studies should speak to those.</li>
<li>Widen the target list. LNG, petrochemicals, power, water and industrial manufacturing buy many of the same services. A firm that sells only to upstream operators lives and dies by the rig count.</li></ul>"""),

            ("B2B marketing budgets in Houston, and when to hire help", f"""<p>Illustrative monthly ranges for a small-to-mid-size Houston industrial firm (not quotes). A company selling multimillion-dollar contracts can justify the top end. A local service outfit usually can’t.</p>
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
<p>Something you can do this week: pull your last 20 closed deals and find out where each one first came from. If nobody knows, fix tracking before you spend another dollar. If you want an outside look at where your Google or LinkedIn budget is going, our free <a href="/contact/">Ad Spend Leak Check</a> is a 10-minute video showing where your spend is leaking, in your inbox within 48 hours. You can also see how we report results on our <a href="/case-studies/">case studies</a> page.</p>"""),
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
             "It can be, if you treat it as a place to hold meetings. OTC 2027 is scheduled for May 3 to 5 at NRG Park in Houston. Book meetings with target accounts weeks ahead, tag every scanned contact, and follow up within five business days. If a booth is out of budget, attending with a full meeting schedule often pays back better."),
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
