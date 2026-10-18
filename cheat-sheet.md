# Cheat sheet

No formula sheet in the exam. This page is the whole module in one go. Read it the night before.

## Numbers

| 2⁰ | 2¹ | 2² | 2³ | 2⁴ | 2⁵ | 2⁶ | 2⁷ | 2⁸ | 2⁻¹ | 2⁻² | 2⁻³ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 0.5 | 0.25 | 0.125 |

- **Hex:** A=10 B=11 C=12 D=13 E=14 F=15.
- **Decimal → base b:** whole part ÷ b, remainders read **up**. Fraction × b, whole parts read **down**. [02](notes/02-number-systems.md)
- **Binary → octal / hex:** groups of 3 / 4 outward from the point. Pad the fraction on the **right**.
- **Arithmetic:** 1+1 = 10, 1+1+1 = 11, 0−1 = 1 borrow 1. Multiply = shift and add. [03](notes/03-binary-arithmetic.md)

| Negative | Make it | Zeros | n-bit range |
|---|---|---|---|
| Signed mag | flip sign bit | two | ±(2ⁿ⁻¹ − 1) |
| 1's | flip all | two | ±(2ⁿ⁻¹ − 1) |
| 2's | flip all, +1 | one | −2ⁿ⁻¹ to 2ⁿ⁻¹ − 1 |

- 2's shortcut: copy up to the first 1 from the right, flip the rest. [04](notes/04-signed-numbers.md)
- Add: 1's → end-around carry. 2's → drop the carry.
- **Overflow:** same signs in, other sign out. Never with mixed signs.
- **Codes:** BCD 4 bits per digit (1010–1111 unused). Gray: neighbours differ by 1 bit. One-hot: one 1. [05](notes/05-binary-codes.md)

## Boolean logic

- x + 1 = 1 · x + x = x · x + x' = 1 · **x + yz = (x + y)(x + z)** [06](notes/06-boolean-algebra.md)
- De Morgan: (x + y)' = x'y' · (xy)' = x' + y'
- x + xy = x · x + x'y = x + y · xy + x'z + yz = xy + x'z
- **Minterm:** 0 → x'. **Maxterm:** 0 → x. Σm(1-rows) = ΠM(0-rows). [07](notes/07-minterms-maxterms.md)
- **K-map:** rows/cols 00, 01, **11, 10**. Blocks of 1, 2, 4, 8, 16, as big as possible, edges and corners wrap. 2ᵏ cells remove k letters. SOP: group 1s. POS: group 0s (0 → plain). [08](notes/08-karnaugh-maps.md)
- **Don't care:** use an x only if it grows a block. [09](notes/09-dont-cares-nand-nor.md)
- **NAND-NAND** ← min SOP. **NOR-NOR** ← min POS. Swap every gate, complement lone letters at the output gate.
- CMOS: NAND, NOR 2n · AND, OR 2n + 2 · NOT 2.

## Combinational blocks

- Half adder: **S = X ⊕ Y, C = XY**. Full adder: **S = X ⊕ Y ⊕ Z, C = XY + XZ + YZ = XY + (X ⊕ Y)Z**. [10](notes/10-adders.md)
- Ripple carry ≈ 2n gate delays.
- Lookahead: **Pᵢ = Aᵢ ⊕ Bᵢ, Gᵢ = AᵢBᵢ, Cᵢ₊₁ = Gᵢ + PᵢCᵢ, Sᵢ = Pᵢ ⊕ Cᵢ**.
- Subtract: A + B' + 1. Half subtractor D = X ⊕ Y, Borrow = X'Y.
- Decoder: active-high → **OR** the Σm outputs. Active-low → **AND** the ΠM outputs. [11](notes/11-decoders-encoders.md)
- Encoder: bit k = OR of inputs with bit k = 1. Priority: highest wins.
- Mux: **Y = S'I₀ + SI₁**. n variables on n − 1 selects: each row pair → 0, 1, v, v'. [12](notes/12-multiplexers.md)
