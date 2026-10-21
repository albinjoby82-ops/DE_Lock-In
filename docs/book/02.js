BOOK.add({
"id": "02",
"title": "Number systems",
"intro": "Mano 1.1–1.10, 1.13. Type plain numbers; commas are fine.",
"problems": [
{
"n": "1.1",
"text": "Octal and hex for 16 to 32; base 13 (digits A, B, C) for 8 to 28.",
"qs": [
{
"tag": "Mano 1.1",
"type": "multi",
"q": "Write the octal and hexadecimal lists for decimal 16 to 32, and the base-13 list for 8 to 28 (A, B, C are the last three digits). Then fill these spot checks.",
"fields": [
{
"label": "25 in octal",
"ans": [
"31"
]
},
{
"label": "32 in octal",
"ans": [
"40"
]
},
{
"label": "26 in hex",
"ans": [
"1A"
]
},
{
"label": "31 in hex",
"ans": [
"1F"
]
},
{
"label": "12 in base 13",
"ans": [
"C"
]
},
{
"label": "13 in base 13",
"ans": [
"10"
]
},
{
"label": "25 in base 13",
"ans": [
"1C"
]
},
{
"label": "28 in base 13",
"ans": [
"22"
]
}
],
"why": "<table class='bits'><tr><th>dec</th><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td><td>29</td><td>30</td><td>31</td><td>32</td></tr><tr><th>oct</th><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>30</td><td>31</td><td>32</td><td>33</td><td>34</td><td>35</td><td>36</td><td>37</td><td>40</td></tr><tr><th>hex</th><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>1A</td><td>1B</td><td>1C</td><td>1D</td><td>1E</td><td>1F</td><td>20</td></tr></table><table class='bits'><tr><th>dec</th><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td></tr><tr><th>b13</th><td>8</td><td>9</td><td>A</td><td>B</td><td>C</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>1A</td><td>1B</td><td>1C</td><td>20</td><td>21</td><td>22</td></tr></table><p>Counting rule: when the last digit runs out (7 in octal, F in hex, C in base 13), it goes back to 0 and the next digit goes up by 1.</p>",
"ref": "02 §0",
"grp": 3,
"core": false
}
]
},
{
"n": "1.2",
"text": "Exact bytes in 32K, 64M and 6.4G bytes.",
"qs": [
{
"tag": "Mano 1.2 ★",
"type": "multi",
"q": "What is the exact number of bytes in (a) 32K bytes, (b) 64M bytes, (c) 6.4G bytes? (K = 2¹⁰, M = 2²⁰, G = 2³⁰)",
"fields": [
{
"label": "(a) 32K",
"ans": [
"32768",
"32,768"
]
},
{
"label": "(b) 64M",
"ans": [
"67108864",
"67,108,864"
]
},
{
"label": "(c) 6.4G",
"ans": [
"6871947674",
"6,871,947,674",
"6871947673.6",
"6,871,947,673.6"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>32K = 32 × 2¹⁰ = 2⁵ × 2¹⁰ = 2¹⁵</td><td>K = 1024</td></tr><tr><td>2</td><td>= 32,768 bytes</td><td></td></tr><tr><td>3</td><td>64M = 2⁶ × 2²⁰ = 2²⁶ = 67,108,864 bytes</td><td>M = 1,048,576</td></tr><tr><td>4</td><td>6.4G = 6.4 × 1,073,741,824 = 6,871,947,673.6 ≈ 6,871,947,674 bytes</td><td>G = 1,073,741,824</td></tr></table>",
"ref": "02 §0",
"grp": 3,
"core": true,
"corder": 2
}
]
},
{
"n": "1.3",
"text": "Convert to decimal.",
"qs": [
{
"tag": "Mano 1.3 (a) ★",
"type": "multi",
"q": "Convert (<b>4310</b>)<sub>5</sub> to decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"580",
"580"
]
}
],
"why": "<p>4×5<sup>3</sup> + 3×5<sup>2</sup> + 1×5<sup>1</sup> + 0×5<sup>0</sup> = 500 + 75 + 5 + 0 = <b>580</b></p>",
"ref": "02 §1",
"grp": 0,
"core": true,
"corder": 1
},
{
"tag": "Mano 1.3 (b) ★",
"type": "multi",
"q": "Convert (<b>198</b>)<sub>12</sub> to decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"260",
"260"
]
}
],
"why": "<p>1×12<sup>2</sup> + 9×12<sup>1</sup> + 8×12<sup>0</sup> = 144 + 108 + 8 = <b>260</b></p>",
"ref": "02 §1",
"grp": 0,
"core": false
},
{
"tag": "Mano 1.3 (c)",
"type": "multi",
"q": "Convert (<b>735</b>)<sub>8</sub> to decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"477",
"477"
]
}
],
"why": "<p>7×8<sup>2</sup> + 3×8<sup>1</sup> + 5×8<sup>0</sup> = 448 + 24 + 5 = <b>477</b></p>",
"ref": "02 §1",
"grp": 0,
"core": false
},
{
"tag": "Mano 1.3 (d)",
"type": "multi",
"q": "Convert (<b>525</b>)<sub>6</sub> to decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"197",
"197"
]
}
],
"why": "<p>5×6<sup>2</sup> + 2×6<sup>1</sup> + 5×6<sup>0</sup> = 180 + 12 + 5 = <b>197</b></p>",
"ref": "02 §1",
"grp": 0,
"core": false
}
]
},
{
"n": "1.4",
"text": "Largest 14-bit binary number in decimal and hex.",
"qs": [
{
"tag": "Mano 1.4",
"type": "multi",
"q": "What is the largest binary number with 14 bits? Give it in decimal and hexadecimal.",
"fields": [
{
"label": "binary",
"ans": [
"11111111111111"
]
},
{
"label": "decimal",
"ans": [
"16383",
"16,383"
]
},
{
"label": "hex",
"ans": [
"3FFF"
]
}
],
"why": "<p>All 14 bits are 1: <b>11111111111111</b> = 2¹⁴ − 1 = 16,384 − 1 = <b>16,383</b>.</p><p>Hex: group in 4s from the right: 11 1111 1111 1111 → <b>3FFF</b>.</p>",
"ref": "02 §4",
"grp": 3,
"core": true,
"corder": 1
}
]
},
{
"n": "1.5",
"text": "Find the base that makes each sum correct.",
"qs": [
{
"tag": "Mano 1.5 (a) ★",
"type": "multi",
"q": "Find base b so that <code>14 / 2 = 5</code> is correct.",
"fields": [
{
"label": "b",
"ans": [
"6"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>14 in base b = b + 4</td><td>digit × place value</td></tr><tr><td>2</td><td>(b + 4) / 2 = 5</td><td></td></tr><tr><td>3</td><td><b>b + 4 = 10 → b = 6</b></td><td>check: 14₆ = 10, and 10 / 2 = 5 ✓</td></tr></table>",
"ref": "02 §1",
"grp": 4,
"core": true,
"corder": 1
},
{
"tag": "Mano 1.5 (b) ★",
"type": "multi",
"q": "Find base b so that <code>54 / 4 = 13</code> is correct.",
"fields": [
{
"label": "b",
"ans": [
"8"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(5b + 4) / 4 = b + 3</td><td>both sides in base b</td></tr><tr><td>2</td><td>5b + 4 = 4b + 12</td><td>multiply by 4</td></tr><tr><td>3</td><td><b>b = 8</b></td><td>check: 54₈ = 44, 13₈ = 11, and 44 / 4 = 11 ✓</td></tr></table>",
"ref": "02 §1",
"grp": 4,
"core": false
},
{
"tag": "Mano 1.5 (c) ★",
"type": "multi",
"q": "Find base b so that <code>24 + 17 = 40</code> is correct.",
"fields": [
{
"label": "b",
"ans": [
"11"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(2b + 4) + (b + 7) = 4b</td><td>both sides in base b</td></tr><tr><td>2</td><td>3b + 11 = 4b</td><td></td></tr><tr><td>3</td><td><b>b = 11</b></td><td>check: 24₁₁ = 26, 17₁₁ = 18, 40₁₁ = 44, and 26 + 18 = 44 ✓</td></tr></table>",
"ref": "02 §1",
"grp": 4,
"core": false
}
]
},
{
"n": "1.6",
"text": "Base where x² − 11x + 22 = 0 has roots 3 and 6.",
"qs": [
{
"tag": "Mano 1.6 ★",
"type": "multi",
"q": "The solutions of <code>x² − 11x + 22 = 0</code> are x = 3 and x = 6. What base are the numbers in?",
"fields": [
{
"label": "base",
"ans": [
"8"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>(x − 3)(x − 6) = x² − 9x + 18</td><td>the roots tell you the factors</td></tr><tr><td>2</td><td>11 in base b = 9 → b + 1 = 9</td><td>match the middle term</td></tr><tr><td>3</td><td>22 in base b = 18 → 2b + 2 = 18</td><td>match the last term</td></tr><tr><td>4</td><td><b>b = 8</b></td><td>both agree</td></tr></table>",
"ref": "02 §1",
"grp": 4,
"core": true,
"corder": 2
}
]
},
{
"n": "1.7",
"text": "Hex 68BE to binary, then to octal.",
"qs": [
{
"tag": "Mano 1.7 ★",
"type": "multi",
"q": "Convert hex <b>68BE</b> to binary, then from binary to octal.",
"fields": [
{
"label": "binary",
"ans": [
"110100010111110",
"0110100010111110",
"0110100010111110",
"0110 1000 1011 1110"
]
},
{
"label": "octal",
"ans": [
"64276"
]
}
],
"why": "<p>Each hex digit → 4 bits: 6 = 0110, 8 = 1000, B = 1011, E = 1110 → <b>0110 1000 1011 1110</b>.</p><p>Regroup in 3s from the right: 110 100 010 111 110 → 6 4 2 7 6 → <b>64276</b>₈.</p>",
"ref": "02 §4",
"grp": 2,
"core": true,
"corder": 1
}
]
},
{
"n": "1.8",
"text": "431 to binary two ways.",
"qs": [
{
"tag": "Mano 1.8",
"type": "multi",
"q": "Convert decimal 431 to binary (a) directly, (b) via hexadecimal. Which is faster?",
"fields": [
{
"label": "binary",
"ans": [
"110101111",
"000110101111"
]
},
{
"label": "hex",
"ans": [
"1AF"
]
}
],
"why": "<p><b>(a)</b> Divide by 2 nine times:</p><table class='wk'><tr><th>#</th><th>Divide</th><th></th></tr><tr><td>1</td><td>431 ÷ 2 = 215 rem <b>1</b></td><td></td></tr><tr><td>2</td><td>215 ÷ 2 = 107 rem <b>1</b></td><td></td></tr><tr><td>3</td><td>107 ÷ 2 = 53 rem <b>1</b></td><td></td></tr><tr><td>4</td><td>53 ÷ 2 = 26 rem <b>1</b></td><td></td></tr><tr><td>5</td><td>26 ÷ 2 = 13 rem <b>0</b></td><td></td></tr><tr><td>6</td><td>13 ÷ 2 = 6 rem <b>1</b></td><td></td></tr><tr><td>7</td><td>6 ÷ 2 = 3 rem <b>0</b></td><td></td></tr><tr><td>8</td><td>3 ÷ 2 = 1 rem <b>1</b></td><td></td></tr><tr><td>9</td><td>1 ÷ 2 = 0 rem <b>1</b></td><td></td></tr></table><p>Read the remainders <b>bottom to top</b>.</p><p><b>(b)</b> Divide by 16 only twice:</p><table class='wk'><tr><th>#</th><th>Divide</th><th></th></tr><tr><td>1</td><td>431 ÷ 16 = 26 rem <b>F</b></td><td></td></tr><tr><td>2</td><td>26 ÷ 16 = 1 rem <b>A</b></td><td></td></tr><tr><td>3</td><td>1 ÷ 16 = 0 rem <b>1</b></td><td></td></tr></table><p>Read the remainders <b>bottom to top</b>.</p><p>1AF → 0001 1010 1111 = <b>110101111</b>. Going through hex is <b>faster</b>: 2 divisions instead of 9.</p>",
"ref": "02 §2",
"grp": 1,
"core": true,
"corder": 1
}
]
},
{
"n": "1.9",
"text": "Express in decimal.",
"qs": [
{
"tag": "Mano 1.9 (a) ★",
"type": "multi",
"q": "Express (<b>10110.0101</b>)<sub>2</sub> in decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"22.3125",
"22.3125"
]
}
],
"why": "<p>Whole part: 1×2<sup>4</sup> + 0×2<sup>3</sup> + 1×2<sup>2</sup> + 1×2<sup>1</sup> + 0×2<sup>0</sup> = 16 + 0 + 4 + 2 + 0 = <b>22</b></p><p>Fraction: 0×2<sup>−1</sup> + 1×2<sup>−2</sup> + 0×2<sup>−3</sup> + 1×2<sup>−4</sup> = 0.3125</p><p>Total: <b>22.3125</b></p>",
"ref": "02 §1",
"grp": 0,
"core": false
},
{
"tag": "Mano 1.9 (b) ★",
"type": "multi",
"q": "Express (<b>16.5</b>)<sub>16</sub> in decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"22.3125",
"22.3125"
]
}
],
"why": "<p>Whole part: 1×16<sup>1</sup> + 6×16<sup>0</sup> = 16 + 6 = <b>22</b></p><p>Fraction: 5×16<sup>−1</sup> = 0.3125</p><p>Total: <b>22.3125</b></p>",
"ref": "02 §1",
"grp": 0,
"core": false
},
{
"tag": "Mano 1.9 (c) ★",
"type": "multi",
"q": "Express (<b>26.24</b>)<sub>8</sub> in decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"22.3125",
"22.3125"
]
}
],
"why": "<p>Whole part: 2×8<sup>1</sup> + 6×8<sup>0</sup> = 16 + 6 = <b>22</b></p><p>Fraction: 2×8<sup>−1</sup> + 4×8<sup>−2</sup> = 0.3125</p><p>Total: <b>22.3125</b></p><p>Notice (a), (b) and (c) are all 22.3125: the same number in three bases.</p>",
"ref": "02 §1",
"grp": 0,
"core": true,
"corder": 2
},
{
"tag": "Mano 1.9 (d)",
"type": "multi",
"q": "Express (<b>FAFA</b>)<sub>16</sub> in decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"64250",
"64,250"
]
}
],
"why": "<p>Whole part: F×16<sup>3</sup> + A×16<sup>2</sup> + F×16<sup>1</sup> + A×16<sup>0</sup> = 61440 + 2560 + 240 + 10 = <b>64250</b></p><p>Total: <b>64250</b></p>",
"ref": "02 §1",
"grp": 0,
"core": false
},
{
"tag": "Mano 1.9 (e)",
"type": "multi",
"q": "Express (<b>1010.1010</b>)<sub>2</sub> in decimal.",
"fields": [
{
"label": "decimal",
"ans": [
"10.625",
"10.625"
]
}
],
"why": "<p>Whole part: 1×2<sup>3</sup> + 0×2<sup>2</sup> + 1×2<sup>1</sup> + 0×2<sup>0</sup> = 8 + 0 + 2 + 0 = <b>10</b></p><p>Fraction: 1×2<sup>−1</sup> + 0×2<sup>−2</sup> + 1×2<sup>−3</sup> + 0×2<sup>−4</sup> = 0.625</p><p>Total: <b>10.625</b></p>",
"ref": "02 §1",
"grp": 0,
"core": false
}
]
},
{
"n": "1.10",
"text": "1.10010 and 110.010 to hex and decimal.",
"qs": [
{
"tag": "Mano 1.10",
"type": "multi",
"q": "Convert binary (a) <b>1.10010</b> and (b) <b>110.010</b> to hexadecimal and to decimal. Why is (b) 4 × (a)?",
"fields": [
{
"label": "(a) hex",
"ans": [
"1.9",
"1.90"
]
},
{
"label": "(a) decimal",
"ans": [
"1.5625"
]
},
{
"label": "(b) hex",
"ans": [
"6.4"
]
},
{
"label": "(b) decimal",
"ans": [
"6.25"
]
}
],
"why": "<p>Group in 4s <b>away from the point</b>, padding with 0s: 1 . 1001 0(000) → <b>1.9</b>₁₆ = 1 + 9/16 = <b>1.5625</b>.</p><p>110 . 010(0) → <b>6.4</b>₁₆ = 6 + 4/16 = <b>6.25</b>.</p><p>Same bit pattern, but the point moved <b>2 places right</b>. Each place is ×2, so ×2² = <b>×4</b>.</p>",
"ref": "02 §4",
"grp": 2,
"core": true,
"corder": 2
}
]
},
{
"n": "1.13",
"text": "27.315 to binary; 2/3 to 8 binary places; check via hex.",
"qs": [
{
"tag": "Mano 1.13 (a)",
"type": "multi",
"q": "Convert decimal 27.315 to binary (8 places after the point).",
"fields": [
{
"label": "binary",
"ans": [
"11011.01010000",
"11011.0101",
"11011.01010"
]
}
],
"why": "<p>Whole part: 27 = 16 + 8 + 2 + 1 = <b>11011</b>.</p><p>Fraction: keep doubling, take the whole part each time:</p><p>0.315 × 2 = 0.63 → <b>0</b><br>0.63 × 2 = 1.26 → <b>1</b><br>0.26 × 2 = 0.52 → <b>0</b><br>0.52 × 2 = 1.04 → <b>1</b><br>0.04 × 2 = 0.08 → <b>0</b><br>0.08 × 2 = 0.16 → <b>0</b><br>0.16 × 2 = 0.32 → <b>0</b><br>0.32 × 2 = 0.64 → <b>0</b></p><p>27.315 ≈ <b>11011.01010000</b> (it never ends exactly).</p>",
"ref": "02 §3",
"grp": 1,
"core": true,
"corder": 2
},
{
"tag": "Mano 1.13 (b)",
"type": "multi",
"q": "Find 2/3 in binary to 8 places, convert back to decimal. How close is it?",
"fields": [
{
"label": "binary",
"ans": [
"0.10101010",
".10101010"
]
},
{
"label": "decimal",
"ans": [
"0.6640625"
]
}
],
"why": "<p>2/3 × 2 = 1.333 → 1, 0.333 × 2 = 0.667 → 0, then it repeats: <b>0.10101010</b>.</p><p>Back to decimal: 0.5 + 0.125 + 0.03125 + 0.0078125 = <b>0.6640625</b>. Error = 0.6667 − 0.6640625 ≈ <b>0.0026</b>.</p>",
"ref": "02 §3",
"grp": 1,
"core": false
},
{
"tag": "Mano 1.13 (c)",
"type": "multi",
"q": "Convert the 8-place answer to hex, then to decimal. Same answer?",
"fields": [
{
"label": "hex",
"ans": [
"0.AA",
".AA"
]
},
{
"label": "decimal",
"ans": [
"0.6640625"
]
}
],
"why": "<p>1010 1010 → <b>0.AA</b>₁₆ = 10/16 + 10/256 = <b>0.6640625</b>. Yes, the same: hex is just a shorthand for the same bits.</p>",
"ref": "02 §4",
"grp": 1,
"core": false
}
]
}
],
"groups": [
{
"name": "Any base → decimal",
"blurb": "Digit × place value, then add. Works for fractions too."
},
{
"name": "Decimal → binary or hex",
"blurb": "Divide for the whole part, multiply for the fraction."
},
{
"name": "Binary ↔ hex ↔ octal",
"blurb": "Group the bits in 4s or 3s from the point."
},
{
"name": "Counting and sizes",
"blurb": "Powers of 2, the biggest n-bit number, counting in other bases."
},
{
"name": "Find the unknown base",
"blurb": "Write both sides in base b and solve."
}
]
});
