/* DE Lock-In quiz engine. Topic data files call QUIZ.add({...}). */
(function () {
  "use strict";
  var REPO = "https://github.com/albinjoby82-ops/DE_Lock-In/blob/main/";
  var TOPICS = [
    ["01", "History and chips", "01-overview"],
    ["02", "Number systems", "02-number-systems"],
    ["03", "Binary arithmetic", "03-binary-arithmetic"],
    ["04", "Signed numbers and overflow", "04-signed-numbers"],
    ["05", "Binary codes", "05-binary-codes"],
    ["06", "Boolean algebra", "06-boolean-algebra"],
    ["07", "Minterms and maxterms", "07-minterms-maxterms"],
    ["08", "Karnaugh maps", "08-karnaugh-maps"],
    ["09", "Don't cares, NAND and NOR", "09-dont-cares-nand-nor"],
    ["10", "Adders and subtractors", "10-adders"],
    ["11", "Decoders and encoders", "11-decoders-encoders"],
    ["12", "Multiplexers", "12-multiplexers"]
  ];
  var store = {
    get: function (k) { try { return JSON.parse(localStorage.getItem("delockin:" + k)); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem("delockin:" + k, JSON.stringify(v)); } catch (e) {} }
  };
  var loaded = {};
  function refLink(ref) {
    var m = /^(\d\d)(?: (?:§(\d+)|(exam drill)))?$/.exec(ref || "");
    var R = window.QUIZ_REFS && m && window.QUIZ_REFS[m[1]];
    var p = el("p", { class: "ref" }, "From the notes: ");
    if (!R) { p.appendChild(document.createTextNode(ref)); return p; }
    var anchor = R[m[2] || m[3]];
    p.appendChild(el("a", { href: REPO + "notes/" + R.file + ".md" + (anchor ? "#" + anchor : ""), target: "_blank", rel: "noopener" }, "Read it: " + ref + " →"));
    return p;
  }
  window.QUIZ = { add: function (t) { loaded[t.id] = t; }, TOPICS: TOPICS, REPO: REPO, store: store };

  /* ------------------------------------------------ Boolean expressions */
  function parseBool(src, vars) {
    var s = src.replace(/\s+/g, "").replace(/[’′`´]/g, "'").replace(/[·∙•*.&]/g, "·")
      .replace(/[|∨]/g, "+").replace(/\^|⊕/g, "⊕").replace(/[¬~!]/g, "¬");
    var i = 0, lits = 0;
    var vmap = {};
    for (var k = 0; k < vars.length; k++) vmap[vars[k].toLowerCase()] = k;
    function peek() { return s[i]; }
    function err(m) { throw new Error(m); }
    function sum() {
      var n = xorx(), kids = [n];
      while (peek() === "+") { i++; kids.push(xorx()); }
      return kids.length > 1 ? { op: "or", k: kids } : n;
    }
    function xorx() {
      var n = prod(), kids = [n];
      while (peek() === "⊕" || peek() === "⊙") {
        var nx = s[i] === "⊙"; i++;
        var r = prod();
        n = nx ? { op: "not", k: [{ op: "xor", k: [n, r] }] } : { op: "xor", k: [n, r] };
      }
      return n;
    }
    function prod() {
      var kids = [unary()];
      while (i < s.length) {
        var c = peek();
        if (c === "·") { i++; kids.push(unary()); continue; }
        if (c === "(" || c === "¬" || /[A-Za-z01]/.test(c)) { kids.push(unary()); continue; }
        break;
      }
      return kids.length > 1 ? { op: "and", k: kids } : kids[0];
    }
    function unary() {
      var neg = 0;
      while (peek() === "¬") { i++; neg ^= 1; }
      var n = atom();
      while (peek() === "'") { i++; n = { op: "not", k: [n] }; }
      if (neg) n = { op: "not", k: [n] };
      return n;
    }
    function atom() {
      var c = peek();
      if (c === undefined) err("The answer ends too early.");
      if (c === "(") { i++; var n = sum(); if (peek() !== ")") err("A bracket is not closed."); i++; return n; }
      if (c === "0" || c === "1") { i++; return { op: "const", v: +c }; }
      if (/[A-Za-z]/.test(c)) {
        var key = c.toLowerCase();
        if (!(key in vmap)) err("'" + c + "' is not one of the variables (" + vars.split("").join(", ") + ").");
        i++; lits++; return { op: "var", v: vmap[key] };
      }
      err("I can't read '" + c + "'.");
    }
    if (!s.length) err("Type an expression first.");
    var tree = sum();
    if (i < s.length) err("I can't read the part starting at '" + s.slice(i) + "'.");
    return { tree: tree, lits: lits };
  }
  function evalB(n, row) {
    switch (n.op) {
      case "const": return n.v;
      case "var": return row[n.v];
      case "not": return 1 - evalB(n.k[0], row);
      case "and": for (var a = 0; a < n.k.length; a++) if (!evalB(n.k[a], row)) return 0; return 1;
      case "or": for (var b = 0; b < n.k.length; b++) if (evalB(n.k[b], row)) return 1; return 0;
      case "xor": var x = 0; n.k.forEach(function (c) { x ^= evalB(c, row); }); return x;
    }
  }
  function isLit(n) { return n.op === "var" || (n.op === "not" && n.k[0].op === "var"); }
  function isProd(n) { return isLit(n) || (n.op === "and" && n.k.every(isLit)); }
  function isSum(n) { return isLit(n) || (n.op === "or" && n.k.every(isLit)); }
  function isSOP(n) { return isProd(n) || (n.op === "or" && n.k.every(isProd)); }
  function isPOS(n) { return isSum(n) || (n.op === "and" && n.k.every(isSum)); }
  function termCount(n, form) {
    if (form === "pos") return n.op === "and" ? n.k.length : 1;
    return n.op === "or" ? n.k.length : 1;
  }
  function truth(tree, nv) {
    var out = [];
    for (var m = 0; m < (1 << nv); m++) {
      var row = [];
      for (var b = 0; b < nv; b++) row.push((m >> (nv - 1 - b)) & 1);
      out.push(evalB(tree, row));
    }
    return out;
  }
  function ensureOnes(q) {
    if (q.ones || !q.fn) return;
    var tt = truth(parseBool(q.fn, q.vars).tree, q.vars.length);
    q.ones = []; tt.forEach(function (v, m) { if (v) q.ones.push(m); });
  }
  QUIZ.ensureOnes = ensureOnes;
  function checkBool(q, txt) {
    ensureOnes(q);
    var p;
    try { p = parseBool(txt, q.vars); } catch (e) { return { ok: false, soft: true, msg: e.message }; }
    var nv = q.vars.length, tt = truth(p.tree, nv), dc = q.dc || [], wrong = [];
    for (var m = 0; m < tt.length; m++) {
      if (dc.indexOf(m) >= 0) continue;
      var want = q.ones.indexOf(m) >= 0 ? 1 : 0;
      if (tt[m] !== want) wrong.push(m);
    }
    if (wrong.length) return { ok: false, msg: "Not the same function. It gives the wrong output on row" + (wrong.length > 1 ? "s " : " ") + wrong.join(", ") + "." };
    if (q.form === "sop" && !isSOP(p.tree)) return { ok: false, msg: "Right function, but that's not written as a sum of products (an OR of AND terms)." };
    if (q.form === "pos" && !isPOS(p.tree)) return { ok: false, msg: "Right function, but that's not written as a product of sums (an AND of OR terms)." };
    if (typeof q.lits === "number" && p.lits > q.lits) return { ok: false, msg: "Right function, but not minimal: you used " + p.lits + " letters. The minimum is " + q.lits + ". Look for bigger blocks, or a block you don't need." };
    if (q.terms && (q.form === "sop" || q.form === "pos") && termCount(p.tree, q.form) > q.terms) return { ok: false, msg: "Right function, but it has more terms than it needs (" + q.terms + ")." };
    return { ok: true };
  }
  QUIZ.parseBool = parseBool; QUIZ.checkBool = checkBool; QUIZ.truth = truth;

  /* ------------------------------------------------ text answers */
  function norm(s) {
    return String(s).toLowerCase().replace(/[’′`´]/g, "'").replace(/\s+/g, "")
      .replace(/[₀₁₂₃₄₅₆₇₈₉]+$/, "").replace(/\((2|8|10|16)\)$/, "").replace(/^0x/, "")
      .replace(/−/g, "-").replace(/,$/, "");
  }
  function checkText(accepted, txt) {
    var t = norm(txt);
    if (!t) return null;
    for (var i = 0; i < accepted.length; i++) if (norm(accepted[i]) === t) return true;
    return false;
  }
  QUIZ.norm = norm;

  /* ------------------------------------------------ helpers */
  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      if (k === "class") e.className = attrs[k]; else if (k === "text") e.textContent = attrs[k]; else e.setAttribute(k, attrs[k]);
    }
    if (html !== undefined) e.innerHTML = html;
    return e;
  }
  function gray(nbits) { return nbits === 1 ? ["0", "1"] : ["00", "01", "11", "10"]; }
  function layout(nv) {
    var rb = nv === 2 ? ["0", "1"] : gray(2), cb = nv === 4 ? gray(2) : ["0", "1"];
    return { rb: rb, cb: cb, rv: nv === 2 ? 1 : 2 };
  }

  function kmapWidget(q, onchange) {
    ensureOnes(q);
    var nv = q.vars.length, L = layout(nv);
    var rv = q.vars.slice(0, L.rv), cv = q.vars.slice(L.rv);
    var wrap = el("div", { class: "kmap-wrap" });
    var t = el("table", { class: "kmap" });
    var head = "<tr><th class='corner'><span class='rv'>" + rv + "</span><span class='cv'>" + cv + "</span></th>";
    L.cb.forEach(function (c) { head += "<th>" + c + "</th>"; });
    t.innerHTML = "<thead>" + head + "</tr></thead>";
    var tb = el("tbody");
    var cells = {};
    L.rb.forEach(function (r) {
      var tr = el("tr"); tr.appendChild(el("th", { text: r }));
      L.cb.forEach(function (c) {
        var m = parseInt(r + c, 2);
        var td = el("td");
        var b = el("button", { type: "button", class: "cell", "data-m": m, "data-v": "", "aria-label": "cell " + m + ", empty" });
        b.innerHTML = "<span class='v'></span><span class='m'>" + m + "</span>";
        b.addEventListener("click", function () {
          var order = q.dc && q.dc.length ? ["", "1", "x"] : ["", "1"];
          var v = b.getAttribute("data-v");
          var nvv = order[(order.indexOf(v) + 1) % order.length];
          b.setAttribute("data-v", nvv);
          b.querySelector(".v").textContent = nvv;
          b.setAttribute("aria-label", "cell " + m + ", " + (nvv || "0"));
          b.classList.remove("bad", "good");
          onchange && onchange();
        });
        cells[m] = b; td.appendChild(b); tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
    var saved = null;
    t.appendChild(tb); wrap.appendChild(t);
    wrap.appendChild(el("p", { class: "tiny" }, "Click a cell: empty (= 0) → 1" + (q.dc && q.dc.length ? " → x" : "") + ". Small number = minterm."));
    return {
      node: wrap,
      check: function () {
        var bad = 0;
        Object.keys(cells).forEach(function (m) {
          m = +m; var b = cells[m], v = b.getAttribute("data-v");
          var want = q.ones.indexOf(m) >= 0 ? "1" : ((q.dc || []).indexOf(m) >= 0 ? "x" : "");
          var ok = v === want;
          b.classList.toggle("bad", !ok); b.classList.toggle("good", ok);
          if (!ok) bad++;
        });
        return bad;
      },
      hide: function () {
        if (!saved) return;
        Object.keys(saved).forEach(function (m) { var b = cells[m]; b.setAttribute("data-v", saved[m]); b.querySelector(".v").textContent = saved[m]; b.classList.remove("bad", "good"); });
        saved = null;
      },
      reveal: function () {
        saved = {};
        Object.keys(cells).forEach(function (m) {
          m = +m; var b = cells[m]; saved[m] = b.getAttribute("data-v") || "";
          var want = q.ones.indexOf(m) >= 0 ? "1" : ((q.dc || []).indexOf(m) >= 0 ? "x" : "");
          b.setAttribute("data-v", want); b.querySelector(".v").textContent = want;
        });
      }
    };
  }

  function ttWidget(q) {
    var nv = q.vars.length, names = Object.keys(q.outs);
    var t = el("table", { class: "tt" });
    var h = "<thead><tr>";
    q.vars.split("").forEach(function (v) { h += "<th>" + v + "</th>"; });
    names.forEach(function (n) { h += "<th class='o'>" + n + "</th>"; });
    t.innerHTML = h + "</tr></thead>";
    var tb = el("tbody"), btns = [];
    for (var m = 0; m < (1 << nv); m++) {
      var tr = el("tr");
      for (var b = 0; b < nv; b++) tr.appendChild(el("td", { text: String((m >> (nv - 1 - b)) & 1) }));
      names.forEach(function (n) {
        var td = el("td", { class: "o" });
        var bt = el("button", { type: "button", class: "bit", "data-v": "", "data-n": n, "data-m": m, "aria-label": n + " row " + m });
        bt.textContent = "·";
        bt.addEventListener("click", function () {
          var v = bt.getAttribute("data-v"), nvv = v === "1" ? "0" : "1";
          bt.setAttribute("data-v", nvv); bt.textContent = nvv; bt.classList.remove("bad", "good");
        });
        btns.push(bt); td.appendChild(bt); tr.appendChild(td);
      });
      tb.appendChild(tr);
    }
    t.appendChild(tb);
    var saved = null;
    var wrap = el("div", { class: "tt-wrap" }); wrap.appendChild(t);
    wrap.appendChild(el("p", { class: "tiny" }, "Click an output cell to set it 1, click again for 0."));
    return {
      node: wrap,
      check: function () {
        var bad = 0;
        btns.forEach(function (bt) {
          var want = String(q.outs[bt.getAttribute("data-n")][+bt.getAttribute("data-m")]);
          var ok = bt.getAttribute("data-v") === want;
          bt.classList.toggle("bad", !ok); bt.classList.toggle("good", ok); if (!ok) bad++;
        });
        return bad;
      },
      hide: function () {
        if (!saved) return;
        btns.forEach(function (bt, i) { bt.setAttribute("data-v", saved[i]); bt.textContent = saved[i] === "" ? "·" : saved[i]; bt.classList.remove("bad", "good"); });
        saved = null;
      },
      reveal: function () {
        saved = btns.map(function (bt) { return bt.getAttribute("data-v"); });
        btns.forEach(function (bt) { var w = String(q.outs[bt.getAttribute("data-n")][+bt.getAttribute("data-m")]); bt.setAttribute("data-v", w); bt.textContent = w; });
      }
    };
  }

  /* ------------------------------------------------ one question card */
  function renderQuestion(q, host, done) {
    host.innerHTML = "";
    var card = el("article", { class: "q" });
    if (q.tag) card.appendChild(el("p", { class: "from" }, q.tag));
    card.appendChild(el("div", { class: "q-kind" }, ({ mcq: "Pick one", tf: "True or false", text: "Type the answer", bool: "Type the expression", kmap: "Fill the K-map", tt: "Fill the truth table", multi: "Fill each box", work: "Do it on paper, then mark yourself" })[q.type] || ""));
    card.appendChild(el("div", { class: "q-text" }, q.q));
    if (q.svg) {
      var fig = el("figure", { class: "q-fig" });
      var link = el("a", { href: "svg/" + q.svg + ".svg", target: "_blank", rel: "noopener", title: "Open full size" });
      link.appendChild(el("img", { src: "svg/" + q.svg + ".svg", alt: q.alt || "diagram", loading: "lazy" }));
      fig.appendChild(link);
      fig.appendChild(el("p", { class: "tiny" }, "Tap the diagram to open it full size."));
      card.appendChild(fig);
    }
    var body = el("div", { class: "q-body" });
    card.appendChild(body);
    var fb = el("div", { class: "fb", "aria-live": "polite" });
    var actions = el("div", { class: "actions" });
    var checkBtn = el("button", { type: "button", class: "btn primary" }, "Check");
    var hintBtn = q.hint ? el("button", { type: "button", class: "btn ghost" }, "Hint") : null;
    var showBtn = el("button", { type: "button", class: q.type === "work" ? "btn primary" : "btn ghost" }, q.type === "work" ? "Show solution" : "Show answer");
    actions.appendChild(checkBtn); if (hintBtn) actions.appendChild(hintBtn); actions.appendChild(showBtn);
    card.appendChild(actions); card.appendChild(fb);
    var answered = false, tries = 0, widget = null, inputs = [];

    function finish(ok, msg) {
      tries++;
      fb.className = "fb " + (ok ? "ok" : "no");
      var head = ok ? (tries === 1 ? "Correct." : "Got it.") : "Not yet.";
      fb.innerHTML = "<p class='fb-head'>" + head + (msg ? " <span>" + msg + "</span>" : "") + "</p>";
      if (ok || tries >= 2) showWhy(ok);
      if (ok && !answered) { answered = true; done(tries === 1 ? 1 : 0.5); }
    }
    function showWhy(ok) {
      if (fb.querySelector(".why")) return;
      if (!ok && !answered) { answered = true; done(0); }
      var w = el("div", { class: "why" }, q.why || "");
      if (q.ref) w.appendChild(refLink(q.ref));
      fb.appendChild(w);
      checkBtn.textContent = "Check again";
    }
    var shown = false, savedInputs = [], markedOpts = [];
    function hideAnswer() {
      shown = false; showBtn.textContent = q.type === "work" ? "Show solution" : "Show answer";
      if (widget && widget.hide) widget.hide();
      markedOpts.forEach(function (b) { b.classList.remove("right"); }); markedOpts = [];
      inputs.forEach(function (inp, i) { inp.value = savedInputs[i] || ""; });
      fb.className = "fb"; fb.innerHTML = "";
      checkBtn.textContent = "Check";
    }
    showBtn.addEventListener("click", function () {
      if (shown) { hideAnswer(); return; }
      shown = true; showBtn.textContent = q.type === "work" ? "Hide solution" : "Hide answer";
      savedInputs = inputs.map(function (inp) { return inp.value; });
      if (widget && widget.reveal) widget.reveal();
      if (q.type === "mcq" || q.type === "tf") body.querySelectorAll(".opt").forEach(function (b, i) { if (i === q.a && !b.classList.contains("right")) { b.classList.add("right"); markedOpts.push(b); } });
      if (q.type === "text" || q.type === "bool") inputs[0].value = q.show || (q.ans ? q.ans[0] : "");
      if (q.type === "multi") q.fields.forEach(function (f, i) { inputs[i].value = f.ans[0]; });
      fb.className = "fb shown"; fb.innerHTML = "<p class='fb-head'>" + (q.type === "work" ? "Solution" : "Answer shown.") + "</p>";
      if (!answered && q.type !== "work") { answered = true; done(0); }
      fb.appendChild(el("div", { class: "why" }, q.why || ""));
      if (q.ref) fb.lastChild.appendChild(refLink(q.ref));
      if (q.type === "work" && !answered) {
        var mk = el("div", { class: "selfmark" });
        mk.appendChild(el("span", {}, "How did you do?"));
        [["Got it", 1], ["Half right", 0.5], ["Missed it", 0]].forEach(function (o) {
          var b = el("button", { type: "button", class: "btn" + (o[1] === 1 ? " primary" : " ghost") }, o[0]);
          b.addEventListener("click", function () {
            if (answered) return;
            answered = true; done(o[1]);
            mk.innerHTML = "<span>Marked: <b>" + o[0] + "</b></span>";
          });
          mk.appendChild(b);
        });
        fb.appendChild(mk);
      }
    });
    if (hintBtn) hintBtn.addEventListener("click", function () { hintBtn.outerHTML = "<p class='hint'>Hint: " + q.hint + "</p>"; });

    if (q.type === "work") {
      checkBtn.style.display = "none";
      body.appendChild(el("p", { class: "tiny" }, "Write your full working on paper first. Then open the solution and mark yourself honestly."));
    } else if (q.type === "mcq" || q.type === "tf") {
      var opts = q.type === "tf" ? ["True", "False"] : q.opts;
      var list = el("div", { class: "opts" });
      var chosen = null;
      opts.forEach(function (o, i) {
        var b = el("button", { type: "button", class: "opt" }, "<span class='k'>" + (q.type === "tf" ? o[0] : "ABCDEF"[i]) + "</span><span>" + o + "</span>");
        b.addEventListener("click", function () {
          list.querySelectorAll(".opt").forEach(function (x) { x.classList.remove("sel"); }); b.classList.add("sel"); chosen = i;
          check();
        });
        list.appendChild(b);
      });
      body.appendChild(list);
      checkBtn.style.display = "none";
      var check = function () {
        var ok = chosen === q.a;
        list.querySelectorAll(".opt").forEach(function (x, i) { x.classList.toggle("wrong", i === chosen && !ok); x.classList.toggle("right", ok && i === chosen); });
        finish(ok, ok ? "" : (q.miss && q.miss[chosen]) || "");
      };
    } else if (q.type === "text" || q.type === "bool") {
      var row = el("div", { class: "inrow" });
      var inp = el("input", { type: "text", class: "ans", autocomplete: "off", autocapitalize: "off", spellcheck: "false", placeholder: q.type === "bool" ? "e.g. A'B + C   (use ' for NOT)" : (q.ph || "your answer") });
      if (q.prefix) row.appendChild(el("span", { class: "pre" }, q.prefix));
      row.appendChild(inp); inputs.push(inp); body.appendChild(row);
      if (q.type === "bool") {
        var keys = el("div", { class: "keys" });
        ["'", "+", "(", ")"].concat(q.vars.split("")).forEach(function (k) {
          var kb = el("button", { type: "button", class: "key" }, k);
          kb.addEventListener("click", function () { var p = inp.selectionStart || inp.value.length; inp.value = inp.value.slice(0, p) + k + inp.value.slice(p); inp.focus(); inp.setSelectionRange(p + 1, p + 1); });
          keys.appendChild(kb);
        });
        body.appendChild(keys);
      }
      inp.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); checkBtn.click(); } });
      checkBtn.addEventListener("click", function () {
        if (q.type === "bool") {
          var r = checkBool(q, inp.value);
          if (r.soft) { fb.className = "fb soft"; fb.innerHTML = "<p class='fb-head'>" + r.msg + "</p>"; return; }
          finish(r.ok, r.msg || "");
        } else {
          var r2 = checkText(q.ans, inp.value);
          if (r2 === null) { fb.className = "fb soft"; fb.innerHTML = "<p class='fb-head'>Type an answer first.</p>"; return; }
          finish(r2, r2 ? "" : (q.miss && q.miss[norm(inp.value)]) || "");
        }
      });
    } else if (q.type === "multi") {
      var grid = el("div", { class: "multi" });
      q.fields.forEach(function (f) {
        var lab = el("label", { class: "mf" });
        lab.appendChild(el("span", {}, f.label));
        var i2 = el("input", { type: "text", class: "ans small", autocomplete: "off", spellcheck: "false" });
        i2.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); checkBtn.click(); } });
        lab.appendChild(i2); grid.appendChild(lab); inputs.push(i2);
      });
      body.appendChild(grid);
      checkBtn.addEventListener("click", function () {
        var bad = 0;
        q.fields.forEach(function (f, i) {
          var ok = checkText(f.ans, inputs[i].value) === true;
          inputs[i].classList.toggle("bad", !ok); inputs[i].classList.toggle("good", ok); if (!ok) bad++;
        });
        finish(bad === 0, bad ? bad + " box" + (bad > 1 ? "es are" : " is") + " wrong (red)." : "");
      });
    } else if (q.type === "kmap" || q.type === "tt") {
      widget = q.type === "kmap" ? kmapWidget(q) : ttWidget(q);
      body.appendChild(widget.node);
      checkBtn.addEventListener("click", function () {
        var bad = widget.check();
        finish(bad === 0, bad ? bad + " cell" + (bad > 1 ? "s are" : " is") + " wrong (red)." : "");
      });
    }
    host.appendChild(card);
    var first = card.querySelector("input");
    if (first && !q._nofocus && window.matchMedia("(pointer:fine)").matches) first.focus({ preventScroll: true });
  }

  /* ------------------------------------------------ quiz runner */
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  function runQuiz(root, qs, opts) {
    var idx = 0, scores = new Array(qs.length).fill(null);
    root.innerHTML = "";
    var bar = el("div", { class: "qbar" });
    var dots = el("div", { class: "dots" });
    qs.forEach(function (q, i) {
      var d = el("button", { type: "button", class: "dot", "aria-label": "Question " + (i + 1) }, String(i + 1));
      d.addEventListener("click", function () { go(i); });
      dots.appendChild(d);
    });
    var sc = el("div", { class: "score" });
    bar.appendChild(dots); bar.appendChild(sc);
    var stage = el("div", { class: "stage" });
    var nav = el("div", { class: "nav" });
    var prev = el("button", { type: "button", class: "btn ghost" }, "← Back");
    var next = el("button", { type: "button", class: "btn" }, "Next →");
    nav.appendChild(prev); nav.appendChild(next);
    root.appendChild(bar); root.appendChild(stage); root.appendChild(nav);
    prev.addEventListener("click", function () { if (idx > 0) go(idx - 1); });
    next.addEventListener("click", function () { if (idx < qs.length - 1) go(idx + 1); else summary(); });

    function refresh() {
      var got = 0, n = 0;
      scores.forEach(function (s, i) {
        var d = dots.children[i];
        d.className = "dot" + (i === idx ? " cur" : "") + (s === null ? "" : s === 1 ? " s1" : s > 0 ? " s5" : " s0");
        if (s !== null) { got += s; n++; }
      });
      sc.textContent = n ? ("Score " + (Math.round(got * 10) / 10) + " / " + n) : (qs.length + " questions");
      next.textContent = idx === qs.length - 1 ? "Finish" : "Next →";
      prev.disabled = idx === 0;
    }
    function go(i) {
      idx = i;
      var q = qs[i];
      var pre = el("div");
      if (q._from) pre.appendChild(el("p", { class: "from" }, q._from));
      else if (q._topic) pre.appendChild(el("p", { class: "from" }, "Topic " + q._topic));
      stage.innerHTML = "";
      stage.appendChild(pre);
      var host = el("div");
      var scoreIt = function (s) { if (scores[i] === null) { scores[i] = s; refresh(); if (opts.onScore) opts.onScore(q, s); } };
      var showOriginal = function () {
        renderQuestion(q, host, scoreIt);
        if (scores[i] !== null) host.querySelector(".q").classList.add("seen");
      };
      var G = window.QUIZ_GEN;
      if (q.gen && G && G[q.gen]) {
        var bar = el("div", { class: "genbar" });
        var newBtn = el("button", { type: "button", class: "btn ghost gen-new" }, "New numbers");
        var backBtn = el("button", { type: "button", class: "btn ghost gen-back" }, "Back to the slide question");
        var note = el("span", { class: "gen-note" }, "Same question, fresh numbers.");
        backBtn.hidden = true;
        newBtn.addEventListener("click", function () {
          var v;
          try { v = G[q.gen](q.gp || {}); } catch (e) { note.textContent = "Couldn't make a new one, try again."; return; }
          v.ref = v.ref || q.ref;
          renderQuestion(v, host, function () {});
          host.querySelector(".q").classList.add("variant");
          note.textContent = "Practice version: new numbers, not scored.";
          newBtn.textContent = "Another one"; backBtn.hidden = false;
        });
        backBtn.addEventListener("click", function () {
          showOriginal();
          note.textContent = "Same question, fresh numbers."; newBtn.textContent = "New numbers"; backBtn.hidden = true;
        });
        bar.appendChild(newBtn); bar.appendChild(backBtn); bar.appendChild(note);
        stage.appendChild(bar);
      }
      stage.appendChild(host);
      showOriginal();
      refresh();
      root.scrollIntoView({ block: "start", behavior: "smooth" });
    }
    function summary() {
      var got = 0, missed = [];
      scores.forEach(function (s, i) { got += s || 0; if (s !== 1) missed.push(i); });
      var pct = Math.round(100 * got / qs.length);
      if (opts.key) { var best = store.get("best:" + opts.key) || 0; if (pct > best) store.set("best:" + opts.key, pct); }
      if (opts.onFinish) opts.onFinish(pct, qs, scores);
      stage.innerHTML = "";
      var box = el("div", { class: "summary" });
      box.appendChild(el("h2", {}, pct + "%"));
      box.appendChild(el("p", {}, pct >= 85 ? "Locked in. Move on, and come back in a couple of days." : pct >= 60 ? "Nearly there. Redo the ones you missed now, while it's fresh." : "Go back to the notes for the missed ones, then try again."));
      if (missed.length) {
        var redo = el("button", { type: "button", class: "btn primary" }, "Redo the " + missed.length + " I missed");
        redo.addEventListener("click", function () { runQuiz(root, missed.map(function (i) { return qs[i]; }), {}); });
        box.appendChild(redo);
      }
      var again = el("button", { type: "button", class: "btn ghost" }, "Start again (shuffled)");
      again.addEventListener("click", function () { runQuiz(root, shuffle(qs.slice()), opts); });
      box.appendChild(again);
      stage.appendChild(box);
      next.textContent = "Finish";
    }
    go(0);
  }
  QUIZ.runQuiz = runQuiz;
  QUIZ.shuffle = shuffle;
  QUIZ.renderQuestion = renderQuestion;

  QUIZ.load = function (ids, cb) {
    var left = ids.length;
    ids.forEach(function (id) {
      if (loaded[id]) { if (--left === 0) cb(loaded); return; }
      var s = document.createElement("script");
      s.src = "data/" + id + ".js";
      s.onload = s.onerror = function () { if (--left === 0) cb(loaded); };
      document.head.appendChild(s);
    });
  };
})();
