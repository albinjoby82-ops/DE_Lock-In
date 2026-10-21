# DE Lock-In

Digital Electronics mid-term (Lectures 1–10), learnt by **doing**, not reading.

**▶ [Open the quiz site](https://albinjoby82-ops.github.io/DE_Lock-In/)** · [Topic tracker](TOPICS.md) · [Cheat sheet](cheat-sheet.md) · [Book questions + mock mid-term](https://albinjoby82-ops.github.io/DE_Lock-In/#book-questions) · [My questions](my-questions.md)

## How to use it

1. **Read a topic's notes.** Each idea is: one short **rule** → a **diagram** → an **Apply** question. Answer on paper before opening the answer.
2. **Do that topic's quiz.** Click to fill K-maps and truth tables, type expressions, trace circuits. It checks your working (Boolean answers are tested on every row, and must be minimal) and shows why. Done the slide version? Press **New numbers** for a fresh one with the full working.
3. **Mixed drill.** Random questions across topics, like the real exam.
4. **Book questions.** The Mano & Ciletti (4th ed.) end-of-chapter problems, each with a full worked solution, grouped into **skills**. Each skill has 1–4 **core** questions; the rest is optional extra practice. Short on time? Do the topic's **Core path** (110 questions across all topics instead of 375). Groups live in `tools/book_groups.py`.
5. **Mock mid-term.** Random book questions against the clock.
6. Got confused? Add it to [my-questions.md](my-questions.md).

## Notation (same as the slides)

`x'` = NOT x · `xy` = x AND y · `x + y` = x OR y · `x ⊕ y` = XOR · `Σm(…)` sum of minterms · `ΠM(…)` product of maxterms

## Repo map

```
notes/NN-topic.md   the 12 topics (rule → diagram → apply question)
docs/               the quiz site (GitHub Pages): data/NN.js = each topic's questions, gen.js = New numbers versions
docs/svg/           every drawn diagram (built by tools/build_svg.py)
docs/book/NN.js     book questions + worked solutions per topic (built by tools/build_book.py + book_ch1/3/4.py)
docs/book.html      book question lists (?t=06) and the timed mock mid-term (?mock=06,07&n=12&min=50)
docs/svg/book/      book circuits, K-maps and timing diagrams (built by tools/build_book.py)
img/                the few lecture slide crops still used
tools/check.py      re-checks every quiz answer, K-map minimality, every link, and re-works thousands of New numbers answers
```
