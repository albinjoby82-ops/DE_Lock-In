(function () {
  "use strict";
  var Q = window.QUIZ, store = Q.store;
  // theme toggle
  var root = document.documentElement;
  var saved = store.get("theme");
  if (saved) root.setAttribute("data-theme", saved);
  var tb = document.getElementById("theme");
  if (tb) tb.addEventListener("click", function () {
    var dark = root.getAttribute("data-theme") ? root.getAttribute("data-theme") === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    var nt = dark ? "light" : "dark";
    root.setAttribute("data-theme", nt); store.set("theme", nt);
  });

  var params = new URLSearchParams(location.search);
  var holder = document.getElementById("quiz");

  // ---- index page
  var grid = document.getElementById("topics");
  if (grid) {
    var W = { "01": "●", "02": "●●●", "03": "●●", "04": "●●●", "05": "●", "06": "●●", "07": "●●", "08": "●●● biggest", "09": "●●●", "10": "●●", "11": "●●", "12": "●●" };
    var L = { "01": "L1", "02": "L2", "03": "L2", "04": "L3", "05": "L3", "06": "L4", "07": "L4–5", "08": "L5", "09": "L6", "10": "L7–8", "11": "L9", "12": "L10" };
    var pick = document.getElementById("pick");
    Q.TOPICS.forEach(function (t) {
      var best = store.get("best:" + t[0]);
      var c = document.createElement("div"); c.className = "tcard";
      c.innerHTML = "<span class='n'>Topic " + t[0] + " · " + L[t[0]] + "</span><h3>" + t[1] + "</h3><span class='w'>Exam weight " + W[t[0]] + "</span>" +
        "<div class='links'><a class='btn ghost' href='" + Q.REPO + "notes/" + t[2] + ".md'>Notes</a><a class='btn primary' href='quiz.html?t=" + t[0] + "'>Quiz</a>" +
        (best !== null && best !== undefined ? "<span class='best'>best " + best + "%</span>" : "") + "</div>";
      grid.appendChild(c);
      if (pick) {
        var lab = document.createElement("label");
        lab.innerHTML = "<input type='checkbox' value='" + t[0] + "'" + (t[0] === "01" || t[0] === "05" ? "" : " checked") + "> " + t[0] + " " + t[1];
        pick.appendChild(lab);
      }
    });
    var go = document.getElementById("mixgo");
    if (go) go.addEventListener("click", function () {
      var ids = Array.prototype.map.call(pick.querySelectorAll("input:checked"), function (i) { return i.value; });
      if (!ids.length) return;
      location.href = "quiz.html?mix=" + ids.join(",") + "&n=" + document.getElementById("mixn").value;
    });
    return;
  }

  // ---- quiz page
  if (!holder) return;
  var t = params.get("t"), mix = params.get("mix");
  var ids = t ? [t] : (mix ? mix.split(",") : []);
  if (!ids.length) { document.getElementById("title").textContent = "No topic picked"; return; }
  Q.load(ids, function (data) {
    var title = document.getElementById("title"), lede = document.getElementById("lede");
    if (t) {
      var d = data[t];
      if (!d) { title.textContent = "Topic " + t + " not found"; return; }
      document.title = "Topic " + t + ": " + d.title + " · DE Lock-In";
      title.textContent = "Topic " + t + ": " + d.title;
      var meta = Q.TOPICS.filter(function (x) { return x[0] === t; })[0];
      lede.innerHTML = (d.intro || "") + " <a href='" + Q.REPO + "notes/" + meta[2] + ".md'>Open the notes</a>.";
      Q.runQuiz(holder, d.qs.slice(), { key: t });
    } else {
      var n = +(params.get("n") || 15), pool = [];
      ids.forEach(function (id) { if (data[id]) data[id].qs.forEach(function (q) { var c = Object.assign({}, q); c._topic = id + " · " + data[id].title; pool.push(c); }); });
      var qs = Q.shuffle(pool).slice(0, n);
      document.title = "Mixed drill · DE Lock-In";
      title.textContent = "Mixed drill";
      lede.textContent = qs.length + " random questions from topics " + ids.join(", ") + ". Mixing topics is how the exam feels.";
      Q.runQuiz(holder, qs, {});
    }
  });
})();
