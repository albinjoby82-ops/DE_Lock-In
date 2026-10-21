"""Mano 3.28-3.33 and Chapter 4 (4.3-4.35): topics 10 (adders and design), 11 (decoders, encoders), 12 (multiplexers).
Truth tables are generated from the specification and every equation is checked against them."""
from booklib import *
from booklib import _cov
from svglib import block, Svg, Gate, wire, label_in, label_out, INK, MUTED, COL
from build_svg import mux_shape

S = "★"


def tag(n, part=None, star=False):
    return f"Mano {n}" + (f" ({part})" if part else "") + (f" {S}" if star else "")


def from_spec(nv, fn):
    """fn(m) -> value or None (don't care). Returns ones, dc."""
    o, d = [], []
    for m in range(2 ** nv):
        v = fn(m)
        if v is None:
            d.append(m)
        elif v:
            o.append(m)
    return o, d


def bitcol(nv, fn, bit, nbits):
    return [None if fn(m) is None else (fn(m) >> (nbits - 1 - bit)) & 1 for m in range(2 ** nv)]


def save_svg(s, name):
    s.save(os.path.join(SVG_OUT, name + ".svg"))
    return name


def ha_block(s, x, y, a, b, sname="S", cname="C", title="HA"):
    return block(s, x, y, 90, 90, title, left=(a, b), right=(sname, cname))


# ======================================================================== TOPIC 10
def topic10():
    P = []
    # ---- 3.28 parity
    tp = G("XNOR", G("XOR", "x", "y"), "z")
    tc = G("XNOR", G("XOR", "x", "y"), G("XOR", "z", "P"))
    assert draw_matches(tp, "(x ⊕ y ⊕ z)'", "xyz") and draw_matches(tc, "(x ⊕ y ⊕ z ⊕ P)'", "xyzP")
    save_circuits("c3-28", [{"title": "3-bit odd-parity generator", "tree": tp, "out": "P"},
                            {"title": "4-bit odd-parity checker (C = 1 means error)", "tree": tc, "out": "C"}], "3.28")
    P.append({"n": "3.28", "text": "Odd-parity generator (3 bits) and checker (4 bits).", "qs": [
        bool_q(tag("3.28", "generator"), "Odd parity: the parity bit P makes the total number of 1s in x, y, z, P <b>odd</b>. Write P.", "xyz",
               "(x ⊕ y ⊕ z)'", "(x ⊕ y ⊕ z)'",
               "<p>x ⊕ y ⊕ z = 1 when x, y, z already have an odd number of 1s. Then P must be 0. So P is the opposite: "
               "<b>P = (x ⊕ y ⊕ z)'</b> (an XOR followed by an XNOR).</p>" + ttable("xyz", {"P": tt("(x ⊕ y ⊕ z)'", "xyz")}), ref="10 §1"),
        bool_q(tag("3.28", "checker"), "The checker gets x, y, z, P. Write the error output C (C = 1 when the count of 1s is <b>even</b>, i.e. something flipped).",
               "xyzP", "(x ⊕ y ⊕ z ⊕ P)'", "(x ⊕ y ⊕ z ⊕ P)'",
               "<p>x ⊕ y ⊕ z ⊕ P = 1 for an odd count (correct). So the error output is its complement: <b>C = (x ⊕ y ⊕ z ⊕ P)'</b>.</p>" + img("c3-28"),
               ref="10 §1")]})

    # ---- 3.29 three half adders
    s = Svg(560, 330, "3.29 three half adders")
    p1 = ha_block(s, 90, 30, "A", "B", "S", "C", "HA 1")
    p2 = ha_block(s, 300, 20, "x", "y", "S", "C", "HA 2")
    p3 = ha_block(s, 300, 190, "x", "y", "S", "C", "HA 3")
    s.line([(40, p1["A"][1]), p1["A"]]); label_in(s, (40, p1["A"][1]), "A")
    s.line([(40, p1["B"][1]), p1["B"]]); label_in(s, (40, p1["B"][1]), "B")
    wire(s, p1["S"], p2["x"], midx=250)
    s.text(250, p1["S"][1] - 6, "A ⊕ B", size=12, color=MUTED, anchor="end")
    wire(s, p1["C"], p3["x"], midx=230)
    s.text(228, p3["x"][1] - 6, "AB", size=12, color=MUTED, anchor="end")
    s.line([(40, 300), (260, 300), (260, p3["y"][1]), p3["y"]]); label_in(s, (40, 300), "C")
    s.line([(260, p3["y"][1] - 0.01), (260, p2["y"][1]), p2["y"]]); s.dot(260, p3["y"][1])
    for nm_, p, txt in [("S", p2["S"], "D = A ⊕ B ⊕ C"), ("C", p2["C"], "E = (A ⊕ B)C"), ("S3", p3["S"], "F = AB ⊕ C"), ("C3", p3["C"], "G = ABC")]:
        s.line([p, (p[0] + 20, p[1])]); label_out(s, (p[0] + 20, p[1]), txt, size=13)
    save_svg(s, "b3-29")
    for e1, e2 in [("A'BC + AB'C", "(A ⊕ B)C"), ("ABC' + (A' + B')C", "(AB) ⊕ C")]:
        assert same(e1, e2, "ABC")
    P.append({"n": "3.29", "text": "Four functions from three half adders.", "qs": [
        work_q(tag("3.29"), "Implement D = A ⊕ B ⊕ C, E = A'BC + AB'C, F = ABC' + (A' + B')C, G = ABC with <b>three half adders</b>.",
               steps([("E = C(A'B + AB') = (A ⊕ B)C", "factor C"),
                      ("F = (AB)C' + (AB)'C = (AB) ⊕ C", "(A' + B') = (AB)' by De Morgan"),
                      ("HA 1 on A, B → A ⊕ B and AB", ""),
                      ("HA 2 on (A ⊕ B), C → D and E", "sum and carry"),
                      ("HA 3 on AB, C → F and G", "sum and carry")], final=False) + img("b3-29"), ref="10 §2")]})

    # ---- 3.30
    F = "AB'CD' + A'BCD' + AB'C'D + A'BC'D"
    tr = G("AND", G("XOR", "A", "B"), G("XOR", "C", "D"))
    assert draw_matches(tr, F, "ABCD")
    save_circuits("c3-30", [{"title": "F = (A ⊕ B)(C ⊕ D)", "tree": tr, "out": "F"}], "3.30")
    P.append({"n": "3.30", "text": "Implement with XOR and AND gates.", "qs": [
        bool_q(tag("3.30", star=True), f"Write <code>F = {F}</code> using XOR (⊕) and AND only.", "ABCD", F, "(A ⊕ B)(C ⊕ D)",
               steps([("CD'(AB' + A'B) + C'D(AB' + A'B)", "factor terms 1+2 and 3+4"),
                      ("(AB' + A'B)(CD' + C'D)", "factor again"),
                      ("(A ⊕ B)(C ⊕ D)", "each bracket is an XOR")]) + img("c3-30"), ref="10 §1")]})

    # ---- 3.33 timing
    sig = [("x", lambda t: 0, None), ("y", lambda t: int(t >= 0), None), ("y' (NOT)", lambda t: int(t < 4), "orange"),
           ("x' (NOT)", lambda t: 1, "orange"), ("xy' (AND)", lambda t: 0, "blue"), ("x'y (AND)", lambda t: int(t >= 8), "blue"),
           ("F (OR)", lambda t: int(t >= 18), "red")]
    save_timing_t("t3-33", sig, "XOR (AND-OR-NOT) as xy goes 00 → 01 at t = 0", 50, 1, t0=-10, px=9)
    P.append({"n": "3.33", "text": "Gate delays in the AND-OR-NOT exclusive-OR.", "qs": [
        work_q(tag("3.33"), "The XOR of Fig 3.32(a) is built as x'y + xy' with inverters (4 ns), ANDs (8 ns) and an OR (10 ns). "
               "The input goes from xy = 00 to xy = 01 at t = 0. Draw every gate output from 0 to 50 ns.",
               steps([("y rises at 0", "the input change"),
                      ("y' falls at 0 + 4 = 4 ns", "inverter delay"),
                      ("x'y rises at 0 + 8 = 8 ns", "x' was already 1; AND delay from y"),
                      ("xy' stays 0", "x = 0 holds it at 0"),
                      ("F rises at 8 + 10 = 18 ns", "OR delay after x'y")], final=False) + img("t3-33") +
               "<p>The output is right (1) from <b>18 ns</b> onwards. The longest path sets the delay.</p>", ref="10 §1")]})

    # ---- 4.4
    qa, *_ = kmap_card(tag("4.4", "a", True), "Three inputs x, y, z, one output. Output = 1 when the binary value of xyz is <b>less than 3</b>. Write F.",
                       "xyz", [0, 1, 2], "k4-4a", ref="08 §3", intro="<p>Less than 3 means rows 0, 1, 2.</p>")
    qb, *_ = kmap_card(tag("4.4", "b"), "Same, but the output = 1 when the input is an <b>odd</b> number.", "xyz", [1, 3, 5, 7], "k4-4b", ref="08 §3",
                       intro="<p>Odd rows: 1, 3, 5, 7. They all end in z = 1.</p>")
    P.append({"n": "4.4", "text": "Design circuits from a word description.", "qs": [qa, qb]})

    # ---- 4.5
    f45 = lambda m: m + 2 if m < 4 else m - 3
    outs = {k: [(f45(m) >> (2 - i)) & 1 for m in range(8)] for i, k in enumerate("ABC")}
    qs = [tt_q(tag("4.5", "table"), "Inputs xyz, outputs ABC. Inputs 0–3 → output = input + 2. Inputs 4–7 → output = input − 3. Fill the table.",
               "xyz", outs, "<p>Outputs in order: " + ", ".join(f"{m}→{f45(m)}" for m in range(8)) + ". Write each as 3 bits.</p>", ref="08 §3")]
    for k in "ABC":
        o = [m for m in range(8) if outs[k][m]]
        q, *_ = kmap_card(tag("4.5", k), f"From the table, write a minimal SOP for output <b>{k}</b>.", "xyz", o, "k4-5" + k.lower(), ref="08 §3")
        qs.append(q)
    P.append({"n": "4.5", "text": "+2 for 0–3, −3 for 4–7.", "qs": qs})

    # ---- 4.6 majority
    maj = [m for m in range(8) if bin(m).count("1") >= 2]
    q, best, *_ = kmap_card(tag("4.6", "a", True), "Three-input <b>majority</b> circuit: output 1 when more inputs are 1 than 0. Write F.", "xyz", maj, "k4-6", ref="08 §3")
    save_circuits("c4-6", [{"title": f"Majority: F = {best}", "tree": best, "out": "F"}], "4.6")
    P.append({"n": "4.6", "text": "Three-input majority circuit.", "qs": [
        tt_q(tag("4.6", "table", True), "Fill the truth table of the 3-input majority function.", "xyz", {"F": [int(m in maj) for m in range(8)]},
             "<p>1 when two or three inputs are 1: rows 3, 5, 6, 7.</p>", ref="08 §3"),
        q, work_q(tag("4.6", "diagram", True), "Draw the majority circuit.", img("c4-6") + "<p>This is also the carry-out of a full adder.</p>", ref="10 §3")]})

    # ---- 4.7 Gray to binary
    g2b = lambda g: g ^ (g >> 1) ^ (g >> 2) ^ (g >> 3)
    for g in range(16):
        b = g2b(g)
        assert b ^ (b >> 1) == g
    outs = {k: [(g2b(m) >> (3 - i)) & 1 for m in range(16)] for i, k in enumerate("wxyz")}
    eqs = {"w": "a", "x": "a ⊕ b", "y": "a ⊕ b ⊕ c", "z": "a ⊕ b ⊕ c ⊕ d"}
    for k, e in eqs.items():
        assert tt(e, "abcd") == outs[k]
    trs = [{"title": "w = a", "tree": ("in", "a"), "out": "w"}, {"title": "x = a ⊕ b", "tree": G("XOR", "a", "b"), "out": "x"},
           {"title": "y = x ⊕ c", "tree": G("XOR", G("XOR", "a", "b"), "c"), "out": "y"},
           {"title": "z = y ⊕ d", "tree": G("XOR", G("XOR", G("XOR", "a", "b"), "c"), "d"), "out": "z"}]
    save_circuits("c4-7", trs, "4.7")
    qs = [tt_q(tag("4.7", "table"), "Gray code abcd (a = MSB) → binary wxyz. Fill the table.", "abcd", outs,
               "<p>Rule: the first binary bit = the first Gray bit; each next binary bit = previous <b>binary</b> bit ⊕ next Gray bit.</p>", ref="05 §2")]
    for k in "xyz":
        qs.append(bool_q(tag("4.7", k, True), f"Write binary bit <b>{k}</b> using XOR gates (a b c d = Gray bits, a = MSB).", "abcd", eqs[k], eqs[k],
                         f"<p><b>{k} = {eqs[k]}</b>: XOR all the Gray bits from the top down to this one.</p>" + (img("c4-7") if k == "z" else ""), ref="05 §2"))
    P.append({"n": "4.7", "text": "Gray-to-binary converter with XOR gates.", "qs": qs})

    # ---- 4.8 84-2-1 to BCD
    code = {0: 0b0000, 1: 0b0111, 2: 0b0110, 3: 0b0101, 4: 0b0100, 5: 0b1011, 6: 0b1010, 7: 0b1001, 8: 0b1000, 9: 0b1111}
    inv = {v: k for k, v in code.items()}
    for d, c in code.items():
        assert sum(((c >> (3 - i)) & 1) * w for i, w in enumerate((8, 4, -2, -1))) == d
    f48 = lambda m: inv.get(m)
    qs = [tt_q(tag("4.8", "table", True), "Inputs abcd in the 8, 4, −2, −1 code, outputs wxyz in BCD. Fill the table (the 6 unused codes are don't cares; leave them 0 here).",
               "abcd", {k: [0 if f48(m) is None else (f48(m) >> (3 - i)) & 1 for m in range(16)] for i, k in enumerate("wxyz")},
               "<p>84-2-1 codes: " + ", ".join(f"{d} = {c:04b}" for d, c in code.items()) + ". Unused: 0001, 0010, 0011, 1100, 1101, 1110.</p>", ref="05 §1")]
    for i, k in enumerate("wxyz"):
        o, d = from_spec(4, lambda m, i=i: None if f48(m) is None else (f48(m) >> (3 - i)) & 1)
        q, *_ = kmap_card(tag("4.8", k, True), f"84-2-1 → BCD: minimal SOP for <b>{k}</b> (unused codes are don't cares).", "abcd", o, "k4-8" + k, dc=d, ref="09 §1")
        qs.append(q)
    P.append({"n": "4.8", "text": "8, 4, −2, −1 code to BCD converter.", "qs": qs})

    # ---- 4.9 BCD to seven segment (invalid codes blank)
    seg = {0: "abcdef", 1: "bc", 2: "abdeg", 3: "abcdg", 4: "bcfg", 5: "acdfg", 6: "acdefg", 7: "abc", 8: "abcdefg", 9: "abcdfg"}
    outs = {k: [int(m <= 9 and k in seg[m]) for m in range(16)] for k in "abcdefg"}
    qs = [tt_q(tag("4.9", "table"), "BCD (ABCD) to seven-segment decoder. Fill the table for segments a–g. 1 = lit. Inputs 10–15 must give a <b>blank</b> display (all 0).",
               "ABCD", outs, "<p>Segments: a top, b upper right, c lower right, d bottom, e lower left, f upper left, g middle. "
               "This book's display draws 6 with the top bar, 7 as a, b, c only, and 9 with the bottom bar.</p>"
               "<p>Rows 10–15 are real 0s here (blank), <b>not</b> don't cares, so the maps can't use them.</p>", ref="11 §1")]
    for k in "abcdefg":
        o = [m for m in range(16) if outs[k][m]]
        q, *_ = kmap_card(tag("4.9", k), f"BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>{k}</b>.", "ABCD", o, "k4-9" + k, ref="08 §4",
                          intro=f"<p>Segment {k} is lit for digits {lst([m for m in range(10) if outs[k][m]])}; rows 10–15 are 0.</p>")
        qs.append(q)
    P.append({"n": "4.9", "text": "BCD-to-seven-segment decoder, invalid codes blank.", "qs": qs})

    # ---- 4.10 2's complementer
    f410 = lambda m: (-m) % 16
    outs = {k: [(f410(m) >> (3 - i)) & 1 for m in range(16)] for i, k in enumerate(["y₃", "y₂", "y₁", "y₀"])}
    eqs = [("y₁", "C ⊕ D"), ("y₂", "B ⊕ (C + D)"), ("y₃", "A ⊕ (B + C + D)")]
    for k, e in eqs:
        assert tt(e, "ABCD") == outs[k], k
    assert tt("D", "ABCD") == outs["y₀"]
    save_circuits("c4-10", [{"title": "y₀ = D", "tree": ("in", "D"), "out": "y₀"}] +
                  [{"title": f"{k} = {e}", "tree": e, "out": k} for k, e in eqs], "4.10")
    qs = [tt_q(tag("4.10", "table", True), "4-bit 2's complementer: input ABCD (D = LSB), output y₃y₂y₁y₀ = 2's complement of the input. Fill the table.",
               "ABCD", outs, "<p>Each output row is 16 − input (and 0 → 0). Shortcut: copy bits from the right up to the first 1, flip the rest.</p>", ref="04 §3")]
    for k, e in eqs:
        qs.append(bool_q(tag("4.10", k, True), f"Write output <b>{k}</b> of the 2's complementer (use ⊕).", "ABCD", e, e,
                         f"<p>Bit flips if any lower bit is 1 (that's the shortcut rule): <b>{k} = {e}</b>.</p>"
                         + (img("c4-10") + "<p>5 bits: y₄ = E ⊕ (A + B + C + D), and so on: each bit is XORed with the OR of all bits below it.</p>" if k == "y₃" else ""),
                         ref="04 §3"))
    P.append({"n": "4.10", "text": "Four-bit 2's complementer with XOR gates.", "qs": qs})

    # ---- 4.11 incrementer / decrementer
    def chain(name, title, dec):
        s = Svg(820, 290 if dec else 280, title)
        pins = []
        for i in range(4):
            x = 620 - 180 * i
            p = block(s, x, 90, 100, 80, "HA", left=("C",), top=("x", "y"), bottom=("S",))
            pins.append(p)
        for i, p in enumerate(pins):
            ax, ay = p["x"]
            sub = "₀₁₂₃"[i]
            if dec:
                g = Gate(s, "NOT", ax - 70, ay - 46, 1, h=24)
                s.line([g.out, (ax, g.out[1]), (ax, ay)])
                s.line([(g.ins[0][0] - 10, g.ins[0][1]), g.ins[0]]); label_in(s, (g.ins[0][0] - 10, g.ins[0][1]), f"A{sub}", size=14)
            else:
                s.line([(ax, ay - 30), (ax, ay)]); s.text(ax, ay - 36, f"A{sub}", size=14, weight="bold")
            yx, yy = p["y"]
            if i == 0:
                s.line([(yx, yy - 30), (yx, yy)]); s.text(yx, yy - 36, "1", size=14, weight="bold")
            else:
                c = pins[i - 1]["C"]
                s.line([c, (c[0] - 10, c[1]), (c[0] - 10, yy - 12), (yx, yy - 12), (yx, yy)])
            sx, sy = p["S"]
            if dec:
                g2 = Gate(s, "NOT", sx + 10, sy + 20, 1, h=24)
                s.line([(sx, sy), (sx, g2.ins[0][1]), g2.ins[0]])
                s.line([g2.out, (g2.out[0] + 10, g2.out[1])]); label_out(s, (g2.out[0] + 10, g2.out[1]), f"D{sub}", size=14)
            else:
                s.line([(sx, sy), (sx, sy + 20)]); s.text(sx, sy + 38, f"S{sub}", size=14, weight="bold")
        c = pins[3]["C"]
        s.line([c, (c[0] - 26, c[1])]); s.text(c[0] - 32, c[1] + 5, "C₄" if not dec else "B₄", size=13, anchor="end", weight="bold")
        s.text(410, s.h - 12, "LSB on the right · each carry feeds the next stage's y input", size=12, color=MUTED)
        save_svg(s, name)
    chain("b4-11a", "4-bit incrementer from half adders", False)
    chain("b4-11b", "4-bit decrementer from half adders", True)
    for m in range(16):  # decrementer logic check: per stage d = (a' ⊕ b)', borrow = a'b
        a = [(m >> i) & 1 for i in range(4)]
        b, out = 1, 0
        for i in range(4):
            d = 1 - ((1 - a[i]) ^ b)
            b = (1 - a[i]) & b
            out |= d << i
        assert out == (m - 1) % 16
    P.append({"n": "4.11", "text": "Incrementer and decrementer from four half adders.", "qs": [
        work_q(tag("4.11", "a"), "Design a 4-bit <b>incrementer</b> (adds 1) with four half adders.",
               "<p>Adding 1 = adding a carry-in of 1 at the bottom. Each half adder adds one bit A<sub>i</sub> to the carry coming up: "
               "S<sub>i</sub> = A<sub>i</sub> ⊕ C<sub>i</sub>, C<sub>i+1</sub> = A<sub>i</sub>C<sub>i</sub>, with C₀ = 1.</p>" + img("b4-11a"), ref="10 §2"),
        work_q(tag("4.11", "b"), "Design a 4-bit <b>decrementer</b> (subtracts 1) with four half adders.",
               steps([("A − 1 = (A' + 1)'", "flip, add 1, flip back (A' + 1 = −A in 2's complement… so (A' + 1)' = A − 1)"),
                      ("so: inverters on the inputs, the incrementer, inverters on the outputs", ""),
                      ("check A = 0110 (6): A' = 1001, +1 = 1010, flip = 0101 = 5 ✓", "")], final=False) + img("b4-11b") +
               "<p>Each stage really computes a borrow: B<sub>i+1</sub> = A<sub>i</sub>'B<sub>i</sub>, which is exactly the half adder's carry when its input is A<sub>i</sub>'.</p>",
               ref="10 §2")]})

    # ---- 4.12 subtractors
    hs = {"Diff": "x ⊕ y", "B_out": "x'y"}
    fs = {"Diff": "x ⊕ y ⊕ z", "B_out": "x'y + x'z + yz"}
    for m in range(8):
        x, y, z = (m >> 2) & 1, (m >> 1) & 1, m & 1
        r = x - y - z
        assert tt(fs["Diff"], "xyz")[m] == r % 2 and tt(fs["B_out"], "xyz")[m] == int(r < 0)
    save_circuits("c4-12", [{"title": "Full subtractor: Diff = x ⊕ y ⊕ B_in", "tree": "x ⊕ y ⊕ z", "out": "Diff"},
                            {"title": "B_out = x'y + x'B_in + yB_in   (z = B_in)", "tree": "x'y + x'z + yz", "out": "B_out"}], "4.12")
    P.append({"n": "4.12", "text": "Half and full subtractors.", "qs": [
        tt_q(tag("4.12", "a"), "Half subtractor: Diff and B_out for x − y.", "xy", {"Diff": "x ⊕ y", "B_out": "x'y"},
             "<p>0 − 1 needs a borrow: Diff = 1, B_out = 1. Otherwise no borrow.</p><p><b>Diff = x ⊕ y</b>, <b>B_out = x'y</b>.</p>", ref="10 §6"),
        tt_q(tag("4.12", "b · table", True), "Full subtractor: x − y − B_in. Inputs x, y, z (z = B_in). Fill Diff and B_out.", "xyz",
             {"Diff": fs["Diff"], "B_out": fs["B_out"]}, "<p>Work out x − y − z on each row. Negative → borrow 1 (and add 2 to get Diff).</p>", ref="10 §6"),
        bool_q(tag("4.12", "b · Diff", True), "Full subtractor (z = B_in): write <b>Diff</b>.", "xyz", fs["Diff"], fs["Diff"],
               "<p>Same as the full adder's sum: 1 when an odd number of inputs are 1. <b>Diff = x ⊕ y ⊕ B_in</b>.</p>", ref="10 §6"),
        bool_q(tag("4.12", "b · B_out", True), "Full subtractor (z = B_in): write a minimal <b>B_out</b>.", "xyz", fs["B_out"], fs["B_out"],
               "<p>Borrow rows: 001, 010, 011, 111 → K-map → <b>B_out = x'y + x'z + yz</b>. (Like the adder's carry, but with x complemented.)</p>" + img("c4-12"),
               lits_=6, ref="10 §6")]})

    # ---- 4.13 adder-subtractor
    qs = []
    for part, M, A, B in [("a", 0, "0111", "0110"), ("b", 0, "1000", "1001"), ("c", 1, "1100", "1000"), ("d", 1, "0101", "1010"), ("e", 1, "0000", "0001")]:
        a, b = int(A, 2), int(B, 2)
        bb = b ^ (0b1111 if M else 0)
        tot = a + bb + M
        S_ = tot & 15
        C = tot >> 4
        c3 = ((a & 7) + (bb & 7) + M) >> 3
        V = C ^ c3
        sa = a - 16 if a & 8 else a
        sb = b - 16 if b & 8 else b
        exact = sa + sb if M == 0 else sa - sb
        assert V == int(not -8 <= exact <= 7)
        qs.append(multi_q(tag("4.13", part, True), f"Adder-subtractor: M = {M}, A = <code>{A}</code>, B = <code>{B}</code>. Give the 4 SUM bits, carry C and overflow V.",
                          [("SUM", [format(S_, "04b")]), ("C", [str(C)]), ("V", [str(V)])],
                          (f"<p>M = 0 → add: {A} + {B}" if M == 0 else f"<p>M = 1 → subtract: B is XORed with 1 (flipped) and the carry-in is 1: {A} + {format(bb, '04b')} + 1") +
                          f" = {C} {format(S_, '04b')}.</p><p>C = <b>{C}</b> (the 5th bit). V = C₄ ⊕ C₃ = {C} ⊕ {c3} = <b>{V}</b>.</p>"
                          f"<p>Signed check: {sa} {'+' if M == 0 else '−'} {sb} = {exact}" + (" → doesn't fit in −8…7, so overflow ✓" if V else " → fits ✓") + "</p>", ref="10 §6"))
    P.append({"n": "4.13", "text": "Adder-subtractor outputs: SUM, C, V.", "qs": qs})

    # ---- 4.14 / 4.15 / 4.16 / 4.17
    P.append({"n": "4.14", "text": "Propagation delay of the 4-bit carry-lookahead adder.", "qs": [
        multi_q(tag("4.14", star=True), "XOR delay 10 ns, AND or OR 5 ns. What is the total delay of the 4-bit adder of Fig 4.12 (carry lookahead)?",
                [("delay (ns)", ["30", "30ns"])],
                steps([("Pᵢ = Aᵢ ⊕ Bᵢ ready at 10 ns", "one XOR (Gᵢ = AᵢBᵢ is ready at 5 ns)"),
                       ("every carry Cᵢ = AND-OR of P, G, C₀: ready at 10 + 5 + 5 = 20 ns", "lookahead: two levels, no rippling"),
                       ("Sᵢ = Pᵢ ⊕ Cᵢ: ready at 20 + 10 = 30 ns", "one more XOR")], final=False) + "<p>Total <b>30 ns</b>, and it doesn't grow with each extra bit the way ripple carry does.</p>",
                ref="10 §5")]})
    P.append({"n": "4.15", "text": "Two-level expression for C₄.", "qs": [
        work_q(tag("4.15"), "Derive the two-level expression for the output carry C₄ of the lookahead carry generator.",
               steps([("C₁ = G₀ + P₀C₀", "carry out of stage 0"),
                      ("C₂ = G₁ + P₁C₁ = G₁ + P₁G₀ + P₁P₀C₀", "substitute C₁"),
                      ("C₃ = G₂ + P₂G₁ + P₂P₁G₀ + P₂P₁P₀C₀", "substitute C₂"),
                      ("C₄ = G₃ + P₃G₂ + P₃P₂G₁ + P₃P₂P₁G₀ + P₃P₂P₁P₀C₀", "substitute C₃: one AND per term, one OR")]) +
               "<p>Read it as: a carry comes out if stage 3 makes one, or stage 2 makes one and stage 3 passes it, … or C₀ passes through every stage.</p>", ref="10 §5")]})
    for i in range(16):
        A, B = (i >> 1) & 1, i & 1
        for C in (0, 1):
            Pp, Gg = A | B, A & B
            assert 1 - (((1 - C) & (1 - Gg)) | (1 - Pp)) == int(A + B + C >= 2)
            assert (Pp & (1 - Gg)) ^ C == (A + B + C) & 1
    P.append({"n": "4.16", "text": "Full adder with P = A + B, G = AB (IC 74283).", "qs": [
        work_q(tag("4.16"), "With Pᵢ = Aᵢ + Bᵢ and Gᵢ = AᵢBᵢ, show Cᵢ₊₁ = (Cᵢ'Gᵢ' + Pᵢ')' and Sᵢ = (PᵢGᵢ') ⊕ Cᵢ. Then identify Pᵢ' and Gᵢ' in Fig P4.16.",
               steps([("(Cᵢ'Gᵢ' + Pᵢ')' = (Cᵢ + Gᵢ)Pᵢ", "De Morgan twice"),
                      ("= PᵢCᵢ + PᵢGᵢ = PᵢCᵢ + Gᵢ", "Gᵢ = AB already means A + B = 1, so PᵢGᵢ = Gᵢ"),
                      ("= AB + (A + B)C ✓", "that is the full-adder carry"),
                      ("PᵢGᵢ' = (A + B)(A' + B') = AB' + A'B = A ⊕ B", "so Sᵢ = A ⊕ B ⊕ C ✓")], final=False) +
               "<p>In Fig P4.16: the <b>NAND</b> output (A₀B₀)' is <b>G₀'</b>, the <b>NOR</b> output (A₀ + B₀)' is <b>P₀'</b>. "
               "C₁ = NOR(P₀', G₀'C₀') = (P₀' + G₀'C₀')' and S₀ = (G₀'P₀) ⊕ C₀: exactly the two equations, so it is a full adder.</p>", ref="10 §5")]})
    # 4.17 check AOI forms
    for m in range(2 ** 7):
        bits = [(m >> k) & 1 for k in range(7)]
        G1, P1, G2, P2, G3, P3, C1 = bits
        C2 = G1 | (P1 & C1)
        C3 = G2 | (P2 & C2)
        C4 = G3 | (P3 & C3)
        n = lambda v: 1 - v
        assert C2 == n((n(G1) & n(P1)) | (n(G1) & n(C1)))
        assert C3 == n((n(G2) & n(P2)) | (n(G2) & n(G1) & n(P1)) | (n(G2) & n(G1) & n(C1)))
        assert C4 == n((n(G3) & n(P3)) | (n(G3) & n(G2) & n(P2)) | (n(G3) & n(G2) & n(G1) & n(P1)) | (n(G3) & n(G2) & n(G1) & n(C1)))
    P.append({"n": "4.17", "text": "Lookahead carries in AND-OR-INVERT form (IC 74182).", "qs": [
        work_q(tag("4.17"), "Show Cᵢ₊₁ = Gᵢ + PᵢCᵢ = (Gᵢ'Pᵢ' + Gᵢ'Cᵢ')'. Then derive C₂, C₃, C₄ in terms of G', P' and C₁'.",
               steps([("(Gᵢ'Pᵢ' + Gᵢ'Cᵢ')' = (Gᵢ'(Pᵢ' + Cᵢ'))' = Gᵢ + PᵢCᵢ ✓", "De Morgan"),
                      ("C₂ = (G₁'P₁' + G₁'C₁')'", "i = 1"),
                      ("C₂' = G₁'P₁' + G₁'C₁'", "keep the complement for the next step"),
                      ("C₃ = (G₂'P₂' + G₂'C₂')' = (G₂'P₂' + G₂'G₁'P₁' + G₂'G₁'C₁')'", "substitute C₂'"),
                      ("C₄ = (G₃'P₃' + G₃'G₂'P₂' + G₃'G₂'G₁'P₁' + G₃'G₂'G₁'C₁')'", "substitute C₃' the same way")]) +
               "<p>Each carry is one AND-OR-INVERT gate fed by the complemented G's, P's and C₁. (Checked on all 128 input combinations.)</p>", ref="10 §5")]})

    # ---- 4.18 9's complementer
    qs = []
    f418 = lambda m: (9 - m) if m <= 9 else None
    qs.append(tt_q(tag("4.18", "table", True), "BCD digit ABCD in, its 9's complement wxyz out (10–15 never happen: leave 0 here).", "ABCD",
                   {k: [0 if f418(m) is None else (f418(m) >> (3 - i)) & 1 for m in range(16)] for i, k in enumerate("wxyz")},
                   "<p>Output = 9 − input: 0 → 9 (1001), 1 → 8, … 9 → 0.</p>", ref="09 §1"))
    for i, k in enumerate("wxyz"):
        o, d = from_spec(4, lambda m, i=i: None if f418(m) is None else (f418(m) >> (3 - i)) & 1)
        q, *_ = kmap_card(tag("4.18", k, True), f"9's complementer: minimal SOP for <b>{k}</b> (10–15 are don't cares).", "ABCD", o, "k4-18" + k, dc=d, ref="09 §1")
        qs.append(q)
    P.append({"n": "4.18", "text": "9's complement of a BCD digit.", "qs": qs})

    # ---- 4.19 BCD adder-subtractor block diagram
    s = Svg(640, 300, "BCD adder-subtractor (one digit)")
    pc = block(s, 120, 120, 130, 70, "9's comp", left=("B",), right=("9−B",))
    pm = block(s, 300, 90, 110, 120, "2-to-1 MUX", left=("0", "1"), right=("Y",), bottom=("sel",))
    pa = block(s, 470, 40, 120, 170, "BCD adder", left=("A", "B", "Cin"), right=("S",), top=("Cout",))
    s.line([(40, 60), (110, 60), (110, pc["B"][1]), pc["B"]]); label_in(s, (40, 60), "B")
    s.line([(110, 60), (270, 60), (270, pm["0"][1]), pm["0"]]); s.dot(110, 60)
    wire(s, pc["9−B"], pm["1"], midx=285)
    wire(s, pm["Y"], pa["B"], midx=445)
    s.line([(40, 30), (440, 30), (440, pa["A"][1]), pa["A"]]); label_in(s, (40, 30), "A")
    s.line([(40, 270), (pm["sel"][0], 270), pm["sel"]]); label_in(s, (40, 270), "M")
    s.line([(pm["sel"][0], 270), (455, 270), (455, pa["Cin"][1]), pa["Cin"]]); s.dot(pm["sel"][0], 270)
    s.line([pa["S"], (pa["S"][0] + 14, pa["S"][1])])
    s.text(330, 290, "M = 0: A + B     M = 1: A + (9 − B) + 1 = A − B (10's complement)", size=12, color=MUTED)
    save_svg(s, "b4-19")
    P.append({"n": "4.19", "text": "BCD adder-subtractor from blocks.", "qs": [
        work_q(tag("4.19"), "Build a BCD adder-subtractor from the BCD adder and the 9's complementer of 4.18 (block diagram).",
               "<p>Subtraction in decimal = add the <b>10's complement</b> = 9's complement + 1. So: a mode bit M picks B (add) or 9 − B (subtract), "
               "and M also feeds the carry-in to supply the +1.</p>" + img("b4-19") +
               "<p>For several digits, chain them: each stage's Cout feeds the next stage's Cin, and only the lowest stage gets M as its carry-in.</p>", ref="10 §6")]})

    # ---- 4.20 multiplier
    s = Svg(760, 430, "4-bit by 4-bit multiplier")
    y = 30
    s.text(20, 22, "A = A₃A₂A₁A₀, B = B₃B₂B₁B₀", size=13, anchor="start", color=MUTED)
    ands = []
    for k in range(4):
        p = block(s, 40, 40 + k * 95, 150, 60, f"4 ANDs: A·B{'₀₁₂₃'[k]}", left=(), right=("out",))
        ands.append(p)
    prev = None
    adders = []
    for k in range(3):
        p = block(s, 300 + k * 140, 110 + k * 95, 110, 90, "4-bit adder", left=("X", "Y"), right=(), bottom=("S",), top=("Co",))
        adders.append(p)
    s.line([ands[0]["out"], (240, ands[0]["out"][1])])
    s.text(246, ands[0]["out"][1] + 5, "→ C₀ (low bit), top 3 bits ↓", size=12, anchor="start", color=MUTED)
    s.line([(240, ands[0]["out"][1]), (240, adders[0]["X"][1]), adders[0]["X"]])
    for k in range(3):
        wire(s, ands[k + 1]["out"], adders[k]["Y"], midx=adders[k]["Y"][0] - 14 if k else 270)
        if k < 2:
            s.line([adders[k]["S"], (adders[k]["S"][0], adders[k + 1]["X"][1]), adders[k + 1]["X"]])
        s.text(adders[k]["S"][0] + 6, adders[k]["S"][1] + 4, f"low bit → C{'₁₂₃'[k]}", size=12, anchor="start", color=MUTED)
    s.text(380, 415, "last adder: S = C₆…C₃, carry-out = C₇", size=13, color=MUTED)
    save_svg(s, "b4-20")
    P.append({"n": "4.20", "text": "4-bit × 4-bit multiplier from AND gates and adders.", "qs": [
        work_q(tag("4.20", "a"), "Design a multiplier for two unsigned 4-bit numbers using AND gates and binary adders.",
               "<p>Same as long multiplication: each bit Bₖ times A is 4 AND gates (a partial product). Shift each one left by k and add.</p>"
               + steps([("16 AND gates make the four partial products A·B₀ … A·B₃", "Aᵢ·Bₖ"),
                        ("C₀ = A₀B₀ straight out", "nothing to add to it"),
                        ("adder 1: (A·B₀ shifted right 1) + A·B₁ → C₁ is its low bit", "4-bit adder, carry-out joins the next sum"),
                        ("adder 2: adds A·B₂ → C₂; adder 3: adds A·B₃ → C₃…C₇", "3 adders in total")], final=False) + img("b4-20") +
               "<p>Result: 8 bits, C₇…C₀. (4 × 4 bits → up to 8 bits: 15 × 15 = 225.)</p>", ref="10 §7")]})

    # ---- 4.21 comparator
    tr = G("AND", G("XNOR", "A₃", "B₃"), G("XNOR", "A₂", "B₂"), G("XNOR", "A₁", "B₁"), G("XNOR", "A₀", "B₀"))
    save_circuits("c4-21", [{"title": "E = 1 when A = B", "tree": tr, "out": "E"}], "4.21")
    P.append({"n": "4.21", "text": "4-bit equality comparator.", "qs": [
        work_q(tag("4.21"), "Design a circuit that outputs 1 when two 4-bit numbers A and B are equal.",
               "<p>Equal means every pair of bits matches. A pair matches when xᵢ = (Aᵢ ⊙ Bᵢ) = AᵢBᵢ + Aᵢ'Bᵢ' = 1 (XNOR).</p>"
               "<p><b>E = x₃x₂x₁x₀ = (A₃ ⊙ B₃)(A₂ ⊙ B₂)(A₁ ⊙ B₁)(A₀ ⊙ B₀)</b>: four XNORs and a 4-input AND.</p>" + img("c4-21"), ref="10 §1")]})

    P.sort(key=lambda p: (int(p["n"].split(".")[0]), int(p["n"].split(".")[1])))
    return write_topic("10", "Adders and subtractors",
                       "Mano 3.28–3.30, 3.33, 4.4–4.21: parity, combinational design, adders, subtractors, comparators.", P)


# ======================================================================== TOPIC 11
def decoder_block(s, x, y, n_in, n_out, title, ins, outs_low=False, enable=None, pitch=26):
    h = max(pitch * (n_out + 1), pitch * (n_in + 2)) + 20
    w = 110
    s.rect(x, y, w, h, fill="#f6f8fa", rx=6)
    s.text(x + w / 2, y + 18, title, size=13, weight="bold")
    pins = {}
    for i, nm_ in enumerate(ins):
        py = y + 40 + i * pitch
        s.line([(x - 26, py), (x, py)])
        s.text(x + 6, py + 4, nm_, size=11, anchor="start", color=MUTED)
        pins[nm_] = (x - 26, py)
    if enable:
        py = y + h - 18
        s.line([(x - 26, py), (x, py)])
        s.text(x + 6, py + 4, enable, size=11, anchor="start", color=MUTED)
        pins["E"] = (x - 26, py)
    for i in range(n_out):
        py = y + 30 + i * (h - 40) / max(n_out - 1, 1)
        sx = x + w
        if outs_low:
            s.add(f'<circle cx="{sx + 4.5}" cy="{py}" r="4.5" fill="#fff" stroke="{INK}" stroke-width="2"/>')
            sx += 9
        s.line([(sx, py), (sx + 18, py)])
        s.text(x + w - 6, py + 4, str(i), size=11, anchor="end", color=MUTED)
        pins[i] = (sx + 18, py)
    pins["h"] = h
    return pins


def topic11():
    P = []
    # 4.22 excess-3 to binary
    f422 = lambda m: (m - 3) if 3 <= m <= 12 else None
    qs = [tt_q(tag("4.22", "table", True), "Excess-3 in (ABCD), binary out (wxyz). Valid codes are 3 to 12; the rest are don't cares (leave them 0 here).",
               "ABCD", {k: [0 if f422(m) is None else (f422(m) >> (3 - i)) & 1 for m in range(16)] for i, k in enumerate("wxyz")},
               "<p>Output = input − 3: 0011 → 0000, 0100 → 0001, … 1100 → 1001.</p>", ref="09 §1")]
    for i, k in enumerate("wxyz"):
        o, d = from_spec(4, lambda m, i=i: None if f422(m) is None else (f422(m) >> (3 - i)) & 1)
        q, *_ = kmap_card(tag("4.22", k, True), f"Excess-3 → binary: minimal SOP for <b>{k}</b> (0, 1, 2, 13, 14, 15 are don't cares).", "ABCD", o, "k4-22" + k, dc=d, ref="09 §1")
        qs.append(q)
    P.append({"n": "4.22", "text": "Excess-3-to-binary decoder with don't cares.", "qs": qs})

    # 4.23 2-to-4 decoder NOR only / NAND only
    nor_secs, nand_secs = [], []
    for i in range(4):
        a, b = (i >> 1) & 1, i & 1
        # NOR: Di = A?B?E -> NOR of the complements
        la = G("NOR", "A", "A") if a else ("in", "A")
        lb = G("NOR", "B", "B") if b else ("in", "B")
        t = G("NOR", la, lb, G("NOR", "E", "E"))
        exp = ("A" if a else "A'") + ("B" if b else "B'") + "E"
        assert draw_matches(t, exp, "ABE")
        nor_secs.append({"title": f"D{'₀₁₂₃'[i]} = {exp}", "tree": t, "out": f"D{'₀₁₂₃'[i]}"})
        na = ("in", "A") if a else G("NAND", "A", "A")
        nb = ("in", "B") if b else G("NAND", "B", "B")
        t2 = G("NAND", na, nb, "E")
        assert draw_matches(t2, f"({exp})'", "ABE")
        nand_secs.append({"title": f"D{'₀₁₂₃'[i]}' = ({exp})'  (active-low)", "tree": t2, "out": f"D{'₀₁₂₃'[i]}'"})
    save_circuits("c4-23a", nor_secs, "4.23 NOR")
    save_circuits("c4-23b", nand_secs, "4.23 NAND")
    P.append({"n": "4.23", "text": "2-to-4 decoder with enable: NOR only and NAND only.", "qs": [
        work_q(tag("4.23", "a"), "Draw a 2-to-4 line decoder with enable E using <b>NOR gates only</b>.",
               "<p>D₀ = A'B'E = (A + B + E')' → one 3-input NOR per output, fed with the <b>complements</b> of the letters it needs. "
               "A NOR with its inputs tied is the inverter.</p>" + img("c4-23a") +
               "<p>In a real circuit the three inverters (A', B', E') are drawn once and shared by all four outputs.</p>", ref="11 §3"),
        work_q(tag("4.23", "b"), "Draw a 2-to-4 line decoder with enable E using <b>NAND gates only</b>.",
               "<p>A NAND gives the minterm complemented, so the outputs are <b>active-low</b> (the selected output goes to 0), like Fig 4.19. "
               "Dᵢ' = NAND(the letters of mᵢ, E).</p>" + img("c4-23b"), ref="11 §4")]})

    # 4.24 BCD to decimal
    qs = []
    for dgt in range(10):
        q, best, *_ = kmap_card(tag("4.24", f"D{dgt}"), f"BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D{dgt}</b>.",
                                "ABCD", [dgt], f"k4-24d{dgt}", dc=list(range(10, 16)), ref="11 §1")
        qs.append(q)
    P.append({"n": "4.24", "text": "BCD-to-decimal decoder using don't cares.", "qs": qs})

    # 4.25 5-to-32 from 2-to-4 + four 3-to-8
    s = Svg(700, 640, "5-to-32 decoder")
    pd = decoder_block(s, 90, 220, 2, 4, "2-to-4", ["A₄", "A₃"], enable="E")
    for k, nm_ in enumerate(["A₄", "A₃"]):
        s.line([(40, pd[nm_][1]), pd[nm_]]); label_in(s, (40, pd[nm_][1]), nm_)
    s.line([(40, pd["E"][1]), pd["E"]]); label_in(s, (40, pd["E"][1]), "E")
    s.line([(330, 20), (330, 620)], COL["blue"][0], 3)
    s.text(330, 14, "A₂ A₁ A₀ (bus to all four)", size=12, color=COL["blue"][0])
    for k in range(4):
        y = 20 + k * 155
        p = decoder_block(s, 400, y, 3, 8, "3-to-8", ["A₂", "A₁", "A₀"], enable="E", pitch=15)
        for nm_ in ["A₂", "A₁", "A₀"]:
            s.line([(330, p[nm_][1]), p[nm_]]); s.dot(330, p[nm_][1], color=COL["blue"][0])
        wire(s, pd[k], p["E"], midx=250 + 18 * k)
        s.text(p[7][0] + 6, (p[0][1] + p[7][1]) / 2 + 5, f"D{8 * k}–D{8 * k + 7}", size=14, anchor="start", weight="bold")
    save_svg(s, "b4-25")
    P.append({"n": "4.25", "text": "5-to-32 decoder from four 3-to-8 and one 2-to-4.", "qs": [
        work_q(tag("4.25"), "Build a 5-to-32 line decoder from four 3-to-8 decoders with enable and one 2-to-4 decoder (block diagram).",
               "<p>The top two bits A₄A₃ pick <b>which</b> 3-to-8 decoder is on (they drive the 2-to-4, whose outputs are the four enables). "
               "The low three bits A₂A₁A₀ go to all four 3-to-8s and pick the line inside the chosen one.</p>" + img("b4-25"), ref="11 §3")]})

    # 4.26 4-to-16 from five 2-to-4
    s = Svg(660, 640, "4-to-16 decoder")
    pd = decoder_block(s, 90, 230, 2, 4, "2-to-4", ["A₃", "A₂"], enable="E")
    for nm_ in ["A₃", "A₂"]:
        s.line([(40, pd[nm_][1]), pd[nm_]]); label_in(s, (40, pd[nm_][1]), nm_)
    s.line([(40, pd["E"][1]), pd["E"]]); label_in(s, (40, pd["E"][1]), "E")
    s.line([(330, 20), (330, 620)], COL["blue"][0], 3)
    s.text(330, 14, "A₁ A₀ (to all four)", size=12, color=COL["blue"][0])
    for k in range(4):
        y = 20 + k * 155
        p = decoder_block(s, 400, y, 2, 4, "2-to-4", ["A₁", "A₀"], enable="E", pitch=24)
        for nm_ in ["A₁", "A₀"]:
            s.line([(330, p[nm_][1]), p[nm_]]); s.dot(330, p[nm_][1], color=COL["blue"][0])
        wire(s, pd[k], p["E"], midx=250 + 18 * k)
        s.text(p[3][0] + 6, (p[0][1] + p[3][1]) / 2 + 5, f"D{4 * k}–D{4 * k + 3}", size=14, anchor="start", weight="bold")
    save_svg(s, "b4-26")
    P.append({"n": "4.26", "text": "4-to-16 decoder from five 2-to-4 decoders.", "qs": [
        work_q(tag("4.26"), "Build a 4-to-16 line decoder from five 2-to-4 decoders with enable.",
               "<p>Same tree idea: one 2-to-4 on the top bits A₃A₂ enables one of four 2-to-4s, which decode A₁A₀.</p>" + img("b4-26"), ref="11 §3")]})

    # 4.27 NAND decoder + gates
    F = {"F₁": [3, 5, 6], "F₂": [1, 4], "F₃": [2, 3, 5, 6, 7]}
    s = Svg(620, 330, "4.27")
    p = decoder_block(s, 120, 20, 3, 8, "3-to-8 (NAND)", ["A", "B", "C"], outs_low=True, pitch=26)
    for nm_ in ["A", "B", "C"]:
        s.line([(70, p[nm_][1]), p[nm_]]); label_in(s, (70, p[nm_][1]), nm_)
    gates = [("F₁", "NAND", [3, 5, 6], 40), ("F₂", "NAND", [1, 4], 140), ("F₃", "AND", [0, 1, 4], 220)]
    for gi, (nm_, kind, ins, gy) in enumerate(gates):
        g = Gate(s, kind, 420, gy, len(ins))
        for j, (m, pin) in enumerate(zip(ins, g.ins)):
            wire(s, p[m], pin, midx=300 + 12 * (gi * 3 + j))
        s.line([g.out, (g.out[0] + 26, g.out[1])]); label_out(s, (g.out[0] + 26, g.out[1]), nm_)
    save_svg(s, "b4-27")
    for m in range(8):
        dl = [0 if k == m else 1 for k in range(8)]  # active-low outputs
        f1 = 1 - (dl[3] & dl[5] & dl[6])
        f2 = 1 - (dl[1] & dl[4])
        f3 = dl[0] & dl[1] & dl[4]
        assert (f1, f2, f3) == (int(m in F["F₁"]), int(m in F["F₂"]), int(m in F["F₃"]))
    P.append({"n": "4.27", "text": "Three functions from a NAND decoder with NAND/AND gates.", "qs": [
        work_q(tag("4.27"), "F₁ = Σ(3, 5, 6), F₂ = Σ(1, 4), F₃ = Σ(2, 3, 5, 6, 7). Use a decoder built from NAND gates (active-low outputs) "
               "plus NAND or AND gates, with as few gate inputs as possible.",
               "<p>Active-low outputs: the selected line is 0. A <b>NAND</b> of active-low lines = OR of the minterms (De Morgan).</p>"
               "<p>F₁: NAND of lines 3, 5, 6 (3 inputs). F₂: NAND of 1, 4 (2 inputs). "
               "F₃ has 5 minterms, so use its 0s instead: F₃' = Σ(0, 1, 4), and F₃ = <b>AND</b> of active-low lines 0, 1, 4 (3 inputs, not 5).</p>"
               + img("b4-27"), ref="11 §4")]})

    # 4.28 decoder + gates
    qs = []
    for part, fns in [("a", {"F₁": "x'y'z' + xz", "F₂": "xy'z' + x'y", "F₃": "x'y'z + xy"}),
                      ("b", {"F₁": "(y' + x)z", "F₂": "y'z' + xy' + yz'", "F₃": "(x' + y)z"})]:
        fields, rows = [], []
        for k, e in fns.items():
            o = ones(e, "xyz")
            fields.append((k + " = Σm(", set_answers(o)))
            gate = f"OR of decoder outputs {lst(o)}" if len(o) <= 4 else f"NOR of outputs {lst([m for m in range(8) if m not in o])} (its 0s: fewer inputs)"
            rows.append(f"<li><b>{k} = {e}</b> = Σ({lst(o)}) → {gate}</li>")
        qs.append(multi_q(tag("4.28", part), "With a 3-to-8 decoder (inputs x, y, z) and OR gates, implement: " +
                          "; ".join(f"<code>{k} = {e}</code>" for k, e in fns.items()) + ". List each function's minterms.",
                          fields, "<p>Expand each to minterms, then OR those decoder outputs.</p><ul>" + "".join(rows) + "</ul>", ref="11 §2"))
    P.append({"n": "4.28", "text": "Decoder plus external gates.", "qs": qs})

    # 4.29 priority encoder D0 highest
    def pe(m):
        d = [(m >> (3 - k)) & 1 for k in range(4)]  # a=D0 b=D1 c=D2 d=D3
        for k in range(4):
            if d[k]:
                return k
        return None
    xo, xd = from_spec(4, lambda m: None if pe(m) is None else pe(m) >> 1)
    yo, yd = from_spec(4, lambda m: None if pe(m) is None else pe(m) & 1)
    qx, *_ = kmap_card(tag("4.29", "x", True), "4-input priority encoder, <b>D₀ highest</b> priority. Write a = D₀, b = D₁, c = D₂, d = D₃. "
                       "Outputs xy = index of the highest-priority 1. Minimal <b>x</b> (all-zero input is a don't care).", "abcd", xo, "k4-29x", dc=xd, ref="11 §5")
    qy, *_ = kmap_card(tag("4.29", "y", True), "Same encoder: minimal <b>y</b>.", "abcd", yo, "k4-29y", dc=yd, ref="11 §5")
    tab = ("<table class='bits'><tr><th>D₀</th><th>D₁</th><th>D₂</th><th>D₃</th><th>x</th><th>y</th><th>V</th></tr>"
           "<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>x</td><td>x</td><td>0</td></tr>"
           "<tr><td>1</td><td>x</td><td>x</td><td>x</td><td>0</td><td>0</td><td>1</td></tr>"
           "<tr><td>0</td><td>1</td><td>x</td><td>x</td><td>0</td><td>1</td><td>1</td></tr>"
           "<tr><td>0</td><td>0</td><td>1</td><td>x</td><td>1</td><td>0</td><td>1</td></tr>"
           "<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>")
    qx["why"] = tab + qx["why"]
    P.append({"n": "4.29", "text": "Priority encoder with D₀ highest.", "qs": [qx, qy,
              bool_q(tag("4.29", "V", True), "Same encoder: write the valid output <b>V</b> (1 when any input is 1).", "abcd", "a + b + c + d", "a + b + c + d",
                     "<p><b>V = D₀ + D₁ + D₂ + D₃</b>.</p>", lits_=4, ref="11 §5")]})

    # 4.30 octal priority encoder
    rows = "".join(f"<tr><td>{'0' * (7 - k)}1{'x' * k}</td><td>{k:03b}</td><td>1</td></tr>" for k in range(7, -1, -1))
    P.append({"n": "4.30", "text": "Octal-to-binary priority encoder.", "qs": [
        multi_q(tag("4.30"), "Octal-to-binary priority encoder (D₇ highest priority) with a valid output V. What are x y z and V when D₂ and D₆ are both 1?",
                [("x", ["1"]), ("y", ["1"]), ("z", ["0"]), ("V", ["1"])],
                "<p>Condensed truth table (inputs written D₇ … D₀; x = don't care):</p><table class='bits'><tr><th>D₇…D₀</th><th>xyz</th><th>V</th></tr>"
                "<tr><td>00000000</td><td>xxx</td><td>0</td></tr>" + rows + "</table>"
                "<p>D₆ beats D₂ (higher subscript wins), so the output is 6 = <b>110</b>, V = <b>1</b>.</p>", ref="11 §5")]})
    return write_topic("11", "Decoders and encoders", "Mano 4.22–4.30. Block diagrams are self-marked; equations are checked on every row.", P)


# ======================================================================== TOPIC 12
def topic12():
    P = []
    # 4.3 quad 2-to-1 mux (Fig 4.26)
    P.append({"n": "4.3", "text": "The quadruple 2-to-1 multiplexer of Fig 4.26.", "qs": [
        work_q(tag("4.3", "a"), "Fig 4.26 (4th ed.) is the <b>quadruple 2-to-1 multiplexer</b>: inputs A₃–A₀, B₃–B₀, select S, enable E (active-low). Write the four outputs.",
               "<p>E = 1 disables (all outputs 0). E = 0: S = 0 picks A, S = 1 picks B.</p>"
               "<p><b>Yᵢ = E'(S'Aᵢ + SBᵢ)</b> for i = 0, 1, 2, 3.</p>", ref="12 §1"),
        multi_q(tag("4.3", "b", True), "If that circuit were listed in a truth table, how many rows and columns would it have?",
                [("rows", ["1024", "1,024"]), ("columns", ["14"])],
                "<p>Inputs: 4 (A) + 4 (B) + S + E = 10 → 2¹⁰ = <b>1024 rows</b>. Columns: 10 inputs + 4 outputs = <b>14</b>.</p>", ref="12 §1")]})

    # 4.31 16x1 from two 8x1 and one 2x1
    s = Svg(560, 590, "16 × 1 from two 8 × 1 and one 2 × 1")
    m1 = mux_shape(s, 120, 20, 8, ["I₀"] + [""] * 6 + ["I₇"], ["S₂", "S₁", "S₀"], out=None, pitch=22, title="8 × 1")
    m2 = mux_shape(s, 120, 290, 8, ["I₈"] + [""] * 6 + ["I₁₅"], ["S₂", "S₁", "S₀"], out=None, pitch=22, title="8 × 1")
    m3 = mux_shape(s, 380, 200, 2, ["", ""], ["S₃"], out="Y", pitch=40, title="2 × 1")
    wire(s, m1["y"], m3["d"][0], midx=320)
    wire(s, m2["y"], m3["d"][1], midx=340)
    s.text(300, 580, "S₂S₁S₀ go to both 8 × 1 muxes", size=12, color=MUTED, anchor="start")
    save_svg(s, "b4-31")
    P.append({"n": "4.31", "text": "16 × 1 multiplexer from smaller ones.", "qs": [
        work_q(tag("4.31"), "Build a 16 × 1 multiplexer from two 8 × 1 and one 2 × 1 multiplexers (block diagram).",
               "<p>The low three select bits S₂S₁S₀ pick one input inside each 8 × 1 (both at once). "
               "The top bit S₃ then picks which half: I₀–I₇ or I₈–I₁₅.</p>" + img("b4-31"), ref="12 §2")]})

    # 4.32 function with a mux (8x1, D as data)
    def mux_inputs(ones_):
        out = []
        for i in range(8):
            a, b = 2 * i in ones_, 2 * i + 1 in ones_
            out.append("1" if a and b else "0" if not a and not b else "D'" if a else "D")
        return out
    qs = []
    for part, o, label in [("a", [0, 2, 5, 7, 11, 14], "Σ(0, 2, 5, 7, 11, 14)"), ("b", [m for m in range(16) if m not in (3, 8, 12)], "Π(3, 8, 12)")]:
        ins = mux_inputs(o)
        for i, v in enumerate(ins):
            for dbit in (0, 1):
                val = {"1": 1, "0": 0, "D": dbit, "D'": 1 - dbit}[v]
                assert val == int(2 * i + dbit in o)
        s = Svg(420, 360, f"4.32 {part}")
        mux_shape(s, 140, 20, 8, ins, ["A", "B", "C"], out="F", pitch=30, title="8 × 1")
        save_svg(s, f"b4-32{part}")
        rows = "".join(f"<tr><td>{i}</td><td>{i:03b}</td><td>{2 * i}</td><td>{int(2 * i in o)}</td><td>{2 * i + 1}</td><td>{int(2 * i + 1 in o)}</td><td><b>{v}</b></td></tr>" for i, v in enumerate(ins))
        qs.append(multi_q(tag("4.32", part), f"Implement <code>F(A, B, C, D) = {label}</code> with an 8 × 1 multiplexer: A, B, C on the selects, "
                          "D (or D', 0, 1) on the data inputs. Fill I₀ … I₇.",
                          [(f"I{'₀₁₂₃₄₅₆₇'[i]}", [v]) for i, v in enumerate(ins)],
                          "<p>Take the rows in pairs (D = 0 and D = 1) for each ABC:</p><table class='bits'><tr><th>I</th><th>ABC</th><th>m (D=0)</th><th>F</th>"
                          "<th>m (D=1)</th><th>F</th><th>input</th></tr>" + rows + "</table>"
                          "<p>Both 0 → 0, both 1 → 1, F = D → D, F = D' → D'.</p>" + img(f"b4-32{part}"), ref="12 §4"))
    P.append({"n": "4.32", "text": "Implement functions with a multiplexer.", "qs": qs})

    # 4.33 full adder with two 4x1
    sm = {"S": ["z", "z'", "z'", "z"], "C": ["0", "z", "z", "1"]}
    for i in range(4):
        x, y = i >> 1, i & 1
        for z in (0, 1):
            vals = {"z": z, "z'": 1 - z, "0": 0, "1": 1}
            assert vals[sm["S"][i]] == (x + y + z) & 1 and vals[sm["C"][i]] == int(x + y + z >= 2)
    s = Svg(520, 260, "Full adder with two 4 × 1 muxes")
    mux_shape(s, 110, 20, 4, sm["S"], ["x", "y"], out="S", pitch=36, title="4 × 1")
    mux_shape(s, 330, 20, 4, sm["C"], ["x", "y"], out="C", pitch=36, title="4 × 1")
    save_svg(s, "b4-33")
    P.append({"n": "4.33", "text": "Full adder from two 4 × 1 multiplexers.", "qs": [
        multi_q(tag("4.33"), "Implement a full adder (inputs x, y, z) with two 4 × 1 multiplexers, x and y on the selects. What goes on each data input?",
                [(f"S: I{'₀₁₂₃'[i]}", [v]) for i, v in enumerate(sm["S"])] + [(f"C: I{'₀₁₂₃'[i]}", [v]) for i, v in enumerate(sm["C"])],
                "<p>For each xy, write S and C as a function of z alone:</p><table class='bits'><tr><th>xy</th><th>S</th><th>C</th></tr>" +
                "".join(f"<tr><td>{i:02b}</td><td>{sm['S'][i]}</td><td>{sm['C'][i]}</td></tr>" for i in range(4)) + "</table>" + img("b4-33"), ref="12 §4")]})

    # 4.34 what does the mux implement
    qs = []
    for part, star, I in [("a", True, ["D", "0", "0", "1", "D", "1", "D'", "0"]), ("b", False, ["D'", "0", "0", "1", "D", "D", "D'", "1"])]:
        o = []
        for i, v in enumerate(I):
            for dbit in (0, 1):
                if {"1": 1, "0": 0, "D": dbit, "D'": 1 - dbit}[v]:
                    o.append(2 * i + dbit)
        best = solve("ABCD", o)[0]
        qs.append(multi_q(tag("4.34", part, star), "An 8 × 1 mux has A, B, C on S₂, S₁, S₀. Data: " + ", ".join(f"I{'₀₁₂₃₄₅₆₇'[i]} = {v}" for i, v in enumerate(I)) +
                          ". Which function F(A, B, C, D) does it implement? Give the minterms.", [("Σm(", set_answers(o))],
                          "<p>Input Iᵢ covers minterms 2i (D = 0) and 2i + 1 (D = 1). 1 → both, D → the odd one, D' → the even one, 0 → neither.</p>"
                          "<table class='bits'><tr><th>I</th><th>value</th><th>minterms</th></tr>" +
                          "".join(f"<tr><td>{i}</td><td>{v}</td><td>{', '.join(str(m) for m in (2 * i, 2 * i + 1) if m in o) or '–'}</td></tr>" for i, v in enumerate(I)) +
                          f"</table><p><b>F = Σ({lst(o)})</b> = {best} (minimal SOP).</p>", ref="12 §4"))
    P.append({"n": "4.34", "text": "Find the function a multiplexer implements.", "qs": qs})

    # 4.35 4x1 mux with external gates
    qs = []
    for part, star, o in [("a", True, [1, 3, 4, 11, 12, 13, 14, 15]), ("b", False, [1, 2, 4, 7, 8, 9, 10, 11, 13, 15])]:
        exprs = []
        for i in range(4):
            sub = [m - 4 * i for m in o if 4 * i <= m < 4 * i + 4]
            if len(sub) == 4:
                e = "1"
            elif not sub:
                e = "0"
            elif sorted(sub) == [1, 2]:
                e = "C ⊕ D"
            elif sorted(sub) == [0, 3]:
                e = "C ⊙ D"
            else:
                e = solve("CD", sub)[0]
            assert ones(e, "CD") == sorted(sub), (e, sub)
            exprs.append((e, sub))
        s = Svg(420, 260, f"4.35 {part}")
        mux_shape(s, 160, 20, 4, [e for e, _ in exprs], ["A", "B"], out="F", pitch=36, title="4 × 1")
        save_svg(s, f"b4-35{part}")
        for i, (e, sub) in enumerate(exprs):
            label = f"Σ({', '.join(str(m) for m in o)})"
            q = bool_q(tag("4.35", f"{part} · I{i}", star), f"F(A, B, C, D) = {label} on a 4 × 1 mux, A B on the selects. "
                       f"What goes on data input <b>I{'₀₁₂₃'[i]}</b> (AB = {i:02b})? Write it in C and D.",
                       "CD", e if e not in ("0", "1") else e, e,
                       f"<p>AB = {i:02b} covers minterms {4 * i}–{4 * i + 3}, i.e. CD = 00, 01, 10, 11. F is 1 on CD = {', '.join(f'{m:02b}' for m in sub) or 'none'}.</p>"
                       f"<p><b>I{'₀₁₂₃'[i]} = {e}</b>" + (" (tie to logic 1)" if e == "1" else " (tie to ground)" if e == "0" else "") + ".</p>" +
                       (img(f"b4-35{part}") if i == 3 else ""), ref="12 §4")
            qs.append(q)
    P.append({"n": "4.35", "text": "4 × 1 multiplexer with external gates.", "qs": qs})
    return write_topic("12", "Multiplexers", "Mano 4.3, 4.31–4.35. For data inputs type 0, 1, D or D' (or an expression in C and D).", P)


def build():
    return {"10": topic10(), "11": topic11(), "12": topic12()}
