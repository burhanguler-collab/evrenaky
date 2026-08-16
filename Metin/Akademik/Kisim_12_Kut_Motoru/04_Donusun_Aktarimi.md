# 12.4 Dönüşün Aktarımı: Kut'tan Yapıya

Bu bölüm Kısım 12'nin — ve bütün kitabın — **omurgasıdır.**

Buraya kadar iki ayrı şey kuruldu: Kut'un kendisi 4B'de dönüyor (12.2), ve Kutlar bir araya gelip yapı kuruyor (12.3). Ama arada duran ve **hiç sorulmamış** bir soru var:

> **Kut'un dönüşü, kurduğu yapıya nasıl geçiyor?**

Bu soru cevapsız kalırsa, kitabın ana iddiası havada kalır. *"Evrendeki bütün hareket Kut dinamiğinden gelir"* demek, ancak Kut'un dönüşünün üst katmanlara **taşındığı** gösterilebilirse anlamlıdır. Aksi hâlde elimizde iki bağımsız olgu olur: dönen Kutlar, ve bir de dönen gezegenler — aralarında hiçbir bağ olmadan.

Bu bölüm o bağı kurar ve **sayıyla** kurar.

---

## 12.4.1 Aktarımın Taşıyıcısı: Dolanım Toplanabilirdir

Aktarım mümkündür çünkü taşınan büyüklük **toplanabilir** ve **korunur**.

Kelvin dolanım teoremi gereği, bir akışkanda kapalı bir eğri boyunca dolanım

$$\Gamma = \oint \vec v \cdot d\vec\ell$$

korunur. (Bu teorem artık dışarıdan devralınan bir sonuç da değildir: birleşik eylemde parçacık yeniden-etiketleme simetrisinin Noether yüküdür — Ek M-50.) Ve birden çok girdabı çevreleyen bir eğri için dolanım, içerdiği girdapların dolanımlarının **toplamıdır**:

$$\boxed{\;\Gamma_{\text{top}} = \sum_i \Gamma_i\;}$$

Bu, aktarımın bütün mekanizmasıdır. Kut'un dönüşü yapıya "aktarılmaz" — yapının dönüşü zaten Kutların dönüşünün **toplamıdır**. Ayrı bir taşıyıcıya, ayrı bir kuvvete, ayrı bir kanala gerek yoktur.

Bu, 12.3.7'de ölçülen sonucun da kaynağıdır: bir Kutam uzaktan tek girdap gibi görünür ve dolanımı $\Gamma_{\text{top}}$'tur; bileşik sınır tabakası yarıçapı $r_e(\text{Kutam}) = |\sum g|\,r_e$ olur.

**Ve korunum olaylarda da tutar.** Simülasyonda ölçüldü:

| Olay | $\Gamma$ öncesi | $\Gamma$ sonrası |
|---|---|---|
| Birleşme (eş çift) | $1 + 1$ | $2$ |
| Yok olma (zıt çift) | $+1 - 1 = 0$ | $0$ (ortama) |
| 44 Kut, uzun koşum | $44$ | **$44$ tam** |

---

## 12.4.2 İki Açısal Hız, İki Farklı İş

4B çift dönüşün iki açısal hızı vardır ve **ikisi tamamen farklı işler yapar.** Bu ayrım, bu bölümün anahtarıdır.

| | Nerede döner | 3B'de görünüşü | Yaptığı iş |
|---|---|---|---|
| $\omega_1$ | Kesitimizin **içindeki** düzlem | **Doğrudan dönme** | Yapıya aktarılan dönüş |
| $\omega_2$ | $W$'yi içeren düzlem | **Pulsasyon** (İmza 1) | Bağı kuran şey |

**$\omega_1$ görünür ve toplanır.** Kesitimizin içindeki düzlemde döndüğü için doğrudan dolanım olarak görünür, ve dolanım toplanabilir olduğu için yapıya geçer.

**$\omega_2$ görünmez ama yapıyı mümkün kılar.** $W$ doğrultusunda döndüğü için 3B'de dönme olarak görünmez; görünen şey Kut'un kesitimizdeki yarıçapının salınmasıdır — pulsasyon. Ve 12.3.2'de gösterildiği gibi, **bağı kuran şey tam olarak bu pulsasyondur** (ikincil Bjerknes kuvveti).

> **İki kanalın birlikte anlamı budur:** $\omega_2$ Kutları **bir araya getirir**, $\omega_1$ o birlikteliğe **dönüşünü verir**. Biri olmadan öteki işe yaramaz — bağsız bir dolanım toplamı yoktur, dönüşsüz bir bağ da ölü bir yığındır.

### Faz uyumu neden kendiliğinden geliyor

Bjerknes kuvveti ancak **aynı fazda** pulsasyon yapan kaviteler arasında çekicidir; zıt fazda iticidir. Rastgele fazlı bir toplulukta ortalama kuvvet sıfıra yakın olurdu ve hiçbir yapı kurulamazdı.

Burada ince bir nokta vardır ve açıkça söylenmelidir: **aynı frekans, tek başına aynı fazı garanti etmez** — $\phi_i(t)=\omega_2t+\phi_{i0}$ yazımında başlangıç fazları serbest kalabilirdi. Teori bu boşluğu frekans ortaklığıyla değil, daha güçlü bir hükümle kapatır (12.0.4): Kutlar bağımsız osilatörler değil, **tek bir küresel 4B dönüşün yerel kesitleridir.** Ortak olan dönüşün kendisidir; dolayısıyla $\phi_{i0}$ diye bağımsız bir serbestlik yoktur. Faz uyumu bir varsayım değil, kurucu hükmün zorunlu sonucudur.

Bu, teorinin en az fark edilen ama en güçlü iç tutarlılıklarından biridir: **yapının var olabilmesi için gereken faz uyumunu, yapının dönüşünü sağlayan aynı mekanizma üretiyor.**

---

## 12.4.3 Yapının Dönüşü Türetilir — ve Tam Tutar

Şimdi ölçüme geliyoruz. $N$ Kut'luk düzgün bir halka, üyelerinin dolanımından türetilen bir hızla döner:

$$\boxed{\;\Omega_N = \frac{\Gamma\,(N-1)}{4\pi R^2}\;}$$

Bu bir varsayım değil, nokta girdap dinamiğinin sonucudur. Sınandı — $R = 1{,}5$, saf girdap kipinde:

| $N$ | $\Omega$ ölçülen | $\Omega$ öngörülen | **Bağıl fark** |
|---|---|---|---|
| 2 | 0,31427 | 0,31427 | **%0,0000** |
| 3 | 0,62854 | 0,62854 | **%0,0000** |
| 4 | 0,94281 | 0,94281 | **%0,0000** |
| 5 | 1,25708 | 1,25708 | **%0,0000** |
| 6 | 1,57135 | 1,57135 | **%0,0000** |
| 7 | 1,88562 | 1,88562 | **%0,0000** |
| 8 | 2,19989 | 2,19989 | **%0,0000** |

**Yedi ayrı yapı, yedi tam isabet.** Yapının dönüşü, üyelerinin dönüşünden hesaplanabiliyor.

Merkeze bir Kut konursa formül genişler ve o Kut da katkısını verir:

$$\Omega = \frac{\Gamma(N-1)}{4\pi R^2} + \frac{g_c\,\Gamma}{2\pi R^2}$$

Merkezdeki Kut'un işareti önemlidir: eş yönlüyse yapının dönüşünü **hızlandırır**, ters yönlüyse **yavaşlatır** ve $g_c < -(N-1)/2$ olduğunda yapının dönme yönünü **tersine çevirir**. Bu da simülasyonun öz-sınamalarında kilitlidir.

---

## 12.4.4 Aktarım Doğrusaldır: $\Omega \propto \Gamma$

Aktarımın en yalın sınavı şudur: üyelerin dolanımı katlanırsa, yapının dönüşü de katlanır mı?

$N = 6$, $R = 1{,}5$ sabit tutulup yalnız $g$ değiştirildi:

| $g$ | $\Gamma_{\text{top}}$ | $\Omega$ | $\Omega/g$ |
|---|---|---|---|
| 0,5 | 26,66 | 0,78567 | **1,57135** |
| 1 | 53,31 | 1,57135 | **1,57135** |
| 2 | 106,63 | 3,14270 | **1,57135** |
| 3 | 159,94 | 4,71405 | **1,57135** |

**Oran altı hanede sabit.** Aktarım tam doğrusaldır:

$$\Omega_{\text{yapı}} \;\propto\; \Gamma_{\text{üye}}$$

Bu, "yapı kendi dönüşünü bir yerden alıyor" ifadesinin sayısal karşılığıdır. Yapının dönüşü **bağımsız bir serbestlik derecesi değildir** — üyelerin dolanımının doğrudan görüntüsüdür.

---

## 12.4.5 Bir Kat Yukarı: Yörünge de Aynı Yasadan

Aktarım tek katta durmuyor. İki **Kutam** birbirinin etrafında dönerken de aynı yasa işliyor:

$$\boxed{\;\Omega_{\text{yörünge}} = \frac{\Gamma_A + \Gamma_B}{2\pi d^2}\;}$$

Merkezleri $d = 30$ uzakta iki Kutam, saf girdap kipinde:

| $N_A$–$N_B$ | $\Gamma_A$ | $\Gamma_B$ | $\Omega$ ölçülen | $\Omega$ öngörülen | Fark |
|---|---|---|---|---|---|
| 1–1 | 8,89 | 8,89 | $3{,}1427\times10^{-3}$ | $3{,}1427\times10^{-3}$ | **%0,000** |
| 2–2 | 17,77 | 17,77 | $6{,}28554\times10^{-3}$ | $6{,}28539\times10^{-3}$ | %0,002 |
| 3–3 | 26,66 | 26,66 | $9{,}42809\times10^{-3}$ | $9{,}42809\times10^{-3}$ | **%0,000** |
| 2–4 | 17,77 | 35,54 | $9{,}4282\times10^{-3}$ | $9{,}42809\times10^{-3}$ | %0,001 |
| 3–6 | 26,66 | 53,31 | $1{,}41421\times10^{-2}$ | $1{,}41421\times10^{-2}$ | **%0,000** |

**Ve iki formül aslında tek formüldür.** $N=2$ için halka yarıçapı $R$, ayrım $d = 2R$:

$$\Omega_{\text{yörünge}} = \frac{2\Gamma}{2\pi(2R)^2} = \frac{\Gamma}{4\pi R^2} = \Omega_{N=2} \quad\checkmark$$

Kutam içi dönüş ile Kutamlar arası yörünge, **aynı yasanın iki okumasıdır.**

### Yörünge, dolanımın dağılımına kördür

Tablodaki en öğretici satır çifti şudur:

| | $\Gamma_A$ | $\Gamma_B$ | Toplam | $\Omega$ |
|---|---|---|---|---|
| 3–3 | 26,66 | 26,66 | 53,31 | $9{,}42809\times10^{-3}$ |
| 2–4 | 17,77 | 35,54 | 53,31 | $9{,}4282\times10^{-3}$ |

**Dengeli 3–3 ile dengesiz 2–4, aynı yörünge hızını veriyor.** Yörünge, dolanımın taraflar arasında nasıl paylaşıldığını umursamıyor — yalnız **toplamını** görüyor.

Bu, 12.3.7'deki "uzak alan iç dizilime kördür" sonucunun dinamik karşılığıdır ve
12.5'teki ölçek değişmezliği için gerekli koşullardan biridir: her katman, bir alt
katmanın dolaşım alanını yalnız $\Gamma_{\text{top}}$ olarak görür. Denge aralığının
da doğrusal ölçeklenmesi ayrıca gecikmeli yanıtların öz-benzer kalmasını gerektirir.

---

## 12.4.6 İmpuls da Aktarılır

Dönüş tek başına aktarılmıyor; hareketin öteki iki büyüklüğü de aktarılıyor.

| Büyüklük | İfade | Durum |
|---|---|---|
| Doğrusal impuls | $\vec I = \sum_i \Gamma_i\,(y_i,\,-x_i)$ | Korunur |
| Açısal impuls | $A = \sum_i g_i\,\lvert P_i\rvert^2$ | Korunur |
| Hamiltonyen | $H = -\sum_{i<j} g_ig_j\ln r_{ij}$ | Saf girdapta korunur |

İkisi de simülasyonda kilitli sınamalardır — karışık işaretli topluluklarda dahi.

**Bunun anlamı:** Kutlar bağ kurup bir yapı oluşturduğunda, yapı üyelerinin doğrusal ve açısal impulsunu **devralır**. Yapı ne kadar hızlı ötelenir, ne kadar hızlı döner — hepsi üyelerin getirdiğiyle belirlenir.

---

## 12.4.7 Zincirin Tamamı

Şimdi bütün halkaları sırayla dizebiliriz. Bu, kitabın ana iddiasının tam gösterimidir:

**1.** 4B'de bir çift dönüş vardır — $\omega_1$ ve $\omega_2$. *(Kaynağı bilinmiyor, beyan edildi — 12.1.5.)*

**2.** $\omega_2$, 3B kesitimizde **pulsasyon** olarak görünür (İmza 1) ve bütün Kutlar aynı 4B dönüşün parçası olduğu için **ortaktır**.

**3.** Ortak $\omega_2$ ⟹ faz uyumu ⟹ ikincil Bjerknes kuvveti **çekicidir** ⟹ Kutlar bağ kurabilir. *(12.3.2)*

**4.** Bağ, gecikmeli Bjerknes torku ile ışıma torkunun dengesinde kilitlenir.
$d_e=(\lambda K^5/\kappa)^{1/3}$ indirgenmiş modelin köküdür; temel aralık ve gerçek
yörünge hızı iki bağlı Green–Magnus denkleminden birlikte çıkar. *(12.3.4)*

**5.** $\omega_1$, dolanım olarak görünür ve dolanım **toplanabilirdir**: $\Gamma_{\text{top}} = \sum\Gamma_i$. *(12.4.1)*

**6.** Yapının dönüşü bu toplamdan **türetilir**: $\Omega_N = \Gamma(N-1)/4\pi R^2$ — yedi yapıda %0,0000 sapma. *(12.4.3)*

**7.** Aktarım **doğrusaldır**: $\Omega \propto \Gamma$ — altı hanede sabit oran. *(12.4.4)*

**8.** Yapılar birbirinin etrafında **aynı yasayla** döner: $\Omega_{\text{yörünge}} = (\Gamma_A+\Gamma_B)/2\pi d^2$ — beş çiftte %0,002'nin altında. *(12.4.5)*

**9.** Her katman bir alt katmanı yalnız $\Gamma_{\text{top}}$ olarak görür ⟹ yasa katman değiştirmez, yalnız birim değişir. *(12.5)*

Zincirin sonucu:

> **Bir gezegenin ekseni etrafındaki dönüşü, bir yıldızın dönüşü, bir Zerre'nin spini ve iki gövdenin ortak yörüngesi — dördü de aynı denklemin farklı $\Gamma$ değerlerindeki okumalarıdır. Hepsi Kut'un 4B dönüşüne dayanır.**

Ve bu yüzden hiçbiri tesadüfi değildir. Tesadüfi olan tek şey, **hangi** Kutların bir araya geldiğidir. Bir araya geldikten sonra ne kadar hızlı döneceklerini yasa belirler — ve o yasa, tek bir Kut için yazılmış olanın ta kendisidir.

---

## 12.4.8 Bu Bölüm Neyi Kanıtlamaz

Dürüstlük kaydı, iddianın ağırlığıyla orantılı olmalıdır.

**Kanıtlanan:** *Eğer* Kutlar dolanım taşıyorsa ve bağ kurabiliyorsa, kurdukları yapının dönüşü üyelerinkinden **tam olarak** hesaplanabilir. Aktarım gerçektir, doğrusaldır ve katmanlar boyunca aynı yasayla ilerler.

**Kanıtlanmayan:**

| | Durum |
|---|---|
| 4B çift dönüşün varlığı | Varsayım. 12.2.5'te açıkça yazıldı. |
| $\omega_1$ ve $\omega_2$'nin sayısal değerleri | Serbest. Teori oranlarını değil, yalnız yapısal rollerini belirliyor. |
| İlk dönmenin kaynağı | Bilinmiyor, beyan edildi. |
| $\Gamma$'nın niceliklenmiş olup olmadığı | Bu kısımda ele alınmadı. Sürekli varsayıldı. |

Özellikle sonuncusu önemlidir: eğer dolanım niceliklenmişse (süperakışkanlarda olduğu gibi), $\Gamma_{\text{top}} = \sum\Gamma_i$ bir **tamsayı toplamına** dönüşür ve yapılar kesikli dönüş değerleri alır. Bu, teoriyi kuantumlaşmaya bağlayacak doğal köprüdür — ama **bu kitapta kurulmamıştır.**

<p style="margin:20px 0;padding:16px;border:1px solid #22c55e;border-radius:10px;background:rgba(34,197,94,0.07)"><a href="Simulasyon/kisim12/kut_birlesme_yapilanma.html" target="_blank" rel="noopener" style="display:inline-block;padding:12px 22px;background:#166534;color:#ffffff;border-radius:8px;font-weight:700;text-decoration:none;font-size:1.05em">&#9654;&#65039; SİMÜLASYONU AÇ — aktarımı canlı ölçün</a><br><span style="color:#a1a1aa;font-size:0.9em;display:inline-block;margin-top:8px">Bu bölümdeki her sayı bu simülasyonda yeniden üretilebilir. <b>Hazır dizilim</b> menüsünden $N$ seçilip halka kurulur; alt bilgi çubuğu <b>yapının Ω</b> değerini canlı gösterir ve Thomson öngörüsüyle karşılaştırır. <b>Dolanım şiddeti</b> sürgüsü $g$'yi değiştirir — Ω'nın orantılı katlandığı doğrudan izlenir. Merkeze Kut eklenip işaretinin yapının dönüşünü hızlandırdığı, yavaşlattığı ya da <b>tersine çevirdiği</b> denenebilir. Sağ paneldeki <b>Korunum sapması</b> satırı $\vec I$, $A$ ve $H$'yi sürekli denetler. Tek dosya, dış bağımlılık yok.</span></p>
