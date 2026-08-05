# 4.2 Evrenakı'nın Matematiksel Modeli — IV: Modelin Sınırları ve İtirazlara Cevaplar (4.2.12–4.2.17)

## 4.2.12 Değerlendirme ve Modelin Sınırları
Geliştirilen bu matematiksel model:
* Newton'un (1687) $1/r^2$ yasasını hidro-mekanik bir sonuç olarak türetir.
* Göksel hareketleri 3 boyutlu basınç bileşenleri üzerinden inceler.
* Galaktik rotasyon eğrilerindeki düzleşmeyi logaritmik basınç kuyusu ile temellendirir.
* Evrenin genişlemesini Süreklilik ve Euler denklemlerindeki diverjans ve basınç gradyanı ile açıklar.

Ancak bilimsel standartlar gereği modelin limitleri dikkate alınmalıdır:
* Klasik Görelilik (Relativity) teorisinin soyut uzay-zaman geometrisinin, Evrenakı'nın somut hidrodinamik stres tensörlerine (matematiksel tercümesine) dönüştürülmesi üzerine daha fazla analitik çalışma yapılmalıdır.
* İleri sürülen hidrodinamik etkiler, bağımsız kozmolojik gözlemlerle test edilmelidir.
* $\alpha$ ve $\gamma_N$ gibi parametrelerin fiziksel doğası daha detaylı analitik modellere oturtulmalıdır.

## 4.2.13 Özet: Rejim-Bağımlı Fiziksel Çerçeve
Gözlemlediğimiz yörünge mekaniği, içinde bulunduğumuz Evrenakı ölçeğinin yerel bir tepkisidir.

| **Rejim (Ölçek)** | **Fiziksel Koşul** | **Evrenakı Yoğunluk Profili ($\rho$)** | **Cosmofluid Net Etki Eğilimi** | **Gözlemsel Sonuç** |
| :--- | :--- | :--- | :--- | :--- |
| **Güneş Sistemi** | Homojen, Kaynaksız, Radyal Simetrik | $\rho \approx$ Sabit | $F \propto 1/r^2$ (Gauss Yüzey Dağılımı) | Kepler Yörüngeleri |
| **Spiral Galaksiler** | Bileşik (Rankine-tipi) Girdap, Asimetrik Sürüklenme | $\rho \approx$ Sabit ($k \ll 1$; bkz. 4.2.9.2) | iç: $F \propto r$; dış: $F \propto 1/r$ (Logaritmik Çukur) | Yükselen iç kol + Düz Rotasyon Eğrisi |
| **Kozmik Ağ** | Global Diverjans, Basınç Gevşemesi | Hacimsel Genleşme | $v \propto r$ (Merkezkaç Genişleme) | Hubble Akışı |

**Sonuç:** Evrenakı modelinde kuvvetler evrensel sabitlerle değil, ortamın yerel dinamiğiyle belirlenir. Sistem, içinde bulunulan Euler ve Süreklilik rejimine göre gözlemlenen itim davranışını otomatik olarak üretir.

## 4.2.14 Bir İtiraf: Matematiksel Karmaşıklık ve Gelecek Vizyonu

Görüldüğü üzere Evrenakı (Cosmofluid) teorisi, evrenin işleyişini klasik mekanikteki $F = G \frac{m_1 m_2}{r^2}$ denklemi gibi izole, statik ve basit birkaç formülle kestirip atılabilecek bir sığlıkta görmez. Aksine, doğanın gerçek yüzü olan akışkanlar mekaniğinin o muazzam ve kaotik karmaşıklığını kucaklar.

Burada sunulan hidrodinamik denklemler, sistemin sadece en idealize edilmiş, temel iskeletidir. Gerçekte, bir gezegenin veya bir galaksinin etrafındaki Evrenakı vorteks yapısı 3 boyutlu, asimetrik, türbülanslı ve inanılmaz derecede non-lineer (doğrusal olmayan) sürüklenme süreçleri içerir. Sadece tek bir galaktik vorteksin tüm akış çizgilerini, basınç haritalarını ve sınır tabakası sürtünmelerini tam anlamıyla hesaplayabilmek için bile her bir özel vaka adına ayrı kalın kitaplar yazılmak, devasa Hesaplamalı Akışkanlar Dinamiği (CFD) simülasyonları yapılmak zorundadır.

Bu nedenle, kitabın bu bölümünde Evrenakı'nın sadece "temel matematiği ve iskeleti" işlenmiş, denklemlerin o kaotik ve boğucu detaylarına bilerek girilmemiştir. Klasik fiziğin matematiği basit ama hatalıdır; Evrenakı hidrodinamiği ise çok daha karmaşık olmakla birlikte doğanın işleyişine sadık kalır. Bu kozmik okyanusun tüm spesifik denklemlerinin çözümü, bu çerçeve üzerinde çalışacak gelecekteki araştırmalara açık bir alandır.

## 4.2.15 G Sabiti Paradigmasının Sınırları ve Klasik Fiziğin İtirazlarına Cevaplar

Kütle-itimin salt bir Evrenakı basıncı ($\mathcal{G} = \alpha/\rho_n$, bkz. 4.2.4) olduğunu gösterdikten sonra, klasik fiziğin ana akım savunucularından gelebilecek en sert 5 eleştiriyi ve bu eleştirilerin Evrenakı mekaniğiyle nasıl karşılandığını incelemek şarttır:

### İtiraz 1: "Eğer $G$ sabit değilse ($\alpha/\rho_n$ ise), neden Güneş sistemindeki yörüngeler kusursuzca $6.67 \times 10^{-11}$ sabitine uyuyor?"

**Evrenakı'nın Cevabı:** Güneş Sistemi dediğimiz lokal bölge, Evrenakı okyanusunun içinde nispeten stabil bir "havuzdur". Bu havuzun içinde arka plan Evrenakı basıncı ($\alpha$) homojene yakındır. Ayrıca gezegenlerin yapıldığı baryonik maddenin (atomların) Evrenakı ile olan aerodinamik sürtünme kesiti ($\gamma_N$), nükleon sayısıyla doğru orantılı olarak büyür. Yani $\gamma_N / m$ oranı standart madde için sabittir. Bizim lokal Güneş Sistemimizde $(\gamma_N/m)\,\alpha = \alpha/\rho_n$ oranı bu yüzden sabit "görünür". 
Eğer $G$ gerçekten evrensel bir sabit olsaydı, devasa galaksilerin dış kollarındaki yıldızların çok yavaş dönmesi gerekirdi. Klasik fizikçiler yıldızların neden hızlı döndüğünü açıklayamadıkları için "Karanlık Madde" teorisini varsaymışlardır. Oysa Evrenakı çok nettir; galaksinin dış çeperlerinde ortam basıncı ($\alpha$) ve girdap dinamikleri değişir. Dolayısıyla oradaki kütle-itim (yani efektif $G$) Güneş sistemindekiyle aynı değildir!

### İtiraz 2: "Galileo'nun deneyinde gösterildiği gibi 1 kiloluk demir de, 10 kiloluk demir de aynı hızda düşer. Eğer aerodinamik sürtünme/direnç ($\gamma_N$) varsa, büyük olanın farklı hızda düşmesi gerekmez mi?"

**Evrenakı'nın Cevabı:** Eleştirmenler burada hava sürtünmesi ile "Evrenakı sürtünmesini" birbirine karıştırmaktadır. Klasik aerodinamikte rüzgar sadece cismin dış yüzeyine çarpar. Ancak Evrenakı o kadar ince bir süper-akışkandır ki, atomların arasındaki devasa boşluklardan geçerek doğrudan atom çekirdeklerine (nükleonlara) sürtünür. 
10 kiloluk bir demirde, 1 kiloluğa göre 10 kat daha fazla nükleon vardır. Dolayısıyla Evrenakı içindeki aerodinamik sürtünme kesiti ($\gamma_N$) 10 kat büyüktür ve onu iten Evrenakı basınç kuvveti de 10 kat fazladır. Ama aynı zamanda eylemsizliği (ivmelendirilmesi gereken kütlesi) de 10 kat fazladır. İten kuvvet 10 kat artarken, direnç gösteren kütle de 10 kat arttığı için oran ($F/m = a$) eşitlenir ve ikisi de aynı hızda düşer. Newton buna "Eylemsizlik Kütlesi = Kütle Çekim Kütlesi" diyerek mekanizmasız bir etiket yapıştırmıştır. Bunun fiziksel sebebini ilk defa Evrenakı'nın içsel nükleon sürtünmesi ($\gamma_N$) açıklamaktadır.

### İtiraz 3: "Eğer hız düştüğü için 1.75 sapma oluyorsa, Güneş'in yanından çok hızlı giden kütleli bir göktaşı geçseydi o neden 2 kat keskin dönmüyor?"

**Evrenakı'nın Cevabı:** İşte Zerre Katarı'nı (Zerre'yi) atomik/kinematik kütleden ayıran sır tam olarak buradadır! 
Göktaşları (veya herhangi bir atomik kütle), kendi kütle enerjisiyle hareket eder ve tamamen Newtonyen eylemsizliğe tabidir. Kütleler Evrenakı içerisinde hareket ederken, boşluk veya seyrek Evrenakı onlara "engel" olmaz; tam tersine az yoğun bir ortama (Güneş'in deplasman bölgesine) girdiklerinde aerodinamik **sürtünmeleri çok daha azalır.** Bu yüzden kütleli bir göktaşı hızını ve momentumunu kolayca koruyup, Newton'un öngördüğü klasik radyal yörüngeye (0.875 yay saniyelik sapmaya) sadık kalır. 

Oysa Zerre'nin (Işığın) kendine ait "canlı" ve tutunmaya dayalı bir hareket mekanizması vardır. Zerre ilerlemek için Evrenakı'ya "diş geçirmek" (grip) zorundadır. Az yoğun bir ortama girdiğinde göktaşının aksine rahatlamaz; tutunmasını kaybeder, doğrusal hızını yitirir ve boşa dönerek **patinaj yapmaya** başlar. Kütleler seyrek uzayda eylemsizliğini korurken, Zerre seyrek uzayda hız kaybına uğrar; göktaşının savrulma katsayısı bozulmazken Zerre'nin hantallığı kırılır ve radyal basıncın mengenesine düşer. Bu mekanizma, kütle ile hidrodinamik Zerre katarı arasındaki en kusursuz ayrım çizgisidir.

**2 çarpanının nicel kaynağı (türetildi).** "Virajı iki kat keskin döner" ifadesi bir analoji değildir; çarpan türetilmiştir ve kaynağı teorinin ölçek yapısıdır (**Ek M-42**): madde ölçeği $\Lambda = 1-\Phi/c^2$ cetvel ve saatleri yönetirken, Zerre'nin arka plandaki yayılma hızı $\Lambda$'nın **karesiyle** ölçeklenir:

$$c_{loc} = c\,\Lambda^2 \quad\Longrightarrow\quad n_{eff} = \frac{1}{\Lambda^2} = 1 + \frac{2\Phi}{c^2}$$

Fermat ilkesi bu indisle uygulandığında Güneş kenarı için:

$$\delta = \frac{4GM_\odot}{c^2 R_\odot} = \mathbf{1{,}7512''}$$

— ölçülen $1{,}7510''$ ile birebir. Yarım indis ($n=1+\Phi/c^2$) kullanılsa Soldner'ın klasik $0{,}876''$ değeri çıkardı; iki kat, Zerre'nin yayılma hızının madde ölçeğinin karesiyle gitmesinden gelir. Aynı yapı, aynı çarpanla, Gravity Probe B'nin jeodetik presesyonunu (~6.606 mas/yıl, ölçüm $6.601{,}8\pm18{,}3$) ve Shapiro gecikmesini de verir; PPN dilinde $\gamma=1$'e denktir. *(Kalan kalem: Merkür günberi kayması için ayrıca $\beta$ parametresi — ortamın ikinci mertebe tepkisi — gerekir; bkz. Bölüm 7.4 md.12.)*

### İtiraz 4: "Gezegenlerin ve Yıldızların Etrafındaki Bu Devasa Evrenakı Vortekslerini Sürekli Döndüren Motor (Kaynak) Nedir?"

**Evrenakı'nın Cevabı:** Evrenakı teorisinin ve sarmal galaksilerin hidrodinamiğinde göz ardı edilmemesi gereken en kritik olgu **Çekirdek Dönüşü (Core Rotation)** mekanizmasıdır. Klasik fizikte Dünya'nın veya Güneş'in kendi etrafında dönmesi sadece günü belirleyen basit bir kinematik olaydır. Oysa Evrenakı'da gökcisimlerinin ultra-yoğun sıvı veya katı metalik çekirdeklerinin muazzam bir hızla fırıldaması, bizzat etraflarındaki uzayı (Evrenakı okyanusunu) fırıldak gibi çeviren **ana motordur**. 
Eğer Dünya'nın merkezindeki demir-nikel çekirdek dönmeyi bırakırsa, etrafındaki Evrenakı girdabı (vorteksi) zamanla sönümlenir. Girdap sönümlendiğinde, Bölüm 4.2.7'de işlediğimiz o "eksenel basınç ve ekvatoral şişkinlik" yavaşça çöker. Galaksileri kollar halinde döndüren ve "Karanlık Madde" hipotezinin öne sürülmesine sebep olan o devasa girdap da aslında Galaksi merkezindeki devasa Süper Kütleli Çekirdek'in dönüşüyle Evrenakı'ya aktarılan torktur. Kütle-itim (Vorteks dinamiği) gücünü kütlenin durağan varlığından değil, çekirdeğin muazzam dönüşünden alır!

### İtiraz 5: "Modern Lorentz-ihlali deneyleri (dönen optik rezonatörler — Herrmann ve ark., 2009; Nagel ve ark., 2015; Kennedy–Thorndike düzenekleri — Kennedy & Thorndike, 1932; optik saat karşılaştırmaları — Chou ve ark., 2010) tercihli bir referans çerçevesinin ve ışık hızındaki değişkenliğin etkilerini $10^{-16}$–$10^{-18}$ düzeyinde dışlamıştır. Evrenakı mutlak bir kozmik ortam ve değişken bir $c$ öneriyorsa, bu ortam neden hiçbir hassas deneyde görünmüyor?"

**Evrenakı'nın Cevabı:** Bu itiraz, teorinin en ciddiye alınması gereken sınavıdır ve dört ayrı katmanda cevaplanması gerekir. Cevabın ilk üç katmanı sağlam bir zemine oturur; dördüncü katman ise teorinin açık bir sınama programı olarak sahiplendiği yüktür.

**(1) Bu deneylerin çürüttüğü ortam, Evrenakı değildir.** Kritik ayrım gözden kaçırılmaktadır: 19. yüzyılın esiri (aether) **sıkıştırılamaz** bir ortam olarak tasarlanmıştı — yoğunluğu her yerde sabitti. Böyle bir ortamda $c=\sqrt{P/\rho}$ değişemez; dolayısıyla tek gözlemlenebilir büyüklük, ortama göre **hareketinizdir** (esir rüzgârı). Michelson–Morley'den (Michelson & Morley, 1887) modern dönen rezonatörlere (Herrmann ve ark., 2009; Nagel ve ark., 2015) kadar uzanan deney geleneği, tam olarak bu **hareket** büyüklüğünü sıfırlamıştır ve bu yüzden sıkıştırılamaz esiri gerçekten de tarihe gömmüştür. Evrenakı ise 1. Postülat gereği **sıkıştırılabilir** bir süper-akışkandır: yoğunluğu sabit bir arka plan değil, dinamik bir alandır ($\rho(\mathbf{r},t)$). Bu, sıkıştırılamaz esirin sahip olmadığı bir serbestlik derecesidir ve teorinin imzasını **hareketten** değil, **ortamın kendi hâlinden** doğan bir büyüklüğe taşır. (Kütle yakınında hem $P$ hem $\rho$ birlikte düştüğü hâlde $c=\sqrt{P/\rho}$'nin yönünü sabitleyen kural için bkz. Bölüm 2.4.2 "Yön kuralı": $k<1$ eşlik oranı gereği basınç daima daha hızlı düşer ve $\delta c/c = \tfrac{1-k}{2}\,\delta P/P_0 < 0$.) "Lorentz testleri esiri çürüttü, öyleyse Evrenakı'yı da çürütür" çıkarımı bu yüzden geçersizdir: çürütülen şey, Evrenakı'nın ayırt edici özelliğinden yoksun bir modeldir.

**(2) Michelson–Morley sınıfı deneyler izotropiyi ölçer; sabitliği ölçmez.** Yaygın bir yanlış ifade, "Michelson–Morley ışık hızının sabit olduğunu kanıtladı" biçimindedir. Deneyin ölçtüğü şey bu değildir. MM ve onun modern ardılları (yüksek-finesse dönen kaviteler), düzenek **döndürülürken** iki dik kol arasındaki farkı arar; yani **yön anizotropisini** ölçer. Eğer $c$ değişir fakat her yönde eşit değişirse (izotropik değişim), saçak deseni kaymaz — düzenek buna **yapısal olarak kördür**. Evrenakı, sürüklenme zarfı gereği (bkz. Bölüm 3.4.5–3.4.6) zaten **sıfır anizotropi** öngörür. Dolayısıyla bu deney sınıfının null sonucu, teoriyle çelişmek bir yana, teorinin beklediği sonuçtur; ve teorinin asıl iddiası olan **zamansal/yoğunluğa bağlı** değişkenliği hiç sınamamaktadır.

**(3) Aynı ortamdaki saat karşılaştırmalarının null sonucu, teorinin öngördüğü sonuçtur.** Optik saat deneylerinin ölçtüğü büyüklük, boyutlu bir $c$ değeri değil, boyutsuz bir orandır (ince yapı sabiti $\alpha_{is}$ ve saat frekansı oranları; $\alpha_{is}$: ince yapı sabiti — teorinin gradyan bağlaşım sabiti $\alpha$'sından ayrıdır). Bu karşılaştırmalar **tek bir laboratuvarda, aynı yerel Evrenakı yoğunluğunda** yürütülür. Aynı ortamı paylaşan iki saat, yerel $P/\rho$ değiştiğinde **eşit oranda** etkilenir; etki ortak-modda (common mode) kalır ve oranlardan düşer. Dolayısıyla aynı-ortam null'u, Evrenakı'nın yanlışlanması değil, ortak-mod ilkesinin doğal sonucudur. Teorinin sınanacağı yer, aynı ortamdaki iki saatin *arası* değil, **farklı ortamların karşılaştırılmasıdır**.

Bu katman uzun süre niteliksel bırakılmıştı; **Ek M-42** onu türetilmiş bir sonuca dönüştürür. Potansiyel, bölgedeki cetveli ve saati aynı çarpanla ölçekler:
$$\Lambda \equiv 1-\frac{\Phi}{c^2}\,,\qquad \ell_{loc}\propto\Lambda\,,\qquad \nu_{loc}\propto\Lambda\,,\qquad c_{loc}=c\,\Lambda^2$$
Bir laboratuvarda ışık hızı ölçmek, kat edilen uzunluğu geçen süreye bölmektir; yani $c_{loc}/(\ell_{loc}\nu_{loc}) \propto \Lambda^2/\Lambda^2 = 1$. **Oran tam olarak birdir** — birinci mertebede yaklaşık değil, her mertebede tam. Bu yüzden $10^{-16}$–$10^{-18}$ düzeyindeki null sonuçlar teorinin **öngörüsüdür**; hassasiyet $10^{-30}$'a inse de değişmezler. Buna karşılık ölçeklenmeyen referans da açıkça belirlenmiştir: **maddi ortam** (cam, su, fiber) yalnız ışığın yolundaki $P/\rho$'yu düşürür, gözlemcinin cetvelini değiştirmez. Bu **diferansiyel** sınıf yerel olarak ölçülebilir ve zaten ölçülmüştür — Fizeau sürüklenme katsayısı ve $n=1/\sqrt{1-\phi}$ bağıntısı (Ek M-15, M-16) bu sınıfın niceliksel doğrulamalarıdır. Yani teori "neden görünmüyor?" sorusuna tek cümleyle cevap verir: **ortak-mod kısmı ilkece görünmez, diferansiyel kısmı ise zaten görünmüştür.**

**(4) Farklı ortamlarda ışık hızının değişkenliği zaten ölçülmüştür — ve teori bunu birebir üretir.** Yukarıdaki üçüncü maddenin işaret ettiği "farklı ortam" testi fizikte mevcuttur ve olumlu sonuç vermiştir. Farklı yükseklikteki (dolayısıyla farklı Evrenakı yoğunluğundaki) atomik saatlerin farklı tiklediği, 33 santimetrelik yükseklik farkında dahi ölçülmüştür (Chou ve ark., 2010). Güneş'in yanından geçen radar sinyallerinin ölçülebilir biçimde geciktiği (Shapiro gecikmesi; Shapiro, 1964; Cassini ile en hassas ölçümü: Bertotti ve ark., 2003) ve kütle yakınından geçen ışığın yavaşlayıp büküldüğü (merceklenme; Dyson ve ark., 1920) yerleşik gözlemlerdir. Standart fizik bu verileri "uzay-zamanın eğriliği ve zamanın genleşmesi" diliyle okur; Evrenakı Teorisi ise aynı verileri **yerel Evrenakı yoğunluğunun ışık hızını değiştirmesi** olarak, ek bir geometrik varsayıma ihtiyaç duymadan üretir (bkz. Bölüm 6.2 ve Bölüm 4.3). **Dürüst kayıt:** Bu katmanda teori, standart fizikten *fazladan* bir öngörü sunmaz; aynı ölçümleri farklı bir ontolojiyle kapsar. Bu bir yorum eşdeğerliğidir ve teorinin tutarlılığının kanıtıdır — ancak tek başına ayırt edici bir sınav değildir.

**Kozmik çerçevenin çapası.** Teorinin "mutlak kozmik ortam" kavramı soyut bir varsayım olarak bırakılmamalıdır: Evrenakı'nın durgun çerçevesi, kozmik mikrodalga arka plan ışımasının dipol ölçümüyle belirlenen çerçeveyle özdeşleştirilir. Güneş sisteminin bu çerçeveye göre yaklaşık 370 km/s hızla hareket ettiği ölçülmüş bir olgudur. Bu hareket bir "esir rüzgârı" olarak görünmez — çünkü hem sürüklenme zarfı hem de 6.1'de türetilen fiziksel deformasyon mekanizmaları (boy kısalması ve saat yavaşlaması) mutlak hızı yerel gözlemden siler. Böylece teori, tercihli bir çerçeveye sahip olmakla anizotropi deneylerinin null sonucunu aynı anda taşıyabilir.

**Teorinin sahiplendiği yük ve yanlışlanma taahhüdü.** Yukarıdaki dört katman, itirazın kavramsal gücünü karşılar. Ancak teorinin en iddialı ayağı bunlarla tamamlanmaz: 4. Postülat, ışık hızının **yerel vakumda dahi** sabit olmadığını öne sürer ve Kısım 5'teki deney programı bunu doğrudan ölçmek üzere kurulmuştur. Bu iddia, mevcut Kennedy–Thorndike ve optik saat sınırlarıyla aynı arazide yarıştığı için, teori onu bir "yorum" olarak değil, **ayırt edici kontrollerle sınanacak yanlışlanabilir bir öngörü** olarak sahiplenir. Bu öngörünün kesin biçimi, sınama protokolü ve teorinin bağladığı yanlışlanma koşulu Bölüm 5.1'de ayrıca tanımlanmıştır (bkz. Bölüm 5.1 "Ayırt Edici Kontroller ve Yanlışlanma Taahhüdü"); açık nicel kalemler ise Bölüm 7.4'te listelenmiştir.

## 4.2.16 Genel Görelilik ve Evrenakı: Matematiğin Fiziksel Nedenselliği
Evrenakı teorisi, modern fiziğin ve Einstein'ın Genel Görelilik (GR) denklemlerinin ürettiği kusursuz matematiksel sonuçları (örneğin kara deliklerin dönüş limitlerini veya uzay-zaman eğriliklerini) **reddetmez.** Aksine, o denklemlerin astronomik gözlemlerle birebir uyuştuğunu kabul eder. 

Ancak Evrenakı'nın itiraz ettiği ve çözdüğü şey, **bu matematiğin arkasındaki fiziksel nedenselliktir (causality).**

Genel Görelilik, uzayın büküldüğünü ve cisimlerin bu geometrik eğriliğe göre hareket ettiğini söyler, ancak "boş uzayın nasıl olup da bükülebilen fiziksel bir doku gibi davrandığını" açıklamaz; sadece matematiğini kurar. Evrenakı teorisi ise o eksik olan "fiziksel aktörü" sahneye koyar: **Süperakışkan Uzay Dokusu (Evrenakı) ve 4. Boyut Mikro Dönüşleri.**

Genel Görelilik'teki o esnek, bükülen ve cisimleri bir arada tutan soyut "Uzay-Zaman Geometrisi", Evrenakı teorisinde devasa ve viskozitesi sıfıra çok yakın bir **Makro Vorteksin (Girdabın) Radyal Basıncıdır.** Evrenakı'nın nihai hedefi; Genel Görelilik'in gözlemlerle uyuşan kusursuz sayısal öngörülerini (örneğin Kritik Dönüş Limitlerini veya $r_{ISCO}$ değerlerini) reddetmek değil, tam aksine bu sayıları saf akışkanlar mekaniği denklemleri üzerinden bağımsızca türetmektir. Genel Görelilik olayı soyut bir matematiksel geometri olarak tanımlayıp bırakırken; Evrenakı teorisi, bu geometrinin arkasında yatan hidro-dinamik basıncı ve 4D spin motorunu ortaya çıkararak **"Matematiğe fiziksel bir vücut"** giydirmeyi amaçlar.

Kısacası bizler GR'nin (Genel Görelilik'in) gözlemlerle doğrulanan matematiğini reddetmiyoruz; o matematiği yaratan asıl "mekanik ve akışkan" nedenselliği felsefi olarak kuruyoruz. Bu programın ilk tamamlanmış örneği Bölüm 6.3.3'tür: *Gravity Probe B*'nin çerçeve sürüklenmesi ($37{,}2\pm7{,}2$ mas/yr; Everitt ve ark., 2011), saf akışkan denklemlerinden — Stokes rotleti artı yerel rotasyon vektörü $\tfrac12\nabla\times\vec v$ — 41,0 mas/yr olarak, ek serbest parametre üretmeden türetilmiştir (0,52σ; **Ek M-40**). Aynı program o günden bu yana GP-B'nin ikinci etkisini (jeodetik presesyon ~6.606 mas/yr; **Ek M-42**), LAGEOS düğüm kaymasını (30,6 / 31,4 mas/yr; **Ek M-41**) ve ışık bükülmesini ($1{,}7512''$; **Ek M-42**) da kapsamıştır — üçü de yeni serbest parametre üretmeden. Genel Görelilik'in ürettiği kalan sayıların (Merkür günberi kayması — ortamın ikinci mertebe tepkisi $\beta$'yı gerektirir; $r_{ISCO}$; kritik dönüş limitleri) aynı yolla bağımsızca türetilmesi, teorinin önündeki en büyük matematiksel sınav olarak durmaktadır. Ancak nedensellik (causality) açısından makro vorteks modeli, fizikteki "soyut geometriye" somut ve mekanik bir gerçeklik kazandırır.

## 4.2.17 Genel Göreliliğin Geometrik Çöküşü: Eksik Olan Basınç Kuvvetleri
Genel Görelilik (GR), uzay-zamanı bükülebilir esnek bir çarşaf gibi modelleyerek bazı kuvvetleri başarıyla geometrik kalıplara sığdırabilir. Nitekim matematiğinde gördüğümüz üzere GR, "merkezcil kuvvetleri" (cismi merkeze çeken kütleçekim eğriliğini) ve "eksenel kuvvetleri" (dönen kütlelerin uzayı peşinden sürüklemesi olan *frame-dragging* etkisini) bu soyut geometri üzerinden başarıyla tanımlayabilir. 

Ancak GR'nin en büyük açmazı, soyut esnek uzayı ne kadar bükerseniz bükün asla elde edemeyeceğiniz, sadece gerçek bir "akışkan" mekaniğinde var olabilecek eksik kuvvetlerdir. Evrenakı teorisi, GR'nin öngöremeyeceği iki devasa hidro-dinamik basınç kuvvetinin daha evrende aktif olarak iş yaptığını ortaya koyar:

1. **Kutupsal Yanal Sıkıştırma Kuvvetleri:** Dönen makro girdaplar, sadece ekvatoral düzlemde dönmekle kalmaz; akışkan mekaniği gereği kutuplardan (üstten ve alttan) ekvator düzlemine doğru devasa bir yanal sıkıştırma kuvveti uygularlar. GR'nin "uzay çukurunda" böyle kutupsal bir basınç karşılığı yoktur.
2. **Akışkanın Doğal Arka Plan Basıncı:** Uzay boşluğu gerçek bir süperakışkan (Evrenakı) olduğu için, zaten kendi içinde doğal bir statik basınca sahiptir. Herhangi bir girdap olmasa bile, akışkanın içine dalmış her kütle bu her yönden gelen omnidireksiyonel doğal sıkıştırmaya maruz kalır.

**Sonuç: Neden Galaksilerde GR Çöküyor?**
Sadece merkezcil ve eksenel kuvvetlerin (Güneş sistemi gibi nispeten küçük ölçeklerde) iş yaptığı yerlerde GR'nin matematiği çalışır ve gözlemlerle uyuşur. Ancak ölçek büyüyüp devasa galaksilere geçildiğinde; o galaksiyi bir arada tutan şey sadece merkezdeki karadeliğin kütleçekim eğriliği (merkezcil kuvvet) değildir. Asıl yapıştırıcı güç, devasa galaktik girdabın yarattığı kutupsal yanal sıkıştırmalar ve Evrenakı'nın statik arka plan basıncıdır. 

GR bu sıvısal basınç kuvvetlerini geometrisine dahil edemediği için galaksilerin dönüş hızlarını ve yıldızların savrulmamasını hesaplarken tamamen çöker. Bilim dünyası bu çöküşü (eksik kuvvetleri) telafi edebilmek için "Karanlık Madde" adında görünmez bir kütle icat etmek zorunda kalmıştır (illüzyonun vorteks çözümü için Bkz. 3.1.8). Özetle Evrenakı teorisi çok yönlü akışkan basınçlarını kapsayan kapsamlı bir hidro-dinamik paket sunarken; GR, bu devasa evrensel dengeyi ancak soyut varsayımlarla ve sadece iki kuvvet (merkezcil ve eksenel) üzerinden eksik bir şekilde modellemeye çalışır.
