"""Extra question builders for the study path (slides, Lectures 9 to 25).
Each returns steps [what, why]. Every table, trace and equation is computed
and checked here, not typed in."""
import math, random
from final_q import *
from final_lib import S, FIG
from svglib import Svg, INK, MUTED, COL
from final_engine import mincover, ev, tname, minterms

LET = "ABCDEFGH"
ACT = {(0, 0): "hold", (0, 1): "reset", (1, 0): "set", (1, 1): "toggle"}
EXC = {(0, 0): "0 x", (0, 1): "1 x", (1, 0): "x 1", (1, 1): "x 0"}


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def jk(j, k, q):
    return int((j and not q) or (not k and q))


# ------------------------------------------------------------ figures
def fig_wave(name, rows, edges=None, note=None, title="Waveforms"):
    n = max(len(r[1]) for r in rows)
    step = 34
    W, H = 100 + n * step / 2 + 20, 34 + len(rows) * 44 + (22 if note else 0)
    s = Svg(W, H, title)
    S.timing(s, 10, 22, rows, step=step, label_w=80, edges=edges)
    if note:
        s.text(W / 2, H - 8, note, size=12, color=MUTED)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


def fig_fsm(name, labels, edges, subs=None, title="State diagram"):
    """Nodes on a circle (4 nodes make a square: TL, TR, BR, BL). edges: {(i, j): label}."""
    n = len(labels)
    R = {2: 90, 3: 105, 4: 118, 5: 140, 6: 158}.get(n, 165)
    W, H = 2 * R + 240, 2 * R + (190 if n > 4 else 150)
    cx, cy = W / 2, H / 2
    s = Svg(W, H, title)
    a0 = -math.pi / 2 - (math.pi / n if n % 2 == 0 else 0)
    P = [(cx + R * math.cos(a0 + 2 * math.pi * i / n), cy + R * math.sin(a0 + 2 * math.pi * i / n)) for i in range(n)]
    for (i, j), lab in edges.items():
        if i == j:
            dx, dy = P[i][0] - cx, P[i][1] - cy
            side = ("right" if dx > 0 else "left") if abs(dx) > abs(dy) * 1.25 else ("bottom" if dy > 0 else "top")
            S.loop(s, P[i], lab, side=side)
        else:
            adj = abs(i - j) in (1, n - 1)
            both = (j, i) in edges
            S.edge(s, P[i], P[j], lab, bend=18 if both else (10 if adj else 0), lpos=0.5 if adj else 0.28)
    for i, l in enumerate(labels):
        S.node(s, P[i][0], P[i][1], l, subs[i] if subs else None)
    s.save(os.path.join(FIG, name + ".svg"))
    return name


# ------------------------------------------------------------ multiplexer / decoder
def p_mux(names, ms):
    nsel, d = len(names) - 1, names[-1]
    rows, data = [], []
    for i in range(1 << nsel):
        a, b = int(2 * i in ms), int(2 * i + 1 in ms)
        v = {(0, 0): "0", (0, 1): d, (1, 0): d + "'", (1, 1): "1"}[(a, b)]
        data.append(v)
        rows.append([bits(i, nsel), f"I<sub>{i}</sub>", f"m<sub>{2*i}</sub> = {a}", f"m<sub>{2*i+1}</sub> = {b}", "<b>" + v + "</b>"])
    # check: the mux really gives F
    for m in range(1 << len(names)):
        v = data[m >> 1]
        bit = m & 1
        assert {"0": 0, "1": 1, d: bit, d + "'": 1 - bit}[v] == int(m in ms)
    sel = ", ".join(names[:-1])
    steps = [
        [f"{len(names)} variables, but a {1 << nsel}-to-1 mux has only {nsel} select lines. Put {sel} on the selects. The last variable, {d}, goes to the data inputs.",
         "A mux with n selects can do a function of n + 1 variables, because each data input can be 0, 1, the last variable or its inverse."],
        [f"Each select value covers <b>two</b> rows of the truth table: {d} = 0 and {d} = 1. Compare F on that pair:"
         + table(["".join(names[:-1]), "Input", f"{d} = 0", f"{d} = 1", "Connect"], rows),
         f"0, 0 → F is 0 whatever {d} is. 1, 1 → F is 1. 0, 1 → F copies {d}. 1, 0 → F is the inverse of {d}."],
        ["Data inputs I<sub>0</sub> … I<sub>" + str((1 << nsel) - 1) + "</sub>: <b>" + ", ".join(data) + "</b>", "One NOT gate makes the inverted variable if it is needed."],
    ]
    return steps, ", ".join(data)


def p_decoder(names, outs):
    """outs: {name: minterm list}. Decoder + one OR gate per output."""
    n = len(names)
    rows = [list(bits(m, n)) + [str(int(m in ms)) for ms in outs.values()] for m in range(1 << n)]
    steps = [
        [f"Write the truth table ({n} inputs → {1 << n} rows):" + table(list(names) + list(outs), rows), "Row number = minterm number."],
        ["Read off the rows where each output is 1:" + "".join("$$" + k + "(" + ", ".join(names) + ") = " + sigma(ms) + "$$" for k, ms in outs.items()),
         "A sum of minterms is all a decoder needs."],
        [f"Put {', '.join(names)} on the inputs of a {n}-to-{1 << n} decoder. Output number i is 1 only on row i. Give each function <b>one OR gate</b> fed by its decoder outputs:"
         + ul(f"{k} = OR of decoder outputs {', '.join(map(str, ms))}" for k, ms in outs.items()),
         "Each decoder output is one minterm, so a decoder is a <b>minterm generator</b>. OR the minterms you want."],
    ]
    return steps


# ------------------------------------------------------------ latches and flip-flops
def p_latch(seq, q0, nand=False):
    q, rows = q0, []
    for s, r in seq:
        if nand:
            assert (s, r) != (0, 0)
            act = {(1, 1): "hold", (0, 1): "set", (1, 0): "reset"}[(s, r)]
        else:
            assert (s, r) != (1, 1)
            act = {(0, 0): "hold", (1, 0): "set", (0, 1): "reset"}[(s, r)]
        q = {"hold": q, "set": 1, "reset": 0}[act]
        rows.append([f"{s} {r}", act, f"<b>{q}</b>"])
    nm = "S' R'" if nand else "S R"
    steps = [
        [("NAND latch: the inputs are <b>active low</b>. 11 hold · 01 set · 10 reset · 00 not allowed." if nand else "NOR latch: 00 hold · 10 set · 01 reset · 11 not allowed."),
         ("A 0 on S' sets, a 0 on R' resets. Both at 1 means nobody is asking for anything, so it holds." if nand else "S = set to 1, R = reset to 0. Both at 0 means nobody is asking for anything, so it holds.")],
        ["Apply one input pair at a time, starting from the Q you had before:" + table([nm, "Action", "Q after"], rows),
         "Hold keeps whatever the last set or reset left behind. That is the memory."],
    ]
    return steps, ", ".join(re.sub("<.*?>", "", r[2]) for r in rows)


def p_fftrace(kind, seq, q0=0):
    q, rows = q0, []
    for v in seq:
        if kind == "JK":
            q2, act, lab = jk(v[0], v[1], q), ACT[v], f"{v[0]}{v[1]}"
        elif kind == "T":
            q2, act, lab = q ^ v, ("toggle" if v else "hold"), str(v)
        else:
            q2, act, lab = v, "copy D", str(v)
        rows.append([len(rows) + 1, lab, act, f"<b>{q2}</b>"])
        q = q2
    first = {"JK": ["Recall the four JK actions: 00 hold · 01 reset · 10 set · 11 toggle.", "J is the set input, K is the reset input. Both on = flip."],
             "T": ["T = 1 toggles, T = 0 holds.", "Q<sup>+</sup> = T ⊕ Q."],
             "D": ["A D flip-flop copies D at each edge.", "Q<sup>+</sup> = D."]}[kind]
    steps = [first, ["Apply one edge at a time, always starting from the previous Q:" + table(["Edge", kind, "Action", "Q after"], rows),
                     "A flip-flop only changes on the clock edge, and what it does depends on what it holds now."]]
    return steps, ", ".join(re.sub("<.*?>", "", r[3]) for r in rows)


def p_latch_ff(d, key):
    """D latch (enable = CLK) against a negative-edge D flip-flop, same CLK and D."""
    n = len(d)
    clk = ("0011" * n)[:n]
    ql, qf, a, b = [], [], 0, 0
    for i in range(n):
        if clk[i] == "1":
            a = int(d[i])
        if i and clk[i - 1] == "1" and clk[i] == "0":
            assert d[i - 1] == d[i], "D changes exactly on the sampling edge"
            b = int(d[i - 1])
        ql.append(str(a))
        qf.append(str(b))
    fall = [i for i in range(1, n) if clk[i - 1] == "1" and clk[i] == "0"]
    fig_wave(key + "-q", [("CLK", clk), ("D", d, "#0b5cad")])
    fig_wave(key + "-a", [("CLK", clk), ("D", d, "#0b5cad"), ("Q latch", "".join(ql), "#1a7f37"), ("Q flip-flop", "".join(qf), "#bc4c00")], edges=fall,
             note="dashed = falling clock edge")
    steps = [
        ["<b>D latch:</b> while CLK = 1 it is open, so Q copies D, including every change of D. When CLK drops it freezes.", "Level triggered: the whole time the clock is high counts."],
        ["<b>Flip-flop (negative edge):</b> Q changes only at each falling edge, to whatever D was just before it.", "Edge triggered: only one instant per clock cycle counts. Changes of D in between are ignored."],
        ["Draw both:" + img(key + "-a", "latch and flip-flop outputs"), "Where D moves while CLK = 1 the latch output moves too, and the flip-flop output does not. That is the whole difference."],
    ]
    return steps


# ------------------------------------------------------------ clocked circuits: analysis
def p_analysis(kind, ffs, z, key, xname="x", zname="z"):
    """ffs: [(state name, input expr or (J, K))] MSB first. Returns steps, table rows, nxt."""
    sv = [f[0] for f in ffs]
    nb = len(sv)
    rows, nxt, edges = [], {}, {}
    for m in range(1 << (nb + 1)):
        st, x = m >> 1, m & 1
        env = {sv[i]: (st >> (nb - 1 - i)) & 1 for i in range(nb)}
        env[xname] = x
        cells, ns = [], 0
        for i, (nm, e) in enumerate(ffs):
            q = env[nm]
            if kind == "JK":
                j, k = ev(e[0], env), ev(e[1], env)
                q2 = jk(j, k, q)
                cells.append(f"{j} {k}")
            elif kind == "T":
                t = ev(e, env)
                q2 = q ^ t
                cells.append(str(t))
            else:
                q2 = ev(e, env)
            ns = (ns << 1) | q2
        zv = ev(z, env) if z else None
        nxt[(st, x)] = (ns, zv)
        rows.append([" ".join(bits(st, nb)), x] + cells + ["<b>" + " ".join(bits(ns, nb)) + "</b>"] + ([zv] if z else []))
        lab = f"{x}/{zv}" if z else str(x)
        edges[(st, ns)] = (edges[(st, ns)] + ", " + lab) if (st, ns) in edges else lab
    fig_fsm(key + "-fsm", [bits(i, nb) for i in range(1 << nb)], edges)
    sub = lambda nm: nm[0] + "<sub>" + nm[1:] + "</sub>" if len(nm) > 1 else nm
    if kind == "JK":
        eqs = "".join(DD(f"J{nm[-1] if len(nm) > 1 else nm} = {e[0]} \\qquad K{nm[-1] if len(nm) > 1 else nm} = {e[1]}") for nm, e in ffs)
        head = [" ".join(sub(n) for n in sv), xname] + ["J K (" + sub(nm) + ")" for nm in sv] + ["next"] + ([zname] if z else [])
    elif kind == "T":
        eqs = "".join(DD(f"T{nm[-1] if len(nm) > 1 else nm} = {e}") for nm, e in ffs)
        head = [" ".join(sub(n) for n in sv), xname] + ["T (" + sub(nm) + ")" for nm in sv] + ["next"] + ([zname] if z else [])
    else:
        eqs = "".join(DD(f"{nm}^+ = D{nm[-1] if len(nm) > 1 else nm} = {e}") for nm, e in ffs)
        head = [" ".join(sub(n) for n in sv), xname, "next"] + ([zname] if z else [])
    how = {"JK": "Work out J and K for each flip-flop from the <b>present</b> state and input, then apply the JK action (00 hold · 01 reset · 10 set · 11 toggle):",
           "T": "Work out T for each flip-flop from the <b>present</b> state and input. T = 1 flips that bit, T = 0 keeps it:",
           "D": "With D flip-flops the next state <b>is</b> D, so just evaluate each D equation on every row:"}[kind]
    steps = [
        ["Read the equations off the circuit:" + eqs + (DD(f"{zname} = {z}") if z else ""), "One equation per flip-flop input, plus one for the output. Everything else comes from these."],
        [f"List every present state with {xname} = 0 and 1: {nb} flip-flops + 1 input → {M('2^%d = %d' % (nb + 1, 1 << (nb + 1)))} rows.", "The table must cover every combination, even ones the circuit may never reach."],
        [how + table(head, rows), "Never use the next state to work out the flip-flop inputs. " + (f"The output {zname} is worked out on the same row, from the present state and input." if z else "")],
        ["State diagram: one circle per state, one arrow per row, labelled " + ("input/output" if z else "with the input") + ":" + img(key + "-fsm", "state diagram"),
         f"Check the size: {nb} flip-flops → {1 << nb} circles, and 1 input → 2 arrows leaving every circle."],
    ]
    return steps, nxt


# ------------------------------------------------------------ clocked circuits: design
def det_table(pats, moore=False, order=None):
    """State = longest ending of the input that is a start of a pattern."""
    cand = {p[:k] for p in pats for k in range(len(p))} | (set(pats) if moore else set())
    states = order or sorted(cand, key=lambda s: (len(s), s))
    assert set(states) == cand
    T = {}
    for i, s in enumerate(states):
        for x in "01":
            w = s + x
            t = w
            while t not in cand:
                t = t[1:]
            z = tuple(int(w.endswith(p)) for p in pats)
            T[(i, int(x))] = (states.index(t), z)
    random.seed(11)
    for _ in range(200):  # brute-force check against the definition
        h, st = "", 0
        for _ in range(30):
            x = random.choice("01")
            st2, z = T[(st, int(x))]
            h += x
            want = tuple(int(h.endswith(p)) for p in pats)
            if moore:
                assert (states[st2] in pats) == bool(want[0])
            else:
                assert z == want, (pats, h)
            st = st2
    return states, T


def fsm_design(nb, T, kind, moore_out=None, given=None):
    """T: {(code, x): (next code, z bit or None)}. Returns eqs (text), on/dc/cover per function, rows."""
    names = [f"Q{b}" for b in reversed(range(nb))] + ["X"]
    nv = nb + 1
    used = {(k << 1) | x for (k, x) in T}
    free = [m for m in range(1 << nv) if m not in used]
    fn = {}

    def add(k, m, on, dc=False):
        fn.setdefault(k, ([], list(free)))
        if dc:
            fn[k][1].append(m)
        elif on:
            fn[k][0].append(m)

    rows = []
    for (k, x) in sorted(T):
        nk, z = T[(k, x)]
        m = (k << 1) | x
        cells = []
        for b in reversed(range(nb)):
            q, qn = (k >> b) & 1, (nk >> b) & 1
            if kind == "JK":
                add(f"J{b}", m, qn, dc=q == 1)
                add(f"K{b}", m, not qn, dc=q == 0)
                cells.append(EXC[(q, qn)])
            elif kind == "T":
                add(f"T{b}", m, q != qn)
                cells.append(str(int(q != qn)))
            else:
                add(f"D{b}", m, qn)
        if z is not None:
            add("Z", m, z)
        rows.append((k, x, nk, z, cells))
    eqs, cov = {}, {}
    for k, (on, dc) in fn.items():
        if not on:
            eqs[k], cov[k] = "0", []
        elif set(on) | set(dc) == set(range(1 << nv)):
            eqs[k], cov[k] = "1", []
        else:
            cov[k] = mincover(nv, on, dc)
            eqs[k] = cover_tex(cov[k], names)
    if moore_out is not None:  # output depends on the state only
        on = [k for k in moore_out if moore_out[k]]
        dc = [k for k in range(1 << nb) if k not in moore_out]
        eqs["Y"] = cover_tex(mincover(nb, on, dc), names[:-1])
    if given:
        eqs.update(given)

    def step(k, x):
        env = {f"Q{b}": (k >> b) & 1 for b in range(nb)}
        env["X"] = x
        nk = 0
        for b in reversed(range(nb)):
            q = env[f"Q{b}"]
            if kind == "JK":
                q2 = jk(ev(eqs[f"J{b}"], env), ev(eqs[f"K{b}"], env), q)
            elif kind == "T":
                q2 = q ^ ev(eqs[f"T{b}"], env)
            else:
                q2 = ev(eqs[f"D{b}"], env)
            nk = (nk << 1) | q2
        return nk, (ev(eqs["Z"], env) if "Z" in eqs else None)

    for (k, x), (nk, z) in T.items():  # the equations must reproduce the state table
        assert step(k, x) == (nk, z), (kind, k, x, step(k, x), nk, z)
    if moore_out is not None:
        for k, v in moore_out.items():
            assert ev(eqs["Y"], {f"Q{b}": (k >> b) & 1 for b in range(nb)}) == v
    return dict(eqs=eqs, fn=fn, cov=cov, rows=rows, names=names, step=step)


def means(s):
    return "nothing useful yet" if not s else "have " + s


def p_detector(pats, kind, key, moore=False, order=None, letters=None, design=True, given=None, sample=None):
    """Sequence detector: diagram + table, then (design=True) codes, flip-flop inputs, K-maps."""
    states, T0 = det_table(pats, moore, order)
    ns = len(states)
    L = letters or LET[:ns]
    nb = max(1, math.ceil(math.log2(ns)))
    multi = len(pats) > 1
    zs = lambda z: "".join(map(str, reversed(z))) if multi else str(z[0])  # first pattern = right-hand output bit, as on the slides
    edges = {}
    for (i, x), (j, z) in T0.items():
        lab = str(x) if moore else f"{x}/{zs(z)}"
        edges[(i, j)] = (edges[(i, j)] + ", " + lab) if (i, j) in edges else lab
    fig_fsm(key + "-fsm", list(L), edges, subs=[("out " + str(int(s in pats))) if moore else (s or "–") for s in states])
    srows = [[f"{L[i]} ({means(states[i])})", x, L[T0[(i, x)][0]]] + ([] if moore else [zs(T0[(i, x)][1])]) for i in range(ns) for x in (0, 1)]
    pat = pats[0]
    steps = [
        ["Each state remembers <b>how much of a pattern you have so far</b>:" + ul(f"{L[i]} = {means(s)}" + (" → <b>output 1</b>" if moore and s in pats else "") for i, s in enumerate(states)),
         ("Moore: the output lives inside a state, so you need one extra state that means \"the whole pattern has just arrived\"." if moore else
          "A detector only needs the useful tail of the input, never the whole history.")],
        ["Draw the arrows. First the path that follows the pattern. Then every other arrow goes to the state for the <b>longest ending of the input that is still the start of " + ("a" if multi else "the") + " pattern</b>:"
         + img(key + "-fsm", "state diagram") + table(["Present", "X", "Next"] + ([] if moore else ["Z"]), srows),
         "After a wrong bit you rarely fall all the way back to the start. After a match, the last bits may already begin the next match (overlap). Every state needs an arrow for 0 and for 1."],
    ]
    if not design:
        return steps, T0, states
    T = {(i, x): (j, None if (moore or multi) else z[0]) for (i, x), (j, z) in T0.items()}
    R = fsm_design(nb, T, kind, moore_out={i: int(s in pats) for i, s in enumerate(states)} if moore else None, given=given)
    qh = " ".join(f"Q<sub>{b}</sub>" for b in reversed(range(nb)))
    ffh = {"JK": [f"J<sub>{b}</sub> K<sub>{b}</sub>" for b in reversed(range(nb))], "T": [" ".join(f"T<sub>{b}</sub>" for b in reversed(range(nb)))], "D": []}[kind]
    trows = []
    for (k, x, nk, z, cells) in R["rows"]:
        c = cells if kind == "JK" else ([" ".join(cells)] if kind == "T" else [])
        trows.append([f"{L[k]} = " + " ".join(bits(k, nb)), x, " ".join(bits(nk, nb))] + c + ([] if z is None else [z]))
    unused = [bits(k, nb) for k in range(1 << nb) if k >= ns]
    steps.append([f"{ns} states → {nb} flip-flops. Codes in order: " + ", ".join(f"{L[i]} = {bits(i, nb)}" for i in range(ns)) + ("." if not unused else ". Unused: " + ", ".join(unused) + " → don't cares.")
                  + {"JK": " Fill in J K for every flip-flop from the excitation table (0→0: 0x · 0→1: 1x · 1→0: x1 · 1→1: x0):",
                     "T": " With T flip-flops, T = 1 exactly where that bit changes:",
                     "D": " With D flip-flops, D = next state, so the Next column <b>is</b> the D column:"}[kind]
                  + table([qh, "X", "next"] + ffh + ([] if (moore or multi) else ["Z"]), trows),
                  {"JK": "Present bit 0 → J = next bit, K = x. Present bit 1 → K = opposite of next bit, J = x.",
                   "T": "Compare each present bit with its next bit. Different → 1.", "D": "Q<sup>+</sup> = D, so there is no excitation step at all."}[kind]])
    maps = [(uni(k) + " = " + uni(R["eqs"][k]), R["fn"][k][0], R["fn"][k][1], R["cov"][k]) for k in R["fn"] if k != "Z" and not (given and k in given)]
    figs = ""
    if nb == 2 and maps:
        for i in range(0, len(maps), 2):
            fig_kmaps(f"{key}-km{i//2}", R["names"], maps[i:i + 2], per_row=2, cell=50)
            figs += img(f"{key}-km{i//2}", "K-maps")
    outk = [k for k in R["eqs"] if k in ("Z", "Y")]
    steps.append([f"K-map each column (variables {', '.join(M(n) for n in R['names'])})" + (", using the x's and the unused codes as don't cares" if kind == "JK" or unused else "") + ":" + figs
                  + "".join(DD(f"{k} = {v}") for k, v in R["eqs"].items()),
                  ("Half of every J and K column is x, which is why JK equations come out short." if kind == "JK" else
                   "The output " + ("depends on the state only (Moore)." if moore else "is 1 on a single row, so it is just that row's product term."))])
    if sample:
        st, outs = 0, []
        for ch in sample:
            st2, z = R["step"](st, int(ch))
            outs.append(str(ev(R["eqs"]["Y"], {f"Q{b}": (st2 >> b) & 1 for b in range(nb)}) if moore else z))
            st = st2
        steps.append([f"Check with the input {' '.join(sample)}: output {' '.join(outs)}.", "Run a short input through your table before you draw anything. " + ("A Moore output shows up one clock after the last bit." if moore else "The 1s must line up with the last bit of each match.")])
    ans = " · ".join(M(f"{k} = {v}") for k, v in R["eqs"].items())
    return steps, R, ans


# ------------------------------------------------------------ BCD ripple counter
def bcd_ripple():
    q1 = q2 = q4 = q8 = 0
    out = []
    for _ in range(11):
        out.append((q8, q4, q2, q1))
        o1, o2 = q1, q2
        q1 ^= 1
        if o1 == 1 and q1 == 0:  # Q1 fell: clocks Q2 and Q8
            n2 = jk(1 - q8, 1, q2)
            n8 = jk(q2 & q4, 1, q8)
            q2, q8 = n2, n8
            if o2 == 1 and q2 == 0:  # Q2 fell: clocks Q4
                q4 ^= 1
    vals = [a * 8 + b * 4 + c * 2 + d for a, b, c, d in out]
    assert vals == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], vals
    return out


# ------------------------------------------------------------ registers
def shift_rows(start, serial, right=True):
    rows, r = [["start", "–", " ".join(start)]], start
    for i, b in enumerate(serial):
        r = (b + r[:-1]) if right else (r[1:] + b)
        rows.append([i + 1, b, " ".join(r)])
    return rows, r


def johnson(k):
    r, seq = "0" * k, []
    while r not in seq:
        seq.append(r)
        r = str(1 - int(r[-1])) + r[:-1]
    assert len(seq) == 2 * k
    return seq


def johnson_decode(seq, names):
    k = len(names)
    out = []
    for s in seq:
        got = None
        for i in range(k):
            for j in range(i + 1, k):
                for a in (1, 0):
                    for b in (1, 0):
                        if [t for t in seq if int(t[i]) == a and int(t[j]) == b] == [s]:
                            cand = names[i] + ("" if a else "'") + names[j] + ("" if b else "'")
                            if got is None or (j - i == 1 and got[1] != 1) or (i == 0 and j == k - 1 and got[1] not in (1,)):
                                got = (cand, j - i)
        assert got, s
        out.append(got[0])
    return out


# ------------------------------------------------------------ asynchronous: two state variables
ROWS4 = [0, 1, 3, 2]


def async2(Y1, Y2):
    return {(y, x): (ev(Y1, {"x": x, "y1": y >> 1, "y2": y & 1}) << 1) | ev(Y2, {"x": x, "y1": y >> 1, "y2": y & 1}) for y in range(4) for x in (0, 1)}


def tt2(tab, letters=None):
    f = (lambda v: letters[v]) if letters else (lambda v: bits(v, 2))
    rows = []
    for y in ROWS4:
        rows.append(["<b>" + f(y) + "</b>"] + [(f'<span class="stable">{f(tab[(y, x)])}</span>' if tab[(y, x)] == y else f(tab[(y, x)])) if (y, x) in tab else "" for x in (0, 1)])
    return table(["y<sub>1</sub>y<sub>2</sub> \\ x", "0", "1"], rows, "tt flow")


def settle(tab, y, x):
    path = [y]
    while tab[(y, x)] != y:
        y = tab[(y, x)]
        if y in path:
            return path + [y], False
        path.append(y)
    return path, True


def race_paths(col, start=0):
    """col: {row: target} for the new input. All orders in which two bits may change."""
    ends, paths = set(), []

    def go(y, path):
        t = col[y]
        if t == y:
            ends.add(y)
            paths.append(path)
            return
        if len(path) > 6:
            ends.add(None)
            return
        diff = y ^ t
        if diff in (1, 2):
            go(t, path + [t])
        else:
            go(t, path + [t])
            go(y ^ 2, path + [y ^ 2])
            go(y ^ 1, path + [y ^ 1])

    go(start, [start])
    return paths, ends


def p_race(col, start=0):
    paths, ends = race_paths(col, start)
    tab = {(start, 0): start}
    tab.update({(y, 1): t for y, t in col.items()})
    crit = len(ends) > 1
    steps = [
        [f"Start in the stable state {bits(start, 2)} with x = 0. When x becomes 1 the circuit moves across to the x = 1 column, where the entry is <b>{bits(col[start], 2)}</b>." + tt2(tab),
         f"{bits(start, 2)} → {bits(col[start], 2)} needs <b>both</b> state variables to change. That is a race: the two feedback paths never have exactly the same delay."],
        ["List what can happen: both change together, y<sub>1</sub> first, or y<sub>2</sub> first. Follow each one down the x = 1 column until it reaches a circle:"
         + ul(" → ".join(bits(p, 2) for p in path) + " (stable)" for path in paths),
         "After the first change the circuit is in a different row, so read that row's entry to see where it goes next."],
        [("The paths end in <b>different</b> stable states (" + ", ".join(sorted(bits(e, 2) for e in ends)) + "). <b>Critical race.</b>" if crit else
          f"Every path ends in the <b>same</b> stable state, {bits(list(ends)[0], 2)}. <b>Non-critical race.</b>"),
         ("Where it ends depends on which variable happens to be faster, so the circuit is unpredictable. Fix: choose state codes so only one variable changes per transition." if crit else
          "The order does not matter, so the race is harmless.")],
    ]
    return steps, ("Critical race: can end in " + ", ".join(sorted(bits(e, 2) for e in ends))) if crit else ("Non-critical race: always ends in " + bits(list(ends)[0], 2))


def p_flow2circ(flow, key):
    """flow[row][col] = (next row, z); rows a, b; columns x1x2 = 00, 01, 11, 10."""
    names = ["x1", "x2", "y"]
    Yon, zon = [], []
    fr, tr = [], []
    for y in (0, 1):
        r1, r2 = ["<b>" + "ab"[y] + "</b>"], [f"<b>{y}</b>"]
        for ci, c in enumerate(GRAY):
            ny, z = flow[y][ci]
            m = (c << 1) | y
            if ny:
                Yon.append(m)
            if z:
                zon.append(m)
            cell = "ab"[ny]
            r1.append((f'<span class="stable">{cell}</span>' if ny == y else cell) + f" , {z}")
            r2.append(f'<span class="stable">{ny}</span>' if ny == y else str(ny))
        fr.append(r1)
        tr.append(r2)
    hd = ["", "00", "01", "11", "10"]
    cY, cz = mincover(3, Yon), (mincover(3, zon) if zon else [])
    Yt, zt = cover_tex(cY, names), cover_tex(cz, names)
    for m in range(8):
        env = {"x1": m >> 2, "x2": (m >> 1) & 1, "y": m & 1}
        assert ev(Yt, env) == int(m in Yon) and ev(zt, env) == int(m in zon)
    lit = lambda l: ("NOT", l[:-1]) if l.endswith("'") else l
    terms = [("AND",) + tuple(lit(l) for l in lits(g, names)) if len(lits(g, names)) > 1 else lit(lits(g, names)[0]) for g in cY]
    tree = ("OR",) + tuple(terms) if len(terms) > 1 else terms[0]
    draw_tree(key, tree, "Y", feedback="y", title="Logic diagram")
    q = "<p>Columns are x<sub>1</sub>x<sub>2</sub>. Each entry is next state , output z. Circled = stable.</p>" + table(["x<sub>1</sub>x<sub>2</sub>"] + hd[1:], fr, "tt flow")
    steps = [
        ["Give the states binary values: a = 0, b = 1. The flow table becomes a transition table for Y (rows y, columns x<sub>1</sub>x<sub>2</sub>):" + table(["y \\ x<sub>1</sub>x<sub>2</sub>"] + hd[1:], tr, "tt flow"),
         "A flow table is a transition table with letters. Going back to numbers gives you a map you can simplify."],
        ["That table is already a K-map of Y in the variables x<sub>1</sub>, x<sub>2</sub>, y. Group the 1s:" + DD("Y = " + Yt), "Rows are y and the columns are in K-map order, so neighbours can be grouped directly."],
        ["Do the same for the output: z is 1 only where the flow table shows 1." + DD("z = " + zt), "One K-map per output."],
        ["Draw it. The output Y is wired back in as y:" + img(key, "logic diagram"), "The feedback wire is the memory. There is no flip-flop and no clock."],
    ]
    return q, steps, M("Y = " + Yt) + " · " + M("z = " + zt)


def flip(l):
    return l[:-1] if l.endswith("'") else l + "'"


def p_hazard0(expr, names, key, out="Y"):
    """Static-0 hazard of a product-of-sums circuit."""
    n = len(names)
    ms = minterms(expr, names)
    zs = [m for m in range(1 << n) if m not in ms]
    cmin, chf = mincover(n, zs), mincover(n, zs, (), True)
    kmin = {(g[0], g[1]) for g in cmin}
    bridges = [g for g in chf if (g[0], g[1]) not in kmin]
    assert all((g[0], g[1]) in {(h[0], h[1]) for h in chf} for g in cmin)
    st = lambda g: "(" + " + ".join(flip(l) for l in lits(g, names)) + ")"
    gaps = [(m, m ^ (1 << b), names[n - 1 - b]) for m in zs for b in range(n) if (m ^ (1 << b)) in zs and m < (m ^ (1 << b)) and not any(m in g[2] and (m ^ (1 << b)) in g[2] for g in cmin)]
    fig_kmap(key + "-min", names, ms, (), [(g[0], g[1], g[2], st(g)) for g in cmin], title="Groups of 0s")
    fig_kmap(key + "-safe", names, ms, (), [(g[0], g[1], g[2], st(g)) for g in list(cmin) + bridges], title="With the bridging group")
    full = "".join(st(g) for g in list(cmin) + bridges)
    assert minterms(full, names) == ms
    steps = [
        ["A product of sums is 0 when any bracket is 0. Mark the <b>0s</b> on the K-map, one group per bracket:" + img(key + "-min", "zeros"), "Each sum term is 0 on a block of cells. Static-0 is about the 0s, so that is what you group."],
        ["Look for <b>neighbouring 0s in different groups</b>:" + ul(f"cells {a} and {b} (only {M(v)} changes)" for a, b, v in gaps),
         "Moving between them, one bracket goes to 1 before the other drops to 0. For a moment every bracket is 1, so the output pulses to 1. That pulse is the static-0 hazard."],
        ["Add a sum term that covers both cells:" + img(key + "-safe", "hazard free") + DD(out + " = " + full), "The extra bracket stays 0 across the move and holds the output down. Same cure as static-1, on the 0s instead of the 1s."],
    ]
    return steps, full
