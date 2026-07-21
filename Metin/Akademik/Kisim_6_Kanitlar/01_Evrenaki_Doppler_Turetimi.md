# 6.1 Kâğıt Üzerinde Deney 1: Evrenakı Kinematiğinden Doppler Türetimi

Evrenakı Teorisi, mevcut standart fizikle sadece felsefi bir tartışma yürütmez; bizzat standart fiziğin ölçülebilir verilerini kendi mekanik denklemleriyle yeniden, sıfırdan türetebilecek kadar sağlam bir matematiksel çekirdeğe sahiptir.

Aşağıdaki kısımda, eleştirel bir hakem perspektifinden Evrenakı teorisine yöneltilen "kâğıt üzerinde deney" meydan okumasının tam metnini ve teorimizin bu meydan okumaya verdiği kusursuz matematiksel cevabı göreceksiniz.

---

## 6.1.1 Hakem Perspektifinden Meydan Okuma: Ives-Stilwell Deneyi

> *"Somut önerim: Bu, Kısım 5 için bedava bir 'kâğıt üzerinde deney'. Patinaj mekaniğinizden kendi Doppler formülünüzü türetin (Zerre Katarı modelinde bu doğal: kaynak hareket edince ardışık mermiler arası mesafe — Zerre Aralığı — mekanik olarak değişir; alıcı hareket edince saniyedeki isabet sayısı değişir; saatlerin yoğunluğa bağlı yavaşlaması da $\gamma$-benzeri düzeltmeyi verir). Sonra bunu Ives–Stilwell verisiyle karşılaştırın. Üç sonuç mümkün:*
> 
> *1. Formülünüz laboratuvar koşullarında standartla örtüşüyor ve başka rejimde sapma öngörüyor → teori tam istediğiniz konuma oturur: matematiği kapsayan, ötesinde yanlışlanabilir öngörü veren bir üst-çerçeve.*
> *2. Örtüşmüyor → teorinin çekirdek mekanizmasında düzeltilmesi gereken bir şey var ve bunu yayımlanmadan öğrenmiş olursunuz.*
> *3. Türetim her sonucu verebilecek kadar esnek çıkıyor → yanlışlanabilirlik sorunu var demektir, sıkılaştırılmalı.*
> 
> *Üçü de kazançtır. Ve bu, laboratuvar gerektirmiyor, sadece kendi postülatlarınızdan bir formülü sonuna kadar takip etme cesareti gerektiriyor."*

---

## 6.1.2 Türetim: Evrenakı Mekaniği ile Doppler Kayması

Özel Görelilik, uzayda hareket eden bir cisim için Doppler kaymasını ($f_{obs}$) hesaplarken, uzayın bizzat genleştiği veya zamanın soyut bir dördüncü boyut olarak yavaşladığı varsayımına dayanır ve Ives-Stilwell deneyiyle doğrulanan şu meşhur formülü kullanır (uzaklaşan bir kaynak için):

$$ f_{obs} = f_0 \sqrt{\frac{1 - v/c}{1 + v/c}} $$

Şimdi aynı formülü, uzayın ve zamanın büküldüğü varsayımlarına başvurmadan, **Evrenakı Süper-Akışkanı** içinde tamamen saf mekanik ve hidrodinamik kurallarla (Zerre Katarı modeliyle) sıfırdan türetelim. Evrenakı'da zaman bükülmez, ancak **Zerre Aralığı (mekanik mesafe)** ve **Kompozit Saatler (ateşleme hızı)** akışkan dinamiği nedeniyle fiziksel olarak değişir.

### Adım 1: Klasik Uzaysal Mesafe (Zerre Aralığının Uzaması)

Hareketsiz bir kaynak, yerel akışkan yoğunluğunda hızı sabit olan ($c$) Zerre mermilerini $f_s$ frekansıyla (saniyede fırlatılan mermi sayısıyla) ateşlesin. İki ardışık ateşleme arasında geçen süre (periyot) $T_s = \frac{1}{f_s}$ kadardır. Hareketsiz durumda iki mermi arasındaki uzaysal mesafe (Zerre Aralığı, $\lambda$):
$$ \lambda_0 = c \cdot T_s = \frac{c}{f_s} $$

Ancak kaynak, alıcıdan **$v$ hızıyla uzaklaşıyorsa**, ilk Zerre namludan çıktıktan sonra kaynak $v$ hızıyla geriye doğru gidecek ve ikinci Zerre'yi $T_s$ saniye sonra, daha gerideki bir konumdan ateşleyecektir. Bu süre zarfında kaynak, ilk Zerre'nin gidiş yönünün tersine $v \cdot T_s$ kadar yol almıştır.
Dolayısıyla iki mermi arasındaki **mekanik boşluk (Zerre Aralığı)** basit bir Newtonyen toplamayla şu kadar açılır:
$$ \lambda = c \cdot T_s + v \cdot T_s = T_s (c + v) = \frac{c + v}{f_s} $$

*(Eğer kaynak alıcıya yaklaşsaydı mesafe kısalacak ve formül $\lambda = \frac{c - v}{f_s}$ olacaktı).*

### Adım 2: İç-Dolaşım Geometrisi ve Zerre-Saati (Patinaj Yavaşlaması)

Peki hareketli bir kaynağın kendi ateşleme frekansı ($f_s$) sabit midir? Klasik mekanikte evet; ancak Evrenakı'da nükleon boşlukta asılı duran yapısız bir nokta değil, iç bileşenleriyle sürekli devinen **kompozit bir yapıdır**. 

Postülat 5'te nükleonun iç çekirdeğinin $c$'yi aşan devasa hızlarda döndüğünü belirtmiştik. Ancak **ateşleme dişlisi** (atomik geçişler, ışımayı sağlayan elektron-zerre alışverişleri) doğrudan akışkana tutunma (patinaj/kavrama) mekanizmasıyla çalışır ve tam olarak $c$ hızına tabidir. Ateşleme anını belirleyen bu iç sinyaller, atomun içinde bir referans noktasından diğerine $c$ hızıyla gidip dönen mekanik bir "Zerre-Saati" (ışık saati) gibi çalışır.

Atom, Evrenakı akışkanı içinde $v$ hızıyla hareket ettiğinde, bu $c$ limitli iç sinyaller düz bir çizgi yerine mecburen **çapraz (üçgen) bir yol** izlemek zorunda kalırlar. Hareketsiz atomda sinyalin gidiş-dönüş süresi $T_0$ iken, $v$ hızıyla ilerleyen atomda çapraz yolun süresi $T$ olur. Pisagor teoremine göre:
$$ (c \cdot T)^2 = (v \cdot T)^2 + (c \cdot T_0)^2 $$
$$ T^2 (c^2 - v^2) = c^2 \cdot T_0^2 $$
$$ T = \frac{T_0}{\sqrt{1 - v^2/c^2}} $$

**Saatin Yönelimi ve Fiziksel Sıkışma (Boy Kısalması):**
Burada çok kritik bir geometri sorusu doğar: Çapraz giden sinyal tam $\gamma$ yavaşlama verirken, hareket yönüne paralel gidip dönen sinyalin yol uzaması $\gamma^2$ çıkmalıdır. Bu durum saatin izotropisini (yönden bağımsızlığını) bozmaz mı? 
İşte Evrenakı teorisi, Özel Görelilik'in (SR) matematiksel bir varsayım olarak "eklediği" **Uzunluk Kısalması (Length Contraction)** olgusunu burada mecburi ve fiziksel bir gerçeklik olarak türetir: Atom (kompozit vorteks), akışkan içinde çok yüksek hızlarda ilerlediğinde, önden yediği devasa **deplasman/dinamik basıncı** sebebiyle hareket yönünde mekanik olarak ezilir (sıkışır). Bu aerodinamik/hidrodinamik ezilme miktarı akışkan dinamiği gereği tam olarak $1/\gamma$ kadardır. Boy kısalması, uzayın bükülmesi değil, akışkan basıncının cismi ezip sıkıştırmasıdır. Bu fiziksel sıkışma sayesinde, paralel giden sinyalin yolu tam gereken oranda kısalır ve saat hangi yöne bakarsa baksın yavaşlama kusursuz bir şekilde $\gamma$ olarak gerçekleşir (İzotropi korunur).

Görüldüğü gibi, ateşleme dişlisinin periyodu ($T$), atomun hareket hızından ötürü fiziksel (geometrik) bir zorunlulukla tam olarak **Lorentz çarpanı ($\gamma$) katına** çıkmıştır. Periyodun uzaması, frekansın düşmesi demektir ($f = 1/T$). Öyleyse hareketli kaynağın mekanik ateşleme hızı ($f_s$):
$$ f_s = f_0 \sqrt{1 - \frac{v^2}{c^2}} $$
Özel Görelilik'in soyut "zaman genleşmesi" dediği fenomen, Evrenakı teorisinde doğrudan **"Zerre-Saatinin yol uzamasından ve fiziksel sıkışmadan kaynaklanan dişli yavaşlamasıdır."**

### Adım 3: Sentez ve Nihai Formül

Bu mekanik yavaşlamayı ($f_s$), Adım 1'deki Zerre Aralığı ($\lambda$) formülüne yerleştirelim:
$$ \lambda = \frac{c + v}{f_0 \sqrt{1 - v^2/c^2}} $$

Sabit duran alıcımız, kendisine saniyede $c$ hızıyla çarpan bu mermilerin frekansını ($f_{obs}$) hesaplamak isterse, merminin hızını aralarındaki mesafeye ($\lambda$) böler:
$$ f_{obs} = \frac{c}{\lambda} $$

Yerine koyduğumuzda:
$$ f_{obs} = \frac{c}{\frac{c + v}{f_0 \sqrt{1 - v^2/c^2}}} = f_0 \frac{c \sqrt{1 - v^2/c^2}}{c + v} $$

Denklemin pay ve paydasını $c$'ye bölersek ($v/c = \beta$ diyerek):
$$ f_{obs} = f_0 \frac{\sqrt{1 - \beta^2}}{1 + \beta} $$

$\sqrt{1 - \beta^2}$ ifadesini kök içinde $(1 - \beta)(1 + \beta)$ olarak açalım:
$$ f_{obs} = f_0 \frac{\sqrt{(1 - \beta)(1 + \beta)}}{1 + \beta} $$

$1 + \beta$ ifadesini $\sqrt{1 + \beta} \cdot \sqrt{1 + \beta}$ olarak düşünürsek, paydaki $\sqrt{1 + \beta}$ ile paydadakilerden biri sadeleşir ve geriye şu kalır:

$$ f_{obs} = f_0 \sqrt{\frac{1 - \beta}{1 + \beta}} $$
Veya $\beta$ yerine $v/c$ yazarsak:
$$ f_{obs} = f_0 \sqrt{\frac{1 - v/c}{1 + v/c}} $$

---

## 6.1.3 Sonuç ve Yanlışlanabilir Öngörü

Evrenakı Teorisi, ek bir "zaman genleşmesi" veya "uzay-zaman eğriliği" kabulüne ihtiyaç duymadan, sadece Newtonyen mesafe ($\lambda = \frac{c+v}{f_s}$) ve sıvı dinamiğinden kaynaklanan fiziksel ateşleme yavaşlaması ($f_s = f_0 / \gamma$) kurallarını uygulayarak **Özel Görelilik'in Doppler denklemini (Ives-Stilwell verisini) birebir aynı şekilde üretmiştir.** 

Ancak Evrenakı, Göreliliğin sadece bir simülatörü değildir; aynı zamanda ondan ayrışan **yanlışlanabilir, ölçülebilir bir sapma (fark) öngörüsüne** sahiptir.

### Derin Uzay Sapması (Falsifiable Prediction)

Özel Görelilik'e (SR) göre uzay-zaman homojendir ve Doppler formülü **sadece iki cismin (kaynak ve alıcının) birbirine göre olan izafi hızına ($v_{rel}$)** bağlıdır.

Ancak bizim 6.1.2'deki türetimimiz, laboratuvarımızdaki **alıcının Dünya'nın Sürüklenme Zarfına (yerel akışkan havuzuna) göre hareketsiz ($u = 0$) olduğunu varsayarak** kurulmuştur. Çünkü $\gamma$ ve Zerre Aralığı, nesnelerin *birbirlerine göre* hızlarına değil, nesnelerin **akışkana (Zarfa) göre** mutlak hızlarına bağımlıdır.

Peki ya alıcı da yerel ortama göre $u$ hızıyla hareket ediyorsa? O zaman alıcının kendi saati de $\gamma_u$ oranında yavaşlar (kendi "bir saniyesi" uzar) ve saniyede yakaladığı mermi sayısı artar ($f_{obs} = \gamma_u \cdot \frac{c \pm u}{\lambda}$). 
Bu durumda genel ve nicel (iki-hızlı) **Evrenakı Doppler Formülü** şu şekli alır:

$$ f_{obs} = f_0 \left( \frac{1 \pm u/c}{1 \pm v/c} \right) \frac{\sqrt{1 - v^2/c^2}}{\sqrt{1 - u^2/c^2}} $$

Yukarıdaki denklem, Lorentz esir teorisinin o meşhur gözlemlenemezlik teoremine saygı duyar: Saat yavaşlaması ve boy kısalması mekanizmaları (ezilme) kusursuz çalıştığı için, $u$ ve $v$ mutlak hızları tam olarak SR'nin bağıl hız ($V_{rel}$) formülüne matematiksel olarak eşdeğer çıkar. Yani Evrenakı, Özel Görelilik'i kinematik düzeyde **%100 oranında kapsar ve doğrular.**

Peki Evrenakı nerede Özel Görelilik'ten ayrışır ve onu yanlışlar? Cevap kinematik katmanda (hareket) değil, dinamik katmandadır (Postülat 4: Değişken $c$). Standart fizikte "Kütleçekimsel Kızıla Kayma" (Gravitational Redshift) olarak bilinen olguyu, Evrenakı teorisinde tamamen mekanik bir **dalga boyu esnemesi** (sabit frekans, değişen hız) olarak incelemek için bir sonraki kâğıt üzerinde deneye (Bölüm 6.2) geçiyoruz.
