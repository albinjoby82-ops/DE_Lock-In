"""Helpers for the book-question builder: Boolean parser, truth tables,
gate-circuit drawer, timing diagrams, and question/HTML helpers.
Used by tools/build_book.py."""
import os, json
from svglib import Svg, Gate, wire, label_in, label_out, kmap, INK, MUTED, COL
from build_svg import route_fan_in

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_OUT = os.path.join(ROOT, "docs", "svg", "book")
os.makedirs(SVG_OUT, exist_ok=True)


# ============================================================ Boolean expressions
def parse(src):
    """Parse ' + juxtaposition ⊕ ⊙ ( ) [ ] 0 1 into a tree.
    ('var', name) ('const', v) ('not', t) ('and', [..]) ('or', [..]) ('xor', [a, b]) ('xnor', [a, b])"""
    s = src.replace(" ", "").replace("·", "").replace("[", "(").replace("]", ")").replace("’", "'")
    i = 0

    def peek():
        return s[i] if i < len(s) else None

    def sum_():
        nonlocal i
        kids = [xor_()]
        while peek() == "+":
            i += 1
            kids.append(xor_())
        return kids[0] if len(kids) == 1 else ("or", kids)

    def xor_():
        nonlocal i
        n = prod()
        while peek() in ("⊕", "⊙"):
            op = "xor" if peek() == "⊕" else "xnor"
            i += 1
            n = (op, [n, prod()])
        return n

    def prod():
        kids = [unary()]
        while peek() is not None and (peek() == "(" or peek().isalpha() or peek() in "01"):
            kids.append(unary())
        return kids[0] if len(kids) == 1 else ("and", kids)

    def unary():
        nonlocal i
        n = atom()
        while peek() == "'":
            i += 1
            n = ("not", n)
        return n

    def atom():
        nonlocal i
        c = peek()
        if c == "(":
            i += 1
            n = sum_()
            assert peek() == ")", f"unclosed bracket in {src!r}"
            i += 1
            return n
        if c in ("0", "1"):
            i += 1
            return ("const", int(c))
        assert c is not None and c.isalpha(), f"can't read {s[i:]!r} in {src!r}"
        i += 1
        return ("var", c)

    t = sum_()
    assert i == len(s), f"trailing {s[i:]!r} in {src!r}"
    return t


def ev(t, env):
    op = t[0]
    if op == "var":
        return env[t[1].lower()]
    if op == "const":
        return t[1]
    if op == "not":
        return 1 - ev(t[1], env)
    if op == "and":
        return int(all(ev(k, env) for k in t[1]))
    if op == "or":
        return int(any(ev(k, env) for k in t[1]))
    if op == "xor":
        return ev(t[1][0], env) ^ ev(t[1][1], env)
    if op == "xnor":
        return 1 - (ev(t[1][0], env) ^ ev(t[1][1], env))
    raise ValueError(op)


def tt(expr, vars_):
    """Truth table column (list of 0/1) in binary row order."""
    t = parse(expr) if isinstance(expr, str) else expr
    n = len(vars_)
    out = []
    for m in range(2 ** n):
        env = {v.lower(): (m >> (n - 1 - k)) & 1 for k, v in enumerate(vars_)}
        out.append(ev(t, env))
    return out


def ones(expr, vars_):
    return [m for m, v in enumerate(tt(expr, vars_)) if v]


def same(a, b, vars_):
    return tt(a, vars_) == tt(b, vars_)


def lits(expr):
    return sum(1 for c in expr if c.isalpha())


# ============================================================ circuits
# drawing tree: ("in", label) | ("g", KIND, [kids])
def to_draw(t, inverters=False):
    """Parse tree -> drawing tree. Complemented variables become input labels x'
    (or explicit NOT gates when inverters=True). NOT over AND/OR/XOR -> NAND/NOR/XNOR."""
    op = t[0]
    if op == "var":
        return ("in", t[1])
    if op == "const":
        return ("in", str(t[1]))
    if op == "not":
        k = t[1]
        if k[0] == "var":
            return ("g", "NOT", [("in", k[1])]) if inverters else ("in", k[1] + "'")
        if k[0] in ("and", "or"):
            return ("g", "NAND" if k[0] == "and" else "NOR", [to_draw(c, inverters) for c in flat(k)[1]])
        if k[0] == "xor":
            return ("g", "XNOR", [to_draw(c, inverters) for c in k[1]])
        return ("g", "NOT", [to_draw(k, inverters)])
    if op in ("and", "or"):
        return ("g", op.upper(), [to_draw(c, inverters) for c in flat(t)[1]])
    if op in ("xor", "xnor"):
        return ("g", op.upper(), [to_draw(c, inverters) for c in t[1]])
    raise ValueError(op)


def flat(t):
    if t[0] not in ("and", "or"):
        return t
    kids = []
    for k in t[1]:
        k = flat(k)
        if k[0] == t[0]:
            kids += k[1]
        else:
            kids.append(k)
    return (t[0], kids)


def G(kind, *kids, label=None):
    """Manual drawing-tree node. Strings become inputs. label = signal name shown at its output."""
    return ("g", kind, [("in", k) if isinstance(k, str) else k for k in kids], label)


def ev_draw(node, env):
    """Evaluate a drawing tree (to prove a drawn circuit is right)."""
    if node[0] == "in":
        lab = node[1]
        if lab in ("0", "1"):
            return int(lab)
        v = env[lab[0].lower()]
        return 1 - v if lab.endswith("'") else v
    vals = [ev_draw(k, env) for k in node[2]]
    kind = node[1]
    base = {"AND": all(vals), "NAND": all(vals), "OR": any(vals), "NOR": any(vals),
            "NOT": vals[0], "BUF": vals[0], "XOR": sum(vals) % 2 == 1, "XNOR": sum(vals) % 2 == 1}[kind]
    out = int(bool(base))
    return 1 - out if kind in ("NAND", "NOR", "NOT", "XNOR") else out


def draw_matches(node, expr, vars_):
    n = len(vars_)
    for m in range(2 ** n):
        env = {v.lower(): (m >> (n - 1 - k)) & 1 for k, v in enumerate(vars_)}
        if ev_draw(node, env) != ev(parse(expr), env):
            return False
    return True


ROW = 34
COLW = 128


def gh(node):
    kind, n = node[1], len(node[2])
    return 34 if kind in ("NOT", "BUF") else max(50, 22 * n + 10)


def size(node):
    if node[0] == "in":
        return ROW
    return max(sum(size(k) for k in node[2]) + 8 * (len(node[2]) - 1), gh(node) + 12)


def depth(node):
    if node[0] == "in":
        return 0
    return 1 + max(depth(k) for k in node[2])


def _place(s, node, ytop, x_in, ncol):
    """Draw node within band [ytop, ytop+size). Returns output point."""
    if node[0] == "in":
        y = ytop + ROW / 2
        label_in(s, (x_in, y), node[1])
        return (x_in, y)
    kids = node[2]
    total = sum(size(k) for k in kids) + 8 * (len(kids) - 1)
    band = size(node)
    y = ytop + (band - total) / 2
    outs = []
    for k in kids:
        outs.append(_place(s, k, y, x_in, ncol))
        y += size(k) + 8
    h = gh(node)
    cy = (outs[0][1] + outs[-1][1]) / 2
    top = min(max(cy - h / 2, ytop + 4), ytop + band - h - 4)
    col = depth(node)
    gx = x_in + 40 + (col - 1) * COLW + 50
    g = Gate(s, node[1], gx, top, len(kids), h=h)
    xlo = max(o[0] for o in outs) + 6
    xhi = min(p[0] for p in g.ins) - 8
    if len(kids) == 1:
        wire(s, outs[0], g.ins[0], midx=(xlo + xhi) / 2)
    else:
        route_fan_in(s, outs, g.ins, xlo, xhi)
    if len(node) > 3 and node[3]:
        s.text(g.out[0] + 6, g.out[1] - 8, node[3], size=13, anchor="start", color=COL["blue"][0], weight="bold")
    return g.out


def circuit_into(s, tree, y0, out_name, x_in=56, title=None, note=None):
    """Draw one circuit at y0 on Svg s. Returns the y below it."""
    y = y0
    if title:
        s.text(16, y + 18, title, size=15, anchor="start", weight="bold")
        y += 30
    if tree is None:
        s.text(30, y + 20, note or "", size=15, anchor="start")
        return y + 40
    ncol = depth(tree)
    out = _place(s, tree, y, x_in, ncol)
    xend = x_in + 40 + ncol * COLW + 40 if tree[0] == "g" else x_in + 120
    s.line([out, (max(xend, out[0] + 24), out[1])])
    label_out(s, (max(xend, out[0] + 24), out[1]), out_name)
    y += size(tree)
    if note:
        s.text(16, y + 16, note, size=13, anchor="start", color=MUTED)
        y += 26
    return y + 8


def width_of(tree, out_name, x_in=56):
    if tree is None:
        return 420
    ncol = depth(tree)
    return int(x_in + 40 + ncol * COLW + 60 + 11 * len(out_name) + 24)


def save_circuits(name, sections, alt=""):
    """sections: list of dicts {title, tree (drawing tree or expr str or None), out, note, inverters}."""
    prepared = []
    for sec in sections:
        tr = sec.get("tree")
        if isinstance(tr, str):
            tr = to_draw(parse(tr), sec.get("inverters", False))
        prepared.append((sec, tr))
    W = max(max(width_of(tr, sec.get("out", "F")) for sec, tr in prepared), 360)
    W = max(W, max(9 * len(sec.get("title") or "") + 40 for sec, _ in prepared))
    s = Svg(W, 10, alt or name)
    y = 8
    for k, (sec, tr) in enumerate(prepared):
        if k:
            s.line([(16, y), (W - 16, y)], "#d0d7de", 1, dash="4 4")
            y += 10
        y = circuit_into(s, tr, y, sec.get("out", "F"), title=sec.get("title"), note=sec.get("note"))
    s.h = int(y + 8)
    s.save(os.path.join(SVG_OUT, name + ".svg"))
    return name


def gate_count(tree):
    if tree is None or tree[0] == "in":
        return 0, 0
    g, i = 1, len(tree[2])
    for k in tree[2]:
        a, b = gate_count(k)
        g += a
        i += b
    return g, i


# ============================================================ timing diagrams
def save_timing(name, signals, title, period=56):
    """signals: list of (name, [bits], colour or None)."""
    n = len(signals[0][1])
    lm = 90
    W = lm + n * period + 30
    H = 50 + len(signals) * 52 + 10
    s = Svg(W, H, title)
    s.text(W / 2, 22, title, size=15, weight="bold")
    for k in range(n + 1):
        x = lm + k * period
        s.line([(x, 34), (x, H - 10)], "#d0d7de", 1, dash="3 4")
    for r, (nm, bits, col) in enumerate(signals):
        base = 50 + r * 52 + 34
        hi = base - 26
        c = COL[col][0] if col else INK
        s.text(lm - 14, base - 8, nm, size=15, anchor="end", weight="bold", color=c)
        pts = []
        for k, b in enumerate(bits):
            y = hi if b else base
            x0, x1 = lm + k * period, lm + (k + 1) * period
            if pts and pts[-1][1] != y:
                pts.append((x0, y))
            elif not pts:
                pts.append((x0, y))
            pts.append((x1, y))
        s.line(pts, c, 2.5)
        for k, b in enumerate(bits):
            s.text(lm + k * period + period / 2, base + 14, str(b), size=11, color=MUTED)
    s.save(os.path.join(SVG_OUT, name + ".svg"))
    return name


def save_kmap(name, vars_, ones_, groups, caption):
    v = {m: ("1" if m in ones_ else "0") for m in range(2 ** len(vars_))}
    kmap(vars_, v, groups, caption=caption).save(os.path.join(SVG_OUT, name + ".svg"))
    return name


# ============================================================ HTML helpers
def img(name, alt=""):
    return f"<img src='svg/book/{name}.svg' alt='{alt}'>"


def hl(x):
    return f"<mark>{x}</mark>"


def steps(rows, final=True):
    """rows: list of (expression_html, reason). Last row is bold if final."""
    h = "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr>"
    for k, (e, why) in enumerate(rows):
        e2 = f"<b>{e}</b>" if (final and k == len(rows) - 1) else e
        h += f"<tr><td>{k + 1}</td><td>{e2}</td><td>{why}</td></tr>"
    return h + "</table>"


def ttable(vars_, cols, highlight=None):
    """cols: dict name -> list. Small static truth table."""
    n = len(vars_)
    h = "<table class='tts'><tr>" + "".join(f"<th>{v}</th>" for v in vars_) + "".join(f"<th class='o'>{c}</th>" for c in cols) + "</tr>"
    for m in range(2 ** n):
        h += "<tr>" + "".join(f"<td>{(m >> (n - 1 - b)) & 1}</td>" for b in range(n))
        h += "".join(f"<td class='o'>{cols[c][m]}</td>" for c in cols) + "</tr>"
    return h + "</table>"


def lst(ms):
    return ", ".join(str(m) for m in ms)


def set_answers(ms):
    """Accepted spellings for a minterm/maxterm list."""
    core = ",".join(str(m) for m in ms)
    return [core, "(" + core + ")", "Σ(" + core + ")", "Σm(" + core + ")", "m(" + core + ")",
            "Π(" + core + ")", "ΠM(" + core + ")", "M(" + core + ")"]


# ============================================================ question builders
def bool_q(tag, q, vars_, fn, show, why, lits_=None, form=None, ref=None):
    assert same(fn, show, vars_), f"{tag}: {show} != {fn}"
    if lits_ is not None:
        assert lits(show) <= lits_, f"{tag}: show has {lits(show)} > {lits_}"
    d = {"tag": tag, "type": "bool", "q": q, "vars": vars_, "ones": ones(fn, vars_), "show": show, "why": why}
    if lits_:
        d["lits"] = lits_
    if form:
        d["form"] = form
    if ref:
        d["ref"] = ref
    return d


def tt_q(tag, q, vars_, outs, why, ref=None):
    d = {"tag": tag, "type": "tt", "q": q, "vars": vars_,
         "outs": {k: (v if isinstance(v, list) else tt(v, vars_)) for k, v in outs.items()}, "why": why}
    if ref:
        d["ref"] = ref
    return d


def multi_q(tag, q, fields, why, ref=None):
    d = {"tag": tag, "type": "multi", "q": q, "fields": [{"label": l, "ans": a} for l, a in fields], "why": why}
    if ref:
        d["ref"] = ref
    return d


def work_q(tag, q, why, svg=None, ref=None):
    d = {"tag": tag, "type": "work", "q": q, "why": why}
    if svg:
        d["svg"] = "book/" + svg
    if ref:
        d["ref"] = ref
    return d


def write_topic(tid, title, intro, problems):
    path = os.path.join(ROOT, "docs", "book", tid + ".js")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = {"id": tid, "title": title, "intro": intro, "problems": problems}
    with open(path, "w", encoding="utf8") as f:
        f.write("BOOK.add(" + json.dumps(data, ensure_ascii=False, indent=0) + ");\n")
    return sum(len(p["qs"]) for p in problems)
