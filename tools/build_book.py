"""Build the Book questions section: Mano & Ciletti, Digital Design 4th ed.
Writes docs/book/NN.js and the diagrams in docs/svg/book/.
Every model answer is checked here against the original expression.
Run: python3 tools/build_book.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from booklib import *

S = "★"  # answer in the back of the book


def tag(n, part=None, star=False):
    return f"Mano {n}" + (f" ({part})" if part else "") + (f" {S}" if star else "")


def draw_card(name, title_orig, orig, simp, vars_, out="F", inv=False):
    """Original + simplified circuit in one SVG, both checked against each other."""
    to = to_draw(parse(orig), inv)
    ts = None if simp in ("0", "1") else to_draw(parse(simp), inv)
    assert draw_matches(to, orig, vars_) and same(orig, simp, vars_), name
    go, gi = gate_count(to)
    gs, gsi = gate_count(ts)
    secs = [{"title": f"Original: {title_orig}", "tree": to, "out": out,
             "note": f"{go} gates, {gi} gate inputs"}]
    if ts is None:
        secs.append({"title": f"Simplified: {out} = {simp}", "tree": None,
                     "note": f"No gates at all: tie {out} to {'0 V (ground)' if simp == '0' else '+V'}."})
    else:
        secs.append({"title": f"Simplified: {out} = {simp}", "tree": ts, "out": out,
                     "note": (f"{gs} gate{'s' if gs != 1 else ''}, {gsi} gate inputs" if gs else "Just a wire: no gates")})
    save_circuits(name, secs, f"{orig} before and after")
    return go, gs


# ======================================================================== TOPIC 06
def topic06():
    P = []

    # ---------------------------------------------------------------- 1.35 / 1.36
    save_circuits("p1-35", [{"title": "f = 3-input NAND", "tree": G("NAND", "a", "b", "c"), "out": "f"},
                            {"title": "g = 3-input NOR", "tree": G("NOR", "a", "b", "c"), "out": "g"}], "Fig P1.35")
    bits = lambda k, n: [(m >> (n - 1 - k)) & 1 for m in range(2 ** n)]
    save_timing("t1-35", [("a", bits(0, 3), None), ("b", bits(1, 3), None), ("c", bits(2, 3), None),
                          ("f", tt("(abc)'", "abc"), "blue"), ("g", tt("(a+b+c)'", "abc"), "red")],
                "Timing diagram: f = (abc)', g = (a + b + c)'")
    q = tt_q(tag("1.35"), "Fig P1.35: <b>f</b> is a 3-input NAND of a, b, c and <b>g</b> is a 3-input NOR of a, b, c. "
             "A timing diagram is just the truth table turned sideways. Fill f and g for all eight combinations.",
             "abc", {"f": "(abc)'", "g": "(a+b+c)'"},
             img("t1-35", "timing diagram") +
             "<p>NAND is <b>0 only when every input is 1</b> (the last slot, abc = 111).</p>"
             "<p>NOR is <b>1 only when every input is 0</b> (the first slot, abc = 000).</p>"
             "<p>Draw a, b, c as a binary count (c changes fastest), then read f and g straight off the table.</p>",
             ref="06 §1")
    q["svg"] = "book/p1-35"
    P.append({"n": "1.35", "text": "Timing diagram for f (NAND) and g (NOR) of a, b, c over all 8 combinations.", "qs": [q]})

    save_circuits("p1-36", [{"title": "f = XOR", "tree": G("XOR", "a", "b"), "out": "f"},
                            {"title": "g = XNOR", "tree": G("XNOR", "a", "b"), "out": "g"}], "Fig P1.36")
    save_timing("t1-36", [("a", bits(0, 2), None), ("b", bits(1, 2), None),
                          ("f", tt("a⊕b", "ab"), "blue"), ("g", tt("a⊙b", "ab"), "red")],
                "Timing diagram: f = a ⊕ b, g = (a ⊕ b)'", period=80)
    q = tt_q(tag("1.36"), "Fig P1.36: <b>f</b> = XOR of a, b and <b>g</b> = XNOR of a, b. Fill f and g for all four combinations.",
             "ab", {"f": "a⊕b", "g": "a⊙b"},
             img("t1-36", "timing diagram") +
             "<p>XOR = 1 when the inputs <b>differ</b> (01, 10). XNOR is its opposite: 1 when they are <b>the same</b> (00, 11).</p>"
             "<p>So g is always the flip of f: f = 0 1 1 0, g = 1 0 0 1.</p>", ref="06 §1")
    q["svg"] = "book/p1-36"
    P.append({"n": "1.36", "text": "Timing diagram for f (XOR) and g (XNOR) of a, b.", "qs": [q]})

    # ---------------------------------------------------------------- 2.1
    qs = []
    q = tt_q(tag("2.1", "a"), "Prove De Morgan for three variables with a truth table: <code>(x + y + z)' = x'y'z'</code> and "
             "<code>(xyz)' = x' + y' + z'</code>. Fill all four columns.", "xyz",
             {"(x+y+z)'": "(x+y+z)'", "x'y'z'": "x'y'z'", "(xyz)'": "(xyz)'", "x'+y'+z'": "x'+y'+z'"},
             "<p>Columns 1 and 2 match on every row (1 only on 000). Columns 3 and 4 match on every row (0 only on 111). "
             "Same output on all 8 rows = <b>the identities hold</b>.</p>"
             "<p>Quick way to fill them: an OR is 0 only on 000, so its NOT is 1 only on 000. An AND is 1 only on 111, so its NOT is 0 only on 111.</p>",
             ref="06 §3")
    qs.append(q)
    for part, lhs, rhs, name in [("b", "x + yz", "(x + y)(x + z)", "distributive law (OR over AND)"),
                                 ("c", "x(y + z)", "xy + xz", "distributive law (AND over OR)"),
                                 ("d", "x + (y + z)", "(x + y) + z", "associative law for OR"),
                                 ("e", "x(yz)", "(xy)z", "associative law for AND")]:
        L, R = tt(lhs, "xyz"), tt(rhs, "xyz")
        assert L == R
        extra = ""
        if part == "b":
            extra = "<p>When x = 1 both sides are 1. When x = 0 both sides become yz. That is why this odd-looking law works.</p>"
        qs.append(tt_q(tag("2.1", part), f"Prove the {name} with a truth table: <code>{lhs} = {rhs}</code>. Fill both columns.",
                       "xyz", {lhs: L, rhs: R},
                       f"<p>Both columns are <b>{' '.join(map(str, L))}</b>: identical on all 8 rows, so the law holds.</p>" + extra,
                       ref="06 §3"))
    P.append({"n": "2.1", "text": "Prove each identity with a truth table.", "qs": qs})

    # ---------------------------------------------------------------- 2.2
    T22 = [
        ("a", True, "xy + xy'", "x", 1, [
            (f"x{hl('(y + y′)')}".replace("′", "'"), "factor out x"),
            ("x·1", "y + y' = 1"),
            ("x", "x·1 = x")]),
        ("b", True, "(x + y)(x + y')", "x", 1, [
            (f"x + {hl('yy′')}".replace("′", "'"), "distributive backwards: (x + y)(x + z) = x + yz"),
            ("x + 0", "yy' = 0"),
            ("x", "x + 0 = x")]),
        ("c", True, "xyz + x'y + xyz'", "y", 1, [
            (f"{hl('xy(z + z′)')} + x'y".replace("′", "'"), "terms 1 and 3 share xy: factor it"),
            ("xy + x'y", "z + z' = 1"),
            (f"y{hl('(x + x′)')}".replace("′", "'"), "factor out y"),
            ("y", "x + x' = 1")]),
        ("d", True, "(A + B)'(A' + B')'", "0", None, [
            (f"{hl('A′B′')} · {hl('AB')}".replace("′", "'"), "De Morgan on each bracket: (A + B)' = A'B', (A' + B')' = AB"),
            ("(AA')(BB')", "reorder the AND"),
            ("0", "AA' = 0, and 0 times anything is 0")]),
        ("e", False, "xyz' + x'yz + xyz + x'yz'", "y", 1, [
            (f"{hl('xy(z′ + z)')} + {hl('x′y(z + z′)')}".replace("′", "'"), "pair terms 1+3 and 2+4"),
            ("xy + x'y", "z + z' = 1"),
            ("y(x + x')", "factor out y"),
            ("y", "x + x' = 1")]),
    ]
    qs = []
    for part, star, fn, ans, L, rows in T22:
        vars_ = "AB" if part == "d" else "xyz"
        if part in ("a", "b"):
            vars_ = "xy"
        qs.append(bool_q(tag("2.2", part, star), f"Simplify to a minimum number of literals: <code>{fn}</code>",
                         vars_, fn, ans, steps(rows), lits_=L, ref="06 §3"))
    fn = "(x + y + z')(x' + y' + z)"
    save_kmap("k2-2f", "xyz", ones(fn, "xyz"), [
        {"cells": [0, 2], "color": "red", "label": "x'z'"},
        {"cells": [3, 7], "color": "blue", "label": "yz"},
        {"cells": [4, 5], "color": "green", "label": "xy'"}], "F = x'z' + yz + xy'")
    qs.append(bool_q(tag("2.2", "f"), f"Simplify to a minimum number of literals: <code>{fn}</code>",
                     "xyz", fn, "x'z' + yz + xy'",
                     steps([
                         ("(x + y + z') = 0 only on xyz = 001", "a sum is 0 only when every letter in it is 0"),
                         ("(x' + y' + z) = 0 only on xyz = 110", "same idea"),
                         ("F = ΠM(1, 6) = Σm(0, 2, 3, 4, 5, 7)", "F is 0 on rows 1 and 6 only"),
                         ("x'z' + yz + xy'", "three pairs on the K-map (below)")]) + img("k2-2f") +
                     "<p><b>Both</b> the original and this SOP have <b>6 literals</b>, and nothing smaller exists "
                     "(each 1 can only join one neighbour). So the given expression was already minimal. Either answer is fine.</p>",
                     lits_=6, ref="06 §3"))
    P.append({"n": "2.2", "text": "Simplify to a minimum number of literals.", "qs": qs})

    # ---------------------------------------------------------------- 2.3
    T23 = [
        ("a", True, "ABC + A'B + ABC'", "B", 1, "ABC", [
            (f"{hl('AB(C + C′)')} + A'B".replace("′", "'"), "terms 1 and 3 share AB"),
            ("AB + A'B", "C + C' = 1"),
            ("B(A + A')", "factor out B"),
            ("B", "A + A' = 1")]),
        ("b", True, "x'yz + xz", "z(x + y)", 3, "xyz", [
            (f"z{hl('(x′y + x)')}".replace("′", "'"), "factor out z"),
            ("z(x + y)", "x + x'y = x + y")]),
        ("c", True, "(x + y)'(x' + y')", "x'y'", 2, "xy", [
            (f"{hl('x′y′')}(x' + y')".replace("′", "'"), "De Morgan: (x + y)' = x'y'"),
            ("x'y'x' + x'y'y'", "multiply out"),
            ("x'y' + x'y'", "x'x' = x', y'y' = y'"),
            ("x'y'", "A + A = A")]),
        ("d", True, "xy + x(wz + wz')", "x(y + w)", 3, "wxyz", [
            (f"xy + x{hl('w(z + z′)')}".replace("′", "'"), "factor w inside the bracket"),
            ("xy + xw", "z + z' = 1"),
            ("x(y + w)", "factor out x")]),
        ("e", True, "(BC' + A'D)(AB' + CD')", "0", None, "ABCD", [
            ("BC'AB' + BC'CD' + A'DAB' + A'DCD'", "multiply out: 4 products"),
            (f"A{hl('BB′')}C' + B{hl('C′C')}D' + {hl('A′A')}B'D + A'C{hl('DD′')}".replace("′", "'"), "every product holds a letter and its complement"),
            ("0 + 0 + 0 + 0 = 0", "XX' = 0")]),
        ("f", False, "(x + y' + z')(x' + z')", "z' + x'y'", 3, "xyz", [
            ("(z' + x + y')(z' + x')", "reorder so z' leads both brackets"),
            (f"z' + {hl('(x + y′)x′')}".replace("′", "'"), "distributive backwards: (A + B)(A + C) = A + BC"),
            ("z' + xx' + x'y'", "multiply out"),
            ("z' + x'y'", "xx' = 0")]),
    ]
    qs = []
    for part, star, fn, ans, L, vars_, rows in T23:
        qs.append(bool_q(tag("2.3", part, star), f"Simplify to a minimum number of literals: <code>{fn}</code>",
                         vars_, fn, ans, steps(rows), lits_=L, ref="06 §3"))
    P.append({"n": "2.3", "text": "Simplify to a minimum number of literals.", "qs": qs})

    # ---------------------------------------------------------------- 2.4
    T24 = [
        ("a", True, "A'C' + ABC + AC'", "C' + AB", 3, "ABC", "three", [
            (f"{hl('C′(A′ + A)')} + ABC".replace("′", "'"), "terms 1 and 3 share C'"),
            ("C' + ABC", "A' + A = 1"),
            ("C' + AB", "x + x'y = x + y, with x = C'")]),
        ("b", True, "(x'y' + z)' + z + xy + wz", "x + y + z", 3, "wxyz", "three", [
            (f"{hl('(x′y′)′z′')} + z + xy + wz".replace("′", "'"), "De Morgan: (P + z)' = P'z'"),
            (f"{hl('(x + y)')}z' + z + xy + wz", "De Morgan: (x'y')' = x + y"),
            ("xz' + yz' + z + xy + wz", "multiply out"),
            ("xz' + yz' + z + xy", "wz is absorbed by z"),
            (f"{hl('x + y + z')} + xy", "z + xz' = z + x and z + yz' = z + y"),
            ("x + y + z", "xy is absorbed by x")]),
        ("c", True, "A'B(D' + C'D) + B(A + A'CD)", "B", 1, "ABCD", "one", [
            (f"A'B{hl('(D′ + C′)')} + B{hl('(A + CD)')}".replace("′", "'"), "x + x'y = x + y, twice"),
            ("B[A'D' + A'C' + A + CD]", "factor out B"),
            (f"B[{hl('A + D′ + C′')} + CD]".replace("′", "'"), "A + A'D' = A + D', A + A'C' = A + C'"),
            (f"B[A + D' + {hl('C′ + D')}]".replace("′", "'"), "C' + CD = C' + D"),
            ("B[1]", "D' + D = 1, so the whole bracket is 1"),
            ("B", "B·1 = B")]),
        ("d", True, "(A' + C)(A' + C')(A + B + C'D)", "A'(B + C'D)", 4, "ABCD", "four", [
            (f"{hl('(A′ + CC′)')}(A + B + C'D)".replace("′", "'"), "distributive backwards on the first two brackets"),
            ("A'(A + B + C'D)", "CC' = 0"),
            ("A'A + A'B + A'C'D", "multiply out"),
            ("A'B + A'C'D", "A'A = 0"),
            ("A'(B + C'D)", "factor A' back out: 4 literals (the SOP has 5)")]),
        ("e", False, "ABCD + A'BD + ABC'D", "BD", 2, "ABCD", "two", [
            (f"{hl('ABD(C + C′)')} + A'BD".replace("′", "'"), "terms 1 and 3 share ABD"),
            ("ABD + A'BD", "C + C' = 1"),
            ("BD(A + A')", "factor out BD"),
            ("BD", "A + A' = 1")]),
    ]
    qs = []
    for part, star, fn, ans, L, vars_, word, rows in T24:
        qs.append(bool_q(tag("2.4", part, star), f"Reduce to <b>{word}</b> literal{'s' if L > 1 else ''}: <code>{fn}</code>",
                         vars_, fn, ans, steps(rows), lits_=L, ref="06 §3"))
    P.append({"n": "2.4", "text": "Reduce each expression to the given number of literals.", "qs": qs})

    # ---------------------------------------------------------------- 2.5 / 2.6 / 2.7 diagrams
    for n, table, src in [("2.5", T22, "2.2"), ("2.6", T23, "2.3"), ("2.7", T24, "2.4")]:
        qs = []
        for row in table:
            part, fn, ans = row[0], row[2], row[3]
            vars_ = {"2.2": {"a": "xy", "b": "xy", "d": "AB"}.get(part, "xyz")}.get(src) or row[5]
            if src == "2.3":
                vars_ = row[5]
            if src == "2.4":
                vars_ = row[5]
            nm = f"c{src.replace('.', '-')}{part}"
            go, gs = draw_card(nm, fn, fn, ans, vars_)
            qs.append(work_q(tag(n, part), f"Draw the logic diagram for the original <code>{fn}</code> and for the simplified "
                             f"<code>F = {ans}</code> (from {src} {part}).",
                             img(nm, "before and after circuits") +
                             f"<p><b>{go} gates → {gs} gate{'s' if gs != 1 else ''}.</b> Complemented inputs (x') are drawn as already available, like the book does. "
                             "Draw an inverter on each one if your lecturer wants them shown.</p>", ref="06 §4"))
            qs[-1]["nomock"] = True
        if src == "2.2":
            go, gs = draw_card("c2-2f", "(x + y + z')(x' + y' + z)", "(x + y + z')(x' + y' + z)", "x'z' + yz + xy'", "xyz")
            qs.append(work_q(tag(n, "f"), "Draw the logic diagram for <code>(x + y + z')(x' + y' + z)</code> and for the simplified "
                             "<code>x'z' + yz + xy'</code> (from 2.2 f).",
                             img("c2-2f") + f"<p>{go} gates either way. This one didn't get cheaper: the original was already minimal.</p>",
                             ref="06 §4"))
            qs[-1]["nomock"] = True
            qs.sort(key=lambda q: q["tag"])
        P.append({"n": n, "text": f"Draw the logic diagrams for the original and simplified expressions in Problem {src}.", "qs": qs})

    # ---------------------------------------------------------------- 2.8
    P.append({"n": "2.8", "text": "Find the complement of F = wx + yz; then show FF' = 0 and F + F' = 1.", "qs": [
        bool_q(tag("2.8"), "F = <code>wx + yz</code>. Find <b>F'</b> (no bar over a group). Then show FF' = 0 and F + F' = 1 on paper.",
               "wxyz", "(wx + yz)'", "(w' + x')(y' + z')",
               steps([("F' = (wx + yz)'", "complement the whole thing"),
                      (f"{hl('(wx)′')}·{hl('(yz)′')}".replace("′", "'"), "De Morgan: (A + B)' = A'B'"),
                      ("(w' + x')(y' + z')", "De Morgan again: (AB)' = A' + B'")]) +
               "<p><b>FF' = 0:</b> FF' = (wx + yz)(w' + x')(y' + z'). "
               "wx(w' + x') = ww'x + wxx' = 0, and yz(y' + z') = 0. Every product dies, so <b>FF' = 0</b>.</p>"
               "<p><b>F + F' = 1:</b> F' = w'y' + w'z' + x'y' + x'z'. If wx = 1 or yz = 1 then F = 1. "
               "If not, one of w, x is 0 <i>and</i> one of y, z is 0, so one of those four F' terms is 1. Either way the sum is <b>1</b>.</p>",
               lits_=4, ref="06 §3")]})

    # ---------------------------------------------------------------- 2.9
    P.append({"n": "2.9", "text": "Find the complement of each expression.", "qs": [
        bool_q(tag("2.9", "a", True), "Find the complement of <code>xy' + x'y</code> (no bar over a group).", "xy",
               "(xy' + x'y)'", "xy + x'y'",
               steps([(f"{hl('(xy′)′')}·{hl('(x′y)′')}".replace("′", "'"), "De Morgan on the +"),
                      ("(x' + y)(x + y')", "De Morgan on each product: flip letters, AND → OR"),
                      ("x'x + x'y' + xy + yy'", "multiply out"),
                      ("xy + x'y'", "x'x = 0, yy' = 0")]) +
               "<p>Makes sense: xy' + x'y is XOR, and its complement is XNOR (1 when x and y are equal).</p>", lits_=4, ref="06 §3"),
        bool_q(tag("2.9", "b"), "Find the complement of <code>(A'B + CD)E' + E</code> (no bar over a group).", "ABCDE",
               "((A'B + CD)E' + E)'", "(A + B')(C' + D')E'",
               steps([("(A'B + CD)E' + E = A'B + CD + E", "simplify first: PE' + E = P + E"),
                      ("(A'B)'·(CD)'·E'", "De Morgan on the three-way OR"),
                      ("(A + B')(C' + D')E'", "De Morgan on each product")]) +
               "<p>Tip: simplifying <i>before</i> complementing saves a lot of writing.</p>", ref="06 §3"),
        bool_q(tag("2.9", "c"), "Find the complement of <code>(x' + y + z')(x + y')(x + z)</code> (no bar over a group).", "xyz",
               "((x' + y + z')(x + y')(x + z))'", "xy'z + x'y + x'z'",
               steps([("(x' + y + z')' + (x + y')' + (x + z)'", "De Morgan: a complemented product becomes a sum"),
                      ("xy'z + x'y + x'z'", "De Morgan on each sum: flip letters, OR → AND")]) +
               "<p>Rule of thumb: <b>flip every letter, swap AND ↔ OR</b>. Done.</p>", ref="06 §3")]})

    # ---------------------------------------------------------------- 2.11
    P.append({"n": "2.11", "text": "List the truth table of each function.", "qs": [
        tt_q(tag("2.11", "a", True), "Fill the truth table for <code>F = xy + xy' + y'z</code>.", "xyz", {"F": "xy + xy' + y'z"},
             "<p>Simplify first: xy + xy' = x, so <b>F = x + y'z</b>.</p>"
             "<p>Bottom half (x = 1): all 1. Top half (x = 0): F = y'z, which is 1 only on 001.</p>", ref="06 §2"),
        tt_q(tag("2.11", "b"), "Fill the truth table for <code>F = x'z' + yz</code>.", "xyz", {"F": "x'z' + yz"},
             "<p>x'z' is 1 on 000 and 010. yz is 1 on 011 and 111. So F = 1 on rows <b>0, 2, 3, 7</b>.</p>", ref="06 §2")]})

    # ---------------------------------------------------------------- 2.12
    A, B = "10110001", "10101100"
    r = {"AND": "".join(str(int(a) & int(b)) for a, b in zip(A, B)),
         "OR": "".join(str(int(a) | int(b)) for a, b in zip(A, B)),
         "XOR": "".join(str(int(a) ^ int(b)) for a, b in zip(A, B)),
         "NOT A": "".join("1" if a == "0" else "0" for a in A),
         "NOT B": "".join("1" if b == "0" else "0" for b in B)}
    assert r["AND"] == "10100000" and r["XOR"] == "00011101"
    rows = "".join(f"<tr><th>{k}</th>" + "".join(f"<td>{c}</td>" for c in v) + "</tr>" for k, v in
                   [("A", A), ("B", B)] + list(r.items()))
    P.append({"n": "2.12", "text": "Bitwise AND, OR, XOR, NOT A, NOT B of A = 10110001 and B = 10101100.", "qs": [
        multi_q(tag("2.12", "", True).replace(" ()", ""), "A = <code>10110001</code>, B = <code>10101100</code>. Work out each 8-bit result bit by bit "
                "(parts a, c, d are starred).", [(k, [v]) for k, v in r.items()],
                f"<table class='bits'>{rows}</table>"
                "<p>Line the bits up in columns and do each column on its own. AND: 1 only if both are 1. OR: 1 if either is 1. "
                "XOR: 1 if they differ. NOT: flip.</p>", ref="06 §1")]})

    # ---------------------------------------------------------------- 2.13
    qs = []
    for part, ex in [("a", "A + B + B'(A + C')"), ("b", "A(B ⊕ D) + C'"), ("c", "A + CD + ABC"),
                     ("d", "(A ⊕ C)' + B"), ("e", "(A' + B')(C + D')"), ("f", "(A + B')(C' + D)")]:
        nm = f"c2-13{part}"
        tr = to_draw(parse(ex))
        assert draw_matches(tr, ex, "ABCD")
        g, i = gate_count(tr)
        save_circuits(nm, [{"title": f"Y = {ex}", "tree": tr, "out": "Y", "note": f"{g} gates"}], ex)
        extra = {"a": "<p>Not asked, but it simplifies a lot: B + B'(A + C') = B + A + C', so Y = <b>A + B + C'</b> (one 3-input OR).</p>",
                 "c": "<p>Not asked, but ABC is absorbed by A, so Y = <b>A + CD</b>.</p>",
                 "d": "<p>(A ⊕ C)' is one XNOR gate: an XOR with a bubble on the output.</p>",
                 "f": "<p>Product of sums: two OR gates feeding one AND gate.</p>"}.get(part, "")
        qs.append(work_q(tag("2.13", part), f"Draw the logic diagram for <code>Y = {ex}</code>.",
                         img(nm, "logic diagram") + "<p>Build it from the inside out: innermost bracket first, the outer operation is the last gate.</p>" + extra,
                         ref="06 §1"))
    P.append({"n": "2.13", "text": "Draw logic diagrams for each expression.", "qs": qs})

    # ---------------------------------------------------------------- 2.14
    F = "xy + x'y' + y'z"
    N = lambda v: G("NOT", v)
    impl = [
        ("a", "AND, OR and inverter gates", G("OR", G("AND", "x", "y"), G("AND", N("x"), N("y")), G("AND", N("y"), "z")),
         "<p>Straight from the SOP: one AND per term, one OR to join them. Inverters make x' and y'.</p>", False),
        ("b", "OR and inverter gates", G("OR", N(G("OR", N("x"), N("y"))), N(G("OR", "x", "y")), N(G("OR", "y", N("z")))),
         steps([("xy = (x' + y')'", "De Morgan: an AND is a NOR of the complements"),
                ("x'y' = (x + y)'", "same"),
                ("y'z = (y + z')'", "same"),
                ("F = (x' + y')' + (x + y)' + (y + z')'", "every AND is now an OR followed by an inverter")], final=False), True),
        ("c", "AND and inverter gates", N(G("AND", N(G("AND", "x", "y")), N(G("AND", N("x"), N("y"))), N(G("AND", N("y"), "z")))),
         steps([("F = [(xy)'·(x'y')'·(y'z)']'", "De Morgan on the whole OR: A + B + C = (A'B'C')'"),
                ("ANDs, inverter on each, AND them, inverter at the end", "only AND and NOT used")], final=False), False),
        ("d", "NAND and inverter gates", G("NAND", G("NAND", "x", "y"), G("NAND", N("x"), N("y")), G("NAND", N("y"), "z")),
         steps([("F = [(xy)'·(x'y')'·(y'z)']'", "same De Morgan as (c)"),
                ("each (AB)' is a NAND, and the outer [ ]' is a NAND", "AND then NOT = NAND")], final=False) +
         "<p>This is the standard <b>NAND-NAND</b> form of an SOP (Topic 09).</p>", False),
        ("e", "NOR and inverter gates", N(G("NOR", G("NOR", N("x"), N("y")), G("NOR", "x", "y"), G("NOR", "y", N("z")))),
         steps([("xy = (x' + y')', x'y' = (x + y)', y'z = (y + z')'", "each AND term as a NOR"),
                ("F = [ (x'+y')' + (x+y)' + (y+z')' ]''", "OR = NOR then NOT")], final=False), False),
    ]
    qs = []
    for part, gates, tree, why, star in impl:
        assert draw_matches(tree, F, "xyz"), part
        g, i = gate_count(tree)
        nm = f"c2-14{part}"
        save_circuits(nm, [{"title": f"F = xy + x'y' + y'z with {gates}", "tree": tree, "out": "F",
                            "note": f"{g} gates drawn (one inverter per complemented input; you can share them)"}], "2.14" + part)
        qs.append(work_q(tag("2.14", part, star), f"Implement <code>F = {F}</code> with <b>{gates}</b> only.",
                         why + img(nm, "circuit") , ref="06 §3"))
    P.append({"n": "2.14", "text": "Implement F = xy + x'y' + y'z with each set of gates.", "qs": qs})

    # ---------------------------------------------------------------- 2.15
    P.append({"n": "2.15", "text": "Simplify T₁ and T₂ from the truth table.", "qs": [
        bool_q(tag("2.15", "T₁", True), "Truth table: T₁ = 1 on ABC = 000, 001, 010 only. Simplify T₁ to a minimum number of literals.",
               "ABC", "A'B'C' + A'B'C + A'BC'", "A'B' + A'C'",
               ttable("ABC", {"T₁": tt("A'B' + A'C'", "ABC"), "T₂": tt("A + BC", "ABC")}) +
               steps([("A'B'C' + A'B'C + A'BC'", "one minterm per 1"),
                      (f"{hl('A′B′')} + A'BC'".replace("′", "'"), "first two: A'B'(C' + C)"),
                      (f"A'{hl('(B′ + BC′)')}".replace("′", "'"), "factor A'"),
                      ("A'(B' + C') = A'B' + A'C'", "B' + BC' = B' + C'")]) +
               "<p>A'(B' + C') is only 3 literals, the book gives A'B' + A'C'. Both are accepted here.</p>", lits_=4, ref="06 §3"),
        bool_q(tag("2.15", "T₂", True), "Same table: T₂ = 1 on ABC = 011, 100, 101, 110, 111. Simplify T₂.",
               "ABC", "A'BC + A", "A + BC",
               steps([("A'BC + AB'C' + AB'C + ABC' + ABC", "one minterm per 1"),
                      ("A'BC + A", "the four A terms cover every BC combination: they sum to A"),
                      ("A + BC", "A + A'BC = A + BC")]) +
               "<p>Also notice T₂ = T₁' (the columns are opposite), and (A'(B' + C'))' = A + BC by De Morgan.</p>", lits_=3, ref="06 §3")]})

    # ---------------------------------------------------------------- 2.18
    F = "xy'z + x'y'z + w'xy + wx'y + wxy"
    S18 = "y'z + xy + wy"
    assert same(F, S18, "wxyz")
    o = ones(F, "wxyz")
    go, gs = draw_card("c2-18", F, F, S18, "wxyz")
    save_kmap("k2-18", "wxyz", o, [
        {"cells": [1, 5, 9, 13], "color": "red", "label": "y'z"},
        {"cells": [6, 7, 14, 15], "color": "blue", "label": "xy"},
        {"cells": [10, 11, 14, 15], "color": "green", "label": "wy"}], "F = y'z + xy + wy")
    P.append({"n": "2.18", "text": f"F = {F}: truth table, diagrams, simplification.", "qs": [
        tt_q(tag("2.18", "a"), f"Fill the truth table for <code>F = {F}</code>.", "wxyz", {"F": F},
             f"<p>Find each term's rows: xy'z → 5, 13 · x'y'z → 1, 9 · w'xy → 6, 7 · wx'y → 10, 11 · wxy → 14, 15.</p>"
             f"<p>So F = 1 on rows <b>{lst(o)}</b>, 0 everywhere else.</p>", ref="06 §2"),
        work_q(tag("2.18", "b"), f"Draw the logic diagram of <code>F = {F}</code> as written.",
               img("c2-18", "circuits") + f"<p>The top circuit is the answer to (b): five 3-input ANDs into a 5-input OR = {go} gates.</p>", ref="06 §1"),
        bool_q(tag("2.18", "c", True), f"Simplify with Boolean algebra: <code>F = {F}</code>.", "wxyz", F, S18,
               steps([(f"{hl('y′z(x + x′)')} + w'xy + wx'y + wxy".replace("′", "'"), "terms 1 + 2 share y'z"),
                      ("y'z + w'xy + wx'y + wxy + wxy", "copy wxy (A = A + A) so it can pair twice"),
                      (f"y'z + {hl('xy(w′ + w)')} + {hl('wy(x′ + x)')}".replace("′", "'"), "pair w'xy with wxy, and wx'y with wxy"),
                      ("y'z + xy + wy", "w' + w = 1, x' + x = 1")]) +
               img("k2-18", "K-map check") + "<p>Factored, y'z + y(w + x) is 5 literals. Both accepted.</p>", lits_=6, ref="06 §4"),
        work_q(tag("2.18", "d"), f"Get the truth table from your simplified <code>F = {S18}</code> and show it matches (a).",
               ttable("wxyz", {"(a)": tt(F, "wxyz"), "y'z+xy+wy": tt(S18, "wxyz")}) + "<p>Identical on all 16 rows, so the simplification is right.</p>",
               ref="06 §2"),
        work_q(tag("2.18", "e"), "Draw the simplified circuit and compare the gate count with (b).",
               img("c2-18", "circuits") + f"<p><b>{go} gates → {gs} gates</b> (and every AND drops from 3 inputs to 2). "
               "Fewer gates and fewer inputs = cheaper and faster.</p>", ref="06 §4")]})

    # ---------------------------------------------------------------- 2.23
    qs = []
    for part, ex in [("a", "BC' + AB + ACD"), ("b", "(A + B)(C + D)(A' + B + D)"),
                     ("c", "(AB + A'B')(CD' + C'D)"), ("d", "A + CD + (A + D')(C' + D)")]:
        nm = f"c2-23{part}"
        tr = to_draw(parse(ex))
        assert draw_matches(tr, ex, "ABCD")
        g, i = gate_count(tr)
        save_circuits(nm, [{"title": f"F = {ex}", "tree": tr, "out": "F", "note": f"{g} gates, as written (not simplified)"}], ex)
        note = {"a": "SOP → AND gates into one OR.", "b": "POS → OR gates into one AND.",
                "c": "Each bracket is a small SOP (it's XNOR(A,B) and XOR(C,D)); an AND joins them.",
                "d": "Three things ORed: A, the AND CD, and the POS block (A + D')(C' + D)."}[part]
        qs.append(work_q(tag("2.23", part), f"Draw the logic diagram for <code>{ex}</code> <b>without simplifying</b>.",
                         img(nm, "logic diagram") + f"<p>{note}</p>", ref="06 §1"))
    P.append({"n": "2.23", "text": "Draw the logic diagram for each expression without simplifying.", "qs": qs})

    # ---------------------------------------------------------------- 2.24 / 2.25 / 2.26
    P.append({"n": "2.24", "text": "Show that the dual of XOR equals its complement (same as 3.27).", "qs": [
        work_q(tag("2.24") + " · also 3.27", "Show that the <b>dual</b> of the exclusive-OR is equal to its <b>complement</b>.",
               steps([("x ⊕ y = xy' + x'y", "XOR as SOP"),
                      ("dual = (x + y')(x' + y)", "dual: swap AND ↔ OR (and 0 ↔ 1), keep the letters"),
                      ("xx' + xy + y'x' + y'y", "multiply out"),
                      ("xy + x'y'", "xx' = 0, yy' = 0"),
                      ("(x ⊕ y)' = (xy' + x'y)' = (x' + y)(x + y') = xy + x'y'", "the complement, by De Morgan"),
                      ("dual = complement = XNOR", "both are xy + x'y'")]), ref="06 §3")]})
    P.append({"n": "2.25", "text": "Inhibition (x/y = xy') and XOR: commutative? associative?", "qs": [
        work_q(tag("2.25", "a"), "Inhibition is <code>x / y = xy'</code> (x but not y). Show it is <b>neither commutative nor associative</b>.",
               "<p><b>Commutative?</b> x/y = xy' but y/x = yx'. Try x = 1, y = 0: xy' = 1, yx' = 0. Different, so <b>not commutative</b>.</p>"
               + steps([("(x/y)/z = (xy')z' = xy'z'", "apply the rule twice from the left"),
                        ("x/(y/z) = x(yz')' = x(y' + z) = xy' + xz", "from the right; De Morgan"),
                        ("try x = y = z = 1: left = 0, right = 1", "one counter-example is enough")], final=False)
               + "<p>So it's <b>not associative</b> either.</p>", ref="06 §3"),
        work_q(tag("2.25", "b"), "Show that XOR is <b>commutative and associative</b>.",
               "<p><b>Commutative:</b> x ⊕ y = xy' + x'y = yx' + y'x = y ⊕ x. ✓</p>"
               + steps([("(x ⊕ y) ⊕ z = (xy' + x'y)z' + (xy' + x'y)'z", "A ⊕ z = Az' + A'z"),
                        ("= xy'z' + x'yz' + (xy + x'y')z", "the complement of XOR is XNOR"),
                        ("= xy'z' + x'yz' + xyz + x'y'z", "multiply out"),
                        ("x ⊕ (y ⊕ z) = x(yz + y'z') + x'(yz' + y'z)", "same rule from the other side"),
                        ("= xyz + xy'z' + x'yz' + x'y'z", "same four minterms ✓")], final=False)
               + "<p>Both are 1 when an <b>odd</b> number of inputs are 1, so the brackets don't matter.</p>", ref="06 §3")]})
    hl_tab = ("<table class='bits'><tr><th>x</th><th>y</th><th>NAND (voltages)</th><th>pos: 1=H</th><th>neg: 1=L</th></tr>"
              "<tr><td>L</td><td>L</td><td>H</td><td>00 → 1</td><td>11 → 0</td></tr>"
              "<tr><td>L</td><td>H</td><td>H</td><td>01 → 1</td><td>10 → 0</td></tr>"
              "<tr><td>H</td><td>L</td><td>H</td><td>10 → 1</td><td>01 → 0</td></tr>"
              "<tr><td>H</td><td>H</td><td>L</td><td>11 → 0</td><td>00 → 1</td></tr></table>")
    P.append({"n": "2.26", "text": "Positive-logic NAND = negative-logic NOR, and vice versa.", "qs": [
        work_q(tag("2.26"), "Show that a positive-logic NAND gate is a negative-logic NOR gate, and vice versa.",
               hl_tab + "<p>Write the gate as voltages (H/L). In <b>positive logic</b> H = 1: output 0 only on 11 → <b>NAND</b>. "
               "In <b>negative logic</b> L = 1: read the same rows again, output 1 only when both inputs are 0 → <b>NOR</b>.</p>"
               "<p>Same physical gate, different labels. Swapping 0 ↔ 1 everywhere turns every function into its dual, "
               "and the dual of NAND is NOR. The NOR → NAND direction works the same way.</p>", ref="06 §1")]})

    # ---------------------------------------------------------------- 2.27
    f1 = [1, 0, 0, 1, 0, 0, 1, 1]
    f2 = [0, 0, 1, 1, 1, 1, 1, 0]
    m1 = [m for m in range(8) if f1[m]]
    m2 = [m for m in range(8) if f2[m]]
    assert ones("a'b'c' + ab + bc", "abc") == m1 and ones("a'b + ab' + bc'", "abc") == m2
    save_kmap("k2-27f1", "abc", m1, [{"cells": [0], "color": "red", "label": "a'b'c'"},
                                    {"cells": [3, 7], "color": "blue", "label": "bc"},
                                    {"cells": [6, 7], "color": "green", "label": "ab"}], "f₁ = a'b'c' + bc + ab")
    save_kmap("k2-27f2", "abc", m2, [{"cells": [2, 3], "color": "red", "label": "a'b"},
                                    {"cells": [4, 5], "color": "blue", "label": "ab'"},
                                    {"cells": [2, 6], "color": "green", "label": "bc'"}], "f₂ = a'b + ab' + bc'")
    save_circuits("c2-27", [{"title": "f₁ = a'b'c' + bc + ab", "tree": "a'b'c' + bc + ab", "out": "f₁"},
                            {"title": "f₂ = a'b + ab' + bc'", "tree": "a'b + ab' + bc'", "out": "f₂"}], "2.27 circuits")
    tab = ("<table class='bits'><tr><th>abc</th>" + "".join(f"<td>{m:03b}</td>" for m in range(8)) + "</tr>"
           "<tr><th>f₁</th>" + "".join(f"<td>{v}</td>" for v in f1) + "</tr><tr><th>f₂</th>" + "".join(f"<td>{v}</td>" for v in f2) + "</tr></table>")
    P.append({"n": "2.27", "text": "Write the equations and draw the circuit for the f₁, f₂ truth table.", "qs": [
        bool_q(tag("2.27", "f₁"), "Table: " + tab + " Write a minimal SOP for <b>f₁</b>.", "abc", f"a'b'c' + a'bc + abc' + abc",
               "a'b'c' + bc + ab", f"<p>f₁ = Σm({lst(m1)}).</p>" + img("k2-27f1") +
               "<p>Row 0 has no neighbouring 1s, so a'b'c' stays as it is. 3 joins 7 (bc), 6 joins 7 (ab).</p>", lits_=7, ref="06 §2"),
        bool_q(tag("2.27", "f₂"), "Same table. Write a minimal SOP for <b>f₂</b>.", "abc", "a'bc' + a'bc + ab'c' + ab'c + abc'",
               "a'b + ab' + bc'", f"<p>f₂ = Σm({lst(m2)}).</p>" + img("k2-27f2") +
               "<p>ac' (cells 4, 6) works instead of bc' too. Also f₂ = (a ⊕ b) + bc'.</p>", lits_=6, ref="06 §2"),
        work_q(tag("2.27", "diagram"), "Draw the logic diagram for f₁ and f₂.", img("c2-27", "circuits") +
               "<p>Two AND-OR circuits. Inputs a', b', c' come from inverters (or are drawn as available).</p>", ref="06 §1")]})

    # ---------------------------------------------------------------- 2.28
    ta = G("NOT", G("NAND", "a", G("NAND", "b", "c", "d"), "e"))
    assert draw_matches(ta, "ae(b' + c' + d')", "abcde")
    save_circuits("p2-28a", [{"title": "Fig 2.28(a)", "tree": ta, "out": "y"}], "Fig 2.28a")
    y1 = G("XOR", "a", G("OR", "c", "d", "e"))
    y2 = G("NOT", G("NAND", G("NOT", "b"), G("OR", "c", "d", "e"), "f"))
    assert draw_matches(y1, "a ⊕ (c + d + e)", "abcdef") and draw_matches(y2, "b'f(c + d + e)", "abcdef")
    save_circuits("p2-28b", [{"title": "Fig 2.28(b), output y₁", "tree": y1, "out": "y₁"},
                             {"title": "output y₂ (the same OR gate c + d + e feeds both)", "tree": y2, "out": "y₂"}], "Fig 2.28b")
    oa = ones("ae(b' + c' + d')", "abcde")
    qa = bool_q(tag("2.28", "a"), "Fig 2.28(a): NAND(b, c, d) feeds a 3-input NAND with a and e, then an inverter gives y. Write y.",
                "abcde", "((a(bcd)'e)')'", "ae(b' + c' + d')",
                steps([("N₁ = (bcd)'", "first NAND"),
                       ("N₂ = (a·N₁·e)' = (a(bcd)'e)'", "second NAND"),
                       ("y = N₂' = a(bcd)'e", "the inverter cancels the bar"),
                       ("y = ae(b' + c' + d')", "De Morgan on (bcd)'")]) +
                f"<p>Truth table (32 rows): y = 1 only when a = e = 1 and b, c, d are <i>not</i> all 1: rows <b>{lst(oa)}</b>. Every other row is 0.</p>",
                ref="06 §2")
    qa["svg"] = "book/p2-28a"
    qb1 = bool_q(tag("2.28", "b · y₁"), "Fig 2.28(b): write <b>y₁</b>.", "abcdef", "a ⊕ (c + d + e)", "a ⊕ (c + d + e)",
                 "<p>The OR gate gives c + d + e. The XOR combines it with a: <b>y₁ = a ⊕ (c + d + e)</b>.</p>"
                 "<p>Truth table: y₁ = 1 when exactly one of a and (c + d + e) is 1. b and f don't matter.</p>", ref="06 §1")
    qb1["svg"] = "book/p2-28b"
    qb2 = bool_q(tag("2.28", "b · y₂"), "Fig 2.28(b): write <b>y₂</b>.", "abcdef", "b'f(c + d + e)", "b'f(c + d + e)",
                 steps([("NAND(b', c + d + e, f) = (b'(c + d + e)f)'", "3-input NAND"),
                        ("y₂ = b'(c + d + e)f", "the inverter cancels the bar")]) +
                 "<p>Truth table: y₂ = 1 only when b = 0, f = 1 and at least one of c, d, e is 1. a doesn't matter.</p>", ref="06 §1")
    qb2["svg"] = "book/p2-28b"
    P.append({"n": "2.28", "text": "Write the Boolean expressions and truth tables for the two circuits.", "qs": [qa, qb1, qb2]})

    # ---------------------------------------------------------------- 4.1
    T = {"T₁": "B'C", "T₂": "A'B", "T₃": "A + B'C", "T₄": "A'B ⊕ D", "F₁": "A + B'C + (A'B ⊕ D)", "F₂": "A'B + D"}
    t1 = G("AND", G("NOT", "B"), "C", label="T₁")
    f1 = G("OR", G("OR", "A", t1, label="T₃"), G("XOR", G("AND", G("NOT", "A"), "B", label="T₂"), "D", label="T₄"))
    f2 = G("OR", G("AND", G("NOT", "A"), "B", label="T₂"), "D")
    assert draw_matches(f1, T["F₁"], "ABCD") and draw_matches(f2, T["F₂"], "ABCD")
    save_circuits("p4-1", [{"title": "Fig P4.1, output F₁", "tree": f1, "out": "F₁"},
                           {"title": "output F₂ (T₂ is one shared gate in the book)", "tree": f2, "out": "F₂"}], "Fig P4.1")
    F1min = "A + (B ⊕ D) + B'C"
    assert same(F1min, T["F₁"], "ABCD")
    save_kmap("k4-1f1", "ABCD", ones(T["F₁"], "ABCD"), [
        {"cells": [8, 9, 10, 11, 12, 13, 14, 15], "color": "red", "label": "A"},
        {"cells": [1, 3, 9, 11], "color": "blue", "label": "B'D"},
        {"cells": [4, 6, 12, 14], "color": "green", "label": "BD'"},
        {"cells": [2, 3, 10, 11], "color": "purple", "label": "B'C"}], "F₁ = A + B'D + BD' + B'C")
    save_kmap("k4-1f2", "ABCD", ones(T["F₂"], "ABCD"), [
        {"cells": [1, 3, 5, 7, 9, 11, 13, 15], "color": "red", "label": "D"},
        {"cells": [4, 5, 6, 7], "color": "blue", "label": "A'B"}], "F₂ = A'B + D")
    qf1 = bool_q(tag("4.1", "a · F₁", True), "Fig P4.1: write T₁ to T₄, then <b>F₁</b> in terms of A, B, C, D.", "ABCD", T["F₁"], F1min,
                 "<p>T₁ = <b>B'C</b> · T₂ = <b>A'B</b> · T₃ = A + T₁ = <b>A + B'C</b> · T₄ = T₂ ⊕ D = <b>A'B ⊕ D</b></p>"
                 + steps([("F₁ = T₃ + T₄ = A + B'C + (A'B ⊕ D)", "OR of T₃ and T₄"),
                          ("A'B ⊕ D = A'BD' + (A + B')D", "P ⊕ D = PD' + P'D, De Morgan on (A'B)'"),
                          ("F₁ = A + B'C + A'BD' + AD + B'D", "substitute"),
                          ("F₁ = A + B'C + BD' + B'D", "A + A'BD' = A + BD', AD absorbed by A"),
                          ("F₁ = A + B'C + (B ⊕ D)", "BD' + B'D = B ⊕ D")]), ref="06 §4")
    qf1["svg"] = "book/p4-1"
    qf2 = bool_q(tag("4.1", "a · F₂", True), "Fig P4.1: write <b>F₂</b> in terms of A, B, C, D.", "ABCD", T["F₂"], "A'B + D",
                 "<p>F₂ = T₂ + D = <b>A'B + D</b>.</p>", ref="06 §4")
    qf2["svg"] = "book/p4-1"
    qtt = tt_q(tag("4.1", "b"), "Fig P4.1: list T₁, T₂, T₃, T₄, F₁, F₂ for all 16 input combinations.", "ABCD",
               {k: T[k] for k in T}, "<p>Fill T₁ and T₂ first (they only need two inputs each), then build T₃, T₄ from them, then F₁, F₂.</p>"
               "<p>Check: F₁ is 0 only on rows 0, 5, 7. F₂ is 0 only on rows 0, 2, 8, 10, 12, 14.</p>", ref="06 §2")
    assert [m for m in range(16) if not tt(T["F₁"], "ABCD")[m]] == [0, 5, 7]
    assert [m for m in range(16) if not tt(T["F₂"], "ABCD")[m]] == [0, 2, 8, 10, 12, 14]
    qtt["svg"] = "book/p4-1"
    qk = work_q(tag("4.1", "c"), "Plot F₁ and F₂ from your table on K-maps and show they simplify to the same expressions as (a).",
                img("k4-1f1") + img("k4-1f2") + "<p>F₁ = A + B'D + BD' + B'C = A + (B ⊕ D) + B'C ✓. F₂ = A'B + D ✓. "
                "(CD' also works instead of B'C in F₁.)</p>", ref="06 §4")
    P.append({"n": "4.1", "text": "Analyse the circuit of Fig P4.1: T₁ to T₄, F₁, F₂, truth table, maps.", "qs": [qf1, qf2, qtt, qk]})

    # ---------------------------------------------------------------- 4.2
    Ap = G("NOT", "A")
    n1 = G("NAND", G("NOT", "A"), "D", label="N₁")
    n2 = G("NAND", G("NOT", "A"), G("NAND", G("NOT", "A"), "D", label="N₁"), label="N₂")
    orr = G("OR", G("NOT", "A"), G("AND", "B", "C"))
    Ft = G("AND", n2, orr)
    Gt = G("AND", G("OR", G("NOT", "A"), G("AND", "B", "C")), n1)
    assert draw_matches(Ft, "ABC + A'D", "ABCD") and draw_matches(Gt, "ABC + A'D'", "ABCD")
    save_circuits("p4-2", [{"title": "Fig P4.2, output F", "tree": Ft, "out": "F"},
                           {"title": "output G (A', N₁ and the OR gate are shared in the book)", "tree": Gt, "out": "G"}], "Fig P4.2")
    qF = bool_q(tag("4.2", "F", True), "Fig P4.2: find the simplified expression for <b>F</b>.", "ABCD", "(A + D)(A' + BC)", "ABC + A'D",
                steps([("N₁ = (A'D)' = A + D'", "NAND, then De Morgan"),
                       ("N₂ = (A'·N₁)' = (A'(A + D'))' = (A'D')' = A + D", "A'A = 0 inside"),
                       ("OR output = A' + BC", ""),
                       ("F = N₂(A' + BC) = (A + D)(A' + BC)", "the AND gate"),
                       ("AA' + ABC + A'D + BCD", "multiply out"),
                       ("ABC + A'D", "AA' = 0, BCD is the consensus of ABC and A'D")]), lits_=5, ref="06 §4")
    qF["svg"] = "book/p4-2"
    qG = bool_q(tag("4.2", "G", True), "Fig P4.2: find the simplified expression for <b>G</b>.", "ABCD", "(A' + BC)(A + D')", "ABC + A'D'",
                steps([("G = (A' + BC)·N₁ = (A' + BC)(A + D')", "the second AND gate"),
                       ("A'A + A'D' + ABC + BCD'", "multiply out"),
                       ("ABC + A'D'", "A'A = 0, BCD' is the consensus of ABC and A'D'")]), lits_=5, ref="06 §4")
    qG["svg"] = "book/p4-2"
    P.append({"n": "4.2", "text": "Simplified F and G for the circuit of Fig P4.2.", "qs": [qF, qG]})

    n = write_topic("06", "Gates and Boolean algebra",
                    "Mano Ch 2 (plus 1.35, 1.36, 4.1, 4.2). Expressions are checked on every row; where the book asks for a minimum, it must be minimal too.",
                    P)
    return n


# ======================================================================== TOPIC 07
def topic07():
    P = []
    P.append({"n": "2.10", "text": "Show what F₁ + F₂ and F₁F₂ do to minterms.", "qs": [
        work_q(tag("2.10", "a"), "Show that E = F₁ + F₂ contains the sum of the minterms of F₁ and of F₂.",
               steps([("F₁ = Σ(minterms of F₁), F₂ = Σ(minterms of F₂)", "any function is the OR of its minterms"),
                      ("E = F₁ + F₂ = Σ(F₁'s) + Σ(F₂'s)", "OR them"),
                      ("a minterm in both appears twice: m + m = m", "idempotent law"),
                      ("E = Σ(every minterm in F₁ or F₂)", "the union of the two lists")], final=False) +
               "<p>Example: F₁ = Σ(1, 3), F₂ = Σ(3, 6) → E = Σ(1, 3, 6).</p>", ref="07 §3"),
        work_q(tag("2.10", "b"), "Show that G = F₁F₂ contains only the minterms common to F₁ and F₂.",
               steps([("G = (Σ mᵢ)(Σ mⱼ) = Σ mᵢmⱼ", "multiply out every pair"),
                      ("i ≠ j: mᵢmⱼ = 0", "two different minterms differ in some letter, so they contain x·x' = 0"),
                      ("i = j: mᵢmᵢ = mᵢ", "x·x = x"),
                      ("G = Σ(minterms in both lists)", "only the common ones survive")], final=False) +
               "<p>Example: F₁ = Σ(1, 3), F₂ = Σ(3, 6) → G = Σ(3).</p>", ref="07 §3")]})
    P.append({"n": "2.16", "text": "The OR of all minterms of n variables is 1.", "qs": [
        work_q(tag("2.16", "a"), "Prove that the sum of all minterms of a 3-variable function is 1.",
               steps([("x'y'z' + x'y'z + x'yz' + x'yz + xy'z' + xy'z + xyz' + xyz", "all 8 minterms"),
                      ("x'y'(z' + z) + x'y(z' + z) + xy'(z' + z) + xy(z' + z)", "pair them up on z"),
                      ("x'y' + x'y + xy' + xy", "z' + z = 1"),
                      ("x'(y' + y) + x(y' + y) = x' + x", "pair again on y"),
                      ("1", "x' + x = 1")]), ref="07 §3"),
        work_q(tag("2.16", "b"), "Suggest a procedure for a general proof (n variables).",
               "<p><b>Induction.</b> Pair every minterm with the one that differs only in the last variable xₙ. "
               "Each pair is P·xₙ' + P·xₙ = P, so the 2ⁿ minterms of n variables collapse to the 2ⁿ⁻¹ minterms of n − 1 variables. "
               "Repeat until one variable is left: x₁' + x₁ = <b>1</b>.</p>"
               "<p>Or the 'truth table' argument: every row of the table makes exactly one minterm equal 1, so the OR is 1 on every row.</p>",
               ref="07 §3")]})

    qs = []
    for part, star, ex, vars_ in [("a", True, "(xy + z)(y + xz)", "xyz"), ("b", False, "(x + y')(y' + z)", "xyz"),
                                  ("c", False, "x'z + wx'y + wyz' + w'y'", "wxyz"), ("d", False, "(xy + yz' + x'z)(x + z)", "xyz")]:
        o = ones(ex, vars_)
        z = [m for m in range(2 ** len(vars_)) if m not in o]
        hint = {"a": "Easiest row by row: put each xyz into both brackets, F = 1 only if both brackets are 1.",
                "b": "Simplify first: (x + y')(y' + z) = y' + xz. So F = 1 whenever y = 0, plus row 111.",
                "c": "Find each term's rows: x'z → 1, 3, 9, 11 · wx'y → 10, 11 · wyz' → 10, 14 · w'y' → 0, 1, 4, 5. Then merge the lists.",
                "d": "Row by row. F needs (x + z) = 1, so rows 000 and 010 are 0 straight away."}[part]
        qs.append(tt_q(tag("2.17", part, star), f"Fill the truth table for <code>{ex}</code>.", vars_, {"F": ex},
                       f"<p>{hint}</p><p>F = 1 on rows <b>{lst(o)}</b>.</p>", ref="07 §3"))
        qs.append(multi_q(tag("2.17", part, star), f"Now write <code>{ex}</code> as a sum of minterms and a product of maxterms. "
                          "Type just the numbers, smallest first, e.g. 1,3,6.",
                          [("Σm(", set_answers(o)), ("ΠM(", set_answers(z))],
                          f"<p><b>Σm({lst(o)})</b>: the rows where F = 1.</p><p><b>ΠM({lst(z)})</b>: every other row.</p>", ref="07 §3"))
    P.append({"n": "2.17", "text": "Truth table, sum of minterms and product of maxterms.", "qs": qs})

    o = ones("B'D + A'D + BD", "ABCD")
    assert o == [1, 3, 5, 7, 9, 11, 13, 15]
    z = [m for m in range(16) if m not in o]
    P.append({"n": "2.19", "text": "F(A, B, C, D) = B'D + A'D + BD as Σm and ΠM.", "qs": [
        multi_q(tag("2.19", star=True), "<code>F(A, B, C, D) = B'D + A'D + BD</code>. Write it as a sum of minterms and a product of maxterms.",
                [("Σm(", set_answers(o)), ("ΠM(", set_answers(z))],
                steps([("B'D + BD = D", "factor D: B' + B = 1"),
                       ("D + A'D = D", "absorption"),
                       ("F = D", "so F = 1 on every odd row")], final=False) +
                f"<p><b>Σm({lst(o)})</b> and <b>ΠM({lst(z)})</b>.</p>", ref="07 §3")]})

    a20 = [m for m in range(16) if m not in (3, 5, 9, 11, 15)]
    b20 = [2, 4, 5, 7]
    P.append({"n": "2.20", "text": "Express the complement in sum-of-minterms form.", "qs": [
        multi_q(tag("2.20", "a"), "<code>F(A, B, C, D) = Σ(3, 5, 9, 11, 15)</code>. Write <b>F'</b> as a sum of minterms.",
                [("F' = Σm(", set_answers(a20))],
                f"<p>F' is 1 exactly where F is 0: every number 0–15 <i>not</i> in F's list. <b>F' = Σm({lst(a20)})</b>.</p>", ref="07 §3"),
        multi_q(tag("2.20", "b"), "<code>F(x, y, z) = Π(2, 4, 5, 7)</code>. Write <b>F'</b> as a sum of minterms.",
                [("F' = Σm(", set_answers(b20))],
                "<p>F = Π(2, 4, 5, 7) means F is <b>0</b> on rows 2, 4, 5, 7. F' is 1 on those rows.</p>"
                f"<p><b>F' = Σm({lst(b20)})</b>: the same numbers, just switch Π → Σ.</p>", ref="07 §3")]})
    P.append({"n": "2.21", "text": "Convert to the other canonical form.", "qs": [
        multi_q(tag("2.21", "a"), "<code>F(x, y, z) = Σ(2, 5, 6)</code>. Write F as a product of maxterms.",
                [("ΠM(", set_answers([0, 1, 3, 4, 7]))],
                "<p>Swap the symbol and list the missing numbers from 0–7: <b>ΠM(0, 1, 3, 4, 7)</b>.</p>", ref="07 §3"),
        multi_q(tag("2.21", "b"), "<code>F(A, B, C, D) = Π(0, 1, 2, 4, 7, 9, 12)</code>. Write F as a sum of minterms.",
                [("Σm(", set_answers([3, 5, 6, 8, 10, 11, 13, 14, 15]))],
                "<p>Missing from 0–15: <b>Σm(3, 5, 6, 8, 10, 11, 13, 14, 15)</b>.</p>", ref="07 §3")]})

    P.append({"n": "2.22", "text": "Convert into sum of products and product of sums.", "qs": [
        bool_q(tag("2.22", "a · SOP", True), "Write <code>(AB + C)(B + C'D)</code> as a <b>sum of products</b> (simplest).", "ABC D".replace(" ", ""),
               "(AB + C)(B + C'D)", "AB + BC",
               steps([("AB·B + AB·C'D + C·B + C·C'D", "multiply out"),
                      ("AB + ABC'D + BC + 0", "BB = B, CC' = 0"),
                      ("AB + BC", "ABC'D is absorbed by AB")]), lits_=4, form="sop", ref="07 §1"),
        bool_q(tag("2.22", "a · POS", True), "Write <code>(AB + C)(B + C'D)</code> as a <b>product of sums</b> (simplest).", "ABCD",
               "(AB + C)(B + C'D)", "B(A + C)", "<p>From the SOP: AB + BC = <b>B(A + C)</b>. Each bracket (B and A + C) is a sum, so this is POS.</p>",
               lits_=3, form="pos", ref="07 §1"),
        bool_q(tag("2.22", "b · SOP", True), "Write <code>x' + x(x + y')(y + z')</code> as a <b>sum of products</b> (simplest).", "xyz",
               "x' + x(x + y')(y + z')", "x' + y + z'",
               steps([("x' + x(y + z')", "x(x + y') = x (absorption)"),
                      ("x' + y + z'", "x' + xP = x' + P")]), lits_=3, form="sop", ref="07 §1"),
        bool_q(tag("2.22", "b · POS", True), "Write <code>x' + x(x + y')(y + z')</code> as a <b>product of sums</b>.", "xyz",
               "x' + x(x + y')(y + z')", "(x' + y + z')",
               "<p>x' + y + z' is a single sum term, so it is <b>already a POS</b> (a product with one factor). It's SOP and POS at once.</p>",
               lits_=3, form="pos", ref="07 §1")]})
    return write_topic("07", "Minterms and maxterms",
                       "Mano Ch 2, canonical forms. Lists: type numbers with commas, smallest first, e.g. 1,3,6.", P)


if __name__ == "__main__":
    a, b = topic06(), topic07()
    print(f"book 06: {a} questions · book 07: {b} questions · {len(os.listdir(SVG_OUT))} svgs")
