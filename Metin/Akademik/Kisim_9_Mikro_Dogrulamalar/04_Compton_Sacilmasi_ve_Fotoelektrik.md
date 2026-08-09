# 9.4 Compton Saçılması ve Fotoelektrik Etki

Standart fiziğin, ışığı "foton" adlı kütlesiz bir parçacık olarak kabul etmesinin iki büyük tarihsel dayanağı fotoelektrik etki ile Compton saçılmasıdır. Kısım 2 bu iki olgunun **mekanizmasını** kurmuştu: fotoelektrik olay, kütleli Zerre katarının ardışık rezonans darbeleriyle elektronu sökmesidir (2.2.2–2.2.3, Ek M-10/M-11). Bu bölümün görevi mekanizma anlatmak değil, **doğrulamaktır**: kurulmuş mekaniğin sayıları, yüz yıllık ölçüm literatürünün sayılarıyla tek tek karşılaştırılır ve — bölümün asıl vuruşu — fotoelektrik veriden sabitlenen tek bir çarpımın ($\delta\tau$), Compton saçılmasının bütün nicel içeriğini **sıfır yeni parametreyle** ürettiği gösterilir.

Bölümün ışıktan istediği envanter bilinçli olarak asgaridir: **Zerre katarı**, **Zerre aralığı** ve **katar sayısı** — teorinin en sağlam üç kalemi. Kesikliliğin ("kuantum"un) adresi ışık değil, alıcıdır; bu ayrımın anatomisi ($h=\delta\tau$, pencere mekaniği, Zerre Paketi) 9.2'de kurulmuştur — bu bölüm onu yalnız sınava sokar.

## 9.4.1 Doğrulanacak Gözlem Envanteri

İki olgu ailesinin, herhangi bir modelin hesap vermek zorunda olduğu ölçülmüş içeriği şudur:

| # | Gözlem | Ölçülen değer / davranış | Kaynak |
|---|---|---|---|
| G-1 | Fotoelektrik doğrusallık: $E_{ke}$, $\nu$ ile doğrusal; eğim evrensel | eğim $= h = 6{,}626\times10^{-34}$ J·s | Millikan, 1916 |
| G-2 | Gecikmesiz emisyon: çok düşük şiddette bile | $\lesssim 3$ ns | Lawrence & Beams, 1927 |
| G-3 | Eşik-altı frekansta şiddet işe yaramaz; eşik üstünde doyma akımı ∝ şiddet | eşik keskin; $E_{ke}$ şiddetten bağımsız | Lenard, 1902; Millikan, 1916 |
| G-4 | Compton kayması: saçılan X-ışını çizgisi açıya bağlı kayar; kayma **gelen dalga boyundan ve şiddetten bağımsız** | $\Delta\lambda = \lambda_C(1-\cos\theta)$, $\lambda_C = 2{,}4263$ pm | Compton, 1923 |
| G-5 | Kaymamış (koherent) çizgi: kaymış çizginin yanında her zaman bir de kaymamış tepe vardır | kayması ölçülemeyecek kadar küçük | Compton, 1923 |
| G-6 | Geri tepen elektronlar: her saçılma olayında, korunumun öngördüğü yön ve enerjide | olay-bazlı koinsidans | Wilson, 1923; Bothe & Geiger, 1925; Compton & Simon, 1925 |

G-4'ün tarihî tuhaflığı özellikle kaydedilmelidir: klasik dalga kuramı (Thomson saçılması) hiçbir kayma öngörmez; kayma öngören her model, ışığın **sayılabilir mermiler** hâlinde momentum teslim ettiğini kabul etmek zorundadır. Evrenakı Teorisi bu kabulü zaten kuruluşundan taşır — ışık, kütleli Zerrelerin katarıdır (Postülat 4, 2.2.2).

## 9.4.2 Fotoelektrik Ayağı: Mekanikten Sayıya

Mekanizmanın anatomisi 9.2.1–9.2.2'de, türetimler Ek M-10/M-11'dedir; burada yalnızca sınav sonuçları toplanır. Muhasebenin iki denklemi:

$$\Phi + E_{ke} = N\cdot\eta\cdot\tfrac12 m_z\!\left(c^2 + k_a v_{cev}^2\right), \qquad N = \nu\tau \;\Longrightarrow\; E_{ke} = (\delta\tau)\,\nu - \Phi$$

| Sınav | Teorinin sözü | Gözlem | Sonuç |
|---|---|---|---|
| G-1 doğrusallık | $E_{ke}$, $\nu$ ile doğrusal; eğim $=\delta\tau$, malzemeden bağımsız (kopma penceresi $\tau$ evrensel) | Millikan doğrusu; eğim $=h$ | ✅ yapı; çarpım $\delta\tau = h$ **gözlemle sabitlenir** [S] |
| G-2 gecikme | birikim penceresi $N\approx1{,}5\times10^4$ vuruş → morötesi ritminde $\approx10$ ps | $\lesssim3$ ns | ✅ üç mertebe payla |
| G-3a eşik | eşik-altı ritimde vuruşlar sönüm süresinden seyrek; enerji birikmez | keskin eşik | ✅ |
| G-3b şiddet | şiddet = paralel katar sayısı; tek elektron tek katarla etkileşir → $E_{ke}$'ye girmez, yalnız sökülen elektron **sayısını** artırır | $E_{ke}$ şiddetten bağımsız; doyma akımı ∝ şiddet | ✅ iki yüzüyle birden |
| çapraz kontrol | $h = 2\tau m_z^2c^2/m_e$ özdeşliği $\tau = 15{,}5$ ps ister; bağımsız birikim hesabı $\sim10$ ps verir | — | ⚠ 1,6 kat uyum (M-10; mertebe doğru, hassas tayin değil) |

Fotoelektrik ayağının doğrulama bilançosu budur: dört gözlemsel davranışın dördü mekanikten çıkar; ödenen bedel, $\delta$ ve $\tau$'nun ayrı ayrı değil yalnız **çarpım** olarak sabitlenmesidir (rozet [S]; Ek C).

## 9.4.3 Compton Saçılması I: Korunum Katmanı

Compton olayı için yeni hiçbir kavram icat edilmez; türetim üç girdiden yürür ve ışık tarafında katar ile aralıktan fazlasını kullanmaz:

1. **Işık tarafı — katar:** aralık $\lambda$, ritim $\nu = c/\lambda$. Şiddet, paralel katar sayısıdır ve tek elektron tek katarla etkileştiği için (D-21, M-10) tek olayın muhasebesine hiç girmez.
2. **Alıcı tarafı — pencere:** elektron-girdabın etkileşim penceresi $\tau$ — fotoelektrik mekanizmayı taşıyan **kopma penceresinin** kendisi (M-10/M-11). Bir pencere boyunca elektron $N = \nu\tau$ vuruş alır; teslim edilen enerji, M-11'in birikim adımından, $E_w = (\delta\tau)\,\nu = h\nu$'dür. 17,4 keV'lik X-ışını ritminde bu, pencere başına $N \approx 6{,}5\times10^7$ vuruş demektir.
3. **Pencere momentumu:** bir pencerede teslim edilen net momentum, ölçülen ışınım basıncının verdiği $p_w = E_w/c$ değeridir; 2.2.1'in açıkça teslim ettiği üzere bu ölçümde hesap çelişkisi yoktur — ayrışma taşıyıcının ontolojisindedir. *(Bu değerin $\eta$-çarpışma muhasebesinden ilk-ilkeler türetimi açık kalemdir — 9.4.8/i.)*

Kesikliliğin adresi 9.2.1'de kurulmuştu: "foton", cisim değil pencerelik alışveriştir; kuantum ışıkta değil etkileşimde yaşar, ışığın kendisi kesintisiz katardır. Compton muhasebesine bunun taşıdığı tek içerik şudur: tek olayın alışverişi $E_w=h\nu$, $p_w=h\nu/c$'dir — gerisi kinematiktir.

Bu üç girdiyle Compton olayı saf **Newtonyen çarpışma kinematiğidir**: duran bir elektron-girdap, bir pencerede katardan $E_w = h\nu$, $p_w = h\nu/c$ alır; yönü değişen katar dilimi $\theta$ açısıyla, elektron $q$ momentumuyla ayrılır. X-ışını rejiminde ($h\nu \ll m_ec^2$ enerji ölçeği) elektronun geri tepmesi yavaştır ve görelilik gerekmez:

$$\text{momentum: } q^2 = \left(\frac{h\nu}{c}\right)^2 + \left(\frac{h\nu'}{c}\right)^2 - 2\frac{h\nu}{c}\frac{h\nu'}{c}\cos\theta, \qquad \text{enerji: } h\nu - h\nu' = \frac{q^2}{2m_e}$$

İki denklem birleştirilip $\lambda = c/\nu$ (Zerre aralığı) diline çevrildiğinde, önder mertebede:

$$\boxed{\Delta\lambda = \frac{\delta\tau}{m_e c}\left(1-\cos\theta\right) = \lambda_C\left(1-\cos\theta\right), \qquad \lambda_C \equiv \frac{\delta\tau}{m_e c} = \frac{2\tau m_z^2 c}{m_e^2}}$$

Compton kayması, teorinin dilinde **saçılan katarın Zerre aralığının açılmasıdır**: pencere alışverişinin bir kısmı geri tepen girdaba gittiği için yönü değişen katar diliminin ritmi düşer, ardışık mermiler arasındaki mesafe açılır. G-4'ün iki tuhaflığı da burada kendiliğinden çözülür: **(a)** formülde $\lambda$ yoktur ve $\nu$-bağımlılığı $\lambda\nu = c$ ile düşer — kayma yalnız açıya ve hedef kütlesine bağlıdır; **(b)** pencere teslimatı katar-içi ritimle ölçeklenir, paralel katar sayısıyla değil — kayma şiddetten de bağımsızdır. İkisi de kinematiğin zorunlu sonucudur, ek varsayım değil.

## 9.4.4 Compton Saçılması II: Mekanizma Katmanı (Doppler Okuma)

Korunum katmanı sonucu verir ama süreci anlatmaz; teorinin temas-mekanik yükümlülüğü süreçtir. Süreç şudur: katar, elektron-girdapla etkileşim penceresi boyunca boğuşur; girdap pencere boyunca geri teper; yönü değişen katar dilimi, **geri tepmekte olan bir kaynağın üzerinden yeniden yayılır**. Geri çekilen kaynaktan çıkan katarın ritmi Kısım 6.1'in Doppler mekaniğiyle düşer — aralık açılır. Alış ve yeniden-yayım olmak üzere iki Doppler adımı üst üste konduğunda, geri tepme momentumu $h\nu/c$ mertebesinde olan bir elektron için tam olarak 9.4.3'ün formülü geri gelir.

Bu okuma teorinin icadı değildir; Schrödinger, Compton olayının kayma formülünün geri tepen elektrondan **çift Doppler** olarak türetilebildiğini 1927'de göstermiştir (Schrödinger, 1927). Standart fizikte bu bir "alternatif hesap yolu" olarak kalır; Evrenakı Teorisi'nde ise mekanizmanın kendisidir: ortada kütlesiz bir kuantum yoktur, geri tepen bir girdap ve ritmi Doppler ile açılan somut bir mermi katarı vardır. Aynı Doppler makinesi kitapta kızıla kaymayı da taşıdığından (Kısım 6.1–6.2), Compton kayması ile kozmolojik kızıla kayma teoride **akraba mekanizmalar** hâline gelir: ikisi de katar ritminin mekanik yeniden ayarlanmasıdır; biri geri tepen hedefte, öteki yol boyu ortamda.

## 9.4.5 Sayısal Karşılaştırma

**(a) Compton dalga boyu — parametresiz üretim.** $\lambda_C = 2\tau m_z^2c/m_e^2$ zincirine fotoelektrik eğimin sabitlediği $\tau = 15{,}5$ ps, Postülat 4'ün $m_z = 1{,}47\times10^{-35}$ kg değeri ve $m_e$ konduğunda:

$$\lambda_C = \frac{2\times(15{,}5\times10^{-12})\times(1{,}47\times10^{-35})^2\times(3{,}0\times10^8)}{(9{,}11\times10^{-31})^2} \approx 2{,}42\times10^{-12}\ \text{m}$$

Ölçüm: $\lambda_C = 2{,}4263$ pm (Tiesinga ve ark., 2021). Uyum, $h=\delta\tau$ özdeşleşmesinin cebirsel sonucudur — bağımsız bir tayin değildir; bağımsız içerik bir sonraki maddededir. M-10'un fotoelektrikten **bağımsız** mekanik birikim tahmini $\tau\approx10$ ps kullanılırsa $\lambda_C\approx1{,}6$ pm çıkar: aynı 1,6 katlık pay, iki olgu ailesinde aynı yönde ve aynı boyda durur.

**(b) Açı taraması.** $\Delta\lambda = \lambda_C(1-\cos\theta)$:

| $\theta$ | 45° | 90° | 135° | 180° |
|---|---|---|---|---|
| $\Delta\lambda$ (pm) | 0,71 | 2,43 | 4,14 | 4,85 |

Compton'ın özgün ölçümü (molibden K$\alpha$, $\lambda=71{,}1$ pm, $\theta=90°$): gözlenen kayma $\approx2{,}4$ pm ↔ öngörü 2,43 pm — yüzde birkaç içinde (Compton, 1923). Modern hassas ölçümler formülün açı bağımlılığını bütün taramada doğrular.

**(c) Kaymamış çizgi (G-5).** Elektron atoma sıkı bağlıysa pencere alışverişinin geri tepen hedefi tek elektron değil bütün atomdur; formülde $m_e \to M_{atom}$ geçer. Karbon için $m_e/M_{atom} \approx 4{,}6\times10^{-5}$, yani kayma $\sim1{,}1\times10^{-16}$ m — ölçülemez: çizgi "kaymamış" görünür. Bu, Ek M-10'daki $4m/M$ mantığının aynısıdır; kaymış/kaymamış çizgi ikilisi, tek formülün iki hedef-kütle rejimidir. Ağır elementlerde (sıkı bağlı elektron kesri büyük) kaymamış tepenin göreli güçlenmesi de aynı mantığın nitel sonucudur.

**(d) Compton kenarı — gündelik doğrulama.** $\theta=180°$'de elektrona aktarılan enerji maksimumdur; 662 keV'lik Cs-137 çizgisi için kinematik kenar 477 keV'dir ve her sintilasyon laboratuvarında her gün ölçülür. Bu enerji ölçeği ($h\nu \sim m_ec^2$) 9.4.3'ün Newtonyen rejiminin dışındadır; kenarın konumu ölçülen $E$–$p$ korunumundan izlenir, elektronun bu hız rejimindeki kinematiğinin teori-içi (Ek A hız merdiveni üzerinden) türetimi açık kalemdir (9.4.8/iv).

## 9.4.6 Tarihsel Sınamalarla Yüzleşme: Koinsidans Deneyleri

Fotoelektrik ayağın üç klasik sınavıyla yüzleşme 2.2.3'te yapılmıştı; Compton ayağının kendi tarihsel sınavı daha az bilinir ama daha serttir. 1924'te Bohr–Kramers–Slater (BKS) kuramı, enerji-momentum korunumunun tek tek olaylarda değil yalnız **istatistiksel ortalamada** geçerli olduğunu öne sürerek Compton olayını sürekli-alan diliyle kurtarmayı denedi. İki deney bu kapıyı kapattı: Bothe & Geiger (1925) saçılan ışınla geri tepen elektronun **aynı anda** (koinsidans içinde) çıktığını; Compton & Simon (1925) sis odasında yön korelasyonunun olay-bazında korunum denklemlerine uyduğunu gösterdi. Korunum, ortalamada değil **her tek olayda** geçerlidir.

Evrenakı Teorisi'nin bu sınava cevabı pencere mekaniğidir: geri tepen elektron ile yönü değişen katar dilimi, **aynı etkileşim penceresinin iki çıktısıdır** — ayrı ayrı üretilmezler, tek temas olayının iki yüzüdürler. Pencere süresi ($\tau \approx 15$ ps), koinsidans deneylerinin zaman çözünürlüğünün (ns–µs) çok altındadır; iki çıktı deney gözünde kesin eşzamanlıdır. Ve korunum her pencerede **mekanik olarak** — temasla — sağlanır, ortalamada değil: istatistiksel BKS'yi öldüren ölçüm, pencere modelinin doğal çıktısıdır. Teori burada standart kuantum mekaniğiyle aynı safta, yarı-klasik istatistiksel modellerin karşısındadır — ayrışma noktası korunumda değil, **kesikliliğin adresindedir**: standart model kesikliliği ışığın kendisine yazar ("foton"), teori alıcının penceresine yazar; ışık tarafında yalnız katar ve aralık kalır.

## 9.4.7 Kenetlenme: Tek Çarpım, İki Olgu Ailesi

Bölümün bilançosu tek cümlede toplanır: **fotoelektrik veriden sabitlenen $\delta\tau$ çarpımı, Compton saçılmasının bütün nicel içeriğini yeni hiçbir parametre olmadan üretir.** Fotoelektrik, çarpımı eğimden sabitler (G-1); Compton, aynı çarpımın $m_ec$'ye bölümünü bağımsız bir olgu ailesinde, bağımsız bir enerji ölçeğinde (eV'lik sökme işleri ↔ keV'lik X-ışınları) ve bağımsız bir gözlenebilirde (enerji doğrusu ↔ aralık açılması) sınar. İki aile tek çarpım üzerinde kenetlenir; M-10'un bağımsız mekanik $\tau$ tahminiyle aradaki 1,6 katlık pay, iki ailede aynı boyda görünür — bu da payın rastgele değil, $\tau$'nun tayinindeki tek bir belirsizlikten geldiğini söyler.

Sınırın dürüst kaydı: bu kenetlenme bir **iç tutarlılık kilididir**, bağımsız iki sabitleme değildir — her iki olgu da aynı $h$'yi kullanır; teorinin katkısı, $h$'nin arkasına ölçülebilir iki mekanik büyüklük ($\delta$, $\tau$) koyması ve "foton"un yerine, ışığın kendisinde değil **etkileşimde** yaşayan pencere alışverişini geçirmesidir. $\delta$ ile $\tau$'nun **ayrı ayrı** tespiti gerçekleştiğinde (ayrıştırma programı: 9.2.6, 7.4), kilit bağımsız bir öngörüye dönüşür: o gün $\lambda_C$, fotoelektrikten hiç veri almadan hesaplanabilir olacaktır.

## 9.4.8 Açık Kalemler

Mekanizma iki olguda da kuruludur; aşağıdakiler mekanizma boşluğu değil, **hesap kalemleridir** (tümü 7.4 envanterine bağlanır):

i. **Net momentum aktarımının ilk-ilkeler türetimi:** pencere başına teslim edilen net momentumun ölçülen $E_w/c$ değerine eşitliği burada 2.2.1'in ölçüm teslimi üzerinden **girdi** alınmıştır; $\eta$-çarpışma muhasebesinin momentum ayağından (geri seken mermilerin götürdüğü pay dahil) türetilmesi açıktır.
ii. **Klein–Nishina genliği:** saçılma şiddetinin açı ve enerjiyle dağılımının (toplam kesitin enerjiyle düşüşü dahil) katar–girdap temas mekaniğinden türetimi.
iii. **Bağlı-elektron Compton profili:** kaymış çizginin genişliğinin, hedef elektronun girdap-içi hız dağılımından türetimi (standart fizikte "Compton profili" ölçüm alanı — teoriye hazır bir veri madeni).
iv. **Yüksek-enerji kinematiği:** $h\nu \gtrsim m_ec^2$ ölçeğinde (γ rejimi, Compton kenarı) elektron kinematiğinin Ek A'nın hız merdiveninden teori-içi türetimi.
v. **Ultrakısa atım rejimi:** attosaniye sökülme-zamanı ölçümleri (Schultze ve ark., 2010), kopma penceresi mekaniğinin atımlı-kaynak rejimindeki davranışına keskin sınır koyar; pencere modelinin bu rejime genellenmesi ve sınırın hesaplanması açıktır.
vi. **Pencere yenilenmesi:** bir saçılma olayını sonlandıran ve ardışık pencereleri birbirinden ayrıştıran mekaniğin (geri tepme sonrası girdabın yeniden kilitlenme süreci) türetimi; olay kesikliliğinin alıcı tarafındaki tam mekanik temeli budur.

---

**Bölüm özeti:** Fotoelektrik etki ve Compton saçılması, "kütlesiz foton"un iki tarihsel kalesi olarak bilinir; bu bölümde ikisi de yalnız katar, aralık ve alıcı penceresi kullanılarak sayısal doğrulamadan geçirilmiştir. Fotoelektrik ayakta dört gözlemsel davranışın dördü mekanikten çıkar; Compton ayakta kayma formülü pencere-başına Newtonyen korunumdan, mekanizması geri tepme Doppler'inden gelir; kaymamış çizgi ve koinsidans deneyleri pencere modelinin doğal çıktılarıdır; ve iki olgu ailesi tek $\delta\tau$ çarpımı üzerinde kenetlenir. Kuantum ışıkta değil etkileşimde yaşar: ışık kesintisiz bir katardır, kesiklilik alıcı penceresinin ısırığıdır. Serbest kalan iki bileşenin ($\delta$, $\tau$) ayrıştırılması, kilidi bağımsız öngörüye çevirecek anahtardır (7.4).
