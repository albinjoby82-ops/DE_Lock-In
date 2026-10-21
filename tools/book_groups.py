"""Skill groups for the book questions.

Each topic is split into a few skills, in learning order. Each skill has a small CORE set
(the questions that cover the skill; do these first) and MORE practice (the rest: same skill,
more reps). Keys are Mano tags without "Mano " and "★": "2.2 (c)" is one part, "2.5" is
every part of 2.5, and a trailing * matches any tag that starts with the text before it.
The builder fails if a question is in no group, in two groups, or a key matches nothing."""

GROUPS = {
    "02": [
        ("Any base → decimal", "Digit × place value, then add. Works for fractions too.",
         ["1.3 (a)", "1.9 (c)"], ["1.3 (b)", "1.3 (c)", "1.3 (d)", "1.9 (a)", "1.9 (b)", "1.9 (d)", "1.9 (e)"]),
        ("Decimal → binary or hex", "Divide for the whole part, multiply for the fraction.",
         ["1.8", "1.13 (a)"], ["1.13 (b)", "1.13 (c)"]),
        ("Binary ↔ hex ↔ octal", "Group the bits in 4s or 3s from the point.",
         ["1.7", "1.10"], []),
        ("Counting and sizes", "Powers of 2, the biggest n-bit number, counting in other bases.",
         ["1.4", "1.2"], ["1.1"]),
        ("Find the unknown base", "Write both sides in base b and solve.",
         ["1.5 (a)", "1.6"], ["1.5 (b)", "1.5 (c)"]),
    ],
    "03": [
        ("Binary and hex arithmetic", "Add, multiply and divide without converting to decimal.",
         ["1.12 (a)", "1.11"], ["1.12 (b)"]),
    ],
    "04": [
        ("1's and 2's complement", "Flip the bits; flip and add 1. Watch the all-0 and 1000… cases.",
         ["1.14 (c)", "1.14 (a)"], ["1.14 (b)", "1.14 (d)", "1.14 (e)", "1.14 (f)", "1.16"]),
        ("Subtract with complements", "Add the complement; an end carry means positive, none means negative.",
         ["1.18 (c)", "1.17 (b)"], ["1.18 (a)", "1.18 (b)", "1.18 (d)", "1.17 (a)", "1.17 (c)", "1.17 (d)"]),
        ("Signed 2's complement sums", "Add the bit patterns, read the sign bit.",
         ["1.20 (a)", "1.20 (c)"], ["1.20 (b)"]),
        ("9's and 10's complement", "The decimal version of 1's and 2's.",
         ["1.15 (a)", "1.15 (d)"], ["1.15 (b)", "1.15 (c)"]),
        ("Signed 10's complement sums", "Same idea with a sign digit 0 or 9.",
         ["1.19 (b)", "1.19 (d)"], ["1.19 (a)", "1.19 (c)", "1.21"]),
    ],
    "05": [
        ("BCD, excess-3 and weighted codes", "Write a number in each code, and read a register back.",
         ["1.25", "1.33"], ["1.24", "1.26", "1.27"]),
        ("BCD addition", "Add digit by digit; over 9 → add 6.",
         ["1.23"], []),
        ("ASCII and parity", "Read and write ASCII, add or check a parity bit.",
         ["1.29", "1.22"], ["1.28", "1.30", "1.34", "1.31", "1.32"]),
    ],
    "06": [
        ("Gates, truth tables and laws", "Evaluate gates on every input, and prove a law row by row.",
         ["1.35", "2.11 (a)", "2.1 (b)"], ["1.36", "2.11 (b)", "2.12", "2.1 (a)", "2.1 (c)", "2.1 (d)", "2.1 (e)", "2.18 (a)", "2.18 (d)", "2.26"]),
        ("Simplify with Boolean algebra", "Factor, kill the 1s and 0s, absorb, De Morgan. The biggest skill here.",
         ["2.2 (c)", "2.3 (b)", "2.4 (b)", "2.4 (c)"],
         ["2.2 (a)", "2.2 (b)", "2.2 (d)", "2.2 (e)", "2.2 (f)", "2.3 (a)", "2.3 (c)", "2.3 (d)", "2.3 (e)", "2.3 (f)",
          "2.4 (a)", "2.4 (d)", "2.4 (e)", "2.15", "2.18 (c)"]),
        ("Complements, duals and De Morgan", "Flip every letter, swap AND ↔ OR.",
         ["2.9 (a)", "2.9 (b)"], ["2.8", "2.9 (c)", "2.24*", "2.25"]),
        ("Truth table → circuit", "Read the 1s, simplify, draw.",
         ["2.27 (f₁)"], ["2.27 (f₂)", "2.27 (diagram)"]),
        ("Expression → circuit", "Inside brackets first; the outer operation is the last gate.",
         ["2.13 (b)", "2.23 (c)"], ["2.13 (a)", "2.13 (c)", "2.13 (d)", "2.13 (e)", "2.13 (f)", "2.23 (a)", "2.23 (b)", "2.23 (d)",
                                    "2.5", "2.6", "2.7", "2.18 (b)", "2.18 (e)"]),
        ("Build with one kind of gate", "De Morgan turns any AND/OR into NANDs or NORs.",
         ["2.14 (b)", "2.14 (d)"], ["2.14 (a)", "2.14 (c)", "2.14 (e)"]),
        ("Circuit → expression", "Label every gate output, work left to right, then simplify.",
         ["2.28 (a)", "4.2 (F)"], ["2.28 (b*", "4.2 (G)", "4.1*"]),
    ],
    "07": [
        ("Truth table → Σm and ΠM", "1-rows are the minterms, 0-rows the maxterms.",
         ["2.17 (a)", "2.19"], ["2.17 (b)", "2.17 (c)", "2.17 (d)"]),
        ("Switch forms and complements", "Swap Σ ↔ Π and list the missing numbers.",
         ["2.20 (b)", "2.21 (b)"], ["2.20 (a)", "2.21 (a)"]),
        ("SOP ↔ POS", "Multiply out for SOP, factor (or group the 0s) for POS.",
         ["2.22 (a · SOP)", "2.22 (a · POS)"], ["2.22 (b*"]),
        ("Why minterms work", "Short proofs about sums and products of minterms.",
         ["2.16 (a)"], ["2.16 (b)", "2.10"]),
    ],
    "08": [
        ("3-variable maps", "Fill from Σ, group in 1s, 2s, 4s, read each block.",
         ["3.1 (b)", "3.2 (b)"], ["3.1 (a)", "3.1 (c)", "3.1 (d)", "3.2 (a)", "3.2 (c)", "3.2 (d)", "3.2 (e)", "3.2 (f)"]),
        ("Plot an expression first", "Each term covers every cell its letters allow.",
         ["3.8 (b)", "3.3 (b)"], ["3.8 (a)", "3.8 (c)", "3.8 (d)", "3.3 (a)", "3.3 (c)", "3.3 (d)"]),
        ("4-variable maps", "Same rules, with corners and edges wrapping.",
         ["3.4 (c)", "3.5 (d)", "3.6 (a)"],
         ["3.4 (a)", "3.4 (b)", "3.4 (d)", "3.4 (e)", "3.4 (f)", "3.5 (a)", "3.5 (b)", "3.5 (c)", "3.6 (b)", "3.6 (c)", "3.6 (d)", "3.7"]),
        ("Prime implicants and essentials", "Biggest possible blocks; essentials first, then cover what's left.",
         ["3.9 (a)", "3.10 (c)"], ["3.9 (b)", "3.9 (c)", "3.9 (d)", "3.9 (e)", "3.9 (f)", "3.10 (a)", "3.10 (b)", "3.10 (d)", "3.10 (e)", "3.10 (f)"]),
        ("POS: group the 0s", "Each 0-block gives an OR term.",
         ["3.12 (b)", "3.13 (a · POS)"], ["3.12 (a)", "3.12 (c)", "3.13 (a · SOP)", "3.13 (b*", "3.13 (c*", "3.13 (d*"]),
        ("5-variable maps", "Two 4-variable maps side by side.",
         ["3.11 (a)"], ["3.11 (b)"]),
        ("Harder ones", "Combine two maps, or beat the SOP with XOR.",
         ["3.26"], ["3.14"]),
    ],
    "09": [
        ("Don't cares", "Use an x only when it makes a block bigger.",
         ["3.15 (b*"], ["3.15 (a*", "3.15 (c*", "3.15 (d*"]),
        ("NAND-NAND from SOP", "Every gate becomes a NAND; lone letters go in complemented.",
         ["3.16 (b)", "3.16 (b · NAND)", "3.17*"], ["3.16 (a*", "3.16 (c*", "3.16 (d*"]),
        ("NOR-NOR from POS", "The same trick from the POS.",
         ["3.19 (a*"], ["3.19 (b*", "3.19 (c*", "3.23*"]),
        ("Multi-level NAND and NOR", "Bubble pushing: two bubbles cancel, one left over is an inverter.",
         ["3.21", "3.20 (NAND)"], ["3.20 (NOR)", "3.22", "3.18"]),
        ("Other two-level forms", "AND-NOR, NAND-AND, OR-NAND, NOR-OR all start from F'.",
         ["3.24 (b)"], ["3.24 (a)", "3.24 (c)", "3.24 (d)", "3.25"]),
    ],
    "10": [
        ("XOR and parity", "Odd number of 1s → XOR is 1.",
         ["3.28 (generator)", "3.30"], ["3.28 (checker)", "3.33", "4.21"]),
        ("Design from a word description", "Words → truth table → K-map → circuit.",
         ["4.4 (a)", "4.6 (table)", "4.6 (a)"], ["4.4 (b)", "4.5*", "4.6 (diagram)"]),
        ("Code converters", "Table of codes, unused codes as don't cares, one map per output.",
         ["4.18 (table)", "4.18 (x)", "4.7 (y)"], ["4.18 (w)", "4.18 (y)", "4.18 (z)", "4.7 (table)", "4.7 (x)", "4.7 (z)", "4.8*"]),
        ("Bigger converters", "Same method with more outputs.",
         ["4.10 (table)", "4.10 (y₂)"], ["4.10 (y₁)", "4.10 (y₃)", "4.9*"]),
        ("Half and full adders and subtractors", "Sum = XOR, carry/borrow from a 3-variable map.",
         ["4.12 (b · table)", "4.12 (b · B_out)"], ["4.12 (a)", "4.12 (b · Diff)", "3.29", "4.11*", "4.20*"]),
        ("Adder-subtractor and overflow", "M flips B and adds 1; V = C₄ ⊕ C₃.",
         ["4.13 (a)", "4.13 (c)"], ["4.13 (b)", "4.13 (d)", "4.13 (e)", "4.19"]),
        ("Carry lookahead", "Every carry from G, P and C₀ in two gate levels.",
         ["4.14", "4.15"], ["4.16", "4.17"]),
    ],
    "11": [
        ("Functions from a decoder", "Decoder gives every minterm; OR the ones you need.",
         ["4.28 (a)", "4.27"], ["4.28 (b)"]),
        ("Inside a decoder, and bigger decoders", "Gate-level decoders; enables build bigger ones.",
         ["4.23 (b)", "4.25"], ["4.23 (a)", "4.26"]),
        ("Decoder design with don't cares", "Unused input codes are free x's.",
         ["4.22 (table)", "4.22 (x)", "4.24 (D8)"], ["4.22 (w)", "4.22 (y)", "4.22 (z)", "4.24 (D0)", "4.24 (D1)", "4.24 (D2)",
                                                     "4.24 (D3)", "4.24 (D4)", "4.24 (D5)", "4.24 (D6)", "4.24 (D7)", "4.24 (D9)"]),
        ("Priority encoders", "Highest-priority 1 wins; V says any input is on.",
         ["4.29 (x)", "4.29 (y)", "4.30"], ["4.29 (V)"]),
    ],
    "12": [
        ("How a mux works", "Select lines pick which data input reaches the output.",
         ["4.3 (a)", "4.3 (b)"], ["4.31"]),
        ("Read a mux circuit", "Each data input covers two minterms.",
         ["4.34 (a)"], ["4.34 (b)"]),
        ("Any function on a mux", "Pair the rows: 0, 1, D or D' on each input.",
         ["4.32 (a)", "4.33"], ["4.32 (b)"]),
        ("One size smaller, plus gates", "Each data input becomes a small function of the leftover variables.",
         ["4.35 (a*"], ["4.35 (b*"]),
    ],
}


def norm(tag):
    return tag.replace("Mano ", "").replace(" ★", "").strip()


def match(key, tn):
    if key.endswith("*"):
        return tn.startswith(key[:-1])
    return tn == key or tn.startswith(key + " (") or tn.startswith(key + " ·")


def apply(tid, problems):
    """Annotate each question with grp (index) and core (bool). Returns the group list."""
    groups = GROUPS.get(tid)
    if not groups:
        return None
    qs = [q for p in problems for q in p["qs"]]
    seen = {}
    out = []
    for gi, (name, blurb, core, extra) in enumerate(groups):
        for keys, is_core in ((core, True), (extra, False)):
            for k in keys:
                hits = [q for q in qs if match(k, norm(q["tag"]))]
                assert hits, f"{tid}: key {k!r} matches nothing"
                for q in hits:
                    assert id(q) not in seen, f"{tid}: {q['tag']} is in two groups ({seen[id(q)]} and {name})"
                    seen[id(q)] = name
                    q["grp"] = gi
                    q["core"] = is_core
                    if is_core:
                        q["corder"] = len([x for x in qs if x.get("grp") == gi and x.get("core")])
        out.append({"name": name, "blurb": blurb})
    missing = [q["tag"] for q in qs if id(q) not in seen]
    assert not missing, f"{tid}: not grouped: {missing}"
    return out
