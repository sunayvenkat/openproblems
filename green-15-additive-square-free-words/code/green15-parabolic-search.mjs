// Bounded synthesis of scalar affine substitutions. No infinite claim from a prefix.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

const marker = process.argv.includes('--marker'), allRoots = process.argv.includes('--all-roots');
const parameter = Number(process.argv[2] ?? (marker ? 6 : 13));
const p = marker ? 4 : parameter, lambda = marker ? 3 : p - 2;
assert.ok(marker ? Number.isInteger(parameter) && parameter >= 3 && parameter <= 30 : Number.isInteger(p) && p >= 5 && p % 2 === 1 && p <= 31);
const slack = Number(process.argv[5] ?? 0), negativeRoot = process.argv.includes('--negative-root');
const backjump = process.argv.includes('--backjump');
const restarts = Number(process.argv.find(x => x.startsWith('--restarts='))?.split('=')[1] ?? 1);
assert.ok(Number.isInteger(restarts) && restarts >= 1 && restarts <= 10000);
assert.ok(Number.isInteger(slack) && slack >= 0 && slack <= 12);
assert.ok(!marker || (!negativeRoot && slack === 0));
const K = marker ? parameter : (p - 2 + slack) * (p - 1), target = Number(process.argv[3] ?? 4096);
const nodeLimit = Number(process.argv[4] ?? 500000);
assert.ok(Number.isInteger(target) && target > p && target * K * 4 < Number.MAX_SAFE_INTEGER);
assert.ok(Number.isInteger(nodeLimit) && nodeLimit > 0);
let seed = 20261106;
function random() {
  seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5;
  return (seed >>> 0) / 4294967296;
}
function square(word) {
  const sums = [0];
  for (let end = 1; end <= word.length; end++) {
    sums[end] = sums[end - 1] + word[end - 1];
    for (let half = 1; 2 * half <= end; half++)
      if (sums[end] - 2 * sums[end - half] + sums[end - 2 * half] === 0)
        return { start: end - 2 * half, half, end };
  }
  return null;
}
function slowSquare(word) {
  for (let end = 1; end <= word.length; end++) for (let half = 1; 2 * half <= end; half++) {
    let d = 0;
    for (let i = end - 2 * half; i < end - half; i++) d += word[i] - word[i + half];
    if (!d) return { start: end - 2 * half, half, end };
  }
  return null;
}
function options(a) {
  if (marker) {
    const residues = [[], [], []], result = [];
    for (let x = -K; x <= K; x++) residues[(x % 3 + 3) % 3].push(x);
    for (const b of residues[0]) for (const c of residues[1]) for (const d of residues[0]) {
      const e = 3 * a - b - c - d;
      if (Math.abs(e) > K || (e % 3 + 3) % 3 !== 2) continue;
      const image = [b, c, d, e];
      assert.equal(image.reduce((x, y) => x + y, 0), 3 * a);
      assert.equal(square(image), null);
      result.push(image);
    }
    return result;
  }
  const choices = new Map();
  const first = Math.floor(lambda * a / (p - 1)) - slack, last = Math.ceil(lambda * a / (p - 1)) + slack;
  for (let c = first; c <= last; c++) {
    const arc = Array.from({ length: p - 1 }, (_, r) => c + 2 * r - p + 2);
    const remainder = lambda * a - (p - 1) * c;
    for (const direction of [arc, [...arc].reverse()]) {
      const base = [...direction, remainder];
      assert.equal(base.length, p);
      assert.equal(base.reduce((x, y) => x + y, 0), lambda * a);
      assert.ok(base.every(Number.isInteger));
      if (!base.every(x => Math.abs(x) <= K)) continue;
      for (let offset = 0; offset < p; offset++) {
        const image = [...base.slice(offset), ...base.slice(0, offset)];
        if (!square(image)) choices.set(image.join(','), image);
      }
    }
  }
  return [...choices.values()];
}
for (let code = 0; code < 4096; code++) {
  let x = code;
  const word = Array.from({ length: 6 }, () => { const a = 2 * (x % 4) - 3; x = Math.floor(x / 4); return a; });
  assert.deepEqual(square(word), slowSquare(word));
}
const pools = new Map(Array.from({ length: 2 * K + 1 }, (_, i) => [i - K, options(i - K)]));
const root = negativeRoot ? -K : 0;
const rootImage = marker ? [0, 1, 0, -1] : negativeRoot
  ? [...Array.from({ length: p - 1 }, (_, r) => root + 2 * r), (p - 1) * slack]
  : [0, ...Array.from({ length: p - 1 }, (_, r) => 2 * r - p + 2)];
assert.ok(pools.get(root).some(w => w.join(',') === rootImage.join(',')));
assert.equal(square(rootImage), null);
const images = new Map([[root, rootImage]]), word = [root], sums = [0, root];
const dependencies = [0n];
const bits = new Map([...pools.keys()].map(a => [a, a === root ? 0n : 1n << BigInt(a + K)]));
let nodes = 0, found = false, stopped = false, best = { validPrefix: 1, images: [[root, rootImage]], word: [root] };
let currentNodeLimit = nodeLimit;
let lastReported = 0;
function remember() {
  if (word.length <= best.validPrefix) return;
  best = { validPrefix: word.length, images: [...images.entries()].map(([a, w]) => [a, [...w]]), word: [...word] };
  if (word.length - lastReported >= 100) {
    lastReported = word.length;
    console.log(JSON.stringify({ nodes, validPrefix: word.length, assignedLetters: images.size }));
  }
}
function extend() {
  while (!stopped && word.length < target) {
    const n = word.length, parent = Math.floor(n / p), offset = n % p, letter = word[parent];
    assert.ok(parent < n);
    if (!images.has(letter)) {
      let conflict = dependencies[parent];
      const letterBit = bits.get(letter);
      const choices = [...pools.get(letter)];
      for (let i = choices.length - 1; i > 0; i--) {
        const j = Math.floor(random() * (i + 1));
        [choices[i], choices[j]] = [choices[j], choices[i]];
      }
      for (const image of choices) {
        if (nodes >= currentNodeLimit) { stopped = true; return null; }
        nodes++;
        images.set(letter, image);
        const failed = extend();
        if (found) return null;
        images.delete(letter);
        word.length = n; sums.length = n + 1; dependencies.length = n;
        if (stopped) return null;
        if (backjump) {
          assert.equal(typeof failed, 'bigint');
          if ((failed & letterBit) === 0n) return failed;
          conflict |= failed & ~letterBit;
        }
      }
      return conflict;
    }
    const value = images.get(letter)[offset], end = n + 1;
    if (marker) assert.equal((value % 3 + 3) % 3, [0, 1, 0, 2][n % 4]);
    const dependency = dependencies[parent] | bits.get(letter);
    sums[end] = sums[end - 1] + value;
    for (let half = marker ? 4 : 1; 2 * half <= end; half += marker ? 4 : 1) {
      if (sums[end] - 2 * sums[end - half] + sums[end - 2 * half] !== 0) continue;
      let conflict = dependency;
      if (backjump) for (let i = end - 2 * half; i < n; i++) conflict |= dependencies[i];
      return conflict;
    }
    word.push(value);
    dependencies.push(dependency);
    remember();
  }
  if (word.length === target) found = true;
  return null;
}
const pattern = [0, 0, 1, 1];
for (let start = 0; start < 4; start++) for (let step = 1; step < 4; step++)
  assert.notEqual((pattern[start] - 2 * pattern[(start + step) % 4] + pattern[(start + 2 * step) % 4]) % 3, 0);
console.log(JSON.stringify({ controls: 'passed', p, lambda, K, slack, root, marker, allRoots, backjump, alphabetSize: pools.size,
  optionCount: { min: Math.min(...[...pools.values()].map(a => a.length)), max: Math.max(...[...pools.values()].map(a => a.length)) } }));
const rootChoices = allRoots ? [rootImage, ...pools.get(root).filter(w => w[0] === root && w.join(',') !== rootImage.join(','))] : [rootImage];
const runs = restarts > 1 ? Array.from({ length: restarts }, () => rootChoices[Math.floor(random() * rootChoices.length)]) : rootChoices;
let rootsTested = 0;
for (const image of runs) {
  rootsTested++;
  stopped = false;
  currentNodeLimit = Math.min(nodeLimit, nodes + Math.ceil(nodeLimit / restarts));
  images.clear(); images.set(root, image);
  word.length = 1; sums.length = 2; dependencies.length = 1;
  extend();
  if (found || nodes >= nodeLimit || (stopped && restarts === 1)) break;
}
assert.equal(square(best.word), null);
assert.ok(best.word.length === best.validPrefix);
const bestImages = new Map(best.images);
for (let n = 1; n < best.word.length; n++)
  assert.equal(best.word[n], bestImages.get(best.word[Math.floor(n / p)])[n % p]);
const result = { scope: marker
  ? 'Bounded synthesis of four-uniform substitutions on [-K,K] with image residues (0,1,0,2) modulo3 and image sum3*a. Root0 is prolongable. A finite prefix does not prove infinite avoidance, and a node cap does not prove exclusion.'
  : 'Bounded backtracking over rotations and reversals of rounded parabolic images. A finite square-free prefix is not an infinite proof; a node cap is not exhaustive exclusion.',
  p, lambda, K, slack, root, marker, allRoots, rootImageCount: rootChoices.length, rootsTested, restarts, backjump, target, nodeLimit, nodes, found, exhausted: restarts === 1 && !stopped && !found, best };
const filename = marker ? `./green15-marker-results-${K}${allRoots ? '-allroots' : ''}${backjump ? '-backjump' : ''}${restarts > 1 ? '-restarts' : ''}.json`
  : `./green15-parabolic-results-${p}${slack ? `-slack${slack}` : ''}${negativeRoot ? '-negative' : ''}${backjump ? '-backjump' : ''}${restarts > 1 ? '-restarts' : ''}.json`;
writeFileSync(new URL(filename, import.meta.url), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ nodes, found, exhausted: result.exhausted, validPrefix: best.validPrefix, assignedLetters: best.images.length }));
