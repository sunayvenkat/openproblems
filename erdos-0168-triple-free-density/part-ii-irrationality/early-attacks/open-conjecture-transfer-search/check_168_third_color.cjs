const fs=require('fs'),path=require('path');
const {mvc}=require('./check_168_ferrers.cjs');
const count=Number(process.argv[2]||10000);
function smoothThreshold(k){const a=[1n];let i=0,j=0;while(a.length<k){const x=2n*a[i],y=3n*a[j];a.push(x<y?x:y);if(x<=y)i++;if(y<=x)j++;}return a[k-1];}
const t=count>0?smoothThreshold(count):null;
const rows=[];
if(t!==null)for(let q=t;q>0n;q/=3n)rows.push(q.toString(2).length);
else rows.push(21,20,18,16,15,14,12,10,9,8,6,4,2);
const vertices=[];
for(let b=0;b<rows.length;b++)for(let a=0;a<rows[b];a++)vertices.push({a,b,color:(a+2*b)%3});
const pairs=[[0,1],[0,2],[1,2]];
const base=pairs.map(([a,b])=>mvc(rows,a,b));
const best=Math.min(...base);
let examined=0,found=null;
for(let z=0;z<vertices.length&&!found;z++){
  const pair=pairs.find(p=>!p.includes(vertices[z].color));
  const restricted=1+mvc(rows,...pair,new Set([z]));examined++;
  if(restricted<best)found={z,vertex:vertices[z],pair,value:restricted};
  if(examined%500===0)console.log(JSON.stringify({examined,vertices:vertices.length,best}));
}
const out={count,t:t?.toString(),rows,base,best,examined,found};
console.log(JSON.stringify(out));
fs.writeFileSync(path.join(__dirname,'168_third_color_results.json'),JSON.stringify(out,null,2));
