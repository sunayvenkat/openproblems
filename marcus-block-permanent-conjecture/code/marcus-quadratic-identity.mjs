import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';

// Exact symbolic Einstein-contraction verification, independent of numeric fits.
// Each vertex is one symmetric quadratic matrix; an edge contracts a holomorphic
// index with an antiholomorphic index. Its 3x3 incidence table specifies the term.
const vertex=(block,bar,...indices)=>({block,bar,indices});
const term=(coefficient,...vertices)=>({coefficient,vertices});
const scale=(terms,c)=>terms.map(t=>({...t,coefficient:c*t.coefficient}));
function rename(terms,map){return terms.map(t=>({...t,vertices:t.vertices.map(v=>({...v,indices:v.indices.map(x=>map[x]??x)}))}));}
function covariants(a,b,c){
  const u=[term(1,vertex(a,false,'a','b'),vertex(b,false,'c','e'),vertex(c,true,'d','e'))];
  const v=[term(1,vertex(b,false,'a','b'),vertex(a,false,'c','e'),vertex(c,true,'d','e'))];
  const t=[...u,...v],s=[...t,...rename(t,{b:'c',c:'b'}),...rename(t,{a:'b',b:'c',c:'a'})];
  const h=[...scale(t,3),...scale(s,-1)];
  const w=[
    term(1,vertex(a,false,'a','e'),vertex(b,false,'f','b'),vertex(c,true,'e','f')),
    term(1,vertex(b,false,'a','e'),vertex(a,false,'f','b'),vertex(c,true,'e','f')),
  ];
  const l=[
    term(1,vertex(a,false,'a','b'),vertex(b,false,'e','f'),vertex(c,true,'e','f')),
    term(1,vertex(b,false,'a','b'),vertex(a,false,'e','f'),vertex(c,true,'e','f')),
  ];
  return{t,s,h,w,l};
}
function innerDiagrams(x,y,boundary){
  const out=new Map();
  for(const left of x)for(const right of y){
    const edges=new Map();
    for(const [side,t]of [[0,left],[1,right]])for(const v of t.vertices)for(const index of v.indices){
      const key=boundary.includes(index)?index:`${side}:${index}`;
      const vertices=edges.get(key)??[];vertices.push({block:v.block,bar:side===0?!v.bar:v.bar});edges.set(key,vertices);
    }
    const table=Array(9).fill(0);
    for(const pair of edges.values()){
      assert.equal(pair.length,2);assert.notEqual(pair[0].bar,pair[1].bar);
      const hol=pair.find(v=>!v.bar),anti=pair.find(v=>v.bar);table[3*hol.block+anti.block]++;
    }
    for(let i=0;i<3;i++){assert.equal(table.slice(3*i,3*i+3).reduce((s,x)=>s+x,0),2);assert.equal(table[i]+table[i+3]+table[i+6],2);}
    const key=table.join('');out.set(key,(out.get(key)??0)+left.coefficient*right.coefficient);
  }return out;
}
function add(target,source,multiplier){for(const[key,value]of source)target.set(key,(target.get(key)??0)+multiplier*value);}
const rhs=new Map(),parts={S:new Map(),H:new Map(),W:new Map(),cross:new Map()};
for(let c=0;c<3;c++){
  const[a,b]=[0,1,2].filter(i=>i!==c),{s,h,w,l}=covariants(a,b,c);
  add(rhs,innerDiagrams(s,s,'abcd'),112);
  add(rhs,innerDiagrams(h,h,'abcd'),16);
  add(rhs,innerDiagrams(w,w,'ab'),288);
  add(rhs,innerDiagrams(w,l,'ab'),108);
  add(rhs,innerDiagrams(l,w,'ab'),108);
  add(parts.S,innerDiagrams(s,s,'abcd'),1);
  add(parts.H,innerDiagrams(h,h,'abcd'),1);
  add(parts.W,innerDiagrams(w,w,'ab'),1);
  add(parts.cross,innerDiagrams(w,l,'ab'),1);
  add(parts.cross,innerDiagrams(l,w,'ab'),1);
}
const lhs=new Map();let included=0,excluded=0;
function permutations(row,used,p){
  if(row===6){
    const blockPreserving=[0,1,2].every(i=>Math.floor(p[2*i]/2)===Math.floor(p[2*i+1]/2));
    if(blockPreserving){excluded++;return;}
    const table=Array(9).fill(0);for(let i=0;i<6;i++)table[3*Math.floor(i/2)+Math.floor(p[i]/2)]++;
    const key=table.join('');lhs.set(key,(lhs.get(key)??0)+27);included++;return;
  }
  for(let j=0;j<6;j++)if(!(used&(1<<j)))permutations(row+1,used|(1<<j),[...p,j]);
}
permutations(0,0,[]);assert.equal(included,672);assert.equal(excluded,48);
const keys=[...new Set([...lhs.keys(),...rhs.keys()])].sort();
for(const key of keys)assert.equal(rhs.get(key)??0,lhs.get(key)??0,`Diagram ${key}`);
const diagrams=keys.map(key=>({table:key,target:(lhs.get(key)??0)/27,S:parts.S.get(key)??0,H:parts.H.get(key)??0,W:parts.W.get(key)??0,cross:parts.cross.get(key)??0,lhs:lhs.get(key)??0,rhs:rhs.get(key)??0}));
const types=new Map();for(const d of diagrams){const key=[d.target,d.S,d.H,d.W,d.cross].join(',');const row=types.get(key)??{count:0,representative:d.table,target:d.target,S:d.S,H:d.H,W:d.W,cross:d.cross};row.count++;types.set(key,row);}
const result={identity:'27 F = sum_centers (112 ||S||^2 + 16 ||H||^2 + 288 ||W||^2 + 216 Re<W,L>)',included,excluded,diagrams,types:[...types.values()]};
writeFileSync('marcus-quadratic-identity.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({verified:true,included,excluded,nonzeroDiagrams:keys.filter(key=>lhs.get(key)).length,diagrams:keys.length}));
console.log(JSON.stringify(result.types));
