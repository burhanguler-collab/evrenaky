# Ek B — Çok Bileşenli Basınç Alanı, Arka Plan Basıncının Sabitlenmesi ve Ortamın Ağırlıksızlığı

> **Taşıma notu:** Bu ek, Kısım 1 Bölüm 1.3.4'ten bu kısma taşınmıştır; Kısım 1'de kompakt özeti bulunur. Şablonlu türetim karşılıkları (Ek M kataloğu): Ek B.2 → **M-7** · Ek B.3 → **M-8** · Ek B.4 → **M-9**.

### Ek B: Çok Bileşenli Basınç Alanı, Arka Plan Basıncının Sabitlenmesi ve Ortamın Ağırlıksızlığı

#### Ek B.1 — Çok Bileşenli Basınç Alanı ve Galileo İvmesi

Yeryüzünde ölçülen $g \approx 9.8\text{ m/s}^2$ ivmesi tek bir statik kuvvetin değil; Dünya'nın toplam nükleon hacminin yarattığı radyal deplasman ($\nabla P_r$) ile kendi eksenindeki dönüşünden doğan yanal/azimut girdap bileşenlerinin ($\nabla P_{spin}$) süperpozisyonudur:

$$\nabla P_{toplam} = \nabla P_r + \nabla P_{spin}$$

Bu spin-girdap bileşeni, Gravity Probe B jiroskobunda ölçülen $37{,}2\pm7{,}2$ mas/yıl çerçeve sürüklenmesinin (Everitt ve ark., 2011) temel mekanik kaynağıdır; teorinin türetilmiş öngörüsü 41,0 mas/yıl'dır (0,52σ ✓ — Ek M-40) (bkz. Kısım 3 ve Kısım 5).

#### Ek B.2 — Yırtılmama Koşulu: Muhafazakâr Alt Sınır

*(Katalog: **M-7**.)*

Yüzeydeki toplam gradyanı $\nabla P \approx 2.6 \times 10^{18}\text{ Pa/m}$ olan bu basınç alanında, Dünya'nın iç kısımlarında iç nükleon kütlesi yarıçapla azaldığından gradyan merkeze doğru lineer olarak sıfıra iner: $\nabla P(r) = \frac{\alpha M r}{R^3}$. Bu değişken gradyanın merkezden yüzeye entegrasyonu, merkezdeki net basınç düşüşünün düz hesaba kıyasla yarıya indiğini gösterir: $\Delta P = \frac{1}{2} \nabla P_{yüzey} \cdot R_{Dünya} \approx 0.83 \times 10^{25}\text{ Pa}$. Akışkanın yırtılmaması için **en muhafazakâr koşul** — kohezyon dayanımı sıfır sayılırsa ($\Sigma=0$; bkz. Ek A.3) — $P_0 > \Delta P \approx 0{,}83\times10^{25}$ Pa'dır; homojen-küre idealleştirmesini ve iç yoğunluk profili belirsizliklerini kabaca karşılamak için buna **~2 kat emniyet payı** uygulanır (M-7, adım 5) ve taban $P_0 \ge 1.6 \times 10^{25}\text{ Pa}$, $\rho_0 = P_0/c_0^2 \ge 1.8 \times 10^8\text{ kg/m}^3$ **alt sınırı** olarak ilan edilir. Kohezyon hesaba katıldığında koşul $P_0+\Sigma>\Delta P$ biçimini alır; yani bu bir kesin değer değil, güvenli tarafta kalan bir tabandır. Ortamın gerçek basıncı, aşağıdaki bağımsız sabitlemeyle bu tabanın **sekiz–dokuz mertebe üzerinde** çıkar — dolayısıyla yırtılmama koşulu her durumda devasa bir marjla sağlanır.

#### Ek B.3 — Arka Plan Basıncının Gözlemsel Sabitlenmesi: $P_0 \approx \tfrac{1}{4}\rho_n c_0^2$

*(Katalog: **M-8**.)*

Alt sınır yerine gerçek değeri, teorinin kendi mekanizmasından sabitlemek mümkündür. Kütleye yaklaşıldıkça ortamın durumu değişir; bu değişimde yoğunluğun basınca eşlik oranını $\delta\rho/\rho_0=k\,\delta P/P_0$ ile parametrize edelim. **Bu, maddenin doğurduğu *deplasman* sürecidir** ve ortamın adiyabatik dalga tepkisiyle karıştırılmamalıdır (ikisi ayrı kısmi türevlerdir — Ek M-44). Deplasman süreci için $k=0$'dır: **basınç düşer, ortalama yoğunluk korunur.** Bu değer serbest değildir; Ek M-15'in G1 (Korunum) aksiyomu ($\bar\rho_m=\rho_0$) ile Ek M-30'un Varsayım 1'i ("gradyanlarda asıl değişen basınçtır") bağımsız olarak aynı sonucu verir; M-44'ün iki değişkenli hâl denklemi bunu kutulu sonuca çevirir. Kavrama Yasası'ndan, yerel ışık hızındaki — ve Postülat 3 gereği yerel saat hızındaki — oransal kayma:

$$\frac{\delta c}{c}=\frac{1}{2}\left(\frac{\delta P}{P_0}-\frac{\delta\rho}{\rho_0}\right)=\frac{1-k}{2}\cdot\frac{\Delta P_{yüzey}}{P_0}$$

Bu kaymanın genliğini veren gözlem, ölçek yapısının (Ek M-42) belirlediği çarpanla okunur. Madde ölçeği $\Lambda=1-\Phi/c_0^2$ ile saat $f\propto\Lambda$, yayılma hızı $c_0\propto\Lambda^2$ ölçeklendiğinden **saat kayması ile yayılma hızı kayması eşit değildir:** $\delta c/c_0 = 2\,\delta f/f$, yani $\delta c/c_0 = -2\Phi/c_0^2$ ($\Phi/c_0^2\approx7\times10^{-10}$; $\Phi$: yüzey kütleçekim potansiyeli). Bu 2 çarpanı ışık bükülmesi ölçümünden ($1{,}751''$) sabitlenmiştir; $\delta c/c_0=\delta f/f$ okuması bükülmeyi gözlenenin yarısı verir ve dışlanmıştır (M-42). Yüzeydeki basınç açığı ise Ek B.2'deki gradyanın integralinden $\Delta P_{yüzey}=\rho_n\Phi$'dir. İkisi eşitlenince $\Phi$ sadeleşir ve arka plan basıncı, kütleden bağımsız **evrensel** bir değere sabitlenir:

$$\frac{1-k}{2}\cdot\frac{\rho_n\Phi}{P_0}=\frac{2\Phi}{c^2}\;\Longrightarrow\;\boxed{P_0=\frac{1-k}{4}\,\rho_n c_0^2\;\xrightarrow{\;k=0\;}\;6{,}07\times10^{33}\ \text{Pa},\qquad \rho_0=\frac{P_0}{c^2}=\frac{\rho_n}{4}\approx6{,}8\times10^{16}\ \text{kg/m}^3}$$

Bu sabitlemenin üç sonucu vardır:

1. **Monizm nicelleşir.** Arka plan yoğunluğu, nükleon öz yoğunluğunun ($\rho_n\approx2.7\times10^{17}\text{ kg/m}^3$) dörtte biri mertebesindedir ($k=0$ için $\rho_0\approx6.8\times10^{16}\text{ kg/m}^3$): madde, okyanustan kopuk bir "yabancı cisim" değil, okyanusun yalnızca ~4 kat sıkışmış girdap fazıdır. Bölüm 1.3.1'deki "madde, uzay okyanusunun yoğunlaşmış hâlidir" cümlesi böylece nicel bir orana kavuşur (Postülat 4'teki Zerre öz yoğunluğuyla da tutarlı).
2. **Zayıf-alan kontrolü.** Dünya'nın toplam basınç çukuru ($\Delta P\approx0.83\times10^{25}$ Pa), $P_0$'ın yanında $\sim10^{-9}$'luk bir pürüzdür. Kütle-itim etkilerinin gözlenen küçüklüğü (saat kaymalarının $10^{-9}$–$10^{-10}$ mertebesi) doğrudan bu orandır: gezegenler, okyanusun milyarda-birlik dalgacıklarıdır.
3. **Yırtılma marjı.** $\Delta P/P_0\sim10^{-9}$ olduğundan, Ek B.2'nin yırtılmama koşulu kohezyondan bağımsız olarak devasa marjla sağlanır.

*Dürüst kayıt:* (i) $k=0$, iki bağımsız aksiyomdan gelir ve M-44'ün kutulu sonucudur — serbest parametre değildir (Ek C.1-ii); SN 1987A bütçesiyle çapraz kontrolü açık iştir (Bölüm 7.4). (ii) $\mathcal{G}$'nin türetimi (Bölüm 4.2; yerleşik adıyla "kütleçekim sabiti") yalnızca gradyan bağlaşımına ($\alpha$) dayandığından $P_0$'ın mutlak değerinden bağımsızdır — sabitleme onu etkilemez; SN 1987A gecikme bütçesinin (Bölüm 2.4.4) bu değerlerle çapraz kontrolü ise açık iştir (Bölüm 7.4). (iii) **Kalibrasyon kaynağı:** bu sabitlemenin gözlemsel dayanağı artık kütleçekimsel kızıla kayma değil, **ışık bükülmesidir** (2 çarpanını veren gözlem odur; Ek M-42). Kızıla kayma zincirde serbest kalır ve öngörüye döner ($\delta f/f=-\Phi/c_0^2$); GPS ve Pound–Rebka böylece girdi değil bağımsız doğrulama olur.

#### Ek B.4 — Ortamın Ağırlıksızlığı: Tanım Değil Teorem

*(Katalog: **M-9**.)*

Postülat 1'deki "ağırlıksız ortam" ifadesi bu ekte kanıt statüsü kazanır. Newtoncu sezgiden gelen itiraz — *"$10^{17}\text{ kg/m}^3$'lük bir ortam neden çökmez, neden tartılmaz?"* — gizli bir varsayım taşır: kütle yoğunluğunun kendiliğinden çekim alanı kaynakladığı ($\nabla^2\Phi=4\pi G\rho_{toplam}$). Evrenakı'da böyle bir yasa yoktur ve olamaz: teoride çekim diye bağımsız bir kuvvet yok; tek alan basınçtır, tek kuvvet gradyandır (Postülat 6). Buradan üç adımlık teorem:

1. **Ağırlıksızlık.** Ağırlık, kütlenin değil gradyanın — yani deplasmanın — özelliğidir. Homojen arka plan hiçbir şeyi yerinden itmez; o, basınç alanının sıfır noktasıdır (datum) ve $\nabla P_0=0$ olduğundan hiçbir kuvvet hissetmez. Arşimet'in kaldırma kuvveti nasıl mutlak yoğunluğun değil yoğunluk *farkının* olayıysa, Evrenakı ağırlığı da mutlak $\rho_0$'ın değil deplasman *açığının* olayıdır.
2. **Kararlılık.** Klasik öz-kütleçekimli akışkanda homojen durum kararsızdır (Jeans kararsızlığı; Jeans, 1902): yoğunlaşan bölge daha çok çeker ve çöküş büyür. Evrenakı'da bu geri-beslemenin iki bacağı da yoktur — yoğunlaşan bölge kimseyi çekmez, yalnızca basıncını yükseltir; ve Kavrama Yasası gereği $c_0^2=dP/d\rho>0$ olduğundan her yoğunluk pürüzü, $c_0$ hızında yayılan basınç dalgası olarak dağılır. Homojen durum yalnızca izinli değil, ortamın **tek doğal taban durumudur.**
3. **Kendiliğinden madde doğumu yok.** Arka planın "kaynayıp" kendiliğinden girdap-madde üretmesi için yerel akışın $v_{kav}=\sqrt{2}\,c_0\sqrt{1+\Sigma/P_0}\gg c_0$ eşiğine (Ek A.3) ulaşması gerekir; $\Sigma\gg P_0$ kohezyonlu bir süper-akışkanda rastgele dalgalanmalar bu eşiğe ulaşamaz. **Arka planın kararlılığı** — uzayın durup dururken maddeye dönüşmemesi — aynı çerçevenin bedava sonucudur. *(Standart çatı aynı soruyu "vakum kararlılığı" diye anar; teoride kararlı olan şey vakum değil, dolu arka plandır.)*

Son bir mekanik incelik: kütle *çevresindeki* gradyan bölgesinde ortamın kendisi de tepkisiz değildir — Euler denklemi gereği gradyana cevap verir; ama cevabı *düşmek* değil **dolaşmaktır**: gradyan, dolaşımın merkezcil ivmesiyle dengelenir ($\nabla P/\rho_0=v_\theta^2/r$; Postülat 7–8'in sürüklenme ve vorteks alanları). Katı deplasman cebi (nükleon) ise akıp dengelenemez; bütün hâlde itilir. **Madde düşer, ortam dolaşır.**

Evrenakı'nın bu devasa yoğunluğuna rağmen nesnelerin ölçülebilir bir direnç duymaksızın hareket edebilmesi, atomların içinin "boşluk" olmamasından; tamamen bu sıfıra yakın (ama sıfır olmayan) viskoziteli süper-akışkanla dolu olmasından kaynaklanır. Madde bu okyanusta yüzen yabancı cisim değil, okyanusun kendi içindeki lokal girdapsal yoğunlaşmadır. Hissettiğimiz kütleitimi, bu devasa hidrostatik okyanus basıncındaki küçük dalgalanmalardan (gradyanlardan) ibarettir.

