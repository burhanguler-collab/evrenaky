# 4. Işık Hakkında Öğrendiğiniz Her Şey Yanlış

Bir önceki bölümde ışığın Zerre denen su damlacıklarından oluştuğunu gördük. Şimdi sıra, okulda ışıkla ilgili size ezberletilen o pürüzsüz masalların altındaki çatlakları göstermeye geldi. Hazır olun: aynadaki yansımadan gökkuşağına, mercekten girişime kadar, standart fiziğin "hallettim" dediği her konu aslında **halının altına süpürülmüş bir çelişkidir.**

## 1. Ayna Neden Yansıtır? (Atomlar Yansıtamaz!)

Size ışığın "atomlardan sekerek" yansıdığı söylendi. Ama küçük bir sorun var: Atomlar minik toplardır ve aralarında dev boşluklar vardır. Bir atomik yüzey, mikroskobik ölçekte pürüzlü, dağ bayır bir arazidir. Böyle bir yüzeye çarpan ışık, her yöne saçılıp dağılırdı — asla düzgün bir ayna görüntüsü oluşturamazdı. O halde tertemiz aynada kendinizi nasıl görüyorsunuz?

Cevap **Evrenakı Rampası**'nda gizli — ama sakın onu sabit, cansız bir duvar sanmayın. Bu görünmez basınç kalkanını, atomun dış kabuğundaki **elektronlar** yaratır. Ve elektronlar durmadan döndüğü için, yüzeydeki bu kalkan da sürekli **açılıp kapanır**: bir perde gibi bir kapanır, bir açılır, bir kapanır... Işık atomlara değil, elektronların ördüğü işte bu **açılıp kapanan sıvı kalkana** çarpar.

> [!NOTE]
> **Asıl Sır: Açı Değil, Zamanlama!** İşte teoriyi anlamanın kilit noktası burası — yanlış bilinen şey de burada. Işığın yansıyıp yansımayacağını belirleyen şey, rampaya hangi **açıyla** geldiği DEĞİLDİR. Belirleyici olan **zamanlamadır:** Zerre katarı tam da kalkanın **kapalı** (en yoğun) olduğu ana denk gelirse geçemez, geri seker → **yansıma**. Kalkanın **açık** olduğu (elektronların o an başka tarafta olup boşluk bıraktığı) ana denk gelirse hiç dirençle karşılaşmadan içeri süzülür → **kırılma/geçme**. Yani mesele şu kadar basit: *Işık geldiğinde kapı açık mıydı, kapalı mıydı?*
>
> (Elbette rampaya sıyırarak, yatık gelen bir zerrenin bu kalkanı yarıp içeri dalması daha zordur; o yüzden yatık gelenler daha çok yansır. Ama işi bitiren şey açı değil, **elektronların açtığı kapının o anki ritmidir.** Açı sadece işi kolaylaştırır ya da zorlaştırır; kararı veren senkronizasyondur.)

<div style="width: 100%; height: 320px; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid rgba(0, 200, 255, 0.2); box-shadow: 0 0 20px rgba(0, 200, 255, 0.1); margin-top: 20px; margin-bottom: 20px;">
    <canvas id="ramp-sync-canvas" style="width: 100%; height: 100%; display: block; background: #04070f;"></canvas>
    <div style="position: absolute; bottom: 10px; left: 10px; color: rgba(255,255,255,0.65); font-size: 12px;">Zerreler hep aynı açıyla gelir — kararı AÇI değil, rampanın o anki durumu verir:<br>KAPALIYKEN gelenler sekiyor (yansıma) · AÇIKKEN gelenler geçiyor (kırılma)</div>
</div>

<script>
(function() {
    const canvas = document.getElementById('ramp-sync-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;
    let width, height;
    function resize() { if(typeof canvas !== "undefined" && !canvas.isConnected) { window.removeEventListener("resize", resize); return; }
        const rect = canvas.parentElement.getBoundingClientRect();
        width = rect.width; height = rect.height;
        canvas.width = width * dpr; canvas.height = height * dpr; ctx.scale(dpr, dpr);
    }
    window.addEventListener('resize', resize); resize();

    const surfaceY = () => height * 0.60;
    const parts = [];
    let t = 0;
    // rampa açık mı kapalı mı? elektronların süpürmesiyle periyodik açılıp kapanır
    function rampClosed(){ return Math.sin(t*2.2) > 0; }

    function spawn(){
        // TÜM zerreler aynı açıyla (dik-ish, hepsi aynı) gelir: açı belirleyici DEĞİL
        parts.push({ x: 40 + Math.random()*(width-80), y: -10, vx: 0.6, vy: 3.2, spin:0, decided:false, passed:false, life:0 });
    }
    for(let i=0;i<5;i++) spawn();

    function animate(){
        if(typeof canvas !== "undefined" && !canvas.isConnected) return;
        t += 0.03;
        ctx.fillStyle = 'rgba(4,7,15,0.30)'; ctx.fillRect(0,0,width,height);
        const sy = surfaceY();
        const closed = rampClosed();
        // madde
        ctx.fillStyle = 'rgba(0,120,180,0.12)'; ctx.fillRect(0, sy, width, height-sy);
        // elektronlar (rampayı yaratan): yüzey boyunca süpüren iki nokta
        for(let e=0;e<2;e++){
            const ex = (width/2) + Math.sin(t*2.2 + e*Math.PI)*(width*0.32);
            ctx.fillStyle = 'rgba(120,200,255,0.9)';
            ctx.beginPath(); ctx.arc(ex, sy, 5, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = 'rgba(120,200,255,0.25)';
            ctx.beginPath(); ctx.arc(ex, sy, 12, 0, Math.PI*2); ctx.fill();
        }
        // rampa: kapalıyken kalın parlak çizgi, açıkken kesik/soluk
        if(closed){
            ctx.strokeStyle = 'rgba(0,240,255,0.95)'; ctx.lineWidth = 5; ctx.setLineDash([]);
        } else {
            ctx.strokeStyle = 'rgba(0,240,255,0.30)'; ctx.lineWidth = 2; ctx.setLineDash([10,12]);
        }
        ctx.beginPath(); ctx.moveTo(0, sy); ctx.lineTo(width, sy); ctx.stroke(); ctx.setLineDash([]);
        ctx.fillStyle = closed ? 'rgba(0,240,255,0.95)' : 'rgba(0,240,255,0.55)';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText(closed ? 'RAMPA KAPALI (elektron kalkanı yüzeyi tutuyor)' : 'RAMPA AÇIK (elektronlar başka tarafta, boşluk var)', 12, sy-10);

        for(let i=parts.length-1;i>=0;i--){
            const p=parts[i]; p.life++;
            p.x+=p.vx; p.y+=p.vy; p.spin+=0.3;
            if(!p.decided && p.y>=sy){
                p.decided = true;
                if(closed){ p.vy = -Math.abs(p.vy); }   // kapalı: sek (yansı)
                else { p.passed = true; }                // açık: geç (kırıl)
            }
            if(p.passed){ p.vy*=0.995; }
            ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.spin);
            ctx.fillStyle = p.passed ? '#ff8c42' : '#fffc00';
            ctx.shadowBlur=12; ctx.shadowColor = p.passed ? '#ff8c42' : '#ffe600';
            ctx.beginPath(); ctx.arc(0,0,4,0,Math.PI*2); ctx.fill();
            ctx.restore();
            if(p.x>width+20 || p.y>height+30 || p.y< -40 || p.life>600){ parts.splice(i,1); spawn(); }
        }
        if(parts.length<6 && Math.random()<0.05) spawn();
        requestAnimationFrame(animate);
    }
    animate();
})();
</script>

## 2. Gökkuşağı ve "Kusurlu" Mercekler

Optikçiler mükemmel bir mercek yapmaya çalışırken iki baş belasıyla boğuşur: **küresel sapma** (kenardan geçen ışık ile merkezden geçen ışığın farklı noktalara odaklanması) ve **renk sapması** (kırmızı ile mavinin farklı açılarla kırılıp odağı bulanıklaştırması). Modern optik bunları "camın kusuru" diye geçiştirir. Oysa bunlar kusur değil, **ışığın gerçek doğasının kanıtıdır:** Farklı renkteki (farklı frekanstaki) Zerreler, Evrenakı sıvısında farklı miktarda patinaj yaptığı için farklı açılarla kırılır. Prizmanın gökkuşağı üretmesi de, merceğin renkleri ayırması da tek ve aynı sebepten: **hız, sıvının yoğunluğuna göre değişir.**

## 3. Girişim: "Yok Olan" Enerji Nereye Gidiyor?

En sevdikleri masal budur. İki ışık demetini üst üste bindirdiğinizde ekranda aydınlık-karanlık şeritler (saçaklar) oluşur. Bilim insanları karanlık şeritler için *"dalgalar birbirini yok etti, enerji söndü"* der. Ama termodinamiğin birinci kuralı ne diyordu? **Enerji yoktan var, vardan yok olmaz!**

İşin komiği, kendi ölçüm aletleri de onları yalanlıyor: Karanlık bölgede kaybolduğu söylenen enerji, aydınlık bölgede **birebir fazladan** ortaya çıkıyor (aydınlık saçağın parlaklığı, tek demetin tam 4 katı). Yani enerji yok olmuyor, sadece karanlık noktadan aydınlık noktaya **fiziksel olarak göç ediyor.**

Peki soyut bir "olasılık dalgası" bir ışık taneciğini tutup nasıl başka bir noktaya taşısın? Taşıyamaz. Evrenakı'da ise cevap nettir: Zerreler, birbirlerinin ardında bıraktığı düşük basınçlı **iz kanallarına (wake)** kapılır — tıpkı bisikletçilerin öndekinin rüzgâr boşluğuna girmesi gibi — ve hep aynı yörüngelere (aydınlık saçaklara) yığılır. Karanlık şeritler, Zerre'nin uğramadığı boş koridorlardır. **Hiçbir enerji ölmez; sadece taşınır.**

## Toparlayalım

Yansıma, kırılma, yutulma, girişim, renkler, mercek "kusurları"... Modern fizik bunları açıklamak için altı ayrı, birbirini tutmayan model kurmak zorunda kaldı. Evrenakı ise hepsini **tek bir cümleyle** açıklıyor: *Işık, yoğunluğu yer yer değişen bir sıvının içinde yol alan fiziksel bir damladır.* Gerisi sadece geometridir.

Şimdi daha da derine ineceğiz. Bu Zerrelerin ve maddenin en temelinde, evrenin motorunu döndüren o gizemli **dördüncü boyuta** gidiyoruz.


---

## Bu Bölümde Ne Öğrendik?

> [!NOTE]
> - **Eski Fizik:** Işığın davranışı, yansıma, kırılma ve yutulma için ayrı ayrı karmaşık modeller gerektirir.
> - **Evrenakı Teorisi:** Tüm bu olaylar, Zerrelerin (mermilerin) çarptığı yüzeyin atomik yoğunluğuna bağlı tek bir mekanik kuralla (Akışkanlar Mekaniği) açıklanır.

> [!TIP]
> Bu bölümün matematiksel ispatlarını ve akademik dildeki detaylı açıklamalarını görmek için **[Akademik Sürüm Kısım 4'ye geçiş yapın](#akademik_04)**.
