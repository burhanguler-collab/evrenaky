# 2. Elma Neden Düşmez, İtilir! (Kütle-İtim)

Isaac Newton'un kafasına elma düşünce, gezegenlerin ve nesnelerin birbirini uzaktan uzağa gizemli bir kuvvetle "çektiğini" düşündü ve buna kütleçekimi (gravity) adını verdi. Yaklaşık 250 yıl sonra Albert Einstein geldi ve dedi ki: "Hayır, çekim yok; kütle uzay-zaman denilen görünmez bir çarşafı büküyor, cisimler de bu çukura yuvarlanıyor."

Kulağa hoş geliyor. Ama iki dâhi de kaçamadıkları o dev soruyu halının altına süpürdü: **Arada hiçbir fiziksel bağ, hiçbir ip, hiçbir temas yokken bir cisim diğerini nasıl çeker?**

Elinizdeki mıknatısı bir düşünün — en azından onun görünmez alan çizgileri var. Ama Newton'un çekimi tamamen büyü gibidir: Güneş, 150 milyon kilometre öteden Dünya'yı hiçbir şeye dokunmadan tutuyor. Bu, Jedi'ların uzaktan kılıç çekmesinden farksız, mistik bir masal. Einstein'ın "bükülen çarşafı" da işi kurtarmıyor: Bir geometri, bir şekil, uzaydaki gerçek bir cismi nasıl **iteleyip** hızlandırabilir? Şeklin eli mi var? İşte tam burada modern fizik susar ve konuyu değiştirir.

## Çekim Diye Bir Şey Yok!

Evrenakı Teorisinin cevabı klasik ezberleri sarsar: **"Çekim" diye bir şey yoktur.** Düşen elmayı yer çeki-**mi**-yor; uzay onu iti-**yor**! Biz buna **Kütle-İtim (Push-Gravity)** diyoruz.

Nasıl mı? Birinci bölümde uzayın devasa bir süper-akışkan (Evrenakı) okyanusu olduğunu öğrenmiştik. Dünya, kendi etrafında saatte 1.600 km hızla dönerken bu görünmez sıvıyı da bir mikser gibi çevirir ve çevresinde muazzam bir girdap oluşturur.

Şimdi lise fizik dersinden ya da uçakların nasıl uçtuğundan bildiğiniz o kuralı hatırlayın — **Bernoulli İlkesi:** *Bir akışkan nerede hızlanırsa, orada basınç düşer.* Uçağın kanadının üstünde hava hızlanır, basınç düşer, uçak yukarı emilir. Aynı şey Dünya'nın çevresindeki sıvı girdabında da olur: Merkeze yaklaştıkça sıvı hızlanır, basınç dibe vurur. Dünya'nın tam ortası, kocaman bir **"alçak basınç kuyusudur."**

Sonra ne olur? Uzayın derinliklerindeki durgun, **yüksek basınçlı** Evrenakı, tıpkı yüksek basıncın alçak basınca hücum etmesi gibi, gezegenin o düşük basınçlı merkezine doğru üşüşür. İşte dalından kopan elma yer tarafından "çekilmez"; çevredeki bu yüksek basınçlı okyanus tarafından merkeze doğru **itilir!** Selin ortasına düşen bir tahta parçasından hiçbir farkımız yok — hepimiz merkeze doğru itiliyoruz.

<div style="width: 100%; height: 350px; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid rgba(255, 0, 127, 0.2); box-shadow: 0 0 20px rgba(255, 0, 127, 0.1); margin-top: 20px; margin-bottom: 20px;">
    <canvas id="gravity-canvas" style="width: 100%; height: 100%; display: block; background: #070308;"></canvas>
    <div style="position: absolute; top: 10px; left: 10px; color: white; background: rgba(0,0,0,0.7); padding: 5px 10px; border-radius: 4px; font-size: 13px;">Gezegen (Alçak Basınç Girdabı)</div>
</div>

<script>
(function() {
    const canvas = document.getElementById('gravity-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;
    let width, height;
    
    function resize() { if(typeof canvas !== "undefined" && !canvas.isConnected) { window.removeEventListener("resize", resize); return; } 
        const rect = canvas.parentElement.getBoundingClientRect();
        width = rect.width;
        height = rect.height;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.scale(dpr, dpr);
    }
    window.addEventListener('resize', resize);
    resize();
    
    const centerX = width / 2;
    const centerY = height / 2;
    
    const apples = [];
    function spawnApple() {
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.max(width, height) / 2 + 50;
        apples.push({
            x: centerX + Math.cos(angle) * radius,
            y: centerY + Math.sin(angle) * radius,
            angle: angle,
            dist: radius,
            color: Math.random() > 0.5 ? '#ff4d4d' : '#ffffff',
            size: Math.random() * 3 + 2
        });
    }
    
    for(let i=0; i<30; i++) spawnApple();
    
    let time = 0;
    
    function animate() {
      if(typeof canvas !== "undefined" && !canvas.isConnected) return;
        ctx.fillStyle = 'rgba(7, 3, 8, 0.2)';
        ctx.fillRect(0, 0, width, height);
        
        ctx.beginPath();
        ctx.arc(centerX, centerY, 30, 0, Math.PI * 2);
        ctx.fillStyle = '#00f2fe';
        ctx.shadowBlur = 20;
        ctx.shadowColor = '#4facfe';
        ctx.fill();
        ctx.shadowBlur = 0;
        
        ctx.strokeStyle = 'rgba(79, 172, 254, 0.1)';
        ctx.lineWidth = 1;
        for(let r=50; r<Math.max(width,height); r+=30) {
            ctx.beginPath();
            ctx.arc(centerX, centerY, r, 0, Math.PI * 2);
            ctx.stroke();
        }
        
        for (let i = apples.length - 1; i >= 0; i--) {
            let a = apples[i];
            a.angle += 0.02;
            a.dist -= 1.5;
            a.x = centerX + Math.cos(a.angle) * a.dist;
            a.y = centerY + Math.sin(a.angle) * a.dist;
            
            ctx.fillStyle = a.color;
            ctx.beginPath();
            ctx.arc(a.x, a.y, a.size, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.strokeStyle = `rgba(255,255,255,0.3)`;
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            let tailX = centerX + Math.cos(a.angle - 0.1) * (a.dist + 10);
            let tailY = centerY + Math.sin(a.angle - 0.1) * (a.dist + 10);
            ctx.lineTo(tailX, tailY);
            ctx.stroke();
            
            if (a.dist < 30) {
                apples.splice(i, 1);
                spawnApple();
            }
        }
        
        if(Math.random() < 0.1) spawnApple();
        
        time += 0.05;
        requestAnimationFrame(animate);
    }
    animate();
})();
</script>

## Neden Her Şey Aynı Hızda Düşer?

Galileo, Pisa Kulesi'nden bir tüyle bir gülleyi (havasız ortamda) bıraktığınızda ikisinin de **aynı anda** yere düştüğünü göstermişti. Modern fizik bunu "e işte öyle, çekim kütleyle orantılı" diye geçiştirir. Ama neden? Evrenakı bunu su gibi berrak açıklar: İtici basınç, cismin dış görünüşüne, rengine, cinsine değil, içindeki en temel yapı taşlarının (nükleonların) sayısına bindiği için, hangi maddeden yapılmış olursa olsun her cisim aynı ivmeyle merkeze itilir. Sırf ağırdır diye daha hızlı düşmez; çünkü onu "ağır" yapan şeyin ta kendisi, itilen malzemedir.

## Düşündürücü Soru

Diyelim ki kütleler gerçekten birbirini "çekiyor". O halde karanlık uzayın ortasında, birbirinden milyarlarca kilometre uzaktaki iki asteroit, birbirinin tam olarak **nerede** olduğunu nasıl biliyor da o yöne kuvvet uyguluyor? Aralarına gizli bir telefon hattı mı çekilmiş? Oysa uzay bir sıvıysa hiç sorun yok: Aralarındaki sıvının basıncı, dıştaki basınçtan düşük kalır ve dış okyanus bu iki taşı bir vakum etkisiyle usulca yan yana **iter**. Ne ip gerekir, ne büyü, ne de gizli haberleşme. Ne kadar mantıklı, değil mi?

Kütleyi çözdük. Peki ya ışık? Sonraki bölümde ışığın o meşhur "hem dalga hem parçacık" efsanesini yerle bir edeceğiz.


---

## Bu Bölümde Ne Öğrendik?

> [!NOTE]
> - **Eski Fizik:** Cisimler birbirini gizemli, temas gerektirmeyen bir kütleçekim kuvvetiyle 'çeker'.
> - **Evrenakı Teorisi:** Çekim yoktur; basınç farkından doğan bir 'itme' vardır (Kütle-İtimi). Gezegenlerin çevresindeki girdap, cisimleri merkeze doğru iter.

> [!TIP]
> Bu bölümün matematiksel ispatlarını ve akademik dildeki detaylı açıklamalarını görmek için **[Akademik Sürüm Kısım 2'ye geçiş yapın](#akademik_02)**.
