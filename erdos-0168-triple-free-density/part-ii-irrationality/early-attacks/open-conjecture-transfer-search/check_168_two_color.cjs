// Exact bipartite matching supplies valid two-color hitting covers.
const fs = require('fs');
const path = require('path');
const samples = process.argv.slice(2).map(Number);
if (!samples.length) samples.push(5000, 10000, 20000, 50000, 100000);
const limit = Math.max(...samples);
const points = [{v:1n,a:0,b:0}];
let i2=0, i3=0;
while(points.length<limit){
  const v2=2n*points[i2].v,v3=3n*points[i3].v;
  const take2=v2<=v3;
  const src=take2?points[i2]:points[i3];
  points.push({v:take2?v2:v3,a:src.a+(take2?1:0),b:src.b+(take2?0:1)});
  if(v2<=v3)i2++;
  if(v3<=v2)i3++;
}
const position=new Map(points.map((p,i)=>[p.v.toString(),i]));
function candidate(k){
  const t=points[k-1].v, sizes=[0,0,0];
  for(let i=0;i<k;i++)sizes[(points[i].a+2*points[i].b)%3]++;
  for(let s=1n,a=0;s<=t;s*=2n,a++){
    if(3n*s>2n*t)sizes[a%3]--;
    if(12n*s<=t&&2n*t<27n*s)sizes[(a+1)%3]--;
  }
  return {value:Math.min(...sizes),sizes};
}
function pairCover(k,leftColor,rightColor){
  const left=[],right=[],li=new Int32Array(k).fill(-1),ri=new Int32Array(k).fill(-1);
  for(let i=0;i<k;i++){
    const c=(points[i].a+2*points[i].b)%3;
    if(c===leftColor){li[i]=left.length;left.push(i);}
    if(c===rightColor){ri[i]=right.length;right.push(i);}
  }
  const adj=Array.from({length:left.length},()=>[]);
  const t=points[k-1].v;
  for(let i=0;i<k&&3n*points[i].v<=t;i++){
    const ids=[i,position.get((2n*points[i].v).toString()),position.get((3n*points[i].v).toString())];
    const l=ids.find(x=>li[x]>=0),r=ids.find(x=>ri[x]>=0);
    adj[li[l]].push(ri[r]);
  }
  const ml=new Int32Array(left.length).fill(-1),mr=new Int32Array(right.length).fill(-1),dist=new Int32Array(left.length);
  let matching=0;
  while(true){
    dist.fill(-1);const queue=[];
    for(let l=0;l<left.length;l++)if(ml[l]<0){dist[l]=0;queue.push(l);}
    let freeFound=false;
    for(let head=0;head<queue.length;head++){
      const l=queue[head];
      for(const r of adj[l])if(mr[r]<0)freeFound=true;else if(dist[mr[r]]<0){dist[mr[r]]=dist[l]+1;queue.push(mr[r]);}
    }
    if(!freeFound)break;
    function dfs(l){
      for(const r of adj[l])if(mr[r]<0||(dist[mr[r]]===dist[l]+1&&dfs(mr[r]))){ml[l]=r;mr[r]=l;return true;}
      dist[l]=-1;return false;
    }
    for(let l=0;l<left.length;l++)if(ml[l]<0&&dfs(l))matching++;
  }
  // Konig witness: (left minus alternating-reachable left) union reachable right.
  const zl=new Uint8Array(left.length),zr=new Uint8Array(right.length),queue=[];
  for(let l=0;l<left.length;l++)if(ml[l]<0){zl[l]=1;queue.push(l);}
  for(let head=0;head<queue.length;head++)for(const r of adj[queue[head]])if(ml[queue[head]]!==r&&!zr[r]){
    zr[r]=1;
    if(mr[r]>=0&&!zl[mr[r]]){zl[mr[r]]=1;queue.push(mr[r]);}
  }
  const selected=[];
  for(let l=0;l<left.length;l++)if(!zl[l])selected.push(left[l]);
  for(let r=0;r<right.length;r++)if(zr[r])selected.push(right[r]);
  if(selected.length!==matching)throw Error('matching/cover cardinalities differ');
  const chosen=new Set(selected);
  for(let i=0;i<k&&3n*points[i].v<=t;i++)if(!chosen.has(i)&&!chosen.has(position.get((2n*points[i].v).toString()))&&!chosen.has(position.get((3n*points[i].v).toString())))throw Error('uncovered corner');
  return {matching,selected};
}
const records=[];
for(const k of samples){
  const prediction=candidate(k),pairs=[];
  for(const pair of [[0,1],[0,2],[1,2]]){
    const result=pairCover(k,...pair);
    const entry={colors:pair,value:result.matching};
    if(result.matching<prediction.value){
      entry.witness=result.selected.map(i=>({index:i+1,...points[i],v:points[i].v.toString()}));
    }
    pairs.push(entry);
  }
  const record={k,t:points[k-1].v.toString(),prediction,pairs};
  records.push(record);
  console.log(JSON.stringify({...record,pairs:pairs.map(({witness,...x})=>x)}));
  if(pairs.some(p=>p.value<prediction.value))break;
}
fs.writeFileSync(path.join(__dirname,'168_two_color_results.json'),JSON.stringify(records,null,2));
