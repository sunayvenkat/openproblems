import fs from 'node:fs';
import assert from 'node:assert/strict';

const witness = JSON.parse(fs.readFileSync(new URL('./196_197_obstruction.json', import.meta.url)));
const a = witness.values;
assert(a.length <= 30 && new Set(a).size === a.length);
assert(a.every((x,i) => Number.isSafeInteger(x) && x > 0 && (!i || a[i-1] < x)));
const triples = [], finishing = Array.from({length:a.length}, () => []);
let fourProgressions = 0;
// Independent enumeration uses index triples, rather than the discovery program's value lookup.
for (let i = 0; i < a.length; ++i) for (let j = i+1; j < a.length; ++j)
  for (let k = j+1; k < a.length; ++k) if (a[i]+a[k] === 2*a[j]) {
    triples.push([a[i],a[j],a[k]]);
    finishing[k].push((1<<i)|(1<<j)|(1<<k));
    for (let l = k+1; l < a.length; ++l) if (a[j]+a[l] === 2*a[k]) ++fourProgressions;
  }
assert.deepEqual(triples,witness.triples);
assert.equal(fourProgressions,0);
let nodes = 0, rejectedBranches = 0;
function search(i, red, blue) {
  ++nodes;
  if (i === a.length) return 1;
  let solutions = 0;
  for (let color = 0; color < 2; ++color) {
    const nextRed = red | (color === 0 ? 1<<i : 0), nextBlue = blue | (color === 1 ? 1<<i : 0);
    if (finishing[i].some(mask => (nextRed & mask) === mask || (nextBlue & mask) === mask)) ++rejectedBranches;
    else solutions += search(i+1,nextRed,nextBlue);
  }
  return solutions;
}
// Complement symmetry fixes the first value red. Every other coloring is examined or pruned by an explicit AP.
const solutionsUpToComplement = search(1,1,0);
assert.equal(solutionsUpToComplement,0);
const result = {vertices:a.length, triples:triples.length, fourProgressions, solutionsUpToComplement,nodes,rejectedBranches};
fs.writeFileSync(new URL('./196_197_verification.json',import.meta.url),JSON.stringify(result,null,2));
console.log(JSON.stringify(result));

const ternary=JSON.parse(fs.readFileSync(new URL('./196_197_ternary_obstruction.json',import.meta.url)));
const p=ternary.permutation, ending=Array.from({length:p.length},()=>[]), orderedTriples=[];
assert.equal(p.length,27); assert.equal(new Set(p).size,27);
assert(p.every(x=>Number.isInteger(x)&&0<=x&&x<27));
let fourCount=0;
for(let i=0;i<p.length;++i) for(let j=i+1;j<p.length;++j) for(let k=j+1;k<p.length;++k)
  if(p[i]+p[k]===2*p[j]) {
    orderedTriples.push([p[i],p[j],p[k]].sort((x,y)=>x-y)); ending[k].push((1<<i)|(1<<j)|(1<<k));
    for(let l=k+1;l<p.length;++l) if(p[j]+p[l]===2*p[k]) ++fourCount;
  }
assert.equal(fourCount,0);
assert.deepEqual(orderedTriples.map(JSON.stringify).sort(),ternary.edges.map(JSON.stringify).sort());
let visited=0,rejected=0;
function enumerate(i,red,blue) {
  ++visited; if(i===p.length) return 1;
  let total=0;
  for(let c=0;c<2;++c) {
    const nr=red|(c===0?1<<i:0),nb=blue|(c===1?1<<i:0);
    if(ending[i].some(mask=>(nr&mask)===mask||(nb&mask)===mask)) ++rejected;
    else total+=enumerate(i+1,nr,nb);
  }
  return total;
}
const ternaryCount=enumerate(1,1,0);
assert.equal(ternaryCount,0);
const ternaryResult={vertices:p.length,monotoneTriples:orderedTriples.length,monotoneFours:fourCount,coloringsUpToComplement:ternaryCount,visited,rejected};
fs.writeFileSync(new URL('./196_197_ternary_verification.json',import.meta.url),JSON.stringify(ternaryResult,null,2));
console.log(JSON.stringify(ternaryResult));
