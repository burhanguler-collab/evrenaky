# 7. Karanlık Madde Masalı

Bu, modern kozmolojinin en büyük "kral çıplak" anıdır. Astrofizikçiler teleskoplarını galaksilere çevirdiklerinde beklemedikleri bir şey gördüler: Galaksinin merkezinden çok uzaktaki, kollardaki yıldızlar **olması gerekenden çok daha hızlı** dönüyordu. Newton'un formüllerine göre bu hızda dönen yıldızların çoktan uzaya savrulup gitmiş olması lazımdı. Ama gitmiyorlardı.

İşte kritik an. Bilim insanlarının önünde iki yol vardı:

1. *"Belki formüllerimiz, belki kütleçekim anlayışımız eksiktir."*
2. *"Formüllerimiz kusursuz; eksik olan evren. Demek ki oralarda göremediğimiz, dokunamadığımız, hiçbir aletle tespit edemediğimiz devasa bir görünmez kütle var."*

Tahmin edin hangisini seçtiler. İkinciyi. Kendi formüllerini sorgulamak yerine, kayıp olanı **icat ettiler** ve adını **Karanlık Madde** koydular. Sonra da rahatça açıkladılar: Evrenin görünen kısmı sadece %15; geri kalan %85'i bu göremediğimiz hayalet maddeymiş. Yani "bilmiyoruz" demek yerine, bilmedikleri şeye bir isim takıp onu evrenin efendisi ilan ettiler.

## Karanlık Madde Yok, Dev Bir Akıntı Var!

Evrenakı Teorisinde hayalet maddelere yer yoktur. Galaksinin dış kollarındaki yıldızların bu kadar hızlı dönmesinin sebebi son derece basit: **İçine kapıldıkları dev bir akıntı** (Makro-Girdap).

Galaksinin merkezindeki o muazzam yoğunluk (halk arasında "kara delik") akıl almaz bir hızla döner ve çevresindeki koca Evrenakı okyanusunu da devasa bir girdap halinde çevirir. Dış kollardaki yıldızlar merkeze "görünmez bir kütle tarafından çekildikleri" için değil, içine düştükleri bu **görünmez su girdabının akıntısına kapıldıkları** için o hızla sürüklenirler.

Bunu her gün mutfağınızda görüyorsunuz: Bir fincan çayı kaşıkla karıştırın. Yüzeydeki çay yaprakları, "merkezde görünmez bir kütle var" diye değil, sadece **suyun akıntısına kapıldıkları** için döner. İşte galaksinin kolları da o çay yapraklarıdır. Karanlık madde dedikleri şey, aslında sadece **sıvının akıntısıdır** (Sürüklenme / Entrainment).

<div style="width: 100%; height: 350px; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid rgba(200, 0, 255, 0.2); box-shadow: 0 0 20px rgba(200, 0, 255, 0.1); margin-top: 20px; margin-bottom: 20px;">
    <canvas id="galaxy-canvas" style="width: 100%; height: 100%; display: block; background: #070308;"></canvas>
    <div style="position: absolute; top: 10px; right: 10px; color: white; background: rgba(0,0,0,0.5); padding: 5px; font-size:12px; border-radius:4px; text-align:right;">Galaktik Girdap<br>(Makro-Spin Akıntısı)</div>
</div>

<script>
(function() {
    const canvas = document.getElementById('galaxy-canvas');
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
    
    const stars = [];
    for(let i=0; i<300; i++) {
        let r = Math.random() * (Math.max(width,height)/2) + 10;
        stars.push({
            angle: Math.random() * Math.PI * 2,
            radius: r,
            speed: 0.05 + (100 / (r + 50)),
            size: Math.random() * 2 + 0.5,
            color: `hsl(${Math.random()*60 + 200}, 100%, 70%)`
        });
    }
    
    function animate() {
      if(typeof canvas !== "undefined" && !canvas.isConnected) return;
        ctx.fillStyle = 'rgba(7, 3, 8, 0.1)';
        ctx.fillRect(0, 0, width, height);
        
        ctx.beginPath();
        ctx.arc(centerX, centerY, 15, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff';
        ctx.shadowBlur = 30;
        ctx.shadowColor = '#d534eb';
        ctx.fill();
        ctx.shadowBlur = 0;
        
        stars.forEach(s => {
            s.angle += s.speed * 0.2;
            let x = centerX + Math.cos(s.angle) * s.radius;
            let y = centerY + Math.sin(s.angle) * s.radius;
            ctx.fillStyle = s.color;
            ctx.beginPath();
            ctx.arc(x, y, s.size, 0, Math.PI * 2);
            ctx.fill();
        });
        
        requestAnimationFrame(animate);
    }
    animate();
})();
</script>

## Kanıt: Neden Hep "Düz Bir Çizgi"?

İşin en çarpıcı yanı şu: Ölçümlerde, yıldızların hızı merkezden uzaklaştıkça **düşmüyor, neredeyse sabit kalıyor** (bilim bunu "düz dönüş eğrisi" diye adlandırır ve karşısında çaresiz kalır). Newton'un çekim yasasında böyle bir şey imkânsızdır; uzaklaştıkça hız düşmeliydi.

Ama akışkanlar mekaniğini bilen her mühendis bu grafiği tanır: Devasa bir su girdabının dış kolları **tam da bu şekilde**, hızını koruyarak döner. Yani astronomların "evrenin %85'i gizemli madde" diye yıllardır aradığı şey, aslında herhangi bir hidrodinamik ders kitabının ilk sayfalarında yazılıdır. Ortada eksik bir kütle yok; eksik olan tek şey, **uzayın bir sıvı olduğunu kabul etme cesareti.**

Şimdi galaksileri çözdük. Peki bu görünmez güçler tek tek nasıl işliyor? Sonraki bölümde bir gezegeni ya da yıldızı şekillendiren o **beş büyük hidrodinamik gücü** tanıyacağız.


---

## Bu Bölümde Ne Öğrendik?

> [!NOTE]
> - **Eski Fizik:** Galaksilerin dağılmamasını sağlayan, göremediğimiz devasa 'Karanlık Madde' haleleri vardır.
> - **Evrenakı Teorisi:** Karanlık madde yoktur. Galaksilerin dönüşünü sabitleyen şey, içlerinde yüzdükleri Evrenakı sıvısının devasa makro-girdap etkileridir.

> [!TIP]
> Bu bölümün matematiksel ispatlarını ve akademik dildeki detaylı açıklamalarını görmek için **[Akademik Sürüm Kısım 7'ye geçiş yapın](#akademik_07)**.
