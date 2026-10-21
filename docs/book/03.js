BOOK.add({
"id": "03",
"title": "Binary arithmetic",
"intro": "Mano 1.11, 1.12. Type answers in the base asked.",
"problems": [
{
"n": "1.11",
"text": "Binary division 111011 ÷ 101.",
"qs": [
{
"tag": "Mano 1.11",
"type": "multi",
"q": "Do the division in binary: <code>111011 ÷ 101</code>.",
"fields": [
{
"label": "quotient",
"ans": [
"1011"
]
},
{
"label": "remainder",
"ans": [
"100",
"0100"
]
}
],
"why": "<table class='wk'><tr><th>#</th><th>Expression</th><th>Why</th></tr><tr><td>1</td><td>101 into 111 → fits: 1, 111 − 101 = 10</td><td>bring down the next bit: 100</td></tr><tr><td>2</td><td>101 into 100 → doesn't fit: 0</td><td>bring down: 1001</td></tr><tr><td>3</td><td>101 into 1001 → fits: 1, 1001 − 101 = 100</td><td>bring down: 1001</td></tr><tr><td>4</td><td>101 into 1001 → fits: 1, remainder 100</td><td></td></tr></table><p>Quotient <b>1011</b>, remainder <b>100</b>. Check: 59 ÷ 5 = 11 r 4 ✓</p>",
"ref": "03 §4"
}
]
},
{
"n": "1.12",
"text": "Add and multiply without converting to decimal.",
"qs": [
{
"tag": "Mano 1.12 (a) ★",
"type": "multi",
"q": "Add and multiply binary <code>1011</code> and <code>101</code>.",
"fields": [
{
"label": "sum",
"ans": [
"10000"
]
},
{
"label": "product",
"ans": [
"110111"
]
}
],
"why": "<p><b>Add:</b> 1011 + 0101: 1+1 = 10 (0 carry 1), 1+0+1 = 10, 0+1+1 = 10, 1+0+1 = 10 → <b>10000</b>.</p><p><b>Multiply:</b> 1011 × 101 = 1011 (×1) + 0 (×0, shifted) + 101100 (×1, shifted twice) = <b>110111</b>.</p><p>Check: 11 + 5 = 16, 11 × 5 = 55 ✓</p>",
"ref": "03 §3"
},
{
"tag": "Mano 1.12 (b) ★",
"type": "multi",
"q": "Add and multiply hex <code>2E</code> and <code>34</code>.",
"fields": [
{
"label": "sum",
"ans": [
"62"
]
},
{
"label": "product",
"ans": [
"958"
]
}
],
"why": "<p><b>Add:</b> E + 4 = 14 + 4 = 18 = 16 + 2 → write <b>2</b> carry 1. 2 + 3 + 1 = <b>6</b>. Sum = <b>62</b>.</p><p><b>Multiply:</b> 2E × 4 = B8 (E×4 = 56 = 3×16 + 8 → 8 carry 3; 2×4 + 3 = 11 = B). 2E × 3 = 8A, shifted one place = 8A0. B8 + 8A0 = <b>958</b>.</p><p>Check: 46 × 52 = 2392 = 958₁₆ ✓</p>",
"ref": "03 §3"
}
]
}
]
});
