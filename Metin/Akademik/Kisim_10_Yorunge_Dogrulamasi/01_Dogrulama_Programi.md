# Kısım X — Evrenakı Yörünge Doğrulaması

## 10.1 Galaktik Doğrulama Programı

Kısım 10, Evrenakı teorisinin (Kafes Kilitlenmeli Gradyan formülasyonu) SPARC galaksi veritabanına karşı uygulanan geniş kapsamlı doğrulama programını içerir.

### 10.1.1 Amaç — fit değil, öngörü

Kısım 6'nın galaktik bölümü (6.5) teorinin denklemini **türetti** ve fitli karşılaştırmalarla sınadı. Bu kısmın sorusu farklıdır:

> **İki taraf da hiçbir şey fitlemeden, yalnız öngörü kurarak yarıştırılırsa ne olur?**

Kitapta bugüne kadar her iki model de galaksi başına parametre fitledi ve karşılaştırma "kim daha iyi uyduruyor" sorusuydu. Oysa iki tarafın da **sıfır serbest parametreli** bir öngörüsü vardır ve doğrulama programının omurgası onu kurmaktır:

| Eğri | Serbest parametre | Girdiler |
|---|---|---|
| **Evrenakı öngörüsü** | **0** | $v^2=V_{bar}^2+\sqrt{a_0\,\mathcal{G}M_{kaps}(R)}\cdot W$, $W=\min(1,a_0/g_{kaps})$ (M-47 — Kafes Kilitlenmesi); $a_0=7{,}67\times10^{-11}$ m/s² (küresel sabit); $\Upsilon_*=0{,}50$ |
| **Standart bilim öngörüsü** | **0** | $M_{200}\leftarrow$ abundance matching (Moster ve ark. 2013); $c_{200}\leftarrow$ Dutton & Macciò (2014); NFW; $\Upsilon_*=0{,}50$ |
| Evrenakı fit | 2 | $\Upsilon_*$, $b$ |
| ΛCDM fit | 2 | $\Upsilon_*$, $M_{200}$ |

*(Alt iki satır yarışçı değil, **teşhis aracıdır**: fitli koşumlar yalnız 6.5.3'ün eşit-serbestlik karşılaştırmasında ve öz-denetimde kullanılır — serbest fitin medyan $\Upsilon_*=0{,}49$ bulması, öngörünün 0,50 girdisinin bağımsız doğrulamasıdır. Bu kısmın hiçbir öngörü sonucu, paneli ve ölçek sınavı fit içermez; teorinin denkleminde galaksiye fitlenen sayı yoktur — 10.2.6.)*

Öngörülerin ikisi de **dönüş eğrisine bakılmadan** kurulur. Ortak girdi $\Upsilon_*=0{,}50$ (3,6 μm popülasyon sentezi orta değeri) — adil olması için iki tarafta aynıdır.

**Hiçbir "öngörü" saf değildir ve bu baştan kaydedilir:** Evrenakı'nın $a_0$'ı SPARC'a kalibredir (biçimi türetilmiştir — 6.5.4.3 Adım 6, 10.7); ΛCDM'in abundance matching ve $c$–$M$ ilişkileri de fitlenmiş ilişkilerdir. Bu, **kalibre öngörü ile kalibre öngörünün** karşılaştırmasıdır ve iki taraf bu bakımdan denktir.

### 10.1.2 Veri — SPARC, değiştirilmeden

Bütün dönüş eğrileri SPARC veritabanından alınmıştır (Lelli, McGaugh & Schombert 2016, AJ 152, 157): 175 disk galaksisinin Spitzer 3,6 μm fotometrisi ve yayınlanmış hata çubuklu dönüş eğrileri. Yerel `Rotmod_LTG` kümesinin dosya olarak indirilebilen ve işlenebilen tamamı **173 galaksidir** ve tamamı işlenmiştir — hiçbir galaksi seçilmemiş, hiçbir eğri değiştirilmemiştir.

Ölçek bağıntısı sınavları için üç ek yayınlanmış küme kullanılır: radyal ivme bağıntısının 2693 noktası ve 16 erken tip galaksinin ivme halkaları (Lelli ve ark. 2017), farklı hız tanımlı BTFR kataloğu (Lelli ve ark. 2019), ve teorinin ilk SPARC dışı sınavı için altı yüksek kırmızıya kayma diski (Genzel ve ark. 2017). Tam liste 10.11'dedir.

### 10.1.3 Neden sınıf sınıf

Örneklem bloğu hâlinde okunduğunda ters yönlü davranışlar birbirini götürür. Ölçülmüştür: aynı büyüklük (fitlenen $\Upsilon_*$'ın fotometrik bandın dışında kalma oranı) spiral sınıfında %44, Macellan sınıfında %91'dir. Blok ortalaması ikisini de gizler. Bu yüzden programın birinci kuralı şudur: **hiçbir sonuç blok hâlinde verilmez** — sınıf sınıf verilir, blok ortalaması yalnız yanında özet olarak durur.

Sınıflama SPARC ana kataloğunun **gerçek Hubble tipleriyle** yapılır (yapısal vekiller kullanılmaz — vekillerin 21 spiral-olmayan sistemi yanlışlıkla spiral sayıp sonuçları iyimserleştirdiği ölçülmüştür; 6.5.3.6):

| Sınıf | Tip | SPARC $T$ | Galaksi | Ölçüm noktası |
|---|---|---|---|---|
| Erken spiral | Sa – Sab | $T=1,2$ | **12** | 632 |
| Orta spiral | Sb – Sbc | $T=3,4$ | **29** | 640 |
| Geç spiral | Sc – Scd | $T=5,6$ | **30** | 730 |
| Çok geç spiral | Sd | $T=7$ | **16** | 300 |
| Macellan | Sdm – Sm | $T=8,9$ | **28** | 423 |
| Düzensiz | Im | $T=10$ | **26** | 272 |
| Karmaşık (denetim kümesi) | ayrım yapılamayanlar | — | **32** | 348 |
| ↳ S0 · BCD (uçlar) | mercek · mavi tıkız cüce | $T=0,11$ | **8** | karmaşık kümeden ayrıştırıldı |

Bir galaksi şu dört ölçütten en az birine takılırsa karmaşık kümeye gider ve gerekçesi galaksi galaksi kayıtlıdır: (1) dönüş eğrisinde $N<6$ nokta; (2) SPARC kalite bayrağı $Q=3$; (3) eğiklik $i<30°$ ($V_{obs}=V\sin i$ kötü belirlenir); (4) kendi Hubble tipinde 5'ten az galaksi kalması (S0, BCD). Karmaşık küme çöp kutusu değildir: 10.5'te ölçütlerin kendisi yansızlık denetiminden geçirilir.

### 10.1.4 Girdi–çıktı ayrımı ve rozet sistemi

Programın en önemli iç kuralı veri türü ayrımıdır: sınıf klasörlerinde yalnız **ölçülen** dönüş eğrileri ve **yayınlanmış** katalog büyüklükleri durur; bu çalışmanın hesapladığı hiçbir şey girdi klasörlerine karışmaz. Karışsaydı girdi ile çıktı ayrımı kaybolur ve sonuçlar denetlenemez hâle gelirdi.

Her sayı bir **rozet** taşır ve etkileşimli paneller bu rozetleri her galaksi için ekranda gösterir:

| Rozet | Anlamı |
|---|---|
| **T** | teoriden türetilmiş |
| **S** | gözlemle sabitlenmiş (kalibre) |
| **Ö** | o galaksinin kendi ölçümü |
| **K** | yeniden kurulmuş — ölçüm değil (yalnız ΛCDM zincirinde geçer) |

### 10.1.5 Ölçütler

- **RMS** (km/s): modelin ölçümden kök-ortalama-kare sapması, ağırlıksız.
- **$\chi^2_{ind}$**: $\chi^2/(N-k)$; öngörüler için $k=0$, fitler için $k=2$.
- **Hata çubuğu içinde**: model noktalarının ölçüm hata çubuğunun içinde kalan oranı.
- **Dış yarı sapması**: eğrinin dış yarısında $(\text{öngörü}-\text{ölçüm})/\text{ölçüm}$ medyanı — teorinin itim bütçesinin işaretli denetimi.
- **Gereken $a_0$ çarpanı**: sınıfın dış yarı sapmasını sıfırlayan küresel çarpan, **sayısal çözülür** (kapalı formül tam denklemde geçersizdir; F1 terimi ölçeklenmez).
- **Öngörü yarışı**: galaksi başına, hangi öngörünün RMS'i daha küçük.

### 10.1.6 Etkileşimli paneller (animasyonlar)

Her sınıf için (ve BTFR ile erken tip galaksiler için) tek dosyalık, dış bağımlılıksız bir etkileşimli panel üretilmiştir; her biri, ilgili bölümdeki yeşil düğmeyle **tarayıcıda ayrı sayfada, tam ekran açılır** (rahat kullanım için gömülü değildir). Panellerde galaksi galaksi gezilir (ok tuşları ve "▶ Oynat" ile sırayla animasyon), dokuz eğri katmanı (ölçüm, iki öngörü, iki fit, baryon bileşenleri) ayrı ayrı açılıp kapatılır ve **öngörünün tam olarak hangi sayılardan üretildiği** rozetleriyle okunur. Paneller kiraz toplamaya izin verir ama **topladığını gösterir**: kurulum teoriyi kayıran ya da haksız cezalandıran bir hâle getirildiğinde ekrana kırmızı uyarı basılır.

Dokuz animasyonun tamamı (ayrı sayfada açmak için tıklayın):

<ul>
<li><a href="Simulasyon/kisim10/panel_01_erken_spiral.html" target="_blank" rel="noopener">▶️ Erken spiral (Sa–Sab) — 12 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_02_orta_spiral.html" target="_blank" rel="noopener">▶️ Orta spiral (Sb–Sbc) — 29 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_03_gec_spiral.html" target="_blank" rel="noopener">▶️ Geç spiral (Sc–Scd) — 30 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_04_cok_gec_spiral.html" target="_blank" rel="noopener">▶️ Çok geç spiral (Sd) — 16 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_05_macellan.html" target="_blank" rel="noopener">▶️ Macellan (Sdm–Sm) — 28 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_06_duzensiz.html" target="_blank" rel="noopener">▶️ Düzensiz (Im) — 26 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_99_KARMASIK.html" target="_blank" rel="noopener">▶️ Karmaşık küme (denetim) — 32 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_btfr.html" target="_blank" rel="noopener">▶️ Baryonik Tully-Fisher paneli — 121 galaksi</a></li>
<li><a href="Simulasyon/kisim10/panel_etg.html" target="_blank" rel="noopener">▶️ Erken tip galaksiler paneli — 16 galaksi + 2693 disk noktası</a></li>
</ul>

### 10.1.7 Bu kısmın haritası

| Bölüm | İçerik | Çalışma kaydı |
|---|---|---|
| 10.2 | Nihai kurulum: tek denklem ve toplu defter | `86_NIHAI/` |
| 10.3 | Spiraller (Sa–Scd): üç sınıf, paneller | `01_… 02_… 03_…` |
| 10.4 | Cüceler ve düzensizler (Sd–Im): üç sınıf | `04_… 05_… 06_…` |
| 10.5 | Denetim kümesi ve uçlar (karmaşık, S0, BCD) | `99_KARMASIK/`, `07_S0_BCD/` |
| 10.6 | Ölçek bağıntıları: BTFR, radyal ivme, erken tipler | `97_BTFR/`, `95_RAR/`, `96_ETG/` |
| 10.7 | Türetim zinciri: $M_{tut}$, mikro $\ell_\omega$, $a_0$'ın biçimi, $\mathcal{G}$'nin yerelliği, tutarlılık kümesi ($N_c$, $\lambda$, σ sınavı) | `92_M_TUT/`, `94_YEREL_LOMEGA/`, `91_A0_KOPRU/`, `93_G_YEREL/`, `85_TUTARLILIK_YASASI/` |
| 10.8 | Eleme zinciri: açığın anatomisi | `89_KAFES/`, `88_TARAMA/` |
| 10.9 | SPARC dışı sınav: yüksek kırmızıya kayma | `90_YUKSEK_Z/` |
| 10.10 | Kod doğrulaması, açık kalemler ve sonuç | `98_KOD_DOGRULAMA/` |
| 10.11 | Kaynakça | `KAYNAKCA.md` |
