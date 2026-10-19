"""Check the whole repo: quiz answers, minimality, links and images.

Run: python3 tools/check.py   (needs node)
"""
import json, os, re, subprocess, itertools, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = []


def fail(msg):
    bad.append(msg)


# ---------------------------------------------------------- minimal SOP by brute force
def implicants(nv):
    """Every product term as (mask, value): mask bit set = variable present."""
    for mask in range(1 << nv):
        for val in range(1 << nv):
            if val & ~mask:
                continue
            yield mask, val


def covers(term, m):
    mask, val = term
    return (m & mask) == val


def min_sop_lits(nv, ones, dc):
    ones, dc = set(ones), set(dc)
    if not ones:
        return 0
    allowed = ones | dc
    primes = []
    terms = [t for t in implicants(nv) if all(m in allowed for m in range(1 << nv) if covers(t, m))]
    # keep prime implicants only
    for t in terms:
        if not any(u != t and (u[0] & t[0]) == u[0] and (t[1] & u[0]) == u[1] for u in terms):
            primes.append(t)
    lits = lambda t: bin(t[0]).count("1")
    best = None
    for k in range(1, len(primes) + 1):
        for combo in itertools.combinations(primes, k):
            if all(any(covers(t, m) for t in combo) for m in ones):
                n = sum(lits(t) for t in combo)
                best = n if best is None else min(best, n)
        if best is not None and k > 4 and best <= k:  # cannot improve with more terms
            break
    return best


def check_refs():
    import build_refs
    refs = build_refs.build()
    for fn in sorted(os.listdir(os.path.join(ROOT, "docs", "data"))):
        txt = open(os.path.join(ROOT, "docs", "data", fn), encoding="utf8").read()
        for ref in re.findall(r'"ref": "([^"]*)"', txt):
            m = re.fullmatch(r"(\d\d)(?: (?:§(\d+)|(exam drill)))?", ref)
            if not m or m.group(1) not in refs:
                fail(f"{fn}: bad ref {ref!r}")
            key = m.group(2) or m.group(3)
            if key and key not in refs[m.group(1)]:
                fail(f"{fn}: ref {ref!r} has no matching heading in the notes")
    cur = open(os.path.join(ROOT, "docs", "refs.js"), encoding="utf8").read()
    if cur != "window.QUIZ_REFS = " + json.dumps(refs, ensure_ascii=False, indent=1) + ";\n":
        fail("docs/refs.js is out of date: run python3 tools/build_refs.py")


def check_quiz():
    raw = subprocess.check_output(["node", os.path.join(ROOT, "tools", "dump.js")], text=True)
    qs = json.loads(raw)
    print(f"{len(qs)} quiz questions")
    for r in qs:
        tag = f"quiz {r['topic']} #{r['i']+1}"
        if r["type"] == "bool":
            if not r["verdict"].get("ok"):
                fail(f"{tag}: model answer {r['show']!r} rejected by engine: {r['verdict']}")
            nv = len(r["vars"])
            if r["form"] in ("sop", "pos"):
                if r["form"] == "sop":
                    m = min_sop_lits(nv, r["ones"], r["dc"])
                else:
                    zeros = [x for x in range(1 << nv) if x not in r["ones"] and x not in r["dc"]]
                    m = min_sop_lits(nv, zeros, r["dc"])
                if r["lits"] != m:
                    fail(f"{tag}: lits={r['lits']} but true minimum {r['form']} letters = {m}")
            if r.get("lits") is not None and r["showLits"] != r["lits"]:
                fail(f"{tag}: model answer has {r['showLits']} letters, lits says {r['lits']}")
        if r["type"] == "mcq" and not (0 <= r["a"] < r["nopts"]):
            fail(f"{tag}: answer index out of range")
        if r["type"] == "tt":
            for k, v in r["outs"].items():
                if len(v) != 2 ** len(r["vars"]):
                    fail(f"{tag}: output {k} has {len(v)} rows")
    return qs


def check_tt():
    """Recompute the truth-table questions."""
    exp = {
        ("06", "f"): [int((x | (1 - y)) & z | (1 - x)) for x in (0, 1) for y in (0, 1) for z in (0, 1)],
        ("07", "f"): [0 if m in (0, 3, 5) else 1 for m in range(8)],
        ("10", "C"): None,
    }
    raw = json.loads(subprocess.check_output(["node", os.path.join(ROOT, "tools", "dump.js")], text=True))
    for r in raw:
        if r["type"] != "tt":
            continue
        n = len(r["vars"])
        rows = [[(m >> (n - 1 - b)) & 1 for b in range(n)] for m in range(2 ** n)]
        for k, v in r["outs"].items():
            if r["topic"] == "10":
                want = [sum(rw) >> 1 if k == "C" else sum(rw) & 1 for rw in rows]
            else:
                want = exp.get((r["topic"], k))
            if want is not None and want != v:
                fail(f"tt {r['topic']} #{r['i']+1} output {k}: {v} != {want}")


def check_numbers():
    """Arithmetic behind the number-topic answers."""
    def b(s):
        if "." in s:
            w, f = s.split(".")
            return int(w or "0", 2) + sum(int(c) * 2 ** -(i + 1) for i, c in enumerate(f))
        return int(s, 2)
    checks = [
        (b("1101.01"), 13.25), (b("10110.011"), 22.375), (0x2F, 47), (0o157, 111), (b("11001"), 25),
        (b("0.1011"), 0.6875), (0x7B, 123), (b("1111011.00101"), 123.15625), (int("26153", 8), int("10110001101011", 2)),
        (0x3A, 0o72), (0xC5, b("11000101")), (b("1100"), 7 + 5), (b("10001"), 11 + 6), (b("1000110"), 43 + 27),
        (b("100011"), 7 * 5), (b("1001110"), 13 * 6), (b("10010001") // b("1011"), b("1101")), (b("10010001") % b("1011"), 2),
        ((256 - 20), b("11101100")), (b("10101010"), 256 - b("01010110")), (b("11011000"), 256 - b("00101000")),
        (5 * 8 + 1 + 0.6875, 41.6875), (0x7B + 0x28 / 256, 123.15625),
    ]
    for i, (a, w) in enumerate(checks):
        if abs(a - w) > 1e-9:
            fail(f"number check {i}: {a} != {w}")


def check_links():
    md = []
    for d, _, fs in os.walk(ROOT):
        if "/.git" in d:
            continue
        md += [os.path.join(d, f) for f in fs if f.endswith(".md")]
    used_imgs = set()
    for f in md:
        txt = open(f, encoding="utf8").read()
        for m in re.finditer(r"!?\[[^\]]*\]\(([^)\s]+)\)", txt):
            url = m.group(1).split("#")[0]
            if url.startswith("http") or not url:
                continue
            p = os.path.normpath(os.path.join(os.path.dirname(f), url))
            if not os.path.exists(p):
                fail(f"{os.path.relpath(f, ROOT)}: broken link {url}")
            used_imgs.add(p)
        if txt.count("<details") != txt.count("</details>"):
            fail(f"{os.path.relpath(f, ROOT)}: unbalanced <details>")
    # svg refs in the quiz data
    for f in os.listdir(os.path.join(ROOT, "docs", "data")):
        txt = open(os.path.join(ROOT, "docs", "data", f), encoding="utf8").read()
        for m in re.finditer(r"svg/([\w-]+)\.svg", txt):
            if not os.path.exists(os.path.join(ROOT, "docs", "svg", m.group(1) + ".svg")):
                fail(f"data/{f}: missing svg {m.group(1)}")
        for m in re.finditer(r'"svg": "([\w-]+)"', txt):
            if not os.path.exists(os.path.join(ROOT, "docs", "svg", m.group(1) + ".svg")):
                fail(f"data/{f}: missing svg {m.group(1)}")
    # unused slide crops
    imgdir = os.path.join(ROOT, "img")
    unused = []
    for d, _, fs in os.walk(imgdir):
        for x in fs:
            p = os.path.join(d, x)
            if p not in used_imgs:
                unused.append(os.path.relpath(p, ROOT))
    return unused


if __name__ == "__main__":
    check_refs()
    check_quiz()
    check_tt()
    check_numbers()
    unused = check_links()
    if unused:
        print(f"{len(unused)} unused slide images (delete with --prune)")
        if "--prune" in sys.argv:
            for u in unused:
                os.remove(os.path.join(ROOT, u))
    if bad:
        print("\n".join("FAIL " + b for b in bad))
        sys.exit(1)
    print("all checks passed")
