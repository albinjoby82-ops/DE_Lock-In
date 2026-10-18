// node tools/dump.js -> JSON of every question, with ones resolved and the engine's verdict on the model answer
global.window = global;
global.localStorage = { getItem() { return null; }, setItem() {} };
const fs = require("fs"), path = require("path");
const docs = path.join(__dirname, "..", "docs");
require(path.join(docs, "quiz.js"));
const Q = window.QUIZ;
const store = {};
Q.add = (t) => { store[t.id] = t; };
for (const f of fs.readdirSync(path.join(docs, "data")).sort()) {
  eval(fs.readFileSync(path.join(docs, "data", f), "utf8").replace(/^QUIZ\.add/, "Q.add"));
}
const out = [];
for (const id of Object.keys(store).sort()) {
  store[id].qs.forEach((q, i) => {
    const r = { topic: id, i, type: q.type, q: q.q };
    if (q.type === "bool" || q.type === "kmap") {
      Q.ensureOnes(q);
      r.vars = q.vars; r.ones = q.ones; r.dc = q.dc || []; r.form = q.form || "any"; r.lits = q.lits; r.show = q.show;
      if (q.type === "bool") r.verdict = Q.checkBool(q, q.show);
      if (q.type === "bool") { try { r.showLits = Q.parseBool(q.show, q.vars).lits; } catch (e) { r.showLits = -1; } }
    }
    if (q.type === "mcq") r.nopts = q.opts.length, r.a = q.a;
    if (q.type === "tt") r.vars = q.vars, r.outs = q.outs;
    out.push(r);
  });
}
console.log(JSON.stringify(out));
