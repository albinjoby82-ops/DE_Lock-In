# 18 · Memory (RAM and ROM)

Lecture 21 · ● · facts and sizes, no design

**▶ Explainer videos** (tap to search YouTube):
- [how RAM works memory cell decoder](https://www.youtube.com/results?search_query=how+RAM+works+memory+cell+decoder)
- [SRAM vs DRAM](https://www.youtube.com/results?search_query=SRAM+vs+DRAM)
- [ROM PROM EPROM EEPROM flash](https://www.youtube.com/results?search_query=ROM+PROM+EPROM+EEPROM+flash)

---

## 1. Sizes ⭐ (the part with numbers)

Memory stores **words**. A memory is described as **words × bits per word**.

**k address lines select one of 2ᵏ words.**

| Memory | Words | Address lines | Data lines |
|---|---|---|---|
| 1024 × 16 | 1024 = 2¹⁰ | **10** | 16 |
| 32 × 8 | 32 = 2⁵ | **5** | 8 |
| 4 × 3 | 4 = 2² | **2** | 3 |

1 kB = 2¹⁰ bytes · 1 MB = 2²⁰ · 1 GB = 2³⁰ · 1 byte = 8 bits.

> **Apply:** a 64K × 8 memory. Address lines? Total bits?
<details><summary>Answer</summary>

64K = 2⁶ × 2¹⁰ = 2¹⁶ → **16 address lines**. Bits = 2¹⁶ × 8 = **524,288**.

</details>

> **Apply:** a memory has 12 address lines and 8 data lines. Size?
<details><summary>Answer</summary>

2¹² = 4096 words × 8 bits = **4K × 8** (4 kB).

</details>

---

## 2. RAM: read and write

**Random access memory:** any word can be read or written, in any order.

| Signal | Job |
|---|---|
| Address | which word |
| Data in / data out | the word |
| Read/Write | **1 = read, 0 = write** |
| Memory enable (select) | 0 = chip does nothing |

**One binary cell** stores one bit: a latch plus gates. Select = 0 → the cell holds and outputs 0. Select = 1 → Read/Write decides whether the bit comes out (read) or the input is stored (write).

**A 4 × 3 RAM** = 12 cells in 4 rows + a **2-to-4 decoder**. The decoder turns the address into one active row (word). On a read, each column's cells are ORed onto that output line.

**Two-dimensional (coincident) decoding** for big memories: split the address in half, one decoder for rows and one for columns.

| 1K words (10 address bits) | AND gates |
|---|---|
| one 10 × 1024 decoder | 1024 gates, 10 inputs each |
| two 5 × 32 decoders | **64 gates**, 5 inputs each |

> **Apply:** why split the decoder?
<details><summary>Answer</summary>

Far fewer and smaller gates: 2 × 32 = 64 five-input gates do the job of 1024 ten-input gates.

</details>

---

## 3. SRAM and DRAM

| | SRAM (static) | DRAM (dynamic) |
|---|---|---|
| Cell | latch, **6 transistors** | **1 transistor + 1 capacitor** |
| Bit stored as | latch state | charge on the capacitor |
| Size | bigger | about **¼** the area → higher density |
| Refresh | no | **yes**: charge leaks, must be topped up |

**Both are volatile:** power off → data gone.

---

## 4. ROM and non-volatile memory

**Non-volatile** = keeps its data with the power off (ROM, flash, magnetic disk).

**ROM: k inputs (address), n outputs (data), no data input, no write.**
Inside: a **k-to-2ᵏ decoder** + **n OR gates**. Each decoder output is one word. A connection (fuse left intact) between a word line and an OR gate puts a 1 in that bit.

**32 × 8 ROM:** 5 address lines, a 5 × 32 decoder, 8 OR gates with 32 inputs each → 32 × 8 = 256 programmable links.

| Type | Programmed | Erased |
|---|---|---|
| Mask ROM | at the factory | never |
| **PROM** | once, by the user, blowing fuses with a high-voltage pulse | never |
| **EPROM** | by the user | **ultraviolet light** |
| **EEPROM** | by the user | **electrically** |
| **Flash** | in-circuit, no special programmer | electrically |

**Flash cell:** a **floating-gate** transistor. Electrons trapped on the insulated floating gate stay for years and shift the transistor's threshold voltage. Reading = checking whether it conducts.

| | NOR flash | NAND flash |
|---|---|---|
| Cells connected | each one straight to the bit line and ground (parallel) | several **in series** |

> **Apply:** a ROM has 8 address inputs and 4 outputs. Decoder size? OR gates? Total bits?
<details><summary>Answer</summary>

**8-to-256** decoder, **4** OR gates, 256 × 4 = **1024 bits**.

</details>

> **Apply:** one difference between EPROM and EEPROM.
<details><summary>Answer</summary>

EPROM is erased with **UV light**, EEPROM with an **electrical signal**.

</details>

**Traps:** address lines = log₂(words), not log₂(bits) · SRAM and DRAM are both volatile · DRAM needs refresh, SRAM does not · a ROM is a decoder + OR gates, so it is combinational.

---

Next: [19 · Programmable logic](19-programmable-logic.md) · [Final exam practice](../final-exam-practice.md)
