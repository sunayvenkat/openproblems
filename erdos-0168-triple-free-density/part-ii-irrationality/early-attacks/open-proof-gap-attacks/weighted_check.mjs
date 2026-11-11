// Exact finite checks for weighted.md; no floating-point optimization is used.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';

const source = new URL('../Open conjecture transfer search/168_exact_diagonal_results.json', import.meta.url);
const rows = JSON.parse(await fs.readFile(source, 'utf8')).exactDp;
const smooth = [];
for (let p2=1; p2<=rows.at(-1).t; p2*=2) {
  for (let d=p2; d<=rows.at(-1).t; d*=3) smooth.push(d);
}
assert.deepEqual(smooth.sort((a,b)=>a-b), rows.map(r=>r.t));
assert(rows.every((r,i)=>r.k===i+1));
const points = rows.map(({t}) => {
  let v = t, a = 0, b = 0;
  while (v % 2 === 0) { v /= 2; a++; }
  while (v % 3 === 0) { v /= 3; b++; }
  assert.equal(v, 1);
  return [t, a, b];
});
const popcount = x => { let count = 0; while (x) { x &= x - 1; count++; } return count; };

// Replay the exhaustive diagonal-mask recurrence already proved in 168_grid.md.
function exactTau(prefix) {
  const layers = new Map();
  for (const [, a, b] of prefix) {
    const k = a + b;
    if (!layers.has(k)) layers.set(k, []);
    layers.get(k).push(a);
  }
  const top = Math.max(...layers.keys());
  let left = Math.min(...layers.get(top));
  let width = layers.get(top).length;
  assert(width < 24);
  let dp = Array.from({length: 1 << width}, (_, mask) => popcount(mask));
  for (let k = top - 1; k >= 0; k--) {
    const nextLeft = left, nextWidth = width;
    left = Math.min(...layers.get(k));
    width = layers.get(k).length;
    assert(width < 24);
    assert.deepEqual([...layers.get(k)].sort((a,b) => a-b), Array.from({length: width}, (_, i) => left+i));
    const costs = Array(1 << width).fill(prefix.length + 1);
    for (let upper = 0; upper < dp.length; upper++) {
      const missing = (~(upper | (upper >> 1))) & ((1 << (nextWidth - 1)) - 1);
      const required = missing << (nextLeft - left);
      costs[required] = Math.min(costs[required], dp[upper]);
    }
    for (let bit = 0; bit < width; bit++) {
      const step = 1 << bit;
      for (let mask = 0; mask < costs.length; mask++) {
        if (mask & step) costs[mask] = Math.min(costs[mask], costs[mask ^ step]);
      }
    }
    dp = costs.map((cost, mask) => cost + popcount(mask));
  }
  return Math.min(...dp);
}

for (let i = 0; i < rows.length; i++) {
  assert.equal(exactTau(points.slice(0, i+1)), rows[i].tau, `prefix ${i+1}`);
}
const ds = rows.map(r => r.t);
const h = rows.map(r => r.k - 3*r.tau); // h=3g.
const delta = new Map(ds.map((d, i) => [d, h[i] - (i ? h[i-1] : 0)]));
assert([...delta.values()].every(a => a === 1 || a === -2));
const index = t => { let i = 0; while (i < ds.length && ds[i] <= t) i++; return i-1; };
const c = [0,0,0];
const colors = points.map(([,a,b]) => { c[(a+2*b)%3]++; return c.slice(); });
const endpoints = [10,5120,60,30720].map(t => ({t, h: h[index(t)], colors: colors[index(t)]}));
assert(endpoints.every(e => e.h === 1));
assert.deepEqual(endpoints.map(e => e.colors), [[3,2,2],[20,19,19],[6,5,5],[28,27,27]]);

const gcd = (a,b) => { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) [a,b] = [b,a%b]; return a; };
const rat = (a,b=1n) => { a=BigInt(a); b=BigInt(b); const k=gcd(a,b); return [a/k,b/k]; };
const add = (x,y) => rat(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
const mul = (x,y) => rat(x[0]*y[0],x[1]*y[1]);
const jumpSum = (l,r) => ds.reduce((s,d) => l<d && d<=r ? add(s,rat(delta.get(d),3n*BigInt(d))) : s,rat(0));
const low = jumpSum(10,60), high = jumpSum(5120,30720);
const defect = add(mul(rat(512),high),mul(rat(-1),low));
assert.deepEqual(low,rat(13,864));
assert.deepEqual(high,rat(45511,967458816));
assert.deepEqual(defect,rat(2135,236196));

// Check the finite reindexing behind the general return identity (2).
for (const Q of [3,6]) {
  const q=2**Q, R=256, scale=3**Math.floor(Math.log(q)/Math.log(3));
  const prefixZ=x=>mul(rat(3),jumpSum(0,x));
  const head=mul(rat(scale),add(mul(rat(q),prefixZ(q)),rat(-1)));
  assert.equal(head[1],1n);
  let events=rat(0);
  for (const d of ds.filter(d=>q<d && d<=q*R)) {
    const coefficient=delta.get(d)-(delta.get(d/q)||0);
    events=add(events,rat(BigInt(coefficient)*BigInt(scale*q),BigInt(d)));
  }
  const reindexed=mul(rat(scale),add(mul(rat(q),prefixZ(q*R)),mul(rat(-1),prefixZ(R))));
  assert.deepEqual(add(head,events),reindexed);
}

const interior = [157464,19683,5832,729].map(d => ({d,deltaH:delta.get(d)}));
assert.deepEqual(interior.map(x=>x.deltaH),[1,1,1,-2]);
assert.equal(interior[0].deltaH-interior[1].deltaH-interior[2].deltaH+interior[3].deltaH,-3);
assert.equal(delta.get(432),1);
assert.equal(delta.get(864),-2);
assert.deepEqual(add(rat(64,432),rat(-128,864)),rat(0));

export const result = {
  exactDpPrefixesReplayed: rows.length,
  lastPrefix: rows.at(-1),
  endpoints,
  low: low.map(String), high: high.map(String), weightedDefect: defect.map(String),
  interiorMixedJump: interior,
  boundaryCancellation: '64/432 - 128/864 = 0'
};
