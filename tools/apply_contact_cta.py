#!/usr/bin/env python3
"""Replace the retired "free Ad Spend Leak Check" offer with a plain "Contact us" call to action, site-wide.

Nov 2026: the owner decided not every visitor is ready for an audit, so every button, form, banner, meta
description and blog mention now invites people to contact us instead. Idempotent; safe to rerun.

    python3 tools/apply_contact_cta.py            # rewrite site/ in place
    python3 tools/apply_contact_cta.py --check    # list any remaining "Leak Check" mentions, exit 1 if found

Two layers:
  1. TEMPLATE: exact strings / regexes for the repeated chrome (header, mobile bar, forms, blog sidebar,
     inline CTA, case-study CTAs, meta descriptions, city FAQs, thank-you page, llms.txt, lead widget).
  2. PROSE: tools/contact_cta_prose.json, hand-written sentence rewrites for the blog posts that mentioned
     the offer in their own words. The same edits are applied to tools/posts_*.py so rebuilds stay clean.
seo_fixes_oct_2026.py calls run() at the end, so the normal build pipeline always applies this.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
PROSE = os.path.join(ROOT, "tools", "contact_cta_prose.json")

REPLY = "We reply within 1 hour, Mon–Fri."

# (old, new) exact replacements, longest/most specific first.
EXACT = [
    # --- blog sidebar card + inline CTA
    ("<b>Free Ad Spend Leak Check</b><p>A 10-minute video showing where your Google or Meta budget is leaking. In your inbox within 48 hours.</p>",
     "<b>Talk to our team</b><p>Questions about your marketing? Tell us what you’re working on. We reply within 1 hour, Mon–Fri.</p>"),
    ("<span>Get a free Ad Spend Leak Check — a 10-minute video showing where your budget is leaking. No pressure.</span>",
     "<span>Tell us what you’re working on and we’ll tell you honestly how we’d help. No pressure.</span>"),
    # --- contact sections and forms
    ("Tell us what you’re spending on ads. We reply within 1 hour, Mon–Fri — and your Leak Check video lands within 48 hours.",
     "Tell us a little about your business and what you need. We reply within 1 hour, Mon–Fri."),
    ('<input type="hidden" name="offer" value="Ad Spend Leak Check">', '<input type="hidden" name="offer" value="Contact request">'),
    ("<small>Free Ad Spend Leak Check · We reply within 1 hour, Mon–Fri</small>", "<small>We reply within 1 hour, Mon–Fri · No pressure</small>"),
    ("Free Fitness Ad Spend Leak Check", "Talk to our fitness team"),
    ("Free Hospitality Ad Spend Leak Check", "Talk to our hospitality team"),
    ("Get a free Ad Spend Leak Check from a senior strategist. No pressure, no fluff — just a plan.",
     "Talk to a senior strategist. No pressure, no fluff — just a plan."),
    ("Ready to turn your marketing into a demand machine? Get a free Ad Spend Leak Check — a 10-minute video showing what’s working, what’s wasting money, and what to do next.",
     "Ready to turn your marketing into a demand machine? Tell us what you’re working on and we’ll talk through what’s working, what’s wasting money, and what to do next."),
    # --- mid-page banners
    ("<span>Get a free Ad Spend Leak Check — a 10-minute video showing where your Google or Meta budget is leaking.</span>",
     "<span>Tell us about your business and we’ll recommend the right mix.</span>"),
    ("<span>Start with a free Ad Spend Leak Check — we’ll show you exactly where your budget is leaking.</span>",
     "<span>Tell us about your goals and we’ll show you where we’d start.</span>"),
    ("<span>Get a free Ad Spend Leak Check — we’ll show you where the quick wins are.</span>",
     "<span>Tell us what you’re working on and we’ll point out the quick wins.</span>"),
    # --- homepage hero sub-line
    ('<p class="cta-sub">A 10-minute video showing where your Google or Meta budget is leaking. In your inbox within 48 hours.</p>',
     f'<p class="cta-sub">{REPLY} No pressure, no obligation.</p>'),
    # --- case-study closing section
    ('Find out where your budget <span class="cy">is leaking.</span>', 'Let’s talk about <span class="cy">your goals.</span>'),
    ("Get a free Ad Spend Leak Check: a 10-minute video showing where your Google or Meta budget is leaking. In your inbox within 48 hours.",
     f"Tell us what you’re working on. {REPLY}"),
    # --- process steps
    ("<h3>Free Leak Check</h3><p>We dig into what’s working and what’s wasting money.</p>",
     "<h3>Intro call</h3><p>We learn your goals and look at what’s working and what’s wasting money.</p>"),
    # --- FAQs and budget lines
    ("Your free Leak Check comes with a recommended budget.", "Contact us and we’ll recommend a budget."),
    ("We’ll recommend a budget in your free Leak Check.", "We’ll recommend a budget when we talk."),
    # --- meta descriptions / schema descriptions
    ("Free Ad Spend Leak Check — call (713) 578-0634.", "Contact us or call (713) 578-0634."),
    ("Call (713) 578-0634 or get a free Ad Spend Leak Check. We reply within 1 hour.", "Call (713) 578-0634 or send us a message. We reply within 1 hour."),
    ("More calls and customers. Free Ad Spend Leak Check.", "More calls and customers. Contact us today."),
    ("Get a free Ad Spend Leak Check today.", "Contact us today."),
    ("Free Leak Check · (713) 578-0634", "Contact us · (713) 578-0634"),
    # --- thank-you page
    ('<span class="cy">your Leak Check is on.</span>', '<span class="cy">we got your message.</span>'),
    ("We reply within 1 hour, Mon–Fri. Your Ad Spend Leak Check — a 10-minute video showing where your Google or Meta budget is leaking — lands in your inbox within 48 hours.",
     "We reply within 1 hour, Mon–Fri. If it’s urgent, call (713) 578-0634."),
    # --- llms.txt
    ("- [Free Ad Spend Leak Check](https://firstbyte.agency/contact/): A free 10-minute video showing where your Google or Meta budget is leaking, in your inbox within 48 hours.",
     "- [Contact](https://firstbyte.agency/contact/): Reach the team by form or phone, (713) 578-0634. Replies within 1 hour, Mon–Fri."),
]

# regex replacements (button labels etc.)
REGEX = [
    (r"<b>Free [^<]{1,40} Ad Spend Leak Check</b>", "<b>Talk to our team</b>"),
    (r"<b>Get your free Leak Check</b>", "<b>Send us a message</b>"),
    (r"<h3>Free Leak Check</h3>", "<h3>We look at your setup</h3>"),
    (r"\s*Free Ad Spend Leak Check\.(\"|<)", r" Contact us today.\1"),
    (r"Tell us what you’re spending on ads\. (Sean or a senior strategist — never a sales rep — replies within 1 hour, Mon–Fri\.) Your Leak Check video lands within 48 hours\.",
     r"Tell us a little about your business. \1"),
    (r"Every page shows exactly what we do in your area — with a free, no-pressure Ad Spend Leak Check\.",
     "Every page shows exactly what we do in your area. Questions? Just ask."),
    (r"Get my free Ad Spend Leak Check(\s*<span class=\"arr\">)", r"Contact us\1"),
    (r"(<button[^>]*>)Contact us(\s*<span class=\"arr\">)", r"\1Send my message\2"),  # form submit buttons read better as an action
    (r"Get my free Ad Spend Leak Check", "Contact us"),
    (r"Get my free Leak Check", "Contact us"),
    (r"Get a free Leak Check", "Contact us"),
    (r"(Run a business like [^<?]+\?) Get your Leak Check", r"\1 Let’s talk"),
    (r"(content=\"[^\"]*?)\s*Free Leak Check\.(\")", r"\1 Contact us today.\2"),
    (r"(\"description\": \"[^\"]*?)\s*Free Leak Check\.(\")", r"\1 Contact us today.\2"),
    (r"Free Leak Check\.", "Contact us today."),
]

# lead widget (site/assets/leadmode.js)
WIDGET = [
    ('<h2>Get your free <span class="a">Ad Spend Leak Check</span></h2>', '<h2>Let’s talk about <span class="a">your marketing</span></h2>'),
    ("A 10-minute video showing where your Google or Meta budget is leaking — and the 3 fastest fixes. In your inbox within 48 hours.",
     "Tell us what you’re working on and we’ll reply within 1 hour, Mon–Fri. No pressure."),
    ("We reply within 1 hour, Mon–Fri, and your Ad Spend Leak Check video lands within 48 hours.", "We reply within 1 hour, Mon–Fri."),
    ("🎯 <b>Free:</b> an Ad Spend Leak Check — a 10-minute video showing where your ad budget is leaking.",
     "👋 <b>Questions about your marketing?</b> Talk to a senior strategist in The Woodlands."),
    ("<button>Claim mine</button>", "<button>Contact us</button>"),
    ("💬 Get my free Leak Check", "💬 Contact us"),
    ("⚡ Free Leak Check", "✉️ Contact us"),
    ('text: "in Conroe requested a Leak Check"', 'text: "in Conroe sent a message"'),
]


def prose_edits():
    try:
        return json.load(open(PROSE, encoding="utf-8"))
    except FileNotFoundError:
        return []


def rewrite(s, prose):
    for e in prose:
        s = s.replace(e["old"], e["new"])
    for a, b in EXACT:
        s = s.replace(a, b)
    for a, b in REGEX:
        s = re.sub(a, b, s)
    return s


def run(verbose=False):
    prose = prose_edits()
    changed = 0
    for f in glob.glob(os.path.join(SITE, "**", "*"), recursive=True):
        if not re.search(r"\.(html|txt|xml)$", f):
            continue
        s = open(f, encoding="utf-8").read()
        n = rewrite(s, prose)
        if n != s:
            open(f, "w", encoding="utf-8").write(n)
            changed += 1
    w = os.path.join(SITE, "assets", "leadmode.js")
    if os.path.exists(w):
        s = open(w, encoding="utf-8").read()
        n = s
        for a, b in WIDGET:
            n = n.replace(a, b)
        if n != s:
            open(w, "w", encoding="utf-8").write(n)
            changed += 1
    # keep post sources in step so a rebuild doesn't bring the old offer back
    for f in glob.glob(os.path.join(ROOT, "tools", "posts_*.py")):
        s = open(f, encoding="utf-8").read()
        n = s
        for e in prose:
            n = n.replace(e["old"], e["new"])
        if n != s:
            open(f, "w", encoding="utf-8").write(n)
    if verbose:
        print(f"rewrote {changed} files")
    return changed


def remaining():
    hits = []
    for f in glob.glob(os.path.join(SITE, "**", "*"), recursive=True):
        if not re.search(r"\.(html|txt|xml|js)$", f):
            continue
        for m in re.finditer(r"Leak Check", open(f, encoding="utf-8").read()):
            hits.append(f)
    return hits


if __name__ == "__main__":
    if "--check" in sys.argv:
        h = remaining()
        for f in sorted(set(h)):
            print(f, h.count(f))
        sys.exit(1 if h else 0)
    run(verbose=True)
