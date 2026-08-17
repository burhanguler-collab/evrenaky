# Ek M — Merkezî Türetim Kataloğu · Blok F: Makro Evren Dinamiği

Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.

---

## M-22 · Radyal Momentum Dengesi: $dP/dr = \rho v_\theta^2/r$ · **[T]** · *DENGE YASASI (kuvvet değil)*

> **Kategori kaydı (3 Ağustos 2026).** Bu girdi bir **kuvvet değil, denge yasasıdır**: alanı üretmez, alana verilen **tepkiyi** belirler. Beş hidrodinamik kuvvetin içindeki rolü ve ondan çıkan **Ortam–Madde Kayma Yasası** ($v_\theta=2v_{madde}$), Blok H'nin *"Denge Yasaları — kuvvet değil, tepki"* bölümünde (M-39'dan sonra, **DY-1**) kurulmuştur. Kuvvetlerle **toplanmaz:** F1 gradyanı kurar, M-22 o gradyanın ortamın dönüşüyle dengede olduğunu söyler — ikisi **aynı gradyandır.**

**Kullanıldığı bölümler:** 3.4.1 (kütle-itim ispatı), 3.10.2 (işaret zemini), 3.6.2 (atmosferik burulma zemini), 4.2.9.2 (galaktik rejime geçiş), **11.3.1** (iki denge / iki yoğunluk). Bağlı katalog: **M-9** (ortamın dolaşma teoremi), M-8 ($\rho_0=\rho_n/4$), M-25 (muhasebe zincirleri).

### Varsayımlar
1. Evrenakı, Navier-Stokes denklemine tabi sıkıştırılabilir bir akışkandır (Postülat 1); viskozitesi sıfıra çok yakındır: $0 < \mu \ll 1$ (Postülat 7; $\mu$ sembolü yalnız bu standart alıntıda geçer, teorinin kendi viskozite parametresi $\eta_E$'dir — S-19).
2. Kütle çevresindeki makro girdap **kararlı** ($\partial\vec v/\partial t = 0$) ve **eksenel simetriktir**; akış alanı saf teğetseldir: $\vec v = v_\theta(r)\,\hat e_\theta$.
   > **⚠ Statü kaydı (17 Ağustos 2026).** Bu varsayım, ortamın dolaştığı **opsiyonel bir dinamik durumu** tanımlar; zorunluluk değildir. Kohezyonlu ortam kuyuyu dolaşmadan da tutabilir (**Ek M-51**) ve gezegen ölçeğinde dolaşım **gözlemle dışlanmıştır** (**Ek M-52**: dolaşan ortamda apsisler $\Omega_m=2n$ ile sürüklenir, kapalı elips kalmaz; dört bağımsız gövdede dışlama $10^2$–$10^6$). Bu girdinin **madde** tarafındaki sonuçları (radyal denge, kuyu konvansiyonu) etkilenmez; etkilenen yalnız ortamın kendi teğetsel alanına ilişkin okumalardır.

### Adımlar
1. Standart Navier-Stokes denkleminden başlanır:
$$\rho\left(\frac{\partial \vec v}{\partial t} + (\vec v\cdot\nabla)\vec v\right) = -\nabla P + \mu\nabla^2\vec v$$
2. $\mu \to 0^+$ idealleştirmesiyle denklem Euler biçimine sadeleşir:
$$\rho\left(\frac{\partial \vec v}{\partial t} + (\vec v\cdot\nabla)\vec v\right) = -\nabla P$$
3. Silindirik koordinatlarda, kararlı saf dönüş için konvektif terimin radyal bileşeni merkezcil ivmedir: $\big[(\vec v\cdot\nabla)\vec v\big]_r = -v_\theta^2/r$. Euler denkleminin radyal bileşeni böylece momentum dengesine (siklostrofik denge) indirgenir:
$$-\rho\frac{v_\theta^2}{r} = -\frac{dP}{dr}$$
4. Sağ taraf düzenlenince sonuç çıkar; $dP/dr$ **kesinlikle pozitiftir** — merkeze yaklaştıkça hız artar, statik basınç düşer; dışarı doğru basınç yükselir. Bu, M-2'nin kuyu konvansiyonunun ($dP/dr > 0$) hidrodinamik ispatıdır: cismi merkeze iten şey gradyanın kendisi değil, itim yasasındaki eksi işarettir — kuvvet daima $-\nabla P$'dir, cismin ivmesi $\vec a = -(1/\rho_n)\nabla P$ (M-2).

### Sonuç
$$\boxed{\frac{dP}{dr} = \rho\,\frac{v_\theta^2}{r} \;>\; 0}$$

Newton'un "çekim" (pull) soyutlaması yerine mekanik zemin: uzayın derinliklerindeki yüksek statik Evrenakı basıncı, kütle çevresindeki düşük basınç havzasına doğru cisimleri kesintisiz **iter** — kütle-itim, Euler denkleminin matematiksel zorunluluğudur.

### Merkezkaçın Mekanik Temeli — ve maddenin ortama tutunamaması

Klasik mekanikte merkezkaç, dönen çerçevede tanımlanan **sanal** bir etkidir. Evrenakı'da karşılığı sanal değildir: dönen ortamın **ataleti gerçektir** ve onu dengeleyen **basınç gradyanı da gerçektir.** M-22 tam olarak bu dengeyi yazar. İki tarafın yönü karıştırılmamalıdır:

| Terim | Yön | Nedir |
|---|---|---|
| $\rho_0\,v_\theta^2/r$ | **dışa** | ortamın kendi **ataleti** (dönüşün merkezcil gereksinimi) |
| $-\,dP/dr$ | **içe** | basınç gradyanının kuvveti |

$dP/dr>0$ olması basıncın **dışa doğru arttığı** anlamına gelir; kuvvet ise daima $-\nabla P$'dir, dolayısıyla **içe** bakar. Dönen kovada suyun kenarda yükselmesi gibi: kenarda basınç yüksektir ve suyu dairede tutan şey kenardan eksene doğru olan **içe** gradyandır. Klasik "Çekim vs Merkezkaç" ikiliği burada iki rakip kuvvet değil, **tek bir gradyanın tek bir atalete karşı dengesidir.**

**Dengenin ikinci sonucu — gerçek dışa savrulma.** Aynı gradyan, ortama $\rho_0$ ile, maddeye $\rho_n$ ile etki eder (M-2). M-8'in sonucuyla $\rho_n = 4\rho_0$ olduğundan — *madde, okyanusun yalnızca ~4 kat sıkışmış girdap fazıdır* — maddenin aynı noktada eline geçen ivme ortamınkinin dörtte biridir:

$$a_{madde}=\frac{1}{\rho_n}\frac{dP}{dr}=\frac{\rho_0}{\rho_n}\cdot\frac{v_\theta^2}{r}=\frac{1}{4}\cdot\frac{v_\theta^2}{r}$$

Madde, ortamın dolaşım hızında dönmeye kalksaydı gereken merkezcil ivmenin ancak **dörtte birini** alırdı — yetersiz merkezcil kuvvet demektir, **dışa savrulur.** Ancak kendi ataletinin gradyanın verebildiğine eşitlendiği hızda dengeye oturur:

$$\frac{v_{madde}^2}{r}=\frac{1}{4}\frac{v_\theta^2}{r} \;\Longrightarrow\; \boxed{\;v_{madde}=\frac{v_\theta}{2}\;}$$

Santrifüjde yoğun maddenin dışa çökmesiyle **aynı mekanizmadır**: madde ortama göre fazla yoğun olduğu için dolaşıma tutunamaz. Bu, **M-9**'un *"madde düşer, ortam düşmez"* ifadesinin mekanik nedenidir *(ortamın cevabının dolaşım mı gerilme mi olduğu ayrı sorudur: Ek M-51/M-52 gerilme kolunu seçer)* ve 2 çarpanını görmenin üçüncü bağımsız yoludur (diğerleri: M-9'un doğrudan ifadesi ve M-25'in muhasebe zincirleri).

> **Sonuç — kapılış yörüngeyi sağlamaz.** Madde ortamın hızına kilitli olsaydı dışa savrulurdu; gözlem gezegenleri $v_{madde}=\sqrt{\mathcal{G}M/r}$'de, yani ortamın **yarı hızında** bulur. Sürüklenme zarfının rolü (Postülat 7) yörüngeyi üretmek değil, **yerel bağıl hızı sıfırlayarak sürüklemeyi bastırmaktır** (M-37 sıfırıncı mertebe; M&M null'unun kaynağı). *(İki yaygın hata: gradyanı "dışa doğru itim" saymak, ve F1 ile M-22'yi iki rakip kuvvet gibi yazmak. Gradyan **içe** iter; M-22 rakip bir kuvvet değil, F1'in kurduğu gradyanın ortamın dönüşüyle dengede olduğunu söyleyen bir **denge koşuludur.** "Merkezkaç reel olmalı" tezi geçerlidir — reellik gradyanın yönünden değil, ataletin gerçekliğinden ve iki yoğunluğun farkından gelir.)*

### Geçerlilik Sınırı
- Kararlı, eksenel simetrik, viskoz terimi ihmal edilmiş rejim.
- **Rejim notu:** Hız profili denkleme dışarıdan girer ve iki rejim ayrışır. Güneş sistemi ölçeğindeki **lokal (Kepler) girdapta** $v_\theta \propto 1/\sqrt{r}$ (M-25) ile $dP/dr \propto 1/r^2$ çıkar — klasik gözlemle örtüşen kuyu. **Galaktik düz-hız rejiminde** ($v_\theta \approx$ sabit) ise $dP/dr \propto 1/r$, yani **logaritmik basınç kuyusu** doğar (4.2.9.2; tam türetim M-30'da).

### Açık Uçlar
- $v_\theta(r)$ profilini iki rejim arasında tek denklemde bağlayan geçiş fonksiyonunun türetimi (M-30, 7.4).
- Kuyunun $\rho(r)$ eşlik profilinin ($k$ eşlik oranıyla, M-8) kapalı çözümü.

---

## M-23 · Coriolis Biçiminin Türetimi · **[T (kısmi)]**

**Kullanıldığı bölümler:** 3.6.3 (matematiksel ispat), 3.6.2 ve 3.6.4–3.6.5 (fırtına/kasırga yön imzaları).

### Varsayımlar
1. Dönen bir gezegen çevresindeki toplam Evrenakı hız alanı iki **fiziksel** bileşenin toplamıdır:
$$\vec v = \vec v_{basınç} + \vec v_{dönüş}$$
$\vec v_{basınç}$: gezegene inen radyal kütle-itim akışı; $\vec v_{dönüş}$: gezegenin dönüşünün akışkana verdiği rotasyon alanı.
2. Rotasyon alanı katı-cisim biçimindedir: $\vec v_{dönüş} = \vec\Omega_{dön}\times\vec r$ (gezegen dönüş vektörü $\vec\Omega_{dön}$ sabittir; Ek D · S-7 — kaynak metinde $\vec\Omega$ yazılıdır, katalogda yörünge frekansı $\Omega_{yör}$ ile karışmaması için $\Omega_{dön}$ kullanılır).

### Adımlar
1. Akışkan ivmesindeki konvektif türev $(\vec v\cdot\nabla)\vec v$, toplam hız yerleştirilince çapraz etkileşim terimleri üretir; incelenen terim:
$$(\vec v_{basınç}\cdot\nabla)\,\vec v_{dönüş}$$
2. Sabit $\vec\Omega_{dön}$ için vektör kimliği doğrudan uygulanır:
$$(\vec v_{basınç}\cdot\nabla)(\vec\Omega_{dön}\times\vec r) = \vec\Omega_{dön}\times\vec v_{basınç}$$
Bu, standart fizikteki Coriolis ivmesinin (Coriolis, 1835) temel matematiksel formudur.
3. **Yön tayini (determinant hesabı).** Kartezyen eksenlerde ($x\to$ doğu, $y\to$ kuzey, $z\to$ yukarı), $\vec\Omega_{dön}=(0,0,\Omega_{dön})$ ve $\vec v_{basınç}=(v_x,v_y,0)$ için:
$$\vec a = \vec\Omega_{dön}\times\vec v_{basınç} = \begin{vmatrix}\hat i & \hat j & \hat k\\ 0 & 0 & \Omega_{dön}\\ v_x & v_y & 0\end{vmatrix} = (-\Omega_{dön}v_y,\ +\Omega_{dön}v_x,\ 0)$$
4. **İşaret analizi.** Türetilen terim, Euler denkleminin sol tarafındaki konvektif ivmede yaşar; parselin hareket denklemine taşındığında etkin saptırıcı ivme $-\vec\Omega_{dön}\times\vec v_{basınç}$ olur. Kuzey Yarımküre'de ($\Omega_{dön}>0$) bu, hareketin **sağına** doğru sapmadır: alçağa koşan her parsel sağa kayar; alçak çevresindeki denge dolaşımı bu yüzden **CCW (siklonik)** kurulur — içe bakan basınç gradyanını ancak dışa bakan saptırıcı ivme dengeler. Güney Yarımküre'de ($\Omega_{dön}<0$) işaretler döner: parsel **sola** sapar, dolaşım **CW**. Yön deseni varsayım değil, türetilmiş sonuçtur. *(Düzeltme kaydı, 9 Ağustos 2026: eski yazım "hareket sola (CCW) bükülür" diyordu — parsel sapması ile dolaşım yönü karıştırılmıştı; gözlemsel sonuç — KYK'de siklon CCW — değişmedi, gerekçe zinciri düzeltildi.)*
5. **Gözlemsel çapa:** Kontrollü küvet-girdabı deneyi (Shapiro, 1962), yarımküre işaret desenini laboratuvarda doğrular.

### Sonuç
$$\boxed{\vec a_{sapma} = -\,\vec\Omega_{dön}\times\vec v_{basınç} \qquad \text{KYK: parsel sağa sapar} \Rightarrow \text{alçak çevresi dolaşım CCW;\ \ GYK: tersi (CW)}}$$

Coriolis terimi burada yeni bir kuvvet değil, ontoloji düzeltmesidir: dönen çerçevenin "sanal" ivmesi değil, radyal basınç akışı ile makro-vorteks alanı arasındaki **gerçek momentum transferidir**.

### Geçerlilik Sınırı
Sabit $\vec\Omega_{dön}$, yatay düzlemde hareket, tek çapraz terimin izolasyonu. Türetim, Coriolis ivmesinin *biçimini* ve *işaret desenini* verir; tam katsayı için aşağıdaki açık uca bakınız.

### Açık Uçlar
- **2 çarpanının tam gösterimi** (ikinci çapraz terimin $(\vec v_{dönüş}\cdot\nabla)\vec v_{basınç}$ ve zaman türevinin katkısı) **açık hesap kalemidir**; kaynak metindeki "Euler'in diğer terimleriyle 2 çarpanı da doğrudan elde edilir" ifadesinin açık hesabı henüz yazılmamıştır. Rozetin **[T (kısmi)]** kalmasının nedeni budur.

---

## M-24 · Kavrama/Kilitlenme Denklemi · **[K]**

**Kullanıldığı bölümler:** 3.4.4 (ana metin + Şekil 3.4.1–3.4.2 + Animasyon 3.4.2), 3.9.1 (Ay'ın 1:1 senkron kilidi), 3.8.2 (girdap rekabeti bağlamı), 7.4 (açık hesap kalemleri).

> **Rozet gerekçesi (peşin dürüstlük):** Bu girdinin ana denklemi bir **ilk-ilke türetimi değil**, gözlemle kalibre edilmiş bir çerçevedir. Kavrama klifi $g(R)$ dört veri noktasına iki parametreyle oturtulmuş **betimleyici bir fittir**; Venüs satırındaki $\sigma\Gamma/k_g \approx 2$ oranı ölçümden kalibre edilmiştir. Yalnızca günberi-ritmi alt-bağıntısı $q_{peri}(e)$ türetilmiştir ve ayrıca **[T]** ile işaretlenmiştir. Bu kayıt kaynak metinde (3.4.4, dürüst kayıt paragrafı) aynen mevcuttur.

### Varsayımlar
1. Her kütlenin dördüncü boyut mikro-motorları, cisme kütlesiyle orantılı bir serbest dönüş ifadesi ($\omega_{serbest}(M)$) yüklemeye çalışır (3.8.2).
2. Merkez yıldızın makro girdabı, kendi kavrama bölgesi içindeki cisimlerin bu ifadesini bastırır ve kalıntı dönüşü **yerel girdap ritmine** ($\Omega_{yör}$) kilitler.
3. Kavrama en şiddetli günberide etkir (klif dikliği nedeniyle pençe fiilen günberide kavrar).

### Bileşenler ve Adımlar
1. **Kavrama derecesi (tanım):**
$$g \equiv 1 - \frac{L_{gözlenen}}{L_{serbest}}$$
2. **Kavrama klifi** — dört iç gezegene uygulanan tanımdan çıkan dik geçiş, iki parametreli biçimle betimlenir:
$$g(R) = \frac{1}{1+(R/R_c)^p}, \qquad R_c \approx 1{,}0 \text{ AU}$$
**[K]:** Bu biçim **türetim değildir**; dört nokta / iki parametre ile betimleyici bir fittir.
3. **Kilit modları:** $q \in \{+\tfrac{3}{2},\ +1,\ \approx -1\}$. İlk ikisi serbest parametre değildir; günberi ritminden okunur (adım 4).
4. **Günberi ritmi alt-bağıntısı — [T]:** Kepler yörüngesinde açısal momentum $h=\sqrt{GMa(1-e^2)}$ ve günberi uzaklığı $r_p=a(1-e)$ ile günberi açısal hızı $\omega_{peri}=h/r_p^2$'dir; ortalama harekete ($\Omega_{yör}=\sqrt{GM/a^3}$) oranı doğrudan hesaplanır:
$$q_{peri}(e) = \frac{\omega_{peri}}{\Omega_{yör}} = \frac{\sqrt{1-e^2}}{(1-e)^2} = \frac{\sqrt{1+e}}{(1-e)^{3/2}} \;\longrightarrow\; \text{en yakın kararlı oran}$$
Ay ($e=0{,}055$): $1{,}12 \to 1{:}1$; Merkür ($e=0{,}206$): $1{,}55 \to 3{:}2$. İki mod arasındaki eşik $e \approx 0{,}125$'tir (R-6 bağlayıcı değeri). Ayırt edici öngörü: ötegezegen sistemlerinde $e\approx0{,}2$ civarında kilitlenmiş cisimler **daima 3:2'de** bulunmalıdır.
5. **Atmosferli gövdeler (yelken kanalı):** Kalın atmosfer ayrı bir kuplaj kanalı ($\sigma$) açar; doygun rejimde kalıntı kilit iki kanalın dengesinden seçilir:
$$\frac{\omega^\ast}{\Omega_{yör}} = q_{peri}(e) - \frac{\sigma\Gamma}{k_g}$$
Venüs kalibrasyonu **[K]**: $e=0{,}007 \Rightarrow q_{peri}=1{,}01$; ölçülen kilit $-0{,}92\,\Omega_{yör}$ ile $\sigma\Gamma/k_g = 1{,}01-(-0{,}92)=1{,}93\approx 2$. Aynı ifade parametresiz tarama yapar: Merkür ve Ay'da $\sigma=0$ (kilit $=q_{peri}$ ✓), Titan ve Dünya'da $\sigma\Gamma/k_g\ll1$ (prograd ✓).
6. **Ana denklem** — tüm tablo tek ifadede toplanır:
$$\omega_{gözlenen}(M,R) = \big[1-g(R)\big]\,\omega_{serbest}(M) + g(R)\,q\,\Omega_{yör}(R)$$
7. **Ölçekleme yasaları — [S] (log-log fit):** hizalı serbest gezegenler (Mars → Jüpiter) için $v_{ekv}\propto M^{0{,}54}$ ($R^2=0{,}98$) ve $L_{spin}\propto M^{1{,}94}$ ($R^2=1{,}00$); $\omega_{serbest}(M)$ bu doğrunun ekstrapolasyonundan okunur.

### Sonuç
$$\boxed{\omega_{gözlenen}(M,R) = \big[1-g(R)\big]\,\omega_{serbest}(M) + g(R)\,q\,\Omega_{yör}(R), \qquad q\in\left\{+\tfrac{3}{2},\ +1,\ \approx-1\right\}}$$

**Sayısal başarılar:** $g_\oplus = 0{,}39$ → Dünya'nın 24 saati (serbest ~14,5 saatlik ifadenin %61'i) kendiliğinden çıkar; Merkür'ün dönüş momentumunun **%97,7'si** yutulmuş, kalıntı $+\tfrac{3}{2}\Omega_{yör}$ (58,6 gün ✓); Venüs ~**244 gün ters** (gerçek: 243 gün, ters).

### Geçerlilik Sınırı
- Yasa, girdapla **hizalı** ($\theta \lesssim 30°$) **serbest-denge** cisimleri içindir; Merkür/Venüs "bastırılmış", Uranüs "hizasız" sınıfındadır (önceden tanımlı ölçüt, sonuca göre ayıklama değildir).
- Kapsam dışı: çökmüş cisimler (beyaz cüce, nötron yıldızı — açısal momentum korunumu dönüşü mertebelerce büyütür) ve beslenen cisimler (yığışma diskinden momentum alan milisaniye pulsarları).

### Açık Uçlar
- $g(R)$ klifinin ($R_c$, $p$) girdap rekabetinden ilk-ilke türetimi (7.4).
- $\sigma\Gamma/k_g$ oranının atmosfer kütlesi ve termal genlikten hesabı (Venüs'te yalnız kalibre, 7.4).
- Hizalanma verimi $f(\theta)$'nın türetimi; ötegezegen sınavı: eksen eğikliği ile dönüş hızı arasında negatif korelasyon (7.4).

---

## M-25 · Girdap Hız Profili ve Muhasebe Zincirleri: $v \propto 1/\sqrt{R}$ · **[T]** *(muhasebe girdileri: [S])*

**Kullanıldığı bölümler:** 3.8.1–3.8.1.1 (Güneş vorteksi + Açısal Momentum Paradoksu), 3.9.4 (Dünya-Ay muhasebesi), 3.8.2 (nedenselliğin tersinmesi), 3.4.4.

### Varsayımlar
1. **Gezegen girdaba kapılmaz; aynı basınç alanında düşer.** Madde $\vec a=-\nabla P/\rho_n$ ile serbest dengede dolanır; ortam ise aynı alana **düşerek** cevap vermez (**M-9**: *"madde düşer, ortam düşmez"*). Kohezyonsuz limitte ortamın cevabı dolaşmaktır ($\nabla P/\rho_0=v_\theta^2/R$; M-22), kohezyonlu Evrenakı'da ise **gerilmektir** (Ek M-51) — ve gözlem gerilme kolunu seçer (Ek M-52). *(Gezegenleri "akıntı katmanlarına kapılmış" saymak M-9 ile çelişir ve literal alındığında onları $2v_{Kepler}$'e koyar.)*
2. Kepler'in Üçüncü Yasası gözlemsel girdi olarak alınır: $T^2 \propto R^3$ (Kepler, 1619) **[S]**.
3. $\rho_0=\frac{1-k}{4}\rho_n$ ve $k=0$ (M-8) ⟹ $\sqrt{\rho_n/\rho_0}=2$ **tam**.

### Adımlar
1. Yörünge hızı tanımı $v = 2\pi R/T$, Kepler-3 ile birleştirilir:
$$T \propto R^{3/2} \;\Longrightarrow\; v_{madde} = \frac{2\pi R}{T} \propto \frac{1}{\sqrt{R}}$$
Bu **maddenin** profilidir. Ortamın profili aynı biçimi taşır, genliği iki katlıdır:
$$v_\theta(R)=\sqrt{\frac{\rho_n}{\rho_0}}\,v_{madde}(R)=2\sqrt{\frac{\mathcal{G}M}{R}}=2\,v_{kopma}(R)$$
Yani ortamın herhangi bir yarıçaptaki dolaşım hızı, o yarıçaptaki **kopma hızının tam iki katıdır.** Muhasebe zincirleri bu türetilmiş profille yürütülür.

2. **Muhasebe zinciri 1 — Güneş (girdiler [S]):** Güneş'in ekvator yüzey hızı 2 km/s'dir (Beck, 2000). Ortamın Merkür yörüngesindeki dolaşım hızı $2\times47{,}4=$ **94,8 km/s**, Güneş yüzeyinde ise $2\sqrt{\mathcal{G}M_\odot/R_\odot}=$ **874 km/s**'dir. Mekanik sürükleme hipotezi bu devri gövdenin yüzeyinden talep eder: ölçülenin **439 katı.** SOHO g-mode verisi (Fossat ve ark., 2017) çekirdeği yüzeyin 4 katında (~8 km/s) bulur — gereken değerin **yüz kattan fazla** altında. **Sonuç:** ne kabuk ne çekirdek; girdabın motoru gövdenin mekanik devri olamaz — motor, kütle nükleonlarının dördüncü boyut çift dönüş deşarjıdır (3.8.2).

3. **Muhasebe zinciri 2 — Dünya-Ay (girdiler [S]):** Ay'ın yörünge hızı 1,02 km/s'dir; ortam onun iki katı (2,04 km/s) ile dolaşır. Dünya yüzeyinde gereken dolaşım $2\sqrt{\mathcal{G}M_\oplus/R_\oplus}=$ **15,8 km/s**'dir. Gerçek ekvator hızı: **0,465 km/s** (R-6 bağlayıcı değeri) — açık **34 kat**. Sismolojik veri (PREM; Song & Richards, 1996; Vidale ve ark., 2000) iç çekirdeğin de neredeyse aynı yavaşlıkta döndüğünü gösterir: mekanik sürükleme muhasebesi her düzeyde çöker.

4. **İki zincirin ortak okuması — ve muhasebeyi kavramsal olarak kapatan gözlem.** 439 ve 34 katlık açıklar teorinin açmazı değil **keşif aracıdır.** Dahası, gereken devirler her iki gövdede de **kopma hızının tam iki katıdır** (Güneş: 874 = 2×437; Dünya: 15,8 = 2×7,91) — çünkü $v_\theta=2v_{kopma}$ bağıntısı bunu zorunlu kılar. Yani mekanik hipotez yalnızca "çok hızlı" bir dönüş değil, **gövdeyi dağıtacak devrin iki katını** talep eder: girdabı üretebilecek devirde gövde var olamaz. Muhasebe böylece sayısal olarak değil, yapısal olarak kapanır.

### Sonuç
$$\boxed{v_{madde}(R) \propto \frac{1}{\sqrt{R}}\,,\quad v_\theta(R)=2\,v_{madde}(R)=2v_{kopma}(R)\,,\quad \frac{v_{gereken}}{v_{mekanik}}\bigg|_{Güneş}\!\!=\frac{874}{1{,}99}\approx439\,,\quad \bigg|_{Dünya}\!\!=\frac{15{,}8}{0{,}465}\approx34}$$

### Geçerlilik Sınırı
Profil, merkez kütlenin baskın olduğu lokal (Kepler) girdap rejimi içindir; galaktik düz-hız rejimi (4.2.9.2, M-30) bu profilin dışındadır. Muhasebe zincirleri profili varsaymaz-doğrular döngüsüne düşmez: profil gözlemsel Kepler-3'ten, açıklar bağımsız hız ölçümlerinden gelir.

### Açık Uçlar
- Dördüncü boyut deşarjının girdaba yüklediği momentum debisinin nicel modeli (7.4).
- Fosil (kalıntı) momentumun ultra-düşük viskoziteli ortamdaki sönüm zaman ölçeği ($\eta_E^{etkin}$ M-43 çerçevesinde yazılınca; bkz. M-27/M-43).

---

## M-26 · Gelgit Elipsoidi ve Güneş/Ay Oranı · **[T]**

**Kullanıldığı bölümler:** 3.9.2 (yanal sıkıştırma mekanizması), 3.9.2.1 (suya batan top anomalisi), 3.9.2.2 (Güneş/Ay farkı).

### Varsayımlar
1. Gelgit bir "çekme" değil, Ay'ın Dünya-Ay arası Evrenakı akıntısını hızlandırmasıyla (Bernoulli, 1738: hız artan yerde iç basınç düşer) doğan **asimetrik yanal sıkıştırmadır** (squeeze).
2. Mekanizmanın hidrostatik analoğu: derinliği $d$ olan suya batırılmış, yarıçapı $r$ olan yumuşak top. *(Derinlik $d$ ile gösterilir; $h$ Planck sabitine ayrılmıştır — Ek D · S-4.)*

### Adımlar
1. Hidrostatik kuvvetler ($P = \rho g \cdot \text{derinlik}$):
$$F_{üst} \propto \rho g (d-r), \qquad F_{alt} \propto \rho g (d+r), \qquad F_{yan} \propto \rho g d$$
2. Kaldırma kuvveti alt-üst farkıdır: $F_{alt}-F_{üst} \propto 2\rho g r$. Bu pay ayrıldıktan sonra topu dikeyde karşılıklı ezen **efektif dikey sıkıştırma**, en zayıf kuvvete eşit kalır: $F_{dikey\_ezme} = F_{üst} \propto \rho g(d-r)$.
3. Karşılaştırma:
$$F_{yan} - F_{dikey\_ezme} \propto \rho g d - \rho g (d-r) = \rho g r > 0$$
Yanlar dikeyden daima daha şiddetli ezer; hacmini koruyan top, sıkışmadan kaçarak zayıf eksene doğru uzar → **elipsoid**.
4. Dünya'ya uygulama: Ay'ın yarattığı hız/basınç asimetrisi yan kuvvetleri baskın kılar; okyanuslar Ay eksenine doğru **ve** tam zıddına fışkırıp kabarır — çift şişkinlik, tek denklemden.
5. **Güneş/Ay oranı.** Sıkıştırmayı yaratan, kuvvetin toplam büyüklüğü değil cismin bir ucundan diğerine **değişimidir**: toplam kütle-itim kuvveti $\propto M/r^2$, gelgit gradyanı $\propto M/r^3$. Sayılar (NASA/JPL, 2024): $M_{Güneş}/M_{Ay} \approx 2{,}7\times10^7$, uzaklık oranı $390$, $390^3 \approx 5{,}9\times10^7$:
$$\frac{\text{Güneş gelgiti}}{\text{Ay gelgiti}} = \frac{2{,}7\times10^7}{5{,}9\times10^7} \approx 0{,}46$$
Toplam kuvvette 177 kat üstün olan Güneş (M-36'nın kendi girdi yuvarlamasıyla 179 — aynı oran; bu yüzden onun etrafında dolanırız), gradyanda Ay'ın **%46'sına** düşer — gözlemle uyum ✓ (Pugh & Woodworth, 2014).

### Sonuç
$$\boxed{F_{yan} > F_{dikey\_ezme} \;\Rightarrow\; \text{elipsoid uzaması}\,, \qquad \frac{\text{Güneş}}{\text{Ay}}\bigg|_{gelgit} = \frac{M_G/M_A}{(r_G/r_A)^3} = \frac{2{,}7\times10^7}{390^3} \approx \%46}$$

### Geçerlilik Sınırı
Hidrostatik analoji $r \ll d$ (cisim boyutu ≪ karakteristik uzaklık) limitinde kurulur; oran hesabı yalnız ölçekleme üstünden yürür ve katsayı iddiası taşımaz. Gradyanın $1/r^3$ ölçeklenmesi standart gelgit kuramıyla ortaktır — teorinin farkı sayıda değil, mekanizmadadır (çekme değil yanal sıkıştırma).

### Açık Uçlar
- Şişkinlik ekseninin Ay'ın önüne kayma açısının (~3°, gözlemle uyumlu) sürtünme-sürüklenme dengesinden nicel hesabı.
- Kabarma **genliğinin** (metre mertebesi) Evrenakı basınç asimetrisinden mutlak hesabı (7.4).

---

## M-27 · Halka Dikey Salınımı ve Ortam Sönümü · **[T]** *(sönüm terimi: $\eta_E^{etkin}$ — M-43 ile türetilmiş; serbest kalem boyutsuz $n$)*

**Kullanıldığı bölümler:** 3.10.2–3.10.7 (Satürn halka dinamiği), 6.3 (GPB tutarlılık uyarısı), Ek C ($\eta_E$ statüsü: M-43 ile türetildi, serbest kalem $n$).

### Varsayımlar
1. Uzay, sıkıştırılabilir süperakışkan Zerre ortamıdır; hareketi sıkıştırılabilir Euler denklemiyle (Euler, 1757) tarif edilir. *(Yerel alanlar $\rho$, $P$ ile gösterilir — Ek D · S-17/S-18; Zerre basınç alanı ile madde basıncı ayrı alanlardır.)*
2. Halka parçacıkları quasi-statik rejimdedir: $\partial\vec v/\partial t \to 0$, $(\vec v\cdot\nabla)\vec v$ ihmal edilebilir.
3. Kuyu konvansiyonu (M-2, M-22): kütle bir basınç çukurudur, $dP/dr>0$; itim $-\nabla P$'den gelir.
4. Ortam viskozitesi sıfıra yakın ama **tam sıfır değildir** (Postülat 7): $\eta_E > 0$ (dinamik viskozite, Pa·s — S-19). $\eta_E$ evrensel bir akışkan sabiti **değildir**; M-43'ün altkritik sürüklenme çerçevesi onu cismin boyutuna ve bağıl hızına bağlar: $\eta_E^{etkin}=C_D\,\rho_0\,a_b\,v_{bağıl}^4/(12\,v_{kav}^3)$.

### Adımlar
1. Sıkıştırılabilir Euler:
$$\rho\left(\frac{\partial\vec v}{\partial t} + (\vec v\cdot\nabla)\vec v\right) = -\nabla P + \rho\,\vec g_{ek}$$
($\vec g_{ek}$: dönme/entrainment kaynaklı ek terim, $\nabla P_{spin}$; bkz. 6.3.)
2. Quasi-statik limitte denklem basınç dengesine indirgenir ve **kalibre edilir**:
$$\frac{1}{\rho}\frac{dP}{dr} = +\frac{GM}{r^2} \quad\Rightarrow\quad a_r = -\frac{1}{\rho}\frac{dP}{dr} = -\frac{GM}{r^2}$$
**Dürüst not (kaynaktan aynen):** güneş sistemi ölçeğinde gradyanın $GM/r^2$'ye eşitlenmesi teorinin rejim aksiyomudur (4.2) — **bu satıra kadar hiçbir yeni fiziksel içerik yok**; yalnızca Newton yasasının Zerre diliyle yeniden yazımı. $G$ ve $GM$ burada kalibrasyon bağlamında kullanılır.
3. Parçacık düzlemden $z$ kadar saptığında gradyanın dikey izdüşümü:
$$F_z = -\frac{GMm}{R^2}\sin\theta, \qquad R=\sqrt{r^2+z^2},\quad \sin\theta = \frac{z}{R}$$
4. $z \ll r$ limitinde ($R^3\approx r^3$) harmonik salınım çıkar (dikey salınım frekansı $\Omega_z$ — S-7):
$$\frac{d^2z}{dt^2} + \Omega_z^2\,z = 0, \qquad \Omega_z^2 = \frac{GM}{r^3}$$
**Dürüst tespit:** Bu denklem Newton mekaniğinin birebir aynısıdır; Newton da, GR de, Evrenakı da aynı $\Omega_z$'yi verir. **Dikey salınım periyodu tek başına Evrenakı lehine ayırt edici kanıt olarak kullanılamaz.**
5. **Ayırt edici terim — sönüm.** Ana akım halka fiziğinde sönüm parçacıklar arası inelastik çarpışmadan gelir (Goldreich & Tremaine, 1978): $\gamma_{standart}\sim \Omega_{yör}\,\tau_c^{-1}(1-\epsilon^2)$. Evrenakı'nın sonlu $\eta_E$'si, çarpışmadan **bağımsız**, ortam kaynaklı Stokes-tipi bir sürtünme ekler (Stokes, 1851; tanecik yarıçapı $r_t$ — S-13, kaynakta $a$):
$$\gamma_{Evrenakı} = \gamma_{standart} + \gamma_{ortam}, \qquad \gamma_{ortam} \sim \frac{6\pi\,\eta_E\,r_t}{m}$$
6. **Somut test (M-43 ölçeklemesiyle).** Sönüm mesafesi (S-25: $\lambda_s$):
$$\lambda_s = \frac{v_{grup}}{\gamma_{toplam}}$$
Gözlemsel çapa: Mimas 5:3 dikey rezonansındaki bending-wave sönümü ~**150 km** (Shu ve ark., 1983). $\eta_E^{etkin}\propto a_b\,v_{bağıl}^4/v_{kav}^3$ olduğundan ortam katkısı **boyuttan bağımsız bir taban değildir**: halka taneciklerinin ortama göre bağıl hızı çok küçük olduğu için taban terim $(v_{bağıl}/v_{kav})^3$ sınıfı çarpanlarla güçlü bastırılır. A/B/C halkalarının sönüm mesafelerinin **boyut ve hız dağılımına karşı** sistematik karşılaştırması yine sınav olarak kalır (mevcut Cassini/Voyager verisiyle; yeni görev gerektirmez); nicel ortam katkısının hesabı M-43'ün açık ucudur. *(Düzeltme kaydı, 9 Ağustos 2026: eski "boyuttan bağımsız taban terim" öngörüsü, $\eta_E$'nin evrensel sabit sayıldığı M-43-öncesi çerçevenin ürünüydü.)*

### Sonuç
$$\boxed{\frac{d^2z}{dt^2} + \Omega_z^2\,z = 0\,,\quad \Omega_z^2=\frac{GM}{r^3}\,; \qquad \gamma_{Evrenakı} = \gamma_{standart} + \underbrace{\frac{6\pi\,\eta_E^{etkin}\,r_t}{m}}_{\text{ortam terimi (M-43 ölçeklemesi)}}\,; \qquad \lambda_s = \frac{v_{grup}}{\gamma_{toplam}}}$$

### Geçerlilik Sınırı
- Quasi-statik rejim, $z\ll r$, güneş sistemi (Kepler) ölçeği.
- Salınım kısmı ([T]) Newton ile özdeştir ve ayırt edicilik taşımaz; teorinin test edilebilir iddiası **yalnızca** $\gamma_{ortam}$ terimindedir.
- $\eta_E^{etkin}$ M-43 ile boyut ve hıza bağlandı; serbest kalan tek sayı boyutsuz üs $n$'dir (Ek C.1). Nicel ortam katkısı hesaplanmadan "halka yağmurunu açıklıyor" türü bir iddia yapılamaz (3.10.4.2'nin dürüst tespiti).

### Açık Uçlar
- ~~$\eta_E$'nin sayısal değeri (Ek C satır 14; Gaia/pulsar programı + A/B/C bending-wave karşılaştırması onu sabitleyebilir)~~ → **statü M-43 ile değişti:** $\eta_E$ evrensel sabit değil, türetilmiş $\eta_E^{etkin}$; serbest kalem boyutsuz $n$ (Ek C.1). Halka kanalının M-43 çerçevesinde nicel yeniden yazımı M-43'ün açık ucudur.
- ~~GPB uyuşmazlığı~~ → **çözüldü (Ek M-40):** 6.3'ün öngörüsüyle GP-B ölçümü arasındaki çarpan, kutupsal yörünge geometrik ortalamasının tam $\tfrac12$ olmasıydı; 41,0 ↔ $37{,}2\pm7{,}2$ mas/yıl (0,52σ). Aynı entrainment mekanizması artık bilinen bir sistematik taşımadan halka sönümüne uygulanabilir; kalan engel, $\gamma_{ortam}$'ın M-43 altkritik çerçevesinde nicel yeniden yazımıdır.
- A, B, C halkalarının sönüm mesafelerinin boyut dağılımına karşı sistematik karşılaştırması (arşiv verisi yeniden analizi).
