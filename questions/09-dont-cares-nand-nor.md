# Topic 9 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises

### S1 (Lecture 6, slide 14)

Simplify F = A'B'C + AC' + ACD + ACD'. Implement it with two-level NAND gates.

<details><summary>Answer</summary>

**Minimise:**

ACD + ACD' = AC. AC + AC' = A.

F = A + A'B'C = **A + B'C**

(K-map: rows 11 and 10 give A. Cells 3, 2, 11, 10 give B'C.)

<br>

**Build:**

Gate 1: NAND(B', C)

A goes straight into the output gate, so complement it → A'

Output: NAND(A', gate 1)

<br>

**Check:** (A' · (B'C)')' = A + B'C ✓

From: §7, §9, Rule 3

</details>

---

### S2 (Lecture 6, slide 15)

Simplify F = AC' + ACD' + ABD. Implement it with two-level NOR gates.

<details><summary>Answer</summary>

**Minimise the POS** (group the 0s):

The 1s are 8, 9, 10, 12, 13, 14, 15. Every A = 1 cell except 11.

Cells 0 to 7: → **(A)**

Cells 3 and 11: B = 0, C = 1, D = 1 → **(B + C' + D')**

F = **A(B + C' + D')**

<br>

**Build:**

Gate 1: NOR(B, C', D')

A goes straight into the output gate, so complement it → A'

Output: NOR(A', gate 1)

<br>

**Check:** (A' + (B + C' + D')')' = A(B + C' + D') ✓

From: §8, §10, Rule 4

</details>

---

### S3 (Lecture 6, slides 3 and 4)

A 3-variable map has 1s at cells 0, 2, 3, 4, 7 and a don't care at cell 6. Find the minimum SOP with and without using the don't care.

<details><summary>Answer</summary>

**x as 0:** F = A'C' + BC + B'C'

**x as 1:** column C = 0 gives C'. Rows 01 and 11 give B.

F = **C' + B**

Using the don't care is much simpler.

From: §1, §2, Rule 1

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. Every don't care must be inside a group.
2. A NAND gate is the same as an OR gate with inverted inputs.
3. NAND-NAND logic starts from the minimum POS.
4. A 4-input NOR gate uses 8 transistors in CMOS.
5. A 2-input OR gate uses 4 transistors in CMOS.

<details><summary>Answer</summary>

1. **False.** Use an x only if it helps. (§1, Rule 1)
2. **True.** DeMorgan: (AB)' = A' + B'. (§5)
3. **False.** NAND-NAND starts from the SOP. NOR-NOR uses the POS. (§7, §8)
4. **True.** 2n = 8. (§4, Rule 2)
5. **False.** OR is 2n + 2 = 6. (§4, Rule 2)

</details>

---

### M2: Multiple choice

Why are NAND and NOR gates often preferred over AND and OR?

- A. They are easier to draw
- B. They are faster and use fewer transistors
- C. They don't need a power supply
- D. They can only make SOP circuits

<details><summary>Answer</summary>

**B.**

From: §4

</details>

---

### M3: Don't cares (study guide)

F(A, B, C, D) = Σm(1, 3, 7, 11, 15) + d(0, 2, 5). Find the minimum SOP.

<details><summary>Answer</summary>

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | x | 1 | 1 | x |
| **01** | 0 | x | 1 | 0 |
| **11** | 0 | 0 | 1 | 0 |
| **10** | 0 | 0 | 1 | 0 |

Column CD = 11 (3, 7, 15, 11): → **CD**

Cell 1 still needs covering. Use d0 and d2 as 1: row 00 (0, 1, 3, 2) → **A'B'**

**F = CD + A'B'**

(Using d5 instead gives cells 1, 3, 5, 7 → A'D. So **CD + A'D** is equally minimal.)

From: §1, Rule 1, and Topic 8

</details>

---

### M4: NAND design

F(A, B, C) = Σm(0, 2, 4, 5, 6). Find the minimum SOP and build it with NAND gates only.

<details><summary>Answer</summary>

| AB \ C | 0 | 1 |
|---|---|---|
| **00** | 1 | 0 |
| **01** | 1 | 0 |
| **11** | 1 | 0 |
| **10** | 1 | 1 |

Column C = 0 (0, 2, 6, 4): → **C'**

Cells 4, 5: A = 1, B = 0 → **AB'**

F = **C' + AB'**

<br>

**Build:**

Gate 1: NAND(A, B')

C' is a single letter at the output, so complement it → feed in **C**

Output: NAND(C, gate 1)

Check: (C · (AB')')' = C' + AB' ✓

From: §7, Rule 3

</details>

---

### M5: NOR design

Build F = (A + B)(C + D) using NOR gates only.

<details><summary>Answer</summary>

It's already a POS.

Gate 1: NOR(A, B)

Gate 2: NOR(C, D)

Output: NOR(gate 1, gate 2)

No single letters at the output, so nothing to complement.

Check: ((A + B)' + (C + D)')' = (A + B)(C + D) ✓ (DeMorgan)

From: §8, Rule 4

</details>

---

### M6: Transistor count

F = AB + CD. Count the CMOS transistors for:

1. the AND-OR circuit
2. the NAND-NAND circuit

<details><summary>Answer</summary>

**1. AND-OR:** two 2-input ANDs and one 2-input OR.

3 × (2 × 2 + 2) = 3 × 6 = **18**

**2. NAND-NAND:** three 2-input NANDs.

3 × (2 × 2) = **12**

The NAND version saves 6 transistors.

From: §4, Rule 2, §7

</details>

---

### M7: Explain

In NAND-NAND logic, why must a single letter going into the output gate be complemented?

<details><summary>Answer</summary>

The output NAND acts like an OR with inverted inputs.

Signals from first-level NANDs are already inverted, so the two inversions cancel.

A single letter has no first-level gate, so nothing cancels the output gate's inversion.

Feeding in its complement fixes that.

From: §5, §6

</details>
