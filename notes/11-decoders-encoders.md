# Topic 11 — Decoders and encoders

Slide exercises: full adder on a 3-to-8 decoder (active-high and active-low)

Slides: Lecture 9, all

---

## The big idea

A **decoder** turns a binary number into "switch on line number i".

An **encoder** does the opposite.

<br>

The big trick:

A decoder's outputs are exactly the **minterms** (Topic 7).

So **any function = a decoder + one OR gate.**

---

**How to use these notes:**
When you see 🧠, stop.
Answer it on paper first.
Then click to check.

---

## 1. What a decoder does

![2-to-4 decoder](../img/11/s2.png)

An **n-to-2ⁿ decoder** has n inputs and 2ⁿ outputs.

The inputs form a binary number, **i**.

**Only output i is 1.** All others are 0.

<br>

**2-to-4 decoder** (inputs A₁A₀):

| A₁ | A₀ | Z₀ | Z₁ | Z₂ | Z₃ |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

Example: A₁A₀ = 10 (decimal 2) → **Z₂ = 1**, the rest are 0.

<br>

**Output equations:**

Z₀ = A₁'A₀' · Z₁ = A₁'A₀ · Z₂ = A₁A₀' · Z₃ = A₁A₀

<br>

### 🧠 Check
A 3-to-8 decoder gets input 101. Which output is 1?

<details><summary>Answer</summary>

101 = 5, so **output 5** (D₅). All others are 0.

</details>

---

## 2. 3-to-8 decoder

![3-to-8 table](../img/11/s3.png)

![3-to-8 circuit](../img/11/s4.png)

**How to read this diagram:**

Three inputs (x, y, z) and their inverted copies run down the middle.

Each of the 8 AND gates picks one combination. D₀ = x'y'z' … D₇ = xyz.

<br>

**Used for:** memory selection and keyboard scanning.

---

## 3. A decoder is a minterm generator

![Minterm generator](../img/11/s5.png)

Look at the output equations: each one is a **minterm**.

- For any input, exactly one output is 1.
- Each output contains every input variable.

---

### 📐 Rule 1: any function from an active-high decoder

**Step 1.** Write the function as **Σm**.

**Step 2.** Feed the inputs into an n-to-2ⁿ decoder.

**Step 3.** **OR** together the outputs listed in Σm.

**Why it works:**
Each output is one minterm. OR-ing minterms gives the sum of minterms.

**Use it when:**
"Implement f with a decoder and gates."

---

## 4. Worked example: full adder on a decoder

![Full adder decoder](../img/11/s6.png)

Full adder (Topic 10): C = Σm(3, 5, 6, 7), S = Σm(1, 2, 4, 7).

<br>

Wire X, Y, Z into a 3-to-8 decoder (X is the MSB).

**S** = OR of outputs **1, 2, 4, 7**

**C** = OR of outputs **3, 5, 6, 7**

Two OR gates. Done.

<br>

### 🧠 Check
f(x, y, z) = Σm(0, 6). How would you build it with a 3-to-8 decoder?

<details><summary>Answer</summary>

OR together outputs **0 and 6**. One 2-input OR gate.

</details>

---

## 5. Enable input

![Enable](../img/11/s7.png)

Many decoders have an **enable (EN)** input.

- **EN = 1:** works as normal. Exactly one output is 1.
- **EN = 0:** switched off. **All outputs are 0.**

<br>

![Enable table](../img/11/s8.png)

**How to read this diagram:**

Left: the full table with all 8 rows.

Right: the short version. When EN = 0, S₁ and S₀ don't matter, so they're written as **x**.

| EN | S₁ | S₀ | Q₀ | Q₁ | Q₂ | Q₃ |
|---|---|---|---|---|---|---|
| 0 | x | x | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 1 |

---

## 6. Building a bigger decoder from smaller ones

![3-to-8 from 2-to-4](../img/11/s9.png)

**Two 2-to-4 decoders make one 3-to-8.**

- S₁ and S₀ go to **both** decoders.
- **S₂'** drives the **first** decoder's EN → gives Q₀ to Q₃.
- **S₂** drives the **second** decoder's EN → gives Q₄ to Q₇.

So S₂ picks which half is switched on.

<br>

### 🧠 Check
Input S₂S₁S₀ = 110. Which decoder is on, and which of its outputs is 1?

<details><summary>Answer</summary>

S₂ = 1, so the **second** decoder is on.

S₁S₀ = 10 = 2, so its output 2 is 1. That's **Q₆** overall.

</details>

---

## 7. Active-low decoders

![Active-low](../img/11/s10.png)

An **active-low** decoder is the same thing, with **everything inverted**:

- EN is inverted: it works when **EN = 0**.
- The outputs are inverted: the chosen output is **0**, all others are **1**.

<br>

![Active-low maxterms](../img/11/s11.png)

**Each output is now the complement of a minterm. That's a maxterm.**

Q₀ = (S₁'S₀')' = S₁ + S₀ = M₀

---

### 📐 Rule 2: any function from an active-low decoder

**Step 1.** Write the function as **ΠM** (the rows where f = 0).

**Step 2.** **AND** together the outputs listed in ΠM.

**Why it works:**
Each active-low output is a maxterm. AND-ing maxterms gives the product of maxterms.

**Remember:** you need an **AND** gate for a product of sums.

---

![Active-low full adder](../img/11/s12.png)

**Worked example: full adder on an active-low decoder.**

EN is tied to ground (logic 0), so it's always on.

C = ΠM(0, 1, 2, 4) → **AND outputs 0, 1, 2, 4**

S = ΠM(0, 3, 5, 6) → **AND outputs 0, 3, 5, 6**

<br>

### 🧠 Check
Why is the EN of the active-low decoder in this example connected to ground?

<details><summary>Answer</summary>

Ground is logic 0. An active-low EN switches the decoder **on** when it's 0. So the decoder is always enabled.

</details>

---

## 8. Encoders

![Encoder](../img/11/s13.png)

An **encoder** is the reverse of a decoder.

**m ≤ 2ⁿ input lines → n output lines.** The output is the number of the input that's on.

<br>

**8-to-3 encoder:**

$$X = D_4 + D_5 + D_6 + D_7$$

$$Y = D_2 + D_3 + D_6 + D_7$$

$$Z = D_1 + D_3 + D_5 + D_7$$

**How to get these:** X is the 4s bit, so it's 1 for inputs 4, 5, 6, 7. And so on.

<br>

**The problem:** it assumes **exactly one** input is 1.

- D₃ and D₅ both on → outputs 111 (= 7). **Wrong.**
- No inputs on → outputs 000. Looks the same as D₀.

<br>

### 🧠 Check
In the 8-to-3 encoder, only D₆ is on. What are X, Y, Z?

<details><summary>Answer</summary>

X = 1 (6 is in 4, 5, 6, 7). Y = 1 (6 is in 2, 3, 6, 7). Z = 0.

**110** = 6 ✓

</details>

---

## 9. Priority encoder

![Priority encoder](../img/11/s14.png)

**When several inputs are 1, the highest-numbered one wins.**

Lower inputs become **don't cares** (x) in the table.

<br>

**How to read the table:**

Each row: the 1 shows the highest input that's on. Every input to its left (lower numbers) is x.

Output ABC = the number of that input.

<br>

**8-to-3 priority encoder equations** (not on the slides):

$$A = D_4 + D_5 + D_6 + D_7$$

$$B = D_7 + D_6 + D_5'D_4'(D_3 + D_2)$$

$$C = D_7 + D_6'D_5 + D_6'D_4'D_3 + D_6'D_4'D_2'D_1$$

<br>

### 🧠 Check
D₂, D₃ and D₅ are on. What does an 8-to-3 priority encoder output?

<details><summary>Answer</summary>

D₅ is the highest, so it wins. Output = 5 = **101**.

</details>

---

## Method: any decoder / encoder question

1. **Function on an active-high decoder:** write Σm. **OR** those outputs.
2. **Function on an active-low decoder:** write ΠM. **AND** those outputs.
3. **Enable:** active-high works when EN = 1. Active-low works when EN = 0.
4. **Bigger decoder:** top select bit drives the ENs (one plain, one inverted). Lower bits go to both.
5. **Encoder output bit k:** OR of every input whose number has bit k = 1.
6. **Priority encoder:** highest-numbered active input wins.

---

Next: [End-of-topic test](../questions/11-decoders-encoders.md)
