// Finite-field exploration only; no uniform covering theorem is asserted.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

const primes = process.argv.slice(2).map(Number);
if (!primes.length) primes.push(5, 7, 11, 17, 31, 59, 127, 251, 503);
const results = [];
function probe(p, width, controls = false) {
  assert.ok(Number.isInteger(p) && p > 3 && p < 10000);
  for (let d = 2; d * d <= p; d++) assert.notEqual(p % d, 0);
  const mod = x => (x % p + p) % p;
  const inv = new Int32Array(p), root = new Int32Array(p).fill(-1);
  const square = new Int32Array(p), cube = new Int32Array(p);
  for (let t = 1; t < p; t++) {
    square[t] = t * t % p; cube[t] = square[t] * t % p;
    root[square[t]] = t;
  }
  root[0] = 0;
  for (let t = 1; t < p; t++) inv[t] = t === 1 ? 1 : mod(-Math.floor(p / t) * inv[p % t]);
  let nonsquare = 2;
  while (root[nonsquare] >= 0) nonsquare++;
  const cubeClass = new Map();
  for (let t = 1; t < p; t++) {
    if (cubeClass.has(t)) continue;
    for (let x = 1; x < p; x++) cubeClass.set(t * cube[x] % p, t);
  }
  const colors = [...new Set(Array.from({ length: width }, (_, i) => [mod(i + 1), mod(-i - 1)]).flat())];
  assert.ok(colors.every(x => x !== 0));
  const curves = colors.map(a => Array.from({ length: p }, (_, t) => [a * t % p, a * square[t] % p, a * cube[t] % p]));
  const nonzeroU = new Uint8Array(p * p), zeroU = [new Uint8Array(p), new Uint8Array(p)], axis = new Set();
  function key(U, V, W) {
    if (U) {
      const z = inv[U], z2 = z * z % p;
      return [0, V * z2 % p + p * (W * z2 % p * z % p)];
    }
    if (V) {
      const cls = root[V] >= 0 ? 0 : 1;
      const z = inv[root[cls ? V * inv[nonsquare] % p : V]];
      return [cls + 1, W * (z * z % p) % p * z % p];
    }
    return [3, W ? cubeClass.get(W) : 0];
  }
  function mark(U, V, W) {
    const [kind, value] = key(U, V, W);
    if (!kind) nonzeroU[value] = 1;
    else if (kind < 3) { zeroU[kind - 1][value] = 1; zeroU[kind - 1][mod(-value)] = 1; }
    else axis.add(value);
  }
  mark(0, 0, 0);
  // Dilation normalizes any nonzero parameter to one; permute that summand first.
  for (let ai = 0; ai < colors.length; ai++) for (let bi = 0; bi < colors.length; bi++)
    for (let ci = bi; ci < colors.length; ci++) for (let x = 0; x < p; x++) {
      const b = curves[bi][x], u = colors[ai] + b[0], v = colors[ai] + b[1], w = colors[ai] + b[2];
      for (let y = bi === ci ? x : 0; y < p; y++) {
        const c = curves[ci][y]; mark((u + c[0]) % p, (v + c[1]) % p, (w + c[2]) % p);
      }
    }
  const missing = [];
  for (let V = 0; V < p; V++) for (let W = 0; W < p; W++)
    if (!nonzeroU[V + p * W]) missing.push([1, V, W]);
  for (let cls = 0; cls < 2; cls++) for (let W = 0; W < p; W++)
    if (!zeroU[cls][W] && W <= mod(-W)) missing.push([0, cls ? nonsquare : 1, W]);
  for (const W of new Set(cubeClass.values())) if (!axis.has(W)) missing.push([0, 0, W]);
  if (controls) {
    const A = [...new Map(curves.flat().map(v => [v.join(','), v])).values()];
    const encode = (U, V, W) => U + p * V + p * p * W;
    const seen = new Uint8Array(p ** 3), visited = new Uint8Array(p ** 3);
    for (const a of A) for (const b of A) for (const c of A) {
      const s = a.map((x, i) => mod(x + b[i] + c[i]));
      seen[encode(...s)] = 1;
    }
    const orbit = (U, V, W) => Array.from({ length: p - 1 }, (_, i) => {
      const s = i + 1;
      return encode(U * s % p, V * s % p * s % p, W * s % p * s % p * s % p);
    });
    const expected = new Set();
    for (let U = 0; U < p; U++) for (let V = 0; V < p; V++) for (let W = 0; W < p; W++) {
      if (visited[encode(U, V, W)]) continue;
      const points = orbit(U, V, W);
      assert.ok(points.every(n => seen[n] === seen[points[0]]));
      for (const n of points) visited[n] = 1;
      if (!seen[points[0]]) expected.add(Math.min(...points));
    }
    const actual = new Set(missing.map(v => Math.min(...orbit(...v))));
    assert.equal(actual.size, missing.length);
    assert.deepEqual(actual, expected);
  }
  return { p, width, colors: colors.length, missingOrbits: missing.length, missing };
}
for (const p of [5, 7, 17, 31]) probe(p, 2, true);
for (const p of primes) for (const width of [2, 3, 4]) {
  const r = probe(p, width); results.push(r);
  console.log(JSON.stringify({ ...r, missing: r.missing.slice(0, 12) }));
  writeFileSync('erdos1192-curves-results.json', JSON.stringify({ scope: 'Finite tested primes and color widths only; all dilation orbits are examined at each tested prime and missing orbits are reported. No asymptotic conclusion.', results }, null, 2));
}
