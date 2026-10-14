# Topic 5 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide examples

### S1 (Lecture 3, slide 21)

Write 185₁₀ in BCD.

<details><summary>Answer</summary>

1 = 0001, 8 = 1000, 5 = 0101

185 = **0001 1000 0101**

From: §2

</details>

---

### S2 (Lecture 3, slide 22)

The number 3 is stored, and its third bit (from the right) gets corrupted.

What value do you read if it was stored in plain binary? In Gray code?

<details><summary>Answer</summary>

**Binary:** 0011 → 0111 = **7**

**Gray:** 0010 → 0110 = Gray for **4**

Gray gives a much smaller error.

From: §3

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. BCD uses the patterns 1010 to 1111.
2. In Gray code, 6 and 7 differ in exactly one bit.
3. In one-hot code, exactly one bit is 1.
4. 25 in BCD is the same as 25 in binary.
5. A 3-bit code can represent 8 different items.

<details><summary>Answer</summary>

1. **False.** Those six patterns are unused. (§2)
2. **True.** 0101 and 0100. (§3)
3. **True.** (§4)
4. **False.** BCD: 0010 0101. Binary: 11001. (§2)
5. **True.** 2³ = 8. (§1)

</details>

---

### M2: Multiple choice

Which code is best when a 1-bit error should only cause a small change in value?

- A. BCD
- B. One-hot
- C. Gray
- D. Plain binary

<details><summary>Answer</summary>

**C.**

Neighbouring values differ in one bit, so flipping one bit often lands on a nearby value.

From: §3

</details>

---

### M3: Conversions

Write the decimal number 9 in:

1. plain 4-bit binary
2. BCD
3. 4-bit Gray code
4. 16-bit one-hot

<details><summary>Answer</summary>

1. **1001**
2. **1001** (same here, because 9 is a single digit)
3. **1101** (from the table, or Rule 2: 1, 1⊕0 = 1, 0⊕0 = 0, 0⊕1 = 1)
4. bit position 8 → **0000000100000000**

From: §2, §3, §4

</details>

---

### M4: BCD back to decimal

What decimal number is 0100 0111 0000 in BCD?

<details><summary>Answer</summary>

0100 = 4, 0111 = 7, 0000 = 0

**470**

From: §2

</details>

---

### M5: How many bits?

You need to code the 26 letters of the alphabet. What is the smallest number of bits?

<details><summary>Answer</summary>

2⁴ = 16 is too few. 2⁵ = 32 ≥ 26.

**5 bits.**

From: §1, Rule 1

</details>

---

### M6: Explain

Give one advantage and one disadvantage of one-hot coding.

<details><summary>Answer</summary>

**Advantage:** it's very easy to see which value it is. Just find the single 1.

**Disadvantage:** it needs one bit per value, so it uses many more bits than binary (8 values need 8 bits instead of 3).

From: §4

</details>
