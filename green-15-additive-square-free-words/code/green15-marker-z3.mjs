// Counterexample-guided synthesis. Learned clauses exclude actual additive squares.
// A model passing the finite check is a candidate, not an infinite proof.
import assert from 'node:assert/strict';
import { writeFileSync, readFileSync } from 'node:fs';
import { init, killThreads } from './.research-tools/node_modules/z3-solver/build/node.js';

const depth = Number(process.argv[2] ?? 2), K = Number(process.argv[3] ?? 18);
const checkLength = Number(process.argv[4] ?? 4096), maxIterations = Number(process.argv[5] ?? 1000);
const bitvectors = process.argv.includes('--bv');
const maxCuts = Number(process.argv.find(x => x.startsWith('--cuts='))?.split('=')[1] ?? 64);
assert.ok(Number.isInteger(maxCuts) && maxCuts > 0 && maxCuts <= 256);
assert.ok(Number.isInteger(depth) && depth >= 1 && depth <= 3);
const L = 4 ** depth, scale = 3 ** depth;
assert.ok(Number.isInteger(K) && K >= scale && K <= 100);
assert.ok(Number.isInteger(checkLength) && checkLength > L && checkLength * K * 4 < Number.MAX_SAFE_INTEGER);
function marker(n) {
  let value = 0, power = 1;
  for (let k = 0; k < depth; k++) { value += power * Number(n % 4 >= 2); n = Math.floor(n / 4); power *= 3; }
  return value;
}
const offsets = Array.from({ length: L }, (_, r) => marker((r + 1) % L) - marker(r));
assert.equal(offsets.reduce((a, b) => a + b, 0), 0);
for (let n = 0; n < L; n++) for (let d = 1; d < L; d++)
  assert.notEqual((marker(n) - 2 * marker((n + d) % L) + marker((n + 2 * d) % L)) % scale, 0);
const index = (a, r) => (a + K) * L + r, fixed = index(0, 0);
const maxLift = Math.ceil(K / scale) + 2;
const width = Math.max(8, Math.ceil(Math.log2(4 * checkLength * maxLift + 1)));
assert.ok(width < 52 && 2 ** (width - 1) > 2 * checkLength * maxLift);
const version = JSON.parse(readFileSync(new URL('./.research-tools/node_modules/z3-solver/package.json', import.meta.url), 'utf8')).version;
const api = await init();
let result;
try {
  const { Int, BitVec, Solver, Sum, Or, Bool } = new api.Context('marker');
  const solver = bitvectors ? new Solver('QF_BV') : new Solver();
  solver.set('timeout', 20000);
  const literal = a => bitvectors ? BitVec.val(a, width) : Int.val(a);
  // Decode explicitly: z3-solver 5.3.3's asSignedValue mishandles odd widths.
  const signedValue = v => { const raw = v.value(), modulus = 1n << BigInt(width); return Number(raw >= modulus / 2n ? raw - modulus : raw); };
  if (bitvectors) for (const a of [-maxLift, -1, 0, 1, maxLift]) assert.equal(signedValue(literal(a)), a);
  const sum = terms => bitvectors ? terms.reduce((s, x) => s.add(x), literal(0)) : Sum(...terms);
  const variables = Array.from({ length: (2 * K + 1) * L }, (_, i) => bitvectors ? BitVec.const(`z_${i}`, width) : Int.const(`z_${i}`));
  for (let a = -K; a <= K; a++) {
    let minSum = 0, maxSum = 0;
    for (let r = 0; r < L; r++) {
      const lower = Math.ceil((-K - offsets[r]) / scale), upper = Math.floor((K - offsets[r]) / scale);
      const v = variables[index(a, r)];
      solver.add(bitvectors ? v.sge(literal(lower)) : v.ge(lower), bitvectors ? v.sle(literal(upper)) : v.le(upper));
      minSum += lower; maxSum += upper;
    }
    assert.ok(minSum <= a && a <= maxSum, 'An unused alphabet letter would make the total encoding infeasible');
    solver.add(sum(Array.from({ length: L }, (_, r) => variables[index(a, r)])).eq(literal(a)));
  }
  solver.add(variables[fixed].eq(literal(0)));
  const cuts = new Set(), startTime = Date.now();
  let best = null, status = 'iteration_limit', iterations = 0;
  console.log(JSON.stringify({ initialized: true, z3: version, depth, L, scale, K, checkLength, variables: variables.length, bitvectors, width }));
  for (let iteration = 1; iteration <= maxIterations; iteration++) {
    iterations = iteration;
    if (Date.now() - startTime > 300000) { status = 'time_limit'; break; }
    const before = Date.now(), answer = await solver.check();
    if (answer !== 'sat') { status = answer; console.log(JSON.stringify({ iteration, status, checkMs: Date.now() - before })); break; }
    const model = solver.model();
    const values = variables.map(v => bitvectors ? signedValue(model.eval(v, true)) : Number(model.eval(v, true).value()));
    assert.ok(values.every(x => Math.abs(x) <= maxLift));
    const images = Array.from({ length: 2 * K + 1 }, (_, i) => Array.from({ length: L }, (_, r) => offsets[r] + scale * values[i * L + r]));
    for (let a = -K; a <= K; a++) {
      assert.ok(images[a + K].every(x => Number.isSafeInteger(x) && Math.abs(x) <= K));
      assert.equal(images[a + K].reduce((x, y) => x + y, 0), scale * a);
    }
    assert.equal(images[K][0], 0);
    const word = [0], sums = [0, 0], dependencies = [[]];
    for (let n = 1; n < checkLength; n++) {
      const parent = Math.floor(n / L), r = n % L, variable = index(word[parent], r);
      word[n] = images[word[parent] + K][r];
      sums[n + 1] = sums[n] + word[n];
      dependencies[n] = [...new Set([...dependencies[parent], ...(variable === fixed ? [] : [variable])])];
    }
    let firstBad = null, added = 0;
    for (let end = 2; end <= checkLength && added < maxCuts; end++) {
      for (let half = 1; 2 * half <= end && added < maxCuts; half++) {
        if (sums[end] - 2 * sums[end - half] + sums[end - 2 * half] !== 0) continue;
        assert.equal(half % L, 0);
        if (!firstBad) firstBad = { start: end - 2 * half, half, end };
        const context = new Set(), coefficients = new Map();
        let constant = 0;
        for (let n = end - 2 * half; n < end; n++) {
          const parent = Math.floor(n / L), r = n % L, variable = index(word[parent], r), sign = n < end - half ? 1 : -1;
          for (const v of dependencies[parent]) context.add(v);
          coefficients.set(variable, (coefficients.get(variable) ?? 0) + sign);
          constant += sign * offsets[r];
        }
        assert.equal(constant, 0);
        const terms = [...coefficients].filter(([, c]) => c !== 0).sort((a, b) => a[0] - b[0]);
        const assumptions = [...context].sort((a, b) => a - b).map(i => [i, values[i]]);
        assert.equal(terms.reduce((s, [i, c]) => s + c * values[i], 0), 0);
        const key = JSON.stringify([assumptions, terms]);
        if (cuts.has(key)) continue;
        cuts.add(key);
        const alternatives = assumptions.map(([i, value]) => variables[i].neq(literal(value)));
        if (terms.length) alternatives.push(sum(terms.map(([i, c]) => variables[i].mul(literal(c)))).neq(literal(0)));
        solver.add(alternatives.length ? Or(...alternatives) : Bool.val(false));
        added++;
      }
    }
    const validPrefix = firstBad ? firstBad.end - 1 : checkLength;
    if (!best || validPrefix > best.validPrefix) {
      best = { validPrefix, images, word: word.slice(0, validPrefix), firstBad };
      console.log(JSON.stringify({ iteration, validPrefix, cuts: cuts.size, checkMs: Date.now() - before }));
      writeFileSync(new URL(`./green15-marker-z3-best-${depth}-${K}${bitvectors ? '-bv' : ''}${maxCuts !== 64 ? `-cuts${maxCuts}` : ''}.json`, import.meta.url), JSON.stringify({ depth, L, scale, K, z3: version, bitvectors, width, maxCuts, best }, null, 2) + '\n');
    } else if (iteration % 10 === 0) console.log(JSON.stringify({ iteration, validPrefix, best: best.validPrefix, cuts: cuts.size, checkMs: Date.now() - before }));
    model.release();
    if (!firstBad) { status = 'finite_candidate'; break; }
    assert.ok(added > 0, 'The current model violates only already-learned clauses');
  }
  result = { scope: 'Counterexample-guided bounded synthesis of uniform modular-marker substitutions. Every learned clause is conditional on parent dependencies and excludes a concrete additive square. A finite candidate is not an infinite construction. Solver outcomes have no independent proof certificate here.', depth, L, scale, K, checkLength, maxIterations, maxCuts, z3: version, bitvectors, width, status, iterations, cuts: cuts.size, best };
  const suffix = `${bitvectors ? '-bv' : ''}${maxCuts !== 64 ? `-cuts${maxCuts}` : ''}`;
  writeFileSync(new URL(`./green15-marker-z3-results-${depth}-${K}${suffix}.json`, import.meta.url), JSON.stringify(result, null, 2) + '\n');
  writeFileSync(new URL(`./green15-marker-z3-${depth}-${K}${suffix}.smt2`, import.meta.url), solver.toString() + '\n(check-sat)\n');
  console.log(JSON.stringify({ status, iterations, cuts: cuts.size, best: best?.validPrefix }));
} finally {
  await killThreads(api.em);
}
