# 01 · History and chips

Lecture 1 · worth a short-answer question at most · [**Quiz →**](https://albinjoby82-ops.github.io/DE_Lock-In/quiz.html?t=01)

Only learn the numbers below. Skip the chip photos.

---

## 1. The timeline

| When | What | Remember |
|---|---|---|
| 1943 | COLOSSUS | first **valve** computer (UK, code-breaking) |
| 1946 | ENIAC | 18,000 valves, 30 tons, 140 kW. **von Neumann** moved the program **inside** the machine |
| 1948 | transistor | Bell Labs: Bardeen, Brattain, Shockley |
| 1971 | Intel 4004 | **2,300** transistors |
| 2017 | Xeon Platinum 8180 | **8 billion** transistors |

Integration scale: **SSI** 10–100 gates · **MSI** 100–1,000 · **LSI** 1,000–10,000.

> **Apply:** a chip has 500 gates. Which scale?
<details><summary>Answer</summary>

**MSI**: 500 is between 100 and 1,000.

</details>

> **Apply:** why did storing the program inside the computer help?
<details><summary>Answer</summary>

Speed was set by the electronics, not by reading the program in. And the machine could make decisions from its own results.

</details>

---

## 2. Moore's law

**Rule:** transistor count **doubles every 18 to 24 months** (Moore's 1965 version: every year).

It came true because the industry used it as a **target**: a self-fulfilling prophecy.

> **Apply:** a chip has 1 million transistors today. Roughly how many in 6 years, doubling every 2 years?
<details><summary>Answer</summary>

6 ÷ 2 = 3 doublings. 1M × 2³ = **8 million**.

</details>

---

## 3. Why the rest of the module simplifies circuits

A chip is a sea of transistors used as switches. Two design goals:

1. **Fewest transistors** → smaller, cheaper.
2. **Shortest propagation delay** → faster.

Every simplification in Topics 6 to 9 serves these two goals.

> **Apply:** name the two goals, and say which one a ripple-carry adder is bad at (Topic 10).
<details><summary>Answer</summary>

Fewest transistors, shortest delay. A ripple-carry adder is cheap but **slow**: the carry has to pass through every stage.

</details>

---

Admin: labs 30%, assignments 30%, exams 40% (mid-term **10%**, final 30%).
