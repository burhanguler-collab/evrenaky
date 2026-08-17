# Girişim Simülatörü — Tartışma Kaydı

**Klasör:** `websitesi/CALISMA/GirisimSimularor/`
**Amaç:** Girişimin (interference) Evrenakı mekaniğiyle nasıl meydana geldiğini HTML5 (Canvas2D) ile, kitabın kendi denklemlerinden yürüyen bir simülatörde canlandırmak.
**Statü:** M1 v4 **Gerçek Ölçek** motoru çalışıyor: SI yakın alan + gerçek 8 m uçuş + ağırlıklı binlerce katar + gerçek $\Delta\ell/\lambda$ wake kanalları. Varsayılan sonuç: 21 aydınlık kanal, 29,31→9,96 µm dışa küçülme, gölgede kanal 0, denklik 0. **Devam etmek için §15 ve Oturum 9'u oku.**
**Açılış:** 16 Ağustos 2026 · Son güncelleme: 16 Ağustos 2026, Oturum 8

> Bu dosya kalıcı tartışma kaydıdır. Her oturumda üzerine eklenir; silinmez.
> Yazım kuralı: teorinin kendi cümlesinde **foton yoktur** (yalnız standart fizik görüşü aktarılırken tırnak içinde), **kütle-itim** kullanılır, **c sabit değildir**.

---

## 1. OKUNAN KAYNAKLAR

| Bölüm | Dosya | Girişime katkısı |
|---|---|---|
| 2.2.3 | `Kisim_2/02_Zerre_ve_Isik.md` | Zerre Katarı; $\lambda$ = ardışık Zerre arası mesafe; frekans = katar-içi vuruş ritmi; şiddet = paralel katar sayısı |
| 2.6.5 | `Kisim_2/06_Isik_Yansima...md` (sat. 938–957) | Zerre Paketi: $\varphi$'si ortak, wake-kilitli katar dilimi; $N=\nu\tau$; $E=\delta N=h\nu$; **"paket tek kolda, wake iki kolda" taahhüdü** |
| 2.7 | `Kisim_2/07_Michelson...md` | Kayıpsız girişim; karanlık saçak = terk edilmiş boşluk; 3 fazlı A/B demeti animasyonu; $4A^2$ muhasebesi |
| 2.8 | `Kisim_2/08_Kirinim_ve_Cift_Yarik...md` | Tek kenar → tek yarık → çift yarık → kırınım ağı zinciri; DENEY 4 (2 m + 8 m, He-Ne); aydınlık tarafta girişim |
| 5.2 | `Kisim_5/02_Kutle_Disi_Evrenaki_Gradyanlari.md` | Kütle dışı gradyanın ölçümü: Michelson ~0,3 saçak; fiber osilatör ~4500 m/s; attometer |
| 9.3 | `Kisim_9/03_Cift_Yarik_Geometrisinin_Sayisal_Ispati.md` | **Mach konisi ispatı ($M=1$ → düzlemsel wake, periyot $=\lambda$)**; $\Delta y=\lambda L/d$ türetimi; sayısal doğrulama |
| 9.9 | `Kisim_9/09_Tek_Foton_Cift_Yarik_Deneyleri.md` | Ölçüm/yorum ayrımı; Y-1…Y-6 çıkarım hataları; faz ortaklığı; hangi-yol mekanik müdahale |
| 1.3 | `Kisim_1/03_Evrenaki_Postulasi.md` | Postülat 1 (sıkıştırılabilir plenum), 4 (c değişken), 6 (kütle-itim) |

---

## 2. MEKANİZMANIN ANLAŞILAN HÂLİ (Claude'un özeti)

### 2.1 Ontoloji — girişen şey nedir?

| Katman | Nesne | Tanım |
|---|---|---|
| Mermi | **Zerre** | Uzaysal hacmi olan, fiziksel kütleli katı enerji damlası. Yok olamaz, bölünemez, yarımı kararsızdır. |
| Dizi | **Zerre Katarı** | Kaynağın ardışık ateşlediği Zerreler. Ardışık iki Zerre arası mesafe $\lambda=c_0/\nu_{fire}$. Frekans = katar-içi vuruş ritmi (renk). Şiddet = paralel katar sayısı. |
| Dilim | **Zerre Paketi** | Kopma penceresi $\tau$ boyunca ateşlenen, wake-kilitli, göreli fazı ($\varphi$) **ortak** katar dilimi. $N=\nu\tau\approx1{,}5\times10^4$. $E=\delta N=h\nu$. Standart fiziğin "tek foton" saydığı tespit budur. |
| Ortam | **Evrenakı** | Sürekli, atomik olmayan, **sıkıştırılabilir**, $0<\mu\ll1$ akışkan. Yerel ses hızı $c_0=\sqrt{P/\rho}$ — **sabit değil**. |

**Kritik:** Girişen şey bir olasılık genliği değildir. Girişen şey, Evrenakı'nda açılmış **gerçek bir wake alanıdır**. Zerre tek yoldadır; hiçbir noktada kendisiyle girişmez.

### 2.2 Alan — kütle dışı gradyan

Her kütle (bıçak sırtı, yarık kenarı, cam plaka) çevresinde bir **deplasman havuzu** açar: kütleye yaklaştıkça Evrenakı basıncı $P$ ve yoğunluğu $\rho$ düşer.

**Yön Kuralı (2.4.2):** $\rho$, $P$'ye ancak $k<1$ kesriyle eşlik eder ⇒
$$\frac{\delta c}{c_0}=\frac{1-k}{2}\,\frac{\delta P}{P_0}<0$$
⇒ **Işık kütlenin yanında zorunlu olarak yavaşlar.** Bu bir varsayım değil, 5.2 deneyleriyle (Michelson ~0,3 saçak, fiber ~4500 m/s, attometer) ölçülmüş bir gradyandır.

Gradyanın Zerre üzerindeki **iki ayrı etkisi** vardır ve simülatörde iki ayrı kanal olarak işlenmelidir:
1. **Yön kanalı:** $\nabla P$ Zerre'yi düşük basınca (kütleye) doğru iter → yörünge bükülür (kırınım).
2. **Hız kanalı:** $|\vec v|=c_0(x,y)=\sqrt{P/\rho}$ → Zerre kütle yanında yavaşlar (Postülat 4).

### 2.3 Wake — Mach konisi ispatı (9.3.2)

Zerre'nin Evrenakı içindeki çizgisel hızı, Evrenakı'nın kendi basınç dalgalarının yayılma hızına **tam eşittir**: $v_z=c_0$ ⇒ Mach sayısı $M=1$.

$$\theta_{Mach}=\arcsin(1/M)=\arcsin(1)=90^\circ$$

⇒ Zerre önünde küresel dalga değil, hareket yönüne **tam dik düzlemsel bir şok cephesi** yaratır. Zerreler $\lambda$ aralıklarla dizildiğinden düzlemsel wake cepheleri de **tam $\lambda$ aralıklarla** dizilir.

$$\boxed{\text{wake periyodu} = \lambda}$$

Bu, açık kalem 9.3.6/i'yi kapatan ispattır ve **simülatörün en önemli girdisidir**: wake alanının periyodu serbest parametre değil, katar aralığının kendisidir.

Her Zerre'nin arkasında ayrıca **düşük basınçlı bir wake tüneli** kalır; geriden gelen Zerreler bu tünellere kapılır → **yörünge kayması (drift)**.

### 2.4 Girişim — dört adımlı mekanizma

**Adım 1 — Kenar bükmesi (2.8.1, DENEY 4).**
Kenara en yakın geçen Zerre en şiddetli gradyana girer, gölgeye derin dalar; uzaklaştıkça bükülme sönümlenir. Kenara **değen** Zerreler ise sekerek düz sürünün içine şahlanır. Yeterince uzaktaki Zerre hiç sapmaz.

**Adım 2 — Yörünge kesişmesi.**
Bükülenler uzun yol, düz gidenler kısa yol alır ⇒ varışta faz/zaman farkı. Bükülen yörüngeler düz süreyi **çaprazlama keser**. Kesişmenin gelişmesi için uzun uçuş mesafesi şarttır (DENEY 4'te 8 m).

> **Teorinin ayırt edici iddiası:** Girişim **gölgede değil, aydınlık alanda** oluşur. Çünkü gölgeye kavis çizen Zerreler oraya *yalnız* gider; kesişecek ikinci bir sürü yoktur. Kesişme yoksa girişim de yoktur. (Şekil 2.8.1.2 laboratuvar kaydı bunu gösteriyor.)

**Adım 3 — Wake kanalına yığılma (drift).**
Kesişme bölgesinde Zerreler birbirlerinin düşük basınçlı wake tünellerine kapılır. Direncin en düşük olduğu birkaç **ana kanala (otoban)** yığılırlar; terk edilen hatlar boşalır.
- **Aydınlık saçak** = yığılma kanalı (Zerre sayısı katlanır)
- **Karanlık saçak** = terk edilmiş boşluk (**yok olma değil, göç**)

Kırınım ağında (binlerce yarık) bu, nehir deltası mantığıyla keskinleşir: ara patikalar kurur, ana yataklar jilet gibi keskinleşir.

**Adım 4 — Wake alanı geometrisi (9.3.3, 9.9.6).**
Çift yarıkta: **paket (somut mermiler) tek yarıktan geçer; paketin açtığı wake izleri her iki yarıktan da geçer.** İki eş-fazlı wake kaynağı arkada üst üste biner:

$$\Delta = d\sin\theta \approx d\frac{y}{L},\qquad \Delta=m\lambda \;\Longrightarrow\; \boxed{\Delta y=\frac{\lambda L}{d}}$$

Bu, mutlak akışkan içinde **duran basınç vadileri** (düşük basınç koridorları) yaratır. Tek yarıktan geçen paket kendi yarattığı bu alanın içine düşer ve vadilere sürüklenir. Hangi vadiye düşeceğini kontrolsüz varış fazı $\varphi$ seçer.

Sayısal kontrol: $\lambda=632{,}8$ nm, $d=0{,}25$ mm, $L=1$ m ⇒ $\Delta y=2{,}53$ mm ✅

### 2.5 Enerji muhasebesi — hiçbir kayıp yok

Standart optik: $S_ş\propto A^2$, aynı fazda $1A+1A=2A$ ⇒ tepe $(2A)^2=4A^2$. Desen ortalaması $2S_{ş,0}$.

Teoride bunun karşılığı Zerre sayısıdır. Tek demetin düzgün yoğunluğu $n_0$ ise:
$$n(y)=4n_0\cos^2\!\Big(\frac{\pi d y}{\lambda L}\Big)$$
- tepe $=4n_0$ (tek demetin **4 katı**) ✅
- çukur $=0$ (Zerre yok — **terk edilmiş**, yok edilmiş değil) ✅
- ortalama $=2n_0$ (iki demetin toplamı — **korunum**) ✅

⇒ **Simülatörün kapanış sınavı budur:** drift dinamiğinden çıkan histogram bu üç sayıyı da tutturmalı.

### 2.6 Türev gözlemler

| Gözlem | Teorinin okuması |
|---|---|
| Tekil tespit hep **tek nokta** (Tonomura ~70.000) | Bir tespit = bir dilimin bir pencereye varışı. Zorunluluk, varsayım değil. |
| Hangi-yol ölçümü deseni siler | Ölçen aygıt fiziksel cisimdir; kütlesiyle ve türbülansıyla **wake'i mekanik olarak bozar**. Bilgi değil müdahale. **Öngörü: silinme kesikli eşiğe değil sürekli müdahale şiddetine bağlıdır.** |
| Anti-demetlenme $g^{(2)}(0)<1$ | Dilim-içi **faz ortaklığı**; rampa kararı dilim boyunca tektir. **Öngörü: faz-karışık (termal) kaynakta $g^{(2)}\geq1$.** |
| Geometriye bağımlı form (dairesel yarık → dairesel desen) | Deseni belirleyen wake/gradyan geometrisidir; Zerre sadece akıntıyı izler. |

---

## 3. TARTIŞMAYA AÇILAN KONULAR

### T-1. İki mekanizma katmanı birleştirilmeli — **en kritik karar**

Kitapta girişimin **iki ayrı anlatımı** var ve ikisi farklı seviyede:

| | (A) Zerre-arası wake drift | (B) Wake alanı geometrisi |
|---|---|---|
| Kaynak | 2.7, 2.8 | 9.3, 9.9.6 |
| Mekanizma | Zerreler birbirinin tünelini takip eder, kanala yığılır | Paket tek yarıkta, wake iki yarıkta; duran basınç vadileri |
| Verdiği | Kontrast (parlak/karanlık farkı), kayıpsızlık | **Saçak konumu** $\Delta y=\lambda L/d$ |
| Vermediği | Saçak aralığının sayısı | Parlaklık dağılımı (9.9.8/i açık kalem) |

**Claude'un önerisi:** İkisi rakip değil, tamamlayıcıdır. Simülatörde **tek motor, iki terim**:
> **(B) saçağın NEREDE olduğunu, (A) NE KADAR parlak olduğunu üretir.**

Yani basınç alanı $P_{toplam}=P_{gradyan}(\text{kenarlar})+P_{wake}(\text{katar cepheleri})+P_{tünel}(\text{komşu Zerreler})$; Zerre bu tek alanın $-\nabla P$ kuvvetiyle sürüklenir ve $|\vec v|=\sqrt{P/\rho}$ ile ilerler.

**Karar gerekli:** Bu birleştirme kabul mü? Yoksa iki ayrı mod (A modu / B modu) olarak mı sunulsun?

---

### T-2. Düzlemsel wake cephesi yarıkta nasıl yanal yayılıyor?

$M=1$ ⇒ wake cephesi harekete **tam dik düzlem**. Ama $\Delta y=\lambda L/d$ türetimi, her yarığın bir **kaynak gibi yayılmasını** ister ($d\sin\theta$ yol farkı için).

Düzlem cephe kendi başına yanal yayılmaz. Aradaki köprü ne?

**Aday açıklama:** Yarık açıklığı bir sert sınırdır; düzlemsel basınç cephesi açıklığa çarptığında kenarlarda basınç yanal olarak boşalır (sıkıştırılabilir ortamda basınç farkı yanal denkleşir) ⇒ açıklıktan çıkan cephe **yerel olarak kavislenir**. Yani Huygens'in hidrodinamik karşılığı, ayrı bir ilke değil; sıkıştırılabilirliğin (Postülat 1) sonucu.

**Karar gerekli:** Bu köprü teorinin bir taahhüdü olarak mı yazılsın (kitaba geri besleme), yoksa simülatörün açıkça ilan edilmiş modelleme varsayımı olarak mı kalsın? *(Not: kitaba girecekse 9.3.6'ya yeni kalem veya kapanış olarak işlenmeli.)*

---

### T-3. Bükülmede çift sayım riski

Gradyan hem (i) $-\nabla P$ kuvvetiyle yörüngeyi büküyor, hem (ii) $c_0=\sqrt{P/\rho}$ ile hızı düşürüyor. Hız düşüşü tek başına da bükülme üretir (yavaş ortama doğru kırılma — Snell mantığı).

**Claude'un önerisi:** Çift sayım değil, **iki ayrı kanal**:
- **Yön** ← $-\nabla P$ (kuvvet, ivme)
- **Büyüklük** ← $c_0(x,y)$ (Postülat 4, hız normu)

Her adımda: ivmeyi uygula → yön güncelle → hız normunu $c_0(x,y)$'ye **yeniden ölçekle**. Böylece bükülmenin tamamı gradyandan gelir ama hız her noktada yerel $c_0$'a kilitli kalır.

**Karar gerekli:** Bu ayrım onaylanıyor mu?

---

### T-4. Parlaklık ölçeği: "katlanarak" ne demek?

2.7.2'de "*parlaklık oraya düşen zerrelerin miktarı oranında katlanarak*" deniyor. §2.5'teki hesap gösteriyor ki **doğrusal orantı** ($I\propto n$) zaten $4\times$ tepeyi veriyor — çünkü tepeye düşen Zerre sayısının kendisi $4n_0$ oluyor.

**Öneri:** Simülatörde $I\propto n$ (doğrusal) kullanılsın; $4\times$ sonucu **çıktı** olsun, girdi değil. Kitaptaki "katlanarak" ifadesi $\propto n^2$ diye okunursa muhasebe bozulur.

**Karar gerekli:** $I\propto n$ onaylanıyor mu? *(Onaylanırsa 2.7.2'deki cümlenin netleştirilmesi için KARNE'ye düzeltme kaydı düşülmeli.)*

---

### T-5. Ölçek ve abartma katsayısı

Gerçek sayılar: $\lambda=632{,}8$ nm, $d=0{,}25$ mm, $L=1$ m ⇒ $\Delta y=2{,}53$ mm. Yani $\lambda/d\approx2{,}5\times10^{-3}$ — ekranda Zerre ile saçak arasında $\sim4000\times$ ölçek farkı var.

**Öneri:** İki mod:
- **Gerçek mod:** Gerçek $\lambda,d,L$; Zerreler nokta; sayısal panel $\Delta y_{ölçülen}$ vs $\lambda L/d$ karşılaştırması yapar. *(Sınav modu)*
- **Anlatı modu:** $\lambda$ abartılmış, Zerreler görünür damla, wake cepheleri çizili. *(Öğretim modu — kitaptaki animasyonların canlı hâli)*

Her iki modda da ekranda "ölçek abartma katsayısı: ×N" açıkça yazılmalı (dürüstlük kaydı).

---

### T-6. Kaç Zerre simüle edilecek?

Bir paket $N\approx1{,}5\times10^4$ Zerre. Tarayıcıda gerçek zamanlı $10^4$ parçacık + karşılıklı wake etkileşimi ağır.

**Öneri:** Katmanlı yaklaşım:
- Wake **alanı** ızgarada (grid) hesaplansın — $O(\text{grid})$, parçacık sayısından bağımsız.
- Zerreler alanı **okuyan** test parçacıkları olsun — $O(N)$.
- Zerre→alan geri beslemesi (kendi tünelini açması) seyreltilmiş temsille (her Zerre ızgaraya küçük bir negatif basınç damgası bıraksın, zamanla sönümlensin).
- Ekranda aynı anda ~300–2000 Zerre; histogram binlerce atım biriktirsin.

---

### T-7. Simülatörün asıl hedefi: hangi açık kalemi kapatacak?

Simülatör sadece görsel olmasın; **7.4 envanterindeki açık kalemlere** sayısal katkı üretsin:

| Açık kalem | Simülatörün yapabileceği |
|---|---|
| **9.9.8/i** — wake-vadi seçim mekaniği; parlaklık dağılımının türetimi | Drift dinamiğinden çıkan histogramın $4n_0\cos^2$ ile karşılaştırılması. **Birincil hedef.** |
| **9.3.6/ii** — DENEY 4'ün Fresnel ile saçak-saçak karşılaştırması | 2 m + 8 m geometrisinde balistik desen vs klasik Fresnel integrali, üst üste |
| **9.9.8/iii** — hangi-yol müdahalesinin niceliği | Yarığa kütle/dedektör konunca görünürlük $V$ vs müdahale şiddeti eğrisi (**sürekli** çıkmalı) |
| **9.3.6/iv** — $\varphi$ dağılımı | $\varphi$ düzgün dağılımlı verilince desenin doğru çıkması; başka dağılımlarla bozulması |

**Karar gerekli:** Birincil hedef 9.9.8/i olsun mu?

---

## 4. ÖNERİLEN MODÜL PLANI (taslak — onay bekliyor)

| # | Modül | İçerik | Sınavı |
|---|---|---|---|
| M0 | **Evrenakı Alanı** | $P$, $\rho$, $c_0=\sqrt{P/\rho}$ ısı haritası; kütleler etrafında deplasman havuzu | Yön Kuralı: kütleye yaklaşınca $c_0$ düşüyor mu? |
| M1 | **Tek Kenar (DENEY 4)** | 15 Zerre, çarpma/sekme/bükülme/sıfır etki; ekranda glow | Saçaklar **aydınlık tarafta** mı? Ölçek $\sqrt{\lambda L}$ mi? |
| M2 | **Tek Yarık** | İki karşılıklı kenar; merkez düz, kenarlar dışa kavis; yelpaze | Yayılma açısı $\sim\lambda/a$ mı? |
| M3 | **Çift Yarık** | Paket tek yarıkta, wake iki yarıkta; duran basınç vadileri; birikim | $\Delta y=\lambda L/d$ ✓; tepe $=4n_0$ ✓; ortalama $=2n_0$ ✓ |
| M4 | **Michelson (2.7)** | 3 fazlı: A tek → B tek → birlikte; enerji defteri paneli | Toplam Zerre sayısı üç fazda da aynı mı? (kayıpsızlık) |
| M5 | **Kırınım Ağı** | $N$ yarık; delta mantığıyla ana kanalların keskinleşmesi | İkincil saçaklar sönüyor mu? Ana maksimumlar keskinleşiyor mu? |
| M6 | **Hangi-Yol** | Yarığa kütle/aygıt; wake bozulması; görünürlük düşüşü | Silinme **sürekli** mi (eşikli değil)? |
| M7 | **Seyreltilmiş Kaynak** | Tek paket → tek nokta; binlerce atımda desen birikimi | Tekil karede desen **yok**, istatistikte **var** |

**Teknik:** Saf HTML5 + Canvas2D + vanilla JS, tek dosya, harici bağımlılık yok (sitedeki diğer simülasyonlarla aynı çizgi: `--bg-color:#121212`, `--accent:#00ffcc` paleti).

---

## 5. TERMİNOLOJİ KİLİDİ (arayüzde uyulacak)

| Kullanılacak | Kullanılmayacak |
|---|---|
| Zerre, Zerre Katarı, Zerre Paketi | foton (yalnız "standart fizik böyle sayar" bağlamında, tırnakta) |
| Evrenakı, deplasman havuzu, basınç gradyanı | eter, alan (field) yerine geçecek şekilde |
| kütle-itim, basınç gradyanı kuvveti | kütleçekim (yalnız std. fizik görüşü aktarılırken) |
| yerel $c_0=\sqrt{P/\rho}$ | "ışık hızı sabiti" |
| wake, wake tüneli, iz, yörünge kayması (drift) | olasılık dalgası, dalga fonksiyonu (yalnız karşılaştırma panelinde) |
| terk edilmiş boşluk (karanlık saçak) | yıkıcı girişim / yok olma |

---

## 6. AÇIK SORULAR — KULLANICI YANITI BEKLENİYOR

1. **T-1:** (A)+(B) tek motorda birleşsin mi, yoksa iki ayrı mod mu?
2. **T-2:** Düzlem wake cephesinin yarıkta yanal yayılması — teori taahhüdü mü, simülatör varsayımı mı?
3. **T-3:** Yön ← $\nabla P$ / Büyüklük ← $c_0$ ayrımı onaylanıyor mu?
4. **T-4:** Parlaklık $I\propto n$ (doğrusal) onaylanıyor mu? 2.7.2'deki "katlanarak" ifadesine düzeltme kaydı düşülsün mü?
5. **T-7:** Birincil hedef 9.9.8/i (parlaklık dağılımının türetimi) olsun mu?
6. **Modül sırası:** M0→M1→M3 mü (mekanizma zinciri), yoksa doğrudan M3 (çift yarık) mı?
7. **Tek dosya mı, modül başına ayrı dosya mı?**

---

## 8. SAF AKIŞKANLAR MEKANİĞİ ÇERÇEVESİ (Oturum 2)

> **Kullanıcı direktifi (16 Ağu 2026):** *"Standart bilimin açıklamalarını unut. Tamamen akışkanlar mekaniği."*
> ⇒ §3'teki T-1 ve T-2, optik iskeleye yaslandığı için **iptal edildi**. Aşağıdaki çerçeve onların yerine geçer.
> Kural: Huygens ilkesi, dalga fonksiyonu, "süperpozisyon ilkesi", ödünç alınmış optik formül **yok**. Yalnız sıkıştırılabilir akışkan mekaniği + katı mermi dinamiği. Optik formüller ancak **sonuç** olarak çıkarsa kabul; **başlangıç** olarak asla.

### 8.1 Ortam ve mermi

| Nesne | Akışkan mekaniği tanımı |
|---|---|
| **Evrenakı** | Sürekli, atomik olmayan, **sıkıştırılabilir** akışkan. $0<\mu\ll1$. Yerel sinyal (ses) hızı $a=\sqrt{P/\rho}$. |
| **Zerre** | Hacimli, kütleli katı damla (blunt body). Ortam içindeki hızı $v_z=a$ ⇒ **$M=1$ tam**. |
| **Katar** | $\nu$ hızıyla ateşlenen Zerre dizisi; aralık $\lambda=a/\nu$. |

### 8.2 Tek Zerre'nin akışkanda bıraktığı yapı (üç parça)

1. **Önünde:** $M=1$ ⇒ Mach konisi $90^\circ$'ye dejenere olur ⇒ harekete **tam dik düzlemsel sıkışma cephesi**. Mermi kendi biriktirdiği bozulmanın ön kenarında oturur.
2. **Arkasında:** taban basıncı düşük **wake tüneli** (blunt-body base pressure). Emici.
3. **Yanında:** deplasman akışı.

### 8.3 Katarın bıraktığı yapı — λ periyotlu basınç oluğu

Zerreler $\lambda$ aralıklı olduğundan, her birinin dik cephesi de $\lambda$ aralıklı dizilir.

$$\Rightarrow \text{Ortamda } \lambda \text{ periyotlu paralel basınç cepheleri dizisi} = \textbf{basınç oluğu (corrugation)}$$

Bu bir "dalga" değil, akışkanda **gerçek bir oluklu basınç manzarasıdır**. Periyodu serbest parametre değil: $\lambda=a/\nu$.

### 8.4 Kenar: gemi-emme etkisi (kırınımın akışkan karşılığı)

Katı cisim akışkanı yer değiştirir ⇒ çevresinde deplasman havuzu ⇒ cisme doğru $P$ düşer.
Yanından geçen Zerre, yüksek basıncın olduğu dış taraftan itilip cisme doğru **emilir**.

Akışkan mekaniğinde ölçülen karşılığı: **gemi-gemi emme etkisi (ship-to-ship suction)** ve **Coandă tutunması**. Paralel seyreden iki gemi birbirine emilir; bir jet yakınındaki duvara yapışır. Aynı mekanik.

- Yakın geçen: güçlü emme, derin kavis
- Uzaklaştıkça: sönümlenerek azalır
- Değen: seker (mekanik çarpışma)

**Optik yok. Sadece cisim-yakını basınç düşüşü.**

### 8.5 Yarık: nabızlı orifis

$\lambda$ periyotlu oluk cephesi bariyere çarpar. Katıdan geçemez; **açıklıktan geçer**.

Açıklıktaki basınç, oluk periyoduyla ritmik olarak yükselip düşer ⇒ **açıklık nabızlı bir orifis gibi davranır** ve her nabızda ortama **yanal yayılan** bir basınç darbesi salar.

> Bu Huygens ilkesi değildir. Sıkıştırılabilir bir ortamda, açıklığın iki yanı arasındaki basınç farkının yanal denkleşmesidir. Bir orifisin nabız attığında ortama darbe salması akustikte ölçülen sıradan bir olgudur (orifis radyasyonu). Bir ilke değil, bir sonuç.

### 8.6 **MOİRE** — girişimin tek cümlelik akışkan tanımı

İki $\lambda$-periyotlu basınç oluğu, aralarında $2\alpha$ açıyla kesişsin. Çukurların çakıştığı yerler **duran alçak-basınç vadileri** oluşturur; vadi aralığı saf geometriden çıkar:

$$\boxed{\Lambda_{vadi}=\frac{\lambda}{2\sin\alpha}}$$

Mutlak ortam + mutlak zaman (Postülat 3) gereği bu vadiler ortamda **gerçekten durur** — hayali değil, ölçülebilir basınç yapısı.

Bu **tek bağıntı** kitaptaki üç ayrı anlatımı birleştirir:

| Düzenek | $\alpha$'nın kaynağı | Sonuç |
|---|---|---|
| **Michelson (2.7)** | Aynaların hizalama farkı | Sabit aralıklı düz saçaklar |
| **Çift yarık (2.8.3, 9.3)** | $2\alpha\approx d/L$ | $\Lambda=\lambda/(2\cdot d/2L)=\boxed{\lambda L/d}$ — **optikten ödünç değil, iki oluğun geometrisinden çıktı** |
| **Tek kenar (2.8.1, DENEY 4)** | Bükülme kavisi konuma göre değişir ⇒ $\alpha=\alpha(y)$ | **Aralık konuma göre değişir** ⇒ dışa doğru saçaklar sıkışır |

> **Kritik kazanç:** Son satır, Şekil 2.8.1.2'deki laboratuvar gözlemini — *"gittikçe küçülen parmaklar"* — doğrudan üretir. Sabit-aralık veren hiçbir formül bunu veremez; moiré çerçevesi kendiliğinden verir. Bu, teorinin kendi laboratuvar kaydıyla kurulmuş bir iç doğrulamadır.

### 8.7 Zerre vadide ne yapar? — iki sıkıştırıcı etki

1. **Yanal sürüklenme:** $\vec F=-V_z\nabla P$ ⇒ Zerre vadiye doğru itilir.
2. **Süreklilik yığılması:** Vadide $P$ düşük ⇒ $a=\sqrt{P/\rho}$ düşük ⇒ **Zerre yavaşlar**. Süreklilik gereği $n\,v=\text{sabit}$ ⇒ **yavaşladığı yerde $n$ yükselir**.

⇒ Parlaklık iki bağımsız akışkan etkisiyle birden artar: içeri sürüklenme **ve** içeride yavaşlama.

### 8.8 Kanal kilitlenmesi — öz-örgütlenme

Her Zerre kendi wake tünelini açar; arkadan gelen o tünele emilir (**drafting / slipstream**).

Akışkanlar mekaniğinde ölçülmüş karşılığı: **eylemsizlik odaklaması (inertial focusing, Segré–Silberberg)** — bir kanalda rastgele dağılmış parçacıklar, salt hidrodinamik kaldırma kuvvetleriyle kendiliğinden belirli yanal konumlara oturur ve **düzenli katarlar** oluşturur. Kimse onlara nereye gideceğini söylemez.

⇒ Vadiler zamanla derinleşir, ara patikalar kurur. Kırınım ağındaki jilet keskinliği (2.8.3.2, nehir deltası) bunun doymuş hâlidir.

### 8.9 Kayıpsızlık bir iddia değil, süreklilik denklemi

$$\frac{\partial n}{\partial t}+\nabla\cdot(n\vec v)=0$$

Zerre yok olamaz. **Karanlık saçak $n\to0$ demektir, imha değil.** Ekrandan geçen toplam akı = ateşlenen toplam. Bu bir tez değil, modelin kimliğidir — ayrıca kanıtlanacak bir şey yoktur.

### 8.10 Viskozitenin işi — iki ölçek ve bir öngörü

$\mu\approx0$ ama $\mu\neq0$ ⇒ wake tünelleri ve oluk cepheleri sönümlenir. İki karakteristik ölçek doğar:

| Ölçek | Anlamı | Gözlemsel karşılığı |
|---|---|---|
| **Wake ömrü** $\ell_\parallel$ (boyuna) | İzin ne kadar geriden takip edilebildiği | Katar-içi kilitlenme mesafesi; koherans uzunluğu |
| **Yanal wake yarıçapı** $R_\perp$ (enine) | Oluk cephesinin yanal olarak nereye kadar uzandığı | **Yeni** |

> **Teoriye özgü, ölçülebilir öngörü:** Yarık aralığı $d>R_\perp$ olursa, ikinci yarık oluk cephesine hiç ulaşamaz ⇒ **desen ölür**. Standart çatı bunu "koherans genişliği" diye adlandırır ama mekanik bir sebep vermez; burada sebep viskoz sönümdür ve $R_\perp$ bağımsız ölçülebilir.

### 8.11 Bu çerçevenin kitaba geri beslemesi

| Kazanım | Nereye |
|---|---|
| Moiré birleştirmesi: 2.7 + 2.8.3 + 9.3 tek mekanizma | 9.3'e mekanizma katmanı; 9.9.8/i'ye doğrudan katkı |
| Tek kenarda saçak sıkışması ($\alpha=\alpha(y)$) | 2.8.1 — laboratuvar kaydının (Şekil 2.8.1.2) türetimi |
| Süreklilikten parlaklık ($n v=$ sbt) | 9.9.8/i — parlaklık dağılımının türetimi |
| Yanal wake yarıçapı $R_\perp$ | Yeni ayırt edici öngörü — 7.4 envanterine aday |
| Kayıpsızlık = süreklilik denklemi | 2.7.3 — iddiadan kimliğe terfi |

### 8.12 Anlaşılması gereken 4 çatal

- **Ç-1** — **Moiré birleştirmesi** (§8.6) kabul mü? Girişimin tek tanımı *"iki $\lambda$-oluğunun kesişmesinden doğan duran basınç vadileri"* olsun mu?
- **Ç-2** — **Yarık = nabızlı orifis** (§8.5) kabul mü, yoksa oluk cephesinin yanal yayılımı için sizin başka bir akışkan mekanizmanız var mı? *(§3'teki T-2'nin akışkanlar hâli)*
- **Ç-3** — **Süreklilikten parlaklık** (§8.7-2: yavaşla → yığıl) kabul mü? Bu kabul edilirse parlaklık $4\times$ tepesi ayrıca varsayılmaz, **çıkar**.
- **Ç-4** — **$R_\perp$ (yanal wake yarıçapı)** simülatöre parametre olarak girsin mi? Girerse desen ölümü öngörüsü sınanabilir hâle gelir.

---

## 9. TEK KENAR (BIÇAK) MEKANİZMASI — KULLANICI TANIMI (Oturum 3)

> **Kullanıcı:** *"Önce tek kenar (bıçak kenarı), çünkü her şey orada temelleniyor."*
> Aşağıdaki 10 madde **kullanıcının kendi tanımıdır** ve simülatörün çekirdek sözleşmesidir. Claude'un yorumu ayrı işaretlenmiştir.

### 9.1 On madde (kullanıcı tanımı)

| # | Madde | Simülatör karşılığı |
|---|---|---|
| **1** | Aynı kaynaktan gelen tüm katarlardaki zerreler **hizalıdır** | Başlangıçta düz, ışına dik bir **saf cephesi** (rank line). Katarlar yan yana paralel, $n$'inci zerreler aynı boylamda. |
| **2** | Zerre gradyanda **yoğundan az yoğuna** kıvrılmak zorundadır | $\vec a=-K\nabla P$; bıçağa doğru. Zorunluluk, seçim değil. |
| **3** | Az yoğun ortamda **yoğunluğa bağlı hız kaybı** | $\vert\vec v\vert=a(x,y)=\sqrt{P/\rho}$; bıçağa yakın yavaş. |
| **4** | En yakın geçen zerre **hem en çok yavaşlar hem en çok kıvrılır** | Tek gradyanın iki çıktısı. Aynı $b$ (çarpma parametresi) fonksiyonu ikisini de yönetir. |
| **5** | Bıçak ucu merkez alınırsa: zerre **yaklaşırken bıçağa doğru**, **uzaklaşırken de bıçak yönünde** kıvrılır | **Merkezî çekici alan.** Kuvvet daima uca doğru. Kapanma noktasından sonra da bükme sürer ⇒ yörünge, en yakın geçiş noktasına göre simetrik bir saçılma yörüngesidir. Toplam sapma, yaklaşma sapmasının ~2 katı. |
| **6** | Bir kısım zerre, uca varmadan kıvrıldığı için **uca çarpıp yansır**. Yansıma geliş=çıkış açısı kuralına uyar. **Farkı:** yüzeye varmadan bükülmüştür, **yansırken de ters yönde kıvrılır** | Açılar **temas anındaki teğetten** ölçülür, özgün ışın yönünden değil. Yansıdıktan sonra alan hâlâ uca çektiği için eğrilik yönü terslenir. *(Standart bilimde bu iki bükülme yoktur.)* |
| **7** | Katarlar paralel gelir; uçtan uzaklaştıkça kıvrılma azalır, **yeterince uzak hiç kıvrılmaz** | Sapma açısı $\theta(b)$ monoton azalan; $b>b_{max}$'ta sıfır. |
| **8** | Hız kaybı düzeni bozmaz: bıçağa aynı uzaklıktaki bir katarın bütün Zerreleri aynı zorunlu hareketi yapar; en yakın katar hem **yol uzunluğu** hem **hız kaybı** nedeniyle daha fazla gecikir | **İki bileşenli gecikme:** $\Delta s(b)=\underbrace{[\ell(b)-\ell_\infty]}_{\text{yol}}+\underbrace{a_0\!\int\!\big(\tfrac{1}{a}-\tfrac{1}{a_0}\big)ds}_{\text{yavaşlama}}$. Katar içindeki $\lambda$ aralığı ve Zerre hizası korunur; gecikme katarın tamamına, bıçağa uzaklığı $b$ tarafından belirlenen tek bir değer olarak uygulanır. |
| **9** | Bıçağı geçen katarlar **hizalı ve düzenlidir**; fakat katarlar arası mesafe daralmış ve her katar bıçağa uzaklığının belirlediği bir açı kazanmıştır | Çıkışta rastgele saçılma yoktur. Başlangıçtaki paralel katar örgüsü, $b$'ye bağlı $\theta(b)$ açılarından ve belirlenimli biçimde daralmış katar aralıklarından oluşan yeni bir düzenli örgüye dönüşür. |
| **10** | **EN ÖNEMLİ:** Arkadan gelen zerre, önden gidenin **izine yakalanır** ve **yörüngesi öndekinin yörüngesine dönüşür**. Aydınlatması gereken yer karanlık kalır; vardığı yeni yer daha aydınlık olur | **Yakalanma = tam kilitlenme**, küçük sürüklenme değil. Yörüngeler ayrık kanallara **çöker**. Karanlık = terk, aydınlık = birleşme. Kilitlenen çiftin izi güçlenir ⇒ daha çok yakalar ⇒ **pozitif geri besleme** ⇒ kanal keskinleşir. |

### 9.2 Bıçak ucu bir nokta değil, dar bir düzlemdir (kullanıcı notu)

> *"Biz bakınca üçgen kenarı gibi görürüz ama zerre boyutlarında bu keskin yer çok dar da olsa bir düzlemdir."*

Üç zorunlu sonucu var — üçü de simülatörde parametre:

1. **Gradyan tekilliği yok.** $P(r)$ uçta ıraksamaz; $w$ (düzlem genişliği) ölçeğinde **doygunluğa** oturur. Aksi hâlde sayısal patlama olur ve fizik de yanlış olur.
2. **Yansıma gerçek bir düzlemdendir.** Madde 6'daki geliş=çıkış kuralı bir yüzey normali gerektirir; düzlem onu sağlar.
3. **$w$, yansıyan aileyi besleyen tek kapıdır.** Sadece $b\lesssim w$ bandındaki zerreler uca çarpar ⇒ **$w$, yansıyan ailenin akısını, dolayısıyla saçak kontrastını belirler.** Saçakların ana demetten çok sönük olmasının sebebi budur.

### 9.3 Claude'un eklemek istediği 11. madde — **periyodikliğin kaynağı**

Madde 1–10 sürekli (continuous) bir sapma haritası veriyor. Ama ekranda görülen **tekrarlayan** saçaklardır. Periyodikliği veren halka şu:

**(a) İkinci aile — madde 6'nın asıl rolü.**
Uçtan yansıyan zerreler, hiç dokunmadan düz giden devasa sürünün **içine** dalar. Aydınlık alanda **iki aile çaprazlama kesişir**:
- **Aile-D:** sapmasız düz sürü
- **Aile-Y:** uçtan yansıyan (madde 6) — akısı $w$ ile orantılı, seyrek

Gölgeye kıvrılan aile ise oraya **yalnız** gider; kesişecek partneri yoktur ⇒ **gölgede saçak yok**. (Kitabın 2.8.1'deki iddiası bu mekanizmadan doğrudan çıkıyor.)

**(b) Periyodikliği veren şey: wake'in λ-yuvalı olması.**
Her katar $\lambda$ aralıklı olduğundan, bir zerrenin ardındaki iz **düzgün değildir** — boyunca $\lambda$ aralıklı alçak-basınç yuvaları (tüneller) ve aralarında $\lambda$ aralıklı sıkışma cepheleri ($M=1$) vardır.

Yanal olarak sürüklenen bir zerre bu yapıya rastgele girmez:

| Boylamsal gecikme | Ne olur | Ekranda |
|---|---|---|
| $\Delta s \equiv 0 \pmod{\lambda}$ | **Yuvaya** düşer ⇒ madde 10 kilitlenmesi çalışır ⇒ yörünge birleşir | **Aydınlık** |
| $\Delta s \equiv \lambda/2 \pmod{\lambda}$ | **Sıkışma cephesine** çarpar ⇒ itilir, bölgeyi terk eder | **Karanlık (gerçekten boş)** |

⇒ Madde 8'in ürettiği gecikme $\Delta s$, madde 10'un kilitlenmesini **$\lambda$ modunda açıp kapatır**. Periyodiklik buradan doğar. Karanlık sadece "yakalanmama" değil, **aktif itilmedir** — bu yüzden gerçekten boştur.

**(c) Neden dışa doğru sıkışıyor? ("küçülen parmaklar")**
İki ailenin kesişme açısı $2\alpha$, ekranda dışa gidildikçe **büyür**. Vadi aralığı $\Lambda=\lambda/(2\sin\alpha)$ olduğundan aralık **küçülür**. Şekil 2.8.1.2'deki laboratuvar kaydı (gittikçe daralan ve sönen parmaklar) tam olarak budur — ayrıca varsayılmadan çıkıyor.

> **Onay gerekiyor:** 11. madde (λ-yuvalı yakalama koşulu) mekanizmaya ekleniyor mu? Ekleniyorsa madde 6 "yan detay" değil, **aydınlık alandaki saçak ailesinin kaynağı** olarak yükseltilmeli.

### 9.4 Simülatörün sayı bekleyen kalemleri

| # | Parametre | Neden gerekli | Aday |
|---|---|---|---|
| P-1 | **Gradyan profili** $P(r)$ | Madde 2–4,7'nin niceliği | 2.8.1: *"doğrusal olarak sönümlenir"* ⇒ $\delta P\propto(1-r/R)$, $r>R$'de sıfır. **Onay?** |
| P-2 | **Etki yarıçapı** $R$ | Madde 7'deki "yeterince uzak hiç kıvrılmaz" sınırı | ? |
| P-3 | **Uç düzlem genişliği** $w$ | Madde 6'nın akısı + tekillik regülasyonu | ? |
| P-4 | **Kaynak: yalnız uç mu, tüm bıçak konturu mu?** | 2.8.1'de 1. zerre **gövdeye** çarpıyor ⇒ gövde de alan üretiyor | Kontur öneriliyor |
| P-5 | **$k$ katsayısı** ($\rho$'nun $P$'ye eşlik oranı) | Madde 3'ün yönü; $a=\sqrt{P/\rho}$'nin düşmesi $k<1$ gerektirir | Yön Kuralı, 2.4.2 |
| P-6 | **İz tüneli yarıçapı** $R_{iz}$ | Madde 10'un yakalama eşiği (yanal) | ? |
| P-7 | **İz ömrü** $\ell_\parallel$ | Madde 10'un yakalama eşiği (boyuna) | ? |

> **Not (P-5):** Madde 3'te *"az yoğun ortamda hız kaybı"* deniyor. Mekanik olarak hızı belirleyen $\rho$ tek başına değil, $P/\rho$ oranıdır; bıçak yanında ikisi de düşer ama $\rho$ ancak $k<1$ kesriyle eşlik ettiği için oran düşer ve zerre yavaşlar. Sonuç kullanıcının dediğiyle aynı; simülatör **iki alanı birden** (ya da $P$ + $k$) taşımalı.

---

## 10. VERNİYER İLKESİ — SAÇAKLARIN KENDİLİĞİNDEN DOĞUŞU (Oturum 4)

> **Kullanıcı:** *"Verniyer kumpaslarda aynı uzunlukta bir uzunluk 10 çizgi içerirken bir uzunluk 9 çizgi içerir. Böylece tek bir çizginin diğer bir çizgi ile tam hizalanması adım adım gerçekleşir. Bizim mekanizmamızda da yansıma ve kıvrılmalar sonucu aynı genişlikte katarlar arası mesafe değişir; böylece yansıyanlar ve yansımayanlar arasında katar arası farklılaşır. Bu girişimi zaten otomatik oluşturacaktır."*

**Bu, §8.6'daki moiré ve §9.3'teki λ-yuva önerisinin yerine geçen, ikisini de kapsayan ana ilkedir.**

### 10.1 İlke

Verniyer kumpasta iki cetvel vardır; **aynı uzunlukta farklı sayıda bölüntü** taşırlar (10'a 9). Sonuç: iki bölüntü yalnızca **tek bir noktada** tam çakışır, komşuları giderek kaçar, sonra bir sonraki noktada yeniden çakışır. **Çakışma noktaları kendiliğinden periyodiktir.** Kimse "çakışsın" demez; farklı adımın kaçınılmaz sonucudur.

Bizim mekanizmamızda da tam olarak iki cetvel vardır:

| | Cetvel | Nereden gelir |
|---|---|---|
| **Aile-D** | Sapmasız düz giden katarlar | Bıçaktan yeterince uzak (madde 7) |
| **Aile-Y** | Uçtan yansıyan katarlar | Uca çarpanlar (madde 6) |

**Katar = cetvel; ardındaki λ-yuvaları = bölüntüler.**

### 10.2 Adım farkı nereden doğuyor?

Madde 8–9 gereği bıçaktan sonra düzen kaybolmaz: her katar kendi içinde hizalı kalır; katar aralıkları belirlenimli biçimde daralır ve her katar bıçağa uzaklığının belirlediği açıyı kazanır. Aile-D ile Aile-Y'nin açıları ve ekran üzerindeki izdüşüm adımları bu yüzden farklıdır. Ekranın aynı genişliğine:
- Aile-D bir sayıda bölüntü düşürür,
- Aile-Y **başka bir** sayıda bölüntü düşürür.

Sebep saf geometri: ekrana **farklı açılarla** varıyorlar. Bir ailenin λ aralıklı yuvaları ekrana $\theta$ açısıyla değiyorsa, ekran üzerindeki iz düşüm adımı $\lambda/\sin\theta$'dir. İki aile için $\theta_D\neq\theta_Y$ ⇒ **iki farklı adım** ⇒ verniyer.

Çakışma koşulu (iki bölüntünün üst üste gelmesi):

$$\boxed{\Lambda_{saçak}=\frac{\lambda}{\lvert\sin\theta_Y-\sin\theta_D\rvert}}$$

Bu formül dalga süperpozisyonundan değil, **iki farklı adımlı cetvelin çakışma sayımından** çıkmıştır. Kumpas mantığı; optik değil.

### 10.3 Çakışmada ne oluyor? — madde 10 devreye giriyor

Verniyer tek başına "nerede" der; "ne kadar parlak" cevabını madde 10 verir:

| Durum | Mekanik | Ekran |
|---|---|---|
| **Bölüntüler çakışıyor** | Y-yörüngesi, D-yörüngesinin **alçak basınç yuvasına** düşer ⇒ madde 10 kilitlenmesi ateşlenir ⇒ yörünge birleşir, akı iki katına çıkar | **Aydınlık** |
| **Bölüntüler kaçık** | Y-yörüngesi **sıkışma cephesine** çarpar ⇒ itilir ⇒ en yakın çakışma noktasına **süpürülür** | **Karanlık — ve süpürdüğü zerreyi komşu saçağa ekler** |

> **Kontrast yükselteci:** Kaçık bölge yalnızca "yakalanmamış" değildir; **aktif olarak boşaltılır** ve boşalttığını çakışma noktasına taşır. Karanlık derinleşirken aydınlık aynı oranda parlar. Enerji muhasebesi (§8.9) kendiliğinden tutar.

### 10.4 Bu ilkenin bedavaya verdiği üç şey

**(1) "Küçülen parmaklar" (Şekil 2.8.1.2).**
Gerçek kumpasta adım oranı sabittir, çakışmalar eşit aralıklıdır. Bizde $\theta_Y$ ekranda dışa gidildikçe **büyür** ⇒ $\Lambda=\lambda/\lvert\sin\theta_Y-\sin\theta_D\rvert$ **küçülür** ⇒ saçaklar dışa doğru sıkışır ve söner. Laboratuvar kaydı ayrıca varsayılmadan çıkıyor.

**(2) Gölgede saçak yok.**
Gölgeye kıvrılan aile oraya **yalnız** gider. Tek cetvelle verniyer olmaz. Kesişecek ikinci cetvel yoksa çakışma da yoktur. (Kitabın 2.8.1'deki iddiası bu ilkenin doğrudan sonucu.)

**(3) Koheransın mekanik tanımı — beklenmedik kazanç.**
Verniyerin çalışması için iki cetvelin **ortak bir sıfır noktası** olmalıdır. Bizde bunu **madde 1** sağlar: aynı kaynaktan gelen tüm katarlar hizalıdır ⇒ iki aile aynı sıfırdan tiklenir.
⇒ **Kaynak hizalı değilse (faz-karışık) cetvellerin sıfırı rastgeledir, çakışma örgüsü kurulamaz, desen doğmaz.**
Standart fiziğin "koherans" dediği şeyin burada mekanik karşılığı budur: *ortak cetvel sıfırı*. Ayrı bir varsayım değil, madde 1'in sonucu.

### 10.5 Dürüst kayıt — sınanması gereken bağ

Verniyerde okunabilir çakışma sayısı, cetvellerin **bölüntü sayısıyla** sınırlıdır. Bizde bir paketin bölüntü sayısı $N\approx1{,}5\times10^4$ (2.6.5) ⇒ cetvel boyu $N\lambda\approx9{,}5$ mm (632,8 nm için).

⇒ **Öngörü:** İki aile arasındaki yol farkı $N\lambda$'yı aşarsa cetveller örtüşmeyi bırakır ve **desen ölür**. Bu, standart fizikteki *koherans uzunluğunun* mekanik karşılığıdır ve $N$'i doğrudan ölçülebilir bir büyüklüğe bağlar.

**Risk kaydı:** $N$ evrensel sabit alınırsa koherans uzunluğu da her kaynak için ~1 cm çıkar; oysa gerçekte kaynaktan kaynağa (termalde µm, iyi lazerde on cm) çok değişir. ⇒ **$N$ kaynak-bağımlı olmalıdır** ($N=\nu\tau$ ve $\tau$ kaynağın kopma penceresi). Bu, 9.2.7/vi açık kalemini (*dilim boyu ↔ koherans uzunluğu*) verniyer üzerinden **nicel ve sınanabilir** hâle getirir. Simülatörde $N$ kaydırıcı olmalı ve desenin $N$ ile ölmesi gösterilmelidir.

### 10.6 Simülatör algoritması (verniyer çekirdeği)

```
1. Kaynak: paralel katarlar, hepsi hizalı (madde 1). Katar içi yuva aralığı λ.
2. Her zerre için gradyan alanında entegrasyon:
     yön   ← -K·∇P            (madde 2,5 — merkezî, geçtikten sonra da açık)
     hız   ← a(x,y)=√(P/ρ)    (madde 3,4)
   Uca çarpan ⇒ teğetten yansıt (madde 6), sonra entegrasyona devam.
3. Her zerrenin biriken faz sayacı: s = ∫ds/λ_yerel   (madde 8 — yol + yavaşlama birlikte)
4. Ekranda / uçuş boyunca komşu yörünge çiftleri için:
     Δs = |s_D - s_Y| mod 1
     Δs ≈ 0      ⇒ KİLİTLEN  (yörüngeyi birleştir, akıyı topla)   → aydınlık
     Δs ≈ 0.5    ⇒ İT        (en yakın kilit noktasına süpür)      → karanlık
   Koşul: yanal mesafe < R_iz  VE  boylamsal gecikme < ℓ∥
5. Kilitlenen çiftin izi güçlenir ⇒ bir sonraki adımda daha çok yakalar (madde 10 geri beslemesi).
6. Ekran histogramı = varan zerre sayısı. Parlaklık ∝ n (doğrusal, §8.7).
```

**Kritik:** Saçak formülü koda hiçbir yerde **yazılmaz**. Adım 4'ün çıktısı olarak **çıkması gerekir**. Simülatörün sınavı budur.

---

## 11. M1 KOD DURUMU VE AÇIK SORU (Oturum 5)

**Dosya:** `M1_Tek_Kenar.html` — tek dosya, HTML5 Canvas2D, harici bağımlılık yok.

### 11.1 Çalışan kısımlar ✅

| Ne | Durum |
|---|---|
| Süreklilik (§8.9) | **Denklik tam sıfır.** Hiçbir zerre yok edilmiyor; gövdeden geri sekenler bile sahnede kalıp sahneyi terk ediyor. |
| Gradyan profili | $\delta P\propto(1-r/R)^2$ ⇒ $\vert\nabla P\vert\propto(1-r/R)$ — kullanıcının karesel profili, kitabın "doğrusal sönümlenir"ini üretiyor |
| Çift sayım yasağı | YÖN ← $\nabla P$ (yalnız dik bileşen), BÜYÜKLÜK ← $a=\sqrt{P/\rho}$ — ayrı kanallar |
| Madde 6 | Aynasal, **kurallı** yansıma; açılar temas anındaki teğetten. Saçılma yok. |
| Madde 8 | Gecikmenin iki bileşeni (yol + yavaşlama) tek sayaçta ($z.t$) |
| Geometri | DENEY 4 oranı 1:4 (kaynak→bıçak : bıçak→ekran) |
| λ | Renge bağlı; atış periyodu **tam** $\lambda/a_0$ ⇒ zerreler arası mesafe kesinlikle eşit |

### 11.2 Bulunan ve düzeltilen üç hata

1. **Atış periyodu λ'nın tam katı değildi** ⇒ ardışık rank'lar birbirine göre kaymış çıkıyordu, **cetvel sıfırı bozuluyordu** (madde 1 ihlali). Düzeltildi: periyot = $\lambda/a_0$.
2. **Yansıyan aile %2,6'da kalıyordu** ⇒ 2. cetvel yoktu. Kullanıcı teşhisi doğru çıktı, iki sebep de gerçekti:
   - Etki yarıçapı $R$ kısaydı ⇒ uca varmadan kıvrılacak mesafe yoktu
   - Zerreye **hacim verilmemişti** ⇒ teğet geçen uca değmiyordu
   Düzeltildi ($R$ uzatıldı + $r_z$ eklendi): **%17–18**.
3. **Ekrandaki tepeler sahteydi** — 40 sabit katar ayrık ışınlar üretiyordu; "saçaklar" verniyerden değil ışınların düştüğü yerlerden geliyordu. Düzeltildi: **belirlenimli katmanlı tarama** (rastgelelik değil — mekanizmada saçılma yok).

### 11.3 AÇIK SORU — madde 10'un freni nedir?

Kullanıcı kaydı: *"gerçek hayatta bıçak ile ekran arasında 8 metre var; aşağısında gözlemlemek neredeyse imkânsız."*
⇒ Yakalanma, uçuşun **tamamı** boyunca çalışmalı; iz ömrü $\ell_\parallel$ 8 m'yi kapsamalı (~5,5 s).

**Ama o değerde simülasyon çöküyor:** madde 10'un pozitif geri beslemesi (kilitlenen çiftin izi güçlenir ⇒ daha çok yakalar) **frensizdir** ve her şeyi 1–2 dev kanala yığar. Ölçüm: tepe/ortalama = 19×, aydınlık bölgede yalnız 2 yığın.

Kısa iz ömründe ($\ell_\parallel\approx1{,}1$ s) çökme olmuyor ama yakalanma yolun ancak dörtte birinde çalışıyor ve desen **geniş bir zarf + ~%30 dalgalanma** olarak kalıyor — temiz saçak katarı değil.

**Soru:** Bir wake kanalının sonsuza kadar zerre yutmasını ne engelliyor?

| Aday fren | Mekanik gerekçe | Sınanabilir sonucu |
|---|---|---|
| **A · Kanal doyması** | Tünel dolunca basınç açığı kapanır; dolu kanal artık çekmez | $\vert C\vert$ doygunluğa oturur; kanal sayısı korunur |
| **B · Geri tepki** | Yığılan zerrelerin kendi hacmi yerel basıncı yükseltir (Postülat 1: sıkıştırılabilir) | Zerre yoğunluğu → $P$ artışı → itme; öz-düzenleyici |
| **C · Kısa $\ell_\parallel$ + çok geçiş** | İz gerçekten kısa ömürlü; 8 m gereken şey yakalanma değil, **kesişmelerin olgunlaşması** | Desen mesafeyle keskinleşir ama çökme olmaz |
| **D · Kilitlenme λ-kilitli** | Yakalanma yalnız faz uyumluysa olur; uyumsuz zerre itilir ⇒ kanal seçici, doymaz | Verniyer doğrudan kanal sayısını sabitler |

**Claude'un tercihi: B + D birlikte.** B fiziksel freni verir (sıkıştırılabilirlikten, ek varsayım yok), D seçiciliği verir (verniyeri kanal mekaniğine bağlar). İkisi birlikte hem çökmeyi engeller hem saçak sayısını λ'ya kilitler.

**Kullanıcı kararı bekleniyor.** Karar verilmeden M1 tamamlanmış sayılmaz.

### 11.4 Henüz doğrulanmamış

- Saçakların **verniyerden** doğduğu (şu an geniş zarf + dalgalanma; temiz katar yok)
- "Küçülen parmaklar" eğilimi (ölçüm var ama gürültülü, tepe bulucu kararsız)
- $\kappa\to0$ kontrolü (desen ölmeli) — fren sorusu çözülmeden anlamlı değil

---

## 11. M1 SONRASI AÇIK İKİ SORU (Oturum 5 sonu)

### S-1. İkinci cetvel hangisi? — yansıyanlar mı, kendi aralarında kesişen bükülenler mi?

Kodlama sırasında ortaya çıktı: mekanizmada **iki ayrı ikinci-cetvel adayı** var ve ikisi de senin maddelerinden çıkıyor.

| Aday | Kaynağı | Gücü |
|---|---|---|
| **(A) Yansıyan aile** | Madde 6 — uçtan sekip düz sürünün içine dalanlar | Ayarlanabilir: %2 ↔ %20. Ama gerçekte uç düzlemi çok dar olduğundan doğal payı **küçük** |
| **(B) Bükülen düzenli katarların kendi aralarında kesişmesi** | Madde 9 — katar içi hiza korunurken her katar $b$ uzaklığının belirlediği farklı $\theta(b)$ açısını kazanır ve katar aralıkları daralır ⇒ düzenli yörüngeler havada kesişir | Doğal olarak **güçlü**; rastgelelik veya saçılma gerekmez |

**Oturum 5 ara okuması:** (B) esas motor, (A) kontrast yükselteci olarak düşünülmüştü. Buradaki gerekçe düzensizlik değildi: farklı $b$ değerlerindeki hizalı katarların belirlenimli $\theta(b)$ açıları kazanması ve aralıklarının daralmasıydı. Bu ara motor yorumu daha sonra v3 sınavlarıyla revize edilmiştir; güncel karar §14.7/8'dedir.

Bu doğruysa, `w`'yi gerçekçi biçimde küçük tutabilir ve deseni yine de alabiliriz — w yalnızca kontrastı ayarlar. **Onay gerekiyor.**

### S-2. Saçak aralığı neden düzgün sıkışmıyor?

Ölçüm 16 → 14 px veriyor: yön doğru (dışa doğru sıkışıyor) ama zayıf ve desen düzensiz. Üç aday sebep:

i. **Kesişme açısı yeterince değişmiyor.** $\Lambda=\lambda/(2\sin\alpha)$; $\alpha$ ekranda çok az değişiyorsa aralık da çok az değişir. Çare: gradyan profilinin uzaklıkla daha keskin düşmesi ($n$ büyütmek) ya da $R$ küçültmek.
ii. **λ ızgarada sınırda çözülüyor.** λ=14 px, hücre=2 px ⇒ 7 hücre/λ. Yeterli ama bol değil; damganın dik yönde ±$R_{iz}$ yayılması fazı biraz bulandırıyor olabilir.
iii. **Kostikler saçakları bastırıyor.** Yörüngelerin yığıldığı katlanma noktaları (kostik) saçaklardan daha parlak; ölçüm bunları saçak sanıyor.

**Sıradaki iş:** S-1 kararlaştıktan sonra, w'yi küçültüp (B)'yi yalnız başına sınamak ve aralık eğrisini $\alpha(y)$ ile karşılaştırmak.

---

## 12. S-1 KAPANDI: MOTOR (B)'DİR — ÇİFT KONTROL (Oturum 6)

**Kullanıcı kararı:** *"B esas motor, w'yi kıs ve tek başına sına."*

### 12.1 Sınav 1 — uç düzlemi taraması

Aynı geometri (R=180, $K_p$=2,0, ışın 450/90), yalnız $w$ değişti; her koşum 1100 kare:

| $w$ | Yansıyan aile | Saçak | Uca yakın aralık | Dıştaki aralık | Eğilim | Tepe/ort |
|---|---|---|---|---|---|---|
| 160 px | %13,8 | 11 | 14 px | 16 px | ↑ açılıyor ✗ | 9,21 |
| 40 px | %2,8 | 12 | 126 px | 46 px | ↓ **sıkışıyor ✓** | 10,25 |
| 10 px | %2,8 | 14 | 98 px | 12 px | ↓ **sıkışıyor ✓** | 10,83 |
| 2 px | **%0** | 8 | 102 px | 16 px | ↓ **sıkışıyor ✓** | 13,32 |

**Beklenenin tersi çıktı.** Uç düzlemini büyütmek deseni iyileştirmiyor — **bozuyor**. w=160'ta saçak sayısı düşüyor, kontrast düşüyor ve "küçülen parmaklar" eğilimi **terse dönüyor**. Yansıyan aile, kalabalıklaştığında (B)'nin ördüğü verniyeri yıkayan bir gürültü kaynağına dönüşüyor.

**Yansıma tam %0 iken bile desen yaşıyor ve en temiz hâlinde.** ⇒ **Motor (B)'dir: bükülen yörüngelerin kendi aralarında kesişmesi.** (A) yalnızca ikincil bir katkıdır ve fazlası zararlıdır.

### 12.2 Sınav 2 — kilitlenme kontrolü (κ = 0)

Aynı geometri, $w$=2 px, yansıma %0:

| κ | Saçak (aydınlık) | Gölgede saçak |
|---|---|---|
| 1,0 | **8** | 2 (yalnız sınır kostiği) |
| **0,0** | **YOK (–)** | **0** |

Kilitlenme kapatıldığında desen **tamamen kayboluyor**. ⇒ Saçaklar salt yörünge katlanmasının (kostik) yan ürünü **değildir**; **madde 10'un iz-yakalaması zorunlu bileşendir**. Verniyerin "çakışmada kilitlen, kaçıkta itil" kararı olmadan ekranda desen doğmuyor.

### 12.3 Bunun kitaba anlamı

| Kayıt | Sonuç |
|---|---|
| **Madde 10'un statüsü** | Kullanıcının *"en önemli mekanizma"* nitelemesi **sayıyla doğrulandı**: κ=0'da desen yok. |
| **Madde 6'nın statüsü (Oturum 6 ara sonucu; geçersiz)** | Bu oturumda yansımanın saçakların kaynağı olmadığı düşünülmüştü. v3 sınavları bu sonucu geçersiz kıldı; güncel kararda aydınlık kesişmenin kaynaklarından biri yansıyan ailedir (§14.7/8). |
| **Madde 9'un statüsü** | Katarların hizası ve düzeni korunur. Deseni besleyen geometrik değişim; katar aralıklarının daralması ve her katarın $b$ uzaklığına bağlı belirli $\theta(b)$ açısını kazanmasıdır. |
| **Gölge** | Derin gölge temiz kalıyor (yalnız sınır kostiği). 2.8.1'in *"gölgede girişim olmaz"* iddiası üretildi ✓ |
| **Süreklilik** | Denklik her koşumda tam **0**. Kayıpsızlık bir tez değil, kimlik ✓ |

### 12.4 Yerleşen varsayılanlar (saf-B kurulumu)

λ=633 nm (14 px) · $g_0$=0,36 · n=2 · **R=180** · **w=10** · **$r_z$=3** · k=0,55 · $R_{iz}$=15 · $\ell_\parallel$=1,10 s · **κ=1,0** · **$K_p$=2,0** · katar=34 · ışın=450/90

Sonuç: **8 saçak, 106 px → 16 px (güçlü sıkışma ✓), denklik 0, gölge temiz.**

### 12.5 Kalan açık kalem

**S-2 (aralık eğrisi):** sıkışma artık güçlü ve monoton, ama $\Lambda(y)=\lambda/(2\sin\alpha(y))$ ile **nicel** karşılaştırma yapılmadı. Simülatörden $\alpha(y)$'yi (varış açısı dağılımı) çıkarıp ölçülen aralıkla yan yana koymak, 9.9.8/i'ye doğrudan sayısal katkı olur. **Sıradaki iş bu.**

**İz ömrü freni:** $\ell_\parallel$ 8 m'nin tamamını kapsayacak kadar (~5,5 s) büyütülürse madde 10'un geri beslemesi frensiz kalıp her şeyi 1–2 dev kanala çökertiyor. Fiziksel frenin ne olduğu (viskoz sönüm mü, kanal doygunluğu mu) **açık soru**.

---

## 12. ANİMASYON 2.8.1'İN İNCELENMESİ VE İKİ DÜZELTME (Oturum 6)

Kaynak: `Gorseller/image_tek_kenar_kirinim_anim_final.gif` — 1200×600, 97 kare. Kareler ayıklanıp incelendi.

### 12.1 Animasyonun gösterdiği yapı

| Gözlem | Sonucu |
|---|---|
| Basınç eğrileri **tam olarak SİVRİ UÇTA merkezlenmiş eş-merkezli daireler** | Alanın kaynağı bıçak konturu değil, **uç noktasıdır** |
| Bıçak = yukarı bakan üçgen; gövde yalnız çarpışma cismi | Gövde alan üretmiyor |
| 15 zerre **dikey, kusursuz hizalı** bir saf hâlinde çıkıyor | Madde 1'in birebir görselleştirmesi |
| Işın **tamamen gölge sınırının üstünde** | Bıçağın kestiği alt bant yok |
| Yörüngeler havada **çaprazlama kesişiyor** (belirgin X deseni) | Madde 10'un ön koşulu |
| Ekrandaki varış sırası **belirlenimli olarak yeniden dizilmiş**: yukarıdan aşağı 15,14,13,12,11,10, **3**, **4**, 9,8,7,6,5 | Uca çarpıp şahlanan 3–4, kazandıkları zorunlu açıyla 9 ile 10 arasına giriyor; rastgele saçılma yok |
| 5–8 gölge sınırının **altına** iniyor | En yakın geçenler gölgeye derin dalıyor |
| Ekranda her zerre farklı büyüklükte glow bırakıyor | En parlak 12'de ve 8–9 civarında |

### 12.2 DÜZELTME 1 — alanın merkezi (Claude'un hatası)

Kullanıcı **madde 5**'te açıkça yazmıştı: *"bıçak sivri ucunu merkez kabul edersek…"*
Claude alanı **bıçak konturundan** (en yakın yüzey noktasından) hesaplamıştı. Animasyon bunun yanlış olduğunu gösteriyor: eğriler uçta merkezli.

**Düzeltildi:** `fieldAt()` artık uç noktasından radyal; $d$, uç düzlem yarı-genişliği $w/2$'de doygunluğa oturuyor (tekillik yok). Gövde yalnız çarpışma. Bu, madde 5'in "yaklaşırken de uzaklaşırken de uca doğru" simetrik saçılma yörüngesini doğrudan üretir.

### 12.3 DÜZELTME 2 — ikinci cetvel yansıyan aile DEĞİL (kullanıcı bulgusu)

Kullanıcının kendi koştuğu iki kontrol:

| Kontrol | Sonuç | Anlamı |
|---|---|---|
| $\kappa\to0$ (kilitlenme kapalı) | Desen **tamamen ölüyor** | Madde 10 zorunlu. Desen bir **kostik değil** — saf balistik odaklanma olsaydı κ'dan bağımsız olurdu |
| $w\to2$ px ⇒ yansıma %0 | Desen **yaşıyor** | Saçakları yansıyan aile üretmiyor |

⇒ **§9.3(a) ve §10.1'deki "Aile-D × Aile-Y" okuması yanlıştı.**
İki cetvel, düz aile ile yansıyan aile değil; **farklı miktarda bükülmüş yörüngelerin kendi aralarındaki kesişmesidir.** Her çarpma parametresi farklı bir sapma açısı ve farklı bir gecikme verdiğinden, bükülme yelpazesi **sürekli bir cetvel ailesi** üretir; kesiştikleri her yerde verniyer koşulu kurulur.

Kitabın kendi cümlesi zaten bunu söylüyordu (2.8.1): *"zerreler havada birbirlerinin yörüngelerini çaprazlama kesmektedir"* — Claude bunu madde 6'ya (yansımaya) fazla yüklemişti.

**Madde 6'nın gerçek rolü küçülmüyor ama değişiyor:** yansıyanlar deseni *kurmuyor*; varış sırasını **karıştırıyorlar** (animasyonda 3–4'ün 9–10 arasına girmesi) ve kesişme sayısını artırıyorlar.

### 12.4 Güncel durum

- Uç-merkezli alan çalışıyor, çökme yok, yakalanma yörüngesi oluşmuyor.
- Aydınlık tarafta çok tepeli yapı var, "dışa doğru sıkışıyor" ölçümü ✓ veriyor; ama tepe/ortalama hâlâ yüksek (12×) — §11.3'teki **fren sorusu açık.**
- Muhasebe denkliği ±0'a çok yakın (elle koşumda ufak çift sayım gürültüsü var, gerçek kayıp yok).

**Sıradaki iş:** §11.3'ün fren kararı. Bu verilmeden saçak sayısı belirlenemez.

---

## 14. DEVAM NOKTASI — BURADAN SÜRDÜR (16 Ağu 2026, Oturum 7 sonu)

> **Bu bölüm, yeni bir oturumun sıfırdan devam edebilmesi için gereken HER ŞEYİ içerir.**
> Okuma sırası: §14 (bu bölüm) → §9 (10 madde sözleşmesi) → §10 (verniyer) → Oturum 7 günlüğü.

### 14.1 Dosya envanteri

| Dosya | Durum |
|---|---|
| `M1_Tek_KenarChat.html` | **v4 "Gerçek Ölçek"** — aktif geliştirme dosyası. Tek dosya, saf Canvas2D, bağımlılık yok. |
| `00_TARTISMA_KAYDI_CHAT.md` | Aktif tartışma ve karar kaydı. |
| `M1_Tek_KenarChat_BASLANGIC_YEDEGI_2026-08-16.html` | v4 dönüşümünden hemen önce alınmış, SHA-256 ile kaynakla birebir doğrulanmış başlangıç yedeği. **Dokunulmayacak.** |
| `M1_Tek_Kenar.html` / `00_TARTISMA_KAYDI.md` | Kullanıcının eski yedekleri. **Dokunulmayacak.** |

### 14.2 v3 mimarisi — özet sözleşme

- **Fizik çekirdeği** HTML içinde `/*==CORE==*/ ... /*==CORE-END==*/` işaretleri arasında, **DOM'suz** (saf JS). UI/çizim ayrı script bloğu. Çekirdek konsoldan bağımsız sınanabilir.
- **Zerre düz uçar** (yön vektörü `dx,dy`; salınım terimi YOK — λ, katardaki aralıktır, madde 1).
- Yön yalnız **3 belirlenimci olayda** değişir:
  1. **Gradyan kavisi:** `δP∝(1−r/R)²` (kullanıcı: pulsasyon ⇒ n=2 ⇒ kuvvet doğrusal, 2.8.1 ile tutarlı); yön←∇P dik bileşeni, büyüklük←`a=a₀√((1−g)/(1−k·g))` (çift sayım yasağı).
  2. **Uçtan yansıma:** teğetten aynasal + **şahlanma** `rot(−refBoost)` (kısa-ekran telafisi; bilerek, ekranda ilan ediliyor). Uç etiketi bandı: `su.ny<−0.05` (köşe sekmeleri dahil → Aile-Y).
  3. **İz benimseme (madde 10):** saf takip — hedef yön = **öncünün GÜNCEL yönü** (izin anlık tanjantı DEĞİL); düzeltme `corr=−adopt·0.05·e`, klamp **±0.22 rad** (bırakma eşiği cos>0.97'nin İÇİNDE olmak zorunda).
- **Kilit kapıları (hepsi birden):** `align>0.5` (yuva hizası) ∧ `cosA>0.99` (iz istikameti) ∧ `cosD>0.995` (öncü güncel yönü) ∧ `lat<λ/4` (yuvanın içine düşmüş) ∧ `own.fam===z.fam` (**aynı aile** — demet-içi takip).
- **İtme (S-manevrası):** `align<−0.35` → 0.35 s kavis+karşı-kavis (yarı 0.175'te işaret döner) ⇒ net dönüş 0, yalnız yanal şerit kayması; sonra `imm=0.30` bağışıklık.
- **Fren kuralı:** kilitli zerre **iz bırakmaz** (tüneli tazeler, açmaz) — mega-kanal çökmesinin freni; §12.5 sorusuna cevap adayı, kitaba aday içgörü.
- **Verniyer fazı:** `ph = z.t·ν` (madde 8: yol+yavaşlama tek sayaçta); iz noktasında okuma boyuna-enterpolasyonlu: `phHere = p.ph − lon/λ`.
- **Atış:** periyot tam `λ/a₀`; rank tick-içi yaş ofsetiyle doğar (`spawn(age)`, `x0=SRC+age·a₀`) ⇒ λ-aralık hatası 0.000 px.
- **Muhasebe:** zerre asla yok edilmez; gövdeye çarpan geri seker (`fam=3`, sayaç bilgi amaçlı); denklik `fired−(hit+exit+live)=0` her koşumda.

### 14.3 Güncel varsayılanlar (kod içindeki P bloğu)

```
nm:633  lamX:1  tScale:1  trains:48
g0:0.36  nExp:2  R:180  Kp:3.5  k:0.55
Riz:10  life:1.40  kap:1.0  adopt:1.8
w:60  rz:5  refBoost:0.35(≈20°)
beamU:300  beamD:60
```
Presetler — **Anlatı:** lamX 7, tScale 0.30, trains 12, beam 240/50, Riz 26, life 2.6 (açılış modu; wake/yörünge/numara açık). **İstatistik:** lamX 1, tScale 1, trains 48, beam 300/60, Riz 10, life 1.40 (wake açık-seyreltilmiş, yörünge/numara kapalı).

**Kurulum kuralları (ihlal edilirse fizik bozulur):**
- `R < beamU` — yoksa "hiç kıvrılmayan" Aile-D doğmaz (madde 7), verniyerin 1. cetveli kaybolur.
- `Riz < λ` — yakalama menzili şerit aralığını aşarsa verniyer çözülemez, mega-kanal çöker.
- Klamp(0.22) < bırakma eşiği(≈0.245 rad) — yoksa "gir-dön-düş-eğik kal" sızıntısı geri gelir.

### 14.4 Sınav durumu (Oturum 7 kapanışı, İstatistik modu, 1300 kare)

| Sınav | Değer | Durum |
|---|---|---|
| λ-aralık hatası | 0.000 px | ✓ |
| Serbest bölge düzlüğü | **maxSapma ≈ 300 px, max\|dy\|≈0.75 (azınlık ~%5)** | ✗ **AÇIK SORUN #1** |
| Denklik | 0 | ✓ |
| NaN/Inf | 0 | ✓ |
| Aydınlıkta saçak | 12 | ✓ |
| Aralık eğilimi | 40→28 px dışa sıkışıyor | ✓ (nicel karşılaştırma yapılmadı) |
| Gölgede saçak | 5–7 (sınır kostiği + taşma) | ⚠ izlenecek |
| Yansıyan aile | ~%15 (Y=623–704) | ✓ hedefte |
| κ=0 kontrolü | saçak 11 kalıyor, t/o 4.9'a düşüyor | ⚠ **AÇIK SORUN #2** |

### 14.5 Açık sorunlar — tam teşhis durumu

**#1 Düzlük sızıntısı (öncelik):** Serbest bölgede (b>R+40) fam=0 azınlık kümesi ~300 px'e kadar sapıyor. **Beş kök bulunup kapatıldı** (Oturum 7 tablosu: köşe-etiket kaçağı, tanjant kopyası, Riz>katar-aralığı, klamp-eşik uyumsuzluğu, çapraz-aile bulaşı) — her seferinde sapan küme küçüldü ama sızıntı sürüyor. **Kalan baş şüpheliler:**
   a. S-manevrasının kesintiye uğradığı yollar (manevra ortasında bıçak teması / ekran varışı / kilit geçişi → yarım kavis net dönüş bırakır).
   b. Kilit bırakma anındaki artık `corr` eğikliği (≤12.6°) — zincirleme birikim.
   **Planlanan izolasyon:** koda `pushOn` / `lockOn` ayrı ablasyon anahtarları ekle; 4 kombinasyonda (00/01/10/11) düzlük ölç → suçlu tek koşumda ayrışır. (Slider gerekmez; P içinde boolean yeter.)

**#2 κ-testinin yeni anlamı:** v2'deki "κ=0 ⇒ desen ölür" bulgusu v2 kusuruymuş. v3'te κ=0'da **balistik yoğunlaşma tarağı** (11 tepe, t/o 4.9) kalıyor; κ=1 deseni λ-düzenine sokuyor (t/o düşük ama saçaklar λ-kilitli). **Ayrıştırma işi:** iki desenin tepe-aralık dağılımını karşılaştır — balistik tarak geometrik-kaotik aralıklı, verniyer deseni λ-taraklı olmalı. Bu ayrım kitap için de değerli: "kostik değil verniyer" iddiasının sayısal kanıtı.

**#3 (bekleyen) Λ(y) nicel sınavı:** ölçülen saçak aralığını `λ/(2sinα(y))` ile karşılaştır (α = iki ailenin yerel kesişme yarı-açısı; simülatörden ölçülebilir). 9.9.8/i'ye doğrudan katkı. Düzlük çözülmeden anlamlı değil.

### 14.6 Sınav düzeneği (kopyala-yapıştır)

Tarayıcı konsolunda / javascript_exec ile — **STA** kümesi ve koşum kalıbı:

```js
const STA={lamX:1,tScale:1,trains:48,beamU:300,beamD:60,Riz:10,life:1.40,
           R:180,Kp:3.5,k:0.55,w:60,rz:5,refBoost:0.35,adopt:1.8};
function run(cfg,frames){ Object.assign(P,cfg); reset();
  for(let f=0;f<frames;f++) tick(1/60);
  return {m:computeMeasure(), bal:fired-(hitScreen+exited+zerre.length)}; }
// desen:   run({...STA,kap:1},1300)  → m.sacak, m.yakin, m.dis, m.egilim, m.golge, m.tepeOrt
// ablasyon: run({...STA,kap:0},1300)
// düzlük:  STA+kap=1 ile 450 kare koş; b=TIP_Y-y0>R+40 & fam===0 zerrelerde
//          max|z.y-y0| ve max|z.dy| (y0=top+(id-1)·st, st=(beamU+beamD)/(trains-1))
```
`computeMeasure()` saf veri döndürür: `{sacak, golge, tepeOrt, yakin, dis, egilim}`.

### 14.7 Kullanıcı kararları defteri (bugüne kadar, kronolojik)

1. Önce **tek kenar** — her şey orada temelleniyor.
2. **10 madde** (§9.1) + bıçak ucu zerre ölçeğinde **dar bir düzlemdir**.
3. **Verniyer ilkesi** (§10) — saçaklar kendiliğinden, iki farklı adımlı cetvelin çakışması.
4. Gradyan profili **(1−r/R)²** — pulsasyon kökenli.
5. Uç düzlemi ve yakalama **ayarlanabilir** (kaydırıcı) olacak.
6. **Zerreler arası mesafe kesinlikle eşit; yalnız renkle değişir** → atış tam λ/a₀, λ↔renk kaydırıcısı.
7. "Yansıyan zerreler çok olmalı ki girişim oluşsun" → yansıma alanı geniş.
8. (Ara karar "B esas motor, w kıs" — v2'nin kusurlu κ-testine dayanıyordu; v3'te **revize**: aydınlık kesişmenin kaynağı yansıyan aile, kitap 2.8.1 ile uyumlu. Kayıt: §12'nin sonucu geçersiz, Oturum 7 geçerli.)
9. **Zerreler dalgalanmaz, düz gider; tam düzen, saçılma yok** → v3 FSM mimarisi.
10. Zerreleri küçült; katar sayısını artırmadan yaklaştır; wake belirgin; **yansıma açısını kısa ekran için bilerek artır** (refBoost); **kapılma güçlü** (adopt↑).
11. Animasyonlardaki görsel dil esas: numaralı az zerre + iz tüpü halkaları + kesikli yörünge (Anlatı modu bu yüzden açılış modu).
12. **Katar düzeni bıçaktan sonra bozulmaz:** davranışı katarın bıçağa uzaklığı $b$ belirler; katar içindeki Zerre hizası ve $\lambda$ aralığı korunur. Katarlar arası mesafe daralır ve her katar $b$'nin belirlediği kesin açıyı kazanır. Rastgele saçılma yoktur. Hedef, DENEY 4'teki aydınlık tarafta dışa doğru daralan ve sönen **"küçülen parmaklar"** desenidir.

### 14.8 Çalışma yöntemi (Fable oturumları için)

- **Browser'ı kendiliğinden koşma** — kullanıcı isterse ya da doğrulama koşumu tek-toplu yapılacaksa (biriktir-ve-tek-koşum). Bu oturumda doğrulamalar tek javascript_exec çağrılarında toplandı.
- Sistemde **node/deno/bun YOK** — başsız JS sınavı çalışmaz; çekirdek sınavı tarayıcı konsolundan `/*==CORE==*/` sayesinde yapılır (§14.6).
- Her mekanizma değişikliği: önce bu dosyaya karar/teşhis, sonra kod, sonra tek toplu sınav, sonra günlüğe sonuç.
- **Saçak formülü koda asla yazılmaz** — desen çıktıdır; sınav budur.
- Terminoloji kilidi §5'te; foton yok, kütle-itim, c değişken.

### 14.9 Sıradaki işler (öncelik sırasıyla)

1. **Ablasyon anahtarları** (`pushOn`,`lockOn`) → düzlük sızıntısı #1'in suçlusunu 4-kombinasyon koşumuyla izole et.
2. Suçluya göre cerrahi düzeltme (aday: S-manevra kesinti telafisi — manevra yarıda kesilirse kalan karşı-kavisi uygula; veya bırakmada `corr` artığını geri sar).
3. Düzlük ✓ olunca: **κ=0 vs κ=1 tepe-aralık dağılımı** karşılaştırması (#2) — "balistik tarak vs λ-verniyer" ayrımının sayısal kanıtı.
4. **Λ(y) ↔ λ/(2sinα(y))** nicel sınavı (#3) → 9.9.8/i'ye rapor edilebilir ilk sonuç.
5. Kullanıcı görsel onayı → M2 (tek yarık = iki karşılıklı kenar; aynı çekirdek, ikinci bıçak aynalı).
6. M3 (çift yarık) → `Δy=λL/d` ÇIKTI olarak sınanacak (§2.5'in üç muhasebe sayısı: tepe 4n₀, çukur 0, ortalama 2n₀).

## 15. GERÇEK DENEY–EKRAN ÖLÇEK UÇURUMU (16 Ağu 2026, kullanıcı fizik hatırlatması)

> **Kullanıcı:** Simülasyon ile gerçek deney arasındaki boyut farkları hedef desenin mekanizmayla oluşmasını engelliyor. Gerçek ölçüler fizik motorunda korunmalı; görünürlük için yapılan büyütmeler fiziğe karışmamalıdır.

### 15.1 Gerçek düzenek ile mevcut görünür temsil arasındaki fark

| Büyüklük | Gerçek deney | Mevcut görünür temsil | Sorun |
|---|---:|---:|---|
| Bıçak → ekran uçuşu | **8 m** | Ekranda yaklaşık **15 cm** | Uzun uçuşta gelişmesi gereken küçük açı farkları ve yörünge kesişmeleri sıkıştırılıyor. |
| Zerre katarı demeti genişliği | **0,5 mm** | Ekranda yaklaşık **5 cm** | Demet, uçuş yoluna göre binlerce kat fazla geniş gösteriliyor. |
| Katar sayısı | 0,5 mm içinde **binlerce katar** | Anlatı modunda yalnız **12 katar** | Sürekli ve sık katar örgüsü birkaç ayrık çizgiye indirgeniyor; sahte tarak/kostik üretme riski var. |
| Katar içi ardışık Zerre aralığı | yaklaşık **650 nm** | Ekranda yaklaşık **5 cm** | Wake yuvalarının periyodu aşırı büyütülüyor; fiziksel gecikme/λ oranı değişiyor. |
| Bıçak gradyanının etki mesafesi | yaklaşık **2 cm** | Piksel tabanlı ve uçuşa göre aşırı büyük | Gerçekte Zerre yalnız bu 2 cm'lik bölgede bükülür ve yavaşlar; sonrasında 8 m serbest uçuş yapar. |
| Wake'e kapılma | Yansıma ve yavaşlamanın oluşturduğu gecikme, hemen arkadaki Zerrelerin öncünün wake'ine düşmesini sağlar | Görünür λ ve kısa uçuş nedeniyle gerekli boylamsal gecikme oranı oluşmuyor | Mevcut motor yakalamayı fiziksel gecikmeden üretmek yerine eşiklerle zorlamaya yatkın. |

Gerçek düzeneğin temel oranları:

$$\frac{L}{R_g}=\frac{8\,\mathrm{m}}{0{,}02\,\mathrm{m}}=400,$$

$$\frac{B}{R_g}=\frac{0{,}0005\,\mathrm{m}}{0{,}02\,\mathrm{m}}=0{,}025,$$

$$\frac{\lambda}{B}=\frac{650\times10^{-9}\,\mathrm{m}}{0{,}5\times10^{-3}\,\mathrm{m}}\approx1{,}3\times10^{-3}.$$

Mevcut Canvas bu üç oranı aynı anda korumuyor. Bu nedenle yalnız bütün sahneyi piksele ölçekleyerek gerçek mekanizma üretilemez.

### 15.2 Çözüm kararı — fizik ölçeği ile çizim ölçeği ayrılacak

Simülatör bundan sonra üç ayrı katman taşımalıdır:

1. **Fizik koordinatları (SI):** Hesaplar metre ve saniye ile yapılır. Temel değerler `L=8 m`, `B=0.5 mm`, `R_g=2 cm`, `λ≈650 nm` olur. Canvas pikseli hiçbir fizik denklemine girmez.
2. **Sayısal temsil:** Binlerce katarın tamamını görünür nokta olarak çizmek yerine, demet genişliği boyunca yüzlerce/binlerce örnek katar kullanılır. Her örnek katar bir akı ağırlığı taşır. Yakınsama sınavı 256→512→1024→2048 katarla yapılır; desen örnek sayısı arttıkça değişmemelidir.
3. **Görselleştirme dönüşümü:** Zerre yarıçapı, wake halkası ve λ çizgileri yalnız görünürlük için büyütülür. Bu büyütmeler yörünge, gecikme, faz veya yakalanma hesabını değiştirmez ve ekranda açıkça “görsel büyütme” olarak ilan edilir.

### 15.3 Tek Canvas yerine üç ölçekli görünüm

- **Yakın alan paneli (±2 cm):** Bıçak gradyanı içinde bükülme, yavaşlama, yansıma ve gecikmenin doğuşu büyütülerek gösterilir.
- **8 m uçuş paneli:** Gradyan sonrasında yörüngeler olaylar arasında analitik/doğrusal ilerletilir; 8 metre milyonlarca küçük zaman adımıyla yürütülmez. Katarların kazandığı açı ve aralık daralması korunur.
- **Ekran/histogram paneli:** Aydınlık taraftaki dışa doğru daralan ve sönen “küçülen parmaklar” gerçek akı ağırlıklarıyla biriktirilir.

Bu paneller farklı büyütme kullanabilir; fakat fizik motoru tektir. Görüntü dönüşümü fiziği değiştirmez.

### 15.4 Wake yakalanmasının yeni hesaplanma biçimi

650 nm aralıklı bütün Zerreleri ayrı ayrı ekranda çizmek mümkün ve gerekli değildir. Her katar için boylamsal gecikme fiziksel uzunluk olarak biriktirilir:

$$\Delta \ell_{eq}=\big(\ell-\ell_0\big)+a_0\int\left(\frac{1}{a(x,y)}-\frac{1}{a_0}\right)ds.$$

Ardından bu gecikme görünür piksele değil gerçek $\lambda$'ya bölünür:

$$q=\frac{\Delta \ell_{eq}}{\lambda}.$$

- `q` tam yuvaya yaklaşıyorsa arkadaki Zerre öncünün wake kanalına düşer.
- Gecikmenin hangi mesafede yakalanma oluşturduğu, katarın bıçağa uzaklığı $b$, yansıma, hız kaybı ve yol uzamasından **çıktı** olmalıdır.
- `lamX`, Zerre büyüklüğü ve wake halka çapı gibi görünürlük ayarları `q` hesabını asla değiştirmemelidir.
- Katar içindeki ardışık Zerrelerin gerçek $\lambda$ aralığı ve hizası korunur; rastgele başlangıç veya saçılma eklenmez.

### 15.5 İki çalışma modu

| Mod | Amaç | Kural |
|---|---|---|
| **Anlatı görünümü** | 12 kadar seçili katarı, Zerreleri ve wake'i gözle izletmek | Semboller büyütülebilir; sonuç panelinde bunun fiziksel ölçek olmadığı açıkça yazılır. Fizik hesabı yine gerçek ölçek motorundan okunur. |
| **Gerçek ölçek / sınav** | DENEY 4'ün 0,5 mm + 2 cm + 8 m geometrisini ve binlerce katarın akısını hesaplamak | Görünür Zerre aralığı kullanılmaz; ağırlıklı yoğun örnekleme, gerçek gecikme/λ ve ekran histogramı kullanılır. |

### 15.6 Uygulama sırası — önce ölçek mimarisi

1. Piksel tabanlı `A0`, `R`, `beamU/beamD`, `lamPx()` fiziğini dondur; bunları yalnız eski anlatı görünümü olarak tut.
2. SI tabanlı `REAL={L:8, beam:0.0005, gradR:0.02, lambda:650e-9}` fizik durumunu ekle.
3. Bıçağın ±2 cm yakın alanında $b\mapsto\{\theta,\Delta\ell_{eq},a_{min},family\}$ çıkış haritasını belirlenimli olarak hesapla.
4. Çıkış durumlarını 8 m boyunca analitik ilerlet; yalnız yörünge/wake karşılaşmalarında olay çöz.
5. Binlerce katarı ağırlıklı örnekle; 12 görünür katar yalnız bu yoğun çözümden seçilen temsilciler olsun.
6. `q=Δ\ell_{eq}/λ` ile wake yakalanmasını sınayıp, aydınlık tarafta dışa doğru daralan ve sönen parmakları histogramdan üret.
7. 256→2048 katar yakınsaması, denklik, gölgede saçak yokluğu ve λ/L/R duyarlılık sınavlarını geçir.

**Yeni öncelik kararı:** §14.9'daki düzlük ablasyonları eski piksel motorunun teşhisidir; yararlı olmakla birlikte ana çözüm değildir. Önce fizik–çizim ölçeği ayrılacak. Aksi hâlde 15 cm'lik görünür sahnede 8 m, 2 cm, 0,5 mm ve 650 nm aynı motor biriminde temsil edilmeye çalışıldığı için eşikler sürekli birbirini bozar.

---

## 7. OTURUM GÜNLÜĞÜ

### 16 Ağustos 2026 — Oturum 1
- Klasör açıldı: `websitesi/CALISMA/GirisimSimularor/`
- Kitabın girişim bölümleri okundu (2.2.3, 2.6.5, 2.7, 2.8, 5.2, 9.3, 9.9).
- Mekanizma özeti çıkarıldı (§2), tartışma konuları açıldı (§3), modül planı taslağı yazıldı (§4).
- **Kod yazılmadı.**

### 16 Ağustos 2026 — Oturum 2
- **Kullanıcı direktifi:** *"Standart bilimin açıklamalarını unut. Tamamen akışkanlar mekaniği. Önce burada anlaşalım."*
- §3'teki T-1 ve T-2 optik iskeleye yaslandığı için **iptal edildi**; yerine §8 (Saf Akışkanlar Mekaniği Çerçevesi) yazıldı.
- Girişim, tek bir akışkan cümlesine indirildi: **iki $\lambda$-periyotlu basınç oluğunun $2\alpha$ açıyla kesişmesinden doğan duran alçak-basınç vadileri** ($\Lambda=\lambda/2\sin\alpha$).
- Bu birleştirme Michelson, çift yarık ve tek kenarı **tek mekanizmaya** indirdi; tek kenarda $\alpha=\alpha(y)$ olduğu için saçak sıkışması (Şekil 2.8.1.2'deki "küçülen parmaklar") kendiliğinden çıktı.
- Parlaklık, süreklilik denkleminden ($nv=$ sabit) türetildi — ayrıca varsayılmıyor.
- Yeni ayırt edici öngörü açıldı: **yanal wake yarıçapı $R_\perp$** ve $d>R_\perp$'de desen ölümü.
- **Kod yazılmadı.** 4 çatalda (§8.12) kullanıcı onayı bekleniyor.

### 16 Ağustos 2026 — Oturum 3
- **Kullanıcı kararı:** Önce **tek kenar (bıçak)** — *"her şey orada temelleniyor."*
- Kullanıcı, tek kenar mekanizmasını **10 maddede** tanımladı + bıçak ucunun zerre ölçeğinde **dar bir düzlem** olduğu notunu düştü. §9'a kaydedildi; simülatörün çekirdek sözleşmesi budur.
- Claude'un maddelerden okuduğu üç ince nokta: (5) merkezî çekici alan ⇒ bükme kapanma noktasından **sonra da** sürer; (6) geliş/yansıma açıları **temas anındaki teğetten** ölçülür; (8) gecikme **iki bileşenli** (yol uzunluğu + hız kaybı).
- Claude **11. madde** önerdi: periyodikliğin kaynağı = izin **λ-yuvalı** olması. $\Delta s\equiv0\ (\mathrm{mod}\ \lambda)$ ⇒ yuvaya düşüp kilitlenir (aydınlık); $\Delta s\equiv\lambda/2$ ⇒ sıkışma cephesine çarpıp **itilir** (karanlık — aktif boşaltma).
- Madde 6 yükseltildi: uçtan yansıyan zerreler, aydınlık alandaki saçak ailesinin **kaynağıdır**; gölgede partner olmadığı için gölgede saçak yoktur.
- Uç düzlem genişliği $w$'nin rolü belirlendi: **yansıyan ailenin tek kapısı** ⇒ saçak kontrastını belirler.
- 7 sayısal parametre kalemi açıldı (§9.4). **Kod yazılmadı.**

### 16 Ağustos 2026 — Oturum 4
- **Kullanıcı, mekanizmanın kilit taşını verdi: VERNİYER İLKESİ.** Aynı genişlikte farklı sayıda bölüntü taşıyan iki cetvel ⇒ çakışmalar **kendiliğinden periyodiktir**. §10'a kaydedildi.
- Claude'un §8.6 (moiré) ve §9.3 (λ-yuva) önerileri bu ilkenin altında **birleştirildi**: *katar = cetvel, λ-yuvaları = bölüntüler*; adım farkı iki ailenin ekrana **farklı açıyla** varmasından doğuyor.
- Saçak bağıntısı $\Lambda=\lambda/\lvert\sin\theta_Y-\sin\theta_D\rvert$ **çakışma sayımından** çıkarıldı — dalga süperpozisyonundan değil.
- Üç kazanım tespit edildi: (1) "küçülen parmaklar" $\theta_Y$'nin dışa doğru büyümesinden çıkıyor; (2) gölgede tek cetvel var, verniyer kurulamıyor ⇒ saçak yok; (3) **koheransın mekanik tanımı = iki cetvelin ortak sıfırı = madde 1**.
- Dürüst risk kaydı: $N$ evrensel alınırsa koherans uzunluğu her kaynakta ~1 cm çıkar; gerçekte çok değişir ⇒ **$N=\nu\tau$ kaynak-bağımlı olmalı**. 9.2.7/vi bu yolla nicelleşiyor.
- Simülatör çekirdek algoritması yazıldı (§10.6). **Kural: saçak formülü koda yazılmaz, çıktı olarak çıkar.**
- **Kod yazılmadı.** §9.4'teki 7 parametre hâlâ sayı bekliyor.

### 16 Ağustos 2026 — Oturum 5 · M1 KODLANDI
**Kullanıcı kararları:**
- **P-1 profil:** $\delta P\propto(1-r/R)^2$ — gerekçe: *"gradyanı pulsasyon doğurmuştur."*
  → Türevi $|\nabla P|\propto(1-r/R)$ : **kuvvet doğrusal** ⇒ 2.8.1'in *"doğrusal olarak sönümlenir"* cümlesiyle birebir. İç tutarlılık doğrulandı.
- **P-3 uç düzlemi:** gözlem için geniş tutulacak; yansıma alanı da geniş olmalı.
- **P-6 yakalama:** *"zerre boyutlarında bile olsa kesiştikleri yerde diğer zerre o ize kapılacaktır"* ⇒ kesişmede yakalanma **kesin**.
- **Hepsi kaydırıcı olacak.**
- **λ kilidi:** *"zerreler arası mesafe kesinlikle eşit; ancak renk değişiminde değişebilir."*
  → Atış periyodu tam $\lambda/a_0$; hiçbir rank atlanmaz; λ doğrudan **renge** bağlandı (400–700 nm kaydırıcısı).
- **Yansıma yetersiz uyarısı:** *"ya yansıma alanı çok dar ya da bıçağa varmadan kıvrılma çok az; yansıyan zerreler çok olmalı ki girişim oluşsun."*
- **Kullanıcı kodu düzeltti:** gövdeye çarpan zerre **yok edilmiyor, geri sekiyor** (teoride hiçbir zerre yok olmaz) + **$r_z$ zerre yarıçapı** eklendi (katı damlanın hacmi ⇒ teğet geçen de uca değer) + R 260'a çıkarıldı.

**Dosya:** `M1_Tek_Kenar.html` (tek dosya, saf Canvas2D, harici bağımlılık yok)

**Süpürme sonuçları (yansıyan aile oranı):**
| Kaldıraç | Etki |
|---|---|
| $K_p$: 1,0 → 5,2 | %2,5 → %14,9 — **bükülme zerreleri uca sürüyor; kullanıcının teşhisi doğru** |
| $w$: 15 → 130 px | %2,5 → %20,0 |
| $r_z$: 3 → 13 px | %4,9 → %7,3 |

**Bulunan kurulum kuralı (yeni):** $R < $ ışın genişliği olmalı. Aksi hâlde ışının tamamı gradyanın içinde kalır, madde 7'nin *"yeterince uzak hiç kıvrılmaz"* ailesi hiç doğmaz ve **1. cetvel (Aile-D) kaybolur** ⇒ verniyer kurulamaz. R=260, ışın=300 iken desen çöktü ve %67 zerre sahneden taştı.

**Yerleşen varsayılanlar:** λ=633 nm (14 px), $g_0$=0,36, n=2, R=180, w=160, $r_z$=8, k=0,55, $R_{iz}$=15, $\ell_\parallel$=1,10 s, κ=1,0, $K_p$=2,0, katar=34, ışın=450/90.

**İlk geçerli sonuç:**
| Sınav | Sonuç |
|---|---|
| Süreklilik (denklik) | **0 — tam** ✓ zerre yok olmuyor |
| Saçaklar aydınlık tarafta | **12 saçak** ✓ |
| Gölgede saçak | 2 (yalnız sınır kostiği) — derin gölge temiz ✓ |
| Tepe / ortalama | 5,49 × |
| Yansıyan aile | %14,1 |
| Aralık: dışa sıkışma | 16 → 14 px — **yön doğru ama zayıf** ⚠ |
| Desen düzgünlüğü | **düzensiz** ⚠ |

**Açık kalan iki soru (§11'e taşındı).**

### 16 Ağustos 2026 — Oturum 6 · S-1 KAPANDI
- **Kullanıcı kararı:** *"B esas motor, w'yi kıs ve tek başına sına."*
- İki kontrol koşturuldu (§12). Sonuç kullanıcının kararını doğruladı ve **beklenenden fazlasını verdi**:
  - $w$ küçüldükçe desen **iyileşti** (saçak ↑, kontrast ↑, sıkışma eğilimi düzeldi). Yansıma %0'da desen en temiz hâlinde.
  - **κ=0'da desen tamamen öldü** ⇒ madde 10 zorunlu; saçaklar kostik yan ürünü değil.
- **Kitaba geri besleme adayı:** 2.8.1'de yansıyan zerrelere yüklenen "girişimi başlatan" rol madde 9'a devredilmeli. Yansıma gerçek ama saçakların kaynağı değil.
- Varsayılanlar saf-B kurulumuna çekildi; `M1_Tek_Kenar.html` güncellendi.
- **Sıradaki iş:** $\Lambda(y)$ ölçümünü $\lambda/(2\sin\alpha(y))$ ile nicel karşılaştırmak (9.9.8/i'ye katkı).

### 16 Ağustos 2026 — Oturum 7 · FABLE DEVRALDI: TAM DÜZEN SÜRÜMÜ (v3)

**Kullanıcı direktifleri (sırasıyla):**
1. *"Standart bilimden kurtul. Zerreler dalgalanarak gitmez, DÜZ giderler. Düzensizlik yok, tam bir düzen var, saçılma yok."* → λ zerrenin salınımı değil, katardaki ARALIKTIR; salınım terimi tamamen söküldü.
2. *"Zerreleri küçült; katar SAYISINI artırmadan katarları yaklaştır; wake belirgin olsun; kısa ekran için yansıma açısını bilerek fazlalaştır; wake kapılması güçlü olsun."*

**Yeni mimari (kuvvet karması → olay-tabanlı sonlu durum makinesi):**
- Zerre yön vektörüyle DÜZ uçar. Yön yalnız üç belirlenimci olayda değişir:
  ① gradyan kavisi ② uçtan aynasal yansıma + **şahlanma** `refBoost` (kısa-ekran telafisi, bilerek ve İLAN EDİLEREK eklenir) ③ **iz benimseme**: saf takip (pure pursuit) — hedef yön = öncünün GÜNCEL yönü; kuvvet yok, salınım yok.
- **Verniyer kararı tek noktada:** yuva hizasıysa (align>+0,5) KİLİTLEN; zıt hizaysa (align<−0,35) **S-manevrasıyla** şerit değiştir (kavis+karşı-kavis ⇒ net dönüş SIFIR, yalnız yanal kayma ≈ λ/2 mertebesi).
- Atış periyodu tam λ/a₀ + tick-içi yaş ofseti ⇒ **λ-aralık hatası 0,000 px** (sınandı).
- Fizik çekirdeği DOM'suz (`/*==CORE==*/` işaretli) — başsız sınanabilir.

**Bu oturumda bulunup kapatılan kök nedenler (beşli zincir):**
| # | Kök neden | Çare |
|---|---|---|
| 1 | Tam benimseme geniş açıyla kesen ize de uygulanıyordu → yansıyanın peşine katar kaskadı (330 px savrulma) | **Açı kapısı:** kilit yalnız dar açıda; geniş açıda yalnız itme |
| 2 | Kilit, izin ANLIK tanjantını kopyalıyordu → S-kıvrımlar zincirle bulaşıyordu | Hedef yön = öncünün GÜNCEL yönü |
| 3 | **Riz > katar aralığı** + "kilitliyken iz bırakma" freni birleşince kendi kanal izi kayboldu, komşu katar kilidi katarları birleştirdi | **Yuva-içi kilit:** yanal hata < λ/4; Riz < λ kuralı (Riz=10) |
| 4 | Takip düzeltme klampı (±28°) bırakma eşiğinin (14°) DIŞINDAydı → gir-dön-düş-eğik kal sızıntısı | Klamp 0,22 rad (12,6°) — eşiğin içinde |
| 5 | Çapraz-aile kilidi eğikliği bulaştırıyordu | Kilit yalnız AYNI aile içinde (demet-içi takip, 2.7.2); aileler arası etkileşim = verniyer İTMESİ |
| + | Uç düzlem KÖŞESİNDEN sığ sekenler (ny∈(−0,35,−0,05)) etiketsiz kalıp kapılardan sızıyordu | Uç etiketi bandı genişletildi (ny<−0,05) |
| + | İtme kavisi net 26° dönüş bırakıyordu | S-manevrası: net dönüş 0 |

**Mega-kanal freni (§12.5 açık sorusuna cevap adayı):** kilitli zerre iz bırakmaz — tünelde giden tüneli TAZELER, yeni tünel açmaz. Kanal çekiciliği öncü sayısıyla sınırlı kalır; frensiz çökme durdu. (Kitaba aday içgörü.)

**Güncel durum (İstatistik modu, 1300 kare):**
| Sınav | Sonuç |
|---|---|
| λ-aralık / muhasebe / NaN | **0,000 px · denklik 0 · temiz** ✓ |
| Saçak (aydınlıkta) | **12**, aralık 40→28 px **dışa sıkışıyor** ✓ |
| Yansıyan aile | ~%15 (w=60, refBoost=20°) |
| κ=0 kontrolü | Saçak 11 kalıyor ama **karakter değişiyor** (t/o 4,9'a düşüyor; kilitsiz desen = salt balistik yoğunlaşma tarağı). κ-testinin eski "desen tamamen ölür" okuması v2'nin kusuruymuş; v3'te dürüst kayıt: kilit deseni λ-düzenine sokuyor, yokluğunda kaba tarak kalıyor. **Ayrıştırma açık iş.** |
| **Serbest bölge düzlüğü** | **HÂLÂ KIRIK:** azınlık bir küme (~%5) 300 px'e kadar sapıyor, max|dy|≈0,75. Beş kök kapatıldı, sızıntı sürüyor — kalan baş şüpheli: S-manevranın kesintiye uğradığı durumlar ve/veya kilit-bırakma anındaki artık eğiklik. **Sıradaki iş: itme-ablasyonu** (itmeyi tek başına kapatan anahtar) ile izole etmek. |

**Görsel:** kitap GIF dili (numaralı zerreler, kesikli yörünge, iz-tüpü halkaları, mor basınç konturu); Anlatı/İstatistik presetleri; zerreler küçüldü, katarlar yaklaştı (beam 300/60), wake halkaları belirginleşti (α=0,45, 22 halka).

### 16 Ağustos 2026 — Oturum 8 · DEVAM NOKTASI KONSOLİDASYONU
- Kullanıcı talebi: *"Kaldığımız yerden devam edebilecek şekilde tartışma dosyasına her şeyi kaydet."*
- **§14 DEVAM NOKTASI** yazıldı: dosya envanteri, v3 mimari sözleşmesi, güncel varsayılanlar + kurulum kuralları, sınav durumu tablosu, 3 açık sorunun tam teşhis durumu, kopyala-yapıştır sınav düzeneği, 11 maddelik kullanıcı kararları defteri, Fable çalışma yöntemi, 6 adımlık öncelikli iş kuyruğu.
- Önemli düzeltme kaydı: §12'nin "B tek başına motor" sonucu **geçersiz** ilan edildi (v2'nin kusurlu κ-testine dayanıyordu); geçerli okuma Oturum 7 + §14.7/8.
- Kod değişikliği yapılmadı. Sıradaki iş: §14.9/1 — ablasyon anahtarlarıyla düzlük sızıntısının izolasyonu.

### 16 Ağustos 2026 — Oturum 9 · M1 v4 GERÇEK ÖLÇEK MOTORU

**Kullanıcı fizik hatırlatması:** Gerçek 8 m uçuş, 0,5 mm demet, 2 cm gradyan, yaklaşık 650 nm katar-içi Zerre aralığı ve binlerce katar tek Canvas/piksel ölçeğinde temsil edilemez. Wake yakalanması da kısa ekran ve görünür λ ile doğru gecikmeyi üretemez. Bu teşhis ve çözüm sözleşmesi §15'e kaydedildi.

**Güvenlik/yedek:** `M1_Tek_KenarChat_BASLANGIC_YEDEGI_2026-08-16.html` oluşturuldu ve aktif dosyayla SHA-256 özeti birebir doğrulandı. Kullanıcının `M1_Tek_Kenar.html` ve `00_TARTISMA_KAYDI.md` yedeklerine dokunulmadı.

**v4 mimarisi:** 
- Fizik ile çizim ayrıldı. Motor metre cinsinden `L=8 m`, `beam=0,5 mm`, `R_g=2 cm`, `λ=650 nm` kullanıyor; piksel yalnız görüntü dönüşümüdür.
- Yakın alan sivri uç merkezli gradyanda 640 adımla çözülüyor. Her katar için $b\mapsto\{\theta,\Delta\ell_{eq},aile\}$ belirlenimli çıkıyor.
- Gradyan sonrasındaki 8 m, olaylar arasında analitik ilerletiliyor.
- Varsayılan 2.048 sayısal katar örneği, ağırlıklarıyla 8.192 fiziksel katarı temsil ediyor. Anlatıdaki 12 görünür katar yalnız bu yoğun çözümden seçilmiş temsilciler.
- Wake yuvası `q=Δ\ell_{eq}/λ` ile okunuyor. En yakın tam yuvaya taşıma kütleyi yok etmiyor; ekran histogramı yalnız varan ağırlıktan oluşuyor. Saçak formülü koda yazılmadı.
- Üç ayrı görünüm: 4 cm yakın alan (dikey büyütülmüş), gerçek 8 m uçuş (yatay sıkıştırılmış), ekran/birikim. Her panelde ölçek büyütmesi açıkça ilan ediliyor.

**Varsayılan sınav (2.048 örnek):**

| Ölçüm | Sonuç |
|---|---:|
| Düz/düzenli D | **7.792** |
| Uçtan yansıyan Y | **244** |
| Gölgeye kıvrılan K | **156** |
| Eşdeğer gecikme | **1,401–1,415 mm** |
| Wake sayacı | **2.155,1–2.176,2 λ** |
| Etkin aydınlık kanal | **21** |
| Uca yakın → dış kanal aralığı | **29,31 → 9,96 µm** (dışa doğru küçülüyor ✓) |
| Tepe / ortalama, κ=0,94 | **4,70×** |
| Gölgede periyodik kanal | **0** |
| Zerre denkliği | **0,000000** |
| Tarayıcı hata/uyarı | **0** |

**Ablasyon:** $κ=0$ iken etkin kanal **0**, tepe/ortalama **1,54×**, denklik 0. $κ=0,94$ iken etkin kanal **21**, tepe/ortalama **4,70×**. Böylece parmak kontrastı salt ayrık katar çizgilerinden değil, gerçek gecikme/λ wake yakalamasından geliyor.

**Yakınsama:** 2.048→4.096 örnekte kanal sayısı **21**, aralık **29,31→9,96 µm**, dışa küçülme ve denklik **aynı** kaldı; tepe/ortalama 4,70×→4,58× değişti. Desen örnek ızgarasının sahte tarağı değildir.
