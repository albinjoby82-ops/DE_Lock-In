BOOK.add({
"id": "05",
"title": "Binary codes",
"intro": "Mano 1.22–1.34. Spaces between groups of bits are fine either way.",
"problems": [
{
"n": "1.22",
"text": "8,723 in BCD and in ASCII with even parity.",
"qs": [
{
"tag": "Mano 1.22",
"type": "multi",
"q": "Convert 8,723 to BCD, and to ASCII with an even parity bit on the left.",
"fields": [
{
"label": "BCD",
"ans": [
"1000 0111 0010 0011",
"1000011100100011"
]
},
{
"label": "ASCII",
"ans": [
"10111000 10110111 10110010 00110011",
"10111000101101111011001000110011"
]
}
],
"why": "<p>BCD: each digit → 4 bits: <b>1000 0111 0010 0011</b>.</p><p>ASCII digits are 011 followed by the BCD of the digit: '8' = 0111000. Count the 1s; add a parity bit to make the count even.</p><table class='bits'><tr><th>char</th><td>8</td><td>7</td><td>2</td><td>3</td></tr><tr><th>7-bit</th><td>0111000</td><td>0110111</td><td>0110010</td><td>0110011</td></tr><tr><th>with parity</th><td>10111000</td><td>10110111</td><td>10110010</td><td>00110011</td></tr></table>",
"ref": "05 §1"
}
]
},
{
"n": "1.23",
"text": "842 + 537 in BCD.",
"qs": [
{
"tag": "Mano 1.23",
"type": "multi",
"q": "Add 842 and 537 in BCD. Show the steps.",
"fields": [
{
"label": "sum (BCD)",
"ans": [
"0001 0011 0111 1001",
"0001001101111001"
]
}
],
"why": "<p>842 = 1000 0100 0010, 537 = 0101 0011 0111. Add digit by digit from the right:</p><table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>2 + 7 = 9 = 1001</td><td>≤ 9: keep it</td></tr><tr><td>2</td><td>4 + 3 = 7 = 0111</td><td>≤ 9: keep it</td></tr><tr><td>3</td><td>8 + 5 = 13 = 1101</td><td>&gt; 9: add 0110 (6)</td></tr><tr><td>4</td><td>1101 + 0110 = 1 0011</td><td>digit 3, carry 1 into a new digit</td></tr><tr><td>5</td><td><b>0001 0011 0111 1001 = 1379</b></td><td>check: 842 + 537 = 1379 ✓</td></tr></table>",
"ref": "05 §1"
}
]
},
{
"n": "1.24",
"text": "Weighted codes 6311 and 6421.",
"qs": [
{
"tag": "Mano 1.24 (a) ★",
"type": "work",
"q": "Make a weighted binary code for the decimal digits with weights <b>6, 3, 1, 1</b>.",
"why": "<table class='bits'><tr><th>digit</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><th>code</th><td>0000</td><td>0001</td><td>0011</td><td>0100</td><td>0101</td><td>0111</td><td>1000</td><td>1001</td><td>1011</td><td>1100</td></tr></table><p>Each digit = sum of the weights where the bit is 1 (e.g. 8 = 6 + 1 + 1 = 1011). Some digits have two choices (1 = 0010 or 0001); pick one and stay consistent.</p>",
"ref": "05 §1"
},
{
"tag": "Mano 1.24 (b)",
"type": "work",
"q": "Make a weighted binary code for the decimal digits with weights <b>6, 4, 2, 1</b>.",
"why": "<table class='bits'><tr><th>digit</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><th>code</th><td>0000</td><td>0001</td><td>0010</td><td>0011</td><td>0100</td><td>0101</td><td>1000</td><td>1001</td><td>1010</td><td>1011</td></tr></table><p>6 could be 1000 or 0110, and 7 could be 1001 or 0111. Any choice that adds up is fine.</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.25",
"text": "5,137 in BCD, excess-3, 2421 and 6311.",
"qs": [
{
"tag": "Mano 1.25",
"type": "multi",
"q": "Write 5,137 in (a) BCD, (b) excess-3, (c) 2421 code, (d) the 6311 code from 1.24.",
"fields": [
{
"label": "(a) BCD",
"ans": [
"0101 0001 0011 0111",
"0101000100110111"
]
},
{
"label": "(b) XS-3",
"ans": [
"1000 0100 0110 1010",
"1000010001101010"
]
},
{
"label": "(c) 2421",
"ans": [
"1011 0001 0011 1101",
"1011000100111101"
]
},
{
"label": "(d) 6311",
"ans": [
"0111 0001 0100 1001",
"0111000101001001"
]
}
],
"why": "<p>(a) BCD: <b>0101 0001 0011 0111</b></p><p>(b) excess-3: add 3 to each digit first (8, 4, 6, 10) → <b>1000 0100 0110 1010</b></p><p>(c) 2421: 5 = 1011 (2+2+1, the self-complementing choice), 1 = 0001, 3 = 0011, 7 = 1101 → <b>1011 0001 0011 1101</b></p><p>(d) 6311: <b>0111 0001 0100 1001</b></p>",
"ref": "05 §1"
}
]
},
{
"n": "1.26",
"text": "9's complement of 5,137 in 2421: self-complementing.",
"qs": [
{
"tag": "Mano 1.26",
"type": "multi",
"q": "Find the 9's complement of 5,137 and write it in 2421 code.",
"fields": [
{
"label": "9's comp",
"ans": [
"4862"
]
},
{
"label": "2421",
"ans": [
"0100 1110 1100 0010",
"0100111011000010"
]
}
],
"why": "<p>9's complement: 4862. In 2421: <b>0100 1110 1100 0010</b>.</p><p>Now flip every bit of 5137 in 2421 (1011 0001 0011 1101) → 0100 1110 1100 0010. Same answer! Flipping the bits gives the 9's complement: that's what <b>self-complementing</b> means.</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.27",
"text": "Code the 52 playing cards with the fewest bits.",
"qs": [
{
"tag": "Mano 1.27",
"type": "work",
"q": "Assign a binary code to the 52 playing cards, in an orderly way, using the minimum number of bits.",
"why": "<p>2⁵ = 32 is too few, 2⁶ = 64 ≥ 52, so <b>6 bits</b>.</p><p>Orderly scheme: <b>2 bits for the suit</b> + <b>4 bits for the rank</b>.</p><table class='bits'><tr><th>suit</th><td>00 ♣</td><td>01 ♦</td><td>10 ♥</td><td>11 ♠</td></tr></table><p>Rank: 0001 = Ace, 0010 = 2 … 1010 = 10, 1011 = J, 1100 = Q, 1101 = K. Example: Q♥ = 10 1100.</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.28",
"text": "\"G. Boole\" in 8-bit ASCII with even parity.",
"qs": [
{
"tag": "Mano 1.28",
"type": "multi",
"q": "Write \"G. Boole\" (with the period and the space) in ASCII, leftmost bit = even parity. Fill the first three and last characters.",
"fields": [
{
"label": "G",
"ans": [
"01000111"
]
},
{
"label": ".",
"ans": [
"00101110"
]
},
{
"label": "space",
"ans": [
"10100000"
]
},
{
"label": "e",
"ans": [
"01100101"
]
}
],
"why": "<table class='bits'><tr><th>char</th><td>G</td><td>.</td><td>SP</td><td>B</td><td>o</td><td>o</td><td>l</td><td>e</td></tr><tr><th>hex</th><td>47</td><td>2E</td><td>20</td><td>42</td><td>6F</td><td>6F</td><td>6C</td><td>65</td></tr><tr><th>8-bit</th><td>01000111</td><td>00101110</td><td>10100000</td><td>01000010</td><td>01101111</td><td>01101111</td><td>01101100</td><td>01100101</td></tr></table><p>Parity bit = 1 if the 7-bit code has an odd number of 1s (to make it even), else 0.</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.29",
"text": "Decode the ASCII string.",
"qs": [
{
"tag": "Mano 1.29 ★",
"type": "multi",
"q": "Decode: <code>1000010 1101001 1101100 1101100 1000111 1100001 1110100 1100101 1110011</code>",
"fields": [
{
"label": "text",
"ans": [
"BillGates",
"Bill Gates"
]
}
],
"why": "<table class='bits'><tr><th>bits</th><td>1000010</td><td>1101001</td><td>1101100</td><td>1101100</td><td>1000111</td><td>1100001</td><td>1110100</td><td>1100101</td><td>1110011</td></tr><tr><th>hex</th><td>42</td><td>69</td><td>6C</td><td>6C</td><td>47</td><td>61</td><td>74</td><td>65</td><td>73</td></tr><tr><th>char</th><td>B</td><td>i</td><td>l</td><td>l</td><td>G</td><td>a</td><td>t</td><td>e</td><td>s</td></tr></table><p><b>BillGates</b>. Tip: 100xxxx = capitals (41 = A), 110xxxx / 111xxxx = lowercase (61 = a).</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.30",
"text": "Hex ASCII string with a parity bit: decode and find the parity.",
"qs": [
{
"tag": "Mano 1.30",
"type": "multi",
"q": "<code>73 F4 E5 76 E5 4A EF 62 73</code>: each byte is a parity bit + 7-bit ASCII. (a) Decode. (b) Odd or even parity?",
"fields": [
{
"label": "text",
"ans": [
"steveJobs",
"steve jobs",
"Steve Jobs"
]
},
{
"label": "parity",
"ans": [
"odd"
]
}
],
"why": "<table class='bits'><tr><th>hex</th><td>73</td><td>F4</td><td>E5</td><td>76</td><td>E5</td><td>4A</td><td>EF</td><td>62</td><td>73</td></tr><tr><th>8 bits</th><td>01110011</td><td>11110100</td><td>11100101</td><td>01110110</td><td>11100101</td><td>01001010</td><td>11101111</td><td>01100010</td><td>01110011</td></tr><tr><th>drop bit 7</th><td>73</td><td>74</td><td>65</td><td>76</td><td>65</td><td>4A</td><td>6F</td><td>62</td><td>73</td></tr><tr><th>char</th><td>s</td><td>t</td><td>e</td><td>v</td><td>e</td><td>J</td><td>o</td><td>b</td><td>s</td></tr><tr><th>1s</th><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>3</td><td>7</td><td>3</td><td>5</td></tr></table><p>(a) <b>steveJobs</b>. (b) Every byte has an odd number of 1s → <b>odd parity</b>.</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.31",
"text": "Printing characters in ASCII.",
"qs": [
{
"tag": "Mano 1.31 ★",
"type": "multi",
"q": "How many printing characters are in ASCII? How many are special (not letters or numerals)?",
"fields": [
{
"label": "printing",
"ans": [
"94",
"95"
]
},
{
"label": "special",
"ans": [
"32",
"33"
]
}
],
"why": "<p>Mano counts <b>94</b> printing (graphic) characters, 21₁₆ to 7E₁₆. Letters 26 + 26 = 52, numerals 10 → 62. Special = 94 − 62 = <b>32</b>.</p><p>(If you count the space as printing: 95 and 33. Both are accepted.)</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.32",
"text": "Which bit changes capital ↔ lowercase?",
"qs": [
{
"tag": "Mano 1.32 ★",
"type": "mcq",
"q": "Which bit must be complemented to change an ASCII letter from capital to lowercase and back?",
"opts": [
"The leftmost bit (b₇)",
"The bit worth 32 (b₆, hex 20)",
"The bit worth 16 (b₅)",
"The rightmost bit (b₁)"
],
"a": 1,
"why": "<p>A = 100 0001 (41₁₆), a = 110 0001 (61₁₆). They differ by 20₁₆ = 32: only <b>bit b₆</b> changes.</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.33",
"text": "Read the register 100010010111 four ways.",
"qs": [
{
"tag": "Mano 1.33 ★",
"type": "multi",
"q": "A 12-bit register holds <code>100010010111</code>. What is it as (a) 3 BCD digits, (b) 3 excess-3 digits, (c) 3 digits in 84-2-1, (d) a binary number?",
"fields": [
{
"label": "(a) BCD",
"ans": [
"897"
]
},
{
"label": "(b) XS-3",
"ans": [
"564"
]
},
{
"label": "(c) 84-2-1",
"ans": [
"871"
]
},
{
"label": "(d) binary",
"ans": [
"2199",
"2,199"
]
}
],
"why": "<p>Split into 4s: 1000 | 1001 | 0111</p><p>(a) 8 | 9 | 7 → <b>897</b>. (b) subtract 3 each: 5 | 6 | 4 → <b>564</b>. (c) weights 8, 4, −2, −1: 1000 = 8, 1001 = 8 − 1 = 7, 0111 = 4 − 2 − 1 = 1 → <b>871</b>. (d) 2048 + 128 + 16 + 4 + 2 + 1 = <b>2,199</b>.</p>",
"ref": "05 §1"
}
]
},
{
"n": "1.34",
"text": "ASCII digits with odd parity.",
"qs": [
{
"tag": "Mano 1.34",
"type": "multi",
"q": "List the ASCII codes for the digits 0 to 9 with an <b>odd</b> parity bit on the left. Fill 0, 3, 7, 9.",
"fields": [
{
"label": "0",
"ans": [
"10110000"
]
},
{
"label": "3",
"ans": [
"10110011"
]
},
{
"label": "7",
"ans": [
"00110111"
]
},
{
"label": "9",
"ans": [
"10111001"
]
}
],
"why": "<table class='bits'><tr><th>digit</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><th>code</th><td>10110000</td><td>00110001</td><td>00110010</td><td>10110011</td><td>00110100</td><td>10110101</td><td>10110110</td><td>00110111</td><td>00111000</td><td>10111001</td></tr></table><p>011 + BCD of the digit, then a parity bit that makes the total number of 1s odd.</p>",
"ref": "05 §1"
}
]
}
]
});
