"""Builders for design questions that start from a description in words and
end with a drawn circuit. Everything is computed and checked against the rule."""
from final_more import *


def _check_rows(expr, names, ms, dc, out):
    n = len(names)
    for m in range(1 << n):  # the simplified equation must agree with the truth table on every real row
        if m not in dc:
            assert ev(expr, {names[i]: (m >> (n - 1 - i)) & 1 for i in range(n)}) == int(m in ms), (expr, m)
    m1 = ms[len(ms) // 2]
    m0 = next(m for m in range(1 << n) if m not in ms and m not in dc)
    return (f"Check two rows against the equation. Row {m1} ({bits(m1, n)}): {out} = 1 ✓. Row {m0} ({bits(m0, n)}): {out} = 0 ✓.",
            "Put the row's 0s and 1s into the equation. If any term is 1 the output is 1. Thirty seconds here catches a wrong group.")


def p_words(key, names, ms, impl, naming, rule, dc=(), out="F", cols=(("N", lambda m: m),)):
    """Words → letters → truth table → minterm list → circuit.
    impl: "gates" (K-map, AND-OR), "nand" (K-map, NAND-NAND) or "mux" (one multiplexer)."""
    n = len(names)
    ms, dc = sorted(ms), sorted(dc)
    head = list(names) + [c[0] for c in cols] + [out]
    rows = [list(bits(m, n)) + [c[1](m) for c in cols] + ["x" if m in dc else f"<b>{int(m in ms)}</b>"] for m in range(1 << n)]
    steps = [
        [naming, "A design question gives you words. The first job is to turn them into letters: one letter for each input bit (most significant first) and a name for the output."],
        [f"Truth table: {n} inputs → {1 << n} rows in counting order. For each row, ask the question from the words: {rule}" + table(head, rows),
         "Do not think about gates yet. The truth table is the whole specification. Once it is right, the rest is routine." + (" Rows that can never happen get an x (don't care)." if dc else "")],
        ["Write it as a list of row numbers:" + "$$" + out + "(" + ", ".join(names) + ") = " + sigma(ms) + "$$" + ("$$\\text{don't cares: } d(" + ", ".join(map(str, dc)) + ")$$" if dc else ""),
         "This short form is what you carry into the next step, whether that is a K-map, a multiplexer or a decoder."],
    ]
    if impl == "mux":
        st, a = p_mux(names, ms, key, out)
        return steps + st, "Data inputs: " + a
    st, c = p_simplify(ms, names, key, dc, out)
    expr = cover_tex(c, names)
    steps += st
    if impl == "nand":
        steps += p_nand(c, names, key, out)[1:]
    else:
        fig_sop(key + "-ckt", expr, out)
        nots = sorted({l[:-1] for g in c for l in lits(g, names) if l.endswith("'")})
        steps.append(["Draw it. <b>One AND gate per product term, one OR gate to join them.</b>" + (" A term with one letter goes straight into the OR gate." if any(len(lits(g, names)) == 1 for g in c) and len(c) > 1 else "") + img(key + "-ckt", "logic diagram")
                      + (f"<p>NOT gates needed for: {', '.join(nots)}.</p>" if nots else "<p>No dashed letters, so no NOT gates.</p>"),
                      "Read the equation like a parts list. The number of terms = the number of inputs on the OR gate. The number of letters in a term = the number of inputs on its AND gate."])
    steps.append(list(_check_rows(expr, names, ms, dc, out)))
    return steps, M(out + " = " + expr)


def p_words_dec(key, names, outs, naming, rule, cols=(("N", lambda m: m),)):
    """Words → truth table with several outputs → decoder + OR gates."""
    n = len(names)
    head = list(names) + [c[0] for c in cols] + list(outs)
    rows = [list(bits(m, n)) + [c[1](m) for c in cols] + [f"<b>{int(m in v)}</b>" for v in outs.values()] for m in range(1 << n)]
    steps = [
        [naming, "Turn the words into letters first: one letter per input bit, and a name for each output."],
        [f"Truth table with one column per output. {rule}" + table(head, rows), "Each output is its own function of the same inputs. Fill one column at a time."],
    ] + p_decoder(names, outs, key)[1:]
    return steps, " · ".join("$" + k + " = " + sigma(v) + "$" for k, v in outs.items())


def p_fsm(key, kind, nb, nxt, intro, sample, zfn=None):
    """Clocked design with one input X where the states are the binary numbers themselves
    (a counter with a control input). nxt: {(state, x): next state}."""
    T = {(k, x): (v, zfn[(k, x)] if zfn else None) for (k, x), v in nxt.items()}
    ns = len({k for k, _ in nxt})
    assert {k for k, _ in nxt} == set(range(ns))
    edges = {}
    for (i, x), (j, z) in sorted(T.items()):
        lab = str(x) if z is None else f"{x}/{z}"
        edges[(i, j)] = (edges[(i, j)] + ", " + lab) if (i, j) in edges else lab
    fig_fsm(key + "-fsm", [bits(i, nb) for i in range(ns)], edges)
    R = fsm_design(nb, T, kind)
    qh = " ".join(f"Q<sub>{b}</sub>" for b in reversed(range(nb)))
    ffh = {"JK": [f"J<sub>{b}</sub> K<sub>{b}</sub>" for b in reversed(range(nb))], "T": [" ".join(f"T<sub>{b}</sub>" for b in reversed(range(nb)))], "D": []}[kind]
    trows = []
    for (k, x, nk, z, cells) in R["rows"]:
        c = cells if kind == "JK" else ([" ".join(cells)] if kind == "T" else [])
        trows.append([" ".join(bits(k, nb)), x, " ".join(bits(nk, nb))] + c + ([] if z is None else [z]))
    maps = [(uni(k) + " = " + uni(R["eqs"][k]), R["fn"][k][0], R["fn"][k][1], R["cov"][k]) for k in R["fn"]]
    figs = ""
    if nb == 2:
        for i in range(0, len(maps), 2):
            fig_kmaps(f"{key}-km{i//2}", R["names"], maps[i:i + 2], per_row=2, cell=50)
            figs += img(f"{key}-km{i//2}", "K-maps")
    st, visited, outs = 0, ["0" * nb], []
    for ch in sample:
        st, z = R["step"](st, int(ch))
        visited.append(bits(st, nb))
        outs.append(str(z))
    pn = {"JK": ("J", "K"), "D": ("D",), "T": ("T",)}[kind]
    fig_seq(key + "-ckt", kind, [(f"Q{b}", {p: R["eqs"][f"{p}{b}"] for p in pn}) for b in reversed(range(nb))],
            extra=[("Z", R["eqs"]["Z"])] if zfn else [], note="same name = same wire · X' = X through a NOT gate")
    steps = [
        [intro + img(key + "-fsm", "state diagram"), "The state is the number the counter shows, so the states are already binary codes. Every circle needs one arrow for X = 0 and one for X = 1."],
        [f"{ns} states → {nb} flip-flops. Write the state table (present state and X → next state)"
         + {"JK": ", then fill in J K for every flip-flop from the excitation table (0→0: 0x · 0→1: 1x · 1→0: x1 · 1→1: x0):",
            "T": ". With T flip-flops, T = 1 exactly where that bit changes:", "D": ". With D flip-flops, D = next state, so the next column <b>is</b> the D column:"}[kind]
         + table([qh, "X", "next"] + ffh + (["Z"] if zfn else []), trows),
         {"JK": "Present bit 0 → J = next bit, K = x. Present bit 1 → K = opposite of next bit, J = x.", "T": "Compare each present bit with its next bit. Different → 1.", "D": "Q<sup>+</sup> = D, so there is no excitation step."}[kind]],
        [f"K-map each column (variables {', '.join(M(n) for n in R['names'])}):" + figs + "".join(DD(f"{k} = {v}") for k, v in R["eqs"].items()),
         "One K-map per flip-flop input. The row order of the map is the state, the columns are X."],
        [f"Check with X = {' '.join(sample)} starting from {'0' * nb}: " + " → ".join(visited) + (f" (Z = {' '.join(outs)})" if zfn else "") + ".", "Run a few clock edges through the equations before you draw. The site ran every row."],
        [f"Build it. {nb} {kind} flip-flops on one clock, each equation drawn as gates on its input:" + img(key + "-ckt", "logic diagram"),
         "One AND gate per product term, one OR gate if there are two or more terms. Label the gate inputs with signal names instead of drawing long wires."],
    ]
    return steps, R, " · ".join(M(f"{k} = {v}") for k, v in R["eqs"].items())
