import fs from 'node:fs';
import assert from 'node:assert/strict';

function reverse(n,m) { let r=0; for(let i=0;i<m;++i) { r=3*r+n%3; n=Math.floor(n/3); } return r; }
function solve(n,edges) {
  const degree=Array(n).fill(0); for(const e of edges) for(const v of e) ++degree[v];
  let nodes=0; const trace=[];
  function branch(c,decisions=[]) {
    ++nodes; let changed; const record={decisions,forced:[]}; trace.push(record);
    do { changed=false;
      for(const e of edges) {
        let a=0,b=0,u=-1; for(const v of e) if(c[v]===0) ++a; else if(c[v]===1) ++b; else u=v;
        if(a===3||b===3) { record.contradiction=e; return false; }
        if(u>=0&&(a===2||b===2)) { c[u]=a===2?1:0; record.forced.push({edge:e,value:u,color:c[u]}); changed=true; }
      }
    } while(changed);
    let v=-1; for(let i=0;i<n;++i) if(c[i]<0&&(v<0||degree[i]>degree[v])) v=i;
    if(v<0) return c;
    for(let bit=0;bit<2;++bit) { const d=c.slice(); d[v]=bit; const result=branch(d,[...decisions,[v,bit]]); if(result) return result; }
    return false;
  }
  const initial=Array(n).fill(-1); initial[0]=0;
  return {coloring:branch(initial),nodes,trace};
}
for(let m=1;m<=4;++m) {
  const n=3**m, rank=Array.from({length:n},(_,i)=>reverse(i,m)), edges=[];
  let fours=0;
  for(let x=0;x<n;++x) for(let d=1;x+2*d<n;++d) {
    const r=[rank[x],rank[x+d],rank[x+2*d]];
    if((r[0]<r[1]&&r[1]<r[2])||(r[0]>r[1]&&r[1]>r[2])) edges.push([x,x+d,x+2*d]);
    if(x+3*d<n) {
      r.push(rank[x+3*d]);
      if(r.every((v,i)=>!i||r[i-1]<v)||r.every((v,i)=>!i||r[i-1]>v)) ++fours;
    }
  }
  assert.equal(fours,0);
  const result=solve(n,edges);
  console.log(JSON.stringify({m,n,edges:edges.length,nodes:result.nodes,colorable:!!result.coloring}));
  if(!result.coloring) {
    fs.writeFileSync(new URL('./196_197_ternary_obstruction.json',import.meta.url),JSON.stringify({m,n,permutation:rank,edges,nodes:result.nodes,proofTrace:result.trace},null,2));
    break;
  }
}
