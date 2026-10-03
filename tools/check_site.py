#!/usr/bin/env python3
"""Pre-deploy check for firstbyte.agency (runs in GitLab CI, or locally: python3 tools/check_site.py site).

Fails the pipeline if any page built in the new design has:
  - an internal link, image, script or stylesheet that points to a file that doesn't exist
  - a #anchor that doesn't exist on the target page
  - a missing/duplicate <title>, meta description, canonical, or not exactly one <h1>
Pages still on the old design are only reported as warnings.
"""
import os, re, sys, html as H, collections
from urllib.parse import urlsplit, unquote

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else 'site')
pages = {}
for r, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.html'):
            p = '/' + os.path.relpath(os.path.join(r, f), ROOT).replace(os.sep, '/')
            pages[p[:-10] if p.endswith('/index.html') else p] = open(os.path.join(r, f), encoding='utf-8', errors='replace').read()
ids = {u: set(re.findall(r'\sid="([^"]+)"', s)) for u, s in pages.items()}
new = {u for u, s in pages.items() if '/assets/firstbyte/' in s}

def exists(path):
    fp = os.path.join(ROOT, unquote(path).lstrip('/'))
    return os.path.exists(os.path.join(fp, 'index.html')) if path.endswith('/') else os.path.isfile(fp)

errors, warns = collections.defaultdict(set), collections.defaultdict(set)
titles, descs = collections.defaultdict(list), collections.defaultdict(list)
for u, s in pages.items():
    out = errors if u in new else warns
    for attr, v in re.findall(r'\s(href|src|action)="([^"]*)"', s):
        v = H.unescape(v)
        if v.startswith(('http:', 'https:', 'mailto:', 'tel:', 'data:', 'javascript:', '//')): continue
        sp = urlsplit(v)
        if not sp.path:
            if sp.fragment and sp.fragment not in ids[u] and u in new: out[u].add('missing anchor ' + v)
            continue
        if not sp.path.startswith('/'): continue
        if sp.path.startswith('/api/') or sp.path.startswith('/cdn-cgi/'): continue
        if not exists(sp.path): out[u].add(f'missing {attr} {v}'); continue
        if sp.fragment and sp.path.endswith('/'):
            if sp.fragment not in ids.get(sp.path, ()): out[u].add('missing anchor ' + v)
    if u not in new: continue
    if '/404' in u: continue
    noindex = 'noindex' in s
    t = re.search(r'<title>(.*?)</title>', s, re.S); d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not t: errors[u].add('no <title>')
    if not d: errors[u].add('no meta description')
    if not noindex:
        if t: titles[t.group(1)].append(u)
        if d: descs[d.group(1)].append(u)
        if '<link rel="canonical"' not in s: errors[u].add('no canonical')
    if len(re.findall(r'<h1\b', s)) != 1: errors[u].add('h1 count %d' % len(re.findall(r'<h1\b', s)))
    for m in re.findall(r'<img\b[^>]*>', s):
        if ' alt=' not in m: errors[u].add('img without alt: ' + m[:80])
for k, v in list(titles.items()) + list(descs.items()):
    if len(v) > 1: errors[v[0]].add('duplicate title/description shared with ' + ', '.join(v[1:4]))

for u in sorted(warns):
    for x in sorted(warns[u])[:3]: print('WARN  (old design)', u, '->', x)
for u in sorted(errors):
    for x in sorted(errors[u]): print('ERROR', u, '->', x)
n = sum(len(v) for v in errors.values())
print(f'{len(pages)} pages scanned, {len(new)} in the new design, {n} errors, {sum(len(v) for v in warns.values())} warnings on old-design pages')
sys.exit(1 if n else 0)
