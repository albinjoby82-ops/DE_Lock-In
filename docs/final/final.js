(function () {
  "use strict";
  var KEY = "de-lockin-final-v1";
  var store = {};
  try { store = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { store = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {} }
  if (!store.status) store.status = {};

  var D, tab = "path", cur = null, curItem = 0, shown = {};
  var main = document.getElementById("main"), side = document.getElementById("side"), tabs = document.getElementById("tabs");

  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function math(node) {
    if (window.renderMathInElement) {
      try { renderMathInElement(node, { delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }], throwOnError: false }); } catch (e) {}
    }
  }
  function parts(t) { return D.parts.filter(function (p) { return p.tab === t; }); }
  function counts(p) {
    var it = p.items || [], ok = 0;
    it.forEach(function (i) { if (store.status[i.id] === "ok") ok++; });
    return [ok, it.length];
  }
  function totals() {
    var ok = 0, n = 0;
    parts("path").forEach(function (p) { var c = counts(p); ok += c[0]; n += c[1]; });
    return [ok, n];
  }
  function drawProgress() {
    var t = totals();
    document.getElementById("prog").textContent = "Exam path: " + t[0] + " / " + t[1] + " got";
  }

  function drawTabs() {
    tabs.innerHTML = "";
    [["path", "Exam path"], ["more", "More practice"]].forEach(function (t) {
      var b = el("button", "tab" + (tab === t[0] ? " on" : ""), t[1]);
      b.type = "button";
      b.onclick = function () { tab = t[0]; go(parts(tab)[0].id); };
      tabs.appendChild(b);
    });
  }
  function drawSide() {
    side.innerHTML = "";
    var sel = el("select", "jump");
    sel.setAttribute("aria-label", "Jump to section");
    var lastKind = null;
    parts(tab).forEach(function (p) {
      if (p.kind !== lastKind && (p.kind === "exam" || p.kind === "topic") && tab === "path") {
        side.appendChild(el("div", "sep", p.kind === "exam" ? "Exams" : "Topics"));
      }
      lastKind = p.kind;
      var c = counts(p);
      var b = el("button", p.id === cur ? "on" : "");
      b.type = "button";
      b.appendChild(el("span", "", p.title));
      if (c[1]) b.appendChild(el("span", "cnt" + (c[0] === c[1] ? " done" : ""), c[0] + "/" + c[1]));
      b.onclick = function () { go(p.id); };
      side.appendChild(b);
      var o = el("option", "", p.title + (c[1] ? "  (" + c[0] + "/" + c[1] + ")" : ""));
      o.value = p.id; if (p.id === cur) o.selected = true;
      sel.appendChild(o);
    });
    sel.onchange = function () { go(sel.value); };
    return sel;
  }

  function go(id, keepScroll) {
    var p = D.parts.filter(function (x) { return x.id === id; })[0] || D.parts[0];
    cur = p.id; tab = p.tab; curItem = 0;
    try { history.replaceState(null, "", "#" + cur); } catch (e) { }
    store.last = cur; save();
    drawTabs();
    var sel = drawSide();
    main.innerHTML = "";
    main.appendChild(sel);
    main.appendChild(el("h1", "", p.title));
    if (p.freq) main.appendChild(el("div", "freq", p.freq));
    if (p.html) main.appendChild(el("div", "info", p.html));
    if (p.intro) main.appendChild(el("div", "intro", p.intro));
    if (p.learn) {
      var d = el("details", "learn");
      d.open = true;
      d.appendChild(el("summary", "", "Learn it"));
      d.appendChild(el("div", "", p.learn));
      if (p.check) {
        var c = el("div", "check");
        c.appendChild(el("div", "q", "Quick check: " + p.check.q));
        var ans = el("div", "a", p.check.a); ans.hidden = true;
        var b = el("button", "btn", "Show answer"); b.type = "button";
        b.onclick = function () { ans.hidden = !ans.hidden; b.textContent = ans.hidden ? "Show answer" : "Hide answer"; };
        c.appendChild(b); c.appendChild(ans);
        d.appendChild(c);
      }
      main.appendChild(d);
    }
    (p.items || []).forEach(function (it, i) { main.appendChild(card(it, i)); });
    var ps = parts(tab), ix = ps.indexOf(p), nav = el("div", "nav2");
    var pb = el("button", "btn", "← " + (ix > 0 ? ps[ix - 1].title : "")); pb.type = "button"; pb.disabled = ix <= 0;
    pb.onclick = function () { go(ps[ix - 1].id); };
    var nb = el("button", "btn primary", (ix < ps.length - 1 ? ps[ix + 1].title : "") + " →"); nb.type = "button"; nb.disabled = ix >= ps.length - 1;
    nb.onclick = function () { go(ps[ix + 1].id); };
    nav.appendChild(pb); nav.appendChild(nb); main.appendChild(nav);
    var r = el("div", "reset", "Progress is saved in this browser only. Content version " + D.version + ". ");
    var rb = el("button", "", "Reset progress"); rb.type = "button";
    rb.onclick = function () { if (rb.dataset.sure) { store.status = {}; save(); go(cur); } else { rb.dataset.sure = "1"; rb.textContent = "Click again to wipe all progress"; } };
    r.appendChild(rb); main.appendChild(r);
    math(main);
    mark();
    drawProgress();
    if (!keepScroll) window.scrollTo(0, 0);
  }

  function card(it, i) {
    var c = el("section", "card"); c.id = "q-" + it.id; c.dataset.i = i;
    if (it.src) c.appendChild(el("div", "src", it.src));
    c.appendChild(el("h2", "", it.title));
    c.appendChild(el("div", "prompt", it.prompt));
    var ol = el("ol", "steps"); c.appendChild(ol);
    var row = el("div", "row");
    var next = el("button", "btn primary", "Show first step"); next.type = "button";
    var all = el("button", "btn", "Show all"); all.type = "button";
    var left = el("span", "left", it.steps.length + " steps");
    var ok = el("button", "btn ok", "Got it"); ok.type = "button";
    var redo = el("button", "btn redo", "Need to redo"); redo.type = "button";
    row.appendChild(next); row.appendChild(all); row.appendChild(left);
    var row2 = el("div", "row"); row2.appendChild(ok); row2.appendChild(redo);
    c.appendChild(row); c.appendChild(row2);
    function reveal() {
      var n = shown[it.id] || 0;
      if (n >= it.steps.length) return false;
      var s = it.steps[n], li = el("li", "", '<div class="do">' + s["do"] + "</div>" + (s.why ? '<div class="why"><b class="w">Why:</b> ' + s.why + "</div>" : ""));
      ol.appendChild(li); math(li);
      shown[it.id] = n + 1;
      if (n + 1 >= it.steps.length) {
        if (it.answer) { var f = el("div", "final", "Answer: " + it.answer); c.insertBefore(f, row); math(f); }
        next.disabled = true; all.disabled = true; next.textContent = "All steps shown"; left.textContent = "";
      } else { next.textContent = "Next step"; left.textContent = (it.steps.length - n - 1) + " left"; }
      return li;
    }
    next.onclick = function () { focusItem(i); var li = reveal(); if (li && li.scrollIntoView) li.scrollIntoView({ block: "nearest", behavior: "smooth" }); };
    all.onclick = function () { focusItem(i); while (reveal()) { } };
    function set(v) { store.status[it.id] = store.status[it.id] === v ? undefined : v; save(); paint(); var n = drawSide(), s = main.querySelector("select.jump"); if (s) s.parentNode.replaceChild(n, s); drawProgress(); }
    function paint() {
      var v = store.status[it.id];
      c.classList.toggle("s-ok", v === "ok"); c.classList.toggle("s-redo", v === "redo");
      ok.classList.toggle("on", v === "ok"); redo.classList.toggle("on", v === "redo");
    }
    ok.onclick = function () { focusItem(i); set("ok"); };
    redo.onclick = function () { focusItem(i); set("redo"); };
    c.addEventListener("click", function () { focusItem(i); });
    c._next = function () { next.click(); }; c._all = function () { all.click(); }; c._ok = function () { ok.click(); }; c._redo = function () { redo.click(); };
    shown[it.id] = 0;
    paint();
    return c;
  }
  function cards() { return Array.prototype.slice.call(main.querySelectorAll(".card")); }
  function mark() { cards().forEach(function (c, i) { c.classList.toggle("cur", i === curItem); }); }
  function focusItem(i, scroll) {
    var cs = cards(); if (!cs.length) return;
    curItem = Math.max(0, Math.min(cs.length - 1, i)); mark();
    if (scroll) cs[curItem].scrollIntoView({ block: "start", behavior: "smooth" });
  }
  document.addEventListener("keydown", function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target.tagName; if (t === "INPUT" || t === "SELECT" || t === "TEXTAREA") return;
    var cs = cards(), c = cs[curItem], k = e.key.toLowerCase();
    if (t === "BUTTON" || t === "SUMMARY" || t === "A") { if (k === " " || k === "enter") return; }
    if (k === " ") { if (c) { e.preventDefault(); c._next(); } }
    else if (k === "a") { if (c) c._all(); }
    else if (k === "j") { focusItem(curItem + 1, true); }
    else if (k === "k") { focusItem(curItem - 1, true); }
    else if (k === "g") { if (c) c._ok(); }
    else if (k === "r") { if (c) c._redo(); }
  });

  function start() {
    D = window.LOCKIN;
    var h = (location.hash || "").slice(1);
    var ids = D.parts.map(function (p) { return p.id; });
    go(ids.indexOf(h) >= 0 ? h : (ids.indexOf(store.last) >= 0 ? store.last : ids[0]));
  }
  function load(v) {
    var s = document.createElement("script");
    s.src = "data.js?v=" + encodeURIComponent(v);
    s.onload = start;
    s.onerror = function () { main.innerHTML = "<p>Could not load the questions. Check your connection and reload.</p>"; };
    document.body.appendChild(s);
  }
  // version.json is fetched fresh each visit, so a new data file shows up straight away
  var done = false;
  function fallback() { if (!done) { done = true; load(Date.now()); } }
  try {
    fetch("version.json?t=" + Date.now(), { cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) { if (!done) { done = true; load(j.version); } }).catch(fallback);
    setTimeout(fallback, 4000);
  } catch (e) { fallback(); }
})();
