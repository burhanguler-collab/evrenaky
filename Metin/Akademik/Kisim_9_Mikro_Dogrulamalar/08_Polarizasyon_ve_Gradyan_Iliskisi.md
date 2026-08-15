# 9.8 Polarizasyon ve Gradyan İlişkisi: Ölçülebilir İmza

Kısım 2 polarizasyonun mekanik zincirini kurmuştu: Zerre, kendi dönüşü nedeniyle kalıcı olarak **basık (disk)** gövdedir ($k_a=1/2$) — "polarizasyon" bu diskin **yönelimidir** (2.4.3); disk, gradyan alanına açılı girdiğinde **basınç torkuyla** hizalanır (2.9.2) ve Malus yasası iki mekanik kesrin çarpımı olarak düşer (2.9.2.1; sınavı 9.7.3'te). Bu bölümün görevi zincirin son halkasıdır: disk yönelimini yöneten **vektörel kanalın** matematik çerçevesini kurmak, bilinen polarizasyon olgularını bu çerçeveye yerleştirmek ve bölümün adını taşıyan şeyi — doğada **ölçülebilir imzayı** — tanımlamak.

> **Kapsam ve tamamlanma notu:** Bu bölüm sınırlı kapsamla yazılmıştır: çerçeve, olguların yerleşimi ve imza öngörüsü. Derin katman — tork katsayısının girdap-disk mekaniğinden türetimi ve imza ölçüm programının raporu (Kısım 5 deney fazı, T-9) — 9.8.5'in açık kalemleri olarak 7.4 envanterine (md. 19) bağlıdır; kalemler kapandığında bölüm genişletilerek **tamamlanacaktır.**

## 9.8.1 Doğrulanacak Gözlem Envanteri

| # | Gözlem | Ölçülen değer / davranış | Kaynak |
|---|---|---|---|
| G-1 | Malus yasası | geçen kesir $\cos^2\theta$; çapraz polarizörde tam söndürme | Malus, 1809 (sınav: 9.7.3) |
| G-2 | Optik aktivite | kiral ortamda polarizasyon düzlemi yol ile **doğrusal** döner (özgül çevirme) | Arago, 1811; Biot, 1815 |
| G-3 | Gerilme çift kırılımı (fotoelastisite) | mekanik gerilme alanı, yöne bağlı hız farkı ve polariskop desenleri üretir | Brewster, 1816 |
| G-4 | Faraday dönmesi | boyuna manyetik alan, düzlemi yol ve alanla orantılı döndürür (Verdet sabiti) | Faraday, 1845 |

Dördünün ortak grameri dikkat çekicidir: hepsinde polarizasyon düzlemi, ortamın **içyapısındaki bir yönlü alanla** orantılı ve yol boyunca **birikimli** biçimde döner. Standart optik her birine ayrı bir bağlaşım sabiti yazar; teoride dördü tek mekanizmanın — disk üzerindeki basınç torkunun — farklı gradyan kaynaklarıyla sürülmüş hâlleridir.

## 9.8.2 Vektörel Kanalın Çerçevesi

Skaler kanal (9.1, 5.3) basıncın **değerini** okur: $c_{yerel}=\sqrt{P/\rho}$. Vektörel kanal basıncın **eğimini** okur: disk normali ile enine gradyan arasındaki açı $\theta$ için, 2.9.2'nin torku diski gradyan çizgilerine hizalamaya zorlar ve yol boyunca birikimli bir yönelim değişimi bırakır. Çerçevenin yapısal yasası budur:

$$\frac{d\theta}{ds} = -\kappa_t\,\big(\nabla_{\!\perp}P\big)_\theta \qquad\Longrightarrow\qquad \Delta\theta = \kappa_t\!\int_{yol}\!\big(\nabla_{\!\perp}P\big)_\theta\, ds$$

Dönme, yol boyu **enine basınç gradyanının integralidir**; $\kappa_t$ (tork katsayısı) diskin atalet ve bağlanım özelliklerini taşıyan tek yeni büyüklüktür — bugün serbest kalemdir (Ek C'ye aday; türetimi 9.8.5/i). İki sınır davranışı çerçeveden bedavaya çıkar: **(a)** gradyana dik gelen disk tork görmez, burkulmadan geçer (5.3/9.1'in kaydettiği seçicilik); **(b)** homojen ortamda $\nabla_{\!\perp}P=0$ → dönme yok — polarizasyonun "durup dururken" dönmemesi varsayım değil, çerçevenin sıfır noktasıdır.

## 9.8.3 Olguların Yerleşimi

| Olgu | Gradyan kaynağı | Çerçevedeki okunuşu | Sonuç |
|---|---|---|---|
| G-1 Malus | polarizörün yapay keskin ızgara gradyanı | tork-hizalanma + geçit; $\cos\theta\times\cos\theta$ | ✅ (9.7.3) |
| G-2 optik aktivite | kiral molekülün **net burulmalı** mikro-gradyan yapısı | her molekül geçişi aynı işaretli küçük $\Delta\theta$ bırakır → yol ile doğrusal birikim | ✅ yapı; özgül çevirmenin molekül yapısından hesabı açık (9.8.5/ii) |
| G-3 fotoelastisite | gerilmenin malzeme içi gradyan haritasını yönlü bozması | zarf anizotropisi (9.1'in K3 kanalı): iki eksende iki $\phi_{etkin}$ → hız farkı + desen | ✅ yapı; gerilme-optik katsayının türetimi açık (9.8.5/iii) |
| G-4 Faraday | mıknatıslanmış ortamın girdap-hizalı içyapısı | boyuna eksen etrafında işaretli burulma; yol ve alanla doğrusal | ✅ yapı; Verdet sabitinin türetimi açık (9.8.5/v) |

Simetri kaydı çerçevenin lehinedir: optik aktivitede dönme yönü ışığın gidiş yönünden **bağımsızdır** (geri dönen ışık dönmeyi geri sarar), Faraday'da ise yön **alana kilitlidir** (geri dönen ışık dönmeyi ikiye katlar). Teoride bu ayrım doğaldır: kiral gradyan yapıya (moleküle) aittir ve ışıkla birlikte "ters okunur"; mıknatıs gradyanı dış eksene kilitlidir ve okunuş yönünden bağımsızdır. Standart optiğin iki ayrı fenomenolojisi, tek tork yasasının iki kaynak-simetrisidir.

### 9.8.3.1 Standart Yorumun İç Kilidi: Polarizasyon ile Yerleşiklik Aynı Anda İstenemez

Standart çatının polarizasyon okuması, taşıyıcıya iki niteliği birlikte yükler: nesnenin bir **polarizasyon durumu** vardır ve nesne polarizörde bir **yerde** bulunur. Bu bölümün kaydetmesi gereken tespit, iki niteliğin standart fiziğin kendi teoreminde birbirini dışladığıdır.

Newton–Wigner yerelleştirilebilirlik sonucunun teknik içeriği şudur: konum operatörü, **kütlesiz ve spini 1/2'den büyük** parçacıklar için tanımlanamaz (9.10.5/a). Yasağın fiziksel nedeni de bellidir: kütlesiz spin-1 taşıyıcının, spininin izin verdiği bütün helisite modları yoktur — boyuna mod eksiktir — ve bu eksiklik onu daima yayılmış kılar. Buradaki "helisite yapısı", ışığın **polarizasyonunun kendisidir**.

Sonuç tek cümlede toplanır: **standart çatı, ışığın polarize olabilmesi için ödediği bedeli, ışığın bir yerde bulunabilmesiyle ödemektedir.** Malus yasasının tekil-olay okuması ("tek fotonun polarizasyon durumu geçme olasılığını verir") bu nedenle hem öznesini kaybeder — o tek foton üretilemez (9.10.6) — hem de kendi içinde tutarsızlaşır: polarizasyonu olan şey, polarizör düzleminde bir noktada bulunamaz.

Teorinin disk–tork mekaniği bu kilitten muaftır ve muafiyetin nedeni yapısaldır: **polarizasyonun taşıyıcısı kütlesiz bir soyutlama değil, kütleli ve yerleşik bir Zerre diskidir.** Disk bir yerdedir, yönelimi vardır, torku hesaplanabilir ve geçişi ölçülebilir bir gecikme imzası bırakır (9.7.3; ölçüm önerisi 9.7.6/iii). Yani standart okumanın çelişki ürettiği yerde teori, aynı olguyu tek bir mekanik büyüklükle — disk yönelimiyle — taşır.

## 9.8.4 Ölçülebilir İmza: Türev Kilidi

Bölümün adını taşıyan imza, 5.3 ile bu bölümün kesişiminde durur. Kütle-içi Evrenakı gradyanı **tek alandır** ($P(r)$) ve ışığa iki dik kanaldan dokunur: skaler kanal değerini okur (5.3'ün ölçtüğü merkez-simetrik saçak kemeri), vektörel kanal eğimini okur (bu bölümün $\Delta\theta$'sı). Tek alandan iki okuma, aralarına pazarlıksız bir kilit koyar:

$$\Delta\theta(x)\;\propto\;\frac{d}{dx}\Big[\text{saçak profili}(x)\Big]$$

**Öngörünün keskin biçimi:** 5.3'ün kemer profili merkez-simetrikse, aynı numunenin polarimetrik taramasında dönme profili zorunlu olarak **antisimetriktir** — tam merkezde sıfır, iki yanda zıt işaretli, S-biçimli; genliği $\kappa_t$'ye bağlı, **biçimi parametresizdir.** Hiçbir deneysel artefakt iki ayrı gözlenebilir arasında türev ilişkisini tesadüfen üretemez; kilit doğrulanırsa iki kanal tek alana perçinlenir, saçak kemerinin gradyan-dışı açıklamaları da (numune kusuru sınıfı) toplu hâlde elenir. Aynı ölçüm $\kappa_t$'yi ilk kez sayıya bağlar; iz çıkmazsa da sonuç bilgi vericidir — gerilmesi giderilmiş numunede vektörel izin yokluğu, skaler kanalda 1,8 saçak dururken, $\kappa_t$'ye doğrudan bir **üst sınır** koyar ve 9.8.5/i'nin türetimini iki uçtan kıstırır. Ölçüm programı Kısım 5'in kütle-içi düzeneğinin (5.3) polarimetrik uzantısıdır; protokol ve rapor, deney fazının (T-9) kalemidir.

## 9.8.5 Açık Kalemler

Tümü 7.4 envanterine (md. 19) bağlanır; bölüm bu kalemler kapandığında genişletilecektir:

i. **$\kappa_t$'nin türetimi:** tork katsayısının disk atalet momenti ve gradyan bağlanımından ilk-ilke hesabı; türev-kilidi ölçümü (9.8.4) ve polariskop sınırıyla iki uçtan kıstırılması.
ii. **Özgül çevirme:** kiral molekülün mikro-gradyan burulmasından, ölçülen çevirme güçlerinin (ör. kuvars, şeker çözeltisi) hesabı.
iii. **Gerilme-optik katsayı:** fotoelastik sabitlerin zarf-anizotropisi (9.1/K3) üzerinden türetimi.
iv. **Türev-kilidi ölçümü ve raporu:** 5.3 düzeneğinin polarimetrik taraması — antisimetri, sıfır-geçiş konumu, genlik (T-9 deney fazı).
v. **Faraday/Verdet:** mıknatıslanmış ortam gradyanının tork yasasına bağlanması ve Verdet sabitinin malzeme sistematiği.
vi. **Şerit değişimi:** 2.9'un vektörel anlatımıyla 5.3'ün skaler ölçümünün tek formel çatıda (bu bölümün çerçevesi) birleştirilmesinin 9.1–9.8 çapraz atıflarla kapanışı.

---

**Bölüm özeti:** Polarizasyonun bütün "tuhaflıkları" teoride tek yasaya iner: disk yönelimi, yol boyu enine basınç gradyanının integraliyle döner ($\Delta\theta=\kappa_t\!\int(\nabla_{\!\perp}P)\,ds$). Standart yorumun bu arenadaki iç kilidi ayrıca kaydedilmiştir: kütlesiz spin-1 taşıyıcıyı yerleşemez kılan şey tam da onun helisite yapısı, yani polarizasyonun kendisidir — polarizasyon ile yerleşiklik aynı nesneden aynı anda istenemez (9.8.3.1); teorinin disk mekaniği bu kilitten muaftır, çünkü polarizasyonun taşıyıcısı kütleli ve yerleşik bir Zerre diskidir. Malus polarizörün yapay gradyanı, optik aktivite kiral mikro-gradyan, fotoelastisite gerilmenin bozduğu gradyan haritası, Faraday mıknatıs-kilitli gradyan — dördü aynı tork yasasının dört kaynağıdır ve yön-simetri ayrımları (aktivite ↔ Faraday) çerçeveden bedavaya çıkar. Bölümün ölçülebilir imzası **türev kilididir**: kütle-içi gradyanın skaler okuması (5.3'ün saçak kemeri) ile vektörel okuması (antisimetrik dönme profili) tek alana kilitlidir — biçimi parametresiz, genliği $\kappa_t$'yi sayıya bağlayan, artefaktla taklit edilemez bir çapraz öngörü. Ölçüm programı ve derin katman 7.4/T-9'a bağlıdır; **bölüm o kalemler kapandığında tamamlanacaktır.**
