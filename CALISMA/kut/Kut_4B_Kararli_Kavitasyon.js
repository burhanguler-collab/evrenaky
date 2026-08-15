(() => {
  'use strict';
  const TAU = Math.PI * 2;
  const $ = id => document.getElementById(id);
  const css = name => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  const field = $('field'), ctx = field.getContext('2d');
  const radial = $('radialChart'), rctx = radial.getContext('2d');
  const history = $('historyChart'), hctx = history.getContext('2d');
  const world = { xmin:-6, xmax:6, ymin:-4.3, ymax:4.3 };

  let kuts = [], running = false, time = 0, steps = 0, last = performance.now();
  let activePreset = 'cav', addSign = 1, drag = null, trails = [], historyData = [];
  let radialData = [], events = [], lastDiag = -1, lastVisible = -1;
  let metrics = { gamma:0, boundary:0, omega:0, enstrophy:0, normError:0, dipole:0, minD4:0, visible:0, meanSection:0 };

  const p = () => ({
    viewXW:+$('nu').value, R4:+$('core').value, gamma:+$('gamma').value,
    viewYZ:+$('sound').value, sliceW:+$('ambientP').value,
    speed:+$('speed').value, showSections:$('cavitationOn').checked
  });

  function q4(x,y,z,w,g,R4,id){ return {x,y,z,w,g,R4,id}; }
  function ring(n,r,g,R4){
    return Array.from({length:n},(_,i)=>{
      const a=TAU*i/n, wob=.26*Math.sin(2*a), dep=.22*Math.cos(3*a);
      return q4(r*Math.cos(a),r*Math.sin(a),dep,wob,g,R4,i+1);
    });
  }
  const scenarios = {
    cav:{name:'Kararlı 4B kavitasyon örgüsü',make:(g,R)=>[
      q4(-1.15,-.72,.18,-.24,g,R,1),q4(1.15,-.72,-.18,.24,g,R,2),
      q4(1.15,.72,.24,-.18,g,R,3),q4(-1.15,.72,-.24,.18,g,R,4)
    ]},
    pair:{name:'4B eşdönüşlü Kut çifti',make:(g,R)=>[q4(-1.25,0,.18,-.2,g,R,1),q4(1.25,0,-.18,.2,g,R,2)]},
    dipole:{name:'4B zıt işaretli dipol sınaması',make:(g,R)=>[q4(0,-.78,.2,.16,g,R,1),q4(0,.78,-.2,-.16,-g,R,2)]},
    ring7:{name:'N = 7 · 4B kritik halka',make:(g,R)=>ring(7,2.25,g,R)},
    ring8:{name:'N = 8 · 4B halka',make:(g,R)=>ring(8,2.25,g,R)},
    mixed:{name:'4B karışık işaret sınaması',make:(g,R)=>[
      q4(-1.7,-.7,.2,-.2,g,R,1),q4(-.3,1.2,-.2,.25,g,R,2),q4(1.45,-.45,.15,.18,g,R,3),
      q4(-1.25,.7,-.15,-.18,-g,R,4),q4(.45,-1.25,.22,-.25,-g,R,5),q4(1.65,.9,-.22,.2,-g,R,6)
    ]}
  };

  function setOutputs(){
    const a=p();
    $('nuOut').value=a.viewXW.toFixed(2); $('coreOut').value=a.R4.toFixed(2)+' L';
    $('gammaOut').value=a.gamma.toFixed(2); $('soundOut').value=a.viewYZ.toFixed(2);
    $('ambientPOut').value=a.sliceW.toFixed(2)+' L'; $('speedOut').value=a.speed.toFixed(1)+'×';
  }
  function log(msg){
    events.unshift({t:time,msg}); events=events.slice(0,5);
    $('eventLog').innerHTML=events.map(e=>`<div class="event"><time>${e.t.toFixed(2)} T</time><span>${e.msg}</span></div>`).join('');
  }
  function reset(name=activePreset){
    activePreset=name; const a=p();
    kuts=scenarios[name].make(a.gamma,a.R4); time=0; steps=0; trails=[]; historyData=[]; radialData=[]; events=[]; lastDiag=-1; lastVisible=-1;
    document.querySelectorAll('.preset').forEach(b=>b.classList.toggle('active',b.dataset.preset===name));
    $('scenarioName').textContent=scenarios[name].name;
    log('Kararlı 4B Kutlar kuruldu; her biri için R₄ sabit.');
    diagnose(true); draw();
  }

  function rotate4(q,t=time){
    const a=p(), ax=t*a.viewXW, ay=t*a.viewYZ, c1=Math.cos(ax),s1=Math.sin(ax),c2=Math.cos(ay),s2=Math.sin(ay);
    return {x:c1*q.x-s1*q.w, y:c2*q.y-s2*q.z, z:s2*q.y+c2*q.z, w:s1*q.x+c1*q.w, g:q.g, R4:q.R4, id:q.id};
  }
  function d4(a,b){ return Math.hypot(a.x-b.x,a.y-b.y,a.z-b.z,a.w-b.w); }
  function sectionRadius(q,slice=p().sliceW){ const dw=q.w-slice; return Math.abs(dw)<q.R4 ? Math.sqrt(Math.max(0,q.R4*q.R4-dw*dw)) : 0; }

  /* 4B kuram girdisi: iki ortogonal dönme düzlemindeki kompleks yapı J.
     J(dx,dy,dz,dw)=(-dy,dx,-dw,dz). Bu seçim J^T J=I ve J^2=-I sağlar. */
  function induced(q,state=kuts,skip=-1){
    let vx=0,vy=0,vz=0,vw=0;
    for(let j=0;j<state.length;j++){
      if(j===skip)continue; const s=state[j];
      const dx=q.x-s.x,dy=q.y-s.y,dz=q.z-s.z,dw=q.w-s.w,r2=dx*dx+dy*dy+dz*dz+dw*dw;
      if(r2<1e-12)continue;
      const soft=s.R4*s.R4, k=s.g/TAU*(1-Math.exp(-r2/soft))/r2;
      vx+=-dy*k; vy+=dx*k; vz+=-dw*k; vw+=dz*k;
    }
    return {x:vx,y:vy,z:vz,w:vw};
  }
  function deriv(state){ return state.map((q,i)=>induced(q,state,i)); }
  function stage(base,k,h){ return base.map((q,i)=>({...q,x:q.x+k[i].x*h,y:q.y+k[i].y*h,z:q.z+k[i].z*h,w:q.w+k[i].w*h})); }
  function stepRK4(dt){
    const b=kuts.map(q=>({...q})),k1=deriv(b),k2=deriv(stage(b,k1,dt/2)),k3=deriv(stage(b,k2,dt/2)),k4=deriv(stage(b,k3,dt));
    kuts.forEach((q,i)=>{q.x=b[i].x+dt*(k1[i].x+2*k2[i].x+2*k3[i].x+k4[i].x)/6;q.y=b[i].y+dt*(k1[i].y+2*k2[i].y+2*k3[i].y+k4[i].y)/6;q.z=b[i].z+dt*(k1[i].z+2*k2[i].z+2*k3[i].z+k4[i].z)/6;q.w=b[i].w+dt*(k1[i].w+2*k2[i].w+2*k3[i].w+k4[i].w)/6;});
    time+=dt;steps++;
    if(steps%4===0){trails.push(kuts.map(q=>rotate4(q)));if(trails.length>170)trails.shift();}
  }

  function probe4(x,y){ return {x,y,z:0,w:p().sliceW}; }
  function omegaAt(x,y){
    const q=probe4(x,y); let o=0;
    for(const s0 of kuts){const s=rotate4(s0),r=d4(q,s);o+=s.g/(Math.PI*s.R4*s.R4)*Math.exp(-(r*r)/(s.R4*s.R4));}
    return o;
  }
  function velocityAt(x,y){return induced(probe4(x,y),kuts.map(q=>rotate4(q)),-1);}
  function centerView(){
    const vs=kuts.map(q=>rotate4(q));let sx=0,sy=0,w=0;for(const q of vs){const a=Math.abs(q.g);sx+=a*q.x;sy+=a*q.y;w+=a;}return{x:sx/(w||1),y:sy/(w||1)};
  }
  function diagnose(force=false){
    if(!force&&time-lastDiag<.12)return;lastDiag=time;
    const a=p(),vs=kuts.map(q=>rotate4(q)),N=56,M=40,dx=(world.xmax-world.xmin)/N,dy=(world.ymax-world.ymin)/M;
    let maxO=0,maxU=0,en=0,normError=0,dip=[0,0,0,0],minD=Infinity;
    for(let iy=0;iy<M;iy++)for(let ix=0;ix<N;ix++){
      const x=world.xmin+(ix+.5)*dx,y=world.ymin+(iy+.5)*dy,o=omegaAt(x,y),u=velocityAt(x,y),um=Math.hypot(u.x,u.y,u.z,u.w);
      maxO=Math.max(maxO,Math.abs(o));maxU=Math.max(maxU,um);en+=o*o*dx*dy;
    }
    for(let i=0;i<kuts.length;i++){
      const q=kuts[i],v=vs[i],n0=Math.hypot(q.x,q.y,q.z,q.w),n1=Math.hypot(v.x,v.y,v.z,v.w);
      normError=Math.max(normError,Math.abs(n1-n0));dip[0]+=q.g*q.x;dip[1]+=q.g*q.y;dip[2]+=q.g*q.z;dip[3]+=q.g*q.w;
      for(let j=i+1;j<kuts.length;j++)minD=Math.min(minD,d4(q,kuts[j]));
    }
    const sections=vs.map(q=>sectionRadius(q,a.sliceW)),visible=sections.filter(r=>r>0),mean=visible.reduce((s,r)=>s+r,0)/(visible.length||1);
    const c=centerView(),bins=40,angles=44,arr=[];let boundary=0;
    for(let b=0;b<bins;b++){const r=.08+b*4.9/(bins-1);let u2=0;for(let k=0;k<angles;k++){const z=TAU*k/angles,u=velocityAt(c.x+r*Math.cos(z),c.y+r*Math.sin(z));u2+=u.x*u.x+u.y*u.y;}const ur=Math.sqrt(u2/angles);boundary=Math.max(boundary,ur);let enc=0;for(let i=0;i<vs.length;i++){const dd=Math.hypot(vs[i].x-c.x,vs[i].y-c.y),f=.5*(1+Math.tanh((r-dd)/(vs[i].R4*.7+.04)));enc+=vs[i].g*f;}arr.push({r,u:ur,g:enc});}
    metrics={gamma:kuts.reduce((s,q)=>s+q.g,0),boundary,omega:maxO,enstrophy:en,normError,dipole:Math.hypot(...dip),minD4:Number.isFinite(minD)?minD:0,visible:visible.length,meanSection:mean};radialData=arr;
    if(lastVisible>=0&&visible.length!==lastVisible)log(`3B kesitte görünen Kut sayısı ${lastVisible} → ${visible.length}; R₄ değişmedi.`);lastVisible=visible.length;
    if(!historyData.length||time-historyData.at(-1).t>.16){historyData.push({t:time,v:visible.length,r:mean,e:normError});while(historyData.length&&time-historyData[0].t>24)historyData.shift();}
    updateDiagnostics();drawCharts();
  }

  function fmtSigned(x){return(x>=0?'+':'−')+Math.abs(x).toFixed(2);}
  function updateDiagnostics(){
    const a=p();$('mGamma').textContent=fmtSigned(metrics.gamma);$('mBoundary').textContent=metrics.boundary.toFixed(2);$('mOmega').textContent=metrics.omega.toFixed(2);$('mMach').textContent=metrics.normError.toExponential(1);$('mCore').textContent=a.R4.toFixed(2);$('mDipole').textContent=metrics.dipole.toFixed(2);$('mPressure').textContent=metrics.minD4.toFixed(2);$('mCavity').textContent=`${metrics.visible} / ${kuts.length}`;$('particleCount').textContent=`${kuts.length} sabit Kut · ${metrics.visible} kesit`;$('clock').textContent=`t = ${time.toFixed(2)} T · adım ${steps}`;
    const val=$('validity');val.className='validity'+(metrics.normError>1e-10?' bad':'');val.textContent=metrics.normError>1e-10?'SO(4) norm korunumunda hata':'4B norm ve R₄ korunuyor';
    const overlap=kuts.length>1?Math.max(0,Math.min(1,(2*a.R4-metrics.minD4)/(2*a.R4))):0,pct=Math.round(overlap*100);$('overlapText').textContent=pct+'%';$('overlapBar').style.width=pct+'%';$('overlapBar').style.background=pct>65?'var(--cyan)':pct>20?'var(--gold)':'var(--good)';
    $('statusTitle').textContent='Kararlı 4B kavitasyon — Kut büyümez';
    $('statusCopy').textContent=`Her Kut için R₄=${a.R4.toFixed(2)} sabit. Kesitte ${metrics.visible}/${kuts.length} Kut görünüyor; ortalama görünen r₃=${metrics.meanSection.toFixed(2)}. Değişen yalnız 3B izdüşümdür.`;
  }

  function resizeCanvas(canvas,c){const dpr=Math.min(devicePixelRatio||1,2),r=canvas.getBoundingClientRect(),w=Math.max(1,Math.round(r.width*dpr)),h=Math.max(1,Math.round(r.height*dpr));if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h;c.setTransform(dpr,0,0,dpr,0,0);}return{w:r.width,h:r.height};}
  function map(x,y,W,H){return{x:(x-world.xmin)/(world.xmax-world.xmin)*W,y:H-(y-world.ymin)/(world.ymax-world.ymin)*H};}
  function unmap(x,y,W,H){return{x:world.xmin+x/W*(world.xmax-world.xmin),y:world.ymin+(H-y)/H*(world.ymax-world.ymin)};}
  function draw(){
    const {w:W,h:H}=resizeCanvas(field,ctx);ctx.clearRect(0,0,W,H);ctx.fillStyle='#050b0c';ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='rgba(135,170,168,.07)';ctx.lineWidth=1;for(let x=-5;x<=5;x++){const q=map(x,0,W,H);ctx.beginPath();ctx.moveTo(q.x,0);ctx.lineTo(q.x,H);ctx.stroke();}for(let y=-4;y<=4;y++){const q=map(0,y,W,H);ctx.beginPath();ctx.moveTo(0,q.y);ctx.lineTo(W,q.y);ctx.stroke();}
    if($('showField').checked)drawField(W,H);if($('showTrails').checked)drawTrails(W,H);if($('showVectors').checked)drawVectors(W,H);drawKuts(W,H);
  }
  function drawField(W,H){const nx=Math.max(60,Math.floor(W/9)),ny=Math.max(42,Math.floor(H/9)),cw=W/nx,ch=H/ny,ref=Math.max(metrics.omega,.1);for(let iy=0;iy<ny;iy++)for(let ix=0;ix<nx;ix++){const p0=unmap((ix+.5)*cw,(iy+.5)*ch,W,H),o=omegaAt(p0.x,p0.y),q=Math.min(1,Math.abs(o)/ref),al=.025+.4*Math.pow(q,.65);ctx.fillStyle=o>=0?`rgba(63,221,207,${al})`:`rgba(255,103,80,${al})`;ctx.fillRect(ix*cw,iy*ch,cw+1,ch+1);}}
  function drawVectors(W,H){ctx.save();ctx.strokeStyle='rgba(241,197,107,.42)';ctx.fillStyle='rgba(241,197,107,.55)';ctx.lineWidth=1;const gap=W<600?54:47;for(let py=55;py<H-38;py+=gap)for(let px=30;px<W-20;px+=gap){const q=unmap(px,py,W,H),u=velocityAt(q.x,q.y),m=Math.hypot(u.x,u.y);if(m<.015)continue;const L=Math.min(16,3+7*Math.log1p(m)),ex=px+u.x/m*L,ey=py-u.y/m*L;ctx.beginPath();ctx.moveTo(px,py);ctx.lineTo(ex,ey);ctx.stroke();ctx.beginPath();ctx.arc(ex,ey,1.4,0,TAU);ctx.fill();}ctx.restore();}
  function drawTrails(W,H){if(trails.length<2)return;ctx.save();ctx.lineWidth=1;for(let i=0;i<kuts.length;i++){ctx.strokeStyle=kuts[i].g>=0?'rgba(98,216,207,.25)':'rgba(255,128,104,.25)';ctx.beginPath();let go=false;for(const f of trails){if(!f[i])continue;const q=map(f[i].x,f[i].y,W,H);go?ctx.lineTo(q.x,q.y):(ctx.moveTo(q.x,q.y),go=true);}ctx.stroke();}ctx.restore();}
  function drawKuts(W,H){
    const scale=Math.min(W/(world.xmax-world.xmin),H/(world.ymax-world.ymin)),a=p();
    kuts.map(q=>rotate4(q)).forEach((q,i)=>{const s=map(q.x,q.y,W,H),r3=sectionRadius(q,a.sliceW)*scale,R=q.R4*scale,base=q.g>=0?css('--cyan'):css('--coral');ctx.save();
      ctx.strokeStyle=q.g>=0?'rgba(98,216,207,.42)':'rgba(255,128,104,.42)';ctx.setLineDash([3,4]);ctx.beginPath();ctx.arc(s.x,s.y,R,0,TAU);ctx.stroke();ctx.setLineDash([]);
      if(a.showSections&&r3>0){const gr=ctx.createRadialGradient(s.x-r3*.25,s.y-r3*.28,0,s.x,s.y,r3);gr.addColorStop(0,'rgba(255,255,255,.78)');gr.addColorStop(.24,q.g>=0?'rgba(98,216,207,.38)':'rgba(255,128,104,.38)');gr.addColorStop(1,'rgba(8,18,20,.12)');ctx.fillStyle=gr;ctx.strokeStyle=base;ctx.lineWidth=1.3;ctx.beginPath();ctx.arc(s.x,s.y,r3,0,TAU);ctx.fill();ctx.stroke();}
      ctx.fillStyle=base;ctx.beginPath();ctx.arc(s.x,s.y,3.5,0,TAU);ctx.fill();ctx.fillStyle=css('--muted');ctx.font='9px ui-monospace';ctx.textAlign='center';ctx.fillText(`w=${q.w.toFixed(2)}`,s.x,s.y+R+12);if(drag===i){ctx.strokeStyle='#fff';ctx.beginPath();ctx.arc(s.x,s.y,R+5,0,TAU);ctx.stroke();}ctx.restore();
    });
  }

  function chartBase(canvas,c){const s=resizeCanvas(canvas,c),W=s.w,H=s.h,pad={l:43,r:15,t:9,b:25};c.clearRect(0,0,W,H);c.strokeStyle='rgba(120,150,149,.22)';c.strokeRect(pad.l+.5,pad.t+.5,W-pad.l-pad.r,H-pad.t-pad.b);c.font='9px ui-monospace';c.fillStyle=css('--muted');c.textAlign='center';c.fillText('0',pad.l,H-7);return{W,H,pad};}
  function path(c,data,x,y,color){if(data.length<2)return;c.strokeStyle=color;c.lineWidth=1.6;c.beginPath();data.forEach((d,i)=>i?c.lineTo(x(d),y(d)):c.moveTo(x(d),y(d)));c.stroke();}
  function drawCharts(){drawRadial();drawHistory();}
  function drawRadial(){const {W,H,pad}=chartBase(radial,rctx);if(!radialData.length)return;const umax=Math.max(...radialData.map(d=>d.u),.1),gmax=Math.max(...radialData.map(d=>Math.abs(d.g)),.1),x=d=>pad.l+d.r/5*(W-pad.l-pad.r),yu=d=>H-pad.b-d.u/umax*(H-pad.t-pad.b),yg=d=>H-pad.b-(d.g/gmax*.43+.5)*(H-pad.t-pad.b);path(rctx,radialData,x,yu,css('--cyan'));path(rctx,radialData,x,yg,css('--coral'));rctx.fillStyle=css('--muted');rctx.textAlign='right';rctx.fillText(umax.toFixed(2),pad.l-5,pad.t+5);rctx.fillText('r / L',W-pad.r,H-7);}
  function drawHistory(){const {W,H,pad}=chartBase(history,hctx);if(historyData.length<2)return;const t0=historyData[0].t,t1=Math.max(time,t0+.01),mv=Math.max(...historyData.map(d=>d.v),1),mr=Math.max(...historyData.map(d=>d.r),.01),me=Math.max(...historyData.map(d=>d.e),1e-15),x=d=>pad.l+(d.t-t0)/(t1-t0)*(W-pad.l-pad.r),yy=(k,m)=>d=>H-pad.b-d[k]/m*(H-pad.t-pad.b);path(hctx,historyData,x,yy('v',mv),css('--cyan'));path(hctx,historyData,x,yy('r',mr),css('--gold'));path(hctx,historyData,x,yy('e',me),css('--coral'));hctx.fillStyle=css('--muted');hctx.textAlign='right';hctx.fillText('ölçekli',pad.l-5,pad.t+5);hctx.fillText('t / T',W-pad.r,H-7);}

  function frame(now){const elapsed=Math.min(.05,(now-last)/1000);last=now;if(running){let left=elapsed*p().speed;while(left>0){const h=Math.min(.006,left);stepRK4(h);left-=h;}diagnose();draw();}requestAnimationFrame(frame);}
  function toggle(){running=!running;$('playBtn').textContent=running?'Ⅱ Duraklat':'▶ Başlat';}
  document.querySelectorAll('.preset').forEach(b=>b.addEventListener('click',()=>reset(b.dataset.preset)));
  $('playBtn').addEventListener('click',toggle);$('resetBtn').addEventListener('click',()=>reset());$('stepBtn').addEventListener('click',()=>{stepRK4(.025);diagnose(true);draw();});
  ['nu','sound','ambientP','speed'].forEach(id=>$(id).addEventListener('input',()=>{setOutputs();diagnose(true);draw();}));
  ['core','gamma'].forEach(id=>$(id).addEventListener('input',()=>{setOutputs();reset();}));
  ['cavitationOn','showField','showVectors','showTrails'].forEach(id=>$(id).addEventListener('change',()=>{diagnose(true);draw();}));
  $('addPos').addEventListener('click',()=>{addSign=1;log('Ekleme modu: +Γ sabit 4B Kut.');});$('addNeg').addEventListener('click',()=>{addSign=-1;log('Ekleme modu: −Γ 4B sınama Kutu.');});
  field.addEventListener('pointerdown',e=>{const r=field.getBoundingClientRect(),m=unmap(e.clientX-r.left,e.clientY-r.top,r.width,r.height),vs=kuts.map(q=>rotate4(q));let best=-1,bd=.45;vs.forEach((q,i)=>{const d=Math.hypot(q.x-m.x,q.y-m.y);if(d<bd){bd=d;best=i;}});if(best>=0){drag=best;field.setPointerCapture(e.pointerId);}else{const a=p(),sg=e.shiftKey?-1:addSign;kuts.push(q4(m.x,m.y,0,a.sliceW,sg*a.gamma,a.R4,Date.now()));log(`${sg>0?'+Γ':'−Γ'} sabit 4B Kut eklendi.`);diagnose(true);draw();}});
  field.addEventListener('pointermove',e=>{if(drag===null)return;const r=field.getBoundingClientRect(),m=unmap(e.clientX-r.left,e.clientY-r.top,r.width,r.height);kuts[drag].x=m.x;kuts[drag].y=m.y;trails=[];diagnose(true);draw();});field.addEventListener('pointerup',()=>drag=null);field.addEventListener('pointercancel',()=>drag=null);
  window.addEventListener('resize',()=>{draw();drawCharts();});

  function selfTests(){
    const tests=[],near=(a,b,t=1e-10)=>Math.abs(a-b)<t,a=p();
    const q=q4(.7,-1.1,.4,.8,1,a.R4,1),r=rotate4(q,1.234);tests.push(near(Math.hypot(q.x,q.y,q.z,q.w),Math.hypot(r.x,r.y,r.z,r.w)));
    tests.push(near(sectionRadius({...q,w:a.sliceW,R4:a.R4}),a.R4));
    tests.push(sectionRadius({...q,w:a.sliceW+2*a.R4,R4:a.R4})===0);
    tests.push(near(d4({x:0,y:0,z:0,w:0},{x:0,y:0,z:0,w:3}),3));
    const Rbefore=q.R4; q.x+=1;tests.push(q.R4===Rbefore);
    const pair=[q4(-1,0,0,0,1,a.R4,1),q4(1,0,0,0,1,a.R4,2)],d=deriv(pair);tests.push(d[0].y<0&&d[1].y>0);
    $('testStatus').textContent=`${tests.filter(Boolean).length}/${tests.length} 4B matematik öz sınaması geçti · fiziksel doğrulama değildir`;return tests.every(Boolean);
  }
  setOutputs();reset('cav');selfTests();requestAnimationFrame(frame);
  window.__kutLab={get state(){return{kuts:kuts.map(q=>({...q})),time,metrics:{...metrics},running};},reset,step:(dt=.01)=>{stepRK4(dt);diagnose(true);draw();},rotate4,d4,sectionRadius,selfTests};
})();
