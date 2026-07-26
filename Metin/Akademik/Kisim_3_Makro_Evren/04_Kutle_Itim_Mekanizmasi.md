# 3.4 Kütle-İtim (Push-Gravity) Mekanizması

## 3.4.1 Navier-Stokes Formülasyonu ve Kütle-İtim İspatı

Evrenakı'nın Kütle-İtim (Push-Gravity) yaratma yeteneği (Le Sage, 1784) yalnızca felsefi bir çıkarım, laboratuvar analojisi veya zihinsel bir kurgu değil; bilimin en sarsılmaz doğrularından biri olan hidrodinamiğin temel yasalarının matematiksel bir zorunluluğudur. Newton'un (1687) klasik "çekim" (pull) konseptine yepyeni ve mekanik bir perspektif getiren bu ispat, akışkanlar dinamiğini yöneten temel **Navier-Stokes** denklemlerinde gizlidir:

$\rho \left( \frac{\partial \vec{v}}{\partial t} + \vec{v} \cdot \nabla \vec{v} \right) = - \nabla P + \mu \nabla^2 \vec{v}$

Evrenakı, elektromanyetik etkileşimleri ve gezegensel yörüngeleri kesintisiz sürdürebilen ideal ve sürtünmesiz bir ortam (kinematik viskozitesi $\mu \approx 0$) olduğu için bu karmaşık Navier-Stokes denklemi doğrudan klasik **Euler Denklemine** sadeleşir: 

$\rho \left( \frac{\partial \vec{v}}{\partial t} + \vec{v} \cdot \nabla \vec{v} \right) = - \nabla P$

Bu denklemden yola çıkarak, dönen bir serbest girdapta (örneğin Güneşin veya Dünyanın etrafındaki makro Evrenakı akıntısında) merkezkaç kuvveti ile basınç kuvvetinin dengesini (radyal momentum denklemini) yazdığımızda karşımıza çıkan nihai formül şudur:

$\frac{dP}{dr} = \rho \frac{v_\theta^2}{r}$

**Bu formülün fiziksel anlamı devrimseldir:** Basıncın ($P$), dönüş merkezine olan uzaklığa ($r$) göre değişimi ($dP/dr$) **kesinlikle pozitiftir**. Matematiksel meali şudur: **Merkeze (kütleye) yaklaştıkça ($r$ küçüldükçe) hız artar ve statik basınç mecburen düşer**. Dışarı doğru ($r$ arttıkça) basınç artar. 

Newton elmanın yere düşmesini "Dünya elmayı çekiyor" olarak tanımlamıştır ve fizik asırlardır bu yaklaşımla yetinmiştir. Oysa elmayı Dünyanın yüzeyine doğru "iten" kuvvet, Dünyayı oluşturan trilyonlarca atomun (çekirdek ve elektronların) her birinin kendi etrafında dönerek (mikro-spin) yarattığı sayısız mikro-girdapların kümülatif olarak birleşmesiyle oluşan devasa basınç gradyanıdır ( $-\nabla P$ ). Uzayın derinliklerindeki yüksek statik Evrenakı (vakum) basıncı, gezegen yüzeyindeki bu devasa düşük basınç havzasına doğru kesintisiz bir akış (vektör) yaratır ve elmayı (yahut Ay'ı) o merkeze doğru kesintisizce **iter**. Böylece Kütle-İtim (Push-Gravity) mekanizması, Euler denklemleri üzerinden matematiksel kesinliğe kavuşur.

## 3.4.2 Kütleçekimine (Push-Gravity) Doğru İlerleyen Görsel Analoji

<div style="background: #121212; padding: 20px; border-radius: 12px; border: 1px solid #404040; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; text-align: center;">
  <h3 style="margin-top: 0; margin-bottom: 20px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon 3.4.1: Newton'un Cansız Çekimi (Pull) ve Evrenakı'nın Akışkan İtimi (Push) Karşılaştırması</h3>
  <svg viewBox="0 0 800 410" width="100%" style="max-width: 800px; background: #050505; border: 1px solid #333; border-radius: 8px;">
<defs>
<radialGradient id="vortexPressure" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.9" />
  <stop offset="100%" stop-color="#020617" stop-opacity="1" />
</radialGradient>
<marker id="arrowRed" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
  <path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444" />
</marker>
<marker id="arrowGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
  <path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981" />
</marker>
<style>
  @keyframes fallIn {
    0% { transform: translate(0px, 0px); opacity: 0; }
    10% { opacity: 1; }
    80% { transform: translate(-30px, 30px); opacity: 1; }
    100% { transform: translate(-30px, 30px); opacity: 0; }
  }
  .falling-mass {
    animation: fallIn 3s ease-in infinite;
  }
  @keyframes spinClockwise {
    100% { transform: rotate(360deg); }
  }
  .spin-core {
    animation: spinClockwise 2s linear infinite;
  }
  .spin-vortex {
    animation: spinClockwise 10s linear infinite;
  }
</style>
</defs>
<!-- Divider -->
<line x1="400" y1="0" x2="400" y2="450" stroke="#4b5563" stroke-width="2" stroke-dasharray="10 10" opacity="0.5" />
<!-- LEFT SIDE: NEWTON (Pull Gravity) -->
<text x="200" y="40" fill="#9ca3af" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Animasyon 3.4.1 (B): Newton Modeli</text>
<text x="200" y="60" fill="#ef4444" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Boş Uzayda Cansız "Çekim" (Pull)</text>
<g transform="translate(200, 240)">
  <!-- Empty space -->
  <circle cx="0" cy="0" r="140" fill="none" stroke="#1f2937" stroke-width="1" stroke-dasharray="5 5" />
  <!-- Planet -->
  <circle cx="0" cy="0" r="30" fill="#4b5563" />
  <text x="0" y="5" fill="#ffffff" font-family="sans-serif" font-size="12" text-anchor="middle">M</text>
  <!-- Pure Mathematical Formula (No Physical Agent) -->
  <text x="-90" y="-80" fill="#ef4444" font-family="serif" font-size="18" font-style="italic" text-anchor="middle">F = G</text>
  <text x="-35" y="-88" fill="#ef4444" font-family="serif" font-size="14" font-style="italic" text-anchor="middle">M · m</text>
  <line x1="-60" y1="-82" x2="-10" y2="-82" stroke="#ef4444" stroke-width="1.5" />
  <text x="-35" y="-68" fill="#ef4444" font-family="serif" font-size="14" font-style="italic" text-anchor="middle">r²</text>
  <text x="-50" y="-45" fill="#9ca3af" font-family="sans-serif" font-size="11" text-anchor="middle">(Mekanizma Yok)</text>
  <!-- Falling Mass -->
  <g class="falling-mass">
    <circle cx="80" cy="-80" r="8" fill="#fbbf24" />
    <text x="100" y="-80" fill="#fbbf24" font-family="sans-serif" font-size="12">m</text>
  </g>
  <text x="0" y="160" fill="#6b7280" font-family="sans-serif" font-size="12" text-anchor="middle">Aktör: Çekici Kütle (M)</text>
</g>
<!-- RIGHT SIDE: EVRENAKI (Push Gravity) -->
<text x="600" y="40" fill="#9ca3af" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Animasyon 3.4.1 (A): Evrenakı Modeli</text>
<text x="600" y="60" fill="#10b981" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Akışkan Girdabında Dinamik "İtim" (Push)</text>
<g transform="translate(600, 240)">
  <!-- Radial Pressure Background -->
  <circle cx="0" cy="0" r="140" fill="url(#vortexPressure)" />
  <!-- Vortex Spirals -->
  <g class="spin-vortex" stroke="#60a5fa" stroke-width="2" fill="none" opacity="0.5">
    <path d="M 0 0 C 40 -40, 80 -10, 120 -60" />
    <path d="M 0 0 C 40 40, 80 10, 120 60" />
    <path d="M 0 0 C -40 40, -80 10, -120 60" />
    <path d="M 0 0 C -40 -40, -80 -10, -120 -60" />
  </g>
  <!-- Central Dynamo (Core Spin) -->
  <circle cx="0" cy="0" r="30" fill="#3b82f6" />
  <g class="spin-core">
    <circle cx="0" cy="0" r="15" fill="#fcd34d" />
    <circle cx="10" cy="0" r="3" fill="#b45309" />
    <circle cx="-10" cy="0" r="3" fill="#b45309" />
  </g>
  <text x="0" y="45" fill="#60a5fa" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">SPIN</text>
  <!-- Physical Fluid Formula (Euler / Navier-Stokes) -->
  <text x="0" y="-100" fill="#10b981" font-family="serif" font-size="18" font-style="italic" text-anchor="middle">F = -∇P</text>
  <text x="-15" y="-78" fill="#10b981" font-family="serif" font-size="14" font-style="italic" text-anchor="middle">∇P = ρ</text>
  <text x="25" y="-86" fill="#10b981" font-family="serif" font-size="14" font-style="italic" text-anchor="middle">v²</text>
  <line x1="15" y1="-80" x2="35" y2="-80" stroke="#10b981" stroke-width="1.5" />
  <text x="25" y="-66" fill="#10b981" font-family="serif" font-size="14" font-style="italic" text-anchor="middle">r</text>
  <!-- PUSH Forces (Pressure Gradient) -->
  <line x1="-120" y1="-120" x2="-50" y2="-50" stroke="#10b981" stroke-width="3" marker-end="url(#arrowGreen)" />
  <line x1="120" y1="-120" x2="50" y2="-50" stroke="#10b981" stroke-width="3" marker-end="url(#arrowGreen)" />
  <line x1="-120" y1="120" x2="-50" y2="50" stroke="#10b981" stroke-width="3" marker-end="url(#arrowGreen)" />
  <line x1="120" y1="120" x2="50" y2="50" stroke="#10b981" stroke-width="3" marker-end="url(#arrowGreen)" />
  <text x="-130" y="-130" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">Yüksek P</text>
  <text x="110" y="-130" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">Yüksek P</text>
  <!-- Falling Mass -->
  <g class="falling-mass">
    <circle cx="80" cy="-80" r="8" fill="#fbbf24" />
    <text x="100" y="-80" fill="#fbbf24" font-family="sans-serif" font-size="12">m</text>
  </g>
  <text x="0" y="160" fill="#10b981" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Aktör: ∇P (Basınç İtimi)</text>
</g>
</svg>
</div>

Tanımladığımız akışkan ilkeleri (Navier-Stokes / Euler) ışığında, dönen bir ortamın (vortex) yarattığı radyal basınç gradyanı Animasyon 3.4.1 (A)'da iki boyutlu bir kesit olarak görselleştirilmiştir. 

Merkezden dışarı gidildikçe rengin koyulaşması, merkeze uzak ($r$ büyük) dış uzayda Evrenakı (Aether) basıncının yüksek olduğunu sembolize etmektedir. Yüksek basınçtan (Koyu renk), düşük basınç olan girdap merkezine (Açık renk) doğru yönelen kırmızı oklar ise bizzat "Net İtim Kuvveti" ($\nabla P$) vektörleridir. Akışkan okyanusu içerisindeki herhangi bir kütleli nesne, bu vektörlerin yönünde kaçınılmaz olarak merkeze doğru bastırılacaktır.

Bu noktada, dönen Evrenakı girdabında sadece "basınç değişiminin" yarattığı bu "merkeze yığılma" mekanizmasının, klasik Newton fiziğindeki "Kütleçekimi" fenomenine (Animasyon 3.4.1 (B)'deki merkeze çekilen oklara) yapısal ve vektörel olarak ne kadar kusursuz bir biçimde oturduğuna dikkat edilmelidir. Formül olarak, yavaş dönüşlü Güneş Sistemi gibi lokal girdaplarda bu akışkan vektörleri Newton'un meşhur Ters Kare ($1/r^2$) ampirik davranışını mükemmel şekilde dengeler. Ancak Evrenakı asıl devrimini, sarmal galaksiler gibi devasa kasırgalarda Newton'un $1/r^2$ formülü yetersiz kaldığında gösterir. Karanlık madde varsaymak yerine, doğrudan diferansiyel denklemler ve logaritmik basınç kuyularıyla sarsılmaz bir Evrenakı dinamiği sunar (Matematiksel ispatları Bölüm 4.2'de detaylandırılmıştır).

Genel Görelilik teorisi bu merkeze çekilme hissini uzay-zamanın geometrik bükülmesi ile izah eder; Newton mekaniği ise kütlelerin birbirini doğrudan çekmesi (uzaktan etki) prensibine dayanır. Ancak Animasyon 3.4.1 (A)'daki Kütle-İtim senaryosunun merkezinde, temas gerektirmeyen hiçbir "çekici kütle ajanı"na ihtiyaç duyulmaz. Sadece ve sadece akışkanın (Evrenakı'nın) dönüşü (girdap / spin) ve onun yarattığı reel basınç farkı vardır. 

Dış gözlemci, gezegene (Dünyaya) doğru düşen göktaşlarına ve elmalara bakarak *"Dünya, kütlesi sayesinde nesneleri kendine çekiyor"* sonucuna varır. Oysa gerçeğinde Dünya'yı saran görünmez Evrenakı girdabı, yarattığı düşük basınç farkıyla nesneleri Dünya'nın yüzeyine (merkezine) doğru uzaydan bastırmakta, itmektedir. Dünya (Kütle), sadece bu akışkan anaforunun tam ortasındaki tahliye deliğidir.

## 3.4.3 Kütlenin Pasifliği ve Dönüşün (Spin) Gücü: Venüs ve Merkür Kanıtı

Klasik Newton ve Einstein mekanikleri, kütleyi ($M$) yerçekimini bizzat üreten, uzayı aktif olarak büken mutlak bir "birincil etken" olarak kabul ederler. Evrenakı (Plenum — ortam doluluğu ilkesi, bkz. 1. Postülat; Descartes, 1644) modelinde ise **kütle, tek başına durduğunda tamamen pasif bir unsurdur.**

Kütleyi aktif kılan, uzay dokusunu etkileyen ve o bildiğimiz çekimsel/itimsel etkilere sebep olan yegane unsur kütlenin kendisi değil; **Dönme Hareketi (Spin)**'dir. Evrenakı teorisi, gravitasyonu anlamak için yüzeydeki yerçekimi ile yörüngesel çekim arasında çok kritik bir hidrodinamik ayrım yapar:

1. **Mikroskobik Spin (Merkezcil Kuvvetler / Yüzey Yerçekimi):** Bir gezegenin kütlesini oluşturan trilyonlarca atomun kendi içsel dönüşlerinden (elektron ve çekirdek mikro-girdaplarından) doğan ve kümülatif olarak (toplamda) birleşerek cismin yüzeyine doğru net bir düşük basınç gradyanı yaratan "Lokal Kütle-İtim" kuvvetidir. Kütle (atomlar) var olduğu sürece o küçük atomik spinler daima var olacağından, yüzey yerçekimi (elmanın yere düşmesi, insanların havada uçmaması) **her gezegende daima mevcuttur**.

2. **Makroskobik Spin (Eksenel Kuvvetler / Uydu Yörüngeleri):** Gezegenin kütlesel bir bütün olarak "kendi ekseni etrafında dönmesiyle (Gezegen Spini)" oluşan, yüzeyin çok ötesine, binlerce kilometre uzaya uzanan o devasa **makro-girdap**'tır. Uyduları (Ay'ı vs.) uzayın derinliğinde yörüngede tutan ve onları sürükleyen asıl mekanizma kütle büyüklüğü değil, bu makroskobik dönüşün (spinin) oluşturduğu "Evrenakı Akışkan Sürüklenmesi"dir (Entrainment).

*Altın Kural: Makroskobik dönme hareketi (gezegensel spin) yoksa, makro girdap yoktur. Makro girdap yoksa, o gezegenin uzayın derinliklerinden uydu yakalama ve onu yörüngesinde tutma yeteneği de bulunmaz.*

**Sarsıcı Öngörü ve Yanlışlanabilirlik (Falsifiability) Kriteri:**
Evrenakı modelinin bu akışkan prensibinden, yerleşik gök mekaniği modellerini temelden sarsacak denli güçlü ve test edilebilir bir astronomik sonuç çıkar: Kendi ekseni etrafındaki dönme hızı sıfıra yakın olan gezegenler, devasa kütlelere ve yüzey yerçekimlerine sahip olsalar bile, çevrelerinde (uzay boşluğunda) uyduları yörüngede sürükleyecek o makro Evrenakı girdabını oluşturamazlar. 

Gerçekten de Güneş Sistemi'ne baktığımızda, kendi ekseni etrafında dönme hızları son derece yavaş olan (hatta Venüs o kadar yavaştır ki kendi ekseni etrafındaki bir günü, Güneş etrafındaki yılından daha uzundur) **Merkür ve Venüs'ün hiçbir uydusu bulunmamaktadır.**

Modern astronomi, klasik kütleçekim teorilerindeki bu yapısal çelişkiyi; Güneş'e yakınlık, radyasyon basıncı, "Hill Küresi (Hill Sphere)" darlığı veya gel-git (tidal stripping) etkileri gibi bir dizi karmaşık ve ikincil argümanla açıklamaya çalışır. Oysa Jüpiter'in uydusu olan Ganymede veya Satürn'ün uydusu Titan'ın çapları Merkür'den bile büyüktür; yörüngeleri harika şekilde stabildir. Ancak Merkür'den katbekat daha devasa bir kütleye sahip olan Venüs'ün bir gramlık bile uydusu yoktur. Doğrudan ve gözlemsel sebep, gezegenin kütle hacmi değil; o yörünge girdabını var edecek olan **Makroskobik Dönüşün (Spin) yokluğudur.** Güneş'e yakınlığın gerçek rolü ise klasik teorinin bu ikincil argümanlarında değil, bir sonraki başlıkta ele alınacak **girdap rekabetinde** saklıdır: bu iki gezegenin dönüşünü bastıran (kilitleyen) şey, bizzat içinde yüzdükleri dev Güneş girdabıdır.

Bu bağlamda Evrenakı Teorisi, bilimsel felsefenin ve epistemolojinin kalbi olan Karl Popper'ın "Yanlışlanabilirlik (Falsifiability)" ilkesi gereği ortaya son derece iddialı ve açık bir meydan okuma (bahis) koyar: **Şayet evrenin herhangi bir yerinde, kendi ekseni etrafında dönmeyen (spini sıfır olan) makroskobik bir gök cisminin etrafında, kalıcı bir yörüngeye oturmuş bir uydu tespit edilirse, Evrenakı (Kütle-İtim) Teorisi'nin tamamen çöktüğünü, yanlış olduğunu kayıtsız şartsız kabul ederiz.**

## 3.4.4 Makro-Girdabın Gerçek Motoru: Dördüncü Boyut Dönüşleri ve Girdap Rekabeti

Venüs ve Merkür örneğinde makroskobik dönüşün (spinin) gezegensel yörüngeler ve uydular için şart olduğunu belirttik. Ancak bu noktada haklı bir fiziksel soru akla gelir: *Dünya'nın kabuğu kendi etrafında 24 saatte (nispeten yavaş bir hızla) dönmektedir. Sadece kabuğun bu yavaş dönüşü, Ay'ı 380.000 kilometre uzaktan yakalayıp savuracak kadar devasa ve güçlü bir Evrenakı makro-girdabı yaratmaya yeter mi?*

Cevap kesinlikle **Hayır'dır** — ve bu cevap, teorinin en kritik ayrımlarından birini zorunlu kılar: Evrenakı makro-girdabının motoru, kütlenin gözlemlenen **mekanik devri değildir**. Bu motor mekanik devirde aransaydı gözlemler yolu kapatırdı: sismolojik veriler Dünya'nın çekirdeğinin kabuğundan kayda değer ölçüde hızlı dönmediğini göstermiştir; Güneş'in çekirdeği bile yüzeyinden yalnızca dört kat hızlıdır ve bu dahi gereken girdap devrinin çok altında kalır (nicel döküm için Bkz. 3.9.4.1 ve 3.9.5).

Girdabın gerçek motoru, kütleyi oluşturan nükleonların **dördüncü boyuttan gelen çift dönüş deşarjıdır** (Bkz. 3.1.3-B ve 3.2.2). Aynı mikro-motorlar hem kütleyi hem de çevresindeki akışkanı döndürür; ancak rijit ve sürtünmeli bir kafes olan kütle yavaş dönerken, sürtünmesiz Evrenakı kat kat yüksek devirle döner (mekanizmanın tam işlenişi için Bkz. 3.9.6). Bu yüzden bir gezegenin görünen spini motorun kendisi değil, motorun o ortamda bulabildiği ifadenin **göstergesidir**.

**Girdap Rekabeti ve Kilitlenme Hiyerarşisi:** Peki dördüncü boyut motoru her kütlede işlediği hâlde Venüs ve Merkür'ün makro-girdabı neden yoktur? Çünkü hiçbir gezegen girdabını boş bir ortamda kurmaz; hepsi Güneş'in dev girdabının **içinde** döner ve kendi dönüşünü bu baskın akıntıya karşı ifade etmek zorundadır:

* **Merkür:** Güneş'e en yakın gezegen olarak tümüyle Güneş girdabının kontrolüne girmiştir; kendi dönüş ifadesi neredeyse bütünüyle bastırılmıştır.
* **Venüs (Kanıtın Sağlaması):** Dördüncü boyut dönüşleri Venüs'te de eksiksiz işler; ancak dönüşünün hemen önünde Güneş'in devasa girdabı durmaktadır. Venüs'ün dönüşü bu girdabı döndüremeyeceği için kendi üzerine geri teper ve gezegen **ters yönde (retrograd) ve aşırı yavaş** döner. Klasik bilimin "kilitlenme" adını verdiği olgu, teoride bu girdap rekabetinin geri tepmesidir. Bastırılmışlık çekirdeğin dinamo etkinliğine de yansır ve bunun jeofizik imzası nettir: Venüs'ün küresel bir manyetik alanı **hiç yoktur** (dinamosu ölüdür); Merkür ise demir açısından zengin, kütlesine oranla devasa bir çekirdeğe sahip olmasına rağmen — ki bu, klasik dinamo teorisine göre güçlü bir alan üretmesi gerektiği anlamına gelir — yalnızca Dünya'nınkinin **yaklaşık yüzde biri** kadar, beklenenin çok altında cılız bir alana sahiptir. Her iki gezegenin de çekirdek dinamiklerindeki bu bastırılmışlık, uydusuzluğun sebebi değil, aynı girdap kilitlenmesinin ikinci bir gözlemsel **belirtisidir**.
* **Dünya:** Güneş'ten yeterince uzak olduğu için çok daha serbesttir; 24 saatlik devri, dördüncü boyut dönüşlerinin Güneş girdabı ortamında izin verdiği dengenin ifadesidir ve ürettiği makro-girdap Ay'ı yörüngesinde taşımaya yeter. Klasik teorinin, Dünya'nın Mars'a kıyasla (kütle oranı gözetildiğinde) yavaş dönüşünü Ay'ın frenlemesine bağlaması ikincil bir okumadır; dönüş hızını asıl belirleyen bu denge yasasıdır.
* **Jüpiter ve Satürn:** Hem devasa kütleli (mikro-motor sayısı yüksek) hem de Güneş'ten uzak (rekabet zayıf) oldukları için dördüncü boyut motorları neredeyse tam ifadeyle çalışır: etraflarında onlarca uyduyu (bazen retrograt yörüngelere rağmen) hizaya sokan ve materyalleri ezerek incecik halkalar yaratan (Bkz. Bölüm 3.10) inanılmaz güçlü makro-vorteksler doğar.
* **Güneş:** Sistemin baskın motoru olarak, Güneş Sistemi'nin sınırlarına kadar uzanan milyarlarca kilometrelik "Kepler girdabını" üretir.

**Ortak Yön İmzası:** Bu rekabet modeli, klasik astronominin açısal momentum dağılımı üzerinden boğuştuğu bir bilmeceyi tek hamlede çözer: Güneş'in ve gezegenlerin tamamının aynı yönde dönmesinin sebebi, Güneş girdabının yalnızca kendisiyle **aynı yönde hizalanmış** dördüncü boyut dönüş ifadelerine izin vermesidir. Venüs'ün retrograd dönüşü bu kuralın istisnası değil, kilitlenmenin geri tepmesi olarak kuralın en güçlü kanıtıdır.

**Sistem Açısal Momentumu ve Kütle–Dönüş İlişkisi.** Bu tabloyu en temelden okumanın yolu, tek tek torklardan değil, **sistemin korunan toplam açısal momentumundan** başlamaktır. Tek bir dördüncü boyut kaynağı (Bkz. 3.1), sisteme tek bir toplam açısal momentum $\vec{L}_{\text{sis}} = \sum_i \vec{L}_i$ yükler; bu vektör korunumlu ve tektir, değişmez düzlemi (invariable plane) ve ortak dönüş yönünü tanımlar. Ortak yön bir tesadüf değil, **bu tek korunan toplamın yönüdür**; kaynak tek olduğu için yön de tektir. Retrograd/eğik cisimler (Venüs, Uranüs) bu toplamın işaretini çevirmeyen azınlık bileşenlerdir. Nitekim klasik kuramın "kayıp açısal momentum" bilmecesi (Güneş kütlenin %99,8'ini taşırken toplam açısal momentumun yalnızca ~%2-3'ünü barındırır; Bkz. 3.1 giriş) bu çerçevede bir zaaf değil, doğrudan öngörüdür: dördüncü boyut motoru tüm sistemi yükler, momentum kütleyle birlikte merkeze yığılmaz.

Motorun her cismi kütlesiyle (mikro-motor sayısıyla) orantılı yüklemesi, gözlemlenebilir bir **kütle–dönüş** eğilimi bırakır. Uranüs hariç serbest gezegenler (Mars → Jüpiter), hem dönüş hızı hem de dönme açısal momentumu ile kütle arasında log-log ölçekte neredeyse kusursuz birer doğru çizer: ekvatoral hız $v_{\text{ekv}} \propto M^{0{,}54}$ ($R^2=0{,}98$), dönme açısal momentumu ise $L_{\text{spin}} = \tfrac{2}{5}MR\,\omega \propto M^{1{,}94}$ ($R^2=1{,}00$) ile — yani kütlenin neredeyse **karesiyle** — çok daha dik büyür. Bu, "dönüş kütleyle orantılıdır" beklentisinin, momentum düzeyinde beklenenden bile güçlü biçimde doğrulanmasıdır. Bastırılmış iç gezegenler Merkür ve Venüs ise her iki grafikte de doğrunun çok altında kalır — girdap rekabetiyle dönüşleri baskılandığı için (Şekil 3.4.1).

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/kutle_donus_ikili_dark.png" alt="Kütle-Dönüş ve Açısal Momentum İlişkisi (Karanlık Mod, İki Panel)" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 3.4.1: Kütle ile (a) ekvatoral dönüş hızı ve (b) dönme açısal momentumu ilişkisi (Uranüs hariç). Serbest/prograd gezegenler (Mars, Dünya, Neptün, Satürn, Jüpiter) her iki panelde tek bir doğruya oturur — solda $v_{\text{ekv}} \propto M^{0{,}54}$ ($R^2=0{,}98$), sağda $L_{\text{spin}} \propto M^{1{,}94}$ ($R^2=1{,}00$). Girdap rekabetiyle bastırılmış Merkür ve Venüs (kırmızı) iki panelde de doğrunun çok altındadır. Kabarcık boyutu uydu sayısıyla orantılıdır. Biçimsel türetim ve sistem açısal momentumu çerçevesi için bkz. `claude4b-aynıdonus.md`.</em></p>
</div>

**Bastırılmanın Nicelleştirilmesi ve Kilit Frekansları.** Serbest doğru Merkür ve Venüs kütlelerine ekstrapole edildiğinde, girdap rekabetinin yuttuğu miktar sayısallaşır: Merkür serbest kalsaydı **~33 saatte**, Venüs **~16 saatte** (Dünya benzeri) dönecekti; Güneş girdabı bu momentumun sırasıyla **%97,7'sini** ve **%100,3'ünü** (tam yutma + işaret dönmesi) soğurmuştur. Kavrama derecesi $g \equiv 1 - L_{\text{gözlenen}}/L_{\text{serbest}}$ dört iç gezegene uygulandığında dik bir kavrama klifi belirir: $g(R) = 1/(1+(R/R_c)^p)$ ile $R_c \approx 1{,}0$ AU — ve bu klif Dünya'nın 24 saatini kendiliğinden üretir ($g_{\oplus}=0{,}39$: serbest ~14,5 saatlik ifadenin %61'i). Daha da önemlisi, kavranmış cisimlerin **kalıntı** dönüşleri rastgele değildir; tümü yerel girdap frekansı $\Omega_{\text{yör}}$ ölçeğindedir: Merkür tam $+\tfrac{3}{2}\Omega_{\text{yör}}$ (rezonans kilidi), Venüs $-0{,}92\,\Omega_{\text{yör}}$ (retrograd kayma), gelgit-kilitli uydular $+1\,\Omega_{\text{yör}}$ (tam senkron — Ay). Serbest cisimlerde ise $|\omega|/\Omega_{\text{yör}} \sim 10^2$–$10^5$'tir; bu boyutsuz oran, serbest ifade ile girdap kilidini ayıran keskin bir tanı parametresidir (Şekil 3.4.2). Tablo tek denklemde toplanır:

$$\omega_{\text{gözlenen}}(M,R) \;=\; \big[1-g(R)\big]\,\omega_{\text{serbest}}(M) \;+\; g(R)\,q\,\Omega_{\text{yör}}(R), \qquad q \in \{+\tfrac{3}{2},\ +1,\ \approx-1\}.$$

Motorun ifadesi tam yutulduğunda cisim durmaz; girdabın **yerel ritmine** oturur. İlk iki kilit modu ($+1$ ve $+\tfrac{3}{2}$) ayrıca serbest parametre de değildir: kavrama klifi çok dik olduğundan pençe fiilen **günberide** kavrar ve kalıntı, günberideki girdap ritmine oturur:

$$\frac{\omega_{\text{kilit}}}{\Omega_{\text{yör}}} \;=\; \frac{\sqrt{1+e}}{(1-e)^{3/2}} \;\longrightarrow\; \text{en yakın kararlı oran}.$$

Ay için ($e=0{,}055$) bu oran $1{,}12 \to 1{:}1$; Merkür için ($e=0{,}206$) $1{,}55 \to 3{:}2$ verir; iki mod arasındaki eşik $e \approx 0{,}125$'tir. Rezonans yakalanmasının klasik çözümlemesi için krş. Goldreich & Peale (1966); fark şudur: klasik çözümleme yakalanmayı *olasılıksal* işlerken, teorinin dik-klifli günberi-kavraması onu *deterministik* kılar — buradan ayırt edici bir öngörü doğar: **ötegezegen sistemlerinde $e \approx 0{,}2$ civarında kilitlenmiş cisimler daima 3:2'de bulunmalıdır** (bazen 1:1, bazen 3:2 değil). **Venüs'ün ters dönüşü: yelken kanalı.** Retrograd kesir, kavrama denklemine eksik kalan son değişkenin eklenmesiyle çözülür: cismin Evrenakı ile **etkileşim kesiti** yalnızca kayaç yarıçapı değildir — kalın bir atmosfer, ayrı bir kuplaj kanalı ("yelken", $\sigma$) açar. Doygun rejimde kalıntı kilit, iki kanalın dengesinden seçilir: **gövde (asimetri) kanalı** kalıntıyı günberi ritmine çekerken ($\sigma \approx 0$: Merkür 3:2, Ay 1:1), **termal yelken kanalı** — Güneş'in gündüz tarafında ısıttığı atmosferin Evrenakı deplasmanının oluşturduğu Güneş-kilitli asimetrik tutamaç — kalıntıyı senkrondan uzaklaştırır. İki dürüstlük kaydı zorunludur: yelken bastırılmayı açıklamaz (yelkensiz Merkür de %97,7 bastırılmıştır; yelken yalnızca **kilit modunu** seçer) ve tekdüze bir yelkene saf kesme $+\tfrac14\Omega$ verir — ters çeviren, yelkenin termal asimetrisidir. $\sigma\Gamma/k_g > 1$ olan Venüs'te çözüm senkron daldan kaçıp retrograd dalda dengelenir ($\omega^\ast \approx -0{,}92\,\Omega$). Mekanizmanın iki gözlemsel çapası vardır: **süper-rotasyon** (Venüs atmosferi gövdeden ~60 kat hızlı *ileri* döner — girdap yelkene ileri momentum yüklerken tepki torkunun gövdeyi geri itmesinin, yani momentum takasının doğrudan imzası) ve **Titan kontrolü** (kalın atmosferli ama 1:1 kilitli: Güneş ısıtması zayıf, Satürn kavraması güçlü — flip koşulu sağlanmaz). Yapı, standart mekaniğin yerçekimsel-gelgit ↔ atmosferik-termal-gelgit dengesinin (Gold & Soter, 1969; Correia & Laskar, 2001) hidrodinamik yeniden okumasıdır; buradan ötegezegen öngörüsü de doğar: kavrama bölgesindeki sıcak, kalın atmosferli gezegenler retrograd/asenkron durakları tercih etmeli, retrograd kilitli her yelkenli cisim süper-rotasyon taşımalıdır.

Denge, sabit-$\Gamma$ yaklaşımında kapalı biçimde çözülür ve kendiliğinden kararlıdır:

$$\frac{\omega^\ast}{\Omega_{\text{yör}}} \;=\; q_{\text{peri}}(e) \;-\; \frac{\sigma\Gamma}{k_g}.$$

Venüs'ün ölçülen kilidi bu ifadeyi kalibre eder: $e=0{,}007 \Rightarrow q_{\text{peri}}=1{,}01$ ile $\sigma\Gamma/k_g = 1{,}01-(-0{,}92) = 1{,}93 \approx 2$ — yani **Venüs'te termal yelken kanalı, gövde kanalından yaklaşık iki kat güçlüdür** ve $-0{,}92$'nin görünürdeki tuhaflığı $q_{\text{peri}}-2$'nin sıradan aritmetiğine iner. Aynı ifade parametresiz olarak diğer cisimleri de tarar: Merkür ve Ay'da $\sigma=0$ (kilit $= q_{\text{peri}}$: 3:2 ve 1:1 ✓), Titan ve Dünya'da $\sigma\Gamma/k_g \ll 1$ (prograd ✓). Modelin üst dalında simetrik ikinci bir durak ($q_{\text{peri}} + \sigma\Gamma/k_g$) bulunması, Correia–Laskar'ın "çoklu son durum" yapısının bu çerçevede kendiliğinden üremesi demektir.

*(Dürüst kayıt: klif uyumu dört nokta / iki parametre ile betimleyicidir; Venüs satırındaki $\sigma\Gamma/k_g \approx 2$ oranı ölçümden kalibre edilmiştir, bağımsız türetilmemiştir — tabloda parametresiz olan diğer dört cisimdir. Açık kalan tek iş, bu oranın atmosfer kütlesi ve termal genlikten ilk-ilke hesabıdır; nicel çözümlemenin tamamı için bkz. `claude4b-aynıdonus.md` §6-B.)*

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/kilitlenme_grafik_dark.png" alt="Bastırılma Miktarı ve Kalıntı Kilit Frekansları (Karanlık Mod, İki Panel)" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 3.4.2: Güneş girdabının yuttuğu dönüş. (a) Serbest doğru Merkür ve Venüs kütlelerine uzatılmış: altın halkalar "olması gereken" momentumu, oklar girdap rekabetinin soğurduğu miktarı gösterir (Merkür: ~33 saat → 58,6 gün; Venüs: ~16 saat → 243 gün, ters). (b) $|\omega_{\text{spin}}|/\Omega_{\text{yör}}$ tanı parametresi: serbest gezegenler $10^2$–$10^5$ bandında, kavranmış Merkür ($+1{,}50\,\Omega$) ve Venüs ($-0{,}92\,\Omega$) tam girdap-kilidi bandındadır; altın kesikli çizgi $R_c \approx 1$ AU kavrama yarıçapını gösterir.</em></p>
</div>

### Animasyon 3.4.2: Kavrama ve Kilitlenme Laboratuvarı

Aşağıdaki etkileşimli laboratuvar, kavrama formülünü ($\omega = (1-g)\,\omega_{\text{serbest}} + g\,q\,\Omega_{\text{yör}}$) serbest hesaplamayla canlandırır: merkez kütleyi, gezegen kütlesini, ortalama uzaklığı ve **yörünge basıklığını (e)** değiştirerek kavrama yarıçapının ($R_c$, altın kesikli çember) nasıl kaydığını ve gezegenin dönüşünün nerede serbest kaldığını, nerede girdaba kilitlendiğini gözlemleyebilirsiniz. Kilit modu $q$ burada bir seçim değildir: kavrama en çok günberide etkidiğinden, kalıntı kilit günberi ritmine oturur ve **basıklıktan hesaplanır** ($\sqrt{1+e}/(1-e)^{3/2}$, en yakın kararlı orana).

**İzlenmesi gerekenler:**

1. **Klifi geçin:** Uzaklık kaydırıcısını 1,5 AU'dan 0,5 AU'ya doğru yavaşça çekin. Altın çemberin ($R_c$) dışında gezegen kendi hızlı dönüşünü sürdürür (SERBEST İFADE, mavi); çemberi geçer geçmez dönüş çöker ve girdabın ritmine kilitlenir (GİRDAP KİLİDİ, kırmızı) — geçiş bandının ne kadar dar (klif gibi) olduğuna dikkat edin.
2. **Merkür'ü basıklıktan üretin:** Uzaklığı 0,39 AU'ya getirip basıklığı e=0,205'e çekin: kilit modu panelde kendiliğinden **"+3/2Ω (günberi ritmi 1,55Ω → hesaplandı)"** olur ve gözlenen dönüş ~59 gün çıkar (gerçek Merkür: 58,6 gün, e=0,206). Sonra e'yi 0,12'nin altına indirin — kilit **1:1'e atlar**: Ay'ın senkron kilidi, aynı hesabın düşük-basıklık ucudur. Yani iki kilit modu da düğmeyle seçilmez, yörünge geometrisinden türetilir.
3. **Venüs'ü deneyin (açık iş):** 0,72 AU'da "Venüs geri tepmesi (yoğun atmosfer)" anahtarını açın: ~247 gün TERS çıkar (gerçek: 243 gün, ters). Bu tek girdi türetilmemiştir ve ekranda da dürüstçe "açık iş" olarak etiketlenmiştir.
4. **Merkez kütleyi büyütün:** Yıldız kütlesi arttıkça $R_c$ çemberinin dışa doğru büyüdüğünü izleyin — daha ağır yıldız, daha geniş bir kavrama bölgesi demektir. Gezegen kütlesini büyütmek serbest dönüşü hızlandırır ($T_{\text{serbest}} \propto m^{-0{,}28}$) ama bu modelde kilidi geciktirmez (hacimsel kuplaj varsayımı; bkz. `claude4b-aynıdonus.md` §5). Basıklığı artırmak ise günberiyi içeri çeker ($a(1-e)$) — dıştaki bir gezegen bile yeterince basık yörüngeyle pençeye yakalanabilir.

<iframe src="Simulasyon/kavrama_kilitlenme_sim.html" width="100%" frameborder="0" style="height: 720px; border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 8px; margin-top: 10px; margin-bottom: 30px;"></iframe>

Evrenakı akışkanında kütleçekim yörüngelerini var eden şey salt "kütle" değildir; kütlenin dördüncü boyut motorlarının, içinde bulunduğu ortam girdabı karşısında bulabildiği **serbest dönüş ifadesidir**.

## 3.4.5 Plenum Direncinin Çözümü (Esir Rüzgarı Yanılgısı ve Bağıl Hız)

Sürekli (continuum) bir Evrenakı'nın varlığına, yani uzayın boş değil dolu olduğuna getirilebilecek en klasik ve haklı görünümlü itiraz şudur: *"Eğer uzay yoğun bir akışkanla (sıvımsı bir şeyle) doluysa ve Dünya bu ortamın içinde saniyede 30 km hızla ilerliyorsa, muazzam bir hidrodinamik sürtünmeye (drag) maruz kalıp hızla yavaşlaması ve zamanla Güneş'e sarmal çizerek düşmesi gerekmez mi?"*

Bu itiraz, klasik mekaniğin sınırlarını bilmemekten ve eski 19. Yüzyıl "Statik Aether" modellerinin hatalı kurgusundan kaynaklanır.

Akışkanlar mekaniğinde havanın veya suyun bir cisme uyguladığı direnç yani Sürüklenme (Drag) kuvveti ($F_d$), her zaman cisim ile akışkan arasındaki **bağıl hıza (relative velocity - $v_{bağıl}$)** dayanır. Formülü şöyledir: $F_d \propto \rho \cdot v_{bağıl}^2$

19. Yüzyıl esir (aether) modellerinin M&M (Michelson-Morley) deneyini açıklamakta yetersiz kalma sebebi, uzayı "statik, hareketsiz, durgun bir göl suyu gibi" değişmez bir ortam kabul etmeleridir. Oysa Evrenakı modelinde gezegenler uzayda durgun bir sıvıya (duvara) çarparak ilerlemezler. 

Dünya, Güneş'in kendi dönüşüyle yarattığı o devasa "Güneş Sistemi Evrenakı Girdabı (Kepler Akıntısı)" içerisinde bir yaprak gibi nehirde sürüklenirken; bir taraftan da kendi ekseni etrafında dönerek (spin) "yerel bir girdap" (atmosferin hemen dışındaki sarmal Evrenakı zarfı) yaratır. Dünya, kendi yarattığı ve kendisiyle birlikte uzayda ilerleyen bu Evrenakı balonunun içinde, Güneş akıntısıyla **aynı hızda** yol alır. 

Gezegenin yüzeyindeki ve çevresindeki yakın Evrenakı onunla birlikte aynı hızda ve yönde döndüğü/ilerlediği için aralarındaki **Bağıl Hız Sıfırdır:**

$$v_{bağıl} = v_{Dünya} - v_{Evrenakı} = 0$$

Bağıl hızın sıfır ($0$) olması, Navier-Stokes kuralları gereği hidrodinamik sürtünme ve sürüklenme kuvvetini doğrudan sıfırlar ($F_d = 0$).

Evrenakı, gezegenlerin önüne çıkıp onları yavaşlatan statik dev bir okyanus/fren değildir. Aksine gezegenleri makro girdap akıntılarıyla (entrainment) taşıyan, içindeki momentum kaybını mikro/makro spin mekanizmalarıyla tazeleyen, sürtünmesiz ve kusursuz bir "Kozmik Akışkan Motorunun" ta kendisidir. Kütle-İtim modeli, bu kusursuz sürüklenme mekanizmasıyla, gezegenlerin milyarlarca yıl boyunca uzayda sürtünme kaynaklı bir enerji kaybına uğramadan yörüngelerinde kalabilmelerinin sırrını tam bir akışkanlar mekaniği rasyonalitesiyle çözer. (Ortam yoğunluğunun kozmolojik ölçekte çok yavaş seyrelmesinden doğan tedrici yörünge açılması ayrı bir olgudur; Bkz. 3.9.5.) M&M deneyi esirin yokluğunu değil, Dünya ile onu saran Evrenakı zarfı arasındaki bağıl hızın (esir rüzgarının) sıfır olduğunu ispatlamış muazzam bir denemedir.

**Zarfın İki Ayrı İşlevi: Yönsel Sürükleme ve Skaler Saydamlık.** Buradan sık karşılaşılan bir yanlış anlama doğar: "Eğer zarf yerel Evrenakı'yı Dünya ile birlikte taşıyıp M&M'i sıfırlıyorsa, ışık hızının kozmolojik değişimlerini ölçmeyi amaçlayan deneyler (bkz. Kısım 5) bu değişimleri nasıl görebilir? Zarf onları perdelemez mi?" Cevap, zarfın **birbirinden bağımsız iki işlevi** olmasında yatar. Zarf, yalnızca **yönsel bağıl hızı** (esir rüzgârını, vektörel büyüklüğü) sıfırlar; ama Evrenakı her maddeye nüfuz ettiğinden, ortamın **skaler $P/\rho$ büyüklüğüne saydamdır** — bu değer perdelenmez, yerel kozmik ortamın değerini izler. Denizaltı benzetmesi nettir: gövdeyi saran sınır tabakası denizaltıyla birlikte hareket eder (gövdede bağıl akış ve sürtünme yoktur ≈ M&M sıfır), ama o tabakanın basıncı ve yoğunluğu, denizaltı farklı derinliklere indikçe yerel ortamın değerini alır. Evrenakı zarfı da Dünya ile birlikte akar (yön anizotropisi sıfır), fakat Dünya farklı kozmik basınç bölgelerinden geçtikçe zarfın $P/\rho$'su bunları izler ve $c=\sqrt{P/\rho}$ zamanla değişir.

Bu ayrım, aynı zamanda hangi düzeneğin neyi ölçtüğünü de belirler. Bir interferometrenin iki kolu arasındaki faz farkı $\Delta\varphi = \tfrac{2\omega}{c}(L_1-L_2)$ olduğundan, skaler bir hız değişiminin ($c\to c+\delta c$) ürettiği kayma $(L_1-L_2)$ ile orantılıdır. Kolları **eşit** olan klasik Michelson–Morley düzeneği bu yüzden skaler zaman-değişimine kördür; yalnızca anlık yön anizotropisini görür ve sonuç sıfırdır. Skaler değişimi yakalamak için kolların **kasıtlı olarak eşitsiz** olması gerekir — Kısım 5'teki asimetrik-kollu düzeneğin (bir kol diğerinin üç katı) fiziksel gerekçesi tam budur. Böylece M&M'in sıfır sonucu ile Kısım 5'in beklenen zamansal sinyali çelişmez; iki deney **farklı fiziksel büyüklükleri** ölçen tamamlayıcı sınamalar olur.

## 3.4.6 Sürüklenme Zarfının Sınavı: Yıldız Sapması ve Fizeau Katsayısı

Bir önceki bölümde (3.4.5), Michelson–Morley deneyinin sıfır sonucunu, Dünya'nın kendi **sürüklenme zarfı** içinde bağıl hızın sıfır olmasıyla açıkladık. Bu açıklama güçlüdür; ancak dürüst bir teori, kendi en güçlü savunmasını da en sert sınava sokmak zorundadır. Sürüklenme fikrine yöneltilebilecek en keskin itiraz, tarihsel olarak esir kuramlarının çoğunu deviren itirazdır: **yıldız sapması.** Bu bölüm, o itirazı tam gücüyle kurar ve Evrenakı'nın ondan nasıl çıktığını gösterir.

### 3.4.6.1 Kıskaç: Beş Gözlem Aynı Anda

Dürüst kayıt: sürüklenme mekanizması tek bir deneyle değil, birbirini kısıtlayan beş bağımsız gözlemle sınanır. Bir modelin ışığı açıklayıp diğerini bozması yetmez; beşini birden vermek zorundadır.

| Gözlem | Ölçülen | Sürüklenmeye dayattığı |
|---|---|---|
| Yıllık yıldız sapması (Bradley, 1728) | Her yıldız gökyüzünde 20,49″ yarıçaplı bir elips çizer | Işığın doğrultusu, gözlemcinin dış ortama göre hızını **taşımalı** |
| Günlük sapma | 0,32″·cos φ (Dünya'nın kendi dönüşünden) | Yön etkisi, zarfın dönüşünden **etkilenmemeli** |
| Su dolu teleskop (Airy, 1871) | Tüp suyla dolunca sapma **değişmez** | Sapma yerel ortamda/zarf sınırında **üretilemez** |
| Kısmi sürükleme (Fizeau, 1851; Zeeman, 1914) | Akan su ışığı hızının $1-1/n^2$'si kadar sürükler | Sürükleme ne tam ne sıfır; **kırılma indisine kilitli** |
| Michelson–Morley (1887) ve modern rezonatörler | Sıfır; yönsel $\Delta c/c < 10^{-17}$ | Yerel ortam laboratuvarla **birlikte hareket etmeli** |

Bu beş satır bir kıskaç kurar. Klasik dalga-esiri mantığında bir çıkış yoktur: birinci ve beşinci satır *tam sürüklenme* ister, ikinci ve üçüncü satır *hiç sürüklenme* ister, dördüncü satır ise *kısmi ve nicel* bir sürüklenme dayatır. Stokes'un (1845) tam sürüklenmeyi kurtarma girişimi, akışkan koşullarının aynı anda sağlanamaması nedeniyle çökmüştü; tarihsel çözüm Lorentz dönüşümlerine, yani göreliliğe giden yol oldu. Evrenakı, farklı ve mekanik bir çıkış sunar.

### 3.4.6.2 Çözümün Anahtarı: Kavrama Skalerdir

Evrenakı'nın esir kuramlarından ayrıldığı kritik nokta, **kavrama ilkesinin doğasıdır** (bkz. 2.4.1). Zerre bir dalga değil, fiziksel bir mermidir; ve ortamla kavraması **skalerdir**: ortamın yerel yoğunluğu Zerre'nin *süratini* belirler, ancak Evrenakı gradyanı yoksa *yönüne karışmaz.* Yön yalnızca gradyan (deplasman eğimi) varlığında, o gradyan ölçüsünde kıvrılır.

Bu tek ilke, kıskacın dört kolunu birden açar:

* **Yıllık ve günlük sapma.** Zerre'nin doğrultusu balistik olarak korunduğundan, sapma tıpkı yağmurda koşan birinin şemsiyesini eğmesi gibi, saf kinematik bir sonuçtur. Dünya'nın dış ortama göre hızı (yörünge için ~30 km/s, dönüş için ~465 m/s) doğrultuya olduğu gibi yansır. Zarfın Dünya (hatta Ay'ı da içine alan gradyan) ile birlikte toplu hareketi, kavrama skaler olduğu için Zerre'nin yönüne karışmaz — bu yüzden zarfın varlığı sapmayı **silmez.**
* **Airy'nin su dolu teleskobu.** Sapma, ışığın gözlemciye varış doğrultusunda zaten kodludur; teleskop içindeki ortam bu doğrultuyu değiştiremez. Skaler kavrama yalnızca tüp içindeki *sürati* düşürür, geliş *açısını* değil — bu yüzden açı değişmez.
* **Michelson–Morley.** Sürat, yerel zarfa göre $c$'ye oturur; zarf laboratuvarla birlikte hareket ettiğinden, laboratuvar çerçevesinde ışık her yönde eşit hızlıdır. Sonuç sıfırdır.

Geriye kıskacın tek sert kolu kalır: Fizeau'nun **kısmi** sürüklemesi. İşte teorinin nicel sınavı buradadır.

### 3.4.6.3 İki Bileşenli Ortam ve Fizeau Katsayısının Türetimi

Fizeau, akan suyun içindeki ışığın, suyun hızının tamamını değil, tam olarak $\left(1-\tfrac{1}{n^2}\right)$ kesrini aldığını ölçmüştür (su için ≈ %44). Neden tam ne 0 ne 1?

Cevap, ortamın **tek parça olmamasındadır.** Işığı taşıyan Evrenakı iki bileşenin süperpozisyonudur — bu, teorinin 1.3.1'deki modelleme dualitesinin ($\Psi_{Evrenakı}=\Psi_0+\sum_i\psi_i$) doğrudan uygulanmasıdır:

1. **Arka plan Evrenakı'sı ($\Psi_0$):** Evrenseldir; suyun molekülleri onu yaratmadı ve akıtamaz. **Durgundur.**
2. **Molekül deplasman payı ($\sum_i\psi_i$):** Her molekülün yerinden ittiği Evrenakı, o molekülün **sürüklenme zarfı** olarak onunla birlikte akar (Postülat 7'nin molekül ölçeğindeki hali).

Su molekülleri, boru ve dış ortamın Evrenakı'sını topluca sürükleyemez; çünkü arka plan durgundur. Yalnızca kendi deplasman paylarını taşırlar. İşte kısmi sürüklemenin fiziksel kökeni budur.

**Nicel türetim.** Işığın dalga boyu molekül ölçeğinden binlerce kat büyük olduğundan, Zerre ortamın hacimce ortalanmış halini örnekler. Üç fiziksel girdi:

(Aşağıda $P$ ve $\rho$ daima **Evrenakı**'nın basıncı ve yoğunluğudur; atomik/moleküler yoğunlukla karıştırılmamalıdır — ikisi birbirine terstir, bkz. 2.4.2 "Birleştirici İlke" kutusu.)

* *(Korunum)* Moleküller Evrenakı'yı yaratmaz/yok etmez, yalnızca iter. Hacimce ortalama **Evrenakı yoğunluğu** sabittir: $\bar\rho_m=\rho_0$.
* *(Basınç)* Moleküller — atomik olarak yoğun olsalar da — hacim kesri $\phi$ kadar yer kaplayan düşük **Evrenakı basıncı** cepleridir (zıtlık kuralı). Hacimce ortalama Evrenakı basıncı: $\bar P_m = P_0(1-\phi)$.
* *(Kavrama Yasası)* Zerre'nin bir ortamdaki sürati, o ortamın Evrenakı basınç-iletim hızıdır: $v=\sqrt{P/\rho}$ (Ek B'de $\rho_0=P_0/c^2$ olarak zaten kullanılan bağıntı; ışığın ses benzeri iletim doğasının, bkz. 2.4.1, nicel ifadesi).

Kırılma indisi bu üçünden çıkar:

$$\left(\frac{c}{n}\right)^2=\frac{\bar P_m}{\bar\rho_m}=\frac{P_0(1-\phi)}{\rho_0}=c^2(1-\phi)\;\;\Longrightarrow\;\; \frac{1}{n^2}=1-\phi$$

Burada kritik bir kavramsal düzeltme vardır: **ışık, madde içinde düşük *Evrenakı basıncı* nedeniyle yavaşlar** (hacimce ortalama Evrenakı yoğunluğu sabit kalır; yalnızca yerel deplasman ceplerinde seyrelir). Bu, kütle-itim mekanizmasıyla tam aynı dildir — her ikisi de bir düşük Evrenakı-basıncı olgusudur.

Sürükleme katsayısına gelince: ortamın momentum-ağırlıklı ortalama hızı, yalnızca akan deplasman payından gelir:

$$w=\frac{\rho_0\cdot 0+\dfrac{\rho_0\phi}{1-\phi}\cdot u}{\dfrac{\rho_0}{1-\phi}}=\phi\,u$$

Zerre balistik olduğundan laboratuvar hızı $v_{lab}=\dfrac{c}{n}+w$, yani sürükleme katsayısı $f=\phi$. İki sonucu birleştirince:

$$\boxed{\,f=\phi=1-\frac{1}{n^2}\,}$$

Su için ($n=1{,}333$) bu $f=0{,}437$ verir; Michelson & Morley'in (1886) ölçtüğü $0{,}434\pm0{,}020$ değeriyle %1'in altında bir uyum. Katsayı yalnızca $n$'ye bağlıdır, boru uzunluğundan bağımsızdır — Zeeman'ın uzunluk-bağımsızlık gözlemi de böylece karşılanır.

### 3.4.6.4 Tek Mekanizma, İki Ölçek

Bu türetimin en güçlü yanı ekonomisidir. Michelson–Morley'in sıfır sonucu ile Fizeau'nun kısmi sürüklemesi, standart tarihte iki ayrı bilmece olmuştur. Evrenakı'da ikisi **tek bir mekanizmanın** iki ölçekteki görünümüdür:

* **Gezegen ölçeğinde** sürüklenme zarfı → Dünya yerel Evrenakı'yı tam taşır → M&M sıfır.
* **Molekül ölçeğinde** sürüklenme zarfı → her molekül yalnızca kendi deplasman payını taşır → Fizeau $1-1/n^2$.

Aynı Postülat 7, hem laboratuvarın neden esir rüzgârı görmediğini hem de akan suyun ışığı neden yalnızca kısmen sürüklediğini açıklar.

### 3.4.6.5 Dispersiyon (Renk) Terimi: Zeeman Sınavı

Zeeman (1914–15), Fizeau katsayısının bir de renge bağlı ince bir düzeltme taşıdığını ölçmüştür. Zerre'nin bir **mermi akışı** oluşu (renk = atış ritmi, bkz. 2.3) bu terimi doğal kılar: akan ortam, mermi akışının ritmini Doppler ile kaydırır.

Molekül ortamı $u$ ile aynı yöne aktığında, Zerreleri daha seyrek yakalar; molekül çerçevesindeki ritim kızıla kayar: $\omega'=\omega(1-nu/c)$. Zerre-molekül etkileşimi bu kaymış ritme göre gerçekleştiğinden, kırılma indisi $\omega'$'de değerlenir ve süratte ek bir pay doğar. Entrainment sürüklemesiyle birleştiğinde laboratuvar hızı:

$$v_{lab}=\frac{c}{n}+u\left[\,1-\frac{1}{n^2}+\frac{\omega}{n}\frac{dn}{d\omega}\,\right]$$

İkinci köşeli terim, Lorentz'in dispersiyon-düzeltmeli katsayısının birebir aynısıdır ve Zeeman'ın ölçtüğü pozitif renk katkısını (normal dispersiyonda $dn/d\omega>0$) verir. Böylece Fizeau deneyinin hem ana katsayısı hem de ince renk yapısı, tek bir Zerre-akışı resminden türetilmiş olur.

### 3.4.6.6 Dürüst Kayıt: Açık Kalanlar

Bu bölüm kıskacı kapatır; ancak bilimsel dürüstlük, geriye kalan üç kalemi de işaretlemeyi gerektirir (ayrıntılı liste için bkz. 7.4):

1. **Sürüklenme zarfı katsayısı.** Türetim, deplase edilen Evrenakı'nın *tamamının* molekülle aktığını (zarfın cisimle taşındığını) varsayar. Bu, Postülat 7'nin entrainment tanımıyla tutarlıdır; ancak tam hidrodinamik bir hesabın bu "tam taşıma" katsayısını bağımsızca doğrulaması gerekir.
2. **Dispersiyonun kökeni.** Burada $n(\omega)$ ölçümden alınmış ve hareketli ortamın renkleri nasıl farklı sürüklediği türetilmiştir. $n$'nin *neden* renge bağlı olduğu (dispersiyonun mikroskobik kaynağı) ise ayrı bir sorudur — standart fizikte de öyledir (Lorentz osilatör modeli). Evrenakı'daki karşılığı, Zerre atış ritmi ile molekül girdaplarının rezonans tepkisi arasındaki bağdır ve bir sonraki sürümün konusudur.
3. **Gradyan bükmesi ve astrometri.** Zarfın gradyanlı (Rampa) yapısı, içinden geçen yıldız ışığını hafifçe kırar. Bu bükmenin, Gaia'nın mikro-yay-saniyesi hassasiyetindeki tüm-gökyüzü astrometrisine koyduğu üst sınırla uyumu, nicel olarak ayrıca gösterilmelidir.

Bu kalemler bir zafiyet değil, araştırma programının bir sonraki adımlarıdır: her biri teorinin hangi hesapla daha da güçleneceğini tarif eder.

---

Bu bölümde kütleçekimin yerine geçen mekanizmayı — girdapların basınç gradyanlarını ve girdap rekabetini — gök mekaniği ölçeğinde kurduk. Bir sonraki bölümde aynı girdap mekaniğini gökyüzünden yeryüzüne indiriyoruz: hortumlar, kasırgalar ve mutfağınızdaki girdap deneyleri (Bölüm 3.5), bu bölümde anlatılan hidrodinamik yasaların gözlerimizin önünde işleyen küçük ölçekli provalarıdır.