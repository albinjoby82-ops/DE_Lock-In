# Topic 10 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide examples

### S1 (Lecture 7/8, slides 12 to 13)

Write the full adder truth table. Find C and S as Σm, and simplify C with a K-map.

<details><summary>Answer</summary>

| X | Y | Z | C | S |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

C = Σm(3, 5, 6, 7). S = Σm(1, 2, 4, 7).

<br>

**Carry map** (XY down the side, Z across):

| XY \ Z | 0 | 1 |
|---|---|---|
| **00** | 0 | 0 |
| **01** | 0 | 1 |
| **11** | 1 | 1 |
| **10** | 0 | 1 |

Cells 6, 7: XY. Cells 3, 7: YZ. Cells 7, 5: XZ.

**C = XY + YZ + XZ**

S is a checkerboard, so it doesn't simplify: **S = X ⊕ Y ⊕ Z**

From: §4, Equation 2

</details>

---

### S2 (Lecture 7/8, slides 15 to 17)

Show that a full adder built from two half adders gives C = XY + (X ⊕ Y)Z.

<details><summary>Answer</summary>

Half adder 1: S₁ = X ⊕ Y, C₁ = XY

Half adder 2 (adds S₁ and Z): S = S₁ ⊕ Z, C₂ = S₁Z = (X ⊕ Y)Z

OR the two carries: **C = C₁ + C₂ = XY + (X ⊕ Y)Z**

From: §5

</details>

---

### S3 (Lecture 7/8, slide 32)

Multiply 1101 × 0110 using partial products.

<details><summary>Answer</summary>

Partial products (one per multiplier bit, right to left):

- bit 0 = 0 → 0000
- bit 1 = 1 → 1101, shifted 1
- bit 2 = 1 → 1101, shifted 2
- bit 3 = 0 → 0000, shifted 3

Sum: 11010 + 110100 = **1001110**

13 × 6 = 78 ✓

From: §10

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. A half adder has three inputs.
2. XOR is 1 when an odd number of its inputs are 1.
3. The full adder's sum simplifies a lot on a K-map.
4. In a ripple carry adder, the delay grows with the number of bits.
5. Carry lookahead uses fewer gates than ripple carry.
6. In the 2 × 2 multiplier, C₃ is a carry bit.

<details><summary>Answer</summary>

1. **False.** Two (X, Y). The full adder has three. (§3, §4)
2. **True.** (§2)
3. **False.** It's a checkerboard. Nothing groups. (§4)
4. **True.** About 2n gate delays. (§6)
5. **False.** It's faster but uses more: O(n²) gates. (§8)
6. **False.** C₃ to C₀ are the product bits. (§10)

</details>

---

### M2: Multiple choice

What is the generate signal Gᵢ in a carry lookahead adder?

- A. Aᵢ ⊕ Bᵢ
- B. Aᵢ + Bᵢ
- C. AᵢBᵢ
- D. Pᵢ ⊕ Cᵢ

<details><summary>Answer</summary>

**C.** A bit generates a carry by itself only when both inputs are 1.

(A is Pᵢ. D is Sᵢ.)

From: §7, Equation 3

</details>

---

### M3: Ripple carry

Add A = 1011 and B = 0110 with a 4-bit ripple carry adder (C₀ = 0). Show the carry and sum at each stage.

<details><summary>Answer</summary>

| Bit | Aᵢ | Bᵢ | Carry in | Sᵢ | Carry out |
|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 1 |
| 3 | 1 | 0 | 1 | 0 | 1 |

Sum = **0001**, C₄ = **1**. So the answer is **10001**.

Check: 11 + 6 = 17 ✓

From: §4, §6

</details>

---

### M4: Carry lookahead

For the same A = 1011, B = 0110, C₀ = 0, find every Pᵢ and Gᵢ. Then find C₁ to C₄ with the lookahead equations.

<details><summary>Answer</summary>

| Bit | Aᵢ | Bᵢ | Pᵢ = Aᵢ ⊕ Bᵢ | Gᵢ = AᵢBᵢ |
|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 |
| 3 | 1 | 0 | 1 | 0 |

C₁ = G₀ + P₀C₀ = 0 + 1 · 0 = **0**

C₂ = G₁ + P₁G₀ + P₁P₀C₀ = 1 + 0 + 0 = **1**

C₃ = G₂ + P₂G₁ + P₂P₁G₀ + P₂P₁P₀C₀ = 0 + 1 · 1 + 0 + 0 = **1**

C₄ = G₃ + P₃G₂ + P₃P₂G₁ + … = 0 + 0 + 1 · 1 · 1 + … = **1**

Same carries as the ripple adder in M3 ✓

Sums: Sᵢ = Pᵢ ⊕ Cᵢ → S₀ = 1, S₁ = 0, S₂ = 0, S₃ = 0 ✓

From: §7, Equation 3

</details>

---

### M5: Subtraction

Compute 0111 − 0010 using an adder and 2's complement.

<details><summary>Answer</summary>

A − B = A + B' + 1

B' = 1101

0111 + 1101 + 1 = 1 0101

Drop the carry: **0101** = 5

Check: 7 − 2 = 5 ✓

From: §9, Equation 4, and Topic 4

</details>

---

### M6: 2 × 2 multiplier

A = 11, B = 10. Find C₃ C₂ C₁ C₀ using the multiplier equations.

<details><summary>Answer</summary>

A₁ = 1, A₀ = 1, B₁ = 1, B₀ = 0.

C₀ = A₀B₀ = 1 · 0 = **0**

A₀B₁ = 1, A₁B₀ = 0 → C₁ = 1 ⊕ 0 = **1**, K = 1 · 0 = 0

A₁B₁ = 1 → C₂ = 1 ⊕ 0 = **1**, C₃ = 1 · 0 = **0**

Product = **0110** = 6. Check: 3 × 2 = 6 ✓

From: §10

</details>

---

### M7: Design

Use the design procedure to design a half subtractor (X − Y). Give the truth table and the equations.

<details><summary>Answer</summary>

**Step 1.** Inputs X, Y. Outputs D (difference) and B (borrow).

**Step 2.**

| X | Y | B | D |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 |

**Step 3.** D is 1 when the inputs differ: **D = X ⊕ Y**. B is 1 only on row 01: **B = X'Y**.

**Step 4.** One XOR gate for D. One NOT on X and one AND for B.

From: §1 Rule 1, §9 Equation 4

</details>

---

### M8: Explain

Explain why a carry lookahead adder is faster than a ripple carry adder, and why it isn't used on its own for very wide adders.

<details><summary>Answer</summary>

**Faster:** in a ripple adder each stage waits for the carry from the previous one, so delay grows with n (about 2n gate delays). Lookahead computes every carry directly from the P and G signals in two gate levels, so no waiting.

**Not used alone for wide adders:** the number of gates grows as O(n²) and transistors as O(n³). The gates get very wide, and wide gates are slow and hit technology limits.

So real designs mix them, for example four 4-bit ripple blocks linked by lookahead.

From: §6, §7, §8

</details>
