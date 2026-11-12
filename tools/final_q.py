"""Question builders for the final-exam site. Each returns a list of steps
[what, why]; all tables, maps and equations are computed from the question."""
from final_lib import *
from final_lib import S


def lits(c, names):
    nv = len(names)
    out = []
    for i in range(nv):
        bit = 1 << (nv - 1 - i)
        if c[0] & bit:
            out.append(names[i] + ("" if c[1] & bit else "'"))
    return out


# ------------------------------------------------------------ circuit -> function
def p_function(tree, out="F"):
    steps = []
    seen = []
    names_of = {"AND": "AND", "OR": "OR", "NAND": "NAND", "NOR": "NOR", "NOT": "NOT", "XOR": "XOR", "XNOR": "XNOR"}

    def walk(n):
        if isinstance(n, str):
            return
        for c in n[1:]:
            walk(c)
        if n[0] == "NOT" and isinstance(n[1], str):
            return
        if n is tree:
            return
        seen.append(n)

    walk(tree)
    why = {"AND": "AND: 1 only when all its inputs are 1, written as a product.",
           "OR": "OR: 1 when any input is 1, written as a sum.",
           "NAND": "NAND = AND, then invert. The bubble on the output is the invert.",
           "NOR": "NOR = OR, then invert. The bubble on the output is the invert.",
           "NOT": "The triangle with a bubble inverts whatever goes in."}
    for n in seen:
        steps.append([f"The {names_of[n[0]]} gate gives {M(T_tex(n))}", why.get(n[0], "")])
    steps.append([f"The last gate is {names_of[tree[0]]}. Put the pieces in:" + DD(out + " = " + T_tex(tree)),
                  "Work from the inputs towards the output. Each gate's output becomes one input of the next gate."])
    return steps


def demorgan_note(tree, names, out="F"):
    ms = T_ms(tree, names)
    c = mincover(len(names), ms)
    return f"Tidy with De Morgan if you want (not asked): {M(out + ' = ' + cover_tex(c, names))}. Same truth table."


def p_truth(tree, names, key, out="F"):
    n = len(names)
    kids = [c for c in tree[1:]] if tree[0] in ("OR", "AND") and len(tree) > 2 else []
    head = list(names) + [M(T_tex(k)) for k in kids] + [M(out)]
    rows = []
    for m in range(1 << n):
        env = {names[i]: (m >> (n - 1 - i)) & 1 for i in range(n)}
        rows.append(list(bits(m, n)) + [str(T_ev(k, env)) for k in kids] + [f"<b>{T_ev(tree, env)}</b>"])
    ms = T_ms(tree, names)
    fig_kmap(key + "-kmap", names, ms, title=f"K-map of {out}")
    steps = [
        [f"{n} inputs → {M('2^%d = %d' % (n, 1 << n))} rows. Write them in counting order 000 … 111.",
         "Counting order makes row number = minterm number. You need that for part (c)."],
        ["Add a helper column for each piece of the function, then combine them:" + table(head, rows),
         "Small columns stop slips. The final column just applies the last gate to the helper columns."],
        ["Copy each 1 into the K-map cell with the same number:" + img(key + "-kmap", "K-map"),
         f"Rows are {names[0]}, columns are {''.join(names[1:])} in the order 00, 01, 11, 10 (only one bit changes between neighbours). The small number in each cell is the row number."],
    ]
    return steps, ms


def p_minmax(ms, names, out="F"):
    n = len(names)
    zs = [m for m in range(1 << n) if m not in ms]
    v = ", ".join(names)
    return [
        [f"Sum of minterms = the rows where {out} = 1:" + "$$" + out + f"({v}) = " + sigma(ms) + "$$",
         "A minterm is 1 on exactly one row. OR together the rows you want to be 1."],
        [f"Product of maxterms = the rows where {out} = 0:" + "$$" + out + f"({v}) = " + pi(zs) + "$$",
         "A maxterm is 0 on exactly one row. AND together the rows you want to be 0. The two lists never overlap and together cover every row."],
    ]


def p_simplify(ms, names, key, dc=(), out="F"):
    n = len(names)
    c = mincover(n, ms, dc)
    fig_kmap(key + "-groups", names, ms, dc, c, title="Groups")
    desc = []
    for g in c:
        desc.append(f"cells {', '.join(map(str, sorted(g[2])))} → {M(tname(g[0], g[1], names, n))}")
    steps = [
        ["Circle the 1s in the biggest groups of 1, 2, 4 or 8:" + img(key + "-groups", "K-map groups"),
         "Bigger group = fewer letters. Groups may overlap and may wrap round the edges." + (" An x can be circled if it helps." if dc else "")],
        ["Read each group: keep only the letters that stay the same inside it.<ul>" + "".join(f"<li>{d}</li>" for d in desc) + "</ul>",
         "A letter that is 0 in half the group and 1 in the other half cancels out."],
        ["OR the groups:" + DD(out + " = " + cover_tex(c, names)), "Every 1 is now inside at least one group, so this is the simplest sum of products."],
    ]
    return steps, c


def p_nand(c, names, key, out="F"):
    terms = [lits(g, names) for g in c]
    fig_two_level(key + "-nand", terms, out, "NAND")
    sop = cover_tex(c, names)
    inner = " \\cdot ".join(("(" + "".join(t) + ")'") if len(t) > 1 else (t[0][:-1] if t[0].endswith("'") else t[0] + "'") for t in terms)
    single = [t[0] for t in terms if len(t) == 1]
    steps = [
        ["Start from the sum of products:" + DD(out + " = " + sop), "Two-level NAND always starts from SOP: AND gates into one OR gate."],
        ["Invert twice, then use De Morgan on the inner bar:" + "$$" + tex(out) + " = \\big(" + tex(inner) + "\\big)'$$",
         "Two inversions change nothing. De Morgan turns the OR into an AND of inverted terms, and \"AND then invert\" is exactly a NAND."],
        ["Draw it: one NAND per product term, then one NAND that collects them:" + img(key + "-nand", "NAND circuit"),
         "Level 1 makes each inverted term. Level 2 NANDs them together."],
    ]
    if single:
        s0 = single[0]
        flip = s0[:-1] if s0.endswith("'") else s0 + "'"
        steps.append([f"Careful with the lone letter {M(s0)}: it goes <b>straight into the last NAND as {M(flip)}</b>.",
                      f"It has no first-level NAND to invert it, so you invert it yourself. " + ("That needs a NOT gate." if not s0.endswith("'") else "The inverted form is the plain input, so no gate is needed.")])
    nots = sorted({l[0] for t in terms if len(t) > 1 for l in t if l.endswith("'")} | {s[0] for s in single if not s.endswith("'")})
    if nots:
        steps.append([f"NOT gates needed for: {', '.join(nots)}.", "The question allows NOT gates for inverted inputs. A NOT is a NAND with its inputs tied together."])
    return steps


def p_nor(ms, names, key, out="F"):
    n = len(names)
    zs = [m for m in range(1 << n) if m not in ms]
    c = mincover(n, zs)
    fig_kmap(key + "-zeros", names, ms, (), [(g[0], g[1], g[2], tname(g[0], g[1], names, n)) for g in c], title="Group the 0s")
    sums = []
    for g in c:
        ls = lits(g, names)
        sums.append([l[:-1] if l.endswith("'") else l + "'" for l in ls])
    pos = "".join("(" + " + ".join(t) + ")" if len(t) > 1 else t[0] for t in sums)
    fig_two_level(key + "-nor", sums, out, "NOR")
    return [
        ["Two-level NOR needs product of sums, so group the <b>0s</b>:" + img(key + "-zeros", "zeros"),
         "Grouping 0s gives the inverse function F'. Inverting that gives POS."],
        ["Read the groups as F':" + DD(out + "' = " + cover_tex(c, names)), "Same reading rule as for 1s."],
        ["Invert with De Morgan:" + DD(out + " = " + pos), "Each product becomes a sum with every letter flipped. The sums are ANDed."],
        ["One NOR per sum term, one NOR to collect them:" + img(key + "-nor", "NOR circuit"),
         "OR-then-AND turns into NOR-NOR the same way AND-then-OR turns into NAND-NAND."],
    ], pos


# ------------------------------------------------------------ hazards
def p_hazard(expr, names, key, out="F", expanded=None):
    n = len(names)
    ms = minterms(expr, names)
    cmin = mincover(n, ms)
    chf = mincover(n, ms, (), True)
    kmin = {(g[0], g[1]) for g in cmin}
    bridges = [g for g in chf if (g[0], g[1]) not in kmin]
    assert all((g[0], g[1]) in {(h[0], h[1]) for h in chf} for g in cmin), "hazard-free cover is not a superset"
    # adjacent pairs not sharing a group in the minimal cover
    gaps = []
    for m in ms:
        for b in range(n):
            q = m ^ (1 << b)
            if q in ms and m < q and not any(m in g[2] and q in g[2] for g in cmin):
                gaps.append((m, q, names[n - 1 - b]))
    fig_kmap(key + "-min", names, ms, (), cmin, title="Minimal groups")
    fig_kmap(key + "-safe", names, ms, (), list(cmin) + bridges, title="With bridging group" + ("s" if len(bridges) > 1 else ""))
    steps = []
    if expanded:
        steps.append(["Multiply out the brackets:" + DD(out + " = " + expanded), "You need plain product terms to fill a K-map."])
    steps += [
        ["Fill the K-map:" + "$$" + out + " = " + sigma(ms) + "$$", "Each product term fills every cell that matches its letters."],
        ["Simplify as normal:" + img(key + "-min", "minimal") + DD(out + " = " + cover_tex(cmin, names)), "This is the cheapest circuit, but it may glitch."],
    ]
    if gaps:
        g = "".join(f"<li>cells {a} and {b} (only {M(v)} changes)</li>" for a, b, v in gaps)
        steps.append(["Look for <b>neighbouring 1s that are in different groups</b>:<ul>" + g + "</ul>",
                      "Moving between those two cells, one term switches off before the other switches on. For a moment no term is 1, so the output dips to 0. That dip is the static-1 hazard."])
        steps.append(["Add a group that covers each such pair:" + img(key + "-safe", "hazard free") + "".join(f"<p>bridge: {M(tname(b[0], b[1], names, n))}</p>" for b in bridges),
                      "The bridge term stays 1 across the move and holds the output up. Use the biggest group that contains the pair."])
    else:
        steps.append(["Every pair of neighbouring 1s already shares a group.", "No jump between groups means no hazard. Nothing to add."])
    full = list(cmin) + bridges
    na = sum(1 for g in full if bin(g[0]).count("1") > 1)
    steps.append(["Hazard-free answer:" + DD(out + " = " + cover_tex(full, names)) + f"<p>{na} AND gates + 1 OR gate (plus NOT gates for inverted inputs).</p>",
                  "It is no longer the minimal SOP. The extra term is redundant in Boolean algebra but needed in real hardware."])
    return steps, cover_tex(full, names)


# ------------------------------------------------------------ JK counter
def p_counter(cycles, names, key, twomode=False):
    nb = len(names)
    r = jk_counter(cycles, names, nb)
    fig_cycles(key + "-states", cycles, nb)
    head = ["".join(names), "next"] + [M(f"J{x}") + " " + M(f"K{x}") for x in names]
    maps = []
    for x in names:
        for p in "JK":
            k = p + x
            on, dc = r["d"][k]
            maps.append((uni(k) + " = " + uni(r["eq"][k]), on, dc, r["cov"][k]))
    fig_kmaps(key + "-kmaps", names, maps, per_row=2)
    labels = [(r["eq"]["J" + x], r["eq"]["K" + x]) for x in names]
    fig_ff_row(key + "-circuit", "JK", labels, names, note="each label is the logic feeding that input · one common clock")
    nstates = len(r["nxt"])
    steps = [
        ["Draw the state diagram:" + img(key + "-states", "states"),
         ("Both loops live in <b>one</b> state table. The circuit has no mode input: whichever loop it starts in, it stays in." if twomode else "A counter has no input, so each state has exactly one arrow out.")],
        [f"{nstates} states → {nb} flip-flops ({M('2^%d = %d' % (nb, 1 << nb))}). " + ("All 8 codes are used, so <b>no don't-care states</b>." if not r["unused"] else "Unused: " + ", ".join(bits(u, nb) for u in r["unused"]) + " → don't cares."),
         "Minimum flip-flops = smallest n with 2ⁿ ≥ number of states."],
        ["Write the state table. Then for each flip-flop compare its present bit with its next bit and fill J K from the excitation table:"
         + table(["Q → Q⁺", "J K"], [["0 → 0", "0 x"], ["0 → 1", "1 x"], ["1 → 0", "x 1"], ["1 → 1", "x 0"]], "tt small")
         + table(head, r["rows"]),
         "Present bit 0: only J matters (J = next bit). Present bit 1: only K matters (K = opposite of next bit). The other input is x."],
        [f"K-map every J and K column (variables {', '.join(names)}):" + img(key + "-kmaps", "K-maps"),
         "The x's are free. Circle them whenever that makes a group bigger."],
        ["Logic functions:" + "".join(DD(f"J{x} = {r['eq']['J'+x]} \\qquad K{x} = {r['eq']['K'+x]}") for x in names),
         "Each one is read straight off its map."],
        ["Logic diagram: three JK flip-flops on one clock, with those functions on the inputs:" + img(key + "-circuit", "circuit"),
         "Synchronous = every flip-flop shares the clock, so all bits change on the same edge."],
    ]
    if r["unused"]:
        t = "".join("<li>" + " → ".join(bits(x, nb) for x in path) + (" ✓ back in the count" if ok else " ✗ never returns") + "</li>" for path, ok in r["trace"])
        steps.append(["Check the unused states with the final equations:<ul>" + t + "</ul>",
                      "You treated them as don't cares, so the K-maps decided where they go. If power-up or noise lands there, the counter must find its way back."])
    else:
        st = sorted(r["nxt"])[0]
        steps.append([f"Check one row with the equations, for example {bits(cycles[0][0], nb)} → {bits(r['nxt'][cycles[0][0]], nb)}. ✓",
                      "A quick check catches a K-map slip. The site re-ran all 8 states through these equations."])
    return steps, r


# ------------------------------------------------------------ ripple
def p_ripple(n, kind, down, key, f0=None):
    fig_ripple(key + "-circuit", n, kind, down)
    fig_ripple_wave(key + "-wave", n, down)
    tog = {"D": f"connect each flip-flop's own {M(chr(81) + chr(39))} back to its D", "T": "set T = 1", "JK": "set J = K = 1"}[kind]
    why_tog = {"D": "D = Q' means the next value is the opposite of the present one: it toggles on every clock edge it sees.",
               "T": "T = 1 means toggle on every clock edge it sees.", "JK": "JK = 11 means toggle on every clock edge it sees."}[kind]
    seq = [((0 - i) if down else i) % (1 << n) for i in range((1 << n) + 1)]
    src = "Q" if down else "Q'"
    steps = [
        [f"Make every flip-flop toggle: {tog}.", why_tog],
        [f"Clock the first flip-flop from CLK. Clock each later one from the <b>{M(src)} of the one before</b> (rising-edge flip-flops):" + img(key + "-circuit", "ripple counter"),
         ("Counting down, a bit must flip when the bit below goes 0 → 1 (a borrow). That is a rising edge on Q, so Q is the clock." if down else
          "Counting up, a bit must flip when the bit below goes 1 → 0 (a carry). That is a rising edge on Q', so Q' is the clock.")
         + f" With falling-edge flip-flops, swap: use {M('Q' + chr(39) if down else 'Q')}."],
        ["Count sequence: " + " → ".join(bits(x, n) for x in seq), "The first clock edge from 000 flips every bit when counting down, like 000 − 1 wrapping round." if down else "Plain binary counting, wrapping after the last state."],
        ["Waveforms:" + img(key + "-wave", "waveforms"), "Q₀ flips on every rising clock edge. Each later output flips on the rising edge of its own clock signal. Draw Q₀ first, then build the others from it."],
        ["Frequency divider: each stage toggles once per full cycle of its clock, so its output has <b>half</b> the frequency."
         + "$$f_{Q_0} = \\frac{f}{2},\\quad f_{Q_1} = \\frac{f}{4}" + ("" if n < 3 else ",\\quad f_{Q_2} = \\frac{f}{8}") + ("" if n < 4 else ",\\quad f_{Q_3} = \\frac{f}{16}") + "$$"
         + (f"<p>With f = {f0[0]} {f0[1]}: " + ", ".join(f"{M('Q%d' % b)} = {f0[0] / 2 ** (b + 1):g} {f0[1]}" for b in range(n)) + ".</p>" if f0 else ""),
         f"n stages divide by 2ⁿ. Take the output from the stage that gives the division you want. It works whether the counter counts up or down."],
    ]
    return steps


# ------------------------------------------------------------ asynchronous
def p_async(Y, z, inputs, key, tree=None):
    cols, tab = async_table(Y, z, inputs)
    name, bad = fig_transition(key + "-tt", cols, tab, inputs)
    ni = len(inputs)
    hd = ["y \\ " + "".join(inputs)] + [bits(c, ni) for c in cols]
    flow = []
    for y in (0, 1):
        row = ["<b>" + "ab"[y] + "</b>"]
        for i, c in enumerate(cols):
            Yv, zv = tab[y][i]
            cell = "ab"[Yv]
            if Yv == y:
                cell = f'<span class="stable">{cell}</span>'
            row.append(cell + (f" , {zv}" if zv is not None else ""))
        flow.append(row)
    i0 = 1 if len(cols) > 1 else 0
    c0 = cols[i0]
    env = {inputs[i]: (c0 >> (ni - 1 - i)) & 1 for i in range(ni)}
    a = [
        ["Name the two ends of the feedback wire: the gate output is <b>Y</b> (next state), the wire coming back in is <b>y</b> (present state). Read the circuit:" + DD("Y = " + Y) + (DD("z = " + z) if z else ""),
         "With the loop cut, the circuit is plain combinational logic with inputs " + ", ".join(inputs) + " and y."],
        [f"Make a map: rows y = 0, 1 and columns {''.join(inputs)} = " + ", ".join(bits(c, ni) for c in cols) + ". Fill each cell with Y:" + img(name, "transition table"),
         "Columns go in K-map (Gray) order so only one input changes between neighbours. Example cell y = 0, " + "".join(inputs) + f" = {bits(c0, ni)}: Y = {tab[0][i0][0]}."],
        ["Circle every cell where Y equals the row's y. Those are the <b>stable</b> states.", "Stable means the next state equals the present state, so nothing is trying to change."],
    ]
    b = [
        ["Rename the states with letters: y = 0 → <b>a</b>, y = 1 → <b>b</b>." + (" Add the output z to each cell." if z else "") + table(hd, flow, "tt flow"),
         "A flow table is the transition table with letters instead of binary codes. Boxed letter = stable."
         + (" z is worked out from the inputs and the present row." if z else "")],
    ]
    if bad:
        cs = ", ".join(bits(cols[i], ni) for i in bad)
        c = [
            ["Check each <b>column</b> for at least one stable (circled) entry.", "For a fixed input the circuit moves up and down inside one column. It can only settle if that column has a circle."],
            [f"Column{'s' if len(bad) > 1 else ''} {''.join(inputs)} = <b>{cs}</b> ha{'ve' if len(bad) > 1 else 's'} no circle. In that column y = 0 gives Y = 1 and y = 1 gives Y = 0.",
             "Each row sends the circuit to the other row, so it never rests."],
            [f"<b>Yes, there is a stability issue.</b> When {''.join(inputs)} = {cs} the circuit oscillates: y flips 0, 1, 0, 1 … for as long as the inputs stay there. Every other column has a stable state.",
             "The period is twice the delay round the feedback loop. Say which input combination causes it: that is what the marks are for."],
        ]
    else:
        c = [
            ["Check each <b>column</b> for at least one stable (circled) entry.", "For a fixed input the circuit moves up and down inside one column. It can only settle if that column has a circle."],
            ["Every column has at least one circle. <b>No stability issue.</b>", "Whatever the inputs, there is a state the circuit can rest in. With one state variable there can be no race either."],
        ]
    return a, b, c, (cols, tab, bad)
