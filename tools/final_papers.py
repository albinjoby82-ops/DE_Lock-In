"""Exam papers: the real 23/24 paper, two mocks in its shape, one mock in the
lecturer's hinted shape (1 combinational + 4 sequential)."""
from final_site import *

use(PAPERS)
RULES = """<p><b>Rules:</b> 120 minutes · answer every question · equal marks · non-programmable calculator · no formula sheet, so the flip-flop tables must be in your head.</p>
<p>Do the whole paper on paper against the clock <b>before</b> revealing anything. The percentages show the weight of each part inside its question.</p>"""


def qt(n, what, first=False):
    topic(f"{_pid[0]}-q{n}", f"Question {n}", what, learn=RULES if first else "")["label"] = "Rules"


_pid = [""]

# ----------------------------------------------------------------- the real paper
part("Autumn 23/24 · the real paper")
_pid[0] = "pp"
qt(1, "Combinational logic · 25% · 30 minutes", True)
for k in ("pp-1a", "pp-1b", "pp-1c", "pp-1d"):
    put(EX[k])
qt(2, "Ripple counter and hazards · 25% · 30 minutes")
put(EX["pp-2a"])
put(EX["pp-2b"])
qt(3, "Synchronous state machine · 25% · 30 minutes")
put(EX["pp-3"])
qt(4, "Asynchronous circuit · 25% · 30 minutes")
for k in ("pp-4a", "pp-4b", "pp-4c"):
    put(EX[k])


# ----------------------------------------------------------------- mocks in the same shape
def mock(mid, title, tree, twolevel, rip, haz, hazexp, cycles, Y, z, ytree, f0):
    part(title)
    _pid[0] = mid
    draw_tree(mid + "-q1", tree, "F", title="Fig. 1")
    a = p_function(tree)
    b, ms = p_truth(tree, XYZ, mid + "-q1")
    c = p_minmax(ms, XYZ)
    d, cov = p_simplify(ms, XYZ, mid + "-q1")
    if twolevel == "NAND":
        d += p_nand(cov, XYZ, mid + "-q1")
        d_ans = M("F = " + cover_tex(cov, XYZ))
    else:
        d1, pos = p_nor(ms, XYZ, mid + "-q1")
        d += d1
        d_ans = M("F = " + pos)
    n, kind, down = rip
    r = p_ripple(n, kind, down, mid + "-q2a", f0=f0)
    assert minterms(hazexp, ABCD) == minterms(haz, ABCD)
    h, hans = p_hazard(haz, ABCD, mid + "-q2b", expanded=hazexp)
    h = [["Cause: one input reaches the output by two paths with different delays. When it changes, one product term switches off before the next switches on, and the output glitches.", "It shows on the K-map as two neighbouring 1s that sit in different groups."]] + h
    cs, R = p_counter(cycles, ABC, mid + "-q3", twomode=len(cycles) > 1)
    draw_tree(mid + "-q4", ytree, "Y", feedback="y", title="Fig. 2")
    qa, qb, qc, info = p_async(Y, z, ["A", "B"], mid + "-q4")
    md = "".join(f"<br><b>Mode {i+1}:</b> " + " → ".join(bits(x, 3) for x in cyc) + f" → back to {bits(cyc[0], 3)}." for i, cyc in enumerate(cycles))
    f1, f4 = img(mid + "-q1", "Fig. 1"), img(mid + "-q4", "Fig. 2")
    qt(1, "Combinational logic · 25% · 30 minutes", True)
    q(mid + "-1a", "Q1(a) · 10%", f1 + "<p>Write a Boolean function relating X, Y, Z and F.</p>", a, M("F = " + T_tex(tree)))
    q(mid + "-1b", "Q1(b) · 30%", f1 + "<p>Draw the Karnaugh map and the truth table.</p>", b, "F = 1 on rows " + ", ".join(map(str, ms)))
    q(mid + "-1c", "Q1(c) · 20%", f1 + "<p>Express F as a sum of minterms and as a product of maxterms (shorthand).</p>", [[f"From (b), F = 1 on rows {', '.join(map(str, ms))}.", "Part (c) is read straight off the truth table."]] + c, "$" + sigma(ms) + " = " + pi([m for m in range(8) if m not in ms]) + "$")
    q(mid + "-1d", "Q1(d) · 40%", f1 + f"<p>Simplify with the K-map and implement with two-level <b>{twolevel}</b> gates. NOT gates can be used.</p>", d, d_ans)
    qt(2, "Ripple counter and hazards · 25% · 30 minutes")
    q(mid + "-2a", "Q2(a) · 60%", f"<p>Design a {['', '', 'two', 'three', 'four'][n]}-bit binary ripple count-<b>{'down' if down else 'up'}</b> counter using {kind} flip-flops. Show the logic diagram, draw the output waveforms, and explain how it works as a frequency divider"
      + (f". If the clock is {f0[0]} {f0[1]}, what frequency is at each output?" if f0 else ".") + "</p>", r, "See the diagram and waveforms in the steps.")
    q(mid + "-2b", "Q2(b) · 40%", f"<p>Explain what causes static hazards. Implement without static-1 hazards, minimum gates:</p>{DD('F(A,B,C,D) = ' + haz)}", h, M("F = " + hans))
    qt(3, "Synchronous state machine · 25% · 30 minutes")
    q(mid + "-3", "Q3 · 100%", f"<p>Use JK flip-flops and external gates to design a 3-bit synchronous state machine{' with two modes depending on its initial state' if len(cycles) > 1 else ''}.{md}</p><p>One circuit block. Show the state table, logic functions and logic diagram.</p>", cs, EQ3(R))
    qt(4, "Asynchronous circuit · 25% · 30 minutes")
    q(mid + "-4a", "Q4(a) · 40%", f4 + f"<p>Asynchronous circuit, inputs A and B, internal state y, output {M('z = ' + z)}. Derive the transition table and show it on a Karnaugh map.</p>", qa, M("Y = " + Y))
    q(mid + "-4b", "Q4(b) · 20%", f4 + "<p>Obtain a flow table for the circuit.</p>", qa[:2] + qb, "See the table in the last step.")
    q(mid + "-4c", "Q4(c) · 40%", f4 + "<p>Check whether there is a stability issue. If so, explain where.</p>", qa[1:3] + qc, ("Oscillates when AB = " + ", ".join(bits(info[0][i], 2) for i in info[2])) if info[2] else "No stability issue")


mock("mA", "Mock A · same shape as 23/24", ("OR", ("NOR", "X", "Y"), ("NAND", ("OR", ("NOT", "X"), "Z"), "Y")), "NAND", (3, "D", False),
     "D(A'B + AC) + B'D'", "A'BD + ACD + B'D'", [[2, 0, 5, 3, 6], [7, 1, 4]],
     "AB' + By", "A'y", ("OR", ("AND", "A", ("NOT", "B")), ("AND", "B", "y")), None)
mock("mB", "Mock B · same shape as 23/24", ("AND", ("NAND", "X", "Z"), ("OR", ("NOT", "Y"), ("AND", "X", ("NOT", "Z")))), "NOR", (4, "T", True),
     "A(B'+CD') + A'D(B+C')", "AB' + ACD' + A'BD + A'C'D", [[0, 3, 5, 6], [7, 4, 2, 1]],
     "AB + (A^B)y'", "A + y", ("OR", ("AND", "A", "B"), ("AND", ("XOR", "A", "B"), ("NOT", "y"))), (1.6, "MHz"))

# ----------------------------------------------------------------- mock in the hinted shape
part("Mock C · 5 questions, 1 combinational + 4 sequential")
_pid[0] = "mC"
RC = RULES.replace("equal marks", "equal marks → about <b>24 minutes each</b>")
topic("mC-q1", "Question 1", "Multiplexers · 20%", learn=RC)["label"] = "Rules"
m1, a1 = p_mux(ABCD, [0, 2, 5, 6, 7, 9, 12, 13])
q("mC-1a", "Q1(a) · 70%", "<p>Implement $F(A, B, C, D) = " + sigma([0, 2, 5, 6, 7, 9, 12, 13]) + "$ using one 8-to-1 multiplexer.</p>", m1, a1)
q("mC-1b", "Q1(b) · 30%", "<p>How many 2-to-1 multiplexers are needed to build an 8-to-1 multiplexer? Which select line goes to which level?</p>",
  [["8 inputs → 4 muxes, then 2, then 1: <b>7</b>.", "Each level halves the number of lines."], ["Level 1 uses the lowest select S<sub>0</sub>, level 2 uses S<sub>1</sub>, the last mux uses S<sub>2</sub>.", "The low bit chooses within a pair, the high bit chooses between halves."]], "7")
topic("mC-q2", "Question 2", "Flip-flops and analysis · 20%")
s2, _ = p_analysis("D", [("A", "Ax' + Bx"), ("B", "A'x + Bx'")], "AB'x", "mC-q2")
s2.append(["It holds when x = 0. When x = 1 it steps 00 → 01 → 11 → 10 → 00: a Gray-code counter with an enable. z = 1 on the arrow 10 → 00, so it flags the wrap-around. z contains x, so the circuit is <b>Mealy</b>.", "Only one bit changes at each step, which is what Gray code means."])
q("mC-2a", "Q2(a) · 30%", "<p>Give the characteristic table and characteristic equation of a JK flip-flop, and explain the difference between a latch and a flip-flop.</p>",
  [["JK: 00 → Q (hold) · 01 → 0 (reset) · 10 → 1 (set) · 11 → Q' (toggle)." + DD("Q^+ = JQ' + K'Q"), "J sets, K resets, both together toggle."],
   ["A latch is <b>level</b> triggered: it is open for the whole time its enable is 1, so the output can change several times. A flip-flop is <b>edge</b> triggered: it samples only at the clock transition (two latches, master and slave, on opposite clock levels).", "That single sampling instant is what makes synchronous design predictable."]], M("Q^+ = JQ' + K'Q"))
q("mC-2b", "Q2(b) · 70%", f"<p>A sequential circuit has two D flip-flops A and B, an input x and an output z:</p>{DD('DA = Ax' + chr(39) + ' + Bx')}{DD('DB = A' + chr(39) + 'x + Bx' + chr(39))}{DD('z = AB' + chr(39) + 'x')}<p>Derive the state table, draw the state diagram, and say what the circuit does. Moore or Mealy?</p>", s2, "A Gray-code counter with enable x. Mealy.")
topic("mC-q3", "Question 3", "Sequence detector · 20%")
s3, R3, a3 = p_detector(["0110"], "JK", "mC-q3", sample="01101100110")
q("mC-3", "Q3 · 100%", "<p>Design a Mealy circuit with one input X and one output Z. Z = 1 when the last four inputs were <b>0110</b>. Overlapping sequences must be detected. Use JK flip-flops. Show the state diagram, state table, flip-flop input functions and the output function.</p>", s3, a3)
topic("mC-q4", "Question 4", "Counter design · 20%")
s4, R4 = p_counter([[0, 1, 3, 2, 6, 7]], ABC, "mC-q4")
q("mC-4", "Q4 · 100%", "<p>Design a synchronous counter that goes through the states 000 → 001 → 011 → 010 → 110 → 111 → back to 000, using JK flip-flops. Check what happens from the unused states.</p>", s4, EQ3(R4))
topic("mC-q5", "Question 5", "Registers and asynchronous logic · 20%")
J5 = johnson(3)
q("mC-5a", "Q5(a) · 30%", "<p>A 3-bit Johnson counter starts at 000. Write its sequence of states. How many flip-flops would a ring counter need for the same number of states?</p>",
  [["Shift right, feeding the inverse of the last bit into the first: " + " → ".join(J5) + " → 000.", "It fills with 1s, then with 0s."], ["6 states from 3 flip-flops (2k). A ring counter gives one state per flip-flop, so it needs <b>6</b>.", "Johnson: 2k states. Ring: k states."]], "6 states · ring counter needs 6 flip-flops")
F5 = p_flow2circ([[(0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (1, 1), (1, 1), (0, 0)]], "mC-q5")
q("mC-5b", "Q5(b) · 40%", "<p>Derive the logic circuit for this flow table (states a and b, inputs x<sub>1</sub>x<sub>2</sub>, output z).</p>" + F5[0], F5[1], F5[2])
r5, ra = p_race({0: 3, 1: 1, 3: 3, 2: 3})
tab5 = {(0, 0): 0, (0, 1): 3, (1, 1): 1, (3, 1): 3, (2, 1): 3}
q("mC-5c", "Q5(c) · 30%", "<p>Explain the difference between a critical and a non-critical race. In this partial transition table the circuit is stable in 00 with x = 0 and x changes to 1. Which kind of race is it?</p>" + tt2(tab5),
  [["A race happens when two or more state variables must change after one input change. <b>Non-critical:</b> the final stable state is the same whichever changes first. <b>Critical:</b> the final state depends on the order.", "Unequal delays in the feedback paths decide the order, and you cannot control them."]] + r5, ra)
