// Scalar affine synthesis with a cyclic AP-free modular marker.
// Every saved witness is finite; no infinite square avoidance is claimed.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

const depth = Number(process.argv[2] ?? 2), K = Number(process.argv[3] ?? 18);
const target = Number(process.argv[4] ?? 4096), nodeLimit = Number(process.argv[5] ?? 2000000);
const restarts = Number(process.argv[6] ?? 100);
const freeRoot = process.argv.includes('--free-root');
assert.ok(Number.isInteger(depth) && depth >= 1 && depth <= 3);
const L = 4 ** depth, scale = 3 ** depth;
assert.ok(Number.isInteger(K) && K >= 2 * scale && K <= 100);
assert.ok(Number.isInteger(target) && target > L && target * K * 4 < Number.MAX_SAFE_INTEGER);
assert.ok(Number.isInteger(nodeLimit) && nodeLimit > 0 && Number.isInteger(restarts) && restarts > 0);
function marker(n) {
  let result = 0, power = 1;
  for (let i = 0; i < depth; i++) { result += power * Number(n % 4 >= 2); n = Math.floor(n / 4); power *= 3; }
  return result;
}
const residues = Array.from({ length: L }, (_, r) => (marker((r + 1) % L) - marker(r) + scale) % scale);
for (let n = 0; n < L; n++) for (let d = 1; d < L; d++)
  assert.notEqual((marker(n) - 2 * marker((n + d) % L) + marker((n + 2 * d) % L)) % scale, 0);
const domains = residues.map(r => Array.from({ length: 2 * K + 1 }, (_, i) => i - K).filter(a => (a % scale + scale) % scale === r));
const restMin = Array(L + 1).fill(0), restMax = Array(L + 1).fill(0);
for (let r = L - 1; r >= 0; r--) { restMin[r] = restMin[r + 1] + domains[r][0]; restMax[r] = restMax[r + 1] + domains[r].at(-1); }
const rootImage = Array.from({ length: L }, (_, r) => marker((r + 1) % L) - marker(r));
assert.equal(rootImage[0], 0);
assert.equal(rootImage.reduce((a, b) => a + b, 0), 0);

function firstSquare(w) {
  const s = [0];
  for (let e = 1; e <= w.length; e++) {
    s[e] = s[e - 1] + w[e - 1];
    for (let d = 1; 2 * d <= e; d++) if (s[e] - 2 * s[e - d] + s[e - 2 * d] === 0) return { start: e - 2 * d, half: d, end: e };
  }
  return null;
}
assert.equal(firstSquare(rootImage), null);
let seed = 20261106;
function random() { seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5; return (seed >>> 0) / 4294967296; }
const images = new Map(), word = [], sums = [], deps = [];
const variableBit = (a, r) => a === 0 && (!freeRoot || r === 0) ? 0n : 1n << BigInt((a + K) * (L - 1) + r);
let nodes = 0, found = false, stopped = false, deadline = nodeLimit, runs = 0;
let best = { validPrefix: 1, word: [0], images: [[0, freeRoot ? [0, ...Array(L - 1).fill(null)] : rootImage]] };
let lastReported = 0;
function remember() {
  if (word.length <= best.validPrefix) return;
  best = { validPrefix: word.length, word: [...word], images: [...images].map(([a, w]) => [a, w.map(x => x ?? null)]) };
  if (word.length - lastReported >= 256) {
    lastReported = word.length;
    console.log(JSON.stringify({ nodes, runs, validPrefix: word.length, trackedLetters: images.size }));
  }
}
function extend() {
  while (!stopped && word.length < target) {
    const n = word.length, parent = Math.floor(n / L), r = n % L, a = word[parent];
    assert.ok(parent < n);
    if (!images.has(a)) images.set(a, Array(L).fill(undefined));
    const image = images.get(a);
    const previousSum = image.slice(0, r).reduce((s, x) => { assert.notEqual(x, undefined); return s + x; }, 0);
    if (r < L - 1 && image[r] === undefined) {
      const bit = variableBit(a, r);
      let conflict = deps[parent];
      // Domain exclusion by the sum constraint also depends on earlier image entries.
      for (let j = 0; j < r; j++) conflict |= variableBit(a, j);
      const choices = domains[r].filter(x => {
        const missing = scale * a - previousSum - x;
        return restMin[r + 1] <= missing && missing <= restMax[r + 1];
      });
      for (let i = choices.length - 1; i > 0; i--) { const j = Math.floor(random() * (i + 1)); [choices[i], choices[j]] = [choices[j], choices[i]]; }
      for (const x of choices) {
        if (nodes >= deadline) { stopped = true; return null; }
        nodes++;
        image[r] = x;
        const failed = extend();
        if (found) return null;
        image[r] = undefined;
        word.length = n; sums.length = n + 1; deps.length = n;
        if (stopped) return null;
        assert.equal(typeof failed, 'bigint');
        if ((failed & bit) === 0n) return failed;
        conflict |= failed & ~bit;
      }
      return conflict;
    }
    let value, dependency = deps[parent];
    if (r === L - 1 && (freeRoot || a !== 0)) {
      value = scale * a - previousSum;
      for (let j = 0; j < L - 1; j++) dependency |= variableBit(a, j);
      if (!domains[r].includes(value)) return dependency;
    } else {
      value = image[r];
      assert.notEqual(value, undefined);
      dependency |= variableBit(a, r);
    }
    assert.equal((value % scale + scale) % scale, residues[r]);
    sums[n + 1] = sums[n] + value;
    for (let half = L; 2 * half <= n + 1; half += L) {
      if (sums[n + 1] - 2 * sums[n + 1 - half] + sums[n + 1 - 2 * half] !== 0) continue;
      let conflict = dependency;
      for (let i = n + 1 - 2 * half; i < n; i++) conflict |= deps[i];
      return conflict;
    }
    word.push(value); deps.push(dependency);
    remember();
  }
  if (word.length === target) found = true;
  return null;
}
console.log(JSON.stringify({ controls: 'passed', depth, L, scale, K, target, nodeLimit, restarts, freeRoot }));
for (runs = 1; runs <= restarts; runs++) {
  images.clear(); images.set(0, freeRoot ? [0, ...Array(L - 1).fill(undefined)] : [...rootImage]);
  word.length = 0; word.push(0);
  sums.length = 0; sums.push(0, 0);
  deps.length = 0; deps.push(0n);
  stopped = false;
  deadline = Math.min(nodeLimit, nodes + Math.ceil(nodeLimit / restarts));
  extend();
  if (found || nodes >= nodeLimit) break;
}
assert.equal(firstSquare(best.word), null);
const witness = new Map(best.images);
for (let n = 1; n < best.word.length; n++) {
  const a = best.word[Math.floor(n / L)], r = n % L, image = witness.get(a);
  const value = r === L - 1 ? scale * a - image.slice(0, L - 1).reduce((s, x) => { assert.notEqual(x, null); return s + x; }, 0) : image[r];
  assert.equal(best.word[n], value);
}
const result = { scope: 'Bounded entry-by-entry synthesis with a modular marker and image-sum constraint. Dependency backjumping and randomized restarts are used. A finite witness does not prove infinite avoidance; no exhaustive exclusion is claimed.', depth, L, scale, K, target, nodeLimit, restarts, freeRoot, nodes, found, best };
writeFileSync(new URL(`./green15-marker-synthesis-results-${depth}-${K}${freeRoot ? '-free-root' : ''}.json`, import.meta.url), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ nodes, found, validPrefix: best.validPrefix, trackedLetters: best.images.length }));
