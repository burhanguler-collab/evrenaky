# Ek M — Merkezî Türetim Kataloğu · Blok E: Doppler ve Kızıla Kayma

> Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.

---

## M-19 · Evrenakı Doppler Türetimi · **[T]**

**Kullanıldığı bölümler:** 6.1.2–6.1.3, 6.2.4, 3.7.3, 7.7.1.

*Notasyon notu:* Gövde metni (6.1) tarihsel Doppler gösterimine sadık kalarak $f_0, f_s, f_{obs}$ yazar; bu katalogda Ek D gereği (R-2, S-15) frekans $\nu$ ile gösterilir: $\nu_0$ (kaynağın öz/durgun frekansı), $\nu_s$ (hareketli kaynağın ateşleme frekansı), $\nu_{obs}$ (alıcının ölçtüğü frekans). Buradaki frekans, **tek bir katarın içindeki** ardışık Zerre ritmidir (şiddet/katar sayısı değildir; bkz. D-21 tanımı, 2.2.3).

### Varsayımlar
1. Işık, $\nu$ frekansıyla (saniyedeki Zerre sayısıyla) ateşlenen bir **Zerre Katarı**dır (mermi dizisi); yerel ortamda çizgisel Zerre hızı $c_0$'dir (M-1).
2. Zaman mutlaktır (Kozmik Zaman); "zaman genleşmesi" diye ayrı bir kabul yoktur. Yavaşlayan şey, kompozit maddenin **mekanik saatidir** (ateşleme dişlisi).
3. Ateşleme dişlisi (atomik geçişler), akışkana kavrama mekanizmasıyla çalışır ve $c_0$ hızına tabidir: atom içinde bir referans noktasından diğerine $c_0$ ile gidip dönen iç sinyal, mekanik bir **Zerre-Saati** (ışık saati) oluşturur.
4. Temel biçimde alıcı, yerel Sürüklenme Zarfına (akışkan havuzuna) göre durgundur ($u = 0$); genel biçim Adım 4'te verilir. Hızlar cisimlerin *birbirine göre* değil, **akışkana göre** hızlarıdır.

### Adımlar

**1. Uzaysal kol — Zerre Aralığının açılması.** Durgun kaynak $\nu_s$ frekansıyla ateşlesin; ardışık iki ateşleme arası süre $T_s = 1/\nu_s$. Durgun durumda iki Zerre arasındaki mekanik mesafe (Zerre Aralığı):
$$ \lambda_0 = c_0\,T_s = \frac{c_0}{\nu_s} $$
Kaynak alıcıdan $v$ hızıyla **uzaklaşıyorsa**, ikinci Zerre $T_s$ süre sonra $v\,T_s$ kadar geriden ateşlenir; aralık basit Newtonyen toplamayla açılır:
$$ \lambda = c_0\,T_s + v\,T_s = \frac{c_0 + v}{\nu_s} $$
(Yaklaşan kaynak için $\lambda = (c_0 - v)/\nu_s$.)

**2. Zamansal kol — mekanik saatin yavaşlaması.** Atom akışkan içinde $v$ hızıyla ilerlerken, $c_0$-limitli iç sinyal düz yol yerine **çapraz (üçgen) yol** izlemek zorundadır. Durgun gidiş-dönüş süresi $T_0$, hareketli süre $T$ ise Pisagor'dan:
$$ (c_0\,T)^2 = (v\,T)^2 + (c_0\,T_0)^2 \;\Longrightarrow\; T = \frac{T_0}{\sqrt{1 - v^2/c_0^2}} $$

*Saat yönelimi bağımsızlığı (boy kısalması):* Çapraz kol $\gamma$ verirken, hareket yönüne **paralel** gidip dönen sinyalin yol uzaması $\gamma^2$ çıkar — izotropi bozulur gibi görünür. Teori burada boy kısalmasını varsaymaz, **mecburiyet olarak türetir**: yüksek hızla ilerleyen kompozit vorteks, önden yediği deplasman/dinamik basıncı nedeniyle hareket yönünde mekanik olarak ezilir; hidrodinamik ezilme oranı $1/\gamma$'dır. Paralel yol tam gereken oranda kısalır ve yavaşlama her yönelimde $\gamma$ olur (izotropi onarılır). Boy kısalması uzayın bükülmesi değil, akışkan basıncının cismi sıkıştırmasıdır.

Periyot $\gamma$ katına çıktığından hareketli kaynağın ateşleme frekansı düşer:
$$ \nu_s = \nu_0 \sqrt{1 - \frac{v^2}{c_0^2}} $$

**3. Sentez.** Adım 2'yi Adım 1'e yerleştirip alıcının ölçümünü ($\nu_{obs} = c_0/\lambda$) yazalım:
$$ \nu_{obs} = \frac{c_0}{\lambda} = \frac{c_0\,\nu_0\sqrt{1 - v^2/c_0^2}}{c_0 + v} = \nu_0\,\frac{\sqrt{1-\beta^2}}{1+\beta}, \qquad \beta = \frac{v}{c_0} $$
$\sqrt{1-\beta^2} = \sqrt{(1-\beta)(1+\beta)}$ açılımı ve $\sqrt{1+\beta}$ sadeleşmesiyle rölativistik Doppler biçimi elde edilir (aşağıda, Sonuç).

**4. Genel iki-hızlı biçim.** Alıcı da yerel ortama göre $u$ hızıyla hareket ediyorsa, alıcının kendi saati $\gamma_u$ oranında yavaşlar ve birim öz-zamanda yakaladığı Zerre sayısı değişir:
$$ \nu_{obs} = \nu_0 \left( \frac{1 \pm u/c_0}{1 \pm v/c_0} \right) \frac{\sqrt{1 - v^2/c_0^2}}{\sqrt{1 - u^2/c_0^2}} $$
Saat yavaşlaması ve boy kısalması kusursuz işlediği için $u$ ve $v$ mutlak hızları gözlemden matematiksel olarak silinir; ifade Özel Görelilik'in bağıl-hız ($v_{rel}$) formülüne eşdeğerdir (Lorentz'in gözlemlenemezlik teoremi, 1904). Evrenakı, SR'yi kinematik düzeyde tam kapsar.

### Sonuç
$$\boxed{\nu_{obs} = \nu_0 \sqrt{\frac{1 - \beta}{1 + \beta}}\,, \qquad \beta = \frac{v}{c_0} \quad (\text{uzaklaşan kaynak; yaklaşan için } \beta \to -\beta)}$$

Ives–Stilwell (1938) verisiyle doğrulanan rölativistik Doppler denklemi, uzay-zaman bükülmesi kabul edilmeden, yalnızca Newtonyen aralık açılması + mekanik saat yavaşlaması ile üretilmiştir.

### Geçerlilik Sınırı
- Türetim, mutlak Kozmik Zaman + mekanik saat (Zerre-Saati) yorumuyla kurulur; **gözlemsel sonuç SR ile özdeş, ontoloji farklıdır** (bükülen zaman yok, yavaşlayan dişli var).
- Kaynak ve alıcı **aynı yoğunluktadır** ($c_0$ ortak). Yoğunluklar farklıysa M-20'nin birleşik formülü geçerlidir.
- Kinematik katmanda SR'den sapma öngörülmez; ayrışma dinamik katmandadır (değişken $c_0$; M-20).

### Açık Uçlar
- ~~Boy kısalmasının ($1/\gamma$ ezilme oranının) hidrodinamik mekanizmadan bağımsız nicel türetimi~~ → **kapandı (17 Ağustos 2026):** türetim **11.4.8.1**'de yapılmıştır — ortama göre $V$ ile giden deplasman kaynağının kararlı alanı, Prandtl–Glauert dönüşümü gereği hareket yönünde tam $\beta=\sqrt{1-V^2/c_0^2}$ oranında kısalmak zorundadır (kapalı biçim; $\Lambda_{kin}$, KARNE satır 21, **[T]**). 6.1.2'nin izotropi argümanı böylece varsayım olmaktan çıkıp türetimin sağlaması konumuna iner. *(Ayrı kalem uyarısı: M-42'nin "$\gamma_\ell$ mekanizması" açık ucu — potansiyel kolunun cetvel ölçeği — bununla kapanmaz, açık kalır.)*

---

## M-20 · Kütleçekimsel Kızıla Kayma Sentezi · **[T]**

**Kullanıldığı bölümler:** 6.2.2–6.2.8, 3.7.3, 7.7.1, Ek B.3/M-8 (yön kuralı, 2.4.2), Ek C satır P1.

*Terminoloji notu:* "Kütleçekimsel kızıla kayma" (gravitational redshift) yerleşik **gözlem adı** olarak korunur; mekanizma teoride kütleçekim değil, **kütle-itim gradyanının** ördüğü basınç kuyusu / yoğunluk profilidir ($c_{loc} = \sqrt{P/\rho}$ üzerinden).

### Varsayımlar
1. $c_{loc} = \sqrt{P/\rho}$ yereldir ve değişkendir (M-1, Postülat 4): kütle çevresindeki basınç kuyusunda (**düşük Evrenakı-basıncı bölgesinde** — Yön Kuralı gereği kuyuda basınç düşer, yoğunluk korunur ya da daha yavaş düşer) yayılma hızı $c_{loc}$ düşüktür (2.4.2 / Ek B.3, M-8: $\delta c/c_0 = \frac{1-k}{2}\,\delta P/P_0 < 0$).
2. **Akı korunumu:** Zerre Katarı'nın mermileri yolda buharlaşamaz; statik alanda sabit bir kesitten birim kozmik zamanda geçen Zerre sayısı korunur.
3. Yerel saat M-21 bağıntısına uyar: $\nu_{tik} \propto \Lambda/\gamma$.
4. **Ölçek ayrımı (M-42):** "Yerel ışık hızı" tek büyüklük değildir. **Madde ölçeği** $\Lambda \equiv e^{-\Phi/c_0^2}$ (tam biçim, **Ek M-55**; birinci mertebede $1-\Phi/c_0^2$) cetvelleri, saatleri ve atomik geçiş frekanslarını yönetir; **yayılma hızı** ise $c_{loc} = c_0\Lambda^2$'dir. Bu girdinin *üretim* ve *ölçüm* adımları $\Lambda$ ile, *yayılım* (Zerre Aralığı) adımı $c_{loc}$ ile yazılır. *(Köken notu: M-42'nin üsleri ışık bükülmesi ve yerel Lorentz-değişmezliği gözlemlerinden sabitlenmiştir; kızıla kayma bu zincirde girdi değil, **öngörüdür** — muhasebe M-42'de, kalibrasyon notu M-8 Açık Uçlar'da.)*

### Kritik Ayrım: İki Ayrı "Frekans"
Görünürdeki çelişkinin tamamı tek kelimenin iki büyüklüğü adlandırmasındandır; teori ikisini titizlikle ayırır:
1. **Akı Frekansı (koordinat frekansı):** sabit kesitten birim kozmik zamanda geçen Zerre sayısı — statik alanda **korunur**.
2. **Gözlem Frekansı (öz-saat frekansı):** gözlemcinin kendi yerel saat tikleri başına saydığı Zerre sayısı — gözlemcinin hızına ve yerel yoğunluğuna bağlıdır, kaynak ile alıcının durumu farklıysa **korunmaz**.

Akı frekansı yol boyunca korunur, ama gözlem frekansı kaymıştır — çünkü o akı, **kaynakta zaten kaymış doğmuştur.**

### Adımlar
Hareket olmasın ($u = v = 0$, $\gamma = 1$); kaynak basınç kuyusunun dibinde (derin kuyu — düşük basınç, küçük $\Lambda_{kaynak}$), alıcı serbest uzayda (arka plan basıncı, büyük $\Lambda_{alıcı}$) olsun.

**1. Üretim.** Kaynağın Zerre-Saati, $\Lambda_{kaynak}$ küçük olduğu için yavaş tikler ve akıyı düşük doğurur:
$$ \nu_{emit} = \nu_0 \cdot \frac{\Lambda_{kaynak}}{\Lambda_{ref}} $$
($\Lambda_{ref}$: öz frekans $\nu_0$'ı tanımlayan standart yoğunluk referansının madde ölçeği.) **Kayma bu ilk adımda doğar.**

**2. Yayılım.** Akı korunur ($\nu_{emit}$ sabit); değişken yayılma hızı nedeniyle Zerre Aralığı konumla esner:
$$ \lambda(r) = \frac{c_{loc}(r)}{\nu_{emit}}\,, \qquad c_{loc} = c_0\,\Lambda^2 $$
Öndeki Zerre kuyu sınırını aşıp hızlanırken arkadaki hâlâ yavaştır; aralık lastik gibi uzar. Bu esneme **yeni kayma üretmez**; kaynakta doğmuş düşük akının uzaydaki geometrik görünümüdür. (Çift sayım yoktur: saat yavaşlaması ile aralık esnemesi tek olayın üretim ve yayılım yüzleridir; 6.2.7.)

**3. Ölçüm.** Alıcı, gelen ışığı kendi ortamındaki referansla ($\nu_0 \cdot \Lambda_{alıcı}/\Lambda_{ref}$) karşılaştırır; $\Lambda_{ref}$ sadeleşir:
$$ \frac{\nu_{obs}}{\nu_0} = \frac{\Lambda_{kaynak}}{\Lambda_{alıcı}} $$

Birinci mertebede $\Lambda = 1-\Phi/c_0^2$ olduğundan *(tam biçim: $\Lambda=e^{-\Phi/c_0^2}$, **Ek M-55**)* bu oran ölçülen genliği doğrudan verir: $\delta\nu/\nu = -\Phi/c_0^2$ (Pound–Rebka 1960; GPS: Ashby 2003).

**İşaret kontrolü:** kuyu dibinde $\Lambda_{kaynak} < \Lambda_{alıcı}$ ⟹ $\nu_{obs} < \nu_0$: **kızıla kayma.** Spektrometreler frekansı değil doğrudan Zerre Aralığını ($\lambda$) ve vuruş momentumunu ölçtüğünden, arası açılmış katarı "kırmızı ışık" olarak kaydeder.

**4. Birleşik formül.** Hareket ve yoğunluk farkı birlikte varsa, ikisi de tek Zerre-Saati oranından ($\nu_{tik} \propto \Lambda/\gamma$, M-21) türediği için tek ifadede toplanır (Sonuç kutusu). $u$: alıcının, $v$: kaynağın **yerel ortama göre** hızıdır. İki çarpanda iki farklı büyüklük geçer: uzaysal çarpanda yayılma hızı $c_{loc}$, saat çarpanında madde ölçeği $\Lambda$ (M-42).

### Sonuç
$$\boxed{\nu_{obs} = \nu_0 \;\underbrace{\frac{1 \pm u/c_{loc,alıcı}}{1 \pm v/c_{loc,kaynak}}}_{\text{uzaysal (Zerre Aralığı)}}\; \underbrace{\frac{\Lambda_{kaynak}}{\Lambda_{alıcı}} \cdot \frac{\gamma_{alıcı}}{\gamma_{kaynak}}}_{\text{Zerre-Saati oranı}}}$$

**İki limit kontrolü:**
- $\Lambda_{kaynak} = \Lambda_{alıcı}$ (aynı yoğunluk; dolayısıyla $c_{loc}$ de ortak): ifade rölativistik Doppler'e (M-19) iner. ✓
- $u = v = 0$ (hareketsiz): ifade saf kütleçekimsel-kayma oranına $\nu_{obs}/\nu_0 = \Lambda_{kaynak}/\Lambda_{alıcı} = 1 - \Delta\Phi/c_0^2$ iner. ✓

Standart fiziğin iki ayrı kuramla (SR kinematiği + GR metriği) modellediği kayma, tek yerel-saat bağıntısının iki yüzüdür.

### Geçerlilik Sınırı
- Akı korunumu **statik alan** içindir; alan zamana bağlıysa kesit akısı da zamana bağlı olur.
- Sonuç bir **orandır**; $\Lambda_{ref}$ seçimi fiziği etkilemez (sadeleşir).
- **Saat/yayılım ayrımı zorunludur (M-42):** üretim ve ölçüm adımlarında $\Lambda$ yerine yayılma hızı $c_{loc} = c_0\Lambda^2$ kullanılırsa kızıla kayma genliği **iki kat** büyük çıkar ($-2\Phi/c_0^2$) ve Pound–Rebka/GPS ile çelişir.
- Test edilmiş lokal rejimlerde (Pound–Rebka 1960; GPS: Ashby 2003; Galileo: Delva ve ark. 2018) teori standart ölçümlerle örtüşmek zorundadır: buralarda Evrenakı yoğunluk profili ile GR metrik potansiyeli aynı sonucu verir. Ayrışma, iki profilin koptuğu ölçekte (galaktik) aranır.

### Açık Uçlar
- **Galaktik ppm sapması:** karanlık-madde destekli metrik ile vorteks kaynaklı $\rho(r)$ profili galaktik yoğunluğu farklı öngörür → farklı $\Lambda(r)$ → uzak galaktik sınırlarda ve galaksiler arası seyrek bölgelerde ppm düzeyinde kızıla kayma sapması. Dönüş eğrisi + kızıla kayma **ortak fiti** profili ve sapmayı birlikte sabitler (Ek C satır P1; 6.2.8, 7.4).

---

## M-21 · Zerre-Saati Bağıntısı · **[T]**

**Kullanıldığı bölümler:** 6.2.3 (tanım evi), 6.1.2 Adım 2, 6.2.4–6.2.6, 3.7.3, 7.7.1. Bağlı katalog: M-42 (ölçek yapısı).

### Varsayımlar
1. Madde kompozittir; bir atomun ışıma frekansını belirleyen atomik geçişler, akışkana kavrama mekanizmasıyla, yerel **yayılma hızına** ($c_{loc}$) tabi iç sinyallerle çalışır (M-1).
2. Bu iç sinyaller, atom içinde bir referans noktasından diğerine $c_{loc}$ ile gidip gelen mekanik bir **Zerre-Saati** oluşturur; gidilen iç yolun uzunluğu $\ell_{loc}$'dur.
3. **Ölçek ayrımı (M-42):** $\Lambda \equiv e^{-\Phi/c_0^2}$ (tam biçim, **Ek M-55**; birinci mertebede $1-\Phi/c_0^2$) **madde ölçeğidir** — cetvelleri ($\ell_{loc}\propto\Lambda$), saatleri ve atomik geçiş frekanslarını yönetir. Zerre'nin **yayılma hızı** ise ayrı bir büyüklüktür: $c_{loc} = c_0\Lambda^2$. "Yerel ışık hızı" ifadesi bu ikisini karıştırmamak için bu girdide kullanılmaz. *(Üslerin gözlemsel kökeni için köken notu: M-20 Varsayım 4.)*

### Adımlar
1. Saatin tik frekansı, iç sinyalin **hızının iç yol uzunluğuna oranıdır**. Basınç kuyusunda ikisi birlikte ölçeklenir ($c_{loc}\propto\Lambda^2$, $\ell_{loc}\propto\Lambda$), dolayısıyla tik hızı madde ölçeğine iner:
$$ \nu_{tik} \propto \frac{c_{loc}}{\ell_{loc}} \propto \frac{\Lambda^2}{\Lambda} = \Lambda $$
Kuyu derinleşip $\Lambda$ düşerse aynı iç çevrim daha uzun sürer → tik yavaşlar.
2. Atom yerel ortama göre $v$ hızıyla hareket ediyorsa, iç sinyal **çapraz yol** izler; yol uzaması $\gamma$ çarpanıdır (Pisagor türetimi: M-19 Adım 2).
3. İki bağımsız fiziksel etken tek ifadede çarpılır:

### Sonuç
$$\boxed{\nu_{tik} \propto \frac{\Lambda}{\gamma}\,, \qquad \Lambda \equiv e^{-\Phi/c_0^2}\,, \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c_0^2}}}$$

*(Kutudaki $\Lambda$ tam biçimdir — **Ek M-55**; birinci mertebede $\Lambda = 1-\Phi/c_0^2$.)*

Bu tek bağıntı, iki kayma türünü **aynı mekanik kökten** doğurur:
- **Yoğunluk değişince** $\Lambda$ değişir → kütleçekimsel (yerleşik gözlem adıyla) kayma; mekanizma kütle-itim gradyanının yoğunluk profilidir. Birinci mertebede $\delta\nu/\nu = -\Phi/c_0^2$.
- **Atom hareket edince** $\gamma$ devreye girer → kinematik kaymanın zaman-genleşmesi bileşeni.

**Çift bileşenli doğrulama — GPS:** yörüngedeki saat hem yüzeye göre hareketlidir (kinematik bileşen: günde ≈ −7 µs) hem de daha sığ bir basınç kuyusundadır — büyük $\Lambda$ (kütle-itim bileşeni: günde ≈ +45 µs). Net ≈ **+38 µs/gün** düzeltme, iki bileşenin aynı saat bağıntısında toplandığının günlük mühendislik doğrulamasıdır (Ashby, 2003).

### Geçerlilik Sınırı
- Bağıntı bir **orantıdır**: mutlak tik hızı saatin iç yapısına (iç yol uzunluğuna, geçiş tipine) bağlıdır; evrensel olan, iki durumun **tik oranıdır**. M-20'nin tüm sonuçları yalnız oranları kullandığından orantı sabiti sadeleşir.
- $\gamma$ içindeki $v$, cismin **yerel Sürüklenme Zarfına göre** hızıdır (Postülat 7); cisimler arası bağıl hız değildir.
- **Bağıntıda $\Lambda$ durur, $c_{loc}$ durmaz.** Bu ayrım olmadan — yani tik hızı yayılma hızıyla ($c_{loc} = c_0\Lambda^2$) orantılı sayılırsa — kızıla kayma genliği **iki kat** büyük çıkar ($-2\Phi/c_0^2$ yerine doğrusu $-\Phi/c_0^2$) ve Pound–Rebka (1960) ile GPS (Ashby, 2003) verisiyle çelişir. Bükülme ve Shapiro gecikmesi ise tersine $c_{loc}$ ile yazılmak zorundadır; $\Lambda$ ile yazılırsa bükülme yarıya iner (M-42).

### Açık Uçlar
- Yok; bağıntı, M-19 (Pisagor kolu) ile M-1 + M-42 (madde ölçeği $\Lambda$ kolu) türetimlerinin birleşik ifadesidir. Orantı sabitinin belirli bir atomik geçiş için hesabı, saat-yapısı modellemesi olarak 7.4 programına girer.
