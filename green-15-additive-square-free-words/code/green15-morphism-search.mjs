// Green 15 experiment: perturb Rao--Rosenfeld substitutions on six or eight letters.
// A square-free finite prefix, including a very long one, is not a proof.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

const six = [[0, 2, 4], [0, 3, 5], [1, 3, 5], [1, 3, 2], [0, 5, 4], [1, 2, 4]];
const forests = process.argv.includes('--forests');
const eight = forests || process.argv.includes('--eight');
const original = eight ? [[7], [6], [5], [4], [7, 2], [0, 2], [3, 1], [4, 1]] : six;
const alphabetSize = original.length, root = eight ? 4 : 0;
const hashWeights = [1, 67, 4489, 300763, 20151121, 1350125107, 4194301, 1048573].slice(0, alphabetSize);
const maxChanges = Number(process.argv[2] ?? 3);
assert.ok(Number.isInteger(maxChanges) && maxChanges >= 0 && maxChanges <= 5);
const output = { scope: forests
  ? 'All primitive non-erasing substitutions on eight letters with four images of length one and four images of length two, up to renaming. Unit-image cycles are impossible under primitivity; their acyclic forests have nineteen renaming classes. Each representative has all 64^4 completions covered by branching or sound pruning. Generated finite factors are checked; no infinite avoidance conclusion follows from a survivor.'
  : eight
  ? 'All substitutions obtained by at most maxChanges output-symbol replacements from the displayed eight-letter substitution, preserving image lengths, the first h in h(e), and the first e in h(h). The tested fixed point is that of h squared starting at e. Finite prefix checks only.'
  : 'Every substitution at Hamming distance at most maxChanges from the displayed 3-uniform substitution, keeping its first symbol a fixed. Finite prefix checks only.',
  spectralMethod: 'Exact Routh tests after a Cayley transform, with exact small rational shifts for singular tables. Exactly two expanding eigenvalues, counted with algebraic multiplicity, and no unit-modulus eigenvalues are pursued.',
  original, maxChanges, eight, tested: 0, valid81: 0, primitive81: 0, eligibleSpectrum: 0, shiftedSpectrum: 0, survivors: [], best: null, completed: false };

function square(word) {
  const n = word.length, hash = new Float64Array(n + 1);
  const parikh = Array.from({ length: alphabetSize }, () => new Int32Array(n + 1));
  assert.ok(n * Math.max(...hashWeights) * 4 < Number.MAX_SAFE_INTEGER);
  for (let end = 1; end <= n; end++) {
    const symbol = word[end - 1];
    hash[end] = hash[end - 1] + hashWeights[symbol];
    for (let a = 0; a < alphabetSize; a++) parikh[a][end] = parikh[a][end - 1] + Number(a === symbol);
    for (let half = 1; 2 * half <= end; half++) {
      if (hash[end] - 2 * hash[end - half] + hash[end - 2 * half] !== 0) continue;
      if (parikh.every(p => p[end] - 2 * p[end - half] + p[end - 2 * half] === 0))
        return { start: end - 2 * half, half, end };
    }
  }
  return null;
}
function slowSquare(word) {
  for (let end = 1; end <= word.length; end++) for (let half = 1; 2 * half <= end; half++) {
    const difference = Array(alphabetSize).fill(0);
    for (let i = end - 2 * half; i < end - half; i++) {
      difference[word[i]]++; difference[word[i + half]]--;
    }
    if (difference.every(x => x === 0)) return { start: end - 2 * half, half, end };
  }
  return null;
}
function expand(word, h) { return word.flatMap(a => h[a]); }
function incidence(h) { return Array.from({ length: h.length }, (_, i) => h.map(w => w.filter(x => x === i).length)); }
function gcd(a, b) { while (b) [a, b] = [b, a % b]; return Math.abs(a); }
function primitive(M) {
  const size = M.length;
  let distances;
  for (let root = 0; root < size; root++) {
    const seen = new Set([root]), stack = [root], distance = Array(size).fill(-1);
    distance[root] = 0;
    while (stack.length) {
      const from = stack.pop();
      for (let to = 0; to < size; to++) if (M[to][from] && !seen.has(to)) {
        seen.add(to); stack.push(to); distance[to] = distance[from] + 1;
      }
    }
    if (seen.size !== size) return false;
    if (root === 0) distances = distance;
  }
  let period = 0;
  for (let from = 0; from < size; from++) for (let to = 0; to < size; to++)
    if (M[to][from]) period = gcd(period, distances[from] + 1 - distances[to]);
  return period === 1;
}
function charpoly(M) {
  // Faddeev--LeVerrier; the small integer matrices keep every operation exact.
  const size = M.length;
  let B = Array.from({ length: size }, (_, i) => Array.from({ length: size }, (_, j) => Number(i === j)));
  const coefficients = [1];
  for (let k = 1; k <= size; k++) {
    B = M.map(row => Array.from({ length: size }, (_, j) => row.reduce((sum, x, t) => sum + x * B[t][j], 0)));
    assert.ok(B.flat().every(Number.isSafeInteger));
    const trace = B.reduce((sum, row, i) => sum + row[i], 0);
    assert.ok(trace % k === 0);
    const c = -trace / k;
    coefficients.push(c === 0 ? 0 : c);
    for (let i = 0; i < size; i++) B[i][i] += c;
  }
  assert.ok(B.flat().every(x => x === 0));
  return coefficients;
}
function determinant(A) {
  if (!A.length) return 1n;
  if (A.length === 1) return A[0][0];
  const B = A.map(row => [...row]);
  let sign = 1n, previous = 1n;
  for (let k = 0; k < B.length - 1; k++) {
    const pivotRow = B.findIndex((row, i) => i >= k && row[k] !== 0n);
    if (pivotRow < 0) return 0n;
    if (pivotRow !== k) { [B[k], B[pivotRow]] = [B[pivotRow], B[k]]; sign = -sign; }
    const pivot = B[k][k];
    for (let i = k + 1; i < B.length; i++) {
      for (let j = k + 1; j < B.length; j++) {
        const numerator = pivot * B[i][j] - B[i][k] * B[k][j];
        assert.equal(numerator % previous, 0n);
        B[i][j] = numerator / previous;
      }
      B[i][k] = 0n;
    }
    previous = pivot;
  }
  return sign * B.at(-1).at(-1);
}
function multiply(p, q) {
  const result = Array(p.length + q.length - 1).fill(0);
  p.forEach((a, i) => q.forEach((b, j) => result[i + j] += a * b));
  return result;
}
function routh(a) {
  const degree = a.length - 1;
  const hurwitz = [];
  for (let size = 1; size <= degree; size++) {
    const matrix = Array.from({ length: size }, (_, i) => Array.from({ length: size }, (_, j) =>
      a[2 * j - i + 1] ?? 0n));
    const d = determinant(matrix);
    if (d === 0n) return null;
    hurwitz.push(d);
  }
  const sign = x => x > 0 ? 1 : -1;
  const firstColumnSigns = [sign(a[0]), sign(hurwitz[0])];
  for (let i = 1; i < hurwitz.length; i++) firstColumnSigns.push(sign(hurwitz[i]) * sign(hurwitz[i - 1]));
  const outside = firstColumnSigns.slice(1).filter((s, i) => s !== firstColumnSigns[i]).length;
  return { outside, halfplane: a, hurwitz: hurwitz.map(String), firstColumnSigns };
}
function shifted(a, numerator, denominator) {
  const degree = a.length - 1, b = Array(a.length).fill(0n);
  for (let i = 0; i <= degree; i++) {
    let binomial = 1n;
    for (let m = 0; m <= degree - i; m++) {
      b[i + m] += a[i] * binomial * numerator ** BigInt(m) * denominator ** BigInt(degree - m);
      binomial = binomial * BigInt(degree - i - m) / BigInt(m + 1);
    }
  }
  return b;
}
function outsideUnitDisk(q) {
  const degree = q.length - 1;
  if (!degree) return { outside: 0, unitRoots: 0, halfplane: q, hurwitz: [] };
  const ascending = Array(degree + 1).fill(0);
  for (let i = 0; i <= degree; i++) {
    let term = [q[i]];
    for (let j = 0; j < degree - i; j++) term = multiply(term, [1, 1]);
    for (let j = 0; j < i; j++) term = multiply(term, [1, -1]);
    term.forEach((x, j) => ascending[j] += x);
  }
  const a = ascending.reverse().map(BigInt);
  // z=(1+s)/(1-s): outside the unit disk corresponds to Re(s)>0.
  if (!a[0] || !a.at(-1)) return { unitRoot: true };
  const direct = routh(a);
  if (direct) return { ...direct, halfplane: a.map(String), unitRoots: 0 };

  // Res_s(R(s),R(t-s)) has coefficient height at most K below.
  // Cauchy's root bound gives |Re(root)| >= 1/(2(1+K)) off the axis.
  const H = a.reduce((h, x) => x < -h ? -x : x > h ? x : h, 0n);
  let factorial = 1n;
  for (let i = 2; i <= 2 * degree; i++) factorial *= BigInt(i);
  const K = factorial * (H * 2n ** BigInt(degree + 1)) ** BigInt(2 * degree);
  const tries = degree * degree * (degree + 1) + 1;
  let denominator = 1n;
  while (denominator <= 4n * BigInt(tries) * (1n + K)) denominator *= 2n;
  // The finitely many Hurwitz minors at both shifts have total degree < tries.
  for (let j = 1; j <= tries; j++) {
    const right = routh(shifted(a, BigInt(j), denominator));
    const left = routh(shifted(a, -BigInt(j), denominator));
    if (!right || !left) continue;
    const unitRoots = left.outside - right.outside;
    assert.ok(unitRoots >= 0);
    return { outside: right.outside, unitRoots, halfplane: a.map(String),
      shift: { numerator: j, denominator: String(denominator), rightSigns: right.firstColumnSigns, leftSigns: left.firstColumnSigns } };
  }
  throw new Error('No nonsingular shifted Routh table within the polynomial degree bound');
}
function lowExpansion(coefficients) {
  // The six-letter uniform case has known Perron root 3. The eight-letter case does not.
  const quotient = eight ? [...coefficients] : [coefficients[0]];
  if (!eight) {
    for (let i = 1; i < coefficients.length; i++) quotient.push(coefficients[i] + 3 * quotient[i - 1]);
    assert.ok(quotient.pop() === 0);
  }
  while (quotient.length > 1 && quotient.at(-1) === 0) quotient.pop();
  const certificate = outsideUnitDisk(quotient);
  if (certificate.shift) output.shiftedSpectrum++;
  return certificate.outside === (eight ? 2 : 1) && certificate.unitRoots === 0 ? { quotient, ...certificate } : null;
}
function step(word, h) { const next = expand(word, h); return eight && !forests ? expand(next, h) : next; }
function inspect(h) {
  output.tested++;
  let word = [root];
  while (word.length < 81) {
    word = step(word, h);
    if (square(word.slice(0, 81))) return;
  }
  output.valid81++;
  const M = incidence(h);
  if (!primitive(M)) return;
  output.primitive81++;
  const coefficients = charpoly(M), spectrum = lowExpansion(coefficients);
  if (!spectrum) return;
  output.eligibleSpectrum++;
  while (true) {
    const found = square(word);
    if (found) {
      if (!output.best || found.end - 1 > output.best.validPrefix) {
        output.best = { h: h.map(w => [...w]), coefficients, spectrum, validPrefix: found.end - 1, checkedLength: word.length, found };
        console.log(JSON.stringify({ best: output.best }));
      }
      return;
    }
    if (word.length >= 6561) break;
    word = step(word, h);
  }
  const candidate = { h: h.map(w => [...w]), coefficients, spectrum, validPrefix: word.length };
  output.survivors.push(candidate);
  console.log(JSON.stringify({ candidate }));
}

// Independent literal Parikh counts test every length-six word on three letters.
for (let code = 0; code < 729; code++) {
  let x = code;
  const word = Array.from({ length: 6 }, () => { const a = x % 3; x = Math.floor(x / 3); return a; });
  assert.deepEqual(square(word), slowSquare(word));
}
assert.deepEqual(square([0, 1, 1, 0]), { start: 1, half: 1, end: 3 });
assert.deepEqual(square([0, 1, 2, 0, 2, 1]), { start: 0, half: 3, end: 6 });
assert.deepEqual(charpoly(incidence(six)), [1, -3, -3, 9, 0, 0, 0]);
assert.equal(primitive([[0, 1], [1, 0]]), false);
assert.equal(primitive([[1, 1], [1, 0]]), true);
function recursiveDet(A) {
  if (!A.length) return 1n;
  return A[0].reduce((sum, x, j) => sum + (j % 2 ? -x : x) *
    recursiveDet(A.slice(1).map(row => row.filter((_, k) => k !== j))), 0n);
}
for (let k = 0; k < 50; k++) {
  const A = Array.from({ length: 4 }, (_, i) => Array.from({ length: 4 }, (_, j) => BigInt((i * i + j * j + k * (i + 2 * j) + i * j * k) % 11 - 5)));
  assert.equal(determinant(A), recursiveDet(A));
}
const selectedM = incidence(original), selectedChar = charpoly(selectedM);
if (eight) {
  assert.equal(outsideUnitDisk(selectedChar).outside, 4);
  assert.equal(outsideUnitDisk(selectedChar).unitRoots, 0);
}
for (let x = 0; x <= alphabetSize; x++) {
  const A = selectedM.map((row, i) => row.map((a, j) => BigInt(Number(i === j) * x - a)));
  assert.equal(determinant(A), selectedChar.reduce((sum, a) => sum * BigInt(x) + BigInt(a), 0n));
}
// Known rational roots and conjugate pairs independently check the Routh signs.
const factors = [[1, -2], [1, 2], [2, -1], [2, 1], [2, 1, 1], [1, 1, 2]];
const outsideCounts = [1, 1, 0, 0, 0, 2];
for (let i = 0; i < factors.length; i++) for (let j = 0; j < factors.length; j++)
  for (let k = 0; k < factors.length; k++) {
    const q = multiply(multiply(factors[i], factors[j]), factors[k]);
    const result = outsideUnitDisk(q);
    if (result) assert.equal(result.outside, outsideCounts[i] + outsideCounts[j] + outsideCounts[k]);
  }
assert.equal(outsideUnitDisk([1, -1, -1]).outside, 1);
assert.equal(outsideUnitDisk([1, 0, -3]).outside, 2);
assert.equal(outsideUnitDisk([1, 0, 1]).unitRoots, 2);
assert.equal(outsideUnitDisk([3, 10, 3]).outside, 1);
let positive = [root];
while (positive.length < 6561) positive = step(positive, original);
assert.equal(square(positive), null);
console.log(JSON.stringify({ controls: 'passed', positiveControlLength: positive.length, selectedChar }));

const flat = original.flat();
const offsets = original.map((_, i) => original.slice(0, i).reduce((sum, w) => sum + w.length, 0));
const fixed = eight ? [4, 10] : [0];
const free = flat.map((_, i) => i).filter(i => !fixed.includes(i));
function mutations(next, remaining) {
  if (remaining === 0) { inspect(original.map((w, i) => flat.slice(offsets[i], offsets[i] + w.length))); return; }
  for (let index = next; index <= free.length - remaining; index++) {
    const p = free[index];
    const old = flat[p];
    for (let symbol = 0; symbol < alphabetSize; symbol++) if (symbol !== old) {
      flat[p] = symbol;
      mutations(index + 1, remaining - 1);
    }
    flat[p] = old;
  }
}
if (forests) {
  function permutations(a) {
    return a.length ? a.flatMap((x, i) => permutations(a.filter((_, j) => j !== i)).map(p => [x, ...p])) : [[]];
  }
  const ps = permutations([0, 1, 2, 3]), classes = new Map();
  let labeledForests = 0;
  for (let code = 0; code < 4096; code++) {
    let x = code;
    const unit = Array.from({ length: 4 }, () => { const a = x % 8; x = Math.floor(x / 8); return a; });
    let good = true;
    for (let start = 0; start < 4; start++) {
      const seen = new Set();
      let v = start;
      while (v < 4) { if (seen.has(v)) { good = false; break; } seen.add(v); v = unit[v]; }
      if (!good) break;
    }
    if (!good) continue;
    labeledForests++;
    let canonical = Infinity;
    for (const p of ps) for (const q of ps) {
      const renamed = [];
      for (let i = 0; i < 4; i++) renamed[p[i]] = unit[i] < 4 ? p[unit[i]] : 4 + q[unit[i] - 4];
      canonical = Math.min(canonical, renamed.reduce((a, b) => 8 * a + b, 0));
    }
    const representative = classes.get(canonical) ?? { unit: Array.from({ length: 4 }, (_, i) => Math.floor(canonical / 8 ** (3 - i)) % 8), orbitSize: 0 };
    representative.orbitSize++;
    classes.set(canonical, representative);
  }
  assert.equal(labeledForests, 2048);
  assert.equal(classes.size, 19);
  output.unitForests = [...classes.values()];
  output.coveredCompletions = 0;
  output.partialNodes = 0;
  output.squarePrunedCompletions = 0;
  output.closedAlphabetPrunedCompletions = 0;
  output.positiveControlVisited = 0;
  const knownGood = [[4], [5], [6], [7], [7, 1], [3, 1], [0, 2], [4, 2]];
  assert.deepEqual(charpoly(incidence(knownGood)), selectedChar);
  function visit(h) {
    output.partialNodes++;
    const missing = h.slice(4).filter(w => !w).length;
    if (!missing) {
      if (h.every((w, i) => w.join(',') === knownGood[i].join(','))) output.positiveControlVisited++;
      inspect(h);
      output.coveredCompletions++;
      return;
    }
    const compatibleControl = h.every((w, i) => !w || w.join(',') === knownGood[i].join(','));
    function prune(reason) {
      assert.ok(!compatibleControl, 'A verified square-free primitive control was pruned');
      const completions = 64 ** missing;
      output.coveredCompletions += completions;
      output[reason] += completions;
    }
    const seen = new Set([4]), pending = [4];
    let reachableUnknown = false;
    while (pending.length) {
      const a = pending.pop();
      if (!h[a]) { reachableUnknown = true; continue; }
      for (const b of h[a]) if (!seen.has(b)) { seen.add(b); pending.push(b); }
    }
    if (!reachableUnknown) { assert.ok(seen.size < 8); prune('closedAlphabetPrunedCompletions'); return; }
    let word = [4];
    for (let iteration = 0; iteration < 9; iteration++) {
      const next = [];
      for (const a of word) {
        if (!h[a]) {
          if (square(next)) { prune('squarePrunedCompletions'); return; }
          for (let b = 0; b < 8; b++) for (let c = 0; c < 8; c++) {
            h[a] = [b, c];
            visit(h);
          }
          h[a] = null;
          return;
        }
        next.push(...h[a]);
      }
      if (square(next)) { prune('squarePrunedCompletions'); return; }
      word = next;
    }
    throw new Error('A reachable undefined image was not requested within eight graph steps');
  }
  for (const representative of output.unitForests) {
    const before = output.coveredCompletions;
    visit([...representative.unit.map(a => [a]), null, null, null, null]);
    assert.equal(output.coveredCompletions - before, 64 ** 4);
    console.log(JSON.stringify({ unit: representative.unit, coveredCompletions: output.coveredCompletions, partialNodes: output.partialNodes, fullAssignmentsInspected: output.tested, valid81: output.valid81, primitive81: output.primitive81, eligibleSpectrum: output.eligibleSpectrum, survivors: output.survivors.length }));
  }
  assert.equal(output.coveredCompletions, 19 * 64 ** 4);
  assert.equal(output.positiveControlVisited, 1);
} else {
  for (let distance = 0; distance <= maxChanges; distance++) {
    mutations(0, distance);
    console.log(JSON.stringify({ distance, tested: output.tested, valid81: output.valid81, primitive81: output.primitive81, eligibleSpectrum: output.eligibleSpectrum, shiftedSpectrum: output.shiftedSpectrum, survivors: output.survivors.length }));
  }
  let expected = 0, binomial = 1;
  for (let d = 0; d <= maxChanges; d++) {
    expected += binomial * (alphabetSize - 1) ** d;
    binomial = binomial * (free.length - d) / (d + 1);
  }
  assert.equal(output.tested, expected);
}
output.completed = true;
writeFileSync(new URL(forests ? './green15-forest-results.json' : `./green15-morphism${eight ? '-eight' : ''}-results-${maxChanges}-routh-exact.json`, import.meta.url), JSON.stringify(output, null, 2) + '\n');
