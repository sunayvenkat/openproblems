// Bounded experiment for Green 15. A surviving prefix is not an infinite proof.
import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

const weights = [0, 1, 2, 5];
const length = Number(process.argv[2] ?? 24);
const diverse = process.argv.includes('--diverse');
assert.ok(Number.isInteger(length) && length >= 24 && length % 4 === 0);
const beta = [-1, 1, -1, 1];
const alpha = beta.map(b => length / 4 - 2 * b);
const counts = weights.map(w => alpha.map((a, i) => a + beta[i] * w));
let seed = 20261106;
function random() {
  seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5;
  return (seed >>> 0) / 4294967296;
}
function firstSquare(word) {
  const sums = [0];
  for (let end = 1; end <= word.length; end++) {
    sums[end] = sums[end - 1] + weights[word[end - 1]];
    for (let half = 1; 2 * half <= end; half++) {
      if (sums[end] - 2 * sums[end - half] + sums[end - 2 * half] === 0)
        return { start: end - 2 * half, half, end };
    }
  }
  return null;
}
function bruteSquare(word) {
  for (let end = 1; end <= word.length; end++) {
    for (let half = 1; 2 * half <= end; half++) {
      let difference = 0;
      for (let i = end - 2 * half; i < end - half; i++)
        difference += weights[word[i]] - weights[word[i + half]];
      if (difference === 0) return { start: end - 2 * half, half, end };
    }
  }
  return null;
}
function pool(letter, limit = 500, nodeLimit = 8_000_000) {
  const remaining = [...counts[letter]], word = [], sums = [0], words = [];
  let nodes = 0, stopped = false, targetCount = limit, exhausted = false;
  function visit() {
    if (nodes >= nodeLimit || words.length >= targetCount) { stopped = true; return; }
    nodes++;
    if (word.length === length) { words.push([...word]); return; }
    const order = [0, 1, 2, 3];
    for (let i = 3; i > 0; i--) {
      const j = Math.floor(random() * (i + 1));
      [order[i], order[j]] = [order[j], order[i]];
    }
    for (const symbol of order) {
      if (!remaining[symbol] || (letter === 0 && word.length === 0 && symbol !== 0)) continue;
      const end = word.length + 1;
      sums[end] = sums[end - 1] + weights[symbol];
      let good = true;
      for (let half = 1; 2 * half <= end; half++) {
        if (sums[end] - 2 * sums[end - half] + sums[end - 2 * half] === 0) {
          good = false; break;
        }
      }
      if (!good) continue;
      word.push(symbol); remaining[symbol]--;
      visit();
      remaining[symbol]++; word.pop();
      if (stopped) return;
    }
  }
  do {
    stopped = false;
    targetCount = diverse ? words.length + 1 : limit;
    visit();
    if (!stopped) { exhausted = true; break; }
  } while (diverse && words.length < limit && nodes < nodeLimit);
  for (const w of words) {
    assert.equal(firstSquare(w), null);
    assert.deepEqual(weights.map((_, s) => w.filter(x => x === s).length), counts[letter]);
  }
  const unique = [...new Map(words.map(w => [w.join(','), w])).values()];
  return { words: unique, samples: words.length, nodes, exhausted };
}
function expand(word, images) { return word.flatMap(s => images[s]); }
function evaluate(images) {
  let word = images[0];
  for (let level = 2; level <= 3; level++) {
    word = expand(word, images);
    const square = firstSquare(word);
    if (square) return { score: square.end - 1, checkedLength: word.length, square };
  }
  return { score: word.length, checkedLength: word.length, square: null };
}

// Independent direct sums check all 4096 words of length six.
for (let code = 0; code < 4096; code++) {
  let value = code;
  const word = Array.from({ length: 6 }, () => { const x = value % 4; value = Math.floor(value / 4); return x; });
  assert.deepEqual(firstSquare(word), bruteSquare(word));
}
assert.deepEqual(firstSquare([0, 3, 2, 1, 3, 1]), { start: 0, half: 3, end: 6 });
for (let j = 0; j < 4; j++) {
  assert.deepEqual(counts[j], alpha.map((a, i) => a + beta[i] * weights[j]));
  assert.equal(counts[j].reduce((a, b) => a + b), length);
  assert.equal(counts[j].reduce((a, b, i) => a + b * weights[i], 0), 2 * length - 8 + 4 * weights[j]);
}
const pools = weights.map((_, i) => pool(i));
console.log(JSON.stringify({ pools: pools.map(({ words, ...r }, i) => ({ letter: weights[i], size: words.length, ...r })) }));
let best = null;
if (pools.every(p => p.words.length > 0)) {
  for (let restart = 0; restart < 300; restart++) {
    let images = pools.map(p => p.words[Math.floor(random() * p.words.length)]);
    let result = evaluate(images);
    for (let step = 0; step < 300; step++) {
      const next = [...images], letter = Math.floor(random() * 4), p = pools[letter];
      next[letter] = p.words[Math.floor(random() * p.words.length)];
      const r = evaluate(next);
      if (r.score >= result.score || random() < 0.01) { images = next; result = r; }
      if (!best || r.score > best.score) {
        best = { ...r, images: next.map(w => w.map(s => weights[s])) };
        console.log(JSON.stringify({ best }));
      }
      if (!r.square) break;
    }
    if (best && !best.square) break;
  }
}
const output = { scope: 'Fixed rank-two incidence matrix, bounded image pools and heuristic search; no infinite conclusion.', length, diverse, weights, counts,
  pools: pools.map(({ words, ...r }, i) => ({ letter: weights[i], size: words.length, ...r })), best };
writeFileSync(new URL(`./green15-rank2-results-${length}${diverse ? '-diverse' : ''}.json`, import.meta.url), JSON.stringify(output, null, 2) + '\n');
