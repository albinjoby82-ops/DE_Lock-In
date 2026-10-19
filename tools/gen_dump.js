// node tools/gen_dump.js [n] -> JSON samples of every fresh-number generator, with the engine's verdict on its own answer
global.window = global;
global.localStorage = { getItem() { return null; }, setItem() {} };
const fs = require("fs"), path = require("path");
const docs = path.join(__dirname, "..", "docs");
require(path.join(docs, "gen.js"));
require(path.join(docs, "quiz.js"));
const Q = window.QUIZ, G = window.QUIZ_GEN, N = +(process.argv[2] || 150);
const store = {};
Q.add = (t) => { store[t.id] = t; };
for (const f of fs.readdirSync(path.join(docs, "data")).sort())
  eval(fs.readFileSync(path.join(docs, "data", f), "utf8").replace(/^QUIZ\.add/, "Q.add"));
const out = [];
const plain = (h) => String(h).replace(/<sup>(\d+)<\/sup>/g, "^$1").replace(/<[^>]+>/g, "").replace(/&nbsp;/g, " ");
for (const id of Object.keys(store).sort()) store[id].qs.forEach((q, i) => {
  if (!q.gen) return;
  if (!G[q.gen]) { out.push({ topic: id, i, gen: q.gen, error: "no such generator" }); return; }
  for (let k = 0; k < N; k++) {
    let v;
    try { v = G[q.gen](q.gp || {}); } catch (e) { out.push({ topic: id, i, gen: q.gen, error: String(e.stack) }); return; }
    const r = { topic: id, i, gen: q.gen, gp: q.gp || {}, type: v.type, q: plain(v.q), why: v.why };
    if (v.type === "text") r.ans = v.ans;
    if (v.type === "multi") r.fields = v.fields.map((f) => [plain(f.label), f.ans]);
    if (v.type === "mcq" || v.type === "tf") r.a = v.a, r.nopts = v.type === "tf" ? 2 : v.opts.length;
    if (v.type === "bool" || v.type === "kmap") {
      Q.ensureOnes(v);
      r.vars = v.vars; r.ones = v.ones; r.dc = v.dc || []; r.form = v.form || "any"; r.lits = v.lits; r.show = v.show;
      if (v.type === "bool") { r.verdict = Q.checkBool(v, v.show); r.showLits = Q.parseBool(v.show, v.vars).lits; }
    }
    if (v.type === "tt") r.vars = v.vars, r.outs = v.outs;
    out.push(r);
  }
});
console.log(JSON.stringify(out));
