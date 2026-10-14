# Topic 2 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises

### S1 (Lecture 2, slide 22)

Convert 123.15625₁₀ to binary.

<details><summary>Answer</summary>

**Whole part: divide by 2**

| | Remainder |
|---|---|
| 123 ÷ 2 = 61 | 1 ← LSB |
| 61 ÷ 2 = 30 | 1 |
| 30 ÷ 2 = 15 | 0 |
| 15 ÷ 2 = 7 | 1 |
| 7 ÷ 2 = 3 | 1 |
| 3 ÷ 2 = 1 | 1 |
| 1 ÷ 2 = 0 | 1 ← MSB |

Read upward: **1111011**

<br>

**Fraction: multiply by 2**

| | Whole part |
|---|---|
| 0.15625 × 2 = 0.3125 | 0 |
| 0.3125 × 2 = 0.625 | 0 |
| 0.625 × 2 = 1.25 | 1 |
| 0.25 × 2 = 0.5 | 0 |
| 0.5 × 2 = 1.0 | 1 ← stop |

Read downward: **.00101**

<br>

123.15625 = **1111011.00101₂**

From: §4, Rule 2

</details>

---

### S2 (Lecture 2, slide 24)

Convert 123.15625₁₀ to hexadecimal, and compare with the binary.

<details><summary>Answer</summary>

**Whole part: divide by 16**

123 ÷ 16 = 7 r 11 → **B**

7 ÷ 16 = 0 r **7**

Read upward: **7B**

<br>

**Fraction: multiply by 16**

0.15625 × 16 = 2.5 → **2**

0.5 × 16 = 8.0 → **8**

Read downward: **.28**

<br>

123.15625 = **7B.28₁₆**

<br>

**Compare with binary (group in 4s outward from the point):**

1111011.00101 → 0111 1011 . 0010 1000 → **7B.28** ✓

Remember to pad the fraction on the right.

From: §5, §6, Rules 2 and 3

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. Hex uses groups of 3 bits.
2. When converting the whole part, you read the remainders from bottom to top.
3. When converting the fraction, you read the whole parts from bottom to top.
4. 1111₂ = F₁₆.
5. To group a binary fraction into hex, you pad zeros on the left of the fraction.

<details><summary>Answer</summary>

1. **False.** Hex uses 4. Octal uses 3. (§6)
2. **True.** The first remainder is the LSB. (§4)
3. **False.** Top to bottom. The first one sits right after the point. (§4)
4. **True.** 8 + 4 + 2 + 1 = 15 = F. (§3)
5. **False.** Pad on the right, at the outer end. (§6)

</details>

---

### M2: Multiple choice

What is 1111011.00101₂ in hex?

- A. 7B.25
- B. 7B.28
- C. F6.28
- D. 7B.A

<details><summary>Answer</summary>

**B.**

A is the classic mistake: padding the fraction on the left (0101 = 5).

Correct: .0010 1000 → .28

From: §6

</details>

---

### M3: Calculation (study guide)

Convert 89.375₁₀ to binary, hex and octal.

<details><summary>Answer</summary>

**Binary**

89: 89→44 r1, 44→22 r0, 22→11 r0, 11→5 r1, 5→2 r1, 2→1 r0, 1→0 r1

Read up: **1011001**

0.375: × 2 = 0.75 → 0, × 2 = 1.5 → 1, 0.5 × 2 = 1.0 → 1

Read down: **.011**

89.375 = **1011001.011₂**

<br>

**Hex** (group in 4s): 0101 1001 . 0110 = **59.6₁₆**

<br>

**Octal** (group in 3s): 001 011 001 . 011 = **131.3₈**

From: §4, §6

</details>

---

### M4: Calculation

Convert to decimal:

1. 3A.C₁₆
2. 1011.101₂
3. 2AF₁₆
4. 57.4₈

<details><summary>Answer</summary>

1. 3 × 16 + 10 + 12/16 = 48 + 10 + 0.75 = **58.75**
2. 8 + 2 + 1 + 0.5 + 0.125 = **11.625**
3. 2 × 256 + 10 × 16 + 15 = 512 + 160 + 15 = **687**
4. 5 × 8 + 7 + 4/8 = 40 + 7 + 0.5 = **47.5**

From: §1, Rule 1

</details>

---

### M5: Grouping

Convert 11010.11₂ to octal and to hex. Check both by converting to decimal.

<details><summary>Answer</summary>

**Octal:** 011 010 . 110 = **32.6₈**

**Hex:** 0001 1010 . 1100 = **1A.C₁₆**

<br>

**Check:**

Binary: 16 + 8 + 2 + 0.5 + 0.25 = 26.75

Octal: 3 × 8 + 2 + 6/8 = 26.75 ✓

Hex: 16 + 10 + 12/16 = 26.75 ✓

From: §6, Rule 3, and Rule 1

</details>

---

### M6: A fraction that never ends

Convert 0.1₁₀ to binary. Give 5 bits after the point.

<details><summary>Answer</summary>

| | Whole part |
|---|---|
| 0.1 × 2 = 0.2 | 0 |
| 0.2 × 2 = 0.4 | 0 |
| 0.4 × 2 = 0.8 | 0 |
| 0.8 × 2 = 1.6 | 1 |
| 0.6 × 2 = 1.2 | 1 |

0.1 ≈ **0.00011₂**

The fraction never reaches 0, so you stop when you have enough bits.

From: §4, Rule 2 "watch out"

</details>

---

### M7: Explain

Explain why each remainder in the "divide by 2" method gives the next bit, starting with the LSB.

<details><summary>Answer</summary>

Dividing by 2 shifts the number one place to the right.

The remainder is the bit that falls off the right-hand end.

So the first remainder is the rightmost bit (LSB), the next is the bit to its left, and so on.

That's why you read the remainders bottom-up.

From: §4, "Why it works"

</details>
