# 9.2 Planck Sabiti ($h$) ve Kuantum Eyleminin Türetilmesi

Modern fiziğin bütün mikro dünyasını taşıyan $h$ sabiti, standart çatıda bir **temel doğa gizemidir**: neden o değerde olduğu sorulamayan, ontolojisi olmayan bir eylem kuantumu. Evrenakı Teorisi'nde ise $h$ temel değildir; iki mekanik büyüklüğün çarpımıdır:

$$h = \delta\tau$$

Burada $\delta$, tek bir Zerre vuruşunun alıcıya devrettiği enerji; $\tau$, alıcı elektron-girdabın **kopma penceresidir**. Türetimlerin tamamı Ek M-10/M-11'de, bu anatominin ölçümle yüzleşmesi (fotoelektrik ve Compton sınavları) 9.4'tedir. Bu bölümün işi ikisinin arasındaki katmandır: $h$'nin **anatomisi** — $\delta$ ile $\tau$'nun mekanik kimlikleri, çarpımın neden evrensel olduğu, $h$'nin doğum yeri olan karacisim ışımasının teori-içi okuması ve iki bileşenin ayrıştırılma programı. Kısım 9'un sonraki bölümleri pencere mekaniğine her ihtiyaç duyduğunda buraya atıf yapacaktır.

## 9.2.1 Pencere Mekaniği: Alışverişin Muhasebe Birimi

Teorinin ışıktan istediği envanter üç kalemdir: **Zerre katarı**, **Zerre aralığı** ($\lambda$; ritim $\nu=c_0/\lambda$) ve **paralel katar sayısı** (şiddet). Katar kesintisizdir — ışığın kendisinde hiçbir kesiklilik yoktur. Kesikliliği üreten, alıcıdır ve mekanizması iki adımdır:

**Tek vuruş yetmez.** Zerre–elektron çarpışması elastik kinematiğe tabidir; $m_z\ll m_e$ olduğundan tek vuruşun aktarabildiği kesir $\eta\approx4m_z/m_e\approx6{,}5\times10^{-5}$'tir (M-10) — pinpon topunun bovling topuna çarpması gibi: mermi, enerjisinin neredeyse tamamıyla geri seker. Tek vuruşun devrettiği enerji tek sembole toplanır:

$$\delta = \eta\cdot\tfrac12 m_z\left(c_0^2+k_a v_{cev}^2\right) = \eta\, m_z c_0^2 \approx 5{,}4\times10^{-4}\ \text{eV/vuruş}$$

*(Sayısal değer öteleme ve dönme paylarının toplamıdır: $k_a=1/2$ ve $v_{cev}=\sqrt2\,c_0$ ile $k_a v_{cev}^2 = c_0^2$ olduğundan iki pay tam eşittir ve muhasebe $\delta = \eta\, m_z c_0^2$'ye kapanır — M-10.)*

Elektronun tek darbeyle değil **ardışık rezonansla** sökülmesinin mekanik zorunluluğu budur (2.2.3).

**Birikimi pencere keser.** Elektron-girdabın evrensel bir kopma penceresi $\tau$ vardır: sökülme kararını, bu pencere boyunca biriken enerji belirler. Pencere boyunca gelen vuruş sayısı $N=\nu\tau$; biriken enerji:

$$E = \delta\cdot N = (\delta\tau)\,\nu$$

Millikan'ın ölçtüğü fotoelektrik doğrunun eğimi Planck sabitidir (Millikan, 1916); eğimlerin eşitlenmesi $h=\delta\tau$ özdeşliğini verir (M-11). Rozet **[S]**: gözlemin sabitlediği şey çarpımdır; bileşenlerin ayrı ayrı sınanması 9.2.6'nın ayrıştırma programına kalır (Ek C).

Kesikliliğin adresi böylece netleşir. Standart fiziğin "foton" dediği ölçüm birimi bu tabloda bir **cisim** değil, bir **pencerelik alışveriştir**: $h\nu$, ışığın bir parçasının taşıdığı enerji değil, alıcı penceresinin katardan bir olayda aldığı ısırıktır. Yayım tarafında da aynı birim iş görür: kaynağın kendi penceresi boyunca ateşlediği $N=\nu\tau$ mermilik wake-kilitli katar dilimi **Zerre Paketi'dir** (2.6.5) ve toplam etkin enerjisi $E_{paket}=(\delta\tau)\nu=h\nu$'dür — standart fiziğin "foton"unun **uçuş yüzüne** teoride karşılık gelen budur; ölçüm yüzü, yukarıda kurulan pencere ısırığıdır. Paket **yayım birimidir, teslim kuantumu değil**: dedektörlerin gördüğü $h\nu$ sayı merdiveninin adresi de alıcıdır — her soğurma olayı, alıcı penceresinin $(\delta\tau)\nu$'lük bir ısırığıdır. Kaynak ile alıcı pencereleri aynı evrensel $\tau$'yu taşıdığından, paketin etkin enerjisi ile alıcının ısırığı aynı $h\nu$'de buluşur; merdiven, iki ucun bu mutabakatıdır. Kuantum, ışıkta değil **etkileşimde** yaşar. Açısal biçimlerde kullanılan indirgenmiş sabit tanımsaldır: $\hbar=\delta\tau/2\pi$ (2.10.2'nin belirsizlik bağıntılarında iş gören budur).

**Adres tespitinin mühendislik teyidi.** Bu bölümün en tartışmalı iddiası — kesikliliğin ışığın değil alıcının özelliği olduğu — bağımsız bir kaynaktan, ölçüm endüstrisinin kendi belgelerinden doğrulanır. Yüz yılın bütün ışık sensörleri iki mimariden birindedir: poz boyunca yük **biriktiren** kuyu (CCD/CMOS) ya da yarı-kararlı bir sistemi eşiğin altına kurup çığ boşaltan **kapan** (PMT, SPAD, SNSPD). İkisi de gelen ışığın kesikliliğini değil, birikimin bir eşiği aşmasını kaydeder; verim birden küçük, karanlık klik sıfırdan büyüktür ve klik enerjisinin ışıktan gelen payı milyarda bir mertebesindedir. Sayı merdivenini çözdüğü söylenen aygıtların tarttığı basamak da **elektron/enerji** basamağıdır (9.10.7). Kova ile pencere birikimi ($N=\nu\tau$), kapan ile eşikli kopma ($h=\delta\tau$) arasındaki karşılık birebirdir: sensör endüstrisi, "tek foton"u yakalama arayışında farkında olmaksızın alıcı penceresini inşa etmiştir.

## 9.2.2 $\delta$ ve $\tau$'nun Anatomisi

**$\delta$ tamamen kurulu büyüklüklerden oluşur:** elastik aktarım kesri $\eta$ (standart kinematik), Zerre kütlesi $m_z$ (Postülat 4; teorinin **ölçülen girdi parametresi**), atalet katsayısı $k_a=1/2$ (basık/disk gövde) ve evrensel çevresel hız $v_{cev}=\sqrt2\,c_0=4{,}24\times10^8$ m/s (M-3 duvar hızı yasası, boyuttan bağımsız). $\delta$'nın içinde ayarlanabilir hiçbir şey yoktur; kapalı biçimde hesaplanır ve belirsizliği yalnız $m_z$'nin ölçüm belirsizliğidir.

**$\tau$ elektronun kendi penceresidir** ve iki yoldan yazılabilir:

1. **Özdeşlik yolu:** $h=\delta\tau$ içine $\delta$'nın açık ifadesi konduğunda (dönme terimi dahil; $k_a v_{cev}^2=c_0^2$) $h = 4\tau m_z^2c_0^2/m_e$ çıkar; ölçülen $h$ bu bağıntıdan $\tau = h/\delta \approx 7{,}7$ ps ister.
2. **Birikim yolu:** Tipik sökme işi ($\Phi+E_{ke}\approx4$ eV), vuruş başına $5{,}4\times10^{-4}$ eV → $N\approx7{,}4\times10^3$ vuruş; morötesi eşik ritminde ($\nu\approx9{,}7\times10^{14}$ Hz) birikim süresi $N/\nu \approx 7{,}7$ ps.

> [!WARNING]
> **Dürüstlük kaydı — bu iki yol bağımsız değildir.** Birikim yolu, fotoelektrik denklemi üzerinden $h$'ı zaten içerir:
> $$\Phi+E_{ke}=N\delta \quad\text{ve}\quad \Phi+E_{ke}=h\nu \;\Longrightarrow\; N=\frac{h\nu}{\delta} \;\Longrightarrow\; \frac{N}{\nu}=\frac{h}{\delta}\equiv\tau$$
> Yani iki yol **cebirsel olarak aynı bağıntıdır**; ikisinin de $7{,}7$ ps vermesi bir sağlama değil, bir özdeşliktir. Buradan şu sonuç çıkar ve açıkça yazılmalıdır: **teori $h$'ın sayısal değerini öngörmez.** $h=\delta\tau$, $h$'ı *üreten* bir hesap değil, onu iki mekanik büyüklüğe **ayrıştıran** bir özdeşliktir.
>
> Ayrıştırmanın kendisi yine de boş değildir: $\delta$ artık $m_z$'den tam hesaplanır ve ayarlanabilir hiçbir şey içermez ($\delta=4m_z^2c_0^2/m_e$), dolayısıyla $h$'ın "kesikliliği" bir doğa gizemi olmaktan çıkıp **tek vuruşun aktardığı enerji × alıcının kopma penceresi** biçiminde mekanik bir okumaya kavuşur. Kazanılan şey bir sayı değil, bir **yorumdur**.
>
> Buradan bir okuma uyarısı da çıkar: iki yol arasında bir "uyum payı" aranmamalıdır. Arada pay yoktur, çünkü arada iki ayrı hesap yoktur — mertebe yuvarlamaları ($\sim10$ ps gibi) bağımsız sonuçlar sanılıp karşılaştırıldığında görünen fark, fizikten değil yuvarlamadan doğar.

$\tau$'nun bağımsız bir tayini — yani $h$'ı kullanmayan bir hesabı — teorinin **tek yapısal açık kalemidir** ve 9.2.6'da tek bir yanlışlanabilir sayıya indirgenmiştir ($\tau=7{,}7$ ps); aranacak yerin haritası ve elenmiş yollar 9.2.7/i'de kayıtlıdır. Dürüstlüğün son kalemi $m_z$ tarafındadır: $m_z$, teorinin **ölçülen girdi parametresidir** — Standart Model'de $m_e$ nasıl girdiyse öyle; türetilmesi beklenmez. Değeri fotoelektrik eşik ölçeğiyle çapalanır (tek Zerre'nin öteleme payının tipik iş fonksiyonuna eşitlenmesi; ~±%25 genişlik, M-10) ve $v_{cev}=\sqrt2\,c_0$ türetilmiş olduğuna göre, keskinleşmeyi bekleyen tek kalem $N$'nin bağımsız sabitlenmesidir.

### Soğurma ile Yayma Birbirinin Tersi Değildir

Pencere mekaniğinin doğrudan bir sonucu, sonradan eklenmiş bir düzeltme olmadığı için burada kayda geçirilmelidir: **soğurma ile yayma zaman-tersi süreçler değildir.**

| | Mekanizma |
|---|---|
| **Soğurma** | $N$ vuruşun $\tau$ penceresi içinde **birikmesi** — kademelidir ve gelen akı gerektirir |
| **Yayma** | Zarfın **tek seferde boşalması** — gelen akı gerektirmez |

Biriktirme ile boşaltma simetrik değildir; dolayısıyla teori **karşılıklı (reciprocal) bir çatı değildir.** Bu, gözlemin dayattığı bir dizi asimetriyi ek varsayım olmadan verir:

* **Soğurma çizgisi listesi, yayma listesinden dardır.** Soğurma için pencere içinde $N$ vuruş toplanmalıdır; akı yetmiyorsa soğurma olmaz. Yayma ise akı gerektirmez. Soğuk hidrojenin Hα'yı soğurmaması ama H II bölgelerinin onu en parlak optik çizgi olarak yayması bu asimetrinin doğrudan görünümüdür.
* **Stokes kayması** (soğurulan ritimden daha düşük bir ritmin yayılması) doğaldır: biriken enerjinin bir kısmı boşalmadan önce alıcı girdabın iç gevşemesine gider.
* **Uyarılmış boşalma ve kazanç** mümkündür: önceden yüklü zarflar, geçen bir katarla eşzamanlı boşalmaya tetiklenebilir.
* **Bir çizginin soğurmada mı yaymada mı görüneceği atomun değil ortamın özelliğidir** — Güneş fotosferinde soğurmada olan Na D çizgileri kromosferde aynı atomla yaymaya döner.

**Buna karşın çizgi konumları her iki yönde de aynıdır**, ve bunun nedeni karşılıklılık değildir: konumları belirleyen şey atomun örgüsünün açtığı **ritmik pencerelerdir**, ve aynı pencere kümesi her iki yönde de **aynı kapıdır** (9.11.6–9.11.7). Kısaca: **konumlar ortak kapıdan, hızlar yönden.** Kirchhoff–Bunsen'in çizgi konumlarındaki örtüşmesi için ortak kapı yeterlidir; zamanda tersinirlik gerekmez — ve gerekmemesi iyidir, çünkü tersinir bir çatı kendiliğinden yaymayı, Stokes kaymasını ve kazancı **imkânsız** kılardı.

Bunun bedeli açıktır ve envanterdedir: yön bağımlı olan **hızlar** (kendiliğinden/uyarılmış salınım oranı, $g$-faktörleri, $\nu^3$ ölçeklemesi) bu bölümde türetilmemiştir — 7.4, madde 6-c.

### Enerji Merdiveni: $h\nu$ Bir Toplamdır

Anatominin en keskin sonucu, $E=h\nu$'nün teorideki katmanlı okunuşudur:

| Basamak | İfade | Değer | Karakter |
|---|---|---|---|
| **Taşınan** (Zerre başına) | $E_{Zerre}=\tfrac12 m_z(c_0^2+k_a v_{cev}^2)=m_zc_0^2$ | **8,25 eV** (öteleme 4,12 + dönme 4,12) | frekanstan bağımsız, evrensel |
| **Aktarılan alt birim** (vuruş başına) | $\delta=\eta\cdot E_{Zerre}$ | $\approx5{,}4\times10^{-4}$ eV | gerçek alışveriş kuantumu; alıcıya özgü ($\eta=4m_z/M$) |
| **Pencere toplamı** | $h\nu=\delta\cdot N$, $\;N=\nu\tau$ | frekansla ölçeklenir | gözlemin "kuantum" dediği **türetilmiş toplam** |

Standart fizik $E=h\nu$'yü tek taşıyıcıya doldurur: mavi "foton", kırmızıdan içkin olarak daha enerjik bir cisimdir. Teoride mavi ışığın Zerresi ile kırmızınınki **aynı enerjiyi taşır**; mavi katar yalnız daha sık atar. Frekans enerjiye değil **sayıma** girer: $E=\delta\cdot(\nu\tau)$ — $\nu$, evrensel pencereye kaç vuruşun sığdığını sayar. Formül iki kuramda aynı sayıyı verir ama zıt gramerle okunur: orada bir cismin niteliği, burada bir sürecin bütçesidir. Enerji, katarın $N$ vuruşuna taksit taksit **dağılmıştır**; toplam, ancak bir pencere kapandığında "kuantum" olur. (Taşınan ile teslim edilebilir olan da ayrılmalıdır: dilimin sırtındaki toplam $N\cdot E_{Zerre}$, teslim edilebilir $h\nu$'nün ~$10^4$ katıdır; alıcı yalnız $\eta$ kesrini alabilir, gerisi geri seker — ışınım basıncı muhasebesinin konusu, 9.4.8/i.)

Bu dağıtımın dört dolaysız sonucu vardır:

1. **Zamana yayılma:** teslimat anlık bir "kuantum sıçraması" değil, $\tau$ boyunca $N$ mikro-adımlık birikimdir. İki resmi ayırt edebilecek tek yer, pencerenin içine bakabilen ultrakısa-atım rejimidir (9.4.8/v).
2. **Uzaya yayılma:** pencere diliminin fiziksel boyu vardır — $L=c_0\tau\approx2{,}3$ mm. "Foton" teoride nokta değil, milimetrelerce uzun bir mermi dizisidir; 2.6.5'in wake taahhüdünün (dilim tek kolda, wake iki kolda) doğal zemini budur. Bu, teorinin tek başına taşıdığı cesur bir öngörü de değildir: standart fiziğin kendi yerleşiklik teoremleri de "foton"un noktasal olamayacağını söyler — kütlesiz spin-1 için konum operatörü tanımlanamaz ve sonlu-$N$ durumları hiçbir bölgeye hapsedilemez (9.10.5). İki çatı burada aynı sonuca varır; ayrım, teorinin yayılmışlığa bir **boy** ve bir **mekanik** vermesindedir.
3. **"Yarım foton neden yok?" sorusunun çözümü:** enerji zaten bölünmüş gelir ($\delta$'lara); bölünemeyen ışık değil, **sayacın kapanma koşuludur** — yarım pencere = kopma yok = klik yok. Kesiklilik toplamda değil, eşiktedir.
4. **Renk–enerji ayrışması:** renk saf ritimdir; "enerji", o ritmin belli bir pencereyle okunmasıdır. $\delta$ hedef kütlesine bağlı olduğundan aynı katar, farklı alıcıya farklı enerji okutur — enerji-frekans bağı ışığın değil, **buluşmanın** özelliğidir (kaymış/kaymamış Compton çizgisi ikilisi, 9.4.5/c, bu çifte-özgülüğün ölçülmüş hâlidir).

Dürüst kayıt: "her Zerre'ye $\delta$" ortalama ifadedir — $\delta$ kafa-kafaya üst sınırdır, eğik vuruşlar daha az aktarır (M-10); dağıtım eşit-pay değil, istatistiksel-paydır. Dilim boyunun ($c_0\tau$) optiğin kaynağa göre mikrometreden kilometreye değişen koherans uzunluğuyla ilişkisi ise hesap ister ve açık kalemdir (9.2.7/vi).

## 9.2.3 Evrensellik: Eğim Neden Malzemeden Bağımsız

Millikan doğrusunun en sert içeriği eğimin **evrenselliğidir**: sodyumda da bakırda da aynı $h$. Muhasebe bunun nedenini doğrudan gösterir:

$$E_{ke} = (\delta\tau)\,\nu - \Phi$$

Malzeme bu denkleme yalnız $\Phi$ (bağlanma enerjisi) üzerinden girer — kesme noktasını kaydırır, eğime dokunamaz. Eğimi taşıyan iki büyüklüğün ikisi de malzemenin değil **alıcının** malıdır: $\delta$, Zerre–elektron çarpışma kinematiğidir; $\tau$, elektron-girdabın kendi kopma penceresidir. Alıcı her fotoelektrik olayda aynı cisim (elektron) olduğu için çarpım evrenseldir. Bu aynı zamanda sınanabilir bir kırılganlıktır: $\tau$'nun malzemeye ya da frekansa zayıf bir bağımlılığı, doğrusallıktan ölçülebilir bir sapma üretir (M-11 geçerlilik sınırı) — hassas fotoelektrik spektroskopi, pencere modelinin keskin sınav penceresidir.

## 9.2.4 Karacisim Işıması: $h$'nin Doğum Yeri

$h$ tarihe fotoelektrikle değil, karacisimle girdi. 1900'de Planck, denge ışıması spektrumunu ancak duvar "osilatörlerinin" enerjiyi $h\nu$'lük paketlerle alıp verdiğini varsayarak türetebildi (Planck, 1901); klasik eşbölüşümün her moda $k_BT$ vermesi, yüksek ritimde ıraksıyordu — morötesi felaketi. Planck kuantalamayı **duvara** yazmıştı; onu ışığın kendisine taşıyan, 1905'te Einstein oldu ve standart fiziğin "foton"u böyle doğdu.

Teorinin okuması nettir: **Planck'ın ilk adresi doğruydu.** Karacisim duvarındaki "osilatörlerin" fiziksel kimliği bellidir — elektron-girdaplar; ve alışveriş birimleri pencere ısırığıdır. Duvar, katardan ancak tam pencere alışverişleriyle ($E=(\delta\tau)\nu$) enerji alır ve Zerre Paketleri hâlinde geri yayar (9.2.1). Morötesi felaketinin mekanik çözümü buradadır: eşbölüşüm, duvar ile alan arasında **sürekli** (istenildiği kadar küçük) enerji alışverişi varsayar; pencere mekaniğinde yüksek ritimli bir mod duvarla ancak $(\delta\tau)\nu$'lük **büyük ısırıklarla** konuşabilir ve denge istatistiğinde bu ısırıkların uyarılması $e^{-h\nu/k_BT}$ ile bastırılır. Planck biçimi bu bastırmanın sonucudur; Rayleigh–Jeans yalnız $h\nu\ll k_BT$ limitinde — ısırığın süreklilik gibi göründüğü yerde — geri gelir.

Dürüst kayıt: bu zincirin iki halkası standart girdidir — denge istatistiği (Boltzmann ağırlığı) ve kovuk mod sayımı ($8\pi\nu^2/c^3$, standart fizik yazımı). İkincisinin teori-içi karşılığının (kovuk içindeki katar konfigürasyonlarının sayımı) türetimi açık kalemdir (9.2.7/iii). Dolayısıyla bölümün buradaki iddiası spektrumun baştan sona teori-içi yeniden türetimi değil, **kuantalama biriminin kimliğidir**: karacisimdeki $h$, fotoelektrikteki $h$ ile aynı $\delta\tau$ çarpımıdır. Bu, çarpımın üçüncü bağımsız olgu ailesinde kenetlenmesidir — sökme olayı (fotoelektrik), saçılma olayı (Compton) ve **denge ışıması** (karacisim), üçü de aynı pencere birimini okur. Dördüncüsü Casimir'dir: iki rampanın kesilmesinden doğan kuvvetin katsayısındaki $\hbar$, aynı $\delta\tau/2\pi$ kimliğiyle okunur (9.5.5) — aynı [S] statüsüyle, yani türetim değil özdeşleştirme olarak. Kozmolojik dipnot: evrenin bugüne dek ölçülmüş en kusursuz karacisim spektrumu CMB'dir (Mather ve ark., 1994; Fixsen, 2009); pencere mekaniği alıcıya ait ve evrensel olduğundan, denge ışımasının her ölçekte aynı biçimde çıkması teorinin doğal beklentisidir — kozmolojik bağlamın kendisi (CMB pik iskeleti ve 2,725 K'nin soğuma bütçesi hesabı dahil) Kısım 3.7'nin konusudur.

## 9.2.5 Diğer Arenalar: $\hbar$, Belirsizlik, Madde Dalgaları

$h$ optikle sınırlı değildir; durum envanteri dürüstçe ayrıştırılmalıdır:

- **Kurulu:** $\hbar=\delta\tau/2\pi$ tanımı ve belirsizlik bağıntılarındaki rolü (2.10.2) — pencere mekaniğinin doğrudan uzantısı.
- **Kısmen kurulu:** çift yarıkta $h$'nin görünümü — katar ve deplasman havuzu girişim geometrisi 9.3'ün konusudur.
- **Açık:** madde arenasında $h$ — de Broglie bağıntısının ($\lambda=h/p$, elektron kırınımı) girdap mekaniğinden ilk-ilke türetimi. Işık tarafında $h$'nin anatomisi pencere alışverişiyse, kütleli girdapların "dalga boyu"nun aynı çarpımı okumasının mekanik nedeni henüz türetilmemiştir (9.2.7/v).

## 9.2.6 Ayrıştırma Programı: Kilitten Öngörüye

Bugünkü durum bir **iç tutarlılık kilididir**: $\delta\tau$ çarpımı fotoelektrik eğimden sabitlenir; Compton, karacisim ve Casimir aynı çarpımı bağımsız ailelerde geri okur; ama $\delta$ ile $\tau$ ayrı ayrı ölçülmemiştir (rozet [S], Ek C). $\delta$'nın bileşenleri kuruludur — $k_a=1/2$ ve $v_{cev}=\sqrt2\,c_0$ türetilmiş, $m_z$ ise teorinin ölçülen girdi parametresidir; dolayısıyla $\delta=\eta\,m_zc_0^2$ kapalı hesaplanır ve $\tau=h/\delta$ zorunlu çıkar.

**Ayrıştırmanın bugün bile ödediği bir bedel vardır ve altı çizilmelidir: $h$'ın evrenselliği.** Standart fizikte "$h$ her yerde aynıdır" bir **postülattır** — nedeni sorulmaz, sorulamaz. Bu teoride ise **açıklanmış bir sonuçtur:** $\delta$ evrenseldir (yalnız $m_z$, $m_e$ ve $c_0$'den kurulu), $\tau$ evrenseldir (alıcı elektronun kendi penceresi, malzemeye bağlı değil), dolayısıyla çarpımları da zorunlu olarak evrenseldir. Bu ayrıca bir tutarlılık kilididir: $\tau$ malzemeye göre değişen bir büyüklük olsaydı $h$ da malzemeye göre değişirdi — ölçüm bunu $10^{-9}$ düzeyinde dışlar. Yani teori $h$'ın *değerini* öngörmese de, standart fiziğin sormadığı bir soruyu — **neden tek bir sayı?** — cevaplar.

**Kilidin öngörüye dönüşmesi tek bir sayıya bağlıdır.** Teori $\tau$ için keskin ve malzemeden bağımsız bir değer söyler:

$$\boxed{\tau = \frac{h}{\delta} \approx 7{,}7\ \text{ps}}$$

$h$'ı hiç kullanmayan bağımsız bir $\tau$ tayini bu sayıyı doğrularsa, $h=\delta\tau$ bir ayrıştırmadan **sayısal öngörüye** dönüşür; çürütürse teori bu olgu ailesinde **yanlışlanır**. Bugünkü statüsünün dürüst adı budur: kusur değil, *tek sayıya indirgenmiş yanlışlanabilir bir tahmin.* İkinci keskin sınav ise $\lambda_C=\delta\tau/m_ec$'nin fotoelektrikten hiç veri almadan hesaplanmasıdır (9.4.7'nin sözü).

## 9.2.7 Açık Kalemler

Mekanizma kuruludur; aşağıdakiler hesap kalemleridir (tümü 7.4 envanterine (md. 19) bağlanır):

i. **$\tau$'nun $h$'tan bağımsız tayini — bu ailenin tek yapısal kalemi.** Kalem bir eksik değil, 9.2.6'da yazılan **yanlışlanabilir tahmindir**: $\tau=7{,}7$ ps. Kapanması iki yoldan biriyle olur — kopma penceresinin alıcı girdabın kendi dinamiğinden ilk-ilkelerle türetilmesi, ya da doğrudan zamanlama ölçümü.

   > **Aranan yerin haritası (elenmiş yollar).** $\tau$, teorinin bilinen zaman ölçeklerinin hiçbirine oturmaz ve bu, kalemin neden açık kaldığının dürüst gerekçesidir. Elektronun dönüş periyodu ($2\pi r_e/\sqrt2c_0 \approx 4\times10^{-23}$ s) ve Zerre'nin elektronu geçiş süresi ($\sim2\times10^{-23}$ s) **$10^{11}$ kat kısadır**; Zerre ölçeği ($r_z/c_0\approx8\times10^{-27}$ s) $10^{15}$ kat kısadır; ortamın viskoz sönüm süresi ($m_e/6\pi\eta_E r_e$, Satürn üst sınırıyla $\approx7\times10^{-6}$ s) $10^{6}$ kat uzundur. Atomik yapıya ait ölçekler (yörünge periyotları, $\sim10^{-16}$ s) hem $10^4$ kat kısadır hem de **evrensel değildir** — $Z$ ve $n$ taşıdıkları için $h$'ın evrenselliğiyle bağdaşmazlar ve bu gerekçeyle sayısal olarak elenmeden önce ilkece elenirler. Boşluğu kapatacak boyutsuz çarpan $10^{15}$ mertebesindedir; teorinin elindeki tek büyük boyutsuz sayı $1/\eta=m_e/4m_z\approx1{,}5\times10^4$ olduğundan bu, $(m_e/m_z)$'nin tam sayı olmayan bir kuvvetini gerektirir. **Bu yüzden $\tau$'ya bugün ayarlanmış bir çarpan zinciriyle değer biçilmemiştir ve biçilmemelidir** (Anayasa Madde 21: yama parametre yasağı). Aranacak yer, mevcut ölçeklerin arasında değil, henüz kurulmamış bir mekanizmadadır: kopma penceresi büyük olasılıkla tek bir geometrik/viskoz zamana değil, **kenetlenmenin çözülme sürecine** aittir.

   Yan kalem: vuruş geometrisi dağılımının (eğik çarpışmaların) $N$'ye etkisi.
iii. **Karacisim mod sayımının teori-içi türetimi:** kovuk içindeki katar konfigürasyonlarının sayımı ve Planck spektrumunun uçtan uca teori-içi yeniden türetimi — ithal edilen denge istatistiğinin pencere alışverişlerine uygulanabilirlik varsayımının denetimi dahil (yöntem kuralı: teoremler denetlenmeden ithal edilmez).
iv. **Paket varış fazı:** 2.6.5'in 50/50 istatistiğinin dayandığı düzgün faz dağılımının kaynak mekaniğinden türetimi (M-11 açık ucu).
v. **Madde arenasında $h$:** de Broglie bağıntısının girdap mekaniğinden türetimi (9.3 ile ortak cephe).
vi. **Dilim boyu ve koherans:** pencere diliminin fiziksel boyu ($L=c_0\tau\approx2{,}3$ mm, evrensel) ile kaynak türüne göre µm–km arasında değişen optik koherans uzunluğunun ilişkisi; muhtemel çözüm hattı, dilim-içi faz ortaklığı ile **dilimler-arası** wake-kilit korelasyonunun ayrıştırılmasıdır (lazer: dilimler kilitli ↔ termal kaynak: kilitsiz) — mekaniğin türetimi açıktır.

---

**Bölüm özeti:** Planck sabiti teoride temel bir sabit değil, iki mekanik büyüklüğün çarpımıdır: tek-vuruş aktarımı $\delta$ ile alıcı girdabın kopma penceresi $\tau$. Kesiklilik ışığın değil etkileşimin özelliğidir — "foton", cisim değil pencerelik alışveriştir; yayım tarafındaki karşılığı Zerre Paketi'dir. Enerji katara yayılmıştır: $h\nu$, tek bir taşıyıcının niteliği değil, $N=\nu\tau$ vuruşluk taksitin pencere toplamıdır — frekans enerjiye değil sayıma girer. Eğimin evrenselliği, $\delta$ ile $\tau$'nun malzemenin değil alıcının malı olmasından zorunlu çıkar. $h$'nin doğum yeri karacisimde Planck'ın kuantalamayı duvara yazan ilk sezgisi teorinin sonucuyla örtüşür: morötesi felaketini çözen şey ışığın taneciklenmesi değil, duvar penceresinin ısırık büyüklüğüdür; böylece fotoelektrik, Compton, karacisim ve Casimir — dört bağımsız olgu ailesi — tek $\delta\tau$ çarpımı üzerinde kenetlenir. Çarpımın iki bileşene ayrıştırılması (7.4), kilidi bağımsız öngörüye çevirecek anahtardır ve teorinin bu cephedeki açık işidir.
