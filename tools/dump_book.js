// node tools/dump_book.js -> JSON of every book question with the engine's verdict on the model answer
global.window = global;
global.localStorage = { getItem() { return null; }, setItem() {} };
const fs = require("fs"), path = require("path");
const docs = path.join(__dirname, "..", "docs");
require(path.join(docs, "quiz.js"));
const Q = window.QUIZ;
const store = {};
global.BOOK = { add: (t) => { store[t.id] = t; } };
for (const f of fs.readdirSync(path.join(docs, "book")).sort()) eval(fs.readFileSync(path.join(docs, "book", f), "utf8"));
const out = [];
for (const id of Object.keys(store).sort()) {
  for (const p of store[id].problems) for (const q of p.qs) {
    const r = { topic: id, tag: q.tag, type: q.type, why: q.why || "", q: q.q, svg: q.svg || null };
    if (q.type === "bool") {
      r.verdict = Q.checkBool(q, q.show); r.vars = q.vars; r.ones = q.ones; r.lits = q.lits || null; r.form = q.form || "any";
      r.showLits = Q.parseBool(q.show, q.vars).lits;
    }
    if (q.type === "tt") { r.vars = q.vars; r.outs = q.outs; }
    if (q.type === "multi") r.fields = q.fields.map(f => ({ label: f.label, first: f.ans[0], normOk: f.ans.every(a => Q.norm(a) !== "") }));
    out.push(r);
  }
}
console.log(JSON.stringify(out));
