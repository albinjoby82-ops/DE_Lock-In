# Topic 4 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises

### S1 (Lecture 3, slide 8)

What is the 2's complement negative representation of 01010110?

<details><summary>Answer</summary>

Use the shortcut. From the right, copy the 0 and the first 1: "10".

Flip everything to the left: 010101 → 101010.

Answer: **10101010**

From: §3, Rule 1

</details>

---

### S2 (Lecture 3, slide 16)

Convert 110101 to decimal, assuming it is in:

(a) 1's complement
(b) 2's complement

<details><summary>Answer</summary>

The sign bit is 1, so it's negative either way.

**(a) 1's complement:** flip → 001010 = 10. Answer: **−10**

**(b) 2's complement:** flip and add 1 → 001011 = 11. Answer: **−11**

From: §5, Rule 2

</details>

---

### S3 (Lecture 3, slides 10 to 12)

Work out −2 + 7 in 4 bits, using 1's complement and then 2's complement.

<details><summary>Answer</summary>

**1's complement:** −2 = 1101, +7 = 0111.

1101 + 0111 = 1 0100. End-around carry: 0100 + 1 = **0101** = +5 ✓

<br>

**2's complement:** −2 = 1110, +7 = 0111.

1110 + 0111 = 1 0101. Drop the carry: **0101** = +5 ✓

From: §7, Rule 4

</details>

---

### S4 (Lecture 3, slide 18)

In 4-bit 2's complement, what happens if you compute 4 + 5, or (−4) + (−5)?

<details><summary>Answer</summary>

**4 + 5:** 0100 + 0101 = 1001. That reads as **−7**. Overflow: +9 doesn't fit.

**(−4) + (−5):** 1100 + 1011 = 1 0111. Drop the carry: 0111 = **+7**. Overflow: −9 doesn't fit.

In both, two numbers of the same sign gave the other sign.

From: §8, Rule 5

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. In all three systems, positive numbers are written the same way.
2. 1's complement has only one representation of zero.
3. 4-bit 2's complement can store −8.
4. Adding a positive and a negative number can overflow.
5. A carry out of the left end always means overflow.

<details><summary>Answer</summary>

1. **True.** (Big idea, §4)
2. **False.** It has +0 (0000) and −0 (1111). (§4)
3. **True.** 1000 = −8. (§4, §6)
4. **False.** The answer is always between the two inputs. (§8)
5. **False.** −2 + 7 has a carry out but no overflow. (§8)

</details>

---

### M2: Multiple choice

What is the range of an 8-bit 2's complement number?

- A. 0 to 255
- B. −127 to +127
- C. −128 to +127
- D. −128 to +128

<details><summary>Answer</summary>

**C.**

−2⁷ to 2⁷ − 1 = −128 to +127.

(A is unsigned. B is signed magnitude or 1's complement.)

From: §6, Rule 3

</details>

---

### M3: Calculation (study guide)

Write −37 in 8 bits as:

1. signed magnitude
2. 1's complement
3. 2's complement

<details><summary>Answer</summary>

+37 = 32 + 4 + 1 = **00100101**

1. Flip the sign bit: **10100101**
2. Flip every bit: **11011010**
3. Flip every bit and add 1: **11011011**

(Shortcut check: from the right, copy "1". Flip the rest: 0010010 → 1101101. Gives 11011011 ✓)

From: §1, §2, §3

</details>

---

### M4: Overflow

In 4-bit 2's complement, work out each sum. Say whether it overflows.

1. 5 + (−3)
2. (−3) + (−6)
3. 6 − 2

<details><summary>Answer</summary>

**1.** 0101 + 1101 = 1 0010. Drop the carry: 0010 = **+2**. Positive + negative: **no overflow**.

**2.** 1101 + 1010 = 1 0111. Drop the carry: 0111 = +7. Two negatives gave a positive: **overflow**. (The real answer, −9, is below −8.)

**3.** 6 − 2 = 6 + (−2) = 0110 + 1110 = 1 0100. Drop the carry: 0100 = **+4**. **No overflow.**

From: §7, §8, Rules 4 and 5

</details>

---

### M5: 1's complement addition

Add −3 + (−2) in 4-bit 1's complement.

<details><summary>Answer</summary>

−3 = 1100, −2 = 1101.

1100 + 1101 = 1 1001.

End-around carry: 1001 + 1 = **1010**.

Check: flip 1010 → 0101 = 5. So it's **−5** ✓

From: §7, Rule 4

</details>

---

### M6: Same bits, three meanings

What does the 8-bit pattern 10000000 mean in each system?

<details><summary>Answer</summary>

**Signed magnitude:** sign 1, magnitude 0000000 → **−0**

**1's complement:** flip → 01111111 = 127 → **−127**

**2's complement:** flip and add 1 → 10000000 = 128 → **−128**

From: §4, §5

</details>

---

### M7: Explain

Give two reasons why computers use 2's complement instead of signed magnitude.

<details><summary>Answer</summary>

1. You can add signed numbers with a plain adder. No extra logic is needed to decide whether to add or subtract. Just drop the carry.
2. There's only one zero, so no confusion between +0 and −0, and the range goes one further (to −2ⁿ⁻¹).

From: §4, §7

</details>
