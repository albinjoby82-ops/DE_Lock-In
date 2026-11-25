"""Study path additions (Nov 2026): design questions that start from a description
in words and end with a drawn circuit, and extra practice on every topic.

Runs after final_path_a and final_path_b: at(topic) reopens an existing topic,
topic(..., after=id) slots a new topic in. Every answer is computed by the builders."""
from final_site import *
from final_design import *
import final_path_a as A
import final_path_b as B

use(PATH)
SHOW = " Show the truth table, the simplified logic function and the logic diagram."
SHOWSEQ = " Show the state diagram, the state table, the flip-flop input functions and the logic diagram."
PQ = (("P", lambda m: m >> 2), ("Q", lambda m: m & 3))

# ===================================================================== 2.7 · combinational design from words
SAYS = table(["The question says", "What you do after the truth table"], [
    ['nothing, or “minimum number of gates”', "K-map → AND gates into an OR gate"], ['“using NAND gates”', "K-map → NAND-NAND (2.4)"],
    ['“using a multiplexer”', "<b>no K-map.</b> Pair the rows on the last variable (2.5)"], ['“using a decoder”', "<b>no K-map.</b> List the minterms, one OR gate per output (2.6)"]])
KINDS = table(["The words", "It is a", "Method"], [
    ['“output 1 when the last inputs were …”, “three 1s in a row”, “when the code has been entered”', "sequence detector", "4.2 to 4.4"],
    ['“goes through the states … and repeats”', "counter (no input)", "5.1"],
    ['“counts up when X = 1, down when X = 0”, “counts only while X = 1”', "counter with a control input", "state table with an X column, then the same steps"]])
topic("c7", "Design questions: from words to a circuit", "Lectures 4 to 10 put together · how exam questions are asked", pri=3, after="c6",
      learn=f"""<p>The exam says <b>“Design a circuit that…”</b>. It gives you <b>words</b>, not a Σm list. The answer is always the same chain:</p>
$$\\text{{words}} \\;\\to\\; \\text{{letters}} \\;\\to\\; \\text{{truth table}} \\;\\to\\; \\text{{K-map}} \\;\\to\\; \\text{{equation}} \\;\\to\\; \\text{{drawing}}$$
<ol><li><b>Letters.</b> One letter per input bit, most significant bit first. Name the output.</li>
<li><b>Truth table.</b> All 2ⁿ rows in counting order. For each row, ask the question in the words. Inputs that can never happen get an <b>x</b>.</li>
<li><b>K-map</b> → the simplest equation (2.3).</li>
<li><b>Draw it.</b> One AND gate per term, one OR gate to join them. A dashed letter needs a NOT gate.</li></ol>
{SAYS}
<p><b>On paper:</b> write the step names down the margin before you start. Then you never stall on “what comes next?”.</p>""",
      check=("A question ends “…using one 8-to-1 multiplexer”. Do you need a K-map?", "<b>No.</b> Truth table, then pair the rows on the last variable. A multiplexer needs no simplifying."))
q("des-1", "Design in words: majority vote",
  "<p>Three judges each have a button: A, B and C (1 = yes). Design a circuit whose output F is 1 when <b>at least two</b> judges say yes." + SHOW + "</p>",
  *p_words("des-1", ABC, [3, 5, 6, 7], "gates", "Inputs: A, B, C (one per judge, 1 = yes). Output: F (1 = passed). Three inputs → 8 rows.", "<b>are two or more of the inputs 1?</b>", cols=()),
  sim=("<p>A 3-bit number N = ABC (A is the most significant bit). Design a circuit with output F = 1 when <b>N is 5 or more</b>." + SHOW + "</p>",
       *p_words("des-1s", ABC, [5, 6, 7], "gates", "Inputs: A, B, C, where A is worth 4, B is worth 2 and C is worth 1. Output: F. Three inputs → 8 rows.", "<b>is N ≥ 5?</b>")))
BCD = range(10, 16)
q("des-2", "Design in words: BCD digit, with don't cares",
  "<p>A decimal digit N (0 to 9) arrives in BCD on four wires A, B, C, D (A is the most significant bit). The codes 1010 to 1111 never occur. Design a circuit with output F = 1 when <b>N ≥ 5</b>. Use the minimum number of gates." + SHOW + "</p>",
  *p_words("des-2", ABCD, [5, 6, 7, 8, 9], "gates", "Inputs: A, B, C, D with weights 8, 4, 2, 1. Output: F. Four inputs → 16 rows, but only rows 0 to 9 can happen.", "<b>is N ≥ 5?</b> Rows 10 to 15 cannot happen, so they get an x.", dc=BCD),
  sim=("<p>A BCD digit N = ABCD (0 to 9; the codes 1010 to 1111 never occur). Design a circuit with output F = 1 when N is a <b>prime number</b> (2, 3, 5 or 7). Use the minimum number of gates." + SHOW + "</p>",
       *p_words("des-2s", ABCD, [2, 3, 5, 7], "gates", "Inputs: A, B, C, D with weights 8, 4, 2, 1. Output: F. Only rows 0 to 9 can happen.", "<b>is N one of 2, 3, 5, 7?</b> Rows 10 to 15 get an x.", dc=BCD)))
q("des-3", "Design in words: compare two numbers, NAND gates",
  "<p>Two 2-bit numbers: P = AB and Q = CD (A and C are the most significant bits). Design a circuit with output F = 1 when <b>P &gt; Q</b>. Implement it with two-level NAND gates. NOT gates can be used. Show the truth table, K-map, logic function and logic diagram.</p>",
  *p_words("des-3", ABCD, [m for m in range(16) if (m >> 2) > (m & 3)], "nand", "Inputs: A, B (the number P, 0 to 3) and C, D (the number Q, 0 to 3). Output: F. Four inputs → 16 rows.", "<b>is P bigger than Q?</b>", cols=PQ),
  sim=("<p>Two 2-bit numbers: P = AB and Q = CD. Design a circuit with output F = 1 when <b>P + Q is 4 or more</b> (the carry out of a 2-bit adder). Implement it with two-level NAND gates. NOT gates can be used.</p>",
       *p_words("des-3s", ABCD, [m for m in range(16) if (m >> 2) + (m & 3) >= 4], "nand", "Inputs: A, B (the number P) and C, D (the number Q). Output: F. Four inputs → 16 rows.", "<b>is P + Q ≥ 4?</b>", cols=PQ)))
q("des-4", "Design in words: on a multiplexer",
  "<p>A 4-bit number N = ABCD (A is the most significant bit). Design a circuit with output F = 1 when N is a <b>prime number</b>. Use one 8-to-1 multiplexer. Show the truth table and the logic diagram.</p>",
  *p_words("des-4", ABCD, [2, 3, 5, 7, 11, 13], "mux", "Inputs: A, B, C, D with weights 8, 4, 2, 1. Output: F. Four inputs → 16 rows.", "<b>is N prime?</b> (2, 3, 5, 7, 11, 13. Remember 0 and 1 are not prime.)"),
  sim=("<p>Three switches A, B and C control one lamp F. The lamp is on when an <b>odd number</b> of switches are on, so flipping any one switch changes the lamp. Design the circuit with one 4-to-1 multiplexer.</p>",
       *p_words("des-4s", ABC, [1, 2, 4, 7], "mux", "Inputs: A, B, C (1 = switch on). Output: F (1 = lamp on). Three inputs → 8 rows.", "<b>is the number of 1s odd?</b>", cols=())))
q("des-5", "Design in words: two outputs from a decoder",
  "<p>A 3-bit number N = ABC. Design a circuit with two outputs, using one 3-to-8 decoder and OR gates: <b>P = 1 when N is prime</b>, and <b>S = 1 when N is a perfect square</b> (0, 1 or 4). Show the truth table and the logic diagram.</p>",
  *p_words_dec("des-5", ABC, {"P": [2, 3, 5, 7], "S": [0, 1, 4]}, "Inputs: A, B, C with weights 4, 2, 1. Outputs: P and S.", "P column: is N one of 2, 3, 5, 7? S column: is N one of 0, 1, 4?"),
  sim=("<p>A 3-bit number N = ABC. Design a circuit with two outputs, using one 3-to-8 decoder and OR gates: <b>G = 1 when N &gt; 4</b>, and <b>E = 1 when N is even</b> (0 counts as even).</p>",
       *p_words_dec("des-5s", ABC, {"G": [5, 6, 7], "E": [0, 2, 4, 6]}, "Inputs: A, B, C with weights 4, 2, 1. Outputs: G and E.", "G column: is N bigger than 4? E column: is N even?")))

# ===================================================================== extra practice · combinational
at("c1")
q("t1-5", "More practice: read a circuit", *A.circ("t1-5", ("AND", ("OR", "A", ("NOT", "B")), ("NAND", "B", "C"))), sim=A.circ("t1-6", ("OR", ("NOR", "A", "C"), ("AND", "B", ("NOT", "C")))))
at("c2")
q("t2-4", "More practice: shorthand forms", *A.mm("AB + B'C'", ABC), sim=A.mm("(A' + C)(B + C')", ABC))
at("c3")
q("t3-7", "More practice: four variables", *A.km(ABCD, [0, 1, 2, 5, 8, 9, 10], "t3-7"), sim=A.km(ABCD, [2, 3, 6, 7, 8, 9, 12, 13], "t3-8"))
q("t3-9", "More practice: a BCD function", *A.km(ABCD, [1, 3, 5, 7, 9], "t3-9", list(BCD), "A BCD digit: the codes 10 to 15 never occur."), sim=A.km(ABCD, [0, 3, 6, 9], "t3-10", list(BCD), "A BCD digit: the codes 10 to 15 never occur."))
at("c4")
q("t4-7", "More practice: NAND, four variables", *A.nand(ABCD, [5, 7, 8, 9, 10, 11, 13, 15], "t4-7"), sim=A.nand(ABC, [0, 1, 2, 6], "t4-8"))
q("t4-9", "More practice: NOR, four variables", *A.nor(ABCD, [0, 1, 2, 3, 4, 6, 12, 14], "t4-9"), sim=A.nor(ABC, [1, 2, 3, 7], "t4-10"))
at("c5")
q("h1-5", "More practice: a 4-to-1 mux", *A.mux(ABC, [0, 3, 5, 6], "h1-5"), sim=A.mux(ABC, [2, 3, 4, 7], "h1-5s"))
q("h1-6", "More practice: an 8-to-1 mux", *A.mux(ABCD, [0, 2, 3, 6, 8, 9, 13, 15], "h1-6"), sim=A.mux(ABCD, [1, 2, 5, 7, 10, 11, 12], "h1-6s"))


def dec2(key, outs):
    pr = "<p>Implement these functions with one 3-to-8 decoder and OR gates:</p>" + "".join("$$" + k + "(A, B, C) = " + sigma(v) + "$$" for k, v in outs.items())
    st = [["The functions are already lists of minterms, so there is nothing to simplify.", "A decoder makes every minterm for you. That is why decoder questions skip the K-map."]] + p_decoder(ABC, outs, key)[2:]
    return (pr, st, " · ".join(f"{k} = OR of outputs {', '.join(map(str, v))}" for k, v in outs.items()))


at("c6")
q("dec-3", "More practice: two functions, one decoder", *dec2("dec-3", {"F1": [0, 3, 5], "F2": [1, 3, 6, 7]}), sim=dec2("dec-3s", {"F1": [1, 2, 4], "F2": [0, 4, 5, 7]}))

# ===================================================================== extra practice · latches and flip-flops
at("f1")
q("lat-3", "More practice: trace a NOR latch", *A.lat([(1, 0), (0, 0), (0, 1), (0, 0), (1, 0), (0, 0)], 0), sim=A.lat([(0, 1), (1, 1), (1, 0), (1, 1), (1, 1), (0, 1)], 1, True))
at("f2")
q("lf-3", "More practice: latch against flip-flop", *A.lff("111110000110011111000111", "lf-3"), sim=A.lff("000110000111100000111001", "lf-4"))
at("f3")
q("t5-3", "More practice: a JK flip-flop that starts at 1", *A.tr("JK", [(0, 0), (1, 1), (1, 1), (0, 1), (1, 0), (0, 0), (0, 1), (1, 1)], 1), sim=A.tr("T", [0, 1, 1, 0, 1, 1, 1, 0], 1))
at("f4")
q("exc-2", "More practice: inputs for a wanted sequence", *A.exq([1, 1, 0, 1, 0, 0]), sim=A.exq([0, 0, 1, 1, 1, 0]))

# ===================================================================== extra practice · clocked circuits


def an(kind, ffs, z, key):
    st, _ = p_analysis(kind, ffs, z, key, zname="y")
    if kind == "JK":
        eqs = "".join(DD(f"J{n} = {e[0]} \\qquad K{n} = {e[1]}") for n, e in ffs)
    else:
        eqs = "".join(DD(f"{kind}{n} = {e}") for n, e in ffs)
    return (f"<p>A sequential circuit has two {kind} flip-flops A and B, one input x and one output y:</p>{eqs}{DD('y = ' + z)}<p>Derive the state table and draw the state diagram.</p>", st, "State table in step 3, diagram in step 4.")


at("s1")
q("an-4", "More practice: analyse a D flip-flop circuit", *an("D", [("A", "A'x + Bx'"), ("B", "Ax + B'x'")], "ABx", "an-4"), sim=an("JK", [("A", ("Bx", "x'")), ("B", ("x", "A + x'"))], "AB", "an-5"))
at("s2")
q("sd-5", "More practice: detect 0101", *A.sd(["0101"], "sd-5"), sim=A.sd(["011"], "sd-6"))
at("s3")
q("h2-4", "More practice: 011 with JK flip-flops", *A.det("011", "JK", "h2-4", sample="0011011"), sim=A.det("100", "JK", "h2-5", sample="1001100"))
q("d-2", "More practice: 010 with D flip-flops", *A.det("010", "D", "d-2", sample="0101001"), sim=A.det("001", "D", "d-3", sample="0010001"))
at("s4")
q("mo-3", "More practice: Moore 010 with JK flip-flops", *A.det("010", "JK", "mo-3", moore=True, sample="0101001"), sim=A.det("100", "D", "mo-4", moore=True, sample="1001100"))

# ===================================================================== 4.5 · sequential design from words
topic("s5", "Design questions in words: any clocked circuit", "Lectures 13 to 18 put together · how exam questions are asked", pri=3, after="s4",
      learn=f"""<p>The exam does not say “detect 1001”. It <b>describes a machine</b>. Your first job is to find the states. Ask: <b>“what does the circuit have to remember?”</b> Each different thing to remember is one state.</p>
{KINDS}
<p><b>Every design answer has the same six lines.</b> Write them down the margin before you start:</p>
<ol><li>State diagram</li><li>State table</li><li>State codes → how many flip-flops</li><li>Flip-flop inputs, from the excitation table</li><li>K-maps → equations</li><li><b>Logic diagram:</b> the flip-flops, with each equation drawn as gates on its input</li></ol>
{ET}
<p><b>Mealy or Moore?</b> “Z = 1 <i>when</i> the last bit arrives” → Mealy, output on the arrow. “The output depends only on the state” → Moore, output inside the circle.</p>
<p><b>Drawing step 6:</b> one AND gate per product term, one OR gate if there are two or more terms. Label each gate input with its signal name (Q<sub>1</sub>, Q<sub>0</sub>', X) instead of drawing long wires. The slides do the same.</p>""",
      check=("“Z = 1 when X has been 0 for two clock edges in a row.” What must a Mealy circuit remember?", "Two things: <b>“the last input was not 0”</b> and <b>“the last input was 0”</b>. Two states → one flip-flop. The second 0 gives Z = 1 on the arrow."))
s1_, _, a1_ = p_detector(["111"], "D", "sw-1", sample="0111101")
s1s, _, a1s = p_detector(["000"], "JK", "sw-1s", sample="1000010")
q("sw-1", "Design in words: three 1s in a row",
  "<p>A sensor sends one bit X on every clock edge. Design a circuit whose output Z is 1 when X has been 1 for <b>three clock edges in a row</b> (Z stays 1 for as long as the 1s continue). Use D flip-flops." + SHOWSEQ + "</p>",
  [["Turn the words into a pattern: Z = 1 when the last three inputs were <b>1 1 1</b>. “Stays 1 while the 1s continue” means overlapping matches count. The output appears as the third 1 arrives, so it is a Mealy circuit.", "Once you see it is a sequence detector, the method is fixed (4.2, 4.3)."]] + s1_, a1_,
  sim=("<p>A machine must stop (Z = 1) when its sensor input X has read <b>0 three times in a row</b>, and stay stopped while X stays 0. Design the circuit with JK flip-flops." + SHOWSEQ + "</p>",
       [["Turn the words into a pattern: Z = 1 when the last three inputs were <b>0 0 0</b>, overlap allowed. Mealy.", "Same machine as before with 0 and 1 swapped."]] + s1s, a1s))
UD = {(s, x): ((s + 1) % 4 if x else (s - 1) % 4) for s in range(4) for x in (0, 1)}
EN = {(s, x): ((s + 1) % 4 if x else s) for s in range(4) for x in (0, 1)}
s2_, _, a2_ = p_fsm("sw-2", "T", 2, UD, "Four states, one for each number the counter can show. From every state, X = 1 goes to the next number up and X = 0 goes to the next number down:", "1110")
s2s, _, a2s = p_fsm("sw-2s", "JK", 2, EN, "Four states, one for each number. X = 1 goes to the next number. X = 0 is an arrow back to the same state (hold):", "1101")
q("sw-2", "Design in words: up/down counter",
  "<p>Design a 2-bit synchronous <b>up/down counter</b> with one input X. When X = 1 it counts up: 00 → 01 → 10 → 11 → 00. When X = 0 it counts down. Use T flip-flops." + SHOWSEQ + "</p>", s2_, a2_,
  sim=("<p>Design a 2-bit synchronous counter with an <b>enable</b> input X. When X = 1 it counts 00 → 01 → 10 → 11 → 00. When X = 0 it holds its value. Use JK flip-flops." + SHOWSEQ + "</p>", s2s, a2s))
s3_, _, a3_ = p_detector(["011"], "JK", "sw-3", moore=True, sample="0110011")
s3s, _, a3s = p_detector(["111"], "T", "sw-3s", moore=True, sample="0111101")
q("sw-3", "Design in words: a lock (Moore)",
  "<p>An electronic lock has one input X. Design a <b>Moore</b> circuit whose output Y is 1 for one clock period after the bits <b>0, 1, 1</b> have arrived in that order. Use JK flip-flops." + SHOWSEQ + "</p>",
  [["The words: Y = 1 after the pattern <b>0 1 1</b>. Moore means the output belongs to a state, so there must be a state that means “011 has just arrived”.", "A Moore detector for an n-bit pattern needs n + 1 states."]] + s3_, a3_,
  sim=("<p>Design a <b>Moore</b> circuit with input X whose output Y is 1 whenever the last three inputs were all 1. Use T flip-flops." + SHOWSEQ + "</p>",
       [["Pattern <b>1 1 1</b>, Moore: four states (nothing, 1, 11, 111) and the output is 1 only in the last one.", "From the state “111” another 1 keeps you there, so Y stays 1."]] + s3s, a3s))

# ===================================================================== extra practice · counters
CW = " Show the state table, the logic functions and the logic diagram, and check what happens if it powers up in a state that is not in the pattern.</p>"
at("k1")
q("t7-5", "Design in words: running lights", *B.ctr([[1, 2, 4]], "t7-5", "<p>Three lamps A, B, C must light <b>one at a time</b>, in the order C, B, A, and repeat: 001 → 010 → 100 → back to 001. Design the circuit with JK flip-flops." + CW),
  sim=B.ctr([[2, 3, 5, 7]], "t7-6", "<p>A display must step through the <b>prime numbers</b> 2 → 3 → 5 → 7 and repeat (010 → 011 → 101 → 111 → back to 010). Design the counter with JK flip-flops." + CW))
q("t7-7", "More practice: 3-bit down counter", *B.ctr([[7, 6, 5, 4, 3, 2, 1, 0]], "t7-7", "<p>Design a 3-bit synchronous <b>down</b> counter (111 → 110 → … → 000 → back to 111) with JK flip-flops. Show the state table, logic functions and logic diagram.</p>"),
  sim=B.ctr([[0, 1, 3, 2, 6, 7, 5, 4]], "t7-8", "<p>Design a synchronous 3-bit <b>Gray code</b> counter (000 → 001 → 011 → 010 → 110 → 111 → 101 → 100 → back to 000) with JK flip-flops.</p>"))


def fdiv(f0, tgt, kind, key):
    n = round(math.log2(f0[0] / tgt[0]))
    assert f0[0] / 2 ** n == tgt[0] and f0[1] == tgt[1]
    return (f"<p>A {f0[0]} {f0[1]} clock must be divided down to {tgt[0]} {tgt[1]}. Design the circuit with {kind} flip-flops. Show the logic diagram and the waveforms.</p>",
            [[f"{f0[0]} ÷ {tgt[0]} = {2 ** n} = 2<sup>{n}</sup>, so you need <b>{n} toggle stages</b> in a ripple chain.", "Every toggling flip-flop halves the frequency. n stages divide by 2ⁿ."]] + p_ripple(n, kind, False, key, f0=f0)
            + [[f"Take the output from the last stage, <b>Q<sub>{n-1}</sub></b>: {tgt[0]} {tgt[1]}.", "Whether it counts up or down does not matter for dividing. Only the number of stages does."]],
            f"{n} {kind} flip-flops, each toggling, in a ripple chain. Output at Q<sub>{n-1}</sub>")


at("k2")
q("t6-5", "More practice: 4-bit ripple counter, JK flip-flops", "<p>Design a 4-bit binary ripple <b>count-up</b> counter using JK flip-flops. Show the logic diagram and the output waveforms.</p>", p_ripple(4, "JK", False, "t6-5"), "J = K = 1 on each, clock each stage from the previous Q' (rising edge)",
  sim=("<p>Design a 3-bit binary ripple <b>count-down</b> counter using JK flip-flops. Show the logic diagram and the output waveforms.</p>", p_ripple(3, "JK", True, "t6-6"), "J = K = 1 on each, clock each stage from the previous Q (rising edge)"))
q("t6-7", "Design in words: a clock divider", *fdiv((32, "kHz"), (4, "kHz"), "T", "t6-7"), sim=fdiv((1, "MHz"), (0.25, "MHz"), "D", "t6-8"))
at("k3")


def bcdq(ns):
    return ("<p>A BCD ripple counter starts at 0000. What does it show after " + ", ".join(map(str, ns[:-1])) + f" and {ns[-1]} count pulses?</p>",
            [["A BCD counter has 10 states (0 to 9) and then wraps, so only the remainder after dividing by 10 matters.", "Every 10 pulses bring it back to 0000."]]
            + [[f"{n} pulses: {n} = {n // 10} × 10 + {n % 10} → it shows {n % 10} = <b>{bits(n % 10, 4)}</b>.", ""] for n in ns],
            " · ".join(bits(n % 10, 4) for n in ns))


q("bcd-3", "More practice: where is the counter?", *bcdq([7, 13, 25]), sim=bcdq([9, 18, 34]))

# ===================================================================== extra practice · registers
at("r1")
q("reg-2", "More practice: Load control", *B.loadq("1100", [(1, "0101"), (0, "1111"), (1, "1000"), (0, "0011")]), sim=B.loadq("0000", [(0, "1010"), (1, "0110"), (1, "1001"), (0, "0001")]))
at("r2")
q("sh-3", "More practice: shift five bits in", *B.shq("1010", "11001"), sim=B.shq("0111", "0010"))
q("sh-4", "More practice: detect 0110 with a shift register", *B.shdet("0110"), sim=B.shdet("1011"))
at("r3")
q("st-2", "More practice: serial transfer", *B.xfer("1101", "0000"), sim=B.xfer("0101", "1110"))
q("sa-2", "More practice: serial addition", *B.sadd("0011", "0111"), sim=B.sadd("1001", "0101"))
at("r4")
q("us-2", "More practice: universal shift register", *B.usr("1001", [("01", "1"), ("01", "0"), ("10", "1"), ("11", "0011"), ("00", "")]), sim=B.usr("0000", [("11", "1100"), ("10", "1"), ("10", "1"), ("01", "0"), ("00", "")]))


def ringq(k, need):
    seq, r = [], "1" + "0" * (k - 1)
    while r not in seq:
        seq.append(r)
        r = r[-1] + r[:-1]
    assert len(seq) == k
    nb = math.ceil(math.log2(need))
    jf = math.ceil(need / 2)
    return (f"<p>(a) A {k}-bit ring counter starts at {seq[0]}. Give its sequence of states. (b) A system needs <b>{need}</b> timing signals, one after the other. How many flip-flops does that take with a ring counter, with a Johnson counter, and with a binary counter plus a decoder?</p>",
            [["(a) A ring counter is a shift register with its last output fed back to its first input. The single 1 goes round: " + " → ".join(seq) + f" → {seq[0]}.", f"{k} flip-flops give {k} states. Each output is 1 for one clock period in turn."],
             [f"(b) Ring counter: one flip-flop per timing signal → <b>{need}</b> flip-flops, no gates.", "Each flip-flop output is already a timing signal."],
             [f"Johnson counter: k flip-flops give 2k states → <b>{jf}</b> flip-flops, plus {need} two-input AND gates to decode the states.", "Feeding back the inverted output doubles the number of states."],
             [f"Binary counter + decoder: 2<sup>{nb}</sup> = {1 << nb} ≥ {need} → <b>{nb}</b> flip-flops, plus a {nb}-to-{1 << nb} decoder.", "Fewest flip-flops, but the decoder is the biggest piece of logic."]],
            f"Ring {need} · Johnson {jf} · binary counter {nb} + decoder")


at("r5")
q("rj-3", "More practice: ring, Johnson or counter + decoder", *ringq(4, 8), sim=ringq(5, 16))

# ===================================================================== extra practice · asynchronous logic


def asy(key, Y, z, tree):
    assert T_ms(tree, ["A", "B", "y"]) == minterms(Y, ["A", "B", "y"]), key  # the drawing and the equation are the same function
    return B.asy(key, Y, z, tree)


N = lambda x: ("NOT", x)
at("y1")
q("t9-5", "More practice: is it stable?", *asy("t9-5", "A'y + AB'", "A + y'", ("OR", ("AND", N("A"), "y"), ("AND", "A", N("B")))), sim=asy("t9-6", "(A + y')B", None, ("AND", ("OR", "A", N("y")), "B")))
q("t9-7", "More practice: two unstable columns", *asy("t9-7", "AB' + A'y'", None, ("OR", ("AND", "A", N("B")), ("AND", N("A"), N("y")))), sim=asy("t9-8", "(A ^ B)y + AB", "y", ("OR", ("AND", ("XOR", "A", "B"), "y"), ("AND", "A", "B"))))
at("y2")
q("as2-2", "More practice: two feedback loops", *B.as2("xy2' + x'y1", "x + y1y2", [(2, 1), (1, 0)]), sim=B.as2("x + y1y2", "xy1' + x'y2", [(1, 1), (2, 0)]))
at("y3")
F3 = p_flow2circ([[(0, 0), (1, 0), (1, 0), (0, 0)], [(0, 0), (1, 1), (1, 1), (1, 1)]], "fl-3")
F4 = p_flow2circ([[(0, 0), (0, 0), (1, 0), (1, 0)], [(1, 1), (0, 0), (1, 1), (1, 1)]], "fl-4")
q("fl-3", "More practice: flow table to circuit", "<p>Derive the logic circuit for this flow table (two states a and b, inputs x<sub>1</sub>x<sub>2</sub>, output z).</p>" + F3[0], F3[1], F3[2],
  sim=("<p>Derive the logic circuit for this flow table.</p>" + F4[0], F4[1], F4[2]))
at("y4")
q("ra-3", "More practice: is this race critical?", *B.race({0: 3, 1: 3, 3: 2, 2: 2}), sim=B.race({0: 3, 1: 1, 3: 2, 2: 2}))
at("y5")
q("t8-7", "More practice: three variables", *B.hz("AB' + BC", ABC, "t8-7"), sim=B.hz("A'C' + AB", ABC, "t8-8"))
q("t8-9", "More practice: four variables, two bridges", *B.hz("B'D' + A'BD + ACD", ABCD, "t8-9"), sim=B.hz("A'B'C' + BD + ACD'", ABCD, "t8-10"))

# ===================================================================== extra practice · memory, PLDs, transistors
at("m1")
q("mem-3", "More practice: address and data lines", *B.memq(4096, "4K", 8), sim=B.memq(1 << 20, "1M", 16))
at("m2")
q("rom-3", "More practice: inside a ROM", *B.romq(4, 8), sim=B.romq(10, 8))
at("m3")
q("pl-3", "More practice: a ROM as a look-up table", *B.lut(lambda x: 2 * x + 3, "y = 2x + 3", 5), sim=B.lut(lambda x: x * x, "y = x²", 6))
at("m4")
q("cm-3", "More practice: which transistors are on?", *B.cmos("NOR", 0, 1), sim=B.cmos("NAND", 0, 0))
