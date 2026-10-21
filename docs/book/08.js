BOOK.add({
"id": "08",
"title": "Karnaugh maps",
"intro": "Mano 3.1–3.14, 3.26. Answers are checked on every cell and must be as small as the best map grouping.",
"problems": [
{
"n": "3.1",
"text": "Simplify with three-variable maps.",
"qs": [
{
"tag": "Mano 3.1 (a) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(0, 2, 6, 7)</code>",
"vars": "xyz",
"ones": [
0,
2,
6,
7
],
"show": "xy + x'z'",
"lits": 4,
"why": "<p>F = 1 on cells 0, 2, 6, 7.</p><img src='svg/book/k3-1a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'z'</b> from cells 0, 2</li><li><b>xy</b> from cells 6, 7</li></ul><p><b>F = xy + x'z'</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.1 (b) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(0, 2, 3, 4, 6)</code>",
"vars": "xyz",
"ones": [
0,
2,
3,
4,
6
],
"show": "z' + x'y",
"lits": 3,
"why": "<p>F = 1 on cells 0, 2, 3, 4, 6.</p><img src='svg/book/k3-1b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>z'</b> from cells 0, 2, 4, 6</li><li><b>x'y</b> from cells 2, 3</li></ul><p><b>F = z' + x'y</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.1 (c) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(0, 1, 2, 3, 7)</code>",
"vars": "xyz",
"ones": [
0,
1,
2,
3,
7
],
"show": "x' + yz",
"lits": 3,
"why": "<p>F = 1 on cells 0, 1, 2, 3, 7.</p><img src='svg/book/k3-1c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'</b> from cells 0, 1, 2, 3</li><li><b>yz</b> from cells 3, 7</li></ul><p><b>F = x' + yz</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.1 (d) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(3, 5, 6, 7)</code>",
"vars": "xyz",
"ones": [
3,
5,
6,
7
],
"show": "xy + xz + yz",
"lits": 6,
"why": "<p>F = 1 on cells 3, 5, 6, 7.</p><img src='svg/book/k3-1d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>yz</b> from cells 3, 7</li><li><b>xz</b> from cells 5, 7</li><li><b>xy</b> from cells 6, 7</li></ul><p><b>F = xy + xz + yz</b> (6 literals).</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.2",
"text": "Simplify with three-variable maps.",
"qs": [
{
"tag": "Mano 3.2 (a) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(0, 1, 5, 7)</code>",
"vars": "xyz",
"ones": [
0,
1,
5,
7
],
"show": "xz + x'y'",
"lits": 4,
"why": "<p>F = 1 on cells 0, 1, 5, 7.</p><img src='svg/book/k3-2a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y'</b> from cells 0, 1</li><li><b>xz</b> from cells 5, 7</li></ul><p><b>F = xz + x'y'</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.2 (b) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(1, 2, 3, 6, 7)</code>",
"vars": "xyz",
"ones": [
1,
2,
3,
6,
7
],
"show": "y + x'z",
"lits": 3,
"why": "<p>F = 1 on cells 1, 2, 3, 6, 7.</p><img src='svg/book/k3-2b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'z</b> from cells 1, 3</li><li><b>y</b> from cells 2, 3, 6, 7</li></ul><p><b>F = y + x'z</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.2 (c)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(0, 1, 6, 7)</code>",
"vars": "xyz",
"ones": [
0,
1,
6,
7
],
"show": "xy + x'y'",
"lits": 4,
"why": "<p>F = 1 on cells 0, 1, 6, 7.</p><img src='svg/book/k3-2c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y'</b> from cells 0, 1</li><li><b>xy</b> from cells 6, 7</li></ul><p><b>F = xy + x'y'</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.2 (d)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(0, 1, 3, 4, 5)</code>",
"vars": "xyz",
"ones": [
0,
1,
3,
4,
5
],
"show": "y' + x'z",
"lits": 3,
"why": "<p>F = 1 on cells 0, 1, 3, 4, 5.</p><img src='svg/book/k3-2d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>y'</b> from cells 0, 1, 4, 5</li><li><b>x'z</b> from cells 1, 3</li></ul><p><b>F = y' + x'z</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.2 (e)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(1, 3, 5, 7)</code>",
"vars": "xyz",
"ones": [
1,
3,
5,
7
],
"show": "z",
"lits": 1,
"why": "<p>F = 1 on cells 1, 3, 5, 7.</p><img src='svg/book/k3-2e.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>z</b> from cells 1, 3, 5, 7</li></ul><p><b>F = z</b> (1 literal).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.2 (f)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(1, 4, 5, 6, 7)</code>",
"vars": "xyz",
"ones": [
1,
4,
5,
6,
7
],
"show": "x + y'z",
"lits": 3,
"why": "<p>F = 1 on cells 1, 4, 5, 6, 7.</p><img src='svg/book/k3-2f.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>y'z</b> from cells 1, 5</li><li><b>x</b> from cells 4, 5, 6, 7</li></ul><p><b>F = x + y'z</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.3",
"text": "Simplify these expressions with three-variable maps.",
"qs": [
{
"tag": "Mano 3.3 (a) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F = xy + x'y'z' + x'yz'</code>",
"vars": "xyz",
"ones": [
0,
2,
6,
7
],
"show": "xy + x'z'",
"lits": 4,
"why": "<p>Plot each term: xy + x'y'z' + x'yz' → 1s on cells <b>0, 2, 6, 7</b>.</p><img src='svg/book/k3-3a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'z'</b> from cells 0, 2</li><li><b>xy</b> from cells 6, 7</li></ul><p><b>F = xy + x'z'</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.3 (b) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F = x'y' + yz + x'yz'</code>",
"vars": "xyz",
"ones": [
0,
1,
2,
3,
7
],
"show": "x' + yz",
"lits": 3,
"why": "<p>Plot each term: x'y' + yz + x'yz' → 1s on cells <b>0, 1, 2, 3, 7</b>.</p><img src='svg/book/k3-3b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'</b> from cells 0, 1, 2, 3</li><li><b>yz</b> from cells 3, 7</li></ul><p><b>F = x' + yz</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.3 (c) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F = x'y + yz' + y'z'</code>",
"vars": "xyz",
"ones": [
0,
2,
3,
4,
6
],
"show": "z' + x'y",
"lits": 3,
"why": "<p>Plot each term: x'y + yz' + y'z' → 1s on cells <b>0, 2, 3, 4, 6</b>.</p><img src='svg/book/k3-3c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>z'</b> from cells 0, 2, 4, 6</li><li><b>x'y</b> from cells 2, 3</li></ul><p><b>F = z' + x'y</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.3 (d)",
"type": "bool",
"q": "Simplify with a K-map: <code>F = xyz + x'y'z + xy'z'</code>",
"vars": "xyz",
"ones": [
1,
4,
7
],
"show": "xyz + xy'z' + x'y'z",
"lits": 9,
"why": "<p>Plot each term: xyz + x'y'z + xy'z' → 1s on cells <b>1, 4, 7</b>.</p><img src='svg/book/k3-3d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y'z</b> from cells 1</li><li><b>xy'z'</b> from cells 4</li><li><b>xyz</b> from cells 7</li></ul><p><b>F = xyz + xy'z' + x'y'z</b> (9 literals).</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.4",
"text": "Simplify with Karnaugh maps.",
"qs": [
{
"tag": "Mano 3.4 (a) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(x, y, z) = Σ(2, 3, 6, 7)</code>",
"vars": "xyz",
"ones": [
2,
3,
6,
7
],
"show": "y",
"lits": 1,
"why": "<p>F = 1 on cells 2, 3, 6, 7.</p><img src='svg/book/k3-4a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>y</b> from cells 2, 3, 6, 7</li></ul><p><b>F = y</b> (1 literal).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.4 (b) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(A, B, C, D) = Σ(4, 6, 7, 15)</code>",
"vars": "ABCD",
"ones": [
4,
6,
7,
15
],
"show": "BCD + A'BD'",
"lits": 6,
"why": "<p>F = 1 on cells 4, 6, 7, 15.</p><img src='svg/book/k3-4b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'BD'</b> from cells 4, 6</li><li><b>BCD</b> from cells 7, 15</li></ul><p><b>F = BCD + A'BD'</b> (6 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.4 (c) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(A, B, C, D) = Σ(3, 7, 11, 13, 14, 15)</code>",
"vars": "ABCD",
"ones": [
3,
7,
11,
13,
14,
15
],
"show": "CD + ABC + ABD",
"lits": 8,
"why": "<p>F = 1 on cells 3, 7, 11, 13, 14, 15.</p><img src='svg/book/k3-4c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>CD</b> from cells 3, 7, 11, 15</li><li><b>ABD</b> from cells 13, 15</li><li><b>ABC</b> from cells 14, 15</li></ul><p><b>F = CD + ABC + ABD</b> (8 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.4 (d) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(w, x, y, z) = Σ(2, 3, 12, 13, 14, 15)</code>",
"vars": "wxyz",
"ones": [
2,
3,
12,
13,
14,
15
],
"show": "wx + w'x'y",
"lits": 5,
"why": "<p>F = 1 on cells 2, 3, 12, 13, 14, 15.</p><img src='svg/book/k3-4d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>w'x'y</b> from cells 2, 3</li><li><b>wx</b> from cells 12, 13, 14, 15</li></ul><p><b>F = wx + w'x'y</b> (5 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.4 (e)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(w, x, y, z) = Σ(1, 4, 5, 6, 7, 13)</code>",
"vars": "wxyz",
"ones": [
1,
4,
5,
6,
7,
13
],
"show": "w'x + xy'z + w'y'z",
"lits": 8,
"why": "<p>F = 1 on cells 1, 4, 5, 6, 7, 13.</p><img src='svg/book/k3-4e.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>w'y'z</b> from cells 1, 5</li><li><b>w'x</b> from cells 4, 5, 6, 7</li><li><b>xy'z</b> from cells 5, 13</li></ul><p><b>F = w'x + xy'z + w'y'z</b> (8 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.4 (f)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(w, x, y, z) = Σ(0, 1, 5, 8, 9)</code>",
"vars": "wxyz",
"ones": [
0,
1,
5,
8,
9
],
"show": "x'y' + w'y'z",
"lits": 5,
"why": "<p>F = 1 on cells 0, 1, 5, 8, 9.</p><img src='svg/book/k3-4f.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y'</b> from cells 0, 1, 8, 9</li><li><b>w'y'z</b> from cells 1, 5</li></ul><p><b>F = x'y' + w'y'z</b> (5 literals).</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.5",
"text": "Simplify with four-variable maps.",
"qs": [
{
"tag": "Mano 3.5 (a) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(w, x, y, z) = Σ(1, 4, 5, 6, 12, 14, 15)</code>",
"vars": "wxyz",
"ones": [
1,
4,
5,
6,
12,
14,
15
],
"show": "xz' + wxy + w'y'z",
"lits": 8,
"why": "<p>F = 1 on cells 1, 4, 5, 6, 12, 14, 15.</p><img src='svg/book/k3-5a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>w'y'z</b> from cells 1, 5</li><li><b>xz'</b> from cells 4, 6, 12, 14</li><li><b>wxy</b> from cells 14, 15</li></ul><p><b>F = xz' + wxy + w'y'z</b> (8 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.5 (b)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(A, B, C, D) = Σ(1, 5, 9, 10, 11, 14, 15)</code>",
"vars": "ABCD",
"ones": [
1,
5,
9,
10,
11,
14,
15
],
"show": "AC + B'C'D + A'C'D",
"lits": 8,
"why": "<p>F = 1 on cells 1, 5, 9, 10, 11, 14, 15.</p><img src='svg/book/k3-5b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'C'D</b> from cells 1, 5</li><li><b>AC</b> from cells 10, 11, 14, 15</li><li><b>B'C'D</b> from cells 1, 9</li></ul><p><b>F = AC + B'C'D + A'C'D</b> (8 literals).</p><p>Just as small: AC + AB'D + A'C'D.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.5 (c)",
"type": "bool",
"q": "Simplify with a K-map: <code>F(w, x, y, z) = Σ(0, 1, 4, 5, 6, 7, 8, 9)</code>",
"vars": "wxyz",
"ones": [
0,
1,
4,
5,
6,
7,
8,
9
],
"show": "w'x + x'y'",
"lits": 4,
"why": "<p>F = 1 on cells 0, 1, 4, 5, 6, 7, 8, 9.</p><img src='svg/book/k3-5c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>w'x</b> from cells 4, 5, 6, 7</li><li><b>x'y'</b> from cells 0, 1, 8, 9</li></ul><p><b>F = w'x + x'y'</b> (4 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.5 (d) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F(A, B, C, D) = Σ(0, 2, 4, 5, 6, 7, 8, 10, 13, 15)</code>",
"vars": "ABCD",
"ones": [
0,
2,
4,
5,
6,
7,
8,
10,
13,
15
],
"show": "BD + B'D' + A'D'",
"lits": 6,
"why": "<p>F = 1 on cells 0, 2, 4, 5, 6, 7, 8, 10, 13, 15.</p><img src='svg/book/k3-5d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>BD</b> from cells 5, 7, 13, 15</li><li><b>A'D'</b> from cells 0, 2, 4, 6</li></ul><p><b>F = BD + B'D' + A'D'</b> (6 literals).</p><p>Just as small: BD + A'B + B'D'.</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.6",
"text": "Simplify these expressions with four-variable maps.",
"qs": [
{
"tag": "Mano 3.6 (a) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F = A'B'C'D' + AC'D' + B'CD' + A'BCD + BC'D</code>",
"vars": "ABCD",
"ones": [
0,
2,
5,
7,
8,
10,
12,
13
],
"show": "B'D' + ABC' + A'BD",
"lits": 8,
"why": "<p>Plot each term: A'B'C'D' + AC'D' + B'CD' + A'BCD + BC'D → 1s on cells <b>0, 2, 5, 7, 8, 10, 12, 13</b>.</p><img src='svg/book/k3-6a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>A'BD</b> from cells 5, 7</li><li><b>ABC'</b> from cells 12, 13</li></ul><p><b>F = B'D' + ABC' + A'BD</b> (8 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.6 (b) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F = x'z + w'xy' + w(x'y + xy')</code>",
"vars": "wxyz",
"ones": [
1,
3,
4,
5,
9,
10,
11,
12,
13
],
"show": "xy' + x'z + wx'y",
"lits": 7,
"why": "<p>Plot each term: x'z + w'xy' + w(x'y + xy') → 1s on cells <b>1, 3, 4, 5, 9, 10, 11, 12, 13</b>.</p><img src='svg/book/k3-6b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'z</b> from cells 1, 3, 9, 11</li><li><b>xy'</b> from cells 4, 5, 12, 13</li><li><b>wx'y</b> from cells 10, 11</li></ul><p><b>F = xy' + x'z + wx'y</b> (7 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.6 (c)",
"type": "bool",
"q": "Simplify with a K-map: <code>F = A'B'C'D' + A'CD' + AB'D' + ABCD + A'BD</code>",
"vars": "ABCD",
"ones": [
0,
2,
5,
6,
7,
8,
10,
15
],
"show": "B'D' + BCD + A'BD + A'CD'",
"lits": 11,
"why": "<p>Plot each term: A'B'C'D' + A'CD' + AB'D' + ABCD + A'BD → 1s on cells <b>0, 2, 5, 6, 7, 8, 10, 15</b>.</p><img src='svg/book/k3-6c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>A'BD</b> from cells 5, 7</li><li><b>BCD</b> from cells 7, 15</li><li><b>A'CD'</b> from cells 2, 6</li></ul><p><b>F = B'D' + BCD + A'BD + A'CD'</b> (11 literals).</p><p>Just as small: B'D' + BCD + A'BC + A'BD.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.6 (d)",
"type": "bool",
"q": "Simplify with a K-map: <code>F = A'B'C'D' + AB'C + B'CD' + ABCD' + BC'D</code>",
"vars": "ABCD",
"ones": [
0,
2,
5,
10,
11,
13,
14
],
"show": "ACD' + AB'C + BC'D + A'B'D'",
"lits": 12,
"why": "<p>Plot each term: A'B'C'D' + AB'C + B'CD' + ABCD' + BC'D → 1s on cells <b>0, 2, 5, 10, 11, 13, 14</b>.</p><img src='svg/book/k3-6d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'B'D'</b> from cells 0, 2</li><li><b>BC'D</b> from cells 5, 13</li><li><b>AB'C</b> from cells 10, 11</li><li><b>ACD'</b> from cells 10, 14</li></ul><p><b>F = ACD' + AB'C + BC'D + A'B'D'</b> (12 literals).</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.7",
"text": "Simplify these expressions with four-variable maps.",
"qs": [
{
"tag": "Mano 3.7 (a) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F = w'z + xz + x'y + wx'z</code>",
"vars": "wxyz",
"ones": [
1,
2,
3,
5,
7,
9,
10,
11,
13,
15
],
"show": "z + x'y",
"lits": 3,
"why": "<p>Plot each term: w'z + xz + x'y + wx'z → 1s on cells <b>1, 2, 3, 5, 7, 9, 10, 11, 13, 15</b>.</p><img src='svg/book/k3-7a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>z</b> from cells 1, 3, 5, 7, 9, 11, 13, 15</li><li><b>x'y</b> from cells 2, 3, 10, 11</li></ul><p><b>F = z + x'y</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.7 (b)",
"type": "bool",
"q": "Simplify with a K-map: <code>F = C'D + A'B'C + ABC' + AB'C</code>",
"vars": "ABCD",
"ones": [
1,
2,
3,
5,
9,
10,
11,
12,
13
],
"show": "B'C + C'D + ABC'",
"lits": 7,
"why": "<p>Plot each term: C'D + A'B'C + ABC' + AB'C → 1s on cells <b>1, 2, 3, 5, 9, 10, 11, 12, 13</b>.</p><img src='svg/book/k3-7b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'C</b> from cells 2, 3, 10, 11</li><li><b>C'D</b> from cells 1, 5, 9, 13</li><li><b>ABC'</b> from cells 12, 13</li></ul><p><b>F = B'C + C'D + ABC'</b> (7 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.7 (c) ★",
"type": "bool",
"q": "Simplify with a K-map: <code>F = AB'C + B'C'D' + BCD + ACD' + A'B'C + A'BC'D</code>",
"vars": "ABCD",
"ones": [
0,
2,
3,
5,
7,
8,
10,
11,
14,
15
],
"show": "AC + CD + B'D' + A'BD",
"lits": 9,
"why": "<p>Plot each term: AB'C + B'C'D' + BCD + ACD' + A'B'C + A'BC'D → 1s on cells <b>0, 2, 3, 5, 7, 8, 10, 11, 14, 15</b>.</p><img src='svg/book/k3-7c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>A'BD</b> from cells 5, 7</li><li><b>AC</b> from cells 10, 11, 14, 15</li><li><b>CD</b> from cells 3, 7, 11, 15</li></ul><p><b>F = AC + CD + B'D' + A'BD</b> (9 literals).</p><p>Just as small: AC + B'C + B'D' + A'BD.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.7 (d)",
"type": "bool",
"q": "Simplify with a K-map: <code>F = xyz + wy + wxy' + x'y</code>",
"vars": "wxyz",
"ones": [
2,
3,
7,
10,
11,
12,
13,
14,
15
],
"show": "wx + yz + x'y",
"lits": 6,
"why": "<p>Plot each term: xyz + wy + wxy' + x'y → 1s on cells <b>2, 3, 7, 10, 11, 12, 13, 14, 15</b>.</p><img src='svg/book/k3-7d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'y</b> from cells 2, 3, 10, 11</li><li><b>yz</b> from cells 3, 7, 11, 15</li><li><b>wx</b> from cells 12, 13, 14, 15</li></ul><p><b>F = wx + yz + x'y</b> (6 literals).</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.8",
"text": "Find the minterms by plotting each function in a map.",
"qs": [
{
"tag": "Mano 3.8 (a) ★",
"type": "multi",
"q": "Plot <code>F = xy + yz + xy'z</code> on a map and list its minterms (numbers, smallest first).",
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
}
],
"why": "<p>Each term covers every cell where its letters match (missing letters = both values):</p><ul><li><b>xy</b> → 6, 7</li><li><b>yz</b> → 3, 7</li><li><b>xy'z</b> → 5</li></ul><img src='svg/book/k3-8a.svg' alt=''><p><b>F = Σ(3, 5, 6, 7)</b>. Cells hit by two terms only count once.</p>",
"ref": "08 §6"
},
{
"tag": "Mano 3.8 (b) ★",
"type": "multi",
"q": "Plot <code>F = C'D + ABC' + ABD' + A'B'D</code> on a map and list its minterms (numbers, smallest first).",
"fields": [
{
"label": "Σm(",
"ans": [
"1,3,5,9,12,13,14",
"(1,3,5,9,12,13,14)",
"Σ(1,3,5,9,12,13,14)",
"Σm(1,3,5,9,12,13,14)",
"m(1,3,5,9,12,13,14)",
"Π(1,3,5,9,12,13,14)",
"ΠM(1,3,5,9,12,13,14)",
"M(1,3,5,9,12,13,14)"
]
}
],
"why": "<p>Each term covers every cell where its letters match (missing letters = both values):</p><ul><li><b>C'D</b> → 1, 5, 9, 13</li><li><b>ABC'</b> → 12, 13</li><li><b>ABD'</b> → 12, 14</li><li><b>A'B'D</b> → 1, 3</li></ul><img src='svg/book/k3-8b.svg' alt=''><p><b>F = Σ(1, 3, 5, 9, 12, 13, 14)</b>. Cells hit by two terms only count once.</p>",
"ref": "08 §6"
},
{
"tag": "Mano 3.8 (c)",
"type": "multi",
"q": "Plot <code>F = wyz + w'x' + wxz'</code> on a map and list its minterms (numbers, smallest first).",
"fields": [
{
"label": "Σm(",
"ans": [
"0,1,2,3,11,12,14,15",
"(0,1,2,3,11,12,14,15)",
"Σ(0,1,2,3,11,12,14,15)",
"Σm(0,1,2,3,11,12,14,15)",
"m(0,1,2,3,11,12,14,15)",
"Π(0,1,2,3,11,12,14,15)",
"ΠM(0,1,2,3,11,12,14,15)",
"M(0,1,2,3,11,12,14,15)"
]
}
],
"why": "<p>Each term covers every cell where its letters match (missing letters = both values):</p><ul><li><b>wyz</b> → 11, 15</li><li><b>w'x'</b> → 0, 1, 2, 3</li><li><b>wxz'</b> → 12, 14</li></ul><img src='svg/book/k3-8c.svg' alt=''><p><b>F = Σ(0, 1, 2, 3, 11, 12, 14, 15)</b>. Cells hit by two terms only count once.</p>",
"ref": "08 §6"
},
{
"tag": "Mano 3.8 (d)",
"type": "multi",
"q": "Plot <code>F = A'B + A'CD + B'CD + BC'D'</code> on a map and list its minterms (numbers, smallest first).",
"fields": [
{
"label": "Σm(",
"ans": [
"3,4,5,6,7,11,12",
"(3,4,5,6,7,11,12)",
"Σ(3,4,5,6,7,11,12)",
"Σm(3,4,5,6,7,11,12)",
"m(3,4,5,6,7,11,12)",
"Π(3,4,5,6,7,11,12)",
"ΠM(3,4,5,6,7,11,12)",
"M(3,4,5,6,7,11,12)"
]
}
],
"why": "<p>Each term covers every cell where its letters match (missing letters = both values):</p><ul><li><b>A'B</b> → 4, 5, 6, 7</li><li><b>A'CD</b> → 3, 7</li><li><b>B'CD</b> → 3, 11</li><li><b>BC'D'</b> → 4, 12</li></ul><img src='svg/book/k3-8d.svg' alt=''><p><b>F = Σ(3, 4, 5, 6, 7, 11, 12)</b>. Cells hit by two terms only count once.</p>",
"ref": "08 §6"
}
]
},
{
"n": "3.9",
"text": "Find all prime implicants and which are essential.",
"qs": [
{
"tag": "Mano 3.9 (a) ★",
"type": "work",
"q": "Find all the prime implicants of <code>F(w, x, y, z) = Σ(0, 2, 4, 5, 6, 7, 8, 10, 13, 15)</code> and say which are essential.",
"why": "<img src='svg/book/k3-9a.svg' alt='prime implicants'><p><b>Prime implicants</b> (4): x'z', xz, w'z', w'x.</p><p>A prime implicant is a block that can't be made any bigger. It is <b>essential</b> if it is the only block covering some 1.</p><p><b>Essential</b> (2): x'z', xz.</p><ul><li><b>x'z'</b> is the only prime covering cells 8, 10</li><li><b>xz</b> is the only prime covering cells 13, 15</li></ul>",
"ref": "08 §2"
},
{
"tag": "Mano 3.9 (b) ★",
"type": "work",
"q": "Find all the prime implicants of <code>F(A, B, C, D) = Σ(0, 2, 3, 5, 7, 8, 10, 11, 14, 15)</code> and say which are essential.",
"why": "<img src='svg/book/k3-9b.svg' alt='prime implicants'><p><b>Prime implicants</b> (5): CD, B'D', B'C, AC, A'BD.</p><p>A prime implicant is a block that can't be made any bigger. It is <b>essential</b> if it is the only block covering some 1.</p><p><b>Essential</b> (3): B'D', A'BD, AC.</p><ul><li><b>B'D'</b> is the only prime covering cells 0, 8</li><li><b>A'BD</b> is the only prime covering cell 5</li><li><b>AC</b> is the only prime covering cell 14</li></ul>",
"ref": "08 §2"
},
{
"tag": "Mano 3.9 (c)",
"type": "work",
"q": "Find all the prime implicants of <code>F(A, B, C, D) = Σ(1, 3, 4, 5, 10, 11, 12, 13, 14, 15)</code> and say which are essential.",
"why": "<img src='svg/book/k3-9c.svg' alt='prime implicants'><p><b>Prime implicants</b> (6): BC', B'CD, AC, A'C'D, AB, A'B'D.</p><p>A prime implicant is a block that can't be made any bigger. It is <b>essential</b> if it is the only block covering some 1.</p><p><b>Essential</b> (2): BC', AC.</p><ul><li><b>BC'</b> is the only prime covering cell 4</li><li><b>AC</b> is the only prime covering cell 10</li></ul>",
"ref": "08 §2"
},
{
"tag": "Mano 3.9 (d)",
"type": "work",
"q": "Find all the prime implicants of <code>F(w, x, y, z) = Σ(1, 3, 6, 7, 8, 9, 12, 13, 14, 15)</code> and say which are essential.",
"why": "<img src='svg/book/k3-9d.svg' alt='prime implicants'><p><b>Prime implicants</b> (6): xy, x'y'z, wy', w'yz, wx, w'x'z.</p><p>A prime implicant is a block that can't be made any bigger. It is <b>essential</b> if it is the only block covering some 1.</p><p><b>Essential</b> (2): xy, wy'.</p><ul><li><b>xy</b> is the only prime covering cell 6</li><li><b>wy'</b> is the only prime covering cell 8</li></ul>",
"ref": "08 §2"
},
{
"tag": "Mano 3.9 (e)",
"type": "work",
"q": "Find all the prime implicants of <code>F(A, B, C, D) = Σ(0, 2, 3, 5, 7, 8, 10, 11, 13, 15)</code> and say which are essential.",
"why": "<img src='svg/book/k3-9e.svg' alt='prime implicants'><p><b>Prime implicants</b> (4): CD, B'D', BD, B'C.</p><p>A prime implicant is a block that can't be made any bigger. It is <b>essential</b> if it is the only block covering some 1.</p><p><b>Essential</b> (2): B'D', BD.</p><ul><li><b>B'D'</b> is the only prime covering cells 0, 8</li><li><b>BD</b> is the only prime covering cells 5, 13</li></ul>",
"ref": "08 §2"
},
{
"tag": "Mano 3.9 (f)",
"type": "work",
"q": "Find all the prime implicants of <code>F(w, x, y, z) = Σ(0, 2, 7, 8, 9, 10, 12, 13, 14, 15)</code> and say which are essential.",
"why": "<img src='svg/book/k3-9f.svg' alt='prime implicants'><p><b>Prime implicants</b> (5): x'z', xyz, wz', wy', wx.</p><p>A prime implicant is a block that can't be made any bigger. It is <b>essential</b> if it is the only block covering some 1.</p><p><b>Essential</b> (3): x'z', xyz, wy'.</p><ul><li><b>x'z'</b> is the only prime covering cells 0, 2</li><li><b>xyz</b> is the only prime covering cell 7</li><li><b>wy'</b> is the only prime covering cell 9</li></ul>",
"ref": "08 §2"
}
]
},
{
"n": "3.10",
"text": "Simplify by first finding the essential prime implicants.",
"qs": [
{
"tag": "Mano 3.10 (a)",
"type": "bool",
"q": "Simplify by first finding the essential prime implicants: <code>F(w, x, y, z) = Σ(0, 2, 4, 5, 6, 7, 8, 10, 13, 15)</code>",
"vars": "wxyz",
"ones": [
0,
2,
4,
5,
6,
7,
8,
10,
13,
15
],
"show": "xz + x'z' + w'z'",
"lits": 6,
"why": "<p>F = 1 on cells 0, 2, 4, 5, 6, 7, 8, 10, 13, 15.</p><img src='svg/book/k3-10a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'z'</b> from cells 0, 2, 8, 10</li><li><b>xz</b> from cells 5, 7, 13, 15</li><li><b>w'z'</b> from cells 0, 2, 4, 6</li></ul><p><b>F = xz + x'z' + w'z'</b> (6 literals).</p><p>Just as small: xz + w'x + x'z'.</p><p>Start with the essential primes (x'z', xz), then cover any 1s left with the fewest extra primes.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.10 (b)",
"type": "bool",
"q": "Simplify by first finding the essential prime implicants: <code>F(A, B, C, D) = Σ(0, 2, 3, 5, 7, 8, 10, 11, 14, 15)</code>",
"vars": "ABCD",
"ones": [
0,
2,
3,
5,
7,
8,
10,
11,
14,
15
],
"show": "AC + CD + B'D' + A'BD",
"lits": 9,
"why": "<p>F = 1 on cells 0, 2, 3, 5, 7, 8, 10, 11, 14, 15.</p><img src='svg/book/k3-10b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>A'BD</b> from cells 5, 7</li><li><b>AC</b> from cells 10, 11, 14, 15</li><li><b>CD</b> from cells 3, 7, 11, 15</li></ul><p><b>F = AC + CD + B'D' + A'BD</b> (9 literals).</p><p>Just as small: AC + B'C + B'D' + A'BD.</p><p>Start with the essential primes (B'D', A'BD, AC), then cover any 1s left with the fewest extra primes.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.10 (c) ★",
"type": "bool",
"q": "Simplify by first finding the essential prime implicants: <code>F(A, B, C, D) = Σ(1, 3, 4, 5, 10, 11, 12, 13, 14, 15)</code>",
"vars": "ABCD",
"ones": [
1,
3,
4,
5,
10,
11,
12,
13,
14,
15
],
"show": "AC + BC' + A'B'D",
"lits": 7,
"why": "<p>F = 1 on cells 1, 3, 4, 5, 10, 11, 12, 13, 14, 15.</p><img src='svg/book/k3-10c.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>BC'</b> from cells 4, 5, 12, 13</li><li><b>AC</b> from cells 10, 11, 14, 15</li><li><b>A'B'D</b> from cells 1, 3</li></ul><p><b>F = AC + BC' + A'B'D</b> (7 literals).</p><p>Start with the essential primes (BC', AC), then cover any 1s left with the fewest extra primes.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.10 (d)",
"type": "bool",
"q": "Simplify by first finding the essential prime implicants: <code>F(w, x, y, z) = Σ(1, 3, 6, 7, 8, 9, 12, 13, 14, 15)</code>",
"vars": "wxyz",
"ones": [
1,
3,
6,
7,
8,
9,
12,
13,
14,
15
],
"show": "wy' + xy + w'x'z",
"lits": 7,
"why": "<p>F = 1 on cells 1, 3, 6, 7, 8, 9, 12, 13, 14, 15.</p><img src='svg/book/k3-10d.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>xy</b> from cells 6, 7, 14, 15</li><li><b>wy'</b> from cells 8, 9, 12, 13</li><li><b>w'x'z</b> from cells 1, 3</li></ul><p><b>F = wy' + xy + w'x'z</b> (7 literals).</p><p>Start with the essential primes (xy, wy'), then cover any 1s left with the fewest extra primes.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.10 (e)",
"type": "bool",
"q": "Simplify by first finding the essential prime implicants: <code>F(A, B, C, D) = Σ(0, 2, 3, 5, 7, 8, 10, 11, 13, 15)</code>",
"vars": "ABCD",
"ones": [
0,
2,
3,
5,
7,
8,
10,
11,
13,
15
],
"show": "BD + CD + B'D'",
"lits": 6,
"why": "<p>F = 1 on cells 0, 2, 3, 5, 7, 8, 10, 11, 13, 15.</p><img src='svg/book/k3-10e.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>B'D'</b> from cells 0, 2, 8, 10</li><li><b>BD</b> from cells 5, 7, 13, 15</li><li><b>CD</b> from cells 3, 7, 11, 15</li></ul><p><b>F = BD + CD + B'D'</b> (6 literals).</p><p>Just as small: BD + B'C + B'D'.</p><p>Start with the essential primes (B'D', BD), then cover any 1s left with the fewest extra primes.</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.10 (f)",
"type": "bool",
"q": "Simplify by first finding the essential prime implicants: <code>F(w, x, y, z) = Σ(0, 2, 7, 8, 9, 10, 12, 13, 14, 15)</code>",
"vars": "wxyz",
"ones": [
0,
2,
7,
8,
9,
10,
12,
13,
14,
15
],
"show": "wz' + wy' + x'z' + xyz",
"lits": 9,
"why": "<p>F = 1 on cells 0, 2, 7, 8, 9, 10, 12, 13, 14, 15.</p><img src='svg/book/k3-10f.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>x'z'</b> from cells 0, 2, 8, 10</li><li><b>xyz</b> from cells 7, 15</li><li><b>wy'</b> from cells 8, 9, 12, 13</li><li><b>wz'</b> from cells 8, 10, 12, 14</li></ul><p><b>F = wz' + wy' + x'z' + xyz</b> (9 literals).</p><p>Just as small: wx + wy' + x'z' + xyz.</p><p>Start with the essential primes (x'z', xyz, wy'), then cover any 1s left with the fewest extra primes.</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.11",
"text": "Simplify with five-variable maps.",
"qs": [
{
"tag": "Mano 3.11 (a) ★",
"type": "bool",
"q": "Simplify with a five-variable map: <code>F(A, B, C, D, E) = Σ(0, 1, 4, 5, 16, 17, 21, 25, 29)</code>",
"vars": "ABCDE",
"ones": [
0,
1,
4,
5,
16,
17,
21,
25,
29
],
"show": "AD'E + B'C'D' + A'B'D'",
"lits": 9,
"why": "<p>F = 1 on cells 0, 1, 4, 5, 16, 17, 21, 25, 29.</p><img src='svg/book/k3-11a.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'B'D'</b> from cells 0, 1, 4, 5</li><li><b>B'C'D'</b> from cells 0, 1, 16, 17</li><li><b>AD'E</b> from cells 17, 21, 25, 29</li></ul><p><b>F = AD'E + B'C'D' + A'B'D'</b> (9 literals).</p><p>Five variables = two 4-variable maps, one for A = 0 and one for A = 1. A block may use the <b>same cells in both maps</b> (then A drops out).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.11 (b)",
"type": "bool",
"q": "Simplify with a five-variable map: <code>F = A'B'CE' + B'C'D'E' + A'B'D' + B'CD' + A'CD + A'BD</code> (the book prints F(A, B, C, D) but it uses A to E)",
"vars": "ABCDE",
"ones": [
0,
1,
4,
5,
6,
7,
10,
11,
14,
15,
16,
20,
21
],
"show": "A'BD + A'CD + B'CD' + B'D'E' + A'B'D'",
"lits": 15,
"why": "<p>Plot each term on the A = 0 and A = 1 maps → 1s on cells <b>0, 1, 4, 5, 6, 7, 10, 11, 14, 15, 16, 20, 21</b>.</p><img src='svg/book/k3-11b.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'B'D'</b> from cells 0, 1, 4, 5</li><li><b>A'BD</b> from cells 10, 11, 14, 15</li><li><b>B'D'E'</b> from cells 0, 4, 16, 20</li><li><b>B'CD'</b> from cells 4, 5, 20, 21</li><li><b>A'CD</b> from cells 6, 7, 14, 15</li></ul><p><b>F = A'BD + A'CD + B'CD' + B'D'E' + A'B'D'</b> (15 literals).</p><p>Just as small: A'BD + B'CD' + A'B'C + B'D'E' + A'B'D'.</p>",
"ref": "08 §3",
"form": "sop"
}
]
},
{
"n": "3.12",
"text": "Simplify to product-of-sums form.",
"qs": [
{
"tag": "Mano 3.12 (a)",
"type": "bool",
"q": "Simplify to <b>product-of-sums</b> form: <code>F(w, x, y, z) = Σ(0, 1, 2, 5, 8, 10, 13)</code>",
"vars": "wxyz",
"ones": [
0,
1,
2,
5,
8,
10,
13
],
"show": "(y' + z')(x' + z)(w' + x + z')",
"lits": 7,
"why": "<p>F = 0 on cells <b>3, 4, 6, 7, 9, 11, 12, 14, 15</b>. For POS you group the <b>0s</b>.</p><img src='svg/book/k3-12a.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(y' + z')</b> from cells 3, 7, 11, 15</li><li><b>(x' + z)</b> from cells 4, 6, 12, 14</li><li><b>(w' + x + z')</b> from cells 9, 11</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (y' + z')(x' + z)(w' + x + z')</b> (7 literals).</p>",
"ref": "08 §5",
"form": "pos"
},
{
"tag": "Mano 3.12 (b) ★",
"type": "bool",
"q": "Simplify to <b>product-of-sums</b> form: <code>F(A, B, C, D) = Π(1, 3, 5, 7, 13, 15)</code>",
"vars": "ABCD",
"ones": [
0,
2,
4,
6,
8,
9,
10,
11,
12,
14
],
"show": "(A + D')(B' + D')",
"lits": 4,
"why": "<p>F = 0 on cells <b>1, 3, 5, 7, 13, 15</b>. For POS you group the <b>0s</b>.</p><img src='svg/book/k3-12b.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(A + D')</b> from cells 1, 3, 5, 7</li><li><b>(B' + D')</b> from cells 5, 7, 13, 15</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (A + D')(B' + D')</b> (4 literals).</p>",
"ref": "08 §5",
"form": "pos"
},
{
"tag": "Mano 3.12 (c)",
"type": "bool",
"q": "Simplify to <b>product-of-sums</b> form: <code>F(A, B, C, D) = Π(1, 3, 6, 9, 11, 12, 14)</code>",
"vars": "ABCD",
"ones": [
0,
2,
4,
5,
7,
8,
10,
13,
15
],
"show": "(B + D')(B' + C' + D)(A' + B' + D)",
"lits": 8,
"why": "<p>F = 0 on cells <b>1, 3, 6, 9, 11, 12, 14</b>. For POS you group the <b>0s</b>.</p><img src='svg/book/k3-12c.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(B + D')</b> from cells 1, 3, 9, 11</li><li><b>(B' + C' + D)</b> from cells 6, 14</li><li><b>(A' + B' + D)</b> from cells 12, 14</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (B + D')(B' + C' + D)(A' + B' + D)</b> (8 literals).</p>",
"ref": "08 §5",
"form": "pos"
}
]
},
{
"n": "3.13",
"text": "Simplify to (1) sum of products and (2) product of sums.",
"qs": [
{
"tag": "Mano 3.13 (a · SOP) ★",
"type": "bool",
"q": "Simplify <code>x'z' + y'z' + yz' + xy</code> to <b>sum of products</b>.",
"vars": "xyz",
"ones": [
0,
2,
4,
6,
7
],
"show": "z' + xy",
"lits": 3,
"why": "<p>Plot it: 1s on cells <b>0, 2, 4, 6, 7</b>.</p><img src='svg/book/k3-13as.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>z'</b> from cells 0, 2, 4, 6</li><li><b>xy</b> from cells 6, 7</li></ul><p><b>F = z' + xy</b> (3 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.13 (a · POS) ★",
"type": "bool",
"q": "Simplify <code>x'z' + y'z' + yz' + xy</code> to <b>product of sums</b>.",
"vars": "xyz",
"ones": [
0,
2,
4,
6,
7
],
"show": "(x + z')(y + z')",
"lits": 4,
"why": "<p>Same map, now group the 0s: cells <b>1, 3, 5</b>.</p><img src='svg/book/k3-13ap.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(x + z')</b> from cells 1, 3</li><li><b>(y + z')</b> from cells 1, 5</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (x + z')(y + z')</b> (4 literals).</p>",
"ref": "08 §5",
"form": "pos"
},
{
"tag": "Mano 3.13 (b · SOP)",
"type": "bool",
"q": "Simplify <code>ACD' + C'D + AB' + ABCD</code> to <b>sum of products</b>.",
"vars": "ABCD",
"ones": [
1,
5,
8,
9,
10,
11,
13,
14,
15
],
"show": "AC + AB' + C'D",
"lits": 6,
"why": "<p>Plot it: 1s on cells <b>1, 5, 8, 9, 10, 11, 13, 14, 15</b>.</p><img src='svg/book/k3-13bs.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>C'D</b> from cells 1, 5, 9, 13</li><li><b>AB'</b> from cells 8, 9, 10, 11</li><li><b>AC</b> from cells 10, 11, 14, 15</li></ul><p><b>F = AC + AB' + C'D</b> (6 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.13 (b · POS)",
"type": "bool",
"q": "Simplify <code>ACD' + C'D + AB' + ABCD</code> to <b>product of sums</b>.",
"vars": "ABCD",
"ones": [
1,
5,
8,
9,
10,
11,
13,
14,
15
],
"show": "(A + D)(A + C')(B' + C + D)",
"lits": 7,
"why": "<p>Same map, now group the 0s: cells <b>0, 2, 3, 4, 6, 7, 12</b>.</p><img src='svg/book/k3-13bp.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(A + D)</b> from cells 0, 2, 4, 6</li><li><b>(A + C')</b> from cells 2, 3, 6, 7</li><li><b>(B' + C + D)</b> from cells 4, 12</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (A + D)(A + C')(B' + C + D)</b> (7 literals).</p>",
"ref": "08 §5",
"form": "pos"
},
{
"tag": "Mano 3.13 (c · SOP)",
"type": "bool",
"q": "Simplify <code>(A + C' + D')(A' + B' + D')(A' + B + D')(A' + B + C')</code> to <b>sum of products</b>.",
"vars": "ABCD",
"ones": [
0,
1,
2,
4,
5,
6,
8,
12,
14
],
"show": "BD' + C'D' + A'D' + A'C'",
"lits": 8,
"why": "<p>Plot it: 1s on cells <b>0, 1, 2, 4, 5, 6, 8, 12, 14</b>.</p><img src='svg/book/k3-13cs.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>A'C'</b> from cells 0, 1, 4, 5</li><li><b>A'D'</b> from cells 0, 2, 4, 6</li><li><b>C'D'</b> from cells 0, 4, 8, 12</li><li><b>BD'</b> from cells 4, 6, 12, 14</li></ul><p><b>F = BD' + C'D' + A'D' + A'C'</b> (8 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.13 (c · POS)",
"type": "bool",
"q": "Simplify <code>(A + C' + D')(A' + B' + D')(A' + B + D')(A' + B + C')</code> to <b>product of sums</b>.",
"vars": "ABCD",
"ones": [
0,
1,
2,
4,
5,
6,
8,
12,
14
],
"show": "(C' + D')(A' + D')(A' + B + C')",
"lits": 7,
"why": "<p>Same map, now group the 0s: cells <b>3, 7, 9, 10, 11, 13, 15</b>.</p><img src='svg/book/k3-13cp.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(C' + D')</b> from cells 3, 7, 11, 15</li><li><b>(A' + D')</b> from cells 9, 11, 13, 15</li><li><b>(A' + B + C')</b> from cells 10, 11</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (C' + D')(A' + D')(A' + B + C')</b> (7 literals).</p>",
"ref": "08 §5",
"form": "pos"
},
{
"tag": "Mano 3.13 (d · SOP)",
"type": "bool",
"q": "Simplify <code>ABC' + AB'D + BCD</code> to <b>sum of products</b>.",
"vars": "ABCD",
"ones": [
7,
9,
11,
12,
13,
15
],
"show": "AD + ABC' + BCD",
"lits": 8,
"why": "<p>Plot it: 1s on cells <b>7, 9, 11, 12, 13, 15</b>.</p><img src='svg/book/k3-13ds.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>BCD</b> from cells 7, 15</li><li><b>AD</b> from cells 9, 11, 13, 15</li><li><b>ABC'</b> from cells 12, 13</li></ul><p><b>F = AD + ABC' + BCD</b> (8 literals).</p>",
"ref": "08 §3",
"form": "sop"
},
{
"tag": "Mano 3.13 (d · POS)",
"type": "bool",
"q": "Simplify <code>ABC' + AB'D + BCD</code> to <b>product of sums</b>.",
"vars": "ABCD",
"ones": [
7,
9,
11,
12,
13,
15
],
"show": "(A + B)(A + C)(B + D)(C' + D)",
"lits": 8,
"why": "<p>Same map, now group the 0s: cells <b>0, 1, 2, 3, 4, 5, 6, 8, 10, 14</b>.</p><img src='svg/book/k3-13dp.svg' alt='grouped K-map'><p>Group the 0s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>(A + B)</b> from cells 0, 1, 2, 3</li><li><b>(A + C)</b> from cells 0, 1, 4, 5</li><li><b>(B + D)</b> from cells 0, 2, 8, 10</li><li><b>(C' + D)</b> from cells 2, 6, 10, 14</li></ul><p>Each group of 0s gives one OR term: a letter that is 0 across the group appears plain, a 1 appears barred.</p><p><b>F = (A + B)(A + C)(B + D)(C' + D)</b> (8 literals).</p>",
"ref": "08 §5",
"form": "pos"
}
]
},
{
"n": "3.14",
"text": "Three ways to write F with eight or fewer literals.",
"qs": [
{
"tag": "Mano 3.14",
"type": "bool",
"q": "<code>F = B'C'D' + AB'CD' + BC'D + A'BCD</code>. Write F with <b>8 or fewer literals</b> (any form: brackets, ⊕ for XOR and ⊙ for XNOR are fine).",
"vars": "ABCD",
"ones": [
0,
5,
7,
8,
10,
13
],
"show": "B'D'(A + C') + BD(A' + C')",
"why": "<p>F = Σ(0, 5, 7, 8, 10, 13). The smallest SOP, <b>AB'D' + BC'D + A'BD + B'C'D'</b>, has 12 literals: too many. So factor or use XOR.</p><table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>AB'D' + B'C'D' + A'BD + BC'D</td><td>the minimal SOP (4 terms)</td></tr><tr><td>2</td><td><b>1.</b> B'D'(A + C') + BD(A' + C')</td><td>factor B'D' and BD: 8 literals</td></tr><tr><td>3</td><td>all 1s have B = D, so F = (B ⊙ D)·(…)</td><td>B ⊙ D = BD + B'D' (XNOR)</td></tr><tr><td>4</td><td><b>2.</b> (B ⊙ D)(C' + (A ⊕ B))</td><td>when B = D = 0 we need A + C', when 1 we need A' + C': that's C' + (A ⊕ B): 5 literals</td></tr><tr><td>5</td><td><b>3.</b> (B ⊙ D)(C' + (A ⊕ D))</td><td>B = D inside that bracket, so D can stand in for B: 5 literals</td></tr></table>",
"lits": 8,
"ref": "08 §3"
}
]
},
{
"n": "3.26",
"text": "Simplest SOP of F = fg using maps.",
"qs": [
{
"tag": "Mano 3.26",
"type": "bool",
"q": "Find the simplest SOP of F = fg, where <code>f = abc' + c'd + a'cd' + b'cd'</code> and <code>g = (a + b + c' + d')(b' + c' + d)(a' + c + d')</code>.",
"vars": "abcd",
"ones": [
1,
2,
5,
10,
12
],
"show": "b'cd' + a'c'd + abc'd'",
"lits": 10,
"why": "<p>Plot f: 1s on 1, 2, 5, 6, 9, 10, 12, 13. Plot g: 0s on 3, 6, 9, 13, 14 (one 0-cell per bracket, e.g. a + b + c' + d' = 0 only on 0011 = 3, and so on).</p><p>F = fg is 1 only where <b>both</b> maps have a 1: cells <b>1, 2, 5, 10, 12</b>.</p><img src='svg/book/k3-26.svg' alt='grouped K-map'><p>Group the 1s in the biggest blocks of 1, 2, 4, 8 (they can wrap round the edges):</p><ul><li><b>a'c'd</b> from cells 1, 5</li><li><b>b'cd'</b> from cells 2, 10</li><li><b>abc'd'</b> from cells 12</li></ul><p><b>F = b'cd' + a'c'd + abc'd'</b> (10 literals).</p>",
"ref": "08 §3",
"form": "sop"
}
]
}
]
});
