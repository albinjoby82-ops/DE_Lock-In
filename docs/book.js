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
          var n = allQs(d).length, done = doneCount(id, d);
          c.innerHTML = "<span class='n'>Topic " + id + "</span><h3>" + t[1] + "</h3>" +
            "<span class='w'>" + n + " questions, all worked · Mano " + MAP[id] + "</span>" +
            "<div class='prog'><i style='width:" + Math.round(100 * done / n) + "%'></i></div>" +
            "<div class='links'><a class='btn primary' href='book.html?t=" + id + "'>Open</a><a class='btn ghost' href='book.html?t=" + id + "&quiz=1&shuffle=1'>Shuffle quiz</a>" +
            "<span class='best'>" + done + " / " + n + " done</span></div>";
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
        location.href = "book.html?mock=" + ids.join(",") + "&n=" + document.getElementById("mockn").value + "&min=" + document.getElementById("mockmin").value;
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
      var qs = allQs(d);
      if (params.get("quiz")) {
        lede.innerHTML = d.intro + " <a href='book.html?t=" + t + "'>Back to the list</a>.";
        var list = params.get("shuffle") ? Q.shuffle(qs.slice()) : qs.slice();
        Q.runQuiz(holder, list, { key: "book" + t, onScore: function (q, s) { mark(t, q, s); } });
        return;
      }
      lede.innerHTML = d.intro + " ★ = answer in the back of the book.";
      var bar = el("div", { class: "bookbar" });
      var prog = el("span", { class: "score" });
      function upd() { prog.textContent = doneCount(t, d) + " / " + qs.length + " done"; }
      upd();
      bar.appendChild(el("a", { class: "btn primary", href: "book.html?t=" + t + "&quiz=1" }, "Do them as a quiz"));
      bar.appendChild(el("a", { class: "btn ghost", href: "book.html?t=" + t + "&quiz=1&shuffle=1" }, "Shuffled"));
      bar.appendChild(el("a", { class: "btn ghost", href: "book.html?mock=" + t + "&n=10&min=40" }, "Mock (this topic)"));
      var meta = Q.TOPICS.filter(function (x) { return x[0] === t; })[0];
      if (meta) bar.appendChild(el("a", { class: "btn ghost", href: Q.REPO + "notes/" + meta[2] + ".md" }, "Notes"));
      bar.appendChild(prog);
      holder.appendChild(bar);
      var jump = el("nav", { class: "jump" }, "Jump to: ");
      d.problems.forEach(function (p) { jump.appendChild(el("a", { href: "#p" + p.n.replace(".", "-") }, p.n)); });
      holder.appendChild(jump);
      d.problems.forEach(function (p) {
        var sec = el("section", { class: "prob", id: "p" + p.n.replace(".", "-") });
        sec.appendChild(el("h2", {}, "Problem " + p.n));
        sec.appendChild(el("p", { class: "ptext" }, p.text));
        p.qs.forEach(function (q) {
          var host = el("div", { class: "bq" });
          var prev = store.get(key(t, q));
          q._nofocus = true;
          Q.renderQuestion(q, host, function (s) { mark(t, q, s); upd(); host.classList.add("did"); });
          if (prev !== null && prev !== undefined) host.classList.add("did");
          sec.appendChild(host);
        });
        holder.appendChild(sec);
      });
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
      var pool = [];
      ids.forEach(function (id) {
        if (!data[id]) return;
        allQs(data[id]).forEach(function (q) { if (q.nomock) return; var c = Object.assign({}, q); c._topic = id + " · " + data[id].title; c._tid = id; pool.push(c); });
      });
      Q.shuffle(pool);
      // spread it out: at most 2 parts of the same book problem
      var per = {}, pick = [];
      pool.forEach(function (q) { var k = q._tid + q._p; if ((per[k] || 0) < 2 && pick.length < n) { per[k] = (per[k] || 0) + 1; pick.push(q); } });
      document.title = "Mock mid-term · DE Lock-In";
      title.textContent = "Mock mid-term";
      lede.innerHTML = pick.length + " book questions from topic" + (ids.length > 1 ? "s " : " ") + ids.join(", ") + " · " + mins + " minutes. " +
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
