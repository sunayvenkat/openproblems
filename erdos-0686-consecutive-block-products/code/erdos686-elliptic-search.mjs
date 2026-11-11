import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

const abs = n => n < 0n ? -n : n;
function gcd(a, b) {
  a = abs(a); b = abs(b);
  while (b) [a, b] = [b, a % b];
  return a;
}
function rational(n, d = 1n) {
  assert(d !== 0n);
  if (d < 0n) { n = -n; d = -d; }
  const g = gcd(n, d);
  return [n / g, d / g];
}
const add = (x, y) => rational(x[0] * y[1] + y[0] * x[1], x[1] * y[1]);
const neg = x => [-x[0], x[1]];
const sub = (x, y) => add(x, neg(y));
const mul = (x, y) => rational(x[0] * y[0], x[1] * y[1]);
const div = (x, y) => rational(x[0] * y[1], x[1] * y[0]);
const scale = (x, n) => rational(x[0] * n, x[1]);
const constant = n => [BigInt(n), 1n];
const equal = (x, y) => x[0] === y[0] && x[1] === y[1];
const point = (x, y) => [constant(x), constant(y)];
const negativePoint = P => P === null ? null : [P[0], neg(P[1])];

function onCurve(P) {
  if (P === null) return true;
  const [x, y] = P;
  return equal(mul(y, y), add(sub(mul(mul(x, x), x), scale(x, 1875n)), constant(391250)));
}

function sumPoints(P, Q) {
  if (P === null) return Q;
  if (Q === null) return P;
  let slope;
  if (equal(P[0], Q[0])) {
    if (equal(P[1], neg(Q[1]))) return null;
    assert(equal(P[1], Q[1]));
    slope = div(sub(scale(mul(P[0], P[0]), 3n), constant(1875)), scale(P[1], 2n));
  } else {
    slope = div(sub(Q[1], P[1]), sub(Q[0], P[0]));
  }
  const x = sub(sub(mul(slope, slope), P[0]), Q[0]);
  const y = sub(mul(slope, sub(P[0], x)), P[1]);
  return [x, y];
}

function toCubic(P) {
  if (P === null || P[1][0] === 0n) return null;
  return [div(scale(sub(P[0], constant(1)), 25n), P[1]),
    div(sub(P[0], constant(625)), P[1])];
}

function fromCubic(x, y) {
  const d = sub(x, scale(y, 25n));
  if (d[0] === 0n) return null;
  return [add(constant(625), div(scale(y, 15600n), d)), div(constant(15600), d)];
}

function cubicIdentity([x, y]) {
  return equal(sub(mul(mul(x, x), x), x), scale(sub(mul(mul(y, y), y), y), 25n));
}

const P = point(1, 624), Q = point(25, 600);
assert(onCurve(P) && onCurve(Q));
assert.deepEqual(sumPoints(P, Q), point(-25, -650));
assert.deepEqual(sumPoints(Q, Q), point(-50, -600));
assert.deepEqual(sumPoints(P, sumPoints(Q, Q)), point(625, -15600));
assert.equal(sumPoints(P, negativePoint(P)), null);
for (let x = -1; x <= 1; x++) for (let y = -1; y <= 1; y++) {
  const c = [constant(x), constant(y)], E = fromCubic(...c);
  assert(onCurve(E));
  if (E !== null) assert.deepEqual(toCubic(E), c);
}

// This box is a subgroup search, not a claim that P,Q generate the full rational-point group.
const bound = Number(process.argv[2] ?? 12);
assert(Number.isSafeInteger(bound) && bound >= 1 && bound <= 50);
function multiples(R) {
  const list = new Map([[0, null]]);
  for (let j = 1; j <= bound; j++) {
    const S = sumPoints(list.get(j - 1), R);
    list.set(j, S); list.set(-j, negativePoint(S));
  }
  return list;
}
const pMultiples = multiples(P), qMultiples = multiples(Q);
const report = { coefficientBound: bound, checkedPoints: 0, distinctPoints: 0,
  largestCoordinateDigits: 0, integralPairs: [], candidate: null };
const seen = new Set();
search: for (let i = -bound; i <= bound; i++) {
  for (let j = -bound; j <= bound; j++) {
    const R = sumPoints(pMultiples.get(i), qMultiples.get(j));
    assert(onCurve(R));
    const c = toCubic(R);
    if (c === null) continue;
    assert(cubicIdentity(c));
    assert.deepEqual(fromCubic(...c), R);
    report.checkedPoints++;
    seen.add(R.flat().map(String).join('/'));
    report.largestCoordinateDigits = Math.max(report.largestCoordinateDigits,
      ...c.flat().map(n => abs(n).toString().length));
    if (c.every(t => t[1] === 1n)) {
      const [x, y] = c.map(t => t[0]);
      report.integralPairs.push({ i, j, x: String(x), y: String(y) });
      if (y >= 2n && x >= y + 3n) {
        const n = y - 2n, m = x - 2n;
        assert.equal((m + 1n) * (m + 2n) * (m + 3n),
          25n * (n + 1n) * (n + 2n) * (n + 3n));
        report.candidate = { k: 3, n: String(n), m: String(m) };
        break search;
      }
    }
  }
  if ((i + bound) % 5 === 0) console.log(JSON.stringify({ row: i, checkedPoints: report.checkedPoints }));
}
report.distinctPoints = seen.size;
report.scope = 'Exact rational subgroup search with coefficient bounds; not an exhaustive integral-point computation.';
writeFileSync('erdos686-elliptic-search-results.json', JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report));
