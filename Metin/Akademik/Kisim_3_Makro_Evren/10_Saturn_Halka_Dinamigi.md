# 3.10 Satürn Halka Dinamiği: Akışkanlar Mekaniği Türetimi ve Dürüst Sınır Analizi

## 3.10.1 Amaç ve Dürüstlük İlkesi

Bu bölüm, Evrenakı Teorisi'nin Satürn halkalarındaki dikey salınım ve sönüm olgusuna dair **kendi postülalarından türetilmiş** bir matematiksel çerçeve sunar. Üç ilkeye sıkı sıkıya bağlı kalınmıştır:

1. **Nerede Evrenakı standart Newton sonucuyla aynı çıkıyorsa, bu açıkça belirtilir** — çünkü teorinin rejim aksiyomu gereği (Bkz. Bölüm 4.2), güneş sistemi ölçeğinde 1/r² yasasına indirgenmesi *zaten beklenen* bir sonuçtur, yeni bir keşif değildir.
2. **Nerede Evrenakı gerçekten farklı/yeni bir terim öngörüyorsa, bu ayrıca izole edilir** — çünkü teorinin asıl test edilebilir iddiası burada yatar.
3. **Ortak mekanizmadan beslenen başka bölümlerin nicel durumu, buraya taşınmadan önce denetlenir** (Bölüm 6.3'ün frame-dragging kalemi; bkz. 3.10.6) — aynı sistematiği iki gözleme taşımamak için.

## 3.10.2 Evrenakı'nın Temel Akışkan Denklemi (Zerre Ortamı)

Evrenakı postülası: uzay, sıkıştırılabilir bir süperakışkan (Evrenakı/Zerre ortamı) ile doludur; kütleli cisimler bu ortamda bir yoğunluk/basınç çukuru (potansiyel kuyusu) oluşturur. Ortamın hareketi, sıkıştırılabilir Euler denklemiyle (Euler, 1757) tarif edilir:

$$\rho \left(\frac{\partial \vec{v}}{\partial t} + (\vec{v}\cdot\nabla)\vec{v}\right) = -\nabla P + \rho \vec{g}_{ek}$$

Burada $\rho$ Zerre yoğunluğu, $P$ Zerre basıncı (teorinin tek yoğunluk/basınç çifti; Ek D), $\vec{g}_{ek}$ ise dönme/entrainment kaynaklı ek terimdir (Bölüm 6.3'te tanımlanan spin-pressure, $\nabla P_{spin}$).

Bir kütle kaynağı (Satürn, $M$) etrafında, **durgun/quasi-statik rejimde** ("yavaş sıkıştırma" limiti) denklem basınç dengesine indirgenir; teorinin kuyu konvansiyonu gereği (Bölüm 1.5 ve 3.4.1 ile ortak) kütle bir **basınç çukurudur**, Zerre basıncı kuyudan dışa doğru **yükselir** ($\rho^{-1}\,dP/dr = +GM/r^2 > 0$) ve cismi merkeze iten şey gradyanın yönü değil, itim yasasındaki eksi işarettir: $a_r = -\rho^{-1}\,dP/dr = -GM/r^2$ *(tam türetim: **Ek M-27**)*.

> *İşaret uyarısı:* Bu bağıntı, standart astrofizikteki **gazın** hidrostatik dengesiyle karıştırılmamalıdır. Gaz basıncı merkezde yüksektir ve o alışkanlık $\frac{1}{\rho}\frac{dP}{dr} = -\frac{GM}{r^2}$ işaretini getirir; teorinin kuyu konvansiyonu ise ters işaret verir (3.4.1'deki siklostrofik denge: $dP/dr = +\rho v_\theta^2/r$), ve 3.10.3'ün geri-çağırıcı kuvveti ($F_z = -\rho^{-1}\partial_z P \cdot m$) ancak bu işaretle geri çağırıcı olur — tersiyle itici çıkar. Zerre basıncı ile madde/gaz basıncı **iki ayrı alandır.**

**Bu adım, teorinin rejim aksiyomunun (Bölüm 4.2) doğrudan sonucudur**: güneş sistemi ölçeğinde (galaktik düz-hız girdap rejiminde değil; bkz. 4.2.9.2), Zerre basınç gradyanının büyüklüğü klasik $GM/r^2$'ye eşitlenecek şekilde kalibre edilmiştir. Yani **bu satıra kadar hiçbir yeni fiziksel içerik yok** — sadece Newton yasasının Zerre diliyle yeniden yazımı.

## 3.10.3 Dikey Salınım: Zerre Basıncının z-Bileşeni

Parçacığın düzlemden $z$ kadar saptığı durumda, Zerre basınç gradyanının dikey izdüşümü geri-çağırıcı bir kuvvet üretir ve $z \ll r$ limitinde hareket denklemi, dikey salınım frekansı $\Omega_z$ ile harmonik salınıma iner *(tam türetim: **Ek M-27**)*:

$$\frac{d^2z}{dt^2} + \Omega_z^2 z = 0, \qquad \Omega_z^2 = \frac{GM}{r^3}$$

**Dürüst tespit #1:** Bu denklem, Newton mekaniğinde türetilen denklemin **birebir aynısıdır**. Evrenakı burada matematiksel olarak farklı bir sayı üretmez — çünkü teorinin kendi tasarımı gereği, düşük hız/zayıf alan limitinde (ki Satürn halka parçacıkları tam bu limittedir) $GM/r^2$'ye indirgenmesi bir *aksiyomdur*, bir *keşif* değil. Bu nedenle, **restoring force / dikey salınım periyodu, Evrenakı lehine ayırt edici bir kanıt olarak kullanılamaz** — Newton da, GR de, Evrenakı da burada aynı $\Omega_z$'yi verir.

## 3.10.4 Sönüm Terimi: Burada Gerçek Bir Fark Var mı?

Teorinin akışkanlar mekaniği temelinin **gerçekten** bir şey söyleyebileceği yer burasıdır — çünkü Evrenakı, ortamı bir süperakışkan olarak tanımladığı için, standart granüler-gaz kinetik teorisinden farklı bir sönüm mekanizması önerebilir: **"hidrodinamik hafıza" (entrainment) etkisi.**

### 3.10.4.1 Standart (ana akım) sönüm terimi — karşılaştırma referansı

Ana akım halka fiziğinde sönüm, parçacıklar arası inelastik çarpışmalardan gelir (halka viskozitesinin kinetik teorisi: Goldreich & Tremaine, 1978; yoğunluk dalgalarından yüzey yoğunluğu ve viskozite kestirimi: Hedman & Nicholson, 2016):

$$\gamma_{standart} \sim \Omega_z \cdot \tau_c^{-1} \cdot (1-\epsilon^2)$$

burada $\tau_c$ ortalama çarpışma zamanı, $\epsilon$ ise geri tepme (restitution) katsayısıdır. Bu tamamen **parçacıklar arası** bir etkileşimdir; ortamın (Zerre/uzay) kendisiyle ilgisi yoktur.

### 3.10.4.2 Evrenakı'nın ek terimi: ortam–parçacık artık kuplajı

Evrenakı'nın farkı şurada yatar: Zerre ortamı parçacık–parçacık çarpışmasından **bağımsız**, ortam kaynaklı bir artık kuplaj taşır. Stokes biçiminde:

$$\gamma_{ortam} \sim \frac{6\pi \eta_E r_t}{m} = \frac{9\eta_E}{2\rho_c r_t^{2}}$$

*(katalog: **Ek M-27**, **Ek M-37**; $r_t$ parçacık yarıçapı, $m$ kütlesi, $\rho_c$ yoğunluğu.)*

**Ama bu terim bir "sabit taban" değildir — ve kritik olan da budur.** Ek M-43 artık kuplajı altkritik rejimde kurar ve etkin katsayı evrensel bir akışkan sabiti olmaktan çıkar:

$$\eta_E^{etkin} \propto \frac{r_t\,\Delta v^{4}}{v_{kav}^{3}} \qquad\Longrightarrow\qquad \boxed{\;\gamma_{ortam} \propto \frac{\Delta v^{4}}{r_t}\;}$$

İki sonucu vardır ve ikisi de bu bölümün eski test önerisini geçersiz kılar:

- **Terim parçacık boyutundan bağımsız değildir; boyutla ters orantılıdır** ($\propto1/r_t$). Ana akım çarpışma sönümü de $1/r_t$ ile ölçeklenir. **Boyut ekseni iki modeli ayırmaz.**
- **Terim, bağıl hızın dördüncü kuvvetiyle gider.** Ayrım bu yüzden boyutta değil, **hangi bağıl hızın devrede olduğundadır.**

### 3.10.4.3 Hangi bağıl hız? — dikey ile yörünge kanalı arasında $10^{28}$ fark

Bir halka taneciğinin ortama göre **iki ayrı** bağıl hızı vardır ve $\Delta v^4$ onları acımasızca ayırır:

| Kanal | Ortamın o yöndeki hızı | $\Delta v$ |
|---|---|---|
| **Dikey** (bükülme dalgası, kalınlık) | ortam ekvator düzleminde dolaşır; dikey bileşeni $\approx0$ | $\sigma_z \approx 1{,}7\times10^{-3}$ m/s |
| **Yörünge** (radyal göç) | **DY-2:** ortam maddenin iki katı hızla dolaşır | $v_{madde} \approx 1{,}9\times10^{4}$ m/s |

$$\frac{\gamma_{ortam}^{y\ddot{o}r\ddot{u}nge}}{\gamma_{ortam}^{dikey}} = \left(\frac{v_{madde}}{\sigma_z}\right)^{4} = 1{,}5\times10^{28}$$

Oran parametresizdir — $r_t$ sadeleşir, Phoebe kalibrasyonuna ve $v_{kav}$'a bağlı değildir.

> **Dürüst tespit #2 (düzeltilmiş).** Bu bölümün önerdiği **bükülme dalgası testi yürütülemez.** Dikey kanalda ortam sönümü, çarpışmalı sönümün $\sim10^{31}$ katı gerisindedir; halka kalınlığında ve bükülme dalgası sönüm mesafesinde ölçülebilir bir iz bırakmaz. Ve gerekçe $\eta_E$'nin bilinmemesi değildir — **$\Delta v^4$ çarpanının mm/s'lik dikey hızda çökmesidir.** Boyut-bağımsız taban terimi diye bir şey yoktur.

### 3.10.4.4 Terimin gerçek adresi: yörünge kanalı — ve işareti

Ortam kuplajının fiilen iş yaptığı yer yörünge kanalıdır. Ama orada **işaret** sorulmalıdır ve cevabı tek yönlüdür:

DY-2 gereği ortam her yarıçapta maddeden hızlı dolaşır ($v_{ortam}=2v_{Kepler}$), yani taneciği **önden geçer**; Ek M-37'nin artık kuplajı cismi ortamla eş-dönüşe gevşetmeye çalışır, dolayısıyla kuvvet **prograddır** ve açısal momentumu **artırır**:

$$\boxed{\;\text{Ortamın torku yörüngeyi } \textbf{DIŞA}\text{ taşır.}\;}$$

> **Dürüst tespit #3: halka yağmuru Evrenakı'nın kanalı değildir.** Halka yağmuru **içe** doğrudur, ortamın torku **dışa**. İşaret ters olduğu için teorinin bu olguda ayrışan bir sözü yoktur; ölçülen içe akış standart mekanizmalara aittir (plazma sürüklemesi, mikrometeorit bombardımanı, viskoz yayılma, elektromanyetik güdüm). Bu bir eksiklik değil, bir **muhasebe sınırıdır** — teori kendi kuvvetinin üretmediği bir gözlemi sahiplenemez.
>
> *("Zarf içinde ortam gövdeyle eş-döner, dolayısıyla kayma senkron yarıçapta işaret değiştirir" biçimindeki kaçış yolu da kapalıdır: eş-dönüş bir **dönme** sürüklenmesi iddiasıdır ve Ek M-40'ın $\xi\approx4{,}6\times10^{-10}$'uyla dışlanır. $\phi$ öteleme, $\xi$ dönme kanalıdır; ikisi birbirinin yerine konulamaz.)*

## 3.10.5 Terimin Gerçek Gözlemsel Değeri: $\eta_E$ Üzerine En Sıkı Sınır

Ortam kuplajı halka yağmurunu açıklamaz; ama **prograd torku halkayı dağıtmamış olmalıdır** ve bu, kitaptaki en güçlü $\eta_E$ kısıtını verir. Halka genişliği $\sim7\times10^{7}$ m, ömrü $\sim10^{7}$ yıl; $\dot a = 2\gamma a$ ile:

$$\dot a < 2{,}2\times10^{-7}\ \mathrm{m/s} \;\Longrightarrow\; \gamma_{ortam} < 1{,}0\times10^{-15}\ \mathrm{s^{-1}} \;\Longrightarrow\; \boxed{\;\eta_E \lesssim 2{,}3\times10^{-11}\ \mathrm{Pa\cdot s}\;}$$

**Phoebe'nin retrograd yörüngesinden gelen eski sınırdan ($3{,}3\times10^{-5}$ Pa·s, Ek M-37) $1{,}4\times10^{6}$ kat sıkıdır.** Sebebi $\Delta v^4$ çarpanıdır: sınırı yöneten kombinasyon $\eta_E/(r_t\Delta v^4)$'tür ve hız çarpanı yarıçap çarpanını ezer. **En güçlü sınırı en küçük cisim değil, en hızlı ve en dar yapı verir.**

Bağımsız çapraz denetim: aynı prograd tork Güneş çevresindeki her cisme etki eder; astronomik birimin kararlılığı ($\lesssim0{,}01$–$0{,}1$ m/yıl) $\eta_E\lesssim1{,}5\times10^{-10}$–$1{,}5\times10^{-9}$ Pa·s verir — aynı yönde, 6–60 kat gevşek. *(Tam türetim ve standart mekanizmalardan ayrıştırma: **11.4.8**.)*

**Ve sınırın önemli bir niteliği vardır:** hiçbir standart model sayısını girdi almaz. Ortamın torku dışa, gözlenen akış içe olduğu için bütçe payı bölüşmek gerekmez — koşul yalnız **halkanın var olmasıdır.**

## 3.10.6 Bölüm 6.3 ile Tutarlılık

Bu bölümün $\gamma_{ortam}$ terimi ile Bölüm 6.3'teki frame-dragging, ortamın **aynı sürüklenme mekanizmasından** beslenir; dolayısıyla 6.3'ün nicel durumu buranın da ön koşuluydu.

6.3'ün öngörüsü ile GP-B ölçümü arasındaki iki katlık görünür açıklık **kapanmıştır:** aradaki çarpan, kutupsal yörünge üzerinde alınan geometrik ortalamanın tam olarak $\tfrac12$ olmasıdır ($\langle 3\cos^2\theta\rangle - 1 = \tfrac12$). Yerel sürüklenme hızı 81,9 mas/yıl, kutupsal yörünge ortalaması 41,0 mas/yıl; ölçülen $37{,}2\pm7{,}2$ mas/yıl ile 0,52σ uyum sağlanır (ayrıntı: Bölüm 6.3.3; tam türetim: **Ek M-40**).

**Buradaki sonuç:** dönme sürüklenme kesri gözlemle sabitlenmiştir ($\xi \approx 4{,}6\times10^{-10}$, Ek C). Ama **$\xi$ ile $\phi$ ayrı kanallardır** ve bu bölümün $\gamma_{ortam}$'ı ikisinden de bağımsızdır: o, artık kuplajın altkritik rejimidir (Ek M-43). Üç kanalı karıştırmamak, bu bölümün en kolay hatasıdır.

## 3.10.7 Sonuç: Neyi Gerçekten Söyleyebiliriz?

| İddia | Durum |
|---|---|
| Dikey restoring force / salınım periyodu | Evrenakı = Newton = GR (ayırt edici değil, aksiyom gereği) |
| Parçacık–parçacık sönüm zinciri | Kapısı ve kesiti taneciklerin **pulsasyon rampasıdır** — alan aracılı karşılaşma, kesit $(r_H/a_b)^2$; temaslı çarpışma artığı ısıya çeviren son adımdır. Kalınlık kilidi parametresiz $h\simeq a_b$ (11.4.5) |
| Ortam kuplajının **dikey** kanalı | **Ölçülemez** — rampa+temas zincirinin $10^{31}$ katı gerisinde; bükülme dalgası testi bu kanalla yürütülemez |
| Ortam kuplajının **yörünge** kanalı | **Dışa** dönük tork; halka yağmurunu üretmez ama **$\eta_E$ üzerine kitaptaki en sıkı sınırı** verir ($\lesssim2{,}3\times10^{-11}$ Pa·s) |
| Halka yağmuru (ring rain) kütle kaybı | **Teorinin kanalı değildir** — işaret ters; standart mekanizmalara aittir |
| Halkada teorinin **ayırt edici** imzası | Dikey frekansta **tek paritede** $(R_e/r)^3$ terimi — hiçbir kütle çokkutbuyla taklit edilemez (11.4.4, Sınav 11.4-A) |
| GP-B ile tutarlılık | **Sağlandı** — geometrik çarpan $\tfrac12$, 0,52σ uyum (6.3.3, Ek M-40) |

**En dürüst ve en güçlü konumlandırma şudur:** Evrenakı, halka dinamiğinin dikey salınım kısmında Newton'la matematiksel olarak özdeştir ve bu bir zayıflık değil, tasarım gereğidir. Halkanın dikey sönümünün kapısı ve kesiti taneciklerin **pulsasyon rampasıdır**; temaslı çarpışma artığı yakan son adımdır, dış ortam kuplajı ise o hanede ölçülemez (11.4.5). Teorinin halkalarda kendine özgü iki sözü vardır ve ikisi de niceldir: **(i)** yörünge kanalındaki prograd tork, $\eta_E$'ye kitaptaki en sıkı sınırı koyar; **(ii)** yanal itimin (F5) dikey frekansta bıraktığı **tek pariteli** $(R_e/r)^3$ terimi, hiçbir kütle dağılımının üretemeyeceği bir imzadır ve Cassini verisinde aranabilir. Halka yağmuru bu listede yer almaz.
