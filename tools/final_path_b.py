"""Study path, parts 4 to 7: counters, registers, asynchronous logic, memory / PLDs / transistors."""
from final_site import *

use(PATH)

# ===================================================================== counters
part("Counters")


def ctr(cycles, key, prompt, two=False):
    st, R = p_counter(cycles, ABC, key, twomode=two)
    return (prompt, st, EQ3(R))


def modes(cycles):
    return "".join(f"<br><b>Mode {i+1}:</b> " + " → ".join(bits(x, 3) for x in c) + f" → back to {bits(c[0], 3)}." for i, c in enumerate(cycles))


TWO = "<p>Use JK flip-flops to design a 3-bit synchronous state machine with two modes, depending on its initial state.{}</p><p>One circuit block only. Show the state table, logic functions and logic diagram.</p>"
topic("k1", "Designing a synchronous counter", "Lectures 17–18, slides 2–10 · 23/24 Q3", pri=3,
      learn=f"""<p>A <b>counter</b> is a sequential circuit whose state is its output: every clock edge it steps to the next state. <b>Modulo-N</b> = N states, then wrap.</p>
<p><b>Synchronous</b> = every flip-flop gets the same clock. Gates on the J and K inputs decide which bits change. Design = find those gates. It is the detector method with no input X: the next state is simply the next number in the count.</p>
<ol><li><b>State table:</b> present state → next state.</li><li><b>Excitation:</b> for each flip-flop, present bit → next bit gives J K.{table(["Q → Q<sup>+</sup>", "J K"], [["0 → 0", "0 x"], ["0 → 1", "1 x"], ["1 → 0", "x 1"], ["1 → 1", "x 0"]], "tt small")}</li><li><b>K-map</b> each J and K (variables = the state bits). Unused states are x in every map.</li><li><b>Draw</b> the flip-flops and gates.</li><li><b>Check the unused states (slides 9–10):</b> push each one through the final equations. It must find its way back into the count. If it does not, give it a real next state and redesign.</li></ol>
<p><b>Two loops in one circuit (23/24 Q3):</b> nothing new. Put both loops in the same state table. If they use all 8 states there are no don't cares.</p>""",
      check=("Row 011 → 100. What is J K for the middle flip-flop (B)?", "B goes 1 → 0, so <b>J K = x 1</b>."))
q("t7-1", "Slides 4–10: modulo-5 counter", *ctr([[0, 1, 2, 3, 4]], "t7-1", "<p>Design a synchronous counter that counts 000 → 001 → 010 → 011 → 100 → 000 using JK flip-flops. Check the unused states.</p>"),
  sim=ctr([[0, 1, 2, 3, 4, 5]], "t7-2", "<p>Design a synchronous 0 to 5 counter with JK flip-flops. Is it self-correcting?</p>"))
C1, C2 = [[0, 2, 3, 6, 5], [1, 4, 7]], [[1, 3, 2, 6, 4], [0, 5, 7]]
q("t7-3", "Two loops in one circuit", *ctr(C1, "t7-3", TWO.format(modes(C1)), True), sim=ctr(C2, "t7-4", TWO.format(modes(C2)), True))
put(EX["pp-3"])

topic("k2", "Ripple counters and frequency division", "Lectures 17–18, slides 11–16 · 23/24 Q2(a)", pri=3,
      learn=f"""<p>A <b>ripple counter</b> is a chain of flip-flops that each <b>toggle</b>. Only the first one gets the count pulses. <b>Each later one is clocked by the flip-flop before it.</b></p>
{img(seq("ripple4-counter"), "ripple counter", True)}
<p>Slide 16 asks how to build it with other flip-flops and how to count down:</p>
{table(["To make it toggle", "Connect"], [["T flip-flop", "T = 1"], ["JK flip-flop", "J = K = 1"], ["D flip-flop", M("D = Q'") + " (its own inverted output)"]])}
{table(["Flip-flop edge", "Clock next stage from", "Counts"], [["falling", "Q", "up (the slides' circuit)"], ["falling", "Q'", "<b>down</b>"], ["rising", "Q'", "up"], ["rising", "Q", "<b>down</b>"]])}
<p><b>Why:</b> counting up, a bit flips when the bit below it <b>falls</b> (carry). Counting down, it flips when the bit below <b>rises</b> (borrow). Pick the connection that gives the next flip-flop its active edge at that moment.</p>
<p><b>Frequency divider (slide 15):</b> every stage halves the frequency: f<sub>0</sub>/2, f<sub>0</sub>/4, f<sub>0</sub>/8 … n stages → ÷ 2ⁿ.</p>
<p><b>Ripple against synchronous:</b> ripple needs no gates but is slow, because the change passes through each flip-flop in turn.</p>""",
      check=("Falling-edge flip-flops, each clocked from the previous Q. Up or down?", "<b>Up.</b> A falling edge on Q is a 1 → 0 change, which is when a carry happens."))
q("t6-1", "Count up with D flip-flops", "<p>Design a 3-bit binary ripple <b>count-up</b> counter using D flip-flops. Show the logic diagram and output waveforms.</p>", p_ripple(3, "D", False, "t6-1"), "D = Q' on each, clock each stage from the previous Q' (rising edge)",
  sim=("<p>Design a 2-bit ripple count-down counter with T flip-flops. Draw the waveforms.</p>", p_ripple(2, "T", True, "t6-2"), "T = 1, clock stage 2 from Q<sub>0</sub>"))
FD = lambda f0, key, tgt, st_: p_ripple(4, "JK", False, key, f0=f0)[4:] + [[f"{tgt} = {f0[0]} {f0[1]} ÷ {2 ** (st_ + 1)} = clock ÷ 2<sup>{st_ + 1}</sup> → stage {st_ + 1}, output <b>Q<sub>{st_}</sub></b>.", "Divide by 2 for each stage you pass through."]]
q("t6-3", "Frequency divider numbers", "<p>A 4-stage ripple counter (JK, J = K = 1) is driven by an 800 kHz clock. What frequency is at each output? Which output gives 100 kHz?</p>", FD((800, "kHz"), "t6-3", "100 kHz", 2), "400, 200, 100, 50 kHz · 100 kHz is at Q<sub>2</sub>",
  sim=("<p>A 4-stage ripple counter is driven by a 2 MHz clock. What frequency is at each output? Which output gives 125 kHz?</p>", FD((2, "MHz"), "t6-4", "125 kHz = 0.125 MHz", 3), "1, 0.5, 0.25, 0.125 MHz · 125 kHz is at Q<sub>3</sub>"))
put(EX["pp-2a"])

B = bcd_ripple()
brow = lambda i: [i, " ".join(map(str, B[i])), B[i][0] * 8 + B[i][1] * 4 + B[i][2] * 2 + B[i][3]]
topic("k3", "BCD ripple counter", "Lectures 17–18, slides 17–20", pri=2,
      learn=f"""<p>A <b>BCD (decade) counter</b> counts 0000 to 1001 (0 to 9), then goes back to 0000. Four falling-edge JK flip-flops Q<sub>8</sub>Q<sub>4</sub>Q<sub>2</sub>Q<sub>1</sub>.</p>
{table(["Flip-flop", "Clocked by", "J", "K", "So it…"], [["Q<sub>1</sub>", "count pulses", "1", "1", "toggles every pulse"], ["Q<sub>2</sub>", "Q<sub>1</sub>", "<b>Q<sub>8</sub>'</b>", "1", "toggles when Q<sub>1</sub> falls, but only while Q<sub>8</sub> = 0"], ["Q<sub>4</sub>", "Q<sub>2</sub>", "1", "1", "toggles when Q<sub>2</sub> falls"], ["Q<sub>8</sub>", "Q<sub>1</sub>", "<b>Q<sub>2</sub>Q<sub>4</sub></b>", "1", "sets when Q<sub>1</sub> falls with Q<sub>2</sub> = Q<sub>4</sub> = 1, clears on the next fall of Q<sub>1</sub>"]])}
<p><b>More digits:</b> chain decade counters, one per decimal digit. Each decade's Q<sub>8</sub> clocks the next: it falls on 9 → 0, which is the carry.</p>""",
      check=("How is a BCD counter different from a 4-bit binary counter?", "After <b>1001</b> (9) it returns to 0000. A binary counter would carry on to 1010 … 1111."))
q("bcd-1", "Why 7 → 8 and 9 → 0 work", "<p>For the BCD ripple counter in the notes, explain using the J and K values what happens on the pulses that take it (a) from 7 to 8 and (b) from 9 to 0.</p>",
  [["The full count, simulated from the connections in the table:" + table(["Pulse", "Q<sub>8</sub> Q<sub>4</sub> Q<sub>2</sub> Q<sub>1</sub>", "Value"], [brow(i) for i in range(11)]), "Each row follows from the one before using only the four J, K and clock connections."],
   ["(a) At 0111 the pulse makes Q<sub>1</sub> fall, which clocks Q<sub>2</sub> and Q<sub>8</sub>. Q<sub>2</sub>: J = Q<sub>8</sub>' = 1, K = 1 → toggles to 0. Its fall clocks Q<sub>4</sub>, which toggles to 0. Q<sub>8</sub>: J = Q<sub>2</sub>Q<sub>4</sub> = 1, K = 1 → toggles to 1. Result <b>1000</b>.", "J and K are read as they were just before the edge, so Q<sub>8</sub> still sees Q<sub>2</sub> = Q<sub>4</sub> = 1."],
   ["(b) At 1001 the pulse makes Q<sub>1</sub> fall again. Q<sub>2</sub>: J = Q<sub>8</sub>' = <b>0</b>, K = 1 → reset, stays 0 (a binary counter would have set it). Q<sub>8</sub>: J = Q<sub>2</sub>Q<sub>4</sub> = 0, K = 1 → reset to 0. Result <b>0000</b>.", "J<sub>2</sub> = Q<sub>8</sub>' is the gate that blocks 1010. K = 1 on Q<sub>8</sub> clears it."]],
  "7 → 8: Q<sub>8</sub> toggles because J = Q<sub>2</sub>Q<sub>4</sub> = 1. 9 → 0: Q<sub>2</sub> is held at 0 by J = Q<sub>8</sub>' = 0 and Q<sub>8</sub> resets.")
q("bcd-2", "Slide 20: multi-decade counter", "<p>How many flip-flops does a BCD counter need to count 000 to 999? How are the decades connected?</p>",
  [["One decade counter (4 flip-flops) per decimal digit: 3 × 4 = <b>12</b>.", "Each digit is stored separately as a 4-bit BCD code."], ["Count pulses go to the units decade. Its Q<sub>8</sub> is the clock of the tens decade, and the tens' Q<sub>8</sub> clocks the hundreds.", "Q<sub>8</sub> falls only on 9 → 0. That is exactly when the next digit must go up by one."]],
  "12 flip-flops, each decade's Q<sub>8</sub> clocks the next",
  sim=("<p>A BCD counter must count 0000 to 9999. How many flip-flops? How many would a plain binary counter need to count that high?</p>",
       [["4 digits × 4 = <b>16</b> flip-flops.", "One decade per digit."], ["Binary: 2<sup>13</sup> = 8192 is too small, 2<sup>14</sup> = 16384 is enough → <b>14</b>.", "BCD wastes 6 of every 16 codes, so it needs more flip-flops for the same range."]], "16 (BCD) · 14 (binary)"))

# ===================================================================== registers
part("Registers")


def loadq(start, ops):
    r, rows = start, []
    for ld, i in ops:
        r = i if ld else r
        rows.append([len(rows) + 1, ld, " ".join(i), "<b>" + " ".join(r) + "</b>"])
    return ("<p>A 4-bit register with a Load control holds " + start + ". On the next clock edges (Load, inputs I<sub>3</sub>…I<sub>0</sub>) are: " + ", ".join(f"({l}, {i})" for l, i in ops) + ". Give the contents after each edge.</p>",
            [["Load = 1 → take in the inputs. Load = 0 → keep the old word.", "Each flip-flop gets D = Load·I + Load'·Q: a 2-to-1 mux choosing between the new bit and its own output."],
             ["Edge by edge:" + table(["Edge", "Load", "Inputs", "Contents"], rows), "With Load = 0 the inputs are ignored completely."]], "Ends holding " + r)


topic("r1", "Registers and parallel load", "Lecture 19, slides 2–7", pri=2,
      learn="""<p>A <b>register</b> = a group of flip-flops sharing one clock, one bit each. n flip-flops store an n-bit word. Gates around them decide <b>how</b> new data gets in.</p>
<p><b>Parallel load:</b> all bits go in at once, on one clock edge. A common asynchronous <b>clear</b> wipes it to 0000.</p>
<p>A plain D register reloads on <b>every</b> edge. A <b>Load</b> input fixes that: Load = 1 loads the inputs, Load = 0 feeds each Q back to its own D so the word is kept.</p>""",
      check=("How many flip-flops store one byte?", "<b>8.</b> One flip-flop per bit."))
q("reg-1", "Register with a Load control", *loadq("1010", [(0, "0111"), (1, "0111"), (0, "1100"), (1, "0001")]), sim=loadq("0011", [(1, "1001"), (0, "1111"), (0, "0000"), (1, "0110")]))


def shq(start, word):
    rows, r = shift_rows(start, word)
    return (f"<p>A 4-bit shift-right register holds {start}. The bits {', '.join(word)} arrive at the serial input, one per clock edge. Give the contents after each edge.</p>",
            [["Every edge, every bit moves one place to the right. The new bit enters at the left. The right-hand bit is lost (it is the serial output).", "Each flip-flop's D is wired to the Q on its left, so each one copies its neighbour."],
             ["Edge by edge:" + table(["After edge", "Serial in", "Q<sub>3</sub> Q<sub>2</sub> Q<sub>1</sub> Q<sub>0</sub>"], rows), "An n-bit word needs n edges to get in, and n more to shift out again."]], "Ends holding " + r)


def shdet(pat):
    n = len(pat)
    lit = [f"Q{i}" + ("" if pat[i] == "1" else "'") for i in reversed(range(n))]
    e = "".join(lit)
    random.seed(3)
    r, h = "0" * n, ""
    for _ in range(300):  # the AND gate fires exactly when the last n bits are the pattern
        b = random.choice("01")
        h += b
        r = b + r[:-1]
        assert ev(e, {f"Q{i}": int(r[n - 1 - i]) for i in range(n)}) == int(h.endswith(pat))
    return (f"<p>How can a {n}-bit shift register be used to detect the sequence <b>{pat}</b> (first bit arrives first)?</p>",
            [[f"Feed the input into the serial input. After every edge the register holds the <b>last {n} input bits</b>: the newest in Q<sub>{n-1}</sub>, the oldest in Q<sub>0</sub>.", "A shift register is a memory of recent inputs, which is all a detector needs."],
             [f"The first bit of the pattern is the oldest, so it ends up in Q<sub>0</sub>. When the whole pattern is in: " + ", ".join(f"Q<sub>{i}</sub> = {pat[i]}" for i in range(n)) + ".", "The pattern sits in the register back to front."],
             ["AND the outputs, inverting the ones that should be 0:" + DD("Z = " + e), "One AND gate, no state diagram. It costs more flip-flops than a state machine (4 against 2 for 1001)."]], M("Z = " + e))


topic("r2", "Shift registers", "Lecture 19, slides 8–12", pri=3,
      learn=f"""<p>Flip-flops in a chain: each Q feeds the next D. <b>Every clock edge, every bit moves one place.</b> A new bit enters at the serial input. The last bit leaves at the serial output.</p>
{img(seq("shift-register"), "shift register", True)}
<p>A <b>shift control</b> (like Load) lets the register ignore the clock when it should not shift.</p>""",
      check=("A 4-bit shift-right register holds 1011. Serial in = 0 for two edges. Contents?", "1011 → 0101 → <b>0010</b>."))
q("sh-1", "Slide 10: shifting 1001 in", *shq("0000", "1001"), sim=shq("1100", "0110"))
q("sh-2", "Slide 11: shift register as a sequence detector", *shdet("1001"), sim=shdet("1101"))


def xfer(a, b):
    rows, A, Bb = [["start", a, b]], a, b
    for i in range(len(a)):
        bit = A[-1]
        A, Bb = bit + A[:-1], bit + Bb[:-1]
        rows.append([f"T{i+1}", A, Bb])
    assert Bb == a and A == a
    return (f"<p>Register A holds {a} and register B holds {b}. Both shift right. A's serial output feeds B's serial input <b>and</b> A's own serial input. Give both registers after each of 4 clock edges.</p>",
            [["On each edge the right-hand bit of A leaves. It goes into the left of B, and also back into the left of A.", "Feeding A's output back to its own input stops the word being lost: it recirculates."],
             [table(["", "A", "B"], rows), f"After {len(a)} edges B holds A's word, and A is back where it started."]], f"A = {A}, B = {Bb}")


def sadd(a, b):
    n, A, c, rows = len(a), a, 0, []
    for i in range(n):
        x, y = int(A[-1]), int(b[n - 1 - i])
        s, c2 = x ^ y ^ c, (x & y) | (x & c) | (y & c)
        A = str(s) + A[:-1]
        rows.append([i + 1, x, y, c, f"<b>{s}</b>", c2, A])
        c = c2
    assert int(A, 2) + (c << n) == int(a, 2) + int(b, 2)
    return (f"<p>A serial adder adds A = {a} and B = {b}. The carry flip-flop starts at 0 and the sum is shifted back into A. Trace it for {n} clock edges.</p>",
            [["Both registers shift right, so the <b>least significant bits come out first</b>. One full adder adds the two bits and the stored carry.", "Add from the right, exactly as on paper."],
             ["The sum bit shifts into the left of A. The carry out is stored in a D flip-flop for the next bit:" + table(["Edge", "A bit", "B bit", "Carry in", "Sum", "Carry out", "A after"], rows),
              "The flip-flop is what lets one full adder do the job of n: it remembers the carry between bits."],
             [f"After {n} edges A holds the sum: <b>{A}</b>" + (" with a final carry of 1." if c else "."), f"{int(a, 2)} + {int(b, 2)} = {int(a, 2) + int(b, 2)}. ✓ A parallel adder needs {n} full adders and one step. This needs 1 full adder and {n} clock edges."]], f"A = {A}" + (", carry 1" if c else ""))


topic("r3", "Serial transfer and serial addition", "Lecture 19, slides 13–16", pri=3,
      learn="""<p><b>Parallel transfer:</b> all bits move at once, in one clock edge.<br><b>Serial transfer:</b> one bit per edge, from one shift register into another. n bits take n edges.</p>
<p>To stop the first register losing its word, connect its output back to <b>its own input</b>.</p>
<p><b>Serial adder:</b> two shift registers feed <b>one full adder</b>, one bit pair per clock, least significant bit first. A <b>D flip-flop holds the carry</b> for the next bit. The sum shifts back into register A.</p>""",
      check=("What is the D flip-flop in a serial adder for?", "It <b>holds the carry</b> from this bit so it can be added to the next bit on the next clock edge."))
q("st-1", "Slide 14: serial transfer", *xfer("1011", "0010"), sim=xfer("0110", "1001"))
q("sa-1", "Serial addition", *sadd("0101", "0110"), sim=sadd("1011", "0011"))


def usr(start, ops):
    r, rows = start, []
    nm = {"00": "no change", "01": "shift right", "10": "shift left", "11": "parallel load"}
    for s, arg in ops:
        r = {"00": r, "01": arg + r[:-1], "10": r[1:] + arg, "11": arg}[s] if s != "00" else r
        rows.append([len(rows) + 1, s, nm[s], arg or "–", "<b>" + r + "</b>"])
    return (f"<p>A 4-bit universal shift register holds {start}. On successive clock edges (s<sub>1</sub>s<sub>0</sub>, serial or parallel input) are: " + ", ".join(f"({s}, {a or '–'})" for s, a in ops) + ". Give the contents after each edge.</p>",
            [["The two select lines choose what every flip-flop loads: 00 no change · 01 shift right · 10 shift left · 11 parallel load.", "A 4-to-1 mux sits in front of each flip-flop. s<sub>1</sub>s<sub>0</sub> is the mux select."],
             [table(["Edge", "s<sub>1</sub>s<sub>0</sub>", "Operation", "Input", "Contents"], rows), "Shift right: the serial bit enters at the left. Shift left: it enters at the right."]], "Ends holding " + r)


topic("r4", "Universal shift register", "Lecture 19, slides 17–19", pri=2,
      learn=f"""<p>One register that can do everything: clear, hold, shift right, shift left, parallel load, with serial and parallel inputs and outputs.</p>
<p>In front of <b>each</b> flip-flop sits a <b>4-to-1 mux</b>. Two select lines s<sub>1</sub>s<sub>0</sub> choose what it loads. A 4-bit register needs 4 flip-flops and 4 muxes.</p>
{img(seq("universal-stage"), "one stage", True)}
{table(["s<sub>1</sub> s<sub>0</sub>", "Mux input", "Operation"], [["0 0", "0", "<b>no change</b> (own output fed back)"], ["0 1", "1", "<b>shift right</b>"], ["1 0", "2", "<b>shift left</b>"], ["1 1", "3", "<b>parallel load</b>"]])}""",
      check=("s<sub>1</sub>s<sub>0</sub> = 10. What happens on the next edge?", "<b>Shift left.</b>"))
q("us-1", "Trace a universal shift register", *usr("0000", [("11", "1011"), ("01", "0"), ("01", "1"), ("00", ""), ("10", "1")]), sim=usr("1111", [("10", "0"), ("10", "0"), ("11", "0101"), ("01", "1"), ("00", "")]))

J4, J3 = johnson(4), johnson(3)
D4, D3 = johnson_decode(J4, list("ABCE")), johnson_decode(J3, ABC)
assert D4 == ["A'E'", "AB'", "BC'", "CE'", "AE", "A'B", "B'C", "C'E"]  # slide 8
jrows = lambda J, Dd: [[f"t<sub>{i}</sub>", " ".join(s), M(d)] for i, (s, d) in enumerate(zip(J, Dd))]
topic("r5", "Ring counter and Johnson counter", "Lecture 20", pri=3,
      learn=f"""<p><b>Ring counter:</b> a shift register joined into a circle (last output → first input) holding <b>a single 1</b>. 1000 → 0100 → 0010 → 0001 → 1000. Each output is high for one clock in turn: ready-made <b>timing signals</b>.</p>
{img(seq("ring-counter"), "ring counter", True)}
<p>Cost: <b>n flip-flops give only n states.</b> Alternative for 2ⁿ timing signals: an n-bit binary counter + an n-to-2ⁿ decoder.</p>
<p><b>Johnson (switch-tail) counter:</b> same circle, but feed back the <b>inverted</b> last output. <b>k flip-flops give 2k states.</b> It fills with 1s from the left, then with 0s.</p>
{img(seq("johnson-counter"), "Johnson counter", True)}
<p><b>Decoding:</b> each of the 2k states needs only <b>one 2-input AND gate</b>. Look at the place where the pattern changes from 1 to 0 (or at the two ends).</p>""",
      check=("5 flip-flops: how many states as a ring counter? As a Johnson counter?", "Ring <b>5</b>. Johnson <b>10</b>."))
q("rj-1", "Slides 6–9: 4-bit Johnson counter", "<p>A 4-bit Johnson counter (flip-flops A, B, C, E) starts at 0000. Give its sequence of states and a 2-input AND gate that decodes each one.</p>",
  [["Each edge everything shifts right, and the <b>inverse of E</b> enters A:" + table(["", "A B C E"], [r[:2] for r in jrows(J4, D4)]), "While E = 0 a 1 is fed in, so 1s fill from the left. Once E = 1, 0s are fed in."],
   ["8 states from 4 flip-flops. For each state find two bits that pick it out from the other seven:" + table(["", "A B C E", "Decode"], jrows(J4, D4)),
    "1100 is the only state with B = 1 and C = 0 → BC'. The all-0 and all-1 states use the two end bits: A'E' and AE."]], "8 states · decoding: " + ", ".join(D4),
  sim=("<p>A 3-bit Johnson counter (A, B, C) starts at 000. Give its sequence and a 2-input AND gate for each state.</p>",
       [["Shift right, feeding C' into A:" + table(["", "A B C", "Decode"], jrows(J3, D3)), "2 × 3 = 6 states. The codes 010 and 101 never occur."]], "6 states · decoding: " + ", ".join(D3)))
JB = {}
for bit, nm in ((2, "Y2"), (1, "Y1"), (0, "Y0")):
    on = [int(s, 2) for i, s in enumerate(J3) if (i >> bit) & 1]
    JB[nm] = cover_tex(mincover(3, on, [2, 5]), ABC)
for i, s in enumerate(J3):  # the three outputs spell the count 0..5
    env = {"A": int(s[0]), "B": int(s[1]), "C": int(s[2])}
    assert sum(ev(JB[f"Y{b}"], env) << b for b in range(3)) == i
q("rj-2", "Slide 10 exercise: Johnson counter to binary 0–5", "<p>Use a 3-bit Johnson counter and external gates to design a binary counter output counting 0 to 5. Show the design procedure.</p>",
  [["A 3-bit Johnson counter has 6 states, one for each count. List them in order with the binary number each should show:" + table(["A B C", "Count", "Y<sub>2</sub> Y<sub>1</sub> Y<sub>0</sub>"], [[" ".join(s), i, " ".join(bits(i, 3))] for i, s in enumerate(J3)]),
    "The Johnson counter does the counting. The gates only translate its code into binary."],
   ["The codes 010 and 101 never happen → <b>don't cares</b>. K-map each output with A, B, C as the variables:" + "".join(DD(f"{k} = {v}") for k, v in JB.items()), "Three small K-maps, each with two x's to help."],
   ["Circuit: three D flip-flops in a ring with C' fed back to the first D, plus these gates on the outputs.", "Check one state: 110 is count 2. Y<sub>2</sub>Y<sub>1</sub>Y<sub>0</sub> = 010. ✓"]],
  " · ".join(M(f"{k} = {v}") for k, v in JB.items()))

# ===================================================================== asynchronous
part("Asynchronous logic")


def asy(key, Y, z, tree):
    draw_tree(key, tree, "Y", feedback="y")
    a, b, c, info = p_async(Y, z, ["A", "B"], key)
    ans = ("Unstable (oscillates) when AB = " + ", ".join(bits(info[0][i], 2) for i in info[2])) if info[2] else "No stability issue"
    return (img(key, "circuit") + (f"<p>The output is {M('z = ' + z)}.</p>" if z else "") + "<p>(a) Transition table. (b) Flow table. (c) Is there a stability issue?</p>", a + b + c, ans)


topic("y1", "Transition table, flow table, stability", "Lectures 23–24, slides 2–23 · 23/24 Q4", pri=3,
      learn=f"""<p>An <b>asynchronous</b> sequential circuit has <b>no clock</b>. The state changes as soon as an input changes. It remembers through a <b>feedback wire</b> (the gate delays are the memory).</p>
<p>Cut the loop. The same wire now has two names:</p>
{table(["Name", "Slides call it", "Means"], [["<b>Y</b> (capital), leaving the gate", "excitation variable", "next state"], ["<b>y</b> (small), coming back in", "secondary variable", "present state"]])}
$$\\text{{stable}} \\iff Y = y$$
<p><b>Transition table (slide 14):</b></p>
<ol><li>Find the feedback loop. Call its output Y and its input y.</li><li>Write Y as a function of the inputs and y.</li><li>Map: rows = y, columns = inputs in K-map order (00, 01, 11, 10), entry = Y.</li><li><b>Circle</b> every entry where Y = the row's y.</li></ol>
{img(seq("transition-table"), "example", True)}
<p><b>Total state</b> = internal state + inputs together. <b>Flow table</b> = the same table with letters (a, b …) for the states, plus the output.</p>
<p><b>Stability:</b> look down each <b>column</b>. A column with <b>no circle</b> means the circuit never settles for that input: it <b>oscillates</b>, with period 2 × the loop delay.</p>
<p><b>Fundamental mode:</b> inputs change <b>one at a time</b>, and only <b>after the circuit has settled</b>.</p>""",
      check=(f"{M('Y = x' + chr(39) + 'y + xy' + chr(39))}. For which x does it oscillate?", f"<b>x = 1.</b> Then {M('Y = y' + chr(39))}: Y is never equal to y. With x = 0, Y = y, always stable."))
q("t9-1", "A circuit that remembers", *asy("t9-1", "AB + Ay + By", None, ("OR", ("AND", "A", "B"), ("AND", "A", "y"), ("AND", "B", "y"))), sim=asy("t9-2", "A'B + By'", "Ay", ("OR", ("AND", ("NOT", "A"), "B"), ("AND", "B", ("NOT", "y")))))
s18 = asy("t9-3", "(Ay)'B", None, ("AND", ("NAND", "A", "y"), "B"))
s18[1].append(["The slides' cure (slide 23): invert y before the first gate, so Y = A'B + yB. Then column 11 gives Y = y and both of its states are stable.", "With y' feeding back the loop inverted an odd number of times. Inverting y makes it even, so the loop holds its value."])
q("t9-3", "Slides 18–22: the unstable NAND loop", s18[0].replace("<p>(a)", "<p>(The slides call the inputs x<sub>1</sub>, x<sub>2</sub>. Here A = x<sub>1</sub>, B = x<sub>2</sub>.)</p><p>(a)"), s18[1], s18[2],
  sim=asy("t9-4", "A'B + By", None, ("OR", ("AND", ("NOT", "A"), "B"), ("AND", "B", "y"))))
q("fm-1", "Fundamental mode", "<p>(a) What is fundamental mode, and why is it needed? (b) Give two reasons for using asynchronous circuits at all.</p>",
  [["(a) Inputs change <b>one at a time</b>, and the next change comes only <b>after the circuit has reached a stable state</b>.", "If two inputs change together you cannot tell which arrives first, because the paths have different delays. If an input changes mid-transition the circuit may never settle."],
   ["(b) Any two of: <b>speed</b> (it responds at once, without waiting for a clock edge) · <b>interfacing</b> two circuits that have independent clocks · understanding large synchronous systems where one global clock no longer holds.", "Slide 4. The price is that they are hard to design."]],
  "One input change at a time, only when stable · speed, interfacing independent clocks")
put(EX["pp-4a"])
put(EX["pp-4b"])
put(EX["pp-4c"])


def as2(Y1, Y2, moves):
    tab = async2(Y1, Y2)
    out, ans = [], []
    for y, x in moves:
        assert tab[(y, 1 - x)] == y  # starts in a stable total state
        path, ok = settle(tab, y, x)
        assert ok and all(bin(a ^ b).count("1") == 1 for a, b in zip(path, path[1:]))
        out.append(f"Stable at {bits(y, 2)} with x = {1 - x}, then x → {x}: move across to column {x}, then " + " → ".join(bits(p, 2) for p in path) + f". Settles at <b>{bits(path[-1], 2)}</b>.")
        ans.append(bits(path[-1], 2))
    e1 = ev(Y1, {"x": 0, "y1": 0, "y2": 1})
    e2 = ev(Y2, {"x": 0, "y1": 0, "y2": 1})
    eqs = DD("Y1 = " + Y1 + " \\qquad Y2 = " + Y2)
    pr = "<p>An asynchronous circuit has one input x and two feedback loops:</p>" + eqs + "<p>(a) Derive the transition table. (b) " + " ".join(f"It is stable in y<sub>1</sub>y<sub>2</sub> = {bits(y, 2)} with x = {1 - x}. x changes to {x}. Where does it settle?" for y, x in moves) + "</p>"
    return (pr, [["Two loops → two state variables → 4 rows (in the order 00, 01, 11, 10) and one column per value of x. Each entry is Y<sub>1</sub>Y<sub>2</sub>.", "Rows are the present state y<sub>1</sub>y<sub>2</sub>. The entry is the next state the logic is asking for."],
                 [f"Work out both equations in every cell. Example, row 01, x = 0: Y<sub>1</sub> = {e1}, Y<sub>2</sub> = {e2} → entry {e1}{e2}." + tt2(tab), "Circle an entry when it equals its own row label: that total state is stable."],
                 ["(b) " + ul(out), "An input change moves you <b>sideways</b> to the new column. An uncircled entry then moves you <b>up or down</b> to the row it names. Repeat until you land on a circle."]], "Settles at " + ", ".join(ans))


topic("y2", "Two state variables", "Lectures 23–24, slides 13–16", pri=2,
      learn="""<p>With two feedback loops there are two state variables y<sub>1</sub>y<sub>2</sub>, so the transition table has <b>4 rows</b>, written in the order 00, 01, 11, 10.</p>
<p>Each entry is the pair Y<sub>1</sub>Y<sub>2</sub>. It is <b>stable</b> (circled) when it equals its own row label.</p>
<p><b>Reading the table:</b> x changes → move <b>sideways</b> to the new column. If the entry is not circled, move <b>up or down</b> to the row it names. Keep going until you reach a circle.</p>""",
      check=("Row 01 has the entry 11 under x = 0. Stable?", "<b>No.</b> 11 ≠ 01. The circuit will move to row 11."))
q("as2-1", "Slide 15: two feedback loops", *as2("xy1 + x'y2", "xy1' + x'y2", [(0, 1), (1, 0)]), sim=as2("x'y1 + xy2", "x'y1' + xy2", [(0, 0), (1, 1)]))

topic("y3", "From a flow table to a circuit", "Lectures 23–24, slide 17", pri=3,
      learn="""<p>The reverse direction (design): you are given the <b>flow table</b> and must produce the circuit.</p>
<ol><li><b>Assign binary numbers</b> to the states (a = 0, b = 1). The flow table becomes a transition table.</li><li>The transition table <b>is a K-map</b> of Y. Simplify it.</li><li>Make a second map for the <b>output</b> z and simplify.</li><li><b>Draw</b> the logic, with Y fed back as y.</li></ol>""",
      check=("In a flow table, what does a circled letter mean?", "A <b>stable</b> state: the next state is the same as the present state for that input."))
F1 = p_flow2circ([[(0, 0), (0, 0), (0, 0), (1, 0)], [(0, 0), (0, 0), (1, 1), (1, 0)]], "fl-1")
assert F1[2] == M("Y = x1y + x1x2'") + " · " + M("z = x1x2y")  # slide 17
F2 = p_flow2circ([[(0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (1, 0), (1, 1), (0, 0)]], "fl-2")
q("fl-1", "Slide 17: derive the circuit", "<p>Derive the logic circuit for this flow table (two states a and b, inputs x<sub>1</sub>x<sub>2</sub>, output z).</p>" + F1[0], F1[1], F1[2],
  sim=("<p>Derive the logic circuit for this flow table.</p>" + F2[0], F2[1], F2[2]))


def race(col):
    st, a = p_race(col)
    tab = {(0, 0): 0}
    tab.update({(y, 1): t for y, t in col.items()})
    return ("<p>Part of a transition table is shown (only the entries that matter). The circuit is stable in 00 with x = 0, then x changes to 1. List the possible transitions. Is there a race, and is it critical?</p>" + tt2(tab), st, a)


topic("y4", "Races", "Lectures 23–24, slides 24–29", pri=3,
      learn=f"""<p><b>Race:</b> <b>two or more state variables</b> must change after one input change. The feedback paths have unequal delays, so you cannot know which changes first.</p>
<p>00 → 11 might really go 00 → <b>10</b> → 11 or 00 → <b>01</b> → 11.</p>
{table(["", "Final stable state", ""], [["<b>Non-critical race</b>", "the same whichever variable wins", "harmless"], ["<b>Critical race</b>", "<b>different</b> depending on which wins", "must be removed"]])}
<p><b>Cure (slide 29):</b> choose the binary codes of the states so that <b>only one state variable changes</b> on every transition.</p>
<p>A race is about <b>state variables</b>. A hazard (7.5) is about <b>path delays in the gates</b>. Do not mix them up.</p>""",
      check=("A transition goes from state 01 to state 10. Is there a race?", "<b>Yes</b>: both bits change. Whether it is critical depends on where the in-between states 00 and 11 lead."))
q("ra-1", "Slide 27: is this race critical?", *race({0: 3, 1: 1, 3: 1, 2: 3}), sim=race({0: 3, 1: 3, 3: 3, 2: 3}))
q("ra-2", "Slide 28: is this race critical?", *race({0: 3, 1: 3, 3: 3, 2: 2}), sim=race({0: 3, 1: 1, 3: 3, 2: 2}))


def hz(e, names, key, exp=None, lead=True):
    assert exp is None or minterms(exp, names) == minterms(e, names), e
    st, ans = p_hazard(e, names, key, expanded=exp)
    return (f"<p>Implement {M('F = ' + e)} without static-1 hazards, using the fewest gates.</p>", st, M("F = " + ans))


topic("y5", "Static hazards", "Lectures 23–24, slides 30–38 · 23/24 Q2(b)", pri=3,
      learn=f"""<p>A <b>hazard</b> is a short unwanted glitch at an output. Cause: one input reaches the output along <b>two paths with different delays</b> (one usually goes through an inverter). It happens in plain combinational logic.</p>
{img(seq("hazard-glitch"), "glitch", True)}
{table(["Hazard", "Output should", "Actually", "Found in"], [["static-1", "stay 1", "1 → 0 → 1", "sum of products (AND-OR)"], ["static-0", "stay 0", "0 → 1 → 0", "product of sums (OR-AND)"], ["dynamic", "change once", "three or more transitions", ""]])}
<p><b>On a K-map:</b> a static-1 hazard exists wherever <b>two neighbouring 1s are in different groups</b>.</p>
{img(seq("hazard-kmap"), "bridge", True)}
<p><b>Fix:</b> add one more group that covers both cells. Algebra calls it redundant, but it holds the output steady during the change.</p>
<p><b>Static-0:</b> the same on the 0s. Slide 38: (x<sub>1</sub> + x<sub>2</sub>')(x<sub>2</sub> + x<sub>3</sub>) needs the extra bracket (x<sub>1</sub> + x<sub>3</sub>).</p>""",
      check=(f"{M('F = XY + X' + chr(39) + 'Z')}. Which term removes the hazard?", f"<b>{M('YZ')}</b>. Cells 011 and 111 are neighbours in different groups; the pair they form is YZ."))
hs = p_hazard("x1x2 + x2'x3", ["x1", "x2", "x3"], "hz-s", out="Y")
q("hz-s", "Slides 33–36: the lecture example", f"<p>{M('Y = x1x2 + x2' + chr(39) + 'x3')}. The inputs are x<sub>1</sub>x<sub>2</sub>x<sub>3</sub> = 111, then x<sub>2</sub> drops to 0. Show that the output can glitch, and remove the hazard.</p>",
  [["Before: x<sub>1</sub>x<sub>2</sub> = 1 and x<sub>2</sub>'x<sub>3</sub> = 0, so Y = 1. After: x<sub>1</sub>x<sub>2</sub> = 0 and x<sub>2</sub>'x<sub>3</sub> = 1, so Y = 1. But the first term switches off at once, and the second switches on only after x<sub>2</sub> has passed through the inverter.", "For that moment both AND gates give 0, so the OR gate gives 0: Y goes 1 → 0 → 1. A static-1 hazard."]] + hs[0][1:],
  M("Y = " + hs[1]), sim=hz("A'B + AC", ABC, "t8-1"))
q("t8-3", "Four variables", *hz("B'C' + A'BD + ACD'", ABCD, "t8-3"), sim=hz("A'C' + ABD + B'CD", ABCD, "t8-5"))
q("t8-4", "Brackets first", *hz("A(B'+CD') + A'D(B+C')", ABCD, "t8-4", "AB' + ACD' + A'BD + A'C'D"), sim=hz("B(A'+CD) + B'D'(A+C)", ABCD, "t8-6", "A'B + BCD + AB'D' + B'CD'"))
h0 = p_hazard0("(x1 + x2')(x2 + x3)", ["x1", "x2", "x3"], "hz-0")
assert h0[1] == "(x2 + x3)(x1 + x2')(x1 + x3)"
h1 = p_hazard0("(A + B)(A' + C)", ABC, "hz-1")
q("hz-0", "Slide 38: static-0 hazard", f"<p>{M('Y = (x1 + x2' + chr(39) + ')(x2 + x3)')} is built as OR gates into an AND gate. Find the static-0 hazard and remove it.</p>", h0[0], M("Y = " + h0[1]),
  sim=(f"<p>Remove the static-0 hazard from {M('Y = (A + B)(A' + chr(39) + ' + C)')}.</p>", h1[0], M("Y = " + h1[1])))
put(EX["pp-2b"])

# ===================================================================== memory, PLDs, transistors
part("Memory, programmable logic, transistors")


def memq(words, wl, bits_):
    k = words.bit_length() - 1
    assert 1 << k == words
    return (f"<p>A memory is {wl} × {bits_} ({wl} words of {bits_} bits). How many address lines and data lines does it have, and how many bits does it store?</p>",
            [[f"{wl} = 2<sup>{k}</sup> words → <b>{k} address lines</b>.", "k address lines select one of 2<sup>k</sup> words. 1K = 2<sup>10</sup>, 1M = 2<sup>20</sup>."],
             [f"{bits_} bits per word → <b>{bits_} data lines</b>.", "One line per bit of the word."], [f"Total = {words} × {bits_} = <b>{words * bits_:,} bits</b>.", "Words × bits per word."]], f"{k} address lines · {bits_} data lines · {words * bits_:,} bits")


def decq(k):
    h = k // 2
    return (f"<p>A memory with {1 << k} words uses two-dimensional (coincident) decoding. Compare the AND gates needed with a single decoder.</p>",
            [[f"One decoder: {k} address bits → a {k} × {1 << k} decoder = <b>{1 << k} AND gates with {k} inputs each</b>.", "One gate per word."],
             [f"Split the address in half: two {h} × {1 << h} decoders, one for rows and one for columns = 2 × {1 << h} = <b>{2 << h} AND gates with {h} inputs each</b>.", "A word is selected where its row line and column line are both active."]],
            f"{1 << k} gates of {k} inputs against {2 << h} gates of {h} inputs")


topic("m1", "Memory: sizes, RAM and decoding", "Lecture 21, slides 2–13", pri=1,
      learn=f"""<p>Memory stores <b>words</b> (groups of bits, usually 8 = a byte). A memory is described as <b>words × bits per word</b>. <b>k address lines select one of 2ᵏ words.</b></p>
<p>1 kB = 2¹⁰ bytes · 1 MB = 2²⁰ · 1 GB = 2³⁰.</p>
<p><b>RAM</b> (random access memory): read and write, any word in any order.</p>
{table(["Signal", "Job"], [["Address", "which word"], ["Data in / data out", "the word"], ["Read/Write", "<b>1 = read, 0 = write</b>"], ["Memory enable", "0 = no word selected"]])}
<p><b>Binary cell:</b> stores one bit (a latch plus gates) with a Select and a Read/Write input. Select = 0 → it holds and outputs 0.</p>
<p><b>A 4 × 3 RAM</b> = 12 cells + a <b>2-to-4 decoder</b> that turns the address into one active word line. On a read, each column's cells are ORed onto that output.</p>
<p><b>Coincident decoding:</b> big memories split the address in half, one decoder for rows and one for columns. Far fewer, smaller gates.</p>""",
      check=("A memory has 12 address lines and 8 data lines. Size?", "2¹² = 4096 words × 8 bits = <b>4K × 8</b>."))
q("mem-1", "Slide 5: address and data lines", *memq(1024, "1024", 16), sim=memq(65536, "64K", 8))
q("mem-2", "Slide 13: two-dimensional decoding", *decq(10), sim=decq(12))

topic("m2", "SRAM, DRAM, ROM and flash", "Lecture 21, slides 14–33", pri=1,
      learn=f"""{table(["", "SRAM (static)", "DRAM (dynamic)"], [["Cell", "latch, <b>6 transistors</b>", "<b>1 transistor + 1 capacitor</b>"], ["Bit stored as", "latch state", "charge on the capacitor"], ["Size", "bigger", "about <b>¼</b> the area → higher density"], ["Refresh", "no", "<b>yes</b>: charge leaks away and must be topped up"]])}
<p><b>Volatile</b> = loses its data when power is off. SRAM and DRAM are both volatile. <b>Non-volatile:</b> ROM, flash, magnetic disk.</p>
<p><b>ROM:</b> k address inputs, n data outputs, no data input and no write. Inside: a <b>k-to-2ᵏ decoder</b> + <b>n OR gates</b>. A connected cross point (fuse intact) puts a 1 in that bit.</p>
{table(["Type", "Programmed", "Erased"], [["Mask ROM", "at the factory", "never"], ["<b>PROM</b>", "once, by blowing fuses with a high-voltage pulse", "never"], ["<b>EPROM</b>", "by the user", "<b>ultraviolet light</b>"], ["<b>EEPROM</b>", "by the user", "<b>electrically</b>"], ["<b>Flash</b>", "in-circuit, no special programmer", "electrically"]])}
<p><b>Flash cell:</b> a <b>floating-gate</b> transistor. Electrons trapped on the insulated floating gate stay for years and shift the threshold voltage. Reading = checking whether it conducts. <b>NOR flash:</b> each cell straight between the bit line and ground. <b>NAND flash:</b> several cells in series.</p>""",
      check=("Is DRAM volatile? Does it need refresh?", "<b>Yes and yes.</b> Both RAM types lose data without power. Only DRAM also needs refreshing while powered."))


def romq(k, n):
    return (f"<p>A ROM has {k} address inputs and {n} data outputs. Give the decoder size, the number of OR gates and their inputs, and the number of programmable links.</p>",
            [[f"{k} address lines → a <b>{k} × {1 << k} decoder</b> ({1 << k} words).", "The decoder makes one line per word."], [f"{n} outputs → <b>{n} OR gates</b>, each with {1 << k} inputs.", "One OR gate per bit of the word, and every word line can reach it."],
             [f"Links = {1 << k} × {n} = <b>{(1 << k) * n}</b>.", "One fuse at every crossing of a word line and an OR gate."]], f"{k} × {1 << k} decoder · {n} OR gates · {(1 << k) * n} links")


q("rom-1", "Slide 22: inside a 32 × 8 ROM", *romq(5, 8), sim=romq(8, 4))
q("rom-2", "Which memory?", "<p>Name the memory type: (a) erased with ultraviolet light, (b) one transistor and one capacitor per bit, (c) six transistors per bit, (d) programmed once by blowing fuses, (e) erased and reprogrammed in-circuit, used in SSDs.</p>",
  [["(a) <b>EPROM</b> · (b) <b>DRAM</b> · (c) <b>SRAM</b> · (d) <b>PROM</b> · (e) <b>flash</b>.", "EEPROM is also erased electrically, but flash adds the circuitry to do it in-circuit without a special programmer."]], "EPROM · DRAM · SRAM · PROM · flash")


def lut(fn, text, nbits):
    rows = [[x, bits(x, 3), fn(x), bits(fn(x), nbits)] for x in range(8)]
    assert all(fn(x) < (1 << nbits) for x in range(8)) and max(fn(x) for x in range(8)) >= (1 << (nbits - 1))
    return (f"<p>Implement {text} for a 3-bit input x with a ROM. What size ROM is needed and what is stored in it?</p>",
            [["Use the ROM as a <b>look-up table</b>: the input x is the address, the stored word is the answer.", "No multiplier or adder is built. Every answer is worked out in advance and stored."],
             [f"3 address bits → 8 words. The largest output is {fn(7)}, which needs {nbits} bits → an <b>8 × {nbits} ROM</b>:" + table(["x", "Address", "y", "Stored word"], rows), "Programming the ROM = filling in the truth table."]], f"8 × {nbits} ROM")


topic("m3", "Programmable logic", "Lecture 22", pri=1,
      learn=f"""<p><b>A ROM is a truth table.</b> Its decoder makes every minterm and its OR gates add up the ones you want. Address = input variables, stored word = outputs.</p>
<p>PROM, PAL and PLA are all an <b>AND array</b> (makes product terms) feeding an <b>OR array</b> (adds them). They differ in which array you can program:</p>
{table(["Device", "AND array", "OR array", ""], [["<b>PROM</b>", "<b>fixed</b> (a full decoder)", "programmable", ""], ["<b>PAL</b>", "programmable", "<b>fixed</b>", "easier to program"], ["<b>PLA</b>", "programmable", "programmable", "most flexible, hardest to program"]])}
<p>PAL and PLA contain only gates → <b>combinational</b> logic only. Add flip-flops and you get sequential devices:</p>
{table(["", "CPLD", "FPGA"], [["Made of", "several PLDs joined by a programmable <b>switch matrix</b>", "hundreds or thousands of <b>configurable logic blocks (CLBs)</b>"], ["Basic unit", "<b>macrocell</b>: sum-of-products logic + an optional flip-flop (8 to 16 per PLD)", "<b>CLB</b>: lookup table + muxes + flip-flop. Any function of <b>4 variables</b>"], ["Around it", "I/O blocks (three-state buffer per pin)", "I/O blocks (IOBs) + programmable interconnect"]])}
<p>Each FPGA interconnect point has <b>6 switches</b> → 2⁶ = <b>64</b> ways to connect the 4 wires meeting there.</p>
{table(["", "ASIC", "FPGA"], [["What", "designed for one job, made in a foundry", "bought off the shelf, configured by the designer"], ["Design ends with", "physical layout", "a <b>bitstream</b>"], ["Good at", "high performance, low power, low cost in high volume", "low development cost, short time to market, reconfigurable"]])}""",
      check=("Which device has a programmable AND array and a fixed OR array?", "<b>PAL.</b>"))
q("pl-1", "Slide 5: a ROM as a look-up table", *lut(lambda x: x * x + 1, "y = x² + 1", 6), sim=lut(lambda x: 3 * x + 2, "y = 3x + 2", 5))
q("pl-2", "FPGA numbers", "<p>(a) A lookup table has 4 inputs. How many bits of memory does it hold? (b) What size ROM implements a full adder? (c) How many CLBs does a full adder need, and how many CLB inputs go unused?</p>",
  [["(a) One bit per truth-table row: 2<sup>4</sup> = <b>16 bits</b>.", "A LUT is a tiny 16 × 1 ROM."], ["(b) 3 inputs → 8 words. 2 outputs (S, C) → 2 bits. <b>8 × 2 ROM.</b>", "Inputs are the address, outputs are the stored word."],
   ["(c) <b>One CLB</b> (slide 18): one logic block for Sum and one for Carry. Each is a 3-variable function in a 4-input block, so <b>one input of each is unused</b>.", "Any function of up to 4 variables fits in one lookup table."]], "16 bits · 8 × 2 ROM · 1 CLB, one input of each block unused")


def cmos(kind, a, b):
    nA, nB, pA, pB = a, b, 1 - a, 1 - b
    down = (nA and nB) if kind == "NAND" else (nA or nB)
    up = (pA or pB) if kind == "NAND" else (pA and pB)
    y = 1 - (a & b) if kind == "NAND" else 1 - (a | b)
    assert bool(up) != bool(down) and bool(up) == bool(y)
    on = lambda v: "<b>on</b>" if v else "off"
    return (f"<p>A CMOS {kind} gate has A = {a}, B = {b}. Which transistors are on, and what is Y?</p>",
            [["NMOS conducts when its gate is 1. PMOS conducts when its gate is 0:" + table(["", "A", "B"], [["NMOS (bottom)", on(nA), on(nB)], ["PMOS (top)", on(pA), on(pB)]]), "Every input drives one NMOS and one PMOS, and they always do opposite things."],
             [(f"{kind}: NMOS in <b>{'series' if kind == 'NAND' else 'parallel'}</b> to ground, PMOS in <b>{'parallel' if kind == 'NAND' else 'series'}</b> to V<sub>DD</sub>. "
               + (f"Path to ground: {'yes' if down else 'no'}. Path to V<sub>DD</sub>: {'yes' if up else 'no'}.")), "Series needs every transistor on. Parallel needs any one."],
             [f"Y is connected to {'V<sub>DD</sub>' if y else 'ground'} → <b>Y = {y}</b>.", "Exactly one of the two networks conducts, so no steady current flows from supply to ground."]], f"Y = {y}")


topic("m4", "Transistor logic: NMOS and CMOS", "Lecture 25", pri=1,
      learn=f"""<p><b>Positive logic:</b> high voltage = 1, low = 0. A MOS transistor is a switch controlled by its <b>gate</b> voltage.</p>
{table(["", "Gate HIGH", "Gate LOW"], [["<b>NMOS</b>", "<b>on</b> (closed)", "off"], ["<b>PMOS</b>", "off", "<b>on</b> (closed)"]], "tt small")}
<p><b>NMOS inverter:</b> one NMOS to ground and a resistive load to the supply. Problem: while the transistor is on, current flows all the time.</p>
<p><b>CMOS</b> (complementary MOS): a <b>PMOS network pulls up</b> to V<sub>DD</sub>, an <b>NMOS network pulls down</b> to ground. Only one is ever on, so <b>no steady current</b>.</p>
{img(seq("cmos-gates"), "CMOS gates", True)}
{table(["Gate", "PMOS (top)", "NMOS (bottom)", "Transistors"], [["NOT", "1", "1", "2"], ["<b>NAND</b>", "<b>parallel</b>", "<b>series</b>", "4"], ["<b>NOR</b>", "<b>series</b>", "<b>parallel</b>", "4"]])}
<p><b>Transmission gate:</b> an NMOS and a PMOS side by side. N = 1, P = 0 → closed switch. N = 0, P = 1 → open. Built from them: XOR = <b>8</b> transistors, D latch = <b>10</b>, 4-to-1 mux = <b>16</b>.</p>""",
      check=("Why does CMOS use less power than NMOS logic?", "In a steady state one of the two networks is always off, so there is no path from V<sub>DD</sub> to ground and <b>no current flows</b>."))
q("cm-1", "Slides 15–18: which transistors are on?", *cmos("NAND", 1, 0), sim=cmos("NOR", 1, 0))
q("cm-2", "NAND, all inputs high", *cmos("NAND", 1, 1), sim=cmos("NOR", 0, 0))
