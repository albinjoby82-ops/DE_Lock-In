"""Shared state for the final-exam site: the study path, the papers, and the
worked 23/24 paper (computed once, used inside topics and as a paper)."""
from final_more import *

PATH, PAPERS = [], []
_cur = {"parts": PATH}
XYZ, ABC, ABCD = list("XYZ"), list("ABC"), list("ABCD")


def use(target):
    _cur["parts"] = target


def part(title):
    _cur["parts"].append(dict(title=title, topics=[]))


def topic(id, title, src, learn="", check=None, pri=0):
    t = dict(id=id, title=title, src=src, learn=learn, check=dict(q=check[0], a=check[1]) if check else None, pri=pri, qs=[])
    _cur["parts"][-1]["topics"].append(t)
    return t


def mk(prompt, steps, a):
    return dict(q=prompt, steps=[{"b": x[0], "why": x[1]} for x in steps], a=a)


def q(id, ref, prompt, steps, a, sim=None, page=False):
    it = dict(id=id, ref=ref, **mk(prompt, steps, a))
    if sim:
        it["sim"] = mk(*sim)
    if page:
        it["page"] = True
    _cur["parts"][-1]["topics"][-1]["qs"].append(it)
    return it


def put(item):
    """Show an existing item (an exam part) inside the current topic as well."""
    _cur["parts"][-1]["topics"][-1]["qs"].append(item)


def ex(n):
    return f"../svg/{n}.svg"


def seq(n):
    return f"../svg/seq/{n}.svg"


ET = table(["Q → Q<sup>+</sup>", "J K", "D", "T"], [["0 → 0", "0 x", "0", "0"], ["0 → 1", "1 x", "1", "1"], ["1 → 0", "x 1", "0", "1"], ["1 → 1", "x 0", "1", "0"]])

# ===================================================================== the 23/24 paper
P1 = ("OR", ("AND", ("NOT", "X"), ("NOT", "Y")), ("NAND", ("OR", "X", "Y"), ("NOT", "Z")))
draw_tree("pp-q1", P1, "F", title="Fig. 1")
pp1a = p_function(P1)
pp1a.append(["Optional tidy-up with De Morgan:" + DD("((X+Y)Z')' = (X+Y)' + Z = X'Y' + Z") + DD("F = X'Y' + X'Y' + Z = X'Y' + Z"),
             "Not required for part (a), but it makes the truth table quicker and it must match what the K-map gives in part (d)."])
pp1b, P1ms = p_truth(P1, XYZ, "pp-q1")
pp1c = [["From Q1(b), F = 1 on rows 0, 1, 3, 5, 7.", "The truth table already has everything. Part (c) is just reading it."]] + p_minmax(P1ms, XYZ)
pp1d_s, P1cov = p_simplify(P1ms, XYZ, "pp-q1")
pp1d = pp1d_s + p_nand(P1cov, XYZ, "pp-q1")
assert P1ms == [0, 1, 3, 5, 7]
pp2a = p_ripple(3, "D", True, "pp-q2a")
PP2B = "AB'(D'+CD) + A'(B+CD) + A'CD'"
pp2b_h, pp2b_ans = p_hazard(PP2B, ABCD, "pp-q2b", expanded="AB'D' + AB'CD + A'B + A'CD + A'CD'")
pp2b = [["Cause: the same input reaches the output by <b>two paths with different delays</b> (for example one goes through an inverter). When that input changes, one product term turns off slightly before another turns on, and the output glitches for a moment.",
         "Static-1 hazard: output should stay 1 but dips to 0. Static-0: should stay 0 but pulses to 1. It happens when two neighbouring K-map cells are covered by different groups."]] + pp2b_h
pp3, PP3R = p_counter([[3, 1, 2, 0, 4], [7, 6, 5]], ABC, "pp-q3", twomode=True)
pp3.insert(8, ["Fewest gates: spot the single-gate forms." + DD("JA = KA = B'C' = (B+C)' \\;\\text{(one NOR)}") + DD("KB = A' + C' = (AC)' \\;\\text{(one NAND)}") + DD("KC = AB + A'B' = (A ^ B)' \\;\\text{(one XNOR)}") + "<p>Total: NOR, OR, NAND, XNOR = <b>4 gates</b>. J<sub>C</sub> = A is just a wire.</p>",
               "The question asks for the minimum number of external gates. De Morgan turns two-term sums of inverted letters into one NAND or NOR, and J<sub>A</sub> and K<sub>A</sub> share the same gate."])
draw_tree("pp-q4", ("OR", ("AND", "A", "B"), ("AND", "A", ("NOT", "y"))), "Y", feedback="y", title="Fig. 2")
pp4a, pp4b, pp4c, PP4 = p_async("AB + Ay'", "A + Y", ["A", "B"], "pp-q4")
pp4a[0][0] += "<p>(z comes from the top OR gate: inputs A and Y.)</p>"
pp4b.append(["Notice z = A + Y = A here.", "Y = A(B + y') can only be 1 when A is 1, so OR-ing it with A adds nothing. The output simply follows A."])


def xq(id, ref, prompt, steps, a):
    return dict(id=id, ref=ref, **mk(prompt, steps, a))


EQ3 = lambda R: " · ".join(M(f"{k} = {v}") for k, v in R["eq"].items())
EX = {
    "pp-1a": xq("pp-1a", "Exam 23/24 · Q1(a) · 10%", img("pp-q1", "Fig. 1") + "<p>Write a Boolean logic function relating the inputs X, Y, Z and the output F.</p>", pp1a, M("F = X'Y' + ((X+Y)Z')' = X'Y' + Z")),
    "pp-1b": xq("pp-1b", "Exam 23/24 · Q1(b) · 30%", img("pp-q1", "Fig. 1") + "<p>Draw the Karnaugh map and the truth table of the logic circuit.</p>", pp1b, "F = 1 on rows 0, 1, 3, 5, 7"),
    "pp-1c": xq("pp-1c", "Exam 23/24 · Q1(c) · 20%", img("pp-q1", "Fig. 1") + "<p>Express the function as a sum of minterms and as a product of maxterms, shorthand format.</p>", pp1c, "$" + sigma(P1ms) + " = " + pi([2, 4, 6]) + "$"),
    "pp-1d": xq("pp-1d", "Exam 23/24 · Q1(d) · 40%", img("pp-q1", "Fig. 1") + "<p>Simplify using the Karnaugh map and implement with two-level NAND gates. NOT gates can be used.</p>", pp1d, M("F = X'Y' + Z = ((X'Y')' \\cdot Z')'")),
    "pp-2a": xq("pp-2a", "Exam 23/24 · Q2(a) · 60%", "<p>Design a three-bit binary ripple count-down counter using D flip-flops. Show the logic diagram, draw the output waveforms and briefly explain how this circuit can be used as a frequency divider.</p>", pp2a, "D = Q' on each flip-flop, each stage clocked by the previous Q, outputs at f/2, f/4, f/8"),
    "pp-2b": xq("pp-2b", "Exam 23/24 · Q2(b) · 40%", f"<p>Briefly explain what causes static hazards in digital circuits. Implement without static-1 hazards, using a minimum number of gates:</p>{DD('F(A,B,C,D) = ' + PP2B)}", pp2b, M("F = " + pp2b_ans)),
    "pp-3": xq("pp-3", "Exam 23/24 · Q3 · 100%", "<p>Use JK flip-flops and external gates to design a 3-bit synchronous binary state machine with two modes of operation depending on its initial state.</p><p><b>Mode 1:</b> 011 → 001 → 010 → 000 → 100 → back to 011.<br><b>Mode 2:</b> 111 → 110 → 101 → back to 111.</p><p>No external control. Both modes must use ONE circuit block. Show the design procedure, state table, logic functions and logic diagram. Minimum flip-flops and external gates.</p>", pp3, EQ3(PP3R)),
    "pp-4a": xq("pp-4a", "Exam 23/24 · Q4(a) · 40%", img("pp-q4", "Fig. 2") + "<p>Two inputs A and B, one internal state y, one output z (top OR gate: z = A + Y). Derive the transition table and show it on a Karnaugh map.</p>", pp4a, M("Y = AB + Ay'")),
    "pp-4b": xq("pp-4b", "Exam 23/24 · Q4(b) · 20%", img("pp-q4", "Fig. 2") + "<p>Obtain a flow table for the circuit.</p>", pp4a[:2] + pp4b, "a = y 0, b = y 1. See the table in the last step."),
    "pp-4c": xq("pp-4c", "Exam 23/24 · Q4(c) · 40%", img("pp-q4", "Fig. 2") + "<p>Check whether there is a stability issue. If so, explain where the instability can occur.</p>", pp4a[1:3] + pp4c, "Yes: it oscillates when AB = 10"),
}
