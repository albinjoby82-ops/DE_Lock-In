(function () {
  "use strict";
  var KEY = "de-lockin-final-v1";
  var store = {};
  try { store = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { store = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {} }
  if (!store.status) store.status = {};

  // One thing on screen at a time. A section is a list of screens:
  // [intro / learn], then each question. A question is paged too:
  // page 0 = the question, 1..n = one step each, n+1 = answer + mark.
  var D, tab = "path", P = null, screens = [], si = 0, pg = 0, showAll = false;
  var $ = function (id) { return document.getElementById(id); };
  var head = $("head"), screen = $("screen"), foot = $("foot"), side = $("side"), tabs = $("tabs");

  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function btn(cls, text, fn) { var b = el("button", "btn " + cls, text); b.type = "button"; b.onclick = fn; return b; }
  function math(node) {
    if (window.renderMathInElement) {
      try { renderMathInElement(node, { delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }], throwOnError: false }); } catch (e) {}
    }
  }
  function parts(t) { return D.parts.filter(function (p) { return p.tab === t; }); }
  function counts(p) { var it = p.items || [], ok = 0; it.forEach(function (i) { if (store.status[i.id] === "ok") ok++; }); return [ok, it.length]; }

  function drawChrome() {
    tabs.innerHTML = "";
    [["path", "Exam path"], ["more", "More practice"]].forEach(function (t) {
      var b = el("button", "tab" + (tab === t[0] ? " on" : ""), t[1]); b.type = "button";
      b.onclick = function () { open(parts(t[0])[0].id); };
      tabs.appendChild(b);
    });
    var ok = 0, n = 0;
    parts("path").forEach(function (p) { var c = counts(p); ok += c[0]; n += c[1]; });
    $("prog").textContent = ok + " / " + n + " got";
    side.innerHTML = "";
    var sel = el("select", "jump"); sel.setAttribute("aria-label", "Jump to section");
    var last = null;
    parts(tab).forEach(function (p) {
      if (tab === "path" && p.kind !== last && (p.kind === "topic" || p.kind === "exam")) side.appendChild(el("div", "sep", p.kind === "exam" ? "Exams" : "Topics"));
      last = p.kind;
      var c = counts(p), b = el("button", p === P ? "on" : ""); b.type = "button";
      b.appendChild(el("span", "", p.title));
      if (c[1]) b.appendChild(el("span", "cnt" + (c[0] === c[1] ? " done" : ""), c[0] + "/" + c[1]));
      b.onclick = function () { open(p.id); };
      side.appendChild(b);
      var o = el("option", "", p.title + (c[1] ? "  (" + c[0] + "/" + c[1] + ")" : "")); o.value = p.id; o.selected = p === P;
      sel.appendChild(o);
    });
    sel.onchange = function () { open(sel.value); };
    return sel;
  }

  function open(id, at) {
    P = D.parts.filter(function (x) { return x.id === id; })[0] || D.parts[0];
    tab = P.tab;
    screens = [];
    if (P.html || P.intro || P.learn) screens.push({ kind: "intro" });
    (P.items || []).forEach(function (it) { screens.push({ kind: "q", it: it }); });
    si = Math.max(0, Math.min(screens.length - 1, at || 0)); pg = 0; showAll = false;
    draw();
  }

  function draw() {
    var s = screens[si];
    try { history.replaceState(null, "", "#" + P.id + (si ? "/" + si : "")); } catch (e) {}
    store.last = P.id; store.at = si; save();
    var sel = drawChrome();
    head.innerHTML = ""; head.appendChild(sel);
    var qn = (P.items || []).length;
    head.appendChild(el("div", "crumb", P.title + (P.freq ? " · " + P.freq : "")));
    if (screens.length > 1) {
      var dots = el("div", "dots");
      screens.forEach(function (x, i) {
        var st = x.kind === "q" ? store.status[x.it.id] : null;
        var label = x.kind === "intro" ? (P.learn ? "Learn" : "Intro") : String(i - (screens[0].kind === "intro" ? 0 : -1));
        var d = el("button", "dot" + (i === si ? " cur" : "") + (st ? " " + st : ""), label); d.type = "button";
        d.onclick = function () { si = i; pg = 0; showAll = false; draw(); };
        dots.appendChild(d);
      });
      head.appendChild(dots);
    }
    screen.innerHTML = ""; foot.innerHTML = "";
    var card = el("div", "card"); screen.appendChild(card);
    if (s.kind === "intro") drawIntro(card); else drawQ(card, s.it);
    math(card);
    screen.scrollTop = 0;
  }

  function nextScreen() {
    if (si < screens.length - 1) { si++; pg = 0; showAll = false; draw(); return; }
    var ps = parts(tab), ix = ps.indexOf(P);
    if (ix < ps.length - 1) open(ps[ix + 1].id);
  }
  function prevScreen() {
    if (si > 0) { si--; pg = 0; showAll = false; draw(); return; }
    var ps = parts(tab), ix = ps.indexOf(P);
    if (ix > 0) { open(ps[ix - 1].id); si = screens.length - 1; draw(); }
  }
  function isLast() { var ps = parts(tab); return si >= screens.length - 1 && ps.indexOf(P) >= ps.length - 1; }
  function isFirst() { var ps = parts(tab); return si === 0 && ps.indexOf(P) === 0; }

  function drawIntro(card) {
    card.appendChild(el("h1", "", P.title));
    if (P.html) card.appendChild(el("div", "", P.html));
    if (P.intro) card.appendChild(el("div", "", P.intro));
    if (P.learn) card.appendChild(el("div", "", P.learn));
    if (P.check) {
      var c = el("div", "check");
      c.appendChild(el("div", "q", "Quick check: " + P.check.q));
      var ans = el("div", "", P.check.a); ans.hidden = true;
      var b = btn("", "Show answer", function () { ans.hidden = !ans.hidden; b.textContent = ans.hidden ? "Show answer" : "Hide answer"; math(ans); });
      c.appendChild(b); c.appendChild(ans); card.appendChild(c);
    }
    if (P.id === "start") {
      var r = el("p", "small", "Progress is saved in this browser only. Content version " + D.version + ". ");
      var rb = btn("link", "Reset progress", function () { if (rb.dataset.sure) { store.status = {}; save(); draw(); } else { rb.dataset.sure = "1"; rb.textContent = "Tap again to wipe all progress"; } });
      r.appendChild(rb); card.appendChild(r);
    }
    var back = btn("", "← Back", prevScreen); back.disabled = isFirst();
    var go = btn("primary", screens.length > 1 ? "Start questions →" : "Next →", nextScreen); go.disabled = isLast();
    foot.appendChild(back); foot.appendChild(el("span", "grow")); foot.appendChild(go);
  }

  function drawQ(card, it) {
    var n = it.steps.length;
    if (it.src) card.appendChild(el("div", "src", it.src));
    card.appendChild(el("h1", "", it.title));
    function mark(v) { store.status[it.id] = v; save(); nextScreen(); if (isLast() && screens[si].it === it) draw(); }
    function forward() { if (pg <= n) { pg++; draw(); } }
    function backward() { if (showAll) { showAll = false; draw(); } else if (pg > 0) { pg--; draw(); } else prevScreen(); }
    var back = btn("", "← Back", backward); back.disabled = isFirst() && pg === 0;
    foot.appendChild(back);
    if (showAll) {
      card.appendChild(el("div", "prompt", it.prompt));
      var ol = el("ol", "allsteps");
      it.steps.forEach(function (s) { ol.appendChild(el("li", "", "<div>" + s["do"] + "</div>" + (s.why ? '<div class="why"><b class="w">Why:</b> ' + s.why + "</div>" : ""))); });
      card.appendChild(ol);
      if (it.answer) card.appendChild(el("div", "final", "<b>Answer:</b> " + it.answer));
      foot.appendChild(el("span", "grow"));
      foot.appendChild(btn("ok" + (store.status[it.id] === "ok" ? " on" : ""), "Got it", function () { mark("ok"); }));
      foot.appendChild(btn("redo" + (store.status[it.id] === "redo" ? " on" : ""), "Need to redo", function () { mark("redo"); }));
      return;
    }
    if (pg === 0) {
      card.appendChild(el("div", "prompt", it.prompt));
      card.appendChild(el("p", "hint", "Try it on paper first. " + n + " steps in the solution."));
      foot.appendChild(el("span", "grow"));
      foot.appendChild(btn("link", "Skip", nextScreen));
      foot.appendChild(btn("primary", "Show step 1 →", forward));
    } else if (pg <= n) {
      var d = el("details", "qq"); d.appendChild(el("summary", "", "Show the question")); d.appendChild(el("div", "prompt", it.prompt));
      d.addEventListener("toggle", function () { math(d); });
      card.appendChild(d);
      var s = it.steps[pg - 1];
      card.appendChild(el("div", "stepno", "Step " + pg + " of " + n));
      card.appendChild(el("div", "", s["do"]));
      if (s.why) card.appendChild(el("div", "why", '<b class="w">Why:</b> ' + s.why));
      foot.appendChild(el("span", "grow"));
      foot.appendChild(btn("link", "All steps", function () { showAll = true; draw(); }));
      foot.appendChild(btn("primary", pg < n ? "Next step →" : "Finish →", forward));
    } else {
      if (it.answer) card.appendChild(el("div", "final", "<b>Answer:</b> " + it.answer));
      card.appendChild(el("p", "", "How did it go?"));
      var row = el("div", "row");
      row.appendChild(btn("ok" + (store.status[it.id] === "ok" ? " on" : ""), "Got it", function () { mark("ok"); }));
      row.appendChild(btn("redo" + (store.status[it.id] === "redo" ? " on" : ""), "Need to redo", function () { mark("redo"); }));
      card.appendChild(row);
      card.appendChild(el("p", "hint", "Got it = you could do it again from a blank page. Either button moves you on."));
      foot.appendChild(el("span", "grow"));
      foot.appendChild(btn("link", "All steps", function () { showAll = true; draw(); }));
      var nx = btn("primary", "Next question →", nextScreen); nx.disabled = isLast();
      foot.appendChild(nx);
    }
    card._f = forward; card._b = backward; card._mark = mark;
  }

  document.addEventListener("keydown", function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey || !P) return;
    var t = e.target.tagName; if (t === "INPUT" || t === "SELECT" || t === "TEXTAREA") return;
    var k = e.key, s = screens[si], card = screen.firstChild;
    if ((k === " " || k === "Enter") && (t === "BUTTON" || t === "SUMMARY" || t === "A")) return;
    if (k === " " || k === "ArrowRight" || k === "Enter") { e.preventDefault(); if (s.kind === "q" && card._f && pg <= s.it.steps.length && !showAll) card._f(); else nextScreen(); }
    else if (k === "ArrowLeft") { e.preventDefault(); if (s.kind === "q" && card._b) card._b(); else prevScreen(); }
    else if (k === "j" || k === "J") { nextScreen(); }
    else if (k === "k" || k === "K") { prevScreen(); }
    else if (k === "a" || k === "A") { if (s.kind === "q") { showAll = !showAll; draw(); } }
    else if (k === "g" || k === "G") { if (s.kind === "q") card._mark("ok"); }
    else if (k === "r" || k === "R") { if (s.kind === "q") card._mark("redo"); }
  });

  function start() {
    D = window.LOCKIN;
    var h = (location.hash || "").slice(1).split("/"), ids = D.parts.map(function (p) { return p.id; });
    if (ids.indexOf(h[0]) >= 0) open(h[0], parseInt(h[1] || "0", 10) || 0);
    else if (ids.indexOf(store.last) >= 0) open(store.last, store.at || 0);
    else open(ids[0]);
  }
  function load(v) {
    var s = document.createElement("script");
    s.src = "data.js?v=" + encodeURIComponent(v);
    s.onload = start;
    s.onerror = function () { screen.innerHTML = '<div class="card">Could not load the questions. Check your connection and reload.</div>'; };
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
