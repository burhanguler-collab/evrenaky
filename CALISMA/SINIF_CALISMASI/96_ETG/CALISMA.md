# 96_ETG — Erken tip galaksiler: fit **yapılamayan** sınav · Çalışma dosyası

> ### ⚡ NİHAİ KURULUM (1 Ağustos 2026 · karar: [86_NIHAI](../86_NIHAI/CALISMA.md))
>
> Bu dosyanın analizi **eski (A) kurulumla** yapıldı ve tarihsel kayıt olarak duruyor.
> Nihai kurulum: yerel $\ell_\omega$ + $a_0=1{,}75\times cH_0/16{,}1$. Nihai sayılar: ETG dış nokta medyan artık **−0,008 dex** (eski −0,090) — ΛCDM'in +0,045'inden **iyi**. Panel nihai $a_0$ ile yenilendi.


**16 galaksi · 32 ivme noktası · referans: Lelli, McGaugh, Schombert & Pawlowski 2016, ApJ 836, 152
— *"One Law to Rule Them All: The Radial Acceleration Relation of Galaxies"***

Hesap: `../../etg_sinavi.py` · Panel: `../../kur_etkilesimli_etg.py`
Çıktılar: [`SONUC.csv`](SONUC.csv) · [`YONTEM.md`](YONTEM.md) · [`etg.png`](etg.png) ·
**[`panel.html`](panel.html) ← etkileşimli**

> ### ▶ Etkileşimli panel — [`panel.html`](panel.html)
>
> Radyal ivme düzlemi, arka planda **2693 disk noktası**. Bu dosyadaki her dürüstlük kaydı bir
> düğmeye bağlıdır. Tek dosya, dış bağımlılığı yok.
>
> | Düğme | Neyi gösterir | İlgili madde |
> |---|---|---|
> | **Nokta kümesi** | iç / dış / ikisi — tablo canlı değişir | md. 3, md. 7.5 |
> | **$a_0$ çarpanı kaydıracı** | ×0,5 – ×4,2 canlı; "gereken çarpana git" (sayısal çözüm) | md. 2 |
> | **Υ\* kaydıracı** (0,40 – 1,00) | **panelin asıl fikri** — ΛCDM oynar, teori kıpırdamaz | md. 5 |
> | **Disk RAR bulutu** | seçili kümenin ivme aralığı sarı şeritle işaretlenir | md. 2 |
> | **F4 payı göstergesi** | gereken $a_0$'ın okunabilir olup olmadığını söyler | md. 3 |
> | **Galaksi listesi** (16) | seçilenin ölçüm↔öngörü bağı ve girdileri T/S/Ö/**K** rozetleriyle | — |
>
> **Υ\* düğmesini deneyin.** 0,40'tan 1,00'e kaydırdığınızda ΛCDM'in dış nokta medyanı
> $+0{,}027 \to +0{,}069$ dex arası oynar; teorininki **$-0{,}090$'da sabit kalır.** Sebep
> ekranda yazılı: teori $g_{bar}$'ı ölçüm olarak alır, ΛCDM yarıçabı ondan geri kurmak zorundadır.
>
> **K rozeti bu panele özgüdür:** "yeniden kurulmuş — ölçüm değil". Yarıçap, $M_*$, $M_{200}$,
> $c_{200}$ ve $a_{DM}$ bu rozeti taşır. Teori tarafında **tek bir K rozeti yoktur.**
>
> Panel, teorinin aleyhine olan sonuçları da basar: iç nokta seçilince kötü koşullanma uyarısı,
> dış noktada ΛCDM önde olduğunda **kırmızı uyarı** çıkar (md. 5).
>
> *Doğrulandı:* panelin ürettiği bütün ölçütler `etg_sinavi.py` çıktısıyla birebir aynı
> (dış ×1,85 · iç ×14,56 · ikisi ×3,64 · disk 1553 nokta ×1,76 · ΛCDM +0,045/0,139).

---

## 0. Bu sınav neden diğerlerinden farklı

Disk çalışmalarında (01–06) her galaksinin 6–60 noktalı dönüş eğrisi vardı ve "$\Upsilon_*$
fitlendi mi" sorusu sürekli açıktı. Burada o soru **tanımsızdır:**

| | Disk çalışması | Bu sınav |
|---|---|---|
| Galaksi başına veri | 6–60 noktalı eğri | **2 ivme noktası** |
| Serbest parametre uydurulabilir mi | evet ($\Upsilon_*$, $M_{200}$, $b$, $R_f$…) | **hayır — 2 nokta, 0 serbestlik** |
| Teorinin öngörüsünde geçen büyüklükler | $\Upsilon_*$, $R$, $M$, ayrıştırma | **hiçbiri** |

Veri, HI halkasının **iç** ve **dış** kenarında ölçülmüş iki ivmeden ibarettir. Teori ne diyorsa o
çıkar; ayar yapılacak yer yoktur.

## 1. Öngörü yarıçapı içermez — türetimde sadeleşir

M-37 merkezcil dengesi tam radyal ivmeyi iki terimli verir:

$$a_{tam} = \underbrace{a_{bar}}_{F1} + \underbrace{\frac{\mathcal{G}M}{\ell_\omega R}}_{F4}$$

$\ell_\omega=\sqrt{\mathcal{G}M/a_0}$ konur ve $\mathcal{G}M = a_{bar}R^2$ yazılırsa **$R$
sadeleşir:**

$$\boxed{\;g_{öng} = g_{bar} + \sqrt{g_{bar}\,a_0}\;}$$

Formülde ne yarıçap, ne $\Upsilon_*$, ne kütle var. $g_{bar}$ **ölçülen** büyüklüktür (Lelli+2017
fotometriden hesaplamıştır) ve F1'in ta kendisidir. Bu, teorinin **en çıplak hâlidir.**

---

## 2. Sonuç 1 — ETG'ler disklerin **üstüne** düşüyor, teori ikisini birden veriyor

| Küme | n | medyan dex | saçılma | gereken $a_0$ |
|---|---|---|---|---|
| **ETG dış nokta** (HI halkasının dışı) | 16 | $-0{,}090$ | 0,153 | **×1,85** |
| — aynı ivme aralığındaki **disk** noktaları | 1553 | $-0{,}077$ | 0,132 | **×1,76** |
| ETG iç nokta | 16 | $-0{,}122$ | 0,210 | (×14,56 — *okunmaz*, md. 3) |
| — aynı ivme aralığındaki **disk** noktaları | 195 | $+0{,}058$ | 0,105 | (×0,07 — *okunmaz*) |
| Disk RAR tümü | 2693 | $-0{,}060$ | 0,146 | ×1,61 |

**Dış noktada ETG ile disk arasındaki fark 0,013 dex'tir.** Yani binde üç hız. 16 erken tip
galaksi, 1553 disk noktasıyla **aynı yasaya** uyuyor ve teori ikisini de tek formülle, sıfır
serbest parametreyle veriyor. Lelli+2017'nin başlığındaki "tek yasa" iddiası, Evrenakı'nın
kurulumunda **kendiliğinden** çıkıyor.

### Ve altı bağımsız ölçüm aynı bandı veriyor

| Ölçüm | Veri | gereken $a_0$ |
|---|---|---|
| **ETG dış nokta** ← bu sınav | 16 nokta, fit yok | **×1,85** |
| disk RAR, aynı ivme aralığı | 1553 nokta | ×1,76 |
| disk RAR, tümü | 2693 nokta | ×1,61 |
| BTFR sınavı ([97_BTFR](../97_BTFR/CALISMA.md)) | 121 galaksi | ×2,02 |
| sınıf çalışması | 141 galaksi | ×2,21 |
| kitabın 6.5.4.5 kaydı | dönüş eğrileri | ×2,26 |

**Bant: ×1,61 – ×2,26.** *(Sınıf değeri önce ×1,70 yazılmıştı; o sayı naif
$10^{-4\Delta}$ formülünden geliyordu. Sayısal çözümle ×2,21 — band değişmedi, sınıf
değeri kitabın ×2,26'sına yaklaştı.)* Bunlar birbirinden bağımsız veri kümeleri, bağımsız gözlem türleri
(ivme / hız / eğri) ve bağımsız yöntemler. Hepsi tek sayıya işaret ediyor. Bu, $a_0$'ın
kalibrasyonunun **sistematik olarak %70–130 düşük** olduğunu söylüyor — ve tutarlı biçimde.

---

## 3. Sonuç 2 — "Gereken $a_0$" iç noktada **anlamsız bir sayıdır**

İç nokta ×14,56 istiyor. Bu sayı grafikte **bilerek yoktur.** Nedeni:

$$\frac{\partial \log g_{öng}}{\partial \log k} = \frac{1}{2}\cdot\frac{F4}{g_{bar}+F4}$$

| | F4'ün öngörüye katkısı |
|---|---|
| iç nokta | **0,10** |
| dış nokta | **0,52** |

İç noktada öngörünün **%90'ı Newton terimidir.** $a_0$'ın orada neredeyse hiç kaldıracı yoktur;
küçük bir açığı kapatmak için devasa bir çarpan gerekir. Bu, $a_0$ hakkında değil, **kötü
koşullanmış bir tersine çözüm** hakkında bilgi verir. Aynı sebeple disk RAR'ı da aynı aralıkta
×0,07 "istiyor" — iki saçma sayı, tek sebep.

**Kural olarak yazılsın:** gereken $a_0$ çarpanı, yalnız F4'ün payının anlamlı olduğu
($\gtrsim 0{,}3$) rejimde raporlanmalıdır.

---

## 4. Sonuç 3 — İç noktadaki açığı teori değil, **girdi** açıklıyor

İç noktada beklentim tersine çıktı. Bekliyordum: $M_{kaps}<M_{top}$ olduğu için $\ell_\omega$
olduğundan küçük alınır, F4 fazla hesaplanır, iç nokta **pozitif** sapmalı olmalı. Ölçülen:

| | medyan sapma |
|---|---|
| iç nokta | $-0{,}122$ dex |
| dış nokta | $-0{,}090$ dex |
| fark | $\mathbf{-0{,}031}$ dex — **ters yönde** |

Yani kapsanan-kütle yaklaşımı bu açığı **açıklamıyor.** Ama iki şey birlikte okununca kaynak
belli oluyor:

1. **ΛCDM de aynı açığı veriyor** (iç noktada $-0{,}155$ dex). İki bağımsız model aynı yönde
   aynı büyüklükte şaşıyorsa, sorun modellerde değil **ortak girdidedir.**
2. Aynı ivme aralığındaki disk noktaları $+0{,}058$ dex veriyor, yani **ters işaretli.**
   ETG'lerin iç noktaları disklere göre 0,18 dex yukarıda duruyor.

Ortak girdi $g_{bar}$'dır ve iç nokta neredeyse saf Newton rejimi olduğu için $g_{bar}$ orada
doğrudan $\Upsilon_* L$'dir. Açığı kapatan kayma $+0{,}122$ dex, yani $\Upsilon_*$ 0,70 yerine
**0,93.** Erken tip galaksilerin yıldız nüfusu disklerinkinden yaşlıdır ve 3,6 µm'de daha yüksek
$\Upsilon_*$ beklenir — **yön doğru.**

> **Ama bu bir açıklama, savunma değil.** Rapor edilen bütün sayılar **yayınlanmış** $g_{bar}$
> iledir. $\Upsilon_*$'ı 0,93'e çekmek bir **fit** olurdu ve bu sınavın tek üstünlüğünü —
> fit yapılamaz olmasını — yok ederdi. Yapılmadı ve yapılmamalıdır.

---

## 5. Sonuç 4 — ΛCDM dış noktada **daha iyi**. Bu satır aleyhtedir.

| | iç (16) | dış (16) |
|---|---|---|
| TEORİ medyan | $-0{,}122$ | $-0{,}090$ |
| **ΛCDM medyan** | $-0{,}155$ | $\mathbf{+0{,}045}$ |
| TEORİ saçılma | 0,210 | 0,153 |
| **ΛCDM saçılma** | 0,213 | $\mathbf{0{,}139}$ |
| *32 noktanın tamamı — saçılma* | *TEORİ 0,184* | *ΛCDM 0,191* |

**Dış noktada ΛCDM hem medyanda hem saçılmada teoriyi geçiyor.** Bu sonuç silinmedi,
yumuşatılmadı ve grafikte duruyor.

Teorinin bu tabloda tek kazancı yöntemseldir ve şudur: **ΛCDM bu sayıyı üretmek için yarıçapı
geri kurmak ve $\Upsilon_*$ seçmek zorundaydı; teori hiçbirini kullanmadı.** ΛCDM'in dış nokta
medyanı $\Upsilon_*$ ile $+0{,}027 \to +0{,}069$ arasında oynuyor; teorininki **hiç oynamıyor**
($-0{,}090$, sabit), çünkü $g_{bar}$ ölçülmüş bir büyüklüktür. Bu bir doğruluk üstünlüğü değil,
**sağlamlık** üstünlüğüdür ve öyle sunulmalıdır.

---

## 6. Sonuç 5 — $a_0$ evrensel mi? **Ayırt edilemiyor** (zayıf lehte)

Teori $a_0$'ın evrensel olduğunu söyler → artık kütleden bağımsız olmalı. ΛCDM'de düşük ivme
davranışı hale kütlesine bağlıdır → artık kütleyle değişmeli. Bu sınav **yarıçap gerektirmez.**

| | |
|---|---|
| Spearman[artık, $\log L_{[3,6]}$] — dış nokta | $\mathbf{+0{,}10}$ |
| 32 noktanın tamamı | $+0{,}22$ |
| $L_{[3,6]}$ aralığı | 13,2 – 126,3 ×10⁹ L☉ (9,6 kat) |
| **$n=16$'da 2σ çözünürlüğü** | $\lvert\rho\rvert \approx \mathbf{0{,}52}$ |

Ölçülen değer çözünürlüğün **çok altında.** Söylenebilecek tek şey: *"sıfırdan ayırt
edilemiyor."* **"Sıfır" denemez.** 16 galaksi bu sınavı sonuçlandırmaya yetmez; daha büyük bir
ETG kümesi gerekir. Şu hâliyle: **zayıf lehte.**

---

## 7. Dürüstlük kayıtları

1. **$g_{bar}$'ın içindeki $\Upsilon_*$ bilinmiyor.** `_etg.mrt` başlığı hangi $\Upsilon_*$ ile
   hesaplandığını yazmıyor. Bütün sonuçlar yayınlanmış $g_{bar}$ ile verilmiştir; md. 4'teki
   0,93 çıkarımı bu belirsizliğe **bağlıdır** ve doğrulanmamıştır.
2. **$\mathcal{G}M=a_{bar}R^2$ adımı bir yaklaşımdır.** $\ell_\omega$'daki toplam kütle yerine
   kapsanan kütle konur. Dış noktada ($\sim 7{,}5\,R_{eff}$) bu iyi, iç noktada
   ($\sim 0{,}8\,R_{eff}$) kötüdür. Etkisi ölçüldü ve **beklenenin tersi** çıktı (md. 4) — yani
   yaklaşımın hatası, ölçülen açığın kaynağı değil.
3. **Yarıçap geri çözümü yalnız ΛCDM içindir.** $R=\sqrt{\mathcal{G}M_*/g_{bar}}$ küresel
   simetri varsayar ve gaz kütlesini içermez (bu dosyada $M_{HI}$ yok). Çıkan değerler makul
   (dış halka medyan 12,1 kpc = 7,5 $R_{eff}$; Lelli+2017 ETG halkaları tipik 5–30 kpc) ama
   **doğrulanmadı.** Teori tarafı bu adımı hiç kullanmaz.
4. **$n=16$.** Bütün korelasyon sonuçları bu örneklem büyüklüğünün çözünürlüğüyle sınırlıdır
   (md. 6). Medyan ve saçılma sayıları da 16 noktalıdır; 0,01–0,02 dex düzeyindeki farklar
   anlamlı değildir.
5. **Nokta bağımsız değil.** Aynı galaksinin iç ve dış noktası ortak mesafe, ortak eğiklik ve
   ortak fotometri hatası taşır. "32 nokta" satırları bu yüzden 32 bağımsız ölçüm **değildir**;
   iç/dış ayrımı ana tablodur, birleşik satır yalnız özet olarak durur.
6. **Disk RAR karşılaştırması aynı yayından.** Hem ETG hem disk verisi Lelli+2017'dir; ortak bir
   yöntem yanlılığı varsa ikisinde de vardır ve "0,013 dex fark" bunu göstermez.
7. **ΛCDM'in dış noktada üstün çıktığı satır (md. 5) silinmedi.** Teorinin lehine çıkan
   sonuçlarla aynı dosyada, aynı vurguyla duruyor.
8. **Bu sınav basınç-destekli sistemleri KAPSAMAZ.** Buradaki 16 galaksi HI halkası olan,
   **dönen** erken tip galaksilerdir; M-37 dairesel yörünge için kuruludur ve geçerlidir.
   Eliptiklerin yıldız kinematiği (hız dağılımı) ve cüce küreseller **hâlâ açıktır** —
   6.5.4'ün gerektirdiği iki türetim yapılmadan oraya uzanılamaz (bkz. 07_Galaktik_Yorungeler
   md. 1482–1492).

---

## 8. Ne çıktı — üç cümle

1. **Erken tip galaksiler, disklerle aynı yasaya uyuyor ve teori ikisini tek formülle veriyor.**
   Dış noktada ETG ile 1553 disk noktası arasındaki fark **0,013 dex.** Bu sonuçta fit yok,
   üstelik fit **yapılamaz.**
2. **Altı bağımsız ölçüm $a_0$ için tek bant veriyor: ×1,61 – ×2,26.** Bu sınav (×1,85) bandın
   ortasına düşüyor. Kalibrasyonun sistematik olarak düşük olduğu artık tek bir veri kümesinin
   iddiası değil.
3. **ΛCDM dış noktada teoriyi geçiyor** ($+0{,}045$ / 0,139 · teori $-0{,}090$ / 0,153) — ama
   bunu yarıçap kurulumu ve $\Upsilon_*$ seçimiyle yapıyor; teori hiçbirini kullanmıyor.

## 9. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| 1 | ETG kümesini büyüt (Lelli+2017 dışı ETG/HI halka verisi) | md. 6 — $n=16$ evrensellik sınavını sonuçlandıramıyor |
| 2 | ETG'ler için $\Upsilon_*$'ı bağımsız bir kaynaktan al, iç nokta açığını yeniden ölç | md. 4 — açıklama var, doğrulama yok |
| 3 | Gereken $a_0$ çarpanını **bütün** çalışmalarda F4-payı eşiğiyle raporla | md. 3 — kötü koşullanmış sayılar tabloya girmesin |
| 4 | ~~Disk RAR'ı kendi başına bir sınava dönüştür~~ | ✅ **yapıldı** → [95_RAR](../95_RAR/CALISMA.md) |
| 5 | Basınç-destekli köprü: (a) F1+F4'ün küresel izdüşümü, (b) $v_c \leftrightarrow \sigma$ | md. 7.8 — eliptik ve cüce küreseller bu olmadan açılamaz |

> **95_RAR bu sınavı yeniden okutuyor.** 2693 noktayla ölçüldü ki gereken $a_0$ çarpanı
> **ivmeye bağlıdır**: derin rejimde ×2,86, Newton rejiminde ×0,92. ETG dış noktalarının
> ×1,85'i ve disklerin ×1,76'sı bu eğilimin **aynı yerinde** oturuyor — yani md. 2'deki
> "0,013 dex fark" tesadüf değil, iki kümenin aynı ivme rejiminde olmasının sonucu.
> Buradaki uyum korunuyor, ama artık **daha az şaşırtıcı** olarak okunmalıdır.
