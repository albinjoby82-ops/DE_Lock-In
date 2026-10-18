# 09 · Don't cares, NAND-NAND and NOR-NOR

Lecture 6, all · ●●● · [**Quiz →**](https://albinjoby82-ops.github.io/DE_Lock-In/quiz.html?t=09)

Two upgrades: **don't cares** make bigger K-map blocks, and **NAND / NOR only** circuits are what real chips prefer.

---

## 1. Don't cares (x)

An input that never happens, or whose output doesn't matter, gets an **x**.

**Rule:** treat x as **1** if it makes a block bigger. Otherwise treat it as 0 and ignore it. You **never** have to cover an x.

![x used as 0](../docs/svg/dc-before.svg) ![x used as 1](../docs/svg/dc-after.svg)

Σm(0, 2, 3, 4, 7) + d(6): **F = C' + B** instead of three terms.

> **Apply:** F(A, B, C) = Σm(1, 3) + d(5, 7). Minimum SOP?
<details><summary>Answer</summary>

Use both x's: column C = 1 is a block of 4 → **F = C**.

</details>

---

## 2. Why NAND and NOR?

CMOS transistor counts (n inputs):

| NAND | NOR | AND | OR | NOT |
|---|---|---|---|---|
| **2n** | **2n** | 2n + 2 | 2n + 2 | 2 |

AND = NAND + inverter, so it costs 2 more. NAND and NOR are smaller **and** faster.

> **Apply:** transistors in a 3-input NAND? A 3-input AND?
<details><summary>Answer</summary>

NAND 2 × 3 = **6**. AND 6 + 2 = **8**.

</details>

---

## 3. The trick: De Morgan turns gates inside out

![NAND = bubbled OR](../docs/svg/demorgan-gates.svg)

A NAND **is** an OR with inverted inputs. So in an AND-OR circuit, add two bubbles on each middle wire (they cancel). Every gate becomes a NAND.

---

## 4. NAND-NAND recipe (from SOP)

1. Minimum **SOP** (K-map, use don't cares).
2. Draw AND → OR.
3. Swap **every** gate for **NAND**. Same wires.
4. A **single letter** going straight into the output gate: **complement it**.

![AND-OR to NAND-NAND](../docs/svg/nand-transform.svg)

Why step 4: a lone letter has no first-level gate, so it misses its bubble. The output NAND would flip it.

## 5. NOR-NOR recipe (from POS)

Same four steps, but start from the minimum **POS** (group the 0s), draw OR → AND, swap every gate for **NOR**, complement lone letters.

> **Apply:** build F = AB + C from NANDs only.
<details><summary>Answer</summary>

Gate 1 = NAND(A, B). C is a lone letter → feed **C'**. Output = NAND(gate 1, C').
Check: ((AB)' · C')' = AB + C ✓

</details>

---

## Exam drill (slides 14 and 15)

**1.** Simplify F = A'B'C + AC' + ACD + ACD' and build it with two-level NANDs.

<details><summary>Answer</summary>

![K-map](../docs/svg/k4-nand.svg)

**F = A + B'C** → NAND(B', C), then NAND(**A'**, gate 1).

![NAND circuit](../docs/svg/nand-slide14.svg)

</details>

**2.** Simplify F = AC' + ACD' + ABD and build it with two-level NORs.

<details><summary>Answer</summary>

Group the 0s:

![K-map of 0s](../docs/svg/k4-nor.svg)

**F = A(B + C' + D')** → NOR(B, C', D'), then NOR(**A'**, gate 1).

![NOR circuit](../docs/svg/nor-slide15.svg)

</details>

**Traps**
- NAND ← SOP. NOR ← POS. Don't mix them up.
- Complement the **lone letters** at the output gate.
- An x never has to be covered.
