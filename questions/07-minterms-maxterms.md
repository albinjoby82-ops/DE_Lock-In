# Topic 7 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises

### S1 (Lecture 4, slides 16, 19 and 21)

A function f(x, y, z) is 1 on rows 0, 1, 2, 3 and 6.

1. Write f as a sum of minterms, in Σm form and in letters.
2. Write f as a product of maxterms.
3. Write f' both ways.

<details><summary>Answer</summary>

**1.** f = Σm(0, 1, 2, 3, 6)

= **x'y'z' + x'y'z + x'yz' + x'yz + xyz'**

<br>

**2.** f = 0 on rows 4, 5, 7.

f = ΠM(4, 5, 7) = **(x' + y + z)(x' + y + z')(x' + y' + z')**

<br>

**3.** f' = **Σm(4, 5, 7) = ΠM(0, 1, 2, 3, 6)**

From: §4, §6, §7, Rule 3

</details>

---

### S2 (Lecture 5, slide 9)

f(x, y, z) is 1 on rows 0, 2, 3 and 5, and 0 elsewhere. Write f as a product of maxterms.

<details><summary>Answer</summary>

f = 0 on rows 1, 4, 6, 7.

f = M₁ M₄ M₆ M₇ = **ΠM(1, 4, 6, 7)**

= **(x + y + z')(x' + y + z)(x' + y' + z)(x' + y' + z')**

From: §5, §6, Rule 2

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. A minterm is 1 on exactly one row of the truth table.
2. In a maxterm, a 0 bit gives a barred letter.
3. Every function has exactly one sum-of-minterms form.
4. mᵢ' = Mᵢ.
5. A POS expression builds as AND gates feeding one OR gate.

<details><summary>Answer</summary>

1. **True.** (§3)
2. **False.** In a maxterm, 0 gives a plain letter. (§5, Rule 2)
3. **True.** (§4)
4. **True.** By DeMorgan. (§7)
5. **False.** That's SOP. POS is OR gates feeding one AND. (§1, §2)

</details>

---

### M2: Multiple choice

For f(A, B, C, D), what is m₁₃?

- A. A'B'CD'
- B. ABC'D
- C. A' + B' + C + D'
- D. ABCD'

<details><summary>Answer</summary>

**B.**

13 = 1101 → A plain, B plain, C barred, D plain → ABC'D.

(C is M₁₃, the maxterm.)

From: §3, Rule 1

</details>

---

### M3: Conversion

f(x, y, z) = ΠM(0, 3, 5, 6). Write f as Σm. Then write it in letters.

<details><summary>Answer</summary>

Missing numbers: 1, 2, 4, 7.

f = **Σm(1, 2, 4, 7)**

= **x'y'z + x'yz' + xy'z' + xyz**

(This is the full adder's sum, from Topic 10.)

From: §7, Rule 3, and Rule 1

</details>

---

### M4: From an expression

f(a, b, c) = ab + c'. Find Σm and ΠM.

<details><summary>Answer</summary>

**Truth table** (f = 1 when ab = 1 or c = 0):

| Row | a b c | f |
|---|---|---|
| 0 | 000 | 1 |
| 1 | 001 | 0 |
| 2 | 010 | 1 |
| 3 | 011 | 0 |
| 4 | 100 | 1 |
| 5 | 101 | 0 |
| 6 | 110 | 1 |
| 7 | 111 | 1 |

f = **Σm(0, 2, 4, 6, 7)** = **ΠM(1, 3, 5)**

From: Topic 6 Rule 1, then §4, §6

</details>

---

### M5: Write a maxterm

For f(A, B, C, D), write M₆.

<details><summary>Answer</summary>

6 = 0110 → A plain, B barred, C barred, D plain.

M₆ = **A + B' + C' + D**

From: §5, Rule 2

</details>

---

### M6: Explain

Why does a minterm equal 1 on only one row?

<details><summary>Answer</summary>

It's an AND of every variable.

Each letter is written so that it's 1 only for that row's bit (plain for 1, barred for 0).

An AND is 1 only if every part is 1, so all the inputs must match that one row.

From: §3, Rule 1

</details>

---

### M7: Explain

A truth table can be written as x'z' + z, or as x' + z, or as x'z' + x'z + xz. Which is "best" and why?

<details><summary>Answer</summary>

**x' + z**, because it has the fewest terms and the fewest letters.

That means the fewest gates and gate inputs, so the circuit is cheaper and faster.

All three are correct. They have the same truth table.

From: §8, and Topic 6 Big idea

</details>
