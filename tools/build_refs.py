"""Build docs/refs.js: where each quiz 'From the notes' reference points.
Run: python3 tools/build_refs.py   (check.py fails if a reference has no heading)"""
import os, re, json, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "notes")


def slug(h):
    """GitHub's heading anchor: lowercase, keep letters/marks/numbers/_/-/space, spaces become '-'."""
    out = ""
    for ch in h.lower():
        if ch in " -_" or unicodedata.category(ch)[0] in "LMN" or unicodedata.category(ch) == "Pc":
            out += "-" if ch == " " else ch
    return out


def build():
    refs = {}
    for fn in sorted(os.listdir(NOTES)):
        m = re.match(r"(\d\d)-.*\.md$", fn)
        if not m:
            continue
        t = {"file": fn[:-3]}
        seen = {}
        for line in open(os.path.join(NOTES, fn), encoding="utf8"):
            h = re.match(r"## (.+?)\s*$", line)
            if not h:
                continue
            text = h.group(1)
            s = slug(text)
            n = seen.get(s, 0)
            seen[s] = n + 1
            if n:
                s += "-%d" % n
            num = re.match(r"(\d+)\.", text)
            if num:
                t[num.group(1)] = s
            elif text.lower().startswith("exam drill"):
                t["exam drill"] = s
        refs[m.group(1)] = t
    return refs


if __name__ == "__main__":
    refs = build()
    with open(os.path.join(ROOT, "docs", "refs.js"), "w", encoding="utf8") as f:
        f.write("window.QUIZ_REFS = " + json.dumps(refs, ensure_ascii=False, indent=1) + ";\n")
    print("refs ok", len(refs))
