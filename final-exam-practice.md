# Final exam practice

**Expected shape (from what the lecturer said, not confirmed in writing): 5 questions. 1 on combinational logic (probably multiplexers), 4 on sequential logic.**

Two mock papers in that shape, then a bank of short questions. Every answer is worked.

**How to use it (Lock-In style):** try the question on paper **first**. Open the answer. Read the linked notes section beside it. Then redo the question from a blank page.

| If the question says… | It is this method | Notes |
|---|---|---|
| "implement F using a multiplexer" | pair the rows on the last variable | [12 §4](notes/12-multiplexers.md) |
| "find Q after each clock edge" | characteristic table | [13 §4](notes/13-latches-flip-flops.md) |
| "derive the state table / diagram of this circuit" | analysis, 3 steps | [14 §1](notes/14-sequential-analysis.md) |
| "design a circuit that detects…" | design, 5 steps | [15](notes/15-sequential-design.md) |
| "design a counter that counts…" | design with no input + check unused states | [16 §1–2](notes/16-counters.md) |
| "shift / ring / Johnson" | trace it row by row | [17](notes/17-registers.md) |
| "race / hazard / stable" | transition table, K-map bridge | [20](notes/20-asynchronous-logic.md) |

**The four tables to have in your head before you start:**

| Q → Q⁺ | J K | D | T |
|---|---|---|---|
| 0 → 0 | 0 x | 0 | 0 |
| 0 → 1 | 1 x | 1 | 1 |
| 1 → 0 | x 1 | 0 | 1 |
| 1 → 1 | x 0 | 1 | 0 |

Q⁺ = D · Q⁺ = JQ' + K'Q · Q⁺ = T ⊕ Q

---

# Paper 1

## Q1 · Multiplexer (combinational)

**(a) Implement F(A, B, C, D) = Σm(0, 1, 3, 4, 8, 9, 15) using one 8-to-1 multiplexer.**
**(b) How many 2-to-1 multiplexers are needed to build an 8-to-1 multiplexer? Which select goes to which level?**

<details><summary>Answer</summary>

**(a)** 4 variables, 8-to-1 mux → A, B, C on the selects, D on the data inputs. Pair the minterms (2i, 2i + 1):

| ABC | Input | m when D = 0 | m when D = 1 | Data |
|---|---|---|---|---|
| 000 | I₀ | m₀ = 1 | m₁ = 1 | **1** |
| 001 | I₁ | m₂ = 0 | m₃ = 1 | **D** |
| 010 | I₂ | m₄ = 1 | m₅ = 0 | **D'** |
| 011 | I₃ | m₆ = 0 | m₇ = 0 | **0** |
| 100 | I₄ | m₈ = 1 | m₉ = 1 | **1** |
| 101 | I₅ | m₁₀ = 0 | m₁₁ = 0 | **0** |
| 110 | I₆ | m₁₂ = 0 | m₁₃ = 0 | **0** |
| 111 | I₇ | m₁₄ = 0 | m₁₅ = 1 | **D** |

Rule: 0,0 → 0 · 0,1 → D · 1,0 → D' · 1,1 → 1.

**(b)** 4 + 2 + 1 = **7**. First level (4 muxes) uses the lowest select S₀, second level (2) uses S₁, last mux uses S₂.

</details>

## Q2 · Flip-flops

**(a) Give the characteristic table and characteristic equation of a JK flip-flop.**
**(b) Explain the difference between a latch and a flip-flop.**
**(c) A T flip-flop starts at Q = 0. T at eight successive clock edges is 1, 1, 0, 1, 0, 0, 1, 1. Give Q after each edge.**

<details><summary>Answer</summary>

**(a)** 00 → Q (hold) · 01 → 0 (reset) · 10 → 1 (set) · 11 → Q' (toggle). **Q⁺ = JQ' + K'Q.**

**(b)** A latch is **level** triggered: it is transparent for the whole time the enable is 1, so the output can change several times. A flip-flop is **edge** triggered: it samples the input only at the clock transition (built from two latches, master and slave, on opposite clock levels).

**(c)** Toggle when T = 1: Q = **1, 0, 0, 1, 1, 1, 0, 1**.

</details>

## Q3 · Analysis

**A sequential circuit has two D flip-flops A and B, an input x and an output z:**
**D<sub>A</sub> = Ax' + Bx · D<sub>B</sub> = A'x + Bx' · z = AB'x**
**(a) Derive the state table. (b) Draw the state diagram. (c) Moore or Mealy? (d) What does it do?**

<details><summary>Answer</summary>

**(a)** D flip-flops, so next state = D.

| A B | x | A⁺ B⁺ | z |
|---|---|---|---|
| 0 0 | 0 | 0 0 | 0 |
| 0 0 | 1 | 0 1 | 0 |
| 0 1 | 0 | 0 1 | 0 |
| 0 1 | 1 | 1 1 | 0 |
| 1 0 | 0 | 1 0 | 0 |
| 1 0 | 1 | 0 0 | 1 |
| 1 1 | 0 | 1 1 | 0 |
| 1 1 | 1 | 1 0 | 0 |

**(b)** Four circles. Every state has a self-loop labelled 0/0. On x = 1: 00 → 01 (1/0), 01 → 11 (1/0), 11 → 10 (1/0), 10 → 00 (**1/1**).

**(c)** **Mealy**: z contains x.

**(d)** Holds when x = 0. When x = 1 it steps 00 → 01 → 11 → 10 → 00: a **Gray-code counter with an enable**, and z flags the wrap-around.

</details>

## Q4 · Design: sequence detector

**Design a Mealy circuit with one input X and one output Z. Z = 1 when the last three inputs were 101. Overlapping patterns count. Use JK flip-flops.**

<details><summary>Answer</summary>

**States:** A = nothing (00) · B = have 1 (01) · C = have 10 (10). Code 11 unused.

**Diagram arrows:** A: 0 → A, 1 → B. B: 0 → C, 1 → B. C: 0 → A, 1 → B with **output 1**.

| Q₁ Q₀ | X | Q₁⁺ Q₀⁺ | J₁ K₁ | J₀ K₀ | Z |
|---|---|---|---|---|---|
| 0 0 | 0 | 0 0 | 0 x | 0 x | 0 |
| 0 0 | 1 | 0 1 | 0 x | 1 x | 0 |
| 0 1 | 0 | 1 0 | 1 x | x 1 | 0 |
| 0 1 | 1 | 0 1 | 0 x | x 0 | 0 |
| 1 0 | 0 | 0 0 | x 1 | 0 x | 0 |
| 1 0 | 1 | 0 1 | x 1 | 1 x | 1 |
| 1 1 | 0 | x x | x x | x x | x |
| 1 1 | 1 | x x | x x | x x | x |

K-maps (variables Q₁, Q₀, X):

**J₁ = Q₀X' · K₁ = 1 · J₀ = X · K₀ = X' · Z = Q₁X**

Check with input 1 0 1 0 1: states A → B → C → B (Z = 1) → C → B (Z = 1). Output 0 0 1 0 1. ✓

</details>

## Q5 · Counter

**Design a synchronous counter that counts 0, 1, 2, 3, 4, 5 and repeats, using JK flip-flops. Show that it is self-correcting.**

<details><summary>Answer</summary>

| A B C | next | J<sub>A</sub> K<sub>A</sub> | J<sub>B</sub> K<sub>B</sub> | J<sub>C</sub> K<sub>C</sub> |
|---|---|---|---|---|
| 0 0 0 | 0 0 1 | 0 x | 0 x | 1 x |
| 0 0 1 | 0 1 0 | 0 x | 1 x | x 1 |
| 0 1 0 | 0 1 1 | 0 x | x 0 | 1 x |
| 0 1 1 | 1 0 0 | 1 x | x 1 | x 1 |
| 1 0 0 | 1 0 1 | x 0 | 0 x | 1 x |
| 1 0 1 | 0 0 0 | x 1 | 0 x | x 1 |

110 and 111 are don't cares.

**J<sub>A</sub> = BC · K<sub>A</sub> = C · J<sub>B</sub> = A'C · K<sub>B</sub> = C · J<sub>C</sub> = K<sub>C</sub> = 1**

**Unused states:**
- 110: J<sub>A</sub> K<sub>A</sub> = 0 0 (hold 1), J<sub>B</sub> K<sub>B</sub> = 0 0 (hold 1), C toggles → **111**
- 111: J<sub>A</sub> K<sub>A</sub> = 1 1 (toggle → 0), J<sub>B</sub> K<sub>B</sub> = 0 1 (reset → 0), C toggles → **000**

110 → 111 → 000: back in the count within two clocks. **Self-correcting.** ✓

</details>

---

# Paper 2

## Q1 · Multiplexer (combinational)

**(a) Implement f(x, y, z) = Σm(1, 2, 4, 7) with one 4-to-1 multiplexer. What well-known function is this?**
**(b) Implement F(A, B, C, D) = Σm(2, 3, 5, 6, 8, 11, 12, 13, 14) with one 8-to-1 multiplexer.**

<details><summary>Answer</summary>

**(a)** Selects x, y. Data in terms of z.

| xy | z = 0 | z = 1 | Data |
|---|---|---|---|
| 00 | m₀ = 0 | m₁ = 1 | **z** |
| 01 | m₂ = 1 | m₃ = 0 | **z'** |
| 10 | m₄ = 1 | m₅ = 0 | **z'** |
| 11 | m₆ = 0 | m₇ = 1 | **z** |

It is **x ⊕ y ⊕ z**: the sum output of a full adder.

**(b)** Selects A, B, C. Pairs:

| ABC | Pair | Data |
|---|---|---|
| 000 | m₀ = 0, m₁ = 0 | **0** |
| 001 | m₂ = 1, m₃ = 1 | **1** |
| 010 | m₄ = 0, m₅ = 1 | **D** |
| 011 | m₆ = 1, m₇ = 0 | **D'** |
| 100 | m₈ = 1, m₉ = 0 | **D'** |
| 101 | m₁₀ = 0, m₁₁ = 1 | **D** |
| 110 | m₁₂ = 1, m₁₃ = 1 | **1** |
| 111 | m₁₄ = 1, m₁₅ = 0 | **D'** |

</details>

## Q2 · Analysis

**Two JK flip-flops A and B, one input x: J<sub>A</sub> = B · K<sub>A</sub> = Bx' · J<sub>B</sub> = x' · K<sub>B</sub> = A ⊕ x. Derive the state table and the state diagram.**

<details><summary>Answer</summary>

| A B | x | J<sub>A</sub> K<sub>A</sub> | J<sub>B</sub> K<sub>B</sub> | A⁺ B⁺ |
|---|---|---|---|---|
| 0 0 | 0 | 0 0 | 1 0 | 0 1 |
| 0 0 | 1 | 0 0 | 0 1 | 0 0 |
| 0 1 | 0 | 1 1 | 1 0 | 1 1 |
| 0 1 | 1 | 1 0 | 0 1 | 1 0 |
| 1 0 | 0 | 0 0 | 1 1 | 1 1 |
| 1 0 | 1 | 0 0 | 0 0 | 1 0 |
| 1 1 | 0 | 1 1 | 1 1 | 0 0 |
| 1 1 | 1 | 1 0 | 0 0 | 1 1 |

Row 0 1, x = 0 slowly: J<sub>A</sub> K<sub>A</sub> = 1 1 → A toggles 0 → 1. J<sub>B</sub> K<sub>B</sub> = 1 0 → B set (stays 1). Next 11.

Diagram: 00 —0→ 01, 00 —1→ 00 · 01 —0→ 11, 01 —1→ 10 · 10 —0→ 11, 10 —1→ 10 · 11 —0→ 00, 11 —1→ 11.

Check: 4 circles, 2 arrows out of each. ✓

</details>

## Q3 · Design: sequence detector

**(a) Design a Mealy detector for the sequence 110 using D flip-flops.**
**(b) Draw the state diagram of the Moore version. How many flip-flops does it need?**

<details><summary>Answer</summary>

**(a)** A = nothing (00) · B = have 1 (01) · C = have 11 (10).

| Present | X | Next | Z |
|---|---|---|---|
| A 00 | 0 | A 00 | 0 |
| A 00 | 1 | B 01 | 0 |
| B 01 | 0 | A 00 | 0 |
| B 01 | 1 | C 10 | 0 |
| C 10 | 0 | A 00 | **1** |
| C 10 | 1 | C 10 | 0 |

(C on a 1: the input ends in 111, and its last two bits are still 11 → stay in C.)

D = next state. With 11 as don't care:

**D₁ = Q₀X + Q₁X · D₀ = Q₁'Q₀'X · Z = Q₁X'**

**(b)** Moore needs a fourth state D = "just saw 110", output 1. A/0, B/0, C/0, D/1.

A: 0 → A, 1 → B · B: 0 → A, 1 → C · C: 0 → **D**, 1 → C · D: 0 → A, 1 → B.

4 states → still **2 flip-flops** (all four codes used, no don't cares).

</details>

## Q4 · Counter

**(a) Design a 2-bit synchronous up/down counter with T flip-flops. X = 1 counts up, X = 0 counts down.**
**(b) A 5-stage binary ripple counter is driven by a 400 kHz clock. What is the frequency at the last stage? Why is a ripple counter slower than a synchronous one?**

<details><summary>Answer</summary>

**(a)**

| A B | X | next | T<sub>A</sub> T<sub>B</sub> |
|---|---|---|---|
| 0 0 | 0 | 1 1 | 1 1 |
| 0 0 | 1 | 0 1 | 0 1 |
| 0 1 | 0 | 0 0 | 0 1 |
| 0 1 | 1 | 1 0 | 1 1 |
| 1 0 | 0 | 0 1 | 1 1 |
| 1 0 | 1 | 1 1 | 0 1 |
| 1 1 | 0 | 1 0 | 0 1 |
| 1 1 | 1 | 0 0 | 1 1 |

**T<sub>B</sub> = 1 · T<sub>A</sub> = B'X' + BX**

**(b)** 400 kHz ÷ 2⁵ = **12.5 kHz**. In a ripple counter each flip-flop is clocked by the one before, so a change has to pass through all the stages one after another (delays add up). In a synchronous counter every flip-flop gets the same clock and they all change together.

</details>

## Q5 · Registers and asynchronous logic

**(a) A 3-bit Johnson counter starts at 000. Give its sequence and a 2-input decoding gate for each state.**
**(b) How many flip-flops are needed for 10 timing signals with a ring counter? With a Johnson counter?**
**(c) F = A'B + AC has a static-1 hazard. Find it and remove it.**

<details><summary>Answer</summary>

**(a)** First flip-flop loads C'. Bits shift right.

| A B C | Gate |
|---|---|
| 0 0 0 | A'C' |
| 1 0 0 | AB' |
| 1 1 0 | BC' |
| 1 1 1 | AC |
| 0 1 1 | A'B |
| 0 0 1 | B'C |

**(b)** Ring: **10**. Johnson: 2k = 10 → **5** (plus 10 two-input AND gates).

**(c)** A'B covers 010, 011. AC covers 101, 111. Cells 011 and 111 are adjacent but in different groups → glitch when B = C = 1 and A changes. Add the bridging term **BC**:

**F = A'B + AC + BC**

</details>

---

# Short-question bank

One or two marks each. Cover the answer and say it out loud.

<details><summary>1. Combinational vs sequential?</summary>

Combinational: output depends on the present inputs only. Sequential: output depends on the inputs **and the stored state** (it has memory).

</details>

<details><summary>2. Which input is forbidden on a NOR SR latch, and why?</summary>

S = R = 1. Both outputs become 0 (not complements), and when S and R return to 0 together the final state is unpredictable.

</details>

<details><summary>3. Why is a D latch preferred to an SR latch?</summary>

R is always the inverse of S, so the forbidden input can never occur.

</details>

<details><summary>4. Moore vs Mealy?</summary>

Moore: output depends on the state only (written inside the circle), synchronous, may need an extra state. Mealy: output depends on state and input (written on the arrow), responds immediately.

</details>

<details><summary>5. n states need how many flip-flops?</summary>

The smallest k with 2ᵏ ≥ n. For example 5 states → 3.

</details>

<details><summary>6. Why can JK designs come out simpler than D designs? Why is D used more anyway?</summary>

JK excitation tables are full of don't cares, so the K-maps simplify more. D needs only one input per flip-flop, no excitation table, and slightly less hardware.

</details>

<details><summary>7. What must you do with a counter's unused states?</summary>

Use them as don't cares, then check each one returns to the valid sequence. If one does not, assign it a next state and redesign.

</details>

<details><summary>8. Synchronous vs ripple counter?</summary>

Synchronous: all flip-flops share the clock. Ripple: each flip-flop is clocked by the previous flip-flop's output.

</details>

<details><summary>9. Universal shift register select codes?</summary>

00 no change · 01 shift right · 10 shift left · 11 parallel load.

</details>

<details><summary>10. Ring vs Johnson counter, k flip-flops?</summary>

Ring: k states, feed back Q. Johnson: 2k states, feed back Q'.

</details>

<details><summary>11. A 1024 × 16 RAM has how many address lines?</summary>

10 (2¹⁰ = 1024).

</details>

<details><summary>12. SRAM vs DRAM?</summary>

SRAM: 6-transistor latch cell, no refresh. DRAM: 1 transistor + capacitor, about a quarter of the area, needs refresh because charge leaks. Both volatile.

</details>

<details><summary>13. PROM, PAL, PLA?</summary>

PROM: fixed AND, programmable OR. PAL: programmable AND, fixed OR. PLA: both programmable.

</details>

<details><summary>14. What is fundamental mode?</summary>

Only one input changes at a time, and only after the circuit has reached a stable state.

</details>

<details><summary>15. Critical vs non-critical race?</summary>

A race is two or more state variables changing at once. Non-critical: same final state whatever the order. Critical: the final state depends on the order.

</details>

<details><summary>16. Static-1, static-0, dynamic hazard?</summary>

Static-1: output should stay 1 but dips to 0. Static-0: should stay 0 but pulses to 1. Dynamic: output changes three or more times when it should change once.

</details>

<details><summary>17. CMOS NAND: how are the transistors arranged?</summary>

Two PMOS in parallel to VDD, two NMOS in series to ground.

</details>

<details><summary>18. ASIC vs FPGA?</summary>

ASIC: custom fabricated, high performance, low power, cheap in high volume. FPGA: off the shelf, reconfigurable, low development cost, fast to market.

</details>
