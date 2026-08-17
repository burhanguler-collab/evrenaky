# 11.6 İkili Sistemlerin Daralması ve Ortamın Ayarlanma Ölçeği

> [!NOTE]
> **Bölümün konumu ve tezi.** Tez üç cümledir: **(i)** Tek ve küresel simetrik bir gövdenin basınç
> alanı **kimliksel olarak korunumludur** (Ek M-44: $\nabla\rho\times\nabla\chi=0$) — böyle bir
> gövdenin uydusunu söndürmesi *küçük* değil, **imkânsızdır**; Güneş Sistemi yörüngelerinin
> kararlılığı teoride bir tesadüf değil, simetri sonucudur (11.6.8). **(ii)** İki gövdeli bir
> sistemde bu simetri **kırılır:** iki merkezli alanda $\nabla\rho\times\nabla\chi\neq0$, alan
> korunumsuzlaşır ve kapalı yörünge tur başına net iş yapmak **zorundadır** — daralma teoride bir
> anomali değil, korunumluluk ölçütünün iki-cisim hâlindeki zorunlu sonucudur. Enerjiyi taşıyan
> çıkış yolu **sıkışma kanalıdır** (Ek M-5) — gözlem literatürünün *"kütleçekim dalgası"* adıyla
> kaydettiği taşıyıcı; kanalın hız sınavı GW170817'de zaten geçilmiştir. Genlik katsayısı
> $C=-(\partial P/\partial\chi)_\rho$ ile bastırma çarpanı 7.4'ün hesap kalemleridir (11.6-i,
> 11.6-iv). **(iii)** Bölümün işi **kanal muhasebesidir:** dört aday kanal teorinin kendi
> nicelikleriyle ayrıştırılır — gelgit lobu geometriden (11.6.2), artık kuplaj işaret ve
> mertebeden (11.6.3), M-22'nin ters okuması DY-1'in kapsam kaydından (11.6.4), ortak deplasman
> fazlalığı efemeris tutarlılığından (11.6.5) — ve taşıyıcı tek terime iner: **iki-cisim
> hizasızlığı.** Ham veriden bir de iz kayıtlıdır: pulsarın kesirli yavaşlaması ile yörüngenin
> kesirli daralmasının oranı $0{,}40$ — standart kuramın ilişkilendirmek için hiçbir sebebe sahip
> olmadığı, popülasyonda sınanabilir bir korelasyon adayı (11.6.7, 11.6-ii).

## 11.6.1 Gözlem Tabanı ve Mekanizmanın Adresi

Sıkı ikili yıldız sistemlerinin yörüngeleri kapanır. En iyi ölçülen örnek PSR B1913+16'dır:
periyodu her yıl ölçülebilir biçimde kısalıyor,

$$\dot P_b=-2{,}423\times10^{-12}\ \mathrm{s/s}
\qquad(P_b=7{,}75\ \mathrm{sa},\ e=0{,}617)$$

Bu, yörünge yarıçapının yılda birkaç metre küçülmesine karşılık gelir — küçük bir sayı, ama elli
yıllık zamanlama verisinde birikerek gökbilimin en keskin ölçümlerinden birine dönüşür. Aynı olgu
uç rejiminde doğrudan da izlenir: LIGO–Virgo–KAGRA kataloğundaki birleşmelerde (GWTC-3) son
saniyelerin sarmalı kayda alınır. Standart kuram her ikisini de dörtkutup yayınımıyla, B1913+16'da
‰2 içinde kapatır — ve yayınımı uzay-zamanın kendi dalgalanmasına yazar.

Kitap bu sistemleri iki ayrı yerde zaten kullanıyor: B1913+16, 11.3'ün nötron yıldızı
tablosunda bir **spin veri noktası** olarak geçer ($\nu=16{,}9$ Hz, $a^*=0{,}008$); GW170817'nin
dalga hızı ise **Ek M-5**'in kanal tablosunda sıkışma kanalının hızını sınırlamak için kullanılır.
Bu bölüm daralmanın **kendisini** ele alır: yörünge neden kapanıyor, ve teorinin hangi kanalı bunu
taşıyor?

> **Mekanizmanın adresi.** Ek M-44'ün korunumluluk ölçütü iki hüküm birden verir. Birincisi:
> $-\nabla P/\rho$'nun rotasyoneli $C\,\nabla\rho\times\nabla\chi$ ile orantılıdır, ve tek, küresel
> simetrik bir gövdede $\chi$ Poisson kaynaklı, $\rho$ radyal olduğundan çapraz çarpım **kimliksel
> sıfırdır** — alan korunumlu, uydu söndürülemez, kararlı yörüngeler yapısal sonuç (11.6.8).
> İkincisi: **iki gövdeli** bir sistemde alan iki merkezlidir, $\rho$ ile $\chi$ eş-yüzeyleri
> hizadan çıkar ve çapraz çarpım **sıfırdan ayrılır** — alan korunumsuzdur, kapalı yörünge tur
> başına net iş yapar. Daralmayı taşıyan kanal budur: **iki-cisim hizasızlığı**; $\nabla\rho\neq0$
> koşulu onu zorunlu olarak **sıkışma kanalına** bağlar (Ek M-5), ve o kanal hız kısıtını yapısal
> olarak zaten geçer. Aynı ölçüt hem Güneş Sistemi'nin kararlılığını hem ikilinin daralmasını
> **tek kalemden** verir. Genlik 7.4'ün hesap kalemidir (11.6-i, 11.6-iv); bu bölümün işi, öteki
> adayları teorinin kendi nicelikleriyle karantinaya almak ve taşıyıcıyı tek terime indirmektir.
> Kapanmaların hiçbiri dışarıdan bir eleştiriye dayanmaz — dördü de teorinin kendi iç tutarlılık
> sınırlarıdır.

## 11.6.2 Gelgit Lobu: 11.5'in Baskın Kanalı Burada Neden Susar · **[T]**

11.5 yörünge göçünü yöneten kanalın **gelgit şişkinliğinin gradyan lobu** olduğunu kurar (kanal (a)),
ve WASP-12b'nin ölçülen yörünge bozunumunu ona yazar. Sıkı bir ikili pulsar da yakın bir çifttir;
kanalın ilk sırada sorulması gerekir. **İki bağımsız sebeple burada susar, ve ikisi de 11.5'in
kendi bağıntılarından çıkar** — kitabın iç tutarlılığı tam olarak bunu gerektirir: baskın kanal
susacaksa, susuşu teorinin kendi yasasından gösterilmelidir.

**İşaret ters.** Pulsarın dönme periyodu $0{,}059$ s, yörünge periyodu $27.900$ s — spin yörüngeden
$4{,}7\times10^{5}$ kat hızlıdır, yani sistem **senkron yarıçapın çok üstündedir.** 11.5.2'nin
kuralıyla lob uydunun önüne taşınır ve teğetsel itki ileri yöndedir ⟹ **dışa.** Gözlenen içe
sarmaldır.

**Ve büyüklük geometriden ölüyor.** 11.5.5'in kalibre edilmiş bağıntısı doğrudan taşınabilir:

$$\frac{R_b}{a}=\frac{10\ \mathrm{km}}{1{,}95\times10^{9}\ \mathrm{m}}=5{,}1\times10^{-6}
\qquad\text{↔}\qquad
\left.\frac{R_b}{a}\right|_{kesim}=4{,}1\times10^{-2}$$

Nötron yıldızı, çembersellik kesim noktasındaki bir yıldıza göre yörüngesine oranla **7.900 kat
küçüktür**, ve kanal $(R_b/a)^5$ ile ölçeklendiği için bu tek başına $3\times10^{19}$ katlık bir
bastırma demektir:

$$\boxed{\;\left.\frac{X}{X_{kesim}}\right|_{\mathrm{B1913+16}}=1{,}0\times10^{-18}\;}$$

**Ve gözlem ölçeklemeyi doğruluyor.** 11.5.5'in tek yönlü okumasıyla $X\ll X_{kesim}$ olan bir
sistem hakkında lob kanalı söz vermez — B1913+16'nın eksantrikliği **$e=0{,}617$**, kitaptaki
bütün cisimlerin en yükseği, ve olduğu yerde duruyor. Bu, 11.5.5'in Ay–Merkür deseninin uç
noktasıdır: **kanal nerede öldüyse eksantriklik orada hayatta kalmıştır.** Lob kanalının burada
susması bir kaçamak değil, kalibre edilmiş ölçeklemenin sınanması ve tutmasıdır.

> **Rijitlik ikinci bir bastırmadır, ama belirleyici olan değil.** Nötron yıldızı
> $\rho_c\approx5\times10^{17}$ kg/m³ ile gelgit gradyanına neredeyse hiç boyun eğmez, dolayısıyla
> şişkinliğin **kendisi** de bastırılmıştır ve gradyan lobu zayıf kalır. Ama bu, yukarıdaki
> $10^{18}$'in üstüne binen bir ek çarpandır; kanalı susturan şey **geometridir** — bir nötron
> yıldızının yörüngesine oranla ne kadar küçük olduğu.

## 11.6.3 Ortamın Artık Kuplajı: İşaret ve Mertebe · **[T]**

İkinci aday, cismi çevreleyen ortamın onu sürüklemesidir. Bu kanal teoride gerçekten vardır ve
11.5.1'de **(b)** olarak envantere alınmıştır — ama kendi kalibre edilmiş yasası onu burada iki
bağımsız kalemden susturur.

**İşaret ters.** DY-2 her yarıçapta $\Delta v=+v_{madde}$ verir: ortam maddeyi önden geçer. Artık
kuplaj cismi ortamın ritmine, yani **daha hızlı** dönüşe gevşetmeye çalışır; teğetsel itki
dolayısıyla ileri yöndedir ve tork **daima dışa** bakar (11.4.8, ve 11.5.1'in (b) kanalı). Bu,
kanalın rejime bağlı olmayan yapısal özelliğidir — senkron yarıçapta dönmez, hiçbir yerde işaret
değiştirmez. Gözlenen ise içe sarmaldır.

**Büyüklük ölü.** 11.5.3'ün kalibre edilmiş ölçekleme yasası
$\gamma_{ortam}\propto\Delta v^4/(\rho_c r_t)$ ikili pulsara taşınabilir, çünkü yasa tek bir
noktadan kalibre edilip her cisme aktarılabilecek biçimde kurulmuştur. İki çarpan zıt yönde
çalışır: hız **lehte** ($\Delta v\approx4{,}4\times10^5$ m/s ⟹ halkaya göre
$\times2{,}9\times10^{5}$), ama nötron yıldızının kompaktlığı bunu ezer, çünkü
$\rho_c\approx5\times10^{17}$ kg/m³ paydadadır.

$$\dot a_{(b)}<+1{,}7\times10^{-18}\ \mathrm{m/s\ (dışa)}
\qquad\text{↔}\qquad
\dot a_{gözlenen}=-1{,}1\times10^{-7}\ \mathrm{m/s\ (içe)}$$

Kanal hem ters işaretlidir hem $\sim10^{11}$ kat küçüktür. Bu iki sonuç birbirinden bağımsızdır:
işaret düzeltilse bile mertebe kurtarılamaz.

Sayı, 11.5.3'ün tablosundaki desenin uç noktasıdır. O yasa **hızlı ve seyrek** cisimleri kayırır
— WASP-12b'yi binde ikiye kadar çıkaran şey buydu. Nötron yıldızı hızlıdır ama seyrek değildir;
$\Delta v^4$'ün kazandırdığı beş mertebeyi $\rho_c$ tek başına geri alır. **Yasa üçüncü rejimde de
kendi öngördüğü yönde çalışıyor** — kalibrasyonun taşınabilirliği bir kez daha sınanmış oldu.

## 11.6.4 Dolaşım Dengesi Neden Kuvvet Üretmez

Üçüncü aday M-22'nin — **ortamın siklostrofik dengesinin** — kendisinden okunmaya çalışılır ve şu
zinciri izler: kavrama (3.4.4) gövdenin dönüşünü yutar ⟹ dönüşün beslediği ortam dolaşımı yavaşlar
⟹ M-22 **ters** okunduğunda — *dolaşım verili, tutabileceği gradyan $\rho_0v_\theta^2/R$ kadardır*
— tutulabilir gradyan düşer ⟹ fiilî gradyanın fazlası dengesiz kalır ⟹ yapı içe çöker. Ve
yaklaştıkça açık büyüdüğü için daralma **hızlanır**, ki gözlenen de budur.

Zincir üç ağır kısıtı geçer, ve geçtiği için kayda değer:

1. **Yayınım kanalı gerektirmez.** Daralma bir kayıptan çıkmaz, dengenin değişmesinden çıkar.
2. **Açısal momentum atılması gerekmez.** Sabit $L$'de potansiyel derinleşirse yarıçap küçülür.
3. **Enerji rezervi yeter.** Nötron yıldızının spin enerjisi yörünge bağlanma enerjisinin ~6 katıdır.

**Ama kullandığı okuma yetkili değildir, ve bunu söyleyen teorinin kendisidir.** DY-1'in kapsam
kaydı bu adımı adıyla yasaklar: *"M-22 denklemi sisteme yeni bir gradyan eklemez — o gradyanın
ortamın dönüşüyle uyumlu olduğunu söyler. Sağ taraf bir kuvvet değil, ortamın **ataletidir.**"*
M-22 yalnızca bir **denge koşuludur**: iki tarafı da aynı fiziksel gradyanı tarif eder, biri ondan
doğan, öteki onu tutan. Ondan bir kuvvet fazlalığı üretmek aynı gradyanı iki kez saymaya varır —
11.4.9'un kategori kaydı aynı fiziksel muhafızı aynı sebeple kurar. Teori kendi denklemlerinin
nerede kuvvet, nerede koşul olduğunu ayırt eder ve bu disiplin pazarlığa açık değildir.

Fiziksel gerekçe de bunu destekler: ortam gerçek bir akışkandır, dolayısıyla dolaşımı **dayatılmış
değil, kendini ayarlar.** Dönüş yutulduğunda dolaşım kendi denge değerine yeniden yerleşir; geride
dengesiz bir gradyan kalmaz. Ne kadar hızlı yerleştiği DY-1'in ölçek kaydından okunur (11.6.6).

> **Zincirin durumu ve mirası.** Kavramsal olarak tutarlıdır ve yukarıdaki üç kısıtı geçer; ancak
> dayandığı denklem (M-22) bir kuvvet motoru olarak çalıştırılamaz — zincir yanlış olduğu için
> değil, **yetkisiz bir adım içerdiği için** kapanır. Fiziksel içeriği ise kaybolmaz: *dönüşün
> yutulması ile daralmanın aynı sürecin iki ucu olduğu* fikri, 11.6.7'nin ham-veri izinde yaşar,
> ve kuvvet okuması ancak yetkili yitimli kanal — 11.6.1'in hizasızlık terimi — üzerinden
> meşrulaşabilir (11.6-i).

## 11.6.5 Toplanamaz Çapraz Terim ve Efemeris Sınavı · **[A]**

Dördüncü aday, teorinin kendi denklemlerinde gerçekten var olan bir **doğrusal olmamadan** çıkar.
Deplasmanın basınç kuyusu doğrusaldır,

$$P=P_0-\rho_n\frac{\mathcal{G}M}{r}$$

ve iki cismin kuyuları toplandığında standart iki cisim çekimi geri gelir. M-22'nin dolaşım terimi
ise **karesel**dir. İki dolaşım üst üste bindiğinde $|\vec v_1+\vec v_2|^2$ açılımındaki çapraz
terim tek tek cisimlerin hiçbirine yazılamaz: **dolaşım katkısı toplanamaz.** Bu yapısal gözlem
doğrudur ve teorinin standart çerçeveden ayrıldığı gerçek bir noktadır.

Ondan bir kuvvet fazlalığı üretilirse — yani 11.6.4'ün yasakladığı adım atılırsa — fazlalığın
biçimi hesaplanabilir. Gradyanların götürüldüğü noktada hız oranı $q\equiv v_2/v_1=(M_2/M_1)^{1/4}$
ve götürülme payı $2q/(1+q^2)$ çıkar:

| Sistem | $M_2/M_1$ | götürülme payı |
|---|---|---|
| İkili nötron yıldızı | $\approx1$ | **1,00** |
| Dünya–Ay | $1{,}2\times10^{-2}$ | **0,60** |
| Güneş–Jüpiter | $9{,}5\times10^{-4}$ | **0,34** |
| Güneş–Dünya | $3{,}0\times10^{-6}$ | **0,083** |
| Güneş–Merkür | $1{,}7\times10^{-7}$ | **0,040** |

Pay kütle oranıyla değiştiği için fazlalık **evrensel bir çarpan olamaz**, ve bunun ölçülebilir bir
sonucu vardır: **aynı merkez cisminin kütlesi farklı yörüngelerden farklı okunur.** Merkür ile
Jüpiter arasındaki fark %30, Dünya–Ay'da %60 olurdu.

**Gözlem bunu dışlıyor.** Gezegen efemerisleri (INPOP, DE440) $\mathcal{G}M_\odot$'u bütün
gezegenlerde $\sim10^{-10}$ tutarlılıkla belirler; LLR'nin verdiği $\mathcal{G}M_\oplus$ uydu
jeodezisinin değeriyle $10^{-9}$ içinde uyuşur. Böyle bir yayılım için yer yoktur — kuvvet
okuması gözlemle de kapanır, yani DY-1'in yasağıyla efemeris aynı hükmü iki bağımsız koldan verir.

> **Ve bu argüman döngüsel değildir.** Tek tek kütlelerin doğru olmasına dayanmıyor —
> **farklı kütle oranlarından okunan aynı $\mathcal{G}M$'in tutarlılığına** dayanıyor. Gezegen
> kütleleri uydularından ve uzay araçlarının izlenmesinden bağımsızca bilindiği için sistem
> **aşırı belirlenmiştir**: fazlalık varsa bir yerde artık olarak görünmek zorundadır.

Çapraz terimin kendisi yapısal olarak vardır; görünmemesinin mekanik adayı 11.6.6'nın ayarlanma
ölçeğidir — ortam, dengesizlik birikmeden kendini yeniden yerleştirir. Bastırmanın tam hesabı
7.4'ün kalemidir (**11.6-iii**).

## 11.6.6 Ortamın Ayarlanma Ölçeği · **[T]**

Yukarıdaki iki kapanmanın ortak mekanik gerekçesi tek bir orandan okunur. Dengesizliğin birikme
süresi ile ortamın kendini ayarlama süresi arasındaki oran DY-1'in ölçek kaydında **parametresiz**
olarak çıkar:

$$\boxed{\;\frac{t_{ayarlanma}}{t_{birikme}}=\sqrt2\,\frac{v}{c_0}\;}$$

Sağ tarafta yalnız yörünge hızının ışık hızına oranı vardır — serbest bir katsayı yoktur. Kompakt
bir ikilide bile oran $\sim2\times10^{-3}$'tür: ortam, dengesizlik birikmeden **500 kat** önce
ayarlanır. DY-1'in denge okuması bu yüzden orada da geçerli kalır, ve 11.6.4'ün zincirinin
gerektirdiği *biriken* dengesizlik hiçbir zaman oluşmaz.

Oran $v/c_0$ ile büyüdüğü için rejim ayrımı da bu nicelikten okunur, ve teorinin ikili pulsarı Güneş
Sistemi'nden ayırdığı yer burasıdır:

| Sistem | $v$ (m/s) | $t_{ayarlanma}/t_{birikme}$ | ayarlanma kaç kat hızlı |
|---|---|---|---|
| Ay–Dünya | $1022$ | $4{,}8\times10^{-6}$ | $2\times10^{5}$ |
| İkili pulsar B1913+16 | $4{,}4\times10^{5}$ | $2{,}1\times10^{-3}$ | $\mathbf{5\times10^{2}}$ |

Aradaki $\sim400$ kat, iki rejim arasındaki yapısal farktır — ve farkın sonunda bile ayarlanma iki
buçuk mertebe baskındır: **denge-temelli hiçbir okuma kompakt rejimde bile kuvvete
çevrilemez.** Daralmayı taşıyabilecek tek terim, dengenin hiç kuramadığı terimdir — hizasızlığın
korunumsuz çapraz çarpımı (11.6.1). Ayarlanma ölçeği böylece iki işi birden yapar: yetkisiz
okumaları kapatır, yetkili kanalı yalnız bırakır.

## 11.6.7 Zamanlama Nicelikleri: Spin ile Daralmanın Oranı · **[G]**

İkili pulsarların kütleleri ve yarı-büyük eksenleri standart dinamik varsayılarak çıkarıldığı için
teori onları hazır girdi olarak alamaz. **Zamanlama nicelikleri bu çekinceden muaftır** — doğrudan
sayılan darbe varış zamanlarıdır — ve orada bir kayıt vardır:

| Nicelik | Değer |
|---|---|
| Yörüngenin kesirli daralma hızı, $-\dot a/a$ | $5{,}8\times10^{-17}$ s⁻¹ |
| Pulsarın kesirli yavaşlama hızı, $\dot P/P$ | $1{,}5\times10^{-16}$ s⁻¹ |
| **oran** | $\mathbf{0{,}40}$ |

**Standart kuramda bu iki sayının ilişkili olması için hiçbir sebep yoktur.** Orada daralma yalnız
iki kütleye, $a$'ya ve $e$'ye bağlıdır; pulsarın spini denkleme hiç girmez, ve yavaşlaması ayrı bir
manyetik dipol süreciyle açıklanır. İki bağımsız sürecin kesirli hızlarının aynı mertebede çıkması
beklenmez. Teorinin dönüş-yutulması resminde ise (11.6.4'ün mirası) ikisi **aynı** sürecin iki
ucudur — ve oranın $O(1)$ olması tam olarak beklenen şeydir.

> **Tek sistemde iz, popülasyonda sınav.** $0{,}40$ tek sistemde tesadüf olabilir; iki nicelik de
> mertebe aralığı geniş olmayan büyüklüklerdir. Ayırt edici hâle gelmesi için **popülasyon
> taraması** gerekir: ikili pulsarlarda spin yavaşlaması ile yörünge daralması arasında korelasyon
> var mı? İki spinin birlikte ölçüldüğü çift pulsar J0737−3039 en iyi adaydır. Korelasyon
> **bulunursa standart kuramın onu açıklayacak bir mekanizması yoktur** — bulunmazsa teori bir
> şey kaybetmez, çünkü iz zorunlu bir öngörü olarak değil kayıt olarak düşülmüştür.
> → **11.6-ii**

## 11.6.8 Bölümün Bilançosu

| Kanal | Akıbet | Kapatan / Kuran |
|---|---|---|
| Gelgit lobu (11.5'in kanalı) | ❌ ters işaretli **ve** $10^{18}$ kat küçük | Geometri: $(R_b/a)^5$ ile 11.5.5'in kalibre yasası |
| Ortamın artık kuplajı | ❌ ters işaretli **ve** $10^{11}$ kat küçük | DY-2 + 11.5.3'ün kalibre yasası |
| Dolaşım dengesinin bozulması | ⏸ **çürütülmemiş, yetkisiz** — mirası 11.6.7'de | DY-1'in kapsam kaydı |
| Ortak deplasmanın fazlalığı | ❌ kütle oranına bağlı ⟹ %30–60 yayılım | Efemeris + LLR tutarlılığı |
| **İki-cisim hizasızlığı → sıkışma kanalı** | ✅ **taşıyıcı** — genlik 7.4'te (11.6-i, 11.6-iv) | Ek M-44 ölçütü + Ek M-5 |

Muhasebe kapalıdır: dört aday teorinin kendi nicelikleriyle ayrışır — üçü elenir, biri yetkisizdir
ve mirasını 11.6.7'nin izine bırakır — ve geriye tam olarak bir terim kalır: **korunumluluk
ölçütünün iki-cisim hâlinde sıfırdan ayrılan çapraz çarpımı.** Elemeler bu yüzden bir kayıp değil,
teoremin öteki yarısıdır: daralmayı taşıyan kanal, elenenlerin hiçbirinin sahip olmadığı tek
özelliğe sahiptir — **yitimlidir.**

**Ve ilk satır kitabın iç tutarlılığı için önemlidir:** 11.5 göçün baskın kanalının gelgit lobu
olduğunu kurar, dolayısıyla o kanalın burada **neden** sustuğu gösterilmek zorundaydı. Gösterilen
şey bir kaçamak değil, 11.5.5'in kendi ölçeklemesinin üçüncü rejimde sınanıp tutmasıdır —
$e=0{,}617$'nin hayatta olması, Ay–Merkür deseninin uç noktası olarak kanalın öldüğü yeri
doğrular.

**Madalyonun öteki yüzü: teori sıradan yörüngeleri kurutacak bir kanal da getirmez — ve bunun
sebebi yapısaldır.** Ek M-44'ün korunumluluk ölçütü, tek ve küresel simetrik bir gövdenin basınç
alanının **kimliksel olarak** korunumlu olduğunu verir: $\chi$ Poisson kaynaklı, $\rho$ radyal,
dolayısıyla $\nabla\rho\times\nabla\chi=0$. Böyle bir gövdenin uydusunu sönümlemesi *küçük* değil,
**imkânsızdır.** Gerçek gövdeler tam küresel olmadığı için aşağıdaki üç sayı yine gereklidir — ama
sıfırdan sapmanın ölçüsü olarak okunurlar, tesadüfen küçük çıkmış nicelikler olarak değil:

| Kayıt | Değer | Nerede |
|---|---|---|
| F5'in 1 AU'daki payı | $1{,}1\times10^{-15}$ | 11.4.3 |
| Ortam kanalının gözlenen göçe oranı, üst uç | $2\times10^{-3}$ | 11.5.3 |
| Ayarlanmanın birikmeye hız üstünlüğü, en kötü durum | $500$ kat | 11.6.6 |

Aynı ölçüt iki ucu birden tutar: **tek gövde ⟹ korunum ⟹ kararlılık; iki gövde ⟹ hizasızlık ⟹
daralma.** Güneş Sistemi'nin milyarlarca yıllık kararlılığı ile Hulse–Taylor'ın elli yıllık
sarmalı, teoride aynı satırın iki okumasıdır.

**Bölümün tek cümlelik sonucu.** *Tek ve küresel gövdenin alanı kimliksel korunumludur — uydu
söndürülemez, yörüngeler kararlıdır; iki gövdede korunum kırılır — yörünge tur başına net iş
yapmak zorundadır ve enerji sıkışma kanalından çıkar; taşıyıcı terim adlandırılmıştır, genliği
7.4'ün hesap kalemidir, ve ham veride standart kuramın ilişkilendiremediği bir iz beklemededir:
spin yavaşlaması ile daralmanın 0,40 oranı.*

### Açık kalemler

- **11.6-i** — **Taşıyıcı kanalın genliği.** Kanal adlandırılmıştır: iki-cisim hizasızlığı —
  $-\nabla P/\rho$'nun rotasyoneli $C\,\nabla\rho\times\nabla\chi$ ile orantılı, tek gövdede
  kimliksel sıfır, iki gövdede sıfırdan ayrık; $\nabla\rho\neq0$ koşulu onu zorunlu olarak
  **sıkışma kanalına** bağlar (Ek M-5), ki hız kısıtını yapısal olarak geçer. Sayıya dökülmesi
  iki girdi ister: $C=-(\partial P/\partial\chi)_\rho$'nun değeri (M-46'nın açık ucu) ve
  hizasızlık açısının yörünge boyunca profili. İkisi de 7.4'ün hesap kalemidir. *(11.6.4'ün
  zinciri, kuvvet okuması bu kanal üzerinden meşrulaştığında yeniden değerlendirilecektir.)*
- **11.6-iv** — **Bastırma çarpanının türetimi.** Ek M-44'ün ölçütü *statik* alan için kesindir;
  zaman bağımlı hâlde küresel-radyal bir gecikme bile kapalı yörüngede net iş yapabilir. Naif
  okuma bu sistemde tur başına $\sim2\times10^{-3}$ verir; gözlenen $\sim1{,}6\times10^{-12}$'dir
  — yani **kanal ailesinin enerji kapasitesi gözleneni fazlasıyla karşılar**, ve gözlenen değeri
  seçen bastırma çarpanı (adayı: 11.6.6'nın ayarlanması, $\sqrt2\,v/c_0$) henüz türetilmemiştir.
  Genlik hesabının öteki yarısıdır; **11.6-iii ile aynı aile.**
- **11.6-ii** — **Spin ↔ daralma korelasyonunun popülasyon taraması.** 11.6.7'nin $0{,}40$'ı tek
  sistemdedir; geniş bir ikili pulsar popülasyonunda sınanmalıdır. Her iki spinin de ölçülebildiği
  çift pulsar J0737−3039 birincil aday. Korelasyon **bulunursa** standart kuramın açıklayacak bir
  mekanizması yoktur.
- **11.6-iii** — **Toplanamaz çapraz terimin gerçek büyüklüğü.** Yapısal olarak vardır; efemeris
  tutarlılığı onu bastırılmış olmaya zorlar. **Bastırmanın tam hesabı** — 11.6.6'nın ayarlanması
  yeterli mi, yoksa ek bir etki mi var — 7.4'ün kalemidir.
