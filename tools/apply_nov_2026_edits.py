"""Nov 2026 copy + layout pass:
1) Reply-time promise: 'within 1 hour, Mon-Fri' -> 'within an hour or two, 7 days a week'.
2) Hide the pill-style SEO H1 on sub-pages visually (kept for screen readers + search) so the hero moves up.
Run from the repo root: python3 tools/apply_nov_2026_edits.py
"""
import pathlib, re, sys
ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
SITE = ROOT / 'site'

PAIRS = [
    # long form intros (biggest, most-seen blocks)
    ("Questions about your marketing? Tell us what you’re working on. We reply within 1 hour, Mon–Fri.",
     "Questions about your marketing? Tell us what you’re working on. We never clock out — and neither should your marketing. Expect a reply within an hour or two, 7 days a week."),
    ("Tell us a little about your business and what you need. We reply within 1 hour, Mon–Fri.",
     "Tell us a little about your business and what you need. We never clock out — and neither should your marketing. Expect a reply within an hour or two, 7 days a week."),
    ("Tell us what you’re working on. We reply within 1 hour, Mon–Fri.",
     "Tell us what you’re working on. We never clock out — and neither should your marketing. Expect a reply within an hour or two, 7 days a week."),
    ("Sean or a senior strategist — never a sales rep — replies within 1 hour, Mon–Fri.",
     "Sean or a senior strategist — never a sales rep — replies within an hour or two, 7 days a week. We never clock out."),
    ("Tell us what you’re working on and we’ll reply within 1 hour, Mon–Fri. No pressure.",
     "Tell us what you’re working on and we’ll reply within an hour or two — 7 days a week. No pressure."),
    # short lines
    ("Takes 60 seconds · We reply within 1 hour, Mon–Fri", "Takes 60 seconds · Replies 7 days a week"),
    ("We reply within 1 hour, Mon–Fri · No pressure", "Replies 7 days a week, usually within an hour or two · No pressure"),
    ("We reply within 1 hour, Mon–Fri.", "We reply 7 days a week, usually within an hour or two."),
    ("Replies within 1 hour, Mon–Fri.", "Replies 7 days a week, usually within an hour or two."),
    ("We reply within 1 hour.", "We reply 7 days a week, usually within an hour or two."),
    ("<b>1 hour (Mon–Fri)</b>", "<b>1–2 hours, 7 days</b>"),
    ("Reply within 1 hour (Mon–Fri)", "Reply within an hour or two, 7 days a week"),
]

HIDE_RULE = ("\n/* nov-2026: hide pill-style SEO H1 visually; keep it for screen readers + search */\n"
             ".seo-h1{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;"
             "margin:-1px!important;overflow:hidden!important;clip:rect(0 0 0 0)!important;clip-path:inset(50%)!important;"
             "white-space:nowrap!important;border:0!important;animation:none!important}\n")

changed = {}
for p in list(SITE.rglob('*.html')) + list(SITE.rglob('*.js')) + list(SITE.rglob('*.txt')) + list(SITE.rglob('*.xml')) + list(SITE.rglob('*.json')):
    s = p.read_text(encoding='utf-8'); o = s
    for a, b in PAIRS:
        s = s.replace(a, b)
    if p.suffix == '.html':
        s = s.replace('lead.css?v=10', 'lead.css?v=11')
    if s != o:
        p.write_text(s, encoding='utf-8'); changed[str(p.relative_to(ROOT))] = 1

css = SITE / 'assets' / 'firstbyte' / 'lead.css'
c = css.read_text(encoding='utf-8')
if 'nov-2026: hide pill-style SEO H1' not in c:
    css.write_text(c.rstrip() + '\n' + HIDE_RULE, encoding='utf-8'); changed[str(css.relative_to(ROOT))] = 1

left = []
for p in SITE.rglob('*'):
    if p.is_file() and p.suffix in ('.html', '.js', '.txt', '.xml', '.json'):
        for m in re.finditer(r'.{0,50}(1 hour|Mon–Fri).{0,30}', p.read_text(encoding='utf-8', errors='ignore')):
            left.append((str(p.relative_to(ROOT)), m.group(0)))
print('files changed:', len(changed))
print('remaining mentions (review):', len(left))
for f, t in left[:15]: print('  ', f, '|', t.strip())
