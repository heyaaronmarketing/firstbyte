"""Swap every "free audit" offer on the site for the named Ad Spend Leak Check offer,
and replace the "one business day" reply promise with "within 1 hour, Mon–Fri".

Idempotent: re-running it changes nothing once the copy is updated.
Run from the repo root:  python3 tools/apply_leak_check_copy.py
"""
import glob
import re

OFFER = "Ad Spend Leak Check"

# (regex, replacement) — applied in order. Longer, more specific phrases first.
RULES = [
    # ---- Response-time promise -------------------------------------------------
    (r"Tell us what you want to grow\. A senior strategist will reply within one business day with a free audit and a plan\.",
     "Tell us what you’re spending on ads. We reply within 1 hour, Mon–Fri — and your Leak Check video lands within 48 hours."),
    (r"Tell us what you want to grow\. You’ll hear back from a senior strategist within one business day — with a free audit and a plan\.",
     "Tell us what you’re spending on ads. We reply within 1 hour, Mon–Fri — and your Leak Check video lands within 48 hours."),
    (r"Tell us what you want to grow\. A senior strategist — not a sales rep — will get back to you within one business day with a free audit and a plan\.",
     "Tell us what you’re spending on ads. Sean or a senior strategist — never a sales rep — replies within 1 hour, Mon–Fri. Your Leak Check video lands within 48 hours."),
    (r"Takes 60 seconds · Reply within one business day", "Takes 60 seconds · We reply within 1 hour, Mon–Fri"),
    (r"Reply within one business day · No pressure", "We reply within 1 hour, Mon–Fri · No pressure"),
    (r"A senior strategist reaches out within one business day\.", "We reply within 1 hour, Mon–Fri."),
    (r"A senior strategist will contact you within one business day\.", "We reply within 1 hour, Mon–Fri."),
    (r">1 business day<", ">1 hour (Mon–Fri)<"),

    # ---- Offer copy: long sentences -------------------------------------------
    (r"Ready to turn your marketing into a demand machine\? Book a free paid media audit — we’ll show you what’s working, what’s wasting money, and what to do next\.",
     f"Ready to turn your marketing into a demand machine? Get a free {OFFER} — a 10-minute video showing what’s working, what’s wasting money, and what to do next."),
    (r"Get a free audit and a channel plan from a senior strategist\.",
     f"Get a free {OFFER} — a 10-minute video showing where your Google or Meta budget is leaking."),
    (r"Get a free audit from a senior strategist — no pressure, just a plan\.",
     f"Get a free {OFFER} — a 10-minute video showing where your budget is leaking. No pressure."),
    (r"Get a free audit from a senior strategist — we’ll show you where t",
     f"Get a free {OFFER} — we’ll show you where t"),
    (r"Get a free (creative &amp; branding|search marketing|digital ooh, tv &amp; radio|web, seo &amp; pr|paid social) audit from a senior strategist\.",
     f"Get a free {OFFER} from a senior strategist."),
    (r"Start with a free audit — we’ll show you where the quick wins are\.",
     f"Start with a free {OFFER} — we’ll show you exactly where your budget is leaking."),
    (r"Your free audit comes with a recommended budget\.", "Your free Leak Check comes with a recommended budget."),
    (r"We’ll recommend a budget in your free audit\.", "We’ll recommend a budget in your free Leak Check."),
    (r"with a free, no-pressure audit\.", f"with a free, no-pressure {OFFER}."),
    (r"Get a free audit today\.", f"Get a free {OFFER} today."),
    (r"See what’s working, what’s wasting money and what to do next\.",
     "A 10-minute video showing where your Google or Meta budget is leaking. In your inbox within 48 hours."),

    # ---- Offer copy: headings / labels ----------------------------------------
    (r"Free marketing audit</b>", f"Free {OFFER}</b>"),
    (r"\bFree ([A-Z][A-Za-z .&;-]{2,40}?) marketing audit\b", rf"Free \1 {OFFER}"),
    (r"\bFree marketing audit\b", f"Free {OFFER}"),
    (r"\bfree marketing audit\b", f"free {OFFER}"),
    (r"Free audit · \(713\)", "Free Leak Check · (713)"),
    (r"Free audit — call \(713\) 578-0634\.", f"Free {OFFER} — call (713) 578-0634."),
    (r"\. Free audit\.", f". Free {OFFER}."),

    # ---- Buttons ---------------------------------------------------------------
    (r"Get my free audit", f"Get my free {OFFER}"),
    (r"Get your free audit", "Get your free Leak Check"),
    (r"Get a free audit", "Get a free Leak Check"),
    (r">Free audit<", ">Free Leak Check<"),

    # ---- Thank-you page --------------------------------------------------------
    (r"will reach out within one business day with next steps for your free audit\.",
     "replies within 1 hour, Mon–Fri. Your Leak Check video lands within 48 hours."),
]

FILES = (
    glob.glob("site/**/*.html", recursive=True)
    + ["site/llms.txt"]
)


def main():
    changed = 0
    for path in FILES:
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        out = src
        for pat, rep in RULES:
            out = re.sub(pat, rep, out)
        if out != src:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(out)
            changed += 1
    print(f"updated {changed} files")


if __name__ == "__main__":
    main()
