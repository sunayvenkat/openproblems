import fs from 'node:fs';
import assert from 'node:assert/strict';

// Test the proposed universal transfer: 4AP-free order implies a 2-colorable 3AP hypergraph.
let seed = 196197;
function rand(n) { seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5; return (seed >>> 0) % n; }
function triples(a) {
  const index = new Map(a.map((x, i) => [x, i]));
  const out = [];
  for (let i = 0; i < a.length; ++i) for (let j = i + 1; j < a.length; ++j) {
    const k = index.get(2 * a[j] - a[i]);
    if (k !== undefined) out.push([i, j, k]);
  }
  return out;
}
function colorable(a) {
  const edges = triples(a), degree = Array(a.length).fill(0);
  for (const e of edges) for (const x of e) ++degree[x];
  const solve = colors => {
    let changed;
    do {
      changed = false;
      for (const e of edges) {
        let zero = 0, one = 0, unknown = -1;
        for (const x of e) if (colors[x] === 0) ++zero; else if (colors[x] === 1) ++one; else unknown = x;
        if (zero === 3 || one === 3) return false;
        if (unknown >= 0 && (zero === 2 || one === 2)) { colors[unknown] = zero === 2 ? 1 : 0; changed = true; }
      }
    } while (changed);
    let v = -1;
    for (let i = 0; i < a.length; ++i) if (colors[i] < 0 && (v < 0 || degree[i] > degree[v])) v = i;
    if (v < 0) return true;
    for (let c = 0; c < 2; ++c) { const next = colors.slice(); next[v] = c; if (solve(next)) return true; }
    return false;
  };
  const start = Array(a.length).fill(-1); if (a.length) start[0] = 0;
  return solve(start);
}
function noFour(a) {
  const set = new Set(a);
  return !a.some(x => a.some(y => y > x && set.has(2 * y - x) && set.has(3 * y - 2 * x)));
}
assert(colorable([1, 2, 3, 4, 5, 6, 7, 8]));
assert(!colorable([1, 2, 3, 4, 5, 6, 7, 8, 9]));
assert(!noFour([1, 2, 3, 4]));
assert(noFour([1, 2, 3, 5]));

for (const n of [100, 200, 400, 800, 1600]) for (let trial = 0; trial < 20; ++trial) {
  const order = Array.from({length:n}, (_, i) => i + 1);
  for (let i = n - 1; i > 0; --i) { const j = rand(i + 1); [order[i], order[j]] = [order[j], order[i]]; }
  const set = new Set();
  for (const x of order) {
    let bad = false;
    for (let d = 1; d < n && !bad; ++d) for (let pos = 0; pos < 4; ++pos) {
      const start = x - pos * d;
      if (start < 1 || start + 3 * d > n) continue;
      if ([0, 1, 2, 3].every(k => k === pos || set.has(start + k * d))) { bad = true; break; }
    }
    if (!bad) set.add(x);
  }
  let a = [...set].sort((x,y) => x-y);
  assert(noFour(a));
  const ok = colorable(a);
  process.stdout.write(JSON.stringify({n, trial, size:a.length, edges:triples(a).length, colorable:ok}) + '\n');
  if (!ok) {
    for (let i = a.length - 1; i >= 0; --i) { const b = a.filter((_,j) => i !== j); if (!colorable(b)) a = b; }
    assert(noFour(a)); assert(!colorable(a));
    const result = {values:a, triples:triples(a).map(e => e.map(i => a[i])), noFour:true, twoColorable:false};
    fs.writeFileSync(new URL('./196_197_obstruction.json', import.meta.url), JSON.stringify(result,null,2));
    process.stdout.write(JSON.stringify(result) + '\n');
    process.exit(0);
  }
}
