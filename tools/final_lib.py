"""Helpers for the final-exam site: LaTeX conversion, tables, figures and
question builders. Every answer here is computed, not typed in."""
import os, re, math, html
from svglib import Svg, Gate, wire, label_in, label_out, kmap, INK, MUTED, COL
from final_engine import primes, mincover, tname, minterms, jk_design, ev
import build_svg_seq as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "docs", "final", "fig")
os.makedirs(FIG, exist_ok=True)
COLORS = ["red", "blue", "green", "orange", "purple"]
COLORS = [c for c in COLORS if c in COL]
SUB = "₀₁₂₃₄₅₆₇₈₉"


# ------------------------------------------------------------ text
def tex(s):
    s = re.sub(r"\b([JKDT])([A-C])\b", r"\1_{\2}", s)
    s = re.sub(r"([A-Za-z])([0-9]+)", r"\1_{\2}", s)
    s = re.sub(r"(?<=[A-Za-z)'}])\s*\^\s*(?=[A-Za-z(])", r" \\oplus ", s)
    s = s.replace("Σm", r"\Sigma m").replace("ΠM", r"\Pi M")
    return s


def M(s):
    return "$" + tex(s) + "$"


def DD(s):
    return "$$" + tex(s) + "$$"


def uni(s):
    """Plain-text label with unicode subscripts (for SVG)."""
    s = re.sub(r"\b([JKDT])([A-C])\b", lambda m: m.group(1) + {"A": "ᴀ", "B": "ʙ", "C": "ᴄ"}[m.group(2)], s)
    return re.sub(r"([A-Za-z])([0-9])", lambda m: m.group(1) + SUB[int(m.group(2))], s)


def img(name, alt="", ext=False):
    src = name if ext else f"fig/{name}.svg"
    return f'<div class="fig"><img src="{src}" alt="{html.escape(alt)}" loading="lazy"></div>'


def table(head, rows, cls="tt", hl=None):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = ""
    for i, r in enumerate(rows):
        c = ' class="hl"' if hl and i in hl else ""
        b += f"<tr{c}>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>"
    return f'<div class="tw"><table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def bits(m, n):
    return format(m, f"0{n}b")


def sigma(ms):
    return r"\Sigma m(" + ", ".join(map(str, ms)) + ")"


def pi(ms):
    return r"\Pi M(" + ", ".join(map(str, ms)) + ")"


# ------------------------------------------------------------ expression trees
def T_ev(t, env):
    if isinstance(t, str):
        return env[t]
    op, *a = t
    v = [T_ev(x, env) for x in a]
    if op == "NOT":
        return 1 - v[0]
    if op in ("AND", "NAND"):
        r = int(all(v))
    elif op in ("OR", "NOR"):
        r = int(any(v))
    elif op in ("XOR", "XNOR"):
        r = sum(v) % 2
    return 1 - r if op in ("NAND", "NOR", "XNOR") else r


def T_tex(t, top=True):
    if isinstance(t, str):
        return t
    op, *a = t
    if op == "NOT":
        x = a[0]
        return x + "'" if isinstance(x, str) else "(" + T_tex(x) + ")'"
    if op in ("AND", "NAND"):
        s = "".join(T_tex(x, False) if (isinstance(x, str) or x[0] in ("NOT", "NAND", "NOR", "AND")) else "(" + T_tex(x) + ")" for x in a)
    elif op in ("OR", "NOR"):
        s = " + ".join(T_tex(x) for x in a)
    else:
        s = " ^ ".join(T_tex(x, False) for x in a)
    if op in ("NAND", "NOR", "XNOR"):
        return "(" + s + ")'"
    return s if (top or op == "AND") else "(" + s + ")"


def T_ms(t, names):
    n = len(names)
    return [m for m in range(1 << n) if T_ev(t, {names[i]: (m >> (n - 1 - i)) & 1 for i in range(n)})]


def draw_tree(name, t, out="F", feedback=None, title="Logic circuit"):
    """Draw an expression tree as a gate circuit. Leaves are labelled inputs."""
    leaves = []
    info = {}

    def depth(n):
        if isinstance(n, str):
            return 0
        return 1 + max(depth(c) for c in n[1:])

    def place(n):
        if isinstance(n, str):
            y = 40 + len(leaves) * 46
            leaves.append((n, y))
            return y
        ys = [place(c) for c in n[1:]]
        return sum(ys) / len(ys)

    def ypos(n, memo={}):
        return None

    # first pass: y for every node
    ys = {}

    def assign(n):
        if isinstance(n, str):
            y = 40 + len(leaves) * 46
            leaves.append((n, y))
            ys[id(n) if not isinstance(n, str) else (len(leaves) - 1, n)] = y
            return y
        cy = [assign(c) for c in n[1:]]
        y = sum(cy) / len(cy)
        ys[id(n)] = y
        return y

    assign(t)
    D = depth(t)
    X0, DX = 70, 112
    H = 40 + len(leaves) * 46 + (56 if feedback else 14)
    W = X0 + D * DX + 110
    s = Svg(W, H, title)
    li = [0]

    def draw(n):
        """returns output point"""
        if isinstance(n, str):
            nm, y = leaves[li[0]]
            li[0] += 1
            s.text(X0 - 26, y + 5, uni(nm), size=16, anchor="end", weight="bold")
            return (X0 - 20, y)
        op = n[0]
        outs = [draw(c) for c in n[1:]]
        y = sum(p[1] for p in outs) / len(outs)
        x = X0 + (depth(n) - 1) * DX + 30
        if op == "NOT":
            g = Gate(s, "NOT", x, y - 13, 1, h=26)
        else:
            g = Gate(s, op, x, y - max(50, 22 * len(outs) + 10) / 2, len(outs))
        for k, (p, q) in enumerate(zip(outs, g.ins)):
            # stagger the vertical runs so wires do not overlap
            mid = q[0] - 14 - 9 * (abs(k - (len(outs) - 1) / 2))
            wire(s, p, q, midx=max(mid, p[0] + 6))
        return g.out

    o = draw(t)
    s.line([o, (o[0] + 34, o[1])])
    s.text(o[0] + 40, o[1] + 5, out, size=16, anchor="start", weight="bold")
    if feedback:
        yb = H - 30
        s.dot(o[0] + 18, o[1], color="#0b5cad")
        s.line([(o[0] + 18, o[1]), (o[0] + 18, yb), (X0 - 40, yb)], "#0b5cad", 2, dash="6 4")
        s.text(X0 - 40, yb + 20, f"{out} is fed back and comes in again as {feedback}", size=13, anchor="start", color="#0b5cad")
    s.save(os.path.join(FIG, name + ".svg"))
    return name


# ------------------------------------------------------------ K-map figures
def fig_kmap(name, names, ones, dc=(), cover=(), title=None, zeros_cover=False):
    nv = len(names)
    vals = {m: "0" for m in range(1 << nv)}
    for m in ones:
        vals[m] = "1"
    for m in dc:
        vals[m] = "X"
    groups = []
    for i, c in enumerate(cover):
        groups.append({"cells": sorted(c[2]), "color": COLORS[i % len(COLORS)], "label": c[3] if len(c) > 3 else tname(c[0], c[1], names, nv)})
    v = names if all(len(x) == 1 for x in names) else S.V([uni(x) for x in names])
    if isinstance(v, list):
        v = "".join(v)
    kmap(v, vals, groups, title=title).save(os.path.join(FIG, name + ".svg"))
    return name


def fig_kmaps(name, names, maps, per_row=3, cell=48):
    """maps: [(title, ones, dc, cover)] drawn in a grid."""
    nv = len(names)
    v = names if all(len(x) == 1 for x in names) else S.V([uni(x) for x in names])
    if isinstance(v, list):
        v = "".join(v)
    cw = 70 + (2 if nv == 3 else 4) * cell + 50
    rows = math.ceil(len(maps) / per_row)
    maxg = max(len(m[3]) for m in maps)
    ch = 94 + 4 * cell + 24 + 26 * maxg + 14
    s = Svg(cw * min(per_row, len(maps)) + 10, ch * rows, "K-maps")
    for i, (title, ones, dc, cover) in enumerate(maps):
        vals = {m: "0" for m in range(1 << nv)}
        for m in ones:
            vals[m] = "1"
        for m in dc:
            vals[m] = "X"
        groups = [{"cells": sorted(c[2]), "color": COLORS[k % len(COLORS)], "label": tname(c[0], c[1], names, nv)} for k, c in enumerate(cover)]
        kmap(v, vals, groups, s=s, x0=(i % per_row) * cw, y0=(i // per_row) * ch, title=title, cell=cell)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def cover_tex(cover, names):
    nv = len(names)
    if not cover:
        return "0"
    return " + ".join(tname(c[0], c[1], names, nv) for c in cover)


# ------------------------------------------------------------ two-level NAND / NOR figure
def fig_two_level(name, terms, out="F", kind="NAND"):
    """terms: list of lists of literal strings. Single-literal terms go straight
    into the last gate, complemented."""
    multi = [t for t in terms if len(t) > 1]
    single = [t[0] for t in terms if len(t) == 1]
    rows = sum(len(t) for t in multi) + len(single)
    H = 50 + rows * 34 + 20 * len(multi)
    s = Svg(470, max(H, 150), f"Two-level {kind}")
    y = 30
    outs = []
    for t in multi:
        h = max(50, 22 * len(t) + 10)
        g = Gate(s, kind, 150, y, len(t), h=h)
        for p, lit in zip(g.ins, t):
            s.line([(p[0] - 34, p[1]), p])
            s.text(p[0] - 40, p[1] + 5, uni(lit), size=15, anchor="end", weight="bold")
        outs.append(g.out)
        y += h + 24
    for lit in single:
        flip = lit[:-1] if lit.endswith("'") else lit + "'"
        outs.append((150, y + 14))
        s.text(110, y + 19, uni(flip), size=15, anchor="end", weight="bold")
        s.line([(116, y + 14), (150, y + 14)])
        y += 44
    cy = sum(p[1] for p in outs) / len(outs)
    h = max(50, 22 * len(outs) + 10)
    g2 = Gate(s, kind, 320, cy - h / 2, len(outs), h=h)
    for k, (p, q) in enumerate(zip(outs, g2.ins)):
        wire(s, p, q, midx=q[0] - 16 - 10 * abs(k - (len(outs) - 1) / 2))
    s.line([g2.out, (g2.out[0] + 34, g2.out[1])])
    s.text(g2.out[0] + 40, g2.out[1] + 5, out, size=16, anchor="start", weight="bold")
    s.save(os.path.join(FIG, name + ".svg"))
    return name


# ------------------------------------------------------------ counters
def fig_cycles(name, cycles, nb, title="State diagram"):
    n = len(cycles)
    W = 300 * n
    s = Svg(W, 280, title)
    for ci, cyc in enumerate(cycles):
        cx, cy, R = 150 + 300 * ci, 135, 88 if len(cyc) > 3 else 70
        P = []
        for i in range(len(cyc)):
            a = -math.pi / 2 + i * 2 * math.pi / len(cyc)
            P.append((cx + R * math.cos(a), cy + R * math.sin(a)))
        for i in range(len(cyc)):
            S.edge(s, P[i], P[(i + 1) % len(cyc)], "", bend=-12, r=27)
        for i, st in enumerate(cyc):
            S.node(s, P[i][0], P[i][1], bits(st, nb), None, r=27, color=[INK, "#0b5cad"][ci % 2])
        if n > 1:
            s.text(cx, 268, f"Mode {ci+1}", size=14, weight="bold", color=[INK, "#0b5cad"][ci % 2])
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def fig_ff_row(name, kind, labels, names, title="Logic diagram", note=None):
    """Row of flip-flops sharing one clock; inputs shown as labelled expressions."""
    n = len(names)
    lw = max(len(uni(x)) for pair in labels for x in pair) * 9 + 20
    step = 164 + lw
    W = 60 + n * step + 20
    s = Svg(W, 236 if note else 216, title)
    ins = {"JK": ("J", "K"), "D": ("D",), "T": ("T",)}[kind]
    ck = 176
    fs = []
    for i in range(n):
        x = 40 + lw + i * step
        f = S.ff(s, x, 30, kind)
        fs.append(f)
        for pin, lab in zip(ins, labels[i]):
            s.line([(f[pin][0] - 10, f[pin][1]), f[pin]])
            s.text(f[pin][0] - 16, f[pin][1] + 5, uni(lab), size=15, anchor="end", weight="bold")
        label_out(s, f["Q"], names[i], dx=4)
        s.text(f["Qn"][0] + 4, f["Qn"][1] + 5, names[i] + "'", size=13, anchor="start", color=MUTED)
    s.line([(16, ck), (fs[-1]["C"][0] - 8, ck)])
    s.text(16, ck + 20, "CLK", size=13, anchor="start")
    for f in fs:
        x = f["C"][0] - 8
        s.line([(x, ck), (x, f["C"][1]), f["C"]])
        s.dot(x, ck)
    if note:
        s.text(W / 2, 228, note, size=12, color=MUTED)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def jk_counter(cycles, names, nb=3):
    """Full JK design. Returns dict with table rows, equations, covers, unused-state trace."""
    nxt = {}
    for cyc in cycles:
        for i, st in enumerate(cyc):
            nxt[st] = cyc[(i + 1) % len(cyc)]
    unused = [m for m in range(1 << nb) if m not in nxt]
    d = jk_design(nxt, nb, names, unused)
    eq, cov = {}, {}
    for k, (on, dc) in d.items():
        c = mincover(nb, on, dc) if on else []
        cov[k] = c
        eq[k] = cover_tex(c, names) if on else "0"
        if on and set(on) | set(dc) == set(range(1 << nb)):
            eq[k] = "1"
            cov[k] = []
    rows = []
    for st in sorted(nxt):
        r = [" ".join(bits(st, nb)), " ".join(bits(nxt[st], nb))]
        for b in range(nb):
            q = (st >> (nb - 1 - b)) & 1
            qn = (nxt[st] >> (nb - 1 - b)) & 1
            r.append({(0, 0): "0 x", (0, 1): "1 x", (1, 0): "x 1", (1, 1): "x 0"}[(q, qn)])
        rows.append(r)

    def step(m):
        env = {names[i]: (m >> (nb - 1 - i)) & 1 for i in range(nb)}
        out = 0
        for b in range(nb):
            j = ev(eq["J" + names[b]], env)
            k = ev(eq["K" + names[b]], env)
            q = env[names[b]]
            out = (out << 1) | int((j and not q) or (not k and q))
        return out

    for st in nxt:  # self-check: equations reproduce the wanted sequence
        assert step(st) == nxt[st], (bits(st, nb), bits(step(st), nb))
    trace = []
    for u in unused:
        path, cur = [u], u
        while cur not in nxt and len(path) < 9:
            cur = step(cur)
            path.append(cur)
            if path.count(cur) > 1:
                break
        trace.append((path, cur in nxt))
    return dict(nxt=nxt, unused=unused, d=d, eq=eq, cov=cov, rows=rows, trace=trace, step=step)


# ------------------------------------------------------------ ripple counter
def ripple_sim(n, down, steps=None):
    """Simulate: returns per-half-step strings for CLK and each Q (rising-edge clock)."""
    steps = steps or (1 << n) + 1
    L = steps * 2
    clk = "".join("0" if i % 2 == 0 else "1" for i in range(L))
    rows = [clk]
    cnt = 0
    vals = []
    for i in range(L):
        if i > 0 and clk[i - 1] == "0" and clk[i] == "1":
            cnt = (cnt - 1) % (1 << n) if down else (cnt + 1) % (1 << n)
        vals.append(cnt)
    for b in range(n):
        rows.append("".join(str((v >> b) & 1) for v in vals))
    return rows, vals


def fig_ripple_wave(name, n, down, title="Waveforms"):
    rows, vals = ripple_sim(n, down)
    cols = [INK, "#0b5cad", "#1a7f37", "#bc4c00", "#c4262e"]
    data = [("CLK", rows[0])] + [("Q" + SUB[b], rows[b + 1], cols[b + 1]) for b in range(n)]
    step = 34
    W = 90 + len(rows[0]) * step / 2 + 70
    s = Svg(W, 60 + (n + 1) * 44 + 30, title)
    rise = [i for i in range(1, len(rows[0])) if rows[0][i - 1] == "0" and rows[0][i] == "1"]
    S.timing(s, 10, 34, data, step=step, label_w=70, edges=rise)
    seen = None
    for i, v in enumerate(vals):
        if i % 2 == 1:
            s.text(10 + 70 + i * step / 2 + step / 2, 22, bits(v, n), size=11, color=MUTED)
    for b in range(n + 1):
        s.text(W - 6, 34 + b * 44 + 17, "f" if b == 0 else f"f / {2**b}", size=12, anchor="end", color=MUTED)
    s.text(W / 2, 60 + (n + 1) * 44 + 18, "count (Q" + "".join(SUB[b] for b in reversed(range(n))) + ") written above each clock period · dashed = rising clock edge", size=12, color=MUTED)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def fig_ripple(name, n, kind, down, title="Ripple counter"):
    """Rising-edge flip-flops. Down: next clock = Q. Up: next clock = Q'."""
    step = 200
    s = Svg(110 + n * step, 250, title)
    prev = None
    src = "Q" if down else "Qn"
    for i in range(n):
        x = 110 + i * step
        f = S.ff(s, x, 60, kind, h=110)
        s.text(x + 42, 52, "Q" + SUB[i], size=15, weight="bold")
        if kind == "D":  # D = own Q'
            qn, dp = f["Qn"], f["D"]
            s.line([qn, (qn[0] + 8, qn[1]), (qn[0] + 8, 200), (dp[0] - 6, 200), (dp[0] - 6, dp[1]), dp], "#c4262e")
        elif kind == "T":
            s.text(f["T"][0] - 6, f["T"][1] + 5, "1", size=15, anchor="end", weight="bold")
        else:
            for p in ("J", "K"):
                s.text(f[p][0] - 6, f[p][1] + 5, "1", size=15, anchor="end", weight="bold")
        if prev is None:
            s.line([(30, f["C"][1]), f["C"]])
            s.text(30, f["C"][1] - 8, "CLK", size=13, anchor="start")
        else:
            p = prev[src]
            yb = 222 if src == "Qn" else 28
            if src == "Q":
                s.line([p, (p[0] + 16, p[1]), (p[0] + 16, 28), (f["C"][0] - 16, 28), (f["C"][0] - 16, f["C"][1]), f["C"]], "#0b5cad")
            else:
                s.dot(p[0] + 8, p[1], color="#0b5cad") if kind == "D" else None
                s.line([(p[0] + (8 if kind == "D" else 0), p[1]), (p[0] + 24, p[1]), (p[0] + 24, 222), (f["C"][0] - 16, 222), (f["C"][0] - 16, f["C"][1]), f["C"]], "#0b5cad")
        prev = f
    s.save(os.path.join(FIG, name + ".svg"))
    return name


# ------------------------------------------------------------ asynchronous
GRAY = [0, 1, 3, 2]


def async_table(Y, z, inputs, state="y"):
    """Y, z: plain expressions over inputs + state. One feedback loop.
    Returns rows[y] = [(Y, z) per column in Gray order]."""
    ni = len(inputs)
    cols = GRAY if ni == 2 else [0, 1]
    tab = []
    for y in (0, 1):
        row = []
        for c in cols:
            env = {inputs[i]: (c >> (ni - 1 - i)) & 1 for i in range(ni)}
            env[state] = y
            Yv = ev(Y, env)
            env["Y"] = Yv
            row.append((Yv, ev(z, env) if z else None))
        tab.append(row)
    return cols, tab


def fig_transition(name, cols, tab, inputs, state="y", title="Transition table"):
    ni = len(inputs)
    cw, ch, ox, oy = 84, 54, 120, 84
    s = Svg(ox + len(cols) * cw + 40, oy + 2 * ch + 60, title)
    s.text(ox + len(cols) * cw / 2, 28, "".join(inputs), size=17, weight="bold")
    s.text(ox - 60, oy + ch + 6, state, size=17, weight="bold")
    for i, c in enumerate(cols):
        s.text(ox + i * cw + cw / 2, oy - 12, bits(c, ni), size=15, color=MUTED)
    for y in (0, 1):
        s.text(ox - 22, oy + y * ch + ch / 2 + 6, str(y), size=15, color=MUTED)
        for i, c in enumerate(cols):
            x0, y0 = ox + i * cw, oy + y * ch
            s.rect(x0, y0, cw, ch, stroke="#8c959f", width=1.5)
            v = tab[y][i][0]
            if v == y:
                s.add(f'<circle cx="{x0+cw/2}" cy="{y0+ch/2}" r="18" fill="{COL["blue"][1]}" stroke="{COL["blue"][0]}" stroke-width="2.5"/>')
            s.text(x0 + cw / 2, y0 + ch / 2 + 7, str(v), size=20, weight="bold", color=COL["blue"][0] if v == y else INK)
    s.rect(ox, oy, len(cols) * cw, 2 * ch, width=2)
    bad = [i for i in range(len(cols)) if tab[0][i][0] != 0 and tab[1][i][0] != 1]
    for i in bad:
        s.rect(ox + i * cw + 3, oy + 3, cw - 6, 2 * ch - 6, stroke=COL["red"][0], width=3, rx=8, dash="7 5")
    s.text(ox + len(cols) * cw / 2, oy + 2 * ch + 26, "entry = Y · circle = stable (Y = y)", size=12, color=MUTED)
    if bad:
        s.text(ox + len(cols) * cw / 2, oy + 2 * ch + 46, "red dashed column = no stable state", size=12, color=COL["red"][0])
    s.save(os.path.join(FIG, name + ".svg"))
    return name, bad
