"""On-brand SVG figures for blog posts.

render(spec) -> SVG string for one figure spec (see FIG_TYPES below).
hero(motif, title) -> SVG string for a post's hero illustration.

Figure specs (all also take "alt" and "caption", used by the builder):
  columns   title, sub, labels[], values[0-100], highlight[idx], y_label, note
  bars      title, sub, items[[label, value, display]], highlight[idx], note
  steps     title, sub, steps[[title, text]]            (3-6 steps)
  checklist title, sub, items[str]                      (4-10 items)
  compare   title, left{title, items[]}, right{title, items[]}  (right is the recommended side)
  map       title, sub, highlight[town names], note     (stylized Greater Houston map)
  stats     title, stats[[big, label]], note            (2-4 tiles)
  funnel    title, stages[[label, display]], note       (3-5 stages)
Colors match /assets/firstbyte/firstbyte.css.
"""
import html
import math

BG, CARD, LINE, LINE2 = "#0e0c0f", "#121014", "rgba(255,255,255,.09)", "rgba(255,255,255,.18)"
INK, SOFT, MUTED = "#ffffff", "#cfcad2", "#8f8a93"
CYAN, MAG, BLUE = "#01f6f2", "#be00bb", "#0054ff"
FONT = "Figtree, 'Helvetica Neue', Arial, sans-serif"
DISPLAY = "'Funnel Display', Figtree, 'Helvetica Neue', Arial, sans-serif"
W = 800


def e(s):
    return html.escape(str(s), quote=True)


def wrap(text, n):
    out, line = [], ""
    for w in str(text).split():
        if len(line) + len(w) + (1 if line else 0) > n:
            out.append(line)
            line = w
        else:
            line = f"{line} {w}" if line else w
    if line:
        out.append(line)
    return out


def tspans(lines, x, y, lh, **attrs):
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    t = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{e(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text x="{x}" y="{y}" {a}>{t}</text>'


def frame(h, title, sub, body, note=None, label=None):
    uid = abs(hash(title)) % 10**6
    head = tspans(wrap(title, int((W - 72) / 14)), 36, 52, 30, fill=INK, font_family=DISPLAY, font_size=24, font_weight=600)
    nlines = len(wrap(title, int((W - 72) / 14)))
    sy = 52 + 30 * (nlines - 1) + 26
    subt = tspans(wrap(sub, int((W - 72) / 7.9)), 36, sy, 20, fill=MUTED, font_family=FONT, font_size=14) if sub else ""
    foot = ""
    if note:
        nl = wrap(note, int((W - 150) / 6.3))
        h += 16 * (len(nl) - 1)
        foot = tspans(nl, 36, h - 22 - 16 * (len(nl) - 1), 16, fill=MUTED, font_family=FONT, font_size=12)
    brand = (f'<text x="{W - 36}" y="{h - 22}" text-anchor="end" fill="{MUTED}" font-family="{DISPLAY}" font-size="12" '
             f'letter-spacing="1">first<tspan fill="{CYAN}">byte</tspan></text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img"'
            f' aria-labelledby="t{uid}"><title id="t{uid}">{e(label or title)}</title>'
            f'<defs><linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity=".10"/>'
            f'<stop offset=".5" stop-color="{CARD}" stop-opacity="0"/></linearGradient>'
            f'<linearGradient id="bar{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="#3ad7ff"/></linearGradient></defs>'
            f'<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="22" fill="{CARD}" stroke="{LINE2}"/>'
            f'<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="22" fill="url(#g{uid})"/>'
            f'{head}{subt}{body.replace("BARFILL", f"url(#bar{uid})")}{foot}{brand}</svg>'), sy + (20 * (len(wrap(sub, int((W - 72) / 7.9))) - 1) if sub else -26)


def top_of(sy):
    return sy + 34


# ---------------------------------------------------------------- figure types
def columns(s):
    labels, vals = s["labels"], s["values"]
    hl = set(s.get("highlight", []))
    h = 400
    _, sy = frame(h, s["title"], s.get("sub"), "")
    y0, y1 = top_of(sy) + 10, h - 80
    x0, x1 = 70, W - 36
    n = len(vals)
    bw = (x1 - x0) / n
    parts = []
    for g in (0, 50, 100):
        y = y1 - (y1 - y0) * g / 100
        parts.append(f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" stroke="{LINE}"/>')
    if s.get("y_label"):
        parts.append(f'<text x="{x0 - 14}" y="{(y0 + y1) / 2:.0f}" fill="{MUTED}" font-family="{FONT}" font-size="12" text-anchor="middle" transform="rotate(-90 {x0 - 14} {(y0 + y1) / 2:.0f})">{e(s["y_label"])}</text>')
    for i, (lab, v) in enumerate(zip(labels, vals)):
        bh = (y1 - y0) * max(0, min(100, v)) / 100
        x = x0 + i * bw + bw * 0.18
        on = i in hl
        parts.append(f'<rect x="{x:.1f}" y="{y1 - bh:.1f}" width="{bw * 0.64:.1f}" height="{max(bh, 2):.1f}" rx="6" '
                     f'fill="{"BARFILL" if on else "rgba(255,255,255,.14)"}"/>')
        parts.append(f'<text x="{x + bw * 0.32:.1f}" y="{y1 + 22}" text-anchor="middle" fill="{INK if on else MUTED}" '
                     f'font-family="{FONT}" font-size="13" font-weight="{600 if on else 400}">{e(lab)}</text>')
    return frame(h, s["title"], s.get("sub"), "".join(parts), s.get("note"), s.get("alt"))[0]


def bars(s):
    items = s["items"]
    hl = set(s.get("highlight", []))
    _, sy = frame(100, s["title"], s.get("sub"), "")
    top = top_of(sy) + 6
    narrow = W < 600
    row = 62 if narrow else 46
    h = top + row * len(items) + 54
    mx = max(float(i[1]) for i in items) or 1
    lx, bx, bxe = (36, 36, W - 110) if narrow else (36, 300, W - 120)
    parts = []
    for i, it in enumerate(items):
        lab, v, disp = it[0], float(it[1]), it[2] if len(it) > 2 else str(it[1])
        y = top + i * row
        on = i in hl
        lines = wrap(lab, 34 if not narrow else 52)
        if narrow:
            y += 22
            parts.append(f'<text x="{lx}" y="{y - 6}" fill="{INK if on else SOFT}" font-family="{FONT}" font-size="14" font-weight="{600 if on else 400}">{e(lines[0])}</text>')
        else:
            parts.append(tspans(lines[:2], lx, y + (18 if len(lines) == 1 else 10), 17, fill=INK if on else SOFT, font_family=FONT, font_size=14, font_weight=600 if on else 400))
        bw = (bxe - bx) * v / mx
        parts.append(f'<rect x="{bx}" y="{y + 2}" width="{bxe - bx}" height="22" rx="11" fill="rgba(255,255,255,.05)"/>')
        parts.append(f'<rect x="{bx}" y="{y + 2}" width="{max(bw, 8):.1f}" height="22" rx="11" fill="{"BARFILL" if on else "rgba(255,255,255,.28)"}"/>')
        parts.append(f'<text x="{bxe + 14}" y="{y + 18}" fill="{CYAN if on else INK}" font-family="{DISPLAY}" font-size="15" font-weight="600">{e(disp)}</text>')
    return frame(h, s["title"], s.get("sub"), "".join(parts), s.get("note"), s.get("alt"))[0]


def steps(s):
    st = s["steps"]
    _, sy = frame(100, s["title"], s.get("sub"), "")
    top = top_of(sy) + 4
    parts, y = [], top
    for i, (t, d) in enumerate(st):
        dl = wrap(d, int((W - 130) / 8.4))
        hgt = 34 + 19 * len(dl)
        parts.append(f'<circle cx="58" cy="{y + 16}" r="17" fill="{"rgba(1,246,242,.12)"}" stroke="{CYAN}"/>')
        parts.append(f'<text x="58" y="{y + 21}" text-anchor="middle" fill="{CYAN}" font-family="{DISPLAY}" font-size="15" font-weight="600">{i + 1}</text>')
        if i < len(st) - 1:
            parts.append(f'<line x1="58" x2="58" y1="{y + 36}" y2="{y + hgt + 2}" stroke="{LINE2}" stroke-dasharray="3 5"/>')
        parts.append(f'<text x="92" y="{y + 21}" fill="{INK}" font-family="{FONT}" font-size="16" font-weight="700">{e(t)}</text>')
        parts.append(tspans(dl, 92, y + 43, 19, fill=SOFT, font_family=FONT, font_size=14))
        y += hgt + 14
    h = y + 40
    return frame(h, s["title"], s.get("sub"), "".join(parts), s.get("note"), s.get("alt"))[0]


def checklist(s):
    items = s["items"]
    _, sy = frame(100, s["title"], s.get("sub"), "")
    top = top_of(sy) + 4
    two = len(items) > 5 and W >= 600
    colw = (W - 72) / (2 if two else 1)
    per = math.ceil(len(items) / 2) if two else len(items)
    parts, ymax = [], top
    for c in range(2 if two else 1):
        y = top
        for it in items[c * per:(c + 1) * per]:
            x = 36 + c * colw
            lines = wrap(it, int((colw - 44) / 8.2))
            parts.append(f'<rect x="{x}" y="{y}" width="22" height="22" rx="7" fill="rgba(1,246,242,.12)" stroke="{CYAN}"/>')
            parts.append(f'<path d="M{x + 6} {y + 11.5} l4 4 l7 -8" fill="none" stroke="{CYAN}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
            parts.append(tspans(lines, x + 34, y + 16, 19, fill=SOFT, font_family=FONT, font_size=14.5))
            y += 19 * len(lines) + 20
        ymax = max(ymax, y)
    h = ymax + 40
    return frame(h, s["title"], s.get("sub"), "".join(parts), s.get("note"), s.get("alt"))[0]


def compare(s):
    L, R = s["left"], s["right"]
    _, sy = frame(100, s["title"], s.get("sub"), "")
    top = top_of(sy) + 4
    narrow = W < 600
    colw = (W - 72) if narrow else (W - 72 - 20) / 2

    def col(x, y0, side, good):
        out, y = [], y0 + 64
        out.append(f'<text x="{x + 22}" y="{y0 + 38}" fill="{CYAN if good else SOFT}" font-family="{DISPLAY}" font-size="18" font-weight="600">{e(side["title"])}</text>')
        for it in side["items"]:
            lines = wrap(it, int((colw - 66) / 7.8))
            mark = (f'<path d="M{x + 22} {y - 4} l4 4 l7 -8" fill="none" stroke="{CYAN}" stroke-width="2.2" stroke-linecap="round"/>' if good else
                    f'<path d="M{x + 23} {y - 9} l8 8 M{x + 31} {y - 9} l-8 8" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>')
            out.append(mark + tspans(lines, x + 44, y, 18, fill=INK if good else SOFT, font_family=FONT, font_size=14))
            y += 18 * len(lines) + 16
        return out, y + 6

    if narrow:
        lp, ly = col(36, top, L, False)
        rtop = ly + 16
        rp, ry = col(36, rtop, R, True)
        boxes = (f'<rect x="36" y="{top}" width="{colw:.0f}" height="{ly - top}" rx="16" fill="rgba(255,255,255,.02)" stroke="{LINE}"/>'
                 f'<rect x="36" y="{rtop}" width="{colw:.0f}" height="{ry - rtop}" rx="16" fill="rgba(1,246,242,.05)" stroke="rgba(1,246,242,.45)"/>')
        bottom = ry
    else:
        lp, ly = col(36, top, L, False)
        rp, ry = col(36 + colw + 20, top, R, True)
        bottom = max(ly, ry)
        boxes = (f'<rect x="36" y="{top}" width="{colw:.0f}" height="{bottom - top}" rx="16" fill="rgba(255,255,255,.02)" stroke="{LINE}"/>'
                 f'<rect x="{36 + colw + 20:.0f}" y="{top}" width="{colw:.0f}" height="{bottom - top}" rx="16" fill="rgba(1,246,242,.05)" stroke="rgba(1,246,242,.45)"/>')
    h = bottom + 46
    return frame(h, s["title"], s.get("sub"), boxes + "".join(lp + rp), s.get("note"), s.get("alt"))[0]


TOWNS = {  # approximate lat, lon
    "The Woodlands": (30.166, -95.461), "Spring": (30.080, -95.417), "Conroe": (30.312, -95.456),
    "Houston": (29.760, -95.369), "Katy": (29.786, -95.824), "Cypress": (29.969, -95.697),
    "Tomball": (30.097, -95.616), "Magnolia": (30.209, -95.751), "Kingwood": (30.050, -95.185),
    "Humble": (29.999, -95.262), "Sugar Land": (29.620, -95.635), "Pearland": (29.564, -95.286),
    "Montgomery": (30.388, -95.696), "Willis": (30.425, -95.480), "Atascocita": (29.998, -95.177),
    "Porter": (30.105, -95.235), "New Caney": (30.153, -95.210), "Shenandoah": (30.180, -95.455),
    "Memorial": (29.770, -95.520), "Galleria": (29.739, -95.463), "Heights": (29.799, -95.398),
    "Bellaire": (29.706, -95.459), "Clear Lake": (29.560, -95.110), "League City": (29.507, -95.095),
    "Baytown": (29.735, -94.977), "Missouri City": (29.618, -95.537), "Fulshear": (29.693, -95.900),
}
ROADS = [  # stylized corridors through town coords
    ("I-45", ["Houston", "Spring", "Shenandoah", "Conroe", "Willis"]),
    ("I-69", ["Houston", "Humble", "Kingwood", "Porter", "New Caney"]),
    ("I-10", ["Fulshear", "Katy", "Memorial", "Houston", "Baytown"]),
    ("290", ["Houston", "Cypress"]),
    ("249", ["Houston", "Tomball", "Magnolia"]),
    ("Grand Pkwy", ["Katy", "Cypress", "Tomball", "Spring", "Porter", "Atascocita"]),
    ("I-45 S", ["Houston", "Clear Lake", "League City"]),
    ("I-69 S", ["Houston", "Bellaire", "Sugar Land"]),
]


def map_(s):
    hl = s.get("highlight", ["The Woodlands", "Houston"])
    _, sy = frame(100, s["title"], s.get("sub"), "")
    top = top_of(sy)
    h = top + 430
    lat0, lat1, lon0, lon1 = 29.45, 30.50, -95.98, -94.90
    mx0, mx1, my0, my1 = 60, W - 60, top + 10, h - 60

    def P(t):
        la, lo = TOWNS[t]
        return (mx0 + (lo - lon0) / (lon1 - lon0) * (mx1 - mx0), my0 + (lat1 - la) / (lat1 - lat0) * (my1 - my0))

    parts = []
    for gx in range(int(mx0), int(mx1) + 1, 40):
        parts.append(f'<line x1="{gx}" x2="{gx}" y1="{my0}" y2="{my1}" stroke="rgba(255,255,255,.035)"/>')
    for gy in range(int(my0), int(my1) + 1, 40):
        parts.append(f'<line x1="{mx0}" x2="{mx1}" y1="{gy}" y2="{gy}" stroke="rgba(255,255,255,.035)"/>')
    wx, wy = P("The Woodlands")
    ppm = (my1 - my0) / ((lat1 - lat0) * 69.0)  # px per mile
    for r in (10 * ppm, 20 * ppm, 30 * ppm):
        parts.append(f'<circle cx="{wx:.0f}" cy="{wy:.0f}" r="{r:.0f}" fill="none" stroke="rgba(1,246,242,.22)" stroke-dasharray="4 6"/>')
    for name, path in ROADS:
        pts = " ".join(f"{P(t)[0]:.0f},{P(t)[1]:.0f}" for t in path)
        parts.append(f'<polyline points="{pts}" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    placed = []
    order = ["The Woodlands", "Houston"] + [t for t in TOWNS if t not in ("The Woodlands", "Houston")]
    for t in order:
        x, y = P(t)
        on = t in hl or t == "Houston"
        if t != "The Woodlands":
            parts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{6 if on else 3.5}" fill="{CYAN if on else "rgba(255,255,255,.35)"}"/>')
        if (on or t == "The Woodlands") and all(abs(x - px) > 70 or abs(y - py) > 18 for px, py in placed):
            placed.append((x, y))
            right = x < W - 170
            parts.append(f'<text x="{x + (14 if right else -14):.0f}" y="{y + 5:.0f}" text-anchor="{"start" if right else "end"}" fill="{INK}" '
                         f'font-family="{FONT}" font-size="13.5" font-weight="600" paint-order="stroke" stroke="{CARD}" stroke-width="4">{e(t)}</text>')
    parts.append(f'<circle cx="{wx:.0f}" cy="{wy:.0f}" r="9" fill="{MAG}"/><circle cx="{wx:.0f}" cy="{wy:.0f}" r="16" fill="none" stroke="{MAG}" stroke-opacity=".5"/>')
    ml = wrap("Stylized map, not to scale. Rings mark roughly 10, 20 and 30 miles from The Woodlands.", int((W - 120) / 6.3))
    parts.append(tspans(ml, mx0, my1 + 26, 16, fill=MUTED, font_family=FONT, font_size=12))
    return frame(h + 10 + 16 * (len(ml) - 1) + (18 if s.get("note") else 0), s["title"], s.get("sub"), "".join(parts), s.get("note"), s.get("alt"))[0]


def stats(s):
    st = s["stats"]
    _, sy = frame(100, s["title"], s.get("sub"), "")
    top = top_of(sy) + 4
    n = len(st)
    gap = 16
    narrow = W < 600
    out = []
    if narrow:
        y = top
        for big, lab in st:
            lines = wrap(lab, int((W - 72 - 150) / 7.8))
            hh = max(76, 30 + 19 * len(lines))
            out.append(f'<rect x="36" y="{y}" width="{W - 72}" height="{hh}" rx="16" fill="rgba(255,255,255,.03)" stroke="{LINE}"/>')
            out.append(f'<text x="56" y="{y + hh / 2 + 13:.0f}" fill="{CYAN}" font-family="{DISPLAY}" font-size="36" font-weight="600" letter-spacing="-1">{e(big)}</text>')
            out.append(tspans(lines, 186, round(y + hh / 2 - 19 * (len(lines) - 1) / 2 + 5), 19, fill=SOFT, font_family=FONT, font_size=14))
            y += hh + 12
        h = y + 38
        return frame(h, s["title"], s.get("sub"), "".join(out), s.get("note"), s.get("alt"))[0]
    tw = (W - 72 - gap * (n - 1)) / n
    parts, hmax = [], 0
    for i, (big, lab) in enumerate(st):
        x = 36 + i * (tw + gap)
        lines = wrap(lab, int(tw / 8.2))
        hh = 96 + 19 * len(lines)
        hmax = max(hmax, hh)
        parts.append((x, big, lines))
    for x, big, lines in parts:
        out.append(f'<rect x="{x:.0f}" y="{top}" width="{tw:.0f}" height="{hmax}" rx="16" fill="rgba(255,255,255,.03)" stroke="{LINE}"/>')
        out.append(f'<text x="{x + 20:.0f}" y="{top + 58}" fill="{CYAN}" font-family="{DISPLAY}" font-size="38" font-weight="600" letter-spacing="-1">{e(big)}</text>')
        out.append(tspans(lines, round(x + 20), top + 88, 19, fill=SOFT, font_family=FONT, font_size=14))
    h = top + hmax + 50
    return frame(h, s["title"], s.get("sub"), "".join(out), s.get("note"), s.get("alt"))[0]


def funnel(s):
    st = s["stages"]
    _, sy = frame(100, s["title"], s.get("sub"), "")
    top = top_of(sy) + 4
    row = 58
    parts = []
    for i, (lab, disp) in enumerate(st):
        base = W - 300 if W >= 600 else W - 140
        w = base * (1 - i * 0.16)
        x = 36 + (base - w) / 2
        y = top + i * row
        op = 1 - i * 0.14
        parts.append(f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{row - 10}" rx="12" fill="{CYAN}" fill-opacity="{0.16 * op + 0.04:.2f}" stroke="{CYAN}" stroke-opacity="{0.6 * op:.2f}"/>')
        parts.append(f'<text x="{36 + base / 2:.0f}" y="{y + 30}" text-anchor="middle" fill="{INK}" font-family="{FONT}" font-size="15" font-weight="600">{e(lab)}</text>')
        parts.append(f'<text x="{36 + base + 18:.0f}" y="{y + 30}" fill="{CYAN}" font-family="{DISPLAY}" font-size="17" font-weight="600">{e(disp)}</text>')
    h = top + row * len(st) + 44
    return frame(h, s["title"], s.get("sub"), "".join(parts), s.get("note"), s.get("alt"))[0]


FIG_TYPES = {"columns": columns, "bars": bars, "steps": steps, "checklist": checklist, "compare": compare,
             "map": map_, "stats": stats, "funnel": funnel}


def render(spec, width=800):
    """Render a figure at the given viewBox width (800 for desktop, 440 for phones)."""
    global W
    old, W = W, width
    try:
        return FIG_TYPES[spec["type"]](spec)
    finally:
        W = old


# ---------------------------------------------------------------- hero illustrations
def _motif(m):
    c, g = CYAN, "rgba(255,255,255,.55)"
    sw = 'fill="none" stroke-linecap="round" stroke-linejoin="round"'
    if m == "hvac":
        return (f'<circle cx="0" cy="-10" r="62" {sw} stroke="#ffd23f" stroke-width="4"/>'
                + "".join(f'<line x1="{80 * math.cos(a):.0f}" y1="{-10 + 80 * math.sin(a):.0f}" x2="{100 * math.cos(a):.0f}" y2="{-10 + 100 * math.sin(a):.0f}" stroke="#ffd23f" stroke-width="4" stroke-linecap="round"/>' for a in [i * math.pi / 6 for i in range(12)])
                + f'<rect x="120" y="-40" width="150" height="120" rx="14" {sw} stroke="{c}" stroke-width="4"/>'
                + "".join(f'<line x1="140" x2="250" y1="{-18 + i * 18}" y2="{-18 + i * 18}" stroke="{g}" stroke-width="3" stroke-linecap="round"/>' for i in range(5))
                + f'<path d="M-230 70 c0-40 30-40 30-80 v-60 a18 18 0 0 1 36 0 v60 c0 40 30 40 30 80 a48 48 0 0 1 -96 0z" {sw} stroke="{c}" stroke-width="4"/>'
                + f'<circle cx="-182" cy="70" r="22" fill="{MAG}"/><line x1="-182" x2="-182" y1="70" y2="-60" stroke="{MAG}" stroke-width="10" stroke-linecap="round"/>')
    if m == "roof":
        return (f'<path d="M-200 40 L0 -110 L200 40" {sw} stroke="{c}" stroke-width="5"/>'
                f'<path d="M-160 20 V130 H160 V20" {sw} stroke="{g}" stroke-width="4"/><rect x="-30" y="60" width="60" height="70" rx="4" {sw} stroke="{g}" stroke-width="4"/>'
                + "".join(f'<path d="M{-170 + i * 34} -40 l-10 22" stroke="{c}" stroke-width="3" stroke-linecap="round"/>' for i in range(11) if i % 3)
                + f'<path d="M-120 -150 a40 40 0 0 1 75 -18 a34 34 0 0 1 64 12 a30 30 0 0 1 -4 60 h-120 a28 28 0 0 1 -15 -54z" {sw} stroke="{MAG}" stroke-width="4"/>'
                + "".join(f'<circle cx="{-100 + i * 30}" cy="{-60 + (i % 2) * 16}" r="5" fill="{INK}"/>' for i in range(5)))
    if m == "pool":
        return (f'<rect x="-220" y="-70" width="440" height="170" rx="40" {sw} stroke="{c}" stroke-width="5"/>'
                + "".join(f'<path d="M-180 {-20 + i * 36} q30 -16 60 0 t60 0 t60 0 t60 0 t60 0 t60 0" {sw} stroke="{g if i else c}" stroke-width="3"/>' for i in range(4))
                + f'<path d="M150 -70 v-60 a24 24 0 0 1 48 0 M190 -70 v-60" {sw} stroke="{INK}" stroke-width="4"/>'
                + f'<circle cx="-190" cy="-140" r="34" {sw} stroke="#ffd23f" stroke-width="4"/>')
    if m == "restaurant":
        return (f'<circle cx="0" cy="0" r="110" {sw} stroke="{g}" stroke-width="4"/><circle cx="0" cy="0" r="78" {sw} stroke="{c}" stroke-width="4"/>'
                f'<path d="M-170 -100 v70 a18 18 0 0 0 36 0 v-70 M-152 -100 v200" {sw} stroke="{INK}" stroke-width="4"/>'
                f'<path d="M160 100 v-200 c-30 20 -36 70 -36 110 h36" {sw} stroke="{INK}" stroke-width="4"/>'
                f'<path d="M-30 -10 c10 -40 50 -40 60 0 c10 40 -50 60 -60 0z" fill="{MAG}" fill-opacity=".8"/>')
    if m == "chiro":
        return ("".join(f'<rect x="{-26 + 6 * math.sin(i / 2)}" y="{-140 + i * 30}" width="52" height="22" rx="9" {sw} stroke="{c if i % 3 else MAG}" stroke-width="4"/>' for i in range(10))
                + f'<path d="M-120 -120 c-60 60 -60 180 0 240 M120 -120 c60 60 60 180 0 240" {sw} stroke="{g}" stroke-width="3" stroke-dasharray="6 10"/>')
    if m == "fitness":
        return (f'<rect x="-150" y="-60" width="34" height="120" rx="8" {sw} stroke="{c}" stroke-width="5"/><rect x="116" y="-60" width="34" height="120" rx="8" {sw} stroke="{c}" stroke-width="5"/>'
                f'<rect x="-196" y="-36" width="34" height="72" rx="8" {sw} stroke="{g}" stroke-width="4"/><rect x="162" y="-36" width="34" height="72" rx="8" {sw} stroke="{g}" stroke-width="4"/>'
                f'<line x1="-116" x2="116" y1="0" y2="0" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'
                f'<path d="M-60 -110 l20 -30 l20 30 l20 -30 l20 30 l20 -30 l20 30" {sw} stroke="{MAG}" stroke-width="4"/>')
    if m == "realestate":
        return (f'<path d="M-170 10 L-60 -90 L50 10 V130 H-170z" {sw} stroke="{c}" stroke-width="5"/><rect x="-80" y="60" width="40" height="70" {sw} stroke="{g}" stroke-width="4"/>'
                f'<path d="M110 -120 a50 50 0 0 1 100 0 c0 50 -50 100 -50 100 s-50 -50 -50 -100z" {sw} stroke="{MAG}" stroke-width="5"/><circle cx="160" cy="-120" r="16" fill="{MAG}"/>'
                f'<path d="M60 130 h150 M40 70 l40 -20" {sw} stroke="{g}" stroke-width="4"/>')
    if m == "medical":
        return (f'<rect x="-60" y="-140" width="120" height="280" rx="18" fill="{c}" fill-opacity=".14" stroke="{c}" stroke-width="4"/>'
                f'<rect x="-140" y="-60" width="280" height="120" rx="18" fill="{c}" fill-opacity=".14" stroke="{c}" stroke-width="4"/>'
                f'<path d="M-230 40 h50 l20 -50 l30 100 l25 -70 h40" {sw} stroke="{MAG}" stroke-width="4"/><path d="M160 40 h70" {sw} stroke="{MAG}" stroke-width="4"/>')
    if m == "wedding":
        return (f'<circle cx="-50" cy="20" r="80" {sw} stroke="{c}" stroke-width="6"/><circle cx="50" cy="20" r="80" {sw} stroke="#ffd23f" stroke-width="6"/>'
                f'<path d="M30 -78 l20 -26 l20 26 l-20 14z" {sw} stroke="{INK}" stroke-width="4"/>'
                + "".join(f'<circle cx="{-200 + i * 50}" cy="{-130 + (i % 3) * 18}" r="4" fill="{MAG}"/>' for i in range(9)))
    if m == "hotel":
        return (f'<rect x="-120" y="-150" width="240" height="290" rx="10" {sw} stroke="{c}" stroke-width="5"/>'
                + "".join(f'<rect x="{-90 + (i % 4) * 48}" y="{-120 + (i // 4) * 50}" width="30" height="30" rx="4" fill="{MAG if i in (5, 10) else "rgba(255,255,255,.18)"}"/>' for i in range(16))
                + f'<rect x="-26" y="90" width="52" height="50" rx="6" {sw} stroke="{INK}" stroke-width="4"/>'
                + "".join(f'<path d="M{170 + i * 26} -60 l6 -16 l6 16 l16 2 l-12 10 l4 16 l-14 -9 l-14 9 l4 -16 l-12 -10z" fill="#ffd23f"/>' for i in range(3)))
    if m == "billboard":
        return (f'<rect x="-210" y="-150" width="420" height="190" rx="10" {sw} stroke="{c}" stroke-width="5"/>'
                f'<rect x="-180" y="-120" width="230" height="22" rx="6" fill="{MAG}" fill-opacity=".8"/>'
                f'<rect x="-180" y="-82" width="160" height="14" rx="6" fill="rgba(255,255,255,.35)"/><rect x="-180" y="-58" width="120" height="14" rx="6" fill="rgba(255,255,255,.2)"/>'
                f'<circle cx="130" cy="-62" r="44" {sw} stroke="#ffd23f" stroke-width="4"/>'
                f'<path d="M-90 40 V150 M90 40 V150 M-90 90 H90" {sw} stroke="{g}" stroke-width="5"/>'
                f'<path d="M-260 150 H260" {sw} stroke="{g}" stroke-width="3" stroke-dasharray="18 14"/>')
    if m == "phone":
        return (f'<rect x="-80" y="-150" width="160" height="300" rx="28" {sw} stroke="{c}" stroke-width="5"/>'
                f'<rect x="-30" y="-134" width="60" height="10" rx="5" fill="{g}"/>'
                f'<circle cx="0" cy="-30" r="40" fill="{MAG}" fill-opacity=".2" stroke="{MAG}" stroke-width="4"/>'
                f'<path d="M-14 -46 l28 32 M14 -46 l-28 32" stroke="{MAG}" stroke-width="5" stroke-linecap="round"/>'
                f'<rect x="-50" y="40" width="100" height="14" rx="7" fill="rgba(255,255,255,.3)"/><rect x="-36" y="66" width="72" height="14" rx="7" fill="rgba(255,255,255,.18)"/>'
                + "".join(f'<path d="M{110 + i * 28} {-60 - i * 6} a{40 + i * 28} {40 + i * 28} 0 0 1 0 {80 + i * 56}" {sw} stroke="{c}" stroke-opacity="{0.8 - i * 0.25:.2f}" stroke-width="4"/>' for i in range(3)))
    if m == "stars":
        pts = lambda cx, cy, r: " ".join(f"{cx + (r if k % 2 == 0 else r * .42) * math.sin(k * math.pi / 5):.0f},{cy - (r if k % 2 == 0 else r * .42) * math.cos(k * math.pi / 5):.0f}" for k in range(10))
        return ("".join(f'<polygon points="{pts(-200 + i * 100, -40, 42)}" fill="{"#ffd23f" if i < 3 else "none"}" stroke="#ffd23f" stroke-width="4" stroke-linejoin="round" opacity="{1 if i < 3 else .5}"/>' for i in range(5))
                + f'<rect x="-230" y="40" width="460" height="100" rx="18" {sw} stroke="{c}" stroke-width="4"/>'
                f'<rect x="-200" y="66" width="260" height="14" rx="7" fill="rgba(255,255,255,.3)"/><rect x="-200" y="94" width="190" height="14" rx="7" fill="rgba(255,255,255,.18)"/>'
                f'<path d="M140 70 l40 40 M180 70 l-40 40" stroke="{MAG}" stroke-width="6" stroke-linecap="round"/>')
    if m == "tools":
        return (f'<rect x="-190" y="-30" width="380" height="170" rx="18" {sw} stroke="{c}" stroke-width="5"/>'
                f'<path d="M-70 -30 v-40 a16 16 0 0 1 16 -16 h108 a16 16 0 0 1 16 16 v40" {sw} stroke="{c}" stroke-width="5"/>'
                f'<path d="M-190 40 H190" stroke="{g}" stroke-width="4"/><rect x="-24" y="26" width="48" height="30" rx="6" fill="{MAG}"/>'
                f'<path d="M150 -150 l-90 90 M60 -60 l-14 30 l30 -14" {sw} stroke="#ffd23f" stroke-width="5"/>'
                f'<path d="M-150 -150 a26 26 0 1 0 30 30 l60 60" {sw} stroke="{INK}" stroke-width="5"/>')
    if m == "search":
        return (f'<circle cx="-70" cy="-30" r="100" {sw} stroke="{c}" stroke-width="6"/>'
                f'<path d="M2 42 L120 160" stroke="{c}" stroke-width="16" stroke-linecap="round"/>'
                f'<path d="M-70 -90 a40 40 0 0 1 40 40 c0 34 -40 70 -40 70 s-40 -36 -40 -70 a40 40 0 0 1 40 -40z" {sw} stroke="{MAG}" stroke-width="5"/>'
                f'<circle cx="-70" cy="-50" r="13" fill="{MAG}"/>'
                + "".join(f'<rect x="110" y="{-130 + i * 34}" width="{100 - i * 20}" height="14" rx="7" fill="rgba(255,255,255,{.35 - i * .07:.2f})"/>' for i in range(4)))
    if m == "growth":
        return (f'<path d="M-230 130 H230 M-230 130 V-140" {sw} stroke="{g}" stroke-width="4"/>'
                + "".join(f'<rect x="{-200 + i * 80}" y="{110 - h}" width="46" height="{h}" rx="8" fill="{c}" fill-opacity="{.25 + i * .15:.2f}"/>' for i, h in enumerate((50, 90, 120, 170, 220)))
                + f'<path d="M-190 40 L-100 0 L-20 -20 L60 -80 L180 -150" {sw} stroke="{MAG}" stroke-width="6"/>'
                f'<path d="M150 -156 L184 -152 L176 -120" {sw} stroke="{MAG}" stroke-width="6"/>')
    if m == "browser":
        return (f'<rect x="-230" y="-150" width="460" height="300" rx="18" {sw} stroke="{c}" stroke-width="5"/>'
                f'<path d="M-230 -105 H230" stroke="{c}" stroke-width="4"/>'
                + "".join(f'<circle cx="{-200 + i * 24}" cy="-128" r="7" fill="{col}"/>' for i, col in enumerate((MAG, "#ffd23f", c)))
                + f'<rect x="-196" y="-76" width="210" height="26" rx="8" fill="rgba(255,255,255,.4)"/><rect x="-196" y="-36" width="160" height="14" rx="7" fill="rgba(255,255,255,.2)"/>'
                f'<rect x="-196" y="0" width="110" height="38" rx="19" fill="{c}"/><rect x="40" y="-76" width="156" height="190" rx="12" fill="{MAG}" fill-opacity=".25" stroke="{MAG}" stroke-width="3"/>')
    return f'<circle r="100" {sw} stroke="{c}" stroke-width="5"/>'


def hero(motif, kicker="The Woodlands · Houston", w=1200, h=600, title=None):
    dots = "".join(f'<circle cx="{(i * 97) % w}" cy="{(i * 53) % h}" r="1.6" fill="rgba(255,255,255,.18)"/>' for i in range(70))
    grid = "".join(f'<line x1="{x}" x2="{x}" y1="0" y2="{h}" stroke="rgba(255,255,255,.04)"/>' for x in range(0, w, 60)) + \
        "".join(f'<line x1="0" x2="{w}" y1="{y}" y2="{y}" stroke="rgba(255,255,255,.04)"/>' for y in range(0, h, 60))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<defs><radialGradient id="hg" cx=".72" cy=".42" r=".6"><stop offset="0" stop-color="{CYAN}" stop-opacity=".22"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="hm" cx=".15" cy=".95" r=".55"><stop offset="0" stop-color="{MAG}" stop-opacity=".28"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="{BG}"/>{grid}{dots}<rect width="{w}" height="{h}" fill="url(#hg)"/><rect width="{w}" height="{h}" fill="url(#hm)"/>'
            + (f'<g transform="translate({w * 0.66:.0f} {h * 0.5:.0f}) scale(1.25)">{_motif(motif)}</g>' if not title else
               f'<g transform="translate({w * 0.79:.0f} {h * 0.5:.0f}) scale(.95)">{_motif(motif)}</g>'
               + tspans(wrap(title, 22)[:4], 70, 210, 64, fill=INK, font_family=DISPLAY, font_size=54, font_weight=600, letter_spacing=-1))
            + f'<g transform="translate(70 {h - 70})"><circle r="7" fill="{MAG}"/><circle r="15" fill="none" stroke="{MAG}" stroke-opacity=".5"/>'
            f'<text x="28" y="6" fill="{SOFT}" font-family="{FONT}" font-size="20" letter-spacing="3">{e(kicker.upper())}</text></g>'
            f'<text x="70" y="96" fill="{INK}" font-family="{DISPLAY}" font-size="40" font-weight="600">first<tspan fill="{CYAN}">byte</tspan></text></svg>')
