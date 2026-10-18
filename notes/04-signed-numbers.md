# 04 · Signed numbers and overflow

Lecture 3, slides 4–19 · ●●● · [**Quiz →**](https://albinjoby82-ops.github.io/DE_Lock-In/quiz.html?t=04)

The leftmost bit is the **sign**: 0 = positive, 1 = negative. Positives look the same in all three systems. Only the way you make a **negative** changes.

---

## 1. Three ways to make −5 (4 bits, +5 = 0101)

| System | Rule | −5 |
|---|---|---|
| Signed magnitude | flip the **sign bit** only | 1101 |
| 1's complement | flip **every** bit | 1010 |
| 2's complement ⭐ | flip every bit, **then add 1** | 1011 |

**Shortcut for 2's complement:** from the right, **copy** up to and including the first 1, **flip** everything left of it.

![2's complement shortcut](../docs/svg/twos-shortcut.svg)

> **Apply:** −6 in 4-bit signed magnitude, 1's and 2's complement.
<details><summary>Answer</summary>

+6 = 0110 → SM **1110**, 1's **1001**, 2's **1010**.

</details>

> **Apply:** 2's complement of 00101000.
<details><summary>Answer</summary>

Copy `1000`, flip `0010` → `1101`. **11011000**.

</details>

---

## 2. Reading a negative number

**Rule:** sign bit 1 → negate it with the **same** system's rule → read the size → put a minus in front.

Same bits, different answer per system. Always check which one the question says.

> **Apply:** read 110101 as 1's complement, then as 2's complement.
<details><summary>Answer</summary>

1's: flip → 001010 = 10 → **−10**.
2's: flip + 1 → 001011 = 11 → **−11**.

</details>

---

## 3. Ranges (n bits, sign bit included)

| System | Range | 4-bit | Zeros |
|---|---|---|---|
| Unsigned | 0 to 2ⁿ − 1 | 0 to 15 | — |
| SM and 1's | −(2ⁿ⁻¹ − 1) to +(2ⁿ⁻¹ − 1) | −7 to +7 | **two** (+0, −0) |
| 2's | **−2ⁿ⁻¹** to +(2ⁿ⁻¹ − 1) | **−8** to +7 | one |

2's complement gets one extra number because it doesn't waste a pattern on −0.

> **Apply:** range of 8-bit 2's complement?
<details><summary>Answer</summary>

−2⁷ to 2⁷ − 1 = **−128 to +127**.

</details>

---

## 4. Adding signed numbers

**Rule:** just add the bits.
- **2's:** a carry out of the left end is **thrown away**.
- **1's:** a carry out of the left end is **added back** to the result (end-around carry).

Subtract by adding: A − B = A + (−B).

| −2 + 7 | 1's complement | 2's complement |
|---|---|---|
| add | 1101 + 0111 = **1** 0100 | 1110 + 0111 = **1** 0101 |
| carry | add it back: 0100 + 1 | drop it |
| answer | **0101** = +5 | **0101** = +5 |

> **Apply:** 5 − 3 in 4-bit 2's complement.
<details><summary>Answer</summary>

0101 + 1101 = **1** 0010 → drop the carry → **0010** = +2.

</details>

---

## 5. Overflow: walk round the wheel

Adding = walking clockwise. Crossing the line between +7 and −8 = **overflow**.

![4-bit two's complement wheel](../docs/svg/wheel4.svg)

**Rule:** overflow only when **two positives give a negative**, or **two negatives give a positive**. A positive plus a negative can **never** overflow.

A carry out of the left end is **not** overflow (−2 + 7 had a carry and was fine).

> **Apply:** 4-bit 2's complement. Does 6 + 3 overflow? Does −4 + −5?
<details><summary>Answer</summary>

6 + 3: 0110 + 0011 = 1001. Two positives gave a negative → **overflow** (+9 > +7).
−4 + −5: 1100 + 1011 = **1** 0111 → 0111 = +7. Two negatives gave a positive → **overflow** (−9 < −8).

</details>

---

## Exam drill (slide exercises)

**1.** 2's complement of 01010110. **2.** Read 110101 as 1's and as 2's complement.

<details><summary>Answer</summary>

1. Copy `10`, flip `010101` → **10101010**.
2. 1's: **−10**. 2's: **−11**.

</details>

**Traps**
- Pad positives with 0s to the full bit count **before** negating.
- 1's: end-around carry. 2's: drop the carry.
- Overflow is about the **sign bits**, not the carry out.
