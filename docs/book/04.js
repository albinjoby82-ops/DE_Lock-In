BOOK.add({
"id": "04",
"title": "Signed numbers and overflow",
"intro": "Mano 1.14–1.21. Keep leading zeros in bit patterns; negatives with a minus sign.",
"problems": [
{
"n": "1.14",
"text": "1's and 2's complements.",
"qs": [
{
"tag": "Mano 1.14 (a)",
"type": "multi",
"q": "Find the 1's and 2's complements of <code>10000000</code>.",
"fields": [
{
"label": "1's",
"ans": [
"01111111"
]
},
{
"label": "2's",
"ans": [
"10000000"
]
}
],
"why": "<p>1's: flip every bit → <b>01111111</b>.</p><p>2's: 1's + 1 = <b>10000000</b>. Shortcut: copy bits from the right up to and including the first 1, flip the rest.</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.14 (b)",
"type": "multi",
"q": "Find the 1's and 2's complements of <code>00000000</code>.",
"fields": [
{
"label": "1's",
"ans": [
"11111111"
]
},
{
"label": "2's",
"ans": [
"00000000"
]
}
],
"why": "<p>1's: flip every bit → <b>11111111</b>.</p><p>2's: 1's + 1 = <b>00000000</b>. Shortcut: copy bits from the right up to and including the first 1, flip the rest.</p><p>Any carry out of the 8 bits is dropped.</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.14 (c)",
"type": "multi",
"q": "Find the 1's and 2's complements of <code>11011010</code>.",
"fields": [
{
"label": "1's",
"ans": [
"00100101"
]
},
{
"label": "2's",
"ans": [
"00100110"
]
}
],
"why": "<p>1's: flip every bit → <b>00100101</b>.</p><p>2's: 1's + 1 = <b>00100110</b>. Shortcut: copy bits from the right up to and including the first 1, flip the rest.</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.14 (d)",
"type": "multi",
"q": "Find the 1's and 2's complements of <code>01110110</code>.",
"fields": [
{
"label": "1's",
"ans": [
"10001001"
]
},
{
"label": "2's",
"ans": [
"10001010"
]
}
],
"why": "<p>1's: flip every bit → <b>10001001</b>.</p><p>2's: 1's + 1 = <b>10001010</b>. Shortcut: copy bits from the right up to and including the first 1, flip the rest.</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.14 (e)",
"type": "multi",
"q": "Find the 1's and 2's complements of <code>10000101</code>.",
"fields": [
{
"label": "1's",
"ans": [
"01111010"
]
},
{
"label": "2's",
"ans": [
"01111011"
]
}
],
"why": "<p>1's: flip every bit → <b>01111010</b>.</p><p>2's: 1's + 1 = <b>01111011</b>. Shortcut: copy bits from the right up to and including the first 1, flip the rest.</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.14 (f)",
"type": "multi",
"q": "Find the 1's and 2's complements of <code>11111111</code>.",
"fields": [
{
"label": "1's",
"ans": [
"00000000"
]
},
{
"label": "2's",
"ans": [
"00000001"
]
}
],
"why": "<p>1's: flip every bit → <b>00000000</b>.</p><p>2's: 1's + 1 = <b>00000001</b>. Shortcut: copy bits from the right up to and including the first 1, flip the rest.</p>",
"ref": "04 §3"
}
]
},
{
"n": "1.15",
"text": "9's and 10's complements.",
"qs": [
{
"tag": "Mano 1.15 (a)",
"type": "multi",
"q": "Find the 9's and 10's complements of <code>52,784,630</code> (8 digits).",
"fields": [
{
"label": "9's",
"ans": [
"47215369",
"47,215,369"
]
},
{
"label": "10's",
"ans": [
"47215370",
"47,215,370"
]
}
],
"why": "<p>9's: each digit → 9 − digit → <b>47215369</b>.</p><p>10's: 9's + 1 → <b>47215370</b> (carry out of 8 digits dropped).</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.15 (b)",
"type": "multi",
"q": "Find the 9's and 10's complements of <code>63,325,600</code> (8 digits).",
"fields": [
{
"label": "9's",
"ans": [
"36674399",
"36,674,399"
]
},
{
"label": "10's",
"ans": [
"36674400",
"36,674,400"
]
}
],
"why": "<p>9's: each digit → 9 − digit → <b>36674399</b>.</p><p>10's: 9's + 1 → <b>36674400</b> (carry out of 8 digits dropped).</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.15 (c)",
"type": "multi",
"q": "Find the 9's and 10's complements of <code>25,000,000</code> (8 digits).",
"fields": [
{
"label": "9's",
"ans": [
"74999999",
"74,999,999"
]
},
{
"label": "10's",
"ans": [
"75000000",
"75,000,000"
]
}
],
"why": "<p>9's: each digit → 9 − digit → <b>74999999</b>.</p><p>10's: 9's + 1 → <b>75000000</b> (carry out of 8 digits dropped).</p>",
"ref": "04 §3"
},
{
"tag": "Mano 1.15 (d)",
"type": "multi",
"q": "Find the 9's and 10's complements of <code>00,000,000</code> (8 digits).",
"fields": [
{
"label": "9's",
"ans": [
"99999999",
"99,999,999"
]
},
{
"label": "10's",
"ans": [
"00000000",
"0",
"0"
]
}
],
"why": "<p>9's: each digit → 9 − digit → <b>99999999</b>.</p><p>10's: 9's + 1 → <b>00000000</b> (carry out of 8 digits dropped).</p>",
"ref": "04 §3"
}
]
},
{
"n": "1.16",
"text": "16's complement of B2FA vs 2's complement in binary.",
"qs": [
{
"tag": "Mano 1.16",
"type": "multi",
"q": "(a) 16's complement of <b>B2FA</b>. (b) B2FA in binary. (c) 2's complement of (b). (d) (c) in hex.",
"fields": [
{
"label": "(a)",
"ans": [
"4D06"
]
},
{
"label": "(b)",
"ans": [
"1011001011111010",
"1011 0010 1111 1010"
]
},
{
"label": "(c)",
"ans": [
"0100110100000110",
"0100 1101 0000 0110"
]
},
{
"label": "(d)",
"ans": [
"4D06"
]
}
],
"why": "<p>(a) 15's complement: each digit → F − digit: B2FA → 4D05. Add 1 → <b>4D06</b>.</p><p>(b) <b>1011 0010 1111 1010</b>. (c) flip and add 1 → <b>0100 1101 0000 0110</b>. (d) = <b>4D06</b>, the same as (a): the 16's complement and 2's complement are the same thing, written in hex vs binary.</p>",
"ref": "04 §3"
}
]
},
{
"n": "1.17",
"text": "Subtraction with the 10's complement.",
"qs": [
{
"tag": "Mano 1.17 (a)",
"type": "multi",
"q": "Use the 10's complement of the subtrahend: <code>6,428 − 3,409</code>.",
"fields": [
{
"label": "answer",
"ans": [
"3019",
"3,019"
]
}
],
"why": "<p>10's complement of 3409 = 6591.</p><p>6428 + 6591 = 13019 → end carry → drop it → <b>3019</b>.</p><p>Check: 6428 − 3409 = 3019 ✓</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.17 (b)",
"type": "multi",
"q": "Use the 10's complement of the subtrahend: <code>125 − 1,800</code>.",
"fields": [
{
"label": "answer",
"ans": [
"-1675",
"-1,675"
]
}
],
"why": "<p>10's complement of 1800 = 8200.</p><p>0125 + 8200 = 8325, no end carry → negative: −(10's complement of 8325) = <b>-1675</b>.</p><p>Check: 125 − 1800 = -1675 ✓</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.17 (c)",
"type": "multi",
"q": "Use the 10's complement of the subtrahend: <code>2,043 − 6,152</code>.",
"fields": [
{
"label": "answer",
"ans": [
"-4109",
"-4,109"
]
}
],
"why": "<p>10's complement of 6152 = 3848.</p><p>2043 + 3848 = 5891, no end carry → negative: −(10's complement of 5891) = <b>-4109</b>.</p><p>Check: 2043 − 6152 = -4109 ✓</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.17 (d)",
"type": "multi",
"q": "Use the 10's complement of the subtrahend: <code>1,631 − 745</code>.",
"fields": [
{
"label": "answer",
"ans": [
"886",
"886"
]
}
],
"why": "<p>10's complement of 0745 = 9255.</p><p>1631 + 9255 = 10886 → end carry → drop it → <b>886</b>.</p><p>Check: 1631 − 745 = 886 ✓</p>",
"ref": "04 §6"
}
]
},
{
"n": "1.18",
"text": "Binary subtraction with the 2's complement.",
"qs": [
{
"tag": "Mano 1.18 (a)",
"type": "multi",
"q": "Subtract using the 2's complement of the subtrahend: <code>10011 − 10001</code>.",
"fields": [
{
"label": "answer",
"ans": [
"00010",
"10"
]
}
],
"why": "<p>Make both 5 bits: 10011 − 10001. 2's complement of 10001 = 01111.</p><p>10011 + 01111 = 100010 → end carry → drop it → <b>00010</b> = 2.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.18 (b)",
"type": "multi",
"q": "Subtract using the 2's complement of the subtrahend: <code>100010 − 100011</code>.",
"fields": [
{
"label": "answer",
"ans": [
"-000001",
"-1",
"−000001"
]
}
],
"why": "<p>Make both 6 bits: 100010 − 100011. 2's complement of 100011 = 011101.</p><p>100010 + 011101 = 111111, no end carry → negative: −(2's complement of 111111) = <b>−000001</b> = -1.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.18 (c)",
"type": "multi",
"q": "Subtract using the 2's complement of the subtrahend: <code>1001 − 101000</code>.",
"fields": [
{
"label": "answer",
"ans": [
"-011111",
"-11111",
"−011111"
]
}
],
"why": "<p>Make both 6 bits: 001001 − 101000. 2's complement of 101000 = 011000.</p><p>001001 + 011000 = 100001, no end carry → negative: −(2's complement of 100001) = <b>−011111</b> = -31.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.18 (d)",
"type": "multi",
"q": "Subtract using the 2's complement of the subtrahend: <code>110000 − 10101</code>.",
"fields": [
{
"label": "answer",
"ans": [
"011011",
"11011"
]
}
],
"why": "<p>Make both 6 bits: 110000 − 010101. 2's complement of 010101 = 101011.</p><p>110000 + 101011 = 1011011 → end carry → drop it → <b>011011</b> = 27.</p>",
"ref": "04 §6"
}
]
},
{
"n": "1.19",
"text": "Signed 10's complement with +9,286 and +801.",
"qs": [
{
"tag": "Mano 1.19 (a) ★",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (+9,286) + (+801).",
"fields": [
{
"label": "result",
"ans": [
"+10087",
"+10,087",
"10087",
"10,087"
]
}
],
"why": "<p>+9,286 = 0 09286 · −9,286 = 9 90714 · +801 = 0 00801 · −801 = 9 99199</p><p>0 09286 + 0 00801 = 0 10087</p><p>sign digit 0 → +10,087.</p><p>Note: the printed problem says the sum is +10,627, but 9,286 + 801 = <b>10,087</b>. The method is what matters.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.19 (b) ★",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (+9,286) + (−801).",
"fields": [
{
"label": "result",
"ans": [
"+8485",
"+8,485",
"8485",
"8,485"
]
}
],
"why": "<p>+9,286 = 0 09286 · −9,286 = 9 90714 · +801 = 0 00801 · −801 = 9 99199</p><p>0 09286 + 9 99199 = 0 08485 (end carry dropped)</p><p>sign digit 0 → +8,485.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.19 (c) ★",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (−9,286) + (+801).",
"fields": [
{
"label": "result",
"ans": [
"-8485",
"-8,485",
"-8485",
"-8,485"
]
}
],
"why": "<p>+9,286 = 0 09286 · −9,286 = 9 90714 · +801 = 0 00801 · −801 = 9 99199</p><p>9 90714 + 0 00801 = 9 91515</p><p>sign digit 9 → negative: 10's complement = 008485 → <b>-8,485</b>.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.19 (d) ★",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (−9,286) + (−801).",
"fields": [
{
"label": "result",
"ans": [
"-10087",
"-10,087",
"-10087",
"-10,087"
]
}
],
"why": "<p>+9,286 = 0 09286 · −9,286 = 9 90714 · +801 = 0 00801 · −801 = 9 99199</p><p>9 90714 + 9 99199 = 9 89913 (end carry dropped)</p><p>sign digit 9 → negative: 10's complement = 010087 → <b>-10,087</b>.</p>",
"ref": "04 §6"
}
]
},
{
"n": "1.20",
"text": "Signed 2's complement sums with ±29 and ±49.",
"qs": [
{
"tag": "Mano 1.20 (a)",
"type": "multi",
"q": "8-bit signed 2's complement: (+29) + (-49). Give the 8-bit result and its decimal value.",
"fields": [
{
"label": "bits",
"ans": [
"11101100"
]
},
{
"label": "decimal",
"ans": [
"-20",
"-20"
]
}
],
"why": "<p>00011101 + 11001111 = <b>11101100</b>.</p><p>Leading 1 → negative: 2's complement 00010100 = 20 → <b>-20</b>.</p><p>Values: +29 = 00011101, +49 = 00110001, −29 = 11100011, −49 = 11001111. (The problem prints +46 = 00101110 first, but then uses 49 in the sums.)</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.20 (b)",
"type": "multi",
"q": "8-bit signed 2's complement: (-29) + (+49). Give the 8-bit result and its decimal value.",
"fields": [
{
"label": "bits",
"ans": [
"00010100"
]
},
{
"label": "decimal",
"ans": [
"20",
"+20"
]
}
],
"why": "<p>11100011 + 00110001 = <b>00010100</b> (carry out dropped).</p><p>Leading 0 → <b>+20</b>.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.20 (c)",
"type": "multi",
"q": "8-bit signed 2's complement: (-29) + (-49). Give the 8-bit result and its decimal value.",
"fields": [
{
"label": "bits",
"ans": [
"10110010"
]
},
{
"label": "decimal",
"ans": [
"-78",
"-78"
]
}
],
"why": "<p>11100011 + 11001111 = <b>10110010</b> (carry out dropped).</p><p>Leading 1 → negative: 2's complement 01001110 = 78 → <b>-78</b>.</p>",
"ref": "04 §6"
}
]
},
{
"n": "1.21",
"text": "Signed 10's complement with +9,742 and +641.",
"qs": [
{
"tag": "Mano 1.21 (a)",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (+9,742) + (+641).",
"fields": [
{
"label": "result",
"ans": [
"+10383",
"+10,383",
"10383",
"10,383"
]
}
],
"why": "<p>+9,742 = 0 09742 · −9,742 = 9 90258 · +641 = 0 00641 · −641 = 9 99359</p><p>0 09742 + 0 00641 = 0 10383</p><p>sign digit 0 → +10,383.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.21 (b)",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (+9,742) + (−641).",
"fields": [
{
"label": "result",
"ans": [
"+9101",
"+9,101",
"9101",
"9,101"
]
}
],
"why": "<p>+9,742 = 0 09742 · −9,742 = 9 90258 · +641 = 0 00641 · −641 = 9 99359</p><p>0 09742 + 9 99359 = 0 09101 (end carry dropped)</p><p>sign digit 0 → +9,101.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.21 (c)",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (−9,742) + (+641).",
"fields": [
{
"label": "result",
"ans": [
"-9101",
"-9,101",
"-9101",
"-9,101"
]
}
],
"why": "<p>+9,742 = 0 09742 · −9,742 = 9 90258 · +641 = 0 00641 · −641 = 9 99359</p><p>9 90258 + 0 00641 = 9 90899</p><p>sign digit 9 → negative: 10's complement = 009101 → <b>-9,101</b>.</p>",
"ref": "04 §6"
},
{
"tag": "Mano 1.21 (d)",
"type": "multi",
"q": "Signed 10's complement (sign digit + 5 digits): (−9,742) + (−641).",
"fields": [
{
"label": "result",
"ans": [
"-10383",
"-10,383",
"-10383",
"-10,383"
]
}
],
"why": "<p>+9,742 = 0 09742 · −9,742 = 9 90258 · +641 = 0 00641 · −641 = 9 99359</p><p>9 90258 + 9 99359 = 9 89617 (end carry dropped)</p><p>sign digit 9 → negative: 10's complement = 010383 → <b>-10,383</b>.</p>",
"ref": "04 §6"
}
]
}
]
});
