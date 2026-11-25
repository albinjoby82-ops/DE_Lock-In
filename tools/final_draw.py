"""Circuit drawings for design answers: AND-OR gate networks, multiplexer and
decoder blocks, and flip-flop circuits with the gates drawn on every input.

Convention (the same one the lecture slides use): a wire is labelled with the
name of the signal it carries, and wires with the same name are joined."""
import os, re
from svglib import Svg, Gate, wire, block, INK, MUTED
from final_lib import uni, FIG, SUB
import build_svg_seq as S

LIT = re.compile(r"[A-Za-z][0-9]*'?")
STUB, GW, GAP = 24, 56, 42  # input stub, gate width, space between the AND column and the OR gate


def sop_terms(expr):
    """"AB' + C" → [["A", "B'"], ["C"]]. "0" / "1" → that string. None if it is not a plain sum of products."""
    e = expr.replace(" ", "")
    if e in ("0", "1"):
        return e
    if re.search(r"[()^]", e):
        return None
    out = []
    for t in e.split("+"):
        l = LIT.findall(t)
        if not l or "".join(l) != t:
            return None
        out.append(l)
    return out


def _terms(expr):
    t = sop_terms(expr)
    return [[expr]] if t is None else t  # anything else is drawn as one labelled wire


def _lw(terms):
    return max(len(uni(l)) for t in terms for l in t) * 10 + 8


def _andh(n):
    return 20 * n + 14


def net_dims(terms):
    """(width, up, down) of the network that net() draws, measured from its output point."""
    if isinstance(terms, str):
        return 16 + STUB, 16, 16
    lw = _lw(terms)
    if len(terms) == 1:
        t = terms[0]
        if len(t) == 1:
            return lw + STUB, 16, 16
        return lw + STUB + GW, _andh(len(t)) / 2, _andh(len(t)) / 2
    hs = [(_andh(len(t)) if len(t) > 1 else 30) for t in terms]
    half = max(sum(hs) + 12 * (len(hs) - 1), max(50, 22 * len(terms) + 10)) / 2
    return lw + STUB + GW + GAP + GW, half, half


def net(s, xr, y, terms):
    """Draw the gates for a sum of products so that the output is at (xr, y).
    One AND gate per product term, one OR gate to collect them."""

    def lab(x, yy, t):
        s.text(x - 6, yy + 6, uni(t), size=17, anchor="end", weight="bold")

    if isinstance(terms, str) or (len(terms) == 1 and len(terms[0]) == 1):
        t = terms if isinstance(terms, str) else terms[0][0]
        s.line([(xr - STUB, y), (xr, y)])
        lab(xr - STUB, y, t)
        return
    if len(terms) == 1:
        t = terms[0]
        h = _andh(len(t))
        g = Gate(s, "AND", xr - GW, y - h / 2, len(t), h=h)
        for p, l in zip(g.ins, t):
            s.line([(p[0] - STUB, p[1]), p])
            lab(p[0] - STUB, p[1], l)
        return
    m = len(terms)
    hor = max(50, 22 * m + 10)
    go = Gate(s, "OR", xr - GW, y - hor / 2, m, h=hor)
    xa = xr - GW - GAP - GW
    hs = [(_andh(len(t)) if len(t) > 1 else 30) for t in terms]
    yy = y - (sum(hs) + 12 * (m - 1)) / 2
    for k, (t, h) in enumerate(zip(terms, hs)):
        cy = yy + h / 2
        if len(t) > 1:
            g = Gate(s, "AND", xa, yy, len(t), h=h)
            for p, l in zip(g.ins, t):
                s.line([(p[0] - STUB, p[1]), p])
                lab(p[0] - STUB, p[1], l)
            o = g.out
        else:
            s.line([(xa - STUB, cy), (xa + GW, cy)])
            lab(xa - STUB, cy, t[0])
            o = (xa + GW, cy)
        # outer wires turn nearer the OR gate, so no wire crosses another
        wire(s, o, go.ins[k], midx=xa + GW + 8 + 9 * abs(k - (m - 1) / 2))
        yy += h + 12


def fig_sop(name, expr, out="F", title="Logic diagram", note=None):
    """AND-OR circuit for one sum-of-products expression."""
    terms = sop_terms(expr)
    assert terms is not None, expr
    w, up, dn = net_dims(terms)
    W = max(24 + w + 70, 250)
    H = up + dn + 44 + (22 if note else 0)
    s = Svg(W, H, title)
    xr, y = 24 + w, 22 + up
    net(s, xr, y, terms)
    s.line([(xr, y), (xr + 30, y)])
    s.text(xr + 36, y + 5, uni(out), size=16, anchor="start", weight="bold")
    if note:
        s.text(W / 2, H - 8, note, size=13, color=MUTED)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def fig_sops(name, eqs, title="Logic diagram", note=None):
    """Several outputs, one AND-OR circuit under the other. eqs: [(output name, expression)]."""
    T = [(k, sop_terms(e)) for k, e in eqs]
    assert all(t is not None for _, t in T), eqs
    D = [net_dims(t) for _, t in T]
    xr = 24 + max(d[0] for d in D)
    W = max(xr + 70, 250)
    H = sum(d[1] + d[2] for d in D) + 22 * (len(D) - 1) + 44 + (22 if note else 0)
    s = Svg(W, H, title)
    y = 22
    for (k, t), d in zip(T, D):
        y += d[1]
        net(s, xr, y, t)
        s.line([(xr, y), (xr + 30, y)])
        s.text(xr + 36, y + 5, uni(k), size=16, anchor="start", weight="bold")
        y += d[2] + 22
    if note:
        s.text(W / 2, H - 8, note, size=13, color=MUTED)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def _sub(i):
    return "".join(SUB[int(c)] for c in str(i))


def fig_mux(name, sels, data, out="F", title=None):
    """Multiplexer block. sels: select names, most significant first. data: what each data input is wired to."""
    n = len(data)
    h = 40 + n * 30
    lw = max(len(uni(d)) for d in data) * 9 + 16
    x, y, w = 30 + lw, 20, 120
    s = Svg(x + w + 90, y + h + 62, title or f"{n}-to-1 multiplexer")
    k = len(sels)
    pins = block(s, x, y, w, h, f"{n}-to-1 MUX", left=[f"I{_sub(i)}" for i in range(n)], right=["out"],
                 bottom=[f"S{_sub(k - 1 - i)}" for i in range(k)])
    for i, d in enumerate(data):
        p = pins[f"I{_sub(i)}"]
        s.text(p[0] - 6, p[1] + 5, uni(d), size=15, anchor="end", weight="bold")
    for i, nm in enumerate(sels):
        p = pins[f"S{_sub(k - 1 - i)}"]
        s.text(p[0], p[1] + 17, uni(nm), size=15, weight="bold")
    p = pins["out"]
    s.text(p[0] + 6, p[1] + 5, uni(out), size=16, anchor="start", weight="bold")
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def fig_muxes(name, sels, cols, title="Multiplexers"):
    """Two or more muxes side by side sharing the same selects. cols: [(output name, data list)]."""
    n = len(cols[0][1])
    h = 40 + n * 30
    k = len(sels)
    lw = max(len(uni(d)) for _, dd in cols for d in dd) * 9 + 16
    step = lw + 120 + 100
    s = Svg(30 + step * len(cols), 20 + h + 62, title)
    for c, (out, data) in enumerate(cols):
        x, y, w = 30 + lw + c * step, 20, 120
        pins = block(s, x, y, w, h, f"{n}-to-1 MUX", left=[f"I{_sub(i)}" for i in range(n)], right=["out"],
                     bottom=[f"S{_sub(k - 1 - i)}" for i in range(k)])
        for i, d in enumerate(data):
            p = pins[f"I{_sub(i)}"]
            s.text(p[0] - 6, p[1] + 5, uni(d), size=15, anchor="end", weight="bold")
        for i, nm in enumerate(sels):
            p = pins[f"S{_sub(k - 1 - i)}"]
            s.text(p[0], p[1] + 17, uni(nm), size=15, weight="bold")
        p = pins["out"]
        s.text(p[0] + 6, p[1] + 5, uni(out), size=16, anchor="start", weight="bold")
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def fig_decoder(name, names, outs, title=None):
    """n-to-2ⁿ decoder with one OR gate per output. outs: {output name: minterm list}."""
    n = len(names)
    N = 1 << n
    h = 40 + N * 26
    x, y, w = 50, 20, 150
    hs = [max(50, 22 * len(ms) + 10) for ms in outs.values()]
    H = max(y + h, y + sum(hs) + 26 * (len(hs) - 1)) + 30
    xg = x + w + 24 + 150
    s = Svg(xg + GW + 80, H, title or f"{n}-to-{N} decoder")
    pins = block(s, x, y, w, h, f"{n}-to-{N} decoder", left=list(names), right=[str(i) for i in range(N)])
    for i in range(N):
        p = pins[str(i)]
        s.text(p[0] + 5, p[1] + 5, "m" + _sub(i), size=14, anchor="start", color=MUTED)
    yy = y + max(0, (h - (sum(hs) + 26 * (len(hs) - 1))) / 2)
    for (k, ms), gh in zip(outs.items(), hs):
        g = Gate(s, "OR", xg, yy, len(ms), h=gh)
        for p, m in zip(g.ins, ms):
            s.line([(p[0] - 26, p[1]), p])
            s.text(p[0] - 32, p[1] + 5, "m" + _sub(m), size=15, anchor="end", weight="bold")
        s.line([g.out, (g.out[0] + 26, g.out[1])])
        s.text(g.out[0] + 32, g.out[1] + 5, uni(k), size=16, anchor="start", weight="bold")
        yy += gh + 26
    s.text((xg + GW + 80) / 2, H - 8, "same name = same wire: each OR input is joined to that decoder output", size=12, color=MUTED)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def fig_seq(name, kind, ffs, extra=(), note=None, title="Logic diagram"):
    """Flip-flops with the gates drawn on every input.
    ffs: [(state name, {pin: expression})], top to bottom. extra: [(output name, expression)]."""
    pins = {"JK": ("J", "K"), "D": ("D",), "T": ("T",)}[kind]
    CH = 74  # clear channel between the gates and the flip-flop pins (the CLK stub sits here)
    rows, wmax = [], 0
    for nm, eq in ffs:
        T = {p: _terms(eq[p]) for p in pins}
        Dm = {p: net_dims(T[p]) for p in pins}
        wmax = max([wmax] + [d[0] for d in Dm.values()])
        rows.append((nm, T, Dm))
    ex = [(nm, _terms(e)) for nm, e in extra]
    exd = [net_dims(t) for _, t in ex]
    wmax = max([wmax] + [d[0] for d in exd])
    xj = 20 + wmax
    xf = xj + CH + 22
    W = max(xf + 84 + 22 + 56, 6.9 * len(note or "") + 24)
    # heights
    lay, y = [], 20
    for nm, T, Dm in rows:
        if kind == "JK":
            upJ, dnJ, upK, dnK = Dm["J"][1], Dm["J"][2], Dm["K"][1], Dm["K"][2]
            dy = max(56, dnJ + 14 + upK)
            yJ = y + max(upJ, 22)
            lay.append((nm, T, {"J": yJ, "K": yJ + dy}, yJ - 22, dy + 44))
            y = yJ + dy + max(dnK, 22) + 22
        else:
            p = pins[0]
            up, dn = Dm[p][1], Dm[p][2]
            y1 = y + max(up, 22)
            lay.append((nm, T, {p: y1}, y1 - 22, 96))
            y = y1 + max(dn, 74) + 22
    exy = []
    for d in exd:
        exy.append(y + d[1])
        y += d[1] + d[2] + 18
    H = y + (26 if note else 6)
    s = Svg(W, H, title)
    for nm, T, ys, fy, fh in lay:
        f = S.ff(s, xf, fy, kind, h=fh)
        for p in pins:
            assert abs(f[p][1] - ys[p]) < 0.01
            net(s, xj, ys[p], T[p])
            s.line([(xj, ys[p]), f[p]])
        s.line([(f["C"][0] - 18, f["C"][1]), f["C"]])
        s.text(f["C"][0] - 24, f["C"][1] + 4, "CLK", size=12, anchor="end", color=MUTED)
        s.text(f["Q"][0] + 5, f["Q"][1] + 6, uni(nm), size=17, anchor="start", weight="bold")
        s.text(f["Qn"][0] + 5, f["Qn"][1] + 5, uni(nm) + "'", size=15, anchor="start", color=MUTED)
    for (nm, t), yy in zip(ex, exy):
        net(s, xj, yy, t)
        s.line([(xj, yy), (xj + 40, yy)])
        s.text(xj + 46, yy + 6, uni(nm), size=17, anchor="start", weight="bold")
    if note:
        s.text(W / 2, H - 8, note, size=13, color=MUTED)
    s.save(os.path.join(FIG, name + ".svg"))
    return name
