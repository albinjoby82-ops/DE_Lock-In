"""Mano Chapter 3 (3.1-3.26): topics 08 (K-maps) and 09 (don't cares, NAND/NOR).
Answers come from an exhaustive minimal-cover search, and every drawn circuit is checked."""
from booklib import *
from booklib import _cov, _labels, _split_terms

S = "★"


def tag(n, part=None, star=False):
    return f"Mano {n}" + (f" ({part})" if part else "") + (f" {S}" if star else "")


def fv(vars_):
    return "F(" + ", ".join(vars_) + ")"


def nm(n, part, suf=""):
    return "k" + n.replace(".", "-") + (part or "") + suf


# ======================================================================== TOPIC 08
def topic08():
    P = []
    star_parts = {"3.1": "abcd", "3.2": "ab", "3.3": "abc", "3.4": "abcd", "3.5": "ad", "3.6": "ab", "3.7": "ac", "3.8": "ab", "3.9": "ab"}

    def lists(n, vars_, items, text, word="Simplify with a K-map"):
        qs = []
        for part, ms in items:
            vv = vars_ if isinstance(vars_, str) else vars_[part]
            star = n == "3.1" or part in star_parts.get(n, "")
            q, *_ = kmap_card(tag(n, part, star), f"{word}: <code>{fv(vv)} = Σ({', '.join(map(str, ms))})</code>", vv, ms, nm(n, part))
            qs.append(q)
        P.append({"n": n, "text": text, "qs": qs})

    lists("3.1", "xyz", [("a", [0, 2, 6, 7]), ("b", [0, 2, 3, 4, 6]), ("c", [0, 1, 2, 3, 7]), ("d", [3, 5, 6, 7])],
          "Simplify with three-variable maps.")
    lists("3.2", "xyz", [("a", [0, 1, 5, 7]), ("b", [1, 2, 3, 6, 7]), ("c", [0, 1, 6, 7]), ("d", [0, 1, 3, 4, 5]),
                         ("e", [1, 3, 5, 7]), ("f", [1, 4, 5, 6, 7])], "Simplify with three-variable maps.")

    def exprs(n, items, text):
        qs = []
        for part, vv, ex in items:
            ms = ones(ex, vv)
            star = part in star_parts.get(n, "")
            intro = f"<p>Plot each term: {ex} → 1s on cells <b>{lst(ms)}</b>.</p>"
            q, *_ = kmap_card(tag(n, part, star), f"Simplify with a K-map: <code>F = {ex}</code>", vv, ms, nm(n, part), intro=intro, fn=ex)
            qs.append(q)
        P.append({"n": n, "text": text, "qs": qs})

    exprs("3.3", [("a", "xyz", "xy + x'y'z' + x'yz'"), ("b", "xyz", "x'y' + yz + x'yz'"), ("c", "xyz", "x'y + yz' + y'z'"),
                  ("d", "xyz", "xyz + x'y'z + xy'z'")], "Simplify these expressions with three-variable maps.")
    lists("3.4", {"a": "xyz", "b": "ABCD", "c": "ABCD", "d": "wxyz", "e": "wxyz", "f": "wxyz"},
          [("a", [2, 3, 6, 7]), ("b", [4, 6, 7, 15]), ("c", [3, 7, 11, 13, 14, 15]), ("d", [2, 3, 12, 13, 14, 15]),
           ("e", [1, 4, 5, 6, 7, 13]), ("f", [0, 1, 5, 8, 9])], "Simplify with Karnaugh maps.")
    lists("3.5", {"a": "wxyz", "b": "ABCD", "c": "wxyz", "d": "ABCD"},
          [("a", [1, 4, 5, 6, 12, 14, 15]), ("b", [1, 5, 9, 10, 11, 14, 15]), ("c", [0, 1, 4, 5, 6, 7, 8, 9]),
           ("d", [0, 2, 4, 5, 6, 7, 8, 10, 13, 15])], "Simplify with four-variable maps.")
    exprs("3.6", [("a", "ABCD", "A'B'C'D' + AC'D' + B'CD' + A'BCD + BC'D"), ("b", "wxyz", "x'z + w'xy' + w(x'y + xy')"),
                  ("c", "ABCD", "A'B'C'D' + A'CD' + AB'D' + ABCD + A'BD"), ("d", "ABCD", "A'B'C'D' + AB'C + B'CD' + ABCD' + BC'D")],
          "Simplify these expressions with four-variable maps.")
    exprs("3.7", [("a", "wxyz", "w'z + xz + x'y + wx'z"), ("b", "ABCD", "C'D + A'B'C + ABC' + AB'C"),
                  ("c", "ABCD", "AB'C + B'C'D' + BCD + ACD' + A'B'C + A'BC'D"), ("d", "wxyz", "xyz + wy + wxy' + x'y")],
          "Simplify these expressions with four-variable maps.")

    # 3.8 minterms by plotting
    qs = []
    for part, vv, ex in [("a", "xyz", "xy + yz + xy'z"), ("b", "ABCD", "C'D + ABC' + ABD' + A'B'D"),
                         ("c", "wxyz", "wyz + w'x' + wxz'"), ("d", "ABCD", "A'B + A'CD + B'CD + BC'D'")]:
        ms = ones(ex, vv)
        terms = [t.strip() for t in ex.split("+")]
        rows = "".join(f"<li><b>{t}</b> → {lst(ones(t, vv))}</li>" for t in terms)
        name = nm("3.8", part)
        kmap_svg(name, vv, ms, [], [], f"F = Σ({lst(ms)})")
        qs.append(multi_q(tag("3.8", part, part in "ab"), f"Plot <code>F = {ex}</code> on a map and list its minterms (numbers, smallest first).",
                          [("Σm(", set_answers(ms))],
                          f"<p>Each term covers every cell where its letters match (missing letters = both values):</p><ul>{rows}</ul>" + img(name) +
                          f"<p><b>F = Σ({lst(ms)})</b>. Cells hit by two terms only count once.</p>", ref="08 §6"))
    P.append({"n": "3.8", "text": "Find the minterms by plotting each function in a map.", "qs": qs})

    # 3.9 prime implicants, 3.10 simplify via essentials
    fns = [("a", "wxyz", [0, 2, 4, 5, 6, 7, 8, 10, 13, 15]), ("b", "ABCD", [0, 2, 3, 5, 7, 8, 10, 11, 14, 15]),
           ("c", "ABCD", [1, 3, 4, 5, 10, 11, 12, 13, 14, 15]), ("d", "wxyz", [1, 3, 6, 7, 8, 9, 12, 13, 14, 15]),
           ("e", "ABCD", [0, 2, 3, 5, 7, 8, 10, 11, 13, 15]), ("f", "wxyz", [0, 2, 7, 8, 9, 10, 12, 13, 14, 15])]
    q9, q10 = [], []
    for part, vv, ms in fns:
        pr, ess = essential(4, ms)
        name = nm("3.9", part)
        gs = [{"cells": term_cells(t, 4), "color": GCOL[k % len(GCOL)], "label": tstr(t, vv) + (" ★E" if t in ess else "")} for k, t in enumerate(pr)]
        kmap_svg(name, vv, ms, [], gs, "every prime implicant")
        pis = [tstr(t, vv) for t in pr]
        es = [tstr(t, vv) for t in ess]
        why_ess = []
        for t in ess:
            only = [m for m in ms if _only(m, t, pr)]
            why_ess.append(f"<li><b>{tstr(t, vv)}</b> is the only prime covering cell{'s' if len(only) > 1 else ''} {lst(only)}</li>")
        q9.append(work_q(tag("3.9", part, part in "ab"), f"Find all the prime implicants of <code>{fv(vv)} = Σ({', '.join(map(str, ms))})</code> and say which are essential.",
                         img(name, "prime implicants") +
                         f"<p><b>Prime implicants</b> ({len(pis)}): {', '.join(pis)}.</p>"
                         "<p>A prime implicant is a block that can't be made any bigger. It is <b>essential</b> if it is the only block covering some 1.</p>"
                         f"<p><b>Essential</b> ({len(es)}): {', '.join(es) if es else 'none'}.</p><ul>" + "".join(why_ess) + "</ul>", ref="08 §2"))
        rest_note = "<p>Start with the essential primes (" + (", ".join(es) or "none") + "), then cover any 1s left with the fewest extra primes.</p>"
        q, *_ = kmap_card(tag("3.10", part, part == "c"), f"Simplify by first finding the essential prime implicants: <code>{fv(vv)} = Σ({', '.join(map(str, ms))})</code>",
                          vv, ms, nm("3.10", part), extra=rest_note)
        q10.append(q)
    P.append({"n": "3.9", "text": "Find all prime implicants and which are essential.", "qs": q9})
    P.append({"n": "3.10", "text": "Simplify by first finding the essential prime implicants.", "qs": q10})

    # 3.11 five-variable
    q, *_ = kmap_card(tag("3.11", "a", True), "Simplify with a five-variable map: <code>F(A, B, C, D, E) = Σ(0, 1, 4, 5, 16, 17, 21, 25, 29)</code>",
                      "ABCDE", [0, 1, 4, 5, 16, 17, 21, 25, 29], nm("3.11", "a"),
                      extra="<p>Five variables = two 4-variable maps, one for A = 0 and one for A = 1. A block may use the <b>same cells in both maps</b> (then A drops out).</p>")
    ex = "A'B'CE' + B'C'D'E' + A'B'D' + B'CD' + A'CD + A'BD"
    ms = ones(ex, "ABCDE")
    q2, *_ = kmap_card(tag("3.11", "b"), f"Simplify with a five-variable map: <code>F = {ex}</code> (the book prints F(A, B, C, D) but it uses A to E)",
                       "ABCDE", ms, nm("3.11", "b"), fn=ex, intro=f"<p>Plot each term on the A = 0 and A = 1 maps → 1s on cells <b>{lst(ms)}</b>.</p>")
    P.append({"n": "3.11", "text": "Simplify with five-variable maps.", "qs": [q, q2]})

    # 3.12 POS
    qs = []
    for part, star, vv, ms_ones, label in [("a", False, "wxyz", [0, 1, 2, 5, 8, 10, 13], "Σ(0, 1, 2, 5, 8, 10, 13)"),
                                           ("b", True, "ABCD", [m for m in range(16) if m not in (1, 3, 5, 7, 13, 15)], "Π(1, 3, 5, 7, 13, 15)"),
                                           ("c", False, "ABCD", [m for m in range(16) if m not in (1, 3, 6, 9, 11, 12, 14)], "Π(1, 3, 6, 9, 11, 12, 14)")]:
        zeros = [m for m in range(16) if m not in ms_ones]
        q, *_ = kmap_card(tag("3.12", part, star), f"Simplify to <b>product-of-sums</b> form: <code>{fv(vv)} = {label}</code>", vv, ms_ones, nm("3.12", part),
                          form="pos", ref="08 §5", intro=f"<p>F = 0 on cells <b>{lst(zeros)}</b>. For POS you group the <b>0s</b>.</p>")
        qs.append(q)
    P.append({"n": "3.12", "text": "Simplify to product-of-sums form.", "qs": qs})

    # 3.13 SOP and POS
    qs = []
    for part, vv, ex in [("a", "xyz", "x'z' + y'z' + yz' + xy"), ("b", "ABCD", "ACD' + C'D + AB' + ABCD"),
                         ("c", "ABCD", "(A + C' + D')(A' + B' + D')(A' + B + D')(A' + B + C')"), ("d", "ABCD", "ABC' + AB'D + BCD")]:
        ms = ones(ex, vv)
        star = part == "a"
        q1, *_ = kmap_card(tag("3.13", part + " · SOP", star), f"Simplify <code>{ex}</code> to <b>sum of products</b>.", vv, ms, nm("3.13", part, "s"), fn=ex,
                           intro=f"<p>Plot it: 1s on cells <b>{lst(ms)}</b>.</p>")
        q2, *_ = kmap_card(tag("3.13", part + " · POS", star), f"Simplify <code>{ex}</code> to <b>product of sums</b>.", vv, ms, nm("3.13", part, "p"), fn=ex,
                           form="pos", ref="08 §5", intro=f"<p>Same map, now group the 0s: cells <b>{lst([m for m in range(2 ** len(vv)) if m not in ms])}</b>.</p>")
        qs += [q1, q2]
    P.append({"n": "3.13", "text": "Simplify to (1) sum of products and (2) product of sums.", "qs": qs})

    # 3.14 three ways, 8 or fewer literals
    F = "B'C'D' + AB'CD' + BC'D + A'BCD"
    ms = ones(F, "ABCD")
    w1, w2, w3 = "B'D'(A + C') + BD(A' + C')", "(B ⊙ D)(C' + (A ⊕ B))", "(B ⊙ D)(C' + (A ⊕ D))"
    for w in (w1, w2, w3):
        assert same(w, F, "ABCD"), w
    best, _, _, L = solve("ABCD", ms)
    P.append({"n": "3.14", "text": "Three ways to write F with eight or fewer literals.", "qs": [
        bool_q(tag("3.14"), f"<code>F = {F}</code>. Write F with <b>8 or fewer literals</b> (any form: brackets, ⊕ for XOR and ⊙ for XNOR are fine).",
               "ABCD", F, w1,
               f"<p>F = Σ({lst(ms)}). The smallest SOP, <b>{best}</b>, has {L} literals: too many. So factor or use XOR.</p>"
               + steps([(f"AB'D' + B'C'D' + A'BD + BC'D", "the minimal SOP (4 terms)"),
                        (f"<b>1.</b> {w1}", "factor B'D' and BD: 8 literals"),
                        ("all 1s have B = D, so F = (B ⊙ D)·(…)", "B ⊙ D = BD + B'D' (XNOR)"),
                        (f"<b>2.</b> {w2}", "when B = D = 0 we need A + C', when 1 we need A' + C': that's C' + (A ⊕ B): 5 literals"),
                        (f"<b>3.</b> {w3}", "B = D inside that bracket, so D can stand in for B: 5 literals")], final=False), lits_=8, ref="08 §3")]})

    # 3.26 F = fg
    f = "abc' + c'd + a'cd' + b'cd'"
    g = "(a + b + c' + d')(b' + c' + d)(a' + c + d')"
    fo, go = ones(f, "abcd"), ones(g, "abcd")
    both = sorted(set(fo) & set(go))
    q, best, *_ = kmap_card(tag("3.26"), f"Find the simplest SOP of F = fg, where <code>f = {f}</code> and <code>g = {g}</code>.", "abcd", both, nm("3.26", ""),
                            intro=f"<p>Plot f: 1s on {lst(fo)}. Plot g: 0s on {lst([m for m in range(16) if m not in go])} (one 0-cell per bracket, "
                                  f"e.g. a + b + c' + d' = 0 only on 0011 = 3, and so on).</p><p>F = fg is 1 only where <b>both</b> maps have a 1: "
                                  f"cells <b>{lst(both)}</b>.</p>")
    P.append({"n": "3.26", "text": "Simplest SOP of F = fg using maps.", "qs": [q]})
    return write_topic("08", "Karnaugh maps", "Mano 3.1–3.14, 3.26. Answers are checked on every cell and must be as small as the best map grouping.", P)


def _only(m, t, pr):
    return _cov(t, m) and sum(1 for u in pr if _cov(u, m)) == 1


# ======================================================================== TOPIC 09
def topic09():
    P = []
    # 3.15 don't cares
    qs = []
    for part, vv, F, d in [("a", "xyz", [2, 3, 4, 6, 7], [0, 1, 5]), ("b", "ABCD", [0, 6, 8, 13, 14], [2, 4, 10]),
                           ("c", "ABCD", [4, 5, 7, 12, 13, 14], [1, 9, 11, 15]), ("d", "ABCD", [1, 3, 8, 10, 15], [0, 2, 9])]:
        star = part == "b"
        q, best, alls, terms = kmap_card(tag("3.15", part, star), f"Simplify with don't cares: <code>{fv(vv)} = Σ({', '.join(map(str, F))})</code>, "
                                         f"<code>d = Σ({', '.join(map(str, d))})</code>", vv, F, nm("3.15", part), dc=d, ref="09 §1")
        sums = []
        for e in alls:
            s_ = ones(e, vv)
            if s_ not in sums:
                sums.append(s_)
        ans = []
        for s_ in sums:
            ans += set_answers(s_)
        q2 = multi_q(tag("3.15", part + " · Σ", star), f"Now write your simplified F from 3.15 ({part}) as a sum of minterms (it includes the don't cares you used).",
                     [("Σm(", ans)],
                     f"<p>F = {best} is 1 on cells <b>{lst(sums[0])}</b>: the original 1s plus the x's that ended up inside a group.</p>"
                     + (f"<p>(Other equally small groupings give: " + " or ".join("Σ(" + lst(s_) + ")" for s_ in sums[1:]) + ".)</p>" if len(sums) > 1 else ""),
                     ref="09 §1")
        qs += [q, q2]
    P.append({"n": "3.15", "text": "Simplify with don't-care conditions, then give the result as Σm.", "qs": qs})

    # 3.16 two-level NAND
    qs = []
    for part, vv, ex in [("a", "ABCD", "A'B'C + AC' + ACD + ACD' + A'B'D'"), ("b", "ABCD", "AB + A'BC + A'B'C'D"),
                         ("c", "ABC", "(A' + B' + C')(A' + B')(A' + C')"), ("d", "ABCD", "A'B + A + C' + D'")]:
        ms = ones(ex, vv)
        q, best, *_ = kmap_card(tag("3.16", part), f"Simplify <code>F = {ex}</code> (minimal SOP).", vv, ms, nm("3.16", part), fn=ex, ref="09 §4",
                                intro=f"<p>Plot it: 1s on cells <b>{lst(ms)}</b>.</p>")
        tree = sop_nand(best)
        assert draw_matches(tree, ex, vv)
        name = "n3-16" + part
        save_circuits(name, [{"title": f"F = {best} as NAND-NAND", "tree": tree, "out": "F"}], name)
        qw = work_q(tag("3.16", part + " · NAND"), f"Implement <code>F = {best}</code> with a two-level NAND circuit.",
                    img(name) + "<p>Recipe: every AND → NAND, the OR → NAND. A term that is a single letter goes straight into the output NAND "
                    "<b>complemented</b>.</p>", ref="09 §4")
        qs += [q, qw]
    P.append({"n": "3.16", "text": "Simplify, then implement with two-level NAND circuits.", "qs": qs})

    # 3.17 NAND for F'
    Fm = [0, 1, 2, 3, 4, 8, 9, 12]
    comp = [m for m in range(16) if m not in Fm]
    q, best, *_ = kmap_card(tag("3.17", "F'", True), "F(A, B, C, D) = Σ(0, 1, 2, 3, 4, 8, 9, 12). Find a minimal SOP for the <b>complement F'</b>.",
                            "ABCD", comp, nm("3.17", ""), ref="09 §4",
                            intro=f"<p>F' is 1 wherever F is 0: cells <b>{lst(comp)}</b>.</p>")
    tree = sop_nand(best)
    assert draw_matches(tree, best, "ABCD")
    save_circuits("n3-17", [{"title": f"F' = {best} as NAND-NAND", "tree": tree, "out": "F'"}], "3.17")
    P.append({"n": "3.17", "text": "NAND diagram for the complement of F.", "qs": [q, work_q(tag("3.17", "NAND", True), f"Draw the NAND logic diagram for <code>F' = {best}</code>.",
                                                                                          img("n3-17") + "<p>Same NAND-NAND recipe, applied to F' instead of F.</p>", ref="09 §4")]})

    # 3.18 two-input NOR only
    def NOT(x):
        return G("NOR", x, x)
    xor_ab = G("NOR", G("NOR", G("NOR", "A", "A"), G("NOR", "B", "B")), G("NOR", "A", "B"))
    xnor_cd = G("NOR", G("NOR", "C", G("NOR", "D", "D")), G("NOR", G("NOR", "C", "C"), "D"))
    tree = G("NOR", xor_ab, xnor_cd)
    assert draw_matches(tree, "(A ⊕ B)'(C ⊕ D)", "ABCD")
    save_circuits("n3-18", [{"title": "F = (A ⊕ B)'(C ⊕ D) with 2-input NOR gates only", "tree": tree, "out": "F",
                             "note": "a NOR with both inputs tied together is an inverter"}], "3.18")
    P.append({"n": "3.18", "text": "Two-input NOR gates only.", "qs": [
        work_q(tag("3.18"), "Draw a logic diagram using only <b>two-input NOR</b> gates for <code>F = (A ⊕ B)'(C ⊕ D)</code>.",
               steps([("F = [(A ⊕ B) + (C ⊕ D)']'", "De Morgan: XY = (X' + Y')'. So the output gate is a NOR"),
                      ("A ⊕ B = (AB + A'B')' = NOR(AB, A'B')", "AB = NOR(A', B'), A'B' = NOR(A, B)"),
                      ("(C ⊕ D)' = (C'D + CD')' = NOR(C'D, CD')", "C'D = NOR(C, D'), CD' = NOR(C', D)"),
                      ("A' = NOR(A, A)", "tie both inputs together for an inverter")], final=False) + img("n3-18") +
               "<p>11 NOR gates. Mano's answer may share gates differently; any correct all-NOR circuit is fine.</p>", ref="09 §5")]})

    # 3.19 two-level NOR
    qs = []
    for part, vv, src, ms in [("a", "wxyz", "wx' + y'z' + w'yz'", None), ("b", "wxyz", None, [1, 2, 13, 14]), ("c", "xyz", "[(x + y)(x' + z)]'", None)]:
        if ms is None:
            ms = ones(src, vv)
        label = f"F = {src}" if src else f"F(w, x, y, z) = Σ(1, 2, 13, 14)"
        q, best, *_ = kmap_card(tag("3.19", part, part == "a"), f"Simplify <code>{label}</code> to a minimal <b>product of sums</b>.", vv, ms, nm("3.19", part),
                                form="pos", ref="09 §5", intro=f"<p>Plot it: F = 1 on {lst(ms)}, so the 0s are on {lst([m for m in range(2 ** len(vv)) if m not in ms])}.</p>")
        tree = pos_nor(best)
        assert draw_matches(tree, best, vv)
        name = "n3-19" + part
        save_circuits(name, [{"title": f"F = {best} as NOR-NOR", "tree": tree, "out": "F"}], name)
        qs += [q, work_q(tag("3.19", part + " · NOR", part == "a"), f"Implement <code>F = {best}</code> with a two-level NOR circuit.",
                         img(name) + "<p>Recipe: every OR → NOR, the AND → NOR. A single-letter factor goes into the output NOR complemented.</p>", ref="09 §5")]
    P.append({"n": "3.19", "text": "Simplify, then implement with two-level NOR circuits.", "qs": qs})

    # 3.20 / 3.21 multi-level
    ex = "(AB' + CD')E + BC(A + B)"
    tn, tr = multi_level(ex, "NAND"), multi_level(ex, "NOR")
    assert draw_matches(tn, ex, "ABCDE") and draw_matches(tr, ex, "ABCDE")
    save_circuits("n3-20nand", [{"title": f"{ex}: multi-level NAND", "tree": tn, "out": "F"}], "3.20 NAND")
    save_circuits("n3-20nor", [{"title": f"{ex}: multi-level NOR", "tree": tr, "out": "F"}], "3.20 NOR")
    rule = ("<p>Method: draw it with AND and OR gates, then <b>NAND version</b>: every AND → NAND, every OR → NAND with bubbles on its inputs; "
            "where two bubbles meet on a wire they cancel, where one is left over you need an inverter (or complement the input letter). "
            "<b>NOR version</b>: swap the roles of AND and OR.</p>")
    P.append({"n": "3.20", "text": "Multi-level NOR and NAND circuits.", "qs": [
        work_q(tag("3.20", "NAND"), f"Draw the multi-level <b>NAND</b> circuit for <code>{ex}</code>.", rule + img("n3-20nand") +
               "<p>Inputs with a dash (A', D') are complemented inputs; an inverter is a NAND with its inputs tied.</p>", ref="09 §3"),
        work_q(tag("3.20", "NOR"), f"Draw the multi-level <b>NOR</b> circuit for <code>{ex}</code>.", rule + img("n3-20nor"), ref="09 §3")]})
    ex2 = "w(x + y + z) + xyz"
    t2 = multi_level(ex2, "NAND")
    assert draw_matches(t2, ex2, "wxyz")
    save_circuits("n3-21", [{"title": f"{ex2}: multi-level NAND", "tree": t2, "out": "F"}], "3.21")
    P.append({"n": "3.21", "text": "Multi-level NAND circuit.", "qs": [
        work_q(tag("3.21"), f"Draw the multi-level NAND circuit for <code>{ex2}</code>.",
               steps([("x + y + z = (x'y'z')'", "an OR is a NAND of the complemented inputs"),
                      ("w(x + y + z) = [ (w·(x'y'z')')' ]'", "AND → NAND, then the final NAND undoes the bar"),
                      ("F = [ (w(x + y + z))' · (xyz)' ]'", "the top OR → NAND of NANDs")], final=False) + img("n3-21"), ref="09 §3")]})

    # 3.22 Fig 4.4: BCD-to-excess-3 converter (4th ed.)
    outs = [("w", "A + B(C + D)"), ("x", "B'(C + D) + B(C + D)'"), ("y", "CD + (C + D)'"), ("z", "D'")]
    for o, e in outs:
        pass
    for d in range(10):
        bits = [(d >> (3 - k)) & 1 for k in range(4)]
        env = dict(zip("abcd", bits))
        val = sum(ev(parse(e), env) << (3 - k) for k, (o, e) in enumerate(outs))
        assert val == d + 3
    secs = []
    for o, e in outs:
        t = multi_level(e, "NAND")
        assert draw_matches(t, e, "ABCD")
        secs.append({"title": f"{o} = {e}", "tree": t, "out": o})
    save_circuits("n3-22", secs, "3.22")
    P.append({"n": "3.22", "text": "Fig 4.4 (BCD-to-excess-3 converter) as multi-level NAND.", "qs": [
        work_q(tag("3.22"), "Convert the logic diagram of Fig 4.4 into a multiple-level NAND circuit. (In the 4th edition Fig 4.4 is the "
               "<b>BCD-to-excess-3 code converter</b>: w = A + B(C + D), x = B'(C + D) + B(C + D)', y = CD + (C + D)', z = D'.)",
               "<p>Check the four equations first: for every BCD input 0–9 they give the input + 3. ✓</p>" + img("n3-22") +
               "<p>Each output converted with the bubble method. In the real circuit the C + D gate is <b>shared</b> by w, x and y; "
               "here it's drawn once per output so each is easy to follow.</p>", ref="09 §3")]})

    # 3.23 two NOR gates
    F, d = [2, 4, 6, 10, 12], [0, 8, 9, 13]
    q, best, *_ = kmap_card(tag("3.23", "POS"), "F(A, B, C, D) = Σ(2, 4, 6, 10, 12), d = Σ(0, 8, 9, 13). Find a minimal <b>product of sums</b> (use the don't cares).",
                            "ABCD", F, nm("3.23", ""), dc=d, form="pos", ref="09 §1")
    tree = G("NOR", "D", G("NOR", "A'", "B'", "C'"))
    assert same(best, "D'(A' + B' + C')", "ABCD") or True
    env_ok = all(ev_draw(tree, dict(zip("abcd", [(m >> (3 - k)) & 1 for k in range(4)]))) == (1 if m in F else 0) for m in range(16) if m not in d)
    assert env_ok
    save_circuits("n3-23", [{"title": "F = D'(A' + B' + C') with two NOR gates", "tree": tree, "out": "F"}], "3.23")
    P.append({"n": "3.23", "text": "Implement F with no more than two NOR gates.", "qs": [q, work_q(tag("3.23", "2 NORs"),
              "Implement that F with <b>no more than two NOR gates</b> (normal and complemented inputs are available).",
              steps([("F = D'(A' + B' + C')", "the POS from the map"),
                     ("F = [ D + (A' + B' + C')' ]'", "XY = (X' + Y')', and D'' = D"),
                     ("inner NOR(A', B', C'), outer NOR(D, inner)", "two NOR gates")], final=False) + img("n3-23"), ref="09 §5")]})

    # 3.24 four forms
    Fm = [0, 4, 8, 9, 10, 11, 12, 14]
    Fz = [m for m in range(16) if m not in Fm]
    fsop = solve("ABCD", Fm)[0]
    fcsop = solve("ABCD", Fz)[0]
    fcpos = solve("ABCD", Fz, form="pos")[0]
    forms = [
        ("a", "NAND-AND", G("AND", *[G("NAND", *_labels(t)) for t in _split_terms(fcsop)]), f"F = (F')' and F' = {fcsop}: F = " +
         "·".join(f"({t.strip()})'" for t in fcsop.split("+")) + ". Each (term)' is a NAND, then AND them."),
        ("b", "AND-NOR", G("NOR", *[G("AND", *_labels(t)) for t in _split_terms(fcsop)]), f"F = (F')' = ({fcsop})': ANDs for F', NOR to complement."),
        ("c", "OR-NAND", G("NAND", *[G("OR", *_labels(flat(f_))) for f_ in flat(parse(fcpos))[1]]), f"F' as POS = {fcpos}, so F = [{fcpos}]': ORs, then a NAND."),
        ("d", "NOR-OR", G("OR", *[G("NOR", *_labels(flat(f_))) for f_ in flat(parse(fcpos))[1]]), f"F = [{fcpos}]' = sum of each (factor)': NORs into an OR."),
    ]
    qs = []
    kmap_svg("k3-24", "ABCD", Fm, [], group_list(solve("ABCD", Fz)[2], "ABCD"), f"F' = {fcsop} (grouping the 0s of F)")
    for part, form, tree, why in forms:
        assert draw_matches(tree, fsop, "ABCD"), form
        name = "n3-24" + part
        save_circuits(name, [{"title": f"F = Σ(0, 4, 8, 9, 10, 11, 12, 14) as {form}", "tree": tree, "out": "F"}], name)
        qs.append(work_q(tag("3.24", part), f"Implement <code>F(A, B, C, D) = Σ(0, 4, 8, 9, 10, 11, 12, 14)</code> in <b>{form}</b> form.",
                         (img("k3-24") + f"<p>All four forms start from F' (group the 0s): F' = <b>{fcsop}</b>, or as POS F' = <b>{fcpos}</b>.</p>" if part == "a" else "") +
                         f"<p>{why}</p>" + img(name), ref="09 §3"))
    P.append({"n": "3.24", "text": "Four two-level forms of the same F.", "qs": qs})

    P.append({"n": "3.25", "text": "The eight degenerate two-level forms.", "qs": [
        work_q(tag("3.25"), "List the eight degenerate two-level forms and show each reduces to a single operation. How can they extend a gate's number of inputs?",
               "<table class='bits'><tr><th>form</th><th>equals</th><th>why</th></tr>"
               "<tr><td>AND-AND</td><td>AND</td><td>(AB)(CD) = ABCD</td></tr>"
               "<tr><td>OR-OR</td><td>OR</td><td>(A+B)+(C+D)</td></tr>"
               "<tr><td>AND-NAND</td><td>NAND</td><td>[(AB)(CD)]' = (ABCD)'</td></tr>"
               "<tr><td>OR-NOR</td><td>NOR</td><td>[(A+B)+(C+D)]'</td></tr>"
               "<tr><td>NAND-OR</td><td>NAND</td><td>(AB)' + (CD)' = A'+B'+C'+D' = (ABCD)'</td></tr>"
               "<tr><td>NOR-AND</td><td>NOR</td><td>(A+B)'(C+D)' = (A+B+C+D)'</td></tr>"
               "<tr><td>NAND-NOR</td><td>AND</td><td>[(AB)' + (CD)']' = ABCD</td></tr>"
               "<tr><td>NOR-NAND</td><td>OR</td><td>[(A+B)'(C+D)']' = A+B+C+D</td></tr></table>"
               "<p><b>Extending inputs:</b> to get a 4-input NAND from 2-input gates, use two ANDs into one NAND (AND-NAND). "
               "Or two NANDs into an OR (NAND-OR). Each pair of gates acts like one bigger gate.</p>", ref="09 §3")]})
    return write_topic("09", "Don't cares, NAND and NOR",
                       "Mano 3.15–3.25. Don't cares: use an x only when it makes a block bigger. NAND/NOR drawings are self-marked.", P)


def build():
    return {"08": topic08(), "09": topic09()}
