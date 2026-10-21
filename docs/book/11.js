BOOK.add({
"id": "11",
"title": "Decoders and encoders",
"intro": "Mano 4.22–4.30. Block diagrams are self-marked; equations are checked on every row.",
"problems": [
{
"n": "4.22",
"text": "Excess-3-to-binary decoder with don't cares.",
"qs": [
{
"tag": "Mano 4.22 (table) ★",
"type": "tt",
"q": "Excess-3 in (ABCD), binary out (wxyz). Valid codes are 3 to 12; the rest are don't cares (leave them 0 here).",
"vars": "ABCD",
"outs": {
"w": [
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
1,
0,
0,
0
],
"x": [
0,
0,
0,
0,
0,
0,
0,
1,
1,
1,
1,
0,
0,
0,
0,
0
],
"y": [
0,
0,
0,
0,
0,
1,
1,
0,
0,
1,
1,
0,
0,
0,
0,
0
],
"z": [
0,
0,
0,
0,
1,
0,
1,
0,
1,
0,
1,
0,
1,
0,
0,
0
]
},
"why": "<p>Output = input − 3: 0011 → 0000, 0100 → 0001, … 1100 → 1001.</p>",
"ref": "09 §1",
"grp": 2,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.22 (w) ★",
"type": "bool",
"q": "Excess-3 → binary: minimal SOP for <b>w</b> (0, 1, 2, 13, 14, 15 are don't cares).",
"vars": "ABCD",
"ones": [
11,
12
],
"show": "AB + ACD",
"lits": 5,
"why": "<p>F = 1 on cells 11, 12, don't care on 0, 1, 2, 13, 14, 15.</p><img src='svg/book/k4-22w.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>ACD</b> from cells 11, 15</li><li><b>AB</b> from cells 12, 13, 14, 15</li></ul><p><b>F = AB + ACD</b> (5 literals).</p>",
"ref": "09 §1",
"dc": [
0,
1,
2,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.22 (x) ★",
"type": "bool",
"q": "Excess-3 → binary: minimal SOP for <b>x</b> (0, 1, 2, 13, 14, 15 are don't cares).",
"vars": "ABCD",
"ones": [
7,
8,
9,
10
],
"show": "B'D' + B'C' + BCD",
"lits": 7,
"why": "<p>F = 1 on cells 7, 8, 9, 10, don't care on 0, 1, 2, 13, 14, 15.</p><img src='svg/book/k4-22x.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>BCD</b> from cells 7, 15</li><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>B'C'</b> from cells 0, 1, 8, 9</li></ul><p><b>F = B'D' + B'C' + BCD</b> (7 literals).</p>",
"ref": "09 §1",
"dc": [
0,
1,
2,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": true,
"corder": 2
},
{
"tag": "Mano 4.22 (y) ★",
"type": "bool",
"q": "Excess-3 → binary: minimal SOP for <b>y</b> (0, 1, 2, 13, 14, 15 are don't cares).",
"vars": "ABCD",
"ones": [
5,
6,
9,
10
],
"show": "CD' + C'D",
"lits": 4,
"why": "<p>F = 1 on cells 5, 6, 9, 10, don't care on 0, 1, 2, 13, 14, 15.</p><img src='svg/book/k4-22y.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>C'D</b> from cells 1, 5, 9, 13</li><li><b>CD'</b> from cells 2, 6, 10, 14</li></ul><p><b>F = CD' + C'D</b> (4 literals).</p>",
"ref": "09 §1",
"dc": [
0,
1,
2,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.22 (z) ★",
"type": "bool",
"q": "Excess-3 → binary: minimal SOP for <b>z</b> (0, 1, 2, 13, 14, 15 are don't cares).",
"vars": "ABCD",
"ones": [
4,
6,
8,
10,
12
],
"show": "D'",
"lits": 1,
"why": "<p>F = 1 on cells 4, 6, 8, 10, 12, don't care on 0, 1, 2, 13, 14, 15.</p><img src='svg/book/k4-22z.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>D'</b> from cells 0, 2, 4, 6, 8, 10, 12, 14</li></ul><p><b>F = D'</b> (1 literal).</p>",
"ref": "09 §1",
"dc": [
0,
1,
2,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
}
]
},
{
"n": "4.23",
"text": "2-to-4 decoder with enable: NOR only and NAND only.",
"qs": [
{
"tag": "Mano 4.23 (a)",
"type": "work",
"q": "Draw a 2-to-4 line decoder with enable E using <b>NOR gates only</b>.",
"why": "<p>D₀ = A'B'E = (A + B + E')' → one 3-input NOR per output, fed with the <b>complements</b> of the letters it needs. A NOR with its inputs tied is the inverter.</p><img src='svg/book/c4-23a.svg' alt=''><p>In a real circuit the three inverters (A', B', E') are drawn once and shared by all four outputs.</p>",
"ref": "11 §3",
"grp": 1,
"core": false
},
{
"tag": "Mano 4.23 (b)",
"type": "work",
"q": "Draw a 2-to-4 line decoder with enable E using <b>NAND gates only</b>.",
"why": "<p>A NAND gives the minterm complemented, so the outputs are <b>active-low</b> (the selected output goes to 0), like Fig 4.19. Dᵢ' = NAND(the letters of mᵢ, E).</p><img src='svg/book/c4-23b.svg' alt=''>",
"ref": "11 §4",
"grp": 1,
"core": true,
"corder": 1
}
]
},
{
"n": "4.24",
"text": "BCD-to-decimal decoder using don't cares.",
"qs": [
{
"tag": "Mano 4.24 (D0)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D0</b>.",
"vars": "ABCD",
"ones": [
0
],
"show": "A'B'C'D'",
"lits": 4,
"why": "<p>F = 1 on cells 0, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d0.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>A'B'C'D'</b> from cells 0</li></ul><p><b>F = A'B'C'D'</b> (4 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D1)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D1</b>.",
"vars": "ABCD",
"ones": [
1
],
"show": "A'B'C'D",
"lits": 4,
"why": "<p>F = 1 on cells 1, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d1.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>A'B'C'D</b> from cells 1</li></ul><p><b>F = A'B'C'D</b> (4 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D2)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D2</b>.",
"vars": "ABCD",
"ones": [
2
],
"show": "B'CD'",
"lits": 3,
"why": "<p>F = 1 on cells 2, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d2.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>B'CD'</b> from cells 2, 10</li></ul><p><b>F = B'CD'</b> (3 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D3)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D3</b>.",
"vars": "ABCD",
"ones": [
3
],
"show": "B'CD",
"lits": 3,
"why": "<p>F = 1 on cells 3, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d3.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>B'CD</b> from cells 3, 11</li></ul><p><b>F = B'CD</b> (3 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D4)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D4</b>.",
"vars": "ABCD",
"ones": [
4
],
"show": "BC'D'",
"lits": 3,
"why": "<p>F = 1 on cells 4, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d4.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>BC'D'</b> from cells 4, 12</li></ul><p><b>F = BC'D'</b> (3 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D5)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D5</b>.",
"vars": "ABCD",
"ones": [
5
],
"show": "BC'D",
"lits": 3,
"why": "<p>F = 1 on cells 5, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d5.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>BC'D</b> from cells 5, 13</li></ul><p><b>F = BC'D</b> (3 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D6)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D6</b>.",
"vars": "ABCD",
"ones": [
6
],
"show": "BCD'",
"lits": 3,
"why": "<p>F = 1 on cells 6, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d6.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>BCD'</b> from cells 6, 14</li></ul><p><b>F = BCD'</b> (3 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D7)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D7</b>.",
"vars": "ABCD",
"ones": [
7
],
"show": "BCD",
"lits": 3,
"why": "<p>F = 1 on cells 7, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d7.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>BCD</b> from cells 7, 15</li></ul><p><b>F = BCD</b> (3 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.24 (D8)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D8</b>.",
"vars": "ABCD",
"ones": [
8
],
"show": "AD'",
"lits": 2,
"why": "<p>F = 1 on cells 8, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d8.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>AD'</b> from cells 8, 10, 12, 14</li></ul><p><b>F = AD'</b> (2 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": true,
"corder": 3
},
{
"tag": "Mano 4.24 (D9)",
"type": "bool",
"q": "BCD-to-decimal decoder (inputs ABCD, 10–15 don't care): minimal output <b>D9</b>.",
"vars": "ABCD",
"ones": [
9
],
"show": "AD",
"lits": 2,
"why": "<p>F = 1 on cells 9, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-24d9.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>AD</b> from cells 9, 11, 13, 15</li></ul><p><b>F = AD</b> (2 literals).</p>",
"ref": "11 §1",
"dc": [
10,
11,
12,
13,
14,
15
],
"form": "sop",
"grp": 2,
"core": false
}
]
},
{
"n": "4.25",
"text": "5-to-32 decoder from four 3-to-8 and one 2-to-4.",
"qs": [
{
"tag": "Mano 4.25",
"type": "work",
"q": "Build a 5-to-32 line decoder from four 3-to-8 decoders with enable and one 2-to-4 decoder (block diagram).",
"why": "<p>The top two bits A₄A₃ pick <b>which</b> 3-to-8 decoder is on (they drive the 2-to-4, whose outputs are the four enables). The low three bits A₂A₁A₀ go to all four 3-to-8s and pick the line inside the chosen one.</p><img src='svg/book/b4-25.svg' alt=''>",
"ref": "11 §3",
"grp": 1,
"core": true,
"corder": 2
}
]
},
{
"n": "4.26",
"text": "4-to-16 decoder from five 2-to-4 decoders.",
"qs": [
{
"tag": "Mano 4.26",
"type": "work",
"q": "Build a 4-to-16 line decoder from five 2-to-4 decoders with enable.",
"why": "<p>Same tree idea: one 2-to-4 on the top bits A₃A₂ enables one of four 2-to-4s, which decode A₁A₀.</p><img src='svg/book/b4-26.svg' alt=''>",
"ref": "11 §3",
"grp": 1,
"core": false
}
]
},
{
"n": "4.27",
"text": "Three functions from a NAND decoder with NAND/AND gates.",
"qs": [
{
"tag": "Mano 4.27",
"type": "work",
"q": "F₁ = Σ(3, 5, 6), F₂ = Σ(1, 4), F₃ = Σ(2, 3, 5, 6, 7). Use a decoder built from NAND gates (active-low outputs) plus NAND or AND gates, with as few gate inputs as possible.",
"why": "<p>Active-low outputs: the selected line is 0. A <b>NAND</b> of active-low lines = OR of the minterms (De Morgan).</p><p>F₁: NAND of lines 3, 5, 6 (3 inputs). F₂: NAND of 1, 4 (2 inputs). F₃ has 5 minterms, so use its 0s instead: F₃' = Σ(0, 1, 4), and F₃ = <b>AND</b> of active-low lines 0, 1, 4 (3 inputs, not 5).</p><img src='svg/book/b4-27.svg' alt=''>",
"ref": "11 §4",
"grp": 0,
"core": true,
"corder": 2
}
]
},
{
"n": "4.28",
"text": "Decoder plus external gates.",
"qs": [
{
"tag": "Mano 4.28 (a)",
"type": "multi",
"q": "With a 3-to-8 decoder (inputs x, y, z) and OR gates, implement: <code>F₁ = x'y'z' + xz</code>; <code>F₂ = xy'z' + x'y</code>; <code>F₃ = x'y'z + xy</code>. List each function's minterms.",
"fields": [
{
"label": "F₁ = Σm(",
"ans": [
"0,5,7",
"(0,5,7)",
"Σ(0,5,7)",
"Σm(0,5,7)",
"m(0,5,7)",
"Π(0,5,7)",
"ΠM(0,5,7)",
"M(0,5,7)"
]
},
{
"label": "F₂ = Σm(",
"ans": [
"2,3,4",
"(2,3,4)",
"Σ(2,3,4)",
"Σm(2,3,4)",
"m(2,3,4)",
"Π(2,3,4)",
"ΠM(2,3,4)",
"M(2,3,4)"
]
},
{
"label": "F₃ = Σm(",
"ans": [
"1,6,7",
"(1,6,7)",
"Σ(1,6,7)",
"Σm(1,6,7)",
"m(1,6,7)",
"Π(1,6,7)",
"ΠM(1,6,7)",
"M(1,6,7)"
]
}
],
"why": "<p>Expand each to minterms, then OR those decoder outputs.</p><ul><li><b>F₁ = x'y'z' + xz</b> = Σ(0, 5, 7) → OR of decoder outputs 0, 5, 7</li><li><b>F₂ = xy'z' + x'y</b> = Σ(2, 3, 4) → OR of decoder outputs 2, 3, 4</li><li><b>F₃ = x'y'z + xy</b> = Σ(1, 6, 7) → OR of decoder outputs 1, 6, 7</li></ul>",
"ref": "11 §2",
"grp": 0,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.28 (b)",
"type": "multi",
"q": "With a 3-to-8 decoder (inputs x, y, z) and OR gates, implement: <code>F₁ = (y' + x)z</code>; <code>F₂ = y'z' + xy' + yz'</code>; <code>F₃ = (x' + y)z</code>. List each function's minterms.",
"fields": [
{
"label": "F₁ = Σm(",
"ans": [
"1,5,7",
"(1,5,7)",
"Σ(1,5,7)",
"Σm(1,5,7)",
"m(1,5,7)",
"Π(1,5,7)",
"ΠM(1,5,7)",
"M(1,5,7)"
]
},
{
"label": "F₂ = Σm(",
"ans": [
"0,2,4,5,6",
"(0,2,4,5,6)",
"Σ(0,2,4,5,6)",
"Σm(0,2,4,5,6)",
"m(0,2,4,5,6)",
"Π(0,2,4,5,6)",
"ΠM(0,2,4,5,6)",
"M(0,2,4,5,6)"
]
},
{
"label": "F₃ = Σm(",
"ans": [
"1,3,7",
"(1,3,7)",
"Σ(1,3,7)",
"Σm(1,3,7)",
"m(1,3,7)",
"Π(1,3,7)",
"ΠM(1,3,7)",
"M(1,3,7)"
]
}
],
"why": "<p>Expand each to minterms, then OR those decoder outputs.</p><ul><li><b>F₁ = (y' + x)z</b> = Σ(1, 5, 7) → OR of decoder outputs 1, 5, 7</li><li><b>F₂ = y'z' + xy' + yz'</b> = Σ(0, 2, 4, 5, 6) → NOR of outputs 1, 3, 7 (its 0s: fewer inputs)</li><li><b>F₃ = (x' + y)z</b> = Σ(1, 3, 7) → OR of decoder outputs 1, 3, 7</li></ul>",
"ref": "11 §2",
"grp": 0,
"core": false
}
]
},
{
"n": "4.29",
"text": "Priority encoder with D₀ highest.",
"qs": [
{
"tag": "Mano 4.29 (x) ★",
"type": "bool",
"q": "4-input priority encoder, <b>D₀ highest</b> priority. Write a = D₀, b = D₁, c = D₂, d = D₃. Outputs xy = index of the highest-priority 1. Minimal <b>x</b> (all-zero input is a don't care).",
"vars": "abcd",
"ones": [
1,
2,
3
],
"show": "a'b'",
"lits": 2,
"why": "<table class='bits'><tr><th>D₀</th><th>D₁</th><th>D₂</th><th>D₃</th><th>x</th><th>y</th><th>V</th></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>x</td><td>x</td><td>0</td></tr><tr><td>1</td><td>x</td><td>x</td><td>x</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>x</td><td>x</td><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>x</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table><p>F = 1 on cells 1, 2, 3, don't care on 0.</p><img src='svg/book/k4-29x.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>a'b'</b> from cells 0, 1, 2, 3</li></ul><p><b>F = a'b'</b> (2 literals).</p>",
"ref": "11 §5",
"dc": [
0
],
"form": "sop",
"grp": 3,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.29 (y) ★",
"type": "bool",
"q": "Same encoder: minimal <b>y</b>.",
"vars": "abcd",
"ones": [
1,
4,
5,
6,
7
],
"show": "a'b + a'c'",
"lits": 4,
"why": "<p>F = 1 on cells 1, 4, 5, 6, 7, don't care on 0.</p><img src='svg/book/k4-29y.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>a'c'</b> from cells 0, 1, 4, 5</li><li><b>a'b</b> from cells 4, 5, 6, 7</li></ul><p><b>F = a'b + a'c'</b> (4 literals).</p>",
"ref": "11 §5",
"dc": [
0
],
"form": "sop",
"grp": 3,
"core": true,
"corder": 2
},
{
"tag": "Mano 4.29 (V) ★",
"type": "bool",
"q": "Same encoder: write the valid output <b>V</b> (1 when any input is 1).",
"vars": "abcd",
"ones": [
1,
2,
3,
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
"show": "a + b + c + d",
"why": "<p><b>V = D₀ + D₁ + D₂ + D₃</b>.</p>",
"lits": 4,
"ref": "11 §5",
"grp": 3,
"core": false
}
]
},
{
"n": "4.30",
"text": "Octal-to-binary priority encoder.",
"qs": [
{
"tag": "Mano 4.30",
"type": "multi",
"q": "Octal-to-binary priority encoder (D₇ highest priority) with a valid output V. What are x y z and V when D₂ and D₆ are both 1?",
"fields": [
{
"label": "x",
"ans": [
"1"
]
},
{
"label": "y",
"ans": [
"1"
]
},
{
"label": "z",
"ans": [
"0"
]
},
{
"label": "V",
"ans": [
"1"
]
}
],
"why": "<p>Condensed truth table (inputs written D₇ … D₀; x = don't care):</p><table class='bits'><tr><th>D₇…D₀</th><th>xyz</th><th>V</th></tr><tr><td>00000000</td><td>xxx</td><td>0</td></tr><tr><td>1xxxxxxx</td><td>111</td><td>1</td></tr><tr><td>01xxxxxx</td><td>110</td><td>1</td></tr><tr><td>001xxxxx</td><td>101</td><td>1</td></tr><tr><td>0001xxxx</td><td>100</td><td>1</td></tr><tr><td>00001xxx</td><td>011</td><td>1</td></tr><tr><td>000001xx</td><td>010</td><td>1</td></tr><tr><td>0000001x</td><td>001</td><td>1</td></tr><tr><td>00000001</td><td>000</td><td>1</td></tr></table><p>D₆ beats D₂ (higher subscript wins), so the output is 6 = <b>110</b>, V = <b>1</b>.</p>",
"ref": "11 §5",
"grp": 3,
"core": true,
"corder": 3
}
]
}
],
"groups": [
{
"name": "Functions from a decoder",
"blurb": "Decoder gives every minterm; OR the ones you need."
},
{
"name": "Inside a decoder, and bigger decoders",
"blurb": "Gate-level decoders; enables build bigger ones."
},
{
"name": "Decoder design with don't cares",
"blurb": "Unused input codes are free x's."
},
{
"name": "Priority encoders",
"blurb": "Highest-priority 1 wins; V says any input is on."
}
]
});
