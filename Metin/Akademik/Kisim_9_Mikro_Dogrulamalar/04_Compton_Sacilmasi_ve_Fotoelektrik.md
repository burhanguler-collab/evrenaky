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

$$\Phi + E_{ke} = N\cdot\eta\cdot\tfrac12 m_z\!\left(c_0^2 + k_a v_{cev}^2\right), \qquad N = \nu\tau \;\Longrightarrow\; E_{ke} = (\delta\tau)\,\nu - \Phi$$

| Sınav | Teorinin sözü | Gözlem | Sonuç |
|---|---|---|---|
| G-1 doğrusallık | $E_{ke}$, $\nu$ ile doğrusal; eğim $=\delta\tau$, malzemeden bağımsız (kopma penceresi $\tau$ evrensel) | Millikan doğrusu; eğim $=h$ | ✅ yapı; çarpım $\delta\tau = h$ **gözlemle sabitlenir** [S] |
| G-2 gecikme | birikim penceresi $N\approx7{,}5\times10^3$ vuruş → morötesi ritminde $\approx10$ ps | $\lesssim3$ ns | ✅ üç mertebe payla |
| G-3a eşik | eşik-altı ritimde vuruşlar sönüm süresinden seyrek; enerji birikmez | keskin eşik | ✅ |
| G-3b şiddet | şiddet = paralel katar sayısı; tek elektron tek katarla etkileşir → $E_{ke}$'ye girmez, yalnız sökülen elektron **sayısını** artırır | $E_{ke}$ şiddetten bağımsız; doyma akımı ∝ şiddet | ✅ iki yüzüyle birden |
| çapraz kontrol | $h = 4\tau m_z^2c^2/m_e$ özdeşliği $\tau = h/\delta \approx 7{,}7$ ps verir; birikim yolu ($N/\nu$) **aynı sayıyı** verir | — | ⚠ Bağımsız sağlama **değildir**: iki yol cebirsel olarak aynı bağıntıdır ($N/\nu \equiv h/\delta$). $\tau$'nun $h$'ı kullanmayan tayini açık kalemdir (9.2.2) |

Fotoelektrik ayağının doğrulama bilançosu budur: dört gözlemsel davranışın dördü mekanikten çıkar; ödenen bedel, $\delta$ ve $\tau$'nun ayrı ayrı değil yalnız **çarpım** olarak sabitlenmesidir (rozet [S]; Ek C).

## 9.4.3 Compton Saçılması I: Korunum Katmanı

Compton olayı için yeni hiçbir kavram icat edilmez; türetim üç girdiden yürür ve ışık tarafında katar ile aralıktan fazlasını kullanmaz:

1. **Işık tarafı — katar:** aralık $\lambda$, ritim $\nu = c_0/\lambda$. Şiddet, paralel katar sayısıdır ve tek elektron tek katarla etkileştiği için (D-21, M-10) tek olayın muhasebesine hiç girmez.
2. **Alıcı tarafı — pencere:** elektron-girdabın etkileşim penceresi $\tau$ — fotoelektrik mekanizmayı taşıyan **kopma penceresinin** kendisi (M-10/M-11). Bir pencere boyunca elektron $N = \nu\tau$ vuruş alır; teslim edilen enerji, M-11'in birikim adımından, $E_w = (\delta\tau)\,\nu = h\nu$'dür. 17,4 keV'lik X-ışını ritminde bu, pencere başına $N \approx 3{,}3\times10^7$ vuruş demektir.
3. **Pencere momentumu:** bir pencerede teslim edilen net momentum, ölçülen ışınım basıncının verdiği $p_w = E_w/c_0$ değeridir; 2.2.1'in açıkça teslim ettiği üzere bu ölçümde hesap çelişkisi yoktur — ayrışma taşıyıcının ontolojisindedir. *(Bu değerin $\eta$-çarpışma muhasebesinden ilk-ilkeler türetimi açık kalemdir — 9.4.8/i.)*

Kesikliliğin adresi 9.2.1'de kurulmuştu: "foton", cisim değil pencerelik alışveriştir; kuantum ışıkta değil etkileşimde yaşar, ışığın kendisi kesintisiz katardır. Compton muhasebesine bunun taşıdığı tek içerik şudur: tek olayın alışverişi $E_w=h\nu$, $p_w=h\nu/c_0$'dir — gerisi kinematiktir.

Bu üç girdiyle Compton olayı saf **Newtonyen çarpışma kinematiğidir**: duran bir elektron-girdap, bir pencerede katardan $E_w = h\nu$, $p_w = h\nu/c_0$ alır; yönü değişen katar dilimi $\theta$ açısıyla, elektron $q$ momentumuyla ayrılır. X-ışını rejiminde ($h\nu \ll m_ec^2$ enerji ölçeği) elektronun geri tepmesi yavaştır ve görelilik gerekmez:

$$\text{momentum: } q^2 = \left(\frac{h\nu}{c}\right)^2 + \left(\frac{h\nu'}{c}\right)^2 - 2\frac{h\nu}{c}\frac{h\nu'}{c}\cos\theta, \qquad \text{enerji: } h\nu - h\nu' = \frac{q^2}{2m_e}$$

İki denklem birleştirilip $\lambda = c_0/\nu$ (Zerre aralığı) diline çevrildiğinde, önder mertebede:

$$\boxed{\Delta\lambda = \frac{\delta\tau}{m_e c_0}\left(1-\cos\theta\right) = \lambda_C\left(1-\cos\theta\right), \qquad \lambda_C \equiv \frac{\delta\tau}{m_e c_0} = \frac{4\tau m_z^2 c_0}{m_e^2}}$$

Compton kayması, teorinin dilinde **saçılan katarın Zerre aralığının açılmasıdır**: pencere alışverişinin bir kısmı geri tepen girdaba gittiği için yönü değişen katar diliminin ritmi düşer, ardışık mermiler arasındaki mesafe açılır. G-4'ün iki tuhaflığı da burada kendiliğinden çözülür: **(a)** formülde $\lambda$ yoktur ve $\nu$-bağımlılığı $\lambda\nu = c_0$ ile düşer — kayma yalnız açıya ve hedef kütlesine bağlıdır; **(b)** pencere teslimatı katar-içi ritimle ölçeklenir, paralel katar sayısıyla değil — kayma şiddetten de bağımsızdır. İkisi de kinematiğin zorunlu sonucudur, ek varsayım değil.

## 9.4.4 Compton Saçılması II: Mekanizma Katmanı (Doppler Okuma)

Korunum katmanı sonucu verir ama süreci anlatmaz; teorinin temas-mekanik yükümlülüğü süreçtir. Süreç şudur: katar, elektron-girdapla etkileşim penceresi boyunca boğuşur; girdap pencere boyunca geri teper; yönü değişen katar dilimi, **geri tepmekte olan bir kaynağın üzerinden yeniden yayılır**. Geri çekilen kaynaktan çıkan katarın ritmi Kısım 6.1'in Doppler mekaniğiyle düşer — aralık açılır. Alış ve yeniden-yayım olmak üzere iki Doppler adımı üst üste konduğunda, geri tepme momentumu $h\nu/c_0$ mertebesinde olan bir elektron için tam olarak 9.4.3'ün formülü geri gelir.

Bu okuma teorinin icadı değildir; Schrödinger, Compton olayının kayma formülünün geri tepen elektrondan **çift Doppler** olarak türetilebildiğini 1927'de göstermiştir (Schrödinger, 1927). Standart fizikte bu bir "alternatif hesap yolu" olarak kalır; Evrenakı Teorisi'nde ise mekanizmanın kendisidir: ortada kütlesiz bir kuantum yoktur, geri tepen bir girdap ve ritmi Doppler ile açılan somut bir mermi katarı vardır. Aynı Doppler makinesi kitapta kızıla kaymayı da taşıdığından (Kısım 6.1–6.2), Compton kayması ile kozmolojik kızıla kayma teoride **akraba mekanizmalar** hâline gelir: ikisi de katar ritminin mekanik yeniden ayarlanmasıdır; biri geri tepen hedefte, öteki yol boyu ortamda.

## 9.4.5 Sayısal Karşılaştırma

**(a) Compton dalga boyu — yeni parametre eklenmeden, ama özdeş olarak.** $\lambda_C = 4\tau m_z^2c/m_e^2$ zincirine fotoelektrik eğimin sabitlediği $\tau = h/\delta \approx 7{,}7$ ps, Postülat 4'ün $m_z = 1{,}47\times10^{-35}$ kg değeri ve $m_e$ konduğunda:

$$\lambda_C = \frac{4\times(7{,}8\times10^{-12})\times(1{,}47\times10^{-35})^2\times(3{,}0\times10^8)}{(9{,}11\times10^{-31})^2} \approx 2{,}44\times10^{-12}\ \text{m}$$

Ölçüm: $\lambda_C = 2{,}4263$ pm (Tiesinga ve ark., 2021). **Uyum, $h=\delta\tau$ özdeşleşmesinin cebirsel sonucudur — bağımsız bir tayin değildir.** $\tau$'nun kendisi $h/\delta$'dan geldiği için bu zincir $\lambda_C=h/m_ec$ standart bağıntısına özdeş olarak indirgenir; sayısal uyum bu yüzden zorunludur, sınayıcı değildir. Bölümün bağımsız içeriği burada değil, **mekanizmadadır**: kaymanın pencere-başına Newtonyen korunumdan ve geri tepme Doppler'inden çıkması (9.4.4). $\tau$'nun $h$'ı kullanmayan bir tayini elde edilirse bu satır sınayıcı bir öngörüye dönüşür; o tayin bugün açık kalemdir (9.2.2).

**(b) Açı taraması.** $\Delta\lambda = \lambda_C(1-\cos\theta)$:

| $\theta$ | 45° | 90° | 135° | 180° |
|---|---|---|---|---|
| $\Delta\lambda$ (pm) | 0,71 | 2,43 | 4,14 | 4,85 |

Compton'ın özgün ölçümü (molibden K$\alpha$, $\lambda=71{,}1$ pm, $\theta=90°$): gözlenen kayma $\approx2{,}4$ pm ↔ öngörü 2,43 pm — yüzde birkaç içinde (Compton, 1923). Modern hassas ölçümler formülün açı bağımlılığını bütün taramada doğrular.

**(c) Kaymamış çizgi (G-5).** Elektron atoma sıkı bağlıysa pencere alışverişinin geri tepen hedefi tek elektron değil bütün atomdur; formülde $m_e \to M_{atom}$ geçer. Karbon için $m_e/M_{atom} \approx 4{,}6\times10^{-5}$, yani kayma $\sim1{,}1\times10^{-16}$ m — ölçülemez: çizgi "kaymamış" görünür. Bu, Ek M-10'daki $4m/M$ mantığının aynısıdır; kaymış/kaymamış çizgi ikilisi, tek formülün iki hedef-kütle rejimidir. Ağır elementlerde (sıkı bağlı elektron kesri büyük) kaymamış tepenin göreli güçlenmesi de aynı mantığın nitel sonucudur.

**(d) Compton kenarı — gündelik doğrulama.** $\theta=180°$'de elektrona aktarılan enerji maksimumdur; 662 keV'lik Cs-137 çizgisi için kinematik kenar 477 keV'dir ve her sintilasyon laboratuvarında her gün ölçülür. Bu enerji ölçeği ($h\nu \sim m_ec^2$) 9.4.3'ün Newtonyen rejiminin dışındadır; kenarın konumu ölçülen $E$–$p$ korunumundan izlenir, elektronun bu hız rejimindeki kinematiğinin teori-içi (Ek A hız merdiveni üzerinden) türetimi açık kalemdir (9.4.8/iv).

## 9.4.6 Tarihsel Sınamalarla Yüzleşme: Koinsidans Deneyleri

Fotoelektrik ayağın üç klasik sınavıyla yüzleşme 2.2.3'te yapılmıştı; Compton ayağının kendi tarihsel sınavı daha az bilinir ama daha serttir. 1924'te Bohr–Kramers–Slater (BKS) kuramı, enerji-momentum korunumunun tek tek olaylarda değil yalnız **istatistiksel ortalamada** geçerli olduğunu öne sürerek Compton olayını sürekli-alan diliyle kurtarmayı denedi. İki deney bu kapıyı kapattı: Bothe & Geiger (1925) saçılan ışınla geri tepen elektronun **aynı anda** (koinsidans içinde) çıktığını; Compton & Simon (1925) sis odasında yön korelasyonunun olay-bazında korunum denklemlerine uyduğunu gösterdi. Korunum, ortalamada değil **her tek olayda** geçerlidir.

Evrenakı Teorisi'nin bu sınava cevabı pencere mekaniğidir: geri tepen elektron ile yönü değişen katar dilimi, **aynı etkileşim penceresinin iki çıktısıdır** — ayrı ayrı üretilmezler, tek temas olayının iki yüzüdürler. Pencere süresi ($\tau \approx 8$ ps), koinsidans deneylerinin zaman çözünürlüğünün (ns–µs) çok altındadır; iki çıktı deney gözünde kesin eşzamanlıdır. Ve korunum her pencerede **mekanik olarak** — temasla — sağlanır, ortalamada değil: istatistiksel BKS'yi öldüren ölçüm, pencere modelinin doğal çıktısıdır. Teori burada standart kuantum mekaniğiyle aynı safta, yarı-klasik istatistiksel modellerin karşısındadır — ayrışma noktası korunumda değil, **kesikliliğin adresindedir**: standart model kesikliliği ışığın kendisine yazar ("foton"), teori alıcının penceresine yazar; ışık tarafında yalnız katar ve aralık kalır.

### 9.4.6.1 Ölçülen ile Yorumlanan: Envanterin İki Katmanı

Bu bölümün eleştirisi hiçbir aşamada deneylere yönelmez. Millikan'ın doğrusu, Compton'ın kayması, Bothe–Geiger koinsidansı gerçektir; teori altı gözlemin altısına da hesap vermek zorundadır ve yukarıdaki tablolar bu hesabı verir. Tartışma, ölçümlerin üzerine eklenen ontolojik cümlelerdedir (yöntem: 9.9.2; hata kodları: 9.9.3):

| Ölçülen (tartışma dışı) | Eklenen yorum | Eklemenin statüsü |
|---|---|---|
| $E_{ke}$ ile $\nu$ arasındaki doğru; eğim evrensel ve $h$'ye eşit (G-1) | "Demek ki ışık $h\nu$'lük bölünmez enerji paketleri hâlinde gelir" | **Adres kayması (Y-2).** Eğim, alışverişin pencere başına büyüklüğünü verir; alışverişin kesikliliği alıcının penceresinden de doğar. Eğimi ölçen Millikan'ın kendisi tanecik yorumunu "tamamen savunulamaz" bulmuştu (9.10.10) |
| Eşik-altı frekansta emisyon yok; eşik üstünde akım şiddetle artar (G-3) | "Tek foton tek elektron söker" | **Hiç sınanmadı.** Bu önerme, saniyede $10^{12}$–$10^{15}$ mermilik akılarla çalışan düzeneklerde kuruldu ve tekil olay hiç gözlenmedi; zayıflatılmış klasik ışıkla sınanması ilkece de mümkün değildi (9.10.6/a, 9.10.8) |
| Saçılan çizgi açıya bağlı kayar; kayma $\lambda$ ve şiddetten bağımsız (G-4) | "Foton, elektronla bilardo topu gibi çarpıştı" | **Hesap ile anlatı ayrışması** — aşağıda 9.4.6.2 |
| Saçılan ışın ile geri tepen elektron koinsidans içinde çıkar (G-6) | "Tekil, yerleşik bir kuantum tekil bir elektrona çarptı" | **Nesneleştirme (Y-1).** Ölçülen şey iki eşikli sayacın zaman eşleşmesidir; korunumun her olayda geçerli olduğunu gösterir, çarpanın yerleşik bir cisim olduğunu değil. Teori korunumu pencerede mekanik olarak sağlar (9.4.6) |

### 9.4.6.2 Hesap ile Anlatının Ayrışması: Düzlem Dalga mı, Bilardo Topu mu?

Compton olayının "parçacık kanıtı" sayılan yanı, standart çatının kendi formalizminin taşıyamadığı yandır ve bu, envanterdeki en sert yorum sorunudur.

Saçılma kesitinin kuantum elektrodinamik hesabı **momentum özdurumlarıyla** — yani düzlem dalgalarla — yapılır. Düzlem dalga bütün uzayı kaplar, normalize edilemez ve hiçbir yerde değildir: $\langle 1_\omega|1_\omega\rangle=\delta(0)$ (9.10.4). Kayma formülünün içindeki $h\nu/c_0$ momentumunun sahibi, tanımı gereği **yerleşik olmayan** bir durumdur. Buna karşılık olayın ders kitabı anlatısı, belirli bir noktada gerçekleşen yerel bir çarpışmadır — iki bilardo topunun teması.

Yani standart fizik, aynı olayın **hesabını yerleşmemiş bir nesneyle, anlatısını yerleşik bir nesneyle** yapmaktadır. Bu iki resim tek nesnede birleştirilemez: keskin momentum keskin yayılmışlık gerektirir (9.10.3), yerleşiklik ise kütlesiz spin-1 için zaten tanımsızdır (9.10.5). Anlatının ikna gücü, formalizmin izin vermediği bir görselleştirmeden gelmektedir.

Deney tarafı da aynı yöne bakar. 9.4.3'ün kendi sayısıyla, 17,4 keV'lik X-ışını ritminde tek bir pencerede elektron $N\approx3{,}3\times10^{7}$ vuruş alır; Compton'ın özgün ölçümü iyonizasyon odasıyla, koinsidans deneyleri ise eşik aşımlarının zaman eşleşmesiyle yapılmıştır (aygıt denetimi: 9.10.7). Hiçbir aşamada tekil bir mermi tespit edilmemiştir.

**Teorinin bu arenadaki üstünlüğü, tam da bu ayrışmanın olmamasıdır.** Teoride hesap ile anlatı aynı nesneyi konu alır: yerleşik, kütleli, sonlu boyutlu bir katar dilimi pencere boyunca girdapla boğuşur; korunum her pencerede temasla sağlanır; kayma, geri tepen kaynaktan yeniden yayılan katarın ritminin düşmesidir (9.4.4). Görselleştirme ile formalizm arasında çeviri kaybı yoktur — çünkü ikisi aynı mekaniktir.

## 9.4.7 Kenetlenme: Tek Çarpım, İki Olgu Ailesi

Bölümün bilançosu tek cümlede toplanır: **fotoelektrik veriden sabitlenen $\delta\tau$ çarpımı, Compton saçılmasının bütün nicel içeriğini yeni hiçbir parametre olmadan üretir.** Fotoelektrik, çarpımı eğimden sabitler (G-1); Compton, aynı çarpımın $m_ec$'ye bölümünü bağımsız bir olgu ailesinde, bağımsız bir enerji ölçeğinde (eV'lik sökme işleri ↔ keV'lik X-ışınları) ve bağımsız bir gözlenebilirde (enerji doğrusu ↔ aralık açılması) sınar. İki aile tek çarpım üzerinde kenetlenir. **Kenetlenmenin sınırı da aynı cümlede yazılmalıdır:** $\delta\tau$ çarpımı fotoelektrik eğiminden, yani ölçülen $h$'tan sabitlendiği için Compton kayması bu çarpımın *sınayıcı* bir öngörüsü değildir; sınanan şey **mekanizmadır** (pencere-başına korunum + geri tepme Doppler'i), çarpımın değeri değil. $\tau$'nun $h$'ı kullanmayan bağımsız bir tayini elde edildiğinde bu satır gerçek bir nicel sınava dönüşür (açık kalem: 9.2.6/ii).

Sınırın dürüst kaydı: bu kenetlenme bir **iç tutarlılık kilididir**, bağımsız iki sabitleme değildir — her iki olgu da aynı $h$'yi kullanır; teorinin katkısı, $h$'nin arkasına ölçülebilir iki mekanik büyüklük ($\delta$, $\tau$) koyması ve "foton"un yerine, ışığın kendisinde değil **etkileşimde** yaşayan pencere alışverişini geçirmesidir. $\delta$ ile $\tau$'nun **ayrı ayrı** tespiti gerçekleştiğinde (ayrıştırma programı: 9.2.6, 7.4), kilit bağımsız bir öngörüye dönüşür: o gün $\lambda_C$, fotoelektrikten hiç veri almadan hesaplanabilir olacaktır.

## 9.4.8 Açık Kalemler

Mekanizma iki olguda da kuruludur; aşağıdakiler mekanizma boşluğu değil, **hesap kalemleridir** (tümü 7.4 envanterine (md. 19) bağlanır):

i. **Net momentum aktarımının ilk-ilkeler türetimi:** pencere başına teslim edilen net momentumun ölçülen $E_w/c_0$ değerine eşitliği burada 2.2.1'in ölçüm teslimi üzerinden **girdi** alınmıştır; $\eta$-çarpışma muhasebesinin momentum ayağından (geri seken mermilerin götürdüğü pay dahil) türetilmesi açıktır.
ii. **Klein–Nishina genliği:** saçılma şiddetinin açı ve enerjiyle dağılımının (toplam kesitin enerjiyle düşüşü dahil) katar–girdap temas mekaniğinden türetimi.
iii. **Bağlı-elektron Compton profili:** kaymış çizginin genişliğinin, hedef elektronun girdap-içi hız dağılımından türetimi (standart fizikte "Compton profili" ölçüm alanı — teoriye hazır bir veri madeni).
iv. **Yüksek-enerji kinematiği:** $h\nu \gtrsim m_ec^2$ ölçeğinde (γ rejimi, Compton kenarı) elektron kinematiğinin Ek A'nın hız merdiveninden teori-içi türetimi.
v. **Ultrakısa atım rejimi:** attosaniye sökülme-zamanı ölçümleri (Schultze ve ark., 2010), kopma penceresi mekaniğinin atımlı-kaynak rejimindeki davranışına keskin sınır koyar; pencere modelinin bu rejime genellenmesi ve sınırın hesaplanması açıktır.
vi. **Pencere yenilenmesi:** bir saçılma olayını sonlandıran ve ardışık pencereleri birbirinden ayrıştıran mekaniğin (geri tepme sonrası girdabın yeniden kilitlenme süreci) türetimi; olay kesikliliğinin alıcı tarafındaki tam mekanik temeli budur.

---

**Bölüm özeti:** Fotoelektrik etki ve Compton saçılması, "kütlesiz foton"un iki tarihsel kalesi olarak bilinir; bu bölümde ikisi de yalnız katar, aralık ve alıcı penceresi kullanılarak sayısal doğrulamadan geçirilmiştir. Deneyler tartışmaya açılmamış, yalnızca ölçümlerin üzerine eklenen yorum katmanı ayrıştırılmıştır (9.4.6.1): "tek foton tek elektron söker" önermesi hiç sınanmamış, "bilardo topu çarpışması" anlatısı ise kuramın kendi hesabıyla çelişmiştir — kesit düzlem dalgayla hesaplanıp olay yerel temas olarak anlatılmaktadır (9.4.6.2), oysa teoride hesap ile anlatı aynı yerleşik nesneyi konu alır. Fotoelektrik ayakta dört gözlemsel davranışın dördü mekanikten çıkar; Compton ayakta kayma formülü pencere-başına Newtonyen korunumdan, mekanizması geri tepme Doppler'inden gelir; kaymamış çizgi ve koinsidans deneyleri pencere modelinin doğal çıktılarıdır; ve iki olgu ailesi tek $\delta\tau$ çarpımı üzerinde kenetlenir. Kuantum ışıkta değil etkileşimde yaşar: ışık kesintisiz bir katardır, kesiklilik alıcı penceresinin ısırığıdır. Serbest kalan iki bileşenin ($\delta$, $\tau$) ayrıştırılması, kilidi bağımsız öngörüye çevirecek anahtardır (7.4).
