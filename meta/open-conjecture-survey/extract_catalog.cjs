const fs = require('node:fs');
const assert = require('node:assert/strict');
const dir = __dirname;
const html = fs.readFileSync(`${dir}/catalog-page.html`, 'utf8');
const chunks = [...html.matchAll(/self\.__next_f\.push\((.*?)\)<\/script>/gs)]
  .map(m => JSON.parse(m[1])[1]).filter(s => typeof s === 'string');
const text = chunks.find(s => s.includes('"cards":['));
assert(text, 'Catalog cards missing');
const start = text.indexOf('"cards":[') + '"cards":'.length;
let depth = 0, quoted = false, escaped = false, end = -1;
for (let i = start; i < text.length; i++) {
  const c = text[i];
  if (quoted) {
    if (escaped) escaped = false;
    else if (c === '\\') escaped = true;
    else if (c === '"') quoted = false;
  } else if (c === '"') quoted = true;
  else if (c === '[' || c === '{') depth++;
  else if (c === ']' || c === '}') {
    depth--;
    if (depth === 0) { end = i + 1; break; }
  }
}
assert(end > start, 'Unclosed catalog array');
const cards = JSON.parse(text.slice(start, end));
assert.equal(cards.length, 307);
assert.equal(new Set(cards.map(x => x.key)).size, cards.length);
assert(cards.find(x => x.key === 'Erdos944.erdos_944').status === 'solved');
fs.writeFileSync(`${dir}/live-catalog.json`, JSON.stringify(cards, null, 2) + '\n');
const open = cards.filter(x => x.status === null || x.status === 'in_review');
fs.writeFileSync(`${dir}/live-open-catalog.txt`, open.map(x => `${x.key}\nhttps://conjectures.io${x.href}\n${x.summary}\nSTATUS: ${x.status}; attempts: ${x.attempts}\n`).join('\n'));
console.log(JSON.stringify({count: cards.length, statuses: cards.reduce((a,x) => {a[String(x.status)] = (a[String(x.status)]||0)+1; return a;}, {}), open: open.length}));
