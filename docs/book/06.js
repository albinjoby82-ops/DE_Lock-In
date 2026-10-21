BOOK.add({
"id": "06",
"title": "Gates and Boolean algebra",
"intro": "Mano Ch 2 (plus 1.35, 1.36, 4.1, 4.2). Expressions are checked on every row; where the book asks for a minimum, it must be minimal too.",
"problems": [
{
"n": "1.35",
"text": "Timing diagram for f (NAND) and g (NOR) of a, b, c over all 8 combinations.",
"qs": [
{
"tag": "Mano 1.35",
"type": "tt",
"q": "Fig P1.35: <b>f</b> is a 3-input NAND of a, b, c and <b>g</b> is a 3-input NOR of a, b, c. A timing diagram is just the truth table turned sideways. Fill f and g for all eight combinations.",
"vars": "abc",
"outs": {
"f": [
1,
1,
1,
1,
1,
1,
1,
0
],
"g": [
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
"why": "<img src='svg/book/t1-35.svg' alt='timing diagram'><p>NAND is <b>0 only when every input is 1</b> (the last slot, abc = 111).</p><p>NOR is <b>1 only when every input is 0</b> (the first slot, abc = 000).</p><p>Draw a, b, c as a binary count (c changes fastest), then read f and g straight off the table.</p>",
"ref": "06 §1",
"svg": "book/p1-35"
}
]
},
{
"n": "1.36",
"text": "Timing diagram for f (XOR) and g (XNOR) of a, b.",
"qs": [
{
"tag": "Mano 1.36",
"type": "tt",
"q": "Fig P1.36: <b>f</b> = XOR of a, b and <b>g</b> = XNOR of a, b. Fill f and g for all four combinations.",
"vars": "ab",
"outs": {
"f": [
0,
1,
1,
0
],
"g": [
1,
0,
0,
1
]
},
"why": "<img src='svg/book/t1-36.svg' alt='timing diagram'><p>XOR = 1 when the inputs <b>differ</b> (01, 10). XNOR is its opposite: 1 when they are <b>the same</b> (00, 11).</p><p>So g is always the flip of f: f = 0 1 1 0, g = 1 0 0 1.</p>",
"ref": "06 §1",
"svg": "book/p1-36"
}
]
},
{
"n": "2.1",
"text": "Prove each identity with a truth table.",
"qs": [
{
"tag": "Mano 2.1 (a)",
"type": "tt",
"q": "Prove De Morgan for three variables with a truth table: <code>(x + y + z)' = x'y'z'</code> and <code>(xyz)' = x' + y' + z'</code>. Fill all four columns.",
"vars": "xyz",
"outs": {
"(x+y+z)'": [
1,
0,
0,
0,
0,
0,
0,
0
],
"x'y'z'": [
1,
0,
0,
0,
0,
0,
0,
0
],
"(xyz)'": [
1,
1,
1,
1,
1,
1,
1,
0
],
"x'+y'+z'": [
1,
1,
1,
1,
1,
1,
1,
0
]
},
"why": "<p>Columns 1 and 2 match on every row (1 only on 000). Columns 3 and 4 match on every row (0 only on 111). Same output on all 8 rows = <b>the identities hold</b>.</p><p>Quick way to fill them: an OR is 0 only on 000, so its NOT is 1 only on 000. An AND is 1 only on 111, so its NOT is 0 only on 111.</p>",
"ref": "06 §3"
},
{
"tag": "Mano 2.1 (b)",
"type": "tt",
"q": "Prove the distributive law (OR over AND) with a truth table: <code>x + yz = (x + y)(x + z)</code>. Fill both columns.",
"vars": "xyz",
"outs": {
"x + yz": [
0,
0,
0,
1,
1,
1,
1,
1
],
"(x + y)(x + z)": [
0,
0,
0,
1,
1,
1,
1,
1
]
},
"why": "<p>Both columns are <b>0 0 0 1 1 1 1 1</b>: identical on all 8 rows, so the law holds.</p><p>When x = 1 both sides are 1. When x = 0 both sides become yz. That is why this odd-looking law works.</p>",
"ref": "06 §3"
},
{
"tag": "Mano 2.1 (c)",
"type": "tt",
"q": "Prove the distributive law (AND over OR) with a truth table: <code>x(y + z) = xy + xz</code>. Fill both columns.",
"vars": "xyz",
"outs": {
"x(y + z)": [
0,
0,
0,
0,
0,
1,
1,
1
],
"xy + xz": [
0,
0,
0,
0,
0,
1,
1,
1
]
},
"why": "<p>Both columns are <b>0 0 0 0 0 1 1 1</b>: identical on all 8 rows, so the law holds.</p>",
"ref": "06 §3"
},
{
"tag": "Mano 2.1 (d)",
"type": "tt",
"q": "Prove the associative law for OR with a truth table: <code>x + (y + z) = (x + y) + z</code>. Fill both columns.",
"vars": "xyz",
"outs": {
"x + (y + z)": [
0,
1,
1,
1,
1,
1,
1,
1
],
"(x + y) + z": [
0,
1,
1,
1,
1,
1,
1,
1
]
},
"why": "<p>Both columns are <b>0 1 1 1 1 1 1 1</b>: identical on all 8 rows, so the law holds.</p>",
"ref": "06 §3"
},
{
"tag": "Mano 2.1 (e)",
"type": "tt",
"q": "Prove the associative law for AND with a truth table: <code>x(yz) = (xy)z</code>. Fill both columns.",
"vars": "xyz",
"outs": {
"x(yz)": [
0,
0,
0,
0,
0,
0,
0,
1
],
"(xy)z": [
0,
0,
0,
0,
0,
0,
0,
1
]
},
"why": "<p>Both columns are <b>0 0 0 0 0 0 0 1</b>: identical on all 8 rows, so the law holds.</p>",
"ref": "06 §3"
}
]
},
{
"n": "2.2",
"text": "Simplify to a minimum number of literals.",
"qs": [
{
"tag": "Mano 2.2 (a) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>xy + xy'</code>",
"vars": "xy",
"ones": [
2,
3
],
"show": "x",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>x<mark>(y + y')</mark></td><td>factor out x</td></tr><tr><td>2</td><td>x·1</td><td>y + y' = 1</td></tr><tr><td>3</td><td><b>x</b></td><td>x·1 = x</td></tr></table>",
"lits": 1,
"ref": "06 §3"
},
{
"tag": "Mano 2.2 (b) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>(x + y)(x + y')</code>",
"vars": "xy",
"ones": [
2,
3
],
"show": "x",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>x + <mark>yy'</mark></td><td>distributive backwards: (x + y)(x + z) = x + yz</td></tr><tr><td>2</td><td>x + 0</td><td>yy' = 0</td></tr><tr><td>3</td><td><b>x</b></td><td>x + 0 = x</td></tr></table>",
"lits": 1,
"ref": "06 §3"
},
{
"tag": "Mano 2.2 (c) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>xyz + x'y + xyz'</code>",
"vars": "xyz",
"ones": [
2,
3,
6,
7
],
"show": "y",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>xy(z + z')</mark> + x'y</td><td>terms 1 and 3 share xy: factor it</td></tr><tr><td>2</td><td>xy + x'y</td><td>z + z' = 1</td></tr><tr><td>3</td><td>y<mark>(x + x')</mark></td><td>factor out y</td></tr><tr><td>4</td><td><b>y</b></td><td>x + x' = 1</td></tr></table>",
"lits": 1,
"ref": "06 §3"
},
{
"tag": "Mano 2.2 (d) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>(A + B)'(A' + B')'</code>",
"vars": "AB",
"ones": [],
"show": "0",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>A'B'</mark> · <mark>AB</mark></td><td>De Morgan on each bracket: (A + B)' = A'B', (A' + B')' = AB</td></tr><tr><td>2</td><td>(AA')(BB')</td><td>reorder the AND</td></tr><tr><td>3</td><td><b>0</b></td><td>AA' = 0, and 0 times anything is 0</td></tr></table>",
"ref": "06 §3"
},
{
"tag": "Mano 2.2 (e)",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>xyz' + x'yz + xyz + x'yz'</code>",
"vars": "xyz",
"ones": [
2,
3,
6,
7
],
"show": "y",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>xy(z' + z)</mark> + <mark>x'y(z + z')</mark></td><td>pair terms 1+3 and 2+4</td></tr><tr><td>2</td><td>xy + x'y</td><td>z + z' = 1</td></tr><tr><td>3</td><td>y(x + x')</td><td>factor out y</td></tr><tr><td>4</td><td><b>y</b></td><td>x + x' = 1</td></tr></table>",
"lits": 1,
"ref": "06 §3"
},
{
"tag": "Mano 2.2 (f)",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>(x + y + z')(x' + y' + z)</code>",
"vars": "xyz",
"ones": [
0,
2,
3,
4,
5,
7
],
"show": "x'z' + yz + xy'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(x + y + z') = 0 only on xyz = 001</td><td>a sum is 0 only when every letter in it is 0</td></tr><tr><td>2</td><td>(x' + y' + z) = 0 only on xyz = 110</td><td>same idea</td></tr><tr><td>3</td><td>F = ΠM(1, 6) = Σm(0, 2, 3, 4, 5, 7)</td><td>F is 0 on rows 1 and 6 only</td></tr><tr><td>4</td><td><b>x'z' + yz + xy'</b></td><td>three pairs on the K-map (below)</td></tr></table><img src='svg/book/k2-2f.svg' alt=''><p><b>Both</b> the original and this SOP have <b>6 literals</b>, and nothing smaller exists (each 1 can only join one neighbour). So the given expression was already minimal. Either answer is fine.</p>",
"lits": 6,
"ref": "06 §3"
}
]
},
{
"n": "2.3",
"text": "Simplify to a minimum number of literals.",
"qs": [
{
"tag": "Mano 2.3 (a) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>ABC + A'B + ABC'</code>",
"vars": "ABC",
"ones": [
2,
3,
6,
7
],
"show": "B",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>AB(C + C')</mark> + A'B</td><td>terms 1 and 3 share AB</td></tr><tr><td>2</td><td>AB + A'B</td><td>C + C' = 1</td></tr><tr><td>3</td><td>B(A + A')</td><td>factor out B</td></tr><tr><td>4</td><td><b>B</b></td><td>A + A' = 1</td></tr></table>",
"lits": 1,
"ref": "06 §3"
},
{
"tag": "Mano 2.3 (b) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>x'yz + xz</code>",
"vars": "xyz",
"ones": [
3,
5,
7
],
"show": "z(x + y)",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>z<mark>(x'y + x)</mark></td><td>factor out z</td></tr><tr><td>2</td><td><b>z(x + y)</b></td><td>x + x'y = x + y</td></tr></table>",
"lits": 3,
"ref": "06 §3"
},
{
"tag": "Mano 2.3 (c) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>(x + y)'(x' + y')</code>",
"vars": "xy",
"ones": [
0
],
"show": "x'y'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>x'y'</mark>(x' + y')</td><td>De Morgan: (x + y)' = x'y'</td></tr><tr><td>2</td><td>x'y'x' + x'y'y'</td><td>multiply out</td></tr><tr><td>3</td><td>x'y' + x'y'</td><td>x'x' = x', y'y' = y'</td></tr><tr><td>4</td><td><b>x'y'</b></td><td>A + A = A</td></tr></table>",
"lits": 2,
"ref": "06 §3"
},
{
"tag": "Mano 2.3 (d) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>xy + x(wz + wz')</code>",
"vars": "wxyz",
"ones": [
6,
7,
12,
13,
14,
15
],
"show": "x(y + w)",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>xy + x<mark>w(z + z')</mark></td><td>factor w inside the bracket</td></tr><tr><td>2</td><td>xy + xw</td><td>z + z' = 1</td></tr><tr><td>3</td><td><b>x(y + w)</b></td><td>factor out x</td></tr></table>",
"lits": 3,
"ref": "06 §3"
},
{
"tag": "Mano 2.3 (e) ★",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>(BC' + A'D)(AB' + CD')</code>",
"vars": "ABCD",
"ones": [],
"show": "0",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>BC'AB' + BC'CD' + A'DAB' + A'DCD'</td><td>multiply out: 4 products</td></tr><tr><td>2</td><td>A<mark>BB'</mark>C' + B<mark>C'C</mark>D' + <mark>A'A</mark>B'D + A'C<mark>DD'</mark></td><td>every product holds a letter and its complement</td></tr><tr><td>3</td><td><b>0 + 0 + 0 + 0 = 0</b></td><td>XX' = 0</td></tr></table>",
"ref": "06 §3"
},
{
"tag": "Mano 2.3 (f)",
"type": "bool",
"q": "Simplify to a minimum number of literals: <code>(x + y' + z')(x' + z')</code>",
"vars": "xyz",
"ones": [
0,
1,
2,
4,
6
],
"show": "z' + x'y'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(z' + x + y')(z' + x')</td><td>reorder so z' leads both brackets</td></tr><tr><td>2</td><td>z' + <mark>(x + y')x'</mark></td><td>distributive backwards: (A + B)(A + C) = A + BC</td></tr><tr><td>3</td><td>z' + xx' + x'y'</td><td>multiply out</td></tr><tr><td>4</td><td><b>z' + x'y'</b></td><td>xx' = 0</td></tr></table>",
"lits": 3,
"ref": "06 §3"
}
]
},
{
"n": "2.4",
"text": "Reduce each expression to the given number of literals.",
"qs": [
{
"tag": "Mano 2.4 (a) ★",
"type": "bool",
"q": "Reduce to <b>three</b> literals: <code>A'C' + ABC + AC'</code>",
"vars": "ABC",
"ones": [
0,
2,
4,
6,
7
],
"show": "C' + AB",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>C'(A' + A)</mark> + ABC</td><td>terms 1 and 3 share C'</td></tr><tr><td>2</td><td>C' + ABC</td><td>A' + A = 1</td></tr><tr><td>3</td><td><b>C' + AB</b></td><td>x + x'y = x + y, with x = C'</td></tr></table>",
"lits": 3,
"ref": "06 §3"
},
{
"tag": "Mano 2.4 (b) ★",
"type": "bool",
"q": "Reduce to <b>three</b> literals: <code>(x'y' + z)' + z + xy + wz</code>",
"vars": "wxyz",
"ones": [
1,
2,
3,
4,
5,
6,
7,
9,
10,
11,
12,
13,
14,
15
],
"show": "x + y + z",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>(x'y')'z'</mark> + z + xy + wz</td><td>De Morgan: (P + z)' = P'z'</td></tr><tr><td>2</td><td><mark>(x + y)</mark>z' + z + xy + wz</td><td>De Morgan: (x'y')' = x + y</td></tr><tr><td>3</td><td>xz' + yz' + z + xy + wz</td><td>multiply out</td></tr><tr><td>4</td><td>xz' + yz' + z + xy</td><td>wz is absorbed by z</td></tr><tr><td>5</td><td><mark>x + y + z</mark> + xy</td><td>z + xz' = z + x and z + yz' = z + y</td></tr><tr><td>6</td><td><b>x + y + z</b></td><td>xy is absorbed by x</td></tr></table>",
"lits": 3,
"ref": "06 §3"
},
{
"tag": "Mano 2.4 (c) ★",
"type": "bool",
"q": "Reduce to <b>one</b> literal: <code>A'B(D' + C'D) + B(A + A'CD)</code>",
"vars": "ABCD",
"ones": [
4,
5,
6,
7,
12,
13,
14,
15
],
"show": "B",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>A'B<mark>(D' + C')</mark> + B<mark>(A + CD)</mark></td><td>x + x'y = x + y, twice</td></tr><tr><td>2</td><td>B[A'D' + A'C' + A + CD]</td><td>factor out B</td></tr><tr><td>3</td><td>B[<mark>A + D' + C'</mark> + CD]</td><td>A + A'D' = A + D', A + A'C' = A + C'</td></tr><tr><td>4</td><td>B[A + D' + <mark>C' + D</mark>]</td><td>C' + CD = C' + D</td></tr><tr><td>5</td><td>B[1]</td><td>D' + D = 1, so the whole bracket is 1</td></tr><tr><td>6</td><td><b>B</b></td><td>B·1 = B</td></tr></table>",
"lits": 1,
"ref": "06 §3"
},
{
"tag": "Mano 2.4 (d) ★",
"type": "bool",
"q": "Reduce to <b>four</b> literals: <code>(A' + C)(A' + C')(A + B + C'D)</code>",
"vars": "ABCD",
"ones": [
1,
4,
5,
6,
7
],
"show": "A'(B + C'D)",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>(A' + CC')</mark>(A + B + C'D)</td><td>distributive backwards on the first two brackets</td></tr><tr><td>2</td><td>A'(A + B + C'D)</td><td>CC' = 0</td></tr><tr><td>3</td><td>A'A + A'B + A'C'D</td><td>multiply out</td></tr><tr><td>4</td><td>A'B + A'C'D</td><td>A'A = 0</td></tr><tr><td>5</td><td><b>A'(B + C'D)</b></td><td>factor A' back out: 4 literals (the SOP has 5)</td></tr></table>",
"lits": 4,
"ref": "06 §3"
},
{
"tag": "Mano 2.4 (e)",
"type": "bool",
"q": "Reduce to <b>two</b> literals: <code>ABCD + A'BD + ABC'D</code>",
"vars": "ABCD",
"ones": [
5,
7,
13,
15
],
"show": "BD",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>ABD(C + C')</mark> + A'BD</td><td>terms 1 and 3 share ABD</td></tr><tr><td>2</td><td>ABD + A'BD</td><td>C + C' = 1</td></tr><tr><td>3</td><td>BD(A + A')</td><td>factor out BD</td></tr><tr><td>4</td><td><b>BD</b></td><td>A + A' = 1</td></tr></table>",
"lits": 2,
"ref": "06 §3"
}
]
},
{
"n": "2.5",
"text": "Draw the logic diagrams for the original and simplified expressions in Problem 2.2.",
"qs": [
{
"tag": "Mano 2.5 (a)",
"type": "work",
"q": "Draw the logic diagram for the original <code>xy + xy'</code> and for the simplified <code>F = x</code> (from 2.2 a).",
"why": "<img src='svg/book/c2-2a.svg' alt='before and after circuits'><p><b>3 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.5 (b)",
"type": "work",
"q": "Draw the logic diagram for the original <code>(x + y)(x + y')</code> and for the simplified <code>F = x</code> (from 2.2 b).",
"why": "<img src='svg/book/c2-2b.svg' alt='before and after circuits'><p><b>3 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.5 (c)",
"type": "work",
"q": "Draw the logic diagram for the original <code>xyz + x'y + xyz'</code> and for the simplified <code>F = y</code> (from 2.2 c).",
"why": "<img src='svg/book/c2-2c.svg' alt='before and after circuits'><p><b>4 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.5 (d)",
"type": "work",
"q": "Draw the logic diagram for the original <code>(A + B)'(A' + B')'</code> and for the simplified <code>F = 0</code> (from 2.2 d).",
"why": "<img src='svg/book/c2-2d.svg' alt='before and after circuits'><p><b>3 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.5 (e)",
"type": "work",
"q": "Draw the logic diagram for the original <code>xyz' + x'yz + xyz + x'yz'</code> and for the simplified <code>F = y</code> (from 2.2 e).",
"why": "<img src='svg/book/c2-2e.svg' alt='before and after circuits'><p><b>5 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.5 (f)",
"type": "work",
"q": "Draw the logic diagram for <code>(x + y + z')(x' + y' + z)</code> and for the simplified <code>x'z' + yz + xy'</code> (from 2.2 f).",
"why": "<img src='svg/book/c2-2f.svg' alt=''><p>3 gates either way. This one didn't get cheaper: the original was already minimal.</p>",
"ref": "06 §4",
"nomock": true
}
]
},
{
"n": "2.6",
"text": "Draw the logic diagrams for the original and simplified expressions in Problem 2.3.",
"qs": [
{
"tag": "Mano 2.6 (a)",
"type": "work",
"q": "Draw the logic diagram for the original <code>ABC + A'B + ABC'</code> and for the simplified <code>F = B</code> (from 2.3 a).",
"why": "<img src='svg/book/c2-3a.svg' alt='before and after circuits'><p><b>4 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.6 (b)",
"type": "work",
"q": "Draw the logic diagram for the original <code>x'yz + xz</code> and for the simplified <code>F = z(x + y)</code> (from 2.3 b).",
"why": "<img src='svg/book/c2-3b.svg' alt='before and after circuits'><p><b>3 gates → 2 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.6 (c)",
"type": "work",
"q": "Draw the logic diagram for the original <code>(x + y)'(x' + y')</code> and for the simplified <code>F = x'y'</code> (from 2.3 c).",
"why": "<img src='svg/book/c2-3c.svg' alt='before and after circuits'><p><b>3 gates → 1 gate.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.6 (d)",
"type": "work",
"q": "Draw the logic diagram for the original <code>xy + x(wz + wz')</code> and for the simplified <code>F = x(y + w)</code> (from 2.3 d).",
"why": "<img src='svg/book/c2-3d.svg' alt='before and after circuits'><p><b>6 gates → 2 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.6 (e)",
"type": "work",
"q": "Draw the logic diagram for the original <code>(BC' + A'D)(AB' + CD')</code> and for the simplified <code>F = 0</code> (from 2.3 e).",
"why": "<img src='svg/book/c2-3e.svg' alt='before and after circuits'><p><b>7 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.6 (f)",
"type": "work",
"q": "Draw the logic diagram for the original <code>(x + y' + z')(x' + z')</code> and for the simplified <code>F = z' + x'y'</code> (from 2.3 f).",
"why": "<img src='svg/book/c2-3f.svg' alt='before and after circuits'><p><b>3 gates → 2 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
}
]
},
{
"n": "2.7",
"text": "Draw the logic diagrams for the original and simplified expressions in Problem 2.4.",
"qs": [
{
"tag": "Mano 2.7 (a)",
"type": "work",
"q": "Draw the logic diagram for the original <code>A'C' + ABC + AC'</code> and for the simplified <code>F = C' + AB</code> (from 2.4 a).",
"why": "<img src='svg/book/c2-4a.svg' alt='before and after circuits'><p><b>4 gates → 2 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.7 (b)",
"type": "work",
"q": "Draw the logic diagram for the original <code>(x'y' + z)' + z + xy + wz</code> and for the simplified <code>F = x + y + z</code> (from 2.4 b).",
"why": "<img src='svg/book/c2-4b.svg' alt='before and after circuits'><p><b>5 gates → 1 gate.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.7 (c)",
"type": "work",
"q": "Draw the logic diagram for the original <code>A'B(D' + C'D) + B(A + A'CD)</code> and for the simplified <code>F = B</code> (from 2.4 c).",
"why": "<img src='svg/book/c2-4c.svg' alt='before and after circuits'><p><b>7 gates → 0 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.7 (d)",
"type": "work",
"q": "Draw the logic diagram for the original <code>(A' + C)(A' + C')(A + B + C'D)</code> and for the simplified <code>F = A'(B + C'D)</code> (from 2.4 d).",
"why": "<img src='svg/book/c2-4d.svg' alt='before and after circuits'><p><b>5 gates → 3 gates.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
},
{
"tag": "Mano 2.7 (e)",
"type": "work",
"q": "Draw the logic diagram for the original <code>ABCD + A'BD + ABC'D</code> and for the simplified <code>F = BD</code> (from 2.4 e).",
"why": "<img src='svg/book/c2-4e.svg' alt='before and after circuits'><p><b>4 gates → 1 gate.</b> Complemented inputs (x') are drawn as already available, like the book does. Draw an inverter on each one if your lecturer wants them shown.</p>",
"ref": "06 §4",
"nomock": true
}
]
},
{
"n": "2.8",
"text": "Find the complement of F = wx + yz; then show FF' = 0 and F + F' = 1.",
"qs": [
{
"tag": "Mano 2.8",
"type": "bool",
"q": "F = <code>wx + yz</code>. Find <b>F'</b> (no bar over a group). Then show FF' = 0 and F + F' = 1 on paper.",
"vars": "wxyz",
"ones": [
0,
1,
2,
4,
5,
6,
8,
9,
10
],
"show": "(w' + x')(y' + z')",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>F' = (wx + yz)'</td><td>complement the whole thing</td></tr><tr><td>2</td><td><mark>(wx)'</mark>·<mark>(yz)'</mark></td><td>De Morgan: (A + B)' = A'B'</td></tr><tr><td>3</td><td><b>(w' + x')(y' + z')</b></td><td>De Morgan again: (AB)' = A' + B'</td></tr></table><p><b>FF' = 0:</b> FF' = (wx + yz)(w' + x')(y' + z'). wx(w' + x') = ww'x + wxx' = 0, and yz(y' + z') = 0. Every product dies, so <b>FF' = 0</b>.</p><p><b>F + F' = 1:</b> F' = w'y' + w'z' + x'y' + x'z'. If wx = 1 or yz = 1 then F = 1. If not, one of w, x is 0 <i>and</i> one of y, z is 0, so one of those four F' terms is 1. Either way the sum is <b>1</b>.</p>",
"lits": 4,
"ref": "06 §3"
}
]
},
{
"n": "2.9",
"text": "Find the complement of each expression.",
"qs": [
{
"tag": "Mano 2.9 (a) ★",
"type": "bool",
"q": "Find the complement of <code>xy' + x'y</code> (no bar over a group).",
"vars": "xy",
"ones": [
0,
3
],
"show": "xy + x'y'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>(xy')'</mark>·<mark>(x'y)'</mark></td><td>De Morgan on the +</td></tr><tr><td>2</td><td>(x' + y)(x + y')</td><td>De Morgan on each product: flip letters, AND → OR</td></tr><tr><td>3</td><td>x'x + x'y' + xy + yy'</td><td>multiply out</td></tr><tr><td>4</td><td><b>xy + x'y'</b></td><td>x'x = 0, yy' = 0</td></tr></table><p>Makes sense: xy' + x'y is XOR, and its complement is XNOR (1 when x and y are equal).</p>",
"lits": 4,
"ref": "06 §3"
},
{
"tag": "Mano 2.9 (b)",
"type": "bool",
"q": "Find the complement of <code>(A'B + CD)E' + E</code> (no bar over a group).",
"vars": "ABCDE",
"ones": [
0,
2,
4,
16,
18,
20,
24,
26,
28
],
"show": "(A + B')(C' + D')E'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(A'B + CD)E' + E = A'B + CD + E</td><td>simplify first: PE' + E = P + E</td></tr><tr><td>2</td><td>(A'B)'·(CD)'·E'</td><td>De Morgan on the three-way OR</td></tr><tr><td>3</td><td><b>(A + B')(C' + D')E'</b></td><td>De Morgan on each product</td></tr></table><p>Tip: simplifying <i>before</i> complementing saves a lot of writing.</p>",
"ref": "06 §3"
},
{
"tag": "Mano 2.9 (c)",
"type": "bool",
"q": "Find the complement of <code>(x' + y + z')(x + y')(x + z)</code> (no bar over a group).",
"vars": "xyz",
"ones": [
0,
2,
3,
5
],
"show": "xy'z + x'y + x'z'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(x' + y + z')' + (x + y')' + (x + z)'</td><td>De Morgan: a complemented product becomes a sum</td></tr><tr><td>2</td><td><b>xy'z + x'y + x'z'</b></td><td>De Morgan on each sum: flip letters, OR → AND</td></tr></table><p>Rule of thumb: <b>flip every letter, swap AND ↔ OR</b>. Done.</p>",
"ref": "06 §3"
}
]
},
{
"n": "2.11",
"text": "List the truth table of each function.",
"qs": [
{
"tag": "Mano 2.11 (a) ★",
"type": "tt",
"q": "Fill the truth table for <code>F = xy + xy' + y'z</code>.",
"vars": "xyz",
"outs": {
"F": [
0,
1,
0,
0,
1,
1,
1,
1
]
},
"why": "<p>Simplify first: xy + xy' = x, so <b>F = x + y'z</b>.</p><p>Bottom half (x = 1): all 1. Top half (x = 0): F = y'z, which is 1 only on 001.</p>",
"ref": "06 §2"
},
{
"tag": "Mano 2.11 (b)",
"type": "tt",
"q": "Fill the truth table for <code>F = x'z' + yz</code>.",
"vars": "xyz",
"outs": {
"F": [
1,
0,
1,
1,
0,
0,
0,
1
]
},
"why": "<p>x'z' is 1 on 000 and 010. yz is 1 on 011 and 111. So F = 1 on rows <b>0, 2, 3, 7</b>.</p>",
"ref": "06 §2"
}
]
},
{
"n": "2.12",
"text": "Bitwise AND, OR, XOR, NOT A, NOT B of A = 10110001 and B = 10101100.",
"qs": [
{
"tag": "Mano 2.12 ★",
"type": "multi",
"q": "A = <code>10110001</code>, B = <code>10101100</code>. Work out each 8-bit result bit by bit (parts a, c, d are starred).",
"fields": [
{
"label": "AND",
"ans": [
"10100000"
]
},
{
"label": "OR",
"ans": [
"10111101"
]
},
{
"label": "XOR",
"ans": [
"00011101"
]
},
{
"label": "NOT A",
"ans": [
"01001110"
]
},
{
"label": "NOT B",
"ans": [
"01010011"
]
}
],
"why": "<table class='bits'><tr><th>A</th><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><th>B</th><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><th>AND</th><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><th>OR</th><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><th>XOR</th><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><th>NOT A</th><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><th>NOT B</th><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr></table><p>Line the bits up in columns and do each column on its own. AND: 1 only if both are 1. OR: 1 if either is 1. XOR: 1 if they differ. NOT: flip.</p>",
"ref": "06 §1"
}
]
},
{
"n": "2.13",
"text": "Draw logic diagrams for each expression.",
"qs": [
{
"tag": "Mano 2.13 (a)",
"type": "work",
"q": "Draw the logic diagram for <code>Y = A + B + B'(A + C')</code>.",
"why": "<img src='svg/book/c2-13a.svg' alt='logic diagram'><p>Build it from the inside out: innermost bracket first, the outer operation is the last gate.</p><p>Not asked, but it simplifies a lot: B + B'(A + C') = B + A + C', so Y = <b>A + B + C'</b> (one 3-input OR).</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.13 (b)",
"type": "work",
"q": "Draw the logic diagram for <code>Y = A(B ⊕ D) + C'</code>.",
"why": "<img src='svg/book/c2-13b.svg' alt='logic diagram'><p>Build it from the inside out: innermost bracket first, the outer operation is the last gate.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.13 (c)",
"type": "work",
"q": "Draw the logic diagram for <code>Y = A + CD + ABC</code>.",
"why": "<img src='svg/book/c2-13c.svg' alt='logic diagram'><p>Build it from the inside out: innermost bracket first, the outer operation is the last gate.</p><p>Not asked, but ABC is absorbed by A, so Y = <b>A + CD</b>.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.13 (d)",
"type": "work",
"q": "Draw the logic diagram for <code>Y = (A ⊕ C)' + B</code>.",
"why": "<img src='svg/book/c2-13d.svg' alt='logic diagram'><p>Build it from the inside out: innermost bracket first, the outer operation is the last gate.</p><p>(A ⊕ C)' is one XNOR gate: an XOR with a bubble on the output.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.13 (e)",
"type": "work",
"q": "Draw the logic diagram for <code>Y = (A' + B')(C + D')</code>.",
"why": "<img src='svg/book/c2-13e.svg' alt='logic diagram'><p>Build it from the inside out: innermost bracket first, the outer operation is the last gate.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.13 (f)",
"type": "work",
"q": "Draw the logic diagram for <code>Y = (A + B')(C' + D)</code>.",
"why": "<img src='svg/book/c2-13f.svg' alt='logic diagram'><p>Build it from the inside out: innermost bracket first, the outer operation is the last gate.</p><p>Product of sums: two OR gates feeding one AND gate.</p>",
"ref": "06 §1"
}
]
},
{
"n": "2.14",
"text": "Implement F = xy + x'y' + y'z with each set of gates.",
"qs": [
{
"tag": "Mano 2.14 (a)",
"type": "work",
"q": "Implement <code>F = xy + x'y' + y'z</code> with <b>AND, OR and inverter gates</b> only.",
"why": "<p>Straight from the SOP: one AND per term, one OR to join them. Inverters make x' and y'.</p><img src='svg/book/c2-14a.svg' alt='circuit'>",
"ref": "06 §3"
},
{
"tag": "Mano 2.14 (b) ★",
"type": "work",
"q": "Implement <code>F = xy + x'y' + y'z</code> with <b>OR and inverter gates</b> only.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>xy = (x' + y')'</td><td>De Morgan: an AND is a NOR of the complements</td></tr><tr><td>2</td><td>x'y' = (x + y)'</td><td>same</td></tr><tr><td>3</td><td>y'z = (y + z')'</td><td>same</td></tr><tr><td>4</td><td>F = (x' + y')' + (x + y)' + (y + z')'</td><td>every AND is now an OR followed by an inverter</td></tr></table><img src='svg/book/c2-14b.svg' alt='circuit'>",
"ref": "06 §3"
},
{
"tag": "Mano 2.14 (c)",
"type": "work",
"q": "Implement <code>F = xy + x'y' + y'z</code> with <b>AND and inverter gates</b> only.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>F = [(xy)'·(x'y')'·(y'z)']'</td><td>De Morgan on the whole OR: A + B + C = (A'B'C')'</td></tr><tr><td>2</td><td>ANDs, inverter on each, AND them, inverter at the end</td><td>only AND and NOT used</td></tr></table><img src='svg/book/c2-14c.svg' alt='circuit'>",
"ref": "06 §3"
},
{
"tag": "Mano 2.14 (d)",
"type": "work",
"q": "Implement <code>F = xy + x'y' + y'z</code> with <b>NAND and inverter gates</b> only.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>F = [(xy)'·(x'y')'·(y'z)']'</td><td>same De Morgan as (c)</td></tr><tr><td>2</td><td>each (AB)' is a NAND, and the outer [ ]' is a NAND</td><td>AND then NOT = NAND</td></tr></table><p>This is the standard <b>NAND-NAND</b> form of an SOP (Topic 09).</p><img src='svg/book/c2-14d.svg' alt='circuit'>",
"ref": "06 §3"
},
{
"tag": "Mano 2.14 (e)",
"type": "work",
"q": "Implement <code>F = xy + x'y' + y'z</code> with <b>NOR and inverter gates</b> only.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>xy = (x' + y')', x'y' = (x + y)', y'z = (y + z')'</td><td>each AND term as a NOR</td></tr><tr><td>2</td><td>F = [ (x'+y')' + (x+y)' + (y+z')' ]''</td><td>OR = NOR then NOT</td></tr></table><img src='svg/book/c2-14e.svg' alt='circuit'>",
"ref": "06 §3"
}
]
},
{
"n": "2.15",
"text": "Simplify T₁ and T₂ from the truth table.",
"qs": [
{
"tag": "Mano 2.15 (T₁) ★",
"type": "bool",
"q": "Truth table: T₁ = 1 on ABC = 000, 001, 010 only. Simplify T₁ to a minimum number of literals.",
"vars": "ABC",
"ones": [
0,
1,
2
],
"show": "A'B' + A'C'",
"why": "<table class='tts'><tr><th>A</th><th>B</th><th>C</th><th class='o'>T₁</th><th class='o'>T₂</th></tr><tr><td>0</td><td>0</td><td>0</td><td class='o'>1</td><td class='o'>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td class='o'>1</td><td class='o'>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td class='o'>1</td><td class='o'>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td class='o'>0</td><td class='o'>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td class='o'>0</td><td class='o'>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td class='o'>0</td><td class='o'>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td class='o'>0</td><td class='o'>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td class='o'>0</td><td class='o'>1</td></tr></table><table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>A'B'C' + A'B'C + A'BC'</td><td>one minterm per 1</td></tr><tr><td>2</td><td><mark>A'B'</mark> + A'BC'</td><td>first two: A'B'(C' + C)</td></tr><tr><td>3</td><td>A'<mark>(B' + BC')</mark></td><td>factor A'</td></tr><tr><td>4</td><td><b>A'(B' + C') = A'B' + A'C'</b></td><td>B' + BC' = B' + C'</td></tr></table><p>A'(B' + C') is only 3 literals, the book gives A'B' + A'C'. Both are accepted here.</p>",
"lits": 4,
"ref": "06 §3"
},
{
"tag": "Mano 2.15 (T₂) ★",
"type": "bool",
"q": "Same table: T₂ = 1 on ABC = 011, 100, 101, 110, 111. Simplify T₂.",
"vars": "ABC",
"ones": [
3,
4,
5,
6,
7
],
"show": "A + BC",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>A'BC + AB'C' + AB'C + ABC' + ABC</td><td>one minterm per 1</td></tr><tr><td>2</td><td>A'BC + A</td><td>the four A terms cover every BC combination: they sum to A</td></tr><tr><td>3</td><td><b>A + BC</b></td><td>A + A'BC = A + BC</td></tr></table><p>Also notice T₂ = T₁' (the columns are opposite), and (A'(B' + C'))' = A + BC by De Morgan.</p>",
"lits": 3,
"ref": "06 §3"
}
]
},
{
"n": "2.18",
"text": "F = xy'z + x'y'z + w'xy + wx'y + wxy: truth table, diagrams, simplification.",
"qs": [
{
"tag": "Mano 2.18 (a)",
"type": "tt",
"q": "Fill the truth table for <code>F = xy'z + x'y'z + w'xy + wx'y + wxy</code>.",
"vars": "wxyz",
"outs": {
"F": [
0,
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
1,
0,
1,
1,
1
]
},
"why": "<p>Find each term's rows: xy'z → 5, 13 · x'y'z → 1, 9 · w'xy → 6, 7 · wx'y → 10, 11 · wxy → 14, 15.</p><p>So F = 1 on rows <b>1, 5, 6, 7, 9, 10, 11, 13, 14, 15</b>, 0 everywhere else.</p>",
"ref": "06 §2"
},
{
"tag": "Mano 2.18 (b)",
"type": "work",
"q": "Draw the logic diagram of <code>F = xy'z + x'y'z + w'xy + wx'y + wxy</code> as written.",
"why": "<img src='svg/book/c2-18.svg' alt='circuits'><p>The top circuit is the answer to (b): five 3-input ANDs into a 5-input OR = 6 gates.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.18 (c) ★",
"type": "bool",
"q": "Simplify with Boolean algebra: <code>F = xy'z + x'y'z + w'xy + wx'y + wxy</code>.",
"vars": "wxyz",
"ones": [
1,
5,
6,
7,
9,
10,
11,
13,
14,
15
],
"show": "y'z + xy + wy",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td><mark>y'z(x + x')</mark> + w'xy + wx'y + wxy</td><td>terms 1 + 2 share y'z</td></tr><tr><td>2</td><td>y'z + w'xy + wx'y + wxy + wxy</td><td>copy wxy (A = A + A) so it can pair twice</td></tr><tr><td>3</td><td>y'z + <mark>xy(w' + w)</mark> + <mark>wy(x' + x)</mark></td><td>pair w'xy with wxy, and wx'y with wxy</td></tr><tr><td>4</td><td><b>y'z + xy + wy</b></td><td>w' + w = 1, x' + x = 1</td></tr></table><img src='svg/book/k2-18.svg' alt='K-map check'><p>Factored, y'z + y(w + x) is 5 literals. Both accepted.</p>",
"lits": 6,
"ref": "06 §4"
},
{
"tag": "Mano 2.18 (d)",
"type": "work",
"q": "Get the truth table from your simplified <code>F = y'z + xy + wy</code> and show it matches (a).",
"why": "<table class='tts'><tr><th>w</th><th>x</th><th>y</th><th>z</th><th class='o'>(a)</th><th class='o'>y'z+xy+wy</th></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td class='o'>0</td><td class='o'>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td class='o'>0</td><td class='o'>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>1</td><td class='o'>0</td><td class='o'>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td class='o'>0</td><td class='o'>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td class='o'>0</td><td class='o'>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td class='o'>0</td><td class='o'>0</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td class='o'>1</td><td class='o'>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td class='o'>1</td><td class='o'>1</td></tr></table><p>Identical on all 16 rows, so the simplification is right.</p>",
"ref": "06 §2"
},
{
"tag": "Mano 2.18 (e)",
"type": "work",
"q": "Draw the simplified circuit and compare the gate count with (b).",
"why": "<img src='svg/book/c2-18.svg' alt='circuits'><p><b>6 gates → 4 gates</b> (and every AND drops from 3 inputs to 2). Fewer gates and fewer inputs = cheaper and faster.</p>",
"ref": "06 §4"
}
]
},
{
"n": "2.23",
"text": "Draw the logic diagram for each expression without simplifying.",
"qs": [
{
"tag": "Mano 2.23 (a)",
"type": "work",
"q": "Draw the logic diagram for <code>BC' + AB + ACD</code> <b>without simplifying</b>.",
"why": "<img src='svg/book/c2-23a.svg' alt='logic diagram'><p>SOP → AND gates into one OR.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.23 (b)",
"type": "work",
"q": "Draw the logic diagram for <code>(A + B)(C + D)(A' + B + D)</code> <b>without simplifying</b>.",
"why": "<img src='svg/book/c2-23b.svg' alt='logic diagram'><p>POS → OR gates into one AND.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.23 (c)",
"type": "work",
"q": "Draw the logic diagram for <code>(AB + A'B')(CD' + C'D)</code> <b>without simplifying</b>.",
"why": "<img src='svg/book/c2-23c.svg' alt='logic diagram'><p>Each bracket is a small SOP (it's XNOR(A,B) and XOR(C,D)); an AND joins them.</p>",
"ref": "06 §1"
},
{
"tag": "Mano 2.23 (d)",
"type": "work",
"q": "Draw the logic diagram for <code>A + CD + (A + D')(C' + D)</code> <b>without simplifying</b>.",
"why": "<img src='svg/book/c2-23d.svg' alt='logic diagram'><p>Three things ORed: A, the AND CD, and the POS block (A + D')(C' + D).</p>",
"ref": "06 §1"
}
]
},
{
"n": "2.24",
"text": "Show that the dual of XOR equals its complement (same as 3.27).",
"qs": [
{
"tag": "Mano 2.24 · also 3.27",
"type": "work",
"q": "Show that the <b>dual</b> of the exclusive-OR is equal to its <b>complement</b>.",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>x ⊕ y = xy' + x'y</td><td>XOR as SOP</td></tr><tr><td>2</td><td>dual = (x + y')(x' + y)</td><td>dual: swap AND ↔ OR (and 0 ↔ 1), keep the letters</td></tr><tr><td>3</td><td>xx' + xy + y'x' + y'y</td><td>multiply out</td></tr><tr><td>4</td><td>xy + x'y'</td><td>xx' = 0, yy' = 0</td></tr><tr><td>5</td><td>(x ⊕ y)' = (xy' + x'y)' = (x' + y)(x + y') = xy + x'y'</td><td>the complement, by De Morgan</td></tr><tr><td>6</td><td><b>dual = complement = XNOR</b></td><td>both are xy + x'y'</td></tr></table>",
"ref": "06 §3"
}
]
},
{
"n": "2.25",
"text": "Inhibition (x/y = xy') and XOR: commutative? associative?",
"qs": [
{
"tag": "Mano 2.25 (a)",
"type": "work",
"q": "Inhibition is <code>x / y = xy'</code> (x but not y). Show it is <b>neither commutative nor associative</b>.",
"why": "<p><b>Commutative?</b> x/y = xy' but y/x = yx'. Try x = 1, y = 0: xy' = 1, yx' = 0. Different, so <b>not commutative</b>.</p><table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(x/y)/z = (xy')z' = xy'z'</td><td>apply the rule twice from the left</td></tr><tr><td>2</td><td>x/(y/z) = x(yz')' = x(y' + z) = xy' + xz</td><td>from the right; De Morgan</td></tr><tr><td>3</td><td>try x = y = z = 1: left = 0, right = 1</td><td>one counter-example is enough</td></tr></table><p>So it's <b>not associative</b> either.</p>",
"ref": "06 §3"
},
{
"tag": "Mano 2.25 (b)",
"type": "work",
"q": "Show that XOR is <b>commutative and associative</b>.",
"why": "<p><b>Commutative:</b> x ⊕ y = xy' + x'y = yx' + y'x = y ⊕ x. ✓</p><table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(x ⊕ y) ⊕ z = (xy' + x'y)z' + (xy' + x'y)'z</td><td>A ⊕ z = Az' + A'z</td></tr><tr><td>2</td><td>= xy'z' + x'yz' + (xy + x'y')z</td><td>the complement of XOR is XNOR</td></tr><tr><td>3</td><td>= xy'z' + x'yz' + xyz + x'y'z</td><td>multiply out</td></tr><tr><td>4</td><td>x ⊕ (y ⊕ z) = x(yz + y'z') + x'(yz' + y'z)</td><td>same rule from the other side</td></tr><tr><td>5</td><td>= xyz + xy'z' + x'yz' + x'y'z</td><td>same four minterms ✓</td></tr></table><p>Both are 1 when an <b>odd</b> number of inputs are 1, so the brackets don't matter.</p>",
"ref": "06 §3"
}
]
},
{
"n": "2.26",
"text": "Positive-logic NAND = negative-logic NOR, and vice versa.",
"qs": [
{
"tag": "Mano 2.26",
"type": "work",
"q": "Show that a positive-logic NAND gate is a negative-logic NOR gate, and vice versa.",
"why": "<table class='bits'><tr><th>x</th><th>y</th><th>NAND (voltages)</th><th>pos: 1=H</th><th>neg: 1=L</th></tr><tr><td>L</td><td>L</td><td>H</td><td>00 → 1</td><td>11 → 0</td></tr><tr><td>L</td><td>H</td><td>H</td><td>01 → 1</td><td>10 → 0</td></tr><tr><td>H</td><td>L</td><td>H</td><td>10 → 1</td><td>01 → 0</td></tr><tr><td>H</td><td>H</td><td>L</td><td>11 → 0</td><td>00 → 1</td></tr></table><p>Write the gate as voltages (H/L). In <b>positive logic</b> H = 1: output 0 only on 11 → <b>NAND</b>. In <b>negative logic</b> L = 1: read the same rows again, output 1 only when both inputs are 0 → <b>NOR</b>.</p><p>Same physical gate, different labels. Swapping 0 ↔ 1 everywhere turns every function into its dual, and the dual of NAND is NOR. The NOR → NAND direction works the same way.</p>",
"ref": "06 §1"
}
]
},
{
"n": "2.27",
"text": "Write the equations and draw the circuit for the f₁, f₂ truth table.",
"qs": [
{
"tag": "Mano 2.27 (f₁)",
"type": "bool",
"q": "Table: <table class='bits'><tr><th>abc</th><td>000</td><td>001</td><td>010</td><td>011</td><td>100</td><td>101</td><td>110</td><td>111</td></tr><tr><th>f₁</th><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><th>f₂</th><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr></table> Write a minimal SOP for <b>f₁</b>.",
"vars": "abc",
"ones": [
0,
3,
6,
7
],
"show": "a'b'c' + bc + ab",
"why": "<p>f₁ = Σm(0, 3, 6, 7).</p><img src='svg/book/k2-27f1.svg' alt=''><p>Row 0 has no neighbouring 1s, so a'b'c' stays as it is. 3 joins 7 (bc), 6 joins 7 (ab).</p>",
"lits": 7,
"ref": "06 §2"
},
{
"tag": "Mano 2.27 (f₂)",
"type": "bool",
"q": "Same table. Write a minimal SOP for <b>f₂</b>.",
"vars": "abc",
"ones": [
2,
3,
4,
5,
6
],
"show": "a'b + ab' + bc'",
"why": "<p>f₂ = Σm(2, 3, 4, 5, 6).</p><img src='svg/book/k2-27f2.svg' alt=''><p>ac' (cells 4, 6) works instead of bc' too. Also f₂ = (a ⊕ b) + bc'.</p>",
"lits": 6,
"ref": "06 §2"
},
{
"tag": "Mano 2.27 (diagram)",
"type": "work",
"q": "Draw the logic diagram for f₁ and f₂.",
"why": "<img src='svg/book/c2-27.svg' alt='circuits'><p>Two AND-OR circuits. Inputs a', b', c' come from inverters (or are drawn as available).</p>",
"ref": "06 §1"
}
]
},
{
"n": "2.28",
"text": "Write the Boolean expressions and truth tables for the two circuits.",
"qs": [
{
"tag": "Mano 2.28 (a)",
"type": "bool",
"q": "Fig 2.28(a): NAND(b, c, d) feeds a 3-input NAND with a and e, then an inverter gives y. Write y.",
"vars": "abcde",
"ones": [
17,
19,
21,
23,
25,
27,
29
],
"show": "ae(b' + c' + d')",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>N₁ = (bcd)'</td><td>first NAND</td></tr><tr><td>2</td><td>N₂ = (a·N₁·e)' = (a(bcd)'e)'</td><td>second NAND</td></tr><tr><td>3</td><td>y = N₂' = a(bcd)'e</td><td>the inverter cancels the bar</td></tr><tr><td>4</td><td><b>y = ae(b' + c' + d')</b></td><td>De Morgan on (bcd)'</td></tr></table><p>Truth table (32 rows): y = 1 only when a = e = 1 and b, c, d are <i>not</i> all 1: rows <b>17, 19, 21, 23, 25, 27, 29</b>. Every other row is 0.</p>",
"ref": "06 §2",
"svg": "book/p2-28a"
},
{
"tag": "Mano 2.28 (b · y₁)",
"type": "bool",
"q": "Fig 2.28(b): write <b>y₁</b>.",
"vars": "abcdef",
"ones": [
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
15,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
48,
49
],
"show": "a ⊕ (c + d + e)",
"why": "<p>The OR gate gives c + d + e. The XOR combines it with a: <b>y₁ = a ⊕ (c + d + e)</b>.</p><p>Truth table: y₁ = 1 when exactly one of a and (c + d + e) is 1. b and f don't matter.</p>",
"ref": "06 §1",
"svg": "book/p2-28b"
},
{
"tag": "Mano 2.28 (b · y₂)",
"type": "bool",
"q": "Fig 2.28(b): write <b>y₂</b>.",
"vars": "abcdef",
"ones": [
3,
5,
7,
9,
11,
13,
15,
35,
37,
39,
41,
43,
45,
47
],
"show": "b'f(c + d + e)",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>NAND(b', c + d + e, f) = (b'(c + d + e)f)'</td><td>3-input NAND</td></tr><tr><td>2</td><td><b>y₂ = b'(c + d + e)f</b></td><td>the inverter cancels the bar</td></tr></table><p>Truth table: y₂ = 1 only when b = 0, f = 1 and at least one of c, d, e is 1. a doesn't matter.</p>",
"ref": "06 §1",
"svg": "book/p2-28b"
}
]
},
{
"n": "4.1",
"text": "Analyse the circuit of Fig P4.1: T₁ to T₄, F₁, F₂, truth table, maps.",
"qs": [
{
"tag": "Mano 4.1 (a · F₁) ★",
"type": "bool",
"q": "Fig P4.1: write T₁ to T₄, then <b>F₁</b> in terms of A, B, C, D.",
"vars": "ABCD",
"ones": [
1,
2,
3,
4,
6,
8,
9,
10,
11,
12,
13,
14,
15
],
"show": "A + (B ⊕ D) + B'C",
"why": "<p>T₁ = <b>B'C</b> · T₂ = <b>A'B</b> · T₃ = A + T₁ = <b>A + B'C</b> · T₄ = T₂ ⊕ D = <b>A'B ⊕ D</b></p><table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>F₁ = T₃ + T₄ = A + B'C + (A'B ⊕ D)</td><td>OR of T₃ and T₄</td></tr><tr><td>2</td><td>A'B ⊕ D = A'BD' + (A + B')D</td><td>P ⊕ D = PD' + P'D, De Morgan on (A'B)'</td></tr><tr><td>3</td><td>F₁ = A + B'C + A'BD' + AD + B'D</td><td>substitute</td></tr><tr><td>4</td><td>F₁ = A + B'C + BD' + B'D</td><td>A + A'BD' = A + BD', AD absorbed by A</td></tr><tr><td>5</td><td><b>F₁ = A + B'C + (B ⊕ D)</b></td><td>BD' + B'D = B ⊕ D</td></tr></table>",
"ref": "06 §4",
"svg": "book/p4-1"
},
{
"tag": "Mano 4.1 (a · F₂) ★",
"type": "bool",
"q": "Fig P4.1: write <b>F₂</b> in terms of A, B, C, D.",
"vars": "ABCD",
"ones": [
1,
3,
4,
5,
6,
7,
9,
11,
13,
15
],
"show": "A'B + D",
"why": "<p>F₂ = T₂ + D = <b>A'B + D</b>.</p>",
"ref": "06 §4",
"svg": "book/p4-1"
},
{
"tag": "Mano 4.1 (b)",
"type": "tt",
"q": "Fig P4.1: list T₁, T₂, T₃, T₄, F₁, F₂ for all 16 input combinations.",
"vars": "ABCD",
"outs": {
"T₁": [
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
1,
1,
0,
0,
0,
0
],
"T₂": [
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
0,
0,
0,
0
],
"T₃": [
0,
0,
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
1,
1,
1,
1
],
"T₄": [
0,
1,
0,
1,
1,
0,
1,
0,
0,
1,
0,
1,
0,
1,
0,
1
],
"F₁": [
0,
1,
1,
1,
1,
0,
1,
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
"F₂": [
0,
1,
0,
1,
1,
1,
1,
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
"why": "<p>Fill T₁ and T₂ first (they only need two inputs each), then build T₃, T₄ from them, then F₁, F₂.</p><p>Check: F₁ is 0 only on rows 0, 5, 7. F₂ is 0 only on rows 0, 2, 8, 10, 12, 14.</p>",
"ref": "06 §2",
"svg": "book/p4-1"
},
{
"tag": "Mano 4.1 (c)",
"type": "work",
"q": "Plot F₁ and F₂ from your table on K-maps and show they simplify to the same expressions as (a).",
"why": "<img src='svg/book/k4-1f1.svg' alt=''><img src='svg/book/k4-1f2.svg' alt=''><p>F₁ = A + B'D + BD' + B'C = A + (B ⊕ D) + B'C ✓. F₂ = A'B + D ✓. (CD' also works instead of B'C in F₁.)</p>",
"ref": "06 §4"
}
]
},
{
"n": "4.2",
"text": "Simplified F and G for the circuit of Fig P4.2.",
"qs": [
{
"tag": "Mano 4.2 (F) ★",
"type": "bool",
"q": "Fig P4.2: find the simplified expression for <b>F</b>.",
"vars": "ABCD",
"ones": [
1,
3,
5,
7,
14,
15
],
"show": "ABC + A'D",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>N₁ = (A'D)' = A + D'</td><td>NAND, then De Morgan</td></tr><tr><td>2</td><td>N₂ = (A'·N₁)' = (A'(A + D'))' = (A'D')' = A + D</td><td>A'A = 0 inside</td></tr><tr><td>3</td><td>OR output = A' + BC</td><td></td></tr><tr><td>4</td><td>F = N₂(A' + BC) = (A + D)(A' + BC)</td><td>the AND gate</td></tr><tr><td>5</td><td>AA' + ABC + A'D + BCD</td><td>multiply out</td></tr><tr><td>6</td><td><b>ABC + A'D</b></td><td>AA' = 0, BCD is the consensus of ABC and A'D</td></tr></table>",
"lits": 5,
"ref": "06 §4",
"svg": "book/p4-2"
},
{
"tag": "Mano 4.2 (G) ★",
"type": "bool",
"q": "Fig P4.2: find the simplified expression for <b>G</b>.",
"vars": "ABCD",
"ones": [
0,
2,
4,
6,
14,
15
],
"show": "ABC + A'D'",
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>G = (A' + BC)·N₁ = (A' + BC)(A + D')</td><td>the second AND gate</td></tr><tr><td>2</td><td>A'A + A'D' + ABC + BCD'</td><td>multiply out</td></tr><tr><td>3</td><td><b>ABC + A'D'</b></td><td>A'A = 0, BCD' is the consensus of ABC and A'D'</td></tr></table>",
"lits": 5,
"ref": "06 §4",
"svg": "book/p4-2"
}
]
}
]
});
