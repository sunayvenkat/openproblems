import assert from 'node:assert/strict';
import { writeFileSync } from 'node:fs';

// Two independent hubs 0,1 joined to paths 2-3-4 and 5-6-7.
const edges = [];
for (const h of [0,1]) for (let v=2;v<8;v++) edges.push([h,v]);
edges.push([2,3],[3,4],[5,6],[6,7]);
const cycle = [0,2,3,4,1,5,6,7];
assert.equal(edges.length,16);
for(let i=0;i<8;i++) {
  const a=cycle[i],b=cycle[(i+1)%8];
  assert(edges.some(([u,v])=>u===a&&v===b||u===b&&v===a));
}
let cubicSubgraphs=0;
for(let mask=1;mask<(1<<edges.length);mask++) {
  const degrees=Array(8).fill(0);
  for(let j=0;j<edges.length;j++) if(mask&(1<<j)) {
    degrees[edges[j][0]]++;
    degrees[edges[j][1]]++;
  }
  if(degrees.every(d=>d===0||d===3)) cubicSubgraphs++;
}
assert.equal(cubicSubgraphs,0);
const result={vertices:8,edges,hamiltonianCycle:cycle,chords:8,nonemptyEdgeSetsChecked:65535,cubicSubgraphs};
writeFileSync(new URL('hamiltonian_cubic_counterexample.json',import.meta.url),JSON.stringify(result,null,2));
console.log(JSON.stringify(result));
