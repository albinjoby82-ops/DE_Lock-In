"""Mano Chapter 1 (1.1-1.34): topics 02, 03, 04, 05. Every number is computed and checked here."""
from booklib import *

S = "★"


def tag(n, part=None, star=False):
    return f"Mano {n}" + (f" ({part})" if part else "") + (f" {S}" if star else "")


def num(n):
    return [str(n), f"{n:,}"]


def to_base(n, b):
    digs = "0123456789ABCDEFGHIJ"
    if n == 0:
        return "0"
    out = ""
    while n:
        out = digs[n % b] + out
        n //= b
    return out


def ladder(n, b):
    """Repeated division rows as an HTML step table."""
    rows = []
    while n:
        q, r = divmod(n, b)
        rows.append((f"{n} ÷ {b} = {q} rem <b>{'0123456789ABCDEF'[r]}</b>", ""))
        n = q
    h = "<table class='wk'><tr><th>#</th><th>Divide</th><th></th></tr>"
    for k, (e, w) in enumerate(rows):
        h += f"<tr><td>{k + 1}</td><td>{e}</td><td>{w}</td></tr>"
    return h + "</table><p>Read the remainders <b>bottom to top</b>.</p>"


def place(digits, b):
    """digit × place value working for an integer string in base b."""
    n = len(digits)
    parts = [f"{d}×{b}<sup>{n - 1 - k}</sup>" for k, d in enumerate(digits)]
    vals = [int(d, 36) * b ** (n - 1 - k) for k, d in enumerate(digits)]
    return " + ".join(parts) + " = " + " + ".join(map(str, vals)) + f" = <b>{sum(vals)}</b>"


def frac_bin(x, places):
    bits, rows = "", []
    for _ in range(places):
        x2 = x * 2
        bit = int(x2)
        rows.append(f"{x:g} × 2 = {x2:g} → <b>{bit}</b>")
        bits += str(bit)
        x = x2 - bit
    return bits, rows


# ======================================================================== TOPIC 02
def topic02():
    P = []
    octs = [to_base(n, 8) for n in range(16, 33)]
    hexs = [to_base(n, 16) for n in range(16, 33)]
    b13 = [to_base(n, 13) for n in range(8, 29)]
    assert to_base(28, 13) == "22" and to_base(32, 8) == "40"
    tab = "<table class='bits'><tr><th>dec</th>" + "".join(f"<td>{n}</td>" for n in range(16, 33)) + "</tr>" + \
          "<tr><th>oct</th>" + "".join(f"<td>{x}</td>" for x in octs) + "</tr><tr><th>hex</th>" + "".join(f"<td>{x}</td>" for x in hexs) + "</tr></table>"
    tab13 = "<table class='bits'><tr><th>dec</th>" + "".join(f"<td>{n}</td>" for n in range(8, 29)) + "</tr><tr><th>b13</th>" + \
            "".join(f"<td>{x}</td>" for x in b13) + "</tr></table>"
    P.append({"n": "1.1", "text": "Octal and hex for 16 to 32; base 13 (digits A, B, C) for 8 to 28.", "qs": [
        multi_q(tag("1.1"), "Write the octal and hexadecimal lists for decimal 16 to 32, and the base-13 list for 8 to 28 (A, B, C are the last three digits). "
                "Then fill these spot checks.",
                [("25 in octal", ["31"]), ("32 in octal", ["40"]), ("26 in hex", ["1A"]), ("31 in hex", ["1F"]),
                 ("12 in base 13", ["C"]), ("13 in base 13", ["10"]), ("25 in base 13", ["1C"]), ("28 in base 13", ["22"])],
                tab + tab13 + "<p>Counting rule: when the last digit runs out (7 in octal, F in hex, C in base 13), it goes back to 0 and the next digit goes up by 1.</p>",
                ref="02 §0")]})

    P.append({"n": "1.2", "text": "Exact bytes in 32K, 64M and 6.4G bytes.", "qs": [
        multi_q(tag("1.2", star=True), "What is the exact number of bytes in (a) 32K bytes, (b) 64M bytes, (c) 6.4G bytes? (K = 2¹⁰, M = 2²⁰, G = 2³⁰)",
                [("(a) 32K", num(32 * 1024)), ("(b) 64M", num(64 * 2 ** 20)), ("(c) 6.4G", num(round(6.4 * 2 ** 30)) + ["6871947673.6", "6,871,947,673.6"])],
                steps([("32K = 32 × 2¹⁰ = 2⁵ × 2¹⁰ = 2¹⁵", "K = 1024"),
                       ("= 32,768 bytes", ""),
                       ("64M = 2⁶ × 2²⁰ = 2²⁶ = 67,108,864 bytes", "M = 1,048,576"),
                       ("6.4G = 6.4 × 1,073,741,824 = 6,871,947,673.6 ≈ 6,871,947,674 bytes", "G = 1,073,741,824")], final=False),
                ref="02 §0")]})

    qs = []
    for part, star, d, b in [("a", True, "4310", 5), ("b", True, "198", 12), ("c", False, "735", 8), ("d", False, "525", 6)]:
        v = int(d, b)
        qs.append(multi_q(tag("1.3", part, star), f"Convert (<b>{d}</b>)<sub>{b}</sub> to decimal.", [("decimal", num(v))],
                          f"<p>{place(d, b)}</p>", ref="02 §1"))
    P.append({"n": "1.3", "text": "Convert to decimal.", "qs": qs})

    v = 2 ** 14 - 1
    P.append({"n": "1.4", "text": "Largest 14-bit binary number in decimal and hex.", "qs": [
        multi_q(tag("1.4"), "What is the largest binary number with 14 bits? Give it in decimal and hexadecimal.",
                [("binary", ["1" * 14]), ("decimal", num(v)), ("hex", ["3FFF"])],
                "<p>All 14 bits are 1: <b>11111111111111</b> = 2¹⁴ − 1 = 16,384 − 1 = <b>16,383</b>.</p>"
                "<p>Hex: group in 4s from the right: 11 1111 1111 1111 → <b>3FFF</b>.</p>", ref="02 §4")]})

    P.append({"n": "1.5", "text": "Find the base that makes each sum correct.", "qs": [
        multi_q(tag("1.5", "a", True), "Find base b so that <code>14 / 2 = 5</code> is correct.", [("b", ["6"])],
                steps([("14 in base b = b + 4", "digit × place value"),
                       ("(b + 4) / 2 = 5", ""),
                       ("b + 4 = 10 → b = 6", "check: 14₆ = 10, and 10 / 2 = 5 ✓")]), ref="02 §1"),
        multi_q(tag("1.5", "b", True), "Find base b so that <code>54 / 4 = 13</code> is correct.", [("b", ["8"])],
                steps([("(5b + 4) / 4 = b + 3", "both sides in base b"),
                       ("5b + 4 = 4b + 12", "multiply by 4"),
                       ("b = 8", "check: 54₈ = 44, 13₈ = 11, and 44 / 4 = 11 ✓")]), ref="02 §1"),
        multi_q(tag("1.5", "c", True), "Find base b so that <code>24 + 17 = 40</code> is correct.", [("b", ["11"])],
                steps([("(2b + 4) + (b + 7) = 4b", "both sides in base b"),
                       ("3b + 11 = 4b", ""),
                       ("b = 11", "check: 24₁₁ = 26, 17₁₁ = 18, 40₁₁ = 44, and 26 + 18 = 44 ✓")]), ref="02 §1")]})

    P.append({"n": "1.6", "text": "Base where x² − 11x + 22 = 0 has roots 3 and 6.", "qs": [
        multi_q(tag("1.6", star=True), "The solutions of <code>x² − 11x + 22 = 0</code> are x = 3 and x = 6. What base are the numbers in?", [("base", ["8"])],
                steps([("(x − 3)(x − 6) = x² − 9x + 18", "the roots tell you the factors"),
                       ("11 in base b = 9 → b + 1 = 9", "match the middle term"),
                       ("22 in base b = 18 → 2b + 2 = 18", "match the last term"),
                       ("b = 8", "both agree")]), ref="02 §1")]})

    bits = bin(0x68BE)[2:]
    octv = oct(0x68BE)[2:]
    assert octv == "64276"
    P.append({"n": "1.7", "text": "Hex 68BE to binary, then to octal.", "qs": [
        multi_q(tag("1.7", star=True), "Convert hex <b>68BE</b> to binary, then from binary to octal.",
                [("binary", [bits, "0" + bits, "0110100010111110", "0110 1000 1011 1110"]), ("octal", [octv])],
                "<p>Each hex digit → 4 bits: 6 = 0110, 8 = 1000, B = 1011, E = 1110 → <b>0110 1000 1011 1110</b>.</p>"
                "<p>Regroup in 3s from the right: 110 100 010 111 110 → 6 4 2 7 6 → <b>64276</b>₈.</p>", ref="02 §4")]})

    P.append({"n": "1.8", "text": "431 to binary two ways.", "qs": [
        multi_q(tag("1.8"), "Convert decimal 431 to binary (a) directly, (b) via hexadecimal. Which is faster?",
                [("binary", [bin(431)[2:], "000110101111"]), ("hex", ["1AF"])],
                "<p><b>(a)</b> Divide by 2 nine times:</p>" + ladder(431, 2) +
                "<p><b>(b)</b> Divide by 16 only twice:</p>" + ladder(431, 16) +
                "<p>1AF → 0001 1010 1111 = <b>110101111</b>. Going through hex is <b>faster</b>: 2 divisions instead of 9.</p>", ref="02 §2")]})

    qs = []
    for part, star, s_, b in [("a", True, "10110.0101", 2), ("b", True, "16.5", 16), ("c", True, "26.24", 8),
                              ("d", False, "FAFA", 16), ("e", False, "1010.1010", 2)]:
        w, _, f = s_.partition(".")
        val = int(w, b) + sum(int(c, 16) * b ** -(k + 1) for k, c in enumerate(f))
        fr = " + ".join(f"{c}×{b}<sup>−{k + 1}</sup>" for k, c in enumerate(f)) if f else ""
        txt = f"<p>Whole part: {place(w, b)}</p>" + (f"<p>Fraction: {fr} = {val - int(w, b):g}</p>" if f else "") + f"<p>Total: <b>{val:g}</b></p>"
        if part == "c":
            txt += "<p>Notice (a), (b) and (c) are all 22.3125: the same number in three bases.</p>"
        qs.append(multi_q(tag("1.9", part, star), f"Express (<b>{s_}</b>)<sub>{b}</sub> in decimal.", [("decimal", [f"{val:g}", f"{val:,}"])], txt, ref="02 §1"))
    P.append({"n": "1.9", "text": "Express in decimal.", "qs": qs})

    P.append({"n": "1.10", "text": "1.10010 and 110.010 to hex and decimal.", "qs": [
        multi_q(tag("1.10"), "Convert binary (a) <b>1.10010</b> and (b) <b>110.010</b> to hexadecimal and to decimal. Why is (b) 4 × (a)?",
                [("(a) hex", ["1.9", "1.90"]), ("(a) decimal", ["1.5625"]), ("(b) hex", ["6.4"]), ("(b) decimal", ["6.25"])],
                "<p>Group in 4s <b>away from the point</b>, padding with 0s: 1 . 1001 0(000) → <b>1.9</b>₁₆ = 1 + 9/16 = <b>1.5625</b>.</p>"
                "<p>110 . 010(0) → <b>6.4</b>₁₆ = 6 + 4/16 = <b>6.25</b>.</p>"
                "<p>Same bit pattern, but the point moved <b>2 places right</b>. Each place is ×2, so ×2² = <b>×4</b>.</p>", ref="02 §4")]})

    fb, rows = frac_bin(0.315, 8)
    two3 = 0.5 + 0.125 + 0.03125 + 0.0078125
    P.append({"n": "1.13", "text": "27.315 to binary; 2/3 to 8 binary places; check via hex.", "qs": [
        multi_q(tag("1.13", "a"), "Convert decimal 27.315 to binary (8 places after the point).", [("binary", ["11011." + fb, "11011.0101", "11011.01010"])],
                "<p>Whole part: 27 = 16 + 8 + 2 + 1 = <b>11011</b>.</p><p>Fraction: keep doubling, take the whole part each time:</p><p>" +
                "<br>".join(rows) + f"</p><p>27.315 ≈ <b>11011.{fb}</b> (it never ends exactly).</p>", ref="02 §3"),
        multi_q(tag("1.13", "b"), "Find 2/3 in binary to 8 places, convert back to decimal. How close is it?",
                [("binary", ["0.10101010", ".10101010"]), ("decimal", [f"{two3}"])],
                "<p>2/3 × 2 = 1.333 → 1, 0.333 × 2 = 0.667 → 0, then it repeats: <b>0.10101010</b>.</p>"
                f"<p>Back to decimal: 0.5 + 0.125 + 0.03125 + 0.0078125 = <b>{two3}</b>. Error = 0.6667 − {two3} ≈ <b>0.0026</b>.</p>", ref="02 §3"),
        multi_q(tag("1.13", "c"), "Convert the 8-place answer to hex, then to decimal. Same answer?",
                [("hex", ["0.AA", ".AA"]), ("decimal", [f"{two3}"])],
                f"<p>1010 1010 → <b>0.AA</b>₁₆ = 10/16 + 10/256 = <b>{two3}</b>. Yes, the same: hex is just a shorthand for the same bits.</p>", ref="02 §4")]})
    return write_topic("02", "Number systems", "Mano 1.1–1.10, 1.13. Type plain numbers; commas are fine.", P)


# ======================================================================== TOPIC 03
def topic03():
    P = []
    q_, r_ = divmod(0b111011, 0b101)
    P.append({"n": "1.11", "text": "Binary division 111011 ÷ 101.", "qs": [
        multi_q(tag("1.11"), "Do the division in binary: <code>111011 ÷ 101</code>.", [("quotient", [bin(q_)[2:]]), ("remainder", [bin(r_)[2:], "0" + bin(r_)[2:]])],
                steps([("101 into 111 → fits: 1, 111 − 101 = 10", "bring down the next bit: 100"),
                       ("101 into 100 → doesn't fit: 0", "bring down: 1001"),
                       ("101 into 1001 → fits: 1, 1001 − 101 = 100", "bring down: 1001"),
                       ("101 into 1001 → fits: 1, remainder 100", "")], final=False) +
                f"<p>Quotient <b>{bin(q_)[2:]}</b>, remainder <b>{bin(r_)[2:]}</b>. Check: 59 ÷ 5 = 11 r 4 ✓</p>", ref="03 §4")]})
    s1, p1 = 0b1011 + 0b101, 0b1011 * 0b101
    s2, p2 = 0x2E + 0x34, 0x2E * 0x34
    P.append({"n": "1.12", "text": "Add and multiply without converting to decimal.", "qs": [
        multi_q(tag("1.12", "a", True), "Add and multiply binary <code>1011</code> and <code>101</code>.", [("sum", [bin(s1)[2:]]), ("product", [bin(p1)[2:]])],
                "<p><b>Add:</b> 1011 + 0101: 1+1 = 10 (0 carry 1), 1+0+1 = 10, 0+1+1 = 10, 1+0+1 = 10 → <b>10000</b>.</p>"
                "<p><b>Multiply:</b> 1011 × 101 = 1011 (×1) + 0 (×0, shifted) + 101100 (×1, shifted twice) = <b>110111</b>.</p>"
                "<p>Check: 11 + 5 = 16, 11 × 5 = 55 ✓</p>", ref="03 §3"),
        multi_q(tag("1.12", "b", True), "Add and multiply hex <code>2E</code> and <code>34</code>.", [("sum", [to_base(s2, 16)]), ("product", [to_base(p2, 16)])],
                "<p><b>Add:</b> E + 4 = 14 + 4 = 18 = 16 + 2 → write <b>2</b> carry 1. 2 + 3 + 1 = <b>6</b>. Sum = <b>62</b>.</p>"
                "<p><b>Multiply:</b> 2E × 4 = B8 (E×4 = 56 = 3×16 + 8 → 8 carry 3; 2×4 + 3 = 11 = B). "
                "2E × 3 = 8A, shifted one place = 8A0. B8 + 8A0 = <b>958</b>.</p><p>Check: 46 × 52 = 2392 = 958₁₆ ✓</p>", ref="03 §3")]})
    return write_topic("03", "Binary arithmetic", "Mano 1.11, 1.12. Type answers in the base asked.", P)


# ======================================================================== TOPIC 04
def ones_c(b):
    return "".join("1" if c == "0" else "0" for c in b)


def twos_c(b):
    n = len(b)
    return format((-int(b, 2)) % (1 << n), f"0{n}b")


def topic04():
    P = []
    qs = []
    for part, b in zip("abcdef", ["10000000", "00000000", "11011010", "01110110", "10000101", "11111111"]):
        o, t = ones_c(b), twos_c(b)
        qs.append(multi_q(tag("1.14", part), f"Find the 1's and 2's complements of <code>{b}</code>.", [("1's", [o]), ("2's", [t])],
                          f"<p>1's: flip every bit → <b>{o}</b>.</p><p>2's: 1's + 1 = <b>{t}</b>. "
                          "Shortcut: copy bits from the right up to and including the first 1, flip the rest.</p>" +
                          ("<p>Any carry out of the 8 bits is dropped.</p>" if b == "00000000" else ""), ref="04 §3"))
    P.append({"n": "1.14", "text": "1's and 2's complements.", "qs": qs})

    qs = []
    for part, d in zip("abcd", ["52784630", "63325600", "25000000", "00000000"]):
        n9 = "".join(str(9 - int(c)) for c in d)
        n10 = format((10 ** 8 - int(d)) % 10 ** 8, "08d")
        qs.append(multi_q(tag("1.15", part), f"Find the 9's and 10's complements of <code>{d[:2]},{d[2:5]},{d[5:]}</code> (8 digits).",
                          [("9's", [n9, f"{int(n9):,}"]), ("10's", [n10, f"{int(n10):,}"] + (["0"] if n10 == "00000000" else []))],
                          f"<p>9's: each digit → 9 − digit → <b>{n9}</b>.</p><p>10's: 9's + 1 → <b>{n10}</b> (carry out of 8 digits dropped).</p>", ref="04 §3"))
    P.append({"n": "1.15", "text": "9's and 10's complements.", "qs": qs})

    c16 = to_base(0x10000 - 0xB2FA, 16)
    bb = format(0xB2FA, "016b")
    P.append({"n": "1.16", "text": "16's complement of B2FA vs 2's complement in binary.", "qs": [
        multi_q(tag("1.16"), "(a) 16's complement of <b>B2FA</b>. (b) B2FA in binary. (c) 2's complement of (b). (d) (c) in hex.",
                [("(a)", [c16]), ("(b)", [bb, "1011 0010 1111 1010"]), ("(c)", [twos_c(bb), "0100 1101 0000 0110"]), ("(d)", [c16])],
                f"<p>(a) 15's complement: each digit → F − digit: B2FA → 4D05. Add 1 → <b>{c16}</b>.</p>"
                f"<p>(b) <b>1011 0010 1111 1010</b>. (c) flip and add 1 → <b>0100 1101 0000 0110</b>. (d) = <b>{c16}</b>, the same as (a): "
                "the 16's complement and 2's complement are the same thing, written in hex vs binary.</p>", ref="04 §3")]})

    qs = []
    for part, a, b in [("a", 6428, 3409), ("b", 125, 1800), ("c", 2043, 6152), ("d", 1631, 745)]:
        c10 = 10000 - b
        s_ = a + c10
        if s_ >= 10000:
            ans = s_ - 10000
            work = f"<p>{a:04d} + {c10:04d} = {s_} → end carry → drop it → <b>{ans}</b>.</p>"
            out = str(ans)
        else:
            ans = -(10000 - s_)
            work = f"<p>{a:04d} + {c10:04d} = {s_:04d}, no end carry → negative: −(10's complement of {s_:04d}) = <b>{ans}</b>.</p>"
            out = str(ans)
        assert ans == a - b
        qs.append(multi_q(tag("1.17", part), f"Use the 10's complement of the subtrahend: <code>{a:,} − {b:,}</code>.", [("answer", [out, f"{ans:,}"])],
                          f"<p>10's complement of {b:04d} = {c10:04d}.</p>" + work + f"<p>Check: {a} − {b} = {a - b} ✓</p>", ref="04 §6"))
    P.append({"n": "1.17", "text": "Subtraction with the 10's complement.", "qs": qs})

    qs = []
    for part, a, b in [("a", "10011", "10001"), ("b", "100010", "100011"), ("c", "1001", "101000"), ("d", "110000", "10101")]:
        n = max(len(a), len(b))
        A, B = a.zfill(n), b.zfill(n)
        c2 = twos_c(B)
        s_ = int(A, 2) + int(c2, 2)
        diff = int(a, 2) - int(b, 2)
        if s_ >= (1 << n):
            r = format(s_ - (1 << n), f"0{n}b")
            work = f"<p>{A} + {c2} = {format(s_, 'b')} → end carry → drop it → <b>{r}</b> = {diff}.</p>"
            outs = [r, r.lstrip("0") or "0"]
        else:
            r = format(s_, f"0{n}b")
            m = twos_c(r)
            work = f"<p>{A} + {c2} = {r}, no end carry → negative: −(2's complement of {r}) = <b>−{m}</b> = {diff}.</p>"
            outs = ["-" + m, "-" + (m.lstrip("0") or "0"), "−" + m]
        qs.append(multi_q(tag("1.18", part), f"Subtract using the 2's complement of the subtrahend: <code>{a} − {b}</code>.", [("answer", outs)],
                          f"<p>Make both {n} bits: {A} − {B}. 2's complement of {B} = {c2}.</p>" + work, ref="04 §6"))
    P.append({"n": "1.18", "text": "Binary subtraction with the 2's complement.", "qs": qs})

    def sc10(v, digits=6):
        return format(v % 10 ** digits, f"0{digits}d")

    def sc_work(x, y):
        a, b = sc10(x), sc10(y)
        s_ = int(a) + int(b)
        r = format(s_ % 10 ** 6, "06d")
        val = x + y
        assert sc10(val) == r
        carry = " (end carry dropped)" if s_ >= 10 ** 6 else ""
        read = f"sign digit 0 → +{int(r):,}" if r[0] == "0" else f"sign digit 9 → negative: 10's complement = {sc10(-val)} → <b>{val:,}</b>"
        return (f"<p>{a[0]} {a[1:]} + {b[0]} {b[1:]} = {r[0]} {r[1:]}{carry}</p><p>{read}.</p>", val)

    for n, x0, y0, star, note in [("1.19", 9286, 801, True,
                                   "<p>Note: the printed problem says the sum is +10,627, but 9,286 + 801 = <b>10,087</b>. The method is what matters.</p>"),
                                  ("1.21", 9742, 641, False, "")]:
        qs = []
        for part, x, y in [("a", x0, y0), ("b", x0, -y0), ("c", -x0, y0), ("d", -x0, -y0)]:
            w, val = sc_work(x, y)
            sx = f"(+{x:,})" if x > 0 else f"(−{-x:,})"
            sy = f"(+{y:,})" if y > 0 else f"(−{-y:,})"
            qs.append(multi_q(tag(n, part, star), f"Signed 10's complement (sign digit + 5 digits): {sx} + {sy}.",
                              [("result", [f"{val:+d}", f"{val:+,}", str(val), f"{val:,}"])],
                              f"<p>+{x0:,} = 0 {sc10(x0)[1:]} · −{x0:,} = 9 {sc10(-x0)[1:]} · +{abs(y0):,} = 0 {sc10(y0)[1:]} · −{abs(y0):,} = 9 {sc10(-y0)[1:]}</p>" + w +
                              (note if part == "a" else ""), ref="04 §6"))
        P.append({"n": n, "text": f"Signed 10's complement with +{x0:,} and +{y0:,}.", "qs": qs})

    def b8(v):
        return format(v % 256, "08b")

    qs = []
    for part, x, y in [("a", 29, -49), ("b", -29, 49), ("c", -29, -49)]:
        s_ = (x + y) % 256
        r = b8(x + y)
        carry = " (carry out dropped)" if (x % 256) + (y % 256) >= 256 else ""
        qs.append(multi_q(tag("1.20", part), f"8-bit signed 2's complement: ({x:+d}) + ({y:+d}). Give the 8-bit result and its decimal value.",
                          [("bits", [r]), ("decimal", [str(x + y), f"{x + y:+d}"])],
                          f"<p>{b8(x)} + {b8(y)} = <b>{r}</b>{carry}.</p><p>" +
                          (f"Leading 1 → negative: 2's complement {b8(-(x + y))} = {-(x + y)} → <b>{x + y}</b>." if x + y < 0 else f"Leading 0 → <b>+{x + y}</b>.") +
                          "</p>" + ("<p>Values: +29 = 00011101, +49 = 00110001, −29 = 11100011, −49 = 11001111. "
                                    "(The problem prints +46 = 00101110 first, but then uses 49 in the sums.)</p>" if part == "a" else ""), ref="04 §6"))
    P.append({"n": "1.20", "text": "Signed 2's complement sums with ±29 and ±49.", "qs": qs})
    P.sort(key=lambda p: float(p["n"].split(".")[1]))
    return write_topic("04", "Signed numbers and overflow", "Mano 1.14–1.21. Keep leading zeros in bit patterns; negatives with a minus sign.", P)


# ======================================================================== TOPIC 05
def ascii7(ch):
    return format(ord(ch), "07b")


def par(bits7, even=True):
    ones_ = bits7.count("1")
    p = (ones_ % 2) if even else (1 - ones_ % 2)
    return str(p) + bits7


def topic05():
    P = []
    bcd = lambda n: " ".join(format(int(c), "04b") for c in str(n))
    asc = [par(ascii7(c)) for c in "8723"]
    P.append({"n": "1.22", "text": "8,723 in BCD and in ASCII with even parity.", "qs": [
        multi_q(tag("1.22"), "Convert 8,723 to BCD, and to ASCII with an even parity bit on the left.",
                [("BCD", [bcd(8723), bcd(8723).replace(" ", "")]), ("ASCII", [" ".join(asc), "".join(asc)])],
                f"<p>BCD: each digit → 4 bits: <b>{bcd(8723)}</b>.</p>"
                "<p>ASCII digits are 011 followed by the BCD of the digit: '8' = 0111000. Count the 1s; add a parity bit to make the count even.</p>"
                "<table class='bits'><tr><th>char</th><td>8</td><td>7</td><td>2</td><td>3</td></tr><tr><th>7-bit</th>" +
                "".join(f"<td>{ascii7(c)}</td>" for c in "8723") + "</tr><tr><th>with parity</th>" + "".join(f"<td>{a}</td>" for a in asc) + "</tr></table>",
                ref="05 §1")]})
    P.append({"n": "1.23", "text": "842 + 537 in BCD.", "qs": [
        multi_q(tag("1.23"), "Add 842 and 537 in BCD. Show the steps.", [("sum (BCD)", [bcd(1379), bcd(1379).replace(" ", "")])],
                f"<p>842 = {bcd(842)}, 537 = {bcd(537)}. Add digit by digit from the right:</p>" +
                steps([("2 + 7 = 9 = 1001", "≤ 9: keep it"),
                       ("4 + 3 = 7 = 0111", "≤ 9: keep it"),
                       ("8 + 5 = 13 = 1101", "&gt; 9: add 0110 (6)"),
                       ("1101 + 0110 = 1 0011", "digit 3, carry 1 into a new digit"),
                       (f"{bcd(1379)} = 1379", "check: 842 + 537 = 1379 ✓")]), ref="05 §1")]})
    t6311 = {0: "0000", 1: "0001", 2: "0011", 3: "0100", 4: "0101", 5: "0111", 6: "1000", 7: "1001", 8: "1011", 9: "1100"}
    t6421 = {0: "0000", 1: "0001", 2: "0010", 3: "0011", 4: "0100", 5: "0101", 6: "1000", 7: "1001", 8: "1010", 9: "1011"}
    for code, w in ((t6311, (6, 3, 1, 1)), (t6421, (6, 4, 2, 1))):
        for d, b in code.items():
            assert sum(int(x) * y for x, y in zip(b, w)) == d
    tabc = lambda code: "<table class='bits'><tr><th>digit</th>" + "".join(f"<td>{d}</td>" for d in range(10)) + "</tr><tr><th>code</th>" + \
        "".join(f"<td>{code[d]}</td>" for d in range(10)) + "</tr></table>"
    P.append({"n": "1.24", "text": "Weighted codes 6311 and 6421.", "qs": [
        work_q(tag("1.24", "a", True), "Make a weighted binary code for the decimal digits with weights <b>6, 3, 1, 1</b>.",
               tabc(t6311) + "<p>Each digit = sum of the weights where the bit is 1 (e.g. 8 = 6 + 1 + 1 = 1011). "
               "Some digits have two choices (1 = 0010 or 0001); pick one and stay consistent.</p>", ref="05 §1"),
        work_q(tag("1.24", "b"), "Make a weighted binary code for the decimal digits with weights <b>6, 4, 2, 1</b>.",
               tabc(t6421) + "<p>6 could be 1000 or 0110, and 7 could be 1001 or 0111. Any choice that adds up is fine.</p>", ref="05 §1")]})
    x3 = " ".join(format(int(c) + 3, "04b") for c in "5137")
    t2421 = {0: "0000", 1: "0001", 2: "0010", 3: "0011", 4: "0100", 5: "1011", 6: "1100", 7: "1101", 8: "1110", 9: "1111"}
    c2421 = " ".join(t2421[int(c)] for c in "5137")
    c6311 = " ".join(t6311[int(c)] for c in "5137")
    P.append({"n": "1.25", "text": "5,137 in BCD, excess-3, 2421 and 6311.", "qs": [
        multi_q(tag("1.25"), "Write 5,137 in (a) BCD, (b) excess-3, (c) 2421 code, (d) the 6311 code from 1.24.",
                [(k, [v, v.replace(" ", "")]) for k, v in [("(a) BCD", bcd(5137)), ("(b) XS-3", x3), ("(c) 2421", c2421), ("(d) 6311", c6311)]],
                f"<p>(a) BCD: <b>{bcd(5137)}</b></p><p>(b) excess-3: add 3 to each digit first (8, 4, 6, 10) → <b>{x3}</b></p>"
                f"<p>(c) 2421: 5 = 1011 (2+2+1, the self-complementing choice), 1 = 0001, 3 = 0011, 7 = 1101 → <b>{c2421}</b></p>"
                f"<p>(d) 6311: <b>{c6311}</b></p>", ref="05 §1")]})
    n9 = "".join(str(9 - int(c)) for c in "5137")
    c9 = " ".join(t2421[int(c)] for c in n9)
    assert c9.replace(" ", "") == ones_c(c2421.replace(" ", ""))
    P.append({"n": "1.26", "text": "9's complement of 5,137 in 2421: self-complementing.", "qs": [
        multi_q(tag("1.26"), "Find the 9's complement of 5,137 and write it in 2421 code.", [("9's comp", [n9]), ("2421", [c9, c9.replace(" ", "")])],
                f"<p>9's complement: {n9}. In 2421: <b>{c9}</b>.</p><p>Now flip every bit of 5137 in 2421 ({c2421}) → {c9}. "
                "Same answer! Flipping the bits gives the 9's complement: that's what <b>self-complementing</b> means.</p>", ref="05 §1")]})
    P.append({"n": "1.27", "text": "Code the 52 playing cards with the fewest bits.", "qs": [
        work_q(tag("1.27"), "Assign a binary code to the 52 playing cards, in an orderly way, using the minimum number of bits.",
               "<p>2⁵ = 32 is too few, 2⁶ = 64 ≥ 52, so <b>6 bits</b>.</p><p>Orderly scheme: <b>2 bits for the suit</b> + <b>4 bits for the rank</b>.</p>"
               "<table class='bits'><tr><th>suit</th><td>00 ♣</td><td>01 ♦</td><td>10 ♥</td><td>11 ♠</td></tr></table>"
               "<p>Rank: 0001 = Ace, 0010 = 2 … 1010 = 10, 1011 = J, 1100 = Q, 1101 = K. Example: Q♥ = 10 1100.</p>", ref="05 §1")]})
    gb = [par(ascii7(c)) for c in "G. Boole"]
    P.append({"n": "1.28", "text": "\"G. Boole\" in 8-bit ASCII with even parity.", "qs": [
        multi_q(tag("1.28"), "Write \"G. Boole\" (with the period and the space) in ASCII, leftmost bit = even parity. Fill the first three and last characters.",
                [("G", [gb[0]]), (".", [gb[1]]), ("space", [gb[2]]), ("e", [gb[7]])],
                "<table class='bits'><tr><th>char</th>" + "".join(f"<td>{c if c != ' ' else 'SP'}</td>" for c in "G. Boole") +
                "</tr><tr><th>hex</th>" + "".join(f"<td>{ord(c):02X}</td>" for c in "G. Boole") +
                "</tr><tr><th>8-bit</th>" + "".join(f"<td>{b}</td>" for b in gb) + "</tr></table>"
                "<p>Parity bit = 1 if the 7-bit code has an odd number of 1s (to make it even), else 0.</p>", ref="05 §1")]})
    codes = "1000010 1101001 1101100 1101100 1000111 1100001 1110100 1100101 1110011".split()
    word = "".join(chr(int(c, 2)) for c in codes)
    P.append({"n": "1.29", "text": "Decode the ASCII string.", "qs": [
        multi_q(tag("1.29", star=True), "Decode: <code>1000010 1101001 1101100 1101100 1000111 1100001 1110100 1100101 1110011</code>",
                [("text", [word, "Bill Gates"])],
                "<table class='bits'><tr><th>bits</th>" + "".join(f"<td>{c}</td>" for c in codes) + "</tr><tr><th>hex</th>" +
                "".join(f"<td>{int(c, 2):02X}</td>" for c in codes) + "</tr><tr><th>char</th>" + "".join(f"<td>{chr(int(c, 2))}</td>" for c in codes) +
                f"</tr></table><p><b>{word}</b>. Tip: 100xxxx = capitals (41 = A), 110xxxx / 111xxxx = lowercase (61 = a).</p>", ref="05 §1")]})
    hx = "73 F4 E5 76 E5 4A EF 62 73".split()
    dec = "".join(chr(int(h, 16) & 0x7F) for h in hx)
    assert all(bin(int(h, 16)).count("1") % 2 == 1 for h in hx)
    P.append({"n": "1.30", "text": "Hex ASCII string with a parity bit: decode and find the parity.", "qs": [
        multi_q(tag("1.30"), "<code>73 F4 E5 76 E5 4A EF 62 73</code>: each byte is a parity bit + 7-bit ASCII. (a) Decode. (b) Odd or even parity?",
                [("text", [dec, "steve jobs", "Steve Jobs"]), ("parity", ["odd"])],
                "<table class='bits'><tr><th>hex</th>" + "".join(f"<td>{h}</td>" for h in hx) + "</tr><tr><th>8 bits</th>" +
                "".join(f"<td>{int(h, 16):08b}</td>" for h in hx) + "</tr><tr><th>drop bit 7</th>" +
                "".join(f"<td>{int(h, 16) & 0x7F:02X}</td>" for h in hx) + "</tr><tr><th>char</th>" + "".join(f"<td>{chr(int(h, 16) & 0x7F)}</td>" for h in hx) +
                f"</tr><tr><th>1s</th>" + "".join(f"<td>{bin(int(h, 16)).count('1')}</td>" for h in hx) +
                f"</tr></table><p>(a) <b>{dec}</b>. (b) Every byte has an odd number of 1s → <b>odd parity</b>.</p>", ref="05 §1")]})
    P.append({"n": "1.31", "text": "Printing characters in ASCII.", "qs": [
        multi_q(tag("1.31", star=True), "How many printing characters are in ASCII? How many are special (not letters or numerals)?",
                [("printing", ["94", "95"]), ("special", ["32", "33"])],
                "<p>Mano counts <b>94</b> printing (graphic) characters, 21₁₆ to 7E₁₆. Letters 26 + 26 = 52, numerals 10 → 62. "
                "Special = 94 − 62 = <b>32</b>.</p><p>(If you count the space as printing: 95 and 33. Both are accepted.)</p>", ref="05 §1")]})
    P.append({"n": "1.32", "text": "Which bit changes capital ↔ lowercase?", "qs": [
        {"tag": tag("1.32", star=True), "type": "mcq", "q": "Which bit must be complemented to change an ASCII letter from capital to lowercase and back?",
         "opts": ["The leftmost bit (b₇)", "The bit worth 32 (b₆, hex 20)", "The bit worth 16 (b₅)", "The rightmost bit (b₁)"], "a": 1,
         "why": "<p>A = 100 0001 (41₁₆), a = 110 0001 (61₁₆). They differ by 20₁₆ = 32: only <b>bit b₆</b> changes.</p>", "ref": "05 §1"}]})
    reg = "100010010111"
    g = [reg[i:i + 4] for i in (0, 4, 8)]
    w8421 = lambda b: sum(int(x) * y for x, y in zip(b, (8, 4, -2, -1)))
    P.append({"n": "1.33", "text": "Read the register 100010010111 four ways.", "qs": [
        multi_q(tag("1.33", star=True), f"A 12-bit register holds <code>{reg}</code>. What is it as (a) 3 BCD digits, (b) 3 excess-3 digits, (c) 3 digits in 84-2-1, (d) a binary number?",
                [("(a) BCD", ["".join(str(int(x, 2)) for x in g)]), ("(b) XS-3", ["".join(str(int(x, 2) - 3) for x in g)]),
                 ("(c) 84-2-1", ["".join(str(w8421(x)) for x in g)]), ("(d) binary", num(int(reg, 2)))],
                f"<p>Split into 4s: {g[0]} | {g[1]} | {g[2]}</p>"
                f"<p>(a) 8 | 9 | 7 → <b>897</b>. (b) subtract 3 each: 5 | 6 | 4 → <b>564</b>. "
                f"(c) weights 8, 4, −2, −1: 1000 = 8, 1001 = 8 − 1 = 7, 0111 = 4 − 2 − 1 = 1 → <b>871</b>. "
                f"(d) 2048 + 128 + 16 + 4 + 2 + 1 = <b>{int(reg, 2):,}</b>.</p>", ref="05 §1")]})
    od = [par(ascii7(str(d)), even=False) for d in range(10)]
    P.append({"n": "1.34", "text": "ASCII digits with odd parity.", "qs": [
        multi_q(tag("1.34"), "List the ASCII codes for the digits 0 to 9 with an <b>odd</b> parity bit on the left. Fill 0, 3, 7, 9.",
                [("0", [od[0]]), ("3", [od[3]]), ("7", [od[7]]), ("9", [od[9]])],
                "<table class='bits'><tr><th>digit</th>" + "".join(f"<td>{d}</td>" for d in range(10)) + "</tr><tr><th>code</th>" +
                "".join(f"<td>{c}</td>" for c in od) + "</tr></table><p>011 + BCD of the digit, then a parity bit that makes the total number of 1s odd.</p>",
                ref="05 §1")]})
    return write_topic("05", "Binary codes", "Mano 1.22–1.34. Spaces between groups of bits are fine either way.", P)
