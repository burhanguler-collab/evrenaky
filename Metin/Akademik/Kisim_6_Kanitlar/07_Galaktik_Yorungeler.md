## Bölüm 6.5 — Galaktik Yörüngeler ve Karanlık Madde Probleminin Çözümü

Astrofiziğin son yüzyıldaki en büyük çözülemeyen gizemlerinden biri, galaksilerin dış kollarındaki yıldızların dönme hızlarıdır. Klasik Newton mekaniğine ve Einstein'ın Genel Görelilik teorisine göre, galaksinin merkezinden uzaklaştıkça kütleçekim kuvvetinin $1/r^2$ ile zayıflaması ve dolayısıyla yıldızların yörünge hızlarının düşmesi gerekir. Tıpkı Güneş Sistemimizde Güneş'ten uzaklaştıkça gezegenlerin daha yavaş dönmesi gibi.

Ancak 1970'lerde Vera Rubin ve meslektaşları tarafından yapılan hassas gözlemler, sarmal galaksilerin dış kollarındaki yıldızların hızının düşmediğini, aksine çok yüksek hızlarda **sabitlendiğini** (asimptota oturduğunu) kanıtlamıştır. Standart fiziğe göre bu hızlarda dönen yıldızların galaksiden kopup uzaya savrulması gerekirdi. Bu muazzam hızı dengede tutacak görünürde hiçbir kütle olmadığı için astrofizikçiler, galaksiyi devasa bir hale gibi saran görünmez bir kütle uydurmak zorunda kaldılar: **Karanlık Madde**.

Bu bölüm, Evrenakı teorisinin hiçbir "görünmez madde" varsayımına ihtiyaç duymadan, sadece kendi yerel mekanik postülatlarıyla bu kozmolojik anomalinin üstesinden nasıl geldiğini ve düz dönüş eğrilerini doğal yollarla nasıl türettiğini göstermektedir.

### 6.5.1 Kütleçekim Grafiği ve $1/r$ Kuvvetinin Yükselişi

Evrenakı teorisinde galaksi merkezlerindeki süper kütleli kara deliklerin dönüş hızları olağanüstü yüksektir. Teorinin temel postülatlarından olan **Eksenel İtim (F4)** ve ona bağlı hidrodinamik yansımalar, galaksi çekirdeğindeki bu devasa dönüşün (devrin) bir sonucudur.

Kritik nokta şudur: Klasik merkezcil kütleçekim $1/r^2$ profiliyle zayıflarken, teorinin öngördüğü eksenel kuvvet (Kısım 4'te türetildiği üzere) $1/r$ profiliyle sönümlenir. Galaksinin dış bölgelerine çıkıldıkça $1/r^2$'ye tabi klasik çekim hızla gücünü yitirir, ancak $1/r$ ile sönümlenen eksenel kuvvet profilde giderek baskın hale gelir. 

### 6.5.2 Matematiksel İspat: Düz Dönüş Eğrisinin Türetilmesi

Dairesel yörüngede dönen bir yıldızın dengede kalabilmesi için Merkezcil İvme'nin, kütleçekim ivmesi ile teorinin öngördüğü eksenel ivmenin toplamına eşit olması şarttır:

$$a_{merkezcil} = a_{kütleçekim} + a_{eksenel}$$

Terimleri kendi fiziksel bağımlılıklarıyla açtığımızda:
1. **Merkezcil İvme:** $\frac{v^2}{r}$
2. **Evrenakı Kütleçekim (Basınç Gradyanı):** $\frac{A}{r^2}$ *(Buradaki A sabiti, galaksinin merkez kütlesinin yarattığı hidrodinamik basınç düşümü ile orantılıdır)*
3. **Eksenel Kuvvet (Evrenakı):** $\frac{B}{r}$ *(Buradaki B sabiti, merkezdeki süper kütleli kara deliğin devri ve galaktik çekirdeğin dönüş karakteristiği ile orantılıdır)*

Eşitliği kuralım:
$$\frac{v^2}{r} = \frac{A}{r^2} + \frac{B}{r}$$

Denklemin her iki tarafını da yarıçap ($r$) ile çarptığımızda, yörünge hızı $v$ şu şekilde doğrudan elde edilir:
$$\mathbf{v = \sqrt{\frac{A}{r} + B}}$$

Bu zarif ve kompakt denklemin sunduğu fiziksel sonuç son derece derindir:
Klasik fizikte (B=0 kabul edildiğinde) yarıçap ($r$) büyüdükçe hız sıfıra yaklaşır. Ancak Evrenakı teorisinde, galaksinin çok uzak dış kollarına gidildiğinde ($r \to \infty$), $\frac{A}{r}$ terimi sıfıra yaklaşsa dahi yıldızın hızı sıfıra düşmez. Hız doğrudan **$\sqrt{B}$** limitine, yani sabit bir asimptota kilitlenir.

Astronomların teleskoplarla gözlemlediği meşhur **"Düz Dönüş Eğrisi" (Flat Rotation Curve)** profili, teorik altyapıda hiçbir yama kullanılmadan, tamamen doğal yollarla elde edilmiştir.

### 6.5.3 Gerçek Gözlem Verileriyle Sınama

Bu matematiksel model ($v = \sqrt{A/r + B}$), evrendeki farklı galaksi türlerinin hassas teleskop ölçümleriyle test edildiğinde kusursuz bir ampirik başarı sergilemektedir. Aşağıdaki testlerde kırmızı kesik çizgiler saf Newton mekaniğini, mavi çizgiler ise Evrenakı teorisinin $1/r$ eklemli formülünü temsil etmektedir.

#### 1. Sarmal Galaksiler: M33 ve NGC 3198
Sarmal galaksiler, karanlık madde probleminin en belirgin gözlemlendiği yapılardır. 
M33 (Triangulum) galaksisinde Newton kütleçekimi hızla düşüşe geçerken, Evrenakı modeli ölçülen hızı ~120 km/s bandında kusursuzca yakalamaktadır. Benzer şekilde, dönüş eğrisinin 30 kpc gibi inanılmaz uzak mesafelere kadar dümdüz kalmasıyla bilinen devasa NGC 3198 galaksisinde, $1/r$ eksenel itim kuvveti yıldız hızlarını ~150 km/s bandında pürüzsüz bir doğrulukla kilitlemektedir.

![M33 Gözlem Testi](Gorseller/m33_gozlem_testi.png)
![NGC 3198 Gözlem Testi](Gorseller/ngc3198_gozlem_testi.png)

#### 2. Dev Eliptik Galaksiler: M87 ve NGC 4472
Eliptik galaksiler sarmal bir diske sahip olmadıkları için net dönüş eğrileri vermezler. Yıldızlar rastgele yörüngelerde bir arı kovanı gibi hareket eder (hız dağılımı). Ancak bu galaksileri saran devasa sıcak X-ışını gaz halelerinden hesaplanan kütleçekim potansiyelleri ("Efektif Dairesel Hız" $V_c$), sarmal galaksilerdeki asimptotik düz yapıyı birebir tekrar eder. 
Evrenin en meşhur dev eliptik galaksilerinden olan M87 ve NGC 4472'nin merkezlerinde korkunç hızlarda dönen süper kütleli kara delikler bulunur. Bu devasa çekirdek dönüşünden kaynaklı eksenel itim, galaksi eliptik de olsa formülün aynı mükemmellikte çalışmasını sağlar.

![M87 Eliptik Testi](Gorseller/m87_eliptik_testi.png)
![NGC 4472 Eliptik Testi](Gorseller/ngc4472_eliptik_testi.png)

#### 3. Cüce Küresel (Dwarf Spheroidal) Galaksiler: Derin Bir Fiziksel Öngörü
Fornax (Ocak) gibi cüce küresel galaksiler, evrendeki karanlık maddenin oransal olarak en yoğun bulunduğu düşünülen, sadece 1-2 kpc boyutlarındaki minicik yapılardır. Çok düşük kütlelerine rağmen efektif hız profilleri $\sim18$ km/s bandında asimptota oturur.
Evrenakı modeli bu galaksilerde de pürüzsüz çalışarak hızı dengeler. Ancak burada astrofiziğe karşı çok derin bir meydan okuma yatar: Güncel astronomiye göre cüce küresellerde süper kütleli kara delik **yoktur**. 
Bu durum, teori açısından çok net bir fiziksel öngörüye işaret eder: Cüce küresel galaksilerin merkezinde astronominin henüz tespit edemediği, **küçük ve düşük hızda dönen gizli bir kara delik (çekirdek devri) bulunmak zorundadır.**

Evrenakı teorisine göre (Bkz. Bölüm 6.6 Gezegen Figürü), güçlü bir eksenel itim kuvveti galaksiyi basıklaştırarak sarmal bir disk formuna sokar. Bu galaksiler küresel formlarını koruduklarına göre, merkezdeki bu kara deliğin kütlesi küçük ve dönüş hızı (dolayısıyla yarattığı eksenel itim kuvveti - $B$ sabiti) nispeten zayıftır. 

Bu zayıf eksenel kuvvet, galaksiyi tamamen yassılaştırmaya yetmez ve küresel form büyük ölçüde korunur. Ancak eksenel itimin uzayda $1/r$ ile yavaş sönümlenme karakteristiği sayesinde, bu zayıf dönüş bile dış bölgelerdeki yıldız hızlarının sıfıra çakılmasını engelleyecek o kritik matematiksel desteği (B sabiti dengesini) sağlamak için yeterlidir. Evrenakı'nın $v = \\sqrt{A/r + B}$ formülü, bu düşük dönüş hızıyla da gözlemlere tam oturur.

![Fornax Küresel Testi](Gorseller/fornax_kuresel_testi.png)

### Sonuç
Evrenakı teorisinin kinematik denklemleri; sarmal, eliptik ve cüce küresel gözetmeksizin, dönen bir çekirdeğe sahip tüm galaktik yapılarda "Karanlık Madde" varsayımını tamamen ortadan kaldırmakta ve kütleçekim anomalisini kendi iç dinamikleriyle, saf matematiksel bir kesinlikle çözmektedir.

### İnteraktif Galaktik Yörünge Simülatörü

<div class="interactive-simulator" style="background-color: #121212; border: 1px solid #333; padding: 20px; border-radius: 8px; margin-top: 30px;">
  <p style="color: #aaa; font-size: 0.9em; margin-bottom: 20px;">Evrenakı formülünü ($v = \sqrt{A/r + B}$) kendiniz test edin! Merkez kütleyi (A) ve kara deliğin dönüş hızını (B) değiştirerek, klasik Newton çekiminin dış bölgelerde nasıl çöktüğünü ve Evrenakı eksenel itiminin hızı nasıl havada tuttuğunu anında gözlemleyin.</p>
  
  <div style="margin-bottom: 15px;">
    <label for="slider-A" style="color: #ddd; display: inline-block; width: 150px;">Merkezcil İtim (A): <span id="val-A" style="font-weight: bold; color: #ff5555;">200</span></label>
    <input type="range" id="slider-A" min="1" max="1000" value="200" style="width: 250px; vertical-align: middle;">
    <span style="color: #888; font-size: 0.8em; margin-left: 10px;">(Merkezi kütle / Basınç Gradyanı)</span>
  </div>
  
  <div style="margin-bottom: 25px;">
    <label for="slider-B" style="color: #ddd; display: inline-block; width: 150px;">Eksenel İtim (B): <span id="val-B" style="font-weight: bold; color: #55aaff;">150</span></label>
    <input type="range" id="slider-B" min="0" max="500" value="150" style="width: 250px; vertical-align: middle;">
    <span style="color: #888; font-size: 0.8em; margin-left: 10px;">(Kara deliğin dönüş hızı)</span>
  </div>

  <canvas id="galaxy-canvas" width="600" height="350" style="background-color: #0a0a0a; border: 1px solid #444; border-radius: 4px; display: block; max-width: 100%;"></canvas>
  
  <div style="margin-top: 15px; font-size: 0.9em;">
    <span style="color: #ff5555; font-weight: bold;">- - - Klasik Çekim ($v = \sqrt{A/r}$)</span> &nbsp; | &nbsp; 
    <span style="color: #55aaff; font-weight: bold;">── Evrenakı ($v = \sqrt{A/r + B}$)</span> &nbsp; | &nbsp;
    <span style="color: #ffff00;">● Temsili Sarmal Galaksi Verisi</span>
  </div>
</div>

<script>
(function() {
    function initSim() {
        const canvas = document.getElementById("galaxy-canvas");
        if (!canvas) {
            setTimeout(initSim, 50); // Canvas yüklenene kadar bekle
            return;
        }
        const ctx = canvas.getContext("2d");
        
        const sliderA = document.getElementById("slider-A");
        const sliderB = document.getElementById("slider-B");
        const valA = document.getElementById("val-A");
        const valB = document.getElementById("val-B");

        const obsData = [
            {r: 0.5, v: 12}, {r: 1.0, v: 16}, {r: 1.5, v: 18},
            {r: 2.0, v: 19.5}, {r: 2.5, v: 20}, {r: 3.0, v: 20.5},
            {r: 3.5, v: 21}, {r: 4.0, v: 21}, {r: 5.0, v: 21.5},
            {r: 6.0, v: 21}, {r: 7.0, v: 21.5}
        ];

        function drawGraph() {
            if (!sliderA || !sliderB) return;
            let A = parseFloat(sliderA.value);
            let B = parseFloat(sliderB.value);
            
            valA.textContent = A;
            valB.textContent = B;
            
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            const padding = 40;
            const width = canvas.width - padding * 2;
            const height = canvas.height - padding * 2;
            const xMax = 8.0; 
            const yMax = 35.0; 
            
            ctx.strokeStyle = "#333";
            ctx.lineWidth = 1;
            
            for(let i=0; i<=xMax; i+=1) {
                let x = padding + (i/xMax)*width;
                ctx.beginPath(); ctx.moveTo(x, padding); ctx.lineTo(x, canvas.height - padding); ctx.stroke();
                ctx.fillStyle = "#888"; ctx.font = "10px sans-serif";
                ctx.fillText(i, x - 3, canvas.height - padding + 15);
            }
            for(let i=0; i<=yMax; i+=5) {
                let y = (canvas.height - padding) - (i/yMax)*height;
                ctx.beginPath(); ctx.moveTo(padding, y); ctx.lineTo(canvas.width - padding, y); ctx.stroke();
                ctx.fillStyle = "#888"; ctx.font = "10px sans-serif";
                ctx.fillText(i, padding - 20, y + 4);
            }
            
            ctx.strokeStyle = "#777";
            ctx.beginPath(); ctx.moveTo(padding, padding); ctx.lineTo(padding, canvas.height - padding); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(padding, canvas.height - padding); ctx.lineTo(canvas.width - padding, canvas.height - padding); ctx.stroke();
            
            ctx.fillStyle = "#bbb";
            ctx.fillText("r (kpc) ->", canvas.width/2 - 15, canvas.height - 5);
            ctx.save();
            ctx.translate(15, canvas.height/2 + 20);
            ctx.rotate(-Math.PI/2);
            ctx.fillText("v (km/s) ->", 0, 0);
            ctx.restore();

            ctx.fillStyle = "#ffff00";
            obsData.forEach(pt => {
                let cx = padding + (pt.r / xMax) * width;
                let cy = (canvas.height - padding) - (pt.v / yMax) * height;
                ctx.beginPath();
                ctx.arc(cx, cy, 4, 0, Math.PI*2);
                ctx.fill();
            });
            
            function drawCurve(color, isDashed, func) {
                ctx.strokeStyle = color;
                ctx.lineWidth = 3;
                if(isDashed) ctx.setLineDash([6, 6]);
                else ctx.setLineDash([]);
                
                ctx.beginPath();
                let first = true;
                for(let px = 0; px <= width; px += 2) {
                    let r = (px / width) * xMax;
                    if(r < 0.1) continue; 
                    let v = func(r);
                    if(v > yMax) continue; 
                    
                    let cx = padding + px;
                    let cy = (canvas.height - padding) - (v / yMax) * height;
                    if(first) { ctx.moveTo(cx, cy); first = false; }
                    else { ctx.lineTo(cx, cy); }
                }
                ctx.stroke();
                ctx.setLineDash([]);
            }
            
            drawCurve("#ff5555", true, (r) => Math.sqrt(A / r));
            drawCurve("#55aaff", false, (r) => Math.sqrt(A / r + B));
        }
        
        sliderA.addEventListener("input", drawGraph);
        sliderB.addEventListener("input", drawGraph);
        
        drawGraph();
    }
    
    setTimeout(initSim, 100);
})();
</script>
