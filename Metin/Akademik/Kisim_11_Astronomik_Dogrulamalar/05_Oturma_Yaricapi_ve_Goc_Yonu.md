# 11.5 Oturma Yarıçapı ve Göç Yönü

> [!NOTE]
> **Bölümün konumu ve tezi.** 11.1 gelgit şişkinliğini kurdu (suyu iten F2'nin sıkıştırması, haritayı çizen F1'in gradyanı); 11.4 ortamın gövde çevresindeki kendi dolaşımını ve artık kuplajını kurdu. Bu bölüm ikisini yörünge tarihine bağlar. Tez üç cümledir: **(i)** Bir uydu yörüngesine sürüklenerek değil, ortamın basınç gradyanında **serbest düşerek oturur** (M-2); oturduğu yer, gezegen girdabının ördüğü **optimum yoğunluk kanalıdır** (3.9.3). Bu bölümün nesnesi, o **oturma yarıçapını** çağlar boyunca taşıyan kuvvetlerin muhasebesidir. **(ii)** Taşımanın **yönünü** gelgit şişkinliğinin Evrenakı'da taşıdığı **gradyan lobu** seçer: lob gövdeye kilitlidir, konumunu dönüş–yörünge yarışı belirler ve işaret kuralı beş cisimde — Ay, Deimos, Phobos, Triton, WASP-12b — serbest parametresiz doğrulanır (11.5.2). Standart anlatı torku hesaplar ama şişkinliği neyin ittiğini adlandıramaz; teoride zincir kesintisizdir: şişkinlik → basınç çukuru → kütle-itim gradyanı → teğetsel itki. **(iii)** Teorinin ikinci kanalı — ortamın DY-2 artık kuplajı — kendi türetilmiş yasasıyla ($\gamma\propto\Delta v^4/\rho_c r_t$) tek noktadan kalibre edilip her cisme taşınır: payı $10^{-8}$–$10^{-3}$'tür, hiçbir yarıçapta işaret değiştirmez, ve bu **dönmeyen işaret** plazma sürüklemesinden ilkece ayrışan bir imzadır (11.5.4). Bölümün teknik kazançları: retrograd cisimde **81 çarpanı** (11.5.3), çemberselleşme menzilinin parametresiz ölçüsü $X=(M_p/M_b)(R_b/a)^5 n$ (11.5.5), ve üç kanalın yalnız işaretlerinin değil **menzillerinin** de tablolanması.

## 11.5.0 Gözlem Tabanı ve Bölümün Soruları

Uyduların yörüngeleri sabit değildir, ve ölçülen yönler aynı değildir. Ay Dünya'dan yılda
$3{,}8$ cm **uzaklaşır**; Phobos Mars'a yılda $\sim1{,}8$ cm **yaklaşır**; Triton Neptün'e
göçüyor; sıcak Jüpiter WASP-12b'nin yörüngesi ölçülebilir hızda bozunuyor. Dört cisim, iki ayrı
yön — ve teori bu ikiye ayrılmayı tek bir muhasebeden, serbest parametre eklemeden üretmek
zorundadır. Üretir; bu bölüm o muhasebedir.

### Teorinin nesnesi: oturma yarıçapı

Kitabın yörünge resmi iki yasayla kuruludur ve ikisini ayırmak bu bölümün anahtarıdır:

- **Madde serbest düşer.** Uyduyu yörüngesinde tutan şey ortamın basınç gradyanıdır; cisim o
  gradyanda serbest düşerek dolanır ($v_{yör}=\sqrt{R\,\lvert a_{radyal}\rvert}$, M-2) ve
  yörüngesi, gezegen girdabının ördüğü **optimum yoğunluk kanalıdır** (3.9.3).
- **Ortam dolaşır.** Aynı yarıçapta ortamın kendisi maddenin iki katı hızla döner
  ($v_{ortam}=2\,v_{madde}$, DY-2). Bu dolaşım yörüngeyi **kurmaz** — yörünge sürüklenme değil,
  serbest düşmedir; kayma tam bu yüzden her yarıçapta $\Delta v=v_{madde}$'dir ve ortam maddeyi
  **daima önden geçer.**

**Oturma yarıçapı**, bu serbest düşme dengesinin bugünkü yarıçapıdır. Ve sabit değildir: dengeye
tur başına iş yapan her kuvvet, oturma yarıçapını çağlar ölçeğinde taşır. Teori bu taşımaya
kitabın kendi sözcüğüyle **göç** der (3.9: *"Triton Neptün'e göçüyor"*). *"Kayma"* bu bölümde
kullanılmaz — o terim DY-2'de ortam–madde hız farkına ayrılmıştır.

| Standart çerçeve | Evrenakı |
|---|---|
| Yörünge elementleri $a$, $e$, $i$ nasıl sürüklenir? | **Oturma yarıçapını hangi kuvvet, hangi yöne taşır?** |
| Pertürbasyonun genliği ne? | **Kanal envanteri: her kanalın işareti ve menzili ne?** |

> **Mekanizma zinciri — bölümün omurgası.** Cisim, girdabın basınç gradyanında **serbest düşerek
> oturur** (M-2; kanal: 3.9.3) → oturma yarıçapına tur başına iş yapan üç kanal onu taşır:
> **lob torku** (yönü seçer; sınır gövde dönüşünün senkron yarıçapı) · **ortam artık kuplajı**
> (daima dışa; retrogradda 81 çarpanı) · **seyrelme** (işaretten bağımsız taban) → göçün yönü ve
> menzili bu kanal muhasebesinden okunur. Teorinin kendine ait iki niceliği: **81 çarpanı**
> (DY-2'nin parametresiz sonucu) ve senkron yarıçapın iki yakasında **dönmeyen ortam işareti**
> (plazma sürüklemesinden ilkece ayıran imza).

### Bölümün Soruları

Dört soru sorulur ve dördü de cevaplanır:

| # | Soru | Cevabın yeri |
|---|---|---|
| **S1** | Oturma yarıçapına dokunan kaç kanal vardır; her birinin işaret kuralı nedir? | 11.5.1 |
| **S2** | Gözlenen dört yön (Ay ve Deimos dışa; Phobos, Triton, WASP-12b içe) tek muhasebeden, serbest parametresiz çıkar mı? | 11.5.2 |
| **S3** | Kanalların payları hesaplanabilir mi; kanallar birbirinden hangi imzalarla ayrışır? | 11.5.3–11.5.4 |
| **S4** | Lob kanalının ikinci işi — eksantrikliği yemek — nerede yaşar, nerede biter? | 11.5.5 |

> **Kapsam.** Lob-itki katsayısının nicel türetimi Bölüm 7.4'ün hesap kalemidir ve burada tekrar
> devralınmaz. Burada kurulan yapı **kanal muhasebesidir:** hangi kanalın hangi yönü verdiği ve
> etki mertebelerinin ne olduğu.

## 11.5.1 Kanal Envanteri: Üç Kanal, Üç İşaret Kuralı · **[T]**

Teori göçü tek bir toptan kuvvete yazmaz; oturma yarıçapına dokunan **üç ayrı kanalı** ayrı ayrı
adlandırır ve her birine kendi işaret kuralını verir. 3.9'un *"senkron yarıçapta döner"* kuralı
ile 11.4.8'in *"hiçbir yerde işaret değiştirmez"* kaydı aynı şeyin iki betimi değil, **iki ayrı
kanalın kimlikleridir** — envanter yazılınca ikisinin yan yana durması bir gerilim değil, teorinin
ayrıştırma gücüdür:

| # | Kanal | Neyi taşır | İşaret kuralı | Nerede kurulu |
|---|---|---|---|---|
| **(a)** | **Gelgit şişkinliğinin gradyan lobu** | Şişkinlik bir kütle fazlasıdır ve çevresindeki Evrenakı'da kendi basınç çukurunu taşır; lob gövdeye kilitlidir | **Senkron yarıçapta döner** | Kısım 3.9 |
| **(b)** | **Ortamın artık kuplajı** | Ortam maddeyi her yarıçapta önden geçer ($\Delta v=+v_{madde}$, DY-2); artık kuplaj cismi eş-dönüşe gevşetmeye çalışır | **Hiç dönmez — daima dışa** | 11.4.8 |
| **(c)** | **Kozmolojik seyrelme** | Arka planın yavaş genişlemesi: ortam seyreldikçe çembersel sıkıştırma gevşer | **İşaretten bağımsız** dışa taban | 3.9.4 |

**Kanalların ayrı olduğunun yapısal gerekçesi:** (a)'yı konumlandıran şey **kayanın kendisidir**
— 3.9'un kaydıyla, *"belirleyici olan girdap hızı değil gövde dönüşüdür; çünkü şişkinliği ve
taşıdığı gradyan lobunu konumlandıran, kayanın kendisidir."* (b) ise ortamın **kendi**
dolaşımına aittir ve gövdenin dönüşünden bağımsızdır. Biri gövdeye, öteki ortama kilitli iki ayrı
fiziksel nesne — işaret kurallarının farklı olması bu ayrımın doğrudan sonucudur.

## 11.5.2 Yönü Lob Belirler: Mekanizma, Kural ve Beş Cisim Sınavı

**Mekanizma.** Gelgit şişkinliği, gövde üzerinde yer değiştiren bir kütle fazlasıdır (11.1) — ve
teoride her kütle fazlası, çevresindeki Evrenakı'da kendi **gradyan lobunu**, yani yerel basınç
çukurunu taşır (3.9.2). Uydu bu çukurun kenarında dolanır: lobun kütle-itim gradyanı uyduya
sürekli bir **teğetsel itki** verir. Lob gövdeye kilitli olduğundan itkinin yönünü dönüş–yörünge
yarışı seçer.

**Kural.** Gövde uydusundan **hızlı** dönüyorsa lob uydunun önüne taşınır ve öne doğru teğetsel
itki verir — uydu tur başına enerji kazanır, oturma yarıçapı **dışa** taşınır. Gövde **yavaş**
dönüyorsa lob arkada kalır ve aynı gradyan geri yönde çeker — yörünge **içe** sarmal çizer.
Yörünge **retrograd** ise lob daima karşı yöndedir — içe göç **en hızlı** biçimde işler. Sınır
çizgisi **gövde dönüşünün senkron yarıçapıdır.**

**Sınav (3.9'dan, beş satır, serbest parametre yok):**

| Uydu | Rejim | Öngörü | Gözlem |
|---|---|---|---|
| Ay | senkron üstü, prograd | dışa | $+3{,}8$ cm/yıl ✓ |
| Deimos | senkron üstü, prograd | yavaşça dışa | uzaklaşıyor ✓ *(hız ölçülmemiş)* |
| Phobos | senkron altı, prograd | içe | $\sim1{,}8$ cm/yıl Mars'a doğru ✓ |
| Triton | retrograd | hızla içe | Neptün'e göçüyor ✓ |
| WASP-12b | senkron altı, prograd | içe | yörünge bozunumu ölçüldü ✓ |

**Ve en iyi ölçülen satırda bütçe de kapanır.** Dünya–Ay sisteminde aktarımın iki ucu bağımsız
ölçülmüştür: Ay'ın yörüngesine giren açısal momentum ($+4{,}50\times10^{16}$ kg·m²/s², LLR)
Dünya'nın dönüşünden çıkanla ($-4{,}93\times10^{16}$, gün uzaması) **%91 doğrulukla** karşılanır,
ve şişkinliğin kayma açısı ($\sim3°$) uzaklaşmanın tam yükünü lob torkunun taşıdığı senaryoyu
seçer (3.9.4). Kozmolojik tabana $\lesssim$%10'luk bir pay kalır. Yani beş satır yalnız işarette
değil, ölçümün en sıkı olduğu yerde **muhasebede** de tutar.

**Mekanik aracı.** Standart gelgit muhasebesi aynı işaret tablosunu üretir; sayılar ortaktır ve
bu 3.9'da açıkça kayıtlıdır. Ayrım **mekanizmadadır.** Standart anlatı torku şişkinliğin
"çekimine" yazar ve orada durur: kütle fazlası uyduyu uzaktan, aracısız etkiler — iten şeyin adı
yoktur. Teoride zincir kesintisizdir: **şişkinlik → basınç çukuru (gradyan lobu) → kütle-itim
gradyanı → teğetsel itki.** Torku taşıyan mekanik aracı adlandırılmıştır; ve aynı aracı,
retrograd cisimlerde standart anlatının kendiliğinden vermediği bir çarpanı da getirir —
11.5.3'ün **81**'i. Lob-itki katsayısının nicel türetimi 7.4'ün hesap kalemidir; bu bölümün
sınavı işaret ve bütçe üzerinedir, ve ikisi de geçilmiştir.

## 11.5.3 Kanal (b): Türetilmiş Yasa, 81 Çarpanı ve Kanal Hiyerarşisi · **[T]**

Kanal (b) teorinin en hesaplanabilir kanalıdır, çünkü 11.4.8 iki bağıntıyı birlikte verir:

$$\gamma_{ortam}=\frac{9\eta_E}{2\rho_c r_t^2},\qquad
\eta_E^{etkin}\propto\frac{r_t\,\Delta v^4}{v_{kav}^3}\ \ (\text{M-43})
\qquad\Longrightarrow\qquad
\boxed{\;\gamma_{ortam}\propto\frac{\Delta v^{4}}{\rho_c\,r_t}\;}$$

$v_{kav}$ ortamın kendi niceliği olduğu için sadeleşir. **Kanal tek bir noktadan kalibre edilip
her cisme taşınır** — ve kalibrasyon noktası kitapta zaten kuruludur: Satürn halkası,
$\gamma_{ortam}<1{,}0\times10^{-15}$ s⁻¹, $\Delta v=1{,}90\times10^{4}$ m/s, $\rho_c=900$.

*(Halka taneciğinin yarıçapı metinde yazılı değildir; $\eta_E\lesssim2{,}3\times10^{-11}$ Pa·s
sınırından geriye çözülür, $r_t\approx11$ m — 11.4'ün "en iri blok $\sim10$ m" kaydıyla tutarlı.
Geriye çözülmüş bir sayıdır ve öyle kullanılır.)*

**Retrograd cisimde 81 çarpanı — teorinin kendi öngörüsü.** DY-2 ile ortam prograd yönde $2v$
dolaştığı için retrograd bir cisimde $\Delta v=|2v-(-v)|=3v$ ⟹ $\Delta v^4$ çarpanı
$3^4=\mathbf{81}$. Retrograd cisimlerin ortam kuplajı, prograd eşdeğerlerinden **seksen bir kat**
güçlüdür — DY-2'nin dolaysız, parametresiz sonucudur ve standart anlatıda karşılığı olmayan bir
çarpandır. Triton'un aşağıdaki tablodaki yerini bu yükseltir.

$\dot a=2\gamma a$ ile, gözlenen göçe oran:

| Cisim | $\Delta v$ (m/s) | $r_t$ (m) | $\rho_c$ | $\dot a_{(b)}$ (dışa) | gözlenen $\lvert\dot a\rvert$ | **(b)/gözlenen** |
|---|---|---|---|---|---|---|
| Ay | $1022$ | $1{,}74\times10^6$ | 3344 | $3{,}4\times10^{-10}$ m/yıl | $0{,}038$ m/yıl | $\mathbf{9\times10^{-9}}$ |
| Phobos | $2137$ | $1{,}11\times10^4$ | 1876 | $4{,}5\times10^{-8}$ m/yıl | $0{,}018$ m/yıl | $\mathbf{2{,}5\times10^{-6}}$ |
| Triton *(retro)* | $3v=1{,}32\times10^4$ | $1{,}35\times10^6$ | 2061 | $1{,}8\times10^{-5}$ m/yıl | $\sim0{,}1$ m/yıl | $\sim2\times10^{-4}$ |
| WASP-12b | $2{,}33\times10^5$ | $1{,}36\times10^8$ | 265 | $1{,}4$ m/yıl | $\sim7\times10^{2}$ m/yıl | $\mathbf{2\times10^{-3}}$ |

**Formülün denetimi:** aynı bağıntı halkanın kendisine uygulandığında
$\dot a=2{,}1\times10^{-7}$ m/s verir — 11.4.8'in $2{,}2\times10^{-7}$'siyle birebir ✓

**Okuması: hiyerarşi hesapla kuruldu.** Sıralama tümüyle ölçekleme yasasının öngördüğü yöndedir —
**hızlı, seyrek ve (görece) küçük** cisimlerde en güçlü; en sıkı durum WASP-12b'dir (sıcak
Jüpiter hem çok hızlı, $\Delta v^4$ çarpanı $\times2{,}3\times10^{4}$, hem çok seyrek,
$\rho_c=265$; onu $10^{-3}$'te tutan yalnız devasa yarıçapıdır). Ve bu küçüklük teorinin bir iç
tutarlılık sınavıdır: **aynı yasa** Satürn halkasını dağıtmayan sınırı verir, gözlenen göçlerin
tamamını lob kanalına bırakır, ve en elverişli cisimde bile binde ikiyi aşmaz. Üç kanalın
işbölümü böylece sayıyla belirlenmiş olur: **yönü lob taşır; (b) her yarıçapta dışa dönük,
kalibre edilmiş bir zemindir; (c) işaretten bağımsız seyrelme tabanıdır.**

*(Deimos nicel karşılaştırmaya girmez: göç hızı gözlemsel olarak sıkı sınırlanmamıştır. İşareti
11.5.2'de kayıtlıdır, oranı verilmez — kalem 11.5-ii.)*

## 11.5.4 Dönmeyen İşaret: Kanal (b)'nin Ayırt Edici İmzası ve Sınır İşlevi

11.4.8'in *"hiçbir yerde işaret değiştirmez"* kaydı gerçek bir **ayırt edici imzadır:** plazma
sürüklemesi senkron yarıçapta dönüm yapar, ortam kanalı yapmaz. Senkron yarıçapın iki yakasında
göç artığının işaretini karşılaştıran bir ölçüm, iki kanalı **ilkece** ayırır — ve bu imza
teorinin DY-2'sinden gelir, ödünç alınmış değildir.

Payı bugünkü ölçümlerde $10^{-3}$'ü aşmadığı için kanalın fiilî işlevi **sınır koymaktır:**
*ortamın dışa sürüklemesi halkayı dağıtmamış olmalıdır.* Sınır etkinin gözlenmemesinden okunur;
kanal bugün bir sayı üretmez, bir sayıya üst sınır koyar — 11.4.8'in halka sınırı tam bu biçimde
kurulmuştur. Ötegezegen yörünge-bozunum ölçümleri iyileştikçe imzanın kendisi ölçüme açılır
(kalem 11.5-iii).

> **İşbölümü kaydı — hangi kanal neyi taşıyor.**
>
> | | Statü |
> |---|---|
> | Kanal **(b)** | **Türetilmiş** — $\gamma\propto\Delta v^4/\rho_cr_t$, halka sınırından kalibre, yeni parametre yok |
> | Kanal **(a)** | **İşaret ve bütçe kurulu** — 3.9 işaret kuralını verir, Ay bütçesi %91 kapanır; hız katsayısı 7.4'ün hesap kalemi (11.5-i) |
> | Kanal **(c)** | **Sınır** — Ay'daki $\lesssim$%10 taban, açısal momentum bütçesinin artığından okunur |
>
> Gözlenen göçlerin yönünü ve büyüklüğünü **lob kanalı** taşır; teorinin ortam kanalı bunun
> $10^{-8}$–$10^{-3}$'ü mertebesinde, işareti hiç dönmeyen bir zemindir. İki kanalın işaret
> kuralları farklıdır ve bu fark ölçülebilir bir imzadır — muhasebe kapalıdır.

## 11.5.5 Lob Kanalının Menzili: Çemberselleşme Nerede Yaşar, Nerede Biter · **[T]**

11.5.2 lob kanalının **işaretini** ve bütçesini verdi. Kanal ikinci bir iş de yapar —
eksantrikliği yer — ve teori o işin menzilini sayıyla çizer. 3.9 mekanizmayı çift yıldızlar için
kurmuştu: *"sürekli enerji alışverişi eksantrikliği yiyerek yörüngeyi **çemberselleştirir**"*, ve
sınırını da yazmıştı: *"Lob torku uzaklıkla çok dik düştüğünden bu süreç **yalnız yakın
çiftlerde** tamamlanır."* Buradaki iş, o sınırın **nerede** olduğunu hesaplamaktır.

**Genlik üç çarpanın çarpımıdır ve ikisi teorinin kendi makinesinden gelir.** Şişkinliğin
yüksekliği, 11.2.6'nın izobar okumasıyla dış gradyana verilen figür tepkisidir
($\propto\frac{M_p}{M_b}(R_b/a)^3R_b$); şişkinliğin taşıdığı gradyan lobu bir kütle fazlası olarak
uzaktan **dörtkutup** gibi etkir ($\propto\delta m\,R_b^2/a^4$); ve enerji alışverişi çevrim
başına tekrarlanır ($\propto n$):

$$\boxed{\;X\;\equiv\;\frac{M_p}{M_b}\left(\frac{R_b}{a}\right)^{5}n\;}$$

Lobun **gecikme açısı** — sönümün katsayısı — bu bağıntıda yoktur; 7.4'ün hesap kalemidir
(11.5-i). Kanal bu yüzden tek bir noktadan kalibre edilir, tam olarak kanal (b)'nin Satürn
halkasından kalibre edildiği gibi (11.5.3). **Kalibrasyon noktası gözlemseldir ve serbest
parametre değildir:** ana kol ikililerinde **çembersellik kesim periyodu**,
$P_{kesim}\approx10$ gün.

$$P_{kesim}=10\ \mathrm{gün}\ \Longrightarrow\
a=0{,}1145\ \mathrm{AB},\quad \frac{R_b}{a}=4{,}06\times10^{-2},\quad
X_{kesim}=8{,}05\times10^{-13}$$

**Dokuz cisme taşındığında:**

| Cisim | $R_b/a$ | $X/X_{kesim}$ | Kanalın hükmü | Gözlenen $e$ |
|---|---|---|---|---|
| WASP-12b | $3{,}88\times10^{-2}$ | $\mathbf{7{,}4\times10^{3}}$ | çemberselleştirir | $\approx0$ ✓ |
| Phobos | $1{,}18\times10^{-3}$ | $\mathbf{4{,}0\times10^{1}}$ | çemberselleştirir | $0{,}0151$ |
| Io | $4{,}32\times10^{-3}$ | $\mathbf{1{,}6}$ | çemberselleştirir | $0{,}0041$ *(rezonans zorluyor)* |
| Europa | $2{,}33\times10^{-3}$ | $6{,}8\times10^{-2}$ | sınırda | $0{,}0094$ *(zorlanıyor)* |
| Ganymede | $2{,}46\times10^{-3}$ | $1{,}5\times10^{-2}$ | sınırda | $0{,}0013$ *(zorlanıyor)* |
| **Ay** | $4{,}52\times10^{-3}$ | $5{,}1\times10^{-4}$ | **ölü** | $\mathbf{0{,}0549}$ ✓ |
| **Merkür** | $4{,}21\times10^{-5}$ | $8{,}2\times10^{-10}$ | **ölü** | $\mathbf{0{,}2056}$ ✓ |
| Dünya | $4{,}26\times10^{-5}$ | $1{,}2\times10^{-11}$ | **ölü** | $0{,}0167$ |
| Jüpiter | $9{,}18\times10^{-5}$ | $1{,}4\times10^{-13}$ | **ölü** | $0{,}0489$ ✓ |

Süreye çevrilirse (kesimde $\tau_e\sim1$ Gyr): Ay $2\times10^{12}$ yıl, Merkür
$1{,}2\times10^{18}$ yıl, Dünya $8{,}7\times10^{19}$ yıl — sırasıyla evren yaşının $10^2$, $10^8$
ve $10^{10}$ katı.

> **Sınav tek yönlüdür — kanal (b) ile aynı yapı (11.5.4).** $X>X_{kesim}$ ⟹ cisim dairesel
> olmak **zorundadır** (bir rezonans zorlamıyorsa); $X<X_{kesim}$ ⟹ kanal $e$ hakkında söz
> vermez. Dünya bu yüzden bir karşı örnek değildir: kanalı ölüdür ve $e=0{,}0167$'sini seküler
> dinamik belirler — teori orada söz vermemiştir. Ganymede'in düşük $e$'si de sınavı bozmaz;
> Laplace rezonansı zorluyor.
>
> **Ve iki satır sınavı gerçekten taşır: Ay ile Merkür.** İkisi de kanalı ölü **ve** listenin en
> eksantrik iki cismi. Sıralama ters yönde de tutuyor — kanal nerede öldüyse eksantriklik orada
> hayatta kalmıştır.

$$\boxed{\;\text{Lob kanalı YAKIN ÇİFT rejiminde çemberselleştirir; GEZEGEN rejiminde }
9\text{–}13\text{ mertebe ölüdür.}\;}$$

Bu ölçüm, 11.4.10'un **11.4-viii** kalemini nicelleştirir. O kalem *"dairesellik yitimli bir kanal
ister"* diyordu. Kanal **vardır** — söndürme yetkisini Ek M-44'ün korunumluluk ölçütü verir
(gelgit lobu küresel simetriyi kırar) — ve menzili artık sayıyla çizilidir: 11.4-viii'in konusu
olan **gezegen** yörüngelerinde bu kanal ölüdür; aranan şey $(R_b/a)^5$ ile ölmeyen bir kanaldır,
ve teorinin kendi adayı kayıtlıdır (11.5-iv).

> **Ölçekleme kaydı.** $(R_b/a)^5n$ üsleri denge-gelgit muhasebesinin üsleriyle aynıdır — 3.9'un
> kaydı gereği sayı tablosu ortaktır; mekanik aracı ve kalibrasyon zinciri teorinindir. Kazanç,
> kanalın nerede yaşayıp nerede öldüğünün **tek gözlemsel noktadan** (kesim periyodu) bütün
> cisimlere taşınmasıdır.
>
> **Katsayı kaydı.** Kalibrasyon bütün cisimlerde aynı gecikme katsayısını varsayar; gerçekte iç
> sönüm konvektif yıldız, buzlu uydu ve kayalık gezegen arasında mertebelerce ayrılır. Bu,
> sınırda oturan iki uyduyu (Europa, Ganymede) etkiler; **gezegen satırlarını etkilemez** — iç
> sönüm yayılımı en fazla $\sim10^4$, tablodaki açıklar $10^{9}$–$10^{13}$.

## 11.5.6 Bölümün Bilançosu

| Soru (11.5.0) | Cevap |
|---|---|
| **S1** — Kaç kanal, hangi işaretler? | **Üç kanal.** (a) gradyan lobu — senkron yarıçapta döner · (b) ortam artık kuplajı — hiç dönmez, daima dışa · (c) seyrelme — işaretten bağımsız taban. İşaret kurallarının farkı, kanalların gövdeye/ortama kilitli iki ayrı nesne olmasının sonucu |
| **S2** — Dört yön tek muhasebeyle çıkar mı? | **Evet — lob kuralıyla, serbest parametresiz.** Beş satır tutuyor; en iyi ölçülen satırda (Ay) bütçe %91 + kayma açısı ~3° ile muhasebe de kapanıyor |
| **S3** — Paylar hesaplanabilir mi, kanallar ayrışır mı? | **Evet.** (b) tek noktadan kalibre edilip taşındı: pay $10^{-8}$–$2\times10^{-3}$; retrogradda 81 çarpanı DY-2'nin parametresiz sonucu; dönmeyen işaret plazma sürüklemesinden ilkece ayıran imza |
| **S4** — Çemberselleşme nerede yaşar? | **Yakın çift rejiminde.** $X=(M_p/M_b)(R_b/a)^5n$, kesim periyodundan kalibre; gezegen rejiminde 9–13 mertebe ölü — Ay ile Merkür sıralamayı ters yönden doğruluyor |

Standart anlatı torku gelgit şişkinliğine yazar ama şişkinliği ne ittiğini adlandırmaz; teori
iteni gösterir: **ortamın gradyan lobu** — kütle fazlasının Evrenakı'daki basınç çukuru. Zincir
kesintisizdir ve aynı zincir, standart anlatının kendiliğinden vermediği iki niceliği getirir:
retrograd cisimlerde **81 çarpanı** ve senkron yarıçapın iki yakasında **dönmeyen** bir ortam
imzası. Sayı tablolarının ortak olduğu yerler 3.9'da açıkça kayıtlıdır; mekanizma, envanter ve
kalibrasyon zinciri teorinindir.

**Bölümün tek cümlelik sonucu.** *Bir uydu ortamın basınç gradyanında serbest düşerek oturur;
oturma yarıçapını taşıyan yönü gelgit şişkinliğinin gradyan lobu seçer — sınır gövde dönüşünün
senkron yarıçapıdır — ortam kanalı her yarıçapta dışa dönük, kalibre edilmiş binde-iki mertebesinde
bir zemindir, seyrelme işaretten bağımsız tabandır; ve lob kanalının çemberselleştirme gücü yakın
çift rejiminin dışında biter.* Üç kanalın artık yalnız işaretleri değil **menzilleri** de tabloda.

### Açık kalemler

- **11.5-i** — **Lob-itki katsayısının nicel türetimi.** Lob kanalı işaret ve bütçeyi veriyor;
  göç **hızlarının** katsayısı 7.4'ün hesap kalemidir ve burada devralınmadı. *(11.5.5'in ölçümü
  bu kalemi gerektirmez: orada katsayı gözlenen kesim periyodundan kalibre edilir.)*
- **11.5-ii** — **Deimos'un göç hızının gözlemsel olarak sıkılaştırılması.** İşareti kayıtlı
  (uzaklaşıyor), hız henüz dar bir hata payına sahip değil; nicel karşılaştırmaya girmesi buna
  bağlı.
- **11.5-iii** — **Ötegezegenlerden ikinci bir kalibrasyon.** Tablodaki en sıkı kısıt WASP-12b'den
  geliyor ($2\times10^{-3}$). Yörünge bozunum ölçümleri iyileştikçe kanal (b) üzerindeki ilk
  gerçek üst sınır bu tür uç sistemlerden gelecektir — Satürn halkasından **bağımsız** olacağı
  için kalibrasyonu denetler.
- **11.5-iv** — **Kanal (b) çemberselleştirir mi?** Ortam kuplajı $\Delta v$ ile çalışır ve
  $\Delta v$ yörünge boyunca değişir (günberide büyük) ⟹ eksantrikliğe bağlı bir net etki
  olabilir; $\gamma_{ortam}$'ın $e$ bağımlılığı 7.4'ün hesap kalemidir. Kalem önemlidir: kanal
  (b) $1/a$ ile ölür, $(R_b/a)^5$ ile değil — **gezegen rejiminde ölmeyen tek aday odur.**
  Menzili 11.5.3'ün $\lesssim2\times10^{-3}$'ü ile sınırlıdır; 11.4-viii'i tek başına kapatması
  beklenmez, ama ölçeklemesi doğru yönde olan tek kanaldır.
