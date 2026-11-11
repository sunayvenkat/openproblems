import assert from 'node:assert/strict';

assert.equal(gcd(84n, 30n), 6n);
assert.equal(inverse(3n, 7n), 5n);
assert.equal(crtBlock([2n, 3n, 7n]), 26n);

const sample = orbit(11n, 29n);
assert.deepEqual(sample.rows.slice(0, 5).map(r => r.a), [4n, 9n, 56n, 2924n, 10684297n]);
assert(sample.terminated);

// Egyptian length can increase even at a step with a small relative numerator change.
const oldNumerator = 5098n, oldDenominator = 101n * 4997n;
const lengthMultiplier = 100n;
const newNumerator = lengthMultiplier * oldNumerator - oldDenominator;
const newDenominator = lengthMultiplier * oldDenominator;
assert.equal(gcd(oldNumerator, oldDenominator), 1n);
assert.equal(gcd(newNumerator, newDenominator), 1n);
assert.equal(newNumerator, 5103n);
assert.equal(newDenominator, 50469700n);
assert.equal(oldNumerator, 101n + 4997n);
assert.equal(oldDenominator - 99n * oldNumerator, -5n);
assert(1000n * (newNumerator - oldNumerator) < oldNumerator);
assert.equal(newDenominator, 2n ** 2n * 5n ** 2n * 19n * 101n * 263n);
let twoTermDivisorsChecked = 0;
for (let e2 = 0n; e2 <= 4n; e2++) for (let e5 = 0n; e5 <= 4n; e5++)
  for (let e19 = 0n; e19 <= 2n; e19++) for (let e101 = 0n; e101 <= 2n; e101++)
    for (let e263 = 0n; e263 <= 2n; e263++) {
      const divisor = 2n ** e2 * 5n ** e5 * 19n ** e19 * 101n ** e101 * 263n ** e263;
      // u/v = 1/x + 1/y would give (ux-v)(uy-v)=v^2 and ux-v == -v (mod u).
      assert.notEqual((divisor + newDenominator) % newNumerator, 0n);
      twoTermDivisorsChecked++;
    }
const auxiliary = 99n * oldDenominator;
const secondUnitDenominator = (auxiliary + 27n) / 5n;
const thirdUnitDenominator = (auxiliary + auxiliary * auxiliary / 27n) / 5n;
assert.equal(auxiliary * auxiliary % 27n, 0n);
assert.equal((auxiliary + 27n) % 5n, 0n);
assert.equal((auxiliary + auxiliary * auxiliary / 27n) % 5n, 0n);
assert.equal(auxiliary * (secondUnitDenominator + thirdUnitDenominator), 5n * secondUnitDenominator * thirdUnitDenominator);
assert.equal(newNumerator * 9900n * auxiliary, newDenominator * (auxiliary + 5n * 9900n));

const residueModulus = 5103n;
const liftedScale = 1222709419n, liftedMultiplier = 121047033277n;
const tinyMultiplier = 29719972n, tinyFirst = 29719973n, tinySecond = 441638367840389n;
for (const prime of [19n, 101n, 263n, liftedScale, liftedMultiplier, tinyMultiplier / 4n, tinyFirst, tinySecond]) {
  assert(prime > 2n && prime % 2n === 1n);
  for (let divisor = 3n; divisor * divisor <= prime; divisor += 2n) {
    assert.notEqual(prime % divisor, 0n);
  }
}
assert.equal(liftedScale, 1n + oldNumerator * 239841n);
assert.equal(liftedMultiplier, lengthMultiplier + oldDenominator * 239841n);
assert(liftedMultiplier > 20000000n * oldNumerator);
assert.equal(gcd(liftedMultiplier, oldDenominator * liftedScale), 1n);
assert.equal(liftedMultiplier * oldNumerator - oldDenominator * liftedScale, newNumerator);
assert.equal(tinyMultiplier * (tinyFirst + tinySecond) - tinyFirst * tinySecond, tinyFirst + tinySecond + 5n);
assert(10n ** 13n * 5n < tinyFirst + tinySecond);
const descentExamples = [];
for (const [multiplier, factors, numerator] of [
  [liftedMultiplier, [[19n, 1n], [101n, 1n], [263n, 1n], [liftedScale, 1n], [liftedMultiplier, 1n]], 5103n],
  [tinyMultiplier, [[2n, 2n], [tinyMultiplier / 4n, 1n], [tinyFirst, 1n], [tinySecond, 1n]], tinyFirst + tinySecond + 5n]
]) {
  const denominator = factors.reduce((product, [p, e]) => product * p ** e, 1n);
  assert.equal(numerator % residueModulus, 0n);
  let divisors = [1n];
  for (const [p, e] of factors) {
    const old = [...divisors];
    for (let exponent = 1n; exponent <= 2n * e; exponent++) for (const d of old) divisors.push(d * p ** exponent);
  }
  for (const d of divisors) assert.notEqual((d + denominator) % residueModulus, 0n);
  descentExamples.push({ multiplier: multiplier.toString(), nextNumerator: numerator.toString(),
    nextDenominator: denominator.toString(), twoTermDivisorsChecked: divisors.length });
}

let checked = 0;
let capped = 0;
let longest = 0;
for (let q = 1n; q <= 100n; q++) {
  for (let p = 1n; p <= q; p++) {
    if (gcd(p, q) !== 1n) continue;
    const result = orbit(p, q);
    checked++;
    capped += Number(!result.terminated);
    longest = Math.max(longest, result.rows.length);
  }
}

let a = 2n;
const moduli = [];
const blocks = [];
for (let width = 1; width <= 12; width++) {
  moduli.push(a);
  a = a * a - a + 1n;
  const start = crtBlock(moduli);
  for (let j = 0; j < width; j++) {
    assert.equal((start + BigInt(j)) % moduli[j], 0n);
  }
  blocks.push({ width, startDigits: start.toString().length });
}

const freshPrimes = [7n, 11n, 13n, 17n, 19n, 23n, 29n, 31n,
  37n, 41n, 43n, 47n, 53n, 59n, 61n, 67n];
const wheelBlocks = [];
for (const [wheel, width] of [[6n, 6], [6n, 12], [6n, 30], [30n, 30], [30n, 60]]) {
  const holes = Array.from({ length: width }, (_, j) => BigInt(j))
    .filter(j => gcd(j, wheel) === 1n);
  assert(holes.length <= freshPrimes.length);
  const selected = freshPrimes.slice(0, holes.length);
  const start = crtBlock([wheel, ...selected], [0n, ...holes.map(j => -j)]);
  const denominator = wheel * selected.reduce((p, m) => p * m, 1n);
  assert.equal(start % wheel, 0n);
  for (let i = 0; i < holes.length; i++) {
    assert.equal((start + holes[i]) % selected[i], 0n);
  }
  for (let j = 0n; j < BigInt(width); j++) {
    assert(gcd(start + j, denominator) > 1n);
  }
  assert.equal(holes.length, width * (wheel === 6n ? 1 / 3 : 4 / 15));
  wheelBlocks.push({ wheel: wheel.toString(), width, assignedModuli: holes.length });
}

const clusteredBlocks = [];
for (const wheel of [6n, 30n]) {
  const width = Number(wheel);
  const classes = Array.from({ length: width }, (_, j) => BigInt(j + 1)).filter(d => wheel % d === 0n);
  const positions = classes.map(d => Array.from({ length: width }, (_, j) => j).filter(j => gcd(BigInt(j), wheel) === d));
  const count = Math.max(...positions.map(list => list.length));
  const selected = freshPrimes.filter(p => gcd(p, wheel) === 1n).slice(0, count);
  const modulus = wheel * selected.reduce((product, b) => product * b, 1n);
  const base = modulus * modulus;
  for (let i = 0; i < classes.length; i++) {
    const targets = selected.map((_, j) => -BigInt(positions[i][j] ?? 0));
    const residue = crtBlock([wheel, ...selected], [0n, ...targets]);
    const start = base + residue;
    assert.equal(start % wheel, 0n);
    for (const [j, offset] of positions[i].entries()) {
      assert.equal(gcd(start + BigInt(offset), wheel), classes[i]);
      assert.equal((start + BigInt(offset)) % selected[j], 0n);
    }
    assert(start >= base && start + BigInt(width) < base + modulus + BigInt(width));
  }
  // A reuse contraction by at least 4/3 exits the entire cluster below its base.
  assert(3n * (base + modulus + 2n * BigInt(width)) < 4n * base);
  clusteredBlocks.push({ wheel: wheel.toString(), width, classes: classes.length, sharedFreshModuli: count });
}

console.log(JSON.stringify({
  checkedRationals: checked,
  cappedOrbits: capped,
  longestCheckedOrbit: longest,
  sampleDenominators: sample.rows.slice(0, 6).map(r => r.a.toString()),
  egyptianLengthCounterexample: { oldLength: 2, newLength: 3, twoTermDivisorsChecked,
    oldDenominators: ['101', '4997'], newDenominators: ['9900', secondUnitDenominator.toString(), thirdUnitDenominator.toString()] },
  strongerDescentCounterexamples: descentExamples,
  crtBlocks: blocks,
  wheelBlocks,
  clusteredBlocks,
  scope: 'Exact checks of finite arithmetic identities and CRT witnesses; no proof of an infinite orbit claim.'
}, null, 2));

function gcd(a, b) {
  while (b !== 0n) [a, b] = [b, a % b];
  return a;
}

function inverse(a, modulus) {
  let [r, nextR] = [a, modulus];
  let [s, nextS] = [1n, 0n];
  while (nextR !== 0n) {
    const q = r / nextR;
    [r, nextR] = [nextR, r - q * nextR];
    [s, nextS] = [nextS, s - q * nextS];
  }
  assert.equal(r, 1n);
  return (s % modulus + modulus) % modulus;
}

function crtBlock(moduli, targets = moduli.map((_, j) => -BigInt(j))) {
  let residue = 0n;
  let modulus = 1n;
  for (let j = 0; j < moduli.length; j++) {
    const b = moduli[j];
    const target = (targets[j] % b + b) % b;
    const step = ((target - residue) * inverse(modulus % b, b) % b + b) % b;
    residue += modulus * step;
    modulus *= b;
  }
  assert(0n <= residue && residue < modulus);
  return residue;
}

function orbit(p, q) {
  let C = p;
  let D = q;
  let L = q;
  let previousA;
  const rows = [];
  // shortcut: direct integers are capped; use Koizumi's modular method for longer orbit searches.
  for (let n = 0; n < 30 && D.toString(2).length <= 65536; n++) {
    const rounded = (2n * D + C) / (2n * C);
    const a = rounded + 1n;
    const E = D - rounded * C;
    const nextC = a * C - D;
    const nextD = a * D;
    const nextL = L / gcd(L, a) * a;
    const G = gcd(C, D);
    const nextG = gcd(nextC, nextD);
    const delta = D / L;
    const nextDelta = nextD / nextL;
    const U = C / delta;
    const V = E / delta;
    const nextU = nextC / nextDelta;
    const reuse = gcd(a, L);
    assert(C > 0n && nextC > 0n);
    assert(2n * E >= -C && 2n * E < C);
    assert.equal(nextC, C - E);
    assert.equal(nextG % G, 0n);
    assert.equal(G % delta, 0n);
    assert.equal(nextDelta, delta * gcd(a, L));
    assert.equal(E % delta, 0n);
    assert.equal(reuse * nextU, U - V);
    if (reuse >= 2n) assert(nextU < U);
    rows.push({ C, D, a, E, G, delta });
    if (previousA !== undefined && E === 0n && rows.at(-2).E === 0n) {
      assert.equal(a, previousA * previousA - previousA + 1n);
      return { rows, terminated: true };
    }
    previousA = a;
    [C, D, L] = [nextC, nextD, nextL];
  }
  return { rows, terminated: false };
}
