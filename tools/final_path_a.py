"""Study path, parts 0 to 3: plan, combinational logic, flip-flops, clocked circuits."""
from final_site import *

use(PATH)

# ===================================================================== 0 · plan
part("Start here")
topic("plan", "The plan", "Built from the 2026/27 lecture slides (Lectures 1 to 25) and the Autumn 23/24 paper")
q("plan-1", "Read me first", f"""
<p><b>What this is.</b> Every final-exam topic in the order to study it. Each topic has a short <b>Notes</b> box that teaches it from zero, a check question, then questions with step-by-step solutions. The slide examples and exercises are in here as questions.</p>
<h3>What the exam should look like</h3>
<p>From a classmate's note of what the lecturer said: <b>5 questions. 1 on combinational logic (they think multiplexers). The other 4 on sequential logic.</b> It is second-hand ("I believe he said"), so treat it as likely, not certain.</p>
{table(["Question", "Most likely from", "Where"], [
 ["1 · combinational", "<b>Multiplexers</b>: put a function on a mux, build a big mux from small ones", "2.5, then 2.7 (back-up: 2.6 decoders, 2.3 K-maps)"],
 ["2 to 5 · sequential", "Flip-flops and analysing a clocked circuit (L11–13)", "Part 3, 4.1"],
 ["", "Sequence detectors, Mealy and Moore (L14–16)", "4.2 to 4.5"],
 ["", "Counters: synchronous, ripple, BCD (L17–18)", "Part 5"],
 ["", "Registers, ring and Johnson counters (L19–20)", "Part 6"],
 ["", "Asynchronous circuits: tables, races, hazards (L23–24)", "Part 7"]])}
<p>The slides have <b>five</b> sequential blocks and the exam has <b>four</b> sequential questions. So no block is safe to skip.</p>
<h3>The only past paper (Autumn 23/24)</h3>
<p>Set by a different lecturer: 4 questions, 30 minutes each. It is still the only real paper, so do it, but the 5-question shape comes first.</p>
{table(["Q", "Asked", "Where"], [
 ["1", "Circuit → function, truth table, K-map, Σm / ΠM, two-level NAND", "2.1 to 2.4"],
 ["2(a)", "3-bit ripple count-down counter with D flip-flops, waveforms, frequency divider", "5.2"],
 ["2(b)", "Cause of static hazards, hazard-free circuit", "7.5"],
 ["3", "Synchronous JK state machine with two count loops", "5.1"],
 ["4", "Asynchronous circuit: transition table, flow table, stability", "7.1"]])}
<h3>The path</h3>
{table(["Part", "Slides", "After it you can", "Priority"], [
 ["2 · Combinational logic", "L4–6, 9, 10", "put a function on a multiplexer or decoder, K-map it, build it from NAND / NOR, <b>design a circuit from a description in words</b>", "★★★ multiplexers, K-maps and design questions, ★★ the rest"],
 ["3 · Latches and flip-flops", "L11–12", "trace any latch or flip-flop, write the excitation table from memory", "★★★"],
 ["4 · Clocked circuits", "L13–16", "analyse a circuit, design a sequence detector (Mealy and Moore), <b>design any clocked circuit from words</b>", "★★★"],
 ["5 · Counters", "L17–18", "design any synchronous counter, build ripple and BCD counters", "★★★"],
 ["6 · Registers", "L19–20", "trace shift registers, serial adder, ring and Johnson counters", "★★★"],
 ["7 · Asynchronous logic", "L23–24", "transition and flow tables, stability, races, hazards", "★★★"],
 ["8 · Memory, PLDs, transistors", "L21, 22, 25", "sizes and facts: RAM, ROM, PAL / PLA, FPGA, CMOS gates", "★"]])}
<p>★★★ = fits the 5-question shape: multiplexers, or a main sequential-logic method. ★★ = a tool those questions use, or a smaller part of the same lectures. ★ = facts only, neither a combinational nor a sequential question.</p>
<h3>Design questions: what the exam really asks</h3>
<p>The real paper says <b>“Design a…”</b> three times. A design question gives you <b>words</b> and wants a <b>drawn circuit</b>. Knowing the ideas is not enough: you have to run the whole chain yourself, on paper.</p>
$$\\text{{words}} \\;\\to\\; \\text{{table}} \\;\\to\\; \\text{{K-map}} \\;\\to\\; \\text{{equation}} \\;\\to\\; \\text{{drawing}}$$
<ul><li><b>2.7</b> is the chain for gates, multiplexers and decoders. <b>4.5</b> is the chain for flip-flop circuits. Both start from a description in words.</li>
<li>Every design solution on this site now ends with the <b>logic diagram</b>: the gates and flip-flops as you would draw them in the exam.</li>
<li>Questions called <b>“Design in words”</b> are this type. Questions called <b>“More practice”</b> are extra goes at each topic.</li></ul>
<h3>How to study it</h3>
<ol><li><b>Paper first, always.</b> The exam is hand-written. Do the whole question on paper, <b>including the drawing</b>, before you reveal a step (Space = next step).</li>
<li>On a phone, <b>tap any diagram</b> to see it full size. Tap again to shrink it.</li>
<li><b>Go in order.</b> Parts 3 to 5 build on each other: flip-flop tables → state tables → counters.</li>
<li>Read the Notes box and answer the check before the first question of a topic.</li>
<li>Press <b>Similar question</b> (S) and do it again with new numbers. Mark <b>Got it</b> only if you could redo it from a blank page.</li>
<li>Questions in <b>bold</b> in the contents are the real 23/24 exam parts.</li>
<li>Finish with <b>Exam papers</b>: the two 5-question mocks first, then the real 23/24 paper.</li></ol>
<p><b>Short on time?</b> Do 2.5, 2.7, 3.3, 3.4, 4.1, 4.2, 4.3, 4.5, 5.1, 5.2, 6.2, 6.5, 7.1, then the 5-question mocks. That is multiplexers, the two design-question topics, and the main method from each of the five sequential blocks.</p>
<p><b>Homework 2</b> is due after the final (same note), so it can wait until the exam is done.</p>
<p><b>Not here:</b> number systems, binary arithmetic, codes and adders (Lectures 1 to 3, 7 to 8). They were the mid-term and are on the <a href="../index.html">mid-term site</a>.</p>
""", [], "", page=True)

# ===================================================================== 1 · combinational
part("Combinational logic")


def circ(key, tree, names=ABC):
    draw_tree(key, tree, "F")
    st = p_function(tree)
    tt, ms = p_truth(tree, names, key)
    st += tt[:2]
    st.append([demorgan_note(tree, names), "Use it as a check: the simplified form must give the same F column."])
    return (img(key, "circuit") + "<p>(a) Write the Boolean function F. (b) Give its truth table.</p>", st, M("F = " + T_tex(tree)) + " · $" + sigma(ms) + "$")


topic("c1", "Circuit → Boolean function → truth table", "Lecture 4 · 23/24 Q1(a), (b)", pri=2,
      learn=f"""<p>Every gate is a tiny rule. Read the circuit <b>left to right</b>, writing each gate's output on its wire.</p>
{img(ex("gates"), "gate symbols", True)}
{table(["Gate", "Output is 1 when…", "Written"], [["AND", "all inputs are 1", M("AB")], ["OR", "any input is 1", M("A+B")], ["NOT", "input is 0", M("A'")], ["NAND", "<b>not</b> all inputs are 1", M("(AB)'")], ["NOR", "<b>no</b> input is 1", M("(A+B)'")]])}
<p>A <b>bubble</b> (small circle) means "invert". De Morgan pushes a bar inside and swaps the operation:</p>
$$(AB)' = A' + B' \\qquad (A+B)' = A'B'$$
<p><b>Truth table:</b> n inputs → {M("2^n")} rows in counting order. Work out F for each row.</p>""",
      check=("A NAND gate has inputs 1 and 1. Output?", "<b>0.</b> AND gives 1, the bubble inverts it."))
q("t1-1", "Read a circuit", *circ("t1-1", ("OR", ("AND", "A", "B"), ("NOR", "B", "C"))), sim=circ("t1-2", ("NAND", ("OR", "A", ("NOT", "B")), "C")))
q("t1-3", "Three levels of gates", *circ("t1-3", ("OR", ("NAND", ("OR", "A", "B"), "C"), ("AND", ("NOT", "A"), "B"))), sim=circ("t1-4", ("NOR", ("AND", "A", ("NOT", "B")), ("AND", "B", "C"))))
put(EX["pp-1a"])
put(EX["pp-1b"])


def mm(e, names):
    ms = minterms(e, names)
    n = len(names)
    rows = [list(bits(m, n)) + [str(int(m in ms))] for m in range(1 << n)]
    st = [["Make the truth table:" + table(list(names) + ["F"], rows), "Row number in binary = the input values. Evaluate F on each row."]] + p_minmax(ms, names)
    return (f"<p>Express {M('F = ' + e)} as a sum of minterms and as a product of maxterms (shorthand).</p>", st, "$" + sigma(ms) + " = " + pi([m for m in range(1 << n) if m not in ms]) + "$")


topic("c2", "Sum of minterms, product of maxterms", "Lectures 4–5 · 23/24 Q1(c)", pri=2,
      learn=f"""<p>Number the truth-table rows 0, 1, 2 … from the top.</p>
<p><b>Minterm</b> {M("m_i")}: an AND of all the variables that is 1 <b>only on row i</b>.<br><b>Maxterm</b> {M("M_i")}: an OR of all the variables that is 0 <b>only on row i</b>.</p>
$$F = \\Sigma m(\\text{{rows where }} F = 1) \\qquad F = \\Pi M(\\text{{rows where }} F = 0)$$
{img(ex("sigma-pi-switch"), "switching between the two", True)}
<p>The two lists are opposites: a row number is in one or the other, never both.</p>""",
      check=("3 variables, $F = \\Sigma m(1, 4, 6)$. Write it as ΠM.", "$\\Pi M(0, 2, 3, 5, 7)$: every row number that is not in the Σ list."))
q("t2-1", "Shorthand forms, SOP", *mm("A'B + AC", ABC), sim=mm("XY' + X'Z", XYZ))
q("t2-2", "Shorthand forms, POS", *mm("(X + Y')(Y + Z)", XYZ), sim=mm("(A + B)(B' + C')", ABC))
q("t2-3", "Four variables", *mm("AB' + C'D", ABCD), sim=mm("A'D + BC", ABCD))
put(EX["pp-1c"])


def km(names, ms, key, dc=(), note=""):
    st, c = p_simplify(ms, names, key, dc)
    pr = "$F(" + ", ".join(names) + ") = " + sigma(ms) + "$" + (" with don't cares $d(" + ", ".join(map(str, dc)) + ")$" if dc else "")
    return (f"<p>Simplify {pr} with a K-map.</p>" + (f"<p>{note}</p>" if note else ""), st, M("F = " + cover_tex(c, names)))


topic("c3", "K-map simplification", "Lectures 5–6 · used in 23/24 Q1, Q2(b), Q3", pri=3,
      learn=f"""<p>A K-map is the truth table folded so that <b>neighbouring cells differ in one variable</b>. That is why the labels go 00, 01, <b>11, 10</b>.</p>
{img(ex("k3-index"), "3-variable map", True)}{img(ex("k4-index"), "4-variable map", True)}
<ol><li>Put a 1 in each minterm's cell.</li><li>Circle groups of <b>1, 2, 4 or 8</b>. As big as possible, as few as possible. Edges wrap round.</li><li>For each group keep only the variables that <b>do not change</b>. 0 → primed, 1 → plain.</li><li>OR the groups.</li></ol>
<p><b>Don't care (x):</b> may be circled if it makes a group bigger, otherwise ignore it.</p>""",
      check=("On a 4-variable map, a group of 4 cells gives a term with how many letters?", "<b>2.</b> Each doubling of the group removes one letter: 1 cell = 4 letters, 2 = 3, 4 = 2, 8 = 1."))
q("t3-2", "Three variables, wrap-around", *km(ABC, [0, 2, 4, 5, 6], "t3-2"), sim=km(ABC, [0, 1, 3, 5, 7], "t3-1"))
q("t3-3", "Four variables, four corners", *km(ABCD, [0, 2, 5, 7, 8, 10, 13, 15], "t3-3"), sim=km(ABCD, [1, 3, 4, 5, 6, 7, 12, 13], "t3-4"))
q("t3-5", "With don't cares", *km(ABC, [1], "t3-5", [2, 3, 5, 6, 7], "This is a real J column from a counter design (5.1)."), sim=km(ABCD, [1, 3, 7, 11, 15], "t3-6", [0, 2, 5]))


def nand(names, ms, key):
    st, c = p_simplify(ms, names, key)
    st = st[:1] + st[2:] + p_nand(c, names, key)
    return ("<p>Simplify $F(" + ", ".join(names) + ") = " + sigma(ms) + "$ and implement it with two-level NAND gates.</p>", st, M("F = " + cover_tex(c, names)))


def nor(names, ms, key):
    st, pos = p_nor(ms, names, key)
    return ("<p>Implement $F(" + ", ".join(names) + ") = " + sigma(ms) + "$ with two-level <b>NOR</b> gates.</p>", st, M("F = " + pos))


topic("c4", "Two-level NAND and NOR circuits", "Lecture 6 · 23/24 Q1(d)", pri=2,
      learn=f"""<p>Any sum of products becomes NAND-NAND with no extra thought:</p>
$$F = AB + CD = \\big((AB)' \\cdot (CD)'\\big)'$$
{img(ex("nand-transform"), "AND-OR to NAND-NAND", True)}
<ol><li>Simplify to SOP with the K-map.</li><li>Replace every AND gate with a NAND.</li><li>Replace the OR gate with a NAND.</li><li><b>A term with one letter</b> has no first gate, so <b>invert that letter</b> before the last NAND.</li></ol>
<p><b>NOR-NOR</b> is the mirror image: group the <b>0s</b> to get F', invert it to get a product of sums, then every OR and the AND become NOR.</p>""",
      check=(f"{M('F = AB + C')} as NAND-NAND. What goes into the last NAND?", f"{M('(AB)' + chr(39))} and {M('C' + chr(39))}. The lone C must be inverted."))
q("t4-1", "Two-level NAND", *nand(ABC, [1, 3, 6, 7], "t4-1"), sim=nand(ABCD, [0, 1, 2, 3, 13, 15], "t4-3"))
q("t4-2", "NAND with a lone letter", *nand(ABC, [1, 3, 4, 5, 7], "t4-2"), sim=nand(ABC, [2, 3, 4, 6, 7], "t4-4"))
q("t4-5", "Two-level NOR", *nor(ABC, [0, 1, 5, 7], "t4-5"), sim=nor(XYZ, [2, 3, 4, 6], "t4-6"))
put(EX["pp-1d"])


def mux(names, ms, key):
    st, a = p_mux(names, ms, key)
    return ("<p>Implement $F(" + ", ".join(names) + ") = " + sigma(ms) + f"$ with one {1 << (len(names) - 1)}-to-1 multiplexer.</p>", st, a)


topic("c5", "Multiplexers", "Lecture 10 · the likely combinational question (lecturer's hint)", pri=3,
      learn=f"""<p>A <b>multiplexer</b> is a switch: the <b>select</b> lines form a number, and that number picks which <b>data</b> input reaches the output. Select 0 → input 0.</p>
{img(ex("mux4-block"), "4-to-1 mux", True)}
<p><b>Any function of n variables fits on a mux with n − 1 selects</b> (slides 7 and 9):</p>
<ol><li>First n − 1 variables → select lines.</li><li>Pair the truth-table rows: in each pair only the last variable changes.</li><li>Connect that data input to <b>0, 1, the variable, or its inverse</b>.</li></ol>
{table(["F when last variable = 0, 1", "Connect"], [["0, 0", "0"], ["0, 1", "the variable"], ["1, 0", "its inverse"], ["1, 1", "1"]], "tt small")}
<p><b>Bigger from smaller:</b> a 16-to-1 mux = four 4-to-1 muxes sharing the low selects + one more 4-to-1 choosing between them.</p>
<p><b>Demultiplexer:</b> the reverse. One input goes to the one output picked by the selects.</p>""",
      check=("How many variables can one 8-to-1 mux implement?", "<b>4.</b> Three on the selects, the fourth on the data inputs."))
q("h1-2", "Slide 7: a 4-to-1 mux", *mux(list("xyz"), [1, 2, 6, 7], "h1-2"), sim=mux(list("xyz"), [1, 2, 4, 7], "h1-2s"))
q("h1-1", "Slide 8: an 8-to-1 mux", *mux(ABCD, [1, 3, 4, 11, 12, 13, 14, 15], "h1-1"), sim=mux(ABCD, [0, 1, 3, 4, 8, 9, 15], "h1-1s"))
q("h1-4", "Bigger muxes from smaller ones", "<p>(a) How many 4-to-1 multiplexers build a 16-to-1 multiplexer, and which select lines go where? (b) How many select lines does a 32-to-1 multiplexer need?</p>",
  [["(a) First level: 16 inputs ÷ 4 = <b>4</b> muxes, all sharing the two low select bits. Second level: <b>1</b> mux picks between those four outputs using the two high select bits. Total <b>5</b>.", "Each level of 4-to-1 muxes uses up two select bits. 16 inputs need 4 select bits, so two levels."],
   ["(b) 2<sup>n</sup> inputs need n select lines. 32 = 2<sup>5</sup> → <b>5</b>.", "The selects must be able to count from 0 to 31."]], "5 muxes · 5 select lines",
  sim=("<p>(a) How many 2-to-1 multiplexers build an 8-to-1 multiplexer? (b) How many select lines does a 64-to-1 multiplexer need?</p>",
       [["(a) 8 inputs → 4 muxes, then 2, then 1. Total <b>7</b>. Level 1 uses S<sub>0</sub>, level 2 uses S<sub>1</sub>, the last mux uses S<sub>2</sub>.", "Each level halves the number of lines."], ["(b) 64 = 2<sup>6</sup> → <b>6</b>.", ""]], "7 muxes · 6 select lines"))

FA = {"S": [1, 2, 4, 7], "C": [3, 5, 6, 7]}
topic("c6", "Decoders as minterm generators", "Lecture 9 · back-up if the combinational question is not multiplexers", pri=2,
      learn=f"""<p>An <b>n-to-2ⁿ decoder</b> has n inputs and 2ⁿ outputs. Exactly <b>one</b> output is 1: the one whose number equals the input.</p>
<p>So output i <b>is minterm i</b>. To build any function: decoder + <b>one OR gate</b> over the minterms you want.</p>
{table(["Decoder type", "Each output is a", "Collect with", "Function form"], [["active-high", "minterm", "OR gate", "Σm"], ["active-low (bubbles on outputs)", "maxterm", "AND gate", "ΠM"]])}
<p><b>Enable</b> input: EN = 0 switches every output off. Two 2-to-4 decoders make a 3-to-8: the third input enables one or the other.</p>
<p><b>Encoder</b> = decoder backwards (2ⁿ lines in, n-bit number out). A <b>priority encoder</b> reports the highest-numbered input that is 1.</p>""",
      check=("A 3-to-8 decoder has input 101. Which output is 1?", "<b>Output 5.</b> 101 in binary is 5."))
q("dec-1", "Slide 6: full adder from a decoder", "<p>Implement a full adder (inputs X, Y, Z, outputs sum S and carry C) with a 3-to-8 decoder and OR gates.</p>",
  [["A full adder adds three bits. S is 1 when an <b>odd</b> number of inputs are 1. C is 1 when <b>two or more</b> are 1.", "X + Y + Z can be 0, 1, 2 or 3, written in binary as C S."]] + p_decoder(XYZ, FA, "dec-1"),
  "$S = " + sigma(FA["S"]) + "$ · $C = " + sigma(FA["C"]) + "$",
  sim=("<p>Implement a full subtractor (X − Y − Z, outputs difference D and borrow B) with a 3-to-8 decoder and OR gates.</p>",
       [["D is 1 when an odd number of inputs are 1 (same as a sum). B is 1 when you have to borrow: when Y + Z is bigger than X.", "Row 0 1 1: 0 − 1 − 1 needs a borrow. Row 1 1 1: 1 − 2 needs a borrow."]] + p_decoder(XYZ, {"D": [1, 2, 4, 7], "B": [1, 2, 3, 7]}, "dec-1s"),
       "$D = " + sigma([1, 2, 4, 7]) + "$ · $B = " + sigma([1, 2, 3, 7]) + "$"))
q("dec-2", "Slide 12: active-low decoder", "<p>The same full adder is built with an <b>active-low</b> 3-to-8 decoder. Which gate collects the outputs, and which decoder outputs feed the gate for S?</p>",
  [["An active-low decoder output is 0 only on its own row: that is a <b>maxterm</b>.", "Inverting a minterm gives the maxterm with the same number."],
   ["Maxterms are collected with an <b>AND</b> gate, and you use the rows where the function is <b>0</b>." + "$$S = " + pi([0, 3, 5, 6]) + " \\qquad C = " + pi([0, 1, 2, 4]) + "$$", "S is 1 on rows 1, 2, 4, 7, so it is 0 on rows 0, 3, 5, 6."]],
  "AND gates · S uses outputs 0, 3, 5, 6 · C uses outputs 0, 1, 2, 4")

# ===================================================================== 2 · latches and flip-flops
part("Latches and flip-flops")


def lat(seq_, q0, nand_=False):
    st, a = p_latch(seq_, q0, nand_)
    nm = "S'R'" if nand_ else "SR"
    return (f"<p>A {'NAND' if nand_ else 'NOR'} latch holds Q = {q0}. Its inputs then take the values {nm} = " + ", ".join(f"{s}{r}" for s, r in seq_) + ". Give Q after each one.</p>", st, "Q = " + a)


topic("f1", "The SR latch", "Lectures 11–12, slides 3–16", pri=2,
      learn=f"""<p>A combinational circuit only knows its inputs <b>now</b>. Feed an output back into an input and the circuit can <b>remember</b>. That is sequential logic.</p>
<p><b>SR latch</b> = two NOR gates, each output fed into the other gate. It stores 1 bit.</p>
{img(seq("sr-latch-nor"), "SR latch", True)}
$$Q_{{next}} = (R + Q')' \\qquad Q'_{{next}} = (S + Q)'$$
{table(["S R", "Q next", "Name"], [["0 0", "Q (no change)", "<b>hold</b> ← the memory"], ["1 0", "1", "<b>set</b>"], ["0 1", "0", "<b>reset</b>"], ["1 1", "Q = Q' = 0", "<b>not allowed</b>"]])}
<p><b>NAND version (S'R' latch):</b> same latch, inputs <b>active low</b>. 11 hold · 01 set · 10 reset · <b>00 not allowed</b>.</p>""",
      check=("The same input SR = 00 can give Q = 0 or Q = 1. Why?", "00 means <b>hold</b>: Q keeps whatever the last set or reset left. The output depends on history, not only on the inputs now."))
q("lat-1", "Trace a NOR latch", *lat([(0, 0), (0, 1), (0, 0), (1, 0), (0, 0), (0, 1)], 1), sim=lat([(1, 1), (0, 1), (1, 1), (1, 0), (1, 1), (0, 1)], 0, True))
q("lat-2", "Slide 13: why SR = 11 is banned", "<p>Explain what goes wrong in a NOR SR latch when S = R = 1, and what happens if both then return to 0 together.</p>",
  [["With S = R = 1 both NOR gates have a 1 on an input, so <b>both outputs are 0</b>:" + DD("Q = (1 + Q')' = 0 \\qquad Q' = (1 + Q)' = 0"), "Q and Q' are supposed to be opposites. Here they are equal, so the latch is not storing a valid bit."],
   ["Now S and R drop to 0 together. Both gates see 0 and 0, so both outputs go to 1. Those 1s feed back and both go to 0. Then 1 again…", "Each gate is reacting to the other's old value. The outputs chase each other."],
   ["The latch <b>oscillates</b>, and where it finally lands depends on which gate is slightly faster. The state is <b>indeterminate</b>.", "That is why SR = 11 is never used, and why the D latch and the JK flip-flop were invented."]],
  "Both outputs 0 (not complements), then an unpredictable state when S and R return to 0")

topic("f2", "D latch, clock, and why flip-flops exist", "Lectures 11–12, slides 17–33", pri=2,
      learn=f"""<p><b>Gated latch:</b> add an enable input C. C = 1 → the latch listens. C = 0 → inputs ignored, it holds.</p>
<p><b>D latch:</b> feed R from S through an inverter and call the input D. Now S = R = 1 can never happen.</p>
{img(seq("d-latch"), "D latch", True)}
{table(["C", "D", "Q next"], [["0", "x", "Q (hold)"], ["1", "0", "0"], ["1", "1", "1"]], "tt small")}
<p><b>Problem:</b> a latch is <b>level triggered</b>. The whole time C = 1 it is open, so Q can change many times in one clock pulse.</p>
<p><b>Flip-flop:</b> two latches in a row on opposite clock levels (<b>master–slave</b>). CLK = 1: master open, slave shut. CLK falls: master freezes, slave opens and passes the value on. So Q changes <b>only at the falling edge</b>.</p>
{img(seq("ms-dff"), "master-slave D flip-flop", True)}
{img(seq("ff-edges"), "edge symbols", True)}
<p>Master–slave D uses 8 gates. A positive-edge D flip-flop can be built from 3 SR latches. An <b>asynchronous reset</b> input forces Q = 0 at once, without waiting for the clock (used at power-up).</p>""",
      check=("One sentence: latch against flip-flop?", "A latch is <b>level</b> triggered (open the whole time the clock is 1). A flip-flop is <b>edge</b> triggered (samples only at the clock transition)."))


def lff(d, key):
    st = p_latch_ff(d, key)
    return (img(key + "-q", "CLK and D") + "<p>The same CLK and D drive (a) a D latch with CLK as its enable and (b) a negative-edge-triggered D flip-flop. Both start at Q = 0. Draw the two Q outputs.</p>", st, "See the waveforms in the last step.")


q("lf-1", "Latch against flip-flop on the same input", *lff("001110100111100110000111", "lf-1"), sim=lff("011111011000011001111000", "lf-2"))


def tr(kind, seq_, q0=0):
    st, a = p_fftrace(kind, seq_, q0)
    s = ", ".join((f"{v[0]}{v[1]}" if kind == "JK" else str(v)) for v in seq_)
    return (f"<p>A {kind} flip-flop starts at Q = {q0}. At {len(seq_)} clock edges in a row {kind} = {s}. Give Q after each edge.</p>", st, "Q = " + a)


topic("f3", "D, JK and T flip-flops", "Lectures 11–12, slides 34–39", pri=3,
      learn=f"""<p>A flip-flop stores 1 bit (Q) and changes only at the clock edge. Q<sup>+</sup> means "Q after the next edge".</p>
{img(seq("ff-symbols"), "flip-flops", True)}
{table(["Flip-flop", "What it does at the edge", "Characteristic equation"], [["D", "copies D", M("Q^+ = D")], ["JK", "00 hold · 01 reset · 10 set · 11 <b>toggle</b>", M("Q^+ = JQ' + K'Q")], ["T", "T = 1 toggle · T = 0 hold", M("Q^+ = T ^ Q")]])}
<p><b>How to remember JK:</b> it is an SR flip-flop (J = set, K = reset) where the banned 11 input now means toggle. A T flip-flop is a JK with J and K tied together.</p>""",
      check=("Q = 1. What is Q<sup>+</sup> for (a) JK = 01 (b) JK = 11 (c) T = 1 (d) D = 1?", "(a) <b>0</b> reset · (b) <b>0</b> toggle · (c) <b>0</b> toggle · (d) <b>1</b>."))
q("t5-1", "Follow a JK flip-flop", *tr("JK", [(1, 0), (0, 0), (1, 1), (0, 1), (1, 1), (1, 1), (0, 0), (1, 0)]), sim=tr("T", [1, 1, 0, 1, 0, 0, 1, 1]))
for kind_, e_ in (("T", "T ^ Q"), ("JK", "JQ' + K'Q")):  # check the conversion claims below on every row
    for m in range(8):
        env = {"T": m & 1, "J": (m >> 1) & 1, "K": m & 1, "Q": m >> 2}
        assert ev(e_, env) == (env["Q"] ^ env["T"] if kind_ == "T" else jk(env["J"], env["K"], env["Q"]))
q("ff-1", "Make a T flip-flop from a D flip-flop", "<p>You only have D flip-flops. Build a T flip-flop from one.</p>",
  [["Write what you want: a T flip-flop gives" + DD("Q^+ = T ^ Q"), "Start from the characteristic equation of the flip-flop you want."],
   ["Write what you have: a D flip-flop gives" + DD("Q^+ = D"), "Whatever sits on D at the edge becomes the next Q."],
   ["So put the wanted next state on D:" + DD("D = T ^ Q") + "<p>One XOR gate, fed by T and the flip-flop's own Q.</p>", "T = 0 → D = Q, it holds. T = 1 → D = Q', it toggles."]],
  M("D = T ^ Q"),
  sim=("<p>You only have D flip-flops. Build a JK flip-flop from one.</p>",
       [["Wanted:" + DD("Q^+ = JQ' + K'Q"), "The JK characteristic equation."], ["A D flip-flop gives " + M("Q^+ = D") + ", so:" + DD("D = JQ' + K'Q") + "<p>Two AND gates, one OR gate, an inverter for K.</p>", "Check JK = 11: D = Q' + 0 = Q', toggle. JK = 00: D = 0 + Q = Q, hold."]],
       M("D = JQ' + K'Q")))

topic("f4", "Excitation tables", "Lectures 14–16, slides 14–16 · inside 23/24 Q3", pri=3,
      learn=f"""<p>The characteristic table says: "these inputs → what happens?" (used for <b>analysis</b>).</p>
<p>The <b>excitation table</b> is the same facts backwards: "I want Q to go from this to that. What inputs?" (used for every <b>design</b> question).</p>
{ET}
<p><b>JK trick:</b> Q = 0 → only <b>J</b> matters (J = next Q, K = x). Q = 1 → only <b>K</b> matters (K = opposite of next Q, J = x).<br><b>D</b> = next Q. <b>T</b> = 1 when Q changes.</p>""",
      check=("Q = 1 and you want Q<sup>+</sup> = 0. What are J and K?", "<b>J = x, K = 1.</b> Reset (01) or toggle (11) both work, so K must be 1 and J can be anything."))
q("t5-2", "Build the JK excitation table", "<p>Starting from the JK characteristic table, work out which J K values make Q go 0→0, 0→1, 1→0 and 1→1.</p>",
  [["0 → 0: hold (00) or reset (01) both work. J = 0 in both, K is either → <b>0 x</b>.", "List every action that gives the move, then see which input is the same in all of them."],
   ["0 → 1: set (10) or toggle (11). J = 1, K either → <b>1 x</b>.", "Same reasoning."],
   ["1 → 0: reset (01) or toggle (11). K = 1, J either → <b>x 1</b>.", "Now Q starts at 1, so K is the input that matters."],
   ["1 → 1: hold (00) or set (10). K = 0, J either → <b>x 0</b>.", ""],
   ["All together:" + ET, "Write this table at the top of your answer sheet before any design question."]], "0x, 1x, x1, x0")


def exq(seqq):
    rows = [[f"{a} → {b}", EXC[(a, b)], b, int(a != b)] for a, b in zip(seqq, seqq[1:])]
    return ("<p>A flip-flop's output must go through the values Q = " + ", ".join(map(str, seqq)) + " on successive clock edges. Give the J K, D and T inputs needed before each edge.</p>",
            [["Split the sequence into moves: present Q → next Q.", "Each clock edge is one move."],
             ["Look each move up in the excitation table:" + table(["Q → Q<sup>+</sup>", "J K", "D", "T"], rows), "D is just the next value. T is 1 when the value changes. JK: present 0 uses J, present 1 uses K."]],
            "JK: " + ", ".join(r[1] for r in rows))


q("exc-1", "Inputs for a wanted sequence", *exq([0, 1, 1, 0, 0, 1]), sim=exq([1, 0, 1, 1, 0, 0]))

# ===================================================================== 3 · clocked circuits
part("Clocked circuits: analysis and design")
topic("s1", "Analysing a clocked circuit", "Lecture 13 · sequential logic", pri=3,
      learn=f"""<p><b>Analysis:</b> circuit → equations → <b>state table</b> → <b>state diagram</b>. Always the same three steps (slide 11):</p>
<ol><li>Read the Boolean expression for each flip-flop input and for the output.</li><li>For every present state and input, work out the flip-flop input values.</li><li>Use the characteristic table to get the next state.</li></ol>
<p><b>State</b> = what the flip-flops hold now. <b>State equations</b> give the next state directly, for example A(t+1) = Ax + Bx.</p>
<p><b>State diagram:</b> a circle per state, an arrow per table row, labelled <b>input/output</b>.</p>
<p><b>Size check (slide 18):</b> n flip-flops → 2ⁿ circles. m inputs → 2ᵐ arrows leaving every circle.</p>""",
      check=("Present Q = 1, J K = 1 1. Next Q?", "<b>0.</b> 11 toggles."))
a1, _ = p_analysis("JK", [("Q1", ("X'Q0", "X + Q0")), ("Q0", ("X + Q1", "X'"))], "Q1Q0X", "an-1", xname="X", zname="Z")
a1.append(["What it does: Z = 1 only on the arrow 11 —1→ 01. Following the 1s and 0s that lead there shows it fires when the last four inputs were <b>1001</b>.", "This is the sequence detector that 4.3 designs from scratch."])
a2, _ = p_analysis("JK", [("A", ("B", "Bx'")), ("B", ("x'", "A ^ x"))], None, "h3-1")
q("an-1", "Slides 8–18: two JK flip-flops", img(seq("fsm-1001-circuit"), "circuit", True) + "<p>Two JK flip-flops Q<sub>1</sub>Q<sub>0</sub>, input X, output Z. Derive the state table and the state diagram.</p>", a1, "State table in step 3. It detects 1001.",
  sim=(f"<p>Two JK flip-flops A and B, input x: {M('JA = B')}, {M('KA = Bx' + chr(39))}, {M('JB = x' + chr(39))}, {M('KB = A ^ x')}. Derive the state table and state diagram.</p>", a2, "State table in step 3."))
a3, _ = p_analysis("D", [("A", "Ax + Bx"), ("B", "A'x")], "(A + B)x'", "an-2", zname="y")
a4, _ = p_analysis("T", [("A", "Bx"), ("B", "x")], "AB", "an-3", zname="y")
a4.append(["What it does: with x = 0 nothing toggles. With x = 1 it steps 00 → 01 → 10 → 11 → 00. A 2-bit counter with an enable, and y flags state 11.", "y = AB has no x in it, so the output depends on the state only: a Moore circuit."])
q("an-2", "Slide 4: state equations with D flip-flops", "<p>Two D flip-flops A and B, input x, output y:</p>$$A(t+1) = Ax + Bx \\qquad B(t+1) = A'x \\qquad y = (A + B)x'$$<p>Derive the state table and state diagram.</p>", a3, "State table in step 3.",
  sim=(f"<p>Two T flip-flops A and B, input x: {M('TA = Bx')}, {M('TB = x')}, output {M('y = AB')}. Derive the state table. What does the circuit do?</p>", a4, "A 2-bit counter that counts only when x = 1"))


def sd(pats, key, **k):
    st, T0, states = p_detector(pats, "JK", key, design=False, **k)
    if len(pats) == 1:
        pr = f"<p>A Mealy circuit has input X and output Z. Z = 1 when the last {len(pats[0])} inputs were <b>{pats[0]}</b>. Overlapping patterns count. Draw the state diagram and give the state table.</p>"
    else:
        pr = f"<p>One input, two outputs. Design the state diagram of a Mealy detector for two 4-bit sequences: <b>{pats[0]}</b> (output 01) and <b>{pats[1]}</b> (output 10). Otherwise the output is 00. Overlapping sequences must be detected, and both must be detected by one circuit block.</p>"
    return (pr, st, f"{len(states)} states. See the diagram and table.")


topic("s2", "State diagram of a sequence detector", "Lectures 14–16, slides 2–11 and 33–35", pri=3,
      learn=f"""<p><b>Design</b> is analysis backwards: words → state diagram → state table → flip-flop inputs → K-maps → circuit. The slides call sequence detectors "the hardest example in this class": get the diagram right and the rest is routine.</p>
{img(seq("moore-vs-mealy"), "Moore against Mealy", True)}
{table(["", "Output depends on", "Drawn", "Notes"], [["<b>Mealy</b>", "state <b>and</b> input", "on the arrow: input/output", "reacts at once"], ["<b>Moore</b>", "state only", "inside the circle", "synchronous output, often one more state"]])}
<p><b>The rule:</b> each state remembers <b>how much of the pattern you have so far</b>. For 1001: A = nothing, B = 1, C = 10, D = 100.</p>
<p><b>Draw it in two passes.</b> (1) The path that follows the pattern. (2) Every other arrow: go to the state for the <b>longest ending of the input that is still a start of the pattern</b>.</p>
<p><b>Overlap:</b> in 1001001 the middle 1 ends one match and starts the next. So from D a 1 gives output 1 and goes to B, not A.</p>""",
      check=("Detecting 110. You are in \"have 11\" and another 1 arrives. Where do you go?", "<b>Stay in \"have 11\".</b> The input ends in 111, and its last two bits are still 11. Going back to \"have 1\" is the classic mistake."))
q("sd-1", "Slides 8–11: detect 1001", *sd(["1001"], "sd-1"), sim=sd(["110"], "sd-2"))
q("sd-3", "Slides 33–35: two sequences, one circuit", *sd(["1011", "1110"], "sd-3", order=["", "1", "10", "101", "11", "111"], letters="ABCDGH"), sim=sd(["110", "101"], "sd-4"))


def det(pat, kind, key, **k):
    st, R, ans = p_detector([pat], kind, key, **k)
    mo = k.get("moore")
    return (f"<p>Design a {'Moore' if mo else 'Mealy'} circuit with input X and output {'Y' if mo else 'Z'} that is 1 when the last {len(pat)} inputs were <b>{pat}</b> (overlap allowed). Use {kind} flip-flops.</p>", st, ans)


topic("s3", "Designing the circuit: JK and D flip-flops", "Lectures 14–16, slides 5 and 12–25", pri=3,
      learn=f"""<p><b>The five steps (slide 5):</b></p>
<ol><li><b>State table</b> from the words (draw the diagram first).</li><li><b>Binary codes</b> for the states. n states need at least log₂ n flip-flops, rounded up.</li><li><b>Flip-flop inputs</b> for every row, from the <b>excitation table</b>.</li><li><b>K-map</b> each flip-flop input and the output. Variables: the state bits and X.</li><li><b>Build</b> the circuit.</li></ol>
{ET}
{table(["", "JK", "D"], [["Step 3", "excitation table needed", "nothing to do: D = next state"], ["Equations", "simpler (half the entries are x)", "usually bigger"], ["In practice", "used less", "<b>used more</b>: one input, less hardware"]])}""",
      check=("Row 0 1 → 1 0 (Q<sub>1</sub>Q<sub>0</sub>). Give J<sub>1</sub>K<sub>1</sub> and J<sub>0</sub>K<sub>0</sub>.", "Q<sub>1</sub>: 0 → 1 → <b>1 x</b>. Q<sub>0</sub>: 1 → 0 → <b>x 1</b>."))
q("h2-3", "Slides 12–20: 1001 with JK flip-flops", *det("1001", "JK", "h2-3", sample="1001001"), sim=det("101", "JK", "h2-1", sample="10101"))
q("d-1", "Slides 21–24: 1001 with D flip-flops", *det("1001", "D", "d-1", sample="1001001"), sim=det("110", "D", "h2-2", sample="1101100"))

topic("s4", "The Moore version", "Lectures 14–16, slides 26–32", pri=3,
      learn=f"""<p>In a <b>Moore</b> machine the output depends on the state only, so it is written <b>inside the circle</b> (state/output). You need a state that <b>means</b> "the full pattern has just been seen".</p>
{img(seq("fsm-1001-moore"), "Moore 1001", True)}
<p>For 1001 that is a fifth state E with output 1. From E: a 0 gives …10 → C. A 1 gives …11 → B.</p>
<p>5 states → <b>3 flip-flops</b>. Codes 101, 110, 111 are unused → don't cares. The output is a function of the state bits only (here Y = Q<sub>2</sub>).</p>
<p>The slides build it with <b>T flip-flops</b>: T = 1 exactly where a state bit changes.</p>""",
      check=("Mealy 1001 needs 4 states, Moore needs 5. Why?", "Mealy puts the 1 on the <b>arrow</b> D → B. Moore cannot put outputs on arrows, so it needs an extra <b>state</b> whose output is 1."))
q("mo-1", "Slides 26–32: Moore 1001 with T flip-flops", *det("1001", "T", "mo-1", moore=True, given={"T2": "Q2 + Q1Q0X", "T1": "Q2X' + Q1X + Q0X'", "T0": "Q1 + Q0'X + Q0X'", "Y": "Q2"}, sample="1001001"),
  sim=det("101", "D", "mo-2", moore=True, sample="10101"))
