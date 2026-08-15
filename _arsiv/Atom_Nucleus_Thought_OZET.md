# ÖZET — "Atom Nucleus Thought / Atom Geometrisi" (Burhan Güler)

> **Bu dosya `Atom Nucleus Thought Ortak Dosya.pdf` (105 sayfa, 16,9 MB) için hazırlanmış çalışma özetidir.**
> Amacı: PDF'i her seferinde baştan okumak zorunda kalmamak. Sayfa numaraları **PDF sayfası**dır (kitabın kendi sayfa numarası ~4 eksiktir).
> Hazırlandı: 10 Ağustos 2026.
> **Metin çıkarma:** `python -c "import fitz; ..."` (pymupdf kurulu). `pdftoppm` yok, Read aracı PDF'i doğrudan render edemiyor — metni çıkarıp okumak gerekiyor.

---

## 0. KİTABIN KİMLİĞİ

- **Seri:** "Mai tezi"nin **ilk** kitabı. Yazar, aslında en son yayınlanması gerektiğini ama Ether açıklanmadan yalnız *geometri* anlatılabildiği için başa aldığını söylüyor (s.8).
- **Son kitap planı:** *"Atomların İşleyişi"* — Ether, deneyler ve diğer bilgiler açıklandıktan sonra yazılacak (dipnot, s.7).

> ### ⚠️ EN ÖNEMLİ OKUMA KURALI — KRONOLOJİ
> **Bu kitap Evrenakı'dan ÖNCE yazılmıştır.** Kitabın kendi dipnotu (s.7) bunu açıkça söyler:
> *"Ayrıntıların açıklanabilmesi ancak Ether'in biliniyor olmasına bağlı olduğundan bu kitapta açıklama yapılabilmesi mümkün görülmemiştir. En son kitap 'Atomların İşleyişi' adıyla, Ether, deneyler ve diğer bilgiler açıklandıktan sonra yazılacak."*
>
> **Sonuç:** Kitabın "reddettim" dediği şeyler, olguların kendisi değil **kaynağı gösterilmemiş yer tutucularıdır.** Kitap mekanizmayı reddetmiyor — **erteliyor**, ve Ether bilindiğinde açıklanacağını söylüyor. **Evrenakı Teorisi, o ertelenmiş açıklamanın kendisidir.**
>
> Bu kuralı uygulamadan kitapla Evrenakı arasında "çelişki" aramak yanlış sonuç verir. İlk okumamda tam bu hatayı yaptım (bkz. §7.2).
- **Dayanak:** 13 yıllık deneysel çalışma; Descartes (uzay boş değil) + Newton (ışık tanecik). Ether kabul edilir, foton reddedilir.
- **İthaf:** kızı Şeyma Nur'un anısına (s.2).
- **Akademik destek:** Prof. Dr. Rıza Demirbilek, Prof. Dr. Ethem Derman.

**Önsözdeki üç itiraz** (s.7–8): (1) foton soyut ve tutarsız — 250 Å'lık bir paket kilometrelerce radyo dalgasını nasıl taşır? (2) uzay-zaman soyut. (3) **nükleer kuvvet kanıtsız** — tek "kanıtı" çok protonlu çekirdeklerin var olması.

---

## 1. ÇEKİRDEK TEZ (tek paragraf)

> **2, 8, 18, 32 sayıları elektronların değil PROTONLARIN sayılarıdır.** Çekirdek, protonların ve nötronların **kare katmanlar** hâlinde dizilmesiyle kurulur; her kare katman kendi etrafında bir elektron yörünge katmanı doğurur ve o katmandaki elektron sayısı katmandaki proton sayısına **birebir eşittir**. Orkestra şefi protondur; elektron dizilimi çekirdek geometrisinin gölgesidir.

**Mantık zinciri (s.9–13):**
1. $2n^2$ ve $n^2/2$ bağıntılarının ikisinde de **kare** var → kare bir *alan* ifadesidir → geometri.
2. Aynı yükler birbirini iter, iki proton yan yana gelemez → **aralarına nötron şart**.
3. Mıknatıs–demir analojisi: proton = mıknatıs (tüm yüzeyi tek kutup), nötron = demir. Aynı kutuplu iki mıknatıs, aralarına demir konunca güçlü bağ kurar.
4. Zincir dizilim üç nükleondan sonra esner ve bozulur → **kare** dizilim kararlıdır.
5. Helyum-4 = 2 proton + 2 nötron, **kare** → ilk kararlı çekirdek, tüm elementlerin temeli.

---

## 2. L-KATMAN SİSTEMİ (kitabın omurgası)

**L = "levha"**, ardından gelen sayı = barındırdığı **proton** sayısı.

| Katman | Izgara | Konum sayısı | Proton | Nötron |
|---|---|---|---|---|
| **L2** | 2×2 | 4 | 2 | 2 |
| **L8** | 4×4 | 16 | 8 | 8 |
| **L18** | 6×6 | 36 | 18 | 18 |
| **L32** | 8×8 | 64 | 32 | 32 |

*(Kitap ızgara boyutlarını açıkça yazmıyor; yukarıdaki tablo metindeki "en dış proton-nötron dizisi çıkarılırsa bir küçük katman kalır" kuralından çıkarılmıştır — $k$'ıncı katman $(2k)^2$ konumlu, $2k^2$ protonlu, yani **$2n^2$ tam olarak buradan geliyor**.)*

**Dizilim kuralları (s.16–17):**
- Katmanlar **zincir yapamaz** — yalnız **üst üste** gelir.
- Birleşmede **her protona bir nötron** karşılık gelmelidir; aynı öge asla yan yana gelmez.
- Bir katman 90° döndürülünce tüm proton/nötron yerleri takas olur → iki aynı katman ancak biri döndürülerek birleşebilir.
- Katmanın bir köşesinden diğerine çekilen çizgilerden biri tamamen proton, diğeri tamamen nötrondur.
- Her katman, bir büyüğünün en dış sırası çıkarılmış hâlidir → iç içe geçebilirler.
- L2 daima L8'in **merkezine** oturur.

**Soy gaz çekirdekleri (s.13–15):**

| Soy gaz | Katman dizisi | Toplam |
|---|---|---|
| Helyum | L2 | 2 |
| Neon | L2·L8 | 10 |
| Argon | L2·L8·L8 | 18 |
| Kripton | L2·L8·L18·L8 | 36 |
| Ksenon | L2·L8·L18·L18·L8 | 54 |
| Radon | L2·L8·L18·L32·L18·L8 | **86** |
| Oganesson | L2·L8·L18·L32·L32·L18·L8 | 118 |

⚠️ **Dizgi hatası kaydı:** s.15'te radon için toplam "96" yazılmış; doğrusu **86**'dır (2+8+18+32+18+8 = 86) ve kitabın kendisi bir satır sonra "radon atom numarası 86" diyor. Kullanırken düzeltilmeli.

**Kural:** hidrojen hariç her element L2 ile başlar; helyumdan sonraki **her soy gaz L8 ile biter** (son katman tam dolu = kimyasal kararlılık).

---

## 3. YÖRÜNGELERİN OLUŞUMU (s.19–20) — "yörünge şekillenmeleri" bölümü

> ⚠️ **İlk özette iki hatalı okumam vardı; düzeltildi (10 Ağu 2026).** Yanlış okumuşum: *"katmanlar üst üste binince ekvator düzlemleri paralel olur → atom disk gibidir"*. Doğrusu aşağıda.

- Her yörünge, **kendi L katmanının belirlediği düzlemdedir.** **L katmanları aynı düzlemde değildir** — alt alta dizilirler. Dolayısıyla **yörüngeler de eşdüzlemli değildir.** Atom düzlemsel/disk değil; uçlarda küçük ortada büyük katmanlardan oluşan **üç boyutlu, simetrik bir yığındır** (radon: L2·L8·L18·L32·L18·L8 → çaplar küçük→büyük→küçük).
- Her kare katman **kendi** yörünge katmanını doğurur; elektron sayısı = o katmanın proton sayısı.
- **BİR KABUK = TEK YÖRÜNGE.** O katmanın bütün elektronları **aynı yörüngeyi paylaşır.** Yörüngede dolanmayı çekirdek belirler; elektronların **birbirinden uzak durmasını kendi negatif yükleri** belirler — aynı yolda olsalar bile karşılıklı itme mesafeyi eşit tutar.
  → **Dışlama ayrı bir ilke değildir:** proton sayısı *kaç* elektron olacağını, karşılıklı itme *nerede duracaklarını* söyler. (Çember üzerine hapsedilmiş $N$ yükün eşit aralıklı dizilmesi klasik denge sonucudur; düzlem seçilmez, katman tarafından dayatılır — bu, Thomson probleminin "büyük $N$ için düzlemsel halka kararsızdır" itirazını da karşılar.)
- **⭐ YÖRÜNGE ÇAPINI ELEKTRON SAYISI BELİRLER.** Aynı halkada daha çok elektron varsa eşit aralıkta durabilmek için halka daha geniş olmak zorundadır. **Sayısal sonuç:** $N=2k^2$ olduğundan $r\propto N \Rightarrow r\propto k^2$, yani $r_1:r_2:r_3:r_4 = 1:4:9:16$ — **Bohr'un $r_n=n^2a_0$ merdiveniyle birebir aynı oran, açısal momentum kuantumlamasına hiç başvurmadan.**
- **Kritik cümle (s.20):** *"Söz konusu orbitalleri tamamen kare katmanlar biçimlendirir, aynı zamanda **yörüngenin konumu ve çapı** kare katmanlar tarafından belirlenir."*
- Yazar orbital kavramını tersine çeviriyor: orbital önsel değildir; **yörüngeyi tayin eden elektronun kendisidir**, orbital yörüngelerden oluşur (s.60).

**Modern kimyaya mekanik itiraz (s.60):** $E=\tfrac12mv^2$ gereği enerji artarsa hız artar; hızı artan cisim yörüngede kalmak için **merkeze yaklaşmalıdır** (merkezkaç dengesi). Oysa modern bilim "enerji alan elektron uzaklaşır" diyor — makro mekaniğe ters.

---

## 4. MODELİN KABULLERİ (s.101–102, aynen özetlendi)

1. Proton pozitif yüklü ve **manyetizma kaynağı** gibi davranır (kanıt: pozitif manyetik moment).
2. **Nötron esas olarak NÖTRDÜR** — bu, modelin omurgası olan demir benzetmesinin ta kendisidir: demir manyetizma açısından nötrdür, mıknatıs onu çeker. Nötronun proton tarafından çekilmesi ve iki protonu bağlaması bu nötrlükten gelir.
   ⚠️ **Sık yapılan okuma hatası:** kitap ayrıca nötronun "zayıf ve negatif bir yük" taşıdığını söyler (kanıt: nötronun manyetik momenti; kuark yüklerinin fizik matematiğiyle işlenmesi). **Bu, protonun karşılığı/simetrik zıddı DEĞİLDİR** — nötronu "eksi yüklü parçacık" yapan bir iddia değil, **çok özel bir durumu** açıklayan ayrı bir kayıttır. Modelin işleyen kabulü nötrlüktür; negatif kalem, bağın *neden bu kadar güçlü* olduğunu açıklayan ikincil bir ayrıntıdır.
3. Çekirdekte proton/nötron **düzen** içinde dizilir; düzensizlik = radyoaktiflik.
4. **İki proton hiçbir surette birbirine dokunamaz.**
5. Nötronlar da birbirini iter, ama proton bağı bu itmeyi yenerse dokunabilirler.
6. Atomu proton ve elektron kurar; **nötron yapıştırıcıdır**.
7. **Simetri zorunludur** — simetriyi koruyamayan çekirdek radyoaktiftir.
8. **Çekirdek kendi çevresinde döner VE devinim (yalpalama) yapar** — yıldız analojisiyle.
9. **Yörüngeler ekvator düzlemindedir.**

## 5. MODELİN REDDETTİKLERİ (s.103)

> **§0'ın kronoloji kuralıyla okunmalı:** reddedilen şey **olgu değil, kaynağı gösterilmemiş standart açıklamadır.** Kitap "bu böyle olmuyor" demiyor; "bu şekilde açıklanamaz, açıklaması Ether bilinince gelecek" diyor.

1. Rastgele proton/nötron dizilimli **küresel çekirdek** — reddedilir. *(Bu gerçek bir ret; Evrenakı da katılır.)*
2. **Nükleer kuvvetin standart tanımı** — reddedilir: kanıtı yok, kaynağı yok, ve daha güçlü bağlanma enerjili çekirdeklerin radyoaktif çıkması tanımla çelişiyor. **Bağlanmanın kendisi reddedilmiyor** — kitap protonların *fiilen* bağlı olduğunu zaten kabul ediyor (kare katmanlar bağ üzerine kurulu). Reddedilen, bağı "kaynaksız bir kuvvet"e yıkmaktır.
3. **Bağlanma ve ayrılma enerjisi** — *nükleer enerjinin fonksiyonu olduğu için* reddedilir. Yani ret, enerjinin varlığına değil **kaynağınadır.**
4. Kütle kaybı — **"kütle kaybı değil, ağırlık kaybı"**. *(Kitap burada standart fiziğin kütle→enerji dönüşümü okumasına direniyor.)*
5. **Nükleer kabuk model ve sihirli sayılar** (2, 8, 20, 28, 50, 126) — s.92'de ayrıca çürütülüyor. Yazara göre 2/8/18/32'nin çekirdekle ilişkilendirilememesinin *sebebi* sihirli sayılardır. *(Bu da gerçek bir ret.)*

---

## 6. BÖLÜM HARİTASI (PDF sayfası — doğrudan atlamak için)

| PDF s. | Bölüm |
|---|---|
| 3–6 | İçindekiler |
| 7–8 | **ÖNSÖZ** — foton/uzay-zaman/nükleer kuvvet itirazları |
| 8–13 | **ATOMLARIN GEOMETRİSİ ÜZERİNE** — çekirdek tez, mıknatıs analojisi, kare geometrinin doğuşu |
| 14–17 | **KARE KATMANLARIN DİZİLİM GEOMETRİSİ** — birleşme kuralları |
| 18 | **SOY GAZLARDA TEMEL ÇEKİRDEK GEOMETRİSİ** |
| 19–20 | **YÖRÜNGE KATMANLARI** ⭐ |
| 20–46 | **ELEMENTLER** — 1'den 82'ye tek tek çekirdek geometrisi (referans malzeme) |
| ~62 | Bazı soy gazların alttan görünüşü |
| ~63 | Bazı elementlerin üstten görünüşü |
| 60–65 | **YÖRÜNGELER ÜZERİNE** ⭐ — orbital kavramının eleştirisi, merkezkaç itirazı |
| 65–67 | **ATOMİK YARIÇAPLAR** |
| 67–71 | **İYONLAŞMA ENERJİSİ** |
| 71–73 | KİMYASAL BAĞ ÜZERİNE |
| 73–74 | KARBON-14 (radyoaktivite) |
| 74–78 | **MIKNATIS DENEYLERİ** — Davranış 1–5 (modelin deneysel temeli) |
| 78–80 | **DÖNÜŞ VE KÜTLE İLİŞKİSİ** ⭐ |
| 80–81 | **YÖRÜNGELER EKVATOR DÜZLEMİNDEDİR** ⭐ |
| 81–101 | **SORULAR & CEVAPLAR** — bağlanma enerjisi, nötron manyetizması, nükleer patlama, nötron yükü, nükleer kabuk model, iyonlaşma |
| 92–101 | NÜKLEER KABUK MODEL TUTARLI MI? — sihirli sayıların çürütülmesi |
| 101–103 | **Kabuller ve Kabul Etmedikleri** ⭐ |
| 103–105 | Kaynakça |

---

## 7. EVRENAKI (KITAP3) İLE BAĞLAR — benim için asıl önemli kısım

### 7.1 ✅ Uyumlu / destekleyici
| Bu kitap | Evrenakı karşılığı |
|---|---|
| Çekirdek döner **ve devinim yapar** | Ö-5 (Anayasa M.30): devinim iç asimetri ister; nükleon bileşik olduğu için devinebilir ✔ |
| Yörüngeler **ekvator düzleminde** | Siklostrofik denge, "yörüngeler ekvator düzlemindedir" ✔ |
| "Kütle kaybı değil **ağırlık kaybı**" | Anayasa Madde 10: *"Ağırlık, kütlenin değil deplasman açığının özelliğidir"* — **birebir uyum** ✔ (ayrıntı: §7.2) |
| Nötron **nötrdür** (demir benzetmesi) | 2.1: nötron *"kendi içinde kilitli, net sızıntısı olmayan"* ✔ |
| Bağ vardır, ama nükleer kuvvet kaynaksızdır | Madde 29 bağın **kaynağını** veriyor: rampa kilitlenmesi ✔ |
| Foton reddi, ışık = tanecik | Anayasa Madde 3 ✔ |
| Ether/uzay boş değil | Madde 1–2 ✔ |
| Simetri zorunluluğu | 4B çift dönüş ve zarf simetrisi ✔ |
| Proton = kaynak, nötron = aracı | 2.1 yük notu (proton Kaynak, nötron kilitli) ✔ |

### 7.2 ✅ SANDIĞIM "ÇELİŞKİLER" ÇELİŞKİ DEĞİL — kitap soruyor, Evrenakı cevaplıyor

> **Düzeltme kaydı (10 Ağu 2026):** Bu bölümün ilk hâli üç "gerilim" listeliyordu. **Üçü de yanlış okumaydı** — kronoloji kuralı (§0) uygulanmamış ve iki kalem yanlış anlaşılmıştı. Doğru tablo:

| Konu | Kitabın söylediği | Evrenakı'nın kattığı | Durum |
|---|---|---|---|
| **Nötron** | Esas olarak **nötrdür** (demir benzetmesinin özü). Negatif kalem, protonun simetrik zıddı değil; **özel bir durumun** ayrı açıklaması | 2.1: *"kendi içinde kilitli, net sızıntısı olmayan"* = net sızıntı yok, yani nötr | ✅ **uyumlu** |
| **Nükleer kuvvet** | Kaynağı gösterilmemiş yer tutucu olduğu için reddedilir; **bağın kendisi kabul edilir** | Madde 29: **kaynağı verilir** — femtometre ölçeğinde rampaların iç içe geçmesi (temas rampa kilitlenmesi) | ✅ **kitap soruyor, Evrenakı cevaplıyor** |
| **Bağlanma enerjisi** | *Nükleer enerjinin fonksiyonu* olduğu için reddedilir — ret **kaynağa**, varlığa değil | Bağlanma artık **Evrenakı kaynaklı** bir kuvvet ve enerjidir (basınç/rampa kilitlenmesi) | ✅ **tamamlanma, çelişki değil** |
| **Kütle/ağırlık kaybı** | "Kütle kaybı değil, ağırlık kaybı" — standart kütle→enerji okumasına direniş | Madde 10: ağırlık, kütlenin değil **deplasman açığının** özelliğidir. Ve Evrenakı'da kütle ≡ deplasman | ✅ kitabın ayrımı Evrenakı'da **kesinleşiyor** |

**Dördüncü satırın §19/F2 ile ilişkisi — doğru okuma:**
F2 kararı ("kütle toplanabilir değil, bağlanma açığı var") kitapla çelişmiyor. Çünkü Evrenakı **kütle ≡ deplasman hacmi** özdeşliğini getiriyor; kitap bunu bilmiyordu. O özdeşlik konduğunda:
- Bağlanmada azalan şey **deplase edilen hacimdir**.
- Evrenakı bu azalmaya "kütle azalması" der (kütle=deplasman olduğu için).
- Kitap ise standart fiziğin "kütle enerjiye dönüştü" okumasını reddetmek için "kütle değil ağırlık" demişti.
- **İkisi aynı olguyu anlatıyor;** Evrenakı yalnız kitabın direndiği şeyi adlandırmayı mümkün kılan özdeşliği ekliyor.

**✅ YAZILDI (10 Ağu 2026):** Uzlaşma, Evrenakı Anayasası'nda **Madde 29'un altına "Seri içi uzlaşma hükmü — 'Atom Geometrisi' ile bağ"** olarak eklendi. Hüküm şunları kayda geçiriyor: (a) ilk kitabın reddi olguya değil **kaynağa** yönelikti ve kronoloji gereği başka türlü kurulamazdı; (b) o kitap bağın varlığını zaten kabul eder (kare katman geometrisi bağ üzerine kuruludur); (c) Madde 29 kaynağı verir — biri soruyu kurar, öteki cevaplar; (d) **kütle ≡ deplase edilen hacim** özdeşliği "kütle kaybı değil ağırlık kaybı" ile "kütle toplanabilir değildir"i uzlaştırır: standart fiziğin *kütle→enerji dönüşümü* okuması reddedilir, buna karşılık kompozit kütlesinin bileşen toplamının altında olması kabul edilir; (e) her iki metinde neyin kastedildiğinin açıkça yazılması kural hâline getirildi.

### 7.3 ⭐ Bu kitap TIKANDIĞIMIZ YERİN BİR AYAĞINI KAPATIYOR *(ilk özette bunu kaçırmışım)*
`01_Atom_Spektrumu_ve_Kesikli_Yapi.md` §10'da tıkandığımız yer iki parçalıydı: **(a) yarıçap merdiveninin biçimi** ($1/n^2$) ve **(b) mutlak ölçek** ($a_0$, dolayısıyla $\hbar$).

**(a) KAPANDI.** §3'teki "çapı elektron sayısı belirler" kuralı + katman geometrisinin $N=2k^2$'si → $r\propto k^2$. Yani $1/n^2$ merdiveninin biçimi **kapanma kuralı / açısal momentum kuantumlaması gerektirmeden** geliyor. §10.1–10.2'nin aradığı kural bu yolda **hiç gerekmiyor.**

**(b) AÇIK.** Mutlak ölçeği kitap da vermiyor — ve vermemesi yapısaldır: hem merkez çekimi hem karşılıklı itme $1/r^2$ gittiği için salt yük mekaniği **ölçekten bağımsızdır**, oran verir mutlak değer vermez. Bu, §10.6.2'nin teşhisiyle (teoride bağımsız uzunluk yok, $\hbar$ üretilemez) birebir aynı sonuca varıyor — **iki metin, iki ayrı yoldan aynı duvara çarpıyor.** Bu bir tesadüf değil; ölçek boşluğunun gerçek olduğunun bağımsız teyididir.

**Güncel tablo (01_Atom... §9.3'ün tablosu bununla değiştirilmeli):**
| Gözlem | Nereden | Durum |
|---|---|---|
| Kabuk sayıları 2, 8, 18, 32 | kare katman geometrisi ($2k^2$) | ✅ Atom Geometrisi |
| Dışlama / eşit aralık | karşılıklı yük itmesi, tek yörünge | ✅ Atom Geometrisi |
| Yarıçap oranları ($n^2$) | elektron sayısı → çap | ✅ Atom Geometrisi |
| $2n^2$'nin "2"si | kare ızgara geometrisi (**spin gerekmez**) | ✅ Atom Geometrisi |
| Rydberg–Ritz toplanabilirliği | geçiş = iki hâlin vurusu | ✅ Evrenakı |
| Harmoniğin yokluğu | durağan düzen + geçiş | ✅ Evrenakı |
| $1/r$ topografyası | kütle-itim $P=P_0-\alpha M/r$ | ✅ Evrenakı |
| **Mutlak ölçek ($a_0$, $\hbar$)** | — | ⬜ **tek kalan; parite kararı: ölçülen girdi** |

### 7.4 ⭐ Doğrudan kullanılabilir malzeme
1. **$2n^2$'nin geometrik türetimi:** $k$'ıncı kare katman $(2k)^2$ konumlu, $2k^2$ protonlu. Bu, `01_Atom...md` §5 Aday 3'ün (Pauli/vortex merger) yerine geçebilecek **çok daha somut** bir doluluk açıklamasıdır.
2. **Mıknatıs deneyleri (s.74–78)** — modelin tek deneysel ayağı. Evrenakı'nın deney fazı (T-9/Kısım 5) yazılırken buraya bakılmalı.
3. **Merkezkaç itirazı (s.60):** "enerji artınca elektron uzaklaşır" ifadesinin mekanik tutarsızlığı. Evrenakı'nın spektrum bölümünde kullanılabilir bir argüman.
4. **Nükleer kabuk model çürütmesi (s.92–101)** — Evrenakı 7.4'e "sihirli sayılar" kalemi eklenirse kaynak.
5. **Element-element çekirdek geometrileri (s.20–46)** — herhangi bir elementin yapısı sorulursa doğrudan buraya bakılır.

---

## 8. OKUMA NOTLARI (pratik)

- PDF'de **görseller taşıyıcı rol oynuyor** (Şekil 1–24 ve element şekilleri). Metin çıkarımı şekilleri vermez; kare dizilim geometrisini görsel olarak doğrulamak gerekiyorsa sayfa görüntüsü alınmalı.
- Metin çıkarımı: `fitz` (pymupdf) ile sayfa sayfa; toplam ~256.000 karakter, sayfa başına ~2.400.
- Dipnotlar metin akışının **ortasına** düşüyor (çıkarım sırası bozuk) — dipnot numaralarına göre okumak gerekir.
- Element bölümü (s.20–46) çoğunlukla tek satırlık tekrarlardan oluşuyor; **baştan okumaya değmez**, sorulan elemente göre atlanmalı.
