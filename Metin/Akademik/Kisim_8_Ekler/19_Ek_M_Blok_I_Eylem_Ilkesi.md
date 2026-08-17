# Ek M — Merkezî Türetim Kataloğu · Blok I: Hâl Denklemi ve Eylem İlkesi

Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.

**Blokun kapsamı.** Teorinin en büyük yapısal açığı, beş kuvvetin ve ölçek yapısının **tek bir eylem ilkesinden** türetilmemiş olmasıdır: her biri ayrı bir ansatz'la kurulur, iç tutarlılık ancak elle denetlenebilir ve korunum yasaları türetilemez. Bu blok o programın ilk adımıdır: ortamın hâl denklemini belirler, oradan akışkan eylemini yazar, ve eylemin nereye kadar gittiğini — daha önemlisi **nerede tıkandığını** — kaydeder.

---

## M-44 · Ortamın İki Değişkenli Hâl Denklemi ve Akışkan Eylemi · **[T]**

**Kullanıldığı bölümler:** Ek B.3 ($k$'nın anlamı ve değeri), 2.4.2 (Yön Kuralı), 7.4 md.16. Bağlı katalog: M-1 (Kavrama Yasası), M-3 ($\sqrt2c_0$), M-7/M-8 ($P_0$), M-9 (kararlılık), M-15 (G2 deplasman aksiyomu), M-30 (galaktik profil varsayımı).

### Sorunun kurulumu: iki ifade bir arada duramıyordu

Teori iki şeyi birden söylüyordu ve tek sembolle yazıldıkları için çeliştikleri görünmüyordu:

- **(A)** "Basınç salınımları $c_0$ ile yayılır" (M-5, M-13) — GW170817'nin gerektirdiği.
- **(B)** "Kütle yakınında $\delta\rho/\rho_0=k\,\delta P/P_0$, $k<1$" (Ek B.3) — Yön Kuralı'nın dayanağı.

Newton–Laplace bağıntısı ($v_{ses}^2=dP/d\rho$) altında bu ikisi tek bir hâl denkleminden çıkarılmaya çalışılırsa ancak $k=1$'de bir arada durur; $k=1$ ise $P_0=\frac{1-k}{4}\rho_nc_0^2\to0$ demektir ve M-7'nin yırtılmama tabanını ($1{,}6\times10^{25}$ Pa) altı buçuk mertebe ihlal eder.

Çelişki fizikte değil, **muhasebededir**: iki farklı süreç aynı harfi paylaşırsa çakışır.

### Varsayımlar

1. Kavrama Yasası'nın oran biçimi geçerlidir: $c_{loc}^2=P/\rho$ (M-1).
2. Ortamın durumu **iki bağımsız değişkenle** tanımlanır: yoğunluk $\rho$ ve maddenin doğurduğu **deplasman alanı** $\chi$. Nükleonlar $\chi$'nin kaynağıdır; $\chi$ kütlenin dışında da sıfır değildir (kütle-itim kuyusunun kendisi $\chi$ alanıdır).
3. Akış dönüsüzdür ($\vec v=\nabla\varphi$) — eylemin en dar biçimi; genişletme Açık Uçlar'dadır.

### Adımlar

**1. İki değişken, iki kısmi türev.** Hâl denklemi $P=P(\rho,\chi)$ biçimindedir ve iki bağımsız tepki katsayısı taşır. Bunlar farklı fiziksel süreçleri tanımlar ve karıştırılamaz:

$$\left(\frac{\partial P}{\partial\rho}\right)_{\chi} \qquad\text{ve}\qquad \left(\frac{\partial P}{\partial\chi}\right)_{\rho}$$

Bu yapı, sıradan bir akışkanın $P=P(\rho,S)$ yapısının birebir karşılığıdır: ses dalgaları sabit entropide ilerler, ısıtma ise sabit yoğunlukta basıncı değiştirir. Newton'un ses hızını ~%18 eksik hesaplaması (izotermal ↔ adiyabatik; $\sqrt\gamma=1{,}18$ düzeltmesi), tam olarak iki kısmi türevin karıştırılmasından doğmuştu.

**2. Dalga kanalı — ortam stifftir, ses hızı tam $c_0$.** Sabit deplasman alanında ($\chi$ donmuş; dalga periyodu deplasmanın kurulma süresinden çok kısa) hâl denklemi Kavrama Yasası'nın kendisidir:

$$P=c_0^2\rho \qquad\Longrightarrow\qquad \left(\frac{\partial P}{\partial\rho}\right)_\chi=c_0^2 \qquad\Longrightarrow\qquad \boxed{\;v_{ses}=c_0\ \text{ tam olarak}\;}$$

Bu, **stiff (Zel'dovich) akışkan** hâl denklemidir: ses hızının **yerel** ışık hızına *tam eşit* olduğu, dalga sertliği en yüksek hâl.

> **⚠ Düzeltme (17 Ağustos 2026, Ek M-55).** Yukarıdaki kutu, sabit $\chi$'de $(\partial P/\partial\rho)_\chi=c_0^2$ yazarak ses hızını **küresel** bir sabite bağlıyordu. Deplasman kanalının yerel (üstel) tepkisiyle birlikte doğru ifade **yerel**dir:
> $$\left(\frac{\partial P}{\partial\rho}\right)_{\!\chi}=\frac{P}{\rho}=c_{loc}^2 \;\Longrightarrow\; v_{ses}=c_{loc}=\sqrt{P/\rho}$$
> Varsayım 1'in *"Kavrama Yasası'nın **oran** biçimi geçerlidir: $c_{loc}^2=P/\rho$"* ifadesi **aynen ve tam olarak** korunur; düşen şey yalnız "$c_0$ küresel sabittir" okumasıdır — ki Postülat 4 onu zaten reddeder.
>
> **Ve bu bir kayıp değil, kazançtır:** GW170817 hâlâ otomatik sağlanır, ama **daha güçlü bir gerekçeyle** — sıkışma dalgası ile Zerre **aynı** $c_{loc}$'u paylaştığı için hız farkı **özdeş sıfırdır**. Eski gerekçe ("ikisi de tam $c_0$'dedir") farklı potansiyellerde birebir eşitliği garanti etmiyordu: lineer okumada dalga hızı $c_0$'da donarken ışık $c_0\Lambda^2$'ye düşer ve ikisi ayrışır (Samanyolu potansiyelinde $8{,}9\times10^{-7}$, kısıt $4{,}2\times10^{-16}$ — **dokuz mertebe ihlal**). Üstel biçim, iddiayı gerçekten otomatik yapan **tek** biçimdir. *(Adlandırma notu: standart kozmolojinin "nedensel olarak en katı" deyişi burada kullanılmaz — o ad, $c$'yi nedensellik tavanı sayan çerçevenin ürünüdür; teoride $c_0$ tavan değildir, yapı/kohezyon kanalı $v_m>10^4c_0$ ile çalışır — M-5 ve aşağıda zaman sektörü.)* M-1'in kutulu sonucundaki $\rho_0=P_0/c_0^2$ bu denklemin ta kendisidir. Sonucu: standart fiziğin **"kütleçekim dalgası"** dediği gözlemin hız kısıtı (GW170817) otomatik sağlanır.

**3. Deplasman kanalı — $k=0$.** Madde ortamı dışlar; bu süreç yoğunluğu değil basıncı değiştirir. Teori bunu iki ayrı yerde zaten söyler:

| Kaynak | İfade |
|---|---|
| **M-15, G2 aksiyomu** | Madde içinde $\bar P_m=P_0(1-\phi)$ ama $\bar\rho_m=\rho_0$ — *"hacimce ortalama yoğunluk sabittir, korunum"* |
| **M-30, Varsayım 1** | *"Gradyanlarda asıl değişen basınçtır"*; yoğunluk yaklaşık sabit |

Bu, Ek B.3'ün parametrizasyonunda tek bir değere karşılık gelir:

$$\frac{\delta\rho}{\rho_0}=0 \qquad\Longrightarrow\qquad \boxed{\;k=0\;}$$

**$k$ serbest parametre değildir.** Değeri, G2 aksiyomu ile M-30'un profil varsayımından belirlenir; ikisi bağımsız olarak aynı sonucu verir.

**4. Yön Kuralı maksimum tepkiyle çalışır.** $k=0$ ile

$$\frac{\delta c}{c_0}=\frac{1}{2}\left(\frac{\delta P}{P_0}-\frac{\delta\rho}{\rho_0}\right)=\frac{1}{2}\,\frac{\delta P}{P_0}$$

Kütleye yaklaşırken $\delta P<0$ olduğundan $\delta c<0$: ışık zorunlu olarak yavaşlar ✓, ve katsayı olabilecek **en büyük** değerdedir ($\tfrac12$).

**5. Arka plan basıncı sabitlenir.** M-8'in zinciri $k=0$ ile kapanır:

$$P_0=\frac{1-k}{4}\rho_nc_0^2 \;\overset{k=0}{=}\; \frac{1}{4}\rho_nc_0^2 = 6{,}07\times10^{33}\ \text{Pa}\,,\qquad \rho_0=\frac{\rho_n}{4}=6{,}8\times10^{16}\ \text{kg/m}^3$$

**6. Akışkan eylemi.** Stiff hâl denklemiyle ($u(\rho)=\tfrac12 c_0^2\rho$ mertebesinde, sabit $\chi$'de) eylem:

$$S=\int dt\,d^{3}x\left[-\rho\left(\partial_t\varphi+\tfrac12(\nabla\varphi)^{2}\right)-u(\rho,\chi)\right]$$

Varyasyonlar teorinin iki temel denklemini verir:

- $\delta S/\delta\varphi=0\;\Rightarrow\;\partial_t\rho+\nabla\cdot(\rho\nabla\varphi)=0$ — **süreklilik**
- $\delta S/\delta\rho=0\;\Rightarrow\;\partial_t\varphi+\tfrac12(\nabla\varphi)^2+h(\rho,\chi)=0$ — **Bernoulli**

**7. M-9'un kararlılık sonucu türetilmiş olur.** Sabit $\chi$'de $(\partial P/\partial\rho)=c_0^2>0$ olduğundan homojen arka plan çöküşe karşı kararlıdır ve yoğunluk pürüzleri **$c_0$ hızında** dağılır — M-9'un metninde yazan sonucun kendisi. Ayrıca ağırlıksızlık, eylemde ortamın öz-kütleçekim teriminin **bulunmaması** olarak görünür: "Poisson'u reddediyoruz" bir red olmaktan çıkıp yazılı bir seçime dönüşür.

### Sonuç

$$\boxed{\;P=P(\rho,\chi)\;;\qquad \left(\frac{\partial P}{\partial\rho}\right)_\chi=c_0^2\ \Rightarrow\ v_{ses}=c_0\;;\qquad k\equiv\left.\frac{\delta\rho/\rho_0}{\delta P/P_0}\right|_{\text{deplasman}}=0\;}$$

| Kısıt | Hangi kanal | Durum |
|---|---|---|
| GW170817 ($\lvert\Delta v\rvert/v<4{,}2\times10^{-16}$) | dalga | ✓ **otomatik** — stiff hâl denklemi |
| Işık bükülmesi $1{,}7512''$ | deplasman | — **kalibrasyon girdisi** (M-8/M-42): $P_0=\frac{1-k}{4}\rho_nc_0^2$ ikamesinde $(1-k)$ sadeleşir, genlik her $k$'de inşa gereği aynı çıkar — $k$'yı sınamaz; $k=0$'ın bu zincire katkısı $P_0$'ı tek değere ($6{,}07\times10^{33}$ Pa) indirmesidir |
| M-7 yırtılmama tabanı | $P_0$ | ✓ $3{,}8\times10^{8}$ kat marj |
| Yön Kuralı ($\delta c<0$) | deplasman | ✓ |

*$k$'nın bağımsız sınavları bu tablonun dışındadır: Sınav 4 (6.6.5, GW–ışık varış farkı; $k=\tfrac12$'yi dışlar) ve Ek C satır 3 (SN 1987A bütçesi). Kalibrasyon ≠ geçilmiş sınav — düzeltme kaydı, 9 Ağustos 2026. GW170817 kısıtının kaba yazımı $10^{-15}$'tir (M-5/M-9/M-14 bu yuvarlak değeri kullanır); buradaki $4{,}2\times10^{-16}$, aynı ölçümün 1,74 s / yol süresi hesabıdır — iki yazım aynı kısıttır.*

**Parametre envanterine etkisi:** $k$ serbest skaler listesinden **çıkar** (Ek C satır 3, [F] → [T]). Dürüst sayım 6 skalerden **5**'e iner.

### Sonuç 2 — Korunumluluk Ölçütü: Hangi Kanal Söndürebilir · **[T]**

İki değişkenli hâl denkleminin ikinci ve doğrudan sonucu, teorinin **hangi koşulda enerji
söndürebileceğini** belirler. Kitap üç ayrı yerde birbirinden bağımsız üç olumsuz hüküm veriyor —
F5 düzlem seçer ama söndürmez (M-39, 11.4.2–11.4.4); kararlı yörüngeler kararlı kalır (11.6.8);
ikili daralma için yitimli ya da yayınımlı bir kanal gerekir (11.6-i). **Üçü de tek bir satırın
sonucudur.**

**Ölçüt $\nabla P$ değil, $\nabla P/\rho$'dur.** Bir gradyanın rotasyoneli tanım gereği sıfırdır,
dolayısıyla $-\nabla P$ **her zaman** rotasyonsuzdur; ama cisme etki eden nicelik birim kütle
başına kuvvettir ve onun rotasyoneli sıfır olmak zorunda değildir:

$$\nabla\times\left(-\frac{\nabla P}{\rho}\right)
=\nabla\!\left(-\frac1\rho\right)\!\times\nabla P
=\frac{1}{\rho^{2}}\,\nabla\rho\times\nabla P$$

$P=P(\rho,\chi)$ konursa gradyan iki bileşene ayrılır — biri stiff adiyabatik tepki
($(\partial P/\partial\rho)_\chi=c_0^2$), öteki deplasman kanalı ($(\partial P/\partial\chi)_\rho=-C$,
M-46) — ve birincisi $\nabla\rho$ ile **paralel olduğu için düşer:**

$$\boxed{\;\nabla\times\left(-\frac{\nabla P}{\rho}\right)
=\frac{1}{\rho^{2}}\left(\frac{\partial P}{\partial\chi}\right)_{\!\rho}\,\nabla\rho\times\nabla\chi
=-\frac{C}{\rho^{2}}\,\nabla\rho\times\nabla\chi\;}$$

**Dolaşım bu ifadede hiç geçmiyor.** Dolaşım $P$'yi belirler (M-22) ama gradyan yapısını bozmaz;
akan bir ortamda basınç kuvvetinin korunumlu olup olmaması akışa değil, **iki durum değişkeninin
gradyanlarının hizasına** bağlıdır. Söndürme için **iki koşul birlikte** gerekir: sıkışma kanalı
etkin olmalı ($\nabla\rho\neq0$) **ve** iki gradyan hizasız olmalı.

| # | Yapılandırma | Sonuç |
|---|---|---|
| **1** | **Yalnız deplasman kanalı** | $k=0$ türetilmiştir (yukarıdaki Sonuç): madde ortamı dışlarken **yoğunluğu değil basıncı** değiştirir ⟹ $\nabla\rho=0$ ⟹ **tam korunumlu** |
| **2** | **Tek, küresel simetrik gövde** | M-46 ile $\chi$ Poisson kaynaklıdır, $\rho$ da radyaldir ⟹ $\nabla\rho\parallel\nabla\chi\parallel\hat r$ ⟹ çapraz çarpım **kimliksel sıfır**; sıkışma etkin olsa bile korunumlu |
| **3** | **İki gövde** | $\nabla\chi$ birinin kuyusundan, $\nabla\rho$ ötekinin sıkışmasından ⟹ genel olarak **hizasız** ⟹ **korunumsuzluk mümkün** |
| **4** | **Gelgit lobu taşıyan gövde** | Lob küresel simetriyi kırar ($\chi$ artık $\chi(r,\theta)$) ⟹ hizasızlık ⟹ **söndürme yetkili** |

**Satır 1, M-39'un hükmünü türetilmiş hâle getirir.** F5'in düzlem seçip söndürmemesinin sebebi
"basınç alanı korunumludur" değil, **$k=0$'dır** — ve bu, F5'in potansiyeli saf $P_2$ olduğu hâlde
değişmez, çünkü ölçüt açısal biçim değil $\nabla\rho$'dur.

> [!NOTE]
> **Sağlamlık kaydı — satır 1 $k=0$'a muhtaç değildir.** Ölçüt $\nabla\rho\times\nabla\chi$ olduğuna göre, yoğunluk pertürbasyonu **yalnız deplasman alanı tarafından uyarılmışsa** — yani $\delta\rho=f(\chi)$ ise — $\nabla\rho=f'(\chi)\nabla\chi$ olur ve çapraz çarpım $k$'nin **hangi değeri için olursa olsun** özdeş sıfırdır. Satır 1'in sonucu dolayısıyla $k=0$'dan daha zayıf bir öncüle dayanır: korunumluluk için $\delta\rho$'nun *sıfır* olması değil, *bağımsız* olmaması yeter. Korunumsuzluk ancak $\rho$ ayrı bir sebeple (ikinci gövde, gelgit lobu, önceden var olan gradyan) değiştiğinde doğar — ki satır 3 ve 4 zaten odur. Bu, hükmü $k$'nin gözlemsel belirsizliğinden bağımsız kılar (Ek C satır 3: $\lvert k\rvert\lesssim2{,}3\times10^{-5}$).

**Satır 2, 11.6.8'nin eşiğini sayısaldan yapısala çevirir.** Tek ve küresel bir gövdenin uydusunu
sönümlemesi *küçük* değil, **kimliksel olarak imkânsızdır.** Gerçek gövdeler tam küresel olmadığı
için 11.6.8'nin sayıları yine gereklidir; ama sıfırdan sapma artık bir tesadüf değil, **simetri
kırılmasının ölçüsü.**

**Satır 3, 11.6-i'nin adresini verir.** O kalem yitimli bir kanal istiyor ama nerede aranacağını
söylemiyordu: yetkili terim $C\,\nabla\rho\times\nabla\chi$'nin **iki-cisim** hizasızlığıdır, ve
$\nabla\rho\neq0$ koşulu onu zorunlu olarak **sıkışma kanalına** (Ek M-5) bağlar — kalemin kendi
işaret ettiği yere.

**Satır 4, lob kanalının söndürme lisansıdır** (3.9, 11.5.5): gelgit şişkinliği simetriyi kırdığı
için lob kanalı gerçekten yitimlidir, ve 11.5.5 onun nerede yaşayıp nerede öldüğünü ölçer.

> **Geçerlilik sınırı — ölçüt yön verir, genlik vermez.** $(\partial P/\partial\chi)_\rho=-C$'nin
> **değeri** M-46'nın açık ucudur ve hizasızlık açısı türetilmemiştir; bağıntı bir kanalın var
> olup olabileceğini söyler, ne kadar güçlü olduğunu söylemez.
>
> **Ve zaman bağımlılığı ayrı bir kapıdır.** Rotasyonsuz bir kuvvet bile $\partial P/\partial t\neq0$
> ise kapalı bir yörüngede net iş yapabilir. Ortamın gecikmesi ölçülüdür (DY-1'in ölçek kaydı,
> $\sqrt2\,v/c_0$), ama **küresel-radyal bir gecikmenin net iş yapmadığı gösterilmemiştir.** Naif
> okuma ikili pulsarda tur başına $\sim2\times10^{-3}$ verirdi; gözlenen kesirli daralma
> $\sim1{,}6\times10^{-12}$'dir, yani naif okuma $10^{9}$ kat fazladır — bastırma mekanizması
> vardır ve yazılmamıştır. → **Açık Uçlar**, aşağıda.

### Geçerlilik Sınırı — eylemin *vermediği* şeyler

Bu blok, programın tamamlandığını değil **başladığını** kaydeder. Yukarıdaki yapı dört şeyi vermez:

1. ~~Kütle-itimin $1/r^2$'si çıkmaz~~ → **M-46 ile kapandı:** $\chi$'nin yayılım terimi yazılmıştır ($\nabla^2\chi=-q_nn_m$), profil ve $1/r^2$ eylemden çıkar; kalan, $C=-(\partial P/\partial\chi)_\rho$ katsayısının **değerinin** mikro türetimidir (aşağıda md. 2 ile birleşir).
2. **İki kısmi türevin ortak mikro-modeli yoktur.** Adiyabatik tepkinin neden tam stiff, deplasmanın neden tam yoğunluk-korumalı olduğu ayrı ayrı ifade düzeyindedir; ikisini tek bir mikro-yapıdan (nükleonun vakum cepli girdap yapısı) türetmek yapılmamıştır.
3. ~~$\omega_1/\omega_2$ çift dönüşü temsil edilemez~~ → **M-50 ile yapı düzeyinde kapandı:** 4B'de iki Clebsch çifti, vortisitenin Darboux ayrışımı olarak çift dönüşü doğrudan temsil eder (izoklin = öz-dual vortisite). Kalan: $\omega_2$'yi süren dinamik ve hizalanma tercihi (M-50 Geçerlilik Sınırı 1–2).
4. **$\Lambda$ ölçeklemesi çıkmaz.** Cetvellerin ve saatlerin neden tam $\Lambda$ ile ölçeklendiği (M-42'nin $\gamma_\ell=-1$'i) maddenin ortam içindeki bağlı yapısının modelini gerektirir.

Kohezyon ($\Sigma$) bu eylemde yoktu: barotropik $u$ çekme dayanımı üretmez. *(Güncelleme: gradyan teriminin "statik tepkiyi perdeler" itirazı, kütle-itimin $\chi$-sektörüne taşınmasıyla (M-46) düşmüştür — $\rho$-gradyan terimi $\chi$ denklemine dokunmaz. Kohezyon sektörü M-50'de perdelemesiz eklenmiştir; $\Sigma(\Lambda_\Sigma)$ özdeşleştirmesi oranın açık kalemidir.)*

### Açık Uçlar

- ~~$\chi$ alanının denklemi (öncelik 1)~~ → **çözüldü: M-46.** Terim yazıldı ($\nabla^2\chi=-q_nn_m$ + kohezyon-taşıyıcılı zaman sektörü), M-35'in profili ve kütle-itim eylemden çıktı; öncelik artık $C$'nin **değerinin** mikro türetimindedir (M-46 Açık Uçlar).
- **İki kısmi türevin birleşik mikro-türetimi.** Nükleonun vakum cebi ve girdap zarfı, hem stiff adiyabatik tepkiyi hem yoğunluk-korumalı deplasmanı birlikte vermeli.
- ~~Kohezyonun perdelemesiz eklenmesi~~ → **M-50 ile eklendi** (sektör ayrımı sayesinde perdelemesiz); kalan iş $\Sigma(\Lambda_\Sigma)$ özdeşleştirmesi.
- ~~Dönüsüz-olmayan genişletme~~ → **M-50 ile çözüldü:** Clebsch genişletmesi yazıldı, Euler ve vortisite eylemden çıkıyor; makro-vorteks kolu (M-22, M-30) eyleme bağlandı.
- **Korunum yasaları** → **program M-50'de açıldı:** yeniden-etiketleme Noether'i Kelvin'i, 2B indirgeme nokta-girdap yüklerini ($H$, $\vec I$, $A$) verdi; alan-düzeyi akımlar ve M-38'in silindirik akısı hâlâ hesaplanmalı.
- **Zaman bağımlı korunumsuzluğun bastırılması** *(Sonuç 2'den).* Küresel-radyal bir basınç gecikmesinin kapalı yörüngede net iş **yapmadığı** gösterilmelidir. Naif okuma gözlenen ikili daralmanın $10^{9}$ katını verir; bir bastırma mekanizması zorunludur ve türetilmemiştir. 11.6-iii ile aynı ailedendir.

### Kritik Ayrım: Deplasman Bağıntısı Bir Hâl Denklemi Değildir

Ek B.3'ün deplasman bağıntısı ($\delta\rho/\rho_0=k\,\delta P/P_0$) bir **hâl denklemi olarak okunamaz.** Öyle okunup integre edilirse $P=K\rho^{1/k}$ politropu, oradan "$k$ politrop indisin tersidir" sonucu ve süper-akışkan yorumundan $k=\tfrac12$ çıkar.

**Bölüm 6.6.5'teki Sınav 4 bu okumayı dışlar:** $k=\tfrac12$, kütleçekim dalgasının ışıktan 38,2 milyon yıl önce gelmesini gerektirir; gözlenen 1,74 saniye **sonra**dır. Bağıntı bir hâl denklemi değil, **maddenin eklenmesiyle ortam durumunun nasıl değiştiğini** söyleyen bir ilişkidir. Doğru okuma iki değişkenli yapıyı verir ($P=P(\rho,\chi)$, Ek M-44) ve $k=0$ türetilir.

*Sonuç:* Ek M-5 ve M-9'un "sıkışma kanalının hızı $c_0$'dir" ifadeleri geçerlidir; $c_0/\sqrt k$ okuması iki kanalın karıştırılmasından doğar (Ek M-44).

---

---

## M-46 · $\chi$-Yayılım Terimi: Kütle-İtimin Eylemden Çıkışı · **[T (yapı) / F ($C$ değeri)]**

**Kullanıldığı bölümler:** M-44 (Geçerlilik Sınırı md. 1 — bloğun en büyük açık ucu), M-35, M-28, 6.5.4. Bağlı katalog: M-2, M-45, Ek A.3 ($v_m$).

M-44 kendi eksiğini kaydetmişti: *"$\chi$ alanının neden $1/r$ ile yayıldığı eylemde henüz yoktur."* Bu girdi o terimi yazar; kütle-itim ($1/r^2$) eylemden çıkar ve $C$'nin kimliği hâl denkleminin ikinci katsayısı olarak kesinleşir.

### Varsayımlar

1. **$\chi$ deplasman potansiyelidir** ve kaynağı, birim hacim başına hacim-enjeksiyon debisidir: nükleon sayı yoğunluğu $n_m$ olan madde, ortama $q_n n_m$ (s⁻¹) debisi boşaltır (M-35'in kaynağıyla aynı). Boyutu $[\chi]=$ m²/s.
2. **Eyleme iki yeni terim eklenir** (M-44'ün $S$'sine):
$$\Delta S=\int dt\,d^3x\left[\frac{1}{2v_m^2}(\partial_t\chi)^2-\frac{1}{2}(\nabla\chi)^2+\chi\,q_n\,n_m\right]$$
Zaman teriminin taşıyıcısı **kohezyon kanalıdır**: $v_m=c_0\sqrt{\Sigma/P_0}>10^4c_0$ (Ek A.3) — deplasman alanı, ortamın yırtılmaz iskeleti üzerinden ayarlanır.
3. **Hâl denkleminin doğrusallaştırılması** (M-44'ün iki kanalı): $\delta P=\left(\frac{\partial P}{\partial\rho}\right)_\chi\delta\rho+\left(\frac{\partial P}{\partial\chi}\right)_\rho\delta\chi$; deplasman kanalında $\delta\rho=0$ ($k=0$, M-44) ve ikinci katsayı tanımlanır: $\left(\frac{\partial P}{\partial\chi}\right)_\rho\equiv-C$.
   > **⚠ Kapsam kaydı (17 Ağustos 2026, Ek M-55).** Bu **doğrusallaştırma**dır ve sabit $C$ ile yazılmıştır. Tam (yerel-referanslı) yanıt üsteldir: $\left(\frac{\partial P}{\partial\chi}\right)_\rho=-C\,\dfrac{P}{P_0}$, dolayısıyla $P=P_0e^{-C\chi/P_0}$. Sabit $C$ okuması, tepki yasasına her konumda aynı basınç ölçeğini yerleştirir ve Postülat 4 ile çelişir; ayrıca ikinci mertebede GW170817'yi ihlal eder. **Aşağıdaki 1. ve 3. adımlar (Poisson ve $\mathcal{G}$) bu değişimden etkilenmez** — yalnız 2. adımın profili üstel biçime yükseltilir.

### Adımlar

1. **Statik alan denklemi** ($\delta\Delta S/\delta\chi=0$, durağan): $\nabla^2\chi=-q_n n_m$ — Poisson. Noktasal $N$ nükleon için
$$\chi(r)=\frac{Nq_n}{4\pi r}$$
**$1/r$ yayılımı eylemden çıkar** (boyut denetimi: $[\nabla^2\chi]=$ s⁻¹ $=[q_nn_m]$ ✓).
2. **Basınç profili** (Varsayım 3): $\delta P=-C\chi\Rightarrow P(r)=P_0-\dfrac{CNq_n}{4\pi r}$ — **M-28/M-35'in profili birebir** ($dP/dr=C\,\Phi_q$ ✓; $[C\chi]=$ Pa ✓).
   **Tam biçim (Ek M-55):** $P(r)=P_0\,e^{-C\chi/P_0}=P_0\,e^{-4\mathcal{G}M/c_0^2r}$; yukarıdaki doğrusal profil onun **birinci mertebe kesitidir** ve zayıf alanda ($\Delta P/P_0\sim10^{-9}$) ayırt edilemez. Üsteki 4 çarpanı, M-46'nın kendi zincir denetiminden gelir ($C\chi/P_0=4\Phi/c_0^2$) ve M-8'in sıkışma oranı $\rho_n/\rho_0$'dır — fit değildir.
3. **Kütle-itim** (M-2): $\vec a=-\dfrac{1}{\rho_n}\nabla P=-\dfrac{Cq_n}{4\pi\rho_n m_n}\dfrac{M}{r^2}\hat r$ — $1/r^2$ ve $\mathcal{G}=\dfrac{Cq_n}{4\pi\rho_n m_n}$ **eylemden türetilmiş olur** — $\mathcal{G}=\alpha/\rho_n$ yereldir, evrensel sabit değildir (Postülat 4); arka plan değeriyle sayısal denetim: $6{,}70\times10^{-11}$ — ölçülenin %0,4 içinde ✓.
4. **Zaman sektörü ve nedensellik:** $\chi$ dalgaları $v_m>10^4c_0$'de yayılır — statik alanın ayar hızı budur ve Bell-tipi sınırların ($\Sigma/P_0>10^8$, Salart) kanalıyla **aynıdır.** Standart fiziğin "kütleçekim dalgası" dediği gözlemler ise $\rho$-sektöründedir ve **yerel** $c_{loc}$'de yayılır (M-44'ün stiff kanalı) — GW170817 uyumu bozulmaz. **Ayrışabilir öngörü:** statik alan ayarı ile dalga yayılımı iki ayrı hızdır.

### Sonuç

$$\boxed{\;\nabla^2\chi=-q_nn_m\;;\qquad \left(\frac{\partial P}{\partial\chi}\right)_\rho=-C\;;\qquad
\vec a=-\frac{Cq_n}{4\pi\rho_nm_n}\frac{M}{r^2}\hat r\;\;\Rightarrow\;\;\mathcal{G}=\frac{Cq_n}{4\pi\rho_nm_n}\;}$$

**$C$'nin kimliği kesinleşir:** hâl denkleminin **iki** tepki katsayısı vardır ve ikisi tam olarak $(A,C)$'dir — $A=(\partial P/\partial\rho)_\chi=c_0^2$ (dalga sertliği), $C=-(\partial P/\partial\chi)_\rho$ (deplasman direnci). M-35'in "ikisi bağımsız olamaz" kaydı ile köprü muhasebesinin boyutsuz empedans oranı ($C\ell_\omega/(\rho_0 c_0)=4{,}2\times10^{-39}$; 1.4.12), artık tek cümledir: *kütle-itimin zayıflığı, hâl denkleminin iki kısmi türevinin oranıdır.* Kazançlar: **(i)** M-44'ün 1 numaralı eksiği kapanır — kütle-itim eylemden çıkar; **(ii)** M-35'in [T (yapı)] statüsü eylem-temelli olur; **(iii)** korunum programı (Noether) kütle-itim sektörü için açılır.

### Geçerlilik Sınırı

- **$C$'nin değeri türetilmemiştir** — yapı [T], değer [F]: $10^{-39}$'luk hiyerarşinin mikro-modeli (nükleonun vakum-cepli girdap yapısından $(\partial P/\partial\chi)_\rho$'nun hesabı) M-44'ün 2 numaralı eksiğiyle birleşerek bloğun kalan işi olur.
- Doğrusallaştırılmış rejim ($\delta P\ll P_0$): galaktik ve Güneş Sistemi alanları için $\delta P/P_0\lesssim10^{-9}$ — bol marj; güçlü-alan davranışı yazılmamıştır.
- Dönüsüz akış kısıtı ve $\omega_1/\omega_2$ temsilsizliği (M-44 md. 3) burada da sürer; kaynak terimi izotropik pulsasyon koludur, dolanım kolu ($\gamma_n$, F4) eylemin hâlâ dışındadır.

### Açık Uçlar

- ~~$(\partial P/\partial\chi)_\rho=-C$'nin mikro türetimi~~ → **kalem yeniden sınıflandırıldı; aşağıdaki kutuya bakınız.** $C$ bir malzeme özelliği değil, bir **madde–ortam kuplaj sabitidir**; türetilecek bir sayı değil, ölçülecek bir kuplajdır. Dokuz türetim yolunun her biri ayrı bir gözlemle kapanmıştır.

> [!IMPORTANT]
> **$C$'nin kategorisi: kuplaj sabiti, hâl katsayısı değil.**
>
> Bu blok $C$'yi *"hâl denkleminin ikinci tepki katsayısı"* diye kaydeder ve $A=(\partial P/\partial\rho)_\chi=c_0^2$ ile kardeş sayar. Kardeşlik **biçimseldir, kategorik değildir**, ve ayrımı yapmak $C$'nin neden türetilemediğini açıklar.
>
> **Ayrım.** $\rho$ *yerel* bir durum değişkenidir: bir noktadaki değeri o noktanın durumudur. $\chi$ **yerel değildir**:
> $$\chi(\vec x)=\int\frac{q_n\,n_m(\vec x')}{4\pi\lvert\vec x-\vec x'\rvert}\,d^3x'$$
> yani evrendeki bütün maddenin bir fonksiyonelidir. Dolayısıyla $P=P(\rho,\chi)$ termodinamik anlamda bir hâl denklemi **değil**, bir alan kuplajıdır — tam emsali elektrostatikte enerji yoğunluğundaki $\rho_{yük}\varphi$ terimidir, ve oradaki kuplaj sabiti de ($e$, ya da $1/\varepsilon_0$) malzemeden türetilmez.
>
> **Bunun üç sonucu vardır.**
>
> **(1) Türetim yollarının tümü kapalıdır — ve her biri ayrı bir gözlemle.** $\mathcal{G}\neq0$, $P\propto1/r$ ve $P$'nin kaynakta **doğrusal** olmasını birlikte ister. Denenen dokuz yol:
>
> | yol | ölüm nedeni | mertebe |
> |---|---|---|
> | $-\rho\,\partial\chi/\partial t$ (kararsız Bernoulli) | seküler büyüme ister; $\dot{\mathcal G}/\mathcal G=1{,}1\times10^{-9}$/yıl | LLR $10^{4}$ |
> | $-\tfrac12\rho\lvert\nabla\chi\rvert^2$ (dinamik) | $P\sim1/r^4$, kuvvet $1/r^5$ | $r^3$ |
> | $-\rho\,(v_{arka}\!\cdot\!\nabla\chi)$ (çapraz) | ışınsal $\propto r$ ister = genleşme; $\mathcal G\propto H$ | LLR $10^{3}$ |
> | $(\mu/k)v$ (Darcy) | gerçek akış ister: $3{,}8\times10^{9}c_0$ | 1.4.12, $10^{13{,}9}$ |
> | $-K\nabla\!\cdot\!u$ (elastik) | kaynak dışında sıfır | uzak alan yok |
> | M-43'ün altkritik bastırması | kendi $n=3$'ünü kırar ($n\to1{,}55$) | tam sayı gider |
> | $\xi$ (dönme sürüklenmesi) | $\varepsilon/\xi_n=20\pi r_nc_0^2/(q_n\omega_n)=17{,}14$; $\mathcal{G}$ sadeleşir | özdeşlik |
> | tam sıkıştırılabilirlik ($k\to1$) | Euler her $k$'de $1/r^4$ verir (log-log eğim $-4{,}0000$) | üs değişmez |
> | $\chi$'nin kendi gerilim tensörü | $P_\chi=\tfrac16\rho_\chi(\nabla\chi)^2$ — karesel | $1/r^4$ |
>
> Ortak kök: akışkan dinamiğinde **korunan her şey $1/r^2$ gider** (kütle, momentum, enerji akısı); bunlardan kurulan basınç ya $1/r^2$ ya $1/r^4$ olur. $1/r$ giden tek nesne **potansiyelin kendisidir.** $P\sim1/r$ istemek $P\sim\chi$ istemektir, ve o bir momentum dengesi değil bir alan kuplajıdır.
>
> **(2) Mikro-model yolu da kapalıdır — ve aynı sebeple.** Bir mikro-model ortamın *yerel* denge durumunu hesaplar; $\chi$ o durumun değişkeni olmadığı için hiçbir yerel denge hesabı $(\partial P/\partial\chi)$ üretemez. Dışlanan-hacim modeli ($P=P(\rho/(1-f))$, $f=n_mV_{cep}$) bu ailenin en güçlüsüdür ve $(\partial P/\partial f)_\rho=\rho_0c_0^2=6{,}07\times10^{33}$ Pa gibi doğru mertebede bir sayı verir — ama $f\propto n_m\propto\nabla^2\chi$ olduğu için kaynak dışında sıfırdır. Tablodaki "elastik" satırın ta kendisidir.
>
> **(3) Ve bu bir kazançtır.** Kuplaj **ortama** olduğu için, gözlenen şiddet ortamın yoğunluğuna bağlıdır: $\mathcal{G}\propto1/\rho_0$. Yani **Postülat 4'ün yerelliği bu sınıflandırmanın sonucudur**, ayrıca varsayılan bir şey değil. Newton $G$'yi evrensel bir sabit olarak postülatlar ve yerelliği hiç öngöremez; burada yerellik kuplajın doğasından çıkar.
>
> **Kuplajın boyutsuz şiddeti.** Yukarıdaki empedans oranı ile nükleon ritmine göre normalize edilmiş biçim aynı sayıdır:
> $$\varepsilon\equiv\frac{C/\rho_0}{\omega_n}=6{,}88\times10^{-41},\qquad
> \varepsilon=\frac{\ell_\omega}{L_\ast}\cdot\frac{c_0}{u_r},\qquad \frac{u_r}{c_0}=\sqrt2\sqrt{m_p/m_e}=60{,}60$$
> Denetim: $4{,}17\times10^{-39}/60{,}60=6{,}88\times10^{-41}$ ✓. İki yazım tek kalemdir; Ek C'de sayı değişmez.
>
> **Zincir denetimi (bağımsız).** $C\chi/P_0$ ile $4\Phi/c_0^2$ aynı olmalıdır ve Dünya yüzeyinde $2{,}7777\times10^{-9}$ ile $2{,}7844\times10^{-9}$ çıkar — **%0,24.** $C$, $q_n$, $r_n$, $\rho_n$ ve $\mathcal{G}$'yi birbirine bağlayan zincirin dıştan denetimidir.
>
> **Kalan iş, artık bir türetim değil bir ölçümdür:** $\varepsilon$'un bağımsız bir düzenekte ölçülmesi. Bu, $e$'nin ya da $c_0^2$'nin statüsüyle aynı statüdür ve bir kuram için kusur değildir.

> [!NOTE]
> **Boyut kaydı — eylemin yoğunluk çarpanı.** Yukarıdaki $\Delta S$'in üç terimi de $[\mathrm{m^2/s^2}]$ boyutundadır (özgül enerji), enerji yoğunluğu değil. Eylem boyutuna ($\mathrm{kg\,m^2/s}$) ulaşmak için genel bir yoğunluk çarpanı gerekir: $\Delta S=\int\rho_\chi[\dots]\,dt\,d^3x$. Alan denklemi etkilenmez ($\rho_\chi$ sadeleşir, $\nabla^2\chi=-q_nn_m$ aynen kalır); etkilenen yalnız enerji ve gerilim tensörü hesaplarıdır. Noether programı açıldığında bu çarpan açıkça yazılmalıdır.

- F4/dolanım kolunun eyleme bağlanması (yönelim alanı; M-44 md. 3 ile ortak).
- Noether akımlarının hesabı: $\chi$-sektörünün korunumları ve M-38'in silindirik akısının türetilmesi.
- $v_m$-sektörünün gözlemsel ayrıştırılması: statik alan ayar hızı ile GW hızının farklı olduğu bir düzenek (öneri: yakın çift kütlelerde alan-gecikme imzası).

---

## M-50 · Birleşik Eylem: Girdaplı Sektör, 4B Çift Dönüş ve Kohezyon · **[T (yapı) / F (katsayılar)]**

**Kullanıldığı bölümler:** Kısım 12 (12.0 Temel Sözleşme, 12.1 profil, 12.2 çift dönüş, 12.3 bağ kanalları, 12.4 korunumlar). Bağlı katalog: M-44 (akışkan eylemi), M-46 ($\chi$-sektörü), M-22/M-30 (makro-vorteks kolu), Ek A.3 ($\Sigma$, $v_{\text{kav}}$).

M-44 kendi eksik listesini yazmıştı: dönüsüz akış kısıtı, çift dönüşün temsilsizliği, kohezyonun yokluğu, Noether programının kapalılığı. Bu girdi o listeye karşılık verir: **girdaplı sektörü, 4B çift dönüşü ve kohezyonu tek eylem iskeletine alır** ve hangi sonucun yapıdan çıktığını, hangisinin hesap kalemi kaldığını tek tek kaydeder.

### Varsayımlar

1. Ortam 4B'dir; akışkan alanları $\mathbb R^4$ üzerinde tanımlıdır ve fiziksel okuma $w=0$ kesitidir (12.0).
2. Hâl denklemi stiff'tir: $P=c_0^2\rho$ (M-44'ün $\rho$-kanalı; $\chi$-sektörü M-46'da ayrı ve aynen korunur).
3. Hız alanı Clebsch temsillidir; 4B'de iki çift yeter (aşağıda Darboux gerekçesi).
4. Kohezyon, yoğunluk-gradyanı enerjisi olarak girer (biçim aşağıda; katsayı özdeşleştirmesi açık).

### Adımlar

**1 · Tam iç enerji — 12.1'in profili eylemden çıkar.** Stiff hâl denkleminin *tam* barotropik potansiyeli (M-44'teki "mertebesinde" yazımının kesinleştirilmesi):

$$U(\rho)=c_0^2\,\rho\,\ln\frac{\rho}{\rho_0} \qquad\Longrightarrow\qquad P=\rho\,U'-U=c_0^2\rho\ \checkmark$$

Bernoulli varyasyonu $U'(\rho)=c_0^2(1+\ln(\rho/\rho_0))$ verir (sabit, $\varphi$ ayarına emilir); durağan girdap çözümünde

$$\tfrac12 v^2 + c_0^2\ln\frac{\rho}{\rho_0}=0 \;\;\Longrightarrow\;\; \rho=\rho_0\,e^{-v^2/2c_0^2} \;\;\overset{v=\sqrt2 c_0 r_e/R}{\Longrightarrow}\;\; \boxed{\;\rho=\rho_0\,e^{-(r_e/R)^2}\;}$$

— **Kısım 12.1.3'ün sınır tabakası profili artık bir eylem sonucudur**, bağımsız bir ansatz değil.

**2 · Girdaplı sektör (3B): Clebsch genişletmesi.** M-44'ün dönüsüz kısıtı kalkar:

$$\vec v=\nabla\varphi+\alpha\nabla\beta,\qquad
S_3=\int dt\,d^3x\Big[-\rho\big(\partial_t\varphi+\alpha\,\partial_t\beta+\tfrac12 v^2\big)-U(\rho)\Big]+S_\chi^{\text{(M-46)}}$$

Varyasyonlar: $\delta\varphi\Rightarrow$ süreklilik; $\delta\rho\Rightarrow$ Bernoulli; $\delta\alpha,\delta\beta\Rightarrow D\beta/Dt=0,\ D\alpha/Dt=0$ — birlikte tam Euler denklemi ve vortisite $\vec\omega=\nabla\alpha\times\nabla\beta$. **Makro-vorteks kolu (M-22, M-30) böylece eyleme bağlanır.**

**3 · Kelvin ve korunumlar Noether'den.** Clebsch eyleminin parçacık **yeniden-etiketleme simetrisi**, Noether yükü olarak dolanımı verir: $\Gamma=\oint\vec v\cdot d\vec\ell$ korunur — Kısım 12.4'ün omurgası ($\Gamma_{\text{top}}=\sum\Gamma_i$) elle konan bir teorem olmaktan çıkıp **eylemin simetri sonucuna** dönüşür. İki boyutlu nokta-girdap indirgemesinde eylem, standart indirgemeyle simülasyonun kullandığı yapıya iner:

$$H=-\frac{\rho_0}{4\pi}\sum_{i\neq j}\Gamma_i\Gamma_j\ln\frac{r_{ij}}{d_{\text{ref}}},\qquad
\vec I=\rho_0\sum_i\Gamma_i(y_i,-x_i),\qquad A=-\frac{\rho_0}{2}\sum_i\Gamma_i|\vec x_i|^2$$

— öteleme, dönme ve zaman simetrilerinin yükleri. **12.4.6'nın "kilitli sınamaları" artık eylem sınamalarıdır.**

**4 · 4B genişletme — çift dönüş, vortisitenin Darboux ayrışımıdır.** $\mathbb R^4$'te hız 1-formu iki Clebsch çiftiyle yazılır:

$$v^\flat=d\varphi+\alpha\,d\beta+\gamma\,d\delta \qquad\Longrightarrow\qquad w\equiv dv^\flat=d\alpha\wedge d\beta+d\gamma\wedge d\delta$$

**Darboux teoremi** bunun bir kısıt olmadığını söyler: kapalı, tam ranklı her 2-form yerel olarak tam bu biçimdedir — 4B akışkanın jenerik vortisitesi *zorunlu olarak* iki dik düzleme ayrışır. Bir noktada $w_{\mu\nu}$ blok-köşegenleştirildiğinde iki düzlem vortisitesi $\lambda_1,\lambda_2$ çıkar (katı dönmede $\lambda=2\omega$): **Kısım 12.2'nin SO(4) çift dönüşü, 4B akışkan vortisitesinin kaçınılmaz normal biçimidir.** $\omega_1$ kesit-içi düzlemin, $\omega_2$ $W$-içeren düzlemin vortisite yarısıdır; pulsasyon kolu $(\gamma,\delta)$ çiftinde yaşar. İki zarif özdeşlik kayda geçer: **(i)** Pfaffian $w\wedge w=2\lambda_1\lambda_2\,\mathrm{vol}_4$ — iki dönüşün çarpımı, koordinattan bağımsız bir değişmezdir; **(ii)** izoklinik dönüş ($|\lambda_1|=|\lambda_2|$) tam olarak vortisitenin **öz-dual** ($w=\pm\star w$) olmasıdır — $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ ideal ayrışımının akışkan karşılığı. M-44'ün 3 numaralı eksiği ("çift dönüş temsil edilemez") **yapı düzeyinde kapanır**: temsil artık vardır; $\omega_2$'yi *süren* dinamik ise hâlâ açıktır (aşağıda).

**5 · Kohezyon sektörü — perdelemesiz.** Eyleme yoğunluk-gradyanı enerjisi eklenir:

$$\Delta S_{\text{koh}}=-\int dt\,d^4x\;\frac{c_0^2\Lambda_\Sigma^2}{2}\,\frac{|\nabla\rho|^2}{\rho}$$

Üç sonucu vardır. **(i)** Dispersiyon kısa dalgada sertleşir: $\omega^2=c_0^2k^2(1+\Lambda_\Sigma^2k^2)$ (bu bağıntı $\Lambda_\Sigma$'nın tanımıdır); $\Lambda_\Sigma$, cep duvarının sağlık (healing) uzunluğudur. **(ii)** Keskin gradyanlı katman bir yüzey enerjisi taşır — ortam **çekme dayanımı** kazanır; $\Sigma(\Lambda_\Sigma)$ özdeşleştirme integrali açık kalemdir ve $\Sigma/P_0\sim10^9$ mertebesi için M-46'nın $v_m$-sektörüyle bağ kurulması gerekir. **(iii)** M-44'ün perdeleme itirazı **düşer**: kütle-itimin $1/r$ kuyruğu $\chi$-sektöründedir (M-46) ve $\rho$-gradyan terimi $\chi$ denklemine dokunmaz; gradyan terimi profili yalnız $R\lesssim\Lambda_\Sigma$ ölçeğinde düzeltir, 12.1.3 profili $R\gg\Lambda_\Sigma$'da aynen kalır.

**6 · 12.3 kanallarının eylemdeki adresi (program).** Bjerknes ve ışıma kanalları bu eylemin *pertürbatif* sektörüdür: iki-Kut çözümü çevresinde akustik genişlemenin monopol–monopol terimi Bjerknes'i, kuadrupol yayını Lighthill'i vermelidir — Lighthill denklemi sıkıştırılabilir Euler'in özdeş yeniden yazımı olduğundan ve Euler bu eylemden çıktığından, kanallar eylemle **tutarlıdır**; açık türetimleri hesap kalemidir. Gecikmeli-Magnus köprüsünün (12.3.4) eylem karşılığı dalga sektörünün **tek geciken Green fonksiyonudur**. Bu çekirdeğin radyal ve teğetsel izdüşümleri $(\mathcal R,\mathcal T)$ ile kuadrupol yanıtı $F_L$ birlikte hesaplanmalıdır; üçü bağımsız fonksiyon veya serbest katsayı değildir. Dairesel iki-Kut geometrisinde gecikme $y=M_{\text{orb}}\cos y$ ve $q=\Omega_p\tau$ ile kapandığından, $M\ll1$, $\Omega_p\gg\Omega_{\text{orb}}$ ve $k_pd\ll1$ yalnız asimptotik sınır koşullarıdır, temel eyleme eklenecek varsayımlar değildir.

### Sonuç

$$\boxed{\;S=\int dt\,d^4x\Big[-\rho\big(\partial_t\varphi+\alpha\partial_t\beta+\gamma\partial_t\delta+\tfrac12 v^2\big)-c_0^2\rho\ln\tfrac{\rho}{\rho_0}-\tfrac{c_0^2\Lambda_\Sigma^2}{2}\tfrac{|\nabla\rho|^2}{\rho}\Big]+S_\chi^{\text{(M-46)}}\;}$$

| Verdiği | Nasıl |
|---|---|
| Süreklilik + Euler (girdaplı) | varyasyon |
| 12.1.3 sınır tabakası profili | tam $U(\rho)$ + durağan çözüm |
| Kelvin / $\Gamma_{\text{top}}=\sum\Gamma_i$ (12.4 omurgası) | yeniden-etiketleme Noether'i |
| Nokta-girdap $H$, $\vec I$, $A$ (simülasyon korunumları) | 2B indirgeme + Noether |
| Çift dönüş = jenerik 4B vortisite; izoklin = öz-dual | Darboux + Hodge |
| Kohezyon sektörü, $1/r$ kuyruğu bozulmadan | sektör ayrımı ($\rho$-gradyan ⊥ $\chi$) |
| Kütle-itim $1/r^2$ | $S_\chi$ (M-46, aynen) |

### Geçerlilik Sınırı — eylemin hâlâ *vermediği* şeyler

1. **$\omega_2$'nin sürücüsü ve ilk dönmenin kaynağı** — temsil var, dinamo yok (12.1.5'in beyanı sürer).
2. **$\vec\omega_1\parallel\vec\omega_2$ hizalanması** — kanonik biçimin seçilme gerekçesi (12.2.1) eylemden çıkarılmadı; öz-dual sektöre bir enerji tercihi gösterilebilirse kapanır (aday: ışıma sönümünün anizotropisi).
3. **$\Sigma(\Lambda_\Sigma)$ özdeşleştirmesi** ve $10^9$ hiyerarşisinin $v_m$-sektörüne bağlanması.
4. **Bjerknes / Lighthill / geciken-Green türetimlerinin eylem-içi açık yazımı.** *(Kısmen kapandı: düşük-Mach/çıplak-yörünge özel sınırında $C_L^{(0)}=8\pi^2$ Euler düzeyinde hesaplandı — 12.3.3–12.3.4. En öncelikli açık iş, eylemin pertürbatif sektöründen $(\mathcal R,\mathcal T,F_L)$'yi tek iki-Kut çözümünde türetmek ve gerçek $M_{\text{orb}}$ ile $d_e$'yi bağlı çözmektir. $L_{\text{eff}}$ ayrıca seçilecek katsayı değil, 4B Kut geometrisinden özdeşleştirilecek mevcut uzunluktur.)*
5. **Alan-düzeyi Noether akımlarının açık hesabı** (nokta-girdap yükleri türetildi; alan ifadeleri ve M-38'in silindirik akısı yazılmadı).
6. M-44'ün 2 ve 4 numaralı eksikleri (iki kısmi türevin mikro-modeli; $\Lambda$ ölçeklemesi) **bu girdide de açıktır.**

### Açık Uçlar

- **Birinci öncelik — tek sonlu-yayılım iki-Kut çözümü:** geciken Green fonksiyonundan $\mathcal R$, $\mathcal T$ ve $F_L$ birlikte çıkarılacak; ardından iki Green–Magnus denklemi $M_{\text{orb}}$, $d_e$ ve $U'(d_e)$ için çözülecek. $M_K(d_e)=1$ yalnız çıplak dolaşım kontrolüdür, işletme Mach sayısının yerine konmaz.
- İndirgenmiş $d^{-3}$ koşumu çift ve öbek düzeyinde uygulama/ölçek tutarlılığı kontrolünü geçti. $\Delta V_{\text{öbek}}\propto N^{3/2}$ ve $\Omega_{p,N}\propto N^{-1}$ fiziksel doğrulama veya postüla değil, $d_N\propto N$ tam ölçeklemesi için simülasyonda bağımsız ölçülecek sonuç koşullarıdır. İkinci koşul ortak tek-Kut $\omega_2$ hükmünden doğrudan çıkmadığından dayatılmayacak; tam çekirdeğin $q$'ya duyarsız kolu veya türetilmiş kolektif modu yoksa doğrusal ölçekleme indirgenmiş statüde kalacaktır (12.3.4, 12.3.7).
- Öz-dual (izoklin) sektörün kararlılık/enerji analizi — hizalanma varsayımının eylem-içi sınavı.
- $\Lambda_\Sigma$'nın $R_{\text{cep}}$ ve $\Sigma$ ile özdeşleştirilmesi; kavitasyon ölçütünün (12.0.3) eylem diline çevrilmesi.
- Alan-düzeyi Noether akımları ve enerji-momentum tensörü (M-46'nın boyut kaydındaki $\rho_\chi$ çarpanı dahil).

---

*Blok I, matematik programının Faz 1–6'sı sonrası açılmıştır. M-44 hâl denklemini ve eylemi kurar; M-46 deplasman alanının yayılım terimini ekleyerek kütle-itimi eyleme bağlar; M-50 girdaplı sektörü, 4B çift dönüşü ve kohezyonu tek iskelete alır; **M-55 deplasman kanalının yerel tepkisini kurar ve M-46'nın lineer yanıtını birinci mertebe kesiti olarak yeniden konumlandırır.** Sonraki girdiler pertürbatif sektörün açık türetimleriyle eklenecektir.*

---

## M-55 · Üstel Ölçek Yapısı: Deplasman Kanalının Yerel Tepkisi · **[T (biçim) / S ($n=1$ gözlemsel kilidi)]**

**Kullanıldığı bölümler:** M-1, M-8, M-42 (ölçek yapısı — bu girdi onun tam biçimini verir), M-44, M-46, M-20/M-21, 11.4.8.1 ($\Lambda_{kin}$), 6.2, 7.4 md.14. Bağlı katalog: **M-51..M-54** (ortamın durgunluğu — bu girdinin yörünge sonuçlarının koşulu).

> **Ne yapar:** M-46'nın deplasman yanıtı $P=P_0-C\chi$ **küçük-deplasman kesitidir**. Yerel-referanslı tam biçim üsteldir ve şu sonuçları verir: **(i)** Merkür'ün günberi kayması kapanır ($\beta_{PPN}=1$; 42,9805″/yy ↔ ölçüm 42,9799 ± 0,0009, **0,69σ**), yani teorinin kayıtlı son klasik boşluğu kapanır; **(ii)** M-44'ün "GW170817 otomatik sağlanır" iddiası gerçekten otomatik olur; **(iii)** yayılma hızı hiçbir sonlu yarıçapta sıfırlanmaz — **ufuk ve tekillik yapısal olarak yoktur**; **(iv)** güçlü alanda yeni ve ayırt edici bir öngörü doğar (karadelik gölge çapı, GR'dan $+\%4{,}63$). **Yeni serbest parametre eklemez.**

### Varsayımlar
1. M-44'ün iki değişkenli hâl denklemi $P=P(\rho,\chi)$ ve deplasman kanalında $k=0$ (yoğunluk korunur, basınç düşer).
2. M-46'nın Poisson denklemi **değişmez**: $\nabla^2\chi=-q_nn_m$, dış alanda $\chi=Nq_n/4\pi r$.
3. M-1'in **oran** biçimi, **yerel** olarak: $c_{loc}^2=P/\rho$.
4. **Postülat 4:** $P_0$, $\rho_0$, $c_0$ yereldir; evrensel sabit değildir.
5. M-8'in sıkışma oranı: $\rho_0=\rho_n/4$.
6. Yörünge sonuçları için: ortam merkezî cismin çerçevesinde durgundur (**M-51–M-54**).

### Adımlar
**1. Sorunun kurulumu.** Sabit $C$ ile yazılan $-(\partial P/\partial\chi)_\rho=C$ yanıtı, tepki yasasına **her konumda aynı** basınç ölçeğini yerleştirir — yani gizli bir evrensel sabit taşır ve Postülat 4 ile çelişir. Yasayı yerel duruma referanslamak için genel aile yazılır:
$$\frac{dP}{d\chi}=-\frac{C}{P_0^{\,n}}P^{\,n} \;\Longrightarrow\; P=P_0\bigl[1-(1-n)u\bigr]^{1/(1-n)},\qquad u\equiv\frac{C\chi}{P_0}$$
Bu aile, madde ölçeğinin ikinci mertebe katsayısını ve dolayısıyla PPN $\beta$'sını tek parametreyle tarar:
$$\Lambda=1-x+\tfrac{\kappa}{2}x^2+\dots,\qquad \kappa=4n-3,\qquad \beta_{PPN}=\frac{1+\kappa}{2}=2n-1,\qquad x\equiv\frac{\Phi}{c_0^2}$$

**2. Biçim tekliği (Postülat 4 / form-değişmezliği).** $n\neq1$ ise yasa mutlak bir basınç ölçeğini **açıkça taşımak zorundadır**. Postülat 4 bunu yasaklar: $\Lambda^4$ derinliğindeki yerel bir gözlemci, kendi $P_0^{loc}=P_0\Lambda^4$'ü ile **aynı yasayı** yazabilmelidir. Bu, çözüm fonksiyonunda form-değişmezlik ister:
$$F(u_0+u_1)=F(u_0)\,F(u_1)$$
$\chi$ Poisson lineerliği gereği toplamsal olduğundan ($\chi_{top}=\chi_1+\chi_2$), bu fonksiyonel denklemin sürekli ve $F(0)=1$ olan **tek** çözümü üsteldir ⟹ **$n=1$**:
$$\boxed{\;P=P_0\,e^{-C\chi/P_0}\;}$$
*(Aynı teorem, ölçek çarpanlarının çarpımsal bileşmesi diliyle de kurulabilir — 11.4.8.1'in $\Lambda=\Lambda_{grav}\Lambda_{kin}$ yapısı. İkisi **aynı** teoremdir; iki bağımsız kanıt sayılmamalıdır.)*

**3. Üssün sayısal kapanışı — 4 çarpanı türetilmiştir, fit değildir.** M-46'nın zincir denetimi $C\chi/P_0=4\Phi/c_0^2$'dir ve buradaki 4, M-8'in sıkışma oranı $\rho_n/\rho_0$'ın ta kendisidir ($\omega_C K=4\mathcal{G}M$ tam özdeşliği). Dolayısıyla:
$$P(r)=P_0\,e^{-4\mathcal{G}M/c_0^2r}=P_0\,e^{-4\Phi/c_0^2},\qquad c_{loc}=\sqrt{P/\rho_0}=c_0\,e^{-2\Phi/c_0^2}$$

**4. Ölçek yapısı.** M-42'nin ilişkileri **aynen** korunur ($\ell,f\propto\Lambda$; $c_{loc}=c_0\Lambda^2$; $n_{eff}=1/\Lambda^2$; yerel Lorentz null); değişen yalnız $\Lambda$'nın biçimidir:
$$\boxed{\;\Lambda=e^{-\Phi/c_0^2}\;;\qquad \Lambda=1-\frac{\Phi}{c_0^2}+O\!\left(\frac{\Phi^2}{c_0^4}\right)\ \text{(birinci mertebe kesiti)}\;}$$

**5. Eylem düzeyi ve $\chi$ denkleminin korunumu.** İç enerji **çarpımsal** yazılır: $U(\rho,\chi)=g(\chi)\,c_0^2\rho\ln(\rho/\rho_0)$ ile $g=\Lambda^4$; buradan $P=\rho U_\rho-U=g(\chi)c_0^2\rho$. $\rho=\rho_0$'da $\partial U/\partial\chi=0$ olduğundan **M-46'nın Poisson denklemi bozulmaz**. Maxwell (çapraz türev) koşulu da yalnız bu biçimde sağlanır: $\partial^2P/\partial\chi\partial\rho$ iki yoldan aynı çıkar.

**6. GW170817 kilidi — Merkür'den bağımsız ikinci gözlemsel dayanak.** Çarpımsal biçimde
$$\left(\frac{\partial P}{\partial\rho}\right)_{\!\chi}=\frac{P}{\rho}=c_{loc}^2 \quad\textbf{her noktada}$$
yani sıkışma dalgası ile Zerre **aynı yerel hızı** paylaşır ve hız farkı **özdeş sıfırdır**. Toplamsal (lineer) biçimde ise $(\partial P/\partial\rho)_\chi=c_0^2$ sabit kalırken $P/\rho=c_{loc}^2$ kuyuda düşer; ikisi ayrışır:

| Ortam | $\Phi/c_0^2$ | lineer okumada $\lvert\Delta v\rvert/v$ | üstel |
|---|---|---|---|
| Dünya yüzeyi | $7{,}0\times10^{-10}$ | $1{,}4\times10^{-9}$ | 0 (özdeş) |
| Samanyolu | $4{,}5\times10^{-7}$ | $\mathbf{8{,}9\times10^{-7}}$ | 0 (özdeş) |
| Güneş yüzeyi | $2{,}1\times10^{-6}$ | $4{,}2\times10^{-6}$ | 0 (özdeş) |

GW170817 kısıtı $4{,}2\times10^{-16}$'dır: **lineer okuma Samanyolu potansiyelinde bile dokuz mertebe ihlal eder.** Dolayısıyla **üstel biçim, M-44'ün "otomatik sağlanır" iddiasını gerçekten otomatik yapan tek biçimdir** — ve bu, kitapta kayıtlı olmayan bir ikinci-mertebe iç tutarsızlığın düzeltme kaydıdır (bkz. M-44 Adım 2'nin düzeltmesi).

**7. Pozitiflik.** Lineer profil $P=P_0(1-4\Phi/c_0^2)$, $r<4\mathcal{G}M/c_0^2$'de $P<0$ verir ve **M-7'nin yırtılmama koşulunu ihlal eder**; üstel biçim hiçbir $r$'de ihlal etmez. Merkür'den bağımsız, üçüncü bir yapısal gerekçe.

### Sonuç
$$\boxed{\;\Lambda=e^{-\Phi/c_0^2},\qquad c_{loc}=c_0\Lambda^2=c_0e^{-2\Phi/c_0^2},\qquad P=P_0\Lambda^4=P_0e^{-4\Phi/c_0^2},\qquad n_{eff}=\frac{1}{\Lambda^2}\;}$$
$$\boxed{\;\gamma_{PPN}=1,\qquad \beta_{PPN}=1\;}$$

### Sayısal Çapraz Kontroller
**(a) Günberi kayması** (teorinin kendi eyleminden, $S=-mc_0^2\!\int\!\Lambda_{grav}\sqrt{1-V^2/c_{loc}^2}\,dt$; mpmath 60 hane):

| Gezegen | ÜSTEL (″/yy) | LİNEER (″/yy) | GR/ölçüm | üstel/GR |
|---|---|---|---|---|
| **Merkür** | **42,9805** | 50,1439 | $42{,}9799\pm0{,}0009$ | **1,0000001** |
| Venüs | 8,6246 | 10,0620 | 8,6246 | 1,0000001 |
| Dünya | 3,8387 | 4,4785 | 3,8387 | 1,0000000 |
| Mars | 1,3509 | 1,5761 | 1,3509 | 1,0000000 |
| Ikaros (1566) | 10,0560 | 11,7320 | 10,0560 | 1,0000001 |

Üstel **0,69σ**; lineer **7960σ** ile dışlanır. Yayınlanmış $\beta$ kısıtıyla ($\beta-1=(-2{,}7\pm3{,}9)\times10^{-5}$, Park ve ark., 2017) bağımsız denetim: üstel 0,69σ, lineer $1{,}3\times10^4\sigma$.
**Nordtvedt çapraz denetimi:** $\eta_N=4\beta-\gamma-3$; üstel **0** (tam), lineer $-2$; LLR sınırı $\lvert\eta_N\rvert<4{,}5\times10^{-4}$ ⟹ lineer Merkür'den **bağımsız olarak** da ölür.

**(b) Korunan gözlemler (tam integrallerle).** Işık bükülmesi 1,7512″ (GR'dan fark $7{,}3\times10^{-7}$″ = ölçüm hassasiyetinin %0,4'ü) · Shapiro (Dünya–Mars teğet) 247,24 µs (kayıtlı 247) · kızıla kayma $-\Phi/c_0^2$ · jeodetik presesyon 6.606 mas/yıl (Fermat holonomisi birinci mertebede değişmez) · GP-B $\xi$ zinciri · Lorentz null'ları · $P_0=\frac14\rho_nc_0^2=6{,}07\times10^{33}$ Pa. **M-8'in kalibrasyon zinciri korunur:** $\Delta P_{yüzey}=\rho_n\Phi$ (oran 0,9999999986) ve $\delta c/c_0=-2\Phi/c_0^2$ (oran 0,9999999993) üstel biçimin birinci mertebe açılımlarıdır; tam biçim $-\ln(P/P_0)=4\Phi/c_0^2$'dir.

**(c) Tepki üssü kilidi.** $\beta=2n-1$ ailesi altı değerde sayısal doğrulandı ($n=0\to\beta=-1$; $n=1\to\beta=+1$; $n=1{,}5\to\beta=+2$). Merkür'ün $\pm0{,}0009$″ hassasiyeti **$n=1{,}000000\pm3{,}1\times10^{-5}$** verir.

**(d) Güçlü alan — gölge (Bouguer değişmezi $b=n_{eff}(r)\,r$'nin ekstremumu).** $n_{eff}=e^{2\mu/r}$ ile $r_{ph}=2\mu$, $b_{krit}=2e\,\mu=5{,}4366\mu$; GR: $3\sqrt3\,\mu=5{,}1962\mu$ ⟹ **$+\%4{,}63$**.

| Nesne | GR gölge çapı | ÜSTEL | EHT halka ölçümü |
|---|---|---|---|
| Sgr A* | 53,27 µas | **55,73 µas** | $51{,}8\pm2{,}3$ µas (1,04σ) |
| M87* | 39,70 µas | **41,53 µas** | $42\pm3$ µas (0,65σ) |

**(e) Ufuk ve kızıla kayma.** $\Lambda=e^{-\mu/r}$ hiçbir **sonlu** $r$'de sıfırlanmaz ⟹ **ufuk yok, tekillik yok**; kızıla kayma sonludur ($r=2\mu$'de $1+z=1{,}65$). Standart görelilikte $r=R_s$'de $z\to\infty$'dur — **kategorik ayrım.**

**(f) İkinci mertebe ayrışması nerede başlar.** Işık bükülmesinde üstel/GR oranı: Güneş kenarında 1,0000004 (görünmez), $b=10\mu$'de 1,034, $b=6\mu$'de 1,163. **Ayrışma yalnız güçlü alandadır** — tam da EHT'nin baktığı yerde.

### Kazanç–kayıp muhasebesi
**Kazanılan.** Merkür kapandı (sıfır yeni parametre) · $\beta_{PPN}$ belirsiz kalemden **türetilmiş+sınanmış** kaleme geçti · M-46'nın kendi ilan ettiği güçlü-alan boşluğu doldu · M-44'ün GW170817 iddiası gerçekten otomatik oldu (ve kayıtsız bir iç tutarsızlık kapandı) · ufuk ve tekilliğin yokluğu iddia olmaktan çıkıp **yapısal sonuç** oldu · lineer yazımın ikinci mertebede **tanımsız** olduğu ortaya çıktı ve giderildi.
**Kaybedilen.** $\beta=1$ ile teori **1PN düzeyinde ve $\beta$ mertebesinde** GR'dan gözlemsel olarak ayrışmaz. 7.4 md.14'ün *"ayırt edicilik için en umut verici yer"* ve H.2'nin *"ayrışmanın aranacağı tek yer"* ifadeleri **düşer**. Bu, 11.4.8.1'in $\Lambda_{kin}$ turuyla aynı türden **ikinci** kayıptır: teori bir arenada daha Einstein fenomenolojisini birebir üretir.
**Doğan yeni ayırt ediciler.** Gölge çapı $+\%4{,}63$ (parametresiz; bugünkü EHT sistematiğiyle **ayırt edilmez**, ngEHT sınıfı duyarlılıkla belirleyici olur) · ufuk yokluğu / sonlu kızıla kayma (kategorik, ölçüm yolu tanımlanmadı).

### Geçerlilik Sınırı
- **Merkür yalnız $\kappa=1$'i (yani $\beta$'yı) sınar, üstel biçimi seçmez.** GR'ın izotropik ölçeği de $\kappa=1$'dir, üstel **değildir** ve **ufku vardır**; $x^3$ katsayısı 100'e kadar Merkür tarafından ayırt edilmez. Üstel biçimin kendine özgü içeriği (ufuksuzluk, gölge) **Adım 2'nin form-değişmezliğine ve Adım 6'nın GW170817 kilidine** dayanır — Merkür'e değil.
- **Saf M-2 tek başına Merkür'ü vermez ve işareti ters verir.** Kütle-itim yasası $\vec a=-\nabla P/\rho_n$, üstel profille bile $-28{,}65$″/yy ($=-\tfrac23\times$GR) verir. Doğru sonuç yalnız **tam eylemden** çıkar: $-0{,}667$ (M-2'nin statik kanalı) $+1{,}667$ (hız-bağımlı terimler, $\Lambda_{kin}$) $=1{,}000\times$GR. Yani 43″'nin %167'si M-2'de olmayan terimlerdendir; **M-2, arka plan koordinat biçiminde yazılmış statik limittir** (M-2'nin işaret konvansiyonundaki iz/izsiz kaydıyla birlikte okunmalıdır).
- **$a=-\nabla P/\rho_n$ ile etkin yapının statik ivmesinin birebir örtüşmesi bir kimliktir, delil değildir:** $P=P_0\Lambda^4$ verildiğinde her iki yol $-c_0^2\Lambda^3\Lambda'$ verir — **her $\Lambda$ için**. Bu örtüşme yalnız **üs muhasebesinin** (4 çarpanının) tutarlılığını denetler.
- **Profilin geçerlilik tabanı $r\gtrsim0{,}20\,\mu$'dur.** M-7'nin yırtılmama tabanı ($P_{yırt}/P_0=2{,}6\times10^{-9}$) üstel profili $r\approx0{,}2025\mu$'de keser; o yarıçapta $1+z\le140$. Daha derin değerler (ör. $r=0{,}1\mu$) profilin geçerlilik bölgesi **dışındadır** ve kullanılmamalıdır.
- **Derin kuyuda ikinci mertebe ihmal edilemez:** nötron yıldızı yüzeyinde $\Delta P_{üstel}/\Delta P_{lineer}=0{,}72$ (%28 kayma). $\xi$, M-40 zinciri ve NS kızıla kaymaları bu rejimde yeniden hesaplanmalıdır. "İkinci mertebe ihmal edilebilir" kaydı yalnız **zayıf alan** için geçerlidir.
- **Yörünge sonuçları ortamın durgunluğuna bağlıdır** ve bu koşul **M-51–M-54**'te kurulmuştur (dört bağımsız gövdede dolaşım dışlandı; kesme salınımının genlik kısıtı $w\le0{,}02v_{yör}$). Ortam dolaşıyor olsaydı apsis sürüklenmesi sonucu yok ederdi.
- **İkili pulsar sınavı geçilmiş sayılmamalıdır.** PSR B1913+16'nın $\dot\omega=4{,}2266$°/yıl'ı 1PN'dir ve kütlelerle **tam dejeneredir**; asıl 2.5PN sınavı $\dot P_b$'dir ve M-44'ün Açık Uçlar'ındaki $10^9$ kat fazlalık kalemi **hâlâ açıktır**. Üstel yapı bu sınavı geçmez, **erteler**.
- Yapı $O(\Phi^2)$ mertebesine kadar GR ile $g_{tt}$'de özdeştir ($1-2x+2x^2$); ayrışma $O(\Phi^3)$'te başlar.

### Açık Uçlar
- **$\gamma_\ell=-1$'in mekanizması** (cetvellerin neden tam $\Lambda$ ile büzüldüğü) hâlâ yerel değişmezlik gözleminden sabitlidir. Üstel yapı $\Lambda$'nın **biçimini** türetir, cetvel kanalının **üssünü** türetmez. *(Hareket kolundaki karşılığı 11.4.8.1'de kapanmıştır.)*
- **$r_{ISCO}$ ve kritik dönüş limitleri** ufuksuz yapıda yeniden türetilmelidir (4.2.16'nın kalan kalemi); üstel metrikte hesaplanmamıştır.
- **Karadelik eşiğinin yeniden temellendirilmesi.** $r_{ph}=2\mu$ Schwarzschild yarıçapıyla **sayısal olarak birebir** çakıştığı için $M_{min}\approx8{,}3\,M_\odot$ formülü ve 11.3'ün yükleme yasası/tavan sonuçları (897,5 ↔ $m_p/2m_e=918$; 2.527 pulsarda $a^*\le1$) **sayısal olarak ayaktadır**; ama mekanizmanın **adı** "ufuk"tan "foton küresi / gölge yarıçapı"na çevrilmelidir. Eşiğin anlamı da değişir: ufuk eşiği değil **gölge eşiği** — altındaki cisimler "karadelik oluşamaz" değil **"gölge vermez"**.
- **Yıldız-kütleli cisimlerde yüzey ışıması.** Ufuk olmadığından $\rho_n$-gövdesinin yüzeyi sonlu kızıla kaymada kalır (10 $M_\odot$: $R_\rho\approx26$ km, $1+z\approx1{,}8$); süperkütlelilerde sorun yoktur (M87*: $1+z=e^{4{,}3\times10^5}$). Teorinin cevap adayı, kilitli kafesin bir **büyüme cephesi** olması ve enerjinin kafes bağlanmasına gitmesidir; **nicelleştirilmemiştir.** Type-I patlama yokluğu ve Sgr A* yüzey-ışıma üst sınırları bu kalemi doğrudan sınar. Aynı zamanda **yıldız-kütleli ↔ süperkütleli arasında keskin bir yanlışlanabilir ayrım** öngörüsü doğurur.
- **$\Phi$'nin tanımı.** Üstel biçimde $\Phi\equiv(P_0-P)/\rho_n$ ile $\Phi=\mathcal{G}M/r$ **aynı anda tam olamaz**. Ek D · S-28'in kararı: $\Phi\equiv-\frac{c_0^2}{4}\ln(P/P_0)$ (logaritmik kuyu derinliği) ikisini birden tam yapar ve zayıf alanda eski tanıma iner.
- **Ortamın uzaysal erimi** ve $\Lambda\to0$ derin rejiminde hâl denkleminin stiff kalıp kalmadığı — M-3′'ün açık ucuyla ortak kalem.
- ~~Ortamın $O(\Phi^2)$ tepkisinin $P(\Phi)$ hâl ilişkisinden türetilmesi~~ → **bu girdiyle kapandı.**

### Elenen gerekçeler — dürüst kayıt
Bu girdi hazırlanırken iki gerekçe denendi ve **çürütüldü**; kitaba girmemeleri kayda geçirilir:
1. **"Stiff ortamda hacim modülü basıncın kendisidir ($K=\rho c_0^2=P$), dolayısıyla tepki çarpımsaldır."** M-44'ün varlık nedeni olan iki-kısmi-türev ayrımını çiğner: $K=\rho(\partial P/\partial\rho)_\chi$ **birinci** türevdir ve deplasman kanalında sabittir ($=\rho_0c_0^2=P_0$), oysa gereken $(\partial P/\partial\chi)_\rho$'dur; ayrıca $K$ hacimsel zorlanmanın katsayısıdır ve bu kanalda $dV/V=0$'dır. Argüman ciddiye alınırsa üs **1** çıkar ($k=1$, M-8'i öldürür), oysa doğru üs 4'tür ve $\rho_n/\rho_0$'dan gelir.
2. **"Deplasman alanı basınca değil entalpiye lineer bağlanır."** $h=c_0^2\ln(P/P_0)$ **$\rho$-kanalının** entalpisidir (orada $\rho$ değişir); kuyu profili ise **deplasman kanalıdır** ($\rho$ sabit). O kanalda $h\propto P$ özdeş olduğundan bu okuma hiçbir ayrım üretmez.
Geçerli gerekçeler yalnız Adım 2 (form-değişmezliği), Adım 6 (GW170817) ve Adım 7 (pozitiflik)'tir.
