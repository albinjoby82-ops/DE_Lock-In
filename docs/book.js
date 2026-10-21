/* DE Lock-In: Book questions (Mano & Ciletti, Digital Design 4th ed.) and the mock mid-term.
   Data files docs/book/NN.js call BOOK.add({...}); they are built by tools/build_book.py. */
(function () {
  "use strict";
  var Q = window.QUIZ, store = Q.store;
  var loaded = {};
  // Which end-of-chapter problems belong to which topic. READY = solutions written.
  var MAP = {
    "02": "1.1–1.10, 1.13", "03": "1.11, 1.12", "04": "1.14–1.21", "05": "1.22–1.34",
    "06": "1.35, 1.36, 2.1–2.9, 2.11–2.15, 2.18, 2.23–2.28, 3.27, 4.1, 4.2", "07": "2.10, 2.16, 2.17, 2.19–2.22",
    "08": "3.1–3.14, 3.26", "09": "3.15–3.25", "10": "3.28–3.30, 3.33, 4.4–4.21", "11": "4.22–4.30", "12": "4.3, 4.31–4.35"
  };
  var READY = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"];
  window.BOOK = { add: function (t) { loaded[t.id] = t; }, MAP: MAP, READY: READY };

  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    if (attrs) for (var k in attrs) { if (k === "class") e.className = attrs[k]; else e.setAttribute(k, attrs[k]); }
    if (html !== undefined) e.innerHTML = html;
    return e;
  }
  function load(ids, cb) {
    var left = ids.length;
    if (!left) { cb(loaded); return; }
    ids.forEach(function (id) {
      if (loaded[id]) { if (--left === 0) cb(loaded); return; }
      var s = document.createElement("script");
      s.src = "book/" + id + ".js";
      s.onload = s.onerror = function () { if (--left === 0) cb(loaded); };
      document.head.appendChild(s);
    });
  }
  BOOK.load = load;
  function allQs(d) { var out = []; d.problems.forEach(function (p) { p.qs.forEach(function (q) { q._p = p.n; out.push(q); }); }); return out; }
  function key(t, q) { return "book:" + t + ":" + q.tag; }
  function mark(t, q, s) { var old = store.get(key(t, q)); if (old === null || old === undefined || s > old) store.set(key(t, q), s); }
  function doneCount(t, d) { return allQs(d).filter(function (q) { var v = store.get(key(t, q)); return v !== null && v !== undefined; }).length; }
  function coreQs(d) {
    return allQs(d).filter(function (q) { return q.core; }).sort(function (a, b) { return (a.grp - b.grp) || (a.corder - b.corder); });
  }
  function isDone(t, q) { var v = store.get(key(t, q)); return v !== null && v !== undefined; }
  function topicName(t) { var m = Q.TOPICS.filter(function (x) { return x[0] === t; })[0]; return m ? m[1] : t; }

  /* ------------------------------------------------ index section */
  BOOK.renderIndex = function () {
    var grid = document.getElementById("bookgrid");
    if (!grid) return;
    load(READY, function (data) {
      Q.TOPICS.forEach(function (t) {
        var id = t[0];
        if (!MAP[id]) return;
        var d = data[id], c = el("div", { class: "tcard" + (d ? "" : " soon") });
        if (d) {
          var n = allQs(d).length, done = doneCount(id, d), cq = coreQs(d);
          var cdone = cq.filter(function (q) { return isDone(id, q); }).length;
          var ng = d.groups ? d.groups.length : 0;
          c.innerHTML = "<span class='n'>Topic " + id + " · Mano " + MAP[id] + "</span><h3>" + t[1] + "</h3>" +
            "<span class='w'>" + ng + " skill" + (ng === 1 ? "" : "s") + " · <b>" + cq.length + " core</b> + " + (n - cq.length) + " more practice</span>" +
            "<div class='prog' title='core done'><i style='width:" + Math.round(100 * cdone / Math.max(cq.length, 1)) + "%'></i></div>" +
            "<div class='links'><a class='btn primary' href='book.html?t=" + id + "&quiz=core'>Core path</a><a class='btn ghost' href='book.html?t=" + id + "'>Open</a>" +
            "<span class='best'>core " + cdone + " / " + cq.length + "</span></div>";
        } else {
          c.innerHTML = "<span class='n'>Topic " + id + "</span><h3>" + t[1] + "</h3><span class='w'>Mano " + MAP[id] + "</span>" +
            "<div class='links'><span class='tiny'>Solutions coming next</span></div>";
        }
        grid.appendChild(c);
      });
      var pick = document.getElementById("mockpick");
      READY.forEach(function (id) {
        var lab = el("label", {}, "<input type='checkbox' value='" + id + "' checked> " + id + " " + topicName(id));
        pick.appendChild(lab);
      });
      document.getElementById("mockgo").addEventListener("click", function () {
        var ids = Array.prototype.map.call(pick.querySelectorAll("input:checked"), function (i) { return i.value; });
        if (!ids.length) return;
        location.href = "book.html?mock=" + ids.join(",") + "&n=" + document.getElementById("mockn").value + "&min=" + document.getElementById("mockmin").value +
          (document.getElementById("mockcore").checked ? "&core=1" : "");
      });
      var hist = store.get("mockhist") || [];
      if (hist.length) {
        var h = document.getElementById("mockhist");
        h.innerHTML = "Last mocks: " + hist.slice(-5).reverse().map(function (r) { return "<b>" + r.pct + "%</b> (" + r.topics + ", " + r.n + " q, " + r.used + ")"; }).join(" · ");
      }
    });
  };

  /* ------------------------------------------------ book page */
  var holder = document.getElementById("book");
  if (!holder) return;
  var params = new URLSearchParams(location.search);
  var t = params.get("t"), mock = params.get("mock");
  var title = document.getElementById("title"), lede = document.getElementById("lede");

  if (t) {
    load([t], function (data) {
      var d = data[t];
      if (!d) { title.textContent = "No book questions for topic " + t + " yet"; lede.innerHTML = MAP[t] ? "Mano problems " + MAP[t] + ": solutions coming next." : ""; return; }
      document.title = "Book · Topic " + t + " · DE Lock-In";
      title.textContent = "Book questions · Topic " + t + ": " + d.title;
      var qs = allQs(d), groups = d.groups || [{ name: "All questions", blurb: "" }];
      var view = params.get("view") === "problem" || !d.groups ? "problem" : "skill";
      var quiz = params.get("quiz");
      if (quiz) {
        var list = quiz === "core" ? coreQs(d) : (params.get("shuffle") ? Q.shuffle(qs.slice()) : qs.slice());
        if (quiz === "core") list = list.map(function (q) { var c = Object.assign({}, q); c._from = "Skill " + (q.grp + 1) + " of " + groups.length + " · " + groups[q.grp].name; return c; });
        lede.innerHTML = (quiz === "core" ? "<b>Core path</b>: the " + list.length + " questions that cover every skill in this topic, in learning order. "
          + "Miss one? The same skill has more practice on the <a href='book.html?t=" + t + "'>topic page</a>." : d.intro + " <a href='book.html?t=" + t + "'>Back to the list</a>.");
        Q.runQuiz(holder, list, { key: quiz === "core" ? "bookcore" + t : "book" + t, onScore: function (q, s) { mark(t, q, s); } });
        return;
      }
      lede.innerHTML = d.intro + " ★ = answer in the back of the book.";
      var bar = el("div", { class: "bookbar" });
      var prog = el("span", { class: "score" });
      var cq = coreQs(d);
      function upd() {
        var cd = cq.filter(function (q) { return isDone(t, q); }).length;
        prog.textContent = "core " + cd + " / " + cq.length + " · all " + doneCount(t, d) + " / " + qs.length;
        holder.querySelectorAll("[data-gprog]").forEach(function (sp) {
          var gi = +sp.getAttribute("data-gprog");
          var gq = qs.filter(function (q) { return q.grp === gi; }), gc = gq.filter(function (q) { return q.core; });
          sp.textContent = "core " + gc.filter(function (q) { return isDone(t, q); }).length + "/" + gc.length + " · all " +
            gq.filter(function (q) { return isDone(t, q); }).length + "/" + gq.length;
        });
      }
      if (d.groups) bar.appendChild(el("a", { class: "btn primary", href: "book.html?t=" + t + "&quiz=core" }, "Core path (" + cq.length + ")"));
      bar.appendChild(el("a", { class: "btn ghost", href: "book.html?t=" + t + "&quiz=1&shuffle=1" }, "All " + qs.length + ", shuffled"));
      bar.appendChild(el("a", { class: "btn ghost", href: "book.html?mock=" + t + "&n=10&min=40" }, "Mock (this topic)"));
      var meta = Q.TOPICS.filter(function (x) { return x[0] === t; })[0];
      if (meta) bar.appendChild(el("a", { class: "btn ghost", href: Q.REPO + "notes/" + meta[2] + ".md" }, "Notes"));
      bar.appendChild(prog);
      holder.appendChild(bar);
      if (d.groups) {
        var tog = el("p", { class: "viewtog" });
        tog.innerHTML = view === "skill"
          ? "Grouped <b>by skill</b> · <a href='book.html?t=" + t + "&view=problem'>show by book problem number</a>"
          : "Grouped <b>by book problem</b> · <a href='book.html?t=" + t + "'>show by skill</a>";
        holder.appendChild(tog);
      }
      function card(q, into) {
        var host = el("div", { class: "bq" });
        q._nofocus = true;
        Q.renderQuestion(q, host, function (s) { mark(t, q, s); upd(); host.classList.add("did"); });
        if (isDone(t, q)) host.classList.add("did");
        into.appendChild(host);
      }
      if (view === "skill") {
        holder.appendChild(el("div", { class: "howto" },
          "<b>How to use this page:</b> work down the skills in order. Do the <b>core</b> questions of a skill on paper first. "
          + "All right? Move to the next skill. Missed one? Open <b>More practice</b> for that skill and do two or three more."));
        var jump = el("nav", { class: "jump" }, "Skills: ");
        groups.forEach(function (g, gi) { jump.appendChild(el("a", { href: "#g" + (gi + 1) }, (gi + 1) + " " + g.name)); });
        holder.appendChild(jump);
        groups.forEach(function (g, gi) {
          var sec = el("section", { class: "prob skill", id: "g" + (gi + 1) });
          var h = el("h2", {}, "<span class='gn'>" + (gi + 1) + "</span> " + g.name + " <span class='gprog' data-gprog='" + gi + "'></span>");
          sec.appendChild(h);
          if (g.blurb) sec.appendChild(el("p", { class: "ptext" }, g.blurb));
          var core = qs.filter(function (q) { return q.grp === gi && q.core; }).sort(function (a, b) { return a.corder - b.corder; });
          var more = qs.filter(function (q) { return q.grp === gi && !q.core; });
          sec.appendChild(el("p", { class: "tier" }, "Core"));
          core.forEach(function (q) { card(q, sec); });
          if (more.length) {
            var det = el("details", { class: "more" });
            det.appendChild(el("summary", {}, "More practice (" + more.length + ") · same skill, more reps"));
            var built = false;
            det.addEventListener("toggle", function () { if (det.open && !built) { built = true; more.forEach(function (q) { card(q, det); }); } });
            sec.appendChild(det);
          }
          holder.appendChild(sec);
        });
      } else {
        var jump2 = el("nav", { class: "jump" }, "Jump to: ");
        d.problems.forEach(function (p) { jump2.appendChild(el("a", { href: "#p" + p.n.replace(".", "-") }, p.n)); });
        holder.appendChild(jump2);
        d.problems.forEach(function (p) {
          var sec = el("section", { class: "prob", id: "p" + p.n.replace(".", "-") });
          sec.appendChild(el("h2", {}, "Problem " + p.n));
          sec.appendChild(el("p", { class: "ptext" }, p.text));
          p.qs.forEach(function (q) { card(q, sec); });
          holder.appendChild(sec);
        });
      }
      upd();
      var reset = el("button", { type: "button", class: "btn ghost" }, "Clear my ticks for this topic");
      reset.addEventListener("click", function () {
        if (!confirm("Clear the done ticks for topic " + t + "?")) return;
        qs.forEach(function (q) { store.set(key(t, q), null); });
        location.reload();
      });
      holder.appendChild(el("p", { class: "tiny" }, "Ticks stay in this browser only."));
      holder.appendChild(reset);
      if (location.hash) { var target = document.querySelector(location.hash); if (target) target.scrollIntoView(); }
    });
    return;
  }

  if (mock) {
    var ids = mock.split(","), n = +(params.get("n") || 12), mins = +(params.get("min") || 50);
    load(ids, function (data) {
      var coreOnly = !!params.get("core");
      // one bucket per (topic, skill); deal round-robin so every skill turns up before any repeats
      var buckets = {};
      ids.forEach(function (id) {
        if (!data[id]) return;
        allQs(data[id]).forEach(function (q) {
          if (q.nomock || (coreOnly && !q.core)) return;
          var c = Object.assign({}, q); c._topic = id + " · " + data[id].title; c._tid = id;
          var k = id + ":" + (q.grp === undefined ? 0 : q.grp);
          (buckets[k] = buckets[k] || []).push(c);
        });
      });
      var keys = Q.shuffle(Object.keys(buckets));
      keys.forEach(function (k) { Q.shuffle(buckets[k]); });
      var per = {}, pick = [], progress = true;
      while (pick.length < n && progress) {
        progress = false;
        keys.forEach(function (k) {
          if (pick.length >= n) return;
          while (buckets[k].length) {
            var q = buckets[k].shift(), pk = q._tid + q._p;
            if ((per[pk] || 0) >= 2) continue;
            per[pk] = (per[pk] || 0) + 1; pick.push(q); progress = true; break;
          }
        });
      }
      Q.shuffle(pick);
      document.title = "Mock mid-term · DE Lock-In";
      title.textContent = "Mock mid-term";
      lede.innerHTML = (coreOnly ? "Core questions only. " : "") + pick.length + " book questions, spread across every skill, from topic" + (ids.length > 1 ? "s " : " ") + ids.join(", ") + " · " + mins + " minutes. " +
        "Exam rules: paper and pen, no notes. Typed answers are checked; paper ones you mark yourself against the solution.";
      var start = el("div", { class: "mockstart" });
      var go = el("button", { type: "button", class: "btn primary" }, "Start the clock");
      start.appendChild(el("p", {}, "Get paper ready. The timer starts when you press the button."));
      start.appendChild(go);
      holder.appendChild(start);
      go.addEventListener("click", function () {
        holder.innerHTML = "";
        var clock = el("div", { class: "clock" });
        holder.appendChild(clock);
        var host = el("div");
        holder.appendChild(host);
        var t0 = Date.now(), end = t0 + mins * 60000, over = false, timer;
        function fmt(ms) { var s = Math.max(0, Math.round(ms / 1000)); return Math.floor(s / 60) + ":" + ("0" + s % 60).slice(-2); }
        function tick() {
          var left = end - Date.now();
          if (left <= 0 && !over) { over = true; clock.classList.add("up"); }
          clock.innerHTML = over ? "Time's up. Finish the question you're on, then press Finish." : "Time left <b>" + fmt(left) + "</b>";
        }
        tick(); timer = setInterval(tick, 1000);
        Q.runQuiz(host, pick, {
          onScore: function (q, s) { mark(q._tid, q, s); },
          onFinish: function (pct) {
            clearInterval(timer);
            var used = fmt(Date.now() - t0);
            clock.classList.remove("up");
            clock.innerHTML = "Finished in <b>" + used + "</b> of " + mins + ":00";
            var hist = store.get("mockhist") || [];
            hist.push({ pct: pct, topics: ids.join("+"), n: pick.length, used: used });
            store.set("mockhist", hist.slice(-20));
          }
        });
      });
    });
    return;
  }
  title.textContent = "Book questions";
  lede.innerHTML = "Pick a topic on the <a href='index.html#book-questions'>home page</a>.";
})();
