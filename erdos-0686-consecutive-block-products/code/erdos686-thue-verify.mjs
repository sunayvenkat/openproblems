import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
const report = JSON.parse(readFileSync('erdos686-thue-results.json', 'utf8'));
const abs = n => n < 0n ? -n : n;
function gcd(a, b) {
  a = abs(a); b = abs(b);
  while (b) [a, b] = [b, a % b];
  return a;
}
const divisors = [];
for (let h = 1; h <= 15600; h++) if (15600 % h === 0) divisors.push(String(h));
assert.deepEqual(Object.keys(report.solutions), divisors);
assert.equal(divisors.length, 60);
const primitivePositive = [];
for (const [key, rows] of Object.entries(report.solutions)) {
  const h = BigInt(key);
  for (const [u, v] of rows) {
    const a = BigInt(u), b = BigInt(v);
    assert.equal(a ** 3n - 25n * b ** 3n, -h);
    if (a > 0n && b > 0n && gcd(a, b) === 1n) {
      const numerator = 25n * b - a;
      assert(numerator > 0n);
      if (numerator >= h) {
        assert.equal(a, 1n); assert.equal(b, 1n); assert.equal(h, 24n);
        assert.equal(numerator, h);
      }
      primitivePositive.push([u, v, Number(h)]);
    }
  }
}
assert.deepEqual(primitivePositive, [[1,1,24],[5,2,75],[35,12,325],[25,9,2600],[15,7,5200]]);
console.log(JSON.stringify({ checkedRightHandSides: divisors.length, primitivePositive,
  scope: 'Exact verification of reported rows and exclusion postfilter; Thue completeness is not verified by this script.' }, null, 2));
