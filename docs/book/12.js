BOOK.add({
"id": "12",
"title": "Multiplexers",
"intro": "Mano 4.3, 4.31–4.35. For data inputs type 0, 1, D or D' (or an expression in C and D).",
"problems": [
{
"n": "4.3",
"text": "The quadruple 2-to-1 multiplexer of Fig 4.26.",
"qs": [
{
"tag": "Mano 4.3 (a)",
"type": "work",
"q": "Fig 4.26 (4th ed.) is the <b>quadruple 2-to-1 multiplexer</b>: inputs A₃–A₀, B₃–B₀, select S, enable E (active-low). Write the four outputs.",
"why": "<p>E = 1 disables (all outputs 0). E = 0: S = 0 picks A, S = 1 picks B.</p><p><b>Yᵢ = E'(S'Aᵢ + SBᵢ)</b> for i = 0, 1, 2, 3.</p>",
"ref": "12 §1",
"grp": 0,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.3 (b) ★",
"type": "multi",
"q": "If that circuit were listed in a truth table, how many rows and columns would it have?",
"fields": [
{
"label": "rows",
"ans": [
"1024",
"1,024"
]
},
{
"label": "columns",
"ans": [
"14"
]
}
],
"why": "<p>Inputs: 4 (A) + 4 (B) + S + E = 10 → 2¹⁰ = <b>1024 rows</b>. Columns: 10 inputs + 4 outputs = <b>14</b>.</p>",
"ref": "12 §1",
"grp": 0,
"core": true,
"corder": 2
}
]
},
{
"n": "4.31",
"text": "16 × 1 multiplexer from smaller ones.",
"qs": [
{
"tag": "Mano 4.31",
"type": "work",
"q": "Build a 16 × 1 multiplexer from two 8 × 1 and one 2 × 1 multiplexers (block diagram).",
"why": "<p>The low three select bits S₂S₁S₀ pick one input inside each 8 × 1 (both at once). The top bit S₃ then picks which half: I₀–I₇ or I₈–I₁₅.</p><img src='svg/book/b4-31.svg' alt=''>",
"ref": "12 §2",
"grp": 0,
"core": false
}
]
},
{
"n": "4.32",
"text": "Implement functions with a multiplexer.",
"qs": [
{
"tag": "Mano 4.32 (a)",
"type": "multi",
"q": "Implement <code>F(A, B, C, D) = Σ(0, 2, 5, 7, 11, 14)</code> with an 8 × 1 multiplexer: A, B, C on the selects, D (or D', 0, 1) on the data inputs. Fill I₀ … I₇.",
"fields": [
{
"label": "I₀",
"ans": [
"D'"
]
},
{
"label": "I₁",
"ans": [
"D'"
]
},
{
"label": "I₂",
"ans": [
"D"
]
},
{
"label": "I₃",
"ans": [
"D"
]
},
{
"label": "I₄",
"ans": [
"0"
]
},
{
"label": "I₅",
"ans": [
"D"
]
},
{
"label": "I₆",
"ans": [
"0"
]
},
{
"label": "I₇",
"ans": [
"D'"
]
}
],
"why": "<p>Take the rows in pairs (D = 0 and D = 1) for each ABC:</p><table class='bits'><tr><th>I</th><th>ABC</th><th>m (D=0)</th><th>F</th><th>m (D=1)</th><th>F</th><th>input</th></tr><tr><td>0</td><td>000</td><td>0</td><td>1</td><td>1</td><td>0</td><td><b>D'</b></td></tr><tr><td>1</td><td>001</td><td>2</td><td>1</td><td>3</td><td>0</td><td><b>D'</b></td></tr><tr><td>2</td><td>010</td><td>4</td><td>0</td><td>5</td><td>1</td><td><b>D</b></td></tr><tr><td>3</td><td>011</td><td>6</td><td>0</td><td>7</td><td>1</td><td><b>D</b></td></tr><tr><td>4</td><td>100</td><td>8</td><td>0</td><td>9</td><td>0</td><td><b>0</b></td></tr><tr><td>5</td><td>101</td><td>10</td><td>0</td><td>11</td><td>1</td><td><b>D</b></td></tr><tr><td>6</td><td>110</td><td>12</td><td>0</td><td>13</td><td>0</td><td><b>0</b></td></tr><tr><td>7</td><td>111</td><td>14</td><td>1</td><td>15</td><td>0</td><td><b>D'</b></td></tr></table><p>Both 0 → 0, both 1 → 1, F = D → D, F = D' → D'.</p><img src='svg/book/b4-32a.svg' alt=''>",
"ref": "12 §4",
"grp": 2,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.32 (b)",
"type": "multi",
"q": "Implement <code>F(A, B, C, D) = Π(3, 8, 12)</code> with an 8 × 1 multiplexer: A, B, C on the selects, D (or D', 0, 1) on the data inputs. Fill I₀ … I₇.",
"fields": [
{
"label": "I₀",
"ans": [
"1"
]
},
{
"label": "I₁",
"ans": [
"D'"
]
},
{
"label": "I₂",
"ans": [
"1"
]
},
{
"label": "I₃",
"ans": [
"1"
]
},
{
"label": "I₄",
"ans": [
"D"
]
},
{
"label": "I₅",
"ans": [
"1"
]
},
{
"label": "I₆",
"ans": [
"D"
]
},
{
"label": "I₇",
"ans": [
"1"
]
}
],
"why": "<p>Take the rows in pairs (D = 0 and D = 1) for each ABC:</p><table class='bits'><tr><th>I</th><th>ABC</th><th>m (D=0)</th><th>F</th><th>m (D=1)</th><th>F</th><th>input</th></tr><tr><td>0</td><td>000</td><td>0</td><td>1</td><td>1</td><td>1</td><td><b>1</b></td></tr><tr><td>1</td><td>001</td><td>2</td><td>1</td><td>3</td><td>0</td><td><b>D'</b></td></tr><tr><td>2</td><td>010</td><td>4</td><td>1</td><td>5</td><td>1</td><td><b>1</b></td></tr><tr><td>3</td><td>011</td><td>6</td><td>1</td><td>7</td><td>1</td><td><b>1</b></td></tr><tr><td>4</td><td>100</td><td>8</td><td>0</td><td>9</td><td>1</td><td><b>D</b></td></tr><tr><td>5</td><td>101</td><td>10</td><td>1</td><td>11</td><td>1</td><td><b>1</b></td></tr><tr><td>6</td><td>110</td><td>12</td><td>0</td><td>13</td><td>1</td><td><b>D</b></td></tr><tr><td>7</td><td>111</td><td>14</td><td>1</td><td>15</td><td>1</td><td><b>1</b></td></tr></table><p>Both 0 → 0, both 1 → 1, F = D → D, F = D' → D'.</p><img src='svg/book/b4-32b.svg' alt=''>",
"ref": "12 §4",
"grp": 2,
"core": false
}
]
},
{
"n": "4.33",
"text": "Full adder from two 4 × 1 multiplexers.",
"qs": [
{
"tag": "Mano 4.33",
"type": "multi",
"q": "Implement a full adder (inputs x, y, z) with two 4 × 1 multiplexers, x and y on the selects. What goes on each data input?",
"fields": [
{
"label": "S: I₀",
"ans": [
"z"
]
},
{
"label": "S: I₁",
"ans": [
"z'"
]
},
{
"label": "S: I₂",
"ans": [
"z'"
]
},
{
"label": "S: I₃",
"ans": [
"z"
]
},
{
"label": "C: I₀",
"ans": [
"0"
]
},
{
"label": "C: I₁",
"ans": [
"z"
]
},
{
"label": "C: I₂",
"ans": [
"z"
]
},
{
"label": "C: I₃",
"ans": [
"1"
]
}
],
"why": "<p>For each xy, write S and C as a function of z alone:</p><table class='bits'><tr><th>xy</th><th>S</th><th>C</th></tr><tr><td>00</td><td>z</td><td>0</td></tr><tr><td>01</td><td>z'</td><td>z</td></tr><tr><td>10</td><td>z'</td><td>z</td></tr><tr><td>11</td><td>z</td><td>1</td></tr></table><img src='svg/book/b4-33.svg' alt=''>",
"ref": "12 §4",
"grp": 2,
"core": true,
"corder": 2
}
]
},
{
"n": "4.34",
"text": "Find the function a multiplexer implements.",
"qs": [
{
"tag": "Mano 4.34 (a) ★",
"type": "multi",
"q": "An 8 × 1 mux has A, B, C on S₂, S₁, S₀. Data: I₀ = D, I₁ = 0, I₂ = 0, I₃ = 1, I₄ = D, I₅ = 1, I₆ = D', I₇ = 0. Which function F(A, B, C, D) does it implement? Give the minterms.",
"fields": [
{
"label": "Σm(",
"ans": [
"1,6,7,9,10,11,12",
"(1,6,7,9,10,11,12)",
"Σ(1,6,7,9,10,11,12)",
"Σm(1,6,7,9,10,11,12)",
"m(1,6,7,9,10,11,12)",
"Π(1,6,7,9,10,11,12)",
"ΠM(1,6,7,9,10,11,12)",
"M(1,6,7,9,10,11,12)"
]
}
],
"why": "<p>Input Iᵢ covers minterms 2i (D = 0) and 2i + 1 (D = 1). 1 → both, D → the odd one, D' → the even one, 0 → neither.</p><table class='bits'><tr><th>I</th><th>value</th><th>minterms</th></tr><tr><td>0</td><td>D</td><td>1</td></tr><tr><td>1</td><td>0</td><td>–</td></tr><tr><td>2</td><td>0</td><td>–</td></tr><tr><td>3</td><td>1</td><td>6, 7</td></tr><tr><td>4</td><td>D</td><td>9</td></tr><tr><td>5</td><td>1</td><td>10, 11</td></tr><tr><td>6</td><td>D'</td><td>12</td></tr><tr><td>7</td><td>0</td><td>–</td></tr></table><p><b>F = Σ(1, 6, 7, 9, 10, 11, 12)</b> = AB'C + A'BC + B'C'D + ABC'D' (minimal SOP).</p>",
"ref": "12 §4",
"grp": 1,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.34 (b)",
"type": "multi",
"q": "An 8 × 1 mux has A, B, C on S₂, S₁, S₀. Data: I₀ = D', I₁ = 0, I₂ = 0, I₃ = 1, I₄ = D, I₅ = D, I₆ = D', I₇ = 1. Which function F(A, B, C, D) does it implement? Give the minterms.",
"fields": [
{
"label": "Σm(",
"ans": [
"0,6,7,9,11,12,14,15",
"(0,6,7,9,11,12,14,15)",
"Σ(0,6,7,9,11,12,14,15)",
"Σm(0,6,7,9,11,12,14,15)",
"m(0,6,7,9,11,12,14,15)",
"Π(0,6,7,9,11,12,14,15)",
"ΠM(0,6,7,9,11,12,14,15)",
"M(0,6,7,9,11,12,14,15)"
]
}
],
"why": "<p>Input Iᵢ covers minterms 2i (D = 0) and 2i + 1 (D = 1). 1 → both, D → the odd one, D' → the even one, 0 → neither.</p><table class='bits'><tr><th>I</th><th>value</th><th>minterms</th></tr><tr><td>0</td><td>D'</td><td>0</td></tr><tr><td>1</td><td>0</td><td>–</td></tr><tr><td>2</td><td>0</td><td>–</td></tr><tr><td>3</td><td>1</td><td>6, 7</td></tr><tr><td>4</td><td>D</td><td>9</td></tr><tr><td>5</td><td>D</td><td>11</td></tr><tr><td>6</td><td>D'</td><td>12</td></tr><tr><td>7</td><td>1</td><td>14, 15</td></tr></table><p><b>F = Σ(0, 6, 7, 9, 11, 12, 14, 15)</b> = BC + ABD' + AB'D + A'B'C'D' (minimal SOP).</p>",
"ref": "12 §4",
"grp": 1,
"core": false
}
]
},
{
"n": "4.35",
"text": "4 × 1 multiplexer with external gates.",
"qs": [
{
"tag": "Mano 4.35 (a · I0) ★",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 3, 4, 11, 12, 13, 14, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₀</b> (AB = 00)? Write it in C and D.",
"vars": "CD",
"ones": [
1,
3
],
"show": "D",
"why": "<p>AB = 00 covers minterms 0–3, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 01, 11.</p><p><b>I₀ = D</b>.</p>",
"ref": "12 §4",
"grp": 3,
"core": true,
"corder": 1
},
{
"tag": "Mano 4.35 (a · I1) ★",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 3, 4, 11, 12, 13, 14, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₁</b> (AB = 01)? Write it in C and D.",
"vars": "CD",
"ones": [
0
],
"show": "C'D'",
"why": "<p>AB = 01 covers minterms 4–7, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 00.</p><p><b>I₁ = C'D'</b>.</p>",
"ref": "12 §4",
"grp": 3,
"core": true,
"corder": 2
},
{
"tag": "Mano 4.35 (a · I2) ★",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 3, 4, 11, 12, 13, 14, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₂</b> (AB = 10)? Write it in C and D.",
"vars": "CD",
"ones": [
3
],
"show": "CD",
"why": "<p>AB = 10 covers minterms 8–11, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 11.</p><p><b>I₂ = CD</b>.</p>",
"ref": "12 §4",
"grp": 3,
"core": true,
"corder": 3
},
{
"tag": "Mano 4.35 (a · I3) ★",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 3, 4, 11, 12, 13, 14, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₃</b> (AB = 11)? Write it in C and D.",
"vars": "CD",
"ones": [
0,
1,
2,
3
],
"show": "1",
"why": "<p>AB = 11 covers minterms 12–15, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 00, 01, 10, 11.</p><p><b>I₃ = 1</b> (tie to logic 1).</p><img src='svg/book/b4-35a.svg' alt=''>",
"ref": "12 §4",
"grp": 3,
"core": true,
"corder": 4
},
{
"tag": "Mano 4.35 (b · I0)",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 2, 4, 7, 8, 9, 10, 11, 13, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₀</b> (AB = 00)? Write it in C and D.",
"vars": "CD",
"ones": [
1,
2
],
"show": "C ⊕ D",
"why": "<p>AB = 00 covers minterms 0–3, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 01, 10.</p><p><b>I₀ = C ⊕ D</b>.</p>",
"ref": "12 §4",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.35 (b · I1)",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 2, 4, 7, 8, 9, 10, 11, 13, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₁</b> (AB = 01)? Write it in C and D.",
"vars": "CD",
"ones": [
0,
3
],
"show": "C ⊙ D",
"why": "<p>AB = 01 covers minterms 4–7, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 00, 11.</p><p><b>I₁ = C ⊙ D</b>.</p>",
"ref": "12 §4",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.35 (b · I2)",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 2, 4, 7, 8, 9, 10, 11, 13, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₂</b> (AB = 10)? Write it in C and D.",
"vars": "CD",
"ones": [
0,
1,
2,
3
],
"show": "1",
"why": "<p>AB = 10 covers minterms 8–11, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 00, 01, 10, 11.</p><p><b>I₂ = 1</b> (tie to logic 1).</p>",
"ref": "12 §4",
"grp": 3,
"core": false
},
{
"tag": "Mano 4.35 (b · I3)",
"type": "bool",
"q": "F(A, B, C, D) = Σ(1, 2, 4, 7, 8, 9, 10, 11, 13, 15) on a 4 × 1 mux, A B on the selects. What goes on data input <b>I₃</b> (AB = 11)? Write it in C and D.",
"vars": "CD",
"ones": [
1,
3
],
"show": "D",
"why": "<p>AB = 11 covers minterms 12–15, i.e. CD = 00, 01, 10, 11. F is 1 on CD = 01, 11.</p><p><b>I₃ = D</b>.</p><img src='svg/book/b4-35b.svg' alt=''>",
"ref": "12 §4",
"grp": 3,
"core": false
}
]
}
],
"groups": [
{
"name": "How a mux works",
"blurb": "Select lines pick which data input reaches the output."
},
{
"name": "Read a mux circuit",
"blurb": "Each data input covers two minterms."
},
{
"name": "Any function on a mux",
"blurb": "Pair the rows: 0, 1, D or D' on each input."
},
{
"name": "One size smaller, plus gates",
"blurb": "Each data input becomes a small function of the leftover variables."
}
]
});
