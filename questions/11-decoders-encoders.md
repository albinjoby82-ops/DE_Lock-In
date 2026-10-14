# Topic 11 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide examples

### S1 (Lecture 9, slide 6)

Implement a full adder with a 3-to-8 active-high decoder and OR gates.

<details><summary>Answer</summary>

C = Σm(3, 5, 6, 7). S = Σm(1, 2, 4, 7).

Feed X, Y, Z into the decoder (X = MSB).

**S = OR of outputs 1, 2, 4, 7**

**C = OR of outputs 3, 5, 6, 7**

From: §3, §4, Rule 1

</details>

---

### S2 (Lecture 9, slide 12)

Implement a full adder with a 3-to-8 active-low decoder.

<details><summary>Answer</summary>

Tie EN to ground (0), so the active-low decoder is always on.

C = ΠM(0, 1, 2, 4). S = ΠM(0, 3, 5, 6).

**C = AND of outputs 0, 1, 2, 4**

**S = AND of outputs 0, 3, 5, 6**

From: §7, Rule 2

</details>

---

### S3 (Lecture 9, slide 9)

Build a 3-to-8 decoder from two 2-to-4 decoders with enable inputs.

<details><summary>Answer</summary>

S₁ and S₀ go to both decoders.

S₂' goes to the first decoder's EN → outputs Q₀ to Q₃.

S₂ goes to the second decoder's EN → outputs Q₄ to Q₇.

When S₂ = 0 only the first is on. When S₂ = 1 only the second is on.

From: §6

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. An n-to-2ⁿ decoder has exactly one output at 1 when enabled.
2. When an active-high decoder's EN = 0, all outputs are 1.
3. Active-low decoder outputs are maxterms.
4. An encoder works correctly when two inputs are on at once.
5. In a priority encoder, the highest-numbered active input wins.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **False.** All outputs are 0. (§5)
3. **True.** (§7)
4. **False.** D₃ and D₅ on gives 111, which is wrong. (§8)
5. **True.** (§9)

</details>

---

### M2: Multiple choice

f(x, y, z) = Σm(1, 2, 5). Using a 3-to-8 **active-low** decoder, you should:

- A. OR outputs 1, 2, 5
- B. AND outputs 1, 2, 5
- C. AND outputs 0, 3, 4, 6, 7
- D. OR outputs 0, 3, 4, 6, 7

<details><summary>Answer</summary>

**C.**

Active-low outputs are maxterms, so use ΠM and an AND.

f = ΠM(0, 3, 4, 6, 7) (the missing numbers).

(A is the answer for an active-high decoder.)

From: §7, Rule 2, and Topic 7 Rule 3

</details>

---

### M3: Decoder with enable

Write the output equations for a 2-to-4 active-high decoder with enable.

<details><summary>Answer</summary>

Each output is its minterm, ANDed with EN:

Q₀ = EN · S₁'S₀'

Q₁ = EN · S₁'S₀

Q₂ = EN · S₁S₀'

Q₃ = EN · S₁S₀

When EN = 0, every output is 0.

From: §1, §5

</details>

---

### M4: Bigger decoder

How would you build a 4-to-16 decoder from two 3-to-8 decoders with enable?

<details><summary>Answer</summary>

S₂, S₁, S₀ go to both 3-to-8 decoders.

S₃' drives the first EN → outputs 0 to 7.

S₃ drives the second EN → outputs 8 to 15.

From: §6

</details>

---

### M5: Encoder

An 8-to-3 encoder (not priority) has D₁ and D₆ both on. What does it output? What should a priority encoder output?

<details><summary>Answer</summary>

**Plain encoder:**

X = D₄ + D₅ + D₆ + D₇ = 1

Y = D₂ + D₃ + D₆ + D₇ = 1

Z = D₁ + D₃ + D₅ + D₇ = 1

Output **111** = 7. Wrong. Neither input is 7.

**Priority encoder:** D₆ is the highest, so **110** = 6.

From: §8, §9

</details>

---

### M6: Design

f(A, B, C) = A'B + AC. Implement it with a 3-to-8 active-high decoder and one gate.

<details><summary>Answer</summary>

Find the minterms.

A'B is 1 on rows 010, 011 → 2, 3.

AC is 1 on rows 101, 111 → 5, 7.

f = Σm(2, 3, 5, 7)

**OR together decoder outputs 2, 3, 5, 7.**

From: §3, Rule 1, and Topic 7

</details>

---

### M7: Explain

Why is a decoder called a "minterm generator"?

<details><summary>Answer</summary>

Each output is 1 for exactly one input combination, and its equation contains every input variable.

That is exactly the definition of a minterm.

So the decoder produces all 2ⁿ minterms at once, and any function is just an OR of some of them.

From: §3

</details>
