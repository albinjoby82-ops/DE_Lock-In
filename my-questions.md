# My questions (per topic)

The bits that confused me, with the short answer. Re-read this before the exam.

How to add one:

**Q: the question, in my words**

The short answer.

📍 Notes: link to the notes section

---

## Topic 2 — Number systems

**Q: Why do I read the remainders upward but the fraction bits downward?**

Each division by 2 strips off the **rightmost** bit first. So the first remainder is the LSB, and you read up to get the MSB.

Each multiply by 2 pulls out the **leftmost** fraction bit first. So the first one goes right after the point, and you read down.

📍 Notes: [02 §4](notes/02-number-systems.md)

---

## Topic 12 — Mux slide 3

**Q: Slide 3 of Lecture 10 says S = 1 passes I₀. Is that right?**

No. It is a typo.

The 4-to-1 table on the next slide, the function examples and the textbook all use: select 0 → input 0.

So Y = S'I₀ + SI₁.

If an exam question states its own convention, follow that.

📍 Notes: [12 §2](notes/12-multiplexers.md)
