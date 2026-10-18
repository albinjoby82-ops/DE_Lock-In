"""Build every drawn diagram into docs/svg/. Run: python3 tools/build_svg.py"""
import os, math
from svglib import Svg, Gate, wire, label_in, label_out, block, kmap, INK, MUTED, COL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "svg")
os.makedirs(OUT, exist_ok=True)


def save(s, name):
    s.save(os.path.join(OUT, name + ".svg"))


def ones(ms, dc=(), nv=3):
    v = {m: "0" for m in range(2 ** nv)}
    for m in ms:
        v[m] = "1"
    for m in dc:
        v[m] = "X"
    return v


# ======================================================== K-maps (Topics 8, 9, 10)
def kmaps():
    # cell-number maps
    save(kmap("ABC", {m: str(m) for m in range(8)}, show_idx=False, title="3-variable map: cell numbers"), "k3-index")
    save(kmap("ABCD", {m: str(m) for m in range(16)}, show_idx=False, title="4-variable map: cell numbers"), "k4-index")
    # 2-variable example
    save(kmap("AB", ones([0, 2, 3], nv=2), [
        {"cells": [0, 2], "color": "red", "label": "B'"},
        {"cells": [2, 3], "color": "blue", "label": "A"}], caption="C = B' + A"), "k2-example")
    # 3-variable SOP example (slide 16)
    save(kmap("ABC", ones([0, 2, 3, 4, 7]), [
        {"cells": [0, 2], "color": "red", "label": "A'C'"},
        {"cells": [3, 7], "color": "blue", "label": "BC"},
        {"cells": [0, 4], "color": "green", "label": "B'C'"}], caption="F = A'C' + BC + B'C'"), "k3-sop")
    # same, POS
    save(kmap("ABC", ones([0, 2, 3, 4, 7]), [
        {"cells": [6], "color": "red", "label": "(A'+B'+C)"},
        {"cells": [1, 5], "color": "blue", "label": "(B+C')"}], caption="F = (A'+B'+C)(B+C')"), "k3-pos")
    # 4-variable example (slide 20)
    save(kmap("ABCD", ones([0, 1, 4, 5, 12, 13, 8, 9, 2, 6], nv=4), [
        {"cells": [0, 1, 4, 5, 12, 13, 8, 9], "color": "red", "label": "C'"},
        {"cells": [0, 2, 4, 6], "color": "blue", "label": "A'D'"}], caption="F = C' + A'D'"), "k4-sop")
    # corners
    save(kmap("ABCD", ones([0, 2, 5, 7, 8, 10, 13, 15], nv=4), [
        {"cells": [0, 2, 8, 10], "color": "green", "label": "B'D'"},
        {"cells": [5, 7, 13, 15], "color": "blue", "label": "BD"}], caption="F = B'D' + BD"), "k4-corners")
    # fill from expression (slides 23-25)
    save(kmap("ABC", ones([2, 3, 6, 7, 5]), [
        {"cells": [2, 3, 6, 7], "color": "red", "label": "B"},
        {"cells": [5, 7], "color": "blue", "label": "AC"}], caption="F = B + AC"), "k3-fill")
    # don't cares
    save(kmap("ABC", ones([0, 2, 3, 4, 7], dc=[6]), [
        {"cells": [0, 2], "color": "red", "label": "A'C'"},
        {"cells": [3, 7], "color": "blue", "label": "BC"},
        {"cells": [0, 4], "color": "green", "label": "B'C'"}], title="x used as 0", caption="3 terms"), "dc-before")
    save(kmap("ABC", ones([0, 2, 3, 4, 7], dc=[6]), [
        {"cells": [0, 2, 6, 4], "color": "red", "label": "C'"},
        {"cells": [2, 3, 6, 7], "color": "blue", "label": "B"}], title="x used as 1", caption="F = C' + B"), "dc-after")
    # NAND example slide 14
    save(kmap("ABCD", ones([2, 3] + list(range(8, 16)), nv=4), [
        {"cells": list(range(8, 16)), "color": "red", "label": "A"},
        {"cells": [2, 3, 10, 11], "color": "blue", "label": "B'C"}], caption="F = A + B'C"), "k4-nand")
    # NOR example slide 15 (group the 0s)
    save(kmap("ABCD", ones([8, 9, 10, 12, 13, 14, 15], nv=4), [
        {"cells": list(range(0, 8)), "color": "red", "label": "(A)"},
        {"cells": [3, 11], "color": "blue", "label": "(B+C'+D')"}], caption="F = A(B+C'+D')"), "k4-nor")
    # full adder maps
    save(kmap("XYZ", ones([3, 5, 6, 7]), [
        {"cells": [6, 7], "color": "red", "label": "XY"},
        {"cells": [3, 7], "color": "blue", "label": "YZ"},
        {"cells": [5, 7], "color": "green", "label": "XZ"}], title="Carry C", caption="C = XY + YZ + XZ"), "k-fa-carry")
    save(kmap("XYZ", ones([1, 2, 4, 7]), [], title="Sum S", caption="checkerboard: no groups"), "k-fa-sum")


# ======================================================== gates (Topic 6, 9)
def gates():
    kinds = [("AND", "F = AB", "1 if all inputs are 1"),
             ("OR", "F = A + B", "1 if any input is 1"),
             ("NOT", "F = A'", "flips the input"),
             ("XOR", "F = A ⊕ B", "1 if inputs differ"),
             ("NAND", "F = (AB)'", "0 only if all are 1"),
             ("NOR", "F = (A + B)'", "1 only if all are 0"),
             ("XNOR", "F = (A ⊕ B)'", "1 if inputs equal")]
    s = Svg(4 * 210 + 20, 2 * 170 + 20, "Logic gates")
    for i, (k, eq, rule) in enumerate(kinds):
        cx, cy = 20 + (i % 4) * 210, 20 + (i // 4) * 170
        s.rect(cx, cy, 196, 156, stroke="#d0d7de", fill="#f6f8fa", rx=8, width=1.5)
        s.text(cx + 98, cy + 24, k, size=16, weight="bold")
        n = 1 if k == "NOT" else 2
        g = Gate(s, k, cx + 74, cy + 36, n=n)
        for j, p in enumerate(g.ins):
            s.line([(cx + 34, p[1]), p])
            label_in(s, (cx + 34, p[1]), "AB"[j], dx=-4)
        s.line([g.out, (cx + 170, g.out[1])])
        label_out(s, (cx + 170, g.out[1]), "F", dx=3, size=14)
        s.text(cx + 98, cy + 120, eq, size=15)
        s.text(cx + 98, cy + 142, rule, size=12, color=MUTED)
    save(s, "gates")

    # NAND = OR with bubbled inputs ; NOR = AND with bubbled inputs
    s = Svg(620, 210, "De Morgan gate equivalents")
    for row, (a, b, t1, t2) in enumerate([("NAND", "OR", "(AB)'", "A' + B'"), ("NOR", "AND", "(A+B)'", "A'B'")]):
        y = 20 + row * 95
        g1 = Gate(s, a, 70, y, 2)
        for j, p in enumerate(g1.ins):
            s.line([(40, p[1]), p]); label_in(s, (40, p[1]), "AB"[j], dx=-4)
        s.line([g1.out, (160, g1.out[1])]); s.text(165, g1.out[1] + 5, t1, size=15, anchor="start")
        s.text(300, y + 26, "=", size=26, weight="bold")
        g2 = Gate(s, b, 400, y, 2, inbub=True)
        for j, p in enumerate(g2.ins):
            s.line([(350, p[1]), p]); label_in(s, (350, p[1]), "AB"[j], dx=-4)
        s.line([g2.out, (480, g2.out[1])]); s.text(485, g2.out[1] + 5, t2, size=15, anchor="start")
    s.text(310, 200, "bubble = NOT.  Flip the letters, swap AND ↔ OR (De Morgan).", size=13, color=MUTED)
    save(s, "demorgan-gates")


# ======================================================== two-level circuits
def route_fan_in(s, srcs, dsts, xlo, xhi):
    """Wire each src->dst with one vertical jog; choose jog x per wire to minimise crossings."""
    import itertools
    n = len(srcs)
    xs = [xlo + (xhi - xlo) * (k + 1) / (n + 1) for k in range(n)]
    def cost(order):
        c = 0
        for i in range(n):
            for j in range(n):
                if i == j: continue
                mi, mj = xs[order[i]], xs[order[j]]
                # horizontal dst segment of i (mi -> dst x) at y=dst_i crosses vertical of j?
                lo, hi = sorted((srcs[j][1], dsts[j][1]))
                if mj > mi and lo < dsts[i][1] < hi: c += 1
                lo2, hi2 = sorted((srcs[i][1], dsts[i][1]))
                # horizontal src segment of j (src -> mj) crosses vertical of i?
                if mi < mj and lo2 < srcs[j][1] < hi2: c += 1
        return c
    best = min(itertools.permutations(range(n)), key=cost)
    for i in range(n):
        wire(s, srcs[i], dsts[i], midx=xs[best[i]])


def two_level(s, terms, out_kind, first_kind, x_in=60, y0=20, gap=18, out_name="F", gx=150, ox=320):
    """terms: list of lists of input labels; a 1-literal term goes straight to the output gate."""
    srcs = []
    y = y0
    for t in terms:
        if len(t) == 1:
            py = y + 14
            s.line([(x_in, py), (gx + 66, py)])
            label_in(s, (x_in, py), t[0])
            srcs.append((gx + 66, py))
            y += 34
        else:
            g = Gate(s, first_kind, gx, y, len(t))
            for lab, p in zip(t, g.ins):
                s.line([(x_in, p[1]), p])
                label_in(s, (x_in, p[1]), lab)
            srcs.append(g.out)
            y += g.h + gap
    mid = (srcs[0][1] + srcs[-1][1]) / 2
    og = Gate(s, out_kind, ox, 0, len(srcs))
    # recentre: re-draw at the right y (Gate draws immediately, so build on a scratch first)
    s.parts.pop()
    og = Gate(s, out_kind, ox, mid - og.h / 2, len(srcs))
    route_fan_in(s, srcs, og.ins, gx + 72, ox - 6)
    s.line([og.out, (og.out[0] + 30, og.out[1])])
    label_out(s, (og.out[0] + 30, og.out[1]), out_name)
    return y


def fit(s, y, pad=14):
    s.h = int(y + pad)
    return s


def circuits_two_level():
    s = Svg(440, 10, "SOP circuit")
    y = two_level(s, [["A'", "C'"], ["B", "C"], ["B'", "C'"]], "OR", "AND")
    s.text(220, y + 10, "SOP = AND gates → one OR gate", size=13, color=MUTED)
    save(fit(s, y + 10), "sop-circuit")

    s = Svg(440, 10, "POS circuit")
    y = two_level(s, [["A'", "B'", "C"], ["B", "C'"]], "AND", "OR")
    s.text(220, y + 10, "POS = OR gates → one AND gate", size=13, color=MUTED)
    save(fit(s, y + 10), "pos-circuit")

    s = Svg(440, 10, "Simplify x'y' + xyz + x'y")
    s.text(20, 22, "Before: x'y' + xyz + x'y  (4 gates, 10 inputs)", size=15, anchor="start", weight="bold")
    y = two_level(s, [["x'", "y'"], ["x", "y", "z"], ["x'", "y"]], "OR", "AND", y0=40, out_name="f")
    s.text(20, y + 14, "After: x' + yz  (2 gates, 4 inputs)", size=15, anchor="start", weight="bold")
    y = two_level(s, [["y", "z"], ["x'"]], "OR", "AND", y0=y + 30, out_name="f")
    save(fit(s, y), "simplify-circuit")

    s = Svg(900, 10, "AND-OR to NAND-NAND")
    s.text(210, 20, "1. AND-OR (from the SOP)", size=15, weight="bold")
    y = two_level(s, [["A", "B"], ["C", "D"], ["E"]], "OR", "AND", y0=36)
    s.add('<g transform="translate(460,0)">')
    s.text(210, 20, "2. Every gate → NAND.  Lone E → E'", size=15, weight="bold")
    two_level(s, [["A", "B"], ["C", "D"], ["E'"]], "NAND", "NAND", y0=36)
    s.add("</g>")
    s.arrow([(424, 100), (456, 100)], color=COL["blue"][0], width=3)
    save(fit(s, y), "nand-transform")

    s = Svg(440, 10, "NAND-NAND F = A + B'C")
    y = two_level(s, [["B'", "C"], ["A'"]], "NAND", "NAND", y0=20)
    s.text(220, y + 12, "F = ((B'C)' · A)' = A + B'C", size=14, color=MUTED)
    save(fit(s, y + 12), "nand-slide14")

    s = Svg(440, 10, "NOR-NOR F = A(B + C' + D')")
    y = two_level(s, [["B", "C'", "D'"], ["A'"]], "NOR", "NOR", y0=20)
    s.text(220, y + 12, "F = ((B+C'+D')' + A')' = A(B + C' + D')", size=14, color=MUTED)
    save(fit(s, y + 12), "nor-slide15")


# ======================================================== adders (Topic 10)
def adders():
    # half adder
    s = Svg(420, 190, "Half adder")
    xg = Gate(s, "XOR", 190, 16, 2)
    ag = Gate(s, "AND", 190, 110, 2)
    s.line([(50, xg.ins[0][1]), xg.ins[0]]); label_in(s, (50, xg.ins[0][1]), "X")
    s.line([(50, xg.ins[1][1]), xg.ins[1]]); label_in(s, (50, xg.ins[1][1]), "Y")
    wire(s, (100, xg.ins[0][1]), ag.ins[0], midx=100, dots=[(100, xg.ins[0][1])])
    wire(s, (130, xg.ins[1][1]), ag.ins[1], midx=130, dots=[(130, xg.ins[1][1])])
    s.line([xg.out, (290, xg.out[1])]); label_out(s, (290, xg.out[1]), "S = X ⊕ Y")
    s.line([ag.out, (290, ag.out[1])]); label_out(s, (290, ag.out[1]), "C = XY")
    save(s, "half-adder")

    # full adder from two half adders
    s = Svg(700, 300, "Full adder from two half adders")
    s.rect(80, 8, 210, 240, stroke=COL["blue"][0], fill="#0969da0d", rx=10, dash="6 4")
    s.text(185, 28, "half adder 1", size=13, color=COL["blue"][0], weight="bold")
    s.rect(330, 8, 200, 240, stroke=COL["green"][0], fill="#1a7f370d", rx=10, dash="6 4")
    s.text(430, 28, "half adder 2", size=13, color=COL["green"][0], weight="bold")
    x1 = Gate(s, "XOR", 200, 40, 2)
    a1 = Gate(s, "AND", 200, 170, 2)
    x2 = Gate(s, "XOR", 440, 46, 2)
    a2 = Gate(s, "AND", 440, 120, 2)
    s.line([(40, x1.ins[0][1]), x1.ins[0]]); label_in(s, (40, x1.ins[0][1]), "X")
    s.line([(40, x1.ins[1][1]), x1.ins[1]]); label_in(s, (40, x1.ins[1][1]), "Y")
    wire(s, (120, x1.ins[0][1]), a1.ins[0], midx=120, dots=[(120, x1.ins[0][1])])
    wire(s, (150, x1.ins[1][1]), a1.ins[1], midx=150, dots=[(150, x1.ins[1][1])])
    # S1 -> XOR2 in0 and AND2 in0
    wire(s, x1.out, x2.ins[0], midx=380)
    wire(s, (380, x2.ins[0][1]), a2.ins[0], midx=380, dots=[(380, x2.ins[0][1])])
    s.text(330, x1.out[1] - 8, "S₁", size=14, color=COL["blue"][0], weight="bold")
    # Z -> XOR2 in1 and AND2 in1
    s.line([(40, 275), (405, 275), (405, a2.ins[1][1]), a2.ins[1]]); label_in(s, (40, 275), "Z")
    wire(s, (405, a2.ins[1][1]), x2.ins[1], midx=405, dots=[(405, a2.ins[1][1])])
    og = Gate(s, "OR", 590, 150, 2)
    wire(s, a2.out, og.ins[0], midx=560)
    s.text(548, a2.out[1] - 8, "C₂", size=14, color=COL["green"][0], weight="bold")
    wire(s, a1.out, og.ins[1], midx=575)
    s.text(320, a1.out[1] - 8, "C₁", size=14, color=COL["blue"][0], weight="bold")
    s.line([x2.out, (660, x2.out[1])]); label_out(s, (660, x2.out[1]), "S", dx=6)
    s.line([og.out, (660, og.out[1])]); label_out(s, (660, og.out[1]), "C", dx=6)
    save(s, "fa-two-ha")

    # 4-bit ripple carry adder
    s = Svg(760, 205, "4-bit ripple carry adder")
    for i in range(4):
        bit = 3 - i
        x = 70 + i * 165
        s.rect(x, 60, 100, 70, fill="#f6f8fa", rx=8)
        s.text(x + 50, 101, "FA", size=18, weight="bold")
        s.line([(x + 30, 34), (x + 30, 60)]); s.text(x + 30, 26, f"A{bit}", size=14)
        s.line([(x + 70, 34), (x + 70, 60)]); s.text(x + 70, 26, f"B{bit}", size=14)
        s.line([(x + 50, 130), (x + 50, 156)]); s.text(x + 50, 175, f"S{bit}", size=15, weight="bold")
        s.arrow([(x + 165, 95), (x + 102, 95)], color=COL["red"][0])
        s.text(x + 134, 86, f"C{bit}", size=13, color=COL["red"][0], weight="bold")
    s.arrow([(70, 95), (20, 95)], color=COL["red"][0])
    s.text(40, 86, "C4", size=13, color=COL["red"][0], weight="bold")
    s.text(752, 114, "C0 = 0", size=12, anchor="end", color=MUTED)
    s.text(380, 198, "carry ripples right → left: each FA waits for the one before (≈ 2n gate delays)", size=12, color=MUTED)
    save(s, "ripple4")

    # adder-subtractor
    s = Svg(800, 280, "4-bit adder-subtractor")
    MB = 112
    pc = COL["purple"][0]
    for i in range(4):
        bit = 3 - i
        x = 90 + i * 170
        s.rect(x, 140, 110, 64, fill="#f6f8fa", rx=8)
        s.text(x + 55, 178, "FA", size=18, weight="bold")
        g = Gate(s, "XOR", x + 14, 40, 2)
        s.line([(x - 2, 30), (x - 2, g.ins[0][1]), g.ins[0]]); s.text(x - 2, 24, f"B{bit}", size=14)
        s.line([(x + 4, MB), (x + 4, g.ins[1][1]), g.ins[1]], color=pc); s.dot(x + 4, MB, color=pc)
        s.line([g.out, (x + 84, g.out[1]), (x + 84, 140)])
        s.line([(x + 100, 30), (x + 100, 140)]); s.text(x + 100, 24, f"A{bit}", size=14)
        s.line([(x + 55, 204), (x + 55, 230)]); s.text(x + 55, 248, f"S{bit}", size=15, weight="bold")
        s.arrow([(x + 170, 172), (x + 112, 172)], color=COL["red"][0])
    s.line([(40, MB), (770, MB), (770, 172), (762, 172)], color=pc, width=2.5)
    s.text(34, MB + 5, "M", size=16, anchor="end", weight="bold", color=pc)
    s.text(792, 196, "C0 = M", size=12, anchor="end", color=pc)
    s.arrow([(90, 172), (40, 172)], color=COL["red"][0]); s.text(52, 164, "C4", size=13, color=COL["red"][0])
    s.text(400, 272, "M = 0: B passes, C0 = 0 → A + B      M = 1: B flipped, C0 = 1 → A + B' + 1 = A − B", size=13, color=MUTED)
    save(s, "add-sub")

    # 2x2 multiplier
    s = Svg(700, 290, "2-bit by 2-bit multiplier")
    ands = []
    labels = [("A0", "B0"), ("A1", "B0"), ("A0", "B1"), ("A1", "B1")]
    for i, (a, b) in enumerate(labels):
        g = Gate(s, "AND", 90, 14 + i * 64, 2)
        s.line([(46, g.ins[0][1]), g.ins[0]]); label_in(s, (46, g.ins[0][1]), a, size=13)
        s.line([(46, g.ins[1][1]), g.ins[1]]); label_in(s, (46, g.ins[1][1]), b, size=13)
        ands.append(g)
    p1 = block(s, 310, 70, 90, 90, "HA", left=["a", "b"], right=["S", "C"])
    p2 = block(s, 480, 150, 90, 90, "HA", left=["a", "b"], right=["S", "C"])
    s.line([ands[0].out, (630, ands[0].out[1])]); label_out(s, (630, ands[0].out[1]), "C0")
    wire(s, ands[1].out, p1["a"], midx=230)
    wire(s, ands[2].out, p1["b"], midx=250)
    s.line([p1["S"], (630, p1["S"][1])]); label_out(s, (630, p1["S"][1]), "C1")
    wire(s, p1["C"], p2["a"], midx=440)
    s.text(440, p1["C"][1] - 8, "K", size=13, color=MUTED, weight="bold")
    wire(s, ands[3].out, p2["b"], midx=270)
    s.line([p2["S"], (630, p2["S"][1])]); label_out(s, (630, p2["S"][1]), "C2")
    s.line([p2["C"], (630, p2["C"][1])]); label_out(s, (630, p2["C"][1]), "C3")
    s.text(350, 282, "C3 C2 C1 C0 are the PRODUCT bits, not carries", size=13, color=MUTED)
    save(s, "mult2x2")


# ======================================================== mux / decoder blocks
def mux_shape(s, x, y, n, data, sels, out="Y", pitch=30, title=None, pin=30):
    H = pitch * (n + 1)
    W = max(70, 34 * (len(sels) + 1))
    s.add(f'<path d="M{x},{y} L{x+W},{y+H*0.18} L{x+W},{y+H*0.82} L{x},{y+H} Z" fill="#f6f8fa" stroke="{INK}" stroke-width="2"/>')
    s.text(x + W / 2, y + H / 2 + 5, title or f"{n}-to-1", size=12, weight="bold", color=MUTED)
    pins = {"d": [], "s": []}
    for i in range(n):
        py = y + pitch * (i + 1)
        s.line([(x - pin, py), (x, py)])
        s.text(x + 5, py + 4, f"{i}", size=11, anchor="start", color=MUTED)
        if data and data[i] is not None:
            s.text(x - pin - 6, py + 5, data[i], size=15, anchor="end", weight="bold")
        pins["d"].append((x - pin, py))
    k = len(sels)
    for j, nm in enumerate(sels):
        px = x + W * (j + 1) / (k + 1)
        ey = y + H - (H * 0.18) * (px - x) / W
        s.line([(px, ey), (px, y + H + 26)])
        s.text(px, y + H + 42, nm, size=14, weight="bold")
        pins["s"].append((px, y + H + 26))
    oy = y + H / 2
    s.line([(x + W, oy), (x + W + pin, oy)])
    if out:
        label_out(s, (x + W + pin, oy), out)
    pins["y"] = (x + W + pin, oy)
    pins["H"] = H
    return pins


def muxes():
    # 2-to-1 at gate level
    s = Svg(460, 200, "2-to-1 multiplexer")
    a0 = Gate(s, "AND", 200, 20, 2)
    a1 = Gate(s, "AND", 200, 110, 2)
    og = Gate(s, "OR", 330, 56, 2)
    s.line([(50, a0.ins[0][1]), a0.ins[0]]); label_in(s, (50, a0.ins[0][1]), "I₀")
    s.line([(50, a1.ins[1][1]), a1.ins[1]]); label_in(s, (50, a1.ins[1][1]), "I₁")
    sy = 185
    s.line([(50, sy), (110, sy)]); label_in(s, (50, sy), "S")
    nt = Gate(s, "NOT", 120, sy - 14, 1, h=28)
    s.line([(110, sy), nt.ins[0]])
    s.line([nt.out, (170, sy), (170, a0.ins[1][1]), a0.ins[1]])
    s.text(176, a0.ins[1][1] + 18, "S'", size=13, anchor="start", color=MUTED)
    s.line([(95, sy), (95, a1.ins[0][1]), a1.ins[0]]); s.dot(95, sy)
    route_fan_in(s, [a0.out, a1.out], og.ins, 270, 326)
    s.line([og.out, (420, og.out[1])]); label_out(s, (420, og.out[1]), "Y")
    s.text(330, 180, "Y = S'I₀ + SI₁", size=15, anchor="start", weight="bold")
    s.w, s.h = 470, 205
    save(s, "mux2-gates")

    # 4-to-1 block with table
    s = Svg(470, 230, "4-to-1 multiplexer")
    mux_shape(s, 90, 20, 4, ["I₀", "I₁", "I₂", "I₃"], ["S₁", "S₀"])
    tx = 300
    s.text(tx, 40, "S₁ S₀ → Y", size=15, anchor="start", weight="bold")
    for i in range(4):
        s.text(tx, 68 + 26 * i, f" {i>>1}   {i&1}  →  I{'₀₁₂₃'[i]}", size=15, anchor="start")
    s.text(tx, 190, "selects = a number", size=13, anchor="start", color=MUTED)
    s.text(tx, 208, "that number picks the input", size=13, anchor="start", color=MUTED)
    save(s, "mux4-block")

    # method 2 example: f = Σm(1,2,6,7) on 4-to-1
    s = Svg(420, 240, "f = Σm(1,2,6,7) on a 4-to-1 mux")
    p = mux_shape(s, 120, 20, 4, ["z", "z'", "0", "1"], ["x", "y"], out="f")
    s.text(210, 232, "selects x y, last variable z on the data inputs", size=12, color=MUTED)
    save(s, "mux-method2")

    # 8-to-1 example
    s = Svg(440, 380, "F = Σm(1,3,4,11,12,13,14,15) on an 8-to-1 mux")
    mux_shape(s, 140, 20, 8, ["D", "D", "D'", "0", "0", "D", "1", "1"], ["A", "B", "C"], out="F", pitch=34)
    s.text(220, 372, "selects A B C; data inputs are 0, 1, D or D'", size=12, color=MUTED)
    save(s, "mux8-example")

    # 16-to-1 tree
    s = Svg(560, 560, "16-to-1 from five 4-to-1 muxes")
    outs = []
    for k in range(4):
        y = 14 + k * 128
        p = mux_shape(s, 100, y, 4, [f"{4*k+i}" for i in range(4)], [], out=None, pitch=20, title="4:1", pin=24)
        s.text(135, y + p["H"] + 16, "A₁A₀", size=12, color=COL["blue"][0], weight="bold")
        outs.append(p["y"])
    p2 = mux_shape(s, 360, 200, 4, None, ["A₃", "A₂"], out="Y", pitch=30, title="4:1")
    route_fan_in(s, outs, p2["d"], 200, 330)
    s.text(110, 548, "first level shares A₁A₀; second level uses A₃A₂", size=13, anchor="start", color=MUTED)
    save(s, "mux16-tree")

    # demux 1-to-4
    s = Svg(440, 220, "1-to-4 demultiplexer")
    x, y, H, W = 150, 20, 150, 70
    s.add(f'<path d="M{x},{y+H*0.18} L{x+W},{y} L{x+W},{y+H} L{x},{y+H*0.82} Z" fill="#f6f8fa" stroke="{INK}" stroke-width="2"/>')
    s.text(x + W / 2, y + H / 2 + 5, "1-to-4", size=12, weight="bold", color=MUTED)
    s.line([(x - 40, y + H / 2), (x, y + H / 2)]); label_in(s, (x - 40, y + H / 2), "I₀")
    for i in range(4):
        py = y + 30 * (i + 1)
        s.line([(x + W, py), (x + W + 30, py)]); label_out(s, (x + W + 30, py), f"F{'₀₁₂₃'[i]}")
    for j, nm in enumerate(["S₁", "S₀"]):
        px = x + W * (j + 1) / 3
        ey = y + H * 0.82 + (H * 0.18) * (px - x) / W
        s.line([(px, ey), (px, y + H + 26)]); s.text(px, y + H + 42, nm, size=14, weight="bold")
    s.text(330, 212, "selects pick which output gets I₀", size=12, color=MUTED)
    save(s, "demux")


def decoders():
    # 2-to-4 decoder at gate level with rails
    s = Svg(560, 450, "2-to-4 decoder")
    rails = {"A₁": 200, "A₁'": 240, "A₀": 280, "A₀'": 320}
    bot = 420
    for nm, yin, rp, rn in (("A₁", 40, 200, 240), ("A₀", 110, 280, 320)):
        s.line([(40, yin), (rp, yin), (rp, bot)]); label_in(s, (40, yin), nm); s.dot(rp, yin)
        s.line([(100, yin), (100, yin + 30)]); s.dot(100, yin)
        g = Gate(s, "NOT", 116, yin + 16, 1, h=28)
        s.line([(100, yin + 30), g.ins[0]])
        s.line([g.out, (rn, yin + 30), (rn, bot)]); s.dot(rn, yin + 30)
    for nm, x in rails.items():
        s.text(x, 440, nm, size=12, color=MUTED)
    combos = [("A₁'", "A₀'"), ("A₁'", "A₀"), ("A₁", "A₀'"), ("A₁", "A₀")]
    for i, (r1, r0) in enumerate(combos):
        g = Gate(s, "AND", 370, 170 + i * 62, 2)
        for rn, p in zip((r1, r0), g.ins):
            x = rails[rn]
            s.line([(x, p[1]), p]); s.dot(x, p[1])
        s.line([g.out, (450, g.out[1])])
        label_out(s, (450, g.out[1]), f"Z{'₀₁₂₃'[i]} = {r1}{r0}")
    save(s, "dec2to4-gates")

    # decoder + OR = full adder
    for low in (False, True):
        s = Svg(520, 330, "Full adder on a 3-to-8 decoder" + (" (active-low)" if low else ""))
        x, y, w, h = 110, 20, 110, 290
        s.rect(x, y, w, h, fill="#f6f8fa", rx=6)
        s.text(x + w / 2, y + 22, "3-to-8", size=14, weight="bold")
        s.text(x + w / 2, y + 40, "decoder", size=13, color=MUTED)
        for i, nm in enumerate(["X (MSB)", "Y", "Z"]):
            py = y + 90 + 50 * i
            s.line([(x - 40, py), (x, py)]); s.text(x - 46, py + 5, nm, size=14, anchor="end", weight="bold")
            s.text(x + 6, py + 4, "₂₁₀"[i], size=12, anchor="start", color=MUTED)
        if low:
            s.line([(x + w / 2, y + h), (x + w / 2, y + h + 0)])
        for i in range(8):
            py = y + 60 + 30 * i
            sx = x + w
            if low:
                s.add(f'<circle cx="{sx+4.5}" cy="{py}" r="4.5" fill="#fff" stroke="{INK}" stroke-width="2"/>')
                sx += 9
            s.line([(sx, py), (x + w + 40, py)])
            s.text(x + w - 6, py + 5, f"D{i}", size=13, anchor="end")
            s.text(x + w + 44, py + 5, f"D{i}", size=13, anchor="start", color=COL["blue"][0], weight="bold")
        kind = "AND" if low else "OR"
        sets = [("S", [0, 3, 5, 6] if low else [1, 2, 4, 7]), ("C", [0, 1, 2, 4] if low else [3, 5, 6, 7])]
        for k, (nm, ms) in enumerate(sets):
            g = Gate(s, kind, 380, 50 + k * 140, 4)
            for m, p in zip(ms, g.ins):
                s.line([(p[0] - 30, p[1]), p])
                s.text(p[0] - 34, p[1] + 5, f"D{m}", size=13, anchor="end", color=COL["blue"][0], weight="bold")
            s.line([g.out, (g.out[0] + 26, g.out[1])]); label_out(s, (g.out[0] + 26, g.out[1]), nm)
        note = "outputs are maxterms → AND the ΠM list" if low else "outputs are minterms → OR the Σm list"
        s.text(390, 322, note, size=12, color=MUTED)
        s.text(390, 306, "same blue label = same wire", size=12, color=MUTED)
        save(s, "dec-fa-low" if low else "dec-fa")

    # 3-to-8 from two 2-to-4 with enables
    s = Svg(520, 360, "3-to-8 decoder from two 2-to-4 decoders")
    for k in range(2):
        y = 20 + k * 170
        s.rect(220, y, 120, 140, fill="#f6f8fa", rx=6)
        s.text(280, y + 22, "2-to-4", size=14, weight="bold")
        for i, nm in enumerate(["S₁", "S₀"]):
            py = y + 60 + 34 * i
            s.text(226, py + 5, nm, size=12, anchor="start", color=MUTED)
        s.text(226, y + 130, "EN", size=12, anchor="start", color=MUTED)
        for i in range(4):
            py = y + 40 + 26 * i
            s.line([(340, py), (380, py)])
            label_out(s, (380, py), f"Q{4*k+i}", size=14)
    s.line([(40, 80), (220, 80)]); s.line([(160, 80), (160, 250)]); label_in(s, (40, 80), "S₁")
    s.line([(40, 114), (220, 114)]); s.line([(185, 114), (185, 284)]); label_in(s, (40, 114), "S₀")
    s.line([(160, 250), (220, 250)]); s.line([(185, 284), (220, 284)])
    s.dot(160, 80); s.dot(185, 114)
    s.line([(40, 320), (220, 320)]); label_in(s, (40, 320), "S₂")
    s.dot(56, 320)
    g = Gate(s, "NOT", 72, 218, 1, h=28)
    s.line([(56, 320), (56, 232), g.ins[0]])
    s.line([g.out, (205, 232), (205, 150), (220, 150)])
    s.text(140, 226, "S₂'", size=13, color=MUTED)
    s.text(400, 352, "S₂ picks which half is switched on", size=12, color=MUTED)
    save(s, "dec3to8-from-2to4")

    # 8-to-3 encoder
    s = Svg(440, 330, "8-to-3 encoder")
    for k, (nm, ms) in enumerate([("X", [4, 5, 6, 7]), ("Y", [2, 3, 6, 7]), ("Z", [1, 3, 5, 7])]):
        g = Gate(s, "OR", 150, 14 + k * 104, 4)
        for m, p in zip(ms, g.ins):
            s.line([(p[0] - 40, p[1]), p])
            s.text(p[0] - 46, p[1] + 5, f"D{m}", size=13, anchor="end", color=COL["blue"][0], weight="bold")
        s.line([g.out, (g.out[0] + 30, g.out[1])]); label_out(s, (g.out[0] + 30, g.out[1]), nm)
        s.text(g.out[0] + 60, g.out[1] + 5, ["4s bit", "2s bit", "1s bit"][k], size=12, anchor="start", color=MUTED)
    s.text(220, 324, "output bit = OR of every input whose number has that bit = 1", size=12, color=MUTED)
    save(s, "encoder8to3")


# ======================================================== numbers (Topics 2, 4)
def numbers():
    # place values
    bits = list("1101.01")
    w = [8, 4, 2, 1, None, 0.5, 0.25]
    s = Svg(560, 200, "Place values of 1101.01")
    x = 40
    tot = []
    for b, wt in zip(bits, w):
        if wt is None:
            s.text(x + 10, 72, ".", size=34, weight="bold"); x += 20; continue
        on = b == "1"
        s.rect(x, 40, 60, 46, stroke=COL["blue"][0] if on else "#8c959f", fill="#0969da18" if on else "#fff", rx=6)
        s.text(x + 30, 72, b, size=24, weight="bold", color=INK if on else MUTED)
        s.text(x + 30, 112, str(wt), size=16, color=COL["blue"][0] if on else MUTED, weight="bold" if on else "normal")
        s.text(x + 30, 28, ["2³", "2²", "2¹", "2⁰", "", "2⁻¹", "2⁻²"][len([t for t in tot]) + (1 if x > 300 else 0)] if False else "", size=12)
        if on:
            tot.append(str(wt))
        x += 70
    exps = ["2³", "2²", "2¹", "2⁰", "2⁻¹", "2⁻²"]
    xs = [40, 110, 180, 250, 340, 410]
    for e, xx in zip(exps, xs):
        s.text(xx + 30, 30, e, size=13, color=MUTED)
    s.text(40, 150, "add the weights under every 1:", size=14, anchor="start", color=MUTED)
    s.text(40, 178, "8 + 4 + 1 + 0.25 = 13.25", size=20, anchor="start", weight="bold")
    save(s, "place-value")

    # hex grouping with right-padding trap
    s = Svg(640, 210, "Binary to hex grouping")
    groups = [("0111", 1, "7"), ("1011", 0, "B"), (".", 0, "."), ("0010", 0, "2"), ("1000", 3, "8")]
    x = 30
    s.text(30, 24, "1111011.00101  →  group 4s outward from the point", size=15, anchor="start", weight="bold")
    for g, pad, h in groups:
        if g == ".":
            s.text(x + 8, 92, ".", size=34, weight="bold"); s.text(x + 8, 160, ".", size=30, weight="bold"); x += 24; continue
        s.rect(x, 50, 4 * 30 + 8, 56, stroke=COL["blue"][0], fill="#0969da10", rx=8)
        for i, b in enumerate(g):
            padbit = (pad and ((i < pad) if h == "7" else (i >= 4 - pad)))
            s.text(x + 19 + 30 * i, 86, b, size=24, weight="bold", color=COL["orange"][0] if padbit else INK)
        s.text(x + 64, 160, h, size=30, weight="bold", color=COL["blue"][0])
        s.arrow([(x + 64, 112), (x + 64, 134)], color=COL["blue"][0])
        x += 4 * 30 + 24
    s.text(30, 196, "orange = padding zeros: LEFT end of the whole part, RIGHT end of the fraction → 7B.28", size=13, anchor="start", color=COL["orange"][0])
    save(s, "hex-grouping")

    # 2's complement shortcut
    s = Svg(560, 210, "2's complement shortcut")
    a = "01010110"; r = "10101010"
    s.text(30, 24, "start at the right: copy up to and including the first 1, flip the rest", size=14, anchor="start", weight="bold")
    for i, (b, c) in enumerate(zip(a, r)):
        x = 40 + i * 58
        keep = i >= 6
        colr = COL["green"][0] if keep else COL["red"][0]
        s.rect(x, 44, 46, 46, stroke="#8c959f", rx=6)
        s.text(x + 23, 76, b, size=24, weight="bold")
        s.arrow([(x + 23, 96), (x + 23, 120)], color=colr)
        s.rect(x, 126, 46, 46, stroke=colr, fill=colr + "18", rx=6)
        s.text(x + 23, 158, c, size=24, weight="bold", color=colr)
    s.text(40 + 6 * 58 + 52, 200, "copy", size=14, color=COL["green"][0], weight="bold")
    s.text(40 + 3 * 58, 200, "flip", size=14, color=COL["red"][0], weight="bold")
    save(s, "twos-shortcut")

    # 4-bit 2's complement wheel
    s = Svg(460, 460, "4-bit two's complement wheel")
    cx, cy, R = 230, 235, 165
    s.add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#d0d7de" stroke-width="2"/>')
    for k in range(16):
        ang = -math.pi / 2 + 2 * math.pi * k / 16
        x, y = cx + R * math.cos(ang), cy + R * math.sin(ang)
        val = k if k < 8 else k - 16
        colr = COL["blue"][0] if val >= 0 else COL["red"][0]
        s.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="21" fill="#fff" stroke="{colr}" stroke-width="2"/>')
        s.text(x, y + 6, f"{val:+d}" if val else "0", size=15, weight="bold", color=colr)
        xi, yi = cx + (R - 46) * math.cos(ang), cy + (R - 46) * math.sin(ang)
        s.text(xi, yi + 5, format(k, "04b"), size=13, color=MUTED)
    # overflow boundary between 7 and -8 (bottom)
    ang = -math.pi / 2 + 2 * math.pi * 7.5 / 16
    s.line([(cx + (R - 70) * math.cos(ang), cy + (R - 70) * math.sin(ang)),
            (cx + (R + 30) * math.cos(ang), cy + (R + 30) * math.sin(ang))], COL["orange"][0], 4)
    s.text(cx, 448, "crossing the orange line = OVERFLOW", size=14, weight="bold", color=COL["orange"][0])
    s.text(cx, cy - 8, "add = go clockwise", size=14, color=MUTED)
    s.text(cx, cy + 14, "blue = positive, red = negative", size=12, color=MUTED)
    save(s, "wheel4")


def ladder(name, title, rows, head, up, result, note):
    """rows: (left text, digit). up=True → read remainders bottom-up."""
    n = len(rows)
    H = 70 + n * 44 + 70
    s = Svg(520, H, title)
    s.text(30, 30, head, size=16, anchor="start", weight="bold")
    col = COL["blue"][0] if up else COL["green"][0]
    for i, (lt, d) in enumerate(rows):
        y = 56 + i * 44
        s.text(30, y + 28, lt, size=18, anchor="start")
        s.rect(300, y + 4, 50, 34, stroke=col, fill=col + "18", rx=6)
        s.text(325, y + 29, d, size=20, weight="bold", color=col)
    y0, y1 = 64, 56 + (n - 1) * 44 + 34
    if up:
        s.arrow([(380, y1), (380, y0)], color=col, width=3)
        s.text(392, y0 + 12, "1st remainder = LSB", size=12, anchor="start", color=MUTED)
        s.text(392, y1 - 4, "last remainder = MSB", size=12, anchor="start", color=MUTED)
        s.text(392, y1 + 12, "(write this one first)", size=12, anchor="start", color=MUTED)
        s.text(392, (y0 + y1) / 2 + 5, "read UP", size=16, anchor="start", weight="bold", color=col)
    else:
        s.arrow([(380, y0), (380, y1)], color=col, width=3)
        s.text(392, y0 + 12, "1st bit after the point", size=12, anchor="start", color=MUTED)
        s.text(392, (y0 + y1) / 2 + 5, "read DOWN", size=16, anchor="start", weight="bold", color=col)
    s.text(30, H - 40, result, size=22, anchor="start", weight="bold")
    s.text(30, H - 14, note, size=13, anchor="start", color=MUTED)
    save(s, name)


def ladders():
    ladder("div-ladder", "41 to binary by dividing by 2",
           [("41 ÷ 2 = 20  rem", "1"), ("20 ÷ 2 = 10  rem", "0"), ("10 ÷ 2 = 5   rem", "0"),
            ("5 ÷ 2 = 2    rem", "1"), ("2 ÷ 2 = 1    rem", "0"), ("1 ÷ 2 = 0    rem", "1")],
           "Whole part: keep dividing by 2", True, "41 = 101001₂",
           "stop when you reach 0, then read the remainders bottom to top")
    ladder("mul-ladder", "0.6875 to binary by multiplying by 2",
           [("0.6875 × 2 = 1.375", "1"), ("0.375 × 2 = 0.75", "0"),
            ("0.75 × 2 = 1.5", "1"), ("0.5 × 2 = 1.0", "1")],
           "Fraction part: keep multiplying by 2", False, "0.6875 = 0.1011₂",
           "the box is the whole number you got; carry on with only the fraction; stop at 0")
    ladder("div16-ladder", "300 to hex by dividing by 16",
           [("300 ÷ 16 = 18  rem", "C"), ("18 ÷ 16 = 1    rem", "2"), ("1 ÷ 16 = 0     rem", "1")],
           "Same thing in hex: divide by 16", True, "300 = 12C₁₆",
           "remainder 12 is written C  (A=10 B=11 C=12 D=13 E=14 F=15)")


if __name__ == "__main__":
    kmaps(); gates(); circuits_two_level(); adders(); muxes(); decoders(); numbers(); ladders()
    print("ok", len(os.listdir(OUT)))
