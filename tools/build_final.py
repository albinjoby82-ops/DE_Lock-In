"""Build the final-exam Lock-In page: docs/final/data.js + figures, and stamp index.html.

Run: python3 tools/build_final.py

Content lives in final_path_a.py, final_path_b.py (the study path, slide order)
and final_papers.py (23/24 paper + mocks). Builders are in final_q.py and
final_more.py; every answer is computed and asserted there.
"""
import glob, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "docs", "final")
for f in glob.glob(os.path.join(OUT, "fig", "*.svg")):  # figures are all redrawn below
    os.remove(f)
sys.path.insert(0, HERE)
import final_site as site  # noqa: E402
import final_path_a, final_path_b, final_papers  # noqa: E402,F401

VERSION = "2026-11-22a"
data = dict(version=VERSION, module="EEEN20050 Digital Electronics", path=site.PATH, papers=site.PAPERS)

# unicode super/subscripts have no glyph in the page font: turn them into real <sup>/<sub>
SUP = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁺ⁿᵏᵐ", "0123456789+nkm"))
SUB = dict(zip("₀₁₂₃₄₅₆₇₈₉", "0123456789"))


def clean(o):
    if isinstance(o, str):
        o = re.sub("[" + "".join(SUP) + "]+", lambda m: "<sup>" + "".join(SUP[c] for c in m.group()) + "</sup>", o)
        return re.sub("[" + "".join(SUB) + "]+", lambda m: "<sub>" + "".join(SUB[c] for c in m.group()) + "</sub>", o)
    if isinstance(o, list):
        return [clean(x) for x in o]
    if isinstance(o, dict):
        for k in o:
            o[k] = clean(o[k])
    return o


clean(site.EX)
clean(data)

# ---------------------------------------------------------------- checks
ids, nq, nsim = {}, 0, 0
for mode in ("path", "papers"):
    seen = set()
    for p in data[mode]:
        for t in p["topics"]:
            assert t["qs"], t["id"]
            for q in t["qs"]:
                assert q["id"] not in seen, "duplicate id in " + mode + ": " + q["id"]
                seen.add(q["id"])
                assert q["q"] and (q.get("page") or (q["steps"] and q["a"])), q["id"]
                if q["id"] in ids:
                    assert ids[q["id"]] is q, "two different questions share the id " + q["id"]
                ids[q["id"]] = q
    data[mode + "_n"] = len(seen)
blob = json.dumps(data, ensure_ascii=False)
for src in set(re.findall(r'<img src=\\"([^"\\]+)\\"', blob)):
    assert os.path.exists(os.path.normpath(os.path.join(OUT, src))), "missing figure " + src
nq = sum(1 for q in ids.values() if not q.get("page"))
nsim = sum(1 for q in ids.values() if "sim" in q)
used = {os.path.basename(s) for s in re.findall(r'fig/([^"\\]+\.svg)', blob)}
for f in glob.glob(os.path.join(OUT, "fig", "*.svg")):  # drop figures nothing points at
    if os.path.basename(f) not in used:
        os.remove(f)

with open(os.path.join(OUT, "data.js"), "w", encoding="utf8") as f:
    f.write("window.DATA = " + blob + ";\n")
ver = hashlib.md5(blob.encode("utf8")).hexdigest()[:8]
ip = os.path.join(OUT, "index.html")
with open(ip, encoding="utf8") as f:
    h = f.read()
h2 = re.sub(r'<script src="data\.js(\?v=\w+)?"></script>', f'<script src="data.js?v={ver}"></script>', h)
assert h2 != h or ver in h
with open(ip, "w", encoding="utf8") as f:
    f.write(h2)
print("study path:", sum(len(p["topics"]) for p in site.PATH), "topics,", data["path_n"], "screens")
print("papers:", len(site.PAPERS), "papers,", data["papers_n"], "parts")
print("questions", nq, "· similar questions", nsim, "· figures", len(used), "· data.js?v=" + ver)
