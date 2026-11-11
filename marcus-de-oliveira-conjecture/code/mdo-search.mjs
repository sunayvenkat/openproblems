import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

let seed = 2432026;
const add = (a, b) => [a[0] + b[0], a[1] + b[1]];
const mul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
const scale = (a, s) => [a[0] * s, a[1] * s];
const norm = a => Math.hypot(...a);
const random = () => ((seed = (Math.imul(1664525, seed) + 1013904223) >>> 0) / 2 ** 32);
const complexRandom = () => [2 * random() - 1, 2 * random() - 1];
const spectrum = (n, mode) => Array.from({ length: n }, (_, i) => {
  const z = complexRandom();
  if (mode === 'near-real') return [z[0], 0.01 * z[1]];
  if (mode === 'two-clusters') return [i < n / 2 ? 1 + 0.03 * z[0] : -1 + 0.03 * z[0], 0.03 * z[1]];
  return z;
});
const identity = n => Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => [Number(i === j), 0]));

function determinant(matrix) {
  const a = matrix.map(row => row.map(z => [...z]));
  let answer = [1, 0];
  for (let j = 0; j < a.length; j++) {
    let pivot = j;
    for (let k = j + 1; k < a.length; k++) if (norm(a[k][j]) > norm(a[pivot][j])) pivot = k;
    if (norm(a[pivot][j]) < 1e-250) return [0, 0];
    if (pivot !== j) {
      [a[j], a[pivot]] = [a[pivot], a[j]];
      answer = scale(answer, -1);
    }
    const p = a[j][j];
    answer = mul(answer, p);
    const inverse = scale([p[0], -p[1]], 1 / (p[0] ** 2 + p[1] ** 2));
    for (let k = j + 1; k < a.length; k++) {
      const factor = mul(a[k][j], inverse);
      for (let l = j + 1; l < a.length; l++) a[k][l] = add(a[k][l], scale(mul(factor, a[j][l]), -1));
    }
  }
  return answer;
}

function rowRotate(matrix, i, j, c, s) {
  const minusConjugate = [-s[0], s[1]];
  for (let k = 0; k < matrix.length; k++) {
    const x = matrix[i][k], y = matrix[j][k];
    matrix[i][k] = add(scale(x, c), mul(minusConjugate, y));
    matrix[j][k] = add(mul(s, x), scale(y, c));
  }
}

function conjugateRotate(matrix, i, j, c, s) {
  const a = matrix.map(row => row.map(z => [...z]));
  rowRotate(a, i, j, c, s);
  for (let k = 0; k < a.length; k++) {
    const x = a[k][i], y = a[k][j];
    a[k][i] = add(scale(x, c), scale(mul(s, y), -1));
    a[k][j] = add(mul([s[0], -s[1]], x), scale(y, c));
  }
  return a;
}

function fromSpectrum(b, U) {
  return U.map((row, i) => row.map((_, j) => {
    let z = [0, 0];
    for (let k = 0; k < b.length; k++) z = add(z, mul(mul(U[i][k], b[k]), [U[j][k][0], -U[j][k][1]]));
    return z;
  }));
}

function value(a, B) {
  return determinant(B.map((row, i) => row.map((z, j) => i === j ? add(z, a[i]) : z)));
}

function vertices(a, b) {
  const values = [];
  function visit(prefix, remaining) {
    if (!remaining.length) {
      values.push(prefix.reduce((z, j, i) => mul(z, add(a[i], b[j])), [1, 0]));
      return;
    }
    for (const j of remaining) visit([...prefix, j], remaining.filter(k => k !== j));
  }
  visit([], b.map((_, i) => i));
  return values;
}

function hull(points) {
  const sorted = points.map(z => [...z]).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const cross = (a, b, c) => (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
  const lower = [], upper = [];
  for (const p of sorted) {
    while (lower.length >= 2 && cross(lower.at(-2), lower.at(-1), p) <= 0) lower.pop();
    lower.push(p);
  }
  for (const p of sorted.toReversed()) {
    while (upper.length >= 2 && cross(upper.at(-2), upper.at(-1), p) <= 0) upper.pop();
    upper.push(p);
  }
  return lower.slice(0, -1).concat(upper.slice(0, -1));
}

function bestRotation(x, y, z) {
  const radius = Math.hypot(x, y, z);
  const transverse = Math.hypot(x, y);
  if (z >= 0) {
    const c = Math.sqrt((1 + z / radius) / 2);
    return { c, s: [x / (2 * c * radius), y / (2 * c * radius)] };
  }
  // Compute the larger component first to avoid cancellation near the south pole.
  const magnitude = Math.sqrt((1 - z / radius) / 2);
  return { c: transverse / (2 * radius * magnitude), s: transverse === 0 ? [1, 0] : [magnitude * x / transverse, magnitude * y / transverse] };
}

function randomUnitary(n) {
  const U = identity(n);
  for (let t = 0; t < 4 * n * n; t++) {
    const i = Math.floor(random() * n), j = (i + 1 + Math.floor(random() * (n - 1))) % n;
    const angle = 2 * Math.PI * random(), phase = 2 * Math.PI * random();
    rowRotate(U, i, j, Math.cos(angle), scale([Math.cos(phase), Math.sin(phase)], Math.sin(angle)));
  }
  return U;
}

function optimize(a, b, direction, maxSweeps = 60, initialU) {
  const n = a.length;
  const U = initialU ? initialU.map(row => row.map(z => [...z])) : randomUnitary(n);
  let B = fromSpectrum(b, U);
  const project = z => z[0] * direction[0] + z[1] * direction[1];
  let current = project(value(a, B));
  for (let sweep = 0; sweep < maxSweeps; sweep++) {
    const initial = current;
    for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) {
      const south = project(value(a, conjugateRotate(B, i, j, 0, [1, 0])));
      const middle = (current + south) / 2;
      const z = (current - south) / 2;
      const x = project(value(a, conjugateRotate(B, i, j, Math.SQRT1_2, [Math.SQRT1_2, 0]))) - middle;
      const y = project(value(a, conjugateRotate(B, i, j, Math.SQRT1_2, [0, Math.SQRT1_2]))) - middle;
      const radius = Math.hypot(x, y, z);
      if (radius < 1e-15) continue;
      const { c, s } = bestRotation(x, y, z);
      assert(Math.abs(c * c + s[0] ** 2 + s[1] ** 2 - 1) < 1e-12);
      B = conjugateRotate(B, i, j, c, s);
      rowRotate(U, i, j, c, s);
      const next = project(value(a, B));
      assert(Math.abs(next - (middle + radius)) < 1e-8 * (1 + radius + Math.abs(middle)));
      assert(next >= current - 1e-8 * (1 + Math.abs(current)));
      current = next;
    }
    // Rebuild from the saved unitary to keep conjugation roundoff from accumulating.
    B = fromSpectrum(b, U);
    current = project(value(a, B));
    if (current - initial < 1e-11 * (1 + Math.abs(current))) break;
  }
  return { value: value(a, B), U, projected: current };
}

// Each plane is [constant, x coefficient, y coefficient]. All candidates
// for a maximum of their minimum on the unit disc are enumerated below.
function maxMinDisc(planes, initial, holes = []) {
  const objective = p => Math.min(...planes.map(([c, x, y]) => c + x * p[0] + y * p[1]));
  let best = [...initial], bestValue = objective(best);
  function consider(p) {
    const r = Math.hypot(...p);
    if (!Number.isFinite(r) || r > 1 + 1e-9) return;
    if (r > 1) p = p.map(t => t / r);
    if (holes.some(({ center, radius }) => norm(add(p, scale(center, -1))) < radius - 1e-9)) return;
    let minimum = Infinity;
    for (const [c, x, y] of planes) {
      minimum = Math.min(minimum, c + x * p[0] + y * p[1]);
      if (minimum <= bestValue) return;
    }
    best = p; bestValue = minimum;
  }
  consider([0, 0]);
  for (const [, x, y] of planes) {
    const r = Math.hypot(x, y);
    if (r > 1e-20) consider([x / r, y / r]);
  }
  for (let i = 0; i < planes.length; i++) for (let j = i + 1; j < planes.length; j++) {
    const c = planes[j][0] - planes[i][0];
    const x = planes[i][1] - planes[j][1], y = planes[i][2] - planes[j][2];
    const r2 = x * x + y * y;
    if (r2 < 1e-30) continue;
    const p = [c * x / r2, c * y / r2];
    consider(p);
    const distance2 = (c * c) / r2;
    if (distance2 <= 1 + 1e-12) {
      const t = Math.sqrt(Math.max(0, (1 - distance2) / r2));
      consider([p[0] - t * y, p[1] + t * x]);
      consider([p[0] + t * y, p[1] - t * x]);
    }
    for (let k = j + 1; k < planes.length; k++) {
      const c2 = planes[k][0] - planes[i][0];
      const x2 = planes[i][1] - planes[k][1], y2 = planes[i][2] - planes[k][2];
      const determinant = x * y2 - y * x2;
      if (Math.abs(determinant) < 1e-12 * Math.sqrt(r2 * (x2 * x2 + y2 * y2))) continue;
      consider([(c * y2 - c2 * y) / determinant, (x * c2 - x2 * c) / determinant]);
    }
  }
  const circles = [{ center: [0, 0], radius: 1 }, ...holes];
  for (const { center, radius } of circles) {
    for (const [, x, y] of planes) {
      const r = Math.hypot(x, y);
      if (r > 1e-20) for (const sign of [-1, 1]) consider([center[0] + sign * radius * x / r, center[1] + sign * radius * y / r]);
    }
    for (let i = 0; i < planes.length; i++) for (let j = i + 1; j < planes.length; j++) {
      const x = planes[i][1] - planes[j][1], y = planes[i][2] - planes[j][2], r2 = x * x + y * y;
      if (r2 < 1e-30) continue;
      const c = planes[j][0] - planes[i][0] - x * center[0] - y * center[1];
      if (c * c > radius * radius * r2 + 1e-12 * r2) continue;
      const p = [center[0] + c * x / r2, center[1] + c * y / r2];
      const t = Math.sqrt(Math.max(0, (radius * radius - c * c / r2) / r2));
      consider([p[0] - t * y, p[1] + t * x]);
      consider([p[0] + t * y, p[1] - t * x]);
    }
  }
  for (let i = 0; i < circles.length; i++) for (let j = i + 1; j < circles.length; j++) {
    const a = circles[i], b = circles[j], v = add(b.center, scale(a.center, -1)), distance = norm(v);
    if (distance < 1e-15 || distance > a.radius + b.radius + 1e-12 || distance < Math.abs(a.radius - b.radius) - 1e-12) continue;
    const offset = (a.radius * a.radius - b.radius * b.radius + distance * distance) / (2 * distance);
    const height = Math.sqrt(Math.max(0, a.radius * a.radius - offset * offset));
    const p = add(a.center, scale(v, offset / distance));
    for (const sign of [-1, 1]) consider([p[0] - sign * height * v[1] / distance, p[1] + sign * height * v[0] / distance]);
  }
  assert(bestValue >= objective(initial) - 1e-12);
  return { point: best, value: bestValue };
}

function bestSupport(a, b, U) {
  const v = vertices(a, b), polygon = hull(v), d = value(a, fromSpectrum(b, U));
  const normalization = Math.max(...v.map(norm), 1e-12);
  let result = { gap: -Infinity, direction: [1, 0], normalization, value: d };
  for (let i = 0; i < polygon.length; i++) {
    const p = polygon[i], q = polygon[(i + 1) % polygon.length];
    const direction = [q[1] - p[1], p[0] - q[0]], r = norm(direction);
    if (r < 1e-18) continue;
    direction[0] /= r; direction[1] /= r;
    const project = z => z[0] * direction[0] + z[1] * direction[1];
    const gap = project(d) - Math.max(...v.map(project));
    if (gap > result.gap) result = { gap, direction, normalization, value: d };
  }
  return result;
}

function spectralCoordinate(a, b, U, direction, side, index, separation = 0) {
  const list = side === 0 ? a : b, old = [...list[index]];
  function evaluate(z) {
    list[index] = z;
    const d = value(a, fromSpectrum(b, U));
    return vertices(a, b).map(v => add(d, scale(v, -1)));
  }
  const zero = evaluate([0, 0]), one = evaluate([1, 0]), imaginary = evaluate([0, 1]);
  const project = z => z[0] * direction[0] + z[1] * direction[1];
  const planes = zero.map((z, i) => {
    const coefficient = add(one[i], scale(z, -1));
    const rotated = [-coefficient[1], coefficient[0]];
    assert(norm(add(imaginary[i], scale(add(z, rotated), -1))) < 1e-8 * (1 + norm(z) + norm(coefficient)));
    return [project(z), project(coefficient), project(rotated)];
  });
  const oldGap = Math.min(...planes.map(([c, x, y]) => c + x * old[0] + y * old[1]));
  const holes = separation ? list.filter((_, j) => j !== index).map(center => ({ center, radius: separation })) : [];
  const update = maxMinDisc(planes, old, holes);
  const actualGap = Math.min(...evaluate(update.point).map(project));
  assert(Math.abs(actualGap - update.value) < 1e-8 * (1 + Math.abs(actualGap)));
  assert(actualGap >= oldGap - 1e-8 * (1 + Math.abs(oldGap)));
  list[index] = update.point;
}

function jointSpectralSearch(restarts, drury = false, distinct = false) {
  const report = { seed, order: 4, restarts, unitaryFamily: distinct ? 'random Givens and Drury' : drury ? 'Drury skew conference' : 'random Givens', pinnedEigenvaluesPerSpectrum: distinct ? [3, 1] : [3, 3], minimumSeparation: distinct ? 0.15 : 0,
    completedRestarts: 0, coordinateUpdates: 0,
    bestNormalizedExcess: -Infinity, candidate: null };
  search: for (let trial = 0; trial < restarts; trial++) {
    let a, b, pinnedVolume;
    do {
      a = spectrum(4, 'general').map(z => scale(z, Math.SQRT1_2));
      b = spectrum(4, 'general').map(z => scale(z, Math.SQRT1_2));
      const pinned = [...a.slice(0, 3), scale(b[0], -1)];
      pinnedVolume = determinant(pinned.map(z => [norm(z) ** 2, ...z, 1].map(t => [t, 0])))[0];
    } while (distinct && (Math.abs(pinnedVolume) < 0.02 || [a, b].some(list => list.some((z, i) => list.slice(i + 1).some(w => norm(add(z, scale(w, -1))) < 0.15)))));
    const useDrury = drury || (distinct && trial % 2 === 0);
    const t = useDrury ? 0.4 + 0.2 * random() : 0;
    const alpha = (1 - 3 * t * t) / (1 + 3 * t * t), beta = 2 * t / (1 + 3 * t * t);
    const conference = [[0, 1, 1, 1], [-1, 0, 1, -1], [-1, -1, 0, 1], [-1, 1, -1, 0]];
    let U = useDrury ? conference.map((row, i) => row.map((s, j) => [i === j ? alpha : beta * s, 0])) : randomUnitary(4);
    if (useDrury) for (let i = 0; i < 4; i++) for (let j = 0; j < 4; j++) {
      assert(Math.abs(U[i].reduce((sum, z, k) => sum + z[0] * U[j][k][0], 0) - Number(i === j)) < 1e-12);
    }
    let support = bestSupport(a, b, U);
    for (let round = 0; round < 12; round++) {
      for (let sweep = 0; sweep < 4; sweep++) {
        // The distinct mode fixes a noncocircular quadruple and excludes repeated spectra.
        const coordinates = distinct ? [3, 5, 6, 7] : [3, 7];
        for (const coordinate of trial % 2 ? coordinates.toReversed() : coordinates) {
          spectralCoordinate(a, b, U, support.direction, Math.floor(coordinate / 4), coordinate % 4, distinct ? 0.15 : 0);
          report.coordinateUpdates++;
        }
        support = bestSupport(a, b, U);
      }
      support = bestSupport(a, b, U);
      const excess = support.gap / support.normalization;
      if (excess > report.bestNormalizedExcess) {
        report.bestNormalizedExcess = excess;
        if (distinct) report.bestCase = structuredClone({ a, b, U, ...support, excess });
      }
      if (excess > 1e-7 && support.gap > 1e-9) {
        report.candidate = { a, b, U, ...support, excess };
        break search;
      }
      if (support.gap > -1e-10 || !Number.isFinite(support.gap)) break;
    }
    report.completedRestarts++;
    if ((trial + 1) % 10 === 0) console.log(JSON.stringify({ restarts: trial + 1, bestNormalizedExcess: report.bestNormalizedExcess }));
  }
  report.scope = 'Floating-point spectral optimization with one fixed sampled unitary per restart. No completeness or global-optimality certificate. Positive candidates require exact reconstruction and verification.';
  writeFileSync(distinct ? 'mdo-distinct-search-results.json' : drury ? 'mdo-drury-search-results.json' : 'mdo-spectral-search-results.json', JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report));
}

// Independent small determinant and rotation checks precede the search.
assert(norm(add(determinant([[[1, 1], [2, 0]], [[0, 1], [3, -1]]]), [-4, 0])) < 1e-12);
const nearPole = bestRotation(2.4681368060441855e-12, 6.4863669990700146e-12, -1.0542747358455173e-7);
assert(Math.abs(nearPole.c ** 2 + norm(nearPole.s) ** 2 - 1) < 1e-14);
const fixtureA = [[1, 2], [-2, 1], [0.3, -0.7], [2, -1]];
const fixtureB = [[-1, 0], [2, 1], [0, 2], [0.4, -0.8]];
const fixtureU = identity(4);
rowRotate(fixtureU, 0, 2, 0.6, [0.48, 0.64]);
rowRotate(fixtureU, 1, 3, 0.8, [0.36, 0.48]);
rowRotate(fixtureU, 0, 3, 0.6, [-0.64, 0.48]);
const fixtureMatrix = fromSpectrum(fixtureB, fixtureU);
const north = value(fixtureA, fixtureMatrix);
const south = value(fixtureA, conjugateRotate(fixtureMatrix, 0, 3, 0, [1, 0]));
const middle = scale(add(north, south), 0.5);
const z = scale(add(north, scale(south, -1)), 0.5);
const x = add(value(fixtureA, conjugateRotate(fixtureMatrix, 0, 3, Math.SQRT1_2, [Math.SQRT1_2, 0])), scale(middle, -1));
const y = add(value(fixtureA, conjugateRotate(fixtureMatrix, 0, 3, Math.SQRT1_2, [0, Math.SQRT1_2])), scale(middle, -1));
assert(norm(x) > 1e-4 && norm(y) > 1e-4);
const actual = value(fixtureA, conjugateRotate(fixtureMatrix, 0, 3, 0.6, [0.48, 0.64]));
const predicted = add(middle, add(scale(z, -0.28), add(scale(x, 0.576), scale(y, 0.768))));
assert(norm(add(actual, scale(predicted, -1))) < 1e-10);
assert(Math.abs(maxMinDisc([[0, 1, 0]], [0, 0]).value - 1) < 1e-12);
assert(Math.abs(maxMinDisc([[0, 1, 0], [0, 0, 1]], [0, 0]).value - Math.SQRT1_2) < 1e-12);
assert(Math.abs(maxMinDisc([[0, 1, 0], [0, 0, 1], [1, -1, -1]], [0, 0]).value - 1 / 3) < 1e-12);
assert(Math.abs(maxMinDisc([[1, 1, 0], [1, -1, 0]], [0.5, 0]).value - 1) < 1e-12);
assert(Math.abs(maxMinDisc([[0, -1, 0]], [0, 0], [{ center: [-1, 0], radius: 0.25 }]).value - 0.96875) < 1e-12);
assert(Math.abs(maxMinDisc([[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], [0.5, 0], [{ center: [0, 0], radius: 0.5 }]).value + Math.SQRT1_2 / 2) < 1e-12);

if (['--spectral', '--drury', '--distinct'].includes(process.argv[2])) {
  const restarts = Number(process.argv[3] ?? 100);
  assert(Number.isSafeInteger(restarts) && restarts >= 1 && restarts <= 10000);
  jointSpectralSearch(restarts, process.argv[2] === '--drury', process.argv[2] === '--distinct');
  process.exit(0);
}

const modes = ['general', 'near-real', 'two-clusters'];
const report = { seed, modes, spectra: 0, optimizations: 0, bestNormalizedExcess: -Infinity, suboptimalRuns: 0, worstNormalizedDeficit: 0, hardestCase: null, candidate: null, byCase: {} };
search: for (const mode of modes) for (const n of [4, 5, 6]) {
  let best = -Infinity;
  for (let trial = 0; trial < 100; trial++) {
    const a = spectrum(n, mode);
    const b = spectrum(n, mode);
    const v = vertices(a, b), polygon = hull(v);
    const normalization = Math.max(...v.map(norm), 1e-12);
    report.spectra++;
    // An outward normal of a polygon edge makes at least two commuting vertices tie.
    for (let edge = 0; edge < polygon.length; edge++) {
      const p = polygon[edge], q = polygon[(edge + 1) % polygon.length];
      const dx = q[0] - p[0], dy = q[1] - p[1], length = Math.hypot(dx, dy);
      if (length < 1e-14) continue;
      const direction = [dy / length, -dx / length];
      const bound = Math.max(...v.map(z => z[0] * direction[0] + z[1] * direction[1]));
      const result = optimize(a, b, direction);
      const excess = (result.projected - bound) / normalization;
      report.optimizations++;
      if (excess < -1e-8) report.suboptimalRuns++;
      if (-excess > report.worstNormalizedDeficit) {
        report.worstNormalizedDeficit = -excess;
        report.hardestCase = { mode, a, b, direction, bound, excess, ...result };
      }
      best = Math.max(best, excess);
      report.bestNormalizedExcess = Math.max(report.bestNormalizedExcess, excess);
      if (excess > 1e-7) {
        report.candidate = { mode, a, b, direction, bound, excess, ...result };
        break;
      }
    }
    if (report.candidate) break;
    if ((trial + 1) % 100 === 0) console.log(JSON.stringify({ mode, order: n, spectra: trial + 1, bestNormalizedExcess: best }));
  }
  report.byCase[`${mode}/${n}`] = best;
  if (report.candidate) break search;
}
report.scope = 'Floating-point targeted search only. Any candidate requires exact rational reconstruction and verification.';
writeFileSync('mdo-search-results.json', JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report));
