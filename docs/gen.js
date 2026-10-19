/* Fresh-number versions of the quiz questions.
   Each generator returns a normal question object (same format as docs/data/*.js)
   with a worked solution in `why`. A data question opts in with "gen": "<name>". */
(function () {
  "use strict";
  var G = {};

  /* ------------------------------------------------ small helpers */
  function ri(a, b) { return a + Math.floor(Math.random() * (b - a + 1)); }
  function pick(a) { return a[ri(0, a.length - 1)]; }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = ri(0, i), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function sample(lo, hi, k) { var a = []; for (var i = lo; i <= hi; i++) a.push(i); return shuffle(a).slice(0, k).sort(function (x, y) { return x - y; }); }
  function bin(n, w) { var s = n.toString(2); while (w && s.length < w) s = "0" + s; return s; }
  function strip0(s) { var t = s.replace(/^0+(?=.)/, ""); return t; }
  function bins(s) { return s === strip0(s) ? [s] : [s, strip0(s)]; }
  var SUBD = "₀₁₂₃₄₅₆₇₈₉";
  function sub(n) { return String(n).replace(/\d/g, function (d) { return SUBD[+d]; }); }
  function hexd(n) { return n.toString(16).toUpperCase(); }
  function letter(d) { return d >= 10 ? d + " → <b>" + hexd(d) + "</b>" : "<b>" + d + "</b>"; }
  function tbl(head, rows) {
    var h = "<table>";
    if (head) h += "<tr>" + head.map(function (c) { return "<th>" + c + "</th>"; }).join("") + "</tr>";
    rows.forEach(function (r) { h += "<tr>" + r.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; });
    return h + "</table>";
  }
  function p(s) { return "<p>" + s + "</p>"; }
  function list(a) { return a.join(", "); }
  function fracStr(num, den) { return String(num / den); } // den is a power of 2, so this is exact
  function lsb(n) { return n & -n; }

  /* ------------------------------------------------ number-system workings */
  function divLadder(n, base) {
    var rows = [], q = n;
    while (q > 0) { var r = q % base; rows.push([q + " ÷ " + base, Math.floor(q / base), base === 16 ? letter(r) : "<b>" + r + "</b>"]); q = Math.floor(q / base); }
    var digits = n === 0 ? "0" : n.toString(base).toUpperCase();
    return { html: tbl(["divide", "answer", "remainder"], rows) + p("Read the remainders <b>up</b>: <b>" + digits + "</b>"), digits: digits };
  }
  function mulLadder(num, den, base) {
    // fraction num/den, den a power of 2, terminates in base 2/8/16
    var rows = [], f = num, out = "";
    var guard = 0;
    while (f !== 0 && guard++ < 12) {
      var x = f * base, d = Math.floor(x / den);
      f = x - d * den;
      rows.push([fracStr(x / base, den) + " × " + base, fracStr(x, den), base === 16 ? letter(d) : "<b>" + d + "</b>"]);
      out += d.toString(base).toUpperCase();
    }
    return { html: tbl(["multiply", "result", "whole part"], rows) + p("Read the whole parts <b>down</b>: <b>." + out + "</b>"), digits: out };
  }
  function weightsTable(bitsWhole, bitsFrac) {
    var head = [], row1 = [], row2 = [], parts = [];
    for (var i = 0; i < bitsWhole.length; i++) {
      var w = Math.pow(2, bitsWhole.length - 1 - i);
      head.push(w); row1.push(bitsWhole[i]); row2.push(bitsWhole[i] === "1" ? "<b>" + w + "</b>" : "·");
      if (bitsWhole[i] === "1") parts.push(w);
    }
    if (bitsFrac) {
      head.push("."); row1.push("."); row2.push("");
      for (var j = 0; j < bitsFrac.length; j++) {
        var wf = Math.pow(2, -(j + 1));
        head.push(wf); row1.push(bitsFrac[j]); row2.push(bitsFrac[j] === "1" ? "<b>" + wf + "</b>" : "·");
        if (bitsFrac[j] === "1") parts.push(wf);
      }
    }
    return { html: tbl(head, [row1, row2]), parts: parts };
  }
  function groupBits(whole, frac, size) {
    var w = whole, f = frac || "";
    var padL = (size - w.length % size) % size, padR = f ? (size - f.length % size) % size : 0;
    var W = "0".repeat(padL) + w, F = f + "0".repeat(padR);
    var gw = [], gf = [];
    for (var i = 0; i < W.length; i += size) gw.push(W.slice(i, i + size));
    for (var j = 0; j < F.length; j += size) gf.push(F.slice(j, j + size));
    var conv = function (g) { return parseInt(g, 2).toString(16).toUpperCase(); };
    var hw = gw.map(conv).join(""), hf = gf.map(conv).join("");
    var show = function (gs, pad, left) {
      return gs.map(function (g, k) {
        var isPadded = left ? (k === 0 && pad) : (k === gs.length - 1 && pad);
        if (!isPadded) return "<code>" + g + "</code>";
        return left ? "<code><span class='pad'>" + g.slice(0, pad) + "</span>" + g.slice(pad) + "</code>"
                    : "<code>" + g.slice(0, size - pad) + "<span class='pad'>" + g.slice(size - pad) + "</span></code>";
      }).join(" ");
    };
    var rows = [gw.concat(gf.length ? ["."] : []).concat(gf).map(function (g) { return g === "." ? "." : "<code>" + g + "</code>"; }),
                gw.map(conv).concat(gf.length ? ["."] : []).concat(gf.map(conv)).map(function (d) { return "<b>" + d + "</b>"; })];
    var html = p("Group in " + size + "s outward from the point" + (padL || padR ? " (orange = padding zeros)" : "") + ": " +
      show(gw, padL, true) + (gf.length ? " . " + show(gf, padR, false) : "")) + tbl(null, rows);
    return { html: html, ans: hw + (hf ? "." + hf : "") };
  }

  /* ------------------------------------------------ Boolean minimiser (exact, ≤ 4 vars) */
  function cubeCovers(c, m) { return (m & c.mask) === c.val; }
  function primes(nv, on, dc) {
    var ok = {}; on.concat(dc).forEach(function (m) { ok[m] = 1; });
    var N = 1 << nv, cubes = [];
    for (var mask = 0; mask < N; mask++) for (var val = 0; val < N; val++) {
      if ((val & ~mask) !== 0) continue;
      var good = true, any = false;
      for (var m = 0; m < N; m++) if ((m & mask) === val) { if (!ok[m]) { good = false; break; } if (on.indexOf(m) >= 0) any = true; }
      if (good && any) cubes.push({ mask: mask, val: val });
    }
    return cubes.filter(function (c) {
      return !cubes.some(function (d) { return d !== c && (d.mask & c.mask) === d.mask && d.mask !== c.mask && (c.val & d.mask) === d.val; });
    });
  }
  function bits(x) { var c = 0; while (x) { c += x & 1; x >>= 1; } return c; }
  function minCover(nv, on, dc) {
    var P = primes(nv, on, dc), best = null;
    function cost(sel) { var l = 0; sel.forEach(function (c) { l += bits(c.mask); }); return [l, sel.length]; }
    function better(a, b) { return !b || a[0] < b[0] || (a[0] === b[0] && a[1] < b[1]); }
    function rec(left, sel) {
      var c = cost(sel);
      if (best && (c[0] > best.c[0] || (c[0] === best.c[0] && c[1] >= best.c[1]))) return;
      if (!left.length) { if (better(c, best && best.c)) best = { sel: sel.slice(), c: c }; return; }
      // branch on the uncovered minterm with the fewest covering primes
      var bm = null, opts = null;
      left.forEach(function (m) { var o = P.filter(function (q) { return cubeCovers(q, m); }); if (!opts || o.length < opts.length) { opts = o; bm = m; } });
      opts.forEach(function (q) {
        rec(left.filter(function (m) { return !cubeCovers(q, m); }), sel.concat([q]));
      });
    }
    rec(on.slice(), []);
    return best.sel;
  }
  function cubeCells(nv, c) { var a = []; for (var m = 0; m < (1 << nv); m++) if (cubeCovers(c, m)) a.push(m); return a; }
  function prodText(vars, c) {
    var nv = vars.length, s = "";
    for (var b = 0; b < nv; b++) { var bit = 1 << (nv - 1 - b); if (c.mask & bit) s += vars[b] + ((c.val & bit) ? "" : "'"); }
    return s || "1";
  }
  function sumText(vars, c) {
    var nv = vars.length, t = [];
    for (var b = 0; b < nv; b++) { var bit = 1 << (nv - 1 - b); if (c.mask & bit) t.push(vars[b] + ((c.val & bit) ? "'" : "")); }
    return "(" + t.join(" + ") + ")";
  }
  var GC = ["#0969da", "#1a7f37", "#cf222e", "#8250df", "#bc4c00", "#127a83"];
  function kmapHTML(vars, vals, groups) {
    // vals: m -> "1" | "0" | "x"; groups: [{cells:[..], name}]
    var nv = vars.length, rb = nv === 2 ? ["0", "1"] : ["00", "01", "11", "10"], cb = nv === 4 ? ["00", "01", "11", "10"] : ["0", "1"];
    var rv = nv === 2 ? 1 : 2;
    var h = "<table class='kshow'><tr><th>" + vars.slice(0, rv) + " \\ " + vars.slice(rv) + "</th>" + cb.map(function (c) { return "<th>" + c + "</th>"; }).join("") + "</tr>";
    rb.forEach(function (r) {
      h += "<tr><th>" + r + "</th>";
      cb.forEach(function (c) {
        var m = parseInt(r + c, 2), v = vals[m];
        var tags = groups.map(function (g, k) { return g.cells.indexOf(m) >= 0 ? "<i style='background:" + GC[k % GC.length] + "'>" + String.fromCharCode(97 + k) + "</i>" : ""; }).join("");
        h += "<td class='" + (v === "1" ? "one" : v === "x" ? "dc" : "zero") + "'><b>" + (v === "0" ? "0" : v) + "</b><span class='tags'>" + tags + "</span><small>" + m + "</small></td>";
      });
      h += "</tr>";
    });
    return h + "</table>";
  }
  function solveSOP(vars, on, dc, pos) {
    var nv = vars.length, N = 1 << nv, zeros = [];
    for (var m = 0; m < N; m++) if (on.indexOf(m) < 0 && dc.indexOf(m) < 0) zeros.push(m);
    var target = pos ? zeros : on;
    var cover = minCover(nv, target, dc);
    var vals = {}; for (var k = 0; k < N; k++) vals[k] = on.indexOf(k) >= 0 ? "1" : dc.indexOf(k) >= 0 ? "x" : "0";
    var groups = cover.map(function (c) { return { cells: cubeCells(nv, c), c: c }; });
    var terms = cover.map(function (c) { return pos ? sumText(vars, c) : prodText(vars, c); });
    var expr = pos ? terms.join("") : terms.join(" + ");
    var lits = 0; cover.forEach(function (c) { lits += bits(c.mask); });
    var lines = groups.map(function (g, k) {
      return "<span class='gtag' style='background:" + GC[k % GC.length] + "'>" + String.fromCharCode(97 + k) + "</span> cells " + list(g.cells) + " → <b>" + (pos ? sumText(vars, g.c) : prodText(vars, g.c)) + "</b>";
    });
    var why = kmapHTML(vars, vals, groups) +
      p((pos ? "Group the <b>0s</b>" : "Group the <b>1s</b>") + (dc.length ? " (use an x only if it makes a block bigger)" : "") + ", blocks as big as possible:") +
      "<p>" + lines.join("<br>") + "</p>" +
      p(pos ? "In each block, a letter that stays 0 goes in plain, one that stays 1 gets a bar." : "In each block, keep only the letters that don't change: 1 → plain, 0 → barred.") +
      p("F = <b>" + expr + "</b> (" + lits + " letters)");
    return { show: expr, lits: lits, why: why, vals: vals, nterms: cover.length };
  }
  function randFn(nv, lo, hi, ndc) {
    var N = 1 << nv;
    for (;;) {
      var k = ri(lo, hi), on = sample(0, N - 1, k);
      var rest = []; for (var m = 0; m < N; m++) if (on.indexOf(m) < 0) rest.push(m);
      var dc = ndc ? shuffle(rest).slice(0, ndc).sort(function (a, b) { return a - b; }) : [];
      if (on.length + dc.length >= N) continue;
      return { on: on, dc: dc };
    }
  }
  function randCube(nv, minL, maxL) {
    var L = ri(minL, maxL), idx = sample(0, nv - 1, L), mask = 0, val = 0;
    idx.forEach(function (b) { var bit = 1 << (nv - 1 - b); mask |= bit; if (Math.random() < 0.5) val |= bit; });
    return { mask: mask, val: val };
  }
  function onesOf(nv, cubes) { var s = {}; cubes.forEach(function (c) { cubeCells(nv, c).forEach(function (m) { s[m] = 1; }); }); return Object.keys(s).map(Number).sort(function (a, b) { return a - b; }); }
  function sigma(a) { return "Σm(" + list(a) + ")"; }
  function vlist(vars) { return vars.split("").join(", "); }

  /* ================================================ 01 */
  G.moore = function () {
    var n = ri(1, 9), y = pick([4, 6, 8, 10, 12]), d = y / 2, ans = n * Math.pow(2, d);
    return { type: "text", q: "A chip has " + n + " million transistors. Doubling every 2 years, about how many million will it have after " + y + " years?", ph: "millions",
      ans: [String(ans), ans + " million", ans + "m"],
      why: p(y + " ÷ 2 = <b>" + d + " doublings</b>.") + p(n + " × 2<sup>" + d + "</sup> = " + n + " × " + Math.pow(2, d) + " = <b>" + ans + " million</b>.") };
  };

  /* ================================================ 02 */
  G.b2d = function (o) {
    var w = ri(4, 6), f = o.frac != null ? o.frac : ri(1, 3);
    var whole = "1" + bin(ri(0, (1 << (w - 1)) - 1), w - 1), frac = f ? bin(ri(0, (1 << f) - 1) | 1, f) : "";
    var wt = weightsTable(whole, frac), val = wt.parts.reduce(function (a, b) { return a + b; }, 0);
    return { type: "text", q: "Convert <code>" + whole + (frac ? "." + frac : "") + "₂</code> to decimal.", ans: [String(val)],
      why: p("Write the place values over the bits, then add the ones under every 1:") + wt.html + p(wt.parts.join(" + ") + " = <b>" + val + "</b>") };
  };
  G.h2d = function () {
    var n = ri(26, 255), h = hexd(n), a = n >> 4, b = n & 15;
    return { type: "text", q: "Convert <code>" + h + "₁₆</code> to decimal.", ans: [String(n)],
      why: p("Place values are 16 and 1. " + (a >= 10 || b >= 10 ? "Letters first: A=10 B=11 C=12 D=13 E=14 F=15." : "")) +
        tbl(["16", "1"], [[h[0] + (a >= 10 ? " = " + a : ""), h[1] + (b >= 10 ? " = " + b : "")]]) +
        p(a + " × 16 + " + b + " = " + a * 16 + " + " + b + " = <b>" + n + "</b>") };
  };
  G.o2d = function () {
    var n = ri(65, 511), s = n.toString(8), d = s.split("").map(Number);
    return { type: "text", q: "Convert <code>" + s + "₈</code> to decimal.", ans: [String(n)],
      why: p("Place values are 64, 8, 1.") + tbl(["64", "8", "1"], [d]) +
        p(d[0] + " × 64 + " + d[1] + " × 8 + " + d[2] + " = " + d[0] * 64 + " + " + d[1] * 8 + " + " + d[2] + " = <b>" + n + "</b>") };
  };
  G.d2b = function () {
    var n = ri(13, 63), L = divLadder(n, 2);
    return { type: "text", q: "Convert <b>" + n + "</b> to binary.", ans: [L.digits],
      why: L.html + p("Check: " + weightsTable(L.digits).parts.join(" + ") + " = " + n + " ✓") };
  };
  G.f2b = function () {
    var f = ri(3, 5), den = 1 << f, num = ri(1, den / 2 - 1) * 2 + 1, M = mulLadder(num, den, 2);
    var v = fracStr(num, den);
    return { type: "text", q: "Convert <b>" + v + "</b> to binary.", ans: ["0." + M.digits, "." + M.digits],
      why: M.html + p("So " + v + " = <b>0." + M.digits + "₂</b>. Check: " + weightsTable("0", M.digits).parts.join(" + ") + " = " + v + " ✓") };
  };
  G.d2h = function () {
    var n = ri(100, 999), L = divLadder(n, 16);
    return { type: "text", q: "Convert <b>" + n + "</b> to hex.", ans: [L.digits],
      why: p("Divide by 16. Any remainder from 10 to 15 becomes a letter.") + L.html };
  };
  G.d2o = function () {
    var w = ri(20, 200), f = pick([3, 6]), den = 1 << f, num = ri(1, den - 1);
    if (f === 6 && num % 8 === 0) num += 1;
    var L = divLadder(w, 8), M = mulLadder(num, den, 8), v = w + num / den;
    return { type: "text", q: "Convert <b>" + v + "</b> to octal.", ans: [L.digits + "." + M.digits],
      why: p("Whole part " + w + ", divide by 8:") + L.html + p("Fraction " + fracStr(num, den) + ", multiply by 8:") + M.html +
        p("Join them: <b>" + L.digits + "." + M.digits + "₈</b>") };
  };
  G.b2h = function (o) {
    var wl = ri(5, 10), whole = "1" + bin(ri(0, (1 << (wl - 1)) - 1), wl - 1);
    var fl = o.nofrac ? 0 : ri(1, 5), frac = fl ? bin(ri(0, (1 << fl) - 1) | 1, fl) : "";
    var g = groupBits(whole, frac, 4);
    return { type: "text", q: "Convert <code>" + whole + (frac ? "." + frac : "") + "₂</code> to hex.", ans: [g.ans],
      why: g.html + p("Answer: <b>" + g.ans + "₁₆</b>" + (frac ? ". The fraction pads on the <b>right</b>." : "")) };
  };
  G.b2o = function () {
    var wl = ri(9, 14), whole = "1" + bin(ri(0, (1 << (wl - 1)) - 1), wl - 1), g = groupBits(whole, "", 3);
    return { type: "text", q: "Convert <code>" + whole + "₂</code> to octal.", ans: [g.ans],
      why: g.html + p("Answer: <b>" + g.ans + "₈</b>") };
  };
  G.h2o = function () {
    var n = ri(16, 255), h = hexd(n), b = h.split("").map(function (d) { return bin(parseInt(d, 16), 4); });
    var g = groupBits(strip0(b.join("")), "", 3);
    return { type: "text", q: "Convert <code>" + h + "₁₆</code> to octal.", ans: [g.ans],
      why: p("Go through binary. Each hex digit is 4 bits: " + h.split("").map(function (d, i) { return d + " = <code>" + b[i] + "</code>"; }).join(", ") + ".") +
        g.html + p("Answer: <b>" + g.ans + "₈</b> (check: both are " + n + ")") };
  };
  G.h2b = function () {
    var n = ri(16, 255), h = hexd(n), b = h.split("").map(function (d) { return bin(parseInt(d, 16), 4); });
    var s = bin(n, 8);
    return { type: "text", q: "A memory dump shows <code>" + h + "₁₆</code>. Write it as 8 bits.", ans: [s],
      why: p("Each hex digit is exactly 4 bits (build it from 8 4 2 1):") +
        tbl(null, [h.split(""), b.map(function (x) { return "<code>" + x + "</code>"; })]) + p("Answer: <b>" + s + "</b>") };
  };
  G.d2bh = function () {
    var w = ri(40, 250), den = 32, num = ri(1, 15) * 2 + 1, v = w + num / den;
    var L = divLadder(w, 2), M = mulLadder(num, den, 2), g = groupBits(L.digits, M.digits, 4);
    var b = L.digits + "." + M.digits;
    return { type: "multi", q: "Convert <b>" + v + "</b>.", fields: [{ label: "binary", ans: [b] }, { label: "hex", ans: [g.ans] }],
      why: p("Whole part " + w + ", divide by 2:") + L.html + p("Fraction " + fracStr(num, den) + ", multiply by 2:") + M.html +
        p("Binary: <b>" + b + "</b>") + p("Now hex by grouping:") + g.html + p("Hex: <b>" + g.ans + "</b>") };
  };

  /* ================================================ 03 */
  function colAdd(a, b, w) {
    var A = bin(a, w), B = bin(b, w), c = 0, into = [], sum = "";
    for (var i = w - 1; i >= 0; i--) { into[i] = c; var t = +A[i] + +B[i] + c; sum = (t & 1) + sum; c = t >> 1; }
    var crow = [c ? "<small>1</small>" : ""];
    for (var k = 0; k < w; k++) crow.push(into[k] ? "<small>1</small>" : "");
    var lead = function (x) { return [x]; };
    return { html: tbl(null, [["carry"].concat(crow), [""].concat(lead(""), A.split("")), ["+"].concat(lead(""), B.split("")),
      ["="].concat([c ? "<b>1</b>" : ""], sum.split("").map(function (x) { return "<b>" + x + "</b>"; }))]), out: (c ? "1" : "") + sum };
  }
  G.badd = function (o) {
    var w = o.bits || ri(4, 6), a = ri(1 << (w - 1), (1 << w) - 1), b = ri(1, (1 << w) - 1), r = colAdd(a, b, w);
    return { type: "text", q: bin(a, w) + " + " + bin(b, w) + " = ?", ans: bins(r.out),
      why: p("Add column by column from the right. 1 + 1 = 10 (write 0, carry 1). 1 + 1 + 1 = 11 (write 1, carry 1). Small 1s are carries:") + r.html +
        p("Answer <b>" + strip0(r.out) + "</b>. Check: " + a + " + " + b + " = " + (a + b) + " ✓") };
  };
  G.bsub = function (o) {
    var w = o.bits || ri(4, 5), a = ri(1 << (w - 1), (1 << w) - 1), b = ri(1, a - 1), A = bin(a, w), B = bin(b, w), out = bin(a - b, w);
    var borrow = [], bo = 0, steps = [];
    for (var i = w - 1; i >= 0; i--) {
      var d = +A[i] - +B[i] - bo;
      steps.push("column " + (w - 1 - i) + ": " + A[i] + " − " + B[i] + (bo ? " − 1 (borrowed)" : "") + " = " + (d < 0 ? d + 2 + ", borrow 1" : d));
      bo = d < 0 ? 1 : 0;
    }
    return { type: "text", q: A + " − " + B + " = ? (give " + w + " bits)", ans: bins(out),
      why: p("Work from the right. 0 − 1 = 1, borrow 1 from the next column.") + p(steps.join("<br>")) +
        tbl(null, [[""].concat(A.split("")), ["−"].concat(B.split("")), [""].concat(out.split("").map(function (x) { return "<b>" + x + "</b>"; }))]) +
        p("Check: " + a + " − " + b + " = " + (a - b) + " ✓") };
  };
  G.bmul = function () {
    var a = ri(5, 15), b = ri(5, 7), A = bin(a), B = bin(b), n = (a * b).toString(2), W = n.length, rows = [];
    var cells = function (str) { var c = []; for (var i = 0; i < W - str.length; i++) c.push(""); return c.concat(str.split("")); };
    for (var i = B.length - 1; i >= 0; i--) {
      var sh = B.length - 1 - i, pp = B[i] === "1" ? A + "0".repeat(sh) : "0".repeat(A.length + sh);
      rows.push(["bit " + B[i] + (sh ? ", shift " + sh : "")].concat(cells(pp)));
    }
    rows.push(["add"].concat(cells(n).map(function (x) { return x ? "<b>" + x + "</b>" : ""; })));
    return { type: "text", q: A + " × " + B + " = ?", ans: [n],
      why: p("Shift and add. Go through the bits of " + B + " from the right: a 1 copies " + A + ", a 0 gives 0s. Shift one place left each time.") +
        tbl(null, rows) + p("Answer <b>" + n + "</b>. Check: " + a + " × " + b + " = " + a * b + " ✓") };
  };
  G.bdiv = function () {
    var d = ri(3, 13), q = ri(5, 15), r = ri(0, d - 1), n = d * q + r, N = bin(n), D = bin(d), steps = [], cur = 0, qs = "";
    for (var i = 0; i < N.length; i++) {
      cur = cur * 2 + +N[i];
      var fits = cur >= d;
      if (qs || fits) steps.push([bin(cur), fits ? "yes → <b>1</b>, subtract " + D : "no → <b>0</b>"]);
      if (fits) { qs += "1"; cur -= d; } else if (qs) qs += "0";
    }
    return { type: "multi", q: "<code>" + N + " ÷ " + D + "</code>", fields: [{ label: "quotient", ans: bins(q.toString(2)) }, { label: "remainder", ans: bins(bin(r)) }],
      why: p("Bring down one bit at a time. Each step asks only: does " + D + " fit?") + tbl(["so far", "does " + D + " fit?"], steps) +
        p("Quotient <b>" + q.toString(2) + "</b>, remainder <b>" + bin(r) + "</b>. Check: " + n + " ÷ " + d + " = " + q + " r " + r + " ✓") };
  };

  /* ================================================ 04 */
  function flip(s) { return s.replace(/[01]/g, function (c) { return c === "0" ? "1" : "0"; }); }
  function twos(s) { var w = s.length; return bin(((1 << w) - parseInt(s, 2)) & ((1 << w) - 1), w); }
  function tcVal(s) { var v = parseInt(s, 2); return s[0] === "1" ? v - (1 << s.length) : v; }
  function sgn(n) { return n < 0 ? "−" + -n : String(n); }
  function sgnAns(n) { return n < 0 ? ["-" + -n, "−" + -n] : [String(n), "+" + n]; }
  G.neg3 = function () {
    var n = ri(1, 7), pz = bin(n, 4), sm = "1" + pz.slice(1), oc = flip(pz), tc = twos(pz);
    return { type: "multi", q: "Write <b>−" + n + "</b> in 4 bits in each system.", fields: [{ label: "signed mag", ans: [sm] }, { label: "1's comp", ans: [oc] }, { label: "2's comp", ans: [tc] }],
      why: p("Start from +" + n + " = <code>" + pz + "</code>.") + tbl(["system", "rule", "−" + n], [["signed mag", "set the sign bit", "<b>" + sm + "</b>"], ["1's comp", "flip every bit", "<b>" + oc + "</b>"], ["2's comp", "flip every bit, then +1", "<b>" + tc + "</b>"]]) };
  };
  G.twos8 = function () {
    var n = ri(1, 254); if (n === 128) n = 100;
    var s = bin(n, 8), t = twos(s), k = s.lastIndexOf("1");
    return { type: "text", q: "2's complement of <code>" + s + "</code>.", ans: [t],
      why: p("Shortcut: from the right, copy up to and including the first 1, then flip everything to its left.") +
        tbl(["", "flip", "copy"], [["in", "<code>" + s.slice(0, k) + "</code>", "<code>" + s.slice(k) + "</code>"], ["out", "<code><b>" + t.slice(0, k) + "</b></code>", "<code><b>" + t.slice(k) + "</b></code>"]]) +
        p("Answer <b>" + t + "</b>. (Long way: flip all → " + flip(s) + ", +1 → " + t + " ✓)") };
  };
  G.neg8 = function () {
    var n = ri(3, 127), pz = bin(n, 8), f = flip(pz), t = twos(pz);
    return { type: "text", q: "Write <b>−" + n + "</b> in 8-bit 2's complement.", ans: [t],
      why: tbl(["step", "bits"], [["+" + n, "<code>" + pz + "</code>"], ["flip all", "<code>" + f + "</code>"], ["+1", "<code><b>" + t + "</b></code>"]]) +
        p("Check: −128 + " + (256 - n - 128) + " = −" + n + " ✓") };
  };
  G.read6 = function () {
    var s = "1" + bin(ri(0, 30), 5), f = flip(s), t = twos(s), v1 = parseInt(f, 2), v2 = parseInt(t, 2);
    return { type: "multi", q: "Read <code>" + s + "</code> as…", fields: [{ label: "1's comp", ans: sgnAns(-v1) }, { label: "2's comp", ans: sgnAns(-v2) }],
      why: p("The left bit is 1, so it's negative in both. Undo the system to find its size:") +
        tbl(["system", "undo", "size", "value"], [["1's comp", "flip → " + f, v1, "<b>−" + v1 + "</b>"], ["2's comp", "flip, +1 → " + t, v2, "<b>−" + v2 + "</b>"]]) };
  };
  G.read4 = function () {
    var v = ri(-8, 7); if (v === 0) v = -5;
    var s = bin(v & 15, 4);
    var why = v >= 0 ? p("Left bit 0 → positive. " + s + " = <b>" + v + "</b>.")
      : p("Left bit 1 → negative. The sign bit is worth <b>−8</b>, the rest as normal:") + tbl(["−8", "4", "2", "1"], [s.split("")]) +
        p("−8 + " + (v + 8) + " = <b>" + v + "</b>");
    return { type: "text", q: "What is <code>" + s + "</code> in 4-bit 2's complement?", ans: sgnAns(v), why: why };
  };
  G.ones_add = function () {
    var a = ri(1, 7), b = ri(1, 7); while (b === a) b = ri(1, 7);
    var A = flip(bin(a, 4)), B = bin(b, 4), raw = parseInt(A, 2) + parseInt(B, 2), c = raw >> 4, low = raw & 15, res = bin((low + c) & 15, 4);
    var v = b - a;
    return { type: "text", q: "Add −" + a + " + " + b + " in 4-bit <b>1's complement</b>. Give the final 4-bit result.", ans: [res],
      why: p("−" + a + " = flip " + bin(a, 4) + " = <code>" + A + "</code>. +" + b + " = <code>" + B + "</code>.") +
        p(A + " + " + B + " = " + (c ? "<b>1</b> " : "") + bin(low, 4) + ".") +
        p(c ? "Carry out of the left → <b>end-around carry</b>: add it back on. " + bin(low, 4) + " + 1 = <b>" + res + "</b>." : "No carry out, so the answer is <b>" + res + "</b>.") +
        p("Check: −" + a + " + " + b + " = " + sgn(v) + " ✓") };
  };
  G.twos_sub = function () {
    var a = ri(1, 7), b = ri(1, 7), B = twos(bin(b, 4)), raw = a + parseInt(B, 2), res = bin(raw & 15, 4);
    return { type: "text", q: "Work out " + a + " − " + b + " in 4-bit 2's complement (add " + a + " and −" + b + "). Give the 4-bit result.", ans: [res],
      why: p("−" + b + ": flip " + bin(b, 4) + " and +1 → <code>" + B + "</code>.") +
        p(bin(a, 4) + " + " + B + " = " + (raw > 15 ? "<b>1</b> " : "") + res + (raw > 15 ? ". Drop the carry." : ".")) +
        p("Answer <b>" + res + "</b> = " + sgn(a - b) + " ✓") };
  };
  G.overflow = function () {
    var a = ri(-8, 7), b = ri(-8, 7), A = bin(a & 15, 4), B = bin(b & 15, 4), s = a + b, res = bin(s & 15, 4), of = s > 7 || s < -8;
    var same = (a < 0) === (b < 0);
    return { type: "multi", q: "4-bit 2's complement: <code>" + A + " + " + B + "</code> (" + sgn(a) + " + " + sgn(b) + ").",
      fields: [{ label: "4-bit result", ans: [res] }, { label: "overflow? (yes/no)", ans: of ? ["yes", "y"] : ["no", "n"] }],
      why: p(A + " + " + B + " → keep 4 bits: <b>" + res + "</b> (reads as " + sgn(tcVal(res)) + ").") +
        p(!same ? "Different signs in → it can <b>never</b> overflow." :
          of ? "Two " + (a < 0 ? "negatives" : "positives") + " gave a " + (a < 0 ? "positive" : "negative") + ": <b>overflow</b>. " + sgn(s) + " is outside −8 … +7."
             : "Same signs in, same sign out → <b>no overflow</b>. " + sgn(s) + " fits in −8 … +7.") };
  };

  /* ================================================ 05 */
  G.bitsfor = function () {
    var n = ri(5, 300), k = Math.ceil(Math.log2(n));
    if (Math.pow(2, k) < n) k++;
    return { type: "text", q: "What is the fewest bits you need to give each of " + n + " items its own code?", ans: [String(k)],
      why: p("Find the first power of 2 that is ≥ " + n + ":") + p("2<sup>" + (k - 1) + "</sup> = " + Math.pow(2, k - 1) + " is too few, 2<sup>" + k + "</sup> = " + Math.pow(2, k) + " is enough. <b>" + k + "</b> bits.") };
  };
  G.bcd = function (o) {
    var dg = o.digits || ri(2, 3), n = ri(Math.pow(10, dg - 1), Math.pow(10, dg) - 1), s = String(n), nib = s.split("").map(function (d) { return bin(+d, 4); });
    return { type: "text", q: "Write " + n + " in BCD (" + dg * 4 + " bits).", ans: [nib.join("")],
      why: p("BCD: each decimal digit becomes its own 4 bits.") + tbl(null, [s.split(""), nib.map(function (x) { return "<code>" + x + "</code>"; })]) + p("Answer <b>" + nib.join(" ") + "</b>") };
  };
  G.bcdvalid = function () {
    var bad = Math.random() < 0.5, d1 = ri(0, 9), d2 = bad ? ri(10, 15) : ri(0, 9);
    var ns = Math.random() < 0.5 ? [d1, d2] : [d2, d1], s = ns.map(function (d) { return bin(d, 4); }).join(" ");
    return { type: "tf", q: "<code>" + s + "</code> is valid BCD.", a: bad ? 1 : 0,
      why: p(bad ? "<b>False.</b> " + bin(d2, 4) + " = " + d2 + ", and BCD only uses 0000 to 1001 (0 to 9)." : "<b>True.</b> " + ns.map(function (d) { return bin(d, 4) + " = " + d; }).join(", ") + ". Both are 0 to 9.") };
  };
  G.bcd2d = function () {
    var n = ri(10, 999), s = String(n), nib = s.split("").map(function (d) { return bin(+d, 4); });
    return { type: "text", q: "BCD <code>" + nib.join(" ") + "</code> is which decimal number?", ans: [s],
      why: p("Read each group of 4 as one digit:") + tbl(null, [nib.map(function (x) { return "<code>" + x + "</code>"; }), s.split("")]) + p("<b>" + s + "</b>") };
  };
  G.b2gray = function () {
    var n = ri(1, 15), b = bin(n, 4), g = b[0], steps = ["keep the first bit: <b>" + b[0] + "</b>"];
    for (var i = 1; i < 4; i++) { var x = +b[i - 1] ^ +b[i]; g += x; steps.push(b[i - 1] + " ⊕ " + b[i] + " = <b>" + x + "</b>"); }
    return { type: "text", q: "Convert binary <code>" + b + "</code> to Gray code.", ans: [g],
      why: p("Keep the first bit. Then each Gray bit = this binary bit ⊕ the one to its left (1 if they differ).") + p(steps.join("<br>")) + p("Gray: <b>" + g + "</b>") };
  };
  G.graynext = function () {
    var n = ri(1, 14), gr = function (k) { return bin(k ^ (k >> 1), 4); }, a = gr(n), b = gr(n + 1);
    var diff = []; for (var i = 0; i < 4; i++) if (a[i] !== b[i]) diff.push(i);
    return { type: "text", q: "Gray code for <b>" + n + "</b> is <code>" + a + "</code>. What is the Gray code for <b>" + (n + 1) + "</b>?", ans: [b],
      why: p("Convert " + (n + 1) + " = <code>" + bin(n + 1, 4) + "</code> to Gray: keep the first bit, then ⊕ neighbours → <b>" + b + "</b>.") +
        p("Check: " + a + " → " + b + " changes only one bit ✓") };
  };
  G.onehot = function () {
    var k = ri(1, 8), s = bin(1 << (k - 1), 8);
    return { type: "text", q: "Write <b>" + k + "</b> in 8-bit one-hot.", ans: [s],
      why: p("Value " + k + " → bit position " + (k - 1) + " (counting from the right, starting at 0) → <b>" + s + "</b>.") };
  };

  /* ================================================ 06 */
  function Q() { return window.QUIZ; }
  function ttOf(expr, vars) { return Q().truth(Q().parseBool(expr, vars).tree, vars.length); }
  function inside(a, b) { return (b.mask & a.mask) === b.mask && (a.val & b.mask) === b.val; } // cube a sits inside cube b
  function randSOP(vars, nTerms, minL, maxL, clean) {
    var nv = vars.length, cubes = [], seen = {};
    while (cubes.length < nTerms) {
      var c = randCube(nv, minL, maxL), k = c.mask + ":" + c.val;
      if (seen[k]) continue;
      if (clean && cubes.some(function (d) { return inside(c, d) || inside(d, c); })) continue;
      seen[k] = 1; cubes.push(c);
    }
    return { cubes: cubes, terms: cubes.map(function (c) { return prodText(vars, c); }) };
  }
  function randPOS(vars, nTerms, minL, maxL) {
    var nv = vars.length, cubes = [], seen = {};
    while (cubes.length < nTerms) { var c = randCube(nv, minL, maxL), k = c.mask + ":" + c.val; if (!seen[k]) { seen[k] = 1; cubes.push(c); } }
    // a sum term is 0 exactly on the cells of the cube whose literals are its complements
    return { cubes: cubes, terms: cubes.map(function (c) { return sumText(vars, c); }) };
  }
  G.ttrows = function () {
    var n = ri(2, 9);
    return { type: "text", q: "How many rows does a truth table with " + n + " inputs have?", ans: [String(Math.pow(2, n))],
      why: p("Each input doubles the rows: 2<sup>" + n + "</sup> = <b>" + Math.pow(2, n) + "</b>.") };
  };
  G.evalb = function () {
    var T = pick([["(x + y)'", ["x + y"]], ["(xy)'", ["xy"]], ["x'y + z", ["x'y", "z"]], ["xy' + y'z", ["xy'", "y'z"]], ["(x + y')z", ["x + y'", "z"]],
      ["x'z' + yz", ["x'z'", "yz"]], ["(x + z)(y' + z')", ["x + z", "y' + z'"]], ["(xz)' + y", ["xz", "y"]], ["(x + y + z)'", ["x + y + z"]], ["x ⊕ y ⊕ z", []]]);
    var v = [ri(0, 1), ri(0, 1), ri(0, 1)], row = (v[0] << 2) | (v[1] << 1) | v[2], expr = T[0].replace(/⊕/g, "^");
    var out = ttOf(expr, "xyz")[row];
    var parts = T[1].map(function (e) { return [e, ttOf(e, "xyz")[row]]; });
    return { type: "text", q: "x = " + v[0] + ", y = " + v[1] + ", z = " + v[2] + ". What is <code>" + T[0] + "</code>?", ans: [String(out)], ph: "0 or 1",
      why: p("Put the values in. A bar flips 0 ↔ 1. AND is 1 only if all are 1. OR is 1 if any is 1.") +
        (parts.length ? tbl(["piece", "value"], parts.map(function (r) { return ["<code>" + r[0] + "</code>", r[1]]; })) : p("XOR of three bits = 1 when an odd number of them are 1.")) +
        p("<code>" + T[0] + "</code> = <b>" + out + "</b>") };
  };
  G.ttexpr = function () {
    var vars = "xyz", s = randSOP(vars, ri(2, 3), 2, 2, true), f = s.terms.join(" + "), cols = s.terms.map(function (t) { return ttOf(t, vars); }), out = ttOf(f, vars);
    var rows = [];
    for (var m = 0; m < 8; m++) rows.push(bin(m, 3).split("").concat(cols.map(function (c) { return c[m]; }), ["<b>" + out[m] + "</b>"]));
    return { type: "tt", q: "Fill the truth table for <code>f = " + f + "</code>.", vars: vars, outs: { f: out },
      why: p("Work out each term on its own, then OR them: f is 1 on any row where at least one term is 1.") +
        tbl(["x", "y", "z"].concat(s.terms, ["f"]), rows) };
  };

  /* ================================================ 07 */
  G.minterm = function () {
    var k = ri(0, 7), b = bin(k, 3), c = { mask: 7, val: k }, t = prodText("xyz", c);
    return { type: "bool", q: "f(x, y, z). Write the minterm <b>m" + sub(k) + "</b>.", vars: "xyz", ones: [k], show: t, form: "sop", lits: 3,
      why: p(k + " = <code>" + b + "</code>. Minterm: 1 → plain letter, 0 → barred. AND them: <b>" + t + "</b>.") + p("It is 1 on row " + k + " only.") };
  };
  G.maxterm = function () {
    var k = ri(0, 7), b = bin(k, 3), ones = []; for (var m = 0; m < 8; m++) if (m !== k) ones.push(m);
    var t = sumText("xyz", { mask: 7, val: k });
    return { type: "bool", q: "f(x, y, z). Write the maxterm <b>M" + sub(k) + "</b>.", vars: "xyz", ones: ones, show: t, form: "pos", lits: 3,
      why: p(k + " = <code>" + b + "</code>. Maxterm is the opposite rule: 0 → plain letter, 1 → barred. OR them: <b>" + t + "</b>.") + p("It is 0 on row " + k + " only.") };
  };
  G.rows2sigma = function () {
    var on = sample(0, 7, ri(2, 4));
    return { type: "text", q: "f(x, y, z) is 1 on rows " + list(on) + " only. Write it as Σm( … ). Type just the numbers.", prefix: "Σm(", ans: [on.join(",")],
      why: p("Σm just lists the rows where f = 1: <b>" + sigma(on) + "</b>.") + p("= " + on.map(function (m) { return prodText("xyz", { mask: 7, val: m }); }).join(" + ")) };
  };
  function zerosOf(on, N) { var z = []; for (var m = 0; m < N; m++) if (on.indexOf(m) < 0) z.push(m); return z; }
  G.sig2pi = function () {
    var on = sample(0, 7, ri(3, 5)), z = zerosOf(on, 8);
    return { type: "text", q: "f(x, y, z) = " + sigma(on) + ". Write f as ΠM( … ).", prefix: "ΠM(", ans: [z.join(",")],
      why: p("ΠM lists the rows where f = <b>0</b>: every number from 0 to 7 that is <i>not</i> in the Σm list.") + p("<b>ΠM(" + list(z) + ")</b>") };
  };
  G.compl = function () {
    var on = sample(0, 7, ri(3, 5)), z = zerosOf(on, 8);
    return { type: "text", q: "f(x, y, z) = " + sigma(on) + ". Write the complement f' as Σm( … ).", prefix: "Σm(", ans: [z.join(",")],
      why: p("f' is 1 exactly where f is 0: the numbers missing from the list.") + p("f' = <b>" + sigma(z) + "</b> (same numbers as f's ΠM list).") };
  };
  G.expr2sigma = function () {
    var vars = "ABC", s = randSOP(vars, 2, 1, 2, true), on = onesOf(3, s.cubes);
    if (on.length === 8) return G.expr2sigma();
    return { type: "text", q: "f(A, B, C) = " + s.terms.join(" + ") + ". Write f as Σm( … ).", prefix: "Σm(", ans: [on.join(",")],
      why: p("Each term is 1 on the rows where its letters match (plain = 1, barred = 0). Missing letters can be anything.") +
        tbl(["term", "rows"], s.cubes.map(function (c, i) { return ["<code>" + s.terms[i] + "</code>", list(cubeCells(3, c))]; })) +
        p("Together (no repeats): <b>" + sigma(on) + "</b>") };
  };
  G.picount = function () {
    var z = sample(0, 15, ri(3, 7));
    return { type: "text", q: "f(A, B, C, D) = ΠM(" + list(z) + "). How many numbers are in its Σm list?", ans: [String(16 - z.length)],
      why: p("4 variables → 16 rows. ΠM lists the " + z.length + " zero rows, Σm lists the rest: 16 − " + z.length + " = <b>" + (16 - z.length) + "</b>.") };
  };
  G.ttpi = function () {
    var z = sample(0, 7, ri(2, 4)), out = []; for (var m = 0; m < 8; m++) out.push(z.indexOf(m) >= 0 ? 0 : 1);
    return { type: "tt", q: "Fill f for <code>f = ΠM(" + list(z) + ")</code>.", vars: "xyz", outs: { f: out },
      why: p("ΠM lists the rows where f = <b>0</b>: rows " + list(z) + ". Every other row is 1.") };
  };

  /* ================================================ 08 / 09 */
  function mapWhy(vars, on, dc) {
    var N = 1 << vars.length, vals = {}; for (var m = 0; m < N; m++) vals[m] = on.indexOf(m) >= 0 ? "1" : dc.indexOf(m) >= 0 ? "x" : "0";
    return kmapHTML(vars, vals, []) + p("Rows and columns go 00, 01, <b>11, 10</b> (not 10 then 11). The small number in each cell is its minterm.");
  }
  G.kmapfill = function (o) {
    var nv = o.nv || 3, vars = "ABCD".slice(0, nv), f = randFn(nv, nv === 3 ? 3 : 5, nv === 3 ? 5 : 9, o.dc ? ri(1, 2) : 0);
    return { type: "kmap", q: "Fill the map for <code>F = " + sigma(f.on) + (f.dc.length ? " + d(" + list(f.dc) + ")" : "") + "</code>." + (f.dc.length ? " Click a cell twice for x." : ""),
      vars: vars, ones: f.on, dc: f.dc.length ? f.dc : undefined, why: mapWhy(vars, f.on, f.dc) };
  };
  G.kmapexpr = function (o) {
    var nv = o.nv || 3, vars = "ABCD".slice(0, nv), s = randSOP(vars, ri(3, 4), 1, nv - 1), on = onesOf(nv, s.cubes);
    if (on.length >= (1 << nv) - 1) return G.kmapexpr(o);
    return { type: "kmap", q: "Fill the map straight from <code>F = " + s.terms.join(" + ") + "</code>.", vars: vars, ones: on,
      why: p("Each term fills the cells where its letters match (plain = 1, barred = 0):") +
        tbl(["term", "cells"], s.cubes.map(function (c, i) { return ["<code>" + s.terms[i] + "</code>", list(cubeCells(nv, c))]; })) + mapWhy(vars, on, []) };
  };
  G.kmappos = function (o) {
    var nv = o.nv || 4, vars = "ABCD".slice(0, nv), s = randPOS(vars, ri(3, 4), 2, nv), zs = onesOf(nv, s.cubes), on = zerosOf(zs, 1 << nv);
    if (on.length < 2) return G.kmappos(o);
    return { type: "kmap", q: "Fill the map for <code>F = " + s.terms.join("") + "</code>. (Each bracket puts 0s where all its letters are false.)", vars: vars, ones: on,
      why: p("A bracket is 0 only when every letter in it is 0. Plain letter → that variable is 0; barred letter → that variable is 1:") +
        tbl(["bracket", "0s at"], s.cubes.map(function (c, i) { return ["<code>" + s.terms[i] + "</code>", list(cubeCells(nv, c))]; })) + mapWhy(vars, on, []) };
  };
  function interesting(sol) { return sol.nterms >= 2 && sol.lits >= 3; }
  G.minsop = function (o) {
    var nv = o.nv || 3, vars = "ABCD".slice(0, nv), pos = !!o.pos;
    for (var tries = 0; tries < 50; tries++) {
      var f = randFn(nv, nv === 3 ? 3 : 5, nv === 3 ? 5 : 10, o.dc ? ri(1, nv === 3 ? 2 : 3) : 0), sol = solveSOP(vars, f.on, f.dc, pos);
      if (interesting(sol)) break;
    }
    return { type: "bool", q: "Minimum <b>" + (pos ? "POS" : "SOP") + "</b> for <code>F(" + vlist(vars) + ") = " + sigma(f.on) + (f.dc.length ? " + d(" + list(f.dc) + ")" : "") + "</code>.",
      vars: vars, ones: f.on, dc: f.dc.length ? f.dc : undefined, show: sol.show, form: pos ? "pos" : "sop", lits: sol.lits, why: sol.why };
  };
  G.minexpr = function (o) {
    var nv = o.nv || 4, vars = "ABCD".slice(0, nv), pos = !!o.pos;
    for (var tries = 0; tries < 50; tries++) {
      var s = randSOP(vars, ri(3, 4), 1, nv), on = onesOf(nv, s.cubes);
      if (on.length < 2 || on.length > (1 << nv) - 2) continue;
      var sol = solveSOP(vars, on, [], pos);
      if (interesting(sol)) break;
    }
    var f = s.terms.join(" + ");
    return { type: "bool", q: "Minimum <b>" + (pos ? "POS" : "SOP") + "</b> for <code>F = " + f + "</code>.", vars: vars, fn: f.replace(/ /g, ""),
      show: sol.show, form: pos ? "pos" : "sop", lits: sol.lits,
      why: p("First put each term on the map: it fills the cells where its letters match. That gives " + sigma(on) + ".") + sol.why };
  };
  G.cmos = function () {
    var a = ri(2, 4), b = ri(2, 4), c = ri(2, 4), kinds = shuffle(["NAND", "NOR", "AND", "OR"]).slice(0, 3), ns = [a, b, c];
    var cnt = function (k, n) { return k === "NAND" || k === "NOR" ? 2 * n : 2 * n + 2; };
    var fields = kinds.map(function (k, i) { return { label: ns[i] + "-in " + k, ans: [String(cnt(k, ns[i]))] }; }).concat([{ label: "NOT", ans: ["2"] }]);
    return { type: "multi", q: "CMOS transistor counts:", fields: fields,
      why: p("NAND, NOR: <b>2n</b>. AND, OR: <b>2n + 2</b> (a NAND/NOR plus an inverter). NOT: <b>2</b>.") +
        tbl(["gate", "count"], kinds.map(function (k, i) { return [ns[i] + "-in " + k, (k === "NAND" || k === "NOR" ? "2 × " + ns[i] : "2 × " + ns[i] + " + 2") + " = <b>" + cnt(k, ns[i]) + "</b>"]; })) };
  };

  /* ================================================ 10 */
  G.xorchain = function () {
    var n = ri(3, 6), b = []; for (var i = 0; i < n; i++) b.push(ri(0, 1));
    var ones = b.filter(Boolean).length, r = ones % 2;
    return { type: "text", q: b.join(" ⊕ ") + " = ?", ans: [String(r)],
      why: p("XOR of many bits = 1 when the number of 1s is <b>odd</b>.") + p("There " + (ones === 1 ? "is 1 one" : "are " + ones + " ones") + " → " + (r ? "odd" : "even") + " → <b>" + r + "</b>.") };
  };
  G.fatrace = function () {
    var X = ri(0, 1), Y = ri(0, 1), Z = ri(0, 1), S1 = X ^ Y, C1 = X & Y, S = S1 ^ Z, C2 = S1 & Z, C = C1 | C2;
    return { type: "multi", q: "Full adder from two half adders. X = " + X + ", Y = " + Y + ", Z = " + Z + ". Trace it.", svg: "fa-two-ha",
      fields: [{ label: "S₁", ans: [String(S1)] }, { label: "C₁", ans: [String(C1)] }, { label: "C₂", ans: [String(C2)] }, { label: "S", ans: [String(S)] }, { label: "C", ans: [String(C)] }],
      why: tbl(["signal", "rule", "value"], [["S₁", "X ⊕ Y = " + X + " ⊕ " + Y, "<b>" + S1 + "</b>"], ["C₁", "X · Y = " + X + " · " + Y, "<b>" + C1 + "</b>"],
        ["S", "S₁ ⊕ Z = " + S1 + " ⊕ " + Z, "<b>" + S + "</b>"], ["C₂", "S₁ · Z = " + S1 + " · " + Z, "<b>" + C2 + "</b>"], ["C", "C₁ + C₂ = " + C1 + " + " + C2, "<b>" + C + "</b>"]]) +
        p("Check: " + X + " + " + Y + " + " + Z + " = " + (X + Y + Z) + " = binary " + C + S + " ✓") };
  };
  G.ripple = function () {
    var n = pick([4, 8, 12, 16, 24, 32, 64]), d = pick([2, 5, 10, 15, 20]);
    return { type: "text", q: "A " + n + "-bit ripple carry adder, " + d + " ns per gate delay. Worst-case delay in ns?", ans: [String(2 * n * d), 2 * n * d + "ns"],
      why: p("The carry passes through about 2 gate delays per bit, so 2n gate delays.") + p("2 × " + n + " × " + d + " = <b>" + 2 * n * d + " ns</b>.") };
  };
  G.addrows = function () {
    var n = ri(2, 6), r = Math.pow(2, 2 * n + 1);
    return { type: "text", q: "How many rows would the truth table of a " + n + "-bit adder have (two " + n + "-bit inputs plus a carry in)?", ans: [String(r)],
      why: p("Inputs: " + n + " + " + n + " + 1 = " + (2 * n + 1) + " bits.") + p("Rows = 2<sup>" + (2 * n + 1) + "</sup> = <b>" + r + "</b>. Too many to design by hand, which is why we chain full adders.") };
  };
  G.cla = function () {
    var A1 = ri(0, 1), A0 = ri(0, 1), B1 = ri(0, 1), B0 = ri(0, 1), C0 = ri(0, 1);
    var G0 = A0 & B0, P0 = A0 ^ B0, G1 = A1 & B1, P1 = A1 ^ B1, C1 = G0 | (P0 & C0), C2 = G1 | (P1 & C1);
    var a = 2 * A1 + A0, b = 2 * B1 + B0;
    return { type: "multi", q: "A₁A₀ = " + A1 + A0 + ", B₁B₀ = " + B1 + B0 + ", C₀ = " + C0 + ". Work out:",
      fields: [{ label: "G₀", ans: [String(G0)] }, { label: "P₀", ans: [String(P0)] }, { label: "G₁", ans: [String(G1)] }, { label: "P₁", ans: [String(P1)] }, { label: "C₂", ans: [String(C2)] }],
      why: p("Gᵢ = AᵢBᵢ (both 1 → makes a carry). Pᵢ = Aᵢ ⊕ Bᵢ (exactly one 1 → passes a carry on).") +
        tbl(["", "rule", "value"], [["G₀", A0 + " · " + B0, "<b>" + G0 + "</b>"], ["P₀", A0 + " ⊕ " + B0, "<b>" + P0 + "</b>"], ["G₁", A1 + " · " + B1, "<b>" + G1 + "</b>"], ["P₁", A1 + " ⊕ " + B1, "<b>" + P1 + "</b>"],
          ["C₂", "G₁ + P₁G₀ + P₁P₀C₀ = " + G1 + " + " + (P1 & G0) + " + " + (P1 & P0 & C0), "<b>" + C2 + "</b>"]]) +
        p("Check: " + a + " + " + b + " + " + C0 + " = " + (a + b + C0) + (C2 ? " ≥ 4, so a carry comes out ✓" : " < 4, so no carry out ✓")) };
  };
  G.mult2 = function () {
    var a = ri(0, 3), b = ri(0, 3), r = bin(a * b, 4);
    return { type: "multi", q: "2-bit multiplier: A₁A₀ = " + bin(a, 2) + ", B₁B₀ = " + bin(b, 2) + ". Give the product bits.", svg: "mult2x2",
      fields: [{ label: "C₃", ans: [r[0]] }, { label: "C₂", ans: [r[1]] }, { label: "C₁", ans: [r[2]] }, { label: "C₀", ans: [r[3]] }],
      why: p(a + " × " + b + " = " + a * b + " = <b>" + r + "</b> in 4 bits.") + p("On the circuit: C₀ = A₀B₀, C₁ = A₁B₀ ⊕ A₀B₁, and the half adder's carry feeds C₂ and C₃.") };
  };

  /* ================================================ 11 */
  G.decout = function () {
    var k = ri(0, 7);
    return { type: "text", q: "A 3-to-8 decoder gets input <code>" + bin(k, 3) + "</code>. Which output number is 1?", ans: [String(k), "D" + k],
      why: p(bin(k, 3) + " = " + k + " → <b>D" + sub(k) + "</b>. Every other output is 0.") };
  };
  G.deceq = function () {
    var k = ri(0, 3), t = prodText("AB", { mask: 3, val: k });
    return { type: "bool", q: "In a 2-to-4 decoder with inputs A₁A₀, write the equation for output Z" + sub(k) + ". Type A for A₁ and B for A₀.", vars: "AB", ones: [k], show: t, lits: 2,
      why: p(k + " = " + bin(k, 2) + " → each output is a minterm: 1 → plain, 0 → barred → <b>" + t + "</b>.") };
  };
  G.decor = function () {
    var on = sample(0, 7, ri(2, 4));
    return { type: "text", q: "f(x, y, z) = " + sigma(on) + " on an active-high 3-to-8 decoder. OR which outputs?", ans: [on.join(",")],
      why: p("Active-high outputs are the minterms. OR the ones in the list: <b>D" + on.map(sub).join(", D") + "</b>.") };
  };
  G.decor2 = function (o) {
    var low = !!o.low, F = sample(0, 7, ri(3, 4)), H = sample(0, 7, ri(3, 4));
    var use = function (on) { return low ? zerosOf(on, 8) : on; };
    return { type: "multi", q: "Two functions on one <b>" + (low ? "active-low" : "active-high") + "</b> 3-to-8 decoder: F = " + sigma(F) + ", H = " + sigma(H) + ". Which outputs go into each " + (low ? "AND" : "OR") + " gate?",
      fields: [{ label: "F: " + (low ? "AND" : "OR") + " of D", ans: [use(F).join(",")] }, { label: "H: " + (low ? "AND" : "OR") + " of D", ans: [use(H).join(",")] }],
      why: low ? p("Active-low outputs are <b>maxterms</b> (0 on their row). So AND the outputs in the <b>ΠM</b> list: the numbers <i>not</i> in Σm.") +
          p("F: ΠM(" + list(use(F)) + "). H: ΠM(" + list(use(H)) + ").")
        : p("Active-high outputs are minterms, so OR the outputs in each Σm list.") + p("F: D" + F.join(", D") + ". H: D" + H.join(", D") + ".") };
  };
  G.deccascade = function () {
    var k = ri(0, 7), top = k < 4;
    return { type: "multi", q: "3-to-8 from two 2-to-4 decoders. Input S₂S₁S₀ = " + bin(k, 3) + ".", svg: "dec3to8-from-2to4",
      fields: [{ label: "Which decoder (top/bottom)", ans: top ? ["top", "first", "1"] : ["bottom", "second", "2"] }, { label: "Q number on", ans: [String(k), "Q" + k] }],
      why: p("S₂ = " + (k >> 2) + " → " + (top ? "S₂' = 1 enables the <b>top</b> one." : "S₂ = 1 enables the <b>bottom</b> one.")) +
        p("S₁S₀ = " + bin(k & 3, 2) + " picks its output " + (k & 3) + ", which is <b>Q" + sub(k) + "</b> overall.") };
  };
  G.enc = function () {
    var k = ri(0, 7), b = bin(k, 3);
    return { type: "multi", q: "8-to-3 encoder. Only D" + sub(k) + " is on.", svg: "encoder8to3",
      fields: [{ label: "X", ans: [b[0]] }, { label: "Y", ans: [b[1]] }, { label: "Z", ans: [b[2]] }],
      why: p("The output is just the input number in binary: " + k + " = <b>" + b + "</b>.") + p("X = OR(D4–D7), Y = OR(D2, D3, D6, D7), Z = OR(odd D's).") };
  };
  G.prienc = function () {
    var on = sample(0, 7, ri(2, 3)), hi = on[on.length - 1];
    return { type: "text", q: "8-to-3 <b>priority</b> encoder: D" + on.join(", D").replace(/, D(\d)$/, " and D$1") + " are on. Output (3 bits)?", ans: [bin(hi, 3)],
      why: p("Highest active input wins: D" + sub(hi) + " → <b>" + bin(hi, 3) + "</b>.") };
  };

  /* ================================================ 12 */
  G.muxsel = function () {
    var n = pick([2, 3]), k = ri(0, (1 << n) - 1), s = bin(k, n);
    return { type: "text", q: (1 << n) + "-to-1 mux, " + (n === 2 ? "S₁S₀" : "S₂S₁S₀") + " = " + s + ". Which input reaches Y? (type e.g. I0)", ans: ["I" + k, "I" + sub(k), String(k)],
      why: p("The select lines are a binary number: " + s + " = " + k + " → <b>I" + sub(k) + "</b>.") };
  };
  G.muxtree = function (o) {
    var four = !!o.four, N = four ? pick([16, 64]) : pick([8, 16, 32]), per = four ? 4 : 2, rows = [], left = N, total = 0;
    while (left > 1) { var c = left / per; rows.push([left + " → " + c, c]); total += c; left = c; }
    return { type: "text", q: "How many " + per + "-to-1 muxes make a " + N + "-to-1 mux?", ans: [String(total)],
      why: p("Build a tree. Each level cuts the number of signals by " + per + ":") + tbl(["signals", "muxes"], rows) + p("Total: <b>" + total + "</b>.") };
  };
  G.mux8 = function () {
    var on = sample(0, 7, ri(3, 5)), f = [];
    for (var i = 0; i < 8; i++) f.push({ label: "D" + i, ans: [on.indexOf(i) >= 0 ? "1" : "0"] });
    return { type: "multi", q: "f(x, y, z) = " + sigma(on) + " on an <b>8-to-1</b> mux (selects xyz). Data inputs?", fields: f,
      why: p("Full size: D<sub>i</sub> = 1 when m<sub>i</sub> is in f, else 0. So D" + on.join(", D") + " = 1, the rest 0.") };
  };
  function residues(on, nv, last) {
    var rows = [], ans = [];
    for (var k = 0; k < (1 << (nv - 1)); k++) {
      var a = on.indexOf(2 * k) >= 0 ? 1 : 0, b = on.indexOf(2 * k + 1) >= 0 ? 1 : 0;
      var r = a === b ? String(a) : (b ? last : last + "'");
      rows.push(["D" + k, "m" + sub(2 * k) + ", m" + sub(2 * k + 1), a + ", " + b, "<b>" + r + "</b>"]); ans.push(r);
    }
    return { rows: rows, ans: ans };
  }
  G.mux4res = function () {
    var on = sample(0, 7, ri(3, 5)), R = residues(on, 3, "z");
    return { type: "multi", q: "f(x, y, z) = " + sigma(on) + " on a <b>4-to-1</b> mux, selects S₁ = x, S₀ = y.",
      fields: R.ans.map(function (a, i) { return { label: "D" + i, ans: [a] }; }),
      why: p("Pair the rows. In each pair z goes 0 then 1. Look at f: 0,0 → 0. 1,1 → 1. 0,1 → z. 1,0 → z'.") + tbl(["input", "rows", "f", "D"], R.rows) };
  };
  G.mux8res = function () {
    var on = sample(0, 15, ri(5, 9)), R = residues(on, 4, "D");
    return { type: "multi", q: "F(A, B, C, D) = " + sigma(on) + " on an 8-to-1 mux, selects ABC.",
      fields: R.ans.map(function (a, i) { return { label: "D" + i, ans: [a] }; }),
      hint: "Pair the rows: (0,1), (2,3), (4,5) … and look at F in each pair.",
      why: p("Pair the rows. In each pair D goes 0 then 1. F = 0,0 → 0. 1,1 → 1. 0,1 → D. 1,0 → D'.") + tbl(["input", "rows", "F", "value"], R.rows) };
  };
  G.demux = function () {
    var k = ri(0, 3), f = [];
    for (var i = 0; i < 4; i++) f.push({ label: "F" + i, ans: [i === k ? "1" : "0"] });
    return { type: "multi", q: "1-to-4 demux, S₁S₀ = " + bin(k, 2) + ", I₀ = 1.", svg: "demux", fields: f,
      why: p(bin(k, 2) + " = " + k + " → only F" + sub(k) + " gets the input (1). The others are 0.") };
  };

  window.QUIZ_GEN = G;
  window.QUIZ_GEN_LIB = { ri: ri, pick: pick, shuffle: shuffle, sample: sample, bin: bin, bins: bins, strip0: strip0, sub: sub, tbl: tbl, p: p, list: list,
    solveSOP: solveSOP, randFn: randFn, randCube: randCube, onesOf: onesOf, sigma: sigma, vlist: vlist, prodText: prodText, sumText: sumText,
    cubeCells: cubeCells, kmapHTML: kmapHTML, minCover: minCover, bitsCount: bits };
})();
