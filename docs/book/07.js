BOOK.add({
"id": "07",
"title": "Minterms and maxterms",
"intro": "Mano Ch 2, canonical forms. Lists: type numbers with commas, smallest first, e.g. 1,3,6.",
"problems": [
{
"n": "2.10",
"text": "Show what F₁ + F₂ and F₁F₂ do to minterms.",
"qs": [
{
"tag": "Mano 2.10 (a)",
"type": "work",
"q": "Show that E = F₁ + F₂ contains the sum of the minterms of F₁ and of F₂.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>F₁ = Σ(minterms of F₁), F₂ = Σ(minterms of F₂)</td><td>any function is the OR of its minterms</td></tr><tr><td>2</td><td>E = F₁ + F₂ = Σ(F₁'s) + Σ(F₂'s)</td><td>OR them</td></tr><tr><td>3</td><td>a minterm in both appears twice: m + m = m</td><td>idempotent law</td></tr><tr><td>4</td><td>E = Σ(every minterm in F₁ or F₂)</td><td>the union of the two lists</td></tr></table><p>Example: F₁ = Σ(1, 3), F₂ = Σ(3, 6) → E = Σ(1, 3, 6).</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.10 (b)",
"type": "work",
"q": "Show that G = F₁F₂ contains only the minterms common to F₁ and F₂.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>G = (Σ mᵢ)(Σ mⱼ) = Σ mᵢmⱼ</td><td>multiply out every pair</td></tr><tr><td>2</td><td>i ≠ j: mᵢmⱼ = 0</td><td>two different minterms differ in some letter, so they contain x·x' = 0</td></tr><tr><td>3</td><td>i = j: mᵢmᵢ = mᵢ</td><td>x·x = x</td></tr><tr><td>4</td><td>G = Σ(minterms in both lists)</td><td>only the common ones survive</td></tr></table><p>Example: F₁ = Σ(1, 3), F₂ = Σ(3, 6) → G = Σ(3).</p>",
"ref": "07 §3"
}
]
},
{
"n": "2.16",
"text": "The OR of all minterms of n variables is 1.",
"qs": [
{
"tag": "Mano 2.16 (a)",
"type": "work",
"q": "Prove that the sum of all minterms of a 3-variable function is 1.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>x'y'z' + x'y'z + x'yz' + x'yz + xy'z' + xy'z + xyz' + xyz</td><td>all 8 minterms</td></tr><tr><td>2</td><td>x'y'(z' + z) + x'y(z' + z) + xy'(z' + z) + xy(z' + z)</td><td>pair them up on z</td></tr><tr><td>3</td><td>x'y' + x'y + xy' + xy</td><td>z' + z = 1</td></tr><tr><td>4</td><td>x'(y' + y) + x(y' + y) = x' + x</td><td>pair again on y</td></tr><tr><td>5</td><td><b>1</b></td><td>x' + x = 1</td></tr></table>",
"ref": "07 §3"
},
{
"tag": "Mano 2.16 (b)",
"type": "work",
"q": "Suggest a procedure for a general proof (n variables).",
"why": "<p><b>Induction.</b> Pair every minterm with the one that differs only in the last variable xₙ. Each pair is P·xₙ' + P·xₙ = P, so the 2ⁿ minterms of n variables collapse to the 2ⁿ⁻¹ minterms of n − 1 variables. Repeat until one variable is left: x₁' + x₁ = <b>1</b>.</p><p>Or the 'truth table' argument: every row of the table makes exactly one minterm equal 1, so the OR is 1 on every row.</p>",
"ref": "07 §3"
}
]
},
{
"n": "2.17",
"text": "Truth table, sum of minterms and product of maxterms.",
"qs": [
{
"tag": "Mano 2.17 (a) ★",
"type": "tt",
"q": "Fill the truth table for <code>(xy + z)(y + xz)</code>.",
"vars": "xyz",
"outs": {
"F": [
0,
0,
0,
1,
0,
1,
1,
1
]
},
"why": "<p>Easiest row by row: put each xyz into both brackets, F = 1 only if both brackets are 1.</p><p>F = 1 on rows <b>3, 5, 6, 7</b>.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.17 (a) ★",
"type": "multi",
"q": "Now write <code>(xy + z)(y + xz)</code> as a sum of minterms and a product of maxterms. Type just the numbers, smallest first, e.g. 1,3,6.",
"fields": [
{
"label": "Σm(",
"ans": [
"3,5,6,7",
"(3,5,6,7)",
"Σ(3,5,6,7)",
"Σm(3,5,6,7)",
"m(3,5,6,7)",
"Π(3,5,6,7)",
"ΠM(3,5,6,7)",
"M(3,5,6,7)"
]
},
{
"label": "ΠM(",
"ans": [
"0,1,2,4",
"(0,1,2,4)",
"Σ(0,1,2,4)",
"Σm(0,1,2,4)",
"m(0,1,2,4)",
"Π(0,1,2,4)",
"ΠM(0,1,2,4)",
"M(0,1,2,4)"
]
}
],
"why": "<p><b>Σm(3, 5, 6, 7)</b>: the rows where F = 1.</p><p><b>ΠM(0, 1, 2, 4)</b>: every other row.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.17 (b)",
"type": "tt",
"q": "Fill the truth table for <code>(x + y')(y' + z)</code>.",
"vars": "xyz",
"outs": {
"F": [
1,
1,
0,
0,
1,
1,
0,
1
]
},
"why": "<p>Simplify first: (x + y')(y' + z) = y' + xz. So F = 1 whenever y = 0, plus row 111.</p><p>F = 1 on rows <b>0, 1, 4, 5, 7</b>.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.17 (b)",
"type": "multi",
"q": "Now write <code>(x + y')(y' + z)</code> as a sum of minterms and a product of maxterms. Type just the numbers, smallest first, e.g. 1,3,6.",
"fields": [
{
"label": "Σm(",
"ans": [
"0,1,4,5,7",
"(0,1,4,5,7)",
"Σ(0,1,4,5,7)",
"Σm(0,1,4,5,7)",
"m(0,1,4,5,7)",
"Π(0,1,4,5,7)",
"ΠM(0,1,4,5,7)",
"M(0,1,4,5,7)"
]
},
{
"label": "ΠM(",
"ans": [
"2,3,6",
"(2,3,6)",
"Σ(2,3,6)",
"Σm(2,3,6)",
"m(2,3,6)",
"Π(2,3,6)",
"ΠM(2,3,6)",
"M(2,3,6)"
]
}
],
"why": "<p><b>Σm(0, 1, 4, 5, 7)</b>: the rows where F = 1.</p><p><b>ΠM(2, 3, 6)</b>: every other row.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.17 (c)",
"type": "tt",
"q": "Fill the truth table for <code>x'z + wx'y + wyz' + w'y'</code>.",
"vars": "wxyz",
"outs": {
"F": [
1,
1,
0,
1,
1,
1,
0,
0,
0,
1,
1,
1,
0,
0,
1,
0
]
},
"why": "<p>Find each term's rows: x'z → 1, 3, 9, 11 · wx'y → 10, 11 · wyz' → 10, 14 · w'y' → 0, 1, 4, 5. Then merge the lists.</p><p>F = 1 on rows <b>0, 1, 3, 4, 5, 9, 10, 11, 14</b>.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.17 (c)",
"type": "multi",
"q": "Now write <code>x'z + wx'y + wyz' + w'y'</code> as a sum of minterms and a product of maxterms. Type just the numbers, smallest first, e.g. 1,3,6.",
"fields": [
{
"label": "Σm(",
"ans": [
"0,1,3,4,5,9,10,11,14",
"(0,1,3,4,5,9,10,11,14)",
"Σ(0,1,3,4,5,9,10,11,14)",
"Σm(0,1,3,4,5,9,10,11,14)",
"m(0,1,3,4,5,9,10,11,14)",
"Π(0,1,3,4,5,9,10,11,14)",
"ΠM(0,1,3,4,5,9,10,11,14)",
"M(0,1,3,4,5,9,10,11,14)"
]
},
{
"label": "ΠM(",
"ans": [
"2,6,7,8,12,13,15",
"(2,6,7,8,12,13,15)",
"Σ(2,6,7,8,12,13,15)",
"Σm(2,6,7,8,12,13,15)",
"m(2,6,7,8,12,13,15)",
"Π(2,6,7,8,12,13,15)",
"ΠM(2,6,7,8,12,13,15)",
"M(2,6,7,8,12,13,15)"
]
}
],
"why": "<p><b>Σm(0, 1, 3, 4, 5, 9, 10, 11, 14)</b>: the rows where F = 1.</p><p><b>ΠM(2, 6, 7, 8, 12, 13, 15)</b>: every other row.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.17 (d)",
"type": "tt",
"q": "Fill the truth table for <code>(xy + yz' + x'z)(x + z)</code>.",
"vars": "xyz",
"outs": {
"F": [
0,
1,
0,
1,
0,
0,
1,
1
]
},
"why": "<p>Row by row. F needs (x + z) = 1, so rows 000 and 010 are 0 straight away.</p><p>F = 1 on rows <b>1, 3, 6, 7</b>.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.17 (d)",
"type": "multi",
"q": "Now write <code>(xy + yz' + x'z)(x + z)</code> as a sum of minterms and a product of maxterms. Type just the numbers, smallest first, e.g. 1,3,6.",
"fields": [
{
"label": "Σm(",
"ans": [
"1,3,6,7",
"(1,3,6,7)",
"Σ(1,3,6,7)",
"Σm(1,3,6,7)",
"m(1,3,6,7)",
"Π(1,3,6,7)",
"ΠM(1,3,6,7)",
"M(1,3,6,7)"
]
},
{
"label": "ΠM(",
"ans": [
"0,2,4,5",
"(0,2,4,5)",
"Σ(0,2,4,5)",
"Σm(0,2,4,5)",
"m(0,2,4,5)",
"Π(0,2,4,5)",
"ΠM(0,2,4,5)",
"M(0,2,4,5)"
]
}
],
"why": "<p><b>Σm(1, 3, 6, 7)</b>: the rows where F = 1.</p><p><b>ΠM(0, 2, 4, 5)</b>: every other row.</p>",
"ref": "07 §3"
}
]
},
{
"n": "2.19",
"text": "F(A, B, C, D) = B'D + A'D + BD as Σm and ΠM.",
"qs": [
{
"tag": "Mano 2.19 ★",
"type": "multi",
"q": "<code>F(A, B, C, D) = B'D + A'D + BD</code>. Write it as a sum of minterms and a product of maxterms.",
"fields": [
{
"label": "Σm(",
"ans": [
"1,3,5,7,9,11,13,15",
"(1,3,5,7,9,11,13,15)",
"Σ(1,3,5,7,9,11,13,15)",
"Σm(1,3,5,7,9,11,13,15)",
"m(1,3,5,7,9,11,13,15)",
"Π(1,3,5,7,9,11,13,15)",
"ΠM(1,3,5,7,9,11,13,15)",
"M(1,3,5,7,9,11,13,15)"
]
},
{
"label": "ΠM(",
"ans": [
"0,2,4,6,8,10,12,14",
"(0,2,4,6,8,10,12,14)",
"Σ(0,2,4,6,8,10,12,14)",
"Σm(0,2,4,6,8,10,12,14)",
"m(0,2,4,6,8,10,12,14)",
"Π(0,2,4,6,8,10,12,14)",
"ΠM(0,2,4,6,8,10,12,14)",
"M(0,2,4,6,8,10,12,14)"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>B'D + BD = D</td><td>factor D: B' + B = 1</td></tr><tr><td>2</td><td>D + A'D = D</td><td>absorption</td></tr><tr><td>3</td><td>F = D</td><td>so F = 1 on every odd row</td></tr></table><p><b>Σm(1, 3, 5, 7, 9, 11, 13, 15)</b> and <b>ΠM(0, 2, 4, 6, 8, 10, 12, 14)</b>.</p>",
"ref": "07 §3"
}
]
},
{
"n": "2.20",
"text": "Express the complement in sum-of-minterms form.",
"qs": [
{
"tag": "Mano 2.20 (a)",
"type": "multi",
"q": "<code>F(A, B, C, D) = Σ(3, 5, 9, 11, 15)</code>. Write <b>F'</b> as a sum of minterms.",
"fields": [
{
"label": "F' = Σm(",
"ans": [
"0,1,2,4,6,7,8,10,12,13,14",
"(0,1,2,4,6,7,8,10,12,13,14)",
"Σ(0,1,2,4,6,7,8,10,12,13,14)",
"Σm(0,1,2,4,6,7,8,10,12,13,14)",
"m(0,1,2,4,6,7,8,10,12,13,14)",
"Π(0,1,2,4,6,7,8,10,12,13,14)",
"ΠM(0,1,2,4,6,7,8,10,12,13,14)",
"M(0,1,2,4,6,7,8,10,12,13,14)"
]
}
],
"why": "<p>F' is 1 exactly where F is 0: every number 0–15 <i>not</i> in F's list. <b>F' = Σm(0, 1, 2, 4, 6, 7, 8, 10, 12, 13, 14)</b>.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.20 (b)",
"type": "multi",
"q": "<code>F(x, y, z) = Π(2, 4, 5, 7)</code>. Write <b>F'</b> as a sum of minterms.",
"fields": [
{
"label": "F' = Σm(",
"ans": [
"2,4,5,7",
"(2,4,5,7)",
"Σ(2,4,5,7)",
"Σm(2,4,5,7)",
"m(2,4,5,7)",
"Π(2,4,5,7)",
"ΠM(2,4,5,7)",
"M(2,4,5,7)"
]
}
],
"why": "<p>F = Π(2, 4, 5, 7) means F is <b>0</b> on rows 2, 4, 5, 7. F' is 1 on those rows.</p><p><b>F' = Σm(2, 4, 5, 7)</b>: the same numbers, just switch Π → Σ.</p>",
"ref": "07 §3"
}
]
},
{
"n": "2.21",
"text": "Convert to the other canonical form.",
"qs": [
{
"tag": "Mano 2.21 (a)",
"type": "multi",
"q": "<code>F(x, y, z) = Σ(2, 5, 6)</code>. Write F as a product of maxterms.",
"fields": [
{
"label": "ΠM(",
"ans": [
"0,1,3,4,7",
"(0,1,3,4,7)",
"Σ(0,1,3,4,7)",
"Σm(0,1,3,4,7)",
"m(0,1,3,4,7)",
"Π(0,1,3,4,7)",
"ΠM(0,1,3,4,7)",
"M(0,1,3,4,7)"
]
}
],
"why": "<p>Swap the symbol and list the missing numbers from 0–7: <b>ΠM(0, 1, 3, 4, 7)</b>.</p>",
"ref": "07 §3"
},
{
"tag": "Mano 2.21 (b)",
"type": "multi",
"q": "<code>F(A, B, C, D) = Π(0, 1, 2, 4, 7, 9, 12)</code>. Write F as a sum of minterms.",
"fields": [
{
"label": "Σm(",
"ans": [
"3,5,6,8,10,11,13,14,15",
"(3,5,6,8,10,11,13,14,15)",
"Σ(3,5,6,8,10,11,13,14,15)",
"Σm(3,5,6,8,10,11,13,14,15)",
"m(3,5,6,8,10,11,13,14,15)",
"Π(3,5,6,8,10,11,13,14,15)",
"ΠM(3,5,6,8,10,11,13,14,15)",
"M(3,5,6,8,10,11,13,14,15)"
]
}
],
"why": "<p>Missing from 0–15: <b>Σm(3, 5, 6, 8, 10, 11, 13, 14, 15)</b>.</p>",
"ref": "07 §3"
}
]
},
{
"n": "2.22",
"text": "Convert into sum of products and product of sums.",
"qs": [
{
"tag": "Mano 2.22 (a · SOP) ★",
"type": "bool",
"q": "Write <code>(AB + C)(B + C'D)</code> as a <b>sum of products</b> (simplest).",
"vars": "ABCD",
"ones": [
6,
7,
12,
13,
14,
15
],
"show": "AB + BC",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>AB·B + AB·C'D + C·B + C·C'D</td><td>multiply out</td></tr><tr><td>2</td><td>AB + ABC'D + BC + 0</td><td>BB = B, CC' = 0</td></tr><tr><td>3</td><td><b>AB + BC</b></td><td>ABC'D is absorbed by AB</td></tr></table>",
"lits": 4,
"form": "sop",
"ref": "07 §1"
},
{
"tag": "Mano 2.22 (a · POS) ★",
"type": "bool",
"q": "Write <code>(AB + C)(B + C'D)</code> as a <b>product of sums</b> (simplest).",
"vars": "ABCD",
"ones": [
6,
7,
12,
13,
14,
15
],
"show": "B(A + C)",
"why": "<p>From the SOP: AB + BC = <b>B(A + C)</b>. Each bracket (B and A + C) is a sum, so this is POS.</p>",
"lits": 3,
"form": "pos",
"ref": "07 §1"
},
{
"tag": "Mano 2.22 (b · SOP) ★",
"type": "bool",
"q": "Write <code>x' + x(x + y')(y + z')</code> as a <b>sum of products</b> (simplest).",
"vars": "xyz",
"ones": [
0,
1,
2,
3,
4,
6,
7
],
"show": "x' + y + z'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>x' + x(y + z')</td><td>x(x + y') = x (absorption)</td></tr><tr><td>2</td><td><b>x' + y + z'</b></td><td>x' + xP = x' + P</td></tr></table>",
"lits": 3,
"form": "sop",
"ref": "07 §1"
},
{
"tag": "Mano 2.22 (b · POS) ★",
"type": "bool",
"q": "Write <code>x' + x(x + y')(y + z')</code> as a <b>product of sums</b>.",
"vars": "xyz",
"ones": [
0,
1,
2,
3,
4,
6,
7
],
"show": "(x' + y + z')",
"why": "<p>x' + y + z' is a single sum term, so it is <b>already a POS</b> (a product with one factor). It's SOP and POS at once.</p>",
"lits": 3,
"form": "pos",
"ref": "07 §1"
}
]
}
]
});
