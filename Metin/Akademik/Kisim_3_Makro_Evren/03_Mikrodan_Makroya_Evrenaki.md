# 3.3 Mikrodan Makroya Evrenakı (Kütle ve Gradyan İlişkisi)


## 3.3.1 Makro Kütle Evrenakı Merkezcil Gradyanları

Bir maddenin Evrenakı içindeki optik ve fiziksel davranışı, yalnızca tekil atomların değil, trilyonlarca atomun bir araya gelerek oluşturduğu **ortak makro alanın (birleşik gradyanın)** sonucudur. Tek tek incelendiğinde her atom kendi etrafında mikro bir sınır tabakası yaratır. Ancak bu atomlar birleşip makro bir kütle (örneğin bir cam parçası) oluşturduğunda, bu mikro alanlar üst üste binerek kesintisiz ve devasa bir "ortak deplasman havuzu" (düşük Evrenakı yoğunluğu alanı) meydana getirir. İşte ışığın madde içindeki yavaşlamasını ve yön değiştirmesini dikte eden asıl yapı, atomların tek tek sahip olduğu alanlardan ziyade birleşerek oluşturdukları bu devasa ortak havuzdur.

<div class="mgw-widget">
<style>
.mgw-widget{--mgw-cyan:#00f0ff;--mgw-amber:#ffb020;--mgw-grey:#8892b0;background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:16px;font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#f3f4f6;max-width:900px;margin:1.5em auto;}
.mgw-widget h4{color:var(--mgw-cyan);font-size:1rem;text-transform:uppercase;letter-spacing:1px;margin:0 0 10px 0;}
.mgw-canvas-wrap{width:100%;height:420px;border-radius:8px;overflow:hidden;background:#0b0f19;}
.mgw-canvas-wrap canvas{display:block;width:100%;height:100%;}
.mgw-legend{margin-top:8px;font-size:0.78rem;color:var(--mgw-grey);}
</style>

<h4>Animasyon 3.3.1: Makro Kütle Evrenakı Gradyanları</h4>
<div class="mgw-canvas-wrap"><canvas id="mgwCanvas"></canvas></div>
<div class="mgw-legend">* Animasyon, tekil atomlardan (mikro ölçek) trilyonlarca atomun oluşturduğu makro kütleye (makro ölçek) doğru sürekli bir uzaklaşma (zoom) hareketi yapar. Yakından bakıldığında her atomun kendi sınır tabakası (mor gradyanı) belirginken, uzaklaşıldıkça bu alanların birleşerek cismin tamamını kaplayan kesintisiz, devasa bir 'Düşük Evrenakı Yoğunluğu (Deplasman)' havuzu oluşturduğu görülür.</div>

<script>
(function(){
  const canvas = document.getElementById('mgwCanvas');
  const ctx = canvas.getContext('2d');
  const wrap = canvas.parentElement;

  const GRADIENT_FACTOR = 1.42;
  const DISK_RADIUS = 26;
  let R = 85;
  let startTime = Date.now();

  let relativeAtoms = [];

  function initGrid(){
    relativeAtoms = [];
    const rows = Math.ceil((DISK_RADIUS * 2) / Math.sqrt(3)) + 4;
    const cols = DISK_RADIUS * 2 + 4;
    
    const startI = -Math.floor(rows / 2);
    const endI = Math.ceil(rows / 2);
    const startJ = -Math.floor(cols / 2);
    const endJ = Math.ceil(cols / 2);
    
    const dy = Math.sqrt(3); 
    
    for(let i = startI; i <= endI; i++){
      const ry = i * dy;
      const offsetX = (i % 2 === 0) ? 0 : 1;
      for(let j = startJ; j <= endJ; j++){
        const rx = j * 2 + offsetX;
        
        const dist = Math.sqrt(rx*rx + ry*ry);
        if(dist <= DISK_RADIUS){
          let edgeAlpha = 1.0;
          const blendWidth = 3.5; 
          if(dist > DISK_RADIUS - blendWidth){
            edgeAlpha = (DISK_RADIUS - dist) / blendWidth;
          }
          relativeAtoms.push({ rx, ry, edgeAlpha });
        }
      }
    }
  }
  initGrid();

  let currentT = 0;

  function draw(elapsed){
      if(typeof canvas !== "undefined" && !canvas.isConnected) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;

    const INTRO_DURATION = 5000;
    const ZOOM_DURATION = 6500;

    let isIntro = elapsed < INTRO_DURATION;
    let zoomElapsed = isIntro ? 0 : elapsed - INTRO_DURATION;
    
    let t = zoomElapsed / ZOOM_DURATION;
    if(t > 1) t = 1; 
    const easedT = t * t * (3 - 2 * t); 
    currentT = easedT; 
    
    R = 85 - 80.8 * easedT; 

    // Intro mantığı
    let centerGradAlpha = 1.0;
    let otherAtomsAlpha = 1.0;
    let gradSizeMultiplier = 1.0;
    let drawOrbit = false;
    let orbitAngle = 0;

    if (isIntro) {
        if (elapsed < 1000) {
            centerGradAlpha = 0;
            otherAtomsAlpha = 0;
            gradSizeMultiplier = 0;
            drawOrbit = false;
        } else if (elapsed < 3000) {
            const phase = (elapsed - 1000) / 2000;
            centerGradAlpha = phase;
            otherAtomsAlpha = 0;
            gradSizeMultiplier = phase;
            drawOrbit = true;
            orbitAngle = phase * Math.PI * 15;
        } else {
            const phase = (elapsed - 3000) / 2000;
            centerGradAlpha = 1.0;
            otherAtomsAlpha = phase;
            gradSizeMultiplier = 1.0;
            drawOrbit = true;
            orbitAngle = (2000 / 2000) * Math.PI * 15 + phase * Math.PI * 25;
        }
    } else {
        otherAtomsAlpha = 1.0;
        centerGradAlpha = 1.0;
        gradSizeMultiplier = 1.0;
        drawOrbit = false;
    }

    for(const a of relativeAtoms){
      const isCenter = (a.rx === 0 && a.ry === 0);
      const currentAlpha = isCenter ? centerGradAlpha : otherAtomsAlpha;
      if (currentAlpha <= 0) continue;

      const x = cx + a.rx * R;
      const y = cy + a.ry * R;
      if(x < -100 || x > canvas.width+100 || y < -100 || y > canvas.height+100) continue;

      const sizeMult = isCenter ? gradSizeMultiplier : 1.0;
      const rOuter = Math.max(0.1, R * GRADIENT_FACTOR * sizeMult);

      const grad = ctx.createRadialGradient(x, y, 0, x, y, rOuter);
      const atomBoost = 1.0 + Math.pow(1.0 - currentT, 2.5) * 2.8; 
      const edgeA = a.edgeAlpha * currentAlpha;

      grad.addColorStop(0, `rgba(210,70,255,${Math.min(1, 0.52 * edgeA * atomBoost)})`);
      grad.addColorStop(0.6, `rgba(160,50,255,${Math.min(1, 0.28 * edgeA * atomBoost)})`);
      grad.addColorStop(1, 'rgba(120,60,255,0)');
      
      ctx.beginPath(); ctx.arc(x, y, rOuter, 0, Math.PI * 2); ctx.fillStyle = grad; ctx.fill();
    }
    
    if (drawOrbit) {
        const orbitR = R * 0.7;
        const ex = cx + orbitR * Math.cos(orbitAngle);
        const ey = cy + orbitR * Math.sin(orbitAngle);
        
        ctx.beginPath();
        ctx.arc(cx, cy, orbitR, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(255, 255, 255, ${0.15 * centerGradAlpha})`;
        ctx.setLineDash([4, 4]);
        ctx.stroke();
        ctx.setLineDash([]);
        
        ctx.beginPath();
        ctx.arc(ex, ey, 4, 0, Math.PI * 2);
        ctx.fillStyle = '#00ffff';
        ctx.shadowColor = '#00ffff';
        ctx.shadowBlur = 8;
        ctx.fill();
        ctx.shadowBlur = 0;
    }

    const nucleiAlpha = Math.max(0, 1 - Math.pow(currentT, 2.5)); 
    if(nucleiAlpha > 0.01){
      for(const a of relativeAtoms){
        const isCenter = (a.rx === 0 && a.ry === 0);
        const currentAlpha = isCenter ? 1.0 : otherAtomsAlpha;
        if (currentAlpha <= 0) continue;

        const x = cx + a.rx * R;
        const y = cy + a.ry * R;
        if(x < -20 || x > canvas.width+20 || y < -20 || y > canvas.height+20) continue;
        
        const finalAlpha = nucleiAlpha * a.edgeAlpha * currentAlpha;
        if(finalAlpha <= 0.01) continue;

        ctx.beginPath(); ctx.arc(x, y, Math.max(1.5, R * 0.14), 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 215, 0, ${finalAlpha})`; 
        ctx.shadowColor = `rgba(255, 215, 0, ${finalAlpha})`; 
        ctx.shadowBlur = 4; ctx.fill(); ctx.shadowBlur = 0;
      }
    }

    if (!isIntro) {
        const macroR = DISK_RADIUS * R * 1.12; 
        if(macroR > 0){
          const macroGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, macroR);
          const alphaCenter = 0.3 + 0.55 * currentT; 
          
          macroGrad.addColorStop(0, `rgba(220, 120, 255, ${alphaCenter})`); 
          macroGrad.addColorStop(0.4, `rgba(160, 50, 255, ${alphaCenter * 0.65})`); 
          macroGrad.addColorStop(0.75, `rgba(80, 20, 200, ${alphaCenter * 0.25})`); 
          macroGrad.addColorStop(0.95, `rgba(50, 0, 150, ${alphaCenter * 0.1})`);
          macroGrad.addColorStop(1, 'rgba(50, 0, 150, 0)');
          
          ctx.globalCompositeOperation = 'screen';
          ctx.beginPath();
          ctx.arc(cx, cy, macroR, 0, Math.PI * 2);
          ctx.fillStyle = macroGrad;
          ctx.fill();
          ctx.globalCompositeOperation = 'source-over';
        }

        if(currentT > 0.1){
          ctx.beginPath();
          ctx.arc(cx, cy, DISK_RADIUS * R, 0, Math.PI * 2);
          ctx.strokeStyle = `rgba(255, 255, 255, ${Math.pow(currentT, 1.5) * 0.85})`; 
          ctx.lineWidth = 1.5;
          ctx.shadowColor = 'rgba(255, 255, 255, 0.8)';
          ctx.shadowBlur = 4;
          ctx.stroke();
          ctx.shadowBlur = 0; 
        }

        if(currentT > 0.1){
          const haloInnerR = DISK_RADIUS * R;
          const haloOuterR = DISK_RADIUS * R * 2.2;
          const haloAlpha = 0.55 * Math.pow(currentT, 1.5); 
          
          const haloGrad = ctx.createRadialGradient(cx, cy, haloInnerR, cx, cy, haloOuterR);
          haloGrad.addColorStop(0, `rgba(0, 240, 255, ${haloAlpha})`); 
          haloGrad.addColorStop(0.4, `rgba(0, 120, 255, ${haloAlpha * 0.4})`);
          haloGrad.addColorStop(1, 'rgba(0, 0, 0, 0)'); 
          
          ctx.globalCompositeOperation = 'screen';
          ctx.beginPath();
          ctx.arc(cx, cy, haloOuterR, 0, Math.PI * 2);
          ctx.arc(cx, cy, haloInnerR, 0, Math.PI * 2, true); 
          ctx.fillStyle = haloGrad;
          ctx.fill();
          ctx.globalCompositeOperation = 'source-over';
        }

        const vRadius = Math.max(canvas.width, canvas.height) / 2;
        const vignette = ctx.createRadialGradient(cx, cy, vRadius * 0.4, cx, cy, vRadius * 1.5);
        vignette.addColorStop(0, 'rgba(0, 0, 0, 0)');
        vignette.addColorStop(1, `rgba(0, 0, 0, ${0.98 * currentT})`); 
        
        ctx.beginPath();
        ctx.rect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = vignette;
        ctx.fill();

        if(zoomElapsed > 8500){
          const waitRatio = (zoomElapsed - 8500) / 5000;
          const textAlpha = Math.min(1, waitRatio * 6); 
          
          ctx.globalAlpha = textAlpha;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          
          const drawPill = (py, width, height) => {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.75)';
            ctx.shadowBlur = 0;
            ctx.beginPath();
            ctx.roundRect(cx - width/2, py - height/2, width, height, 10);
            ctx.fill();
          };
          
          drawPill(cy + 1, 300, 56);
          
          ctx.font = 'bold 16px Segoe UI';
          ctx.fillStyle = '#ffffff';
          ctx.shadowColor = 'rgba(0,0,0,1)';
          ctx.shadowBlur = 10;
          ctx.fillText('KÜTLE İÇİ', cx, cy - 10);
          ctx.font = '14px Segoe UI';
          ctx.fillStyle = '#e2b3ff'; 
          ctx.fillText('EVRENAKI GRADYANI (DEPLASMAN)', cx, cy + 12);
          
          const outerY = cy - (DISK_RADIUS * R * 1.5); 
          drawPill(outerY + 1, 320, 56);
          
          ctx.font = 'bold 16px Segoe UI';
          ctx.fillStyle = '#00f0ff'; 
          ctx.shadowColor = 'rgba(0,0,0,1)';
          ctx.shadowBlur = 10;
          ctx.fillText('KÜTLE DIŞI', cx, outerY - 10);
          ctx.font = '14px Segoe UI';
          ctx.fillStyle = '#b3f0ff';
          ctx.fillText('EVRENAKI GRADYANI', cx, outerY + 12);
          
          ctx.shadowBlur = 0;
          ctx.globalAlpha = 1.0;
        }
    }
  }

  function step(){
      if(typeof canvas !== "undefined" && !canvas.isConnected) return;
    if(canvas.width !== wrap.clientWidth || canvas.height !== wrap.clientHeight){
      canvas.width = wrap.clientWidth;
      canvas.height = wrap.clientHeight;
    }
    
    const elapsed = Date.now() - startTime;
    draw(elapsed);
    
    const INTRO_DURATION = 5000;
    const ZOOM_DURATION = 6500;
    const WAIT_DURATION = 7000;
    
    if (elapsed > INTRO_DURATION + ZOOM_DURATION + WAIT_DURATION) {
      startTime = Date.now();
    }
    
    requestAnimationFrame(step); 
  }

  requestAnimationFrame(step);
})();
</script>
</div>

## 3.3.2 Makro Kütle Geometri Gradyanları

Evrenakı Teorisi'nin merkezinde yatan temel prensiplerden biri, standart fizikte "kütleçekim" denen etkinin bir "çekim" (pull) değil, çevresel kozmik akışkanın (Cosmofluid) makro kütle üzerinde oluşturduğu bir "itim" (push) ve basınç gradyanı — yani kütle-itim — olmasıdır. Bu hidrodinamik modelde, mikro ölçekteki girdapların (vortekslerin) bir araya gelerek oluşturduğu makro kütleler, sadece kütle miktarından ibaret statik nesneler değil; aynı zamanda içinde bulundukları Evrenakı denizinde kendi fiziksel formlarına ve geometrilerine tam uyumlu bir "gölgelenme" ve basınç sönümleme alanı yaratan dinamik engellerdir.

Klasik fizik modellerinde kütleçekimi, çoğunlukla noktasal kütleler (point-mass) etrafında oluşan ve mesafe ile zayıflayan basit küresel simetrik alanlar olarak idealize edilir (küresel kabuk teoremi ve noktasal indirgeme: Newton, 1687). Ancak Evrenakı modeline göre; bir makro kütlenin sahip olduğu fiziksel şekil, bu kütlenin içerisindeki ve çevresindeki basınç gradyanının yayılım topolojisini doğrudan şekillendirir. Kütlenin geometrisi, her yönden gelen Evrenakı itiminin kütle boyunca ilerlerken hangi eksenlerde daha fazla sönümleneceğini ve nerede nasıl bir iç kuvvet dengesi (gradyan) oluşturacağını dikte eder.

Bu bölümde, makro kütlelerin şekillerine bağlı olarak (örneğin tam küre, elipsoit, disk veya düzensiz asteroit yapıları) kütle içerisindeki ve yakın çevresindeki gradyanın şekil ile beraber nasıl bir yayılım gösterdiğini inceleyeceğiz. Geometriye bağlı olarak farklılaşan bu gradyanların; 
- Cisim içindeki basınç dağılımını nasıl değiştirdiği,
- Eksenel ve yanal itim farklarını nasıl doğurduğu,
- Teorimizin öngörüleri doğrultusunda, yıldızlardan galaksilere kadar gözlemlenen anomalilerin (kutuplardaki basıklık veya galaktik disklerin oluşumu gibi) altında yatan asıl mekanizmanın bu gradyan mimarisi olduğu detaylıca ortaya konacaktır.

### 3.3.2.1 Klasik Geometrik Şekillerin 2D Gradyanları

Evrenakı'nın (Cosmofluid) her yönden gelen merkezcil itim etkisi, kütle bloğunun içinden geçerken bir sönümleme (gölgelenme) yaşar. Bu etkiyi en iyi anlayabilmek için öncelikle 3 boyutlu karmaşık yapıları bir kenara bırakıp, klasik 2 boyutlu geometrik şekillerin (daire, kare, üçgen, çubuk) kesitleri üzerinden nasıl bir "basınç gradyanı" haritası oluştuğunu incelemeliyiz. Böylece şeklin köşe, kenar ve merkez noktalarındaki itim farkları çok daha net anlaşılacaktır.

<style>
  #bolum26-sim { background: #121212; color: #fff; font-family: 'Inter', sans-serif; margin: 20px 0; padding: 20px; text-align: center; border-radius: 12px; border: 1px solid #404040; box-shadow: 0 10px 30px rgba(0,0,0,0.8); overflow: hidden; }
  #bolum26-sim .btn-group { margin-bottom: 20px; display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; }
  #bolum26-sim button { background: #1e1e1e; color: #0ea5e9; border: 1px solid #0ea5e9; padding: 10px 20px; cursor: pointer; border-radius: 8px; transition: 0.3s; font-weight: 500; }
  #bolum26-sim button:hover, #bolum26-sim button.active { background: #0ea5e9; color: #fff; box-shadow: 0 0 15px rgba(14, 165, 233, 0.5); }
  #bolum26-sim canvas { background: #050505; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); border: 1px solid #333; max-width: 100%; }
  #bolum26-sim .info { margin-top: 20px; font-size: 15px; color: #cbd5e1; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.5; background: rgba(255, 0, 127, 0.05); border-left: 3px solid #ff007f; padding: 12px 20px; border-radius: 0 8px 8px 0; text-align: left; }
</style>
<div id="bolum26-sim">
  <h3 style="margin-top: 0; margin-bottom: 20px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon 3.3.2.1: Klasik Geometrik Şekillerin 2D Gradyanları</h3>
  <div class="btn-group">
    <button class="active" onclick="window.setShape26('circle', this)">Tam Daire (Küre Kesiti)</button>
    <button onclick="window.setShape26('square', this)">Kare (Kübik Kesit)</button>
    <button onclick="window.setShape26('rod', this)">Çubuk (İnce Uzun)</button>
    <button onclick="window.setShape26('triangle', this)">Üçgen (Asimetrik)</button>
    <button onclick="window.setShape26('binary', this)">İkili Sistem</button>
    <button onclick="window.setShape26('ellipse', this)">Elips (Gezegen Formu)</button>
    <button onclick="window.setShape26('ring', this)">Halka (Yığılma Diskleri)</button>
    <button onclick="window.setShape26('asteroid', this)">Asteroit (Kaotik)</button>
  </div>
  
  <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px; margin-bottom: 15px; font-size: 13px; color: #cbd5e1;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: #00e5ff; box-shadow: 0 0 8px #00e5ff;"></span>
      Dış Evrenakı Gradyanı (Basınç ve Yoğunluk Sönümlemesi)
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: #8b0099; box-shadow: 0 0 8px #8b0099;"></span>
      İç Evrenakı Gradyanı (Kütle İçi Basınç ve Yoğunluk Merkezi)
    </div>
  </div>

  <canvas id="simCanvas26" width="800" height="500"></canvas>
  <div class="info" id="infoText26">
    <strong>Tam Daire:</strong> Daire şekli, her yönden gelen basınçlı Evrenakı akışına karşı kusursuz bir radyal sönümleme (gölgelenme) gradyanı oluşturur. Merkezcil itim yüzeyin her noktasında eşittir, bu yüzden gök cisimleri makro boyutta küreselleşme eğilimindedir.
  </div>

<script>
(function(){
  const canvas = document.getElementById('simCanvas26');
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  
  let currentShape = 'circle';
  let time = 0;

  const infos = {
    circle: "<strong>Tam Daire:</strong> Daire şekli, her yönden gelen basınçlı Evrenakı akışına karşı kusursuz bir radyal sönümleme (gölgelenme) gradyanı oluşturur. Merkezcil itim yüzeyin her noktasında eşittir, bu yüzden gök cisimleri makro boyutta küreselleşme eğilimindedir.",
    square: "<strong>Kare:</strong> Kare şeklinde köşeler, köşegenler boyunca uzandığı için basınca karşı daha kalın bir duvar oluşturur. Bu durum, basınç gradyanının içeriye nüfuzunu engeller ve yıldızvari (haç şeklinde) bir düşük basınç gölgesi oluşturur.",
    rod: "<strong>Çubuk (Dikdörtgen):</strong> Çubuk şeklinde, uzun kenarlar boyunca yanal basınç çok daha yüksektir (daha fazla gölgeleme alanı). Bu durum eksenel (uçlardan) ve yanal (yanlardan) kütle-itim asimetrisine yol açar. Çubuk yapılar uzayda spin atmaya mecbur kalır.",
    triangle: "<strong>Üçgen:</strong> Üçgen kesitte kusursuz bir asimetrik sönümleme oluşur. Sivri uç Evrenakı itimini kolay yararken (aerodinamik), geniş taban kendi arkasında çok büyük bir gölge (düşük basınç alanı) yaratır. Gradyan dengesizliği doğurur.",
    binary: "<strong>İkili Sistem:</strong> İki kütle birbirine yaklaştığında, ortalarında kalan bölgede Evrenakı itimi çift taraflı gölgelenir ve devasa bir düşük basınç alanı (vakum) oluşur. Dış basınç, içerideki eksik basıncı yenerek kütleleri birbirine iter. (Kütle-itimin asıl doğası).",
    ellipse: "<strong>Elips (Kutuplardan Basık Form):</strong> Gezegenler ve yıldızlar ekvatordan şişkin, kutuplardan basıktır. Elips gradyanı, kutup ekseni ile ekvator ekseni arasındaki dönüşten (spin) kaynaklı yanal gölgeleme farklarını ve şekil dengesini gösterir.",
    ring: "<strong>Halka / Simit (Torus Kesiti):</strong> Dışarıdan gelen Evrenakı basıncı dış çeperde klasik bir gölge oluştururken, ortadaki boşluğa sızan basınç hapsolur. Bu durum merkezin 'boş' olmasına rağmen inanılmaz bir yüksek basınç girdabı oluşturmasına neden olur (Kara delik yığılma diskleri).",
    asteroid: "<strong>Düzensiz Asteroit (Çokgen Form):</strong> Pürüzsüz olmayan, asimetrik yüzeylerde Evrenakı basıncı son derece kaotik ve düzensiz mikro-gradyanlar oluşturur. Bu asimetrik gölgelenme, uzaydaki göktaşlarının neden doğrusal değil de sürekli takla atarak (kaotik spin) ilerlediklerini açıklar."
  };

  window.setShape26 = function(shape, btn) {
    currentShape = shape;
    document.querySelectorAll('#bolum26-sim button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('infoText26').innerHTML = infos[shape];
  };

  function step() {
      if(typeof canvas !== "undefined" && !canvas.isConnected) return;
    // Sabit arka plan dolgusu (clearRect yerine, saydamlık hatalarını önlemek için)
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = '#050505';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;

    const pulsate = 0;
    ctx.globalCompositeOperation = 'lighter';
    
    if(currentShape === 'circle') {
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let r = 80 + i*5 + pulsate;
        ctx.beginPath(); 
        ctx.arc(cx, cy, r, 0, Math.PI*2); 
        ctx.fill();
      }

      ctx.globalCompositeOperation = 'source-over';
      const innerGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, 80);
      innerGrad.addColorStop(0, '#b800e6');
      innerGrad.addColorStop(1, '#2d004d');
      ctx.fillStyle = innerGrad;
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cx, cy, 80, 0, Math.PI*2); ctx.fill(); ctx.stroke();
      
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.lineWidth = 1;
      for(let r=20; r<80; r+=15) {
        ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.stroke();
      }
    } else if(currentShape === 'square') {
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let size = 160 + i*6 + pulsate;
        ctx.fillRect(cx - size/2, cy - size/2, size, size);
      }
      ctx.globalCompositeOperation = 'source-over';
      const innerGradSq = ctx.createRadialGradient(cx, cy, 0, cx, cy, 110);
      innerGradSq.addColorStop(0, '#b800e6');
      innerGradSq.addColorStop(1, '#2d004d');
      ctx.fillStyle = innerGradSq;
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.fillRect(cx - 80, cy - 80, 160, 160);
      ctx.strokeRect(cx - 80, cy - 80, 160, 160);
      
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.lineWidth = 1;
      for(let s=30; s<160; s+=30) {
        ctx.strokeRect(cx - s/2, cy - s/2, s, s);
      }
      ctx.beginPath(); ctx.moveTo(cx-80, cy-80); ctx.lineTo(cx+80, cy+80); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx+80, cy-80); ctx.lineTo(cx-80, cy+80); ctx.stroke();
    } else if(currentShape === 'rod') {
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let w = 340 + i*6 + pulsate;
        let h = 80 + i*6 + pulsate;
        ctx.fillRect(cx - w/2, cy - h/2, w, h);
      }
      ctx.globalCompositeOperation = 'source-over';
      ctx.fillStyle = '#2d004d';
      ctx.fillRect(cx - 170, cy - 40, 340, 80);
      for(let i = 0; i <= 30; i++) {
        ctx.fillStyle = `rgba(184, 0, 230, 0.05)`;
        let shrinkW = i * 5.5;
        let shrinkH = i * 1.3;
        ctx.fillRect(cx - 170 + shrinkW, cy - 40 + shrinkH, 340 - 2*shrinkW, 80 - 2*shrinkH);
      }
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.strokeRect(cx - 170, cy - 40, 340, 80);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.lineWidth = 1;
      for(let s=20; s<80; s+=20) {
        ctx.strokeRect(cx - 170 + s*1.5, cy - 40 + s/2, 340 - 3*s, 80 - s);
      }
    } else if(currentShape === 'triangle') {
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let s = 1 + i*0.05 + pulsate*0.005;
        ctx.save();
        ctx.translate(cx, cy + 13);
        ctx.scale(s, s);
        ctx.beginPath();
        ctx.moveTo(0, -103);
        ctx.lineTo(90, 52);
        ctx.lineTo(-90, 52);
        ctx.closePath();
        ctx.fill();
        ctx.restore();
      }
      ctx.globalCompositeOperation = 'source-over';
      const innerGradTri = ctx.createRadialGradient(cx, cy + 20, 0, cx, cy + 20, 90);
      innerGradTri.addColorStop(0, '#b800e6');
      innerGradTri.addColorStop(1, '#2d004d');
      ctx.fillStyle = innerGradTri;
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx, cy - 90);
      ctx.lineTo(cx + 90, cy + 65);
      ctx.lineTo(cx - 90, cy + 65);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.lineWidth = 1;
      for(let s=0.2; s<1.0; s+=0.2) {
        ctx.save();
        ctx.translate(cx, cy + 13);
        ctx.scale(s, s);
        ctx.beginPath();
        ctx.moveTo(0, -103);
        ctx.lineTo(90, 52);
        ctx.lineTo(-90, 52);
        ctx.closePath();
        ctx.stroke();
        ctx.restore();
      }
    } else if(currentShape === 'binary') {
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let r = 70 + i*5 + pulsate;
        ctx.beginPath(); 
        ctx.arc(cx - 90, cy, r, 0, Math.PI*2);
        ctx.arc(cx + 90, cy, r, 0, Math.PI*2);
        ctx.fill();
      }
      ctx.globalCompositeOperation = 'source-over';
      const leftGrad = ctx.createRadialGradient(cx - 90, cy, 0, cx - 90, cy, 70);
      leftGrad.addColorStop(0, '#b800e6'); leftGrad.addColorStop(1, '#2d004d');
      const rightGrad = ctx.createRadialGradient(cx + 90, cy, 0, cx + 90, cy, 70);
      rightGrad.addColorStop(0, '#b800e6'); rightGrad.addColorStop(1, '#2d004d');
      
      ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2;
      ctx.fillStyle = leftGrad;
      ctx.beginPath(); ctx.arc(cx - 90, cy, 70, 0, Math.PI*2); ctx.fill(); ctx.stroke();
      ctx.fillStyle = rightGrad;
      ctx.beginPath(); ctx.arc(cx + 90, cy, 70, 0, Math.PI*2); ctx.fill(); ctx.stroke();
      
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)'; ctx.lineWidth = 1;
      for(let r=20; r<70; r+=15) {
        ctx.beginPath(); ctx.arc(cx - 90, cy, r, 0, Math.PI*2); ctx.stroke();
        ctx.beginPath(); ctx.arc(cx + 90, cy, r, 0, Math.PI*2); ctx.stroke();
      }
    } else if(currentShape === 'ellipse') {
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let rx = 120 + i*6 + pulsate;
        let ry = 70 + i*4 + pulsate;
        ctx.beginPath(); 
        ctx.ellipse(cx, cy, rx, ry, 0, 0, Math.PI*2);
        ctx.fill();
      }
      ctx.globalCompositeOperation = 'source-over';
      ctx.save();
      ctx.translate(cx, cy);
      ctx.scale(1, 70/120);
      const innerGrad = ctx.createRadialGradient(0, 0, 0, 0, 0, 120);
      innerGrad.addColorStop(0, '#b800e6'); innerGrad.addColorStop(1, '#2d004d');
      ctx.fillStyle = innerGrad;
      ctx.beginPath(); ctx.arc(0, 0, 120, 0, Math.PI*2); ctx.fill();
      ctx.restore();
      
      ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.ellipse(cx, cy, 120, 70, 0, 0, Math.PI*2); ctx.stroke();
      
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)'; ctx.lineWidth = 1;
      for(let r=0.2; r<1.0; r+=0.2) {
        ctx.beginPath(); ctx.ellipse(cx, cy, 120*r, 70*r, 0, 0, Math.PI*2); ctx.stroke();
      }
    } else if(currentShape === 'ring') {
      // Dış Gradyan (İç boşluğa sızması engellendi)
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let r = 100 + i*5 + pulsate;
        ctx.beginPath(); 
        ctx.arc(cx, cy, r, 0, Math.PI*2, false);
        ctx.arc(cx, cy, 40, 0, Math.PI*2, true); // Orta deliği boş bırak
        ctx.fill();
      }
      
      // İç Boşluktaki Ters Gradyan (Koyu/açık geçişi sertleştirilmiş)
      for(let i = 0; i <= 40; i++) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.035)`;
        let innerR = 40 * Math.pow(i/40, 0.4); // Üstel (power) eğrisi ile keskin geçiş
        ctx.beginPath(); 
        ctx.arc(cx, cy, 40, 0, Math.PI*2, false);
        ctx.arc(cx, cy, innerR, 0, Math.PI*2, true);
        ctx.fill();
      }
      
      ctx.globalCompositeOperation = 'source-over';
      
      // Halka Kütlesi
      const ringGrad = ctx.createRadialGradient(cx, cy, 40, cx, cy, 100);
      ringGrad.addColorStop(0, '#2d004d');
      ringGrad.addColorStop(0.5, '#b800e6');
      ringGrad.addColorStop(1, '#2d004d');
      
      ctx.fillStyle = ringGrad;
      ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(cx, cy, 100, 0, Math.PI*2, false);
      ctx.arc(cx, cy, 40, 0, Math.PI*2, true);
      ctx.fill(); ctx.stroke();
      
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)'; ctx.lineWidth = 1;
      for(let r=55; r<100; r+=15) {
        ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.stroke();
      }
    } else if(currentShape === 'asteroid') {
      // Dış Gradyan (Kaotik)
      for(let i = 40; i >= 0; i--) {
        ctx.fillStyle = `rgba(0, 229, 255, 0.015)`;
        let scale = 1 + i*0.04 + pulsate*0.005;
        ctx.save();
        ctx.translate(cx, cy);
        ctx.scale(scale, scale);
        ctx.beginPath();
        ctx.moveTo(90, 0); ctx.lineTo(60, 40); ctx.lineTo(80, 80); ctx.lineTo(20, 70);
        ctx.lineTo(-40, 90); ctx.lineTo(-80, 40); ctx.lineTo(-60, -20); ctx.lineTo(-90, -60);
        ctx.lineTo(-30, -80); ctx.lineTo(30, -90); ctx.lineTo(60, -50);
        ctx.closePath();
        ctx.fill();
        ctx.restore();
      }
      
      ctx.globalCompositeOperation = 'source-over';
      
      // Kütle arka planı
      ctx.fillStyle = '#2d004d'; ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2;
      ctx.save();
      ctx.translate(cx, cy);
      ctx.beginPath();
      ctx.moveTo(90, 0); ctx.lineTo(60, 40); ctx.lineTo(80, 80); ctx.lineTo(20, 70);
      ctx.lineTo(-40, 90); ctx.lineTo(-80, 40); ctx.lineTo(-60, -20); ctx.lineTo(-90, -60);
      ctx.lineTo(-30, -80); ctx.lineTo(30, -90); ctx.lineTo(60, -50);
      ctx.closePath();
      ctx.fill(); ctx.stroke();
      
      // Şekle uygun katmanlı iç gradyan (Merkeze doğru parlaklaşan asteroit formu)
      ctx.globalCompositeOperation = 'lighter';
      for(let i = 0; i <= 30; i++) {
        let s = 1.0 - (i / 30);
        ctx.fillStyle = `rgba(139, 0, 153, 0.05)`;
        ctx.save();
        ctx.scale(s, s);
        ctx.beginPath();
        ctx.moveTo(90, 0); ctx.lineTo(60, 40); ctx.lineTo(80, 80); ctx.lineTo(20, 70);
        ctx.lineTo(-40, 90); ctx.lineTo(-80, 40); ctx.lineTo(-60, -20); ctx.lineTo(-90, -60);
        ctx.lineTo(-30, -80); ctx.lineTo(30, -90); ctx.lineTo(60, -50);
        ctx.closePath();
        ctx.fill();
        ctx.restore();
      }
      
      ctx.globalCompositeOperation = 'source-over';
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)'; ctx.lineWidth = 1;
      for(let s=0.2; s<1.0; s+=0.25) {
        ctx.save();
        ctx.scale(s, s);
        ctx.beginPath();
        ctx.moveTo(90, 0); ctx.lineTo(60, 40); ctx.lineTo(80, 80); ctx.lineTo(20, 70);
        ctx.lineTo(-40, 90); ctx.lineTo(-80, 40); ctx.lineTo(-60, -20); ctx.lineTo(-90, -60);
        ctx.lineTo(-30, -80); ctx.lineTo(30, -90); ctx.lineTo(60, -50);
        ctx.closePath();
        ctx.stroke();
        ctx.restore();
      }
      ctx.restore();
    }

    time++;
    requestAnimationFrame(step);
  }

  requestAnimationFrame(step);
})();
</script>
</div>

### 3.3.2.2 Klasik Geometrik Şekillerin 3D Gradyanları

2 boyutlu kesitlerde gördüğümüz gradyanlar, uzayın 3 boyutlu derinliğinde aslında kütleyi her yönden saran devasa **basınç bulutları (vakum zırhları)** oluşturur. Evrenakı akışkanı kütleye uzayın 3 ekseninden (x, y, z) ve her bir açıdan aynı anda çarptığı için, oluşan gölgelenme ve düşük basınç bölgeleri volumetrik (hacimsel) bir yapı kazanır.

Aşağıdaki interaktif simülasyonda, temel geometrik şekillerin uzayda nasıl bir hidrodinamik gölge (gradyan) yarattığını görebilirsiniz. Fare ile tıklayıp sürükleyerek (veya dokunmatik ekranda kaydırarak) yapıları 3 boyutlu olarak her açıdan inceleyebilirsiniz.

> ⚠️ **Uyarı:** Aşağıdaki 3 boyutlu simülasyon, tarayıcınızın grafik işlemci birimini (WebGL donanım hızlandırmasını) kullanmaktadır. Eğer simülasyon yüklenmezse veya siyah ekranda kalırsa, lütfen tarayıcı ayarlarınızda "Donanım hızlandırma" özelliğinin açık olduğundan emin olun veya güncel bir web tarayıcısı kullanın.

<div id="bolum26-3d-widget" style="background: #0b0f19; border: 1px solid rgba(0,240,255,0.2); border-radius: 12px; padding: 20px; text-align: center; margin: 20px 0; font-family: 'Segoe UI', Roboto, sans-serif;">
  <h3 style="margin-top: 0; margin-bottom: 15px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon 3.3.2.2: Klasik Geometrik Şekillerin 3D Gradyanları</h3>
  
  <div style="margin-bottom: 15px; display: flex; justify-content: center; flex-wrap: wrap; gap: 8px;" id="b26-3d-btns">
    <button class="active" onclick="window.setShape3dInline('tetra', this)" style="background: #0ea5e9; color: #fff; border: 1px solid #0ea5e9; padding: 8px 16px; cursor: pointer; border-radius: 8px; font-weight: 500; font-size: 13px; transition: 0.3s;">Piramit</button>
    <button onclick="window.setShape3dInline('cube', this)" style="background: #1e1e1e; color: #0ea5e9; border: 1px solid #0ea5e9; padding: 8px 16px; cursor: pointer; border-radius: 8px; font-weight: 500; font-size: 13px; transition: 0.3s;">Küp</button>
    <button onclick="window.setShape3dInline('cylinder', this)" style="background: #1e1e1e; color: #0ea5e9; border: 1px solid #0ea5e9; padding: 8px 16px; cursor: pointer; border-radius: 8px; font-weight: 500; font-size: 13px; transition: 0.3s;">Silindir</button>
    <button onclick="window.setShape3dInline('sphere', this)" style="background: #1e1e1e; color: #0ea5e9; border: 1px solid #0ea5e9; padding: 8px 16px; cursor: pointer; border-radius: 8px; font-weight: 500; font-size: 13px; transition: 0.3s;">Küre</button>
  </div>

  <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px; margin-bottom: 12px; font-size: 13px; color: #cbd5e1;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: #00e5ff; box-shadow: 0 0 8px #00e5ff;"></span>
      Dış Evrenakı Gradyanı (Basınç ve Yoğunluk Sönümlemesi)
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: #8b0099; box-shadow: 0 0 8px #8b0099;"></span>
      İç Evrenakı Gradyanı (Kütle İçi Basınç ve Yoğunluk Merkezi)
    </div>
  </div>

  <div style="width: 100%; height: 420px; background: #050505; border-radius: 8px; overflow: hidden; position: relative;" id="cvsWrap3d">
    <canvas id="cvs3d26" style="width: 100%; height: 100%; display: block; cursor: grab;"></canvas>
  </div>

  <div id="infoText3dInline" style="margin-top: 15px; font-size: 14px; color: #cbd5e1; line-height: 1.5; background: rgba(0, 229, 255, 0.1); border-left: 3px solid #00e5ff; padding: 12px 20px; border-radius: 8px; text-align: left;">
    <strong>Piramit (Üçgenin 3D'si - Tetrahedron):</strong> Uzayda asimetrik basınç gölgelenmesinin en belirgin 3D örneğidir. Dört sivri uç (köşe) aerodinamik olarak akışı yararken, geniş düz yüzeyler devasa vakum cepleri oluşturur. Kendi kendine yönelim (oryantasyon) ve itki kazanır.
  </div>

  <script>
  (function(){
    const infosInline = {
      sphere: "<strong>Küre (Dairenin 3D'si):</strong> 3D uzayda kusursuz bir volumetrik sönümleme oluşturur. Basınç her noktadan eşit gölgelendiği için, etrafında katman katman mükemmel bir 'vakum küresi' örülür.",
      cube: "<strong>Küp (Karenin 3D'si):</strong> 8 köşesi ve 12 ayrıtı sayesinde 3D uzayda karmaşık bir yıldız (haç) şeklinde basınç gölgesi yaratır. Köşegenler boyunca uzanan duvarlar, Evrenakı itimini en çok süzen kısımlardır.",
      cylinder: "<strong>Silindir (Çubuğun 3D'si):</strong> Uzun eksen (gövde) boyunca devasa bir volumetrik gölge yaratırken, dairesel kapakları yönünde daha zayıf bir gradyan oluşturur. Uzayda spin atan asteroitlerin dönüş mekanizmasını tetikler.",
      tetra: "<strong>Piramit (Üçgenin 3D'si - Tetrahedron):</strong> Uzayda asimetrik basınç gölgelenmesinin en belirgin 3D örneğidir. Dört sivri uç (köşe) aerodinamik olarak akışı yararken, geniş düz yüzeyler devasa vakum cepleri oluşturur. Kendi kendine yönelim (oryantasyon) ve itki kazanır."
    };

    let activeShape = 'tetra';
    
    window.setShape3dInline = function(type, btn) {
      activeShape = type;
      const btns = document.querySelectorAll('#b26-3d-btns button');
      btns.forEach(b => {
        b.style.background = '#1e1e1e';
        b.style.color = '#0ea5e9';
        b.classList.remove('active');
      });
      if(btn) {
        btn.style.background = '#0ea5e9';
        btn.style.color = '#fff';
        btn.classList.add('active');
      }
      const infoEl = document.getElementById('infoText3dInline');
      if (infoEl) infoEl.innerHTML = infosInline[type];
    };

    const canvas = document.getElementById('cvs3d26');
    if(!canvas) return;
    const ctx = canvas.getContext('2d');
    const wrap = document.getElementById('cvsWrap3d');

    let isDragging = false;
    let previousMousePosition = { x: 0, y: 0 };
    let angleX = 0.3;
    let angleY = 0.4;

    canvas.addEventListener('mousedown', e => {
      isDragging = true;
      previousMousePosition = { x: e.clientX, y: e.clientY };
      canvas.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', e => {
      if (!isDragging) return;
      let deltaX = e.clientX - previousMousePosition.x;
      let deltaY = e.clientY - previousMousePosition.y;
      angleY += deltaX * 0.01;
      angleX += deltaY * 0.01;
      previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
      if (canvas) canvas.style.cursor = 'grab';
    });

    // Touch support for mobile
    canvas.addEventListener('touchstart', e => {
      if (e.touches.length === 1) {
        isDragging = true;
        previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      }
    });

    canvas.addEventListener('touchmove', e => {
      if (!isDragging || e.touches.length !== 1) return;
      let deltaX = e.touches[0].clientX - previousMousePosition.x;
      let deltaY = e.touches[0].clientY - previousMousePosition.y;
      angleY += deltaX * 0.01;
      angleX += deltaY * 0.01;
      previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    });

    canvas.addEventListener('touchend', () => { isDragging = false; });

    const solidShapes = {
      tetra: {
        nodes: [[0,-2,0], [1.9,1.1,-1.1], [-1.9,1.1,-1.1], [0,1.1,1.9]],
        faces: [[0,2,1], [0,1,3], [0,3,2], [1,2,3]]
      },
      cube: {
        nodes: [[-1.3,-1.3,-1.3],[1.3,-1.3,-1.3],[1.3,1.3,-1.3],[-1.3,1.3,-1.3],
                [-1.3,-1.3,1.3],[1.3,-1.3,1.3],[1.3,1.3,1.3],[-1.3,1.3,1.3]],
        faces: [[0,3,2,1], [4,5,6,7], [0,1,5,4], [2,3,7,6], [0,4,7,3], [1,2,6,5]]
      },
      cylinder: {
        nodes: (function(){
          let n = [];
          for(let i=0;i<16;i++){
            let a = (i/16)*Math.PI*2;
            n.push([Math.cos(a)*1.4, -2.4, Math.sin(a)*1.4]);
            n.push([Math.cos(a)*1.4, 2.4, Math.sin(a)*1.4]);
          }
          return n;
        })(),
        faces: (function(){
          let f = [];
          for(let i=0;i<16;i++){
            let b1 = i*2, t1 = i*2+1;
            let b2 = ((i+1)%16)*2, t2 = ((i+1)%16)*2+1;
            f.push([b1, b2, t2, t1]);
          }
          let topCap = [], botCap = [];
          for(let i=0;i<16;i++){ topCap.push(i*2+1); botCap.unshift(i*2); }
          f.push(topCap); f.push(botCap);
          return f;
        })()
      },
      sphere: {
        nodes: (function(){
          let n = [];
          const lats = 10, lons = 16;
          for(let i=0; i<=lats; i++){
            let theta = (i/lats)*Math.PI;
            let sinT = Math.sin(theta), cosT = Math.cos(theta);
            for(let j=0; j<lons; j++){
              let phi = (j/lons)*Math.PI*2;
              n.push([sinT*Math.cos(phi)*2.1, cosT*2.1, sinT*Math.sin(phi)*2.1]);
            }
          }
          return n;
        })(),
        faces: (function(){
          let f = [];
          const lats = 10, lons = 16;
          for(let i=0; i<lats; i++){
            for(let j=0; j<lons; j++){
              let first = i*lons + j;
              let second = first + lons;
              let nextJ = (j+1)%lons;
              f.push([first, first - j + nextJ, second - j + nextJ, second]);
            }
          }
          return f;
        })()
      }
    };

    function rotate3D(pt, ax, ay) {
      let x = pt[0], y = pt[1], z = pt[2];
      let x1 = x * Math.cos(ay) + z * Math.sin(ay);
      let z1 = -x * Math.sin(ay) + z * Math.cos(ay);
      let y2 = y * Math.cos(ax) - z1 * Math.sin(ax);
      let z2 = y * Math.sin(ax) + z1 * Math.cos(ax);
      return [x1, y2, z2];
    }

    function renderFrame() {
      if(!canvas.isConnected) return;

      if(canvas.width !== wrap.clientWidth || canvas.height !== wrap.clientHeight){
        canvas.width = wrap.clientWidth;
        canvas.height = wrap.clientHeight;
      }

      const w = canvas.width;
      const h = canvas.height;
      const cx = w / 2;
      const cy = h / 2;
      const scale = Math.min(w, h) * 0.14;

      if(!isDragging){
        angleY += 0.008;
      }

      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#050505';
      ctx.fillRect(0, 0, w, h);

      // Volumetric Radial Gradient Aura
      const outerR = scale * 4.0;
      const gradOuter = ctx.createRadialGradient(cx, cy, scale * 0.5, cx, cy, outerR);
      gradOuter.addColorStop(0, 'rgba(210, 70, 255, 0.45)');
      gradOuter.addColorStop(0.35, 'rgba(139, 0, 153, 0.28)');
      gradOuter.addColorStop(0.7, 'rgba(0, 229, 255, 0.12)');
      gradOuter.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = gradOuter;
      ctx.beginPath(); ctx.arc(cx, cy, outerR, 0, Math.PI * 2); ctx.fill();

      // Transform Vertices
      const data = solidShapes[activeShape] || solidShapes.tetra;
      const rotatedNodes = data.nodes.map(pt => rotate3D(pt, angleX, angleY));
      const projNodes = rotatedNodes.map(r => [cx + r[0] * scale, cy + r[1] * scale, r[2]]);

      // Face Depth Sorting
      let renderFaces = [];
      for (let face of data.faces) {
        let avgZ = 0;
        for (let idx of face) avgZ += rotatedNodes[idx][2];
        avgZ /= face.length;

        let v0 = rotatedNodes[face[0]], v1 = rotatedNodes[face[1]], v2 = rotatedNodes[face[2]];
        let ax = v1[0] - v0[0], ay = v1[1] - v0[1], az = v1[2] - v0[2];
        let bx = v2[0] - v0[0], by = v2[1] - v0[1], bz = v2[2] - v0[2];
        let nx = ay*bz - az*by, ny = az*bx - ax*bz, nz = ax*by - ay*bx;
        let len = Math.sqrt(nx*nx + ny*ny + nz*nz) || 1;
        nz /= len; ny /= len; nx /= len;

        renderFaces.push({ face, avgZ, nz, ny, nx });
      }

      renderFaces.sort((a, b) => a.avgZ - b.avgZ);

      // Render Solid Polygon Faces
      for (let item of renderFaces) {
        let dot = item.nx * 0.4 - item.ny * 0.6 + item.nz * 0.7;
        let intensity = Math.max(0.25, Math.min(1.0, dot * 0.7 + 0.35));

        ctx.beginPath();
        let first = true;
        for (let idx of item.face) {
          let p = projNodes[idx];
          if (first) { ctx.moveTo(p[0], p[1]); first = false; }
          else { ctx.lineTo(p[0], p[1]); }
        }
        ctx.closePath();

        let r = Math.floor(45 + intensity * 60);
        let g = Math.floor(0 + intensity * 40);
        let b = Math.floor(77 + intensity * 120);

        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, 0.88)`;
        ctx.fill();

        ctx.strokeStyle = 'rgba(0, 229, 255, 0.7)';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }

      requestAnimationFrame(renderFrame);
    }

    requestAnimationFrame(renderFrame);
  })();
  </script>
</div>



## 3.3.3 Makro Kütle Işık Davranışları

Şu ana kadar ışığın (zerrelerin) tekil atomlar ve atomik dizilimler (mikro ölçek) etrafındaki temel hidrodinamik davranışlarını (yansıma, mikro saydamlık, patinaj ve soğurma) inceledik. Ancak fiziksel gerçeklikte maddeler izole atomlardan değil, trilyonlarca atomun bir araya gelmesiyle oluşan bütünsel kütlelerden (makro nesnelerden) meydana gelir. Bu davranışların mikro mekanizmaları Kısım 2'de kurulmuştu (kırılma ve geçirme: 2.6, girişim: 2.7–2.8, kutuplanma: 2.9); burada aynı mekanizmaların makro kütle geometrisiyle nasıl ölçeklendiği özetlenecek, en büyük ölçekli uygulaması olan kütleçekimsel merceklenme ise Bölüm 4.3'te ele alınacaktır.

### 3.3.3.1 Makro Kütlelerin Birleşik Gradyan Alanı ve Işığın Yönlenmesi

Atomlar birleşip makro bir kütle (örneğin bir cam levha, bir mercek, bir prizma veya bir gezegen) oluşturduğunda, içerdikleri sayısız çekirdeğin taşıdığı o mikro Evrenakı gradyanları birleşerek nesnenin tamamını saran devasa ve **bütünsel bir Makro Evrenakı Gradyanı** oluşturur. Bu noktadan itibaren ışığın davranışını belirleyen temel unsur yalnızca içerideki atomik kafes değil, aynı zamanda kütlenin uzayda kapladığı geometrik şeklin hem içinde hem de dışında kümelenen bu devasa, birleşik hidrodinamik alandır.

Bir merceğin ışığı tek bir noktada odaklaması veya bir prizmanın ışığı keskin bir açıyla bükmesi, standart fiziğin varsaydığı gibi maddenin "kırılma indisinin" soyut matematiksel bir sonucu değildir. Bu, tamamen malzemenin fiziksel şeklinin, uzaydaki Evrenakı akışkanında yarattığı o bükülmüş, aerodinamik/hidrodinamik dış gradyanın mekanik sonucudur. Zerreler, bu bütünsel makro gradyanlara dışarıdan girdiklerinde, seyrelmiş (deplasmana uğramış) akışkanın basınç farkına maruz kalarak tıpkı bir rüzgar tünelindeki aerodinamik hava akımı gibi yön değiştirir, bükülür ve şekillenirler.

Böylece bu bölümün zinciri tamamlanmış olur: tekil atomun mikro gradyanı (3.3.1), kütle geometrisinin 2D/3D gradyan desenleri (3.3.2) ve bu desenlerin ışığı yönlendiren bütünsel makro alanı (3.3.3). Bir sonraki bölümde (3.4), aynı makro gradyanın yalnızca ışığı değil, kütleli cisimleri de nasıl yönettiği — yani kütle-itim mekanizmasının kendisi — ele alınacaktır.


