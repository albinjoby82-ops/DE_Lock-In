# DE Lock-In — Digital Electronics: from Gate to System

Start at **[TOPICS.md](TOPICS.md)** (progress tracker). Cheat sheet: **[cheat-sheet.md](cheat-sheet.md)**. Confusing bits I asked about: **[my-questions.md](my-questions.md)**.

Covers the **mid-term**: Lectures 1 to 10 (Dr. Ruijia Liu).

## Reading style (dyslexia-friendly)
- One idea per line. Short sentences.
- Big rules and equations on their own line.
- Lots of space between sections.
- Few brackets, little italics, no long bullet points.

## Notation (same as the slides)
| Write | Means | Say |
|---|---|---|
| x' | NOT x (a bar over x on the slides) | "x bar" or "not x" |
| xy or x·y | x AND y | "x and y" |
| x + y | x OR y | "x or y" |
| x ⊕ y | x XOR y | "x xor y" |
| Σm(…) | sum of minterms | "sum of m" |
| ΠM(…) | product of maxterms | "product of M" |

## How each topic is built
- `notes/NN-topic.md`: slide diagrams + short explanation, with **🧠 check questions inline** (answer before opening).
- `questions/NN-topic.md`: end-of-topic test with
  1. the **slide exercises** ("Try now" and "Exercises" slides), and
  2. **midterm-style questions in other formats** (true/false, MCQ, explain, calculation, design), because the midterm won't just copy the slides.
- **Every new rule or method gets a 📐 box:** what each symbol means, *why* it works, **"use it when…"**, and when it does NOT apply.
- **Rule:** every answer and method used in the questions is taught in that topic's notes (or an earlier one), and the answer cites the notes section (§). Nothing appears in an answer that isn't in the notes.
- Every worked answer in this repo was checked against a full truth table.
