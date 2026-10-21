BOOK.add({
"id": "10",
"title": "Adders and subtractors",
"intro": "Mano 3.28–3.30, 3.33, 4.4–4.21: parity, combinational design, adders, subtractors, comparators.",
"problems": [
{
"n": "3.28",
"text": "Odd-parity generator (3 bits) and checker (4 bits).",
"qs": [
{
"tag": "Mano 3.28 (generator)",
"type": "bool",
"q": "Odd parity: the parity bit P makes the total number of 1s in x, y, z, P <b>odd</b>. Write P.",
"vars": "xyz",
"ones": [
0,
3,
5,
6
],
"show": "(x ⊕ y ⊕ z)'",
"why": "<p>x ⊕ y ⊕ z = 1 when x, y, z already have an odd number of 1s. Then P must be 0. So P is the opposite: <b>P = (x ⊕ y ⊕ z)'</b> (an XOR followed by an XNOR).</p><table class='tts'><tr><th>x</th><th>y</th><th>z</th><th class='o'>P</th></tr><tr><td>0</td><td>0</td><td>0</td><td class='o'>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td class='o'>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td class='o'>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td class='o'>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td class='o'>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td class='o'>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td class='o'>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td class='o'>0</td></tr></table>",
"ref": "10 §1",
"grp": 0,
"core": true,
"corder": 1
},
{
"tag": "Mano 3.28 (checker)",
"type": "bool",
"q": "The checker gets x, y, z, P. Write the error output C (C = 1 when the count of 1s is <b>even</b>, i.e. something flipped).",
"vars": "xyzP",
"ones": [
0,
3,
5,
6,
9,
10,
12,
15
],
"show": "(x ⊕ y ⊕ z ⊕ P)'",
"why": "<p>x ⊕ y ⊕ z ⊕ P = 1 for an odd count (correct). So the error output is its complement: <b>C = (x ⊕ y ⊕ z ⊕ P)'</b>.</p><img src='svg/book/c3-28.svg' alt=''>",
"ref": "10 §1",
"grp": 0,
"core": false
}
]
},
{
"n": "3.29",
"text": "Four functions from three half adders.",
"qs": [
{
"tag": "Mano 3.29",
"type": "work",
"q": "Implement D = A ⊕ B ⊕ C, E = A'BC + AB'C, F = ABC' + (A' + B')C, G = ABC with <b>three half adders</b>.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>E = C(A'B + AB') = (A ⊕ B)C</td><td>factor C</td></tr><tr><td>2</td><td>F = (AB)C' + (AB)'C = (AB) ⊕ C</td><td>(A' + B') = (AB)' by De Morgan</td></tr><tr><td>3</td><td>HA 1 on A, B → A ⊕ B and AB</td><td></td></tr><tr><td>4</td><td>HA 2 on (A ⊕ B), C → D and E</td><td>sum and carry</td></tr><tr><td>5</td><td>HA 3 on AB, C → F and G</td><td>sum and carry</td></tr></table><img src='svg/book/b3-29.svg' alt=''>",
"ref": "10 §2",
"grp": 4,
"core": false
}
]
},
{
"n": "3.30",
"text": "Implement with XOR and AND gates.",
"qs": [
{
"tag": "Mano 3.30 ★",
"type": "bool",
"q": "Write <code>F = AB'CD' + A'BCD' + AB'C'D + A'BC'D</code> using XOR (⊕) and AND only.",
"vars": "ABCD",
"ones": [
5,
6,
9,
10
],
"show": "(A ⊕ B)(C ⊕ D)",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>CD'(AB' + A'B) + C'D(AB' + A'B)</td><td>factor terms 1+2 and 3+4</td></tr><tr><td>2</td><td>(AB' + A'B)(CD' + C'D)</td><td>factor again</td></tr><tr><td>3</td><td><b>(A ⊕ B)(C ⊕ D)</b></td><td>each bracket is an XOR</td></tr></table><img src='svg/book/c3-30.svg' alt=''>",
"ref": "10 §1",
"grp": 0,
"core": true,
"corder": 2
}
]
},
{
"n": "3.33",
"text": "Gate delays in the AND-OR-NOT exclusive-OR.",
"qs": [
{
"tag": "Mano 3.33",
"type": "work",
"q": "The XOR of Fig 3.32(a) is built as x'y + xy' with inverters (4 ns), ANDs (8 ns) and an OR (10 ns). The input goes from xy = 00 to xy = 01 at t = 0. Draw every gate output from 0 to 50 ns.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>y rises at 0</td><td>the input change</td></tr><tr><td>2</td><td>y' falls at 0 + 4 = 4 ns</td><td>inverter delay</td></tr><tr><td>3</td><td>x'y rises at 0 + 8 = 8 ns</td><td>x' was already 1; AND delay from y</td></tr><tr><td>4</td><td>xy' stays 0</td><td>x = 0 holds it at 0</td></tr><tr><td>5</td><td>F rises at 8 + 10 = 18 ns</td><td>OR delay after x'y</td></tr></table><img src='svg/book/t3-33.svg' alt=''><p>The output is right (1) from <b>18 ns</b> onwards. The longest path sets the delay.</p>",
"ref": "10 §1",
"grp": 0,
"core": false
}
]
},
{
"n": "4.4",
"text": "Design circuits from a word description.",
"qs": [
{
"tag": "Mano 4.4 (a) ★",
"type": "bool",
"q": "Three inputs x, y, z, one output. Output = 1 when the binary value of xyz is <b>less than 3</b>. Write F.",
"vars": "xyz",
"ones": [
0,
1,
2
],
"show": "x'z' + x'y'",
"lits": 4,
"why": "<p>Less than 3 means rows 0, 1, 2.</p><img src='svg/book/k4-4a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y'</b> from cells 0, 1</li><li><b>x'z'</b> from cells 0, 2</li></ul><p><b>F = x'z' + x'y'</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop",
"grp": 1,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.4 (b)",
"type": "bool",
"q": "Same, but the output = 1 when the input is an <b>odd</b> number.",
"vars": "xyz",
"ones": [
1,
3,
5,
7
],
"show": "z",
"lits": 1,
"why": "<p>Odd rows: 1, 3, 5, 7. They all end in z = 1.</p><img src='svg/book/k4-4b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>z</b> from cells 1, 3, 5, 7</li></ul><p><b>F = z</b> (1 literal).</p>",
"ref": "08 §3",
"form": "sop",
"grp": 1,
"core": false
}
]
},
{
"n": "4.5",
"text": "+2 for 0–3, −3 for 4–7.",
"qs": [
{
"tag": "Mano 4.5 (table)",
"type": "tt",
"q": "Inputs xyz, outputs ABC. Inputs 0–3 → output = input + 2. Inputs 4–7 → output = input − 3. Fill the table.",
"vars": "xyz",
"outs": {
"A": [
0,
0,
1,
1,
0,
0,
0,
1
],
"B": [
1,
1,
0,
0,
0,
1,
1,
0
],
"C": [
0,
1,
0,
1,
1,
0,
1,
0
]
},
"why": "<p>Outputs in order: 0→2, 1→3, 2→4, 3→5, 4→1, 5→2, 6→3, 7→4. Write each as 3 bits.</p>",
"ref": "08 §3",
"grp": 1,
"core": false
},
{
"tag": "Mano 4.5 (A)",
"type": "bool",
"q": "From the table, write a minimal SOP for output <b>A</b>.",
"vars": "xyz",
"ones": [
2,
3,
7
],
"show": "yz + x'y",
"lits": 4,
"why": "<p>F = 1 on cells 2, 3, 7.</p><img src='svg/book/k4-5a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y</b> from cells 2, 3</li><li><b>yz</b> from cells 3, 7</li></ul><p><b>F = yz + x'y</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop",
"grp": 1,
"core": false
},
{
"tag": "Mano 4.5 (B)",
"type": "bool",
"q": "From the table, write a minimal SOP for output <b>B</b>.",
"vars": "xyz",
"ones": [
0,
1,
5,
6
],
"show": "y'z + x'y' + xyz'",
"lits": 7,
"why": "<p>F = 1 on cells 0, 1, 5, 6.</p><img src='svg/book/k4-5b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y'</b> from cells 0, 1</li><li><b>y'z</b> from cells 1, 5</li><li><b>xyz'</b> from cells 6</li></ul><p><b>F = y'z + x'y' + xyz'</b> (7 literals).</p>",
"ref": "08 §3",
"form": "sop",
"grp": 1,
"core": false
},
{
"tag": "Mano 4.5 (C)",
"type": "bool",
"q": "From the table, write a minimal SOP for output <b>C</b>.",
"vars": "xyz",
"ones": [
1,
3,
4,
6
],
"show": "xz' + x'z",
"lits": 4,
"why": "<p>F = 1 on cells 1, 3, 4, 6.</p><img src='svg/book/k4-5c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'z</b> from cells 1, 3</li><li><b>xz'</b> from cells 4, 6</li></ul><p><b>F = xz' + x'z</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop",
"grp": 1,
"core": false
}
]
},
{
"n": "4.6",
"text": "Three-input majority circuit.",
"qs": [
{
"tag": "Mano 4.6 (table) ★",
"type": "tt",
"q": "Fill the truth table of the 3-input majority function.",
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
"why": "<p>1 when two or three inputs are 1: rows 3, 5, 6, 7.</p>",
"ref": "08 §3",
"grp": 1,
"core": true,
"corder": 2
},
{
"tag": "Mano 4.6 (a) ★",
"type": "bool",
"q": "Three-input <b>majority</b> circuit: output 1 when more inputs are 1 than 0. Write F.",
"vars": "xyz",
"ones": [
3,
5,
6,
7
],
"show": "xy + xz + yz",
"lits": 6,
"why": "<p>F = 1 on cells 3, 5, 6, 7.</p><img src='svg/book/k4-6.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>yz</b> from cells 3, 7</li><li><b>xz</b> from cells 5, 7</li><li><b>xy</b> from cells 6, 7</li></ul><p><b>F = xy + xz + yz</b> (6 literals).</p>",
"ref": "08 §3",
"form": "sop",
"grp": 1,
"core": true,
"corder": 3
},
{
"tag": "Mano 4.6 (diagram) ★",
"type": "work",
"q": "Draw the majority circuit.",
"why": "<img src='svg/book/c4-6.svg' alt=''><p>This is also the carry-out of a full adder.</p>",
"ref": "10 §3",
"grp": 1,
"core": false
}
]
},
{
"n": "4.7",
"text": "Gray-to-binary converter with XOR gates.",
"qs": [
{
"tag": "Mano 4.7 (table)",
"type": "tt",
"q": "Gray code abcd (a = MSB) → binary wxyz. Fill the table.",
"vars": "abcd",
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
1,
1,
1,
1,
1,
1,
1,
1
],
"x": [
0,
0,
0,
0,
1,
1,
1,
1,
1,
1,
1,
1,
0,
0,
0,
0
],
"y": [
0,
0,
1,
1,
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
1,
1
],
"z": [
0,
1,
1,
0,
1,
0,
0,
1,
1,
0,
0,
1,
0,
1,
1,
0
]
},
"why": "<p>Rule: the first binary bit = the first Gray bit; each next binary bit = previous <b>binary</b> bit ⊕ next Gray bit.</p>",
"ref": "05 §2",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.7 (x) ★",
"type": "bool",
"q": "Write binary bit <b>x</b> using XOR gates (a b c d = Gray bits, a = MSB).",
"vars": "abcd",
"ones": [
4,
5,
6,
7,
8,
9,
10,
11
],
"show": "a ⊕ b",
"why": "<p><b>x = a ⊕ b</b>: XOR all the Gray bits from the top down to this one.</p>",
"ref": "05 §2",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.7 (y) ★",
"type": "bool",
"q": "Write binary bit <b>y</b> using XOR gates (a b c d = Gray bits, a = MSB).",
"vars": "abcd",
"ones": [
2,
3,
4,
5,
8,
9,
14,
15
],
"show": "a ⊕ b ⊕ c",
"why": "<p><b>y = a ⊕ b ⊕ c</b>: XOR all the Gray bits from the top down to this one.</p>",
"ref": "05 §2",
"grp": 2,
"core": true,
"corder": 3
},
{
"tag": "Mano 4.7 (z) ★",
"type": "bool",
"q": "Write binary bit <b>z</b> using XOR gates (a b c d = Gray bits, a = MSB).",
"vars": "abcd",
"ones": [
1,
2,
4,
7,
8,
11,
13,
14
],
"show": "a ⊕ b ⊕ c ⊕ d",
"why": "<p><b>z = a ⊕ b ⊕ c ⊕ d</b>: XOR all the Gray bits from the top down to this one.</p><img src='svg/book/c4-7.svg' alt=''>",
"ref": "05 §2",
"grp": 2,
"core": false
}
]
},
{
"n": "4.8",
"text": "8, 4, −2, −1 code to BCD converter.",
"qs": [
{
"tag": "Mano 4.8 (table) ★",
"type": "tt",
"q": "Inputs abcd in the 8, 4, −2, −1 code, outputs wxyz in BCD. Fill the table (the 6 unused codes are don't cares; leave them 0 here).",
"vars": "abcd",
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
1,
0,
0,
0,
0,
0,
0,
1
],
"x": [
0,
0,
0,
0,
1,
0,
0,
0,
0,
1,
1,
1,
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
0,
1
]
},
"why": "<p>84-2-1 codes: 0 = 0000, 1 = 0111, 2 = 0110, 3 = 0101, 4 = 0100, 5 = 1011, 6 = 1010, 7 = 1001, 8 = 1000, 9 = 1111. Unused: 0001, 0010, 0011, 1100, 1101, 1110.</p>",
"ref": "05 §1",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.8 (w) ★",
"type": "bool",
"q": "84-2-1 → BCD: minimal SOP for <b>w</b> (unused codes are don't cares).",
"vars": "abcd",
"ones": [
8,
15
],
"show": "ab + ac'd'",
"lits": 5,
"why": "<p>F = 1 on cells 8, 15, don't care on 1, 2, 3, 12, 13, 14.</p><img src='svg/book/k4-8w.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>ac'd'</b> from cells 8, 12</li><li><b>ab</b> from cells 12, 13, 14, 15</li></ul><p><b>F = ab + ac'd'</b> (5 literals).</p>",
"ref": "09 §1",
"dc": [
1,
2,
3,
12,
13,
14
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.8 (x) ★",
"type": "bool",
"q": "84-2-1 → BCD: minimal SOP for <b>x</b> (unused codes are don't cares).",
"vars": "abcd",
"ones": [
4,
9,
10,
11
],
"show": "b'c + b'd + bc'd'",
"lits": 7,
"why": "<p>F = 1 on cells 4, 9, 10, 11, don't care on 1, 2, 3, 12, 13, 14.</p><img src='svg/book/k4-8x.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>bc'd'</b> from cells 4, 12</li><li><b>b'd</b> from cells 1, 3, 9, 11</li><li><b>b'c</b> from cells 2, 3, 10, 11</li></ul><p><b>F = b'c + b'd + bc'd'</b> (7 literals).</p>",
"ref": "09 §1",
"dc": [
1,
2,
3,
12,
13,
14
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.8 (y) ★",
"type": "bool",
"q": "84-2-1 → BCD: minimal SOP for <b>y</b> (unused codes are don't cares).",
"vars": "abcd",
"ones": [
5,
6,
9,
10
],
"show": "cd' + c'd",
"lits": 4,
"why": "<p>F = 1 on cells 5, 6, 9, 10, don't care on 1, 2, 3, 12, 13, 14.</p><img src='svg/book/k4-8y.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>c'd</b> from cells 1, 5, 9, 13</li><li><b>cd'</b> from cells 2, 6, 10, 14</li></ul><p><b>F = cd' + c'd</b> (4 literals).</p>",
"ref": "09 §1",
"dc": [
1,
2,
3,
12,
13,
14
],
"form": "sop",
"grp": 2,
"core": false
},
{
"tag": "Mano 4.8 (z) ★",
"type": "bool",
"q": "84-2-1 → BCD: minimal SOP for <b>z</b> (unused codes are don't cares).",
"vars": "abcd",
"ones": [
5,
7,
9,
11,
15
],
"show": "d",
"lits": 1,
"why": "<p>F = 1 on cells 5, 7, 9, 11, 15, don't care on 1, 2, 3, 12, 13, 14.</p><img src='svg/book/k4-8z.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>d</b> from cells 1, 3, 5, 7, 9, 11, 13, 15</li></ul><p><b>F = d</b> (1 literal).</p>",
"ref": "09 §1",
"dc": [
1,
2,
3,
12,
13,
14
],
"form": "sop",
"grp": 2,
"core": false
}
]
},
{
"n": "4.9",
"text": "BCD-to-seven-segment decoder, invalid codes blank.",
"qs": [
{
"tag": "Mano 4.9 (table)",
"type": "tt",
"q": "BCD (ABCD) to seven-segment decoder. Fill the table for segments a–g. 1 = lit. Inputs 10–15 must give a <b>blank</b> display (all 0).",
"vars": "ABCD",
"outs": {
"a": [
1,
0,
1,
1,
0,
1,
1,
1,
1,
1,
0,
0,
0,
0,
0,
0
],
"b": [
1,
1,
1,
1,
1,
0,
0,
1,
1,
1,
0,
0,
0,
0,
0,
0
],
"c": [
1,
1,
0,
1,
1,
1,
1,
1,
1,
1,
0,
0,
0,
0,
0,
0
],
"d": [
1,
0,
1,
1,
0,
1,
1,
0,
1,
1,
0,
0,
0,
0,
0,
0
],
"e": [
1,
0,
1,
0,
0,
0,
1,
0,
1,
0,
0,
0,
0,
0,
0,
0
],
"f": [
1,
0,
0,
0,
1,
1,
1,
0,
1,
1,
0,
0,
0,
0,
0,
0
],
"g": [
0,
0,
1,
1,
1,
1,
1,
0,
1,
1,
0,
0,
0,
0,
0,
0
]
},
"why": "<p>Segments: a top, b upper right, c lower right, d bottom, e lower left, f upper left, g middle. This book's display draws 6 with the top bar, 7 as a, b, c only, and 9 with the bottom bar.</p><p>Rows 10–15 are real 0s here (blank), <b>not</b> don't cares, so the maps can't use them.</p>",
"ref": "11 §1",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.9 (a)",
"type": "bool",
"q": "BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>a</b>.",
"vars": "ABCD",
"ones": [
0,
2,
3,
5,
6,
7,
8,
9
],
"show": "A'C + AB'C' + A'BD + B'C'D'",
"lits": 11,
"why": "<p>Segment a is lit for digits 0, 2, 3, 5, 6, 7, 8, 9; rows 10–15 are 0.</p><img src='svg/book/k4-9a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'C</b> from cells 2, 3, 6, 7</li><li><b>A'BD</b> from cells 5, 7</li><li><b>AB'C'</b> from cells 8, 9</li><li><b>B'C'D'</b> from cells 0, 8</li></ul><p><b>F = A'C + AB'C' + A'BD + B'C'D'</b> (11 literals).</p><p>Just as small: A'C + AB'C' + A'BD + A'B'D'.</p>",
"ref": "08 §4",
"form": "sop",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.9 (b)",
"type": "bool",
"q": "BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>b</b>.",
"vars": "ABCD",
"ones": [
0,
1,
2,
3,
4,
7,
8,
9
],
"show": "B'C' + A'B' + A'CD + A'C'D'",
"lits": 10,
"why": "<p>Segment b is lit for digits 0, 1, 2, 3, 4, 7, 8, 9; rows 10–15 are 0.</p><img src='svg/book/k4-9b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'B'</b> from cells 0, 1, 2, 3</li><li><b>A'C'D'</b> from cells 0, 4</li><li><b>A'CD</b> from cells 3, 7</li><li><b>B'C'</b> from cells 0, 1, 8, 9</li></ul><p><b>F = B'C' + A'B' + A'CD + A'C'D'</b> (10 literals).</p>",
"ref": "08 §4",
"form": "sop",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.9 (c)",
"type": "bool",
"q": "BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>c</b>.",
"vars": "ABCD",
"ones": [
0,
1,
3,
4,
5,
6,
7,
8,
9
],
"show": "A'B + A'D + B'C'",
"lits": 6,
"why": "<p>Segment c is lit for digits 0, 1, 3, 4, 5, 6, 7, 8, 9; rows 10–15 are 0.</p><img src='svg/book/k4-9c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'D</b> from cells 1, 3, 5, 7</li><li><b>A'B</b> from cells 4, 5, 6, 7</li><li><b>B'C'</b> from cells 0, 1, 8, 9</li></ul><p><b>F = A'B + A'D + B'C'</b> (6 literals).</p>",
"ref": "08 §4",
"form": "sop",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.9 (d)",
"type": "bool",
"q": "BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>d</b>.",
"vars": "ABCD",
"ones": [
0,
2,
3,
5,
6,
8,
9
],
"show": "AB'C' + A'CD' + A'B'C + B'C'D' + A'BC'D",
"lits": 16,
"why": "<p>Segment d is lit for digits 0, 2, 3, 5, 6, 8, 9; rows 10–15 are 0.</p><img src='svg/book/k4-9d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'B'C</b> from cells 2, 3</li><li><b>A'BC'D</b> from cells 5</li><li><b>A'CD'</b> from cells 2, 6</li><li><b>AB'C'</b> from cells 8, 9</li><li><b>B'C'D'</b> from cells 0, 8</li></ul><p><b>F = AB'C' + A'CD' + A'B'C + B'C'D' + A'BC'D</b> (16 literals).</p><p>Just as small: AB'C' + A'CD' + A'B'C + A'B'D' + A'BC'D.</p>",
"ref": "08 §4",
"form": "sop",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.9 (e)",
"type": "bool",
"q": "BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>e</b>.",
"vars": "ABCD",
"ones": [
0,
2,
6,
8
],
"show": "A'CD' + B'C'D'",
"lits": 6,
"why": "<p>Segment e is lit for digits 0, 2, 6, 8; rows 10–15 are 0.</p><img src='svg/book/k4-9e.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'CD'</b> from cells 2, 6</li><li><b>B'C'D'</b> from cells 0, 8</li></ul><p><b>F = A'CD' + B'C'D'</b> (6 literals).</p>",
"ref": "08 §4",
"form": "sop",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.9 (f)",
"type": "bool",
"q": "BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>f</b>.",
"vars": "ABCD",
"ones": [
0,
4,
5,
6,
8,
9
],
"show": "AB'C' + A'BD' + A'BC' + B'C'D'",
"lits": 12,
"why": "<p>Segment f is lit for digits 0, 4, 5, 6, 8, 9; rows 10–15 are 0.</p><img src='svg/book/k4-9f.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'BC'</b> from cells 4, 5</li><li><b>A'BD'</b> from cells 4, 6</li><li><b>AB'C'</b> from cells 8, 9</li><li><b>B'C'D'</b> from cells 0, 8</li></ul><p><b>F = AB'C' + A'BD' + A'BC' + B'C'D'</b> (12 literals).</p><p>Just as small: AB'C' + A'BD' + A'BC' + A'C'D'.</p>",
"ref": "08 §4",
"form": "sop",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.9 (g)",
"type": "bool",
"q": "BCD → 7-segment, invalid inputs blank: minimal SOP for segment <b>g</b>.",
"vars": "ABCD",
"ones": [
2,
3,
4,
5,
6,
8,
9
],
"show": "AB'C' + A'BC' + A'CD' + A'B'C",
"lits": 12,
"why": "<p>Segment g is lit for digits 2, 3, 4, 5, 6, 8, 9; rows 10–15 are 0.</p><img src='svg/book/k4-9g.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'B'C</b> from cells 2, 3</li><li><b>A'BC'</b> from cells 4, 5</li><li><b>AB'C'</b> from cells 8, 9</li><li><b>A'CD'</b> from cells 2, 6</li></ul><p><b>F = AB'C' + A'BC' + A'CD' + A'B'C</b> (12 literals).</p><p>Just as small: AB'C' + A'BD' + A'BC' + A'B'C.</p>",
"ref": "08 §4",
"form": "sop",
"grp": 3,
"core": false
}
]
},
{
"n": "4.10",
"text": "Four-bit 2's complementer with XOR gates.",
"qs": [
{
"tag": "Mano 4.10 (table) ★",
"type": "tt",
"q": "4-bit 2's complementer: input ABCD (D = LSB), output y₃y₂y₁y₀ = 2's complement of the input. Fill the table.",
"vars": "ABCD",
"outs": {
"y₃": [
0,
1,
1,
1,
1,
1,
1,
1,
1,
0,
0,
0,
0,
0,
0,
0
],
"y₂": [
0,
1,
1,
1,
1,
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
0
],
"y₁": [
0,
1,
1,
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
1,
1,
0
],
"y₀": [
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
1,
0,
1,
0,
1
]
},
"why": "<p>Each output row is 16 − input (and 0 → 0). Shortcut: copy bits from the right up to the first 1, flip the rest.</p>",
"ref": "04 §3",
"grp": 3,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.10 (y₁) ★",
"type": "bool",
"q": "Write output <b>y₁</b> of the 2's complementer (use ⊕).",
"vars": "ABCD",
"ones": [
1,
2,
5,
6,
9,
10,
13,
14
],
"show": "C ⊕ D",
"why": "<p>Bit flips if any lower bit is 1 (that's the shortcut rule): <b>y₁ = C ⊕ D</b>.</p>",
"ref": "04 §3",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.10 (y₂) ★",
"type": "bool",
"q": "Write output <b>y₂</b> of the 2's complementer (use ⊕).",
"vars": "ABCD",
"ones": [
1,
2,
3,
4,
9,
10,
11,
12
],
"show": "B ⊕ (C + D)",
"why": "<p>Bit flips if any lower bit is 1 (that's the shortcut rule): <b>y₂ = B ⊕ (C + D)</b>.</p>",
"ref": "04 §3",
"grp": 3,
"core": true,
"corder": 2
},
{
"tag": "Mano 4.10 (y₃) ★",
"type": "bool",
"q": "Write output <b>y₃</b> of the 2's complementer (use ⊕).",
"vars": "ABCD",
"ones": [
1,
2,
3,
4,
5,
6,
7,
8
],
"show": "A ⊕ (B + C + D)",
"why": "<p>Bit flips if any lower bit is 1 (that's the shortcut rule): <b>y₃ = A ⊕ (B + C + D)</b>.</p><img src='svg/book/c4-10.svg' alt=''><p>5 bits: y₄ = E ⊕ (A + B + C + D), and so on: each bit is XORed with the OR of all bits below it.</p>",
"ref": "04 §3",
"grp": 3,
"core": false
}
]
},
{
"n": "4.11",
"text": "Incrementer and decrementer from four half adders.",
"qs": [
{
"tag": "Mano 4.11 (a)",
"type": "work",
"q": "Design a 4-bit <b>incrementer</b> (adds 1) with four half adders.",
"why": "<p>Adding 1 = adding a carry-in of 1 at the bottom. Each half adder adds one bit A<sub>i</sub> to the carry coming up: S<sub>i</sub> = A<sub>i</sub> ⊕ C<sub>i</sub>, C<sub>i+1</sub> = A<sub>i</sub>C<sub>i</sub>, with C₀ = 1.</p><img src='svg/book/b4-11a.svg' alt=''>",
"ref": "10 §2",
"grp": 4,
"core": false
},
{
"tag": "Mano 4.11 (b)",
"type": "work",
"q": "Design a 4-bit <b>decrementer</b> (subtracts 1) with four half adders.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>A − 1 = (A' + 1)'</td><td>flip, add 1, flip back (A' + 1 = −A in 2's complement… so (A' + 1)' = A − 1)</td></tr><tr><td>2</td><td>so: inverters on the inputs, the incrementer, inverters on the outputs</td><td></td></tr><tr><td>3</td><td>check A = 0110 (6): A' = 1001, +1 = 1010, flip = 0101 = 5 ✓</td><td></td></tr></table><img src='svg/book/b4-11b.svg' alt=''><p>Each stage really computes a borrow: B<sub>i+1</sub> = A<sub>i</sub>'B<sub>i</sub>, which is exactly the half adder's carry when its input is A<sub>i</sub>'.</p>",
"ref": "10 §2",
"grp": 4,
"core": false
}
]
},
{
"n": "4.12",
"text": "Half and full subtractors.",
"qs": [
{
"tag": "Mano 4.12 (a)",
"type": "tt",
"q": "Half subtractor: Diff and B_out for x − y.",
"vars": "xy",
"outs": {
"Diff": [
0,
1,
1,
0
],
"B_out": [
0,
1,
0,
0
]
},
"why": "<p>0 − 1 needs a borrow: Diff = 1, B_out = 1. Otherwise no borrow.</p><p><b>Diff = x ⊕ y</b>, <b>B_out = x'y</b>.</p>",
"ref": "10 §6",
"grp": 4,
"core": false
},
{
"tag": "Mano 4.12 (b · table) ★",
"type": "tt",
"q": "Full subtractor: x − y − B_in. Inputs x, y, z (z = B_in). Fill Diff and B_out.",
"vars": "xyz",
"outs": {
"Diff": [
0,
1,
1,
0,
1,
0,
0,
1
],
"B_out": [
0,
1,
1,
1,
0,
0,
0,
1
]
},
"why": "<p>Work out x − y − z on each row. Negative → borrow 1 (and add 2 to get Diff).</p>",
"ref": "10 §6",
"grp": 4,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.12 (b · Diff) ★",
"type": "bool",
"q": "Full subtractor (z = B_in): write <b>Diff</b>.",
"vars": "xyz",
"ones": [
1,
2,
4,
7
],
"show": "x ⊕ y ⊕ z",
"why": "<p>Same as the full adder's sum: 1 when an odd number of inputs are 1. <b>Diff = x ⊕ y ⊕ B_in</b>.</p>",
"ref": "10 §6",
"grp": 4,
"core": false
},
{
"tag": "Mano 4.12 (b · B_out) ★",
"type": "bool",
"q": "Full subtractor (z = B_in): write a minimal <b>B_out</b>.",
"vars": "xyz",
"ones": [
1,
2,
3,
7
],
"show": "x'y + x'z + yz",
"why": "<p>Borrow rows: 001, 010, 011, 111 → K-map → <b>B_out = x'y + x'z + yz</b>. (Like the adder's carry, but with x complemented.)</p><img src='svg/book/c4-12.svg' alt=''>",
"lits": 6,
"ref": "10 §6",
"grp": 4,
"core": true,
"corder": 2
}
]
},
{
"n": "4.13",
"text": "Adder-subtractor outputs: SUM, C, V.",
"qs": [
{
"tag": "Mano 4.13 (a) ★",
"type": "multi",
"q": "Adder-subtractor: M = 0, A = <code>0111</code>, B = <code>0110</code>. Give the 4 SUM bits, carry C and overflow V.",
"fields": [
{
"label": "SUM",
"ans": [
"1101"
]
},
{
"label": "C",
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
"why": "<p>M = 0 → add: 0111 + 0110 = 0 1101.</p><p>C = <b>0</b> (the 5th bit). V = C₄ ⊕ C₃ = 0 ⊕ 1 = <b>1</b>.</p><p>Signed check: 7 + 6 = 13 → doesn't fit in −8…7, so overflow ✓</p>",
"ref": "10 §6",
"grp": 5,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.13 (b) ★",
"type": "multi",
"q": "Adder-subtractor: M = 0, A = <code>1000</code>, B = <code>1001</code>. Give the 4 SUM bits, carry C and overflow V.",
"fields": [
{
"label": "SUM",
"ans": [
"0001"
]
},
{
"label": "C",
"ans": [
"1"
]
},
{
"label": "V",
"ans": [
"1"
]
}
],
"why": "<p>M = 0 → add: 1000 + 1001 = 1 0001.</p><p>C = <b>1</b> (the 5th bit). V = C₄ ⊕ C₃ = 1 ⊕ 0 = <b>1</b>.</p><p>Signed check: -8 + -7 = -15 → doesn't fit in −8…7, so overflow ✓</p>",
"ref": "10 §6",
"grp": 5,
"core": false
},
{
"tag": "Mano 4.13 (c) ★",
"type": "multi",
"q": "Adder-subtractor: M = 1, A = <code>1100</code>, B = <code>1000</code>. Give the 4 SUM bits, carry C and overflow V.",
"fields": [
{
"label": "SUM",
"ans": [
"0100"
]
},
{
"label": "C",
"ans": [
"1"
]
},
{
"label": "V",
"ans": [
"0"
]
}
],
"why": "<p>M = 1 → subtract: B is XORed with 1 (flipped) and the carry-in is 1: 1100 + 0111 + 1 = 1 0100.</p><p>C = <b>1</b> (the 5th bit). V = C₄ ⊕ C₃ = 1 ⊕ 1 = <b>0</b>.</p><p>Signed check: -4 − -8 = 4 → fits ✓</p>",
"ref": "10 §6",
"grp": 5,
"core": true,
"corder": 2
},
{
"tag": "Mano 4.13 (d) ★",
"type": "multi",
"q": "Adder-subtractor: M = 1, A = <code>0101</code>, B = <code>1010</code>. Give the 4 SUM bits, carry C and overflow V.",
"fields": [
{
"label": "SUM",
"ans": [
"1011"
]
},
{
"label": "C",
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
"why": "<p>M = 1 → subtract: B is XORed with 1 (flipped) and the carry-in is 1: 0101 + 0101 + 1 = 0 1011.</p><p>C = <b>0</b> (the 5th bit). V = C₄ ⊕ C₃ = 0 ⊕ 1 = <b>1</b>.</p><p>Signed check: 5 − -6 = 11 → doesn't fit in −8…7, so overflow ✓</p>",
"ref": "10 §6",
"grp": 5,
"core": false
},
{
"tag": "Mano 4.13 (e) ★",
"type": "multi",
"q": "Adder-subtractor: M = 1, A = <code>0000</code>, B = <code>0001</code>. Give the 4 SUM bits, carry C and overflow V.",
"fields": [
{
"label": "SUM",
"ans": [
"1111"
]
},
{
"label": "C",
"ans": [
"0"
]
},
{
"label": "V",
"ans": [
"0"
]
}
],
"why": "<p>M = 1 → subtract: B is XORed with 1 (flipped) and the carry-in is 1: 0000 + 1110 + 1 = 0 1111.</p><p>C = <b>0</b> (the 5th bit). V = C₄ ⊕ C₃ = 0 ⊕ 0 = <b>0</b>.</p><p>Signed check: 0 − 1 = -1 → fits ✓</p>",
"ref": "10 §6",
"grp": 5,
"core": false
}
]
},
{
"n": "4.14",
"text": "Propagation delay of the 4-bit carry-lookahead adder.",
"qs": [
{
"tag": "Mano 4.14 ★",
"type": "multi",
"q": "XOR delay 10 ns, AND or OR 5 ns. What is the total delay of the 4-bit adder of Fig 4.12 (carry lookahead)?",
"fields": [
{
"label": "delay (ns)",
"ans": [
"30",
"30ns"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>Pᵢ = Aᵢ ⊕ Bᵢ ready at 10 ns</td><td>one XOR (Gᵢ = AᵢBᵢ is ready at 5 ns)</td></tr><tr><td>2</td><td>every carry Cᵢ = AND-OR of P, G, C₀: ready at 10 + 5 + 5 = 20 ns</td><td>lookahead: two levels, no rippling</td></tr><tr><td>3</td><td>Sᵢ = Pᵢ ⊕ Cᵢ: ready at 20 + 10 = 30 ns</td><td>one more XOR</td></tr></table><p>Total <b>30 ns</b>, and it doesn't grow with each extra bit the way ripple carry does.</p>",
"ref": "10 §5",
"grp": 6,
"core": true,
"corder": 1
}
]
},
{
"n": "4.15",
"text": "Two-level expression for C₄.",
"qs": [
{
"tag": "Mano 4.15",
"type": "work",
"q": "Derive the two-level expression for the output carry C₄ of the lookahead carry generator.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>C₁ = G₀ + P₀C₀</td><td>carry out of stage 0</td></tr><tr><td>2</td><td>C₂ = G₁ + P₁C₁ = G₁ + P₁G₀ + P₁P₀C₀</td><td>substitute C₁</td></tr><tr><td>3</td><td>C₃ = G₂ + P₂G₁ + P₂P₁G₀ + P₂P₁P₀C₀</td><td>substitute C₂</td></tr><tr><td>4</td><td><b>C₄ = G₃ + P₃G₂ + P₃P₂G₁ + P₃P₂P₁G₀ + P₃P₂P₁P₀C₀</b></td><td>substitute C₃: one AND per term, one OR</td></tr></table><p>Read it as: a carry comes out if stage 3 makes one, or stage 2 makes one and stage 3 passes it, … or C₀ passes through every stage.</p>",
"ref": "10 §5",
"grp": 6,
"core": true,
"corder": 2
}
]
},
{
"n": "4.16",
"text": "Full adder with P = A + B, G = AB (IC 74283).",
"qs": [
{
"tag": "Mano 4.16",
"type": "work",
"q": "With Pᵢ = Aᵢ + Bᵢ and Gᵢ = AᵢBᵢ, show Cᵢ₊₁ = (Cᵢ'Gᵢ' + Pᵢ')' and Sᵢ = (PᵢGᵢ') ⊕ Cᵢ. Then identify Pᵢ' and Gᵢ' in Fig P4.16.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(Cᵢ'Gᵢ' + Pᵢ')' = (Cᵢ + Gᵢ)Pᵢ</td><td>De Morgan twice</td></tr><tr><td>2</td><td>= PᵢCᵢ + PᵢGᵢ = PᵢCᵢ + Gᵢ</td><td>Gᵢ = AB already means A + B = 1, so PᵢGᵢ = Gᵢ</td></tr><tr><td>3</td><td>= AB + (A + B)C ✓</td><td>that is the full-adder carry</td></tr><tr><td>4</td><td>PᵢGᵢ' = (A + B)(A' + B') = AB' + A'B = A ⊕ B</td><td>so Sᵢ = A ⊕ B ⊕ C ✓</td></tr></table><p>In Fig P4.16: the <b>NAND</b> output (A₀B₀)' is <b>G₀'</b>, the <b>NOR</b> output (A₀ + B₀)' is <b>P₀'</b>. C₁ = NOR(P₀', G₀'C₀') = (P₀' + G₀'C₀')' and S₀ = (G₀'P₀) ⊕ C₀: exactly the two equations, so it is a full adder.</p>",
"ref": "10 §5",
"grp": 6,
"core": false
}
]
},
{
"n": "4.17",
"text": "Lookahead carries in AND-OR-INVERT form (IC 74182).",
"qs": [
{
"tag": "Mano 4.17",
"type": "work",
"q": "Show Cᵢ₊₁ = Gᵢ + PᵢCᵢ = (Gᵢ'Pᵢ' + Gᵢ'Cᵢ')'. Then derive C₂, C₃, C₄ in terms of G', P' and C₁'.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(Gᵢ'Pᵢ' + Gᵢ'Cᵢ')' = (Gᵢ'(Pᵢ' + Cᵢ'))' = Gᵢ + PᵢCᵢ ✓</td><td>De Morgan</td></tr><tr><td>2</td><td>C₂ = (G₁'P₁' + G₁'C₁')'</td><td>i = 1</td></tr><tr><td>3</td><td>C₂' = G₁'P₁' + G₁'C₁'</td><td>keep the complement for the next step</td></tr><tr><td>4</td><td>C₃ = (G₂'P₂' + G₂'C₂')' = (G₂'P₂' + G₂'G₁'P₁' + G₂'G₁'C₁')'</td><td>substitute C₂'</td></tr><tr><td>5</td><td><b>C₄ = (G₃'P₃' + G₃'G₂'P₂' + G₃'G₂'G₁'P₁' + G₃'G₂'G₁'C₁')'</b></td><td>substitute C₃' the same way</td></tr></table><p>Each carry is one AND-OR-INVERT gate fed by the complemented G's, P's and C₁. (Checked on all 128 input combinations.)</p>",
"ref": "10 §5",
"grp": 6,
"core": false
}
]
},
{
"n": "4.18",
"text": "9's complement of a BCD digit.",
"qs": [
{
"tag": "Mano 4.18 (table) ★",
"type": "tt",
"q": "BCD digit ABCD in, its 9's complement wxyz out (10–15 never happen: leave 0 here).",
"vars": "ABCD",
"outs": {
"w": [
1,
1,
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
0,
0,
0
],
"x": [
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
0,
0,
0,
0,
0,
0
],
"y": [
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
0,
0,
0,
0
],
"z": [
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
0,
0,
0,
0,
0
]
},
"why": "<p>Output = 9 − input: 0 → 9 (1001), 1 → 8, … 9 → 0.</p>",
"ref": "09 §1",
"grp": 2,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.18 (w) ★",
"type": "bool",
"q": "9's complementer: minimal SOP for <b>w</b> (10–15 are don't cares).",
"vars": "ABCD",
"ones": [
0,
1
],
"show": "A'B'C'",
"lits": 3,
"why": "<p>F = 1 on cells 0, 1, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-18w.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>A'B'C'</b> from cells 0, 1</li></ul><p><b>F = A'B'C'</b> (3 literals).</p>",
"ref": "09 §1",
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
"tag": "Mano 4.18 (x) ★",
"type": "bool",
"q": "9's complementer: minimal SOP for <b>x</b> (10–15 are don't cares).",
"vars": "ABCD",
"ones": [
2,
3,
4,
5
],
"show": "BC' + B'C",
"lits": 4,
"why": "<p>F = 1 on cells 2, 3, 4, 5, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-18x.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>B'C</b> from cells 2, 3, 10, 11</li><li><b>BC'</b> from cells 4, 5, 12, 13</li></ul><p><b>F = BC' + B'C</b> (4 literals).</p>",
"ref": "09 §1",
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
"corder": 2
},
{
"tag": "Mano 4.18 (y) ★",
"type": "bool",
"q": "9's complementer: minimal SOP for <b>y</b> (10–15 are don't cares).",
"vars": "ABCD",
"ones": [
2,
3,
6,
7
],
"show": "C",
"lits": 1,
"why": "<p>F = 1 on cells 2, 3, 6, 7, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-18y.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>C</b> from cells 2, 3, 6, 7, 10, 11, 14, 15</li></ul><p><b>F = C</b> (1 literal).</p>",
"ref": "09 §1",
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
"tag": "Mano 4.18 (z) ★",
"type": "bool",
"q": "9's complementer: minimal SOP for <b>z</b> (10–15 are don't cares).",
"vars": "ABCD",
"ones": [
0,
2,
4,
6,
8
],
"show": "D'",
"lits": 1,
"why": "<p>F = 1 on cells 0, 2, 4, 6, 8, don't care on 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k4-18z.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges), using an x only if it makes a block bigger:</p><ul><li><b>D'</b> from cells 0, 2, 4, 6, 8, 10, 12, 14</li></ul><p><b>F = D'</b> (1 literal).</p>",
"ref": "09 §1",
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
"n": "4.19",
"text": "BCD adder-subtractor from blocks.",
"qs": [
{
"tag": "Mano 4.19",
"type": "work",
"q": "Build a BCD adder-subtractor from the BCD adder and the 9's complementer of 4.18 (block diagram).",
"why": "<p>Subtraction in decimal = add the <b>10's complement</b> = 9's complement + 1. So: a mode bit M picks B (add) or 9 − B (subtract), and M also feeds the carry-in to supply the +1.</p><img src='svg/book/b4-19.svg' alt=''><p>For several digits, chain them: each stage's Cout feeds the next stage's Cin, and only the lowest stage gets M as its carry-in.</p>",
"ref": "10 §6",
"grp": 5,
"core": false
}
]
},
{
"n": "4.20",
"text": "4-bit × 4-bit multiplier from AND gates and adders.",
"qs": [
{
"tag": "Mano 4.20 (a)",
"type": "work",
"q": "Design a multiplier for two unsigned 4-bit numbers using AND gates and binary adders.",
"why": "<p>Same as long multiplication: each bit Bₖ times A is 4 AND gates (a partial product). Shift each one left by k and add.</p><table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>16 AND gates make the four partial products A·B₀ … A·B₃</td><td>Aᵢ·Bₖ</td></tr><tr><td>2</td><td>C₀ = A₀B₀ straight out</td><td>nothing to add to it</td></tr><tr><td>3</td><td>adder 1: (A·B₀ shifted right 1) + A·B₁ → C₁ is its low bit</td><td>4-bit adder, carry-out joins the next sum</td></tr><tr><td>4</td><td>adder 2: adds A·B₂ → C₂; adder 3: adds A·B₃ → C₃…C₇</td><td>3 adders in total</td></tr></table><img src='svg/book/b4-20.svg' alt=''><p>Result: 8 bits, C₇…C₀. (4 × 4 bits → up to 8 bits: 15 × 15 = 225.)</p>",
"ref": "10 §7",
"grp": 4,
"core": false
}
]
},
{
"n": "4.21",
"text": "4-bit equality comparator.",
"qs": [
{
"tag": "Mano 4.21",
"type": "work",
"q": "Design a circuit that outputs 1 when two 4-bit numbers A and B are equal.",
"why": "<p>Equal means every pair of bits matches. A pair matches when xᵢ = (Aᵢ ⊙ Bᵢ) = AᵢBᵢ + Aᵢ'Bᵢ' = 1 (XNOR).</p><p><b>E = x₃x₂x₁x₀ = (A₃ ⊙ B₃)(A₂ ⊙ B₂)(A₁ ⊙ B₁)(A₀ ⊙ B₀)</b>: four XNORs and a 4-input AND.</p><img src='svg/book/c4-21.svg' alt=''>",
"ref": "10 §1",
"grp": 0,
"core": false
}
]
}
],
"groups": [
{
"name": "XOR and parity",
"blurb": "Odd number of 1s → XOR is 1."
},
{
"name": "Design from a word description",
"blurb": "Words → truth table → K-map → circuit."
},
{
"name": "Code converters",
"blurb": "Table of codes, unused codes as don't cares, one map per output."
},
{
"name": "Bigger converters",
"blurb": "Same method with more outputs."
},
{
"name": "Half and full adders and subtractors",
"blurb": "Sum = XOR, carry/borrow from a 3-variable map."
},
{
"name": "Adder-subtractor and overflow",
"blurb": "M flips B and adds 1; V = C₄ ⊕ C₃."
},
{
"name": "Carry lookahead",
"blurb": "Every carry from G, P and C₀ in two gate levels."
}
]
});
