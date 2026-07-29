# 2.9 Evrenakı Gradyanları ve Polarizasyon

Işığın uzayda (Evrenakı denizinde) nasıl ilerlediğini tam anlamıyla kavrayabilmek için, standart fiziğin "foton" dediği ışık birimlerinin "dalga" veya "parçacık" gibi sabit kimliklere sahip olmadığını, bulundukları hidrodinamik şartlara göre şekil değiştiren **esnek akışkan zerreler** olduğunu hatırlamalıyız. Evrenakı teorisine göre zerreler sabit boyutlu katı bilyeler değil, kendi iç dinamikleri (spinleri) ile Evrenakı'nın dış basıncı arasında sürekli dinamik bir denge kuran esnek akışkan yapılardır.

Bu esnekliğin kutuplaşma bağlamındaki temel sonucu Bölüm 2.4.3'te kurulmuştu ve tek cümleyle özetlenebilir: düşük basınçlı gradyana giren Zerre patinaja geçer, doğrusal enerjisi dönüşe aktarılır ve artan merkezkaç ile azalan dış baskı altında **küreden diske (elipsoide)** yassılaşır — standart fiziğin "polarizasyon" dediği durum, bu mekanik form değişiminin ta kendisidir. Bu bölümün özgün konusu ise bir sonraki adımdır: polarize olmuş diskin, gradyan alanlarında **basınç torkuyla** nasıl yönlendirildiği.

## 2.9.1 Evrenakı Gradyanı ve Zerre Polarizasyonu (Küreden Diske Geçiş)

Işığın kutuplanma mekanizmasını görselleştiren temel animasyon ve hidrodinamik açıklamalar, **Bölüm 2.4.3: Evrenakı Gradyanı ve Küreden Diske Geçiş** başlığı altında detaylıca işlenmiştir; gradyan artışının spin'i nasıl hızlandırdığını ve Zerre'yi disk formuna nasıl yassılaştırdığını etkileşimli incelemek için oradaki **Animasyon 2.4.3**'e başvurunuz.

## 2.9.2 Evrenakı Gradyanı ve Zerre Bükülmeleri

Evrenakı Teorisi'nde ışığın kırılması veya yön değiştirmesi (bükülmesi), soyut bir dalga cephesinin yavaşlamasıyla değil, son derece somut bir hidrodinamik basınç mekanizmasıyla gerçekleşir. 

Halihazırda polarize olmuş (disk formuna kavuşmuş) bir zerre, uzayda ilerlerken Evrenakı gradyanlarına (farklı basınç bölgelerine) açılı bir şekilde girdiğinde, zerre diski üzerinde fiziksel bir dönme momenti (tork) oluşur. 

Zerre diskini çeviren asıl unsur, Evrenakı gradyanlarının yoğun (yüksek basınçlı) bölgeden az yoğun (düşük basınçlı) bölgeye doğru itici bir kuvvet doğurmasından gelir. Disk, bu basınç farkı alanına açılı girdiğinde, diskin farklı noktalarına etki eden eşitsiz hidro-kuvvetler net bir tork yaratır. Bu tork, diski Evrenakı gradyanlarının akış çizgilerine uymaya (hizalanmaya) zorlar. Dönüş hareketi, zerre diski gradyanın müsaade ettiği nihai kararlı denge konumuna (akışa tam paralel hale) ulaşana kadar devam eder. Polarizör filtrelerin ve kırılma olaylarının arkasında yatan gerçek fiziksel mekanizma, basınç farkından doğan bu tork etkisidir.

Aşağıdaki canlandırmada, makro kütleleri tamamen ortadan kaldırdık ve olayı saf hidrodinamik basınç (gradyan) bölgeleri üzerinden modeledik. Sağda ve solda düşük basınçlı (eflatun) Evrenakı gradyanları, ortada ise normal basınçlı (siyah) bir kanal bulunmaktadır. Geliş açısını değiştirerek diskin gradyanlara nasıl sürtünüp hizaya girdiğini gözlemleyebilirsiniz.

<div class="bend-widget">
<style>
.bend-widget{--bend-cyan:#00f0ff;--bend-amber:#ffb020;background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:16px;font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#f3f4f6;max-width:900px;margin:1.5em auto;}
.bend-widget h4{color:var(--bend-cyan);font-size:1rem;text-transform:uppercase;letter-spacing:1px;margin:0 0 10px 0;}
.bend-controls{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:10px;align-items:flex-end;}
.bend-control{display:flex;flex-direction:column;gap:4px;font-size:0.8rem;color:#9ca3af;flex:1;min-width:150px;}
.bend-control input[type=range]{accent-color:var(--bend-cyan);width:100%;}
.bend-angle-btns{display:flex;gap:8px;flex-wrap:wrap;margin-top:5px;}
.bend-btn{background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.2);color:#f3f4f6;padding:6px 12px;border-radius:6px;cursor:pointer;font-weight:600;flex:1;min-width:45px;}
.bend-btn:hover{background:rgba(0,240,255,0.2);}
.bend-btn.active{background:var(--bend-cyan);color:#000;box-shadow:0 0 10px var(--bend-cyan);}
.bend-canvas-wrap{width:100%;height:400px;border-radius:8px;overflow:hidden;background:#000000;position:relative;box-shadow:inset 0 0 50px rgba(120,40,200,0.2);}
.bend-canvas-wrap canvas{display:block;width:100%;height:100%;}
.bend-legend{margin-top:10px;font-size:0.78rem;color:#8892b0;}
</style>

<h4>Animasyon 2.9.2: Zerre Bükülmeleri</h4>
<div class="bend-controls">
  <div class="bend-control">
      <div style="display:flex; gap:16px;">
          <label style="color:var(--bend-cyan); display:flex; align-items:center; gap:8px; font-weight:600; cursor:pointer; margin-bottom:4px;">
              <input type="checkbox" id="bendNegDirCheck" style="width:16px; height:16px;">
              Negatif Yön
          </label>
          <label style="color:var(--bend-amber); display:flex; align-items:center; gap:8px; font-weight:600; cursor:pointer; margin-bottom:4px;">
              <input type="checkbox" id="bendPolarizerCheck" style="width:16px; height:16px;">
              <span id="bendPolarizerLabel">Makro Kütle Modu</span>
          </label>
      </div>
      <div class="bend-angle-btns">
          <button class="bend-btn" data-angle="15">15°</button>
          <button class="bend-btn" data-angle="30">30°</button>
          <button class="bend-btn" data-angle="45">45°</button>
          <button class="bend-btn" data-angle="60">60°</button>
          <button class="bend-btn" data-angle="75">75°</button>
          <button class="bend-btn" data-angle="90">90°</button>
      </div>
  </div>
</div>
<div class="bend-canvas-wrap"><canvas id="bendCanvas"></canvas></div>
<div class="bend-legend">
  * <b>3 Boyutlu Akış (Bize Doğru):</b> Zerre kameraya doğru uçarken, sağda ve solda eflatun renkli düşük basınç gradyanları (deplasman havuzları) bulunur.<br>
  * <b>Basınç Torku ile Bükülme:</b> Zerre yola açılı (çapraz) girdiğinde, Evrenakı'nın yoğun (yüksek basınçlı) bölgesinden az yoğun (düşük basınçlı) bölgesine doğru doğan itici kuvvetler disk üzerinde net bir tork yaratır. Bu tork, zerre diskini gradyanın müsaade ettiği kararlı akış konumuna ulaşana kadar (hizalanana dek) zorla çevirir.
</div>

<script>
(function(){
  const canvas = document.getElementById('bendCanvas');
  const ctx = canvas.getContext('2d');
  const wrap = canvas.parentElement;

  let currentYaw = 0;
  let isHolding = false;
  let zerreXOffset = 0;
  let flashAlpha = 0;
  let isAbsorbed = false;
  let absorbDir = 1;
  
  const btns = document.querySelectorAll('.bend-btn');
  const negCheck = document.getElementById('bendNegDirCheck');
  const polCheck = document.getElementById('bendPolarizerCheck');
  const polLabel = document.getElementById('bendPolarizerLabel');
  polCheck.addEventListener('change', () => {
      polLabel.textContent = polCheck.checked ? 'Polarizer Modu' : 'Makro Kütle Modu';
  });
  
  function releaseAngle() {
      isHolding = false;
      btns.forEach(b => b.classList.remove('active'));
  }

  btns.forEach(btn => {
      const baseAng = parseInt(btn.getAttribute('data-angle'), 10);
      
      const press = (e) => {
          e.preventDefault();
          isHolding = true;
          const sign = negCheck.checked ? -1 : 1;
          const ang = baseAng * sign;
          currentYaw = ang * Math.PI / 180;
          
          // 90 dereceye her tıklandığında efekti (yutulmayı) baştan oynatmak için sıfırlama
          if (Math.abs(ang) === 90) {
              zerreXOffset = 0;
              isAbsorbed = false;
              flashAlpha = 0;
              absorbDir = Math.random() > 0.5 ? 1 : -1; // Yönü rastgele seç
          }

          btns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
      };
      
      btn.addEventListener('mousedown', press);
      btn.addEventListener('touchstart', press, {passive: false});
  });

  window.addEventListener('mouseup', releaseAngle);
  window.addEventListener('touchend', releaseAngle);

  function resize(){ if(typeof canvas !== "undefined" && !canvas.isConnected) { window.removeEventListener("resize", resize); return; } 
      canvas.width = wrap.clientWidth;
      canvas.height = wrap.clientHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  // 3D Particles
  const particles = [];
  const NUM_PARTICLES = 250;
  for(let i=0; i<NUM_PARTICLES; i++){
      particles.push({
          x: (Math.random() - 0.5) * 2000,
          y: (Math.random() - 0.5) * 1500,
          z: Math.random() * 1000
      });
  }

  const FOV = 300;
  // Diskin sabit boyutları: Geniş kısmı Y ekseninde olacak (0 derece = dikey duruş)
  const DISK_RADIUS_X = 20;  // Dar kısım
  const DISK_RADIUS_Y = 140; // Geniş kısım (Y ekseninde)

  function step(){
      if(typeof canvas !== "undefined" && !canvas.isConnected) return;
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const gradMargin = cx - 40; 
      
      const isPolarizer = polCheck.checked;

      // Arka plan
      ctx.fillStyle = '#06080e';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      if (isPolarizer) {
          // Polarizer Modu: Tüm ekranı kaplayan 3'lü gradyan (Katı Izgara)
          const polGrad = ctx.createLinearGradient(0, 0, canvas.width, 0);
          
          // 1. Kolon
          polGrad.addColorStop(0.00, 'rgba(0, 0, 0, 1)');
          polGrad.addColorStop(0.16, 'rgba(120, 40, 200, 0.5)');
          polGrad.addColorStop(0.33, 'rgba(0, 0, 0, 1)');
          
          // 2. Kolon (Merkez)
          polGrad.addColorStop(0.50, 'rgba(120, 40, 200, 0.5)');
          polGrad.addColorStop(0.66, 'rgba(0, 0, 0, 1)');
          
          // 3. Kolon
          polGrad.addColorStop(0.83, 'rgba(120, 40, 200, 0.5)');
          polGrad.addColorStop(1.00, 'rgba(0, 0, 0, 1)');
          
          ctx.fillStyle = polGrad;
          ctx.fillRect(0, 0, canvas.width, canvas.height);
      } else {
          // Normal Mod: Akışkan Evrenakı Kanalı
          
          ctx.fillStyle = 'rgba(180, 100, 255, 0.55)';
          ctx.fillRect(gradMargin, 0, canvas.width - 2 * gradMargin, canvas.height);

          const gradLeft = ctx.createLinearGradient(0, 0, gradMargin, 0);
          gradLeft.addColorStop(0, 'rgba(0, 0, 0, 1)');
          gradLeft.addColorStop(1, 'rgba(180, 100, 255, 0.55)');
          ctx.fillStyle = gradLeft;
          ctx.fillRect(0, 0, gradMargin, canvas.height);

          const gradRight = ctx.createLinearGradient(canvas.width, 0, canvas.width - gradMargin, 0);
          gradRight.addColorStop(0, 'rgba(0, 0, 0, 1)');
          gradRight.addColorStop(1, 'rgba(180, 100, 255, 0.55)');
          ctx.fillStyle = gradRight;
          ctx.fillRect(canvas.width - gradMargin, 0, gradMargin, canvas.height);
      }

      if (!isHolding) {
          // Doğal hidrodinamik Tork formülü: sin(2 * açı)
          const torque = Math.sin(currentYaw * 2) * 0.006; 
          currentYaw -= torque;
      }

      let forwardSpeedMult = 1.0;
      let zerreEnerji = 1.0;

      if (isPolarizer) {
          // Polarizer Modu: 90 derecede (yatayken) tamamen yutulur/durur
          forwardSpeedMult = Math.max(0, Math.abs(Math.cos(currentYaw)));
          zerreEnerji = Math.max(0.05, forwardSpeedMult); // Hız sıfırlanınca görünmezliğe yaklaşır
          
          // 90 dereceye tam yatıldıysa, karanlık alana kayma ve yutulma (Flaş)
          if (Math.abs(Math.abs(currentYaw) - Math.PI/2) < 0.05) {
              if (!isAbsorbed) {
                  zerreXOffset += 3 * absorbDir;
                  if (Math.abs(zerreXOffset) >= 136) {
                      flashAlpha = 1.0;
                      isAbsorbed = true;
                  }
              }
          } else {
              zerreXOffset *= 0.85;
              isAbsorbed = false;
          }
      } else {
          zerreXOffset *= 0.85;
          isAbsorbed = false;
      }
      
      if (flashAlpha > 0) flashAlpha -= 0.05;

      // 3D Yıldız/Akışkan Efekti
      ctx.strokeStyle = 'rgba(0, 255, 255, 0.9)'; // Tüm yıldızlar (parçacıklar) parlak camgöbeği
      particles.forEach(p => {
          let px2d = cx + (p.x / p.z) * FOV;
          
          let pSpeed = 15; // Temel uçuş hızını artırdık
          if (!isPolarizer) {
              // Standart mod: 90 derecede bile ileri gidiş var (sadece sürtünmeden dolayı biraz yavaşlar)
              pSpeed = 15 - Math.abs(Math.sin(currentYaw)) * 6; 
          } else {
              // Polarizer modu: disk durursa (90 derece) akış tamamen durur
              pSpeed = 15 * forwardSpeedMult; 
          }

          p.z -= pSpeed * 1.5;
          
          if(p.z <= 1) {
              p.z = 1000;
              p.x = (Math.random() - 0.5) * 2000;
              p.y = (Math.random() - 0.5) * 1500;
          }

          const scale = FOV / p.z;
          const x2d = cx + p.x * scale;
          const y2d = cy + p.y * scale;

          // Polarizer modunda hız 0'a düşerse division by zero olmasın diye 0.1 ekliyoruz
          const oldScale = FOV / (p.z + pSpeed * 4 + (isPolarizer ? 0.1 : 0));
          const oldX = cx + p.x * oldScale;
          const oldY = cy + p.y * oldScale;

          ctx.beginPath();
          ctx.moveTo(oldX, oldY);
          ctx.lineTo(x2d, y2d);
          ctx.lineWidth = scale * 1.5;
          ctx.stroke();
      });

      // Flaş Efekti Çizimi (Yutulma anı)
      if (flashAlpha > 0) {
          ctx.save();
          ctx.translate(cx + zerreXOffset, cy);
          ctx.beginPath();
          ctx.arc(0, 0, 30 + (1 - flashAlpha) * 60, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(255, 255, 255, ${flashAlpha})`;
          ctx.shadowBlur = 40;
          ctx.shadowColor = '#ffffff';
          ctx.fill();
          ctx.restore();
      }

      if (!isAbsorbed) {
          // Merkezi Zerre (Disk) Çizimi
          ctx.save();
          ctx.translate(cx + zerreXOffset, cy);
          ctx.rotate(currentYaw);
          
          // Enerjisine (Polarizer moduna) göre parlaklık/soğurulma
          ctx.globalAlpha = zerreEnerji;
          ctx.shadowBlur = (20 + Math.abs(currentYaw)*10) * zerreEnerji; 
      ctx.shadowColor = 'rgba(255, 204, 0, 0.9)';
      
      ctx.beginPath();
      ctx.ellipse(0, 0, DISK_RADIUS_X, DISK_RADIUS_Y, 0, 0, Math.PI*2);
      ctx.fillStyle = '#ffcc00';
      ctx.fill();
      
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#ffffff';
      ctx.stroke();
      
      ctx.beginPath();
      ctx.ellipse(0, 0, DISK_RADIUS_X * 0.4, DISK_RADIUS_Y * 0.6, 0, 0, Math.PI*2);
      ctx.strokeStyle = 'rgba(255,255,255,0.4)';
      ctx.stroke();

      ctx.beginPath();
      ctx.ellipse(0, 0, 8, 40, 0, 0, Math.PI*2);
      ctx.fillStyle = '#fff';
      ctx.fill();
      
      ctx.restore();
      } // isAbsorbed if bloğu sonu

      // Tork Göstergesi (HUD)
      if (!isPolarizer) {
          const torkDegeri = Math.sin(currentYaw * 2); 
          const barWidth = 160;
          const barHeight = 8;
          const startX = 20;
          const barX = startX + barWidth / 2; // Merkezin X koordinatı
          const barY = canvas.height - 30;

          ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
          ctx.font = '14px "Segoe UI", Arial, sans-serif';
          ctx.textAlign = 'left';
          ctx.fillText("Bükücü Tork Etkisi:", startX, barY - 12);

          // Arka plan (boş bar)
          ctx.fillStyle = 'rgba(255, 255, 255, 0.15)';
          ctx.fillRect(startX, barY, barWidth, barHeight);

          // Merkez sıfır çizgisi
          ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
          ctx.fillRect(barX - 1, barY - 4, 2, barHeight + 8);

          // Tork dolgusu
          ctx.fillStyle = 'rgba(0, 240, 255, 0.9)'; // Camgöbeği
          let fillWidth = torkDegeri * (barWidth / 2);
          if (fillWidth > 0) {
              ctx.fillRect(barX, barY, fillWidth, barHeight);
          } else {
              ctx.fillRect(barX + fillWidth, barY, -fillWidth, barHeight);
          }
          
          // Metin olarak da şiddetini yazalım (0.00 - 1.00 arası)
          ctx.fillStyle = 'rgba(0, 240, 255, 0.9)';
          ctx.fillText(Math.abs(torkDegeri).toFixed(2), startX + barWidth + 12, barY + 8);
      }

      requestAnimationFrame(step);
  }
  
  requestAnimationFrame(step);
})();
</script>
</div>

*(Not: Yukarıdaki canlandırma tek Zerre'nin geçen doğrusal hız bileşenini gösterir; bu bileşen $\cos\theta$ ile ölçeklenir. Ölçülen makro şiddet ise katar istatistiğiyle bunun $\cos^2\theta$ karşılığıdır — bkz. 2.9.2.1.)*

### 2.9.2.1 İki Ayrı Mekanizma: Yutan Polarizör ve Burkan Gradyan

Zerre diskiyle etkileşen alanlar iki kategoriye ayrılır ve bu ayrım, teorinin en önemli gözlem araçlarından birini doğurur:

**1. Soğurucu (yutan) polarizör — Malus yasasının mekanik karşılığı:** Polarizör filtre, yalnızca kendi geçirme eksenine paralel disk yönelimini geçiren bir rampa dizisidir. Geçirme eksenine **dik** yönelmiş gelen Zerreler rampaya çarpar ve **yutulur**. Eksenle $\theta$ açısı yapan bir diskin geçidi ise iki çarpanla belirlenir: geçen Zerre'nin doğrusal hız bileşeni $\cos\theta$ ile ölçeklenir; rampadan sağ (soğurulmadan) geçen **katar kesri** de $\cos\theta$ ile orantılıdır. Şiddet, birim alana düşen katar sayısı olduğundan (Bölüm 2.2.3) makro geçirgenlik iki çarpanın çarpımıdır:

$$I(\theta) = I_0\,\underbrace{\cos\theta}_{\text{hız bileşeni}}\cdot\underbrace{\cos\theta}_{\text{geçen katar kesri}} = I_0\cos^2\theta$$

Bu, Malus yasasının (Malus, 1809) katar dilindeki mekanik karşılığıdır. Bölüm 2.10.1'de dolanıklık ölçümlerinde karşılaşılan $\cos^2(a-b)$ korelasyon yapısının kökeni de aynı geçit mekaniğidir; nicel türetimi Bölüm 7.4'te açık kalemdir.

**2. Burkan gradyan alanı (saydam cisim) — yutma yok, burkulma var:** Polarizör olmayan saydam bir cismin içindeki Evrenakı gradyanları Zerre'yi yutmaz; diskin yönelimini **burkar** (döndürür). Kritik ayrım şudur: bu burkan alanlara **dik gelen Zerreler hiç burkulmaya uğramadan geçer**; açılı gelen Zerreler ise gradyan geometrisi boyunca birikimli olarak burkulur.

Bu ayrımın sonucu, teoriye bir gözlem penceresi açar: **saydam cisimlerin içindeki Evrenakı gradyanları, çıkan ışığın burkulma deseninden okunabilir.** Cisme farklı yönelimlerle gönderilen polarize katarların çıkışta ne kadar burkulduğu haritalanırsa, kütle-içi gradyanın geometrisi görünür hâle gelir (kütle-içi gradyanların interferometrik haritalaması için bkz. Bölüm 5.3; bu ayrıma dayanan burkulma deneyleri mevcut olup kitabın deney fazında yazılacaktır). Standart fiziğin üç ayrı başlık altında topladığı olgular — soğurucu polaroid (Malus), optik aktivite (şeker çözeltisinin polarizasyon düzlemini döndürmesi) ve gerilme çift kırılımı (fotoelastisite) — bu tek ayrımın (**yutan rampa ↔ burkan gradyan**) farklı görünümleridir.

## 2.9.3 Bölüm Kapanışı ve Geçiş

Bu bölümde kutuplaşmanın iki ayağı tamamlandı: Zerre'nin gradyan basıncı altında küreden diske geçişi (mekanizmanın tam kuruluşu için bkz. 2.4.3) ve polarize diskin, gradyanlara açılı girdiğinde basınç torkuyla akış çizgilerine hizalanması (2.9.2). Böylece Kısım 2'nin mekanik araç seti — patinaj, rampa geçidi, wake, paket ve tork — eksiksiz kuruldu. Bir sonraki bölümde (2.10) bu araçların, standart fiziğin en gizemli saydığı kuantum anomalilerini — dolanıklık ve belirsizlik — nasıl karşıladığını göreceğiz.
