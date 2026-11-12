"""Build docs/final/data.js (+ figures) for the final-exam Lock-In page.

Run: python3 tools/build_final.py
Bump VERSION whenever the content changes so browsers fetch the new data file.
"""
import json, os, re
from final_q import *
from final_lib import S

VERSION = "2026-11-12c"
OUT = os.path.join(ROOT, "docs", "final")

PARTS = []


def part(**k):
    PARTS.append(k)
    return k


def item(id, title, prompt, steps, src="", answer=""):
    return dict(id=id, title=title, prompt=prompt, steps=[{"do": a, "why": b} for a, b in steps], src=src, answer=answer)


def ex(n):
    return f"../svg/{n}.svg"


XYZ, ABC, ABCD = list("XYZ"), list("ABC"), list("ABCD")

# =====================================================================
# The 23/24 paper (worked once, reused by topics and the sample exam)
# =====================================================================
P1 = ("OR", ("AND", ("NOT", "X"), ("NOT", "Y")), ("NAND", ("OR", "X", "Y"), ("NOT", "Z")))
draw_tree("pp-q1", P1, "F", title="Fig. 1")
pp1a = p_function(P1)
pp1a.append(["Optional tidy-up with De Morgan:" + DD("((X+Y)Z')' = (X+Y)' + Z = X'Y' + Z") + DD("F = X'Y' + X'Y' + Z = X'Y' + Z"),
             "Not required for part (a), but it makes the truth table quicker and it must match what the K-map gives in part (d)."])
pp1b, P1ms = p_truth(P1, XYZ, "pp-q1")
pp1c = p_minmax(P1ms, XYZ)
pp1d_s, P1cov = p_simplify(P1ms, XYZ, "pp-q1")
pp1d = pp1d_s + p_nand(P1cov, XYZ, "pp-q1")
assert P1ms == [0, 1, 3, 5, 7]

pp2a = p_ripple(3, "D", True, "pp-q2a")
PP2B = "AB'(D'+CD) + A'(B+CD) + A'CD'"
pp2b_h, pp2b_ans = p_hazard(PP2B, ABCD, "pp-q2b", expanded="AB'D' + AB'CD + A'B + A'CD + A'CD'")
pp2b = [["Cause: the same input reaches the output by <b>two paths with different delays</b> (for example one goes through an inverter). When that input changes, one product term turns off slightly before another turns on, and the output glitches for a moment.",
         "Static-1 hazard: output should stay 1 but dips to 0. Static-0: should stay 0 but pulses to 1. It happens when two neighbouring K-map cells are covered by different groups."]] + pp2b_h

PP3 = [[3, 1, 2, 0, 4], [7, 6, 5]]
pp3, PP3R = p_counter(PP3, ABC, "pp-q3", twomode=True)
pp3.insert(8, ["Fewest gates: spot the single-gate forms." + DD("JA = KA = B'C' = (B+C)' \\;\\text{(one NOR)}") + DD("KB = A' + C' = (AC)' \\;\\text{(one NAND)}") + DD("KC = AB + A'B' = (A ^ B)' \\;\\text{(one XNOR)}") + "<p>Total: NOR, OR, NAND, XNOR = <b>4 gates</b>. J<sub>C</sub> = A is just a wire.</p>",
               "The question asks for the minimum number of external gates. De Morgan turns two-term sums of inverted letters into one NAND or NOR, and J<sub>A</sub> and K<sub>A</sub> share the same gate."])

PP4Y, PP4Z = "AB + Ay'", "A + Y"
draw_tree("pp-q4", ("OR", ("AND", "A", "B"), ("AND", "A", ("NOT", "y"))), "Y", feedback="y", title="Fig. 2")
pp4a, pp4b, pp4c, PP4 = p_async(PP4Y, PP4Z, ["A", "B"], "pp-q4")
pp4a[0][0] += "<p>(z comes from the top OR gate: inputs A and Y.)</p>"
pp4b.append(["Notice z = A + Y = A here.", "Y = A(B + y') can only be 1 when A is 1, so OR-ing it with A adds nothing. The output simply follows A."])

# =====================================================================
# EXAM PATH
# =====================================================================
part(id="start", kind="info", tab="path", title="Start here", html=f"""
<h3>What the 23/24 paper asked</h3>
<p>One past paper (Autumn 23/24, Prof. Anding Zhu). 4 questions, equal marks, 120 minutes → <b>30 minutes each</b>. Calculator allowed. No formula sheet is listed, so the flip-flop tables must be in your head.</p>
{table(["Q", "What it asked", "Marks", "Topics here"], [
 ["1", "Circuit → Boolean function, truth table + K-map, Σm and ΠM, simplify, two-level NAND", "25%", "1, 2, 3, 4"],
 ["2a", "3-bit ripple <b>count-down</b> counter with D flip-flops, waveforms, frequency divider", "15%", "5, 6"],
 ["2b", "What causes static hazards, hazard-free circuit for a 4-variable function", "10%", "3, 8"],
 ["3", "Synchronous JK state machine with two count loops", "25%", "3, 5, 7"],
 ["4", "Asynchronous circuit: transition table, flow table, stability", "25%", "9"]])}
<h3>How often each topic came up (1 paper)</h3>
{table(["Topic", "Share of paper", "Needed by"], [
 ["3 · K-maps", "used in 3 of 4 questions", "Q1, Q2b, Q3"],
 ["7 · Synchronous counter design (JK)", "25%", "Q3"],
 ["9 · Asynchronous circuits", "25%", "Q4"],
 ["6 · Ripple counters", "15%", "Q2a"],
 ["8 · Static hazards", "10%", "Q2b"],
 ["1 · Circuit → function → truth table", "10%", "Q1a, b"],
 ["4 · Two-level NAND", "about 8%", "Q1d"],
 ["2 · Σm and ΠM", "5%", "Q1c"],
 ["5 · Flip-flops and excitation table", "inside Q2a and Q3", "Q2a, Q3"]])}
<div class="warn"><b>Two warnings.</b> (1) This is one paper, so "how often" is thin evidence. (2) You remembered the lecturer saying this year has 5 questions: 1 combinational (maybe multiplexers) and the rest sequential. Multiplexers and sequence detectors were <b>not</b> on the 23/24 paper, so they are in the <b>More practice</b> tab under "Lecturer hinted". Do them after the exam path, not instead of it.</div>
<h3>How to use this page</h3>
<ol><li>One thing per screen. Read <b>Learn</b>, then each question.</li><li>Try the question on paper, then press <b>Next</b>: one step per screen, each with its why.</li><li>At the end mark <b>Got it</b> or <b>Need to redo</b>. Red dots are the ones to redo tomorrow.</li><li>Finish with the worked paper, then the two mocks under time.</li></ol>
<p class="keys">Keys: <kbd>Space</kbd> or <kbd>→</kbd> next · <kbd>←</kbd> back · <kbd>J</kbd> / <kbd>K</kbd> skip question · <kbd>A</kbd> all steps · <kbd>G</kbd> got it · <kbd>R</kbd> redo</p>
""")

# ---------------------------------------------------------------- Topic 1
C1 = ("OR", ("AND", "A", "B"), ("NOR", "B", "C"))
C2 = ("NAND", ("OR", "A", ("NOT", "B")), "C")
C3 = ("OR", ("NAND", ("OR", "A", "B"), "C"), ("AND", ("NOT", "A"), "B"))
t1_items = []
for i, (tr, nm) in enumerate(((C1, "1.1"), (C2, "1.2"), (C3, "1.3"))):
    key = f"t1-{i+1}"
    draw_tree(key, tr, "F")
    st = p_function(tr)
    tt, ms = p_truth(tr, ABC, key)
    st += tt[:2]
    st.append([demorgan_note(tr, ABC), "Use it as a check: the simplified form must give the same F column."])
    t1_items.append(item(key, f"{nm} Read this circuit", img(key, "circuit") + "<p>(a) Write the Boolean function F. (b) Give its truth table.</p>", st,
                         src="Past paper Q1(a), (b) style", answer=M("F = " + T_tex(tr)) + " · " + "$" + sigma(ms) + "$"))
t1_items.append(item("t1-pp", "1.4 Past paper Q1(a)", img("pp-q1", "Fig. 1") + "<p>Write a Boolean function relating X, Y, Z and F.</p>", pp1a, src="23/24 Q1(a) · 10%", answer=M("F = X'Y' + ((X+Y)Z')' = X'Y' + Z")))
part(id="t1", kind="topic", tab="path", title="1 · Circuit → Boolean function → truth table", freq="Q1(a), (b) · 10%",
     learn=f"""<p>Every gate is a tiny rule. Read the circuit <b>left to right</b>, writing each gate's output on its wire.</p>
{img(ex("gates"), "gate symbols", True)}
{table(["Gate", "Output is 1 when…", "Written"], [["AND", "all inputs are 1", M("AB")], ["OR", "any input is 1", M("A+B")], ["NOT", "input is 0", M("A'")], ["NAND", "<b>not</b> all inputs are 1", M("(AB)'")], ["NOR", "<b>no</b> input is 1", M("(A+B)'")]])}
<p>A <b>bubble</b> (small circle) means "invert". De Morgan pushes a bar inside and swaps the operation:</p>
$$(AB)' = A' + B' \\qquad (A+B)' = A'B'$$
<p><b>Truth table:</b> n inputs → {M("2^n")} rows in counting order. Work out F for each row.</p>""",
     check=dict(q="A NAND gate has inputs 1 and 1. Output?", a="<b>0.</b> AND gives 1, the bubble inverts it."), items=t1_items)

# ---------------------------------------------------------------- Topic 2
t2_items = []
for i, (e, names) in enumerate((("A'B + AC", ABC), ("(X + Y')(Y + Z)", XYZ), ("AB' + C'D", ABCD))):
    ms = minterms(e, names)
    n = len(names)
    rows = [list(bits(m, n)) + [str(int(m in ms))] for m in range(1 << n)]
    st = [["Make the truth table:" + table(list(names) + ["F"], rows), "Row number in binary = the input values. Evaluate F on each row."]] + p_minmax(ms, names)
    t2_items.append(item(f"t2-{i+1}", f"2.{i+1} Shorthand forms", f"<p>Express {M('F = ' + e)} as a sum of minterms and as a product of maxterms (shorthand).</p>", st,
                         src="Past paper Q1(c) style", answer="$" + sigma(ms) + " = " + pi([m for m in range(1 << n) if m not in ms]) + "$"))
t2_items.append(item("t2-pp", "2.4 Past paper Q1(c)", img("pp-q1", "Fig. 1") + "<p>Express the function as a sum of minterms and as a product of maxterms, shorthand format.</p>",
                     [["From Q1(b), F = 1 on rows 0, 1, 3, 5, 7.", "The truth table already has everything. Part (c) is just reading it."]] + pp1c, src="23/24 Q1(c) · 20%",
                     answer="$" + sigma(P1ms) + " = " + pi([2, 4, 6]) + "$"))
part(id="t2", kind="topic", tab="path", title="2 · Sum of minterms, product of maxterms", freq="Q1(c) · 5%",
     learn=f"""<p>Number the truth-table rows 0, 1, 2 … from the top.</p>
<p><b>Minterm</b> {M("m_i")}: an AND of all the variables that is 1 <b>only on row i</b>.<br><b>Maxterm</b> {M("M_i")}: an OR of all the variables that is 0 <b>only on row i</b>.</p>
$$F = \\Sigma m(\\text{{rows where }} F = 1) \\qquad F = \\Pi M(\\text{{rows where }} F = 0)$$
{img(ex("sigma-pi-switch"), "switching between the two", True)}
<p>The two lists are opposites: a row number is in one or the other, never both.</p>""",
     check=dict(q=f"3 variables, {M('F = ' )}$\\Sigma m(1, 4, 6)$. Write it as ΠM.", a="$\\Pi M(0, 2, 3, 5, 7)$: every row number that is not in the Σ list."), items=t2_items)

# ---------------------------------------------------------------- Topic 3
t3_items = []
specs = [("3.1 Three variables", ABC, [0, 1, 3, 5, 7], [], "Same shape as the past paper."),
         ("3.2 Three variables, wrap-around", ABC, [0, 2, 4, 5, 6], [], ""),
         ("3.3 Four variables", ABCD, [0, 2, 5, 7, 8, 10, 13, 15], [], "Four corners."),
         ("3.4 Four variables", ABCD, [1, 3, 4, 5, 6, 7, 12, 13], [], ""),
         ("3.5 With don't cares", ABC, [1], [2, 3, 5, 6, 7], "This is a real J column from a counter design (Topic 7).")]
for i, (ttl, names, ms, dc, note) in enumerate(specs):
    key = f"t3-{i+1}"
    st, c = p_simplify(ms, names, key, dc)
    pr = "$F(" + ", ".join(names) + ") = " + sigma(ms) + "$" + (" with don't cares $d(" + ", ".join(map(str, dc)) + ")$" if dc else "")
    t3_items.append(item(key, ttl, f"<p>Simplify {pr} with a K-map.</p>" + (f"<p class='note'>{note}</p>" if note else ""), st,
                         src="Used in past paper Q1(d), Q2(b), Q3", answer=M("F = " + cover_tex(c, names))))
part(id="t3", kind="topic", tab="path", title="3 · K-map simplification", freq="Used in Q1, Q2(b), Q3",
     learn=f"""<p>A K-map is the truth table folded so that <b>neighbouring cells differ in one variable</b>. That is why the labels go 00, 01, <b>11, 10</b>.</p>
{img(ex("k3-index"), "3-variable map", True)}{img(ex("k4-index"), "4-variable map", True)}
<ol><li>Put a 1 in each minterm's cell.</li><li>Circle groups of <b>1, 2, 4 or 8</b>. As big as possible, as few as possible. Edges wrap round.</li><li>For each group keep only the variables that <b>do not change</b>. 0 → primed, 1 → plain.</li><li>OR the groups.</li></ol>
<p><b>Don't care (x):</b> may be circled if it makes a group bigger, otherwise ignore it.</p>""",
     check=dict(q="On a 4-variable map, a group of 4 cells gives a term with how many letters?", a="<b>2.</b> Each doubling of the group removes one letter: 1 cell = 4 letters, 2 = 3, 4 = 2, 8 = 1."), items=t3_items)

# ---------------------------------------------------------------- Topic 4
t4_items = []
for i, (ttl, names, ms) in enumerate((("4.1", ABC, [1, 3, 6, 7]), ("4.2 A lone letter", ABC, [1, 3, 4, 5, 7]), ("4.3 Four variables", ABCD, [0, 1, 2, 3, 13, 15]))):
    key = f"t4-{i+1}"
    st, c = p_simplify(ms, names, key)
    st = st[:1] + st[2:] + p_nand(c, names, key)
    t4_items.append(item(key, f"{ttl} Two-level NAND", "<p>Simplify $F(" + ", ".join(names) + ") = " + sigma(ms) + "$ and implement it with two-level NAND gates.</p>", st,
                         src="Past paper Q1(d) style", answer=M("F = " + cover_tex(c, names))))
t4_items.append(item("t4-pp", "4.4 Past paper Q1(d)", img("pp-q1", "Fig. 1") + "<p>Simplify with the K-map and implement with two-level NAND gates. NOT gates allowed.</p>", pp1d, src="23/24 Q1(d) · 40%", answer=M("F = X'Y' + Z = ((X'Y')' \\cdot Z')'")))
part(id="t4", kind="topic", tab="path", title="4 · Two-level NAND circuits", freq="Q1(d) · about 8%",
     learn=f"""<p>Any sum of products becomes NAND-NAND with no extra thought:</p>
$$F = AB + CD = \\big((AB)' \\cdot (CD)'\\big)'$$
{img(ex("nand-transform"), "AND-OR to NAND-NAND", True)}
<ol><li>Simplify to SOP with the K-map.</li><li>Replace every AND gate with a NAND.</li><li>Replace the OR gate with a NAND.</li><li><b>A term with one letter</b> has no first gate, so <b>invert that letter</b> before the last NAND.</li></ol>
<p>Why it works: invert twice (no change), then De Morgan turns the OR into "AND of inverted things, inverted" = NAND.</p>""",
     check=dict(q=f"{M('F = AB + C')} as NAND-NAND. What goes into the last NAND?", a=f"{M('(AB)' + chr(39))} and {M('C' + chr(39))}. The lone C must be inverted."), items=t4_items)

# ---------------------------------------------------------------- Topic 5
ET = table(["Q → Q⁺", "J K", "D", "T"], [["0 → 0", "0 x", "0", "0"], ["0 → 1", "1 x", "1", "1"], ["1 → 0", "x 1", "0", "1"], ["1 → 1", "x 0", "1", "0"]])
jkseq = [(1, 0), (0, 0), (1, 1), (0, 1), (1, 1), (1, 1), (0, 0), (1, 0)]
q, rows = 0, []
for i, (j, k) in enumerate(jkseq):
    q2 = int((j and not q) or (not k and q))
    rows.append([i + 1, f"{j}{k}", {(0, 0): "hold", (0, 1): "reset", (1, 0): "set", (1, 1): "toggle"}[(j, k)], f"<b>{q2}</b>"])
    q = q2
t5_items = [
    item("t5-1", "5.1 Follow a JK flip-flop", "<p>A JK flip-flop starts at Q = 0. At eight clock edges in a row JK = 10, 00, 11, 01, 11, 11, 00, 10. Give Q after each edge.</p>",
         [["Recall the four JK actions: 00 hold, 01 reset, 10 set, 11 toggle.", "J is the set input, K is the reset input. Both on = flip."],
          ["Apply one edge at a time, always starting from the previous Q:" + table(["Edge", "JK", "Action", "Q after"], rows), "A flip-flop only changes on the clock edge, and what it does depends on what it holds now."]],
         src="Skill needed for Q2(a), Q3", answer="Q = " + ", ".join(re.sub("<.*?>", "", r[3]) for r in rows)),
    item("t5-2", "5.2 Build the excitation table", "<p>Starting from the JK characteristic table, work out which J K values make Q go 0→0, 0→1, 1→0 and 1→1.</p>",
         [["0 → 0: hold (00) or reset (01) both work. J = 0 in both, K is either → <b>0 x</b>.", "List every action that gives the move, then see which input is the same in all of them."],
          ["0 → 1: set (10) or toggle (11). J = 1, K either → <b>1 x</b>.", "Same reasoning."],
          ["1 → 0: reset (01) or toggle (11). K = 1, J either → <b>x 1</b>.", "Now Q starts at 1, so K is the input that matters."],
          ["1 → 1: hold (00) or set (10). K = 0, J either → <b>x 0</b>.", ""],
          ["Shortcut:" + ET, "Present Q = 0 → J = next Q, K = x. Present Q = 1 → K = opposite of next Q, J = x. D is simply next Q. T is 1 when Q changes."]],
         src="Skill needed for Q3", answer="0x, 1x, x1, x0"),
    item("t5-3", "5.3 Make a D flip-flop toggle", "<p>How do you connect a D flip-flop so that Q flips on every clock edge? Why does that halve the clock frequency?</p>",
         [["Connect its own inverted output back to its input:" + DD("D = Q'"), "A D flip-flop copies D at the clock edge. If D is always the opposite of Q, the next Q is always the opposite of the present Q."],
          ["Q flips once per clock edge, so it needs <b>two</b> clock periods to go 0 → 1 → 0.", "One full cycle of Q takes two full cycles of the clock."],
          ["So the frequency of Q is half the clock frequency: $f_Q = f / 2$.", "This is the building block of the ripple counter in Q2(a)."]],
         src="Skill needed for Q2(a)", answer=M("D = Q'") + ", output at f / 2"),
]
part(id="t5", kind="topic", tab="path", title="5 · Flip-flops and the excitation table", freq="Inside Q2(a) and Q3",
     learn=f"""<p>A <b>flip-flop</b> stores 1 bit (Q). It only changes at the <b>clock edge</b>. Q⁺ means "Q after the next edge".</p>
{img("../svg/seq/ff-symbols.svg", "flip-flops", True)}
{table(["Flip-flop", "What it does at the edge", "Equation"], [["D", "copies D", M("Q^+ = D")], ["T", "T = 1: toggle. T = 0: hold", M("Q^+ = T ^ Q")], ["JK", "00 hold · 01 reset · 10 set · 11 toggle", M("Q^+ = JQ' + K'Q")]])}
<p><b>Excitation table</b> = the same facts backwards: "I want Q to go from this to that. What inputs?" You need it for every design question.</p>
{ET}""",
     check=dict(q="Q = 1 and you want Q⁺ = 0. What are J and K?", a="<b>J = x, K = 1.</b> Reset (01) or toggle (11) both work, so K must be 1 and J can be anything."), items=t5_items)

# ---------------------------------------------------------------- Topic 6
t6_items = [
    item("t6-1", "6.1 Count up, D flip-flops", "<p>Design a 3-bit binary ripple <b>count-up</b> counter using D flip-flops. Show the logic diagram and output waveforms.</p>", p_ripple(3, "D", False, "t6-1"), src="Past paper Q2(a) variation", answer="D = Q' on each, clock each stage from the previous Q' (rising edge)"),
    item("t6-2", "6.2 Count down, T flip-flops, 2 bits", "<p>Design a 2-bit ripple count-down counter with T flip-flops. Draw the waveforms.</p>", p_ripple(2, "T", True, "t6-2"), src="Past paper Q2(a) variation", answer="T = 1, clock stage 2 from Q₀"),
    item("t6-3", "6.3 Frequency divider numbers", "<p>A 4-stage ripple counter (JK, J = K = 1) is driven by an 800 kHz clock. What frequency is at each output? Which output gives 100 kHz?</p>", p_ripple(4, "JK", False, "t6-3", f0=(800, "kHz"))[4:] + [["100 kHz = 800 kHz ÷ 8 = 800 kHz ÷ 2³ → the <b>third</b> stage, Q₂.", "Divide by 2 for each stage you pass through."]], src="Past paper Q2(a) last part", answer="400, 200, 100, 50 kHz · 100 kHz is at Q₂"),
    item("t6-pp", "6.4 Past paper Q2(a)", "<p>Design a three-bit binary ripple count-down counter using D flip-flops. Show the logic diagram, draw the output waveforms and briefly explain how this circuit can be used as a frequency divider.</p>", pp2a, src="23/24 Q2(a) · 60%", answer="D = Q' on each flip-flop, each stage clocked by the previous Q, outputs at f/2, f/4, f/8"),
]
part(id="t6", kind="topic", tab="path", title="6 · Ripple counters and frequency division", freq="Q2(a) · 15%",
     learn=f"""<p>A <b>ripple counter</b> is a chain of flip-flops that each <b>toggle</b>. Only the first one gets the real clock. <b>Each later one is clocked by the flip-flop before it.</b></p>
{img("../svg/seq/ripple4-counter.svg", "ripple counter", True)}
{table(["To make it toggle", "Connect"], [["D flip-flop", M("D = Q'") + " (its own inverted output)"], ["T flip-flop", "T = 1"], ["JK flip-flop", "J = K = 1"]])}
{table(["Flip-flop edge", "Clock next stage from", "Counts"], [["rising", "Q", "<b>down</b>"], ["rising", "Q'", "up"], ["falling", "Q", "up"], ["falling", "Q'", "<b>down</b>"]])}
<p><b>Why:</b> counting up, a bit flips when the bit below it <b>falls</b> (carry). Counting down, it flips when the bit below <b>rises</b> (borrow). Pick the clock connection that gives the flip-flop its active edge at that moment.</p>
<p><b>Frequency divider:</b> every stage halves the frequency. n stages → f ÷ 2ⁿ.</p>""",
     check=dict(q="Falling-edge flip-flops, each clocked from the previous Q. Up or down?", a="<b>Up.</b> A falling edge on Q is a 1 → 0 change, which is when a carry happens."), items=t6_items)

# ---------------------------------------------------------------- Topic 7
m5, R5 = p_counter([[0, 1, 2, 3, 4]], ABC, "t7-1")
m6, R6 = p_counter([[0, 1, 2, 3, 4, 5]], ABC, "t7-2")
tw, RT = p_counter([[0, 2, 3, 6, 5], [1, 4, 7]], ABC, "t7-3", twomode=True)
t7_items = [
    item("t7-1", "7.1 Modulo-5 counter", "<p>Design a synchronous counter that counts 000 → 001 → 010 → 011 → 100 → 000 using JK flip-flops. Check the unused states.</p>", m5, src="Lecture 17 example · Q3 style", answer=" · ".join(M(f"{k} = {v}") for k, v in R5["eq"].items())),
    item("t7-2", "7.2 Modulo-6 counter", "<p>Design a synchronous 0 to 5 counter with JK flip-flops. Is it self-correcting?</p>", m6, src="Q3 style", answer=" · ".join(M(f"{k} = {v}") for k, v in R6["eq"].items())),
    item("t7-3", "7.3 Two loops in one circuit", "<p>Use JK flip-flops to design a 3-bit synchronous state machine with two modes. Mode 1: 000 → 010 → 011 → 110 → 101 → 000. Mode 2: 001 → 100 → 111 → 001. One circuit only.</p>", tw, src="Past paper Q3 variation", answer=" · ".join(M(f"{k} = {v}") for k, v in RT["eq"].items())),
    item("t7-pp", "7.4 Past paper Q3", "<p>Use JK flip-flops and external gates to design a 3-bit synchronous binary state machine with two modes. Mode 1: 011 → 001 → 010 → 000 → 100 → 011. Mode 2: 111 → 110 → 101 → 111. One circuit block only. Show the design procedure, state table, logic functions and logic diagram. Minimum flip-flops and gates.</p>", pp3, src="23/24 Q3 · 100%", answer=" · ".join(M(f"{k} = {v}") for k, v in PP3R["eq"].items())),
]
part(id="t7", kind="topic", tab="path", title="7 · Designing a synchronous counter (JK)", freq="Q3 · 25%",
     learn=f"""<p>A <b>synchronous</b> counter: every flip-flop shares the clock. Gates on the J and K inputs decide which bits change. Design = find those gates.</p>
<ol><li><b>State diagram</b> from the count sequence.</li><li><b>State table:</b> present state → next state, one row per state.</li><li><b>Excitation:</b> for each flip-flop, present bit → next bit gives J K.{table(["Q → Q⁺", "J K"], [["0 → 0", "0 x"], ["0 → 1", "1 x"], ["1 → 0", "x 1"], ["1 → 1", "x 0"]], "tt small")}</li><li><b>K-map</b> each J and K (variables = the state bits). x's are free.</li><li><b>Draw</b> the flip-flops and gates.</li><li><b>Unused states</b> are don't cares, then check each one returns to the count.</li></ol>
<p><b>Two loops (the past paper):</b> nothing new. Put both loops in the same state table. If the loops use all 8 states there are no unused states.</p>""",
     check=dict(q="Row 011 → 100. What is J K for the middle flip-flop (B)?", a="B goes 1 → 0, so <b>J K = x 1</b>."), items=t7_items)

# ---------------------------------------------------------------- Topic 8
t8_items = []
for i, (ttl, e, names, exp) in enumerate((("8.1 Three variables", "A'B + AC", ABC, None), ("8.2 Three variables", "XY' + YZ", XYZ, None),
                                          ("8.3 Four variables", "B'C' + A'BD + ACD'", ABCD, None), ("8.4 Brackets first", "A(B'+CD') + A'D(B+C')", ABCD, "AB' + ACD' + A'BD + A'C'D"))):
    key = f"t8-{i+1}"
    st, ans = p_hazard(e, names, key, expanded=exp)
    t8_items.append(item(key, ttl, f"<p>Implement {M('F = ' + e)} without static-1 hazards, using the fewest gates.</p>", st, src="Past paper Q2(b) style", answer=M("F = " + ans)))
t8_items.append(item("t8-pp", "8.5 Past paper Q2(b)", f"<p>Briefly explain what causes static hazards. Implement {M('F(A,B,C,D) = ' + PP2B)} without static-1 hazards, using a minimum number of gates.</p>", pp2b, src="23/24 Q2(b) · 40%", answer=M("F = " + pp2b_ans)))
part(id="t8", kind="topic", tab="path", title="8 · Static hazards", freq="Q2(b) · 10%",
     learn=f"""<p>A <b>hazard</b> is a short glitch at the output. Cause: one input reaches the output along <b>two paths with different delays</b>.</p>
{img("../svg/seq/hazard-glitch.svg", "glitch", True)}
{table(["Hazard", "Output should", "Actually"], [["static-1", "stay 1", "1 → 0 → 1"], ["static-0", "stay 0", "0 → 1 → 0"], ["dynamic", "change once", "changes 3 or more times"]])}
<p><b>On a K-map:</b> a static-1 hazard exists wherever <b>two neighbouring 1s are in different groups</b>.</p>
{img("../svg/seq/hazard-kmap.svg", "bridge", True)}
<p><b>Fix:</b> add one more group that covers both cells (a "bridge"). It is redundant in algebra, but it holds the output at 1 during the change.</p>
<p>Static-0 is the same idea on the 0s of a product-of-sums circuit.</p>""",
     check=dict(q=f"{M('F = XY + X' + chr(39) + 'Z')}. Which term removes the hazard?", a=f"<b>{M('YZ')}</b>. Cells 011 and 111 are neighbours in different groups; the pair they form is YZ."), items=t8_items)

# ---------------------------------------------------------------- Topic 9
def async_item(id, title, Y, z, tree, src):
    draw_tree(id, tree, "Y", feedback="y")
    a, b, c, info = p_async(Y, z, ["A", "B"], id)
    ans = ("Unstable when AB = " + ", ".join(bits(info[0][i], 2) for i in info[2])) if info[2] else "No stability issue"
    pr = img(id, "circuit") + (f"<p>The output is {M('z = ' + z)}.</p>" if z else "") + "<p>(a) Transition table. (b) Flow table. (c) Is there a stability issue?</p>"
    return item(id, title, pr, a + b + c, src=src, answer=ans)


t9_items = [
    async_item("t9-1", "9.1 A circuit that remembers", "AB + Ay + By", None, ("OR", ("AND", "A", "B"), ("AND", "A", "y"), ("AND", "B", "y")), "Past paper Q4 style"),
    async_item("t9-2", "9.2 Find the unstable column", "A'B + By'", "Ay", ("OR", ("AND", ("NOT", "A"), "B"), ("AND", "B", ("NOT", "y"))), "Past paper Q4 style"),
    async_item("t9-3", "9.3 NAND feedback", "(Ay)'B", None, ("AND", ("NAND", "A", "y"), "B"), "Lecture 23 slide 18 (renamed inputs)"),
    item("t9-pp", "9.4 Past paper Q4", img("pp-q4", "Fig. 2") + "<p>Inputs A and B, one internal state y, output z (the top OR gate: z = A + Y). (a) Derive the transition table and show it on a Karnaugh map. (b) Obtain a flow table. (c) Check whether there is a stability issue and explain where it occurs.</p>", pp4a + pp4b + pp4c, src="23/24 Q4 · 100%", answer="Y = AB + Ay' · unstable when AB = 10"),
]
part(id="t9", kind="topic", tab="path", title="9 · Asynchronous circuits: transition table, flow table, stability", freq="Q4 · 25%",
     learn=f"""<p>An <b>asynchronous</b> sequential circuit has <b>no clock</b>. It remembers through a <b>feedback wire</b>: an output that loops back in as an input.</p>
<p>Cut the loop. The same wire now has two names:</p>
{table(["Name", "Which end", "Means"], [["<b>Y</b> (capital)", "leaving the gate", "next state"], ["<b>y</b> (small)", "coming back in", "present state"]])}
$$\\text{{stable}} \\iff Y = y$$
<p><b>Transition table</b> (lecturer's method):</p>
<ol><li>Write Y as a function of the inputs and y.</li><li>Map: rows = y, columns = inputs in K-map order (00, 01, 11, 10), entry = Y.</li><li><b>Circle</b> the entries where Y = the row's y.</li></ol>
{img("../svg/seq/transition-table.svg", "example", True)}
<p><b>Flow table:</b> the same table with letters (a, b …) for the states, plus the output.</p>
<p><b>Stability check:</b> look down each <b>column</b>. A column with <b>no circle</b> means the circuit can never settle for that input: it <b>oscillates</b>.</p>""",
     check=dict(q=f"{M('Y = x' + chr(39) + 'y + xy' + chr(39))}. For which x does it oscillate?", a=f"<b>x = 1.</b> Then {M('Y = y' + chr(39))}: Y is never equal to y. With x = 0, Y = y, always stable."), items=t9_items)

# =====================================================================
# SAMPLE EXAM
# =====================================================================
RULES = """<div class="rules"><b>Rules:</b> 120 minutes · answer all 4 · equal marks → about <b>30 minutes per question</b> · non-programmable calculator · no formula sheet. Percentages show the weight of each part inside its question.</div>"""
part(id="pp", kind="exam", tab="path", title="Sample exam · Autumn 23/24 (the real paper)", freq="Fully worked",
     intro=RULES + "<p>Do it on paper first with a 30-minute timer per question. Then reveal.</p>",
     items=[
         item("pp-1a", "Q1(a) · 10%", img("pp-q1", "Fig. 1") + "<p>Write a Boolean logic function relating the inputs X, Y, Z and the output F.</p>", pp1a, src="Topic 1", answer=M("F = X'Y' + ((X+Y)Z')'")),
         item("pp-1b", "Q1(b) · 30%", "<p>Draw the Karnaugh map and the truth table of the logic circuit.</p>", pp1b, src="Topics 1, 3", answer="F = 1 on rows 0, 1, 3, 5, 7"),
         item("pp-1c", "Q1(c) · 20%", "<p>Express the function as a sum of minterms and as a product of maxterms, shorthand format.</p>", pp1c, src="Topic 2", answer="$" + sigma(P1ms) + " = " + pi([2, 4, 6]) + "$"),
         item("pp-1d", "Q1(d) · 40%", "<p>Simplify using the Karnaugh map and implement with two-level NAND gates. NOT gates can be used.</p>", pp1d, src="Topics 3, 4", answer=M("F = X'Y' + Z")),
         item("pp-2a", "Q2(a) · 60%", "<p>Design a three-bit binary ripple count-down counter using D flip-flops. Show the logic diagram, draw the output waveforms and briefly explain how this circuit can be used as a frequency divider.</p>", pp2a, src="Topics 5, 6", answer="D = Q', clock from previous Q, f/2, f/4, f/8"),
         item("pp-2b", "Q2(b) · 40%", f"<p>Briefly explain what causes static hazards in digital circuits. Implement without static-1 hazards, minimum gates:</p>{DD('F(A,B,C,D) = ' + PP2B)}", pp2b, src="Topics 3, 8", answer=M("F = " + pp2b_ans)),
         item("pp-3", "Q3 · 100%", "<p>Use JK flip-flops and external gates to design a 3-bit synchronous binary state machine with two modes of operation depending on its initial state.</p><p><b>Mode 1:</b> 011 → 001 → 010 → 000 → 100 → back to 011.<br><b>Mode 2:</b> 111 → 110 → 101 → back to 111.</p><p>No external control. Both modes must use ONE circuit block. Show the design procedure, state table, logic functions and logic diagram. Minimum flip-flops and external gates.</p>", pp3, src="Topics 3, 5, 7", answer=" · ".join(M(f"{k} = {v}") for k, v in PP3R["eq"].items())),
         item("pp-4a", "Q4(a) · 40%", img("pp-q4", "Fig. 2") + "<p>Two inputs A and B, one internal state y, one output z (top OR gate: z = A + Y). Derive the transition table and show it on a Karnaugh map.</p>", pp4a, src="Topic 9", answer=M("Y = AB + Ay'")),
         item("pp-4b", "Q4(b) · 20%", "<p>Obtain a flow table for the circuit.</p>", pp4b, src="Topic 9", answer="see table"),
         item("pp-4c", "Q4(c) · 40%", "<p>Check whether there is a stability issue. If so, explain where the instability can occur.</p>", pp4c, src="Topic 9", answer="Oscillates when AB = 10"),
     ])


# =====================================================================
# FRESH MOCKS
# =====================================================================
def mock(mid, title, tree, twolevel, rip, haz, hazexp, cycles, Y, z, ytree, f0):
    key = mid
    draw_tree(key + "-q1", tree, "F", title="Fig. 1")
    a = p_function(tree)
    b, ms = p_truth(tree, XYZ, key + "-q1")
    c = p_minmax(ms, XYZ)
    if twolevel == "NAND":
        d, cov = p_simplify(ms, XYZ, key + "-q1")
        d += p_nand(cov, XYZ, key + "-q1")
        d_ans = M("F = " + cover_tex(cov, XYZ))
    else:
        d0, cov = p_simplify(ms, XYZ, key + "-q1")
        d1, pos = p_nor(ms, XYZ, key + "-q1")
        d = d0 + d1
        d_ans = M("F = " + pos)
    n, kind, down = rip
    r = p_ripple(n, kind, down, key + "-q2a", f0=f0)
    h, hans = p_hazard(haz, ABCD, key + "-q2b", expanded=hazexp)
    h = [["Cause: one input reaches the output by two paths with different delays. When it changes, one product term switches off before the next switches on, and the output glitches.", "It shows on the K-map as two neighbouring 1s that sit in different groups."]] + h
    cs, R = p_counter(cycles, ABC, key + "-q3", twomode=len(cycles) > 1)
    draw_tree(key + "-q4", ytree, "Y", feedback="y", title="Fig. 2")
    qa, qb, qc, info = p_async(Y, z, ["A", "B"], key + "-q4")
    modes = "".join(f"<br><b>Mode {i+1}:</b> " + " → ".join(bits(x, 3) for x in cyc) + f" → back to {bits(cyc[0], 3)}." for i, cyc in enumerate(cycles))
    ffname = {"D": "D", "T": "T", "JK": "JK"}[kind]
    part(id=mid, kind="exam", tab="path", title=title, freq="New questions, same style", intro=RULES + "<p>Unseen questions. Set a 2-hour timer and do the whole paper before revealing anything.</p>",
         items=[
             item(key + "-1a", "Q1(a) · 10%", img(key + "-q1", "Fig. 1") + "<p>Write a Boolean function relating X, Y, Z and F.</p>", a, src="Topic 1", answer=M("F = " + T_tex(tree))),
             item(key + "-1b", "Q1(b) · 30%", "<p>Draw the Karnaugh map and the truth table.</p>", b, src="Topics 1, 3", answer="F = 1 on rows " + ", ".join(map(str, ms))),
             item(key + "-1c", "Q1(c) · 20%", "<p>Express F as a sum of minterms and as a product of maxterms (shorthand).</p>", c, src="Topic 2", answer="$" + sigma(ms) + " = " + pi([m for m in range(8) if m not in ms]) + "$"),
             item(key + "-1d", "Q1(d) · 40%", f"<p>Simplify with the K-map and implement with two-level <b>{twolevel}</b> gates. NOT gates can be used.</p>", d, src="Topics 3, 4", answer=d_ans),
             item(key + "-2a", "Q2(a) · 60%", f"<p>Design a {['', '', 'two', 'three', 'four'][n]}-bit binary ripple count-<b>{'down' if down else 'up'}</b> counter using {ffname} flip-flops. Show the logic diagram, draw the output waveforms, and explain how it works as a frequency divider" + (f". If the clock is {f0[0]} {f0[1]}, what frequency is at each output?" if f0 else ".") + "</p>", r, src="Topics 5, 6", answer="see steps"),
             item(key + "-2b", "Q2(b) · 40%", f"<p>Explain what causes static hazards. Implement without static-1 hazards, minimum gates:</p>{DD('F(A,B,C,D) = ' + haz)}", h, src="Topics 3, 8", answer=M("F = " + hans)),
             item(key + "-3", "Q3 · 100%", f"<p>Use JK flip-flops and external gates to design a 3-bit synchronous state machine{' with two modes depending on its initial state' if len(cycles) > 1 else ''}.{modes}</p><p>One circuit block. Show the state table, logic functions and logic diagram.</p>", cs, src="Topics 3, 5, 7", answer=" · ".join(M(f"{k} = {v}") for k, v in R["eq"].items())),
             item(key + "-4a", "Q4(a) · 40%", img(key + "-q4", "Fig. 2") + f"<p>Asynchronous circuit, inputs A and B, internal state y, output {M('z = ' + z)}. Derive the transition table and show it on a Karnaugh map.</p>", qa, src="Topic 9", answer=M("Y = " + Y)),
             item(key + "-4b", "Q4(b) · 20%", "<p>Obtain a flow table for the circuit.</p>", qb, src="Topic 9", answer="see table"),
             item(key + "-4c", "Q4(c) · 40%", "<p>Check whether there is a stability issue. If so, explain where.</p>", qc, src="Topic 9", answer=("Oscillates when AB = " + ", ".join(bits(info[0][i], 2) for i in info[2])) if info[2] else "No stability issue"),
         ])


mock("mA", "Mock exam A", ("OR", ("NOR", "X", "Y"), ("NAND", ("OR", ("NOT", "X"), "Z"), "Y")), "NAND", (3, "D", False),
     "D(A'B + AC) + B'D'", "A'BD + ACD + B'D'", [[0, 2, 3, 6, 5], [1, 4, 7]] if False else [[2, 0, 5, 3, 6], [7, 1, 4]],
     "A'B + By", "Ay'", ("OR", ("AND", ("NOT", "A"), "B"), ("AND", "B", "y")), None)
mock("mB", "Mock exam B", ("AND", ("NAND", "X", "Z"), ("OR", ("NOT", "Y"), ("AND", "X", ("NOT", "Z")))), "NOR", (4, "T", True),
     "A(B'+CD') + A'D(B+C')", "AB' + ACD' + A'BD + A'C'D", [[0, 3, 5, 6], [7, 4, 2, 1]],
     "AB + (A^B)y'", "A + y", ("OR", ("AND", "A", "B"), ("AND", ("XOR", "A", "B"), ("NOT", "y"))), (1.6, "MHz"))

# =====================================================================
# MORE PRACTICE tab
# =====================================================================
part(id="more-info", kind="info", tab="more", title="What is here and why", html=f"""
<p>There are <b>no homework sheets</b> for this module, so this tab holds what was left off the exam path.</p>
{table(["Left off the exam path", "Why", "Where"], [
 ["Multiplexers", "Not on the 23/24 paper. Lecturer hinted it may be this year's combinational question.", "below"],
 ["Sequence detectors (Mealy / Moore)", "Not on the 23/24 paper. Biggest topic in Lectures 14–16, so a likely swap for the counter question.", "below"],
 ["Analysing a clocked circuit", "Not on the paper. Short, and it is design backwards.", "below"],
 ["Registers, ring and Johnson counters", "Not on the paper.", "<a href='https://github.com/albinjoby82-ops/DE_Lock-In/blob/main/notes/17-registers.md'>notes 17</a>"],
 ["Memory, programmable logic, transistor logic", "Not on the paper. Facts only.", "<a href='https://github.com/albinjoby82-ops/DE_Lock-In/blob/main/notes/18-memory.md'>18</a>, <a href='https://github.com/albinjoby82-ops/DE_Lock-In/blob/main/notes/19-programmable-logic.md'>19</a>, <a href='https://github.com/albinjoby82-ops/DE_Lock-In/blob/main/notes/21-transistor-logic.md'>21</a>"],
 ["Races (critical / non-critical)", "Q4 had one state variable, so no race was possible. Know the definitions.", "<a href='https://github.com/albinjoby82-ops/DE_Lock-In/blob/main/notes/20-asynchronous-logic.md'>notes 20 §4</a>"],
 ["Number systems, Boolean algebra drills, adders, decoders", "Mid-term material. Only K-maps, minterms and NAND carried into the final paper.", "<a href='../index.html'>mid-term site</a>"]])}
<p>More drill on K-maps and NAND: the <a href="../index.html">mid-term quiz site</a> (Topics 7, 8, 9) and the 375 worked <a href="../index.html#book-questions">Mano book questions</a>.</p>""")

# --- multiplexers
def mux_rows(ms, nsel, d="D"):
    rows, data = [], []
    for i in range(1 << nsel):
        a, b = int(2 * i in ms), int(2 * i + 1 in ms)
        v = {(0, 0): "0", (0, 1): d, (1, 0): d + "'", (1, 1): "1"}[(a, b)]
        data.append(v)
        rows.append([bits(i, nsel), f"I<sub>{i}</sub>", f"m<sub>{2*i}</sub> = {a}", f"m<sub>{2*i+1}</sub> = {b}", "<b>" + v + "</b>"])
    return rows, data


def mux_item(id, title, names, ms):
    nsel = len(names) - 1
    rows, data = mux_rows(ms, nsel, names[-1])
    sel = ", ".join(names[:-1])
    return item(id, title, "<p>Implement $F(" + ", ".join(names) + ") = " + sigma(ms) + f"$ with one {1 << nsel}-to-1 multiplexer.</p>",
                [[f"{len(names)} variables but only {nsel} select lines. Put {sel} on the selects. The last variable, {names[-1]}, goes to the data inputs.", "A mux with n selects can do a function of n + 1 variables, because each data input can be 0, 1, the last variable or its inverse."],
                 [f"Each select value covers two rows of the truth table: {names[-1]} = 0 and {names[-1]} = 1. Compare F on that pair:" + table(["".join(names[:-1]), "Input", f"{names[-1]} = 0", f"{names[-1]} = 1", "Connect"], rows),
                  f"Pair 0,0 → F is 0 whatever {names[-1]} is. Pair 1,1 → 1. Pair 0,1 → F copies {names[-1]}. Pair 1,0 → F is the inverse."],
                 ["Data inputs I₀ … : " + ", ".join(data), "One NOT gate makes the inverted variable if it is needed."]],
                src="Lecture 10 · lecturer hinted", answer=", ".join(data))


part(id="h1", kind="topic", tab="more", title="H1 · Multiplexers (lecturer hinted)", freq="Not on 23/24 paper",
     learn=f"""<p>A <b>multiplexer</b> is a switch: the <b>select</b> lines pick which <b>data</b> input reaches the output.</p>
{img(ex("mux4-block"), "4-to-1 mux", True)}
<p><b>Any function of n + 1 variables fits on a mux with n selects:</b></p>
<ol><li>First n variables → select lines.</li><li>For each select value, look at F when the last variable is 0 and when it is 1.</li><li>Connect that data input to <b>0, 1, the variable, or its inverse</b>.</li></ol>
{table(["F for last variable = 0, 1", "Connect"], [["0, 0", "0"], ["0, 1", "D"], ["1, 0", "D'"], ["1, 1", "1"]], "tt small")}""",
     check=dict(q="How many variables can one 8-to-1 mux implement?", a="<b>4.</b> Three on the selects, the fourth on the data inputs."),
     items=[mux_item("h1-1", "H1.1 8-to-1 mux", ABCD, [0, 1, 3, 4, 8, 9, 15]), mux_item("h1-2", "H1.2 4-to-1 mux", XYZ, [1, 2, 4, 7]), mux_item("h1-3", "H1.3 8-to-1 mux", ABCD, [2, 3, 5, 6, 8, 11, 12, 13, 14])])

# --- sequence detectors (checked against the engine)
from final_engine import mincover as _mc


def detector(pat):
    n = len(pat)
    T = {}
    for k in range(n):
        for x in "01":
            s = pat[:k] + x
            outv = int(s == pat)
            while not (pat.startswith(s) and len(s) < n):
                s = s[1:]
            T[(k, int(x))] = (len(s), outv)
    return T


def det_item(id, title, pat, kind):
    T = detector(pat)
    ns = len(pat)
    names = ["Q1", "Q0", "X"]
    lab = "ABCD"
    means = ["nothing"] + ["have " + pat[:k] for k in range(1, ns)]
    rows, onD, onJ, dcJ, onK, dcK, Z = [], {1: [], 0: []}, {1: [], 0: []}, {1: [], 0: []}, {1: [], 0: []}, {1: [], 0: []}, []
    used = set()
    for k in range(ns):
        for x in (0, 1):
            nk, o = T[(k, x)]
            m = (k << 1) | x
            used.add(m)
            if o:
                Z.append(m)
            cells = []
            for bit in (1, 0):
                q, qn = (k >> bit) & 1, (nk >> bit) & 1
                if qn:
                    onD[bit].append(m)
                if q == 0:
                    dcK[bit].append(m)
                    if qn:
                        onJ[bit].append(m)
                else:
                    dcJ[bit].append(m)
                    if not qn:
                        onK[bit].append(m)
                cells.append({(0, 0): "0 x", (0, 1): "1 x", (1, 0): "x 1", (1, 1): "x 0"}[(q, qn)])
            rows.append([f"{lab[k]} {bits(k, 2)}", x, f"{lab[nk]} {bits(nk, 2)}", o] + (cells if kind == "JK" else []))
    dc = [m for m in range(8) if m not in used]

    def eqn(on, d):
        if not on:
            return "0"
        if set(on) | set(d) == set(range(8)):
            return "1"
        return cover_tex(_mc(3, on, d), names)

    if kind == "JK":
        eqs = {f"J{b}": eqn(onJ[b], dcJ[b] + dc) for b in (1, 0)}
        eqs.update({f"K{b}": eqn(onK[b], dcK[b] + dc) for b in (1, 0)})
    else:
        eqs = {f"D{b}": eqn(onD[b], dc) for b in (1, 0)}
    eqs["Z"] = eqn(Z, dc)
    # simulate to verify against a brute-force detector
    import random
    random.seed(7)
    for _ in range(300):
        s = "".join(random.choice("01") for _ in range(24))
        q1 = q0 = 0
        for i, ch in enumerate(s):
            env = {"Q1": q1, "Q0": q0, "X": int(ch)}
            assert ev(eqs["Z"], env) == int(s[max(0, i - ns + 1):i + 1] == pat), (pat, s, i)
            if kind == "JK":
                n1 = int((ev(eqs["J1"], env) and not q1) or (not ev(eqs["K1"], env) and q1))
                n0 = int((ev(eqs["J0"], env) and not q0) or (not ev(eqs["K0"], env) and q0))
            else:
                n1, n0 = ev(eqs["D1"], env), ev(eqs["D0"], env)
            q1, q0 = n1, n0
    head = ["Present", "X", "Next", "Z"] + ([M("J1") + " " + M("K1"), M("J0") + " " + M("K0")] if kind == "JK" else [])
    fb = "".join(f"<li>{lab[k]} = {means[k]}</li>" for k in range(ns))
    steps = [
        [f"States = how much of {pat} you have so far:<ul>{fb}</ul>", "A detector only needs to remember the useful tail of the input. " + str(ns) + " states → 2 flip-flops."],
        ["Happy path first: " + " → ".join(f"{lab[k]} —{pat[k]}→" for k in range(ns - 1)) + f" {lab[ns-1]}, and from {lab[ns-1]} the bit {pat[-1]} completes the pattern (Z = 1).", "Draw the arrows that follow the pattern before worrying about anything else."],
        ["Every other arrow: go to the state for the <b>longest ending of the input that is still a start of the pattern</b>. State table:" + table(head[:4], [r[:4] for r in rows]),
         "After a wrong bit you rarely go all the way back. After a match, the last bits may already start the next match (overlap)."],
    ]
    if kind == "JK":
        steps.append(["Add the J K columns from the excitation table:" + table(head, rows), "Present bit 0 → J = next bit, K = x. Present bit 1 → K = opposite of next bit, J = x."])
    else:
        steps.append(["With D flip-flops, D = next state. The Next column <b>is</b> D₁D₀.", "Q⁺ = D, so there is no excitation step."])
    steps.append(["K-map each column (variables Q₁, Q₀, X" + (f"; code {bits(dc[0] >> 1, 2)} is unused → don't care" if dc else "") + "):" + "".join(DD(f"{k} = {v}") for k, v in eqs.items()),
                  "Unused state codes can never occur, so they are x in every map."])
    return item(id, title, f"<p>Design a Mealy circuit with input X and output Z. Z = 1 when the last {ns} inputs were <b>{pat}</b> (overlap allowed). Use {kind} flip-flops.</p>", steps,
                src="Lectures 14–16 · not on 23/24 paper", answer=" · ".join(M(f"{k} = {v}") for k, v in eqs.items()))


part(id="h2", kind="topic", tab="more", title="H2 · Sequence detectors (likely swap for Q3)", freq="Not on 23/24 paper",
     learn=f"""<p>Same design steps as Topic 7, but now there is an <b>input X</b>, so every state has <b>two</b> arrows out (X = 0 and X = 1), and an output Z.</p>
{img("../svg/seq/fsm-1001-mealy.svg", "1001 detector", True)}
{table(["", "Output depends on", "Drawn"], [["<b>Mealy</b>", "state and input", "on the arrow: input / output"], ["<b>Moore</b>", "state only", "in the circle. Needs one more state."]])}
<p><b>Rule for the diagram:</b> each state = how much of the pattern you have. On any bit, go to the state for the <b>longest ending that is still a start of the pattern</b>.</p>
<p>Then: state table → codes → excitation table → K-maps (variables Q₁, Q₀, X) → circuit.</p>""",
     check=dict(q="Detecting 110. You have 11 and another 1 arrives. Which state next?", a="<b>Stay in \"have 11\".</b> The input ends in 111, and its last two bits are still 11."),
     items=[det_item("h2-1", "H2.1 Detect 101 (JK)", "101", "JK"), det_item("h2-2", "H2.2 Detect 110 (D)", "110", "D"), det_item("h2-3", "H2.3 Detect 1001 (JK)", "1001", "JK")])

# --- analysis
an_rows = []
for m in range(8):
    A, B, x = (m >> 2) & 1, (m >> 1) & 1, m & 1
    env = {"A": A, "B": B, "x": x}
    JA, KA, JB, KB = ev("B", env), ev("Bx'", env), ev("x'", env), ev("A^x", env)
    nA = int((JA and not A) or (not KA and A))
    nB = int((JB and not B) or (not KB and B))
    an_rows.append([f"{A} {B}", x, f"{JA} {KA}", f"{JB} {KB}", f"<b>{nA} {nB}</b>"])
part(id="h3", kind="topic", tab="more", title="H3 · Analysing a clocked circuit", freq="Not on 23/24 paper",
     learn=f"""<p><b>Analysis</b> = design backwards: circuit → equations → state table → state diagram.</p>
<ol><li>Read the equation for each flip-flop input (and the output).</li><li>List every present state and input. Work out the flip-flop inputs on each row.</li><li>Use the characteristic table to get the next state (JK: 00 hold, 01 reset, 10 set, 11 toggle).</li></ol>
<p>Check: n flip-flops → 2ⁿ circles, and with one input, 2 arrows leave every circle.</p>""",
     check=dict(q="Present Q = 1, J K = 1 1. Next Q?", a="<b>0.</b> 11 toggles."),
     items=[item("h3-1", "H3.1 JK circuit", f"<p>Two JK flip-flops A and B, input x: {M('JA = B')}, {M('KA = Bx' + chr(39))}, {M('JB = x' + chr(39))}, {M('KB = A ^ x')}. Derive the state table.</p>",
                 [["8 rows: every present state A B with x = 0 and 1.", "2 flip-flops + 1 input = 2³ combinations."],
                  ["Work out J and K for each flip-flop from the <b>present</b> state, then apply the JK action:" + table(["A B", "x", M("JA") + " " + M("KA"), M("JB") + " " + M("KB"), "A⁺ B⁺"], an_rows),
                   "Example row 0 1, x = 0: J K for A = 1 1 → toggle → 1. J K for B = 1 0 → set → 1. Next state 1 1."],
                  ["State diagram: 4 circles, arrows labelled with x. 00 —0→ 01, 00 —1→ 00, 01 —0→ 11, 01 —1→ 10, 10 —0→ 11, 10 —1→ 10, 11 —0→ 00, 11 —1→ 11.", "One arrow per table row."]],
                 src="Lecture 13 style", answer="see table")])

# =====================================================================
total = sum(len(p.get("items", [])) for p in PARTS)
data = dict(version=VERSION, module="EEEN20050 Digital Electronics", parts=PARTS)
with open(os.path.join(OUT, "data.js"), "w", encoding="utf8") as f:
    f.write("window.LOCKIN = " + json.dumps(data, ensure_ascii=False) + ";\n")
with open(os.path.join(OUT, "version.json"), "w", encoding="utf8") as f:
    json.dump({"version": VERSION}, f)
print("parts", len(PARTS), "questions", total, "figures", len(os.listdir(FIG)))
