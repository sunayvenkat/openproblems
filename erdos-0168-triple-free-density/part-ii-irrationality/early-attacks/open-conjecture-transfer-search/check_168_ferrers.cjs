const fs=require('fs'),path=require('path');
const width=Number(process.argv[2]||8),height=Number(process.argv[3]||8),strict=process.argv.includes('--strict'),linear=process.argv.includes('--linear'),balanced=process.argv.includes('--balanced');
function compare(a,b){if(a===null)return b===null?0:1;if(b===null)return -1;return Math.sign(a[0]*b[1]-b[0]*a[1]);}
function boundsAfter(rows,next,lo,hi){
  const b=rows.length;
  for(let i=0;i<b;i++){
    const lower=[rows[i]-next-1,b-i],upper=[rows[i]-next+1,b-i];
    if(compare(lower,lo)>0)lo=lower;
    if(compare(upper,hi)<0)hi=upper;
  }
  return compare(lo,hi)<0?[lo,hi]:null;
}
function completeTriangle(rows,lo,hi){
  for(let i=0;i<rows.length;i++){
    const lower=[rows[i]-1,rows.length-i];
    if(compare(lower,lo)>0)lo=lower;
  }
  return compare(lo,hi)<0;
}
function popcount(x){let c=0;while(x){x&=x-1;c++;}return c;}
function advance(dp,previous,w,trace=false){
    const anchors=Math.min(w,previous-1), am=(1<<anchors)-1;
    const best=new Array(1<<w).fill(Infinity);
    const predecessor=trace?new Int32Array(1<<w).fill(-1):null;
    for(let m=0;m<dp.length;m++){
      const r=(~m)&(~(m>>1))&am;
      if(dp[m]<best[r]){best[r]=dp[m];if(trace)predecessor[r]=m;}
    }
    for(let bit=1;bit<(1<<w);bit<<=1)for(let m=0;m<(1<<w);m++)if((m&bit)&&best[m^bit]<best[m]){best[m]=best[m^bit];if(trace)predecessor[m]=predecessor[m^bit];}
    const result=best.map((x,m)=>x+popcount(m));
    return trace?{dp:result,predecessor}:result;
}
function exactCover(rows){
  let dp=Array.from({length:1<<rows[0]},(_,m)=>popcount(m));const history=[];
  for(let b=1;b<rows.length;b++){const next=advance(dp,rows[b-1],rows[b],true);dp=next.dp;history.push(next.predecessor);}
  let mask=0;for(let m=1;m<dp.length;m++)if(dp[m]<dp[mask])mask=m;
  const value=dp[mask],masks=new Array(rows.length);masks[rows.length-1]=mask;
  for(let b=rows.length-1;b>0;b--){mask=history[b-1][mask];masks[b-1]=mask;}
  for(let b=0;b+1<rows.length;b++){
    const am=(1<<Math.min(rows[b]-1,rows[b+1]))-1;
    if(((~masks[b])&(~(masks[b]>>1))&(~masks[b+1])&am)!==0)throw Error('invalid reconstructed cover');
  }
  if(masks.reduce((s,m)=>s+popcount(m),0)!==value)throw Error('cover size mismatch');
  return{value,masks};
}
function mvc(rows,c1,c2,added=new Set()){
  const indices=rows.map(w=>new Array(w)),colors=[];let n=0;
  for(let b=0;b<rows.length;b++)for(let a=0;a<rows[b];a++){indices[b][a]=n++;colors.push((a+2*b)%3);}
  const adj=Array.from({length:n},()=>[]);
  for(let b=0;b+1<rows.length;b++)for(let a=0;a<Math.min(rows[b]-1,rows[b+1]);a++){
    const edge=[indices[b][a],indices[b][a+1],indices[b+1][a]];
    if(edge.some(i=>added.has(i)))continue;
    const l=edge.find(i=>colors[i]===c1),r=edge.find(i=>colors[i]===c2);
    adj[l].push(r);
  }
  const matched=new Int32Array(n).fill(-1);let answer=0;
  function augment(l,seen){for(const r of adj[l])if(!seen[r]){seen[r]=1;if(matched[r]<0||augment(matched[r],seen)){matched[r]=l;return true;}}return false;}
  for(let i=0;i<n;i++)if(colors[i]===c1&&augment(i,new Uint8Array(n)))answer++;
  return answer;
}
let checked=0,found=null;
function walk(rows,max,dp,lo=[0,1],hi=null){
  if(found)return;
  if(rows.length&&(!strict||rows[rows.length-1]<=2)&&(!linear||completeTriangle(rows,lo,hi))){
    let exact=Infinity;for(const value of dp)exact=Math.min(exact,value);
    const pairs=[[0,1],[0,2],[1,2]].map(([a,b])=>mvc(rows,a,b));checked++;
    if(exact<Math.min(...pairs)){found={rows:[...rows],exact,pairs};return;}
  }
  if(rows.length===height||(strict&&rows.length&&rows[rows.length-1]<=1))return;
  if(strict&&rows.length){
    for(const next of [rows[rows.length-1]-1,rows[rows.length-1]-2])if(next>0)walk([...rows,next],next,advance(dp,rows[rows.length-1],next));
  }else for(let next=1;next<=max;next++){
    const bounds=linear?boundsAfter(rows,next,lo,hi):[lo,hi];
    if(bounds)walk([...rows,next],next,rows.length?advance(dp,rows[rows.length-1],next):Array.from({length:1<<next},(_,m)=>popcount(m)),...bounds);
  }
}
if(require.main===module){
  walk([],width,null,balanced?[1,1]:[0,1],balanced?[2,1]:null);
  const out={width,height,strict,linear,balanced,checked,found};
  console.log(JSON.stringify(out));
  fs.writeFileSync(path.join(__dirname,balanced?'168_ferrers_balanced_results.json':linear?'168_ferrers_linear_results.json':strict?'168_ferrers_strict_results.json':'168_ferrers_results.json'),JSON.stringify(out,null,2));
}
module.exports={mvc,advance,popcount,exactCover};
