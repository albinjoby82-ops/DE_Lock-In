# Topic 10 — Adders, carry lookahead, subtractors, multipliers

Slide exercises: none set, but every circuit here is a likely exam question

Slides: Lecture 7/8, all

---

## The big idea

Now we use Topics 6 to 9 to **design real circuits**.

The first one: a circuit that **adds**.

Everything else in a computer's maths unit (subtract, multiply) is built from adders.

<br>

**Four equations carry this topic:**

Half adder: S = X ⊕ Y, C = XY

Full adder: S = X ⊕ Y ⊕ Z, C = XY + XZ + YZ

---

**How to use these notes:**
When you see 🧠, stop.
Answer it on paper first.
Then click to check.

---

## 1. Combinational logic and the design procedure

A **combinational circuit** takes n inputs and gives m outputs using gates.

The output depends **only on the inputs right now**. No memory.

---

### 📐 Rule 1: design procedure for any combinational circuit

![Procedure](../img/10/s5.png)

**Step 1.** From the spec, decide the **inputs and outputs**. Give them letters.

**Step 2.** Write the **truth table**.

**Step 3.** **Simplify** each output (algebra or K-map).

**Step 4.** **Draw** the circuit.

**Use it when:**
Any "design a circuit that…" question.

---

## 2. XOR

![XOR](../img/10/s10.png)

**XOR (exclusive OR)** is 1 when the inputs are **different**.

$$A \oplus B = A'B + AB'$$

| A | B | A ⊕ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<br>

![Multiple XOR](../img/10/s11.png)

**With more inputs:** XOR is 1 when an **odd** number of inputs are 1.

That makes it perfect for adders and error checking (parity).

<br>

### 🧠 Check
What is 1 ⊕ 1 ⊕ 1?

<details><summary>Answer</summary>

Three 1s is an odd count, so **1**.

</details>

---

## 3. Half adder

Adds **two bits**: 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1, 1 + 1 = 10.

Needs two outputs: **S** (sum) and **C** (carry).

![Half adder table](../img/10/s7.png)

| X | Y | C | S |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

<br>

![Half adder maps](../img/10/s8.png)

The K-maps don't simplify anything.

---

### 📐 Equation 1: half adder

$$S = X \oplus Y \qquad\qquad C = XY$$

| Symbol | Means |
|---|---|
| X, Y | the two bits being added |
| S | sum bit |
| C | carry bit |

**Why:** S = X'Y + XY', which is exactly XOR. C is 1 only for 1 + 1.

**Use it when:**
Adding two bits with no carry coming in. Also inside the full adder and carry lookahead.

---

![Half adder circuit](../img/10/s9.png)

**How to read this diagram:**

(a) The sum with two ANDs and an OR. (b) The same sum with one XOR gate. The carry is one AND either way.

---

## 4. Full adder ⭐

Adds **three bits**: X, Y and a carry-in Z.

![Full adder table](../img/10/s12.png)

| X | Y | Z | C | S |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

**Tip:** C = 1 when **two or more** inputs are 1. S = 1 when an **odd number** are 1.

<br>

![Full adder maps](../img/10/s13.png)

**How to read this diagram:**

Top map (carry): three groups of 2 → XY + YZ + XZ.

Bottom map (sum): a **checkerboard**. No two 1s touch, so nothing simplifies.

---

### 📐 Equation 2: full adder

$$S = X \oplus Y \oplus Z = \Sigma m(1, 2, 4, 7)$$

$$C = XY + XZ + YZ = \Sigma m(3, 5, 6, 7)$$

| Symbol | Means |
|---|---|
| X, Y | the two bits being added |
| Z | carry in from the bit to the right |
| S | sum bit |
| C | carry out to the bit on the left |

**Use it when:**
Adding one column of a multi-bit sum.

**Built directly:** the carry needs 3 ANDs + 1 OR. The sum needs 4 ANDs + 1 OR.

![Direct build](../img/10/s14.png)

---

## 5. Full adder from two half adders

![Two half adders](../img/10/s15.png)

**How to read this diagram:**

Half adder 1 adds x and y → S₁ and C₁.

Half adder 2 adds S₁ and z → S₂ (the final sum) and C₂.

An OR combines the two carries.

<br>

$$S_1 = X \oplus Y \qquad C_1 = XY$$

$$S = S_1 \oplus Z \qquad C_2 = S_1 Z$$

$$C = C_1 + C_2 = XY + (X \oplus Y)Z$$

<br>

![Carry check](../img/10/s17.png)

This carry **looks different** from XY + XZ + YZ, but it gives the **same truth table**.

<br>

### 🧠 Check
X = 1, Y = 0, Z = 1. Find S₁, C₁, S and C.

<details><summary>Answer</summary>

S₁ = 1 ⊕ 0 = 1. C₁ = 1 · 0 = 0.

S = 1 ⊕ 1 = **0**. C₂ = 1 · 1 = 1.

C = 0 + 1 = **1**.

(1 + 0 + 1 = 2 = 10 ✓)

</details>

---

## 6. Ripple carry adder

![2-bit adder](../img/10/s18.png)

To add bigger numbers, chain full adders. **One per bit.**

Each carry-out feeds the next carry-in.

<br>

![4-bit ripple](../img/10/s19.png)

**How to read this diagram:**

Four full adders (FA) side by side. Bit 0 on the right.

The carry C₀ comes in on the right (usually 0). C₄ comes out on the left.

<br>

**The problem: speed.**

![Delay](../img/10/s20.png)

Each adder must **wait** for the carry from the one before.

The carry **ripples** through every stage.

**Delay ≈ 2n gate delays** for n bits. Each gate delay is about 10 ns.

<br>

**Why not just build a 4-bit adder straight from a truth table?**

It would have 9 inputs (4 + 4 + carry-in). That's 2⁹ = **512 rows**. Too big.

<br>

### 🧠 Check
Roughly how long does a 16-bit ripple carry adder take, at 10 ns per gate?

<details><summary>Answer</summary>

2n = 32 gate delays. 32 × 10 ns = **320 ns**.

</details>

---

## 7. Carry lookahead ⭐

Work out **every carry at once**, straight from the inputs. No waiting.

![CLA definitions](../img/10/s22.png)

---

### 📐 Equation 3: propagate and generate

$$P_i = A_i \oplus B_i \qquad\qquad G_i = A_i B_i$$

$$S_i = P_i \oplus C_i \qquad\qquad C_{i+1} = G_i + P_i C_i$$

| Symbol | Means |
|---|---|
| Aᵢ, Bᵢ | bit i of the two numbers |
| Gᵢ | **generate**: this bit makes a carry by itself (1 + 1) |
| Pᵢ | **propagate**: this bit passes an incoming carry on (exactly one input is 1) |
| Cᵢ | carry into bit i. C₀ is the input carry. |

**What it means:**
A carry comes out of bit i if bit i **generates** one, **or** if it **propagates** the one coming in.

**Use it when:**
Writing out carry lookahead equations.

---

![Half adder makes P and G](../img/10/s23.png)

A half adder makes Pᵢ and Gᵢ: its sum is Pᵢ and its carry is Gᵢ.

<br>

**Expanding the carries** (keep substituting the previous one):

![Carries](../img/10/s24.png)

$$C_1 = G_0 + P_0 C_0$$

$$C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$$

$$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$

$$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$

(The slides stop at C₃. C₄ follows the same pattern.)

**Pattern:** each term is "some bit generates, and every bit after it propagates".

<br>

![CLA circuit](../img/10/s25.png)

Every carry is now just **two levels** of gates (AND then OR). Fast.

![CLA adder](../img/10/s26.png)

---

## 8. Carry lookahead: the catch

![Practical](../img/10/s27.png)

| Problem | Why |
|---|---|
| Gates grow as **O(n²)** | each carry has more terms |
| Transistors grow as **O(n³)** | and each term has more inputs |
| Wide gates are **slow** | and there are technology limits |

**Real designs mix the two:**
- 8-bit adder = two 4-bit CLA blocks, rippled together.
- 16-bit adder = four 4-bit ripple adders, linked by lookahead.

<br>

### 🧠 Check
Write C₂ in terms of P, G and C₀.

<details><summary>Answer</summary>

C₂ = G₁ + P₁C₁ = G₁ + P₁(G₀ + P₀C₀)

= **G₁ + P₁G₀ + P₁P₀C₀**

</details>

---

## 9. Subtraction

![Half subtractor](../img/10/s29.png)

Half subtractor: X − Y. Outputs **D** (difference) and **B** (borrow).

| X | Y | B | D |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 |

---

### 📐 Equation 4: subtraction

**Half subtractor:**

$$D = X \oplus Y \qquad\qquad B = X'Y$$

A borrow happens only for 0 − 1.

**Full subtractor** (two half subtractors + an OR):

$$D = X \oplus Y \oplus Z \qquad\qquad B = X'Y + X'Z + YZ$$

**The easy way (what real circuits do):** use 2's complement (Topic 4).

$$A - B = A + B' + 1$$

Invert every bit of B, and set the adder's carry-in to **1**.

**Use it when:**
Building a subtractor. The 2's complement way reuses the adder you already have.

---

<br>

### 🧠 Check
Why does setting the carry-in to 1 help with subtraction?

<details><summary>Answer</summary>

−B in 2's complement = flip B, then add 1.

The inverters do the flip. The carry-in of 1 does the "add 1". So the adder computes A + (−B).

</details>

---

## 10. Multiplication

![2x2 multiplier](../img/10/s31.png)

Multiplying two bits = **AND**. So each partial product bit is an AND gate.

<br>

**2 × 2 bits** (A₁A₀ × B₁B₀):

| Output | Equation |
|---|---|
| C₀ | A₀B₀ |
| C₁ | A₀B₁ ⊕ A₁B₀ (half adder sum). Its carry is K = A₀B₁ · A₁B₀ |
| C₂ | A₁B₁ ⊕ K (half adder sum) |
| C₃ | A₁B₁ · K (half adder carry) |

That's **4 ANDs and 2 half adders**.

**⚠️ C₃ to C₀ are the product bits, not carries.**

<br>

![4x4 multiplier](../img/10/s32.png)

**4 × 4 bits:**

16 ANDs make **four partial products**. Each is either 0000 or the multiplicand.

Add them in pairs with **three 4-bit adders**, each shifted left one place.

Slide example: 1101 × 0110 = **1001110** (13 × 6 = 78)

---

## 11. Shifts

![Shift](../img/10/s34.png)

| Shift | Effect | Example |
|---|---|---|
| left 1 | × 2 | 11 → 110 (3 → 6) |
| left 2 | × 4 | 11 → 1100 (3 → 12) |
| right 1 | ÷ 2 | 110 → 11 (6 → 3) |

Just like adding a 0 in decimal multiplies by 10.

---

## Method: any adder question

1. **Half adder:** S = X ⊕ Y, C = XY.
2. **Full adder:** S = X ⊕ Y ⊕ Z, C = XY + XZ + YZ (or XY + (X ⊕ Y)Z from two half adders).
3. **n-bit ripple adder:** chain n full adders. Delay ≈ 2n gate delays.
4. **Carry lookahead:** Pᵢ = Aᵢ ⊕ Bᵢ, Gᵢ = AᵢBᵢ, Cᵢ₊₁ = Gᵢ + PᵢCᵢ. Expand.
5. **Subtract:** A + B' + 1.
6. **Design from scratch:** use the 4-step procedure (Rule 1).

---

Next: [End-of-topic test](../questions/10-adders.md)
