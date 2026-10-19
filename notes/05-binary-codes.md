# 05 · Binary codes

Lecture 3, slides 20–24 · ● · [**Quiz →**](https://albinjoby82-ops.github.io/DE_Lock-In/quiz.html?t=05)

**▶ Explainer videos** (tap to search YouTube):
- [BCD binary coded decimal](https://www.youtube.com/results?search_query=BCD+binary+coded+decimal)
- [Gray code explained](https://www.youtube.com/results?search_query=Gray+code+explained)
- [binary to Gray code conversion](https://www.youtube.com/results?search_query=binary+to+Gray+code+conversion)
- [one-hot encoding digital logic](https://www.youtube.com/results?search_query=one-hot+encoding+digital+logic)

A **code** is a list: each bit pattern stands for one thing. **n bits give 2ⁿ patterns.**

> **Apply:** how many bits to code 10 items? 40 items?
<details><summary>Answer</summary>

Smallest n with 2ⁿ ≥ items: 10 → **4** (16). 40 → **6** (64).

</details>

---

## 1. BCD: 4 bits per decimal digit

▶ Video: [BCD binary coded decimal](https://www.youtube.com/results?search_query=BCD+binary+coded+decimal)

**Rule:** code each decimal digit on its own. 1010 to 1111 are **never** used.

185 → 0001 | 1000 | 0101. Not the same as binary (185 = 10111001).

> **Apply:** 92 in BCD. Is 0110 1011 valid BCD?
<details><summary>Answer</summary>

92 = **1001 0010**. 0110 1011 is **not valid**: 1011 = 11 isn't a digit.

</details>

---

## 2. Gray code: neighbours differ in ONE bit

▶ Video: [Gray code explained](https://www.youtube.com/results?search_query=Gray+code+explained) · [binary to Gray code conversion](https://www.youtube.com/results?search_query=binary+to+Gray+code+conversion)

| Dec | Gray | Dec | Gray |
|---|---|---|---|
| 0 | 0000 | 4 | 0110 |
| 1 | 0001 | 5 | 0111 |
| 2 | 0011 | 6 | 0101 |
| 3 | 0010 | 7 | 0100 |

**Why:** one corrupted bit only moves you to a neighbour. (Binary 0011 → 0111 jumps 3 → 7.)

**Quick way (not on slides):** keep the MSB. Each next Gray bit = this binary bit XOR the one to its left (1 if they differ).

You'll see Gray order again on every K-map: **00, 01, 11, 10**.

> **Apply:** binary 0110 → Gray.
<details><summary>Answer</summary>

0 | 0≠1 → 1 | 1=1 → 0 | 1≠0 → 1 → **0101** (= 6 in the table ✓)

</details>

---

## 3. One-hot: one bit per value

▶ Video: [one-hot encoding digital logic](https://www.youtube.com/results?search_query=one-hot+encoding+digital+logic)

Exactly one bit is 1. Value k → bit position k − 1 (from the right, starting at 0).

| Value | 1 | 3 | 5 | 8 |
|---|---|---|---|---|
| 8-bit one-hot | 00000001 | 00000100 | 00010000 | 10000000 |

Lots of bits, but trivial to decode.

> **Apply:** which value is 00100000?
<details><summary>Answer</summary>

The 1 is at position 5 → value **6**.

</details>

---

**Summary: 4 in each code** · binary 0100 · BCD 0100 · Gray 0110 · one-hot 00001000

---

## Test yourself

**▶ [Topic 05 quiz](https://albinjoby82-ops.github.io/DE_Lock-In/quiz.html?t=05)** (answers checked as you go, **New numbers** for fresh practice)  
[Mixed quiz: topics 04 + 05](https://albinjoby82-ops.github.io/DE_Lock-In/quiz.html?mix=04,05&n=15)  
[All quizzes](https://albinjoby82-ops.github.io/DE_Lock-In/)

Next: [06 · Gates and Boolean algebra](06-boolean-algebra.md)
