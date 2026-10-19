"""Independent check of the fresh-number generators (docs/gen.js).
Runs every generator many times through node, then recomputes each answer here in Python."""
import json, os, re, subprocess
from fractions import Fraction as F

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def to_base(x, base, maxf=12):
    w, f = int(x), x - int(x)
    digs = "0123456789ABCDEF"
    s = ""
    while True:
        s = digs[w % base] + s; w //= base
        if not w: break
    fr = ""
    while f and len(fr) < maxf:
        f *= base; d = int(f); fr += digs[d]; f -= d
    return s + ("." + fr if fr else "")


def from_base(s, base):
    w, _, fr = s.partition(".")
    v = F(int(w, base))
    for i, c in enumerate(fr):
        v += F(int(c, base), base ** (i + 1))
    return v


def tc(s):
    v = int(s, 2)
    return v - (1 << len(s)) if s[0] == "1" else v


def nums(q):
    return [int(x) for x in re.findall(r"-?\d+", q.replace("−", "-"))]


def expect(r):
    """Return the answer(s) we expect: str for text, list for multi, or None if not independently checked."""
    g, q = r["gen"], r["q"]
    m = lambda pat: re.search(pat, q).group(1)
    if g == "b2d": return str(from_base(m(r"Convert ([01.]+)₂"), 2).__float__())
    if g == "h2d": return str(int(m(r"Convert ([0-9A-F]+)₁₆"), 16))
    if g == "o2d": return str(int(m(r"Convert ([0-7]+)₈"), 8))
    if g == "d2b": return bin(int(m(r"Convert (\d+) to"))) [2:]
    if g == "f2b": return "0." + to_base(F(m(r"Convert ([\d.]+) to")), 2).split(".")[1]
    if g == "d2h": return to_base(int(m(r"Convert (\d+) to")), 16)
    if g == "d2o": return to_base(F(m(r"Convert ([\d.]+) to")), 8)
    if g == "b2h": return to_base(from_base(m(r"Convert ([01.]+)₂"), 2), 16)
    if g == "b2o": return to_base(from_base(m(r"Convert ([01]+)₂"), 2), 8)
    if g == "h2o": return to_base(int(m(r"Convert ([0-9A-F]+)₁₆"), 16), 8)
    if g == "h2b": return format(int(m(r"shows ([0-9A-F]+)₁₆"), 16), "08b")
    if g == "d2bh":
        v = F(m(r"Convert ([\d.]+)\.$")); return [to_base(v, 2), to_base(v, 16)]
    if g in ("badd", "bsub", "bmul"):
        a, op, b = re.match(r"([01]+) ([+−×]) ([01]+)", q).groups(); a, b = int(a, 2), int(b, 2)
        v = a + b if op == "+" else a - b if op == "−" else a * b
        return bin(v)[2:] if op != "−" else format(v, "0%db" % int(m(r"give (\d) bits")))
    if g == "bdiv":
        a, b = re.match(r"([01]+) ÷ ([01]+)", q).groups(); a, b = int(a, 2), int(b, 2)
        return [bin(a // b)[2:], bin(a % b)[2:]]
    if g == "neg3":
        n = int(m(r"−(\d)")); return ["1" + format(n, "03b"), format(~n & 15, "04b"), format(-n & 15, "04b")]
    if g == "twos8": return format(-int(m(r"of ([01]{8})"), 2) & 255, "08b")
    if g == "neg8": return format(-int(m(r"−(\d+)")) & 255, "08b")
    if g == "read6":
        s = m(r"Read ([01]{6})"); return [str(-int(s.translate(str.maketrans("01", "10")), 2)), str(tc(s))]
    if g == "read4": return str(tc(m(r"What is ([01]{4})")))
    if g == "ones_add":
        a, b = re.search(r"−(\d) \+ (\d)", q).groups(); v = int(b) - int(a)
        return format(v & 15 if v >= 0 else (~(-v)) & 15, "04b")
    if g == "twos_sub":
        a, b = re.search(r"out (\d) − (\d)", q).groups(); return format((int(a) - int(b)) & 15, "04b")
    if g == "overflow":
        a, b = re.search(r"([01]{4}) \+ ([01]{4})", q).groups(); s = tc(a) + tc(b)
        return [format(s & 15, "04b"), "yes" if not -8 <= s <= 7 else "no"]
    if g == "bitsfor":
        n = int(m(r"each of (\d+)")); k = 0
        while 2 ** k < n: k += 1
        return str(k)
    if g == "bcd": return "".join(format(int(d), "04b") for d in m(r"Write (\d+) in"))
    if g == "bcd2d": return str(int("".join(str(int(x, 2)) for x in m(r"BCD ([01 ]+) is").split())))
    if g == "bcdvalid": return 0 if all(int(x, 2) <= 9 for x in m(r"^([01 ]+) is").split()) else 1
    if g == "b2gray": n = int(m(r"binary ([01]{4})"), 2); return format(n ^ (n >> 1), "04b")
    if g == "graynext": n = int(m(r"for (\d+)\?")); return format(n ^ (n >> 1), "04b")
    if g == "onehot": return format(1 << (int(m(r"Write (\d)")) - 1), "08b")
    if g == "ttrows": return str(2 ** int(m(r"with (\d) inputs")))
    if g == "moore":
        n, y = re.search(r"has (\d+) million.*after (\d+) years", q).groups(); return str(int(n) * 2 ** (int(y) // 2))
    if g in ("sig2pi", "compl"):
        on = [int(x) for x in m(r"Σm\(([\d, ]+)\)").split(",")]; return ",".join(str(x) for x in range(8) if x not in on)
    if g == "rows2sigma": return ",".join(re.search(r"rows ([\d, ]+) only", q).group(1).replace(" ", "").split(","))
    if g == "picount": return str(16 - len(m(r"ΠM\(([\d, ]+)\)").split(",")))
    if g == "xorchain":
        b = [int(x) for x in re.findall(r"[01]", q)]; return str(sum(b) % 2)
    if g == "fatrace":
        X, Y, Z = map(int, re.search(r"X = (\d), Y = (\d), Z = (\d)", q).groups()); S1 = X ^ Y
        return [str(S1), str(X & Y), str(S1 & Z), str(S1 ^ Z), str((X + Y + Z) >> 1)]
    if g == "ripple":
        n, d = re.search(r"A (\d+)-bit.*?(\d+) ns", q).groups(); return str(2 * int(n) * int(d))
    if g == "addrows": return str(2 ** (2 * int(m(r"of a (\d)-bit")) + 1))
    if g == "cla":
        a1, a0, b1, b0, c0 = map(int, re.search(r"A₁A₀ = (\d)(\d), B₁B₀ = (\d)(\d), C₀ = (\d)", q).groups())
        return [str(a0 & b0), str(a0 ^ b0), str(a1 & b1), str(a1 ^ b1), str((2 * a1 + a0 + 2 * b1 + b0 + c0) >> 2)]
    if g == "mult2":
        a, b = re.search(r"A₁A₀ = ([01]{2}), B₁B₀ = ([01]{2})", q).groups(); return list(format(int(a, 2) * int(b, 2), "04b"))
    if g == "decout": return str(int(m(r"input ([01]{3})"), 2))
    if g == "decor": return m(r"Σm\(([\d, ]+)\)").replace(" ", "")
    if g == "decor2":
        f, h = re.findall(r"Σm\(([\d, ]+)\)", q); low = "active-low" in q
        conv = lambda s: [int(x) for x in s.split(",")]
        pick = (lambda on: [x for x in range(8) if x not in on]) if low else (lambda on: on)
        return [",".join(map(str, pick(conv(f)))), ",".join(map(str, pick(conv(h))))]
    if g == "deccascade":
        k = int(m(r"= ([01]{3})"), 2); return ["top" if k < 4 else "bottom", str(k)]
    if g == "enc": return list(format(int(m(r"Only D(\S)").translate(str.maketrans("₀₁₂₃₄₅₆₇", "01234567"))), "03b"))
    if g == "prienc": return format(max(int(x) for x in re.findall(r"D(\d)", q)), "03b")
    if g == "muxsel": return "I" + str(int(m(r"= ([01]+)\."), 2))
    if g == "muxtree":
        per, n = re.search(r"many (\d)-to-1 muxes make a (\d+)-to-1", q).groups(); per, n = int(per), int(n); t = 0
        while n > 1: n //= per; t += n
        return str(t)
    if g == "demux": k = int(m(r"= ([01]{2}),"), 2); return ["1" if i == k else "0" for i in range(4)]
    if g == "mux8":
        on = [int(x) for x in m(r"Σm\(([\d, ]+)\)").split(",")]; return ["1" if i in on else "0" for i in range(8)]
    if g in ("mux4res", "mux8res"):
        on = [int(x) for x in m(r"Σm\(([\d, ]+)\)").split(",")]; v = "z" if g == "mux4res" else "D"; out = []
        for k in range(4 if g == "mux4res" else 8):
            a, b = 2 * k in on, 2 * k + 1 in on
            out.append(("1" if a else "0") if a == b else (v if b else v + "'"))
        return out
    if g == "cmos":
        out = []
        for n, kind in re.findall(r"(\d)-in (\w+)", " ".join(f[0] for f in r["fields"])):
            out.append(str(2 * int(n) + (0 if kind in ("NAND", "NOR") else 2)))
        return out + ["2"]
    return None


def run(min_lits, n=150):
    raw = subprocess.check_output(["node", os.path.join(ROOT, "tools", "gen_dump.js"), str(n)], text=True)
    rows = json.loads(raw)
    bad, checked, gens = [], 0, set()
    for r in rows:
        tag = f"gen {r.get('topic')} #{r.get('i', 0) + 1} {r.get('gen')}"
        if "error" in r: bad.append(f"{tag}: {r['error']}"); continue
        gens.add(r["gen"])
        if re.search(r"undefined|NaN|null|\[object", r["q"] + r.get("why", "")): bad.append(f"{tag}: junk text in {r['q']!r}")
        if not r.get("why"): bad.append(f"{tag}: no worked solution")
        if r["type"] == "bool":
            if not r["verdict"].get("ok"): bad.append(f"{tag}: engine rejects its own answer {r['show']!r}: {r['verdict']}")
            if r["form"] in ("sop", "pos"):
                nv = len(r["vars"])
                tgt = r["ones"] if r["form"] == "sop" else [x for x in range(1 << nv) if x not in r["ones"] and x not in r["dc"]]
                mm = min_lits(nv, tgt, r["dc"])
                if r["lits"] != mm: bad.append(f"{tag}: lits {r['lits']} but true minimum is {mm} for {r['q']}")
            if r["showLits"] != r["lits"]: bad.append(f"{tag}: shown answer has {r['showLits']} letters, lits says {r['lits']}")
        if r["type"] == "tt":
            for k, v in r["outs"].items():
                if len(v) != 2 ** len(r["vars"]): bad.append(f"{tag}: tt column {k} has {len(v)} rows")
        if r["type"] == "kmap" and not (0 < len(r["ones"]) < 2 ** len(r["vars"])): bad.append(f"{tag}: kmap has no 1s or all 1s")
        exp = expect(r)
        if exp is None: continue
        checked += 1
        if r["type"] == "text":
            if str(exp).lower() not in [a.lower() for a in r["ans"]]: bad.append(f"{tag}: {r['q']} → generator says {r['ans']}, Python says {exp}")
        elif r["type"] == "multi":
            for (lab, ans), e in zip(r["fields"], exp):
                if str(e).lower() not in [a.lower() for a in ans]: bad.append(f"{tag}: {r['q']} [{lab}] → {ans}, Python says {e}")
        elif r["type"] in ("tf", "mcq"):
            if r["a"] != exp: bad.append(f"{tag}: {r['q']} → a={r['a']}, Python says {exp}")
    return rows, gens, checked, bad
