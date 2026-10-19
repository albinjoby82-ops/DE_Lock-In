QUIZ.add({
"id": "01", "title": "History and chips",
"intro": "Quick one. Only the numbers and two ideas matter.",
"qs": [
{"type": "mcq", "q": "Which was the first <b>valve</b> computer?", "opts": ["ENIAC", "COLOSSUS", "TX-0", "PDP-8"], "a": 1,
 "why": "COLOSSUS (1943, UK, code-breaking). ENIAC came in 1946. TX-0 was the first <i>transistor</i> computer.", "ref": "01 §1"},
{"type": "text", "q": "How many transistors did the Intel 4004 (1971) have?", "ans": ["2300", "2,300", "2 300"], "ph": "a number",
 "why": "<b>2,300</b> transistors on a 2 × 4 mm die. Compare: Xeon Platinum 8180 (2017) has 8 billion.", "ref": "01 §1"},
{"type": "mcq", "q": "A chip has 5,000 gates. Which integration scale is that?", "opts": ["SSI", "MSI", "LSI"], "a": 2,
 "why": "LSI is 1,000 to 10,000 gates. (SSI 10–100, MSI 100–1,000.)", "ref": "01 §1"},
{"type": "mcq", "q": "What was von Neumann's big change?", "opts": ["He invented the transistor", "He stored the program inside the computer", "He built the first chip", "He predicted the doubling of transistors"], "a": 1,
 "why": "Stored program: speed set by the electronics, and the machine can act on its own results.", "ref": "01 §1"},
{"gen": "moore", "type": "text", "q": "A chip has 2 million transistors. Doubling every 2 years, about how many million will it have after 8 years?", "ans": ["32", "32 million", "32m", "32000000"], "ph": "millions",
 "why": "8 ÷ 2 = 4 doublings. 2 × 2⁴ = <b>32 million</b>.", "ref": "01 §2"},
{"type": "mcq", "q": "Why is Moore's law called a self-fulfilling prophecy?", "opts": ["Physics forces transistors to shrink at that rate", "Chip makers used it as a target, so they made it come true", "Moore controlled Intel's roadmap", "It was proven mathematically"], "a": 1,
 "why": "It began as a forecast. Companies treated it as a goal, fearing rivals would hit it.", "ref": "01 §2"},
{"type": "mcq", "q": "Which pair are the two design goals for a digital IC?", "opts": ["Most gates, highest voltage", "Fewest transistors, shortest propagation delay", "Lowest price, most pins", "Most memory, fewest wires"], "a": 1,
 "why": "Fewest transistors (size, cost) and shortest delay (speed). That's why we simplify circuits.", "ref": "01 §3"},
{"type": "text", "q": "What percentage of the module is the mid-term worth?", "ans": ["10", "10%"], "ph": "%",
 "why": "Mid-term <b>10%</b>, final 30%, labs 30%, assignments 30%."}
]});
