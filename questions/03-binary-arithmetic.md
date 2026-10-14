# Topic 3 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises

### S1 (Lecture 2, slide 26)

Add, subtract and multiply in binary: 111 and 101.

<details><summary>Answer</summary>

**Add:** 111 + 101 = **1100** (7 + 5 = 12)

**Subtract:** 111 − 101 = **010** (7 − 5 = 2)

**Multiply:**

```
        1 1 1
      × 1 0 1
      -------
        1 1 1
      0 0 0
  + 1 1 1
  -----------
    1 0 0 0 1 1
```

111 × 101 = **100011** (7 × 5 = 35)

From: §1, §2, §3

</details>

---

### S2 (Lecture 2, slide 28)

Divide in binary: 10010001 ÷ 1011.

<details><summary>Answer</summary>

| Bring down | Fits 1011? | Answer bit | Left over |
|---|---|---|---|
| 10010 | yes | 1 | 111 |
| 1110 | yes | 1 | 11 |
| 110 | no | 0 | 110 |
| 1101 | yes | 1 | 10 |

10010001 ÷ 1011 = **1101 remainder 10**

Decimal check: 145 ÷ 11 = 13 r 2 ✓

From: §4, Rule 4

</details>

---

### S3 (Lecture 2, slide 19)

Add 101011 + 011011. Then check by subtracting.

<details><summary>Answer</summary>

101011 + 011011 = **1000110**

(43 + 27 = 70 ✓)

Check: 1000110 − 101011 = **011011** ✓

From: §1, §2

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. In binary, 1 + 1 = 2.
2. 1 + 1 + 1 = 11 in binary.
3. 0 − 1 in binary gives 1 with a borrow.
4. Shifting a binary number right by one place multiplies it by 2.
5. In binary long division, each answer bit is 0 or 1.

<details><summary>Answer</summary>

1. **False.** There's no "2". 1 + 1 = 10. (§1)
2. **True.** Write 1, carry 1. (§1)
3. **True.** (§2)
4. **False.** Right = ÷ 2. Left = × 2. (§5)
5. **True.** The divisor fits once or not at all. (§4)

</details>

---

### M2: Multiple choice

What is 1101 × 0110?

- A. 1001110
- B. 1011110
- C. 110110
- D. 1000110

<details><summary>Answer</summary>

**A.**

The multiplier 0110 has 1s in places 1 and 2.

So add 1101 shifted 1 and 1101 shifted 2:

11010 + 110100 = **1001110**

Check: 13 × 6 = 78 = 64 + 8 + 4 + 2 ✓

From: §3, Rule 3

</details>

---

### M3: Calculation

Work out 11011 − 01101. Check in decimal.

<details><summary>Answer</summary>

11011 − 01101 = **01110**

Check: 27 − 13 = 14 = 8 + 4 + 2 ✓

From: §2

</details>

---

### M4: Calculation

Divide 1100100 by 101.

<details><summary>Answer</summary>

| Bring down | Fits 101? | Answer bit | Left over |
|---|---|---|---|
| 110 | yes | 1 | 1 |
| 10 | no | 0 | 10 |
| 101 | yes | 1 | 0 |
| 0 | no | 0 | 0 |
| 0 | no | 0 | 0 |

Answer: **10100 remainder 0**

Check: 100 ÷ 5 = 20 = 10100 ✓

From: §4, Rule 4

</details>

---

### M5: Shifting

1. Shift 101 left three places. What decimal number do you get?
2. Shift 11000 right three places. What do you get?

<details><summary>Answer</summary>

1. 101000 = **40**. That's 5 × 8, because 3 shifts = × 2 × 2 × 2.
2. 11 = **3**. That's 24 ÷ 8.

From: §5

</details>

---

### M6: Explain

Why is binary long division simpler than decimal long division?

<details><summary>Answer</summary>

In decimal you have to guess how many times (0 to 9) the divisor fits.

In binary it either fits (write 1 and subtract) or it doesn't (write 0).

From: §4

</details>
