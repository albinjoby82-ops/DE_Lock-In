# Final exam: what to know and how to study it

**▶ Cram site: https://albinjoby82-ops.github.io/DE_Lock-In/final/** (exam path, worked 23/24 paper, 2 mocks)

## Updated after the 23/24 past paper

The real paper had **4 questions, 30 minutes each**, and it changes the priorities below:

| Q | Asked | Weight |
|---|---|---|
| 1 | circuit → function, truth table, K-map, Σm / ΠM, two-level NAND | 25% |
| 2a | 3-bit ripple count-down counter with D flip-flops, waveforms, frequency divider | 15% |
| 2b | static hazards, hazard-free circuit | 10% |
| 3 | synchronous JK state machine with two count loops | 25% |
| 4 | asynchronous circuit: transition table, flow table, stability | 25% |

**So the must-know list is now:** K-maps and NAND (mid-term Topics 7–9), flip-flops (13), ripple and synchronous counters (16), hazards and asynchronous circuits (20).

**Not on that paper** but hinted for this year: multiplexers (12) and sequence detectors (15). Do them second.

One paper is thin evidence. The lecturer's hint (5 questions, 1 combinational, rest sequential) may still be right for this year.

---

*The section below was written before the past paper turned up.*

Final = Lectures 11–25 (Topics 13–21). Expected shape (from the lecturer in class, not confirmed in writing): **5 questions: 1 combinational (probably multiplexers), 4 sequential.** Check this against a past paper if you can get one.

## What you actually need to know

**Must know (these are the 5 questions)**

| Topic | The skill |
|---|---|
| [12 Multiplexers](notes/12-multiplexers.md) | the one combinational question: implement a function on a smaller mux using 0, 1, D, D' |
| [13 Latches and flip-flops](notes/13-latches-flip-flops.md) | JK, D, T characteristic and excitation tables |
| [14 Analysing a circuit](notes/14-sequential-analysis.md) | circuit → state table → state diagram |
| [15 Designing a circuit](notes/15-sequential-design.md) | sequence detectors (Mealy and Moore), the 5-step method |
| [16 Counters](notes/16-counters.md) | design a mod-N counter, check the unused states |

**Probably a question or part of one**

| Topic | The skill |
|---|---|
| [17 Registers](notes/17-registers.md) | shift register, Johnson counter, universal shift register |
| [20 Asynchronous logic](notes/20-asynchronous-logic.md) | critical race, static hazard and its fix |

**Skim only (a short question at most)**

| Topic | The skill |
|---|---|
| [18 Memory](notes/18-memory.md) | address lines and sizes, SRAM vs DRAM |
| [19 Programmable logic](notes/19-programmable-logic.md) | PAL vs PLA |
| [21 Transistor logic](notes/21-transistor-logic.md) | CMOS NAND and NOR wiring |

**Old topics still used:** minterms ([7](notes/07-minterms-maxterms.md)), K-maps ([8](notes/08-karnaugh-maps.md)) and don't cares ([9](notes/09-dont-cares-nand-nor.md)). Every design question ends in K-maps with x's.

**Skip for the final:** Topics 1–6, 10, 11 (background only).

## How to study (Lock-In, backwards)

For each topic:

1. Try the practice question **cold**, even if you get nowhere.
2. Open the matching notes section and read it next to your attempt.
3. Close everything and redo it from a blank page.
4. Redo it once more with changed details (detect 110 instead of 101, mod-6 instead of mod-5).

Step 4 shows whether you understand it or just remember the answer.

**Rules**
- Write by hand. State tables and K-maps are a drawing skill, not a reading skill.
- Mark yourself harshly. A guessed step = wrong, redo it.
- Log the traps that catch you in [my-questions.md](my-questions.md) and re-read them the night before.
- Short on time? Skip everything else and do the two papers in [final-exam-practice.md](final-exam-practice.md) twice.

## Plan (adjust to your number of days)

| When | Do |
|---|---|
| Day 1 | Topic 13, then 14. Write the excitation table out 5 times from memory. Do the Topic 14 drill. |
| Day 2 | Topic 15 (hardest). All three detector drills. |
| Day 3 | Topic 16, then **Paper 1** under time pressure. |
| Day 4 | Topics 12, 17, 20, then **Paper 2**. |
| Last evening | Topics 18, 19, 21 (about 20 minutes), the short-question bank, the [cheat sheet](cheat-sheet.md). Nothing new. |

Links: [topic tracker](TOPICS.md) · [practice papers](final-exam-practice.md) · [cheat sheet](cheat-sheet.md)
