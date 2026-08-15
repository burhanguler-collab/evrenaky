# 9.11 Atom Spektrumları ve Kesikli Yörüngelerin Hidrodinamiği

> **Bu bölüm nasıl okunur?** Kısım 9'un diğer bölümleri tek tek olguları (fotoelektrik, Compton, Casimir, polarizasyon) alıp mekanik karşılıklarını kuruyordu. Bu bölüm farklı bir iş yapar: **atomun kesikli yapısını** ele alır ve teorinin bu ailede neyi türettiğini, neyi girdi aldığını, neyi bir sonraki kitaba bıraktığını **tek yerde** toplar. Bölümün omurgası dağınık değildir ama kaynakları çoktur: kabuk geometrisi Mai tezinin ilk kitabından (Güler, *Atom Geometrisi*), duvar hızı yasası Postülat 5'ten, basınç topografyası Kısım 3'ten, pencere mekaniği 9.2'den gelir.

---

## 9.11.1 Olgu ve rakibin gerçek gücü

Isıtılan hidrojen her frekansta değil, yalnız belirli frekanslarda ışır. Balmer, Lyman ve Paschen serileri Rydberg biçimine uyar:

$$\frac{1}{\lambda} = R\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right)$$

ve $R_\infty$ bugün **bağıl $10^{-12}$ duyarlıkla** ölçülüdür; hidrojenin 1S–2S geçişi $\sim10^{-15}$ düzeyinde bilinir. Bu, fiziğin en hassas ölçülmüş nicelik ailelerinden biridir.

**Rakip hafife alınmamalıdır ve bu kayıt önemlidir.** Bohr (1913) kesikliliği gerçekten *postüla* etmişti; ama Schrödinger (1926) onu **türetti**: Coulomb potansiyelinde bağlı durum için dalga denklemi çözülür, dalga fonksiyonunun sonsuzda sıfıra gitmesi koşulu konur ve özdeğerler kendiliğinden kesikli çıkar. Kesiklilik standart çatıda bir varsayım değil, **sınırlı bölgeye hapsedilmiş dalga probleminin teoremidir** — telin belirli notaları vermesiyle aynı matematik.

Dolayısıyla teorinin iddiası *"kesikliliği biz açıklıyoruz, onlar açıklamıyor"* biçiminde kurulamaz. Standart çatının gerçekten açıklamadığı şey bir katman aşağıdadır: **dalga denklemi neden geçerlidir, $\hbar$ neden vardır.** Evrenakı'nın katkısı bu düzeydedir — kesikliliğin altındaki **mekanik tabanı** verir.

**Hangi barın aşılması gerekmediği de kaydedilmelidir.** Kapalı formda çözüm yalnız **tek elektronlu** sistemler için vardır (hidrojen ve H-benzeri iyonlar; Born–Oppenheimer içinde H₂⁺). Helyum 40 anlamlı basamağa **hesaplanmıştır** ama analitik çözümü yoktur; üç ve daha çok elektronlu sistemlerde de yoktur. "Her elementi ilk ilkelerden türetmek" diye bir başarı standart fizikte de mevcut değildir ve bu kitap böyle bir iddia taşımaz. **Hedef bar hidrojendir.**

---

## 9.11.2 Kesikliliğin adresi: çekirdek geometrisi

Standart kimya kabuk doluluk sayılarını (2, 8, 18, 32) **elektron tarafında** kurulan bir sayımdan çıkarır: $2n^2$, burada 2 spin eşleşmesinden, $n^2$ ise açısal momentum sayımından gelir.

Mai tezinin ilk kitabı bu sayıların **çekirdekteki proton diziliminin geometrik sonucu** olduğunu gösterir. İki proton hiçbir surette birbirine dokunamaz; aralarına elektrik yükü bakımından nötr olan nötron girmek zorundadır. Bu kısıt altında kararlı dizilim zincir değil **kare katmandır**: $k$'ıncı katman $(2k)^2$ konum taşır ve bunların yarısı protondur —

$$N_k = 2k^2 \;\Longrightarrow\; 2,\;8,\;18,\;32$$

Katmanlar aynı düzlemde değildir; **alt alta** dizilirler ve biri diğerinin en dış sırası çıkarılmış hâlidir, böylece iç içe geçebilirler. Birleşmede her protona bir nötron karşılık gelir. Katman toplamları soy gazların atom numaralarını verir: $2$, $2{+}8=10$, $2{+}8{+}8=18$, $2{+}8{+}18{+}8=36$, $54$, $86$, $118$ *(ayrıntılı türetim, şekiller ve element-element geometriler: Güler, Atom Geometrisi)*.

**İki kazanç kaydedilmelidir.** Birincisi, kabuk doluluğu artık elektron tarafında postüla edilen bir sayım değil, çekirdek geometrisinin okunuşudur — ve bu, 2.1'in "nükleon, atomun basınç gradyanlarının ana odağıdır" tespitiyle aynı yöne bakar. İkincisi, $2n^2$'nin içindeki **"2" spinden değil geometriden** gelir: kare ızgaranın yarısı protondur. Standart çatı o çarpanı ayrı bir bileşen olarak eklemek zorundadır; burada aynı sayı **bir varsayım eksiğiyle** çıkar.

---

## 9.11.3 Dışlama ayrı bir ilke değildir

Bir kabuk **tek yörüngedir**. O katmanın bütün elektronları aynı yörüngeyi paylaşır. Yörüngede dolanmayı çekirdek belirler; elektronların **birbirinden uzak durmasını kendi yükleri belirler** — aynı yolda olsalar bile karşılıklı itme aralarındaki mesafeyi eşit tutar.

$$\text{proton sayısı} \;\to\; \textit{kaç} \text{ elektron} \qquad \text{karşılıklı itme} \;\to\; \textit{nerede} \text{ duracakları}$$

**Verilmiş bir çember üzerinde** $N$ yükün eşit aralıklı dizilmesi klasik bir denge sonucudur; bu adımda tartışma yoktur. "Büyük $N$ için düzlemsel halka neden çökmüyor?" itirazı da karşılanır: **düzlem seçilmez, katman tarafından dayatılır** — serbest bir üç boyutlu minimizasyon değil, geometrik bir kısıt vardır.

Böylece "iki elektron aynı yeri tutamaz" olgusu ayrı bir dışlama ilkesine ihtiyaç duymaz. Teori burada **iki varsayım tasarruf eder**: spin eşleşmesi ve dışlama ilkesi.

---

## 9.11.3-b Örgü: yörünge deseni nasıl doğar

Buraya kadar kabuğun *kaç* elektron aldığı ve onların halka üzerinde *nasıl* dizildiği kuruldu. Ama bir soru henüz sorulmadı: **elektron neden bir yerde durur da başka bir yerde durmaz?** Cevap elektronda değil, ortamda yazılıdır — ve o yazıya **örgü** denir.

### Örgüyü çekirdek dokur

**(1) Çekirdek tek bir zarf değil, kaynak yığınıdır.** Kare katmanlar alt alta dizilir ve her katman **kendi düzlemindedir** (§9.11.2; radon için L2·L8·L18·L32·L18·L8). Her proton bir **Kaynak**tır: içinde vakum cebi taşır, çeperine yüksek yoğunluklu Evrenakı Rampası örer, akışkanı dışa pompalar (Anayasa Madde 25). Dolayısıyla atomun akış alanı **doğuştan küresel-simetrik değildir**; düzlemleri ve konumları belirli bir kaynak dizilimidir.

**(2) Çekirdek döner ve yalpalar.** Dönüş duvar hızı yasasındandır. Yalpalama ise bir kaza değil zorunluluktur: kuark yapısı taşıyan bir proton ideal küre olamaz, bileşik çekirdek hiç olamaz — dolayısıyla devinim **zorunludur** (Ö-5). Ve teorinin devinimi klasik rijit gövdenin konik presesyonu **değildir**: Postülat 5'in kaydı açıktır — eksen *koni değil, doğrusal* salınır (1.4.8). Örgüyü dokuyan hareket bir koni taraması değil, iki dik düzlemde bileşik bir salınımdır.

**(3) Sistematik hareket duran bir desen bırakır.** Kaynak dizilimi, dönüş ve doğrusal salınım rastlantısal değil belirlenimlidir. O hâlde dışa pompalanan akışkanın sırt-ve-oluk yapısı da rastlantısal değildir: yönelimi **kapalı bir figür** boyunca çevrim yapar. O figürün basınç alanına yazılmış hâli örgüdür — **duran oluklar dizisi**, yani izler. Elektron bir Kuyu olduğu için oluğa oturur, sırta oturamaz.

> **Ve izler, üzerlerinde elektron olmasa da vardır.** Örgü ortamın malıdır, işgalcinin değil. §9.11.4'ün merdiveni bu yüzden katmanın **kapasitesini** kullanır, fiilî doluluğunu değil — hidrojenin uyarılmış hâlleri de aynı merdivendedir.

### Kesikliliğin kaynağı: kapanma

Bir iz deseni ancak **kapanırsa** durur; çekirdek başlangıç duruşuna geri dönmelidir. Kapanmayan desen kendi kendini siler.

$$\text{duran iz} \;\Longleftrightarrow\; \text{açısal desen kapanır} \;\Longleftrightarrow\; \text{tamsayı koşulu}$$

**Teorinin kuantumlaması budur: açısal kapanma.** Standart çatıda $L=n\hbar$ bir postüladır (Bohr) ya da dalga fonksiyonunun sınır koşulundan gelir (Schrödinger); burada kapanma mekanik bir zorunluluktur — kapanmayan bir desen kalıcı olamaz.

### Küresellik: halka rijit, yönelim devinir

Halka bir bütün olarak korunur; devinen şey halkanın **normalidir**. Bir salınım çevriminde halka bütün yönelimleri süpürür ve kabuk bir **küre** olur.

> **Rijitlik zorunlu bir kısıttır, üslup tercihi değil.** Elektronlar halka yerine küreyi döşerse paketleme $4\pi r^2 = Na$ olur, $r\propto\sqrt N$ çıkar ve merdiven $1:2:3:4$'e döner — ölçülen $1:4:9:16$ ölür. Örgü halkayı **sürer**, dağıtmaz.

Ve süpürme elektronun gördüğü her ölçekte tamamlanır: çekirdeğin dönüş hızı $\Omega_p=\sqrt2c/r_p=5{,}05\times10^{23}$ rad/s mertebesindedir, ilk kabuğun dolanım ritmi ise 15 mertebe altındadır. Elektron bir tur atmadan yönelim çoktan taranmıştır. **Küresellik statik bir şekil değil, dinamik bir sonuçtur** — ve hidrojenin taban hâlinin küresel ölçülmesi bu yüzden teorinin öngörüsüdür.

**Katmanların eşdüzlemsizliği de buradan çözülür:** her katmanın halkası kendi küresini süpürür, atom **iç içe küreler** olur. Yığılmış diskler resmi terk edilir.

### Kapı: aynı desen, aynı küme

Örgünün deseni sabit olduğu için geçitleri de sabittir. Bir Zerre katarının örgüye girebilmesi desene uymasını gerektirir — ve **uyan çıkabilir de.** Kirchhoff–Bunsen'in çizgi konumlarındaki örtüşmesi bu yüzden bir tesadüf ya da bir tersinirlik varsayımı değil, **tek kapının iki yönde aynı kümeyi seçmesidir** (§9.11.8'in "konumlar ortak merdivenden" hükmünün mekaniği). Elementlerin parmak izi de aynı yerden gelir: her çekirdek kendi örgüsünü dokur, kendi kapısını kurar.

> **Kapı veto değil süzgeçtir** ve bu ayrım ölçümle zorunludur. "Yasaklı" geçişler yasak değil, yavaştır: 2s→1s iki-Zerre bozunumu Lyman-α'nın $\sim10^{-8}$'i, [O III] 500,7 nm $\sim10^{-10}$'u, 21 cm aşırı ince geçiş $\sim10^{-24}$'ü. Yirmi dört mertebe bastırma — ama sıfır değil. Bastırma çarpanlarının türetilmesi §9.11.11'in açık kalemidir.

### Örgünün kapsamı — kesin sınır

Burada teorinin kendi sınırı **teoremle** çizilir ve bu sınır saklanmayacaktır.

> **Teorem.** Örgünün ilmek adımı açısal alınırsa — yani $s=r\,\Delta\varphi$ — çevre paylaşımı
> $$2\pi r = N\,r\,\Delta\varphi \;\Longrightarrow\; 1=\frac{N\,\Delta\varphi}{2\pi}$$
> verir ve **$r$ özdeş olarak düşer**: her yarıçap çözümdür, merdiven belirsizleşir.
>
> **Sonuç:** dönüşlerden dokunan bir yapının doğal ürünü bir **açıdır**; kendi başına hiçbir uzunluk üretmez. Uzunluk ölçeği örgüden **çıkarılamaz**, dışarıdan gelmek zorundadır.

Dolayısıyla örgü **açısal-topolojik** bir yapıdır, metrik bir yapı değil:

| Örgü şunu verir | Örgü şunu **vermez** |
|---|---|
| Kabuğun **neresinde** — hangi yönelimler duruyor | Kabuk **ne kadar büyük** — uzunluk ölçeği |
| **Kaç mod** var — alt-durum sayımı ve katlılıkları | Hangi **frekansta** — mutlak ritim |
| **Hangi geçişler** — kapının seçtiği desen değişimleri | Geçişin **hızı** — çizgi şiddetleri |

Bu bir eksiklik itirafı değil, **kapsam beyanıdır** ve yukarıdaki teoremin zorunlu sonucudur: açısal kapanma kesikliliği üretir, uzunluğu üretmez. Uzunluk ölçeği teorinin ilan edilmiş girdisidir (§9.11.10) ve merdivenin *oranları* §9.11.4'ün çevre paylaşımından gelir. **Örgünün kazandırdığı şey, aynı yarıçapta birden çok durumun bulunabilmesidir** — ve bu, aşağıdaki alt-durum sayımının kapısını açar.

### Alt-durumlar: aynı yarıçap, farklı mod

Örgü aynı izde birden çok kapalı desen taşıyabilir. Bunlar **aynı yarıçapta** oldukları için **aynı enerjidedirler** — yarıçap enerjiyi belirler (§9.11.5), örgü modu belirlemez.

Bu, hidrojende ölçülen **$l$-yozlaşmasının** mekanik karşılığıdır: kaba yapıda 2s ve 2p aynı enerjidedir; enerji yalnız $n$'ye bağlıdır. Teoride bunun nedeni açıktır — iki durum aynı izin iki örgü modudur ve iz tektir. Standart çatı bunu Coulomb potansiyelinin özel simetrisine bağlar; burada aynı sonuç örgünün yapısından çıkar. **Ve molekülde yozlaşmanın bozulması da beklenir**, çünkü orada iki merkez örgüyü bozar.

**Sayım problemi açıkça kurulabilir** ve teorinin bu ailedeki sıradaki nicel işidir:

- **Girdi:** kaynak dizilimi ($k$'ıncı katmanda $(2k)^2$ konumun yarısı proton) · dönüş fazı · doğrusal salınım fazı
- **Koşul:** iz deseni kapanır
- **Çıktı:** duran açısal desenlerin ayrık kümesi ve **katlılıkları**

Hedef sayı bellidir. Kapasite $2k^2=2\cdot k^2$'dir ve $k^2$ bir kare ızgaranın gnomon ayrışımını taşır:

$$k^2 = 1+3+5+\dots+(2k-1)$$

| $k$ | Gnomonlar | Katlılıklar | Gözlenen alt kabuklar | Toplam |
|---|---|---|---|---|
| 1 | $\{1\}$ | 1 | s | $2\cdot1=2$ |
| 2 | $\{1,3\}$ | 1, 3 | s, p | $2\cdot4=8$ |
| 3 | $\{1,3,5\}$ | 1, 3, 5 | s, p, d | $2\cdot9=18$ |
| 4 | $\{1,3,5,7\}$ | 1, 3, 5, 7 | s, p, d, f | $2\cdot16=32$ |

> ⚠️ **Bu tablo bir kanıt değildir ve öyle sunulmayacaktır.** $k^2=\sum_{l}(2l+1)$ bir **aritmetik özdeşliktir**; iki taraf aynı sayıyı yazmak zorundadır ve uyuşma otomatiktir. Parametre disiplini (Anayasa Madde 21) desen uyumunu kanıt saymayı yasaklar.
>
> **Kanıt olacak olan şudur:** kapanma koşulu bağımsız olarak çözüldüğünde mod ailelerinin *gerçekten* gnomon biçiminde çıkması ve sıralamalarının (neden s önce, sonra p) türetilmesi. Tablo bir hedeftir, sonuç değil — ve hedefin yazılı olması hesabın yapılmış olduğu anlamına gelmez.

### İki borç, adlandırılarak bırakılıyor

**Birincisi — "2" çarpanı.** Standart çatı $2n^2$'nin içindeki 2'yi **spinden** alır; bu resim onu **ızgaranın yarılanmasından** alır, yani geometriden (§9.11.2). İki hesap aynı sayıyı verir, ama **Stern–Gerlach spini doğrudan ölçer**: gümüş demeti ikiye ayrılır. Manyetizma bu kitapta *Atomların İşleyişi*'ne havale edilmiştir (1.1.3), ama havale borcu görünmez kılmaz — **gümüş demetinin ikiye ayrılmasının geometrik karşılığı teorinin borcudur** ve §9.11.11'e yazılıdır.

**İkincisi — örgünün frekans üretmemesi.** Yukarıdaki kapsam tablosu gereği örgü mutlak ritmi vermez; rijit bir desen tek bir açısal hızla döner ve iki eş ritmin vurusu sıfırdır. Çizgi frekansının kaynağı bu yüzden örgü değil, §9.11.6'nın konusudur — ve orada kaydedilen açık kalem geçerlidir.

---

## 9.11.4 Yarıçap merdiveni: çevre paylaşımı

Bir önceki alt bölüm çemberin **üzerindeki** dizilimi verdi; şimdi çemberin **yarıçapı** gerekiyor. Ve burada, teoriyi standart çatıdan ayıran asıl adım vardır.

**Önce neyin işe yaramadığı.** Yarıçap bir **kuvvet dengesinden** çıkarılmaya kalkışılırsa hiçbir şey çıkmaz: merkez çekimi $Zk_e/r^2$, elektronların karşılıklı itmesi $k_e S(N)/r^2$ — ikisi de aynı üsle gider, $r$ sadeleşir. Salt yük mekaniğinde denge yarıçapı **yoktur**; ne mutlak değer ne oran. Bu, Earnshaw teoreminin bilinen içeriğidir ve nokta yüklerden kurulu her modeli bağlar.

**Ve teorinin mekanizması bir kuvvet dengesi değildir.** Evrenakı'da elektron nokta değil — süpürdüğü **diski olan** fiziksel bir girdaptır (2.1). İki girdap üst üste binemez; her biri halka üzerinde bir **yay** işgal eder. Yörüngeyi kuran kısıt bu yüzden kuvvet dengesi değil, **çevrenin bölüşülmesidir**:

$$\boxed{\;2\pi r_k \;=\; N_k\,s\;}$$

Burada $s$ tek bir uzunluktur: bir elektron girdabının halka boyunca **işgal ettiği yay** — teorinin bu ailedeki tek ölçek girdisi (§9.11.10). $N_k = 2k^2$ konduğunda:

$$r_k = \frac{2k^2 s}{2\pi} = \frac{k^2 s}{\pi} \;\Longrightarrow\; \boxed{r_1:r_2:r_3:r_4 = 1:4:9:16}$$

Standart kimyanın $r_n = n^2 a_0$ merdiveniyle **birebir aynı oran** — ve açısal momentum kuantumlamasına hiç başvurulmadan. Üç şey kaydedilmelidir:

**(1) Earnshaw itirazı çürütme değil, dayanaktır.** Yarıçapın yük dengesinden gelemeyeceği kanıtı, teorinin onu **başka** bir yerden alması gerektiğinin kanıtıdır. Kısıt geometrikse teorem bağlamaz: çevre paylaşımı bir denge koşulu değil, **yer kaplama** koşuludur.

**(2) Oran kesindir, çünkü çevre kesin bölünür.** "Eşit yay mı, eşit kiriş mi?" tartışması burada konusuzdur. Elektron halka **boyunca** hareket eder; sıradakini engelleyen şey onun hareket doğrultusundaki uzanımıdır, yani bir **yay**. Çevre tam olarak $N$ yaya bölünür ve $r \propto N$ **yaklaşık değil, tamdır**.

**(3) Elektron neden tam paylaşım sınırında durur?** Basınç kuyusu onu içe çeker (Kısım 3); geometri daha içe girmesine izin vermez. Elektron, **geometrinin izin verdiği en derin yarıçapta** oturur. Bu, sınırın neden doyurulduğunu söyler.

Ölçek: $r_1 = a_0$ ve $N_1 = 2$ konduğunda

$$s = \pi a_0 = 1{,}6625\times10^{-10}\ \text{m}$$

— atomlarda ölçülen tipik elektron-elektron uzaklığının mertebesi.

$s$ bir **uzunluktur**, bir açı değil; hangi kabukta olduğuna bakmaz. Bunun görünür sonucu şudur: $k=1$'de iki elektron halkanın yarısını birer yayla doldurur (180°, tam karşılıklı), $k=2$'de sekiz elektronun her biri 45° kaplar, $k=3$'te on sekiz elektron 20°. Açısal uzanım daralır çünkü halka büyür; **yay sabit kalır.** Alçak kabuklarda elektronun yörüngenin geniş bir bölümüne yayılmış olması teorinin elektron tanımının doğrudan gereğidir — elektron 2.1'de nokta değil, "geniş çaplı disk rüzgârı"dır.

> **Hidrojen boşta kalmaz.** Çevre paylaşımı bir katmanın **kapasitesini** kullanır, fiilî doluluğunu değil: $r_k$ katmanın özelliğidir, içinde kaç elektron bulunduğunun değil. İzler, üzerlerinde elektron olmasa da vardır — **elektronlar ortamın örgüsünün izlerini takip eder**, izleri kendileri kurmaz. Hidrojenin tek elektronu bu yüzden merdivenin herhangi bir basamağına oturabilir; uyarılmış hâller kapasite merdivenidir, doluluk merdiveni değil.
>
> Bu ayrım teorinin bir **posit**idir ve açık yazılmalıdır: örgünün izlerinin izinli yarıçaplar olduğu varsayılır. Karşılığında açısal momentum kuantumlaması varsayımı düşer — bir posit, bir posit yerine.

---

## 9.11.5 Enerji merdiveni: $1/r$ topografyası $1/n^2$ verir

Teorinin kütle-itim topografyası $1/r$ biçimindedir (Ek B.3):

$$P(r) = P_0 - \frac{\alpha M}{r}$$

**Merdivenin biçimini kuyunun şekli belirler** ve karşılaştırma bunu görünür kılar: kuyu $1/r$ ise $r\propto k^2$ merdiveni üzerinde $E\propto-1/k^2$ çıkar; kuyu parabolik ($V\propto r^2$) olsaydı aynı merdiven **eşit aralıklı** bir tayf verirdi. Atom tayfı eşit aralıklı değildir; $1/n^2$'dir. **Merdivenin deseni, onu üreten düzenin biçim imzasıdır** ve teorinin düzeni doğru biçimi taşır.

Enerji, ölçülen yük katsayısı $k_e=e^2/4\pi\varepsilon_0$ ile birlikte kapanır:

$$E_n = -\frac{k_e}{2r_n} = -\frac{k_e}{2n^2a_0}$$

$n=1$ için $-13{,}606$ eV — hidrojenin iyonlaşma enerjisi.

> **Bu sayı bir sınav değildir, kalibrasyondur.** $a_0$ ölçülen girdi olarak alındığında $k_e/2a_0$ özdeş olarak $hcR_\infty$'a eşittir; $a_0$'ı sabitleyen gözlem de Rydberg sabitidir (Ek C, satır 1-b). Yani $-13{,}606$ eV'nin çıkması, girdinin geri okunmasıdır. Bu ailede **sınanabilir olan mutlak ölçek değil, biçim ve oranlardır** — ve §9.11.9'un tablosu tam olarak onları sınar.

---

## 9.11.6 Çizgi frekansı bir **vurudur** — ve ritim duvar hızından gelir

Teori frekansı kaynağın ateşleme ritmi olarak tanımlar (2.3.1). Bu tanımın altında rahatsız edici bir soru vardır: **mekanik bir ritim neden iki terimin farkı olsun?** Standart çatıda cevap kolaydır ("enerji farkı"), ama teoride ritim fiziksel bir dönüştür ve farkın karşılığı kurulmalıdır.

Cevap geçişin kendisindedir: elektron zarfı $r_2$'den $r_1$'e indiğinde ortada **iki ritim** vardır ve yayılan katarın ritmi bu ikisinin **vurusudur.** Bunun nicel içeriği için ritmin ne olduğunu söylemek gerekir — ve teorinin buna kendi yasası vardır.

**Ritim, yörünge dolanma frekansı değildir; zarfın duvar frekansıdır.** Postülat 5'in duvar hızı yasası (M-3) her kavitasyon zarfının duvarını **boyuttan bağımsız** olarak $\sqrt2\,c$ hızında döndürür. Dolayısıyla:

$$\Omega_k = \frac{\sqrt2\,c}{r_k} \;\propto\; \frac{1}{r_k} \;\propto\; \frac{1}{k^2}$$

Vuru alındığında Rydberg biçimi **doğrudan** çıkar:

$$\nu_{12} \;\propto\; \Omega_1-\Omega_2 \;\propto\; \left(\frac{1}{k_1^2}-\frac{1}{k_2^2}\right)$$

> **Buradaki ayrım kritiktir ve teoriyi sınanabilir kılar.** Eğer ritim Kepler dolanma frekansı olsaydı ($v=\sqrt{k_e/m r}$, $\Omega\propto r^{-3/2}\propto n^{-3}$), vuru $\left(1/n_1^3-1/n_2^3\right)$ verirdi — **yanlış seri.** Teorinin duvar hızı yasası boyuttan bağımsız olduğu için $\Omega\propto1/r$ verir ve doğru seriye götürür. Yani $1/n^2$ yapısı, teorinin kendi $\sqrt2\,c$ yasasının **imzasıdır**; ödünç alınmış bir kinematikle bu yapı elde edilemez.

Vuru yapısının ikinci sonucu **Rydberg–Ritz birleşme ilkesidir** (Ritz, 1908):

$$(\Omega_1-\Omega_2) + (\Omega_2-\Omega_3) = \Omega_1-\Omega_3 \qquad\Longleftrightarrow\qquad \nu_{13}=\nu_{12}+\nu_{23}$$

Toplanabilirlik **ek varsayım olmadan** sağlanır. Standart çatıda bu enerji korunumunun sonucudur; burada geçiş mekanizmasının geometrik zorunluluğudur.

### Ölçek çarpanı: ikinci girdi — ve $h$'ın ikinci ayrıştırması

Biçim ve oranlar kesindir; **mutlak frekans için bir boyutsuz çarpan gerekir.** Duvar frekansının kendisi çok yüksektir:

$$f_1 = \frac{\sqrt2\,c}{2\pi a_0} = 1{,}2751\times10^{18}\ \text{Hz}, \qquad \frac{f_1}{cR_\infty} = 387{,}60$$

Yayılan katarın ritmi duvarın her turunda değil, kopma penceresinin izin verdiği kesirde doğar (9.2); bu kesir **görev çevrimi** $\eta_d$'dir:

$$\nu_{12} = \eta_d\,\frac{\sqrt2\,c}{2\pi}\left(\frac{1}{r_1}-\frac{1}{r_2}\right), \qquad \eta_d = \frac{1}{387{,}60} = 2{,}580\times10^{-3}$$

> **$\eta_d$ türetilmemiştir ve türetilmiş gibi yazılmayacaktır.** Değeri, $a_0$'ı sabitleyen gözlemin *aynısıyla* (Rydberg sabiti) sabitlenir; dolayısıyla yeni bir gözlem maliyeti getirmez ama **öngörü de değildir.** Teorinin bu ailedeki **ikinci boyutsuz girdisidir** ve envantere öyle yazılmıştır (§9.11.10).
>
> ⚠️ **Bir sayı benzerliği burada kullanılmayacaktır.** $a_0R_\infty=\alpha/4\pi$ standart sabitlerin bilinen bir özdeşliği olduğu için $\eta_d$ sayısal olarak $\alpha/2\sqrt2$'ye eşit çıkar. Bu bir kazanç değildir — $a_0$ ile $R_\infty$ arasındaki özdeşliğin yeniden yazımıdır ve teori $\alpha$'yı üretmiş olmaz. $\alpha$ bu zincire ancak 9.6'nın kendi mekanik türetiminden girebilir; uyum sağlamak için elle konulması Anayasa Madde 21'in yasakladığı **yama parametredir.**

**Buna karşılık yapısal bir kazanç vardır ve kaydedilmelidir.** Teori bu ailede enerjiyi ve frekansı **iki ayrı yoldan** verir: enerjiyi $1/r$ topografyasından ($\Delta E=\tfrac12k_e(1/r_1-1/r_2)$), frekansı duvar hızı yasasından. İkisinin oranı Planck sabitini **ödünç almadan** kurar:

$$h \;=\; \frac{\Delta E}{\nu} \;=\; \frac{\pi k_e}{\eta_d\sqrt2\,c} \;=\; 6{,}626\times10^{-34}\ \text{J·s}$$

Statüsü 9.2'nin $h=\delta\tau$ kaydıyla **aynıdır ve aynı dürüstlükle yazılmalıdır:** $\eta_d$ tayfın kendisiyle sabitlendiği için bu bir **sayısal öngörü değil, mekanik bir ayrıştırmadır.** Söylediği şey şudur — $h$ temel bir sabit değildir; bir yük katsayısı, bir ışık hızı ve bir görev çevrimine ayrılır. $\eta_d$ bağımsız olarak türetilirse ayrıştırma öngörüye döner; kalem §9.11.11 md. ①'dedir.

---

## 9.11.7 Harmonik: yasak değil, koşullu bir öngörü

Mekanik bir dizge **zamanda** tekrar ediyorsa (periyot $T$), Fourier gereği yalnız $1/T$'nin tam katlarında ışıyabilir ve aralıklar sabit olur. Bu, klasik atom modellerini 1913'te öldüren itirazdır.

Alçak seviyelerde gözlem harmonik değildir. Balmer'de ardışık frekans farkları ($\times10^{14}$ Hz): **1,599 · 0,740 · 0,402 · 0,242 · 0,157** — ilk dört aralıkta **6,6 kat**, beş aralıkta **10,2 kat** oynar ve $8{,}225\times10^{14}$ Hz'lik seri limitine sıkışır.

**Teorinin cevabı yapısaldır:** harmonik teoremi *zamansaldır*; ışıma burada tek bir dönüşün frekansı değil, **iki duvar frekansının vurusudur** (§9.11.6). Vuru zamanda tekrar eden tek bir periyoda bağlı olmadığı için teorem bağlamaz.

### Ve teori nerede harmonik **beklendiğini** de söyler

Vuru $\left(1/k_1^2-1/k_2^2\right)$ ile gittiğine göre, harmonik yapı terim farklarının **doğrusallaştığı** her yerde çıkmak zorundadır. Bu iki koşulla olur:

**(a) Rijit dönme — iki merkez.** Bileşikte gerçekten dönen bir gövde vardır; tayf harmoniktir.

**(b) Yüksek $n$ — komşu basamaklar.** $k_2 = k_1 - j$ için:

$$\frac{1}{(n-j)^2}-\frac{1}{n^2} \;=\; \frac{j(2n-j)}{n^2(n-j)^2} \;\approx\; \frac{2j}{n^3}$$

$j$'de **doğrusal** — yani yüksek $n$'de teori **harmonik bir tayf öngörür.** Bu bir kaçış değil, sınanmış bir öngörüdür:

| Geçiş | Vuru kuralı | H110α'ya oran |
|---|---|---|
| H110α (111→110) | 4,874 GHz | 1 |
| H110β (112→110) | 9,618 GHz | **1,973** |
| H110γ (113→110) | 14,237 GHz | **2,921** |

$1 : 1{,}97 : 2{,}92$ — %3 içinde harmonik. Radyo astronomisinin ölçtüğü Rydberg çizgileri (H110α, 4,874 GHz) **gerçekten** harmoniğe yakındır ve teori bunu $2j/n^3$'ten üretir.

**İkinci öngörü daha da keskindir.** $j=1$ için vuru $\approx 2/n^3$'e gider; yani komşu basamaklar arası ışıma, yüksek $n$'de **klasik dolanma frekansına yakınsar** — Bohr'un uyum ilkesinin içeriği. Sayısal sınav:

$$\nu(51\!\to\!50)_{\text{vuru}} = 51{,}072\ \text{GHz} \qquad\text{vs}\qquad f_{\text{dolanma}}(n\!=\!50{,}5) = 51{,}062\ \text{GHz}$$

$2\times10^{-4}$ uyum. **Bu uyum teorinin sonucudur, çelişkisi değil:** $n^{-2}$ giden niceliklerin komşu vurusu zorunlu olarak $n^{-3}$ ile gider. Yüksek-$n$'de dolanma frekansıyla çakışma, ışımanın bir dolanma frekansı **olduğunu** göstermez — vurunun o limitte öyle davrandığını gösterir. §9.11.6'nın ayrımı bu yüzden alçak $n$'de sınanır: orada Kepler kinematiği yanlış seri, duvar hızı yasası doğru seri verir.

### Alçak $n$'de neden harmonik yok — ayrım tablosu

| Yapı | Terim farkı doğrusal mı | Tayf | Ölçüm |
|---|---|---|---|
| **Tek atom, alçak $n$** | hayır ($1/k^2$ hızla açılır) | terim farkı | Balmer: **6,6 kat** (4 aralık) |
| **Tek atom, yüksek $n$** | **evet** ($\approx2j/n^3$) | **harmonik** | H110: **%3** (3 aralık) |
| **Molekül** (iki merkez) | evet (rijit dönme) | **harmonik** | CO: **%0,02** (4 aralık) |
| Manyetik alanda yüklü gövde | evet (siklotron/Larmor) | **harmonik** | 28,0 GHz/T · 13,996 GHz/T |
| Deforme çekirdek | $J(J+1)$ | bant | MeV |

**Hüküm dar değil geneldir:** harmonik, iki merkezin bulunmasına değil, **terim farklarının doğrusallaşmasına** bağlıdır — rijit dönmede *ve* yüksek $n$'de. Teori ikisini de öngörür; ikisi de gözlenir. Bu, harmoniği toptan yasaklayan bir çatıdan da, onu yalnız rijit dönmeye bağlayan bir çatıdan da daha güçlüdür: dört ayrı rejimin hangisinde ne beklendiğini önceden söyler.

> **Bağımsız bir teyit.** Hidrojende kaba yapıda 2s ve 2p **aynı enerjidedir**; enerji yalnız $n$'ye bağlıdır, $l$'ye değil. Atomda rijit bir dönme enerjisi olsaydı $E_{dönme}\propto l(l+1)$ gereği bu durumlar belirgin biçimde ayrışırdı. Ayrışmıyor: **alçak $n$'de atomun içinde rijit dönen bir gövde olmadığı ölçülmüştür** — ve bu, $1/r$ düzeninin simetri imzasıdır. Molekülde aynı yozlaşma yoktur, çünkü orada gerçekten dönen bir gövde vardır.

---

## 9.11.8 Soğurma ile yayma birbirinin tersi değildir

Çizgi **konumları** her iki yönde aynıdır, ama süreçler simetrik değildir. Soğurma, $N$ vuruşun kopma penceresi $\tau$ içinde **birikmesidir** ve gelen akı gerektirir; yayma ise zarfın **tek seferde boşalmasıdır** ve akı gerektirmez (9.2). Teori bu nedenle **karşılıklı (reciprocal) bir çatı değildir.**

Konumların yine de örtüşmesi karşılıklılıktan gelmez: soğurma alıcıyı $r_i\to r_j$, yayma $r_j\to r_i$ taşır; **ikisi de aynı izinli kabuk kümesi** arasındaki geçiştir. Kısaca **konumlar ortak merdivenden, hızlar yönden.** Kirchhoff–Bunsen'in çizgi konumlarındaki örtüşmesi için ortak seviye yapısı yeterlidir; zamanda tersinirlik gerekmez — ve gerekmemesi iyidir, çünkü tersinir bir çatı kendiliğinden yaymayı, Stokes kaymasını ve lazer kazancını **imkânsız** kılardı.

Bir aşırı iddiadan da kaçınılmalıdır: soğurma çizgilerinin listesi yayma listesinden **daha dardır**, çünkü soğurma alt seviyenin dolu olmasını gerektirir ve 300 K'de Hα'nın alt seviyesinin doluluk oranı $n_2/n_1 \approx 10^{-171}$'dir. Çizginin **işaretini** (soğurma mı yayma mı görüldüğü) sıcaklık gradyanı $dT/d\tau$ belirler. Ayrıntı ve gözlemsel sonuçları 9.2'dedir.

---

## 9.11.9 Hidrojen: sayısal sınav

Sınav iki katmanda yapılmalıdır, çünkü iki katmanın kanıt değeri farklıdır.

### (i) Girdisiz katman: oranlar

Aşağıdaki tablo **hiçbir girdi kullanmaz** — ne $s$, ne $a_0$, ne $k_e$, ne $h$. Yalnız §9.11.4'ün $r_k\propto k^2$ merdiveni ve §9.11.6'nın vuru kuralı vardır; $\eta_d$ de oranlarda sadeleşir. Teori sütunu **kesin kesirdir.**

| Çizgi | Geçiş | Teori: $\nu/\nu_{\text{Ly-}\alpha}$ | Ölçülen orandan | Sapma |
|---|---|---|---|---|
| Lyman-α | 2→1 | $1$ (dayanak) | — | — |
| Balmer-α | 3→2 | $5/27 = 0{,}1851852$ | 0,1851857 | $+2{,}7\times10^{-6}$ |
| Balmer-β | 4→2 | $1/4 = 0{,}2500000$ | 0,2500000 | $<10^{-7}$ |
| Balmer-γ | 5→2 | $7/25 = 0{,}2800000$ | 0,2799999 | $-3{,}3\times10^{-7}$ |
| Paschen-α | 4→3 | $7/108 = 0{,}0648148$ | 0,0648146 | $-2{,}6\times10^{-6}$ |

*(Ölçülen oran $=\lambda_{\text{Ly-}\alpha}/\lambda_X$, serbest Evrenakı'ndaki Zerre aralıklarından: 121,567 · 656,460 · 486,268 · 434,168 · 1875,61 nm.)*

> **Terim kaydı — burada "vakum" yazılmaz.** Standart fizik bu değerleri *vakum dalga boyu* diye anar; teori bu adlandırmayı kendi cümlesinde kullanamaz, çünkü **serbest uzayda boşluk yoktur** — orada dolu Evrenakı vardır (Madde 1). Ölçüm pratiğinde yapılan işlem gerçektir ve teoride karşılığı vardır: *havanın deplasmanı çıkarılmış* değer, yani **serbest Evrenakı'ndaki Zerre aralığı.** ("Vakum" sözcüğü teoride yalnız **yırtılmış cebin adı** olarak geçer — girdap zarfının içindeki kavitasyon boşluğu — ve orada bile hiçliği değil, aşırı düşük basıncı adlandırır: Madde 2 gereği uzayın hiçbir noktası boş değildir.)
>
> Ve bu yalnız sözcük değil, içerik farkıdır: standart çatı vakum dalga boyunu **evrensel** bir referans sayar; teoride $c$ yerel $\sqrt{P/\rho}$ ile değiştiği için (Postülat 4) serbest-Evrenakı değeri de **yereldir.** Yukarıdaki oranlar bundan etkilenmez — ortak çarpan sadeleşir — ama mutlak değerler için referansın nerede ölçüldüğü ilkece anlamlıdır. Bugünkü duyarlıkta bu bir sınav değil; kaydı, ödünç alınan sayının statüsünün görünmesi içindir.

**Dört bağımsız oran, $10^{-5}$ içinde.** Sapmaların bu düzeyde kalması alıntılanan çizgi merkezlerinin basamak sayısıyla sınırlıdır, teoriyle değil. İndirgenmiş kütle düzeltmesi oranlarda **sadeleşir**, dolayısıyla bu katman ondan da bağımsızdır.

### (ii) Girdili katman: mutlak konumlar

Mutlak Zerre aralığı için $E_n=-k_e/2n^2a_0$ ve $\lambda=hc/\Delta E$ gerekir. **İkinci adım ölçülen $h$'ı kullanır** ve bu açıkça kaydedilmelidir: aşağıdaki sütun teorinin oran öngörüsü değil, o öngörünün ölçülen $h$ ve $c$ ile uzunluk birimine çevrilmiş hâlidir.

| Çizgi | Teori $\lambda$ (sonsuz çekirdek) | $R_H$ ile (geri tepme katılmış) | Ölçülen (serbest Evrenakı) |
|---|---|---|---|
| Lyman-α | 121,502 nm | 121,568 nm | 121,567 nm |
| Balmer-α | 656,112 nm | 656,469 nm | 656,460 nm |
| Balmer-β | 486,009 nm | 486,274 nm | 486,268 nm |
| Balmer-γ | 433,937 nm | 434,173 nm | 434,168 nm |
| Paschen-α | 1874,607 nm | 1875,628 nm | 1875,61 nm |

İkinci ve üçüncü sütun arasındaki fark $\sim10^{-5}$'tir ve ince yapı düzeyindedir. Birinci ile ikinci arasındaki $5{,}446\times10^{-4}$ ise **çekirdek geri tepmesidir** ($m_e/m_p$, indirgenmiş kütle) — teoriye özgü bir açık değil, standart çatıda da yapılan aynı düzeltmedir.

> **Bu katmanın kanıt değeri sınırlıdır ve bunu yazmak zorunludur.** $a_0$ girdi, $k_e$ ölçülü olduğuna göre $E_1$ kalibrasyondur (§9.11.5); tabloyu ilginç kılan tek şey, aynı kalibrasyonun beş çizgide de tutarlı kalması ve tek bir bilinen düzeltmeyle kapanmasıdır. **Teorinin gerçek sınavı (i) katmanıdır.**

### İzotoplar

Balmer-α (serbest Evrenakı): ¹H 656,460 nm · ²H 656,280 nm · ³H 656,223 nm. Fark tamamen çekirdek kütlesinden gelir ($\lambda\propto1+m_e/M$); Urey döteryumu 1932'de tam bu kaymayı görerek keşfetmiştir. Kayma **bütün çizgilerde aynı bağıl orandadır** — desen bozulmaz, yalnız ölçeklenir. Bu, kabuk deseninin proton sayısıyla (dolayısıyla çekirdek geometrisiyle) kurulduğu, nötronun ise yalnız atalet eklediği okumasının beklentisidir: **desen $Z$'den, ölçek düzeltmesi $A$'dan.** Periyodik tablonun kütle numarasıyla değil proton sayısıyla sıralanmasının mekanik nedeni de budur.

---

## 9.11.10 Ne türetilmiştir, ne girdi alınmıştır

**Türetilen:** kabuk doluluk sayıları ($2k^2$) · dışlamanın mekanizması (tek yörünge + yük itmesi) · yarıçap **oranları** ($1:4:9:16$, çevre paylaşımından) · enerji merdiveninin $1/n^2$ **biçimi** ($1/r$ topografyasından) · Rydberg'in $\left(1/n_1^2-1/n_2^2\right)$ **biçimi** (duvar hızı yasası + vuru) · Rydberg–Ritz toplanabilirliği · alçak $n$'de harmoniğin yokluğu **ve** yüksek $n$'de harmonikleşme (uyum ilkesi) · izotop kaymasının deseni bozmadan ölçeklemesi.

**Girdi alınan — iki kalem, açıkça:**

| Girdi | Değer | Statü |
|---|---|---|
| $s$ — elektron girdabının yay uzunluğu | $1{,}6625\times10^{-10}$ m ($=\pi a_0$) | Ek C satır 1-b, rozet **S**; sabitleyen gözlem: Rydberg sabiti |
| $\eta_d$ — görev çevrimi (boyutsuz) | $2{,}580\times10^{-3}$ | aynı gözlemle sabitlenir; türetilmemiş (§9.11.6) |

*(Bunların yanında $k_e=e^2/4\pi\varepsilon_0$ kullanılır; o standart çatının da girdisidir, ortak kalemdir. **$h$ girdi değildir:** teorinin frekans yolu duvar hızı yasasından geçer ve $h$'ı ödünç almaz — §9.11.6. $h$ yalnız §9.11.9-ii'nin uzunluk sütununda, birim çevrimi olarak görünür.)*

$s$'nin türetilmesi beklenmez ve gerekçe teoriktir, kolaylık değil: §9.11.4'te gösterildiği gibi salt yük mekaniği ölçekten bağımsızdır, dolayısıyla mutlak değeri *hiçbir* yük-temelli denge veremez. Aynı sonuca teorinin kendi tarafından da varılır: Evrenakı'nın nicelik kümesinden eylem boyutunda bağımsız bir büyüklük kurulamaz, dolayısıyla $\hbar$ bu çatıdan üretilemez. İki bağımsız yol aynı sınıra çıkar; bu, boşluğun gerçek olduğunun teyididir.

> **Parite hesabı dürüst tutulmalıdır.** Teorinin bu ailedeki kümesi $\{s,\,\eta_d,\,k_e\}$, standart çatının kümesi $\{m_e,\,\hbar,\,k_e\}$'dir — **üçe üç.** Bir uzunluk + bir boyutsuz sayı, bir kütle + bir eylem karşılığındadır. Sayı eşitliği bir zafer değildir, ama bir kayıp da değildir.
>
> **Kazanç açıklama tarafındadır ve sayılabilir:** aynı üç girdiyle kabuk doluluk sayıları, dışlamanın mekanizması, yarıçap oranları, harmoniğin nerede beklenip nerede beklenmediği ve — $\eta_d$ üzerinden — $h$'ın kendisi *ayrıca* çıkar. Standart çatı bunların her biri için ayrı bir ilke koyar (spin eşleşmesi, Pauli, açısal momentum kuantumlaması) ve $h$'ı temel alır. **Aynı bütçe, daha çok çıktı.**
>
> Ve $s$'nin ilanı bir eksiklik itirafı değil, **parametre disiplininin gereğidir** (Anayasa Madde 21): kaynağı gösterilemeyen bir büyüklük uydurulmaz, ilan edilir.

---

## 9.11.11 Açık Kalemler ve Havaleler

> ### Randevu beyanı — iki kalem kapatılmak üzere ertelenmiştir
> Aşağıdaki **①** ve **②** kalemleri bu kitabın borcudur ve **havale edilmemiştir**; silinmiş, küçültülmüş ya da bir sonraki kitabın konusu ilan edilmiş de değildir. Ama ikisinin de kapanma yolu bu kitapta bulunmayan bir makinede geçer: ① kopma penceresinin duvar turuna oranını, ② basınç kuyusunun derinlik dinamiğini gerektirir — ikisi de **işleyiş** katmanındadır (1.1.3, ikinci sınır beyanı).
>
> **Bu nedenle beyan edilir:** serinin *Atomların İşleyişi* kitabı yayımlandığında **her iki kalem de yeniden ele alınacaktır.** O kitabın ısıl ve elektromanyetik işleyiş makinesi kurulduğunda ① ve ② ya kapanacak ya da kapanamama gerekçeleri nicel olarak yazılacaktır. Bu kitaptaki statüleri o zamana kadar **açık borç** olarak kalır — ertelenen şey kalemlerin kendisi değil, onları kapatacak hesabın adresi.
>
> Havale ile randevunun ayrımı korunmalıdır: **havale edilen** konular bu kitabın borcu değildir (aşağıdaki iki küme); **randevu verilen** kalemler bu kitabın borcudur ve envanterde borç olarak durur (7.4, md. 6-g).

**① Görev çevrimi $\eta_d$ (7.4, md. 6-g).** Vuru mutlak frekansı $\eta_d = 2{,}580\times10^{-3}$ çarpanıyla verir ve bu sayı **türetilmemiş bir girdidir** (§9.11.6): kopma penceresinin duvar turuna oranı, pencere mekaniğinden (9.2) bağımsız olarak hesaplanmalıdır. Kalemin bedeli iki kattır — kapanırsa teori hem mutlak frekansı öngörür hem de $h=\pi k_e/\eta_d\sqrt2c$ ayrıştırması gerçek bir **sayısal öngörüye** döner. Aynı borç 9.2'nin $\tau$ kaleminde de durur ve ikisi aynı mekanizmaya bakar; birinin kapanması büyük olasılıkla ötekini de kapatır. **$\alpha$ ile sayısal benzerlik bu kaleme yazılmayacaktır** — gerekçe §9.11.6'nın uyarı kutusundadır.

**② $Z$ ölçeklemesi (7.4, md. 6-g).** Çevre paylaşımı yarıçapı **elektron sayısından** kurar, çekirdek yükünden değil. H-benzeri iyonlarda ölçülen $r = n^2a_0/Z$ ölçeklemesi (He⁺ Lyman-α 30,378 nm, hidrojenin dört katı enerji) bu yüzden paketlemeden **çıkmaz**; kuyunun derinliğinden gelmesi gerekir ve türetilmemiştir. §9.11.1'in ilan ettiği hedef bar hidrojendir, ama bu kalem o barın hemen yanındadır ve kapatılması beklenir.

**③ Katman yinelenmesi (7.4, md. 6-g).** Periyodik tablonun periyot uzunlukları yinelenir (2, 8, 8, 18, 18, 32, 32). Çevre paylaşımı yarıçapı kapasiteden kurduğu için aynı kapasiteli iki katman **aynı yarıçapı** verir; gerçek atomlarda vermez. Teorinin okuması, aynı kapasiteli katmanların **eksen boyunca farklı yükseklikte** yığılmış olmasıdır (§9.11.2) — ama bunun yarıçap farkına nasıl döndüğü hesaplanmamıştır. Bu, çok elektronlu atomlar alanındadır ve §9.11.1'in bar ilanının dışındadır.

**④ Örgünün mod sayımı (7.4, md. 6-g).** §9.11.3-b'nin kapanma koşulu **çözülmemiştir.** Örgü aynı izde birden çok kapalı desen taşıyarak $l$-yozlaşması için mekanik yer açar, ama duran desenlerin **kaç tane** olduğu ve **katlılıklarının** ne olduğu türetilmemiştir. Hedef sayı bellidir (gnomon dizisi $1,3,5,\dots,2k-1$; toplam $2k^2$) — ama §9.11.3-b'nin uyarı kutusu geçerlidir: hedefin yazılı olması hesabın yapılmış olduğu anlamına gelmez, ve aritmetik özdeşlik kanıt değildir. Bu kaleme bağlı üç ikincil borç: **alt kabuk sıralaması** (neden s, sonra p), **seçim kurallarının** ($\Delta l=\pm1$) kapı geometrisinden çıkarılması, ve **ince yapı · Lamb kayması · aşırı ince yapı** — hiçbiri açıklanmış sayılmaz. Bastırma çarpanlarının nicel hedefleri §9.11.3-b'de kayıtlıdır (2s→1s $10^{-8}$, [O III] $10^{-10}$, 21 cm $10^{-24}$).

**⑤ "2" çarpanının geometrik karşılığı (7.4, md. 6-g).** $2k^2$'nin içindeki 2 bu resimde kare ızgaranın yarılanmasından gelir, spinden değil (§9.11.2). Aynı sayıyı veren iki hesaptan hangisinin doğru olduğunu **ölçüm ayırt eder**: Stern–Gerlach gümüş demetini ikiye ayırır ve bu bir spin ölçümüdür. Manyetizma *Atomların İşleyişi*'ne havale edilmiştir (1.1.3), ama **havale bu borcu kapatmaz** — demetin ikiye ayrılmasının geometrik karşılığı gösterilmelidir.

**⑥ Çizgi şiddetleri (7.4, md. 6-c).** Çizgi **konumları** kuruludur, çizgi **şiddetleri** değildir. Kendiliğinden/uyarılmış salınım oranı ($A_{21}/B_{21}=8\pi h\nu^3/c^3$), $g$-faktörleri, $\nu^3$ ölçeklemesi ve Kennard–Stepanov/McCumber bağıntısı türetilmemiştir. Bunların yön bağımlı olması §9.11.8'in doğal sonucudur; kalemi kapatacak olan da o asimetrinin nicelleştirilmesidir. Aynı listede bir **fırsat** vardır: $A/B\propto1/c^3$ olduğundan değişken-$c$ postülatı ortam indisiyle ışıma ömrünün kısalmasını öngörmek zorundadır ve bu ölçülmüş bir sınavdır (9.1 ile doğal köprü).

**Bir sonraki kitaba havale edilenler (7.4, md. 6-d):** bileşik yapıların tayfı (molekül dönme ve titreşim bantları) ve **yönlü kimyasal bağın geometrisi** — suyun 104,5°'si, metanın dörtyüzlü 109,5°'si. Bu bölüm **tek atomun** düzenini konu alır; bileşikler iki ritmin birleşmesinden doğar ve birleşmiş yapının davranışı ayrı bir katmandır. Havale keyfî değildir ve sınanabilir bir sonucu vardır: §9.11.7'nin tablosu, rijit-dönme harmoniğinin yalnız bileşik yapılarda beklendiğini söyler.

**Havale edilen ikinci küme:** kabuk geçişlerinin **ısıl** istatistiği (denge dağılımı, kovuk mod sayımı) ve **elektrik yükü dinamiği** — dolayısıyla Zeeman yarılması ve Stern–Gerlach. Bu kitap yapı ve geometriyi kurar; ısıl ve elektromanyetik **işleyiş** serinin *Atomların İşleyişi* kitabına aittir — havalenin tam listesi ve gerekçesi 1.1.3'ün ikinci sınır beyanındadır.
