# Ek A — Hız Kavramlarının Ayrıştırılması: Patinaj Sınırı, Denge Hızı ve Kavitasyon Eşiği

> **Taşıma notu:** Bu ek, Kısım 1 Bölüm 1.3.4'ten bu kısma taşınmıştır; Kısım 1'de kompakt özeti bulunur. Şablonlu türetim karşılıkları (Ek M kataloğu): Ek A.1 → **M-1** · Ek A.2 → **M-3** · Ek A.3 → **M-4**, **M-5** · hız tablosu ve sıralama zinciri → **M-6**.

### Ek A: Hız Kavramlarının Ayrıştırılması: Patinaj Sınırı, Denge Hızı ve Kavitasyon Eşiği

Bölüm 2.2.1'de detaylandırılacağı üzere $c$ (SI'da tanım gereği 299.792.458 m/s; BIPM, 2019), Evrenakı'nın yırtılma (kavitasyon) sınırı DEĞİLDİR; o yalnızca ışığın bulunduğu yoğunluktaki yola tutunabildiği lokal 'patinaj' sınırıdır. Bu ek, teoride adı geçen tüm hız kavramlarını tek bir çatı altında ayrıştırır ve aralarındaki ilişkiyi nicel olarak kurar.

#### Ek A.1 — İki Sınır, İki Kategori

Kavrama Yasası ($v=\sqrt{P/\rho}$; Ek B'de $\rho_0=P_0/c^2$ olarak kullanılan ve Bölüm 3.4.6.3'te Fizeau katsayısını türeten bağıntı), $c$'nin fiziksel kimliğini netleştirir: **$c$, ortamın basınç-iletim (sonik) hızıdır** — Evrenakı'nın "Mach 1"i (bkz. Bölüm 2.4.1) *(katalog: **Ek M-1**)*. Bu kimlik, sık karıştırılan iki sınırın kategorik farkını kendiliğinden verir:

| | $c$ — kavrama (patinaj) sınırı | $v_{kav}$ — yırtılma (kavitasyon) eşiği |
|---|---|---|
| **Neyin sınırı?** | Kavrama yoluyla *ilerlemenin*: Zerre'nin ortama tutunarak yol alabilmesinin | Ortamın *bütünlüğünün*: akışkanın sürekli (yırtıksız) kalabilmesinin |
| **Aşılırsa ne olur?** | Yasak değildir: patinaj/şok oluşur, enerji kaybedilir, hız $c$'ye oturur | Yasak değildir: akışkan yırtılır, vakum cebi açılır — **madde doğar** |
| **Gündelik karşılığı** | Havada ses hızı: süpersonik uçuş vardır, yalnızca şok üretir | Sıvının çekme dayanımı: pervane ucundaki kavitasyon köpüğü |

Buradan teorinin en yalın özeti çıkar: **ışık tam-sonik bir olgudur** (ortama kavrayarak tam $c$'de ilerler); **madde ise kalıcı süpersonik bir olgudur** (yüzeyi $c$'nin üstünde dönen, kendini sürekli yeniden kuran şok zarfı). $c$'nin üstündeki hızlar yasak değildir; yalnızca kavrama ile *sürdürülemez* — ya şok üreterek $c$'ye geri oturur, ya da ($v_{kav}$ da aşılmışsa) ortamı yırtarak maddeyi var eder.

#### Ek A.2 — Denge Hızının Türetimi: Her Vakum-Cepli Girdap, Duvarını $\sqrt{2}\,c$'de Döndürür

*(Bu türetim katalogda **M-3** olarak numaralanmıştır.)*

Teoride madde, içinde vakum cebi (yırtık) taşıyan ve dengede dönen bir girdap zarfıdır (bkz. Animasyon 1.3.2, Aşama 2–3). Cebin dışındaki akışkanda dönme akışı $v_\theta(r)=\Gamma/2\pi r$ ve Bernoulli ilkesi geçerlidir:

$$P(r)=P_0-\tfrac{1}{2}\rho_0\, v_\theta^2(r)$$

Cep duvarında ($r=r_{cep}$; vakum cebi yarıçapı — eski yazım: $a$) basınç, cebin iç basıncına (vakum, $P\approx0$) inmek zorundadır:

$$P_0-\tfrac{1}{2}\rho_0\, v_{duvar}^2=0 \;\;\Longrightarrow\;\; v_{duvar}=\sqrt{\frac{2P_0}{\rho_0}}=\boxed{\sqrt{2}\,c\approx 4{,}24\times10^8\ \text{m/s}}$$

Bu sonucun üç kritik özelliği vardır:

1. **Evrensellik.** $v_{duvar}=\sqrt{2}\,c$ sonucu cebin yarıçapına bağlı değildir; sirkülasyon $\Gamma$ yalnızca cebin *boyutunu* belirler ($r_{cep}=\Gamma/2\pi\sqrt{2}c$), duvar hızını değil. Üstelik bu bir denge çekim noktasıdır: zarf daha hızlı dönerse cep genişler, genişleyen yarıçapta çevresel hız düşer ve duvar $\sqrt{2}\,c$'ye geri oturur. **Her kararlı vakum-cepli girdap — boyutu ne olursa olsun — duvarını tam $\sqrt{2}\,c$'de döndürür.** Tüm nükleonların (ve onlarla aynı sıkışmış girdap fazını taşıyan Zerre'nin) yüzey hızının evrenselliği buradan çıkar.
2. **Sayısal uyum.** Postülat 5'in bağımsız yoldan (Compton frekansı × proton yarıçapı: $2\pi\nu_c R_p$; proton yarıçapı için $R_p$ — eski yazım: $R$) verdiği kompozit ekvator hızı $\approx5\times10^8$ m/s'dir; türetilen $\sqrt{2}\,c=4{,}24\times10^8$ m/s ile fark ~%18'dir. Ters okuma da tutarlıdır: $\nu=\sqrt{2}c/2\pi R_p$ bağıntısı, $R_p=0{,}84$ fm için $\nu\approx8\times10^{22}$ Hz verir — postüladaki $\sim10^{23}$ Hz ile aynı mertebe. Bu uyum **kesin eşitlik değil, mertebe + $O(1)$ uyumudur:** türetim, sıkıştırılamaz Bernoulli, iki boyutlu ideal girdap ve tam-sıfır cep basıncı varsayımlarını kullanır; sıkıştırılabilirlik (zarf bölgesinde yoğunluk artışı), dört boyutlu çift dönüşün üç boyuta izdüşümü ve zarfın sonlu kalınlığı $O(1)$ düzeltmeler getirir (açık hesap: Bölüm 7.4).
3. **Zorunluluk.** Protonun ekvator hızının $c$'yi aşması bir istisna ya da savunulması gereken bir pürüz değil, **yapısal bir zorunluluktur.** Duvarı $c$'nin altında dönen bir zarf, cebindeki vakuma karşı gereken basınç açığını ($\tfrac12\rho_0 v^2<P_0$) üretemez ve cep çöker. Kısacası: **yüzeyi $c$-altı hızda dönen madde var olamaz.** Postülat 5'in "ışık hızını aşan ekvator hızı" ifadesi, böylece Kavrama Yasası'nın doğrudan bir sonucu hâline gelir.

#### Ek A.3 — Kavitasyon Eşiği ve Kohezyon Dayanımı ($\Sigma$): Yaratma ile Sürdürme Ayrımı

*(Katalog: **M-4** kavitasyon eşiği, **M-5** kohezyon kanalı hızı.)*

Sağlam (yırtıksız) bir akışkanı yırtmak, basıncı sıfırın da altına — akışkanın **kohezyon (çekme) dayanımı** olan $-\Sigma$'nın altına — düşürmeyi gerektirir. Aynı Bernoulli hesabıyla yırtma eşiği:

$$v_{kav}=\sqrt{\frac{2(P_0+\Sigma)}{\rho_0}}=\sqrt{2}\,c\,\sqrt{1+\frac{\Sigma}{P_0}}$$

Evrenakı'nın kavitasyon eşiğinin $c$'den çok daha yüksek olması, $\Sigma\gg P_0$ demektir. Bu keyfî bir kabul değildir; gerçek akışkanlarda doğrudan emsali vardır: suyun teorik çekme dayanımı ($\sim10^2$ MPa), üzerindeki atmosfer basıncının ($\sim0{,}1$ MPa) yaklaşık bin katıdır (ölçüm ve teorik sınırlar: Briggs, 1950; Caupin & Herbert, 2006). Nükleasyon çekirdeği içermeyen, viskozitesi sıfıra yakın bir süper-akışkanda bu oranın çok daha yüksek olması beklenir. ($\Sigma$, teorinin adlandırılmış bir parametresidir; Bell hız-sınırı deneyleri $v_m$ özdeşleştirmesi üzerinden ilk gözlemsel alt sınırı verir — $\Sigma/P_0>10^8$, Bölüm 2.10.1 — tam sabitlenmesi Bölüm 7.4'te açık iş olarak kayıtlıdır.)

Kohezyon yalnızca yırtılmaya direnç değil, aynı zamanda ikinci bir **sinyal kanalıdır.** Basınç (sıkışma) salınımları ortamda sonik hızla ($c=\sqrt{P_0/\rho_0}$) yayılırken, ortamın *yapısal* yeniden düzenlenmesi — gradyan ve topografya kurulumu — kohezyon kanalının elastik hızıyla taşınır:

$$v_m=\sqrt{\frac{\Sigma}{\rho_0}}=c\,\sqrt{\frac{\Sigma}{P_0}}$$

Bu hızın fiziksel rolü ve gözlemsel ölçüm programı Bölüm 2.10.1'de işlenir.

<div class="pol-widget-134" id="animasyon-134-ikikanal">
<style>
.pol-widget-134 { --pol-blue:#00f0ff; --pol-magenta:#ff00e5; background:#0b0f19; border:1px solid rgba(0,240,255,0.2); border-radius:10px; padding:16px; font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif; color:#f3f4f6; max-width:900px; margin:1.5em auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
.pol-widget-134 h4 { color:var(--pol-blue); font-size:1rem; text-transform:uppercase; letter-spacing:1px; margin:0 0 10px 0; }
.pol-controls-134 { display:flex; align-items:center; justify-content:space-between; gap:12px; margin-bottom:10px; flex-wrap:wrap; }
.btn-134 { background:rgba(0,240,255,0.12); color:var(--pol-blue); border:1px solid rgba(0,240,255,0.4); border-radius:4px; padding:6px 16px; cursor:pointer; font-size:0.9rem; }
.btn-134:hover { background:rgba(0,240,255,0.25); }
.note-134 { font-size:0.8rem; color:#8892b0; }
.pol-canvas-wrap-134 { width:100%; height:380px; border-radius:8px; overflow:hidden; background:#02050a; position:relative; }
.pol-canvas-wrap-134 canvas { display:block; width:100%; height:100%; }
.desc-134 { background: rgba(255,0,229,0.1); padding: 12px; border-radius: 4px; border: 1px solid rgba(255,0,229,0.3); margin-top: 10px; font-size: 0.95rem; line-height: 1.5; color: #f3f4f6; }
</style>

<h4>Animasyon 1.3.4: İki Kanal — Basınç ($c$) ve Kohezyon ($v_m$) <a name="animasyon-134-ikikanal"></a></h4>
<div class="pol-controls-134">
  <button class="btn-134" id="btn-fire-134">⟳ Sinyali Gönder</button>
  <div class="note-134">Temsilî oran: kohezyon kanalı burada yalnızca <b>50×</b> hızlı çizilmiştir; gerçekte oran <b>&ge; 10.000×</b>tir (Salart 2008 alt sınırı).</div>
</div>
<div class="pol-canvas-wrap-134"><canvas id="canvas134"></canvas></div>
<div class="desc-134">Solda bir kütle (analizör) belirdiğinde ortama <b>iki ayrı haber</b> yayılır. <b>Üst şerit — basınç (sıkışma) kanalı:</b> yoğunluk dalgası sonik hızla ($c$) ilerler; ışık ve —standart fiziğin "kütleçekim dalgası" dediği— basınç salınımları bu kanaldadır. <b>Alt şerit — kohezyon (yapı) kanalı:</b> ortamın basınç topografyası, yapıyı bir arada tutan kohezyon ($\Sigma$) üzerinden $v_m=c\sqrt{\Sigma/P_0}$ hızıyla neredeyse anında yeniden kurulur; kütle-itim alanının kurulumu ve dolanıklık geçidi (Bölüm 2.10.1) bu kanaldadır. İki kanalın karıştırılması yasaktır: GW170817'nin bu basınç salınımlarının hızını tam $c$ ölçmesi üst şeridin, Bell korelasyonlarının "anındalığı" alt şeridin olayıdır.</div>

<script>
(function(){
  const canvas = document.getElementById('canvas134');
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  const wrap = canvas.parentElement;
  function resize(){ if(!canvas.isConnected) { window.removeEventListener('resize', resize); return; }
      canvas.width = wrap.clientWidth; canvas.height = wrap.clientHeight; }
  window.addEventListener('resize', resize); resize();

  let t = -1; // sinyal yok
  const DUR = 7.0;          // basınç dalgasının ekranı geçme süresi (sn)
  const RATIO = 50;         // temsilî v_m/c oranı
  document.getElementById('btn-fire-134').onclick = () => { t = 0; };

  function lane(y0, h, label, color){
      ctx.strokeStyle = 'rgba(42,53,90,0.8)'; ctx.strokeRect(8, y0, canvas.width-16, h);
      ctx.fillStyle = color; ctx.font = 'bold 12px Segoe UI';
      ctx.fillText(label, 18, y0 + 18);
  }

  function draw(){
      if(!canvas.isConnected) return;
      const W = canvas.width, H = canvas.height;
      ctx.fillStyle = '#02050a'; ctx.fillRect(0,0,W,H);
      const x0 = 60, x1 = W - 30;
      const laneH = (H - 60) / 2;
      const yP = 20, yK = 40 + laneH;      // üst ve alt şerit
      lane(yP, laneH, 'BASINÇ KANALI — hız: c  (ışık; std. fizikte "kütleçekim dalgaları")', '#00f0ff');
      lane(yK, laneH, 'KOHEZYON KANALI — hız: v_m ≥ 10⁴·c  (topografya, kütle-itim kurulumu)', '#ff00e5');

      // kaynak kütle
      for(const yy of [yP, yK]){
          ctx.beginPath(); ctx.arc(x0-18, yy+laneH/2, 10, 0, 6.283);
          ctx.fillStyle = '#ffcc00'; ctx.fill();
      }
      ctx.fillStyle = '#8892b0'; ctx.font = '11px Segoe UI';
      ctx.fillText('kütle / analizör', x0-45, yK + laneH + 16);

      // ortam noktaları
      const nx = 60, ny = 6;
      const fP = (t < 0) ? -1 : Math.min(1, t/DUR);              // basınç cephesi (0..1)
      const fK = (t < 0) ? -1 : Math.min(1, (t*RATIO)/DUR);      // kohezyon cephesi
      for(let i=0;i<nx;i++){
        const fx = i/(nx-1), px = x0 + fx*(x1-x0);
        for(let j=0;j<ny;j++){
          const fy = (j+1)/(ny+1);
          // üst: sıkışma darbesi — gauss paketi cepheyle taşınır
          let dx = 0, glow = 0;
          if(fP >= 0){
              const d = (fx - fP) / 0.05;
              dx = -8 * Math.exp(-d*d) * Math.sign(d || 1);
              glow = Math.exp(-d*d);
          }
          ctx.beginPath(); ctx.arc(px + dx, yP + fy*laneH, 2 + 1.5*glow, 0, 6.283);
          ctx.fillStyle = glow > 0.05 ? 'rgba(0,240,255,'+(0.35+0.65*glow)+')' : 'rgba(136,146,176,0.35)';
          ctx.fill();
          // alt: yapısal yeniden dizilim — cephe geçince noktalar yeni (eğimli) konuma oturur
          let shift = 0, hot = 0;
          if(fK >= 0 && fx <= fK){ shift = (0.5 - fy) * 14 * (1 - fx*0.5); hot = Math.max(0, 1 - Math.abs(fx - fK)/0.04); }
          ctx.beginPath(); ctx.arc(px, yK + fy*laneH + shift, 2 + 1.5*hot, 0, 6.283);
          ctx.fillStyle = (fK >= 0 && fx <= fK) ? 'rgba(255,0,229,'+(0.45+0.55*hot)+')' : 'rgba(136,146,176,0.35)';
          ctx.fill();
        }
      }
      // cephe çizgileri ve varış rozetleri
      function front(f, y, color, doneLabel){
          if(f < 0) return;
          const fx = x0 + Math.min(f,1)*(x1-x0);
          ctx.strokeStyle = color; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(fx, y+4); ctx.lineTo(fx, y+laneH-4); ctx.stroke(); ctx.lineWidth = 1;
          if(f >= 1){ ctx.fillStyle = color; ctx.font = 'bold 12px Segoe UI'; ctx.fillText(doneLabel, x1-150, y+laneH-10); }
      }
      front(fP, yP, '#00f0ff', 'ulaştı  (t = L/c)');
      front(fK, yK, '#ff00e5', 'ulaştı  (t ≈ 0)');

      if(t >= 0 && t < DUR + 0.5) t += 0.016;
      requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();
</script>
</div>

Böylece teorinin tüm hız kavramları tek bir sıralama üzerinde yerini bulur *(sıralama teoremi: **Ek M-6**)*:

$$c \;<\; \underbrace{\sqrt{2}\,c}_{v_{denge}\;\approx\;v_{ekvator}} \;<\; \underbrace{c\sqrt{\Sigma/P_0}}_{v_m} \;<\; \underbrace{\sqrt{2}\,c\sqrt{1+\Sigma/P_0}}_{v_{kav}} \;\le\; v_{saf}$$

| Hız | Fiziksel kimliği | Formülü | Değeri |
|---|---|---|---|
| $c$ | Zerre'nin kavrama (patinaj) sınırı = ortamın sonik hızı | $\sqrt{P_0/\rho_0}$ (yerel: $\sqrt{P/\rho}$) | $2{,}998\times10^8$ m/s |
| $v_{denge}$ | Vakum-cepli girdap zarfının denge yüzey hızı | $\sqrt{2}\,c$ | $4{,}24\times10^8$ m/s |
| $v_{ekvator}$ | Protonun kompozit ekvator hızı (gözlemsel girdi) | $2\pi\nu_c R$ | $\approx5\times10^8$ m/s |
| $v_m$ | Kohezyon kanalının elastik sinyal hızı — topografya/gradyan kurulumu (Bölüm 2.10.1) | $\sqrt{\Sigma/\rho_0}=c\sqrt{\Sigma/P_0}$ | $>10^4\,c$ (Bell alt sınırı) |
| $v_{kav}$ | Sağlam akışkanı yırtma (kavitasyon) eşiği | $\sqrt{2}\,c\sqrt{1+\Sigma/P_0}\approx\sqrt2\,v_m$ | $\gg c$ ($\Sigma\gg P_0$) |
| $v_{saf}$ | Temel alt-bileşenlerin saf dönüş hızları | $>v_{kav}$ | $\gg c$ |

#### Ek A.4 — Makro hızlar: madde düşer, ortam dolaşır

Yukarıdaki merdiven **mikro/relativistik** merdivendir: hepsi $c$ mertebesindedir ve maddenin *iç*
yapısını yönetir. Teorinin bir de **makro** hız çifti vardır ($\ll c$); bunlar merdivene girmez ama
sözlüğe girer, çünkü karıştırılmaları kitabın kaydettiği en yaygın hatadır *(katalog: **M-9**;
denge yasası: **DY-2**)*:

| Hız | Kime ait? | Formülü | Yorum |
|---|---|---|---|
| $v_{y\ddot{o}r}$ | **maddeye** (yıldız, gezegen, tanecik) | $\sqrt{R\lvert a_{radyal}\rvert}=\sqrt{\mathcal{G}M/R}$ | **Gözlenen** yörünge/dönüş hızı. Madde katı bir deplasman cebi olduğu için akıp dengelenemez; bütün hâlde **düşer** |
| $v_\theta$ | **ortama** (Evrenakı girdabı) | $\sqrt{\rho_n/\rho_0}\;v_{y\ddot{o}r}=2\,v_{y\ddot{o}r}$ | Ortam aynı gradyanda düşmez, **dolaşır**: siklostrofik denge $dP/dR=\rho_0v_\theta^2/R$ (M-22 / DY-1). Ortamın tepkisi $\rho_0$ ile, maddenin tepkisi $\rho_n$ ile ölçülür |

$$\boxed{\;\frac{v_\theta}{v_{y\ddot{o}r}}=\sqrt{\frac{\rho_n}{\rho_0}}=\sqrt{4}=2\qquad\text{(R-5: }\rho_0=\tfrac14\rho_n\text{, }k=0)\;}$$

> [!IMPORTANT]
> **İki tuzak.** **(1)** $v_\theta$ **yörünge hızı değildir** — yörüngeyi ortamın sürüklemesi
> kurmaz, maddenin serbest düşmesi kurar (M-2). Sürüklenme yükü $\eta_E$ üzerinden taşınır ve
> yörünge zaman ölçeğinde etkisizdir ($\tau_E/\tau_{madde}\approx1{,}8\times10^{16}$).
> **(2)** Ek D'nin tanımı bağlayıcıdır: $v_\theta$ *"girdabın teğetsel hızı"*, yani **ortamın**
> hızıdır. Gözlenen bir eğriyi $v_\theta$ ile adlandırmak R-1'i ihlal eder; doğru sembol
> $v_{y\ddot{o}r}$'dür.
>
> Bu $2\times$ fark teorinin **parametresiz bir öngörüsüdür** (karnede S-7): ortam ile maddenin
> arasında kalıcı bir kayma tabakası bulunmalıdır, ve büyüklüğü tam olarak $v_{y\ddot{o}r}$'dür.

<div class="pol-widget-135" id="animasyon-135-merdiven">
<style>
.pol-widget-135 { --pol-blue:#00f0ff; --pol-magenta:#ff00e5; background:#0b0f19; border:1px solid rgba(0,240,255,0.2); border-radius:10px; padding:16px; font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif; color:#f3f4f6; max-width:900px; margin:1.5em auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
.pol-widget-135 h4 { color:var(--pol-blue); font-size:1rem; text-transform:uppercase; letter-spacing:1px; margin:0 0 10px 0; }
.pol-canvas-wrap-135 { width:100%; height:340px; border-radius:8px; overflow:hidden; background:#02050a; position:relative; }
.pol-canvas-wrap-135 canvas { display:block; width:100%; height:100%; }
.desc-135 { background: rgba(255,0,229,0.1); padding: 12px; border-radius: 4px; border: 1px solid rgba(255,0,229,0.3); margin-top: 10px; font-size: 0.95rem; line-height: 1.5; color: #f3f4f6; min-height: 64px; }
.ladder-135 { margin-top: 14px; position: relative; height: 56px; background: rgba(0,0,0,0.5); border: 1px solid #2a355a; border-radius: 4px; padding: 0 4%; }
.ladder-inner-135 { position:relative; height:100%; }
.lmark-135 { position:absolute; top:8px; width:2px; height:14px; }
.llabel-135 { position:absolute; top:26px; transform:translateX(-50%); font-size:0.72rem; white-space:nowrap; color:#8892b0; }
.slider-135 { width:100%; margin-top: 12px; accent-color:#00f0ff; }
.readout-135 { font-size:0.95rem; color:#ffcc00; font-weight:bold; }
</style>

<h4>Animasyon 1.3.5: Hız Merdiveni — Kavramadan Yırtılmaya <a name="animasyon-135-merdiven"></a></h4>
<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
  <div class="readout-135">Hız: <span id="v-read-135">1,00 c</span> — <span id="v-mode-135">TAM-SONİK</span></div>
  <div style="font-size:0.8rem; color:#8892b0;">Eksen logaritmiktir (0,1c → ~10⁴·c). Kaydırıcıyı sürükleyin.</div>
</div>
<input type="range" class="slider-135" id="slider135" min="-1" max="4.35" step="0.01" value="0">
<div class="ladder-135"><div class="ladder-inner-135" id="ladder135">
  <div style="position:absolute; top:14px; left:0; right:0; height:2px; background:linear-gradient(90deg,#3a4c8a 0%, #00f0ff 20%, #ff8800 45%, #ff00e5 88%, #ff0000 100%);"></div>
</div></div>
<div class="pol-canvas-wrap-135" style="margin-top:14px;"><canvas id="canvas135"></canvas></div>
<div class="desc-135" id="desc135"></div>

<script>
(function(){
  const canvas = document.getElementById('canvas135');
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  const wrap = canvas.parentElement;
  const slider = document.getElementById('slider135');
  const vRead = document.getElementById('v-read-135');
  const vMode = document.getElementById('v-mode-135');
  const desc = document.getElementById('desc135');
  const ladder = document.getElementById('ladder135');

  const LOGMIN = -1, LOGMAX = 4.35;
  const pos = lg => ((lg - LOGMIN) / (LOGMAX - LOGMIN) * 100);
  const marks = [
      [0,            'c (patinaj sınırı)',        '#00f0ff'],
      [0.1505,       '√2·c (denge zarfı)',        '#ff8800'],
      [0.2227,       'v_ekvator (proton)',        '#ffcc00'],
      [4,            'v_m (kohezyon sinyali)',    '#ff00e5'],
      [4.1505,       'v_kav (yırtılma)',          '#ff0000']
  ];
  marks.forEach(([lg, label, color]) => {
      const m = document.createElement('div'); m.className = 'lmark-135';
      m.style.left = pos(lg) + '%'; m.style.background = color; m.style.boxShadow = '0 0 5px ' + color;
      const l = document.createElement('div'); l.className = 'llabel-135';
      l.style.left = pos(lg) + '%'; l.style.color = color; l.textContent = label;
      ladder.appendChild(m); ladder.appendChild(l);
  });
  const dot = document.createElement('div');
  dot.style.cssText = 'position:absolute; top:10px; width:10px; height:10px; border-radius:50%; background:#fff; box-shadow:0 0 10px #fff; transform:translateX(-5px); z-index:3;';
  ladder.appendChild(dot);

  function regime(v){ // v: c biriminde
      if(v < 0.97)        return ['KAVRAMA', 'Zerre ortama kavrayarak ilerler; önünde yumuşak bir baş dalgası taşır. Işık, bu bölgenin tepe noktasında — tam-sonik rejimde — yaşar.'];
      if(v < 1.25)        return ['TAM-SONİK (IŞIK)', 'Tam patinaj sınırı: Zerre, ortamın basınç-iletim hızında yol alır (c = √(P/ρ); yerel ve değişkendir). Işık kalıcı olarak bu basamaktadır.'];
      if(v < 1.41)        return ['SÜPERSONİK — ŞOK', 'c aşıldı: kavramayla taşınamaz, Mach konisi (şok) açılır. Bu hız kavramayla sürdürülemez — ya şok üretip c\'ye geri oturur, ya da dengeye tırmanır.'];
      if(v < 1.8)         return ['DENGE ZARFI (√2·c bölgesi)', 'Vakum-cepli girdap zarfının zorunlu yüzey hızı: √2·c (Ek A.2). Protonun kompozit ekvator hızı (~1,67c) bu banttadır: yüzeyi c-altı dönen madde var olamaz.'];
      if(v < 10000)       return ['SÜRDÜRÜLEMEZ ARA BÖLGE', 'Denge bandının üstü, kavitasyon eşiğinin altı: burada kalıcı yapı yoktur. Cisimler şok üretip yavaşlar; yalnızca kohezyon kanalının SİNYALİ (v_m) bu bölgenin tepesine erişir.'];
      if(v < 14100)       return ['v_m — KOHEZYON SİNYAL HIZI', 'Dikkat: bu bir cisim hızı değil, yapısal bilginin hızıdır. Topografya/gradyan kurulumu ve dolanıklık geçidi (2.10.1) bu hızla ayarlanır: v_m = c·√(Σ/P₀) ≥ 10⁴·c.'];
      return ['YIRTILMA — MADDE DOĞUŞU', 'Kavitasyon eşiği aşıldı (v_kav = √2·c·√(1+Σ/P₀) ≈ √2·v_m): akışkan yırtılır, vakum cebi açılır, şok zarfı kurulur — madde doğar (bkz. Animasyon 1.3.2). v_saf, temel alt-bileşenlerin bu eşiği aşan saf dönüş hızlarıdır.'];
  }

  function resize(){ if(!canvas.isConnected) { window.removeEventListener('resize', resize); return; }
      canvas.width = wrap.clientWidth; canvas.height = wrap.clientHeight; }
  window.addEventListener('resize', resize); resize();

  let time = 0;
  function draw(){
      if(!canvas.isConnected) return;
      const W = canvas.width, H = canvas.height, cy = H/2, ox = W*0.32;
      const lg = parseFloat(slider.value), v = Math.pow(10, lg);
      dot.style.left = pos(lg) + '%';
      vRead.textContent = (v >= 100 ? v.toExponential(1).replace('e+','×10^') : v.toFixed(2)).replace('.', ',') + ' c';
      const [mode, text] = regime(v);
      vMode.textContent = mode; desc.textContent = text;

      ctx.fillStyle = '#02050a'; ctx.fillRect(0,0,W,H);
      time += 0.016;
      // ortam akış çizgileri (cisim sabit, ortam akar)
      const flow = Math.min(60, 8 + 10*Math.log10(1+v));
      ctx.strokeStyle = 'rgba(58,76,138,0.5)';
      for(let j=0;j<7;j++){
          const y = (j+1)*H/8;
          ctx.beginPath();
          for(let x=0;x<=W;x+=6){
              const ph = ((x + time*flow*10) % W);
              ctx.lineTo(x, y + 2*Math.sin(ph*0.05));
          }
          ctx.stroke();
      }
      if(v < 10000){
          // cisim
          const isMatterBand = (v >= 1.41 && v < 1.8);
          ctx.beginPath(); ctx.arc(ox, cy, 14, 0, 6.283);
          ctx.fillStyle = isMatterBand ? '#ffcc00' : '#f3f4f6'; ctx.fill();
          if(v < 1.0){
              // kavrama: yumuşak baş dalgaları
              for(let k=1;k<=3;k++){
                  ctx.beginPath(); ctx.arc(ox + 8*k + 6*Math.sin(time*3), cy, 14 + 9*k, -1.1, 1.1);
                  ctx.strokeStyle = 'rgba(0,240,255,' + (0.5/k) + ')'; ctx.stroke();
              }
          } else {
              // Mach konisi: yarım açı = asin(c/v)
              const a = Math.asin(Math.min(1, 1/v));
              const L = W*0.6;
              ctx.strokeStyle = (v < 1.41) ? 'rgba(255,136,0,0.9)' : 'rgba(255,0,229,0.8)';
              ctx.beginPath();
              ctx.moveTo(ox + L, cy - Math.tan(a)*L); ctx.lineTo(ox, cy); ctx.lineTo(ox + L, cy + Math.tan(a)*L);
              ctx.stroke();
              for(let k=1;k<=2;k++){
                  ctx.beginPath(); ctx.arc(ox - 10*k, cy, 6*k, 0, 6.283);
                  ctx.strokeStyle = 'rgba(255,136,0,' + (0.35/k) + ')'; ctx.stroke();
              }
          }
          if(isMatterBand){
              ctx.beginPath(); ctx.arc(ox, cy, 22 + 2*Math.sin(time*5), 0, 6.283);
              ctx.strokeStyle = '#ffcc00'; ctx.stroke();
              ctx.fillStyle = '#ffcc00'; ctx.font = 'bold 12px Segoe UI';
              ctx.fillText('kararlı zarf', ox - 34, cy - 30);
          }
      } else if(v < 14100){
          // kohezyon sinyal cephesi
          const fx = (time*1.4 % 1) * W;
          ctx.strokeStyle = '#ff00e5'; ctx.lineWidth = 3;
          ctx.beginPath(); ctx.moveTo(fx, 20); ctx.lineTo(fx, H-20); ctx.stroke(); ctx.lineWidth = 1;
          ctx.fillStyle = '#ff00e5'; ctx.font = 'bold 13px Segoe UI';
          ctx.fillText('yapısal sinyal (cisim değil)', W*0.36, 30);
      } else {
          // yırtılma
          const r = 26 + 6*Math.sin(time*6);
          ctx.beginPath(); ctx.arc(ox, cy, r, 0, 6.283); ctx.fillStyle = '#000'; ctx.fill();
          ctx.strokeStyle = '#ff0000'; ctx.lineWidth = 3; ctx.stroke(); ctx.lineWidth = 1;
          ctx.beginPath(); ctx.arc(ox, cy, r + 14, 0, 6.283); ctx.strokeStyle = 'rgba(255,0,229,0.8)'; ctx.stroke();
          ctx.fillStyle = '#ff0000'; ctx.font = 'bold 13px Segoe UI';
          ctx.fillText('vakum cebi + şok zarfı = madde', ox + r + 24, cy + 4);
      }
      requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();
</script>
</div>

Bu sıralama, maddenin öyküsünü iki ayrı hıza böler — **yaratma ve sürdürme:**

* **Yaratma ($v_{saf}>v_{kav}$):** Evrenakı'yı yırtarak maddeyi (şok zarfını) sıfırdan var eden şey; protonun yavaşlamış kompozit hızı olan $5 \times 10^8 \text{ m/s}$ değil, onu oluşturan temel alt-bileşenlerin o devasa kavitasyon eşiğini aşan **'saf dönüş' hızlarıdır**. Kavitasyon sınırını aşarak uzayı yırtan bu temel parçacıklar, viskozitenin sıfıra çok yakın olduğu bu süper-akışkanda enerjilerini gözlemsel ölçekte fark edilir biçimde dağıtmazlar; tam aksine **kendilerini (kuantize olmuş kararlı bir şok zarfı veya topolojik bir hata olarak) yaratırlar.**
* **Sürdürme ($v_{denge}=\sqrt{2}\,c$):** Yırtık bir kez açıldıktan sonra zarf, artık kohezyona değil yalnızca arka plan basıncına ($P_0$) karşı çalışır ve Ek A.2'deki denge hızına oturur. Proton, bu önceden yırtılmış ölümsüz şok dalgalarının birleşip yavaşladığı kompozit bir makinedir: hızı kavitasyon eşiğinin çok altına düşmüştür, ama denge gereği lokal patinaj sınırını ($c$) daima aşar.

> **Ek B ile bağ (açık iş):** Ek B'deki asgari arka plan basıncı türetimi, yırtılmanın $P=0$'da başladığını varsayar. Kohezyon dayanımı hesaba katıldığında bu koşul $P_0+\Sigma>\Delta P$ biçimini alır; iki ekin bu ortak paydada uzlaştırılması Bölüm 7.4'te kayıtlı açık iştir.

<div class="pol-widget-132" id="animasyon-132-kavitasyon">
<style>
.pol-widget-132 { --pol-blue:#00f0ff; --pol-magenta:#ff00e5; background:#0b0f19; border:1px solid rgba(0,240,255,0.2); border-radius:10px; padding:16px; font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif; color:#f3f4f6; max-width:900px; margin:1.5em auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
.pol-widget-132 h4 { color:var(--pol-blue); font-size:1rem; text-transform:uppercase; letter-spacing:1px; margin:0 0 10px 0; }
.pol-controls-132 { display:flex; justify-content: space-between; align-items: center; margin-bottom:15px; }
.btn-group-132 { display:flex; gap: 10px; }
.btn-132 { background: rgba(0, 240, 255, 0.1); border: 1px solid var(--pol-blue); color: var(--pol-blue); padding: 8px 16px; border-radius: 4px; cursor: pointer; transition: all 0.2s; font-weight: bold; }
.btn-132:hover:not(:disabled) { background: rgba(0, 240, 255, 0.3); }
.btn-132:disabled { border-color: #3a4c8a; color: #3a4c8a; cursor: not-allowed; background: transparent; }
.stage-indicator { font-weight: bold; color: #ffcc00; }
.pol-canvas-wrap-132 { width:100%; height:400px; border-radius:8px; overflow:hidden; background:#02050a; position:relative; }
.pol-canvas-wrap-132 canvas { display:block; width:100%; height:100%; }
.stage-desc-132 { background: rgba(255,0,229,0.1); padding: 12px; border-radius: 4px; border: 1px solid rgba(255,0,229,0.3); margin-top: 10px; font-size: 0.95rem; line-height: 1.5; color: #f3f4f6; min-height: 48px; }
.scale-wrap-132 { margin-top: 25px; background: rgba(0,0,0,0.5); padding: 10px; border-radius: 4px; position: relative; height: 40px; border: 1px solid #2a355a; }
.scale-marker { position: absolute; top: 10px; width: 2px; height: 12px; background: #fff; }
.scale-label { position: absolute; top: 28px; transform: translateX(-50%); font-size: 0.75rem; color: #8892b0; white-space: nowrap; }
</style>

<h4>Animasyon 1.3.2: Kavitasyon ve Maddenin Doğuşu <a name="animasyon-132-kavitasyon"></a></h4>
<div class="pol-controls-132">
  <div class="stage-indicator">Aşama: <span id="stg-num-132">1</span> / 4</div>
  <div class="btn-group-132">
      <button class="btn-132" id="btn-prev-132" disabled>Geri</button>
      <button class="btn-132" id="btn-next-132">İleri</button>
  </div>
</div>
<div class="pol-canvas-wrap-132"><canvas id="canvas132"></canvas></div>
<div class="stage-desc-132" id="stg-desc-132">Aşama 1: Homojen akışkanda giderek hızlanan yerel bir dönüş (mikro-girdap) başlar. Akışkan henüz bütündür.</div>

<div class="scale-wrap-132">
    <div style="position:relative; width:80%; margin: 0 auto; height:100%;">
        <div style="position:absolute; top:15px; left:0; right:0; height:2px; background: linear-gradient(90deg, #3a4c8a 0%, #ff00e5 80%, #ff0000 100%);"></div>
        <div class="scale-marker" style="left:0%;"></div><div class="scale-label" style="left:0%;">0 m/s</div>
        <div class="scale-marker" style="left:10%; background: var(--pol-blue); box-shadow: 0 0 5px var(--pol-blue);"></div><div class="scale-label" style="left:10%; color: var(--pol-blue);">c (Patinaj Sınırı)</div>
        <div class="scale-marker" style="left:90%; background: #ffcc00; box-shadow: 0 0 5px #ffcc00;"></div><div class="scale-label" style="left:90%; color: #ffcc00; font-weight: bold;">Kavitasyon (Yırtılma) Eşiği</div>
        <div id="speed-bar-132" style="position:absolute; top:15px; left:0; width:0%; height:2px; background:#fff; box-shadow:0 0 8px #fff; transition:width 0.5s; z-index:2;"></div>
        <div id="speed-dot-132" style="position:absolute; top:12px; left:0%; width:8px; height:8px; border-radius:50%; background:#fff; transform:translateX(-4px); transition:left 0.5s; box-shadow:0 0 10px #fff; z-index:3;"></div>
    </div>
</div>

<script>
(function(){
  const canvas = document.getElementById('canvas132');
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  const wrap = canvas.parentElement;
  
  let stage = 1;
  const btnPrev = document.getElementById('btn-prev-132');
  const btnNext = document.getElementById('btn-next-132');
  const stgNum = document.getElementById('stg-num-132');
  const stgDesc = document.getElementById('stg-desc-132');
  const speedBar = document.getElementById('speed-bar-132');
  const speedDot = document.getElementById('speed-dot-132');

  const descriptions = [
      "Aşama 1: Homojen akışkanda giderek hızlanan yerel bir dönüş (mikro-girdap) başlar. Akışkan henüz bütündür, yırtılma yoktur.",
      "Aşama 2: Dönüş hızı muazzam kavitasyon eşiğini aşar; akışkan fiziksel olarak yırtılır ve merkezde bir vakum boşluğu (void) açılır.",
      "Aşama 3: Yırtığın çevresinde çökmeye çalışan akışkan, dönüşün merkezkaçıyla dengelenir ve kararlı bir 'şok zarfı' oluşur. Madde doğmuştur.",
      "Aşama 4: Direnç (Kalıcılık) - Dış basınç (Evrenakı P₀) zarfı ezmeye çalışsa da, içerideki 'saf dönüş' sürdükçe şok zarfı kendini daima yeniden kurar; yapı ölümsüzleşir."
  ];

  const speedTargets = [ "3%", "10%", "90%", "95%" ];

  btnNext.onclick = () => { if(stage < 4) { stage++; updateStage(); } };
  btnPrev.onclick = () => { if(stage > 1) { stage--; updateStage(); } };

  function updateStage() {
      btnPrev.disabled = (stage === 1);
      btnNext.disabled = (stage === 4);
      stgNum.textContent = stage;
      stgDesc.textContent = descriptions[stage-1];
      
      let w = speedTargets[stage-1];
      speedBar.style.width = w;
      speedDot.style.left = w;
      
      initParticles();
  }

  function resize(){ if(typeof canvas !== "undefined" && !canvas.isConnected) { window.removeEventListener("resize", resize); return; } 
      canvas.width = wrap.clientWidth;
      canvas.height = wrap.clientHeight;
      initParticles();
  }
  window.addEventListener('resize', resize);
  
  let particles = [];
  const numParticles = 1000;
  let cx = 0, cy = 0;
  
  function initParticles() {
      particles = [];
      cx = canvas.width / 2;
      cy = canvas.height / 2;
      
      for(let i=0; i<numParticles; i++) {
          let r = Math.random() * Math.max(cx, cy) * 1.5;
          let a = Math.random() * Math.PI * 2;
          particles.push({
              baseR: r,
              a: a,
              r: r
          });
      }
  }

  let time = 0;

  function draw() {
      if(typeof canvas !== "undefined" && !canvas.isConnected) return;
      if(!canvas.isConnected) return;
      ctx.fillStyle = 'rgba(2, 5, 10, 0.25)'; 
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      time += 0.016;

      let voidRadius = 0;
      let rotationSpeed = 0.02;
      let showShock = false;
      let crushSpike = 0;

      if(stage === 1) {
          rotationSpeed = 0.03 + (Math.sin(time)*0.01);
          voidRadius = 0;
      } else if (stage === 2) {
          rotationSpeed = 0.2;
          voidRadius = 45 + Math.random()*15; 
      } else if (stage === 3) {
          rotationSpeed = 0.15;
          voidRadius = 55;
          showShock = true;
      } else if (stage === 4) {
          rotationSpeed = 0.18;
          voidRadius = 55;
          showShock = true;
          if(Math.sin(time*8) > 0.85) crushSpike = Math.random() * 25;
      }

      ctx.globalCompositeOperation = 'lighter';

      if(showShock) {
          let rEdge = voidRadius - crushSpike;
          if(rEdge < 10) rEdge = 10;
          let grad = ctx.createRadialGradient(cx, cy, rEdge - 5, cx, cy, rEdge + 25);
          grad.addColorStop(0, 'rgba(255, 0, 229, 0)');
          grad.addColorStop(0.2, 'rgba(255, 0, 229, 0.9)');
          grad.addColorStop(0.6, 'rgba(0, 240, 255, 0.5)');
          grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
          
          ctx.beginPath();
          ctx.arc(cx, cy, rEdge + 25, 0, Math.PI*2);
          ctx.fillStyle = grad;
          ctx.fill();
      }

      ctx.fillStyle = 'rgba(0, 240, 255, 0.7)';
      for(let i=0; i<particles.length; i++) {
          let p = particles[i];
          
          let v = rotationSpeed * (80 / (p.r + 10));
          p.a += v;
          
          let targetR = p.baseR;
          
          if(stage >= 2) {
              if(targetR < voidRadius) targetR = voidRadius + Math.random()*8; 
          }
          if(stage === 4 && p.baseR < voidRadius + 30) {
              targetR -= crushSpike; 
              if(targetR < 15) targetR = 15; 
          }
          
          p.r += (targetR - p.r) * 0.15;

          let x = cx + Math.cos(p.a) * p.r;
          let y = cy + Math.sin(p.a) * p.r;
          
          if(stage >= 2 && p.r < voidRadius + 18) {
              ctx.fillStyle = 'rgba(255, 204, 0, 0.9)'; 
          } else {
              ctx.fillStyle = 'rgba(0, 240, 255, 0.5)';
          }

          ctx.fillRect(x, y, 1.5, 1.5);
      }
      
      if(stage >= 2) {
          ctx.globalCompositeOperation = 'source-over';
          ctx.beginPath();
          let rCore = voidRadius - crushSpike - 5;
          if(rCore < 0) rCore = 0;
          ctx.arc(cx, cy, rCore, 0, Math.PI*2);
          ctx.fillStyle = '#000000';
          ctx.fill();
      }

      requestAnimationFrame(draw);
  }

  setTimeout(() => { resize(); updateStage(); draw(); }, 100);
})();
</script>
</div>

