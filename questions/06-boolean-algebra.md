# Topic 6 — End-of-topic test

Try each question first.
Then click to check.

Each answer says which notes section (§) it comes from.

---

## Part A: Slide exercises

### S1 (Lecture 4, slide 12)

Simplify x'y' + xyz + x'y using Boolean algebra. Name each step.

<details><summary>Answer</summary>

| Step | Expression | Rule |
|---|---|---|
| 1 | x'(y' + y) + xyz | distributive (14) |
| 2 | x' · 1 + xyz | axiom 7 |
| 3 | x' + xyz | axiom 2 |
| 4 | (x' + x)(x' + yz) | distributive (15) |
| 5 | 1 · (x' + yz) | axiom 7 |
| 6 | **x' + yz** | axiom 2 |

From: §4, §5

</details>

---

### S2 (Lecture 4, slide 7)

Write the truth table for f(x, y, z) = (x + y')z + x'.

<details><summary>Answer</summary>

| x | y | z | x + y' | (x + y')z | x' | f |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 | **1** |
| 0 | 0 | 1 | 1 | 1 | 1 | **1** |
| 0 | 1 | 0 | 0 | 0 | 1 | **1** |
| 0 | 1 | 1 | 0 | 0 | 1 | **1** |
| 1 | 0 | 0 | 1 | 0 | 0 | **0** |
| 1 | 0 | 1 | 1 | 1 | 0 | **1** |
| 1 | 1 | 0 | 0 | 0 | 0 | **0** |
| 1 | 1 | 1 | 1 | 1 | 0 | **1** |

f = 1 on rows 0, 1, 2, 3, 5, 7.

(This simplifies to x' + z. Try proving it in M4.)

From: §2, Rule 1

</details>

---

## Part B: Midterm-style questions

---

### M1: True or false

1. In Boolean algebra, 1 + 1 = 1.
2. x + 1 = x.
3. (xy)' = x'y'.
4. x + yz = (x + y)(x + z).
5. A truth table for 3 inputs has 6 rows.

<details><summary>Answer</summary>

1. **True.** OR, not normal adding. (§1)
2. **False.** x + 1 = 1 (axiom 3). (§4)
3. **False.** DeMorgan: (xy)' = x' + y'. (§4, Rule 2)
4. **True.** Axiom 15. (§4)
5. **False.** 2³ = 8. (§2)

</details>

---

### M2: Multiple choice

Which is equal to (a + b)'?

- A. a' + b'
- B. a'b'
- C. ab
- D. (ab)'

<details><summary>Answer</summary>

**B.** DeMorgan: flip each letter, swap OR → AND.

From: §4, Rule 2

</details>

---

### M3: Simplify

Simplify each one. Name the rules.

1. xy + xy'
2. (x + y)(x + y')
3. x'y'z + x'yz + xz
4. a + a'b

<details><summary>Answer</summary>

**1.** x(y + y') = x · 1 = **x** (14, 7, 2)

**2.** Axiom 15 backwards: x + yy' = x + 0 = **x** (15, 8, 1)

**3.** x'z(y' + y) + xz = x'z + xz = z(x' + x) = **z** (14, 7, 2, then 14, 7, 2)

**4.** **a + b** (shortcut x + x'y = x + y, or axiom 15: (a + a')(a + b) = 1 · (a + b))

From: §4, Rule 3, §5

</details>

---

### M4: Prove

Show that (x + y')z + x' = x' + z.

<details><summary>Answer</summary>

(x + y')z + x'

= xz + y'z + x' (distributive, 14)

= x' + xz + y'z (commutative)

= x' + z + y'z (shortcut x' + xz = x' + z)

= x' + z(1 + y') (distributive, 14)

= x' + z · 1 (axiom 3)

= **x' + z** (axiom 2)

From: §4, Rule 3, method

</details>

---

### M5: DeMorgan

Find the complement of F = a'b + c. Simplify so bars are only on single letters.

<details><summary>Answer</summary>

F' = (a'b + c)'

= (a'b)' · c' (DeMorgan, 16)

= (a + b') c' (DeMorgan, 17, and involution, 9)

**F' = (a + b')c'**

From: §4, Rule 2

</details>

---

### M6: Consensus

Simplify ab + a'c + bc.

<details><summary>Answer</summary>

This matches the consensus pattern xy + x'z + yz with x = a, y = b, z = c.

So the bc term is redundant.

**ab + a'c**

From: §4, Rule 3

</details>

---

### M7: Explain

Why do we bother simplifying Boolean expressions?

<details><summary>Answer</summary>

Each operation becomes a gate.

Fewer gates means the circuit is cheaper and uses less power.

Fewer gates between input and output usually means it's faster too.

From: Big idea, §3

</details>
