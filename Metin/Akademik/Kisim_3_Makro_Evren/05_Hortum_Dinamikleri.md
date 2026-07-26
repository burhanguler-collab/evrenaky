# 3.5 Hortum Dinamikleri ve Siklostrofik Denge

## 3.5.1 Akışkan Davranışları ve Basınç Gradyanı

Evrenakı ortamında meydana gelen devasa astrofiziksel olayları (kütle-itim, uydu yörüngeleri, galaktik rotasyonlar) anlayabilmek adına, öncelikle mekanizması bilinen temel akışkan davranışlarına dair klasik analojiler kurmak pedagojik olarak zorunludur. Su gibi gündelik yaşamdan aşina olduğumuz akışkanlar üzerinden yürütülecek bir düşünce deneyi, bize Evrenakı'nın görünmez doğasını ifşa edecektir.

Örneğin, hidrostatik basıncın yarattığı "kaldırma kuvveti" mekanizmasını ele alalım. Su ortamında, yüzeyden derinlere inildikçe kütle-itim kaynaklı hidrostatik basıncın arttığı gözlemlenir. Bu derinliğe bağlı basınç artışının skaler dağılımı ( $\nabla P$ ), suyun temel karakteristiğidir. 
<div style="background: #121212; padding: 20px; border-radius: 12px; border: 1px solid #404040; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; text-align: center;">
  <h3 style="margin-top: 0; margin-bottom: 20px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon 3.5.1: Basınç farkının Net İtim (Kaldırma) ve Sıkıştırma kuvvetlerine dönüşümü.</h3>
  <svg viewBox="0 0 600 360" width="100%" style="max-width: 600px; background: #050505; border: 1px solid #333; border-radius: 8px;">
<defs>
<linearGradient id="waterPressure" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" stop-color="#93c5fd" stop-opacity="1" />
<stop offset="100%" stop-color="#020617" stop-opacity="1" />
</linearGradient>
<marker id="arrowPink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#be185d" />
</marker>
<marker id="arrowGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#022c22" />
</marker>
<marker id="arrowBlue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#3b82f6" />
</marker>
<style>
@keyframes massFloat {
  0%   { transform: translateY(100px); }
  100% { transform: translateY(-80px); }
}
.animated-mass {
  animation: massFloat 6s linear infinite;
}
</style>
</defs>
<rect x="150" y="50" width="300" height="300" fill="url(#waterPressure)" rx="10" />
<line x1="120" y1="80" x2="140" y2="80" stroke="#9ca3af" stroke-width="2" />
<text x="110" y="85" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="end">Düşük Basınç</text>
<line x1="120" y1="200" x2="140" y2="200" stroke="#9ca3af" stroke-width="2" />
<text x="110" y="205" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="end">Orta Basınç</text>
<line x1="120" y1="320" x2="140" y2="320" stroke="#9ca3af" stroke-width="2" />
<text x="110" y="325" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="end">Yüksek Basınç</text>
<line x1="90" y1="80" x2="90" y2="320" stroke="#3b82f6" stroke-width="4" marker-end="url(#arrowBlue)" style="opacity: 0.5" />
<text x="80" y="200" fill="#3b82f6" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" transform="rotate(-90 80 200)">∇P (Basınç Artışı)</text>
<g class="animated-mass">
<circle cx="300" cy="200" r="40" fill="#b45309" />
<text x="300" y="205" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">KÜTLE</text>
<line x1="300" y1="130" x2="300" y2="155" stroke="#be185d" stroke-width="3" marker-end="url(#arrowPink)" />
<line x1="300" y1="290" x2="300" y2="245" stroke="#be185d" stroke-width="6" marker-end="url(#arrowPink)" />
<line x1="220" y1="200" x2="245" y2="200" stroke="#be185d" stroke-width="4" marker-end="url(#arrowPink)" />
<line x1="380" y1="200" x2="355" y2="200" stroke="#be185d" stroke-width="4" marker-end="url(#arrowPink)" />
<line x1="370" y1="200" x2="370" y2="140" stroke="#022c22" stroke-width="4" stroke-dasharray="5 5" marker-end="url(#arrowGreen)" />
<text x="380" y="160" fill="#022c22" font-family="sans-serif" font-size="14" font-weight="bold">NET İTİM</text>
</g>
<text x="460" y="150" fill="#9ca3af" font-family="sans-serif" font-size="12">Alt Basınç &gt; Üst Basınç</text>
<text x="460" y="170" fill="#ff007f" font-family="sans-serif" font-size="12" font-weight="bold">Kaldırma (İtim)</text>
<text x="460" y="240" fill="#9ca3af" font-family="sans-serif" font-size="12">Yan Basınçlar Eşit</text>
<text x="460" y="260" fill="#ff007f" font-family="sans-serif" font-size="12" font-weight="bold">Küresel Sıkıştırma</text>
</svg>
</div>
Basınç, doğası gereği skaler (yönsüz) bir büyüklük olmasına rağmen, akışkan içerisine bir nesne yerleştirildiğinde bu diferansiyel basınç farkı, nesnenin yüzeyinde entegre edilerek net bir "Kuvvet Vektörüne" ($F$) dönüşür. Bu hidrodinamik mekanizma, Evrenakı ortamındaki basınç-kuvvet dönüşümlerinin (Yani Kütle-İtim Teorisi'nin) en temel analojisidir.

Akışkan bir ortama daldırılan bir nesne, her yönden uygulanan dinamik bir basınç alanına maruz kalır. Animasyon 3.5.1'de dikey eksendeki kuvvetleri ele aldığımızda; nesnenin alt yüzeyine uygulanan basınç (derinlikten dolayı) üst yüzeye uygulanan basınçtan daha yüksektir. Basınç alanındaki bu eşitsizlik, yukarı yönlü net bir "İtim Vektörü" yaratır. Kütle-itimi geçici olarak ihmal ettiğimizde, nesne hidrodinamik olarak yüksek basınç bölgesinden düşük basınç bölgesine (yüzeye) doğru "itilecektir". 

İşte bu basit doğa kuralı, fiziğin en büyük sırrını barındırır: **Bir cismin akışkan içinde her zaman yüksek basınçtan düşük basınca doğru itilmesi kuralı.** Bu kural, Evrenakı teorisinin kütle-itimi açıklamadaki en kritik matematiksel temelidir. Kütleler birbirini çekmezler; aralarındaki uzayı (Evrenakı'yı) döndürerek basıncı düşürürler ve dış uzaydaki yüksek Evrenakı basıncı tarafından birbirlerine doğru "İtilirler" (Push).

Öte yandan, yatay kuvvetleri incelediğimizde; nesnenin sağ ve sol yüzeylerine uygulanan basınç eşit büyüklüktedir. Bu zıt yönlü kuvvetlerin vektörel toplamı sıfır olduğu için yatay bir hareket doğmaz. Ancak bu zıt kuvvetler sistemi, nesnenin üzerinde sürekli bir "sıkıştırma (kompresyon)" stresi yaratır. Yumuşak yapılı veya devasa bir nesne (örneğin sıcak magmatik bir gezegen başlangıcı), bu eşit basınç altında kusursuz bir küresel forma sokulur. Yüksek yoğunluklu Evrenakı basıncının, gezegenleri ve yıldızları neden kusursuz "küresel" formda tutan asıl "sıkıştırma kuvveti" olduğu gerçeği, modern bilimin kütleçekimine atfettiği hatalı rolü düzelten hidrodinamik bir gerçektir. (Gezegenlerin kutuplardan basık, ekvatordan şişkin elipsoid formda olmasının sebebi ise burada anlattığımız statik uzay basıncı değil, tamamen ayrı bir mekanizma olan dönüş (spin) dinamiğidir; gezegen döndükçe oluşan merkezkaç etkisi ekvatoru dışa savururken, eksenel/yanal kuvvetler kutuplardan baskı yapar. Bu dinamik deformasyon, Evrenakı'nın anlattığımız bu izotropik/homojen sıkıştırma etkisinden tamamen bağımsızdır).

Ancak unutulmamalıdır ki, bu yanal sıkıştırma kuvvetleri, sisteme Ay gibi ikinci bir kütle yaklaştığında asıl dramatik etkisini gösterir. İlerleyen bölümlerde detaylıca göreceğimiz **"Gelgit" (Tidal)** olayı, Newton fiziğindeki gibi Ay'ın Dünya'daki suları uzaktan "çekmesi" değildir. Asıl mekanizma; Ay'ın kendi Evrenakı girdabının (merkezcil vortex), Dünya yüzeyini çepeçevre saran dinamik bir yanal sıkıştırma kuvveti oluşturmasıdır. Bu girdap kaynaklı sıkıştırma kuvveti, dünyadaki suları (sıkışma kuşağına dik eksende) hem Ay'a doğru hem de Ay'dan uzağa doğru çift yönlü iterek elipsoid bir su kabarması oluşturur. Gelgit, "uzaktan çekim" değil, Ay girdabının Dünya üzerindeki asimetrik yanal hidrodinamik sıkıştırmasının kaçınılmaz bir sonucudur. (Mekanizmanın tam işlenişi, $1/r^3$ gradyan matematiği ve Güneş-Ay kıyası için Bkz. 3.9.2.)

Animasyon 3.5.1'de bu hidrodinamik süreçlerin eşzamanlı etkisi açıkça görülmektedir: Alttaki yüksek basıncın (Alt Basınç) üstteki düşük basıncı yenmesiyle oluşan güçlü **Kaldırma (İtim) Kuvveti**, tüm sistemi düşük basınç alanına (yukarıya) doğru sürüklerken; eşzamanlı olarak yanlardan etki eden eşit kompresyon kuvvetleri, ortadaki küreyi kendi hacmini koruyacak şekilde kusursuz bir küresel forma (sıkıştırılmış hale) sokmaktadır.

## 3.5.2 Klasik Akışkanlarda İtim (Repulsion) Mekanizması ve Gemi Çarpışmaları (Olympic-Hawke Vakası)

Kozmolojik ölçekteki devasa kuvvetleri (gezegenlerin çekimi gibi) anlamadan önce, yeryüzündeki standart akışkanlarda nesnelerin birbirini "çekiyormuş" gibi göründüğü yanılgıların ardındaki fiziksel gerçeği incelemek elzemdir. Algılarımız bizi nasıl aldatır?

Gemi inşaatı ve denizcilik literatüründe "Hydrodynamic Interaction" (Hidrodinamik Etkileşim) veya "Ship-to-Ship Suction" (Gemiden Gemiye Emme) olarak bilinen meşhur ve tehlikeli bir kural vardır: İki büyük gemi denizde birbirine paralel ve dar bir mesafede seyrettiklerinde, hızlandıkça açıklanamaz bir şekilde birbirlerine doğru "çekilirler" ve çarpışma riski doğar. 

Tarihte 1911 yılında devasa lüks yolcu gemisi *RMS Olympic* ile donanma kruvazörü *HMS Hawke* gemilerinin Southampton açıklarında okyanus ortasında açıklanamaz bir şekilde birbirlerine "çekilerek" çarpışması, bu etkinin mahkemelerde bilimsel olarak incelendiği ilk büyük vakadır. Bu durum, iki geminin kütlesinin uzaktan anında etki eden hipotetik bir Newton çekim kuvvetiyle birbirini çekmesiyle açıklanamaz; oysa uzaydaki gezegenler söz konusu olduğunda klasik yaklaşım tam olarak bu varsayımsal çekime (Gravity) dayanmaktadır.

Olayın ardındaki asıl mekanizma **Bernoulli İlkesi**'dir (Bernoulli, 1738) ve gezegenler için de geçerlidir:
1. İki geminin arasındaki dar kanalda (boğazda) akan suyun hızı, gemilerin dış taraflarındaki (açık denizdeki) suyun hızından çok daha yüksektir. (Daralma etkisi).
2. Suyun hızının arttığı bu orta bölgede basınç ($P_{iç}$) Bernoulli ilkesi gereği aniden düşer.
3. Gemilerin dış yüzeylerindeki durgun (veya yavaş akan) deniz suyu ise çok daha yüksek bir statik basınca ($P_{dış}$) sahiptir.
4. Oluşan bu devasa yüksek basınç farkı ($\nabla P = P_{dış} - P_{iç}$), gemileri dışarıdan içeriye doğru kararlılıkla **iter (push)**.

Uzaktan bakan bir gözlemci "gemiler birbirini çekiyor (pull)" biçiminde yorumlar; tıpkı klasik yaklaşımın elmanın düşüşünü Dünya'nın çekimi olarak yorumlaması gibi. Oysa gerçekte olan biten, **dış okyanus basıncının nesneleri içteki düşük basınca doğru itmesidir (push)**. Akışkanlar dünyasında "çekim" (Gravity) aslında kavramsal bir basitleştirmedir, asıl çalışan mekanizma her zaman "İtim" (Push) yönündedir.

<div style="background: #121212; padding: 20px; border-radius: 12px; border: 1px solid #404040; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; text-align: center;">
  <h3 style="margin-top: 0; margin-bottom: 20px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon 3.5.2: Dış okyanus (veya Evrenakı) basıncı, gemileri (veya kütleleri) birbirine doğru iter.</h3>
  <svg viewBox="0 0 600 360" width="100%" style="max-width: 600px; background: #050505; border: 1px solid #333; border-radius: 8px;">
<defs>
<linearGradient id="lowPressure" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="rgba(255,0,127,0)" />
<stop offset="50%" stop-color="rgba(255,0,127,0.2)" />
<stop offset="100%" stop-color="rgba(255,0,127,0)" />
</linearGradient>
</defs>
<rect x="240" y="50" width="120" height="300" fill="url(#lowPressure)" />
<text x="300" y="190" fill="#ff007f" font-family="sans-serif" font-size="16" text-anchor="middle" font-weight="bold" opacity="0.9">DÜŞÜK BASINÇ</text>
<text x="300" y="210" fill="#ff007f" font-family="sans-serif" font-size="12" text-anchor="middle" opacity="0.8">(Hızlı Akış - Çukur)</text>
<g transform="translate(180, 100)">
<path style="fill: #1f2937; stroke: #60a5fa; stroke-width: 2;" d="M 20 0 Q 50 0 50 50 L 50 150 Q 50 200 20 200 Q -10 200 -10 150 L -10 50 Q -10 0 20 0 Z" />
<text x="20" y="105" style="fill: #9ca3af; font-family: sans-serif; font-size: 14px; font-weight: bold;" text-anchor="middle" transform="rotate(-90 20 100)">OLYMPIC</text>
</g>
<g transform="translate(380, 100)">
<path style="fill: #1f2937; stroke: #60a5fa; stroke-width: 2;" d="M 20 0 Q 50 0 50 50 L 50 150 Q 50 200 20 200 Q -10 200 -10 150 L -10 50 Q -10 0 20 0 Z" />
<text x="20" y="105" style="fill: #9ca3af; font-family: sans-serif; font-size: 14px; font-weight: bold;" text-anchor="middle" transform="rotate(-90 20 100)">HAWKE</text>
</g>
<line x1="80" y1="0" x2="80" y2="400" style="stroke: #3b82f6; stroke-width: 2; opacity: 0.4; stroke-dasharray: 10 5;">
<animate attributeName="stroke-dashoffset" from="0" to="-30" dur="3s" repeatCount="indefinite" />
</line>
<line x1="120" y1="0" x2="120" y2="400" style="stroke: #3b82f6; stroke-width: 2; opacity: 0.4; stroke-dasharray: 10 5;">
<animate attributeName="stroke-dashoffset" from="0" to="-30" dur="3s" repeatCount="indefinite" />
</line>
<text x="100" y="50" fill="#3b82f6" font-family="sans-serif" font-size="16" text-anchor="middle" font-weight="bold" opacity="0.9">YÜKSEK BASINÇ</text>
<text x="100" y="70" fill="#3b82f6" font-family="sans-serif" font-size="12" text-anchor="middle" opacity="0.8">(Yavaş Akış)</text>
<line x1="480" y1="0" x2="480" y2="400" style="stroke: #3b82f6; stroke-width: 2; opacity: 0.4; stroke-dasharray: 10 5;">
<animate attributeName="stroke-dashoffset" from="0" to="-30" dur="3s" repeatCount="indefinite" />
</line>
<line x1="520" y1="0" x2="520" y2="400" style="stroke: #3b82f6; stroke-width: 2; opacity: 0.4; stroke-dasharray: 10 5;">
<animate attributeName="stroke-dashoffset" from="0" to="-30" dur="3s" repeatCount="indefinite" />
</line>
<text x="500" y="50" fill="#3b82f6" font-family="sans-serif" font-size="16" text-anchor="middle" font-weight="bold" opacity="0.9">YÜKSEK BASINÇ</text>
<text x="500" y="70" fill="#3b82f6" font-family="sans-serif" font-size="12" text-anchor="middle" opacity="0.8">(Yavaş Akış)</text>
<line x1="260" y1="0" x2="260" y2="400" style="stroke: #06b6d4; stroke-width: 3; opacity: 0.8; stroke-dasharray: 15 5;">
<animate attributeName="stroke-dashoffset" from="0" to="-60" dur="1s" repeatCount="indefinite" />
</line>
<line x1="300" y1="0" x2="300" y2="400" style="stroke: #06b6d4; stroke-width: 3; opacity: 0.8; stroke-dasharray: 15 5;">
<animate attributeName="stroke-dashoffset" from="0" to="-60" dur="1s" repeatCount="indefinite" />
</line>
<line x1="340" y1="0" x2="340" y2="400" style="stroke: #06b6d4; stroke-width: 3; opacity: 0.8; stroke-dasharray: 15 5;">
<animate attributeName="stroke-dashoffset" from="0" to="-60" dur="1s" repeatCount="indefinite" />
</line>
<g style="fill: #ff007f;">
<animateTransform attributeName="transform" type="translate" values="95,200; 115,200; 95,200" dur="1.5s" repeatCount="indefinite" />
<animate attributeName="opacity" values="0.5; 1; 0.5" dur="1.5s" repeatCount="indefinite" />
<path d="M 0 -15 L 40 -15 L 40 -25 L 65 0 L 40 25 L 40 15 L 0 15 Z" />
<text x="30" y="-35" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">İTİM KUVVETİ</text>
</g>
<g style="fill: #ff007f;">
<animateTransform attributeName="transform" type="translate" values="505,200; 485,200; 505,200" dur="1.5s" repeatCount="indefinite" />
<animate attributeName="opacity" values="0.5; 1; 0.5" dur="1.5s" repeatCount="indefinite" />
<path d="M 0 -15 L -40 -15 L -40 -25 L -65 0 L -40 25 L -40 15 L 0 15 Z" />
<text x="-30" y="-35" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">İTİM KUVVETİ</text>
</g>
</svg>
</div>

## 3.5.3 Hortum (Vortex) Dinamikleri ve Merkezdeki Çekim Fenomeninin Akışkanlar Dinamiğindeki Karşılığı

Atmosfer, akışkanlar mekaniği kurallarına tabi gaz tabanlı bir ortamdır. Astronomik ölçekteki devasa girdapları (galaksileri) anlamak için atmosferdeki en dramatik fenomen olan girdapları (hortumları/tornadoları) analiz etmeliyiz. Girdap dinamiği açısından hortumun nasıl oluştuğu sorusundan ziyade, ortam rotasyonel bir akışa geçtiğinde hangi hidro-mekanik kuvvetlerin doğduğuna odaklanacağız.

![Şekil 3.5.1: Hortum. (Weather.gov > Safety > Tornado Safety)](Gorseller/image2.jpg)

Tipik bir hortumun merkez hattı (Göz bölgesi) incelendiğinde, bu bölgenin çevresine kıyasla daha koyu/katı parçacıklarla, tozla, taşla, hatta sökülmüş ev çatılarıyla dolu olduğu görülür. Klasik bir dairesel dönüş (santrifüj) modelinde, kütlesi olan ağır partiküllerin "merkezkaç" (centrifugal) etkisiyle dışarı fırlatılması ve dönme merkezinin (gözün) tamamen boş kalması beklenirdi. Bir ipin ucundaki taşı çevirdiğinizde taş dışarı kaçmak ister. Peki, dışarı savrulması gereken o devasa ağır çatıların ve partiküllerin inatla hortumun merkezinde hapsolmasını ve güçlü bir şekilde merkeze doğru "çekilmesini" sağlayan içsel kuvvet nedir? 

Bu paradoksun çözümü, Evrenakı ortamında kütle-itim mekanizmasını anlamanın yegâne anahtarıdır.
<div style="background: #121212; padding: 20px; border-radius: 12px; border: 1px solid #404040; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; text-align: center;">
  <h3 style="margin-top: 0; margin-bottom: 20px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon 3.5.3: Merkezde hızın artmasıyla çöken basınç, partikülü merkeze doğru "İter".</h3>
  <svg viewBox="0 0 600 360" width="100%" style="max-width: 600px; background: #050505; border: 1px solid #333; border-radius: 8px;">
<defs>
<radialGradient id="vortexPressure" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="#ff007f" stop-opacity="0.8" />
<stop offset="30%" stop-color="#a855f7" stop-opacity="0.5" />
<stop offset="100%" stop-color="#3b82f6" stop-opacity="0.2" />
</radialGradient>
<marker id="arrowP" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#ff007f" />
</marker>
<marker id="arrowC" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#3b82f6" />
</marker>
</defs>
<line x1="300" y1="20" x2="300" y2="350" style="stroke: #4b5563; stroke-width: 2; stroke-dasharray: 5 5;" />
<text x="150" y="40" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Siklostrofik Denge (Girdap)</text>
<text x="150" y="60" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">Üstten Kesit Görünümü</text>
<circle cx="150" cy="220" r="120" fill="url(#vortexPressure)" />
<circle cx="150" cy="220" r="100" style="fill: none; stroke: #3b82f6; stroke-width: 1; stroke-dasharray: 10 5;">
<animateTransform attributeName="transform" type="rotate" from="0 150 220" to="360 150 220" dur="4s" repeatCount="indefinite" />
</circle>
<circle cx="150" cy="220" r="60" style="fill: none; stroke: #a855f7; stroke-width: 1.5; stroke-dasharray: 15 5;">
<animateTransform attributeName="transform" type="rotate" from="0 150 220" to="360 150 220" dur="2s" repeatCount="indefinite" />
</circle>
<circle cx="150" cy="220" r="25" style="fill: none; stroke: #ff007f; stroke-width: 2; stroke-dasharray: 20 5;">
<animateTransform attributeName="transform" type="rotate" from="0 150 220" to="360 150 220" dur="0.8s" repeatCount="indefinite" />
</circle>
<g>
<animateTransform attributeName="transform" type="translate" values="50,0; -15,0; 50,0" dur="4s" repeatCount="indefinite" />
<circle cx="200" cy="220" r="6" fill="#10b981" />
<text x="190" y="205" fill="#10b981" font-family="sans-serif" font-size="12" font-weight="bold">Kütle</text>
<line x1="250" y1="220" x2="210" y2="220" stroke="#ff007f" stroke-width="3" marker-end="url(#arrowP)" />
<text x="260" y="225" fill="#ff007f" font-family="sans-serif" font-size="12" font-weight="bold">∇P (İtim)</text>
<line x1="200" y1="220" x2="230" y2="220" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowC)" />
<text x="235" y="235" fill="#3b82f6" font-family="sans-serif" font-size="11">v²/r</text>
</g>
<text x="150" y="360" fill="#ff007f" font-family="sans-serif" font-size="12" text-anchor="middle" font-weight="bold">İç Basınç &lt; Dış Basınç (İçeri İtim)</text>
<text x="450" y="40" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Hız (V) ve Basınç (P) Profili</text>
<line x1="330" y1="300" x2="570" y2="300" stroke="#4b5563" stroke-width="2" />
<text x="580" y="305" fill="#9ca3af" font-family="sans-serif" font-size="12">r</text>
<text x="450" y="320" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">Merkez (r=0)</text>
<line x1="450" y1="80" x2="450" y2="300" stroke="#4b5563" stroke-width="1" stroke-dasharray="4 4" />
<path d="M 330 120 Q 400 120 440 280 L 460 280 Q 500 120 570 120" fill="none" stroke="#ff007f" stroke-width="3" />
<text x="350" y="110" fill="#ff007f" font-family="sans-serif" font-size="14" font-weight="bold">Basınç (P)</text>
<path d="M 330 280 Q 400 280 430 150 L 450 300 L 470 150 Q 500 280 570 280" fill="none" stroke="#fbbf24" stroke-width="3" />
<text x="550" y="270" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">Hız (v)</text>
<line x1="520" y1="80" x2="520" y2="300" stroke="#10b981" stroke-width="2" stroke-dasharray="4 4">
<animate attributeName="x1" values="550; 485; 550" dur="4s" repeatCount="indefinite" />
<animate attributeName="x2" values="550; 485; 550" dur="4s" repeatCount="indefinite" />
</line>
<circle cx="520" cy="300" r="4" fill="#10b981">
<animate attributeName="cx" values="550; 485; 550" dur="4s" repeatCount="indefinite" />
</circle>
</svg>
</div>
Hortumun (Vortex) iç dinamikleri Bernoulli ilkesi ve dairesel akım (circulation) kuralları ile analiz edildiğinde, "Hız" ve "Basınç" arasında ters orantılı kesin bir denklem ortaya çıkar. Animasyon 3.5.3'te net bir şekilde görüldüğü gibi; girdap merkezinde (r=0 noktasına yaklaştıkça) dönüş hızı inanılmaz boyutlara ulaşırken, akışkan (hava) basıncı merkezde ani bir çökme (düşüş) yaşar. Akışkanlar mekaniğindeki **Siklostrofik Denge** formülü ($v^2/r \propto \nabla P$) gereği, merkezdeki düşük basınç alanı devasa bir vakum (emme/itme) kuvveti yaratır.

Merkezden dışarıya doğru radyal olarak ilerledikçe rüzgar (akışkan) hızı azalırken, statik hava basıncı artarak atmosferik normale döner. Su altı analojisinde (ve Gemi örneğinde) kurduğumuz altın kuralı burada da işletirsek: **Partiküller daima yüksek basınçtan (dış çeperden) düşük basınca (hortumun merkezine) doğru itilir.** 

İşte merkezkaç kuvvetiyle dışarı fırlamaya çalışan ağır partikülleri yenecek kadar güçlü olan ve onları merkeze kesintisizce yapıştıran mekanizma, dönüş nedeniyle merkezde oluşan bu olağanüstü basınç düşüşüdür. (Basınç Gradyanı Kuvveti > Merkezkaç Kuvveti). Çatıları içeri çeken şey "çekim" değil, dış havanın "itimidir". 

Güneş sistemi de, Evrenakı (Aether) okyanusunda dönen devasa bir hortumdur. Merkezinde Güneş vardır ve gezegenlerin Güneş'ten dışarı savrulmasını (merkezkaç etkisini) yenen şey, Evrenakı'nın dış uzaydaki o devasa basıncının ( $\nabla P$ ) gezegenleri girdap merkezine (Güneşe) doğru itmesidir.

## 3.5.4 Makroskobik Girdap (Forced Vortex) Laboratuvar Deneyi

Hortum mekanizmasında gördüğümüz, dönen akışkanın merkezine doğru oluşan bu basınç gradiyanı etkisini laboratuvar şartlarında izole edebiliriz. Kapalı bir silindirik kap (örneğin bir Erlenmeyer şişesi) içine su ve bir miktar askıda kalabilen ağır partikül (örn. sim veya pirinç taneleri) konulup sistem dış eksen etrafında döndürüldüğünde (Forced Vortex oluşturulduğunda) şaşırtıcı bir sonuç gözlemlenir.

![Şekil 3.5.2: Su içerisinde yaratılan kuvvetler ve makroskobik girdap deneyimi.](Gorseller/image4.png)

Akışkan kuvvetlice döndürülüp dışarıdan müdahale kesildiğinde, kap içindeki su kendi ataletiyle dönmeye devam eder. Tıpkı atmosferdeki hortum analojisinde olduğu gibi, sıvı girdabının merkez hattında akış hızı (açısal sirkülasyon nedeniyle) maksimize olurken sıvı basıncı minimuma (hatta bazen kavitasyona varacak düzeyde aşağı) iner. 

Kaptaki dağınık ve ağır sim partikülleri, merkezkaçın dışarı savurma etkisini ezip geçen bu **"radyal basınç gradyanı"** (Dış suyun basıncının merkeze doğru bastırması) nedeniyle hızla merkeze doğru itilir ve tam merkez sütununda dikine birikir. (Şekil 3.5.2). Kütleleri yoğun olan bu cisimler dış cama değil, girdabın tam ortasına yığılmıştır.

Evrenakı teorisinde güneş sisteminin gezegensel disk formu ve Samanyolu gibi devasa galaksilerin o belirgin yassı-sarmal formu, kütlelerin birbirini "hipotetik gravitonlarla" çekmesiyle değil, tamamen bu makroskobik girdap mekaniğinin hidrodinamik itimi (merkeze yığılması) sonucu oluşur. Galaktik ölçekte dönen bir Evrenakı havzası, içindeki tüm yıldız kütlelerini o muazzam girdabın basınç gradyanı sayesinde merkeze doğru bir arada tutar ve galaksileri parçalanmaktan kurtarır. Karanlık Madde arayışı, işte tam da bu akışkan denklemini fizikten kopardıkları için içine düştükleri teorik bir çıkmazdır (illüzyonun tam çözümlemesi için Bkz. 3.1.8; matematiksel rejim analizi için Bölüm 4.2).