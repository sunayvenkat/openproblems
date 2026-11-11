// Exact finite necessary conditions only; no exclusion of arbitrary numerator orbits.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

assert.equal(analyze(2, 4, [0, 1]).acyclic, true);
assert.equal(analyze(2, 4, [0, 1, 2, 3]).acyclic, false);
assert.equal(analyze(2, 4, [1]).eligible, false);

function gcd(a, b) { while (b) [a, b] = [b, a % b]; return a; }
function inverse(a, q) {
  if (q === 1) return 0;
  for (let b = 1; b < q; b++) if (a * b % q === 1) return b;
  throw new Error('Nonunit passed to modular inverse');
}
function polynomial(q, degree, k) {
  return Array.from({ length: q }, (_, n) => Number((BigInt(n) ** BigInt(degree) + BigInt(k)) % BigInt(q)));
}
function analyze(p, q, table) {
  assert.ok(Number.isInteger(q) && q > 1 && q <= 121);
  assert.ok(table.length && table.every(x => Number.isInteger(x) && 0 <= x && x < q));
  let power = q;
  while (power % p === 0) power /= p;
  assert.equal(power, 1);
  assert.ok([2, 3, 5, 11].includes(p));
  const eligible = table.some(x => x % p === 0) && table.some(x => x % p !== 0);
  if (!eligible) return { eligible: false, acyclic: null };
  let period = table.length;
  for (let d = 1; d <= table.length; d++) if (table.length % d === 0 &&
      table.every((x, i) => x === table[(i + d) % table.length])) { period = d; break; }
  const units = Array.from({ length: q }, (_, x) => x).filter(x => x % p !== 0);
  const edges = Array.from({ length: period * q }, () => []);
  const predecessors = Array.from({ length: period * q }, () => []);
  const vertices = [], remaining = new Int32Array(period * q), ranks = new Int32Array(period * q);
  for (let j = 0; j < period; j++) {
    const c = table[j], nextC = table[(j + 1) % period], g = gcd(c, q), step = q / g;
    const inv = inverse(c / g, step);
    for (const d of units) {
      const v = j * q + d; vertices.push(v);
      if ((d + nextC) % g !== 0) continue;
      const a0 = (d + nextC) / g * inv % step;
      for (let t = 0; t < g; t++) {
        const a = a0 + t * step;
        if (a % p === 0) continue;
        const w = ((j + 1) % period) * q + a * d % q;
        edges[v].push(w); predecessors[w].push(v);
      }
      remaining[v] = edges[v].length;
    }
  }
  const queue = vertices.filter(v => remaining[v] === 0);
  for (let i = 0; i < queue.length; i++) {
    const v = queue[i]; ranks[v] = Math.max(1, ranks[v]);
    for (const u of predecessors[v]) {
      ranks[u] = Math.max(ranks[u], ranks[v] + 1);
      if (--remaining[u] === 0) queue.push(u);
    }
  }
  const acyclic = queue.length === vertices.length;
  if (acyclic) for (const v of vertices) {
    assert.ok(ranks[v] > 0);
    for (const w of edges[v]) assert.ok(ranks[v] > ranks[w]);
  }
  return { eligible, acyclic, period, vertices, edges, ranks,
    states: vertices.length, transitions: vertices.reduce((s, v) => s + edges[v].length, 0),
    maxRank: Math.max(...ranks), unremoved: vertices.length - queue.length };
}

// Independent edge generation and DFS cycle check on all small fixtures.
for (const [p, q, degree] of [[2, 4, 2], [2, 4, 1], [3, 9, 3], [3, 9, 5], [5, 25, 5]])
  for (let k = 0; k < q; k++) {
    const table = polynomial(q, degree, k), result = analyze(p, q, table);
    assert.ok(result.eligible);
    const brute = Array.from({ length: result.period * q }, () => []);
    for (const v of result.vertices) {
      const j = Math.floor(v / q), d = v % q;
      for (let a = 1; a < q; a++) if (a % p &&
          (a * table[j] - d - table[(j + 1) % result.period]) % q === 0)
        brute[v].push(((j + 1) % result.period) * q + a * d % q);
      assert.deepEqual([...result.edges[v]].sort((a,b) => a-b), brute[v].sort((a,b) => a-b));
    }
    const color = new Uint8Array(brute.length);
    function cycle(v) {
      if (color[v] === 1) return true;
      if (color[v] === 2) return false;
      color[v] = 1;
      for (const w of brute[v]) if (cycle(w)) return true;
      color[v] = 2; return false;
    }
    assert.equal(result.acyclic, !result.vertices.some(cycle));
  }

const families = [
  { p: 2, q: 4, representatives: [2], degreeClass: 'Every even degree >=2' },
  { p: 3, q: 9, representatives: [3], degreeClass: 'Degrees ==3 modulo6' },
  { p: 3, q: 27, representatives: [5,11,17], degreeClass: 'Degrees ==5 modulo6' },
  { p: 5, q: 25, representatives: [3,7,11,15,19], degreeClass: 'Degrees ==3 modulo4' },
  { p: 11, q: 121, representatives: [13], degreeClass: 'Degrees ==13 modulo110, >=2' }
];
const results = [];
for (const family of families) {
  let cases = 0, states = 0, transitions = 0, maxRank = 0;
  for (const degree of family.representatives) for (let k = 0; k < family.q; k++) {
    const r = analyze(family.p, family.q, polynomial(family.q, degree, k));
    assert.ok(r.eligible && r.acyclic);
    cases++; states += r.states; transitions += r.transitions; maxRank = Math.max(maxRank, r.maxRank);
  }
  const result = { ...family, cases, states, transitions, maxRank, allAcyclic: true };
  results.push(result); console.log(JSON.stringify(result));
}
writeFileSync('erdos243-polynomial-results.json', JSON.stringify({
  scope: 'Necessary finite unit-state graphs for eventual C_n=n^d+k. An acyclic graph excludes only that polynomial pattern. The unrestricted Erdos243 problem is not solved.',
  controls: 'Explicit quadratic acyclic and linear cyclic fixtures; brute legal-edge enumeration and independent DFS on every offset for q=4,9 and a cyclic q=25 family; every acyclic production graph has all edges checked against a strictly decreasing integer rank.',
  completed: true, results
}, null, 2));
