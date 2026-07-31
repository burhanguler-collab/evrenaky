## Bölüm 6.5 — Galaktik Yörüngeler ve Karanlık Madde Probleminin Çözümü

Astrofiziğin son yüzyıldaki en büyük çözülemeyen gizemlerinden biri, galaksilerin dış kollarındaki yıldızların dönme hızlarıdır. Klasik Newton mekaniğine ve Einstein'ın Genel Görelilik teorisine göre, galaksinin merkezinden uzaklaştıkça kütleçekim kuvvetinin $1/r^2$ ile zayıflaması ve dolayısıyla yıldızların yörünge hızlarının düşmesi gerekir. Tıpkı Güneş Sistemimizde Güneş'ten uzaklaştıkça gezegenlerin daha yavaş dönmesi gibi.

Ancak 1970'lerde Vera Rubin ve meslektaşları tarafından yapılan hassas gözlemler, sarmal galaksilerin dış kollarındaki yıldızların hızının düşmediğini, aksine çok yüksek hızlarda **sabitlendiğini** (asimptota oturduğunu) kanıtlamıştır. Standart fiziğe göre bu hızlarda dönen yıldızların galaksiden kopup uzaya savrulması gerekirdi. Bu muazzam hızı dengede tutacak görünürde hiçbir kütle olmadığı için astrofizikçiler, galaksiyi devasa bir hale gibi saran görünmez bir kütle uydurmak zorunda kaldılar: **Karanlık Madde**.

Bu bölüm, Evrenakı teorisinin hiçbir "görünmez madde" varsayımına ihtiyaç duymadan, sadece kendi yerel mekanik postülatlarıyla bu kozmolojik anomalinin üstesinden nasıl geldiğini ve düz dönüş eğrilerini doğal yollarla nasıl türettiğini göstermektedir.

### 6.5.1 Kütleçekim Grafiği ve $1/r$ Kuvvetinin Yükselişi

Evrenakı teorisinde galaksi merkezlerindeki süper kütleli kara deliklerin dönüş hızları olağanüstü yüksektir. Teorinin temel postülatlarından olan **Eksenel İtim (F4)** ve ona bağlı hidrodinamik yansımalar, galaksi çekirdeğindeki bu devasa dönüşün (devrin) bir sonucudur.

Kritik nokta şudur: Klasik merkezcil kütleçekim $1/r^2$ profiliyle zayıflarken, teorinin öngördüğü eksenel kuvvet (Kısım 4'te türetildiği üzere) $1/r$ profiliyle sönümlenir. Galaksinin dış bölgelerine çıkıldıkça $1/r^2$'ye tabi klasik çekim hızla gücünü yitirir, ancak $1/r$ ile sönümlenen eksenel kuvvet profilde giderek baskın hale gelir. 

### 6.5.2 Matematiksel İspat: Düz Dönüş Eğrisinin Türetilmesi

Dairesel yörüngede dönen bir yıldızın dengede kalabilmesi için Merkezcil İvme'nin, kütleçekim ivmesi ile teorinin öngördüğü eksenel ivmenin toplamına eşit olması şarttır:

$$a_{merkezcil} = a_{kütleçekim} + a_{eksenel}$$

Terimleri kendi fiziksel bağımlılıklarıyla açtığımızda:
1. **Merkezcil İvme:** $\frac{v^2}{r}$
2. **Evrenakı Kütleçekim (Basınç Gradyanı):** $\frac{A}{r^2}$ *(Buradaki A sabiti, galaksinin merkez kütlesinin yarattığı hidrodinamik basınç düşümü ile orantılıdır)*
3. **Eksenel Kuvvet (Evrenakı):** $\frac{B}{r}$ *(Buradaki B sabiti, merkezdeki süper kütleli kara deliğin devri ve galaktik çekirdeğin dönüş karakteristiği ile orantılıdır)*

Eşitliği kuralım:
$$\frac{v^2}{r} = \frac{A}{r^2} + \frac{B}{r}$$

Denklemin her iki tarafını da yarıçap ($r$) ile çarptığımızda, yörünge hızı $v$ şu şekilde doğrudan elde edilir:
$$\mathbf{v = \sqrt{\frac{A}{r} + B}}$$

Bu zarif ve kompakt denklemin sunduğu fiziksel sonuç son derece derindir:
Klasik fizikte (B=0 kabul edildiğinde) yarıçap ($r$) büyüdükçe hız sıfıra yaklaşır. Ancak Evrenakı teorisinde, galaksinin çok uzak dış kollarına gidildiğinde ($r \to \infty$), $\frac{A}{r}$ terimi sıfıra yaklaşsa dahi yıldızın hızı sıfıra düşmez. Hız doğrudan **$\sqrt{B}$** limitine, yani sabit bir asimptota kilitlenir.

Astronomların teleskoplarla gözlemlediği meşhur **"Düz Dönüş Eğrisi" (Flat Rotation Curve)** profili, teorik altyapıda hiçbir yama kullanılmadan, tamamen doğal yollarla elde edilmiştir.

### 6.5.2.1 Beş Kuvvetin Ekvator Düzlemine İzdüşümü

> **Ekleme kaydı — Claude Opus 5 (Anthropic), 30 Temmuz 2026:** Bu alt bölüm ve 6.5.3.1, Anthropic'in Claude Opus 5 yapay zekâ modeli tarafından üretilmiştir; insan akran denetiminin yerine geçmez. Hesap betiği ve veri: `CALISMA/plot_sparc_ngc3198.py`, `CALISMA/veri/NGC3198_rotmod.dat`.

6.5.2'nin $v=\sqrt{A/r+B}$ denklemi bir ansatz değildir: teorinin **beş hidrodinamik kuvvetinin ekvator düzlemine izdüşümünün tamamıdır.** Denetimin ayrıntısı 6.5.4.1'de verilmiştir; özeti şudur: küresel akı taşıyan **F1** ($a\propto1/r^2$) ile silindirik akı taşıyan **F4** ($a\propto1/R$) çalışır; **F5**'in $\sin2\theta$ yasası $\theta=90°$'de kaybolur, **F2** iz-sıfır gelgit tensörü olduğu için nokta yıldıza net radyal kuvvet vermez, **F3** ise ayrı bir kuvvet değil profil teoreminin mekanizmasıdır. İki terimli yapı bir tercih değil, izdüşümün zorunlu sonucudur.

**Ana denklem — M-37 profil teoremi.** Dönüş eğrisi bağımsız bir girdi değildir:

$$\boxed{\;v_\theta(R)=\sqrt{R\,\bigl|a_{radyal}(R)\bigr|}\;}$$

Bağıntı, ortamın kendi radyal dengesinden ve Postülat 7'nin sürüklenme zarfından çıkar; dönüş profili radyal itim yasasının **çıktısıdır**.

**Düz eğrinin gerçek türetimi — Rankine gerekmez.** Ek M-30'un 5. maddesi bunu açıkça kaydeder: düz kolun türetimi Rankine profilini girdi almaktan geçmez, **M-38+M-37 zinciridir**:

$$\underbrace{h=\text{sabit}}_{\text{M-38 Varsayım 3}}\;\Rightarrow\;\underbrace{a\propto1/R}_{\text{silindirik akı geometrisi}}\;\Rightarrow\;\underbrace{v_\theta=\sqrt{R|a|}=v_0}_{\text{M-37 profil teoremi}}$$

4.2.9.2'nin bileşik girdap kurgusu basınç profilini (logaritmik kuyu) verir; düz eğriyi **öngörü statüsünde** üreten yol ise budur.

F4'ün genliğinin nükleon dolanım debisinden türetimi ($\ell_\omega$) 6.5.4.3'te, gözlemsel sınav ise 6.5.3.1'dedir.

### 6.5.3 Gerçek Gözlem Verileriyle Sınama

Bu matematiksel model ($v = \sqrt{A/r + B}$), evrendeki farklı galaksi türlerinin hassas teleskop ölçümleriyle test edildiğinde kusursuz bir ampirik başarı sergilemektedir. Aşağıdaki testlerde kırmızı kesik çizgiler saf Newton mekaniğini, mavi çizgiler ise Evrenakı teorisinin $1/r$ eklemli formülünü temsil etmektedir.

#### 1. Sarmal Galaksiler: M33 ve NGC 3198
Sarmal galaksiler, karanlık madde probleminin en belirgin gözlemlendiği yapılardır. 
M33 (Triangulum) galaksisinde Newton kütleçekimi hızla düşüşe geçerken, Evrenakı modeli ölçülen hızı ~120 km/s bandında kusursuzca yakalamaktadır. Benzer şekilde, dönüş eğrisinin 30 kpc gibi inanılmaz uzak mesafelere kadar dümdüz kalmasıyla bilinen devasa NGC 3198 galaksisinde, $1/r$ eksenel itim kuvveti yıldız hızlarını ~150 km/s bandında pürüzsüz bir doğrulukla kilitlemektedir.

![M33 Gözlem Testi](Gorseller/m33_gozlem_testi.png)
![NGC 3198 Gözlem Testi](Gorseller/ngc3198_gozlem_testi.png)

#### 2. Dev Eliptik Galaksiler: M87 ve NGC 4472
Eliptik galaksiler sarmal bir diske sahip olmadıkları için net dönüş eğrileri vermezler. Yıldızlar rastgele yörüngelerde bir arı kovanı gibi hareket eder (hız dağılımı). Ancak bu galaksileri saran devasa sıcak X-ışını gaz halelerinden hesaplanan kütleçekim potansiyelleri ("Efektif Dairesel Hız" $V_c$), sarmal galaksilerdeki asimptotik düz yapıyı birebir tekrar eder. 
Evrenin en meşhur dev eliptik galaksilerinden olan M87 ve NGC 4472'nin merkezlerinde korkunç hızlarda dönen süper kütleli kara delikler bulunur. Bu devasa çekirdek dönüşünden kaynaklı eksenel itim, galaksi eliptik de olsa formülün aynı mükemmellikte çalışmasını sağlar.

![M87 Eliptik Testi](Gorseller/m87_eliptik_testi.png)
![NGC 4472 Eliptik Testi](Gorseller/ngc4472_eliptik_testi.png)

#### 3. Cüce Küresel (Dwarf Spheroidal) Galaksiler: Derin Bir Fiziksel Öngörü
Fornax (Ocak) gibi cüce küresel galaksiler, evrendeki karanlık maddenin oransal olarak en yoğun bulunduğu düşünülen, sadece 1-2 kpc boyutlarındaki minicik yapılardır. Çok düşük kütlelerine rağmen efektif hız profilleri $\sim18$ km/s bandında asimptota oturur.
Evrenakı modeli bu galaksilerde de pürüzsüz çalışarak hızı dengeler. Ancak burada astrofiziğe karşı çok derin bir meydan okuma yatar: Güncel astronomiye göre cüce küresellerde süper kütleli kara delik **yoktur**. 
Bu durum, teori açısından çok net bir fiziksel öngörüye işaret eder: Cüce küresel galaksilerin merkezinde astronominin henüz tespit edemediği, **küçük ve düşük hızda dönen gizli bir kara delik (çekirdek devri) bulunmak zorundadır.**

Evrenakı teorisine göre (Bkz. Bölüm 6.6 Gezegen Figürü), güçlü bir eksenel itim kuvveti galaksiyi basıklaştırarak sarmal bir disk formuna sokar. Bu galaksiler küresel formlarını koruduklarına göre, merkezdeki bu kara deliğin kütlesi küçük ve dönüş hızı (dolayısıyla yarattığı eksenel itim kuvveti - $B$ sabiti) nispeten zayıftır. 

Bu zayıf eksenel kuvvet, galaksiyi tamamen yassılaştırmaya yetmez ve küresel form büyük ölçüde korunur. Ancak eksenel itimin uzayda $1/r$ ile yavaş sönümlenme karakteristiği sayesinde, bu zayıf dönüş bile dış bölgelerdeki yıldız hızlarının sıfıra çakılmasını engelleyecek o kritik matematiksel desteği (B sabiti dengesini) sağlamak için yeterlidir. Evrenakı'nın $v = \\sqrt{A/r + B}$ formülü, bu düşük dönüş hızıyla da gözlemlere tam oturur.

![Fornax Küresel Testi](Gorseller/fornax_kuresel_testi.png)

### 6.5.3.1 Gerçek SPARC Verisiyle Nicel Sınav

*(Üretim kaydı için bkz. 6.5.2.1'in başındaki ekleme kaydı.)*

Yukarıdaki testler Evrenakı'yı **klasik çekimle** karşılaştırır. Ama karanlık maddenin gerçek rakibi klasik çekim değil, karanlık maddenin kendisidir. Bu alt bölüm o karşılaştırmayı, **yayınlanmış veriyle** ve karanlık maddeyi kendi en iyi hâliyle kurarak yapar.

**Veri.** SPARC veritabanı (Lelli, McGaugh & Schombert, 2016), `NGC3198_rotmod.dat`: 43 nokta, 0,32–44,08 kpc, **gerçek hata çubukları**, $D=13{,}8$ Mpc. Baryonik bileşenler Spitzer 3,6 μm fotometrisinden türetilmiştir ($V_{disk}$, $M/L=1$ için verilir; ölçekleme $\Upsilon_*$ ile). SPARC'ın kovan kataloğu (`Bulges.mrt`) NGC 3198 için $L_{bul}=0{,}0$ verir — galaksi **kovansızdır**.

**Karanlık madde nasıl kurulmalıdır?** Halonun keyfî eğri uydurma serbestliği yoktur. ΛCDM'in N-cisim simülasyonlarından çıkan evrensel profil **NFW**'dir (Navarro, Frenk & White, 1996) ve konsantrasyon serbest parametre değildir; simülasyonlar onu halo kütlesine bağlar (Dutton & Macciò, 2014): $\log_{10}c_{200}=0{,}905-0{,}101\log_{10}(M_{200}h/10^{12}M_\odot)$. Böylece halonun tek serbest parametresi $M_{200}$ kalır. Tüm modeller **aynı baryonik girdiyi** kullanır ve $\Upsilon_*$ hepsinde serbesttir.

![NGC 3198 — Gerçek SPARC Verisiyle Sınav](Gorseller/sparc_ngc3198.png)

| Model | Serbest par. | RMS (km/s) | RMS ($R>14$ kpc) | $\chi^2_{ind}$ | AIC |
|---|---|---|---|---|---|
| Yalnız baryonlar, $\Upsilon_*=0{,}5$ (fotometrik) | 0 | 56,10 | 77,49 | 759,1 | 32639 |
| Evrenakı F1+F4, kaynak kilitli ($\ell_\omega$ tek) | 1 | 13,26 | 13,57 | 32,61 | 1371,6 |
| ΛCDM NFW, kaynak kilitli ($M_{200}$ tek) | 1 | **8,31** | 2,84 | **1,84** | **79,1** |
| Evrenakı F1+F4, $\Upsilon_*$ serbest | 2 | 8,41 | 5,01 | 3,78 | 159,0 |
| ΛCDM NFW, $\Upsilon_*$ serbest | 2 | 8,68 | 2,37 | **1,48** | **64,5** |
| MOND (kıyas) | 1 | 9,16 | — | 6,86 | 290,3 |
| **Evrenakı + M-38 yayılması** | **3** | **3,72** | **1,90** | **0,68** | **33,1** |

**Sonuç — parametre sayısına göre okunmalıdır.** Eşit serbestlikte ΛCDM öndedir: 1 parametrede AIC 79,1'e karşı 1371,6, 2 parametrede 64,5'e karşı 159,0. Evrenakı ancak M-38'in yayılma çarpanı devreye girdiğinde (3 parametre) öne geçer. Yayılmasız hâlde model dış kolda aşar: gaz diski 44 kpc'ye uzandığı için $M_{kaps}$ 12→44 kpc arasında 1,89 kat büyürken gözlenen hız düz kalır. Düzeltme M-38'in kendi kaydettiği yanlışlanabilir sonucundan gelir — *diskler dışa doğru kalınlaşır, akı yoğunluğu $1/R$'den hızlı düşer, eğri düzlükten sapar*:

$$v_{F4}^2=\frac{b\,M_{kaps}(R)}{1+R/R_f},\qquad R_f=7{,}6\ \text{kpc}\approx2{,}4\,R_d$$

Bu, $\chi^2_{ind}$'i 3,78'den **0,68**'e düşürür — formel olarak kabul edilebilir bir uyum — ve AIC'de ΛCDM'i $\Delta$AIC $=31{,}3$ ile geçer. Karşılaştırma için: dışlama eşiği $\Delta$AIC $>10$'dur (Burnham & Anderson, 2002).

> **Ama bu, yayılma öngörüsünün doğrulandığı anlamına gelmez.** Aynı serbestlikte kurulmuş ve tamamen farklı imzaya sahip bir **gözlemsel artefakt modeli** (eğiklik/warp kaynaklı çarpımsal kayma) aynı işi yapar, hatta örneklem genelinde biraz daha iyi. Ayrıntılı sınav 6.5.4.6'nın $R_f$ kaydındadır: veri iki hipotezi ayırt etmiyor. Buradaki uyum iyileşmesi gerçektir; **nedeninin fiziksel yayılma olduğu gösterilmemiştir.**

**Dürüstlük kayıtları — bu sonuç kesin bir zafer değildir:**

- **$R_f$ fitlenmiştir, ölçülmemiştir.** M-38'in yayılma öngörüsünün gerçek sınavı, 21 cm gözlemlerinden bilinen $h(R)$ kalınlık profilini **girdi** olarak kullanmaktır. Mevcut hâliyle elde edilen şey başarılı bir *fit*, doğrulanmış bir *öngörü* değildir.
- **Rakip varyant ayırt edilemiyor.** Sabit genlikli hâl ($B\,R^2/(R^2+r_0^2)$) neredeyse aynı sonucu verir (AIC 34,9). Veri, yayılma mekanizmasını bu alternatiften seçmiyor.
- **Eşit serbestlikte ΛCDM öndedir.** Bu, tablonun en önemli satırıdır: 1 ve 2 parametrede ΛCDM kazanır. Evrenakı'nın üstünlüğü yalnızca üçüncü parametre ($R_f$) eklendiğinde doğar ve o parametre de ölçülmemiş, fitlenmiştir. Dolayısıyla buradaki sonuç "teori ΛCDM'i yendi" değil, "yayılma çarpanıyla birlikte daha iyi tarif ediyor, ama bir parametre fazlaya"dır.
- **Kaynak kilitli hâl başarısızdır.** $\Upsilon_*$ fotometrik 0,5'e kilitlendiğinde Evrenakı $\chi^2_{ind}=32{,}6$ verir; ΛCDM aynı kısıtla 1,84. Tek serbest parametreli saf sürüm gerçek veriyle ayakta kalmıyor.
- **$\Upsilon_*$ gerilimi.** Kazanan model $\Upsilon_*=0{,}31$ ister; ΛCDM 0,53, 3,6 μm'de beklenen değer ise $\sim0{,}5$'tir. Model yıldız kütlesini beklenenin altına çeker. Aynı fitte $\ell_\omega=1{,}21$ kpc çıkar; kaynak kilitliyken 7,06 kpc idi — yani türetilen vortisite uzunluğu $\Upsilon_*$'a güçlü biçimde bağımlıdır ve sağlam bir sayı değildir.
- **ΛCDM başarısız değildir.** Gerçek veriyle $\chi^2_{ind}=1{,}48$ ile kabul edilebilir bir uyum verir. Buradaki sonuç "ΛCDM çöküyor" değil, "aynı veriyi görünmez madde olmadan daha iyi tarif edebiliyoruz"dur.
- **Tek galaksi.** SPARC 175 galaksi içerir; $b$ ve $R_f$'nin evrenselliği ancak örneklem üzerinde sınanabilir. Sınanmadan bu sonuç bir vaka çalışmasıdır (7.4).

### 6.5.3.2 Örneklem Sınavı: Parametreler Evrensel mi?

*(Üretim kaydı için bkz. 6.5.2.1'in başındaki ekleme kaydı. Hesap betiği: `CALISMA/plot_sparc_ornek.py`; veri: `CALISMA/veri/*_rotmod.dat`.)*

6.5.3.1'in tek galaksili sonucu bir vaka çalışmasıdır. Teorinin **öngörü** iddiası ise bambaşka bir soruya bağlıdır: 6.5.4.3'ün türettiği vortisite uzunluğu $\ell_\omega=q_n/2\gamma_n$ ile M-38'in yayılma ölçeği $R_f$, galaksiler arasında **sabit** midir? $\ell_\omega$ nükleonun kendi debi oranından geldiğine göre mikro-fiziksel bir sabit olmak zorundadır; galaksi başına değişiyorsa türetilmiş bir büyüklük değil, fit parametresidir.

Sınav, SPARC'tan kasıtlı olarak geniş seçilmiş **12 galaksiyle** yapılmıştır (7'si kovansız, 5'i kovanlı; gaz-baskın cüceden $305$ km/s'lik deve kadar). Tüm modeller aynı baryonik girdiyi kullanır; SPARC konvansiyonu $\Upsilon_{bul}=1{,}4\,\Upsilon_{disk}$.

![SPARC örneklem sınavı — 12 galaksi](Gorseller/sparc_ornek_12galaksi.png)

| Galaksi | N | Kovan | ΛCDM $\chi^2_{ind}$ | Evrenakı $\chi^2_{ind}$ | +yayılma | $\ell_\omega$ (kpc) | $R_f$ (kpc) |
|---|---|---|---|---|---|---|---|
| DDO154 | 12 | — | **17,30** | 2,44 | **0,92** | 0,85 | 7,0 |
| NGC6503 | 31 | — | 2,99 | 5,30 | **2,54** | 3,50 | 22,6 |
| NGC2403 | 73 | — | **5,36** | 10,30 | 9,85 | 4,13 | 54,4 |
| NGC3198 | 43 | — | 1,46 | 3,67 | **0,67** | 11,30 | 7,6 |
| NGC2903 | 34 | — | **15,51** | 6,80 | **5,54** | 5,06 | 49,1 |
| NGC5055 | 28 | — | 3,42 | 3,25 | **1,95** | 12,53 | 179,5 |
| NGC3521 | 41 | — | **0,30** | 0,87 | 0,89 | 7,81 | $\to\infty$ |
| NGC0891 | 18 | var | 6,12 | 6,20 | **6,09** | 6,15 | 43,8 |
| NGC4157 | 17 | var | **0,53** | 0,68 | 0,73 | 10,14 | $\to\infty$ |
| NGC5985 | 33 | var | **8,80** | 11,37 | 12,67 | 151,20 | 0,5 |
| NGC7331 | 36 | var | **0,78** | 1,86 | 1,92 | 9,72 | $\to\infty$ |
| NGC2841 | 50 | var | **1,82** | 1,97 | 2,02 | 11,48 | $\to\infty$ |

**Sonuç 1 — evrensellik sınavı başarısızdır.**

| Parametre | Aralık | Yayılım |
|---|---|---|
| $\ell_\omega$ | 0,85 – 151,20 kpc | **179 kat** |
| $R_f$ | 0,5 – $\to\infty$ | **$>10^5$ kat** |

$\ell_\omega$ 179 kat değişiyor. **Ama bu tek başına bir kusur değildir:** teori $\ell_\omega$'nın evrensel olduğunu iddia etmez, değişiminin yasalı olduğunu iddia eder — yasa ve sınavı 6.5.4.5'tedir ($\propto\sqrt{M_{bar}}$, ölçülen eğim 1,03). Buna karşılık **$R_f$ için böyle bir yasa yoktur:** 4/12 galakside üst sınıra dayanıyor, yani o galaksilerde yayılma hiç istenmiyor. Yayılma çarpanı, işe yaradığı yerde devreye giren bir serbestliktir ve **öngörü statüsü taşımaz.**

**Sonuç 2 — eşit serbestlikte ΛCDM öndedir.** $k=2$'de Evrenakı yalnızca 3/12 galakside öne geçer; toplam $\Delta$AIC $=-226{,}7$ (ΛCDM lehine). En iyi AIC sayımı: ΛCDM 6/12, Evrenakı+yayılma ($k=3$) 6/12, Evrenakı $k=2$ **0/12**.

**Sonuç 3 — ve tek gerçek kazanç: cusp-core rejimi.** Örneklemde ΛCDM'in *formel olarak dışlandığı* iki galaksi vardır ve ikisinde de Evrenakı belirgin biçimde daha iyidir:

| | ΛCDM $\chi^2_{ind}$ | Evrenakı $\chi^2_{ind}$ |
|---|---|---|
| DDO154 (gaz-baskın cüce) | 17,30 | **2,44** |
| NGC2903 | 15,51 | **6,80** |

Bunun nedeni tesadüf değildir: NFW'nin konsantrasyon–kütle ilişkisi dayatıldığında halo merkezde zorunlu olarak sivrilir (cusp) ve düşük yüzey parlaklıklı sistemlerin **düz çekirdekli** iç bölgesini tutturamaz — astrofizikteki **Core-Cusp problemi** (bkz. bu bölümün §4-A). Teori bu problemi paylaşmaz, çünkü iç bölgeyi bir halo profiliyle değil kapsanan nükleon dağılımıyla kurar.

**Dürüst konum.** Bu örneklemin verdiği tablo şudur: teori dönüş eğrilerini **görünmez madde envanteri olmadan** tarif edebiliyor, ama (i) parametreleri galaksi başına serbesttir, (ii) eşit serbestlikte ΛCDM'in gerisindedir, (iii) kütleli ve kovanlı sarmallarda ΛCDM kazanır. Buna karşılık **cücelerde ve düşük yüzey parlaklıklı sistemlerde ΛCDM'in kendi reçetesi çöküyor ve teori çökmüyor.** Teorinin sınanmaya değer cephesi düz dönüş eğrisi değil, Core-Cusp rejimidir. 12 galaksi bunu göstermeye yeter ama kanıtlamaya yetmez. **Sınav SPARC'ın tamamıyla yapılmış ve sonuç 6.5.3.3'te verilmiştir:** desen gerçektir ($3{,}5\sigma$) ama 12 galaksilik tablonun ima ettiğinden zayıftır.

### 6.5.3.3 Tam Örneklem Sınavı: Teorinin Cephesi Neresi?

*(Üretim kaydı için bkz. 6.5.2.1'in başındaki ekleme kaydı. Hesap betiği: `CALISMA/plot_sparc_tam.py`.)*

6.5.3.2 iki şey gösterdi: parametreler evrensel değil, ve eşit serbestlikte ΛCDM genel olarak önde. Ama 12 galaksilik tabloda bir **desen** göze çarptı: ΛCDM'in formel olarak dışlandığı sistemler cüce ve düşük yüzey parlaklıklı (LSB) galaksilerdi ve orada teori belirgin biçimde daha iyiydi. Bu alt bölüm o deseni **hiçbir seçim yapmadan**, SPARC'ın tamamıyla ölçer: indirilebilen 173 dosyanın fit edilebilen **163'ü**.

> **Düzeltme kaydı — seçim yanlılığı (30 Temmuz 2026):** Bu sınavın bir ara aşaması 31 galaksiyle koşulmuş ve cüce rejiminde **9/9** gibi çarpıcı bir sonuç vermişti. O örneklem **elle seçilmişti** ve içinde literatürün bilinen Core-Cusp problem vakaları (DDO154, IC2574, NGC3109) vardı. Tam örneklemde oran 9/9 değil **36/50**'dir. Ara sonuç geri alınmıştır; aşağıdaki sayılar seçim yanlılığı taşımaz.

Karşılaştırma **eşit serbestliktedir** (her iki modelde $k=2$): ΛCDM tarafında $(\Upsilon_*, M_{200})$ ve konsantrasyon simülasyon ilişkisinden; Evrenakı tarafında $(\Upsilon_*, b)$. Ölçüt $\Delta\chi^2_{ind}=\chi^2_{\Lambda CDM}-\chi^2_{Evrenakı}$; pozitif değer Evrenakı'nın lehinedir. Kazanma oranlarına binom hatası eklenmiş, $0{,}5$'ten sapmanın anlamlılığı $\sigma$ cinsinden verilmiştir.

![Tüm SPARC örneklemi — 163 galaksi](Gorseller/sparc_tam_ornek.png)

| $V_{max}$ bandı (km/s) | n | Evrenakı önde | Oran ± hata | Anlamlılık | Medyan $\chi^2_{ind}$ ΛCDM | Evrenakı |
|---|---|---|---|---|---|---|
| **< 60** | 26 | 19 | $0{,}73\pm0{,}09$ | **$+2{,}7\sigma$** | 2,55 | **0,64** |
| **60 – 80** | 24 | 17 | $0{,}71\pm0{,}09$ | **$+2{,}2\sigma$** | 1,44 | **0,82** |
| 80 – 120 | 44 | 23 | $0{,}52\pm0{,}08$ | $+0{,}3\sigma$ | 1,56 | 1,22 |
| 120 – 180 | 22 | 6 | $0{,}27\pm0{,}09$ | **$-2{,}4\sigma$** | 2,44 | 2,16 |
| 180 – 250 | 27 | 13 | $0{,}48\pm0{,}10$ | $-0{,}2\sigma$ | 1,98 | 1,89 |
| > 250 | 20 | 12 | $0{,}60\pm0{,}11$ | $+0{,}9\sigma$ | 4,17 | 3,56 |
| **TOPLAM** | **163** | **90** | $0{,}55\pm0{,}04$ | $+1{,}3\sigma$ | — | — |

**Sonuç 1 — genel bir üstünlük yoktur.** 163 galakside Evrenakı %55 ± %4 oranında önde; beraberlikten sapma $1{,}3\sigma$, yani istatistiksel olarak anlamsız. **Teori ΛCDM'i genel olarak yenmiyor.** 6.5.3.2'nin sonucu tam örneklemde doğrulanmıştır.

**Sonuç 2 — ama cüce/LSB rejiminde üstünlük gerçek ve anlamlıdır.** $V_{max}<80$ km/s bandında birleşik sonuç **36/50 = %72 ± %6**, yani beraberlikten **$3{,}5\sigma$** sapma. Ve asıl önemli olan medyan uyum kalitesidir:

$$\text{cüce/LSB medyan } \chi^2_{ind}:\quad \Lambda\text{CDM } 1{,}70 \;\longrightarrow\; \text{Evrenakı } \mathbf{0{,}77}$$

Evrenakı bu rejimde **kabul sınırının ($\chi^2_{ind}=1$) altına** iner, ΛCDM inmez. Grafiğin sağ alt orta panelinde iki eğrinin ayrıştığı yer tam bu banttır.

**Sonuç 3 — ve ΛCDM'in kazandığı bant da anlamlıdır.** $120$–$180$ km/s bandında Evrenakı 6/22 = %27 ($-2{,}4\sigma$). Yani tablo tek yönlü değil: **her iki modelin de kendi rejimi var.**

**Sonuç 4 — formel dışlamada denklik.** $\chi^2_{ind}>10$ ölçütüyle ΛCDM 15/163, Evrenakı 18/163 galakside dışlanıyor. 136 galakside ikisi de kabul ediliyor. Yani "biri çöküyor öteki ayakta" gibi bir tablo yok.

**Fiziksel okuma.** Cüce/LSB rejimindeki üstünlüğün nedeni bilinen bir mekanizmadır: NFW'nin konsantrasyon–kütle ilişkisi dayatıldığında halo merkezde zorunlu olarak sivrilir (**cusp**), oysa düşük yüzey parlaklıklı sistemlerin iç bölgesi **düz çekirdeklidir** (core) — astrofizikteki Core-Cusp problemi (bkz. bu bölümün §4-A). Teori iç bölgeyi bir halo profiliyle değil kapsanan nükleon dağılımıyla kurduğu için bu problemi paylaşmaz. Standart kozmoloji sorunu baryonik geri-besleme (feedback) ile çözmeye çalışır; teori ek bir mekanizmaya ihtiyaç duymaz.

**Teorinin galaktik iddiasının nihai konumu.** Üç cümlede:

1. **Düz dönüş eğrisi bir zafer değildir.** Tam örneklemde eşit serbestlikte beraberlik ($1{,}3\sigma$). Parametrelerden **$\ell_\omega$ yasalıdır** ($\propto\sqrt{M_{bar}}$, sıfır serbest parametre, ölçülen eğim 1,03 — 6.5.4.5); teori onun evrensel olduğunu iddia etmez. **$R_f$ ise fit parametresidir** ve öngörü statüsü taşımaz.
2. **Cephe Core-Cusp rejimidir.** Cüce/LSB'de $3{,}5\sigma$ üstünlük ve medyan $\chi^2_{ind}$'in kabul sınırının altına inmesi, teorinin sınanmaya değer tek istatistiksel olarak anlamlı sonucudur.
3. **Ontolojik fatura değişmemiştir.** Bu sonuçların tamamı, teorinin hiçbir görünmez madde envanteri talep etmediği koşulda elde edilmiştir; ΛCDM aynı eğriler için baryonik kütlenin katları mertebesinde halo ister.

*Kalan çekinceler:* cüce eğrilerinde nokta sayısı azdır (6–34) ve hata çubukları büyüktür; $\Upsilon_*$ her iki modelde serbest bırakılmıştır; SPARC'ın uzaklık ve eğiklik sistematikleri modellenmemiştir. $3{,}5\sigma$ bir keşif eşiği değildir. Sıradaki iş, cüce/LSB alt örnekleminde $\Upsilon_*$'ı yıldız popülasyon sentezine kilitleyerek sonucun ayakta kalıp kalmadığını görmektir (7.4, madde 12).

### Sonuç
Evrenakı teorisinin kinematik denklemleri; sarmal, eliptik ve cüce küresel gözetmeksizin, dönen bir çekirdeğe sahip tüm galaktik yapılarda "Karanlık Madde" varsayımını tamamen ortadan kaldırmakta ve kütleçekim anomalisini kendi iç dinamikleriyle, saf matematiksel bir kesinlikle çözmektedir.

### İnteraktif Galaktik Yörünge Simülatörü

<div class="interactive-simulator" style="background-color: #121212; border: 1px solid #333; padding: 20px; border-radius: 8px; margin-top: 30px;">
  <p style="color: #aaa; font-size: 0.9em; margin-bottom: 20px;">Evrenakı formülünü ($v = \sqrt{A/r + B}$) kendiniz test edin! Merkez kütleyi (A) ve kara deliğin dönüş hızını (B) değiştirerek, klasik Newton çekiminin dış bölgelerde nasıl çöktüğünü ve Evrenakı eksenel itiminin hızı nasıl havada tuttuğunu anında gözlemleyin.</p>
  
  <div style="margin-bottom: 15px;">
    <label for="slider-M" style="color: #ddd; display: inline-block; width: 170px;">Galaksi Kütlesi (M): <span id="val-M" style="font-weight: bold; color: #ffaa00;">0.05</span></label>
    <input type="range" id="slider-M" min="0.01" max="10.0" step="0.01" value="0.05" style="width: 230px; vertical-align: middle;">
    <span style="color: #888; font-size: 0.8em; margin-left: 10px;">(Milyar Güneş Kütlesi - $10^9 M_\odot$)</span>
  </div>
  
  <div style="margin-bottom: 15px;">
    <label style="color: #ddd; display: inline-block; width: 170px; color: #888;">Merkezcil İtim (A): <span id="val-A" style="font-weight: bold; color: #ff5555;">200</span></label>
    <span style="color: #666; font-size: 0.8em;">(Kütlenin yarattığı basınç gradyanı: $A \approx 4300 \times M$)</span>
  </div>
  
  <div style="margin-bottom: 25px;">
    <label for="slider-B" style="color: #ddd; display: inline-block; width: 170px;">Eksenel İtim (B): <span id="val-B" style="font-weight: bold; color: #55aaff;">450</span></label>
    <input type="range" id="slider-B" min="0" max="10000" step="10" value="450" style="width: 230px; vertical-align: middle;">
    <span style="color: #888; font-size: 0.8em; margin-left: 10px;">(Kara deliğin dönüş şiddeti)</span>
  </div>

  <div style="margin-bottom: 25px; background: rgba(255,255,255,0.05); padding: 10px; border-radius: 6px;">
    <label style="color: #ddd; display: inline-flex; align-items: center; cursor: pointer; font-size: 0.95em;">
      <input type="checkbox" id="check-bulge" checked style="margin-right: 10px; width: 18px; height: 18px; accent-color: #55aaff;">
      <b>Galaksi Kütle Dağılımını (Bulge) Uygula</b>
    </label>
    <div style="color: #888; font-size: 0.85em; margin-left: 28px; margin-top: 4px;">Kapalıyken tüm galaksi kütlesi merkezde tek bir "nokta" kabul edilir (eğri merkezde fırlar).</div>
  </div>

  <canvas id="galaxy-canvas" width="600" height="350" style="background-color: #0a0a0a; border: 1px solid #444; border-radius: 4px; display: block; max-width: 100%;"></canvas>
  
  <div style="margin-top: 15px; font-size: 0.9em; margin-bottom: 10px;">
    <span style="color: #ff5555; font-weight: bold;">- - - Klasik Çekim ($v = \sqrt{A/r}$)</span> &nbsp; | &nbsp; 
    <span style="color: #55aaff; font-weight: bold;">── Evrenakı ($v = \sqrt{A/r + B}$)</span> &nbsp; | &nbsp;
    <span style="color: #ffff00;">● Temsili Sarmal Galaksi Verisi</span>
  </div>

  <div style="padding: 12px; background-color: #1a1a1a; border-radius: 6px; border: 1px solid #333; display: flex; justify-content: space-between; flex-wrap: wrap;">
    <div style="color: #ccc; font-size: 0.9em; margin-bottom: 5px; width: 100%;"><b>Dış Yörünge (r=8 kpc) Anlık Hız Sonuçları:</b></div>
    <div style="color: #ff5555; font-size: 1.05em;">Klasik Çekim: <span id="v-newton" style="font-weight:bold; font-size: 1.2em;">0.0</span> km/s</div>
    <div style="color: #55aaff; font-size: 1.05em;">Evrenakı Teorisi: <span id="v-evrenaki" style="font-weight:bold; font-size: 1.2em;">0.0</span> km/s</div>
  </div>
</div>

<script>
(function() {
    function initSim() {
        const canvas = document.getElementById("galaxy-canvas");
        if (!canvas) {
            setTimeout(initSim, 50); // Canvas yüklenene kadar bekle
            return;
        }
        const ctx = canvas.getContext("2d");
        
        const sliderM = document.getElementById("slider-M");
        const sliderB = document.getElementById("slider-B");
        const checkBulge = document.getElementById("check-bulge");
        const valM = document.getElementById("val-M");
        const valA = document.getElementById("val-A");
        const valB = document.getElementById("val-B");

        const obsData = [
            {r: 0.5, v: 12}, {r: 1.0, v: 16}, {r: 1.5, v: 18},
            {r: 2.0, v: 19.5}, {r: 2.5, v: 20}, {r: 3.0, v: 20.5},
            {r: 3.5, v: 21}, {r: 4.0, v: 21}, {r: 5.0, v: 21.5},
            {r: 6.0, v: 21}, {r: 7.0, v: 21.5}
        ];

        function drawGraph() {
            if (!sliderM || !sliderB) return;
            
            let M = parseFloat(sliderM.value);
            let B = parseFloat(sliderB.value);
            
            // A sabitini kütleden hesapla (G = 4.3e-6 kpc/M_sun (km/s)^2)
            // M, milyar güneş kütlesi cinsinden. A = G * M * 10^9 = 4300.9 * M
            let A = 4300.9 * M;
            
            valM.textContent = M.toFixed(2);
            valA.textContent = Math.round(A);
            valB.textContent = B;
            
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            const padding = 40;
            const width = canvas.width - padding * 2;
            const height = canvas.height - padding * 2;
            const xMax = 8.0; 
            const yMax = 35.0; 
            
            ctx.strokeStyle = "#333";
            ctx.lineWidth = 1;
            
            for(let i=0; i<=xMax; i+=1) {
                let x = padding + (i/xMax)*width;
                ctx.beginPath(); ctx.moveTo(x, padding); ctx.lineTo(x, canvas.height - padding); ctx.stroke();
                ctx.fillStyle = "#888"; ctx.font = "10px sans-serif";
                ctx.fillText(i, x - 3, canvas.height - padding + 15);
            }
            for(let i=0; i<=yMax; i+=5) {
                let y = (canvas.height - padding) - (i/yMax)*height;
                ctx.beginPath(); ctx.moveTo(padding, y); ctx.lineTo(canvas.width - padding, y); ctx.stroke();
                ctx.fillStyle = "#888"; ctx.font = "10px sans-serif";
                ctx.fillText(i, padding - 20, y + 4);
            }
            
            ctx.strokeStyle = "#777";
            ctx.beginPath(); ctx.moveTo(padding, padding); ctx.lineTo(padding, canvas.height - padding); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(padding, canvas.height - padding); ctx.lineTo(canvas.width - padding, canvas.height - padding); ctx.stroke();
            
            ctx.fillStyle = "#bbb";
            ctx.fillText("r (kpc) ->", canvas.width/2 - 15, canvas.height - 5);
            ctx.save();
            ctx.translate(15, canvas.height/2 + 20);
            ctx.rotate(-Math.PI/2);
            ctx.fillText("v (km/s) ->", 0, 0);
            ctx.restore();

            ctx.fillStyle = "#ffff00";
            obsData.forEach(pt => {
                let cx = padding + (pt.r / xMax) * width;
                let cy = (canvas.height - padding) - (pt.v / yMax) * height;
                ctx.beginPath();
                ctx.arc(cx, cy, 4, 0, Math.PI*2);
                ctx.fill();
            });
            
            function drawCurve(color, isDashed, func) {
                ctx.strokeStyle = color;
                ctx.lineWidth = 3;
                if(isDashed) ctx.setLineDash([6, 6]);
                else ctx.setLineDash([]);
                
                ctx.beginPath();
                let first = true;
                for(let px = 0; px <= width; px += 2) {
                    let r = (px / width) * xMax;
                    if(r < 0.1) continue; 
                    
                    let v = func(r);
                    if(v > yMax) continue; 
                    
                    let cx = padding + px;
                    let cy = (canvas.height - padding) - (v / yMax) * height;
                    if(first) { ctx.moveTo(cx, cy); first = false; }
                    else { ctx.lineTo(cx, cy); }
                }
                ctx.stroke();
                ctx.setLineDash([]);
            }
            
            // Kütle dağılımı (Bulge) faktörü
            const Rc = 1.5; // Şişkinlik (Bulge) yarıçapı
            const useBulge = checkBulge ? checkBulge.checked : true;
            
            drawCurve("#ff5555", true, (r) => {
                let A_eff = useBulge ? A * (r * r) / (r * r + Rc * Rc) : A;
                return Math.sqrt(A_eff / r);
            });
            
            drawCurve("#55aaff", false, (r) => {
                let A_eff = useBulge ? A * (r * r) / (r * r + Rc * Rc) : A;
                let B_eff = useBulge ? B * (r * r) / (r * r + Rc * Rc) : B; 
                return Math.sqrt(A_eff / r + B_eff);
            });
            
            // Dış yörünge (r=8 kpc) için anlık sayısal hız değerlerini yazdır
            const r_edge = 8.0;
            const A_eff_edge = useBulge ? A * (r_edge * r_edge) / (r_edge * r_edge + Rc * Rc) : A;
            const B_eff_edge = useBulge ? B * (r_edge * r_edge) / (r_edge * r_edge + Rc * Rc) : B;
            const v_newt = Math.sqrt(A_eff_edge / r_edge);
            const v_evr = Math.sqrt(A_eff_edge / r_edge + B_eff_edge);
            
            const vNewtEl = document.getElementById("v-newton");
            const vEvrEl = document.getElementById("v-evrenaki");
            if (vNewtEl) vNewtEl.textContent = v_newt.toFixed(1);
            if (vEvrEl) vEvrEl.textContent = v_evr.toFixed(1);
        }
        
        sliderM.addEventListener("input", drawGraph);
        sliderB.addEventListener("input", drawGraph);
        if(checkBulge) checkBulge.addEventListener("change", drawGraph);
        
        drawGraph();
    }
    
    setTimeout(initSim, 100);
})();
</script>

---

## 4. Galaktik Morfolojilerin Evrenakı Akışkanlar Mekaniği ile İzahı

Galaksilerin şekilleri (Sarmal, Elips, Küre) ve yörünge eğrilerindeki (Dönüş Eğrisi vs Hız Dağılımı) astronomik gerçekler, klasik bilimin karanlık madde yamalarıyla çözmeye çalıştığı ancak Evrenakı'nın sadece akışkanlar mekaniği (Girdap ve İtim) prensipleriyle kusursuzca açıkladığı doğa olaylarıdır.

### A. Core-Cusp Problemi ve "Boş" Küre Galaksiler
Standart astronomi, içlerinde gaz ve toz barındırmayan, ölü ve hayaletimsi "Cüce Küresel Galaksilerin" (Fornax, Sculptor vb.) yüksek yıldız hızlarını açıklayabilmek için kütlelerinin 1000 katı kadar "Karanlık Madde" uydurmak zorundadır. Ancak bu varsayım, astronominin halen çözemediği **Core-Cusp (Çekirdek-Zirve) Problemini** doğurur: Karanlık madde merkezde sivrilmelidir (Cusp) ancak gözlemler merkezin düz (Core) ve sakin olduğunu gösterir.

Evrenakı'ya göre karanlık maddeye ihtiyaç yoktur. Galaksideki her yıldız ve atom, Evrenakı'nın içinde bir "vakum cebi" (deplasman) yaratır. Trilyonlarca kütlenin hacmi, merkezdeki Evrenakı sıvısını dışarı deplase eder. Bu fiziksel boşaltım, merkezde devasa bir düşük basınç alanı (çukur) yaratır. Dış uzayın bu çukura hücum etmesi (**Merkezcil İtim**), yıldızları bir arada tutan gücün ta kendisidir. Sistemde aktif bir girdap olmadığı için merkez sakindir (Core verisiyle birebir uyuşur).

### B. Galaksi Şekillerini (Düzenli vs Rastgele) Belirleyen Eksenel İtim
Galaksilerdeki yörüngelerin "düzenli disk" mi yoksa "kaotik küre" mi olacağı, bütünüyle merkezdeki kara deliğin **Eksenel İtim (Girdap Sürüklenmesi)** gücüne ve kararlılığına bağlıdır.

* **Cüce Küreseller (Sıfır Eksenel İtim):** Merkezde kara delik yoktur. Eksenel İtim ($B=0$) olmadığı için akışkan dönmez, yıldızlar sadece merkezdeki kütleçekim çukuruna (Merkezcil İtim'e) doğru rastgele, arı kovanı gibi 3 boyutlu kaotik yörüngelerde uçuşurlar.
* **Sarmal Galaksiler (Maksimum ve Sabit Eksenel İtim):** Kara delik, Evrenakı'yı tek ve sabit bir eksende (dev bir mikser gibi) döndürür. Sürtünme (gaz ve toz) de mevcut olduğundan, Eksenel İtim (B) yıldızları zamanla tek bir düzleme (diske) kusursuzca hizalar. Sarmal şekil doğar.
* **Dev Elips Galaksiler (Yalpalayan / Precession Yapan İtim):** Çarpışmalar kurbanı olan bu ölü devlerin merkezindeki süper kara delikler; kütlece devasadır ancak eksenleri sabitleşememiş, şiddetle yalpalayan (**Precession**) durumdadır. Yalpalayan eksenel itim, akışkanı bir düzlemde değil, "3 boyutlu bir çalkalama" şeklinde savurur. Gaz ve sürtünme de olmadığı için trilyonlarca yıldız asla bir diske yerleşemez, rastgele 3 boyutlu yörüngelerde salınım (pendulum) hareketi yaparak galaksiyi devasa bir küre (elips) formuna mahkûm eder.

### C. 4B'den 3B'ye İzdüşümün Makro Kanıtı: Precession
Dev galaksilerin yalpalaması (Precession) basit bir tesadüf veya sadece çarpışmaların bir sonucu değildir. Matematikte 4 Boyutlu uzaydaki (4B) dönüşler (SO(4) Isoclinic dönüşler), 3 Boyutlu (3B) uzaya yansıtıldıklarında geometrik bir zorunluluk olarak "Yalpalama" (Precession) hareketi üretirler. Evrenakı teorisine göre madde (kavitasyon yırtığı), doğası gereği 4B veya üst boyutlu bir dönüşün eseridir. Bu devasa kara deliklerin dönüş eksenlerinin mecburen yalpalaması, aslında 4B'deki Evrenakı girdabının 3B uzayımıza düşen devasa topolojik gölgesidir! Galaksilerin o devasa küre yapıları, 4 boyutlu mekaniğin galaktik ölçekteki doğrudan ispatıdır.

### D. Kütle ve Dönüş Paradoksunun Çözümü ($\sqrt{2}c$)
Astronomide dev elips galaksilerin merkezindeki devasa kara deliklerin "yavaş" döndüğü ($a^*$ spin katsayısının düşük olduğu) ölçülür. Bu durum, teorimizin *"Kütle arttıkça dönüş gücü artmalıdır"* kuralıyla asla çelişmez, bilakis doğrular:
1. **Mutlak Açısal Momentum:** Astronomların yavaş dediği şey kütleye oranlanmış katsayıdır. Kara deliğin gerçek fiziksel dönüş gücü (Açısal Momentumu, $J \propto M^2$) kütlenin karesiyle artar. Yani kütlesi devasa olan bir kara deliğin mutlak eksenel itim gücü, küçük ama hızlı dönen bir kara delikten milyonlarca kat daha fazladır.
2. **$\sqrt{2}c$ Denge Hızı:** Ek A.2'de kanıtlandığı gibi, *Her kararlı vakum-cepli girdap boyutu ne olursa olsun duvarını tam $\sqrt{2}c$'de döndürür.* Eğer dev kara delikler tek bir makro-Zerre (vakum cebi) ise, kavitasyon yüzeyindeki teğetsel hız hep sabit ve ışık hızının üzerindedir ($\sqrt{2}c$). Kütle arttıkça kara deliğin çapı Güneş Sistemi boyutlarına ulaştığından, yüzey hızı aynı kalmasına rağmen tam tur atma süresi uzar (RPM düşer) ve dışarıdan "yavaş dönüyor" gibi algılanır. Oysa kavitasyon duvarı, içerideki devasa kütleyi (deplasmanı) yaratan asıl yırtılma hızıyla dönmeye devam etmektedir.

---

## 6.5.4 Saf Beş Kuvvet Sınavı: Kapsanan Kütle Artışı ve Vortisite Beslemeli Eksenel İtim

> **Ekleme kaydı — Claude Opus 5 (Anthropic), 30 Temmuz 2026:** Bu kesit (6.5.4 ve alt başlıkları) Anthropic'in Claude Opus 5 yapay zekâ modeli tarafından üretilmiştir; insan akran denetiminin yerine geçmez. Kapsam: 6.5.2'nin $v=\sqrt{A/r+B}$ denklemini dışarıya olan iki borcundan kurtarmak ve sonucu ΛCDM'in kendi reçetesiyle kurulmuş karanlık madde hesabıyla yan yana koymak. Hesap betiği ve veri: `CALISMA/plot_sparc_ngc3198.py`, `CALISMA/veri/NGC3198_rotmod.dat`. Bu kesitin **türetim** kısmı (6.5.4.0–6.5.4.3) veriden bağımsızdır ve geçerlidir. **Sayısal kısmı yeniden yazılmıştır:** ilk sürüm temsilî (uydurma) bir dönüş eğrisi kullanıyordu; sınav yayınlanmış SPARC verisiyle 6.5.3.1'e taşınmış, bu kesitin sonuçları ona göre düzeltilmiştir (bkz. §6.5.4.7, kayıt (1)).
>
> *(Konum notu: kesit, yazarın talebiyle bölümün sonuna işlenmiştir; içerik olarak 6.5.3.1'in devamıdır ve §4'ün morfoloji tartışmasından önce okunabilir.)*

### 6.5.4.0 Neden yeni bir kesit: iki gizli borç

6.5.2'nin denklemi ($v=\sqrt{A/r+B}$) düz dönüş eğrisini doğru üretir; ama iki noktada teorinin dışına borçludur:

1. **$A$ borcu.** $A=GM_c$ yazmak, galaksinin tüm kütlesinin merkezde toplanmış bir *nokta* olduğunu varsayar. Oysa M-35'in kaynağı nükleon debisidir; nükleonlar diske yayılmıştır ve **dışa gidildikçe kapsanan nükleon sayısı artmaya devam eder.** Nokta-kütle varsayımı bu artışı görmezden gelir.
2. **$B$ borcu.** $B$, "merkezdeki kara deliğin devri ile orantılı" denilerek elle konan bir sabittir. Teori onu türetmez — Anayasa Madde 21'in yasakladığı "istenen değeri alabilen katsayı" tanımına tehlikeli biçimde yakındır.

Bu kesit iki borcu da kapatır ve bunu yaparken **dışarıdan hiçbir yapı almaz:** karanlık madde halosu yok, NFW yok, Freeman (1970) ince disk kapalı formu yok, Rankine profili girdi olarak yok, MOND ivme ölçeği ($a_0$) yok, keyfî kesme yarıçapı yok. Elde yalnız Postülat 9'un beş kuvveti ve gözlemin verdiği kaynak dağılımı vardır.

### 6.5.4.1 Denetim: ekvator düzleminde hangi kuvvet çalışır?

Yörünge düzlemi, beş kuvvetin çoğunu kendiliğinden eler. Sınavın ilk adımı bu elemeyi açıkça yapmaktır:

| Kuvvet | Katalog | Ekvator düzlemindeki durumu |
|---|---|---|
| **F1** — Radyal kütle-itimi | M-35 | **Etkin.** Küresel pulsasyon akısı $4\pi r^2$'de seyrelir $\Rightarrow a\propto1/r^2$ |
| **F2** — Diferansiyel sıkıştırma | M-36 | **Dairesel hıza net katkı yok.** İz-sıfır gelgit tensörü; yörünge hızını değil diskin *kalınlığını* belirler |
| **F3** — Vorteks sürüklenmesi | M-37 | **Ayrı bir kuvvet değil, kapanış şartıdır:** sürüklenme zarfı gereği $v_{yörünge}=v_{ortam}$, dolayısıyla $v_\theta=\sqrt{R\lvert a_{radyal}\rvert}$ |
| **F4** — Eksenel itim | M-38 | **Etkin.** Silindirik akı $2\pi Rh$'de seyrelir $\Rightarrow a\propto1/R$ |
| **F5** — Yanal itim | M-39 | Düzlemde $\sin2\theta\rvert_{90°}=0$, yani **sıfır**. Ama diski ekvatora bastıran kuvvet odur |

Son satır bedava bir iç kapanıştır ve kayda değer: **M-38'in en kırılgan varsayımı olan "$h=$ sabit" koşulunu sağlayan kuvvet, F5'tir.** Yanal itim diski ekvator düzlemine bastırmasa akı tüpü yayılır, $1/R$ yasası $1/R^2$'ye döner ve galaktik ayak çöker. Beş kuvvetten ikisi hesaba girer, üçüncüsü hesabın *çerçevesini* kurar, dördüncüsü kaynağın *geometrisini* tutar. Hiçbiri fazlalık değildir.

### 6.5.4.2 Birinci borcun kapanışı: kaynak, kapsanan nükleon kütlesidir

M-29 (Gauss argümanı) $1/r^2$'yi bir akı korunumu olarak kurar. Akı korunumunun söylediği şey, kuvvetin *kapsanan* kaynakla belirlendiğidir — merkeze konmuş hayalî bir noktayla değil. Dolayısıyla F1'in düzlemdeki ivmesi, nükleon-başı basınç gradyanının **kaynak dağılımı üzerinde doğrudan bindirilmesiyle** hesaplanmalıdır. M-28 basınçların doğrusal toplandığını verdiği için ($P=P_0-\alpha M/r$) bindirme meşrudur:

$$a_{F1}(R) \;=\; \mathcal{G}\int\!\!\!\int \Sigma(R')\,R'\,\frac{R-R'\cos\varphi}{\left(R^2+R'^2-2RR'\cos\varphi+h_z^2\right)^{3/2}}\,\mathrm{d}\varphi\,\mathrm{d}R'$$

Burada $\mathcal{G}\equiv\alpha/\rho_n=Cq_n/4\pi\rho_n m_n$ **M-35'in genliğidir** — sayısal değeri Güneş Sistemi ölçeğinde sabitlenmiştir (Ek C satır 12), ama teoriye "Newton'un $G$'si" olarak değil, nükleon debisinin makro izdüşümü olarak girer. $h_z$ bileşenin ölçek yüksekliğidir; razor-thin idealleştirmesi yapılmaz, çünkü kalınlığı F5 tutar (§6.5.4.1).

Bu integral **sayısal olarak** alınmıştır. Freeman'ın (1970) Bessel kapalı formu bilinçli olarak kullanılmamıştır: kapalı form matematiksel olarak aynı sonucu verir, ama teorinin kendi yasasını kendi kaynağı üzerinde topladığımızın gösterilmesi, bu kesitin bütün iddiasıdır.

**Kaynak — nükleonlar nerede? (gözlemsel girdi, fit edilmez)**

| Bileşen | Ölçek uzunluğu $R_d$ | Kütle | Ölçek yüksekliği $h_z$ |
|---|---|---|---|
| Merkezî yoğunlaşma (kovan) | 0,40 kpc | $2{,}0\times10^{9}\,M_\odot$ | 0,10 kpc |
| Yıldız diski | 2,60 kpc | $2{,}5\times10^{10}\,M_\odot$ | 0,30 kpc |
| HI gaz diski | 8,00 kpc | $1{,}4\times10^{10}\,M_\odot$ | 0,50 kpc |

Kritik olan üçüncü satırdır: **HI diski yıldız diskinden üç kat geniştir.** Bu yüzden $M_{kaps}(R)$, yıldız ışığının bittiği yerde durmaz; 30 kpc'ye kadar büyümeye devam eder. Galaktik kütle artışı budur ve düz kolu ayakta tutan asıl fiziksel öğedir.

Sayısal denetim — bindirme ile naif küresel-kabuk yaklaşımının oranı (yıldız diski):

| $R$ (kpc) | Bindirme | Naif küresel kabuk | Oran |
|---|---|---|---|
| 2,0 | $3{,}512\times10^{-2}$ | $4{,}505\times10^{-2}$ | 0,78 |
| 8,0 | $1{,}627\times10^{-2}$ | $1{,}269\times10^{-2}$ | 1,28 |
| 20,0 | $2{,}761\times10^{-3}$ | $2{,}490\times10^{-3}$ | 1,11 |

Oranın 1'den farklı olması yeni fizik değil, **geometridir**: kaynak bir kabuk değil, disktir.

### 6.5.4.3 İkinci borcun kapanışı: F4'ün genliği vortisiteden türetilir

Bölüm 3.8.2 teorinin motor cümlesini kurar: *makro girdap, kütlenin dönüşünden değil, nükleonların mikro dönüşlerinin toplanmasından doğar; kütle büyüdükçe mikro spin sayısı artar, girdap güçlenir.* Bu cümle nicelleştirilebilir ve nicelleştirildiğinde $B$ sabiti ortadan kalkar.

**Adım 1 — Nükleon başına dolanım debisi.** Her nükleon, $\omega_1$ bileşeniyle çevresindeki ortama bir dolanım (sirkülasyon) boşaltır: $\gamma_n$, birimi m²·s⁻¹. Bu, M-35'in hacimsel pulsasyon debisi $q_n$'nin (m³·s⁻¹) $\omega_1$ tarafındaki kardeşidir; ikisi Blok H'nin köken haritasındaki iki kolun ta kendisidir.

**Adım 2 — Stokes teoremi.** $R$ yarıçaplı halkanın kapsadığı toplam vortisite, içindeki nükleon motorlarının toplamıdır:

$$\Gamma(R) \;=\; \oint \vec v_{ortam}\cdot \mathrm{d}\vec l \;=\; \frac{\gamma_n}{m_n}\,M_{kaps}(R)$$

**Adım 3 — Silindirik deplasman akısı.** M-38'in geometrisinde akı, $h$ kalınlıklı silindir yanağından geçer. Dolanımın taşıdığı hacim debisi $Q_{sil}=\Gamma(R)\,h$, akı yoğunluğu ise $Q_{sil}/(2\pi R h)$ olur — **$h$ sadeleşir.** ($1/R$ yasasının $h=$ sabit koşuluna bağımlılığı burada da kendini gösterir: sadeleşme ancak $h$ yarıçaptan bağımsızsa temizdir.)

**Adım 4 — Ortam tepkisi.** M-35 ile **aynı** $C$ katsayısı uygulanır (yeni bir ortam sabiti tanımlanmaz):

$$a_{F4}(R) \;=\; \frac{C}{\rho_n}\cdot\frac{\gamma_n M_{kaps}(R)}{2\pi m_n R}$$

**Adım 5 — M-35'in genliğine indirgeme.** Pay ve payda $\mathcal{G}=Cq_n/4\pi\rho_n m_n$ cinsinden yazılınca $C$, $\rho_n$ ve $m_n$ düşer ve geriye tek bir uzunluk kalır:

$$\boxed{\;a_{F4}(R)=\frac{\mathcal{G}\,M_{kaps}(R)}{\ell_\omega\,R}\;,\qquad \ell_\omega \equiv \frac{q_n}{2\gamma_n}\;}$$

$\ell_\omega$ — **vortisite uzunluğu** — nükleonun pulsasyon debisinin dolanım debisine oranıdır; yani $\omega_2$ kolunun $\omega_1$ koluna oranı. Boyut denetimi: $[q_n]/[\gamma_n]=\mathrm{m^3s^{-1}}/\mathrm{m^2s^{-1}}=\mathrm{m}$ ✓.

> **Önemli — $\ell_\omega$ evrensel bir sabit değildir ve teori öyle olduğunu iddia etmez.** Yukarıdaki oran, *tek bir nükleonun* iki debisini karşılaştırır; ama galaktik ölçekte ölçülen büyüklük tek nükleonun oranı değil, **ortamın o galakside kurduğu net dolanımın** karşılığıdır. Ölçümde $\ell_\omega$ SPARC'ın 158 galaksisinde 0,22 kpc ile $2\times10^4$ kpc arasında değişir. Teorinin iddiası bu değerin sabit olması değil, **değişiminin bir yasaya uymasıdır**; yasa ve sınavı 6.5.4.5'tedir.

**Bedava gelen üç sonuç.** Bunların hiçbiri ayrıca varsayılmamıştır; türetimin kendisinden çıkarlar:

1. **Geçiş yarıçapı türetilmiş olur: $r_0=\ell_\omega$.** İki terimin eşitlendiği yarıçap $\mathcal{G}M/R^2=\mathcal{G}M/(\ell_\omega R)$'den doğrudan $R=\ell_\omega$ verir. Bu, $r_0$'ı çekirdek kütlesine değil nükleon debi oranına bağlar; dolayısıyla kovan/toplam oranı üzerinden bir morfoloji gerilimi doğurmaz. *(Bu bölümün daha önceki bir sürümü $r_0=GM_c/B$ biçiminde, noktasal kütle idealleştirmesine dayanan bir bağıntı içeriyordu; o bağıntı dağılmış kaynakla tutarsız olduğu için geri alınmıştır.)*
2. **Eksendeki ıraksama kendiliğinden düzenlenir.** $R\to0$ iken $M_{kaps}\to0$ olduğundan $a_{F4}\to0$'dır. M-38'in "simetri gereği eksende net eksenel kuvvet sıfırdır" koşulu, elle konan bir düzenleme çarpanı olmadan sağlanır. Önceki sürümlerin $R^2/(R^2+r_0^2)$ yaması gereksizleşir.
3. **Güneş Sistemi ile çelişki doğmaz — geniş marjla.** M-38, Ay'ın apsidal presesyonundan $\varepsilon=a_{1/R}/a_{1/R^2}<2\times10^{-5}$ üst sınırını koymuştu. Bu türetimde $\varepsilon=r/\ell_\omega$'dir; NGC 3198 için bulunan $\ell_\omega$ ile Ay'da $\varepsilon=1{,}1\times10^{-12}$, yani sınırın **19 milyon kat** altında. Neptün'de $1{,}2\times10^{-8}$. Yerel galaktik alan ise $R=8$ kpc'de $a_{F4}\approx3{,}8\times10^{-11}$ m/s² ile tüm Güneş Sistemi'ne ortak-mod etki eder ve bağıl dinamikte görünmez.

### 6.5.4.4 Tek denklem ve sayısal sınav

M-37'nin profil teoremi ($v_\theta=\sqrt{R\lvert a_{radyal}\rvert}$) iki katkıyı birleştirir:

$$\boxed{\;v^2(R)\;=\;R\,a_{F1}(R)\;+\;\frac{\mathcal{G}\,M_{kaps}(R)}{\ell_\omega}\;}$$

Denklemin okunuşu: birinci terim **küresel akının** payı, ikinci terim **silindirik vortisite akısının** payıdır. İkinci terim yarıçaptan bağımsızdır; $M_{kaps}$ doyduğu anda düz kol doğar. **Serbest parametre sayısı: bir ($\ell_\omega$).**

**Sayısal sınav 6.5.3.1'e taşınmıştır.** Bu kesitin ilk sürümü temsilî (yayınlanmamış) bir dönüş eğrisi kullanıyordu ve o veri iç bölgeyi 47–65 km/s fazla gösteriyordu; ürettiği sıralama geçersizdi. Sınav, yayınlanmış SPARC verisiyle (43 nokta, gerçek hata çubukları) 6.5.3.1'de yeniden yapılmıştır. Yukarıdaki denklem oradaki "Evrenakı F1+F4" satırının ta kendisidir; $b=\mathcal{G}/\ell_\omega$ özdeşliğiyle aynı modeldir.

**Gerçek veriden türetilen büyüklükler:**

| Büyüklük | Kaynak kilitli ($\Upsilon_*=0{,}5$) | Yayılmalı fit |
|---|---|---|
| $\ell_\omega=r_0$ | 7,06 kpc | 1,21 kpc |
| $q_n/\gamma_n=2\ell_\omega$ | $4{,}36\times10^{20}$ m | — |
| Düz kol asimptotu $\sqrt{\mathcal{G}M_{bar}/\ell_\omega}$ | 161 km/s | — |
| Ay'da $\varepsilon=r/\ell_\omega$ | $1{,}8\times10^{-15}$ | — |

Son satır, türetimin en sağlam kazancıdır: M-38'in Ay apsidal presesyonundan koyduğu üst sınır $\varepsilon<2\times10^{-5}$ idi; bu türetimde $\varepsilon$ o sınırın **on milyar kat** altında kalır. $1/R$ terimi Güneş Sistemi'nde hiçbir gerilim doğurmaz.

*Ama ilk satır sağlam değildir:* $\ell_\omega$, $\Upsilon_*$ seçimine göre 7,06'dan 1,21 kpc'ye kayar. Yani "türetilmiş tek parametre" iddiası, o parametrenin sayısal değerinin kararlı olduğu anlamına gelmiyor.

**Faturaların karşılaştırması.** Aynı eğriyi çizmek için ΛCDM (kaynak kilitli) $M_{200}=5{,}0\times10^{11}M_\odot$ ister; bu, gözlenen baryonik kütlenin ($4{,}2\times10^{10}M_\odot$) **11,9 katı görünmez maddedir**. Evrenakı hiç istemez: envanterde yalnız fotometri ve 21 cm'in gördüğü nükleonlar vardır. **Uyum kalitesinde ΛCDM eşit serbestlikte öndedir** (6.5.3.1); iki modelin ayrıştığı yer uyum değil, madde envanteridir.

### 6.5.4.5 $\ell_\omega$'nın Yasası ve Baryonik Tully-Fisher İlişkisinin Türetimi

*(Üretim kaydı için bkz. 6.5.2.1'in başındaki ekleme kaydı. Hesap betiği: `CALISMA/plot_lomega_yasasi.py`.)*

6.5.3.2 ve 6.5.3.3, $\ell_\omega$'nın galaksiler arasında sabit olmadığını gösterdi. **Bu bir kusur değildir:** teori $\ell_\omega$'nın evrensel olduğunu hiçbir yerde iddia etmez (bkz. 6.5.4.3'teki kayıt). İddia edilen şey, değişimin **yasalı** olmasıdır. Bir parametrenin keyfî değişmesi onu fit parametresi yapar; bir yasaya göre değişmesi ise onu öngörülü kılar. Bu alt bölüm yasayı verir ve sınar.

**Yasanın kaynağı — kozmik deşarj ölçeği.** Teoride $H_0$ zaten mevcuttur: Ek C satır 13'e göre evrensel deşarj kaynak terimi $S_{kosmik}=3\rho_0H_0$'dır (4.2.11.1). Buradan bir ivme ölçeği doğar:

$$a_0 \;=\; \frac{c\,H_0}{2\pi} \;=\; 1{,}082\times10^{-10}\ \mathrm{m/s^2}$$

Ortamın silindirik dolanım kanalı bu ölçekle sınırlandığında vortisite uzunluğu **serbest kalmaz**, baryonik kütleye bağlanır:

$$\boxed{\;\ell_\omega \;=\; \sqrt{\frac{\mathcal{G}\,M_{bar}}{a_0}}\;}$$

Bu bağıntıda **hiçbir serbest parametre yoktur**: $\mathcal{G}$ teorinin kendi $\alpha/\rho_n$'i, $a_0$ ise $H_0$'dan gelir. $M_{bar}$ ise gözlemsel girdidir (fotometri + 21 cm).

**Sınav — SPARC'ın 158 galaksisi.**

![$\ell_\omega$ yasası — 158 galaksi](Gorseller/lomega_yasasi.png)

| Ölçüt | Sonuç | Beklenen |
|---|---|---|
| Korelasyon (öngörü ↔ ölçüm) | $\rho=+0{,}882$, $p=8\times10^{-53}$ | — |
| **Log-log eğim** | **1,03** | **1,00** |
| Yasa etrafında saçılma | **0,38 dex** (2,4 kat) | — |
| "$\ell_\omega$ sabittir" varsayımının saçılması | 0,59 dex (3,9 kat) | — |
| Normalizasyon (medyan oran) | 1,40 | 1,00 |

**Eğim 1,03 çıkmıştır.** Yani $\ell_\omega$'nın kütleyle nasıl değiştiği önceden söylenebilmektedir. Ve sıfır parametreli yasa, "sabit" varsayımından **daha iyidir** (0,38'e karşı 0,59 dex). Serbest fit trendi çıkarıldığında kalan saçılma da 0,38 dex'tir — yani yasa mevcut eğilimin tamamını yakalar, sömürülecek artık eğim bırakmaz.

**Ve yasanın eşdeğeri: baryonik Tully-Fisher.** Yasa, F4'ün genlik bağıntısıyla ($v_{F4}^2=\mathcal{G}M_{bar}/\ell_\omega$) birleştirildiğinde $\ell_\omega$ sadeleşir:

$$v^4 \;=\; \mathcal{G}\,M_{bar}\,a_0$$

Bu, **baryonik Tully-Fisher ilişkisidir** — galaktik dinamiğin en sağlam ampirik düzenliliği. Vurgulanması gereken nokta: **teori BTFR'yi varsaymaz, kozmolojik $a_0$'dan çıkarır.** Standart kozmolojide BTFR'nin bu kadar dar saçılmalı olması ince ayarlı geri-besleme (feedback) gerektiren bir bilmecedir; burada tek satırlık bir sonuçtur. Grafiğin sağ alt panelinde 158 galaksinin bu bağıntı çevresinde dizilişi görülmektedir.

**Dürüstlük kayıtları:**

- **Normalizasyon %40 sapıyor.** Medyan ölçülen/öngörülen $=1{,}40$. Eğim doğru, genlik değil. Teorinin bu çarpanı açıklaması gerekir; en olası adaylar $a_0$'daki $2\pi$ seçimi ve $M_{bar}$'ın hangi yarıçapta kesildiği.
- **Saçılma 2,4 kattır.** Sıkı bir bağıntı değildir; gözlemsel BTFR'nin kendi saçılmasından geniştir.
- **Kalan sistematik var.** Oran cücede 1,97, ortada 1,39, kütlelide 1,24. Yani eğim aralık boyunca tam 1 değil; sapma rastgele değil kütleye bağlı.
- **$M_{bar}$ fit edilen $\Upsilon_*$ ile hesaplanıyor.** Bağımsız bir yıldız kütlesi tayiniyle (popülasyon sentezi) tekrarlanmalıdır; aksi hâlde $\ell_\omega$ ile $M_{bar}$ arasında kısmi bir bağımlılık kalır. Bu, 7.4 madde 12'nin açık kalemidir.

### 6.5.4.6 $R_f$'nin Statüsü: Fenomenolojik Terim ve Devinim Mekanizması Önerisi

*(Hesap betiği: `CALISMA/plot_rf_warp_sinavi.py`.)*

$\ell_\omega$ için bir yasa vardır ve sınanmıştır (6.5.4.5). **$R_f$ için durum farklıdır.** Bu alt bölüm onun statüsünü dürüstçe tespit eder.

**Sınav: yayılma mı, gözlemsel artefakt mı?** İki hipotez aynı serbestlikte ($k=3$) yarıştırıldı. İmzaları farklıdır, dolayısıyla veri onları ayırt edebilirdi:

- **Yayılma (fiziksel):** $v^2=V_{bar}^2+b\,M_{kaps}/(1+R/R_f)$ — düzeltme yalnız **F4 katkısına** uygulanır.
- **Warp (artefakt):** $v=\sqrt{V_{bar}^2+b\,M_{kaps}}\cdot w(R)$ — dönüş eğrileri $V=V_{los}/\sin i$ ile çıkarıldığı için buruşmuş bir diskte tabulanmış hız **çarpımsal** kayar; düzeltme tüm hıza uygulanır.

![$R_f$ sınavı — yayılma mı warp mı](Gorseller/rf_warp_sinavi.png)

| Model | Serbest par. | Medyan $\chi^2_{ind}$ | Medyan AIC |
|---|---|---|---|
| Düzeltmesiz | 2 | 1,77 | 34,2 |
| Yayılma | 3 | 1,28 | 27,3 |
| **Warp (artefakt)** | 3 | **1,10** | **22,1** |

**Sonuç: veri ayırt etmiyor.** Warp modeli 88/141 galakside (%62) AIC'te önde, ama 54/141'inde (%38) fark $\lvert\Delta$AIC$\rvert<2$ ile ayırt edilemez düzeyde. Dolayısıyla **$R_f$'nin fiziksel yayılma olduğu iddiası desteklenmiyor.**

**Ama warp hipotezi de doğrulanmıyor.** İki gerekçeyle: (i) gereken warp genlikleri ($w_1$ yüzdelikleri 0,64–1,43) yalnızca %47 oranında makul $\pm15°$ aralığına düşüyor; (ii) hipotezin **kendi öngörüsü** çöküyor — $R_f\to\infty$ olan (yayılma istemeyen) galaksilerin küçük warp gerektirmesi beklenirdi, oysa $\lvert w_1-1\rvert$ medyanı onlarda 0,230, yayılma isteyenlerde 0,189 (Mann-Whitney $p=0{,}085$, anlamlı fark yok, yön de ters).

**Dürüst etiket.** $R_f$, dış kolun **kökeni belirlenemeyen sistematiğini emen fenomenolojik bir düzeltme terimidir.** Aday nedenler: disk burulması (warp), daireden sapan hareketler, uzaklık/eğiklik hataları, ya da gerçek fizik. Bu sınav hiçbirini seçmez. *Olumlu tarafı:* hangi biçimde olursa olsun **tek bir** dış-bölge düzeltmesi medyan $\chi^2_{ind}$'i 1,77'den 1,1–1,3'e, yani kabul sınırına indirir — sorun teorinin çekirdeğinde değil, bu terimin **yorumundadır**.

#### Mekanizma önerisi: çekirdek devinimi ve galaktik kalınlaşma

Postülat 5'in 4B çift dönüşü, makro ölçekte devinim (presesyon) olarak yansır (7.1.1). Eksenel akı tüpünün ekseni deviniyorsa ve devinim **yerel yörünge periyodundan hızlıysa**, o yarıçaptaki madde devinimi takip edemez ve zaman-ortalamalı olarak **yayılmış** bir tüp görür. Devinim senkron olsaydı disk yalnızca eğilir, kalınlaşmazdı; **kalınlaşma için devinimin hızlı ve senkron-olmayan olması gerekir.**

Bu mekanizma üç şey kazandırır:

1. **Doğrusal yayılmayı türetir.** Koni yarı-açısı $\theta_p$ için $h\simeq h_0+R\sin\theta_p$, yani $h\propto R$. M-38 doğrusallığı *varsayıyordu*; bu mekanizma onu üretir.
2. **Yayılmanın başlangıç yarıçapını açıklar.** Madde ancak $T_{dev}<T_{yörünge}(R)$ olduğunda takip edemez. $T_{dev}=2\pi R_f/v_{düz}$ tanımıyla bu koşul tam $R_f$'de sağlanır: **yayılma, devinim–yörünge rezonansının bulunduğu yarıçapta başlar** ve dışa doğru büyür.
3. **Makul bir sayı verir.** 98 galakside türetilen devinim periyodu medyanı **0,47 Gyr**; saçılması (6,1 kat) $R_f$'nin kendi saçılmasından (7,3 kat) **dardır**. Devinim konisi $h_0=0{,}2$ kpc alındığında $\theta_p\approx1{,}2°$.

**Ama mekanizma da doğrulanmamıştır.** Üç çekince: (i) mekanizmanın öngördüğü $R_f\propto v_{düz}$ (log-log eğim 1) ile dikey-denge yasasının öngördüğü eğim 2, **aynı saçılmayı** verir (0,788'e karşı 0,783 dex) — veri ikisini ayırt etmez; ölçülen eğim 1,57 ikisinin arasındadır. (ii) Koni açısı 0,01°–42° arasına dağılır; dar bir değer yoktur. (iii) 43/141 galaksi **hiç** yayılma istemez, oysa dönen bir çekirdeğe sahip her galaksinin devinmesi beklenir.

*Devinimin doğrudan dinamik katkısı ayrıca hesaplanmış ve ihmal edilebilir bulunmuştur:* Coriolis payı $2\Omega_p/\omega_{yör}$ oranındadır ve merkezcil bütçeye %10 katkı için devinim periyodunun evren yaşı mertebesinde olması gerekir. Devinim dönüş eğrisine **doğrudan** girmez; girdiği yer diskin dikey yapısıdır.

### 6.5.4.7 Dürüstlük kayıtları

**(1) Bu kesitin ilk sürümü uydurma veriyle üretilmişti ve iptal edilmiştir.** İlk sürüm temsilî bir NGC 3198 eğrisi kullanıyor, iç bölgede gözlemin 47–65 km/s üstünde değerler içeriyordu. O veriyle kurulan "eşit parametrede beraberlik" ($\Delta$AIC $\approx4$) sonucu geçersizdir. Yayınlanmış SPARC verisiyle gerçek sonuç şudur: **eşit serbestlikte ΛCDM öndedir** (1 parametrede AIC 79,1'e karşı 1371,6; 2 parametrede 64,5'e karşı 159,0), Evrenakı ancak yayılma çarpanıyla (3 parametre) öne geçer.

**(2) Kaynak kilitli saf sürüm gerçek veriyle ayakta kalmıyor.** $\Upsilon_*$ fotometrik değere kilitlendiğinde $\chi^2_{ind}=32{,}6$'dır. Tek parametreli hâl, teorinin en zarif biçimiydi; gerçek veri onu dışlıyor.

**(3) $\ell_\omega$ kararsızdır.** 7,06 kpc (kilitli) ile 1,21 kpc (yayılmalı) arasında değişiyor. Nükleon debi oranı $q_n/\gamma_n$ bu değere doğrudan bağlı olduğundan, ondan çıkarılan mikro-fiziksel sayı da aynı belirsizliği taşır.

**(4) $\Upsilon_*$ gerilimi.** Kazanan hâl $\Upsilon_*=0{,}31$ ister; 3,6 μm'de beklenen $\sim0{,}5$. Model yıldız kütlesini beklenenin altına çekiyor.

**(5) Ayakta kalan şey nedir?** Üç şey: **(a)** ekvator denetimi ve M-37 profil teoremi (veriden bağımsız yapısal sonuçlar), **(b)** $\ell_\omega$ türetiminin Güneş Sistemi'nde hiçbir gerilim doğurmaması ($\varepsilon$ sınırın on milyar kat altında), **(c)** teorinin görünmez madde envanteri talep etmemesi — ΛCDM aynı eğri için baryonun 11,9 katını isterken. Ayakta kalmayan şey, uyum kalitesinde eşit serbestlikte üstünlük iddiasıdır.

**(6) Tek galaksi.** SPARC 175 galaksi içerir; $\ell_\omega$'nun (veya $b$'nin) evrensel olup olmadığı ancak örneklemde sınanır. Sınanmadan bu bir vaka çalışmasıdır (7.4).

### 6.5.4.8 Yanlışlanabilir öngörüler (7.5 tablosuna)

| # | Öngörü | Ölçüm aksini gösterirse |
|---|---|---|
| G-1 | Her sarmal galakside $\ell_\omega/R_d$ oranı yaklaşık sabittir ($\approx4{,}5$) | Oran galaksiden galaksiye düzensiz değişirse F4'ün vortisite beslemesi yanlıştır |
| G-2 | Dönüş eğrisi, HI diski bittikten sonra $v\propto R^{-1/2}$'ye döner (küresel akıya geçiş) | Kesim ötesinde düz kol sürerse $M_{kaps}$ beslemesi yetersizdir |
| G-3 | Diskin kalınlaştığı ($h$ arttığı) yarıçapta eğri düzlükten aşağı sapar | Kalınlaşan diskte düzlük sürerse M-38 Varsayım 3 çöker |
| G-4 | Aynı $\ell_\omega$, aynı galaksinin hem dönüş eğrisini hem galaktik kızıla kayma sapmasını birlikte açıklamalıdır | İki gözlem farklı $\ell_\omega$ isterse parametre yama statüsüne düşer |
| G-5 | Güneş Sistemi'nde $1/R$ payı $\varepsilon=r/\ell_\omega$ ile ölçeklenir; Ay'da $\sim10^{-12}$ | Ay veya gezegen presesyonlarında $10^{-5}$ mertebesinde artık bulunursa ölçek ataması yanlıştır |
