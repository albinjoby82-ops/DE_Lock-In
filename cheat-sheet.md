# Cheat sheet

Read this the night before.

No formula sheet is mentioned for this exam.

**So learn this page by heart.**

Each line is explained in the topic linked next to it.

---

## Numbers (Topics 2 to 4)

**Powers of 2**

| 2⁰ | 2¹ | 2² | 2³ | 2⁴ | 2⁵ | 2⁶ | 2⁷ | 2⁸ | 2⁹ | 2¹⁰ |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |

| 2⁻¹ | 2⁻² | 2⁻³ | 2⁻⁴ | 2⁻⁵ |
|---|---|---|---|---|
| 0.5 | 0.25 | 0.125 | 0.0625 | 0.03125 |

<br>

**Hex digits:** A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.

<br>

**Decimal → any base b** ([Topic 2](notes/02-number-systems.md))

Whole part: divide by b. Read the remainders **upward**.

Fraction part: multiply by b. Read the whole parts **downward**.

<br>

**Binary → octal or hex** ([Topic 2](notes/02-number-systems.md))

Group outward from the point. 3 bits for octal, 4 bits for hex.

Pad zeros at the **outer ends only**.

<br>

**Binary arithmetic** ([Topic 3](notes/03-binary-arithmetic.md))

1 + 1 = 10. 1 + 1 + 1 = 11. 0 − 1 = 1, borrow 1.

Multiply = shift and add.

<br>

**Negative numbers** ([Topic 4](notes/04-signed-numbers.md))

| System | Make it negative | Zeros | n-bit range |
|---|---|---|---|
| Signed magnitude | flip the sign bit | two | −(2ⁿ⁻¹ − 1) to +(2ⁿ⁻¹ − 1) |
| 1's complement | flip every bit | two | −(2ⁿ⁻¹ − 1) to +(2ⁿ⁻¹ − 1) |
| 2's complement | flip every bit, add 1 | one | −2ⁿ⁻¹ to +(2ⁿ⁻¹ − 1) |

2's complement shortcut: from the right, copy up to and including the first 1. Flip the rest.

1's complement add: carry out of the left → add it back on the right.

2's complement add: carry out of the left → throw it away.

Overflow: two numbers with the **same sign** give an answer with the **other sign**.

<br>

**Codes** ([Topic 5](notes/05-binary-codes.md))

BCD: 4 bits per decimal digit. Gray: neighbours differ by 1 bit. One-hot: one bit per value.

---

## Boolean logic (Topics 6 to 9)

**Key laws** ([Topic 6](notes/06-boolean-algebra.md))

$$x + x' = 1 \qquad x \cdot x' = 0$$

$$x + yz = (x + y)(x + z)$$

$$(x + y)' = x'y' \qquad (xy)' = x' + y'$$

$$x + xy = x \qquad x + x'y = x + y$$

<br>

**Minterm and maxterm** ([Topic 7](notes/07-minterms-maxterms.md))

Minterm: bit 0 → x', bit 1 → x.

Maxterm: bit 0 → x, bit 1 → x'.

Σm(rows where f = 1) = ΠM(rows where f = 0).

<br>

**K-map** ([Topic 8](notes/08-karnaugh-maps.md))

Order the rows and columns 00, 01, **11, 10**.

Groups of 1, 2, 4, 8 or 16. Make them as big as possible. Edges wrap.

A group of 2ᵏ cells removes k variables.

SOP: group the 1s. POS: group the 0s.

<br>

**Don't cares** ([Topic 9](notes/09-dont-cares-nand-nor.md))

Use an x as a 1 only if it makes a group bigger.

<br>

**NAND-NAND / NOR-NOR** ([Topic 9](notes/09-dont-cares-nand-nor.md))

NAND-NAND from the minimum SOP. NOR-NOR from the minimum POS.

Swap every gate. Complement any single letter going into the output gate.

<br>

**CMOS transistors** ([Topic 9](notes/09-dont-cares-nand-nor.md))

NAND and NOR: 2n. AND and OR: 2n + 2. NOT: 2.

---

## Combinational logic (Topics 10 to 12)

**Adders** ([Topic 10](notes/10-adders.md))

$$\text{Half adder: } S = X \oplus Y \qquad C = XY$$

$$\text{Full adder: } S = X \oplus Y \oplus Z \qquad C = XY + XZ + YZ = XY + (X \oplus Y)Z$$

Ripple carry delay: about 2n gate delays.

<br>

**Carry lookahead** ([Topic 10](notes/10-adders.md))

$$P_i = A_i \oplus B_i \qquad G_i = A_i B_i$$

$$S_i = P_i \oplus C_i \qquad C_{i+1} = G_i + P_i C_i$$

<br>

**Subtraction** ([Topic 10](notes/10-adders.md))

Half subtractor: D = X ⊕ Y, B = X'Y.

Or use 2's complement: A − B = A + B' + 1.

<br>

**Shifts:** left = × 2. Right = ÷ 2.

<br>

**Decoder** ([Topic 11](notes/11-decoders-encoders.md))

Active-high outputs are minterms → OR the ones in Σm.

Active-low outputs are maxterms → AND the ones in ΠM.

<br>

**Encoder** ([Topic 11](notes/11-decoders-encoders.md))

Assumes exactly one input is on. Priority encoder: highest number wins.

<br>

**Mux** ([Topic 12](notes/12-multiplexers.md))

2-to-1: Y = S'I₀ + SI₁.

n-variable function on a mux with n − 1 select lines: each pair of rows gives 0, 1, v or v'.
