BOOK.add({
"id": "09",
"title": "Don't cares, NAND and NOR",
"intro": "Mano 3.15–3.25. Don't cares: use an x only when it makes a block bigger. NAND/NOR drawings are self-marked.",
"problems": [
{
"n": "3.15",
"text": "Simplify with don't-care conditions, then give the result as Σm.",
"qs": [
{
"tag": "Mano 3.15 (a)",
"type": "bool",
"q": "Simplify with don't cares: <code>F(x, y, z) = Σ(2, 3, 4, 6, 7)</code>, <code>d = Σ(0, 1, 5)</code>",
"vars": "xyz",
"ones": [
2,
3,
4,
6,
7
],
"show": "1",
"lits": 0,
"why": "<p>F = 1 on cells 2, 3, 4, 6, 7, don't care on 0, 1, 5.</p><img src='svg/book/k3-15a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>1</b> from cells 0, 1, 2, 3, 4, 5, 6, 7</li></ul><p><b>F = 1</b> (0 literals).</p>",
"ref": "09 §1",
"dc": [
0,
1,
5
],
"grp": 0,
"core": false
},
{
"tag": "Mano 3.15 (a · Σ)",
"type": "multi",
"q": "Now write your simplified F from 3.15 (a) as a sum of minterms (it includes the don't cares you used).",
"fields": [
{
"label": "Σm(",
"ans": [
"0,1,2,3,4,5,6,7",
"(0,1,2,3,4,5,6,7)",
"Σ(0,1,2,3,4,5,6,7)",
"Σm(0,1,2,3,4,5,6,7)",
"m(0,1,2,3,4,5,6,7)",
"Π(0,1,2,3,4,5,6,7)",
"ΠM(0,1,2,3,4,5,6,7)",
"M(0,1,2,3,4,5,6,7)"
]
}
],
"why": "<p>F = 1 is 1 on cells <b>0, 1, 2, 3, 4, 5, 6, 7</b>: the original 1s plus the x's that ended up inside a group.</p>",
"ref": "09 §1",
"grp": 0,
"core": false
},
{
"tag": "Mano 3.15 (b) ★",
"type": "bool",
"q": "Simplify with don't cares: <code>F(A, B, C, D) = Σ(0, 6, 8, 13, 14)</code>, <code>d = Σ(2, 4, 10)</code>",
"vars": "ABCD",
"ones": [
0,
6,
8,
13,
14
],
"show": "CD' + B'D' + ABC'D",
"lits": 8,
"why": "<p>F = 1 on cells 0, 6, 8, 13, 14, don't care on 2, 4, 10.</p><img src='svg/book/k3-15b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>ABC'D</b> from cells 13</li><li><b>CD'</b> from cells 2, 6, 10, 14</li></ul><p><b>F = CD' + B'D' + ABC'D</b> (8 literals).</p>",
"ref": "09 §1",
"dc": [
2,
4,
10
],
"form": "sop",
"grp": 0,
"core": true,
"corder": 1
},
{
"tag": "Mano 3.15 (b · Σ) ★",
"type": "multi",
"q": "Now write your simplified F from 3.15 (b) as a sum of minterms (it includes the don't cares you used).",
"fields": [
{
"label": "Σm(",
"ans": [
"0,2,6,8,10,13,14",
"(0,2,6,8,10,13,14)",
"Σ(0,2,6,8,10,13,14)",
"Σm(0,2,6,8,10,13,14)",
"m(0,2,6,8,10,13,14)",
"Π(0,2,6,8,10,13,14)",
"ΠM(0,2,6,8,10,13,14)",
"M(0,2,6,8,10,13,14)"
]
}
],
"why": "<p>F = CD' + B'D' + ABC'D is 1 on cells <b>0, 2, 6, 8, 10, 13, 14</b>: the original 1s plus the x's that ended up inside a group.</p>",
"ref": "09 §1",
"grp": 0,
"core": true,
"corder": 2
},
{
"tag": "Mano 3.15 (c)",
"type": "bool",
"q": "Simplify with don't cares: <code>F(A, B, C, D) = Σ(4, 5, 7, 12, 13, 14)</code>, <code>d = Σ(1, 9, 11, 15)</code>",
"vars": "ABCD",
"ones": [
4,
5,
7,
12,
13,
14
],
"show": "AB + BD + BC'",
"lits": 6,
"why": "<p>F = 1 on cells 4, 5, 7, 12, 13, 14, don't care on 1, 9, 11, 15.</p><img src='svg/book/k3-15c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>BC'</b> from cells 4, 5, 12, 13</li><li><b>BD</b> from cells 5, 7, 13, 15</li><li><b>AB</b> from cells 12, 13, 14, 15</li></ul><p><b>F = AB + BD + BC'</b> (6 literals).</p>",
"ref": "09 §1",
"dc": [
1,
9,
11,
15
],
"form": "sop",
"grp": 0,
"core": false
},
{
"tag": "Mano 3.15 (c · Σ)",
"type": "multi",
"q": "Now write your simplified F from 3.15 (c) as a sum of minterms (it includes the don't cares you used).",
"fields": [
{
"label": "Σm(",
"ans": [
"4,5,7,12,13,14,15",
"(4,5,7,12,13,14,15)",
"Σ(4,5,7,12,13,14,15)",
"Σm(4,5,7,12,13,14,15)",
"m(4,5,7,12,13,14,15)",
"Π(4,5,7,12,13,14,15)",
"ΠM(4,5,7,12,13,14,15)",
"M(4,5,7,12,13,14,15)"
]
}
],
"why": "<p>F = AB + BD + BC' is 1 on cells <b>4, 5, 7, 12, 13, 14, 15</b>: the original 1s plus the x's that ended up inside a group.</p>",
"ref": "09 §1",
"grp": 0,
"core": false
},
{
"tag": "Mano 3.15 (d)",
"type": "bool",
"q": "Simplify with don't cares: <code>F(A, B, C, D) = Σ(1, 3, 8, 10, 15)</code>, <code>d = Σ(0, 2, 9)</code>",
"vars": "ABCD",
"ones": [
1,
3,
8,
10,
15
],
"show": "B'D' + A'B' + ABCD",
"lits": 8,
"why": "<p>F = 1 on cells 1, 3, 8, 10, 15, don't care on 0, 2, 9.</p><img src='svg/book/k3-15d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>A'B'</b> from cells 0, 1, 2, 3</li><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>ABCD</b> from cells 15</li></ul><p><b>F = B'D' + A'B' + ABCD</b> (8 literals).</p>",
"ref": "09 §1",
"dc": [
0,
2,
9
],
"form": "sop",
"grp": 0,
"core": false
},
{
"tag": "Mano 3.15 (d · Σ)",
"type": "multi",
"q": "Now write your simplified F from 3.15 (d) as a sum of minterms (it includes the don't cares you used).",
"fields": [
{
"label": "Σm(",
"ans": [
"0,1,2,3,8,10,15",
"(0,1,2,3,8,10,15)",
"Σ(0,1,2,3,8,10,15)",
"Σm(0,1,2,3,8,10,15)",
"m(0,1,2,3,8,10,15)",
"Π(0,1,2,3,8,10,15)",
"ΠM(0,1,2,3,8,10,15)",
"M(0,1,2,3,8,10,15)"
]
}
],
"why": "<p>F = B'D' + A'B' + ABCD is 1 on cells <b>0, 1, 2, 3, 8, 10, 15</b>: the original 1s plus the x's that ended up inside a group.</p>",
"ref": "09 §1",
"grp": 0,
"core": false
}
]
},
{
"n": "3.16",
"text": "Simplify, then implement with two-level NAND circuits.",
"qs": [
{
"tag": "Mano 3.16 (a)",
"type": "bool",
"q": "Simplify <code>F = A'B'C + AC' + ACD + ACD' + A'B'D'</code> (minimal SOP).",
"vars": "ABCD",
"ones": [
0,
2,
3,
8,
9,
10,
11,
12,
13,
14,
15
],
"show": "A + B'C + B'D'",
"lits": 5,
"why": "<p>Plot it: 1s on cells <b>0, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15</b>.</p><img src='svg/book/k3-16a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>B'C</b> from cells 2, 3, 10, 11</li><li><b>A</b> from cells 8, 9, 10, 11, 12, 13, 14, 15</li></ul><p><b>F = A + B'C + B'D'</b> (5 literals).</p>",
"ref": "09 §4",
"form": "sop",
"grp": 1,
"core": false
},
{
"tag": "Mano 3.16 (a · NAND)",
"type": "work",
"q": "Implement <code>F = A + B'C + B'D'</code> with a two-level NAND circuit.",
"why": "<img src='svg/book/n3-16a.svg' alt=''><p>Recipe: every AND → NAND, the OR → NAND. A term that is a single letter goes straight into the output NAND <b>complemented</b>.</p>",
"ref": "09 §4",
"grp": 1,
"core": false
},
{
"tag": "Mano 3.16 (b)",
"type": "bool",
"q": "Simplify <code>F = AB + A'BC + A'B'C'D</code> (minimal SOP).",
"vars": "ABCD",
"ones": [
1,
6,
7,
12,
13,
14,
15
],
"show": "AB + BC + A'B'C'D",
"lits": 8,
"why": "<p>Plot it: 1s on cells <b>1, 6, 7, 12, 13, 14, 15</b>.</p><img src='svg/book/k3-16b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'B'C'D</b> from cells 1</li><li><b>BC</b> from cells 6, 7, 14, 15</li><li><b>AB</b> from cells 12, 13, 14, 15</li></ul><p><b>F = AB + BC + A'B'C'D</b> (8 literals).</p>",
"ref": "09 §4",
"form": "sop",
"grp": 1,
"core": true,
"corder": 1
},
{
"tag": "Mano 3.16 (b · NAND)",
"type": "work",
"q": "Implement <code>F = AB + BC + A'B'C'D</code> with a two-level NAND circuit.",
"why": "<img src='svg/book/n3-16b.svg' alt=''><p>Recipe: every AND → NAND, the OR → NAND. A term that is a single letter goes straight into the output NAND <b>complemented</b>.</p>",
"ref": "09 §4",
"grp": 1,
"core": true,
"corder": 2
},
{
"tag": "Mano 3.16 (c)",
"type": "bool",
"q": "Simplify <code>F = (A' + B' + C')(A' + B')(A' + C')</code> (minimal SOP).",
"vars": "ABC",
"ones": [
0,
1,
2,
3,
4
],
"show": "A' + B'C'",
"lits": 3,
"why": "<p>Plot it: 1s on cells <b>0, 1, 2, 3, 4</b>.</p><img src='svg/book/k3-16c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'</b> from cells 0, 1, 2, 3</li><li><b>B'C'</b> from cells 0, 4</li></ul><p><b>F = A' + B'C'</b> (3 literals).</p>",
"ref": "09 §4",
"form": "sop",
"grp": 1,
"core": false
},
{
"tag": "Mano 3.16 (c · NAND)",
"type": "work",
"q": "Implement <code>F = A' + B'C'</code> with a two-level NAND circuit.",
"why": "<img src='svg/book/n3-16c.svg' alt=''><p>Recipe: every AND → NAND, the OR → NAND. A term that is a single letter goes straight into the output NAND <b>complemented</b>.</p>",
"ref": "09 §4",
"grp": 1,
"core": false
},
{
"tag": "Mano 3.16 (d)",
"type": "bool",
"q": "Simplify <code>F = A'B + A + C' + D'</code> (minimal SOP).",
"vars": "ABCD",
"ones": [
0,
1,
2,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15
],
"show": "A + B + D' + C'",
"lits": 4,
"why": "<p>Plot it: 1s on cells <b>0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15</b>.</p><img src='svg/book/k3-16d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>C'</b> from cells 0, 1, 4, 5, 8, 9, 12, 13</li><li><b>D'</b> from cells 0, 2, 4, 6, 8, 10, 12, 14</li><li><b>B</b> from cells 4, 5, 6, 7, 12, 13, 14, 15</li><li><b>A</b> from cells 8, 9, 10, 11, 12, 13, 14, 15</li></ul><p><b>F = A + B + D' + C'</b> (4 literals).</p>",
"ref": "09 §4",
"form": "sop",
"grp": 1,
"core": false
},
{
"tag": "Mano 3.16 (d · NAND)",
"type": "work",
"q": "Implement <code>F = A + B + D' + C'</code> with a two-level NAND circuit.",
"why": "<img src='svg/book/n3-16d.svg' alt=''><p>Recipe: every AND → NAND, the OR → NAND. A term that is a single letter goes straight into the output NAND <b>complemented</b>.</p>",
"ref": "09 §4",
"grp": 1,
"core": false
}
]
},
{
"n": "3.17",
"text": "NAND diagram for the complement of F.",
"qs": [
{
"tag": "Mano 3.17 (F') ★",
"type": "bool",
"q": "F(A, B, C, D) = Σ(0, 1, 2, 3, 4, 8, 9, 12). Find a minimal SOP for the <b>complement F'</b>.",
"vars": "ABCD",
"ones": [
5,
6,
7,
10,
11,
13,
14,
15
],
"show": "AC + BC + BD",
"lits": 6,
"why": "<p>F' is 1 wherever F is 0: cells <b>5, 6, 7, 10, 11, 13, 14, 15</b>.</p><img src='svg/book/k3-17.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>BD</b> from cells 5, 7, 13, 15</li><li><b>BC</b> from cells 6, 7, 14, 15</li><li><b>AC</b> from cells 10, 11, 14, 15</li></ul><p><b>F = AC + BC + BD</b> (6 literals).</p>",
"ref": "09 §4",
"form": "sop",
"grp": 1,
"core": true,
"corder": 3
},
{
"tag": "Mano 3.17 (NAND) ★",
"type": "work",
"q": "Draw the NAND logic diagram for <code>F' = AC + BC + BD</code>.",
"why": "<img src='svg/book/n3-17.svg' alt=''><p>Same NAND-NAND recipe, applied to F' instead of F.</p>",
"ref": "09 §4",
"grp": 1,
"core": true,
"corder": 4
}
]
},
{
"n": "3.18",
"text": "Two-input NOR gates only.",
"qs": [
{
"tag": "Mano 3.18",
"type": "work",
"q": "Draw a logic diagram using only <b>two-input NOR</b> gates for <code>F = (A ⊕ B)'(C ⊕ D)</code>.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>F = [(A ⊕ B) + (C ⊕ D)']'</td><td>De Morgan: XY = (X' + Y')'. So the output gate is a NOR</td></tr><tr><td>2</td><td>A ⊕ B = (AB + A'B')' = NOR(AB, A'B')</td><td>AB = NOR(A', B'), A'B' = NOR(A, B)</td></tr><tr><td>3</td><td>(C ⊕ D)' = (C'D + CD')' = NOR(C'D, CD')</td><td>C'D = NOR(C, D'), CD' = NOR(C', D)</td></tr><tr><td>4</td><td>A' = NOR(A, A)</td><td>tie both inputs together for an inverter</td></tr></table><img src='svg/book/n3-18.svg' alt=''><p>11 NOR gates. Mano's answer may share gates differently; any correct all-NOR circuit is fine.</p>",
"ref": "09 §5",
"grp": 3,
"core": false
}
]
},
{
"n": "3.19",
"text": "Simplify, then implement with two-level NOR circuits.",
"qs": [
{
"tag": "Mano 3.19 (a) ★",
"type": "bool",
"q": "Simplify <code>F = wx' + y'z' + w'yz'</code> to a minimal <b>product of sums</b>.",
"vars": "wxyz",
"ones": [
0,
2,
4,
6,
8,
9,
10,
11,
12
],
"show": "(w + z')(x' + z')(w' + x' + y')",
"lits": 7,
"why": "<p>Plot it: F = 1 on 0, 2, 4, 6, 8, 9, 10, 11, 12, so the 0s are on 1, 3, 5, 7, 13, 14, 15.</p><img src='svg/book/k3-19a.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(w + z')</b> from cells 1, 3, 5, 7</li><li><b>(x' + z')</b> from cells 5, 7, 13, 15</li><li><b>(w' + x' + y')</b> from cells 14, 15</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (w + z')(x' + z')(w' + x' + y')</b> (7 literals).</p>",
"ref": "09 §5",
"form": "pos",
"grp": 2,
"core": true,
"corder": 1
},
{
"tag": "Mano 3.19 (a · NOR) ★",
"type": "work",
"q": "Implement <code>F = (w + z')(x' + z')(w' + x' + y')</code> with a two-level NOR circuit.",
"why": "<img src='svg/book/n3-19a.svg' alt=''><p>Recipe: every OR → NOR, the AND → NOR. A single-letter factor goes into the output NOR complemented.</p>",
"ref": "09 §5",
"grp": 2,
"core": true,
"corder": 2
},
{
"tag": "Mano 3.19 (b)",
"type": "bool",
"q": "Simplify <code>F(w, x, y, z) = Σ(1, 2, 13, 14)</code> to a minimal <b>product of sums</b>.",
"vars": "wxyz",
"ones": [
1,
2,
13,
14
],
"show": "(y + z)(y' + z')(w + x')(w' + x)",
"lits": 8,
"why": "<p>Plot it: F = 1 on 1, 2, 13, 14, so the 0s are on 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15.</p><img src='svg/book/k3-19b.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(y + z)</b> from cells 0, 4, 8, 12</li><li><b>(y' + z')</b> from cells 3, 7, 11, 15</li><li><b>(w + x')</b> from cells 4, 5, 6, 7</li><li><b>(w' + x)</b> from cells 8, 9, 10, 11</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (y + z)(y' + z')(w + x')(w' + x)</b> (8 literals).</p>",
"ref": "09 §5",
"form": "pos",
"grp": 2,
"core": false
},
{
"tag": "Mano 3.19 (b · NOR)",
"type": "work",
"q": "Implement <code>F = (y + z)(y' + z')(w + x')(w' + x)</code> with a two-level NOR circuit.",
"why": "<img src='svg/book/n3-19b.svg' alt=''><p>Recipe: every OR → NOR, the AND → NOR. A single-letter factor goes into the output NOR complemented.</p>",
"ref": "09 §5",
"grp": 2,
"core": false
},
{
"tag": "Mano 3.19 (c)",
"type": "bool",
"q": "Simplify <code>F = [(x + y)(x' + z)]'</code> to a minimal <b>product of sums</b>.",
"vars": "xyz",
"ones": [
0,
1,
4,
6
],
"show": "(x + y')(x' + z')",
"lits": 4,
"why": "<p>Plot it: F = 1 on 0, 1, 4, 6, so the 0s are on 2, 3, 5, 7.</p><img src='svg/book/k3-19c.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(x + y')</b> from cells 2, 3</li><li><b>(x' + z')</b> from cells 5, 7</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (x + y')(x' + z')</b> (4 literals).</p>",
"ref": "09 §5",
"form": "pos",
"grp": 2,
"core": false
},
{
"tag": "Mano 3.19 (c · NOR)",
"type": "work",
"q": "Implement <code>F = (x + y')(x' + z')</code> with a two-level NOR circuit.",
"why": "<img src='svg/book/n3-19c.svg' alt=''><p>Recipe: every OR → NOR, the AND → NOR. A single-letter factor goes into the output NOR complemented.</p>",
"ref": "09 §5",
"grp": 2,
"core": false
}
]
},
{
"n": "3.20",
"text": "Multi-level NOR and NAND circuits.",
"qs": [
{
"tag": "Mano 3.20 (NAND)",
"type": "work",
"q": "Draw the multi-level <b>NAND</b> circuit for <code>(AB' + CD')E + BC(A + B)</code>.",
"why": "<p>Method: draw it with AND and OR gates, then <b>NAND version</b>: every AND → NAND, every OR → NAND with bubbles on its inputs; where two bubbles meet on a wire they cancel, where one is left over you need an inverter (or complement the input letter). <b>NOR version</b>: swap the roles of AND and OR.</p><img src='svg/book/n3-20nand.svg' alt=''><p>Inputs with a dash (A', D') are complemented inputs; an inverter is a NAND with its inputs tied.</p>",
"ref": "09 §3",
"grp": 3,
"core": true,
"corder": 2
},
{
"tag": "Mano 3.20 (NOR)",
"type": "work",
"q": "Draw the multi-level <b>NOR</b> circuit for <code>(AB' + CD')E + BC(A + B)</code>.",
"why": "<p>Method: draw it with AND and OR gates, then <b>NAND version</b>: every AND → NAND, every OR → NAND with bubbles on its inputs; where two bubbles meet on a wire they cancel, where one is left over you need an inverter (or complement the input letter). <b>NOR version</b>: swap the roles of AND and OR.</p><img src='svg/book/n3-20nor.svg' alt=''>",
"ref": "09 §3",
"grp": 3,
"core": false
}
]
},
{
"n": "3.21",
"text": "Multi-level NAND circuit.",
"qs": [
{
"tag": "Mano 3.21",
"type": "work",
"q": "Draw the multi-level NAND circuit for <code>w(x + y + z) + xyz</code>.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>x + y + z = (x'y'z')'</td><td>an OR is a NAND of the complemented inputs</td></tr><tr><td>2</td><td>w(x + y + z) = [ (w·(x'y'z')')' ]'</td><td>AND → NAND, then the final NAND undoes the bar</td></tr><tr><td>3</td><td>F = [ (w(x + y + z))' · (xyz)' ]'</td><td>the top OR → NAND of NANDs</td></tr></table><img src='svg/book/n3-21.svg' alt=''>",
"ref": "09 §3",
"grp": 3,
"core": true,
"corder": 1
}
]
},
{
"n": "3.22",
"text": "Fig 4.4 (BCD-to-excess-3 converter) as multi-level NAND.",
"qs": [
{
"tag": "Mano 3.22",
"type": "work",
"q": "Convert the logic diagram of Fig 4.4 into a multiple-level NAND circuit. (In the 4th edition Fig 4.4 is the <b>BCD-to-excess-3 code converter</b>: w = A + B(C + D), x = B'(C + D) + B(C + D)', y = CD + (C + D)', z = D'.)",
"why": "<p>Check the four equations first: for every BCD input 0–9 they give the input + 3. ✓</p><img src='svg/book/n3-22.svg' alt=''><p>Each output converted with the bubble method. In the real circuit the C + D gate is <b>shared</b> by w, x and y; here it's drawn once per output so each is easy to follow.</p>",
"ref": "09 §3",
"grp": 3,
"core": false
}
]
},
{
"n": "3.23",
"text": "Implement F with no more than two NOR gates.",
"qs": [
{
"tag": "Mano 3.23 (POS)",
"type": "bool",
"q": "F(A, B, C, D) = Σ(2, 4, 6, 10, 12), d = Σ(0, 8, 9, 13). Find a minimal <b>product of sums</b> (use the don't cares).",
"vars": "ABCD",
"ones": [
2,
4,
6,
10,
12
],
"show": "D'(A' + B' + C')",
"lits": 4,
"why": "<p>F = 1 on cells 2, 4, 6, 10, 12, don't care on 0, 8, 9, 13.</p><img src='svg/book/k3-23.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>D'</b> from cells 1, 3, 5, 7, 9, 11, 13, 15</li><li><b>(A' + B' + C')</b> from cells 14, 15</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = D'(A' + B' + C')</b> (4 literals).</p>",
"ref": "09 §1",
"dc": [
0,
8,
9,
13
],
"form": "pos",
"grp": 2,
"core": false
},
{
"tag": "Mano 3.23 (2 NORs)",
"type": "work",
"q": "Implement that F with <b>no more than two NOR gates</b> (normal and complemented inputs are available).",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>F = D'(A' + B' + C')</td><td>the POS from the map</td></tr><tr><td>2</td><td>F = [ D + (A' + B' + C')' ]'</td><td>XY = (X' + Y')', and D'' = D</td></tr><tr><td>3</td><td>inner NOR(A', B', C'), outer NOR(D, inner)</td><td>two NOR gates</td></tr></table><img src='svg/book/n3-23.svg' alt=''>",
"ref": "09 §5",
"grp": 2,
"core": false
}
]
},
{
"n": "3.24",
"text": "Four two-level forms of the same F.",
"qs": [
{
"tag": "Mano 3.24 (a)",
"type": "work",
"q": "Implement <code>F(A, B, C, D) = Σ(0, 4, 8, 9, 10, 11, 12, 14)</code> in <b>NAND-AND</b> form.",
"why": "<img src='svg/book/k3-24.svg' alt=''><p>All four forms start from F' (group the 0s): F' = <b>BD + A'C + A'D</b>, or as POS F' = <b>(C + D)(A' + B)(A' + D)</b>.</p><p>F = (F')' and F' = BD + A'C + A'D: F = (BD)'·(A'C)'·(A'D)'. Each (term)' is a NAND, then AND them.</p><img src='svg/book/n3-24a.svg' alt=''>",
"ref": "09 §3",
"grp": 4,
"core": false
},
{
"tag": "Mano 3.24 (b)",
"type": "work",
"q": "Implement <code>F(A, B, C, D) = Σ(0, 4, 8, 9, 10, 11, 12, 14)</code> in <b>AND-NOR</b> form.",
"why": "<p>F = (F')' = (BD + A'C + A'D)': ANDs for F', NOR to complement.</p><img src='svg/book/n3-24b.svg' alt=''>",
"ref": "09 §3",
"grp": 4,
"core": true,
"corder": 1
},
{
"tag": "Mano 3.24 (c)",
"type": "work",
"q": "Implement <code>F(A, B, C, D) = Σ(0, 4, 8, 9, 10, 11, 12, 14)</code> in <b>OR-NAND</b> form.",
"why": "<p>F' as POS = (C + D)(A' + B)(A' + D), so F = [(C + D)(A' + B)(A' + D)]': ORs, then a NAND.</p><img src='svg/book/n3-24c.svg' alt=''>",
"ref": "09 §3",
"grp": 4,
"core": false
},
{
"tag": "Mano 3.24 (d)",
"type": "work",
"q": "Implement <code>F(A, B, C, D) = Σ(0, 4, 8, 9, 10, 11, 12, 14)</code> in <b>NOR-OR</b> form.",
"why": "<p>F = [(C + D)(A' + B)(A' + D)]' = sum of each (factor)': NORs into an OR.</p><img src='svg/book/n3-24d.svg' alt=''>",
"ref": "09 §3",
"grp": 4,
"core": false
}
]
},
{
"n": "3.25",
"text": "The eight degenerate two-level forms.",
"qs": [
{
"tag": "Mano 3.25",
"type": "work",
"q": "List the eight degenerate two-level forms and show each reduces to a single operation. How can they extend a gate's number of inputs?",
"why": "<table class='bits'><tr><th>form</th><th>equals</th><th>why</th></tr><tr><td>AND-AND</td><td>AND</td><td>(AB)(CD) = ABCD</td></tr><tr><td>OR-OR</td><td>OR</td><td>(A+B)+(C+D)</td></tr><tr><td>AND-NAND</td><td>NAND</td><td>[(AB)(CD)]' = (ABCD)'</td></tr><tr><td>OR-NOR</td><td>NOR</td><td>[(A+B)+(C+D)]'</td></tr><tr><td>NAND-OR</td><td>NAND</td><td>(AB)' + (CD)' = A'+B'+C'+D' = (ABCD)'</td></tr><tr><td>NOR-AND</td><td>NOR</td><td>(A+B)'(C+D)' = (A+B+C+D)'</td></tr><tr><td>NAND-NOR</td><td>AND</td><td>[(AB)' + (CD)']' = ABCD</td></tr><tr><td>NOR-NAND</td><td>OR</td><td>[(A+B)'(C+D)']' = A+B+C+D</td></tr></table><p><b>Extending inputs:</b> to get a 4-input NAND from 2-input gates, use two ANDs into one NAND (AND-NAND). Or two NANDs into an OR (NAND-OR). Each pair of gates acts like one bigger gate.</p>",
"ref": "09 §3",
"grp": 4,
"core": false
}
]
}
],
"groups": [
{
"name": "Don't cares",
"blurb": "Use an x only when it makes a block bigger."
},
{
"name": "NAND-NAND from SOP",
"blurb": "Every gate becomes a NAND; lone letters go in complemented."
},
{
"name": "NOR-NOR from POS",
"blurb": "The same trick from the POS."
},
{
"name": "Multi-level NAND and NOR",
"blurb": "Bubble pushing: two bubbles cancel, one left over is an inverter."
},
{
"name": "Other two-level forms",
"blurb": "AND-NOR, NAND-AND, OR-NAND, NOR-OR all start from F'."
}
]
});
