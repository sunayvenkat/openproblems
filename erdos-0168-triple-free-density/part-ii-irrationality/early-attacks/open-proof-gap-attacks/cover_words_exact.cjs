// Exact diagonal DP for strict Ferrers shapes with drops avoiding 11 and 222.
const fs = require('fs'), path = require('path');
const {mvc, exactCover} = require('../Open conjecture transfer search/check_168_ferrers.cjs');

function diagonalTau(rows) {
  const left = new Int32Array(rows[0]).fill(rows[0]);
  for (let b = 0; b < rows.length; b++) for (let a = 0; a < rows[b]; a++)
    left[a+b] = Math.min(left[a+b], a);
  const maxWidth = Math.max(...left.map((l,k) => k-l+1));
  const pc = new Uint8Array(1 << maxWidth);
  for (let m = 1; m < pc.length; m++) pc[m] = pc[m >> 1] + (m & 1);
  let k = rows[0]-1, width = k-left[k]+1;
  let dp = Int32Array.from(pc.subarray(0, 1 << width));
  for (k--; k >= 0; k--) {
    const oldWidth = width; width = k-left[k]+1;
    const best = new Int32Array(1 << width).fill(rows[0]*rows.length+1);
    const mask = (1 << (oldWidth-1))-1, shift = left[k+1]-left[k];
    for (let u = 0; u < dp.length; u++) {
      const required = ((~(u | (u >> 1))) & mask) << shift;
      if (dp[u] < best[required]) best[required] = dp[u];
    }
    for (let bit = 1; bit < best.length; bit <<= 1)
      for (let base = 0; base < best.length; base += bit << 1)
        for (let low = base; low < base+bit; low++)
          if (best[low] < best[low+bit]) best[low+bit] = best[low];
    for (let m = 0; m < best.length; m++) best[m] += pc[m];
    dp = best;
  }
  return Math.min(...dp);
}
function* shapes(w, rows=[], word='') {
  rows = [...rows, w];
  if (w <= 2) yield {rows, word};
  for (const d of [1,2]) if (w > d && !(word+d).endsWith('11') && !(word+d).endsWith('222'))
    yield* shapes(w-d, rows, word+d);
}
const assert = require('assert');
module.exports = {diagonalTau, shapes};
if (require.main === module) {
for (const {rows} of shapes(10)) assert.strictEqual(diagonalTau(rows), exactCover(rows).value);
assert.strictEqual(diagonalTau([21,20,18,16,15,14,12,10,9,8,6,4,2]), 50);
assert.strictEqual(diagonalTau([9,8,6,5,3,2]), 11);
let checked = 0, found = null;
const start = Number(process.argv[2] || 21), end = Number(process.argv[3] || 34);
for (let width = start; width <= end && !found; width++) {
  for (const {rows,word} of shapes(width)) {
    const exact = diagonalTau(rows), pairs = [[0,1],[0,2],[1,2]].map(p => mvc(rows,...p));
    checked++;
    if (exact < Math.min(...pairs)) {
      found = {rows, drops:word, vertices:rows.reduce((a,b)=>a+b,0), exact, pairs, checked};
      console.log(JSON.stringify(found)); break;
    }
  }
  console.log(JSON.stringify({width,checked}));
}
fs.writeFileSync(path.join(__dirname,'cover_words_exact_results.json'),JSON.stringify({start,end,checked,found},null,2));
}
