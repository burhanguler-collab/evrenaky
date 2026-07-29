# Ek M — Merkezî Türetim Kataloğu · Blok I: Hâl Denklemi ve Eylem İlkesi

Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.

**Blokun kapsamı.** Teorinin en büyük yapısal açığı, beş kuvvetin ve ölçek yapısının **tek bir eylem ilkesinden** türetilmemiş olmasıdır: her biri ayrı bir ansatz'la kurulur, iç tutarlılık ancak elle denetlenebilir ve korunum yasaları türetilemez. Bu blok o programın ilk adımıdır: ortamın hâl denklemini belirler, oradan akışkan eylemini yazar, ve eylemin nereye kadar gittiğini — daha önemlisi **nerede tıkandığını** — kaydeder.

---

## M-44 · Ortamın İki Değişkenli Hâl Denklemi ve Akışkan Eylemi · **[T]**

**Kullanıldığı bölümler:** Ek B.3 ($k$'nın anlamı ve değeri), 2.4.2 (Yön Kuralı), 7.4 md.14. Bağlı katalog: M-1 (Kavrama Yasası), M-3 ($\sqrt2c$), M-7/M-8 ($P_0$), M-9 (kararlılık), M-15 (G2 deplasman aksiyomu), M-30 (galaktik profil varsayımı).

### Sorunun kurulumu: iki ifade bir arada duramıyordu

Teori iki şeyi birden söylüyordu ve tek sembolle yazıldıkları için çeliştikleri görünmüyordu:

- **(A)** "Basınç salınımları $c$ ile yayılır" (M-5, M-13) — GW170817'nin gerektirdiği.
- **(B)** "Kütle yakınında $\delta\rho/\rho_0=k\,\delta P/P_0$, $k<1$" (Ek B.3) — Yön Kuralı'nın dayanağı.

Newton–Laplace bağıntısı ($v_{ses}^2=dP/d\rho$) altında bu ikisi tek bir hâl denkleminden çıkarılmaya çalışılırsa ancak $k=1$'de bir arada durur; $k=1$ ise $P_0=\frac{1-k}{4}\rho_nc^2\to0$ demektir ve M-7'nin yırtılmama tabanını ($1{,}6\times10^{25}$ Pa) altı buçuk mertebe ihlal eder.

Çelişki fizikte değil, **muhasebededir**: iki farklı sürecin katsayısı aynı harfle yazılmıştı.

### Varsayımlar

1. Kavrama Yasası'nın oran biçimi geçerlidir: $c^2=P/\rho$ (M-1).
2. Ortamın durumu **iki bağımsız değişkenle** tanımlanır: yoğunluk $\rho$ ve maddenin doğurduğu **deplasman alanı** $\chi$. Nükleonlar $\chi$'nin kaynağıdır; $\chi$ kütlenin dışında da sıfır değildir (kütle-itim kuyusunun kendisi $\chi$ alanıdır).
3. Akış dönüsüzdür ($\vec v=\nabla\varphi$) — eylemin en dar biçimi; genişletme Açık Uçlar'dadır.

### Adımlar

**1. İki değişken, iki kısmi türev.** Hâl denklemi $P=P(\rho,\chi)$ biçimindedir ve iki bağımsız tepki katsayısı taşır. Bunlar farklı fiziksel süreçleri tanımlar ve karıştırılamaz:

$$\left(\frac{\partial P}{\partial\rho}\right)_{\chi} \qquad\text{ve}\qquad \left(\frac{\partial P}{\partial\chi}\right)_{\rho}$$

Bu yapı, sıradan bir akışkanın $P=P(\rho,S)$ yapısının birebir karşılığıdır: ses dalgaları sabit entropide ilerler, ısıtma ise sabit yoğunlukta basıncı değiştirir. Newton'un ses hızını %22 yanlış hesaplaması, tam olarak iki kısmi türevin karıştırılmasından doğmuştu.

**2. Dalga kanalı — ortam stifftir, ses hızı tam $c$.** Sabit deplasman alanında ($\chi$ donmuş; dalga periyodu deplasmanın kurulma süresinden çok kısa) hâl denklemi Kavrama Yasası'nın kendisidir:

$$P=c^2\rho \qquad\Longrightarrow\qquad \left(\frac{\partial P}{\partial\rho}\right)_\chi=c^2 \qquad\Longrightarrow\qquad \boxed{\;v_{ses}=c\ \text{ tam olarak}\;}$$

Bu, **stiff (Zel'dovich) akışkan** hâl denklemidir: ses hızının ışık hızına *tam eşit* olduğu, nedensel olarak en katı hâl. M-1'in kutulu sonucundaki $\rho_0=P_0/c^2$ bu denklemin ta kendisidir. Sonucu: **kütleçekim dalgası hızı kısıtı otomatik sağlanır.**

**3. Deplasman kanalı — $k=0$.** Madde ortamı dışlar; bu süreç yoğunluğu değil basıncı değiştirir. Teori bunu iki ayrı yerde zaten söyler:

| Kaynak | İfade |
|---|---|
| **M-15, G2 aksiyomu** | Madde içinde $\bar P_m=P_0(1-\phi)$ ama $\bar\rho_m=\rho_0$ — *"hacimce ortalama yoğunluk sabittir, korunum"* |
| **M-30, Varsayım 1** | *"Gradyanlarda asıl değişen basınçtır"*; yoğunluk yaklaşık sabit |

Bu, Ek B.3'ün parametrizasyonunda tek bir değere karşılık gelir:

$$\frac{\delta\rho}{\rho_0}=0 \qquad\Longrightarrow\qquad \boxed{\;k=0\;}$$

**$k$ serbest parametre değildir.** Değeri, G2 aksiyomu ile M-30'un profil varsayımından belirlenir; ikisi bağımsız olarak aynı sonucu verir.

**4. Yön Kuralı maksimum tepkiyle çalışır.** $k=0$ ile

$$\frac{\delta c}{c}=\frac{1}{2}\left(\frac{\delta P}{P_0}-\frac{\delta\rho}{\rho_0}\right)=\frac{1}{2}\,\frac{\delta P}{P_0}$$

Kütleye yaklaşırken $\delta P<0$ olduğundan $\delta c<0$: ışık zorunlu olarak yavaşlar ✓, ve katsayı olabilecek **en büyük** değerdedir ($\tfrac12$).

**5. Arka plan basıncı sabitlenir.** M-8'in zinciri $k=0$ ile kapanır:

$$P_0=\frac{1-k}{4}\rho_nc^2 \;\overset{k=0}{=}\; \frac{1}{4}\rho_nc^2 = 6{,}07\times10^{33}\ \text{Pa}\,,\qquad \rho_0=\frac{\rho_n}{4}=6{,}8\times10^{16}\ \text{kg/m}^3$$

**6. Akışkan eylemi.** Stiff hâl denklemiyle ($u(\rho)=\tfrac12 c^2\rho$ mertebesinde, sabit $\chi$'de) eylem:

$$S=\int dt\,d^{3}x\left[-\rho\left(\partial_t\varphi+\tfrac12(\nabla\varphi)^{2}\right)-u(\rho,\chi)\right]$$

Varyasyonlar teorinin iki temel denklemini verir:

- $\delta S/\delta\varphi=0\;\Rightarrow\;\partial_t\rho+\nabla\cdot(\rho\nabla\varphi)=0$ — **süreklilik**
- $\delta S/\delta\rho=0\;\Rightarrow\;\partial_t\varphi+\tfrac12(\nabla\varphi)^2+h(\rho,\chi)=0$ — **Bernoulli**

**7. M-9'un kararlılık sonucu türetilmiş olur.** Sabit $\chi$'de $(\partial P/\partial\rho)=c^2>0$ olduğundan homojen arka plan çöküşe karşı kararlıdır ve yoğunluk pürüzleri **$c$ hızında** dağılır — M-9'un metninde yazan sonucun kendisi. Ayrıca ağırlıksızlık, eylemde ortamın öz-kütleçekim teriminin **bulunmaması** olarak görünür: "Poisson'u reddediyoruz" bir red olmaktan çıkıp yazılı bir seçime dönüşür.

### Sonuç

$$\boxed{\;P=P(\rho,\chi)\;;\qquad \left(\frac{\partial P}{\partial\rho}\right)_\chi=c^2\ \Rightarrow\ v_{ses}=c\;;\qquad k\equiv\left.\frac{\delta\rho/\rho_0}{\delta P/P_0}\right|_{\text{deplasman}}=0\;}$$

| Kısıt | Hangi kanal | Durum |
|---|---|---|
| GW170817 ($\lvert\Delta v\rvert/v<4{,}2\times10^{-16}$) | dalga | ✓ **otomatik** — stiff hâl denklemi |
| Işık bükülmesi $1{,}7512''$ | deplasman | ✓ maksimum tepki ($k=0$) |
| M-7 yırtılmama tabanı | $P_0$ | ✓ $3{,}8\times10^{8}$ kat marj |
| Yön Kuralı ($\delta c<0$) | deplasman | ✓ |

**Parametre envanterine etkisi:** $k$ serbest skaler listesinden **çıkar** (Ek C satır 3, [F] → [T]). Dürüst sayım 6 skalerden **5**'e iner.

### Geçerlilik Sınırı — eylemin *vermediği* şeyler

Bu blok, programın tamamlandığını değil **başladığını** kaydeder. Yukarıdaki yapı dört şeyi vermez:

1. **Kütle-itimin $1/r^2$'si çıkmaz.** Statik limitte Bernoulli cebirseldir; barotropik bir akışkan eyleminde statik basınç kuyularının $1/r$ kuyruğu yoktur. $\chi$ alanının **neden $1/r$ ile yayıldığı** — yani deplasman alanının kendi denkleminin ne olduğu — eylemde henüz yoktur. **Bloğun en büyük açık ucudur.**
2. **İki kısmi türevin ortak mikro-modeli yoktur.** Adiyabatik tepkinin neden tam stiff, deplasmanın neden tam yoğunluk-korumalı olduğu ayrı ayrı ifade düzeyindedir; ikisini tek bir mikro-yapıdan (nükleonun vakum cepli girdap yapısı) türetmek yapılmamıştır.
3. **$\omega_1/\omega_2$ çift dönüşü temsil edilemez.** Skaler $\varphi$, $\rho$, $\chi$ ile 4B çift dönüş yazılamaz; beş kuvvetin köken haritası eylemin dışındadır. 4B genişletme ya da bir yönelim/direktör alanı gerekir.
4. **$\Lambda$ ölçeklemesi çıkmaz.** Cetvellerin ve saatlerin neden tam $\Lambda$ ile ölçeklendiği (M-42'nin $\gamma_\ell=-1$'i) maddenin ortam içindeki bağlı yapısının modelini gerektirir.

Ayrıca kohezyon ($\Sigma$) da bu eylemde yoktur: barotropik $u$ çekme dayanımı üretmez. Gradyan terimi ($\propto(\nabla\rho)^2/\rho$) $\Sigma$ ve $v_{kav}$'ı verebilir ama statik tepkiyi perdeler (Yukawa, $\sim10^{-18}$ m), yani 1. maddeyi ağırlaştırır.

### Açık Uçlar

- **$\chi$ alanının denklemi (öncelik 1).** Deplasman alanının $1/r$ ile yayılmasını veren terim nedir? Bu bulunursa M-35'in $P(r)=P_0-\alpha M/r$ profili eylemden çıkar ve kütle-itim türetilmiş olur.
- **İki kısmi türevin birleşik mikro-türetimi.** Nükleonun vakum cebi ve girdap zarfı, hem stiff adiyabatik tepkiyi hem yoğunluk-korumalı deplasmanı birlikte vermeli.
- **Kohezyonun perdelemesiz eklenmesi.** $\Sigma$ ve $v_{kav}$'ı $1/r$ kuyruğunu bozmadan üretecek terim.
- **Dönüsüz-olmayan genişletme.** Clebsch veya Lin kısıtıyla vortisiteli akış; makro-vorteks kolunun (M-22, M-30) eyleme bağlanması buna bağlıdır.
- **Korunum yasaları.** Eylem tamamlandığında Noether akımları hesaplanmalı; elle konan korunumlar (M-38'in silindirik akısı) böylece türetilmiş olur.

### Süreç Kaydı (28–29 Temmuz 2026)

Bu girdinin ilk sürümü hatalıydı ve düzeltilmesi bir sınavla geldi. İlk sürüm, Ek B.3'ün deplasman bağıntısını ($\delta\rho/\rho_0=k\,\delta P/P_0$) bir **hâl denklemi** sanıp integre ediyor ve $P=K\rho^{1/k}$ politropunu, oradan da "$k$ politrop indisin tersidir" sonucunu ve süper-akışkan yorumundan $k=\tfrac12$ öngörüsünü çıkarıyordu.

**Bölüm 6.6.5'teki Sınav 4 bunu yanlışladı:** $k=\tfrac12$, kütleçekim dalgasının ışıktan 38,2 milyon yıl önce gelmesini gerektirir (gözlenen: 1,74 saniye sonra). Hata, söz konusu bağıntının bir hâl denklemi olmaması — maddenin eklenmesiyle ortam durumunun nasıl değiştiğini söyleyen bir ilişki olması — idi. Kategori hatası düzeltilince iki değişkenli yapı ortaya çıktı ve mengene kapandı.

*Aynı düzeltmenin yan sonucu:* bir denetim turunda Ek M-5 ve M-9'un "sıkışma kanalının hızı $c$'dir" ifadeleri $c/\sqrt k$ diye değiştirilmişti. **O değişiklik hatalıydı; orijinal metin doğruydu** ve geri alınmıştır.

---

*Blok I, matematik programının Faz 1–6'sı sonrası açılmış olup tek girdiyle başlar. Sonraki girdiler eylemin genişletilmesiyle eklenecektir.*
