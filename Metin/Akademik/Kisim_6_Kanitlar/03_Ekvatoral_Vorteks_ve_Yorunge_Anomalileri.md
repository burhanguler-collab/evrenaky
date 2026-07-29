# 6.3 Ekvatoral Vorteks ve Yörünge Anomalileri: Kutuplara Karşı Ekvator

Evrenakı Teorisi'nin makro ölçekteki en büyük mekanik çıktılarından biri, gök cisimlerinin etraflarında oluşturdukları hidrodinamik girdaplardır (vorteksler). Standart fiziğin soyut "uzay-zaman geometrisi" veya izotropik (her yöne eşit) kütleçekimi modelleri, gezegenlerin etrafındaki yörüngesel davranışı salt kütle merkezli bir çekim olarak açıklar. Oysa Evrenakı akışkanlar dinamiği, uzayın bir "boşluk" değil, bizzat dönen kütle tarafından sürüklenen devasa bir "nehir" (akışkan) olduğunu gösterir.

Bu akışkan modelinin en belirgin kanıtı, Ekvatoral (yatay) yörüngeler ile Kutupsal (dikey) yörüngeler arasındaki devasa asimetridir.

## 6.3.1 Ekvatoral Yörünge ile Kutup Yörüngesi Arasındaki Hidrodinamik Fark

Ekvator bölgesinde Dünya saniyede yaklaşık 460 metre gibi devasa bir çizgisel hızla döner. Bu dönüş, Ekvator çevresindeki Evrenakı akışkanını da kendisiyle birlikte şiddetle sürükleyerek dışa doğru yayılan güçlü bir **Ekvatoral Girdap** yaratır. Kutuplarda ise dönüş hızı sıfıra yakındır; bu nedenle kutup üstlerinde akışkan sürüklenmesi (vorteks) çok zayıftır ve uzaydan gelen "Yanal İtim" (statik basınç) radyal olarak merkeze doğru çok daha baskındır.

* **Ekvatoral Yörüngeler:** Ekvator düzleminde dolanan bir uydu, dönen bir akışkan nehrinin (vorteksin) içindedir. Eğer uydu Dünya ile aynı yönde (doğuya doğru) dönüyorsa akıntıyı arkasına alır; ters yönde dönüyorsa akıntıya karşı kürek çeker ve ek bir hidrodinamik dirence maruz kalır. Bu direncin büyüklüğü ise küçüktür: Juno üst sınırı (6.3.2) gereği alçak yörüngede atmosferik sürüklemenin çok altında kalır ve ayırt edici imzası mutlak değil **diferansiyeldir** (prograd/retrograd sönüm farkı; Bkz. 3.6.1 ve 7.5 tablosu, satır 15).
* **Kutup Yörüngeleri:** Kutup noktalarında akışkan görece durgundur. Kutup yörüngesindeki bir uydu (polar orbit), turu boyunca kutupların durgun akışkanından çıkıp Ekvatorun fırtınalı nehrine dalmak zorundadır. Uydu her Ekvator geçişinde, Dünya'nın dönüşünden kaynaklı Evrenakı vorteksinin yanal akıntısıyla **dikine (çapraz) kesişir**. 

**Girdabın İzi Yörünge Verisinde Nerede? (Hassas Yörünge Belirleme ile Yüzleşme)**
Bu asimetri iddiasının en sert sınavı, uzay çağının en hassas veri setidir: binlerce uydunun santimetre düzeyindeki rutin yörünge belirlemesi (GNSS/SLR/DORIS izleme; GRACE/GOCE gravite haritaları), gözlenen tüm sapmaları bilinen terimlerle kapatır ve modellenmemiş bir "girdap artığı" bırakmaz; "donmuş yörünge" tasarımlı kutupsal uydular, dairesel-yakın yörüngelerini yıllarca korur. Teorinin cevabı bu veriyi reddetmek değil, **sahiplenmektir** — iki katmanda:

1. **Verinin en büyük düzeltme terimi olan $J_2$ düğüm gerilemesinin kendisi, teoride girdabın imzasıdır.** Dünya'nın ekvatoral şişkinliği dönüşün — teorideki okumayla girdap/deplasman dengesinin — eseridir; dolayısıyla standart fiziğin "kütle geometrisinin basıklık terimi" diye etiketlediği $J_2$ alanı, Evrenakı okumasında **ekvatoral girdabın şekillendirdiği kalıcı basınç deseninin ta kendisidir.** Kutup yörüngesinin düzlem devinimi, tam da bu desenin dikte ettiği harekettir: girdabın izi hassas yörünge verisinde "eksik" değil, verinin en büyük modellenen teriminin **içindedir.** Donmuş yörüngelerin işlemesi de bundandır — tasarım, bu kalıcı desenle çalışır.
2. **Kalıcı desenin ötesindeki ayrık girdap-kesme artığı ise teoride Lense-Thirring mertebesindedir ve ölçülmüştür:** GP-B ve LAGEOS'un mas/yıl düzeyindeki eksen kaymaları (6.3.3). Teori, hassas yörünge belirlemede bundan büyük, modellenmemiş bir artık **öngörmez**; Juno geçişinin sıfır sonucundan gelen kesme üst sınırı (6.3.2) da bu beklentiyle tutarlıdır (bir sıfır sonuç beklentiyi doğrulamaz; yalnızca ondan büyük etkileri dışlayarak sınırlar).

Böylece iki ontoloji — "kütle geometrisi + metrik burulması" ile "girdabın basınç deseni + akışkan kesmesi" — aynı ölçüm setini paylaşır; bu bir yeniden-yorum durumudur (Kanıtların Statüsü, 6.5) ve ayrıştırıcı yük, 7.4'te senetli nicel türetimler ile 7.5'teki ayrık öngörülere biner.

## 6.3.2 Flyby (Yakın Geçiş) Anomalisi: Kanıttan Sınır Koşuluna

1990'lı ve 2000'li yıllarda NASA uzay araçları (Galileo 1990, NEAR 1998, Rosetta 2005) yakıt tasarrufu için Dünya'ya yaklaşıp sapan yörüngeler (flyby) izlediklerinde, izleme verilerinde Newton ve Einstein modellerinin öngörmediği küçük hız sapmaları ($\Delta V$) rapor edildi. 2008'de J. D. Anderson ve ekibi bu verilerden çarpıcı bir ampirik formül çıkardı (Anderson ve ark., 2008):

$$\Delta V_\infty = \frac{2\omega_\oplus R_\oplus}{c} V_\infty (\cos \delta_i - \cos \delta_o)$$

Formülün anlamı şudur: rapor edilen sapma, aracın Ekvator düzlemine giriş ($\delta_i$) ve çıkış ($\delta_o$) açılarına bağlıdır. İzotropik bir kütleçekim modelinde ekvatordan ya da kutuptan gelmek sonucu değiştirmezdi; açı bağımlılığı ise tam da bir **Ekvatoral Girdap** kesme (shear) etkisinin taşıması gereken imza şablonudur.

**Dürüst kayıt — verinin bugünkü durumu:** Bu tablo sonraki hassas geçişlerde doğrulanmamıştır. Rosetta'nın 2009 ve 2011 geçişlerinde ve özellikle Juno'nun 2013 geçişinde — Anderson formülünün açıkça sıfırdan farklı bir sapma öngördüğü geometride — anomali **gözlenmemiştir** (Thompson ve ark., 2014). Pioneer 10/11'in eski "açıklanamayan ivmesi" ise (Anderson ve ark., 2002) sondaların kendi ısıl ışınımının asimetrik geri tepmesiyle nicel olarak çözülmüştür (Turyshev ve ark., 2012); Evrenakı ısıl geri tepmeyi dışlamadığından bu çözüm burada da kabul edilir ve Pioneer bu kitabın kanıt matrisinden çıkarılmıştır.

**Bu nedenle bu bölümün iddiası bilinçli olarak düşürülmüştür:** flyby verisi artık teorinin *kanıtı* değil, ekvatoral girdabın kesme kuvvetine bugüne kadarki en sıkı **üst sınırı** koyan ölçümdür. Juno'nun sıfır sonucu, girdap kesme katsayısının Anderson formülü ölçeğindeki değerlerden küçük kalması gerektiğini söyler; açı bağımlılığı ise girdap geometrisinin imza şablonu olarak arşivde durmaktadır. Kesme katsayısının bu üst sınırla tutarlı yeniden hesabı 7.4'ün hesap kalemidir. (Kitap genelindeki Karşı Kayıt ilkesi için bkz. Bölüm 1.1.2.)

## 6.3.3 Yeniden-Yorum: Gravity Probe B ve LAGEOS

Einstein, uzay-zaman geometrisinin dönen kütleler tarafından bükülüp sürüklendiğini (Frame-Dragging) iddia etmişti (Lense & Thirring, 1918). Bunu kanıtlamak için NASA, Gravity Probe B (GP-B) uydusunu özellikle **Kutupsal Yörüngeye** yerleştirdi (Everitt ve ark., 2011). 

Kutupsal yörüngedeki uydunun jiroskopları kuzey-güney ekseninde dönmekteyken, alttaki Ekvator akıntısı (Evrenakı vorteksi) doğu-batı ekseninde hızla dönüyordu. Bu çapraz kesişim sonucunda Ekvator akıntısı, kutup yörüngesindeki uydunun jiroskoplarını alttan yanal olarak sürükledi ve eksenlerini yılda **37,2 ± 7,2 mas (miliarksaniye; yay-saniyesinin binde biri)** kaydırdı (Genel Görelilik'in aynı etki için öngörüsü 39,2 mas/yıl'dır; ölçüm öngörüyü hata payı içinde doğrulamıştır).

Aynı ortam alanı, jiroskop spinini değil doğrudan **yörünge düzlemini** de sürükler: LAGEOS uydularının düğüm doğrusunda yılda ~31 mas'lık bir kayma kaydedilmiştir (Ciufolini & Pavlis, 2004). Bu ikinci gözlemlenebilir, aynı sürüklenme kesriyle ($\xi$) ve yeni parametre eklenmeden türetilir — mekanizma bu kez paralel taşıma değil, **Coriolis kuvvetidir** (Bölüm 3.6.3'ün atmosferik dolaşım için kurduğu $-2\vec\Omega\times\vec v$ yapısının yörünge ölçeğindeki karşılığı):

$$\left|\frac{d\Omega_{düğüm}}{dt}\right| = \frac{2GJ_\oplus}{c^2a^3(1-e^2)^{3/2}}$$

| Uydu | $a$ | **Evrenakı öngörüsü** | Gözlem |
|---|---|---|---|
| LAGEOS-1 | 12.270 km | **30,6 mas/yıl** | ~31 mas/yıl |
| LAGEOS-2 | 12.163 km | **31,4 mas/yıl** | aynı program |

*(Tam türetim: **Ek M-41**.)* Bu, türetilmiş $\xi$'nin bağımsız ikinci sınavıdır: tek bir sürüklenme kesri, iki farklı deneyi (jiroskop spini ve yörünge düzlemi) birden karşılar. İki sonucun geometrik çarpanları farklıdır (jiroskopta $\tfrac12$, düğümde $2$) ve bu fark mekanizma ayrımından gelir — paralel taşıma ↔ kuvvet.

> **Düzeltme kaydı — eğiklik:** Düğüm sürüklenme hızı, formülde görüldüğü üzere **eğiklikten bağımsızdır**. LAGEOS'un 109,8°'lik eğikliği etkinin *büyüklüğünü* belirlemez; iki farklı eğiklikteki uydunun birlikte kullanılması, bu etkiyi kendisinden $10^7$ kat büyük olan Newtonyen $J_2$ düğüm gerilemesinden (~126°/yıl) *ayrıştırabilmek* içindir.

Fizikçiler bu değerleri kurgusal "uzay-zaman kumaşının burulması" ile açıklarken, Evrenakı Navier–Stokes denklemlerinden (Navier, 1823; Stokes, 1845) yola çıkarak bunu bizzat lokal Evrenakı akışkanının yerel rotasyon vektörü ($\vec{\Omega}_{rot}$; eski yazım: $\vec{\Omega}$) üzerinden hesaplar:

$$\vec{\Omega}_{rot} = \frac{1}{2} \nabla \times \vec{v}_{vorteks}$$

($\vec{\Omega}_{rot}$: yerel rotasyon vektörü; vortisite ise $\vec{\omega}_v = \nabla \times \vec{v} = 2\vec{\Omega}_{rot}$ olarak tanımlanır. Bir jiroskop, taşındığı akışkanın **vortisitesiyle değil rotasyon hızıyla** — yani vortisitenin yarısıyla — devinir; hız gradyan tensörünün antisimetrik kısmı budur.)

#### Dönme Patinajı: Zarf Taşınır, Ama Dönmez

Hesabın önüne bir kavramsal ayrım geçmelidir ve bu ayrım teorinin kendi öngörüsüdür. Postülat 7'nin sürüklenme zarfı, cismin yerel Evrenakı'yı **öteleme** olarak birlikte taşıdığını söyler ($\vec v_{bağıl}\approx0$) — Michelson–Morley'in sıfır sonucu bunu ölçer. Ancak zarf, gövdenin **dönmesine** aynı ölçüde tutunmaz: Patinaj ilkesi (Bölüm 2.4.2) burada dönme eksenine uygulanır ve ortam gövdeyle birlikte neredeyse hiç dönmez. Nitekim ortam Dünya'yla eş-dönseydi ($\Omega_{ortam}=\omega_\oplus$) jiroskop presesyonu ölçülenin $10^{10}$ katı çıkardı — mutlak dışlanır.

Bu yüzden dönme kuplajı bir **sürüklenme kesri** ($\xi$) ile yazılır. Viskoz ortamda dönen küre için akış çözümü (Stokes rotleti):

$$\vec v_{vorteks} = \xi\,\frac{R^3}{r^3}\left(\vec\omega_\oplus \times \vec r\right),\qquad 0<\xi\ll1$$

Bu alan **dipolardır**; curl'ü alındığında manyetik-dipol yapısı çıkar ve $\vec\Omega_{rot}=\tfrac12\nabla\times\vec v$ ile Lense–Thirring'in açısal biçimi **birebir** elde edilir. Yani teorinin denklemi ek makine gerektirmez; belirlenecek tek nicelik $\xi$'dir.

#### Nicel Karşılaştırma

Dünya için $J_\oplus = I\omega_\oplus = 5{,}85\times10^{33}$ kg·m²/s ve GP-B yarıçapı $r = 7013$ km alındığında, **yörünge yarıçapındaki yerel** sürüklenme hızı:

$$\Omega_{yerel} = \frac{G J_\oplus}{c^2 r^3} = 1{,}26\times10^{-14}\ \mathrm{rad/s} = 81{,}9\ \mathrm{mas/yıl}$$

Ölçülen büyüklük ise **yörünge boyunca ortalanmış** presesyondur. Dipolar alanın açısal yapısı ($3(\vec J\cdot\hat r)\hat r-\vec J$) kutupsal yörünge üzerinde ortalanınca kesin bir geometrik çarpan verir:

$$\bigl\langle 3\cos^2\theta\bigr\rangle - 1 = 3\cdot\tfrac12 - 1 = \tfrac12$$

$$\Rightarrow\qquad \langle\Omega\rangle^{\text{kutupsal}} = \tfrac12 \times 81{,}9 = \mathbf{41{,}0\ mas/yıl}$$

| Büyüklük | Değer | Karşılaştırma |
|---|---|---|
| GP-B ölçümü | $37{,}2\pm7{,}2$ mas/yıl | 1σ aralığı: 30,0–44,4 |
| **Evrenakı öngörüsü** | **41,0 mas/yıl** | **0,52σ** ✓ |
| Genel Görelilik | 39,2 mas/yıl | %4,5 fark |

Kalan %4-5, nokta-dipol yaklaşımının payıdır: GP-B'nin yayımlanmış değeri Dünya'nın tam çekim modelini (GRACE/EGM), yörüngenin küçük basıklığını ve yüksek çokkutupluları içerir. *(Tam türetim ve adım dökümü: **Ek M-40**.)*

#### Kalibrasyon: $\xi$ ve $\Phi/c^2$'nin İkinci Kez Ölçülmesi

Ölçüm, sürüklenme kesrini doğrudan verir. $\langle\Omega\rangle = \xi R^3\omega_\oplus/4r^3$ bağıntısı terse çevrildiğinde:

$$\boxed{\;\xi_{\text{GP-B}} = (4{,}2\pm0{,}8)\times10^{-10}\;}$$

Yani Dünya çevresinde ortam, gövdenin **milyarda yarısı** kadar bir kesirle döner — teorinin öngördüğü neredeyse-tam dönme patinajı, sayıyla doğrulanmış olur.

Bu kesrin yapısı ise beklenmedik bir bağ açar:

$$\xi = 2\left(\frac{I}{MR^2}\right)\frac{GM}{c^2R} = 2\left(\frac{I}{MR^2}\right)\frac{\Phi}{c^2}$$

Sağdaki $\Phi/c^2$, **Teknik Ek B.3'ün arka plan basıncını ($P_0$) sabitlemek için kullandığı tam o gözlemsel girdidir** — GPS uydularının günde 38 µs'si ve Pound–Rebka genliği. Teori böylece şunu söyler: *atom saatinin kaymasını belirleyen sayı, jiroskobun sürüklenmesini de belirler.* Sınandığında:

| $\Phi/c^2$ kaynağı | Değer |
|---|---|
| GPS + Pound–Rebka (Ek B.3'ün girdisi) | $7{,}0\times10^{-10}$ |
| **GP-B jiroskobundan, yukarıdaki bağıntıyla** | $(6{,}3\pm1{,}2)\times10^{-10}$ |
| Sapma | **0,55σ** ✓ |

Yörüngedeki bir jiroskop ile yerdeki atom saatleri, birbirinden tamamen bağımsız iki deney sınıfı olarak, teorinin makinesinden geçirildiğinde aynı sayıda buluşur. Bu, Ek B.3'ün $P_0$ kalibrasyonuna ikinci bağımsız dayanaktır.

#### Kompaktlık Ölçeklemesi ve Ergosferin Mekanik Okuması

$\xi \propto GM/c^2R$ olduğundan dönme sürüklenmesi **kompaktlıkla** ölçeklenir:

| Cisim | $GM/c^2R$ | $\xi$ (dönme sürüklenme kesri) |
|---|---|---|
| Dünya | $7{,}0\times10^{-10}$ | $4{,}6\times10^{-10}$ |
| Güneş | $2{,}1\times10^{-6}$ | $1{,}4\times10^{-6}$ |
| Nötron yıldızı (1,4 M☉, 12 km) | $0{,}17$ | $\approx 0{,}11$ |
| Karadelik ufku | $\to O(1)$ | $\to 1$ |

$\xi\to1$, ortamın **tam eş-dönüşe** geçmesi, yani hiçbir cismin durağan kalamaması demektir — Genel Görelilik'in ergosfer tanımının birebir kendisi. Teori ergosfere mekanik bir okuma verir: **dönme sürüklenmesinin doyduğu yüzey.** Buradan çıkan sınama hattı, nötron yıldızı çevresinde ortamın %11 mertebesinde eş-dönmesidir; bu, Dünya'daki $10^{-10}$'un dokuz mertebe üzerindedir ve Bölüm 3.1.8'in pulsar glitch / devinim programıyla (PSR B1828-11) doğrudan bağlanabilir.

#### GP-B'nin İkinci Etkisi: Jeodetik Presesyon

GP-B **iki** etki ölçmüştür ve ikisi de aynı ölçek yapısından çıkar:

| Etki | Ölçüm | Hassasiyet | Evrenakı |
|---|---|---|---|
| Çerçeve sürüklenmesi (doğu-batı) | 37,2 ± 7,2 mas/yıl | %19 | **41,0** (0,52σ) — bu bölüm, Ek M-40 |
| Jeodetik presesyon (kuzey-güney) | **6.601,8 ± 18,3 mas/yıl** | **%0,28** | **~6.606** — Ek M-42 |

Jeodetik (de Sitter) presesyon, çerçeve sürüklenmesinden 169 kat büyük ve 70 kat daha hassas ölçülmüştür; GP-B'nin ağırlıklı kısmı budur. Etki iki paya ayrılır:

1. **Thomas presesyonu**, $\tfrac12\,GMv/c^2r^2$ — hızlanan çerçevenin özel görelilik kinematiğinden gelir; teorinin kendi türetimlerinden (M-19'un $\gamma$'sı ve boy kısalması) doğrudan çıkar.
2. **Ölçek payı**, $GMv/c^2r^2$ — Genel Görelilik'in uzay eğriliğine yazdığı pay. Teoride karşılığı, madde ölçeğinin ($\Lambda = 1-\Phi/c^2$) cetvelleri ve saatleri yönetirken Zerre'nin yayılma hızını $\Lambda^2$ ile ölçeklemesidir (**Ek M-42**).

İkisi toplandığında GR'ın $\tfrac32\,GMv/c^2r^2$ katsayısı elde edilir; PPN dilinde bu $\gamma=1$'e denktir ve aynı yapı ışık bükülmesini de ($1{,}7512''$) verir. Uzun süre açık kalan **2 çarpanı** sorunu — bükülmenin neden 0,875″ değil 1,75″, presesyonun neden $\tfrac12$ değil $\tfrac32$ katsayısıyla geldiği — böylece tek bir yapıdan çözülmüştür.

> **Karşı Kayıt — kalan kalem.** $\Lambda$ yapısı yalnız **birinci mertebeyi** ($\gamma=1$) verir. Merkür'ün günberi kayması (43″/yüzyıl) ayrıca ortamın ikinci mertebe tepkisini ($\beta$ parametresi, $O(\Phi^2/c^4)$) gerektirir ve **henüz türetilmemiştir.** Teorinin Genel Görelilik'in klasik sınavları karşısındaki kalan tek boşluğu budur (Bölüm 7.4 md.12).

#### Statü — Dürüst Kayıt

Bu sonuç, teoriyi Genel Görelilik'ten **ayırt etmez**; onunla yapısal olarak özdeştir (aynı dürüstlük Bölüm 3.10.3'ün dikey salınım kaydında da vardır). Kazanç iki yerdedir: (i) teori, kendi akışkan denklemlerinden GR'ın sayısını ek serbest parametre üretmeden veriyor; (ii) $\Phi/c^2$'nin iki bağımsız yolla aynı çıkması, teorinin iç tutarlılığının sınanmış bir noktası hâline geliyor.

**Kapanan açık kalem (28 Temmuz 2026).** Bu paragrafın önceki sürümü şunu kaydediyordu: *"$\xi$ Ek C'de [S], gözlemle sabitlenmiş; $\xi\propto\Phi/c^2$ ilişkisi eşleştirmeyle elde edilmiştir."* İlişki artık **türetilmiştir** (Ek M-40, "$\xi$'nin Türetimi"). Ortam bir cismi ancak kavrama hızının bozulduğu ölçüde tutar; bozulmanın kesri Ek M-42'de ışık bükülmesinden sabitlenmiştir ve dönme kütleyi $r^2$ ile ağırlıklandırır:
$$\xi = \frac{I}{MR^{2}}\left|\frac{\delta c_{loc}}{c}\right| = \frac{I}{MR^{2}}\cdot\frac{2\Phi}{c^{2}} = 0{,}3307\times1{,}392\times10^{-9} = 4{,}605\times10^{-10}$$
Serbest sayısal katsayı yoktur ve sonuç, Lense–Thirring'e eşlemeyle bulunanın birebir aynısıdır. Dolayısıyla **GP-B artık bir girdi değil, bir öngörüdür**: zincir ışık bükülmesinden başlar ($1{,}751''$ → $c_{loc}=c\Lambda^2$ → $\delta c/c=2\Phi/c^2$ → $\xi$ → 41,0 mas/yıl) ve $37{,}2\pm7{,}2$ ölçümü bu zinciri **sınar** (0,52σ). Ek M-40'ın rozeti [T]'ye yükselmiştir. *Kalan incelik:* bağıntı birinci mertebedir; $\xi\to1$ yaklaşırken (nötron yıldızı, ergosfer) doğrusal biçim geçerliliğini yitirir (Bölüm 7.4 md.13).

**Sonuç**
Gravity Probe B ve LAGEOS ölçümleri, uzayın bir hiçlik (veya metrik kumaş) olmadığını; Dünya'nın etrafında Ekvator hizasında dönen fiziksel bir "Uzay Nehri" (Evrenakı Vorteksi) okumasıyla uyumlu bir sürüklenme bulunduğunu göstermektedir — ve bu nehrin şiddeti artık sayıyla bellidir ($\xi\approx4\times10^{-10}$). Flyby verisi ise — sonraki geçişlerin sıfır sonuçları nedeniyle — bu nehre üst sınır koyan bir ölçüm olarak kayıttadır (6.3.2).
