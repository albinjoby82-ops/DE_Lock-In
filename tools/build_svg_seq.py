"""Build the sequential-logic diagrams (Topics 13 to 21) into docs/svg/seq/.

Run: python3 tools/build_svg_seq.py
"""
import os, math
from svglib import Svg, Gate, wire, label_in, label_out, block, kmap, INK, MUTED, COL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "svg", "seq")
os.makedirs(OUT, exist_ok=True)
RED, BLUE, GREEN, ORANGE = COL["red"][0], COL["blue"][0], COL["green"][0], COL["orange"][0]


def save(s, name):
    s.save(os.path.join(OUT, name + ".svg"))


class V:
    """K-map variable names longer than one character (Q₁, Q₀ ...)."""

    def __init__(self, parts):
        self.p = list(parts)

    def __len__(self):
        return len(self.p)

    def __getitem__(self, sl):
        return "".join(self.p[sl])


def vals(nv, ones, dc=()):
    v = {m: "0" for m in range(2 ** nv)}
    for m in ones:
        v[m] = "1"
    for m in dc:
        v[m] = "X"
    return v


# ------------------------------------------------------------ helpers
def ff(s, x, y, kind, name="", w=84, h=96, neg=False, pin=22, fill="#f6f8fa", qn=True):
    """Flip-flop block. kind: D, T, JK, SR. Returns pin tips."""
    s.rect(x, y, w, h, fill=fill, rx=5)
    p = {}
    ins = {"D": ["D"], "T": ["T"], "JK": ["J", "K"], "SR": ["S", "R"]}[kind]
    ys = [y + 22] if len(ins) == 1 else [y + 22, y + h - 22]
    for nm, py in zip(ins, ys):
        s.line([(x - pin, py), (x, py)])
        s.text(x + 7, py + 5, nm, size=14, anchor="start", weight="bold")
        p[nm] = (x - pin, py)
    cy = y + h / 2 if len(ins) == 2 else y + h - 24
    s.line([(x, cy - 8), (x + 12, cy), (x, cy + 8)], width=2)
    if neg:
        s.add(f'<circle cx="{x-5}" cy="{cy}" r="4.5" fill="#fff" stroke="{INK}" stroke-width="2"/>')
        s.line([(x - pin, cy), (x - 9.5, cy)])
    else:
        s.line([(x - pin, cy), (x, cy)])
    p["C"] = (x - pin, cy)
    s.line([(x + w, y + 22), (x + w + pin, y + 22)])
    s.text(x + w - 7, y + 27, "Q", size=14, anchor="end", weight="bold")
    p["Q"] = (x + w + pin, y + 22)
    if qn:
        s.line([(x + w, y + h - 22), (x + w + pin, y + h - 22)])
        s.text(x + w - 7, y + h - 17, "Q'", size=14, anchor="end", weight="bold")
        p["Qn"] = (x + w + pin, y + h - 22)
    if name:
        s.text(x + w / 2, y + h + 18, name, size=13, color=MUTED)
    return p


def node(s, x, y, top, bottom=None, r=30, color=INK, fill="#f6f8fa"):
    s.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="2.5"/>')
    if bottom is None:
        s.text(x, y + 6, top, size=17, weight="bold")
    else:
        s.text(x, y - 2, top, size=17, weight="bold")
        s.text(x, y + 17, bottom, size=13, color=MUTED)


def _head(s, x2, y2, a, color):
    L = 10
    p1 = (x2 - L * math.cos(a - 0.42), y2 - L * math.sin(a - 0.42))
    p2 = (x2 - L * math.cos(a + 0.42), y2 - L * math.sin(a + 0.42))
    s.add(f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')


def edge(s, a, b, label, bend=0, r=30, color=INK, lpos=0.5, loff=13, size=14):
    """Arrow between node centres a and b. bend > 0 bows to the left of travel."""
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    nx, ny = dy / d, -dx / d  # left normal (screen coords)
    cx, cy = (x1 + x2) / 2 + nx * bend, (y1 + y2) / 2 + ny * bend
    # trim to the circle edges along the control direction
    a1 = math.atan2(cy - y1, cx - x1)
    a2 = math.atan2(y2 - cy, x2 - cx)
    sx, sy = x1 + r * math.cos(a1), y1 + r * math.sin(a1)
    ex, ey = x2 - (r + 2) * math.cos(a2), y2 - (r + 2) * math.sin(a2)
    s.add(f'<path d="M{sx:.1f},{sy:.1f} Q{cx:.1f},{cy:.1f} {ex:.1f},{ey:.1f}" fill="none" stroke="{color}" stroke-width="2"/>')
    _head(s, ex, ey, a2, color)
    t = lpos
    px = (1 - t) ** 2 * sx + 2 * t * (1 - t) * cx + t * t * ex
    py = (1 - t) ** 2 * sy + 2 * t * (1 - t) * cy + t * t * ey
    sign = 1 if bend >= 0 else -1
    s.text(px + nx * loff * sign, py + ny * loff * sign + 5, label, size=size, color=color, weight="bold")


def loop(s, c, label, side="top", r=30, color=INK, size=14):
    x, y = c
    k = {"top": (0, -1), "bottom": (0, 1), "left": (-1, 0), "right": (1, 0)}[side]
    if k[0] == 0:
        sy = y + k[1] * r * 0.8
        x1, x2 = x - r * 0.6, x + r * 0.6
        top = y + k[1] * (r + 44)
        s.add(f'<path d="M{x1:.1f},{sy:.1f} C{x1-22:.1f},{top:.1f} {x2+22:.1f},{top:.1f} {x2+1:.1f},{sy+k[1]*-0:.1f}" fill="none" stroke="{color}" stroke-width="2"/>')
        _head(s, x2 + 1, sy - k[1] * 1, math.atan2(-k[1] * 1.0, -0.45), color)
        s.text(x, y + k[1] * (r + 40) + (0 if k[1] < 0 else 12), label, size=size, color=color, weight="bold")
    else:
        sx = x + k[0] * r * 0.8
        y1, y2 = y - r * 0.6, y + r * 0.6
        far = x + k[0] * (r + 44)
        s.add(f'<path d="M{sx:.1f},{y1:.1f} C{far:.1f},{y1-22:.1f} {far:.1f},{y2+22:.1f} {sx:.1f},{y2+1:.1f}" fill="none" stroke="{color}" stroke-width="2"/>')
        _head(s, sx, y2 + 1, math.atan2(-0.45, -k[0] * 1.0), color)
        s.text(x + k[0] * (r + 40), y + 5, label, size=size, color=color, weight="bold",
               anchor="start" if k[0] > 0 else "end")


def timing(s, x0, y0, rows, step=40, h=24, gap=20, edges=None, edge_color="#8c959f", label_w=64):
    """rows: [(name, 'levels', color)] one char per half step ('0'/'1'/'x')."""
    n = max(len(r[1]) for r in rows)
    half = step / 2
    total_h = len(rows) * (h + gap)
    if edges:
        for e in edges:
            x = x0 + label_w + e * half
            s.line([(x, y0 - 6), (x, y0 + total_h - gap + 6)], edge_color, 1.2, dash="4 4")
    for i, row in enumerate(rows):
        name, lv = row[0], row[1]
        col = row[2] if len(row) > 2 else INK
        yb = y0 + i * (h + gap) + h
        s.text(x0 + label_w - 12, yb - h / 2 + 5, name, size=15, anchor="end", weight="bold", color=col)
        pts = []
        prev = None
        for j, ch in enumerate(lv):
            x = x0 + label_w + j * half
            if ch == "x":
                s.rect(x, yb - h, half, h, stroke="none", fill="#d0d7de", width=0)
                prev = None
                if pts:
                    s.line(pts, col, 2.4); pts = []
                continue
            y = yb - (h if ch == "1" else 0)
            if prev is not None and prev != y:
                pts.append((x, y))
            elif not pts:
                pts.append((x, y))
            pts.append((x + half, y))
            prev = y
        if pts:
            s.line(pts, col, 2.4)
    return x0 + label_w + n * half, y0 + total_h - gap


def mos(s, x, y, p=False, label=None):
    """MOSFET, channel vertical. (x, y) = gate tip on the left. Returns (drain_top, source_bottom)."""
    gx = x + 26
    if p:
        s.line([(x, y), (gx - 9, y)])
        s.add(f'<circle cx="{gx-4.5}" cy="{y}" r="4.5" fill="#fff" stroke="{INK}" stroke-width="2"/>')
    else:
        s.line([(x, y), (gx, y)])
    s.line([(gx, y - 14), (gx, y + 14)], width=2.5)
    s.line([(gx + 7, y - 16), (gx + 7, y + 16)], width=2.5)
    s.line([(gx + 7, y - 12), (gx + 24, y - 12), (gx + 24, y - 28)])
    s.line([(gx + 7, y + 12), (gx + 24, y + 12), (gx + 24, y + 28)])
    if label:
        s.text(x - 6, y + 5, label, size=14, anchor="end", weight="bold")
    return (gx + 24, y - 28), (gx + 24, y + 28)


def vdd(s, x, y):
    s.line([(x - 14, y), (x + 14, y)], width=2.5)
    s.text(x, y - 7, "VDD", size=12, color=MUTED)


def gnd(s, x, y):
    s.line([(x - 13, y), (x + 13, y)], width=2.5)
    s.line([(x - 8, y + 5), (x + 8, y + 5)], width=2)
    s.line([(x - 3, y + 10), (x + 3, y + 10)], width=2)


# ============================================================ Topic 13
def latches():
    # SR latch from NOR gates
    s = Svg(470, 230, "SR latch from two NOR gates")
    g1 = Gate(s, "NOR", 200, 30, 2, h=60)
    g2 = Gate(s, "NOR", 200, 140, 2, h=60)
    s.line([(90, g1.ins[0][1]), g1.ins[0]]); label_in(s, (90, g1.ins[0][1]), "R")
    s.line([(90, g2.ins[1][1]), g2.ins[1]]); label_in(s, (90, g2.ins[1][1]), "S")
    qx = 330
    s.line([g1.out, (400, g1.out[1])]); label_out(s, (400, g1.out[1]), "Q")
    s.line([g2.out, (400, g2.out[1])]); label_out(s, (400, g2.out[1]), "Q'")
    # cross-coupling
    s.line([(qx, g1.out[1]), (qx, 104), (160, 126), (160, g2.ins[0][1]), g2.ins[0]], BLUE); s.dot(qx, g1.out[1], color=BLUE)
    s.line([(qx - 26, g2.out[1]), (qx - 26, 126), (160, 104), (160, g1.ins[1][1]), g1.ins[1]], RED); s.dot(qx - 26, g2.out[1], color=RED)
    s.text(235, 222, "each output feeds the other gate: that loop is the memory", size=12, color=MUTED)
    save(s, "sr-latch-nor")

    # D latch
    s = Svg(560, 200, "Gated D latch")
    a1 = Gate(s, "AND", 210, 24, 2)
    a2 = Gate(s, "AND", 210, 116, 2)
    p = block(s, 370, 20, 90, 150, "SR latch", left=("S", "R"), right=("Q", "Q'"))
    s.line([a1.out, (330, a1.out[1]), (330, p["S"][1]), p["S"]])
    s.line([a2.out, (330, a2.out[1]), (330, p["R"][1]), p["R"]])
    s.line([(60, a1.ins[0][1]), a1.ins[0]]); label_in(s, (60, a1.ins[0][1]), "D")
    nt = Gate(s, "NOT", 130, a2.ins[1][1] - 14, 1, h=28)
    s.line([(100, a1.ins[0][1]), (100, a2.ins[1][1]), nt.ins[0]]); s.dot(100, a1.ins[0][1])
    s.line([nt.out, a2.ins[1]])
    cy = (a1.ins[1][1] + a2.ins[0][1]) / 2
    s.line([(60, cy), (190, cy)]); label_in(s, (60, cy), "C")
    s.line([(190, a1.ins[1][1]), (190, a2.ins[0][1])]); s.dot(190, cy)
    s.line([(190, a1.ins[1][1]), a1.ins[1]]); s.line([(190, a2.ins[0][1]), a2.ins[0]])
    label_out(s, p["Q"], "Q"); label_out(s, p["Q'"], "Q'")
    s.text(280, 192, "S = D·C and R = D'·C, so S = R = 1 can never happen", size=12, color=MUTED)
    save(s, "d-latch")

    # master-slave D flip-flop
    s = Svg(600, 210, "Master-slave D flip-flop")
    m = block(s, 130, 30, 110, 110, "D latch", left=("D", "C"), right=("Q",))
    sl = block(s, 360, 30, 110, 110, "D latch", left=("D", "C"), right=("Q",))
    s.text(185, 22, "MASTER", size=12, color=BLUE, weight="bold")
    s.text(415, 22, "SLAVE", size=12, color=RED, weight="bold")
    s.line([(60, m["D"][1]), m["D"]]); label_in(s, (60, m["D"][1]), "D")
    s.line([m["Q"], (290, m["Q"][1]), (290, sl["D"][1]), sl["D"]]); s.text(278, m["Q"][1] - 8, "Y", size=14, weight="bold")
    s.line([sl["Q"], (540, sl["Q"][1])]); label_out(s, (540, sl["Q"][1]), "Q")
    ck = 180
    s.line([(60, ck), (250, ck)]); label_in(s, (60, ck), "CLK")
    s.line([(90, ck), (90, m["C"][1]), m["C"]]); s.dot(90, ck)
    nt = Gate(s, "NOT", 250, ck - 14, 1, h=28)
    s.line([nt.out, (318, ck), (318, sl["C"][1]), sl["C"]])
    s.text(185, 162, "open while CLK = 1", size=12, color=BLUE)
    s.text(420, 162, "open while CLK = 0", size=12, color=RED)
    s.text(300, 204, "Q only changes at the 1 → 0 clock edge (negative-edge triggered)", size=12, color=MUTED)
    save(s, "ms-dff")

    # latch vs flip-flop timing
    clk = "0011001100110011"
    d = "0001101100010110"
    ql, qf = [], []
    q = 0
    for i, c in enumerate(clk):
        if c == "1":
            q = int(d[i])
        ql.append(str(q))
    q = 0
    for i, c in enumerate(clk):
        if i > 0 and clk[i - 1] == "0" and c == "1":
            q = int(d[i - 1])
        qf.append(str(q))
    s = Svg(520, 230, "Latch against flip-flop")
    rise = [i for i in range(1, len(clk)) if clk[i - 1] == "0" and clk[i] == "1"]
    timing(s, 20, 20, [("CLK", clk), ("D", d, BLUE), ("Q latch", "".join(ql), ORANGE), ("Q flip-flop", "".join(qf), RED)],
           step=48, edges=rise, label_w=110)
    s.text(260, 212, "latch: follows D the whole time CLK = 1 · flip-flop: samples D only at the rising edge", size=12, color=MUTED)
    save(s, "latch-vs-ff")

    # flip-flop symbols
    s = Svg(640, 190, "D, JK and T flip-flops")
    for i, (k, eq) in enumerate([("D", "Q⁺ = D"), ("JK", "Q⁺ = JQ' + K'Q"), ("T", "Q⁺ = T ⊕ Q")]):
        x = 60 + i * 210
        ff(s, x, 20, k)
        s.text(x + 42, 146, k + " flip-flop", size=14, weight="bold")
        s.text(x + 42, 170, eq, size=15, color=BLUE, weight="bold")
    save(s, "ff-symbols")

    # edge symbols
    s = Svg(420, 170, "Positive and negative edge symbols")
    ff(s, 60, 20, "D")
    ff(s, 260, 20, "D", neg=True)
    s.text(102, 146, "triangle = edge triggered", size=12, color=MUTED)
    s.text(102, 162, "rising edge (0 → 1)", size=13, weight="bold")
    s.text(302, 146, "triangle + bubble", size=12, color=MUTED)
    s.text(302, 162, "falling edge (1 → 0)", size=13, weight="bold")
    save(s, "ff-edges")


# ============================================================ Topics 14, 15
def fsm_1001_circuit():
    s = Svg(640, 400, "1001 detector with JK flip-flops")
    f1 = ff(s, 320, 24, "JK", "", h=130)
    f0 = ff(s, 320, 204, "JK", "", h=130)
    gj1 = Gate(s, "AND", 150, f1["J"][1] - 25, 2, h=50)
    gk1 = Gate(s, "OR", 150, f1["K"][1] - 25, 2, h=50)
    gj0 = Gate(s, "OR", 150, f0["J"][1] - 25, 2, h=50)
    for g, pin, nm in ((gj1, f1["J"], "J₁"), (gk1, f1["K"], "K₁"), (gj0, f0["J"], "J₀")):
        s.line([g.out, pin])
        s.text(g.out[0] + 44, g.out[1] - 7, nm, size=13, color=BLUE, weight="bold")
    for g, labs in ((gj1, ("X'", "Q₀")), (gk1, ("X", "Q₀")), (gj0, ("X", "Q₁"))):
        for p_, t in zip(g.ins, labs):
            s.line([(p_[0] - 30, p_[1]), p_]); label_in(s, (p_[0] - 30, p_[1]), t)
    s.line([(f0["K"][0] - 60, f0["K"][1]), f0["K"]]); label_in(s, (f0["K"][0] - 60, f0["K"][1]), "X'")
    s.text(f0["K"][0] - 24, f0["K"][1] - 7, "K₀", size=13, color=BLUE, weight="bold")
    for f in (f1, f0):
        s.line([(f["C"][0] - 18, f["C"][1]), f["C"]]); label_in(s, (f["C"][0] - 18, f["C"][1]), "CLK", size=12)
    label_out(s, f1["Q"], "Q₁"); label_out(s, f0["Q"], "Q₀")
    gz = Gate(s, "AND", 530, 145, 3, h=70)
    for p_, t in zip(gz.ins, ("Q₁", "Q₀", "X")):
        s.line([(p_[0] - 26, p_[1]), p_]); label_in(s, (p_[0] - 26, p_[1]), t)
    s.line([gz.out, (612, gz.out[1])]); label_out(s, (612, gz.out[1]), "Z")
    s.text(320, 372, "J₁ = X'Q₀     K₁ = X + Q₀     J₀ = X + Q₁     K₀ = X'     Z = Q₁Q₀X", size=14, weight="bold")
    s.text(320, 392, "wires with the same name are joined (Q₁ and Q₀ feed back from the flip-flop outputs)", size=12, color=MUTED)
    save(s, "fsm-1001-circuit")


def fsm_diagrams():
    # Mealy 1001
    s = Svg(700, 310, "Mealy state diagram: detect 1001")
    P = {"A": (130, 150), "B": (290, 150), "C": (450, 150), "D": (610, 150)}
    sub = {"A": "00", "B": "01", "C": "10", "D": "11"}
    edge(s, P["A"], P["B"], "1/0", r=34)
    edge(s, P["B"], P["C"], "0/0", r=34)
    edge(s, P["C"], P["D"], "0/0", r=34)
    edge(s, P["D"], P["B"], "1/1", bend=-95, r=34, color=RED)
    edge(s, P["C"], P["B"], "1/0", bend=48, r=34, color=BLUE, loff=14)
    edge(s, P["D"], P["A"], "0/0", bend=150, r=34, color=BLUE)
    loop(s, P["A"], "0/0", "left", r=34, color=BLUE)
    loop(s, P["B"], "1/0", "top", r=34, color=BLUE)
    for k, (x, y) in P.items():
        node(s, x, y, k, sub[k], r=34)
    s.text(350, 300, "label = input / output · red = pattern found · blue = the fall-back arrows", size=12, color=MUTED)
    save(s, "fsm-1001-mealy")

    # Moore 1001
    s = Svg(760, 300, "Moore state diagram: detect 1001")
    P = {"A": (80, 150), "B": (230, 150), "C": (380, 150), "D": (530, 150), "E": (680, 150)}
    edge(s, P["A"], P["B"], "1", r=34)
    edge(s, P["B"], P["C"], "0", r=34)
    edge(s, P["C"], P["D"], "0", r=34)
    edge(s, P["D"], P["E"], "1", r=34, color=RED)
    loop(s, P["A"], "0", "top", r=34, color=BLUE)
    loop(s, P["B"], "1", "top", r=34, color=BLUE)
    edge(s, P["C"], P["B"], "1", bend=-40, r=34, color=BLUE)
    edge(s, P["D"], P["A"], "0", bend=110, r=34, color=BLUE)
    edge(s, P["E"], P["C"], "0", bend=-70, r=34, color=BLUE)
    edge(s, P["E"], P["B"], "1", bend=-125, r=34, color=BLUE, lpos=0.5)
    for k, (x, y) in P.items():
        node(s, x, y, k + "/" + ("1" if k == "E" else "0"), None, r=34, color=RED if k == "E" else INK)
    s.text(380, 292, "output lives inside the state (state/output) · one extra state E = “just saw 1001”", size=12, color=MUTED)
    save(s, "fsm-1001-moore")

    # two-sequence detector 1011 / 1110
    s = Svg(760, 400, "Mealy detector for 1011 and 1110")
    P = {"A": (130, 110), "B": (290, 110), "C": (470, 110), "D": (670, 110), "G": (290, 300), "H": (540, 300)}
    sub = {"A": "nothing", "B": "1", "C": "10", "D": "101", "G": "11", "H": "111"}
    loop(s, P["A"], "0/00", "left", r=32)
    edge(s, P["A"], P["B"], "1/00", r=32)
    edge(s, P["B"], P["C"], "0/00", r=32)
    edge(s, P["B"], P["G"], "1/00", r=32, loff=-24)
    edge(s, P["C"], P["A"], "0/00", bend=75, r=32, lpos=0.72)
    edge(s, P["C"], P["D"], "1/00", bend=24, r=32)
    edge(s, P["D"], P["C"], "0/00", bend=24, r=32)
    edge(s, P["D"], P["G"], "1/01", r=32, color=RED, lpos=0.22, loff=16)
    edge(s, P["G"], P["C"], "0/00", r=32, lpos=0.3, loff=-22)
    edge(s, P["G"], P["H"], "1/00", r=32, bend=-24)
    edge(s, P["H"], P["C"], "0/10", r=32, color=GREEN, lpos=0.3, loff=-22)
    loop(s, P["H"], "1/00", "right", r=32)
    for k, (x, y) in P.items():
        node(s, x, y, k, sub[k], r=32)
    s.text(380, 388, "under each letter = the useful tail of the input so far · red: 1011 found (01) · green: 1110 found (10)", size=12, color=MUTED)
    save(s, "fsm-two-seq")

    # generic mealy vs moore blocks
    s = Svg(640, 230, "Moore against Mealy")
    for i, (nm, mealy) in enumerate((("Moore", False), ("Mealy", True))):
        y = 20 + i * 108
        s.text(20, y + 46, nm, size=16, anchor="start", weight="bold", color=BLUE if mealy else GREEN)
        s.rect(130, y + 14, 110, 54, fill="#f6f8fa", rx=6); s.text(185, y + 38, "next-state", size=13); s.text(185, y + 55, "logic", size=13)
        s.rect(290, y + 14, 90, 54, fill="#f6f8fa", rx=6); s.text(335, y + 38, "flip-flops", size=13); s.text(335, y + 55, "(state)", size=13)
        s.rect(440, y + 14, 100, 54, fill="#f6f8fa", rx=6); s.text(490, y + 38, "output", size=13); s.text(490, y + 55, "logic", size=13)
        s.arrow([(90, y + 30), (130, y + 30)]); s.text(86, y + 35, "X", size=14, anchor="end", weight="bold")
        s.arrow([(240, y + 41), (290, y + 41)]); s.arrow([(380, y + 41), (440, y + 41)]); s.arrow([(540, y + 41), (590, y + 41)])
        s.text(596, y + 46, "Z", size=14, anchor="start", weight="bold")
        s.line([(410, y + 41), (410, y + 86), (112, y + 86), (112, y + 54)]); s.arrow([(112, y + 54), (130, y + 54)]); s.dot(410, y + 41)
        if mealy:
            s.line([(100, y + 30), (100, y + 2), (425, y + 2), (425, y + 26)], RED); s.arrow([(425, y + 26), (440, y + 26)], RED); s.dot(100, y + 30, color=RED)
            s.text(262, y - 3 + 0, "", size=11)
    s.text(320, 122, "Mealy only: the input also reaches the output logic (red)", size=12, color=RED)
    save(s, "moore-vs-mealy")


def kmaps_1001():
    names = V(["Q₁", "Q₀", "X"])
    s = Svg(1180, 300, "K-maps for the 1001 detector JK inputs")
    x = 0
    data = [("J₁ = X'Q₀", vals(3, [2], [4, 5, 6, 7]), [{"cells": [2, 6], "color": "red", "label": "X'Q₀"}]),
            ("K₁ = X + Q₀", vals(3, [5, 6, 7], [0, 1, 2, 3]), [{"cells": [1, 3, 5, 7], "color": "red", "label": "X"}, {"cells": [2, 3, 6, 7], "color": "blue", "label": "Q₀"}]),
            ("J₀ = X + Q₁", vals(3, [1, 4, 5], [2, 3, 6, 7]), [{"cells": [1, 3, 5, 7], "color": "red", "label": "X"}, {"cells": [4, 5, 6, 7], "color": "blue", "label": "Q₁"}]),
            ("K₀ = X'", vals(3, [2, 6], [0, 1, 4, 5]), [{"cells": [0, 2, 4, 6], "color": "red", "label": "X'"}])]
    for title, v, g in data:
        W, H = kmap(names, v, g, s=s, x0=x, y0=0, title=title, cell=50)
        x += 292
    save(s, "fsm-1001-kmaps")


# ============================================================ Topic 16
def counters():
    # mod-5 state diagram with unused states
    s = Svg(560, 330, "Modulo-5 counter with its unused states")
    cx, cy, R = 200, 165, 105
    seq = ["000", "001", "010", "011", "100"]
    P = {}
    for i, k in enumerate(seq):
        a = -math.pi / 2 - math.pi * 0.4 + i * 2 * math.pi / 5
        P[k] = (cx + R * math.cos(a), cy + R * math.sin(a))
    for i, k in enumerate(seq):
        edge(s, P[k], P[seq[(i + 1) % 5]], "", bend=-14, r=28)
    P["101"] = (440, 150); P["110"] = (440, 250); P["111"] = (60, 40)
    edge(s, P["101"], P["010"], "", r=28, color=RED)
    edge(s, P["110"], P["010"], "", r=28, color=RED, bend=-30)
    edge(s, P["111"], P["000"], "", r=28, color=RED)
    for k, (x, y) in P.items():
        un = k in ("101", "110", "111")
        node(s, x, y, k, None, r=28, color=RED if un else INK, fill="#fff5f5" if un else "#f6f8fa")
    s.text(440, 100, "unused states", size=13, color=RED, weight="bold")
    s.text(280, 322, "every unused state falls back into the loop → self-correcting", size=12, color=MUTED)
    save(s, "mod5-states")

    # mod-5 K-maps
    s = Svg(900, 300, "Modulo-5 counter K-maps")
    data = [("J_A = BC", vals(3, [3], [4, 5, 6, 7]), [{"cells": [3, 7], "color": "red", "label": "BC"}]),
            ("J_B = C  (K_B = C too)", vals(3, [1], [2, 3, 5, 6, 7]), [{"cells": [1, 3, 5, 7], "color": "red", "label": "C"}]),
            ("J_C = A'", vals(3, [0, 2], [1, 3, 5, 6, 7]), [{"cells": [0, 1, 2, 3], "color": "red", "label": "A'"}])]
    x = 0
    for title, v, g in data:
        title = title.replace("_", "")
        kmap("ABC", v, g, s=s, x0=x, y0=0, title=title, cell=50)
        x += 300
    save(s, "mod5-kmaps")

    # mod-5 circuit
    s = Svg(640, 230, "Modulo-5 synchronous counter")
    xs = [470, 280, 90]  # C, B, A drawn right to left? keep A left
    fa = ff(s, 110, 40, "JK", "A"); fb = ff(s, 310, 40, "JK", "B"); fc = ff(s, 510, 40, "JK", "C")
    for f, j, k in ((fa, "BC", "1"), (fb, "C", "C"), (fc, "A'", "1")):
        s.line([(f["J"][0] - 16, f["J"][1]), f["J"]]); label_in(s, (f["J"][0] - 16, f["J"][1]), j)
        s.line([(f["K"][0] - 16, f["K"][1]), f["K"]]); label_in(s, (f["K"][0] - 16, f["K"][1]), k)
    ck = 190
    s.line([(40, ck), (480, ck)]); label_in(s, (40, ck), "CLK", size=13)
    for f in (fa, fb, fc):
        x = f["C"][0] - 8
        s.line([(x, ck), (x, f["C"][1]), f["C"]]); s.dot(x, ck)
    for f, nm in ((fa, "A"), (fb, "B"), (fc, "C")):
        label_out(s, f["Q"], nm, dx=4)
    s.text(320, 222, "one common clock = synchronous · JA = BC needs one AND gate", size=12, color=MUTED)
    save(s, "mod5-circuit")

    # ripple counter
    s = Svg(850, 210, "4-bit binary ripple counter")
    prev = None
    for i in range(4):
        x = 140 + i * 185
        f = ff(s, x, 50, "T", neg=True, qn=False)
        s.line([(f["T"][0] - 14, f["T"][1]), f["T"]]); label_in(s, (f["T"][0] - 14, f["T"][1]), "1")
        s.line([f["Q"], (f["Q"][0], 26)]); s.text(f["Q"][0], 18, "A" + "₀₁₂₃"[i], size=15, weight="bold")
        if prev is None:
            s.line([(70, f["C"][1]), f["C"]]); label_in(s, (70, f["C"][1]), "Count", size=13)
        else:
            s.line([prev["Q"], (prev["Q"][0] + 14, prev["Q"][1]), (prev["Q"][0] + 14, f["C"][1]), f["C"]], BLUE); s.dot(*prev["Q"], color=BLUE)
        prev = f
    s.text(410, 180, "each Q clocks the next flip-flop (blue) → not one common clock → asynchronous", size=12, color=MUTED)
    s.text(410, 198, "bubble = toggles on the falling edge, so the count goes UP", size=12, color=MUTED)
    save(s, "ripple4-counter")

    # ripple timing
    n = 34
    clk = "".join("10"[(i // 1) % 2] for i in range(n))  # high first: falls at odd->even
    clk = "".join("1" if i % 2 == 0 else "0" for i in range(n))
    rows = [("Count", clk)]
    sig = clk
    for b in range(4):
        q, out = 0, []
        for i in range(n):
            if i > 0 and sig[i - 1] == "1" and sig[i] == "0":
                q ^= 1
            out.append(str(q))
        sig = "".join(out)
        rows.append(("A" + "₀₁₂₃"[b], sig, [BLUE, GREEN, ORANGE, RED][b]))
    s = Svg(700, 270, "Ripple counter timing")
    timing(s, 10, 30, rows, step=36, label_w=70)
    for i in range(16):
        s.text(10 + 70 + 18 + i * 36 + 9, 18, format(i, "X"), size=12, color=MUTED)
    for b, t in enumerate(("f", "f / 2", "f / 4", "f / 8", "f / 16")):
        s.text(694, 30 + b * 44 + 17, t, size=12, anchor="end", color=MUTED)
    s.text(330, 262, "each stage toggles when the one before it falls: every stage halves the frequency", size=12, color=MUTED)
    save(s, "ripple-timing")

    # stuck counter (0,2,4,6 with JK) lock-out
    s = Svg(640, 250, "A counter that locks out")
    P = {"000": (70, 60), "010": (190, 60), "100": (190, 180), "110": (70, 180)}
    order = ["000", "010", "100", "110"]
    for i, k in enumerate(order):
        edge(s, P[k], P[order[(i + 1) % 4]], "", r=28)
    Q = {"001": (370, 60), "011": (490, 60), "101": (490, 180), "111": (370, 180)}
    o2 = ["001", "011", "101", "111"]
    for i, k in enumerate(o2):
        edge(s, Q[k], Q[o2[(i + 1) % 4]], "", r=28, color=RED)
    for k, (x, y) in P.items():
        node(s, x, y, k, None, r=28)
    for k, (x, y) in Q.items():
        node(s, x, y, k, None, r=28, color=RED, fill="#fff5f5")
    s.text(130, 238, "wanted loop", size=13, weight="bold")
    s.text(440, 238, "unused states: a second loop, never returns", size=13, weight="bold", color=RED)
    save(s, "lockout")


# ============================================================ Topic 17
def registers():
    def chain(name, title, fb, note, init=None):
        s = Svg(720, 220, title)
        fs = []
        for i in range(4):
            x = 110 + i * 150
            f = ff(s, x, 50, "D", qn=(fb == "inv" and i == 3))
            fs.append(f)
            s.text(x + 42, 42, "ABCE"[i] if fb else "Q" + "₃₂₁₀"[i], size=14, weight="bold")
            if init:
                s.text(x + 42, 116, init[i], size=18, weight="bold", color=BLUE)
            if i:
                s.line([fs[i - 1]["Q"], (f["D"][0], f["D"][1])])
        ck = 176
        s.line([(40, ck), (fs[3]["C"][0] - 8, ck)]); label_in(s, (40, ck), "CLK", size=13)
        for f in fs:
            x = f["C"][0] - 8
            s.line([(x, ck), (x, f["C"][1]), f["C"]]); s.dot(x, ck)
        if fb is None:
            s.line([(40, fs[0]["D"][1]), fs[0]["D"]]); label_in(s, (40, fs[0]["D"][1]), "SI", size=13)
            s.line([fs[3]["Q"], (680, fs[3]["Q"][1])]); s.text(676, fs[3]["Q"][1] - 8, "SO", size=13, anchor="end", weight="bold")
        else:
            col = RED if fb == "inv" else BLUE
            q = fs[3]["Qn"] if fb == "inv" else fs[3]["Q"]
            s.line([q, (700, q[1]), (700, 12), (70, 12), (70, fs[0]["D"][1]), fs[0]["D"]], col)
            if fb == "inv":
                s.text(690, q[1] + 20, "E'", size=14, weight="bold", color=col, anchor="end")
        s.text(350, 208, note, size=12, color=MUTED)
        save(s, name)

    chain("shift-register", "4-bit shift register", None, "every clock edge, each bit moves one flip-flop to the right")
    chain("ring-counter", "Ring counter", "plain", "last Q back to first D · one 1 goes round: 1000 → 0100 → 0010 → 0001 → 1000", init="1000")
    chain("johnson-counter", "Johnson (switch-tail) counter", "inv", "last Q' (inverted) back to first D · 4 flip-flops give 8 states", init="0000")

    # universal shift register: one stage
    s = Svg(560, 250, "One stage of a universal shift register")
    from build_svg import mux_shape
    p = mux_shape(s, 190, 20, 4, ["Aᵢ (hold)", "Aᵢ₊₁ (shift right)", "Aᵢ₋₁ (shift left)", "Iᵢ (parallel load)"], ["s₁", "s₀"], out=None)
    f = ff(s, 400, 60, "D", qn=False)
    s.line([p["y"], (p["y"][0] + 20, p["y"][1]), (p["y"][0] + 20, f["D"][1]), f["D"]])
    label_out(s, f["Q"], "Aᵢ")
    s.line([(f["C"][0] - 16, f["C"][1]), f["C"]]); label_in(s, (f["C"][0] - 16, f["C"][1]), "CLK", size=12)
    s.text(280, 242, "a 4-to-1 mux in front of every flip-flop chooses what it loads next", size=12, color=MUTED)
    save(s, "universal-stage")


# ============================================================ Topic 20
def async_logic():
    # transition table
    s = Svg(430, 330, "Transition table")
    ox, oy, cw, ch = 150, 80, 110, 52
    s.text(ox + cw, 30, "x", size=16, weight="bold")
    for c, t in enumerate(("0", "1")):
        s.text(ox + c * cw + cw / 2, oy - 12, t, size=15, color=MUTED)
    s.text(ox - 70, oy + 2 * ch + 5, "y₁y₂", size=16, weight="bold")
    rows = [("00", "00", "01"), ("01", "11", "01"), ("11", "11", "10"), ("10", "00", "10")]
    for r, (y, a, b) in enumerate(rows):
        s.text(ox - 22, oy + r * ch + ch / 2 + 6, y, size=15, color=MUTED)
        for c, v in enumerate((a, b)):
            x0, y0 = ox + c * cw, oy + r * ch
            s.rect(x0, y0, cw, ch, stroke="#8c959f", width=1.5)
            if v == y:
                s.add(f'<ellipse cx="{x0+cw/2}" cy="{y0+ch/2}" rx="26" ry="18" fill="{COL["blue"][1]}" stroke="{BLUE}" stroke-width="2.5"/>')
            s.text(x0 + cw / 2, y0 + ch / 2 + 6, v, size=18, weight="bold", color=BLUE if v == y else INK)
    s.rect(ox, oy, 2 * cw, 4 * ch, width=2)
    s.text(215, 310, "entry = Y₁Y₂ (next) · circled = stable, because Y = y", size=12, color=MUTED)
    save(s, "transition-table")

    # hazard K-map
    names = V(["x₁", "x₂", "x₃"])
    s = Svg(640, 300, "Static-1 hazard and its fix")
    kmap(names, vals(3, [1, 5, 6, 7]), [{"cells": [6, 7], "color": "red", "label": "x₁x₂"}, {"cells": [1, 5], "color": "blue", "label": "x₂'x₃"}],
         s=s, x0=0, y0=0, title="Before: hazard", cell=50)
    kmap(names, vals(3, [1, 5, 6, 7]), [{"cells": [6, 7], "color": "red", "label": "x₁x₂"}, {"cells": [1, 5], "color": "blue", "label": "x₂'x₃"},
                                         {"cells": [5, 7], "color": "green", "label": "x₁x₃ (bridge)"}],
         s=s, x0=320, y0=0, title="After: bridge added", cell=50)
    save(s, "hazard-kmap")

    # hazard timing
    s = Svg(520, 190, "Static-1 hazard glitch")
    timing(s, 20, 20, [("x₂", "1111000000"), ("x₁x₂", "1111100000", RED), ("x₂'x₃", "0000001111", BLUE), ("Y", "1111101111", ORANGE)],
           step=60, label_w=80, h=22, gap=16)
    s.text(280, 180, "the inverter makes x₂'x₃ rise late → for a moment both terms are 0 → Y dips", size=12, color=MUTED)
    save(s, "hazard-glitch")


# ============================================================ Topic 21
def cmos():
    s = Svg(720, 330, "CMOS inverter, NAND and NOR")
    # inverter
    x = 60
    d, sp = mos(s, x, 90, p=True); dn, sn = mos(s, x, 190)
    vdd(s, d[0], d[1]); gnd(s, sn[0], sn[1])
    s.line([sp, dn]); s.line([(x, 90), (x, 190)]); s.line([(x - 22, 140), (x, 140)]); s.dot(x, 140); label_in(s, (x - 22, 140), "A")
    s.line([(sp[0], 140), (sp[0] + 34, 140)]); s.dot(sp[0], 140); label_out(s, (sp[0] + 34, 140), "Y")
    s.text(x + 40, 262, "NOT", size=15, weight="bold"); s.text(x + 40, 282, "2 transistors", size=12, color=MUTED)
    # NAND: PMOS parallel, NMOS series
    x = 260
    d1, s1 = mos(s, x, 80, p=True, label="A"); d2, s2 = mos(s, x + 110, 80, p=True, label="B")
    s.line([d1, d2]); vdd(s, (d1[0] + d2[0]) / 2, d1[1])
    s.line([s1, s2])
    n1d, n1s = mos(s, x, 170, label="A"); n2d, n2s = mos(s, x, 226, label="B")
    s.line([s1, n1d]); gnd(s, n2s[0], n2s[1])
    oy = 125
    s.line([(s2[0], s2[1]), (s2[0] + 36, s2[1])]); s.dot(*s2); label_out(s, (s2[0] + 36, s2[1]), "Y")
    s.text(x + 80, 292, "NAND", size=15, weight="bold"); s.text(x + 80, 312, "PMOS parallel · NMOS series", size=12, color=MUTED)
    # NOR: PMOS series, NMOS parallel
    x = 500
    p1d, p1s = mos(s, x, 60, p=True, label="A"); p2d, p2s = mos(s, x, 116, p=True, label="B")
    vdd(s, p1d[0], p1d[1])
    n1d, n1s = mos(s, x, 210, label="A"); n2d, n2s = mos(s, x + 110, 210, label="B")
    s.line([p2s, (p2s[0], n1d[1])]); s.line([n1d, n2d]); s.line([n1s, n2s]); gnd(s, (n1s[0] + n2s[0]) / 2, n1s[1])
    s.line([n2d, (n2d[0] + 30, n2d[1])]); s.dot(*n2d); label_out(s, (n2d[0] + 30, n2d[1]), "Y")
    s.text(x + 80, 292, "NOR", size=15, weight="bold"); s.text(x + 80, 312, "PMOS series · NMOS parallel", size=12, color=MUTED)
    save(s, "cmos-gates")


if __name__ == "__main__":
    latches(); fsm_1001_circuit(); fsm_diagrams(); kmaps_1001(); counters(); registers(); async_logic(); cmos()
    print("ok", len(os.listdir(OUT)))
