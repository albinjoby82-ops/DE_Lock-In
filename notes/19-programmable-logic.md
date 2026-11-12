# 19 · Programmable logic (PROM, PAL, PLA, CPLD, FPGA)

Lecture 22 · ● · mostly "which array is programmable?"

**▶ Explainer videos** (tap to search YouTube):
- [PROM PAL PLA difference](https://www.youtube.com/results?search_query=PROM+PAL+PLA+difference)
- [how an FPGA works LUT CLB](https://www.youtube.com/results?search_query=how+an+FPGA+works+LUT+CLB)

---

## 1. A ROM is a truth table

Topic 11: a decoder makes every minterm, OR gates add up the ones you want. A ROM **is** a decoder + OR gates. So:

**address = the input variables · stored word = the outputs · programming the ROM = filling in the truth table.**

**Slide 5: y = x² + 1 as a lookup table** (3-bit x → 8 words of 6 bits):

| x | A₂A₁A₀ | y | B₅…B₀ |
|---|---|---|---|
| 0 | 000 | 1 | 000001 |
| 1 | 001 | 2 | 000010 |
| 2 | 010 | 5 | 000101 |
| 3 | 011 | 10 | 001010 |
| 4 | 100 | 17 | 010001 |
| 5 | 101 | 26 | 011010 |
| 6 | 110 | 37 | 100101 |
| 7 | 111 | 50 | 110010 |

No multiplier, no adder: just an **8 × 6 ROM**.

> **Apply:** what size ROM implements a full adder (inputs X, Y, Z; outputs S, C)?
<details><summary>Answer</summary>

3 inputs → 8 words. 2 outputs → 2 bits. **8 × 2 ROM.**

</details>

---

## 2. PROM, PAL, PLA ⭐

All three are an **AND array** (makes product terms) feeding an **OR array** (adds them). The only difference is which array you can program.

| Device | AND array | OR array | Notes |
|---|---|---|---|
| **PROM** | **fixed** (a full decoder: all minterms) | **programmable** | |
| **PAL** | **programmable** | **fixed** | easier to program |
| **PLA** | **programmable** | **programmable** | most flexible, hardest to program |

**How to remember:** PRO**M** fixes the **AND** side (**M**interms all made for you). P**A**L programs the **A**ND side only. PLA does both.

PAL and PLA outputs are **sum-of-products** expressions. Gates only → **combinational** logic only.

> **Apply:** which device has a programmable AND array and a fixed OR array?
<details><summary>Answer</summary>

**PAL.**

</details>

---

## 3. Adding flip-flops: CPLD and FPGA

| | CPLD | FPGA |
|---|---|---|
| Made of | several PLDs joined by a programmable **switch matrix** | hundreds to thousands of **configurable logic blocks (CLBs)** |
| Basic unit | **macrocell** = sum-of-products logic + an optional flip-flop (8 to 16 per PLD) | **CLB** = lookup table + muxes + flip-flop |
| Around it | I/O blocks (three-state buffer per pin: input or output) | I/O blocks (IOBs) + programmable interconnect (switch matrices) |
| Use | smaller designs | large designs |

**FPGA details worth a mark:**
- A CLB's **lookup table (LUT)** can be programmed to be **any Boolean function of 4 variables**. Its result goes straight out or into a 1-bit flip-flop.
- A full adder fits in one CLB: one logic block for Sum, one for Carry (each a 3-variable function, so one input is unused).
- Each interconnect point in a **switch matrix** has **6 switches** → 2⁶ = **64** possible connections between the 4 wires meeting there.
- **IOB:** sits between a package pin and the CLBs. Can be input, output or bidirectional.

> **Apply:** a LUT has 4 inputs. How many bits of memory does it need?
<details><summary>Answer</summary>

One bit per truth-table row: 2⁴ = **16 bits**. (A LUT is a tiny 16 × 1 ROM.)

</details>

---

## 4. ASIC or FPGA

| | ASIC | FPGA |
|---|---|---|
| What | chip designed for one job, made in a foundry | bought off the shelf, configured by the designer |
| Design ends with | physical layout | a **bitstream** |
| Good at | **high performance, low power, low cost in high volume** | **low development cost, short time to market, reconfigurable** |

**Traps:** PAL = programmable AND, fixed OR (not the other way round) · PAL and PLA are combinational, CPLD and FPGA add flip-flops · a ROM with k inputs always has all 2ᵏ minterms, used or not.

---

Next: [20 · Asynchronous logic](20-asynchronous-logic.md) · [Final exam practice](../final-exam-practice.md)
