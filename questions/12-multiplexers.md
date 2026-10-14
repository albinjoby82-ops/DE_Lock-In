# Topic 12 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises

### S1 (Lecture 10, slide 7)

Implement f(x, y, z) = Σm(1, 2, 6, 7) with a 4-to-1 multiplexer. Use S₁ = x, S₀ = y.

<details><summary>Answer</summary>

| x y | f (z = 0, z = 1) | Data input |
|---|---|---|
| 00 | 0, 1 | D₀ = **z** |
| 01 | 1, 0 | D₁ = **z'** |
| 10 | 0, 0 | D₂ = **0** |
| 11 | 1, 1 | D₃ = **1** |

From: §6, Rule 2

</details>

---

### S2 (Lecture 10, slide 8)

Implement F(A, B, C, D) = Σm(1, 3, 4, 11, 12, 13, 14, 15) with an 8-to-1 multiplexer. Use S₂S₁S₀ = ABC.

<details><summary>Answer</summary>

| ABC | F (D = 0, D = 1) | Data input |
|---|---|---|
| 000 | 0, 1 | D₀ = **D** |
| 001 | 0, 1 | D₁ = **D** |
| 010 | 1, 0 | D₂ = **D'** |
| 011 | 0, 0 | D₃ = **0** |
| 100 | 0, 0 | D₄ = **0** |
| 101 | 0, 1 | D₅ = **D** |
| 110 | 1, 1 | D₆ = **1** |
| 111 | 1, 1 | D₇ = **1** |

From: §7, Rule 2

</details>

---

### S3 (Study guide)

Implement f(x, y, z) = Σm(0, 2, 5, 7) with a 4-to-1 mux (S₁ = x, S₀ = y).

<details><summary>Answer</summary>

| x y | f (z = 0, z = 1) | Data input |
|---|---|---|
| 00 | 1, 0 | D₀ = **z'** |
| 01 | 1, 0 | D₁ = **z'** |
| 10 | 0, 1 | D₂ = **z** |
| 11 | 0, 1 | D₃ = **z** |

From: §6, Rule 2

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. A 2ⁿ-to-1 mux needs n select lines.
2. Any 3-variable function can be built with a 4-to-1 mux and maybe one inverter.
3. In method 2, a data input can be 0, 1, v or v'.
4. A demux is a decoder whose outputs are each ANDed with the input.
5. For a mux/demux link to work, the two ends can use different select signals.

<details><summary>Answer</summary>

1. **True.** (§1)
2. **True.** The inverter is only needed if some input is v'. (§6)
3. **True.** (§6, Rule 2)
4. **True.** (§8)
5. **False.** Both ends must use the same selects. (§9)

</details>

---

### M2: Multiple choice

For a 2-to-1 mux, Y = ?

- A. SI₀ + S'I₁
- B. S'I₀ + SI₁
- C. I₀ + I₁
- D. S(I₀ + I₁)

<details><summary>Answer</summary>

**B.** S = 0 picks I₀. S = 1 picks I₁.

(A is what slide 3's typo would give.)

From: §2, Equation 1

</details>

---

### M3: Full adder on muxes

Implement the full adder's sum S = Σm(1, 2, 4, 7) and carry C = Σm(3, 5, 6, 7) with two 4-to-1 muxes. Use S₁ = X, S₀ = Y, and Z as the last variable.

<details><summary>Answer</summary>

**Sum:**

| XY | S (Z = 0, Z = 1) | Data input |
|---|---|---|
| 00 | 0, 1 | **Z** |
| 01 | 1, 0 | **Z'** |
| 10 | 1, 0 | **Z'** |
| 11 | 0, 1 | **Z** |

**Carry:**

| XY | C (Z = 0, Z = 1) | Data input |
|---|---|---|
| 00 | 0, 0 | **0** |
| 01 | 0, 1 | **Z** |
| 10 | 0, 1 | **Z** |
| 11 | 1, 1 | **1** |

From: §6, Rule 2, and Topic 10 §4

</details>

---

### M4: Method 1

Implement f(A, B, C) = Σm(0, 3, 5) with an 8-to-1 mux.

<details><summary>Answer</summary>

Wire A, B, C to S₂, S₁, S₀.

**D₀ = D₃ = D₅ = 1.** All others (D₁, D₂, D₄, D₆, D₇) = **0**.

From: §5, Rule 1

</details>

---

### M5: Building bigger muxes

How many 4-to-1 muxes do you need to build a 16-to-1 mux? How are the select lines wired?

<details><summary>Answer</summary>

**Five.**

Four first-level muxes take data 0–3, 4–7, 8–11, 12–15. They all share the low selects A₁A₀.

The fifth mux takes those four outputs and uses the high selects A₃A₂.

From: §4

</details>

---

### M6: Demux

Write the output equations for a 1-to-4 demux with input I and selects S₁S₀.

<details><summary>Answer</summary>

F₀ = S₁'S₀' I

F₁ = S₁'S₀ I

F₂ = S₁S₀' I

F₃ = S₁S₀ I

From: §8

</details>

---

### M7: Explain

Explain why, in method 2, each data input can only be 0, 1, v or v'.

<details><summary>Answer</summary>

Within one pair of rows, all the select variables are fixed. Only the last variable v changes.

So on that data input, f is a function of v alone.

A function of one variable has only four possibilities: always 0, always 1, equal to v, or equal to v'.

From: §6, Rule 2 "Why it works"

</details>
