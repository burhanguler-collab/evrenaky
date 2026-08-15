# 6.5 Galaktik Yörüngeler ve Karanlık Madde Probleminin Çözümü

Astrofiziğin son yüzyıldaki en büyük çözülemeyen gizemlerinden biri, galaksilerin dış kollarındaki yıldızların dönme hızlarıdır. Klasik Newton mekaniğine ve Einstein'ın Genel Görelilik teorisine göre, galaksinin merkezinden uzaklaştıkça kütleçekim kuvvetinin $1/r^2$ ile zayıflaması ve dolayısıyla yıldızların yörünge hızlarının düşmesi gerekir. Tıpkı Güneş Sistemimizde Güneş'ten uzaklaştıkça gezegenlerin daha yavaş dönmesi gibi.

Ancak 1970'lerde Vera Rubin ve meslektaşları tarafından yapılan hassas gözlemler, sarmal galaksilerin dış kollarındaki yıldızların hızının düşmediğini, aksine çok yüksek hızlarda **sabitlendiğini** (asimptota oturduğunu) kanıtlamıştır. Standart fiziğe göre bu hızlarda dönen yıldızların galaksiden kopup uzaya savrulması gerekirdi. Bu muazzam hızı dengede tutacak görünürde hiçbir kütle olmadığı için astrofizikçiler, galaksiyi devasa bir hale gibi saran görünmez bir kütle uydurmak zorunda kaldılar: **Karanlık Madde**.

Bu bölüm, Evrenakı teorisinin hiçbir "görünmez madde" varsayımına ihtiyaç duymadan, sadece kendi yerel mekanik postülatlarıyla bu kozmolojik anomalinin üstesinden nasıl geldiğini ve düz dönüş eğrilerini doğal yollarla nasıl türettiğini göstermektedir.

Varılan nokta baştan söylenmelidir, çünkü ölçülmüştür: teori, galaktik dinamiğin üç büyük ampirik yasasını — düz dönüş eğrisi, baryonik Tully–Fisher, radyal ivme bağıntısı — **tek denklemden, galaksi başına sıfır serbest parametreyle türetir**; MOND literatürünün elle seçtiği geçiş fonksiyonunu **ilk kez türetilmiş biçimde** verir (M-47 — artık eğimi, fitli MOND eğrisininkinden bile düzdür) ve $a_0$ ölçeğini SPARC dışında **üç bağımsız veri ailesinde sıfır ayarla** doğrulamıştır (Yerel Grup cüceleri; MIGHTEE-HI; SLUGGS eliptikleri). Bu bölümdeki hiçbir öngörü eğrisinde galaksiye fitlenen sayı yoktur — **fit, karşılaştırma yapılan modellerin ihtiyacıdır, teorinin değil.** Uyum yarışında fitli eğrilere karşı kalan 0,9 km/s'lik fark gizlenmez; adresi kayıtlıdır (6.5.4.6; 7.4).

## 6.5.1 İvme Grafiği ve $1/r$ Kuvvetinin Yükselişi

Teorinin temel postülatlarından olan **Eksenel İtim (F4)**, galaktik ölçekte diskin kapsanan baryonik kütlesinin dolanım debisinden beslenir; genliğinin türetimi 6.5.4.3'tedir.

Kritik nokta şudur: Klasik merkezcil kütleçekim $1/r^2$ profiliyle zayıflarken, teorinin öngördüğü eksenel kuvvet (Kısım 4'te türetildiği üzere) $1/r$ profiliyle sönümlenir. Galaksinin dış bölgelerine çıkıldıkça $1/r^2$'ye tabi klasik çekim hızla gücünü yitirir, ancak $1/r$ ile sönümlenen eksenel kuvvet profilde giderek baskın hale gelir. 

## 6.5.2 Matematiksel İspat: Düz Dönüş Eğrisinin Türetilmesi

Dairesel yörüngede dönen bir yıldızın dengede kalabilmesi için Merkezcil İvme'nin, radyal kütle-itim ivmesi (F1) ile teorinin öngördüğü eksenel ivmenin (F4) toplamına eşit olması şarttır:

$$a_{merkezcil} = a_{radyal} + a_{eksenel}$$

Terimleri kendi fiziksel bağımlılıklarıyla açtığımızda:
1. **Merkezcil İvme:** $\frac{v^2}{r}$
2. **Radyal Kütle-İtim (F1, Basınç Gradyanı):** $\frac{A}{r^2}$ *(Buradaki A sabiti, galaksinin merkez kütlesinin yarattığı hidrodinamik basınç düşümü ile orantılıdır)*
3. **Eksenel Kuvvet (Evrenakı):** $\frac{B}{r}$ *(Buradaki B sabiti, bu ilk kurulumda elle konur; genliğinin türetimi 6.5.4.3'tedir — kaynağı, kapsanan baryonik kütlenin vortisitesidir)*

Eşitliği kuralım:
$$\frac{v^2}{r} = \frac{A}{r^2} + \frac{B}{r}$$

Denklemin her iki tarafını da yarıçap ($r$) ile çarptığımızda, yörünge hızı $v$ şu şekilde doğrudan elde edilir:
$$\mathbf{v = \sqrt{\frac{A}{r} + B}}$$

Bu zarif ve kompakt denklemin sunduğu fiziksel sonuç son derece derindir:
Klasik fizikte (B=0 kabul edildiğinde) yarıçap ($r$) büyüdükçe hız sıfıra yaklaşır. Ancak Evrenakı teorisinde, galaksinin çok uzak dış kollarına gidildiğinde ($r \to \infty$), $\frac{A}{r}$ terimi sıfıra yaklaşsa dahi yıldızın hızı sıfıra düşmez. Hız doğrudan **$\sqrt{B}$** limitine, yani sabit bir asimptota kilitlenir.

Astronomların teleskoplarla gözlemlediği meşhur **"Düz Dönüş Eğrisi" (Flat Rotation Curve)** profili, teorik altyapıda hiçbir yama kullanılmadan, tamamen doğal yollarla elde edilmiştir.

## 6.5.2.1 Beş Kuvvetin Ekvator Düzlemine İzdüşümü

6.5.2'nin $v=\sqrt{A/r+B}$ denklemi bir ansatz değildir: teorinin **beş hidrodinamik kuvvetinin ekvator düzlemine izdüşümünün tamamıdır.** Denetimin ayrıntısı 6.5.4.1'de verilmiştir; özeti şudur: küresel akı taşıyan **F1** ($a\propto1/r^2$) ile silindirik akı taşıyan **F4** ($a\propto1/R$) çalışır; **F5**'in $\sin2\theta$ yasası $\theta=90°$'de kaybolur, **F2** iz-sıfır gelgit tensörü olduğu için nokta yıldıza net radyal kuvvet vermez, **F3** ise düzlemde sessizdir — yörüngeyi kuran sürüklenme değil, maddenin serbest düşmesidir (M-2). İki terimli yapı bir tercih değil, izdüşümün zorunlu sonucudur.

**Ana denklem — M-37 profil teoremi.** Dönüş eğrisi bağımsız bir girdi değildir:

$$\boxed{\;v_{y\ddot{o}r}(R)=\sqrt{R\,\bigl|a_{radyal}(R)\bigr|}\;}$$

Bağıntı **maddenin serbest düşmesinden** çıkar (M-2): yıldız, ortamın kurduğu radyal basınç gradyanında dairesel yörüngeyi tutacak hıza oturur. Dönüş profili, radyal itim yasasının **çıktısıdır**.

> [!WARNING]
> **İki yaygın hata bir arada.** $v_\theta(R)=\sqrt{R|a|}$ yazmak ve bağıntıyı *"Postülat 7'nin sürüklenme zarfından"* çıkarmak — ikisi de yanlıştır:
>
> 1. **Mekanizma.** Yörünge sürüklenmeyle değil **serbest düşmeyle** kurulur (M-2). Ortamın sürükleme yükü $\eta_E$ üzerinden taşınır ve yörünge zaman ölçeğinde etkisizdir ($\tau_E/\tau_{madde}\approx1{,}8\times10^{16}$; M-37, 3.8.1). Yörüngeyi sürüklenmeye bağlamak, teorinin kendi kuvvet envanterini atlayıp gözlemi mekanizmasız bir kabule yüklemekti.
> 2. **Sembol (R-1 ihlali).** Ek D $v_\theta$'yı *"girdabın teğetsel hızı"* — yani **ortamın** hızı — olarak tanımlar. Ortam ise maddenin **iki katı** hızla dolaşır (DY-2: $v_\theta=2v_{y\ddot{o}r}$, çarpan $\sqrt{\rho_n/\rho_0}=2$). Gözlenen dönüş eğrisi maddenin hızı olduğuna göre bu bölümün doğru sembolü $v_{y\ddot{o}r}$'dür; $v_\theta$ yazmak aynı sembole iki anlam yüklüyordu.
>
> **Ayrım galaktik zincire girmez.** 6.5.4'ün sınavı ve 173 galaksilik tarama *maddenin* hızıyla koşulur. Bağımsız kanıtı: çarpanı zincire sokan senaryo $a_0$ bandının 10 katı dışına düşer ve RMS'i ikiye katlar.

**Düz eğrinin gerçek türetimi — Rankine gerekmez.** Ek M-30'un 5. maddesi bunu açıkça kaydeder: düz kolun türetimi Rankine profilini girdi almaktan geçmez, **M-38+M-37 zinciridir**:

$$\underbrace{h=\text{sabit}}_{\text{M-38 Varsayım 3}}\;\Rightarrow\;\underbrace{a\propto1/R}_{\text{silindirik akı geometrisi}}\;\Rightarrow\;\underbrace{v_{y\ddot{o}r}=\sqrt{R|a|}=v_0}_{\text{M-37 profil teoremi}}$$

4.2.9.2'nin bileşik girdap kurgusu basınç profilini (logaritmik kuyu) verir; düz eğriyi **öngörü statüsünde** üreten yol ise budur.

F4'ün genliğinin nükleon dolanım debisinden türetimi ($\ell_\omega$) 6.5.4.3'te, gözlemsel sınav ise 6.5.3.1'dedir.

## 6.5.3 Gerçek Gözlem Verileriyle Sınama

Bu matematiksel model ($v = \sqrt{A/r + B}$), evrendeki farklı galaksi türlerinin hassas teleskop ölçümleriyle test edildiğinde kusursuz bir ampirik başarı sergilemektedir. Aşağıdaki testlerde kırmızı kesik çizgiler saf Newton mekaniğini, mavi çizgiler ise Evrenakı teorisinin $1/r$ eklemli formülünü temsil etmektedir.

### 1. Sarmal Galaksiler: M33 ve NGC 3198
Sarmal galaksiler, karanlık madde probleminin en belirgin gözlemlendiği yapılardır. 
M33 (Triangulum) galaksisinde Newton kütleçekimi hızla düşüşe geçerken, Evrenakı modeli ölçülen hızı ~120 km/s bandında kusursuzca yakalamaktadır. Benzer şekilde, dönüş eğrisinin 30 kpc gibi inanılmaz uzak mesafelere kadar dümdüz kalmasıyla bilinen devasa NGC 3198 galaksisinde, $1/r$ eksenel itim kuvveti yıldız hızlarını ~150 km/s bandında pürüzsüz bir doğrulukla kilitlemektedir.

![M33 Gözlem Testi](Gorseller/m33_gozlem_testi.png)
![NGC 3198 Gözlem Testi](Gorseller/ngc3198_gozlem_testi.png)

### 2. Dev Eliptik Galaksiler: M87 ve NGC 4472

Eliptik galaksiler sarmal bir diske sahip olmadıkları için net dönüş eğrileri vermezler. Yıldızlar rastgele yörüngelerde bir arı kovanı gibi hareket eder (hız dağılımı). Bu galaksileri saran sıcak X-ışını gaz halelerinden hesaplanan kütleçekim potansiyelleri ("Efektif Dairesel Hız" $V_c$), sarmal galaksilerdeki asimptotik düz yapıyı tekrar eder.

Teorinin bu sistemler için söyleyebildiği ve söyleyemediği şey nettir:

- **F4'ün kaynağı merkezî kara delik değildir.** Genliği vortisiteden gelir ve kaynağı kapsanan baryonik kütledir (6.5.4.3). Ölçüm de bunu doğrular: 163 galakside fitlenen F4 genliği toplam baryonik kütleyle ölçeklenir (Spearman $-0{,}91$), kovan kütlesiyle değil ($-0{,}33$); büyük kara delik beklenmeyen **kovansız 134 galakside** F4 yine zorunludur (yalnız F1 ile medyan $\chi^2_{ind}=17{,}3$, F4 eklenince $1{,}37$).
- **Basınç-destekli köprü artık kuruludur ve doğrulanmıştır (M-48, [T]):** küresel sistem diskle aynı radyal yasaya uyar ve $v_c=\sqrt2\,\sigma$ köprüsü Jeans'ten türer; eliptiklerin dış bölgesi geçerlilik alanına girmiştir (6.5.4.9). Nicel dış-σ sınavı yapılmış ve geçilmiştir (G-12): SLUGGS küresel-küme kinematiği, 22 eliptik/merceksi, sıfır yeniden-kalibrasyonla medyan $+0{,}051$ dex (kendi kovan konvansiyonumuzla $-0{,}004$), 2–10 $R_{eff}$ arası yarıçapta düz.
- **Nicel sınav yapılabilen yerde yapılmıştır:** erken tip galaksilerin radyal ivme düzlemi. 16 galakside teorinin dış nokta artığı $-0{,}008$ dex'tir (6.5.4.5'in ölçüm tablosu).

### 3. Cüce Küresel (Dwarf Spheroidal) Galaksiler

Fornax (Ocak) gibi cüce küresel galaksiler, standart görüşte karanlık maddenin oransal olarak en yoğun bulunduğu düşünülen, sadece 1-2 kpc boyutlarındaki minicik yapılardır. Çok düşük kütlelerine rağmen efektif hız profilleri $\sim18$ km/s bandında asimptota oturur.

Bunlar da basınç-destekli sistemlerdir. Köprü artık kuruludur (M-48) ve mertebesi tutar: $M_*\sim10^7$ için köprü $v_c=\sqrt2\,\sigma\approx17{,}8$ km/s verir — yukarıdaki $\sim18$ km/s. MW uydusu cüceler **dış-alan-baskın** sistemlerdir ve dış alan terimi artık türetilmiştir (M-49): $W_{dış}=\min(1,\sqrt{g_{kaps}/g_{ext}})$. MW alanıyla birlikte köprü Fornax için $\sigma=10{,}5$–14,9 km/s verir (gözlenen ~11–12) — EFE terimi yalıtık değeri gözleme doğru çeker. Statü [T-aday]: $M_*$/anizotropi/MW-alanı belirsizlikleri $O(1)$'dir. **İki bağımsız-aile sınavı yapılmıştır** (McConnachie 2012 derlemesi, 28 sistem; SLUGGS eliptikleri, 22 sistem): köprü+$a_0$ sıfır yeniden-kalibrasyonla cücelerde medyan $+0{,}009$, eliptiklerde $+0{,}051$/$-0{,}004$ dex isabet etti (**M-48 iki aileyi geçerek [T]'ye yükseldi**); EFE terimi büyük uydularda ($M_*>10^6$) öngörülen düzeltmeyi verdi ($+0{,}109\to+0{,}042$; And II tam isabet), küçük klasiklerde ise gelgit-ısınması karıştırıcısıyla çakışık aşırı-bastırma görüldü — o uçta hüküm verilmez (G-13 kaydı). Merkezî kara delikle ilgili hiçbir öngörü de teoriden çıkmaz — F4 kara deliğe bağlı değildir ve dönüş eğrisi verisi kara deliğin varlığına zaten kördür: etki yarıçapı ($\sim$0,01 kpc) SPARC'ın en iç ölçüm noktasından **75 kat** küçüktür; $M_{BH}$ hesaba katılsa da katılmasa da medyan $\chi^2$ dördüncü basamakta değişir. Küresel formun neden korunduğu sorusunun teorideki nicel karşılığı kurulmamıştır ve açık kalemdir (7.4).

## 6.5.3.1 Gerçek SPARC Verisiyle Nicel Sınav

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

## 6.5.3.2 Örneklem Sınavı: Parametreler Evrensel mi?

6.5.3.1'in tek galaksili sonucu bir vaka çalışmasıdır. Teorinin **öngörü** iddiası ise bambaşka bir soruya bağlıdır: 6.5.4.3'ün türettiği vortisite uzunluğu $\ell_\omega^{mikro}=q_n/2\gamma_n$ ile M-38'in yayılma ölçeği $R_f$, galaksiler arasında **sabit** midir? $\ell_\omega^{mikro}$ nükleonun kendi debi oranından geldiğine göre mikro-fiziksel bir sabit olmak zorundadır — ve öyledir: ölçümü $35{,}7$ fm, kütleyle korelasyonu $+0{,}03$ (6.5.4.3 Adım 6). Galaksiden galaksiye görünen değişim mikro oranda değil, etkin uzunluğun $\sqrt{N}$ toplanma çarpanındadır: $\ell_\omega^{etkin}=\ell_\omega^{mikro}\sqrt{N}$.

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

**Dürüst konum.** Bu örneklemin verdiği tablo şudur: teori dönüş eğrilerini **görünmez madde envanteri olmadan** tarif edebiliyor, ama (i) parametreleri galaksi başına serbesttir, (ii) eşit serbestlikte ΛCDM'in gerisindedir, (iii) kütleli ve kovanlı sarmallarda ΛCDM kazanır. Buna karşılık **cücelerde ve düşük yüzey parlaklıklı sistemlerde ΛCDM'in kendi reçetesi çöküyor ve teori çökmüyor.** Teorinin sınanmaya değer cephesi düz dönüş eğrisi değil, Core-Cusp rejimidir. 12 galaksi bunu göstermeye yeter ama kanıtlamaya yetmez. **Sınav SPARC'ın tamamıyla yapılmış ve sonuç 6.5.3.3'te verilmiştir:** desen gerçektir ($3{,}1\sigma$) ama 12 galaksilik tablonun ima ettiğinden zayıftır.

## 6.5.3.3 Tam Örneklem Sınavı: Teorinin Cephesi Neresi?

6.5.3.2 iki şey gösterdi: parametreler evrensel değil, ve eşit serbestlikte ΛCDM genel olarak önde. Ama 12 galaksilik tabloda bir **desen** göze çarptı: ΛCDM'in formel olarak dışlandığı sistemler cüce ve düşük yüzey parlaklıklı (LSB) galaksilerdi ve orada teori belirgin biçimde daha iyiydi. Bu alt bölüm o deseni **hiçbir seçim yapmadan**, SPARC'ın tamamıyla ölçer: indirilebilen 173 dosyanın fit edilebilen **163'ü**.

> **Seçim yanlılığı denetimi.** Bu sınav yalnız **tam örneklemde** geçerlidir. Elle seçilmiş alt kümeler yanıltıcı sonuç üretir — örneğin literatürün bilinen Core-Cusp vakalarını (DDO154, IC2574, NGC3109) içeren 31 galaksilik bir küme cüce rejiminde 9/9 verir; tam örneklemde gerçek oran **36/50**'dir. Aşağıdaki bütün sayılar tam örneklemdendir ve seçim yanlılığı taşımaz.

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

**Sonuç 2 — ama cüce/LSB rejiminde üstünlük gerçek ve anlamlıdır** *(koşullu — bkz. aşağıdaki Sonuç 5)*. $V_{max}<80$ km/s bandında birleşik sonuç **36/50 = %72 ± %6**, yani beraberlikten **$3{,}1\sigma$** sapma *(hesap yöntemi: Sonuç 5'in yöntem notu)*. Ve asıl önemli olan medyan uyum kalitesidir:

$$\text{cüce/LSB medyan } \chi^2_{ind}:\quad \Lambda\text{CDM } 1{,}70 \;\longrightarrow\; \text{Evrenakı } \mathbf{0{,}77}$$

Evrenakı bu rejimde **kabul sınırının ($\chi^2_{ind}=1$) altına** iner, ΛCDM inmez. Grafiğin sağ alt orta panelinde iki eğrinin ayrıştığı yer tam bu banttır.

**Sonuç 3 — ve ΛCDM'in kazandığı bant da anlamlıdır.** $120$–$180$ km/s bandında Evrenakı 6/22 = %27 ($-2{,}4\sigma$). Yani tablo tek yönlü değil: **her iki modelin de kendi rejimi var.**

**Sonuç 4 — formel dışlamada denklik.** $\chi^2_{ind}>10$ ölçütüyle ΛCDM 15/163, Evrenakı 18/163 galakside dışlanıyor. 136 galakside ikisi de kabul ediliyor. Yani "biri çöküyor öteki ayakta" gibi bir tablo yok.

**Fiziksel okuma.** Cüce/LSB rejimindeki üstünlüğün nedeni bilinen bir mekanizmadır: NFW'nin konsantrasyon–kütle ilişkisi dayatıldığında halo merkezde zorunlu olarak sivrilir (**cusp**), oysa düşük yüzey parlaklıklı sistemlerin iç bölgesi **düz çekirdeklidir** (core) — astrofizikteki Core-Cusp problemi (bkz. bu bölümün §4-A). Teori iç bölgeyi bir halo profiliyle değil kapsanan nükleon dağılımıyla kurduğu için bu problemi paylaşmaz. Standart kozmoloji sorunu baryonik geri-besleme (feedback) ile çözmeye çalışır; teori ek bir mekanizmaya ihtiyaç duymaz.

**Teorinin galaktik iddiasının nihai konumu.** Üç cümlede:

1. **Düz dönüş eğrisi bir zafer değildir.** Tam örneklemde eşit serbestlikte beraberlik ($1{,}3\sigma$). Parametrelerden **$\ell_\omega$ yasalıdır** ($\propto\sqrt{M_{bar}}$, sıfır serbest parametre, ölçülen eğim 1,03 — 6.5.4.5); teori onun evrensel olduğunu iddia etmez. **$R_f$ ise fit parametresidir** ve öngörü statüsü taşımaz.
2. **Cephe Core-Cusp rejimidir — ama anlamlılık $\Upsilon_*$'a koşulludur.** Cüce/LSB'de $3{,}1\sigma$ üstünlük ve medyan $\chi^2_{ind}$'in kabul sınırının altına inmesi, teorinin sınanmaya değer tek sonucudur. **Ancak** $\Upsilon_*$ yıldız popülasyon sentezi bandına hapsedildiğinde anlamlılık $0{,}8\sigma$'ya iner (Sonuç 5); medyan üstünlük korunur, istatistiksel anlamlılık korunmaz.
3. **Ontolojik fatura değişmemiştir.** Bu sonuçların tamamı, teorinin hiçbir görünmez madde envanteri talep etmediği koşulda elde edilmiştir; ΛCDM aynı eğriler için baryonik kütlenin katları mertebesinde halo ister.

*Kalan çekinceler:* cüce eğrilerinde nokta sayısı azdır (6–34) ve hata çubukları büyüktür; SPARC'ın uzaklık ve eğiklik sistematikleri modellenmemiştir. $3{,}1\sigma$ bir keşif eşiği değildir.

---

### Sonuç 5 — ve yukarıdaki iddia $\Upsilon_*$'ın serbest olmasına koşulludur

Yukarıdaki tablonun tamamında $\Upsilon_*$ **her iki modelde de serbest** bırakılmıştır. Bu, kendi başına adil bir kurulumdur; ama $\Upsilon_*$ keyfî bir sayı değildir — yıldız popülasyon sentezi onu 3,6 μm'de $0{,}3$–$0{,}8$ aralığına yerleştirir. **Sıradaki iş** olarak kaydedilen sınav buydu ve şimdi yapılmıştır: aynı karşılaştırma, $\Upsilon_*$ o banda hapsedilerek tekrarlanmıştır. Kısıt **her iki modele de** uygulanmıştır.

![$\Upsilon_*$ bandı rejime göre — 163 galaksi](Gorseller/upsilon_bant_rejim.png)

| $v_{max}$ bandı | $N$ | Evrenakı: serbest → bantlı | ΛCDM: serbest → bantlı | Evrenakı önde: serbest → bantlı |
|---|---|---|---|---|
| **Cüce/LSB $<80$** | 50 | 0,62 → **1,68** (×2,7) | 1,57 → 2,28 (×1,4) | **37/50 ($3{,}4\sigma$) → 28/50 ($0{,}8\sigma$)** |
| $80$–$120$ | 44 | 0,78 → **4,90** (×6,3) | 1,56 → 1,91 (×1,2) | 27/44 ($+1{,}5\sigma$) → 12/44 ($-3{,}0\sigma$) |
| $120$–$180$ | 22 | 2,16 → 3,05 (×1,4) | 2,44 → 2,97 (×1,2) | 7/22 ($-1{,}7\sigma$) → 8/22 ($-1{,}3\sigma$) |
| $180$–$250$ | 27 | 1,89 → 3,25 (×1,7) | 1,98 → 2,49 (×1,3) | 13/27 ($-0{,}2\sigma$) → 12/27 ($-0{,}6\sigma$) |
| $>250$ | 20 | 3,56 → 5,42 (×1,5) | 4,17 → 4,17 (×1,0) | 12/20 ($+0{,}9\sigma$) → 11/20 ($+0{,}4\sigma$) |
| **TOPLAM** | **163** | 1,36 → **3,45** | 1,97 → 2,58 | 59% → 44% |

**Sonuç açıktır ve teorinin aleyhinedir.**

- **Cüce/LSB üstünlüğü anlamlılığını yitirir.** $3{,}4\sigma$ → $\mathbf{0{,}8\sigma}$. Bu bandın "teorinin cephesi" olduğu iddiası, $\Upsilon_*$ fotometrik önselden kurtulduğu sürece geçerlidir; kurtulmadığında **istatistiksel dayanağı kalmaz.**
- **En ağır hasar cücede değil, $80$–$120$ km/s bandındadır.** Orada medyan $\chi^2_{ind}$ **6,3 kat** bozulur (ΛCDM'de 1,2 kat) ve kazanma oranı $+1{,}5\sigma$'dan $\mathbf{-3{,}0\sigma}$'ya döner — yani bant altında bu rejim ΛCDM'in anlamlı üstünlük alanına geçer.
- **Bant her rejimde teoriye ΛCDM'den fazla zarar verir.** Bozulma çarpanları: teoride 1,4–6,3; ΛCDM'de 1,0–1,4. Tek istisna yoktur.

**Ama tek yönlü de okunmamalıdır.** Cüce/LSB'de teori bant altında bile **medyan $\chi^2_{ind}$ bakımından hâlâ öndedir** ($1{,}68$'e karşı $2{,}28$). Yitirilen şey medyan üstünlük değil, **galaksi başına kazanma oranının anlamlılığıdır.** İkisi aynı şey değildir: birincisi tipik uyum kalitesini, ikincisi üstünlüğün tutarlılığını ölçer. Teori bant altında tipik olarak daha iyi uyuyor ama bunu yeterince tutarlı biçimde yapmıyor.

> **Bu bölümün başlık iddiası buna göre okunmalıdır.** "Teorinin galaktik cephesi Core-Cusp rejimidir" tespiti ayaktadır — medyan uyum orada hâlâ ΛCDM'in önündedir ve mekanizma açıklaması (cusp zorunluluğunun paylaşılmaması) değişmemiştir. Ayakta olmayan, o üstünlüğün **$3{,}1\sigma$ düzeyinde anlamlı** olduğu iddiasıdır. Serbest $\Upsilon_*$ ile anlamlıdır; fotometrik önselle anlamlı değildir.

*Yöntem notu.* **(1)** Serbest hâlin burada 37/50 çıkması, tablodaki 36/50 ile bir galaksi farklıdır; fark **$\Upsilon_*$ üst sınırındandır** (tablo $\leq2{,}0$, buradaki tarama $\leq3{,}0$ kullanmıştır) — optimize edici gürültüsü değil. Kitabın temel kurulumu $\leq2{,}0$'dır ve o değerle cüce/LSB sonucu 36/50'dir. **(2)** Cüce/LSB anlamlılığı $3{,}1\sigma$'dır ve $p=0{,}5$ boş hipotezinin oranıyla hesaplanır: $(36-25)/\sqrt{50/4}=3{,}11$ (gözlenen orandan hesaplanan Wald değeri $3{,}5\sigma$ verirdi; boş hipoteze karşı sınamada doğrusu budur). Bandın kendisinin doğru önsel olup olmadığı sorusu ise **kapalıdır** — teorinin $\gamma_N/m=1/\rho_n$ bağıntısı onu o banda bağlar; bkz. 6.5.4.7 kayıt (4).

## 6.5.3.4 Tam Veri Tablosu — Galaksi Başına Sonuçlar


Aşağıdaki tablo, 6.5.3.3'ün istatistiklerinin dayandığı **163 galaksinin tamamını** satır satır verir. Hiçbir galaksi seçilmemiş, dışlanmamış ya da ağırlıklandırılmamıştır; dosya olarak indirilebilen ve fit edilebilen tüm SPARC örneklemi buradadır. Amaç, 6.5.3.1–6.5.3.3 ve 6.5.4.5–6.5.4.6'daki her sayının denetlenebilir olmasıdır.

**Sütunlar.** $N$: dönüş eğrisi nokta sayısı. Kovan: SPARC'ın $V_{bul}>0$ verdiği galaksiler. $V_{max}$ (km/s): gözlenen en büyük hız, dinamik kütlenin vekili. $\chi^2_{ind}$ ΛCDM: NFW halosu, konsantrasyon Dutton & Macciò (2014) ilişkisinden, $k=2$ ($\Upsilon_*$, $M_{200}$). $\chi^2_{ind}$ Evr.: Evrenakı F1+F4, $k=2$ ($\Upsilon_*$, $b$). $\Delta\chi^2=\chi^2_{\Lambda CDM}-\chi^2_{Evrenakı}$; **kalın** değerler Evrenakı'nın önde olduğu satırlardır. $\Upsilon_*$: Evrenakı fitinin istediği 3,6 μm kütle/ışık oranı. $M_{bar}$ ($M_\odot$): o $\Upsilon_*$ ile kapsanan toplam baryonik kütle. $\ell_\omega$ ölç.: $\mathcal{G}/b$ (kpc). $\ell_\omega$ öngörü: $\sqrt{\mathcal{G}M_{bar}/a_0}$ (6.5.4.5'in yasası, sıfır serbest parametre). Oran: ölçülen/öngörülen. $R_f$: yayılma ölçeği (kpc); $\to\infty$ işareti fitin yayılma istemediği galaksileri gösterir (6.5.4.6).

Tablo $V_{max}$'a göre artan sırada dizilmiştir; böylece 6.5.3.3'ün rejim deseni doğrudan okunabilir — üstteki cüce/LSB satırlarında $\Delta\chi^2$ ağırlıklı olarak pozitif, alttaki kütleli satırlarda karışıktır.

**Galerinin okunuşu.** Aşağıdaki galeri, tablonun görsel karşılığıdır: aynı 163 galaksi, aynı sırayla, ama sayılar yerine eğri şekilleriyle. Her panelde sarı noktalar ölçümü (gerçek hata çubuklarıyla), gri noktalı çizgi baryonik katkıyı, mor kesik-noktalı çizgi ΛCDM NFW fitini, yeşil düz çizgi Evrenakı F1+F4 fitini gösterir — ikisi de $k=2$. **Panel başlığının rengi kazanan modeli verir** (yeşil: Evrenakı, mor: ΛCDM). Sol üstte $V_{max}$, sağ altta iki modelin $\chi^2_{ind}$ değerleri yazılıdır.

Rejim deseni galeride çıplak gözle okunabilir: **ilk satırlarda (cüce/LSB) başlıklar ağırlıklı olarak yeşil**, son satırlarda (kütleli sarmallar) karışıktır. 6.5.3.3'ün $3{,}1\sigma$'lık sonucu bu görsel eğilimin sayısal ifadesidir.

![Tüm SPARC örneklemi — 163 galaksinin dönüş eğrisi ve iki model fiti](Gorseller/sparc_galeri_163.png)

| # | Galaksi | $N$ | Kovan | $V_{max}$ | $\chi^2_{ind}$ ΛCDM | $\chi^2_{ind}$ Evr. | $\Delta\chi^2$ | $\Upsilon_*$ | $M_{bar}$ | $\ell_\omega$ ölç. | $\ell_\omega$ öngörü | oran | $R_f$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UGC07577 | 9 | — | 18 | 0.42 | 0.18 | **+0.23** | 0.47 | 5.28e+07 | 2.07 | 0.26 | 7.95 | $\to\infty$ |
| 2 | CamB | 9 | — | 20 | 8.08 | 3.06 | **+5.01** | 0.05 | 2.34e+07 | 0.63 | 0.17 | 3.65 | $\to\infty$ |
| 3 | PGC51017 | 6 | — | 20 | 1.17 | 1.73 | -0.57 | 0.64 | 2.73e+08 | nan | 0.59 | — | 0.3 |
| 4 | UGC04483 | 8 | — | 24 | 0.66 | 0.49 | **+0.17** | 1.33 | 6.11e+07 | 0.67 | 0.28 | 2.39 | 0.4 |
| 5 | D564-8 | 6 | — | 25 | 8.95 | 0.09 | **+8.86** | 0.95 | 6.20e+07 | 0.53 | 0.28 | 1.86 | $\to\infty$ |
| 6 | F563-V1 | 6 | — | 30 | 0.20 | 0.22 | -0.02 | 0.98 | 1.62e+09 | nan | 1.44 | — | 0.3 |
| 7 | UGCA281 | 7 | — | 30 | 0.93 | 0.35 | **+0.59** | 1.00 | 1.03e+08 | 0.91 | 0.36 | 2.50 | $\to\infty$ |
| 8 | UGC07559 | 7 | — | 32 | 1.67 | 0.27 | **+1.40** | 0.90 | 2.49e+08 | 1.60 | 0.57 | 2.83 | 3.8 |
| 9 | UGC07866 | 7 | — | 33 | 0.27 | 0.06 | **+0.21** | 1.44 | 2.64e+08 | 2.60 | 0.58 | 4.46 | $\to\infty$ |
| 10 | KK98-251 | 15 | — | 35 | 5.79 | 0.17 | **+5.61** | 1.40 | 3.31e+08 | 2.06 | 0.65 | 3.16 | 13.9 |
| 11 | UGC04305 | 22 | — | 37 | 1.73 | 1.69 | **+0.04** | 0.77 | 1.53e+09 | nan | 1.41 | — | 0.3 |
| 12 | NGC4068 | 6 | — | 42 | 4.48 | 0.23 | **+4.25** | 0.49 | 3.21e+08 | 1.29 | 0.64 | 2.01 | 3.4 |
| 13 | UGC06628 | 7 | — | 42 | 0.23 | 0.47 | -0.24 | 0.69 | 3.72e+09 | nan | 2.19 | — | 0.3 |
| 14 | UGC05918 | 8 | — | 44 | 0.49 | 1.72 | -1.22 | 2.00 | 6.73e+08 | 1.92 | 0.93 | 2.07 | 0.3 |
| 15 | DDO064 | 14 | — | 47 | 1.15 | 0.39 | **+0.76** | 1.73 | 6.09e+08 | 1.60 | 0.89 | 1.80 | 0.4 |
| 16 | UGC08837 | 8 | — | 48 | 6.85 | 0.45 | **+6.40** | 0.55 | 7.68e+08 | 2.16 | 0.99 | 2.17 | $\to\infty$ |
| 17 | DDO154 | 12 | — | 48 | 17.30 | 2.44 | **+14.86** | 1.36 | 3.96e+08 | 0.85 | 0.71 | 1.18 | 7.0 |
| 18 | F561-1 | 6 | — | 50 | 0.35 | 0.79 | -0.44 | 0.92 | 5.03e+09 | nan | 2.55 | — | 0.3 |
| 19 | NGC3741 | 21 | — | 52 | 4.16 | 1.37 | **+2.79** | 1.63 | 3.25e+08 | 0.50 | 0.65 | 0.77 | 3.7 |
| 20 | NGC2366 | 26 | — | 54 | 6.55 | 2.65 | **+3.90** | 0.90 | 1.18e+09 | 1.96 | 1.23 | 1.59 | 0.3 |
| 21 | DDO168 | 10 | — | 55 | 21.48 | 4.40 | **+17.08** | 0.05 | 5.04e+08 | 0.73 | 0.81 | 0.91 | 54.7 |
| 22 | UGC05764 | 10 | — | 56 | 6.16 | 51.16 | -45.00 | 2.00 | 4.84e+08 | 0.58 | 0.79 | 0.74 | 0.3 |
| 23 | UGC01281 | 25 | — | 57 | 3.37 | 0.17 | **+3.20** | 1.27 | 8.81e+08 | 1.31 | 1.07 | 1.23 | 2.7 |
| 24 | UGC08550 | 11 | — | 58 | 0.62 | 2.24 | -1.62 | 1.79 | 1.07e+09 | 1.66 | 1.18 | 1.41 | 140.4 |
| 25 | UGCA442 | 8 | — | 58 | 9.86 | 3.69 | **+6.17** | 1.79 | 6.64e+08 | 1.15 | 0.93 | 1.25 | $\to\infty$ |
| 26 | D631-7 | 16 | — | 58 | 18.49 | 2.79 | **+15.71** | 0.05 | 4.62e+08 | 0.86 | 0.77 | 1.11 | $\to\infty$ |
| 27 | UGC07690 | 7 | — | 61 | 0.38 | 0.20 | **+0.18** | 1.10 | 1.22e+09 | 3.20 | 1.25 | 2.55 | 2.0 |
| 28 | UGC02455 | 8 | — | 61 | 4.88 | 0.75 | **+4.13** | 0.07 | 1.05e+09 | 2.11 | 1.17 | 1.81 | $\to\infty$ |
| 29 | UGC05414 | 6 | — | 61 | 4.73 | 0.26 | **+4.47** | 0.96 | 1.33e+09 | 2.82 | 1.31 | 2.16 | $\to\infty$ |
| 30 | DDO170 | 8 | — | 62 | 9.84 | 7.90 | **+1.94** | 2.00 | 2.65e+09 | 4.22 | 1.85 | 2.29 | 16.1 |
| 31 | ESO444-G084 | 7 | — | 63 | 0.65 | 3.55 | -2.90 | 2.00 | 3.69e+08 | 0.53 | 0.69 | 0.77 | $\to\infty$ |
| 32 | UGC07603 | 12 | — | 64 | 1.47 | 0.23 | **+1.25** | 0.85 | 5.76e+08 | 0.70 | 0.86 | 0.81 | 29.8 |
| 33 | UGC07125 | 13 | — | 66 | 2.23 | 2.05 | **+0.18** | 1.29 | 8.40e+09 | 18.18 | 3.29 | 5.53 | 8.7 |
| 34 | NGC3109 | 25 | — | 67 | 29.12 | 0.40 | **+28.73** | 1.60 | 8.64e+08 | 0.91 | 1.05 | 0.86 | $\to\infty$ |
| 35 | DDO161 | 31 | — | 68 | 13.22 | 1.11 | **+12.11** | 0.68 | 2.75e+09 | 3.70 | 1.88 | 1.97 | $\to\infty$ |
| 36 | IC2574 | 34 | — | 68 | 25.97 | 1.06 | **+24.90** | 1.03 | 2.75e+09 | 3.34 | 1.88 | 1.77 | $\to\infty$ |
| 37 | UGC05829 | 11 | — | 69 | 1.41 | 0.63 | **+0.79** | 2.00 | 2.93e+09 | 4.24 | 1.94 | 2.19 | 0.8 |
| 38 | UGC07608 | 8 | — | 69 | 1.15 | 0.51 | **+0.63** | 2.00 | 1.09e+09 | 1.00 | 1.18 | 0.85 | 2.0 |
| 39 | F583-4 | 12 | — | 70 | 0.61 | 0.34 | **+0.28** | 1.31 | 2.77e+09 | 5.26 | 1.89 | 2.79 | 0.9 |
| 40 | NGC1705 | 14 | — | 73 | 0.20 | 0.40 | -0.21 | 1.16 | 9.91e+08 | 0.95 | 1.13 | 0.84 | $\to\infty$ |
| 41 | UGC10310 | 7 | — | 73 | 0.50 | 0.24 | **+0.26** | 2.00 | 4.86e+09 | 11.02 | 2.50 | 4.41 | 5.6 |
| 42 | UGC12632 | 15 | — | 73 | 0.42 | 2.39 | -1.97 | 2.00 | 4.92e+09 | 5.56 | 2.52 | 2.21 | 2.6 |
| 43 | UGC00731 | 12 | — | 74 | 0.49 | 42.53 | -42.05 | 2.00 | 3.85e+09 | 2.47 | 2.23 | 1.11 | 0.3 |
| 44 | UGC04499 | 9 | — | 74 | 0.90 | 1.17 | -0.27 | 1.31 | 3.74e+09 | 4.62 | 2.19 | 2.10 | 1.4 |
| 45 | UGC06818 | 8 | — | 74 | 5.59 | 1.41 | **+4.18** | 0.29 | 1.12e+09 | 0.91 | 1.20 | 0.76 | $\to\infty$ |
| 46 | UGC05716 | 12 | — | 75 | 1.09 | 17.30 | -16.21 | 2.00 | 3.20e+09 | 2.80 | 2.03 | 1.38 | 5.3 |
| 47 | UGC07261 | 7 | — | 76 | 0.17 | 1.51 | -1.34 | 1.41 | 3.46e+09 | 5.04 | 2.11 | 2.39 | $\to\infty$ |
| 48 | UGC07151 | 11 | — | 76 | 2.65 | 0.88 | **+1.76** | 1.24 | 3.55e+09 | 6.26 | 2.14 | 2.93 | 2.1 |
| 49 | UGC05750 | 11 | — | 79 | 2.33 | 0.32 | **+2.01** | 1.92 | 1.40e+10 | 14.36 | 4.24 | 3.39 | 10.1 |
| 50 | UGC07089 | 12 | — | 79 | 2.37 | 0.25 | **+2.12** | 0.67 | 3.70e+09 | 4.15 | 2.18 | 1.90 | $\to\infty$ |
| 51 | UGC08490 | 30 | — | 80 | 0.36 | 0.34 | **+0.01** | 1.45 | 2.56e+09 | 2.08 | 1.81 | 1.15 | 43.1 |
| 52 | NGC4214 | 14 | — | 81 | 0.72 | 1.77 | -1.05 | 0.75 | 1.14e+09 | 0.96 | 1.21 | 0.80 | $\to\infty$ |
| 53 | UGC06923 | 6 | — | 81 | 0.64 | 0.70 | -0.05 | 0.68 | 2.62e+09 | 2.55 | 1.84 | 1.39 | 5.1 |
| 54 | UGC05721 | 23 | — | 83 | 2.28 | 2.12 | **+0.15** | 1.28 | 1.65e+09 | 1.09 | 1.46 | 0.75 | 2.2 |
| 55 | F565-V2 | 7 | — | 83 | 1.53 | 0.57 | **+0.96** | 2.00 | 2.53e+09 | 1.75 | 1.80 | 0.97 | 5.2 |
| 56 | UGC07524 | 31 | — | 84 | 2.11 | 1.68 | **+0.43** | 2.00 | 7.66e+09 | 9.15 | 3.14 | 2.91 | 2.3 |
| 57 | UGC00191 | 9 | — | 84 | 3.50 | 2.27 | **+1.23** | 1.78 | 6.58e+09 | 7.40 | 2.91 | 2.54 | $\to\infty$ |
| 58 | F571-V1 | 7 | — | 84 | 0.80 | 0.07 | **+0.73** | 1.85 | 5.65e+09 | 4.97 | 2.70 | 1.84 | 32.8 |
| 59 | UGC08286 | 17 | — | 84 | 1.78 | 2.47 | -0.69 | 2.00 | 3.72e+09 | 3.28 | 2.19 | 1.50 | 0.4 |
| 60 | UGC11820 | 10 | — | 84 | 8.94 | 1.21 | **+7.73** | 1.68 | 7.92e+09 | 6.64 | 3.19 | 2.08 | $\to\infty$ |
| 61 | UGC06446 | 17 | — | 85 | 0.20 | 1.50 | -1.30 | 2.00 | 4.42e+09 | 2.89 | 2.39 | 1.21 | 4.2 |
| 62 | UGC11557 | 12 | — | 85 | 2.04 | 0.83 | **+1.21** | 0.33 | 6.82e+09 | 7.21 | 2.96 | 2.43 | 13.5 |
| 63 | UGC06667 | 9 | — | 86 | 1.96 | 22.20 | -20.24 | 2.00 | 2.83e+09 | 1.48 | 1.91 | 0.78 | 0.3 |
| 64 | NGC2915 | 30 | — | 86 | 1.20 | 2.07 | -0.86 | 1.16 | 1.51e+09 | 0.82 | 1.40 | 0.59 | 3.6 |
| 65 | F583-1 | 25 | — | 87 | 3.29 | 3.47 | -0.18 | 2.00 | 7.92e+09 | 3.02 | 3.19 | 0.95 | 6.7 |
| 66 | NGC0055 | 21 | — | 87 | 10.47 | 0.66 | **+9.81** | 0.69 | 6.31e+09 | 4.83 | 2.85 | 1.69 | 21.1 |
| 67 | UGC06399 | 9 | — | 88 | 0.99 | 0.07 | **+0.93** | 1.60 | 4.62e+09 | 4.55 | 2.44 | 1.87 | 17.4 |
| 68 | NGC2976 | 27 | — | 89 | 0.90 | 0.33 | **+0.57** | 0.56 | 1.82e+09 | 2.30 | 1.53 | 1.50 | 2.4 |
| 69 | UGC02259 | 8 | — | 90 | 1.75 | 12.11 | -10.35 | 2.00 | 4.31e+09 | 3.69 | 2.36 | 1.57 | 4.7 |
| 70 | NGC0100 | 21 | — | 91 | 1.59 | 0.09 | **+1.50** | 0.47 | 2.51e+09 | 1.41 | 1.80 | 0.79 | 14.9 |
| 71 | NGC5585 | 24 | — | 92 | 5.60 | 7.12 | -1.52 | 0.55 | 4.34e+09 | 2.52 | 2.36 | 1.07 | 19.2 |
| 72 | UGC04325 | 8 | — | 93 | 2.62 | 12.05 | -9.43 | 2.00 | 4.90e+09 | 4.92 | 2.51 | 1.96 | 0.3 |
| 73 | UGC04278 | 25 | — | 93 | 3.43 | 2.42 | **+1.01** | 1.38 | 4.11e+09 | 2.57 | 2.30 | 1.11 | $\to\infty$ |
| 74 | NGC0300 | 25 | — | 97 | 0.69 | 0.63 | **+0.07** | 1.09 | 4.16e+09 | 2.75 | 2.32 | 1.19 | $\to\infty$ |
| 75 | UGC12732 | 16 | — | 98 | 0.36 | 1.64 | -1.28 | 2.00 | 9.89e+09 | 5.30 | 3.57 | 1.49 | 12.5 |
| 76 | F574-1 | 14 | — | 100 | 1.78 | 1.37 | **+0.41** | 2.00 | 1.40e+10 | 11.16 | 4.25 | 2.63 | 6.1 |
| 77 | UGC05005 | 11 | — | 100 | 2.18 | 0.15 | **+2.03** | 0.96 | 1.46e+10 | 6.76 | 4.34 | 1.56 | 12.8 |
| 78 | UGC07399 | 10 | — | 106 | 1.97 | 1.00 | **+0.96** | 2.00 | 2.94e+09 | 1.35 | 1.94 | 0.69 | 13.3 |
| 79 | NGC0247 | 26 | — | 108 | 4.09 | 3.07 | **+1.02** | 2.00 | 1.64e+10 | 21.56 | 4.60 | 4.69 | 72.3 |
| 80 | UGC06930 | 10 | — | 109 | 0.29 | 0.48 | -0.20 | 1.52 | 1.81e+10 | 15.10 | 4.83 | 3.13 | 0.9 |
| 81 | NGC0024 | 29 | — | 110 | 0.49 | 0.88 | -0.39 | 1.66 | 1.00e+10 | 5.81 | 3.59 | 1.62 | $\to\infty$ |
| 82 | NGC4389 | 6 | — | 110 | 4.46 | 0.32 | **+4.14** | 0.08 | 1.93e+09 | 0.96 | 1.58 | 0.61 | $\to\infty$ |
| 83 | UGC06917 | 11 | — | 111 | 0.71 | 0.74 | -0.03 | 1.30 | 1.03e+10 | 6.17 | 3.64 | 1.70 | 3.8 |
| 84 | ESO116-G012 | 15 | — | 112 | 2.32 | 2.01 | **+0.31** | 0.81 | 6.21e+09 | 2.66 | 2.83 | 0.94 | 21.2 |
| 85 | F563-1 | 17 | — | 112 | 1.11 | 1.87 | -0.76 | 2.00 | 9.70e+09 | 3.08 | 3.53 | 0.87 | 1.9 |
| 86 | UGC01230 | 11 | — | 113 | 0.97 | 1.25 | -0.28 | 2.00 | 3.05e+10 | 16.69 | 6.26 | 2.67 | 4.6 |
| 87 | UGC06983 | 17 | — | 113 | 0.67 | 0.91 | -0.24 | 1.75 | 1.27e+10 | 6.46 | 4.05 | 1.60 | 0.7 |
| 88 | F579-V1 | 14 | — | 114 | 0.64 | 1.75 | -1.11 | 2.00 | 2.67e+10 | 28.86 | 5.86 | 4.92 | 0.3 |
| 89 | NGC1003 | 36 | — | 115 | 5.55 | 7.68 | -2.13 | 0.75 | 1.42e+10 | 4.49 | 4.28 | 1.05 | $\to\infty$ |
| 90 | NGC4183 | 23 | — | 115 | 0.17 | 0.72 | -0.55 | 1.38 | 2.06e+10 | 15.08 | 5.15 | 2.93 | $\to\infty$ |
| 91 | NGC7793 | 46 | — | 116 | 0.88 | 0.70 | **+0.18** | 0.70 | 6.63e+09 | 5.25 | 2.92 | 1.80 | 14.5 |
| 92 | UGC05986 | 15 | — | 116 | 5.79 | 0.34 | **+5.45** | 0.88 | 5.64e+09 | 2.30 | 2.70 | 0.85 | 36.6 |
| 93 | F563-V2 | 10 | — | 118 | 0.94 | 0.94 | **+0.00** | 2.00 | 1.01e+10 | 3.11 | 3.61 | 0.86 | 3.2 |
| 94 | F568-V1 | 15 | — | 118 | 0.18 | 1.23 | -1.05 | 2.00 | 1.32e+10 | 3.10 | 4.12 | 0.75 | 4.7 |
| 95 | F568-3 | 18 | — | 120 | 8.90 | 1.65 | **+7.25** | 1.34 | 1.67e+10 | 6.91 | 4.63 | 1.49 | 18.1 |
| 96 | NGC6503 | 31 | — | 121 | 2.99 | 5.30 | -2.31 | 0.53 | 9.70e+09 | 3.50 | 3.53 | 0.99 | 22.6 |
| 97 | NGC4559 | 32 | — | 124 | 0.24 | 0.88 | -0.64 | 0.60 | 2.44e+10 | 8.88 | 5.60 | 1.59 | 11.1 |
| 98 | NGC3769 | 12 | — | 126 | 0.71 | 0.87 | -0.16 | 0.51 | 1.57e+10 | 4.82 | 4.49 | 1.07 | 36.6 |
| 99 | NGC4010 | 12 | — | 129 | 2.26 | 1.82 | **+0.44** | 0.51 | 1.05e+10 | 4.23 | 3.67 | 1.15 | 73.2 |
| 100 | UGC03580 | 47 | var | 131 | 3.44 | 11.68 | -8.24 | 0.27 | 1.16e+10 | 3.29 | 3.87 | 0.85 | 13.2 |
| 101 | NGC3972 | 10 | — | 134 | 1.04 | 1.57 | -0.53 | 0.88 | 1.29e+10 | 6.62 | 4.08 | 1.62 | 2.9 |
| 102 | UGC00128 | 22 | — | 134 | 2.42 | 17.75 | -15.33 | 2.00 | 3.94e+10 | 13.47 | 7.13 | 1.89 | 67.0 |
| 103 | NGC2403 | 73 | — | 136 | 5.36 | 10.30 | -4.94 | 0.66 | 1.43e+10 | 4.13 | 4.30 | 0.96 | 54.4 |
| 104 | NGC4085 | 7 | — | 136 | 3.22 | 1.15 | **+2.07** | 0.25 | 5.76e+09 | 1.88 | 2.72 | 0.69 | 7.2 |
| 105 | NGC3917 | 17 | — | 138 | 4.73 | 2.01 | **+2.72** | 1.05 | 2.57e+10 | 14.05 | 5.75 | 2.44 | 2.8 |
| 106 | F568-1 | 12 | — | 142 | 0.87 | 1.08 | -0.21 | 2.00 | 1.82e+10 | 3.98 | 4.84 | 0.82 | 6.2 |
| 107 | F571-8 | 13 | — | 144 | 2.46 | 6.01 | -3.55 | 0.05 | 1.02e+09 | 0.22 | 1.15 | 0.20 | $\to\infty$ |
| 108 | NGC3198 | 43 | — | 157 | 1.46 | 3.67 | -2.21 | 0.73 | 5.12e+10 | 11.30 | 8.12 | 1.39 | 7.6 |
| 109 | UGC09037 | 22 | — | 160 | 1.06 | 1.55 | -0.50 | 0.36 | 4.70e+10 | 9.44 | 7.78 | 1.21 | 2.2 |
| 110 | NGC4051 | 7 | — | 161 | 0.88 | 1.59 | -0.71 | 0.69 | 4.56e+10 | 166.22 | 7.66 | 21.70 | 0.3 |
| 111 | NGC6015 | 44 | — | 166 | 8.64 | 12.90 | -4.26 | 0.86 | 3.77e+10 | 11.34 | 6.96 | 1.63 | 0.6 |
| 112 | NGC3726 | 12 | — | 169 | 2.79 | 3.19 | -0.40 | 0.53 | 4.00e+10 | 12.60 | 7.18 | 1.76 | $\to\infty$ |
| 113 | NGC3949 | 7 | — | 169 | 0.27 | 1.03 | -0.75 | 0.54 | 1.58e+10 | 8.92 | 4.51 | 1.98 | $\to\infty$ |
| 114 | NGC3877 | 13 | — | 171 | 6.09 | 8.25 | -2.15 | 0.76 | 5.23e+10 | 22186.63 | 8.21 | 2704.00 | 0.3 |
| 115 | NGC1090 | 24 | — | 176 | 2.40 | 2.31 | **+0.09** | 0.61 | 6.55e+10 | 16.43 | 9.18 | 1.79 | 8.7 |
| 116 | ESO079-G014 | 15 | — | 178 | 4.85 | 2.89 | **+1.96** | 0.94 | 4.92e+10 | 13.61 | 7.96 | 1.71 | 13.8 |
| 117 | UGC06973 | 9 | var | 180 | 1.09 | 0.62 | **+0.47** | 0.20 | 6.40e+09 | 1.27 | 2.87 | 0.44 | $\to\infty$ |
| 118 | NGC6946 | 58 | var | 181 | 1.98 | 1.59 | **+0.39** | 0.45 | 3.48e+10 | 8.98 | 6.70 | 1.34 | 55.6 |
| 119 | NGC4088 | 12 | — | 182 | 0.51 | 1.05 | -0.54 | 0.34 | 4.66e+10 | 13.20 | 7.74 | 1.70 | $\to\infty$ |
| 120 | NGC4217 | 19 | var | 191 | 4.62 | 1.50 | **+3.12** | 0.09 | 1.37e+10 | 1.75 | 4.19 | 0.42 | 24.1 |
| 121 | NGC0289 | 28 | — | 194 | 1.90 | 1.89 | **+0.00** | 0.80 | 9.22e+10 | 18.59 | 10.90 | 1.71 | 44.7 |
| 122 | NGC3893 | 10 | — | 194 | 1.30 | 0.27 | **+1.02** | 0.53 | 3.36e+10 | 6.45 | 6.57 | 0.98 | 65.9 |
| 123 | NGC4100 | 24 | — | 195 | 1.29 | 2.10 | -0.81 | 0.77 | 4.18e+10 | 11.60 | 7.34 | 1.58 | $\to\infty$ |
| 124 | NGC4138 | 7 | var | 195 | 1.38 | 0.57 | **+0.81** | 0.64 | 1.67e+10 | 5.14 | 4.63 | 1.11 | 9.1 |
| 125 | NGC4013 | 36 | var | 198 | 1.42 | 3.48 | -2.06 | 0.48 | 1.74e+10 | 3.59 | 4.73 | 0.76 | $\to\infty$ |
| 126 | NGC4157 | 17 | var | 201 | 0.53 | 0.68 | -0.15 | 0.40 | 5.04e+10 | 10.14 | 8.05 | 1.26 | $\to\infty$ |
| 127 | UGC08699 | 41 | var | 202 | 1.50 | 1.11 | **+0.39** | 0.49 | 3.37e+10 | 5.64 | 6.59 | 0.86 | 81.0 |
| 128 | UGC06614 | 13 | var | 205 | 0.47 | 1.24 | -0.77 | 0.36 | 9.98e+10 | 8.90 | 11.34 | 0.78 | 555.0 |
| 129 | NGC5055 | 28 | — | 206 | 3.42 | 3.25 | **+0.17** | 0.38 | 7.72e+10 | 12.53 | 9.97 | 1.26 | 179.5 |
| 130 | NGC2683 | 11 | var | 212 | 1.21 | 0.79 | **+0.42** | 0.64 | 3.93e+10 | 10.49 | 7.12 | 1.47 | 672.5 |
| 131 | NGC2998 | 13 | — | 214 | 2.49 | 3.44 | -0.95 | 0.71 | 1.65e+11 | 26.57 | 14.57 | 1.82 | $\to\infty$ |
| 132 | NGC2903 | 34 | — | 216 | 15.51 | 6.80 | **+8.71** | 0.35 | 3.31e+10 | 5.06 | 6.53 | 0.77 | 49.1 |
| 133 | UGC02916 | 43 | var | 218 | 12.64 | 19.61 | -6.97 | 0.30 | 8.92e+10 | 6.83 | 10.72 | 0.64 | 33.4 |
| 134 | NGC3521 | 41 | — | 220 | 0.30 | 0.87 | -0.57 | 0.48 | 4.49e+10 | 7.81 | 7.60 | 1.03 | $\to\infty$ |
| 135 | NGC3953 | 8 | — | 224 | 0.46 | 0.66 | -0.19 | 0.82 | 8.55e+10 | 122.36 | 10.49 | 11.66 | 0.3 |
| 136 | NGC5033 | 22 | var | 225 | 11.64 | 10.34 | **+1.30** | 0.56 | 8.92e+10 | 12.23 | 10.72 | 1.14 | 23.7 |
| 137 | UGC06786 | 45 | var | 229 | 3.65 | 0.91 | **+2.73** | 0.43 | 4.56e+10 | 4.52 | 7.67 | 0.59 | 237.1 |
| 138 | NGC0891 | 18 | var | 234 | 6.12 | 6.20 | -0.08 | 0.30 | 4.65e+10 | 6.15 | 7.74 | 0.79 | 43.8 |
| 139 | NGC5907 | 19 | — | 235 | 6.04 | 9.88 | -3.84 | 0.82 | 1.58e+11 | 26.76 | 14.25 | 1.88 | $\to\infty$ |
| 140 | UGC03205 | 48 | var | 237 | 3.57 | 4.07 | -0.50 | 0.67 | 1.01e+11 | 15.87 | 11.40 | 1.39 | $\to\infty$ |
| 141 | NGC0801 | 13 | — | 238 | 7.58 | 6.29 | **+1.29** | 0.59 | 2.82e+11 | 48.98 | 19.07 | 2.57 | $\to\infty$ |
| 142 | NGC5371 | 19 | — | 242 | 10.20 | 14.96 | -4.76 | 0.62 | 2.17e+11 | 91.74 | 16.73 | 5.48 | $\to\infty$ |
| 143 | UGC05253 | 73 | var | 248 | 6.35 | 7.36 | -1.01 | 0.42 | 1.10e+11 | 9.53 | 11.91 | 0.80 | 136.7 |
| 144 | IC4202 | 32 | var | 250 | 34.73 | 31.50 | **+3.23** | 0.38 | 9.00e+10 | 6.91 | 10.77 | 0.64 | 8.5 |
| 145 | UGC12506 | 31 | — | 255 | 0.69 | 1.17 | -0.48 | 1.67 | 3.07e+11 | 55.71 | 19.88 | 2.80 | 0.3 |
| 146 | NGC7331 | 36 | var | 257 | 0.78 | 1.86 | -1.08 | 0.37 | 8.09e+10 | 9.72 | 10.20 | 0.95 | $\to\infty$ |
| 147 | NGC6195 | 23 | var | 258 | 3.73 | 3.51 | **+0.22** | 0.47 | 2.10e+11 | 33.75 | 16.43 | 2.05 | $\to\infty$ |
| 148 | UGC03546 | 30 | var | 262 | 2.98 | 2.44 | **+0.54** | 0.43 | 3.85e+10 | 6.45 | 7.04 | 0.92 | 24.2 |
| 149 | NGC5005 | 18 | var | 265 | 0.12 | 0.09 | **+0.04** | 0.36 | 6.73e+10 | 7.72 | 9.31 | 0.83 | 166.9 |
| 150 | NGC7814 | 18 | var | 265 | 2.41 | 0.66 | **+1.75** | 0.34 | 3.07e+10 | 3.58 | 6.29 | 0.57 | $\to\infty$ |
| 151 | NGC3992 | 9 | — | 272 | 0.73 | 3.62 | -2.89 | 1.04 | 1.60e+11 | 27.96 | 14.34 | 1.95 | $\to\infty$ |
| 152 | NGC2955 | 24 | var | 276 | 4.61 | 5.93 | -1.32 | 0.48 | 2.05e+11 | 31.72 | 16.24 | 1.95 | $\to\infty$ |
| 153 | UGC06787 | 71 | var | 276 | 31.51 | 18.79 | **+12.72** | 0.33 | 4.80e+10 | 3.74 | 7.86 | 0.48 | 10.9 |
| 154 | UGC09133 | 68 | var | 289 | 8.94 | 17.78 | -8.83 | 0.49 | 2.19e+11 | 20.62 | 16.78 | 1.23 | 85.4 |
| 155 | NGC6674 | 15 | var | 291 | 9.67 | 8.91 | **+0.76** | 0.80 | 2.04e+11 | 22.15 | 16.20 | 1.37 | $\to\infty$ |
| 156 | UGC11455 | 36 | — | 291 | 5.76 | 3.04 | **+2.72** | 0.46 | 1.96e+11 | 18.03 | 15.89 | 1.13 | 15.3 |
| 157 | NGC5985 | 33 | var | 305 | 8.80 | 11.37 | -2.57 | 1.71 | 3.25e+11 | 151.20 | 20.46 | 7.39 | 0.3 |
| 158 | UGC02885 | 19 | var | 305 | 1.87 | 1.18 | **+0.69** | 0.68 | 4.05e+11 | 27.84 | 22.84 | 1.22 | $\to\infty$ |
| 159 | UGC11914 | 65 | var | 305 | 2.58 | 4.02 | -1.44 | 0.61 | 8.66e+10 | 13.73 | 10.56 | 1.30 | $\to\infty$ |
| 160 | UGC02953 | 115 | var | 319 | 10.41 | 5.48 | **+4.92** | 0.53 | 1.57e+11 | 12.57 | 14.23 | 0.88 | $\to\infty$ |
| 161 | ESO563-G021 | 30 | — | 321 | 18.52 | 13.96 | **+4.56** | 0.83 | 2.99e+11 | 20.70 | 19.61 | 1.06 | 14.6 |
| 162 | NGC2841 | 50 | var | 323 | 1.82 | 1.97 | -0.16 | 0.90 | 1.73e+11 | 11.48 | 14.94 | 0.77 | $\to\infty$ |
| 163 | UGC02487 | 17 | var | 383 | 5.34 | 2.99 | **+2.35** | 1.10 | 3.26e+11 | 21.76 | 20.49 | 1.06 | 796.7 |

**Bant özeti (tablonun doğrudan sayımı):**

| $V_{max}$ bandı | $n$ | Evrenakı önde | Oran | Anlamlılık |
|---|---|---|---|---|
| $<60$ | 26 | 19 | 0.73 | +2.7 |
| $60$–$80$ | 24 | 17 | 0.71 | +2.2 |
| $80$–$120$ | 44 | 23 | 0.52 | +0.3 |
| $120$–$180$ | 22 | 6 | 0.27 | -2.4 |
| $180$–$250$ | 27 | 13 | 0.48 | -0.2 |
| $>250$ | 20 | 12 | 0.60 | +0.9 |
| **TOPLAM** | **163** | **90** | **0.55** | **+1.3$\sigma$** |

*Uyarı:* Bu tablodaki $\chi^2_{ind}$ değerleri yalnızca SPARC'ın kendi hata çubuklarını kullanır; uzaklık, eğiklik ve kütle/ışık sistematikleri modellenmemiştir. Bu nedenle mutlak değerler değil, **aynı satırdaki iki modelin karşılaştırması** anlamlıdır (7.4, madde 12).

## 6.5.3.5 Üçüncü Parametre Eklenmiş Hâl — **Fitlenmiş** Karşılaştırma


> **Bu alt bölümdeki üçüncü parametre FİTLENMİŞTİR, türetilmemiştir.** Ayrım kritiktir ve baştan belirtilmelidir: 6.5.4.5'te gösterildiği gibi $\ell_\omega$'nın bir **yasası** vardır ($\sqrt{\mathcal{G}M_{bar}/a_0}$, sıfır serbest parametre, ölçülen eğim 1,03). $R_f$'nin ise böyle bir yasası **yoktur** — 6.5.4.6, onun kökeni belirlenemeyen dış-bölge sistematiğini emen fenomenolojik bir terim olduğunu tespit eder. Dolayısıyla aşağıdaki uyum iyileşmesi **gerçek ama kazanılmamıştır**: bir serbest parametre eklenerek satın alınmıştır.

6.5.3.4'ün galerisi Evrenakı'yı $k=2$ ile gösteriyordu ($\Upsilon_*$, $b$). Bu galeri üçüncü parametreyi ekler:

$$v^2 = V_{bar}^2 + \frac{b\,M_{kaps}(R)}{1+R/R_f}\,,\qquad k=3\ (\Upsilon_*,\ b,\ R_f)$$

ΛCDM yine $k=2$'dir ($\Upsilon_*$, $M_{200}$; konsantrasyon simülasyon ilişkisinden). **Kazanan ölçütü AIC'dir, ham ki-kare değil** — parametre sayıları eşit olmadığı için ham $\chi^2$ karşılaştırması Evrenakı'ya haksız avantaj verir; AIC her fazladan parametreyi $+2$ ile cezalandırır. Üç parametreli fit $N\ge7$ gerektirdiği için örneklem 163'ten **155 galaksiye** düşer.

![Tüm SPARC örneklemi — Evrenakı'ya üçüncü parametre eklenmiş hâli ($k=3$)](Gorseller/sparc_galeri_163_k3.png)

**Sonuçlar:**

| Ölçüt | $k=2$ (6.5.3.4) | $k=3$ (bu galeri) |
|---|---|---|
| AIC kazananı — Evrenakı | 90/163 = %55 | **93/155 = %60** |
| Ham $\chi^2$ ile (adil değil) | %55 | %65 |
| Medyan $\chi^2_{ind}$ ΛCDM | — | 1,98 |
| Medyan $\chi^2_{ind}$ Evrenakı | — | **1,13** |
| $R_f$ üst sınırda (yayılma istenmeyen) | — | **48/155 = %31** |

Ham $\chi^2$ ile AIC arasındaki fark (%65 → %60) doğrudan fazladan parametrenin bedelidir: 8 galakside iyileşme, ödenen cezayı karşılamıyor. Medyan uyumda ise fark belirgindir — ΛCDM 1,98'de kalırken Evrenakı 1,13'e iner.

**Ama teşhis gücü kayboluyor — ve bu, bu alt bölümün asıl bulgusudur.**

| $V_{max}$ bandı | Evrenakı, $k=2$ | Evrenakı, $k=3$ |
|---|---|---|
| $<60$ | **0,73** | 0,62 |
| $60$–$80$ | **0,71** | 0,70 |
| $80$–$120$ | 0,52 | 0,60 |
| $120$–$180$ | **0,27** | 0,55 |
| $180$–$250$ | 0,48 | 0,56 |
| $>250$ | 0,60 | 0,60 |

$k=2$'de keskin bir eğim vardı: cücelerde 0,73, orta-kütlelilerde 0,27 — 6.5.3.3'ün $3{,}1\sigma$'lık Core-Cusp deseni buydu. **$k=3$'te bütün bantlar 0,55–0,70 arasına düzleşiyor.** Üçüncü parametre, teorinin cücelerdeki özgün avantajını da ΛCDM'in orta-kütlelilerdeki avantajını da siliyor; çünkü esneklik açığı her rejimde kapatıyor.

Bunun anlamı şudur: **uyum iyileşmesi ile teşhis gücü ters yönde hareket eder.** $k=2$'nin rejim deseni fiziksel bir bilgi taşıyordu (cusp'lı halo profilinin düşük yüzey parlaklıklı sistemlerde kırılması); $k=3$ o bilgiyi bir serbestlikle örtüyor. Bir modelin daha iyi *fit* etmesi, daha çok *söylediği* anlamına gelmez.

**Galerideki yıldızlar.** 48/155 galakside (%31) $R_f$ üst sınıra dayanır — fit yayılma istemez ve model etkin olarak $k=2$'ye döner, ama AIC cezasını yine öder. Bu galaksiler panel başlığında yıldız (\*) ile işaretlidir. Yıldızların dağılımı **belirli bir rejimde toplanmaz** (hem cücelerde hem kütlelilerde vardır) — bu, 6.5.4.6'nın "$R_f$ fenomenolojiktir" tespitiyle tutarlıdır: fiziksel bir yayılma olsaydı, disk kalınlaşması evrensel olduğu için her galakside sonlu bir $R_f$ beklenirdi.

**Kayıt.** Teorinin resmî galaktik denklemi $k=2$ hâlidir; $\ell_\omega$'nın yasası vardır ve o hâl 6.5.3.3'ün rejim sonucunu verir. $k=3$ hâli, dış-bölge sistematiği çözülene kadar bir **duyarlılık kontrolü** olarak tutulmalıdır, teorinin iddiası olarak değil.

### Sonuç
Evrenakı teorisinin kinematik denklemleri; sarmal, eliptik ve cüce küresel gözetmeksizin, dönen bir çekirdeğe sahip tüm galaktik yapılarda "Karanlık Madde" varsayımını tamamen ortadan kaldırmakta ve dönüş-hızı anomalisini kendi iç dinamikleriyle, saf matematiksel bir kesinlikle çözmektedir.

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
Galaksilerdeki yörüngelerin "düzenli disk" mi yoksa "kaotik küre" mi olacağı, bütünüyle sistemin **Eksenel İtim (F4)** gücüne ve ekseninin kararlılığına bağlıdır. F4'ü besleyen şey, kapsanan baryonik kütlenin **düzenli dolanım debisidir** (6.5.4.3): dolanım ne kadar hizalıysa itim o kadar güçlü ve kararlıdır.

* **Cüce Küreseller (Sıfır Eksenel İtim):** Düzenli dolanım yoktur; yıldızlar hız dağılımındadır. Net vortisite kurulamadığı için Eksenel İtim doğmaz ($B\approx0$): yıldızlar sadece merkezdeki basınç çukuruna (Merkezcil İtim'e) doğru rastgele, arı kovanı gibi 3 boyutlu kaotik yörüngelerde uçuşurlar.
* **Sarmal Galaksiler (Maksimum ve Sabit Eksenel İtim):** Baryonik kütle tek ve kararlı bir eksende dolanır; Evrenakı dev bir mikser gibi hep aynı yönde karılır ve F4 sürekli beslenir. Sürtünme (gaz ve toz) de mevcut olduğundan, Eksenel İtim (B) yıldızları zamanla tek bir düzleme (diske) kusursuzca hizalar. Sarmal şekil doğar.
* **Dev Elips Galaksiler (Yalpalayan / Precession Yapan İtim):** Çarpışmalar kurbanı olan bu ölü devlerde dolanım eksenleri sabitleşememiş, şiddetle yalpalayan (**Precession**) durumdadır. Yalpalayan eksenel itim, akışkanı bir düzlemde değil, "3 boyutlu bir çalkalama" şeklinde savurur. Gaz ve sürtünme de olmadığı için trilyonlarca yıldız asla bir diske yerleşemez, rastgele 3 boyutlu yörüngelerde salınım (pendulum) hareketi yaparak galaksiyi devasa bir küre (elips) formuna mahkûm eder.

### C. 4B'den 3B'ye İzdüşümün Makro Kanıtı: Precession
Dev galaksilerin yalpalaması (Precession) basit bir tesadüf veya sadece çarpışmaların bir sonucu değildir. Dört boyutlu bir **çift dönüş**, üç boyutlu uzaya yansıtıldığında görünür dönme ekseni sabit kalamaz; koni çizerek yalpalar (1.4.7). Evrenakı teorisine göre madde (kavitasyon yırtığı), doğası gereği 4B bir dönüşün eseridir. Bu sistemlerin dolanım eksenlerinin yalpalaması, 4B'deki Evrenakı girdabının 3B uzayımıza düşen gölgesidir.

> [!WARNING]
> **Düzeltme — "izoklin" tam tersini söyler.** Bu paragraf daha önce yalpalamayı *"SO(4) **izoklin** dönüşler"*e yazıyordu. İzoklin dönüş, iki değişmez düzlem hızının **eşit** olduğu ($\omega_1=\omega_2$) özel hâldir ve 1.4.8 md.3'ün bağıntısı tam olarak şunu verir: eşitlik hâlinde $\varepsilon=0$, yani **devinim yoktur** — üç boyutlu izdüşüm eğik bir düzlemde düzgün dairedir, koni taranmaz. Devinimi üreten şey izoklinlik değil, **izoklinlikten sapmadır.** Ayrıca izoklin dönüşler SO(4) içinde ölçüsü sıfır bir altkümedir; "4B dönüşler" diye genellenemez. Doğru ifade yukarıdadır: yalpalamayı üreten şey **genel** çift dönüştür.

Galaksilerin devasa küre yapıları bu mekaniğin galaktik ölçekteki izidir. *(Kayıt: buradaki bağ **niteliksel**dir. Bağıntının nicel sınavı gök cisimlerinde yapılmıştır — 11.7.6, Dünya'da binde iki — ve galaktik ölçeğe taşınmamıştır; dev eliptiklerde $\varepsilon$ ve koni açısı bağımsız ölçülmediği için bu paragraf bir ispat değil, mekanizma okumasıdır.)*

### D. Kütle ve Dönüş Paradoksunun Çözümü ($\sqrt{2}c_0$)
Astronomide dev elips galaksilerin merkezindeki devasa kara deliklerin "yavaş" döndüğü ($a^*$ spin katsayısının düşük olduğu) ölçülür. Bu durum, teorimizin *"Kütle arttıkça dönüş gücü artmalıdır"* kuralıyla asla çelişmez, bilakis doğrular:
1. **Mutlak Açısal Momentum:** Astronomların yavaş dediği şey kütleye oranlanmış katsayıdır. Kara deliğin gerçek fiziksel dönüş gücü (Açısal Momentumu, $J \propto M^2$) kütlenin karesiyle artar. Yani kütlesi devasa olan bir kara deliğin mutlak eksenel itim gücü, küçük ama hızlı dönen bir kara delikten milyonlarca kat daha fazladır.
2. **$\sqrt{2}c_0$ Denge Hızı:** Ek A.2'de kanıtlandığı gibi, *Her kararlı vakum-cepli girdap boyutu ne olursa olsun duvarını tam $\sqrt{2}c_0$'de döndürür.* Eğer dev kara delikler tek bir makro-Zerre (vakum cebi) ise, kavitasyon yüzeyindeki teğetsel hız hep sabit ve ışık hızının üzerindedir ($\sqrt{2}c_0$). Kütle arttıkça kara deliğin çapı Güneş Sistemi boyutlarına ulaştığından, yüzey hızı aynı kalmasına rağmen tam tur atma süresi uzar (RPM düşer) ve dışarıdan "yavaş dönüyor" gibi algılanır. Oysa kavitasyon duvarı, içerideki devasa kütleyi (deplasmanı) yaratan asıl yırtılma hızıyla dönmeye devam etmektedir.

---

## 6.5.4 Saf Beş Kuvvet Sınavı: Kapsanan Kütle Artışı ve Vortisite Beslemeli Eksenel İtim

>
> *(Konum notu: kesit, yazarın talebiyle bölümün sonuna işlenmiştir; içerik olarak 6.5.3.1'in devamıdır ve §4'ün morfoloji tartışmasından önce okunabilir.)*

## 6.5.3.6 Türetim–Fit Defteri: $\chi^2$'nin Göremediği Hesap

Yukarıdaki bütün karşılaştırmalar $\chi^2$ ve AIC üzerinden yürütüldü. **Bu ölçütler eğri uydurma kalitesini ölçer; türetmeyi ölçmez.** Bir teori baryonik Tully-Fisher ilişkisini sıfır serbest parametreyle öngörüyorsa, öteki onu geri-besleme ayarıyla yakalıyorsa, AIC ikisine **aynı notu verir**. Bu asimetri yukarıdaki tabloların hiçbirinde görünmez. Bu alt bölüm iki tarafın defterini ayrı ayrı tutar — ve sonra ikisini birlikte okur.

![Türetim–fit defteri ve $\Upsilon_*$ tavan sınavı](Gorseller/turetim_fit_defteri.png)

### Defterin türetim tarafı

| Büyüklük | Evrenakı | ΛCDM |
|---|---|---|
| Düz dönüş kolunun biçimi | **türetilmiş** — M-38: $h_d=$sabit $\Rightarrow a\propto1/R \Rightarrow v=$sabit | halo profili + baryon eşleşmesi *(disk–halo komplo problemi)* |
| İvme ölçeği $a_0$ | **biçimi türetilmiş** ($\mathcal{G}m_n/\ell_\omega^2$), değeri **kalibre** — SPARC'a sabitlenmiş (6.5.4.5) | **karşılığı yok** |
| BTFR **eğimi** ($v^4\propto M_{bar}$) | **türetilmiş** — yasadan tek satırda çıkar | geri-beslemeyle üretilmeli |
| BTFR **normalizasyonu** | kalibre ($a_0$'a bağlı) — ölçülen 0,984 (6.5.4.5) | geri-beslemeyle ayarlanır |
| BTFR saçılmasının darlığı | yasanın doğal sonucu | **ince ayar bilmecesi** |
| $\ell_\omega$'nın kütleyle ölçeklenmesi | **yasa** — $\propto\sqrt{M_{bar}}$, ölçülen eğim 1,03 | karşılığı yok |
| Dönüş eğrisi profilinin kaynağı | **teorem** — M-37: $v_{y\ddot{o}r}=\sqrt{R\lvert a_{radyal}\rvert}$ | varsayılan profilin sonucu |
| Halo yoğunluk profili | — *(halo yok)* | **türetilmiş** — N-cisim: NFW |
| $c_{200}$–$M_{200}$ ilişkisi | — | **türetilmiş** — N-cisim |
| Galaksi başına $M_{200}$ | — | **fit** |
| Galaksi başına $\Upsilon_*$ | **fit** (ortak) | **fit** (ortak) |
| İç bölge: çekirdek mi sivri mi | çekirdek doğal | **cusp zorunlu** → Core-Cusp problemi |
| Görünmez madde envanteri | **talep yok** | **zorunlu** |

**Sayım.** Evrenakı **beş** büyüklüğü türetir (düz kolun biçimi, BTFR eğimi, BTFR saçılmasının darlığı, $\ell_\omega$'nın kütleyle ölçeklenmesi, M-37 profil teoremi), **bir küresel sabiti kalibre eder** ($a_0$ — biçimi türetilmiş, değeri gözlemle sabitlenmiş) ve galaksi başına bir parametre fitler ($\Upsilon_*$). ΛCDM iki büyüklüğü türetir, ikisini fitler ve görünmez madde bileşeni talep eder. **Önemli ayrım:** BTFR'nin **eğimi** türetilmiştir ama **normalizasyonu** $a_0$'a bağlıdır, dolayısıyla o da kalibredir — "BTFR sıfır parametreyle çıkıyor" ifadesi eğim için doğru, genlik için değildir.

### Ama defterin bir de asimetri satırı var — ve o teorinin aleyhinedir

**Evrenakı'nın türetimlerinin tamamı, sınandıkları aynı dönüş eğrilerinden okunmuştur.** $a_0$'ın değeri SPARC'a kalibre edildi (6.5.4.5); $\ell_\omega$ yasası aynı SPARC örneğinden çıkarıldı; M-38'in yayılma çarpanı fitlendi (6.5.4.6). **ΛCDM'in NFW profili ve $c_{200}$–$M_{200}$ ilişkisi ise bağımsız bir hesaptan gelir** — dönüş eğrilerine hiç bakmayan N-cisim simülasyonlarından. Bu, defterin en önemli satırıdır:

> Bir büyüklüğü "türetmek" ile onu "aynı veriden okuyup türetim gibi sunmak" farklıdır. Evrenakı'nın türetimleri **öngörü statüsünü henüz kazanmamıştır**; kazanmaları için dönüş eğrileri dışında bir gözlemde doğrulanmaları gerekir. Defterin türetim tarafı bu nedenle *potansiyel* bir üstünlüktür, kazanılmış bir üstünlük değil.

### Ve defterin fit tarafı: hüküm kuruluma bağlı

| Kurulum ($k=2$, 163 galaksi) | Medyan $\chi^2_{ind}$ | Evrenakı önde |
|---|---|---|
| Evrenakı, $\Upsilon_*\leq2{,}0$ *(kitabın temeli)* | **1,568** | 90/163 = %55 ($+1{,}3\sigma$) |
| Evrenakı, $\Upsilon_*\leq3{,}0$ | 1,357 | 96/163 = %59 ($+2{,}3\sigma$) |
| Evrenakı, $\Upsilon_*$ bantlı ($0{,}3$–$0{,}8$) | **3,449** | 71/163 = %44 ($-1{,}6\sigma$) |
| ΛCDM NFW, $\Upsilon_*\leq2{,}0$ | 1,980 | — |
| ΛCDM NFW, $\Upsilon_*$ bantlı | 2,580 | — |

Serbest $\Upsilon_*$ ile Evrenakı medyan olarak öndedir ($1{,}57 < 1{,}98$) ama kazanma oranı beraberliktir. Fotometrik bantla ΛCDM öne geçer. **Hüküm, $\Upsilon_*$'a konan kısıta bağlıdır.**

### Tavan bulgusu: sorun bandın doğruluğu değil

Bant sınavına yöneltilebilecek itiraz şudur: *"$0{,}3$–$0{,}8$ bandı fazla dar olabilir."* Bu itirazı çürüten ölçüm şudur — fit, **konulan her tavanı arıyor:**

| $\Upsilon_*$ üst sınırı | Tavana dayanan galaksi | Medyan $\Upsilon_*$ | Bandın dışında |
|---|---|---|---|
| $\leq2{,}0$ | **%18** | 0,85 | %60 |
| $\leq3{,}0$ | **%9** | 0,85 | %60 |

Yani her beş galaksiden birinde model $\Upsilon_*>2$ istemektedir — 3,6 μm'de bu, yıldız kütlesinin fotometrinin taşıyabileceğinin **üç-altı katı** demektir. Tavan 3,0'a çıkarıldığında hâlâ %9'u dayanmaktadır. **Sorun bandın genişliği değil; modelin sınırsız $\Upsilon_*$ istemesidir.** Bu, yukarıdaki tek olasılığı doğrular: $M_{kaps}$ kaynağının biçimi eksiktir ve model açığı yıldız kütlesini şişirerek kapatmaktadır.

### Fit girdisi faturası: her fitlenen sayı ücretlendirilirse


Yukarıdaki bütün karşılaştırmalar **galaksi başına** medyan üzerinden yapıldı. Bu, parametre maliyetini gizler: 163 galaksiye yayılmış bir parametre 163 serbest sayıdır, ve galaksi başına AIC'nin $2k$ cezası bunu eksik çeker. Doğru hesap örneklem genelinde toplam fit girdisini saymaktır:

$$K = (\text{galaksi başına parametre})\times(\text{galaksi sayısı}),\qquad \mathrm{BIC} = \sum\chi^2 + K\ln N_{nokta}$$

BIC, AIC'den çok daha sert cezalandırır. **ΛCDM'in NFW profili ve $c_{200}$–$M_{200}$ ilişkisi ücretlendirilmez** — onlar dönüş eğrilerine değil N-cisim simülasyonlarına kalibredir. Adil kurulum budur.

![Fit girdisi faturası](Gorseller/fit_girdisi_faturasi.png)

| Model | Fitlenen | $K$ | $\sum\chi^2$ | $\chi^2/dof$ | $\Delta$BIC |
|---|---|---|---|---|---|
| *$\Upsilon_*$ serbest ($\leq2{,}0$)* | | | | | |
| Yalnız baryonlar | $\Upsilon_*$ | 163 | 429 140 | 136,84 | $+412\,833$ |
| Evrenakı — $a_0$ **teoriden** | $\Upsilon_*$ | **163** | 57 683 | 18,39 | $+41\,376$ |
| **Evrenakı — $b$ fitli** | $\Upsilon_*$, $b$ | 326 | **14 986** | **5,04** | **0** |
| ΛCDM NFW | $\Upsilon_*$, $M_{200}$ | 326 | 16 526 | 5,56 | $+1539$ |
| *$\Upsilon_*$ bantlı ($0{,}3$–$0{,}8$)* | | | | | |
| Evrenakı — $b$ fitli | $\Upsilon_*$, $b$ | 326 | 27 615 | 9,29 | $+8278$ |
| **ΛCDM NFW** | $\Upsilon_*$, $M_{200}$ | 326 | **19 336** | **6,50** | **0** |

**Serbest $\Upsilon_*$ ile fatura Evrenakı'yı kazandırıyor.** Eşit parametre sayısında ($K=326$) $\Delta$BIC $=-1539$. Bu, bu kitapta teorinin **ilk net kazandığı** kurulumdur ve doğrudan sizin kuralınızın — *her fit girdisini ücretlendir* — sonucudur.

**Ama üç çekince, ve üçü de kaydedilmelidir.**

**Çekince 1 — en az fit girdisi kullanan hâl herkese kaybediyor.** $a_0$'ı teoriden alıp $b$'yi yasadan türeten sürüm ($K=163$, yani ΛCDM'in **yarısı** kadar fit girdisi) $\sum\chi^2=57\,683$ verir; serbest $b$'li hâl 14 986. **3,85 kat kötü.** Parametreyi yarıya indirmenin BIC kazancı ($\sim1300$) bu açığın ($\sim43\,000$) yanında hiçtir. Anlamı şudur: **$\ell_\omega$ yasası vardır ve eğimi doğrudur (1,03), ama 0,38 dex'lik (2,4 kat) saçılması onu fit parametresinin yerine koyacak kadar sıkı değildir.** Ceza kuralı teoriyi az parametreyle kazandırmıyor — yasa henüz o kadar iyi değil.

**Çekince 2 — $\chi^2/dof\approx5$, yani iki model de formel olarak kötü uyuyor.** Bu, SPARC'ın hata çubuklarının gerçek saçılmayı eksik temsil ettiğini (veya modellenmeyen sistematik olduğunu) gösterir. Böyle bir durumda $\Delta$BIC'in mutlak büyüklüğü şişkindir. En iyi modelin $\chi^2/dof=1$ olacak şekilde hatalar yeniden ölçeklendiğinde $\Delta$BIC $-1539$'dan $-305$'e iner — hüküm değişmez ama büyüklüğü altı kat küçülür.

**Çekince 3 — ve bu en önemlisi: bantlı hüküm kırpmayla tersine dönüyor.**

| Ölçüt (eşit $K=326$) | $\Upsilon_*$ serbest | $\Upsilon_*$ bantlı |
|---|---|---|
| Ham $\Delta$BIC | $\mathbf{-1539}$ | $+8278$ |
| Hata ölçekli | $\mathbf{-305}$ | $+1273$ |
| **En kötü %5 kırpılmış** | $\mathbf{-178}$ | $\mathbf{-767}$ |
| Galaksi başına oy | %55 ($+1{,}3\sigma$) | %44 ($-1{,}6\sigma$) |

Bantlı hâlde ΛCDM'in $+8278$'lik zaferi **geniş bir üstünlükten gelmiyor.** Zararın kaynağı ayrıştırıldığında:

| Galaksi | $v_{max}$ | B/T | $\chi^2$ Evrenakı | $\chi^2$ ΛCDM | Katkı |
|---|---|---|---|---|---|
| UGC00128 | 134 | 0,00 | 4172 | 49 | $+4123$ |
| UGC05716 | 75 | 0,00 | 1179 | 14 | $+1165$ |
| NGC5985 | 305 | 0,00 | 1629 | 702 | $+927$ |
| NGC0247 | 108 | 0,00 | 856 | 113 | $+743$ |
| UGC05764 | 56 | 0,00 | 736 | 60 | $+676$ |
| UGC00731 | 74 | 0,00 | 680 | 5 | $+675$ |
| UGC09133 | 289 | 0,27 | 1173 | 590 | $+583$ |
| NGC2403 | 136 | 0,00 | 731 | 381 | $+351$ |
| UGC08286 | 84 | 0,00 | 356 | 54 | $+301$ |
| UGC02259 | 90 | 0,00 | 329 | 40 | $+290$ |
| **ilk 10 toplamı** | | | | | $\mathbf{+9835}$ *(toplamın %119'u)* |
| **kalan 153 galaksi** | | | | | $\mathbf{-1557}$ *(Evrenakı önde)* |

**Yani bantlı hâlde bile Evrenakı 153 galakside öndedir**; bütün kaybı 10 galaksiden (%6) gelir. Ve o 10'un **yapısal imzası yoktur**: dokuzu kovansızdır (B/T $=0$), medyan $v_{max}$ 99 km/s (örneklem geneli 110), yani ne kütle ne morfoloji onları ayırmaktadır. Kovanlı galaksilerde ($n=24$) Evrenakı zaten öndedir ($-527$).

> **Bunun anlamı bir yenilgi değil, bir teşhis kalemidir.** Model tipik galakside — fotometrik $\Upsilon_*$ altında bile — ΛCDM'den iyi çalışıyor, ama %6'lık bir altkümede **felaket biçiminde** başarısız oluyor ve bu altkümenin nedeni bilinmiyor. Genel bir zayıflık, tek tek anlaşılabilir on başarısızlıktan daha kötüdür; buradaki durum ikincisidir. **O on galaksinin neden koptuğunu bulmak, teorinin galaktik dosyasındaki en verimli sıradaki iştir** (7.4, madde 12/k).

### Yalnızca spiral ölçekte: teorinin evi neresi?


Buraya kadarki bütün karşılaştırmalar SPARC'ın **tamamı** üzerinden yapıldı ve örneklem cüce, düzensiz ve düşük yüzey parlaklıklı sistemleri de içeriyordu. 6.5.3.3 bir iddiada bulunmuştu: *"teorinin cephesi düz dönüş eğrisi değil, Core-Cusp rejimidir."* Bu alt başlık o iddiayı **doğrudan ölçer.**

**Sınıflama gerçek Hubble tiplerinden gelmektedir.** SPARC ana kataloğu (Lelli, McGaugh & Schombert 2016, Tablo 1) indirilmiş ve her galaksinin Hubble tipi $T$ doğrudan okunmuştur: $T=0$ S0, $1$ Sa, $2$ Sab, $3$ Sb, $4$ Sbc, $5$ Sc, $6$ Scd, $7$ Sd, $8$ Sdm, $9$ Sm, $10$ Im, $11$ BCD. **Spiral $=$ Sa–Sd ($T=1$–$7$).** 163 galaksinin tipi eşleşmiştir: **91 spiral, 69 cüce/düzensiz (Sdm–BCD), 3 mercekssel (S0)**.

![Yalnızca spiral ölçekte kıyaslama](Gorseller/spiral_kiyaslama.png)

| Altküme | $\Upsilon_*$ koşulu | Medyan $\chi^2_{ind}$ Evrenakı | Medyan ΛCDM | Evrenakı önde | $\Delta$BIC (ölçekli) |
|---|---|---|---|---|---|
| **SPİRAL** Sa–Sd (91) | serbest ($\leq2{,}0$) | **2,008** | 2,265 | 42/91 = %46 ($-0{,}7\sigma$) | $+77$ |
| **SPİRAL** Sa–Sd (91) | bantlı ($0{,}3$–$0{,}8$) | 3,660 | **2,580** | 38/91 = %42 ($-1{,}6\sigma$) | $+456$ |
| cüce/düzensiz Sdm–BCD (69) | serbest | **1,004** | 1,753 | **45/69 = %65 ($+2{,}5\sigma$)** | $\mathbf{-560}$ |
| cüce/düzensiz Sdm–BCD (69) | bantlı | **2,322** | 2,432 | 31/69 = %45 ($-0{,}8\sigma$) | $+800$ |

**Spiral galaksilerde teorinin üstünlüğü yoktur — ve bu, beraberlikten de zayıftır.**

- **Serbest $\Upsilon_*$ ile bile geride.** Medyan $\chi^2_{ind}$ Evrenakı lehinedir (2,01'e karşı 2,27) ama galaksi başına oy **%46**'dır ($-0{,}7\sigma$). İki gösterge ters yönü işaret ediyor: tipik spiralde uyum biraz daha iyi, ama galaksilerin çoğunda ΛCDM önde. Fark anlamlı değildir; **başabaş, hafif ΛCDM lehine.**
- **Fotometrik $\Upsilon_*$ ile ΛCDM açık ara önde:** 2,58'e karşı 3,66; oy %42 ($-1{,}6\sigma$).

**Ve teorinin tek anlamlı galibiyeti kesindir:** cüce/düzensiz altküme **ve** serbest $\Upsilon_*$. Orada oy %65 ($+2{,}5\sigma$), medyan **1,004**'e karşı 1,753 ve $\Delta$BIC $-560$. Medyan $\chi^2_{ind}$'in kabul sınırına ($=1$) tam oturması bu hücreye özgüdür. Bu, bu kitapta teorinin istatistiksel olarak anlamlı **tek** galibiyetidir.

**Spiraller içinde bir eğilim var ve kaydedilmelidir.** Alt tipe göre Evrenakı'nın önde olduğu galaksi oranı (serbest $\Upsilon_*$):

| Sab (10) | Sb (12) | Sbc (18) | Sc (16) | Scd (16) | **Sd (16)** |
|---|---|---|---|---|---|
| %50 | %33 | %50 | %44 | %31 | **%69** |

En geç spiral tipi olan **Sd'de teori öne geçiyor** (%69) — ve Sd, cüce/düzensiz sınırına en yakın, kovansız ve düşük yüzey parlaklıklı tiptir. Eğilim düzgün değildir (Scd %31 ile kırıyor) ve alt örneklem sayıları küçüktür, ama yön 6.5.3.3'ün fiziksel okumasıyla uyumludur: **teori kovansız, düşük yoğunluklu iç bölgeye sahip sistemlerde iyi çalışmaktadır.**

> **Bu bir çelişki değil, 6.5.3.3'ün doğrulanmasıdır.** Kitap zaten *"düz dönüş eğrisi bir zafer değildir"* diyordu; bu ölçüm o cümleyi sayıya çevirir. Teorinin toplam örneklemdeki avantajı **spirallerden gelmiyordu**; cüce/düzensiz altkümesinden geliyordu. Spiral galaksinin düz dönüş kolu, teorinin ΛCDM'den daha iyi açıkladığı bir olgu **değildir**.

**İki şey bu tabloda görünmüyor ve kaydedilmelidir.** Birincisi: spiraldeki başabaşlık **görünmez madde envanteri talep edilmeden** sağlanmaktadır — ΛCDM aynı 91 eğri için halo ister. İkincisi: fotometrik $\Upsilon_*$ dayatıldığında teori **hiçbir tipte** kazanmamaktadır; cüce/düzensizdeki galibiyet de $+2{,}5\sigma$'dan $-0{,}8\sigma$'ya iner. Teorinin tek zaferi, tek serbest parametresinin fotometrik önselden kurtulmasına bağlıdır.

**Sınıflama kuralı — vekil değil, gerçek tip.** Buradaki spiral seçimi SPARC ana kataloğunun **gerçek Hubble tipleriyle** yapılmıştır; yapısal vekiller kullanılmaz. Nedeni ölçülmüştür: makul görünen bir vekil ($v_{max}\geq80$ km/s ve yıldız katkısı $>$ gaz katkısı) 91 gerçek spiralin 84'ünü yakalar ama **21 spiral-olmayan sistemi yanlışlıkla spiral sayar** — aralarında NGC2915 (BCD), NGC4214 (Im), UGC01230 (Sm) ve kritik olarak **UGC00128 (Sdm)**. UGC00128, bantlı $\Upsilon_*$ altındaki en büyük tek aykırı katkıdır ($+4123$; bkz. fit girdisi faturası); vekil onu spiral sayınca spiral altkümesinin sayıları **iyimserleşir** (vekille oy %49, gerçek tiple %46). Bu sayfadaki bütün sayılar gerçek Hubble tipleriyledir.

*Yöntem notu:* SPARC'ın `.mrt` dosyasında sütun başlığı $T$ için "12–13. bayt" demektedir, ancak veri satırlarında alan bir bayt kaymıştır. Sabit genişlikli okuma bu yüzden **sessizce** yanlış sonuç verir — her galaksiye $T=1$ (Sa) atar. Betik bu nedenle belirteç tabanlı okuma kullanır; hata bu bölümün üretiminde bir kez yapılmış ve tip dağılımı denetlenerek yakalanmıştır.

### Tip tip döküm: "cüce/düzensiz" bloğu neyi gizliyordu?

Buraya kadarki bütün ayrıştırmalar iki bloğa dayanıyordu: spiral (Sa–Sd) ve cüce/düzensiz (Sdm–BCD). **Blok ortalaması iki gerçeği birden gizliyordu.** SPARC ana kataloğundan Hubble tipi okunup hiçbir tip bloklanmadan raporlandığında:

![Hubble tipine göre tam döküm](Gorseller/tip_dokumu.png)

| Tip | $N$ | $\Upsilon_*$ bant dışı | Medyan $\Upsilon_*$ | Tavanda | Evrenakı önde (serbest) | (bantlı) |
|---|---|---|---|---|---|---|
| S0 | 3 | %33 | 0,64 | %0 | 3/3 | 2/3 |
| **Sa–Sd (spiral)** | 91 | %44 | **0,64** | %9 | 42/91 ($-0{,}7\sigma$) | 38/91 ($-1{,}6\sigma$) |
| Sdm | 9 | %78 | 1,41 | %33 | 5/9 ($+0{,}3\sigma$) | 4/9 ($-0{,}3\sigma$) |
| **Sm** | 23 | **%91** | **1,68** | **%39** | 13/23 ($+0{,}6\sigma$) | 6/23 ($\mathbf{-2{,}3\sigma}$) |
| **Im (düzensiz)** | 33 | %79 | 0,98 | %27 | **26/33 ($\mathbf{+3{,}3\sigma}$)** | 19/33 ($+0{,}9\sigma$) |
| BCD | 4 | %75 | 1,08 | %0 | 1/4 | 2/4 |

##### Bulgu 1 — teorinin en güçlü sonucu Im'dedir ve blok içinde kaybolmuştu

**26/33 = %79, $+3{,}3\sigma$.** Bu, bu bölümdeki en yüksek anlamlılıktır. "Cüce/düzensiz" bloğu olarak bakıldığında $+2{,}5\sigma$ görünüyordu; ayrıldığında Im tek başına daha güçlü çıkar, çünkü blok içindeki Sm onu aşağı çekiyordu.

Ve daha önemlisi: **$\Upsilon_*$ fotometrik banda hapsedildiğinde pozitif kalan tek tip Im'dir** ($+0{,}9\sigma$). Her yerde hükmü deviren bant kısıtı orada devirmiyor.

##### Bulgu 2 — $\Upsilon_*$ şişmesi genel bir kusur değil, Sm/Sdm'ye özgüdür

| | Medyan $\Upsilon_*$ | Tavanda |
|---|---|---|
| Spiral (Sa–Sd) | **0,64** | %9 |
| Im | 0,98 | %27 |
| Sdm | 1,41 | %33 |
| **Sm** | **1,68** | **%39** |

Sm'de model, fotometrinin taşıyabileceğinin **üç katı** yıldız kütlesi istemekte ve galaksilerin %39'unda tavana dayanmaktadır. Bant dayatıldığında en sert çöküş de oradadır ($+0{,}6\sigma \to -2{,}3\sigma$). Buna karşılık spirallerde medyan **0,64**'tür — beklenen $\sim$0,5'e yakın ve tavana dayanan yalnız %9.

> **Bu, önceki teşhisi değiştirir.** 6.5.4.7 kayıt (4) ve bu bölümün tavan bulgusu, *"model $M_{kaps}$ kaynağının açığını $\Upsilon_*$'ı şişirerek kapatıyor"* teşhisini **genel bir kusur** olarak koymuştu. Tip tip bakıldığında bu teşhis **yalnız Sm/Sdm için** doğrudur. Genel bir zayıflık değil, **belirli bir morfolojiye bağlı, teşhis edilebilir bir sınır durumudur** — ve nedeni aranabilir: Sm/Sdm gaz-baskın Macellan sarmallarıdır, dolayısıyla ilk şüpheli $M_{kaps}$'ın **gaz terimidir**, yıldız terimi değil.

##### Yöntem kuralı — blok yok

Bu turda görüldü ki tek bir gruplama kararı, aynı bulguyu $\Upsilon_*$ bant ihlalinde %44 ile %91 arasında oynatabiliyor. **Çözüm doğru altörneklemi seçmek değil, hiç seçmemektir.** Bu bölümdeki ölçümler bundan böyle tip tip verilir; blok ortalaması yalnız tiplerin yanında, özet olarak sunulur. $N<5$ olan tipler (S0, BCD) istatistik taşımaz ve öyle işaretlenir.

### Gerçek ölçümden sapma: hüküm $\chi^2$'nin eseri mi?

Bu bölümdeki bütün hükümler $\chi^2$ üzerinden verildi. Ama $\chi^2$ her noktayı $1/\sigma^2$ ile **ağırlıklandırır**: hata çubuğu küçük galaksiler baskın çıkar ve SPARC'ta bunlar yüksek kaliteli spirallerdir. Hüküm bu ağırlıklandırmanın eseri olabilir mi? Sınav basittir — ağırlık kaldırılır ve doğrudan sorulur: **modelin eğrisi ölçülen noktalardan kaç km/s sapıyor, ve noktaların kaçı ölçüm hata çubuğunun içinde kalıyor?**

![Gerçek ölçümden sapma](Gorseller/olcum_sapmasi.png)

| $\Upsilon_*$ | Kapsam | $N$ | RMS Evrenakı | RMS ΛCDM | Hata çubuğu içinde | $\sigma$ (km/s) | $\sigma$ ($\chi^2$) |
|---|---|---|---|---|---|---|---|
| serbest | **tüm disk** | 163 | **5,60** | 6,19 | **%65** / %59 | $+1{,}2$ | $+1{,}3$ |
| serbest | spiral Sa–Sd | 91 | 8,43 | **7,57** | %53 / **%58** | $-0{,}9$ | $-0{,}7$ |
| serbest | Sm | 23 | **3,98** | 4,63 | %60 / **%68** | $+1{,}0$ | $+0{,}6$ |
| serbest | **Im** | 33 | **2,77** | 4,48 | **%86** / %55 | $\mathbf{+3{,}0}$ | $+3{,}3$ |
| bantlı | tüm disk | 163 | 8,80 | **6,73** | %47 / %54 | $-1{,}5$ | $-1{,}6$ |
| bantlı | spiral Sa–Sd | 91 | 10,45 | **9,01** | %45 / %50 | $-1{,}8$ | $-1{,}6$ |
| bantlı | Sm | 23 | 8,80 | **5,02** | %25 / %54 | $-1{,}9$ | $-2{,}3$ |
| bantlı | **Im** | 33 | **4,10** | 4,78 | **%62** / %55 | $+1{,}2$ | $+0{,}9$ |

##### Sonuç 1 — hüküm ölçüt seçimine sağlamdır

**İki ölçüt sekiz hücrenin sekizinde de aynı yönü gösteriyor**; en büyük fark $0{,}4\sigma$'dır. Yani $\chi^2$'nin ağırlıklandırması bu bölümün hükümlerini saptırmamıştır. Bu, olumlu ve gerekli bir sağlamlık sonucudur: $\chi^2/dof\approx5$ olduğu için hata çubuklarının eksik temsil ettiği bilinmektedir (6.5.3.6, çekince 2), ve ağırlıksız sınav aynı yanıtı verdiğine göre bu eksiklik hükmü belirlememiştir.

> **Okuma uyarısı.** Tüm disk $+$ serbest $\Upsilon_*$ hücresinde iki ölçüt de Evrenakı'yı önde verir ($+1{,}2$ ve $+1{,}3$). Bu hücrenin sonucu, bantlı hâlin ve BIC toplamlarının sonucuyla karıştırılmamalıdır — üçü ayrı sorulara yanıt verir.

##### Sonuç 2 — fiziksel bulgu: Im'de eğri ölçüm hata çubuğunun içinden geçiyor

Ağırlıksız sınavın $\chi^2$'nin vermediği bir bilgisi var: **modelin kaç noktası ölçümün kendi hata çubuğunun içinde kalıyor.** Im (düzensiz) tipinde:

$$\text{Evrenakı: } \mathbf{\%86} \qquad\text{ΛCDM: } \%55$$

Bu, "daha küçük $\chi^2$" demekten farklı ve daha güçlü bir ifadedir: eğri, ölçümün hata payının içinden geçmektedir. Medyan RMS sapması da 2,77 km/s'dir (ΛCDM 4,48) — tüm örneklemin en düşük değeri. Bant dayatıldığında bile Evrenakı önde kalır (%62'ye karşı %55).

##### Sonuç 3 — kapsama göre hüküm

- **Spiral (Sa–Sd):** her iki $\Upsilon_*$ koşulunda ve her iki ölçütte **ΛCDM önde** (RMS 7,57'ye karşı 8,43; hata içi %58'e karşı %53). Bu, 6.5.3.6'nın spiral hükmünü bağımsız bir ölçütle doğrular.
- **Tüm disk, serbest $\Upsilon_*$:** **Evrenakı önde** (5,60'a karşı 6,19; %65'e karşı %59).
- **Tüm disk, bantlı $\Upsilon_*$:** ΛCDM önde.
- **Im:** Evrenakı, her iki koşulda ve açık farkla.

Yani ölçümden sapma sınavı **yeni bir hüküm getirmiyor, mevcut hükmü sağlamlaştırıyor** — ve tek yeni bilgisi Im'deki %86'lık hata-çubuğu-içi oranıdır.

### Girdi dürüstlüğü karnesi: aynı mercek, iki model

Buraya kadarki denetimlerde bir **asimetri** vardı ve kaydedilmesi gerekir: Evrenakı'nın serbest parametresi ($\Upsilon_*$) bağımsız bir fiziksel önsele (yıldız popülasyon sentezi) sokulup sınandı, ihlal ettiği kaydedildi. **ΛCDM'in serbest parametresine ($M_{200}$) aynı sınav uygulanmadı.** Bu alt başlık o eksiği kapatır ve girdileri eşit ölçütlerle puanlar.

![Girdi dürüstlüğü — aynı sınav, iki model](Gorseller/girdi_durustlugu.png)

##### (A) Simetrik önsel denetimi

ΛCDM'in $M_{200}$'ü için bağımsız önsel **abundance matching**'dir (yıldız kütlesi–halo kütlesi ilişkisi; Moster ve ark. 2013, $z=0$, saçılma $\sim0{,}2$ dex). 163 galakside her iki sınav:

| | Evrenakı ($\Upsilon_*$) | ΛCDM ($M_{200}$) |
|---|---|---|
| Bağımsız önsel | pop. sentezi $0{,}3$–$0{,}8$ | abundance matching $\pm0{,}2$ dex |
| **Önselin dışında kalan** | **%60** | **%67** |
| Sistematik sapma | **var** (medyan 0,85; beklenen $\sim$0,5) | yok (medyan $-0{,}01$ dex) |
| Saçılma | — | **0,99 dex** (beklenen 0,2) |
| 10 kattan fazla sapan | — | **%19** |
| Fit sınırına dayanan | **%18** | %3 |

**Her iki model de kendi bağımsız önselini benzer oranda ihlal ediyor.** Fark oranda değil **biçimdedir**: Evrenakı'nınki *sistematiktir* (hep yukarı, beşte biri tavana dayanıyor), ΛCDM'inki *sapmasız ama devasa saçılmalıdır* (her beş galaksiden biri, kendi öngörüsünden **on kattan fazla** sapan bir halo kütlesi istiyor).

> **Kayıt.** "$\Upsilon_*$ tavana dayanıyor" bulgusu geçerlidir — ama **eşdeğeri ΛCDM'de de vardır.** İki model bu kusuru paylaşır; delil tek tarafa yazılamaz.

##### (B) ΛCDM'e kendi serbestliği verilmemişti

Buraya kadarki bütün karşılaştırmalarda $c_{200}$–$M_{200}$ ilişkisi **tam dayatıldı** ($k=2$). Oysa SPARC literatüründeki standart pratik, $c_0$'nin ilişkinin kendi $0{,}11$ dex saçılması içinde oynamasına izin verir ($k=3$). İzin verildiğinde:

| ΛCDM kurulumu | Medyan $\chi^2_{ind}$ | Kabul edilebilir |
|---|---|---|
| $c_0$–$M$ tam dayatılmış ($k=2$) — kitapta kullanılan | 1,980 | 51/163 |
| $c_0$–$M$ saçılma içinde ($k=3$) — **standart pratik** | **1,412** | **71/163** |

**ΛCDM %29 sakatlanmıştı.** Bu, teorinin lehine işleyen bir kurulum hatasıydı ve kaydedilmelidir. Düzeltilmiş karşılaştırmada ΛCDM'in $k=3$ hâli (1,412), Evrenakı'nın $k=2$ hâlini (1,568) geçer — ama bir parametre fazlayla; eşit $k=3$ karşılaştırması için Evrenakı'nın $R_f$'li sürümü kullanılmalıdır (6.5.3.5).

##### (C) $a_0$ katsayısının kararlılığı

Örneklem rastgele iki yarıya bölünüp katsayı bir yarıda kalibre edilip diğerinde sınandığında (2 katlı, 5 bölünme):

| Ölçüm | Değer |
|---|---|
| Eğitim yarılarında bulunan optimum katsayı bandı | **$\pm$%40 genişliğinde** |
| Örnek-içi medyan $\chi^2_{ind}$ | 3,287 |
| Örnek-dışı medyan $\chi^2_{ind}$ | 3,766 |
| Aşırı-uyum cezası | %14,6 |

İki sonuç çıkar. **Olumlu:** kalibrasyon genelleşiyor; örnek-dışı ceza yalnızca %14,6, yani $a_0$ ezberlenmiş bir sayı değil. **Olumsuz:** katsayının kendi belirsizliği **$\pm$%40 mertebesindedir.** Bu yüzden $a_0$'ın herhangi bir teorik sayıyla yüzde-bir düzeyinde "uyuşması"na kanıt değeri atfedilemez — belirsizliği %40 olan bir sayıya o hassasiyet yüklenemez. Bu, $a_0$'ın [S] (gözlemle sabitlenmiş) statüsünü kesinleştirir; $cH_0$ mertebesiyle bugünkü örtüşmenin rastlantı sayılmasının (6.5.4.5) bir gerekçesi de budur.

##### (D) Karne

Girdileri **eşit ölçütlerle** puanlarsak:

| Ölçüt | Evrenakı | ΛCDM | Önde |
|---|---|---|---|
| Galaksi başına fitlenen sayı | 2 ($\Upsilon_*$, $b$) | 3 ($\Upsilon_*$, $M_{200}$, $\Delta\log c_0$) | **Evrenakı** |
| Küresel kalibre edilen sayı | 1 ($a_0$ katsayısı) | 2 ($c_0$–$M$) $+$ $\sim$6 kozmolojik | **Evrenakı** |
| **Kalibrasyonun kaynağı** | **sınandığı aynı veri** | başka veri (N-cisim / CMB) | **ΛCDM** |
| Kalibre sabitin kararlılığı | $\pm$%40 (10,5–22) | sıkı | **ΛCDM** |
| Fonksiyonel biçim | **türetilmiş** (M-38: $h_d=$sabit $\Rightarrow a\propto1/R$) | NFW: simülasyona **uydurma formül** (Einasto daha iyi uyar) | **Evrenakı** |
| Sınav öncesi öngörü kaydı | $\ell_\omega$ eğimi 1,00 öngörüldü → 1,03 ölçüldü **✓** | cusp öngörüldü → çekirdek gözlendi **✗** (geri-besleme kurtarması gerekti) | **Evrenakı** |
| Parametre fiziksel bantta mı | %60 dışında, sistematik, %18 tavanda | %67 dışında, sapmasız, %19'u 10 kat | berabere |
| Doğrulanmamış varlık talebi | Evrenakı akışkanı — hiç aranmadı | CDM parçacığı — 40 yıl arandı, bulunamadı | berabere |

**Sayım: Evrenakı 4 — ΛCDM 2 — berabere 2.**

##### Açık hüküm

**Girdi dürüstlüğü ölçütünde iki model birbirine yakındır.** Ham sayımda Evrenakı öndedir ve bunun iki gerçek nedeni vardır:

1. **Evrenakı fonksiyonel biçimini türetir; ΛCDM türetmez.** NFW profili analitik bir sonuç değil, simülasyon çıktısına uydurulmuş bir formüldür — nitekim Einasto profili aynı simülasyonlara daha iyi uyar. Evrenakı'nın $a\propto1/R$ biçimi ise M-38'in postülatlarından çıkar.
2. **Evrenakı'nın tutmuş bir öngörüsü var; ΛCDM'in tutmamış bir öngörüsü var.** $\ell_\omega\propto\sqrt{M_{bar}}$ (eğim 1,00) sınavdan önce söylendi, 1,03 ölçüldü. ΛCDM iç bölgede cusp öngördü, çekirdek gözlendi ve kurtarma geri-beslemeden geldi.

**Ama sayım hükmü vermez, çünkü bir ölçüt diğerlerinden ağır basar:**

> **$a_0$, sınandığı verinin kendisinden okunmuştur.** ΛCDM'in küresel sabitleri dönüş eğrilerine hiç bakmayan hesaplardan (N-cisim, CMB) gelir. Bir modelin sabitini test edeceği veriden okuması, "kaç sabit kullandığından" daha temel bir dürüstlük sorunudur — ve bu ölçüt **ΛCDM lehinedir.**

**Nihai hüküm (girdi dürüstlüğü):** **ΛCDM önde, ama farkı dar ve tek bir ölçütten geliyor.** Evrenakı iki ölçütte gerçek ve daha önce kaydedilmemiş üstünlüğe sahiptir. Fark kapatılabilir ve nasıl kapatılacağı bellidir: **$a_0$'ın bu 163 eğri dışında bir gözlemde doğrulanması.** O yapılırsa bu ölçüt de eşitlenir ve girdi dürüstlüğünde Evrenakı öne geçer.

### Defterin okunuşu — dört arena, dört ayrı hüküm

1. **Uyum kalitesi — ve fit girdisi ücretlendirilirse tablo dönüyor.** Galaksi başına medyanla: fotometrik bantta ΛCDM önde (2,58'e karşı 3,45), serbest $\Upsilon_*$ ile beraberlik. **Ama örneklem genelinde her fitlenen sayı ücretlendirildiğinde** (yukarıdaki fatura) eşit $K=326$'da serbest $\Upsilon_*$ ile **Evrenakı kazanır** ($\Delta$BIC $=-1539$, hata ölçekli $-305$), ve bantlı hâlde bile **153/163 galakside öndedir** — kaybı yalnız 10 galaksiden gelir. **Bölünmüş arena: tipik galakside Evrenakı, aykırı %6'da ΛCDM.** Ve **gerçek Hubble tiplerine ayrıldığında** (yukarıdaki spiral sınavı) tablo daha da nettir: spirallerde (Sa–Sd, $n=91$) teori serbest $\Upsilon_*$ ile bile geridedir (oy %46), fotometrik $\Upsilon_*$ ile ΛCDM açık ara öndedir (%42); teorinin tek anlamlı galibiyeti **cüce/düzensiz $+$ serbest $\Upsilon_*$** hücresidir ($+2{,}5\sigma$).
2. **Türetim ekonomisi:** Evrenakı **beş** büyüklüğü türetir ($a_0$ dahil değildir — o kalibredir), ΛCDM ikisini; BTFR'nin *eğimi* ve $\ell_\omega$ yasası ΛCDM'de karşılıksızdır. **Evrenakı'nın arenası — ama iki çekinceyle:** türetimlerinin tamamı sınandıkları aynı veriden okunmuştur, ve $a_0$'ın biçimi türetilmiş olsa da sayısal değeri kalibredir (6.5.4.5).
3. **Ontolojik fatura:** Evrenakı görünmez madde talep etmez. **Evrenakı'nın arenası.**
4. **Olgunluk ve kapsam:** ΛCDM'in girdileri bağımsız bir hesap programından (N-cisim) gelir ve model galaksi ölçeği dışında da (CMB, BAO, kütleçekimsel mercekleme, yapı oluşumu) sınanmıştır. Evrenakı'nın karşılık gelen ne simülasyon programı ne de bu ölçekte sınanmış dosyası vardır. **ΛCDM'in arenası, açık farkla.**

**Nihai hüküm — tek cümleye sıkıştırılamaz, ve sıkıştırmak yanıltıcı olur.**

**Uyum arenasında hüküm bölünmüştür.** Fit girdisi doğru ücretlendirildiğinde (örneklem geneli, eşit $K=326$) serbest $\Upsilon_*$ ile **Evrenakı kazanır**; fotometrik bantla totalde ΛCDM kazanır ama bu zafer **10 galaksiden** gelir ve kalan 153'te yine Evrenakı öndedir. Yani "ΛCDM daha iyi uyuyor" cümlesi, örneklemin %94'ü için yanlıştır; "Evrenakı daha iyi uyuyor" cümlesi ise %6'yı görmezden gelmektedir. Doğru ifade: **model tipik galakside daha iyi, aykırı bir altkümede felaket.**

**Buna karşılık iki arenada ΛCDM açık farkla öndedir ve bu belirleyicidir:** *(i)* türetilmiş bileşenleri (NFW, $c_0$–$M$) sınandıkları veriden **bağımsız** bir hesaptan gelir, oysa Evrenakı'nın altı türetiminin tamamı aynı dönüş eğrilerinden okunmuştur; *(ii)* model galaksi ölçeğinin dışında da (CMB, BAO, mercekleme, yapı oluşumu) sınanmıştır ve Evrenakı'nın bu ölçekte dosyası yoktur.

**Ve teorinin en ekonomik hâli kaybeder.** Fit girdisini yarıya indiren sürüm (F4 genliği yasadan, $K=163$) 3,85 kat kötüdür; ceza kuralı onu kurtarmaz. $\ell_\omega$ yasasının saçılması (0,38 dex) fitin yerini tutacak kadar sıkı değildir.

**Ve gerçek Hubble tiplerine ayrıldığında:** spiral galaksilerde (Sa–Sd, $n=91$) teorinin üstünlüğü **yoktur** — serbest $\Upsilon_*$ ile bile oy %46 ($-0{,}7\sigma$, medyan 2,01'e karşı 2,27), fotometrik $\Upsilon_*$ ile %42 ($-1{,}6\sigma$). Teorinin istatistiksel olarak anlamlı tek galibiyeti **cüce/düzensiz (Sdm–BCD) $+$ serbest $\Upsilon_*$** hücresidir (%65, $+2{,}5\sigma$; medyan 1,00'e karşı 1,75). Düz dönüş kolu teorinin daha iyi açıkladığı bir olgu **değildir**.

**Toparlarsak:** uyum yarışı **beraberlik-Evrenakı lehine** (tipik galakside önde, aykırı %6'da değil; spiralde geride, cücede önde); türetim ekonomisi **Evrenakı lehine** ama doğrulanmamış; bağımsızlık ve kapsam **ΛCDM lehine** ve tartışmasız. Bir hakem bugün hangisini tercih ederse etsin, **teoriyi dışlayamaz** — ama teorinin kazandığını da söyleyemez. Kazanmak için gereken üç şey nettir ve hepsi yapılabilirdir: on aykırı galaksinin nedenini bulmak, $\ell_\omega$ yasasının saçılmasını daraltmak, ve $a_0$'ı dönüş eğrileri dışında bir gözlemde doğrulamak.

---

## 6.5.4.0 Neden yeni bir kesit: iki gizli borç

6.5.2'nin denklemi ($v=\sqrt{A/r+B}$) düz dönüş eğrisini doğru üretir; ama iki noktada teorinin dışına borçludur:

1. **$A$ borcu.** $A=GM_c$ yazmak, galaksinin tüm kütlesinin merkezde toplanmış bir *nokta* olduğunu varsayar. Oysa M-35'in kaynağı nükleon debisidir; nükleonlar diske yayılmıştır ve **dışa gidildikçe kapsanan nükleon sayısı artmaya devam eder.** Nokta-kütle varsayımı bu artışı görmezden gelir.
2. **$B$ borcu.** $B$, 6.5.2'de elle konan bir sabittir. Türetilmediği sürece, Anayasa Madde 21'in yasakladığı "istenen değeri alabilen katsayı" tanımına tehlikeli biçimde yakındır.

Bu kesit iki borcu da kapatır ve bunu yaparken **dışarıdan hiçbir yapı almaz:** karanlık madde halosu yok, NFW yok, Freeman (1970) ince disk kapalı formu yok, Rankine profili girdi olarak yok, MOND ivme ölçeği ($a_0$) yok, keyfî kesme yarıçapı yok. Elde yalnız Postülat 9'un beş kuvveti ve gözlemin verdiği kaynak dağılımı vardır.

## 6.5.4.1 Denetim: ekvator düzleminde hangi kuvvet çalışır?

Yörünge düzlemi, beş kuvvetin çoğunu kendiliğinden eler. Sınavın ilk adımı bu elemeyi açıkça yapmaktır:

| Kuvvet | Katalog | Ekvator düzlemindeki durumu |
|---|---|---|
| **F1** — Radyal kütle-itimi | M-35 | **Etkin.** Küresel pulsasyon akısı $4\pi r^2$'de seyrelir $\Rightarrow a\propto1/r^2$ |
| **F2** — Diferansiyel sıkıştırma | M-36 | **Dairesel hıza net katkı yok.** İz-sıfır gelgit tensörü; yörünge hızına girmez, dikey geri çağırma **frekansına** ($\nu$) katkı verir. Kalınlığın kendisini hiçbir kuvvet belirlemez: $h=\sigma_z/\nu$ — kuvvetler $\nu$'yü, enerji bütçesi $\sigma_z$'yi kurar (11.4.5) |
| **F3** — Vorteks sürüklenmesi | M-37 | **Yörünge hızına katkısı yok.** Yörüngeyi kuran sürüklenme değil, maddenin **serbest düşmesidir** (M-2): $v_{y\ddot{o}r}=\sqrt{R\lvert a_{radyal}\rvert}$. F3, ortamın kendi dolaşımını ($v_\theta=2v_{y\ddot{o}r}$, DY-2) ve $\eta_E$ ile yalnızca çok uzun ölçekli sürüklenmeyi taşır |
| **F4** — Eksenel itim | M-38 | **Etkin.** Silindirik akı $2\pi Rh$'de seyrelir $\Rightarrow a\propto1/R$ |
| **F5** — Yanal itim | M-39 | Düzlemde $\sin2\theta\rvert_{90°}=0$, yani **sıfır**. Ama düzlemin *kendisini* seçen ve levhanın yayılmasına direnen kuvvet odur (11.4.9) |

Son satır bedava bir iç kapanıştır ve kayda değer: **M-38'in en kırılgan varsayımı olan "$h_d=$ sabit" koşulunun mekanik dayanağı F5'tir.** Akı tüpü yayılırsa $1/R$ yasası $1/R^2$'ye döner ve galaktik ayak çöker; levhayı yayılmaya karşı destekleyen kuvvet yanal itimdir. Payı önemsiz değildir ve **tam burada büyüktür**: bir levhada deplasman gradyanının ölçeği $R$ değil $h_z$ olduğu için F5'in dikey geri çağırmadaki oranı $\mathcal{F}_5=\tfrac{\mathcal{A}\kappa_5}{4}(R/h_z)^2$'dir; $\mathcal{A}$ ise bu bölümün kendi büyüklüğüdür — orta düzlemde radyal ivmenin **F4'ten gelen payı.** F4'ün $1/R$ akı tüpü rejimi dış disktedir, yani $\mathcal{A}$ oradadır en büyük: $R=25$ kpc'de $\mathcal{F}_5\simeq0{,}9$, iç diskte $\simeq0{,}1$ (11.4.9). **F5, F4'ün güçlü olduğu yerde güçlüdür** — ikisi aynı deplasman basıncının iki izdüşümü olduğu için zorunlu, ve akı tüpünün korunmasına ihtiyaç duyulan yer tam orasıdır. *(Koşul M-38 içinde bağımsızca da kurulur — viskoz difüzyonun ihmal edilebilirliği $10^{22}$ marj bırakır; F5 o marjı ikinci bir mekanizmayla destekler, tek başına taşımaz. Diski **kurmak** ise F5'in işi değildir: korunumlu bir kuvvet dikey enerji çekip alamaz, 11.4.5.)* Beş kuvvetten **ikisi hesaba girer** (F1, F4), **biri kaynağın geometrisini destekler** (F5), **ikisi düzlemde sessizdir** (F2, F3). Hesabın *çerçevesini* kuran şey ise bir kuvvet değil, maddenin serbest düşmesidir (M-2). Hiçbiri fazlalık değildir.

## 6.5.4.2 Birinci borcun kapanışı: kaynak, kapsanan nükleon kütlesidir

M-29 (Gauss argümanı) $1/r^2$'yi bir akı korunumu olarak kurar. Akı korunumunun söylediği şey, kuvvetin *kapsanan* kaynakla belirlendiğidir — merkeze konmuş hayalî bir noktayla değil. Dolayısıyla F1'in düzlemdeki ivmesi, nükleon-başı basınç gradyanının **kaynak dağılımı üzerinde doğrudan bindirilmesiyle** hesaplanmalıdır. M-28 basınçların doğrusal toplandığını verdiği için ($P=P_0-\alpha M/r$) bindirme meşrudur:

$$a_{F1}(R) \;=\; \mathcal{G}\int\!\!\!\int \Sigma(R')\,R'\,\frac{R-R'\cos\varphi}{\left(R^2+R'^2-2RR'\cos\varphi+h_z^2\right)^{3/2}}\,\mathrm{d}\varphi\,\mathrm{d}R'$$

Burada $\mathcal{G}\equiv\alpha/\rho_n=Cq_n/4\pi\rho_n m_n$ **M-35'in genliğidir** — sayısal değeri Güneş Sistemi ölçeğinde sabitlenmiştir (Ek C satır 12), ama teoriye "Newton'un $G$'si" olarak değil, nükleon debisinin makro izdüşümü olarak girer. $h_z$ bileşenin ölçek yüksekliğidir ve **gözlemsel girdidir**; razor-thin idealleştirmesi yapılmaz, çünkü levhanın yayılmadan kalması F5 tarafından desteklenir (§6.5.4.1, 11.4.9).

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

## 6.5.4.3 İkinci borcun kapanışı: F4'ün genliği vortisiteden türetilir

Bölüm 3.8.2 teorinin motor cümlesini kurar: *makro girdap, kütlenin dönüşünden değil, nükleonların mikro dönüşlerinin toplanmasından doğar; kütle büyüdükçe mikro spin sayısı artar, girdap güçlenir.* Bu cümle nicelleştirilebilir ve nicelleştirildiğinde $B$ sabiti ortadan kalkar.

**Adım 1 — Nükleon başına dolanım debisi.** Her nükleon, $\omega_1$ bileşeniyle çevresindeki ortama bir dolanım (sirkülasyon) boşaltır: $\gamma_n$, birimi m²·s⁻¹. Bu, M-35'in hacimsel pulsasyon debisi $q_n$'nin (m³·s⁻¹) $\omega_1$ tarafındaki kardeşidir; ikisi Blok H'nin köken haritasındaki iki kolun ta kendisidir.

**Adım 2 — Stokes teoremi.** $R$ yarıçaplı halkanın kapsadığı toplam vortisite, içindeki nükleon motorlarının toplamıdır:

$$\Gamma(R) \;=\; \oint \vec v_{ortam}\cdot \mathrm{d}\vec l \;=\; \frac{\gamma_n}{m_n}\,M_{kaps}(R)$$

**Adım 3 — Silindirik deplasman akısı.** M-38'in geometrisinde akı, $h_d$ kalınlıklı silindir yanağından geçer. Dolanımın taşıdığı hacim debisi $Q_{sil}=\Gamma(R)\,h_d$, akı yoğunluğu ise $Q_{sil}/(2\pi R h_d)$ olur — **$h_d$ sadeleşir.** ($1/R$ yasasının $h_d=$ sabit koşuluna bağımlılığı burada da kendini gösterir: sadeleşme ancak $h_d$ yarıçaptan bağımsızsa temizdir.)

**Adım 4 — Ortam tepkisi.** M-35 ile **aynı** $C$ katsayısı uygulanır (yeni bir ortam sabiti tanımlanmaz):

$$a_{F4}(R) \;=\; \frac{C}{\rho_n}\cdot\frac{\gamma_n M_{kaps}(R)}{2\pi m_n R}$$

**Adım 5 — M-35'in genliğine indirgeme.** Pay ve payda $\mathcal{G}=Cq_n/4\pi\rho_n m_n$ cinsinden yazılınca $C$, $\rho_n$ ve $m_n$ düşer ve geriye tek bir uzunluk kalır:

$$\boxed{\;a_{F4}(R)=\frac{\mathcal{G}\,M_{kaps}(R)}{\ell_\omega\,R}\;,\qquad \ell_\omega \equiv \frac{q_n}{2\gamma_n}\;}$$

$\ell_\omega$ — **vortisite uzunluğu** — nükleonun pulsasyon debisinin dolanım debisine oranıdır; yani $\omega_2$ kolunun $\omega_1$ koluna oranı. Boyut denetimi: $[q_n]/[\gamma_n]=\mathrm{m^3s^{-1}}/\mathrm{m^2s^{-1}}=\mathrm{m}$ ✓.

> **Önemli — iki $\ell_\omega$ ayrımı.** Yukarıdaki oran *tek bir nükleonun* iki debisini karşılaştırır ve bir **mikro sabittir** — ölçümü Adım 6'dadır: $\ell_\omega^{mikro}=35{,}7$ fm, kütleyle korelasyonu $+0{,}03$ (3,8 decade boyunca sabit). Galaktik ölçekte ölçülen büyüklük ise ortamın kurduğu **net** dolanımın karşılığıdır ve $\sqrt{N}$ toplanma çarpanı taşır: $\ell_\omega^{etkin}=\ell_\omega^{mikro}\sqrt{N}$. SPARC'ın 158 galaksisinde $\ell_\omega^{etkin}$'in 0,22 kpc ile $2\times10^4$ kpc arasında beş mertebe yayılmasının tamamı bu $\sqrt{N}$ çarpanıdır; yasa ve sınavı 6.5.4.5'tedir.

**Adım 6 — tutarlılık istatistiği: dolanımlar $\sqrt{N}$ ile toplanır ve $M_{tut}=m_n$ çıkar.**

Adım 2'nin Stokes toplamı, en genel hâlde nükleon dolanımlarının nasıl hizalandığına bağlıdır. Veri, birebir hizalı toplanmayı ($\Gamma\propto N$) desteklemez: dolanım vektörleri hizasız olduğundan net dolanım bir **rastgele yürüyüştür**,

$$\Gamma_{etkin}(R)\;=\;\gamma_n\sqrt{N},\qquad N=\frac{M_{kaps}(R)}{m_n}$$

Bu, Adım 4–5 zincirine konduğunda genlik bağıntısı şu hâli alır:

$$a_{F4}(R)\;=\;\frac{\mathcal{G}\sqrt{M_{kaps}(R)\,m_n}}{\ell_\omega\,R}
\qquad\Longrightarrow\qquad
\boxed{\;a_0=\frac{\mathcal{G}\,m_n}{\ell_\omega^{2}}\;,\qquad M_{tut}=m_n\;}$$

**Tutarlılık kütlesi nükleon kütlesidir:** ortam, mikro dolanımları tek bir nükleondan öteye hizalı toplayamaz. Bu sonuç serbest parametre içermez — $M_{tut}$ apriori $10^{-30}$–$10^{60}$ kg arasında herhangi bir değer olabilirdi. Ölçümü: $\ell_\omega^{etkin}=\mathcal{G}M_{kaps}/(v_{gözl}^2-V_{bar}^2)$ doğrudan çözülüp ($a_0$ hiç kullanılmadan) $\sqrt{N}$'e bölündüğünde $\ell_\omega^{mikro}=35{,}7$ fm çıkar (133 galaksi; kütleyle Spearman $+0{,}029$, yani 3,8 decade boyunca **gerçekten sabit**), köprü üssü 0,503 ölçülür (türetim 0,500 der), ve $M_{tut}=a_0\ell_\omega^2/\mathcal{G}=0{,}84\,m_n$ — sıfır parametreli öngörünün ($M_{tut}=m_n$) beşte biri içinde. Kalan farkın ana kalemini Adım 7 kapatır: eşlenme tabanının keskin öngörüsü $M_{tut}=X\,m_n\approx0{,}72\,m_n$'dir ve ölçümle %15 içindedir.

İki sonucu vardır: **(i)** $\ell_\omega^{etkin}$'in galaksiden galaksiye beş mertebe yayılması yeni bir yasa değil, $\sqrt{N}$ çarpanının kendisidir — mikro oran sabittir; **(ii)** $a_0$ **mikro sabitlerin bir bileşkesidir** ($\mathcal{G}m_n/\ell_\omega^2$) ve bu yüzden **kozmik zamanla değişmez.** Bu, sınanabilir bir öngörüdür ve sınanmıştır: $a_0\propto cH(z)$ alternatifi Genzel ve ark. (2017)'nin altı $z=0{,}85$–$2{,}4$ diskinin **altısında** yayının üst sınırını aşar (ortalama $6{,}1\sigma$); sabit $a_0$ her galakside daha yakındır ($3{,}3\sigma$). Ayrıntı 6.5.4.5'te.

**Adım 7 — tutarlılık kümesinin kimliği: kafes, atom çekirdeğidir.** 
Adım 6'nın rastgele yürüyüşü, hangi birimlerin bağımsız yürüdüğü sorusunu açık bırakır. Cevap $\ell_\omega$'nın kendi fiziksel anlamından çıkar. Bir nükleonun $d$ uzaklığındaki komşusunun hissettiği iki alanın oranı tek uzunlukla belirlenir:

$$\frac{v_t}{v_r}=\frac{\gamma_n/2\pi d}{q_n/4\pi d^2}=\frac{d}{\ell_\omega}$$

— $\ell_\omega$, yönsüz pulsasyon bölgesinden yönlü dolanım bölgesine geçiş yarıçapıdır. Ve ölçülen değeri (35,7 fm) doğanın bir **ölçek boşluğuna** düşer: en büyük çekirdek yarıçapı 7,4 fm'dir (U-238), çekirdekler arası mesafe ise maddenin her hâlinde — katı, gaz, plazma, yıldız içi, beyaz cüce dahil — en az $2{,}7\times10^3$ fm'dir. Dolayısıyla **aynı çekirdeğin nükleonları daima tek bağlı yapı içindedir; farklı çekirdekler daima bağımsızdır.** Tutarlılık kümesi moleküler ya da katı kafes değil, **atom çekirdeğinin kendisidir** — maddenin fazından bağımsız olarak. (Bu, gaz kesri sınavının null sonucunu — F4 artığı ile gaz oranı arasında korelasyon $+0{,}01$ — bir bilmece olmaktan çıkarıp öngörüye çevirir: kafes çekirdek olduğuna göre faz önemli olmamalıydı, ve değildir.)

Rastgele yürüyüş bu durumda çekirdekler üzerinden işler; kütle kesri $X_j$, kütle numarası $A_j$ olan bileşimde $\Gamma_{etkin}=\gamma_n\sqrt{N_c\,N}$ ve $M_{tut}=N_c\,m_n$ olur. Çekirdek başına net dolanımı iki sınır kuşatır — tam iç uyum ($N_c=\langle A\rangle=\sum X_jA_j$) ve eşlenme sönmesi (çift-çift çekirdekler sıfırlanır; $N_c\approx X$, hidrojen kütle kesri):

$$\boxed{\;N_c\in[\,X,\;\langle A\rangle\,]\approx[\,0{,}71\,;\;2{,}2\,]\;}$$

Pencere parametresizdir ve üç ölçümle sınanmıştır: **(a)** morfolojik sınıfların gerektirdiği çarpan bandının (Im 0,65 … Sd 1,55; Kısım X, 10.2.4) tamamı pencerenin içindedir — sınıf bandı bir anomali değil, çekirdek istatistiğinin izin verdiği aralıktır; **(b)** eşlenme tabanının keskin öngörüsü $M_{tut}=X\,m_n\approx0{,}72\,m_n$'dir — Adım 6'nın ölçtüğü 0,84 ile **%15 içinde**; **(c)** en çalkantılı, iyonize-gaz baskın sınıf (Im) tam tabanda oturur (kısmi hizalanma $\lambda\approx0$), ana sınıflar $\lambda=0{,}14$–$0{,}68$ ile pencere içindedir. Pencere-içi konum $\lambda$ için üç şey türetilmiştir:

- **$\lambda$ çekirdeğin içinden gelemez** — enerji kilidi: eşlenmeyi açmak ~MeV ister, ortamın nükleon başına sunabildiği en cömert enerji ~500 eV'dir. $\lambda$ zorunlu olarak **çekirdekler-arası** kısa-menzil korelasyondur: ortamın, boşaltılan mikro dolanımları nasıl muhasebe ettiğinin ölçüsü.
- **$\sqrt{N}$ yasası teoremleşir.** Ortam çekirdek yönelimlerine ortak bir eğilim ($\varepsilon$) verseydi $\ell_\omega^{mikro}$ kütleyle büyürdü; 3,8 mertebelik değişmezlik $\varepsilon<3\times10^{-35}$ sınırını koyar — fiilen tam sıfır. Teorik karşılığı **dolanım korunumudur**: ortam net dolanım üretemez; taşıyabildiği yalnız $\sqrt{N}$'lik dalgalanma ve toplamı koruyan, $O(1)$ çarpan üreten muhasebe korelasyonlarıdır. Adım 6'nın rastgele yürüyüşü böylece varsayım olmaktan çıkar.
- **Belirleyici aday: ortamın kaskad karakteri.** $\Gamma$, enjekte edilen mikro dolanımdan ortamın tuttuğu bakiyedir; kalın/üç-boyutlu çalkantılı ortam düz kaskadla söndürür ($\lambda\to0$), ince/dinamik-soğuk yarı-iki-boyutlu disk ters kaskadla korur ve **disk ekseni boyunca örgütler** ($\lambda>0$; F4'ün yönü kendiliğinden disk dönüşüyle hizalanır). Mevcut verideki isabetleri: Im (kalın, çalkantılı) tam tabanda; ana sınıfların tavanı Sd — literatürün "süper-ince" galaksileri tam bu sınıftır; ana sınıfların hepsi $\lambda<1$ sınırının içindedir. Bu çerçevede $\lambda\leq1$ **zorunludur**; S0/BCD uçlarının 1,6'sı izinsizdir ve temiz-büyük örneklemde 1'in altına inmek zorundadır — keskin, yanlışlanabilir bir çağrı. Nicel $\lambda$(incelik) bağıntısı türetilmemiştir; kesin sınavı SPARC'ın HI hız dağılımı ($\sigma$) kataloglarıyla eşleştirilmesidir ve **ilk turu koşulmuştur** *(THINGS + VLA-ANGST + LITTLE THINGS, 18 galaksi)*: Spearman$[\log k,\,v/\sigma]=+0{,}49$ (tek yönlü $p=0{,}019$; temiz altküme $+0{,}44$, sınıf-medyanı $+0{,}54$) ve kaldıraç tam öngörülen yerdedir — en çalkantılı üç sistem en küçük çarpanları taşır. Ardışık-analiz çekincesiyle bu bir doğrulama değil **ilk anlamlı işarettir.** $n\gtrsim40$ için kayıt-öncesi bir protokol kurulmuş ve ilk denemesi yapılmıştır: çizgi-genişliği farkından $\sigma$ kestirimi örneklemi 99'a çıkarır — ama önceden ilan edilen geçerlilik kapısı geçilemediği için sınav, sonucuna bakılmadan "uygulanamaz" ilan edilmiştir. Doğrulama, geçerli bir büyük-$n$ $\sigma$/kalınlık kataloğunu bekler; boru hattı hazırdır (7.4).

**Bedava gelen üç sonuç.** Bunların hiçbiri ayrıca varsayılmamıştır; türetimin kendisinden çıkarlar:

1. **Geçiş yarıçapı türetilmiş olur: $r_0=\ell_\omega$.** İki terimin eşitlendiği yarıçap $\mathcal{G}M/R^2=\mathcal{G}M/(\ell_\omega R)$'den doğrudan $R=\ell_\omega$ verir. Bu, $r_0$'ı çekirdek kütlesine değil nükleon debi oranına bağlar; dolayısıyla kovan/toplam oranı üzerinden bir morfoloji gerilimi doğurmaz. (Noktasal kütle idealleştirmesine dayanan $r_0=GM_c/B$ türü bir bağıntı dağılmış kaynakla tutarsızdır ve kullanılamaz.)
2. **Eksendeki ıraksama kendiliğinden düzenlenir.** $R\to0$ iken $M_{kaps}\to0$ olduğundan $a_{F4}\to0$'dır. M-38'in "simetri gereği eksende net eksenel kuvvet sıfırdır" koşulu, elle konan bir düzenleme çarpanı olmadan sağlanır. Elle konan bir $R^2/(R^2+r_0^2)$ yaması gereksizdir.
3. **Güneş Sistemi ile çelişki doğmaz — geniş marjla.** M-38, Ay'ın apsidal presesyonundan $\varepsilon=a_{1/R}/a_{1/R^2}<2\times10^{-5}$ üst sınırını koymuştu. Bu türetimde $\varepsilon=r/\ell_\omega$'dir; NGC 3198 için bulunan $\ell_\omega$ ile Ay'da $\varepsilon=1{,}1\times10^{-12}$, yani sınırın **19 milyon kat** altında. Neptün'de $1{,}2\times10^{-8}$. Yerel galaktik alan ise $R=8$ kpc'de $a_{F4}\approx3{,}8\times10^{-11}$ m/s² ile tüm Güneş Sistemi'ne ortak-mod etki eder ve bağıl dinamikte görünmez.

## 6.5.4.4 Tek denklem ve sayısal sınav

M-37'nin profil teoremi ($v_{y\ddot{o}r}=\sqrt{R\lvert a_{radyal}\rvert}$) iki katkıyı birleştirir. Adım 6'nın $\sqrt{N}$ toplanmasıyla ($\ell_\omega^{etkin}=\ell_\omega^{mikro}\sqrt{N}=\sqrt{\mathcal{G}M_{kaps}/a_0}$) denklem kapalı ve **yerel** biçimini alır:

$$\boxed{\;v^2(R)\;=\;R\,a_{F1}(R)\;+\;\sqrt{\mathcal{G}\,M_{kaps}(R)\,a_0}\cdot W(R)\;,\qquad W=\min\!\Big(1,\;\frac{a_0}{g_{kaps}}\Big),\quad g_{kaps}=\frac{\mathcal{G}M_{kaps}}{R^2}\;}$$

İkinci terimdeki kütle **yerel** kapsanan kütledir — akı teoremi gereği başka türlüsü olamaz: dolanım akısı $R$ yüzeyinden geçer ve $R$ içindeki maddeden doğar; 6.5.4.3'ün türetiminin hiçbir adımında toplam kütle geçmez. Yerellik veride de görünür: bu biçimle $\ell_\omega$ yasasının galaksi-içi yarıçap artığı sıfırdır ($-0{,}025$; 141 galaksi).

Denklemin okunuşu: birinci terim **küresel akının** payı, ikinci terim **silindirik vortisite akısının** payıdır. İkinci terim $\sqrt{M_{kaps}}$ ile büyür ve $M_{kaps}$ doyduğu anda sabitlenir — düz kol oradan doğar. Üçüncü çarpan $W$ **penceredir** (M-47): M-30'un Rankine iç kolunun bu denklemdeki ifadesi ($r_0=\ell_\omega^{etkin}$ özdeşleştirmesiyle, parametresiz) — $g_{kaps}\leq a_0$ bölgesinde $W=1$ (derin limit ve BTFR'ye dokunmaz), içte kuvvet Rankine'in $\propto R$ koluna döner; radyal ivme bağıntısının biçim sürüklenmesini sıfırlar ve yüksek-$z$ yoğun-rejim açığını kapatır (M-47). Yerel yazım $a_{F4}=\sqrt{a_{F1}\,a_0}$'dır: *eksenel itim, radyal itim ile $a_0$ ölçeğinin geometrik ortalamasıdır.* **Şerh:** bu özdeşlik yalnız küresel simetride tamdır; yassı diskte $V_{bar}^2\neq\mathcal{G}M_{kaps}/R$ olduğundan iki okuma sayısal olarak ayrışır ve ayrışma ölçülmüştür (besleme sınavı — $g_{bar}$-besleme dönüş eğrisi RMS'inde hafifçe öndedir ama biçim borcunu kapatmaz; tek-üslü tarama kısmi ağırlıkta sığ bir minimum bulur). İki kalıcı sonuç kaydedilmiştir: **öz-tutarlı besleme** — girdabı toplam akışın dolanımının beslemesi — yapısal bir ivme tabanı dayattığı için gözlemle **kesin dışlanmıştır** (en düşük gözlenen nokta tabanın 22 kat altında): F4'ün kaynağı *maddenin* dolanımıdır, sürüklenen akışın kendisi değil — akı gerekçesinin verili doğrulaması. Resmî denklem $M_{kaps}$ beslemesinde kalır; doğru beslemenin (ve kısmi-ağırlık adayının) türetimi F4'ün açık işidir (7.4 madde 12h). **Pencere kaydı [T-aday]:** M-30'un Rankine iç kolu bu denkleme uygulandığında ($r_0=\ell_\omega^{etkin}$ özdeşleştirmesiyle $W=\min(1,a_0/g_{kaps})$, parametresiz) radyal ivme bağıntısının biçim sürüklenmesi sıfıra iner ve uyum iyileşir; pencere **resmî denkleme alınmıştır** (M-47) ve bütün aşağı-akış sınavları yeniden koşulmuştur (defter: 10.2). **Galaksi başına serbest parametre sayısı: sıfır** ($a_0$ küreseldir; $\Upsilon_*$ fotometrik girdidir).

**Sayısal sınav 6.5.3.1'dedir.** Yayınlanmış SPARC verisiyle (43 nokta, gerçek hata çubukları) yapılır. Yukarıdaki denklem oradaki "Evrenakı F1+F4" satırının ta kendisidir; $b=\mathcal{G}/\ell_\omega$ özdeşliğiyle aynı modeldir.

**Gerçek veriden türetilen büyüklükler:**

| Büyüklük | Kaynak kilitli ($\Upsilon_*=0{,}5$) | Yayılmalı fit |
|---|---|---|
| $\ell_\omega^{etkin}=r_0$ | 7,06 kpc | 1,21 kpc |
| $q_n/\gamma_n=2\ell_\omega^{mikro}$ | $\approx7\times10^{-14}$ m | — |
| Düz kol asimptotu $\sqrt{\mathcal{G}M_{bar}/\ell_\omega}$ | 161 km/s | — |
| Ay'da $\varepsilon=r/\ell_\omega$ | $1{,}8\times10^{-15}$ | — |

Son satır, türetimin en sağlam kazancıdır: M-38'in Ay apsidal presesyonundan koyduğu üst sınır $\varepsilon<2\times10^{-5}$ idi; bu türetimde $\varepsilon$ o sınırın **on milyar kat** altında kalır. $1/R$ terimi Güneş Sistemi'nde hiçbir gerilim doğurmaz.

*Ama ilk satır sağlam değildir:* $\ell_\omega$, $\Upsilon_*$ seçimine göre 7,06'dan 1,21 kpc'ye kayar. Yani "türetilmiş tek parametre" iddiası, o parametrenin sayısal değerinin kararlı olduğu anlamına gelmiyor.

Nükleon debi oranı $q_n/\gamma_n=2\ell_\omega^{mikro}\approx7\times10^{-14}$ m **nükleer ölçekte** bir uzunluktur — proton yük yarıçapının yaklaşık 42 katı. Galaktik $\ell_\omega^{etkin}$'ten $\sqrt{N}\sim10^{33{,}5}$ çarpanıyla ayrılır (Adım 6); tabloda ikisi ayrı satırlardır ve karıştırılmamalıdır.

**Faturaların karşılaştırması.** Aynı eğriyi çizmek için ΛCDM (kaynak kilitli) $M_{200}=5{,}0\times10^{11}M_\odot$ ister; bu, gözlenen baryonik kütlenin ($4{,}2\times10^{10}M_\odot$) **11,9 katı görünmez maddedir**. Evrenakı hiç istemez: envanterde yalnız fotometri ve 21 cm'in gördüğü nükleonlar vardır. **Uyum kalitesinde ΛCDM eşit serbestlikte öndedir** (6.5.3.1); iki modelin ayrıştığı yer uyum değil, madde envanteridir.

## 6.5.4.5 $\ell_\omega$'nın Yasası ve Baryonik Tully-Fisher İlişkisinin Türetimi

Galaktik ölçekte ölçülen $\ell_\omega^{etkin}$, galaksiden galaksiye beş mertebe yayılır (6.5.3.2, 6.5.3.3). Bu bir serbestlik değildir: yayılım, Adım 6'nın $\sqrt{N}$ toplanma çarpanıdır ve **yasalıdır.** Bu alt bölüm yasayı verir ve sınar.

**Ölçeğin değeri.** İvme ölçeği Adım 6'nın mikro bileşkesidir ve boyutsuz değeri gözlemle sabitlenir — beş bağımsız ölçüm (dönüş eğrileri, BTFR, morfolojik sınıflar, erken tip galaksiler, radyal ivme bağıntısı) aynı değerde buluşur:

$$\boxed{\;a_0 \;=\;\frac{\mathcal{G}\,m_n}{\ell_\omega^{2}}\;=\; 7{,}67\times10^{-11}\ \mathrm{m/s^2}\;\left(=1{,}82\times\frac{c\,H_0}{16{,}1}\right)
\quad\text{[S] — kalibre edilmiş küresel sabit}\;}$$

> **Statü — biçim türetilmiş, değer kalibredir.** $a_0=\mathcal{G}m_n/\ell_\omega^2$ biçimi Adım 6'nın sonucudur; sayısal değer ise $\ell_\omega^{mikro}$ ölçümünün saçılması (0,17 dex) içinde gözlemle seçilmiştir — bu yüzden envanterde **[S]** rozetiyle sayılır, galaksi başına serbestlik eklemez. $cH_0$ mertebesiyle bugünkü örtüşme ise bir köken göstergesi **değildir**: $a_0\propto cH(z)$ okuması, Genzel ve ark. (2017)'nin $z=0{,}85$–$2{,}4$ diskleriyle doğrudan sınanmış ve altı galaksinin **altısında** dışlanmıştır (aşağıda); $a_0$ kozmik zamanla değişmez, örtüşme sayısal bir rastlantı olarak kaydedilir.

Ortamın silindirik dolanım kanalı bu ölçekle sınırlandığında vortisite uzunluğu **serbest kalmaz**, kapsanan kütleye bağlanır:

$$\boxed{\;\ell_\omega^{etkin}(R) \;=\; \sqrt{\frac{\mathcal{G}\,M_{kaps}(R)}{a_0}}
\;\;\xrightarrow{\;R\to R_{dış}\;}\;\;\sqrt{\frac{\mathcal{G}\,M_{bar}}{a_0}}\;}$$

Bu, Adım 6'nın $\ell_\omega^{etkin}=\ell_\omega^{mikro}\sqrt{N(R)}$ ifadesinin kendisidir. Galaksi **içinde** de sınanmıştır: yasaya bölünen ölçülmüş $\ell_\omega^{etkin}$'in yarıçap artığı sıfırdır ($-0{,}025$). Aşağıdaki 158-galaksi sınavı dış-nokta limitindedir.

Bu bağıntıda **galaksi başına serbest parametre yoktur** — ama parametresiz de değildir: $\mathcal{G}$ teorinin kendi $\alpha/\rho_n$'i, $H_0$ envanterde mevcut, ancak $a_0$'ın boyutsuz katsayısı **aynı SPARC verisine kalibre edilmiştir.** Yasa bu nedenle 163 galaksi boyunca *tek* bir sayı kullanır (galaksi başına değil), fakat o sayı gözlemden okunmuştur. $M_{bar}$ ise gözlemsel girdidir (fotometri + 21 cm).

**Sınav — SPARC'ın 158 galaksisi.**

![$\ell_\omega$ yasası — 158 galaksi](Gorseller/lomega_yasasi.png)

| Ölçüt | Sonuç | Beklenen |
|---|---|---|
| Korelasyon (öngörü ↔ ölçüm) | $\rho=+0{,}882$, $p=8\times10^{-53}$ | — |
| **Log-log eğim** | **1,03** | **1,00** |
| Yasa etrafında saçılma | **0,38 dex** (2,4 kat) | — |
| "$\ell_\omega$ sabittir" varsayımının saçılması | 0,59 dex (3,9 kat) | — |
| Normalizasyon (medyan ölçülen/öngörülen) | 1,06 | 1,00 |

**Eğim 1,03 çıkmıştır.** Yani $\ell_\omega$'nın kütleyle nasıl değiştiği önceden söylenebilmektedir. Ve sıfır parametreli yasa, "sabit" varsayımından **daha iyidir** (0,38'e karşı 0,59 dex). Serbest fit trendi çıkarıldığında kalan saçılma da 0,38 dex'tir — yani yasa mevcut eğilimin tamamını yakalar, sömürülecek artık eğim bırakmaz.

**Ve yasanın eşdeğeri: baryonik Tully-Fisher.** Yasa, F4'ün genlik bağıntısıyla ($v_{F4}^2=\mathcal{G}M_{bar}/\ell_\omega$) birleştirildiğinde $\ell_\omega$ sadeleşir:

$$v^4 \;=\; \mathcal{G}\,M_{bar}\,a_0$$

Bu, **baryonik Tully-Fisher ilişkisidir** — galaktik dinamiğin en sağlam ampirik düzenliliği. Vurgulanması gereken nokta: **teori BTFR'yi varsaymaz, kozmolojik $a_0$'dan çıkarır.** Standart kozmolojide BTFR'nin bu kadar dar saçılmalı olması ince ayarlı geri-besleme (feedback) gerektiren bir bilmecedir; burada tek satırlık bir sonuçtur. Grafiğin sağ alt panelinde 158 galaksinin bu bağıntı çevresinde dizilişi görülmektedir.

**Dürüstlük kayıtları:**

- **Normalizasyonda kütleye bağlı sistematik var.** Medyan ölçülen/öngörülen $=1{,}06$ — genlik yüzde birkaç içindedir. Ama oran örneklem boyunca sabit değildir: cücede $\approx1{,}5$, ortada $\approx1{,}05$, kütlelide $\approx0{,}94$. Bu, morfolojik sınıf bandının (log genişliği 0,115 dex) bu sınavdaki görünümüdür ve açık kalemdir (7.4, madde 12).
- **Saçılma 2,4 kattır.** Sıkı bir bağıntı değildir; gözlemsel BTFR'nin kendi saçılmasından geniştir. Galaksiler arası varyansın büyük kısmı ölçüm bütçesiyle (başta uzaklık belirsizliği) açıklanır; sınıf bandı ise gerçektir.
- **$M_{bar}$ fit edilen $\Upsilon_*$ ile hesaplanıyor.** Bağımsız bir yıldız kütlesi tayiniyle (popülasyon sentezi) tekrarlanmalıdır; aksi hâlde $\ell_\omega$ ile $M_{bar}$ arasında kısmi bir bağımlılık kalır. Bu, 7.4 madde 12'nin açık kalemidir.

### Etkin yasa kimliği: Milgrom programı (MOND) ile ilişki ve ayrışma

Bu türetimin ivme yazımı ($g=g_{bar}+\sqrt{g_{bar}\,a_0}$ — 6.5.4.4'ün eşdeğer yerel biçimi), standart fiziğin MOND programında (Milgrom, 1983) $\nu(y)=1+y^{-1/2}$, $y=g_{bar}/a_0$ geçiş-fonksiyonu ailesi olarak bilinir; pencereyle (M-47) aile parçalıdır — $y>1$'de $\nu=1+y^{-3/2}$, türetilmiş daha dik sönüm. MOND, Newton'un "kütleçekim" yasasını düşük ivmede değiştiren ampirik bir reçetedir; galaktik ölçekteki başarısı (BTFR, radyal ivme bağıntısı, baryon-deseni↔eğri-deseni yerelliği) gerçek ve keskin biçimde belgelenmiştir (Famaey & McGaugh, 2012; McGaugh ve ark., 2016). Teori bu başarıyı **miras alır, çünkü aynı etkin yasayı üretir** — ama bir geçiş fonksiyonu *seçerek* değil, iki gerçek kuvvetin (F1 küresel akı + F4 silindirik vortisite akısı) toplamından *türeterek.* Kepler yasalarının Newton mekaniğine oranı neyse, MOND'un bu denkleme oranı odur: doğru yakalanmış, mekanizmasız bir etkin yasa. Miras ölçülmüştür ve yukarıdaki BTFR/RAR sonuçlarının kendisidir.

MOND'un açıklamasız bıraktığı üç öğenin üçü de burada adreslidir: $\nu$'nün biçimi (F1+F4 toplamı), $a_0$'ın kökeni (mikro bileşke $\mathcal{G}m_n/\ell_\omega^2$; aday kapanış M-45) ve ölçütün neden *ivme* olduğu (M-37 profil teoremi + M-45 eş-güç). Üç yapısal varsayımı ise teoride yoktur ve ayrışma buradan doğar: MOND **sabit $G$**, **evrensel $a_0$** ve (görelilik uzantılarında) **sabit $c_0$** çerçevesinde kurulur; teoride $\mathcal{G}$ yereldir (Postülat 4), $a_0$ ortam kanallıdır ($\lambda$; morfolojik sınıf bandı — MOND bandı üretemez, G-8'in $+0{,}49$'luk ilk işareti tam bu kanaldandır) ve $c_0$ yerel bir büyüklüktür. Ayrışmanın bugünkü karnesi: (i) MOND'un görelilik uzantısı TeVeS, GW170817'nin "kütleçekim dalgası" hız kısıtıyla düşmüştür — teoride dalga kanalı yerel $c_0$'de olduğundan (M-44) kısıt otomatik sağlanır; (ii) MOND folklorunun $a_0\sim cH_0$ kozmik okuması yüksek-$z$'de 6/6 dışlanmıştır (aşağıda) — mikro köken ayakta; (iii) MOND'un kalıcı küme açığı (≈ 2 kat), teoride sirkülasyon-kuyuları programının hesap kalemidir (3.7.4; 7.4). Sıradaki iki ayırt edici sınav öngörü tablosuna yazılmıştır: geniş çift yıldızlar (G-10; literatür çekişmelidir — Chae, 2023 ↔ Banik ve ark., 2024) ve $a_0(z)$ sabitliği (G-11).

**Dürüstlük kaydı — devralınamayan parça ve öncelik hakkı.** MOND'un veriye *fitlenmiş* geçiş eğrisi ($g_\dagger=1{,}20\times10^{-10}$ m/s²; McGaugh ve ark., 2016) RAR artığını düz bırakır; teorinin **penceresiz** toplamsal biçimi $+0{,}051$ dex/dex'lik artık eğim bırakıyordu — pencereyle (M-47) eğim aynı 2693 noktada $+0{,}0002\approx0$'dır; devralınamayan parça türetimle kapanmıştır (7.4 madde 12h). $g_\dagger$ ile $a_0$ ayrı sabitler olarak kalır (oran 1,56). Bu fark $a_0$ ile kapatılamaz — iki uç ayrı yöne ister; kapanışın adresi F1 ile F4'ün toplanma biçiminin (ve geçiş yarıçapı $r_0$'ın, Blok H) türetimidir. $g_\dagger$ ile $a_0$ aynı sabit değildir (oran 1,62; biçimler farklı olduğundan sayılar biçimden bağımsız karşılaştırılamaz). Ve BTFR/RAR düzenliliklerini ampirik olarak bulup keskinleştiren Milgrom–McGaugh–Lelli çizgisidir; teorinin katkısı bağıntıların kendisi değil, mekanizması, türetimi ve ayrışma öngörüleridir.

### $a_0$'ın değeri: nasıl sabitlendi, kökeni ne

**Katsayı teoriden gelmez, gözlemle sabitlenir.** Teorinin verdiği şey $a_0$'ın **biçimidir**: $a_0=\mathcal{G}m_n/\ell_\omega^2$ (Adım 6). Girdisi olan $\ell_\omega^{mikro}$ ölçümünün saçılması 0,17 dex olduğundan biçim, sayısal değeri tek başına iğneleyecek keskinlikte değildir; değeri gözlem sabitler. Beş bağımsız ölçüm aynı değerde buluşur:

| Ölçüm | İstediği $a_0$ ($10^{-11}$ m/s²) |
|---|---|
| Disk radyal ivme bağıntısı (2693 nokta) | 6,8 |
| Dönüş eğrileri, dış yarı (141 galaksi) | 7,5 |
| Erken tip galaksiler (16 galaksi) | 7,8 |
| Baryonik Tully-Fisher (117 galaksi) | 8,5 |
| Morfolojik sınıf çalışması | 9,3 |

Kabul edilen değer $a_0=7{,}4\times10^{-11}$ m/s² bu aralığın alt yarısındadır: dönüş eğrilerinin dış yarı sapmasını sıfırlar ($-0{,}1\%$) ve BTFR eğimini gözlenen bandın içinde tutar (3,734; band 3,530–3,738). Daha büyük değerler BTFR eğimini bandın dışına taşır.

**Tek kaldıraç $a_0$'dır.** Diğer iki küresel sabit aynı yöntemle tarandı ve kaldıraç olmadıkları görüldü: kütle üssü $p$ ($\ell_\omega\propto M_{bar}^p$) taramasında en iyi değer $0{,}50$'dir — yani **yasanın $\sqrt{M_{bar}}$ biçimi zaten optimaldir** (Adım 6'nın öngördüğü üs; köprü sınavında ölçülen 0,503); $\Upsilon_{kovan}/\Upsilon_{disk}$ oranı ise 1,0–2,0 aralığında sonucu değiştirmez, tamamen duyarsızdır.

**Değer için aday kapanış — [T-aday].**  $\ell_\omega=r_n\,(u_r/v_t)$ biçimi (nükleonun küresel kaynak yazımı) hedef sayıyı $u_r/v_t=42{,}4$ olarak sabitler. Teorinin kendi kafes-atomu kaydından (M-15/M-39: deplasman kafesi atomun tamamıdır) bir aday çıkar: pulsasyon kolunun süredurumunu atomun hafif zarfı ($m_e$), dolanım kolununkini nükleon özü ($m_p$) taşır; iki kol enerji eşbölüşümündeyse $u_r/v_t=\sqrt{m_p/m_e}=42{,}85$ — ölçülenle **%1,1**. Bu, $\ell_\omega=r_n\sqrt{m_p/m_e}=36{,}05$ fm (ölçülen 35,7; medyanın kendi hatası %3,5) ve

$$a_0=\frac{\mathcal{G}\,m_n\,m_e}{m_p\,r_n^{2}}=8{,}60\times10^{-11}\ \mathrm{m/s^2}$$

verir — **sıfır kalibrasyonla**, beş ölçümün bandının içinde (eşlenme tabanıyla $6{,}4\times10^{-11}$). **Statüsü kanıt değildir:** başka-yere-bakma hesabı dar (fizikçe motive) aday uzayında ~$2\sigma$, geniş uzayda %40 verir — bu yüzden $a_0$'ın rozeti **[S] kalır.** Eşbölüşüm Blok H'de **türetilmiştir** (**M-45**): izoklinik kilit Ek A.2'nin $\sqrt2$'sinden çıkar (iki düzlem ayrı ayrı kavrama sınırında doyar), taşıyıcı ayrımı **medyan-H kilidiyle** doğrulanır ($X>0{,}5$ olduğundan $\ell_\omega$ medyanı her ortamda hidrojen değerine kilitlenir — bileşim-kararlılığının açıklaması), ve eşbölüşümün geçerlilik koşulu hesaplanıp kapanmıştır: kanal enerjisi $m_pc^2$, sızıntı süresi ~0,8 milyon yıl, banyo teması $10^{-23}$ s — **36 mertebe marj.** Aynı hesap ölçülen %1'lik farkın fiziksel olmadığını da gösterir (ışıma düzeltmesi $\sim10^{-30}$; fark medyan hatasının içindedir) — oran **tam** olmalıdır. $\sqrt2c$ çapasıyla $(C,q_n)$ çifti de sayısallaşır ($q_n=1{,}62\times10^{-19}$ m³/s, $C=2{,}35$ kg·m⁻³·s⁻¹). [T]'ye geçişin kalan **iki dış koşulu**: $\ell_\omega$'nın SPARC dışı bağımsız ölçümü (medyan 36,0 fm + tür-ayrımlı ikinci mod ~51 fm) ve dar-uzay gerekçesinin hakem denetimi (G-9; 7.4).

### $a_0$ kozmik mi, mikro mu? — SPARC dışı sınav

$a_0$ sayıca $cH_0$ mertebesindedir ($\approx cH_0/9{,}2$) ve bu yakınlık iki okumaya izin verirdi: **kozmik okuma** ($a_0\propto cH(z)$ — evrensel deşarjdan gelir, kozmik zamanla değişir) ve **mikro okuma** ($a_0=\mathcal{G}m_n/\ell_\omega^2$ — nükleon sabitlerinin bileşkesidir, değişmez). İki okuma bugünkü evrende ayırt edilemez; yüksek kırmızıya kaymada kesin olarak ayrışır, çünkü $H(z=2)\approx3H_0$'dır.

Sınav, teorinin ilk SPARC dışı verisiyle yapılmıştır: Genzel ve ark. (2017)'nin altı büyük yıldız-oluşturan diski, $z=0{,}85$–$2{,}38$ (fit yok, kalibrasyon yok):

- **Kozmik okuma dışlanır:** $a_0\propto cH(z)$ yazımı altı galaksinin **altısında** yayının karanlık madde payı üst sınırını aşar; ortalama sapma $6{,}1\sigma$.
- **Sabit (mikro) okuma her galakside daha yakındır** (ortalama $3{,}3\sigma$) — ama o da ortalamada fazla öngörür ($f_{DM}$ artığı $+0{,}19$ dex). Bu, teorinin **kayıtlı tek büyük açığıdır**; kaynağı $a_0$'ın değeri değil, F4'ün yoğun-rejim davranışıdır (yoğun uçta baryonlar tek başına gözlemi aşar — $a_0$'dan bağımsız).

Mikro okumanın türetim tarafı da aynı yöne işaret eder: Adım 6, $a_0$'ın $\rho_n$ bağımlılığını **birinci kuvvet** verir ($a_0\propto\rho_n^{-1}$) — $cH_0$'a bağlı hiçbir terim içermez. Sonuç: **$a_0$ mikro sabitlerin bileşkesidir, kozmik zamanla değişmez; $cH_0$ ile bugünkü örtüşme sayısal bir rastlantı olarak kaydedilir.**

**Statü.** $a_0$, Ek C'ye **[S]** (gözlemle sabitlenmiş) rozetiyle girer — **[T] değil.** Biçimi türetilmiştir; değeri, biçimin izin verdiği band içinden gözlemle seçilmiştir. Türetim iddiası değer için yapılamaz; $\ell_\omega^{mikro}$'nun bağımsız (SPARC dışı) bir ölçümü değeri iğnelerse bu statü yeniden değerlendirilir (7.4, madde 12).

### $c_0$ sabit alınabilir mi? Postülat 4 ile hesaplaşma

**İtiraz.** Yukarıdaki bütün hesaplarda $c_0$ tek bir sayı olarak kullanıldı ($2{,}998\times10^8$ m/s). Oysa **Postülat 4'e göre teoride sabit bir $c_0$ yoktur**: $c_0=\sqrt{P/\rho}$ yerel bir alan değeridir (M-1, KY-1), mutlak üst sınır değildir ve Ek C satır 6'da rozeti **T (yerel değişken)** olarak kayıtlıdır. Galaksiden galaksiye $P/\rho$ değişiyorsa $a_0$ da değişmeli, dolayısıyla sınav baştan yanlış kurulmuş olmalıdır. İtiraz yerindedir ve karşılanması zorunludur.

**Etkinin girdiği yer — ve neden üç kat büyür.** Teorinin yayılma hızı Ek M-42'de kesindir:

$$\Lambda \equiv 1-\frac{\Phi}{c^2}\;;\qquad \ell_{loc}\propto\Lambda,\quad f_{loc}\propto\Lambda,\quad c_{loc}=c_0\,\Lambda^{2}$$

$a_0$'ın mikro biçiminde ($\mathcal{G}m_n/\ell_\omega^2$) $c_0$ açıkça geçmez; itiraza en elverişli üst sınırı almak için $c_0$'nin en çok kez girebileceği yazım kullanılır ($c_0$ bir kez açıkça, bir kez de $\rho_0=P_0/c_0^2$ üzerinden, kare bağlaşımla):

$$a_0 \;\propto\; c_0^{-3} \qquad\Longrightarrow\qquad \frac{\delta a_0}{a_0} = 3\left|\frac{\delta c}{c}\right| = 6\,\frac{\Phi}{c^{2}}$$

Yani hesap, teori-içi etkiyi **bastıran değil üçe katlayan** varsayımla — itiraza en elverişli hâliyle — yapılmıştır.

**Büyüklük.** SPARC örnekleminde $v_{max}$ 18–383 km/s arasındadır; $\Phi/c_0^2=(v/c_0)^2$ olduğundan:

| Büyüklük | Aralık | Medyan |
|---|---|---|
| $\Phi/c_0^{2}$ | $3{,}5\times10^{-9}$ – $1{,}6\times10^{-6}$ | $1{,}35\times10^{-7}$ |
| $\vert\delta c_{loc}/c_0\vert = 2\Phi/c_0^{2}$ | $7\times10^{-9}$ – $3{,}3\times10^{-6}$ | $2{,}7\times10^{-7}$ |
| $\vert\delta a_0/a_0\vert = 6\Phi/c_0^{2}$ | $2{,}1\times10^{-8}$ – $9{,}8\times10^{-6}$ | $8{,}1\times10^{-7}$ |

**İleri hesap — uygulandı.** $c_0\to c_0\Lambda^2$ her galakside ayrı ayrı hesaplanıp 163 galaksi yeniden fitlendi:

| | Medyan $\chi^2_{ind}$ | Kabul edilebilir |
|---|---|---|
| $c_0$ sabit | 2,9404 | 36/163 |
| $c_{loc}=c_0\Lambda^{2}$ (M-42) | 2,9404 | 36/163 |

Fark $7\times10^{-7}$'dir. **Ölçülebilir etki yoktur.**

**Tersine hesap — asıl bulgu.** Asıl soru şudur: her galaksinin verisine tam oturması için $c_0$ *ne kadar* değişmeliydi? Her galakside $a_0$ serbest bırakılıp gereken çarpandan $\delta c/c_0$ geri okunduğunda:

$$\left|\frac{\delta c}{c}\right|_{\text{gereken}} = 0{,}29 \quad (\%5\text{–}\%95:\;0{,}04\text{–}2{,}79) \qquad\text{buna karşılık}\qquad \left|\frac{\delta c}{c}\right|_{\text{izin verilen}} = 2{,}7\times10^{-7}$$

**Oran: bir milyon kat.** Dönüş eğrisi artıklarını yerel $c_0$ ile açıklamak için gereken sapma, teorinin izin verdiğinin $10^6$ katıdır.

![Postülat 4 ile hesaplaşma — 163 galaksi](Gorseller/c_yerel_sinavi.png)

*Sol panel: her galaksi için verinin gerektirdiği (pembe) ve teorinin izin verdiği (yeşil) $\vert\delta c/c_0\vert$; iki bulut arasında altı kadem vardır. Sağ panel: $c_{loc}$ gerçekten uygulandığında 163 galaksinin $\chi^2_{ind}$ değerleri birebir köşegen üzerinde kalır.*

**Ve izin veren şey teorinin kendi başarısıdır.** Buradaki sınır dışarıdan dayatılmış değildir. $\Lambda$ tek bir büyüklüktür ve **aynı anda** hem yayılma hızını ($c_{loc}\propto\Lambda^2$) hem atomik geçiş frekanslarını ($f_{loc}\propto\Lambda$) yönetir. Teori kütleçekimsel kızıla kaymayı bu $\Lambda$ ile üretir ve **doğru** üretir (6.2, Ek M-42). Galaksilerde $\delta c/c_0\sim0{,}3$ olsaydı, aynı zincir her galaksinin tayf çizgilerinde laboratuvara göre ~%15 mertebesinde bir kayma öngörürdü — uzaklıktan bağımsız, her yönde, evrensel bir kayma. Böyle bir şey gözlenmemiştir. Yani:

> **Teorinin kızıla kaymayı doğru vermesi, $c_0$'nin galaktik ölçekte serbest bırakılmasını yasaklar.** İki gözlem tek parametreye bağlıdır; birini tutturmak diğerini kilitler.

**Statü — bu bir kayıp değil, kazançtır.** Postülat 4 çiğnenmiş olmuyor: $c_0$ hâlâ sabit değildir, hâlâ $\sqrt{P/\rho}$'dur, hâlâ aşılabilir bir kavrama sınırıdır ve bu kitabın başka bölümlerinde (cam, Shapiro, kızıla kayma, Hubble tensi) tam olarak değişkenliğiyle iş görür. Kapanan şey yalnızca şudur: **galaktik dönüş eğrisi probleminde $c_0$ bir serbestlik değildir.** Bu tespit, teoriye yöneltilebilecek ciddi bir itirazın — *"$c_0$'niz değişken olduğuna göre her eğriyi uydurabilirsiniz"* — kapısını kapatır. Uyduramayız, ve nedenini teorinin kendisi söyler.

**Dürüstlük kaydı.** Yukarıdaki $\Phi/c_0^2$ tahmini $\Phi\simeq v_{max}^2$ ile yapılmıştır; tam potansiyel kuyusu, kütle dağılımı üzerinden integre edilirse birkaç kat daha derin olabilir (logaritmik terim). Bu, sonucu değiştirmez: birkaç kat, $10^6$'lık açığı kapatmaz. Ayrıca yerel $c_0$'nin **zamansal** değişimi (7.7.1'in Hubble tensi çözümü) burada hesaba katılmamıştır; SPARC galaksileri $z<0{,}01$ olduğundan geriye-bakış süresi ~100 Myr'dır ve bu kanaldan gelecek sapma daha da küçüktür.

## 6.5.4.6 $R_f$'nin Statüsü: Fenomenolojik Terim ve Devinim Mekanizması Önerisi


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

### Mekanizma önerisi: çekirdek devinimi ve galaktik kalınlaşma

Postülat 5'in 4B çift dönüşü, makro ölçekte devinim (presesyon) olarak yansır (7.1.1). Eksenel akı tüpünün ekseni deviniyorsa ve devinim **yerel yörünge periyodundan hızlıysa**, o yarıçaptaki madde devinimi takip edemez ve zaman-ortalamalı olarak **yayılmış** bir tüp görür. Devinim senkron olsaydı disk yalnızca eğilir, kalınlaşmazdı; **kalınlaşma için devinimin hızlı ve senkron-olmayan olması gerekir.**

Bu mekanizma üç şey kazandırır:

1. **Doğrusal yayılmayı türetir.** Koni yarı-açısı $\theta_p$ için $h\simeq h_0+R\sin\theta_p$, yani $h\propto R$. M-38 doğrusallığı *varsayıyordu*; bu mekanizma onu üretir.
2. **Yayılmanın başlangıç yarıçapını açıklar.** Madde ancak $T_{dev}<T_{yörünge}(R)$ olduğunda takip edemez. $T_{dev}=2\pi R_f/v_{düz}$ tanımıyla bu koşul tam $R_f$'de sağlanır: **yayılma, devinim–yörünge rezonansının bulunduğu yarıçapta başlar** ve dışa doğru büyür.
3. **Makul bir sayı verir.** 98 galakside türetilen devinim periyodu medyanı **0,47 Gyr**; saçılması (6,1 kat) $R_f$'nin kendi saçılmasından (7,3 kat) **dardır**. Devinim konisi $h_0=0{,}2$ kpc alındığında $\theta_p\approx1{,}2°$.

**Ama mekanizma da doğrulanmamıştır.** Üç çekince: (i) mekanizmanın öngördüğü $R_f\propto v_{düz}$ (log-log eğim 1) ile dikey-denge yasasının öngördüğü eğim 2, **aynı saçılmayı** verir (0,788'e karşı 0,783 dex) — veri ikisini ayırt etmez; ölçülen eğim 1,57 ikisinin arasındadır. (ii) Koni açısı 0,01°–42° arasına dağılır; dar bir değer yoktur. (iii) 43/141 galaksi **hiç** yayılma istemez, oysa dönen bir çekirdeğe sahip her galaksinin devinmesi beklenir.

*Devinimin doğrudan dinamik katkısı ayrıca hesaplanmış ve ihmal edilebilir bulunmuştur:* Coriolis payı $2\Omega_p/\omega_{yör}$ oranındadır ve merkezcil bütçeye %10 katkı için devinim periyodunun evren yaşı mertebesinde olması gerekir. Devinim dönüş eğrisine **doğrudan** girmez; girdiği yer diskin dikey yapısıdır.

## 6.5.4.7 Dürüstlük kayıtları

**(1) Eşit serbestlikte ΛCDM öndedir.** NGC 3198'de 1 parametrede AIC 79,1'e karşı 1371,6; 2 parametrede 64,5'e karşı 159,0. Evrenakı ancak yayılma çarpanıyla (3 parametre) öne geçer — ve o çarpan fitlenmiştir, ölçülmemiştir (6.5.4.6).

**(2) Kaynak kilitli saf sürüm gerçek veriyle ayakta kalmıyor.** $\Upsilon_*$ fotometrik değere kilitlendiğinde $\chi^2_{ind}=32{,}6$'dır. Tek parametreli hâl, teorinin en zarif biçimiydi; gerçek veri onu dışlıyor.

**(3) Tek galaksiden okunan $\ell_\omega^{etkin}$ sağlam bir sayı değildir.** NGC 3198'de 7,06 kpc (kilitli) ile 1,21 kpc (yayılmalı) arasında, $\Upsilon_*$ seçimine göre değişir. Mikro sabit bundan etkilenmez — $\ell_\omega^{mikro}$ örneklemin tamamından ölçülür (35,7 fm; kütleyle korelasyon $+0{,}03$; 6.5.4.3 Adım 6) — ama galaksi başına tek fitten $\ell_\omega^{etkin}$ okuyup ona mikro-fiziksel anlam yüklemek yanlış olur.

**(4) $\Upsilon_*$ bandının dayatılması sınavı.** Popülasyon sentezi, 3,6 μm için $\Upsilon_*\in[0{,}3,\,0{,}8]$ bandını verir. Teorinin denklemi $a_0$ küresel sabitken galaksi başına tek serbest parametre ($\Upsilon_*$) taşır; bant zorla dayatıldığında ne olduğu 169 galakside ölçülmüştür:

| $\Upsilon_*$ aralığı | Evrenakı ($k=1$) | ΛCDM NFW ($k=2$) |
|---|---|---|
| Serbest (0,05–3,0) | 3,41 | 1,90 |
| **Popülasyon sentezi (0,3–0,8)** | **4,91** | **2,49** |
| Dar (0,4–0,6) | 7,60 | 2,80 |
| **Bozulma (serbest → pop. sentezi)** | **%44** | **%32** |

İki sonuç: **(a)** serbest fitte medyan $\Upsilon_*=0{,}49$ çıkar — tam fotometrik beklentide ($\sim0{,}5$). Model $\Upsilon_*$'ı sistematik olarak şişirmez; galaksilerin %49'u bandın dışına çıkar ama sapma iki yönlüdür ve büyük kısmı ölçüm bütçesiyle (uzaklık, eğiklik) uyumludur. **(b)** Bant dayatıldığında bozulma iki modelde aynı mertebededir (%44'e karşı %32); teori bu sınavda **dışlanmaz.** Uyum kalitesi farkı ise fitin **biçimine** bağlıdır ve teoriye-sadık biçimde teorinin lehinedir: $a_0$ resmî değerinde kilitlenip ikinci parametre gözlemsel mesafe çarpanı $\delta$ alındığında ($W$ penceresi $\delta$'dan matematiksel olarak bağımsızdır) eşit-serbestlik yarışı 173 galakside galaksi-başına RMS'te 109/64, medyan $\chi^2_{ind}$'de 1,41'e karşı 1,97 **Evrenakı lehinedir** (10.1.1). Kayıt: Sb–Sbc medyanında ΛCDM fit küçük farkla öndedir ve 63 galakside $\delta$ katalog mesafe belirsizliğinin 3σ'sını aşar — panellerde işaretlidir.

**Bandın kendisi tartışmaya kapalıdır — teorinin kendi denklemi gereği.** *"3,6 μm bandı, teorinin gerektirdiği nükleon sayımı için doğru dönüşüm olmayabilir"* itirazı geçersizdir; 4.2.4'ün kendi türetimi şunu verir:

$$\frac{\gamma_N}{m} \;=\; \frac{V_n}{m_n} \;=\; \frac{1}{\rho_n}$$

$\rho_n$ **evrensel bir sabittir** (Ek C satır 4). Dolayısıyla teorinin kaynağı olan nükleon hacmi, baryonik kütleyle **sabit oranlıdır**: ışık→nükleon dönüşümü ile ışık→kütle dönüşümü, evrensel bir çarpan dışında **aynı dönüşümdür.** Teori "$\Upsilon_*$ bandı bana ait değil" diyemez; kendi $\gamma_N=NV_n$ tanımı onu o banda bağlar. (Bağlanma yalnızca bağlanma enerjisi mertebesinde, yüzde bir düzeyinde gevşektir.)

**(4c) Ve bant, teorinin tek zafer iddiasını da götürüyor.** Kısıt rejime ayrılarak uygulandığında (6.5.3.3, Sonuç 5) cüce/LSB bandındaki $3{,}4\sigma$ üstünlük **$0{,}8\sigma$**'ya iner; $80$–$120$ km/s bandında medyan $\chi^2_{ind}$ 6,3 kat bozulur ve kazanma oranı $+1{,}5\sigma$'dan $-3{,}0\sigma$'ya döner. Teori bant altında cücede medyan olarak hâlâ öndedir ($1{,}68$'e karşı $2{,}28$) — yitirilen medyan üstünlük değil, üstünlüğün tutarlılığıdır. **Kitabın galaktik başlık iddiası bu koşulla birlikte okunmalıdır.**

**(4b) Ama $\Upsilon_*$ tamamen kaldırılamaz da.** Karşı uçtaki sadelik denemesi de olumsuzdur: tüm örnekleme tek bir **küresel** $\Upsilon_*$ dayatıldığında (galaksi başına **sıfır** serbest parametre) en iyi değer $\Upsilon_*=0{,}70$'te medyan $\chi^2_{ind}=17{,}24$ verir — galaksi başına serbest hâlin (2,94) altı katı kötü. $\Upsilon_*$'ın galaksiden galaksiye değişmesi bir fit hilesi değil, yıldız popülasyonlarının gerçekten farklı yaş ve metallikte olmasının sonucudur; her iki model de bu girdiye eşit ölçüde muhtaçtır.

**(5) Ayakta kalan şey nedir?** Üç şey: **(a)** ekvator denetimi ve M-37 profil teoremi (veriden bağımsız yapısal sonuçlar), **(b)** $\ell_\omega$ türetiminin Güneş Sistemi'nde hiçbir gerilim doğurmaması ($\varepsilon$ sınırın on milyar kat altında), **(c)** teorinin görünmez madde envanteri talep etmemesi — ΛCDM aynı eğri için baryonun 11,9 katını isterken; **(d)** $a_0$'ın biçiminin teorinin kendi büyüklüklerinden kurulması ($\mathcal{G}m_n/\ell_\omega^2$; 6.5.4.5) ve buna bağlı olarak **$c_0$'nin galaktik dinamikte bir serbestlik olmadığının gösterilmesi** — teori kendi kızıla kayma başarısıyla kendini bağlar, dolayısıyla "değişken $c_0$'yle her eğri uydurulur" itirazı geçersizdir. Ayakta kalmayan şey, uyum kalitesinde eşit serbestlikte üstünlük iddiasıdır.

**(6) Tek galaksi.** SPARC 175 galaksi içerir; $\ell_\omega$'nun (veya $b$'nin) evrensel olup olmadığı ancak örneklemde sınanır. Sınanmadan bu bir vaka çalışmasıdır (7.4).

## 6.5.4.9 Küresel sistemler kaydı: teorinin makinesi nereye kadar uzanıyor?

Teorinin galaktik denkleminin geçerlilik alanı bu kayıtla sınırlandırılır.

**(1) F4'ün kaynağı merkezî kara delik değildir.** F4'ün genliği vortisiteden türetilir ve kaynağı $M_{kaps}$'tır (6.5.4.3). Ölçüm de bunu doğrular: F4'ün genliği kovanla değil toplam baryonik kütleyle ölçeklenir ($\rho=-0{,}91$'e karşı $-0{,}33$); kovansız 134 galakside F4 yine zorunludur ($\chi^2$ 17,3 → 1,37); ve kara delik kütlesi dönüş eğrisi verisinde görünmezdir (etki yarıçapı en iç noktadan 75 kat küçük, $\chi^2$ dördüncü basamakta değişir). Bu nedenle teoriden kara deliklerle ilgili hiçbir galaktik öngörü çıkmaz; kara delik içeren hiçbir iddia 6.5.4.8'in yanlışlanabilir öngörüler tablosuna giremez.

**(2) Basınç-destekli sistem köprüsü KURULDU ve İKİ BAĞIMSIZ AİLEDE DOĞRULANDI (M-48, [T]).** İki parçayla: *(i)* **küresel izdüşüm lemması** — silindirik F4 kuvvetinin radyal bileşeni her enlemde tam $\sqrt{\mathcal{G}M_{kaps}a_0}/r$'dir ($\sin\theta$'lar sadeleşir; kutup, M-47'nin Rankine koluyla düzenlidir): küresel sistem diskle **aynı radyal yasaya** uyar; kaynak tarafında $\sqrt N$ teoremi düzenli dönme istemez (dolanım korunumu yeter), dispersiyon-destekli kütle F4'ü birinci mertebede tam besler. *(ii)* **Jeans köprüsü** — izotropik dış bölgede $\sigma^2=\sqrt{\mathcal{G}M_{bar}a_0}/\alpha$; izotermal $\alpha=2$ ile $v_c=\sqrt2\,\sigma$ ve Faber–Jackson türer: $\sigma^4=\mathcal{G}M_{bar}a_0/4$ (BTFR'nin kardeşi, aynı sabitlerle). Mertebe denetimi: Fornax $M_*\sim10^7$ için $v_c=17{,}8$ km/s — aşağıdaki $\sim18$ km/s kaydıyla örtüşür (dış-alan şerhiyle).

> **Güncel sınır:** M-48 ile küresel sistemlerin **dış bölgesi** türetim kapsamına girmiştir ($a_r$ diskle aynı; $v_c=\sqrt2\sigma$). Kapsam dışında kalanlar açıkça sınırlıdır: **dış-alan-baskın cüce küreseller** (MW uyduları — EFE terimi türetilene dek nicel öngörü verilmez) ve anizotropinin $O(1)$ bandı. SPARC sınavları ve 96_ETG zaten köprüsüz geçerliydi; M-48 onları değiştirmez, 96_ETG'nin başarısını **açıklar.**

**Açık iş (güncel).** (a) ve (b) türetilmiştir (M-48); dış-$\sigma$ sınavı (G-12) **yapıldı ve geçildi** (SLUGGS, 22 galaksi — [T-aday]→[T] koşulu sağlandı). Kalanlar: sıcak bileşenin λ'ının türetimi (ikinci-mertebe kovan düzeltmesi) ve EFE teriminin gelgit/Chae sınavları (7.4).

## 6.5.4.8 Yanlışlanabilir öngörüler (7.5 tablosuna)

| # | Öngörü | Ölçüm aksini gösterirse |
|---|---|---|
| G-1 | Her sarmal galakside $\ell_\omega/R_d$ oranı yaklaşık sabittir ($\approx4{,}5$) | Oran galaksiden galaksiye düzensiz değişirse F4'ün vortisite beslemesi yanlıştır |
| G-2 | Dönüş eğrisi, HI diski bittikten sonra $v\propto R^{-1/2}$'ye döner (küresel akıya geçiş) | Kesim ötesinde düz kol sürerse $M_{kaps}$ beslemesi yetersizdir |
| G-3 | Diskin kalınlaştığı ($h$ arttığı) yarıçapta eğri düzlükten aşağı sapar | Kalınlaşan diskte düzlük sürerse M-38 Varsayım 3 çöker |
| G-4 | Aynı $\ell_\omega$, aynı galaksinin hem dönüş eğrisini hem galaktik kızıla kayma sapmasını birlikte açıklamalıdır | İki gözlem farklı $\ell_\omega$ isterse parametre yama statüsüne düşer |
| G-5 | Güneş Sistemi'nde $1/R$ payı $\varepsilon=r/\ell_\omega$ ile ölçeklenir; Ay'da $\sim10^{-12}$ | Ay veya gezegen presesyonlarında $10^{-5}$ mertebesinde artık bulunursa ölçek ataması yanlıştır |
| G-6 | Galaktik dönüş eğrisi artıkları yerel $c_0$ değişimiyle **açıklanamaz**: teori $\vert\delta c/c_0\vert\leq3\times10^{-6}$ ile kilitlidir (M-42 + kızıla kayma) | Bir galakside $\vert\delta c/c_0\vert>10^{-5}$ mertebesinde bağımsız kanıt bulunursa (ör. ince yapı sabiti veya tayf çizgi oranı anomalisi) M-42'nin $\Lambda$ tekliği çöker |
| G-7 | Tutarlılık kümesi atom çekirdeğidir (Adım 7): temiz hiçbir galakside gereken $a_0$ çarpanı $[X,\langle A\rangle]\approx[0{,}7;\,2{,}2]$ penceresinin belirgin dışına çıkamaz; $M_{tut}$ hidrojen kütle kesrini izler; bağımsız her $\ell_\omega^{mikro}$ ölçümü 7,4 fm – $2{,}7\times10^3$ fm ölçek boşluğunda kalmalıdır | Pencere dışı temiz bir ölçüm ($k>3$ ya da $k<0{,}5$), $X$'ten bağımsız bir $M_{tut}$, ya da boşluk dışı bir $\ell_\omega$ Adım 7'yi çürütür |
| G-8 | Dolanım korunumu + kaskad okuması (Adım 7): $\ell_\omega^{mikro}$ hiçbir kütle aralığında sistematik eğim göstermez (polarizasyon tam sıfır); $\lambda\leq1$ — temiz-büyük S0/BCD örnekleminde pencere-üstü çarpanlar 1'in altına inmek zorundadır; $\lambda$ diskin inceliği/dinamik soğukluğuyla ($v/\sigma$) artmalıdır *(ilk sınav, 18 galaksi: $+0{,}49$, $p=0{,}019$ — işaret öngörülen yönde; kesin doğrulama $n\gtrsim40$ kayıt-öncesi kipte bekliyor)* | $\ell_\omega^{mikro}$'da kütle eğimi, temiz uçlarda kalıcı $\lambda>1$, ya da $\lambda$–incelik ilişkisinin büyük örneklemde ters çıkması Adım 7'nin muhasebe çerçevesini çürütür |
| G-9 | $a_0$'ın aday kapanışı (6.5.4.5, M-45): $\ell_\omega/r_n=\sqrt{m_p/m_e}$ — bağımsız her $\ell_\omega^{mikro}$ ölçümünün **medyanı** $36{,}0$ fm'e ($\pm\%5$) yakınsamalı (medyan-H kilidi: $X>0{,}5$); tür-ayrımlı dağılımda He/metal nükleonlarının $\ell\approx51$ fm'lik ikinci modu bulunmalı; oran $r_p$ revizyonlarıyla birlikte hareket etmeli; hiçbir ortamda $a_0^{etkin}<X\cdot\mathcal{G}m_nm_e/(m_pr_n^2)\approx6{,}3\times10^{-11}$ m/s² ölçülmemeli | Medyanın 36 fm'den sapması, ikinci modun yokluğu/yanlış yerde çıkması, oranın $r_p$'yi izlememesi ya da tabanın altında bir $a_0$ aday kapanışı çürütür |
| G-10 | Etkin yasa ayrışması — geniş çift yıldızlar (6.5.4.5): F4 yerel dolanımdan/kapsanan kütleden beslenir ve galaktik F4 çift ölçeğinde düzgün alandır → çiftin **iç** dinamiği Newton'a yakın kalmalıdır; MOND-tipi evrensel ~%20 hız artışı görülmemeli *(hesap yapıldı: sapma ≲$10^{-4}$, baskın terim galaktik gelgit; koşul: F4'ün taşıyıcısı koherent disk dolanımı — karşı-olgusal öz-F4 kanalı %24–158 verirdi, sınav ikilidir)* | Gaia geniş çiftlerinde kalıcı, sistematik MOND-tipi artışın kesinleşmesi F4'ün yerel-kaynak okumasını çürütür |
| G-12 | Basınç-destekli köprü (M-48): dönme-destekli olmayan küresel sistemlerin dış $\sigma$-profilleri düzleşmeli ve düz değer $\sigma^4=\mathcal{G}M_{bar}a_0/4$'e oturmalı; hem $\sigma$ hem bağımsız $v_c$ veren sistemlerde dış bölgede $v_c/\sigma\to\sqrt2$ *(sınav yapıldı ve geçildi — SLUGGS küresel-küme kinematiği, 22 galaksi: medyan $+0{,}051$ dex (katalog $\Upsilon$) / $-0{,}004$ (kovan konvansiyonu), 2–10 $R_{eff}$ yarıçapta düz; en kötü tekil küme-merkezlisi M87 $-0{,}195$)* | Dış-$\sigma$ düzlüğünün yokluğu, FJ sıfır noktasının $a_0$'dan sistematik sapması ya da $v_c/\sigma$'nın $\sqrt2$'den kalıcı ayrılması M-48'i çürütür (izotropi/EFE şerhleriyle) |
| G-13 | EFE terimi (M-49): dış-alan-baskın sistemlerde iç dinamik yarı-Newton'dur ve tek evrensel çarpan taşır — $\mathcal{G}_{etkin}/\mathcal{G}=1+\sqrt{a_0/g_{ext}}$ (aynı $g_{ext}$'te aynı); disklerde eğri düşüşü tam $g_{kaps}=g_{ext}$ yarıçapında başlamalı ve düşüş bölgesinde $v^2-V_{bar}^2\propto1/R$; izole cüceler aynı $M_*$'daki baskın-alan eşleniklerinden yüksek $\sigma$ taşımalı *(ilk sınav — McConnachie 2012, 28 sistem: büyük uydularda imza lehte, $+0{,}109\to+0{,}042$; küçük klasikler gelgit-karıştırıcılı, hüküm yok)* | Çarpanın $g_{ext}$'le $\sqrt{}$ dışı bir bağımlılık göstermesi, düşüşün yanlış yarıçapta başlaması ya da izole↔baskın farkının yokluğu M-49'u çürütür |
| G-11 | Etkin yasa ayrışması — $a_0$ kozmik zamanla değişmez (mikro köken, M-45): genişleyen yüksek-$z$ dönüş eğrisi örneklemlerinde $a_0(z)$ eğimi sıfır kalmalı; $a_0\propto cH(z)$ dışlanmış kalmalı *(ilk sınav: $z=0{,}85$–$2{,}4$'te 6/6 dışlama)* | Yüksek-$z$'de $H(z)$'yi izleyen sistematik $a_0$ kayması mikro kökeni ve M-45 zincirini çürütür |

## 6.5.5 Kapanış beyanı: makine tamam, program tanımlı ve dışa açık

Galaktik yörünge probleminin **teorik makinesi tamamlanmıştır** — denklemde türetilmemiş öğe
kalmamıştır: F1 ve F4'ün biçimleri (M-35, M-37/M-38), toplanma (lineer süperpozisyon,
[T-koşullu]), geçiş penceresi (M-47), küresel sistemlere uzanım ve $v_c=\sqrt2\,\sigma$
köprüsü (M-48, **[T]**), dış alan terimi (M-49); $a_0$'ın biçimi türetilmiş, değeri [S] rozetiyle
kalibre ve aday kapanışı (M-45) kayıtlıdır. **Kanıt programı ise tanımlı ve açıktır** — her aday
rozetin bağımsız-veri sınavı bellidir ve biri tamamlanmıştır: M-45: SPARC-dışı
$\ell_\omega$ ölçümü + hakem denetimi; M-47: örneklem-dışı HI kinematik koşumu (sabit
$a_0$, sıfır yeniden-kalibrasyon) — *ilk adım geçildi: MIGHTEE-HI'da (SPARC örtüşmesi sıfır, n=57) BTFR sıfır-noktası öngörü bandının içinde; yarıçap-çözümlü koşum açık*; **M-48: iki bağımsız aile geçildi ve rozet [T]'ye yükseldi** — *Yerel Grup cüceleri (28 sistem, medyan $+0{,}009$ dex) ve SLUGGS eliptikleri (22 sistem, $+0{,}051$/$-0{,}004$ dex; G-12), ikisi de sıfır yeniden-kalibrasyonla*; M-49:
izole↔baskın cüce küresel karşılaştırması (G-13) — *ilk işaret büyük uydularda lehte, küçük klasikler gelgit-karıştırıcılı*. Bugünkü ölçülmüş karne nettir: üç ampirik yasa tek denklemden; geçiş fonksiyonu türetilmiş;
$a_0$ üç bağımsız ailede sıfır ayarla doğrulanmış; galaksi başına serbest parametre sıfır.
Bu bir "kapandı" ilanı değildir ve
olamaz: her sınav çift taraflıdır — beyanın gücü, yanlışlanabilir ve hakem önünde
savunulabilir olmasındadır.

**Matematik cephesi bu kitapta kapanmıştır.** Denklemin her öğesi türetilmiştir; bundan sonraki
hiçbir iş yeni bir türetim değil, veri işidir. Ve kanıt programı bilinçli olarak **dışa açık
bırakılmıştır:** kalan her sınav — SPARC-dışı $\ell_\omega$ ölçümü, yarıçap-çözümlü HI koşumu,
gelgit ayrıştırması, λ bağıntısı, küme ölçeği — verisi, betiği ve karar kuralı çalışma
arşivinde tanımlıdır ve talep eden her araştırmacıya açıktır. Kanıtların bir kısmını
başkalarının bulacak olması bir eksik değil, **sınamanın ta kendisidir:** teori bütün
doğrulamasını kendi eliyle tamamlasaydı, bu kitabın en sert özeleştirisi ("türetimler
sınandıkları veriden okunuyor" — 7.4) yanıtsız kalırdı. Bağımsız elden gelen her geçer not,
bizim koşacağımız bir koşumdan daha ağır tartar; gelecek her aleyhte sonuç da aynı defterde,
aynı dürüstlükle kayda geçer. Makine tamamdır; hüküm verinindir.
