"""Tiny SVG drawing kit for the DE Lock-In diagrams.

Every diagram has a white background so it reads the same in GitHub light
and dark mode. Run tools/build_svg.py to regenerate docs/svg/.
"""
from html import escape

INK = "#1b1f24"
MUTED = "#6a737d"
FONT = "Atkinson Hyperlegible, Verdana, Arial, sans-serif"
COL = {  # group colours: stroke, fill
    "red": ("#d1242f", "#d1242f22"),
    "blue": ("#0969da", "#0969da22"),
    "green": ("#1a7f37", "#1a7f3722"),
    "purple": ("#8250df", "#8250df22"),
    "orange": ("#bc4c00", "#bc4c0022"),
    "teal": ("#127a83", "#127a8322"),
}


class Svg:
    def __init__(self, w, h, title=""):
        self.w, self.h, self.title = w, h, title
        self.parts = []

    def add(self, s):
        self.parts.append(s)
        return self

    def text(self, x, y, s, size=15, anchor="middle", color=INK, weight="normal", italic=False):
        st = ' font-style="italic"' if italic else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
                 f'fill="{color}" font-weight="{weight}"{st}>{escape(s)}</text>')

    def line(self, pts, color=INK, width=2, dash=None):
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
                 f'stroke-linejoin="round" stroke-linecap="round"{da}/>')

    def dot(self, x, y, r=3.5, color=INK):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>')

    def rect(self, x, y, w, h, stroke=INK, fill="none", rx=0, width=2, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{da}/>')

    def arrow(self, pts, color=INK, width=2):
        self.line(pts, color, width)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        import math
        a = math.atan2(y2 - y1, x2 - x1)
        L = 9
        p1 = (x2 - L * math.cos(a - 0.45), y2 - L * math.sin(a - 0.45))
        p2 = (x2 - L * math.cos(a + 0.45), y2 - L * math.sin(a + 0.45))
        self.add(f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')

    def render(self):
        t = f"<title>{escape(self.title)}</title>" if self.title else ""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" font-family="{FONT}" role="img">{t}'
                f'<rect width="100%" height="100%" fill="#ffffff"/>' + "".join(self.parts) + "</svg>")

    def save(self, path):
        with open(path, "w", encoding="utf8") as f:
            f.write(self.render())


# ---------------------------------------------------------------- gates
class Gate:
    """kind: AND OR NOT NAND NOR XOR XNOR BUF. (x, y) = top-left of body."""

    def __init__(self, s, kind, x, y, n=2, h=None, label=None, inbub=False):
        self.kind, self.x, self.y, self.n = kind, x, y, n
        h = h or max(50, 22 * n + 10)
        self.h = h
        w = 56 if kind not in ("NOT", "BUF") else 34
        self.w = w
        base = kind.replace("N", "", 1) if kind in ("NAND", "NOR") else kind
        if kind == "XNOR":
            base = "XOR"
        bub = kind in ("NAND", "NOR", "NOT", "XNOR")
        r = 4.5
        p = []
        if base == "AND":
            fl = w - h / 2
            p.append(f'<path d="M{x},{y} H{x+fl} A{h/2},{h/2} 0 0 1 {x+fl},{y+h} H{x} Z" fill="#fff" stroke="{INK}" stroke-width="2"/>')
            ox = x + w
        elif base in ("OR", "XOR"):
            p.append(f'<path d="M{x},{y} Q{x+w*0.62},{y} {x+w},{y+h/2} Q{x+w*0.62},{y+h} {x},{y+h} '
                     f'Q{x+w*0.25},{y+h/2} {x},{y} Z" fill="#fff" stroke="{INK}" stroke-width="2"/>')
            if base == "XOR":
                p.append(f'<path d="M{x-8},{y} Q{x-8+w*0.25},{y+h/2} {x-8},{y+h}" fill="none" stroke="{INK}" stroke-width="2"/>')
            ox = x + w
        else:  # NOT / BUF triangle
            p.append(f'<path d="M{x},{y} L{x+w},{y+h/2} L{x},{y+h} Z" fill="#fff" stroke="{INK}" stroke-width="2"/>')
            ox = x + w
        oy = y + h / 2
        if bub:
            p.append(f'<circle cx="{ox+r}" cy="{oy}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="2"/>')
            ox += 2 * r
        self.out = (ox, oy)
        # input pins
        self.ins = []
        for i in range(n):
            f = (i + 1) / (n + 1) if n > 1 else 0.5
            py = y + h * f
            if base in ("OR", "XOR"):
                px = x + 0.5 * w * f * (1 - f)
                if base == "XOR":
                    px -= 8
            else:
                px = x
            if inbub:
                p.append(f'<circle cx="{px-r}" cy="{py}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="2"/>')
                px -= 2 * r
            self.ins.append((px, py))
        if label:
            p.append(f'<text x="{x+w*0.42}" y="{y+h/2+5}" font-size="12" text-anchor="middle" fill="{MUTED}">{escape(label)}</text>')
        s.add("".join(p))


def wire(s, a, b, midx=None, color=INK, dots=()):
    """Orthogonal wire a -> b: horizontal, vertical at midx, horizontal."""
    (x1, y1), (x2, y2) = a, b
    if abs(y1 - y2) < 0.5:
        s.line([a, b], color)
    else:
        mx = midx if midx is not None else (x1 + x2) / 2
        s.line([a, (mx, y1), (mx, y2), b], color)
    for d in dots:
        s.dot(*d, color=color)


def label_in(s, p, text, dx=-8, size=15):
    s.text(p[0] + dx, p[1] + 5, text, size=size, anchor="end")


def label_out(s, p, text, dx=8, size=15, weight="bold"):
    s.text(p[0] + dx, p[1] + 5, text, size=size, anchor="start", weight=weight)


# ---------------------------------------------------------------- blocks
def block(s, x, y, w, h, title, left=(), right=(), top=(), bottom=(), pin=24, fill="#f6f8fa"):
    """Rectangle block with named pins. Returns dict name->(x,y) of pin tips."""
    s.rect(x, y, w, h, fill=fill, rx=6)
    s.text(x + w / 2, y + 20, title, size=14, weight="bold")
    pins = {}
    for side, names in (("l", left), ("r", right), ("t", top), ("b", bottom)):
        k = len(names)
        for i, nm in enumerate(names):
            if not nm:
                continue
            f = (i + 1) / (k + 1)
            if side == "l":
                py = y + h * f if title == "" else y + 26 + (h - 30) * f
                s.line([(x - pin, py), (x, py)])
                s.text(x + 6, py + 5, nm, size=13, anchor="start")
                pins[nm] = (x - pin, py)
            elif side == "r":
                py = y + h * f if title == "" else y + 26 + (h - 30) * f
                s.line([(x + w, py), (x + w + pin, py)])
                s.text(x + w - 6, py + 5, nm, size=13, anchor="end")
                pins[nm] = (x + w + pin, py)
            elif side == "t":
                px = x + w * f
                s.line([(px, y - pin), (px, y)])
                pins[nm] = (px, y - pin)
            else:
                px = x + w * f
                s.line([(px, y + h), (px, y + h + pin)])
                s.text(px, y + h - 6, nm, size=13)
                pins[nm] = (px, y + h + pin)
    return pins


# ---------------------------------------------------------------- K-maps
GRAY2 = ["00", "01", "11", "10"]


def kmap_layout(nv):
    """Return (rows, cols, rowbits, colbits, cell(r,c)->minterm)."""
    if nv == 2:
        rb, cb = ["0", "1"], ["0", "1"]
    elif nv == 3:
        rb, cb = GRAY2, ["0", "1"]
    else:
        rb, cb = GRAY2, GRAY2
    def idx(r, c):
        return int(rb[r] + cb[c], 2)
    return len(rb), len(cb), rb, cb, idx


def _runs(sorted_set, n):
    """Split a set of indices (0..n-1, cyclic) into contiguous linear runs."""
    xs = sorted(sorted_set)
    runs, cur = [], [xs[0]]
    for v in xs[1:]:
        if v == cur[-1] + 1:
            cur.append(v)
        else:
            runs.append(cur)
            cur = [v]
    runs.append(cur)
    return runs


def kmap(vars_, vals, groups=(), cell=54, show_idx=True, title=None, legend=True,
         blank="0", x0=None, y0=None, s=None, caption=None):
    """vars_ like 'ABCD' (row vars first). vals: dict minterm->'1'/'0'/'X'.
    groups: list of dicts {cells:[..], color:'red', label:"B'D'"}."""
    nv = len(vars_)
    R, C, rb, cb, idx = kmap_layout(nv)
    rv, cv = (vars_[:1], vars_[1:]) if nv == 2 else (vars_[:2], vars_[2:])
    lm, tm = 70, (66 if not title else 94)
    W = lm + C * cell + 40
    leg_h = 26 * len(groups) + 10 if (legend and groups) else 0
    cap_h = 26 if caption else 0
    H = tm + R * cell + 24 + leg_h + cap_h
    own = s is None
    if own:
        W = max(W, 260, 9 * len(title or "") + 30)
        s = Svg(W, H, title or "K-map")
        x0, y0 = 10, 0
    ox, oy = x0 + lm, y0 + tm
    if title:
        s.text((s.w / 2) if own else x0 + (lm + C * cell) / 2 + 10, y0 + 26, title, size=16, weight="bold")
    # corner label
    s.line([(ox - 46, oy - 46), (ox, oy)], MUTED, 1.5)
    s.text(ox - 40, oy - 6, rv, size=15, anchor="middle", weight="bold")
    s.text(ox - 8, oy - 34, cv, size=15, anchor="middle", weight="bold")
    for c in range(C):
        s.text(ox + c * cell + cell / 2, oy - 14, cb[c], size=15, color=MUTED)
    for r in range(R):
        s.text(ox - 22, oy + r * cell + cell / 2 + 5, rb[r], size=15, color=MUTED)
    for r in range(R):
        for c in range(C):
            m = idx(r, c)
            x, y = ox + c * cell, oy + r * cell
            s.rect(x, y, cell, cell, stroke="#8c959f", width=1.5)
            v = vals.get(m, blank)
            if v != "":
                colr = {"0": MUTED, "X": "#bc4c00"}.get(v, INK)
                s.text(x + cell / 2, y + cell / 2 + 7, v.lower() if v == "X" else v, size=20,
                       color=colr, weight="bold" if v != "0" else "normal")
            if show_idx:
                s.text(x + cell - 5, y + cell - 5, str(m), size=10, anchor="end", color="#8c959f")
    s.rect(ox, oy, C * cell, R * cell, stroke=INK, width=2)
    # groups
    pos = {}
    for r in range(R):
        for c in range(C):
            pos[idx(r, c)] = (r, c)
    for gi, g in enumerate(groups):
        st, fl = COL[g.get("color", "red")]
        rows = {pos[m][0] for m in g["cells"]}
        cols = {pos[m][1] for m in g["cells"]}
        inset = 5 + 4 * (gi % 3)
        for rr in _runs(rows, R):
            for cc in _runs(cols, C):
                x = ox + cc[0] * cell + inset
                y = oy + rr[0] * cell + inset
                w = len(cc) * cell - 2 * inset
                h = len(rr) * cell - 2 * inset
                # wrapped pieces poke past the edge
                if len(_runs(rows, R)) > 1:
                    if rr[0] == 0:
                        y -= inset + 5; h += inset + 5
                    if rr[-1] == R - 1:
                        h += inset + 5
                if len(_runs(cols, C)) > 1:
                    if cc[0] == 0:
                        x -= inset + 5; w += inset + 5
                    if cc[-1] == C - 1:
                        w += inset + 5
                s.rect(x, y, w, h, stroke=st, fill=fl, rx=14, width=3)
    yy = oy + R * cell + 30
    if legend and groups:
        for g in groups:
            st, fl = COL[g.get("color", "red")]
            s.rect(ox, yy - 13, 18, 16, stroke=st, fill=fl, rx=4, width=2.5)
            cells = ",".join(str(c) for c in sorted(g["cells"]))
            s.text(ox + 26, yy, f'{g["label"]}', size=16, anchor="start", color=st, weight="bold")
            s.text(ox + 26 + 9 * len(g["label"]) + 18, yy, f"cells {cells}", size=12, anchor="start", color=MUTED)
            yy += 26
    if caption:
        s.text(ox + C * cell / 2, yy + 4, caption, size=15, weight="bold")
    return s if own else (W, H)
