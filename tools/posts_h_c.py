"""Batch 8 (agency intent): fixing bad Facebook lead ads (fake numbers, "I never filled that out", no answer), and
whether Microsoft Ads (Bing) is worth it for a small business in 2026.

Research: Jon Loomer's instant forms guide (More Volume / Higher Intent review screen, question types, conditional
logic with Go to question / Submit form / Close form) and his lead ads features roundup (Quality filters: "Require
SMS verification to submit form", autofill toggle, Website and Instant Forms location, Messenger follow-up); Meta's
Conversions API for CRM developer docs (200 leads/month, daily upload, 28-day stage, 1-40% rate); Social Media
Examiner on conversion leads and placements; Relevant Audience on Meta's 2026 placement-control change (Leads
campaigns lose ad-set placement picks; Audience Network exclusion lives in account controls). Microsoft post:
StatCounter US search share Oct 2026 (all platforms and desktop), Microsoft Advertising search page (Comscore March
2023 claim), Microsoft Learn on Google Import and LinkedIn profile targeting, PPC Land on AI Max (Aug 19, 2026) and
Predictive Matching, JumpFly on Copilot ad types. CPC "33% cheaper" claims checked and rejected as unsourced.
"""

A = lambda url, name: f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'  # noqa: E731

SRC = {
    "loomer_forms": A("https://www.jonloomer.com/instant-forms/", "Jon Loomer’s instant forms guide"),
    "loomer_new": A("https://www.jonloomer.com/11-new-meta-lead-ads-features/", "Jon Loomer’s roundup of newer lead ad features"),
    "capi": A("https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration", "Meta’s Conversions API for CRM documentation"),
    "sme": A("https://www.socialmediaexaminer.com/how-to-capture-more-qualified-leads-with-facebook-ads/", "Social Media Examiner"),
    "placements": A("https://www.relevantaudience.com/meta/meta-placement-controls-alternatives-documented/", "Relevant Audience’s write-up of Meta’s placement change"),
    # Microsoft post
    "sc_all": A("https://gs.statcounter.com/search-engine-market-share/desktop-mobile-tablet/united-states-of-america", "StatCounter"),
    "sc_desk": A("https://gs.statcounter.com/search-engine-market-share/desktop/united-states-of-america/", "StatCounter’s desktop numbers"),
    "msa_search": A("https://about.ads.microsoft.com/en/solutions/ad-products-formats/search", "Microsoft Advertising’s search page"),
    "import": A("https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_proc_importcampaign", "Microsoft’s Google Import instructions"),
    "linkedin": A("https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_linkedintargeting", "Microsoft’s LinkedIn profile targeting page"),
    "aimax": A("https://ppc.land/microsoft-advertising-gains-ai-max-across-all-accounts-globally/", "PPC Land"),
    "predictive": A("https://ppc.land/microsoft-kills-predictive-matching-shifts-search-ads-to-ai-max/", "a July 2026 help-doc change"),
    "jumpfly": A("https://www.jumpfly.com/blog/how-to-show-ads-in-google-ai-overviews-ai-mode-and-microsoft-copilot/", "JumpFly’s breakdown"),
}

FB = "/blog/facebook-lead-ads-bad-leads-fix-quality/"
MS = "/blog/are-microsoft-ads-worth-it-small-business/"

POSTS = [
    # ------------------------------------------------------------------ post 1: bad Facebook leads
    {
        "slug": "facebook-lead-ads-bad-leads-fix-quality",
        "title": "Facebook Lead Ads Bringing Bad Leads? How to Fix Lead Quality",
        "seo_title": "Facebook Lead Ads Bad Leads? How to Fix Lead Quality",
        "desc": "Facebook lead ads bringing bad leads, fake numbers and people who never answer? The exact Meta settings, form fixes and scorecard we use in Houston.",
        "category": "Paid ads",
        "icons": ["Meta", "Facebook", "HubSpot"],
        "art": "b3",
        "hero": "filter",
        "hero_alt": "Illustration of a funnel filtering leads, for fixing Facebook lead ads bad leads at Houston and The Woodlands businesses",
        "related": ["facebook-instagram-ads-local-businesses", "understanding-cost-per-lead", "landing-pages-101"],
        "sections": [
            (None, f"""<p>It’s Monday morning. The weekend brought in 31 Facebook leads, and you feel good about that for about forty minutes. Then you start calling. Three numbers are disconnected. One is 713-555-1234. A woman in Cypress tells you she never filled anything out. Eleven go to voicemail, and the voicemail box is full on two of them.</p>
<p>If your Facebook lead ads are bringing bad leads, look hard at the setup before you blame the platform. Meta optimizes for whatever you count as a lead. Count every tap on “Submit” and it will go find the people most likely to tap Submit, who are rarely the people most likely to buy. Fixing it means a slightly harder form and questions that actually filter. Usually a different offer, too. Then somebody has to call within minutes, and once you have the volume, Meta needs your CRM results so it can learn what a good lead looks like.</p>
<p>What follows is the order we work through it for local businesses around The Woodlands and Houston, actual settings included. Fair warning, your cost per lead will go up. Your cost per <i>customer</i> should come down, and that’s the number that pays the bills.</p>"""),

            ("Why are my Facebook leads so bad?", f"""<p>Start with how an instant form works. Someone scrolling Instagram in a car line at a Spring ISD school taps your ad. A form opens inside the app, already filled in with the name, email and phone number from their profile. Two taps later, you have a “lead.” They never left the app, never saw your website, and may have been thinking about something else the whole time.</p>
<p>That convenience is what Meta is selling, and it cuts both ways. Cheap leads, lots of junk. What the junk looks like once you start dialing:</p>
<ul>
<li><b>“I don’t remember filling that out.”</b> Autofill did the work and the whole thing took eight seconds.</li>
<li>Fake or dead numbers. Some people want the freebie but not the phone call, so they make one up. Others never updated the number on their profile.</li>
<li>No answer at all. Part of that is Houston reality (plenty of people here won’t pick up an unknown number). Part of it is you calling two days later.</li>
<li>A lead from Beaumont, for a pool builder in Magnolia.</li>
</ul>
<p>The algorithm then makes it worse. With the campaign goal set to “maximize leads,” Meta’s delivery system learns who submits forms cheaply and goes looking for more people like them. Junk trains it to find more junk, and it’s very good at its job.</p>"""),

            ("More volume vs Higher intent: change the form type first", f"""<p>When you build an instant form, Meta asks you to pick a form type. The default is <b>More volume</b>, which is built to be quick to fill out and submit. The alternative is <b>Higher intent</b>, which adds a review screen where the person has to look at their information and confirm it before the form goes through, per {SRC['loomer_forms']}.</p>
<p>One extra screen sounds trivial. It catches accidental submits, though, and because the phone number is sitting right there in front of them, people with an old number on their profile tend to fix it. {SRC['sme']} recommends Higher intent for exactly this reason, unless you have another efficient way to qualify.</p>
<p>Two more switches live nearby.</p>
<p><b>SMS verification.</b> Under Quality filters, some accounts show “Require SMS verification to submit form.” The person gets a one-time code by text and has to enter it, or the submission doesn’t count as a lead. {SRC['loomer_new']} found it in three places (as a quality filter, a separate form type, and an option inside Higher intent) and says they all work the same way. If fake numbers are your main headache, this is the strongest filter Meta offers.</p>
<p>Some accounts also have an autofill checkbox on the email and phone fields. Turn it off and people have to type their real, current details. Fewer finish. The ones who do actually wanted to.</p>
<p>Meta rolls these out unevenly, so if one is missing, don’t lose a day hunting for it. Use what you have.</p>
<!--fig:formtype-->
<p>Expect your cost per lead to climb when you do this, sometimes a lot. We’ve made peace with that. A $28 lead you can reach beats a $9 lead that was never real, and the math usually works out in favor of the filtered form within a few weeks.</p>"""),

            ("How to improve Facebook lead quality with qualifying questions", f"""<p>Contact fields alone tell you nothing about whether someone is a buyer. Custom questions do. Meta’s instant forms support several question types: multiple choice, short answer, conditional questions (built from a CSV so later answers depend on earlier ones), appointment requests and sliders.</p>
<p>The part most people skip is <b>conditional logic</b>. Turn it on and each question gets a Logic column with three routes, as {SRC['loomer_forms']} lays out: <i>Go to a question</i>, <i>Submit form</i>, or <i>Close form</i>. Close form sends a non-fit person to a separate ending page without submitting their contact info. The renter in Atascocita, or the guy who wants a $200 fence, gets turned away politely and never becomes a lead you pay for or call.</p>
<p>Say you run a remodeling company in The Woodlands. A form that filters might look like this:</p>
<ol>
<li>“Which area is the home in?” Multiple choice: The Woodlands, Spring, Conroe, Magnolia, Tomball, Other. “Other” routes to Close form.</li>
<li>“Do you own the home?” Yes or No. No routes to Close form.</li>
<li>“What’s the project?” Kitchen, bathroom, whole home, other.</li>
<li>“When do you want to start?” In the next 3 months, 3 to 6 months, just researching.</li>
<li>“What budget range are you planning around?” Give real ranges that start where your jobs start.</li>
<li>One short-answer question, like “Anything we should know about the project?” Having to type a sentence filters out a surprising number of people.</li>
</ol>
<p>Keep it to four to six questions. Past that, even good prospects bail on a phone screen. And don’t make every answer a trap; “just researching” people can go into a nurture list instead of your call queue.</p>
<!--fig:build-->
<p>{SRC['sme']} notes Meta itself says conditional logic may raise cost per lead. It will. Let it.</p>"""),

            ("Offer framing that attracts freebie hunters (and what to say instead)", f"""<p>Plenty of lead problems are really offer problems. The ad does a lot of the filtering before anyone sees a form.</p>
<p>“Enter to win a free roof.” “FREE estimate, no obligation, claim yours today!” “Get a $500 gift card when you book.” Every one of these is a magnet for people who like free things. Some are buyers. Most are not, and Meta will happily find you thousands of them in Harris County alone.</p>
<p>What tends to work better for local service businesses:</p>
<ul>
<li><b>Show a price signal.</b> “Kitchen remodels in The Woodlands typically start around $45,000” scares off the people who were never going to hire you.</li>
<li>Tell them what happens next. “A project manager will call you within an hour to schedule a walkthrough.” Anyone who doesn’t want a call drops out on their own, and the rest are expecting you when the phone rings.</li>
<li>Match the ask to the size of the job. For a $15,000 pool remodel, “Book a design consult” brings fewer, better leads than “Get a free quote.”</li>
<li>Drop the giveaways unless you’re building an email list. If you are, those people are subscribers. Keep them away from your sales team.</li>
</ul>
<p>Put the same language on the form’s intro screen. The intro is where you can be blunt: “This form is for homeowners in Montgomery County planning a project in the next six months.”</p>
"""),

            ("Facebook leads not answering? Fix the first five minutes", f"""<p>A lot of “bad leads” are good leads called too late. A Facebook lead has a short memory. They submitted while scrolling, then went back to scrolling, and by Wednesday your call is just another unknown Houston number.</p>
<p>Speed starts with plumbing. If leads sit inside Meta until someone remembers to download a CSV, you lose. Options, from simplest:</p>
<ul>
<li>Email. {SRC['loomer_new']} describes a newer lead delivery option right in the form setup that emails new leads to whoever you choose. Better than nothing, barely.</li>
<li>A direct CRM integration. Meta offers direct integrations with many CRMs, and tools like HubSpot or Zapier can push each lead into your CRM and fire a text alert to whoever is on call.</li>
<li><b>An automatic text.</b> The moment the lead lands: “Hi Maria, this is Dave with Lakeside Pools. Got your request. I’ll call you from this number in the next few minutes.” Now your number isn’t a stranger.</li>
<li>Messenger. The form’s ending screen has a “Connect with leads on Messenger” option that opens a chat after they submit.</li>
</ul>
<p>Then the calls. Most of our clients run some version of this:</p>
<ol>
<li>Call within five minutes during business hours (the auto-text buys you some goodwill if it’s ten).</li>
<li>No answer: leave a short voicemail and send a text.</li>
<li>Call again that evening, around 6:30, when people are home.</li>
<li>Call and text the next morning.</li>
<li>Day 3 and day 7: one text each, then move them to email.</li>
</ol>
<p>Log every outcome in the CRM: bad number, no answer, not interested, qualified, booked. You need those labels for the next section, and for the scorecard at the end.</p>
<!--fig:leak-->
<p>If after-hours leads are a big share (they usually are for home services here, because people browse at night), an answering service or a part-time evening setter often pays for itself faster than any ad change.</p>"""),

            ("Tell Meta which leads were good: Conversions API for CRM", f"""<p>Everything so far filters on the way in. This step changes what Meta optimizes for.</p>
<p>With the Conversions API for CRM, you send your lead stages back to Meta: this lead was qualified, this one booked, this one bought. Meta can then use the “maximize number of conversion leads” goal, which {SRC['sme']} describes as built to find people more likely to convert after you follow up, even if total lead count drops.</p>
<p>The requirements rule out a lot of small businesses. Per {SRC['capi']}, you need to:</p>
<ul>
<li>Generate at least 200 leads a month.</li>
<li>Upload data at least once a day.</li>
<li>Pick a target stage that happens within 28 days of the lead.</li>
<li>Have that stage convert at between 1% and 40% of leads.</li>
</ul>
<p>A one-location HVAC company spending $2,000 a month probably isn’t at 200 leads, and that’s fine. Set up the CRM stages anyway, because clean stage data is what makes the scorecard below work, and you’ll be ready if volume grows. Many CRMs (HubSpot included) have a native Meta connection for this, so it may not need a developer.</p>
<p>Below that volume, we’d send the traffic to a landing page with your pixel and server-side events, and count only the actions you actually want (a booked appointment, a completed quote request) as the conversion. Meta then optimizes toward something closer to a sale.</p>"""),

            ("Facebook lead form vs landing page: which brings better leads?", f"""<p>Instant forms win on cost per lead. Landing pages usually win on quality. Which one you want depends mostly on how fast your team follows up and what a job is worth to you.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Instant form</th><th>Landing page</th></tr></thead>
<tbody>
<tr><td>Cost per lead</td><td>Lower</td><td>Higher</td></tr>
<tr><td>Typical lead quality</td><td>Mixed, better with Higher intent and questions</td><td>Usually better; people chose to leave the app</td></tr>
<tr><td>What the lead sees first</td><td>Your ad and a form</td><td>Your page, photos, reviews, prices</td></tr>
<tr><td>Speed to build</td><td>Minutes</td><td>Days, unless you have a template</td></tr>
<tr><td>Tracking</td><td>Inside Meta; needs CRM sync for quality</td><td>Pixel, Conversions API, analytics, call tracking</td></tr>
<tr><td>Best for</td><td>Lower-ticket offers, quick bookings, fast follow-up teams</td><td>Big-ticket jobs, regulated services, slower sales cycles</td></tr>
</tbody></table></div>
<p>There’s also a hybrid. {SRC['loomer_new']} describes a “Website and Instant Forms” conversion location where Meta can send each person to whichever one it predicts will work. We’d only try it once both versions work well on their own.</p>
<p>If you go the landing page route, build a page for this ad. (Send it to your homepage and you’re paying for people to read your About page and leave.) One offer, one form, a phone number, real photos of your work in Houston-area homes, and reviews. Our {f'<a href="/blog/landing-pages-101/">landing pages guide</a>'} covers the structure.</p>
<p>For most home service and medical clients, we start with a filtered Higher intent form because it’s fast to test, then add a landing page version beside it once there’s budget for two ad sets. Compare them on cost per booked appointment. Cost per lead will mislead you here.</p>"""),

            ("Audience and placement settings that quietly hurt quality", f"""<p>Some junk is a placement problem.</p>
<p><b>Audience Network</b> places your ad inside other apps and sites, and it has a long reputation for accidental taps. {SRC['sme']} suggests excluding it if it produces low-quality leads. How you do that changed in 2026. Per {SRC['placements']}, Meta is rolling out a change where Leads campaigns (along with Sales, Engagement and App promotion) no longer let you pick placements manually at the ad set level. Exclusions for Audience Network, Facebook Marketplace and the right column now live in account-level controls, and those can be set per objective. If your Ads Manager still shows the old placement picker, the rollout hasn’t reached you yet.</p>
<p>A few other settings worth a look:</p>
<ul>
<li><b>Location.</b> A 25-mile radius around The Woodlands reaches well into north Houston. If you don’t want work in Aldine or Humble, don’t pay for it. List the zip codes or cities you actually serve.</li>
<li>In Ads Manager, break results down by placement and by age. When one placement or one age band produces most of your no-answers, you’ve found a leak.</li>
<li>Special Ad Categories. Housing, employment, credit and financial services ads run with limited targeting by design. Mortgage and real estate advertisers should lean even harder on form questions, because the audience settings can’t do the filtering.</li>
</ul>
<p>For the broader picture of building Meta campaigns for local businesses, see our {f'<a href="/blog/facebook-instagram-ads-local-businesses/">Facebook and Instagram ads guide</a>'}.</p>"""),

            ("A lead-quality scorecard you can run on last month’s leads", f"""<p>Pull last month’s leads into a spreadsheet, add an outcome column, and fill it in from your call notes. Then score them against this. The thresholds come from our own local service accounts, so treat them as rules of thumb and adjust to your business.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Metric</th><th>How to calculate</th><th>Healthy</th><th>Problem</th><th>Likely fix</th></tr></thead>
<tbody>
<tr><td>Bad contact rate</td><td>Fake, disconnected or wrong numbers ÷ all leads</td><td>Under 10%</td><td>Over 20%</td><td>SMS verification, Higher intent, autofill off</td></tr>
<tr><td>“Never filled it out”</td><td>Leads who deny submitting ÷ leads reached</td><td>Under 5%</td><td>Over 15%</td><td>Higher intent, check Audience Network, plainer offer</td></tr>
<tr><td>Reached within 48 hours</td><td>Leads you spoke to ÷ all leads</td><td>Over 50%</td><td>Under 30%</td><td>Speed to lead, auto-text, evening calls</td></tr>
<tr><td>Qualified rate</td><td>Right area, right job, real budget ÷ leads reached</td><td>Over 40%</td><td>Under 20%</td><td>Qualifying questions, Close form logic, offer</td></tr>
<tr><td>Booked rate</td><td>Appointments ÷ qualified leads</td><td>Over 35%</td><td>Under 15%</td><td>Sales process, pricing, follow-up</td></tr>
<tr><td>Cost per booked appointment</td><td>Ad spend ÷ appointments</td><td>Fits your margin</td><td>More than you can earn back</td><td>All of the above</td></tr>
</tbody></table></div>
<p>The last row is the one that decides whether the campaign lives. Our {f'<a href="/blog/understanding-cost-per-lead/">cost per lead guide</a>'} shows how to work backward from job value to what you can afford.</p>
<!--fig:check-->
<p>Run the scorecard monthly. When you change something, change one thing at a time and give it two to three weeks, or you’ll never know which change helped.</p>"""),

            ("When to fix it yourself and when to get help", f"""<p>Most of this you can do in an afternoon: switch to Higher intent, turn on SMS verification if you have it, add four questions with Close form logic, rewrite the offer, set up an auto-text. Do those first.</p>
<p>The CRM integration and Conversions API take more skill, and so does a landing page that actually converts on a phone. Outside help tends to pay off there, especially if your team is already stretched answering the leads you have.</p>
<p>If you want a second set of eyes before you change anything, <a href="/contact/">get in touch</a> and tell us what your lead forms are bringing in. Or see how our <a href="/services/paid-social-advertising/">paid social team</a> runs lead campaigns for businesses from Conroe to Sugar Land.</p>"""),
        ],
        "faq": [
            ("Why are my Facebook leads fake?",
             "Instant forms autofill a person’s name, email and phone from their profile, so submitting takes seconds and many people do it without real intent or with an outdated number. Freebie offers attract people who type fake numbers on purpose. Switch to the Higher intent form type, turn on SMS verification if your account has it, and ask a few qualifying questions."),
            ("How do I improve Facebook lead quality?",
             "Use the Higher intent form type, add four to six qualifying questions with conditional logic that closes the form for non-fits, rewrite the offer so it shows price signals instead of giveaways, call leads within minutes, and send lead outcomes from your CRM back to Meta so it optimizes for qualified leads rather than form fills."),
            ("Is a Facebook lead form or a landing page better?",
             "Instant forms produce cheaper leads and are fast to launch, but quality is mixed. Landing pages cost more per lead and usually bring more serious prospects because people chose to leave the app and see your prices and reviews. For big-ticket local services, test both and compare cost per booked appointment, not cost per lead."),
            ("Why do Facebook leads not answer the phone?",
             "Most people submit a form while scrolling and forget about it quickly, and many won’t answer an unknown number. Call within five minutes, send an automatic text first so your number is recognized, call again in the early evening, and follow a set call and text pattern for a week before giving up on a lead."),
            ("Does the Higher intent form cost more per lead?",
             "Usually yes. The review screen and any extra questions mean fewer people finish the form, so cost per lead rises. What matters is cost per qualified lead and cost per booked job. In local service accounts, filtering out fake and accidental submissions often lowers the cost of each real customer even when the lead price goes up."),
        ],
        "figures": {
            "formtype": {
                "type": "compare",
                "title": "Default form vs a filtered form",
                "left": {"title": "More volume, default settings", "items": ["Autofilled contact fields", "Two taps to submit", "No questions beyond contact info", "Every submit counts as a lead", "Free offer in the headline"]},
                "right": {"title": "Higher intent, filtered", "items": ["Review screen before submit", "SMS code to confirm the number", "Four to six qualifying questions", "Close form for non-fits", "Price signal and what happens next"]},
                "alt": "Comparison of a default Facebook lead form and a filtered form that cuts bad leads for Houston businesses",
                "caption": f"Settings described in {SRC['loomer_forms']} and {SRC['loomer_new']}; availability varies by account.",
            },
            "build": {
                "type": "steps",
                "title": "Building a form that filters",
                "sub": "Instant form setup, in order",
                "steps": [
                    ["Pick Higher intent", "Adds a review screen so people confirm their details."],
                    ["Add SMS verification", "Under Quality filters, if your account shows it."],
                    ["Write the intro bluntly", "Who it’s for, where you work, what happens next."],
                    ["Add 4 to 6 questions", "Area, ownership, project, timing, budget, one short answer."],
                    ["Turn on conditional logic", "Route non-fits to Close form so they never submit."],
                    ["Connect delivery", "CRM or email, plus an instant text alert to your team."],
                ],
                "alt": "Six steps to build a Facebook instant form that filters bad leads for a The Woodlands remodeling company",
                "caption": "Expect fewer leads and a higher cost per lead. Judge it on booked jobs.",
            },
            "leak": {
                "type": "funnel",
                "title": "Where 100 Facebook leads go",
                "stages": [["Form submissions", "100"], ["Real, working numbers", "82"], ["Reached within 48 hours", "45"], ["Qualified", "20"], ["Booked appointment", "8"]],
                "note": "Illustrative example",
                "alt": "Funnel showing how 100 Facebook lead ads submissions shrink to booked appointments for a Houston service business",
                "caption": "Fixing speed and form quality moves the middle of this funnel more than any new ad.",
            },
            "check": {
                "type": "checklist",
                "title": "Lead quality quick check",
                "sub": "Tick what’s true for your account today",
                "items": [
                    "Form type is Higher intent",
                    "SMS verification on, if available",
                    "At least four qualifying questions",
                    "Non-fits routed to Close form",
                    "Offer shows a price signal, no giveaway",
                    "Leads reach a phone within five minutes",
                    "Every lead has an outcome logged in a CRM",
                    "Audience Network excluded if it underperforms",
                ],
                "alt": "Checklist for fixing Facebook lead ads bad leads, used by First Byte for Houston-area local businesses",
                "caption": "Fewer than six ticks means there’s cheap quality to gain before you touch the budget.",
            },
        },
    },

    # ------------------------------------------------------------------ post 2: Microsoft Ads
    {
        "slug": "are-microsoft-ads-worth-it-small-business",
        "title": "Are Microsoft Ads (Bing) Worth It for a Small Business in 2026?",
        "seo_title": "Is Bing Ads Worth It? Microsoft Ads for Small Business",
        "desc": "Is Bing Ads worth it in 2026? Real search share data, Microsoft Ads vs Google Ads, Copilot placements, and when a Houston small business should test it.",
        "category": "Paid ads",
        "icons": ["Microsoft Ads", "Google Ads", "LinkedIn"],
        "art": "b4",
        "hero": "search",
        "hero_alt": "Illustration of a search bar for deciding if Microsoft Ads and Bing are worth it for a Houston small business",
        "related": ["small-business-guide-google-ads-2026", "google-ads-cost-per-click-houston-benchmarks", "b2b-marketing-houston-energy-industrial"],
        "sections": [
            (None, f"""<p>Your Google Ads clicks keep getting more expensive. Somebody at a chamber lunch in The Woodlands says, “Have you tried Bing? Nobody advertises there, it’s cheap.” You laugh, because who uses Bing. Then you remember the PC on your own office desk opens Edge every morning.</p>
<p>So, is Bing Ads worth it? For a lot of small businesses, yes, as a small and controlled test. We wouldn’t make it a big bet. Bing handled 9.72% of U.S. searches across devices in October 2026 and 18.8% of desktop searches, per {SRC['sc_all']}. A minority, sure, but real money, and you can copy your Google campaigns over in an afternoon. B2B companies tend to get the most out of it, along with anyone whose customers search from a work computer or whose Google clicks have gotten painfully expensive. If your Google account isn’t profitable yet, skip it for now.</p>
<p>Below are the actual numbers and what changed this year with Copilot and AI Max. We also chased down where the “Bing is 33% cheaper” line comes from (nowhere solid, it turns out), and there’s a decision table plus the setup steps.</p>"""),

            ("How many people actually use Bing in 2026?", f"""<p>More than most owners assume, and fewer than Microsoft’s sales deck implies. It depends a lot on which device you count.</p>
<p>Across desktop, mobile and tablet, {SRC['sc_all']} put October 2026 U.S. search share at Google 85.5%, Bing 9.72%, Yahoo 2.54% and DuckDuckGo 1.74%. On desktop alone, {SRC['sc_desk']} show a very different split: Google 74.86%, Bing 18.8%, Yahoo 3.98% and DuckDuckGo 1.96%.</p>
<p>Why the gap? Windows PCs ship with Edge, Edge defaults to Bing, and a lot of office computers never get changed. On phones, Google is the default almost everywhere. So Bing’s audience leans toward people sitting at a desk.</p>
<!--fig:share-->
<p>Microsoft’s own numbers are bigger, and it’s worth knowing why. {SRC['msa_search']} claims 109 million unique U.S. PC users, 6.4 billion monthly PC searches and a 38.1% PC market share. Read the footnote: that’s Comscore data from March 2023, desktop traffic only, and it covers Microsoft’s whole search network. Yahoo, AOL and DuckDuckGo results show Microsoft ads too, so they’re counted in. Not wrong, exactly. It’s a sales pitch resting on three-year-old data.</p>
<p>For a Houston-area business, we assume Microsoft Ads reaches somewhere around a tenth of the search demand Google does. More if your buyers search from work.</p>"""),

            ("Where Microsoft ads show up now: Bing, Yahoo, DuckDuckGo and Copilot", f"""<p>A Microsoft Ads search campaign can appear on more than bing.com. Microsoft’s search page lists Bing, AOL, Yahoo, DuckDuckGo and Ecosia among the sites that show its search ads, plus syndicated partners. Its audience ads can run across MSN, Edge and Outlook.com.</p>
<p>The newer piece is <b>Copilot</b>, Microsoft’s AI assistant that’s built into Edge, Windows and Bing. Ads now appear inside Copilot answers. According to {SRC['jumpfly']}, to be eligible you need to be running certain ad types: responsive search ads, Dynamic Search Ads or Performance Max for search placements, plus product and multimedia ads. Microsoft says Copilot ads are built only from your existing assets rather than newly generated copy. There’s no separate “Copilot campaign” to create; it rides on what you already run.</p>
<p>Then there’s <b>AI Max</b>. On August 19, 2026, Microsoft started rolling AI Max out to all accounts globally, per {SRC['aimax']}. It’s a toggle at the Search campaign level. Flip it and you get search term matching that reaches past your keyword list (including the longer, chattier queries people type into Bing and Copilot), plus text customization, where Microsoft tests messaging variations based on your ads and website. It also turns on final URL expansion, which sends people to whichever page on your site Microsoft thinks fits best. You can exclude URLs, and you probably should.</p>
<p>Each piece can be switched off. Microsoft’s older Predictive Matching feature is being folded into AI Max’s search term matching, according to {SRC['predictive']}, with no effective date announced.</p>
<p>On a small test budget, we leave AI Max off for the first month. You want clean search terms from your own keywords before the system starts wandering. Turn it on later as a deliberate experiment, and read the search terms report every week while it runs (bring coffee).</p>"""),

            ("Microsoft Ads vs Google Ads: what’s actually different", f"""<p>The interfaces look almost identical, and that’s on purpose. The differences that matter are underneath.</p>
<div class="bp-tbl"><table>
<thead><tr><th></th><th>Google Ads</th><th>Microsoft Ads</th></tr></thead>
<tbody>
<tr><td>U.S. search share, all devices (Oct 2026)</td><td>85.5%</td><td>9.72% for Bing, plus partner sites</td></tr>
<tr><td>U.S. desktop share (Oct 2026)</td><td>74.86%</td><td>18.8% for Bing</td></tr>
<tr><td>Professional targeting</td><td>No LinkedIn data</td><td>LinkedIn company, industry and job function</td></tr>
<tr><td>Broad match negative keywords</td><td>Supported</td><td>Not supported; imported as phrase match</td></tr>
<tr><td>AI answer placements</td><td>AI Overviews and AI Mode</td><td>Copilot</td></tr>
<tr><td>Setup effort if you already run Google</td><td>n/a</td><td>Import tool copies campaigns, keywords and ads</td></tr>
<tr><td>Competition in most local auctions</td><td>Heavy</td><td>Usually lighter, check your own keywords</td></tr>
</tbody></table></div>
<p>Now about cost. You’ll read everywhere that Bing clicks are “33% cheaper” or “up to 70% cheaper.” We went looking for where those numbers come from. Mostly, they trace back to agency blog posts with no named source, or to studies that are years old. We won’t quote them, and you shouldn’t plan a budget around them.</p>
<p>In practice, fewer advertisers bid in Microsoft’s auctions for local keywords. Clicks are often cheaper, though not always, and volume is much lower. Your own numbers are the ones to trust. Microsoft has its own Keyword Planner; run your top 20 Google keywords through it with Houston-area targeting and compare the suggested bids against your actual Google CPCs. Our {f'<a href="/blog/google-ads-cost-per-click-houston-benchmarks/">Houston Google Ads CPC benchmarks</a>'} give you the Google side.</p>"""),

            ("LinkedIn profile targeting: the B2B reason to care", f"""<p>This is the feature Google can’t match. Microsoft owns LinkedIn, and Microsoft Ads lets you layer LinkedIn profile data onto your campaigns. Per {SRC['linkedin']}, you can target by:</p>
<ul>
<li>Company (up to 1,000 of them in a single ad group or campaign)</li>
<li>Industry, such as oil and energy, construction, or hospital and health care</li>
<li>Job function, such as purchasing, engineering or operations</li>
</ul>
<p>It works in Search, Dynamic Search Ads, Shopping, Audience and (for some accounts) Performance Max campaigns.</p>
<p>The detail people miss is that in search campaigns this works as a <b>bid adjustment</b>. Targeting a company doesn’t exclude everyone else; it lets you bid more when someone from that company searches your keywords. That turns out to be more useful than a filter. Picture an industrial valve distributor in Conroe. When someone searches “api 6d ball valve supplier houston,” you want the click either way, but you’d pay a lot more for it if the searcher works in purchasing at one of the operators along the Energy Corridor or one of the big petrochemical plants on the Ship Channel.</p>
<p>If you sell B2B, we think that signal alone justifies the setup time. Our {f'<a href="/blog/b2b-marketing-houston-energy-industrial/">B2B marketing guide for Houston energy and industrial companies</a>'} covers the rest of that playbook.</p>"""),

            ("When Microsoft Ads is worth it, and when we’d skip it", f"""<p>This is the decision table we actually use. There’s judgment baked into every row, but it gets most businesses to the right answer.</p>
<div class="bp-tbl"><table>
<thead><tr><th>Your situation</th><th>Our call</th><th>Why</th></tr></thead>
<tbody>
<tr><td>B2B, industrial, professional services</td><td>Test it</td><td>Buyers search on work PCs, and LinkedIn targeting helps</td></tr>
<tr><td>High-CPC local services (law, roofing, HVAC replacement)</td><td>Test it</td><td>Even small volume can come cheaper than Google’s top-of-page bids</td></tr>
<tr><td>Older customers (Medicare, retirement planning, home care)</td><td>Test it</td><td>Microsoft pitches an older, desktop-heavy audience; verify with your own data</td></tr>
<tr><td>Google campaigns limited by budget, not demand</td><td>Fix Google first</td><td>Spend more where 85% of the searches are</td></tr>
<tr><td>Google account not profitable yet</td><td>Skip for now</td><td>Importing a broken campaign gives you two broken campaigns</td></tr>
<tr><td>Emergency, mobile-first searches (locksmith, towing)</td><td>Low priority</td><td>Those searches happen on phones, where Bing is small</td></tr>
<tr><td>Restaurants, quick retail, impulse buys</td><td>Usually skip</td><td>Maps, social and Google’s local results matter more</td></tr>
<tr><td>Under about $1,500 a month on Google</td><td>Usually skip</td><td>The Microsoft slice would be too small to learn from</td></tr>
</tbody></table></div>
<!--fig:fit-->
<p>Microsoft has no $1,500 minimum. That line is ours. Below it, a 10% to 15% test is $150 to $225 a month, which in a Houston auction might be 30 clicks, and nobody can read anything into 30 clicks.</p>
<p>A quick word on that “older audience” pitch. Microsoft markets its audience as more affluent and more desktop-based, and desktop share does skew that way. We just haven’t seen independent data we’d stake your budget on. Treat it as a hypothesis and let your own conversion data settle it.</p>"""),

            ("Two Houston examples, worked through", f"""<p>Numbers make this easier. Both of these are hypotheticals with made-up but realistic figures, so swap in your own.</p>
<h3>An estate planning attorney in The Woodlands</h3>
<p>Say she spends $4,000 a month on Google search and gets about 20 consultation requests, so roughly $200 per lead. Her clients are mostly 55 and older, and a lot of them research from a desktop at home or at the office near Hughes Landing. That’s close to the profile Microsoft pitches. A $600 monthly Microsoft test (15% of Google) that produces three or four consults at $150 to $200 each is a clear keep. If it produces one consult a month for three months straight, it isn’t, and she’s out $1,800, which is a fair price for a real answer.</p>
<h3>A two-truck HVAC company in Spring</h3>
<p>Now say he spends $2,500 a month on Google, and most of his calls come from phones in July and August when an AC quits at 9 p.m. Emergency searches like that happen on mobile, where Bing’s share is small. He might still test Microsoft for “ac replacement cost” and “new hvac system quote” type keywords, which people often research at a desk, but we’d put his next $375 into Google Local Services Ads or more budget on his best Google campaign first.</p>
<p>Same platform, and we’d give these two owners opposite advice.</p>"""),

            ("How to import Google Ads into Microsoft Ads, step by step", f"""<p>This is the part that makes the test cheap. You don’t rebuild anything. Per {SRC['import']}:</p>
<ol>
<li>Create the account at ads.microsoft.com with a business email, and set up billing.</li>
<li><b>Install the UET tag</b> (Microsoft’s version of the Google tag). If you use Google Tag Manager, add it there. Create conversion goals that match your Google ones: calls, form submits, booked appointments.</li>
<li><b>Go to Import, then Import from Google Ads.</b> Sign in to Google. Choose Customize rather than Quick import so you can pick specific campaigns and associate your UET tag.</li>
<li>Import only the one or two search campaigns that already make money on Google. Leave the rest behind for now.</li>
<li><b>Decide on scheduled imports.</b> Automatic schedules re-sync changes from Google, and Microsoft warns they can reactivate paused campaigns and revert budgets. For a test, we turn the schedule off and manage Microsoft on its own.</li>
<li><b>Check what changed on the way in.</b> Bids and budgets below Microsoft’s minimums get raised by default. Broad match negatives become phrase match negatives, so review your negative list.</li>
<li>Re-check location targeting. Microsoft notes targeting settings differ significantly between platforms, so confirm your radius or zip codes and the location intent options before going live.</li>
<li>Set a separate budget and launch.</li>
</ol>
<!--fig:steps-->
<p>If you have Google’s two-step verification on and the direct import fails, Microsoft suggests an application-specific password or uploading an import file instead.</p>
<p>New to paid search altogether? Start with our {f'<a href="/blog/small-business-guide-google-ads-2026/">small business guide to Google Ads</a>'} and come back to this once Google works.</p>"""),

            ("What a fair test looks like: budget, time and the numbers to watch", f"""<p>Give it 60 to 90 days and a budget of 10% to 20% of your Google search spend. Shorter than that and the test mostly measures luck, because the volume is low.</p>
<p>What to watch, in this order:</p>
<ul>
<li><b>Search terms, weekly.</b> Microsoft’s matching can be looser than you expect. Add negatives early.</li>
<li>Conversions. Make sure the UET goals are actually recording before you judge anything, which means making a test call yourself.</li>
<li><b>Cost per lead against Google’s.</b> If it’s within about 25% of your Google cost per lead, the channel is earning its keep, because it’s incremental volume.</li>
<li>Lead quality. Ask every caller how they found you and tag the Microsoft leads in your CRM. Cheap leads that never book aren’t cheap.</li>
<li>Device and hour reports. If almost everything converts on desktop from 8 a.m. to 5 p.m., consider a desktop-focused schedule.</li>
</ul>
<!--fig:test-->
<p>By day 90 you’ll know roughly where you stand. If it’s working, raise the budget gradually. If it’s close, try LinkedIn bid adjustments or AI Max as the next experiment. If it isn’t, turn it off, put the money back into Google, and don’t feel bad about it.</p>
<p>The expensive mistake is a mediocre campaign left running for two years because nobody looked.</p>"""),

            ("Should you hire someone to run it?", f"""<p>Honestly, Microsoft Ads is one of the easier things to do yourself if your Google account is in good shape. The import does most of the work. Budget a couple of hours to set it up and twenty minutes a week to watch it.</p>
<p>Where it gets harder is when the Google account itself has problems, because the import copies them. If you’re not sure your Google campaigns are healthy, fix that first. If you’d like help sorting that out before you expand to a second search engine, <a href="/contact/">get in touch</a> and tell us what you’re seeing. If you’d rather hand off the whole search program, our <a href="/services/search-marketing/">search marketing team</a> runs Google and Microsoft campaigns for businesses across The Woodlands and Houston.</p>"""),
        ],
        "faq": [
            ("Is Bing Ads cheaper than Google Ads?",
             "Often, but not always, and the popular claims of 33% or 70% savings don’t trace back to solid current sources. Fewer advertisers bid in most local Microsoft auctions, so clicks can cost less, but volume is much lower. Run your own top keywords through Microsoft’s Keyword Planner and compare suggested bids with what you pay on Google today."),
            ("Can I import my Google Ads campaigns into Microsoft Ads?",
             "Yes. In Microsoft Ads, choose Import, then Import from Google Ads, sign in to Google and pick the campaigns to copy. Bids and budgets below Microsoft’s minimums are raised by default and broad match negatives become phrase match. Recheck location targeting and decide whether to keep scheduled imports on, since they can overwrite changes."),
            ("Do Microsoft ads show on Yahoo and DuckDuckGo?",
             "Yes. Microsoft lists Bing, AOL, Yahoo, DuckDuckGo and Ecosia among the sites that show its search ads, along with other syndicated partners. That’s why Microsoft’s reach claims are larger than Bing’s own search share. Check the publisher reports in your account to see which sites your clicks actually came from."),
            ("Do Microsoft ads show in Copilot?",
             "Yes. Ads can appear inside Copilot answers, and there is no separate Copilot campaign to build. Eligibility depends on running supported ad types such as responsive search ads, Dynamic Search Ads, Performance Max, and product or multimedia ads. Microsoft says Copilot ads are assembled from your existing assets rather than newly generated copy."),
            ("How much should a small business spend on Microsoft Ads?",
             "For a first test, we suggest 10% to 20% of your Google search budget for 60 to 90 days, starting with your best-performing Google campaigns. If you spend less than about $1,500 a month on Google, the Microsoft slice is usually too small to learn from, and the money does more good in Google."),
        ],
        "figures": {
            "share": {
                "type": "bars",
                "title": "U.S. desktop search share, Oct 2026",
                "sub": "Desktop only; Bing is about half this on all devices",
                "items": [["Google", 74.86, "74.86%"], ["Bing", 18.8, "18.8%"], ["Yahoo", 3.98, "3.98%"], ["DuckDuckGo", 1.96, "1.96%"]],
                "highlight": [1],
                "note": "Source: StatCounter",
                "alt": "Bar chart of US desktop search share in October 2026 showing Bing at 18.8 percent, relevant to Microsoft Ads for Houston businesses",
                "caption": f"From {SRC['sc_desk']}. Across all devices Bing had 9.72%.",
            },
            "fit": {
                "type": "checklist",
                "title": "Microsoft Ads is worth testing if…",
                "sub": "Three or more ticks: run a 90-day test",
                "items": [
                    "Your Google Ads account is already profitable",
                    "You spend $1,500+ a month on Google search",
                    "Customers search from work computers",
                    "You sell B2B or to specific industries",
                    "Your Google CPCs are high for your margin",
                    "Your buyers skew older",
                    "Google is limited by demand, not budget",
                ],
                "alt": "Checklist for whether Microsoft Ads and Bing are worth testing for a small business in Houston or The Woodlands",
                "caption": "Our rules of thumb, not Microsoft’s requirements.",
            },
            "steps": {
                "type": "steps",
                "title": "Google Ads to Microsoft Ads import",
                "sub": "An afternoon, if Google is in good shape",
                "steps": [
                    ["Install UET and goals", "Match the conversions you track in Google."],
                    ["Customize the import", "Pick your one or two best search campaigns."],
                    ["Turn off scheduled import", "So Google syncs don’t overwrite your test."],
                    ["Review negatives and bids", "Broad negatives become phrase; minimums get raised."],
                    ["Recheck locations", "Targeting options differ; confirm your service area."],
                ],
                "alt": "Five steps to import Google Ads campaigns into Microsoft Ads for a small business in the Houston area",
                "caption": f"Based on {SRC['import']}.",
            },
            "test": {
                "type": "stats",
                "title": "A fair Microsoft Ads test",
                "stats": [["15%", "of Google search budget (10-20% range)"], ["60-90", "days before judging it"], ["±25%", "of Google’s cost per lead = keep it"]],
                "note": "Illustrative ranges",
                "alt": "Guidelines for a fair Microsoft Ads test budget and timeline for a small business in The Woodlands or Houston",
                "caption": "Our starting rules for a test, adjusted to each account.",
            },
        },
    },
]
